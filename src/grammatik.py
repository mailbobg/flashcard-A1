# -*- coding: utf-8 -*-
"""语法课：零基础的第一批「必须先讲，讲完才谈得上练」的内容。

原先应用里只有背单词和五个测验，没有一句讲解——让没学过的人去做
einundzwanzig 的听写题，那不是练习是猜谜。这份文件补的就是讲解。

覆盖范围以官方《Prüfungsziele》第 101–106 页的语法清单为准，40 个条目
逐条对应，对照表见 src/check_lehrplan.py（跑一下能验证有没有漏）。

前五课按「不会就寸步难行」排序，不按语法书章节；后八课按考纲补齐：
    1 数字     听力口语每场必考，规则反直觉（倒读）
    2 性别     中文没有语法性，最大的认知门槛
    3 变位     不会变位一个句子也说不出来
    4 语序     动词第二位 + 动词框，和中文组织方式完全不同
    5 格       考纲明确要考 Nominativ / Akkusativ / Dativ
    6 情态动词  考纲逐个列了六个的例句，听力里满是
    7 完成时    德语讲过去几乎全用它；考纲点名只考 15 个动词
    8 冠词与否定 ein/kein/mein/dieser 变化方式相同，一起学最省力
    9 代词     mir/dir/ihn 听不出角色，整段听力就白听
   10 介词     考纲篇幅最大的一块，三张表
   11 形容词    表语与副词不变形；attributiv 词尾只要求看得懂
   12 命令式    试卷指令语本身就是命令式，看不懂就答不了题
   13 连句构词  连词决定语序；长复合词从后往前拆

一条重要的取向，来自考纲第 100 页的说明：语法清单主要面向**接受性技能**
（听力、阅读），对口语写作产出「处于次要地位」，且 A1 阶段「可理解性的
重要性高于形式正确性」。所以讲解偏向「听到/看到这个形式意味着什么」，
而不是纠结产出时的词尾。

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

# ============ 6. 情态动词 ============
{
    'id': 'modal', 'no': 6,
    'title': '情态动词',
    'sub': '能 / 想 / 必须 / 可以 / 应该',
    'why': '官方考纲把六个情态动词逐个列了例句。它们几乎出现在每一段听力里，'
           '而且会把句子撑成「动词框」——不认得就抓不住句尾那个关键动词。',
    'blocks': [
        ('t', '六个：<b>können</b>（能、会）· <b>wollen</b>（想要）· <b>müssen</b>（必须）· '
              '<b>dürfen</b>（可以、被允许）· <b>sollen</b>（应该）· <b>möchten</b>（想要，客气）。'),
        ('r', '变位有个共同特点：ich 和 er 长得一样，都不带词尾',
              '这和普通动词很不一样（普通动词 er 要加 -t）。'),
        ('tab', ['人称', 'können', 'müssen', 'dürfen'], [
            ['ich',           '*ich kann',   '*ich muss',   '*ich darf'],
            ['du',            '*du kannst',  '*du musst',   '*du darfst'],
            ['er / sie / es', '*er kann',    '*er muss',    '*er darf'],
            ['wir / sie / Sie', '*wir können', '*wir müssen', '*wir dürfen'],
            ['ihr',           '*ihr könnt',  '*ihr müsst',  '*ihr dürft'],
        ]),
        ('tab', ['人称', 'wollen', 'sollen', 'möchten'], [
            ['ich',           '*ich will',   '*ich soll',    '*ich möchte'],
            ['du',            '*du willst',  '*du sollst',   '*du möchtest'],
            ['er / sie / es', '*er will',    '*er soll',     '*er möchte'],
            ['wir / sie / Sie', '*wir wollen', '*wir sollen', '*wir möchten'],
            ['ihr',           '*ihr wollt',  '*ihr sollt',   '*ihr möchtet'],
        ]),

        ('r', '句子被撑成动词框', '情态动词变位后放第二位，<b>真正的动词用原形放到句尾</b>。'),
        ('bsp', [
            ('Ich kann gut Deutsch sprechen.', '我德语说得不错。'),
            ('Du musst zuerst die Hausaufgaben machen.', '你得先把作业做了。'),
            ('Sie dürfen hier nicht rauchen.', '这里禁止吸烟。'),
            ('Was soll ich machen?', '我该怎么办？'),
            ('Möchtest du eine Tasse Tee?', '你想来杯茶吗？'),
            ('Er will eine Ausbildung machen.', '他想去接受职业培训。'),
        ]),
        ('w', '否定形式差别很大，考试爱考：<br>'
              '<b>nicht dürfen</b> = 禁止（Sie dürfen hier nicht rauchen. 不许抽烟）<br>'
              '<b>nicht müssen</b> = 不必（Du musst nicht kommen. 你不用来，但可以来）<br>'
              '按中文直觉这两个容易译反。'),
        ('r', 'möchten 比 wollen 客气', '点餐、购物、提要求一律用 möchten。'
              'wollen 语气偏硬，说自己的打算时才用。'),
        ('t', '还有一个 <b>würde</b>，考纲里也列了，当固定说法记就行：'
              '<b>Ich würde gerne …</b>（我很想…），比 möchten 更客气。'),
        ('bsp', [
            ('Ich möchte einen Kaffee, bitte.', '我要一杯咖啡，谢谢。'),
            ('Ich würde gerne ins Kino gehen.', '我很想去看电影。'),
            ('Können Sie mir bitte helfen?', '您能帮我一下吗？'),
        ]),
        ('drill', 'satz', '去练：把词块排成句子'),
    ],
},

# ============ 7. 完成时 ============
{
    'id': 'perfekt', 'no': 7,
    'title': '完成时 Perfekt',
    'sub': '德语讲过去的事，用的是这个',
    'why': '德语口语说过去的事几乎全用完成时，不用过去式。'
           '好消息是官方考纲<b>点名了只考 15 个动词</b>的完成时，范围小得惊人。',
    'blocks': [
        ('r', '构成：haben / sein 放第二位，第二分词放句尾',
              '又是一个动词框。<b>Ich habe gestern Deutsch gelernt.</b>'),
        ('t', '第二分词怎么变，看动词属于哪一类：'),
        ('tab', ['类型', '怎么变', '例子'], [
            ['规则动词', 'ge + 词干 + t', '*machen → gemacht'],
            ['不规则动词', 'ge + 词干 + en（常换元音）', '*trinken → getrunken'],
            ['-ieren 结尾', '不加 ge-', '*passieren → passiert'],
            ['不可分前缀', '不加 ge-', '*verstehen → verstanden'],
            ['可分动词', 'ge 夹在前缀和词干之间', '*einkaufen → eingekauft'],
        ]),
        ('w', '判断加不加 <b>ge-</b>，靠的还是重音：重音在第一个音节的加 ge-，'
              '重音不在第一个音节的（ver<b>STE</b>hen、pas<b>SIE</b>ren）不加。'
              '这条和发音关里的可分动词判断法是同一条。'),

        ('r', '用 haben 还是 sein', '绝大多数用 <b>haben</b>。'
              '只有「位置移动」和「状态改变」用 <b>sein</b>——A1 范围内主要是 '
              'fahren / gehen / kommen / passieren，外加一个特例 bleiben。'),
        ('t', '下面这 15 个就是考纲点名要考的全部，直接背这张表：'),
        ('tab', ['原形', '完成时', '意思'], [
            ['arbeiten',  '*hat gearbeitet',  '工作'],
            ['bleiben',   '*ist geblieben',   '留下'],
            ['essen',     '*hat gegessen',    '吃'],
            ['fahren',    '*ist gefahren',    '乘车去'],
            ['fragen',    '*hat gefragt',     '问'],
            ['glauben',   '*hat geglaubt',    '相信'],
            ['haben',     '*hat gehabt',      '有'],
            ['lesen',     '*hat gelesen',     '读'],
            ['lernen',    '*hat gelernt',     '学'],
            ['machen',    '*hat gemacht',     '做'],
            ['passieren', '*ist passiert',    '发生'],
            ['schlafen',  '*hat geschlafen',  '睡'],
            ['sehen',     '*hat gesehen',     '看见'],
            ['trinken',   '*hat getrunken',   '喝'],
            ['verstehen', '*hat verstanden',  '理解'],
        ]),
        ('bsp', [
            ('Ich habe gestern viel gearbeitet.', '我昨天工作了很久。'),
            ('Wir sind mit dem Zug gefahren.', '我们坐火车去的。'),
            ('Hast du schon gegessen?', '你吃过了吗？'),
            ('Was ist passiert?', '出什么事了？'),
            ('Ich habe dich nicht verstanden.', '我没听懂你说的。'),
        ]),

        ('r', '分词也能当形容词用', '店铺告示上最常见，阅读题必考。'),
        ('bsp', [
            ('Heute geöffnet.', '今日营业。'),
            ('Bis Donnerstag geschlossen.', '休息至周四。'),
        ]),
        ('r', '过去式只需要两个词', '考纲只要求 haben 和 sein 的第一、三人称过去式。'
              '其余动词讲过去一律用完成时。'),
        ('bsp', [
            ('Ich hatte keine Zeit.', '我当时没时间。'),
            ('Er war nicht da.', '他当时不在。'),
        ]),
    ],
},

# ============ 8. 冠词与否定 ============
{
    'id': 'artikel', 'no': 8,
    'title': '冠词全家与否定',
    'sub': 'ein / kein / mein / dieser · nicht 还是 kein',
    'why': '这几个词形状几乎一样，变化方式也一样——一起学最省力。'
           '而 nicht 和 kein 的分工是中文母语者最容易错的地方：中文只有一个「不」。',
    'blocks': [
        ('r', '不定冠词 ein：只有阳性四格会变', '和定冠词一样，四格的变化只发生在阳性上。'),
        ('tab', ['', '阳性', '阴性', '中性', '复数'], [
            ['主格', 'ein', 'eine', 'ein', '—'],
            ['四格', 'einen', 'eine', 'ein', '—'],
            ['三格', 'einem', 'einer', 'einem', '—'],
        ]),
        ('t', '不定冠词<b>没有复数</b>。要说「一些书」，直接不用冠词：<b>Bücher</b>。'
              '这叫零冠词，物质名词和职业也用它。'),
        ('bsp', [
            ('Ich esse gern Fleisch.', '我爱吃肉。（物质名词，不加冠词）'),
            ('Ich bin Lehrer.', '我是老师。（说职业不加冠词）'),
        ]),

        ('r', 'mein / dein / kein 全都跟着 ein 变',
              '记住 ein 的变化，这一整家就都会了——词尾完全一样。'),
        ('tab', ['词', '意思', '例子'], [
            ['mein',  '我的',   '*Mein Vater ist Arzt.'],
            ['dein',  '你的',   '*Ist das dein Auto?'],
            ['sein',  '他的',   '*Das ist seine Frau.'],
            ['ihr',   '她的/他们的', '*Ihre Adresse, bitte?'],
            ['Ihr',   '您的（大写）', '*Wie ist Ihr Name?'],
            ['unser', '我们的', '*Das ist unsere Lehrerin.'],
            ['euer',  '你们的', '*Euer Kurs beginnt heute.'],
            ['kein',  '一个也没有', '*Ich habe keine Zeit.'],
        ]),
        ('t', '另外还有 <b>dieser / diese / dieses</b>（这个），跟着<b>定冠词</b>的词尾变——'
              'der→dieser、die→diese、das→dieses。'),

        ('r', 'nicht 还是 kein？看被否定的是不是名词',
              '否定<b>带 ein 或不带冠词的名词</b> → 用 <b>kein</b>；其他一切 → 用 <b>nicht</b>。'),
        ('tab', ['肯定', '否定', '用哪个'], [
            ['*Ich habe Zeit.',        '*Ich habe keine Zeit.',      'kein（名词无冠词）'],
            ['*Er ist Lehrer.',        '*Er ist kein Lehrer.',       'kein（职业无冠词）'],
            ['*Ich verstehe dich.',    '*Ich verstehe dich nicht.',  'nicht（否定动词）'],
            ['*Das ist der Bus.',      '*Das ist nicht der Bus.',    'nicht（有定冠词）'],
            ['*Es ist teuer.',         '*Es ist nicht teuer.',       'nicht（否定形容词）'],
        ]),
        ('w', '<b>nicht 的位置</b>：否定整句时放句尾（但在动词框的另一半之前）；'
              '否定某一个成分时紧挨在那个成分前面。<br>'
              'Ich kann heute <b>nicht</b> kommen.（nicht 在句尾动词 kommen 之前）'),
        ('bsp', [
            ('Ich habe kein Geld.', '我没钱。'),
            ('Ich komme heute nicht.', '我今天不来。'),
            ('Das ist nicht mein Koffer.', '这不是我的箱子。'),
        ]),
    ],
},

# ============ 9. 代词 ============
{
    'id': 'pronomen', 'no': 9,
    'title': '代词',
    'sub': '我你他的三格四格 · 疑问代词 · man',
    'why': '第 5 课只用一句话带过了代词变格，但考纲把它单列了一大块，'
           '而且听力里满是 mir / dir / ihn / Ihnen——听不出是谁对谁做，整段就白听了。',
    'blocks': [
        ('r', '人称代词的三张形式', '横着背：ich–mich–mir。'),
        ('tab', ['主格（谁）', '四格（对谁）', '三格（给谁）'], [
            ['*ich',  '*mich',  '*mir'],
            ['*du',   '*dich',  '*dir'],
            ['*er',   '*ihn',   '*ihm'],
            ['*sie',  '*sie',   '*ihr'],
            ['*es',   '*es',    '*ihm'],
            ['*wir',  '*uns',   '*uns'],
            ['*ihr',  '*euch',  '*euch'],
            ['*sie',  '*sie',   '*ihnen'],
            ['*Sie',  '*Sie',   '*Ihnen'],
        ]),
        ('w', '<b>sie</b> 一个词有三个意思：她 / 他们 / 您（大写 Sie）。'
              '靠动词变位区分——sie ist（她是）、sie sind（他们是）、Sie sind（您是）。'),

        ('r', '这几个动词后面跟三格', '考纲点名：danken、gehören、helfen、geben，'
              '外加一个固定说法 es geht + 三格。'),
        ('bsp', [
            ('Ich danke Ihnen sehr.', '非常感谢您。'),
            ('Kann ich dir helfen?', '我能帮你吗？'),
            ('Wem gehört die Jacke?', '这件外套是谁的？'),
            ('Es geht mir gut.', '我很好。'),
            ('Gib mir bitte dein Wörterbuch.', '把你的词典给我一下。'),
        ]),

        ('r', '疑问代词也分格', '问「谁」的时候要先想清楚问的是哪个角色。'),
        ('tab', ['格', '疑问词', '例子'], [
            ['主格', 'Wer? / Was?', '*Wer ist da?'],
            ['四格', 'Wen? / Was?', '*Wen besuchst du?'],
            ['三格', 'Wem?',        '*Wem gehört die Jacke?'],
        ]),

        ('r', '几个常用的不定代词', '考纲逐个列了例句，都是听力里的高频词。'),
        ('tab', ['词', '意思', '例子'], [
            ['man',    '泛指的「人们」', '*Kann man hier Fahrkarten kaufen?'],
            ['etwas',  '某些东西',      '*Möchten Sie etwas trinken?'],
            ['nichts', '什么也没有',    '*Ich esse jetzt nichts.'],
            ['alles',  '一切',          '*Er versteht alles.'],
            ['mehr',   '更多',          '*Möchten Sie noch mehr?'],
            ['welch-', '哪一个 / 一些',  '*Hast du welche?'],
        ]),
        ('t', '还有相互代词 <b>sich / uns</b>，表示「互相」：'
              '<b>Wir sehen uns morgen.</b>（我们明天见）。'
              '以及专有名词的二格，只有这一种形式要会：<b>Karls Freunde</b>（卡尔的朋友们）。'),
    ],
},

# ============ 10. 介词 ============
{
    'id': 'praep', 'no': 10,
    'title': '介词',
    'sub': '时间 · 地点 · 方式，各配固定的格',
    'why': '考纲给介词开了整整三张表，是清单里篇幅最大的一块。'
           '时间和地点的说法几乎每道听力题都要用，而且介词决定后面用哪个格。',
    'blocks': [
        ('r', '先记四个缩合形式', '介词和冠词会缩成一个词，写法上必须认得。'),
        ('tab', ['原形', '缩合', '例子'], [
            ['an dem', 'am',  '*am Montag'],
            ['in dem', 'im',  '*im Sommer'],
            ['zu dem', 'zum', '*zum Bahnhof'],
            ['zu der', 'zur', '*zur Schule'],
            ['in das', 'ins', '*ins Kino'],
        ]),

        ('r', '时间介词', '照考纲原样，这九个全部会考。'),
        ('tab', ['介词', '格', '例子'], [
            ['an',       '三格', '*am Morgen / am Dienstag'],
            ['in',       '三格', '*im Sommer / im Februar'],
            ['um',       '四格', '*um halb sieben'],
            ['vor',      '三格', '*vor dem Konzert'],
            ['nach',     '三格', '*nach dem Essen'],
            ['ab',       '四格', '*ab Februar'],
            ['für',      '四格', '*für drei Wochen'],
            ['über',     '—',    '*über zwanzig Minuten'],
            ['von … bis', '—',   '*von Dienstag bis Donnerstag'],
        ]),
        ('w', '钟点用 <b>um</b>（um acht Uhr），星期和日期用 <b>am</b>（am Montag），'
              '月份和季节用 <b>im</b>（im Juli、im Winter）。这三个别混。'),

        ('r', '地点介词', '注意 in 和 an 有两个格：静止在哪儿用三格，动向哪儿用四格。'),
        ('tab', ['介词', '格', '例子'], [
            ['in',        '三格 / 四格', '*im Park spielen / in die Stadt fahren'],
            ['an',        '三格 / 四格', '*am Meer / an den See'],
            ['auf',       '三格', '*auf dem Tisch'],
            ['aus',       '三格', '*aus Italien'],
            ['bei',       '三格', '*bei Familie Müller'],
            ['nach',      '三格', '*nach Deutschland fahren'],
            ['zu',        '三格', '*zur Schule gehen'],
            ['unter',     '三格', '*unter der Nummer'],
            ['von … nach', '三格', '*von Hamburg nach Bremen'],
        ]),
        ('w', '判断三格还是四格，问一句：<b>wo（在哪儿）→ 三格</b>，'
              '<b>wohin（往哪儿）→ 四格</b>。<br>'
              'Ich bin <b>im</b> Park.（在公园里）　vs　Ich gehe <b>in den</b> Park.（走进公园）'),

        ('r', '方式介词', '考纲只列了四个。'),
        ('tab', ['介词', '格', '例子'], [
            ['mit',   '三格', '*mit dem Auto'],
            ['ohne',  '四格', '*ohne dich'],
            ['für',   '四格', '*für meinen Freund'],
            ['aus',   '三格', '*aus Plastik'],
        ]),
        ('bsp', [
            ('Ich fahre am Montag mit dem Zug nach Berlin.', '我周一坐火车去柏林。'),
            ('Der Kurs beginnt um neun Uhr.', '课程九点开始。'),
            ('Wir machen im Sommer Urlaub am Meer.', '我们夏天去海边度假。'),
        ]),
    ],
},

# ============ 11. 形容词 ============
{
    'id': 'adjektiv', 'no': 11,
    'title': '形容词',
    'sub': '三种用法 · 比较级最高级',
    'why': '考纲列了 attributiv、prädikativ、adverbial 和 Komparation 四项。'
           '前两种和副词用法完全不变形，很好学；放在名词前面才要加词尾。',
    'blocks': [
        ('r', '两种最简单的用法：完全不变形', '这也是考纲详表里唯一给了例句的两种。'),
        ('tab', ['用法', '位置', '例子'], [
            ['表语', '放在 sein / werden 后面', '*Das Haus ist modern.'],
            ['副词', '直接修饰动词',            '*Ich lese gern.'],
        ]),
        ('t', '德语的形容词和副词<b>长得一样</b>，不像英语要加 -ly。'
              'schnell 既是「快的」也是「快地」：<b>Er ist schnell.</b> / <b>Er fährt schnell.</b>'),

        ('r', '放在名词前面就要加词尾', '这一项叫 attributiv，是形容词里唯一麻烦的部分。'),
        ('t', '好在 A1 只要能<b>看懂</b>就行——考纲明说语法清单主要针对听读理解，'
              '口语写作的形式正确性要求不高。所以先记一条最省力的规律：'),
        ('tab', ['前面是什么', '词尾', '例子'], [
            ['定冠词 der/die/das', '几乎都是 -e', '*der kleine Tisch'],
            ['定冠词 + 阳性四格',   '-en',        '*Ich sehe den kleinen Tisch.'],
            ['定冠词 + 复数',       '-en',        '*die kleinen Sachen'],
            ['不定冠词 + 阳性',     '-er',        '*ein kleiner Tisch'],
            ['不定冠词 + 阴性',     '-e',         '*eine kleine Lampe'],
            ['不定冠词 + 中性',     '-es',        '*ein kleines Bett'],
        ]),
        ('w', '一个实用的偷懒法：<b>定冠词后面基本写 -e，复数和阳性四格写 -en</b>，'
              '八成场合就对了。剩下两成读得懂就行，A1 不会因为这个扣掉及格线。'),

        ('r', '比较级与最高级', '规则是加 -er 和 am …-sten，但最常用的几个不规则。'),
        ('tab', ['原级', '比较级', '最高级'], [
            ['klein 小',  '*kleiner',  '*am kleinsten'],
            ['schnell 快', '*schneller', '*am schnellsten'],
            ['gut 好',    '*besser',   '*am besten'],
            ['viel 多',   '*mehr',     '*am meisten'],
            ['gern 喜欢', '*lieber',   '*am liebsten'],
        ]),
        ('t', '比较时用 <b>als</b>（比），同级用 <b>so … wie</b>（和…一样）。'),
        ('bsp', [
            ('Der Zug ist schneller als der Bus.', '火车比公交快。'),
            ('Ich trinke lieber Tee als Kaffee.', '比起咖啡我更爱喝茶。'),
            ('Mein Bruder ist so groß wie ich.', '我哥和我一样高。'),
            ('Das Zimmer ist nicht sehr groß, aber sehr hell.', '房间不大，但很亮堂。'),
        ]),
    ],
},

# ============ 12. 命令式 ============
{
    'id': 'imperativ', 'no': 12,
    'title': '命令式与试卷指令',
    'sub': '让别人做某事 · 看懂题目在要求什么',
    'why': '考纲要求 du / ihr / Sie 三种命令式。而更现实的理由是：'
           '<b>试卷上每一道题的指令语本身就是命令式</b>——看不懂指令，会做也答不对。',
    'blocks': [
        ('r', '三种形式', 'Sie 形式最常用，也最简单：动词原样 + Sie。'),
        ('tab', ['对谁', '怎么变', '例子'], [
            ['Sie（您）',  '动词 + Sie',        '*Kommen Sie bitte mit!'],
            ['du（你）',   'du 形式去掉 -st',    '*Komm bitte nach Hause!'],
            ['ihr（你们）', '和 ihr 形式一样，去掉主语', '*Kommt bitte alle mit!'],
        ]),
        ('w', '换元音的动词在 du 命令式里<b>不换回来</b>：'
              'du fährst → <b>Fahr!</b>（不是 Fähr）。<br>'
              '但 e→i 的换元音要保留：du sprichst → <b>Sprich!</b>'),
        ('t', '加上 <b>bitte</b> 语气就客气了，口语考试里提要求一定要带上。'),
        ('bsp', [
            ('Sprechen Sie bitte langsamer!', '请您说慢一点。'),
            ('Mach bitte das Fenster zu!', '请把窗户关上。'),
            ('Kommen Sie bitte um neun Uhr!', '请您九点来。'),
        ]),

        ('r', '试卷上的指令语', '这些词看不懂，题就无从下手。全部是 Sie 命令式。'),
        ('tab', ['指令', '意思'], [
            ['*Kreuzen Sie an.',       '打叉选择'],
            ['*Markieren Sie.',        '标出来'],
            ['*Ergänzen Sie.',         '补全'],
            ['*Ordnen Sie zu.',        '配对连线'],
            ['*Schreiben Sie.',        '写'],
            ['*Lesen Sie den Text.',   '读这段文字'],
            ['*Hören Sie zweimal.',    '听两遍'],
            ['*Wählen Sie die richtige Lösung.', '选出正确答案'],
        ]),
        ('drill', 'pruef', '去练：考试指令语与救场句'),
    ],
},

# ============ 13. 连句与构词 ============
{
    'id': 'verbinden', 'no': 13,
    'title': '连句与构词',
    'sub': 'und / aber / denn · 长词怎么拆',
    'why': '连词决定了后面的语序，接错了整句就散了。'
           '而德语的长复合词看着吓人，其实拆开全是学过的词——这是阅读题的救命技能。',
    'blocks': [
        ('r', 'und / oder / aber / denn：语序不变',
              '这四个只是把两个完整句子接起来，<b>后面那句照常「动词第二位」</b>。'),
        ('bsp', [
            ('Ich hätte gern eine Cola und ein Brötchen.', '我要一杯可乐和一个小面包。'),
            ('Möchten Sie lieber Tee oder Kaffee?', '您想要茶还是咖啡？'),
            ('Das ist schön, aber leider zu teuer.', '这个很好看，可惜太贵了。'),
            ('Ich gehe nicht spazieren, denn es ist zu kalt.', '我不去散步了，因为太冷。'),
        ]),
        ('w', '<b>dann</b> 不一样：它是副词，占掉第一位，所以后面<b>动词紧跟着来，主语挪后</b>。<br>'
              'Ich muss noch telefonieren, <b>dann gehen wir</b>.（不是 dann wir gehen）'),
        ('t', '还有一个 <b>wenn</b>（如果 / 当…时），它引出从句，'
              '<b>从句里的动词要跑到最末尾</b>。A1 只要能听懂，不要求自己造。'),
        ('bsp', [
            ('Wenn ich Zeit habe, komme ich mit.', '我要是有时间就一起去。'),
        ]),

        ('r', '动词决定句子还缺什么', '考纲把这叫 Verbergänzung，五种补足成分。'),
        ('tab', ['补什么', '哪些动词', '例子'], [
            ['主格',   'heißen / sein', '*Er heißt Heinz Bartels.'],
            ['四格',   '大多数动词',     '*Ich nehme eine Cola.'],
            ['三格',   'danken / gehören / geben / helfen', '*Gib mir dein Wörterbuch.'],
            ['地点',   'wohnen / liegen', '*Wir wohnen in der Heinestraße 7.'],
            ['性质',   'sein + 形容词',   '*Der Film ist langweilig.'],
        ]),

        ('r', '复合词：从后往前读', '德语可以把好几个词粘成一个。'
              '<b>最后一个词决定意思和性别</b>，前面的都是修饰。'),
        ('tab', ['复合词', '拆开', '性别跟谁'], [
            ['*die Reisegruppe',  'Reise + Gruppe',   'die Gruppe'],
            ['*der Bahnhofsplatz', 'Bahnhof + Platz', 'der Platz'],
            ['*das Kinderbett',   'Kinder + Bett',    'das Bett'],
        ]),
        ('t', '所以看到不认识的长词别慌，<b>先找最后那一截</b>——那才是它到底是什么。'),

        ('r', '几个高频后缀', '认得它们，生词也能猜个八九不离十。'),
        ('tab', ['后缀', '作用', '例子'], [
            ['-er',   '做这件事的人', '*der Arbeiter'],
            ['-in',   '女性形式',     '*die Kollegin'],
            ['-ung',  '动词变名词',   '*die Wohnung'],
            ['un-',   '否定',        '*unbekannt'],
            ['-los',  '没有…的',     '*arbeitslos'],
            ['-bar',  '可以…的',     '*erreichbar'],
        ]),
    ],
},
]
