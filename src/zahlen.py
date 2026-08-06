# -*- coding: utf-8 -*-
"""数字与报时的德语说法，构建期生成。

原先这两套是在前端用 JS 现拼的，带来两个问题：

1. 拼出来的字符串没有预生成音频，点了要等网络 404 才回落到系统语音，
   而那时 iOS 已经脱离用户手势，语音合成被系统拦掉——表现就是「没声音」。
   放到构建期生成，就能提前把每一条都合成好。

2. 前端那份报时是错的：halb 和 Viertel vor 要用**下一个**整点，
   代码用的是当前整点，2:30 拼成了 halb zwei（正确是 halb drei）。
   而测验的说明里恰好写着「halb drei 是 2:30」，自相矛盾。

数字上限取 200：测验出题范围是 4–200。
报时只覆盖整点与一刻钟，因为测验只考这四种。
"""

EINS   = ['null', 'eins', 'zwei', 'drei', 'vier', 'fünf', 'sechs', 'sieben',
          'acht', 'neun', 'zehn', 'elf', 'zwölf']
ZEHN10 = ['zehn', 'elf', 'zwölf', 'dreizehn', 'vierzehn', 'fünfzehn',
          'sechzehn', 'siebzehn', 'achtzehn', 'neunzehn']
# 个位在复合数里用 ein 不用 eins：einundzwanzig
EINZ   = ['', 'ein', 'zwei', 'drei', 'vier', 'fünf', 'sechs', 'sieben', 'acht', 'neun']
ZEHNER = ['', '', 'zwanzig', 'dreißig', 'vierzig', 'fünfzig',
          'sechzig', 'siebzig', 'achtzig', 'neunzig']

MAX = 200


def zahl(n):
    """0–200 的德语写法，全部连写"""
    if n < 13:
        return EINS[n]
    if n < 20:
        return ZEHN10[n - 10]
    if n < 100:
        return (EINZ[n % 10] + 'und' if n % 10 else '') + ZEHNER[n // 10]
    h = 'hundert' if n < 200 else 'zweihundert'
    return h + (zahl(n % 100) if n % 100 else '')


def uhrzeit(h, m):
    """整点与一刻钟的口语说法。

    halb 与 Viertel vor 指向**下一个**整点，这是德语和中文最容易错位的地方：
    halb drei 是 2:30，不是 3:30。
    """
    now = h % 12 or 12               # 当前整点，12 小时制
    nxt = (h % 12) + 1               # 下一个整点，0→1、11→12、12→1
    if m == 0:
        return 'Es ist %s Uhr.' % EINS[now]
    if m == 15:
        return 'Es ist Viertel nach %s.' % EINS[now]
    if m == 30:
        return 'Es ist halb %s.' % EINS[nxt]
    if m == 45:
        return 'Es ist Viertel vor %s.' % EINS[nxt]
    raise ValueError('只覆盖整点与一刻钟：%d' % m)


MINUTEN = (0, 15, 30, 45)
STUNDEN = tuple(range(1, 13))        # 只用 12 小时制出题：24 小时制下
                                     # 「halb drei」既可能是 2:30 也可能是 14:30，
                                     # 选项里两个都出现就成了无解题


def data():
    return {
        'zahl': {str(n): zahl(n) for n in range(MAX + 1)},
        'uhr': {'%d:%d' % (h, m): uhrzeit(h, m) for h in STUNDEN for m in MINUTEN},
        'stunden': list(STUNDEN),
        'minuten': list(MINUTEN),
    }


def texts():
    d = data()
    return list(d['zahl'].values()) + list(d['uhr'].values())


if __name__ == '__main__':
    for n in (0, 12, 16, 17, 21, 30, 66, 99, 100, 101, 137, 200):
        print('%4d  %s' % (n, zahl(n)))
    print()
    for h, m in ((2, 0), (2, 15), (2, 30), (2, 45), (12, 30), (1, 45)):
        print('%2d:%02d  %s' % (h, m, uhrzeit(h, m)))
