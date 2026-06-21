很棒的Haskell [！[很棒](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
=============

很棒的 Haskell 链接、框架、库和软件的辅助列表。 [awesome](https://github.com/sindresorhus/awesome) 项目线的一部分。

- [很棒的哈斯克尔](#awesome-haskell)
    - [_Basics_](#basics)
    - [Algorithmics](#algorithmics)
    - [音频、音乐和声音](#audio-music--sound)
    - [范畴论](#category-theory)
    - [Compilers](#compilers)
    - [并发与并行](#concurrency--parallelism)
    - [Configuration](#configuration)
    - [密码学和散列](#cryptography--hashing)
    - [数据存取](#data-access)
    - [数据格式](#data-formats)
    - [数据科学](#data-science)
    - [数据结构](#data-structures)
    - [Database](#database)
    - [开发工具](#development-tools)
    - [Documentation](#documentation)
    - [分布式计算](#distributed-computing)
    - [Editors](#editors)
    - [Extensions](#extensions)
    - [Games](#games)
    - [GUI](#gui)
    - [Graphics](#graphics)
    - [Network](#network)
    - [数论](#number-theory)
    - [网络/框架](#web--frameworks)
    - [文本处理](#text-processing)
    - [Messaging](#messaging)
    - [Languages](#languages)
    - [操作系统](#operating-systems)
    - [Platforms](#platforms)
    - [Programming](#programming)
    - [Science](#science)
    - [流处理](#streaming-processing)
- [Resources](#resources)
    - [Websites](#websites)
    - [Bloggers](#bloggers)    
    - [Community](#community)
    - [Tutorials](#tutorials)
    - [Courses](#courses)
    - [Conferences](#conferences)
    - [Packages](#packages)
- [License](#license)


## _基础知识_

* [Alex](https://www.haskell.org/alex/) - Haskell 的词法分析器生成器。
* [Cabal](https://www.haskell.org/cabal/) - 用于构建和打包 Haskell 库和程序的系统。
* [GHC](https://www.haskell.org/ghc/) - 最先进的 Haskell 优化本机代码编译器。
* [GHCi](https://downloads.haskell.org/~ghc/latest/docs/html/users_guide/ghci.html) - Haskell 的字节码解释器和交互式 REPL 环境。
* [GHCup](https://www.haskell.org/ghcup) - GHCup 是通用语言 Haskell 的主要安装程序。
* [Hackage](http://hackage.haskell.org/) - Haskell 社区的中央包存档。
* [Haddock](https://www.haskell.org/haddock/) - 一个从带注释的 Haskell 源代码自动生成文档的工具。
* [Happy](https://www.haskell.org/happy/) - Haskell 的解析器生成器。
* [Hayoo](http://hayoo.fh-wedel.de/) - 将搜索 Hackage 中的所有包，包括所有函数和类型定义。
* [Hoogle](https://www.haskell.org/hoogle/) - Haskell API 搜索引擎，允许您通过函数名称或近似类型签名来搜索许多标准 Haskell 库。
* [hsenv](https://github.com/Paczesiowa/hsenv/) - 创建隔离的 Haskell 环境的工具。这允许项目使用与当前安装的 GHC 版本不同的 GHC 版本。
* [Stack](https://github.com/commercialhaskell/stack) - 帮助构建 Haskell 项目的跨平台工具。它支持创建隔离的 Haskell 环境并自动管理项目的依赖项。
* [Stackage](https://github.com/fpco/stackage) - “Stable Hackage”，用于从 Hackage 创建一组经过审查的软件包的工具。

## 算法学

* [Theorem Provers](https://wiki.haskell.org/Applications_and_libraries/Theorem_provers) - 官方网站资源。

    ---
* [Algorithm](http://hackage.haskell.org/packages/#cat:Algorithm) - 协作 Hackage 列表。
* [Algorithm Visualization](http://hackage.haskell.org/packages/#cat:Algorithm%20Visualization) - 协作 Hackage 列表。
* [Algorithms](http://hackage.haskell.org/packages/#cat:Algorithms) - 协作 Hackage 列表。
* [Compression](http://hackage.haskell.org/packages/#cat:Compression) - 协作 Hackage 列表。
* [Formal Languages](http://hackage.haskell.org/packages/#cat:Formal%20Languages) - 协作 Hackage 列表。
* [Formal Methods](http://hackage.haskell.org/packages/#cat:Formal%20Methods) - 协作 Hackage 列表。
* [Logic](http://hackage.haskell.org/packages/#cat:Logic) - 协作 Hackage 列表。
* [Logic Programming](http://hackage.haskell.org/packages/#cat:Logic%20Programming) - 协作 Hackage 列表。
* [Map Reduce](http://hackage.haskell.org/packages/#cat:MapReduce) - 协作 Hackage 列表。
* [Graphs](http://hackage.haskell.org/packages/#cat:Graphs) - 协作 Hackage 列表。
* [Optimization](http://hackage.haskell.org/packages/#cat:Optimization) - 协作 Hackage 列表。
* [Simulation](http://hackage.haskell.org/packages/#cat:Simulation) - 协作 Hackage 列表。
* [SMT](http://hackage.haskell.org/packages/#cat:SMT) - 可满足性模理论 (SMT) 的协作 Hackage 列表。
* [Symbolic Computation](http://hackage.haskell.org/packages/#cat:Symbolic%20Computation) - 协作 Hackage 列表。
* [Theorem Provers](http://hackage.haskell.org/packages/#cat:Theorem%20Provers) - 协作 Hackage 列表。

## 音频、音乐和声音

* [Audio, music and sound](https://wiki.haskell.org/Applications_and_libraries/Music_and_sound) - 官方网站资源。

    ---
* [Audio](http://hackage.haskell.org/packages/#cat:Audio) - 协作 Hackage 列表。
* [Codec](http://hackage.haskell.org/packages/#cat:Codec) - 协作 Hackage 列表。
* [Graphics](http://hackage.haskell.org/packages/#cat:Graphics) - 协作 Hackage 列表。
* [Media](http://hackage.haskell.org/packages/#cat:Media) - 协作 Hackage 列表。
* [Music](http://hackage.haskell.org/packages/#cat:Music) - 协作 Hackage 列表。
* [Sound](http://hackage.haskell.org/packages/#cat:Sound) - 协作 Hackage 列表。


## 范畴论

* [Adjunctions](http://hackage.haskell.org/packages/#cat:Adjunctions) - 协作 Hackage 列表。
* [Algebra](http://hackage.haskell.org/packages/#cat:Algebra) - 协作 Hackage 列表。
* [Categories](http://hackage.haskell.org/packages/#cat:Categories) - 协作 Hackage 列表。
* [Combinators](http://hackage.haskell.org/packages/#cat:Combinators) - 协作 Hackage 列表。
* [Comonads](http://hackage.haskell.org/packages/#cat:Comonads) - 协作 Hackage 列表。
* [Composition](http://hackage.haskell.org/packages/#cat:Composition) - 协作 Hackage 列表。
* [Computer Algebra](http://hackage.haskell.org/packages/#cat:Computer%20Algebra) - 协作 Hackage 列表。
* [Constraints](http://hackage.haskell.org/packages/#cat:Constraints) - 协作 Hackage 列表。
* [Functors](http://hackage.haskell.org/packages/#cat:Functors) - 协作 Hackage 列表。
* [Monad](http://hackage.haskell.org/packages/#cat:Monad) - 协作 Hackage 列表。
* [Monads](http://hackage.haskell.org/packages/#cat:Monads) - 协作 Hackage 列表。
* [Semigroups](http://hackage.haskell.org/packages/#cat:Semigroups) - 协作 Hackage 列表。

## 编译器

* [Compilers & Interpreters](https://wiki.haskell.org/Applications_and_libraries/Compilers_and_interpreters) - 官方网站资源。
* [Compiler construction, lexing, parsing, pretty printing](https://wiki.haskell.org/Applications_and_libraries/Compiler_tools) - 官方网站资源。

    ---
* [Compiler](http://hackage.haskell.org/packages/#cat:Compiler) - 协作 Hackage 列表。
* [Compiler Plugin](http://hackage.haskell.org/packages/#cat:Compiler%20Plugin) - 协作 Hackage 列表。
* [Compilers/Interpreters](http://hackage.haskell.org/packages/#cat:Compilers/Interpreters) - 协作 Hackage 列表。

## 并发与并行

* [Concurrency & Parallelism](https://wiki.haskell.org/Applications_and_libraries/Concurrency_and_parallelism) - 官方网站信息。

    ---
* [Concurrency](http://hackage.haskell.org/packages/#cat:Concurrency) - 协作 Hackage 列表。
* [Concurrent](http://hackage.haskell.org/packages/#cat:Concurrent) - 协作 Hackage 列表。
* [Functional Reactive Programming](http://hackage.haskell.org/packages/#cat:FRP) - 协作 Hackage 列表。
* [Parallelism](http://hackage.haskell.org/packages/#cat:Parallelism) - 协作 Hackage 列表。

    ---
* [Concurrency & Parallelism](http://chimera.labs.oreilly.com/books/1230000000929/index.html) - （书籍）Haskell 中的并行和并发编程

## 配置

* [Deiko-config](http://hackage.haskell.org/package/deiko-config) - 使用 [HOCON](https://github.com/lightbend/config#features-of-hocon) 配置格式的小型类型安全库
* [Dhall](https://github.com/dhall-lang/dhall-haskell) - 保证终止的配置语言
* [Configurator](http://hackage.haskell.org/package/configurator) - 一个配置管理库，支持自动动态重新加载以响应配置文件的修改。

## 密码学和散列

* [Cryptography & Hashing](https://wiki.haskell.org/Applications_and_libraries/Cryptography) - 官方网站资源。

    ---
* [Crypto](http://hackage.haskell.org/packages/#cat:Crypto) - 协作 Hackage 列表。
* [Cryptography](http://hackage.haskell.org/packages/#cat:Cryptography) - 协作 Hackage 列表。


## 数据存取

* [Haxl](https://github.com/facebook/Haxl) - 一个用于高效、并发、简洁的数据访问的库。

## 数据格式

* [JSON](http://hackage.haskell.org/packages/#cat:JSON) - 协作 Hackage 列表。
* [PDF](http://hackage.haskell.org/packages/#cat:PDF) - 协作 Hackage 列表。
* [XML](http://hackage.haskell.org/packages/#cat:XML) - 协作 Hackage 列表。
* [RSS](http://hackage.haskell.org/packages/#cat:RSS) - 协作 Hackage 列表。

## 数据科学
* [Linguistics and natural language processing](https://wiki.haskell.org/Applications_and_libraries/Linguistics) - 官方网站资源。
* [Robotics](https://wiki.haskell.org/Applications_and_libraries/Robotics) - 官方网站资源。

    ---
* [Artificial Intelligence](http://hackage.haskell.org/packages/#cat:AI) - 协作 Hackage 列表。
* [Argumentations](http://hackage.haskell.org/packages/#cat:Argumentation) - 协作 Hackage 列表。
* [Classification](http://hackage.haskell.org/packages/#cat:Classification) - 协作 Hackage 列表。
* [Clustering](http://hackage.haskell.org/packages/#cat:Clustering) - 协作 Hackage 列表。
* [Data Mining](http://hackage.haskell.org/packages/#cat:Data%20Mining) - 协作 Hackage 列表。
* [Datamining](http://hackage.haskell.org/packages/#cat:Datamining) - 协作 Hackage 列表。
* [Image Processing](http://hackage.haskell.org/packages/#cat:Image%20Processing) - 协作 Hackage 列表。
* [Machine Learning](http://hackage.haskell.org/packages/#cat:Machine%20Learning) - 协作 Hackage 列表。
* [Machine Vision](http://hackage.haskell.org/packages/#cat:Machine%20Vision) - 协作 Hackage 列表。
* [Natural Language Processing](http://hackage.haskell.org/packages/#cat:Natural%20Language%20Processing) - 协作 Hackage 列表。
* [Pattern Classification](http://hackage.haskell.org/packages/#cat:Pattern%20Classification) - 协作 Hackage 列表。
* [Pattern Recognition](http://hackage.haskell.org/packages/#cat:Pattern%20Recognition) - 协作 Hackage 列表。
* [Search](http://hackage.haskell.org/packages/#cat:Search) - 协作 Hackage 列表。
* [Statistics](http://hackage.haskell.org/packages/#cat:Statistics) - 协作 Hackage 列表。
* [Text Recognition](http://hackage.haskell.org/packages/#cat:Text%20Recognition) - 协作 Hackage 列表。
* [Robotics](http://hackage.haskell.org/packages/#cat:Robotics) - 协作 Hackage 列表。

    ---
*附加库*
* [m2cgen](https://github.com/BayesWitnesses/m2cgen) - 一个 CLI 工具，用于将经过训练的经典 ML 模型转换为零依赖的本机 Haskell 代码。

## 数据结构
* [Data Structures & IO Libraries](https://wiki.haskell.org/Applications_and_libraries/Data_structures) - 官方网站资源。

    ---
* [Advanced Structures](http://hackage.haskell.org/packages/#cat:Structures) - 协作 Hackage 列表。
* [Bit Vectors](http://hackage.haskell.org/packages/#cat:Bit%20Vectors) - 协作 Hackage 列表。
* [Containers](http://hackage.haskell.org/packages/#cat:Containers) - 协作 Hackage 列表。
* [Data Structures](http://hackage.haskell.org/packages/#cat:Data%20Structures) - 协作 Hackage 列表。
* [Enumerator](http://hackage.haskell.org/packages/#cat:Enumerator) - 协作 Hackage 列表。
* [Generics](http://hackage.haskell.org/packages/#cat:Generics) - 协作 Hackage 列表。
* [List](http://hackage.haskell.org/packages/#cat:List) - 协作 Hackage 列表。
* [Tree](http://hackage.haskell.org/packages/#cat:Tree) - 协作 Hackage 列表。
* [Vector](http://hackage.haskell.org/packages/#cat:Vector) - 协作 Hackage 列表。

## 数据库
* [Database Interfaces](https://wiki.haskell.org/Applications_and_libraries/Database_interfaces) - 官方网站资源。

    ---
* [Database](http://hackage.haskell.org/packages/#cat:Database) - 协作 Hackage 列表。

## 开发工具
* [Development Libraries and Tools](https://wiki.haskell.org/Development_Libraries_and_Tools) - 官方网站资源。

    ---
* [Debug](http://hackage.haskell.org/packages/#cat:Debug) - 协作 Hackage 列表。
* [IDE](http://hackage.haskell.org/packages/#cat:IDE) - 协作 Hackage 列表。
* [Test](http://hackage.haskell.org/packages/#cat:Test) - 协作 Hackage 列表。
* [Testing](http://hackage.haskell.org/packages/#cat:Testing) - 协作 Hackage 列表。
* [Logging](http://hackage.haskell.org/packages/#cat:Logging) - 协作 Hackage 列表。
* [CLI Tool](http://hackage.haskell.org/packages/#cat:CLI%20Tool) - 协作 Hackage 列表。
* [Monitoring](http://hackage.haskell.org/packages/#cat:Monitoring) - 协作 Hackage 列表。

## 分布式计算

* [Distributed Computing](http://hackage.haskell.org/packages/#cat:Distributed%20Computing) - 协作 Hackage 列表。

    ---
* [Cloud Haskell](http://haskell-distributed.github.io/) - Haskell 中的并发和分布式编程。


## 文档

* [Documentation](http://hackage.haskell.org/packages/#cat:Documentation) - 协作 Hackage 列表。

## 编辑

* [Editors written in Haskell](https://wiki.haskell.org/Applications_and_libraries/Editors) - 官方网站资源。
* [editors for Haskell](https://wiki.haskell.org/Editors) - 官方网站资源。

## 扩展

* [Extended Haskell](https://wiki.haskell.org/Applications_and_libraries/Extended_Haskell) - 官方网站资源。

## 游戏
* [Games](https://wiki.haskell.org/Applications_and_libraries/Games) - 官方网站资源。

    ---
* [Game](http://hackage.haskell.org/packages/#cat:Game) - 协作 Hackage 列表。
* [Game Engine](http://hackage.haskell.org/packages/#cat:Game%20Engine) - 协作 Hackage 列表。

## 图形用户界面
* [Graphical User Interface (GUI) Libraries](https://wiki.haskell.org/Applications_and_libraries/GUI_libraries) - 官方网站资源。

    ---
* [GUI](http://hackage.haskell.org/packages/#cat:GUI) - 协作 Hackage 列表。
* [User Interfaces](http://hackage.haskell.org/packages/#cat:User%20Interfaces) - 协作 Hackage 列表。

## 图形
* [Graphics](https://wiki.haskell.org/Applications_and_libraries/Graphics) - 官方网站资源。

    ---
* [Graphics](http://hackage.haskell.org/packages/#cat:Graphics) - 协作 Hackage 列表。

## 网络

* [Network](https://wiki.haskell.org/Applications_and_libraries/Network) - 官网资源

    ---
* [Network](http://hackage.haskell.org/packages/#cat:Network) - 协作 Hackage 列表。

## 数论

* [Number Theory](http://hackage.haskell.org/packages/#cat:Number%20Theory) - 协作 Hackage 列表。
* [Numeric](http://hackage.haskell.org/packages/#cat:Numeric) - 协作 Hackage 列表。
* [Numerical](http://hackage.haskell.org/packages/#cat:Numerical) - 协作 Hackage 列表。
* [Math](http://hackage.haskell.org/packages/#cat:Math) - 协作 Hackage 列表。


## 网络/框架

* [Web Servers](https://wiki.haskell.org/Web/Servers) - 官方网站资源。
* [Web Frameworks](https://wiki.haskell.org/Web/Frameworks) - 官方网站资源。
* [Cloud](https://wiki.haskell.org/Web/Cloud) - 官方网站资源。
* [Deploy](https://wiki.haskell.org/Web/Deploy) - 官方网站资源。
* [Libraries](https://wiki.haskell.org/Web/Libraries) - 官方网站资源。
* [框架接口]() - 官方网站资源。
* [Database and Persistence](https://wiki.haskell.org/Web/Databases_and_Persistence) - 官方网站资源。
* [Testing and Verification](https://wiki.haskell.org/Web/Testing_and_Verification) - 官方网站资源。
* [CMS](https://wiki.haskell.org/Web/Content_Management) - 内容管理系统 (CMS) 的官方网站资源。
* [IHP: Integrated Haskell Platform](https://ihp.digitallyinduced.com/) - 开始使用 haskell web dev 的最佳方式。
    ---
* [Web](http://hackage.haskell.org/packages/#cat:Web) - 框架、库等的协作 Hackage 列表...

    ---
*附加库*
* [HTTP](https://github.com/haskell/HTTP) - Haskell HTTP 包。支持 Haskell 中的客户端 Web 编程。
* [hoauth2](https://github.com/freizl/hoauth2) - 一个轻量级的 oauth2 haskell 绑定。

## 文本处理

* [Pandoc](http://pandoc.org/) - 是一个用于从一种标记格式转换为另一种标记格式的库，以及使用该库的命令行工具。


## 消息传递

* [SimpleX Chat](https://github.com/simplex-chat/simplex-chat) - 第一个设计为 100% 私密的聊天平台 - 它无法访问您的连接图！
* [Stomp](http://stomp.github.io/) - 是简单（或流）文本导向的消息传递协议。 [资源](http://hackage.haskell.org/packages/#cat:Stomp)。
* [amqp](https://github.com/hreinhardt/amqp) - AMQP 服务器的客户端库（目前只有 RabbitMQ）。
* [IRC](http://hackage.haskell.org/packages/#cat:IRC) - 互联网中继聊天 (IRC) 的协作 Hackage 列表。
* [IRC Client](http://hackage.haskell.org/packages/#cat:IRC Client) - 协作 Hackage 列表。

## 语言

* [Tools for interfacing with other languages](https://wiki.haskell.org/Applications_and_libraries/Interfacing_other_languages) - 官方网站资源。

    ---
* [Code Generation](http://hackage.haskell.org/packages/#cat:Code%20Generation) - 协作 Hackage 列表。
* [FFI](http://hackage.haskell.org/packages/#cat:FFI) - 协作 Hackage 列表。
* [FFI Tools](http://hackage.haskell.org/packages/#cat:FFI%20Tools) - 协作 Hackage 列表。
* [HTML](http://hackage.haskell.org/packages/#cat:HTML) - 协作 Hackage 列表。
* [Java](http://hackage.haskell.org/packages/#cat:Java) - 协作 Hackage 列表。
* [Javascript](http://hackage.haskell.org/packages/#cat:Javascript) - 协作 Hackage 列表。
* [LaTex](http://hackage.haskell.org/packages/#cat:LaTeX) - 协作 Hackage 列表。
* [Lua](http://hackage.haskell.org/packages/#cat:LUA) - 协作 Hackage 列表。

    ---
*Haskell 之上的其他语言*
* [Fay](http://fay-lang.org/) - 编译为 JavaScript 的 Haskell 的适当子集。
* [Idris](https://github.com/idris-lang/Idris-dev) - 一种依赖类型的函数式编程语言
* [Copilot](http://leepike.github.io/Copilot/) - 用于生成硬实时 C 代码的 (Haskell DSL) 流语言。
* [Wasp](https://wasp-lang.dev/) - 一种简单的语言，用于使用更少的代码开发全栈 Javascript Web 应用程序（使用 Haskell 构建）

## 操作系统

* [Operating systems and systems programming](https://wiki.haskell.org/Applications_and_libraries/Operating_system) - 官方网站资源。

    ---
* [BSD](http://hackage.haskell.org/packages/#cat:BSD) - 协作 Hackage 列表。
* [Fedora](http://hackage.haskell.org/packages/#cat:Fedora) - 协作 Hackage 列表。
* [Gentoo](http://hackage.haskell.org/packages/#cat:Gentoo) - 协作 Hackage 列表。
* [Linux](http://hackage.haskell.org/packages/#cat:Linux) - 协作 Hackage 列表。
* [System](http://hackage.haskell.org/packages/#cat:System) - 协作 Hackage 列表。

## 平台

* [.NET](http://hackage.haskell.org/packages/#cat:.NET) - 协作 Hackage 列表。
* [Apple](http://hackage.haskell.org/packages/#cat:Apple) - 协作 Hackage 列表。
* [JVM](http://hackage.haskell.org/packages/#cat:JVM) - 协作 Hackage 列表。
* [Mobile](http://hackage.haskell.org/packages/#cat:Mobile) - 协作 Hackage 列表。

## 编程

* [Generic Programming](https://wiki.haskell.org/Applications_and_libraries/Generic_programming) - 官方网站资源。

    ---
* [Aspect Oriented Programming](http://hackage.haskell.org/packages/#cat:Aspect%20Oriented%20Programming) - 协作 Hackage 列表。
* [Generic Programming](http://hackage.haskell.org/packages/#cat:Generics) - 协作 Hackage 列表。
* [Logic Programming](http://hackage.haskell.org/packages/#cat:Logic) - 协作 Hackage 列表。
* [Reactive Programming](http://hackage.haskell.org/packages/#cat:Reactivity) - 协作 Hackage 列表。
* [Visual Programming](http://hackage.haskell.org/packages/#cat:Visual%20Programming) - 协作 Hackage 列表。

## 科学

* [Bioinformatics](https://wiki.haskell.org/Applications_and_libraries/Bioinformatics) - 官方网站资源。
* [Mathematics & Physics](https://wiki.haskell.org/Applications_and_libraries/Mathematics) - 官方网站资源。

    ---
* [Chemistry](http://hackage.haskell.org/packages/#cat:Chemistry) - 协作 Hackage 列表。
* [Bioinformatics](http://hackage.haskell.org/packages/#cat:Bioinformatics) - 协作 Hackage 列表。
* [Finance](http://hackage.haskell.org/packages/#cat:Finance) - 协作 Hackage 列表。
* [Physics](http://hackage.haskell.org/packages/#cat:Physics) - 协作 Hackage 列表。
* [Science](http://hackage.haskell.org/packages/#cat:Science) - 协作 Hackage 列表。
* [Scientific Simulation](http://hackage.haskell.org/packages/#cat:Scientific%20Simulation) - 协作 Hackage 列表。

## 流处理

* [Conduit](https://github.com/snoyberg/conduit) - 流式数据库。 [资源](http://hackage.haskell.org/packages/#cat:Conduit)。
* [IO-Streams](http://hackage.haskell.org/packages/#cat:IO-Streams) - 协作 Hackage 列表。
* [Pipes](https://github.com/Gabriel439/Haskell-Pipes-Library) - 是一个干净而强大的流处理库，可让您构建和连接可重用的流组件。 [资源](http://hackage.haskell.org/packages/#cat:Pipes)。
* [HStreamDB](https://github.com/hstreamdb/hstream) - 专为物联网数据存储和实时处理而构建的流数据库。

# 资源

## 网站

* [Haskell](https://www.haskell.org/) - 官方网站。
* [The Haskell Programming Language](https://wiki.haskell.org/Haskell) - 哈斯克尔维基。
* [Try Haskell](http://tryhaskell.org/) - 哈斯克尔在线。
* [School of Haskell](https://www.schoolofhaskell.com/) - 学习哈斯克尔。

## 博主

* [Neil Mitchell](https://neilmitchell.blogspot.com/) - 尼尔·米切尔的 Haskell 博客。


## 社区

* [Community](https://www.haskell.org/community) - 官方社区资源。
* [Reddit](https://www.reddit.com/r/haskell/)
* [Stackoverflow](http://stackoverflow.com/questions/tagged?tagnames=haskell)
* [G+](https://plus.google.com/communities/104818126031270146189)
* [邮件列表](https://wiki.haskell.org/Mailing_lists)
* [IRC 频道](https://wiki.haskell.org/IRC_channel)
* [本地用户组](https://wiki.haskell.org/User_groups)
* [哈斯克尔星球](http://planet.haskell.org/)
* [Haskell 社区和活动报告](https://wiki.haskell.org/Haskell_Communities_and_Activities_Report)

## 教程

* [Documentation](https://www.haskell.org/documentation) - 官方文档资源。
* [Learn Haskell](https://wiki.haskell.org/Learning_Haskell) - 维基学习资源。
* [书籍](https://wiki.haskell.org/Books) & [教程](https://wiki.haskell.org/Tutorials)
* [learnhaskell](https://github.com/bitemyapp/learnhaskell) - Haskell Learning（也适用于非英语人士）。
* [What I Wish I Knew When Learning Haskell](http://dev.stephendiehl.com/hask/) - 各种事物的精彩指南。
* [LearnYouHaskell](http://learnyouahaskell.com/chapters) - 学习 Haskell 是为了大有裨益！
* [Happy Learn Haskell Tutorial](http://happylearnhaskelltutorial.com/) - 卡通机器人的无痛渐进 Haskell 教程！
* [Revised report](https://www.haskell.org/onlinereport/) - Haskell 98 语言和库。修订后的报告。
* [H-99](https://wiki.haskell.org/H-99:_Ninety-Nine_Haskell_Problems) - 九十九个哈斯克尔问题。

### 网络教程
    * [Haskell 简介 - 网络编程](http://www.shakthimaan.com/posts/2016/01/27/haskell-web-programming/news.html)
    * [您的第一个 Spock Web 应用程序](https://haskell-at-work.com/episodes/2018-04-09-your-first-web-application-with-spock.html)
    * [Scotty-Tutorials-&-Examples](https://github.com/scotty-web/scotty/wiki/Scotty-Tutorials-&-Examples)
    * [开始使用](https://www.spock.li/tutorials/getting-started)
    * [使用 Yesod 和 Haskell 开发 Web 应用程序](https://www.yesodweb.com/book-1.6)

### 视频教程

* [从头开始重做 Make - Haskell](http://www.youtube.com/playlist?list=PLxj9UAX4Em-Ij4TKwKvo-SLp-Zbv-hB4B)
* [Haskell - 代码解构](http://www.youtube.com/playlist?list=PLxj9UAX4Em-IBXkvcC3MycLlcxyoi7v8B)
* [Haskell 历险记 - 计算器](http://www.youtube.com/playlist?list=PL_xuff3BkASMOzBr0hKVKLuSnU4UIinKx)
* [Haskell 中的 Sed 实现](http://www.youtube.com/playlist?list=PLUQzXLQ6jvHL_k3QOMKXehVoZdk-sKtHd)
* [LazyCasts](http://www.youtube.com/user/LazyCasts)
* [Haskell 开发工作流程演示](http://www.youtube.com/watch?v=Li6oaO8x2VY)
* [Learn You a Haskell](https://www.youtube.com/watch?v=NBKnY7Z_w3I&list=PLPqPwGvHPSZB-urE6QFjKYt6AGXcZqJUh) - 《Learn You a Haskell for Great Good!》一书附带的视频讲座
* [Awesome Haskell Videos](https://github.com/andys8/awesome-haskell-videos) - Haskell 讲座和教程精选列表
* [IHP Casts](https://ihpcasts.com/ShowEpisode?episodeId=ab384647-3665-4a36-b5e5-e05fea6c2288) 学习使用 Haskell 和 IHP 构建类型安全的 Web 应用程序

## 课程

* [Introduction to Functional Programming](https://www.edx.org/course/introduction-functional-programming-delftx-fp101x-0) - 2014 年秋季 DelftX 在 edX 上推出的 MOOC，以 Haskell 为主要重点语言。
* [Functional Programming in Haskell](https://www.futurelearn.com/courses/functional-programming-haskell/) - 格拉斯哥大学推出的 Haskell 函数式编程入门 MOOC。
* [Haskell MOOC](https://haskell.mooc.fi/) - 赫尔辛基大学关于使用 Haskell 的函数式编程的 MOOC。

## 会议

* [ICFP](http://www.icfpconference.org/) - 国际函数式编程会议。 [Youtube 频道](https://www.youtube.com/channel/UCwRL68qZFfub1Ep1EScfmBw)。
* [Conferences](https://wiki.haskell.org/Conferences) - 官方会议列表
* [2015 年哈斯克尔研讨会](https://www.youtube.com/playlist?list=PLnqUlCo055hV5dPC-4VWeXzhI8ooeTsVy)
* [2015 年 Haskell 实施者研讨会](https://www.youtube.com/playlist?list=PLnqUlCo055hVfNkQHP7z43r10yNo-mc7B)

## 套餐

* [Stackage](https://www.stackage.org/) - 是 Haskell 软件包的稳定来源，“Stable Hackage”。
* [Hackage](http://hackage.haskell.org/) - 是 Haskell 社区的中央包存档。
* [Application & Libraries](https://wiki.haskell.org/Applications_and_libraries) - 官方收藏和指南。
* [Hoogle](https://www.haskell.org/hoogle/) - 是一个 Haskell API 搜索引擎，它允许您通过函数名称或近似类型签名来搜索许多标准 Haskell 库。
* [Hayoo](http://hayoo.fh-wedel.de/) - 将搜索 Hackage 中的所有包，包括所有函数和类型定义。

## 最佳实践
* [Haskell 风格指南](https://kowainik.github.io/posts/2019-02-06-style-guide)
# 许可证

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png)](http://creativecommons.org/publicdomain/zero/1.0/)
