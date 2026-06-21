# 很棒的 J2ME [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[<img src="j2me-logo.jpg"align="right"width="100">](https://www.oracle.com/java/technologies/javameoverview.html)


> 关于 Java 平台微型版本的精彩列表[(J2ME)](https://en.wikipedia.org/wiki/Java_Platform,_Micro_Edition)。文档、学术论文、教程、社区、IDE、SDK、模拟器、应用程序、视频游戏。 J2ME 是专为老式键盘电话和 PDA 设计的 Java 规范。 MIDP 构建于 CLDC 之上，用于创建 Midlet，其扩展名为“.jad”或“.jar”，可在老式键盘手机、Symbian 和 PDA 等平台上运行。 Java ME SDK 3.4 之前支持 MIDP。

<!--lint disable double-link-->
请给它一颗星（⭐），以提高人们对 J2ME 社区的认识，并支持该项目的发展。在<a href="https://hstsethi.vercel.app/posts/programming/awesome-j2me">这篇博文</a>中了解 Awesome J2ME 的介绍、设置过程和历史。另请查看 [Awesome Symbian](https://github.com/hstsethi/awesome-symbian)。

<!--lint disable double-link-->
很荣幸能够在 [Awesome](https://github.com/sindresorhus/awesome)、[Hackclub](https://retrospect.hackclub.com/j2me)、[Awesome Java](https://github.com/akullpp/awesome-java) 等中亮相。

## 内容

- [Communities](#communities)
- [Development](#development)
   - [IDEs](#ides)
   - [SDKs](#sdks)
- [Emulators](#emulators)
- [Finance](#finance)
- [Hardware](#hardware)
- [原生软件](#native-software)
   - [Apps](#apps)
   - [电子游戏](#video-games)
- [相关项目](#related-projects)
- [逆向工程](#reverse-engineering)
   - [Decompilers](#decompilers)
- [Tutorials](#tutorials)
    - [学术文章](#academic-articles)



## 社区

- [HackClub Retrospect J2ME](https://retrospect.hackclub.com/j2me) - Hackclub 举办的 J2ME 开发竞赛。在其资源部分中包含 Awesome J2ME。
- [Kahvibreak Discord](https://discord.gg/8TgbHAG) - Discord 社区专注于保存 J2ME 游戏。
- [Ketai Wiki](https://keitaiwiki.com/wiki/KeitaiWiki) - Wiki 致力于对日本功能手机 (keitai)（日本发布的 Android/iPhone 之前的移动设备）中的游戏进行编目。
- [r/J2MEGaming](https://reddit.com/r/j2megaming) - J2ME、Symbian 和相关平台的 Reddit 社区。



## 发展

- [Cibyl](https://github.com/SimonKagstrom/cibyl) - 在 J2ME 手机上编译和运行用 C、Objective-C、C++ 和可能的 Fortran 编写的程序的环境。
- [NN JSON](https://github.com/shinovon/NNJSON) - CLDC 1.1 的 JSON 解析器。
- [NN JSON CLDC 1.0](https://github.com/gtrxAC/discord-j2me/tree/main/src/cc/nnproject/json) - CLDC 1.0 的 NN JSON 的修改版本。
- [J2ME Game Script Engine](https://j2megamescript.sourceforge.net/) - 一个轻量级脚本解释器，用于构建灵活的 J2ME 游戏，具有类似 BASIC 的脚本语言。运行在J2SE/J2ME/Win C++平台上；非常适合游戏快速原型设计和定制。
- [J2ME Gradle template](https://gitea.bedohswe.eu.org/pixtaded/j2me-hello-gradle) - 使用 Microemulator 进行 J2ME 开发的 Gradle 模板。
- [Lightweight User Interface Toolkit(LWUIT)](https://en.wikipedia.org/wiki/Lightweight_User_Interface_Toolkit) - 受 Swing 启发的 J2ME 小部件工具包。

### IDE

- [Eclipse](https://archive.eclipse.org/eclipse/downloads) - Eclipse IDE 所有版本的存档。
- [NetBeans 6.1](https://archive.org/download/netbeans-olds/6.1) - Mobility-pack、普通NetBeans和Java-ME SDK，这些都是搭建MIDP开发环境所必需的。

### 软件开发工具包

- [Extra Transit Mobile Interaction Suite](http://web.archive.org/web/20070210202710/http://www.extransit.com) - J2ME 的 IDE 和 SDK 专门用于开发基于 Internet 的应用程序。
- [Hecl](https://www.hecl.org) - 一种基于Java的移动脚本语言，能够在基于J2ME的设备上运行。
- [J2ME Polish](https://github.com/Enough-Software/j2mepolish) - 用于 J2ME 的基于 Ant 的开源构建工具，支持包括 Blackberry 和 Symbian 在内的多个平台的构建。
- [MBooster](https://web.archive.org/web/20070314004015/http://innaworks.com/mBooster.html) - .jar 文件的优化套件。压缩图像、音频、zip 文件并优化 API 调用。
- [Micro Code](https://web.archive.org/web/20061225061546/http://j2me-device-db.sourceforge.net/pmwiki/index.php?n=Main.HomePage) - J2ME 的跨设备开发框架。支持超过 100 种设备。
- [Sony Ericsson](https://archive.org/details/semc_java_me_cldc_sdk.2-5-0-6) - 支持各种索尼爱立信设备。也可以运行 Mascot 胶囊软件。
- [Soap ME](https://dl.acm.org/doi/abs/10.1145/1462802.1462805) - 支持动态开发的符合 SOAP 规范的 Web 服务容器。
- [Sun Java Me SDK](https://www.oracle.com/java/technologies/javame-sdk/java-me-sdk-v30.html) [mirror](https://archive.org/details/sun_java_me_sdk-3_0-win) - 集成 CLDC/MIDP 开发的 WTK 的后继者。
- [Sun WTK](https://www.oracle.com/java/technologies/java-archive-downloads-javame-downloads.html#sun_java_wireless_toolkit-2.5.2_01) - Sun 的官方 J2ME SDK。



## 模拟器

- [FreeJ2ME](https://github.com/hex007/freej2me) - 带有 LibRetro、AWT 和 SDL2 前端的 J2ME 模拟器。
- [FreeJ2ME Plus](https://github.com/TASEmulators/freej2me-plus) - FreeJ2ME 的活跃分支。
- [J2ME Loader](https://github.com/nikita36078/J2ME-Loader) - 适用于 Android 的 J2ME 模拟器。
- [JL Mod](https://github.com/woesss/JL-Mod) - J2ME 加载器的分支，支持 Mascotcapsule v3。
- [JS2 J2ME](https://github.com/szatkus/js2me) - 适用于 Firefox 操作系统的 J2ME 模拟器。
- [KEmulator nnmod](https://github.com/shinovon/KEmulator) - Java 中的开源 J2ME 模拟器，基于 KEmulator 1.0.3。
- [PSPKvm](https://sourceforge.net/projects/pspkvm/) - PSP 的 J2ME 模拟器。
- [SquirrelJME](https://github.com/squirreljme/squirreljme) - 适用于嵌入式和物联网设备的 Java ME 8 虚拟机。

## 金融

- [Glu Mobile 10-K archive](https://www.sec.gov/edgar/search/#/dateRange=all&category=custom&entityName=0001366246&forms=10-K) - Glu Mobile 10-K 从 IPO（2007 年）到收购（2021 年）的档案。包括按发行和地区划分的收入明细、管理层评论、游戏组合等。
- [UPI 123PAY](https://www.npci.org.in/what-we-do/upi-123pay/product-overview) - NPCI 针对功能手机的官方统一支付接口 (UPI) 支付解决方案。不需要互联网。仅在印度受支持。

## 硬件

- [Mobile Phone Museum](https://mobilephonemuseum.com/about) - 注册手机慈善机构和博物馆。目前拥有250多个品牌2800多个型号。


## 原生软件

### 应用程序

- [Discord J2ME](https://github.com/gtrxAC/discord-j2me) - J2ME 的非官方 Discord 客户端。利用代理服务器进行 HTTP 和网关连接。
- [Hotpants](https://github.com/baumschubser/hotpants/) - HOTP/TOTP 客户端。
- [J2ME Emu Software](https://archive.org/details/j2me-emuSoftware) - 可执行文件，在 J2ME 上运行的各种模拟器的源代码。
- [Jtube](https://github.com/shinovon/JTube) - 基于 Invidious API 的 YouTube 客户端。
- [MeBoy](http://arktos.se/meboy) - 支持模拟 GBC 的声音、颜色和保存状态。
- [Telegram Micro](https://github.com/faissaloo/telegram-micro) - 电报客户端。
- [VK4ME](https://github.com/VK4ME/client) - 俄罗斯社交网络 VK 的非官方客户端，适用于支持 CLDC 1.1 和 MIDP 2.0 的设备。
- [Opera FTP Archive](https://ftp.opera.com/pub/opera) - 适用于所有支持平台的各个版本 Opera 浏览器的官方 FTP 存档。
- [Pocket Gopher](https://github.com/felixp7/pocket-gopher) - J2ME 的开源 Gopher 和 Gopher+ 客户端。

### 电子游戏

- [Gravity Defied CPP](https://github.com/rgimad/gravity_defied_cpp) - C++、同名 J2ME 游戏的 SDL2 移植。
- [Kahvibreak](https://bluemaxima.org/kahvibreak) - J2ME 游戏合集。
- [Moby Games](https://www.mobygames.com/platform/j2me) - J2ME 游戏数据库以及官方商店的链接。
- [The "New" J2ME software archive](https://archive.org/details/96x65pixels_j2me) - 74GB+，J2ME 游戏的排序集合。
- [Nowhere Dialogues](https://gist.github.com/hstsethi/d4ef0c9f0710e5b713d1beb2ff93a1ce) - Dialogues from a Nowhere，一款 2007 年 J2ME 游戏，角色名称经过逆向工程。
- [J2ME Games at MyAbandonware](https://www.myabandonware.com/browse/platform/j2me) - 废弃 J2ME 游戏的精选目录，可直接下载。
- [J2ME Games Speedruns](https://www.speedrun.com/games?platform=nzel5r6q) - 与 J2ME 游戏相关的所有速通游戏列表以及指南、讨论和屏幕录制。

## 相关项目

- [Awesome Symbian](https://github.com/hstsethi/awesome-symbian) - 这是一份关于 Symbian 相关所有内容的精彩列表，Symbian 是 2000 年代初流行的 ARM 移动操作系统，已停产。它支持 J2ME 应用程序。
- [Cell Phone Game Preservation Wiki](https://cellphonegamespreservation.miraheze.org/wiki/Main_Page) - Wiki 致力于手机保存，包括模拟和游戏转储。
- [J2ME Fandom](https://j2me.fandom.com/wiki) - 与 J2ME 相关的所有内容的 Wiki。
- [J2ME Preservation](https://github.com/j2me-preservation/j2me-preservation) - 各种 J2ME 软件的存档。
- [Legacy Portable Computing Wiki](https://lpcwiki.miraheze.org) - 经常更新的 Wiki 致力于保存过时移动设备的知识和内容。


## 逆向工程

- [PyLng](https://github.com/CakesTwix/pylng) - 用 Python 编写的 HandyGames .lng 文件解析器。

### 反编译器

- [Fernflower](https://github.com/fesh0r/fernflower) - JetBrains 的分析型 Java 反编译器。
- [Jd Decompiler](https://java-decompiler.github.io) - Java 反编译器，支持 Java 5 及更高版本。
- [Javadecompilers.com](https://www.javadecompilers.com) - 在线Java反编译器，支持各种反编译器。
- [Recaf](https://github.com/Col-E/Recaf) - 支持多种反编译器的字节码编辑器。
- [Vineflower](https://github.com/vineflower/vineflower) - Fernflower 反编译器的分支，提高了输出质量。
- [Sporeflower](https://github.com/hourianto/sporeflower) - Vineflower 反编译器的 Fork 专为 J2ME 量身定制。


## 教程

- [J2ME In Nutshell](https://www.oreilly.com/library/view/j2me-in-a/059600253X) - “对微版编程‘字母汤’的可靠、严肃的参考，涵盖 CLDC、CDC、KVM 等。”
- [Revive Nokia N95](https://github.com/domib97/revive.nokia.n95) - 复兴传统诺基亚 N95 并为其开发的快速指南。
- [J2ME Docs](https://nikita36078.github.io/J2ME_Docs) - J2ME 和一些特定于供应商的 API 的文档。
- [Java ME 3.4 Developer's Guide for NetBeans on Windows](https://docs.oracle.com/javame/dev-tools/jme-sdk-3.4/nb/html/toc.htm) - SDK 3.4、Windows 版本 NetBeans 的官方教程。
- [J2ME Performance Tips](https://web.archive.org/web/20050223040231/https://www.javaperformancetuning.com/tips/j2me.shtml#REF25) - 特定于 J2ME 开发的性能优化技巧。
- [Basic Java Examples](https://web.archive.org/web/20121102161050/http://www.java-tips.org/java-me-tips/midp/page3.html) - Java ME 和 MIDP 开发的基本示例。
- [General Java Optimization Tips](https://web.archive.org/web/20050215222448/http://www-2.cs.cmu.edu/~jch/java/) - 基础 Java 性能优化技术。
- [Basic Java Performance Good Practices](https://web.archive.org/web/19970607121931/http://www.javaworld.com/javaworld/jw-04-1997/jw-04-optimize.html) - Java 性能最佳实践的早期参考指南。
- [The JavaTM Virtual Machine Specification Second Edition](https://web.archive.org/web/19990508124421/http://java.sun.com/docs/books/vmspec/2nd-edition/html/VMSpecTOC.doc.html) - 涵盖虚拟机内部结构的官方 JVM 规范文档。
- [Sony Ericsson Development Tips and Tricks](https://web.archive.org/web/20061006072043/http://developer.sonyericsson.com/site/global/techsupport/tipstrickscode/java/p_java.jsp) - 索尼爱立信针对特定设备的开发指南和优化技术。
- [Nokia/Microsoft Mobile Developer Slideshare](https://www.slideshare.net/nokia-developer) - 有关为诺基亚平台（包括 Asha 和 Series 40 平台）开发应用程序的演示。

### 学术文章

- [A Testing Method for Java ME Software](https://doi.org/10.1109/EmbeddedCom-ScalCom.2009.21) - 回顾 J2ME 的各种单元测试方法，并介绍一种适用于 NetBeans 的自定义方法。
- [Automated GUI Testing for J2ME Software Based on FSM](https://ieeexplore.ieee.org/abstract/document/5341641) - 介绍了一种基于 FSM 的 LCDUI J2ME 应用程序自动化测试技术。
- [Developing Jini applications using J2ME technology](https://dl.acm.org/doi/abs/10.5555/507165) - 有关使用 Jini 和 J2ME 开发网络应用程序的书籍。
- [Distributed Gaming using J2ME and XML](https://www.cs.sjsu.edu/faculty/pollett/masters/Semesters/Fall03/Rekha/CS297Report.pdf) - 关于使用 Oracle XML 数据库创建跨平台游戏的文章。
- [Experiences of Implementing BitTorrent on Java ME Platform](https://ieeexplore.ieee.org/abstract/document/4446557) - 关于在诺基亚 S40 上实现 BitTorrent 客户端的详细文章。包括方法和结果。
- [Networked J2ME Applications](https://www.mooreds.com/midp/midp.htm) - 论文探讨了构建网络 MIDP 1.0 应用程序的各个方面。
- [JSR 184: M3G Specification](https://jcp.org/en/jsr/detail?id=184) - 移动图形 3D 图形 API (M3G) 规范，它是 J2ME 设备的 3D 图形功能的文件格式和 API。它有两种模式：立即模式和保留模式。前者与 OpenGL ES 兼容。
