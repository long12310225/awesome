![](https://raw.githubusercontent.com/jagracey/Awesome-Unicode/58f28d08aef7f36eb6cdca22d25e7654cd8de5ae/resources/banner.jpg)


# 很棒的统一码 [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)



> 令人愉快的 Unicode 花絮、软件包和资源的精选列表。

*贡献前请阅读[贡献指南](CONTRIBUTING.md)。*
*关键 Unicode 术语在 [词汇表](GLOSSARY.md) 中定义。*

*交叉发布到[Wisdom的开发博客](https://wisdom.engineering/awesome-unicode/)*

<br><br>

# 前言

统一码太棒了！在 Unicode 出现之前，国际交流非常困难 - 每个人都在 ASCII 的上半部分（称为代码页）定义了各自的扩展字符集，这会发生冲突 - 试想一下，说德语的人与说韩语的人协调使用哪个 127 个字符的代码页。值得庆幸的是，Unicode 标准流行起来并统一了通信。 Unicode 8.0 对来自超过 129 种文字的 120,000 多个字符进行了标准化 - 一些是现代的，一些是古代的，还有一些尚未破译。 Unicode 处理从左到右和从右到左的文本、组合标记，并包括不同的文化、政治、宗教字符和表情符号。 Unicode 非常人性化——但最终却被低估了。

<br>

# 内容

- [快速 Unicode 背景](#quick-unicode-background)
	- [Unicode 标准包含哪些字符？](#what-characters-does-the-unicode-standard-include)
	- [Unicode 字符编码](#unicode-character-encodings)
	- [让我们谈谈数字](#lets-talk-numbers)
	- [UTF-16 代理对](#utf-16-surrogate-pairs)
	- [计算代理对](#calculating-surrogate-pairs)
	- [组合与分解](#composing--decomposing)
	- [统一码的神话](#myths-of-unicode)
	- [应用的 Unicode 编码](#applied-unicode-encodings)
	- [源代码](#source-code)
- [很棒的角色列表](#awesome-characters-list)
	- [特殊字符](#special-characters)
	- [变量标识符可以有效地包含空格！](#variable-identifiers-can-effectively-include-whitespace)
	- [Modifiers](#modifiers)
	- [大写转换碰撞](#collision-uppercase-transformation-collisions)
	- [小写转换碰撞](#collision-lowercase-transformation-collisions)
- [怪癖和故障排除](#quirks-and-troubleshooting)
	- [一对多案例映射](#one-to-many-case-mappings)
- [很棒的包和库](#awesome-packages--libraries)
- [Emojis](#emojis)
	- [Diversity](#diversity)
- [创造性地命名变量和方法](#creatively-naming-variables-and-methods)
	- [递归 HTML 标签重命名脚本](#recursive-html-tag-renaming-script)
- [统一字体](#unicode-fonts)
- [更多阅读](#more-reading)
- [深入探索 Unicode 自身](#exploring-deeper-into-unicode-yourself)
- [概览图](#overview-map)
	- [基本多语言平面地图](#a-map-of-the-basic-multilingual-plane)
	- [Unicode 块](#unicode-blocks)
- [Unicode 标准的原则](#principles-of-the-unicode-standard)
- [统一码版本](#unicode-versions)
- [Contributing](#contributing)
- [行为准则](#code-of-conduct)
- [License](#license)


# 快速 Unicode 背景

## Unicode 标准包含哪些字符？

Unicode 标准定义了当今所有主要语言中使用的字符代码。文字包括欧洲字母文字、中东从右到左文字和许多亚洲文字。

Unicode 标准还包括标点符号、变音符号、数学符号、技术符号、箭头、装饰符号、表情符号等。它提供变音符号代码，这些变音符号修改字符标记，例如波形符 (~)，与基本字符结合使用来表示重音字母（例如ñ）。总之，Unicode 标准 9.0 版为来自世界各地的字母表、表意文字集和符号集的 128,172 个字符提供了代码。

大多数常用字符都适合前 64K 代码点，该代码空间的区域称为基本多语言平面，简称 BMP。还有 16 个其他补充平面可用于对其他字符进行编码，目前有超过 850,000 个未使用的代码点。正在考虑在该标准的未来版本中添加更多字符。

Unicode 标准还保留代码点供私人使用。供应商或最终用户可以在内部为自己的字符和符号分配这些字符和符号，或将它们与专用字体一起使用。 BMP 上有 6,400 个专用代码点，另外还有 131,068 个补充专用代码点（如果 6,400 个代码点不足以满足特定应用的需要）。



## Unicode 字符编码

字符编码标准不仅定义每个字符的标识及其数值或代码点，还定义该值如何以位表示。

Unicode 标准定义了三种编码形式，允许以字节、字或双字格式（即每个代码单元 8、16 或 32 位）传输相同的数据。所有三种编码形式都编码相同的通用字符库，并且可以有效地相互转换而不会丢失数据。 Unicode 联盟完全认可使用任何这些编码形式作为实现 Unicode 标准的一致方式。

UTF-8 在 HTML 和类似协议中很流行。 UTF-8 是一种将所有 Unicode 字符转换为可变长度字节编码的方法。它的优点是，与熟悉的 ASCII 集相对应的 Unicode 字符具有与 ASCII 相同的字节值，并且转换为 UTF-8 的 Unicode 字符可以与许多现有软件一起使用，而无需进行大量的软件重写。

UTF-16 在许多需要平衡字符的高效访问和存储的经济使用的环境中很流行。它相当紧凑，所有频繁使用的字符都适合单个 16 位代码单元，而所有其他字符都可以通过成对的 16 位代码单元访问。

当不关心内存空间，但需要固定宽度、单个代码单元访问字符时，UTF-32 非常有用。使用 UTF-32 时，每个 Unicode 字符都以单个 32 位代码单元进行编码。

所有三种编码形式每个字符最多需要 4 个字节（或 32 位）数据。




## 让我们谈谈数字


Unicode 字符集分为 17 个称为“平面”的核心段，这些核心段又进一步分为块。每个平面有 65,536 (216) 个代码点的空间，总共支持 1,114,112 个代码点。有两个“私人使用区域”平面（#16 和 #17），可以根据需要分配使用。这两架私人用途飞机共有 131,072 个代码点。

| \# |名称 |范围 |
|-----|-----------------------------------------|------------------------|
| 1.| **基本多语言飞机** | （U+0000 到 U+FFFF）|
| 2.| **补充多语言飞机** | （U+10000 到 U+1FFFF）|
| 3.| **补充表意平面** | （U+20000 到 U+2FFFF）|
| 4.|第三表意平面| （U+30000 至 U+3FFFF）|
| 5.|飞机 5（未分配）| （U+40000 至 U+4FFFF）|
| 6.|飞机 6（未分配）| （U+50000 至 U+5FFFF）|
| 7.| 7 号飞机（未分配）| （U+60000 至 U+6FFFF）|
| 8.|飞机 8（未分配）| （U+70000 至 U+7FFFF）|
| 9.|飞机 9（未分配）| （U+80000 到 U+8FFFF）|
| 10.| 10 号飞机（未分配）| （U+90000 到 U+9FFFF）|
| 11.| 11 号飞机（未分配）| （U+A0000 至 U+AFFFF）|
| 12.| 12 号飞机（未分配）| （U+B0000 至 U+BFFFF）|
| 13.| 13 号飞机（未分配）| （U+C0000 至 U+CFFFF）|
| 14.| 14 号飞机（未分配）| （U+D0000 至 U+DFFFF）|
| 15.| **补充专用飞机** | （U+E0000 至 U+EFFFF）|
| 16.| **补充私人使用区 - A** | （U+F0000 至 U+FFFFF）|
| 17.| **补充私人使用区 - B** | （U+100000 到 U+10FFFF）|


第一个平面称为基本多语言平面或 BMP。它包含从 U+0000 到 U+FFFF 的代码点，这是最常用的字符。其他十六个位面（U+010000 → U+10FFFF）称为辅助位面或星界位面。




## UTF-16 代理对
> BMP 之外的字符，例如U+1D306 中心四元组 (𝌆)，只能使用两个 16 位代码单元以 UTF-16 进行编码：0xD834 0xDF06。这称为代理对。请注意，代理对仅代表单个字符。
代理对的第一个代码单元始终在 0xD800 到 0xDBFF 范围内，称为高代理或前导代理。
代理对的第二个代码单元始终在 0xDC00 到 0xDFFF 范围内，称为低代理或尾代理。

-- [Mathias Bynens](https://mathiasbynens.be/notes/javascript-encoding#surrogate-pairs)

> 代理对：单个抽象字符的表示，由
两个 16 位代码单元的序列，其中该对的第一个值是高代理项
代码单元，第二值是低代理代码单元。代理对仅在 UTF-16 中使用。 （参见第 3.9 节，Unicode 编码
形式。） -- [Unicode 8.0.0 第 3 章 - 代理](http://unicode.org/versions/Unicode8.0.0/ch03.pdf#page=47)


## 计算代理对

UTF-16 中的 Unicode 字符 **💩 Pile of Poo (U+1F4A9)** 必须编码为代理对，即两个代理。要将任何代码点转换为代理对，请使用以下算法（在 JavaScript 中）。请记住，我们使用的是十六进制表示法。

```javascript
 var High_Surrogate = function(Code_Point){ return Math.floor((Code_Point - 0x10000) / 0x400) + 0xD800 };
 var Low_Surrogate  = function(Code_Point){ return (Code_Point - 0x10000) % 0x400 + 0xDC00 };

 // Reverses The Conversion
 var Code_Point = function(High_Surrogate, Low_Surrogate){
	return (High_Surrogate - 0xD800) * 0x400 + Low_Surrogate - 0xDC00 + 0x10000;
 };
```

```javascript
 > var codepoint = 0x1F4A9;   								// 0x1F4A9 == 128169
 > High_Surrogate(codepoint).toString(16)
 "d83d"  													// 0xD83D == 55357
 > Low_Surrogate(codepoint).toString(16)
 "dca9"  													// 0xDCA9 == 56489

 > String.fromCharCode(  High_Surrogate(codepoint) , Low_Surrogate(codepoint) );
  "💩"
> String.fromCodePoint(0x1F4A9)
  "💩"
 > '\ud83d\udca9'
  "💩"
```



## 组合与分解
Unicode 包含一种修改字符形状的机制，极大地扩展了支持的字形库。这涵盖了组合变音标记的使用。它们被插入到主角之后。多个组合变音符号可以堆叠在同一字符上。 Unicode 还包含正常使用的大多数字母/变音符号组合的预组合版本。



某些字符序列也可以表示为单个字符，称为预组合字符（或复合或可分解字符）。例如，字符“ü”可编码为单个代码点 U+00FC“ü”，或编码为基本字符 U+0075“u”，后跟非空格字符 U+0308“¡”。 Unicode 标准对预组合字符进行编码，以便与现有标准（例如 Latin 1）兼容，其中包括许多预组合字符，例如“ü”和“ñ”。

为了一致性或分析，可以分解预组合字符。例如，在按字母顺序排列（整理）名称列表时，字符“ü”可以分解为“u”，后跟非空格字符“¡”。一旦字符被分解，排序规则就可以更容易地处理该字符，因为它可以被处理为经过修改的“u”。这使得字符修饰符不影响字母顺序的语言可以更轻松地按字母顺序排序。 Unicode 标准定义了所有预组合字符的[分解](http://unicode.org/versions/Unicode8.0.0/ch03.pdf#page=44)。它还定义了规范化形式以提供字符的独特表示。


## 统一码的神话
*摘自 Mark Davis 的 [Unicode Myths](http://macchiato.com/slides/UnicodeMyths.pdf) 幻灯片。*
- **Unicode 只是一个 16 位代码** - 有些人错误地认为 Unicode 只是一个 16 位代码，其中每个字符占用 16 位，因此可能有 65,536 个字符。实际上，这是不正确的。这是关于 Unicode 的最常见的误解，所以如果您这么认为，请不要感到难过。

- **您可以使用任何未分配的代码点供内部使用** - 不。最终该漏洞将由不同的字符填充。而是使用私人使用或非字符。

- **每个 Unicode 代码点代表一个字符** - 不。有很多非字符（FFFE、FFFF、1FFFE，...）
还有代理代码点、私有和未分配的代码点以及控制/格式“字符”（RLM、ZWNJ，...）

- **Unicode 将耗尽空间** - 如果是线性的，我们将在公元 2140 年耗尽空间。但它不是线性的。请参阅http://www.unicode.org/roadmaps/

- **案例映射为 1-1** - 否。它们也可以是：
- 一对多：(ß → SS )
- 上下文：(…Σ ↔ …ς AND …ΣΤ… ↔ …στ… )
- 区域设置敏感：( I ↔ ı AND й ↔ i )




## 应用的 Unicode 编码


|编码类型 |  原始编码 |
|---------------------------|---------------------------------------|
|HTML 实体（十进制）| &#128406;								|
|HTML 实体（十六进制）| &#x1F596;								|
|URL 转义代码 | %F0%9F%96%96 | %F0%9F%96%96 |
|UTF-8（十六进制）| 0xF0 0x9F 0x96 0x96 (f09f9696) | 0xF0 0x9F 0x96 0x96 (f09f9696)
|UTF-8（二进制）| 11110000:10011111:10010110:10010110 |
|UTF-16/UTF-16BE（十六进制）| 0xD83D 0xDD96（d83ddd96）|
|UTF-16LE（十六进制）| 0x3DD8 0x96DD（3dd896dd）|
|UTF-32/UTF-32BE（十六进制）| 0x0001F596（0001f596）|
|UTF-32LE（十六进制）| 0x96F50100 (96f50100) |
|八进制转义序列| \360\237\226\226 |


## 源代码
|编码类型|原始编码|
|-------------|-------------|
| JavaScript | §596 |
| JSON | §596 |
| C | §596 |
| C++ | §596 |
|爪哇 | §596 |
|蟒蛇 | §596 |
|珀尔| \x{1F596} |
|红宝石 | \u{1F596} |
| CSS | \01F596 |






# 很棒的角色列表




<中心>
[![](http://imgs.xkcd.com/comics/rtl.png )](https://xkcd.com/1137/)
</中心>

## 特殊字符

Unicode 联盟发布了一个[通用标点符号图表](http://www.unicode.org/charts/PDF/U2000.pdf)，您可以在其中找到更多详细信息。


|查尔 |名称 |描述 |
|----------|------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ````'` | U+FEFF（字节顺序标记 - BOM）|在字节重新排序上具有明确的重要属性。它也是零宽度且不可见的。在不合规的软件（如 PHP 解释器）中，这会导致各种有趣的行为。 |
| `'￯'` | '\\uFFEF' 反转字节顺序标记 (BOM) |不等于除文本开头之外的合法字符。                                                                                                                        |
| `'​'` | '\\u200B' 零宽度不间断空格 | （没有外观且除了防止连字形成之外没有任何作用的字符）。                                                                                               |
| `````` | U+00A0 不间断空格 |强制相邻的字符粘在一起。在 HTML 中众所周知的“&nbsp;”。                                                                                                                          |
| ````` | U+00AD 软连字符 | （在 HTML 中：）类似于 ZERO WIDTH SPACE，但如果（且仅当）发生中断时显示连字符。                                                                                                         |
| ```` | U+200D 零宽度连接器 |强制将相邻字符连接在一起（例如阿拉伯字符或支持的表情符号）。可以用它来组成顺序组合的表情符号。                                         |
| '''` | U+2060 字连接器 |与U+00A0相同，但完全不可见。适合在 Twitter 上写@font-face。                                                                                                          |
| `` '` | U+1680 奥格姆空间标记 |一个看起来像破折号的空格。太棒了，让程序员接近疯狂：1 +  2 === 3。 |
| ``;'` | U+037E 希腊问号 |与分号类似。这也是一种惹恼开发人员的有趣方式。                                                                                                                             |
| ````` | U+202D |将文本方向更改为从左到右。                                                                                                                                                    |
| ````` | U+202E |将文本方向更改为从右到左： |
| ''ꓸ'` | U+A4F8 傈僳语字母音调 MYA TI |与时期字符相似。 |
| ''ꓹ'` | U+A4F9 傈僳字母声调 NA PO |与逗号字符相似。|
| ''ꓼ'` | U+A4FC 傈僳族字母声调 MYA NA |与分号字符相似。|
| ''ꓽ'` | U+A4FD 傈僳族字母音 MYA JEU|与冒号字符相似。|
| `'︀'` | **变体选择器**（U+FE00 至 U+FE0F 和 U+E0100 至 U+E01EF）|具有 ID_Continue 属性的 256 个零宽度字符的块，这意味着它们可以在变量名称中使用（不是第一个字母）。这些特殊之处在于，鼠标光标在组合字符时会经过它们 - 与大多数其他零宽度字符不同。
| `'ᅟ'` | **U+115F 韩文初声填充词** |一般来说，它会产生一个空间。如果渲染中未明确支持，则渲染为零宽度（不可见）。指定ID_Start|
| `'ᅠ'` | **U+1160 韩文中城填充词** |也许它产生了一个空间？如果渲染中未明确支持，则渲染为零宽度（不可见）。指定ID_Start|
| ''ㅤ'` | **U+3164 朝鲜文填充符** |一般来说，它会产生一个空间。如果渲染中未明确支持，则渲染为零宽度（不可见）。指定ID_Start |
<br><br>
#### 等一下...我刚刚读到了什么？


<br><br>
## 变量标识符可以有效地包含空格！

**U+3164 HANGUL FILLER** 字符显示为前进的空白字符。如果没有明确[渲染中支持](http://unicode.org/faq/unsup_char.html)，则字符将渲染为完全不可见（并且不前进，即“零宽度”）。这意味着永远不应该显示丑陋的字符替换 (�) 符号。

我还不确定为什么 U+3164 被指定为这种方式。有趣的是，U+3164 在 1.1 版（1993 年）中被添加到 Unicode 中——所以联盟一定花了很多时间来考虑。无论如何，这里有几个例子。

```javascript
> var ᅟ = 'foo';
undefined
> ᅟ
'foo'


> var ㅤ= alert;
undefined
> var foo = 'bar'
undefined
> if ( foo ===ㅤ`baz` ){} 	// alert
undefined


> var varㅤfooㅤ\u{A60C}ㅤπ = 'bar';
undefined
> varㅤfooㅤꘌㅤπ
'bar'

```
<br>
**注意：** 我已经在 Ubuntu 和 OS X 上使用以下命令测试了 U+3164 渲染：`node`、`php`、`ruby`、`python3.5`、`scala`、`vim`、`cat`、`chrome`+`github gist`。 Atom 是唯一一个因（错误地）显示空框而失败的系统。我还没有在 Emacs 和 Sublime 上测试过它。据我了解，Unicode 联盟不会重新分配或重命名字符或代码点，但可能会说服更改 ID_Start/ID_Continue 等字符属性。


<br>



## 修饰符

零宽度连接符 (ZWJ) 是一种非打印字符，用于某些复杂脚本（例如阿拉伯脚本或任何印度脚本）的计算机排版。当放置在两个原本不会连接的字符之间时，ZWJ 会使它们以其连接的形式打印。

零宽度非连接符 (ZWNJ) 是一种非打印字符，用于使用连字的书写系统的计算机化中。当放置在本来会连接成连字的两个字符之间时，ZWNJ 会使它们分别以其最终形式和初始形式打印。这也是空格字符的效果，但当需要使单词更靠近或将单词与其语素连接时，可以使用 ZWNJ。



```javascript
> 'a'
 "a"

> 'a\u{0308}'
 "ä"

> 'a\u{20DE}\u{0308}'
 "a⃞̈"

> 'a\u{20DE}\u{0308}\u{20DD}'
 "a⃞̈⃝"

// Modifying Invisible Characters
> '\u{200E}\u{200E}\u{200E}\u{200E}\u{200E}\u{200E}\u{200E}\u{200E}\u{200E}\u{200E}'
 "‎‎‎‎‎‎‎‎‎‎"

> '\u{200E}\u{200E}\u{200E}\u{200E}\u{200E}\u{200E}\u{200E}\u{200E}\u{200E}\u{200E}'.length
 10
```


## :collision: 大写转换碰撞

|查尔 |代码点|输出字符|
|------|------------|-------------|
| ß | 0x00DF | 0x00DF `SS` |
|我 | 0x0131 | 0x0131 ‘我’|
| ſ | 0x017F | 0x017F `S` |
| ff | 0xFB00 | 0xFB00 `FF` |
| fi | 0xFB01 | 0xFB01 `FI` |
|飞 | 0xFB02 | 0xFB02 '佛罗里达州' |
| ﬃ | 0xFB03 | 0xFB03 `FFI`|
| ﬄ | 0xFB04 | 0xFB04 `FFL`|
| ﬅ | 0xFB05 | 0xFB05 `ST` |
| ﬆ | 0xFB06 | `ST` |

## :collision: 小写变换碰撞
|查尔 |代码点|输出字符|
|------|------------|-------------|
|克 | 0x212A | 0x212A `k` |



# 怪癖和故障排除

- **字符串长度通常通过计算代码点来确定。**这意味着代理项对将计为两个字符。可以将多个变音符号组合在同一字符上。 `a + ̈ == ̈a `，增加长度，但仅产生单个字符。

- **同样，反转字符串通常是一项不简单的任务。**同样，代理项对和变音符号必须一起反转。 [ES Reverser](https://github.com/mathiasbynens/esrever) 提供了一个非常好的解决方案。

- **大小写映射并不总是一对一的。**它们也可以是：
- 一对多：(ß → SS )
- 上下文：(…Σ ↔ …ς AND …ΣΤ… ↔ …στ… )
- 区域设置敏感：( I ↔ ı AND й ↔ i )



### 一对多案例映射
*以下大多数字符在大写时表达其一对多大小写映射 - 而其他字符应小写。该列表应该分开*





|代码点|人物 |名称 |映射角色 |映射代码点 |
|-------------------------------------------------|-----------|--------------------------------------------------------------------------|------------------|------------------------|
| [U+00DF](https://codepoints.net/U+00DF?lang=en) | `ß` |拉丁文小写字母升号 S | `s`、`s` | U+0073，U+0073 |
| [U+0130](https://codepoints.net/U+0130?lang=en) | '我' |上面带点的拉丁文大写字母 I | `我`，`̇` | U+0069、U+0307 |
| [U+0149](https://codepoints.net/U+0149?lang=en) | `ŉ` |前面带有撇号的拉丁文小写字母 | ''`，`n` | U+02BC、U+006E |
| [U+01F0](https://codepoints.net/U+01F0?lang=en) | ``ϰ` |带抑扬符的拉丁文小写字母 J | `j`、`̌` | U+006A、U+030C |
| [U+0390](https://codepoints.net/U+0390?lang=en) | 'ΐ' |带有 DIALYTIKA 和 TONOS 的希腊小写字母 IOTA | `ι`、`̈`、`́` | U+03B9、U+0308、U+0301 |
| [U+03B0](https://codepoints.net/U+03B0?lang=en) | ``ΰ` |带有 DIALYTIKA 和 TONOS 的希腊小写字母 UPSILON | `υ`、`̈`、`́` | U+03C5、U+0308、U+0301 |
| [U+0587](https://codepoints.net/U+0587?lang=en) | `և` |亚美尼亚小连字 ECH YIWN | `ɥ`, `ւ` | U+0565、U+0582 |
| [U+1E96](https://codepoints.net/U+1E96?lang=en) | `ẖ` |带有下划线的拉丁文小写字母 H | `h`、`̱` | U+0068，U+0331 |
| [U+1E97](https://codepoints.net/U+1E97?lang=en) | `ẗ` |带分音符的拉丁文小写字母 T | `t`、`̈` | U+0074，U+0308 |
| [U+1E98](https://codepoints.net/U+1E98?lang=en) | `ẘ` |上面有环的拉丁文小写字母 W | `w`、`̊` | U+0077、U+030A |
| [U+1E99](https://codepoints.net/U+1E99?lang=en) | `ẙ` |上面有环的拉丁文小写字母 Y | `y`、`̊` | U+0079、U+030A |
| [U+1E9A](https://codepoints.net/U+1E9A?lang=en) | `ẚ` |带右半环的拉丁文小写字母 A | `a`, `ʾ` | U+0061，U+02BE |
| [U+1E9E](https://codepoints.net/U+1E9E?lang=en) | `ẞ` |拉丁文大写字母升号 S | `s`、`s` | U+0073，U+0073 |
| [U+1F50](https://codepoints.net/U+1F50?lang=en) | `ὐ` |带有 PSILI 的希腊小写字母 UPSILON | `υ`、`̓` | U+03C5，U+0313 |
| [U+1F52](https://codepoints.net/U+1F52?lang=en) | `ὒ` |带有 PSILI 和 VARIA 的希腊小写字母 UPSILON | `υ`、`̓`、`̀` | U+03C5、U+0313、U+0300 |
| [U+1F54](https://codepoints.net/U+1F54?lang=en) | `ὔ` |带有 PSILI 和 OXIA 的希腊小写字母 UPSILON | `υ`、`̓`、`́` | U+03C5、U+0313、U+0301 |
| [U+1F56](https://codepoints.net/U+1F56?lang=en) | `ὖ` |带有 PSILI 和 PERISPOMENI 的希腊小写字母 UPSILON | `υ`、`̓`、`͂` | U+03C5、U+0313、U+0342 |
| [U+1F80](https://codepoints.net/U+1F80?lang=en) | `ᾀ` |带有 PSILI 和 YPOGEGRAMMENI 的希腊小写字母 ALPHA | `ἀ`, `ι` | U+1F00，U+03B9 |
| [U+1F81](https://codepoints.net/U+1F81?lang=en) | `ᾁ` |带有 DASIA 和 YPOGRAMMENI 的希腊小写字母 ALPHA | `ἁ`, `ι` | U+1F01，U+03B9 |
| [U+1F82](https://codepoints.net/U+1F82?lang=en) | `ᾂ` |希腊小写字母 ALPHA 与 PSILI 和 VARIA 以及 YPOGRAMMENI | `ἂ`, `ι` | U+1F02、U+03B9 |
| [U+1F83](https://codepoints.net/U+1F83?lang=en) | `ᾃ` |希腊小写字母 ALPHA 与 DASIA 和 VARIA 以及 YPOGEGRAMMENI | `ἃ`, `ι` | U+1F03，U+03B9 |
| [U+1F84](https://codepoints.net/U+1F84?lang=en) | `ᾄ` |希腊小写字母 ALPHA 与 PSILI 和 OXIA 以及 YPOGRAMMENI | `ἄ`，`ι` | U+1F04，U+03B9 |
| [U+1F85](https://codepoints.net/U+1F85?lang=en) | `ᾅ` |带有 DASIA 和 OXIA 以及 YPOGRAMMENI 的希腊小写字母 ALPHA | `ἅ`，`ι` | U+1F05，U+03B9 |
| [U+1F86](https://codepoints.net/U+1F86?lang=en) | `ᾆ` |带有 PSILI 和 PERISPOMENI 和 YPOGRAMMENI 的希腊小写字母 ALPHA | `ἆ`, `ι` | U+1F06，U+03B9 |
| [U+1F87](https://codepoints.net/U+1F87?lang=en) | `ᾇ` |带有 DASIA 和 PERISPOMENI 和 YPOGRAMMENI 的希腊小写字母 ALPHA | `ἇ`，`ι` | U+1F07、U+03B9 |
| [U+1F88](https://codepoints.net/U+1F88?lang=en) | `ᾈ` |带有 PSILI 和 PROSGEGRAMMENI 的希腊大写字母 ALPHA | `ἀ`, `ι` | U+1F00，U+03B9 |
| [U+1F89](https://codepoints.net/U+1F89?lang=en) | `ᾉ` |带有 DASIA 和 PROSGEGRAMMENI 的希腊大写字母 ALPHA | `ἁ`, `ι` | U+1F01，U+03B9 |
| [U+1F8A](https://codepoints.net/U+1F8A?lang=en) | `ᾊ` |带有 PSILI 和 VARIA 以及 PROSGEGRAMMENI 的希腊大写字母 ALPHA | `ἂ`, `ι` | U+1F02、U+03B9 |
| [U+1F8B](https://codepoints.net/U+1F8B?lang=en) | `ᾋ` |希腊大写字母 ALPHA 与 DASIA 和 VARIA 以及 PROSGEGRAMMENI | `ἃ`, `ι` | U+1F03，U+03B9 |
| [U+1F8C](https://codepoints.net/U+1F8C?lang=en) | `ᾌ` |希腊大写字母 ALPHA 与 PSILI 和 OXIA 以及 PROSGEGRAMMENI | `ἄ`，`ι` | U+1F04，U+03B9 |
| [U+1F8D](https://codepoints.net/U+1F8D?lang=en) | `ᾍ` |希腊大写字母 ALPHA 与 DASIA 和 OXIA 以及 PROSGEGRAMMENI | `ἅ`，`ι` | U+1F05，U+03B9 |
| [U+1F8E](https://codepoints.net/U+1F8E?lang=en) | `ᾎ` |带有 PSILI 和 PERISPOMENI 和 PROSGEGRAMMENI 的希腊大写字母 ALPHA | `ἆ`, `ι` | U+1F06，U+03B9 |
| [U+1F8F](https://codepoints.net/U+1F8F?lang=en) | `ᾏ` |希腊大写字母 ALPHA 与 DASIA、PERISPOMENI 和 PROSGEGRAMMENI | `ἇ`，`ι` | U+1F07、U+03B9 |
| [U+1F90](https://codepoints.net/U+1F90?lang=en) | `ᾐ` |带有 PSILI 和 YPOGEGRAMMENI 的希腊小写字母 ETA | `ἠ`, `ι` | U+1F20，U+03B9 |
| [U+1F91](https://codepoints.net/U+1F91?lang=en) | `ᾑ` |带有 DASIA 和 YPOGEGRAMMENI 的希腊小写字母 ETA | `ἡ`，`ι` | U+1F21，U+03B9 |
| [U+1F92](https://codepoints.net/U+1F92?lang=en) | `ᾒ` |带有 PSILI 和 VARIA 和 YPOGEGRAMMENI 的希腊小写字母 ETA | `ἢ`，`ι` | U+1F22，U+03B9 |
| [U+1F93](https://codepoints.net/U+1F93?lang=en) | `ᾓ` |带有 DASIA 和 VARIA 和 YPOGRAMMENI 的希腊小写字母 ETA | `ἣ`，`ι` | U+1F23，U+03B9 |
| [U+1F94](https://codepoints.net/U+1F94?lang=en) | `ᾔ` |带有 PSILI 和 OXIA 以及 YPOGRAMMENI 的希腊小写字母 ETA | `ἤ`，`ι` | U+1F24，U+03B9 |
| [U+1F95](https://codepoints.net/U+1F95?lang=en) | `ᾕ` |带有 DASIA 和 OXIA 以及 YPOGRAMMENI 的希腊小写字母 ETA | `ἥ`，`ι` | U+1F25，U+03B9 |
| [U+1F96](https://codepoints.net/U+1F96?lang=en) | `ᾖ` |带有 PSILI 和 PERISPOMENI 和 YPOGEGRAMMENI 的希腊小写字母 ETA | `ἦ`, `ι` | U+1F26、U+03B9 |
| [U+1F97](https://codepoints.net/U+1F97?lang=en) | `ᾗ` |带有 DASIA 和 PERISPOMENI 和 YPOGEGRAMMENI 的希腊小写字母 ETA | `ἧ`，`ι` | U+1F27、U+03B9 |
| [U+1F98](https://codepoints.net/U+1F98?lang=en) | `ᾘ` |带有 PSILI 和 PROSGEGRAMMENI 的希腊大写字母 ETA | `ἠ`, `ι` | U+1F20，U+03B9 |
| [U+1F99](https://codepoints.net/U+1F99?lang=en) | `ᾙ` |带有 DASIA 和 PROSGEGRAMMENI 的希腊大写字母 ETA | `ἡ`，`ι` | U+1F21，U+03B9 |
| [U+1F9A](https://codepoints.net/U+1F9A?lang=en) | `ᾚ` |带有 PSILI 和 VARIA 以及 PROSGEGRAMMENI 的希腊大写字母 ETA | `ἢ`，`ι` | U+1F22，U+03B9 |
| [U+1F9B](https://codepoints.net/U+1F9B?lang=en) | `ᾛ` |带有 DASIA 和 VARIA 以及 PROSGEGRAMMENI 的希腊大写字母 ETA | `ἣ`，`ι` | U+1F23，U+03B9 |
| [U+1F9C](https://codepoints.net/U+1F9C?lang=en) | `ᾜ` |带有 PSILI 和 OXIA 以及 PROSGEGRAMMENI 的希腊大写字母 ETA | `ἤ`，`ι` | U+1F24，U+03B9 |
| [U+1F9D](https://codepoints.net/U+1F9D?lang=en) | `ᾝ` |带有 DASIA 和 OXIA 以及 PROSGEGRAMMENI 的希腊大写字母 ETA | `ἥ`，`ι` | U+1F25，U+03B9 |
| [U+1F9E](https://codepoints.net/U+1F9E?lang=en) | `ᾞ` |带有 PSILI 和 PERISPOMENI 和 PROSGEGRAMMENI 的希腊大写字母 ETA | `ἦ`, `ι` | U+1F26、U+03B9 |
| [U+1F9F](https://codepoints.net/U+1F9F?lang=en) | `ᾟ` |带有 DASIA 和 PERISPOMENI 和 PROSGEGRAMMENI 的希腊大写字母 ETA | `ἧ`，`ι` | U+1F27、U+03B9 |
| [U+1FA0](https://codepoints.net/U+1FA0?lang=en) | `ᾠ` |带有 PSILI 和 YPOGRAMMENI 的希腊小写字母 OMEGA | `ὠ`、`ι` | U+1F60、U+03B9 |
| [U+1FA1](https://codepoints.net/U+1FA1?lang=en) | `ᾡ` |带有 DASIA 和 YPOGRAMMENI 的希腊小写字母 OMEGA | `ὡ`、`ι` | U+1F61、U+03B9 |
| [U+1FA2](https://codepoints.net/U+1FA2?lang=en) | `ᾢ` |带有 PSILI 和 VARIA 以及 YPOGRAMMENI 的希腊小写字母 OMEGA | `ὢ`、`ι` | U+1F62、U+03B9 |
| [U+1FA3](https://codepoints.net/U+1FA3?lang=en) | `ᾣ` |带有 DASIA 和 VARIA 以及 YPOGRAMMENI 的希腊小写字母 OMEGA | `ὣ`、`ι` | U+1F63、U+03B9 |
| [U+1FA4](https://codepoints.net/U+1FA4?lang=en) | `ᾤ` |带有 PSILI 和 OXIA 以及 YPOGRAMMENI 的希腊小写字母 OMEGA | `ὤ`、`ι` | U+1F64、U+03B9 |
| [U+1FA5](https://codepoints.net/U+1FA5?lang=en) | `ᾥ` |带有 DASIA 和 OXIA 以及 YPOGRAMMENI 的希腊小写字母 OMEGA | `ὥ`、`ι` | U+1F65、U+03B9 |
| [U+1FA6](https://codepoints.net/U+1FA6?lang=en) | `ᾦ` |带有 PSILI 和 PERISPOMENI 和 YPOGRAMMENI 的希腊小写字母 OMEGA | `ὦ`, `ι` | U+1F66、U+03B9 |
| [U+1FA7](https://codepoints.net/U+1FA7?lang=en) | `ᾧ` |带有 DASIA 和 PERISPOMENI 和 YPOGRAMMENI 的希腊小写字母 OMEGA | `ὧ`、`ι` | U+1F67、U+03B9 |
| [U+1FA8](https://codepoints.net/U+1FA8?lang=en) | `ᾨ` |带有 PSILI 和 PROSGEGRAMMENI 的希腊大写字母 OMEGA | `ὠ`、`ι` | U+1F60、U+03B9 |
| [U+1FA9](https://codepoints.net/U+1FA9?lang=en) | `ᾩ` |带有 DASIA 和 PROSGEGRAMMENI 的希腊大写字母 OMEGA | `ὡ`、`ι` | U+1F61、U+03B9 |
| [U+1FAA](https://codepoints.net/U+1FAA?lang=en) | `ᾪ` |带有 PSILI 和 VARIA 以及 PROSGEGRAMMENI 的希腊大写字母 OMEGA | `ὢ`、`ι` | U+1F62、U+03B9 |
| [U+1FAB](https://codepoints.net/U+1FAB?lang=en) | `ᾫ` |希腊大写字母 OMEGA 与 DASIA 和 VARIA 以及 PROSGEGRAMMENI | `ὣ`、`ι` | U+1F63、U+03B9 |
| [U+1FAC](https://codepoints.net/U+1FAC?lang=en) | `ᾬ` |带有 PSILI 和 OXIA 以及 PROSGEGRAMMENI 的希腊大写字母 OMEGA | `ὤ`、`ι` | U+1F64、U+03B9 |
| [U+1FAD](https://codepoints.net/U+1FAD?lang=en) | `ᾭ` |带有 DASIA 和 OXIA 以及 PROSGEGRAMMENI 的希腊大写字母 OMEGA | `ὥ`、`ι` | U+1F65、U+03B9 |
| [U+1FAE](https://codepoints.net/U+1FAE?lang=en) | `ᾮ` |带有 PSILI 和 PERISPOMENI 和 PROSGEGRAMMENI 的希腊大写字母 OMEGA | `ὦ`, `ι` | U+1F66、U+03B9 |
| [U+1FAF](https://codepoints.net/U+1FAF?lang=en) | `ᾯ` |希腊大写字母 OMEGA 与 DASIA、PERISPOMENI 和 PROSGEGRAMMENI | `ὧ`、`ι` | U+1F67、U+03B9 |
| [U+1FB2](https://codepoints.net/U+1FB2?lang=en) | `ᾲ` |带有 VARIA 和 YPOGEGRAMMENI 的希腊小写字母 ALPHA | `ὰ`、`ι` | U+1F70、U+03B9 |
| [U+1FB3](https://codepoints.net/U+1FB3?lang=en) | `ᾳ` |带有 YPOGRAMMENI 的希腊小写字母 ALPHA | `α`, `ι` | U+03B1、U+03B9 |
| [U+1FB4](https://codepoints.net/U+1FB4?lang=en) | `ᾴ` |带有 OXIA 和 YPOGEGRAMMENI 的希腊小写字母 ALPHA | 'ά', 'ι' | U+03AC，U+03B9 |
| [U+1FB6](https://codepoints.net/U+1FB6?lang=en) | `ᾶ` |带有 PERISPOMENI 的希腊小写字母 ALPHA | `α`, `͂` | U+03B1，U+0342 |
| [U+1FB7](https://codepoints.net/U+1FB7?lang=en) | `ᾷ` |带有 PERISPOMENI 和 YPOGEGRAMMENI 的希腊小写字母 ALPHA | `α`、`͂`、`ι` | U+03B1、U+0342、U+03B9 |
| [U+1FBC](https://codepoints.net/U+1FBC?lang=en) | `ᾼ` |带有 PROSGEGRAMMENI 的希腊大写字母 ALPHA | `α`, `ι` | U+03B1、U+03B9 |
| [U+1FC2](https://codepoints.net/U+1FC2?lang=en) | `ῂ` |带有 VARIA 和 YPOGEGRAMMENI 的希腊小写字母 ETA | `ὴ`，`ι` | U+1F74、U+03B9 |
| [U+1FC3](https://codepoints.net/U+1FC3?lang=en) | `ῃ` |希腊小写字母 ETA 与 YPOGEGRAMMENI | `η`, `ι` | U+03B7，U+03B9 |
| [U+1FC4](https://codepoints.net/U+1FC4?lang=en) | `ῄ` |带有 OXIA 和 YPOGEGRAMMENI 的希腊小写字母 ETA | `ή`, `ι` | U+03AE，U+03B9 |
| [U+1FC6](https://codepoints.net/U+1FC6?lang=en) | `ῆ` |带有 PERISPOMENI 的希腊小写字母 ETA | `η`, `͂` | U+03B7，U+0342 |
| [U+1FC7](https://codepoints.net/U+1FC7?la​​ng=en) | `ῇ` |带有 PERISPOMENI 和 YPOGRAMMENI 的希腊小写字母 ETA | `η`、`͂`、`ι` | U+03B7、U+0342、U+03B9 |
| [U+1FCC](https://codepoints.net/U+1FCC?lang=en) | `ῌ` |带有 PROSGEGRAMMENI 的希腊大写字母 ETA | `η`, `ι` | U+03B7，U+03B9 |
| [U+1FD2](https://codepoints.net/U+1FD2?lang=en) | `ῒ` |带有 DIALYTIKA 和 VARIA 的希腊小写字母 IOTA | `ι`、`̈`、`̀` | U+03B9、U+0308、U+0300 |
| [U+1FD3](https://codepoints.net/U+1FD3?lang=en) | 'ΐ' |带有 DIALYTIKA 和 OXIA 的希腊小写字母 IOTA | `ι`、`̈`、`́` | U+03B9、U+0308、U+0301 |
| [U+1FD6](https://codepoints.net/U+1FD6?lang=en) | `ῖ` |带有 PERISPOMENI 的希腊小写字母 IOTA | `ι`, `͂` | U+03B9，U+0342 |
| [U+1FD7](https://codepoints.net/U+1FD7?lang=en) | `ῗ` |带有 DIALYTIKA 和 PERISPOMENI 的希腊小写字母 IOTA | `ι`、`̈`、`͂` | U+03B9、U+0308、U+0342 |
| [U+1FE2](https://codepoints.net/U+1FE2?lang=en) | `ῢ` |带有 DIALYTIKA 和 VARIA 的希腊小写字母 UPSILON | `υ`、`̈`、`̀` | U+03C5、U+0308、U+0300 |
| [U+1FE3](https://codepoints.net/U+1FE3?lang=en) | ``ΰ` |带有 DIALYTIKA 和 OXIA 的希腊小写字母 UPSILON | `υ`、`̈`、`́` | U+03C5、U+0308、U+0301 |
| [U+1FE4](https://codepoints.net/U+1FE4?lang=en) | `ῤ` |带有 PSILI 的希腊小写字母 RHO | `ρ`、`̓` | U+03C1，U+0313 |
| [U+1FE6](https://codepoints.net/U+1FE6?lang=en) | `ῦ` |带有 PERISPOMENI 的希腊小写字母 UPSILON | `υ`、`͂` | U+03C5，U+0342 |
| [U+1FE7](https://codepoints.net/U+1FE7?lang=en) | `ῧ` |带有 DIALYTIKA 和 PERISPOMENI 的希腊小写字母 UPSILON | `υ`、`̈`、`͂` | U+03C5、U+0308、U+0342 |
| [U+1FF2](https://codepoints.net/U+1FF2?lang=en) | `ῲ` |带有 VARIA 和 YPOGEGRAMMENI 的希腊小写字母 OMEGA | `ὼ`、`ι` | U+1F7C、U+03B9 |
| [U+1FF3](https://codepoints.net/U+1FF3?lang=en) | `ῳ` |带有 YPOGRAMMENI 的希腊小写字母 OMEGA | `ω`，`ι` | U+03C9、U+03B9 |
| [U+1FF4](https://codepoints.net/U+1FF4?lang=en) | `ῴ` |带有 OXIA 和 YPOGRAMMENI 的希腊小写字母 OMEGA | `ώ`, `ι` | U+03CE、U+03B9 |
| [U+1FF6](https://codepoints.net/U+1FF6?lang=en) | `ῶ` |带有 PERISPOMENI 的希腊小写字母 OMEGA | `ω`, `͂` | U+03C9，U+0342 |
| [U+1FF7](https://codepoints.net/U+1FF7?lang=en) | `ῷ` |带有 PERISPOMENI 和 YPOGRAMMENI 的希腊小写字母 OMEGA | `ω`、`͂`、`ι` | U+03C9、U+0342、U+03B9 |
| [U+1FFC](https://codepoints.net/U+1FFC?lang=en) | `ῼ` |带有 PROSGEGRAMMENI 的希腊大写字母 OMEGA | `ω`，`ι` | U+03C9、U+03B9 |
| [U+FB00](https://codepoints.net/U+FB00?lang=en) | 'ff' |拉丁文小连字 FF | `f`，`f` | U+0066，U+0066 |
| [U+FB01](https://codepoints.net/U+FB01?lang=en) | `fi` |拉丁文小连字 FI | `f`、`i` | U+0066、U+0069 |
| [U+FB02](https://codepoints.net/U+FB02?lang=en) | `fl` |拉丁文小连字 FL | `f`、`l` | U+0066、U+006C |
| [U+FB03](https://codepoints.net/U+FB03?lang=en) | `ﬃ` |拉丁文小连字 FFI | `f`、`f`、`i` | U+0066、U+0066、U+0069 |
| [U+FB04](https://codepoints.net/U+FB04?lang=en) | `ﬄ` |拉丁文小连字 FFL | `f`、`f`、`l` | U+0066、U+0066、U+006C |
| [U+FB05](https://codepoints.net/U+FB05?lang=en) | `ﬅ` |拉丁文小连字 LONG ST | `s`、`t` | U+0073、U+0074 |
| [U+FB06](https://codepoints.net/U+FB06?lang=en) | `ﬆ` |拉丁文小连字 ST | `s`、`t` | U+0073、U+0074 |
| [U+FB13](https://codepoints.net/U+FB13?lang=en) | `ﬓ` |亚美尼亚小结扎男士现在 | `` ``, `` `` | U+0574、U+0576 |
| [U+FB14](https://codepoints.net/U+FB14?lang=en) | `ﬔ` |亚美尼亚小结扎男子 ECH | `` ``, `` `` | U+0574、U+0565 |
| [U+FB15](https://codepoints.net/U+FB15?lang=en) | `ﬕ` |亚美尼亚小连衣男士 INI | `` ``, `` `` | U+0574、U+056B |
| [U+FB16](https://codepoints.net/U+FB16?lang=en) | `ﬖ` |亚美尼亚小结扎现在查看 | `` ``, `` `` | U+057E、U+0576 |
| [U+FB17](https://codepoints.net/U+FB17?lang=en) | `ﬗ` |亚美尼亚小连字男式 XEH | `` ``, `` `` | U+0574、U+056D |





# 很棒的包和库
- [PhantomScript](https://github.com/jagracey/PhantomScript) - :ghost: :flashlight：隐形 JavaScript 代码执行和社会工程
- [ESReverser](https://github.com/mathiasbynens/esrever) - 用 JavaScript 编写的 Unicode 感知字符串反转器。
- [mimic](https://github.com/reinderien/mimic) - [ab]利用Unicode制造悲剧
- [python-ftfy](https://github.com/LuminosoInsight/python-ftfy) - 给定 Unicode 文本，使其表示一致并且尽可能减少损坏。
- [vim-troll-stopper](https://github.com/vim-utils/vim-troll-stopper) - 阻止 Unicode 巨魔搞乱您的代码。


# 表情符号
* [Unicode 联盟的表情符号图表](http://www.unicode.org/emoji/charts/full-emoji-list.html)
* [Emojipedia](http://emojipedia.org/) - 有关特定表情符号、新闻博客的信息。
* [emojitracker](http://emojitracker.com/) - Twitter 上的实时表情符号使用。
* [World Translation Foundation](http://www.emojifoundation.com/) - 一种推广、探索并将书面文字转化为表情符号图画字母的方法。
* [Can I Emoji?](http://caniemoji.com/android-2/) - 显示 iOS、Android 和 Windows 原生表情符号支持的当前状态。
* [如何注册表情符号 URL](http://www.name.com/blog/how-tos/2015/12/want-an-emoji-url-this-is-how-you-register-one/)


## 多样性

Unicode 联盟做出了巨大的努力，更好地反映和融合人类多样性，包括文化习俗。这是联盟的[多样性报告](http://unicode.org/reports/tr51/#Diversity)。

现在可以使用混合性别情况的表情符号，例如同性家庭、牵手和接吻。真正的亮点是[表情符号组合序列](http://www.unicode.org/emoji/charts/emoji-zwj-sequences.html)。基本上：


|代码点 |食谱|合并 |
|-------------|----------|----------|
| U+1F469 U+200D U+2764 U+FE0F U+200D U+1F469 | <img height="36" width="auto" alt="👩" src="http://unicode.org/reports/tr51/images/apple/apple_1f469.png"> <img height="36" width="auto" alt="❤️‍" src="http://unicode.org/reports/tr51/images/other/zwj.png"> <img height="36" width="auto" alt="❤️‍" src="http://unicode.org/reports/tr51/images/apple/apple_2764.png"> <img height="36" width="auto" alt="❤️‍" src="http://unicode.org/reports/tr51/images/other/zwj.png"> <img height="36" width="auto" alt="👩" src="http://unicode.org/reports/tr51/images/apple/apple_1f469.png"> | <img height="36" width="auto" alt="情侣与心：女人，女人" src="http://unicode.org/reports/tr51/images/apple/apple_1f469_200d_2764_fe0f_200d_1f469.png"> |
|U+1F468 U+200D U+1F468 U+200D U+1F467 U+200D U+1F466|<img height="36" width="auto" src =“https://raw.githubusercontent.com/jagracey/Awesome-Unicode/c575db618a89c88624a8c3bdfe57eada0 64cbf14/资源/family%3B%20man%2C%20man%2C%20girl%2C%20boy%20-%20fallback%20-%20ZWJ.jpg">|<img高度=“36”宽度=“自动”src=“https://raw.githubusercontent.com/jagracey/Awesome-Unicode/58f28d08aef7f36eb6cdca22d25e7654cd8de5ae/resources/family%3B%20man%2C%20man%2C%20girl%2C%20boy.png”>|

此外，表情符号现在支持肤色修饰符。

> Unicode 版本 8.0（2015 年中）中发布了五个符号修饰符，为人类表情符号提供了一系列肤色。这些字符基于菲茨帕特里克等级的六个音调，菲茨帕特里克等级是皮肤病学公认的标准（网上有很多该等级的示例，例如 FitzpatrickSkinType.pdf）。确切的色调可能因实施方式而异。 -- [Unicode 联盟的多样性报告](http://unicode.org/reports/tr51/#Diversity)




|代码|名称 |样品|
|---------|-------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| U+1F3FB |表情符号修改器 FITZPATRICK TYPE-1-2 | <img src="http://www.unicode.org/reports/tr51/images/other/swatch-type-1-2.png" height="20" width="20"> <img src="http://www.unicode.org/reports/tr51/images/other/swatch-type-1-2-bw.png" height="20" width="20"> |
| U+1F3FC |表情符号修改器 FITZPATRICK TYPE-3 | <img src="http://www.unicode.org/reports/tr51/images/other/swatch-type-3.png" height="20" width="20"> <img src="http://www.unicode.org/reports/tr51/images/other/swatch-type-3-bw.png" height="20" width="20"> |
| U+1F3FD|表情符号修改器 FITZPATRICK TYPE-4 | <img src="http://www.unicode.org/reports/tr51/images/other/swatch-type-4.png" height="20" width="20"> <img src="http://www.unicode.org/reports/tr51/images/other/swatch-type-4-bw.png" height="20" width="20"> |
| U+1F3FE|表情符号修改器 FITZPATRICK TYPE-5 | <img src="http://www.unicode.org/reports/tr51/images/other/swatch-type-5.png" height="20" width="20"> <img src="http://www.unicode.org/reports/tr51/images/other/swatch-type-5-bw.png" height="20" width="20"> |
| U+1F3FF |表情符号修改器 FITZPATRICK TYPE-6 | <img src="http://www.unicode.org/reports/tr51/images/other/swatch-type-6.png" height="20" width="20"> <img src="http://www.unicode.org/reports/tr51/images/other/swatch-type-6-bw.png" height="20" width="20"> |



只需在所需的表情符号后面加上肤色修饰符之一“\u{1F466}\u{1F3FE}”即可。

<p对齐=“中心”>
	<img src="http://unicode.org/reports/tr51/images/other/person.png" height="36" width="auto" alt="">
<font size="36"> + </font>
	<img src="http://unicode.org/reports/tr51/images/other/swatch-type-5.png" height="36" width="auto" alt="">
<font size="36">&nbsp;→&nbsp;</font>
	<img src="http://unicode.org/reports/tr51/images/other/person-5.png" height="36" width="auto" alt="">
</p>



<p对齐=“中心”>
	<img src="http://unicode.org/reports/tr51/images/other/palette-with-gray.png" alt="" height="48" width="auto">
</p>




# 创造性地命名变量和方法
*示例是用 JavaScript (ES6) 编写的*

一般来说，指定 [ID_START](https://codepoints.net/search?IDS=1) 属性的字符可以用在变量名称的开头。使用 [ID_CONTINUE](https://codepoints.net/search?IDC=1) 属性指定的字符可以在变量的第一个字符之后使用。


```javascript

function rand(μ,σ){ ... };

String.prototype.reverseⵑ = function(){..};

Number.prototype.isTrueɁ = function(){..};

var WhatDoesThisDoɁɁɁɁ = 42
```



以下是来自 [Mathias Bynes] 的一些非常有创意的变量名称(https://mathiasbynens.be/notes/javascript-identifiers#examples)

```javascript
// How convenient!
var π = Math.PI;

// Sometimes, you just have to use the Bad Parts of JavaScript:
var ಠ_ಠ = eval;

// Code, Y U NO WORK?!
var ლ_ಠ益ಠ_ლ = 42;

// How about a JavaScript library for functional programming?
var λ = function() {};

// Obfuscate boring variable names for great justice
var \u006C\u006F\u006C\u0077\u0061\u0074 = 'heh';

// …or just make up random ones
var Ꙭൽↈⴱ = 'huh';

// While perfectly valid, this doesn’t work in most browsers:
var foo\u200Cbar = 42;

// This is *not* a bitwise left shift (`<<`):
var 〱〱 = 2;
// This is, though:
〱〱 << 〱〱; // 8

// Give yourself a discount:
var price_9̶9̶_89 = 'cheap';

// Fun with Roman numerals
var Ⅳ = 4;
var Ⅴ = 5;
Ⅳ + Ⅴ; // 9

// Cthulhu was here
var Hͫ̆̒̐ͣ̊̄ͯ͗͏̵̗̻̰̠̬͝ͅE̴̷̬͎̱̘͇͍̾ͦ͊͒͊̓̓̐_̫̠̱̩̭̤͈̑̎̋ͮͩ̒͑̾͋͘Ç̳͕̯̭̱̲̣̠̜͋̍O̴̦̗̯̹̼ͭ̐ͨ̊̈͘͠M̶̝̠̭̭̤̻͓͑̓̊ͣͤ̎͟͠E̢̞̮̹͍̞̳̣ͣͪ͐̈T̡̯̳̭̜̠͕͌̈́̽̿ͤ̿̅̑Ḧ̱̱̺̰̳̹̘̰́̏ͪ̂̽͂̀͠ = 'Zalgo';
```


这里有一些来自 David Walsh 的 [Unicode CSS 类](https://davidwalsh.name/unicode-css-classes)
```html
<!-- place this within the document head -->
<meta charset="UTF-8" />

<!-- error message -->
<div class="ಠ_ಠ">You do not have access to this page.</div>

<!-- success message -->
<div class="❤">Your changes have been saved successfully!</div>
```

```css
.ಠ_ಠ {
	border: 1px solid #f00;
}

.❤ {
	background: lightgreen;
}
```

## 递归 HTML 标签重命名脚本
如果您想将所有 HTML 标签重命名为看似空无一物的名称，那么以下脚本正是您所需要的。

*但请注意，HTML 不支持所有 unicode 字符。*
```javascript
// U+1160 HANGUL JUNGSEONG FILLER
transformAllTags('ᅠ');

// An actual HTML element node designed to look like a comment node, using the U+01C3 LATIN LETTER RETROFLEX CLICK 
//	<ǃ-- name="viewport" content="width=device-width"></ǃ-->
transformAllTags('ǃ--');

// or even <ᅠ⃝
transformAllTags('\u{1160}\u{20dd}');

// and for a bonus, all existing tag names will have each character ensquared. h⃞t⃞m⃞l⃞
transformAllTags();


function transformAllTags (newName){
   // querySelectorAll doesn't actually return an array.
   Array.from(document.querySelectorAll('*'))
     .forEach(function(x){
         transformTag(x, newName);
   });
}

function wonky(str){
  return str.split('').join('\u{20de}') + '\u{20de}';
}

function transformTag(tagIdOrElem, tagType){
    var elem = (tagIdOrElem instanceof HTMLElement) ? tagIdOrElem : document.getElementById(tagIdOrElem);
    if(!elem || !(elem instanceof HTMLElement))return;
    var children = elem.childNodes;
    var parent = elem.parentNode;
    var newNode = document.createElement(tagType||wonky(elem.tagName));
    for(var a=0;a<elem.attributes.length;a++){
        newNode.setAttribute(elem.attributes[a].nodeName, elem.attributes[a].value);
    }
    for(var i= 0,clen=children.length;i<clen;i++){
        newNode.appendChild(children[0]); //0...always point to the first non-moved element
    }
    newNode.style.cssText = elem.style.cssText;
    parent.replaceChild(newNode,elem);
}
```
这是它支持的内容：

```javascript
function testBegin(str){
 try{
    eval(`document.createElement( '${str}' );`)
    return true;
 }
 catch(e){ return false; }
}

function testContinue(str){
 try{
    eval(`document.createElement( 'a${str}' );`)
    return true;
 }
 catch(e){ return false; }
}
```

这是一些基本结果
```javascript
// Test if dashes can start an HTML Tag
> testBegin('-')
< false

> testContinue('-')
< true

> testBegin('ᅠ-')	// Prepend dash with U+1160 HANGUL JUNGSEONG FILLER
< true
```


# Unicode 字体
*单一 TrueType / OpenType 字体格式无法涵盖所有 UTF-8 字符，因为字体中存在 65535 个字形的硬性限制。由于有超过 110 万个 UTF-8 glphy，您将需要使用字体系列来涵盖所有它们。*
- https://en.wikipedia.org/wiki/Unicode_font#List_of_Unicode_fonts
- http://www.unifont.org/fontguide/


# 更多阅读
* [The Absolute Minimum Every Software Developer Absolutely, Positively Must Know About Unicode and Character Sets](http://www.joelonsoftware.com/articles/Unicode.html) - 作者：乔尔·斯波尔斯基
* [每个程序员绝对需要了解的关于处理文本的编码和字符集的知识](http://kunststube.net/encoding/)
* [Unicode 联盟的推荐阅读列表](http://www.unicode.org/resources/readinglist.html)
* [Space Yourself](https://www.smashingmagazine.com/2015/10/space-yourself/) - Smashing Magazine 的间距指南
* [JavaScript 有一个 Unicode 问题](https://mathiasbynens.be/notes/javascript-unicode)
* [创意用户名和 Spotify 帐户劫持](https://labs.spotify.com/2013/06/18/creative-usernames/)


# 深入探索 Unicode
- [Shapecatcher](http://shapecatcher.com/) - 画出您要寻找的角色。
- [容易混淆的 Unicode 字符](http://unicode.org/cldr/utility/confusables.jsp?r=None)
- [Unicode 字符数据库](http://www.unicode.org/ucd/)
- [Codepoints.net 的数据库转储](https://dumps.codepoints.net/)
- [Unicode 块列表](http://www.unicode.org/Public/UCD/latest/ucd/Blocks.txt)
- [Unicode 字符代码表](http://www.unicode.org/charts/index.html)
- [Unicode 案例图表](http://www.unicode.org/charts/case/)
- [Unicode 标准化表](http://www.unicode.org/charts/normalization/)
- [统一码常见问题解答](http://www.unicode.org/faq/)




# 概览图
## 基本多语言平面地图
**每个编号框代表 256 个代码点。**
<p对齐=“中心”>
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Roadmap_to_Unicode_BMP.svg/750px-Roadmap_to_Unicode_BMP.svg.png" alt="A map of the Basic Multilingual Plane. Each numbered box represents 256 code points."/>
</p>

*中文、日文和韩文 (CJK) 文字具有共同的背景，统称为 CJK 字符。在汉族统一的过程中，共同（共享）字符被识别并命名为“中日韩统一表意文字”。*


## Unicode 块
*Unicode 标准将字符组排列在块中。这是所有 17 个平面上的块的完整列表。*

|名称 |来自|至 | \# 代码点 |
|------------------------------------------------------------------------------------------------------------------------------|----------|----------|---------------|
| [基础拉丁语](https://wikipedia.org/wiki/Basic_Latin) | U+0000 | U+007F | (128) |
| [Latin-1 补充](https://wikipedia.org/wiki/Latin-1_Supplement) | U+0080 | U+00FF | (128) |
| [拉丁语扩展-A](https://wikipedia.org/wiki/Latin_Extended-A) | U+0100 | U+017F | (128) |
| [拉丁语扩展-B](https://wikipedia.org/wiki/Latin_Extended-B) | U+0180 | U+024F | (208)|
| [IPA 扩展](https://wikipedia.org/wiki/IPA_Extensions) | U+0250 | U+02AF | (96) |
| [间距修饰符字母](https://wikipedia.org/wiki/Spacing_Modifier_Letters) | U+02B0 | U+02FF | (80) |
| [组合变音标记](https://wikipedia.org/wiki/Combining_Diaritic_Marks) | U+0300 | U+036F | (112) |
| [希腊语和科普特语](https://wikipedia.org/wiki/Greek_and_Coptic) | U+0370 | U+03FF | (135) |
| [西里尔文](https://wikipedia.org/wiki/Cyrillic) | U+0400 | U+04FF | (256) |
| [西里尔字母补充](https://wikipedia.org/wiki/Cyrillic_Supplement) | U+0500 | U+052F | (48) |
| [亚美尼亚语](https://wikipedia.org/wiki/Armenian) | U+0530 | U+058F | (89) |
| [希伯来语](https://wikipedia.org/wiki/Hebrew) | U+0590 | U+05FF | (87) |
| [阿拉伯语](https://wikipedia.org/wiki/Arabic) | U+0600 | U+06FF | (255) |
| [叙利亚语](https://wikipedia.org/wiki/Syriac) | U+0700 | U+074F | (77) |
| [阿拉伯语补充](https://wikipedia.org/wiki/Arabic_Supplement) | U+0750 | U+077F | (48) |
| [塔纳](https://wikipedia.org/wiki/Thaana) | U+0780 | U+07BF | (50) |
| [NKo](https://wikipedia.org/wiki/NKo) | U+07C0 | U+07FF | (59) |
| [撒玛利亚人](https://wikipedia.org/wiki/Samaritan) | U+0800 | U+083F | (61) |
| [曼达克](https://wikipedia.org/wiki/Mandaic) | U+0840 | U+085F | (29) |
| [阿拉伯语扩展-A](https://wikipedia.org/wiki/Arabic_Extended-A) | U+08A0 | U+08FF | (50) |
| [天城文](https://wikipedia.org/wiki/Devanagari) | U+0900 | U+097F | (128) |
| [孟加拉语](https://wikipedia.org/wiki/Bengali) | U+0980 | U+09FF | (93) |
| [古尔穆基](https://wikipedia.org/wiki/Gurmukhi) | U+0A00 | U+0A7F | (79) |
| [古吉拉特语](https://wikipedia.org/wiki/Gujarati) | U+0A80 | U+0AFF | (85) |
| [奥里亚语](https://wikipedia.org/wiki/Oriya) | U+0B00 | U+0B7F | (90) |
| [泰米尔语](https://wikipedia.org/wiki/Tamil) | U+0B80 | U+0好朋友 | (72) |
| [泰卢固语](https://wikipedia.org/wiki/Telugu) | U+0C00 | U+0C7F | (96) |
| [卡纳达语](https://wikipedia.org/wiki/Kannada) | U+0C80 | U+0CFF | (87) |
| [马拉雅拉姆语](https://wikipedia.org/wiki/马拉雅拉姆语) | U+0D00 | U+0D7F | (100) |
| [僧伽罗语](https://wikipedia.org/wiki/Sinhala) | U+0D80 | U+0DFF | (90) |
| [泰语](https://wikipedia.org/wiki/Thai) | U+0E00 | U+0E7F | (87) |
| [老挝](https://wikipedia.org/wiki/Lao) | U+0E80 | U+0EFF | (67) | (67)
| [藏语](https://wikipedia.org/wiki/Tibetan) | U+0F00 | U+0FFF | (211) |
| [缅甸](https://wikipedia.org/wiki/Myanmar) | U+1000 | U+109F | (160) |
| [格鲁吉亚语](https://wikipedia.org/wiki/Georgian) | U+10A0 | U+10FF | (88) |
| [韩文 Jamo](https://wikipedia.org/wiki/Hangul_Jamo) | U+1100 | U+11FF | (256) |
| [埃塞俄比亚](https://wikipedia.org/wiki/Ethiopic) | U+1200 | U+137F | (358) |
| [埃塞俄比亚补充](https://wikipedia.org/wiki/Ethiopic_Supplement) | U+1380 | U+139F | (26) |
| [切诺基](https://wikipedia.org/wiki/Cherokee) | U+13A0 | U+13FF | (92) | (92)
| [统一加拿大原住民音节](https://wikipedia.org/wiki/Unified_Canadian_Aboriginal_Syllabics) | U+1400 | U+167F | (640) |
| [奥格姆](https://wikipedia.org/wiki/Ogham) | U+1680 | U+169F | (29) |
| [符文](https://wikipedia.org/wiki/Runic) | U+16A0 | U+16FF | (89) |
| [他加禄语](https://wikipedia.org/wiki/Tagalog) | U+1700 | U+171F | (20) |
| [哈努努](https://wikipedia.org/wiki/Hanunoo) | U+1720 | U+173F | (23) |
| [布希德](https://wikipedia.org/wiki/Buhid) | U+1740 | U+175F | (20) |
| [塔格班瓦](https://wikipedia.org/wiki/Tagbanwa) | U+1760 | U+177F | (18) |
| [高棉语](https://wikipedia.org/wiki/Khmer) | U+1780 | U+17FF | (114) |
| [蒙古语](https://wikipedia.org/wiki/Mongolian) | U+1800 | U+18AF | (156) |
| [统一加拿大原住民音节扩展](https://wikipedia.org/wiki/Unified_Canadian_Aboriginal_Syllabics_Extended)| U+18B0 | U+18FF | (70) |
| [林布](https://wikipedia.org/wiki/Limbu) | U+1900 | U+194F | (68) |
| [泰乐](https://wikipedia.org/wiki/Tai_Le) | U+1950 | U+197F | (35) |
| [新泰略](https://wikipedia.org/wiki/New_Tai_Lue) | U+1980 | U+19DF | (83) |
| [高棉符号](https://wikipedia.org/wiki/Khmer_Symbols) | U+19E0 | U+19FF | (32) |
| [Buginese](https://wikipedia.org/wiki/Buginese) | U+1A00 | U+1A1F | (30) |
| [Tai Tham](https://wikipedia.org/wiki/Tai_Tham) | U+1A20 | U+1AAF | (127) |
| [组合变音符扩展](https://wikipedia.org/wiki/Combining_Diaritic_Marks_Extended) | U+1AB0 | U+1AFF | (15) |
| [巴厘岛语](https://wikipedia.org/wiki/Balinese) | U+1B00 | U+1B7F | (121) |
| [巽他语](https://wikipedia.org/wiki/Sundanese) | U+1B80 | U+1BBF | (64) |
| [巴塔克](https://wikipedia.org/wiki/Batak) | U+1BC0 | U+1 最好的朋友 | (56) |
| [Lepcha](https://wikipedia.org/wiki/Lepcha) | U+1C00 | U+1C4F | (74) |
| [Ol Chiki](https://wikipedia.org/wiki/Ol_Chiki) | U+1C50 | U+1C7F | (48) |
| [巽他语补充](https://wikipedia.org/wiki/Sundanese_Supplement) | U+1CC0 | U+1CCF | (8) |
| [吠陀扩展](https://wikipedia.org/wiki/Vedic_Extensions) | U+1CD0 | U+1CFF | (41) |
| [拼音扩展](https://wikipedia.org/wiki/Phonetic_Extensions) | U+1D00 | U+1D7F | (128) |
| [拼音扩展补充](https://wikipedia.org/wiki/Phonetic_Extensions_Supplement) | U+1D80 | U+1DBF | (64) |
| [组合变音符补充](https://wikipedia.org/wiki/Combining_Diaritic_Marks_Supplement) | U+1DC0 | U+1DFF | (58) |
| [拉丁语扩展附加](https://wikipedia.org/wiki/Latin_Extended_Additional) | U+1E00 | U+1EFF | (256) |
| [希腊语扩展](https://wikipedia.org/wiki/Greek_Extended) | U+1F00 | U+1FFF | (233) |
| [一般标点符号](https://wikipedia.org/wiki/General_Punctuation) | U+2000 | U+206F | （111）|
| [上标和下标](https://wikipedia.org/wiki/Superscripts_and_Subscripts) | U+2070 | U+209F | (42) |
| [货币符号](https://wikipedia.org/wiki/Currency_Symbols) | U+20A0 | U+20CF| (31) |
| [组合符号的变音标记](https://wikipedia.org/wiki/Combining_Diaritic_Marks_for_Symbols) | U+20D0 | U+20FF | (33) |
| [类似字母的符号](https://wikipedia.org/wiki/Letterlike_Symbols) | U+2100 | U+214F | (80) |
| [数字形式](https://wikipedia.org/wiki/Number_Forms) | U+2150 | U+218F | (60) |
| [箭头](https://wikipedia.org/wiki/Arrows) | U+2190 | U+21FF | (112) |
| [数学运算符](https://wikipedia.org/wiki/Mathematical_Operators) | U+2200 | U+22FF | (256) |
| [杂项技术](https://wikipedia.org/wiki/Miscellaneous_Technical) | U+2300 | U+23FF | (251) |
| [控制图片](https://wikipedia.org/wiki/Control_Pictures) | U+2400 | U+243F | (39) |
| [光学字符识别](https://wikipedia.org/wiki/Optical_Character_Recognition) | U+2440 | U+245F | (11) |
| [附上字母数字](https://wikipedia.org/wiki/Enlined_Alphanumerics) | U+2460 | U+24FF | (160) |
| [方框图](https://wikipedia.org/wiki/Box_Drawing) | U+2500 | U+257F | (128) |
| [块元素](https://wikipedia.org/wiki/Block_Elements) | U+2580 | U+259F | (32) |
| [几何形状](https://wikipedia.org/wiki/Geometric_Shapes) | U+25A0 | U+25FF | (96) |
| [杂项符号](https://wikipedia.org/wiki/Miscellaneous_Symbols) | U+2600 | U+26FF | (256) |
| [Dingbats](https://wikipedia.org/wiki/Dingbats) | U+2700 | U+27BF | (192) |
| [杂项数学符号-A](https://wikipedia.org/wiki/Miscellaneous_Mathematical_Symbols-A) | U+27C0 | U+27EF | (48) |
| [补充箭头-A](https://wikipedia.org/wiki/Supplemental_Arrows-A) | U+27F0 | U+27FF | (16) |
| [盲文图案](https://wikipedia.org/wiki/Braille_Patterns) | U+2800 | U+28FF | (256) |
| [补充箭头-B](https://wikipedia.org/wiki/Supplemental_Arrows-B) | U+2900 | U+297F | (128) |
| [杂项数学符号-B](https://wikipedia.org/wiki/Miscellaneous_Mathematical_Symbols-B) | U+2980 | U+29FF | (128) |
| [补充数学运算符](https://wikipedia.org/wiki/Supplemental_Mathematical_Operators) | U+2A00 | U+2AFF | (256) |
| [杂项符号和箭头](https://wikipedia.org/wiki/Miscellaneous_Symbols_and_Arrows) | U+2B00 | U+2BFF| (206)|
| [格拉哥里](https://wikipedia.org/wiki/Glagolitic) | U+2C00 | U+2C5F | (94) |
| [拉丁语扩展-C](https://wikipedia.org/wiki/Latin_Extended-C) | U+2C60 | U+2C7F | (32) |
| [科普特](https://wikipedia.org/wiki/Coptic) | U+2C80 | U+2CFF | (123) |
| [格鲁吉亚补充](https://wikipedia.org/wiki/Georgian_Supplement) | U+2D00 | U+2D2F | (40) |
| [蒂菲纳](https://wikipedia.org/wiki/Tifinagh) | U+2D30 | U+2D7F | (59) |
| [埃塞俄比亚扩展](https://wikipedia.org/wiki/Ethiopic_Extended) | U+2D80 | U+2DDF | (79) |
| [西里尔文扩展-A](https://wikipedia.org/wiki/Cyrillic_Extended-A) | U+2DE0 | U+2DFF | (32) |
| [补充标点符号](https://wikipedia.org/wiki/Supplemental_Punctuation) | U+2E00 | U+2E7F | (67) | (67)
| [CJK 部首补充](https://wikipedia.org/wiki/CJK_Radicals_Supplement) | U+2E80 | U+2EFF | (115) |
| [康熙激进派](https://wikipedia.org/wiki/Kangxi_Radicals) | U+2F00 | U+2FDF | (214) |
| [表意描述字符](https://wikipedia.org/wiki/Idegraphic_Description_Characters) | U+2FF0 | U+2FFF | (12) |
| [CJK 符号和标点符号](https://wikipedia.org/wiki/CJK_Symbols_and_Punctuation) | U+3000 | U+303F | (64) |
| [平假名](https://wikipedia.org/wiki/Hiragana) | U+3040 | U+309F | (93) |
| [片假名](https://wikipedia.org/wiki/Katakana) | U+30A0 | U+30FF | (96) |
| [Bopomofo](https://wikipedia.org/wiki/Bopomofo) | U+3100 | U+312F | (41) |
| [韩文兼容性 Jamo](https://wikipedia.org/wiki/Hangul_Compatibility_Jamo) | U+3130 | U+318F | (94) |
| [Kanbun](https://wikipedia.org/wiki/Kanbun) | U+3190 | U+319F | (16) |
| [Bopomofo 扩展](https://wikipedia.org/wiki/Bopomofo_Extended) | U+31A0 | U+31BF | (27) |
| [中日韩笔画](https://wikipedia.org/wiki/CJK_Strokes) | U+31C0 | U+31EF | (36) |
| [片假名拼音扩展](https://wikipedia.org/wiki/Katakana_Phonetic_Extensions) | U+31F0 | U+31FF | (16) |
| [附上中日韩字母和月份](https://wikipedia.org/wiki/Enheld_CJK_Letters_and_Months) | U+3200 | U+32FF | (254) |
| [中日韩兼容性](https://wikipedia.org/wiki/CJK_Compatibility) | U+3300 | U+33FF | (256) |
| [中日韩统一表意文字扩展 A](https://wikipedia.org/wiki/CJK_Unified_Ideographs_Extension_A) | U+3400 | U+4DBF | (6191) |
| 【易经卦象】(https://wikipedia.org/wiki/Yijing_Hexagram_Symbols) | U+4DC0 | U+4DFF | (64) |
| [中日韩统一表意文字](https://wikipedia.org/wiki/CJK_Unified_Ideographs) | U+4E00 | U+9FFF | (20941) |
| [彝语音节](https://wikipedia.org/wiki/Yi_Syllables) | U+A000 | U+A48F | (1165) |
| [彝族激进派](https://wikipedia.org/wiki/Yi_Radicals) | U+A490 | U+A4CF | (55) |
| [傈僳族](https://wikipedia.org/wiki/Lisu) | U+A4D0 | U+A4FF | (48) |
| [Vai](https://wikipedia.org/wiki/Vai) | U+A500 | U+A63F | (300) |
| [西里尔文扩展-B](https://wikipedia.org/wiki/Cyrillic_Extended-B) | U+A640 | U+A69F | (96) |
| [Bamum](https://wikipedia.org/wiki/Bamum) | U+A6A0 | U+A6FF | (88) |
| [修饰语气字母](https://wikipedia.org/wiki/Modifier_Tone_Letters) | U+A700 | U+A71F | (32) |
| [拉丁语扩展-D](https://wikipedia.org/wiki/Latin_Extended-D) | U+A720 | U+A7FF | (159) | （159）
| [Syloti Nagri](https://wikipedia.org/wiki/Syloti_Nagri) | U+A800 | U+A82F | (44) |
| [常见印度数字形式](https://wikipedia.org/wiki/Common_Indic_Number_Forms) | U+A830 | U+A83F | (10) |
| [Phags-pa](https://wikipedia.org/wiki/Phags-pa) | U+A840 | U+A87F | (56) |
| [Saurashtra](https://wikipedia.org/wiki/Saurashtra) | U+A880 | U+A8DF | (81) |
| [天城文扩展](https://wikipedia.org/wiki/Devanagari_Extended) | U+A8E0 | U+A8FF | (30) |
| [Kayah Li](https://wikipedia.org/wiki/Kayah_Li) | U+A900 | U+A92F | (48) |
| [Rejang](https://wikipedia.org/wiki/Rejang) | U+A930 | U+A95F | (37) |
| [Hangul Jamo Extended-A](https://wikipedia.org/wiki/Hangul_Jamo_Extended-A) | U+A960 | U+A97F | (29) |
| [爪哇语](https://wikipedia.org/wiki/Javanese) | U+A980 | U+A9DF | (91) | (91)
| [缅甸扩展-B](https://wikipedia.org/wiki/Myanmar_Extended-B) | U+A9E0 | U+A9FF | (31) |
| [Cham](https://wikipedia.org/wiki/Cham) | U+AA00 | U+AA5F | (83) |
| [缅甸扩展-A](https://wikipedia.org/wiki/Myanmar_Extended-A) | U+AA60 | U+AA7F | (32) |
| [大越](https://wikipedia.org/wiki/Tai_Viet) | U+AA80 | U+AADF| (72) |
| [Meetei Mayek 扩展](https://wikipedia.org/wiki/Meetei_Mayek_Extensions) | U+AAE0 | U+AAFF | (23) |
| [埃塞俄比亚扩展-A](https://wikipedia.org/wiki/Ethiopic_Extended-A) | U+AB00 | U+AB2F | (32) |
| [拉丁语扩展-E](https://wikipedia.org/wiki/Latin_Extended-E) | U+AB30 | U+AB6F | (54) |
| [切诺基补充](https://wikipedia.org/wiki/Cherokee_Supplement) | U+AB70 | U+ABBF | (80) |
| [Meetei Mayek](https://wikipedia.org/wiki/Meetei_Mayek) | U+ABC0 | U+ABFF | (56) |
| [韩文音节](https://wikipedia.org/wiki/Hangul_Syllables) | U+AC00 | U+D7AF | (2) |
| [Hangul Jamo Extended-B](https://wikipedia.org/wiki/Hangul_Jamo_Extended-B) | U+D7B0 | U+D7FF | (72) |
| [高代理](https://wikipedia.org/wiki/High_Surrogates) | U+D800 | U+DB7F | (2) |
| [高私人使用代理](https://wikipedia.org/wiki/High_Private_Use_Surrogates) | U+DB80 | U+DBFF | (2) |
| [低代理](https://wikipedia.org/wiki/Low_Surrogates) | U+DC00 | U+DFFF | (2) |
| [私人使用区域](https://wikipedia.org/wiki/Private_Use_Area) | U+E000 | U+F8FF | (2) |
| [CJK 兼容性表意文字](https://wikipedia.org/wiki/CJK_Compatibility_Ideographs) | U+F900 | U+FAFF| (472) |
| [按字母顺序展示表格](https://wikipedia.org/wiki/Alphabetic_Presentation_Forms) | U+FB00 | U+FB4F | (58) |
| [阿拉伯语演示形式-A](https://wikipedia.org/wiki/Arabic_Presentation_Forms-A) | U+FB50 | U+FDFF | (643) |
| [变体选择器](https://wikipedia.org/wiki/Variation_Selectors) | U+FE00 | U+FE0F | (16) |
| [垂直表格](https://wikipedia.org/wiki/Vertical_Forms) | U+FE10 | U+FE1F | (10) |
| [组合半分](https://wikipedia.org/wiki/Combining_Half_Marks) | U+FE20 | U+FE2F | (16) |
| [CJK 兼容性表格](https://wikipedia.org/wiki/CJK_Compatibility_Forms) | U+FE30 | U+FE4F | (32) |
| [小形式变体](https://wikipedia.org/wiki/Small_Form_Variants) | U+FE50 | U+FE6F | (26) |
| [阿拉伯语演示形式-B](https://wikipedia.org/wiki/Arabic_Presentation_Forms-B) | U+FE70 | U+FEFF| (141) |
| [半角和全角表格](https://wikipedia.org/wiki/Halfwidth_and_Fullwidth_Forms) | U+FF00 | U+FFEF | (225) |
| [特价](https://wikipedia.org/wiki/Specials) | U+FFF0 | U+FFFF | (7) |
| [线性 B 音节表](https://wikipedia.org/wiki/Linear_B_Syllabary) | U+10000 | U+1007F | (88) |
| [线性 B 表意文字](https://wikipedia.org/wiki/Linear_B_Ideograms) | U+10080 | U+100FF | (123) |
| [爱琴海数字](https://wikipedia.org/wiki/Aegean_Numbers) | U+10100 | U+1013F | （57）|
| [古希腊数字](https://wikipedia.org/wiki/Ancient_Greek_Numbers) | U+10140 | U+1018F | (77) |
| [古代符号](https://wikipedia.org/wiki/Ancient_Symbols) | U+10190 | U+101CF| (13) |
| [斐斯托斯光盘](https://wikipedia.org/wiki/Phaistos_Disc) | U+101D0 | U+101FF | (46) |
| [利西亚](https://wikipedia.org/wiki/Lycian) | U+10280 | U+1029F | (29) |
| [卡里安](https://wikipedia.org/wiki/Carian) | U+102A0 | U+102DF | (49) |
| [科普特契约数字](https://wikipedia.org/wiki/Coptic_Epact_Numbers) | U+102E0 | U+102FF | (28) |
| [旧斜体](https://wikipedia.org/wiki/Old_Italic) | U+10300 | U+1032F | (36) |
| [哥特式](https://wikipedia.org/wiki/Gothic) | U+10330 | U+1034F | (27) |
| [旧彼尔米克](https://wikipedia.org/wiki/Old_Permic) | U+10350 | U+1037F | (43) |
| [乌加里特](https://wikipedia.org/wiki/Ugaritic) | U+10380 | U+1039F | (31) |
| [古波斯语](https://wikipedia.org/wiki/Old_Persian) | U+103A0 | U+103DF | (50) |
| [德塞雷特](https://wikipedia.org/wiki/Deseret) | U+10400 | U+1044F | (80) |
| [Shavian](https://wikipedia.org/wiki/Shavian) | U+10450 | U+1047F | (48) |
| [奥斯曼亚](https://wikipedia.org/wiki/Osmanya) | U+10480 | U+104AF | (40) |
| [爱尔巴桑](https://wikipedia.org/wiki/Elbasan) | U+10500 | U+1052F | (40) |
| [高加索阿尔巴尼亚语](https://wikipedia.org/wiki/Caucasian_Albanian) | U+10530 | U+1056F | (53) |
| [线性 A](https://wikipedia.org/wiki/Linear_A) | U+10600 | U+1077F | (341) |
| [塞浦路斯音节表](https://wikipedia.org/wiki/Cypriot_Syllabary) | U+10800 | U+1083F | (55) |
| [帝国阿拉姆语](https://wikipedia.org/wiki/Imperial_Aramaic) | U+10840 | U+1085F| (31) |
| [巴尔米林](https://wikipedia.org/wiki/Palmyrene) | U+10860 | U+1087F | (32) |
| [纳巴泰安](https://wikipedia.org/wiki/Nabataean) | U+10880 | U+108AF | (40) |
| [哈特兰](https://wikipedia.org/wiki/Hatran) | U+108E0 | U+108FF | (26) |
| [腓尼基](https://wikipedia.org/wiki/Phoenician) | U+10900 | U+1091F | (29) |
| [Lydian](https://wikipedia.org/wiki/Lydian) | U+10920 | U+1093F | (27) |
| [Meroitic 象形文字](https://wikipedia.org/wiki/Meroitic_Hieroglyphs) | U+10980 | U+1099F | (32) |
| [Meroitic 草书](https://wikipedia.org/wiki/Meroitic_Cursive) | U+109A0 | U+109FF | (90) |
| [Kharoshthi](https://wikipedia.org/wiki/Kharoshthi) | U+10A00 | U+10A5F | (65) |
| [古南阿拉伯语](https://wikipedia.org/wiki/Old_South_Arabian) | U+10A60 | U+10A7F | (32) |
| [古北阿拉伯语](https://wikipedia.org/wiki/Old_North_Arabian) | U+10A80 | U+10A9F | (32) |
| [摩尼教](https://wikipedia.org/wiki/Manichaean) | U+10AC0 | U+10AFF | (51) |
| [阿维斯坦](https://wikipedia.org/wiki/Avestan) | U+10B00 | U+10B3F | (61) |
| [铭文帕提亚](https://wikipedia.org/wiki/Inscriptional_Parthian) | U+10B40 | U+10B5F | (30) |
| [巴列维铭文](https://wikipedia.org/wiki/Inscriptional_Pahlavi) | U+10B60 | U+10B7F | (27) |
| [巴列维诗篇](https://wikipedia.org/wiki/Psalter_Pahlavi) | U+10B80 | U+10BAF| (29) |
| [古突厥语](https://wikipedia.org/wiki/Old_Turkic) | U+10C00 | U+10C4F | (73) |
| [古匈牙利语](https://wikipedia.org/wiki/Old_Hungarian) | U+10C80 | U+10CFF | (108)|
| [鲁米数字符号](https://wikipedia.org/wiki/Rumi_Numeral_Symbols) | U+10E60 | U+10E7F | (31) |
| [婆罗米](https://wikipedia.org/wiki/Brahmi) | U+11000 | U+1107F | (109) | （109）
| [凯蒂](https://wikipedia.org/wiki/Kaithi) | U+11080 | U+110CF| (66) |
| [Sora Sompeng](https://wikipedia.org/wiki/Sora_Sompeng) | U+110D0 | U+110FF | (35) |
| [查克马](https://wikipedia.org/wiki/Chakma) | U+11100 | U+1114F | (67) | (67)
| [马哈贾尼](https://wikipedia.org/wiki/Mahajani) | U+11150 | U+1117F | (39) |
| [沙拉达](https://wikipedia.org/wiki/Sharada) | U+11180 | U+111DF | (94) |
| [僧伽罗古数字](https://wikipedia.org/wiki/Sinhala_Archaic_Numbers) | U+111E0 | U+111FF | (20) |
| [Khojki](https://wikipedia.org/wiki/Khojki) | U+11200 | U+1124F | (61) |
| [穆尔塔尼](https://wikipedia.org/wiki/Multani) | U+11280 | U+112AF | (38) |
| [Khudawadi](https://wikipedia.org/wiki/Khudawadi) | U+112B0 | U+112FF | (69) |
| [Grantha](https://wikipedia.org/wiki/Grantha) | U+11300 | U+1137F | (85) |
| [蒂尔胡塔](https://wikipedia.org/wiki/Tirhuta) | U+11480 | U+114DF | (82) |
| [Siddham](https://wikipedia.org/wiki/Siddham) | U+11580 | U+115FF | (92) | (92)
| [莫迪](https://wikipedia.org/wiki/Modi) | U+11600 | U+1165F | (79) |
| [塔克里](https://wikipedia.org/wiki/Takri) | U+11680 | U+116CF| (66) |
| [阿霍姆](https://wikipedia.org/wiki/Ahom) | U+11700 | U+1173F | （57）|
| [Warang Citi](https://wikipedia.org/wiki/Warang_Citi) | U+118A0 | U+118FF | (84) |
| [包善后](https://wikipedia.org/wiki/Pau_Cin_Hau) | U+11AC0 | U+11AFF | （57）|
| [楔形文字](https://wikipedia.org/wiki/Cuneiform) | U+12000 | U+123FF | (922) |
| [楔形文字数字和标点符号](https://wikipedia.org/wiki/Cuneiform_Numbers_and_Punctuation) | U+12400 | U+1247F | （116）|
| [早期王朝楔形文字](https://wikipedia.org/wiki/Early_Dynastic_Cuneiform) | U+12480 | U+1254F | (196) |
| [埃及象形文字](https://wikipedia.org/wiki/Egyptian_Hieroglyphs) | U+13000 | U+1342F | (1071) |
| [安纳托利亚象形文字](https://wikipedia.org/wiki/Anatolian_Hieroglyphs) | U+14400 | U+1467F | (583) |
| [Bamum 补充](https://wikipedia.org/wiki/Bamum_Supplement) | U+16800 | U+16A3F | (569) |
| [Mro](https://wikipedia.org/wiki/Mro) | U+16A40 | U+16A6F | (43) |
| [巴萨瓦](https://wikipedia.org/wiki/Bassa_Vah) | U+16AD0 | U+16AFF | (36) |
| [Pahawh Hmong](https://wikipedia.org/wiki/Pahawh_Hmong) | U+16B00 | U+16B8F | (127) |
| [苗](https://wikipedia.org/wiki/Miao) | U+16F00 | U+16F9F | (133) |
| [假名补充](https://wikipedia.org/wiki/Kana_Supplement) | U+1B000 | U+1B0FF | (2) |
| [Duployan](https://wikipedia.org/wiki/Duployan) | U+1BC00 | U+1BC9F | (143) |
| [速记格式控件](https://wikipedia.org/wiki/Shorthand_Format_Controls) | U+1BCA0 | U+1BCAF | (4) |
| [拜占庭音乐符号](https://wikipedia.org/wiki/Byzantine_Musical_Symbols) | U+1D000 | U+1D0FF | (246) |
| [音乐符号](https://wikipedia.org/wiki/Musical_Symbols) | U+1D100 | U+1D1FF | (231) |
| [古希腊乐谱](https://wikipedia.org/wiki/Ancient_Greek_Musical_Notation) | U+1D200 | U+1D24F | (70) |
| [太玄经符号](https://wikipedia.org/wiki/Tai_Xuan_Jing_Symbols) | U+1D300 | U+1D35F | (87) |
| [计数棒数字](https://wikipedia.org/wiki/Counting_Rod_Numerals) | U+1D360 | U+1D37F | (18) |
| [数学字母数字符号](https://wikipedia.org/wiki/Mathematical_Alphanumeric_Symbols) | U+1D400 | U+1D7FF | (996) |
| [萨顿 SignWriting](https://wikipedia.org/wiki/Sutton_SignWriting) | U+1D800 | U+1DAAF | (672) |
| [Mende Kikakui](https://wikipedia.org/wiki/Mende_Kikakui) | U+1E800 | U+1E8DF | (213) |
| [阿拉伯数学字母符号](https://wikipedia.org/wiki/Arabic_Mathematical_Alphabetic_Symbols) | U+1EE00 | U+1EEFF | (143) |
| [麻将牌](https://wikipedia.org/wiki/Mahjong_Tiles) | U+1F000 | U+1F02F | (44) |
| [多米诺骨牌](https://wikipedia.org/wiki/Domino_Tiles) | U+1F030 | U+1F09F | (100) |
| [扑克牌](https://wikipedia.org/wiki/Playing_Cards) | U+1F0A0 | U+1F0FF | (82) |
| [附上字母数字补充](https://wikipedia.org/wiki/Enlined_Alphanumeric_Supplement) | U+1F100 | U+1F1FF | (173) |
| [附上表意文字补充](https://wikipedia.org/wiki/Enlined_Idegraphic_Supplement) | U+1F200 | U+1F2FF | （57）|
| [杂项符号和象形文字](https://wikipedia.org/wiki/Miscellaneous_Symbols_and_Pictographs) | U+1F300 | U+1F5FF | (766) |
| [表情符号](https://wikipedia.org/wiki/Emoticons) | U+1F600 | U+1F64F | (80) |
| [装饰装饰](https://wikipedia.org/wiki/Ornamental_Dingbats) | U+1F650 | U+1F67F | (48) |
| [交通和地图符号](https://wikipedia.org/wiki/Transport_and_Map_Symbols) | U+1F680 | U+1F6FF | (98) |
| [炼金术符号](https://wikipedia.org/wiki/Alchemical_Symbols) | U+1F700 | U+1F77F | （116）|
| [几何形状扩展](https://wikipedia.org/wiki/Geometric_Shapes_Extended) | U+1F780 | U+1F7FF | (85) |
| [补充箭头-C](https://wikipedia.org/wiki/Supplemental_Arrows-C) | U+1F800 | U+1F8FF | (148) |
| [补充符号和象形文字](https://wikipedia.org/wiki/Supplemental_Symbols_and_Pictographs) | U+1F900 | U+1F9FF | (15) |
| [中日韩统一表意文字扩展 B](https://wikipedia.org/wiki/CJK_Unified_Ideographs_Extension_B) | U+20000 | U+2A6DF | (42676) |
| [中日韩统一表意文字扩展 C](https://wikipedia.org/wiki/CJK_Unified_Ideographs_Extension_C) | U+2A700 | U+2B73F | (60) |
| [CJK 统一表意文字扩展 D](https://wikipedia.org/wiki/CJK_Unified_Ideographs_Extension_D) | U+2B740 | U+2B81F | (27) |
| [CJK 统一表意文字扩展 E](https://wikipedia.org/wiki/CJK_Unified_Ideographs_Extension_E) | U+2B820 | U+2CEAF | (2) |
| [CJK 兼容性表意文字补充](https://wikipedia.org/wiki/CJK_Compatibility_Ideographs_Supplement) | U+2F800 | U+2FA1F | (542) |
| [标签](https://wikipedia.org/wiki/Tags) | U+E0000 | U+E007F | (97) |
| [变体选择器补充](https://wikipedia.org/wiki/Variation_Selectors_Supplement) | U+E0100 | U+E01EF | (240) |
| [补充私人使用区域-A](https://wikipedia.org/wiki/Supplementary_Private_Use_Area-A) | U+F0000 | U+FFFFF| (4) |
| [补充私人使用区域-B](https://wikipedia.org/wiki/Supplementary_Private_Use_Area-B) | U+100000 | U+10FFFF | (4) |



# [Unicode标准的原理](http://www.unicode.org/standard/principles.html)


Unicode 标准规定了以下基本原则：

* **通用指令** - 曾经使用过的每一种书写系统都应受到尊重并在标准中得到体现
* **逻辑顺序** - 在双向文本中，字符按逻辑顺序存储，而不是以表示方式存储
* **效率** - 文档必须高效且完整。
* **统一** - 如果不同的文化或语言使用相同的字符，则仅应包含一次。这一点是
* **字符，而不是字形** - 仅对字符进行编码，而不是字形。简而言之，字形是实际的图形
* **动态组合** - 新字符可以由其他已经标准化的字符组成。例如，字符“Ä”可以由“A”和分音符号（“ ¡ ”）组成。
* **语义** - 包含的字符必须明确定义并与其他字符区分开来。
* **稳定性** - 一旦定义的字符将永远不会被删除或它们的代码点被重新分配。如果出现错误，则应弃用代码点。
* **纯文本** - 标准中的字符是文本，而不是标记或元字符。
* **可转换性** - 所有其他使用的编码都可以用 Unicode 编码表示。

注：原理描述来自[codepoints.net](https://codepoints.net/about#unicode)



# Unicode 版本

* [版本 9.0.0](http://www.unicode.org/versions/Unicode9.0.0/)（最新版本，2016 年 8 月 - 添加了 7,500 个字符）
* [版本8.0.0](http://www.unicode.org/versions/Unicode8.0.0/)
* [版本7.0.0](http://www.unicode.org/versions/Unicode7.0.0/)
* [版本6.3.0](http://www.unicode.org/versions/Unicode6.3.0/)
* [版本6.2.0](http://www.unicode.org/versions/Unicode6.2.0/)
* [版本6.1.0](http://www.unicode.org/versions/Unicode6.1.0/)
* [版本6.0.0](http://www.unicode.org/versions/Unicode6.0.0/)
* [版本5.2.0](http://www.unicode.org/versions/Unicode5.2.0/)
* [版本5.1.0](http://www.unicode.org/versions/Unicode5.1.0/)
* 版本5.0.0（不可用）
* [版本4.0.1](http://www.unicode.org/versions/Unicode4.0.1/)
* [版本4.0.0](http://www.unicode.org/versions/corrigendum5.html)




<br><br>


# 贡献

有关如何贡献的详细信息，请参阅 *Awesome Unicode* [贡献指南](CONTRIBUTING.md)。


# 行为准则

详情请参阅【行为准则】(CODE-OF-CONDUCT.md)。基本上可以归结为：
>为了营造开放和热情的环境，我们
贡献者和维护者承诺参与我们的项目并
我们的社区为每个人提供无骚扰的体验，无论年龄、身体状况如何
身材、残疾、种族、性别认同和表达、经验水平、
国籍、外表、种族、宗教或性认同和取向。


# 许可证
[![CC0](http://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

在法律允许的范围内，[
贡献者](https://github.com/jagracey/Awesome-Unicode/graphs/contributors)
已放弃本作品的所有版权以及相关或邻接权。请参阅
[许可证文件](LICENSE) 了解详细信息。
