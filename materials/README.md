# 素材清单

全部来自 Goethe-Institut 官网公开的备考材料，供本项目开发与个人学习使用。
下载日期：2026-08-06。

---

## official/ —— 官方 PDF（5 份，11.3 MB）

| 文件 | 页数 | 内容与用途 |
| --- | --- | --- |
| `A1_SD1_Wortliste_02.pdf` | 29 | **官方词表。项目最核心的数据源。** 见下方格式说明 |
| `Pruefungsziele_Testbeschreibung_A1_SD1.pdf` | 110 | 考试目标与题型详解。第 26–53 页 Prüfungsformen 用于核对题型；第 100–106 页是 A1 语法结构清单 |
| `sd_1_modellsatz.pdf` | 47 | 官方模拟题（完整一套） |
| `sd_1_uebungssatz01.pdf` | 47 | 官方练习题 01 |
| `sd_1_uebungssatz02.pdf` | 47 | 官方练习题 02 |
| `Durchfuehrungsbestimmungen_A1_Start_Deutsch_1.pdf` | 16 | 考试实施细则（时长、评分、及格线） |

### 词表格式（决定了数据模型）

`A1_SD1_Wortliste_02.pdf` 的结构：

- **第 4 页 Themen** —— 官方主题清单（Person / Wohnen / Umwelt / Essen-Trinken /
  Reisen-Verkehr / Einkaufen-Gebrauchsartikel …）。**应作为应用的主题分组依据**，
  不要自己另起一套。
- **第 6–8 页 Wortgruppenliste** —— 按词群列出：数字、时间、星期、月份、季节、
  货币、度量衡、国家与国籍。`21 = einundzwanzig` 在此明列，
  印证了 PRODUCT.md 5.1 的数字倒读专项。
- **第 9–27 页 Alphabetische Wortliste** —— 字母序全表，每条形如：

```
der Apfel, -Ä              Ein Pfund Äpfel bitte.
die Adresse, -n            Wie ist Ihre Adresse?
der Arbeitsplatz, -ä, e    An meinem Arbeitsplatz fehlt ein Drucker.
arbeiten                   Wo arbeiten Sie?
  die Arbeit, -en          Mein Bruder sucht Arbeit.
```

**性别、复数、例句官方直接给全**，缩进表示派生关系（`die Arbeit` 属于 `arbeiten`）。
试解析：名词 324 条、非名词 321 条，复数标记规整可程序化
（`-n` 45 · `-e` 31 · `-s` 19 · `-ä, e` 变音复数 9 …）。

> 这意味着 PRODUCT.md 第 7 节数据模型里的 `art` / `pl` / `ex` 三个字段可自动填充，
> 人工只需补音标、发音规则、中文释义与句框拆解。

---

## modellsatz_online/ —— 官方在线模拟考（57 MB）

抓自 <https://bfu.goethe.de/a1_sd1/>，是官方无障碍版在线模拟考的完整素材。

| 目录 | 数量 | 说明 |
| --- | --- | --- |
| `audio/` | 51 | **听力音频，总时长约 20 分钟。** 容器是 mp4（h264 + aac），单段 11–20 秒 |
| `bilder/` | 76 | 听力与阅读题的配图（gif/jpg） |
| `pages/` | 6 | 四个模块的题目页面 HTML，含题干、选项与正确答案结构 |

音频命名规律：

- `A1_mod_A*_V1.mp4` —— 模拟题各题音频
- `audio1_*` / `audio2_*` / `audio3_*` —— 听力三个部分
- `goe_a1_TR*.mp4` —— 朗读稿（Transkript）音频
- `audio_bsp*.mp4` —— 例题

> **这些是真人录音**，可用于 PRODUCT.md 4.6「最小对立对听辨」的备选方案——
> 若 TTS 合成音的长短元音区分度不足，可从这里取真实语音片段。

未取到 `Pfeil_links.gif` 与 `print.gif`（页面 UI 图标，与内容无关）。

---

## 尚缺

- **教材**（Menschen / Netzwerk neu / Schritte international neu）——
  商业出版物。若课程指定了某一本，需按其进度编排章节顺序；纯自学则按官方 Themen 组织即可。
- 更多 Übungssatz（官网目前只提供 01、02 两套）

---

## 来源

- 词表 <https://www.goethe.de/pro/relaunch/prf/de/A1_SD1_Wortliste_02.pdf>
- 测试说明 <https://www.goethe.de/pro/relaunch/prf/de/Pruefungsziele_Testbeschreibung_A1_SD1.pdf>
- 模拟题 <https://www.goethe.de/pro/relaunch/prf/materialien/A1_sd1/sd_1_modellsatz.pdf>
- 练习题 01 <https://www.goethe.de/pro/relaunch/prf/materialien/A1_sd1/sd_1_uebungssatz01.pdf>
- 练习题 02 <https://www.goethe.de/pro/relaunch/prf/materialien/A1_sd1/sd_1_uebungssatz02.pdf>
- 实施细则 <https://www.goethe.de/pro/relaunch/prf/de/Durchfuehrungsbestimmungen_A1_Start_Deutsch_1.pdf>
- 在线模拟考 <https://bfu.goethe.de/a1_sd1/>
