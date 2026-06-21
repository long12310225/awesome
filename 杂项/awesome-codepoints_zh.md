# 很棒的代码点 [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

这是 Unicode 字符的精选列表，其中有有趣的（并且
也许并不广为人知）功能或在其他方面很棒。

## 目录

1. [独立代码点](#standalone-code-points)
2. [影响他人的代码点](#code-points-that-affect-others)
1. [破坏和粘合其他字符](#break-and-gluing-other-characters)
3. [记录保持者和极端者](#record-holders-and-extremes)
4. [搞笑](#for-funsies)
1. [游戏](#games)
5. [其他代码点列表](#other-lists-of-code-points)
6. [贡献](#contributing-your-code-points)
7. [许可证](#license)

## 独立代码点

* Unicode 块的代码点 [Box
绘图](https://codepoints.net/box_drawing) (U+2500 到 U+257F) 和 [块
元素](https://codepoints.net/block_elements)（U+2580 至 U+259F）封面
大部分等宽命令行可视化需求。

        ╭───────╮
│统一码│
│规则！ │
        ╰┬─────┬╯
* [U+2E2E](https://codepoints.net/U+2E2E) 颠倒的问号 - “讽刺”
mark”来表达讽刺/挖苦。一个有用的角色&#x2E2E;
* [U+D800](https://codepoints.net/U+D800) 至
[U+DFFF](https://codepoints.net/U+DFFF) - 代理代码点。他们是
仅保留以缓解 [UTF-16
编码](https://en.wikipedia.org/wiki/UTF-16)。
* [U+FEFF](https://codepoints.net/U+FEFF) 零宽度无中断空间 - 它的名字
建议，它可以像 U+2060 WORD JOINER 一样使用。而事实上
引入后者是为了继承其语义。这是因为 U+FEFF 有
成为一个特殊的信标，称为[字节顺序
标记](https://en.wikipedia.org/wiki/Byte_order_mark)，被放置在
一些 UTF-8 文件的开头。在合规软件中（包括许多
文本编辑器）该字符从文件的开头被删除并且
作为元数据处理。在不合规的软件中（例如 PHP 解释器）
这会导致各种有趣的行为。
* [U+FFFD](https://codepoints.net/U+FFFD) 替换字符 - 当
无法显示字符（例如，解码错误的 UTF-8 序列），
该代码点进入了漏洞。
* [U+1D455](https://codepoints.net/U+1D455) 缺失。这将是斜体
小“h”。它没有被编码，因为它与普朗克相同
常数 ℎ ([U+210E](https://codepoints.net/U+210E))。
* [U+FF03](https://codepoints.net/U+FF03) 全宽数字符号 - 这是
“日本标签”`＃`。 Twitter 等网站将其视为等同于
常规“#”（[U+0023](https://codepoints.net/U+0023)）。

## 影响其他代码点

* [U+202D](https://codepoints.net/U+202D) 和
[U+202E](https://codepoints.net/U+202E) - 更改文本方向。
相关XKCD：

    [![](http://imgs.xkcd.com/comics/rtl.png )](https://xkcd.com/1137/)
* [U+FE0E](https://codepoints.net/U+FE0E) VARIATION SELECTOR-15 - 强制
黑_&_白表情符号。如果此代码点跟随表情符号，则显式
请求表情符号的单色渲染（如果客户端支持）。
* [U+FE0F](https://codepoints.net/U+FE0F) VARIATION SELECTOR-16 - 强制
多彩的表情符号。如果此代码点跟随表情符号，则为明确的彩色表情符号
请求渲染表情符号（如果客户端支持）。
* 变音符号和组合标记：有 [host of
字符](https://codepoints.net/search?gc=Mn)，添加
到之前的人物。这些称为组合标记。统一码
提供了一个[方便的常见问题解答](http://unicode.org/faq/char_combmark.html)
详细信息，但简而言之：如果在字符后添加一个，则会将其放置在
在上一个之上。所以，`a + ̊ = å`。这_可能_导致各种
有趣的问题，因为对于某些组合，有预先组合的
字符。我们这里的小“å”也可以编码为U+00E5。你可能会
请注意，虽然它的长度为一个字符，但“a”的组合
组合环的长度为两个字符。

当然，人们也可以和这些角色一起做一些有趣的事情，比如
StackOverflow 上的[此答案](http://stackoverflow.com/a/1732454/113195)。
* [区域指示符号](https://codepoints.net/U+1F1E6..U+1F1FF)
U+1F1E6 到 U+1F1FF 类似于 26 个拉丁字符。他们习惯了
创建旗帜表情符号。由于 Unicode 联盟不想继续下去
与国际政治接轨，旗帜的解决方案是结合
这 26 个字符对应一个国家/地区的相应 ISO 代码。示例：

国家 | ISO 代码 |代码点 |表情符号（如果支持）
    --------|----------|-------------------|---------------------
美国 |美国 | U+1F1FA + U+1F1F8 | &#x1F1FA;&#x1F1F8;
德国 |德国 | U+1F1E9 + U+1F1EA | &#x1F1E9;&#x1F1EA;
中国 |中文 | U+1F1E8 + U+1F1F3 | &#x1F1E8;&#x1F1F3;
* 表情符号的肤色：有五个代码点，控制肤色
表情符号，[U+1F3FB 到 U+1F3FF](https://codepoints.net/U+1F3FB..U+1F3FF)。
它们被称为“表情符号修饰符 Fitzpatrick 类型”1 至 6，其中 1 最浅
6是最暗的。如果这些字符之一跟随表情符号，则该表情符号
旨在以[Fitzpatrick]的适当肤色进行渲染
比例]（https://en.wikipedia.org/wiki/Fitzpatrick_scale）。如果没有这样的
添加修饰剂后，肤色应该不自然，例如。 例如，亮黄色。
有趣的事实：由于 Fitzpatrick 修饰符是正常的代码点，因此表情符号
这种肤色的长度为 2，这是 Twitter 用户首先注意到的。
这是一个对比图【直接来自
规范](http://www.unicode.org/reports/tr51/tr51-2.html#Diversity):

代码|名称 |样品
    --------|-------------------------------------|---------
U+1F3FB |表情符号修改器 FITZPATRICK TYPE-1-2 | <img src="http://www.unicode.org/reports/tr51/images/other/swatch-type-1-2.png" alt="" height="20" width="auto"> <img src="http://www.unicode.org/reports/tr51/images/other/swatch-type-1-2-bw.png" alt="" height="20" width="auto">
U+1F3FC |表情符号修改器 FITZPATRICK TYPE-3 | <img src="http://www.unicode.org/reports/tr51/images/other/swatch-type-3.png" alt="" height="20" width="auto"> <img src="http://www.unicode.org/reports/tr51/images/other/swatch-type-3-bw.png" alt="" height="20" width="auto">
U+1F3FD|表情符号修改器 FITZPATRICK TYPE-4 | <img src="http://www.unicode.org/reports/tr51/images/other/swatch-type-4.png" alt="" height="20" width="auto"> <img src="http://www.unicode.org/reports/tr51/images/other/swatch-type-4-bw.png" alt="" height="20" width="auto">
U+1F3FE|表情符号修改器 FITZPATRICK TYPE-5 | <img src="http://www.unicode.org/reports/tr51/images/other/swatch-type-5.png" alt="" height="20" width="auto"> <img src="http://www.unicode.org/reports/tr51/images/other/swatch-type-5-bw.png" alt="" height="20" width="auto">
U+1F3FF |表情符号修改器 FITZPATRICK TYPE-6 | <img src="http://www.unicode.org/reports/tr51/images/other/swatch-type-6.png" alt="" height="20" width="auto"> <img src="http://www.unicode.org/reports/tr51/images/other/swatch-type-6-bw.png" alt="" height="20" width="auto">

### 破坏和粘合其他角色

* [U+00A0](https://codepoints.net/U+00A0) 无中断空格 - 强制相邻
字符粘在一起。在 HTML 中众所周知的“&nbsp;”。
* [U+00AD](https://codepoints.net/U+00AD) 软连字符 - （HTML 中：`&shy;`）
与 ZERO WIDTH SPACE 类似，但如果（且仅当）发生中断时显示连字符。
* [U+200B](https://codepoints.net/U+200B) 零宽度空间 - 与
U+00A0：不创建空格，但允许断字。
* [U+200D](https://codepoints.net/U+200D) 零宽度连接器 - 强制相邻
要连接在一起的字符（例如，阿拉伯字符或支持的
表情符号）。苹果用它来组成一些像不同家庭的表情符号。
* [U+2060](https://codepoints.net/U+2060) WORD JOINER - 与
U+00A0，但完全看不见。适合在 Twitter 上写“@font-face”。

为了更好地比较哪个代码点具有哪种效果，请参阅此
表：

| U+00A0 | U+00AD | U+200B | U+200D | U+2060
---------------|--------|--------|--------|--------|--------
创造空间|   ✓ |   ✗ |   ✗ |   ✗ |   ✗
允许破坏|   ✗ |   ✓ |   ✓ |   ✗ |   ✗
可能的改变|   ✗ |   ✓ |   ✗ |   ✓ |   ✗

Smashing 杂志精选[综合
文章](http://www.smashingmagazine.com/2015/10/space-yourself/)
不同类型的空白。

## 记录保持者和极限

* [U+0000](https://codepoints.net/U+0000) <control> - 第一个代码点。
* [U+10FFFF](https://codepoints.net/U+10FFFF) (_非字符_) - 最后一个代码
点。除了 U+10FFFE 之外的整个平面的其余部分，代码点
在0x10000-0x10FFFD范围内，是私有字符，保证
永远不会被未来的 Unicode 标准所填补。
* [U+1F402](https://codepoints.net/U+1F402) OX - 最短名称。
* U+1FBA8 盒子图浅色对角线 上中心到左中，中右到下中心
和
U+1FBA9 包装盒图浅色对角线上中心到右中和左中到下中心 - 最长名称：88
每个字符。
* [U+FDFA](https://codepoints.net/U+FDFA) 阿拉伯连字 SALLALLAHOU ALAYHE
WASALLAM - 最长分解形式：18 个字符。
* [U+5146](https://codepoints.net/U+5146) 和
[U+16B61](https://codepoints.net/U+16B61) - 表示的代码点
最高的“个位数”数字。在这两种情况下都是 1,000,000,000,000，
万亿。
* [U+0F33](https://codepoints.net/U+0F33) 藏文数字半零 - 代码点
代表_最低_“个位数”数字，同时
只有负数，-1/2。
* 最无用代码点的奖杯授予
[U+0080](https://codepoints.net/U+0080),
[U+0081](https://codepoints.net/U+0081) 和
[U+0099](https://codepoints.net/U+0099)。这些所谓的C1控制
字符或多或少未指定。他们进入了 Unicode，因为
它们出现在后来成为 ISO 的第一个版本中
10646，ISO 标准化版本的 Unicode。他们[本应成为一部分
升级到 ISO
2022](http://unicode.org/mail-arch/unicode-ml/y2015-m10/0050.html)，即
从未出现过。
* 在这方面紧随其后的是中日韩统一表意文字
    [妛](https://codepoints.net/U+599B),
    [挧](https://codepoints.net/U+6327),
    [暃](https://codepoints.net/U+6683),
    [椦](https://codepoints.net/U+6926),
    [槞](https://codepoints.net/U+69DE),
    [蟐](https://codepoints.net/U+87D0),
    [袮](https://codepoints.net/U+88AE),
    [閠](https://codepoints.net/U+95A0),
    [駲](https://codepoints.net/U+99F2),
    [墸](https://codepoints.net/U+58B8),
    [壥](https://codepoints.net/U+58E5), and
    [彁](https://codepoints.net/U+5F41). These so-called [“ghost characters”](https://www.dampfkraft.com/ghost-characters.html)
通过日本 JIS 标准来到 Unicode，它们被添加到其中，因为
在编制 JIS 时，它们与其他标志被误读或误解
来自原始印刷文本来源。
* [U+006F](https://codepoints.net/U+006F) 拉丁文小写字母 O - 领先列表
具有令人困惑的形状的字符。在所有可能的映射中
[易混淆的列表
字符](http://www.unicode.org/reports/tr39/#Data_Files)，小“o”
领先的有多达 73 个看起来相似的字形条目，其次是
[U+006C](https://codepoints.net/U+006C) 带有 70 的拉丁文小写字母 L
条目。
* [U+1F4C0](https://codepoints.net/U+1F4C0) DVD - 仅代码点名称，不含任何元音（[来源](https://twitter.com/ken_lunde/status/960188623390846976)）
* [U+3106C](https://codepoints.net/U+3106C) 中日韩统一表意文字 3106C -
最多的角色
[笔划](https://en.wikipedia.org/wiki/Chinese_character_lines)：84。
花点时间写这篇吧！

## 对于有趣的人

* [U+1680](https://codepoints.net/U+1680) OGHAM SPACE MARK - 一个看起来的空间
像破折号一样。很高兴让程序员接近疯狂：`1 +  2 === 3`。
* [U+037E](https://codepoints.net/U+037E) 希腊问号 - 类似于
分号。这也是一种惹恼开发人员的有趣方式。
* [U+1DD2](https://codepoints.net/U+1DD2) 结合我们上面 - 这是最
浪漫的代码点。
* [U+F8FF](https://codepoints.net/U+F8FF) 私人使用代码点 - 此私人
使用代码点在许多 Apple 设备上呈现为 Apple 徽标。
* [U+1F574](https://codepoints.net/U+1F574) 西装男子悬浮 -
一个相当奇怪的字符，只是因为它的特性才被纳入 Unicode
以 Webdings 字体显示（出于向后兼容性的原因）。
* [U+1F596](https://codepoints.net/U+1F596) 举手，中间有一部分
中指和无名指——瓦肯敬礼。长寿并繁荣！
&#x1F596;
* [U+1F918](https://codepoints.net/U+1F918) 号角标志 - 继续摇滚！
&#x1F918;
* [U+2800](https://codepoints.net/U+2800) 盲文图案空白 - 填充了六个或八个点中的零个点的盲文图案。根据标准：“*虽然此字符在许多字体中被成像为固定宽度的空白，但它并不充当空格”本质上它被渲染为空白，但由于它被指定为*非*空白，所以它与空白验证正则表达式。这可用于绕过禁止或修剪空白的各种验证。


### 游戏

对于纯文本游戏，Unicode 配备了几套完整的：

* [国际象棋棋子](https://codepoints.net/U+2654..U+265F)。
* [纸牌套装](https://codepoints.net/U+2660..U+2667) 甚至一整副 [纸牌]
卡](https://codepoints.net/playing_cards) 配有小丑和背面
卡的。
* [骰子面孔](https://codepoints.net/U+2680..U+2685) 和一个漂亮的[骰子
表情符号](https://codepoints.net/U+1F3B2)。
* [Go 件](https://codepoints.net/U+2686..U+2689)。
* [跳棋（或跳棋）棋子](https://codepoints.net/U+26C0..U+26C3)。
* [将棋棋子](https://codepoints.net/U+2616,U+2617,U+26C9,U+26CA)，一个
[国际象棋的日本变体](https://en.wikipedia.org/wiki/Shogi)。
* [多米诺骨牌](https://codepoints.net/domino_tiles)
* [麻将牌](https://codepoints.net/mahjong_tiles)

## 其他代码点列表

* [Cross-platform terminal characters](https://github.com/ehmicky/cross-platform-terminal-characters) - 适用于大多数终端的字符列表。

## 贡献您的代码点

详情请参阅[贡献指南](CONTRIBUTING.md)。

## 许可证

[![CC0](https://i.creativecommons.org/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

在法律允许的范围内，[
贡献者](https://github.com/Codepoints/awesome-codepoints/graphs/contributors)
已放弃本作品的所有版权以及相关或邻接权。参见
[许可证文件](LICENSE) 了解详细信息。
