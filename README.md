# 德语 A1 · Goethe 备考闪卡

手机端 H5 学德语应用，面向 **Goethe-Zertifikat A1（Start Deutsch 1）** 考试，
按官方词表编排，**685 个词条 + 第 0 关发音**。
单个 `index.html`，**零外部请求、可离线使用**，浏览器打开即可。

面向零基础纯自学：不假设你手里有教材或老师，从字母表开始，到考试题型结束。

## 功能

**第 0 关 · 发音**

学德语最早也最大的一次正反馈——德语拼读规则性强，这一关过了，看到任何生词都能读出来。
编写主线是**拆掉英语干扰**：有英语底子的人，直觉在德语里大量失效（`w` 读 /v/、`v` 读 /f/、
`j` 读 /j/、`z` 读 /ts/、`ie` 读长 i 而 `ei` 读 ai），不点破会一路读错。

- 字母表 30 个（含 ä ö ü ß），标注**字母名的读音**——口语 Teil 1 要求拼写自己的名字，字母名本身就是考点
- 发音规则 28 条，分五组：英语干扰 · 元音长短 · 特殊组合 · 词尾清化 · 重音。
  每条给 IPA、四个例词、中文说明，会踩英语坑的另配一条黄底提示
- 最小对立对 10 组（`Tür/Tur`、`Staat/Stadt`、`schön/schon`…），针对中文母语者的听辨盲区
- 页面上任何德语词都能点着听

**词汇**

- 词条全部来自官方 `A1_SD1_Wortliste`，**性别、复数、例句都是官方原文**
- **der / die / das 三色编码**，全应用一致。名词永远和它的颜色一起出现，
  靠颜色形成条件反射，比背这三个字管用；复数一律用 die 的颜色，因为所有复数都是 die
- 复数由官方标记程序化展开（`der Apfel, -Ä` → `die Äpfel`），构建期自检
- 词表按官方缩进还原了派生关系（`die Arbeit` 挂在 `arbeiten` 名下），卡背显示同词族

**记忆**

- 三档自评 + 间隔重复：即时 / 10 分钟 / 1 天 / 3 天 / 7 天 / 21 天；「忘记」的词本轮末尾再出现一次
- 首页有今日到期复习、按词性进度、难词本
- 词表支持搜索与「遮住例句」自测
- 进度存 `localStorage`，离线保留

**其他**

- 朗读走系统 TTS（Web Speech API），优先选 `de-DE` 语音，语速可调，另有固定 0.4 倍的慢速
- 浅色 / 深色主题（基于 `light-dark()` + `color-scheme`）
- 内嵌 Figtree 可变字体（OFL），latin-ext 子集覆盖 IPA 扩展区与 ä ö ü ß

## 使用

直接用浏览器打开 `index.html` 即可。手机上可用局部静态服务：

```bash
python3 -m http.server 8778
```

然后手机访问 `http://<电脑 IP>:8778`。在 Safari 里「添加到主屏幕」后是全屏 App 形态。

## 从源码构建

官方素材（词表 PDF、模拟考音频）不入库，需先按 `materials/README.md` 里的地址自行下载。

```bash
python3 src/parse_wortliste.py materials/official/A1_SD1_Wortliste_02.pdf   # 解析词表 → src/wortliste.json
python3 src/build.py                                                       # 生成 index.html
```

| 文件 | 说明 |
| --- | --- |
| `src/parse_wortliste.py` | 解析官方词表 PDF：按页现算基准列、展开复数标记、合并折行复合词 |
| `src/wortliste.json` | 解析产物，687 条 |
| `src/aussprache.py` | 第 0 关发音内容（字母表 / 规则 / 最小对立对），手工编写 |
| `src/tpl.html` | 应用模板，含样式、逻辑与内嵌字体，`__DATA__` 为数据占位符 |
| `src/build.py` | 合成数据并注入模板，产出根目录 `index.html`（含构建期自检） |
| `src/share.html` | 分享卡片设计稿，复用应用内嵌的 Figtree |
| `src/make_share.py` | Chrome headless 出图：`share.jpg` / `share-square.jpg` / 图标 |
| `PRODUCT.md` | 产品文档：考试对标、学习方法、功能规划 |

换域名时改 `src/build.py` 顶部的 `BASE` 一行再重新构建即可——`og:image`
必须是绝对地址，模板里统一用 `__BASE__` 占位。分享图改动后需重跑
`python3 src/make_share.py`。

`parse_wortliste.py` 里有一份 `QUELLE_FIX`，记录官方 PDF 的排印疏漏
（如 `die Adresse,-en` 按字面会拼出 `Adresseen`）。新发现的错处加在那里，附上原文写法。

## 说明

- 词表数据来自 Goethe-Institut 公开的 A1 官方备考材料，仅作个人学习之用；素材本身不随本仓库分发
- 发音规则与中文说明为人工编写，欢迎指正
- 界面配色、圆角、字阶与动效曲线取自 [Astryx](https://astryx.atmeta.com/) design tokens
- 字体 [Figtree](https://fonts.google.com/specimen/Figtree) 以 SIL Open Font License 1.1 授权
