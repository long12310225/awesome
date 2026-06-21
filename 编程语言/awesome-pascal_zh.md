# 很棒的帕斯卡 [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

精选的 Delphi、FreePascal 和其他 *Pascal 框架、库、资源和闪亮的东西的列表。灵感来自 Awesome-xxx 的东西。

**请注意，仅考虑开源项目。死项目（3 年或更长时间未更新）必须非常出色或独特才能包含在内。**

请随意通过评论或拉取请求来建议其他缺失的好项目。

:感叹: **关于编译器兼容性的注意事项**。根据项目的描述，所有项目都有编译器/语言方言兼容性徽章。不检查与未正式支持的编译器的真正兼容性。通常，代码可以与不受支持的编译器/语言方言一起使用，只需进行少量修改，但也可能存在例外。

：感叹：**关于大型项目中包含的功能的注释**。列表中有很多大型项目，其中包含许多值得在相应部分中注意的功能。例如，HTTP 服务器可以具有 JSON 解析器、记录器、命令行解析器、数据库访问类等。对于非常大的代码库，允许特定部分中的重复条目链接到具有主要描述的部分。然而，为了减少重复，附加功能通常会在注释中列出。因此，如果您正在寻找某些功能，除了检查相应部分之外，请不要忘记在整个列表中按关键字进行搜索。也可以随意建议在大型项目中添加可用功能，以帮助其他人找到他们想要的东西。

## 内容##

- [普通图书馆](#general-libraries)
- [Multimedia](#multimedia)
	- [Audio](#audio)
	- [Video](#video)
	- [Graphic](#graphic)
- [游戏开发](#game-dev)
- [Communications](#communications)
	- [Network](#network)
	- [云和远程服务](#cloud-remote-services)
	- [串口](#serial-port)
	- [活动巴士](#event-bus)
- [GUI](#gui)
	- [控制包](#control-packs)
	- [单一控制](#single-controls)
	- [Editors](#editors)
	- [Viewers](#viewers)
	- [其他图形用户界面](#other-gui)
- [Database](#database)
- [Scripting](#scripting)
- [机器学习](#machine-learning)
- [非视觉类/实用程序](#non-visual-classesutils)
	- [Compression](#compression)
	- [Encryption](#encryption)
	- [XML/JSON/YAML/HTML](#xmljsonyamlhtml)
	- [Language](#language)
	- [内存管理器](#memory-managers)
	- [System](#system)
	- [Template](#template)
	- [Logging](#logging)
	- [Math](#math)
	- [Command-line](#command-line)
	- [其他非视觉](#other-non-visual)
- [OS](#os)
- [报告生成](#report-generating)
- [单元测试](#unit-testing)
- [调试/错误处理](#debugging--error-handling)
- [Utilities](#utilities)
	- [RAD Studio IDE 插件/向导](#rad-studio-ide-pluginswizards)
	- [其他 IDE 的插件](#plugins-for-other-ides)
	- [Documentation](#documentation)
	- [代码检查/审查、调试](#code-checkreview-debug)
	- [Setup](#setup)
	- [Other](#other)

---

## 通用图书馆##

*大型通用库*

* [JCL](https://github.com/project-jedi/jcl)。 `[Delphi]` `[FPC]` 一组经过彻底测试和完整记录的实用函数和非可视类，可以在您的 Delphi 和 C++ Builder 项目中立即重用。该库分为几个类别，例如字符串、文件和 I/O、安全性、数学等等。

* [JVCL](https://github.com/project-jedi/jvcl)。 `[Delphi]` 包含由“Project JEDI”成员开发的 600 多个 Delphi 组件的库。
// *GUI、算法、类、API 标头等*

* [Alcinoe](http://sourceforge.net/projects/alcinoe) ([GH 镜像](https://github.com/Zeus64/alcinoe))。 `[Delphi]` Delphi 的可视和非可视组件库。
// *网络：FTP/Http/NNTP/POP3/SMTP、ISAPI、WinInet Http/FTP 客户端；数据库：Firebird/MySQL/SQLite3/Memcached/MongoDb/SphinxQL； XML/JSON 解析器；零点库；加密技术：AES、Blowfish、MD5、SHA、安全密钥 MD5/SHA； opengl视频播放器； FireMonkey控件；其他：自平衡二叉树、表达式求值器*

* [基础代码库](http://sourceforge.net/projects/fundamentals)（已废弃，更新的分支在[此处](https://github.com/fundamentalslib/fundamentals4) - 尽管单位设置略有不同，例如没有 XML。最近的主要版本 5 [此处](https://github.com/fundamentalslib/fundamentals5)）。 `[Delphi]` `[FPC]` Delphi / FreePascal 代码单元的集合。包括 Unicode、字符串、数据结构、套接字和数学库。
// *Utils：ZLIB 压缩； JSON； XML；协议缓冲区；统一码例程；数据结构；哈希：XOR、CRC、Adler、MD5、SHA、安全密钥 MD5/SHA 等；网络：阻止 TCP 客户端/服务器、通过 SSL3/TLS1.0/TLS1.1/TLS1.2 的 HTTP(S)（完全原生）； SQL 解析器；比特币 MtGox 客户端； Blaise 脚本引擎；密码：AES、DES、FUNE、RC2、RC4、RSA、Diffie-Hellman；数学：矩阵、复数、统计、巨数*

* [Spring4D](https://bitbucket.org/sglienke/spring4d)。 `[Delphi]` Embarcadero Delphi 2010 及更高版本的开源代码库。它由许多不同的模块组成，这些模块包含基类库（通用类型、基于接口的集合类型、反射扩展）和依赖项注入框架。包括加密库。
// *使用泛型并基于 IEnumerable 的集合和其他容器，可能比 RTL 类似物更准确、更有特色；加密：CRC、DES、MD5、SHA；文件实用程序等*

* [TheUnknownOnes](https://github.com/chaosben/theunknownones)。 `[Delphi]` 大量的类、组件、实用程序几乎适用于所有用途。几乎没有记录，而且似乎不是最新的。

* [CNVCL](https://github.com/cnpack/cnvcl)。 `[Delphi]` CnPack 组件包。大量可视化组件、类和实用程序的集合。 // *很多有用的东西；文档和注释主要为中文*

* [mORMot](https://github.com/synopse/mORMot)。 `[Delphi]` `[FPC]` 用于 Delphi 6 及更高版本或 FPC 2.7 的客户端-服务器 ORM/ODM SOA MVC 框架。直接 SQL/NoSQL 数据库访问、对象上的 ORM/ODM、通过高性能 HTTP 服务器接口的 RESTful ORM 和 SOA 服务、MVC/MVVM 网站、测试（包括模拟和存根）、日志记录、加密、压缩、命令行解析器、线程、服务/守护程序支持；巨大的文档。

* [火星 - 好奇心](https://github.com/andrea-magni/MARS)。 `[Delphi]` Delphi REST 库。纯 REST 方法，熟悉的 Delphi 风格的标准概念（包括基于组件的客户端库）。已知兼容性：Delphi 版本从 XE 到 10 Seattle。某些功能需要 FireDAC。

* [ADAPT](https://github.com/LaKraven/ADAPT)。 “[Delphi]”高级开发人员异步编程工具包，基础库，旨在用于项目的核心，以提供极其强大的多线程（和线程安全）功能。事件引擎 - 一个非常强大的系统，用于生成多线程、异步和事件驱动的程序。泛型集合 - 高效的集合类型（列表、树、地图等）。数学库 - 用于单位转换、特殊计算和其他有用的数学例程的库。包引擎 - Streamables 引擎的扩展，支持将文件打包在一起（某种 VFS）。共享流库 - 100% 线程安全的流类（也有接口）允许从多个线程读/写。流处理库 - 使使用流变得更加容易！处理删除、插入、读取和写入数据。

* [Redux Delphi](https://github.com/pierrejean-coudert/ReduxDelphi)。 “[Delphi]” 利用单向数据流的 Delphi 应用程序的可预测状态容器。受到 ReduxJS 的启发。附带不可变的通用列表。

* [GrijjyFoundation](https://github.com/grijjy/GrijjyFoundation)。在其他 Grijjy 存储库中使用的“[Delphi]”基础类和实用程序。
// *BSON/JSON、IOCP/EPOLL 套接字、套接字池、HTTP、HTTP/2、OpenSSL、ProtocolBuffers。*

* [unRxLib](http://www.micrel.cz/RxLib/dfiles.htm)。 `[Delphi]` 努力保持 RxLibrary（包含 60 多个组件的库）的真实性。

* [QuickLib](https://github.com/exilon/QuickLib)。 `[Delphi]` `[FPC]` 快速开发库（AutoMapper、LinQ、IOC 依赖注入、MemoryCache、计划任务、配置、序列化器、Json 序列化、Chronometer、线程、列表、配置、控制台服务等），支持 Delphi/Firemonkey（Windows、Linux、macOS/IOS/Android）和 freepascal（Windows/Linux）的跨平台。

* [KOL](https://sourceforge.net/projects/kolmck)。 `[Delphi]` `[FPC]`（[KOL-CE](https://sourceforge.net/p/kol-ce) 移植到 FPC）Delphi（和 FPC）的关键对象库 - 使应用程序更小、更强大。该库是免费软件和开源软件。 MCK是使用KOL库在Delphi环境下进行VISUAL项目开发的镜像类套件。

* [minilib](https://github.com/parmaja/minilib)。 `[Delphi]` `[FPC]` 跨平台库、Socket 包装器（包括 SSL 和 TLS）、数据库连接（SQLite、PostgreSQL、FirebirdSQL、MariaDB）、XML 读取器和写入器、ComPort（COM1、COM2 等）。

* [Fido 库](https://github.com/mirko-bianco/FidoLib)。 `[Delphi]` Fido 库的创建是为了让 Delphi 开发人员的生活更轻松，遵循“尽可能描述行为而不是对其进行编码”的设计原则。以下是最重要的核心功能列表：映射器、JSON 编组和解组、虚拟数据库功能、虚拟 Api 客户端、虚拟 Api 服务器、Websockets、Consul 和 Fabio 支持、盒子、事件驱动架构、函数式编程、柯里化、缓存、通道

* [TeeBI](https://github.com/Steema/TeeBI)。 `[Delphi]` `[FPC]` 数据挖掘、可视化、多维查询、数据透视表和大数据组件库。 VCL，火猴。

## 多媒体##


## 音频

* [音频工具库](http://mac.sourceforge.net/atl)。 `[Delphi]` 用于操作许多音频格式的文件信息。
// *自 2005 年起被废弃。*

* [Delphi ASIO 和 VST 项目](http://sourceforge.net/projects/delphiasiovst)。 “[Delphi]”使用 ASIO 接口和 VST 插件编写应用程序的框架。它配备了无数的 DSP 算法，所有这些算法都在数十个示例中进行了演示。
// *最近不太活跃，但主干处于可用状态*

* [NewAC - 新音频组件](http://code.google.com/p/newac)（已废弃，GH 上的分叉列表[此处](https://github.com/search?l=Pascal&o=desc&q=newac&s=updated&type=Repositories)）。 `[Delphi]` 旨在帮助您的 Delphi 程序执行不同的声音处理任务。使用 NewAC，您可以播放以多种格式存储的音频（wav、Ogg Vorbis、FLAC、Monkey Audio、WavPack、MP3、Windows WMA、DTS、AC-3（杜比环绕声）、VOB（DVD 文件））。
// *播放、录音、标签读/写、一些音频编辑任务和转换*

* [Audorra](https://sourceforge.net/projects/audorra)。 `[Delphi]` `[FPC]` 用于 Delphi 和 Freepascal 的数字音频库。使用灵活的插件架构，它允许您交换音频后端（例如 WaveOut、OpenAL）、添加协议类（例如文件、http）和解码器。

* [Delphi-BASS](https://github.com/TDDung/Delphi-BASS)。 `[Delphi]` Delphi 的 FMX 和 VCL 标头/包装单元用于 [BASS](https://www.un4seen.com) 音频库以及附加组件。

* [FMXAudio](https://github.com/HemulGM/FMXAudio)。适用于 FMX（Windows、Android）的基于“[Delphi]”音频播放器组件的 [BASS](https://www.un4seen.com)


## 视频

* [DSPack](https://code.google.com/p/dspack)（已废弃、活跃的分叉位于[此处](https://github.com/micha137/dspack-continued-mirror-for-delphinus)）。 `[Delphi]` 使用 MS Direct Show 和 DirectX 技术编写多媒体应用程序的组件和类集。

* [Delphi-OpenCV](https://github.com/Laex/Delphi-OpenCV)。 `[Delphi]` Delphi 中 OpenCV 库头文件的翻译
// *包括 FFMPEG 标头*

* [FFmpeg Delphi/Pascal 标头](http://www.delphiffmpeg.com/headers)。 `[Delphi]` `[FPC]` FFMPEG 标头的开源翻译。

* [PasLibVlc](http://prog.olsztyn.pl/paslibvlc)。 `[Delphi]` `[FPC]` VideoLAN libvlc.dll 和基于 VideoLAN 的 Delphi / FreePascal 的 VCL 播放器组件的接口

* [fevh264](https://github.com/dpethes/fevh264)。 `[FPC]` 基线 h.264 编码器。支持 Windows 和 Linux


## 图文

*图像文件、自由绘图、条形码等。[游戏开发](#game-dev)部分还有一些绘图引擎*

* [Graphics32](https://github.com/graphics32/graphics32)。 `[Delphi]` `[FPC]` 专为 Delphi 和 Lazarus 上的快速 32 位图形处理而设计。它针对 32 位像素格式进行了优化，提供了对像素、矢量和多边形图形基元的快速抗锯齿和 Alpha 混合操作，并且显着优于 GDI、GDI+ 和标准 TCanvas 类。每像素访问速度快了近一百倍，画线速度快了约 80-100 倍。

* [GraphicEx](https://github.com/mike-lischke/GraphicEx)。 “[Delphi]” Delphi Graphics.pas 的附录，使您的应用程序能够加载许多常见的图像格式。该库主要设计用于加载图像作为背景（按钮、表单、工具栏）和纹理（DirectX、OpenGL），或者用于图像浏览和编辑目的（只要您不需要保存图像）。

* [Vampyre 成像库](https://github.com/galfar/imaginglib)。 `[Delphi]` `[FPC]` 跨平台本机 Object Pascal（Delphi 和 Free Pascal）图像加载、保存和操作库。

* [CCR-EXIF](https://code.google.com/p/ccr-exif)（似乎已被放弃，GH 上的分叉列表[此处](https://github.com/search?l=Pascal&o=desc&q=ccr-exif&s=updated&type=Repositories)）。 “[Delphi]”库用于从 JPEG、TIFF 和 PSD 图像读取和写入 Exif、IPTC 和 XMP 元数据。

* [KIcon](https://github.com/kryslt/KControls)。 `[Delphi]` `[FPC]` 如果需要对图标进行更复杂的操作（或更好的图标文件 *.ico）而不仅仅是查看，则此组件是有意义的。完整的 PNG 图标图像支持、正确渲染、带有 Alpha 通道的图标。

* [德尔福吐温](http://www.kluug.ne​​t/delphitwain.php)。 `[Delphi]` `[FPC]` 该库允许您轻松访问 Delphi 和 Lazarus 的扫描功能。

* [概要 PDF](https://github.com/synopse/SynPDF)。 `[Delphi]` `[FPC]` 用于 Delphi 的全功能开源 PDF 文档创建库，嵌入在一个单元中。纯 Delphi 代码，Delphi 5 到 Delphi 10.3 Rio（以及最新版本的 FPC），适用于 Win32 和 Win64 平台。

* [PowerPDF](https://github.com/TurboPack/PowerPDF)。 `[Delphi]` VCL 组件用于可视化创建 PDF 文档。与 Forms 一样，您可以在 Delphi 或 C++Builder IDE 上轻松设计 PDF 文档。

* [IGDI+](https://sourceforge.net/projects/igdiplus)。 `[Delphi]` 免费的开源库允许以自然的 Delphi 友好代码快速、轻松地实现复杂的 GDI+ 应用程序。

* [GLScene](https://sourceforge.net/projects/glscene)。 `[Delphi]` `[FPC]` 用于 Delphi、C++Builder 和 Lazarus 的基于 OpenGL 的 3D 库。它提供可视化组件和对象，允许以简单、轻松但功能强大的方式描述和渲染 3D 场景。 GLScene 不仅仅是一个 OpenGL 包装器或实用程序库，它已经发展成为一组通用 3D 引擎的基础类，并考虑到快速应用程序开发。 GLScene 允许您快速设计和渲染 3D 场景，而无需学习复杂的 OpenGL，如果您知道如何设计 TForm，您将轻松掌握 GLScene 的基本操作。该库附带了大量演示，展示了其易用性，并演示了 RAD 并非以牺牲 CPU/GPU 马力为代价。

* [SynGdiPlus](https://github.com/synopse/mORMot/blob/master/SynGdiPlus.pas)。 `[Delphi]` `[FPC]` 使应用程序能够加载和保存 GIF、TIF、PNG 和 JPG 图片。它还允许从任何 TMetaFile 进行抗锯齿绘图。也就是说，您可以使用 GDI+ 而不是 GDI 来播放 .emf 内容，以获得更好的渲染效果。

* [安道尔 2D](http://sourceforge.net/projects/andorra)。 `[Delphi]` `[FPC]` 用于 Delphi 和 Lazarus 的新一代 2D 引擎。 Andorra 2D 能够通过图形插件使用 DirectX 或 OpenGL。 Andorra 2D 以非常模块化的方式构建，并且易于使用。

* [透明画布](https://github.com/vintgedave/transparent-canvas)。 `[Delphi]` Delphi VCL / Windows 项目用于绘制半透明的字母混合图形。它提供了一个类似于TCanvas的类。

* [完全对齐文本](https://github.com/vintgedave/完全对齐文本)。 `[Delphi]` 用于文本输出的 Delphi VCL / Windows 项目，允许使用各种选项打印完全对齐的文本。

* [AsciiImage](https://github.com/Memnarch/AsciiImage)。 `[Delphi]` AsciiImage - Alexander Benikowski 的 Delphi 实现，基于 Charles Parnot 的 AsciiImage。阅读更多关于[他的文章](http://cocoamine.net/blog/2015/03/20/replacing-photoshop-with-nsstring)。
// *从 ASCII 像素图创建可缩放的单色图像*

* [PngComponents](https://github.com/UweRaabe/PngComponents)。 `[Delphi]` PngComponents 是一组组件，允许您在应用程序中包含真实的 PNG 文件。 PNG 文件本身并不会产生巨大的优势，但它们对 Alpha 通道的支持确实具有相当大的魅力。

* [AggPasMod](https://github.com/CWBudde/AggPasMod)。 `[Delphi]` 现代化的 Pascal Anti-Grain 几何。该项目基于 AggPas（本身基于 Anti-Grain Geometry），提供对最新 Delphi 版本（XE 及更高版本）的支持，并包含一些辅助类（VCL 组件和 FireMonkey 接口）。 2D矢量图形库。基本上，您可以将 AggPas 视为一个渲染引擎，它根据一些矢量数据在内存中生成像素图像。当然，AGG 能做的远不止这些。
// *矢量图形库，渲染 SVG 等等*

* [delphi-shader](https://github.com/WouterVanNifterick/delphi-shader)。 `[Delphi]` 数百种图形效果，以及一个以纯 Delphi 代码提供 GLSL 功能的库。该项目生成具有一百多种实时图形效果的可执行文件。所有这些都是 100% pascal 实现，无需使用外部库或硬件加速。

* [dglOpenGL](https://github.com/SaschaWillems/dglOpenGL)。 `[Delphi]` `[FPC]` Delphi / Pascal OpenGL 标头翻译。

* [DelphiZXingQRCodeEx](https://github.com/MichaelDemidov/DelphiZXingQRCodeEx)。 `[Delphi]` `[FPC]` Delphi/Lazarus 移植了来自 ZXing（一个开源条形码图像处理库）的 QR 码生成功能。

* [ZXing.Delphi](https://github.com/Spelt/ZXing.Delphi)。 “[Delphi]”适用于 Delphi XE 至 10.2 Tokyo 的本机对象 Pascal 库，基于众所周知的开源条形码扫描库 ZXing（斑马线）。它针对所有 FireMonkey 移动平台，从 v3.1 开始，它还完全支持 Windows VCL 应用程序（不依赖于 FMX.Graphics 单元）。

* [Zint-Barcode-Generator-for-Delphi](https://github.com/landrix/Zint-Barcode-Generator-for-Delphi)。 `[Delphi]` Zint-Barcode-Generator 的本机 Delphi 端口。

* [QuickImageFX](https://github.com/exilon/QuickImageFX)。 `[Delphi]` Delphi 库用于简化图像加载/保存、转换和转换。加载/保存 png、jpg、gif 和 bmp。从不同的资源获取图像：文件、流、http、图像列表、关联的窗口图标、可执行文件图标等。旋转、翻转、灰度和许多其他转换。

* [NativeJpg](https://code.google.com/p/simdesign)。 `[Delphi]` 完全面向对象的 Pascal 实现，允许读取和写入 Jpeg 文件。您可以使用此软件从文件或流中读取和写入 Jpeg 图像。它支持基线和渐进式 Jpeg、元数据支持以及所有可以想象的无损操作。

* [OpenGL Pascal 工具包](https://github.com/daar/GLPT)。 `[FPC]` 易于使用的原生 pascal 工具包，允许以独立于平台的方式创建和管理 OpenGL 上下文。

* [BGRA位图](https://github.com/edivando-fpc/BGRABitmap)。 `[Delphi]` `[FPC]` 使用 Lazarus 绘制具有透明度和抗锯齿功能的例程。还提供各种变换。这些例程允许操作 BGRA 格式或 RGBA 格式（取决于平台）的 32 位图像。

* [剪辑器](http://angusj.com/delphi/clipper.php)。 `[Delphi]` 库执行线和多边形裁剪 - 交集、并集、差值和异或以及线和多边形偏移

* [dexif](https://github.com/cutec-chris/dexif)。 `[Delphi]` `[FPC]` Delphi EXIF 库的 Lazarus 端口，用于从图像中提取 Exif 信息

* [字体图标编辑器](https://github.com/lminuti/FontIconEditor)。 `[Delphi]` 简单的组件编辑器，允许您将图标从字体添加到 TImageList。您可以使用任何您想要的字体。

* [IconFontsImageList](https://github.com/EtheaDev/IconFontsImageList)。 `[Delphi]` 扩展了 Delphi 的 ImageList（VCL 和 FMX），以简单地使用和管理图标字体（支持 GDI+）

* [Mundus](https://github.com/Memnarch/Mundus)。 `[Delphi]` 用 Delphi 编写的软件渲染器。目前仅支持 Win32，因为它使用一些内联汇编程序。

* [Image32](https://sourceforge.net/projects/image32)。 `[Delphi]` `[FPC]` ([网站](http://www.angusj.com/delphi/image32/Docs/_Body.htm)) 用 Delphi Pascal 编写的 2D 图形库。它提供了广泛的图像处理功能，并包括支持各种画笔填充选项的线条和多边形渲染器。

* [SVGIconImageList](https://github.com/EtheaDev/SVGIconImageList)。 `[Delphi]` 四个渲染 SVG 的引擎（Delphi TSVG、Delphi Image32、Direct2D 或 Cairo）和四个组件来简化 SVG 图像的使用（调整大小、固定颜色、灰度等）。

* [Skia4Delphi](https://github.com/viniciusfbb/skia4delphi)。 `[Delphi]` 用于 Delphi 平台的跨平台 2D 图形 API，基于 Google 的 Skia 图形库。它提供了全面的 2D API，可跨移动、服务器和桌面模型使用来渲染图像。

* [PdfiumLib](https://github.com/ahausladen/PdfiumLib)。使用 PDFium 的 PDF VCL 控件的“[Delphi]”示例

* [llPDFLib](https://github.com/SybrexSys/llPDFLib)。 `[Delphi]` 用于创建 PDF 文档的 Pure Object Pascal 库。该库不使用任何 DLL 或外部第三方软件来生成 PDF 文件。库包括 TPDFDocument 组件，其属性和方法类似于 Delphi 的 TPrinter，但旨在生成 PDF 文件。

* [图像质量](https://github.com/GodModeUser/ImageQuality)。 `[Delphi]` `[FPC]` 用于客观测量图像/视频质量的库。它实现了许多流行的算法，例如 MS-SSIM、MS-SSIM*、SIMM、MSE 和 PSNR。它的设计目标是快速、准确且可靠。可以直接编译，不需要额外的库。

* [DelphiX](http://www.micrel.cz/Dx/)。 `[Delphi]` `[FPC]` 一个很好的 DirectX 包装器。它可用于创建游戏或任何类型的图形界面。

* [Blen2d4Delphi](https://github.com/fatihtsp/Blen2d4Delphi)。 `[Delphi]` Blend2D 是一个用 C++ 编写的高性能 2D 矢量图形引擎，并在 Zlib 许可证下发布。该引擎利用内置的 JIT 编译器在运行时生成优化的管道，并且能够使用多线程来提升性能，超越单线程渲染的可能性。

* [libdmtx 的 Delphi 包装器](https://github.com/JanOosting/delphidmtx)。 `[Delphi]` Libdmtx 是一个软件库，使程序能够读取和写入现代 ECC200 品种的数据矩阵条形码。该库在多个平台上本机运行，并且可以使用 libdmtx 语言包装器通过多种语言进行访问


## 游戏开发##

*[Graphic](#graphic)部分还有一些适合游戏开发的绘图引擎*

* [RecastNavigation](https://github.com/Kromster80/RecastNavigationDelphi)。 `[Delphi]` 用于游戏的导航网格构建工具集。 Recast 附带 Detour、寻路和空间推理工具包。您可以在 Detour 中使用任何导航网格，但当然，使用 Recast 生成的数据非常适合。这是用 C++ 编写的原始 RecastNavigation 的端口。

* [Kraft 物理引擎](https://github.com/BeRo1985/kraft)。 `[Delphi]` `[FPC]` 可用于 3D 游戏的开源 Object Pascal 物理引擎库。兼容：Delphi 7-XE7（但不适用于 Android 和 iOS 目标）、FreePascal >= 2.6.2（几乎所有支持 FPC 的目标，包括 Android 和 iOS）

* [ZenGL](https://github.com/Seenkao/New-ZenGL)。 `[Delphi]` `[FPC]` OpenGL 用 Pascal 编写的跨平台游戏开发库，旨在提供渲染 2D 图形、处理输入、声音输出等所需的功能。

* [Asphyre 又名平台扩展库 (PXL)](https://sourceforge.net/projects/asphyre)。 `[Delphi]` `[FPC]` 用于开发 2D/3D 视频游戏、交互式和科学应用程序的跨平台框架。它帮助开发人员掌握数学、硬件控制、资源管理、显示实时图形和文本、处理用户输入和网络通信功能。

* [CrystalPathFinding](https://github.com/d-mozulyov/CrystalPathFinding)。 `[Delphi]` `[FPC]` 简单而有效的开源库，旨在通过算法 A*/WA* 搜索基于具有 4 个（简单）、8 个（对角线/对角线）或 6 个（六边形）邻居的图块的地图的最短路径。

* [Allegro-Pas](https://sourceforge.net/projects/allegro-pas) ([GitHub](https://github.com/niuniomartinez/allegro-pas))。 `[Delphi]` `[FPC]` 包装器，用于将 Allegro 游戏库与 Pascal/Delphi 结合使用。

* [城堡游戏引擎](https://github.com/castle-engine/castle-engine)。 `[Delphi]` `[FPC]` 完整的 Pascal 游戏引擎。跨平台 3D 和 2D 游戏引擎，具有大量图形效果和基于 X3D 的场景图。

* [TileEngine](http://www.tilengine.org)。 ([GitHub](https://github.com/turric4n/PascalTileEngine)) `[Delphi]` `[FPC]` OOP Pascal 包装器和 Tilengine 2D 复古图形引擎的绑定。 Tilengine 是一个跨平台 2D 图形引擎，用于使用图块地图、精灵和调色板创建经典/复古游戏。其基于扫描线的渲染算法使光栅效果成为核心功能，许多在真实 2D 图形芯片上运行的游戏都使用这种技术。

* [SDL2](http://www.freepascal-meets-sdl.net/) ([GitHub](https://github.com/ev1313/Pascal-SDL-2-Headers))。 `[Delphi]` `[FPC]` Pascal SDL 2 标头。 Simple DirectMedia Layer 是一个跨平台开发库，旨在通过 OpenGL 和 Direct3D 提供对音频、键盘、鼠标、操纵杆和图形硬件的低级访问。

* [SFML](https://github.com/CWBudde/PasSFML)。 `[Delphi]` `[FPC]` Pascal SFML 标头。 SFML 为 PC 的各个组件提供了一个简单的接口，以简化游戏和多媒体应用程序的开发。它由系统、窗口、图形、音频和网络五个模块组成。目前支持 Delphi 和 FPC/Lazarus。但是，由于编译器与 Delphi 编译器不兼容（通过解决方法解决），目前建议使用 FPC。

* [pasvulkan](https://github.com/BeRo1985/pasvulkan)。 `[Delphi]` `[FPC]` Vulkan 标头生成器、OOP 风格的 API 包装器、框架和面向 Object Pascal 的基于 Vulkan 的未来游戏引擎。

* [DarkGlass](https://github.com/kenjones007/DarkGlass)。 `[Delphi]` DarkGlass 是一个使用 Delphi 编写的通用游戏引擎。

* [JEDI-SDL](https://sourceforge.net/projects/jedi-sdl)。来自 JEDI 的 SDL 的“[Delphi]”“[FPC]” Pascal 标头。适用于 Delphi、Kylix、Free Pascal、Gnu Pascal 和 TMT Pascal。

* [Apus游戏引擎](https://github.com/Cooler2/ApusGameEngine)。 `[Delphi]` `[FPC]` 跨平台库，主要用于制作 2D 游戏、GUI 应用程序和 Web 服务。支持 UI、文本渲染、即时本地化、粒子、基本脚本和许多较低级别的子系统。使用 OpenGL/GLES 和 DirectX。

* [Delphi3D 引擎](https://github.com/BrokenGamesUG/delphi3d-engine)。 `[Delphi]` 用于 Delphi 和 Windows 的 3D 图形和游戏引擎

* [Ray4Laz](https://github.com/GuvaCode/Ray4Laz)。 `[FPC]` [raylib](https://www.raylib.com/) 到 Pascal 的完整标头翻译（绑定）。

* [TurboRaylib](https://github.com/turborium/TurboRaylib)。 `[Delphi]` `[FPC]` TurboRaylib 是一个很酷且干净的 Object Pascal 绑定 [raylib](https://www.raylib.com/)。支持Windows、Linux、OSX。 TurboRaylib 有许多在 Delphi 和 Lazarus 中运行的示例。

* [ImGui-Pascal](https://github.com/Coldzer0/ImGui-Pascal)。 `[Delphi]` `[FPC]` ImGui-Pascal 是 [ImGui](https://github.com/ocornut/imgui) 与最新版本的绑定（跨平台 GUI 库）和对接。支持Windows、Linux、OSX。

* [abmaze](https://github.com/DosWorld/abmaze)。 `[FPC]` `[TP]`Aldous-Broder 算法在 Pascal 中实现，用于迷宫生成。包含少量优化。


## 通讯##


## 网络

*套接字通信、网络协议、编码等*

* [互联网组件套件](http://www.overbyte.be/frame_index.html)。 `[Delphi]` 由各种 Internet 组件和应用程序组成的基于异步的库。 TCP、UDP、原始套接字、FTP、SMTP、POP3、NNTP、HTTP、Telnet 等的客户端/服务器。在 OpenSSL 的帮助下支持 SSL 和 TLS。还包括 Mime 解码器、SHA1/MD4/MD5 哈希值、DES 加密。

* [Indy](https://github.com/IndySockets/Indy)。 `[Delphi]` `[FPC]` 用于 Delphi、C++Builder、Delphi.NET 和 FreePascal 的网络组件
// *基于阻塞套接字和线程的一体化网络库。自 2006 年起包含在默认的 RAD studio 安装中。*

* [亚拉拉山突触](https://github.com/geby/synapse)。 `[Delphi]` `[FPC]` 用于 Delphi、C++Builder、Kylix 和 FreePascal 的 Pascal TCP/IP 库。通过阻塞（同步）套接字或有限的非阻塞模式处理网络通信。该项目不使用异步套接字！该项目包含简单的低级非可视对象，可轻松实现最简单的编程（无需多线程同步，无需 Windows 消息处理等）非常适合命令行实用程序、可视化项目、NT 服务等
// *TCP、UDP、ICMP、RAW； ICMP、DNS、SMTP、HTTP、SNMP、NTP、FTP、LDAP、NNTP、Telnet；  IPv6； SOCKS代理； SSL/TLS（通过 OpenSSL 或 Windows CryptoApi）；平；字符代码转码； MIME编码和解码； CRC16、CRC32、MD5 和 HMAC-MD5。*

* [互联网专业](http://sourceforge.net/projects/tpipro2010)。 `[Delphi]` VCL 组件集，为 Borland Delphi 和 C++Builder 提供 Internet 连接。 iPRO 包括 POP3、SMTP、NNTP、FTP、HTTP、即时消息和 HTML 查看器组件，以及用于低级套接字访问的组件。
// *似乎已被放弃，但包含相当多的功能，包括 ICMP、POP、SMTP、HTTP、NNTP、NTP、FTP、SMTP； HTML 解析器和查看器； MIME 实用程序； cookie、证书、缓存、加密等*

* [SynCrtSock](https://github.com/synopse/mORMot/blob/master/SynCrtSock.pas)。 `[Delphi]` `[FPC]` 具有多个套接字和 HTTP 客户端-服务器类，包括 Windows 下基于 http.sys 的高性能服务器，以及新的线程池驱动的套接字服务器。
// *还实现了Windows下的http.sys绑定和nix下的cURL绑定*

* [TML 消息套件](https://github.com/tml21/libtml-pascal)。 `[Delphi]` `[FPC]` 用于快速开发可扩展和可缩放接口的网络消息传递库。基于点对点标准协议[BEEP（块可扩展交换协议）](http://www.beepcore.org)，在[RFC3080](https://tools.ietf.org/html/rfc3080)和[RFC3081](https://tools.ietf.org/html/rfc3081)中定义。 libTML 适用于许多用例和通信模式。配备类型安全数据 API，TML 可以快速可靠地传输分层数据结构。
// *libTML Object Pascal 组件不仅是与核心库绑定的语言，而且是一套完整的非可视化组件，可简化 libTML 与 Embarcadero RAD Studio 和 Lazarus 的使用。*

* [DMVCFramework](https://github.com/danieleteti/delphimvcframework)。 `[Delphi]` Delphi 中流行且强大的 Web 解决方案框架。

* [德尔福 IOCP](https://github.com/ymofen/diocp-v5)。 `[Delphi]` 实现了几个基于 Windows IOCP 技术的网络类。 Socket、HTTP、Ntrip 服务器和客户端。
// *有很好的文档记录和良好的风格代码，但只有中文。*

* [Kitto](https://github.com/EtheaDev/kitto)。 `[Delphi]` 允许基于可映射到任何数据库的数据模型创建富互联网应用程序。客户端部分使用 ExtJS（通过 ExtPascal 库）创建一个完整的 AJAX 应用程序，使您可以在很短的时间内构建标准和高级的数据操作表单。 Kitto 面向需要创建 Web 应用程序的 Delphi 开发人员，无需深入研究 HTML、CSS、JavaScript 的复杂性或学习使用 ExtJS 等特定库，但如果需要，它允许访问裸机。另外还有较新的版本 [Kitto 2](https://github.com/EtheaDev/kitto2) 和 [Kitto 3](https://github.com/EtheaDev/kitto3)。

* [Daraja 框架](https://github.com/michaelJustin/daraja-framework)。 `[Delphi]` `[FPC]` 用于 Object Pascal 的轻量级 HTTP 服务器框架（Delphi 2009+ / Free Pascal 3.0）。通过 [daraja-restful](https://github.com/michaelJustin/daraja-restful) 扩展支持实现 RESTful 服务。

* [Alcinoe](#general-libraries)。 FTP/Http/NNTP/POP3/SMTP、ISAPI、WinInet Http/FTP 客户端。

* [基础代码库](#general-libraries)。通过 SSL3/TLS1.0/TLS1.1/TLS1.2（完全本机）阻止 TCP 客户端/服务器、HTTP(S)。

* [mORMot](#general-libraries)。通过高性能 HTTP 服务器、MVC/MVVM 网站上的接口提供 RESTful ORM 和 SOA 服务

* [Hprose for Delphi/Lazarus](https://github.com/hprose/hprose-delphi)。 `[Delphi]` `[FPC]` 高性能远程对象服务引擎。它是一个现代化的、轻量级的、跨语言、跨平台、面向对象、高性能、远程动态通信的中间件。它不仅易于使用，而且功能强大。该项目是 Hprose for Delphi/Lazarus 的实现。

* [DelphiZeroMQ](https://github.com/grijjy/DelphiZeroMQ)。 `[Delphi]` ZeroMQ Majordomo 协议和 CZMQ 高级绑定的 Delphi 实现。

* [GrijjyFoundation](#general-libraries)。 IOCP/EPOLL 套接字、套接字池、HTTP、HTTP/2、OpenSSL、ProtocolBuffers。

* [STOMP 客户端](https://github.com/danieleteti/delphistompclient)。 `[Delphi]` `[FPC]` 用于 Embarcadero Delphi 和 FreePascal 的 STOMP 客户端。该项目可以使用 INDY (Delphi) 或 Synapse (Delphi 或 FreePascal)。

* [BesaSoap](https://github.com/besasoftware/besasoap)。 `[Delphi]` BesaSoap 库旨在帮助程序员开发更快、更原生的 Web 服务客户端应用程序。表示类似 C# 或 Java 的本机类支持、可空数据类型和自定义属性。

* [IndySoap](https://sourceforge.net/projects/indysoap)。 “[Delphi]”开源库，用于使用 Delphi/CBuilder 编译器实现 Web 服务。尽管包含基于 Indy 的传输服务，但 IndySoap 并不与 Indy 相关的传输服务相关联。

* [Fano框架](https://fanoframework.github.io)。 `[FPC]` 现代 Pascal 编程语言的 Web 应用程序框架。它是用 Free Pascal 编写的。

* [互联网工具](#xmljsonyaml)。 XPath/XQuery/JSONiq/CSS/HTML；在 Windows/Linux/macOS/Android 上执行 HTTP/S 请求的函数、受 XSLT 启发的网页抓取语言和自动更新类。

* [Delphi 交叉套接字](https://github.com/winddriver/Delphi-Cross-Socket/)。 `[Delphi]` `[FPC]` Delphi/FPC 跨平台套接字库（中文）。针对不同平台使用不同的 IO 模型：IOCP (Windows)、KQUEUE (FreeBSD(macOS、iOS 等))、EPOLL (Linux(Linux、Android))。支持 TCP、HTTP/HTTPS、带 SSL/TLS 的 WebSocket。
// *零拷贝流架构可实现最大吞吐量。 10K+ 并发连接。 [英文评论叉](https://github.com/bero/Delphi-Cross-Socket)*

* [ToroKernel](https://github.com/torokernel/torokernel)。 `[FPC]` 这是一个库内核，允许专门移植的 freepascal 应用程序在系统中单独运行。 Toro 在用户的应用程序中进行编译，从而生成一个可以在裸机上启动或作为现代虚拟机管理程序（例如 hyperv、kvm、qemu、firecraker）中的来宾启动的二进制文件。 ToroKernel 通过提供专用 API 来解决微服务的开发问题。

* [马](https://github.com/HashLoad/horse)。 `[Delphi]` `[FPC]` 快速且简约的 Web 框架。 Horse 允许毫不费力地创建强大的 RESTful 服务器。专注于微服务。

* [Bauglir WebSocket](https://github.com/MFernstrom/Bauglir-WebSocket-2)。 `[Delphi]` `[FPC]` 基于 Ararat Synapse 的 WebSocket 服务器/客户端实现。

* [Delphi-RabbitMQ](https://github.com/HeZiHang/Delphi-RabbitMQ)。用于 Delphi 的“[Delphi]” RabbitMQ 驱动程序

* [DelphiGrpc](https://github.com/ultraware/DelphiGrpc)。 `[Delphi]` 实时和流式 gRPC 协议的实现

* [Delphi JOSE 和 JWT 库](https://github.com/paolo-rossi/delphi-jose-jwt)。 `[Delphi]` JOSE（JSON 对象签名和加密）和 JWT（JSON Web 令牌）的 Delphi 实现

* [WiRL](https://github.com/delphi-blocks/WiRL)。 “[Delphi]”项目的创建是为了简化 Delphi 中的 RESTful 服务实现，但更重要的是，实现与用其他语言和工具编写的 REST 客户端的最大互操作性

* [OpenSSL](https://github.com/lminuti/Delphi-OpenSSL)。 OpenSSL 的“[Delphi]”Delphi 包装器

* [Thrift Delphi 软件库](https://github.com/apache/thrift/tree/master/lib/delphi)。 `[Delphi]` 用于点对点 RPC 实现的轻量级、独立于语言的软件堆栈。 Thrift 为数据传输、数据序列化和应用程序级处理提供了干净的抽象和实现。代码生成系统以简单的定义语言作为输入，生成跨编程语言的代码，使用抽象堆栈来构建可互操作的 RPC 客户端和服务器。 Thrift使得用不同编程语言编写的程序可以轻松地共享数据和调用远程过程。 Thrift 支持 28 种编程语言，因此很可能支持您当前使用的语言。

* [Delphi Modbus](https://github.com/coassoftwaresystems/delphi-modbus)。 `[Delphi]` `[FPC]` 通过 TCP/IP 实现 ModbusTCP 协议主站和从站。

* [RESTRequest4Delphi](https://github.com/viniciussanchez/RESTRequest4Delphi)。 `[Delphi]` RESTRequest4Delphi 是一个 API，用于使用以任何编程语言编写的 REST 服务。旨在以简单、简约的方式促进开发。

* [LazWebsockets](https://github.com/Warfley/LazWebsockets)。 `[FPC]` 这提供了为 FPC 和 Lazarus 编写的小型 Websocket 服务器和客户端实现。它完全基于 fcl ssockets 单元，因此独立于除 FCL 之外的任何其他依赖项。

* [NetCom7](https://github.com/DelphiBuilder/NetCom7)。 `[Delphi]` 这组组件是任何语言中最快的套接字通信实现；这是 TCP/IP 套接字上极其优化的代码。

* [语音通信](https://github.com/terrylao/voice_communication)。 `[Delphi]` 语音通信器组件。
// *实现RTP、RTSP、SHOUT、SNTP、STUN协议和多种音频格式编码/解码*

* [libPasCURL](https://github.com/isemenkov/libpascurl)。 `[Delphi]` `[FPC]` cURL 库的绑定和包装。 libcurl 是用于传输以 URL 语法指定的数据的库，支持 HTTP、HTTPS、FTP、FTPS、GOPHER、TFTP、SCP、SFTP、SMB、TELNET、DICT、LDAP、LDAPS、FILE、IMAP、SMTP、POP3、RTSP 和 RTMP。

* [Delphi_SChannelTLS](https://github.com/Fr0sT-Brutal/Delphi_SChannelTLS)。 `[Delphi]` 辅助函数和套接字类通过 WinAPI (SChannel) 执行 TLS 通信。包括 Overbyte ICS TWSocket 后代类。

* [Delphi-Kafka](https://github.com/HeZiHang/Delphi-Kafka)。 `[Delphi]` 基于 Librdkafka 的高性能 Delphi 客户端，具有完整的协议支持。

* [DelphiKafkaClient](https://github.com/norgepaul/DelphiKafkaClient)。 `[Delphi]` Apache Kafka 的跨平台 Delphi 客户端/包装器。支持 Windows (i386/x64) 和 Linux (x64)。在 Delphi 10.4 上进行了测试，但应该适用于所有现代 Delphi 版本。虽然它看起来按预期工作，但该项目只是概念验证，从未在生产中进行过测试。

* [KafkaGate](https://github.com/dinmil/KafkaGate)。 `[FPC]` 使用 librdkafka 和 ZeroMQ 的 Apache Kafka Free Pascal 绑定。

* [delphi-mqtt](https://github.com/pjde/delphi-mqtt)。 `[Delphi]` 基于 ICS 网络组件的 Delphi MQTT 服务器和客户端组件。

* [mqtt](https://github.com/bkeevil/mqtt)。 `[FPC]` 用于 Lazarus/FPC 的消息队列遥测传输 (MQTT) 客户端和服务器组件包以及演示应用程序。对于客户端和服务器演示应用程序，使用 LNet 组件。

* [LNet](https://github.com/almindor/lnet)。 `[FPC]` 用 Free Pascal 编写的轻量级网络库。异步 TCP/UDP 通信类。 LTCP、LUDP、LTELNET、LFTP 和 LSMTP 是示例程序。

* [NamedPipeExchange](https://github.com/kami-soft/NamedPipeExchange)。用于通过命名管道进行通信的“[Delphi]”服务器和客户端类。基于
[FWIOCompletionPipes](http://rouse.drkb.ru/network.php#fwiocompletionpipe) 单元。

* [delphizmq](https://github.com/bvarga/delphizmq)。 `[Delphi]` `[FPC]` ZeroMQ 绑定。应适用于 Delphi7+ 版本和 FPC 2.6.0。该包包含一个包装器 (zmq.pas) 和一个更高级别的 api (zmqapi.pas)。它应该与 ZMQ 2.2.x 和 3.2.x 一起使用。对于版本 2.2.x，在 zmq.inc 中取消定义 zmq3。该 dll 不属于此存储库，您可以从官方发行版下载相应的，并将其重命名为 libzmq.dll。

* [xxm](https://github.com/stijnsanders/xxm)。 `[Delphi]` 库使您能够在 Delphi 中创建动态网站，在源文件中结合 Delphi 和 HTML。该项目被编译成一个模块，可供 Internet Explorer 中的可插入协议处理程序、ISAPI 扩展、Apache 模块、HTTPAPI、CGI 或 SCGI 或独立 HTTP 服务器使用。

* [Delphi 的 WebSocket 组件](https://bitbucket.org/freeonterminate/websocket/src/master/)。 `[Delphi]` 用于 Delphi 的 WebSocket 组件，平台：Windows / macOS / Linux（可能是 iOS、Android）

* [Bird Socket 服务器](https://github.com/mateusvicente100/bird-socket-server)。用于 Delphi 的“[Delphi]” Websocket 服务器。

* [RealThinClient SDK](https://github.com/teppicom/RealThinClient-SDK/)。 `[Delphi]` 灵活的模块化框架，用于使用 Delphi 构建可靠且可扩展的跨平台应用程序，通过利用 HTTP/S 为 Web 设计，具有完整的 IPv4 和 IPv6 支持以及内置多线程，经过广泛的压力测试以确保最高的稳定性

* [JabberClient](https://github.com/HemulGM/HGMJabberClient)。 `[Delphi]` Jabber 客户端。 XMPP协议

* [libssh2 Delphi](https://github.com/pult/libssh2_delphi)。 `[Delphi]` `[FPC]` Delphi/Pascal 库 libssh2、ssh 和 sftp 协议的包装器

* [布鲁克框架](https://github.com/risoflora/brookframework)。 `[Delphi]` `[FPC]` 微框架，有助于开发 Web Pascal 应用程序。
// *基于外部[libsagui](https://risoflora.github.io/libsagui/)*

* [WebSocket.pas](https://github.com/biot2/WebSocket.pas)。 `[Delphi]` `[FPC]` WebSocket 客户端和服务器库，带有纯 Object Pascal 源代码

* [nats.pas](https://github.com/biot2/nats.pas)。 `[Delphi]` `[FPC]` 基于 libnats-c 的 NATS 对象 Pascal 客户端

* [适用于 Delphi 的 Firebase 服务](https://github.com/SchneiderInfosystems/FB4D)。适用于以下 Firebase 服务 (Google) 的“[Delphi]”跨平台 (FMX/VCL/Console) 库：Firebase RT-DB、Firestore DB、云存储、VisionML、Firebase 授权和 Firebase 函数。该库支持所有平台（Windows、Mac、iOS、Android 和 Linux）。

* [Dext 框架](https://github.com/cesarliws/dext)。 `[Delphi]` 用于现代 Delphi 开发的现代全栈生态系统。它将 ASP.NET Core 和 Spring Boot 等框架的生产力和架构模式引入了 Object Pascal 的本机性能。


## 云和远程服务

*用于云和其他远程服务的API*

* [delphi-aws-ses](https://github.com/monde-sistemas/delphi-aws-ses)。用于 Delphi 应用程序的“[Delphi]” Amazon Simple Email Service (AWS SES) 库。

* [delphi-slackbot](https://github.com/monde-sistemas/delphi-slackbot)。 `[Delphi]` Delphi 库使用 slackbot 在 [Slack](https://slack.com) 上发送消息。

* [SDriver](https://github.com/andrea-magni/SDriver)。 [Delphi]` [Slack](https://slack.com) API 的 Delphi 包装器。

* [TelegaPi](https://github.com/rareMaxim/TelegaPi)。用于在 Delphi 中使用 Telegram Messenger Bot API 的“[Delphi]”库。

* [fp-telegram](https://github.com/Al-Muhandis/fp-telegram)。用于在 FreePascal/Lazarus 中使用 Telegram 机器人 API 的“[FPC]”库。

* [delphiXero](https://github.com/littleearth/delphiXERO)。 `[Delphi]` 用于 Delphi 的 XERO 云会计 API。

* [用于 Delphi 的 Google API](https://github.com/googleapi/googleapi)。用于 Delphi 的“[Delphi]”Google API

* [VK API](https://github.com/HemulGM/VK_API)。用于在 Delphi 中使用 Vkontakte（俄罗斯社交网络）API 的“[Delphi]”库。完整的 API（带有机器人示例）。

* [适用于 Dephi 的 AWS 开发工具包](https://github.com/landgraf-dev/aws-sdk-delphi)。 `[Delphi]` 适用于 Delphi 的非官方 AWS（Amazon Web Services）SDK。

* [Ntfy for Delphi](https://github.com/hazzelnuts/ntfy-for-delphi)。 `[Delphi]` 在 Delphi 中使用 ntfy.sh 服务器推送即时通知的友好库

* [DelphiOpenAI](https://github.com/HemulGM/DelphiOpenAI)。用于 Delphi 的“[Delphi]”OpenAI GPT-3 API

* [IPInfo API](https://github.com/HemulGM/IPInfo_API)。 IP 信息 API 服务的“[Delphi]”包装器

* [TGBot Mini API](https://github.com/HemulGM/TGBotMini)。 `[Delphi]` 用于创建 Telegram 机器人的快速而简单的 API

* [ImgBB API](https://github.com/HemulGM/ImgBB.API)。 `[Delphi]` ImgBB.com API 包装器

* [OWM API](https://github.com/HemulGM/OWM_API)。 `[Delphi]` OpenWeatherMap.com API 包装器


## 串口

* [Synaser](https://github.com/geby/synapse/blob/master/synaser.pas)。 `[Delphi]` `[FPC]` 用于阻止串行端口通信的库。它是与 Synapse 中一样的非可视类，并且程序员界面与 Synapse 非常相似。

* [Async Professional](http://sourceforge.net/projects/tpapro)（[最新](https://github.com/TurboPack/AsyncPro) 和仅针对最新编译器版本的维护版本）。 `[Delphi]` 用于 Embarcadero Delphi、C++Builder 和 ActiveX 环境的综合通信工具包。它提供对串行端口、TAPI 和 Microsoft Speech API（TTS/语音识别）的直接访问。它支持传真、终端仿真、VOIP、RAS 拨号等。
// *似乎已经过时（最后一次更新是在 2011 年），但已适应 XE，并且应该易于在新版本中使用。该项目也有非常详尽的记录。第二个链接指向最新编译器版本的改编版本。*

* [TComPort](https://sourceforge.net/projects/comport)。 `[Delphi]` Delphi/C++ Builder 串行通信组件。它通常很容易用于基本的串行通信目的。
// *自 2011 年以来似乎已被废弃*

* [ComPortDriver](https://github.com/MHumm/ComPortDriver)。 '[Delphi]' Delphi/C++ Builder 串行通信组件。测试波特率高达 921600。也支持发送中断。通过计时器轮询异步工作（间隔可配置）。包括演示。

* [ComPort 库](https://github.com/CWBudde/ComPort-Library)。 `[Delphi]` Delphi 的 COM 端口库（来自 SourceForge 的分支）。 ComPort 库包含访问 COM 端口的代码。最初，COM端口是IBM-PC兼容计算机的串行端口接口的名称。虽然现在 COM 端口对于通信的重要性不再那么重要，而有利于 USB 访问，但它仍然用作虚拟端口，尤其是作为创客板的简单通信协议。

* [适用于 Android 的 USB 串行控制器](https://github.com/felHR85/UsbSerial)。适用于 Android 的“[Delphi]” USB 串行控制器


## 活动巴士

*项目内部沟通*

* [PubSub Chimera](https://code.google.com/p/pubsubchimera)。用于 Delphi 的“[Delphi]”开源（MIT 许可证）库，它在不糟糕的许可证下提供了快速且跨平台的 PubSub 和消息队列实现。

* [Delphi 事件总线](https://github.com/spinettaro/delphi-event-bus)（简称 DEB）。用于 Delphi 的“[Delphi]”事件总线框架。

* [DelphiEventBus](https://github.com/BitecSPB/DelphiEventBus)。 `[Delphi]` Delphi 的另一个事件总线框架，具有注释和丰富的事件过滤。

* [VSoft.Messaging](https://github.com/VSoftTechnologies/VSoft.Messaging)。 `[Delphi]` 库为 Delphi 应用程序提供内部同步/异步发布/订阅消息系统。

* [iPub 消息传递](https://github.com/viniciusfbb/ipub-messaging)。 `[Delphi]` 由 iPub 团队创建的线程安全、异步和简单的消息传递系统，用于 delphi 中的类/层之间的通信。

* [NX-Horizo​​n](https://github.com/dalijap/nx-horizo​​n)。用于 Delphi 的“[Delphi]”事件总线。实现发布/订阅模式，支持同步/异步类型的事件传递，实现和使用简单，速度快，全线程安全。


## 图形用户界面##

*视觉组件*


## 控制包

*大量 GUI 控件*

* [Cindy 组件](http://sourceforge.net/projects/tcycomponents)。包含 71 个组件的“[Delphi]”包：VCL 控件（标签、按钮、面板、编辑、TabControls、StaticText），具有背景渐变、彩色斜角、壁纸、阴影文本、标题方向等功能。

* [Orpheus](http://sourceforge.net/projects/tporpheus)（[最新](https://github.com/TurboPack/Orpheus) 和仅针对最新编译器版本的维护版本）。 “[Delphi]” 屡获殊荣的 Borland Delphi 和 C++Builder UI 工具包。它包含 120 多个组件，涵盖从数据输入到日历和时钟的所有内容。其他值得注意的组件包括对象检查器、LookOut 栏和报告视图。
// *高级编辑、组合框、网格+组件（反）序列化器。 GUI 组件看起来相当老式，主题支持可能有限。包包含许多演示，但似乎没有可用的文档。第二个链接指向最新编译器版本的改编版本。*

* [KControls](https://github.com/kryslt/KControls)。 `[Delphi]` `[FPC]` 控制组件。所有控件的编写目的都是为了跨 IDE 兼容（Delphi/C++Builder VCL 和 Lazarus LCL）和 Lazarus 中的跨平台兼容。
// *最有用的是 TKGrid 及其数据库感知传统 TKDBGrid — 一个功能非常齐全的网格实现，包括。就地编辑。还有十六进制编辑器、打印预览、编辑器、标签、按钮等。*

* [D.P.F Delphi Android](http://sourceforge.net/projects/dpfdelphiandroid) / [D.P.F Delphi iOS](http://sourceforge.net/projects/dpfdelphiios) 原生组件。 `[Delphi]` D.P.F Delphi 本机组件，100% iOS 性能和样式。开发具有快速本机性能和本机风格的 iPhone、iPad 和 iPod Touch 应用程序。使用原生 Android 控件和服务。快速的本机性能。与 FM VCL 控件混合。可以快速更新最新的 Android 控件和功能。

* [必需品](https://github.com/TurboPack/Essentials)。 `[Delphi]` 包含 13 个用于 Embarcadero Delphi 和 C++Builder 的本机 VCL 控件。这些控件包括下拉日历和计算器、卷起对话框、3D 标签、平铺背景、滚动消息、菜单按钮等。

* [FreeEsVCLComponents](https://github.com/errorcalc/FreeEsVCLComponents)。 `[Delphi]` 用于 Delphi 和 C++Builder 的免费 VCL 组件库。这种新的控件和组件改善了应用程序的外观并带来更好的用户体验。组件支持视觉风格并具有现代风格。所有组件都具有最好的支持透明度，不闪烁，并且支持 TGraphicControl 继承者的双缓冲的有趣可能性。

* [SpTBXLib](https://github.com/SilverpointDev/sptbxlib)。 `[Delphi]` 为 Toolbar2000 组件添加包，它添加了以下功能：皮肤、Unicode 支持、自定义绘画事件等等。

* [Kastri](https://github.com/DelphiWorlds/Kastri)。 `[Delphi]` 跨平台库，构建于 Delphi 中现有的 RTL 和 FMX 库之上。支持许多在 FMX/RTL 中找不到的较新 API，并“回填”缺失的 API

* [DelphiUCL](https://github.com/VuioVuio/DelphiUCL)。用于 Delphi VCL 的“[Delphi]”UWP 控件。

* [JPPack](https://github.com/jackdp/JPPack)。 `[Delphi]` `[FPC]` Delphi 的 VCL 组件以及 Lazarus 和 CodeTyphon 的 LCL 组件集合 - 按钮、面板、LinkLabel、ProgressBar、ColorComboBox、ColorListBox、Timer 等

* [DDuce](https://github.com/beNative/dduce)。 `[Delphi]` 使用 Delphi 新语言功能（如运算符重载、属性、泛型、匿名方法和扩展 RTTI）的组件、模块、扩展和原语，提供了一些新的强大工具来扩展开发人员的创造力。
// *属性编辑器、网格、XML 树等*

* [liblcl](https://github.com/ying32/liblcl)。 `[FPC]` 一个通用的跨平台GUI库，核心使用Lazarus LCL。
// *基于 Pascal 的库，具有 GUI 绑定，可用于 C++、Go、Rust 等语言。*


## 单一控制

* [EasyListView](http://code.google.com/p/mustangpeakeasylistview)（似乎已被放弃，GH 上的活跃分叉[此处](https://github.com/TurboPack/MustangpeakEasyListview)）。 `[Delphi]` 是 Listview 的 VirtualShellTools 的一部分，但可用于更快、更可定制的 TListview 替换。
// *功能丰富的 Listview 实现虚拟（基于回调）MVC 范例。*

* [VirtualTreeView](https://github.com/Virtual-TreeView/Virtual-TreeView)。 `[Delphi]`（[VirtualTreeView-Lazarus](https://github.com/blikblum/VirtualTreeView-Lazarus) 端口到 FPC `[FPC]`）。从头开始构建的树视图控件。多年的发展使其成为当今最灵活、最先进的树控件之一。
// *极其灵活的可视化组件实现虚拟（基于回调）MVC 范例。也可以用作列表视图或网格。用于 RAD Studio GUI。*

* [Delphi Chromium 嵌入式](https://github.com/hgourvest/dcef3)。 `[Delphi]` 在 Delphi 中嵌入 Chromium，在 Delphi 2010、XE、XE2、Delphi 7 上进行测试。
// *需要几个 Chromium DLL*

* [TChromeTabs](https://github.com/norgepaul/tchrometabs)。 `[Delphi]` 全面实现 Delphi 6 - Delphi 10.1 Berlin 的 Google Chrome 选项卡

* [TFrameStand](https://github.com/andrea-magni/TFrameStand)。 `[Delphi]` 在您的 FireMonkey (FMX) 应用程序中轻松使用 TFrame，以在整个用户体验中获得视觉一致性，并轻松添加现代外观元素，例如效果和过渡。

* [TPrintPreview](https://github.com/landrix/TPrintPreview-for-Delphi)。用于 Delphi Vcl Win32/Win64 的“[Delphi]”打印预览组件

* [VolgaDB](https://sourceforge.net/projects/volgadb)。 `[Delphi]` 用于 Delphi 的非常可定制的 DBgrid。 TCustomGrid 后代。复选框、组合框列样式。还包括 TVolgaDBEdit，它在一个组件中取代了 TDBEdit、TDBComboBox、TDBLookupCombo、TDBLookupTree 和 TDBDatePicker。 TVolgaDBEdit 可以是数据库感知的和非数据库感知的。
// *自 2013 年以来似乎已被废弃*

* [TTreeListView](http://github.com/benibela/treelistview)。 `[Delphi]` `[FPC]` 该组件是 TTreeView 和 TListView 的混合体，可以绘制一棵树，其节点具有按列排序的附加信息。

* [neTabControl](https://github.com/jkour/neTabControl)。 `[Delphi]` Delphi 的 FireMonkey 控件。它建立在本机 TabControl 的基础上，并添加了许多功能。

* [ATTabs](https://github.com/Alexey-T/ATFlatControls)。 `[Delphi]` `[FPC]` 用于精简选项卡的 Delphi/Lazarus 组件。独立于操作系统，完全自定义绘制。

* [zControls](https://github.com/MahdiSafsafi/zcontrols)。 `[Delphi]` 包含 TzObjectInspector - 一个具有许多功能的强大对象检查器。

* [RiverSoftAVG 图表组件套件](http://www.riversoftavg.com/charting.htm)。 `[Delphi]` 免费（用于非商业用途），带有源图表套件，用于将图表和图形添加到您的程序中。对于 Delphi 2010-Tokyo (Win32/Win64/macOS/iOS/Android) 和 Appmethod (Object Pascal)。

* [DzHTMLText](https://github.com/digao-dalpiaz/DzHTMLText)。 `[Delphi]` `[FPC]` 可视化组件，允许您使用 HTML 代码中使用的几乎相同的语法在标签中指定格式化文本。

* [SMDBGrid组件](http://www.scalabium.com/smdbgrid.htm)。 `[Delphi]` TDBGrid 的继承者，具有扩展功能。能够显示多行自动换行列标题、布尔字段的复选框、通过复选框从键盘和鼠标方便地选择记录、扩展指示符列、固定列、排除 DBGrid 中记录的插入和删除的机会、自己的标准弹出菜单、保存/恢复列状态、处理其他事件等。多语言资源。

* [decTreeView](https://github.com/DenisAnisimov/decTreeView)。 `[Delphi]` decTreeView 库是 TreeView (SysTreeView32) 控件的替代实现

* [TeeGrid](https://github.com/Steema/TeeGrid)。 `[Delphi]` `[FPC]` 轻量级全功能网格/表格控件。适用于 Embarcadero RAD Studio 2009 及 Sydney 10.4 及更高版本、Delphi 和 C++、VCL 和 Firemonkey 框架（所有平台：Windows 32 和 64 位、Mac OSX、Android 和 iOS）以及 Lazarus FreePascal（Windows、Linux 等）

* [AXW 色带](https://www.axolot.com/axwribbon.htm)。具有 Office 2016 风格的“[Delphi]”功能区组件。适用于 Delphi 7 及最新的 Delphi 版本。可能会使用 Delphi 6 甚至 Delphi 5 进行编译。


## 编辑

* [SynEdit](https://sourceforge.net/projects/synedit)（[GitHub 上的镜像](https://github.com/TurboPack/SynEdit)）。 `[Delphi]` 语法高亮编辑控件，不基于Windows通用控件。 SynEdit 与 Delphi 和 Kylix 兼容

* [LazEdit](https://svn.code.sf.net/p/lazarus-ccr/svn/applications/lazedit)。 `[FPC]` 通用文本编辑器，具有语法突出显示和帮助编辑 HTML 的工具。

* [ATSynEdit](https://github.com/Alexey-T/ATSynEdit)。 `[FPC]` Lazarus 的多行编辑器控件，包括语法突出显示。

* [QDSEquations](https://github.com/karser/QDSEquations)。 “[Delphi]” Delphi 和 Lazarus 的方程编辑器允许您输入和显示任何复杂的数学公式，从简单的希腊符号到矩阵和复杂的积分表达式。

* [TBCEditor](https://github.com/LaKraven/TBCEditor)。 `[Delphi]` RAD Studio (Delphi/C++ Builder) 的语法突出显示编辑控件，具有代码折叠、补全建议、匹配对、小地图、同步编辑、自动换行等功能。外部突出显示和颜色方案文件采用 JSON 格式，也可以从流加载。


## 观众

* [ATViewer](https://sourceforge.net/projects/atviewer)（[GitHub 上的镜像](https://github.com/Alexey-T/ATViewer)）。 `[Delphi]` Delphi 组件用于查看各种文件类型：文本、二进制、图像、多媒体、网页等。
// *用于Universal Viewer 软件。可用于显示十六进制转储，具有快速显示无限大小文件/流的功能。支持 Total Commander Lister 插件。*

* [ATImageMap](https://sourceforge.net/projects/atviewer/files/ATImageMap) ([GitHub 上的镜像](https://github.com/Alexey-T/ATViewer))。 “[Delphi]”组件旨在将许多图像（整个图像的一部分）显示为单个地图。例如，您可能有图像数组，X 为 200 个，Y 为 100 个，控件会将它们显示为单个地图。组件还允许绘制路径：每条路径由许多线、点和图标组成。

* [HtmlViewer](https://github.com/BerndGabriel/HtmlViewer)。 `[Delphi]` `[FPC]` Delphi/Lazarus HtmlViewer/FrameViewer。
// *Html 可视化工具支持大多数标签、内联样式和 CSS。*

* [SciDe](https://github.com/da-baranov/SciDe)。 `[Delphi]` `[FPC]` [Sciter](https://sciter.com)（嵌入式 HTML/CSS/脚本引擎）Delphi 包装器。

* [用于 Delphi 的 ATBinHex](https://github.com/Alexey-T/ATViewer/blob/master/Source/ATBinHex.pas)。 `[Delphi]`，[Laz 的 ATBinHex](https://github.com/Alexey-T/ATBinHex-Lazarus)。 `[FPC]` 查看器，用于无限大小的文件，如 Total Commander 中。

* [用于 Delphi 的 ATImageBox](https://github.com/Alexey-T/ATViewer/blob/master/Source/ATImageBox.pas)。 `[Delphi]`，[Laz 的 ATImageBox](https://github.com/Alexey-T/ATImageBox-Lazarus)。 `[FPC]` 带有嵌入式 TImage 的 TScrollBox。控件可以自动将图像放置在里面。

* [CEF4Delphi](https://github.com/salvadordf/CEF4Delphi)。 `[Delphi]` `[FPC]` 项目将基于 Chromium 的浏览器嵌入到使用 Delphi 或 Lazarus/FPC 制作的应用程序中

* [WebView4Delphi](https://github.com/salvadordf/WebView4Delphi)。 `[Delphi]` `[FPC]` 项目将基于 Chromium 的浏览器嵌入到使用 Delphi 或 Lazarus/FPC for Windows 制作的应用程序中。


## 其他图形用户界面

* [GMLib](https://code.google.com/p/gmlibrary)（Google 地图库）（似乎已被废弃，GH 上的活跃分叉[此处](https://github.com/bero/GMLibrary) 和[此处](https://github.com/cadetill/gmlib_v1)）。用于 Delphi/C++ Builder 的“[Delphi]”组件，封装了 GoogleMaps API 以管理地图、标记、多边形、矩形、折线等。可以放入地图中的所有对象。

* [VCL 样式实用程序](https://github.com/rruz/vcl-styles-utils)。 `[Delphi]` 类和样式挂钩的集合，用于扩展、修复 QC 报告并向 VCL 样式添加新功能。
// *将现有 VCL 样式引擎提升到新水平的补丁/增强功能集合。 Inno Setup 和 NSIS 的样式也可用。*

* [任务栏列表组件](https://github.com/chaosben/theunknownones/tree/master/Components/TaskBarList)。 `[Delphi]` 一组组件，设计为 Windows 7 任务栏列表接口的 Delphi 包装器（例如 ITaskbarlist3）
// *需要 JVCL*

* [TFireMonkeyContainer](https://github.com/vintgedave/firemonkey-container)。 `[Delphi]` 用于托管 FMX HD 或 3D 表单的 Delphi VCL 组件。这意味着您可以将 FireMonkey (FMX) 表单作为控件嵌入到 VCL 表单中，这样您就可以设计 FMX 表单并在 VCL 应用程序中使用它。

* [PascalSCADA](http://sourceforge.net/projects/pascalscada)。 `[Delphi]` `[FPC]` Delphi/Lazarus 的组件（框架）集，可轻松开发工业应用程序（HMI=人机界面/SCADA=系统控制和数据采集）。它运行在 Windows、Linux 和 FreeBSD 上。

* [适用于 Delphi 的 Windows 功能区框架](https://github.com/turbopack/ribbonframework)。 `[Delphi]` 这个 Delphi 库允许 Delphi 开发人员在他们的 Delphi 应用程序中使用 Windows Ribbon Framework。该库使用本机 Windows 库来实现功能区功能。它不像其他 Delphi 组件集（或 Delphi 的内置 Ribbon 模拟组件）那样模拟 Ribbon 用户界面。

* [DKLang](https://github.com/yktoo/dklang)。 `[Delphi]` DKLang Localization Package 是一组类，旨在简化用 Delphi 编写的应用程序的本地化。

* [GNU Gettext for Delphi、C++ 和 Kylix](https://sourceforge.net/projects/dxgettext/)。 `[Delphi]` 用于 Borland Delphi 和 Borland C++ Builder 的 GNU GetText 翻译工具。

* [OpenWire](https://sourceforge.net/projects/openwireproject)。 `[Delphi]` 该库允许编写高级 VCL 和 FireMonkey 组件，以实现快速无代码应用程序开发。使用该库开发的组件允许使用零行程序代码创建复杂的应用程序。

* [SynTaskDialog](https://github.com/synopse/mORMot/blob/master/SynTaskDialog.pas)。 `[Delphi]` `[FPC]` 实现 TaskDialog 窗口（Vista/7 上原生，XP 上模拟）

* [AnyiQuack](https://github.com/WladiD/AnyiQuack)。 `[Delphi]` 类似 jQuery 的控件动画框架。

* [TLanguages](https://github.com/albertodev01/TLanguages)。用于 VCL 和 FMX 的“[Delphi]”本地化工具。

* [BitMapEditor - Delphi](https://github.com/EverestSoftwareLLC/BitMapEdtior-Delphi)。 `[Delphi]` 用于 Delphi 的单格式、简单位图编辑器。

* [BearLibTerminal](https://github.com/cfyzium/bearlibterminal)。 `[Delphi]` 提供了一个带有字符单元网格的伪终端窗口和一个简单而强大的 API，用于灵活的文本输出和简单的输入处理。
*// 具有 Delphi 绑定的多平台动态库*

* [Dam](https://github.com/digao-dalpiaz/Dam)。 `[Delphi]` `[FPC]` 带有格式化文本的 Delphi 和 Lazarus 消息对话框。

* [Windows 7 任务栏组件](https://delphi.fsprolabs.com/)。 “[Delphi]” Windows 7 中最显着的功能之一是新的 Windows 任务栏。它提供了一种控制桌面、管理窗口和启动应用程序的新方法。

* [GUI AutoSave](https://github.com/GodModeUser/Dephi-LightSaber-GUI_AutoSave) 在应用程序关闭时保存所有 GUI 控件的状态，然后在应用程序启动时恢复它们加载：它可以加载/保存：表单的位置、复选框、单选按钮等

* [FMXTrayIcon](https://github.com/HemulGM/FMXTrayIcon)。用于 FMX Windows 的“[Delphi]” TrayIcon

* [Delphi 的表单设计器组件 (VCL)](https://github.com/havlicekp/form-designer)。 `[Delphi]` 表单设计器 (TFormDesigner) 可用于在运行时设计和修改 Delphi (VCL) 表单。其行为和外观与 Delphi IDE 类似。


## 数据库##

* [ZeosLib](http://sourceforge.net/projects/zeoslib)。 `[Delphi]` `[FPC]` MySQL、PostgreSQL、Interbase、Firebird、MS SQL、Sybase、Oracle 和 SQLite 的数据库组件集。

* [统一Interbase](https://github.com/hgourvest/uib)。 `[Delphi]` 使用 Interbase、FireBird 和 YAFFIL 的组件集。这些组件的诞生是因为需要在多线程环境（例如服务器）中尽可能快地使用 Interbase、FireBird 或 Yaffil。

* [ASQLite](https://github.com/remobjects/ASQLite3)。 “[Delphi]” 来自 aducom 软件的 Delphi SQLite DAC 组件集，基于 Delphi 2009 的最新版本，并进行了更新以支持较新版本的 Delphi（包含在 Delphi 的 RemObjects Data Abstract 中）。

* [TxQuery](https://github.com/ccy/txquery)。 `[Delphi]` TDataSet 后代组件，可用于使用 SQL 语句查询一个或多个 TDataSet 后代组件。它是用Delphi 100%源代码实现的，不需要DLL，因为它实现了自己的SQL语法解析器和SQL引擎。

* [Delphi-ORM](https://github.com/danieleteti/delphi-orm)。用于 Delphi XE2-7 (Win32) 的“[Delphi]”对象关系映射。支持 FirebirdSQL、SQLServer 和 SQLite3。

* [delphimemcache](https://code.google.com/p/delphimemcache)。 `[Delphi]` 为 memcached 实现线程安全客户端。
// *需要 Indy 10*

* [SynDB](https://github.com/synopse/mORMot) ([文档](http://synopse.info/files/html/Synopse%20mORMot%20Framework%20SAD%201.18.html#TITL_126))。 `[Delphi]` `[FPC]` 高性能直接访问 SQLite3、Oracle、MSSQL、PostgreSQL、Firebird、MySQL、ODBC、OleDB，包括远程 HTTP 连接和直接 JSON 支持。

* [SynMongoDB](https://github.com/synopse/mORMot/blob/master/SynMongoDB.pas) ([文档](http://blog.synopse.info/post/2014/05/07/MongoDB-database-access))。 `[Delphi]` `[FPC]` 提供对任何 MongoDB 服务器、其自定义数据类型、JSON 或通过 `TDocVariant` 自定义变体文档存储的直接低级访问。

* [DSharp](https://bitbucket.org/sglienke/dsharp)。 `[Delphi]` 用于在 Delphi 中提供数据绑定的小型库。它不需要特殊的组件来将数据绑定到属性。它还提供依赖注入、MVVM 和更多有趣的实用程序。

* [ghORM](https://github.com/leledumbo/ghORM)。 `[FPC]` 对象关系映射单元通过抽象后端和简单的数据检索（带过滤）、插入和更新来简化 Free Pascal 的数据库访问。

* [tDBF](http://sourceforge.net/p/tdbf/code/HEAD/tree)。 `[Delphi]` `[FPC]` 用于 Delphi、BCB、Kylix、FreePascal 的本机 dBASE III+、dBase IV 和 dBase 2k 数据访问组件。它允许您创建非常紧凑的数据库程序，不需要任何特殊的安装程序。数据库引擎代码直接编译到您的可执行文件中。

* [Redis 客户端](https://github.com/danieleteti/delphiredisclient)。 `[Delphi]` Delphi Redis 客户端版本 2 与 Delphi 10.1 Berlin 及更高版本兼容。警告！如果您使用较旧的 Delphi 版本，则必须使用 [Delphi Redis 客户端版本 1](https://github.com/danieleteti/delphiredisclient/tree/DELPHI_REDIS_CLIENT_VERSION_1)，它适用于 Delphi 10 Seattle、XE8、XE7、XE6 和 XE5（也应适用于旧版本）。该客户端能够发送所有 Redis 命令并使用内部解析器读取响应。

* [QDAC3](http://blog.qdac.cc/?page_id=139) (SVN: svn://www.qdac.cc/QDAC3)。 `[Delphi]` 代表快速数据访问组件。有用的单元，例如 QJson（易于使用的 json 单元）、QWorker（作业交付）等。
// *中文描述和评论，作者英文不好。我自己还没有测试过这个库。*

* [InstantObjects](https://github.com/EtheaDev/InstantObjects)。 `[Delphi]` 用于在 Delphi 中开发面向对象的业务解决方案的集成框架。该框架为开发过程以及为最终应用程序提供动力的引擎提供了基础。 InstantObjects 提供： 通过集成的双向工具在 Delphi IDE 中实现模型；最常见的关系数据库或基于 XML 的平面文件中的对象持久化；通过标准数据感知控件呈现对象。

* [Alcinoe](#general-libraries)。 Firebird/MySQL/SQLite3/Memcached/MongoDb/SphinxQL。

* [SynBigTable](https://github.com/synopse/mORMot/blob/master/SynBigTable.pas)。 `[Delphi]` `[FPC]` 类用于存储大量数据并快速检索。

* [tiOPF](https://github.com/graemeg/tiopf)。 `[Delphi]` `[FPC]` 用 Object Pascal 编写的对象持久框架，用于 Delphi 和 Free Pascal (FPC) 编译器。 tiOPF 简化了面向对象的业务模型到关系数据库的映射。持久层可用于 Firebird、Oracle、MS SQL Server、MySQL、PostgreSQL、SQLite、NexusDB、XML、CSV、TAB、远程（通过 HTTP）等。它还允许您使用您选择的数据库连接组件，如 IBX、dbExpress、DOA、SqlDB、FBLib 等。

* [hcOPF](https://sourceforge.net/projects/larryhengensopf)。 `[Delphi]` 用 Embarcadero 的 Delphi (Object Pascal) 编写的对象持久框架。该值类型框架提供了一个由属性对象组成的基类 (ThcObject)，这些属性对象可以自动保存到对象存储（通常是 RDBMS）。

* [棉花糖](https://bitbucket.org/soundvibe/marshmallow/wiki/Home)。 “[Delphi]”Delphi XE2-7 (Win32) 的对象关系映射受到 .NET micro ORM（主要由 PetaPoco）和 Java Hibernate 的启发。由 Linas Naginionis 开发。支持 SQLite、Sybase ASA、SQL Server、Firebird、Oracle、MySQL、PostgreSQL、MongoDB。使用 [Spring](http://code.google.com/p/delphi-spring-framework/) 框架。正在积极开发中。

* [DelphiCassandra](https://github.com/grijjy/DelphiCassandra)。 `[Delphi]` 用于与 Cassandra 数据库通信的 Delphi 驱动程序类。

* [DelphiCouchbase](https://github.com/grijjy/DelphiCouchbase)。 `[Delphi]` Delphi 驱动程序类与 Couchbase 数据库通信。

* [DelphiMongoDB](https://github.com/grijjy/DelphiMongoDB)。 `[Delphi]` Delphi 驱动程序类与 MongoDB 数据库通信。

* [QuickORM](https://github.com/exilon/QuickORM)。 `[Delphi]` `[FPC]` QuickORM 是一个基于 mORMot 框架的简单 RestServer 和 Restclient。在几分钟内提供客户端-服务器应用程序的快速实施。

* [iORM](https://github.com/mauriziodm/iORM)。 `[Delphi]` 基于 Delphi ORM 接口，可用于开发桌面和移动应用程序。

* [d-ORModel](https://github.com/ultraware/d-ORModel)。用于 Delphi 的“[Delphi]” ORM，基于模型和对象字段。 LINQ 支持、完全类型化和编译时检查。

* [Trysil](https://github.com/davidlastrucci/Trysil)。用于 Delphi 的“[Delphi]” ORM（对象关系映射）。支持 SQLServer、FirebirdSQL 和 SQLite。

* [用于 Delphi 和 FreePascal/Lazarus 的 SQLite](https://github.com/plashenkov/SQLite3-Delphi-FPC)。 `[Delphi]` `[FPC]` Delphi 和 FreePascal/Lazarus 的完整 SQLite3 API 翻译，以及一个简单的支持 Unicode 的对象包装器，以简化该数据库引擎的使用。

* [Delphi 的粗体](https://github.com/bero/BoldForDelphi)。 `[Delphi]` 模型驱动架构 (MDA) 框架和 ORM。在 UML 中设计域模型并生成 Delphi 类和数据库模式。具有用于查询和派生属性的 OCL（对象约束语言）、自动 UI 同步、内置撤消/重做、乐观锁定和对象订阅。通过 FireDAC、UniDAC 或 XML 进行持久化，支持大多数现代数据库。该分支添加了 Unicode 和现代 Delphi 支持。 [官方 Embarcadero 存储库](https://github.com/Embarcadero/BoldForDelphi) 适用于 Delphi 7。


## 脚本编写##

*在您的应用程序中使用脚本引擎*

* [Pascal 脚本](https://github.com/remobjects/pascalscript)。 `[Delphi]` `[FPC]` 免费脚本引擎，允许您在运行时在 Delphi 或 Free Pascal 项目中使用大多数 Object Pascal 语言。它完全用 Delphi 编写，由一组可以编译成可执行文件的单元组成，无需分发任何外部文件。 Pascal Script 最初是为了需要一个良好的工作脚本，而当时没有可用的脚本。

* [DWScript](https://bitbucket.org/egrange/dwscript)。 `[Delphi]` 基于 Delphi 语言的 Delphi 面向对象脚本引擎，具有借用其他 Pascal 语言（FreePascal、Prism 等）的扩展。它还引入了一些自己的 Pascal 语言扩展。

* [Delphi-JavaScript](https://code.google.com/p/delphi-javascript)。 `[Delphi]` 用于 delphi 的 JavaScript 引擎，基于 Mozilla 的 Spidermonkey。
// *需要Spidermonkey DLL*

* [布莱斯](http://sourceforge.net/projects/blaise)。 `[Delphi]` 开源面向对象脚本语言。语言特点：面向对象；统一码支持；可选类型，即动态或静态类型；文字丰富；高级数学支持，例如复数、有理数和矩阵；虚拟机架构；协同例程；熟悉的语言语法，受 Object Pascal、Python 和 Ada 的影响。

* [SpiderMonkey](https://github.com/synopse/mORMot/blob/master/SynSM.pas)。 `[Delphi]` `[FPC]` 绑定 Mozilla JavaScript 引擎，包括 JIT 和多线程，可通过 Delphi 变体轻松访问对象。
// *需要Spidermonkey DLL*

* [贝森](https://github.com/BeRo1985/besen)。 `[Delphi]` `[FPC]` 在 Object Pascal 中完成 ECMAScript 第五版实现，可与 Delphi >=7 和 Free Pascal >= 2.5.1（也可能是 2.4.1）编译。

* [Python for Delphi (P4D)](https://github.com/pyscripter/python4delphi)。 `[Delphi]` `[FPC]` 一组免费组件，将 Python dll 封装到 Delphi 和 Lazarus (FPC) 中。它们可让您轻松执行 Python 脚本、创建新的 Python 模块和新的 Python 类型。您可以将 Python 扩展创建为 dll 等

* [CrystalLUA](https://github.com/d-mozulyov/CrystalLUA)。 `[Delphi]` Lua 绑定 (Delphi6-2007)。
// *需要 LUA DLL*

* [lua4delphi](https://github.com/danieleteti/lua4delphi)。 `[Delphi]` Lua 5.1 语言的 Delphi 绑定。
// *需要 LUA DLL*

* [chakracore-delphi](https://github.com/tondrej/chakracore-delphi)。 `[Delphi]` `[FPC]` 用于 Microsoft ChakraCore JavaScript 引擎库的 Delphi 和 Free Pascal 绑定和类。

* [VerySimple.Lua](https://github.com/Dennis1000/verysimplelua)。用于 Delphi XE5-D10.1 的“[Delphi]” Lua 包装器，自动为 Delphi <-> Lua 创建 OOP 回调函数。
// *需要 LUA DLL*

* [QuickJS-Engine](https://github.com/Coldzer0/QuickJS-Pascal)。 `[Delphi]` `[FPC]` 用于 Bellard 的 [QuickJS](https://bellard.org/quickjs) JavaScript 引擎的 Delphi 和 Free Pascal 绑定。

* [钍](https://github.com/horazont/thorium)。 `[Delphi]` `[FPC]` 用 FreePascal 编写的强大的嵌入式脚本语言。它具有可插入的编译器和打字系统，并且可以使用 RTTI 轻松快速地导入主机类。它还允许调用主机方法和函数，而无需包装函数，从而节省开发人员（即您）编写这些方法和函数的时间。

* [JvInterpreter（JEDI VCL 项目的一部分）](https://github.com/project-jedi/jvcl)。 `[Delphi]` `[FPC]` Pascal 脚本解释器


## 机器学习##

*机器学习和神经网络*

* [noe](https://github.com/ariaghora/noe)。 “[FPC]”框架用于在纯对象 pascal 中构建神经网络。

* [Keras4Delphi](https://github.com/Pigrecos/Keras4Delphi)。 `[Delphi]` 高级神经网络 API，使用 Pascal 和 Python 绑定编写

* [Marvin.IA](https://github.com/marvinbraga/Marvin.IA)。 `[Delphi]` 面向对象的 Pascal 原语的机器学习集合（仅接口和类）。

* [CAI 神经 API](https://github.com/joaopauloschuler/neural-api)。 `[FPC]` 基于 Pascal 的深度学习神经网络 API，针对 AVX、AVX2 和 AVX512 指令集以及支持 OpenCL 的设备（包括 AMD、Intel 和 NVIDIA）进行了优化。该API已在Windows和Linux下进行了测试。

* [TensorFlow.Delphi](https://github.com/Pigrecos/TensorFlow.Delphi)。 `[Delphi]` [TensorFlow](https://tensorflow.org) Delphi 库绑定。它的目标是在 Delphi 中实现完整的 Tensorflow API，允许 Pascal 开发人员使用 Pascal Delphi 开发、训练和部署机器学习模型

* [提升](https://github.com/inversed-ru/Ascension)。 `[Delphi]` `[FPC]` 旨在开发通用全局优化框架的研究计划。其核心组件是称为元启发式的智能算法，适用于各种优化问题。

* [sherpa-onnx](https://github.com/k2-fsa/sherpa-onnx)。 `[Delphi]` `[FPC]` 语音转文本、文本转语音、说话者二值化、语音增强、源分离和 VAD，使用下一代 Kaldi 和 onnxruntime，无需互联网连接。支持嵌入式系统、Android、iOS、HarmonyOS、Raspberry Pi、RISC-V、RK NPU、Ascend NPU、x86_64服务器、websocket服务器/客户端，支持12种编程语言


## 非可视类/实用程序##


## 压缩

* [FWZip](https://github.com/AlexanderBagel/FWZip)。 `[Delphi]` 使用 Store 和 Deflate 方法处理 Zip 档案的类，支持 ZIP64、DataDescryptors、PKWARE 加密、NTFS 属性、文件名中的 Utf8。
// *使用普通的 ZLIB.obj 并编译成二进制文件。俄语评论和描述。*

* [Abbrevia](http://sourceforge.net/p/tpabbrevia)（[最新](https://github.com/TurboPack/Abbrevia) 和仅针对最新编译器版本的维护版本）。 `[Delphi]` 用于 Delphi 和 C++Builder 的高级数据压缩工具包。支持 PKZIP、Microsoft CAB、tar、gzip 和 bzip2 存档，并可以创建自解压可执行文件。在 Windows 上，它还为 LZMA、Bzip2 和 WavPack SDK 以及 PPMd 解压缩提供 Delphi 包装器。 Abbrvia 还有几个可视化控件可以简化档案的显示和操作，包括树视图和列表视图组件。特点：所有存档格式的 Unicode 文件名；解压缩大多数 .zipx 和旧版 (PKZIP v1) zip； ZIP64 支持大于 2GB 的档案；跨区和分割 zip 档案；跨平台（Windows、OS X 和 Linux）；无需 DLL；包含COM组件；丰富的文档
// *第二个链接指向最新编译器版本的改编版本。*

* [SynLZ SynLZO SynZip PasZip](https://github.com/synopse/mORMot)。 `[Delphi]` `[FPC]` 几个高速压缩单元，具有 ZIP/LZ77 Deflate/Inflate、LZO 和 SynLZ 算法，采用 pascal 和优化的汇编程序。

* [Delphi zlib](http://www.base2ti.com/?id=delphi.zlib)。 `[Delphi]` zlib.obj 的包装器最初由 Borland 使用。 Delphi 最高支持 XE3。

* [DIUcl](http://www.yunqa.de/delphi/products/ucl/index)。 `[Delphi]` DIUcl 是一个无损压缩库，具有极快且小型（仅 200 字节！）ASM 解压缩器。压缩时间和比率与 deflate/zip 和 bzip2 类似。流行的 UCL 压缩库的 Delphi 端口，流行且众所周知的 UPX Ultimate Packer for eXecutables 也使用该库。


## 加密

* [Delphi 加密纲要 (DEC)](https://github.com/MHumm/DelphiEncryptionCompendium)。 `[Delphi]` `[FPC]` Delphi 和 C++ Builder 的加密库。对称加密函数：Blowfish、Twofish、IDEA、Cast128、Cast256、Mars、RC2、RC4、RC5、RC6、Rijndael / AES、Square、SCOP、Sapphire、1DES、2DES、3DES、2DDES、3DDES、3TDES、3Way、Gost、Misty、NewDES、Q128、SAFER、Shark、鲣鱼、茶、TEAN；分组密码操作模式：CTSx、CBCx、CFB8、CFBx、OFB8、OFBx、CFSx、ECBx、GCM；哈希值：MD2、MD4、MD5、RipeMD128、RipeMD160、RipeMD256、RipeMD320、SHA、SHA1、SHA224、SHA256、SHA384、SHA512、SHA3-224、SHA3-256、SHA3-384、SHA3-512、Shake128、Shake256、哈弗128、哈弗160、哈弗192、哈弗224、哈弗256、老虎、巴拿马、惠而浦、惠而浦1、惠而浦T、方形、Snefru128、Snefru256、蓝宝石。

* [LockBox](http://sourceforge.net/projects/tplockbox)（[最新](https://github.com/TurboPack/LockBox3) 和仅针对最新编译器版本的维护版本）。 `[Delphi]` Delphi 密码学库。目前支持Delphi XE6。它支持 AES、DES、3DES、Blowfish、Twofish、SHA2（包括新的 SHA-512/224 和 SHA-512/256）、MD5； ECB、CBC、CFB8、CFB、CTR、ECB、OFB、PCBC 链接模式、RSA 数字签名和验证。具有 OpenSSL 库的接口。
// *也请查看 [this](https://github.com/jarto/lockbox2) 页面以及替代版本。*

* [SynCrypto](https://github.com/synopse/mORMot/blob/master/SynCrypto.pas)。 `[Delphi]` `[FPC]` 快速加密例程（散列和密码），实现 AES、XOR、RC4、ADLER32、MD5、SHA1、SHA256 算法，优化速度（调整汇编器和 VIA PADLOCK 可选支持）。

* [TForge](https://github.com/sergworks/tforge)（似乎已废弃，[较新的 fork](https://github.com/ElminsterAU/tforge)）。 `[Delphi]` `[FPC]` 用 Delphi 编写的开源加密库，与 Free Pascal 编译器兼容。 MD5、SHA1、SHA256、CRC32、Jenkins 一次一次、HMAC、PBKDF1、PBKDF2、AES、DES、RC4、RC5、Salsa20。
// *代码位于 `porting` 分支*

* [Spring4D](#general-libraries)。 CRC、DES、MD5、SHA

* [基础代码库](#general-libraries)。哈希：XOR、CRC、Adler、MD5、SHA、安全密钥 MD5/SHA 等；密码：AES、DES、FUNE、RC2/4、RSA。

* [Alcinoe](#general-libraries)。 AES、Blowfish、MD5、SHA、安全密钥 MD5/SHA。

* [DCPcrypt (fork #1)](https://sourceforge.net/projects/dcpcrypt), [DCPcrypt (fork #2)](https://github.com/evpobr/DcpCrypt2)。 `[Delphi]` Delphi 的加密组件套件。

* [bcrypt](https://github.com/viniciussanchez/bcrypt)。 `[Delphi]` 一个帮助您散列密码的库。

* [MurMur-Delphi](https://github.com/thibmo/murmur-delphi)。 `[Delphi]` MurMur1/2/3 快速种子哈希算法以纯 Pascal 移植。

* [HashLib4Pascal](https://github.com/Xor-el/HashLib4Pascal)。 `[Delphi]` `[FPC]` Object Pascal 哈希库在宽松的 MIT 许可证下发布，它提供了一个易于使用的界面来计算数据的哈希值和校验和。它还支持基于状态（增量）的哈希。 CRC、Adler、Murmur、Jenkins、MD5、SHA、Blake 等等。

* [SimpleBaseLib4Pascal](https://github.com/Xor-el/SimpleBaseLib4Pascal)。 `[Delphi]` `[FPC]` 用于 Delphi/FreePascal 编译器的简单使用的 Base Encoding Package，目前提供对各种 Base 编码和解码的支持，例如 Base16、Base32（各种变体）、Base58（各种变体）、Base64（各种变体）和 Base85（各种变体）。

* [CryptoLib4Pascal](https://github.com/Xor-el/CryptoLib4Pascal)。 `[Delphi]` `[FPC]` Object Pascal 加密库在宽松的 MIT 许可证下发布。密码：AES（128、192 和 256）、Rijndael、Blowfish、Speck、ChaCha、(X)Salsa20、DSA、(DET)ECDSA（支持的曲线：NIST、X9.62、SEC2、Brainpool）、ECNR、ECSchnorr、EdDSA（Ed25519、Ed25519Blake2B）

* [RHash 的 Pascal 包装器](https://github.com/jackdp/LibRHash4P)。 `[Delphi]` `[FPC]` RHash 是一个控制台应用程序，用于计算各种校验和哈希和，包括 CRC32、CRC32C、MD4、MD5、SHA1、SHA256、SHA512、SHA3、AICH、ED2K、DC++ TTH、BitTorrent BTIH、Tiger、GOST R 34.11-94、GOST R 34.11-2012、RIPEMD-160、HAS-160、EDON-R 和惠而浦。 RHash 是用 C 语言编写的，速度非常快。 LibRHash是一个“驱动”RHash的库，可以编译成单独的DLL或SO库文件。

## XML/JSON/YAML/HTML

* [数据集序列化](https://github.com/viniciussanchez/dataset-serialize)。 `[Delphi]` `[FPC]` 该组件是 DataSet 组件的 JSON 序列化器。允许您将 JSON 转换为 DataSet、将 DataSet 转换为 JSON，以及以 JSON 格式导出和加载 DataSet 字段的结构。兼容VCL项目、FMX和uniGUI（框架）。

* [OmniXML](https://github.com/mremec/omnixml)。 `[Delphi]` 用 Delphi 编写的 XML 解析器。全面支持文档对象模型（DOM）Level 1规范；支持可扩展标记语言（XML）1.0（第二版）规范；内置对不同代码页的支持（主要8位代码页、UTF-8、UTF-16）；与MS XML解析器兼容；快速解析大型且高度结构化的文档；包括帮助函数以简化 XML 文档的处理；简化的 XPath 支持。

* [SAX for Pascal](http://sourceforge.net/projects/saxforpascal)。 `[Delphi]` `[FPC]` 设计用于在 Pascal/Delphi 中实现用于 XML 解析的简单 API。
// *基于回调的 XML 解析器，对于处理巨大的 XML 流很有用。自 2004 年起就被废弃，但几乎是唯一可用的 SAX 实现。*

* [KDS XML](http://sourceforge.net/projects/kdsxml)。用于流式解析、验证和生成 XML 的“[Delphi]”类库。它是用 Object Pascal/Delphi 编写的，可在 Win32 (Delphi) 和 Linux (Kylix) 上运行。它的一部分取决于 SAX for Pascal 接口规范。
// *看起来死了。*

* [XML 合作伙伴](http://sourceforge.net/projects/tpxmlpartner)。 `[Delphi]` 通过本机、易于使用的 VCL 和 CLX 组件，帮助将 XML 的强大功能添加到 Borland Delphi、C++ Builder 和 Kylix 项目中。这些强大的组件简化了创建、修改和解析 XML 数据文档的过程。
// *似乎已死，请查看 [this](http://www.songbeamer.com/delphi) 页面以获取可能更新的版本。*

* [打开 XML](http://www.philo.de/xml/downloads.shtml)。 `[Delphi]` 提供了广泛的方法、组件和基础类。它可用于 Win32/Kylix 以及 .NET 开发。

* [超级对象](https://github.com/hgourvest/superobject)。 `[Delphi]` `[FPC]` JSON 数据格式的解析器/编写器。该工具包设计用于与 Delphi 和 FreePascal（win32、win64、linux32、linux64、macOS Intel）配合使用。还支持读/写 XML。

* [用于 pascal 的 Libxml2](https://sourceforge.net/projects/libxml2-pas)。 `[Delphi]` `[FPC]` Pascal 单元访问 Daniel Veillard 流行的 XML API。这至少应该可以从 Kylix 和 Delphi 中使用，但希望也可以从其他 Pascal 编译器（如 freepascal）中使用。

* [NativeXml](https://code.google.com/p/simdesign)。 `[Delphi]` 该组件包含一个占用空间较小的 Object Pascal (Delphi) XML 实现，允许读取和写入 XML 文档。您基本上只需要一个单位，只需将其添加到“uses”子句即可。您可以使用该软件从文件、流或字符串中读取 XML 文档。加载例程生成可用于动态显示加载进度的事件。您还可以使用它来创建和保存 XML 文档。

* [Delphi-XmlLite](https://github.com/the-Arioch/Delphi-XmlLite)。 Microsoft XmlLite 的“[Delphi]”标头翻译。 XmlLite 是 .NET XmlReader+Writer 的本机 C++ 实现，用于基于流的、只进的 XML 解析和创建。需要 XmlLite.dll。它包含在所有新版本的 Windows 以及旧版本的服务包中。 XmlReader 的基于拉取的接口比 SAX 的基于事件的接口更易于使用。
// *似乎被遗弃并报告有些问题。*

* [嵌合体](https://bitbucket.org/sivv/chimera)。 Delphi XE2 的“[Delphi]”开源（MIT 许可证）库，它在一个不错的许可证下提供了一个快速且跨平台的 JSON 生成器/解析器（序列化器/反序列化器）。

* [SynCommons](https://github.com/synopse/mORMot/blob/master/SynCommons.pas)。 `[Delphi]` `[FPC]` 高速 JSON 库，使用 `TDocVariant` 自定义变体类型进行存储和访问。

* [SynCrossPlatformJSON](https://github.com/synopse/mORMot/blob/master/CrossPlatform/SynCrossPlatformJSON.pas)。 `[Delphi]` `[FPC]` 高速跨平台 JSON 库，使用 `TJSONVariant` 自定义变体类型进行存储和访问。

* [Json 数据对象](https://github.com/ahausladen/JsonDataObjects)。 `[Delphi]` 该 Delphi 单元包含一个 JSON 解析器，支持 Delphi 2009-10Seattle 以及 Win32、Win64 和 ARM Android 平台（MacOS 和 iOS 可能适用）。

* [TinyJSON](http://sourceforge.net/projects/tiny-json) ([GH 镜像](https://github.com/tmcdos/tiny-json))。 `[Delphi]` 这是一个小而干净的库，用于具有布尔/整数/浮点/宽字符串值的关联数组。允许从 JSON 文本导入（导出）。广泛的错误检查。使用 FunHash（由 Sokolov Yura 开发）、HatTrie（由 Daniel C. Jones 开发）、FastInt64 和 FastMove（由 FastCode 项目开发）。

* [JSON delphi 库](http://sourceforge.net/projects/lkjson)。 `[Delphi]` 这是一个实现 JSON 数据格式和对象结构的 delphi 库。轻量且快速。

* [dwsJSON](https://bitbucket.org/egrange/dwscript/src/b9f99d4b8187defac3f3713e2ae0f7b83b63d516/Source/dwsJSON.pas?at=master)。 `[Delphi]` `[FPC]` dwsJSON 是一个支持 JSON 解析/创建的单元，它是 DWScript 的一部分，但相对“独立”，因为如果您将它添加到 Delphi（或 FPC）项目中，它不会拉动整个 DWScript 库，因此可以在您需要的任何地方使用。

* [基础代码库](#general-libraries)。 JSON、XML。

* [Alcinoe](#general-libraries)。 XML/JSON 解析器。

* [delphi-yaml](https://github.com/ashumkin/delphi-yaml)。 `[Delphi]` Delphi 7 兼容 libyaml、YAML 解析器和用 C 实现的发射器库的绑定。提出了四层绑定。

* [GrijjyFoundation](#general-libraries)。 JSON/BSON。

* [VerySimpleXML](https://github.com/Dennis1000/verysimplexml)。 `[Delphi]` 用于 Delphi 2010 - 10.2.2 Tokyo 的轻量级、单一单元、跨平台 XML 读取器/编写器

* [XSuperObject](https://github.com/onryldz/x-superobject)。 `[Delphi]` Delphi 跨平台快速 JSON

* [互联网工具](https://github.com/benibela/internettools)。 `[Delphi]` `[FPC]` 包提供标准一致的 XPath 2.0、XQuery 1.0 和 XPath/XQuery 3.0 解释器，以及 JSONiq、模式匹配、CSS 和 HTML 等扩展；以及在 Windows/Linux/macOS/Android 上执行 HTTP/S 请求的函数、受 XSLT 启发的网页抓取语言和自动更新类。

* [Delphi-JsonToDelphiClass](https://github.com/PKGeorgiev/Delphi-JsonToDelphiClass) ([Newer fork](https://github.com/JensBorrisholt/Delphi-JsonToDelphiClass)。`[Delphi]`基于 JSON 字符串生成 Delphi 类（Json 到 Delphi 类生成器/JSON 数据绑定工具）。还包括与 GitHub 交互的单元。

* [XML 解析器](http://www.destructor.de/xmlparser)。 `[Delphi]` `[FPC]` 用于 Delphi 和 FreePascal 的轻量级 ObjectPascal XML 解析器。通过省略语法检查、格式良好检查和/或验证，并选择渐进式扫描技术，该解析器速度非常快。

* [HTML 解析器](https://github.com/ying32/htmlparser)。 `[Delphi]` HTML 解析器。支持Windows、macOS、iOS、Android平台。中文评论

* [Neslib](https://github.com/neslib/Neslib.Xml)。 `[Delphi]` 用于 Delphi 的超轻量级跨平台 XML 库。

* [DJSON](https://github.com/mauriziodm/DJSON)。 `[Delphi]` Delphi JSON 对象映射器

* [fast-html-parser](https://github.com/z505/fast-html-parser)。 `[Delphi]` `[FPC]` 快速 HTML 解析器

* [THTMLWriter](https://github.com/NickHodges/delphihtmlwriter)。 `[Delphi]` 类库使开发人员能够创建 HTML 和 HTML 文档。它使用流畅的界面使创建 HTML 文本变得简单自然。

* [霓虹灯](https://github.com/paolo-rossi/delphi-neon)。 `[Delphi]` Delphi 序列化库可帮助您将对象和其他值（来回）转换为 JSON。它支持简单的 Delphi 类型，也支持复杂的类和记录。 Neon 的设计考虑了 REST，可以在没有“元数据”或添加字段的应用程序之间交换纯数据

* [YAML/JSON 解析器工具](https://github.com/biot2/Yaml.Json.Parser)。 `[Delphi]` `[FPC]` YAML 和 JSON 解析器、序列化器和反序列化器，具有 YAML 到 JSON 的转换工具，反之亦然，包含用于 Delphi 和 Lazarus 的纯 Object Pascal 源代码

* [动态数据对象](https://github.com/SeanSolberg/DynamicDataObjects)。 `[Delphi]` 类库，可让您对结构化数据进行建模并与各种数据序列化格式进行序列化，例如：CBOR、JSON、MessagePack、ION、UBJSON、BSON、Smile、DataObj、CSV、ICS、BinaryJData 等。

## 语言

*Pascal 和其他语言的工具*

* [下一个 Delphi Yacc 和 Lex](https://github.com/RomanYankovsky/ndyacclex)。用于 Delphi 的“[Delphi]”解析器生成器工具集。

* [抽象语法树生成器](https://github.com/RomanYankovsky/DelphiAST)。 `[Delphi]` 使用 DelphiAST，您可以获取真正的 Delphi 代码并获得抽象语法树。一次一个单元，但没有符号表。

* [Castalia-Delphi-Parser](https://github.com/jacobthurman/Castalia-Delphi-Parser)。 `[Delphi]` 这些文件构成了一个针对 Object Pascal 方言（称为“Delphi”）的手​​写高速解析器。最初的工作是由 Martin Waldenburg 在 20 世纪 90 年代末完成的，该项目在 2003 年之前被放弃，当时我找到了代码并开始研究它。  我根据需要对其进行了更新，以配合我的项目“Castalia”。

* [CrossPascal](https://github.com/BeRo1985/crosspascal)。 `[Delphi]` 旨在成为一个兼容 Delphi 7 的跨平台源到源编译器（与 XE3 中的新 unicode 字符串类型一起使用，但 ansistring 仍然是默认字符串类型，以便仍然与 Delphi 7 兼容），它生成中间 C 代码。
// *非常有趣的项目，尽管似乎被放弃了*

* [pas2js](https://gitlab.com/freepascal.org/fpc/pas2js)，[文档](http://wiki.freepascal.org/pas2js)。 `[Delphi]` `[FPC]` 一个开源 Pascal 到 JavaScript 转译器。它解析 Object Pascal 并发出 JavaScript。 JavaScript 当前的级别为 ECMAScript 5，应该在任何浏览器或 Node.js（目标“nodejs”）中运行。基本上支持Delphi 7语法。用于 TMS WebCore 和 Elevate Web Builder 等工具。


## 内存管理器

*实现动态内存分配的库*

* [FastMM](https://github.com/pleriche/FastMM4)。 “[Delphi]” Embarcadero Delphi Win32 和 Win64 应用程序的快速替代内存管理器，不易产生内存碎片，并且支持共享内存，无需使用外部 .DLL 文件。
// *自 2006 年起用作库存内存管理器，但采用简化版本。提供强大的内存泄漏/损坏检测工具。*

* [ScaleMM](https://github.com/andremussche/scalemm)。 `[Delphi]` Delphi 的快速扩展内存管理器

* [BrainMM](https://github.com/d-mozulyov/BrainMM)。 `[Delphi]` Delphi 的极快内存管理器。
// *高级内存分配函数可实现更快的对齐操作。*

* [FastMM4-AVX](https://github.com/maximmasiutin/FastMM4-AVX)。 `[Delphi]` `[FPC]` FastMM4 分支，具有 AVX 支持和多线程增强功能（更快的锁定）

* [FastMM5](https://github.com/pleriche/FastMM5)。 “[Delphi]” Embarcadero Delphi 应用程序的快速替代内存管理器，可在多个线程和 CPU 内核之间良好扩展，不易产生内存碎片，并且支持共享内存，无需使用外部 .DLL 文件。版本 5 完全重写了 FastMM。

* [Delphi64RTL](https://github.com/RDP1974/Delphi64RTL)。来自英特尔集成性能基元和英特尔线程构建模块免版税软件包的“[Delphi]”对象 Pascal 包装器。包括无锁可扩展分配器、支持 simd 的 RTL 子集例程（内存填充、复制、比较）和加速 zlib 压缩
// *使用英特尔 DLL 来加速低级内存操作*


## 系统

*低级辅助工具：内存、线程等*

* [OmniThreadLibrary](https://github.com/gabr42/OmniThreadLibrary)。 `[Delphi]` 简单易用的 Delphi 线程库。
// *在您的应用程序中轻松集成异步流程*

* [Delphi Detours 库](https://github.com/mahdisafsafi/delphi-detours-library)。 `[Delphi]` `[FPC]` 库允许您挂钩 Delphi 函数和对象方法以及 Windows API 函数。它提供了一种插入和移除挂钩的简单方法。
// *支持x64，调用原始函数，多钩子，COM/Interfaces/win32api，对象方法钩子，完全线程安全，Delphi 7/2005-2010/XE-XE7 & Lazarus/FPC，支持64位地址。*

* [MemoryModule](https://github.com/Fr0sT-Brutal/Delphi_MemoryModule)。 `[Delphi]` `[FPC]` 使用 MemoryModule 引擎，您可以将所有必需的 DLL 存储在二进制文件中以保持其独立性。额外的钩子单元允许透明地使用 MM 引擎，从而允许切换 MM/WinAPI 加载以及启用不知道 MM 的第 3 方动态加载 DLL 接口（使用 Interbase Express 组件和 Firebird 客户端库进行测试）。 MemoryModule 是 Joachim Bauch 的 C MemoryModule 的 Pascal 移植。

* [DirectoryWatcher](https://github.com/Wosi/DirectoryWatcher)。 `[Delphi]` 观察不同平台（Windows/Linux/Mac OS）上目录的变化。

* [ezthreads](https://github.com/mr-highball/ezthreads)。 `[FPC]` 简单易用的线程库

* [AsyncCalls](https://github.com/ahausladen/AsyncCalls)。 `[Delphi]` 异步函数调用框架

* [存储访问框架SAF](https://github.com/emozgun/delphi-android-SAF)。 `[Delphi]` Android 作用域存储：存储访问框架 SAF API


## 模板

*基于模板生成文本输出的引擎*

* [SynMustache](https://github.com/synopse/dmustache)。 `[Delphi]` `[FPC]` Mustache 模板语言的 Delphi 实现，支持 Delphi 6 到 Delphi 10 Seattle（以及 FPC/Lazarus 编译）。

* [Delphi 模板引擎](http://sourceforge.net/projects/delphi-templeng)。 `[Delphi]` 模板引擎设计为在 Delphi（主要是 Delphi 7）应用程序中用作库，允许开发人员在其软件上使用模板，而无需担心实现它。

* [MustaPAS](https://github.com/leledumbo/mustapas)。 `[Delphi]` `[FPC]` 简单程序 Pascal 中的 Mustache 实现。

* [Sempare 模板引擎](https://github.com/sempare/sempare-delphi-template-engine)。 `[Delphi]` 模板引擎允许灵活的文本操作。它可以用于生成电子邮件、html、源代码、xml、配置等。它非常易于使用、灵活且可扩展，模板可读且可维护。它支持：条件、循环、自定义函数和通过 RTTI 引用数据。 XE4、XE8+

* [DVD首席模板引擎](https://github.com/Fr0sT-Brutal/TemplateEngine)。 `[Delphi]` `[FPC]` 由 [DVD Chief](http://dvdchief.com/delphi) 放弃的 Delphi PHP Smarty 模板引擎实现的分支。

* [liquid-delphi](https://github.com/arimateia/liquid-delphi)。 `[Delphi]` 流行的 [Ruby Liquid 模板语言](https://shopify.github.io/liquid) 的 Delphi 端口和 dotLiquid 实现。它是一个独立的项目，旨在保留与原始模板语法相同的模板语法，同时尽可能使用 delphi 编码约定。

* [免费 Pascal 的简单模板引擎](https://github.com/sash-rc/ste)。 `[FPC]` 快速引擎，用于生成带有 Object/Free Pascal 中的标签/变量的文本（html、xml 或任何标记）（可能与 delphi 兼容）。 IF/ELSE 块。 FOR 块（数据集迭代）。每个标签的回调。嵌套块。

## 记录

* [Log4d](https://github.com/landrix/Log4d-for-Delphi)。 `[Delphi]` `[FPC]` 基于 Log4j 的 Delphi 日志系统实现。

* [TraceTool](http://tracetool.sourceforge.net/)。 `[Delphi]` C#、C++、Delphi、ActiveX 和 Java 跟踪框架和跟踪查看器。

* [LoggerPro](https://github.com/danieleteti/loggerpro)。 `[Delphi]` Delphi 的现代且可插入的日志框架。

* [SynLog](https://github.com/synopse/mORMot/blob/master/SynLog.pas)。 `[Delphi]` `[FPC]` Synopse 项目使用的日志记录函数。

* [slf4p](https://github.com/michaelJustin/slf4p)。 `[Delphi]` `[FPC]` 一个简单的日志外观，支持 LazLogger、Log4D 和其他日志框架。

* [GrijjyCloudLogger](https://github.com/grijjy/GrijjyCloudLogger)。 `[Delphi]` 远程日志记录工具，允许您通过 Intranet 或 Internet 从 Windows、Linux、iOS、Android 和 macOS 设备向在 Windows 上运行的查看器发送日志消息。除了发送消息和任何数据之外，它还具有许多功能，包括自定义实时监视、对象的远程实时视图、跟踪实时内存使用情况、对象分配、增长泄漏等等。

* [QuickLogger](https://github.com/exilon/QuickLogger)。 `[Delphi]` `[FPC]` Delphi/freepascal/.NET (Windows/Linux) 库，用于记录文件、控制台、内存、电子邮件、休息、电报、slack、事件日志、redis、ide 调试消息和抛出事件。

* [jachLog](https://github.com/jachguate/jachLogMgr)。 `[Delphi]` 纯 pascal、灵活、可扩展且轻量级的库，可为您的 Delphi 应用程序添加日志记录功能。支持多个日志目的地。该库支持多线程应用程序，并且本身是多线程的，以最大限度地减少写入日志对关键任务应用程序性能的影响。

* [LogLib](https://github.com/GabrielOnDelphi/Delphi-LightSaber-LogLib)。 `[Delphi]` 一个简单但有效的可视化日志控制/库。程序员可以从代码中的任何位置向日志窗口发送消息。日志窗口可以设置为在收到错误消息时自动弹出。根据所选的日志详细级别（请参阅详细属性），是否显示低级别消息（如详细/调试消息）。包含： 非可视日志 (TRamLog) 可视日志 (TRichLog)

* [简单记录器](https://github.com/paweld/simple-logger)。 `[FPC]` 用于 FPC/Lazarus 的简单、线程安全记录器。日志保存到文件，支持日志归档和压缩。

* [MultiLog4D](https://github.com/adrianosantostreina/MultiLog4D)。 `[Delphi]` MultiLog4D 是一个库，旨在促进和加速向 Android、iOS、Windows、macOS 和 Linux 发送日志。只需一行代码，就可以发送一条消息，该消息将在相应平台上看到和监控，例如 Android 上的 adb logcat 或 Linux 上的 syslog。

## 数学

* [大十进制数学](https://github.com/benibela/bigdecimalmath)。 `[Delphi]` 该单元提供任意精度的 BCD 浮点数类型。它可以像任何数字类型一样使用，并支持：至少 10-2147483647 到 102147483647 之间的数字，十进制数字精度为 2147483647；所有标准算术和比较运算符；舍入函数（floor、ceil、to-even、..）；一些更高级的操作，例如功率和开方。

* [TIntX](https://github.com/Xor-el/IntXLib4Pascal)。 `[Delphi]` `[FPC]` IntX 任意精度整数库的 Pascal 端口，具有快速、大约 O(N * log N) 乘法/除法算法实现。它提供了整数上的所有基本算术运算、比较、按位移位等。它还允许解析不同基数的数字并将其转换为字符串（也可以是任何基数）。该库的优点是其快速乘法、除法和基数/基数转换算法。所有快速版本的算法都基于使用快速 Hartley 变换的大整数的快速乘法，该变换的运行时间为 O(N * log N * log log N) 时间，而不是经典的 O(N^2)。

* [DelphiBigNumberXLib](https://github.com/Xor-el/DelphiBigNumberXLib)。 `[Delphi]` 用于 Delphi 的任意精度库，支持整数和浮点计算。

* [FastMath](https://github.com/neslib/FastMath)。 `[Delphi]` Delphi 数学库针对快速性能进行了优化（有时以不执行错误检查或损失一点准确性为代价）。它使用手工优化的汇编代码来实现比 Delphi RTL 提供的等效功能更好的性能。
// *浮点、向量、矩阵运算。*

* [MPArith](http://www.wolfgang-ehrhardt.de/misc_en.html#mparith)。 `[Delphi]` 多精度整数、有理数、实数和复数算术。

* [AMath](http://www.wolfgang-ehrhardt.de/misc_en.html#amath) 和 [DAMath](http://www.wolfgang-ehrhardt.de/misc_en.html#damath)。 `[Delphi]` 不使用多精度算术的精确数学方法和不使用多精度算术或汇编器的双精度精确数学方法分别。

* [ALGLIB](http://www.alglib.net/download.php)。 `[Delphi]` `[FPC]` 跨平台数值分析和数据处理库。它支持多种操作系统（Windows 和 POSIX，包括 Linux）。 ALGLIB 功能包括： 数据分析（分类/回归、统计）；优化和非线性求解器；插值和线性/非线性最小二乘拟合；线性代数（直接算法、EVD/SVD）、直接和迭代线性求解器；快速傅立叶变换和许多其他算法。
// 免费版是 Delphi 围绕通用 C 核心的包装，许可供个人和学术使用。

* [CAI 神经 API](https://github.com/joaopauloschuler/neural-api)。 `[FPC]` `[Delphi]` 跨平台神经网络 API 针对 AVX、AVX2 和 AVX512 指令集以及支持 OpenCL 的设备（包括 AMD、Intel 和 NVIDIA）进行了优化。

* [DFF 库](http://www.delphiforfun.org/programs/library/Default.htm)。 `[Delphi]` `[FPC]` 大浮点、大整数、天文计算

* [LMath](https://sourceforge.net/projects/lmath-library)。 `[FPC]` 提供数值分析的例程和演示程序，包括数学函数、概率、矩阵、优化、线性和非线性方程、积分、快速傅里叶变换、随机数、曲线拟合、统计和图形。它完全用 Pascal 编写，不依赖外部库。

* [mrMath](https://github.com/mikerabat/mrmath)。 `[Delphi]` `[FPC]` 高性能、多线程矩阵和线性代数库，具有针对 SSE、AVX、AVX2 和 FMA 的手动优化汇编程序例程。提供核心分解（SVD、LU、QR、Hessian、Cholesky）、对称矩阵的优化特征值求解器，以及 PCA、CCA、非负矩阵分解、SSA、小波变换、RBF 样条、t-SNE 和线性/非线性最小二乘拟合等高级算法。支持 32 位和 64 位平台上的 Windows 和 Linux。


## 命令行

*用于解析命令行参数的库*

* [TCommandLineReader](https://github.com/benibela/rcmdline)。 `[Delphi]` `[FPC]` 该单元为 Lazarus 和 Delphi 提供了先进的、独立于平台的命令行解析器。它检查允许的选项，自动打印包含所有选项列表的帮助，并且与 rtl 中的解析器相反，在 Windows 和 Linux 上的行为相同。

* [CommandLineParser](https://github.com/VSoftTechnologies/VSoft.CommandLineParser)。 `[Delphi]` 简单命令行选项解析器 - 源自 DUnitX 项目。

* [GpCommandLineParser](https://github.com/gabr42/GpDelphiUnits/blob/master/src/GpCommandLineParser.pas)。 `[Delphi]` 基于属性的命令行解析器。

* [JPL.CmdLineParser](https://github.com/jackdp/JPLib/blob/master/Base/JPL.CmdLineParser.pas)。 `[Delphi]` `[FPC]` Delphi 和 Free Pascal 的命令行解析器

* [Nullpobug.ArgumentParser](https://github.com/tokibito/delphi-argparse)。 `[Delphi]` `[FPC]` Delphi 和 Free Pascal 的命令行解析器


## 其他非视觉

* [TRegExpr](https://github.com/andgineer/TRegExpr)。 `[Delphi]` `[FPC]` 纯 Object Pascal 中的正则表达式引擎。

* [FLRE](https://github.com/BeRo1985/flre)。 `[Delphi]` `[FPC]` FLRE (Fast Light Regular E xpressions) 是一个快速、安全且高效的正则表达式库，它在 Object Pascal（Delphi 和 Free Pascal）中实现，但甚至可以从其他语言（如 C/C++ 等）中使用。

* [OnGuard](http://sourceforge.net/projects/tponguard)（[备用](https://github.com/TurboPack/OnGuard-VCL) 和仅针对最新编译器版本的维护版本）。用于创建 Borland Delphi 和 C++Builder 应用程序演示版本的“[Delphi]”库。创建有时间限制、功能有限、仅限于一定数量的使用或仅限于一定数量的并发网络用户的演示版本。
// *第二个链接指向最新编译器版本的改编版本。*

* [字符串相似度](https://github.com/chaosben/theunknownones)。 `[Delphi]` 包设计用于一些模糊和语音字符串比较算法。到目前为止，实现了以下算法：DamerauLevenshtein、Koelner Phonetik、SoundEx、Metaphone、DoubleMetaphone、NGram、Dice、JaroWinkler、NeedlemanWunch、SmithWatermanGotoh、MongeElkan。

* [DuckDuckDelphi](https://code.google.com/p/duckduckdelphi)。 `[Delphi]` 向 Delphi 对象添加简单的鸭子类型，并提供 RTTI 帮助器类来简化许多常见的 RTTI 任务。

* [byterage](https://github.com/quartexNOR/byterage)。 `[Delphi]` Object pascal 类库旨在消除流的一些限制。该框架使用起来非常简单，只有一个共同的祖先类（TBRBuffer），它定义了一组与存储无关的机制，用于分配、缩放、插入、删除和以其他方式操作原始二进制数据段。

* [无状态](https://github.com/SirRufo/stateless)。 `[Delphi]` 用于在 Delphi 代码中创建状态机的简单库。

* [GenericTree](https://github.com/davidberneda/GenericTree)。 `[Delphi]` 通用树结构的 Delphi 实现。

* [DHibernate](https://github.com/thecocce/delphi-hibernate)。 `[Delphi]` 基于 Hibernate 和 NHibernate for Delphi 的对象持久框架。
// *自 2012 年起被废弃*

* [UniConv](https://github.com/d-mozulyov/UniConv)。 `[Delphi]` `[FPC]` 通用文本转换库是一个通用的快速且紧凑的库，用于根据 Unicode 联盟的最新标准转换、比较和更改文本寄存器。这些库的功能与 ICU、libiconv 和 Windows.kernel 非常相似，它们是流行操作系统的事实上的标准。

* [CachedBuffers](https://github.com/d-mozulyov/CachedBuffers)。 `[Delphi]` `[FPC]` 该库对于顺序数据读取或写入的任务是不可替代的，特别是在性能要求提高且数据量很大的情况下。

* [CachedTexts](https://github.com/d-mozulyov/CachedTexts)。 `[Delphi]` `[FPC]` 强大而紧凑的跨平台库，旨在以尽可能高的性能解析和生成文本数据。取决于另外两个库：CachedBuffers 和 UniConv。

* [ZEXMLSS](https://github.com/Avemey/zexmlss)。 `[Delphi]` `[FPC]` 用于读/写 ods、excel xml、xlsx 的 Lazarus/Delphi 组件。

* [PasMP](https://github.com/BeRo1985/pasmp)。 `[Delphi]` `[FPC]` 用于 Object Pascal 的并行处理/多处理库。

* [ICU4PAS](http://www.crossgl.com/icu4pas/index.html)。 `[Delphi]` `[FPC]` Object Pascal，跨平台，直接类包装器，基于成熟且广泛使用的 C/C++ ICU 库集，提供 Unicode 支持、软件国际化 (i18n) 和全球化 (g11n)，为应用程序在所有平台上提供相同的结果。您可以在 Windows 上使用 Delphi 和 FreePascal，在 Linux 上使用 Kylix 和 FreePascal。
// *自 2007 年以来就没有更新过，但 ICU 界面可能保持不变*

* [GpDelphiUnits](https://github.com/gabr42/GpDelphiUnits)。 `[Delphi]` 有用的 Delphi 单元的集合。各种 TList 后代、TList 兼容类和 TList 类似类。动态分配、O(1) 入队和出队、线程安全、微锁定队列。具有一些附加功能的 64 位文件函数的接口。字符串哈希、表和字典。 Win32/Win64 包装器和辅助函数的集合。时区例程。嵌入式文件系统。

* [BaseNcodingPascal](https://github.com/Xor-el/BaseNcodingPascal)。 `[Delphi]` `[FPC]` 用于使用 Base32、base85、base128 以及 FPC 和 Delphi 的其他算法将二进制数据编码为字符串的库。

* [ByteSizeLibPascal](https://github.com/Xor-el/ByteSizeLibPascal)。 `[Delphi]` `[FPC]` TByteSize 是一个实用程序“记录”，通过消除所表示的值的歧义，使代码中的字节大小表示更加容易。

* [EmailValidationPascal](https://github.com/Xor-el/EmailValidationPascal)。 `[Delphi]` `[FPC]` 用于在 Pascal/Delphi 中验证电子邮件地址语法的简单类。

* [PRNG](http://www.wolfgang-ehrhardt.de/misc_en.html#prng)。 `[Delphi]` 七个快速伪随机数生成器，其周期长度远大于 Pascal 的随机函数。所有这些都是通过上下文记录实现的，因此可以同时使用多个独立的生成器，它们在加密上并不安全。此外还有三个密码生成器。

* [CSV 文件和字符串读取器](https://www.codeproject.com/Tips/783493/Delphi-CSV-File-and-String-Reader-Classes)。 `[Delphi]` TnvvCSVFileReader 和 TnvvCSVStringReader 是类似于单向数据集的轻量级且快速的类。

* [HTMLBuilder](https://github.com/guitorres/htmlbuilder)。 `[Delphi]` 使用 pascal 代码构建简化的 html。

* [FreePascal Generics.Collections](https://github.com/maciej-izak/generics.collections)。 `[FPC]` FreePascal Generics.Collections 库（TList、TDictionary、THashMap 等）

* [FuzzyWuzzy.pas](https://github.com/DavidMoraisFerreira/FuzzyWuzzy.pas)。 `[FPC]` 著名的 Python 模糊字符串匹配包的端口，它使用 Levenshtein 距离来计算字符串序列之间的差异。

* [GS.Core](https://github.com/VincentGsell/GS.Core)。 `[Delphi]` `[FPC]` 多个项目共享的核心功能。
// *线程池、文件操作、Key<>Value 数据库、JSON 库等*

* [PascalTZ](https://github.com/dezlov/PascalTZ)。 `[FPC]` 帕斯卡时区允许您在各个时区的本地时间和 GMT/UTC 之间进行转换，同时考虑到时区规则的历史变化。

* [字符集谜](https://github.com/ms301/charset-enigma)。 `[Delphi]` Delphi 字符集检测器社区版

* [DelphiPatterns](https://github.com/jimmckeeth/DelphiPatterns)。 `[Delphi]` Delphi语言实现的完整设计模式集

* [Pascal 的 Markdown 处理器](https://github.com/grahamegrieve/delphi-markdown)。 `[Delphi]` `[FPC]` 这是一个 Pascal (Delphi) 库，可将 markdown 处理为 HTML

* [基于协程的多线程库](https://github.com/Purik/AIO)。 `[Delphi]` AIO 在 Delphi 中实现面向过程的编程 (POP) 风格。这意味着开发人员可以结合 OOP 和 POP 的优点，将逻辑拆分到多个状态机，将它们调度到线程，像 GoLang 中那样通过通信通道连接它们

* [Rapid.Generics](https://github.com/d-mozulyov/Rapid.Generics)。 `[Delphi]` Delphi (XE8+) 的快速泛型/默认等效类

* [TZDB](https://github.com/pavkam/tzdb)。 `[Delphi]` `[FPC]` Delphi/FreePascal 的 IANA 时区数据库

* [PascalUtils](https://github.com/isemenkov/pascalutils)。 `[Delphi]` `[FPC]` Delphi 和 utils 数据结构的 object pascal 库

* [libPasC-算法](https://github.com/isemenkov/libpasc-algorithms)。 `[Delphi]` `[FPC]` Delphi 和 object pascal 库的常用数据结构和算法。从 c 算法存储库和其他来源重写的库。

* [Delphi-Hunspell](https://github.com/darianmiller/Delphi-Hunspell)。 `[Delphi]` Delphi 的简单 [Hunspell](http://hunspell.github.io) 拼写检查引擎包装器。

* [CocinAsync](https://bitbucket.org/sivv/cocinasync)。 `[Delphi]` Delphi 的高性能库，可简化编码并提高异步和多线程应用程序的性能。

* [Delphi LightSaber-CoreLib](https://github.com/GodModeUser/Delphi-LightSaber-CoreLib)。 `[Delphi]` Jedi 库的轻量级替代品。简单、清晰、无混淆、带有完整注释的代码。没有外部依赖。数百个超级有用的函数，用于文件/文件夹/磁盘操作、快速（缓冲）二进制文件访问、字符串转换、操作系统版本检测等。

* [LAMW](https://github.com/jmpessoa/lazandroidmodulewizard)。 `[FPC]` Lazarus Android 模块向导使用 Lazarus/Free Pascal 创建 JNI Android 可加载模块 (.so) 和 Android Apk。

* [DCContainers](https://github.com/dsapolska/dccontainers)。 `[Delphi]` 容器库，带有基于红黑树的映射和集合

* [DOS命令](https://github.com/TurboPack/DOSCommand)。 `[Delphi]` 组件允许您执行 dos 程序（exe、com 或批处理文件）并捕获输出，以便将其放入备忘录或列表框中，...您还可以发送输入。

* [TDiff](https://github.com/rickard67/TextDiff)。 `[Delphi]` `[FPC]` Delphi 和 Free Pascal 的文本比较组件。极大地简化了需要计算“最短路径”或“最长公共序列”的编程任务，正如文件比较实用程序中通常需要的那样。

* [Delphi 的 GraphQL](https://github.com/lminuti/graphql)。 `[Delphi]` GraphQL 的简单实现，GraphQL 是 Facebook 创建的 API 的查询语言。 GraphQL 是 API 的查询语言和服务器端运行时，用于使用您为数据定义的类型系统执行查询。 GraphQL 不依赖于任何特定的数据库或存储引擎，而是由现有代码和数据支持。

* [GraphQL 构造函数](https://github.com/HemulGM/GraphQL)。 `[Delphi]` GraphQL 构造函数（仅限构造函数）

* [ACBr (巴西商业自动化)](https://sourceforge.net/projects/acbr/) ([GitHub 镜像](https://github.com/ProjetoACBr/ACBr), [GitHub 中的组织页面](https://github.com/Projeto-ACBr-Oficial)。 `[Delphi]` `[FPC]` Delphi 和 Lazarus 的组件和库集，旨在简化巴西商业自动化系统的开发。它是被需要将其软件与财务义务和自动化设备集成的开发人员广泛使用


## 操作系统##

*有助于处理操作系统特定内部结构的工具*

* [GLibWMI](https://github.com/germanestevez/GLibWMI)。 `[Delphi]` Delphi 组件库，将用于访问 Windows WMI 的类封装在一组 VCL 中。 BiosInfo、PrinterInfo、DiskInfo 等。允许访问 WMI 类：WIN32_Bios、WIN32_Printers、WIN32_DiskDrive。

* [内存映射](https://github.com/AlexanderBagel/ProcessMemoryMap/tree/master/MemoryMap)。 `[Delphi]` 一组类，用于获取有关正在运行的进程的内存的所有信息。

* [拖放组件套件](https://github.com/landrix/The-Drag-and-Drop-Component-Suite-for-Delphi)。 `[Delphi]` VCL 组件库使您的 Delphi 和 C++Builder 应用程序能够支持基于 COM 的拖放并与 Windows 剪贴板集成。

* [TSMBIOS](https://github.com/RRUZ/tsmbios)。 `[Delphi]` `[FPC]` 允许使用 Object Pascal 语言（Delphi 或 Free Pascal）访问系统管理 BIOS (SMBIOS)。 SMBIOS（系统管理BIOS）是DMTF 制定的标准。 SMBIOS 中存储的信息包括设备制造商、型号名称、序列号、BIOS 版本、资产标签、处理器、端口和安装的设备内存。

* [Delphi 版本信息](http://melander.dk/articles/versioninfo)。 `[Delphi]` 该库使得从 Windows 可执行文件和 DLL 的版本信息资源中读取值变得非常容易。可以选择通过类帮助器使用版本信息属性扩展 TApplication 类。

* [Magenta Systems WMI 和 SMART 组件](http://www.magsys.co.uk/delphi/magwmi.asp)。 `[Delphi]` 包含 WMI、SMART 和 SCSI PassThrough 功能，特别用于获取硬盘信息和配置网络适配器，但也可用于许多其他常规用途。 MagWMI 使用类似 SQL 的命令提供对任何 WMI 信息的常规视图访问，还提供许多与 TCP/IP 配置相关的专用功能，例如设置适配器 IP 地址、计算机名称、域/工作组、BIOS 和磁盘驱动器信息。

* [madKernel](http://help.madshi.net/madKernel.htm)。 `[Delphi]` 该包的最大部分是关于内核对象的。最重要的对象类型被封装在接口中，利用所有特定的 kernel32 API。具有以下接口包装器：事件、互斥体、线程、进程、Windows、模块、托盘图标、共享内存缓冲区。
// *在某些[条件](http://help.madshi.net/License.htm)的情况下，免费提供非商业用途的源代码(仅)。可作为“madCollection”安装程序的一部分下载。有据可查。需要 `madBasic` 包。*

* [madSecurity](http://help.madshi.net/madSecurity.htm)。 `[Delphi]` 该包可以轻松处理共享和其他安全对象，如文件安全或注册表安全。为此，该软件包还提供有关帐户、ACE 和 ACL 的功能。
// *在某些[条件](http://help.madshi.net/License.htm)的情况下，免费提供非商业用途的源代码(仅)。可作为“madCollection”安装程序的一部分下载。有据可查。需要 `madBasic` 包。*

* [madShell](http://help.madshi.net/madShell.htm)。 `[Delphi]` 该包实现了经常需要的 shell 功能，从“Windows”文件夹或“Program Files”文件夹等特殊文件夹开始，然后是 Shell ID 列表、Shell 对象和 Shell 事件。然后您将找到有关快捷方式/ShellLinks 的功能，最后找到有关显示模式的所有功能。
// *在某些[条件](http://help.madshi.net/License.htm)的情况下，免费提供非商业用途的源代码(仅)。可作为“madCollection”安装程序的一部分下载。有据可查。需要 `madBasic` 包。*

* [Windows自动运行](https://github.com/ms301/WindowsAutorun)。 `[Delphi]` 帮助您管理 Windows 操作系统中的自动加载。

* [ActiveDirectory4Delphi](https://github.com/EdZava/VCL-ActiveDirectory4Delphi)。 `[Delphi]` Delphi 基本库，用于在 Active Directory 中验证和验证 LDAP 用户。

* [SVGShellExtensions](https://github.com/EtheaDev/SVGShellExtensions)。 SVG 文件的 `[Delphi]` Shell 扩展（预览面板、缩略图图标、SVG 编辑器）

* [MarkdownShellExtensions](https://github.com/EtheaDev/MarkdownShellExtensions)。适用于 Windows 资源管理器的“[Delphi]” Markdown 文件 Shell 扩展以及具有即时预览功能的 Markdown 文件编辑器


## 报告生成##

* [报告管理器](http://reportman.sourceforge.net)。 `[Delphi]` 报表管理器是一个报表应用程序（报表管理器设计器）和一组用于预览、导出或打印报表的库和实用程序。包括本机 .Net 和 Delphi/C++Builder 库、ActiveX 组件以及标准动态链接库，可在任何语言（如 GNU C）中使用。

* [FortesReport](https://github.com/fortesinformatica/fortesreport-ce)。 `[Delphi]` FortesReport 是一个功能强大的报告生成器，可作为 Delphi 的组件包使用。

* [mORMotReport](https://github.com/synopse/mORMot/blob/master/SQLite3/mORMotReport.pas) ([文档](http://synopse.info/files/html/api-1.18/mORMotReport.html))。 `[Delphi]` 快速高效的基于代码的报告组件，具有预览表单和 PDF 导出功能。

* [Kryvich 的 Delphi 报告器](https://github.com/Kryuski/kryvich-delphi-reporter)。 `[Delphi]` 用于 Embarcadero（CodeGear、Borland）Delphi 的简单但功能强大的报告工具。它根据自定义模板和来自任何 TDataSet 兼容数据集的信息生成 TXT、RTF、HTML 和 XML 格式的报告。


## 单元测试##

* [DUnitX](https://github.com/VSoftTechnologies/DUnitX)。 `[Delphi]` 新的测试框架，借鉴了 DUnit、NUnit 和其他测试框架的思想。它设计用于与 Delphi 2010 或更高版本一起使用，它利用旧版本 Delphi 中不可用的语言/RTL 功能。

* [DUnit](http://dunit.sourceforge.net)。 “[Delphi]”单元测试框架多年来一直是标准测试框架，Delphi IDE 现在附带此库。
// *自 XE 起包含，自 XE8 起已弃用，转而使用 DUnitX；似乎被遗弃了。*

* [DUnit2](http://dunit2.sourceforge.net)。 DUnit 项目的“[Delphi]”分支添加了一些新功能。
// *似乎已被放弃，缺少上一个 DUnit 版本的一些功能。*

* [DelphiSpec](https://github.com/RomanYankovsky/DelphiSpec)。用于运行以简单语言编写的自动化测试的“[Delphi]”库。因为它们是用简单的语言编写的，所以团队中的任何人都可以阅读。由于任何人都可以阅读它们，因此您可以使用它们来帮助改善团队的沟通、协作和信任。

* [Delphi-Mocks](https://github.com/VSoftTechnologies/Delphi-Mocks)。 `[Delphi]` 用于 Delphi XE2 或更高版本的简单模拟框架。允许您模拟类和接口以进行测试。

* [DUnit-XML](https://github.com/VSoftTechnologies/DUnit-XML)。 “[Delphi]”测试运行器允许 DUnit 测试输出 NUnit 兼容的 XML。

* [Smoketest](https://github.com/deltics/delphi.libs/tree/master/smoketest)。 “[Delphi]”框架，用于使用 Microsoft Windows 的 Delphi 语言编写测试和性能基准测试。从 7 月到 2010 年，它已经在所有版本的 Delphi 上进行了测试。

* [SynTests](https://github.com/synopse/mORMot/blob/master/SynTests.pas)。 `[Delphi]` `[FPC]` 单元测试功能，包括模拟和存根。

* [OpenCTF](https://github.com/michaelJustin/openctf)。 `[Delphi]`（上一个[主页](http://web.archive.org/web/20090418162025/https://sourceforge.net/projects/openctf/)）Embarcadero Delphi 的测试框架插件，它对表单（或数据模块）中的所有组件执行自动检查。它提供了一种简单的方法来为大型项目构建自动质量检查，其中许多组件必须通过重复测试。 OpenCTF 基于 DUnit 开源测试框架，并通过专门的测试类和辅助函数对其进行了扩展。

* [DelphiUIAutomation](https://github.com/jhc-systems/DelphiUIAutomation)。包装 MS UIAutomation 库的“[Delphi]”Delphi 类。 DelphiUIAutomation 是一个基于 Win32 的富客户端应用程序自动化框架（并专门使用 Delphi XE5 进行了测试）。它是用Delphi XE5 编写的，不需要使用脚本语言。它提供了一致的面向对象的API，隐藏了Microsoft UIAutomation 库和Windows 消息的复杂性。

* [DelphiCodeCoverageWizardPlus](https://github.com/MHumm/delphi-code-coverage-wizard-plus)。 `[Delphi]` GUI 向导，用于创建批处理文件来调用命令行代码覆盖工具。包括项目格式，以便以后更轻松地更改设置。包括代码覆盖率工具 itssel 的二进制文件。


## 调试/错误处理##

* [Delphi LeakCheck](https://bitbucket.org/shadow_cs/delphi-leakcheck)。 `[Delphi]` 免费代码库，用于检查 DUnit 和 DUnit2 测试中的内存泄漏。支持德尔福XE-XE7。

* [FastMM](#内存管理器)。提供强大的内存泄漏/损坏检测工具。

* [JclDebug（JEDI 项目的一部分）](https://github.com/project-jedi/jcl/blob/master/jcl/source/windows/JclDebug.pas)。 `[Delphi]` `[FPC]` 跟踪、MAP 文件解析器、异常报告生成、异常堆栈跟踪。

* [调试引擎](https://github.com/MahdiSafsafi/DebugEngine)。 `[Delphi]` 与调试相关的实用程序集合（堆栈跟踪、CPU 寄存器快照、调试信息等）。访问 Delphi 调试信息、从名称获取符号地址、Delphi 映射解析和映射转换器到二进制格式、智能堆栈跟踪、Delphi 异常堆栈跟踪挂钩等。

* [对象调试器](https://github.com/marcocantu/ObjectDebugger)。用于 Delphi VCL 应用程序的“[Delphi]”运行时对象检查器。

* [Capstone4Delphi](https://github.com/Pigrecos/Capstone4Delphi)。 `[Delphi]` [Capstone 反汇编程序库](http://www.capstone-engine.org/) 绑定 Delphi


## 公用事业##

*此处允许免费的非开源产品。*


## RAD Studio IDE 插件/向导

* [Delphi IDE 主题编辑器/Delphi IDE Colorizer](https://github.com/rruz/delphi-ide-theme-editor)。用于更改多个 Object Pascal IDE（例如 Delphi (RAD Studio)、Appmethod、Lazarus 和 Smart Mobile Studio）的 IDE 颜色突出显示的工具。 DITE支持Delphi 5-7、2005-2010、XE-XE8、Appmethod 1.13-1.14、Lazarus v1.0.1.3和Smart Mobile Studio IDE v1.1.2.17。 Delphi IDE Colorizer (DIC) 是一个插件，允许自定义 RAD Studio IDE 和 Appmethod 工作区的外观和感觉。

* [DDevExtensions](https://github.com/ahausladen/DDevExtensions)。通过添加一些新的生产力功能来扩展 Delphi/C++Builder IDE。
// *许多有用的 IDE 调整，必须有。*

* [VCL 修复包](https://www.idefixpack.de/blog/bugfix-units/vclfixpack-10/)。 Delphi 单元通过修补原始函数来修复运行时的 VCL 和 RTL 错误。如果您想要应用程序中的所有 IDE Fix Pack 修复，那么这个单元就是您所需要的。将单元添加到您的项目（Delphi 和 C++Builder）会自动安装适用于您的 Delphi/C++Builder 版本的补丁。
// *Delphi/C++ 6..2009 的实际值*

* [IDE 修复包](https://www.idefixpack.de/blog/ide-tools/ide-fix-pack/)。针对 RAD Studio IDE、Win32/Win64 编译器和 Win32 调试器的非官方错误修复和性能优化的集合。 IDE Fix Pack 是 RAD Studio 2009-XE6 的 IDE 插件，可在运行时修复 IDE 错误。所有的改变都是在内存中完成的。磁盘上的文件没有被修改。除了编译速度更快之外，您的所有项目都不会被修改或从 IDE Fix Pack 中受益。只有 IDE 才能获得修复和优化。
// *支持自 2007 年以来的所有 RAD Studio 版本。消除了 EMBT 多年来未修复的许多恼人的错误。耶！*

* [GExperts](https://sourceforge.net/projects/gexperts)。通过向 IDE 添加多项功能来提高 Delphi 和 C++Builder 程序员的工作效率的免费工具集。 GExperts 是作为开源软件开发的，我们鼓励用户为该项目做出贡献。 Grep 搜索和替换支持 unicode 文件、DFM 等；自动重命名组件、插入文本宏、打开最近的文件；使用自定义附加文件列表轻松备份您的项目；保留最喜爱文件的嵌套列表以便快速访问；跟踪项目中各单元之间的依赖关系；快速跳转到当前单元中的任意程序；还有很多很多。

* [CnWizards](https://github.com/cnpack)。 Delphi/C++ Builder/CodeGear RAD Studio 的免费插件工具集，提高开发效率。

* [Delphi 软件包安装程序 (DelphiPI)](https://bitbucket.org/idursun/delphipi)。帮助您将组件安装到 Delphi IDE 的工具。 DelphiPI 自动解决包之间的依赖关系、编译、安装并将源路径添加到您的 IDE。

* [ResEd](https://github.com/chaosben/theunknownones)。 Delphi 2005、2006、2007、2009、2010 和 XE 专家。该专家设计用于编辑链接到活动项目的资源文件（.res；.resx）。它将自动搜索所有出现的 {$R xyz.res} 行，并为它们打开/创建资源文件。专家将其自身注册在 Delphi 菜单栏中的“视图”下。

* [帕纳苏斯书签](https://parnassus.co/delphi-tools/bookmarks)。扩展书签功能的 IDE 插件。

* [DelphiSettingManager](https://github.com/Arvur/DelphiSettingManager)。 Delphi 的多个 IDE 配置文件（最高 XE6）。允许为不同的项目安装同一组件的多个版本或不同的组件集。

* [Delphinus](https://github.com/Memnarch/Delphinus)。新的 Packagemanager 在 Delphi XE 和更新版本上运行，并使用 GitHub 作为后端来提供包。

* [TestInsight](https://bitbucket.org/sglienke/testinsight/wiki/Home)。 Delphi 的单元测试 IDE 插件。它支持从XE到10 Seattle的所有版本。支持 DUnit、DUnit2、DUnitX 框架。

* [Delphi IDE 资源管理器](https://github.com/DGH2112/Delphi-IDE-Explorer)。向导/专家/插件，允许您浏览IDE的内部字段、方法、属性和事件。
// *主要对IDE专家的开发者有用*

* [Multi-RAD Studio IDE Expert Manager](https://github.com/DGH2112/Expert-Manager)。应用程序允许您管理加载到 RAD Studio 多个版本中的专家和包

* [OTA接口搜索](https://github.com/DGH2112/OTA-Interface-Search)。应用程序有助于查找开放工具 API (OTA) 接口、方法和属性，并了解如何获取这些接口或接口的方法/属性。

* [自动保存](https://github.com/DGH2112/Auto-Save)。定期自动保存所有打开的修改过的 IDE 文件的专家。

* [浏览并记录](https://github.com/DGH2112/Browse-and-Doc-It)。 RAD Studio IDE 插件允许您浏览代码并提供文档、编码检查和指标支持。

* [集成测试助手](https://github.com/DGH2112/Integrated-Testing-Helper)。 Delphi 和 RAD Studio 的插件，允许您在项目编译之前和之后运行命令行应用程序。它还提供了在每次编译/构建时将项目文件压缩到存档中的能力，并管理应用程序的版本信息。

* [魔术师项目](https://www.uweraabe.de/Blog/2018/05/17/keep-your-project-files-clean-with-project-magician)。用于高级项目选项操作的向导。

* [选择性调试](http://www.uweraabe.de/Blog/2015/05/08/selective-debugging/)。允许调整调试版本将用于哪些单元的向导。

* [MMX 代码浏览器](https://www.mmx-delphi.de)。功能丰富的生产力增强插件。包括重构、类浏览器、高级编辑、metrict 等等。

* [FormResource](http://chapmanworld.com/2017/03/22/formresource-a-free-delphi-component-for-organizing-product-dependencies)。帮助将各种数据存储为表单资源的向导。

* [Delphi Library Helper](https://github.com/littleearth/delphi-library-helper) 帮助 Delphi 开发人员配置库文件夹的工具。

* [Mobile Image Creator](https://github.com/littleearth/mobile-image-creator) 为 Delphi 移动应用程序 (Firemonkey) 创建图标和启动器图像。这是 Mobile Gfx 的一个分支，由 [RiverSoftAVG 的 Thomas Grubb](http://riversoftavg.com/blogs/index.php/2014/02/03/creating-icons-and-launchers-for-delphi-mobile-applications/) 创建。

* [Delphi-Adb-WiFi](https://github.com/ms301/Delphi-Adb-WiFi)。 RAD Studio 插件，允许在 Android 设备上启动和调试，而无需通过 USB 连接到计算机。通过 WiFi 工作。

* [RADSplit](https://github.com/LaKraven/RADSplit)。 RAD Studio（Delphi 和 C++ Builder）的可停靠分屏编辑器。

* [DzNoteEditor](https://github.com/digao-dalpiaz/DzNoteEditor)。用于 TString 的 Delphi 属性编辑器支持带语法突出显示的格式化语言。

* [IDE-Notifiers](https://github.com/DGH2112/DGH-IDE-Notifiers)。 RAD Studio IDE 插件，用于在 IDE 中发生各种操作时显示通知。

* [C4D-Validate-Components](https://github.com/Code4Delphi/C4D-Validate-Components)。 `[Delphi]` 用于自动验证 Delphi 表单的实用程序。非常适合用于新项目和旧产品。促进表单字段验证并降低代码复杂性。它可用于 DBWare 和非 DBWare 组件。


## 其他 IDE 的插件

* [Delphi IDE 主题编辑器/Delphi IDE Colorizer](#rad-studio-ide-pluginswizards)。支持Appmethod、Lazarus和Smart Mobile Studio。

* [Pascal](https://github.com/alefragnani/vscode-language-pascal) 和 [Pascal Formatter](https://github.com/alefragnani/vscode-pascal-formatter)。为 Visual Studio Code 创建的开源扩展，添加了 Pascal 支持。

* [Intellij IDEA Object Pascal 插件](https://github.com/casteng/i-pascal)。 `[Delphi]` `[FPC]` IntelliJ IDEA 的免费 Object Pascal 语言插件


## 文档

* [SynProject](https://github.com/synopse/SynProject) ([文档](http://synopse.info/fossil/wiki?name=SynProject))。用于 Delphi 项目的代码源版本控制和自动文档编制的工具。

* [PasDoc](https://sourceforge.net/projects/pasdoc)。 `[Delphi]` `[FPC]` 用于 ObjectPascal（FreePascal 和 Delphi）源代码的文档工具。文档是根据源代码中的注释生成的。可用的输出格式有 HTML、HtmlHelp、LaTeX、latex2rtf、simplexml。将来可能会添加更多输出格式。


## 代码检查/审查、调试

* [GpProfiler2017](https://github.com/ase379/gpprofile2017)。 `[Delphi]` 用于 Delphi XE 及更高版本的源代码检测分析器。其他分支支持旧版本。

* [SamplingProfiler](https://www.delphitools.info/samplingprofiler)。 `[Delphi]` 用于 Delphi 5 至 32 位 Delphi XE4 的性能分析工具。其目的是帮助定位瓶颈，即使是在全速运行的最终优化代码中也是如此。

* [Delphi 代码覆盖率](https://github.com/DelphiCodeCoverage/DelphiCodeCoverage)。 `[Delphi]` 用于 Delphi 的简单代码覆盖率工具，可根据详细的 MAP 文件创建代码覆盖率报告。

* [Pascal 分析器](http://www.peganza.com/products_pal.html)（提供免费精简版）。 `[Delphi]` Pascal 分析器，简称 PAL，解析 Delphi 或 Borland Pascal 源代码。它构建大型内部标识符表，并收集其他信息，例如子程序之间的调用。解析完成后，会生成大量报告。这些报告包含大量有关源代码的重要信息。这些信息将帮助您更好地理解源代码，并帮助您生成更高质量和可靠性的代码。

* [madExcept](http://madshi.net/madExceptShop.htm)。 `[Delphi]` madExcept 旨在帮助您定位软件中的错误。每当您的程序出现崩溃/异常时，madExcept 都会自动捕获它，分析它，收集大量有用的信息，并使最终用户能够向您发送完整的错误报告。 madExcept 还能够为您查找内存泄漏、资源泄漏和缓冲区溢出。
// *免费**无源**用于非商业用途（仅限），但有一些[条件](http://help.madshi.net/License.htm)。可作为“madCollection”安装程序的一部分下载（您需要安装“madExcept”项目）。有很好的记录。*

* [delphiunitsizes](https://github.com/VilleKrumlinde/delphiunitsizes)。 `[Delphi]` 用于显示 Delphi 可执行文件中每个单元的大小的工具。显示 Delphi exe 文件中包含的每个单元的大小。它还显示单元中每个符号（类、方法、过程等）的大致大小。

* [MapFileStats](https://www.delphitools.info/other-tools/mapfilestats)。 `[Delphi]` 工具，提供来自 .MAP 文件的简单二进制大小统计（任何 Delphi 版本，至少 Delphi XE5）。

* [蜘蛛](https://github.com/yavfast/dbg-spider)。用于 Delphi 应用程序的“[Delphi]”实时分析器

* [AsmProfiler](https://github.com/andremussche/asmprofiler)。 `[Delphi]` 完整跟踪 32 位分析器（检测和采样），用 Delphi 和一些程序集编写

* [map2pdb](https://github.com/andersmelander/map2pdb)。 “[Delphi]”工具用于将 Delphi 和 C++ Builder 编译器生成的 MAP 文件转换为 Microsoft PDB 文件，以便在支持该格式的工具中使用，例如 Visual Studio 调试器以及 Intel 的 VTune 和 AMD 的 μProf 分析器。

* [ProfileViewer](https://github.com/DGH2112/ProfileViewer)。 “[Delphi]”应用程序用于查看 Profiler.pas 代码生成的探查器信息。

* [SonarDelphi](https://github.com/integrated-application-development/sonar-delphi)。 `[Delphi]` SonarQube 代码质量平台的静态分析器。


## 设置

* [Lazy Delphi Builder](https://bitbucket.org/tdelphi/lazy-delphi-builder-downloads)。 Delphi 的构建工具。从具有所有依赖项的源重新编译项目/包，无需搞乱配置。快速（重新）将组件从源安装到 IDE 中，无需更改库路径。
// *强大的自动化工具。免费软件但非开源*

* [Inno设置](http://www.jrsoftware.org/isinfo.php)。 Windows 程序的免费安装程序。 Inno Setup 于 1997 年首次推出，如今在功能集和稳定性方面可与许多商业安装程序相媲美甚至超越。

* [WinSparkle](https://winsparkle.org) 及其 [Delphi 包装器](https://github.com/jkour/neSparkleComponent)。 WinSparkle 是一个面向 Windows 开发人员的易于使用的软件更新库。 WinSparkle 很大程度上（几乎是移植版）受到最初由 Andy Matuschak 开发的 Sparkle 框架的启发，该框架成为 macOS 上软件更新的事实上的标准。

* [Silverpoint MultiInstaller](http://www.silverpointdevelopment.com/multiinstaller/index.htm)。 Embarcadero Delphi 和 C++Builder 的多组件包安装程序，它的创建是为了简化 IDE 上的组件安装。

* [Grijjy 部署管理器](https://github.com/grijjy/GrijjyDeployMan)。用于简化用 Delphi 编写的 iOS 和 Android 应用程序的文件和文件夹部署的工具。如果您需要部署大量文件（例如第 3 方 SDK），它尤其有用。

* [AutoGetIt](https://github.com/corneliusdavid/AutoGetIt)。 `[Delphi]` 开源工具，通过调用 GetIt 命令行工具来自动安装选定的 GetIt 软件包。适用于 Delphi 10.4、11 和 12。源代码和预构建的可执行文件均可用。需要 [DosCommand](https://github.com/TurboPack/DOSCommand) 来编译源代码。


## 其他

* [WMI Delphi 代码创建器](https://github.com/RRUZ/wmi-delphi-code-creator)。允许您生成 Object Pascal、Oxygene、C++ 和 C# 代码来访问 WMI（Windows 管理规范）类、事件和方法。还包括一组用于浏览和查询 WMI 内容的工具。

* [Delphi 预览处理程序](https://github.com/RRUZ/delphi-preview-handler)。适用于 Windows Vista、7 和 8 的预览处理程序，允许您通过语法突出显示读取对象 pascal、C++ 和汇编代码，而无需在编辑器中打开

* [德尔福开发。 Shell 工具](https://github.com/RRUZ/delphi-dev-shell-tools)。 Windows shell 扩展，为 Object Pascal 开发人员（Delphi、Free Pascal）提供有用的任务。

* [Delphi.gitignore](https://github.com/github/gitignore)。 Delphi 的 .gitignore 模板。还有一个是给拉撒路的。

* [OmniPascal](http://omnipascal.com)。该项目使 Delphi 和 Free Pascal 开发人员能够使用现代编辑器 [Visual Studio Code](https://code.visualstudio.com) 编写和维护代码。

* [Delphi 单元测试](https://github.com/NickHodges/DelphiUnitTests)。 Delphi 库的单元测试集。鼓励 Delphi 社区成员分叉存储库、添加测试并创建拉取请求。特别鼓励 Embarcadero 员工从使用官方 Delphi 版本运行的内部测试中添加测试。

* [madDisAsm](http://help.madshi.net/madDisAsm.htm)。该软件包具有完整的 x86 反汇编程序，包括 MMX、3dNow 增强、SSE 和 SSE2 支持。反汇编器可以检查单个 x86 指令（请参阅 ParseCode）或完整函数（请参阅 ParseFunction），并返回简短分析或全文反汇编。如果可能的话，监视/跟踪寄存器内容，这改进了对跳转/调用目标的分析。自动检测并正确处理案例/开关跳转表。
// *免费**无源**用于非商业用途（仅限），但有一些[条件](http://help.madshi.net/License.htm)。可作为“madCollection”安装程序的一部分下载（您需要安装“madExcept”项目）。有很好的记录。*

* [Chet - Delphi 的 C 头文件转换器](https://github.com/neslib/Chet)。 Chet 是一个由 libclang 为 Delphi 提供支持的 .h 到 .pas 转换器。使用 Clang 编译器解析头文件，从而获得更准确的翻译，并且需要更少的手动调整。

* [老板](https://github.com/HashLoad/boss)。 Delphi 项目的依赖管理器。

* [C-To-Delphi](https://github.com/WouterVanNifterick/C-To-Delphi)。 `[Delphi]` 该工具将转换您的大部分标准 C 代码。

* [更好的翻译管理器](https://github.com/andersmelander/better-translation-manager)。 `[Delphi]` 翻译管理器。

* [dzBdsLauncher](https://osdn.net/projects/dzbdslauncher/)。用于 Delphi IDE 的“[Delphi]”启动器，根据传递给它的 dproj 文件的后缀决定启动多个 IDE 中的哪一个。

* [DFMJSON](https://github.com/masonwheeler/DFMJSON)。用于在 Delphi 的 .DFM（或 .FMX）格式和 JSON 之间进行转换的“[Delphi]”库。它可用于将 DFM 文件解析为 JSON 格式的抽象语法树，然后可以对其进行编辑并将结果返回为 DFM 格式。

* [James - Delphi 项目经理](https://github.com/alefragnani/delphi-james)。 `[Delphi]` 它使您从一个项目切换到另一个项目时的生活更加轻松。如果您发现自己每次必须从一个项目切换到另一个项目时都手动安装组件并更新 Delphi 设置，James 可能会为您提供帮助。

* [OpenAPI 客户端生成器](https://github.com/landgraf-dev/openapi-delphi-generator)。 `[Delphi]` 为使用 OpenAPI 规范定义的任何 REST API 生成 Delphi 客户端 SDK。该生成器可以读取 REST API 的 OpenAPI 文档（从本地文件或 URL）并生成 Delphi 类，您可以使用这些类以友好的方式调用此类 REST API 端点。
// *开源，但需要商业 TMS BIZ 库进行构建（试用版也可以）。二进制文件可用*
