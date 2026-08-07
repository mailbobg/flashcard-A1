# -*- coding: utf-8 -*-
"""字母名发音音频生成。

优先用维基词典（Wikimedia Commons）的真人发音，取不到再用 edge-tts 纯德语
Katja 合成。真人发音比任何合成音都标准，学习字母名值得用真人。

用法：
    .venv/bin/python src/fetch_alphabet_audio.py

产物：src/alphabet_audio.json（{字母: base64 mp3}，构建时注入 __ALPH_AUDIO__）

Wikimedia 限制很严（每 ~6 个文件就会 429），脚本会自动放慢并重试；
一次跑不完可以多跑几次，已生成的（src/letters/*.mp3）会跳过。
"""
import asyncio, base64, hashlib, json, os, subprocess, sys, time
import urllib.request, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'alphabet_audio.json')
LETTERS_DIR = os.path.join(HERE, 'letters')
sys.path.insert(0, HERE)
from aussprache import ALPHABET

UA = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                    'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36'}

# 字母 → Wikimedia Commons 上的德语字母名真人发音文件
WIKI = {
    'A': 'De-A.OGG', 'B': 'Buchstabe B.ogg', 'C': 'Buchstabe C.ogg',
    'D': 'Buchstabe D.ogg', 'E': 'De-E.ogg', 'F': 'Buchstabe F.ogg',
    'G': 'Buchstabe G.ogg', 'H': 'Buchstabe H.ogg', 'I': 'Buchstabe I.ogg',
    'J': 'Buchstabe J.ogg', 'K': 'DE-K.OGG', 'L': 'De-L.OGG', 'M': 'De-M.OGG',
    'N': 'Buchstabe N.ogg', 'O': 'De-O.OGG', 'P': 'Buchstabe P.ogg',
    'Q': 'De-Q.ogg', 'R': 'De-R.ogg', 'S': 'De-S.OGG', 'T': 'Buchstabe T.ogg',
    'U': 'De-U.OGG', 'V': 'De-V.OGG', 'W': 'Buchstabe W.ogg',
    'X': 'Buchstabe X.ogg', 'Y': 'Buchstabe Y.ogg', 'Z': 'De-Z.OGG',
    'Ä': 'De-Ä.ogg', 'Ö': 'De-Ö.ogg', 'Ü': 'De-Ü.ogg', 'ß': 'De-Eszett.ogg',
}


def upload_url(fname):
    """Commons 文件直链：路径 = md5(文件名) 的前 1 / 2 字符"""
    fn = fname.replace(' ', '_')
    m = hashlib.md5(fn.encode()).hexdigest()
    return ('https://upload.wikimedia.org/wikipedia/commons/'
            + m[0] + '/' + m[0:2] + '/' + urllib.parse.quote(fn))


def fetch_wiki(letter, fname, tries=4):
    """下载真人 ogg 并转 mp3，返回 src/letters/<字母>.mp3；失败返回 None"""
    dst = os.path.join(LETTERS_DIR, letter + '.mp3')
    if os.path.exists(dst) and os.path.getsize(dst) > 3000:
        return dst
    ogg = os.path.join(LETTERS_DIR, letter + '.ogg')
    for attempt in range(tries):
        try:
            req = urllib.request.Request(upload_url(fname), headers=UA)
            with urllib.request.urlopen(req, timeout=30) as r, open(ogg, 'wb') as f:
                f.write(r.read())
            if os.path.getsize(ogg) > 3000:
                subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', ogg,
                                '-codec:a', 'libmp3lame', '-b:a', '64k', dst], check=True)
                os.remove(ogg)
                return dst
        except Exception:
            time.sleep(15 * (attempt + 1))
    return None


def gen_katja(letter, name):
    """edge-tts 纯德语 Katja 兜底（读德语标准字母名拼写）"""
    async def one():
        import edge_tts
        dst = os.path.join(LETTERS_DIR, letter + '.mp3')
        await edge_tts.Communicate(name, 'de-DE-KatjaNeural').save(dst)
        return dst
    return asyncio.run(one())


def main():
    os.makedirs(LETTERS_DIR, exist_ok=True)
    out = {}
    for letter, ipa, name, ex, tip in ALPHABET:
        dst = os.path.join(LETTERS_DIR, letter + '.mp3')
        src = None
        if os.path.exists(dst) and os.path.getsize(dst) > 3000:
            src = dst                                # 已有（真人或 Katja）
        elif letter in WIKI:
            src = fetch_wiki(letter, WIKI[letter])   # 先试真人
            if src:
                print('%s 真人' % letter)
        if not src:
            src = gen_katja(letter, name)            # Katja 兜底
            print('%s Katja' % letter)
        out[letter] = base64.b64encode(open(src, 'rb').read()).decode()
        time.sleep(2 if letter in WIKI else 0)
    json.dump(out, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False)
    print('→ %s（%d 个字母）' % (OUT, len(out)))


if __name__ == '__main__':
    main()
