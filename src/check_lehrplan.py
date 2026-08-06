# -*- coding: utf-8 -*-
"""官方考纲条目 → 课号 的覆盖对照（依据 Prüfungsziele 第 101–106 页）"""
INVENTAR = [
 ('Verb', 'Tempus · Präsens', 3), ('Verb', 'Tempus · Perfekt（15 动词）', 7),
 ('Verb', 'Tempus · Partizipien(geöffnet)', 7), ('Verb', 'Tempus · Präteritum(war/hatte)', 7),
 ('Verb', 'Modus · Indikativ', 3), ('Verb', 'Modus · Konjunktiv II(möchte/würde)', 6),
 ('Verb', 'Modus · Imperativ', 12), ('Verb', 'Modalverben（6 个）', 6),
 ('Verb', 'trennbare Präfixe', 3),
 ('Nomen', 'Genus', 2), ('Nomen', 'Numerus', 2), ('Nomen', 'Kasus Nom/Akk/Dat', 5),
 ('Nomen', 'Genitiv bei Eigennamen', 9),
 ('Artikel', 'definit', 2), ('Artikel', 'demonstrativ dieser', 8),
 ('Artikel', 'indefinit ein', 8), ('Artikel', 'Nullartikel', 8),
 ('Artikel', 'Possessiv mein/unser', 8), ('Artikel', 'negativ kein', 8),
 ('Pronomen', 'man/etwas/nichts/mehr/alles/welch-', 9),
 ('Pronomen', 'Personal Nom/Akk/Dat', 9), ('Pronomen', 'Dativverben danken/helfen', 9),
 ('Pronomen', 'Reziprok sich/uns', 9), ('Pronomen', 'Frage Wer/Wen/Wem', 9),
 ('Adjektiv', 'attributiv', 11), ('Adjektiv', 'prädikativ', 11),
 ('Adjektiv', 'adverbial', 11), ('Adjektiv', 'Komparation', 11),
 ('Adjektiv', 'Zahlwörter', 1),
 ('Präposition', 'temporal', 10), ('Präposition', 'lokal', 10), ('Präposition', 'modal', 10),
 ('Syntax', 'Verbzweitstellung', 4), ('Syntax', 'Verbergänzung（5 种）', 13),
 ('Syntax', 'Satzklammer', 4), ('Syntax', 'Negation nicht/kein', 8),
 ('Syntax', 'Fragesatz', 4), ('Syntax', 'Satzverbindungen', 13),
 ('Wortbildung', 'Nomen -er/-ung/-in/Komposita', 13),
 ('Wortbildung', 'Adjektive un-/-los/-bar', 13),
]
import sys; sys.path.insert(0, 'src')
from grammatik import LEKTIONEN
have = {L['no'] for L in LEKTIONEN}
miss = [x for x in INVENTAR if x[2] not in have]
print('考纲条目 %d 条，全部有归属：%s' % (len(INVENTAR), '✅' if not miss else '❌ %s' % miss))
used = {x[2] for x in INVENTAR}
idle = sorted(have - used)
print('未承接考纲条目的课：%s' % (idle or '无'))
cur = None
for grp, item, no in INVENTAR:
    if grp != cur: print('\n%s' % grp); cur = grp
    t = next(L['title'] for L in LEKTIONEN if L['no'] == no)
    print('  %-34s → 第 %2d 课 %s' % (item, no, t))
