# 很棒的 PICO-8 [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)


![PICO-8](https://www.lexaloffle.com/gfx/p8_jelpi.gif)
![tools](https://www.lexaloffle.com/gfx/p8_tracker.gif)
![code](https://www.lexaloffle.com/gfx/p8_cast.gif)

PICO-8 资源、教程、工具等的精选列表。受到 [awesome](https://github.com/sindresorhus/awesome) 列表的启发。您可能还喜欢 [awesome-lua](https://github.com/LewisJEllis/awesome-lua) 和 [awesome-love2d](https://github.com/JanWerder/awesome-love2d)。

PICO-8 是一款用于制作、共享和玩小游戏和其他计算机程序的梦幻控制台。当您打开它时，机器会向您显示一个 shell，用于输入 [Lua](https://www.lua.org/) 命令的子集，并提供简单的内置工具来创建您自己的卡带。

## 内容

- [Community](#community)
- [Demoscene](#demoscene)
- [Resources](#resources)
- [Tutorials](#tutorials)
- [Tools](#tools)
- [Libraries](#libraries)
- [Assets](#assets)
- [文本编辑器语言支持](#text-editors-language-support)
- [Hacks](#hacks---undocumented-pico-8-features)
- [Hardware](#hardware)
- [文章和帖子](#articles--posts)
- [Talks](#talks)
- [Clones](#clones)
- [Contributing](#i-want-to-contribute)
- [License](#license)

### 社区

- [Lexaloffle](https://www.lexaloffle.com)
  - [Blog](https://www.lexaloffle.com/bbs/?uid=1)
  - [PICO-8](https://www.lexaloffle.com/pico-8.php)
  - [Forum/BBS](https://www.lexaloffle.com/bbs/?cat=7)
  - [Twitter](https://twitter.com/lexaloffle)
  - [BlueSky](https://bsky.app/profile/lexaloffle.bsky.social)
  - [Mastodon](http://mastodon.social/@zep)
  - [Facebook](https://www.facebook.com/lexaloffle/)
  - [Youtube](https://www.youtube.com/user/lexaloffletv)
- [Subreddit](https://www.reddit.com/r/pico8/)
- [推特上的#pico8](https://twitter.com/hashtag/pico8)
- [蓝天#pico8](https://bsky.app/hashtag/pico8)
- [乳齿象上的 #pico8](https://mastodon.social/tags/pico8)
- [Freenode 上的 #pico8](https://webchat.freenode.net/?randomnick=1&channels=#pico8&prompt=1)
- [Pico-8 控制台新闻](https://twitter.com/pico8console)
- [Pico-8 维基](https://pico-8.wikia.com/wiki/Pico-8_Wikia)
- [Slack Team](https://slofile.com/slack/pico-8) - PICO-8 Slack 聊天。
- [Discord Server](https://discord.gg/EwQ86eq) - PICO-8 Discord 聊天。

### 演示场景

- [Demozoo 上的 Pico-8 演示](https://demozoo.org/platforms/81/)
- [Pouet 上的 Pico-8 演示](https://www.pouet.net/prodlist.php?platform%5B%5D=PICO-8)
- [带有demoscene效果代码的文章](https://medium.com/swlh/creativity-through-limitation-pico-8-fantasy-console-175294e13332)
- [YouTube 上的 Pico-8 演示](https://www.youtube.com/results?search_query=pico+8+demoscene)


### 资源

- [Official Manual](https://www.lexaloffle.com/pico-8.php?page=manual) - pico-8.txt 的占位符转储！ （适当的手册即将推出）。
- [PicoZine #1](https://sectordub.itch.io/pico-8-fanzine-1)、[#2](https://sectordub.itch.io/pico-8-fanzine-2)、[#3](https://sectordub.itch.io/pico-8-fanzine-3) 和 [#4](https://sectordub.itch.io/-pico-8-zine-4) - PICO-8 Zine 是由 PICO-8 用户制作并为 PICO-8 用户制作的 48 页同人杂志。
- [Going from Lua 5.2 to PICO-8's Lua](https://gist.github.com/josefnpat/bfe4aaa5bbb44f572cd0) - 本文档旨在帮助精通 Lua 的人们了解 Lua 和 PICO-8 的 Lua 之间的局限性和差异。
- [Cheat Sheet (printable)](https://ztiromoritz.github.io/pico-8-spick/) - 可打印格式的简化备忘单。提供德语和英语版本。
- [Cheat Sheet (wallpaper)](https://www.lexaloffle.com/bbs/?tid=28207) - 可打印备忘单的增强功能，可用作桌面壁纸。

### 教程

- [Music Tracker Tutorial Series](https://www.youtube.com/playlist?list=PLjZAika8vyZkyOjoCp0EbHeIFZ8MLlhvg) - 使用 PICO-8 制作音频。
- [Tron Lightcycle game from scratch](https://youtu.be/ZuaLuMhwcc8) - 快速介绍 PICO-8 从头开始​​编写游戏。
- [A PICO-8 Spaceshooter in 16 GIFs](https://ztiromoritz.github.io/pico-8-shooter/) - 逐步编写太空射击游戏的屏幕截图。
- [Token optimization](https://github.com/seleb/PICO-8-Token-Optimizations) - 保存代币的提示和技巧。
- [Tweetjam, BBS thread](https://www.lexaloffle.com/bbs/?tid=3726) - 代码适合推文的卡片（对于学习一些有趣的技术非常有用）。
- [Sample code on the BBS](https://www.lexaloffle.com/bbs/?search=sample+code) - 搜索并非 100% 准确，但其中一些卡片具有一些不错的技巧，您可以在将来的代码中重复使用。
- [Newgrounds Medals Tutorial](https://github.com/Bigaston/pico-8-newgrounds-tutorial) - 将 Newgrounds 奖章添加到 PICO-8 游戏的小教程。
- [Binary save system](https://ultiman3rd.wordpress.com/2018/02/01/pico-8-binary-save-system/) - 支持各种数据类型的自定义游戏保存系统
- [Lazy Devs Breakout](https://youtube.com/playlist?list=PLea8cjCua_P0qjjiG8G5FBgqwpqMU7rBk&si=CaivHwqC6uYjJA21) - [roguelikes] 的分步视频(https://youtube.com/playlist?list=PLea8cjCua_P3LL7J1Q9b6PJua0A-96uUS&si=ZYrBbZMJr9ABHsnA)， [shmups](https://youtube.com/playlist?list=PLea8cjCua_P3Sfq4XJqNVbd1vsWnh7LZd&si=bKKGy-2IKwcTQxeF) 等

### 工具

- [Sprite Editor](https://www.lexaloffle.com/bbs/?tid=51270) - 仅键盘 8x8 像素艺术工具。
- [pico2png](https://github.com/briacp/pico2png) - Spritesheet 提取是用 Perl 编写的。
- [Spritesheets and tools for the PICO-8 Palette](https://www.reddit.com/r/pico8/comments/3jhmni/spritesheets_and_tools_for_the_pico8_palette/) - 使用 PICO-8 调色板编译工程资产和工具。
- [Pico8Utils](https://github.com/josefnpat/pico8utils) - 基于处理 .p8 文件的 unix 理念编译 lua 脚本。
- [picotool](https://github.com/dansanderson/picotool) - 用于操作 Pico-8 游戏文件的工具和 Python 库。
- [p8dl - Carts Downloader - Python](https://github.com/franciscod/p8dl) - 将盒式磁带下载到正确的文件夹中（查看您的 config.txt）。
- [Pico-8 Carts Downloader - Bash ](https://github.com/kikookoubis/pico-8-carts-bash-downloader) - 从 BBS 下载盒式磁带（单个购物车、整个索引或转储您最喜欢的条目）并根据其元数据重命名它们。
- [p8 responsive webplayer transform](https://github.com/benwiley4000/pico8-responsive-webplayer-transform) - 使您的 HTML 导出页面具有响应能力的 Python 脚本。
- [Color Palette](https://www.romanzolotarev.com/pico-8-color-palette/) - Web 的十六进制和 RGB 颜色代码。
- [PICO-8 font](https://www.lexaloffle.com/bbs/?tid=3760) - 作者：[RhythmLynx](https://www.lexaloffle.com/bbs/?uid=11704)。
- [P8Coder](https://github.com/movAX13h/P8Coder) - 一种编程工具，可将 pico-8 卡带 (p8) 中的 lua 代码替换为您在 P8Coder 中编写的代码。
- [picoDeploy](https://github.com/torch2424/picoDeploy) - 将 Pico-8 购物车部署为桌面 (Electron) 和移动 (Ionic) 上的独立应用程序。
- [pico8Grunt](https://github.com/TeamNoComplyGames/pico8Grunt) - 使用 gruntjs 的 pico8 游戏构建系统。
- [PICO-EC](https://github.com/JoebRogers/PICO-EC) - 为 PICO-8 fantasty 控制台创建的小型场景实体组件库。
- [p8](https://github.com/jozanza/p8) - 依赖管理器和构建工具。允许您共享代码/精灵、“require()”依赖项以及保存时自动重新加载购物车。可与任何外部代码编辑器配合使用并支持 [MoonScript](https://moonscript.org/)。
- [MIDI to PICO-8](https://github.com/andmatand/midi-to-pico8) - 将 MIDI 文件转换为 PICO-8 音乐的工具。
- [midi2pico](https://github.com/gamax92/midi2pico) - MIDI 到 PICO-8 转换器。
- [Denote](https://bikibird.itch.io/denote) - 将 MIDI 文件转换为 SFX 数据 - 交互式且基于网络。
- [Custom template](https://www.lexaloffle.com/bbs/?tid=31000) - 一个简单干净的模板，解决了全屏、鼠标问题，而且看起来不错。
- [Fillp Tool](https://seansleblanc.itch.io/pico-8-fillp-tool) - 用于生成填充图案的简单辅助工具。
- [Depict](https://bikibird.itch.io/depict) - 使用 PICO-8 颜色将图像转换为抖动图像，并将其缩小到最大尺寸 128 x 128。
- [picoCAD](https://johanpeitz.itch.io/picocad) - 用于构建低多边形 3D 模型并对其进行纹理处理的 PICO-8 程序。
- [pico8-deploy](https://github.com/tducasse/pico8-deploy) - 将 PICO-8 项目导出并部署到 itch.io 的简单方法
- [yap8b](https://github.com/Enerccio/yap8b) - 用于从多个源文件创建 pico 购物车的构建工具。
- [TS-PICO-8](https://github.com/tmountain/pico-8-typescript) - 使用 TypeScript 创建 PICO-8 游戏。
- [Shrinko8](https://github.com/thisismypassport/shrinko8) - 一种大幅缩小 Pico-8 代码大小的压缩器。还包括 linter 和其他工具。
- [jspicl](https://github.com/jspicl/jspicl) - 使用 JavaScript 或 TypeScript 编写 PICO-8 游戏，并进行实时重新加载，这样您就可以立即看到您的更改！

### 图书馆

- [pico-test](https://github.com/jozanza/pico-test) - PICO-8 测试框架。
- [Lib-Pico8](https://github.com/clowerweb/Lib-Pico8) - 有用的常用函数的 Pico-8 库。
- [pico8-missing-builtins](https://github.com/adamscott/pico8-missing-builtins) - 为 pico8 提供 Lua 内置函数。
- [Pico-Kit](https://github.com/outkine/pico-kit) - 一系列固执己见的 Pico-8 助手，让您更容易上手。  添加了 OOP、更好的调试和物理。
- [PICO-Tween](https://github.com/JoebRogers/PICO-Tween) - 一个小型的补间/缓动函数库，用于 PICO-8 Fantasy 控制台，灵感来自 Robert Penner 的缓动函数。
- [parens-8](https://github.com/Siapran/parens-8) - 使用小型 lisp 解释器/编译器绕过 Lua 令牌限制。
- [p8-canvas](https://github.com/Siapran/p8-canvas) - 高性能无限画布/纹理库。
- [pico8-physics](https://github.com/jamesedge/pico8-physics) - Box2d 的 Pico8 实现，带有 8 个演示。
- [SCUMM-8](https://github.com/Liquidream/scumm-8) - 拆除 SCUMM 引擎，用于制作点击式经典冒险游戏。
  
### 资产
- [midilib](https://www.lexaloffle.com/bbs/?cat=7#tag=midilib) - 定制 SFX 乐器

### 文本编辑器语言支持

- Visual Studio Code: [pico8-ls](https://github.com/japhib/pico8-ls) - PICO-8 语言服务器，为 Lua 的 PICO-8 方言提供完整的语言支持。
- Atom：[语言-pico8](https://atom.io/packages/language-pico8)
- Sublime：[Sublime PICO-8](https://packagecontrol.io/packages/PICO-8) - Sublime Text 编辑器的 PICO-8 插件（配色方案、字体、构建系统、代码完成、片段...）。
- Vim: [vim-pico8-syntax](https://github.com/justinj/vim-pico8-syntax)
- Emacs：[pico8-mode](https://github.com/Kaali/pico8-mode)
- Visual Studio Code / NeoVim / JetBrains / 其他： [pico8-definitions](https://github.com/ahai64/pico8-definitions) - sumneko/lua 的附加组件，提供 PICO-8 语言支持。

### 字体编程

您可能有兴趣安装 [pico-8 编程字体](https://github.com/juanitogan/p8-programming-fonts)，它们支持 pico-8 自定义字符以及各种字体（位图和常规抗锯齿字体）。检查[此处的 BBS 线程](https://www.lexaloffle.com/bbs/?tid=28975)。

如何安装字体：

* **Linux:** 复制 ~/.fonts 和 `sudo fc-cache -f -v` 上的文件
* **Windows:** 将文件复制到 c:/windows/fonts/

### 黑客 - 未记录的 PICO-8 功能

- [Mouse](https://www.lexaloffle.com/bbs/?tid=3549) - 如何检索鼠标坐标（带演示）。
- [p8keyboard.js](https://github.com/dppc/p8keyboard.js) - Pico-8 的 Javascript“键盘适配器”。将 ASCII 字符发送到浏览器中运行的 Pico-8 程序。
- [SFX Modifications](https://www.lexaloffle.com/bbs/?tid=3561) - 四种只能通过修改内存才能应用的效果（带演示）。
- [Tracker State/Audio Memory Locations](https://www.lexaloffle.com/bbs/?pid=10719#p10719) - 如何在播放时访问和修改音频数据。

### 硬件

- [GameShell](https://www.clockworkpi.com/) - 模块化手持游戏机，可让您玩和修改复古游戏以及 DIY 新设备。检查 [GameShell 文档](https://github.com/clockworkpi/GameShellDocs/wiki/Running-PICO-8-on-the-GameShell) 了解如何在 GameShell 上运行 PICO-8。
- [PocketChip](https://shop.pocketchip.co/) - 专为随时随地玩耍和编码而设计的手持设备。 pico-8 正式支持。 [PoketChip版本的pico-8](https://www.lexaloffle.com/bbs/?tid=34009)

### 文章和帖子

- [Indie Retro News](https://www.indieretronews.com/2015/10/pico-8-8-bit-fantasy-console-from.html) - [@ABrugsch](https://twitter.com/ABrugsch) 对 PICO-8 进行了精彩介绍。

### 会谈

- [Sharing the love](https://www.youtube.com/watch?v=AmMYWD2Zbso) - 使用 PICO-8 制作游戏。 linux conf au 2017 - 澳大利亚霍巴特

### 克隆
- [TIC-80 by Nesbox](https://nesbox.itch.io/tic) - 微型计算机，适用于 HTML 5、Windows、Linux 32/64 位、Android 和 MacOSX
- [PicoLove](https://github.com/picolove/picolove) - LÖVE 中的 Pico-8 重新实现。
- [LIKO-12](https://github.com/RamiLego4Game/LIKO-12) - 一款使用 LÖVE 制作的开源幻想计算机，具有 96kb RAM。
- [Pikuseru](https://github.com/PikuseruConsole/pikuseru) - 纯 Rust [核心] 中的开源 Fantasy Console。
- [tac08](https://0xcafed00d.itch.io/tac08-rg350) - tac08 是 Pico-8 Fantasy 控制台运行时部分的仿真，在 RG350 手持游戏机上运行。
- [LowRes NX](https://lowresnx.inutilis.com/) - Fantasy Console 可在 IOS、MacOS、Windows、Linux 和 GameShell 上使用（BASIC 代码支持）
- [BeetPx](https://beetpx.dev/) - 用于像素艺术浏览器游戏的 TypeScript 框架。深受 PICO-8 启发。

### 我想贡献！

伟大的！ ：笑脸：

请先阅读[贡献指南](CONTRIBUTING.md)。

### 许可证

[![CC0](https://i.creativecommons.org/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

在法律允许的范围内，[Felipe Bueno](https://twitter.com/felipebueno) 已放弃本作品的所有版权以及相关或邻接权。

有关详细信息，请参阅[许可证]（许可证）。
