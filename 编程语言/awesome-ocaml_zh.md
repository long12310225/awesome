很棒的 OCaml
=============

<img src="colour-logo.png" width="70%" />

> _**掌握 OCaml 之路上所需的一切。**_

精选的 OCaml 工具、框架、库和文章的参考列表。此外，还有一系列免费提供的[**书籍**](https://github.com/rizo/awesome-ocaml/tree/master/books)、[**论文**](https://github.com/rizo/awesome-ocaml/tree/master/papers)和[**演示文稿**](https://github.com/rizo/awesome-ocaml/tree/master/presentations)。

如果您正在寻找有关 OCaml 的全面社区驱动内容，请访问 📚[OCamlverse](https://ocamlverse.github.io/)！

有关现代 OCaml 开发工作流程的快速介绍，请参阅 [**使用 OCaml** 进行启动和运行**](https://ocaml.org/learn/tutorials/up_and_running.html) 教程。

您最喜欢的套餐没有列出？ Fork 并[创建 Pull 请求](https://github.com/rizo/awesome-ocaml/edit/master/README.md) 来添加它！

## 内容

- [Community](#community)
- [算法和数据结构](#algorithms-and-data-structures)
- [应用程序库](#application-libraries)
- [Benchmarking](#benchmarking)
- [Blogs](#blogs)
- [Books](#books)
- [Videos](#videos)
- [代码分析和 Linters](#code-analysis-and-linters)
- [编译器和编译工具](#compilers-and-compiler-tools)
- [Concurrency](#concurrency)
- [Databases](#databases)
- [Datetime](#datetime)
- [开发者工具](#developer-tools)
- [练习和简短示例](#exercises-and-short-examples)
- [正式软件验证](#formal-software-verification)
- [General](#general)
- [Graphics](#graphics)
- [Internationalization](#internationalization)
- [用户界面](#user-interface)
- [Language-related](#language-related)
- [大型源代码示例](#large-source-code-examples)
- [Logging](#logging)
- [机器学习](#machine-learning)
- [Messaging](#messaging)
- [Metaprogramming](#metaprogramming)
- [Metrics](#metrics)
- [移动应用程序](#mobile-applications)
- [Networking](#networking)
- [在线课程](#online-courses)
- [包管理](#package-management)
- [Parallelism](#parallelism)
- [项目启动模板](#project-starter-templates)
- [打印机助手](#printers-helpers)
- [Questions](#questions)
- [正则表达式](#regular-expressions)
- [科学与技术计算](#science-and-technical-computing)
- [安全与密码学](#security-and-cryptography)
- [语义技术](#semantic-technology)
- [Serialization](#serialization)
- [系统编程](#system-programming)
- [Testing](#testing)
- [Utilities](#utilities)
- [网页开发](#web-development)

* * *


## 社区

- [OCaml 官方网站](https://ocaml.org/)
- [OCaml Discourse 网络论坛](https://discuss.ocaml.org/)
- [OCaml Discord 聊天](https://discord.gg/ZBgYuvR)
- [官方 OCaml 邮件列表](https://inbox.ocaml.org/caml-list/)
- [奥卡星球](https://ocaml.org/community/planet/)
- [OCaml Reddit 子版块](https://www.reddit.com/r/ocaml/)


## 算法和数据结构

- [比较用 F# 和 OCaml 实现的机器学习算法](https://philtomson.github.io/blog/2014-05-29-comparing-a-machine-learning-algorithm-implemented-in-f-sharp-and-ocaml/)
- [OCamlgraph](https://github.com/backtracking/ocamlgraph) - OCaml 的通用图形库。
- [ods](https://github.com/owainlewis/ods) - OCaml 数据结构和算法的大量集合。
- [combine](https://github.com/backtracking/combine) - 用于组合学的 OCaml 库 <https://www.lri.fr/~filliatr/combine/>。
- [Decompress](https://github.com/mirage/decompress) - Zlib 的纯 OCaml 实现。
- [Ke](https://github.com/mirage/ke) - OCaml 中队列 (FIFO) 的快速实现。
- [Duff](https://github.com/mirage/duff) - P. MacDonald 在 OCaml 中实现 Rabin 指纹和增量压缩（与 [libXdiff](http://www.xmailserver.org/xdiff-lib.html) 相同）
- [ORaft](https://github.com/komamitsu/oraft) - OCaml实现的[Raft共识算法](https://raft.github.io/raft.pdf)库
- [ODiff](https://github.com/dmtrKovalenko/odiff) - 在 OCaml 和 ReasonML 中实现的 [YIQ NTSC 传输图像差异算法](http://www.progmat.uaem.mx:8080/artVol2Num2/Articulo3Vol2Num2.pdf) 库。

## 应用程序库

- [Batteries Included](https://github.com/ocaml-batteries-team/batteries-included) - 社区维护的 OCaml 项目基础库。
- [Cmdliner](https://github.com/dbuenzli/cmdliner) - OCaml 命令行接口的声明性定义。
- [Core](https://github.com/janestreet/core) - Jane Street Capital 成熟的标准库覆盖。 Core 的可移植子集也可用：[Core_kernel](https://github.com/janestreet/core_kernel)。
- [Base](https://github.com/janestreet/base) - Jane Street Capital 的无依赖、快速编译、完全可移植跨任何可以运行 OCaml 代码的环境的标准库。
- [React](http://erratique.ch/software/react) - React 是一个用于函数反应式编程 (FRP) 的 OCaml 模块。它为具有时变值、声明性事件和信号的程序提供支持。
- [Minicli](https://github.com/UnixJunkie/minicli) - 用于命令行解析的极简库。
- [easy-format](https://github.com/mjambon/easy-format) - OCaml 的漂亮打印库。
- [ocaml-rpc](https://github.com/mirage/ocaml-rpc) - 在 OCaml 中处理 RPC 的轻量级库。
- [ocaml-containers](https://github.com/c-cube/ocaml-containers) - 轻量级、模块化标准库扩展、字符串库以及各种库（bigarrays、Unix 等）的接口 BSD 许可证。


## 标杆管理

- [core_bench](https://github.com/janestreet/core_bench) - Jane Street 的 OCaml 微基准测试库。
  - [Core_bench 入门](https://github.com/janestreet/core_bench/wiki/Getting-Started-with-Core_bench)
- [benchmark](https://github.com/Chris00/ocaml-benchmark) - 用于使用延迟或吞吐量测量函数运行时间的基准函数。


## 博客

- [Gagallium](http://gallium.inria.fr/blog/)
- [OCaml 类型 – 关于 OCaml 的许多事情](http://typeocaml.com/)
- [OCaml平台](https://opam.ocaml.org/blog/)
- [德鲁普的事](https://drup.github.io/)
- [Thomas Letan 关于 OCaml 的文章](https://soap.coffee/~lthms/tags/ocaml.html)

## 书籍

- [More OCaml: Algorithms, Methods, and Diversions](https://www.amazon.com/More-OCaml-Algorithms-Methods-Diversions/dp/0957671113/) - 在《更多 OCaml》一书中，John Whitington 深入介绍了 OCaml 的函数式编程，介绍了各种语言功能并描述了一些经典算法。本书最后以一个处理 PDF 文件生成的大型示例结束。每章都有问题，以及已制定的答案和提示。
- [How to Think Like a (Functional) Programmer](http://www.greenteapress.com/thinkocaml/index.html) 作者是 Allen Downey 和 Nicholas Monje – How to Think Like a Computer Scientist 是一本基于 OCaml 语言的入门编程教科书。它是 Allen Downey 的 Think Python 的修改版本。它面向编程新手，以及那些了解一些编程但想学习面向函数范式编程的人，或者只是想学习 OCaml 的人。
- [OCaml from the Very Beginning](http://ocaml-book.com/) 作者：J. Whitington - OCaml from the Very Beginning 将吸引渴望探索 OCaml 等函数式语言的新程序员和经验丰富的程序员。
- Richard Bird 的 [Pearls of Function Algorithm Design](https://www.amazon.co.uk/Pearls-Functional-Algorithm-Design-Richard/dp/0521513383) - 总结了函数编程世界中的 30 个难题。虽然是针对Haskell，但是算法问题很有趣，尝试用OCaml解决也有助于函数式编程的思维。 OCaml 中的部分解决方案位于[此处](https://github.com/MassD/pearls)。
- [Real World OCaml](https://realworldocaml.org/)，作者：Y. Minsky、A. Madhavapeddy 和 J. Hickey - 面向大众的函数式编程。
- [OCaml 中的 Unix 系统编程](https://ocaml.github.io/ocamlunix/)，作者 X. Leroy 和 D. Rémy – Unix 系统编程简介，重点是进程之间的通信。
- [Using, Understanding, and Unraveling OCaml](https://caml.inria.fr/pub/docs/u3-ocaml) - 本书介绍了 OCaml 语言及其强大的类型系统背后的理论基础。
- [Purely Functional Data Structures](https://www.amazon.co.uk/Purely-Functional-Structures-Chris-Okasaki/dp/0521631246/ref=sr_1_1?ie=UTF8&qid=1406279836&sr=8-1&keywords=functional+data+structures) - 这是第一本或唯一一本关注 FP 世界中各种数据结构的书。必读之作。
- [OCaml for Scientists](http://www.ffconsultancy.com/products/ocaml_for_scientists/) - 作者：乔恩·哈罗普。
- [OCaml Programming: Correct + Efficient + Beautiful](https://cs3110.github.io/textbook) - OCaml 中的函数式编程和数据结构教科书 - Michael R. Clarkson 等人编写。

## 视频

 - [OCaml Programming: Correct + Efficient + Beautiful](https://www.youtube.com/playlist?list=PLre5AT9JnKShBOPeuiD9b-I4XROIJhkIU) - Michael R. Clarkson 录制的 200 个小视频列表。它可以独立于标题相同并在[书籍部分](#books) 中列出的教科书之外观看。

## 代码分析和 Linters

- [Mascot](http://mascot.x9c.fr/) - Mascot 是 OCaml 源代码的样式检查器。
- [pfff](https://github.com/returntocorp/pfff) - pfff 是一组工具和 API，用于执行一些静态分析、动态分析、代码可视化、代码导航或保留样式的源到源转换（例如源代码重构）。
- [Infer](https://github.com/facebook/infer) - Infer 是 Java、C 和 Objective-C 的静态分析器
- [Frama-C](http://frama-c.com) - Frama-C 是 C 和 C++ 的静态分析和形式化证明框架。
- [flow](https://github.com/facebook/flow) - flow 是 JavaScript 的静态类型检查器。
- [SLAyer](https://github.com/Microsoft/SLAyer) - SLAyer是一种自动形式验证工具，使用分离逻辑来验证C程序的内存安全性。
- [MemCAD](https://github.com/Antique-team/memcad) - MemCAD 是形状分析的抽象解释器。 MemCAD 可以验证操作复杂数据结构的 C 程序。
- [Camelot](https://github.com/upenn-cis1xx/camelot) - Camelot 是一个模块化且完全可配置的 OCaml linter 和样式检查器。
- [coq-of-ocaml](https://github.com/formal-land/coq-of-ocaml) - 从 OCaml 到 Coq 的转换器，以正式验证 OCaml 代码。
- [MOPSA](https://gitlab.com/mopsa/mopsa-analyzer) - MOPSA 是一个基于抽象解释理论构建健全静态分析器的通用框架。


## 程序分析
- [BAP](https://github.com/BinaryAnalysisPlatform/bap) - BAP是一个针对二进制程序的逆向工程和程序分析平台。
- [BinCat](https://github.com/airbus-seclab/bincat) - BinCat是一个二进制代码静态分析工具包。
- [cwe_checker](https://github.com/fkie-cad/cwe_checker) - cwe_checker 在二进制可执行文件中查找易受攻击的模式。
- [Owi](https://github.com/OCamlPro/owi) - Owi 是一个用于在 OCaml 中使用 WebAssembly (Wasm) 的工具链，具有强大的 Wasm 并行符号执行引擎。它还提供用于编译和分析 C 和 Rust 程序的前端。
- [Smt.ml](https://github.com/formalsec/smtml) - Smt.ml 是一个前端 OCaml 库，可与多个 SMT 求解器交互，支持在 OCaml 程序中无缝集成 Z3、cvc5、Colibri2、Bitwuzla 和 Alt-Ergo 等求解器。

## 编译器和编译工具

- **语言和编译器**：
  - [Caramel](https://caramel.run/) - Caramel 是一种函数式语言，用于构建类型安全、可扩展且可维护的应用程序。
  - [cDuce](http://www.cduce.org/) - cDuce 是一种具有创新功能的现代面向 XML 的函数式语言。
  - [Compcert C Compiler](http://compcert.inria.fr/) - 它是一个 C 编译器，支持大多数 ISO C90 和 C99 / ANSI C 功能。
  - [Eff Programming Language](http://www.eff-lang.org/) - Eff 是一种函数式语言，不仅具有异常处理程序，还具有其他计算效果（例如状态或 I/O）的处理程序。
  - [黑客编程语言](https://hacklang.org/)
  - [Haxe编程语言](https://haxe.org/)
  - [Neko Programming Language](https://nekovm.org/) - 最初编译器是用 OCaml 编写的。
  - [Mazeppa](https://github.com/mazeppa-dev/mazeppa) - 用于按值调用函数语言的现代超级编译器。
  - [Mezzo Programming Language](https://protz.github.io/mezzo/) - Mezzo 是一种遵循 ML 传统的编程语言，它非常强调对别名的控制和对可变内存的访问。
  - [OCaml-Java](http://www.ocamljava.org/) - OCaml 到 Java 字节码编译器。
  - [奥帕编程语言](http://opalang.org/)
  - [Rhine](https://github.com/artagnon/rhine-ml) - 用 OCaml 编写的 LLVM 上的 Lisp。
  - [Rust Programming Language](https://www.rust-lang.org/) - 最初是在引导之前用 OCaml 编写的。
  - [Quick C-- Target Language](http://www.cminusminus.org/) - 现在它是一个死项目。 [Github 存储库](https://github.com/nrnrnr/qc--)。 [替代网站](http://www.cs.tufts.edu/~nr/c--/qc--.html)。
  - [tis-interpreter](https://github.com/TrustInSoft/tis-interpreter) - 一个解释器，用于查找用标准 C 编写的程序中的细微错误

  - [Reason](http://facebook.github.io/reason/) - Facebook 的 OCaml 友好语法和工具链。
  - [RaML](http://raml.co/index.html) - 资源感知 ML (RaML) 是一种自动静态计算 OCaml 程序资源使用范围的工具。
  - [Liquid ML](https://github.com/benfaerber/liquid-ml) - 适用于 OCaml 的 Shopify Liquid 模板语言。

- **解析器和词法分析器生成器**：
  - [Opal](https://github.com/pyrocat101/opal) - OCaml 的自包含一元解析器组合器。
- [Sedlex](https://github.com/ocaml-community/sedlex) 是一个现代的、与编码无关的（读取：支持 Unicode）词法分析器生成器（[ulex](http://www.cduce.org/download.html#side) 的基于 ppx 的后继者。）
  - [Menhir](http://gallium.inria.fr/~fpottier/menhir/) - Menhir 是 OCaml 的 LR(1) 解析器生成器。
- 有关使用 Menhir 和 Sedlex 生成有用解析器的更清晰示例，请参阅 [ocaml-parsing](https://github.com/smolkaj/ocaml-parsing)，
- ...和 [Obelisk](https://github.com/Lelio-Brun/Obelisk)，一个简洁的项目，可为您的语法生成可读的 LaTeX、HTML 或纯文本 EBNF 样式文档。
  - [ocamllex/ocamlyacc](http://caml.inria.fr/pub/docs/manual-ocaml-4.01/lexyacc.html) - OCaml 的 lex 和 yacc 实现。
  - [Angstrom](https://github.com/inhabitedtype/angstrom) - 为速度和内存效率而构建的解析器组合器
- **文章**：
  - [万花筒：在 Objective Caml 中使用 LLVM 实现语言¶](http://llvm.org/docs/tutorial/OCamlLangImpl1.html)


## 并发性
在 OCaml 5.0 之前，有两个用于并发编程的库：_Lwt_ 和 _Async_。它们提供非常相似的功能，但在错误处理和内部实现细节方面做出完全不同的决定（有关更多详细信息，请参阅下面的链接）。 [真实世界 OCaml](https://realworldocaml.org/) 使用异步，但 [代码示例翻译为 Lwt](https://github.com/dkim/rwo-lwt) 的版本也可用。

随着 OCaml 5.0 中 [Effect Handlers](https://ocaml.org/manual/effects.html) 的引入，已经创建了许多其他用于并发编程的库，用直接风格的方法取代了 LWT 和 Async 的单子方法。

- **图书馆**：
  - [Eio](https://github.com/ocaml-multicore/eio) - 用于多核 OCaml 的基于效果的直接式 IO。
  - [Miou](https://github.com/robur-coop/miou) - OCaml 5 的简单调度程序。
  - [Lwt](http://ocsigen.org/lwt/) - OCaml 的协作线程库。
  - [Async](https://opensource.janestreet.com/async/) - 与核心库配合使用的单子并发库。
- **文章**：
  - [介绍 Async 的博文](https://blog.janestreet.com/announcing-async/)
  - [用户放弃异步](http://rgrinberg.com/posts/abandoning-async/)
- [OCaml 中的协作并发：Core.Std.Async 示例](http://philtomson.github.io/blog/2014/07/09/core-dot-async-example/)。

## 数据库

- **绑定**
  - [Dbm](https://forge.ocamlcore.org/projects/camldbm/) - 与 NDBM/GDBM Unix“数据库”的绑定。
  - [Mongo.ml](https://massd.github.io/mongo/) - Mongodb 的 OCaml 驱动程序
  - [PG'OCaml](http://pgocaml.forge.ocamlcore.org/) - 纯 OCaml 中 PostgreSQL 的类型安全接口。
    - [ppx_pgsql](https://github.com/tizoc/ppx_pgsql) - 使用 PG'OCaml 的嵌入式 SQL 查询的语法扩展。
  - [PostgreSQL-OCaml](https://mmottl.github.io/postgresql-ocaml/) - 通过 C API (`libpq`) 的 PostgreSQL 接口。
  - [SQLite3](https://github.com/mmottl/sqlite3-ocaml) - OCaml 绑定到 SQLite3 数据库。
  - [Sqlite3EZ](https://mlin.github.io/ocaml-sqlite3EZ/) - SQLite3 的瘦包装器，具有简化的界面。
  - [ocaml-redis](https://github.com/0xffea/ocaml-redis) - OCaml 的 Redis 绑定。
  - [mariadb](https://github.com/ocaml-community/ocaml-mariadb) - 绑定MariaDB/MySQL，支持非阻塞API
  - [pgx](https://github.com/arenadotio/pgx) - 一个纯 OCaml PostgreSQL 客户端库。
  - [mysql_protocol](https://github.com/slegrand45/mysql_protocol) - 使用 Bitstring 库实现 MySQL 协议。
- **新实施**
  - [Irmin](https://github.com/mirage/irmin) - 遵循与 Git 相同设计原则的分布式数据库。
  - [Obigstore](http://obigstore.forge.ocamlcore.org/) - LevelDB 之上具有类似 BigTable 数据模型的数据库。
  - [RunOrg](https://github.com/RunOrg/RunOrg) - 它是一个用 OCaml 编写的 WIP 数据库服务器。
  - [dokeysto](https://github.com/UnixJunkie/dokeysto) - 哑 OCaml 键值存储、字符串键和字符串
价值观。可选的即时 LZ4 值压缩或 tokyabinet 后端。
- **叠加**
  - [Sequoia](https://github.com/andrenth/sequoia) - Sequoia 是 MySQL/MariaDB 和 PostgreSQL 的类型安全查询构建器
  - [Macaque](https://github.com/ocsigen/macaque) - Macaque 是一个使用 PG'OCaml 之上的推导式进行安全、灵活的数据库查询的库。
  - [ORM](https://github.com/mirage/orm) - SQLite 的 ORM。
  - [Caqti](https://github.com/paurkedal/ocaml-caqti) - 对关系数据的协作线程访问
  - [Caqti 设置准备，ppx_rapper](https://github.com/roddyyaga/ppx_rapper)
- **文章**：
  - [使用 Ocaml 和 Bitstring 实现二进制 Memcached 协议](https://andreas.github.io/2014/08/22/implementing-the-binary-memcached-protocol-with-ocaml-and-bitstring/)
  - [将 OCaml 和 PostgreSQL 与 Caqti 连接](https://medium.com/@bobbypriambodo/interfacing-ocaml-and-postgresql-with-caqti-a92515bdaa11)
- [最后，类型安全、可扩展且高效的语言集成查询](https://www.cs.tsukuba.ac.jp/~kam/papers/pepm2016a.pdf)，作者：Oleg and Co.
所提出的方法是以类型安全的方式描述 SQL 查询并在发送到数据库引擎之前对其进行优化（使用术语重写或评估标准化）。它有可能将 O(n^2) 查询优化为 O(n) 查询。


## 日期时间

- [ISO8601](https://github.com/sagotch/ISO8601.ml)
- [calendar](http://calendar.forge.ocamlcore.org/)
- [odate](https://github.com/hhugo/odate)
- [ptime](http://erratique.ch/software/ptime)


## 开发者工具

- [Try OCaml](https://try.ocamlpro.com/) - 在网络浏览器中尝试 OCaml。
- [学习-ocaml](https://github.com/ocaml-sf/learn-ocaml)。 learn-ocaml-corpus 底层的 Web 应用程序（用 OCaml 编写）。可以定制以服务讲座（使用 Markdown 幻灯片）、游乐场（使用顶级前奏）和互动练习（使用 OCaml 测试）。麻省理工学院许可证。
- [learn-ocaml.el](https://github.com/pfitaxel/learn-ocaml.el)。 Emacs 的次要模式，可以在登录到 Learn-OCaml 实例后显示练习主题并对练习解决方案进行评分。麻省理工学院许可证。
- [BetterOCaml](https://betterocaml.ml) - 一个高效、直观、跨平台的 Web IDE，可在浏览器中解释并运行 OCaml 代码！
- [codingground](https://www.tutorialspoint.com/compile_ocaml_online.php) - 在线编译并执行 OCaml 代码。
- [OCaml: Learn & Code iOS app](https://apps.apple.com/app/ocaml-learn-code/id1547506826) - 从您的 iPhone/iPad/Mac 学习并执行 OCaml 代码。
- [Jupyter](https://github.com/akabe/ocaml-jupyter) - Jupyter 笔记本的 OCaml 内核。
- [utop](https://github.com/ocaml-community/utop) - OCaml 的通用顶层，支持多行版本、历史记录、实时和上下文相关的完成、颜色等。
- [ocamlformat](https://github.com/ocaml-ppx/ocamlformat) - 用于格式化 OCaml 代码的命令行工具。
- [ocamlbrowser](http://caml.inria.fr/pub/docs/manual-ocaml/browser.html) - 源代码和编译的界面浏览器，使用 LablTk 编写。包含在 ocaml <= 4.01 的标准发行版中，并包含在 ocaml >= 4.02 的 labltk 中。
- [ghim](https://github.com/samoht/ghim) - 用于管理 Github 问题的命令行工具。
- [OCaml Yeoman Generator](https://github.com/mabrasil/generator-ocaml) - 用于搭建 OCaml 模块的 Yeoman 生成器。
- [puml2xml](https://github.com/khalidbelk/puml2xml) - PlantUML (**.puml**) 到 XML (**.xmi**) 转换器。

- **对外函数接口**：
  - [ctypes](https://github.com/ocamllabs/ocaml-ctypes) - 使用纯 OCaml 绑定到 C 库的库。
  - [ocaml-main-program-in-c](https://github.com/johnwhitington/ocaml-main-program-in-c) - 用于制作混合 C/Ocaml 二进制文件的示例构建系统，其中主程序使用 C 语言。
  - [模块化外部函数绑定](http://openmirage.org/blog/modular-foreign-function-bindings)
  - [Py.ml](https://github.com/thierry-martinez/pyml) - Python 的 OCaml 绑定。
- **编辑器集成**：
  - [ocaml-lsp](https://github.com/ocaml/ocaml-lsp) - OCaml 的 LSP 语言服务器，可与任何理解 LSP 的编辑器集成，例如 [VSCode](https://github.com/microsoft/vscode)、Vim 和 Emacs。
  - [merlin](https://github.com/ocaml/merlin) - Vim 和 Emacs 中 OCaml 的上下文敏感完成。
  - [tuareg](https://github.com/ocaml/tuareg) - Emacs 的 OCaml 模式可以在 Emacs 中运行顶层和调试器。
  - [opam-switch-mode](https://github.com/ProofGeneral/opam-switch-mode) - Emacs 的次要模式，通过菜单扩展 Tuareg 和 Merlin，以更改或重置环境 Emacs 会话中的 opam 开关。
  - [merlin-eldoc](https://github.com/Khady/merlin-eldoc) - Emacs 包通过 eldoc 提供 merlin 的功能。
  - [vscode-ocaml](https://github.com/hackwaly/vscode-ocaml) - 为 [VSCode](https://github.com/microsoft/vscode) 提供 OCaml 语言支持的扩展
  - [OCaml Debugger](https://github.com/hackwaly/ocamlearlybird) - 为 [VSCode](https://github.com/microsoft/vscode) 提供 OCaml 调试器的扩展
  - [Sublime better ocaml](https://github.com/whitequark/sublime-better-ocaml) - Sublime Text 更好的 OCaml 模式。
    - [Sublime文本包](https://github.com/def-lkb/sublime-text-merlin)
  - [ocp-index](http://www.typerex.org/ocp-index.html) - 轻松访问已安装的 OCaml 库的接口信息。提供独立工具，如“ocp-browser”和“ocp-grep”。
    - [ocp-browser](http://www.typerex.org/ocp-index.html#ocp-browser) - 基于 ncurses 的小型 API 和文档浏览器。
    - [ocp-index-top](https://github.com/reynir/ocp-index-top) - 使用 ocp-index 查找文档的顶级指令。
    - [Sublime文本包](https://sublime.wbond.net/packages/OCaml%20Autocompletion)
  - [ocp-indent](http://www.typerex.org/ocp-indent.html) - OCaml 的缩进工具，可在 Emacs 和 Vim 等编辑器中使用。
- [Vim 插件](https://github.com/def-lkb/ocp-indent-vim)。
- **代码覆盖率**：
  - [Bisect_ppx](https://github.com/aantron/bisect_ppx)


## 练习和简短示例

- [99 个问题](https://ocaml.org/learn/tutorials/99problems.html)。 99% 的解决方案都在[这里](https://github.com/MassD/99)。
- [learn-ocaml-corpus](https://ocaml-sf.org/learn-ocaml-public/#activity=exercises)。带有自动评分测试的初级到高级在线练习语料库（包括来自 OCaml MOOC 的练习）。
- [罗塞塔代码](http://rosettacode.org/wiki/Category:OCaml)
- [OCaml at Exercism](http://exercism.io/languages/ocaml) - Exercism 是您参与有关代码的深思熟虑的对话的场所。探索简单性、惯用的语言特性以及富有表现力、可读性的代码。 [解决方案](https://github.com/exercism/xocaml)。
- [Programming Language Examples Alike Cookbook](http://pleac.sourceforge.net/pleac_ocaml/index.html) - 本书的 OCaml 部分是使用 OCaml 解决常见编程问题的免费参考。

## 正式软件验证

- [Coq](https://coq.inria.fr/) - Coq 是一个正式的证明管理系统。它提供了一种用于编写数学定义、可执行算法和定理的形式语言，以及用于机器检查证明的半交互式开发的环境。
- [Why3](http://why3.lri.fr/) - Why3是一个演绎程序验证平台。它提供了一种丰富的规范和编程语言，称为 WhyML，并依赖于自动和交互式的外部定理证明器来释放验证条件。
- [Alt-Ergo](http://alt-ergo.lri.fr/) - Alt-Ergo 是一款开源 SMT 求解器，致力于证明程序验证中生成的数学公式。


## 一般

- [使用 OCaml 进行函数式编程](https://haifengl.wordpress.com/2014/06/17/ocaml-introduction/)
- [Python 到 OCaml：回顾](http://roscidus.com/blog/blog/2014/06/06/python-to-ocaml-retrospective/)
- [面向大众的 OCaml](http://queue.acm.org/detail.cfm?id=2038036)
- [为什么我们使用 OCaml](https://espertech.wordpress.com/2014/07/15/why-we-use-ocaml)
- [Xen – OCaml 编码注意事项](http://wiki.xen.org/wiki/OCaml_Coding_Considerations)
- [单子是一类硬性药物](http://lambda-diode.com/programming/monads-are-a-class-of-hard-drugs)
- [OCaml 初学者指南](http://blog.nullspace.io/beginners-guide-to-ocaml-beginners-guides.html)
- [为什么选择 OCaml，为什么是现在？](http://spyder.wordpress.com/2014/03/16/why-ocaml-why-now/)
- [关于 OCaml 游戏开发的博客](http://cranialburnout.blogspot.ca/)
- [（功能）继承的替代方案](http://ocamltutorials.blogspot.se/2013/06/alternatives-to-subtyping.html)
- [camlPDF](https://github.com/johnwhitington/camlpdf) - 用于读取、写入和修改 PDF 文件的 OCaml 库。
- [slacko](https://github.com/Leonidas-from-XIV/slacko) - OCaml 中 Slack 的简洁界面。
- [Learn X in Y minutes](https://learnxinyminutes.com/docs/ocaml/) - 其中 X=OCaml。


## 图形

- **2D**
  - [archimedes](http://archimedes.forge.ocamlcore.org/) - 2D 绘图库。
  - [cairo2](https://github.com/Chris00/ocaml-cairo) - 绑定到 Cairo，一个 2D 矢量图形库。与 lablgtk 集成良好。
  - [Vg](https://github.com/dbuenzli/vg) - OCaml 的声明性 2D 矢量图形。
- **3D**
  - [glMLite](https://github.com/fccm/glMLite) - OCaml 的 OpenGL 绑定。提供（实验性）功能 API。 ([主页](http://decapode314.free.fr/ocaml/GL/))
  - [lablgl](https://forge.ocamlcore.org/projects/lablgl/) - OpenGL 接口。与 lablgtk 集成良好。
  - [tgls](http://erratique.ch/software/tgls) - 精简绑定 OpenGL 3.{2,3},4.{0,1,2,3,4} 和 OpenGL ES {2,3}。


## 国际化

- [Camomile](https://github.com/yoriyuki/Camomile/) - OCaml 的 Unicode 库。
- [ocaml-m17n](https://github.com/whitequark/ocaml-m17n) - OCaml 源代码的多语言化。允许在 OCaml 源代码中使用 Unicode 标识符。
- [Uucd](https://github.com/dbuenzli/uucd) - OCaml 的 Unicode 字符数据库解码器。
- [Uucp](https://github.com/dbuenzli/uucp) - OCaml 的 Unicode 字符属性。
- [Uunf](https://github.com/dbuenzli/uunf) - OCaml 的 Unicode 文本规范化。
- [Uuseg](https://github.com/dbuenzli/uuseg) - OCaml 的 Unicode 文本分段。
- [Uutf](https://github.com/dbuenzli/uutf) - 适用于 OCaml 的非阻塞流式 Unicode 编解码器。


## 用户界面

- [lablgtk](https://garrigue.github.io/lablgtk/) - OCaml 的 GTK2 和 GTK3 绑定与各种更高级别的工具来定义 GUI。
- [lablqml](https://github.com/Kakadu/lablqml) - OCaml 的 QML Qt5 绑定。
- [labltk](https://forge.ocamlcore.org/projects/labltk/) - Tcl/Tk GUI 框架的接口。在 ocaml <= 4.01 的标准分布中。
- [TSDL](http://erratique.ch/software/tsdl) - Tsdl 是一个 OCaml 模块，提供与跨平台 SDL 库的精简绑定。
- [Lambda-Term](https://github.com/ocaml-community/lambda-term) - Lambda-Term 是一个用于操作终端的跨平台库。它提供了按键、鼠标事件和颜色的抽象，以及一组用于编写类似诅咒的应用程序的小部件。
- [Notty](https://github.com/ocaml-community/notty-community) - Notty 是 OCaml 的声明性终端库，围绕可组合图像的概念构建。
- [ocaml-linenoise](https://github.com/ocaml-community/ocaml-linenoise) - 独立的 OCaml 与 linenoise 绑定； OCaml 中简单的高级 readline 功能。


## 语言相关

- [OCaml 中的高阶多态性](http://devmusings.legiasoft.com/blog/2008/05/23/higher-rank_polymorphism_in_ocaml)
- [mikmatch](https://github.com/mjambon/mikmatch) - 使用正则表达式扩展 OCaml 模式匹配
- [构造函数中的内联记录](https://www.lexifi.com/ocaml/inlined-records-constructors/)
- [代数数据类型](https://espertech.wordpress.com/2014/07/30/algebraic-data-types/)
- [XEN – 面向开发人员的 OCaml 最佳实践](http://wiki.xen.org/wiki/OCaml_Best_Practices_for_Developers)
- [OCaml Style Guide (by Jane Street)](https://opensource.janestreet.com/standards/) - 另请参阅：[[1]](https://www.seas.upenn.edu/~cis500/cis500-f06/resources/programming_style.html)、[[2]](http://www.cs.cornell.edu/Courses/cs312/2001sp/style.html)、 [[3]](https://www.seas.upenn.edu/~cis120/20fa/ocaml_style/)。
- [一种安全但奇怪的修改 OCaml 编译器的方法](https://camlspotter.blogspot.com/2012/09/a-safe-but-strange-way-of-modifying.html)
- [摆弄 OCaml 类型系统](https://technotroph.wordpress.com/2013/10/25/fiddling-with-the-ocaml-type-system/)


## 大型源代码示例

- [Base](https://github.com/janestreet/base) - OCaml 标准库
- [cil](https://github.com/cil-project/cil) - C中间语言
- [coq](https://github.com/coq/coq) - 正式证明管理系统
- [frama-c](https://git.frama-c.com/pub/frama-c) - 专用于分析用 C 编写的源代码的平台
- [libguestfs](https://github.com/libguestfs/libguestfs) - 用于访问和修改虚拟机磁盘映像的库和工具
- [Liquidsoap](https://github.com/savonet/liquidsoap) - 用于多媒体流媒体的瑞士军刀，特别用于网络广播和网络电视
- [mirage](https://github.com/mirage/mirage) - 图书馆操作系统，为跨各种云计算和移动平台的安全、高性能网络应用程序构建unikernels
- [MLDonkey](https://github.com/ygrek/mldonkey) - 跨平台多网络点对点守护进程
- [Oni2](https://github.com/onivim/oni2) - 本机、轻量级模态代码编辑器。
- [pfff](https://github.com/returntocorp/pfff) - 用于编写静态分析、动态分析、代码可视化、代码导航或保留样式的源到源转换（例如源代码重构）的 OCaml API。
- [Tezos](https://gitlab.com/tezos/tezos) - 可自我升级的权益证明区块链
- [WHY3](https://gitlab.inria.fr/why3/why3) - 演绎程序验证平台
- [xen-api](https://github.com/xapi-project/xen-api) - 管理堆栈，用于配置和控制启用 Xen 的主机和资源池，并协调池内的资源。

## 记录

- [dolog](https://github.com/UnixJunkie/dolog) - 一个愚蠢的 OCaml 记录器。
- [Volt](https://github.com/codinuum/volt) - Bolt OCaml 日志记录工具的变体。
- [Logs](http://erratique.ch/software/logs) - Logs 为 OCaml 提供了日志记录基础设施。

## 机器学习

- **图书馆**
- [Ocaml-sklearn](https://github.com/lehy/ocaml-sklearn) OCaml 的 scikit-learn。
	- [Owl](https://ocaml.xyz/) - 具有神经网络、算法微分和 ONNX 支持的科学库。
- [使用 OCaml 的对象检测卷积神经网络（基于 Owl）](https://github.com/owlbarn/owl_mask_rcnn)。
	- [PyTorch bindings](https://github.com/LaurentMazare/ocaml-torch) - PyTorch 的 OCaml 绑定。
  	- [Ocaml-NN](https://github.com/ck090/ocaml-nn/tree/main) - OCaml 中神经网络 (FCNN) 的全功能单元实现
- **文章**
- [使用 OCaml 进行深度学习（PyTorch 绑定）](https://blog.janestreet.com/deep-learning-experiments-in-ocaml/)。
- [使用 OCaml 进行迁移学习（PyTorch 绑定）](https://blog.janestreet.com/of-pythons-and-camels/)。
- [使用 OCaml 进行强化学习（PyTorch 绑定）](https://blog.janestreet.com/playing-atari-games-with-ocaml-and-deep-rl/)。

## 消息传递

- [ocaml-zmq](https://github.com/issuu/ocaml-zmq) - 用于 OCaml 的 ZeroMQ 与异步和 Lwt 包装器的绑定。
- [onanomsg](https://github.com/rgrinberg/onanomsg) - OCaml 的 nanomsg 绑定。
- [Kafka](https://github.com/didier-wenzek/ocaml-kafka) - Apache Kafka 的 OCaml 绑定。
- [AMQP](https://github.com/andersfugmann/amqp-client) - 适用于 Async 和 Lwt 的 AMQP 客户端库。
- [MPI](https://github.com/xavierleroy/ocamlmpi) - OCaml 的消息传递接口绑定。
- [MQTT](https://github.com/j0sh/ocaml-mqtt) - MQTT pubsub 协议的 OCaml 实现。
- [capnp-ocaml](https://github.com/capnproto/capnp-ocaml) - 适用于 Cap'n Proto 序列化框架的 OCaml 代码生成器插件。

## 元编程

- **文章**：
  - [OCaml 扩展点指南](http://whitequark.org/blog/2014/04/16/a-guide-to-extension-points-in-ocaml/)
  - [扩展点，或者 OCaml 如何变得更像 Lisp](https://blogs.janestreet.com/extension-points-or-how-ocaml-is-becoming-more-like-lisp)
  - [没有 Camlp4 的语法扩展：让我们开始吧！](https://www.lexifi.com/ocaml/syntax-extensions-without-camlp4-lets-do-it/)
  - [阅读 Camlp4 – 计算机大使](https://ambassadortothecomputers.blogspot.com/p/reading-camlp4.html)
- **语法扩展**：
  - [ppx_import](https://github.com/ocaml-ppx/ppx_import) - Import 是一个语法扩展，允许从其他编译的接口文件中提取类型或签名。
  - [ppx_string_interpolate](https://github.com/sheijk/ppx_string_interpolate) - 一个简单的 ppx 过滤器，支持字符串插值，例如 `[%str "value of foo is $(foo)"]`。
  - [ppx_monad](https://github.com/rizo/ppx_monad) - OCaml 的 Monad 语法扩展。
  - [ppx_deriving_yojson](https://github.com/whitequark/ppx_deriving_yojson) - OCaml 的 Yojson 编解码器生成器。
- **工具和语言扩展**：
  - [MetaOCaml](http://okmij.org/ftp/ML/MetaOCaml.html) - 用于多阶段编程的 OCaml 方言。
  - [Fan](http://bobzhang.github.io/fan/) - Fan 是 OCaml 的编译时元编程系统，最初受到 Camlp4 的启发。它是 OCaml 和 Lispy 宏的组合。它与 OCaml 共享相同的具体语法。
  - [camlp5](https://camlp5.github.io/) - Camlp5 是 OCaml 的一个漂亮的预处理器打印机。
  - [camlp4](http://caml.inria.fr/pub/docs/manual-camlp4/manual002.html) - Camlp4 是标准 OCaml 发行版的一部分，与 Camlp5 不同。

## 指标

- [prometheus](https://github.com/mirage/prometheus) - 用于 Prometheus 监控的 OCaml 客户端库。

## 移动应用程序

- **文章**：
  - [iOS 7 上的 OCaml 发布](http://psellos.com/2014/08/2014.08.ocamlxarm-402.html)
  - [OCaml + Cordova = 更安全、类型化和混合的移动应用程序](https://dannywillems.github.io/2016/07/14/ocaml-cordova-secured-typed-hybrid-mobile-applications.html)
- **绑定**：
  - [Cordova plugins](https://github.com/dannywillems/ocaml-cordova-plugin-list) - Cordova 插件的绑定列表。在 OCaml 中访问本机设备组件，例如加速度计、短信、地理定位等。


## 网络

- **HTTP 工具**：
  - [ocaml-cohttp](https://github.com/mirage/ocaml-cohttp) - 使用 Lwt 或 Async 的非常轻量级的 HTTP 服务器。
  - [ocurl](https://github.com/ygrek/ocurl) - OCaml 绑定到 libcurl。
  - [httpaf](https://github.com/inhabitedtype/httpaf) - 用 OCaml 编写的高性能、内存高效且可扩展的 Web 服务器。
  - [piaf](https://github.com/anmonteiro/piaf) - 完全用 OCaml 编写的 HTTP/1.X / HTTP/2 客户端/服务器库。
- [ocaml-dns](https://github.com/mirage/ocaml-dns) - DNS 协议的纯 OCaml 实现。
- [fluent-logger](https://github.com/fluent/fluent-logger-ocaml) - OCaml 的 Fluentd 记录器。
- [charrua-unix](https://github.com/haesbaert/charrua-unix) - charrua-unix 是一个基于 [charrua-core](https://github.com/haesbaert/charrua-core) 的 Unix DHCP 守护进程。


## 在线课程

- [OCaml MOOC: Introduction to Functional Programming in OCaml](https://www.fun-mooc.fr/en/courses/introduction-functional-programming-ocaml/) - [OCaml Software Foundation](https://ocaml-sf.org/) YouTube 频道的[此播放列表](https://www.youtube.com/playlist?list=PLTBEN441uEY36t5CCrJkdTSv588d3nWN5) 中提供视频。
- [康奈尔大学 – 数据结构和函数式编程](http://www.cs.cornell.edu/Courses/cs3110/2014fa/course_info.php)。
- [普林斯顿大学 - OCaml 中的函数式编程](http://www.cs.princeton.edu/~dpw/courses/cos326-12/)。
- [University of Illinois](https://courses.engr.illinois.edu/cs421/fa2014/) - 使用 OCaml 教授函数式编程和编程语言设计的课程


## 包管理
- **分布**：
  - [OPAM](http://opam.ocamlpro.com/) - 一个灵活的 Git 友好的包管理器，具有多个编译器支持。
  - [ocamlfind](http://projects.camlcity.org/projects/findlib.html) - 本地 OCaml 库管理器。被大多数 OCaml 生态系统使用。
  - [OCaml for Windows](https://fdopen.github.io/opam-repository-mingw) - opam 存储库和 Windows 实验版本（自 2021 年起已弃用）。
  - [Diskuv OCaml](https://github.com/diskuv/dkml-installer-ocaml#readme) - 适用于 Windows 的 Diskuv OCaml 发行版。
  - [makorel](https://github.com/sagotch/makorel) - 轻松发布 OPAM 包。
  - [esy](https://github.com/esy/esy) - 使用 Reason/OCaml 进行本机开发的 package.json 工作流程。

- **构建工具**：
  - [dune](https://github.com/ocaml/dune) - OCaml 的可组合且固执己见的构建系统（前 jbuilder）
  - [Oasis](http://oasis.forge.ocamlcore.org/) - 一个用于在 OCaml 项目中集成配置、构建和安装系统的工具。它有助于在构建系统中创建标准入口点，并允许外部工具轻松分析您的项目。
    - [oasis2opam](https://github.com/ocaml/oasis2opam) - 将 OASIS 元数据转换为 OPAM 包描述的工具。
  - [obuild](https://github.com/ocaml-obuild/obuild) - ocaml 的简单包构建系统。
  - [ocaml-makefile](https://github.com/mmottl/ocaml-makefile) - 易于使用的 Makefile，适用于中小型 OCaml 项目。
  - [topkg](https://github.com/dbuenzli/topkg) - 使用 ocamlbuild 的 OPAM 感知打包系统。
  - [Bazel](https://github.com/jin/rules_ocaml) - OCaml 规则适用于 Google 的多语言和平台构建工具 [Bazel](https://bazel.build/)。

## 并行性

（_注：从更容易使用到更灵活排序。_）

- **图书馆**：
  - [Parmap](http://rdicosmo.github.io/parmap/) - 提供易于使用的并行地图和折叠功能。
  - [ForkWork](https://github.com/mlin/forkwork) - 一个简单的库，用于分叉子进程以在多个核心上执行工作。
  - [Functory](http://functory.lri.fr/About.html) - 分布式计算库，有助于以无缝方式分布式执行可并行计算。
  - [Rpc.Parallel](https://github.com/janestreet/rpc_parallel) - 用于在机器集群上生成进程并在它们之间传递类型化消息的库。
  - [Ocamlnet](http://projects.camlcity.org/projects/ocamlnet.html) - 增强的系统平台库。包含“netmulticore”库，可根据需要在尽可能多的机器核心上计算任务。
  - [Nproc](https://github.com/MyLifeLabs/nproc) - OCaml 的进程池实现。
  - [Parany](https://github.com/UnixJunkie/parany) - 对独立项目进行并行计算，即使它们的数量是无限的。
  - [Sklml](http://sklml.inria.fr) - OCaml 程序的功能并行骨架编译器和编程系统。
  - [SPOC](https://github.com/mathiasbourgoin/SPOC) - 用于将密集计算卸载到并行加速器（多核 CPU、GPU 和与 GPGPU 框架兼容的其他加速器）的库和语法扩展。

- **文章**：
  - [OCaml 的并行化能力状况如何？](https://stackoverflow.com/questions/6588500/what-is-the-state-of-ocamls-parallelization-abilities)
  - [多核 OCaml 中的并行编程](https://github.com/ocaml-multicore/parallel-programming-in-multicore-ocaml)
- [并行编程](https://v2.ocaml.org/releases/5.0/htmlman/parallelism.html) 来自 OCaml 官方手册
- [很棒的多核 OCaml](https://github.com/ocaml-multicore/awesome-multicore-ocaml)。资源汇编

## 打印机助手

- Reason 的原生 [**Console.log**](https://github.com/reasonml/reason-native/tree/master/src/console#consoleloganything)
- [**Dum**](https://github.com/mjambon/dum#readme)
- [**Inspect**](https://github.com/krohrer/caml-inspect#readme)
- [**ppx_deriving** ](https://github.com/ocaml-ppx/ppx_deriving#usage) 的 `[@@deriving show]`。
- [**refl** ](https://github.com/thierry-martinez/refl#basic-usage)，类似 ppx_deriving。
- [**lrt** ](https://github.com/LexiFi/lrt#getting-started)，另一个类似 ppx_deriving 的。
- [**tpf** ](https://github.com/pqwy/tpf#readme)，又是类似 ppx_deriving 的。
- [**typerep** ](https://github.com/janestreet/typerep)，可能是与 ppx_typerep_conv 类似的 ppx_deriving。
- [**repr**](https://mirage.github.io/repr/repr/Repr/index.html#val-pp_json)，除了让用户在需要的地方传递它之外，它似乎还让用户从组合器手动构建类型表示。
- [**data-encoding**](https://gitlab.com/nomadic-labs/data-encoding/-/blob/master/src/tutorial.md#how-to-build-an-encoding)，也是完全手动的。
- [**cmon** ](https://github.com/let-def/cmon#documentation)，完全手动。
- 沙丘中的 [**dyn** ](https://github.com/ocaml/dune/blob/4b95cd3d1b3a62e69a9a9db2bc4af2f9fd2e56d8/otherlibs/dyn/dyn.mli)。它似乎也是完全手动的。
- [**Genprint** ](https://github.com/progman1/genprintlib#readme)
- [**OCaml@p** ](https://github.com/tsubame-sp/ocaml_at_p#readme)


## 项目启动模板

- [drom](https://github.com/OCamlPro/drom/) - drom 工具是 opam/dune 的包装器，试图提供类似货物的用户体验。
- [spin](https://github.com/tmattio/spin) - Reason 和 Ocaml 项目生成器
- [modern-ocaml](https://github.com/Khady/modern-ocaml) - 具有现代工具的 ocaml 项目模板

## 问题

- [除了模板函数之外的 OCaml 多态示例？](https://stackoverflow.com/questions/14440531/ocaml-polymorphism-example-other-than-template-function)
- [OCaml - 多态打印和类型丢失](https://stackoverflow.com/questions/7442449/ocaml-polymorphic-print-and-type-losing)


# 科学与技术计算

- [biocaml](https://github.com/biocaml/biocaml) - OCaml 生物信息学库 <http://biocaml.org>。
- [bistro](https://github.com/pveber/bistro) - 用于构建生物信息学管道的 OCaml 库。
- [lacaml](https://mmottl.github.io/lacaml/) - BLAS/LAPACK（高性能线性代数 Fortran 库）的 OCaml 绑定。
- [obandit](http://freux.fr/oss/obandit.html) - 用于多臂老虎机的 OCaml 库。
- [onumerical](https://github.com/cheshire/onumerical) - OCaml 的数值库。
- [oml](https://github.com/hammerlab/oml) - 用于一般数值工作的 OCaml 库。
- [ocephes](https://github.com/rleonid/ocephes) - 绑定到常用的“C”特殊函数库。
- [slap](https://github.com/akabe/slap) - OCaml 中的线性代数库，具有用于矩阵运算的基于类型的静态大小检查。
- [tensorflow-ocaml](https://github.com/LaurentMazare/tensorflow-ocaml) - TensorFlow 的 OCaml 绑定。
- [owl](https://github.com/owlbarn/owl) - OCaml 数值库：密集和稀疏矩阵、线性代数、回归、数学和统计函数。
- [WHIZARD](https://whizard.hepforge.org/) - 专为高效计算多粒子散射截面和模拟事件样本而设计的系统。


## 正则表达式

- [Re](https://github.com/ocaml/ocaml-re) - 带有组合器的纯 OCaml 正则表达式库，支持多种格式（glob、posix、str 等）。
- [ocaml-pcre](https://github.com/mmottl/pcre-ocaml) - 绑定到 PCRE 库（perl 兼容的正则表达式）
- [Humane-re](https://github.com/rgrinberg/humane-re) - Humane-re 尝试提供一个简单的界面来满足 90% 的正则表达式需求。由 ocaml-re 提供。
- [Tyre](https://github.com/Drup/tyre) - Tire 是一组用于构建类型安全正则表达式的组合器，允许自动提取和修改匹配组。


## 安全与密码学

- [ocaml-tls](https://github.com/mirleft/ocaml-tls) - 纯 OCaml 中的 TLS。
- [Digestif](https://github.com/mirage/digestif) - OCaml 和 C 中的哈希算法（如 SHA* 或 BLAKE2*）。
- [cryptokit](https://github.com/xavierleroy/cryptokit) - OCaml 的 Cryptokit 库提供了多种加密原语，可用于在安全敏感应用程序中实现加密协议。
- [nocoiner](https://github.com/marcoonroad/nocoiner) - 用于在线拍卖、赌博等多方计算的承诺方案库。
- [nocrypto](https://github.com/mirleft/ocaml-nocrypto) - ocaml-tls 项目背后的一个小型加密库。它易于使用，遵循函数式编程原则，并且能够在基于 Xen 的 unikernel 中运行。

> 注意：以下博客文章描述了“nocrypto”和“cryptokit”加密库之间的差异：[OCaml-TLS：构建 nocrypto 库核心](https://mirage.io/blog/introducing-nocrypto)。


## 语义技术

- [OCaml-RDF](https://framagit.org/zoggy/ocaml-rdf) - 用于操作 RDF 图并执行 Sparql 查询的 OCaml 库。


## 序列化

- [atdgen](https://github.com/ahrefs/atd) - 适用于多种语言（OCaml、Java、Python、Scala、Typescript）的序列化编译器，采用 Binou 或 JSON 格式
- [bencode](https://github.com/rgrinberg/bencode) - Bencode（.torrent 文件格式）读取器/写入器。
- [biniou](https://github.com/mjambon/biniou) - 可扩展的二进制数据格式，类似于 JSON，但速度更快。
- [cbor](https://github.com/ygrek/ocaml-cbor) - OCaml 原生 [CBOR](https://cbor.io/) 解码器/编码器。
- [jsonm](http://erratique.ch/software/jsonm) - 适用于 OCaml 的非阻塞流式 JSON 编解码器。
- [xmlm](http://erratique.ch/software/xmlm) - 用于解码和编码 XML 数据格式的流编解码器。
- [yojson](https://github.com/ocaml-community/yojson) - 针对 JSON 格式的优化解析和打印库。
- [sexplib](https://github.com/janestreet/sexplib) - S 表达式解析器和打印机


## 系统编程

- [Mirage OS](https://github.com/mirage/mirage) - Mirage 是一个编程框架，用于跨各种云计算和移动平台构建安全、高性能的网络应用程序。
- [ocaml-fat](https://github.com/mirage/ocaml-fat) - 从 OCaml 读取和写入 FAT 格式文件系统。
- [ocaml-git](https://github.com/mirage/ocaml-git) - 纯 OCaml 低级 git 绑定。
- [ocaml-vchan](https://github.com/mirage/ocaml-vchan) - “vchan”共享内存通信协议的纯 OCaml 实现。

- **嵌入式系统**
  - [OMicroB](https://github.com/stevenvar/omicrob) - 设计用于在 AVR（例如 Arduino）微控制器上运行 OCaml 字节码的虚拟机。
  - [OCaPIC](http://www.algo-prog.info/ocapic/web/index.php?id=OCAPIC:OCAPIC) - 用于 PIC18 微控制器的 OCaml 虚拟机。
  - [ocaml-esp32](https://github.com/sadiqj/ocaml-esp32) - ESP32 SoC 的编译器。


## 测试

- [Alcotest](https://github.com/mirage/alcotest) - 一个轻量级且丰富多彩的测试框架。
- [OUnit](http://ounit.forge.ocamlcore.org/) - OUnit 是 OCaml 的单元测试框架。它允许人们轻松地为 OCaml 代码创建单元测试。它基于 HUnit，Haskell 的单元测试框架。
- [QCheck](https://github.com/c-cube/qcheck) - QCheck 是一个属性测试库，灵感来自 Haskell 的 QuickCheck
- [iTeML](https://github.com/vincent-hugot/iTeML)（以前称为 [qtest](http://batteries.vhugot.com/qtest/)） — 支持内联编译指示生成测试。
- [Kaputt](http://kaputt.x9c.fr/) - 全面的测试框架。
- [Pa_test](https://ocaml.janestreet.com/ocaml-core/111.28.00/doc/pa_test) - 通用内联测试宏。
- [TestSimple](https://github.com/hcarty/ocaml-testsimple) - 与 [Test Anything Protocol](https://testanything.org/) 兼容的轻量级单元测试框架。
- [expect-test](https://github.com/janestreet/ppx_expect) - 一个用 OCaml 编写测试的框架，类似于 [Cram](https://bitheap.org/cram/)，由 [JaneStreet](https://blog.janestreet.com/testing-with-expectations/) 开发。


## 公用事业

- [ocaml-cuid](https://github.com/marcoonroad/ocaml-cuid) - 用于服务器可扩展性和数据库性能的防冲突 ID。
- [Validate](https://github.com/Axot017/validate) - PPX 派生程序旨在简化验证记录的过程。
- [Uuidm](https://erratique.ch/software/uuidm) - Uuidm 是一个 OCaml 模块，根据 RFC 4122 实现 128 位通用唯一标识符版本 3、5（基于 MD5、SHA-1 哈希的名称）和 4（基于随机）。
- [sqids-ocaml](https://github.com/sqids/sqids-ocaml) - Sqids 的官方 OCaml 移植。从数字生成简短的唯一 ID。


## 网页开发

- **框架**：
  - [Opium](https://github.com/rgrinberg/opium) - 用于 OCaml 的类似 Sinatra 的网络工具包。
  - [Ocsigen Eliom](http://ocsigen.org/eliom/) - Eliom 是一个功能齐全的多层框架，用于将多平台 Web 和移动应用程序开发为 100% OCaml 分布式应用程序。它还可用于更传统的 Web 或移动应用程序：网站、单页应用程序、REST API 等。
  - [Dream](https://camlworks.github.io/dream/) - 适用于 OCaml 和 ReasonML 的 Tidy Web 框架
  - [webmachine](https://github.com/inhabitedtype/ocaml-webmachine) - OCaml 的 REST 工具包。 OCaml webmachine 是 cohttp 之上的一层，它实现了基于状态机的 HTTP 请求处理器。它特别适合编写 RESTful API。顾名思义，这是 webmachine 项目的 OCaml 端口。
  - [incr_dom](https://github.com/janestreet/incr_dom) - 使用 Js_of_ocaml 构建动态 Web 应用程序的库
  - [fmlib_browser](https://hbr.github.io/fmlib/odoc/fmlib_browser/doc_overview.html) - 一个库，有助于编写以纯函数式风格在浏览器中运行的 Web 应用程序。
  - [ocaml-vdom](https://github.com/LexiFi/ocaml-vdom) - Elm 架构和 OCaml 的 (V)DOM

- **工具**：
  - [COW](https://github.com/mirage/ocaml-cow) - Caml on the Web (COW) 是一组解析器和语法扩展，可让您直接从 OCaml 代码操作 HTML、CSS、XML、JSON 和 Markdown。
  - [Ocamlnet](http://projects.camlcity.org/projects/ocamlnet.html)
有许多相关的网络库 -
[Nethtml](http://projects.camlcity.org/projects/dl/ocamlnet-4.0.4/doc/html-main/Nethtml.html)
html 解析器,
[Netasn1](http://projects.camlcity.org/projects/dl/ocamlnet-4.0.4/doc/html-main/Netasn1.html)
对于 ASN.1 解析，
[网络编码](http://projects.camlcity.org/projects/dl/ocamlnet-4.0.4/doc/html-main/Netencoding.html)
对于 Base64、引用的可打印、URL 编码和 HTML 转义，
[Netmime](http://projects.camlcity.org/projects/dl/ocamlnet-4.0.4/doc/html-main/Netmime.html)
用于 MIME 处理等。请参阅 [列表
模块](http://projects.camlcity.org/projects/dl/ocamlnet-4.0.4/doc/html-main/index.html)
在 Ocamlnet 的手册中。
  - [tyxml](http://ocsigen.org/tyxml) - 用于构建有效（根据 W3C 规范）Html 和 Svg 树的库。
  - [js_of_ocaml](http://ocsigen.org/js_of_ocaml) - js_of_ocaml 是 OCaml 字节码到 Javascript 的编译器。它使得在 Web 浏览器中运行 Ocaml 程序成为可能。
    - [commonjs_of_ocaml](https://github.com/AngryLawyer/commonjs_of_ocaml) - 从 js_of_ocaml 项目轻松导入和导出 CommonJS 模块。
  - [ReScript](https://rescript-lang.org/) - ReScript 是一种强大的类型语言，可以编译为高效且人类可读的 JavaScript。
  - [ocaml-uri](https://github.com/mirage/ocaml-uri) - RFC3986 URI 解析库。
  - [Goji](https://github.com/klakplok/goji) - JavaScript 库的 OCaml 绑定生成器。
  - [Syndic](https://github.com/Cumulus/Syndic) - RSS 和 Atom feed 解析
  - [ocaml-mustache](https://github.com/rgrinberg/ocaml-mustache) - OCaml 中的 Mustache.js 无逻辑模板。
  - [atdjs](https://github.com/barko/atdjs) - OCaml/js_of_ocaml 的 atd 代码生成器（序列化）。
  - [jingoo](https://github.com/tategakibunko/jingoo) - OCaml 模板引擎几乎与 jinja2 兼容。
  - [dispatch](https://github.com/inhabitedtype/ocaml-dispatch) - 客户端和服务器端应用程序的基于路径的调度。
  - [Lambda Soup](https://github.com/aantron/lambda-soup) - 使用 CSS 选择器进行功能性 HTML 抓取和操作，就像 Python 的 Beautiful Soup 一样。
  - [Markup.ml](https://github.com/aantron/markup.ml) - 错误恢复流式 HTML5 和 XML 解析器、序列化器。
  - [gen_js_api](https://github.com/LexiFi/gen_js_api) - gen_js_api 旨在简化 Javascript 库的 OCaml 绑定的创建。
  - [routes](https://github.com/anuragsoni/routes) - OCaml/ReasonML Web 应用程序的类型化路由。

- **开源项目**：
  - [Cumulus](https://github.com/Cumulus/Cumulus) - 黑客新闻，例如使用 OCaml 框架 Ocsigen 的网站

* * *

_灵感来自于很棒的项目系列。发现[更多精彩](https://github.com/bayandin/awesome-awesomeness) :sparkles:._
