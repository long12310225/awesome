# 很棒的国际象棋 [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

互联网上与国际象棋相关的资产的精选列表。

*受到[awesome](https://github.com/sindresorhus/awesome)列表的启发。您可能想阅读完整的 [awesome](https://github.com/sindresorhus/awesome) 列表。*

### 贡献
请先阅读[贡献指南](https://github.com/hkirat/awesome-chess/blob/master/CONTRIBUTING.md#contribution-guidelines)。

内容
---
 - [Books](#books)
 - [FEN 解析器](#fen-parsers)
 - [移动验证器](#move-validators)
 - [Bots](#bots)
 - [Websites](#websites)
 - [Boards](#boards)
 - [董事会符号](#board-notations)
 - [Pieces](#pieces)
 - [Talks](#talks)

书籍
---
*有关国际象棋的书籍。*

 - [Chess Problems](https://kairavacademydotcom.files.wordpress.com/2013/06/john-thursby-75-chess-problems.pdf) - 国际象棋谜题的集合。
 - [Chess strategy](http://www.gutenberg.org/cache/epub/5614/pg5614-images.html) - 爱德华·拉斯克 (Edward Lasker) 的 HTML 版本的国际象棋策略。
 - [Sicilian Dragon](http://www.chesscity.com/PDF/Sicilian_Dragon_Black_Attacks_ssd.pdf) - 黑棋的进攻计划。

FEN 解析器
---
*福赛思-爱德华兹表示法 (FEN) 是描述国际象棋游戏特定棋盘位置的标准表示法。*

 - [fenparser by tlehman](https://github.com/tlehman/fenparser) - 用 Python 编写的 Forsyth-Edwards Notation 解析器。
 - [fen by ucarion](https://github.com/ucarion/fen) - 具有正确错误处理功能的 Rust Forsyth-Edwards 符号解析器。
 - [fen-diagram by andyherbert](https://github.com/andyherbert/fen-diagram) - 使用 Forsyth-Edwards 表示法生成国际象棋图表的 JavaScript。

机器人
---
*机器人是涉及人工智能的算法，用于与用户对战。*

 - [latrunculorum](https://github.com/benwr/latrunculorum) - Python 中的一个简单的国际象棋机器人。
 - [Chessbot](https://github.com/jfabeel/Chessbot) - 用 Java 编写的机器人。

移动验证器
---
*验证器是检查举动真实性的工具。*

 - [chess.js](https://github.com/jhlywa/chess.js) - chess.js，国际象棋身份验证的结构化代码。
 - [npm chess package](https://www.npmjs.com/package/chess) - 代数符号驱动的国际象棋引擎，可以验证棋盘位置并生成可行的移动列表。
 - [Chessnut](https://github.com/cgearhart/Chessnut.git) - Chessnut 是一个用 Python 编写的简单棋盘模型。它提供解析 FEN 并为每个 FEN 表示生成合法动作列表的功能。

网站
---
*网站包括供人们下棋的平台。*

 - [multiplayerchess.com](http://multiplayerchess.com) - 一个简单的单页国际象棋比赛应用程序，方便下棋。
 - [lichess.org](http://en.lichess.org/) - 最成熟的互联网下棋平台之一。它也是开源的。它配备了日常拼图和一台电视来观看其他比赛。
 - [chess24.com](https://chess24.com/en/play/chess) - 通过 chess24 的最佳教程来玩和学习国际象棋。
 - [chessbase.com](http://play.chessbase.com/js/apps/playchess/) - 用于下棋的利润丰厚的单页应用程序。
 - [chess.com](http://www.chess.com/) - 与超过 500 万其他用户一起学习和下棋。
 - [chesscademy.com](https://www.chesscademy.com/) - 观看视频、解决谜题、玩游戏。全部免费。 （与可汗学院类似。）
 - [chesstempo.com](http://chesstempo.com) - 在线国际象棋战术培训网站。
 - [chessprogramming.wikispaces.com](https://chessprogramming.wikispaces.com/) - 有关计算机下棋编程的信息存储库。
 - [freechess.org](http://freechess.org/) - “免费互联网国际象棋服务器”（FICS）是最古老的互联网国际象棋服务器之一。几乎所有可用的设备、操作系统或网络浏览器都有大量的客户端应用程序。

板
---
*板是用于封装渲染板过程的工具。*

 - [Chessboard.js](https://github.com/oakmac/chessboardjs/) - chessboard.js 是一个独立的 JavaScript 棋盘。
 - [chess-board](https://github.com/laat/chess-board) - 用于显示国际象棋位置的 Web 组件。它将 FEN 字符串作为输入，并将板渲染为输出。
 - [jchess](https://github.com/bmarini/jchess) - 一个基于 jQuery 的 JavaScript 库，用于解析和显示国际象棋游戏。目前采用 FEN 和 PGN 作为输入。
 - [Chessboard-js](https://github.com/caustique/chessboard-js) - 响应式移动优先 JavaScript 棋盘库。

董事会符号
---
*符号是一种以文本格式表达棋盘属性的方式。 [国际象棋记谱教程](http://chess.eusa.ed.ac.uk/Chess/Rules/notation.html).*

 - [FEN](https://en.wikipedia.org/wiki/Forsyth%E2%80%93Edwards_Notation) - FEN“记录”定义了特定的游戏位置，全部在一个文本行中并且仅使用 ASCII 字符集。
 - [PNG](http://www6.chessclub.com/help/PGN-spec) - PGN 的结构是为了“方便人类用户阅读和编写，以及方便计算机程序解析和生成”。
- 其他符号
- [代数国际象棋表示法](https://en.wikipedia.org/wiki/Algebraic_notation_(chess))
 	- [ICCF numeric notation](https://en.wikipedia.org/wiki/ICCF_numeric_notation) - 所有国际函授国际象棋联合会比赛的官方国际象棋比赛符号。
 	- [史密斯国际象棋记谱法](http://www6.chessclub.com/chessviewer/smith.html)
 	- [描述性符号](https://en.wikipedia.org/wiki/Descriptive_notation)

件
---
*这包括获取各种国际象棋作品的工具。*

 - [3D 螺旋片](https://www.thingiverse.com/thing:470700)
 - [维基百科上的文章](https://commons.wikimedia.org/wiki/Category:PNG_chess_pieces/Standard_transparent)
 - [Unicode 中的国际象棋棋子](https://en.wikipedia.org/wiki/Chess_symbols_in_Unicode)
 - [平面图标上的图标](http://www.flaticon.com/search/chess)
 - [thenounproject 上的图标](https://thenounproject.com/search/?q=chess)

会谈
---
*关于国际象棋的讲座。*
 
 - [Understanding Chess Mastery](https://www.youtube.com/watch?v=fPopQaY7Og4) - 詹妮弗·沙哈德 (Jennifer Shahade) 谈论如何理解国际象棋。
 - [How Chess Can Revolutionize Learning](https://www.youtube.com/watch?v=A3yDvM8aplY) - 科迪·彭慕兰 (Cody Pomeranz) 谈论国际象棋如何彻底改变学习。
 - [Working backward to solve problems](https://www.youtube.com/watch?v=v34NqCbAA1c) - 莫里斯·阿什利 (Maurice Ashley) 谈论逆向工作解决问题
 - [象棋人生](https://www.youtube.com/watch?v=lgCSo1Txw3c)
 - [Why Chess is Boring ](https://www.youtube.com/watch?v=7EuxVOgrEig) - 鲍比·费舍尔 (Bobby Fischer) 谈论国际象棋为什么无聊
 - [国际象棋窥视](https://www.youtube.com/watch?v=p027ysBt0_M)
