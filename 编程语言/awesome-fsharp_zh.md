# 很棒的 F# <img src="https://fsharp.org/img/logo/fsharp.svg" width="48" height="48"align="right"/> [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

F# 是一种编程语言，专注于不变性、类型推断、一流的函数、强大的数据类型和模式匹配，面向 .NET 和其他平台。

这是一个精选的 F# 框架、库、软件和资源列表。

## 内容
- [主要语言相关存储库](#main-language-related-repositories)
- [流行 .NET 库的 F# 包装器](#f-wrappers-for-popular-net-libraries)
- [参与者框架](#actor-frameworks)
- [构建工具](#build-tools)
- [Cloud](#cloud)
- [代码分析](#code-analysis)
- [代码生成](#code-generation)
- [其他平台的编译器](#compilers-for-other-platforms)
- [并发、异步和并行编程](#concurrent-asynchronous-and-parallel-programming)
- [Configuration](#configuration)
- [数据科学](#data-science)
- [开发工具](#development-tools)
  - [IDE](#ide)
  - [编辑器插件](#editor-plugins)
  - [绩效分析](#performance-analysis)
- [通用库](#general-purpose-libraries)
- [游戏开发](#game-development)
- [GUI](#gui)
- [HTTP 客户端](#http-clients)
- [Logging](#logging)
- [包管理](#package-management)
- [Parsing](#parsing)
- [Serialization](#serialization)
- [Simulation](#simulation)
- [静态站点生成器](#static-site-generators)
- [Testing](#testing)
- [类型提供者](#type-providers)
  - [创建类型提供者](#creating-type-providers)
- [Visualization](#visualization)
- [网络框架](#web-frameworks)
- [.NET 核心模板](#net-core-templates)
- [Resources](#resources)
  - [Blogs](#blogs)
  - [Books](#books)
  - [Cheatsheets](#cheatsheets)
  - [Community](#community)
  - [其他清单](#other-lists)
  - [Websites](#websites)
  - [Videos](#videos)
  - [Courses](#courses)

## 主要语言相关存储库

- [F# 主存储库](https://github.com/dotnet/fsharp)
- [F# 项目](https://github.com/fsprojects)
- [F#建议](https://github.com/fsharp/fslang-suggestions)
- [F# RFC](https://github.com/fsharp/fslang-design)

## 流行 .NET 库的 F# 包装器
希望在使用流行的 .NET 库时获得更愉快的体验？这是一个快速表。

<!-- The following table includes some entries that are duplicated in the list below. This is by design. -->  
<!--lint disable double-link -->
|.NET 库 |F# 包装器 |
|---------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|[ASP.NET Core Blazor](https://github.com/dotnet/aspnetcore/tree/main/src/Components) |[Bolero](https://github.com/fsbolero/Bolero) |
|[ASP.NET Core](https://github.com/dotnet/aspnetcore) |[Giraffe](https://github.com/giraffe-fsharp/Giraffe)（+ 可选 [Saturn](https://github.com/SaturnFramework/Saturn))<br/>[Oxpecker](https://github.com/Lanayx/Oxpecker)|
|[Avalonia](https://github.com/AvaloniaUI/Avalonia) |[Avalonia.FuncUI](https://github.com/fsprojects/Avalonia.FuncUI) |
|[MAUI](https://github.com/dotnet/maui)/[Xamarin.Forms](https://github.com/xamarin/Xamarin.Forms) |[Fabulous](https://github.com/fabulous-dev/Fabulous) |
|[MSTest](https://github.com/microsoft/testfx)/[NUnit](https://github.com/nunit/nunit)/[xUnit.net](https://github.com/xunit/xunit)|[FsUnit](https://github.com/fsprojects/FsUnit) |
|[System.Text.Json](https://github.com/dotnet/runtime/tree/main/src/libraries/System.Text.Json) |[FSharp.SystemTextJson](https://github.com/Tarmil/FSharp.SystemTextJson) |
|[WPF](https://github.com/dotnet/wpf) |[Elmish.WPF](https://github.com/elmish/Elmish.WPF) |

<!--lint enable double-link -->

## 参与者框架

- [Akka.NET](https://github.com/akkadotnet/akka.net) - 社区驱动的流行 Java/Scala 框架 Akka 到 .NET 的移植。
- [Akkling](https://github.com/Horusiath/Akkling) - Akka.NET 的 F# 类型 API。
- [Orleankka](https://github.com/OrleansContrib/Orleankka) - Microsoft Orleans 框架的功能扩展。
- [Orleans](https://github.com/dotnet/orleans) - 分布式虚拟演员模型。
- [Proto.actor](https://github.com/AsynkronIT/protoactor-dotnet) - 适用于 .NET、Go、Java 和 Kotlin 的跨平台 Actor 框架。

## 构建工具

- [FAKE](https://github.com/fsharp/FAKE) - “F# Make”是一个跨平台构建自动化系统。
- [Xake](https://github.com/OlegZee/Xake) - F# 上的另一个 Make 实用程序实现，完全声明性且无脑并行，受到 Shake 的启发。

## 云

- [Chia](https://github.com/DanpowerGruppe/Chia) - 一个 F# 库，其中包含用于报告、日志记录和 Azure 云操作的 HelperFunctions。
- [Farmer](https://github.com/CompositionalIT/farmer) - 使用 ARM 模板可轻松进行可重复的 Azure 部署。
- [FsFirestore](https://github.com/mrbandler/FsFirestore) - 用于访问 Google Cloud Platform (GCP) 或 Firebase 上托管的 Firestore 数据库的功能 F# 库。
- [Pulumi.FSharp.Extensions](https://github.com/UnoSD/Pulumi.FSharp.Extensions) - F# 计算表达式可减少 Pulumi 代码中的样板代码。

## 代码分析
- [Ionide FSharp.Analyzers.SDK](https://github.com/ionide/FSharp.Analyzers.SDK) - 用于为 F# / FSharp.Analyzers.Cli 构建自定义分析器的库。

## 代码生成

- [Hawaii](https://github.com/Zaid-Ajaj/Hawaii) - 一个 dotnet CLI 工具，用于从 OpenAPI/Swagger 服务生成类型安全的 F# 客户端。
- [Myriad](https://github.com/MoiraeSoftware/myriad) - 预编译代码生成器。

## 其他平台的编译器

- [Fable](https://github.com/fable-compiler/Fable) - F# 到 JavaScript 编译器。
- [Fez](https://github.com/kjnilsson/fez) - F# 到 Erlang 编译器。
- [FunScript](https://github.com/ZachBray/FunScript) - F# 到 JavaScript 编译器，通过 TypeScript 类型提供程序进行 JQuery 等映射。
- [Juniper](https://github.com/calebh/Juniper) - 适用于 Arduino 和其他微控制器的函数式反应式编程。

## 并发、异步和并行编程

- [FIO](https://github.com/iyyel/fio) - 基于纯函数式编程的类型安全、高并发、异步的 F# 库。
- [FSharp.Control.AsyncSeq](https://github.com/fsprojects/FSharp.Control.AsyncSeq) - 异步序列支持，与“IAsyncEnumerable”集成。
- [FSharp.Control.FusionTasks](https://github.com/kekyo/FSharp.Control.FusionTasks) - F# 异步工作流 <--> .NET Task/ValueTask 轻松无缝互操作性库。
- [FSharpx.Async](https://github.com/fsprojects/FSharpx.Async) - F# 异步编程实用程序集合。
- [Hopac](https://github.com/Hopac/Hopac) - F# 的并发 ML 风格并发编程库。
- [IcedTasks](https://github.com/TheAngryByrd/IcedTasks) - 冷任务、可取消任务以及“异步”工作流程的扩展。
- [Ply](https://github.com/crowded/ply) - F# 的高性能 System.Threading.(Value)Task 计算表达式。
- [Reaction.AsyncRx](https://github.com/dbrattli/Reaction) - F# 中针对 .NET 和 Fable 的异步 Observables 实现。
- [TaskBuilder.fs](https://github.com/rspeele/TaskBuilder.fs) - System.Threading.Tasks 的 F# 计算表达式生成器。

## 配置

- [Argu](https://github.com/fsprojects/Argu) - F# 应用程序的声明性 CLI 参数/XML 配置解析器。
- [FsConfig](https://github.com/demystifyfp/FsConfig) - F# 库，用于从环境变量和 AppSettings 中读取类型安全的配置数据。
- [Skid](https://github.com/Meyhem/Skid) - 用于配置模板的简单、单文件便携式 CLI 实用程序。
- [docopt.fs](https://github.com/docopt/docopt.fs/) - 命令行参数解析器，[docopt](https://github.com/docopt/docopt) 的 F# 端口。

## 数据科学

- [Deedle](https://github.com/BlueMountainCapital/Deedle) - .NET 探索性数据库。
- [DiffSharp](https://github.com/DiffSharp/DiffSharp) - 功能自动微分（AD）库。
- [FsLab](https://github.com/fslaborg/FsLab) - 数据科学库的集合。它提供了一个快速开发环境，使您可以使用几行生产质量的代码编写高级分析。
- [IfSharp](https://github.com/fsprojects/IfSharp) - 适用于 Jupyter 笔记本的 F#。
- [Math.NET Numerics](https://github.com/mathnet/mathnet-numerics) - 科学、工程和日常使用中数值计算的方法和算法。 F# 特定绑定可用。
- [Math.NET Symbolics](https://github.com/mathnet/mathnet-symbolics/) - 完全用 F# 编写的适用于 .NET、Silverlight 和 Mono 的基本开源计算机代数库。
- [SIMDArray](https://github.com/jackmott/SIMDArray) - SIMD 增强了数组扩展，可实现更快的计算。
- [Synapses](https://github.com/mrdimosthenis/Synapses) - F# 中的神经网络库。
- [m2cgen](https://github.com/BayesWitnesses/m2cgen) - 一个 CLI 工具，用于将经过训练的经典 ML 模型转换为零依赖的本机 F# 代码。

## 开发工具

### 集成开发环境

- [F# Playground](https://github.com/Seng-Jik/FSharpPlayground) - F# 的最小游乐场。
- [JetBrains Rider](https://www.jetbrains.com/rider) - 支持 F# 的跨平台 .NET IDE（专有，免费供非商业用途）。
- [MonoDevelop](http://www.monodevelop.com/) - 跨平台 IDE 主要针对 Mono/.NET 开发人员。
- [Visual Studio](https://www.visualstudio.com/) - 来自 Microsoft 的 IDE，具有一流的 F# 支持（仅限 Windows，专有）。

### 编辑器插件

- [Emacs F# mode](https://github.com/fsharp/emacs-fsharp-mode) - Emacs 中的 F# 支持（包括智能感知和交互模式）。
- [FSharpFar](https://github.com/nightroman/FarNet) - F# 对 Far Manager 的支持。
- [FSharpLint](https://github.com/fsprojects/FSharpLint) - F# 代码检查。
- [Fantomas](https://github.com/fsprojects/fantomas) - F# 代码格式化程序。
- [Ionide](http://ionide.io/) - 用于跨平台 F# 开发的 Atom Editor 和 Visual Studio Code 软件包套件。
- [Vim F#](https://github.com/fsharp/vim-fsharp) - F# 对 Vim 的支持。
- [VimSpeak](https://github.com/AshleyF/VimSpeak) - 一个使用语音识别来控制 Vim 的工具。
- [fsharp-notebook](https://github.com/pablofrommars/fsharp-notebook) - F# Interactive 的数据科学笔记本。
- [neofsharp.vim](https://github.com/adelarsq/neofsharp.vim) - (Neo)Vim 的基本 F# 支持。

### 绩效分析

- [fasm](https://github.com/d-edge/fasm) - F# JIT 反汇编器，作为 dotnet 工具。

## 通用库

- [Aether](https://github.com/xyncro/aether) - F# 的光学库，类似于 Haskell Data.Lens 包。
- [Chessie](https://github.com/fsprojects/Chessie) - 面向铁路的编程。
- [Donald](https://github.com/pimbrouwers/Donald) - ADO.NET 的简单 F# 接口。
- [DustyTables](https://github.com/Zaid-Ajaj/DustyTables) - SqlClient 的精简 F# API，可通过顶部的功能调节轻松访问 MS sql 服务器的数据。
- [ExtCore](https://github.com/jack-pappas/ExtCore) - F# 的扩展核心库。
- [FSharp.CosmosDb](https://github.com/aaronpowell/fsharp.cosmosdb) - CosmosDB SDK 的 F# 包装器，使其功能更加友好。
- [FSharp.HashCollections](https://github.com/mvkara/fsharp-hashcollections) - 基于快速哈希的不可变映射和集合。
- [FSharpLu](https://github.com/Microsoft/fsharplu) - 用于字符串操作、日志记录、集合数据结构、文件操作、文本处理、安全、异步、解析、诊断、配置文件和 Json 序列化的轻量级实用程序。
- [FSharpPlus](https://github.com/gmpl/FSharpPlus) - F# 的扩展。
- [FSharpx.Extras](https://github.com/fsprojects/FSharpx.Extras) - 用于 F# 的库和工具的集合。
- [Fli](https://github.com/CaptnCodr/Fli) - 用于运行系统进程并管理其输出的计算表达式。
- [Fling](https://github.com/cmeeren/Fling) - 显着减少将复杂域实体有效保存到多个表或从多个表加载复杂域实体所需的样板。
- [FsToolkit.ErrorHandling](https://github.com/demystifyfp/FsToolkit.ErrorHandling) - 通过面向铁路的编程进行清晰、简单且强大的错误处理。灵感来自切西。
- [Fumble](https://github.com/tforkmann/Fumble) - 适用于 SQLite 的精简 F# API，可通过顶部的功能调节轻松访问 SQLite 数据库的数据。
- [LiteDB.FSharp](https://github.com/Zaid-Ajaj/LiteDB.FSharp) - F# 支持 [LiteDB](https://github.com/mbdavid/LiteDB)，这是一个用于 .NET 的嵌入式单文件数据库。
- [Npgsql.FSharp](https://github.com/Zaid-Ajaj/Npgsql.FSharp) - 围绕 PostgreSQL 数据库驱动程序 [Npgsql](https://github.com/npgsql/npgsql) 的精简 F# 包装器。
- [SqlHydra](https://github.com/JordanMarr/SqlHydra) - 用于处理 F# 中的数据库的 NuGet 包套件，包括查询表达式和代码生成工具（用于根据数据库表生成强类型 F# DTO 记录类型）。支持 MySQL、PostgreSQL、Oracle、SQL Server 和 SQLite。
- [TypeShape](https://github.com/eiriktsarpalis/TypeShape) - 用于实用泛型编程的小型、可扩展的 F# 库。
- [Validus](https://github.com/pimbrouwers/Validus) - F# 的可组合验证库，具有适用于大多数原始类型的内置验证器，并可通过自定义验证器轻松扩展。
- [Vp.FSharp.Sql](https://github.com/veepee-oss/Vp.FSharp.Sql) - 通用 F# ADO 提供程序包装器（SqlServer、PostgreSQL、SQLite）。

## 游戏开发

- [FsUnity](https://github.com/FsUnity) - Unity 游戏引擎的 F# 库、工具和插件。
- [Garnet](https://github.com/bcarruthers/garnet) - F# 的轻量级游戏组合库，具有实体组件系统 (ECS) 和类似角色的消息传递功能。
- [Godot](https://www.lkokemohr.de/fsharp_godot.html) - 教程如何将 F# 与 Godot 结合使用。
- [Nu Game Engine](https://github.com/bryanedds/Nu) - 以函数式风格构建的跨平台 F# 2D 游戏引擎。使用 SDL2 和 Farseer 物理。

## 图形用户界面
<!--lint disable double-link -->
- [Avalonia.FuncUI](https://github.com/fsprojects/Avalonia.FuncUI) - 使用 F# 和 Avalonia 开发跨平台 MVU GUI 应用程序。
- [Elmish.WPF](https://github.com/elmish/Elmish.WPF) - Elmish（或 MVU）WPF 编程方法。
- [Epoxy](https://github.com/kekyo/epoxy) - 适用于 .NET 的独立灵活 XAML MVVM 库。
- [Fabulous](https://github.com/fabulous-dev/Fabulous) - F# 功能应用程序开发，使用声明式动态 UI。
<!--lint enable double-link -->

## HTTP 客户端

- [FsHttp](https://github.com/ronaldschlenker/FsHttp) - 一个方便的库，用于通过 F# 使用 HTTP/REST 端点。
- [Http.fs](https://github.com/haf/Http.fs) - 一个简单、实用的 F# HTTP 客户端库。
- [Oryx](https://github.com/cognitedata/oryx) - 高性能 .NET 跨平台功能性 HTTP 请求处理程序库，用于编写 HTTP 客户端和编排 Web 请求。

## 记录

- [FsLibLog](https://github.com/TheAngryByrd/FsLibLog) - 您可以复制并粘贴或通过 Paket GitHub 依赖项添加单个文件，以为您的 F# 库提供日志记录抽象。
- [Logary](https://github.com/logary/logary/) - 适用于 mono 和 .NET 的高性能、多目标日志记录、指标、跟踪和运行状况检查库。

## 包管理

- [NuGet](https://www.nuget.org/) - 适用于 Microsoft 开发平台（包括 .NET）的包管理器。
- [Paket](https://github.com/fsprojects/Paket) - .NET 依赖管理器，支持 NuGet 包和 Git 存储库。

## 解析

- [FParsec](https://github.com/stephan-tolksdorf/fparsec) - F# 的解析器组合器库。
- [FsAttoparsec](https://github.com/haf/FsAttoparsec) - 布莱恩·奥沙利文 (Bryan O'Sullivan) 的阿托秒差距从哈斯克尔 (Haskell) 到 F# 的端口。
- [XParsec](https://github.com/corsis/XParsec) - 适用于 F# 3.0 和 4.0 的可扩展、类型和源多态、非线性应用解析器组合器库。

## 序列化
<!--lint disable double-link -->
- [FSharp.Json](https://github.com/vsapronov/FSharp.Json) - 基于反射的序列化库。
- [FSharp.SystemTextJson](https://github.com/Tarmil/FSharp.SystemTextJson) - F# 类型的 System.Text.Json 扩展。
- [Fleece](https://github.com/mausch/Fleece) - F# 的 JSON 映射器。它简化了从 Json 库的 JsonValue 到您的类型的映射，以及从您的类型到 JsonValue 的映射。
- [FsCodec](https://github.com/jet/FsCodec) - 具有版本容忍转换器的 F# Event-Union 契约编码。
- [FsPickler](https://github.com/mbraceproject/FsPickler) - 适用于 .NET 的快速、多格式消息传递序列化器。
- [Legivel](https://github.com/fjoppe/Legivel) - F# Yaml 1.2 解析器。
- [Thoth.Json](https://thoth-org.github.io/Thoth.Json/) - JSON 编码器/解码器库受 Elm 启发。
<!--lint enable double-link -->

## 模拟
 
- [F# RISC-V Instruction Set formal specification](https://github.com/mrLSD/riscv-fs) - RISC-V CPU 正式 ISA 规范。具有 ELF 文件执行功能的 RISC-V CPU 模拟器。

## 静态站点生成器

- [SkunkHTML](https://github.com/mg0x7BE/skunk-html) - 带有 GitHub Pages 的 Markdown 博客。

## 测试
<!--lint disable double-link -->
- [Expecto](https://github.com/haf/expecto) - 默认情况下具有测试即值和并行性的 F# 平滑测试框架。
- [Faqt](https://github.com/cmeeren/Faqt) - F# 测试和域代码的出色流畅断言。
- [FsCheck](https://github.com/fscheck/FsCheck) - .NET 的随机测试。
- [FsUnit](https://github.com/fsprojects/FsUnit) - 使使用 F# 进行单元测试变得更加愉快。它为您最喜欢的 .NET 测试框架添加了特殊的语法。
- [NBomber](https://github.com/PragmaticFlow/NBomber) - 适用于拉动和推送场景的简单负载测试框架。
- [Persimmon](https://github.com/persimmon-projects/Persimmon) - 使用计算表达式的 F# 单元测试框架。
- [altcover](https://github.com/SteveGilham/altcover) - 适用于 .NET/.NET core 和 Mono 的跨平台覆盖率收集和处理工具集。
- [canopy](https://github.com/lefthandedgoat/canopy) - F# Web 自动化和测试框架。
- [fsharp-hedgehog](https://github.com/hedgehogqa/fsharp-hedgehog) - F# 基于属性的测试系统。
- [unquote](https://github.com/swensensoftware/unquote) - 将 F# 单元测试断言编写为带引号的表达式。
- [xUnit.net](https://xunit.net/) - 适用于 .NET Framework 的免费、开源、以社区为中心的单元测试工具。
<!--lint enable double-link -->

## 类型提供者

- [AzureStorageTypeProvider](https://github.com/fsprojects/AzureStorageTypeProvider) - F# Azure 类型提供程序，可用于探索 Blob、表和队列 Azure 存储资产并轻松对其应用 CRUD 操作。
- [DynamicsCRMProvider](https://github.com/fsprojects/DynamicsCRMProvider) - Microsoft Dynamics CRM 2011 的类型提供程序。
- [EasyBuild.FileSystemProvider](https://github.com/easybuild-org/EasyBuild.FileSystemProvider) - 类型提供程序可根据您的项目结构或虚拟文件系统提供文件和目录的类型表示。
- [ExcelProvider](https://github.com/fsprojects/ExcelProvider) - Excel 类型提供者。
- [FSharp.Configuration](https://github.com/fsprojects/FSharp.Configuration) - 该项目包含用于配置 .NET 项目的类型提供程序。处理 AppSettings、ResX、Yaml 和 Ini 文件。
- [FSharp.Data.Npgsql](https://github.com/demetrixbio/FSharp.Data.Npgsql) - F# 类型提供程序库位于著名的 Npgsql ADO.NET 客户端库之上。
- [FSharp.Data.SqlClient](https://github.com/fsprojects/FSharp.Data.SqlClient) - F# 类型提供程序，用于对 T-SQL 命令参数和结果集进行静态类型访问。
- [FSharp.Data.Tdms](https://github.com/mettekou/FSharp.Data.Tdms) - F# 的 TDMS 支持。
- [FSharp.Data.Toolbox](https://github.com/fsprojects/FSharp.Data.Toolbox) - 基于 FSharp.Data 的各种数据访问 API 的库。该库当前包括用于访问 Twitter 用户和提要的 Twitter 类型提供程序，以及用于读取 SAS 数据集文件的 SAS 类型提供程序。
- [FSharp.Data.TypeProviders](https://github.com/fsprojects/FSharp.Data.TypeProviders) - 包含“.edmx”文件、“.dbml”文件、WSDL 服务、OData 服务和 SQL 数据库的类型提供程序的库。
- [FSharp.Data](https://github.com/fsharp/FSharp.Data) - 数据科学库，包含 CSV、HTML、JSON、XML 和 WorldBank 数据的类型提供程序。
- [FSharp.Management](https://github.com/fsprojects/FSharp.Management) - 该项目包含用于管理机器的各种类型的提供程序。处理文件系统、注册表、Windows Management Instrumentation、PowerShell 和 SystemTimeZones。
- [FSharp.Text.RegexProvider](https://github.com/fsprojects/FSharp.Text.RegexProvider) - 正则表达式的类型提供程序。
- [Facil](https://github.com/cmeeren/Facil) - 从 SQL 查询和存储过程生成 F# 数据访问源代码。
- [FsXaml](https://github.com/fsprojects/FsXaml) - 用于处理 XAML 项目的 F# 工具。
- [FsYaml](https://github.com/bleis-tift/FsYaml) - F# 的类型化 Yaml 库。
- [GraphProvider](https://github.com/fsprojects/GraphProvider) - `.dgml` 状态机类型提供程序。
- [MatDataProvider](https://github.com/fsprojects/matprovider) - 删除了“.mat”文件（二进制 MATLAB 格式文件）的类型提供程序。
- [R Type Provider](https://github.com/BlueMountainCapital/FSharpRProvider) - 输入与 R 互操作的提供程序。
- [Rezoom.SQL](https://github.com/rspeele/Rezoom.SQL) - F# 的静态类型 SQL。
- [S3Provider](https://github.com/fsprojects/S3Provider) - Amazon S3 的实验型提供商。
- [SQLProvider](https://github.com/fsprojects/SQLProvider) - 通用 F# SQL 数据库擦除类型提供程序，支持 LINQ 查询、模式探索、个人、CRUD 操作等等。
- [SwaggerProvider](https://github.com/fsprojects/SwaggerProvider) - Swagger 的生成类型提供程序。

### 创建类型提供者

- [FSharp.TypeProviders.StarterPack](https://github.com/fsprojects/FSharp.TypeProviders.StarterPack) - 用于创建 F# 类型提供程序的 ProvidedTypes SDK。

## 可视化

- [FSharp.Charting](https://github.com/fslaborg/FSharp.Charting) - 适用于交互式 F# 脚本编写的图表库。
- [GG.Net](https://github.com/pablofrommars/GGNet) - 数据科学家的可视化库。
- [Plotly.NET](https://github.com/plotly/Plotly.NET) - 一个基于 Plotly 的 F# 通用绘图库。
- [SharpVG](https://github.com/ChrisNikkel/SharpVG) - 在 F# 中创建 SVG 矢量图形。
- [XPlot](https://github.com/fslaborg/XPlot) - F# 编程语言的绘图库。

## 网络框架
<!--lint disable double-link -->
- [Bolero](https://github.com/fsbolero/Bolero/) - WebAssembly 中的 F#，利用 F# 和 .NET Blazor 的全部功能来开发 SPA。
- [Falco](https://github.com/pimbrouwers/Falco/) - 功能优先的工具包，用于使用 F# 构建出色的 ASP.NET Core 应用程序。
- [Felicity](https://github.com/cmeeren/Felicity) - 无样板、惯用的 JSON:API，用于您美丽、惯用的 F# 域模型。
- [Feliz](https://github.com/Zaid-Ajaj/Feliz) - 在 Fable 中重新审视 React API 以及在 F# 中构建 React 应用程序的高质量组件的集合。
- [Genit](https://github.com/lefthandedgoat/genit) - 使用 F#、Suave 和 PostgreSQL 或 MS SQL Server 的跨平台网站生成器和服务器。
- [Giraffe](https://github.com/giraffe-fsharp/Giraffe) - 面向 F# 开发人员的本机功能 ASP.NET Core Web 框架。
- [Oxpecker](https://github.com/Lanayx/Oxpecker) - 基于 ASP.NET Core 的 F# 框架+支持工具（ViewEngine、Htmx、OpenApi）。
- [Saturn](https://github.com/SaturnFramework/Saturn) - F# 的固执己见的 Web 开发框架，实现服务器端功能性 MVC 模式。
- [Suave](https://github.com/SuaveIO/suave) - 一个简单的 Web 开发 F# 库，提供轻量级 Web 服务器和一组组合器来操纵路由流和任务组合。
- [WebSharper](https://github.com/intellifactory/websharper) - 基于 F# 的 Web 编程平台，包括从 F# 代码到 JavaScript 的编译器。
<!--lint enable double-link -->

## .NET 核心模板
<!--lint disable awesome-list-item-->
- [ASP.NET Core WebAPI F# Template](https://github.com/MNie/FSharpNetCoreWebApiTemplate) - `dotnet new -i WebAPI.FSharp.Template::*`
- [Expecto Template](https://github.com/MNie/Expecto.Template) - `dotnet new -i Expecto.Template::*`
- [Fable, F# |> Babel](http://fable.io) - `dotnet new -i Fable.Template::*`
- [Fable-elmish](https://github.com/fable-compiler/fable-elmish) - `dotnet new -i Fable.Template.Elmish.React::*`
- [Giraffe Template](https://github.com/giraffe-fsharp/giraffe-template) - `dotnet new -i "长颈鹿模板::*"`
- [MiniScaffold](https://github.com/TheAngryByrd/MiniScaffold) - 用于创建和发布面向 .NET Full (net45) 和 Core (netstandard1.6) 的库的 F# 模板，`dotnet new -i MiniScaffold::*`
- [NancyFx Template](https://github.com/MNie/NancyFxCore) - `dotnet new -i NancyFx.Core.Template::*`
- [SAFE Stack Template](https://github.com/SAFE-Stack/SAFE-template) - `dotnet new -i SAFE.Template::*`
<!--lint enable awesome-list-item-->

## 资源

### 博客

- [.NET Blog (F# tag)](https://devblogs.microsoft.com/dotnet/tag/f/) - .NET 团队有关 F# 的新闻和讨论。
- [Codesuji](https://codesuji.com) - 社区成员博客，重点关注 F# 的功能方面。
- [Krzysztof Cieslak](https://kcieslak.io/) - Ionide 维护者的博客。
- [Mark Seemann](https://blog.ploeh.dk/) - 讨论软件设计各个方面的博客。
- [Sergey Tihon (F# Weekly)](https://sergeytihon.com/) - 整个生态系统收集的每周时事通讯。
- [Tomas Petricek](http://tomasp.net/blog/) - 一位致力于各种主题的知名社区成员。

### 书籍

- [Domain Modeling Made Functional by Scott Wlaschin](https://pragprog.com/titles/swdddf/domain-modeling-made-functional/) - 通过领域驱动设计和 F# 解决软件复杂性。
- [F# in Action by Isaac Abraham](https://www.manning.com/books/f-sharp-in-action) - F# 软件开发实用指南。

### 备忘单

- [F# Snips](https://fssnip.net/) - 分享您的 F# 代码片段。
- [F# cheatsheet](https://fsprojects.github.io/fsharp-cheatsheet/) - 主要语言功能的快速参考。
- [F# tour](https://docs.microsoft.com/en-us/dotnet/articles/fsharp/tour) - Microsoft 的官方语言导览。
- [Guide for C# devs to learn F#](https://github.com/knocte/2fsharp/blob/master/csharp2fsharp.md) - 面向 C# 程序员的 30 分钟 F# 教程，包含背对背的代码片段。
- [Guide for Python devs to learn F#](https://github.com/knocte/2fsharp/blob/master/python2fsharp.md) - 面向 Python 程序员的 30 分钟 F# 教程，包含背对背的代码片段。
- [Guide for Rust devs to learn F#](https://github.com/Dhghomon/rust-fsharp) - 供 Rust 和 F# 用户阅读以了解另一种语言的非正式手册。
- [Learn F# in Y minutes](https://learnxinyminutes.com/docs/fsharp) - 建议快速开始 F# 编程的指南。

### 社区

- [放大 F#](https://amplifyingfsharp.io)
- [蓝天上的 F#](https://bsky.app/hashtag/fsharp)
- [Discord 上的 F#](https://discord.com/invite/fsharp-196693847965696000)
- [F# 论话语](https://forums.fsharp.org/)
- [Reddit 上的 F#](https://www.reddit.com/r/fsharp/)
- [Telegram 上的 F#](https://t.me/fsharp_chat)
- [Twitter 上的 F#](https://x.com/hashtag/fsharp)

### 其他清单

- [Awesome .NET!](https://github.com/quozd/awesome-dotnet) - 很棒的 .NET 库、工具、框架和软件的集合。
- [Companies using F#](https://github.com/fsprojects/fsharp-companies) - 社区精选的使用 F# 的公司列表（如果您正在找工作，也许有用？）
- [F# Community Projects](http://fsharp.org/community/projects/) - F# 社区制作的所有内容。
- [Fable Resources](https://fable.io/resources.html) - 与寓言相关的有用教程、库和软件的精选列表。

### 网站

- [Community for F#](http://c4fsharp.net/) - 道场和社区演示录音的链接。
- [Decompiler.com](https://www.decompiler.com/) - 在线 C#/VB/F# 反编译器。
- [DotNetFiddle](https://dotnetfiddle.net/) - 在线 REPL。
- [F# Software Foundation](http://fsharp.org/) - 主要网站。
- [F# for Fun and Profit](https://fsharpforfunandprofit.com/) - 参考教程。
- [SharpLab](https://sharplab.io/) - C#/VB/F# 编译器游乐场。
- [Try F#](https://try.fsharp.org/) - 在线教程，由于 Silverlight 依赖性，目前无法执行代码。
- [cs2fs](https://jindraivanek.gitlab.io/cs2fs-online) - 将 C# 代码转换为 F# 代码。
- [fantomas-tools](https://fsprojects.github.io/fantomas-tools) - 一组 Fantomas 相关工具，例如 AST 查看器和在线错误报告器。

### 视频

- [放大 F# YouTube 频道](https://www.youtube.com/@amplifyingfsharp)
- [F# 在线 YouTube 频道](https://www.youtube.com/@fonline6018)
- [Austin F# 聚会小组录制的演示文稿](http://usergroup.tv/videos/category/group/austin-f-meetup)
- [F# 性能讨论](https://www.youtube.com/watch?v=EIBRoNEpg6c&list=PLqWncHdBPoD4O1sr2Q3W9gAuJ30s09U2r)
- [F# 中的快速字典](https://www.youtube.com/watch?v=KMR2y1vcO-s&list=PLqWncHdBPoD4-d_VSZ0MB0IBKQY0rwYLd)
- [F# 简介](https://www.youtube.com/watch?v=1ioGr701c5Q&list=PLqWncHdBPoD4YEWoXQlRj1tiTc96HZxH8)
- [拓扑排序](https://www.youtube.com/playlist?list=PLqWncHdBPoD5hEK31CcfmTHP-7icw2Xd0)

### 课程

- [使用 F# 在 48 小时内为自己编写一个方案](https://write-yourself-a-scheme.pangwa.com/)
