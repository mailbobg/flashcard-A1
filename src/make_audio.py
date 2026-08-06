# -*- coding: utf-8 -*-
"""预生成德语朗读音频。

用法：
    python3 -m venv .venv && .venv/bin/pip install edge-tts
    .venv/bin/python src/make_audio.py --dry-run     # 只统计，不发请求
    .venv/bin/python src/make_audio.py               # 全量生成
    .venv/bin/python src/make_audio.py -v katja      # 只生成一个音色

产物：audio/<音色>/<id>.mp3 与 audio/index.json

为什么预生成而不是运行时调接口：
  Safari 与 iOS 每个 locale 只把一个音色交给网页，德语通常就只有 Anna
  一个（实测同一个 Safari 里英语 25 个、德语 1 个，因为系统只装了 de-DE
  一个德语 locale）。这在应用里绕不过去，只能自带音源。
  词表是固定的，一次性合成好当静态文件发，运行时既不依赖接口也不需要
  密钥，浏览器缓存后离线可用。

为什么用 edge-tts：
  微软 Edge「大声朗读」的接口，免费、不需要账号、德语是 neural 音质。
  它不是公开 API，将来可能失效——但只在构建期用一次，产物是静态 mp3，
  接口没了也不影响线上运行。这和「运行时依赖某个在线接口」是两回事。
"""
import argparse, asyncio, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, 'audio')
sys.path.insert(0, HERE)

# 短名 → (edge-tts 音色名, 界面上的名字)。短名同时是目录名与前端的选项值
VOICES = {
    'katja':     ('de-DE-KatjaNeural',                 'Katja（女声）'),
    'conrad':    ('de-DE-ConradNeural',                'Conrad（男声）'),
    'seraphina': ('de-DE-SeraphinaMultilingualNeural', 'Seraphina（女声 · 多语言）'),
}
CONCURRENCY = 8          # 再高容易被限流，反而更慢
RETRIES = 3


def texts():
    """应用里所有会被朗读的德语文本，去重。

    与 build.py 取自同一批数据源。漏了哪一条，前端播放时会回落到系统
    语音——不会出错，但那条享受不到好音色。
    """
    from build import load_woerter
    from aussprache import ALPHABET, REGELN, MINIMALPAARE
    out = []
    for w in load_woerter():
        for item in [w] + w.get('derived', []):
            out.append(item['w'])
            out += item['ex']
    out += [a[2] for a in ALPHABET]
    out += [x for _, rules in REGELN for r in rules for x in r[2]]
    out += [x for p in MINIMALPAARE for x in p[:2]]
    seen, uniq = set(), []
    for t in out:
        t = (t or '').strip()
        if t and t not in seen:
            seen.add(t)
            uniq.append(t)
    return uniq


def clip_id(text):
    """文本 → 文件名。前端用同样的算法算，所以不需要下发映射表。

    FNV-1a 64 位：实现短，Python 与 JS 都能写得一模一样。1600 条文本下
    碰撞概率约 7e-14——碰撞意味着点一个词放出另一个词的音，背单词应用里
    这属于不能接受的错误，所以不用 32 位。
    """
    h = 0xcbf29ce484222325
    for b in text.encode('utf-8'):
        h = ((h ^ b) * 0x100000001b3) & 0xFFFFFFFFFFFFFFFF
    return format(h, 'x').rjust(16, '0')


async def one(edge_tts, text, path, voice, sem, stats):
    async with sem:
        for attempt in range(RETRIES):
            try:
                tmp = path + '.part'
                await edge_tts.Communicate(text, voice).save(tmp)
                # 写完再改名：中断时不会留下半个文件被下次运行当成已完成
                if os.path.getsize(tmp) < 512:
                    raise ValueError('文件过小，可能是空响应')
                os.replace(tmp, path)
                stats['ok'] += 1
                return
            except Exception as e:
                if os.path.exists(path + '.part'):
                    os.unlink(path + '.part')
                if attempt == RETRIES - 1:
                    stats['fail'] += 1
                    stats['errs'].append('%s → %s' % (text[:28], e))
                else:
                    await asyncio.sleep(1.5 * (attempt + 1))


async def gen(short, ts):
    import edge_tts
    voice, label = VOICES[short]
    d = os.path.join(OUT, short)
    os.makedirs(d, exist_ok=True)
    todo = [(t, os.path.join(d, clip_id(t) + '.mp3')) for t in ts]
    todo = [(t, p) for t, p in todo if not (os.path.exists(p) and os.path.getsize(p) > 512)]
    print('%s：待生成 %d 条（已有 %d 条跳过）' % (label, len(todo), len(ts) - len(todo)))

    sem = asyncio.Semaphore(CONCURRENCY)
    stats = {'ok': 0, 'fail': 0, 'errs': []}
    tasks = [one(edge_tts, t, p, voice, sem, stats) for t, p in todo]
    for i in range(0, len(tasks), 200):
        await asyncio.gather(*tasks[i:i + 200])
        print('  %s %d/%d' % (short, min(i + 200, len(tasks)), len(tasks)))

    size = sum(os.path.getsize(os.path.join(d, f))
               for f in os.listdir(d) if f.endswith('.mp3'))
    n = len([f for f in os.listdir(d) if f.endswith('.mp3')])
    print('%s：成功 %d · 失败 %d · 共 %d 个文件 %.1f MB'
          % (label, stats['ok'], stats['fail'], n, size / 1048576))
    for e in stats['errs'][:5]:
        print('    ✗ %s' % e)
    return n == len(ts)          # 全齐了才写进 index.json


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('-v', '--voice', choices=sorted(VOICES), action='append',
                    help='只生成指定音色，可重复；默认全部')
    ap.add_argument('--dry-run', action='store_true')
    a = ap.parse_args()
    picked = a.voice or ['katja', 'conrad', 'seraphina']

    ts = texts()
    chars = sum(len(t) for t in ts)
    print('待合成 %d 条 · %d 字符 · %d 个音色' % (len(ts), chars, len(picked)))
    if a.dry_run:
        return

    done = []
    for short in picked:
        if asyncio.run(gen(short, ts)):
            done.append(short)

    # 前端据此决定「发音」下拉里出哪些选项；没生成全的不写进去，
    # 免得下拉里有选项却一半的词播不出来
    os.makedirs(OUT, exist_ok=True)
    json.dump([{'v': s, 'zh': VOICES[s][1]} for s in done],
              open(os.path.join(OUT, 'index.json'), 'w', encoding='utf-8'),
              ensure_ascii=False)
    print('→ audio/index.json：%s' % (', '.join(done) or '（无）'))
    print('生成完记得重新构建：python3 src/build.py')


if __name__ == '__main__':
    main()
