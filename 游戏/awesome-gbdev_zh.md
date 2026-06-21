# ![GameboyIcon](http://i.imgur.com/ROUq7NT.gif) 很棒的 Game Boy 开发

#### 加入我们的 Discord

精选的 Game Boy（彩色）开发资源、工具、文档、相关项目和开源 ROM 列表。受到 [awesome](https://github.com/sindresorhus/awesome) 列表的启发。

您可以在[此处](https://gbdev.github.io/resources)找到此列表的（更酷的）网络版本。

## 内容

- [Introduction](#introduction)
  - [Disambiguation](#disambiguation)
- [Community](#community)
- [Documentation](#documentation)
  - [Misc](#misc)
  - [Opcodes](#opcodes)
  - [游戏男孩颜色](#game-boy-color)
  - [Hardware](#hardware)
  - [Peripherals](#peripherals)
  - [Cartridges](#cartridges)
- [模拟器开发](#emulator-development)
  - [Testing](#testing)
- [软件开发](#software-development)
  - [Assemblers](#assemblers)
  - [Compilers](#compilers)
    - [实验/概念验证](#experimentalproof-of-concepts)
  - [Emulators](#emulators)
  - [Tools](#tools)
    - [Engines](#engines)
    - [开发工具](#development-tools)
    - [图形实用程序](#graphics-utilities)
    - [硬件和 ROM 实用程序](#hardware-and-rom-utilities)
    - [音乐驱动程序和跟踪器](#music-drivers-and-trackers)
- [Programming](#programming)
  - [ASM](#asm)
    - [Sources](#sources)
    - [Timings](#timings)
    - [Boilerplates](#boilerplates)
    - [语法高亮包](#syntax-highlighting-packages)
  - [C](#c)
- [Homebrews](#homebrews)
  - [ASM](#asm-1)
  - [C](#c-1)
  - [GB工作室](#gb-studio)
  - [Demos](#demos)
- [逆向工程](#reverse-engineering)
  - [游戏拆解](#game-disassemblies)
- [游戏男孩相机](#game-boy-camera)
  - [检索图像](#retrieving-images)
  - [改变相机的行为](#changing-the-cameras-behavior)
  - [Post-processing](#post-processing)
- [相关项目](#related-projects)
  - [Directories](#directories)
  - [Websites](#websites)
- [About](#about)
  - [Contribute](#contribute)
  - [License](#license)
  - [Acknowledgements](#acknowledgements)
  - [Sponsors](#sponsors)

## 简介

- [Game Boy，硬件剖析](https://www.youtube.com/playlist?list=PLu3xpmdUP-GRDp8tknpXC_Y4RUQtMMqEu)
- [终极游戏男孩谈话](https://media.ccc.de/v/33c3-8029-the_ultimate_game_boy_talk)


> ### 消歧义
>
> #### Game Boy Advance
>
> Game Boy Advance 开发由另一个项目 [awesome-gbadev](https://github.com/gbdev/awesome-gbadev) 列表涵盖。
> 然而，GBA *可以运行* GB/GBC 游戏。与本机硬件相比，它的实现方式略有不同：此列表的模拟器开发部分对此进行了介绍。
>
> #### Game Boy Color 和 Super Game Boy
>
> 此列表重点关注原始 *Game Boy*（GB 或 DMG，1989）、*Game Boy Color*（GBC 或 CGB）和 *Super Game Boy* (SGB) 是非常相似的系统，但有一些重要的区别，例如：
>
>>- 硬件规格不同；
>> 具体的硬件和软件功能；
>>- 特定寄存器；
>- 特定的错误、怪癖和可利用的行为。
>
>如果您的目标是为 SGB 或 GBC 开发软件，或者您想知道它如何在其他系统上运行，您可能想利用并适应这些差异，请检查 [Game Boy Color](#game-boy-color) 类别并查找 GBC/CGB 和 SGB 的具体参考。


## 社区

- [聊天频道](https://gbdev.io/chat)
- [Forum](https://gbdev.gg8.se/forums/)

## 文档

- [**Pan Docs**](https://gbdev.github.io/pandocs/) - 向公众提供的唯一、最全面的 Game Boy 技术参考。由社区修正、更新和维护。
- [The Cycle-Accurate Game Boy Docs](https://github.com/AntonioND/giibiiadvance/blob/master/docs/TCAGBD.pdf) - AntonioND 的精确文档，用于制作周期精确的 Game Boy 模拟器。
- [Complete Technical Reference](https://gekkio.fi/files/gb-docs/gbctr.pdf) - 由盖基奥.
- [Game Boy Architecture: A Practical Analysis](https://www.copetti.org/writings/consoles/game-boy/) - 作者：罗德里戈·科佩蒂。
- [Game Boy Project Report](http://www.cs.columbia.edu/~sedwards/classes/2019/4840-spring/reports/GameBoy.pdf) - 硬件[模拟器](https://github.com/kitsuneh/SVGameBoy)（在 Terasic DE1-SoC 板上）的报告，作为哥伦比亚大学 CSEE4840 嵌入式系统设计课程的最终项目而开发。

#### 操作码

- [gb-opcodes](https://gbdev.github.io/gb-opcodes/optables/) - 操作码表
- [RGBDS opcodes reference](https://rgbds.gbdev.io/docs/gbz80.7) - 所有指令的参考，包括简短描述、周期和字节计数以及标志修改的解释。

### 游戏男孩颜色

- [引导程序ROM](https://tcrf.net/Game_Boy_Color_Bootstrap_ROM)
- [未使用的调色板](https://tcrf.net/Notes:Game_Boy_Color_Bootstrap_ROM)
- [BIOS 中的调色板](https://forums.nesdev.org/viewtopic.php?p=114388#p114388)
- [引导ROM反汇编](https://gist.github.com/drhelius/6063265)
- [GBC Hicolour notes](https://romhack.github.io/doc/gbcHiColour/) - 关于 Game Boy Color 的 Hicolour 模式技巧及其在 GBC 游戏“Crystalis”中的实现的技术说明。

### 硬件

- [DMG Schematics](http://gbdev.gg8.se/wiki/articles/DMG_Schematics) - 硬件原理图。
- [The Game Boy Project](http://marc.rawer.de/Gameboy/Docs/GBProject.pdf) - 提供有关实现三个 8 位双向并行端口的硬件研究和详细结构信息。
- [Related custom hardware](https://github.com/Gekkio/gb-hardware) - 由盖基奥.
- [ESP8266 GB Dev Board](https://github.com/applefreak/esp8266-gameboy-dev-board) - 用于 Game Boy 配件开发的开发板，由 ESP8266 提供支持。
- [ESP8266 GB Printer](https://github.com/applefreak/esp8266-gameboy-printer) - 一种模拟 GB 打印机并允许您使用 WiFi 检索图像的设备。
- [fruttenboel](https://web.archive.org/web/20220628023315/https://verhoeven272.nl/fruttenboel/Gameboy/index.html) - 页面包含有关硬件、与控制台和其他相关项目连接的自定义板的大量信息。
- [Game Boy hardware database](https://gbhwdb.gekkio.fi/) - 各种类型 Game Boy 游戏机的数据和照片。
- [dmg-schematics](https://github.com/msinger/dmg-schematics) - DMG-CPU B 芯片的原理图和带注释的覆盖图，从芯片照片中提取，使用 KiCad 制作。还包含 Electric VLSI 库，其中包含一些单元和存储器的布局。

### 周边设备

- [Dan Docs](https://shonumi.github.io/dandocs.html) - 模糊的 Game Boy 硬件文档。
- [Edge of Emulation](https://shonumi.github.io/articles.html)，一系列有关模拟和研究 Game Boy 配件的文章。也可作为 GBE 模拟器文档中的[技术文档](https://github.com/shonumi/gbe-plus/tree/master/src/docs/technical) 获取。
  - [Mobile Adapter GB](https://shonumi.github.io/articles/art14.html) - Game Boy Color 上的互联网连接和 DLC。
  - [Game Boy 打印机](https://shonumi.github.io/articles/art2.html)
  - [Pocket Sonar](https://shonumi.github.io/articles/art13.html) - 带有内置声纳硬件的蓝色推车。
  - [Zok Zok Heroes](https://shonumi.github.io/articles/art8.html) - Zok Zok Heroes 的 Full Changer，一款动作激活配件。
  - [Infrared Madness](https://shonumi.github.io/articles/art11.html) - Game Boy Color 上的红外通信。
  - [Game Boy 4-Player Adapter](https://shonumi.github.io/articles/art9.html) - DMG-07。
  - [Barcode Boy](https://shonumi.github.io/articles/art7.html) - 第一个 Game Boy 卡片扫描仪。
  - [Barcode Taisen Bardigun](https://shonumi.github.io/articles/art6.html) - 90 年代末 DMG-GBC 条码阅读器。
- [DMG-07 技术文档](https://raw.githubusercontent.com/shonumi/gbe-plus/master/src/docs/technical/DMG_07.txt)
- [Game Boy Camera RE](https://github.com/AntonioND/gbcam-rev-engineer) - 有关 GB 相机以及用于使用 Arduino 对其进行逆向工程的工具的文档。
- [使用神经网络和 Gameboy 相机创建逼真的图像](http://www.pinchofintelligence.com/photorealistic-neural-network-gameboy/)
- [The Game Boy Printer](https://shonumi.github.io/articles/art2.html) - 关于打印机硬件、通信协议以及游戏用于实现打印功能的常用例程的深入技术文档。
- [Ben Heck 逆向工程师 Game Boy 打印机](https://www.youtube.com/watch?v=43FfJvd-YP4)（勘误表：使用的热敏纸已过期，实际上可以打印 4 种颜色）。
- [Arduino Game Boy Printer Emulator](https://github.com/mofosyne/arduino-gameboy-printer-emulator) - 通过 Game Boy Link 电缆和 Arduino 模拟 Game Boy 打印机。
- [手机游戏男孩适配器](https://bulbapedia.bulbagarden.net/wiki/Mobile_Game_Boy_Adapter)
- [GB KISS LINK 调制解调器](http://nectaris.tg-16.com/GB-KISS-LINK-FAQ-hudson-gameboy-nectaris.html)

### 墨盒

- [GB Flash Cartridges for Sale](https://bbbbbr.github.io/GameBoy-Flash-Carts/) - 可用的现成 Game Boy 闪存盒列表。
- [AntonioND's docs](https://github.com/AntonioND/giibiiadvance/tree/master/docs) - 更正了墨盒标题数据的原理图和信息。
- [Gekkio's Game Boy cartridge types](http://gekkio.fi/blog/2015-02-14-mooneye-gb-gameboy-cartridge-types.html) - 现有墨盒类型的概述。
- Gekkio的墨盒分析：
- [DMG-BEAN-02](http://gekkio.fi/blog/2015-05-18-mooneye-gb-cartridge-analysis-dmg-bean-02.html);
- [MBC1](http://gekkio.fi/blog/2015-05-17-mooneye-gb-cartridge-analysis-fortress-of-fear.html);
- [无 MBC](http://gekkio.fi/blog/2015-02-28-mooneye-gb-cartridge-analysis-tetris.html)。
- Tauwasser 维基上某些墨盒类型的引脚分配、寄存器描述和 VHDL 代码：
  - [MBC1](https://wiki.tauwasser.eu/view/MBC1)
  - [MBC2](https://wiki.tauwasser.eu/view/MBC2)
  - [MMM01](https://wiki.tauwasser.eu/view/MMM01)
- [Game Boy Cartridges Schematics](http://www.devrs.com/gb/files/gb.html) - MBC2 和 MBC3 类型的原理图。
- [墨盒 PCB 照片](https://imgur.com/a/D5bpC)
- [MBC1+RAM+Battery cartridge Schematic](http://www.devrs.com/gb/files/mbc1.gif) - Jeff Frohwein 绘制的第一张示意图。
- [MBC1 and MBC2 cartridges circuits](http://fms.komkon.org/GameBoy/Tech/Carts.html) - 并解释这些 MBC Bank 如何切换和控制 RAM。
- [GB Rom List](CartridgeList.csv) - 每个已发布游戏的导航表以及其卡带的详细信息。
- [Game Boy 卡带 PCB 照片](http://gekkio.fi/blog/2016-03-19-game-boy-cartridge-pcb-photos.html)


#### 定制墨盒

- [Emulating a GameBoy Cartridge](https://dhole.github.io/post/gameboy_cartridge_emu_1/) - 使用开发板 STM32F4 模拟 Game Boy 卡带的功能。
- [Wolf](http://www.happydaze.se/wolf/) - 带协处理器的 Game Boy 卡带。
- [Homebrew-Gameboy-Cartridge](https://github.com/dwaq/Homebrew-Gameboy-Cartridge) - 使用 Atmel AT49F040 作为 ROM 的盒式 PCB 的 Eagle 库、原理图和电路板文件。
- [Homebrew Gameboy Color Cartridge](https://github.com/Xyl2k/Gameboy-Color-Cartridge) - EEPROM 供电盒的电路板布局。
- [Nekocart](https://github.com/zephray/NekoCart-GB) - 使用 Xilinx CPLD 作为 MBC5 的开源闪存盒（[帖子](https://hackaday.io/project/41160-nekocart-cpld-gameboy-cartridge)）。
- [Reiner Ziegler's Game Boy page](http://reinerziegler.de.mirrors.gg8.se/) - 商业和自制的可编程盒和编程系统。提供教程、接线和原理图。
- [Gameboy-MBC5-MBC1-Hybrid](https://github.com/insidegadgets/Gameboy-MBC5-MBC1-Hybrid) - MBC5/MBC1 混合盒的 CPLD 实现。

#### 杂项

- [Introduction to Game Boy Hacking](http://pepijndevos.nl/sha2017/workshop.pdf) - 介绍基本组装、调试和逆向工程的车间。
- [GBSOUND.txt](https://github.com/bwhitman/pushpin/blob/master/src/gbsound.txt) - 详细介绍 Game Boy 声音引擎的文档。
- [gbdev FAQs](http://www.devrs.com/gb/files/faqs.html) - 杰夫·弗罗温 (Jeff Frohwein) 的必读之作。
- [Game Boy Bootrom](http://www.neviksti.com/DMG/DMG_ROM.asm) - 注释 DMG bootrom 的转储。
- [Z80 和 Gameboy 处理器之间的差异](http://www.z80.info/z80gboy.txt)
- [Gameboy 2BPP Graphics Format](http://www.huderlem.com/demos/gameboy2bpp.html) - 有关 Game Boy 如何将 VRAM 图块数据解释为彩色像素的信息。

## 模拟器开发

- [Reverse Engineering fine details of Game Boy hardware](https://www.youtube.com/watch?v=GBYwjch6oEE) - Gekkio 在 Disobey 2018 上发表的 43 分钟演讲（[勘误表](https://gekkio.fi/blog/2018-02-05-errata-for-reverse-engineering-fine-details-of-game-boy-hardware.html)）。
- [Emulation of Nintendo Game Boy](https://github.com/Baekalfen/PyBoy/blob/master/extras/PyBoy.pdf) - 从构建模拟器的角度概述 Game Boy 硬件。
- [DMG-01](https://rylev.github.io/DMG-01/public/book/) - Rust 中的教育版 Gameboy 模拟器以及解释其开发的配套书籍。 *[哦，孩子！用 Rust 创建 Game Boy 模拟器](https://media.ccc.de/v/rustfest-rome-3-gameboy-emulator) - 是 Rust Fest 18 上关于此问题的演讲。
- [Building a Game Boy emulator in JavaScript](http://imrannazar.com/gameboy-Emulation-in-JavaScript) - 一步一步的教程。
- [编写 Game Boy 模拟器 Cinoop](https://cturt.github.io/cinoop.html)
- [0dmg](https://jeremybanks.github.io/0dmg/2018/05/23/getting-started.html) - 通过构建部分 Game Boy 模拟器来学习 Rust。
- [RealBoy Emulator](https://realboyemulator.wordpress.com/posts/) - 关于 RealBoy 模拟器的设计和实现的一系列帖子。
- [Codeslinger](http://www.codeslinger.co.uk/pages/projects/gameboy.html) - 另一个记录模拟器构建的系列文章。
- [Why did I spend 1.5 months creating a Gameboy emulator?](http://blog.rekawek.eu/2017/02/09/coffee-gb/) - 博客文章。
- [binjgb rewind](https://binji.github.io/2017/12/31/binjgb-rewind.html) - 实现*倒带- 功能。
- [binjgb on the web](https://binji.github.io/2017/02/26/binjgb-on-the-web-part-1.html) - 将 binjgb 模拟器移植到 Web Assembly。 [（第 2 部分）](https://binji.github.io/2017/02/27/binjgb-on-the-web-part-2.html)
- [binjgb debugging hangs](https://binji.github.io/2017/05/03/debugging-hangs.html) - 对仿真怪癖的调查。
- [Decoding Gameboy Z80 opcodes](https://gb-archive.github.io/salvage/decoding_gbz80_opcodes/Decoding%20Gamboy%20Z80%20Opcodes.html) - 如何通过算法解码 Game Boy 指令（而不是编写一个巨大的 switch-case 语句）。
- [将 GO Game Boy 模拟器移植到 WebAssembly](https://djhworld.github.io/post/2018/09/21/i-ported-my-gameboy-color-emulator-to-webassembly/)
- [About swotGB](https://mitxela.com/projects/swotgb/about) - 有关用 JavaScript 开发 Game Boy 模拟器的说明。
- [开源模拟器列表](EMULATORS.md)
- [Game Boy Doctor](https://github.com/robert/gameboy-doctor) - 一种命令行工具，用于将模拟器中的日志与已知正确的模拟器中的日志进行比较。对于 Blargg 测试 ROM 的逐行调试很有用。

### 测试

- [Blargg 的测试版](http://gbdev.gg8.se/files/roms/blargg-gb-tests/)
- [Gekkio 的测试版](https://gekkio.fi/files/mooneye-gb/latest/)
- [SameSuite](https://github.com/LIJI32/SameSuite)
- [粉蚧茶室测试](https://github.com/mattcurrie/mealybug-tearoom-tests)
- [国标精度测试](http://tasvideos.org/EmulatorResources/GBAccuracyTests.html)
- [144p Test Suite](https://github.com/pinobatch/240p-test-mini/tree/master/gameboy) - Artemio Urbina 的 240p 测试套件移植到 Game Boy。
- [MBC3 RTC 测试 ROM](https://github.com/aaaaaa123456789/rtc3test)
- [dmg-acid2](https://github.com/mattcurrie/dmg-acid2) 和 [cgb-acid2](https://github.com/mattcurrie/cgb-acid2) - 基本 PPU 渲染测试。

## 软件开发

[选择 Game Boy 开发工具](https://gbdev.io/guides/tools.html) 文章概述了 Game Boy 的可用开发工具。

### 装配工

- [RGBDS](https://github.com/gbdev/rgbds) - 汇编器和链接器包。 [文档](https://rgbds.gbdev.io)。
- [ASMotor](https://github.com/csoren/asmotor) - 针对 Game Boy 等 CPU 的汇编引擎和开发系统。由 RGBDS 原作者编写。 [文档](https://github.com/asmotor/asmotor/tree/develop#further-reading)。
- [wla-dx](https://github.com/vhelin/wla-dx) - 另一个 GB-Z80/Z80/... 多平台交叉汇编程序包。 [文档](http://www.villehelin.com/wla.txt)。

### 编译器

- [GBDK](https://github.com/gbdk-2020/gbdk-2020/) - 由 SDCC 工具链更新版本提供支持的 GBDK（Game Boy 开发套件）的维护和现代化。提供 C 编译器、汇编器、链接器和一组库。
  - [API 文档：入门](https://gbdk-2020.github.io/gbdk-2020/docs/api/docs_getting_started.html)
  - [Examples](https://github.com/mrombout/gbdk_playground)
  - [文档、链接和工具](https://gbdk-2020.github.io/gbdk-2020/docs/api/docs_links_and_tools.html)
- [Turbo Rascal Syntax Error](https://lemonspawn.com/turbo-rascal-syntax-error-expected-but-begin/) - 完整的套件（IDE、编译器、编程语言、资源编辑器），用于为 8 / 16 位计算机系列开发游戏/演示，包括 Game Boy 和 Game Boy Color。

#### 实验/概念验证

- [RGBDS-Live](https://gbdev.io/rgbds-live) - 用于尝试 RGBDS 的浏览器内编码环境。
- [Wiz](https://github.com/wiz-lang/wiz) - 一种高级汇编语言，用于在复古游戏机平台（Game Boy、NES、Atari 2600 等）上编写自制程序。
- [gbforth](https://github.com/ams-hackers/gbforth) - 基于 Forth 的 Game Boy 开发套件。
- [gbasm-rs](https://gitlab.com/BonsaiDen/gbasm-rs) - 一个基于 Rust 的 Game Boy z80 汇编代码的固执己见的编译器。
- [gbasm](https://github.com/BonsaiDen/gbasm) - 基于 JavaScript 的 Game Boy z80 汇编代码编译器。
- [tniASM](http://www.tni.nl/products/tniasm.html) - 宏汇编器。
- [Assembler](https://github.com/ulrikdamm/Assembler) - 用 Swift 编写的汇编程序。
- [llvm-gbz80](https://github.com/Bevinsky/llvm-gbz80) / [clang-gbz80](https://github.com/Bevinsky/clang-gbz80) - GBZ80 CPU 的 Clang/LLVM 端口（类似于已弃用的[euclio/llvm-gbz80](https://github.com/euclio/llvm-gbz80))。
- [gbdk-go](https://github.com/pokemium/gbdk-go) - 编译器将 Go 程序翻译为 C 代码。输出的C代码由GBDK内置到GB ROM中。
- [Rust-GB](https://github.com/zlfn/rust-gb) - 一个编译器和库，支持使用 Rust 开发 GB ROM。

### 模拟器

- [BGB](https://bgb.bircd.org/) - 强大的模拟器和调试器。提供准确的硬件仿真。
- [SameBoy](https://github.com/LIJI32/SameBoy) - 精确的仿真器，具有各种强大的调试功能。
- [Mooneye GB](https://github.com/Gekkio/mooneye-gb) - Rust 中的研究项目和模拟器。
- [mGBA](https://github.com/mgba-emu/mgba) - 现代跨平台 GBA 模拟器，也运行 GB/GBC 游戏。
- [Binjgb](https://github.com/binji/binjgb) - 通过大部分测试的 5Kloc 模拟器。 *倒带功能。使用 WebAssembly 在浏览器中运行。
- [Gambatte](https://github.com/gb-archive/gambatte) - 跨平台且准确的模拟器。

- [MetroBoy](https://github.com/aappleby/MetroBoy) - 整个 Game Boy 的可玩电路级模拟。
- [gbe-plus](https://github.com/shonumi/gbe-plus) - 最近重写的模拟器，在保留不起眼的附件的功能方面付出了巨大的努力（例如 IR 连接、移动网络 GB、Barcode Boy、GB 打印机、本地和在线 GB 串行链路电缆，...）
- [Emulicious](https://emulicious.net/) - 提供准确的模拟，并包括强大的工具，例如通过 [VS Code 调试适配器](https://marketplace.visualstudio.com/items?itemName=emulicious.emulicious-debugger) 对 ASM 和 C 进行分析器和源代码级调试。

[开源模拟器完整列表](EMULATORS.md)

### 工具

#### 发动机

- [ZGB](https://github.com/Zal0/ZGB) - 一个用于为原始 Game Boy 创建游戏的小引擎（扩展了 gbdk，更多信息[此处](http://zalods.blogspot.com/2017/01/zgb-little-engine-for-game-boy.html)）。
- [Retr0 GB](https://bitbucket.org/HellSuffering/retr0-gb/) - 用于创建游戏的引擎（扩展 GBDK）。

#### 开发工具

- [GBExtended](https://www.tensi.eu/thomas/programming/utilities/gbx_library/gbx_library.html) - 扩展 gbdk 的 C 库。
- [gbdk-lib-extension](https://github.com/ProGM/gbdk-lib-extension) - Michael Hope 的 Game Boy 开发套件的一小部分源代码和工具。
- [mgbdis](https://github.com/mattcurrie/mgbdis) - 具有 RGBDS 兼容输出的 Game Boy ROM 反汇编器。
- [ROM Header Utility](http://catskull.net/GB-Logo-Generator/) - 用于检查和修改 ROM 标头数据（包括徽标）的在线工具。
- [romusage](https://github.com/bbbbbr/romusage) - 用于从 .map、.noi 或 ihx 文件估计 Game Boy ROM 的使用情况（可用空间）的命令行工具。适用于 GBDK-2020 和 RGBDS。
- [awake](https://github.com/devdri/awake) - Game Boy 反编译器。
- [Game Boy Text Tools](https://github.com/raphaklaus/gameboy-text-tools) - 用于文本操作和用 Node.js 编写的 Game Boy ROM 翻译的工具集。
- [evscript](https://github.com/eievui5/evscript) - Game Boy 的脚本语言，可用于敌人 AI、对话、动画和协程。
- [evunit](https://github.com/eievui5/evunit) - 汇编代码的单元测试程序。
- [opcode_count](https://github.com/rondnelson99/opcode_count) - 使用 Python 和 Emulicious 生成最常运行的 CPU 指令的统计信息

#### 图形实用程序

- [Game Boy Tile Data Generator](https://github.com/chrisantonellis/gbtdg) - HTML5 / JS Web 应用程序，可将位图图像转换为适合在基于图块的图形应用程序（特别是 GB）中使用的十六进制数据。
- [Harry Mulder's GB Development](http://www.devrs.com/gb/hmgd/intro.html) - Game Boy Tile Designer (GBTD) 和 Game Boy Map Builder (GBMB) 工具的一些来源和主页。
- [GBTiles](https://github.com/bashaus/gbtiles) - 将使用 Harry Mulder 的 Tile Designer (GBTD) 创建的 .GBR 文件和使用 Harry Mulder 的 Map Builder (GBMB) 创建的 .GBM 文件转换为不同的格式，以便与 Game Boy 和 GBDK 一起使用。
- [bmp2cgb](https://github.com/gitendo/bmp2cgb) - 用于 Game Boy 颜色开发的图形转换器，提供实时调色板调整。
- [png2gb](https://github.com/LuckyLights/png2gb) - 用于将图像文件转换为 game boy .c 数组的 CLI 工具。
- [GB-convert](https://github.com/gb-archive/gb-convert) - Game Boy 瓷砖转换和地图编辑器工具（转换为组件）。
- [brewtool](http://make.vg/brewtool/) - 原始编辑器/转换器工具的集合，用于制作用于自制 ROM 开发的资源。
- [vtGBte](https://github.com/paul-arutyunov/vtGBte) - 简约的 ncurses 磁贴编辑器。
- [tpp1](https://github.com/TwitchPlaysPokemon/tpp1) - 自定义 GB/GBC 内存/硬件映射器的定义和规范，作为 MBC 的功能超集。
- [libstdgb](https://github.com/delwink/libstdgb) - 有用的 Game Boy 操作 (SDCC) 的 C 库。
- [Tilemap GB](https://github.com/bbbbbr/gimp-tilemap-gb) - GIMP 图像编辑器插件，用于导入和导出 GBMB 和 GBTD 图块地图和图块集（作为位图图像或 .GBM/.GBR 文件）。
- [Tilemap Helper](https://github.com/bbbbbr/gimp-tilemap-helper) - 用于优化图块地图和图块集的 GIMP 图像编辑器插件。
- [Tilemap Studio](https://github.com/Rangi42/tilemap-studio) - 适用于 Game Boy、Color、Advance 和 SNES 项目的图块地图编辑器。使用 C++ 和 FLTK 编写。
- [Superfamiconv](https://github.com/Optiroc/SuperFamiconv) - 灵活且可组合的图块图形转换器支持 Super Nintendo、Game Boy、Game Boy Color、Game Boy Advance、Mega Drive 和 PC Engine 格式。

#### 硬件和 ROM 实用程序

- [cart-dumper](https://github.com/Palmr/cart-dumper) - Game Boy 卡带转储器 ROM。
- [gbcamextract](https://github.com/jkbenaim/gbcamextract) - 从 Game Boy 相机保存中提取照片。
- [Game Boy LCD sniffing](https://github.com/svendahlstrand/game-boy-lcd-sniffing) - 使用逻辑分析仪嗅探 Game Boy 的 LCD。
- [swapdump](https://github.com/sanqui/swapdump) - Game Boy 烧录卡的诊断实用程序。
- [Gameboy-LinkUp](https://github.com/JustinLloyd/Gameboy-LinkUp) - Game Boy LinkUp 串行电缆网络项目。

#### 音乐驱动程序和跟踪器

- [DevSoundX](https://github.com/DevEd2/DevSoundX) - 可嵌入自制软件中的声音驱动程序，支持脉冲宽度操作、琶音和多种波形。
- [Carillon Player](http://gbdev.gg8.se/files/musictools/Aleksi%20Eeben/Carillon%20Editor.zip) - 音乐引擎。
- [GBT PLAYER](https://github.com/AntonioND/gbt-player) - 音乐播放器库和转换器套件。
- [mmlgb](https://github.com/SimonLarsen/mmlgb) - 适用于 Nintendo Game Boy 的 MML 解析器和 GBDK 声音驱动程序。
- [XPMCK](https://github.com/bazzinotti/XPMCK) - 基于 MML 的音乐编译器，支持 Game Boy 和 Game Boy Color。
- [GBSoundSystem](https://github.com/gbdev/GBSoundSystem) - GameBoy Tracker（又名 Paragon 5 音乐播放器）的现代化音频驱动程序。
- [hUGETracker](https://github.com/SuperDisk/hUGETracker) - 基于 OpenMPT 的音乐跟踪器，专注于自制游戏中的易用性、紧凑输出和可嵌入性。
- [CBT-FX](https://github.com/datguywitha3ds/CBT-FX) - 兼容FX-Hammer音效的GBDK-2020音效驱动。

## 编程

使用[软件开发](#软件开发)章节中描述的开发工具链为 Game Boy 开发软件的指南、教程和工具。

### 先进制造商

- **[gb asm 教程](https://gbdev.io/gb-asm-tutorial)** - 分步教程，构建几个 ROM 来配合其解释。
- [hardware.inc](https://github.com/tobiasvl/hardware.inc) - 标准包含文件包含用于 RGBDS 项目的 Game Boy 硬件定义。
- [Assembly tutorial by David Pello](https://gb-archive.github.io/salvage/tutorial_de_ensamblador/tutorial_de_ensamblador_la_decadence.html) - 学习为 GB 生成工作 asm 代码的好文档。许多重要主题的简要解释。许多带有注释源代码的示例。
- [assemblydigest](https://github.com/assemblydigest/gameboy) - 探索 Game Boy 编程技术：
  - [制作一个空的 Game Boy ROM（在 Wiz 中）](https://assemblydigest.tumblr.com/post/77203696711/tutorial-making-an-empty-game-boy-rom-in-wiz)
  - [为 Game Boy 创作艺术](https://assemblydigest.tumblr.com/post/77404621743/tutorial-making-art-for-the-game-boy)
- [Beginner's Guide to Reverse Engineering GB](http://web.archive.org/web/20150511145100/http://www.bennvenn.com/Beginners_Guide_To_Reverse_Engineering.htm) - 有关反汇编和逆向工程的一些入门技巧。
- [FlappyBoy：制作一个简单的 Game Boy 游戏](http://voidptr.io/blog/2017/01/21/GameBoy.html)
- [Super Game Boy development](https://imanoleasgames.blogspot.no/2016/12/games-aside-1-super-game-boy.html) - 逐步教程来实现 Super Game Boy 功能（框架和调色板）。
- [GameBoy programming tutorial: Hello World!](https://peterwynroberts.wordpress.com/2014/05/11/gameboy-programming-tutorial-hello-world/) - 一步一步的教程。
- [DMGreport](https://github.com/lancekindle/DMGreport) - 汇编游戏编程教程。
- [OAM DMA tutorial](https://gbdev.gg8.se/wiki/articles/OAM_DMA_tutorial) - 如何在汇编中使用 OAM DMA 的示例。
- [Game Boy Assembly Programming for the Modern Game Developer](https://github.com/ahrnbom/gbapfomgd) - 关于在 Assembly 中制作 Game Boy 游戏的电子书。

#### 来源

代码片段、效果、概念证明以及通常不完整的游戏。

- [dev'rs ASM section](https://web.archive.org/web/20250329180046/http://www.devrs.com/gb/asmcode.php) - 很多工作演示和资源。
- [EmmaEwert's experiments](https://github.com/EmmaEwert/gameboy) - 原型程序的集合，大部分只是玩玩。其中包括日光效果、透明度和天气效果。
- [DeadCScroll](https://github.com/gb-archive/DeadCScroll) - 有关如何使屏幕摆动以及其他“光栅效果”的详细教程

#### 时间安排

- [实质内容 Gameboy 周期计时](http://blog.kevtris.org/blogfiles/Nitty%20Gritty%20Gameboy%20VRAM%20Timing.txt)
- [模式 3 精灵时序](https://old.reddit.com/r/EmuDev/comments/59pawp/gb_mode3_sprite_timing/)
- [GameBoy Color DMA-传输 v0.0.1](http://gameboy.mongenel.com/dmg/gbc_dma_transfers.txt)
- [STAT 中断时序](http://gameboy.mongenel.com/dmg/istat98.txt)
- [视频计时](https://github.com/jdeblese/gbcpu/wiki/Video-Timing)

#### 样板文件和库

- [rgbds-template](https://github.com/nezticle/rgbds-template) - 使用 RGBDS 的 Game Boy 基本 hello-world 示例。
- [Game Boy Assembly Language Primer](http://www.devrs.com/gb/files/galp.zip) - 带有内存定义、复制例程和 IBM 字体图块图的简单模板代码。
- [bootstrap.gb](https://github.com/yenatch/bootstrap.gb) - Game Boy 项目示例。
- [Gameboy Boilerplate](https://github.com/junebug12851/GameboyBoilerplateProj) - 样板项目可以更快地进入游戏的实际汇编代码。
- [GingerBread](https://github.com/ahrnbom/gingerbread) - 用于制作您自己的 Game Boy 游戏的软件库。它与《现代游戏开发人员的 Game Boy 汇编编程》(https://github.com/ahrnbom/gbapfomgd) 一书一起使用，该书也兼作文档。
- [gb-vwf](https://github.com/ISSOtm/gb-vwf) - 用于打印可变宽度文本的库，附带演示。
- [gb-boilerplate](https://github.com/ISSOtm/gb-boilerplate) - 用于启动 Game Boy 项目的模板，为基础设施提供 Makefile。
- [gb-starter-kit](https://github.com/ISSOtm/gb-starter-kit) - 对上述内容的扩展，包括基础库代码以及更快上手。
- [gb-template](https://github.com/gb-archive/gb-template) - 具有手柄输入、DMA 传输和地图/图块数据加载等基本功能的模板。

#### 语法高亮包

- [gbz80-highlight](https://github.com/ISSOtm/gbz80-highlight) - Notepad+- 和 gedit 语法高亮显示用于 RGBDS 汇编的文件。
- [Vim syntax file for the Game Boy assembler RGBASM](http://www.vim.org/scripts/script.php?script_id=819) - RGBDS 汇编的 Vim 语法高亮显示。
- [Vim syntax file for RGBDS](https://github.com/Leandros/dotfiles/blob/master/.vim/syntax/rgbds.vim) - 另一个用于 RGBDS 汇编的 Vim 语法突出显示文件。
- [sublime-rgbds](https://packagecontrol.io/packages/RGBDS) - 用于 RGBDS 的 Sublime Text 3 包，包括语法突出显示和一些完成片段。
- [Z80 程序集对 Visual Studio Code 的支持](https://github.com/Imanolea/z80asm-vscode)
- [rgbds-vscode](https://github.com/DonaldHays/rgbds-vscode) - RGBDS GBZ80 程序集的 Visual Studio Code 语言扩展。
- [rgbds-mode](https://github.com/japanoise/rgbds-mode) - RGBDS 汇编的 Emacs 主要模式。

### C

- [8-Bit Wonderland](https://github.com/gb-archive/salvage/blob/master/misc/8bit_wonderland.pdf) - 关于 Game Boy 如何工作以及如何开始为其开发工作代码的详细介绍性文档。
- [Grooves Game Boy Programming](https://github.com/gbdk-salvage/grooves-game-boy-programming) - 关于在 Game Boy 游戏中实现各种游戏机制的完整课程。
- [How to Write a Simple Side Scrolling Game](http://pastebin.com/F3tHLj68) - 旧的（但仍然相关）教程。
- [只是另一个简单的教程](http://web.archive.org/web/20230327070526/http://pastebin.com/gzT47MPJ)
- [GBDK Tutorial](https://refreshgames.co.uk/2016/04/18/gameboy-tutorial-rom/) - 用于 GBDK 入门的相当简单的游戏演示。
- [GBDK Sprite](http://gbdev.gg8.se/wiki/articles/GBDK_Sprite_Tutorial) - 展示了用于显示多个精灵并为其设置动画的工作流程。
- [GBDK Color](http://gbdev.gg8.se/wiki/articles/GBDK_Color_Tutorial) - 通过向精灵、背景和窗口层添加颜色，扩展您在 Game Boy 上的基本精灵绘制知识。
- [GBDK Joypad](http://gbdev.gg8.se/wiki/articles/GBDK_Joypad_Tutorial) - 详细介绍了手柄与GBDK的使用。
- [Game Boy home of Flavor](https://web.archive.org/web/20210427064949/www.personal.triticom.com/~erm/GameBoy/) - 一些完整的游戏和资源。
- [GBDK Configuring and Programming Tutorial](https://videlais.com/2016/07/03/programming-game-boy-games-using-gbdk-part-1-configuring-programming-and-compiling/) - 配置 GBDK、使用 Tiles、碰撞精灵、GBTD、GBMB、内存管理和 ROM Banking。
- [简化的 GBDK 示例](https://github.com/mrombout/gbdk_playground)
- [GBDK Programming Video Tutorials](https://www.youtube.com/playlist?list=PLeEj4c2zF7PaFv5MPYhNAkBGrkx4iPGJo) - 向初学者介绍 GBDK 编程的一系列视频教程。
- [Larold's Retro Gameyard](https://laroldsretrogameyard.com/category/tutorials/gb/) - 基于 GBDK-2020 的详细教程的集合。

## 自制啤酒

完整且开源的游戏。

- [Homebrew Hub](https://hh.gbdev.io) - 由社区主导的尝试，旨在收集、存档和保存为 Game Boy 发布的所有未经许可的自制游戏。参赛作品可在线播放。

### 先进制造商

- [Tuff](https://github.com/BonsaiDen/Tuff.gb)
- [2048-gb](https://github.com/Sanqui/2048-gb)
- [Snake](https://bitbucket.org/Sanqui/snake/src/?at=master)
- [Lazerpong](https://github.com/huderlem/lazerpong)
- [Geometrix](https://github.com/AntonioND/geometrix)
- [µCity](https://github.com/AntonioND/ucity)
- [Carazu](https://github.com/mholtkamp/carazu)
- [Snake-gb](https://github.com/DonaldHays/snake-gb)
- [GB303](https://github.com/furrtek/GB303) - 基于 GB303 波表的 TB-303 风格合成器，适用于 Nintendo Game Boy。
- [Sushi](https://github.com/JustSid/Sushi)
- [Flappy-boy-asm](https://github.com/bitnenfer/flappy-boy-asm)
- [kupman](https://github.com/dubvulture/gbdev) 和其他一些项目。
- [Adjustris](https://github.com/tbsp/Adjustris)
- [exeman](https://github.com/gb-archive/exeman)
- [Aevilia](https://github.com/ISSOtm/Aevilia-GB)
- [GBSlides](https://github.com/Kartones/gameboy) - 一个简单的类似 Game Boy Powerpoint 的幻灯片查看器。
- [Pokered-gbc](https://github.com/dannye/pokered-gbc) - 《神奇宝贝红》重制版，完全支持 GBC。
- [ToyToy](https://github.com/tslanina/Retro-GameBoyColor-ToyToy)
- [StefaN](https://github.com/tslanina/Retro-GameBoyColor-StefaN) - Fourway 突破克隆。
- [Galaxia](https://github.com/tslanina/Retro-GameBoyColor-Galaxia)
- [desgb](https://github.com/sanqui/desgb) - DES 加密。
- [superhappyfunbubbletime](https://github.com/l0k1/superhappyfunbubbletime)
- [minesweepGB](https://github.com/lancekindle/minesweepGB)
- [利贝特和魔法地板](https://github.com/pinobatch/libbet)
- [waveform-gb](https://github.com/dannye/waveform-gb) - 程序可视化波通道使用的波形。波形可以自由编辑，波形回放立即更新。
- [vectroid.gb](https://gitlab.com/BonsaiDen/vectroid.gb) - 使用 gbasm 开发。
- [PlantBoy](https://github.com/gb-archive/plantboy)
- [死亡星球](https://makrill.itch.io/death-planet)
- [Quartet](https://makrill.itch.io/quartet) - 适用于 Game Boy（彩色）和 Super Game Boy 的益智游戏。
- [Dangan](https://snorpung.itch.io/dangan-gb)

### C

- [FlappyBoy](https://github.com/bitnenfer/FlappyBoy)
- [flappybird-gameboy](https://github.com/pashutk/flappybird-gameboy)
- [fbgb](https://github.com/gb-archive/fbgb)
- [Novascape](https://web.archive.org/web/20171002042716/http://ludumdare.com/compo/ludum-dare-34/?action=preview&uid=6823)
- [软软的乌龟](https://github.com/cppchriscpp/SquishyTheTurtle)
- [Quadratino](https://github.com/avivace/quadratino)
- [豪医生](https://github.com/elfgames/doctorhow)
- [Super Princess' 2092 Exodus](https://github.com/Zal0/gbjam2016) - （[ZGB 引擎](https://github.com/Zal0/ZGB/)）。
- [GBsnake](https://github.com/brovador/GBsnake)
- [gb-mines](https://github.com/andreasjhkarlsson/gb-mines)
- [oranges](http://www.atari2600land.com/gameboy/oranges.html)
- [炽热公主大屠杀](https://github.com/Imanolea/bitbitjam3_red_hot_princess_carnage)
- [loderunner](https://www.tensi.eu/thomas/programming/games/loderunner/loderunner.html)
- [Hives](https://refreshgames.co.uk/2017/04/24/ludum-dare-38-entry-hives/)
- [Bubble Factory](https://github.com/DonaldHays/bubblefactory) - *Vanilla-SDCC（无 gbdk）。
- [GBC Atari Boxing](https://github.com/rubfi/gbc-atari-boxing) - Game Boy 的 Atari 2600 Boxing 克隆版（彩色）。
- [GB raycaster, Vision-8](https://github.com/haroldo-ok/really-old-stuff/tree/master/gameboy) - 以及其他一些项目。
- [Tobu Tobu Girl Deluxe](https://github.com/SimonLarsen/tobutobugirl-dx) - Game Boy（彩色）的街机平台游戏。
- [魁梧熊 vs. 卑鄙狐狸](http://sebastianmihai.com/gameboy-burly-bear.html) ([GBC](http://sebastianmihai.com/gameboy-color-burly-bear.html) 端口)
- [PostBot](https://github.com/MasterIV/PostBot)
- [枪与骑手](https://github.com/kanfor/gunsridersgameboy)
- [Dino's Offline Adventure](https://github.com/gingemonster/DinosOfflineAdventure) - Google Chrome 离线游戏的克隆。
- [dino-gb](https://github.com/rnegron/dino-gb) - Chrome 游戏的另一个克隆。
- [Evoland.gb](https://github.com/flozz/evoland.gb) - 进化大陆第一层的港口。
- [Petris](https://github.com/bbbbbr/Petris) - Game Boy Color 的形状优美的宠物益智游戏 ([itch.io](https://bbbbbr.itch.io/petris))。
- [Infinity](https://github.com/gb-archive/infinity-gbc) - 角色扮演游戏主要由 Affiix Software 在 1999 年至 2001 年间开发。该游戏从未找到发行商，最终被取消。最近发布了完整的源代码、开发工具和工作流程。
- [Black Castle](https://gbdev.gg8.se/forums/viewtopic.php?id=743) - Game Boy 的横向滚动平台游戏 ([itch.io](https://user0x7f.itch.io/black-castle))。
- [Genesis](https://gbdev.gg8.se/forums/viewtopic.php?id=674) - Game Boy 的 Shmup ([itch.io](https://user0x7f.itch.io/genesis))。
- [毁坏坦克！](https://antonylavelle.itch.io/indestructotank-gb)
- [超级JetPak DX](https://asobitech.itch.io/super-jetpak-dx)
- [Powa!](https://aiguanachein.itch.io/powa) - Game Boy（彩色）的横向卷轴平台游戏（[ZGB 引擎](https://github.com/Zal0/ZGB/)）。
- [Cavern](https://thegreatgallus.itch.io/cavern-mvm-9) - （[ZGB 引擎](https://github.com/Zal0/ZGB/)）。
- [Mona and the Witch's Hat Deluxe](https://ctneptune.itch.io/mona-and-the-witchs-hat-dx) - （[ZGB 引擎](https://github.com/Zal0/ZGB/)）。
- [弹跳球](https://gamejolt.com/games/the-bouncing-ball-gb/86699)
- [DMG 造成伤害](https://drludos.itch.io/dmg-deals-damage)
- [totp-gb](https://github.com/dmang-dev/totp-gb) - TOTP (RFC 6238) 二因素身份验证器，具有 SGB 边框、GBC 调色板和 MBC3 RTC 时钟。

### GB工作室

- [Soul Void](https://kadabura.itch.io/soul-void) - 互动恐怖小说。
- [Deadeus](https://izma.itch.io/deadeus)
- [超级冒名顶替者兄弟。](https://lumpytouch.itch.io/super-impostor-bros)

### 演示

- [返回颜色](https://github.com/AntonioND/back-to-color)
- [beach-gbc](https://github.com/vegard/beach-gbc)
- [可爱的演示](https://github.com/mills32/CUTE_DEMO)
- [‘10 PRINT’ Game Boy](https://github.com/svendahlstrand/10-print-game-boy)
- [机器人演示](https://github.com/naavis/roboto-demo)
- [matrix-rain-gb](https://github.com/wtjones/matrix-rain-gb) - 汇编器中的矩阵数字雨效果。
- [GBVideoPlayer](https://github.com/LIJI32/GBVideoPlayer) - 技术演示演示了如何破解 Game Boy LCD 控制器，使 Game Boy Color 播放彩色全动态视频和音乐。
- [GBVideoPlayer2](https://github.com/LIJI32/GBVideoPlayer2) - 上述演示的第二次迭代提高了分辨率，添加了*立体声 PCM 音频，并引入了视频压缩*。

## 逆向工程

- [逆向工程《星之卡比的梦境 2》](http://ecc-comp.blogspot.it/2016/03/reverse-engineering-kirbys-dreamland-2.html)
- [pokemontools](https://github.com/pret/pokemon-reverse-engineering-tools) - 一个Python模块，为各种神奇宝贝游戏提供各种逆向工程组件。
- [Reverse Engineering a Gameboy ROM with radare2](https://www.megabeets.net/reverse-engineering-a-gameboy-rom-with-radare2) - 使用radare2 对 Game Boy ROM 挑战进行逆向工程的演练。
- [Disassembling Link's Awakening](http://kemenaran.winosx.com/posts/category-disassembling-links-awakening/) - 关于拆解林克觉醒DX的一系列博文。
- [GameBoy 俄罗斯方块逆向工程](https://github.com/h3nnn4n/Reverse-Engineering-the-GameBoy-Tetris)
- [DMA hijacking](https://gbdev.io/guides/dma_hijacking) - 一种简单的技术，允许您在大多数 GB/SGB/CGB 游戏中运行自定义代码，前提是您有 ACE 漏洞。

### 游戏拆解

- [神奇宝贝红/蓝](https://github.com/pret/pokered)
- [神奇宝贝水晶](https://github.com/pret/pokecrystal)
- [神奇宝贝黄](https://github.com/pret/pokeyellow)
- [神奇宝贝金银](https://github.com/pret/pokegold)
- [神奇宝贝弹球](https://github.com/pret/pokepinball)
- [神奇宝贝卡牌游戏](https://github.com/pret/poketcg)
- [pokegold-spaceworld](https://github.com/pret/pokegold-spaceworld) - 神奇宝贝金银 1997 年太空世界演示。
- [林克的觉醒DX](https://github.com/mojobojo/LADX-Disassembly)
- [历代神谕](https://github.com/drenn1/ages-disasm)
- [Tetris](https://github.com/vinheim3/tetris-gb-disasm) - 完成俄罗斯方块拆解。
- [外汇锤](https://github.com/DevEd2/FXHammer-Disasm)
- [牧场物语 3](https://github.com/sanqui/hm3)
- [最终幻想冒险](https://daid.github.io/FFA-Disassembly/)
- [丛林之书](https://github.com/not-chciken/jungle-book-gb-disassembly)

## 游戏男孩相机

### 检索图像

Game Boy 打印机模拟（例如从相机检索图像）：

- [Arduino Gameboy Printer Emulator](https://github.com/mofosyne/arduino-gameboy-printer-emulator) - 通过 Gameboy 连接线模拟 Gameboy 打印机。
- [ESP8266 Game Boy Printer](https://github.com/applefreak/esp8266-gameboy-printer) - 一款模拟 Gameboy 打印机的设备，可让您使用由 ESP8266 供电的 WiFi 检索图像。
- [WiFi GBP Emulator](https://github.com/HerrZatacke/wifi-gbp-emulator) - GameBoy 打印机模拟器，通过 WiFi 连接提供接收到的数据。
- [Game Boy WiFi Printer - D1 Mini Shield](https://github.com/cristofercruz/gbp-esp-shield-pcb) - 适用于 D1 mini/mini Pro ESP8266 板的 Game Boy 打印机接口扩展板。
- [Game Boy Printer Sniffer](https://github.com/mofosyne/GameboyPrinterSniffer) - 嗅探 Game Boy 和打印机之间的数据包通信。

### 改变相机的行为

改进和/或操纵相机的质量和行为的方法：

- [Game Boy 相机佳能 EF 镜头卡口](http://ekeler.com/game-boy-camera-canon-ef-mount)
- [Game Boy Camera to Canon Lens mount](https://www.thingiverse.com/thing:4337362) - 基于上述。
- [game-boy-camera-frame-replacer](https://github.com/cristofercruz/game-boy-camera-frame-replacer) - 操作相机的 ROM 以包含自定义帧

### 后处理

- [Game Boy Printer Paper Simulation](https://github.com/mofosyne/GameboyPrinterPaperSimulation) - 生成数字打印图像的打印图像。
- [Game Boy Printer Web](https://github.com/HerrZatacke/gb-printer-web) - 适用于 Game Boy 相机的图库应用程序：从导出或卡带转储中导入图片并选择调色板。

## 相关项目

- [GB Studio](https://www.gbstudio.dev/) - 通过简单、无需知识的可视化脚本拖放游戏创建器。
  - [入门资源](https://gbstudiocentral.com/resources/)
  - [专用不和谐](https://discord.gg/knRryZWGcm)
  - [Lets Build a Platformer Game!](https://gumpyfunction.itch.io/lets-build-a-platformer) - 该课程旨在教任何人如何使用 GB Studio 4+ 创建平台游戏。
- [ArduinoBoy](https://github.com/trash80/Arduinoboy) - 从 Arduino 到 Game Boy 的串行通信 (MIDI)，适用于 LittleSoundDJ、Nanoloop 和 mGB 等音乐应用程序。
- [papiGB](https://github.com/diegovalverde/papiGB) - Game Boy Classic 从头开始​​实现全功能 FPGA。
- [fpgaboy](https://github.com/trun/fpgaboy) - 在 FPGA 上实现任天堂的 Game Boy 控制台。
- [Piglet](https://github.com/danShumway/Piglet) - 一个 LUA 驱动的 AI，通过实验玩经典的 Game Boy 彩色游戏。正在积极开发中。
- [Ostrich](https://github.com/PumpMagic/ostrich) - 用 Swift 编写的 Game Boy 声音系统播放器。
- [mGB](https://github.com/trash80/mGB) - 一个 Game Boy 卡带程序，使 Game Boy 能够充当完全支持 MIDI 的声音模块。
- [GBVisualizer](https://github.com/LIJI32/GBVisualizer) - 演示如何使用两个未公开的 Game Boy Color 寄存器，昵称为 PCM12 (FF76) 和 PCM34 (FF77)，可用于读取 4 个 APU 通道的当前 PCM 幅度。
- [ArduinoGameBoy](https://github.com/drhelius/arduinogameboy) - 基于 Arduino 的 Game Boy 卡带读取器和写入器。
- [gameboy-brainfuck](https://github.com/bitnenfer/gameboy-brainfuck) - 脑残翻译。
- [gbfk](https://github.com/elseyf/gbfk) - Brainf*ck 解释器，带输入。
- [gb-save-states](https://github.com/mattcurrie/gb-save-states) - 为在原始硬件上玩 Game Boy 游戏时添加保存状态支持的补丁。
- [gbcpu](https://github.com/jdeblese/gbcpu) - 实现 Game Boy 指令集和功能的 CPU 和外围设备。
- [Game Boy 游戏中的数字化语音](https://youtube.com/watch?v=1lzHfLYzyRM)
- [使用 STM32F4 嗅探 Game Boy 串行流量](https://dhole.github.io/post/gameboy_serial_1/)
- [使用 STM32F4 的虚拟 Game Boy 打印机](https://dhole.github.io/post/gameboy_serial_2/)
- [使用 STM32F4 在 Game Boy 打印机上打印](https://dhole.github.io/post/gameboy_serial_3/)
- [使用 STM32F4 对 Game Boy 中文卡带进行编程](https://dhole.github.io/post/gameboy_cartridge_rw_1/)
- [Pokemon Pocket Computer:](https://tilde.town/~minerobber/techwriteups/pokemonpc.html) - 它是什么以及如何使用它来制作作弊代码。
- [Booting the Game Boy with a custom logo](https://dhole.github.io/post/gameboy_custom_logo/) - 绕过任天堂标志检查。
- 2017 年制作 Game Boy 游戏：“Sheep It Up!”验尸（[第 1 部分](https://www.gamasutra.com/blogs/DoctorLudos/20171207/311143/)，[第 2 部分](https://www.gamasutra.com/blogs/DoctorLudos/20180213/314554/))
- [Nintendo's fake logos](http://fuji.drillspirits.net/?post=87) - 每个墨盒都必须显示真实的徽标才能被视为有效并运行，但显然有些公司设法利用检查系统。
- [liblsdj](https://github.com/stijnfrishert/liblsdj) - 用于与 LSDj 保存格式 (.sav)、歌曲文件 (.lsdsng) 等交互的实用程序库。
- [lsdpatch](https://github.com/jkotlinski/lsdpatch) - 用于修改 LSDj ROM 映像上的样本、字体和调色板的工具。
- [Game Boy video effects](https://github.com/ChaosCabbage/crazy-gameboy-video-experiments) - 一些使用 STAT 中断进行有趣的视频操作的小实验。
- [gbos](https://github.com/ekimekim/gbos) - Game Boy 的基本操作系统。
- [Work Master OS](https://translate.google.com/translate?hl=&sl=ru&tl=en&u=https%3A%2F%2Fweb.archive.org%2Fweb%2F20081226145726%2Fhttp%3A%2F%2Fworkmaster.ru%2Findex.php%3Fp%3D8&sandbox=1) - 俄罗斯多任务操作系统。
- [Game Boy Link 电缆分线板](https://github.com/Palmr/gb-link-cable)
- [GBCartFlasher 固件](https://github.com/Tauwasser/GBCartFlasher)
- [VerilogBoy](https://github.com/zephray/VerilogBoy/) - Game Boy 兼容控制台 Verilog RTL 实现。
- [GBCamcorder](https://github.com/furrtek/GBCamcorder) - 使用 GameBoy 相机盒的低保真便携式录像机。
- [GBCartRead](https://github.com/insidegadgets/GBCartRead) - 从 GameBoy 卡带读取 ROM、读取 RAM 或写入 RAM。
- [GBxCart-RW](https://github.com/insidegadgets/GBxCart-RW) - 用于通过 USB 从 PC 读取游戏 ROM、保存游戏以及恢复 GB、GBC 和 GBA 游戏卡的保存的设备。
- [转储 Super Game Boy 启动 ROM](https://www.its.caltech.edu/~costis/sgb_hack/)
- [sm83-render](https://github.com/msinger/sm83-render) - Blender 中 Game Boy CPU 布局的 3D 模型。
- [visual-sm83](https://iceboy.a-singer.de/visual6502/expert-sm83.html) - 使用 JavaScript 对 Game Boy CPU 核心进行视觉晶体管级模拟，在浏览器中运行。

### 目录

- [相关文件存档](http://gbdev.gg8.se/files/)
- [The Game Boy Archive](https://github.com/gb-archive) - Game Boy 相关软件、硬件和文献库。旨在反映和保存过去三十年的旧的和零碎的贡献。
- [The Game Boy Archive - Salvage](https://github.com/gb-archive/salvage) - 软件历史档案、旧文章、常见问题解答和各种文档。

### 网站

- [devrs.com/gb](http://devrs.com/gb) - 场景的老家：示例、源代码、完整的文档、指南、教程和各种工具。
- [pdroms.de](http://pdroms.de/news/gameboy/) - 游戏男孩发布。
- [Handheld Underground](http://hhug.me) - 未经许可的游戏、有关 Game Boy（hugboy 模拟器之家）的博客文章。


## 关于

### 贡献

查看[贡献指南](CONTRIBUTING.md)。

### 许可证

根据 **GPLv3** 获得许可。
有关详细信息，请参阅[许可证]（许可证）。

### 致谢

感谢该项目的每个贡献者，Jeff Frohwein、Pascal Felber、KOOPa、Pan of Anthrox、GABY、Marat Fayzullin、Paul Robson、BOWSER、neviksti、Martin "nocash" Korth、Nitro2k01、Duo、Chris Antonellis、Michael Hope、当心，乔纳森“梦魇之王”格瓦里亚胡、卡斯滕·索伦斯、辛德·阿莫斯、宅男佐库、GeeBee。

### 赞助商

特别感谢 [DigitalOcean](https://www.digitalocean.com/) 和 [Incube8 Games](https://incube8games.com/) 的朋友们赞助我们 Game Boy 开发社区的开源活动。

