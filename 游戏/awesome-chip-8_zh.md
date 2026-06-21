# 很棒的 CHIP-8 [![Awesome](https://awesome.re/badge-flat.svg)](https://awesome.re)

[<img src="c8.png"align="right"width="100">](https://chip-8.github.io)

> 70 年代的虚拟电脑游戏机

精选的 CHIP-8 资源、工具、文档、相关项目和开源 ROM 列表。

[CHIP-8](https://en.wikipedia.org/wiki/CHIP-8) 创建于 1977 年，是最初的幻想控制台。它最初是为了简化 COSMAC VIP 套件计算机的游戏开发而设计的，几十年来它经历了多次复兴，推出了令人兴奋的新平台。如今，创建 CHIP-8 实现对于任何有兴趣了解仿真的人来说都是必经之路。

要向此列表添加内容，请参阅[贡献指南](CONTRIBUTING.md)。

## 内容

* [Community](#community)
* [Documentation](#documentation)
* [模拟器/解释器开发](#emulatorinterpreter-development)
  * [Testing](#testing)
* [Emulators/interpreters](#emulatorsinterpreters)
* [软件开发](#software-development)
  * [Tools](#tools)
  * [指南和片段](#guides-and-snippets)
  * [Postmortems](#postmortems)
* [Games](#games)

## 社区

* [COSMAC Elf Group](https://groups.io/g/cosmacelf) - 用于讨论 COSMAC Elf 以及其他与 RCA 1802 相关的内容的小组，包括 COSMAC VIP 和 CHIP-8。
* [#chip8 channel on the Emulation Development Discord server](https://discordapp.com/invite/Gf7cP3w) - 讨论 CHIP-8 仿真器/解释器开发的聊天室。
* [OctoJam](http://octojam.com/) - 每年十月都会举办以章鱼为中心的游戏盛会。

## 文档

* [Mastering CHIP-8](https://github.com/mattmikolay/chip-8/wiki/Mastering-CHIP%E2%80%908) - CHIP-8 指令集的深入概述。
* [CHIP-8 Instruction Set](http://johnearnest.github.io/Octo/docs/chip8ref.pdf) - CHIP-8 指令的快速备忘单。
* [CHIP-8 Instruction Set](https://github.com/mattmikolay/chip-8/wiki/CHIP%E2%80%908-Instruction-Set) - 综合指令/操作码表。
* [CHIP-8 Technical Reference](https://github.com/mattmikolay/chip-8/wiki/CHIP%E2%80%908-Technical-Reference) - CHIP-8 解释器的工作原理概述。
* [CHIP-8 Extensions Reference](https://github.com/mattmikolay/chip-8/wiki/CHIP%E2%80%908-Extensions-Reference) - CHIP-8 变体和扩展的列表。
* [Chip-8 on the COSMAC VIP](https://laurencescotford.com/chip-8-on-the-cosmac-vip-index/) - 对 COSMAC VIP 上原版 CHIP-8 解释器的深入拆解和分析。
* [HP48-Superchip](https://github.com/Chromatophore/HP48-Superchip) - 深入了解 HP48 计算器的 CHIP48 和 Super-CHIP，并进行修改以使它们兼容 CHIP-8。
* [Octo Extensions](http://johnearnest.github.io/Octo/docs/XO-ChipSpecification.html) - Octo 的 XO-CHIP 扩展规范。

## 模拟器/解释器开发

* [How to write an emulator (CHIP-8 interpreter)](http://www.multigesture.net/articles/how-to-write-an-emulator-chip-8-interpreter/) - 使用 C/C++ 开发 CHIP-8 解释器的指南。
* [Emulator 101: CHIP-8](http://www.emulator101.com/introduction-to-chip-8.html) - 用 C 语言开发 CHIP-8 反汇编器和解释器的指南。
* [Chip 8 Instruction Scheduling and Frequency](https://jackson-s.me/2019/07/13/Chip-8-Instruction-Scheduling-and-Frequency.html) - COSMAC VIP 上 CHIP-8 指令的计时。
* [High-level guide to making a CHIP-8 emulator](https://tobiasvl.github.io/blog/write-a-chip-8-emulator/) - 开发 CHIP-8 解释器的指南，无需代码。

### 测试

* [chip8-test-rom](https://github.com/corax89/chip8-test-rom) - corax89 的 CHIP-8 测试程序，用于测试大多数指令的正确（符合 Super-CHIP）行为。
* [CHIP-8 test suite](https://github.com/Timendus/chip8-test-suite) - Timendus 的测试集，包括 corax89 测试 rom 的改进版本、标志行为测试以及 CHIP-8 / Super-CHIP / XO-CHIP 怪癖测试。
* [Delay timer test](https://github.com/mattmikolay/chip-8/tree/master/delaytimer) - 检查延迟计时器行为的测试程序。
* [Random number test](https://github.com/mattmikolay/chip-8/tree/master/randomnumber) - 检查随机数生成的扩展和掩码的测试程序。

## 模拟器/解释器

* [Octo](http://johnearnest.github.io/Octo/) - 用于开发 CHIP-8、Super-CHIP 和 XO-Chip 游戏的 IDE。
* [Emma02](https://www.emma02.hobby-site.com/) - 适用于许多旧微型计算机的模拟器，包括 COSMAC VIP、Telmac 1800 和 ETI 660，它们运行早期的 CHIP-8 解释器（包含在模拟器中）。
* [Super-Chip8x](https://github.com/Ersanio/Super-Chip8x) - SNES 的 CHIP-8 模拟器。
* [CHIP-8 console on FPGA](https://github.com/pwmarcz/fpga-chip8) - 适用于 TinyFPGA BX 芯片的 CHIP-8 仿真器。
* [Vinegar](http://benryves.com/bin/vinegar/) - 用于 TI-83 (Plus) 计算器的 CHIP-8/Super-CHIP 解释器。
* [LowResNX](https://lowresnx.inutilis.com/topic.php?id=1648) - CHIP-8 解释器和调试器在另一个复古幻想控制台中以 BASIC 编程。

## 软件开发

### 工具

* [Octo](http://github.com/johnearnest/Octo/) - 适用于 CHIP-8、Super-CHIP 和 XO-CHIP 的高级汇编器，配有测试程序的环境以及用于共享您的作品的工具。
* [wernsey chip8](https://github.com/wernsey/chip8) - CHIP-8 汇编器/反汇编器。
* [EZ-Bake Animator](http://beyondloom.com/tools/ezbake.html) - 一种创建异或动画的图形准备工具。
* [EZ-Writer](http://beyondloom.com/tools/ezwriter.html) - 用于将文本转换为 CHIP-8 精灵的工具。
* [EZ-Pack](http://beyondloom.com/tools/ezpack.html) - 图像切片/重新调色工具。
* [Chipify](http://johnearnest.github.io/Octo/tools/Chipify/) - 将单通道 WAV 音频过滤并编码为 XO-CHIP 音频的脚本。
* [octofont](https://github.com/jdeeny/octofont/) - 将 TrueType (ttf) 字体转换为 CHIP-8 的 Octo 代码。

### 指南和片段

* [Octo manual](https://johnearnest.github.io/Octo/docs/Manual.html) - Octo 的手册。
* [A Beginner's Guide to Programming with Chip8](http://johnearnest.github.io/Octo/docs/BeginnersGuide.html) - Octo 中 CHIP-8 编程的介绍性指南。
* [An Intermediate Guide to Game Development with Chip8](http://johnearnest.github.io/Octo/docs/IntermediateGuide.html) - 在 Octo 中为 CHIP-8 重制 Atari 2600 游戏“Outlaw”。
* [Chip8 Programming Techniques](http://johnearnest.github.io/Octo/docs/Chip8%20Programming.html) - CHIP-8 的许多不同编程技巧。
* [Octo Metaprogramming Cookbook](http://johnearnest.github.io/Octo/docs/MetaProgramming.html) - 如何使用 Octo 的汇编指令进行元编程。
* [Mastering SuperChip](http://johnearnest.github.io/Octo/docs/SuperChip.html) - 如何使游戏兼容CHIP-8和Super-CHIP，以及一些Super-CHIP的具体技术。
* [Adventures in Sorting](https://johnearnest.github.io/Octo/docs/Sorting.html) - 在 Octo 中为 CHIP-8 实现高效的排序算法。
* [chip8-multiply](https://github.com/jdeeny/chip8-multiply) - CHIP-8 的乘法例程，用 Octo 编写。

### 事后剖析

由开发人员撰写的详细说明特定游戏开发情况的事后分析。

* [外星人伊蒂的内心](http://johnearnest.github.io/Octo/docs/EatyTheAlien.html)
* [章鱼尸检](http://www.awfuljams.com/octojam-ii/games/octopeg)
* [CosmacCalc：COSMAC VIP 在电子表格历史中的地位](https://abitoutofplace.wordpress.com/2015/05/02/cosmaccalc-the-cosmac-vip-s-place-in-spreadsheet-history/)
* [洞穴探险家内部](http://johnearnest.github.io/Octo/docs/CaveExplorer.html)
* [黑彩虹里面](http://johnearnest.github.io/Octo/docs/BlackRainbow.html)
* [事后剖析：迷你熄灯](https://tobiasvl.itch.io/mini-lights-out/devlog/102679/postmortem-mini-lights-out)

## 游戏

* [CHIP-8 Archive](https://johnearnest.github.io/chip8Archive/) - 公共领域 (CC0) 游戏的集合，全部可以在线玩。
* [A collection of CHIP-8 programs and documentation](https://github.com/mattmikolay/chip-8) - Matt Mikolay 的游戏、程序和文档。
