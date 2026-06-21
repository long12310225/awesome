# 太棒了D [![Awesome](https://cdn.jsdelivr.net/gh/sindresorhus/awesome@d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

精选的精彩 D 框架、库和软件列表。受到 [awesome-python](https://github.com/vinta/awesome-python) 的启发。

大多数文档和链接都是从 [D 论坛](https://forum.dlang.org)、[D wiki](https://wiki.dlang.org) 和 [D 包存储库](https://code.dlang.org) 收集的。探索 GitHub 也很有帮助，因为许多库都托管在那里。如果您知道有趣的 D 项目，请通过 [GitHub issues](https://github.com/dlang-community/awesome-d/issues) 或通过[编辑此文件](https://github.com/dlang-community/awesome-d/edit/master/README.md) 告诉我们。

## 内容

* 基本信息
	* [官方网站](#official-website)
	* [寻求帮助](#getting-help)
	* [People](#people)
	* [Events](#events)
	* [Organizations](#organizations)
* 文件
	* [Books](#books)
	* [Tutorials](#tutorials)
	* [Blogs](#blogs)
	* [Articles](#articles)
* 语言相关
	* [包管理](#package-management)
	* [Compilers](#compilers)
	* [替代/WIP 编译器](#alternative--wip-compilers)
	* [开发工具](#dev-tools)
	* [构建工具](#build-tools)
	* [IDE 和编辑器](#ides--editors)
	* [词法分析器、解析器和生成器](#lexers-parsers--generators)
	* [Preprocessors](#preprocessors)
	* [版本管理器](#version-managers)
* 持续集成
	* [GitHub 操作](#github-actions)
	* [测试框架](#testing-frameworks)
* 语言
	* [编程语言](#programming-languages)
* 操作系统
	* [操作系统](#operating-systems)
	* [裸机/内核开发](#bare-metal--kernel-development)
* 常见
	* [一般集装箱](#general-containers)
	* [核心实用程序](#core-utilities)
* 网络/网络
	* [网络框架](#web-frameworks)
	* [数据序列化](#data-serialization)
* 数据库
	* [数据库客户端](#database-clients)
* 命令行界面
	* [CLI 库](#cli-libraries)
	* [CLI 应用程序](#cli-applications)
* 图形用户界面
	* [图形用户界面库](#gui-libraries)
	* [图形用户界面应用程序](#gui-applications)
* 游戏开发
	* [游戏绑定](#game-bindings)
	* [游戏库](#game-libraries)
	* [Games](#games)
* 国际化（i18n）/全球化
	* [Internationalization](#internationalization)
* 图像处理
	* [图像处理](#image-processing)
* 机器学习
	* [机器学习](#machine-learning)
	* [并行计算](#parallel-computing)
* 科学的
	* [Scientific](#scientific)
	* [语言处理](#language-processing)
* 其他
	* [文本处理](#text-processing)
	* [Logging](#logging)
	* [Configuration](#configuration)
	* [BlogEngine](#blog-engine)
	* [依赖注入](#dependency-injection)
	* [Cryptography](#cryptography)
	* [Unmaintained](#unmaintained)

## 官方网站

*D. 的官方网站网址*

* [dlang.org](https://dlang.org) - D 的官方网站
* [wiki.dlang.org](https://wiki.dlang.org) - D 的官方 wiki
* [blog.dlang.org](https://dlang.org/blog/) - D 的官方博客
* [forum.dlang.org](https://forum.dlang.org/) - D 的官方论坛。每天都会发生许多有趣的讨论。
* [code.dlang.org](https://code.dlang.org) - D 的官方图书馆注册表
* [GitHub organization](https://github.com/dlang) - D 的官方 GitHub 组织。所有官方 D 工具和代码的存储库。
* [Issue tracker](https://github.com/dlang) - D. 较旧报告的官方问题跟踪器可以在[存档跟踪器](https://issues.dlang.org/) 中找到。
* [Language specification](https://dlang.org/spec/spec.html) - D 编程语言规范。

## 寻求帮助

*当你陷入困境时。*

* [Official D Forum Learn Group](https://forum.dlang.org/group/learn) - 用于回答 D 问题的流量最高的网站。
* [D on Stack Overflow](https://stackoverflow.com/questions/tagged/d) - 流量比论坛少，但可能更容易搜索。
* [D on Rosetta Code](https://rosettacode.org/wiki/Category:D) - 如何在 D 中执行许多基本操作的示例。
* [D on Discord](https://discord.com/invite/bMZk9Q4) - 另一个非常活跃的 D 讨论和问题社区。

## 人

*让 D 成为这种语言的人们。*

* [Walter Bright](https://www.walterbright.com/) - D. Walter Bright 之父是 D 编程语言的创建者和第一个实现者，并实现了其他几种语言的编译器。
* [Andrei Alexandrescu, PhD](http://erdani.org/) - C++大师。 《D 编程语言》和《现代 C++ 设计》的作者。 Andrei 与 Walter Bright 共同设计了 D 的许多重要功能，并编写了 D 标准库的很大一部分。 Andrei 担任高级 C++ 编程和算法培训师，目前正在组织中积极宣传 D。
* [Átila Neves](https://atilaoncode.blog/) - [D副组长](https://dlang.org/blog/2019/10/15/my-vision-of-ds-future/)。
* **您** - 如果您在 D 中做过一些有趣的事情，请添加您的信息。正是你们，这些了不起的人让 D 变得如此出色。

## 活动

* [DConf](https://dconf.org/) - 这是 D 语言杰出人士就与 D 语言及其生态系统相关的一切知识、见解和灵感进行交流的重要活动。
* [Beerconf](https://wiki.dlang.org/Beerconf) - D 社区成员每月一次的休闲虚拟聚会。

## 组织机构

*为 D 项目做出贡献的组织。*

* [D Programming Language](https://github.com/dlang) - 官方组织，托管 DMD、Phobos 和其他官方工具和库。
* [LDC Developers](https://github.com/ldc-developers) - 最不发达国家相关项目。
* [DerelictOrg](https://github.com/DerelictOrg) - 托管所有废弃绑定的 GitHub 组织，包括 OpenGL 和其他多媒体/游戏相关的库绑定。 （OpenGL 3、Bgfx、ENet、SDL 2、GLFW 3，OpenGLES、免费图像、Assimp3、libtheora、libogg、libvorbis、SFML 2、libpq、PhysicsFS、开放动态引擎、Lua、DevIL、OpenAL、ALURE）。
* [DlangScience](https://github.com/DlangScience) - 科学图书馆和 D 工具的焦点和第一站。
* [Circular Studios](https://github.com/Circular-Studios) - 我们是罗彻斯特理工学院的一群游戏开发人员，致力于构建游戏和游戏技术。托管 [Dash](https://github.com/Circular-Studios/Dash)，一个用 D 编写的 3D 游戏引擎，以及其他相关库。
* [EMSI](https://github.com/economicmodeling) - 一家使用 D 作为主要语言的职业发展公司。托管他们的开源项目。
* [infognition](http://www.infognition.com/company.html) - Infognition 是一家自筹资金、自给自足的公司，专门为最终用户和开发人员提供视频处理和压缩技术。他们提供了几个用 D 编写的开源视频相关应用程序和工具，托管在 [bitbucket](https://bitbucket.org/infognition/workspace/repositories/) 上。他们还将他们的主要产品——[Video Enchanser](http://www.infognition.com/VideoEnhancer/)从C/C++移植到D。
* [libmir](https://github.com/libmir) - D的数值库开发团队
* [sociomantic labs](https://github.com/sociomantic-tsunami) - 总部位于柏林的公司，专门从事在线广告实时竞价。 [年度D语言会议](https://dconf.org/)的主要赞助商。作为 [tsunami](https://github.com/sociomantic-tsunami) 组织的一部分，开源了大部分代码库。
* [Symmetry Investments](https://symmetryinvestments.com/) - Symmetry Investments LP 是一家投资管理公司，截至 2018 年 12 月 31 日，管理资产约为 47 亿美元。[Symmetry Autumn of Code](https://dlang.org/blog/symmetry-autumn-of-code/) 的主要赞助商。赞助了 [excel-d](https://dlang.org/blog/2017/05/31/project-highlight-excel-d/)、[dpp](https://github.com/atilaneves/dpp)、[autowrap](https://github.com/symmetryinvestments/autowrap)、[mir-algorithm](https://github.com/libmir/mir-algorithm) 和各种其他项目的开发。
* [HuntLabs](https://github.com/huntlabs) - 使用 DLang 的技术小组。具有快速开发服务器端应用程序和构建分布式系统服务的纯D语言实现。

## 书籍

*D 相关书籍。* 您可以在 [书籍](https://wiki.dlang.org/Books) D wiki 页面上找到另一个书籍列表。

* [TDPL](https://www.amazon.com/The-Programming-Language-Andrei-Alexandrescu/dp/0321635361/) - *Andrei Alexandrescu 的《D 编程语言》。
* [Programming in D](https://ddili.org/ders/d.en/index.html) - Ali Çehreli 撰写的一本关于 D 编程的非常详细的书，涵盖了该语言的许多领域。有免费的在线版本，适合初学者。
* [D Cookbook](https://www.packtpub.com/en-us/product/d-cookbook-9781783287215) - 一本内容丰富的参考指南，其中包含实用任务，并对其进行了简明解释，以培养和扩展用户使用 D 编程语言的能力。作者：亚当·D·鲁佩 (Adam D. Ruppe)这是一篇有趣的[书评](https://www.cppstories.com/2014/08/review-of-d-cookbook/)。
* [Learning D](https://www.packtpub.com/en-us/product/learning-d-9781783552481) - 本书面向那些具有一定 C 系列语言背景、想要学习如何将其知识和经验应用到 D 语言的人。(...)本书将帮助您快速熟悉该语言，并避免将 C 系列经验翻译为 D 时出现的常见陷阱。
* [D Web Development](https://www.packtpub.com/en-us/product/d-web-development-9781785288890) - 无论您是 D 世界的新手，还是已经使用 D 开发过应用程序，或者如果您想利用 D 的强大功能进行 Web 开发，那么本书都是您的理想选择。

## 教程

*D相关教程。*

* [The Dlang Tour](https://tour.dlang.org/) - D 的交互式教程，灵感来自 Golang Tour。
* [Programming in Dlang](https://www.youtube.com/watch?v=HS7X9ERdjM4&list=PLvv0ScY6vfd9Fso-3cB4CGnSlW0E4btJV&ab_channel=MikeShah) - 有关 D 编程的介绍性视频系列。
* [Pragmatic D tutorial](https://qznc.github.io/d-tut/index.html) - 这是对 D 编程语言的实用介绍。安德烈亚斯·茨温考。
* [D Template Tutorial](https://github.com/PhilippeSigaud/D-templates-tutorial) - 专门针对 D 模板的教程。关于模板的很好的解释。有pdf版本。作者：菲利普·西高。
* [Component programming with ranges](https://wiki.dlang.org/Component_programming_with_ranges) - 一篇详细的博客文章，介绍如何使用范围以惯用的 D 方式进行组件编程，并提供完整的工作示例。
* [Functional image processing in D](https://blog.cy.md/2014/03/21/functional-image-processing-in-d/) - 一个关于在 D 中编写图像处理库的非常有趣的教程。展示了 D 的模板/CTFE/Ranges/UFCS 对于函数式编程的强大功能。
* [OpenGL tutorials](https://github.com/drewet/opengl-tutorials) - D 中的 OpenGL 教程
* [Creating a simple JSON serialiser in D](https://bradley.chatha.dev/BlogPost/JsonSerialiser/0) - D元编程教程系列
* [Let's learn D programming Game Dev!](https://www.youtube.com/watch?v=j-Zm1zgSxMQ&list=PLgM-lc_kSqFQPF0UXgmFZpZalqcrSofe-&ab_channel=KiRill) - 来自 Ki Rill 的关于与 D 一起学习游戏开发的视频系列。 [他的频道](https://www.youtube.com/@rillki-dev/) 还发布了与 D 编程相关的其他视频。
* [DLang YouTube Tutorials from Mike Shah](https://www.youtube.com/playlist?list=PLvv0ScY6vfd9Fso-3cB4CGnSlW0E4btJV) - 系列教程涵盖 D 编程语言和标准库的基础到高级功能。

## 博客

*D相关博客。*

* [blog.dlang.org](https://dlang.org/blog/) - 官方博客。
* [/r/d_language on Reddit](https://www.reddit.com/r/d_language/) - 有关 D 的新闻和博客文章的提要。
* [This week in D](https://dpldocs.info/this-week-in-d/Blog.html) - 每周 D 社区活动概述和简短建议专栏可帮助您充分利用 D 编程语言。
* [Planet D](http://planet.dsource.org) - 由 Vladimir Panteleev 维护的共同撰写的 D 特定博客存储库。
* [D Idioms](https://p0nce.github.io/d-idioms/) - 这是一个很棒的博客，介绍了许多 D 编程的有用习惯用法。
* [GTK-D coding](https://web.archive.org/web/20241201013031/https://gtkdcoding.com/) - 如何使用 GtkD 构建 GUI 应用程序的简单示例。
* [Tasty D](https://tastyminerals.github.io/tasty-blog/) - 关于学习 D 编程语言和各种 D 语言琐事的博客。

## 文章

*D相关文章。*

* [Origins of the D programming language](https://dl.acm.org/doi/pdf/10.1145/3386323) - 作者：沃尔特·布莱特、安德烈·亚历山德雷斯库、迈克尔·帕克。 D语言的历史和发展。
* [Purity in D](https://klickverbot.at/blog/2012/05/purity-in-d/) - 一篇解释 D 纯度功能背后的设计原理的文章。
* [Hidden treasures in the D standard library](https://web.archive.org/web/20171119072212/http://nomad.so/2014/08/hidden-treasure-in-the-d-standard-library/) - 一篇讨论 Phobos 中几个有用的函数和模板的文章。
* [D is for Data Science](https://tech.nextroll.com/blog/data/2014/11/17/d-is-for-data-science.html) - 一篇关于 D 如何适用于数据科学的精彩文章，特别是取代 python 脚本的角色以实现快速原型设计。
* [D 功能花园](https://garden.dlang.io/)

## 包管理

*用于包和依赖管理的库。*

* [code.dlang.org](https://code.dlang.org/) - 官方 D 库存储库。由配音支持。
* [dub](https://github.com/dlang/dub) - D 的官方包和构建管理系统。

## 编译器

*D 语言的官方编译器。*

* [DMD](https://github.com/dlang/dmd) - D 编程语言的参考编译器。稳定，构建速度极快，非常适合学习和快速原型设计/开发。目前前端是用D实现的，并在dmd、ldc和gdc之间共享，后端是用C++实现的。
* [LDC](https://github.com/ldc-developers/ldc) - 基于 LLVM 的 D 编译器。使用 DMD 前端和 LLVM 后端。构建速度比 dmd 慢，但生成的代码比 DMD 更优化。它支持LLVM的所有目标平台。
* [GDC](https://github.com/D-Programming-GDC/GDC) - GNU D 编译器。使用 DMD 前端和 GCC 后端。由于使用 GCC，目前针对大多数平台。在大多数情况下，生成的代码运行速度比 DMD 更快，与 LDC 相当。正在与官方 GCC 工具链集成过程中。

## 替代/WIP 编译器

*这些编译器可能与官方工具集不同或不兼容。*

* [SDC](https://github.com/snazzy-d/SDC) - Snazzy D 编译器。用 D 语言编写。每天都变得更聪明。
* [OpenD](https://opendlang.org/index.html) - D 语言的一个分支，专注于实际和增量改进。

## 开发工具

*提高 D 开发效率的工具。*

* [D-Scanner](https://github.com/dlang-community/D-Scanner) - D 源代码的瑞士军刀（linting、静态分析、D 代码解析等）
* [dfmt](https://github.com/dlang-community/dfmt) - D 源代码的格式化程序

## 构建工具

*管理项目并从源代码编译软件。*

* [dub](https://github.com/dlang/dub) - D 的事实上的官方软件包和构建管理系统。将很快正式包含在内。
* [scons-d](https://scons.org/) - 感谢 Russel Winder，Scons 内置了对构建 D 项目的支持。
* [premake](https://github.com/premake/premake-dlang) - Premake 内置了对 D 项目的支持
* [reggae](https://github.com/atilaneves/reggae) - D 中的元构建系统
* [Makefile](https://github.com/bioinfornatics/MakefileForD) - D 项目的 Makefile 模板
* [cmake-d](https://github.com/dcarp/cmake-d) - CMake D 项目
* [cook2](https://github.com/gecko0307/Cook2) - 适用于 D 语言项目的快速增量构建工具
* [button](https://jasonwhite.io/button/) - 通用构建系统，只需按一下按钮即可构建您的软件。
* [wild](https://github.com/Vild/Wild) - Wild构建系统，用于构建[PowerNex](https://github.com/PowerNex/PowerNex)内核
* [XMake](https://xmake.io) - XMake 是一个跨平台构建系统，它结合了 D 语言，并且还支持 DUB 存储库。
* [wox](https://github.com/redthing1/wox) - 受 Make 启发的高度灵活的配方构建系统

## IDE 和编辑器

*集成开发环境。*

* [Visual D](https://github.com/dlang/visuald) - D 编程语言的 Visual Studio 扩展。
* [IntelliJ D Language](https://intellij-dlanguage.github.io/) - IntelliJ IDEA 中支持 D 编程语言。
* [Dexed](https://gitlab.com/basile.b/dexed) - 用于 D 编程语言、其编译器、工具和库的 IDE。
* [Dutyl](https://github.com/idanarye/vim-dutyl) - 集成各种D开发工具的Vim插件
* [code-d](https://marketplace.visualstudio.com/items?itemName=webfreak.code-d) <sup>\[[open-vsx](https://open-vsx.org/extension/webfreak/code-d)\]</sup> - 使用serve-d的Visual Studio Code扩展
* [ide-d](https://packages.pulsar-edit.dev/packages/ide-d) - 使用serve-d 对 D 进行 Pulsar（Atom 分叉）扩展
* [DCD](https://github.com/dlang-community/DCD) - D 编程语言的独立自动完成程序。可与 vim、emacs、sublime text、textadept 和 zeus 等编辑器一起使用。请参阅[编辑器支持](https://github.com/dlang-community/DCD/wiki/IDEs-and-Editors-with-DCD-support)。
* [serve-d](https://github.com/Pure-D/serve-d) - D 的语言服务器协议 (LSP) 实现。为任何支持 LSP 的编辑器（VSCode、Atom、Vim/Neovim 等）添加现代 IDE 功能

## 词法分析器、解析器和生成器

* [libdparse](https://github.com/dlang-community/libdparse) - D 语言词法分析器和解析器，（可能）未来的标准 D 解析器/词法分析器。
* [Martin Nowak's Lexer](https://github.com/MartinNowak/lexer) - 词法分析器生成器。
* [Mono-D's DParser](https://github.com/aBothe/D_Parser) - 用 C# 编写并在 Mono-D 中使用的 D 解析器。
* [Pegged](https://github.com/dlang-community/Pegged) - 用 D 编写的解析表达式语法 (PEG) 模块。
* [Goldie](https://bitbucket.org/Abscissa/goldie/wiki/Home) - 戈尔迪解析系统。
* [ctpg](https://github.com/youxkei/ctpg) - 编译时解析器（带转换器） 用 D 编写的生成器。
* [dunnart](https://github.com/pwil3058/dunnart) - LALR(1) 用 D 编写的解析器生成器。

## 预处理器

* [warp](https://github.com/facebookarchive/warp) - Facebook 基础设施中使用的 C 和 C++ 快速预处理器。由沃尔特·布莱特撰写。

## 版本管理器

* [dvm](https://github.com/jacob-carlborg/dvm) - 一个安装和管理 DMD（自托管）编译器的小工具。
* [ldcup](https://github.com/kassane/ldcup) - 一个安装和管理LDC2（LLVM后端）编译器的小工具。


## GitHub 操作

* [setup-dlang](https://github.com/dlang-community/setup-dlang) - 在 GitHub Actions 中安装 D 编译器和 DUB
* [dub-upgrade](https://github.com/WebFreak001/dub-upgrade) - 运行“dub Upgrade”，尝试在网络故障时重复并使用 GitHub Actions 上的包缓存

## 测试框架

* [unit-threaded](https://github.com/atilaneves/unit-threaded) - 多线程单元测试框架
* [silly](https://gitlab.com/AntonMeep/silly) - 更好的 D 编程语言测试运行器。不废话。
* [fluent-asserts](https://github.com/gedaiu/fluent-asserts) - 流畅的断言框架，具有表达性语法和详细的错误消息。

## 编程语言

*用 D 编写的编程语言*

* [higgs](https://github.com/higgsjs/Higgs) - Higgs JavaScript 虚拟机，用 D 实现。
* [brainfuck-d](https://codeberg.org/GuineaPigUuhh/brainfuck-d) - Brainfuck 解释器、编译器和 REPL 用 D 编写。

## 操作系统

*用 D 编写的操作系统*

* [PowerNex](https://github.com/PowerNex/PowerNex) - 用 D 编写的内核
* [SerpentOS](https://gitlab.com/serpent-os) - 斯内克工厂
* [Trinix](https://github.com/Rikarin/Trinix) - 用 D 编写的 x64 PC 混合操作系统
* [XOmB](https://github.com/xomboverlord/xomb) - 用 D 编写的外内核操作系统

## 裸机/内核开发

* [D Bare bones](https://wiki.osdev.org/D_Bare_Bones) - D 中的内核 hello world（使用 GDC 编译器）
* [D barebone with ldc2](https://wiki.osdev.org/D_barebone_with_ldc2) - D 中的另一个内核 hello world（使用 LDC 编译器）
* [XOmB bare bones](https://web.archive.org/web/20161214232759/http://wiki.xomb.org/index.php?title=XOmB_Bare_Bones) - 用 D 编写的外内核操作系统。 [主页](https://web.archive.org/web/20161201061242/http://wiki.xomb.org/index.php?title=Main_Page), [github](https://github.com/xomboverlord/xomb/tree/unborn)。
* [Bare Metal ARM Cortex-M GDC Cross Compiler](https://wiki.dlang.org/Bare_Metal_ARM_Cortex-M_GDC_Cross_Compiler) - 为 Linux 主机构建裸机 ARM Cortex-M (arm-none-eabi) GDC 交叉编译器。

## 一般集装箱

*数据结构和容器库。*

* [EMSI containers](https://github.com/dlang-community/containers) - 不使用GC的容器
* [memutils](https://github.com/etcimon/memutils) - D 对象的开销分配器、分配器感知容器和生命周期管理
* [dlib.container](https://github.com/gecko0307/dlib) - 通用数据结构（无 GC 动态数组和关联数组等）
* [std.rcstring](https://github.com/burner/std.rcstring) - D 内置字符串构造的引用计数字符串实现

## 核心实用程序

*通用实用程序库。*

* [NuMem](https://github.com/Inochi2D/numem) - DLang 的无 GC 内存管理实用程序。
* [NuLib](https://github.com/Inochi2D/nulib) - D“标准”库构建在 numem 之上。
* [Joka](https://github.com/Kapendev/joka) - 一个 nogc 实用程序库。

## 网络框架

*网络库。*

* [dlang-requests](https://github.com/ikod/dlang-requests) - 受 python-requests 启发的 HTTP 客户端库
* [Handy-Httpd](https://github.com/andrewlalis/handy-httpd) - 一个简单、轻量级且文档齐全的 HTTP 服务器，可让您引导想法并在几分钟内启动并运行某些内容。
* [serverino](https://github.com/trikko/serverino) - 小型且随时可用的 http 服务器，D 语言
* [libasync](https://github.com/etcimon/libasync) - 异步对象的跨平台事件循环库
* [libhttp2](https://github.com/etcimon/libhttp2) - D 中的 HTTP/2 库，翻译自 nghttp2

*全栈网络框架。*

* [vibe.d](https://vibed.org/) - 异步 I/O Web 框架，不会妨碍您，用 D 编写。
* [arsd](https://github.com/adamdruppe/arsd) - Adam D. Ruppe 的 Web 框架。
* [cmsed](https://github.com/rikkimax/Cmsed) - 充当 CMS 的 Vibe 组件库。

*RPC 库。*

* [Apache Thrift](https://code.dlang.org/packages/apache-thrift) - 一个轻量级、独立于语言、功能强大的 RPC 框架。 Thrift 为数据传输、数据序列化、代码生成和应用程序级处理提供了干净的抽象。 [Apache Thrift 页面](https://thrift.apache.org/)
* [Hprose](https://github.com/hprose/hprose-d) - 一个非常新颖的 D RPC 库，现在支持 25 多种语言。

*静态站点生成器。*

* [DSSG](https://github.com/kambrium/dssg) - 采用不同方法的静态站点生成器。

## 数据序列化

*JSON、XML、protobuf等数据序列化库。*

* [cerealed](https://github.com/atilaneves/cerealed) - D 的序列化库
* [dproto](https://github.com/msoucy/dproto) - D 中的 Google Protocol Buffer 支持。

*JSON 库。*

* [vibe.data.json](https://vibed.org/api/vibe.data.json/) - Vibe.d 中的 JSON 函数。目前我使用的最好的实现。
* [fast.json](https://github.com/etcimon/fast) - 一个 D 库，旨在以最快的速度实现一些日常例程。
* [std.json](https://dlang.org/phobos/std_json.html) - D 的标准库 JSON 模块。需要细化。
* [painlessjson](https://github.com/BlackEdder/painlessjson) - 在 D 类型和 std.json 之间转换。
* [std.data.json](https://github.com/dlang-community/std_data_json) - 用于 JSON 序列化的 Phobos 候选者（基于 Vibed）
* [asdf](https://github.com/libmir/asdf) - 基于 JSON 表示的面向缓存字符串，用于快速读写和序列化。

*XML 库。*

* [orange](https://github.com/jacob-carlborg/orange) - 通用序列化器（目前仅支持XML）
* [std.experimental.xml](https://github.com/lodo1995/experimental.xml) - 用于 XML 序列化的 Phobos 候选者
* arsd [dom.d](https://github.com/adamdruppe/arsd/blob/master/dom.d) - 基于 Javascript 在浏览器中提供的 xml/html DOM
* [newxml](https://github.com/ZILtoid1991/newxml) - std.experimental.xml 的后继者。兼容 DOM，并且还具有 SAX 解析器。

## 数据库客户端

*关系数据库和 nosql 数据库的客户端和 C 客户端的绑定。*

* [vibe.d](https://github.com/vibe-d/vibe.d) - Vibe.d 内部支持 Redis 和 MongoDB，非常稳定。很快，数据库驱动程序将被分成独立的项目。
* [arsd](https://github.com/adamdruppe/arsd) - Adam D. Ruppe 的图书馆；除了 Web 后端之外，它还支持使用 database.d、sqlite.d、mysql.d 和 postgres.d 进行数据库访问。
* [hibernated](https://github.com/buggins/hibernated) - HibernateD 是 D 的 ORM（类似于 [Hibernate](https://hibernate.org/)）。
* [mysql-native](https://github.com/mysql-d/mysql-native) - 在本机 D 中实现的 MySQL 客户端。
* [ddb](https://github.com/pszturmaj/ddb) - D2 的数据库访问。目前仅支持 PostgreSQL。
* [ddbc](https://github.com/buggins/ddbc) - DDBC 是 D 语言的 DB Connector（类似于 JDBC）。 HibernateD（见下文）使用 ddbc 进行数据库抽象。
* [dvorm](https://github.com/rikkimax/Dvorm) - 具有 Vibe 支持的 D ORM。与 vivi.d 和 mysql-d 配合使用，使其能够访问 MongoDB 和 MySQL。
* [Tiny Redis](http://adilbaig.github.io/Tiny-Redis/) - D 的 Redis 驱动程序。快速、简单、稳定。没有依赖性。
* [libpb](https://github.com/Hax-io/libpb) - 与 PocketBase 数据库交互

## CLI 库

* [terminal.d](https://github.com/adamdruppe/arsd/blob/master/terminal.d) - Adam Ruppe 的 [arsd](https://github.com/adamdruppe/arsd) 库的一部分，支持控制台上的光标和颜色操作。
* [commandr](https://github.com/robik/commandr) - 一个现代、强大的命令行参数解析器。
* [argsd](https://github.com/burner/argsd) - DLang 的命令行和配置文件解析器
* [luneta](https://github.com/fbeline/luneta) - 命令行模糊查找器。
* [argparse](https://code.dlang.org/packages/argparse) - 命令行参数的灵活解析器。
* [gogga](https://github.com/deavmi/gogga) - 用于命令行应用程序的简单易用的彩色记录器
* [scriptlike](https://github.com/Abscissa/scriptlike) - 帮助在 D 中编写类似脚本的程序的实用程序库。
* [d-colorize](https://code.dlang.org/packages/colorize) - ruby 库 [colorize](https://github.com/fazibear/colorize) 的端口。它添加了一些方法，可以使用 ANSI 转义序列更轻松地在控制台上设置颜色、背景颜色和文本效果。
* [dexpect](https://github.com/grogancolin/dexpect/) - Expect 框架的 D 实现。对于 bash 模拟来说很方便。
* [Argon](https://github.com/markuslaker/Argon) - 命令行参数的处理器，是 Getopt 的替代品，用 D 编写。

## CLI 应用程序

* [Literate](https://github.com/zyedidia/Literate) - 适用于任何语言的文学编程工具。
* [onedrive](https://github.com/abraunegg/onedrive) - #1 适用于 Linux 的免费 OneDrive 客户端。
* [tshare](https://github.com/trikko/tshare) - 使用transfer.sh 从 cli 快速共享文件。
* [todod](https://github.com/BlackEdder/todod) - Todod 是一个基于命令行的待办事项列表管理器。它还支持基于 [linenoise](https://github.com/antirez/linenoise) 的 shell 交互。
* [Soulfind](https://github.com/soulfind-dev/soulfind) - Soulseek 服务器在 D 中的实现。

## 图形用户界面库

*用于使用图形用户界面应用程序的库。*

* [giD](https://github.com/Kymorphia/gid) - GObject Introspection D 包存储库。
* [Fluid](https://git.samerion.com/Samerion/Fluid) - D 的声明性跨平台用户界面库。
* [minigui](https://arsd-official.dpldocs.info/arsd.minigui.html) - 一个小型 GUI 小部件库，旨在至少与 HTML4 表单和一些其他预期的 GUI 组件相当。它是 [arsd 库](https://github.com/adamdruppe/arsd/blob/master/minigui.d) 的一部分。
* [DLangUI](https://github.com/buggins/dlangui) - D 编程语言的跨平台 GUI。我个人最喜欢，因为它是用 D 编写的（不是绑定），并且是跨平台的。 DLangUI 在 IDE [DLangIDE](https://github.com/buggins/dlangide) 中也有很好的展示。
* [microui-d](https://github.com/Kapendev/microui-d) - 一个小型即时模式 UI 库。
* [GtkD](https://github.com/gtkd-developers/GtkD) - GtkD 是 GTK+ 的 D 绑定和 OO 包装器。 GtkD 得到积极维护，是目前最稳定的 D GUI 库。
* [tkD](https://github.com/nomad-software/tkd) - 基于 Tcl/Tk 的 D 编程语言的 GUI 工具包。
* [dqml](https://github.com/filcuc/dqml) - D 编程语言的 Qt Qml 绑定。
* [Sciter-Dport](https://github.com/sciter-sdk/Sciter-Dport) - [Sciter](https://sciter.com) 的 D 绑定 - 跨平台 HTML/CSS/script 桌面 UI 工具包。

*注意*：您还可以在 [wiki.dlang.org](https://wiki.dlang.org/Libraries_and_Frameworks#GUI_Libraries) 上找到 GUI 库列表，但并非所有库现在都得到积极维护。

## 图形用户界面应用程序

* [tilix](https://github.com/gnunn1/tilix) - 使用 GTK+ 3 的 Linux 平铺终端模拟器。
* [Inochi Creator](https://github.com/Inochi2D/inochi-creator) - Inochi2D 索具应用程序。
* [Inochi Session](https://github.com/Inochi2D/inochi-session) - 允许使用 Inochi2D 木偶进行流式传输的应用程序。

## 游戏绑定

*绑定到 C、C++ 和其他语言的游戏开发相关库。*

* [raylib-d](https://github.com/schveiguy/raylib-d) - raylib 的 D 绑定。
* [sokol-d](https://github.com/floooh/sokol-d) - sokol 标头的 D 绑定。
* [DAllegro5](https://github.com/SiegeLord/DAllegro5) - D 绑定/包装到 Allegro 5，一个现代游戏编程库。
* [DSFML](https://github.com/Jebbs/DSFML) - 以对 D 有意义的方式进行 SFML 的静态绑定。
* [Godot-D](https://github.com/godot-d/godot-d) - Godot 引擎的 GDNative API 的 D 语言绑定。
* [BindBC](https://github.com/BindBC) - 使用 [bindbc-loader](https://github.com/BindBC/bindbc-loader) 与 `-betterC` 和 `@nogc` 兼容的绑定。
	* [OpenGL](https://github.com/BindBC/bindbc-opengl) - 图形API
	* [GLFW 3](https://github.com/BindBC/bindbc-glfw) - 窗口/输入库
	* [SDL 2](https://github.com/BindBC/bindbc-sdl) - 多媒体库
	* [SDL2_gfx](https://github.com/aferust/bindbc-sdlgfx) - SDL2 的绘图基元
	* [SFML 2](https://github.com/BindBC/bindbc-sfml) - 多媒体库
	* [Imgui](https://github.com/Inochi2D/i2d-imgui) - 立即模式 GUI
	* [Nuklear](https://github.com/Timu5/bindbc-nuklear) - 立即模式 GUI
	* [raylib3](https://github.com/o3o/bindbc-raylib3) - 游戏库
	* [bgfx](https://github.com/GoaLitiuM/bindbc-bgfx) - 跨平台渲染器
	* [WebGPU](https://github.com/DLangGamedev/bindbc-wgpu) - 现代 GPU API
	* [Zstandard](https://github.com/ZILtoid1991/bindbc-zstandard) - 快速压缩
	* [nanomsg-next-gen](https://github.com/darkridder/bindbc-nng) - 消息库
	* [OpenAL](https://github.com/BindBC/bindbc-openal) - 音频库
	* [SoLoud](https://github.com/DLangGamedev/bindbc-soloud) - 音频库
	* [KiWi](https://github.com/aferust/bindbc-kiwi) - UI小部件工具包
	* [NanoVG](https://github.com/aferust/bindbc-nanovg) - 矢量图形
	* [Blend2D](https://github.com/kdmult/bindbc-blend2d) - 矢量图形
	* [Lua](https://github.com/BindBC/bindbc-lua) - 脚本语言
	* [JoyShockLibrary](https://github.com/ZILtoid1991/bindbc-JSL) - 游戏手柄/陀螺仪输入
	* [Newton Dynamics](https://github.com/DLangGamedev/bindbc-newton) - 物理库
	* [FreeImage](https://github.com/BindBC/bindbc-freeimage) - 图片加载
	* [FreeType](https://github.com/BindBC/bindbc-freetype) - 字体渲染
	* [HarfBuzz](https://github.com/DlangGraphicsWG/bindbc-harfbuzz) - 文字塑造
* [DerelictOrg](https://github.com/DerelictOrg) - 绑定，现在基本上已经过时了。 BindBC 是它的现代继承者。
	* [OpenGLES](https://github.com/DerelictOrg/DerelictGLES) - 图形API
	* [ENet](https://github.com/DerelictOrg/DerelictENet) - 网络库
	* [libtheora](https://github.com/DerelictOrg/DerelictTheora) - 视频编解码器
	* [libogg](https://github.com/DerelictOrg/DerelictOgg) - 音频编解码器
	* [libvorbis](https://github.com/DerelictOrg/DerelictVorbis) - 音频编解码器
	* [libpq](https://github.com/DerelictOrg/DerelictPQ) - PostgreSQL 库
	* [PhysicsFS](https://github.com/DerelictOrg/DerelictPHYSFS) - 虚拟文件系统
	* [Open Dynamics Engine (ODE)](https://github.com/DerelictOrg/DerelictODE) - 物理库
	* [ALURE](https://github.com/DerelictOrg/DerelictALURE) - 音频库
	* [DevIL](https://github.com/DerelictOrg/DerelictIL) - 图片库

## 游戏库

*用于游戏开发的D库。*

* [InMath](https://github.com/Inochi2D/inmath) - D 的游戏数学库
* [godot-math](https://github.com/AuburnSounds/godot-math) - Godot 线性代数的 D 端口，语义不变。
* [text-mode](https://github.com/AuburnSounds/text-mode) - 具有 8x8 Unicode 字体和标记语言的虚拟文本模式。

*2D 相关项目的库。*

* [gfm](https://github.com/drug007/gfm7) - D 游戏开发工具包。
* [Parin](https://github.com/Kapendev/parin) - 一个非常简单的 2D 游戏引擎。
* [PixelPerfectEngine](https://github.com/ZILtoid1991/pixelperfectengine) - 用 D 编写的 2D 图形引擎。
* [HipremeEngine](https://github.com/MrcSnm/HipremeEngine) - 具有脚本支持的跨平台 D-Lang 游戏引擎。

*2D/3D 相关项目的库。*

* [rengfx](https://github.com/bmchtech/rengfx) - 轻量级、富有表现力、可扩展的 2D/3D 游戏引擎。

*3D 相关项目的库。*

* [Dagon](https://github.com/gecko0307/dagon) - D 的 3D 游戏引擎。参见：<https://gecko0307.github.io/dagon/>
* [Voxelman](https://github.com/MrSmith33/voxelman) - 用 D 语言编写的基于插件的客户端-服务器体素游戏引擎。

## 游戏

*用 D. 制作的游戏*

* [Spacecraft](https://github.com/Ingrater/Spacecraft) - 用 D 2.0 编写的 3D 多人死亡竞赛太空游戏。
* [Dtanks](https://github.com/kingsleyh/dtanks) - 机器人坦克对战游戏。
* [Electronvolt (formerly Atrium)](https://github.com/gecko0307/electronvolt) - 使用 OpenGL 进行基于物理谜题的 FPS 游戏。
* [Backgammony](https://github.com/jonathanballs/backgammony) - 使用 Gtk 构建的 Linux 西洋双陆棋 GUI。
* [Worms Within](https://kapendev.itch.io/worms-within) - 一款小型密室逃脱游戏。
* [Clean & Haunted](https://kapendev.itch.io/clean-haunted) - 清理阴森恐怖的鬼屋。
* [Runani](https://kapendev.itch.io/runani) - 一款无尽的跑酷游戏，您可以在其中帮助可爱的动物。
* [A Short Metamorphosis](https://kapendev.itch.io/a-short-metamorphosis) - 一部关于看鸡蛋的可爱视觉小说。

## 国际化

* [bindbc-icu](https://github.com/shoo/bindbc-icu) - Bindbc 绑定 unicode ICU 库。

## 图像处理

* [ArmageddonEngine](https://github.com/CyberShadow/ae/tree/master/utils/graphics) - Vladimir Panteleev 的 ae 库有一个用于函数式图像处理的包，在文章 [D 中的函数图像处理](https://blog.cy.md/2014/03/21/function-image-processing-in-d/) 中对此进行了描述。
* [dlib.image](https://github.com/gecko0307/dlib) - 图像处理（每通道 8 和 16 位、浮点运算、滤波、FFT、HDRI、图形格式支持，包括 JPEG 和 PNG）
* [color.d](https://github.com/adamdruppe/arsd/blob/master/color.d) + [bmp.d](https://github.com/adamdruppe/arsd/blob/master/bmp.d), [jpg.d](https://github.com/adamdruppe/arsd/blob/master/jpg.d), [png.d](https://github.com/adamdruppe/arsd/blob/master/png.d) - 基本颜色结构、HSL 函数以及读写图像文件
* [opencvd](https://github.com/aferust/opencvd) - D 的非官方 OpenCV 绑定

## 机器学习

* [vectorflow](https://github.com/Netflix/vectorflow) - Nexflix 的开源深度学习框架。
* [bindbc-onnxruntime](https://github.com/lempiji/bindbc-onnxruntime) - bindbc 绑定到 Microsoft 的跨平台、高性能 ML 推理和训练加速器
* [grain2](https://github.com/ShigekiKarita/grain2) - D 中动态神经网络的 Autograd 和 GPGPU 库
* [tfd](https://github.com/ShigekiKarita/tfd) - D 的 Tensorflow 包装器

## 并行计算

* [DCompute](https://github.com/libmir/dcompute) - [GPGPU与用于OpenCL和CUDA的Native D](https://dlang.org/blog/2017/07/17/dcompute-gpgpu-with-native-d-for-opencl-and-cuda/)
* [DerelictCUDA](https://github.com/DerelictOrg/DerelictCUDA) - 动态绑定到 D 编程语言的 CUDA 库。
* [DerelictCL](https://github.com/DerelictOrg/DerelictCL) - 动态绑定到 D 编程语言的 OpenCL 库。

## 科学的

*科学编程。*

* [scid](https://github.com/DlangScience/scid) - D 编程语言的科学库
* [dstats](https://github.com/DlangScience/dstats) - D 的统计库。
* [mir](https://github.com/libmir/mir) - 一些 mir 包的沙箱：稀疏张量、霍夫曼等。
* [mir-algorithm](https://github.com/libmir/mir) - N 维数组（矩阵、张量）、算法、通用库。
* [mir-random](https://github.com/libmir/mir-random) - 高级随机数生成器。

### 语言处理

* [bindbc-mecab](https://github.com/lempiji/bindbc-mecab) - bindbc MeCab 绑定（日语词性和形态分析器）

## 文本处理

* [hunt-markdown](https://github.com/huntlabs/hunt-markdown) - D 编程语言的 Markdown 解析和渲染库。支持通用标记。
* [eBay's TSV utilities](https://github.com/eBay/tsv-utils/) - 对TSV文件进行过滤、统计、采样、连接等操作。非常快，特别适合大型数据集。

## 记录

*小心打印。*

* [dlog](https://github.com/deavmi/dlog) - 可扩展的日志记录框架，具有消息转换支持和自定义记录器和上下文
* [std.experimenatal.logger](https://dlang.org/phobos/std_experimental_logger.html) - 火卫一即将推出的标准测井设施。
* [dlogg](https://github.com/NCrashed/dlogg) - 并发应用程序和守护程序的日志记录，具有惰性和延迟日志记录、logrotate 支持。

## 配置

*解析配置文件。*

* [sdlang](https://github.com/dlang-community/SDLang-D) - D 的 SDL（简单声明语言）库。
* [D:YAML](https://github.com/dlang-community/D-YAML) - D 编程语言的 YAML 解析器和发射器。
* [inifile-D](https://github.com/burner/inifiled) - D 的编译时 ini 文件解析器和编写器生成器

## 博客引擎

*自己托管博客。*

* [mood](https://github.com/mihails-strasuns/mood) - 简单的基于vibe.d的博客引擎

## 依赖注入

*应用控制反转。*

* [Poodinis](https://github.com/mbierlee/poodinis) - 支持自动装配的 D 依赖注入框架。

## 密码学

* [Botan](https://github.com/etcimon/botan) - 块和流密码、公钥加密、散列、KDF、MAC、PKCS、TLS、ASN.1、BER/DER 等。
* [OpenSSL](https://github.com/D-Programming-Deimos/openssl) - OpenSSL 的 C 标头的 D 版本。
* [Crypto](https://github.com/shove70/crypto) - 加密、解密、编码、散列和消息数字签名的 D 库。

## 无人维护

*保存旧的或存档的项目以供参考。*

* [dunit](https://github.com/nomad-software/dunit) - 高级单元测试和模拟工具包
* [hunt](https://github.com/huntlabs/hunt) - D 编程语言的精炼核心库。该模块有并发/集合/事件/io/日志记录/文本/序列化等。
* [hunt-time](https://github.com/huntlabs/hunt-time) - 一个时间库，类似于 Joda-time 和 Java.time api。
* [hunt-validation](https://github.com/huntlabs/hunt-validation) - 基于 Hunt 库的 DLang 数据验证库。
* [collie](https://github.com/huntlabs/collie) - 用 dlang 编写的异步事件驱动网络框架，类似于 D 中的 netty 框架。
* [hunt-net](https://github.com/huntlabs/hunt-net) - D编程语言的高性能网络库，事件驱动的异步实现（IOCP / kqueue / epoll）。
* [hunt-http](https://github.com/huntlabs/hunt-http) - D.HTTP/1 和 HTTP/2 协议库
* [Hunt Framework](https://github.com/huntlabs/hunt-framework/) - Hunt 是一个高级 D 编程语言 Web 框架，鼓励快速开发和简洁、实用的设计。它可以让您快速、轻松地构建高性能 Web 应用程序。
* [grpc](https://github.com/huntlabs/grpc-dlang) - Grpc 用于 D 编程语言，基于 Hunt-http 库。
* [kissrpc](https://github.com/huntlabs/kissrpc) - 快速、轻量、基于 Flatbuffers 的 RPC 框架。
* [hunt-gossip](https://github.com/huntlabs/hunt-gossip) - D 编程语言的 Apache V2 gossip 协议实现。
* [hunt-cache](https://github.com/huntlabs/hunt-cache) - D语言通用缓存库，使用radix、redis和memcached。
* [flatbuffers](https://github.com/huntlabs/flatbuffers) - 谷歌 Flatbuffers 库的 D 编程语言实现。
* [hunt-entity](https://github.com/huntlabs/hunt-entity) - Hunt 实体是 D 编程语言的对象关系映射工具。参考JPA的设计思想，支持PostgreSQL/MySQL/SQLite。
* [hunt-database](https://github.com/huntlabs/hunt-database) - Hunt数据库抽象层为D编程语言，支持PostgreSQL/MySQL/SQLite。
* [hunt-console](https://github.com/huntlabs/hunt-console) - Hunt 控制台创建更容易创建功能强大的命令行应用程序。
* [DWT](https://github.com/d-widget-toolkit/dwt) - 用于创建跨平台 GUI 应用程序的库。 GWT 是 Java SWT 库到 D 的端口。DWT 被提升为 D 的半标准 GUI 库，但不幸的是还没有流行起来。
* [LibUI](https://github.com/Extrawurst/DerelictLibui) - [libui]的动态绑定(https://github.com/andlabs/libui)
