# -*- coding: utf-8 -*-
"""用微软 Azure Speech 预生成德语朗读音频。

用法：
    export AZURE_SPEECH_KEY=<你的密钥>
    export AZURE_SPEECH_REGION=eastasia          # 建资源时选的区域
    python3 src/make_audio.py                    # 全量生成
    python3 src/make_audio.py --voice katja      # 只生成一个音色
    python3 src/make_audio.py --dry-run          # 只统计字符数，不发请求

产物：audio/<音色>/<id>.mp3 与 audio/index.json

为什么预生成而不是运行时调接口：
  密钥不能进前端——这是个公开的单文件静态页，写进去等于公开。走服务端
  代理又会让应用不再是纯静态，且每次朗读都要联网。词表是固定的，一次性
  生成好当静态文件发，运行时既不需要密钥也不需要接口，浏览器缓存后离线可用。

字符数：约 3.1 万，Azure 免费层 F0 每月 50 万字符，一次全量只占 6%。
脚本可重复运行，已存在的文件会跳过，中断了直接再跑一次即可。
"""
import argparse, hashlib, json, os, sys, time, urllib.error, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, 'audio')
sys.path.insert(0, HERE)

# 音色：短名 → Azure 名。短名同时是目录名与前端的选项值
VOICES = {
    'katja':   ('de-DE-KatjaNeural',   '微软 Katja（女声）'),
    'conrad':  ('de-DE-ConradNeural',  '微软 Conrad（男声）'),
}
FORMAT = 'audio-24khz-48kbitrate-mono-mp3'


def texts():
    """应用里所有会被朗读的德语文本，去重。

    与 build.py 取自同一批数据源，漏了哪一条前端就会回落到系统语音——
    不会出错，但那条就享受不到微软音色。
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

    FNV-1a 64 位：实现短、Python 与 JS 都能写得一模一样。1600 条文本下
    碰撞概率约 7e-14——碰撞意味着点一个词放出另一个词的音，学习类应用里
    这属于不能接受的错误，所以不用 32 位。
    """
    h = 0xcbf29ce484222325
    for b in text.encode('utf-8'):
        h = ((h ^ b) * 0x100000001b3) & 0xFFFFFFFFFFFFFFFF
    return format(h, 'x').rjust(16, '0')


def ssml(text, voice):
    esc = (text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;'))
    return ('<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="de-DE">'
            '<voice name="%s">%s</voice></speak>' % (voice, esc))


def synth(text, voice, key, region):
    req = urllib.request.Request(
        'https://%s.tts.speech.microsoft.com/cognitiveservices/v1' % region,
        data=ssml(text, voice).encode('utf-8'),
        headers={'Ocp-Apim-Subscription-Key': key,
                 'Content-Type': 'application/ssml+xml',
                 'X-Microsoft-OutputFormat': FORMAT,
                 'User-Agent': 'flashcard-a1'})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--voice', choices=sorted(VOICES), action='append',
                    help='只生成指定音色，可重复；默认全部')
    ap.add_argument('--dry-run', action='store_true', help='只统计，不发请求')
    a = ap.parse_args()
    picked = a.voice or sorted(VOICES)

    ts = texts()
    chars = sum(len(t) for t in ts)
    print('待合成 %d 条 · %d 字符 · %d 个音色 → 共 %d 字符（免费层 50 万/月）'
          % (len(ts), chars, len(picked), chars * len(picked)))
    if a.dry_run:
        return

    key = os.environ.get('AZURE_SPEECH_KEY')
    region = os.environ.get('AZURE_SPEECH_REGION')
    if not key or not region:
        raise SystemExit('缺环境变量：先 export AZURE_SPEECH_KEY 和 AZURE_SPEECH_REGION\n'
                         '（密钥只从环境变量读，不进代码也不进仓库）')

    done_voices = []
    for short in picked:
        azure_name, label = VOICES[short]
        d = os.path.join(OUT, short)
        os.makedirs(d, exist_ok=True)
        made = skipped = failed = 0
        for i, t in enumerate(ts, 1):
            path = os.path.join(d, clip_id(t) + '.mp3')
            if os.path.exists(path) and os.path.getsize(path) > 0:
                skipped += 1
                continue
            for attempt in range(3):
                try:
                    open(path, 'wb').write(synth(t, azure_name, key, region))
                    made += 1
                    break
                except urllib.error.HTTPError as e:
                    if e.code == 429:            # 免费层限速，等一下再来
                        time.sleep(2 + attempt * 3)
                        continue
                    print('  ✗ %s [%s] %s' % (t[:30], e.code, e.reason))
                    failed += 1
                    break
                except Exception as e:
                    time.sleep(1 + attempt)
                    if attempt == 2:
                        print('  ✗ %s %s' % (t[:30], e))
                        failed += 1
            if i % 100 == 0:
                print('  %s %d/%d' % (short, i, len(ts)))
        size = sum(os.path.getsize(os.path.join(d, f)) for f in os.listdir(d))
        print('%s：新生成 %d · 已存在 %d · 失败 %d · %.1f MB'
              % (label, made, skipped, failed, size / 1048576))
        if failed < len(ts):
            done_voices.append(short)

    # 前端据此决定「发音」下拉里出不出微软选项；没生成过就不出现
    os.makedirs(OUT, exist_ok=True)
    json.dump([{'v': s, 'zh': VOICES[s][1]} for s in done_voices],
              open(os.path.join(OUT, 'index.json'), 'w', encoding='utf-8'),
              ensure_ascii=False)
    print('→ audio/index.json：%s' % ', '.join(done_voices))
    print('生成完记得重新构建：python3 src/build.py')


if __name__ == '__main__':
    main()
