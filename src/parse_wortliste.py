# -*- coding: utf-8 -*-
"""解析 Goethe A1 官方词表 PDF（A1_SD1_Wortliste_02.pdf）。

用法：python3 src/parse_wortliste.py materials/official/A1_SD1_Wortliste_02.pdf
产物：src/wortliste.json
依赖：pdftotext（poppler）

PDF 版式（pdftotext -layout 后按缩进量区分）：
    +0  主词条        die Birne, -n        Ein Kilo Birnen, bitte!
    +1  派生词条        die Bitte, -n       Ich habe noch eine Bitte.
   +20  例句续行/追加例句                    Ich warte bis morgen.
    （缩进为相对该页基准列的偏移，见 raw_lines）

名词写作「冠词 + 词 + , + 复数标记」，复数标记形如：
    -n / -e / -en / -s / -er     直接加后缀
    –  或缺省                     单复数同形
    -ä, e                        变音 + 后缀（Arbeitsplatz → Arbeitsplätze）
    -Ä                           仅变音（Apfel → Äpfel）
    -ö, er/-e                    两种复数并存
"""
import json, os, re, subprocess, sys

ART = ('der', 'die', 'das')
PAGE_FROM, PAGE_TO = 9, 27          # 字母序词表所在页
NOISE = ('Inventare', 'VS_', 'Seite ')


def raw_lines(pdf):
    """逐页产出 (相对缩进, 正文)。

    各页的左边距并不一致：第 9 页左侧多了一个「Alphabetische Wortliste」
    标题块，把整页词条推到了第 31 列，而其余页在第 15 列。所以基准列按页
    现算——取该页出现次数最多的缩进——再把缩进换算成相对值输出。
    """
    for pg in range(PAGE_FROM, PAGE_TO + 1):
        txt = subprocess.run(['pdftotext', '-layout', '-f', str(pg), '-l', str(pg), pdf, '-'],
                             capture_output=True, text=True, check=True).stdout
        lines = [l for l in txt.split('\n')
                 if l.strip() and not l.strip().startswith(NOISE)]
        if not lines:
            continue
        indents = [len(l) - len(l.lstrip()) for l in lines]
        base = max(set(indents), key=indents.count)      # 该页词条列所在的列
        for l in lines:
            ind = len(l) - len(l.lstrip())
            if ind < base:            # 左侧标题块：切掉基准列以左，剩下的才是词条
                l, ind = l[base:], base
                if not l.strip():
                    continue
            body = l.strip()
            if re.fullmatch(r'[A-ZÄÖÜ]', body):          # 字母分节标题（A / B / C …）
                continue
            yield ind - base, body


# 复数标记的合法写法（穷举，用于把词形列与例句列切开——
# 词形太长时两列之间只剩一个空格，不能靠空格数分列）
MARK = (r'–|-{1,2}'
        r'|-?[äöüÄÖÜ](?:\s*,\s*-?[a-zA-Z]+)?(?:\s*/\s*-?[a-zA-Z]+)?'
        r'|-[a-zA-Z]+')
NOUN_RE = re.compile(r'^(der/die|der|die|das)\s+([A-ZÄÖÜ][\wäöüßÄÖÜ\-]*)'
                     r'(?:\s*,\s*(' + MARK + r'))?'
                     r'(?:\s+(.*))?$')


def split_cols(body):
    """把一行拆成「词形」与「例句」两列。
    名词按复数标记的形态切；其余按 2+ 空格切。"""
    m = NOUN_RE.match(body)
    if m:
        art, word, mark, ex = m.groups()
        head = '%s %s' % (art, word) + (', %s' % mark if mark else '')
        return head, (ex or '').strip()
    parts = re.split(r'\s{2,}', body, maxsplit=1)
    return (parts[0].strip(), parts[1].strip() if len(parts) > 1 else '')


def parse_head(head):
    """词形列 → (词条, 词性, 冠词, 复数标记)"""
    m = re.match(r'^(der/die|der|die|das)\s+(.+)$', head)
    if not m:
        return head, ('verb_or_other'), None, None
    art, rest = m.group(1), m.group(2)
    art = art.split('/')[0]          # der/die Bekannte：形容词变名词，取阳性作代表
    if ',' in rest:
        word, pl = rest.split(',', 1)
        return word.strip(), 'noun', art, pl.strip()
    return rest.strip(), 'noun', art, None      # 无复数标记


def expand_plural(word, mark):
    """把复数标记展开成完整复数形式。展不开的返回 None，留待人工补。"""
    if mark is None:
        return None
    m = mark.strip()
    if m in ('–', '-', '—'):
        return word                              # 单复数同形
    if '/' in m or m.count(',') > 1:
        return None                              # 多复数形式，人工处理
    if ',' in m:                                 # 变音 + 后缀，如 "-ä, e" 或 "ä, er"（原文偶有漏写连字符）
        um, suf = [x.strip() for x in m.split(',', 1)]
        return umlaut(word, um.lstrip('-')) + suf.lstrip('-')
    if re.fullmatch(r'-?[äöüÄÖÜ]', m):           # 仅变音，如 "-Ä" / "-ü"
        return umlaut(word, m.lstrip('-'))
    if m.startswith('-'):
        return word + m[1:]
    return None


def umlaut(word, hint):
    """把词干里最后一个可变音的元音换成变音形式"""
    table = {'a': 'ä', 'o': 'ö', 'u': 'ü', 'A': 'Ä', 'O': 'Ö', 'U': 'Ü'}
    target = hint.lower() if hint and hint.lower() in 'äöü' else None
    src = {'ä': 'a', 'ö': 'o', 'ü': 'u'}.get(target)
    bases = [src] if src else ['a', 'o', 'u']
    # 德语名词首字母大写，词干元音可能就是首字母（Apfel/Arzt），大小写都要找
    cands = [(word.rfind(b), b) for b in bases] + [(word.rfind(b.upper()), b.upper()) for b in bases]
    i, base = max(cands)
    if i < 0:
        return word
    if word[i:i + 2].lower() == 'au':            # au → äu 整体替换
        return word[:i] + ('Äu' if base.isupper() else 'äu') + word[i + 2:]
    return word[:i] + table[base] + word[i + 1:]


# 官方 PDF 的排印疏漏：左边是原文写法，右边是改正后的词形列
QUELLE_FIX = {
    'die Adresse, -en': 'die Adresse, -n',    # 按原文会拼出 Adresseen
    'Satz, -ä, e':      'der Satz, -ä, e',    # 漏了冠词
    'die Lebens-':      'das Lebens-',        # 原文按复数 die Lebensmittel (pl.) 列，单数是 das
}


def merge_wrapped(entries):
    """合并被折行拆开的复合词。

    官方词表窄栏排版，长复合词会断成两行：
        der Anruf-        Wir sind im Moment nicht da. …
        beantworter       den Anrufbeantworter.
    判据不能只看结尾的连字符——Feier- / Lieblings- 是真的前缀词条。
    这里要求拼起来的整词确实出现在两条的例句里，才认定是折行。
    """
    out = []
    i = 0
    while i < len(entries):
        e = entries[i]
        nxt = entries[i + 1] if i + 1 < len(entries) else None
        if nxt and e['w'].endswith('-') and re.match(r'^[a-zäöüß]', nxt['w']):
            whole = e['w'][:-1] + nxt['w'].split()[0]
            if any(whole.lower() in x.lower() for x in e['ex'] + nxt['ex']):
                e['w'] = whole
                e['ex'] = e['ex'] + nxt['ex']
                out.append(e)
                i += 2
                continue
        out.append(e)
        i += 1
    return out


def parse(pdf):
    entries, cur = [], None
    for indent, body in raw_lines(pdf):
        if indent >= 10:                          # 例句续行或追加例句
            if cur is None:
                continue
            if cur['ex'] and body and body[0].islower():
                cur['ex'][-1] += ' ' + body       # 续行：接到上一句尾部
            elif body:
                cur['ex'].append(body)            # 追加例句
            continue
        head, ex = split_cols(body)
        if not head:
            continue
        word, pos, art, plmark = parse_head(QUELLE_FIX.get(head, head))
        cur = {'w': word, 'pos': pos, 'art': art, 'plmark': plmark,
               'pl': expand_plural(word, plmark) if pos == 'noun' else None,
               'sub': indent >= 1, 'ex': [ex] if ex else []}
        entries.append(cur)
    return merge_wrapped(entries)


if __name__ == '__main__':
    pdf = sys.argv[1] if len(sys.argv) > 1 else 'materials/official/A1_SD1_Wortliste_02.pdf'
    es = parse(pdf)
    nouns = [e for e in es if e['pos'] == 'noun']
    withpl = [e for e in nouns if e['pl']]
    noex = [e for e in es if not e['ex']]
    print('词条 %d 条（主 %d / 派生 %d）' % (len(es), sum(1 for e in es if not e['sub']),
                                        sum(1 for e in es if e['sub'])))
    print('  名词 %d，其中复数可自动展开 %d（%.0f%%）' % (len(nouns), len(withpl),
                                                100 * len(withpl) / max(len(nouns), 1)))
    print('  非名词 %d' % (len(es) - len(nouns)))
    print('  无例句 %d' % len(noex))
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'wortliste.json')
    json.dump(es, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('→ %s' % out)
