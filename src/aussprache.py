# -*- coding: utf-8 -*-
"""第 0 章 · 发音关。

零基础入口。德语拼读规则性强，这一关过了之后看到任何生词都能读出来，
是最大的一次正反馈。而这块恰恰是应用强于纸质教材的地方——即时发音、
成对听辨、音节拆分，纸上做不到。

编写取向：**主线是拆掉英语干扰**。学习者有英语底子，
而英语直觉在德语里大量失效（W 读 /v/、V 读 /f/、J 读 /j/、Z 读 /ts/、
S 在元音前读 /z/、ie 读长 i 而 ei 读 ai）。不点破这些，会一路读错。

字段：
  ALPHABET   [字母, 字母名读音(IPA), 例词, 中文提示]
             字母名是口语 Teil 1「拼写」题的直接考点
  REGELN     发音规则，按类分组：
             [规则, IPA, [例词…], 中文说明, 英语干扰提示(可空)]
  MINIMALPAARE  最小对立对，用于听辨训练：[A, B, 差在哪]
"""

# ============ 一、字母表 ============
# 拼写题要求逐个字母念出来，字母名本身就是考点
ALPHABET = [
    ["A", "aː",          "Apfel",     None],
    ["B", "beː",         "Buch",      None],
    ["C", "tseː",        "Computer",  "单独的 C 少见，多出现在 ch / sch 组合里"],
    ["D", "deː",         "Deutsch",   None],
    ["E", "eː",          "Essen",     "读「诶」不读「衣」——英语 E 读 /iː/，德语不是"],
    ["F", "ɛf",          "Frau",      None],
    ["G", "ɡeː",         "gut",       "读「给」不读「杰」"],
    ["H", "haː",         "Haus",      None],
    ["I", "iː",          "ich",       "读「衣」——和 E 正好是英语的反过来"],
    ["J", "jɔt",         "ja",        "读「幼特」，字母名不是英语的「杰」"],
    ["K", "kaː",         "Kind",      None],
    ["L", "ɛl",          "Lehrer",    None],
    ["M", "ɛm",          "Mutter",    None],
    ["N", "ɛn",          "Name",      None],
    ["O", "oː",          "Obst",      None],
    ["P", "peː",         "Post",      None],
    ["Q", "kuː",         "Quittung",  "总是跟着 u，读 /kv/：Quittung ≈ 「克维通」"],
    ["R", "ɛʁ",          "rot",       None],
    ["S", "ɛs",          "Sonne",     None],
    ["T", "teː",         "Tag",       None],
    ["U", "uː",          "Uhr",       None],
    ["V", "faʊ",         "Vater",     "字母名读「fau」，发音也是 /f/——不是英语的 /v/"],
    ["W", "veː",         "Wasser",    "字母名读「vee」，发音是 /v/——英语的 W 音德语里没有"],
    ["X", "ɪks",         "Taxi",      None],
    ["Y", "ˈʏpsilɔn",    "Yoga",      "字母名最长，拼写题里出现要反应过来"],
    ["Z", "tsɛt",        "Zeit",      "读「采特」，发 /ts/ 不是 /z/"],
    ["Ä", "ɛː",          "Äpfel",     "念作 A-Umlaut。开口比 e 大"],
    ["Ö", "øː",          "hören",     "念作 O-Umlaut。撅嘴发 e，中文没有这个音"],
    ["Ü", "yː",          "Tür",       "念作 U-Umlaut。撅嘴发 i，接近普通话「绿」的韵母"],
    ["ß", "ɛsˈtsɛt",     "Straße",    "念作 Eszett 或 scharfes S，只发 /s/，永远不大写"],
]

# ============ 二、发音规则 ============
REGELN = [

["英语干扰 —— 先拆掉这五条", [
    ["w", "v", ["Wasser", "wo", "Wohnung", "wir"],
     "德语 w 发英语 v 的音。",
     "英语的 /w/（water）在德语里根本不存在。看到 w 就想 v。"],
    ["v", "f", ["Vater", "vier", "von", "verstehen"],
     "德语 v 绝大多数发 /f/。",
     "和 w 正好换了个位置：英语 v→/v/，德语 v→/f/。这两条要一起记。"],
    ["j", "j", ["ja", "Jahr", "jetzt", "Junge"],
     "德语 j 发英语 y 的音。",
     "英语 j 读 /dʒ/（job），德语完全不是。ja 读「呀」不读「贾」。"],
    ["z", "ts", ["Zeit", "zwei", "Zug", "zahlen"],
     "德语 z 发 /ts/，像中文的「次」。",
     "英语 z 读 /z/，德语没有这个用法。zwei 读「次外」。"],
    ["s + 元音", "z", ["Sonne", "sagen", "sieben", "Sie"],
     "s 在元音前发 /z/（浊音）。",
     "英语 s 多读 /s/。德语 Sie 读「zee」不是「see」。"],
]],

["元音长短 —— 德语靠它区分词义", [
    ["元音 + 单辅音", "长", ["Tag", "gut", "Name", "Buch"],
     "元音后面只有一个辅音字母 → 读长音。", None],
    ["元音 + 双辅音", "短", ["Mann", "kommen", "bitte", "Sonne"],
     "元音后面有两个及以上辅音 → 读短音。这是最常用的判断法。", None],
    ["ie", "iː", ["Bier", "vier", "wieder", "Liebe"],
     "ie 永远读长音的「衣」。", "别按英语的 ie 读。Bier 就是英语的 beer。"],
    ["元音 + h", "长", ["Uhr", "gehen", "Jahr", "ihn"],
     "h 在元音后不发音，只表示前面的元音读长音（Dehnungs-h）。", None],
    ["双写元音", "长", ["Tee", "Boot", "Haar", "Staat"],
     "aa / ee / oo 都读长音。", None],
]],

["特殊组合", [
    ["ei", "aɪ", ["ein", "nein", "Zeit", "heißen"],
     "ei 读「爱」。", "记法：读音跟第二个字母走 —— ei 里的 i 读「爱」。"],
    ["ie", "iː", ["die", "sieben", "Miete", "nie"],
     "ie 读长「衣」。", "与 ei 正好相反，这是最高频的错。同样规律：跟第二个字母走。"],
    ["eu / äu", "ɔɪ", ["neun", "Deutsch", "Häuser", "Freund"],
     "eu 和 äu 都读「奥伊」。", None],
    ["ch（在 a/o/u/au 后）", "x", ["Buch", "auch", "acht", "Tochter"],
     "ach-Laut：喉咙后部摩擦，像用力哈气。", None],
    ["ch（其余情况）", "ç", ["ich", "nicht", "Milch", "München"],
     "ich-Laut：舌面靠前，接近汉语「希」的起头。", None],
    ["sch", "ʃ", ["Schule", "schön", "Deutsch", "schreiben"],
     "sch 读「什」。", None],
    ["词首 sp-", "ʃp", ["sprechen", "Sport", "spät", "Sprache"],
     "词首的 sp 读「什普」，s 变成 /ʃ/。", "英语 sp 直读 /sp/，德语不是。"],
    ["词首 st-", "ʃt", ["Straße", "Stadt", "stehen", "Student"],
     "词首的 st 读「什特」。", "Straße 读「什特拉塞」，不是「斯特拉塞」。"],
    ["-ig（词尾）", "ɪç", ["richtig", "wichtig", "billig", "zwanzig"],
     "词尾 -ig 读 ich-Laut，不读 /ɪɡ/。", None],
    ["qu", "kv", ["Quittung", "Qualität", "bequem"],
     "qu 读 /kv/。", "英语 qu 读 /kw/。"],
]],

["词尾清化 —— 写的和读的不一样", [
    ["-b（词尾）", "p", ["halb", "gelb", "Verb"],
     "词尾的 b 读成 /p/。", None],
    ["-d（词尾）", "t", ["Kind", "und", "Land", "Freund"],
     "词尾的 d 读成 /t/。", "Kind 读「kint」，Land 读「lant」。"],
    ["-g（词尾）", "k", ["Tag", "Zug", "Weg", "genug"],
     "词尾的 g 读成 /k/。", "Tag 读 /taːk/，不是 /taːɡ/。"],
    ["-er（词尾）", "ɐ", ["Mutter", "Vater", "Lehrer", "wieder"],
     "词尾 -er 读成弱化的「呃」，几乎听不到 r。", None],
]],

["重音", [
    ["默认首音节", "", ["Arbeit", "Fenster", "Wohnung", "Morgen"],
     "德语词绝大多数重音在第一个音节。", None],
    ["可分动词在前缀", "", ["aufstehen", "einkaufen", "ankommen", "mitkommen"],
     "可分动词的重音落在前缀上：AUFstehen。", "重音位置正好帮你判断动词可不可分。"],
    ["外来词常在词尾", "", ["Student", "Musik", "Hotel", "Papier"],
     "外来词是例外，重音常在最后一个音节：StuDENT。", None],
    ["be- / ge- / er- / ver- / ent- 不重读", "", ["besuchen", "gefallen", "erklären", "verstehen"],
     "这些不可分前缀永远不重读，重音在后面的词干上。", None],
]],
]

# ============ 三、最小对立对 ============
# 中文母语者的听辨盲区。先能听出区别，才谈得上发准。
MINIMALPAARE = [
    ["Tür",    "Tur",    "ü / u —— 撅嘴发 i vs 直接发 u。中文没有 ü 的对立，最需要练"],
    ["schön",  "schon",  "ö / o —— schön 是「美」，schon 是「已经」，意思完全不同"],
    ["Staat",  "Stadt",  "长 a / 短 a —— 「国家」vs「城市」。中文无音位性长短对立，最难"],
    ["Beet",   "Bett",   "长 e / 短 e —— 「花坛」vs「床」"],
    ["ihn",    "in",     "长 i / 短 i —— 「他（宾格）」vs「在……里」"],
    ["Ofen",   "offen",  "长 o / 短 o —— 「炉子」vs「开着的」"],
    ["Vater",  "Water",  "v / w —— 前者 /f/，后者 /v/。英语干扰的直接检验"],
    ["ich",    "ach",    "两种 ch —— 舌面前 vs 喉咙后，德语里是两个不同的音"],
    ["Kiste",  "Küste",  "i / ü —— 「箱子」vs「海岸」"],
    ["Mutter", "Mütter", "u / ü —— 单数「母亲」vs 复数「母亲们」，变音就是复数标志"],
]
