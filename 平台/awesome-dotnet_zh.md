# 太棒了.NET！

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
[![Build Status](https://github.com/quozd/awesome-dotnet/actions/workflows/awesome-bot.yml/badge.svg)](https://github.com/quozd/awesome-dotnet/actions/workflows/awesome-bot.yml)
[![Join the chat at https://gitter.im/quozd/awesome-dotnet](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/quozd/awesome-dotnet?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

一系列出色的 .NET 库、工具、框架和软件。

灵感来自 [awesome-ruby](https://github.com/markets/awesome-ruby)、[awesome-php](https://github.com/ziadoz/awesome-php)、[awesome-python](https://github.com/vinta/awesome-python)、[frontend-dev-bookmarks](https://github.com/dypsilon/frontend-dev-bookmarks) 和[ruby-bookmarks](https://github.com/dreikanter/ruby-bookmarks)。

随时欢迎您的贡献！请先查看[贡献指南和质量标准](https://github.com/quozd/awesome-dotnet/blob/master/CONTRIBUTING.md)页面。我们也接受专有和商业软件。

感谢所有[贡献者](https://github.com/quozd/awesome-dotnet/graphs/contributors)，你们太棒了，没有你们就不可能！目标是建立一个分类的、由社区驱动的知名资源集合。

# 许可证

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

在法律允许的范围内，[Vitali Fokin](https://github.com/quozd) 已放弃本作品的所有版权以及相关或邻接权。

# 目录

* [很棒的点网](#awesome-dotnet)
  * [算法和数据结构](#algorithms-and-data-structures)
  * [API](#api)
  * [应用框架](#application-frameworks)
  * [申请模板](#application-templates)
  * [人工智能](#artificial-intelligence)
  * [装配操作](#assembly-manipulation)
  * [Assets](#assets)
  * [认证与授权](#authentication-and-authorization)
  * [后台处理](#background-processing)
  * [Blazor](#blazor)
  * [构建自动化](#build-automation)
  * [商业智能和报告](#business-intelligence)
  * [Caching](#caching)
  * [Calendar](#calendar)
  * [Chat](#chat)
  * [CLI](#cli)
  * [CLR](#clr)
  * [CMS](#cms)
  * [代码分析和指标](#code-analysis-and-metrics)
  * [代码片段](#code-snippets)
  * [编译器、转译器和语言](#compilers-transpilers-and-languages)
  * [Compression](#compression)
  * [Configuration](#configuration)
  * [持续集成](#continuous-integration)
  * [Cryptography](#cryptography)
  * [云存储](#cloud-storage)
  * [Database](#database)
  * [数据库驱动程序](#database-drivers)
  * [DateTime](#datetime)
  * [Decompilation](#decompilation)
  * [Deployment](#deployment)
  * [Desktop](#desktop)
  * [DirectX](#directx)
  * [分布式计算](#distributed-computing)
  * [DLR](#dlr)
  * [Documentation](#documentation)
  * [电子商务和支付](#e-commerce-and-payments)
  * [Emulators](#emulators)
  * [环境管理](#environment-management)
  * [ETL](#etl)
  * [事件聚合器和消息传递者](#event-aggregator-and-messenger)
  * [Exceptions](#exceptions)
  * [扩展库](#extensions)
  * [功能管理](#feature-management)
  * [函数式编程](#functional-programming)
  * [Game](#game)
  * [GIS](#gis)
  * [git 工具](#git-tools)
  * [Graphics](#graphics)
  * [GraphQL](#graphql)
  * [GUI](#gui)
  * [HTML 和 CSS](#html-and-css)
  * [HTTP](#http)
  * [IDE](#ide)
  * [图像处理](#image-processing)
  * [安装工具](#install-tools)
  * [Internationalization](#internationalization)
  * [Interoperability](#interoperability)
  * [IoC](#ioc)
  * [JavaScript 引擎](#javascript-engines)
  * [Logging](#logging)
  * [Mail](#mail)
  * [机器学习和数据科学](#machine-learning-and-data-science)
  * [Markdown 处理器](#markdown-processors)
  * [Mathematics](#mathematics)
  * [Media](#media)
  * [Metrics](#metrics)
  * [微框架](#micro-framework)
  * [Minification](#minification)
  * [Misc](#misc)
  * [MQTT](#mqtt)
  * [MVVM](#mvvm)
  * [Networking](#networking)
  * [对象到对象映射](#object-to-object-mapping)
  * [Office](#office)
  * [OpenAI](#openai)
  * [ORM](#orm)
  * [包管理](#package-management)
  * [PDF](#pdf)
  * [Profiler](#profiler)
  * [Protocols](#protocols)
  * [推送通知](#push-notifications)
  * [查询生成器](#query-builders)
  * [Queue](#queue)
  * [RPC](#RPC)
  * [反应式编程](#reactive-programming)
  * [实时通讯](#real-time-communications)
  * [正则表达式](#regular-expression)
  * [Scheduling](#scheduling)
  * [SDK 和 API 客户端](#sdk-and-api-clients)
  * [Search](#search)
  * [Serialization](#serialization)
  * [短信和电话](#sms-and-phone-calls)
  * [状态机](#state-machines)
  * [静态站点生成器](#static-site-generators)
  * [强命名](#strong-naming)
  * [风格指南](#style-guide)
  * [模板引擎](#template-engine)
  * [Testing](#testing)
  * [Tools](#tools)
  * [Trading](#trading)
  * [用户界面自动化](#ui-automation)
  * [Visual Studio 插件](#visual-studio-plugins)
  * [网络浏览器](#web-browsers)
  * [网络框架](#web-frameworks)
  * [网络服务器](#web-servers)
  * [WebSocket](#websocket)
  * [视窗服务](#windows-services)
  * [WPF](#wpf)
  * [解析器库](#parser-library)
  * [源发生器](#source-generator)
* [其他清单](#other-lists)
* [Resources](#resources)

## 算法和数据结构

* [OneOf](https://github.com/mcintyre321/OneOf) - OneOf 为 C# 提供了可区分的联合，并具有详尽的编译时匹配。
* [Algorithmia](https://github.com/SolutionsDesign/Algorithmia) - 适用于 .NET 3.5 及更高版本的算法和数据结构库。 Algorithmia 包含复杂的算法和数据结构，如图形、优先级队列、命令、撤消重做等。
* [Towel](https://github.com/ZacharyPatten/Towel) - 数据结构、算法、数学、元数据、扩展、控制台、测量和其他有用的东西
* [Akade.IndexedSet](https://github.com/akade/Akade.IndexedSet) - 方便的数据结构，支持高效的内存索引和查询，包括范围查询和模糊字符串匹配。

## 应用程序编程接口

* [FastEndpoints](https://github.com/FastEndpoints/FastEndpoints) - 经典 ASP.NET Core API 控制器和最小 API 之间的高性能中间地带。该库使用 REPR（[Request-Endpoint-Response](https://deviq.com/design-patterns/repr-design-pattern)）模式，通过改进代码的共置来消除控制器的样板和整体感觉。
* [Telegram.Bot](https://github.com/TelegramBots/Telegram.Bot) - [Telegram Bot API] 的 .NET 客户端(https://core.telegram.org/bots/api)
* [WTelegramClient](https://github.com/wiz0u/WTelegramClient) - 使用最新版本的 [Telegram 客户端 API](https://core.telegram.org/methods) 在 Telegram 上自动创建用户帐户
* [ASP.NET Web API](https://dotnet.microsoft.com/apps/aspnet/apis) - 可以轻松构建覆盖广泛客户端（包括浏览器和移动设备）的 HTTP 服务的框架
* [Breeze](https://breeze.github.io/doc-net/) - API 框架通过使用 OData 3 协议实现丰富的数据访问。可用于 JavaScript 和 C# 的客户端库。
* [Mobius: C# API for Spark](https://github.com/Microsoft/Mobius) - Mobius 为 Apache Spark 添加了 C# 语言绑定，从而可以用 C# 实现 Spark 驱动程序代码和数据处理操作。
* [ServiceStack](https://github.com/ServiceStack/ServiceStack) - 为所有人提供经过深思熟虑的架构、极快的速度、令人愉悦的 Web 服务
* [Ocelot](https://github.com/ThreeMammals/Ocelot) - .NET核心API网关
* [CommandQuery](https://github.com/hlaueriksson/CommandQuery) - 🌐ASP.NET Core ⚡AWS Lambda ⚡Azure Functions ⚡Google Cloud Functions 🌐ASP.NET Web API 2 的命令查询分离
* [Population.NET](https://github.com/Authentic199/Population.NET) - .NET 库允许客户端指定他们需要的确切字段，通过避免默认情况下检索所有字段来减少不必要的数据传输。
* [Wissance.WebApiTookit](https://github.com/Wissance/WebApiToolkit) - 一组库和类，可简化 REST API 和 gRPC 服务的构建，甚至减少为功能齐全的 REST 控制器编写的一行代码的代码量。

## 应用框架

* [.NET Boxed Framework](https://github.com/Dotnet-Boxed/Framework) - .NET Core 扩展和 Helper NuGet 包
* [ASP.NET Boilerplate](https://github.com/aspnetboilerplate/aspnetboilerplate) - 新的现代 ASP.NET MVC Web 应用程序的起点，具有最佳实践和最流行的工具。
* [ABP](https://github.com/abpframework/abp) - 下一代 ASP.NET Boilerplate Web 应用程序框架。
* [Orleans](https://github.com/dotnet/orleans) - Orleans 是一个框架，提供了一种直接的方法来构建分布式大规模计算应用程序，无需学习和应用复杂的并发或其他扩展模式
* [Runtime](https://github.com/dotnet/runtime) - 运行时存储库包含 .NET (5+) 的库实现（以前称为“CoreFX”）。它包括System.Collections、System.IO、System.Xml 和许多其他组件。
* [CSLA .NET](https://github.com/MarimerLLC/csla) - 业务层开发框架 https://cslanet.com/
* [Mono](https://github.com/mono/mono) - 开源 ECMA CLI、C#、F#、VB 和 .NET 实现
* [peasy](https://github.com/peasy/Peasy.NET) - Peasy 是一个中间层框架，提供易于使用且灵活的规则引擎，旨在解决并发处理、事务支持、容错、线程、可扩展性、异步和多客户端支持以及易于测试等常见挑战，所有这些都不需要巨大的学习曲线！
* [Plastic](https://github.com/sang-hyeon/Plastic) - Plastic 提供了对域、应用程序规则、业务规则或应用程序中的业务逻辑等内容的封装。为此，使用命令模式。
* [Signals](https://github.com/EmitKnowledge/Signals) - Signals 是一个基于 .NET5 的框架，专注于通过为开发团队提供工具、方面和流程来提高开发团队的质量和生产力。
* [Spring.Net](https://github.com/spring-projects/spring-net) - Spring.NET 是一个开源应用程序框架，使构建企业 .NET 应用程序变得更加容易
* [DotNetty](https://github.com/Azure/DotNetty) - DotNetty 是 Netty 的一个端口，异步事件驱动的网络应用程序框架，用于快速开发可维护的高性能协议服务器和客户端。
* [AspectCore Framework](https://github.com/dotnetcore/AspectCore-Framework) - AspectCore Framework 是一个基于面向方面编程的 .NET Core 和 .NET Framework 跨平台框架。对切​​面拦截器、依赖注入集成、Web 应用程序、数据验证等的核心支持。
* [ActualLab.Fusion](https://github.com/ActualLab/Fusion) - 跳过 SignalR 和 gRPC。只需编写 0.1% 的常用实时更新代码即可构建实时 Blazor 和 MAUI 应用程序。使用 ActualLab.Rpc 协议处理 10 倍以上的 API 请求，或者使用 Fusion 透明且完全一致的缓存处理 1000 倍以上的 API 请求。 [示例](https://github.com/ActualLab/Fusion.Samples)。 [文档](https://fusion.actuallab.net/)。
* [silky](https://github.com/liuhll/silky) - Silky框架旨在帮助开发者在.net平台下通过简单的代码和配置快速构建微服务开发框架。
* [Positron-JS](https://github.com/Positron-JS/positron-web-view) - 具有本机 JavaScript 上下文的高级 Web 视图 (PositronWebView)，可从受电容器/cordova 启发的混合应用程序访问 .NET API。

## 申请模板

* [.NET Boxed Templates](https://github.com/Dotnet-Boxed/Templates) - 包含电池的 .NET 项目模板，提供了让您更快地进行所需的最少量的代码。
* [ASP.NET Core Starter Kit](https://github.com/kriasoft/aspnet-starter-kit) - 后端：.NET Core、EF Core、C#；前端：Babel、Webpack、React、CSS 模块
* [ProjectScaffold](https://github.com/fsprojects/ProjectScaffold) - F# 基金会推荐的原型 .NET 解决方案 — 包括文件系统设置、用于依赖项的 Paket 以及用于构建/测试自动化的 FAKE。默认情况下，构建过程还会编译文档并生成 NuGet 包。
* [Serene](https://github.com/volkanceylan/Serenity) - Serenity 是一个 ASP.NET MVC 应用程序平台，旨在通过基于服务的体系结构简化和缩短以数据为中心的业务应用程序的开发。 Serene 是构建 Serenity 应用程序的入门模板。
* [Side-Waffle](https://github.com/LigerShark/side-waffle) - 用于 Web 和桌面开发的大量有用模板的集合。
* [Template10](https://github.com/Windows-XAML/Template10) - 具有设计模式的 Windows 10 模板。
* [Nucleus](https://github.com/alirizaadiyahsi/Nucleus) - Vue启动应用程序模板，后端使用ASP.NET Core API分层架构和基于JWT的身份验证
* [JHipster.NET](https://github.com/jhipster/jhipster-dotnetcore) JHipster 蓝图，用 asp.net core 替换原来的 SpringBoot 后端。 jhipster 的主要目标生成器是展示现代 Java Web 开发的最佳实践。所以该项目的目标是在.net 中做同样的事情。前端可以使用 Angular 或 React 生成，很快就会使用 blazor 生成。 - **注意**：这与 Microsoft 或 .NET 无关

## 人工智能
* [LLamaSharp](https://github.com/SciSharp/LLamaSharp) - C#/.NET 绑定 llama.cpp，使用 C# 运行 LLaMA/GPT 模型，无需编译 lama.cpp。
* [LlmTornado](https://github.com/lofcz/LlmTornado) - 一个 .NET 库，用于使用 OpenAI、Anthropic、Cohere、Google、Azure、Groq 和自托管 API。

## 装配操作

* [Fody](https://github.com/Fody/Fody) - 用于编织 .NET 程序集的可扩展工具。
* [ILRepack](https://github.com/gluck/il-repack) - ILMerge 的开源替代方案。
* [Mono.Cecil](https://github.com/jbevain/cecil) - Cecil 是一个用于生成和检查 ECMA CIL 形式的程序和库的库。

## 资产
* [Bundle Transformer](https://github.com/Taritsyn/BundleTransformer) - [Microsoft ASP.NET Web 优化框架](https://www.nuget.org/packages/Microsoft.AspNet.Web.Optimization) 的模块化扩展。它的模块支持 LESS、Sass、CoffeeScript、TypeScript、Mustache、Handlebars、Autoprefixer 以及一堆不同的 JS 和 CSS 压缩器。

## 认证与授权

* [Abblix OIDC Server](https://github.com/Abblix/Oidc.Server) - 由 OpenID 基金会完全认证的 .NET OpenID Connect 服务器库，为所有配置文件中的 OAuth2 和 OpenID Connect 提供全面支持。 **[$][免费用于非商业用途]**
* [ASP.NET Core Identity](https://github.com/dotnet/aspnetcore/) - ASP.NET 应用程序的新会员系统
* [ASP.NET SAML](https://github.com/jitbit/AspNetSaml) - 对 ASP.NET 应用程序的 SAML 身份验证支持
* [Logibit Hawk](https://github.com/logibit/logibit.hawk/) - 一个 F# [Hawk](https://github.com/outmoded/hawk) 身份验证库
* [Logto](https://github.com/logto-io/csharp) - 适用于现代应用程序和 SaaS 产品的 IAM 基础设施，支持 OIDC、OAuth 2.0 和 SAML 进行身份验证和授权 **[$][OSS 免费]**
* [IdentityModel](https://github.com/IdentityModel) - 用于 .NET 4.5 和 MVC4/Web API 中身份和访问控制的帮助程序库。
* [openiddict](https://github.com/openiddict/openiddict-core) - 适用于 .NET 的灵活且多功能的 OAuth 2.0/OpenID Connect 堆栈
* [Topaz](https://www.topaz.sh/docs/software-development-kits/dotnet/install) - 带有.NET SDK的细粒度授权系统。
* [Enforcer](https://www.identityserver.com/products/enforcer) - 用易于阅读的语言编写细粒度的授权策略，并将其编译为本机 .NET 代码 **[$]**
* [SAML IdentityServer](https://www.identityserver.com/products/saml2p) - 向您的 Duende IdentityServer 添加 SAML 2P 支持 **[$]**
* [SAML OpenIddict](https://www.openiddictcomponents.com/home/) - 向您的 OpenIddict 添加 SAML 2P 支持 **[$]**

## 后台处理

* [BusyBee](https://github.com/mikasjp/BusyBee) - .NET 应用程序的快速内存后台作业处理，具有可配置的队列、超时、并行性和内置 OpenTelemetry 支持。

## 布拉佐尔

* [BootstrapBlazor](https://github.com/dotnetcore/BootstrapBlazor) - 一组基于Bootstrap和Blazor的企业级UI组件。 - **注意**：这与 Microsoft 或 .NET 无关
* [ant-design-blazor](https://github.com/ant-design-blazor/ant-design-blazor) - 一组基于 Ant Design 和 Blazor WebAssembly 的企业级 UI 组件。
* [MASA.Blazor](https://github.com/BlazorComponent/MASA.Blazor) - 一组基于 Material Design 和 Blazor WebAssembly 的企业级 UI 组件。
* [Megabit.Blazorise](https://github.com/Megabit/Blazorise) - Blazorise 是一个构建在 Blazor 和 Bootstrap、Bulma 和 Material 等 CSS 框架之上的组件库。非常容易使用。
* [blazork8s](https://github.com/weibaohui/blazork8s) - Blazor 和 .NET Core 中的 k8s 管理 ui。
* [MudBlazor](https://github.com/MudBlazor/MudBlazor) - Blazor 的 Material Design 框架，允许 .NET 开发人员快速构建 Web 应用程序，并提供大量文档和示例。

## 区块链

* [Nethermind](https://github.com/NethermindEth/nethermind) - .NET Core 中的完整以太坊客户端

## 构建自动化

* [Psake](https://github.com/psake/psake) - 用 PowerShell 编写的基于 .NET 的构建自动化工具
* [FAKE](https://github.com/fsharp/FAKE) - F# Make，跨平台构建自动化系统
* [Invoke-Build](https://github.com/nightroman/Invoke-Build) - PowerShell 构建和测试自动化工具受 Psake 启发。
* [MSBuild](https://github.com/dotnet/msbuild) - Microsoft 构建引擎 (MSBuild) 是 .NET 和 Visual Studio 的构建平台
* [Cake](https://github.com/cake-build/cake) - Cake (C# Make) 是一个带有 C# DSL 的跨平台构建自动化系统。
* [Nake](https://github.com/yevhen/Nake) - 基于 Magic 脚本的 C# 任务运行器
* [Nuke](https://github.com/nuke-build/nuke) - 跨平台构建自动化系统
* [FlubuCore](https://github.com/dotnetcore/FlubuCore) - 跨平台构建和部署自动化系统，用于使用 C# 代码构建项目和执行部署脚本。 - **注意**：这与 Microsoft 或 .NET 无关
* [ModularPipelines](https://github.com/thomhurst/ModularPipelines) - 用 C# 编写管道

## 商业智能

* [FastReport](https://github.com/FastReports/FastReport) - 适用于 .NET Core 2.x/.Net Framework 4.x 的开源报告生成器。 FastReport可用于ASP.NET MVC、Web API应用程序。
* [NReco PivotData](https://www.nrecosite.com/pivot_data_library_net.aspx) - 内存中数据聚合/OLAP 库、数据透视表生成（呈现为 HTML、导出）、ASP.NET 数据透视构建器控件 **[$][单一部署/非 SaaS 免费]**

## 缓存

* [CacheCow](https://github.com/aliostad/CacheCow) - 客户端和服务器上的 ASP.NET Web API HTTP 缓存实现
* [Akavache](https://github.com/reactiveui/Akavache) - 异步、持久的键值存储
* [EasyCaching](https://github.com/dotnetcore/EasyCaching) - 一个缓存库，包含缓存的基本和一些高级用法，可以帮助更轻松地处理缓存！ - **注意**：这与 Microsoft 或 .NET 无关
* [CacheManager](https://github.com/MichaCo/CacheManager) - 用于缓存的通用接口和抽象层。
* [FastCache](https://github.com/jitbit/FastCache) - .NET 的“MemoryCache”替代方案速度快 10 倍
* [Foundatio](https://github.com/FoundatioFx/Foundatio#caching) - 内存、Redis 和混合实现的通用接口。
* [Cache Tower](https://github.com/TurnerSoftware/CacheTower) - .NET 的高效多层缓存系统（内存、Redis、数据库、文件等）
* [FusionCache](https://github.com/jodydonetti/ZiggyCreatures.FusionCache) - 易于使用、高性能且强大的缓存，具有可选的分布式第二层和一些高级功能，例如故障安全机制和高级超时管理
* [BitFaster.Caching](https://github.com/bitfaster/BitFaster.Caching) - 线程安全的内存缓存针对非常高的并发吞吐量、接近最佳的命中率和低延迟进行了优化。

## 日历

* [iCal.NET](https://github.com/rianjs/ical.net) iCal.NET 是一个适用于 .NET 的 iCalendar (RFC 5545) 类库，旨在提供 RFC 5545 合规性，同时提供与流行日历应用程序和库的完全兼容性。

## 聊天

* [Stream](https://github.com/GetStream/stream-chat-net) Stream Chat 的官方 .NET API 客户端，这是一种用于构建聊天应用程序的服务。

## 命令行界面

* [Argu](https://github.com/fsprojects/Argu) - F# 应用程序的声明式 CLI 参数和 XML 配置解析器。
* [CliFx](https://github.com/Tyrrrz/CliFx) - 用于构建命令行界面的声明性框架。
* [CliWrap](https://github.com/Tyrrrz/CliWrap) - 命令行界面的包装。
* [CommandDotNet](https://github.com/bilal-fazlani/commanddotnet) - 使用 C# 以可组合的方式对控制台应用程序进行建模。用方法定义命令。使用属性或嵌套类定义子命令。可扩展的解析和命令执行。
* [Command Line Parser](https://github.com/commandlineparser/commandline) - 命令行解析器库为 CLR 应用程序提供了一个干净简洁的 API，用于操作命令行参数和相关任务
* [CommandLineUtils](https://github.com/natemcmaster/CommandLineUtils) - 这是 Microsoft.Extensions.CommandLineUtils 的一个分支，已不再积极开发。
* [Docopt](https://github.com/docopt/docopt.net) - 命令行界面描述语言会让您微笑。
* [Gui.cs](https://github.com/migueldeicaza/gui.cs) - 用于.NET 的终端 UI 工具包。
* [Power Args](https://github.com/adamabdelhamed/PowerArgs) - PowerArgs 将命令行参数转换为易于编程的 .NET 对象。它还提供了大量的可选功能，例如参数验证、自动生成的用法、制表符完成和大量的可扩展性
* [SharpNetSH](https://github.com/rpetz/SharpNetSH) - 一个简单的 C# netsh 库。
* [spectre.console](https://github.com/spectresystems/spectre.console) - 一个可以更轻松地创建漂亮的控制台应用程序的库。

## CLR

* [Runtime](https://github.com/dotnet/runtime) - Mono 和 CoreCLR .NET 运行时，以及标准库和一些更高级别的组件，例如“System.Linq”和“System.Text.Json”。

## 内容管理系统

* [FluentCMS](https://github.com/fluentcms/FluentCMS) - FluentCMS 是开源 AI 驱动的 ASP.NET Core Blazor 内容管理系统 (CMS)
* [Composite C1](https://github.com/Orckestra/C1-CMS-Foundation) - 专注于用户体验和适应性的 Web CMS
* [mojoPortal ](https://github.com/i7media/mojoportal) - MojoPortal 是一个可扩展、跨数据库、移动友好的 Web 内容管理系统 (CMS) 和用 C# ASP.NET 编写的 Web 应用程序框架
* [Orchard ](https://github.com/OrchardCMS/Orchard) - 免费、开源、以社区为中心的项目，旨在在 ASP.NET 平台上交付应用程序和可重用组件
* [Piranha CMS](https://github.com/PiranhaCMS/piranha.core) - Piranha 是一个有趣、快速且轻量级的 .NET 框架，用于开发基于 cms 的 Web 应用程序。它基于 ASP.NET MVC 和网页构建，并且与 Visual Studio 和 WebMatrix 完全兼容。 https://piranhacms.org
* [Umbraco](https://github.com/umbraco/Umbraco-CMS) - Umbraco 是一个构建在 ASP.NET 平台上的免费开源内容管理系统
* [DotNetNuke](https://www.dnnsoftware.com/community/download) - DNN 平台是我们的免费开源 Web CMS，也是每个专业 DNN 解决方案的基础。全球超过 750,000 个组织已经构建了由 DNN 平台提供支持的网站。
* [Squidex](https://github.com/Squidex/squidex) ![GitHub 星星](https://img.shields.io/github/stars/Squidex/squidex?style=flat-square&cacheSeconds=604800) ![GitHub星星](https://img.shields.io/github/last-commit/Squidex/squidex?style=flat-square&cacheSeconds=86400) - 开源无头 CMS 和内容管理中心。  https://squidex.io
* [fluent-cms](https://github.com/fluent-cms/fluent-cms) - RESTful CRUD（创建、读取、更新、删除）API、管理面板网页、GraphQL 风格的查询设计器和所见即所得网页设计器，所有这些都完全可配置，无需编写代码。

## 代码分析和指标

* [.NET Compiler Platform ("Roslyn") Analyzers](https://github.com/dotnet/roslyn-analyzers) - 最初开发的许多 Roslyn 诊断分析器是为了帮助充实静态分析 API 的设计和实现。
* [PVS-Studio](https://pvs-studio.com/en/pvs-studio/) - PVS-Studio 是一款静态分析器，可保护代码质量、安全性 (SAST) 和代码安全。 **[[OSS 免费](https://pvs-studio.com/en/order/open-source-license/)]** **[$]**
* [NDepend](https://www.ndepend.com) - 是一个 Visual Studio 和 VS Team Services 扩展，可评估您的 .NET 代码质量和技术债务，允许使用 C# LINQ 语法创建代码规则、可视化代码结构并专注于更改和演变。 **[$]**
* [StyleCop](https://github.com/StyleCop) - StyleCop 分析 C# 源代码以强制执行一组样式和一致性规则
* [BenchmarkDotNet](https://github.com/dotnet/BenchmarkDotNet) - 强大的 .NET 基准测试库。
* [Bencher](https://bencher.dev/) - 旨在捕获 CI 中性能回归的连续基准测试工具套件。
* [NsDepCop](https://github.com/realvizu/NsDepCop) - 用于在 C# 项目中强制执行命名空间依赖规则的静态代码分析工具。
* [WebBen](https://github.com/omerfarukz/WebBen) - 是用于对超文本传输​​协议 (HTTP) 服务器进行基准测试的工具。

## 代码片段

* [.NET Fiddle](https://dotnetfiddle.net/) - 在浏览器中编写、编译和运行 C#、F# 和 VB 代码。 JSFiddle 的 .Net 等价物。
* [Sharplab](https://sharplab.io/) - 使用 Roslyn 的不同分支和版本运行 C# 代码，查看生成的 IL 并检查 JIT 的输出。
* [Entity Framework Playground](https://efplayground.io) - 通过编写“DbContext”并在浏览器中使用它进行查询，检查生成的 SQL 进行迁移和查询。通过示例进行学习，比较不同版本的实体框架和提供程序，例如 MS SQL、PostgreSql 和 Sqlite。

## 编译器、转译器和语言

* [ClojureCLR](https://github.com/clojure/clojure-clr) - Clojure 到 C# 中 CLR 的端口
* [ClojureCLR Next](https://github.com/dmiller/clojure-clr-next?tab=readme-ov-file) - 用 F# 重写 Clojure CLR
* [F#](https://github.com/fsharp/fsharp/) - F# 编程语言使每个人都能编写简洁、健壮且高性能的代码
* [Fable](https://github.com/fable-compiler/Fable) - F# 到 JavaScript、TypeScript、JSX、Python、Dart 和 Rust 转译器
* [Eiffel](https://www.eiffel.org/doc/solutions/The_Eiffel_for_.NET_language) - Eiffel for .NET 是在 .NET 环境中提供的 Eiffel 编程语言。
* [Rust](https://github.com/FractalFir/rustc_codegen_clr) - 适用于 .NET 的实验性 Rust 编译器。
* [Wrapped Mono](https://github.com/FractalFir/wrapped_mono) - 嵌入 Rust 中的 Mono 运行时。
* [Hybridizer](https://www.altimesh.com/hybridizer-essentials/) - CIL（C#、VB.Net、F#、ClojureCLR...）到 CUDA 编译器。 **[$]**
* [IronScheme](https://github.com/IronScheme/IronScheme) - R6RS方案编译器、运行时和许多标准库
* [Mond](https://github.com/Rohansi/Mond) - 用 C# 编写的动态类型脚本语言，带有 REPL、调试器和简单的嵌入 API
* [Lua-C#](https://github.com/nuskey8/Lua-CSharp) - 用 C# 在 .NET 上实现 Lua
* [Nemerle](https://github.com/rsdn/nemerle) - Nemerle 是一种适用于 .NET 平台的高级静态类型编程语言。它提供函数式、面向对象和命令式特性。它具有简单的类似 C# 的语法和强大的元编程系统。
* [P](https://github.com/p-org/P) - P 是一种用于异步事件驱动编程的语言。
* [PeachPie](https://github.com/peachpiecompiler/peachpie) - PeachPie 是适用于 .NET 和 .NET Core 的 PHP 编译器和运行时，它允许整个 PHP 应用程序在现代、安全和高性能的 .NET 和 .NET Core 平台上运行。
* [Roslyn](https://github.com/dotnet/roslyn) - .NET 编译器平台（“Roslyn”）提供开源 C# 和 Visual Basic 编译器以及丰富的代码分析 API。它支持使用 Visual Studio 使用的相同 API 构建代码分析工具。
* [PascalABC.NET](https://github.com/pascalabcnet/pascalabcnet) .NET 上的 Pascal 实现。
* [Iron Python](https://github.com/IronLanguages/ironpython3) - 与 .NET 框架集成的 Python 3 实现。
* [IKVM](https://ikvm.org) - 用于 .NET 的 Java 虚拟机和字节码到 IL 转换器。在 .NET 上执行已编译的 Java 代码（字节码）
* [Lib.Harmony](https://github.com/pardeike/Harmony) - 一个用于在运行时修补、替换和装饰 .NET 和 Mono 方法的库，主要用于游戏修改。
* [dotnet-repl](https://github.com/jonsequitur/dotnet-repl) - 基于 .NET Interactive 的多语言 REPL

## 压缩

* [SharpCompress](https://github.com/adamhathcock/sharpcompress) - SharpCompress 是一个适用于 .NET/Mono/Silverlight/WP7 的压缩库，可以通过只进读取和文件随机访问 API 来解压缩、un7zip、unzip、untar unbzip2 和 ungzip。实现了对 zip/tar/bzip2/gzip 的写入支持
* [FastLZMA2NET](https://github.com/kingsznhone/FastLZMA2Net) - [快速 LZMA2 算法](https://github.com/conor42/fast-lzma2) 的 .NET 包装器。

## 配置
* [AgileConfig](https://github.com/dotnetcore/AgileConfig) - AgileConfig是一个轻量级的配置中心，可以帮助您通过网站管理所有应用程序的配置。 - **注意**：这与 Microsoft 或 .NET 无关

## 持续集成
* [TeamCity](https://www.jetbrains.com/teamcity/) - 准备工作、可扩展且对开发人员友好的构建服务器 — 开箱即用 **[$]**
* [MyGet](https://www.myget.org/) - 持续集成和部署，适用于 NuGet、NPM、Bower 和 VSIX 的托管包存储库 **[$]**
* [AppVeyor](https://www.appveyor.com/) - .NET 持续集成和部署即服务。 **[$]** **[OSS 免费]**

## 密码学

* [BouncyCastle](https://bouncycastle.org/) - 与 .Net System.Security.Cryptography 一起，是 CLR 上加密算法的参考实现。
* [NaCl.Core](https://github.com/daviddesmet/NaCl.Core) - .NET 的仅托管加密库，提供现代加密原语。
* [Paseto.Core](https://github.com/daviddesmet/paseto-dotnet) - .NET 的 Paseto（与平台无关的安全令牌）实现
* [Pkcs11Interop](https://github.com/Pkcs11Interop/Pkcs11Interop) - 用于非托管 PKCS#11 库的托管 .NET 包装器，提供对加密硬件的访问
* [SecurityDriven.Inferno](https://github.com/sdrapkin/SecurityDriven.Inferno) - .NET 加密库。经过专业审核。
* [CryptoNet](https://github.com/maythamfahmi/CryptoNet) - .NET 简单加密库。原生 C#。

## 云存储

* [Foundatio](https://github.com/FoundatioFx/Foundatio#jobs) - 支持 AWS、Azure 和许多其他提供商的云存储库。
* [FluentStorage](https://github.com/robinrodricks/FluentStorage) - Polycloud .NET 云存储抽象层最初称为 Storage.Net。为 Blob 存储（AWS S3、GCP、FTP、SFTP、Azure Blob/文件/事件中心/数据湖）和消息传递（AWS SQS、Azure Queue/ServiceBus）提供通用接口。
* [Stowage](https://github.com/aloneguid/stowage) - 无膨胀零依赖 .NET 云存储套件，至少支持主要云提供商。
* [云存储](https://github.com/managedcode/Storage)：- 该库提供了一个通用接口，用于访问和操作不同云 blob 存储提供商（Azure 存储、AWS S3、Google 云存储）中的数据。它可以轻松地在提供商之间切换或同时使用多个提供商，而无需学习和使用多个 API。

## 数据库

* [RocksDB](https://github.com/curiosity-ai/rocksdb-sharp) - Facebook 的 RocksDB 键值存储的 C# 绑定 + 适用于 Windows、macOS 和 Linux 的本机构建
* [DBreeze](https://github.com/hhblaze/DBreeze) - DBreeze Database 是一个开源嵌入式键值存储
* [Event Store](https://github.com/EventStore/EventStore) - 具有 JavaScript 复杂事件处理功能的开源功能数据库
* [LiteDB](https://github.com/mbdavid/LiteDB) - 单个数据文件中的 .NET NoSQL 文档存储 - https://www.litedb.org
* [RavenDB](https://github.com/ravendb/ravendb) - 适用于 .NET 的支持 LINQ 的文档数据库
* [Marten](https://github.com/JasperFx/marten) - PostgreSQL 作为 .NET 应用程序的文档数据库和事件存储
* [Realm Xamarin](https://github.com/realm/realm-dotnet) - SQLite 和 ORM 的快速、易于使用的替代方案 - https://realm.io/docs/dotnet/latest/
* [Streamstone](https://github.com/yevhen/Streamstone) - Azure 表存储的事件存储
* [Ignite](https://github.com/apache/ignite) - 分布式内存平台：支持SQL和LINQ的文档数据库；分布式计算；分布式服务和事件。
* [Yessql](https://github.com/sebastienros/yessql) - 适用于任何 RDBMS 的 .NET 文档数据库
* [JsonFlatFileDataStore](https://github.com/ttu/json-flatfile-datastore) - 简单的 JSON 平面文件数据存储，支持类型化和动态数据
* [ZoneTree](https://github.com/koculu/ZoneTree) - 适用于 .NET 的持久、高性能、事务性且符合 ACID 的有序键值数据库。

## 数据库驱动程序

* [DuckDB.NET](https://github.com/Giorgi/DuckDB.NET) - DuckDB 的 .NET 数据提供程序
* [MySQL Connector](https://dev.mysql.com/downloads/connector/net/) - Connector/Net 是用于 MySQL 的完全托管的 ADO.NET 驱动程序
* [Npgsql](https://github.com/npgsql/Npgsql) - PostgreSQL 的 .NET 数据提供程序
* [MongoDB](https://github.com/mongodb/mongo-csharp-driver) - 官方 MongoDB C# 驱动程序
* [ServiceStack Redis](https://github.com/ServiceStack/ServiceStack) - .NET 领先的 C# Redis 客户端
* [StackExchange Redis](https://github.com/ServiceStack/ServiceStack) - StackExchange 的通用 Redis 客户端
* [Cassandra](https://github.com/datastax/csharp-driver) - 适用于 Apache Cassandra 的 DataStax .NET 驱动程序
* [Couchbase](https://github.com/couchbase/couchbase-net-client) - 官方 Couchbase .NET 客户端库，基于 Enyim memcached 客户端
* [Firebird.NET](https://sourceforge.net/projects/firebird/) - .NET 数据提供程序是用 C# 编写的，提供 Firebird API 的高性能本机实现
* [Rqlite-dotnet](https://github.com/rqlite/rqlite-dotnet) - rqlite 的.NET 客户端（基于 SQLite 的分布式关系数据库）

## 日期时间

* [NodaTime](https://github.com/nodatime/nodatime) - Noda Time 是 .NET 的替代日期和时间 API。它可以帮助您更清晰地思考数据，并更准确地表达对该数据的操作。 https://nodatime.org/
* [DateTimeExtensions](https://github.com/joaomatossilva/DateTimeExtensions) - 以“System.DateTime”扩展形式进行的常见日期时间操作，包括多种文化区域设置的假期和工作日计算。
* [Exceptionless.DateTimeExtensions](https://github.com/exceptionless/Exceptionless.DateTimeExtensions) - DateTimeRange、Business Day 和各种 `DateTime`、`DateTimeOffset`、`TimeSpan` 扩展方法。

## 反编译

* [dnSpy](https://github.com/0xd4d/dnSpy) - 开源 .NET 程序集浏览器、编辑器、反编译器和调试器
* [dnSpyEx](https://github.com/dnSpyEx/dnSpy) - dnSpy 的非官方复兴
* [ILSpy](https://ilspy.net/) - ILSpy 是开源 .NET 程序集浏览器和反编译器
* [dotPeek](https://www.jetbrains.com/decompiler/) - 基于 ReSharper 捆绑反编译器的免费独立工具。它可以可靠地将任何 .NET 程序集反编译为等效的 C# 或 IL 代码。它可以直接基于原始二进制文件创建 Visual Studio 解决方案。 **[专有]** **[免费]**

## 部署
* [DbUp](https://github.com/DbUp/DbUp) - .NET 库可帮助您将更改部署到 SQL Server 数据库。它跟踪已运行的 SQL 脚本，并运行使数据库保持最新状态所需的更改脚本


## 直接X

* [Vortice.Windows](https://github.com/amerkoleci/Vortice.Windows) - 适用于 DirectX、WIC、Direct2D1、XInput、XAudio 和 X3DAudio 的跨平台 .NET 标准库

## 桌面

* [Sucrose Wallpaper Engine](https://github.com/Taiizor/Sucrose) - Sucrose 是一款多功能壁纸引擎，可通过各种交互式壁纸为您的桌面带来生机。

## 分布式计算

* [.NEXT Raft](https://github.com/dotnet/dotNext) - .NET 和 ASP.NET Core 的 Raft 实现，允许构建由分布式共识和复制支持的集群微服务
* [Orleans](https://github.com/dotnet/orleans) - Orleans 是一个框架，它提供了一种直接的方法来构建分布式大规模计算应用程序，而无需学习和应用复杂的并发或其他扩展模式。它是由微软研究院创建的。
* [Orleankka](https://github.com/OrleansContrib/Orleankka) - Orleankka 是 Microsoft Orleans 框架的函数式 API。它非常适合需要可组合、统一通信接口的场景，例如：CQRS、事件源、重新路由、FSM 等。可用于 F# 的附加 API 称为 Orleankka.FSharp。
* [Akka.net](https://github.com/akkadotnet/akka.net) - Akka.NET 是流行的 Java/Scala 框架 Akka 到 .NET 的端口。这是一个社区驱动的端口，与制作原始 Java/Scala 版本的 Typesafe 无关。
* [Zebus](https://github.com/Abc-Arbitrage/Zebus) - Zebus 是一种轻量级、高度通用的点对点服务总线，在构建时考虑了 CQRS 原则。它允许应用程序以快速、轻松的方式相互通信。大多数复杂性都隐藏在库中，您可以专注于编写对您重要的代码，而不是调试消息传递代码。任何分布式应用程序的非常基础的基础。
* [protoactor-dotnet](https://github.com/AsynkronIT/protoactor-dotnet) - Proto Actor - 适用于 Golang 和 C# 的超快速分布式 Actor

## 德国航天中心

## 文档

* [Sandcastle](https://github.com/EWSoftware/SHFB) - Sandcastle 帮助文件生成器类似于 NDoc
* [SourceBrowser](https://github.com/KirillOsenkov/SourceBrowser) - 为 https://referencesource.microsoft.com 提供支持的源浏览器网站生成器
* [Swashbuckle](https://github.com/domaindrivendev/Swashbuckle.WebApi) - 将 Swagger 无缝添加到 Web API 项目。
* [F# Formatting](https://fsprojects.github.io/FSharp.Formatting/) - 用于从 F# 脚本文件、Markdown 文档和内联 XML 或 Markdown 注释记录 F# 和 C# 项目的工具
* [DocFX](https://github.com/dotnet/docfx) - 用于为 .NET 项目构建和发布 API 文档的工具
* [DocNet](https://github.com/FransBouma/DocNet) - 您友好的静态文档生成器，使用 markdown 文件来构建内容。
* [HubDocs](https://github.com/mberrishdev/HubDocs) - 类似 Swagger 的 UI 工具，如 Swagger，但适用于 SignalR 集线器 - 自动发现集线器、探索方法、调用和预览实时客户端消息。

## 电子商务和支付

* [NopCommerce](https://github.com/nopSolutions/nopCommerce) - nopCommerce。免费开源电子商务购物车（ASP.NET Core）
* [ServiceStack.Stripe](https://github.com/ServiceStack/ServiceStack) - stripe.com REST API 的类型化 .NET 客户端
* [SmartStoreNET](https://github.com/smartstore/Smartstore) - 免费的ASP.NET Core MVC电子商务购物车解决方案
* [Stripe.Net](https://github.com/stripe/stripe-dotnet) - Stripe.net 是 https://stripe.com/ 的完整 .NET API 服务
* [Virto Commerce](https://github.com/VirtoCommerce/vc-platform) - Virto Commerce 是第二代版本，是唯一在开源许可下完全可用的企业级电子商务产品。 Virto Commerce 基于 .NET 4.5，广泛使用了 MVC、IoC、EF、Azure、AngularJS 等众多前沿技术。它可以部署在 Microsoft 云 (Azure)、Amazon Web Services (AWS) 和本地。 https://virtocommerce.com
* [SimplCommerce](https://github.com/simplcommerce/simplcommerce) - 基于.NET Core 构建的超级简单的电子商务系统。使用简单且易于定制。借助 .NET Core，您可以在 Windows、Linux 上运行 SimplCommerce。使用各种 RDBMS：Microsoft SQL Server、PostgreSQL、MySQL
* [GrandNode](https://github.com/grandnode/grandnode2) - 无头、多供应商、多租户、基于 .NET Core 5.0 和 MongoDB 的最先进的开源电子商务平台。
* [Adyen](https://github.com/Adyen/adyen-dotnet-api-library) - 适用于 .NET 的官方 Adyen 支付 API 库

## 模拟器

* [Blzhawk](https://github.com/TASEmulators/BizHawk) - BizHawk 是一个用 C# 编写的多系统模拟器。 BizHawk 为休闲游戏玩家提供了很好的功能，例如全屏和手柄支持，以及适用于所有系统核心的完整重新录制和调试工具。

## 环境管理

* [Dotnet CLI](https://github.com/dotnet/sdk) - 跨平台 .NET Core 命令行工具链实用程序。

## ETL

* [Cinchoo ETL](https://github.com/Cinchoo/ChoETL) - .NET 的 ETL 框架（读/写 CSV、Flat、Xml、JSON、键值格式文件）
* [EtlBox.Classic](https://github.com/rpsft/etlbox) - 基于 Microsoft TPL.Dataflow 库构建的轻量级 ETL（提取、转换、加载）库和 .NET 数据集成工具箱。

## 事件聚合器和消息传递者

* [Mediator.Net](https://github.com/mayuanyang/Mediator.Net) - .NET 的简单中介，用于发送命令、发布事件和请求响应，并支持管道
* [MediatR](https://github.com/jbogard/MediatR) - .NET 中简单、简单的中介实现
* [EventFlow](https://github.com/eventflow/EventFlow) - EventFlow 是适用于 .NET 的异步/等待第一 CQRS 和事件源 DDD 框架
* [LiteBus](https://github.com/litenova/LiteBus) - 一个易于使用且雄心勃勃的进程内中介器，为实现命令查询分离 (CQS) 提供了基础

## 例外情况
* [Exceptionless](https://github.com/exceptionless/Exceptionless.Net) - 无异常的 .NET 客户端

## 扩展
* [ExtensionMethods.Net](https://www.extensionmethod.net/csharp) - 具有扩展方法集合的站点

## 功能管理
* [Microsoft.FeatureManagement](https://github.com/microsoft/FeatureManagement-Dotnet) - 该库提供了一种基于功能标志开发和公开应用程序功能的方法。它支持新功能推出和用于实验目的的 A/B 测试等场景。它还提供与常见 .NET 编码模式和 ASP.NET Core 的集成。
* [OpenFeature](https://openfeature.dev) - OpenFeature 是功能标志管理的开放标准，旨在提供统一的 API 和 SDK，使开发人员能够将功能标志评估与特定于供应商的实现分离。它促进了跨不同工具和平台管理功能标志的互操作性、灵活性和标准化。

## 函数式编程
* [language-ext](https://github.com/louthy/language-ext) - 该库使用并滥用了 C# 6+ 的功能来提供功能性“基类库”，如果您仔细观察，它看起来就像是语言本身的扩展。它还包括一个“类似 Erlang”的流程系统（参与者），可以选择将消息和状态保存到 Redis（请注意，您可以在没有 Redis 的情况下使用它进行应用内消息传递）。该进程系统还支持 Rx 消息流和状态，从而实现反应事件和消息调度的完整系统。
* [MoreLinq](https://github.com/MoreLinq/MoreLinq) - 为 LINQ to Objects 提供额外的方法。

## 游戏

* [MonoGame](https://github.com/MonoGame/MonoGame) - 一种用于创建强大的跨平台游戏的框架
* [FNA](https://github.com/FNA-XNA/FNA) - FNA 是 XNA4 的重新实现，仅专注于为桌面开发完全准确的 XNA4 运行时
* [Duality](https://github.com/AdamsLair/duality) - Duality 是一个 2D 游戏开发框架。专注于模块化，配有可视化编辑器。
* [Stride Game Engine](https://stride3d.net/ ) - Stride Game Engine 是一款 2D/3D 跨平台游戏引擎，具有场景编辑器、粒子、基于物理的渲染 (PBR)、脚本编写等
* [Wave Engine](https://waveengine.net/Engine) - Wave 引擎是一个免费的基于 C# 组件的现代游戏引擎，它允许您创建支持 Kinect、Oculus Rift、Vuforia、Cardboard、Leap Motion 等的跨平台游戏。 **[免费][专有]**
* [Nez](https://github.com/prime31/Nez) - Nez 是一个免费的 2D 框架，可与 MonoGame 和 FNA 配合使用
* [BEPUphysics](https://github.com/bepu/bepuphysics2) - BEPUphysical 是一个纯 C# 3D 物理库
* [osu!framework](https://github.com/ppy/osu-framework) - 一款专为精彩游戏而编写的 2D 应用程序/游戏。
* [DotRecast](https://github.com/ikpil/DotRecast) - Recast & Detour 的端口，用于游戏、Unity3D、服务器、C# 的导航网格工具集
* [Foster](https://github.com/FosterFramework/Foster) - Foster 是一个 C# 编写的小型跨平台 2D 游戏框架。
* [Friflo.Engine.ECS](https://github.com/friflo/Friflo.Engine.ECS) - 具有简单 API 的高性能 C# ECS。支持.NET、WASM/WebAssembly、本机 AOT、Unity、Godot、MonoGame 等
* [Box2D.NET](https://github.com/ikpil/Box2D.NET) - Box2D 的 C# 端口，用于游戏、服务器和 Unity3D 的 2D 物理引擎

## 地理信息系统

* [NetTopologySuite](https://github.com/NetTopologySuite/NetTopologySuite/) .NET GIS 解决方案，针对 .NET 平台快速可靠
 * [OsmSharp](https://www.osmsharp.com/) - 用于处理 OpenStreetMap (OSM) 数据的 C# 库。提供OSM数据的读取、写入和路由规划。
 * [GeoJSON.NET](https://github.com/GeoJSON-Net/GeoJSON.Net) - 用于 GeoJSON 类型和相应 Json.Net（反）序列化器的 .Net 库
 * [CoordinateSharp](https://github.com/Tronald/CoordinateSharp) - 轻松解析或转换坐标格式并计算基于位置的太阳/月球信息。
 * [DEM Net Elevation API](https://github.com/dem-net/dem.net) - 用于数字高程模型的.Net 库，允许以 glTF / STL 格式生成 3D 地形。

## git 工具

* [Husky.Net](https://github.com/alirezanet/Husky.Net) - 使用 Husky.Net 内部任务运行器可以轻松使用 Git 挂钩，您可以在提交或推送时使用它来检查提交消息、运行测试、检查代码等。支持 C# 脚本、gitflow hooks、多文件状态（staged、lastCommit、glob）
* [GitExtensions](https://github.com/gitextensions/gitextensions) - GitExtensions 是一个 shell 扩展、一个 Visual Studio 2008/2010/2012/2013 插件和一个独立的 Git 存储库工具。 https://gitextensions.github.io/
* [GitVersion](https://github.com/GitTools/GitVersion) - 根据 Git 存储库的状态生成语义版本号
* [LibGit2Sharp](https://github.com/libgit2/libgit2sharp) - LibGit2Sharp 将本机 Git 实现 libgit2 的所有功能和速度带入 .NET 和 Mono 的托管世界。
* [posh-git](https://github.com/dahlbyk/posh-git) - Git 的 PowerShell 环境
* [Git Credential Manager](https://github.com/git-ecosystem/git-credential-manager) - 帮助解决凭证问题

## 图形

* [Oxyplot](https://github.com/oxyplot/) - OxyPlot 是 .NET 的跨平台绘图库
* [OpenTK](https://github.com/opentk/opentk) - Open Toolkit 是一个高级的低级 C# 库，封装了 OpenGL、OpenCL 和 OpenAL
* [Aspose.Drawing](https://products.aspose.com/drawing/net) - 完全托管、跨平台、完整的 2D 图形库，用于绘制文本、几何图形和图像，具有 System.Drawing 兼容 API。 **[$]**
* [ScottPlot](https://swharden.com/scottplot/) - 用于交互式显示大型数据集的绘图库。线图、条形图、饼图、散点图等。它支持 WinForms、WPF、Avalonia、控制台。
* [LiveCharts2](https://github.com/beto-rodriguez/LiveCharts2) - 简单、灵活、交互式且功能强大的 .Net 图表、地图和仪表。 LiveCharts2 支持 WPF、WinForms、Xamarin、Avalonia、WinUI、UWP。
* [Helix Toolkit](https://github.com/helix-toolkit/helix-toolkit) - Helix Toolkit 是 .NET 的 3D 组件集合
* [AssimpNet](https://bitbucket.org/Starnick/assimpnet) - 用于开放资产导入器（“Assimp”）的跨平台 .NET Standard 包装器。该库支持导入、处理和导出 3D 模型，以便在图形/游戏应用程序中进行渲染。支持超过 40 种格式导入（例如 OBJ、FBX、GLTF、3DS、Collada），并且可以导出这些格式的子集（例如 OBJ、GLTF、3DS、Collada）。网格处理功能允许生成网格数据或优化实时渲染。
* [Silk.NET](https://github.com/dotnet/Silk.NET) - 跨平台、高性能、低级 .NET Standard 包装器，适用于许多高级 API，例如 OpenGL、OpenCL、OpenAL、OpenXR、Assimp、GLFW 以及许多其他 API。除了封装本机 API 之外，它还带有自己的窗口和输入抽象。这使得使用 Silk.NET 进行游戏和应用程序开发变得轻而易举，并且几乎拥有 3D 应用程序开发人员所需的一切。
* [Veldrid](https://github.com/mellinoe/veldrid) - 适用于 .NET 的低级便携式图形和计算库
* [VectSharp](https://github.com/arklumpus/VectSharp) - .NET 库创建矢量图形和文本，然后将其导出为 PDF、SVG 和光栅图像格式。

## GraphQL
* [GraphQL.NET](https://github.com/graphql-dotnet/graphql-dotnet) - [Facebook 的 GraphQL](https://github.com/graphql/graphql-spec) 在 .Net 中的实现
* [HotChocolate](https://github.com/ChilliCream/hotchocolate) - GraphQL 服务器与所有 GraphQL 兼容的客户端兼容，例如 Strawberry Shake、Relay、Apollo 客户端以及各种其他客户端和工具。
* [EntityGraphQL](https://github.com/EntityGraphQL/EntityGraphQL) - 用于在数据模型之上构建 GraphQL API 的库，具有可扩展性，可以轻松地将多个数据源整合到单个 GraphQL 架构中（EF 不是必需的 - 任何与 LinqProvider 或内存中对象一起使用的 ORM 都可以）。
* [ZeroQL](https://github.com/byme8/ZeroQL) - 高性能 C# 友好的 GraphQL 客户端。它支持类似 Linq 的语法。它不需要 Reflection.Emit 或表达式。因此，运行时提供的性能非常接近原始 HTTP 调用。

## 图形用户界面

### 图形用户界面-框架

* [Avalonia](https://github.com/AvaloniaUI/Avalonia) - 多平台 .NET UI 框架（以前称为 Perspex）。
* [Windows UI Library](https://github.com/microsoft/microsoft-ui-xaml) - Windows UI 库 (WinUI) 为 Windows UWP 应用程序提供官方本机 Microsoft UI 控件和功能。
* [UNO Platform](https://github.com/unoplatform) - 唯一使用 C#、XAML 从单一代码库构建本机移动、桌面和 WebAssembly 的平台。开源并得到专业支持。网站：[platform.uno](https://platform.uno/)
* [Xamarin.Forms](https://github.com/xamarin/Xamarin.Forms) - 从单个共享的 C# 代码库构建适用于 iOS、Android 和 Windows 的本机 UI。
* [Eto.Forms](https://github.com/picoe/Eto) - 适用于 .NET 和 Mono 中的桌面和移动应用程序的跨平台 GUI 框架
* [Gtk#](https://github.com/mono/gtk-sharp) - Gtk# 是 Mono/.NET 与跨平台 Gtk+ GUI 工具包的绑定，也是大多数使用 Mono 构建的 GUI 应用程序的基础
* [QtSharp](https://github.com/ddobrev/QtSharp) - Qt 的 Mono/.NET 绑定
* [SciterSharp](https://github.com/ramon-mendes/SciterSharp) - 不仅使用 HTML，还使用 Sciter 引擎的所有功能创建 .NET 跨平台桌面应用程序：CSS3、SVG、脚本、AJAX、<视频>...Sciter 可免费用于商业用途
* [XWT](https://github.com/mono/xwt) - 用于使用 .NET 和 Mono 创建桌面应用程序的跨平台 UI 工具包
* [Qml.Net](https://github.com/qmlnet/qmlnet) - Mono/.NET/.NET Core 的跨平台 Qml/.NET 集成
* [Lara](https://github.com/integrativesoft/lara) - Lara Web Engine 是一个用于用 C# 开发 Web 用户界面的库 - （Blazor 服务器端替代方案）
* [Neutronium](https://github.com/NeutroniumCore/Neutronium) - 使用 HTML、CSS、javascript 和 MVVM 绑定（例如 WPF）构建 .NET 桌面应用程序。
* [photino.NET](https://github.com/tryphotino/photino.NET) - Photino 是一个轻量级开源框架，用于使用 Web UI 技术构建本机、跨平台桌面应用程序。
  
### GUI - 主题控制工具包

* [Modern UI for WPF - MUI](https://github.com/firstfloorsoftware/mui) - 一组控件和样式，用于将 WPF 应用程序转换为美观的现代 UI 应用程序。
* [MahApps.Metro](https://github.com/MahApps/MahApps.Metro) - 用于创建 Metro 风格的 WPF 应用程序的工具包
* [MaterialSkin](https://github.com/IgnaceMaes/MaterialSkin) - 将 .NET WinForms、C# 或 VB.Net 主题化为 Google 的 Material Design 原则。
* [AdonisUI](https://github.com/benruehl/adonis-ui) - 适用于 WPF 应用程序的轻量级 UI 工具包，提供经典但增强的 Windows 视觉效果。
* [Bunifu UI Framework](https://bunifuframework.com) - 精心制作的 Winforms 控件和组件，用于创建令人惊叹的现代应用程序 UI。 **[$]**
* [HandyControl](https://github.com/HandyOrg/HandyControl) - 包含一些简单常用的WPF控件
* [MaterialDesignInXamlToolkit](http://materialdesigninxaml.net/) - 用于创建 Material Design 风格的 WPF 应用程序的工具包
* [UWP Community Toolkit](https://github.com/windows-toolkit/WindowsCommunityToolkit) - UWP 社区工具包是辅助函数、自定义控件和应用服务的集合。它简化并演示了为 Windows 10 构建 UWP 应用程序的常见开发人员任务。
* [Empty Keys UI](https://www.emptykeys.com/ui_library/) - 基于多平台和多引擎 XAML 的用户界面库 **[免费][专有]**

### GUI-其他

* [Callisto](https://github.com/timheuer/callisto) - 适用于 Windows 8 XAML 应用程序的控制工具包。包含一些 UI 控件，以便更轻松地根据 Windows UI 指南为 Windows 应用商店创建 Windows UI 风格的应用程序。
* [WinApi](https://github.com/prasannavl/WinApi) - 一个简单、直接、超薄的 CLR 库，用于高性能 Win32 本机互操作，具有自动化、窗口、DirectX、OpenGL 和 Skia 帮助程序。
* [ObjectListView](http://objectlistview.sourceforge.net/cs/index.html) - ObjectListView 是 .NET ListView 的 C# 包装器。它使 ListView 更容易使用并教给它一些新技巧
* [DockPanelSuite](https://sourceforge.net/projects/dockpanelsuite/) - 受 Visual Studio 启发的 .NET WinForms 对接库
* [AvalonEdit](https://github.com/icsharpcode/AvalonEdit) - SharpDevelop中使用的基于WPF的文本编辑器组件

## HTML 和 CSS

* [AngleSharp](https://github.com/AngleSharp/AngleSharp) - 完整的 HTML5 DOM 和 CSS3 OM 构建
* [dotless](https://github.com/dotless/dotless) - Ruby Less CSS 库的 .NET 端口 http://www.dotlesscss.org
* [ExCSS](https://github.com/TylerBrinks/ExCSS) - C# 的 CSS3 解析器库
* [HtmlAgilityPack](https://html-agility-pack.net/?z=codeplex) - 敏捷的 HTML 解析器，可构建读/写 DOM 并支持纯 XPath 或 XSLT
* [LibSass Host](https://github.com/Taritsyn/LibSassHost) - 围绕 [libSass](https://sass-lang.com/libsass) 库的 .NET 包装器，能够支持虚拟文件系统

## HTTP协议

* [RestSharp](https://github.com/restsharp/RestSharp) - 适用于 .NET 的简单 REST 和 HTTP API 客户端
* [Flurl](https://flurl.dev) - 流畅、可移植、可测试的 REST/HTTP 客户端库
* [Refit](https://github.com/reactiveui/refit) - 适用于 Xamarin 和 .NET 的自动类型安全 REST 库
* [WebApiClient](https://github.com/dotnetcore/WebApiClient) 一个基于HttpClient的开源项目。只需要定义c#接口并修改相关功能即可异步调用远程http接口的客户端库。
* [Apizr](https://github.com/Respawnsive/Apizr) 基于 Web api 客户端的改装，但具有弹性（重试、连接、缓存、身份验证、日志、优先级等）。
* [Fluxzy.Core](https://github.com/haga-rak/fluxzy.core) - 一个完全托管和完全流式传输的 Man-On-The-Middle 库，用于通过普通或安全通道拦截、记录和更改 HTTP/1.1、H2、websocket 流量。
* [NotoriousClient](https://github.com/Notorious-Coding/Notorious-Client) - 强类型、可扩展的 HTTP 客户端，具有流畅的请求生成器、流式传输和多部分。基于 .NET 的 HttpRequestMessage 构建。

## 集成开发环境
* [Visual Studio Community](https://visualstudio.microsoft.com/vs/community/) - 功能齐全的 IDE
* [Waf DotNetPad](https://jbe2277.github.io/dotnetpad/) - 一个简单快速的代码编辑器，可使用 C# 或 Visual Basic 编写有趣的程序。
* [Visual Studio Code](https://code.visualstudio.com/) - 来自微软的优秀开源编辑器，基于Electron。
* [Ionide](http://ionide.io/) - 用于跨平台 F# 开发的 Atom 编辑器和 Visual Studio Code 软件包套件。
* [Rider](https://www.jetbrains.com/rider/) - 基于 IntelliJ 平台和 ReSharper 的跨平台 C# IDE
* [RoslynPad](https://github.com/aelij/RoslynPad) - 一个基于 Roslyn 和 AvalonEdit 的简单 C# 编辑器。
* [Consulo](https://consulo.io) - 支持 C# 和 Java 的跨平台 IDE，IntelliJ IDEA 社区版的分支
* [vvvv](https://visualprogramming.net) .NET 的可视化实时编程环境 **[OSS 免费]**
* [MongoDB 的 CSharp 分析器](https://github.com/mongodb/mongo-csharp-analyzer) 面向 MongoDB 用户的免费 Visual Studio 扩展，可帮助将代码转换为 MongoDB 查询

## 图像处理

* [ImageWizard](https://github.com/usercode/ImageWizard) - 基于ASP.NET Core和ImageSharp / SkiaSharp / SvgNet / DocNET的图像处理Web服务
* [ImageResizer](https://imageresizing.net/) - 将命令添加到图像 URL 以在几毫秒内获取更改的版本。实时调整图像大小、编辑图像等。
* [ImageSharp](https://github.com/SixLabors/ImageSharp) - 用于处理图像文件的完全托管的跨平台库。
* [MagicScaler](https://github.com/saucecontrol/PhotoSauce) - 适用于 .NET 的高性能图像处理管道，专注于使复杂的成像任务变得简单。
* [MetadataExtractor](https://github.com/drewnoakes/metadata-extractor-dotnet) - 从图像文件中提取 Exif、IPTC、XMP、ICC 和其他元数据。
* [Emgu CV](http://www.emgu.com/wiki/index.php/Main_Page) - OpenCV 库的跨平台 .NET 包装器。
* [SimpleITK](https://simpleitk.org/) - 通往洞察力的简化路径。使用 Python、R、Java、C#、Lua、Ruby、TCL 和 C++ 进行开源多维图像分析。由 Insight Toolkit 社区为生物医学科学及其他领域开发。
* [Magick.NET](https://github.com/dlemstra/Magick.NET) - ImageMagick 库的 .NET 包装器。
* [OpenCvSharp](https://github.com/shimat/opencvsharp/) - .NET Framework 的 OpenCV 跨平台包装器。
* [PixelViewer](https://github.com/carina-studio/PixelViewer) - 跨平台（Windows/macOS/Linux）图像查看器，支持从文件读取原始亮度/YUV/RGB/ARGB/Bayer 像素数据并渲染它。还支持 10/16 位 YUV 和查看图像帧序列 (v1.99+)。
* [Colourful](https://github.com/tompazourek/Colourful) - 用于处理色彩空间的开源 .NET 库。
* [Unicolour](https://github.com/waacton/Unicolour) - .NET 的颜色转换、插值和比较。

## 安装工具

* [Wix Toolset](https://github.com/wixtoolset/wix) - 可用于打造 Windows 安装体验的最强大工具集
* [Squirrel](https://github.com/squirrel/squirrel.windows) - Squirrel 既是一组工具又是一个库，可以完全管理桌面 Windows 应用程序的安装和更新。
* [Chocolatey](https://github.com/chocolatey/choco) - 类似于“yum”或“apt-get”，但适用于 Windows。
* [Onova](https://github.com/Tyrrrz/Onova) - 桌面应用程序的无主见自动更新框架。

## 互动编程

* [.NET Interactive](https://github.com/dotnet/interactive) - .NET Interactive 利用 .NET 的强大功能并将其嵌入到您的交互式体验中。

## 国际化

* [MessageFormat.NET](https://github.com/jeffijoe/MessageFormat.NET) - .NET 中的 ICU MessageFormat 实现允许您编写上下文 UI 消息（PCL 库）
* [ResX Resource Manager](https://github.com/dotnet/ResXResourceManager) - 最流行的免费工具，用于使用基于 resx 的资源本地化所有类型的应用程序。

## 互操作性

* [CppSharp](https://github.com/mono/CppSharp) - 将 C++ API 呈现给 C# 的工具
* [pythonnet](https://github.com/pythonnet/pythonnet) - Python 和 .NET 互操作框架
* [pinvoke](https://github.com/dotnet/pinvoke) - 包含最新 Windows 操作系统的 P/Invoke 代码的库。
* [Pyrolite](https://github.com/irmen/Pyrolite) - 该库允许您的 Java 或 .NET 程序非常轻松地与
Python 世界。它使用 Pyro 协议来调用远程对象上的方法。

## 国际奥委会
* [Autofac](https://github.com/autofac/Autofac) - 令人上瘾的 .NET IoC 容器
* [DryIoc](https://github.com/dadhi/DryIoc) - 简单、快速、功能齐全的 IoC 容器。
* [Ninject](https://github.com/ninject/ninject) - .NET 依赖注入器的忍者
* [Spring.Net](https://github.com/spring-projects/spring-net) - Spring.NET 是一个开源应用程序框架，使构建企业 .NET 应用程序变得更加容易
* [Lamar](https://jasperfx.github.io/lamar/) - 快速 IoC 容器，针对 ASP.NET Core 和其他 .NET 服务器端应用程序中的使用进行了高度优化。
* [LightInject](https://github.com/seesharper/LightInject) - 超轻量级 IoC 容器
* [Simple Injector](https://github.com/simpleinjector/SimpleInjector) - Simple Injector 是一个易于使用的 .NET 4+ 依赖注入 (DI) 库，支持 Silverlight 4+、Windows Phone 8、Windows 8（包括通用应用程序和 Mono）。
* [Microsoft.Extensions.DependencyInjection](https://github.com/dotnet/runtime/tree/main/src/libraries/Microsoft.Extensions.DependencyInjection) - NET 应用程序的默认 IoC 容器。
* [Scrutor](https://github.com/khellang/Scrutor) - Microsoft.Extensions.DependencyInjection 的程序集扫描扩展。
* [VS MEF](https://github.com/Microsoft/vs-mef) - Visual Studio 使用的托管扩展性框架 (MEF) 实现。
* [Stashbox](https://github.com/z4kn4fein/stashbox) - 用于基于 .NET 的解决方案的轻量级、可移植的依赖项注入框架。

## JavaScript 引擎

* [ClearScript](https://github.com/Microsoft/ClearScript) - 一个库，可以轻松地将脚本添加到 .NET 应用程序中。它目前支持 JavaScript（通过 V8 和 JScript）和 VBScript。
* [Edge.js](https://github.com/tjanczuk/edge) - 在 Windows、macOS 和 Linux 上运行 .NET 和 Node.js 进程内代码
* [Jint](https://github.com/sebastienros/jint) - 适用于 .NET 的 JavaScript 解释器提供完全的 ECMA 5.1 合规性，并且可以在任何 .NET 平台上运行。
* [Jurassic](https://github.com/paulbartrum/jurassic) - ECMAScript 语言和运行时的实现。它旨在为 .NET 提供性能最佳且最符合标准的 JavaScript 实现。
* [YantraJS](https://github.com/yantrajs/yantra) - 适用于 .NET Standard 的 JavaScript 运行时（类似于 NodeJS），将 JavaScript 编译为 IL，支持许多 ES6 功能、生成器、CommonJS 模块、CSX 模块和表达式编译器。

## 记录

* [NLog](https://github.com/nlog/NLog/) - NLog - 高级 .NET 和 Silverlight 日志记录
* [Logazmic](https://github.com/ihtfw/Logazmic) - 适用于 Windows 的开源 NLog 查看器
* [ELMAH](https://elmah.github.io/) - ELMAH 官方网站
* [Elmah MVC](https://github.com/alexbeletsky/elmah-mvc) - 用于 MVC 的 Elmah
* [Logary](https://github.com/logary/logary) - Logary 是一个适用于 Mono 和 .NET 的高性能、多目标日志记录、指标、跟踪和运行状况检查库。 .NET 对 DropWizard 的回答。支持许多为微服务构建的目标。
* [Log4Net](https://logging.apache.org/log4net/) - Apache log4net库是一个帮助程序员将日志语句输出到各种输出目标的工具
* [Rollbar.NET](https://github.com/rollbar/Rollbar.NET) - 简化使用 Rollbar.com 时的实时远程错误监控。适用于任何基于 .NET 的技术堆栈的开源 Rollbar Notifier SDK。该 SDK 可在基于以下 .NET 版本构建的任何应用程序中使用：.NET Core 2.0+、.NET Standard 2.0+、.NET Full Framework 4.5.1+、Mono、Xamarin 以及通常的 .NET Standard 2.0+ 的任何实现。它简化了基于异常数据、跟踪数据、信息消息和遥测数据的数据有效负载的构建，并将有效负载发送到 Rollbar API 以远程监控和分析托管应用程序的行为。 **[连接到专有服务]** **[免费套餐]**
* [Sentry](https://github.com/getsentry/sentry-dotnet) - .NET SDK for [Sentry](https://sentry.io/welcome/) 开源错误跟踪，可帮助开发人员实时监控和修复崩溃。
* [Serilog](https://github.com/serilog/serilog) - NoSQL 时代的严肃日志库。将传统诊断日志记录和结构化诊断日志记录的优点结合在一个易于使用的软件包中。
* [StackExchange.Exceptional](https://github.com/NickCraver/StackExchange.Exceptional) - 用于 Stack Exchange 网络的错误处理程序
* [ULogViewer](https://github.com/carina-studio/ULogViewer) - 跨平台（Windows/macOS/Linux）通用日志查看器，支持读取和解析各种类型的日志。您还可以定义自己的配置文件来解析和显示日志。
* [Foundatio](https://github.com/FoundatioFx/Foundatio#logging) - 流畅的日志记录 API，可用于在整个应用程序中记录消息。
* [Exceptionless](https://github.com/exceptionless/Exceptionless.Net) - 无异常的 .NET 客户端
* [Loupe](https://onloupe.com) - 集中式 .NET 日志记录和监控。 **[专有]** **[免费套餐]**
* [elmah.io](https://elmah.io) - 使用 ELMAH 的 .NET Web 应用程序的云日志记录。在上线之前查找错误。强大的搜索、API、与 Slack、GitHub、Visual Studio 等的集成。 **[[OSS 免费](https://elmah.io/sponsorship/opensource)]** **[$]**
* [BugSnag](https://docs.bugsnag.com/platforms/dotnet/) - 记录错误。包括有用的诊断信息，如堆栈跟踪、会话、版本等。有免费套餐。 **[OSS 免费][$]**
* [ZeroLog](https://github.com/Abc-Arbitrage/ZeroLog) - ZeroLog 是一个零分配 .NET 日志库。它提供了基本的日志记录功能，可用于延迟敏感的应用程序，在这些应用程序中不需要垃圾收集。
* [AutoLoggerMessage](https://github.com/stbychkov/AutoLoggerMessage) - 一个源生成器，可自动将所有日志记录调用迁移到高性能“LoggerMessage”版本。

## 机器学习和数据科学
* [Infer.NET](https://dotnet.github.io/infer/) - 用于在图形模型中运行贝叶斯推理的框架。它还可以用于概率编程。
* [Catalyst](https://github.com/curiosity-ai/catalyst) 受 spaCy 启发的跨平台自然语言处理 (NLP) 库，具有预训练模型、对训练单词和文档嵌入的开箱即用支持以及灵活的实体识别模型。 [SciSharp 堆栈](https://sciSharp.github.io/SciSharp/) 的一部分
* [FsLab](https://fslab.org/) - 适用于 F# 和 .NET 的数据科学和机器学习库的集合
* [GeneticSharp](https://github.com/giacomelli/GeneticSharp) - 适用于 .NET Core 和 .NET Framework 的多平台遗传算法库。该库有多种 GA 算子的实现，例如：选择、交叉、变异、重新插入和终止。
* [ML.NET](https://github.com/dotnet/machinelearning) - 跨平台开源机器学习框架，使 .NET 开发人员可以使用机器学习。
* [F# Data](https://github.com/fsprojects/FSharp.Data) - 用于访问 XML、JSON、CSV 和 HTML 文件（基于示例文档）以及访问 WorldBank 数据的 F# 类型提供程序
* [SciSharp STACK](https://scisharp.github.io/SciSharp/) - 通过将最流行的 Python 库移植到 C# 创建的丰富的 .NET 机器学习生态系统。
* [OpenGA.Net](https://github.com/asarnaout/OpenGeneticAlgorithm.NET) - 用于解决优化问题的遗传算法.NET 库，具有可扩展运算符和自适应策略选择。

## Markdown 处理器
* [F# Formatting](https://fsprojects.github.io/FSharp.Formatting/) - 用于记录 F# 和 C# 项目的工具。  该库包含可扩展的 Markdown 解析器作为核心组件。
* [markdig](https://github.com/lunet-io/markdig) - 适用于 .NET 的快速、功能强大、兼容 CommonMark、可扩展的 Markdown 处理器。

## 邮件

* [MailKit](https://github.com/jstedfast/MailKit) - 完整的跨平台邮件堆栈，包括 IMAP、POP3、SMTP、身份验证等。建立在 MimeKit 之上。
* [MailKitSimplified](https://github.com/danzuep/MailKitSimplified) - MailKit 的全功能流畅包装器，使发送和接收电子邮件尽可能简单。
* [MimeKit](https://github.com/jstedfast/MimeKit) - 跨平台 .NET MIME 创建和解析器库，支持 S/MIME、PGP、TNEF 和 Unix mbox 线轴。
* [PreMailer.Net](https://github.com/milkshakesoftware/PreMailer.Net) - C# 库可将样式表移动到内联样式属性，以最大程度地兼容电子邮件客户端。
* [StrongGrid](https://github.com/Jericho/StrongGrid) - SendGrid v3 API 的客户端。不仅允许您发送电子邮件，还允许您批量导入联系人、管理列表和细分、为列表创建自定义字段等。还包括 SendGrid Webhooks 的解析器。

## 数学

* [MathFlow](https://github.com/Nonanti/MathFlow) - 全面的数学表达式库，具有符号计算支持，包括微分、简化和方程求解。
* [MathNet](https://www.mathdotnet.com/) - Math.NET 是一项开源计划，旨在构建和维护涵盖基础数学的工具包，满足 .NET 开发人员的高级需求和日常需求
* [Microsoft Automatic Graph Layout](https://github.com/Microsoft/automatic-graph-layout) - 一组用于图形布局和查看的工具。
* [ALGLIB](https://www.alglib.net/) - ALGLIB 是一个跨平台的数值分析和数据处理库。它支持多种编程语言（C++、C#、Delphi）和多种操作系统（Windows 和 POSIX，包括 Linux）**[专有]** 和 **[免费版]**
* [GeometRi](https://github.com/RiSearcher/GeometRi.CSharp) - .Net 的简单且轻量级的计算几何库
* [Rationals](https://github.com/tompazourek/Rationals) - .NET 任意精度有理数算术的实现。
* [MKL.NET](https://github.com/AnthonyLloyd/MKL.NET) - 适用于英特尔 MKL 的简单跨平台 .NET API。
* [AngouriMath](https://github.com/asc-community/AngouriMath) - 一个开源符号/计算机代数库，主要针对 C# 和 F# 制作。它涵盖了一系列功能，可以被视为 .NET 中 SymPy 的替代品。
* [WPF-Math](https://github.com/ForNeVeR/wpf-math) - 用于使用 LaTeX 排版样式呈现数学公式的 .NET 库，适用于 WPF 框架
* [Jodo.Numerics](https://github.com/JosephJShort/Jodo/#numerics) - 提供额外的数字类型（例如定点和非溢出数字），全面支持运算符、数学、字符串解析等。经过广泛测试，跨平台兼容。

## 媒体

* [CSCore](https://github.com/filoe/cscore) - 先进的音频库，支持实时播放/录制、解码/编码和音频数据处理（效果、可视化……）。
* [TagLib#](https://github.com/mono/taglib-sharp) - TagLib#（又名 taglib-sharp）是一个用于读写的库
媒体文件中的元数据，包括视频、音频和照片格式
* [LibVLCSharp](https://github.com/videolan/libvlcsharp) - libvlc 的 Xamarin 绑定，libvlc 是为 VideoLAN 制作的 VLC 应用程序提供支持的多媒体框架。
* [NAudio](https://github.com/naudio/NAudio) - 播放、解码和编码多种文件格式的音频，如 MP3、MP4、WAV、AIFF、Speex 等。
* [Xabe.FFmpeg](https://github.com/tomaszzmuda/Xabe.FFmpeg) - FFmpeg 的 .NET 标准包装器。它允许在不知道 FFmpeg 如何工作的情况下处理媒体，并且可用于将自定义参数从 C# 应用程序传递给 FFmpeg。 **[$]**
* [Sonora](https://github.com/ImAxel0/Sonora) - 用于音频和 MIDI 播放、编辑和插件集成的 .NET 音频框架。

## 指标

* [Foundatio](https://github.com/FoundatioFx/Foundatio#metrics) - 与内存、Redis、StatsD 和 Metrics.NET 实现的通用接口。

## 微框架


## 缩小化

* [Web Markup Minifier](https://github.com/Taritsyn/WebMarkupMin) - 包含一组标记缩小器的.NET 库。该项目的目标是通过减少 HTML、XHTML 和 XML 代码的大小来提高 Web 应用程序的性能。
* [CompressedStaticFiles](https://github.com/AnderssonPeter/CompressedStaticFiles) - 将压缩的静态文件发送到浏览器，而无需按需压缩，还支持在浏览器指示支持时发送更高级的图像格式。

## 杂项
* [RazorKit](https://github.com/ekondur/RazorKit) - RazorKit 是轻量级、流畅风格的 Razor HTML 帮助程序的集合，使开发人员可以轻松地将流行的 JavaScript 库集成到他们的 ASP.NET 应用程序中。
* [CSharp Pad](http://csharppad.com) - 基于 Web 的 C# REPL，具有出色的代码补全功能。
* [AzureCrawler](https://github.com/yagopv/AzureCrawler) - 为您的 Angular、Ember、Durandal 或任何 JavaScript 应用程序拍摄 HTML 快照
* [CSScript](https://www.cs-script.net/) - CS-Script 是一个基于 CLR 的脚本系统，使用 C# 作为编程语言。 CS-Script 目前针对 CLR (.NET 2.0/3.0/3.5/4.0/4.5) 的 Microsoft 实现，并完全支持 Mono。附带许多附加功能，例如脚本托管。
* [CsvHelper](https://github.com/JoshClose/CsvHelper) - 帮助读取和写入 CSV 文件的库 https://github.com/JoshClose/CsvHelper
* [RecordParser](https://github.com/leandromoh/recordparser) - 帮助以零堆分配读取和写入 CSV 和平面文件的库。
* [Sep](https://github.com/nietras/Sep) - 世界上最快的 .NET CSV 解析器。现代、最小、快速、零分配、读取和写入分隔值（`csv`、`tsv` 等）。跨平台、可调整且兼容 AOT/NativeAOT。
* [ConsoleTableExt](https://github.com/minhhungit/ConsoleTableExt) - 用于为 .Net 控制台应用程序创建表的 Fluent 库。
* [FluentValidation](https://github.com/FluentValidation/FluentValidation) - .NET 的小型验证库，使用流畅的接口和 lambda 表达式来构建验证规则。
* [Validot](https://github.com/bartoszlenar/Validot) - Validot 是一个性能优先、紧凑的库，用于高级模型验证。使用简单的声明式流畅接口，它可以有效地处理类、结构、嵌套成员、集合、可空值以及它们的任何关系或组合。它还支持翻译、带有测试的自定义逻辑扩展和 DI 容器。
* [Humanizer](https://github.com/Humanizr/Humanizer) - Humanizer 满足您操作和显示字符串、枚举、日期、时间、时间跨度、数字和数量的所有 .NET 需求
* [LINQPad](https://www.linqpad.net) - 一个 C#/VB/F# 暂存器，可立即执行任何表达式、语句块或程序，具有丰富的输出格式和丰富的功能。还允许您在 LINQ 中交互式查询数据库。 [$]
* [LINQPad.QueryPlanVisualizer](https://github.com/Giorgi/LINQPad.QueryPlanVisualizer/) - 直接在 LINQPad 内查看 SQL Server 和 Postgres 查询计划。
* [Polly](https://github.com/App-vNext/Polly) - 以流畅的方式表达瞬态异常处理和弹性策略，例如重试、等待和重试、断路器和舱壁隔离。完全线程安全和完全异步支持。  （4.0 / 4.5 / .NET Core / .NET Standard / Xamarin）。
* [Aeron.NET](https://github.com/AdaptiveConsulting/Aeron.NET) - 高效可靠的 UDP 单播、UDP 多播和 IPC 消息传输 - Aeron 的 .NET 端口
* [TypeShape](https://github.com/eiriktsarpalis/TypeShape) - TypeShape 是一个小型、可扩展的 F# 库，用于实用的泛型编程
* [ByteSize](https://github.com/omar/ByteSize) - ByteSize 是一个实用程序类，它通过消除所表示的值的歧义来使代码中的字节大小表示更加容易。 ByteSize 与字节的关系就像 System.TimeSpan 与时间的关系一样。
* [Jot](https://github.com/anakic/jot) - 用于保存和恢复应用程序状态的库（.settings 文件的更好替代方案）。
* [Enums.NET](https://github.com/TylerBrinkley/Enums.NET) - Enums.NET 是一个高性能类型安全的 .NET 枚举实用程序库
* [YoutubeExplode](https://github.com/Tyrrrz/YoutubeExplode) - 用于提取元数据和下载 YouTube 视频和播放列表的终极库。
* [DeviceId](https://github.com/MatthewKing/DeviceId) - 生成可用于唯一标识计算机的“设备 ID”。
* [DeviceDetector.NET](https://github.com/totpero/DeviceDetector.NET) - 通用设备检测库将解析任何用户代理并检测浏览器、操作系统、使用的设备（台式机、平板电脑、移动设备、电视、汽车、控制台等）、品牌和型号。
* [NaturalSort.Extension](https://github.com/tompazourek/NaturalSort.Extension) - StringComparer 的扩展方法，添加了对自然排序的支持（例如“abc1”、“abc2”、“abc10”而不是“abc1”、“abc10”、“abc2”）。
* [Coravel](https://github.com/jamesmh/coravel) 近乎零配置的 .NET Core 库，使任务调度、缓存、排队、邮件、事件广播（等等）变得轻而易举！
* [Build Versioning](https://github.com/TurnerSoftware/BuildVersioning) - .NET 的简单构建版本控制，由 Git 标签提供支持
* [SystemTextJson.JsonDiffPatch](https://github.com/weichch/system-text-json-jsondiffpatch) - System.Text.Json 的高性能、低分配 JSON 对象差异和补丁扩展。支持生成 RFC 6902 JSON Patch 格式的补丁文档。
* [dotnet-exec](https://github.com/WeihanLi/dotnet-exec) - 一个无需项目文件即可执行 C# 程序的命令行工具，您可以拥有除 Main 方法之外的自定义入口点。
* [ComputeSharp](https://github.com/Sergio0694/ComputeSharp) - 一个 .NET 库，可通过 DX12、D2D1 以及动态生成的 HLSL 计算和像素着色器在 GPU 上并行运行 C# 代码。
* [ILGPU](https://github.com/m4rs-mt/ILGPU) - 用于使用基于 .Net 的语言编写的高性能 GPU 程序的 JIT（即时）编译器。

## MQTT

* [HiveMQtt](https://github.com/hivemq/hivemq-mqtt-client-dotnet) - 适用于 .NET 的 HiveMQ C# MQTT 客户端
* [MQTTNet](https://github.com/dotnet/MQTTnet) - 用于基于 MQTT 通信的高性能 .NET 库。它提供了 MQTT 客户端和 MQTT 服务器（代理）。

## MVVM

* [Community Toolkit](https://github.com/CommunityToolkit) - 各种 .NET 技术的控件和帮助程序库以及示例的集合。包含由 Microsoft 支持的现代 MVVM 库。包括 [Windows 社区工具包](https://github.com/CommunityToolkit/WindowsCommunityToolkit)、[MAUI 社区工具包](https://github.com/CommunityToolkit/Maui) 和 [Dotnet 社区工具包](https://github.com/CommunityToolkit/dotnet)。
* [Caliburn.Micro](https://github.com/Caliburn-Micro/Caliburn.Micro) - 一个小型但功能强大的框架，旨在跨所有 XAML 平台构建应用程序。它对 MV* 模式的强大支持将使您能够快速构建解决方案，而无需牺牲代码质量或可测试性。
* [Catel](https://github.com/Catel/Catel) - Catel 是一个专注于 MVVM（WPF、Silverlight、Windows Phone 和 WinRT）和 MVC（ASP.NET MVC）的应用程序开发平台。 Catel的核心包含IoC容器、模型、验证、备忘录、消息中介、参数检查等。
* [ReactiveUI](https://github.com/reactiveui/reactiveui/) - .NET 的 MVVM 框架集成了响应式扩展 (Rx) 框架，使开发人员能够使用 WPF、Windows 应用商店应用程序、WP8 或 Xamarin 构建优雅、可测试的应用程序。
* [Prism](https://github.com/PrismLibrary/Prism) - 跨平台桌面和移动 MVVM 开发框架。
* [Win Application Framework (WAF)](https://github.com/jbe2277/waf) - 一个轻量级框架，可帮助您创建结构良好的 WPF 和 UWP 应用程序。它支持您应用分层架构和模型-视图-视图模型模式。
* [MVVMCross](https://github.com/MvvmCross/MvvmCross) - 适用于 WPF、适用于 WP7 和 WP8 的 Silverlight、适用于 Android 的 Mono、适用于 iOS 的 MonoTouch、Windows 通用项目（WPA8.1 和 Windows 8.1 应用商店应用）的跨平台 mvvm 移动开发框架。广泛使用可移植类库 (PCL) 来提供可维护的跨平台 C# 本机应用程序。
* [Stylet](https://github.com/canton7/stylet/) - 受 Caliburn Micro 启发的最小 MVVM 框架，具有良好的文档、高测试覆盖率和自己的 IoC 容器
* [Toms Toolbox](https://github.com/tom-englert/TomsToolbox) - 可视化组合框架，可基于[托管扩展性框架 (MEF)](https://docs.microsoft.com/en-us/dotnet/framework/mef/) 轻松构建模块化 MVVM 应用程序。
* [MVVM Dialogs](https://github.com/FantasticFiasco/mvvm-dialogs) - 该框架简化了在 WPF 或 UWP 中使用 MVVM 时从视图模型打开对话框的概念。

## 网络

* [NetCoreServer](https://github.com/chronoxor/NetCoreServer) - 超快速、低延迟的异步套接字服务器和客户端 C# .NET Core 库，支持 TCP、SSL、UDP、HTTP、HTTPS、WebSocket 协议和 10K 连接问题解决方案 (NETStandard)。
* [SharpPcap](https://github.com/chmorgan/sharppcap) - 完全托管的跨平台（Windows、Mac、Linux）.NET 库，用于从实时设备和基于文件的设备捕获数据包。

## 对象到对象映射

* [AutoMapper](https://github.com/AutoMapper/AutoMapper) - .NET 中基于约定的对象到对象映射器。 https://automapper.org
* [Mapperly](https://github.com/riok/mapperly) - 用于生成对象映射的 .NET 源生成器。无运行时反射。
* [Mapster](https://github.com/MapsterMapper/Mapster) - .net 中的高性能对象映射器

## 办公室

* [ExcelDna](https://github.com/Excel-DNA/ExcelDna) - ExcelDna 使使用 C#、F# 或 VB .NET 创建和部署 Excel 加载项变得更加轻松
* [ClosedXML](https://github.com/ClosedXML/ClosedXML) - ClosedXML 使开发人员可以更轻松地创建 Excel 2007/2010 文件
* [OfficeIMO](https://github.com/EvotecIt/OfficeIMO) - OfficeIMO 使开发人员可以更轻松地创建/修改 Word (docx) 文件，而无需安装 Microsoft Word 或 Office
* [NPOI](https://github.com/tonyqus/npoi) - 该项目是 POI Java 项目的 .NET 版本，位于 https://poi.apache.org/。
* [EPPlus](https://github.com/EPPlusSoftware/EPPlus) - EPPlus 是一个 .NET 库，它使用 Open Office XML 格式 (xlsx) 读取和写入 Excel 2007/2010 文件。
**[可用来源]** **[免费套餐]**
* [Open XML SDK](https://github.com/officedev/open-xml-sdk) - Open XML SDK 提供了用于处理 Open XML 文档（DOCX、XLSX 和 PPTX）的开源库。
* [DocX](https://github.com/xceedsoftware/DocX) - DocX 是一个 .NET 库，允许开发人员操作 Word 2007/2010/2013 文件，不需要安装 Microsoft Word 或 Office。
* [ExcelDataReader](https://github.com/ExcelDataReader/ExcelDataReader) - 用 C# 编写的轻量级快速库，用于读取 Microsoft Excel 文件 (2.0-2007)。
* [NetOffice](https://github.com/NetOfficeFw/NetOffice) - Microsoft Office 应用程序的.NET 包装程序集。
* [GemBox.Bundle](https://www.gemboxsoftware.com/bundle) - .NET 组件包，可快速、简单且高效地处理办公文件（Excel、Word、PowerPoint、PDF 和电子邮件）。 **[$]****[免费精简版]**
* [Outlook Redemption](http://www.dimastr.com/redemption/home.htm) - 用于与 Outlook 对象模型和（扩展）MAPI 配合使用的库。  支持 Outlook 98 - 2019。在 Exchange 和 Outlook 中处理对象/邮件/帐户/文件夹。 **[$]**
* [ShapeCrawler](https://github.com/ShapeCrawler/ShapeCrawler) - 流畅的 API，用于在未安装 Microsoft Office 的情况下处理 PowerPoint 演示文稿。
* [MiniExcel](https://github.com/shps951023/MiniExcel) - 微型 Excel 助手可避免 OOM 并提高创建/映射/模板填充数据的性能。
* [MatchFlow](https://github.com/datpham0412/invoice-processor) - 基于 Web 的发票核对平台，使用 ASP.NET Core 和 Azure Form Recognizer 进行 OCR 提取和自动采购订单匹配。
* [Toxy](https://github.com/nissl-lab/toxy) - .NET 文本提取框架支持几种文件格式
* [Syncfusion .NET Word Framework](https://www.syncfusion.com/document-processing/word-framework/net) - 高性能 .NET Word 框架，无需 Microsoft Office 或互操作依赖项。无缝创建、阅读和编辑 Word 文档。利用高级编辑器组件轻松查看、编辑和打印。使用强大的转换 API 轻松将 Word 文档转换为 PDF、HTML、RTF、ODT 和 EPUB 格式。 **[$]** **[[个人和小型企业免费](https://www.syncfusion.com/products/communitylicense)]**
* [Syncfusion .NET Excel Framework](https://www.syncfusion.com/document-processing/excel-framework/net) - 高性能 .NET Excel 框架，无需 Microsoft Office 或互操作依赖项。无缝创建、阅读和编辑 Excel 文档。利用电子表格控件轻松创建、编辑和查看。使用强大的转换 API 轻松将 Excel 文件转换为 PDF、图像等。 **[$]** **[[个人和小型企业免费](https://www.syncfusion.com/products/communitylicense)]**
* [Syncfusion .NET PowerPoint Framework](https://www.syncfusion.com/document-processing/powerpoint-framework/net) - 高性能 .NET PowerPoint 框架，无需 Microsoft Office 或互操作依赖项。无缝创建、阅读和编辑 PowerPoint 文件。使用强大的转换 API 轻松将 PowerPoint 文件转换为 PDF 和图像。 **[$]** **[[个人和小型企业免费](https://www.syncfusion.com/products/communitylicense)]**

## 开放人工智能


## ORM

* [Entity Framework Core](https://github.com/dotnet/efcore) - 对象关系映射器，使 .NET 开发人员能够使用特定于域的对象来处理关系数据
* [EntityFramework.Exceptions](https://github.com/Giorgi/EntityFramework.Exceptions) - 当 SQL 查询违反 SqlServer、MySql、PostgreSQL 或 SQLite 中的数据库约束时，使用 Entity Framework Core 的类型化异常
* [EntityFrameworkCore.SqlServer.SimpleBulks](https://github.com/phongnguyend/EntityFrameworkCore.SqlServer.SimpleBulks) - 简单的库，可以帮助将内存中的大量记录同步到数据库中。支持 Lambda 表达式。
* [EFCore.BulkExtensions](https://github.com/borisdj/EFCore.BulkExtensions) - 实体框架核心批量扩展，用于在多个数据库上实现超快速（批量复制）CRUD 操作 + SaveChanges：SQL、PG、My、Lite。
* [Dapper](https://github.com/DapperLib/Dapper) - [StackExchange](https://stackexchange.github.io/) 的 .NET 简单对象映射器
* [Dapper.FastCRUD](https://github.com/MoonStorm/Dapper.FastCRUD) - Dapper 最快的微 ORM 扩展
* [DapperQueryBuilder](https://github.com/Drizin/DapperQueryBuilder) - 使用字符串插值和 Fluent API 的 Dapper 查询生成器
* [SqlSugar](https://github.com/DotNetNext/SqlSugar) - 另一个 ORM 库支持许多 RDBMS，包括 MySql、SqlServer、Sqlite、Oracle、Postgresql - **注意**：这与 Microsoft 或 .NET 无关
* [FreeSql](https:/github.com/dotnetcore/FreeSql) - a convenient ORM in dotnet, supports MySql, SqlServer, PostgreSQL, Oracle, Sqlite, Firebird, 达梦, 人大金仓, 神舟通用, 翰高 and Access. -  **NOTE**: This is not affiliated with Microsoft or .NET
* [NHibernate](https://github.com/nhibernate) - NHibernate 对象关系映射器
* [Fluent NHibernate](https://github.com/nhibernate/fluent-nhibernate) - 流畅、无 XML、编译安全、自动化、基于约定的 NHibernate 映射。
* [FluentMigrator](https://github.com/fluentmigrator/fluentmigrator) - .net 的流畅迁移框架
* [ServiceStack.OrmLite](https://github.com/ServiceStack/ServiceStack/tree/main/ServiceStack.OrmLite) - 轻量、简单、快速的基于约定的 POCO ORM **[[OSS 免费](https://github.com/ServiceStack/ServiceStack/blob/master/license.txt)]** **[$]**
* [LINQ to DB](https://github.com/linq2db/linq2db) - 最快的 LINQ 数据库访问库在 POCO 对象和数据库之间提供简单、轻量、快速且类型安全的层。
* [PetaPoco](https://github.com/CollaboratingPlatypus/PetaPoco) - 适合 POCO 的类似 ORM 的小东西
* [NPoco](https://github.com/schotime/NPoco) - 将查询结果映射到 POCO 对象的简单 microORM。基于Schotime的PetaPoco分支
* [LLBLGen Pro](https://www.llblgen.com) - 适用于 Entity Framework、NHibernate、Linq to SQL 及其自己的 ORM 框架的实体建模解决方案：LLBLGen Pro Runtime Framework。 **[$][免费精简版]**
* [Insight.Database](https://github.com/jonwagner/Insight.Database) - Insight.Database 是适用于 .NET 的快速、轻量级微型 ORM
* [RepoDb](https://github.com/mikependon/RepoDb) - .NET 的混合 ORM 库。
* [MongoFramework](https://github.com/TurnerSoftware/MongoFramework) - MongoDB 的类似“实体框架”的接口
* [Friflo.Json.Fliox](https://github.com/friflo/Friflo.Json.Fliox) - 适用于 Sqlite、MySql、SqlServer、PostgreSQL 和 NoSQL 的高性能 ORM。为服务器提供 REST、GraphQL 和 WebSocket / PubSub API。

## 包管理

* [NuGet](https://www.nuget.org/) - .NET 包管理器
* [Cloudsmith](https://cloudsmith.com/nuget-feed/) - 完全托管的包管理 SaaS，支持 NuGet、Npm、Docker 等。 **[免费供公众/OSS]** **[$]**
* [MyGet](https://www.myget.org/) - NuGet、NPM、Bower 和 VSIX 的托管包存储库。还提供 CI 即服务。 **[$]**
* [Paket](https://github.com/fsprojects/Paket) - .NET 的包依赖项管理器，支持 NuGet 包和 GitHub 存储库。 https://fsprojects.github.io/Paket/
* [Sleet](https://github.com/emgarten/sleet/) - 支持 AWS S3 和 Azure 存储的 NuGet v3 静态源生成器

## PDF

* [QPdfSharp](https://github.com/svengeance/QPdfSharp) - 围绕 QPdf 编写的 C# 包装器，可轻松进行 PDF 操作，并在 Linux 和 Windows 上进行了测试。 QPdf 是唯一能够进行 PDF 线性化的库之一，这个包装器可确保您及时了解底层改进。
* [Cloudmersive PDF](https://cloudmersive.com/pdf-api) - Cloudmersive PDF 是原生 .NET Framework 和 .NET Core NuGet 库和 API 服务，可以大规模高保真地创建、修改、加密或转换 PDF 文档；并且免费使用，无有效期 **[免费]**
* [Docotic.Pdf](https://bitmiracle.com/pdf-library/) - PDF 库，用于在 .NET 和 .NET Core 应用程序中创建、读取、编辑、绘制和打印 PDF 文档。 100% 托管，无不安全块。 **[$]** **[[OSS 免费](https://bitmiracle.com/pdf-library/free-pdf-library.aspx)]**
* [IText](https://github.com/itext/itext-dotnet) - iText 是一个 PDF 库，允许您以可移植文档格式 (PDF) 创建、调整、检查和维护文档**[$]** **[OSS 免费]**
* [Pdfium.Net SDK](https://pdfium.patagames.com/) - 高级 C# PDF 库，用于渲染、创建、编辑、合并、拆分、打印和查看 PDF。开源 PDF 查看器可在 [GitHub](https://github.com/patagames) 上找到。 [NuGet 包](https://www.nuget.org/packages/Pdfium.Net.SDK/) 也可用于轻松包含到您的项目中。**[$]**
* [PdfPig](https://uglytoad.github.io/PdfPig/) - 使用 C# 读取、创建和提取 PDF 中的文本和其他内容（PdfBox 的端口）
* [QuestPDF](https://www.questpdf.com/) - QuestPDF 是一个经过考验的现代库，可以通过提供友好、可发现和可预测的 C# 流利 API 来帮助您生成 PDF 文档。 **[可用来源]** **[OSS 免费]**
* [Kevsoft.PDFtk](https://github.com/kevbite/Kevsoft.PDFtk) - 一个用于驱动出色的 pdftk 二进制文件的包装器，它可以填充 PDF 表单、获取字段信息、连接多个文档或页面、分割文档、添加或替换图章，并且可以将文件附加到页面或从页面下载文件。
* [IronPDF](https://ironpdf.com/) - 高性能 C# PDF 库，兼容各种 .NET 版本、HTML 到 PDF 转换、内容页面转换、文件格式支持（例如 DOCX、RTF、MD）、响应式布局和强大的 PDF 功能，包括兼容性、生成 PDF、格式化 PDF 和编辑 PDF。 **[$]** **[免费试用]**
* [Syncfusion .NET PDF Framework](https://www.syncfusion.com/document-processing/pdf-framework/net) - 不依赖 Adobe 的高性能 .NET PDF 框架。无缝创建、阅读和编辑 PDF 文件。利用 PDF 查看器控件轻松查看、审阅和打印。使用强大的转换 API 轻松将 HTML、Word、Excel、PowerPoint 文件和图像转换为 PDF。 **[$]** **[[个人和小型企业免费](https://www.syncfusion.com/products/communitylicense)]**

## 分析器

* [MiniProfiler](https://github.com/MiniProfiler/dotnet) - 一个简单但有效的 ASP.NET 网站迷你分析器

## 协议

* [SSH.NET](https://github.com/sshnet/SSH.NET) - 用于 .NET 的 Secure Shell (SSH) 库，针对并行性进行了优化。提供SSH命令、SFTP/SCP上传下载、SOCKS4/SOCKS5/HTTP代理。
* [FluentFTP](https://github.com/robinrodricks/FluentFTP) - 用于 .NET 的 FTP 和 FTPS 库，针对速度进行了优化。提供广泛的 FTP 命令、文件上传/下载和 FTP 代理。
* [SharpSnmpLib](https://docs.sharpsnmp.com/) - .NET/Mono/Xamarin 的开源 SNMP 实现。支持版本 1、2c 和 3。
* [DnsClient.NET](https://github.com/MichaCo/DnsClient.NET) - 一个简单但非常强大且高性能的开源库，用于 .NET Framework 进行 DNS 查找。
* [Tecan SiLA2 SDK](https://gitlab.com/SiLA2/vendors/sila_tecan) - 用于开发 SiLA2 客户端和服务器的库和代码生成器。

## 推送通知


## 查询生成器
* [SqlKata](https://sqlkata.com) - 优雅的 SQL 查询构建器，支持复杂查询、联接、子查询、嵌套 where 条件、供应商引擎目标等
* [InterpolatedSql](https://github.com/Drizin/InterpolatedSql) - 使用字符串插值和 Fluent API 的 SQL Builder

## 队列
* [CAP](https://github.com/dotnetcore/CAP) - 具有 RabbitMQ 或 Kafka 本地持久消息功能的 EventBus。 - **注意**：这与 Microsoft 或 .NET 无关
* [Cap.Outbox](https://github.com/dex-it/dex-common/tree/main/src/Dex.Cap) - 实现Outbox模式和保证幂等性的OnceExecutor服务：操作将被执行一次
* [NServiceBus](https://github.com/Particular/NServiceBus) - 最流行的 .NET 服务总线
* [Hangfire](https://github.com/HangfireIO/Hangfire) - 在 ASP.NET 应用程序中执行即发即忘、延迟和重复任务的极其简单的方法
* [RabbitMQ.NET](https://github.com/rabbitmq/rabbitmq-dotnet-client) - C# 的 AMQP 客户端库的实现，以及通过 WCF 公开 AMQP 服务的绑定
* [NetMQ](https://github.com/zeromq/netmq) - NetMQ 是 ZeroMQ 的 100% 原生 C# 端口
* [MassTransit](https://github.com/MassTransit/MassTransit) - MassTransit 是精益服务总线实现，用于使用 .NET Framework 构建松散耦合的应用程序。
* [Rebus](https://github.com/rebus-org/Rebus) - Rebus 是 .NET 的精益服务总线实现，本质上与 NServiceBus 和 MassTransit 类似，只是更精益
* [EasyNetQ](https://github.com/EasyNetQ/EasyNetQ) - 易于使用的 RabbitMQ .NET API
* [Warewolf ESB](https://github.com/Warewolf-ESB/Warewolf) - 易于使用的服务总线和微服务平台。在可视化 IDE 中轻松构建应用程序和服务。
* [Confluent's .NET Client](https://github.com/confluentinc/confluent-kafka-dotnet) - Confluence 的 Apache Kafka .NET 客户端。
* [Streamiz](https://github.com/LGouellec/streamiz) - 用于 Apache Kafka 的 .NET 流处理库。
* [Foundatio](https://github.com/FoundatioFx/Foundatio#queues) - 与内存、Redis 和 Azure 实现的通用接口。
* [Brighter](https://github.com/BrighterCommand/Brighter) - 命令调度程序、处理器和分布式任务队列 https://www.goparamore.io/
* [Silverback](https://silverback-messaging.net) - 一个简单但功能丰富的 .NET core 消息总线（支持 Kafka、RabbitMQ 和 MQTT）。
* [SlimMessageBus](https://github.com/zarusz/SlimMessageBus) - 轻量级消息总线，具有流行消息系统（Kafka、Redis、Azure 服务总线等）和内存通信的传输。
* [AsyncMonolith](https://github.com/Timmoth/AsyncMonolith) - 促进 dotnet 应用程序中的简单异步消息传递。
## 远程过程调用

* [gRPC](https://github.com/grpc/grpc-dotnet) .NET Core 的 RPC 库和框架。在 [Microsoft 文档](https://docs.microsoft.com/en-us/aspnet/core/grpc) 上了解更多相关信息
* [gRPCurl](https://github.com/fullstorydev/grpcurl) - gRPCurl 是一个命令行工具，可让您与 gRPC 服务器交互。它基本上是 gRPC 服务器的curl。
* [gRPC UI](https://github.com/fullstorydev/grpcui) - gRPC UI 是一个命令行工具，可让您通过浏览器与 gRPC 服务器交互。它有点像 Postman，但针对的是 gRPC API，而不是 REST。

## 反应式编程

* [Rx.NET](https://github.com/dotnet/reactive) - Reactive Extensions (Rx) 是一个使用可观察序列和 LINQ 样式查询运算符来编写异步和基于事件的程序的库
* [Dynamic Data](https://github.com/reactivemarbles/DynamicData) - 集合的反应式扩展 (Rx)

## 实时通讯

* [SIPSorcery](https://github.com/sipsorcery/sipsorcery) - 支持 SIP、VoIP 和 WebRTC 的跨平台 C# .NET 库。

## 正则表达式

## 调度

* [NCrontab](https://github.com/atifaziz/NCrontab) - 用于解析和格式化 [crontab](http://crontab.org/) 表达式以及根据 crontab 计划计算时间出现的类库
* [NCrontab.Scheduler](https://github.com/thomasgalliker/NCrontab.Scheduler) - 用于调度基于 Ncrontab 的任务的简单任务调度程序库
* [QuartzNet](https://github.com/quartznet/quartznet) - Quartz 企业调度程序 .NET
* [Hangfire](https://github.com/HangfireIO) - 在 .NET 应用程序中执行即发即忘、延迟和重复任务的简单方法
* [DurableTask](https://github.com/Azure/durabletask) - 该框架允许用户使用 async/await 功能在 C# 中编写长时间运行的持久工作流程。
* [Workflow Core](https://github.com/danielgerlag/workflow-core) - 轻量级嵌入式工作流引擎
* [Occurify](https://github.com/Occurify/Occurify) - 一个强大且直观的 .NET 库，用于定义、过滤、转换和调度即时和周期时间线。
* [TickerQ](https://github.com/Arcenox-co/TickerQ) - 适用于 .NET 的轻量级、高性能、无反射作业调度程序，具有 EF Core、基于 cron/时间的执行、自定义锁定和重试支持。
* [NCronJob](https://github.com/NCronJob-Dev/NCronJob) - 位于 dotnet 中 IHostedService 之上的作业调度程序。
* [NaturalCron](https://github.com/hugoj0s3/NaturalCron) - 使用自然语言表达式的人类可读的 .NET 调度库。


## SDK 和 API 客户端

* [AWS SDK](https://github.com/aws/aws-sdk-net) - 适用于 .NET 的 AWS 开发工具包使 .NET 开发人员能够轻松使用 Amazon Web Services
* [Azure PowerShell](https://github.com/Azure/azure-powershell) - 一组供开发人员和管理员开发、部署和管理 Microsoft Azure 应用程序的 PowerShell cmdlet
* [Countly SDK for Windows](https://github.com/Countly/countly-sdk-windows/) - 适用于产品和营销经理的 Countly 分析和营销平台的 Windows SDK
* [Octokit.NET](https://github.com/octokit/octokit.net) - 适用于 .NET 的 GitHub API 客户端库
* [Dropbox.NET](https://github.com/dropbox/dropbox-sdk-dotnet) - 适用于 Dropbox API 的官方 .NET SDK
* [Getty Images API SDK](https://github.com/gettyimages/gettyimages-api_dotnet) - 适用于 Getty Images 和 iStock API 的 SDK

## 搜索

* [Elasticsearch .NET](https://github.com/elastic/elasticsearch-net) - Elasticsearch.Net 和 NEST
* [SolrNet](https://github.com/SolrNet/SolrNet) - 适用于 .NET 的 Solr 客户端
* [Lucene.net](https://lucenenet.apache.org/) - Lucene.Net 是 Lucene 搜索引擎库的一个端口，用 C# 编写，面向 .NET 运行时用户

**嵌入式搜索库** - 类似于 lucene，但更易于使用。
  * [Lunr-Core](https://github.com/bleroy/lunr-core) - Lunr-core 是一个小型全文搜索库，适用于小型应用程序。它是 LUNR.js 的 .NET 端口。
  * [hOOt](https://github.com/mgholam/hOOt) - 最小的全文搜索引擎（lucene 替代）。使用反向Roaring位图索引从头开始构建，高度紧凑的存储，在数据库和文档模式下运行
  * [ZoneTree.FullTextSearch](https://github.com/koculu/ZoneTree.FullTextSearch) - 高效的全文搜索库。扩展 ZoneTree。它是快速的嵌入式搜索引擎，适合需要高性能且不依赖外部数据库的应用程序。

## 序列化

* [CsvExport](https://github.com/jitbit/CsvExport) - 非常简单且轻量级的 CSV 导出器，Excel 友好，转义文本和引号等。
* [Protobuf.NET](https://github.com/protobuf-net/protobuf-net) - 协议缓冲区是 Google 用于大部分数据通信的二进制序列化格式的名称
* [Json.NET](https://github.com/JamesNK/Newtonsoft.Json) - 适用于 .NET 的流行高性能 JSON 框架
* [ServiceStack.Text]https://github.com/ServiceStack/ServiceStack/tree/main/ServiceStack.Text) - servicestack.net 中使用的 JSON、JSV 和 CSV 文本序列化器
* [Msgpack-Cli](https://github.com/msgpack/msgpack-cli) - 公共语言基础结构的 MessagePack 实现
* [FlatSharp](https://github.com/jamescourtney/FlatSharp) - 快速、惯用的 FlatBuffers 实现。使用 .fbs 文件或属性。
* [F# Data](https://fsprojects.github.io/FSharp.Data/) - 用于访问 XML、JSON、CSV 和 HTML 文件（基于示例文档）以及访问 WorldBank 数据的 F# 类型提供程序
* [Hyperion](https://github.com/akkadotnet/Hyperion) - 适用于 .NET 框架的高性能多态序列化器。
* [Migrant](https://github.com/antmicro/Migrant) - 快速灵活的序列化框架可用于未修饰的类。
* [ObjectDumper.NET](https://github.com/thomasgalliker/ObjectDumper) - 将内存中的对象序列化为 C# 代码。
* [FluentSerializer](https://github.com/Marvin-Brouwer/FluentSerializer#readme) - 适用于多种数据格式的基于配置文件的序列化器。

## 短信和电话

* [Twilio-csharp](https://github.com/twilio/twilio-csharp) - 用于使用 Twilio 发送和接收电话和短信的 C#/.NET 库。

## 状态机

* [Stateless](https://github.com/dotnet-state-machine/stateless) - 直接在 .NET 代码中创建状态机和基于状态机的轻量级工作流

## 静态站点生成器

* [Sandra.Snow](https://github.com/Sandra/Sandra.Snow) - 受 Jekyll 启发的 .NET 静态站点生成
* [AspNetStatic](https://github.com/ZarehD/AspNetStatic) - 将 ASP.NET Core Web 应用程序转变为静态站点生成器。

## 强命名

* [.NET Assembly Strong-Name Signer](https://github.com/brutaldev/StrongNameSigner) - 用于对 .NET 程序集进行强名称签名的实用程序软件，包括您没有源代码的程序集。

## 风格指南

* [C# Style Guide](https://stackoverflow.com/questions/4678178/style-guide-for-c) - StackOverflow 关于风格指南的问答
* [C# Coding Conventions](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/inside-a-program/coding-conventions) - 官方 MSDN C# 代码约定
* [C# Async Guidance](https://github.com/davidfowl/AspNetCoreDiagnosticScenarios/blob/master/AsyncGuidance.md) - .NET Core 有问题的异步模式列表以及如何解决这些问题的说明

## 模板引擎

* [RazorLight](https://github.com/toddams/RazorLight) - 基于微软Razor解析引擎的开源模板引擎，支持.NET Standard 2.0
* [DotLiquid](https://github.com/dotliquid/dotliquid) - Ruby Liquid 模板语言的 C# 端口
* [Scriban](https://github.com/lunet-io/scriban) - 快速、强大、安全且轻量级的 .NET 文本模板语言和引擎
* [Morestachio](https://github.com/JPVenson/morestachio) - 一个全尺寸的类似模板引擎，注重可扩展性。
* [Fluid](https://github.com/sebastienros/fluid) - Fluid 是一个基于 Liquid 模板语言的开源 .NET 模板引擎。
* [SmartFormat](https://github.com/axuno/SmartFormat) - 用 C# 编写的轻量级文本模板库，可以直接替代 string.Format
* [Handlebars.Net](https://github.com/Handlebars-Net/Handlebars.Net) - 真正的 .NET Handlebars 引擎

## 测试

* [ArchUnitNET](https://github.com/TNG/ArchUnitNET) - 用于使用流畅的 API 检查 C# 代码架构的简单库。
* [AutoFixture](https://github.com/AutoFixture/AutoFixture) - AutoFixture 是一个 .NET 开源框架，旨在最大限度地减少单元测试的“安排”阶段
* [BDTest](https://github.com/thomhurst/BDTest/wiki) - 行为驱动的测试和报告框架！
* [Bogus](https://github.com/bchavez/Bogus) - 一个简单而理智的 C# 假数据生成器。基于并移植自著名的 faker.js。
* [ExpressionToCode](https://github.com/EamonNerbonne/ExpressionToCode) - 在包含失败消息中的表达式表达式和子表达式值的断言中使用纯 C# 语法。
* [FakeItEasy](https://github.com/FakeItEasy/FakeItEasy) - .NET 的简单模拟库 https://fakeiteasy.github.io
* [Fluent Assertions](https://github.com/fluentassertions/fluentassertions) - 一组 .NET 扩展方法，允许您更自然地指定 TDD 或 BDD 式测试的预期结果 **[可用源]** **[OSS 免费]**
* [FsCheck](https://github.com/fscheck/FsCheck) - .NET 的随机测试。
* [Machine.Specifications](https://github.com/machine/machine.specifications) - Machine.Specifications (MSpec) 是一个上下文/规范框架，可以消除语言噪音并简化测试。
* [Moq](https://github.com/devlooped/moq) - 最流行、最友好的 .NET 模拟框架
* [NBomber](https://github.com/PragmaticFlow/NBomber) - 适用于拉动和推送场景的非常简单的负载测试框架。它 100% 用 F# 编写，面向 .NET Core 和完整的 .NET Framework。
* [NCrunch](https://www.ncrunch.net/) - Visual Studio 的自动化连续和并发测试工具。 **[$]**
* [NFluent](http://www.n-fluent.net) - NFluent 是一个断言库，旨在让您的 .NET TDD 体验更加流畅。
* [NSubstitute](https://nsubstitute.github.io/) - .NET 模拟框架的友好替代品
* [NUnit](https://github.com/nunit/nunit) - 适用于所有 .NET 语言的单元测试框架
* [Testcontainers](https://github.com/testcontainers/testcontainers-dotnet) - 一个库，支持使用所有兼容 .NET Standard 版本的一次性 Docker 容器实例进行测试。
* [SecTester](https://github.com/NeuraLegion/sectester-net) - SecTester 是一款新工具，可将 [Bright](https://brightsec.com/) 企业级扫描引擎直接集成到您的集成或 e2e 测试中。 **[专有]** **[免费]**
* [Shouldly](https://github.com/shouldly/shouldly) - Shouldly 是一个断言框架，它的重点是在断言失败时提供重要的错误消息，同时又简单又简洁。
* [Snapshooter](https://github.com/SwissLife-OSS/snapshooter) - .NET Core 和 .NET Framework 的快照测试工具
* [Stryker.NET](https://github.com/stryker-mutator/stryker-net) - .NET Core 项目的突变测试
* [xUnit.net](https://github.com/xunit/xunit) - 适用于 .NET Framework 的免费、开源、以社区为中心的单元测试工具。
* [Canopy](https://github.com/lefthandedgoat/canopy) - Canopy 是一个免费、开源的 F# Web 自动化和测试框架
* [Expecto](https://github.com/haf/expecto) - 一个流畅的 F# 测试框架，以测试为值。单元测试、基于属性的测试、性能测试和压力测试。
* [ReportPortal](https://reportportal.io) - 人工智能驱动的测试自动化仪表板。获取、汇总和分析测试报告以确定发布运行状况。
* [Compare-Net-Objects](https://github.com/GregFinzer/Compare-Net-Objects) - 使用反射对任意两个 .NET 对象执行深度比较。显示两个对象之间的差异。
* [Verify](https://github.com/VerifyTests/Verify) - 验证工具可以简单地批准复杂的模型和文档。
* [CsCheck](https://github.com/AnthonyLloyd/CsCheck) - C# 的随机测试库。包括并发、因果分析、回归和性能测试。
* [NotoriousTest](https://github.com/Notorious-Coding/Notorious-Test) - 轻量级 .NET 框架，通过编排可重用的基础设施和环境以及测试之间的自动重置，使集成测试完全隔离。 TestContainers 和 SQL Server 内置支持。基于XUnit。
## 工具

* [Downloader](https://github.com/bezzad/Downloader) - 快速可靠的多部分下载器，具有适用于 .NET 应用程序的异步进度事件。
* [Fiddler](https://www.telerik.com/fiddler) - 适用于任何浏览器、系统或平台的免费 Web 调试代理 **[专有]** **[$]** **[提供免费试用]**
* [Open Live Writer](https://github.com/OpenLiveWriter/OpenLiveWriter) - 与 WordPress、Blogger 等集成的博客作家。等人。 Open Live Writer 让您可以轻松地编写、预览和发布到博客。
* [ShareX](https://github.com/ShareX/ShareX) - ShareX 是一个免费的开源程序，可让您捕获或记录屏幕的任何区域，并只需按一下键即可共享它。它还允许将图像、文本或其他类型的文件上传到 80 多个受支持的目的地，您可以从中选择。
* [Opserver](https://github.com/Opserver/Opserver) - Stack Exchange的监控系统
* [CatLight](https://catlight.io) - 为 TFS/Jenkins/Travis/Appveyor 构建状态通知。基于 .NET Core 和 Electron 的跨平台桌面应用程序。 **[提供免费版本][专有]**
* [Mockaco](https://github.com/natenho/Mockaco/) - API 模拟服务器具有快速设置，可用于模拟 HTTP 响应，利用 ASP.NET Core 功能、内置假数据生成和由 Roslyn 脚本 API 提供支持的 C# 脚本引擎。
* [Papercut](https://github.com/ChangemakerStudios/Papercut-SMTP) - Papercut 是一个开源（基于 .NET）测试电子邮件查看器，它通过内置 SMTP 服务器在本地运行，旨在接收和通知测试电子邮件消息。
* [Fake JSON Server](https://github.com/ttu/dotnet-fake-json-server) - 用于原型设计或作为 CRUD 后端的假 REST API。无需定义类型，使用动态类型。数据存储到单个 JSON 文件中。具有身份验证、WebSocket 通知、异步长时间运行操作、错误/延迟随机生成以及实验性 GraphQL 支持。
* [NETworkManager](https://github.com/BornToBeRoot/NETworkManager) - 用于管理网络和解决网络问题的强大工具！
* [YARP](https://github.com/microsoft/reverse-proxy) - YARP 是一个反向代理工具包，用于使用 ASP.NET 和 .NET 的基础结构在 .NET 中构建快速代理服务器。
* [JSON Formatter and Validator](https://elmah.io/tools/json-formatter/) - 一个极快的 JSON 格式化程序和验证程序，不会与服务器共享 JSON。
* [CSharpier](https://github.com/belav/csharpier) - 一个基于 [Prettier](https://github.com/prettier/prettier) 打印过程的 C# 代码格式化程序。
* [UnitsNet](https://github.com/angularsen/UnitsNet) - 让使用测量单位的生活变得更加美好。
* [Another Redis Desktop Manager](https://github.com/qishibo/AnotherRedisDesktopManager) - 更快、更好、更稳定的redis桌面管理器[GUI客户端]，兼容Linux、Windows、Mac。更重要的是，加载大量密钥时它不会崩溃。
* [OctaneEngine](https://github.com/gregyjames/OctaneDownloader) - 高性能多部分下载器，具有暂停/恢复支持、异步进度和限制等许多功能。
* [FastCloner](https://github.com/lofcz/FastCloner) - 适用于 .NET 8+ 的快速深度克隆库。零配置，开箱即用。
* [STranslate](https://github.com/ZGGSONG/STranslate) - STranslate 是一款使用 WPF 开发的即用型翻译 ocr 工具。
* [BouncyHSM](https://github.com/harrison314/BouncyHsm) - HSM 和智能卡模拟器的软件模拟器，具有 HTML UI、REST API 和 PKCS#11 接口。

## 交易

* [Lean](https://github.com/QuantConnect/Lean) - Lean Engine 是一款开源、完全托管的 C# 算法交易引擎，专为桌面和云使用而构建。 https://www.quantconnect.com/lean/
* [StockSharp](https://github.com/StockSharp/StockSharp) - 交易和算法交易开源平台（股票市场、外汇、比特币和期权）。 https://stocksharp.com

## 用户界面自动化

* [Atata](https://github.com/atata-framework/atata) - 基于 Selenium WebDriver 的自动化 Web 测试全功能框架。
* [Managed Windows API](http://mwinapi.sourceforge.net/) - 内省和自动化第三方 Windows / VC++ 应用程序，而无需其源代码。
* [FlaUI](https://github.com/FlaUI/FlaUI) - FlaUI 是一个 .NET 库，有助于 Windows 应用程序（Win32、WinForms、WPF、Store Apps 等）的自动化 UI 测试。
* [PuppeteerSharp](https://github.com/hardkoded/puppeteer-sharp) - Puppeteer Sharp 是官方 Node.JS Puppeteer API 的 .NET 端口。
* [PuppeteerSharp.Contrib](https://github.com/hlaueriksson/puppeteer-sharp-contrib) - 对 Puppeteer Sharp 的贡献，提供了一种编写可读且健壮的浏览器测试的便捷方法。

## Visual Studio 插件

* [EFCore.Visualizer](https://marketplace.visualstudio.com/items?itemName=GiorgiDalakishvili.EFCoreVisualizer) - 直接在 Visual Studio 中查看 Entity Framework Core 查询计划。
* [VsVIM](https://github.com/VsVim/VsVim) - Visual Studio 中的 VIM
* [Resharper](https://www.jetbrains.com/resharper/) - Visual Studio 开发人员生产力工具 **[$]**
* [Productivity Power Tools](https://marketplace.visualstudio.com/items?itemName=VisualStudioPlatformTeam.ProductivityPowerTools) - Visual Studio Professional（及更高版本）的一组扩展，可提高开发人员的工作效率。
* [Tabs Studio](https://tabsstudio.com/) - Visual Studio 选项卡管理器具有多个选项卡行、选项卡着色和选项卡分组。 **[$]**
* [VSColorOutput](https://marketplace.visualstudio.com/items?itemName=MikeWard-AnnArbor.VSColorOutput) - 构建、查找和调试输出窗口的颜色突出显示。可以添加自定义匹配图案和颜色。
* [Roslynator](https://github.com/JosefPihrt/Roslynator) - 由 Roslyn 提供支持的 500 多个 C# 分析器、重构和修复程序的集合
* [SonarSource.sonarlint-visualstudio](https://github.com/SonarSource/sonarlint-visualstudio) - SonarLint 是一款免费、开源的 Visual Studio 2017、2019 和 2022 扩展，可向开发人员提供有关 C#、VB.NET、C/C++、TypeScript 和 JavaScript 中的新错误和质量问题的即时反馈。

## 网络浏览器

* [CefSharp](https://github.com/cefsharp/CefSharp/) - 由 Chromium 提供支持的 HTML5、CSS3 和 JS Web 浏览器，适用于 WinForms 和 WPF
* [SharpBrowser](https://github.com/sharpbrowser/SharpBrowser) - 使用 C# 和 CefSharp 构建的全功能 .NET Web 浏览器

## 网络框架

* [ASP.NET [Core]](https://dotnet.microsoft.com/apps/aspnet) - ASP.NET 是一个免费的 Web 框架，用于构建出色的网站和应用程序
* [Coalesce](https://github.com/IntelliTect/Coalesce/) - Coalesce 是一个用于快速开发 ASP.NET Core Web 应用程序的框架。
* [CodeBehind Framework](https://github.com/elanatframework/Code_behind) - ASP.NET Core 下的现代且强大的后端框架。
* [Suave.IO](https://suave.io/) - 当您提前完成项目后，当您看到用 F# 编写的漂亮代码时，框架/库/Web 服务器会让您喜极而泣。
* [DotVVM](https://github.com/riganti/dotvvm) - MVVM 框架，适合不喜欢编写 JavaScript 的人，支持 OWIN 和 ASP.NET Core，以及 Visual Studio 2015 和 2017 的免费扩展。
* [Giraffe](https://github.com/giraffe-fsharp/Giraffe) - 用于构建丰富 Web 应用程序的功能性 (F#) ASP.NET Core 微框架

## 网络服务器

* [EmbedIO](https://github.com/unosquare/embedio) - 基于 Mono 和跨平台构建的 Web 服务器
* [GenHTTP](https://github.com/Kaliumhexacyanoferrat/GenHTTP) - 用于快速创建 REST API 的轻量级嵌入式 Web 服务器
* [SimpleW](https://stratdev3.github.io/SimpleW) - .NET Core 中的 Web 服务器库。非常简单、极快的内置组件（API REST、JWT、Websockets、自序列化、Opentelemetry）。

## WebSocket

* [SignalR](https://github.com/SignalR/SignalR) - 面向 ASP.NET 开发人员的库，使向应用程序添加实时 Web 功能变得异常简单
* [SuperSocket](https://github.com/kerryjiang/SuperSocket) - SuperSocket是一个轻量级可扩展的socket应用框架
* [Websocket-Sharp](https://github.com/sta/websocket-sharp) - WebSocket 协议客户端和服务器的 C# 实现
* [Crossertech](https://crosser.io/) - 提供了一组很棒的工具，供您在 Microsoft.NET 平台等上构建实时应用程序。 **[$]**
* [Websocket.Client](https://github.com/Marfusios/websocket-client) - 本机 C# 类 ClientWebSocket 的多平台包装器，具有内置的重新连接和错误处理功能。

## 视窗服务

* [Servy](https://github.com/aelassas/servy) - 该工具可将任何应用程序转换为本机 Windows 服务，具有强大的配置和管理选项（NSSM 和 WinSW 的现代替代品）。

## WPF

* [DeftSharp.Windows.Input](https://github.com/Empiree/DeftSharp.Windows.Input) - 监听全局键盘/鼠标事件。使用简单。适用于 Windows UI 应用程序（WPF、MAUI、Avalonia）
* [Data Grid Extensions](https://github.com/tom-englert/DataGridExtensions) - WPF DataGrid 控件的模块化扩展，例如筛选、附加列事件、扩展的星形列行为等等...
* [Extended WPF Toolkit™](https://github.com/xceedsoftware/wpftoolkit) - 用于创建 WPF 应用程序的丰富控件、组件和实用程序集合
* [WPF](https://github.com/dotnet/wpf) - WPF 是一个用于构建 Windows 桌面应用程序的 .NET Core UI 框架。

## 解析器库

* [Silverfly](https://github.com/furesoft/Silverfly) - 普拉特解析器库。
* [Pidgin](https://github.com/benjamin-hodgson/Pidgin) - 一个轻量级、快速且灵活的 C# 解析库，由 Stack Overflow 开发
* [Superpower](https://github.com/datalust/superpower) - 具有高质量错误报告的 C# 解析器构建工具包
* [CSLY](https://github.com/b3b00/CSLY) - 一个轻型嵌入式 C# 词法分析器/解析器生成器。
* [Parakeet](https://github.com/ara3d/parakeet) - 具有 C# 运算符重载的递归下降解析库。
  
## 源发生器

* [CodegenCS](https://github.com/Drizin/CodegenCS) - 代码生成工具包，其中模板是使用纯 C# 编写的。命令行工具、MSBuild 任务、Visual Studio 扩展和 Roslyn 源生成器。
* [M31.FluentAPI](https://github.com/m31coding/M31.FluentAPI) - 轻松为您的 C# 类生成流畅的 API。
* [Supernova.Enum.Generators](https://github.com/EngRajabi/Enum.Source.Generator) - 用于从枚举类型创建枚举类的 C# 源生成器。使用这个包，您可以非常非常快地处理枚举，而无需使用反射。
* [Vogan](https://github.com/SteveDunn/Vogen) - 带有分析器的值对象生成器。
* [Dunet](https://github.com/domn1995/dunet) - C# 中可区分联合的简单源生成器。
* [SyncMethodGenerator](https://github.com/zompinc/sync-method-generator) - 从异步方法生成同步方法以避免代码重复。


# 其他列表

* [List of Automated Testing Tools and Frameworks for .NET](https://github.com/dariusz-wozniak/List-of-Testing-Tools-and-Frameworks-for-.NET) - .NET 自动化测试 (TDD/BDD/ATDD/SBE) 工具和框架列表
* [.NET-libraries-that-make-your-life-easier](https://github.com/tallesl/net-libraries-that-make-your-life-easier) - 让您的生活更轻松的开源 .NET 库
* [awesome-LINQ](https://github.com/aloisdg/awesome-linq) - 精彩的 LINQ 库、工具等的精选集合。
* [awesome-analyzers](https://github.com/Cybermaxs/awesome-analyzers) - .NET 编译器平台（“Roslyn”）诊断分析器和代码修复的精选列表。
* [Awesome .NET Core](https://github.com/thangchung/awesome-dotnet-core) - 一系列出色的 .NET 核心库、工具、框架和软件
* [ASP.NET Core Library and Framework Support](https://github.com/jpsingleton/ANCLAFS) - ASP.NET Core 和 .NET Core 目前支持哪些 .NET 库和框架的列表。
* [Awesome .NET Performance](https://github.com/adamsitnik/awesome-dot-net-performance) - 精彩的 .NET 性能书籍、课程、培训、会议演讲、博客和最鼓舞人心的开源贡献者的精选列表。
* [awesome-ddd](https://github.com/heynickc/awesome-ddd) - 领域驱动设计 (DDD)、命令查询职责分离 (CQRS)、事件溯源和事件风暴资源的精选列表
* [Awesome Unity](https://github.com/RyanNielson/awesome-unity) - 由社区驱动的高质量 Unity 资产、项目和资源的分类集合。
* [Awesome Xamarin](https://github.com/XamSome/awesome-xamarin) - 适用于 Xamarin 移动项目的有趣库/工具的集合。
* [Awesome Roslyn](https://github.com/ironcev/awesome-roslyn) - 精彩的 Roslyn 书籍、教程、开源项目、分析器、代码修复和重构的精选列表。
* [.NET Open Source Developer Projects](https://github.com/Microsoft/dotnet/blob/master/dotnet-developer-projects.md) - 此社区维护的列表展示了对开发过程的任何方面都有用的 .NET 开源项目。
* [Awesome Microservices .NET Core](https://github.com/mjebrahimi/Awesome-Microservices-NetCore) - .NET Core 中微服务的精彩培训系列、文章、视频、书籍、课程、示例项目和工具的集合。
* [dotnet-console-games](https://github.com/dotnet/dotnet-console-games) - 在 .NET 控制台应用程序中实现的游戏示例。
* [extra-awesome-dotnet](https://github.com/ara3d/extra-awesome-dotnet) - 很棒的 .NET 存储库的排序列表，包含星星、问题和分支的数量！

# 资源

* [Discover .NET](https://discoverdot.net) - 很棒的 .NET 开源和社区资源。
* [NuGet Trends](https://nugettrends.com) - 查看 NuGet 包的采用情况以及 NuGet 上的趋势。
* [Weekly C# Digest](https://csharpdigest.net/) - 每周电子邮件通讯，其中包含来自 .NET 社区的手动精选的前 5 个链接。
* [ASP.NET Core Developer Roadmap](https://roadmap.sh/aspnet-core) - 成为 ASP.NET 开发人员的完整指南。
