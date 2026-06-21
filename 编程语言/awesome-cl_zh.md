<div align="center">
  <a href="https://awesome-cl.com" target="_blank">
    <img src="https://raw.githubusercontent.com/CodyReichert/awesome-cl/refs/heads/master/alien.png">
  </a>
</div>

# 很棒的 Common Lisp [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

一个很棒的 Common Lisp 库的精选列表。

此处列出的所有库均可从 [Quicklisp][16] 获得，除非
另有说明。标有 ⭐ 的应用非常普遍，而且
坚定地认为它们成为了社区标准。你不会错的
他们。 Quicklisp、BordeauxThreads 和
这样的。标有 👍 的图书馆是我们喜欢并想要的图书馆
在 Awesome-cl 列表中进行推广。他们被证明是可靠的，他们可以解决
一个比社区标准更好的问题，但它们并不那么好
广泛存在，或不被认为是稳定的。例如，我们更喜欢
Cl-Who 上方的喷丝板。

---

有关 *软件* 的列表，请参阅 [lisp-screenshots.org](https://www.lisp-screenshots.org/) 图库和
[awesome-cl-software](https://github.com/azzamsa/awesome-cl-software) 列表。

有关*公司*在生产中使用 CL 的示例，请参阅 [lisp-lang.org 的成功案例](http://lisp-lang.org/success/)，
[awesome-lisp-companies](https://github.com/azzamsa/awesome-lisp-companies/) 列表，
还有 [LispWorks 的成功故事](https://www.lispworks.com/success-stories/index.html)
以及[Allegro 的成功案例](https://franz.com/success/)。

---

添加新内容！请参阅 [contributing](#contributing) 部分以向
列表。

这是在 GNU 自由文档许可证下发布的 - 其文本
在 LICENSE 文件中提供。优先考虑[自由软件][13]并且
不为物质资源作恶的卖家。

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**目录**

- [人工智能（AI、法学硕士）](#artificial-intelligence-ai-llms)
  - [围绕 OpenAI API](#around-the-openai-api)
  - [MCP服务器](#mcp-servers)
  - [机器学习](#machine-learning)
  - [自然语言处理](#natural-language-processing)
  - [专家系统](#expert-systems)
  - [Educational](#educational)
- [Audio](#audio)
- [构建系统](#build-systems)
- [编译器、代码生成器](#compilers-code-generators)
  - [APL](#apl)
  - [C、C++](#c-c)
- [Cryptography](#cryptography)
- [Cryptocurrencies](#cryptocurrencies)
- [Database](#database)
  - [ORMs](#orms)
  - [持久对象数据库](#persistent-object-databases)
  - [图数据库](#graph-databases)
  - [其他数据库包装器](#other-db-wrappers)
  - [迁移工具](#migration-tools)
  - [致第三方](#to-third-parties)
  - [Tools](#tools)
- [数据格式](#data-formats)
  - [CSV](#csv)
  - [JSON](#json)
  - [TOML](#toml)
  - [XML](#xml)
  - [YAML](#yaml)
- [数据结构](#data-structures)
- [Docker 镜像](#docker-images)
- [外部函数接口、语言互操作](#foreign-function-interface-languages-interop)
  - [C](#c)
  - [Clojure](#clojure)
  - [Erlang](#erlang)
  - [Java](#java)
  - [Objective-C](#objective-c)
  - [Python](#python)
  - [.Net核心](#net-core)
  - [Emacs Lisp](#emacs-lisp)
- [游戏开发](#game-development)
- [Graphics](#graphics)
- [GUI](#gui)
  - [网页浏览量](#web-views)
  - [Mobile](#mobile)
- [Implementations](#implementations)
- [语言库](#language-libraries)
  - [Lisp 解析器](#lisp-parsers)
  - [树保姆语法](#tree-sitter-grammars)
- [语言扩展](#language-extensions)
  - [模式匹配](#pattern-matching)
  - [可移植层](#portability-layers)
  - [更改语法](#changing-the-syntax)
  - [CLOS 扩展](#clos-extensions)
  - [功能扩展](#function-extensions)
  - [Iteration](#iteration)
  - [Lambda 简写](#lambda-shorthands)
  - [非确定性逻辑编程](#non-deterministic-logic-programming)
  - [反应式编程](#reactive-programming)
  - [合约编程](#contract-programming)
  - [Typing](#typing)
  - [定理证明者](#theorem-provers)
- [学习和教程](#learning-and-tutorials)
  - [Online](#online)
  - [Beginner](#beginner)
  - [Intermediate](#intermediate)
  - [Advanced](#advanced)
  - [编码平台](#coding-platforms)
  - [网页开发](#web-development)
  - [Reference](#reference)
  - [Offline](#offline)
  - [Beginner](#beginner-1)
  - [Intermediate](#intermediate-1)
  - [Advanced](#advanced-1)
  - [其他书籍](#other-books)
  - [Community](#community)
  - [Showcase](#showcase)
- [图书馆经理](#library-manager)
  - [与其他包管理器的接口](#interfaces-to-other-package-managers)
- [网络和互联网](#network-and-internet)
  - [HTTP 客户端](#http-clients)
  - [HTTP 服务器](#http-servers)
    - [Hunchentoot 插件](#hunchentoot-plugins)
    - [叮当插件](#clack-plugins)
  - [网络框架](#web-frameworks)
    - [同构 Web 框架](#isomorphic-web-frameworks)
  - [解析html](#parsing-html)
  - [查询 HTML/DOM、网页抓取](#querying-htmldom-web-scraping)
  - [HTML 生成器和模板](#html-generators-and-templates)
  - [URI 和 IP 处理](#uri-and-ip-handling)
  - [Javascript](#javascript)
  - [Deployment](#deployment)
    - [托管平台](#hosting-platforms)
  - [Monitoring](#monitoring)
  - [Websockets](#websockets)
  - [HTTPS](#https)
  - [网络开发实用程序](#web-development-utilities)
    - [浏览器测试](#browser-tests)
    - [表格处理](#form-handling)
    - [用户登录和密码管理](#user-login-and-password-management)
    - [Web 项目框架和生成器](#web-project-skeletons-and-generators)
  - [Others](#others)
    - [Email](#email)
    - [OpenAPI、OData、OpenRPC](#openapi-odata-openrpc)
    - [静态站点生成器](#static-site-generators)
    - [第三方API](#third-party-apis)
- [数值与科学](#numerical-and-scientific)
  - [矩阵库](#matrix-libraries)
  - [Statistics](#statistics)
  - [Units](#units)
  - [Plotting](#plotting)
  - [Utils](#utils)
- [并行性和并发性](#parallelism-and-concurrency)
  - [演员图案](#actors-pattern)
  - [事件处理](#event-processing)
  - [作业处理](#job-processing)
- [正则表达式和字符串解析](#regular-expressions-and-string-parsing)
- [Scripting](#scripting)
  - [运行脚本](#running-scripts)
  - [命令行选项解析器](#command-line-options-parsers)
  - [Readline、ncurses 和其他图形 TUI 帮助程序](#readline-ncurses-and-other-graphical-tui-helpers)
  - [外壳、外壳接口](#shells-shells-interfaces)
  - [系统管理](#system-administration)
  - [更新可执行文件](#updating-executables)
  - [其他脚本实用程序](#other-scripting-utilities)
- [文本编辑器资源](#text-editor-resources)
  - [Emacs](#emacs)
  - [维姆和尼奥维姆](#vim--neovim)
  - [Eclipse](#eclipse)
  - [Lem](#lem)
  - [LispWorks](#lispworks)
  - [Mine - 适用于 Common Lisp 和 Coalton 的单次下载初学者友好 IDE](#mine---single-download-beginner-friendly-ide-for-common-lisp-and-coalton)
  - [原子、脉冲星](#atom-pulsar)
  - [崇高的文字](#sublime-text)
  - [VSCode](#vscode)
  - [JetBrains](#jetbrains)
  - [吉尼（实验）](#geany-experimental)
  - [Notebooks](#notebooks)
  - [REPLs](#repls)
  - [在线编辑](#online-editors)
- [文本和二进制解析器](#text-and-binary-parsers)
- [文本处理](#text-processing)
- [Tools](#tools-1)
- [单元测试](#unit-testing)
- [Utilities](#utilities)
  - [缓存（序列化）](#caching-serialization)
  - [缓存（记忆）](#caching-memoization)
  - [压缩/减压](#compression--decompression)
  - [Configuration](#configuration)
  - [日期和时间](#date-and-time)
  - [数据验证](#data-validation)
  - [开发者实用程序](#developer-utilities)
  - [文档构建者](#documentation-builders)
  - [文档查找](#documentation-lookup)
  - [文件和目录](#files-and-directories)
  - [Git](#git)
  - [i18n](#i18n)
  - [Linting、代码格式化](#linting-code-formatting)
  - [识字编程](#literate-programming)
  - [Logging](#logging)
  - [宏助手](#macro-helpers)
  - [Markdown](#markdown)
  - [包裹声明](#package-declarations)
  - [PDF](#pdf)
  - [项目骨架](#project-skeletons)
  - [Security](#security)
  - [系统界面](#system-interface)
  - [Other](#other)
- [Contributing](#contributing)

<!-- markdown-toc end -->

人工智能（AI、法学硕士）
==================================

## 围绕 OpenAI API

* [openai-openapi-client](https://codeberg.org/kilianmh/openai-openapi-client) - 半自动生成的 Openapi 客户端经常根据[官方 Openapi 规范](https://github.com/openai/openai-openapi/blob/master/openapi.yaml) 进行更新。 AGPL-3。
* 可在 Ultralisp 上使用。
* [cl-completions](https://github.com/atgreen/cl-completions) - 法学硕士完成。
* 可以轻松地在 Common Lisp 中创建 GPT 函数。
* 奥拉马支持。
* [cl-embeddings](https://github.com/atgreen/cl-embeddings) - LLM 嵌入。
* [cl-chroma](https://github.com/atgreen/cl-chroma) - 矢量数据库接口。

演示：[cl-rag-example](https://github.com/atgreen/cl-rag-example) 和 [cl-chat](https://github.com/atgreen/cl-chat)，一个 LLM 聊天库和 Web UI。

正在进行的工作：

* [Caten](https://github.com/hikettei/Caten) - 基于多面体编译器和轻量级 IR 的深度学习编译器以及优化模式匹配器，用 Common Lisp 编写

## MCP服务器

* [cl-MCP](https://github.com/cl-ai-project/cl-mcp) - 用于 Common Lisp 的 MCP。
* 通过 stdio 或 TCP 提供换行符分隔的 JSON-RPC 2.0 传输、小型协议层（初始化、ping、工具/列表、工具/调用）以及评估表单并返回最后值的 REPL 工具。
* [40ants-MCP](https://github.com/40ants/mcp) - 用于在 Common Lisp 中构建模型上下文协议服务器的框架。
* [mcp-lisp](https://github.com/jsulmont/mcp-lisp) - Common Lisp SDK for MCP (2025-11-25) 具有完全一致性（44/44 检查）和有限的 A2A 支持。支持 stdio 和 SSE 传输、工具、资源、提示、结构化错误和访问日志记录。 [麻省理工学院][200]。
* [Lisply MCP](https://github.com/gornskew/lisply-mcp) - 一个通用的 Node.js 包装器，几乎可以与任何支持“eval”和 http 的语言后端一起使用。
* 默认情况下，它配置为与现有的参考实现后端基于 CL 的容器映像配合使用，并将按需拉取并运行该容器映像。


## 机器学习

* [MGL](https://github.com/melisgl/mgl) - 用于反向传播神经网络、玻尔兹曼机、高斯过程等的机器学习库。 [麻省理工学院][200]。
* 一些部分最初由 Ravenpack International 提供。
* 被其[作者](https://github.com/melisgl)用来[赢得](https://github.com/melisgl/higgsml)希格斯玻色子机器学习挑战赛。
* 关于作者的更多信息：他还在 2010 年使用 Common Lisp 赢得了 Google [AI Challenge](https://en.wikipedia.org/wiki/AI_Challenge)，但没有使用 MGL，因为不需要机器学习。 [相关演讲](https://www.youtube.com/watch?v=7sgERtZkycU) (59', 2013)。
* [clml](https://github.com/mmaul/clml) - 最初由日本公司 Mathematicl Systems Inc. 开发。带有[教程](https://mmaul.github.io/clml.tutorials//2015/08/08/CLML-Time-Series-Part-1.html)。 [LLGPL][8]。
* [antik](https://www.common-lisp.net/project/antik/) - Common Lisp 中科学和工程计算的基础。通用公共许可证。还有 [mgl-mat](https://github.com/melisgl/mgl-mat) 和 [LLA](https://github.com/tpapp/lla)。

图片来源：borretti.me 的 [2015 年 CL 生态系统状况](http://borretti.me/article/common-lisp-sotu-2015#machine-learning)。

* [llama.cl](https://github.com/snunez1/llama.cl) - Llama 推理操作的实现。麻省理工学院。
*“使研究人员和开发人员能够在 Common Lisp 生态系统中探索 LLM 技术，利用该语言的交互式开发功能以及与符号 AI 系统的集成。”

## 自然语言处理

* 🚀 [sparser](https://github.com/ddmcdonald/sparser) - 英语自然语言理解系统。 [日食][209]。
*> 模型驱动、基于规则的语言文本分析系统，用于大容量、高精度信息提取。从本质上讲，Sparser 是一个自下而上、基于短语结构的图表解析器，针对语义语法和部分解析进行了优化。
* [cl-nlp](https://github.com/vseloved/cl-nlp) - 自然语言处理工具集。 [Apache2.0][89]。
* [babel2](https://github.com/lucas8/Babel2/) - 流体构造语法实现、计算框架和基于统一的语法形式[Apache2.0][89]。

## 专家系统

* [Lisa](https://github.com/youngde811/Lisa) - 一个生产质量的前向链接专家系统外壳，具有 Charles Forgy 的 Rete 算法的优化实现，该算法是解决困难的多对多模式匹配问题的高效解决方案。麻省理工学院。
* [WouldWork](https://github.com/davypough/wouldwork) - 无需丰富的编程经验即可解决经典的规划和约束满足问题。 BSD_3 条款。

## 教育性

* [PAIP-lisp](https://github.com/norvig/paip-lisp) - 教科书的 Lisp 代码 [“人工智能编程范式”](https://norvig.github.io/paip-lisp/#/)。
* [AIMA-lisp](https://github.com/aimacode/aima-lisp) - Russell 和 Norvig 的“人工智能 - 一种现代方法”中的算法的 Common Lisp 实现。
* Richard S. Sutton 和 Andrew G. Barto 所著的书 [强化学习：简介](http://www.incompleteideas.net/book/the-book.html)，包含 Lisp 代码。
* 作者是 [2024 ACM A.M.图灵奖](https://awards.acm.org/about/2024-turing) 表彰强化学习的概念和算法基础。
* [microgpt](https://github.com/40ants/microgpt) - @karpathy microgpt.py 的 Common Lisp 端口 — 具有手写标量 autograd 引擎的 GPT 的最原子实现。


音频
=====

音乐构成：

* [OpenMusic](https://github.com/openmusic-project/openmusic/) 可视化编程/计算机辅助作曲环境。 [GPL3][2]。在法国 [IRCAM](https://www.stms-lab.fr/team/representations-musicales/) 开发。
* [OM7](https://github.com/openmusic-project/om7) - OpenMusic 可视化编程和计算机辅助作曲环境的新实现，包括图形界面、计算模式以及与外部软件库的连接方面的多项改进。 [GPL3][2]。
* 扩展：[rq](https://github.com/openmusic-project/RQ) - OpenMusic 中节奏转录的库（版本 6.10 及更高版本）。 [演示视频](https://www.youtube.com/watch?v=XVEllB0TtVs)。 [GPL3][2]。
* [Incudine](http://incudine.sourceforge.net/) - Common Lisp 的音乐/DSP 编程环境。对于从头开始设计软件合成器或声音插件很有用。它也是一种作曲工具，可以在样本级别产生可控制的高质量声音，从而动态定义和重新定义数字信号处理器和音乐结构。
* [CLM](https://ccrma.stanford.edu/software/clm/) - Common Lisp Music 是 Music V 系列中的音乐合成和信号处理包。它提供了与 Stk、Csound、SuperCollider、PD、CMix、cmusic 和 Arctic 几乎相同的功能——一组创建和操作声音的函数，主要针对作曲家（无论如何，在 CLM 的情况下）。
  * [common-tones](https://github.com/theraphonics/common-tones) - CLM5 与现代 Lisp 的分支（ASDF、cffi...）。 [BSD_3 条款][15]。
* [Slippery Chicken](https://github.com/mdedwards/slippery-chicken/) - 算法作曲库，通过 Lilypond 输出 Midi、通用音乐符号、pdf 乐谱，通过 Common Lisp Music 输出声音。 [GPL3][2]。
* 附带文档：https://michael-edwards.org/sc/
* [Common Music](https://github.com/ormf/cm) - 的存储库
Common Music 的古代版本（2.12.0 版），大概是
在 Common Lisp 上运行的最后一个版本可以追溯到 2007 年 9 月左右，
在 Common Music 的工作转向（基于方案）cm3 之前。
* 注意：旧项目但有效。
  * [cm-incudine](https://github.com/ormf/cm-incudine) - 扩展了 Common Music 2 的实时功能。 GPL2。
* [cl-patterns](https://github.com/defaultxr/cl-patterns) - 一个通过 Lisp 代码创作音乐的系统，深受 SuperCollider 模式系统的启发，旨在实现其中的大部分内容，但以更强大、更具表现力、一致、反思和 lispy 的方式。通过 SuperCollider 进行音频输出，初步支持 Incudine，并通过 ALSA 进行 MIDI 输出。
* [Music](https://github.com/MegaLoler/Music) - Lisp 中的音乐表达框架，重点是音乐理论（从头开始构建，与通用音乐无关）。

解码器、声音处理：

* [Harmony](https://shirakumo.github.io/harmony) - 实时声音处理和播放系统。 [zlib][33]。
*“为您提供音频处理工具以及音频服务器来播放音乐、音效等。”
* 使用 [cl-mixed](https://github.com/Shirakumo/cl-mixed) 进行混音和声音处理库。
* [easy-audio](https://github.com/shamazmazum/easy-audio) - 音频解码器和元数据读取器的集合。

其他：

* [scheduler](https://github.com/byulparan/scheduler) - Common Lisp 的基于时间的音乐事件调度程序。 [Apache2.0][89]。
* [Common Music Notation](https://ccrma.stanford.edu/software/cmn/) - 通用乐谱 (CMN) 提供了一组函数来分层描述乐谱。公共领域。
* [osc](https://github.com/zzkt/osc) - 开放声音协议的实现。 [LGPL2.1][11]。

与其他软件和库的绑定和客户端：

* [cl-mpg123](https://github.com/Shirakumo/cl-mpg123), [cl-opus](https://github.com/Shirakumo/cl-opus) (OGG/Opus), [cl-vorbis](https://github.com/Shirakumo/cl-vorbis) (OGG/Vorbis), [cl-SoLoud](https://github.com/Shirakumo/cl-soloud)、[cl-out123](https://github.com/Shirakumo/cl-out123) (libout123)、[cl-flac](https://github.com/Shirakumo/cl-flac)
* [csound](https://github.com/csound/csound) - 声音和音乐计算系统。包括 Common Lisp 的 CFFI 和 FFI 接口。
* [cl-collider](https://github.com/byulparan/cl-collider) - CommonLisp 的 [SuperCollider](http://supercollider.github.io/) 客户端。带有[教程](https://github.com/defaultxr/cl-collider-tutorial)和[实时编码演示](https://www.youtube.com/watch?v=xzTH_ZqaFKI)。公共领域。
* [cl-openal](https://github.com/zkat/cl-openal) - OpenAL 音频库的绑定。公共领域。

以及 [awesome-cl-software#audio](https://github.com/CodyReichert/awesome-cl#audio) 上更多针对音乐家的音频软件（Opus Modus、OpenMusic...）。



构建系统
=============

* ⭐[ASDF](https://common-lisp.net/project/asdf/) - 另一个系统定义工具； Common Lisp 的构建系统。 [外籍人士][14]。 Quicklisp（请参阅[库管理器](#library-manager)）在底层使用 ASDF。
* [已知的 ASDF 扩展](https://common-lisp.net/project/asdf/#extensions)，例如 `asdf-system-connections`，它允许您指定在加载其他两个系统时自动加载的系统，以连接它们。
* [asdf-viz](https://github.com/guicho271828/asdf-viz) - 一个可视化 ASDF 系统的库依赖关系、函数调用图和类继承的工具。 [LLGPL][8]。


另请参阅：

* [modularize](https://codeberg.org/shinmera/modularize) - Common Lisp 的模块化框架。 [zlib][33]。
* 提供一个通用接口来隔离主要的应用程序组件。
* 例如，通过添加模块定义选项，您可以引入将模块在功能上捆绑在一起、相互挂钩等的机制。
* 充当 `defpackage` 的包装器并集成到 ASDF 中。
* [asdf-linguist](https://github.com/eudoxia0/asdf-linguist) - ASDF 的扩展，用于编译各种语言并在项目中的文件上运行各种预处理工具。 [外籍人士][14]。
* Sass、LESS、Myth、C、C++、Fortran、CSS/JS 压缩器、ParensScript、Make、CMake、org-mode、pandoc、dot、diita…
* 目前已存档且未维护。
* [asdf-dependency-traverser](https://codeberg.org/johnlorentzson/asdf-dependency-traverser/) - 一个用于遍历 ASDF 系统的依赖树的小实用程序。兹利布。


编译器、代码生成器
==========================

APL
---

* [April](https://github.com/phantomics/april) - APL 编程语言（其子集）编译为 Common Lisp。用一行 APL 替换数百行数字运算代码。 [阿帕奇2][89]。


C、C++
------

* [C-mera](https://github.com/kiselgra/c-mera) - 一个源到源的编译器，利用 Lisp 的宏系统对类 C 语言进行元编程。 [GPL3][2]。
* [lispc](https://github.com/eratosthenesia/lispc) - 一种强大的 C 语言“lispsy”宏语言。[MIT][200]。
* [with-c-syntax](https://github.com/y2q-actionman/with-c-syntax) - 一个有趣的包，它将 C 语言语法引入 Common Lisp。 （是的，我认为这个包不适用于实际编码。）WTFPL 许可证。
* [ecrepl](https://gitlab.common-lisp.net/ecl/ecrepl) - C 语言的交互式 REPL。 [BSD_2 条款][17]。
* [Software-Evolution-Library](https://github.com/GrammaTech/sel) - SEL 支持对软件进行编程修改和评估（使用 Clang、编译的汇编程序和链接的 ELF 二进制文件支持 C/C++）。 [GPL3][2]。
* [vacietis](https://github.com/vsedach/Vacietis) - C 到 Common Lisp 编译器。 [LGPL3][9]。
* 自 2025 年起新增 [Cicili](https://github.com/saman-pasha/cicili/) - C 生成器宏驱动语言。 GPL3.0。
*“可以使用 lisp 库为内部 C 生成的代码生成编译时内容，如 html、json、sql 等”。

密码学
============

* ⭐ [Ironclad](https://github.com/sharplispers/ironclad) - Common Lisp 的加密函数库。不被认为是安全的，但对于消息摘要功能仍然有用。 [外籍人士][14]。
* [crypto-shortcuts](https://codeberg.org/shinmera/crypto-shortcuts) - 常见加密快捷方式的集合。 [zlib][33]。
* [cl-ssh-keys](https://github.com/dnaeon/cl-ssh-keys) - 用于生成和解析 OpenSSH 密钥的 Common Lisp 系统。 [BSD_3 条款][15]。
* [cl-bcrypt](https://github.com/dnaeon/cl-bcrypt) - 用于解析和生成 bcrypt 密码哈希值的 Common Lisp 系统。 [BSD_3 条款][15]。
* [gpgme](https://www.gnupg.org/download/index.en.html#gpgme) (GnuPG Made Easy) 是从编程语言访问 GnuPG 函数的标准库。它提供了官方的 Common Lisp 系统。
* [gpgme lisp 源代码](https://git.gnupg.org/cgi-bin/gitweb.cgi?p=gpgme.git;a=tree;f=lang/cl;h=05151bdf839e513f534a1b423d59332a2e46fd5d;hb=HEAD)（不在 Quicklisp 中）。 GPL2。
* [cl-frugal-uuid](https://github.com/ak-coram/cl-frugal-uuid/) - 零依赖的 Common Lisp UUID 库。 [麻省理工学院][200]。

加密货币
================

* [bitcoin-core-rpc](https://codeberg.org/kilianmh/bitcoin-core-rpc/) - 一个（希望）完整的比特币核心 RPC 客户端。 [AGPL-3.0+][agpl3]
* [bp](https://github.com/rodentrabies/bp) - Common Lisp 中的比特币协议组件。 [麻省理工学院][200]。
* [peercoin-blockchain-parser](https://github.com/glv2/peercoin-blockchain-parser) - 解析文件中包含的区块链并将其部分数据导出到文本文件、SQL 脚本或数据库。它还可以使用 Peercoin 守护程序的 RPC 作为数据源而不是区块链文件来创建数据库。 LGPL3。不在 Quicklisp 中。
* [peercoin-calculator](https://github.com/glv2/peercoin-calculator) - 该计划为您提供在 10 分钟、24 小时、31 天、90 天和 1 年内生成 POS 或 POW 区块的概率，以及可预期的奖励。 Qt 中的 GUI。 [GPL3][2]。不在 Quicklisp 中。
* [peercoin-vote](https://github.com/glv2/peercoin-vote) - 基于区块链数据（地址和余额）的投票系统。 [GPL3][2]。不在 Quicklisp 中。
* [stacks-api](https://github.com/kilianmh/stacks-api) - Stacks API 客户端。 [AGPL-3.0][89]

另请参阅 [legochain](https://github.com/defunkydrummer/legochain)，一个简单的教育区块链； [emotiq](https://github.com/emotiq/emotiq)，一种下一代区块链，采用创新的自然语言方法来构建 Common Lisp 中的智能合约（已停止）。

数据库
========

* ⭐ [postmodern](http://marijnhaverbeke.nl/postmodern/) - 用于与 PostgreSQL 交互的库。 [zlib][33]。
* [cl-dbi](https://github.com/fukamachi/cl-dbi) - Common Lisp 的独立于数据库的接口。 [LLGPL][8]。
* [sxql](https://github.com/fukamachi/sxql) - 用于生成 SQL 的 DSL。 [3 条款 BSD][15]。
* 截至 2025 年 10 月的新功能：[可组合查询生成器](https://github.com/fukamachi/sxql/blob/master/COMPOSER.md)。查询成为一流的值，可以派生、组合和重用，而不会产生副作用。
* [cl-sqlite](https://github.com/dmitryvk/cl-sqlite) - SQLite 的绑定。公共领域。
* [cl-yesql](https://github.com/ruricolist/cl-yesql) - SQL 语句以 SQL 语法存在于它们自己的文件中，并作为函数导入到 Lisp 中。您不受 DSL 支持的功能的限制。基于 Clojure 的 Yesql。 [麻省理工学院][200]。

另请参阅：

* [endatabas](https://github.com/endatabas/endb) - 具有完整历史记录的无模式 SQL 文档数据库。 [AGPL-3.0][89]。
- 用 Common Lisp 和 Rust 构建，正在开发中。

ORM
----

* 👍 [mito](https://github.com/fukamachi/mito) - Common Lisp 的 ORM，具有迁移、关系和 PostgreSQL 支持 [BSD_3Clause][15]。
* [mitho-auth](https://github.com/fukamachi/mito-auth)，一个用于使用授权的mixin类
* [mito-attachment](https://github.com/fukamachi/mito-attachment)，一个用于 RDBMS 之外的文件管理的 mixin 类。
* 与 SxQL 及其查询编辑器配合使用效果最佳。
* [clsql](http://www.cliki.net/CLSQL) - 具有 Common Lisp 接口的 SQL 数据库。 [LLGPL][8]。
  * [dbd-oracle](https://github.com/sergadin/dbd-oracle) - CL-DBI 的 Oracle 数据库驱动程序。 [LLGPL][8]。
* [datafly](https://github.com/fukamachi/datafly) - 一个轻量级的数据库。 [3 条款 BSD][15]。

持久对象数据库
---------------------------

* bknr.datastore - RAM 中基于 CLOS 的仅 lisp 数据库，具有事务日志持久性。 [手册](https://www.common-lisp.net/project/bknr/html/documentation.html)。 [许可证][208]。
* 活跃且重要的分叉：[tdrhk/bknr-datastore](https://github.com/tdrhq/bknr-datastore)
  * [原始存储库](https://github.com/hanshuebner/bknr-datastore)
*另请参阅这篇[很好的介绍性博客文章](https://ashok-khanna.medium.com/persistent-in-memory-data-storage-in-common-lisp-b-k-n-r-37f8ae76042f)
* 使用 bknr.datastore 的示例 Web 应用程序：[screenshotbot-oss](https://github.com/screenshotbot/screenshotbot-oss)。
* 如果您想要高可用的 bknr.datastore 复制版本，另请参阅 [bknr.cluster](https://github.com/tdrhq/bknr.cluster)。 [博客文章](https://screenshotbot.io/blog/building-a-highly-available-web-service-without-a-database)。
* [ubiquitous](https://codeberg.org/shinmera/ubiquitous) - 提供易于使用的持久配置存储的库。 [zlib][33]。
* [cl-prevalence](https://common-lisp.net/project/cl-prevalence/) - 内存数据库系统。对象普遍性的实现，其中业务对象保留在内存中，并记录事务以供系统恢复。 [github 分支](https://github.com/40ants/cl-prevalence)。 [LLGPL][8]。
* 另请参阅 [cl-prevalence-multimaster](https://github.com/40ants/cl-prevalence-multimaster)，以同步多个 cl-prevalence 系统状态。

另请参阅[缓存（序列化）](#caching-serialization) 部分。

图数据库
---------------

* [AllegroGraph](https://allegrograph.com/) - 一种高性能、多模型（文档和图）、实体事件知识图谱技术。
* 专有，免费版本限制为 500 万个 RDF 三元组。
* 使用[托管版本](https://allegrograph.cloud/)
* AllegroGraph 8.0 - “将大型语言模型 (LLM) 组件直接合并到 SPARQL 中，以及向量生成和向量存储，以实现全面的 AI 知识图解决方案。”
* [cl-agraph](https://github.com/vseloved/cl-agraph)，AllegroGraph 的最小客户端。
* [neo4cl](https://codeberg.org/Equill/neo4cl) - 用于与 Neo4J 交互的库。将 Cypher 查询发送到 Neo4J 服务器，并将响应解码为可用于 CL 处理的内容。 [阿帕奇2][89]。
* 或许： [cl-neo4j](https://github.com/kraison/cl-neo4j) - 一个精简的 neo4j RESTFUL 客户端界面。
* [vivace-graph](https://github.com/kraison/vivace-graph-v3) - 图数据库和 Prolog 实现。从 CouchDB、neo4j 和 AllegroGraph 获取设计灵感。它使用用户定义的索引和映射缩减视图实现符合 ACID 的对象图模型。它还实现了主/从复制方案，以实现冗余和水平读取扩展。查询图是通过许多 Lisp 方法或类似 Prolog 的查询语言来完成的。 [麻省理工学院][200]。
* “我使用 Vivace Graph 作为数百万产品的在线目录，作为复杂、适应性强的基于 VoIP 的 IVR 的后端，以及多个复杂大数据分析系统的数据存储，最后作为两个推荐系统的引擎。” （问题＃23）
* “为什么 vivace graph 这么快？我一直在将它与基于 SQL 的方法和 Neo4j 进行比较，vivace graph 快得多。”
* [Ariadne](https://git.sr.ht/~hajovonta/ariadne) - Common Lisp 中的图形数据库，具有完整的 W3C SPARQL 1.1 和 SHACL 一致性、Gremlin 式遍历、RDF 导入/导出、属性图支持、推理规则、图形分析和 Graphviz 可视化。
* *由法学硕士构建*。

还有：

* [restagraph](https://github.com/JermellB/restagraph) - 一个使用数据库中定义的模式为 Neo4j 数据库动态生成 REST API 的应用程序。 [GPL3][2]。

<!-- lost in translation: (it was slow anyways) -->
<!-- * [facts](https://github.com/cl-facts/facts) - an in-memory graph database with transactions and rollbacks, logging/replay and dumping/loading to/from disk. BSD-style license (ISC). -->


其他数据库包装器
-----------------

* [cl-memcached](https://github.com/quasi/cl-memcached) - Memcached 对象缓存系统的快速、线程安全接口。 [外籍人士][14]。
* [cl-redis](https://github.com/vseloved/cl-redis) - Redis 客户端。 [外籍人士][14]。
* [cl-disque](https://github.com/CodyReichert/cl-disque) - 磁盘客户端。 [3 条款 BSD][15]。
* [cl-rethinkdb](https://github.com/orthecreedence/cl-rethinkdb) - RethinkDB 客户端。 [外籍人士][14]。
* [cl-mango](https://github.com/cmoore/cl-mango/) - 极简的 CouchDB 2.x 数据库客户端。 BSD_3 条款。
* 另请参阅 [clouchdb](https://common-lisp.net/project/clouchdb/) - 用于与 CouchDB 交互的库。 [FreeBSD][39]。
* [lmdb](https://github.com/melisgl/lmdb) - 绑定到 [LMDB](http://www.lmdb.tech/doc/)、Lightning 内存映射数据库、具有多版本并发控制的 ACID 键值数据库。
* [cl-ndbapi](https://github.com/datagraph/cl-ndbapi) - 绑定到 [RonDB](https://www.rondb.com/) 的 C++ NDB API，“世界上最快的键值存储”，作者：[Dydra](https://dydra.com/home)。 GPLv2。
* [cl-duckdb](https://github.com/ak-coram/cl-duckdb) - Common Lisp CFFI 围绕 DuckDB C API 的包装器。 [麻省理工学院][200]。
* [cl-bunny](https://github.com/cl-rabbit/cl-bunny) - 基于 IOLib 的 Common Lisp RabbitMQ 客户端。麻省理工学院。

迁移工具
---------------

（回想一下 Mito 处理迁移）

* [cl-migratum](https://github.com/dnaeon/cl-migratum) - 提供用于执行数据库模式迁移的工具的系统，旨在与各种数据库一起使用。 [BSD_3 条款][15]。
* [postmodern-passenger-pigeon](https://github.com/fisxoj/postmodern-passenger-pigeon/) - 后现代的迁移经理。未指定许可证。


致第三方
----------------

* [dyna](https://github.com/Rudolph-Miller/dyna) - AWS DynamoDB ORM。 [麻省理工学院][200]。
* [cl-influxdb](https://github.com/mmaul/cl-influxdb/) - 时间序列数据库 InfluxDB 的接口。 [麻省理工学院][200]。
* [cl-remizmq](https://fossil.cyberia9.org/cl-remizmq/index) - ZeroMQ 套接字、消息、计时器、原子和代理。
* 低级和高级 API。使用 libzmq 5.2.5 进行测试，任何 v4.x 和 v5.x 都应该可以工作，v3.x 也可以。
* [coalton-zmq](https://github.com/coalton-lang/coalton-zmq) - Coalton 的 ZeroMQ 接口。
- “它足够完整，可用于构建使用 ZeroMQ 的应用程序”。许多官方 [ZeroMQ 示例](https://github.com/coalton-lang/coalton-zmq/tree/main/zmq-examples) 都已实现。

工具
-----

* ⭐ [pgloader](https://github.com/dimitri/pgloader) - PostgreSQL 的数据加载工具。 [PostgreSQL 许可证][205]。
* 必填博客文章：[为什么 pgloader 这么快？](https://tapoueh.org/blog/2014/05/why-is-pgloader-so-much-faster/)（提示：它是从 Python 重写为 Common Lisp）

数据格式
============

CSV
---

* ⭐ [cl-csv](https://github.com/AccelerationNet/cl-csv) - 用于解析 CSV 文件的库。 [3 条款 BSD][15]。
  * [documentation](https://github.com/AccelerationNet/cl-csv/blob/master/DOCUMENTATION.md)
* [示例博客文章](https://dev.to/vindarel/read-csv-files-in-common-lisp-cl-csv-data-table-3c9n)。
* [cl-decimals](https://github.com/tlikonen/cl-decimals) - 十进制数解析器和格式化器。公共领域。
* [auto-text](https://github.com/defunkydrummer/auto-text) - 文本文件的自动（编码、行尾、列宽、csv 分隔符等）检测。 [麻省理工学院][200]。另请参阅 [inquisitor](https://github.com/t-sin/inquisitor) 以检测亚洲和远东语言。
* [csv-validator](https://github.com/KoenvdBerg/csv-validator) - 使用预定义的验证来验证表格 CSV 数据，其灵感来自于其 Python 同源“Great Expectations”。 [BSD_3 条款][15]。

另请参阅：用于快速解析的 cl-duckdb、[lisp-stat 的数据帧 `read-csv`](https://lisp-stat.dev/docs/manuals/data-frame/)、[vellum-csv](https://github.com/sirherrbatka/vellum-csv/) （数据帧库）、vellum-duckdb。

JSON
----

* 👍 [jzon](https://github.com/Zulu-Inuoe/jzon/) - 一个正确、安全、快速的 JSON 解析器。 [麻省理工学院][200]。
* jzon 是唯一一个 CL JSON 库，它可以正确拒绝每个官方 JSON 测试套件的所有无效输入，并接受该套件的所有有效输入。
* 它不会因无效输入而崩溃（jsown），不会因大型数据集而阻塞（Jonathan）等等。
* “我相信 jzon 是更好的选择，并希望它一劳永逸地成为 JSON-in-CL 领域新的、真正的事实上的库。”
* [shasht](https://github.com/yitzchak/shasht) - 用于 Kzinti 的 Common Lisp JSON 读写。 [麻省理工学院][14]。
- “Shasht 是我特别喜欢的两个新库之一，并且已经在 Quicklisp 中。它速度快，可以正确处理 null，它可以对 CLOS 对象、结构和哈希表进行编码。它还可以进行增量编码。”萨布拉·克罗尔顿。
* [cl-json](https://github.com/sharplispers/cl-json) - 高度可定制的 JSON 编码器和解码器。 [麻省理工学院][14]。
*“如果你需要精细控制，cl-json 和 yason 仍然是主力，但速度不是他们的强项。” @sabracrolleton
* [parcom/json](https://github.com/fosskers/parcom) - “parcom”的扩展，用于简单、快速、无依赖的 JSON 解析。

请参阅更多 JSON 库的[广泛比较](https://sabracrolleton.github.io/json-review)，以及[这些基准](https://github.com/fosskers/parcom?tab=readme-ov-file#json-benchmarks)。

JSON 工具：

* [NJSON](https://github.com/atlas-engineer/njson) - 与解析器无关的 JSON 索引（支持 JSON 指针）、解构和验证框架。 [BSD][15]。
* [json-mop](https://github.com/gschjetne/json-mop) - 用于桥接 CLOS 和 JSON 对象的元类。 [麻省理工学院][200]。
* 取决于亚森
* 对于本身不执行此操作的 JSON 库（jzon、shasht 和 cl-json 能够将 CLOS 对象“编码”为开箱即用的 JSON，并且 cl-json 能够将 JSON 对象“解码”为“流体类”CLOS 对象。）
* [cl-json-pointer](https://github.com/y2q-actionman/cl-json-pointer) - JSON 指针实现。 [麻省理工学院][200]。
* [cl-jwk](https://github.com/dnaeon/cl-jwk) - 用于解码公共 JSON Web 密钥 (JWK) 的 Common Lisp 系统。 BSD 许可证。
* [JOSE](https://github.com/fukamachi/jose) - Common Lisp 的 JSON 对象签名和加密 (JOSE) 实现。 BSD_2 条款。
* [cl-jsonpath](https://git.sr.ht/~hajovonta/cl-jsonpath) - Common Lisp 的 JSONPath 实现，具有 99% 的测试合规性和完全的现实兼容性。麻省理工学院。内置人工智能。
* [cl-json-utils](https://git.sr.ht/~q3cpma/cl-json-utils) - 查询 JSON，受到 lisp-ier 的 JSONPath 的启发。
* jsonpath: `$.store.book[*].author`, json-utils: `(query $ "store" "book" :wild "author")`

JSON在线服务：

* [pantry](https://github.com/dotemacs/pantry) - [Pantry JSON 存储服务](https://getpantry.cloud/) 的客户端库。 BSD。

并在下面搜索 JSON RPC。

TOML
----
* [parcom/toml](https://github.com/fosskers/parcom) - “parcom”的扩展，用于简单、无依赖的 TOML 解析。
* [clop](https://github.com/sheepduke/clop) - 兼容 1.0 的 TOML 解析器。

XML
---

* [CXML](https://common-lisp.net/project/cxml/) - XML 解析器和序列化器，以及一系列扩展库。 [LLGPL][8]。
- 👍 有一个增量解析器，允许解析大文件。
- 请参阅 [FXML](https://github.com/ruricolist/FXML) 分支，其中包含修复和新功能。如果您正在解析可能格式不正确或恶意的 XML，或者需要将 Klacks 与命名空间一起使用，则应该使用它。
* [Plump][71] - 一个宽松的 XML 解析器。 [zlib][33]。
* [parcom/xml](https://github.com/fosskers/parcom) - “parcom”的扩展，用于简单、快速的 XML 解析。
* [xpath](https://github.com/sharplispers/xpath) ([主页](https://common-lisp.net/project/plexippus-xpath/atdoc/index.html) - XML 路径语言 (XPath) 版本 1.0 的实现。[BSD_2Clause][17]。
* [s-xml](http://cliki.net/S-XML) - 一个基本的解析器。 [LLGPL][8]。
* [xmls](https://github.com/rpgoldman/xmls) - 一个小型、简单、非验证的 XML 解析器。 [3 条款 BSD][15]。
* [cl-feedparser](https://github.com/TBRSS/cl-feedparser) - Common Lisp（RSS、Atom）提要解析器。 [LLGPL][8]
* [Buildnode](https://github.com/AccelerationNet/buildnode) - 一个通用的 Lisp 库，用于简化与 CXML-dom 的交互，例如构建 Excel 电子表格。 [BSD][15]。

<!-- * [cl-xmlspan](https://github.com/rogpeppe/cl-xmlspam/) - concise, regexp-like pattern matching on streaming XML. BSD_3-clause. -->
<!--   * "What do you do when you have a XML file that's larger than you want to fit in memory, and you want to extract some information from it? Writing code to deal with SAX events, or even using Klacks quickly becomes tedious. Cl-xmlspam is designed to make it easy to write code that mirrors the structure of the XML that it's parsing." -->

读取Excel文件：

* [cl-excel](https://github.com/gwangjinkim/cl-excel) - 一个现代且强大的 Common Lisp 库，用于读写 Microsoft Excel .xlsx 和 LibreOffice .ods 文件。麻省理工学院。
*“允许开发人员用最少的代码处理复杂的电子表格，同时保持大型数据集的内存效率。”
* 完整的写作支持。
* 强大的格式检测。

YAML
----

* 👍 [cl-yaml](https://github.com/eudoxia0/cl-yaml.git) - 构建在 libyaml 之上的 YAML 解析器和发射器。 [麻省理工学院][200]。
* 一个活跃的分叉：[cl-RemiYaml](https://nanako.mooo.com/fossil/cl-remiyaml/index)，并进行了一些修复。不是直接替代品。
* [yamson](https://github.com/bohonghuang/yamson) - Common Lisp 的快速 YAML 和 JSON 解析器（还不是发射器）。阿帕奇2.0。

<!-- * [nyaml](https://github.com/jasom/nyaml) - A lisp native YAML parser. MIT. -->
  <!-- * *in our tests (2026), nyaml was slow (too orders of magnitude slower than cl-yaml* -->

数据结构
===============

字符串：

* 👍 [str](https://github.com/vindarel/cl-str) - 一个现代、简单且一致的字符串操作库。 [麻省理工学院][200]。
* [rope](https://github.com/garlic0x1/rope) - Common Lisp 的不可变绳索。麻省理工学院。
- 另请参阅：梧桐中的绳索。

列表和序列：

* [trivial-extensible-sequences](https://codeberg.org/shinmera/trivial-extensible-sequences) - 可扩展序列协议的可移植库（[SBCL 文档](http://www.sbcl.org/manual/#Extensible-Sequences)）。 [zlib][33]。
* [listopia](https://github.com/Dimercel/listopia) - 受 Haskell 的 Data.List 启发的列表操作库。 [LLGPL][8]。
* [nonempty](https://github.com/fosskers/cl-nonempty) - Common Lisp 的非空集合。  [LGPL3][9]。
* 还有 cl-容器、cl-数据结构、serapeum

（纯粹）函数式数据结构：

* 👍 [FSet](https://common-lisp.net/project/fset) - 一个功能性的集合论集合数据结构库。 [LLGPL][8]。
* 定义了四种主要类型：seqs（序列）、maps（哈希表）、sets 和 bag（类似于集合，但它们记住每个成员被添加到其中的次数）。  现在系统 FSet/Jzon 中包含 JSON 支持。
* [sycamore](https://github.com/ndantam/sycamore) - 一个快速、纯函数式的数据结构库。 [BSD_3 条款][15]。
- 比较：[FSet 与 Sycamore](https://scottlburson2.blogspot.com/2024/10/comparison-fset-vs-sycamore.html)
* [modf](https://github.com/smithzvk/modf) - 用于函数式编程的类似 setf 的宏。
* 还有 cl-容器、cl-数据结构

哈希表：

* Serapeum 的哈希表函数：`dict` 等。
* [cl-hash-util](https://github.com/orthecreedence/cl-hash-util) - 哈希表创建、访问和操作实用程序。 [麻省理工学院][200]。
* [hash-set](https://github.com/samebchase/hash-set/) - 在 CL 哈希表之上实现哈希集的便利库 [The Unlicense][5]
* 还有 cl-容器、cl-数据结构、serapeum

算法：

* [cl-competitive](https://github.com/privet-kitty/cl-competitive) - 用于竞争性编程的 Common Lisp 算法集合。公共领域、CCO 或 MIT。
* [cl-permutation](https://github.com/stylewarning/cl-permutation) - Common Lisp 中的排列和排列群。 [BSD_3 条款][15]。

树木：

* [bst](https://codeberg.org/glv/bst) - 二叉搜索树。 [GPL3][2]。
* 还有 cl-容器、cl-数据结构、serapeum

堆：

* [pileup](http://nikodemus.github.io/pileup/) - Common Lisp 的可移植、高性能和线程安全的二进制堆。 [麻省理工学院][200]。

队列：

* [cl-freelock](https://github.com/ItsMeForLua/cl-freelock) - 针对不同用例和硬件优化的线程安全、无锁队列。该库提供三种队列类型，每种类型都针对特定的并发模式和性能要求而设计。
* 在具有多核的系统上，cl-freelock 的性能比竞争库提高了 3.2 倍。


更大的收藏库：

* [cl-data-structures](https://github.com/sirherrbatka/cl-data-structures) - 数据结构（可变和不可变）和流算法（聚合、分组等，主要是字典和序列，具有一些统计功能）的可移植集合。 [BSD][15]。
* 序列、集合、队列、字典
* [cl-containers](https://github.com/hraban/cl-containers) - 一个广泛的数据结构和实用程序库 - 队列、树、堆、双向链表、集合、包……[MIT][200]
* 和“标准接口，使它们更易于使用，并且使更改设计决策变得更加容易”。

其他数据结构：

* [cl-ctrie](https://github.com/danlentz/cl-ctrie) - 
无锁、并发、键/值索引，具有高效的内存映射持久性和快速瞬态存储模型。 [麻省理工学院][200]。
* [bitfield](https://github.com/marcoheisig/bitfield) - 有效地将多个有限集或小整数表示为单个非负整数。 [麻省理工学院][200]。
* [bit-smasher](https://github.com/thephoeron/bit-smasher) - 用于处理位向量、位向量算术和类型转换的 Common Lisp 库。 [麻省理工学院][200]。

数据结构的通用访问：

* 👍 [access](https://github.com/AccelerationNet/access/) - 对最常见数据结构的一致和嵌套访问。 [BSD_3 条款][15]。


另请参阅：

* [Common Lisp 中漂亮的打印树数据结构](https://gist.github.com/WetHat/9682b8f70f0241c37cd5d732784d1577)（作为 Jupyter 笔记本）


Docker 镜像
=============

* [cl-docker-images](https://common-lisp.net/project/cl-docker-images/) - Windows (amd64) 以及 Alpine 和 Debian (amd64、arm64、arm/v7) 上的 ABCL、CCL、ECL 和 SBCL 的 Docker 映像 [BSD_2Clause][17]。
* [base-lisp-image](https://github.com/40ants/base-lisp-image) - 基地
使用 SBCL 或 CCL 以及最新版本的 Common Lisp 项目的 Docker 镜像
ASDF、Qlot 和罗斯威尔。
* [40ants/setup-lisp](https://github.com/40ants/setup-lisp) - 设置 Common Lisp 工具的 GitHub Action。
* 更新 ASDF、安装 Qlot、安装 Roswell
* 对于多种实现
* 适用于 Ubuntu、OSX 和 Windows。
* 使用示例：[Trial 的 CI](https://github.com/Shirakumo/Trial/blob/master/.github/workflows/examples.yml)
* [fukamachi/dockerfiles](https://github.com/fukamachi/dockerfiles) - 用于 Common Lisp 编程的 Dockerfile。罗斯威尔，SBCL，CCL。
* [archlinux-cl](https://github.com/yitzchak/archlinux-cl) - 带有 Common Lisp 实现的 Docker Arch Linux 镜像（至今 7 日）。麻省理工学院。
* [docker-lisp-gamedev](https://gitlab.com/lockie/docker-lisp-gamedev) - 包含 Common Lisp 游戏开发和部署所需工具的 Docker 映像。有 Linux 和 Windows 版本。通过 CI 进行了彻底测试。


外部函数接口、语言互操作
=============================================

## C##

* ⭐ [CFFI](https://github.com/cffi/cffi) - 可移植、易于使用的 C 外部函数接口。 [外籍人士][14]。
  * [cffi-ops](https://github.com/bohonghuang/cffi-ops) - 有助于编写简洁的 CFFI 相关代码。
  * [cffi-objects](https://github.com/bohonghuang/cffi-object) - 实现与外部对象的快速便捷的互操作。
* 👍[cl-autowrap](https://github.com/rpav/cl-autowrap) - 自动将头文件解析为 CFFI 定义。 [FreeBSD][39]。
* [cl-bindgen](https://github.com/sdilts/cl-bindgen) - 用于从 C 头文件创建 Common Lisp 语言绑定的命令行工具和库。 [麻省理工学院][200]。
* [cl-gobject-introspection](https://github.com/andy128k/cl-gobject-introspection) - [Gobject 自省](https://gi.readthedocs.io/en/latest/) FFI。自动绑定以调用 C 库。 [BSD][15]。使用 [gir2cl](https://github.com/kat-co/gir2cl) 生成 Lisp 接口。 [LGPL3][9]。
* [cl-cxx-jit](https://github.com/Islam0mar/CL-CXX-JIT) - Common Lisp 和 C++ 与 JIT 的互操作。 [麻省理工学院][200]。

## 克洛尤尔

* [ABCLJ](https://github.com/lsevero/abclj) - Clojure 到 Common lisp 的互操作非常简单。 EPL-2.0。

开发中：

* [Cloture](https://github.com/ruricolist/cloture) - Common Lisp 中的 Clojure。

> Cloture 处于非常早期（pre-alpha）阶段，但它已经进展到足以加载 clojure.test，从而允许测试套件实际上用 Clojure 编写。

另请参阅这些库：

* 新！ 2025 年 [clj-coll](https://github.com/dtenny/clj-coll) - Common Lisp 中的 Clojure 集合和序列 API，具有可选的 Clojure 集合语法。 [日食][209]。
* 提供不可变的 Cons、Queue、PersistentList、功能以及基于 FSet 构建的 Vector、Set 和 Map 类似物（但完全通过 Clojure API 访问）。
* 可选的读取语法，因此您可以输入“{:a 1 :b 2}”、“#{1 2 3}”和“[1 2 3]”。
* [clj-con](https://github.com/dtenny/clj-con) - Common Lisp 中的 Clojure 风格的并发操作。 [麻省理工学院][200]。
* [clj-re](https://github.com/dtenny/clj-re/) - Clojure 风格的正则表达式函数。
* [clj-arrows](https://github.com/dtenny/clj-arrows) - Common Lisp 的 Clojure 兼容线程/转换/箭头宏。
* [with-redefs](https://github.com/dtenny/with-redefs) - 受 Clojure 的 with-redefs 启发，可以重新绑定全局函数。
* [cl-oju](https://github.com/eigenhombre/cl-oju/) - 我在编写 Common Lisp 时错过了一些习惯用法，主要与序列有关。 [麻省理工学院][200]。

## 埃尔兰##

* [CLERIC](https://github.com/flambard/CLERIC) - Common Lisp Erlang 接口。 Erlang 分发协议的实现，与 erl_interface 和 jinterface 相当。 [麻省理工学院][200]。

## 爪哇##

（另请参阅 LispWorks 和 ABCL）

* [open-ldk](https://github.com/atgreen/openldk) - Common Lisp 中的 Java JIT 编译器和运行时。 [GPL3.0][89]。 （工作进行中）
*“通过逐步将 Java 字节码转换为 Lisp，然后编译为本机机器代码来执行，弥合了 Java 和 Common Lisp 之间的差距。这种独特的方法允许 Java 类无缝映射到 Common Lisp 对象系统 (CLOS) 类，从而实现 Java 和 Common Lisp 代码库之间的轻松集成。”
*“提供了一种实用的解决方案，可以将 Java 库集成到基于 Lisp 的工作流程中，而无需进程外 Java 运行时环境。”

另请参阅：

* [FOIL](https://github.com/jasom/foil/blob/master/docs/foil.md) - Rich Hickey 的 Lisp 外部对象接口可访问 JVM 和 CLI/CLR。


## Objective-C ##

* [cl-nextstep](https://github.com/byulparan/cl-nextstep) - macOS 上 Common Lisp 的 Cocoa 绑定。
* [objc-lisp-bridge](https://github.com/fiddlerwoaroof/objc-lisp-bridge) - 用于与 Objective-C 和 Cocoa 交互的便携式阅读器和桥梁。 [麻省理工学院][200]。
* [cocoas](https://codeberg.org/shinmera/cocoas) - 一个帮助处理 CoreFoundation、Cocoa 和 objc 的工具包库。兹库。

## 蟒蛇##

* [burgled-batteries](https://github.com/pinterface/burgled-batteries) - Python 和 Common Lisp 之间的桥梁。目标是 Lisp 程序可以使用 Python 库。在 Quicklisp 上不可用。 [麻省理工学院][200]。
* [cl4py](https://github.com/marcoheisig/cl4py) - 库 cl4py（发音为 clappy）允许 Python 程序调用 Common Lisp 库。 [麻省理工学院][200]。
* [py4cl](https://github.com/bendudson/py4cl) - 允许 Common Lisp 代码访问 Python 库的库。它基本上是 cl4py 的逆过程。 [麻省理工学院][200]。
* 它的分支 [py4cl2](https://github.com/digikar99/py4cl2)，起初不太稳定，现在更发达、更快。
  * [py4cl2-cffi](https://github.com/digikar99/py4cl2-cffi) - 基于 CFFI 的 py4cl2 替代方案。
*“如果有能力，CFFI 方法可以比 py4cl2 快 50 倍。”

另请参阅[async-process](https://github.com/cxxxr/async-process/)。

* [cl-python](https://github.com/metawilm/cl-python) - Python 在 Common Lisp 中的实现。 [LLGPL][8]，未在积极开发中。


## .Net核心

* [Bike](https://github.com/Lovesan/bike) - 跨平台.Net Core 接口。 [麻省理工学院][200]。

## Emacs Lisp

* [CEDAR](https://gitlab.com/sasanidas/cedar) - 一个先进的交互式开发环境，旨在与 Emacs 兼容，并与其附带的所有功能兼容。停滞了。
* [CLOCC's elisp.lisp](https://sourceforge.net/p/clocc/hg/ci/default/tree/src/cllib/elisp.lisp) - Common Lisp 中的 Emacs Lisp。
* 将 Emacs Lisp 语言实现为 Common Lisp 包。 [1999]
* 不尝试重新实现 Emacs 中提供的函数库来操作缓冲区和其他相关对象，因此它专注于“纯”Emacs Lisp 语言；但它能够运行 Emacs 日历的非 UI 部分。 （S.莫尼尔，M.斯珀伯）


游戏开发
================

* [Trial](https://codeberg.org/shirakumo/trial) - Trial 是一个 OpenGL 游戏引擎，非常注重模块化。它应该提供一个包含有用的零碎内容的大型工具包，您可以从中创建游戏。自定义：[zlib][33] 添加了政治条款。
* [Kandria](https://kandria.com/) 游戏是通过试用版构建的。
* [claw-raylib](https://github.com/bohonghuang/claw-raylib) - 使用claw和cffi-object完全自动生成Common Lisp绑定到Raylib和Raygui。阿帕奇2.0。
* [raylib](https://github.com/fosskers/raylib/) (2025) - 手写的 Raylib 绑定​​，以提高性能并减少依赖足迹。 [MPL-2.0][211]。
* [trivial-gamekit](https://github.com/borodust/trivial-gamekit) - 有了这个小框架，您将能够制作简单的 2D 游戏：绘制基本的几何形状、图像和文本、播放声音以及聆听鼠标和键盘输入。 [麻省理工学院][200]。
* [Xelf](https://gitlab.com/dto/xelf/) - 可扩展的游戏库。在 Quicklisp 上不可用。 [GNU LGPL2.1][11]。
* [eon](https://github.com/bohonghuang/eon) - 一个易于使用但灵活的游戏框架，基于 Raylib for Common Lisp。阿帕奇2.0。

公用事业：

* [cl-gamepad](https://shirakumo.github.io/cl-gamepad) - 访问 Windows、Mac OS 和 Linux 上的游戏手柄和操纵杆。 [zlib][33]。
* [cl-mpg123](https://shirakumo.github.io/cl-mpg123) 和 [cl-out123](https://shirakumo.github.io/cl-out123)，分别是 libmpg123 和 libout123 的绑定库，为您提供快速且易于使用的 mp3 解码和跨平台音频输出。 [zlib][33]。

国际象棋：

* [Queen.lisp](https://github.com/mishoo/queen.lisp) - Common Lisp 的国际象棋实用程序。麻省理工学院。
* 板生成（0x88 方法）、移动生成、FEN/SAN/PGN 解析器和生成器、基本评估引擎。

图形
========

这些是用于处理图形的库，而不是制作 GUI（即小部件工具包），它们有自己的部分。

* ⭐ [Sketch](https://github.com/vydd/sketch) - 用于创建电子艺术、图形等的 CL 框架。 [麻省理工学院][200]。
* [Vecto](http://www.xach.com/lisp/vecto/) - 简单的矢量绘图库。 [FreeBSD][39]。
* [cl-svg](https://github.com/wmannis/cl-svg) - 用于生成 SVG 文件的基本库。 [外籍人士][14]。
* [trivial-svg](https://github.com/calsys456/trivial-svg) - 使用 Vecto 和 zpb-ttf 将 SVG 图像渲染为 PNG。 0BSD。
* [dufy](https://github.com/privet-kitty/dufy) - 各种颜色模型中精确的颜色操作和转换。 [麻省理工学院][200]。
* [opticl](https://github.com/slyrus/opticl) - 用于表示和处理图像的库。 [BSD_2 条款][17]。
* [Varjo](https://github.com/cbaggers/varjo) - Lisp 到 GLSL 转换器。 [BSD_2 条款][17]。
* [zpng](http://www.xach.com/lisp/zpng/) - 用于创建 PNG 文件的库。 [FreeBSD][39]。
* [pngload-fast](https://github.com/lisp-mirror/pngload) - 便携式 Common Lisp 中的 PNG（便携式网络图形）图像格式解码器，重点是速度。 [麻省理工学院][200]。
* [imago](https://github.com/tokenrove/imago) - Common Lisp 的图像处理库。
* 支持 png、pcx、便携式位图 (.pnm)、Truevision TGA (.tga) 和 jpeg 格式的图像
* 允许：调整大小、旋转、浮雕效果、反转颜色、调整对比度、操作颜色元素、构图、绘制简单的图元……
* 与 common-lisp-jupyter 集成。

这些是绑定：

* [glfw](https://github.com/shirakumo/glfw) - 最新的 Common Lisp 绑定库到最新的 GLFW OpenGL 上下文管理库。
* [cl-cairo2](https://github.com/rpav/cl-cairo2) - 开罗绑定。 [提升1.0][54]
* [cl-gd](http://weitz.de/cl-gd/) - 提供 GD 图形库接口的库。 [FreeBSD][39]。
* [cl-horde3d](https://github.com/anwyn/cl-horde3d/) - FFI 绑定到 Horde3D 图形库。在 Quicklisp 上不可用。 [EPL 1.0][59]
* [cl-jpeg](https://github.com/sharplispers/cl-jpeg) - 基线 JPEG 编码器和解码器库。 [3 条款 BSD][15]。
* [cl-liballegro](https://github.com/resttime/cl-liballegro) - Allegro 5 游戏编程库的接口和绑定。 [zlib][33]。
* [cl-opengl](https://github.com/3b/cl-opengl) - CFFI 绑定到 OpenGL、GLU 和 GLUT API。 [3 条款 BSD][15]。
* [cl-sdl2](https://github.com/lispgames/cl-sdl2) - 使用 C2FFI 绑定 SDL2。 [外籍人士][14]。
* [CLinch](https://github.com/BradWBeer/CLinch) - 用于 OpenGL 的 Common Lisp 2D/3D 图形引擎。 [FreeBSD][39]。
* [donuts](https://github.com/tkych/donuts) - Common Lisp 的 Graphviz 接口。 [外籍人士][14]。
* [lispbuilder-sdl](https://github.com/lispbuilder/lispbuilder) - SDL 的一组绑定。 [外籍人士][14]。
* [lisp-magick-wand](https://github.com/ruricolist/lisp-magick-wand) - ImageMagick 绑定。 [BSD][15]。不在 Quicklisp 中。
* [okra](https://www.common-lisp.net/project/okra/manual.html) - CFFI 与 Ogre 的绑定。在 Quicklisp 上不可用。 [3 条款 BSD][15]。
* [cl-cuda](https://github.com/takagi/cl-cuda) - 在 Common Lisp 程序中使用 NVIDIA CUDA 的库。 [LLGPL][8]。

图形用户界面
===

有关 GUI 工具包的概述和教程，请参阅 [the Cookbook/GUI](https://lispcookbook.github.io/cl-cookbook/gui.html)。

* [LispWork's CAPI](http://www.lispworks.com/products/capi.html) - 具有移动运行时的便携式 GUI 工具包。专有，但附带免费版本。
* [Allegro's Common Graphics](https://franz.com/products/allegro-common-lisp/acl_gui_tools.lhtml) - 用于为 Windows、Mac 和 Linux 编写窗口化 GUI 的函数库。专有且有免费版本。
- 自 Allegro 10.1（2022 年 3 月）起，IDE 和通用图形工具包[在浏览器中运行](https://franz.com/ftp/pri/acl/cgjs/doc.html)。
* 🆕 [cl-gtk4](https://github.com/bohonghuang/cl-gtk4) - Common Lisp 的 GTK4/Libadwaita/WebKit 绑定。 [LGPL3][9]。
* [cl-cffi-gtk](https://github.com/crategus/cl-cffi-gtk) - GTK+3 的绑定。 [GNU LGPL2.1][11]。
- 教程：[通过示例学习 Common Lisp：带有 SBCL 的 GTK GUI](https://dev.to/goober99/learn-common-lisp-by-example-gtk-gui-with-sbcl-5e5c)
* [Qtools](https://codeberg.org/shinmera/qtools/) - 一个基于 CommonQt 的 Qt 工具包。 [zlib][33]还有[Qtools-ui](https://codeberg.org/shinmera/qtools-ui)（预制UI组件），以及[视频](https://www.youtube.com/watch?v=KwASFOhYta4&index=7&list=PLkDl6Irujx9Mh3BWdBmt4JtIrwYgihTWp)。
* [CommonQt](https://github.com/commonqt/commonqt) - 通过 QtSmoke 绑定 Qt4 的 Common Lisp。 [FreeBSD][39]。
  * [CommonQt5](https://github.com/commonqt/commonqt5/) - Qt5 的绑定。
*警告：目前很难安装。由 SISCOG 用于生产©。
* ⭐ [ltk](http://www.peter-herth.de/ltk/) - Tk 工具包的绑定。 [LLGPL][8] 或 [GNU LGPL2.1][11]。
  * [LTk Examples](https://peterlane.codeberg.page/ltk-examples/) - 为 tkdocs 教程提供 LTk 示例。
  * [LTk Plotchart](https://peterlane.codeberg.page/ltk-plotchart/) - 围绕 tklib/plotchart 库的包装器，可与 LTk 一起使用。其中包括 20 多种不同的图表类型（xy 绘图、甘特图、3d 条形图等）。
* [nodgui](https://codeberg.org/cage/nodgui) - Tk 工具包的绑定，基于 Ltk，带有语法糖和附加小部件。 [LLGPL][8]。
* 🎨 支持 [tk 自定义主题](https://wiki.tcl-lang.org/page/List+of+ttk+Themes)，例如 [ttkthemes](https://ttkthemes.readthedocs.io/en/latest/themes.html) 和 [Forest-ttk-theme](https://github.com/rdbende/Forest-ttk-theme)。
* 当需要快速渲染时，支持 SDL 框架作为 Tk 画布的替代方案。用于 2D（基于像素）和 3D 渲染（使用 openGL）。
* [IUP](https://github.com/lispnik/iup/) - CFFI 绑定到 [IUP](https://www.tecgraf.puc-rio.br/iup/) 便携式用户界面库（ALPHA 之前）。
- IUP 是跨平台的（Windows、macOS、GNU/Linux，带有新的 Android、iO、Cocoa 和 Web Assembly 驱动程序），有许多小部件，有一个小型 api，并且正在积极开发。
- 有网络视图。
* 🆕 [Barium](https://tomscii.sig7.se/barium/) - 一个 X 小部件工具包，直接访问 X 客户端库和其他平台库（OpenGL、Cairo）。 [麻省理工学院][200]。
* 带有菜单、窗格、选项卡、对话框、文件选择器、灵活的事件循环……
* 不是另一个工具包的包装。允许增量 GUI 开发。
* 截至 2025 年 4 月的新内容。

但这还不是全部。


* [CocoaInterface](https://github.com/plkrueger/CocoaInterface/) - 
Clozure Common Lisp 的 Cocoa 接口。构建 Cocoa 用户界面
Windows 动态使用 Lisp 代码并绕过典型的 Xcode
流程。它有
[良好的文档和教程](https://github.com/plkrueger/CocoaInterface/blob/master/Documentation/UserInterfaceTutorial.pdf)。
* [McCLIM](https://common-lisp.net/project/mcclim/) - Common Lisp 接口管理器版本 II 的实现。 [GNU LGPL2.1][11]。
* 示例项目：Lem 编辑器 CLIM 界面：[讨论](https://github.com/lem-project/lem/discussions/1311#discussioncomment-10203860)，[屏幕截图](https://framapiaf.org/@frescosecco@mastodon.social/112909105163460836)。
* [Anathema](https://codeberg.org/contrapunctus/anathema)，McCLIM 应用程序的主题库。无执照。
* *阅读时（2026-05-18），提供字体和颜色变化。不改变小部件的渲染。提供 Doom 主题。*
  * [clim-modern](https://git.sr.ht/~hajovonta/clim-modern) - McCLIM 的主题库，用平面、现代外观的等效项取代了现有的 90 年代 Motif 风格的小部件。通过主题和每个小部件样式覆盖完全可定制。麻省理工学院。 *由法学硕士构建*。
* [cl-webkit](https://github.com/joachifm/cl-webkit) - 与 WebKitGTK+ 的绑定。还为应用程序添加了 Web 浏览功能，充分利用 WebKit 浏览引擎的功能。 [麻省理工学院][200]。
* [ftw](https://github.com/fjames86/ftw) - Win32 GUI 库。 [麻省理工学院][200]。
* [eql, eql5, eql5-android](https://gitlab.com/eql) - 嵌入式Qt4和Qt5 Lisp，嵌入ECL，可嵌入Qt。将 EQL5 移植到 Android 平台。 [麻省理工学院][200]。
  * [Android 商店中的 EQL5](https://play.google.com/store/apps/details?id=org.eql5.android.repl&pcampaignid=web_share)
* [bodge-nuklear](https://github.com/borodust/bodge-nuklear) - [Nuklear](https://github.com/Immediate-Mode-UI/Nuklear) 即时模式 GUI 库的包装。 [麻省理工学院][200]。
* [vk](https://github.com/JolifantoBambla/vk) - Vulkan API 的通用 Lisp/CFFI 绑定。 [麻省理工学院][200]。
* 另请参阅 [cl-vulkan](https://github.com/awolven/cl-vulkan) - 支持 Vulkan 1.0 和 1.2，包括计算管道。 Vulkan 1.1 和 1.3 即将推出©。麻省理工学院。
* cl-vulkan 目前支持 Microsoft Windows、Linux 和 MacOS 上的 SBCL 和 Clozure Common Lisp。

其他实用程序：

* [file-select](https://codeberg.org/shinmera/file-select) - 用于调用本机系统文件对话框来选择或创建文件的库。兹利布。

另请参阅此[使用 ABCL 中的 Java Swing 的演示](https://github.com/defunkydrummer/abcl-jazz)。

网页浏览量
-----------

对于电子，请参阅：

* [Electron-lisp-boilerplate](https://github.com/mikelevins/electron-lisp-boilerplate) - 用于构建启动 Lisp 进程的 Electron 应用程序的基本样板。
* [ceramic](https://ceramic.github.io/) - 围绕更简单的工具的包装器，用于为 Common Lisp 创建和构建 Electron 应用程序。它目前已损坏且无人维护，但有些工具可以使用。
* 注意：在 Electron 中嵌入 lisp web 应用程序的主要思想是从 Electron 的 `main.js` 文件中作为异步进程启动 lisp web 服务器，并将 Electron 窗口指向本地主机 URL。就是这样。

阅读：[Common Lisp 的三个 Web 视图](https://lisp-journey.gitlab.io/blog/third-web-views-for-common-lisp--cross-platform-guis/)。

对于其他网络视图，请参阅：

* [cl-webui](https://github.com/garlic0x1/cl-webui/) - [webui](https://webui.me/) 的绑定，允许使用任何 Web 浏览器或 WebView 作为 GUI。
* [clogframe](https://github.com/rabbibotton/clog/tree/main/clogframe) - webview.h 的可执行包装器，允许显示由 Common Lisp 服务器提供服务的任何 Web 应用程序。
* clogframe *不会*诱导使用整个 CLOG 框架。


手机
------

* [LispWork's mobile runtime](http://www.lispworks.com/products/lw4mr.html) - Android 和 iO。  所有权。
* [LQML](https://gitlab.com/eql/lqml) - 与源自 EQL5 的 QML（Qt5 和 Qt6）的轻量级 ECL 绑定。 LGPL 和公共领域。
* [sbcl-termux-build](https://github.com/bohonghuang/sbcl-termux-build/) - 适用于 Android (Termux) 的预构建 SBCL 二进制文件。

另外：

[hello-alien](https://github.com/Gleefre/hello-alien/)，为 Android 应用程序构建的 SBCL。


实施
===============

* ⭐ [SBCL](http://www.sbcl.org/index.html) - Steel Bank Common Lisp。 CMUCL 的一个分叉；编译为高效的机器代码。 [标准符合性][13]。公共领域，某些部分位于 [Expat][14] 和 [3-clause BSD][15] 下。
* 另请参阅：[sbcl-librarian](https://github.com/quil-lang/sbcl-librarian) - SBCL 的动态库交付工具。创建可以从 C 或 Python 调用的共享库。麻省理工学院。 [博客文章](https://mstmetent.blogspot.com/2022/04/using-lisp-libraries-from-other.html)。 [教程](https://lispcookbook.github.io/cl-cookbook/dynamic-libraries.html)。
  * [SBCL-GOODIES](https://github.com/sionescu/sbcl-goodies) - 使用 Common Lisp 和外部库分发二进制文件：静态烘焙 libssl、libcrypto 和 libfixposix。[MIT][200]。
  * [Nightly Windows builds of SBCL](https://github.com/olnw/sbcl-builds) - 使用 MSYS2 UCRT64 每晚构建 SBCL。另请参阅 [Roswell 的 SBCL MSI 版本](https://github.com/roswell/sbcl_bin/releases/)。
* [SBCL on Chocolatey for Windows](https://community.chocolatey.org/packages/sbcl)（非官方）
* [WIP，2021] [使用 SBCL 的静态可执行文件](https://www.timmons.dev/posts/static-executables-with-sbcl-v2.html)。
* [SBCL Windows 构建支持 Windows 7+](https://github.com/lockie/sbcl-w7)，打包到 NSIS 安装程序中并每月更新（非官方）
* *提示：要增强 SBCL 的默认终端体验，另请参阅下面编辑器部分中的“icl”或“cl-repl”。*
* ⭐ [CCL](https://ccl.clozure.com/) - Clozure Common Lisp；仅编译器实现，生成本机代码。  [LLGPL][8]。
* [ECL](https://common-lisp.net/project/ecl/) - 可嵌入的 Common Lisp；编译为 C。[GNU LGPL2.1][11]。
  * [交叉编译](https://ecl.common-lisp.dev/static/files/manual/current-manual/System-building.html#Cross-compilation)
* [博客报告：将 Maxima 移植到 iOS](https://li-yiyang.github.io/lisp/imaxima/)。
* 开发中的 WASM 支持（[2025 年 NLNET 拨款](https://nlnet.nl/project/ECL/)）
* [eclweb](https://github.com/chee/eclweb) 是[浏览器内的概念验证 REPL](https://repl.chee.party/)，使用 Web Assembly (WASM)。
* [ABCL](https://common-lisp.net/project/armedbear/) - 武装熊 Common Lisp；以 JVM 为目标，编译为字节码。 [标准一致性][4]。 [GNU GPL3][2] 和 [类路径例外][3]。
  * [abcl-memory-compiler](https://gitlab.com/cl-projects/abcl-memory-compiler) - 一种编译 Java 源代码以在运行时使用 ABCL 创建 Java 类的方法。 [阿帕奇2][89]。
  * [py4abcl](https://gitlab.com/cl-projects/py4abcl) - 使用 ABCL 与 Python 进行通信。
* [CLASP](https://github.com/drmeister/clasp) - 一种新的 Common Lisp 实现，可与使用 LLVM 编译为本机代码的 C++ 库和程序无缝互操作。这使得 Clasp 能够利用大量现有的库和程序，例如科学计算生态系统之外的库和程序。 [LGPL2.1][11]（及其他）。

专有：

* [LispWorks](http://www.lispworks.com/) - Common Lisp 的集成跨平台开发工具。
* 著名的功能包括：CAPI 跨平台和本机 GUI 工具包、LispWorks IDE、移动平台运行时（iO、Android）、Java 接口、用于构建更轻量级二进制文件的摇树机、用于“基于规则、面向对象、逻辑、函数和数据库编程”的 KnowledgeWorks 系统等等。
* 有免费版本，有限制（堆大小限制、时间限制）。
* [Allegro CL](https://franz.com/products/allegro-common-lisp/) - 提供完整的 ANSI Common Lisp 标准和许多扩展。
* 著名的功能包括：AllegroCache 对象持久数据库系统、KnowledgeGraph 系统、并发垃圾收集器、基于 Web 的 IDE 等等。
* 有免费版本。它包括 AllegroCache，但有大小限制。
* 可能很贵。获得许可的开发人员可以访问大部分源代码。 Franz Inc. 还发布[开源库](https://github.com/franzinc)（通常与 AllegroCL 绑定）。

其他实现，主要用于历史目的：

* [CMUCL](http://www.cons.org/cmucl/) - 卡内基梅隆大学的实施。公共领域。 SBCL 是 CMUCL 的一个分支。
* [GNU CLISP](http://www.clisp.org/) - GNU 实现；包含一个编译器和一个解释器。 [标准一致性][6]。 [GNU GPL3][2]。他们在 Gitlab 上开发（https://gitlab.com/gnu-clisp/clisp）。
* 编译为字节码，其默认 REPL 比 SBCL 更用户友好（具有符号完成和 readline 集成）。
* 然而，它的开发并不积极，它不完全符合 ANSI 标准，它的性能低于 SBCL，并且缺乏兼容性功能。
* [Corman Lisp](https://github.com/sharplispers/cormanlisp) - 用于在 Intel 平台上运行的 Microsoft Windows 的 Common Lisp 开发环境。 [麻省理工学院][200]。

您可以在此处检查实现与常见扩展的兼容性：[portability.cl](https://portability.cl)。

另请参阅：

* [cl-all](https://codeberg.org/shinmera/cl-all) - 在多个实现中运行 Lisp 片段的脚本。这使您可以快速比较实现行为和差异。 [zlib][33]。

# 语言库

## Lisp 解析器

* [Eclector](https://github.com/s-expressionists/Eclector/) - 一个高度可定制的便携式 Common Lisp 阅读器，可以从错误中恢复，并可以返回具体的语法树。
* 用于工具和库，但仍在积极开发中*
* [rewrite-cl](https://github.com/atgreen/rewrite-cl) - 阅读、修改和编写 Common Lisp 源代码，同时保留空格和注释。麻省理工学院。 *由法学硕士构建*。
* [cl-sourcery](https://sr.ht/~hajovonta/cl-sourcery/) - 拦截所有标准 CL 定义形式（defun、defmacro、defclass、defstruct 等）以捕获并存储书面的确切源代码 — 包括空格、注释和格式。麻省理工学院。 *由法学硕士构建*。

另请参阅：

* [breeze](https://github.com/fstamour/breeze/) - Common Lisp 工作流程实验。在制品。

## 树保姆语法

* [tree-sitter-commonlisp](https://github.com/tree-sitter-grammars/tree-sitter-commonlisp) - 树看护者的 Common Lisp 语法。麻省理工学院。
* 仍在进行中。
* [tree-sitter-cl-syntax](https://codeberg.org/zshaftel/tree-sitter-cl-syntax) - 另一种 WIP 语法，专门关注该语言的语法。
* 具有“format”指令的语法。

语言扩展
===================

* ⭐ [alexandria](https://common-lisp.net/project/alexandria/) - 通用实用程序库。公共领域。
* 👍 [serapeum](https://github.com/ruricolist/serapeum/) - 另一个通用实用程序库。 [外籍人士][14]。
* [rutils](https://github.com/vseloved/rutils) - Common Lisp 的激进但合理的语法实用程序。 [麻省理工学院][200]。
* [generic-cl](https://github.com/alex-gutev/generic-cl/) - 标准 Common Lisp 函数的通用函数接口（相等、比较、算术、对象、迭代器、序列……）。 [麻省理工学院][200]。
* 另请参阅更轻量级的 [equals](https://github.com/karlosz/equals/) [MIT][200]。
* [anaphora](https://common-lisp.net/project/anaphora/) - 照应宏的集合。公共领域。
* [arrow-macros](https://github.com/hipeta/arrow-macros) - 类似 Clojure 的线程宏。 [麻省理工学院][200]。
* [hu.dwim.walker](https://github.com/hu-dwim/hu.dwim.walker) - 代码解析器和解解析器（又名 AST 解析器和解解析器）。 [BSD][15]。另请参阅[此博文](http://40ants.com/lisp-project-of-the-day/2020/04/0044-hu.dwim.walker.html)。

模式匹配
--------------------

* ⭐ [trivia](https://github.com/guicho271828/trivia/) - 优化的模式匹配库。 [LLGPL][8]。


可移植层
------------------

这里收集了大量可移植层：[portability.cl/](https://portability.cl/)。以下是其中一些：

* [trivial-arguments](https://codeberg.org/shinmera/trivial-arguments) - 用于检索函数的参数列表和参数类型的可移植库。 [zlib][33]。
* [definitions](https://codeberg.org/shinmera/definitions) - 通用定义内省库。它使您能够检索与指示符（例如符号、包和名称）关联的定义或绑定。 [zlib][33]。
* [DRef](https://github.com/melisgl/dref) - 另一个定义内省库，具有大量文档、测试并强调可扩展性。 [麻省理工学院][200]。
* [dissect](https://shinmera.github.io/dissect) - 当许多项目使用“trivial-backtrace”系统时，该系统只为它们提供一个带有回溯的字符串，而 Dissect 允许您捕获、单步执行和完全检查各种 Lisp 实现上的堆栈跟踪。对于日志记录和其他自动继续执行的情况也非常有用，但当前堆栈的信息对于存储在某处仍然有用。 [zlib][33]。

更改语法
-------------------

* [cl-annot](https://github.com/m2ym/cl-annot) - Common Lisp 的类似于 Python 的注释。 [LLGPL][8]。
  * [cl-annot-revisit](https://github.com/y2q-actionman/cl-annot-revisit/) - 重新实施 cl-annot。 WTFPL。
* [cl-reader](https://github.com/digikar99/reader) - 一个实用程序库，旨在为 lambda、映射、访问器、哈希表和哈希集提供读取器宏。 [麻省理工学院][200]。
* [clamp](https://github.com/malisper/Clamp) - Arc 语言比 Common Lisp 简洁。 [艺术许可2.0][51]。
* 还有 [arc-compat](https://github.com/g000001/arc-compat) - Arc 兼容包。 Perl 基金会的艺术许可证 2.0。

对于字符串：

* ⭐ [cl-interpol](https://github.com/edicl/cl-interpol/) - 一组允许字符串插值的阅读器修改。 [BSD][15]。
* 另请参阅：[f-string](https://git.sr.ht/~dieggsy/f-string) 仅用于字符串插值，没有依赖项。麻省理工学院。
* [mstrings](https://git.sr.ht/~shunter/mstrings) - 一个阅读器宏，提供视觉上吸引人的多行块。 M 字符串会修剪前导空格、将行连接在一起等。[BSD_3Clause][15]。
* [pythonic-string-reader](https://github.com/smithzvk/pythonic-string-reader) - 受 Python 三引号字符串启发的简单且不显眼的读表修改。 [BSD_3 条款][15]。
* [cl-heredoc](https://github.com/outergod/cl-heredoc) - 一个 [“heredocs”](https://github.com/outergod/cl-heredoc) 调度程序。 [GPL3][2]。允许写入：`#>eof>写任何（你）“想要”的内容，无论什么字符，直到达到神奇的结束序列。eof`

实验：

* [Moonli](https://gitlab.com/digikar/moonli) - 一个 Julia/Python 风格的语法层，可转换为 Common Lisp。
* *实验性*。自 2025 年起新。

CLOS 扩展
---------------

* ⭐ [closer-mop](https://github.com/pcostanza/closer-mop) - 一个兼容层，可以纠正许多缺失或不正确的 MOP 功能。 [外籍人士][14]。
* [specialization-store](https://github.com/markcox80/specialization-store/) - 基于类型的泛型函数。简化的 BSD 许可证变体。
* [filtered-functions](https://github.com/pcostanza/filtered-functions) - 允许使用任意谓词来选择和应用方法。 [麻省理工学院][200]。
* [inlined-generic-function](https://github.com/guicho271828/inlined-generic-function) - 
将静态调度的速度提升至 CLOS。 [LLGPL][8]。
* [static-dispatch](https://github.com/alex-gutev/static-dispatch) - 允许静态（在编译时）而不是动态（运行时）执行标准通用函数调度。这类似于 C++ 和 Java 等语言中所谓的“重载”。 [麻省理工学院][200]。
* [dynamic-mixins](https://github.com/rpav/dynamic-mixins) - 简单、动态的类组合。 [BSD_2 条款][17]。
* [fast-generic-functions](https://github.com/marcoheisig/fast-generic-functions) - 密封您的通用函数以进一步提高性能。 [麻省理工学院][200]。
* [polymorphic functions](https://github.com/digikar99/polymorphic-functions) - 用于分派类型而不是类的函数类型，部分支持分派可选和关键字参数类型。仍处于实验阶段（2021 年 5 月）。 [麻省理工学院][200]。
- 多态函数根据提供给它的参数类型进行分派。这有助于在专用数组和用户定义类型上进行分派。
- 有关专业化存储和快速通用函数的差异，请参阅其自述文件。

编写简洁的 defclass 形式：

* [defclass-std](https://github.com/lisp-maintainers/defclass-std) - 用于快速编写 DEFCLASS 和 PRINT-OBJECT 表单的快捷宏。 [LLGPL][8]。
* [nclasses](https://github.com/atlas-engineer/nclasses) - 类和泛型函数声明的语法糖。具有类型推断、自动访问器、内联 initform 语法、自动导出和其他便利功能。 [BSD][15]。

还有：

* [slot-extra-options](https://github.com/some-mthfka/slot-extra-options) - 允许您构建一个元类，该元类又允许您在其类中指定额外的插槽选项。 [LGPL3][9]。

功能扩展
-------------------

* [cl-hooks](https://github.com/scymtym/architecture.hooks/) - Hooks 扩展点机制（如已知的，例如来自 GNU Emacs）。 LGPL。
* [method-hooks](https://gitlab.com/Gnuxie/method-hooks) - 当 CLOS 方法组合只允许每个方法有一个钩子时，该库允许任意数量的钩子。 Mozilla 公共许可证。
* [cl-advice](https://github.com/lisp-mirror/budden-tools/blob/213ab2b52a1b0c0b496efd30c3b5143f5c8e1ff2/cl-advice/README.md) - SBCL、CCL、LispWorks 和 Allegro 的可移植层建议库的尝试。不在 Quicklisp 中。
* [nhooks](https://github.com/atlas-engineer/nhooks) - 增强了钩子（扩展点）的实现，并进行了重大改进。

迭代
---------

* ⭐ [iterate](https://common-lisp.net/project/iterate/) - Common Lisp 的迭代构造，可扩展且 Lispier。 [麻省理工学院][200]。
* [Khazern](https://github.com/s-expressionists/Khazern) - CL:LOOP 的实现可以在任何 CL 实现中使用，而无需替换核心 CL:LOOP，它是可扩展的，并且具有“包含电池”的扩展系统，具有许多有用的迭代结构。
* [for](https://shinmera.github.io/for/) - 一个简洁、口齿不清且可扩展的迭代宏。它是可扩展且合理的，与迭代不同，它不需要代码遍历并且更容易扩展。 [zlib][33]。
* [series](https://series.sourceforge.net/) - 函数式风格完全没有任何运行时损失。 [麻省理工学院][200]。
* [trivial-do](https://github.com/yitzchak/trivial-do/) - Common Lisp 的附加 dolist 风格宏。 [麻省理工学院][200]。
* [doplus](https://github.com/alessiostalla/doplus) - 另一个可扩展的迭代库，类似于 :for。
* [cl-transducers](https://github.com/fosskers/cl-transducers/) - 符合人体工程学、高效的数据处理。 [LGPL3][9]。
*“传感器是一种符合人体工程学且极其节省内存的数据源处理方式。这里的“数据源”指的是列表或向量等简单集合，但也可能是大文件或无限数据生成器。”
*“总的来说，这是 Transducer 模式最完整的实现。”
* 一个“现代”API，带有`map`、`filter`、`take`、`repeat`、`cycle`、`fold`…
* [snakes](https://github.com/BnMcGn/snakes) - Common Lisp 的 Python 风格生成器。包括 itertools 的端口。 [阿帕奇2][89]。
* [picl](https://github.com/anlsh/picl) - Python 的 itertools 包的（几乎）完整移植，在适用的情况下完成了惰性，并且不依赖于 cl-cont。 [麻省理工学院][200]。
* [gtwiwtg](https://cicadas.surf/cgit/colin/gtwiwtg.git/about/) - 一个惰性序列库。与“系列”类似，但不那么完整。然而，它有一个“现代”API，其中包含“take”、“filter”、“for”、“fold”等易于使用的内容。
* [gmap](https://github.com/slburson/misc-extensions) - 一个简洁且可扩展的迭代工具，具有与 FSet 良好集成的优点（请参阅数据结构部分），因为它是由同一作者编写的。在 Quicklisp 中作为“misc-extensions”的一部分。公共领域。


Lambda 简写
-----------------

* [fn](https://github.com/cbaggers/fn) - 几个 lambda 速记宏。 `(fn* (+ _ _)) --> (lambda (_) (+ _ _))`。公共领域。
* [f-underscore](https://gitlab.common-lisp.net/bpm/f-underscore) - 一个小型的函数式编程实用程序库。 `(f_ (+ _ _)) -> (lambda (_) (+ _ _))`。公共领域。
* [cl-punch](https://github.com/windymelt/cl-punch/) - 类似 Scala 的匿名 lambda 文字。 `(mapcar ^(* 2 _) '(1 2 3 4 5))`。 [麻省理工学院][200]。


另请参阅 [Rutils](https://github.com/vseloved/rutils)。


非确定性逻辑编程
------------------------------------

* [cl-prolog2](https://github.com/guicho271828/cl-prolog2) - Common Lisp 到 ISO Prolog 实现的通用接口。 [麻省理工学院][200]。
* [Screamer](https://github.com/nikodemus/screamer) - 增强通用
Lisp 几乎具有 Prolog 和 Prolog 的所有功能
约束逻辑编程
语言。 [博客文章](https://chriskohlhepp.wordpress.com/reasoning-systems/specification-driven-programming-in-common-lisp/)
解决欧拉计划难题。 [麻省理工学院][200]。
* [Screamer+](https://github.com/yakovzaytsev/screamer-plus) - 增加 SCREAMER 的表现力。 [麻省理工学院][200]。
* [AP5](https://ap5.com/) - 允许用户在一阶逻辑模型或关系数据库中进行编程。 1989 年，2024 年更新。公共领域。
* [Temperance](https://github.com/sjl/temperance) - 逻辑编程。 [麻省理工学院][200]。注重性能，考虑一般游戏玩法。

反应式编程
--------------------

* [Cells](https://github.com/kennytilton/cells) - 数据流编程范式的实现，CLOS 的反应式电子表格表达能力。用于构建[代数学习系统](http://tiltontec.com/)。带有[文档](https://github.com/stefano/cells-doc/)。 Lisp LGPL。
* [lwcells](https://github.com/kchanqvq/lwcells) - 轻质电池。
* LWCELLS 是 Common Lisp 的数据流扩展。它根据指定细胞关系的函数维持细胞的一致状态。 LWCELLS 的设计简单、干净、组合且灵活。
* 新 (2025) · [live-cells](https://github.com/alex-gutev/live-cells-cl/) - Lisp 的反应式编程库。 BSD_3 条款。


合约编程
--------------------

* [quid-pro-quo](https://github.com/sellout/quid-pro-quo) - 一份合同
Eiffel 的 Design by Contract ™ 风格的编程库。公共领域。

打字
------

* 👍 [Coalton](https://github.com/coalton-lang/coalton/) - 一种高效的静态类型函数编程语言，可增强 Common Lisp 的性能。 [麻省理工学院][200]。
* 专注于高性能、内置高级数学，是比 Lisp 更强大、可扩展的数值塔：
* 任意精度浮点数、精确可计算实数算术、超限数、[双数](https://coalton-lang.github.io/reference/#coalton-library/math/dual-package)和[超双数](https://coalton-lang.github.io/reference/#coalton-library/math/hyperdual-package),
  * [flime](https://github.com/fukamachi/flime) - 实时、项目范围的 Coalton 编译，具有用于 LSP 集成的隔离进程。 [麻省理工学院][200]。
  * [tokyo-tojo-json](https://github.com/tojoqk/tokyo.tojo.json) - 在 Coalton 中实现的 JSON 解析器。
  * [coalton-threads](https://github.com/garlic0x1/coalton-threads) - Coalton 的原始线程和并发操作。
  * [coalton-io](https://github.com/Jason94/coalton-io) - 功能性IO接口。包括终端 IO、文件系统 IO、随机变量、可变变量、多线程以及线程之间安全共享状态。
  * [mine editor](https://coalton-lang.github.io/mine/) - 适用于 Windows、macOS 和 Linux 的 Coalton 和 Common Lisp 集成开发环境。
  * [Lem editor mode for Coalton](https://lem-project.github.io/modes/coalton-lang/) - 语法高亮、代码完成、自动文档、交互式编译命令（`coalton-compile-defun`、`C-c C-c`）。
  * [Slime contrib for Coalton](https://github.com/slime/slime/pull/919) - 显示类型签名。附有简短的演示视频。
  * [Coalton.app playground](https://coalton.app/) - Coalton 的基于网络的 REPL。 [博客文章公告](https://abacusnoir.com/2025/08/12/coalton-playground-type-safe-lisp-in-your-browser/)。
  * [smelter](https://smelter.app/) - 一个零设置的 Coalton（和 CL）脚本运行器，带有一些电池（JSON、HTTP、文件系统、进程实用程序）。
* 👍 [trivial-types](https://github.com/m2ym/trivial-types) - 提供缺失但重要的类型定义，例如“proper-list”、“association-list”、“property-list”和“tuple”。 [LLGPL][8]。
* [defstar](https://bitbucket.org/eeeickythump/defstar/src/master/) - 宏的集合，用于轻松包含 lambda 列表中参数的类型声明。 [GNU GPL3][2]
* [algebraic-data-types](https://github.com/stylewarning/cl-algebraic-data-type) - 以与 Haskell 或 Standard ML 类似的精神定义代数数据类型以及对它们进行操作。 [BSD_3 条款][15]。

另请参阅：

* [typo](https://github.com/marcoheisig/Typo/) - Common Lisp 的可移植类型推理库。 [麻省理工学院][200]。
* 实验性的：[PELTADOT](https://gitlab.com/digikar/peltadot/) - PELTADOT 扩展了 Lisp 的类型和调度。

定理证明者
-------------------

* [ACL2](https://www.cs.utexas.edu/users/moore/acl2/) - 一种逻辑和编程语言，您可以在其中对计算机系统进行建模，并提供一个工具来帮助您证明这些模型的属性。
* 自 20 世纪 90 年代起在业界使用。
* 它支持 ANSI 标准 Common Lisp 编程语言的子集。
* “经常使用 ACL2 的公司包括 AMD、Centaur Technology、IBM、Intel、Kestrel Institute、Motorola/Freescale、Oracle 和 Rockwell Collins。” ([来源](https://royalsocietypublishing.org/doi/10.1098/rsta.2015.0399))
* [Proofpad](https://github.com/calebegg/proof-pad/)，ACL2 的在线 IDE。
* [ACL2-kernel](https://github.com/tani/acl2-kernel)，ACL2 的 Jupyter 内核。
  * [2025 年第 19 届 ACL2 定理证明器及其应用国际研讨会论文集 (PDF)](https://cgi.cse.unsw.edu.au/~eptcs/Published/ACL2in2025/Proceedings.pdf)
* NASA 的 [PVS](https://pvs.csl.sri.com/)（原型验证系统）和 [NASAlib](https://github.com/nasa/pvslib)（正式开发库的集合）。
* 其63个顶级库涵盖：实分析、极限、连续性、导数、积分等领域；复杂的集成；有向图；精确的实数算术，包括三角函数；区间算术和数值近似；线性代数； 2-D、3-D、4-D 和 n 维向量……等等。

学习和教程
=====================

## 在线##

初学者
--------

* [Learn X in Y minutes - Where X = Common Lisp](https://learnxinyminutes.com/docs/common-lisp/) - 小型 Common Lisp 教程，涵盖了要点。
* [Lisp Koans][201] - 该项目引导学习者逐步了解许多 Common Lisp 语言功能。
* [Practical Common Lisp][206] - 很好的 Common Lisp 介绍性文本，带有实际示例。
* 使用 [Firefox 插件：Practical-cl beautified](https://github.com/vale981/practical-cl-beautified) 可以更好地阅读。
* 翻译为【简体中文】(https://binghe.github.io/pcl-cn/)
* [Common LISP: A Gentle Introduction to Symbolic Computation](http://www.cs.cmu.edu/afs/cs.cmu.edu/user/dst/www/LispBook/index.html) - 对这门语言的很好的介绍。
* [Successful Lisp](http://successful-lisp.blogspot.com/) - 对于具有一定编程背景的初学者来说是一本好书。
* [Lisp Quickstart](https://cs.gmu.edu/~sean/lisp/LispTutorial.html) - 一个很好的教程，可以帮助您快速入门并编写 Common Lisp 代码。
* [Casting SPELs in LISP](http://www.lisperati.com/casting.html) - 这是一种边看漫画书边学习 LISP 的有趣方式。
* 📹 [Common Lisp 编程：从新手到高效的开发人员](https://www.udemy.com/course/common-lisp-programming/?referralCode=2F3D698BBC4326F94358) - Udemy 平台上的学习视频系列（*付费访问的完整内容*）。由活跃的 lisper 和社区贡献者 (@vindarel) 撰写。 [Github 主页](https://github.com/vindarel/common-lisp-course-in-videos/)。
> 感谢您支持我在 Udemy 上的工作。我可以向学生发送免费链接，请联系我。

中级
------------

* [Common Lisp 食谱](https://lispcookbook.github.io/cl-cookbook/)
* [Lisp Tips](https://github.com/lisp-tips/lisp-tips/issues/) - 包含有用提示和技巧的博客。
* [Lisp project of the day](http://40ants.com/lisp-project-of-the-day/) - 展示许多 Lisp 库的博客。
* 编译时计算的简要介绍 - [第 1 部分](https://medium.com/@MartinCracauer/a-gentle-introduction-to-compile-time-computing-part-1-d4d96099cea0)，[部分2](https://medium.com/@MartinCracauer/a-gentle-introduction-to-compile-time-computing-part-2-cb0a46f6cfe8)，[第 3 部分（在编译时安全处理变量的科学单位）时间）]（https://medium.com/@MartinCracauer/a-gentle-introduction-to-compile-time-computing-part-3-scientific-units-8e41d8a727ca）
* [可编程编程语言中的静态类型检查](https://medium.com/@MartinCracauer/static-type-checking-in-the-programmable-programming-language-lisp-79bb79eb068a)
* [Loving Common Lisp, or the Savvy Programmer's Secret Weapon](https://leanpub.com/lovinglisp) - 通过许多示例快速介绍 Common Lisp。特别关注如何使用大型语言模型 (LLM)。

高级
--------

* [Let Over Lambda][156] - 一本关于高级宏观技术的书。前六章可在​​线获取。
* [On Lisp](http://www.paulgraham.com/onlisp.html) - Paul Graham 关于 Lisp 宏（以及其他有趣的东西）的精彩书籍。
* [Programming Algorithms in Lisp](https://link.springer.com/book/10.1007/978-1-4842-6428-7) - “[编程算法](https://leanpub.com/progalgs)”的更新版本；使用 Lisp 中的数据结构和算法编写高效程序的综合指南。

还有一些有关 SBCL 内部结构的学习资源：

* [SBCL内部结构](https://simonsafar.com/2020/sbcl/)
* [sbcl-wiki](https://github.com/guicho271828/sbcl-wiki/wiki) - 一个开放的 wiki，用于记录 SBCL 的内部结构。


编码平台
----------------

* [Codewars](https://docs.codewars.com/languages/commonlisp/) - 一个代码培训平台，支持 Common Lisp (SBCL)。

网页开发
--------

* [Section on Web Development in The Common Lisp Cookbook](https://lispcookbook.github.io/cl-cookbook/web.html) - 介绍性教程，涵盖 Web 服务器设置、路由、weblocks、模板、错误处理、打包、热重载、数据库连接和部署，以及当前 Lisp Web 开发生态系统中的其他主题。
* 新的 [Lisp 中的 Web 应用程序：知识](https://web-apps-in-lisp.github.io/) - 在 Common Lisp 中构建交互式 Web 应用程序的教程和参考材料。 CC-BY。

参考
---------

* 新！ [CL CommunitySpec](https://cl-community-spec.github.io/pages/index.html) - Common Lisp ANSI 规范草案的演绎版。
* 具有交互式搜索、语法高亮！并且开源。
* 新的！ [novaspec](https://novaspec.org/) - CL ANSI 草案的现代版本。
* 不是开源的？
* [Common Lisp Quick Reference](http://clqr.boundp.org/index.html) - ANSI CL 规范的精炼袖珍版本。可供下载 PDF 版本。
* [CLHS](http://www.lispworks.com/documentation/lw50/CLHS/Front/index.htm) - Common Lisp HyperSpec；超文本形式的 ANSI CL 标准。
* [CLOS MOP specification](https://clos-mop.hexstreamsoft.com/) - 《元对象协议的艺术》第 5 章和第 6 章的现代公共领域在线版本
* [Common Lisp Standard Draft (pdf)](https://franz.com/support/documentation/cl-ansi-standard-draft-w-sidebar.pdf) - Common Lisp 规范的标准草案，格式良好，带有侧边栏的 PDF。
* 还有 [dpans2texi](https://github.com/mmontone/dpans2texi/releases/) - 标准草案转换为 Texinfo 并作为格式良好的 PDF 发布。
* 可以在线阅读：https://mmontone.github.io/dpans2texi/
* [Common Lisp the Language](http://www.cs.cmu.edu/Groups/AI/html/cltl/cltl2.html) - ANSI 规范之前的 Common Lisp 原始标准。
  * [CLtL2，PDF 格式](https://github.com/mmontone/cltl2-doc)
* [Minispec](https://lamberta.github.io/minispec/) - CLHS 的更友好但不太完整的版本。还包含一些常用 CL 库（例如 Alexandria）的文档。
* [Simplified Common Lisp reference](http://jtra.cz/stuff/lisp/sclr/index.html) - CLHS 的简化版本。
* [CDR](https://cdr.common-lisp.dev/) - Common Lisp 文档存储库。 Common Lisp 社区感兴趣的文档存储库。 CDR 文档最重要的属性是它永远不会改变：如果您引用它，您可以确保您的引用将始终引用完全相同的文档。
- Common Lisp 文档存储库托管在 [Zenodo](https://zenodo.org/communities/cdr/)。

## 离线##

CLHS 可通过 [archive](ftp://ftp.lispworks.com/pub/software_tools/reference/HyperSpec-7-0.tar.gz) 以及 [Dash](https://kapeli.com/dash)、[Zeal](https://zealdocs.org/) 和 [Velocity](https://velocity.silverlakesoftware.com/) 中的文档集离线获取。

初学者
--------

* [Land of Lisp](http://landoflisp.com/) - 有趣的、面向游戏的 Common Lisp 介绍。
* [Practical Common Lisp][206] - 很好的 Common Lisp 介绍性文本，带有实际示例。

中级
------------

* [ANSI Common Lisp](http://www.paulgraham.com/acl.html) - 全面、实用地涵盖整个语言，并附有练习。由于[一些注意事项][20]，不建议将其作为起始文本。
* [Common Lisp Recipes](http://weitz.de/cl-recipes/) - **Common Lisp Recipes** 是您在使用 Common Lisp 编写实际应用程序时可能遇到的问题的解决方案和答案的集合。 2015 年出版。

高级
--------

* [Let Over Lambda][156] - 一本关于高级宏观技术的书。所有八章均可在印刷版中找到。
* [Common Lisp 中的面向对象编程：CLOS 程序员指南][21] - 一本关于 CLOS 的古老但非常详尽的书。
* [人工智能编程范式：Common Lisp 案例研究][157] - 一本关于人工智能编程的书，涵盖了一些高级 Lisp。
* 网页版：[https://norvig.github.io/paip-lisp/](https://norvig.github.io/paip-lisp/#/)
  * [PAIP-lisp](https://github.com/norvig/paip-lisp) - 教科书《人工智能编程范式》的 Lisp 代码。
* [Norvig 的 Lisp 风格](https://www.cs.umd.edu/~nau/cmsc421/norvig-lisp-style.pdf)
* 和 [lisp-lang.org 的风格指南](https://lisp-lang.org/style-guide/)

其他书籍
-----------

* [构建问题解决者](https://www.qrg.northwestern.edu/BPS/readme.html) ([PDF](https://www.qrg.northwestern.edu/BPS/BPS-Searchable.pdf))，作者 Ken Forbus 和 Johan de Kleer，由麻省理工学院出版社免费提供 - 标准人工智能文本中的一本独特的书，结合科学与工程、理论和工艺来描述人工智能推理系统的构建，并包括说明人工智能推理系统的代码想法。

社区
---------

* [/r/Common_Lisp](https://www.reddit.com/r/Common_Lisp/) - 关于 Common Lisp 的 Reddit 子版块
* [/r/learnlisp](https://www.reddit.com/r/learnlisp/) - 一个用于提问和获取有关 Lisp 的帮助的 Reddit 子版块
* [common-lisp.net](https://common-lisp.net)
* [Lisp Discord 服务器](https://discord.gg/hhk46CE)
* Libera Chat 上的 [#commonlisp](https://irclog.tymoon.eu/libera/%23commonlisp) - 主要 Common Lisp IRC 频道。
* Libera Chat 上的 [#lisp](https://irclog.tymoon.eu/libera/%23lisp) - 所有 Lisp 方言的 IRC 频道。
* Libera Chat 上的 #clschool - 用于学习 Common Lisp 的 IRC 频道。
* Libera Chat 上的 #lispcafe - 用于题外讨论的 IRC 频道。
* [Planet Lisp](http://planet.lisp.org/) - 一个元博客，收集了各种 Lisp 相关博客的内容。
* [Lisp Jabber/XMPP 通道](https://xmpp.link/#lisp@conference.a3.pm?join)
* [Matrix-for-lispers](https://web.matrix-for-lispers.net/) - 一个讨论不同 Lisp 主题的空间，支持持久性、Markdown、屏幕截图。
* 截至 2026 年 5 月的新内容。
* 注册令牌是 `lisp-spelt-without-caps`。单击“探索”即可查看所有可用房间。

展示柜
--------

* [lisp-lang.org](https://lisp-lang.org/)
* 🔥 [lisp-screenshots.org](https://www.lisp-screenshots.org/)
* [awesome-lisp-companies](https://github.com/azzamsa/awesome-lisp-companies/)
* [cl-software](https://github.com/azzamsa/awesome-cl-software)

图书馆经理
===============

* ⭐ [Quicklisp][16] - 包含许多库的库管理器，具有轻松的依赖关系管理。 [外籍人士][14]。
  * [ql-https](https://github.com/rudolfochrist/ql-https) - 默认情况下，shell 为 cURL 并使用 HTTPS。
  * [Quicklisp bundles](https://quicklisp.org/beta/bundles.html) - 从 Quicklisp 导出并可在不涉及 Quicklisp 的情况下加载的独立系统集。
* [ocicl](https://github.com/ocicl/ocicl) - 具有新颖功能的现代依赖管理工具。 [麻省理工学院][200]。
* 项目本地依赖项、代码检查、项目脚手架、LLM 生成的包版本之间更改的摘要
* 通过 TLS 安全地分发软件包，所有软件都打包为符合 OCI 的工件等等。
* [Ultralisp](http://ultralisp.org/) - 一种 Quicklisp 发行版，每 5 分钟更新一次，并且可以一键添加他的项目。 [BSD][15]。
* [Roswell](https://github.com/roswell/roswell) - Lisp 实现安装程序、脚本启动程序等。 [麻省理工学院][200]。
* [Qlot](https://github.com/fukamachi/qlot) - 项目本地库安装程序，类似于 Bundler 或 Virtualenv。 [外籍人士][14]。
* 如何在没有 Roswell 的情况下[从 Lisp REPL 使用它](https://github.com/svetlyak40wt/qlot-without-roswell)。
* [vend](https://github.com/fosskers/vend) - 只需供应您的依赖项即可！ [MPL-2.0][211]。

另请参阅：

* [CLPM](https://www.clpm.dev) - Common Lisp 的包管理器，致力于将包管理器进程本身与使用它的客户端映像完全分离。 [BSD_2 条款][17]。
* CLPM 作为预构建的二进制文件提供，默认支持 HTTPS，支持安装多个软件包版本，支持版本化系统等等。
* [trivial-system-loader](https://github.com/atgreen/trivial-system-loader) - Common Lisp 的系统安装/加载抽象。
* 与使用除 Quicklisp 之外的其他库管理器的人相处融洽：不要使用硬编码 `(ql:quickload :mysystem)`，而是使用 `(tsl:load-system :mysystem)`。 tsl:load-system 将首先尝试使用 ocicl（如果可用），然后是 Quicklisp，最后是普通的 asdf:load-system。
* [Quicksys](https://lisp.com.br/quicksys/) - 安装来自多个 Quicklisp 发行版的系统。 [麻省理工学院][200]。
* [Quickutil](https://github.com/stylewarning/quickutil) - 实用程序管理器，类似于 Quicklisp，但适用于小型实用程序而不是整个库。 [3 条款 BSD][15]。

可能有帮助：

* [redist](https://github.com/shirakumo/redist) - 生成 Quicklisp 发行版的设施。
* [quick-patch](https://github.com/tdrhq/quick-patch/) - 无需使用 git 子模块即可轻松覆盖 Quicklisp 项目。 [MPL-2.0][211]。
* [print-licenses](https://github.com/vindarel/print-licenses) - 打印项目及其依赖项使用的许可证。 [麻省理工学院][200]。
* [asdf-dependency-graph](https://github.com/digikar99/asdf-dependency-graph/) - 围绕“dot”的最小包装器，用于生成依赖关系图的图像。

## 与其他包管理器的接口

* [linux-packaging](https://gitlab.com/ralt/linux-packaging) - 使用单个 ASDF 声明为您的应用程序构建 .deb、.rpm 或 .pkg 包。在后台使用 fpm。 [麻省理工学院][200]。
* [qldeb](https://github.com/ralt/qldeb) - Quicklisp 系统到 debian 软件包，以及 [deb-packager](https://github.com/ralt/deb-packager)（只需通过定义 s-表达式来创建 debian 软件包）。两者都是[麻省理工学院][200]。
* [ql-to-deb](https://github.com/dimitri/ql-to-deb) - 从 Quicklisp 版本更新 cl-* debian 软件包。 WTFPL。
* [dh-quicklisp-buildapp](https://github.com/ralt/dh-quicklisp-buildapp) - debhelper 实用程序可让您几乎毫不费力地将基于 Quicklisp 的 Common Lisp 代码编译为 .deb 中的 buildapp 二进制文件。 [麻省理工学院][200]。
* [cl-brewer](https://github.com/can3p/cl-brewer) - 用于（命令行）common lisp 应用程序的自制公式生成器。公共领域。
* [flatpack-common-lisp](https://gitlab.com/ralph-schleicher/flatpak-common-lisp) - 一个 BuildStream 项目，用于为 Common Lisp 应用程序构建基于 Flatpak 的运行时环境。
* [alien-works-delivery](https://github.com/borodust/alien-works-delivery) - 用于将 Common Lisp 应用程序作为可执行包提供的 WIP 系统。目前，它仅支持 Linux 的 AppImage 格式和 Windows 的 MSIX 格式，但也计划支持 Android 的 .APK 以及更高版本的 MacOSX 和 iOS 捆绑包格式。
* [cl-nix-lite](https://github.com/hraban/cl-nix-lite) - Nix 的 Common Lisp 模块，没有 Quicklisp。 [AGPL-3.0][51]


另请参阅：

- [asdf-sbcl](https://github.com/smashedtoatoms/asdf-sbcl)，通用包管理器的插件。
- 📹 [此 Youtube 视频](https://www.youtube.com/watch?v=lGS4sr6AzKw)（由 40ants，2023 年）介绍如何使用 Alien-works-delivery 和 linux-packaging。

网络和互联网
====================

更多信息请参见[Cliki](http://www.cliki.net/Web)。

HTTP 客户端
------------
* 👍 [Dexador](https://github.com/fukamachi/dexador) - 一个 HTTP 客户端，旨在取代 Drakma。 [麻省理工学院][200]。
* [Carrier](https://github.com/orthecreedence/carrier) - 构建在 cl-async 和 fast-http 之上的轻量级异步 HTTP 客户端。 [麻省理工学院][200]。
* [fast-http](https://github.com/fukamachi/fast-http) - Common Lisp 的快速 HTTP 请求/响应解析器。 [麻省理工学院][200]。
* [http2](https://github.com/zellerin/http2/) - Common Lisp 中的 HTTP/2 实现。 [麻省理工学院][200]。


HTTP 服务器
------------

* ⭐ [Hunchentoot](http://weitz.de/hunchentoot/) - 网络服务器。 [2 条款 BSD][207]
* 👍[Clack](https://github.com/fukamachi/clack) - 受 Rack 和 WSGI 启发的 Web 应用程序环境。 [LLGPL][8]。  为所选的网络服务器提供统一的接口（默认为 Hunchentoot）。有更多[入门指南](https://jasom.github.io/clack-tutorial/posts/getting-started-with-clack/)。
* [wookie](https://github.com/orthecreedence/wookie) - 异步 HTTP 服务器。 [外籍人士][14]。
* [woo](https://github.com/fukamachi/woo) - 基于 libev 的快速非阻塞 HTTP 服务器。 [麻省理工学院][200]。

另请参阅：

* [portableaserve](https://github.com/sharplispers/portableaserve) - 尝试向其他 lisp 实现提供 Franz.com 的 [AllegroServe Web 服务器](https://github.com/franzinc/aserve)（开源但与 AllegroCL 绑定）的功能。
* Quicklisp 上名为 `aserve` 的系统。
* AllegroServe 是开源的：LGPL2.1。
* 它提供：
* 符合 HTTP/1.1 的 Web 服务器能够提供静态和动态页面。
* 用于客户端服务器的 SSL、Web 代理、CGI、动态分块、压缩和膨胀文件，
* 发布功能，从静态和动态数据构建页面并处理结果缓存，并具有访问权限。
* Allegro 的 [Aserve 文档](https://github.com/franzinc/aserve/blob/master/doc/aserve.md)
*！并非所有 AllegroServe 测试都在 portableaserve 上通过。
  * [zaserve](https://github.com/gendl/aserve) - AllegroServe 的便携式叉子 [LLGPL][8]。
* [cl-http2-protocol](https://github.com/akamai/cl-http2-protocol) (*已存档*) - 草案 14 中 HTTP/2 协议的纯 Common Lisp 传输不可知实现。 [麻省理工学院][200]。

### Hunchentoot 插件

* 👍 [easy-routes](https://github.com/mmontone/easy-routes) - Hunchentoot 之上的路由处理系统。它支持基于 HTTP 方法的调度、从 url 路径中提取参数、装饰器、从路由名称生成 url 等。[MIT][200]。
* [hunchentoot-cgi](https://github.com/slyrus/hunchentoot-cgi) - 用于从 hunchentoot Web 服务器执行 CGI 脚本的库。 [BSD][207]。
* [hunchentoot-multi-acceptor](https://github.com/moderninterpreters/hunchentoot-multi-acceptor/) - 使用单个端口在单个 hunchentoot 接受器上路由多个域（虚拟主机）。 [Apache2.0][89]。
* [hunchentoot-errors](https://github.com/mmontone/hunchentoot-errors) - 使用请求和会话信息增强了 Hunchentoot 错误页面和日志。 [麻省理工学院][200]。
* [hunchentoot-stuck-connection-monitor](https://github.com/avodonosov/hunchentoot-stuck-connection-monitor/) - 监控 hunchentoot 连接并记录长时间处于同一状态的连接。
- 提供手动或自动关闭卡住的连接套接字的选项，从而解锁连接线程并防止线程和套接字泄漏。 [BSD_2 条款][17]。

使 Hunchentoot 更快：

* [cl-tbnl-gserver-tmgr](https://github.com/mdbergmann/cl-tbnl-gserver-tmgr) - Hunchentoot 基于 Gserver 的任务管理器。 cl-gserver 是一个类似于 actor 的消息传递库（请参阅下面的“Actors 模式”）。实验性的。
* [hunchentoot-recycling-taskmaster](https://github.com/y2q-actionman/hunchentoot-recycling-taskmaster) - Hunchentoot 的任务管理器实现，旨在通过线程池和灵活的线程数调整来提高连接建立效率。 BSD_2 条款。

### 叮当插件

* [tiny-routes](https://github.com/jeko2000/tiny-routes) - 一个针对 Common Lisp 的小型路由库，目标是 Clack。 [BSD_3 条款][15]。
* [clack-errors](https://github.com/eudoxia0/clack-errors) - Clack 的错误页面中间件。未维护。 [LLGPL][8]。
* [clath](https://github.com/BnMcGn/clath) - 单点登录
Clack 的中间件。它允许使用 OAuth1.0a、OAuth2 进行基本登录
和 OpenID。在撰写本文时，它支持来自
谷歌、Twitter、LinkedIn、StackExchange、Reddit 和 Github。 [Apache2.0][89]。
* [clack-pretend](https://github.com/BnMcGn/clack-pretend) - 一个测试
以及clack的调试工具。 [Apache2.0][89]。
* [hismetic](https://github.com/dertuxmalwieder/cl-hismetic) - 基于 Clack 的 Web 应用程序的安全性。 [外籍人士][14]。
* [live-reload](https://github.com/knobo/live-reload) - clack 的实时重新加载原型。 [LLGPL][8]。
* [clack-static-asset-middleware](https://github.com/fisxoj/clack-static-asset-middleware) - 一个用于 clack 的缓存清除静态资产中间件。 [麻省理工学院][200]。
* [lack-expression-cache](https://github.com/daninus14/lack-compression-cache) - 缺乏用于压缩和缓存静态资源的中间件。麻省理工学院。
* [lack-rerouter](https://github.com/daninus14/lack-rerouter) - 缺乏重新路由请求 URI 的中间件。麻省理工学院。
* [clack-cors](https://40ants.com/clack-cors/) - 用于设置 CORS 相关 HTTP 标头的 Clack 中间件。 — 无执照。
* [clack-promotheus](https://40ants.com/clack-prometheus/) - Clack 中间件以 Prometheus 格式提供统计数据。无执照。


网络框架
--------------

* [Caveman](https://github.com/fukamachi/caveman) - 一个强大的网络框架。 [LLGPL][8]。
示例项目：[Quickdocs](https://github.com/quickdocs)
* [ningle](https://github.com/fukamachi/ningle) - 一个超微型网络框架。 [LLGPL][8]。
  - [jingle](https://github.com/dnaeon/cl-jingle) - 基于 ningle，添加了附加功能，例如中间件。
- 包括 OpenAPI 和 Swagger UI 演示。
* [radiance](https://codeberg.org/shirakumo/radiance) - Web 应用程序环境和框架。 [zlib][33]。

以 REST 为中心的框架：

* 👍 [Snooze](https://github.com/joaotavora/snooze) - 一个 RESTful Web 框架。与 Web 服务器无关。目前支持 Hunchentoot 和 Clack。路由只是函数，HTTP 条件只是 Lisp 条件。 [LLGPL][8]。
* [cl-rest-server](https://github.com/mmontone/cl-rest-server) - 用于编写 REST Web API 的库。具有模式验证、日志记录注释、缓存、权限或身份验证、通过 Swagger 提供的文档等功能。[MIT][200]。

请参阅下面的 OpenAPI、OData 和其他库。

### 同构 Web 框架

* [CLOG](https://github.com/rabbibotton/clog) - Common Lisp Omnificent GUI。使用 Web 技术为本地或远程应用程序生成图形用户界面。 [BSD_3 条款][15]。
- CLOG 基于 GNOGA 的思想，GNOGA 是作者为 Ada 编写的框架，自 2013 年起用于商业生产代码。
* [Weblocks (Reblocks)](https://github.com/40ants/reblocks) - 一个基于小部件的框架，具有内置的 ajax 更新机制，可以“解决 JavaScript 问题”。 [LLGPL][8]。
- 示例代码库：[Ultralisp](https://github.com/ultralisp/ultralisp/)、[krasnodar](https://github.com/lct23/krasnodar)、为 hackaton 制作的仪表板 (2024) ([demo视频](https://diode.zone/videos/watch/9e379a86-c530-4e9d-b8be-7437b1f7200b))。
* [Interactive SSR](https://github.com/interactive-ssr/client/blob/master/main.org/) - ISSR 允许您制作交互式网页，而无需编写客户端脚本。无需了解 Javascript 或 DOM。
- 它与 Phoenix LiveView 或 Hotwire 没有什么不同。

基于 CLOG 的框架：

- [mold-desktop](https://codeberg.org/mmontone/mold-desktop) - 可编程桌面。
- [WIP] [clog-moldable-inspector](https://codeberg.org/khinsen/clog-moldable-inspector) - 基于 CLOG 的可塑 Common Lisp 对象检查器。因此，检查器显示在 Web 浏览器中。


解析html
---------------
* 👍 [Plump][71] - 一个宽松的 HTML/XML 解析器，能够容忍格式错误的标记。 [zlib][33]。最好与 [lquery][72] 和 [clss](https://codeberg.org/shimera/CLSS) 一起使用。
* [cl-html5-parser](https://github.com/rotatef/cl-html5-parser) - Common Lisp 的 HTML5 解析器。 GPL3.0。
* Python 库 html5lib 的端口。
* 与 Plump 相比：Plump 是 XML 和 HTML 解析器的混合体，违反了一些 HTML 规则，而 cl-html5-parser 是完全兼容的 HTML 解析器。

清理 HTML：

* [cl-sanitize-html](https://github.com/atgreen/cl-sanitize-html/) - 适用于 Common Lisp 的 OWASP 样式 HTML 清理库，旨在安全地呈现不受信任的 HTML 内容（例如 HTML 电子邮件或用户生成的内容）。麻省理工学院。
- 部分是法学硕士。 [reddit 公告](https://old.reddit.com/r/Common_Lisp/comments/1q30bqh/atgreenclsanitizehtml_a_common_lisp_library_for/)。
- 相关：[trivial-sanitize](https://codeberg.org/cage/trivial-sanitize)


查询 HTML/DOM、网页抓取
---------------------------------------

* 👍 [lquery][72] - 类似 jQuery 的 HTML/DOM 操作库。 [zlib][33]。
* [scrapycl](https://40ants.com/scrapycl/) - 用于用 Common Lisp 编写爬虫的网络抓取框架。无执照。
* 依赖lquery。

另请参阅下面的 XML 部分以了解 xpath 库等。


HTML 生成器和模板
-----------------------------

* 👍 [spinneret](https://github.com/ruricolist/spinneret) - Common Lisp HTML5 生成器。 [外籍人士][14]。
* ⭐ [cl-who](http://weitz.de/cl-who/) - 久负盛名的 HTML 生成器。 [FreeBSD][39]。
* ⭐ [Djula](https://github.com/mmontone/djula) - Django 模板引擎到 Common Lisp 的端口。 [外籍人士][14]。
  - [cl-djula-tailwind](https://github.com/rajasegar/cl-djula-tailwind) - 在 Djula 模板中使用 TailwindCSS 类，无需任何 JavaScript 或 Node.js 工具。
  - [djula-template-designer](https://github.com/mmontone/djula-template-designer) - 模板设计器工具。
* [TEN](https://github.com/mmontone/ten) - Djula 的完整性以及模板中 Common Lisp 代码的完全可用性。 [麻省理工学院][200]。
* [cl-closure-template](https://github.com/archimag/cl-closure-template) - Google Closure 模板的实现，其中编译模板会创建一个生成结果的函数。 [LLGPL][8]。
* [hsx](https://github.com/skyizwhite/hsx/) - 一个易于组合的 HTML5 生成库，具有最简单的语法。 [麻省理工学院][200]。
* [clip](https://shinmera.github.io/clip) - HTML 模板处理器，其中模板以 HTML 编写。 [zlib][33]。
* [lsx](https://github.com/fukamachi/lsx/) 和 [markup](https://github.com/moderninterpreters/markup) - 两个类似 JSX 的模板引擎，其中 HTML 标签是 Common Lisp 代码。 `markup` 带有 Emacs 包。

URI 和 IP 处理
-------------------

* [quri](https://github.com/fukamachi/quri) - 另一个 URI 库
通用 Lisp。支持用户信息、IPv6主机名、编码/解码
公用事业，... [BSD_3Clause][15]。
* [cl-slug](https://github.com/lisp-maintainers/cl-slug) - 一个小型库，用于制作 slugs，主要用于 URI，以 CamelCase 进行转换，删除重音符号和标点符号，适用于英语及其他语言。 [LLGPL][8]。
* [netaddr](https://github.com/ynadji/netaddr) - Common Lisp 的网络地址操作库。麻省理工学院。
* 用于操作 IP 地址、子网、范围和集。它的灵感来自于 Python 中的同名库 netaddr。

JavaScript
----------

* ⭐ [Parenscript](https://common-lisp.net/project/parenscript/) - 从 Common Lisp 到 Javascript 的翻译器。 [3 条款 BSD][15]。请参阅 [Trident-mode](https://github.com/johnmastro/trident-mode.el)，这是一种提供与浏览器实时交互的 Emacs 模式。[unlicence][5]。
  * [paren6](https://github.com/BnMcGn/paren6/) - 一组用于 Parenscript 的 ES6 宏。
* [paren-async](https://github.com/Junker/paren-async) async/await 用于 Parenscript。
  * [paren-jquery](https://github.com/Junker/paren-jquery) - Parenscript 的 Jquery 风格宏。麻省理工学院。
* 示例：渐进式 Web 应用程序 (PWA) [2025] 的 [ParenScript + Mithril 演示](https://mmontone.codeberg.page/lisp-pwa/#!/home)。
* 示例：[使用 ParenScript 和 Preact 构建空当接龙游戏](https://nickfa.ro/wiki/Building_with_Parenscript_and_Preact) [2024]。
* [JSCL](https://github.com/jscl-project/jscl) - 一个从第一天起就被设计为自托管的 CL 到 JS 编译器。 GPL3.0。
* 完全支持 `format`([pull request](https://github.com/jscl-project/jscl/pull/525))
* 支持 `loop`([tests](https://github.com/jscl-project/jscl/tree/master/tests/loop)) 和 `CLOS`([tests](https://github.com/jscl-project/jscl/blob/master/tests/clos.lisp))
  * [现场游乐场](https://jscl-project.github.io/)
* 🔥 [实时 JupyterLite 游乐场](https://wiki3-ai.github.io/jscl-kernel/)（由 Wasm 驱动的 Jupyter 在浏览器中运行）。项目来源：[jscl-kernel](https://github.com/wiki3-ai/jscl-kernel)。
* [CL-JavaScript](http://marijnhaverbeke.nl/cl-javascript/) - 从 Javascript 到 Common Lisp 的翻译器。在 Quicklisp 上不可用。 [外籍人士][14]。
* [parse-js](http://marijnhaverbeke.nl/parse-js/) - 用于解析 ECMAScript 3 的包。[zlib][33]。
* [remote-js](https://github.com/ceramic/remote-js) - 将 JavaScript 从 Common Lisp 发送到浏览器。 [麻省理工学院][200]。
* [sigil](https://github.com/BnMcGn/sigil) - Javascript 命令行编译器和 REPL 的 Parenscript。 [麻省理工学院][200]。

开发中：

* [Valtan](https://github.com/cxxxr/valtan) - Common Lisp 到 JavaScript 编译器。
* [JACL](https://tailrecursion.com/JACL/) - 用于 Web 浏览器平台的实验性 Lisp 系统，用于探索使用 Lisp 开发大型单页应用程序的新技术。
* [SLip](https://lisperator.net/slip/) - 浏览器中理想的 Common Lisp 环境。
* 自托管编译器、TCO、CLOS、结构、条件、循环和格式、JavaScript“FFI”、绿色线程……
* 受 Emacs 和 Slime 启发的浏览器内开发环境，基于 [Ymacs](https://lisperator.net/ymacs/)。
* [现场演示](https://lisperator.net/s/slip/)！


**React** 的实用程序：

* [cl-react](https://github.com/helmutkian/cl-react) - 用于在 ReactJs 中构建 Web 应用程序的 Common Lisp (Parenscript) 实用程序。麻省理工学院。
* [Panic](https://github.com/michaeljforster/panic)，React 的 Parenscript 库。不在 Quicklisp 中。 [麻省理工学院][200]。它的[TodoMVC示例](https://github.com/40ants/todomvc/blob/common-lisp-example/examples/common-lisp-react/src/app.lisp)。
* [Parenscriptx](https://github.com/jasom/parenscriptx) - Parenscript 宏帮助生成反应代码。 [麻省理工学院][200]。
* [jscl-react](https://github.com/nilesr/jscl-react) - 一个使用 jscl 在 common lisp 中编写 React 组件的 Web 框架。未指定许可证。

**[Datastar](https://data-star.dev/)** 的 SDK：

- [datastar-cl](https://github.com/fsmunoz/datastar-cl) - Datastar Common Lisp SDK。
- 在线演示：https://dataspice.interlaye.red/


另请参阅：

* [trident-mode](https://github.com/johnmastro/trident-mode.el)，一种用于实时 Parenscript 交互的 Emacs 小模式。


部署
----------

* 👍 [deploy](https://shinmera.github.io/deploy) - 用于 Lisp 应用程序二进制部署的工具包，并对外部共享库提供额外支持。 [zlib][33]。
* [common-lisp-heroku-example](https://github.com/fstamour/common-lisp-heroku-example) - Heroku 上使用 Docker 的 Common Lisp 服务器示例。
* [cube](https://github.com/xh4/cube) - 根据 Swagger 规范生成的 Common LISP 的 Kubernetes 客户端库。 [麻省理工学院][200]。
* [s2i-lisp](https://github.com/container-lisp/s2i-lisp) - 基于 CentOS 或 RHEL7 的源到映像构建器映像，用于为 OpenShift（以及 Docker）构建 Common LISP 映像。它具有最新的 SBCL 和 Quicklisp 安装、SLIME 或 SLY 集成，并允许通过环境变量进行自定义。 [阿帕奇2][89]
* [cl-aws-runtime-test](https://github.com/y2q-actionman/cl-aws-custom-runtime-test) - 使用 Common Lisp (SBCL) 作为 AWS lambda 上的自定义运行时的示例。 WTFPL。
* [40ants/ci](https://github.com/40ants/ci/) - 适用于 Common Lisp 项目的高度自动化的 Github Actions 工作流程构建器。
* 包括：linter、lisp comment、测试运行器、测试矩阵、文档构建、缓存……
* [make-common-lisp-program](https://github.com/melusina-org/make-common-lisp-program/) - 在 Ubuntu、MacOS 和 Windows 上构建可执行 Common Lisp 程序的 GitHub 操作。麻省理工学院。

另请参阅：

- [Cloud Init file for SBCL](https://git.sr.ht/%7Emarcuskammer/cloudinit/tree/main/item/sbcl-nginx.yml) - 支持 cloudinit 格式（DigitalOcean 等）的提供商的 init 文件。

### 托管平台

我们可以在任何服务器上托管 Common Lisp 服务。这些服务提供
CL 的开箱即用可用性：

- [Heliohost](https://www.heliohost.org/) 免费托管解决方案。
- [Nearly Free Speech](https://www.nearlyfreespeech.net/) - 超过 25 种编程语言，按使用量付费。
- SBCL 和 GNU CLISP


监控
----------

* [prometheus.cl](https://github.com/deadtrickster/prometheus.cl) - Prometheus.io 客户端。用于 SBCL 和 Hunchentoot 指标（内存、线程、每秒请求数……）的 Grafana 仪表板。 [麻省理工学院][200]。
  * [prometheus-g](https://github.com/40ants/prometheus-gc) - prometheus.cl 的扩展，用于收集有关垃圾收集器状态的指标。
* [lisp-sentry](https://gitlab.com/lockie/lisp-sentry) - 用于 Sentry 应用程序监控软件的全功能 Common Lisp 客户端库。麻省理工学院。
* 依赖关系较轻，为 Sentry 提供堆栈跟踪中的源代码，支持文件附件、事件面包屑、自动填充的执行上下文、线程和用户报告、GPU 信息。
* 仅支持SBCL
* [cl-sentry-client](https://github.com/mmontone/cl-sentry-client) - Common Lisp（基于云的错误监控系统）的 Sentry 客户端。 [麻省理工学院][200]。
* 基于用于 HTTP 通信的 dexador 和用于堆栈跟踪的 swank。它还通过简单任务库提供异步 HTTP 客户端。
* [rollbar.lisp](https://github.com/adventuring/rollbar.lisp) - 与错误跟踪软件 [Rollbar.com](https://rollbar.com/) 的接口。


网络套接字
----------

* 👍 [usocket](https://github.com/usocket/usocket) - 一个可移植的 TCP 和 UDP 套接字接口。 [外籍人士][14]。
* [Portal](https://github.com/charJe/portal) - Common Lisp 的可移植 websocket，使用 usocket。 [LLGPL][8]。
* [clws](https://github.com/3b/clws) - CL 中的 websockets 服务器，基于 IOlib 和 libfixposix 构建。麻省理工学院。
* [Hunchensocket](https://github.com/joaotavora/hunchensocket) - 适用于 Common Lisp 的 RFC6455 兼容 WebSocket，作为 Hunchentoot 的扩展。 [麻省理工学院][200]。
* [websocket-driver](https://github.com/fukamachi/websocket-driver) - 基于克拉克。
* [iolib](https://github.com/sionescu/iolib) - I/O 库。 [外籍人士][14]。
*“IOlib 是一个比标准 Common Lisp 库更好、更现代的 I/O 库。它包含：套接字库、DNS 解析器、I/O 多路复用器、路径名库和文件系统实用程序。”

*编者注：在撰写本文时，我们似乎还没有 Common Lisp 的全功能 websocket 实现。不过，我们可以推荐 Portal，并邀请您仔细检查 Hunchensocket 和 websocket-driver 的当前问题。*

HTTPS
-----

- [pure-tls](https://github.com/atgreen/pure-tls) - 纯 Common Lisp TLS 1.3 实现，带有自动 Let's Encrypt 证书的 HTTPS 服务器。麻省理工学院
- 警告：新代码，部分由法学硕士完成。
- 阅读：
    - [在 Common Lisp 中构建 TLS 1.3 实现](https://atgreen.github.io/repl-yell/posts/pure-tls/)
    - [使用 pure-tls/acme 为 Common Lisp 提供自动 TLS 证书](https://atgreen.github.io/repl-yell/posts/pure-tls-acme/)


网络开发实用程序
-------------------------

### 浏览器测试

* [cl-webdriver-client](https://github.com/copyleft/cl-webdriver-client/) - WebDriver 的绑定库（支持 Selenium 4.0）。

### 表格处理

* 👍 [cl-forms](https://github.com/mmontone/cl-forms) - Common lisp 的 Web 表单处理库。 [麻省理工学院][200]。

### 用户登录和密码管理

* [cl-authentic](https://github.com/charJe/cl-authentic) - Common Lisp（Web）应用程序的密码管理。 [LLGPL][8]。
- 安全密码存储：无明文，通过铁定使用您选择的哈希算法，存储在 SQL 数据库中，
- 具有一次性令牌的密码重置机制（适合邮寄给用户进行确认），
- 可选择使用确认令牌创建用户（适合邮寄给用户），
* [mito-email-auth](https://github.com/40ants/mito-email-auth) - 通过电子邮件向网站用户发送唯一代码来帮助验证网站用户。

* [cl-cas](https://github.com/fferrere/cl-cas) - 一个帮助 [CAS 验证](https://en.wikipedia.org/wiki/Central_Authentication_Service) 进行 Common Lisp Web 应用程序的库。不在 Quicklisp 中。
  * [cas-middleware](https://github.com/fferrere/cas-middleware) - Caveman 的 CAS 身份验证中间件。
  * [cas-demo](https://github.com/fferrere/cas-demo) - 一个演示项目。

另请参阅上面的 mito-auth 以及 Hunchentoot 和 Clack 插件。

### Web 项目框架和生成器

* [cl-cookieweb](https://github.com/vindarel/cl-cookieweb) - 用于启动 Web 项目的 Cookiecutter 模板。 [BSD_3 条款][15]。不在 Quicklisp 中。
* 提供一个可运行的玩具 Web 应用程序，其中包含 Hunchentoot Web 服务器、简单路线、Djula 模板、Bulma 样式、基于 SQLite、迁移、示例表定义和使用 FiveAM 的测试套件。
* [make-like](https://github.com/container-lisp/make-like) - 适用于 LIKE（Kubernetes + Emacs 中的 Lisp）应用程序的应用程序模板构建器。 [Apache2.0][51]。
* Makefile、podman 支持、GitHub Actions、Prometheus 指标支持、TOML 风格的 config.ini、预配置健康检查的简单路由等。
* [cl-webapp-seed](https://github.com/rajasegar/cl-webapp-seed) - 一个简单的 Web 应用程序样板。使用 Hunchentoot、cl-who，轻松部署到 Heroku。 [麻省理工学院][200]。

其他
------

* [LASS](https://codeberg.org/shinmera/LASS) - Lisp 增强样式表。很大程度上受到 SASS 的启发。兹利布。
* [css-lite](https://github.com/paddymul/css-lite) - CSS 语法。 [外籍人士][14]。
* [find-port](https://github.com/lisp-maintainers/find-port) - 以编程方式查找开放端口。 [麻省理工学院][200]。
* [cl-wget](https://github.com/cl-wget/cl-wget) - 使检索大文件或镜像整个网站变得容易。 [AGPL-3.0][51]。
* [trivial-download](https://github.com/eudoxia0/trivial-download) - 下载文件。
* 目前已存档且未维护。 [麻省理工学院][200]。
* [cl-cookie](https://github.com/fukamachi/cl-cookie) HTTP Cookie (jar) 管理器：解析和写入 (set-)cookie 标头、比较 cookie、可选的 cookie 属性健全性检查。 [麻省理工学院][200]
* [dns-client](https://codeberg.org/Shinmera/dns-client) - DNS 记录客户端。请参阅[文档](https://shimera.github.io/dns-client/)。 [zlib][33]。
* [mobiledetect](https://github.com/Junker/mobiledetect) - 用于检测用户代理字符串中的移动设备（包括平板电脑）的系统。麻省理工学院。
* [random-ua](https://github.com/Junker/random-ua) - Common Lisp 的随机用户代理生成器。 BSD_2 条款。
* [cl-web-push](https://github.com/ryukinix/cl-web-push) - Common Lisp 应用程序的 Web 推送通知。


### 电子邮件

* [trivial-imap](https://github.com/40ants/trivial-imap) - 尝试简化使用 IMAP 服务器的一些常见情况，例如从服务器读取电子邮件。邮局库（Franz 的 cl-imap 的一个分支）的薄包装。 [BSD][15]。
* [cl-smtp](https://gitlab.common-lisp.net/cl-smtp/cl-smtp) - CL-SMTP 是一个简单的 lisp smtp 客户端。

通过第三方提供商发送电子邮件：

* [sendgrid](https://github.com/vindarel/cl-sendgrid) - 使用 Sendgrid 的 API 发送电子邮件。 [麻省理工学院][200]。
* [mailgun](https://github.com/40ants/mailgun) - 通过 mailgun.com 发布 HTML 电子邮件的薄包装。 [无执照][5]。

解析电子邮件地址：

* [parcom/email](https://github.com/fosskers/parcom/?tab=readme-ov-file#email-addresses) - RFC5322 电子邮件地址的类型和解析器。该实现符合 RFC 标准，并且对于表现良好的地址来说特别具有内存效率。


### OpenAPI、OData、OpenRPC

* 新！ [openapi-generator](https://codeberg.org/kilianmh/openapi-generator) - OpenAPI 客户端代码生成器。 [AGPL-3.0][51]。
* 在一个命令中生成 OpenAPI ASDF/Quicklisp 可加载项目，
* 支持路径、（任意）查询、（任意）标头、（json）内容参数、
* 将 OpenAPI 规范转换为 CLOS 对象 -> 在检查器中探索 API，
* 使用 swagger 转换器将 OpenAPI-2.0 或 YAML 文件转换为 OpenAPI-3.0 JSON（需要网络连接），
* 等
* [apispec](https://github.com/cxxxr/apispec) - 用于处理 Web API 请求和响应的 Common Lisp 库。 [BSD_3 条款][15]。
- 采用 OpenAPI3 yaml 规范，并允许验证和解析 HTTP 请求标头、参数和主体。
* [cl-odata-client](https://github.com/copyleft/cl-odata-client) - 用于访问 [OData 服务](https://www.odata.org) 的 Common Lisp 客户端库。 [麻省理工学院][200]。
* [OpenRPC](https://github.com/40ants/openrpc) - Common Lisp 的 OpenRPC 实现。 [BSD][15]。
- 自动生成 OpenRPC 规范
- 按照 OpenRPC 规范自动构建 JSON-RPC 客户端。这包括创建用于发出 RPC 请求和返回本机 CL 对象的 Common Lisp 类和方法。
- 所有 JSON 编组都是在后台完成的。
- [jsonrpc](https://github.com/cxxxr/jsonrpc) - Common Lisp 的 JSON-RPC 2.0 服务器/客户端。 [BSD][15]。


### 静态站点生成器

* [凉拌卷心菜](https://github.com/kingcons/coleslaw) 及其
[coleslaw-cli](https://github.com/40ants/coleslaw-cli) - 灵活
Lisp Blogware 类似于 Frog、Jekyll 或 Hakyll。 [BSD][15]。

### 第三方API

* [pirá](https://github.com/fukamachi/pira) - 适用于 Common Lisp 的非官方 AWS 开发工具包。
*“Pirá 是一款基于 Smithy 协议框架构建的现代非官方 Common Lisp AWS 开发工具包。它通过从官方 AWS 服务模型自动生成的客户端代码提供全面的 AWS 服务覆盖。”
* 支持400+ AWS服务
* 多种协议：REST-JSON、REST-XML、AWS 查询、EC2 查询和 AWS JSON。
* [aws-sdk-lisp](https://github.com/pokepay/aws-sdk-lisp/) - 为每个 AWS 服务作为单独的系统提供接口。 [BSD_2 条款][17]。
* *打算被皮拉取代*
* 包括数十种服务：dsn、appstream、athena、cloudfront、codedeploy、cognito-*、directconnect、dynamodb、dms、elasticache、电子邮件、事件、kinesis、机器学习、监控、s3、sms、storagegateway、工作区...
* [Aws-sign4](https://github.com/rotatef/aws-sign4) - 用于 Amazon Web Services 签名版本 4 的 Common Lisp 库。[GNU GPL3][2]。
* [zs3](https://github.com/xach/zs3) - 用于使用 Amazon Simple Storage 的库
服务 (S3) 和 CloudFront 服务。 [BSD][15]。
* [north](https://shinmera.github.io/north) - South (Simple OaUTH) 库的后继者，在客户端和服务器端实现了完整的 oAuth 1.0a 协议。使用 North，您可以轻松成为 oAuth 提供者或消费者。 [zlib][33]。
* [Ciao](https://github.com/kjinho/ciao) - 易于使用的 Common Lisp OAuth 2.0 客户端库。它是 Racket OAuth 2.0 客户端到 Common Lisp 的端口。 [LGPL3][9]。
* [cl-oauth2](https://sr.ht/~hajovonta/cl-oauth2/) - Common Lisp 的 OAuth 2.0 和 OpenID Connect 客户端库。支持授权码（使用 PKCE）、客户端凭据、设备授权、令牌刷新、JWT 验证 (RS256/ES256/HS256)、OIDC 发现和令牌缓存。麻省理工学院。
* *由法学硕士构建*
* [tooter](https://codeberg.org/shinmera/tooter) - 为 Mastodon 实现完整 v1 REST API 协议的客户端库。 [zlib][33]。
* [cl-irc](https://www.common-lisp.net/project/cl-irc/) - IRC 客户端库。 [外籍人士][14]。
* [cl-mediawiki](https://github.com/AccelerationNet/cl-mediawiki) - MediaWiki api 的包装器。 [麻省理工学院][200]。
* [cl-openid](https://github.com/cl-openid/cl-openid) - OpenID 的实现。 [LLGPL][8]。
* [cl-pushover](https://github.com/TeMPOraL/cl-pushover) - Common Lisp 与 Pushover 的绑定。 [麻省理工学院][200]。
* [humbler](https://codeberg.org/shinmera/humbler) - Tumblr API 接口。 [zlib][33]。
* [multiposter](https://codeberg.org/shinmera/multiposter) - 同时发布到多个服务。 [zlib][33]。
* [stripe](https://github.com/boogsbunny/stripe) - Stripe 支付系统的客户端。 [麻省理工学院][200]。
* [lisp-pay](https://github.com/K1D77A/lisp-pay) - 各种支付处理器的包装：Paypal、Stripe、Coin payments 和 BTCPayServer。 [麻省理工学院][200]。
* [lunamech-matrix-api](https://github.com/K1D77A/lunamech-matrix-api) - 客户端 -> 服务器矩阵 API 的完整包装。 [麻省理工学院][200]。
* [cl-telegram-bot](https://40ants.com/cl-telegram-bot/) - 电报机器人 API。 [麻省理工学院][200]。
* 包括示例机器人，例如计算器、发票付款、基于参与者的机器人......
* 自动API规范解析器
  * [cl-telegram-bot-auto-api](https://github.com/aartaka/cl-telegram-bot-auto-api) - 替代 Telegram Bot API 绑定，从 Telegram 网站自动生成。 [3 条款 BSD][15]。


数值与科学
========================

* ⭐ [maxima](http://maxima.sourceforge.net/) - 计算机代数系统。 [GNU GPL3][2]。
* [wxMaxima](https://wxmaxima-developers.github.io/wxmaxima/)：图形前端。
  * [Jupyter 上的 Maxima](https://github.com/robert-dodier/maxima-jupyter)
* [新，POC] [WASM 上浏览器中的 Maxima](https://maxima-on-wasm.pages.dev/)，[来源](https://gitlab.com/spaghettisalat/maxima/-/tree/emscripten-port-deployed)
* 它可以通过 [SageMath](https://www.sagemath.org/) 和 [KDE Cantor](https://apps.kde.org/cantor/) 使用。
* 它可以在 Emacs 中使用：
* [maxima-mode](https://gitlab.com/sasanidas/maxima) ([截图](https://community.linuxmint.com/img/screenshots/maxima-emacs.png))
* [maxima-interface](https://github.com/jmbr/maxima-interface) 简化 Maxima 和 Common Lisp 之间的接口。
    * [symbol-cruncher](https://git.sr.ht/~jmbr/symbol-cruncher) - 用于微分几何计算的计算机代数系统。构建在 maxima-interface 之上。
* [numcl](https://github.com/numcl/numcl) - Common Lisp 中的 Numpy 克隆。 [LGPL3][9]。
* [numericals](https://github.com/digikar99/numericals) - SIMD 通过 CFFI 支持 Common Lisp 数组上的简单数学数值运算 [仍处于实验阶段]。麻省理工学院。
* 文档：https://digikar99.github.io/numerics/
* [dense-arrays](https://github.com/digikar99/dense-arrays) - Numpy 类似于 Common Lisp 的数组对象。麻省理工学院。
* [GSLL](https://common-lisp.net/project/gsll/) - GNU Lisp 科学图书馆；允许使用 Common Lisp 中的 GSL。 [GNU LGPL2.1][11]。
* [Xecto](https://github.com/pkhuong/Xecto) - 用于常规数组并行性的库。 [3 条款 BSD][15]。
* [Petalisp](https://github.com/marcoheisig/Petalisp) - 尝试
为并行计算机生成高性能代码
JIT 编译数组定义。它适用于更多
比 NumPy 更基础的水平，提供更强大的
N 维数组，但只是一些用于处理的构建块
他们。 [AGPL-3.0][agpl3]。
* [cl-ana](https://github.com/ghollisjr/cl-ana) - Common Lisp 数据分析库强调模块化和概念清晰度。它的目标是成为一个用于分析小型和大型数据集的通用框架，包括分级数据分析和可视化。 [GNU GPL3][2]。
* [avm](https://github.com/takagi/avm) - 高效且富有表现力的阵列向量数学库，具有多线程和 CUDA 支持。 [麻省理工学院][200]。
* [array-operations](https://github.com/bendudson/array-operations) - 用于操作 Common Lisp 数组并用它们执行数值计算的函数和宏的集合。 [麻省理工学院][200]。
* [cl-geometry](https://github.com/Ramarren/cl-geometry/) - Common Lisp 的二维计算几何系统。 [麻省理工学院][200]。
* [Vellum](https://github.com/sirherrbatka/vellum) - Common Lisp 的数据框架。 BSD_2 条款。
* [rtg-math](https://github.com/cbaggers/rtg-math/) - 在 lisp 中制作实时图形最常用的数学例程的选择（2、3 和 4 个分量向量、3x3 和 4x4 矩阵、四元数、球坐标和极坐标）。 BSD_2 条款。


规划求解器：

* [linear-programming](https://neil-lindquist.github.io/linear-programming/) - 用于解决线性规划问题的库。 [麻省理工学院][200]。
* [shop3](https://github.com/shop-planner/shop3) - 分层任务网络 (HTN) AI 规划器。 Mozilla 公共许可证。


新的！如果您有精确的需求、模糊的需求或简单的问题，存储库 [Common Lisp numsci 需求需求](https://github.com/digikar99/common-lisp-numsci-call-for-needs) 是一个讨论它们的新地方。


矩阵库
----------------

* [LLA](https://github.com/Lisp-Stat/lla) - Lisp 线性代数。 MS-PL。
* 一个基于 BLAS 和 LAPACK 构建的高级 Common Lisp 库，但提供了更抽象的接口，目的是将用户从低级问题中解放出来，并减少数字代码中的错误数量。
* [magicl](https://github.com/quil-lang/magicl) - 基于 BLAS/LAPACK 和 Expokit 的 Common Lisp 中的矩阵代数程序，作者：RigettiComputing。 [BSD_3 条款][15]。
* [lisp-matrix](https://github.com/blindglobe/lisp-matrix) - 矩阵包。 [FreeBSD][39]。
* [3d-matrices](https://shinmera.github.io/3d-matrices) - 实现常见矩阵计算的库，重点关注图形中常用的 2x2、3x3 和 4x4 矩阵。它还提供了一些数值函数，但这些不是重点。该库经过了深度优化，因此它不是由漂亮的代码组成的。 [zlib][33]。
* [clem](https://github.com/slyrus/clem) - 矩阵库。 [BSD_2 条款][17]。

统计数据
---------

* 👍 [lisp-stat](https://github.com/lisp-stat) - 统计计算环境，概念上类似于 R，也适合一线生产部署。 “它源于一种愿望，即拥有一个能够快速构建分析和人工智能解决方案原型的环境，并以最小的摩擦直接转移到生产环境。”
* https://lisp-stat.dev/
* 受到 Luke Tierney 的 [XLisp-Stat](https://homepage.stat.uiowa.edu/~luke/xls/xlsinfo/)（R 的前身）的启发，为其提供了一个兼容性库，否则构建在其他和更新的库上。

另请参阅 [common-lisp-stat](https://github.com/blindglobe/common-lisp-stat/)，Common Lisp 统计库。 [FreeBSD][39]，陈旧。

单位
-----

* [physical-quantities](https://github.com/mrossini-ethz/physical-quantities) - 一个库，提供具有可选单位和/或不确定性的数字类型，用于自动错误传播的计算。通用公共许可证2

绘图
--------

* lisp-stat 的 [plot (vega-lite)](https://github.com/Lisp-Stat/plot) - 一个 Vega-lite DSL。 MS-PL。
* 包括在 REPL 中工作的基于文本的绘图功能，以及在浏览器中呈现的 JavaScript 可视化功能。
  * [emacs-vega-view](https://github.com/applied-science/emacs-vega-view?tab=readme-ov-file#common-lisp) - 一个 Emacs 插件，允许显示缓冲区中 lisp-stat 表达式的 Vega 图。
* [vgplot](https://github.com/volkers/vgplot) - 一个接口
gnuplot 绘图实用程序，旨在类似于某些
Octave 或 Matlab 的绘图命令。 [GPL3][2]。
* [eazy-gnuplot](https://github.com/guicho271828/eazy-gnuplot) - a
lispy，无结构的 Gnuplot 库。以其
[食谱](http://guicho271828.github.io/eazy-gnuplot/)。 [LLGPL][8]
* [kai](https://github.com/komi1230/kai) - Common Lisp 的高级绘图仪库。 [Plotly](https://plotly.com/javascript/) JS 库的包装器。 [麻省理工学院][200]。
* [ADW-Charting](https://common-lisp.net/project/adw-charting/) - 一个完全用 Common Lisp 编写的简单图表绘制库。还包括 Google 图表服务的后端。类似 BSD。

很酷但未完成：

* [plotly-user](https://github.com/ajberkley/plotly-user) - 在浏览器中使用plotly 来探索Common Lisp REPL 中的数据。 [BSD_3 条款][15]。

用文本绘制：

* [cl-text-plot](https://github.com/moneylobster/cl-text-plot/) - 用 Common Lisp 绘制文本。未指定许可证。
* [cl-spark](https://github.com/tkych/cl-spark) - 控制台的迷你图字符串：`(spark '(1 1 2 3 5 8))` => " ▂▃▅▇"。 [麻省理工学院][200]。

另请参阅 IUP 和 ltk-plotchart 的图表工具（GUI 部分）。

实用工具
-----

* [cmu-infix](https://github.com/rigetti/cmu-infix) - 用于在 Common Lisp 中编写中缀数学符号的库。另请参见 [polisher](https://github.com/mrcdr/polisher)。


并行性和并发性
===========================

* ⭐ [BordeauxThreads](https://common-lisp.net/project/bordeaux-threads/) - 可移植、共享状态并发。 [外籍人士][14]。
* ⭐ [lparallel](https://github.com/sharplispers/lparallel) - 并行编程库。 [3 条款 BSD][15]。最初位于 [lmj/lparallel](https://github.com/lmj/lparallel)。
- 具有[良好的文档](https://sharplispers.github.io/lparallel/)
* [lfarm](https://github.com/lmj/lfarm) - 跨机器分配工作（在 lparallel 和 usocket 之上）。 [BSD_3条款][15]
* [calispel](https://github.com/hawkir/calispel) - Common Lisp 的类似 [CSP](https://en.wikipedia.org/wiki/Communicating_sequential_processes) 的通道。具有阻塞、可选缓冲通道和“CSP select”语句。 ISC 风格。
- “它完整、灵活且易于使用。我会推荐 Calispel，而不是 Lparallel 和 ChanL。” @安布雷瓦尔。 [讨论](https://github.com/CodyReichert/awesome-cl/issues/290)
* [chanl](https://github.com/zkat/chanl) - 可移植的、基于通道的并发。 [Expat][14]，部分内容位于 [3-clause BSD][15] 下。
* [cl-async](https://github.com/orthecreedence/cl-async) - 用于通用、非阻塞编程的库。 [外籍人士][14]。
* [Moira](https://github.com/TBRSS/moira) - 监视并重新启动后台线程。 In-lisp 流程主管。 [麻省理工学院][200]。
* [trivial-monitored-thread](https://gitlab.com/ediethelm/trivial-monitored-thread) - 
一个 Common Lisp 库，提供了一种生成线程的方法
当其中任何一个坠毁并死亡时通知。 [麻省理工学院][200]。
* [cl-gearman](https://github.com/taksatou/cl-gearman) - 用于 [Gearman](https://github.com/gearman/gearmand/) 分布式作业系统的库。 [LLGPL][8]。
* [swank-crew](https://github.com/brown/swank-crew) - 使用Swank Client实现的分布式计算框架。 [BSD_3 条款][15]。
* [cl-coroutine](https://github.com/takagi/cl-coroutine) - 一个协程库。它在实现中使用 CL-CONT 延续库。 [麻省理工学院][200]。
* [STMX](https://github.com/cosmos72/stmx) - Common Lisp 的高性能事务内存。 [LLGPL][8]。
* [Blackbird](https://orthecreedence.github.io/blackbird/) - Common Lisp 的 Promise 实现 [MIT][200]。
* 另请参阅 [promise](https://codeberg.org/Shimera/promise) - 一个基本的 Promise 数据结构，带有超时。 ZLIB。
* [cl-cancel](https://github.com/atgreen/cl-cancel) - Common Lisp 的取消传播库，具有截止日期和超时。麻省理工学院。 *拥有法学硕士学位*。

另请参阅：

* [cl-etcd](https://github.com/atgreen/cl-etcd) - 将 etcd 作为异步下级进程运行。  [etcd](https://etcd.io/) 是一个强一致的分布式键值存储。 [AGPL-3.0][agpl3]。

演员图案
--------------

* 👍 [Sento](https://github.com/mdbergmann/cl-gserver) - Sento 是一个“消息传递”库/框架，其参与者类似于 Erlang 或 Akka。它支持创建反应式工作、需要并行计算和基于事件的消息处理的系统。 [阿帕奇2][89]。
* 自 2026 年 3 月起提供远程处理支持。

另请参阅：

* [lisp-actors](https://github.com/dbmcclain/Lisp-Actors)，“对 Common Lisp 中 Actor 模型的使用进行的持续调查，该模型已从实际应用中受益”。
* 它是 [Emotiq 区块链](https://github.com/emotiq/emotiq/blob/dev/src/test/blockchain-test.lisp) 的一部分（已停止的项目）
* 进行远程处理，包括类似于 Bordeaux-Threads 的线程抽象层库。
*！它缺乏单元测试。
* [Actors](https://github.com/aarvid/Actors) LispWorks 包（[公告](https://www.reddit.com/r/Common_Lisp/comments/77vsft/david_mcclains_actors_package_for_lispworks/)）[MIT][200]。


事件处理
----------------

* [simple-tasks](https://codeberg.org/shinmera/simple-tasks) - 一个非常简单的任务调度框架。 [zlib][33]。
* 保存失败时的返回值和任务环境，以便我们稍后检查。
* [deeds](https://codeberg.org/shinmera/deeds) - Deeds 是一个可扩展的事件传递系统。它允许通过复杂的事件过滤系统将事件有效地传递到多个处理程序。 [zlib][33]。
* [cl-flow](https://github.com/borodust/cl-flow/) - 用于非阻塞并发 Common Lisp 的数据流计算树库。 [麻省理工学院][200]。
* [event-glue](https://github.com/orthecreedence/event-glue) - 简单的事件抽象。没有依赖性。它可以在任何需要通用事件处理系统的地方使用。 [麻省理工学院][200]。
* [cl-nats](https://github.com/atgreen/cl-nats) - 用于 Common Lisp 的全功能 NATS 消息传递客户端。麻省理工学院。 *拥有法学硕士学位*。
* Pub/Sub、请求/回复、TLS 1.3、自动重新连接、集群发现、Keep-Alive、取消。


作业处理
--------------


* [SBCL 的计时器](http://www.sbcl.org/manual/#Timers)，系统范围的事件调度程序。
* [psychiq](https://github.com/fukamachi/psychiq) - 用于 Common Lisp 应用程序的基于 redis 的后台作业处理。受到 Ruby 的 Sidekiq 的启发，并与其 Web UI 兼容。 [LLGPL][8]。
* [cl-cron](https://github.com/lisp-maintainers/cl-cron) - 一个简单的工具，提供类似 cron 的功能。 [GPL3][2]。
* [clerk](https://github.com/tsikov/clerk) - 以给定的时间间隔运行常规或一次性作业。 [麻省理工学院][200]。
* 维护在 [lisp-maintainers/clerk](https://github.com/lisp-maintainers/clerk)


正则表达式和字符串解析
===============================================

* ⭐ [cl-ppcre](http://weitz.de/cl-ppcre/) - 可移植、与 Perl 兼容的正则表达式。 [FreeBSD][39]。
* [one-more-re-nightmare](https://github.com/no-defun-allowed/one-more-re-nightmare) - Common Lisp 中的快速正则表达式编译器。 [BSD_2 条款][17]。

另请参阅：

* [rexxparse](https://github.com/dtenny/rexxparse) - 受 REXX PARSE 构造启发的字符串解析工具。麻省理工学院。
* [pregexp](http://ds26gte.github.io/pregexp/index.html) - 适用于Scheme 和Common Lisp 的可移植正则表达式。

另请参见上面的 clj-re。


脚本编写
=========

运行脚本
---------------

*实现可以使用`--load`运行文件，SBCL有`--script`，
但有一个启动时间，特别是在加载库时。我们可以吗
做得更好吗？我们总是可以构建一个二进制文件。*

* [ScriptL](https://github.com/rpav/ScriptL) - Shell 脚本变得像 Lisp 一样！或者，实时编码远程函数调用 shell。在 REPL 中编写命令，然后立即在 shell 中运行它。 [LLGPL][8]。
* 类似并且可能更简单：[lserver](https://notabug.org/quasus/lserver/)
* [CIEL](https://github.com/ciel-lang/CIEL/) - CIEL 是一个扩展 Lisp，是数十个可用于日常任务（HTTP、JSON、正则表达式...）的库的集合。 [许可证不明确]
* 它还以二进制形式提供，能够从源运行脚本。使用内置库的脚本可以快速启动，无需编译步骤。
**截至 2024 年处于测试阶段*
* [kiln](https://github.com/ruricolist/kiln) - 一个基础设施（管理隐藏的多重调用二进制文件），使 Lisp 脚本高效且符合人体工程学。 [麻省理工学院][200]。
* Kiln 使得编写非常小的脚本变得实用。 Kiln 脚本快速且廉价，甚至可以向 shell 公开 Lisp 功能的一小部分。


命令行选项解析器
----------------------------

* 👍 [Clingon](https://github.com/dnaeon/clingon) - 一个丰富的命令行选项解析器系统。
* 它可能具有最丰富的功能集：子命令、bash补全的生成、支持各种选项（整数、布尔值、计数器、枚举……）、可扩展……
  * [clingon-scripter](https://git.sr.ht/~michal_atlas/clingon-scripter) - 将标志定义为简单的“defvar”声明。
* [Adopt](https://github.com/sjl/adopt/) - 一个该死的OPTion解析库。 [麻省理工学院][200]。


Readline、ncurses 和其他图形 TUI 帮助程序
-------------------------------------------------

* 🔥 [cl-tuition](https://github.com/atgreen/cl-tuition) - 用于构建丰富、响应式 TUI 的 Common Lisp 库。麻省理工学院。
* 模型-视图-更新 Elm 架构、可重用小部件（文本输入、微调器、进度条……）、鼠标支持、布局助手……
* [cl-readline](https://github.com/vindarel/cl-readline) - 一组
函数可以在输入行时对其进行编辑，以维护列表
以前输入的命令行，调用并重新编辑它们
执行类似 csh 的历史扩展。  Emacs 和 vi 编辑
模式。 [GPL3][2]。
* [cl-isocline](https://codeberg.org/digikar/cl-isocline/) - libreadline、libedit 等的替代品。
* 与流行的 GPL 许可的 libreadline 相比，它是 MIT 许可的，纯 C，可跨 Unix、Windows、MacOS 移植，支持开箱即用的多行编辑等等。
* 包含 `isocline-repl`，一个功能丰富的 Common Lisp REPL，支持：多行编辑、历史记录、语法突出显示、基本调试。
* [Linedit](https://common-lisp.net/project/linedit) - Readline风格
提供可定制行编辑的库
特点。 [麻省理工学院风格][210]。
* [cl-charms](https://github.com/HiTECNOLOGYs/cl-charms) - 一个
Common Lisp 中“libcurses”的接口。它既提供了原始的、
通过 CFFI 到 libcurses 的低级接口，以及更高级别的接口
利皮尔接口。 [麻省理工学院][200]。
* [cl-termbox2](https://github.com/garlic0x1/cl-termbox2) - [Termbox2](https://github.com/termbox/termbox2) 绑定。
*“termbox2 是一个用于创建 TUI 的终端 I/O 库。它是无处不在的 ncurses 库的精简替代品。与 ncurses 不同，它具有更严格的 API，并且如果系统上不存在 terminfo 数据库，它还内置对流行终端的支持。”
* [replic](https://github.com/vindarel/replic/) - 帮助程序将现有代码转换为 readline 应用程序，重点是定义命令参数的完成。还作为一个随时可用的可执行文件提供，它将用户的 lispy 初始化文件转换为 readline 命令。 [麻省理工学院][200]。
* [cl-ansi-term](https://github.com/vindarel/cl-ansi-term) - 打印
彩色文本、水平线、进度条、（未）排序列表
以及符合 ANSI 标准的终端上的表格。 [GPL3][2]。
* [cl-progress-bar](https://github.com/sirherrbatka/cl-progress-bar/) - 进度条，就像 Quicklisp 中一样！ [麻省理工学院][200]。
* 和 [progressons](https://github.com/vindarel/progressons)，一行进度条，用于真正的哑终端。麻省理工学院。
* [text-draw](https://codeberg.org/shinmera/text-draw) - 仅使用纯 Unicode 文本绘制图形的工具包：框、背景、复选框和单选按钮、线条、箭头、表格、树……zlib。
* [old-norse](https://github.com/nallen05/old-norse) - 具有集成事件循环的低延迟、基于网格的终端图形引擎。麻省理工学院。
* 鼠标支持，60fps 渲染，通过 SSH 或 TTYD 部署在任何地方。
* [uncursed](https://github.com/Plisp/uncursed) - 用于编写具有最小依赖性的终端接口的跨平台库。 BSD_3 条款。
* 提供了更高级别的缓冲绘图抽象和低级别实用程序。

外壳、外壳接口
-------------------------

* [shcl](https://github.com/bradleyjensen/shcl) - Common Lisp 中的类似 POSIX 的 shell。 [Apache2.0][89]。
* [unix-in-lisp](https://github.com/PuellaeMagicae/unix-in-lisp) - 将 Unix 系统挂载到 Common Lisp 镜像中。
* Unix 概念直接/浅层嵌入到 Lisp 中（Unix 命令变成 Lisp 宏，Unix 文件变成 Lisp 变量，Unix 流变成惰性 Lisp 序列，等等）。

Lisp 实用程序：

* [cmd](https://github.com/ruricolist/cmd) - 用于运行外部程序的实用程序。防止 shell 插值，在构建时考虑到多线程程序，支持 Windows。 [麻省理工学院][200]。
* `uiop:run-program`（同步）和 `uiop:launch-program`（异步）随 ASDF 一起提供，可用于所有现代实现。请参阅[CL Cookbook：运行外部程序](https://lispcookbook.github.io/cl-cookbook/os.html#running-external-programs)。
* [Clesh](https://github.com/Neronus/Clesh) - 扩展 Common Lisp 以类似于 Perl 反引号的方式嵌入 shell 代码。 [FreeBSD][39]。

另请参阅：

* [Lish](https://github.com/lisp-mirror/yew) - 有一天，“lish”可能会成为一个 Lisp shell。 [GPL3][2]。
* 支持路径和 Lisp 符号中可执行文件的制表符补全，允许编写和混合 shell 命令和 Lisp 代码，具有小型 REPL 和交互式调试器等等。
* 警告：这是旧备份。原来的存储库已经不复存在了。


系统管理
---------------------

配置工具与 Ansible、Chef 或 Puppet 没有什么不同。

* [Consfigurator](https://spwhitton.name/tech/code/consfigurator/) - Lisp 声明式配置管理系统。  您可以使用它以 root 身份配置主机、以非特权用户身份部署服务、构建和部署容器、生成光盘映像、操作文件和目录等等。 [GPL3][2]。
* apache、apt、cmd、容器、cron、磁盘、文件、firewalld、git、主机名、let-encrypt、区域设置、lxc、安装、网络、操作系统、包、定期、postgres、重新启动、服务、ssh、sshd、systemd、时区、用户...
* [cl-unix-cybernetics](https://github.com/cl-unix-cybernetics/cl-unix-cybernetics)（以前称为 Adams） - Common Lisp 中的 UNIX 系统管理。 [国际标准委员会][22]。
- 您使用具有属性的资源来描述您的系统（主机）。然后仅使用远程主机上的 /bin/sh 和控制主机上的 /usr/bin/ssh 来探测和同步属性。
- [cl-ssh](https://github.com/jmeissen/cl-ssh) - SSH v2 客户端实现。麻省理工学院。
* 核心传输、身份验证和会话执行工作。使用风险自负。
* 另请参阅：[trivial-ssh](https://github.com/eudoxia0/trivial-ssh)（*截至 2026 年的 bitrot？*）

更新可执行文件
--------------------

* [cl-selfupdate](https://github.com/atgreen/cl-selfupdate) - 通过 GitHub/GitLab 发布的 Common Lisp 可执行文件的自我更新功能。麻省理工学院。


其他脚本实用程序
-------------------------

* [clawk](https://github.com/sharplispers/clawk) - 嵌入到 Common Lisp 中的 AWK 实现，用于搜索文件中的行并对其字段执行指定的操作。 BSD 风格。
* [lqn](https://github.com/inconvergent/lqn) - 用于查询和转换 Lisp、JSON 和其他文本文件的查询语言和终端实用程序。用 Common Lisp 编写。 [麻省理工学院][200]。

此外，停滞的项目：

* [WCL](https://github.com/wadehennessey/wcl) [停滞] - 允许数百个 Lisp
应用程序立即可用，同时允许
其中几个同时运行。  WCL 通过以下方式实现这一目标
提供 Common Lisp 作为可以链接的 Unix 共享库
Lisp 和 C 代码可生成高效的应用程序。  例如，
规范“Hello World!”的 Lisp 版本的可执行文件
程序在 32 位 x86 Linux 上仅需要 20k 字节。  WCL也
支持完整的开发环境，包括动态文件
加载和调试。  GDB 的修改版本用于调试 WCL
程序，提供对混合语言调试的支持。
- 一篇[论文](https://dl.acm.org/doi/abs/10.1145/141478.141560)：“在 Unix 下交付高效的 Common Lisp 应用程序”。


文本编辑器资源
=====================

其中包含各种文本编辑器的插件和其他好东西。

* [Parinfer](https://shaunlebron.github.io/parinfer/) - Parinfer 是一种编辑 Lisp 代码的方法，有助于保持缩进和括号平衡。它很容易上手，但它提供了 Paredit 的高级功能。它可在许多编辑器上使用（Emacs、Vim、Neovim、Atom、Sublime Text、Visual Studio Code、LightTable、CodeMirror 等）。

## Emacs##

* ⭐ [Slime](https://github.com/slime/slime) - Emacs 的高级 Lisp 交互模式； Emacs 内成熟的 Common Lisp 环境。公共领域。
* [Sly](https://github.com/joaotavora/sly) - SLY 是 SLIME 的一个分支，包含多项更改和新功能，例如 Sly 贴纸。
* *没有 C-c C-y 快捷键，又名 slime-call-defun 等效项！*

入门套件：

* [Emacs4CL](https://github.com/susam/emacs4cl) - 一个小型 Emacs 初始化文件，可快速设置普通 Emacs 进行 Common Lisp 编程。附带初始化文件中每一行代码的逐行解释。
* [plain-common-lisp](https://github.com/pascalcombier/plain-common-lisp/) - 在 Windows 上获取本机 Common Lisp 环境的简单方法。
* 附带 SBCL、Quicklisp、Emacs 和 Slime。
* 带有控制台程序的示例程序，访问 Win32 API，使用 IUP 显示 GUI，运行 OpenGL 窗口。
* [cl-devel2](https://hub.docker.com/r/eshamster/cl-devel2/) - 用于 Common Lisp 开发环境的 Docker 容器。随 Slime 一起发布 SBCL、CCL、Roswell 和 Emacs 26。
* [Portacle](https://shinmera.github.io/portacle/) - 一个可移植的多平台 Common Lisp 环境：SBCL、Quicklisp、Emacs、Slime、Git。
* *温暖：Portacle 现在不再维护，并且提供了一个旧的 Emacs。*
* [IDEmacs](https://codeberg.org/IDEmacs/IDEmacs) 是让 Emacs 初学者友好的尝试。
* 它为 Common Lisp 提供了 Sly。使用 Emacs v29 或更高版本，您可以暂时尝试 IDEmacs，而不会弄乱您的 .emacs 配置，这要归功于新的“--init-directory”选项。
* [lisp-stat 的 Docker 镜像](https://lisp-stat.dev/blog/2026/03/09/getting-started/) 附带一个即用型 Emacs。

史莱姆扩展：

* 👍 [slime-star](https://github.com/mmontone/slime-star) - 预装扩展的 SLIME 配置，还有一些自定义实用程序和菜单：
- Lisp系统浏览器
  - [SLIME doc contrib](https://github.com/mmontone/slime-doc-contribs) - 增强默认帮助缓冲区。
  - [Quicklisp systems](https://github.com/mmontone/quicklisp-systems) - 从 Emacs 搜索、浏览和加载 Quicklisp 系统。
  - [史莱姆断点](https://github.com/mmontone/slime-breakpoints)
  - [Slite](https://github.com/tdrhq/slite/) - FiveAM 的测试运行程序。
  - [Quicklisp-apropos](https://github.com/mmontone/quicklisp-apropos) - 在 Quicklisp 中跨库执行“apropos”查询（对符号名称、类、文档等进行全文搜索）。
  - [slime-critic](https://github.com/mmontone/slime-critic) - Lisp 评论家温和地批评你的代码是否存在不良模式。

狡猾的扩展：

* [sly-overlay](https://git.sr.ht/~fosskers/sly-overlay) - Sly 的扩展，可以本着 CIDER (Clojure)、Eros (Emacs Lisp) 和 Lem 编辑器的精神，将 Common Lisp 评估结果直接叠加到缓冲区中。
* [sly-mrepl-db](https://gitlab.com/akashadutchie/sly-mrepl-db) - 从调试器中，使用帧上下文（而不仅仅是在迷你缓冲区中）评估 REPL 中的表达式。

工具：

- [Quicksearch](https://github.com/lisp-maintainers/quicksearch) - 在 GitHub、Quicklisp、Cliki 和 Bitbucket 上搜索项目。麻省理工学院。

## Vim 和 Neovim ##

* [SLIMV](https://github.com/kovisoft/slimv) - Vim 的高级 Lisp 交互模式； Vim 内部成熟的 Common Lisp 环境。未指定许可证。
* [Vlime](https://github.com/vlime/vlime) - VLIME：Vim 加上 Lisp 是最邪恶的。 Vim（和 Neovim）的 Common Lisp 开发环境。 [麻省理工学院][200]。
* [quicklisp.nvim](https://gitlab.com/HiPhish/quicklisp.nvim) - Neovim 的 Quicklisp 前端。
* [Slimv_box](https://github.com/justin2004/slimv_box) - Docker 容器中的 slimv。


## 日食##

* [Dandelion](https://github.com/Ragnaroek/dandelion) - Eclipse IDE 的 Common Lisp 插件。

## 莱姆##

* [Lem](https://github.com/lem-project/lem) - 可在 Common Lisp 中扩展的通用开发环境。[MIT][200]。
* ncurses 和 webview 前端。
* 内置LSP客户端。
* 为 Common Lisp 量身定制的开箱即用、类似 Emacs、基于 Slime 的编辑器。
* 网站和文档：[https://lem-project.github.io/](https://lem-project.github.io/)

* 🚀 [房间：云上的 Lem](https://www.youtube.com/watch?v=IMN7feOQOak)（视频演示）
*“Rooms 是一款在云中运行 Lem 的产品，Lem 是用 Common Lisp 创建的文本编辑器，可供多个用户使用。”
* 截至 2024 年 4 月的新内容。

## LispWorks

* [lw-plugins](https://github.com/apr3vau/lw-plugins) - 四月和五月的 LispWorks 插件。 OBSD。
* 终端集成、代码折叠、侧树、Markdown 高亮、Nerd Fonts、模糊匹配、增强目录模式、扩展区域、配对编辑、SVG 渲染……
* [lw-rich-text](https://codeberg.org/fourier/lw-rich-text/) - LispWorks 窗格支持类似 HTML 的标记。

## Mine - 适用于 Common Lisp 和 Coalton 的单次下载初学者友好 IDE

* [mine](https://coalton-lang.github.io/mine/) - 适用于 Windows、macOS 和 Linux 的 Coalton 和 Common Lisp 集成开发环境。

## 原子、脉冲星##

* [SLIMA](https://github.com/neil-lindquist/slima) 允许您
交互式地开发 Common Lisp 代码，将 Atom（或现在的 Pulsar）变成
Lisp IDE 非常好，并且正在积极开发。 [麻省理工学院][200]。
- *注意：在撰写本文时，SLIMA 有点落后于 Slime 和 Swank 的最新变化。它适用于我们的 [Slime 2.27](https://github.com/slime/slime/releases/tag/v2.27)。在 SBCL 2.5.8 和 SBCL 2.1.11.debian 上测试。*

## 崇高的文字##

* [Sublime Text](http://www.sublimetext.com/3)（专有）有
Common Lisp 支持及其 SublimeREPL 和
[Slyblime](https://github.com/s-clerc/slyblime) 软件包。斯莱布利姆
是 SLY 的实现，它使用相同的后端 (SLYNK)。它
提供高级功能，包括带有堆栈框架的调试器
检查。

## VSCode##

* 自 2026 年 5 月起新增 · [OLIVE](https://github.com/kchanqvq/olive/) - VSCode 的 Common Lisp 扩展，带有 REPL、调试器、转到定义、宏步进器。基于斯万克。
  * [宣布与Alive的区别](https://old.reddit.com/r/lisp/comments/1tn3zff/new_cl_vscode_extension_olive/)
* [alive](https://github.com/nobody-famous/alive) - VSCode 的 Common Lisp 扩展。公共领域。
* 并非基于 Slime/Swank。
*参见Cookbook：[将VSCode与Alive结合使用](https://lispcookbook.github.io/cl-cookbook/vscode-alive.html)
* [commonlisp-vscode](https://marketplace.visualstudio.com/items?itemName=ailisp.commonlisp-vscode) - 支持语法突出显示、自动完成、悬停文档、转到定义、编译和加载文件、REPL 的扩展。它是[在 GitHub 上](https://github.com/ailisp/commonlisp-vscode/)。
* [strict-paredit-vscode](https://marketplace.visualstudio.com/items?itemName=ailisp.strict-paredit) - 像 Emacs 一样进行结构编辑和导航。

## 捷脑公司

* [SLT](https://github.com/Enerccio/SLT) - Intellij/Jetbrains IDE 系列的 IDE 插件，通过 SBCL 和 Slime/Swank 实现对 Common Lisp 的支持。
- 2023 年 1 月发布。实验性。
- 请参阅[此分支](https://github.com/ivanbulanov/SLT/releases)，该分支已更新以在 Intellij 2025.3.2 上工作。

## Geany（实验）##

* [Geany-lisp](https://github.com/jasom/geany-lisp) 是 [Geany](https://geany.org/) 编辑器的实验性 Lisp 模式。

## 笔记本##

* [common-lisp-jupyter](https://github.com/yitzchak/common-lisp-jupyter) - Jupyter 的 Common Lisp 内核以及用于构建 Jupyter 内核的库，基于 Robert Dodier 的 Maxima-Jupyter，而该库基于 Frederic Peschanski 的 cl-jupyter。 [麻省理工学院][200]。
  * [Cytoscape widget](https://github.com/yitzchak/cytoscape-clj) - common-lisp-jupyter 的 Cytoscape.js 小部件。
  * [Kekule widget](https://github.com/yitzchak/kekule-clj) - common-lisp-jupyter 的 Kekule.js 小部件。
  * [ngl widget](https://github.com/yitzchak/ngl-clj) - 用于 common-lisp-jupyter 的 ngl 小部件（蛋白质查看器）。
  * [sheet widget](https://github.com/yitzchak/sheet-clj) - common-lisp-jupyter 的数据网格小部件。
* [cl-jupyter](https://github.com/fredokun/cl-jupyter) - 适用于 Jupyter 笔记本的 Common Lisp 内核 [自定义许可证](https://github.com/fredokun/cl-jupyter/blob/master/LICENSE)。

## REPL ##

* [icl](https://github.com/atgreen/icl) - 终端的增强 REPL。麻省理工学院。
* 基于Slynk：与Slime共享许多功能。
* 交互式检查器
* 实验性的 `,explain` 命令启动 Gemini 或 Claude CLI。
* [cl-repl](https://github.com/lisp-maintainers/cl-repl) - 类似 ipython 的 REPL。具有补全、shell 命令、magic 命令、调试器等[GPL3][2]。
* 二进制版本：只需下载二进制文件（Ubuntu、OSX、Windows）并运行即可。
* [颜色主题](https://github.com/koji-kojiro/lem-pygments-colorthemes)。
* 与 icl 相比：有一个交互式调试器，有一个 `!` shell 快捷方式，有一个 `%edit` 命令，有经典的基于 readline 的自动完成（icl 有一个下拉菜单），不基于 Slynk，无法连接到正在运行的 Lisp 图像。
* [cl-isocline](https://codeberg.org/digikar/cl-isocline/) - 包含“isocline-repl”，一个功能丰富的 Common Lisp REPL，支持：多行编辑、历史记录、语法突出显示、基本调试。
* [magic-ed](https://github.com/sanel/magic-ed) - 一个小型编辑工具，您可以在其中直接加载、编辑、操作和评估来自 REPL 的文件或文件内容，而使用完整的 IDE 实在是太麻烦了。 [麻省理工学院][200]。

<!-- See also: -->

<!-- * [cl-web-editor](https://git.sr.ht/~hajovonta/cl-web-editor) - a simple in-browser editor that does on-the-fly form validation and instant REPL results. MIT. -->

## 在线编辑##

* [Judge0 IDE](https://ide.judge0.com/?lUpj) 是一个支持 Common Lisp (SBCL) 的在线编辑器。 [麻省理工学院][200]。
* [Riju](https://riju.codes/commonlisp)，一个“适合每种编程语言的快速在线游乐场”，支持 Common Lisp (SBCL)。


文本和二进制解析器
============================

* ⭐ [esrap](https://github.com/scymtym/esrap) - 解析语法、Packrat 解析器、TDPL 功能等等。 [外籍人士][14]。
* [parseq](https://github.com/mrossini-ethz/parseq) - 使用解析表达式语法 (PEG) 解析字符串和列表等序列的库。受到 Esrap 的启发。 GPL2。
* [uclp](https://github.com/ravi-delia/uclp) - Common Lisp 中解析表达式语法（PEG，la Janet）的实验性实现。麻省理工学院。
* [alexa](https://github.com/quil-lang/alexa) - 词法分析器生成器。 [BSD_3 条款][15]。
- ALEXA是一个类似于lex或flex的工具，用于生成词法分析器。然而，与 lex 等工具不同的是，ALEXA 在您的 Lisp 程序中定义了特定于域的语言，因此您不需要调用单独的工具。
* [cl-yacc](https://github.com/jech/cl-yacc) - LALR(1) 解析器生成器。 [麻省理工学院][200]。
* [cl-shlex](https://github.com/ruricolist/cl-shlex/) - 用于类似 shell 语法的简单词法分析器。 [麻省理工学院][200]。
* [smug](https://github.com/drewc/smug) - Common Lisp 的解析器组合器。 SMUG 可以轻松创建快速可扩展的递归下降解析器，而无需时髦的语法或难以理解的宏观学。 [麻省理工学院][200]。
* [MaxPC](https://github.com/eugeneia/maxpc) - 一个简单实用的库，用于编写基于组合解析的解析器和词法分析器。
* MaxPC能够解析确定性、上下文无关的语言，为解析树转换和错误处理提供强大的工具，并且可以对序列和流进行操作。
* 优秀的文档。
* [parcom](https://github.com/fosskers/parcom) - Common Lisp 的简单解析器组合器，采用 Haskell 的“parsec”和 Rust 的“nom”风格。 [MPL-2.0][211]。

另请参阅：

* [lisp-binary](https://github.com/j3pic/lisp-binary) - 一个可以轻松读取和写入复杂二进制格式的库。 [GPL3][2]。
* [texp](https://github.com/eugeneia/texp/) - 用于生成 TeX 的 DSL。 [AGPL-3.0][agpl3]。

文本处理
===============

* [montezuma](https://github.com/sharplispers/montezuma/) - Common Lisp 的全文索引和搜索。 [外籍人士][14]。
* [mk-string-metrics](https://github.com/cbaggers/mk-string-metrics) - 
在 Common Lisp 中高效计算各种字符串指标
（Damerau-Levenshtein、Hamming、Jaro、Jaro-Winkler、Levenshtein、
等）。 [麻省理工学院][200]。
* [wiki-lang-detect](https://github.com/vseloved/wiki-lang-detect) - 
使用维基百科数据进行文本语言识别。未指定许可证。
* [cl-phonetic](https://github.com/bgutter/cl-phonetic) - Common Lisp 的语音模式匹配库（旨在替换 Python 的 Sylvia 库）。 [麻省理工学院][200]。
* [cl-string-generator](https://github.com/pokepay/cl-string-generator) - 从正则表达式生成字符串。 [麻省理工学院][200]。
* [trivial-sanitize](https://codeberg.org/cage/trivial-sanitize) - 干净的 html 字符串：`"<a>foo</a>"` → `"foo"`。 [LLGPL][8]。

另请参阅：

* [Resolve](https://github.com/GrammaTech/resolve) - 一款用于基于 AST 的差异计算、显示和自动解析的软件。您会发现用 C++ 和 CL 编写的 Lisp 实用程序。

工具
=====

这些应用程序或代码片段使 Common Lisp 中的开发变得更加容易，而它们本身并不是 Common Lisp 库。

* [quicksearch](https://github.com/tkych/quicksearch) - 从 REPL 查找在线图书馆。 [外籍人士][14]。
* [lake](https://github.com/takagi/lake) - 类似于构建实用程序的 GNU make。 [麻省理工学院][200]。


单元测试
============

* ⭐ [FiveAM](https://github.com/sionescu/ Fiveam) - 简单的回归测试框架。 [FreeBSD][39]。
  * [FiveAM 文档](https://fiveam.common-lisp.dev/docs/index.html)
  * [fiveam-matchers](https://github.com/tdrhq/fiveam-matchers/) - Fiveam 的可扩展、可组合的匹配器库。 [Apache2.0][89]。
* [Parachute](https://codeberg.org/shinmera/parachute) - 可扩展且交叉兼容的测试框架。具有测试依赖性、条件、固定装置和重新启动。 [zlib][33]。
* [CLUnit2](https://codeberg.org/cage/clunit2/) - 一个单元测试库。 [麻省理工学院][200]。
* [Mockingbird](https://github.com/Chream/mockingbird) - 一个小
Common Lisp 的存根和模拟库。还可以检查是否
一个存根函数被调用了多少次以及调用的次数
论据。 [麻省理工学院][200]。
* [cl-mock](https://github.com/Ferada/cl-mock) - 另一个模拟库。它比 Mockingbird 有更多的功能，比如模拟调用的模式匹配等。
* [Check-it](https://github.com/DalekBaldwin/check-it) - QuickCheck 风格的基于属性的随机测试。 [LLGPL][8]。
* [cl-coveralls](https://github.com/fukamachi/cl-coveralls) - 一个帮手
库将测试覆盖率发布到 Coveralls。请参阅[SBCL 的代码覆盖率工具](http://www.sbcl.org/manual/index.html#sb_002dcover)。 [FreeBSD][39]。
* [CheckL](https://github.com/rpav/CheckL/) - 为什么用 Common Lisp 编写程序，却像 Java 那样编写测试？来认识一下CheckL吧！
* 一个测试库，用于对照前一个测试值检查当前测试值并提供重新启动。
* [Try](https://github.com/melisgl/try) - Try 是一个可扩展的测试反框架，对交互式和非交互式工作流程以及 Emacs 集成提供同等支持。 [麻省理工学院][200]。

另请参阅：

* [testiere](https://cicadas.surf/cgit/colin/testiere.git/about/) - 一个测试实用程序，其中测试包含在“defun/t”表单的顶部。当您以交互方式重新编译函数时，它们就会运行。具有模拟和存根支持。 [GPL3][2]。
* [testiere-mode](https://github.com/dotemacs/testiere-mode.el) 用于 Emacs，隐藏和显示 `#+testiere` 部分。
* [cl-hamcrest](https://github.com/40ants/cl-hamcrest) - 一组 [Hamcrest](https://hamcrest.org/) 匹配器，可以组合起来创建灵活的意图表达。通过使用“has-plist-entries”、“has-slots”、“has-length”、“contains”、“contains-in-any-order”、“has-all”等断言，帮助提高单元测试的可读性……[BSD_3Clause][15]。

编辑器实用程序：

* [Slite](https://github.com/tdrhq/slite/) - 用于 FiveAM 测试的基于 SLIme 的 TEst 运行程序。 [Apache2.0][89]
- Slite 以交互方式运行您的 Common Lisp 测试（在撰写本文时仅支持 FiveAM）。它允许您查看测试失败的摘要、跳转到测试定义、使用调试器重新运行测试，所有这些都可以在 Emacs 内部进行。

CI 实用程序：

* [CI-utils](https://github.com/neil-lindquist/CI-Utils)（低活动）- 一组用于在持续集成平台上工作的实用程序和示例，包括 Fiveam 测试库的运行脚本。
* 帮助使用正确的退出代码运行 Fiveam 测试。
* 与罗斯威尔集成。

有关更多信息：[Sabra Crolleton 的广泛测试框架比较](https://sabracrolleton.github.io/testing-framework)。


公用事业
=========

缓存（序列化）
-----------------------

* [cl-store](https://github.com/skypher/cl-store) - 一个便携式序列化包，使您能够将所有 common-lisp 数据类型存储到流中。麻省理工学院。
* 调用 `store object "file.bin")` 将一个（可能是复合的）lisp 对象存储到磁盘，并调用 `restore` 将其取回。
* [clache](https://github.com/html/clache) - 通用缓存设施。在磁盘或内存中缓存任何 Lisp 对象。  [LLGPL][8]。
* 建立在 cl-store 之上
* 缓存可以是持久的或者有过期时间。
* 也暴露了商店位置。
* [conspack](https://github.com/conspack/cl-conspack) - 二进制序列化。
* [cl-naive-store](https://gitlab.com/naive-x/cl-naive-store) - Common Lisp 的一个简单的持久性内存（延迟加载）索引文档存储。 [麻省理工学院][200]。
- 请参阅[介绍性博客文章](https://zaries.wordpress.com/2022/05/31/cl-naive-store/)
- 我们敢添加：由作者公司（ASTN Group，请参阅 [awesome-lisp-companies](https://github.com/azzamsa/awesome-lisp-companies/)）在生产中使用
* 🚀 [cl-binary-store](https://github.com/ajberkley/cl-binary-store) - 快速 Common Lisp 二进制序列化器/反序列化器。 BSD_3 条款。请参阅 [reddit 公告](https://www.reddit.com/r/Common_Lisp/comments/1hz5879/new_binary_serializationdeserialization_library/) (2025)。
*“超快速且可定制的 Common Lisp 对象序列化器/反序列化器，与非常紧凑的二进制格式之间的转换。支持对象相等、循环引用和完整的 Common Lisp 类型系统。专用数组（在 SBCL 上）以闪电般的速度存储/恢复。”

另请参阅[持久对象数据库](#persistent-object-databases) 部分。


缓存（记忆）
-----------------------

* [function-cache](https://github.com/AccelerationNet/function-cache) - 一个 Common Lisp 函数缓存/记忆库。 [BSD][15]。


压缩/减压
---------------------------

* [chipz](https://github.com/froydnj/chipz) - 一个解压库。 [3 条款 BSD][15]。
* [Salza2](http://www.xach.com/lisp/salza2/) - 用于创建压缩数据的库。 [FreeBSD][39]。
* [zippy](https://codeberg.org/shinmera/zippy) - 基于3bz的ZIP存档格式库。 [zlib][33]。
* [archive](https://github.com/froydnj/archive) - 用于读取和创建存档（tar、cpio）文件的库。 [BSD_3 条款][15]。 “tar”程序的纯 Common Lisp 替代品。
* 请参阅其最近的分支 [cl-tar](https://common-lisp.net/project/cl-tar/) (2021)。 [公告](https://www.timmons.dev/posts/new-project-cl-tar.html)。
* [deoxybyte-gzip](https://github.com/keithj/deoxybyte-gzip) - Common Lisp 通过 CFFI 与 zlib 接口。 GPL3。
* 该系统提供 gzip 和gunzip 函数以及 Gray-streams 实现，两者都构建在一组较低级别的 zlib 函数上。


配置
-------------

* 👍 [py-configparser](https://common-lisp.net/project/py-configparser/) - 读取和写入 Python 的类似 ConfigParser 的配置文件。 [麻省理工学院][200]。
* [envy](https://github.com/fukamachi/envy) - 配置切换器。 [FreeBSD][39]。
* [chameleon](https://github.com/sheepduke/chameleon/) - 附带配置文件支持的配置管理库。 [麻省理工学院][200]。

日期和时间
-------------

* ⭐ [local-time](https://codeberg.org/dlowe/local-time) - 以半标准方式操作日期和时间信息的开发库。 [3 条款 BSD][15]。
* [本地时间文档](https://local-time.common-lisp.dev/)，[github镜像](https://github.com/dlowe-net/local-time)。
* [fuzzy-dates](https://codeberg.org/shinmera/fuzzy-dates) - 模糊解析日期和时间字符串的库。兹利布。
* [cl-date-time-parser](https://github.com/tkych/cl-date-time-parser) - 自由地解析日期时间字符串。隐藏日期-时间格式之间的差异，并能够将日期和时间作为一种日期-时间格式进行管理。 [麻省理工学院][200]。
* [chronicity](https://github.com/chaitanyagupta/chronicity) - 自然语言日期和时间解析，用于解析“3 天后”等字符串。 [BSD_3 条款][15]。
* [local-time-duration](https://github.com/enaeher/local-time-duration) - 
建立在本地时间之上的持续时间处理库。 [麻省理工学院][200]。
* 请参阅此分支：[ humanize-duration ](https://github.com/40ants/ humanize-duration)，它仅输出持续时间对象的重要部分。有本地化支持。
* [iso-8601-date](https://gitlab.com/DataLinkDroid/iso-8601-date) - Common Lisp 中的各种日期例程基于 ISO 8601 字符串表示形式。 [LLGPL][8]。
* [calendar-times](https://github.com/copyleft/calendar-times) - 在 LOCAL-TIME 库之上实现的日历时间库。它具有分区日历时间和计算功能。
* 另请参阅：[calendar-date](https://github.com/takagi/calendar-date) - 公历日期库。 [麻省理工学院][200]。
* [periods](https://github.com/jwiegley/periods) - 在更高级别上操作日期/时间对象。具有系列兼容的数据结构。 [BSD_3 条款][15]。
* 带有[一些文档](https://lisp-maintainers.github.io/periods/)
* [stopclock](https://github.com/Gleefre/stopclock) - 使用（停止）时钟测量时间的库。它允许您创建时钟、暂停它、恢复它并改变它的速度。 [Apache2.0][89]。

另请参阅《日历计算》一书(https://www.cambridge.org/us/academic/subjects/computer-science/computing-general-interest/calendrical-calculations-ultimate-edition-4th-edition?format=HB#resources)，作者：Edward M. Reingold、Nachum Dershowitz，剑桥出版社。它提供 Lisp 源代码。

数据验证
---------------

* [clavier](https://github.com/mmontone/clavier) - Common Lisp 的通用验证库。 [麻省理工学院][200]。
* [ratify](https://codeberg.org/shinmera/ratify) - 用于批准、验证和解析输入的实用程序集合。 [zlib][33]。
* [json-schema](https://github.com/fisxoj/json-schema) - 用于根据 [JSON 架构](https://json-schema.org/) 标准草案 4、6、7 和 2019-09 的架构验证数据的库。 [LLGPL][8]。
* [sanity-clause](https://github.com/fisxoj/sanity-clause) - Common Lisp 的数据序列化/契约库。模式可以是属性列表或基于类，允许在“make-instance”期间检查槽的类型。 [LLGPL][8]。
* [cl-semver](https://github.com/cldm/cl-semver) - [语义版本控制](https://semver.org) 规范的实施。 [麻省理工学院][200]

开发者实用程序
-------------------

Common Lisp 实现有大量的调试工具。请参阅：[Cookbook / 调试](https://lispcookbook.github.io/cl-cookbook/debugging.html)。这些是额外的实用程序。


* [repl-utilities](https://github.com/m-n/repl-utilities) - 轻松
REPL 的常见任务（打印文档、打印外部符号、
加载包时调用挂钩，...）。 [BSD_2 条款][17]。
* [flight-recorder](https://github.com/vseloved/flight-recorder) - 强大的 REPL 历史记录工具。
* [tracer](https://github.com/TeMPOraL/tracer) - Common Lisp 的跟踪分析器，其输出适合在 Chrome/Chromium 的跟踪查看器中显示。 [麻省理工学院][200]。
* [cl-flamegraph](https://github.com/40ants/cl-flamegraph) - SBCL 统计分析器的包装器，用于为 Common Lisp 程序生成 FlameGraph 图表。 [BSD][15]。
* [supertrace](https://github.com/fukamachi/supertrace) - 用于调试/分析的高级 Common Lisp“跟踪”功能。一次跟踪多个函数，使用 before 和 after 钩子。 [BSD_2 条款][17]。
* [printv](https://github.com/danlentz/printv) - 包含电池的跟踪和调试日志宏。 [阿帕奇2][89]。
* [journal](https://github.com/melisgl/journal) - 用于日志记录、跟踪、记录和重放测试以及持久性的库。麻省理工学院。
* [brake](https://github.com/varjagg/brake) - Common Lisp 的扩展断点工具。 [麻省理工学院][200]。
* [cl-codegraph](https://sr.ht/~hajovonta/cl-codegraph/) - 通过实时图像自省的 Common Lisp 代码的自动知识图。
* 给定一个加载到 SBCL 镜像中的包，构建并维护一个
其符号图、类层次结构、方法
专业化、调用关系和元数据——所有这些都没有
解析源代码。包括实时 Emacs 集成，显示
导航时的代码智能和基于 Web 的图形查看器。

还有：

* [GTFL](http://www.martin-loetzsch.de/gtfl/) - Lisp 的图形终端，适用于想要调试或可视化自己的算法的 Lisp 程序员。浏览器中的图形跟踪。 BSD 风格。
* [trivial-benchmark](https://codeberg.org/shinmera/trivial-benchmark) - 小型基准测试库。 [zlib][33]。
* 类似的宏（`benchmark`）是 [trivial-time](https://github.com/aartaka/trivial-time) 的一部分，为更多实现（ABCL、Allegro、CCL、CLISP、ECL）提供支持。
* 事实上，大多数 trivial-benchmark 的指标仅在 SBCL 上实现。在其他实现中，它测量实际时间和用户空间时间（而不是分配的字节（ECL 的情况）、系统运行时间或 GC 运行时间）。
* [glyphs](https://github.com/ahungry/glyphs/) - 一个用于减少 Common Lisp 某些地方的冗长性的库。 [GNU GPL3][2]。
* [Lisp REPL core dumper](https://gitlab.com/ambrevar/lisp-repl-core-dumper/) - 
一个可移植的包装器，可按需生成 Lisp 核心，从而快速启动 REPL。
它可以预加载提供的系统，以帮助构建专门的集合
Lisp 核心。


文档构建者
----------------------

* [Staple](https://codeberg.org/shinmera/staple) - 使用 HTML 模板生成文档页面的工具。使用现有的 README，添加文档字符串、交叉引用和 CLHS 链接。 [zlib][33]。
* [mgl-pax](https://github.com/melisgl/mgl-pax) - 探索性
编程环境和文档生成器。一个可能
实现与文学编程类似的效果，但是
文档是从代码生成的，反之亦然。代码是第一位的，
代码必须看起来漂亮，文档就是代码。 [麻省理工学院][200]。
- 还可以导出 PDF
- 请参阅此 [40ants/doc](https://github.com/40ants/doc) 分支：更轻的核心系统、JavaScript 搜索索引、多种格式输出、HTML 主题、用于更新日志的 RSS 和 Atom 提要等等。
* [sphinxcontrib-cldomain](https://sphinxcontrib-cldomain.russellsim.org/) - 
扩展 Sphinx 以覆盖 Common Lisp。构建文档
就像 Python 项目中的 sphinx 一样简单。 [GPL3][2]
- 交叉引用、CLHS 链接、符号索引、搜索和所有 Sphinx 功能。
* [Codex](https://github.com/CommonDoc/codex) - 一个漂亮的 Common Lisp 文档系统。 [麻省理工学院][200]。
* [QBook](https://github.com/mmontone/qbook) - 生成 Common Lisp 源文件的 HTML（或 LaTeX）格式的代码列表。 [BSD_3 条款][15]。
- 所有以 4 `;`（“;;;;”）开头的注释都被解释为文档。使用标题和指令增强文档。
- QBook 充当“一个轻量级的文学编程系统，其中 Lisp 代码不是内联呈现的，而是在单独的部分中呈现，这使得文档更易于浏览。” @mmontone
* [Declt](https://github.com/didierverna/declt) - Common Lisp 库的参考手册生成器。构建可进一步处理为各种格式（例如 HTML 或 PDF）的 texinfo 文档。 BSD。
* [cl-bibtex](https://github.com/mkoeppe/cl-bibtex) - Common Lisp 中 BibTeX 程序的兼容重新实现，带有 BST-to-CL 编译器。 [GNU LGPL2.1][11]。
* [adp](https://github.com/HectareaGalbis/adp) - 使用 Scribble 文件的 Common Lisp 文档生成器。 [麻省理工学院][200]。
* 🟢 [2025 年新增] [HyperDoc](https://hyperdoc.khinsen.net/) - 将代码、数据和计算结果与解释性文本以及软件文档相结合的科学出版物，软件文档是软件系统的组成部分，而不是一堆保留在软件系统之外的文档。


包含更多文档生成器的概述博客文章：https://lisp-journey.gitlab.io/blog/overview-of-documentation-generators/ 以及包含评论和演示的专用网站：https://cl-doc-systems.github.io/

您可能还喜欢：[文学编程系统](#literate-programming)。

文档查找
--------------------

`apropos` 和 `ppcre:regex-apropos` 在函数名称中搜索。

* [docbrowser](https://github.com/lokedhs/docbrowser) - 为加载的系统动态生成文档的服务器。
- 它的主页显示了 Lisp 镜像中所有已加载系统的列表。单击一个系统，您会看到一个包含三个窗格的页面：函数、类和变量。单击某个函数可在上下文中查看其源代码以及行号。单击类可查看其插槽和专门功能。
* [cl-livedocs](https://github.com/mmontone/cl-livedocs) - 类似的和更新的，基于 Webinfo。
* 默认情况下启用全文搜索。
* [cl-docsearch](https://github.com/digikar99/cl-docsearch) - 一个在当前 Lisp 图像中搜索 Lisp 符号文档的工具。
* 也索引和搜索文档字符串。
* [docsearch-ollama](https://github.com/digikar99/cl-docsearch/blob/main/README-docsearch-ollama.md) 通过 Ollama 提供 Common Lisp 文档搜索功能。它计算并缓存与符号文档相对应的嵌入，并通过比较查询嵌入与符号文档嵌入的余弦相似度来查找用户查询。
* 我们可以做类似的事情：`(查询“如何删除字符串末尾的空格？”)`

mgl-pax（见上文）还有一个实时文档浏览器。 [文档](https://melisgl.github.io/mgl-pax-world/mgl-pax-manual.html#MGL-PAX:@BROWSING-LIVE-DOCUMENTATION%20MGL-PAX:SECTION) 和 [演示视频](https://www.youtube.com/watch?v=4bl8PS8OW94&list=PLxbqYr4DvjX68AEdLky4IiHG69VJu6f5s)。


文件和目录
---------------------

* ⭐ [uiop](https://common-lisp.net/project/asdf/uiop.html) 及其 `pathname` 包
（取代 [cl-fad](http://weitz.de/cl-fad/)）。 uiop 是 ASDF3 的一部分
因此在许多实现中都是如此。 [麻省理工学院][200]。
* [pathname-utils](https://codeberg.org/shinmera/pathname-utils) - 帮助进行路径名操作的实用程序集合。 [zlib][33]。
  * [filesystem-utils](https://codeberg.org/shinmera/filesystem-utils) - 处理文件系统的常见问题，例如列出文件、探测文件类型、确定默认目录等。
* 无依赖关系，不访问文件系统。
  * [file-attributes](https://codeberg.org/shinmera/file-attributes) - 访问公共文件属性（uid、gid、权限、ctime、mtime、atime）。
* [filepaths](https://github.com/fosskers/filepaths) - Common Lisp 的现代且一致的文件路径操作。 [LGPL3][9]。
* 无依赖关系，不访问文件系统。
* [file-finder](https://github.com/lisp-maintainers/file-finder/) - 文件对象查找器 Common Lisp 库。实现快速文件搜索、检查和操作。 [GPL3][2]。
* [osicat](https://common-lisp.net/project/osicat/) - 类 POSIX 系统上的轻量级操作系统接口，包括 Windows（目录迭代和删除、文件权限、文件类型识别等）[Expat][14]。
* 注意：Osicat 不是一个纯 Lisp 库，它依赖于编译 C 代码，这可能会使您的部署更加困难。
* [ppath](https://codeberg.org/fourier/ppath) - Common Lisp 对 Python os.path 模块的实现。 [BSD][15]。
* [mmap](https://codeberg.org/shinmera/mmap) - 便携式 mmap 文件内存映射实用程序库。 [zlib][33]。
* [nfiles](https://github.com/atlas-engineer/nfiles) - 文件持久性、监视、数据同步、（每个用户配置文件）路径解析和结构化数据检索。具有用于配置文件、远程获取文件、数据文件、Lisp 可读文件等的预定义类。 [BSD][15]。
* [trivial-glob](https://github.com/fukamachi/trivial-glob) - Common Lisp 的 Shell 风格的全局模式匹配和文件系统全局匹配。麻省理工学院。
* `(glob "**/*.lisp")`

文件查看库：

* [file-notify](https://codeberg.org/shinmera/file-notify) - 用于文件更改检测的跨平台库。 [zlib][33]。

git
---

* [cl-git](https://cl-git.russellsim.org/) - libgit2 库的 CFFI 接口。 [LGPL3][9]。
* [legit](https://shinmera.github.io/legit/) - Git 二进制文件的接口。 [zlib][33]。
* [git-api](https://codeberg.org/fourier/git-api) - 用于访问 git 存储库的 Common Lisp 库。它不需要安装 git 或 libgit。 [BSD][15]。

另请参阅 [Lem 编辑器的 Git 界面](https://lem-project.github.io/usage/usage/#version-control-with-lemlegit-git-experimental)！

国际化
----

* [cl-i18n](https://codeberg.org/cage/cl-i18n) - 一个 i18n 库。从 GNU gettext 文本或二进制文件或其本机格式加载翻译。复数形式的本地化助手。 [LLGPL][8]。
* [gettext](https://github.com/rotatef/gettext) - gettext 运行时到 Common Lisp 的端口。 [GPL3][2]。
* [fluent](https://github.com/fosskers/fluent) - 现代本地化系统 [Fluent](https://github.com/project Fluent/fluent/) 的实现。 MPL-2.0。

另请参阅：

* [translate](https://github.com/dkochmanski/translate) - 无缝语言本地化。 LLGPL。
* [enchant](https://github.com/tlikonen/cl-enchant) - Enchant 拼写检查器库的绑定。公共领域。
* [oxenfurt](https://codeberg.org/shinmera/oxenfurt) - 牛津词典 API 的客户端库。 [zlib][33]。
* [language-codes](https://shinmera.github.io/language-codes) - ISO 语言代码数据库。 [zlib][33]
* [system-locale](https://shinmera.github.io/system-locale) - 用于检索用户首选语言的库，以便您的应用程序可以选择合理的默认值。 [zlib][33]。
* [multilang-documentation](https://shinmera.github.io/multilang-documentation) - 允许用多种语言编写文档字符串，以实现真正的国际文档库。 [zlib][33]。

Linting、代码格式化
------------------------

* [sblint](https://github.com/fukamachi/sblint) - 使用 SBCL 的 Common Lisp 源代码的 linter，适用于 Reviewdog（[幻灯片](http://www.slideshare.net/fukamachi/sblint)）。 [BSD_2 条款][17]。
* [mallet](https://github.com/fukamachi/mallet) - 一个明智的 Common Lisp linter 可以捕获真正的错误，而不是风格。麻省理工学院。
* [ocicl](https://github.com/ocicl/ocicl/) 的内置 linter 和自动修复功能。
* [trivial-formatter](https://github.com/hyotang666/trivial-formatter) - Common Lisp 的代码格式化程序。 [麻省理工学院][200]。

还有：

* [lisp-format](https://github.com/eschulte/lisp-format) 和 [cl-indentify](https://github.com/yitzchak/cl-indentify)。

识字编程
--------------------

* [literate-lisp](https://github.com/jingtaozf/literate-lisp) - 从 Emacs 的 Org 文件加载 Common Lisp 代码块。 [麻省理工学院][200]。
* [erudite](https://github.com/mmontone/erudite) - 文字编程系统以交互式开发为理念而构建。 [麻省理工学院][200]。
* [papyrus](https://github.com/tani/papyrus) - Papyrus 使用 Common Lisp 的 reader 宏使你的 markdown 可执行。[MIT][200]


记录
-------

* ⭐ [log4cl](https://github.com/sharplispers/log4cl/) - 模仿 Log4J 的日志框架。 [Apache2.0][89]。与 Slime 的高级集成。
  * [log4cl-json](https://github.com/40ants/log4cl-json) - JSON 附加器扩展。 [BSD][15]。
* [verbose](https://shinmera.github.io/verbose) - 快速且高度可配置的日志记录框架。 [zlib][33]。
* [a-cl-logger](https://github.com/AccelerationNet/a-cl-logger) - 日志库提供上下文敏感的日志记录，而不仅仅是字符串到本地文件或输出流。具有logstash支持、json支持、记录器层次结构、上下文敏感日志记录、打印为可检查演示文稿的对象……

致第三方：

* [cl-fluent-logger](https://github.com/fukamachi/cl-fluent-logger) - [Fluentd](https://www.fluentd.org/) 的 Common Lisp 结构化记录器。

另请参阅：[日志记录库的广泛比较](https://sabracrolleton.github.io/logging-comparison)。

宏助手
-------------

* [easy-macros](https://github.com/tdrhq/easy-macros/) - 编写 90% 宏的简单方法。 [Apache2.0][89]。
* [trivial-with-current-source-from](https://github.com/scymtym/trivial-with-current-source-form/) - 帮助宏编写者为宏用户产生更好的错误。 [GPL3][2]。

降价
--------

* [3bmd](https://github.com/3b/3bmd) - 一个 markdown -> html 转换器。 [麻省理工学院][200]。

包裹声明
-------------------------

* [cl-reexport](https://github.com/takagi/cl-reexport) - 当您想要一次导入和重新导出许多符号以及`:include`或`:exclude`一些符号时。

另请参阅 [uiop:define-package](https://common-lisp.net/project/asdf/uiop.html#UIOP_002fPACKAGE) 及其 `:reexport` 子句（不包括/排除）、`:recycle`、`mix`…

PDF
---

* [cl-typesetting](https://github.com/mbattyani/cl-typesetting) 和 [cl-pdf](https://github.com/mbattyani/cl-pdf) - 用于生成 PDF 文件的跨平台 Common Lisp 库。 [FreeBSD][39]。
* [cl-pslib](https://codeberg.org/cage/cl-pslib) - 用于生成 PostScript 文件的 [pslib](http://pslib.sourceforge.net/) 库的（薄）包装器。还有[cl-pslib-barcode](https://codeberg.org/cage/cl-pslib-barcode)。 [LLGPL][8]。

项目骨架
-----------------

* [cl-project](https://github.com/fukamachi/cl-project) - 一般现代项目骨架。 [LLGPL][8]。
* [cl-project-with-docs](https://github.com/40ants/cl-project-with-docs) - 使用 Sphinx 和重构文本来呈现漂亮且可读的 HTML 文档。 [BSD][15]。
* [cl-cookieproject](https://github.com/vindarel/cl-cookieproject) - 生成一个随时可用的 Common Lisp 项目。不在 Quicklisp 中。 [BSD_3 条款][15]。
* 测试定义、从源运行的入口点、构建二进制文件、Roswell 集成……
* [cookiecutter-lisp-game](https://github.com/lockie/cookiecutter-lisp-game) - 用于 Common Lisp 视频游戏项目的固执己见的 cookiecutter 模板。允许在 liballegro、raylib 和 SDL2 之间选择[后端中间件库](#graphics)。包含使用 [docker-lisp-gamedev](#docker-images) 自动构建适用于 Windows、MacOS 和 Linux 的二进制文件的 CI 脚本。

安全性
--------

* [cl-isolated](https://github.com/kanru/cl-isolated) - Common Lisp 代码评估的受限环境 [AGPL-3.0][agpl3]。
* [safe-read](https://github.com/phoe/safe-read) - READ 的一个变体，可以防止内部轰炸、过多的输入和宏字符。 [BSD_2 条款][17]。
* [secret-values](https://github.com/rotatef/secret-values) - 一个 Common Lisp 库，可降低意外泄露密码等秘密值的风险。
  * [privacy-output-stream](https://github.com/atgreen/privacy-output-stream) - 一个输出流，根据秘密值用“****”屏蔽秘密字符串。麻省理工学院。

要安全地“读取”数据，另请参阅“uiop:with-safe-io-syntax”和
关联的“safe-read-*”函数（它们确保我们用
标准可读表和“#.”被禁止以避免读取时间
评价）。


系统界面
--------------------

* [machine-state](https://codeberg.org/shinmera/machine-state/) - 检索有关 CPU 时间、内存使用情况、线程处理时间等机器状态信息。

其他
-----

其中包含不属于其他类别的任何内容。

* [babel](https://github.com/cl-babel/babel) - 字符集编码/解码库。 [外籍人士][14]。
* [fast-io](https://github.com/rpav/fast-io) - 快速八位位组向量/流 I/O。 [3 条款 BSD][15]。
* [named-readtables](https://github.com/melisgl/named-readtables) - 提供一个可读的命名空间，类似于包命名空间。 [3 条款 BSD][15]。
* [simple-currency](https://github.com/a0-prw/simple-currency) - 使用欧洲央行发布的每日信息的货币换算库。 [FreeBSD][39]。
* [trivial-garbage](https://github.com/trivial-garbage/trivial-garbage) - 一个可移植的终结器、弱哈希表和弱指针 API。公共领域。
* [trivial-utf8](https://common-lisp.net/project/trivial-utf-8/) - 用于执行基于 UTF-8 的 I/O 的小型库。 BSD。

贡献
============
随时欢迎您的贡献！请提交拉取请求或创建
将新框架、库或软件添加到列表中的问题。

我们（尝试）遵守的规则如下：

- 默认情况下，将库添加到其部分的末尾。
- 绝对事实上的库，如 BordeauxThreads 或 Quicklisp，
应用 ⭐ 表示（Unicode 代码 U+2B50）。
- 两个范围非常相似的库应该并排，或者在一个
他们自己的部分。
- 根据您的经验和现状进行一些策划
图书馆的文档。我们*不*旨在列出所有现有的
CL 库（请参阅 Cliki）也不列出每个
“流行”库（参见 Quicklisp 统计）。
- 因此，我们最喜欢的库标有 👍 (`1F44D`
统一码字符）。另请参阅中的标志说明
介绍。


[2]：http://www.gnu.org/copyleft/gpl.html
[3]：http://www.gnu.org/software/classpath/license.html
[4]：https://common-lisp.net/project/armedbear/faq.shtml#qa
[5]：http://unlicense.org/
[6]：http://www.gnu.org/software/clisp/impnotes.html
[8]：http://opensource.franz.com/preamble.html
[9]：https://www.gnu.org/licenses/lgpl-3.0.en.html
[11]：http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html
[13]：http://www.sbcl.org/manual/index.html#ANSI-Conformance
[14]：https://directory.fsf.org/wiki/License:Expat
[15]：https://directory.fsf.org/wiki/License:BSD_3Clause
[16]：https://www.quicklisp.org/beta/
[17]：https://directory.fsf.org/wiki/License:BSD_2Clause
[20]：http://www.cs.northwestern.edu/academics/courses/325/readings/graham/graham-notes.html
[21]：http://www.goodreads.com/book/show/1175730.Object_Oriented_Programming_in_Common_LISP
[22]：https://en.wikipedia.org/wiki/ISC_license
[33]：https://directory.fsf.org/wiki/License:Zlib
[39]: https://directory.fsf.org/wiki?title=License:FreeBSD
[47]：https://directory.fsf.org/wiki/License:CPLv1.0
[51]：https://directory.fsf.org/wiki/License:ArtisticLicense2.0
[54]：https://directory.fsf.org/wiki/License:Boost1.0
[59]：https://directory.fsf.org/wiki/License:EPLv1.0
[71]：https://codeberg.org/shimera/plump
[72]：https://codeberg.org/shimera/lquery
[89]: https://directory.fsf.org/wiki/License:Apache2.0
[156]：http://letoverlambda.com/
[157]：http://norvig.com/paip.html
[176]: https://github.com/gwkkwg/lift/blob/master/COPYING
[188]: https://github.com/triclops200/quickapp
[200]：https://opensource.org/licenses/MIT
[201]: https://github.com/google/lisp-koans
[205]: https://www.postgresql.org/about/licence/
[206]: http://www.gigamonkeys.com/book/
[207]: https://opensource.org/licenses/bsd-license.php
[208]: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html
[209]: http://www.eclipse.org/legal/epl-v10.html
[210]: https://common-lisp.net/project/linedit/license.html
[agpl3]：https://directory.fsf.org/wiki/License:AGPL-3.0
[211]：http://mozilla.org/MPL/2.0/
