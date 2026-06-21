# 很棒的电子产品 [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> 为电子工程师和爱好者精心准备的精彩资源列表

电子工程 (EE) 是理解、设计和构建电子电路的实践。它通常与电气工程不同，因为它主要处理低功率直流电子电路而不是高功率交流系统，但电子工程和电气工程之间有很多重叠。

实验和构建电子电路也是一种流行的爱好，许多专业资源通常同样适用于业余爱好者，反之亦然。

此列表适用于网站、服务、软件、工具等：您认为电子工程领域很棒的一切。如果您有任何需要添加的内容，请按照 [contributing.md](contributing.md) 中的说明进行操作。

## 内容

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Learning](#learning)
- [Documentation](#documentation)
- [Simulators](#simulators)
- [格柏浏览器](#gerber-viewers)
- [免费 EDA 包](#free-eda-packages)
- [付费 EDA 包](#paid-eda-packages)
- [CAD 专用](#cad-specific)
- [PCB批量服务](#pcb-batching-services)
- [零件搜索引擎](#part-search-engines)
- [项目共享平台](#project-sharing-platforms)
- [库存管理和采购](#inventory-management-and-purchasing)
- [杂项软件项目](#miscellaneous-software-projects)
- [开发板零售商](#development-board-retailers)
- [Blogs](#blogs)
- [Forums](#forums)
- [Podcasts](#podcasts)
- [Videos](#videos)
- [订阅套件服务](#subscription-kit-services)
- [3D 零件模型](#3d-part-models)
- [其他清单](#other-lists)
- [阿拉伯语部分](#arabic-section)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## 学习

### 技术教程
- ["skill" tag on learn.sparkfun.com](https://learn.sparkfun.com/tutorials/tags/skill) - 关于各种 EE 相关技能的各种技术教程。
- [Soldering is Easy](https://mightyohm.com/blog/2011/04/soldering-is-easy-comic-book/) - 漫画书介绍了焊接的基础知识，已被翻译成多种语言。
- [Uses of Different Soldering Iron Tips](https://www.instructables.com/id/Uses-of-Different-Soldering-Iron-Tips/) - 涵盖了所有不同烙铁头的用途。
- [How to design a motherboard for your electronics project](https://www.staycaffeinated.com/2021/02/21/how-to-design-a-motherboard-for-your-project-part-1) - 原理图和 PCB 设计入门教程

### 课程
- [Khan Academy - Electrical Engineering](https://www.khanacademy.org/science/electrical-engineering) - 非营利学习平台，提供电气工程及相关主题的完整课程。
- [NEETS (Navy Electricity and Electronics Training Series)](https://www.fcctests.com/neets/Neets.htm) - 美国海军非常驻培训课程材料。
- [NPTEL](https://nptel.ac.in/course.html) - 拥有所有免费工程课程，包括电子、电气和通信工程。
- [Udemy courses related to Electronics](https://www.udemy.com/topic/electronics/) - Udemy 上提供顶级付费课程。
- [Coursera courses related to Electronics](https://www.coursera.org/courses?query=electronics) - 包括一些在完成后提供电子证书的免费课程。

### 理论
- [Electronics textbook](https://upload.wikimedia.org/wikipedia/commons/e/ee/Electronics.pdf) - 文本涵盖电子电路和元件的设计和功能、直流分析和交流分析。
- [Student Handbook](http://cbseacademic.nic.in/web_material/Curriculum/Vocational/2018/Basic_Electronics_XI.pdf) - 本书使用的语言易于理解，涵盖了演变、基础知识、二极管、整流器、晶体管及其应用、SCR、DIAC 和 TRIAC。
- [Electronics circuits and systems](http://aems.edu.sd/wp-content/uploads/2019/02/Electronics-Circuits-and-Systems-Fourth-Edition-PDFDrive.com-.pdf) - 高质量的免费电子书，涵盖电路和系统下的所有主题，强烈推荐用于概念理解。
- [Lessons In Electric Circuits](https://www.ibiblio.org/kuphaldt/electricCircuits/) - 免费的高质量教科书和工作表，重点是理论、模拟和苏格拉底方法。
- [Ultimate Electronics: Practical Circuit Design and Analysis](https://ultimateelectronicsbook.com/) - 免费在线书籍，包含 CircuitLab 提供的交互式原理图和模拟（正在开发中）。


### 大学课程档案

- [Berkeley EECS](http://inst.eecs.berkeley.edu/classes-eecs.html) - 全面的 EE 和 CS 课程网站档案。
- [Dr. Jacob Baker](http://cmosedu.com) - 课程和教程，内华达大学拉斯维加斯分校教授。
- [博士。亚伯拉罕](https://www.cerc.utexas.edu/~jaa/teaching.html)，[博士。麦克德莫特](http://users.ece.utexas.edu/~mcdermot/)，和[博士。 Valvano](http://users.ece.utexas.edu/~valvano/) - 课程材料，UT Austin 教授

## 文档
- [Inkscape Electric Symbols](https://github.com/upb-lea/Inkscape_electric_Symbols) - Inkscape 的电路绘图符号
- [Tabula](http://tabula.ondata.it/) - 从 pdf 中提取表格数据，对于从数据表中提取引脚表或零件特征非常有用。
- [WebPlotDigitizer](https://automeris.io/WebPlotDigitizer/) - 从绘图、图表等中提取数据，对于从数据表中获取零件性能曲线非常有用。
- [WaveDrom](https://wavedrom.com/) - 从 JSON 描述文件创建波形和时序图。
- [tscircuit](https://tscircuit.com) - 使用 React 进行原理图和 PCB 设计的开源 EDA 包

## 模拟器

### 模拟和混合信号电路模拟器

- [LTspice](https://www.analog.com/en/design-center/design-tools-and-calculators/ltspice-simulator.html) - Linear Technologies 的行业标准免费 SPICE 电路模拟器。另请参阅非官方 [LTwiki](http://ltwiki.org/?title=Main_Page) 和 [Group](https://groups.io/g/LTspice)。
- [ngspice](http://ngspice.sourceforge.net/) - 开源 SPICE 电路模拟器。
- [Circuit JS/Falstad](http://www.falstad.com/circuit/circuitjs.html) - 免费、开源在线模拟器，具有电子流可视化功能（由 Paul Falstad 重写原始 Java 小程序）。
- [EveryCircuit](https://everycircuit.com) - 免费尝试在线、可视化、交互式电路模拟器，以获得更简单的电路。
- [Qucs](http://qucs.sourceforge.net/) - 开源、跨平台、非基于 SPICE 的电路模拟器，具有 S 参数和谐波平衡功能。
- [Qucs-S](https://ra3xdh.github.io/) - 使用 SPICE 进行仿真的 Qucs 开源分支。
- [QucsStudio](http://qucsstudio.de/) - 免费、闭源、仅限 Windows 的 Qucs 分支，具有类似的界面、新引擎和更多功能。
- [Open Circuit Design Software](http://opencircuitdesign.com) - 开源，完整的 EDA 套件芯片设计套件，专注于跟上商业工具的步伐。
- [TINA-TI](http://www.ti.com/tool/TINA-TI) - 专为德州仪器 (TI) 构建的 [DesignSoft-TINA](https://www.tina.com) 与德州仪器 (TI) 型号捆绑在一起。
- [CppSim](https://www.cppsim.com/) - 免费的开源电路模拟器，利用 C++ 语言实现非常快的模拟时间。
- [Scilab with Xcos](https://www.scilab.org/) - MATLAB 的免费开源数值计算替代方案。 Xcos 提供类似于 Simulink 的电气系统建模功能。
- [iCircuit](http://icircuitapp.com/) - 易于使用的电子电路模拟器，其先进的模拟引擎可以处理模拟和数字电路，并具有实时不间断分析功能。
- [Micro-Cap](http://www.spectrum-soft.com/download/download.shtm) - 专业级混合信号模拟器，具有多种交互式模拟类型。
- [GeckoCIRCUITS](https://de.wikipedia.org/wiki/GeckoCircuits) - 开源电力电子电路模拟器。 [GitHub 项目](https://github.com/geckocircuits/GeckoCIRCUITS)。由于网站损坏，直接[下载链接](http://gecko-simulations.com/GeckoCIRCUITS/GeckoCIRCUITS.zip)。
- [Proteus](https://www.labcenter.com/) - PCB 设计和电路模拟器软件。

### Verilog HDL 模拟器

- [Verilator](https://www.veripool.org/wiki/verilator) - 免费、开源 Verilog 编译器。测试平台采用 C++ 或 SystemC。非常快，但仅限于 2 状态、基于周期的模拟和可综合代码。
- [Icarus Verilog](http://iverilog.icarus.com/) - 免费、开源的 verilog 解释器。测试平台采用行为 verilog。模拟是 4 状态且基于事件的。

## 格柏浏览器

### 在线
- [Tracespace Viewer](https://tracespace.io/) - Gerber 查看器可让您检查各个层以及电路板预览。
- [Gerblook](https://www.gerblook.org/) - 由 Gerbv 提供支持的在线 Gerber 查看器。
- [Mayhew Labs 3dpcb](http://mayhewlabs.com/3dpcb) - 3D Gerber 查看器。
- [CircuitPeople](https://circuitpeople.com) - Gerbers 的简洁 2D 图层查看器，无需过多处理。
- [Stackrate Viewer](https://stackrate.de/viewer/) - 易于使用的在线 Gerber 查看器，带有跟踪悬停和测量工具。

### 可安装
- [Gerbv](http://gerbv.geda-project.org/) - 适用于 Linux 和 BSD 的优秀 Gerber 查看器。
- [KiCAD Gerbview](https://kicad.org/) - KiCAD gerber 查看器。
- [GC-Prevue](http://www.graphicode.com/GC-Prevue_Gerber_Viewer) - 商业版与免费版。可以比 Gerbv 和 KiCAD 更好地处理一些 gerber。
- [ZofZPCB](https://www.zofzpcb.com/) - 免费 3D Gerber 查看器。

## 免费 EDA 包
- [KiCad](https://kicad.org/) - 开源 EDA 包，带有推推路由器、差分对等。
- [Eagle](https://www.autodesk.com/products/eagle/overview) - 由于它是（电路板尺寸受限）免费版本，因此成为最受欢迎的 EDA 软件包之一。
- [DesignSpark PCB](https://www.rs-online.com/designspark/pcb-software) - 无限制的免费 EDA 软件包，由 RS Components 赞助。
- [Altium CircuitMaker](https://circuitmaker.com/) - go to pro 软件制造商提供的免费软件包。
- [gEDA](http://geda-project.org) - 另一个开源包，适合喜欢脚本和 makefile、仅限 Linux 和 BSD 的人。
- [DipTrace](https://diptrace.com) - 优质原理图捕获和 PCB 设计软件（仅限引脚和信号层）免费版本。
- [LibrePCB](https://librepcb.org/) - 一款适合所有人的全新、强大且直观的 EDA 工具，跨平台和 GNU GPLv3。
- [Horizon EDA](https://github.com/horizon-eda/horizon) - 一款免费开源的EDA工具，注重快捷操作。
- [EasyEDA](https://easyeda.com/) - 易于使用基于浏览器和跨平台的应用程序版本。将 [LCSC](https://www.lcsc.com/products) 和 [JLCPCB](https://jlcpcb.com/parts) 组件目录与 3D 模型集成。

## 付费 EDA 包
- [Altium](https://www.altium.com/) - PCB 设计软件和工具。
- [Proteus](https://www.labcenter.com/) - PCB 设计和电路模拟器软件。

## CAD 专用

### 凯德
- [Xesscorp 的 KiCad 3rd 方工具列表](https://github.com/xesscorp/kicad-3rd-party-tools)
- [Contextual Electronics' Shine on You Crazy KiCad](https://contextualelectronics.com/courses/shine-on-you-crazy-kicad/) - 初学者视频教程可让您尽快了解制造好的电路板。
- [Contextual Electronics' Getting to Blinky Tutorial](https://www.youtube.com/playlist?list=PLy2022BX6Eso532xqrUxDT1u2p4VVsg-q) - 更全面的初级到中级视频教程。
- [KiCad.info Forums](https://forum.kicad.info) - 用户讨论和帮助论坛。
- [Keyboard PCB Guide](https://github.com/ruiqimao/keyboard-pcb-guide) - 全面的书面教程，带您完成键盘 PCB 的创建。
- [Cheatsheet](https://silica.io/wp-content/uploads/2018/06/kicad-cheatsheet.pdf)（也[横向](https://silica.io/wp-content/uploads/2018/06/kicad-cheatsheet-landscape.pdf)） - 简短的 PDF，介绍了最常见操作的菜单和键盘快捷键。
- [Footprint Collection](https://github.com/kitspace/kicad_footprints) - 在线提供的所有 KiCad 足迹的集合以及一些用于管理它们的脚本。
- [InteractiveHtmlBom](https://github.com/openscopeproject/InteractiveHtmlBom) - 用于手动拾取和放置的 html BOM 生成工具。
- [KiBot](https://github.com/INTI-CMNB/KiBot) - 轻松、可重复且最重要的是可脚本化地为您的 KiCad 项目生成制造和文档文件。

### 鹰
- [每个人都应该知道的 ULP 列表](https://www.element14.com/community/community/eagle/blog/2015/01/19/eagle-ulps-every-user-should-know)
- [Adafruit Eagle 图书馆](https://github.com/adafruit/Adafruit-Eagle-Library)
- [SparkFun Electronics Eagle 图书馆](https://github.com/sparkfun/SparkFun-Eagle-Libraries)

### 阿尔蒂姆
- [Altium Designer Libraries](https://www.altium.com/documentation/other_installers#!libraries) - 来自不同制造商的电子元件的`.IntLib`和`.PcbLib`。


## PCB批量服务
- [PCBShopper](https://pcbshopper.com/) - 为相当多不同的 PCB 批量和组装服务提供比较服务。
- [OSH Park](https://oshpark.com) - 低成本 PCB 批量服务，提供带有标志性紫色丝印的高品质电路板。
- [Aisler](https://aisler.net) - 价格实惠的优质电路板，在欧洲（德国）制造并发货。
- [Dirty PCBs](http://dirtypcbs.com/store/pcbs) - 以其“脏”品质而自豪的低成本 PCB 批量服务。
- [JLCPCB](https://jlcpcb.com/) - 低成本 PCB 批量服务与内部低成本 SMT 服务。
- [PCBWay](https://www.pcbway.com/) - 低成本 PCB 批量服务，包括 PCBA、CNC 和 3D 打印服务。

## 零件搜索引擎
- [Octopart](https://octopart.com) - 可能是最知名的零件搜索引擎。
- [Findchips](https://www.findchips.com/) - 从供应框架中搜索零件。
- [Parts.io](https://parts.io/) - Supply Frame 的另一个搜索引擎，旨在发现新零件。
- [Electronic Component Search Engine](https://componentsearchengine.com/) - 免费访问原理图符号、PCB 封装和 3D 模型。
- [Yoo Need One - SMD Marking Database](https://smd.yooneed.one/) - 表面贴装器件 (SMD) 元件标记数据库。
- [JLCSearch](https://jlcsearch.tscircuit.com) - 查找不同类别最流行的库存 JLC 组件


## 项目共享平台
- [Kitspace](https://kitspace.org) - 项目共享网站可帮助您购买零件和重建项目。真正开源并由您开发。
- [Hackaday.io](https://hackaday.io) - 用于分享流行博客项目的社交网站。
- [Hackster.io](https://www.hackster.io/) - 另一个用于分享项目的社交网站。按平台、主题和产品组织良好。
- [InventHub](https://inventhub.io/) - 基于 Git 的硬件开发项目托管和协作平台。
- [CADLAB](https://cadlab.io/) - 另一个基于 Git 的硬件开发项目托管和协作平台。
- [Eyrie](https://eyrie.io) - 用于在线查看 Eagle 和 KiCad 设计。
- [WikiFactory](https://wikifactory.com/) - 用于产品开发的项目托管和协作平台。过滤“电子”以获取更多电子相关项目。
- [Instructables](https://www.instructables.com/) - 用于分享项目的社交网站。过滤“电路”以获取更多电子相关项目。


## 库存管理和采购
- [PartsBox](https://partsbox.io) - 通过良好的用户界面和 Octopart 集成来管理零件库存的 Web 服务。
- [Part-DB](https://github.com/Part-DB/Part-DB) - 另一个开源 Web 服务，用于通过权限系统和良好的条形码生成器管理零件库存。
- [InvenTree](https://inventree.org) - 用于通过参数搜索、广泛的 API 和插件系统管理零件库存的开源 Web 服务
- 
## 杂项软件项目
- [SnapEDA](https://www.snapeda.com) - 带有免费符号和封装的零件库。 （兼容 Eagle、KiCad、Altium、OrCad、Allegro 等）
- [Language PCB](https://github.com/Alhadis/language-pcb) - 各种 PCB 格式的语法突出显示。
- [NinjaCalc](https://gbmhunter.github.io/NinjaCalc/) - 嵌入式工程计算器工具箱，可轻松进行计算。
- [Saturn PCB Design Toolkit](https://saturnpcb.com/saturn-pcb-toolkit/) - Saturn PCB 工具包是您能找到的用于 PCB 相关计算的最佳免费软件资源。
- [KiCanvas](https://kicanvas.org/) - KiCad 原理图和电路板的开源在线查看器。

## 开发板零售商
- [Sparkfun](https://www.sparkfun.com/) - 开源电子开发板和其他设备和材料的零售商和设计商，并提供优秀的随附教程。
- [Adafruit](https://www.adafruit.com/) - 另一家零售商和设计师提供出色的选择和教程。
- [Tindie](https://www.tindie.com) - 电子产品制造商小批量销售自己设计的市场。

## 博客
- [Hackaday](https://hackaday.com) - 可能是最受欢迎的涵盖电子和硬件黑客的博客，由全体作者组成。
- [bunniestudios.com](https://www.bunniestudios.com) - Andrew 'Bunnie' Huang 涵盖硬件黑客、开放硬件、制造等领域。
- [Bald Engineer](https://www.baldengineer.com) - James Lewis 撰写的有关电子和嵌入式软件的项目日志、教程和文章。
- [Rheingold Heavy](https://rheingoldheavy.com) - 更多关于电子和嵌入式软件的项目日志、教程和文章，这些由 Dan Hienzsch 撰写。
- [Hackster.io](https://www.hackster.io/news) - 另一个涉及电子产品的博客。
- [Dangerous Prototypes](http://dangerousprototypes.com/blog/) - 有关开源硬件项目和有趣的应用笔记的博客。
- [N-O-D-E](https://n-o-d-e.net/) - 有关 DIY 电子产品、硬件和技术的博客。


## 论坛

### 讨论
- [EEVBlog forum](https://www.eevblog.com/forum/) - 可能是讨论电子工程主题的最大、最活跃的论坛。
- [/r/Electronics](https://www.reddit.com/r/Electronics/) 和 [/r/ECE](https://www.reddit.com/r/ECE/) 是 EE 主题的两个最活跃的 Reddit 子版块。

### 帮助
- [/r/askelectronics](https://www.reddit.com/r/AskElectronics/) - Reddit 子版块致力于为电子主题提供帮助。
- [Electronics Stack Exchange](https://electronics.stackexchange.com) - 在流行的 Stack Overflow 服务上运行的电子产品问答网站。
- [EEVBlog beginners forum](https://www.eevblog.com/forum/beginners/) - 适合初学者提问的好地方，EEVblog 上的其他子论坛应该适合更高级主题的问题。


## 播客
- [The Amp Hour](https://theamphour.com/) - 与 Chris Gammel 和 Dave Jones (EEVBlog) 经常与嘉宾即兴谈论电子产品
- [Embedded.fm](https://embedded.fm/) - Christopher 和 Elecia White 经常与来宾讨论嵌入式系统开发等内容。
- [The Spark Gap Podcast](http://thesparkgap.net) - 每集涵盖一个特定的 EE 主题，有时与嘉宾一起。
- [MacroFab Engineering Podcast](https://macrofab.com/blog/podcast/) - 来自 MacroFab 的 Parker 和 Stephen 讨论 EE 主题和行业新闻的每周播客。
- [The Engineering Commons Podcast](http://theengineeringcommons.com/) - 涵盖从机械到电气的一般工程主题。


## 视频
- [EEVblog](https://www.youtube.com/user/EEVblog) - 最早、最成功的 YouTube 频道之一，戴夫·琼斯 (Dave Jones) 在这里进行拆解、教程等。
- [BigClive](http://bigclive.com) - [YouTube 频道](https://www.youtube.com/user/bigclivedotcom) 有关拆解（包括危险产品）、电路逆向工程和教程的内容。
- [ElectroBOOM](https://www.youtube.com/user/msadaghd) - YouTube 频道通过大量喜剧来揭穿和解释 EE 主题。
- [Micah Scott](https://www.youtube.com/user/micahjd) - 以创造性方式逆向工程和重新利用消费电子硬件的视频日志。
- [Afrotechmods](https://www.youtube.com/user/afrotechmods) - 电子项目教程，通常也适合初学者。
- [The Signal Path](https://www.youtube.com/user/TheSignalPathBlog) - 对实验室设备和原型产品进行非常深入的拆卸、维修和审查。
- [w2aew](https://www.youtube.com/channel/UCiqd3GLTluk2s_IBt7p_LjA) - 关于基本和复杂模拟硬件的优秀教程。
- [Mr. Carlson's Lab](https://www.youtube.com/user/MrCarlsonsLab) - 拆卸、维修和修复，重点是经典电子设备。
- [GreatScott](https://www.youtube.com/user/greatscottlab) - 电子教程、项目和操作方法。
- [Julian Ilett](https://www.youtube.com/user/julius256) - 购买他能找到的最便宜的电子模块，并尝试用它们做有用的事情。
- [MikesElectricStuff](https://www.youtube.com/channel/UCcs0ZkP_as4PpHDhFcmCHyA) - 拆解、大型照明项目、X 射线等等。
- [Ben Eater](https://www.youtube.com/playlist?list=PLowKtXNTBypGqImE405J2565dvjafglHU) - 关于在面包板上构建 8 位计算机的系列视频，并对所有子电路进行了精彩的解释。
- [Robert Feranec](https://www.youtube.com/user/matarofe) - 100 多个硬件设计提示和技巧。有关原理图设计和 PCB 布局的视频。
- [Strange Parts](https://strangeparts.com) - [YouTube 频道](https://www.youtube.com/channel/UCO8DQrSp5yEP937qNqTooOw) 有关电子、制造、制作、环球旅行、在中国生活和制作的内容。
- [Analog Circuit Design](https://youtube.com/playlist?list=PLc7Gz02Znph-c2-ssFpRrzYwbzplXfXUT) - 模拟电路设计由加州理工学院的 Ali Hajimiri 教授完成。
## 订阅套件服务
- [AdaBox](https://www.adafruit.com/adabox/) - 精选 Adafruit 产品、独特收藏品和独家折扣。全部按季度交付。
- [HackerBoxes](https://hackerboxes.com/) - 每月惊喜盒，其中包括项目、组件、模块和工具。

## 3D 零件模型
- [GrabCad](https://grabcad.com/library/electronic-components-1) - 社区支持的 3D 模型数据库，包含大量电子元件模型。
- [3D ContentCentral](https://www.3dcontentcentral.com) - 专门提供零件 3D 模型的网站（需要登录）。

## 其他清单
- [PwnKitteh/InsanelyCheapElectronics](https://github.com/PwnKitteh/InsanelyCheapElectronics) - 来自中国的廉价电子产品列表，您可以在您的项目中使用。
- [PCB/EDA software list on the EEVblog forums](https://www.eevblog.com/forum/eda/pcbeda-software-list/) - 所有可用软件工具的更全面的列表。
- [intajay/open-electronics](https://github.com/intajay/open-electronics) - 另一个 GitHub 列表：电子爱好者和硬件黑客的资源。
- [Vitorian/awesome-fpga](https://github.com/Vitorian/awesome-fpga) - 很棒的 FPGA 资源列表。
- [cajt/list_of_robot_electronics](https://github.com/cajt/list_of_robot_electronics) - 机器人电子产品的资源、项目和产品的 GitHub 列表。
- [embedded-boston/awesome-embedded-systems](https://github.com/embedded-boston/awesome-embedded-systems) - 很棒的嵌入式编程资源列表。
- [TCAD Central](https://tcadcentral.com/Software.html) - DEVSIM 制造商提供的技术 CAD (TCAD) 软件和资源列表。
- [Awesome Lattice FPGAs](https://github.com/kelu124/awesome-latticeFPGAs) - 精选的优秀开源 FPGA 板列表。
- [TM90/awesome-hwd-tools](https://github.com/TM90/awesome-hwd-tools) - 精选的硬件设计工具列表，重点关注芯片设计。
- [delftopenhardware/awesome-open-hardware](https://github.com/delftopenhardware/awesome-open-hardware) - 对于制作和学习开源硬件项目有帮助的项目。
- [upb-lea/awesome-open-source-power-electronics](https://github.com/upb-lea/awesome-open-source-power-electronics) - 专门针对电力电子的开源软件列表。

## 阿拉伯语部分
 - [Complete EE Course](https://youtube.com/playlist?list=PLww54WQ2wa5rOJ7FcXxi-CMNgmpybv7ei&si=4Whr8h-_9kGdUN3_) - 详细信息
 - [Complete Digital Electronics Course](https://youtube.com/playlist?list=PLww54WQ2wa5obq6IbRbIiql8oHaTUp3T_&si=I4mqjy3JUZ8xmElT) - 德鲁克·拉德鲁尼·阿塔·拉克米尔
 - [professional Electronics Design](https://youtube.com/playlist?list=PLww54WQ2wa5oKEhE_D3UVbKWwml8o8_Fu&si=BF213_MSJwSiyvIV) - 德鲁拉·阿塔图尔尼·阿塔图尔
 - [professional PCB Design](https://www.youtube.com/playlist?list=PLww54WQ2wa5pBm96kQTkqAyMXn9F4Q0i9) - 印刷电路板 (PCB)


