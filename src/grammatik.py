# -*- coding: utf-8 -*-
"""语法课：零基础的第一批「必须先讲，讲完才谈得上练」的内容。

原先应用里只有背单词和五个测验，没有一句讲解——让没学过的人去做
einundzwanzig 的听写题，那不是练习是猜谜。这份文件补的就是讲解。

排序按「不会就寸步难行」，不按语法书的章节顺序：
    1 数字   —— 听力口语每场必考，且规则反直觉（倒读）
    2 性别   —— 中文没有语法性，这是最大的认知门槛，且每个名词都受影响
    3 变位   —— 不会变位一个句子也说不出来
    4 语序   —— 德语靠「动词第二位 + 动词框」组织句子，和中文完全不同
    5 格     —— 官方考纲 A1 明确要考 Nominativ / Akkusativ / Dativ

每课由若干块组成，块的写法：
    ('t',   正文)                       讲解段落，可用 <b> 强调
    ('r',   标题, 说明)                 规则框，要背下来的那句话
    ('w',   提醒)                       中文母语者的坑，黄底
    ('tab', [表头…], [[单元格…]…])       对照表；单元格以 * 开头的可点朗读
    ('bsp', [(德语, 中文)…])             例句，整句可点朗读
    ('drill', 测验 id, 按钮文字)         跳到对应测验
"""

LEKTIONEN = [

# ============ 1. 数字 ============
{
    'id': 'zahlen', 'no': 1,
    'title': '数字 0–100',
    'sub': '读法 · 写法 · 反着读的那条规则',
    'why': '听力每套题都考电话号码、价格、门牌号。而德语两位数是反着读的，'
           '不先把这条弄明白，听多少遍都是白听。',
    'blocks': [
        ('t', '先把 0–12 背下来。这十三个没有规律，只能死记，但后面全靠它们拼。'),
        ('tab', ['数字', '德语', '数字', '德语'], [
            ['0', '*null',  '7',  '*sieben'],
            ['1', '*eins',  '8',  '*acht'],
            ['2', '*zwei',  '9',  '*neun'],
            ['3', '*drei',  '10', '*zehn'],
            ['4', '*vier',  '11', '*elf'],
            ['5', '*fünf',  '12', '*zwölf'],
            ['6', '*sechs', '',   ''],
        ]),
        ('w', '电话号码里 <b>zwei</b> 常读成 <b>zwo</b>，为的是不和 drei 听混。'
              '考试录音里出现别愣住。'),

        ('r', '13–19：个位 + zehn', 'dreizehn = drei + zehn。照这个拼就行，但有两个要改写。'),
        ('tab', ['数字', '德语', '数字', '德语'], [
            ['13', '*dreizehn', '17', '*siebzehn'],
            ['14', '*vierzehn', '18', '*achtzehn'],
            ['15', '*fünfzehn', '19', '*neunzehn'],
            ['16', '*sechzehn', '',   ''],
        ]),
        ('w', '<b>16 = sechzehn</b>，不是 sech<b>s</b>zehn——丢掉一个 s。<br>'
              '<b>17 = siebzehn</b>，不是 sieb<b>en</b>zehn——丢掉 en。<br>'
              '这两个是拼写题的高频失分点。'),

        ('r', '整十：个位 + zig', '例外是 20 和 30，另外 60、70 和上面一样要缩写。'),
        ('tab', ['数字', '德语', '数字', '德语'], [
            ['20', '*zwanzig', '60', '*sechzig'],
            ['30', '*dreißig', '70', '*siebzig'],
            ['40', '*vierzig', '80', '*achtzig'],
            ['50', '*fünfzig', '90', '*neunzig'],
        ]),
        ('w', '<b>20 = zwanzig</b> 不是 zweizig，<b>30 = dreißig</b> 用 ß 且不是 -zig。'
              '这两个只能单独记。'),

        ('r', '21–99：个位 + und + 十位，全部连写',
              '<b>21 = einundzwanzig</b>，字面顺序是「一和二十」——'
              '先说个位，再说十位，中间夹一个 und。'),
        ('tab', ['数字', '德语', '怎么拆'], [
            ['21', '*einundzwanzig',   'ein + und + zwanzig'],
            ['42', '*zweiundvierzig',  'zwei + und + vierzig'],
            ['66', '*sechsundsechzig', 'sechs + und + sechzig'],
            ['99', '*neunundneunzig',  'neun + und + neunzig'],
        ]),
        ('w', '两个必须记住的细节：<br>'
              '① 个位的 1 用 <b>ein</b> 不用 eins——einundzwanzig，不是 einsundzwanzig。<br>'
              '② <b>全部连成一个词</b>，不空格也不加连字符。这是写作题的送分点也是失分点。'),
        ('t', '听力上的对策：听到 <b>…und…</b> 就知道这是两位数，<b>先别动笔</b>，'
              '等 und 后面那截听完再从后往前写。很多人一听到 ein 就写下 1，然后整个数就错了。'),

        ('r', '100 以上', 'hundert（或 einhundert）。101 = hunderteins，'
              '200 = zweihundert，1000 = tausend。'),
        ('bsp', [
            ('Ich bin einundzwanzig Jahre alt.', '我二十一岁。'),
            ('Das kostet siebenundneunzig Euro.', '这个九十七欧元。'),
            ('Meine Nummer ist null vier drei zwo acht.', '我的号码是 0 4 3 2 8。'),
            ('Ich wohne in der Bahnhofstraße sechsunddreißig.', '我住火车站大街 36 号。'),
        ]),
        ('drill', 'num', '去练：听德语报数写数字'),
    ],
},

# ============ 2. 名词与性别 ============
{
    'id': 'genus', 'no': 2,
    'title': '名词与性别',
    'sub': 'der / die / das 到底是什么',
    'why': '中文里没有「语法性」这回事，所以这是中国人学德语的第一个真门槛。'
           '而它又躲不开——每个名词都带着一个性，冠词、形容词、代词全跟着它变。',
    'blocks': [
        ('t', '德语每个名词都属于三类之一，用不同的冠词标出来：'
              '<b>der</b>（阳性）· <b>die</b>（阴性）· <b>das</b>（中性）。'),
        ('r', '性别和意思基本无关',
              '这不是「男的用 der、女的用 die」。<b>das Mädchen</b>（女孩）是中性，'
              '<b>der Löffel</b>（勺子）是阳性。绝大多数时候没有道理可讲。'),
        ('t', '所以只有一个办法：<b>背单词时永远连冠词一起背</b>。'
              '不要背「Tisch = 桌子」，要背「<b>der</b> Tisch」。'
              '这个应用里名词永远和它的颜色一起出现，就是为了让你形成条件反射。'),
        ('tab', ['冠词', '这个应用里的颜色', '例子'], [
            ['der', '蓝色',  '*der Tisch'],
            ['die', '红色',  '*die Lampe'],
            ['das', '绿色',  '*das Buch'],
        ]),

        ('r', '复数一律用 die', '不管单数是 der、die 还是 das，变成复数以后冠词统统是 <b>die</b>。'),
        ('bsp', [
            ('der Apfel → die Äpfel', '苹果 → 苹果（复数）'),
            ('das Buch → die Bücher', '书 → 书（复数）'),
        ]),
        ('t', '所以卡片上的复数用的是红色——红色就是 die 的颜色，看一眼就知道那是复数。'),

        ('r', '约八成能从词尾猜出来', '记住下面这几组词尾，剩下的才需要硬背。'),
        ('tab', ['词尾', '性别', '例子'], [
            ['-ung',  'die', '*die Wohnung'],
            ['-heit / -keit', 'die', '*die Gesundheit'],
            ['-schaft', 'die', '*die Freundschaft'],
            ['-ion / -tät', 'die', '*die Information'],
            ['-e（多数）', 'die', '*die Blume'],
            ['-er（人 / 工具）', 'der', '*der Lehrer'],
            ['-ling', 'der', '*der Frühling'],
            ['-chen / -lein', 'das', '*das Mädchen'],
            ['-um', 'das', '*das Datum'],
        ]),
        ('t', '另外几条也很稳：<b>der</b>——男性的人、星期、月份、季节、方位、天气现象；'
              '<b>das</b>——字母、颜色、动词直接当名词用（das Essen 吃饭这件事）。'),
        ('w', '这解释了为什么 <b>das Mädchen</b> 是中性：<b>-chen</b> 是「小」的后缀，'
              '带这个后缀的词一律中性，压过了「女孩是女性」这层意思。'),

        ('r', '名词首字母永远大写', '这是德语独有的规则。句子中间的名词也一样要大写，'
              '写作题里小写就是错。'),
        ('bsp', [
            ('Der Mann liest ein Buch.', '这个男人在读一本书。'),
            ('Die Wohnung hat drei Zimmer.', '这套房子有三个房间。'),
            ('Das Kind spielt im Garten.', '孩子在花园里玩。'),
        ]),
        ('drill', 'art', '去练：看名词选冠词'),
    ],
},

# ============ 3. 动词变位 ============
{
    'id': 'verben', 'no': 3,
    'title': '动词变位',
    'sub': '主语一换，动词就得跟着换',
    'why': '中文的动词从不变形——「我去、你去、他去」都是「去」。'
           '德语必须跟着主语改词尾，不会这个就一个完整句子都说不出来。',
    'blocks': [
        ('t', '动词原形（叫不定式）都以 <b>-en</b> 结尾：lernen（学）、wohnen（住）、'
              'kommen（来）。去掉 -en 剩下的叫词干，变位就是给词干换词尾。'),
        ('r', '规则动词的六个词尾', 'lernen → 词干 lern-'),
        ('tab', ['人称', '词尾', 'lernen（学）'], [
            ['ich 我',        '-e',  '*ich lerne'],
            ['du 你',         '-st', '*du lernst'],
            ['er / sie / es 他她它', '-t', '*er lernt'],
            ['wir 我们',      '-en', '*wir lernen'],
            ['ihr 你们',      '-t',  '*ihr lernt'],
            ['sie / Sie 他们 / 您', '-en', '*sie lernen'],
        ]),
        ('w', '<b>Sie</b> 大写是「您」，用于陌生人和正式场合，变位跟「他们」一样。'
              '口语考试第一句就要用 Sie，别用错成 du。'),

        ('r', 'sein 和 haben 必须单独背', '这两个最常用，也最不规则。'),
        ('tab', ['人称', 'sein（是）', 'haben（有）'], [
            ['ich',            '*ich bin',  '*ich habe'],
            ['du',             '*du bist',  '*du hast'],
            ['er / sie / es',  '*er ist',   '*er hat'],
            ['wir',            '*wir sind', '*wir haben'],
            ['ihr',            '*ihr seid', '*ihr habt'],
            ['sie / Sie',      '*sie sind', '*sie haben'],
        ]),

        ('r', '有些动词在 du 和 er 时词干换元音', '只在这两个人称变，其余不变。A1 里这几个最常用。'),
        ('tab', ['原形', 'du', 'er / sie / es'], [
            ['fahren 乘车',  '*du fährst',  '*er fährt'],
            ['sprechen 说',  '*du sprichst', '*er spricht'],
            ['essen 吃',     '*du isst',    '*er isst'],
            ['nehmen 拿',    '*du nimmst',  '*er nimmt'],
            ['sehen 看',     '*du siehst',  '*er sieht'],
            ['schlafen 睡',  '*du schläfst', '*er schläft'],
        ]),

        ('r', '可分动词：前缀会跑到句尾', 'aufstehen（起床）用起来时，auf- 被甩到最后。'),
        ('bsp', [
            ('Ich stehe um sieben Uhr auf.', '我七点起床。'),
            ('Wann kommt der Zug an?', '火车几点到？'),
            ('Ich kaufe im Supermarkt ein.', '我在超市买东西。'),
        ]),
        ('t', '怎么判断一个动词可不可分？<b>听重音</b>——重音落在前缀上（<b>AUF</b>stehen）的可分，'
              '落在词干上（be<b>SU</b>chen）的不可分。这条在发音关里也讲过。'),
        ('bsp', [
            ('Ich bin Student und lerne Deutsch.', '我是学生，在学德语。'),
            ('Wo wohnst du?', '你住哪儿？'),
            ('Meine Schwester hat zwei Kinder.', '我姐姐有两个孩子。'),
        ]),
    ],
},

# ============ 4. 句子语序 ============
{
    'id': 'satzbau', 'no': 4,
    'title': '句子语序',
    'sub': '动词第二位 · 动词框',
    'why': '德语句子不是按中文顺序摆的。掌握「动词永远第二位」和「动词框」这两条，'
           '就能把学过的词拼成正确的句子。',
    'blocks': [
        ('r', '陈述句：变位动词永远在第二位',
              '注意是第二个<b>成分</b>，不是第二个词。第一位放什么都行，动词的位置不动。'),
        ('tab', ['第一位', '第二位（动词）', '其余'], [
            ['Ich',        '*lerne', 'heute Deutsch.'],
            ['Heute',      '*lerne', 'ich Deutsch.'],
            ['Deutsch',    '*lerne', 'ich heute.'],
        ]),
        ('t', '三句意思一样，都对。想强调什么就把什么放最前面，<b>主语被挤到动词后面去</b>——'
              '这一点和中文完全不同，中文里主语几乎总在最前。'),
        ('w', '最常见的错误：把状语提前之后忘了把主语挪后。<br>'
              '❌ Heute ich lerne Deutsch.　✅ Heute <b>lerne ich</b> Deutsch.'),

        ('r', '疑问句有两种', '要么疑问词打头，要么动词打头。'),
        ('tab', ['类型', '语序', '例子'], [
            ['W-疑问句', '疑问词 + 动词 + 主语', '*Wo wohnen Sie?'],
            ['是否疑问句', '动词 + 主语', '*Wohnen Sie in Berlin?'],
        ]),
        ('bsp', [
            ('Wie heißen Sie?', '您叫什么名字？'),
            ('Woher kommen Sie?', '您从哪儿来？'),
            ('Haben Sie Zeit?', '您有时间吗？'),
            ('Sprechen Sie Deutsch?', '您说德语吗？'),
        ]),

        ('r', '动词框（Satzklammer）：句子被两个动词夹住',
              '变位的那个留在第二位，另一半跑到<b>句子最末尾</b>，中间夹着所有其他成分。'),
        ('t', '三种情况会撑起动词框，A1 全考：'),
        ('tab', ['情况', '第二位', '句尾'], [
            ['情态动词', '*Ich muss heute Abend arbeiten.', 'arbeiten'],
            ['可分动词', '*Ich stehe jeden Tag um sieben auf.', 'auf'],
            ['完成时',   '*Ich habe gestern Deutsch gelernt.', 'gelernt'],
        ]),
        ('t', '所以听德语要<b>听到最后</b>——句尾那个词往往才决定整句在说什么。'
              '「Ich habe gestern Deutsch …」听到这儿你还不知道是学了、教了还是忘了。'),
        ('bsp', [
            ('Kannst du mir helfen?', '你能帮我一下吗？'),
            ('Wir möchten einen Tisch reservieren.', '我们想订一张桌子。'),
            ('Wann fängt der Kurs an?', '课程什么时候开始？'),
        ]),
        ('drill', 'satz', '去练：把词块排成句子'),
    ],
},

# ============ 5. 格 ============
{
    'id': 'kasus', 'no': 5,
    'title': '三格与四格',
    'sub': '冠词为什么会变形',
    'why': '官方考纲写明 A1 要考主格、四格和三格。中文里没有「格」，'
           '但只要抓住一条捷径，入门比想象中容易。',
    'blocks': [
        ('t', '中文靠词序表示谁对谁做了什么：「我看见他」和「他看见我」全靠位置区分。'
              '德语靠<b>冠词变形</b>——名词在句中扮演什么角色，冠词就跟着换一个样子。'),
        ('r', '先记这一条捷径', '四格里<b>只有阳性会变</b>：der → den。'
              '阴性、中性、复数在主格和四格里长得一模一样。'),
        ('tab', ['', '阳性', '阴性', '中性', '复数'], [
            ['主格 Nominativ（谁）', 'der', 'die', 'das', 'die'],
            ['四格 Akkusativ（对谁）', 'den', 'die', 'das', 'die'],
            ['三格 Dativ（给谁）', 'dem', 'der', 'dem', 'den'],
        ]),
        ('t', '所以初学时的实用做法是：<b>先只盯住阳性名词</b>。'
              '看到 der 开头的词做宾语，改成 den 就对了一大半。'),
        ('bsp', [
            ('Der Mann kauft einen Apfel.', '这个男人买一个苹果。（Mann 是主语 → der）'),
            ('Ich sehe den Mann.', '我看见那个男人。（Mann 是宾语 → den）'),
            ('Ich gebe dem Mann das Buch.', '我把书给那个男人。（给谁 → dem）'),
        ]),

        ('r', '哪些动词要三格', '大部分动词跟四格，但下面这几个常用的跟三格，得单独记。'),
        ('tab', ['动词', '意思', '例子'], [
            ['helfen',  '帮助', '*Können Sie mir helfen?'],
            ['danken',  '感谢', '*Ich danke Ihnen.'],
            ['gehören', '属于', '*Das Buch gehört mir.'],
            ['gefallen', '中意', '*Die Wohnung gefällt mir.'],
            ['antworten', '回答', '*Er antwortet mir nicht.'],
        ]),

        ('r', '介词固定支配某个格', '这个没道理可讲，跟着介词一起背。'),
        ('tab', ['支配三格', '支配四格'], [
            ['mit（和）', 'für（为了）'],
            ['nach（去 / 之后）', 'ohne（没有）'],
            ['bei（在…处）', 'gegen（朝 / 反对）'],
            ['seit（自从）', 'um（在…点）'],
            ['von（从 / 的）', 'durch（穿过）'],
            ['zu（到）', ''],
        ]),
        ('bsp', [
            ('Ich fahre mit dem Bus.', '我坐公交车。（mit + 三格）'),
            ('Das Geschenk ist für dich.', '这个礼物是给你的。（für + 四格）'),
            ('Ich wohne seit drei Jahren in Köln.', '我在科隆住了三年了。'),
        ]),
        ('w', '人称代词也跟着变格，这几个最常用，直接背下来：<br>'
              'ich → mich（四）/ mir（三）　·　du → dich / dir　·　'
              'er → ihn / ihm　·　sie → sie / ihr　·　Sie → Sie / Ihnen'),
    ],
},
]
