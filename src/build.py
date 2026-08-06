# -*- coding: utf-8 -*-
"""构建德语 A1 应用：把各数据源合成 DATA，注入 tpl.html 生成 index.html。

用法：python3 src/build.py
产物：项目根目录的 index.html（单文件，含内嵌字体，可离线打开）

数据来源
  wortliste.json   由 parse_wortliste.py 从官方词表 PDF 解析而来
                   （含性别、复数、例句——官方直接给全）
  aussprache.py    第 0 章发音关，手工编写
  themen.py        官方主题分组（词表第 4 页），手工整理
"""
import json, os, re, sys

BASE = 'https://flash.imyway.cn/'      # 换域名只改这一行（末尾保留斜杠）

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from aussprache import ALPHABET, REGELN, MINIMALPAARE   # noqa: E402


def logo_svg():
    return open(os.path.join(HERE, 'logo.svg'), encoding='utf-8').read().strip()


def logo_data_uri():
    from urllib.parse import quote
    return 'data:image/svg+xml,' + quote(logo_svg(), safe="/:=<>' ")


def load_woerter():
    """读入解析好的官方词表，整理成应用用的结构。

    官方词表用缩进表示派生关系（die Arbeit 挂在 arbeiten 下），
    这里把派生词并入主词条的 derived 字段，避免词表里出现两条独立的近义项。
    """
    p = os.path.join(HERE, 'wortliste.json')
    if not os.path.exists(p):
        raise SystemExit('缺 wortliste.json，先跑：python3 src/parse_wortliste.py')
    raw = json.load(open(p, encoding='utf-8'))
    out, cur, seen = [], None, {}
    for e in raw:
        item = {
            'w': e['w'],
            'pos': e['pos'],
            'art': e['art'],            # der / die / das，决定配色
            'pl': e['pl'],              # 展开后的复数，展不开为 None
            'plmark': e['plmark'],      # 官方原始标记，保留以便核对
            'ex': e['ex'],
        }
        # 少数词条在词表里出现两次（an sein / auf sein 既列在 a 处，
        # 又挂在 sein 名下）。界面按词形索引，重名会互相覆盖，这里合并例句。
        old = seen.get(item['w'])
        if old is not None:
            old['ex'] += [x for x in item['ex'] if x not in old['ex']]
            continue
        seen[item['w']] = item
        if e['sub'] and cur is not None:
            cur.setdefault('derived', []).append(item)
        else:
            out.append(item)
            cur = out[-1]
    return out


def aussprache_data():
    return {
        'alphabet': [{'l': a[0], 'ipa': a[1], 'ex': a[2], 'tip': a[3]} for a in ALPHABET],
        'regeln': [{'group': g, 'items': [
            {'rule': r[0], 'ipa': r[1], 'ex': r[2], 'zh': r[3], 'en': r[4]} for r in rules
        ]} for g, rules in REGELN],
        'paare': [{'a': p[0], 'b': p[1], 'zh': p[2]} for p in MINIMALPAARE],
    }


def check(data):
    """构建期自检：数据坏了要在这里就停住，而不是到界面上才发现"""
    w = data['woerter']
    if not w:
        raise SystemExit('词表为空')
    heads = [x['w'] for x in w] + [d['w'] for x in w for d in x.get('derived', [])]
    if len(set(heads)) != len(heads):
        import collections
        dup = [k for k, n in collections.Counter(heads).items() if n > 1]
        raise SystemExit('词条重名（BY_W 会互相覆盖）: %s' % dup)
    bad_art = [x['w'] for x in w if x['pos'] == 'noun' and x['art'] not in ('der', 'die', 'das')]
    if bad_art:
        raise SystemExit('名词缺冠词: %s' % bad_art[:5])
    # 复数若已展开，必须与单数不同（单复同形的官方标记是 –，展开后相同，属正常）
    a = data['aussprache']
    if len(a['alphabet']) < 30:
        raise SystemExit('字母表不全，应含 26 字母 + ä ö ü ß')
    dup = [p for p in a['paare'] if p['a'] == p['b']]
    if dup:
        raise SystemExit('最小对立对两侧相同: %s' % dup)
    return len(heads)   # 摊平后的总条数，与界面里的 ALL.length 一致


if __name__ == '__main__':
    woerter = load_woerter()
    data = {'woerter': woerter, 'aussprache': aussprache_data()}
    n = check(data)

    nouns = [x for x in woerter if x['pos'] == 'noun']
    tpl = open(os.path.join(HERE, 'tpl.html'), encoding='utf-8').read()
    for ph in ('__DATA__', '__BASE__'):
        assert ph in tpl, 'tpl.html 缺 %s 占位符' % ph
    html = (tpl.replace('__DATA__', json.dumps(data, ensure_ascii=False, separators=(',', ':')))
               .replace('__LOGO_URI__', logo_data_uri())
               .replace('__LOGO__', logo_svg())
               .replace('__BASE__', BASE)
               .replace('__N__', str(n)))
    dst = os.path.join(ROOT, 'index.html')
    open(dst, 'w', encoding='utf-8').write(html)
    print('built %s' % dst)
    print('  词条 %d（名词 %d，其中复数已展开 %d）'
          % (n, len(nouns), sum(1 for x in nouns if x['pl'])))
    print('  发音关：字母 %d · 规则 %d 条 · 最小对立对 %d 组'
          % (len(data['aussprache']['alphabet']),
             sum(len(g['items']) for g in data['aussprache']['regeln']),
             len(data['aussprache']['paare'])))
    print('  %d KB' % round(os.path.getsize(dst) / 1024))
