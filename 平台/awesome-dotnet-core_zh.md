# 很棒的 .NET Core [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

受到 [awesome](https://github.com/sindresorhus/awesome)、[awesome-dotnet](https://github.com/quozd/awesome-dotnet)、[awesome-nodejs](https://github.com/sindresorhus/awesome-nodejs) 的启发， [frontend-dev-bookmarks](https://github.com/dypsilon/frontend-dev-bookmarks)。

随时欢迎您的贡献！请先查看[贡献指南](https://github.com/thangchung/awesome-dotnet-core/blob/master/contributing.md)页面。我们也接受专有和商业软件。

感谢所有[贡献者](https://github.com/thangchung/awesome-dotnet-core/graphs/contributors)，你们太棒了，没有你们就不可能！目标是建立一个分类的、由社区驱动的知名资源集合。

查看我的[博客](https://dev.to/thangchung) 或在[Twitter](https://twitter.com/thangchung) 上打个招呼！

## 内容

* [General](#general)
* [框架、库和工具](#frameworks-libraries-and-tools)
  * [API](#api)
  * [应用框架](#application-frameworks)
  * [申请模板](#application-templates)
  * [认证与授权](#authentication-and-authorization)
  * [Blockchain](#blockchain)
  * [Bot](#bot)
  * [构建自动化](#build-automation)
  * [捆绑和缩小](#bundling-and-minification)
  * [Caching](#caching)
  * [CMS](#cms)
  * [代码分析和指标](#code-analysis-and-metrics)
  * [Compression](#compression)
  * [编译器、转译器和语言](#compilers-transpilers-and-languages)
  * [Cryptography](#cryptography)
  * [Database](#database)
  * [数据库驱动程序](#database-drivers)
  * [数据库工具和实用程序](#database-tools-and-utilities)
  * [日期和时间](#date-and-time)
  * [分布式计算](#distributed-computing)
  * [电子商务和支付](#e-commerce-and-payments)
  * [Exceptions](#exceptions)
  * [函数式编程](#functional-programming)
  * [Graphics](#graphics)
  * [GUI](#gui)
  * [IDE](#ide)
  * [Internationalization](#internationalization)
  * [IOC](#ioc)
  * [Logging](#logging)
  * [机器学习和数据科学](#machine-learning-and-data-science)
  * [Mail](#mail)
  * [Mathematics](#mathematics)
  * [Media](#media)
  * [Networking](#networking)
  * [Misc](#misc)
  * [Office](#office)
  * [ORM](#orm)
  * [Profiling](#profiling)
  * [队列和消息传递](#queue-and-messaging)
  * [查询生成器](#query-builders)
  * [调度程序和作业](#scheduler-and-job)
  * [SDKs](#sdks)
  * [Security](#security)
  * [Searching](#searching)
  * [Serialization](#serialization)
  * [模板引擎](#template-engine)
  * [Testing](#testing)
  * [Tools](#tools)
  * [网络框架](#web-framework)
  * [网络套接字](#web-socket)
  * [视窗服务](#windows-service)
  * [Workflow](#workflow)
* [Roadmaps](#roadmaps)
* [入门套件](#starter-kits)
* [示例项目](#sample-projects)
* [Articles](#articles)
* [Books](#books)
* [Videos](#videos)
* [Podcasts](#podcasts)
* [Community](#community)

## 一般

* [ASP.NET Core Documentation](https://docs.asp.net/en/latest/) - 官方 ASP.NET Core 文档站点。
* [.NET Core Documentation](https://docs.microsoft.com/en-us/dotnet/articles/welcome) - .NET Core、C#、F# 和 Visual Basic 的技术文档主页，包括基本概念、入门说明、教程和示例。
* [.NET Core SDK](https://www.microsoft.com/net/core) - .NET Core SDK 是由 Microsoft 和 [GitHub](https://github.com/dotnet/core) 上的 .NET 社区维护的通用开发平台。
* [.NET Platform Standard](https://github.com/dotnet/corefx/blob/1719a3fe2a5c81b67a4909787da4a02fb0d0d419/Documentation/architecture/net-platform-standard.md) - .NET旧版本和新版本的区别。
* [Introducing .NET Standard 2.0](https://blogs.msdn.microsoft.com/dotnet/2016/09/26/introducing-net-standard) - 对 .NET Standard 2.0 将要发生的事情的描述以及当前 .NET Standard 中某些缺失部分的路线图。
* [Clean Code .NET/.NET Core](https://github.com/thangchung/clean-code-dotnet) - 适用于 .NET / .NET Core 的干净代码概念。

## 框架、库和工具

### 应用程序编程接口

* [autorest](https://github.com/Azure/autorest) - Swagger (OpenAPI) 规范代码生成器，具有 C# 和 Razor 模板。支持 C#、Java、Node.js、TypeScript、Python 和 Ruby。 `4.5.x 或更高版本`
* [aspnet-api-versioning](https://github.com/Microsoft/aspnet-api-versioning) - 一组库，将服务 API 版本控制添加到 ASP.NET Web API、带有 ASP.NET Web API 的 OData 和 ASP.NET Core。
* [AspNetCoreRateLimit](https://github.com/stefanprodan/AspNetCoreRateLimit) - ASP.NET Core 速率限制中间件。
* [CondenserDotNet](https://github.com/Drawaes/CondenserDotNet) - 使用 Kestrel 和 Consul 的 API Condenser / 反向代理，包括轻量级 consul 库。
* [Flurl](https://github.com/tmenier/Flurl) - 适用于 .NET 的流畅 URL 构建器和可测试 HTTP [https://flurl.dev](https://flurl.dev)。
* 图形语言
  * [Dapper.GraphQL](https://github.com/landmarkhw/Dapper.GraphQL) - 一个旨在集成 Dapper 和 graphql-dotnet 项目的库，以易用性为中心，以性能为首要考虑。
  * [graphql-aspnetcore](https://github.com/JuergenGutsch/graphql-aspnetcore) - ASP.NET Core MiddleWare 创建 GraphQL 端点。
  * [graphql-convention](https://github.com/graphql-dotnet/conventions) - 该库是顶部的补充层，允许您使用现有属性获取器和方法作为字段解析器，自动将 .NET 类包装到 GraphQL 模式定义中
  * [graphiql-dotnet](https://github.com/JosephWoodward/graphiql-dotnet) - 适用于 ASP.NET Core 的 GraphiQL 中间件。
  * [graphql-dotnetcore](https://github.com/mkmarek/graphql-dotnetcore) - 基于 [https://github.com/graphql/graphql-js](https://github.com/graphql/graphql-js) 的 .NET Core 的 GraphQL。
  * [graphql-dotnet](https://github.com/graphql-dotnet/graphql-dotnet) - 适用于 .NET 的 GraphQL。
  * [graphql-dotnet-server](https://github.com/graphql-dotnet/server) - GraphQL for .NET - 订阅传输 WebSocket。
  * [Hot Chocolate](https://github.com/ChilliCream/hotchocolate) - 适用于 .Net Core 和 .NET Framework 的 GraphQL 服务器。
  * [FSharp.Data.GraphQL](https://github.com/fsprojects/FSharp.Data.GraphQL) - Facebook GraphQL 查询语言的 FSharp 实现 [https://fsprojects.github.io/FSharp.Data.GraphQL](https://fsprojects.github.io/FSharp.Data.GraphQL)。
  * [parser](https://github.com/graphql-dotnet/parser) - .NET 中 GraphQL 的词法分析器和解析器。
  * [tanka-graphql](https://github.com/pekkah/tanka-graphql) - GraphQL 执行和服务器库支持 SignalR、Apollo、模式操作以及 Apollo 和 graphql-js 中熟悉的其他功能
* [halcyon](https://github.com/visualeyes/halcyon) - ASP.NET 的 HAL 实现。
* [JSON API .NET Core](https://github.com/Research-Institute/json-api-dotnet-core) - 用于构建 json:api 兼容 API 的框架，其目标是消除 RESTful 样板文件。
* [LightNode](https://github.com/neuecc/LightNode) - 基于 OWIN [http://neuecc.github.io/LightNode](http://neuecc.github.io/LightNode) 构建的 Micro RPC/REST 框架。
* [NetCoreStack.Proxy](https://github.com/NetCoreStack/Proxy) - 适用于 .NET Standard 2.0 的类型安全分布式 REST 库 (NetCoreStack Flying Proxy)
* [NSwag](https://github.com/RSuter/NSwag) - 适用于 .NET、Web API 和 TypeScript 的 Swagger/OpenAPI 工具链。 [http://NSwag.org](http://NSwag.org)。
* [OData](https://github.com/OData/WebApi/tree/feature/netcore) - 开放数据协议 (OData) 支持创建基于 HTTP 的数据服务，允许使用统一资源标识符 (URI) 标识并在抽象数据模型中定义的资源，并由 Web 客户端使用简单的 HTTP 消息进行发布和编辑。
* [OpenAPI Generator](https://github.com/OpenAPITools/openapi-generator) - OpenAPI 生成器允许根据 OpenAPI 规范（v2、v3）自动生成 API 客户端库（例如 C#、TypeScript 等）、服务器存根（ASP.NET Core、NancyFx 等）、文档和配置。
* [refit](https://github.com/paulcbetts/refit) - 适用于 Xamarin 和 .NET 的自动类型安全 REST 库。
* [RestClient.Net](https://github.com/MelbourneDeveloper/RestClient.Net) - 适用于所有 C# 平台的跨平台 REST 客户端
* [RestEase](https://github.com/canton7/RestEase) - 易于使用的类型安全 REST API 客户端库，简单且可定制。
* [RestLess](https://github.com/letsar/RestLess) - 适用于 .Net Standard 的自动类型安全无反射 REST API 客户端库。
* [Restier](https://github.com/OData/RESTier) - RESTier 是一个 RESTful API 开发框架，用于在 .NET 平台上构建基于 OData V4 的标准化 RESTful 服务。
* [Restsharp](https://github.com/restsharp/RestSharp) - 适用于 .NET 的简单 REST 和 HTTP API 客户端
* [Swashbuckle](https://github.com/domaindrivendev/Swashbuckle.AspNetCore) - 无缝地为 WebApi 项目增添魅力。
  * [MicroElements.Swashbuckle.FluentValidation](https://github.com/micro-elements/MicroElements.Swashbuckle.FluentValidation) - 向 swagger 添加 FluentValidation 规则。
  * [Swashbuckle.AspNetCore.Filters](https://github.com/mattfrear/Swashbuckle.AspNetCore.Filters) - Swashbuckle.AspNetCore 的一堆有用的过滤器。
* [WebAnchor](https://github.com/mattiasnordqvist/Web-Anchor) - Web Anchor 提供类型安全、可测试且灵活、运行时生成的对 Web 资源的访问。
* [WebAPIContrib for ASP.NET CORE](https://github.com/WebApiContrib/WebAPIContrib.Core) - ASP.NET Core 的社区贡献。

### 应用框架
* [ASP.NET Boilerplate](https://github.com/aspnetboilerplate/aspnetboilerplate) - ASP.NET Boilerplate 是一个通用应用程序框架，专为新的现代 Web 应用程序而设计。它使用已经熟悉的工具并围绕它们实施最佳实践，为您提供可靠的开发体验。
* [Abp vNext](https://github.com/abpframework/abp) - Abp vNext 是下一代开源 [ASP.NET Boilerplate](https://github.com/aspnetboilerplate/aspnetboilerplate) 框架。它是创建现代 Web 应用程序的完整架构和强大的基础设施！
遵循最佳实践和约定，为您提供可靠的开发体验。
* [AsyncEx](https://github.com/StephenCleary/AsyncEx) - 用于异步/等待的辅助库。
* [Aeron.NET](https://github.com/AdaptiveConsulting/Aeron.NET) - 高效可靠的 UDP 单播、UDP 多播和 IPC 消息传输 - Aeron 的 .NET 端口。
* [akka.net](https://github.com/akkadotnet/akka.net) - 用于在 .NET 和 Mono 上构建高度并发、分布式和容错的事件驱动应用程序的工具包和运行时。
* [Aggregates.NET](https://github.com/volak/Aggregates.NET) - Aggregates.NET 是一个帮助开发人员将优秀的 NServiceBus 和 EventStore 库集成在一起的框架。
* [ASP.NET MVC](https://github.com/dotnet/aspnetcore/tree/master/src/Mvc) - 模型视图控制器框架，用于构建具有清晰的关注点分离的动态网站，包括合并的 MVC、Web API 和带有 Razor 的网页。
* [Butterfly Server .NET](https://github.com/firesharkstudios/butterfly-server-dotnet) - 允许以最小的努力构建实时网络应用程序和本机应用程序。定义可在连接的客户端之间自动同步数据集的 Web API 和订阅 API。
* [CAP](https://github.com/dotnetcore/CAP) - 具有本地持久消息功能的 EventBus，用于 SOA 或微服务架构中的系统集成。
* [Carter](https://github.com/CarterCommunity/Carter) - Carter 是一个允许 Nancy 式路由与 ASP.Net Core 一起使用的库。
* [Chromely](https://github.com/mattkol/Chromely) - Electron.NET 的轻量级替代方案，Electron for .NET/.NET Core。
* [Cinchoo ETL](https://github.com/Cinchoo/ChoETL) - .NET 的 ETL 框架（CSV、Flat、Xml、JSON、键值格式文件的解析器/编写器）。
* [CQRSlite](https://github.com/gautema/CQRSlite) - 用于帮助用 C# 编写 CQRS 和事件采购应用程序的轻量级框架。
* [dataaccess_aspnetcore](https://github.com/digipolisantwerp/dataaccess_aspnetcore) - DataAccess Toolbox 包含使用工作单元和存储库模式在 ASP.NET Core 和 Entity Framework Core 1.0 中进行数据访问的基类。
* [DNTFrameworkCore](https://github.com/rabbal/DNTFrameworkCore) - 用于构建基于 ASP.NET Core 的高质量 Web 应用程序的轻量级可扩展基础架构。
* [DotNetCorePlugins](https://github.com/natemcmaster/DotNetCorePlugins) - 用于将程序集作为插件加载的 .NET Core 库。
* [DotnetSpider](https://github.com/dotnetcore/DotnetSpider) - DotnetSpider，一个类似于 WebMagic 和 Scrapy 的 .NET Standard 网络爬虫库。它是一个轻量级、高效、快速的.NET高级网络爬行和抓取框架。
* [DotNetty](https://github.com/Azure/DotNetty) - Netty的端口，事件驱动的异步网络应用框架。
* [dotvvm](https://github.com/riganti/dotvvm) - 用于 Web 应用程序的开源 MVVM 框架。
* [ElectronNET](https://github.com/ElectronNET/Electron.NET) - 使用 ASP.NET NET Core 构建跨平台桌面应用程序。
* [EmbedIO](https://github.com/unosquare/embedio) - 适用于 .NET Framework 和 .NET Core 的微型、跨平台、基于模块的 Web 服务器。
* [Ether.Network](https://github.com/aloisdg/Ether.Network) - Ether.Network 是一个开源网络库，允许开发人员通过 TCP/IP 协议创建简单、快速且可扩展的套接字服务器或客户端应用程序。
* [EventFlow](https://github.com/eventflow/EventFlow) - Async/await 第一个适用于.NET 的 CQRS+ES 和 DDD 框架。
* [ExcelDataReader](https://github.com/ExcelDataReader/ExcelDataReader) - 用 C# 编写的轻量级快速库，用于读取 Microsoft Excel 文件。
* [ExtCore](https://github.com/ExtCore) - 免费、开源和跨平台框​​架，用于创建基于 ASP.NET Core 1.0 的模块化和可扩展的 Web 应用程序。
* [Finbuckle.MultiTenant](https://github.com/Finbuckle/Finbuckle.MultiTenant) - Finbuckle.MultiTenant 是一个 .NET 标准库，用于为 ASP.NET 2.0+ 设计的多租户支持。它提供租户解析、每租户应用程序配置和每租户数据隔离的功能。
* [fission](https://github.com/fission/fission) - Kubernetes 的快速无服务器功能。
* [grpc](https://github.com/grpc/grpc/tree/master/src/csharp) - 远程过程调用 (RPC) 为构建分布式应用程序和服务提供了有用的抽象。此存储库中的库提供了 gRPC 协议的具体实现，基于 HTTP/2 分层。这些库支持使用受支持语言的任意组合在客户端和服务器之间进行通信。
* [Halibut](https://github.com/OctopusDeploy/Halibut) - 使用基于 SSL 的 JSON-RPC 的 .NET 安全通信堆栈。
* [MagicOnion](https://github.com/neuecc/MagicOnion) - 基于 gRPC 的 HTTP/2 RPC 流框架，适用于 .NET、.NET Core 和 Unity。
* [MassTransit](https://github.com/MassTransit/MassTransit) - .NET 分布式应用程序框架。
* [microdot](https://github.com/gigya/microdot) - 开源 .NET 微服务框架。
* [MoreLINQ](https://github.com/morelinq/MoreLINQ) - LINQ to Objects 的扩展。
* [Nancy](https://github.com/NancyFx/Nancy) - 用于在 .NET 和 Mono 上构建基于 HTTP 的服务的轻量级、简单的框架。
* [opencvsharp](https://github.com/shimat/opencvsharp) - OpenCV 的 .NET Framework 包装器。
* [orleans](https://github.com/dotnet/orleans) - 该框架提供了一种直接方法来构建分布式大规模计算应用程序，无需学习和应用复杂的并发或其他扩展模式。
* [Prism](https://github.com/PrismLibrary/Prism) - Prism 是一个框架，用于在 WPF、Windows 10 UWP 和 Xamarin Forms 中构建松散耦合、可维护和可测试的 XAML 应用程序。
* [protoactor-dotnet](https://github.com/AsynkronIT/protoactor-dotnet) - 适用于 Golang 和 C# 的超快速分布式 actor [http://proto.actor](http://proto.actor)。
* [resin](https://github.com/kreeben/resin) - 具有 HTTP API 和可插拔读/写管道的 16 位宽向量空间搜索引擎。
* [RService.io](https://github.com/Stoom/RService.IO) - ASP.Net Core RESTful 微服务框架，注重速度和易用性。
* [ServiceStack](https://github.com/ServiceStack/ServiceStack) - 为所有人提供经过深思熟虑的架构、极快的速度、令人愉悦的 Web 服务 [https://servicestack.net](https://servicestack.net)。
* [Steeltoe OSS](https://github.com/SteelToeOSS) - 用于常见微服务模式的.NET 工具包。
* [Strathweb.TypedRouting.AspNetCore](https://github.com/filipw/Strathweb.TypedRouting.AspNetCore) - 在 ASP.NET Core MVC 项目中启用强类型路由的库。
* [surging](https://github.com/dotnetcore/surging) - Surging是一个微服务引擎，提供轻量级、高性能、模块化的RPC请求管道。服务引擎支持http、TCP、WS、Mqtt、UDP、DNS协议。它使用ZooKeeper和Consul作为注册中心，哈希算法、随机、轮询、压力最小优先级作为负载均衡算法，内置服务治理来保证可靠的RPC通信。
* [Xer.Cqrs](https://github.com/jeyjeyemem/Xer.Cqrs) - 一个简单的库，用于创建基于 CQRS 模式的应用程序，支持属性路由和托管处理程序。使用 C# 开发，面向 .NET Standard 1.0。
* [X.PagedList](https://github.com/dncuug/X.PagedList) - 用于轻松地对 ASP.NET/ASP.NET Core 中的任何 IEnumerable/IQueryable 进行分页的库。

### 申请模板
* [.NET Boxed](https://github.com/Dotnet-Boxed/Templates) - 包含电池的项目模板，提供了启动所需的最少量代码。包括 ASP.NET Core API 和 GraphQL 模板。
* [aspnet-core-react-template](https://github.com/bradymholt/aspnet-core-react-template) - ASP.NET Core 2.0 / React SPA 模板应用程序。
* [AspNetCoreSpa](https://github.com/asadsahi/AspNetCoreSpa) - Asp.Net Core 2+ 和 Angular 6 SPA 以及 Angular CLI 全功能应用程序。
* [ASP.NET-MVC-Template](https://github.com/NikolayIT/ASP.NET-MVC-Template) - 适用于 ASP.NET MVC 5 和 ASP.NET Core 的现成模板，包含存储库、服务、模型映射以及 DI 和 StyleCop 警告修复。
* [AddFeatureFolders](https://github.com/OdeToCode/AddFeatureFolders) - 在 ASP.NET Core 中启用 MVC 控制器和视图的功能文件夹。
* [Angular Visual Studio Webpack Starter](https://github.com/damienbod/AngularWebpackVisualStudio) - 适用于 Webpack、Visual Studio、ASP.NET Core 和 Angular 的模板。应用程序的客户端和服务器端都在一个 ASP.NET Core 项目中实现，这使得部署更加容易。
* [CleanArchitecture](https://github.com/ardalis/CleanArchitecture) - 使用 ASP.NET Core 构建干净架构的起点。清洁架构只是松散耦合、依赖倒置架构的一系列名称中的最新一个。您还会发现它被命名为六边形、端口和适配器或洋葱架构。
* [CleanArchitecture (SPA)](https://github.com/JasonGT/CleanArchitecture) - 遵循清洁架构原则，使用 Angular 8 和 ASP.NET Core 3 创建单页应用程序 (SPA) 的解决方案模板
* [DNTFrameworkCoreTemplate](https://github.com/rabbal/DNTFrameworkCoreTemplate) - 基于 [DNTFrameworkCore](https://github.com/rabbal/DNTFrameworkCore) 的样板项目模板
* [dotnet new caju](https://github.com/ivanpaulovich/dotnet-new-caju) - dotnet 新模板具有出色的架构风格！提高基于六角形、简洁或事件源架构样式设计分层应用程序的生产力。它支持多种数据访问框架（MongoDB、EntityFramework、Dapper 或 Kafka）并且完全可测试。
* [EISK](https://github.com/EISK/eisk.webapi) - 为开发人员提供简单的用例资源，以利用[架构最佳实践](https://docs.microsoft.com/en-us/dotnet/standard/modern-web-apps-azure-architecture/common-web-application-architectures)在.NET Core之上构建可扩展的应用程序（DDD、洋葱架构等）
* [JavaScriptServices](https://github.com/aspnet/JavaScriptServices) - Microsoft ASP.NET Core JavaScript 服务。
* [kendo-ui-core](https://github.com/telerik/kendo-ui-core) - 一个 HTML5、基于 jQuery 的小部件库，用于构建现代 Web 应用程序。 [http://www.telerik.com/kendo-ui](http://www.telerik.com/kendo-ui)。
* [QuickApp](https://github.com/emonney/QuickApp) - ASP.NET Core / Angular4启动项目模板，具有完整的登录、用户和角色管理。
* [Serenity](https://github.com/volkanceylan/Serenity) - Serenity 是一个 ASP.NET MVC / TypeScript 应用程序平台，旨在通过基于服务的架构简化和缩短以数据为中心的业务应用程序的开发。
* [Toucan](https://github.com/mrellipse/toucan) - 用于构建单页应用程序的样板。 Server 是围绕 SOLID 原则设计的多项目 .Net Core 解决方案。客户端是 TypeScript 2、Vuejs 2、Vuex 2。

### 认证与授权
* [AspNet.Security.OpenIdConnect.Server](https://github.com/aspnet-contrib/AspNet.Security.OpenIdConnect.Server) - 适用于 OWIN/Katana 和 ASP.NET Core 的 OpenID Connect/OAuth2 服务器框架。
* [Auth0](https://github.com/auth0/auth0.net) - 用于现代身份的托管企业级平台。
* [Casbin.NET](https://github.com/casbin-net/Casbin.NET) - C# 中支持 ACL、RBAC、ABAC 等访问控制模型的授权库
* [Identity](https://github.com/aspnet/Identity) - ASP.NET Core Identity 是用于构建 ASP.NET Core Web 应用程序的会员系统，包括会员资格、登录和用户数据。
* [IdentityServer](https://github.com/IdentityServer/IdentityServer4) - 用于 ASP.NET Core 1.0 和 2.0 的 IdentityServer
  * [IdentityServer4.EntityFramework](https://github.com/IdentityServer/IdentityServer4.EntityFramework) - EntityFramework 持久层
  * [IdentityServer4.MongoDB](https://github.com/diogodamiani/IdentityServer4.MongoDB) - MongoDB 持久层
  * [IdentityServer4.EntityFrameworkCore](https://github.com/2020IP/TwentyTwenty.IdentityServer4.EntityFrameworkCore) - Entity Framework Core 持久层
  * [IdentityServer4.Templates](https://github.com/IdentityServer/IdentityServer4.Templates) - IdentityServer4 的 dotnet cli 模板。
* [Okta](https://github.com/okta/okta-aspnet) - 用于现代身份的托管企业级平台。
* [openiddict](https://github.com/openiddict/openiddict-core) - 适用于 ASP.NET Core 的易于使用的 OpenID Connect 服务器。
  * [oidc-debugger](https://github.com/nbarbettini/oidc-debugger) - OAuth 2.0 和 OpenID Connect 调试工具。
* [stormpath-sdk](https://github.com/stormpath/stormpath-sdk-dotnet) - 使用 Stormpath 和 ASP.NET Core 构建[简单、安全的 Web 应用程序](https://github.com/stormpath/stormpath-aspnetcore)。
* [stormpath-sdk](https://github.com/stormpath/stormpath-sdk-dotnet) - 使用 Stormpath 和 ASP.NET Core 构建[简单、安全的 Web 应用程序](https://github.com/stormpath/stormpath-aspnetcore)。（已弃用：加入 OKTA 后，自 2017 年 3 月起将不再更新）
* [stuntman](https://github.com/ritterim/stuntman) - 用于在开发过程中利用 ASP.NET Identity 模拟用户的库。

### 区块链
* [BTCPayServer](https://github.com/btcpayserver/btcpayserver) - 与 Bitpay API 兼容的跨平台、自托管服务器。
* [Meadow](https://github.com/MeadowSuite/Meadow) - 一个集成的以太坊实现和工具套件，专注于 Solidity 测试和开发。
* [NBitcoin](https://github.com/MetacoSA/NBitcoin) - 适用于 .NET 框架的综合比特币库。
* [NBlockchain](https://github.com/danielgerlag/NBlockchain) - 用于构建支持区块链的应用程序的.NET标准库
* [NBXplorer](https://github.com/dgarage/NBXplorer) - 比特币和山寨币轻量级区块浏览器。
* [NEO](https://github.com/neo-project/neo) - 智能经济开放网络。
* [Nethereum](https://github.com/Nethereum) - 将以太坊的热爱带入 .NET。
* [Nethermind](https://github.com/NethermindEth/nethermind) - .NET Core 以太坊客户端
* [StratisBitcoinFullNode](https://github.com/stratisproject/StratisBitcoinFullNode) - 简单且经济实惠的端到端解决方案，用于在 .Net 框架上开发、测试和部署本机 C# 区块链应用程序。
* [Trezor.Net](https://github.com/MelbourneDeveloper/Trezor.Net) - 用于与 Trezor Hardwarewallet 对话的跨平台 C# 库
* [WalletWasabi](https://github.com/zkSNACKs/WalletWasabi) - 注重隐私、ZeroLink 兼容的比特币钱包。

### 机器人
* [BotSharp](https://github.com/SciSharp/BotSharp) - 开源 AI 聊天机器人平台构建器，采用 100% C# 语言，在 .NET Core 中运行，采用机器学习算法。
* [NadekoBot](https://github.com/Kwoth/NadekoBot) - 用 C# 编写的开源通用 Discord 聊天机器人。
* [Telegram.Bot](https://github.com/TelegramBots/Telegram.Bot) - C# Telegram Bot API 库。
* [Funogram](https://github.com/Dolfik1/Funogram) - F# Telegram Bot Api 库。

### 构建自动化
* [cake-build](https://github.com/cake-build/cake) - 跨平台构建自动化系统。
* [CatLight](https://catlight.io) - 供开发人员监视项目中的构建和任务的状态通知程序。使用 .Net Core 和 Electron 构建。
* [Colorful.Console](https://github.com/tomakita/Colorful.Console) - 设计您的 C# 控制台输出！
* [dotnet-docker](https://github.com/dotnet/dotnet-docker) - 用于使用 .NET Core 和 .NET Core 工具的基本 Docker 映像。
* [Dockerize.NET](https://github.com/brthor/Dockerize.NET) - .NET Cli 工具将 .NET Core 应用程序打包到 docker 镜像中：“dotnet dockerize”
* [FlubuCore](https://github.com/dotnetcore/FlubuCore) - 跨平台构建和部署自动化系统，用于使用 C# 代码构建项目和执行部署脚本。
* [GitInfo](https://github.com/kzu/GitInfo) - 来自 MSBuild、C# 和 VB 的 Git 和 SemVer 信息。
* [GitVersioning](https://github.com/AArnott/Nerdbank.GitVersioning) - 使用单个简单 version.txt 文件中的版本标记您的程序集和 NuGet 包，并包含非官方构建的 git 提交 ID。
* [go-dotnet](https://github.com/matiasinsaurralde/go-dotnet) - .NET Core 运行时的 Go 包装器。
* [Image2Docker](https://github.com/docker/communitytools-image2docker-win) - PowerShell 模块将现有的 Windows 应用程序工作负载移植到 Docker。
* [LocalAppVeyor](https://github.com/joaope/LocalAppVeyor) - 在本地运行您的 AppVeyor 构建。
* [msbuild](https://github.com/Microsoft/msbuild) - Microsoft Build Engine 是一个用于构建应用程序的平台。
* [Nuke](https://github.com/nuke-build/nuke) - 跨平台构建自动化系统。
* [Opserver](https://github.com/opserver/Opserver) - Stack Exchange 的监控系统。
* [vsts-agent](https://github.com/Microsoft/vsts-agent/blob/master/README.md) - Visual Studio Team Services 构建和发布代理。

### 捆绑和缩小
* [BundlerMinifier](https://github.com/madskristensen/BundlerMinifier) - Visual Studio 扩展可让您配置 JS、CSS 和 HTML 文件的捆绑和缩小。
* [JavaScriptViewEngine](https://github.com/pauldotknopf/JavaScriptViewEngine) - 用于在 JavaScript 环境中呈现标记的 ASP.NET MVC ViewEngine。非常适合 React 和 Angular 服务器端渲染。
* [Smidge](https://github.com/Shazwazza/Smidge/) - 适用于 ASP.NET Core 的轻量级运行时 CSS/JavaScript 文件缩小、组合、压缩和管理库。
* [Web Markup Minifier](https://github.com/Taritsyn/WebMarkupMin) - 包含一组标记缩小器的.NET 库。该项目的目标是通过减少 HTML、XHTML 和 XML 代码的大小来提高 Web 应用程序的性能。

### 缓存
* [CacheManager](https://github.com/MichaCo/CacheManager) - 用 C# 编写的 .NET 开源缓存抽象层。它支持各种缓存提供程序并实现许多高级功能。 [http://cachemanager.michaco.net](http://cachemanager.michaco.net)
* [EasyCaching](https://github.com/dotnetcore/EasyCaching) - 开源缓存库，包含缓存的基本用法和一些高级用法，可以帮助我们更轻松地处理缓存。
* [Faster](https://github.com/Microsoft/FASTER/tree/master/cs) - 来自 Microsoft Research 的快速键值存储。
* [Foundatio](https://github.com/exceptionless/Foundatio) - 用于构建分布式应用程序的可插入基础块。
* [Microsoft Caching](https://github.com/aspnet/Caching) - 用于内存缓存和分布式缓存的库。
* [Stack Exchange Redis](https://github.com/StackExchange/StackExchange.Redis) - 适用于 .NET 语言（C# 等）的高性能通用 Redis 客户端。

### 内容管理系统
* [Awesome-CMS-Core](https://github.com/SaiGonSoftware/Awesome-CMS-Core) - Awesome CMS Core 是一个使用 ASP.Net Core 和 ReactJS 构建的开源 CMS，考虑到模块分离问题并提供最新的技术趋势
* [Blogifier.Core](https://github.com/blogifierdotnet/Blogifier.Core) - ASP.NET 应用程序提供常见的博客功能。
* [Cofoundry](https://github.com/cofoundry-cms/cofoundry) - 开源.NET Core CMS 和模块化应用程序框架。代码优先、不显眼且可扩展。
* [CoreWiki](https://github.com/csharpfritz/CoreWiki) - 我们在实时编码流中正在处理的简单 ASP.NET Core wiki。
* [dasblog-core](https://github.com/poppastring/dasblog-core) - 使用 ASP.NET Core 重新构想的原始 DasBlog
* [Lynicon](https://github.com/jamesej/lyniconanc) - O/S ASP.Net Core/.Net Core CMS，具有付费模块：JSON 内容，适用于各种数据存储，c# 内容类型
* [Miniblog](https://github.com/madskristensen/Miniblog.Core) - ASP.NET Core 博客引擎。
* [Mixcore CMS](https://github.com/mixcore/mix.core) - 由 DotNet Core 提供支持的开源 CMS。 Mixcore CMS 是一个可扩展的开放平台，用于 Web 内容管理和数字体验。 Mixcore CMS 在网络上提供了深厚的功能和无限的灵活性。
* [NetCoreCMS](https://github.com/OnnoRokomSoftware/NetCoreCMS) - 开源 ASP.NET Core 2.0 CMS。目前支持MySQL，并计划实现MSSQL、SQLite和PostgreSQL。它也是一个模块化的 CMS，支持主题、皮肤、自定义布局、小部件、多语言（En、BN）。
* [Orchard Core CMS](https://github.com/OrchardCMS/OrchardCore) - 使用 ASP.NET Core 在模块化和可扩展的应用程序框架之上构建的开源内容管理系统。
* [Piranha CMS](https://github.com/piranhacms/piranha.core) - 适用于 ASP.NET Core 和 Entity Framework Core 的轻量级且不显眼的开源 CMS。
* [Platformus](https://github.com/Platformus) - 基于 ASP.NET Core 1.0 和 ExtCore 框架的免费、开源、跨平台 CMS。
* [SimpleContent](https://github.com/joeaudette/cloudscribe.SimpleContent) - 适用于 ASP.NET Core 的简单而灵活的内容和博客引擎，可以使用或不使用数据库。
* [Squidex](https://github.com/Squidex/squidex) - Headless CMS，基于 MongoDB、CQRS 和事件源。
* [Swastika I/O Core CMS](https://github.com/Swastika-IO/Swastika-IO-Core) - 开源 ASP.NET Core 2.x CMS。目前支持MS SQL，并计划在不久的将来实现MSSQL、SQLite。它具有许多开箱即用的内置功能，如多语言支持、主题、模板......
* [Umbraco](https://github.com/umbraco/umbraco-cms) - 可扩展且友好的开源 ASP.NET Core CMS
* [Weapsy](https://github.com/Weapsy/Weapsy) - 基于DDD和CQRS的开源ASP.NET Core CMS。它开箱即用地支持 MSSQL、MySQL、SQLite 和 PostgreSQL。
* [Wyam](https://github.com/Wyamio/Wyam) - 模块化静态内容和静态站点生成器。
* [ZKEACMS](https://github.com/SeriaWei/ZKEACMS.Core) - 视觉设计，只需拖放即可构建网站。

### 代码分析和指标
* [awesome-static-analysis](https://github.com/mre/awesome-static-analysis) - 适用于各种编程语言的静态分析工具、linter 和代码质量检查器的精选列表。
* 代码分析
  * [CodeFormatter](https://github.com/dotnet/codeformatter) - 使用 Roslyn 自动重写源代码以遵循 netfx 编码风格的工具。 [Nuget 包](https://www.nuget.org/packages/Dotnet.CodeFormatter.BuildTask.Fork)
  * [DevSkim](https://github.com/Microsoft/DevSkim) - 一组提供安全“linting”功能的 IDE 插件和规则。
  * [RefactoringEssentials](https://github.com/icsharpcode/RefactoringEssentials) - Visual Studio 重构要点。
  * [roslyn-analyzers](https://github.com/dotnet/roslyn-analyzers) - .NET 编译器平台（“Roslyn”）分析器。
  * [StyleCopAnalyzers](https://github.com/DotNetAnalyzers/StyleCopAnalyzers) - StyleCop 使用 .NET 编译器平台进行规则。
* 指标
  * [AppMetrics](https://github.com/alhardy/AppMetrics) - App Metrics 是一个开源跨平台 .NET 库，用于记录和报告应用程序中的指标并报告其运行状况。
  * [Audit.NET](https://github.com/thepirat000/Audit.NET) - 用于审核 .NET 对象更改的小型框架。
  * [BenchmarkDotNet](https://github.com/dotnet/BenchmarkDotNet) - 强大的 .NET 基准测试库。
  * [coverlet](https://github.com/tonerdo/coverlet) - .NET Core 的跨平台代码覆盖库。
  * [Foundatio](https://github.com/exceptionless/Foundatio#metrics) - 内存、redis、StatsD 和 Metrics.NET 实现的通用接口。
  * [MiniCover](https://github.com/lucaslorentz/minicover) - 适用于 .NET Core 的极简代码覆盖工具。
  * [NBench](https://github.com/petabridge/NBench) - .NET 应用程序的性能基准测试和测试框架。
  * [Nexogen.Libraries.Metrics](https://github.com/nexogen-international/Nexogen.Libraries.Metrics) - 用于收集 .NET 中的应用程序指标并将其导出到 Prometheus 的库。
  * [OpenCover](https://github.com/OpenCover/opencover) - 适用于 .NET 2 及更高版本（仅限 WINDOWS 操作系统）的代码覆盖率工具，支持具有分支点和序列点的 32 和 64 个进程。
  * [PerformanceMonitor](https://github.com/dotnet-architecture/PerformanceMonitor) - .NET Core 应用程序性能监视器。
  * [prometheus-net](https://github.com/prometheus-net/prometheus-net) - [https://prometheus.io](https://prometheus.io) 的 .NET 客户端。
  * [Prometheus.Client](https://github.com/PrometheusClientNet/Prometheus.Client) - [Prometheus](https://prometheus.io) 的 .NET 客户端。
  	* [Prometheus.Client.MetricPusher](https://github.com/PrometheusClientNet/Prometheus.Client.MetricPusher) - 将指标推送到 Prometheus.Client 的 PushGateaway。
  	* [Prometheus.Client.AspNetCore](https://github.com/PrometheusClientNet/Prometheus.Client.AspNetCore) - Prometheus.Client 的中间件。
  	* [Prometheus.Client.MetricServer](https://github.com/PrometheusClientNet/Prometheus.Client.MetricServer) - Prometheus.Client 的 MetricServer。
  	* [Prometheus.Client.HttpRequestDurations](https://github.com/PrometheusClientNet/Prometheus.Client.HttpRequestDurations) - Prometheus.Client 的请求持续时间的指标记录。

### 压缩
* [lz4net](https://github.com/MiloszKrajewski/K4os.Compression.LZ4) - 适用于所有 .NET 平台的超快速压缩算法。
* [sharpcompress](https://github.com/adamhathcock/sharpcompress) - 完全托管的 C# 库可处理多种压缩类型和格式。

### 编译器、转译器和语言
* [Fable](https://github.com/fable-compiler/Fable) - F# 到 JavaScript 编译器。
* [fparsec](https://github.com/stephan-tolksdorf/fparsec) - F# 和 C# 的解析器组合库。
* [IL2C](https://github.com/kekyo/IL2C) - ECMA-335 CIL/MSIL 到 C 语言的翻译器。
* [Mond](https://github.com/Rohansi/Mond) - 一种用 C# 编写的动态类型脚本语言，带有 REPL、调试器和简单的嵌入 API。
* [peachpie](https://github.com/peachpiecompiler/peachpie) - .NET 的开源 PHP 编译器。
* [Pidgin](https://github.com/benjamin-hodgson/Pidgin) - 一个轻量级、快速且灵活的 C# 解析库，由 Stack Overflow 开发。
* [roslyn](https://github.com/dotnet/roslyn) - .NET 编译器平台（“Roslyn”）提供开源 C# 和 Visual Basic 编译器以及丰富的代码分析 API。
* [Sprache](https://github.com/sprache/Sprache) - 微型 C# Monadic 解析器框架。

### 密码学
* [BCrypt.Net](https://github.com/BcryptNet/bcrypt.net) - 对原始 bcrypt 包进行更新。
* [BCrypt.NET-Core](https://github.com/neoKushan/BCrypt.Net-Core) - BCrypt.NET 的 .NET Core 端口用于安全地存储密码。
* [BouncyCastle PCL](https://github.com/onovotny/BouncyCastle-PCL) - Bouncy Castle Crypto 包是加密算法和协议的 C# 实现。
* [multiformats](https://github.com/multiformats/cs-multihash) - 一个通用的哈希库，但是一个用于编码/解码多重哈希的库，它是一个“容器”，描述了计算摘要的哈希算法。
* [nsec](https://github.com/ektrah/nsec) - NSec 是基于 libsodium 的 .NET Core 的新加密库。
* [SecurityDriven.Inferno](github.com/sdrapkin/SecurityDriven.Inferno) - 使用.Net原语的高级加密库，已经过专业审核。

### 数据库
* [DBreeze](https://github.com/hhblaze/DBreeze) - C# .NET MONO NOSQL（嵌入键值存储）ACID 多范式数据库管理系统。
* [JsonFlatFileDataStore](https://github.com/ttu/json-flatfile-datastore) - 简单的 JSON 平面文件数据存储，支持类型化和动态数据。
* [LiteDB](https://github.com/mbdavid/LiteDB) - .NET NoSQL 文档存储在单个数据文件中 - [http://www.litedb.org](http://www.litedb.org)。
* [NoDb](https://github.com/joeaudette/NoDb) - .NET Core/ASP.NET Core 的“无数据库”文件系统存储，因为并非每个项目都需要数据库。
* [marten](https://github.com/JasperFx/marten) - Postgresql 作为 .NET 应用程序的文档数据库和事件存储 [http://jasperfx.github.io/marten](http://jasperfx.github.io/marten)。
* [StringDB](https://github.com/SirJosh3917/StringDB) - StringDB 是一个模块化的键/值对归档数据库，旨在消耗“微小”的内存并生成“微小”的数据库。
* [yessql](https://github.com/sebastienros/yessql) - 适用于任何 RDBMS 的 .NET 文档数据库。

### 数据库驱动程序
* [cassandra-csharp-driver](https://github.com/datastax/csharp-driver) - Apache Cassandra 的 DataStax C# 驱动程序。
* [confluent-kafka-dotnet](https://github.com/confluentinc/confluent-kafka-dotnet) - Confluence 的 Apache Kafka .NET 客户端。
* [couchbase-lite-net](https://github.com/couchbase/couchbase-lite-net) - 适用于 .NET 的轻量级、面向文档 (NoSQL)、可同步的数据库引擎。
* [MongoDB.Driver](https://github.com/mongodb/mongo-csharp-driver) - MongoDB 的 .NET 驱动程序。
* [MongoDB.Entities](https://github.com/dj-nitehawk/MongoDB.Entities) - MongoDB 数据访问库，具有优雅的 API、LINQ 支持和内置实体关系管理
* MySQL
  * [mysql-connector-net](https://github.com/mysql/mysql-connector-net/tree/8.0) - Connector/Net 是用于 MySQL 的完全托管的 ADO.NET 驱动程序。
  * [MySqlConnector](https://github.com/mysql-net/MySqlConnector) - 适用于 .NET 和 .NET Core 的异步 MySQL 连接器。
* 新4j
  * [neo4j-dotnet-driver](https://github.com/neo4j/neo4j-dotnet-driver) - 适用于 .NET 的 Neo4j Bolt 驱动程序。
  * [Neo4jClient](https://github.com/Readify/Neo4jClient) - Neo4j 的 .NET 客户端绑定。
* [npgsql](https://github.com/npgsql/npgsql) - PostgreSQL 的 .NET 数据提供程序。它允许任何为.NET框架开发的程序访问PostgreSQL数据库服务器。它是用 100% C# 代码实现的。 PostgreSQL 版本自 9.1 起得到正式支持，其他版本也可以工作。 [http://www.npgsql.org](http://www.npgsql.org)
* [ravendb](https://github.com/ayende/ravendb/tree/v4.0) - Linq 支持 .NET 文档数据库。
* [RethinkDb.Driver](https://github.com/bchavez/RethinkDb.Driver) - C#/.NET RethinkDB 驱动程序具有 100% ReQL API 覆盖率。
* [progaudi.tarantool](https://github.com/progaudi/progaudi.tarantool) - Tarantool NoSql 数据库的 .NET 客户端。

### 数据库工具和实用程序
* [DbUp](https://github.com/DbUp/DbUp) - .NET 库可帮助您将更改部署到 SQL Server 数据库。它跟踪已运行的 SQL 脚本，并运行使数据库保持最新状态所需的更改脚本。
* [Evolve](https://github.com/lecaillon/Evolve) - 使用纯 SQL 脚本的简单数据库迁移工具。灵感来自飞路。
* [EFCorePowerTools](https://github.com/ErikEJ/EFCorePowerTools) - Entity Framework Core Power Tools - EF Core 的逆向工程、迁移和模型可视化。
* [fluentmigrator](https://github.com/fluentmigrator/fluentmigrator) - .NET 的迁移框架与 Ruby on Rails 迁移非常相似。
* [monitor-table-change-with-sqltabledependency](https://github.com/christiandelbianco/monitor-table-change-with-sqltabledependency) - 获取有关记录表更改的 SQL Server 通知。
* [NReco.PivotData](https://www.nuget.org/packages/NReco.PivotData) - 具有 OLAP 操作和数据透视表数据模型的内存数据立方体。
* [roundhouse](https://github.com/chucknorris/roundhouse) - 使用 sql 文件和基于源代码控制的版本控制的 .NET 数据库迁移实用程序。
* [SapphireDb](https://github.com/SapphireDb/SapphireDb) - SapphireDb 的服务器实现，这是一个通过实时数据同步轻松开发应用程序的框架，也是用于 asp.net core 和 ef core 的 firebase 实时数据库/firestore 的自托管替代方案。查看文档了解更多详细信息：[文档](https://sapphire-db.com)
* [SharpRepository](https://github.com/SharpRepository/SharpRepository) - SharpRepository 是一个用 C# 编写的通用存储库，支持各种关系、文档和对象数据库，包括 Entity Framework、RavenDB、MongoDb 和 Db4o。 SharpRepository 还包括 Xml 和 InMemory 存储库实现。
* [TrackableEntities.Core](https://github.com/TrackableEntities/TrackableEntities.Core) - 使用 .NET Core 跨服务边界进行变更跟踪。
* [Mongo.Migration](https://github.com/SRoddis/Mongo.Migration) - Mongo.Migration 专为 [MongoDB C# 驱动程序]( https://github.com/mongodb/mongo-csharp-driver) 设计，可轻松即时迁移文档。架构迁移不再需要停机。只需编写小而简单的迁移即可。 [链接]( https://github.com/SRoddis/Mongo.Migration)
* [EntityFrameworkCore.DataEncryption](https://github.com/Eastrall/EntityFrameworkCore.DataEncryption) - Microsoft.EntityFrameworkCore 的插件，用于使用内置或自定义加密提供程序添加对加密字段的支持。

### 日期和时间
* [Exceptionless.DateTimeExtensions](https://github.com/exceptionless/Exceptionless.DateTimeExtensions) - DateTimeRange、Business Day 和各种 DateTime、DateTimeOffset、TimeSpan 扩展方法。
* [FluentDateTime](https://github.com/FluentDateTime/FluentDateTime) - 允许您编写更清晰的 DateTime 表达式和操作。部分受到 Ruby DateTime Extensions 的启发。
* [nodatime](https://github.com/nodatime/nodatime) - 更好的 .NET 日期和时间 API [http://nodatime.org](http://nodatime.org)。

### 分布式计算
* [AspNetCore.Diagnostics.HealthChecks](https://github.com/xabaril/AspNetCore.Diagnostics.HealthChecks) - ASP.NET Core 诊断包的企业健康检查
  - [BeatPulse](https://github.com/Xabaril/BeatPulse) - 启用负载平衡器来监视已部署的 Web 应用程序的状态
* [Foundatio](https://github.com/exceptionless/Foundatio) - 用于构建分布式应用程序的可插入基础块
* [jasper](https://github.com/JasperFx/jasper) - .NET 的下一代应用程序开发框架
* [Rafty](https://github.com/ThreeMammals/Rafty) - .NET Core 中的 RAFT 共识
* [Obvs](https://github.com/christopherread/Obvs) - 一个可观察的微服务总线 .NET 库，将底层传输封装在基于简单 Rx 的接口中
* [Ocelot](https://github.com/ThreeMammals/Ocelot) - 使用.NET Core创建的API网关
* [OpenTracing](https://github.com/opentracing/opentracing-csharp) - 供应商中立的 API 和分布式跟踪工具
* [Polly](https://github.com/App-vNext/Polly) - .NET 3.5 / 4.0 / 4.5 / PCL 库，允许开发人员以流畅的方式表达瞬态异常和故障处理策略，例如重试、永远重试、等待重试或断路器
* [ProxyKit](https://github.com/damianh/ProxyKit) - 在 ASP.NET Core 上创建代码优先 HTTP 反向代理的工具包

### 电子商务和支付
* [nopCommerce](https://github.com/nopSolutions/nopCommerce) - 免费的开源电子商务购物车（ASP.NET MVC / ASP.NET Core MVC）拥有庞大的社区和充满新功能、主题和插件的市场。
* [GrandNode](https://github.com/grandnode/grandnode) - 基于 ASP.NET Core 2.1 和 MongoDB 的多平台、免费、开源电子商务购物车，源自 [nopCommerce](https://github.com/nopSolutions/nopCommerce)。
* [PayPal](https://github.com/paypal/PayPal-NET-SDK) - 用于 PayPal RESTful API 的 .NET SDK。
* [SimplCommerce](https://github.com/simplcommerce/SimplCommerce) - 基于.NET Core 构建的超级简单的电子商务系统。
* [Stripe](https://github.com/ServiceStack/Stripe) - stripe.com REST API 的类型化 .NET 客户端。


### 例外情况
* [Demystifier](https://github.com/benaadams/Ben.Demystifier) - 对堆栈跟踪的高性能理解（使错误日志更加高效）。
* [Exceptionless](https://github.com/exceptionless/Exceptionless.Net) - 无异常的 .NET 客户端
* [GlobalExceptionHandlerDotNet](https://github.com/JosephWoodward/GlobalExceptionHandlerDotNet) - GlobalExceptionHandlerDotNet 允许您将异常处理配置为 ASP.NET Core 应用程序管道的约定，而不是在每个控制器操作中显式处理它们。
* [Sentry](https://github.com/getsentry/sentry-dotnet) - .NET SDK for Sentry，一种开源错误跟踪工具，可帮助开发人员实时监控和修复崩溃。

### 函数式编程
* [CSharpFunctionalExtensions](https://github.com/vkhorikov/CSharpFunctionalExtensions) - C# 的功能扩展。
* [DynamicData](https://github.com/RolandPheasant/DynamicData) - 基于 Rx.NET 的反应式集合。
* [echo-process](https://github.com/louthy/echo-process) - 用于 C# 的 Actor 库，带有支持 Redis 持久性以及 JS 集成的附加模块。
* [FsCheck](https://github.com/fscheck/FsCheck) - .NET 的随机测试。
* [Giraffe](https://github.com/dustinmoris/Giraffe) - 面向 F# 开发人员的本机功能 ASP.NET Core Web 框架。
* [language-ext](https://github.com/louthy/language-ext) - C# 函数式语言扩展和“类 Erlang”并发系统。
* [LaYumba.Functional](https://github.com/la-yumba/functional-csharp-code) - 用于使用 C# 进行功能编程的实用程序库。
* [NetMQ.ReactiveExtensions](https://github.com/NetMQ/NetMQ.ReactiveExtensions) - 使用反应式扩展 (RX) 轻松地在网络上的任何位置发送消息。传输协议是ZeroMQ。
* [Optional](https://github.com/nlkl/Optional) - C# 的强大选项类型。
* [reactive-streams-dotnet](https://github.com/reactive-streams/reactive-streams-dotnet) - [Reactive Streams](http://www.reactive-streams.org/) 适用于 .NET。
* [ReactiveUI](https://github.com/reactiveui/ReactiveUI) - MVVM 框架与 .NET 的响应式扩展集成，可创建在任何移动或桌面平台上运行的优雅、可测试的用户界面。
* [Rx.NET](https://github.com/Reactive-Extensions/Rx.NET) - .NET 的 [Reactive Extensions](http://reactivex.io)。
* [Qactive](https://github.com/RxDave/Qactive) - 反应式可查询可观察框架。 `4.x.x 或以上`
* [sodium](https://github.com/SodiumFRP/sodium/tree/master/) - 函数反应式编程 (FRP) 库。 `4.x.x 或以上`

### 图形
* [GLFWDotNet](https://github.com/smack0007/GLFWDotNet) - GLFW 的 .NET 绑定。
* [ImageProcessor](https://github.com/JimBobSquarePants/ImageProcessor) - System.Drawing 的流畅包装，用于处理图像文件 [http://imageprocessor.org](http://imageprocessor.org)。 `4.5.x 或更高版本`
* [ImageSharp](https://github.com/SixLabors/ImageSharp) - 用 C# 编写的用于处理图像文件的跨平台库。
* [LibVLCSharp](https://github.com/videolan/libvlcsharp)：libvlc 的 .NET/Mono 绑定，libvlc 是为 VideoLAN 制作的 VLC 应用程序提供支持的多媒体框架。
* [Magick.NET](https://github.com/dlemstra/Magick.NET) - ImageMagick 的 .NET 库。
* [MagicScaler](https://github.com/saucecontrol/PhotoSauce) - MagicScaler 适用于 .NET 的高性能、高质量图像处理管道
* [QRCoder](https://github.com/codebude/QRCoder) - 纯C#开源QR码实现。
* [SharpBgfx](https://github.com/MikePopoloski/SharpBgfx) - bgfx 图形库的 C# 绑定。
* [Structure.Sketching](https://github.com/JaCraig/Structure.Sketching) - 用于支持 .NET Core 的 .NET 应用程序的图像处理库。
* [veldrid](https://github.com/mellinoe/veldrid) - 适用于 .NET 的低级硬件加速 3D 图形库。
* [ZXing.Net](https://github.com/micjahn/ZXing.Net/) - 原始基于java的条码读取器和生成器库zxing的.Net端口。

### 图形用户界面
* [AdonisUI](https://github.com/benruehl/adonis-ui) - 适用于 WPF 应用程序的轻量级 UI 工具包，提供经典但增强的 Windows 视觉效果。
* [Avalonia](https://github.com/AvaloniaUI/Avalonia) - 多平台 .NET UI 框架（以前称为 Perspex）。
* [AvaloniaEdit](https://github.com/AvaloniaUI/AvaloniaEdit/) - 基于 Avalonia 的文本编辑器组件源自 [AvalonEdit](https://github.com/icsharpcode/AvalonEdit)
[HandyControls](https://github.com/ghost1372/HandyControls) - 包含一些简单且常用的 WPF 控件。
* [Lara](https://github.com/integrativesoft/lara) - Lara Web Engine 是一个用 C# 开发 Web 用户界面的库
* [ShellProgressBar](https://github.com/Mpdreamz/shellprogressbar) - 在控制台程序中创建进度条的库
* [Qml.Net](https://github.com/pauldotknopf/Qml.Net) - Mono/.NET/.NET Core 的跨平台 Qml/.NET 集成。
* [WinApi](https://github.com/prasannavl/WinApi) - 一个简单、直接、超薄的 CLR 库，用于高性能 Win32 本机互操作，具有自动化、窗口、DirectX、OpenGL 和 Skia 帮助程序。

### 集成开发环境
* [Mono](https://github.com/mono/monodevelop) - MonoDevelop 使开发人员能够在 Linux、Windows 和 Mac OS X 上快速编写桌面和 Web 应用程序。它还使开发人员可以轻松地将使用 Visual Studio 创建的 .NET 应用程序移植到 Linux 和 Mac OS X，从而为所有平台维护单一代码库。
* [rider](https://www.jetbrains.com/rider/) - 基于 IntelliJ 平台和 ReSharper 的跨平台 C# IDE。
* [Omnisharp](http://www.omnisharp.net/) - 一系列开源项目，每个项目都有一个目标：在您选择的编辑器中提供出色的 .NET 体验。
* [SharpDevelop](https://github.com/icsharpcode/SharpDevelop) - SharpDevelop 是一款免费的集成开发环境 (IDE)，适用于 Microsoft .NET 平台上的 C#、VB.NET、Boo、IronPython、IronRuby 和 F# 项目。它（几乎）完全用 C# 编写，并具有您在 IDE 中所期望的功能以及更多功能。
* [Visual Studio Code](https://github.com/Microsoft/vscode) - 新型工具将代码编辑器的简单性与开发人员核心编辑-构建-调试周期所需的功能相结合。代码提供全面的编辑和调试支持、可扩展性模型以及与现有工具的轻量级集成。
* [Visual Studio Community](https://www.visualstudio.com/en-us/products/visual-studio-community-vs.aspx) - 适用于个人开发者、开源项目、学术研究、教育和小型专业团队的免费编辑器。

### 国际化
* [Localization](https://github.com/aspnet/Localization) - ASP.NET Core 应用程序的本地化抽象和实现。
* [NetCoreStack.Localization](https://github.com/NetCoreStack/Localization) - 具有实体框架和内存缓存的 .NET Core 数据库资源本地化
* [Westwind.Globalization](https://github.com/RickStrahl/Westwind.Globalization) - .NET 应用程序的数据库驱动资源本地化。

### 国际奥委会
* [AutoDI](https://github.com/Keboo/AutoDI) - 使用 IL 编织的超快速编译时依赖项注入。
* [Autofac](https://github.com/autofac/Autofac) - 令人上瘾的 .NET IoC 容器。
* [Castle.Windsor](https://github.com/castleproject/Windsor) Castle Windsor 是可用于 .NET 的同类最佳、成熟的控制反转容器。
* [DryIoc](https://github.com/dadhi/DryIoc) - 适用于 .NET 的快速、小型、功能齐全的 IoC 容器。
* [Grace](https://github.com/ipjohnson/Grace) - Grace 是一个功能丰富的依赖注入容器，其设计时考虑到了易用性和性能。
* [Inyector](https://github.com/davidrevoledo/Inyector) - AspNetCore 的依赖注入自动化
* [Lamar](https://github.com/JasperFx/lamar) - Roslyn Chicanery 控制工具和杂项的快速反转。
* [LightInject](https://github.com/seesharper/LightInject) - 超轻量级 IoC 容器。
* [SimpleInjector](https://github.com/simpleinjector/SimpleInjector) - 简单、灵活、快速的依赖注入库，促进最佳实践，引导开发人员走向成功的深渊。
* [Stashbox](https://github.com/z4kn4fein/stashbox) - 用于基于 .NET 的解决方案的轻量级、可移植的依赖项注入框架。
* [Unity](https://github.com/unitycontainer/unity) - 一个轻量级的、可扩展的依赖注入容器。

### 记录
* [common-logging](https://github.com/net-commons/common-logging) - .NET 的可移植日志记录抽象。
* [dnxcore-logging-logstash](https://github.com/jvandevelde/dnxcore-logging-logstash) - 适用于具有 UDP 和 Redis 传输的 .NET Core 应用程序的 Logstash 日志记录扩展。
* [ElmahCore](https://github.com/ElmahCore/ElmahCore) - 错误日志库，包括错误过滤和从网页查看错误日志的功能等功能。
* [Exceptionless](https://github.com/exceptionless/Exceptionless.Net) - 无异常的 .NET 客户端
* [Foundatio](https://github.com/exceptionless/Foundatio#logging) - 流畅的日志记录 API，可用于在整个应用程序中记录消息。
* [Karambolo.Extensions.Logging.File](https://github.com/adams85/filelogger) - 一个轻量级库，为内置 .NET Core 日志记录框架 (Microsoft.Extensions.Logging) 实现文件日志记录。
* [LibLog](https://github.com/damianh/LibLog) - 单个文件供您复制/粘贴或通过 nuget 安装到您的库/框架/应用程序中以提供日志记录抽象。
* [log4net](https://github.com/apache/logging-log4net) - log4net 是优秀的 Apache log4j™ 框架到 Microsoft® .NE​​T 运行时的端口。
* [NLog](https://github.com/NLog/NLog) - 高级 .NET、Silverlight 和 Xamarin 日志记录，支持结构化和非结构化日志记录。
  * [NLog for ASP.NET and ASP.NET Core](https://github.com/NLog/NLog.Web) - ASP.NET 和 ASP.NET Core 1-3 的 NLog 集成
  * [NLog.Extensions.Logging](https://github.com/NLog/NLog.Extensions.Logging) - 用于 .NET 标准库和 .NET Core 应用程序的 Microsoft.Extensions.Logging 的 NLog 提供程序
  * [NLog.Windows.Forms](https://github.com/NLog/NLog.Windows.Forms) - 特定于 Windows.Forms 的 NLog 目标
  * [NLog.MailKit](https://github.com/NLog/NLog.MailKit) - 使用 MailKit 库的替代邮件目标
* [Q42.Logging.ApplicationInsights](https://github.com/Q42/Q42.Logging.ApplicationInsights) - 用于在 ASP.NET Core 日志记录中构建的日志附加程序，用于将所有日志发送到 Application Insights。
* [serilog](https://github.com/serilog/serilog) - 具有完全结构化事件的简单 .NET 日志记录。
  * [serilog-aspnetcore](https://github.com/serilog/serilog-aspnetcore) - ASP.NET Core 2+ 的 Serilog 集成。
  * [Serilog.Exceptions](https://github.com/RehanSaeed/Serilog.Exceptions) - Serilog.Exceptions 是 [Serilog](https://serilog.net/) 的附加组件，用于记录未在 Exception.ToString() 中输出的异常详细信息和自定义属性。
  * [Serilog.Settings.Configuration](https://github.com/serilog/serilog-settings-configuration) - 从 Microsoft.Extensions.Configuration 读取的 Serilog 配置提供程序。
* [SEQ](https://getseq.net) - Seq 通过 HTTP 收集数据，而您的应用程序则使用适合您平台的最佳可用结构化日志记录 API。

### 机器学习和数据科学
* [Accord](https://github.com/accord-net/framework) - .NET 的机器学习、计算机视觉、统计和通用科学计算。
* [Catalyst](https://github.com/curiosity-ai/catalyst) 受 spaCy 启发的跨平台自然语言处理 (NLP) 库，具有预训练模型、对训练单词和文档嵌入的开箱即用支持以及灵活的实体识别模型。 [SciSharp 堆栈](https://sciSharp.github.io/SciSharp/) 的一部分
* [ML.NET](https://github.com/dotnet/machinelearning) - 跨平台开源机器学习框架，使 .NET 开发人员可以使用机器学习 [http://dot.net/ml](http://dot.net/ml)。
* [Spreads](https://github.com/Spreads/Spreads/) - 用于数据流实时和探索性分析的系列和面板。
* [TensorFlowSharp](https://github.com/migueldeicaza/TensorFlowSharp) - 适用于 .NET 语言的 TensorFlow API。
* [WaveFunctionCollapse](https://github.com/mxgmn/WaveFunctionCollapse) - 借助量子力学的思想，从单个示例生成 itmap 和tilemap。
* [SiaNet](https://github.com/SciSharp/SiaNet) - 一个C#深度学习库，人性化，支持CUDA/OpenCL，结构良好，易于扩展

### 邮件
* [FluentEmail](https://github.com/lukencode/FluentEmail) - 适用于 .NET 和 .NET Core 的多合一电子邮件发送器
* [MailBody](https://github.com/doxakis/MailBody) - 使用流畅的界面 (.NET) 创建交易电子邮件。
* [MailKit](https://github.com/jstedfast/MailKit) - 适用于 IMAP、POP3 和 SMTP 的跨平台 .NET 库。
* [MailMergeLib](https://github.com/axuno/MailMergeLib) - SMTP 邮件客户端库，为文本、内联图像和附件提供舒适的邮件合并功能，以及发送邮件消息的良好吞吐量和容错能力。
* [MimeKit](https://github.com/jstedfast/MimeKit) - 跨平台 .NET MIME 创建和解析器库，支持 S/MIME、PGP、DKIM、TNEF 和 Unix mbox 线轴。
* [netDumbster](https://github.com/cmendible/netDumbster) - 用于测试的.Net Fake SMTP 服务器。流行的阿呆的克隆。
* [Papercut](https://github.com/ChangemakerStudios/Papercut) - 简单的桌面 SMTP 服务器
* [PreMailer.Net](https://github.com/milkshakesoftware/PreMailer.Net) - C# 库可将样式表移动到内联样式属性，以实现与电子邮件客户端的最大兼容性。
* [SendGrid Client](https://github.com/0xdeafcafe/sendgrid-dotnet) - SendGrid v3 邮件端点的 C# 库。
* [SmtpServer](https://github.com/cosullivan/SmtpServer) - 用于创建您自己的 SMTP 服务器的库。
* [StrongGrid](https://github.com/Jericho/StrongGrid) - SendGrid v3 API 的客户端。不仅允许您发送电子邮件，还允许您批量导入联系人、管理列表和细分、为列表创建自定义字段等。还包括 SendGrid Webhooks 的解析器。

### 数学
* [AutoDiff](https://github.com/alexshtf/autodiff) - 一个提供快速、准确和自动微分（计算导数/梯度）数学函数的库。
* [UnitConversion](https://github.com/Stratajet/UnitConversion) - 适用于 .NET Core 和 .NET Framework 的可扩展单位转换库。
* [UnitsNet](https://github.com/angularsen/UnitsNet) - Units.NET 为您提供所有常见的测量单位以及它们之间的转换。

### 媒体
* [MetadataExtractor](https://github.com/drewnoakes/metadata-extractor-dotnet) - 使用简单易用的 API 从媒体（图像、视频、音频）中提取元数据。

### 杂项
* [AdvanceDLSupport](https://github.com/Firwood-Software/AdvanceDLSupport) - 用于改进 P/Invoke-ing 本机代码的库。与本机对象交互，就好像它们是一流对象一样。
* [AngleSharp](https://github.com/AngleSharp/AngleSharp) - 终极尖括号解析器库。它解析 HTML5、MathML、SVG 和 CSS，以构建基于官方 W3C 规范的 DOM。相当于python的beautifulsoup4。
* [AgileMapper](https://github.com/agileobjects/AgileMapper) - AgileMapper 是一个零配置、高度可配置的对象到对象映射器，具有可视的执行计划。
* [AspNetCore Extension Library](https://github.com/sgjsakura/AspNetCore) - ASP.NET Core 扩展库。
* [AutoMapper](https://github.com/AutoMapper/AutoMapper) - .NET 中基于约定的对象到对象映射器。
* [Baget](https://github.com/loic-sharma/BaGet) - 轻量级 NuGet 服务器。
* [Bleak](https://github.com/Akaion/Bleak) - Windows 本机 DLL 注入库。
* [Bullseye](https://github.com/adamralph/bullseye/) - 用于描述和运行目标及其依赖项的 .NET 包。
* [Castle.Core](https://github.com/castleproject/Core) - Castle Core，包括 Castle DynamicProxy、日志服务和 DictionaryAdapter [http://www.castleproject.org](http://www.castleproject.org)。
* [Chessie](https://github.com/fsprojects/Chessie) - 面向铁路的 .NET 编程 [http://fsprojects.github.io/Chessie](http://fsprojects.github.io/Chessie)。
* [CliWrap](https://github.com/Tyrrrz/CliWrap) - 命令行界面的包装。
* [commanddotnet](https://github.com/bilal-fazlani/commanddotnet) - 在类中对命令行应用程序界面进行建模。
* [CommonMark.NET](https://github.com/Knagis/CommonMark.NET) - CommonMark 规范在 C# 中的实现，用于将 Markdown 文档转换为 HTML。
* [ConsoleTableExt](https://github.com/minhhungit/ConsoleTableExt) - 用于为 .NET 控制台应用程序创建表的 Fluent 库。
* [CoordinateSharp](https://github.com/Tronald/CoordinateSharp) - 一个可以快速格式化和转换地理坐标并提供基于位置的太阳和月亮信息（日落、日出、月亮照明等）的库。
* [datatables](https://github.com/ALMMa/datatables.aspnet/tree/dev) - Microsoft ASP.NET 服务器端支持和 jQuery DataTables 帮助程序。
* [DinkToPdf](https://github.com/rdvojmoc/DinkToPdf) - wkhtmltopdf 库的 C# .NET Core 包装器，使用 Webkit 引擎将 HTML 页面转换为 PDF。
* [dotnet-env](https://github.com/tonerdo/dotnet-env) - 用于从 .env 文件加载环境变量的 .NET 库。
* [DotNet.Glob](https://github.com/dazinator/DotNet.Glob) - 适用于 .NET / .NETStandard 应用程序的快速通配库。优于正则表达式。
* [Dotnet outdated](https://github.com/dotnet-outdated/dotnet-outdated) - .NET Core 全局工具，用于显示和更新项目中过时的 NuGet 包
* [Dotnet Script](https://github.com/filipw/dotnet-script) - 从 .NET CLI 运行 C# 脚本。
* [Dotnet Serve](https://github.com/natemcmaster/dotnet-serve) - 适用于 .NET Core CLI 的简单命令行 HTTP 服务器。
* [Downloader](https://github.com/bezzad/Downloader) - Downloader 是一个现代、流畅、异步、可测试和可移植的 .NET 库。这是一个具有异步进度事件的多部分下载器。
* [Eighty](https://github.com/benjamin-hodgson/Eighty) - 一个简单的HTML生成库
* [Enums.NET](https://github.com/TylerBrinkley/Enums.NET) - Enums.NET 是一个高性能类型安全的 .NET 枚举实用程序库
* [FastExpressionCompiler](https://github.com/dadhi/FastExpressionCompiler) - 快速的 ExpressionTree 编译器进行委托。
* [FluentDocker](https://github.com/mariotoffia/FluentDocker) - 用于 docker、docker-compose 和 docker-machine 的命令、服务和 Fluent API，适用于 win/mac/linux 和本机 docker。
* [FluentFTP](https://github.com/robinrodricks/FluentFTP/) - FTP 和 FTPS 客户端，具有广泛的 FTP 命令、SSL/TLS 连接、散列/校验和等。
* [Fody](https://github.com/Fody/Fody) - 用于编织 .net 程序集的可扩展工具
* [HdrHistogram.NET](https://github.com/HdrHistogram/HdrHistogram.NET) - 高动态范围 (HDR) 直方图。
* [httpclient-interception](https://github.com/justeat/httpclient-interception) - 用于拦截服务器端 HTTP 依赖项的 .NET 标准库。
* [Humanizer](https://github.com/Humanizr/Humanizer) - Humanizer 满足您操作和显示字符串、枚举、日期、时间、时间跨度、数字和数量的所有 .NET 需求。
* [Humidifier](https://github.com/jakejscott/Humidifier) - 使用 C# 编写和维护 AWS Cloudformation 模板。
* [impromptu-interface](https://github.com/ekonbenefits/impromptu-interface) - 动态实现的静态接口（鸭子铸造）。将 DLR 与 Reflect.Emit 结合使用。
* [JqueryDataTablesServerSide](https://github.com/fingers10/JqueryDataTablesServerSide) - 用于 Jquery 数据表的 ASP.NET Core 服务器端处理库，具有数据库级别的多列过滤、排序和分页功能，并支持 Excel 导出和 TagHelper。
* [LibSass Host](https://github.com/Taritsyn/LibSassHost) - 围绕 [libSass](http://sass-lang.com/libsass) 库的 .NET 包装器，能够支持虚拟文件系统。
* [markdig](https://github.com/lunet-io/markdig) - 适用于 .NET 的快速、功能强大、兼容 CommonMark、可扩展的 Markdown 处理器。
* [NetCoreBeauty](https://github.com/nulastudio/NetCoreBeauty) - 简单的库，可将 .NET Core 应用程序运行时组件和依赖项移动到子目录中并使其美观。
* [NFlags](https://github.com/bartoszgolek/NFlags) - 简单的库使解析 CLI 参数变得容易。库还允许“开箱即用”打印使用帮助。
* [NReco.LambdaParser](https://github.com/nreco/lambdaparser) - 将字符串表达式（公式、方法调用、条件）解析为可编译为 lambda 并进行计算的 LINQ 表达式树。
* [NuGet Trends](https://github.com/NuGetTrends/nuget-trends) - 包含 NuGet 包下载计数统计信息的网站。
* [NYoutubeDL](https://gitlab.com/BrianAllred/NYoutubeDL) - 用于 C#/.NET 的简单 youtube-dl 库。
* [Otp.NET](https://github.com/kspearrin/Otp.NET) - 用 C# 实现 TOTP RFC 6238 和 HOTP RFC 4226。
* [pose](https://github.com/tonerdo/pose) - 用委托替换任何 .NET 方法（包括静态和非虚拟）
* [PuppeteerSharp](https://github.com/kblok/puppeteer-sharp) - Puppeteer Sharp 是官方 Node.JS Puppeteer API 的 .NET 端口。
* [readline](https://github.com/tsolarin/readline) - 适用于 .NET/.NET Core 的纯 C# GNU-Readline 类库。
* [ReflectionMagic](https://github.com/ReflectionMagic/ReflectionMagic) - 使用 C# 动态极大简化您的私有反射代码的框架
* [Relinq](https://github.com/re-motion/Relinq) - 借助 re-linq，现在创建功能齐全的 LINQ 提供程序比以往任何时候都更加容易。
* [Remote.Linq](https://github.com/6bee/Remote.Linq) - Remote Linq 是一个小型且易于使用但功能非常强大的库，用于将 LINQ 表达式树转换为强类型、可序列化的表达式树，反之亦然。
* [ReverseMarkdown](https://github.com/mysticmind/reversemarkdown-net) - Html 到 Markdown 转换器库。
* [PdfReport.Core](https://github.com/VahidN/PdfReport.Core) - PdfReport.Core 是一个代码优先的报告引擎，它构建在 iTextSharp.LGPLv2.Core 和 EPPlus.Core 库之上。
* [Scientist](https://github.com/github/Scientist.net) - .NET 库，用于仔细重构关键路径。它是 GitHub 的 Ruby Scientist 库的移植。
* [Scrutor](https://github.com/khellang/Scrutor) - Microsoft.Extensions.DependencyInjection 的程序集扫描扩展。
* [Sheller](https://github.com/twitchax/Sheller) - 一个 .NET 库，使命令的 shell 处理变得超级简单和流畅。
* [SmartFormat.NET](https://github.com/scottrippey/SmartFormat.NET) - string.Format 的可扩展替代品。
* 股票
  * [Trady](https://github.com/lppkarl/Trady) - 用于计算技术指标的便捷库，其目标是成为一个自动交易系统，提供股票数据输入、指标计算、策略构建和自动交易。
* [System.Linq.Dynamic.Core](https://github.com/StefH/System.Linq.Dynamic.Core) - System Linq Dynamic 功能的 .NET Standard (.NET Core) 版本。
* 验证
  * [FluentValidation](https://github.com/JeremySkinner/FluentValidation) - 适用于 .NET 的小型验证库，使用流畅的接口和 lambda 表达式来构建验证规则。
  * [FormHelper](https://github.com/SinanBozkus/FormHelper) - ASP.NET Core 的表单和验证助手。 Form Helper 可帮助您创建 ajax 表单和验证，而无需编写任何 JavaScript 代码。 （与 Fluent 验证兼容）。
  * [Guard](https://github.com/safakgur/guard) - 高性能、可扩展的参数验证库。
  * [Valit](https://github.com/valit-stack/Valit) - .NET Core 的极其简单的验证。您的代码中不再有 if 语句。而是编写漂亮、干净、流畅的验证器！
* [Vanara](https://github.com/dahall/Vanara) - 一组用于 Windows 的 .NET 库，通过支持包装器实现对许多本机 Windows API 的 PInvoke 调用。
* [warden-stack](https://github.com/warden-stack) - 对您的应用程序、资源和基础设施进行“健康检查”。让你的典狱长随时注意。
* [WebEssentials.AspNetCore.ServiceWorker](https://github.com/madskristensen/WebEssentials.AspNetCore.ServiceWorker) - ASP.NET Core 渐进式 Web 应用程序。
* [Xabe.FFmpeg](https://github.com/tomaszzmuda/Xabe.FFmpeg) - FFmpeg 的 .NET 标准包装器。它允许在不知道 FFmpeg 如何工作的情况下处理媒体，并且可用于将自定义参数从 C# 应用程序传递给 FFmpeg。
* [YoutubeExplode](https://github.com/Tyrrrz/YoutubeExplode) - 用于提取元数据和下载 YouTube 视频和播放列表的终极库。

### 网络
* [AspNetCore.Proxy](https://github.com/twitchax/AspNetCore.Proxy) - ASP.NET Core 代理变得简单。
* [CurlThin](https://github.com/stil/CurlThin) - 用于 C# 的轻量级 cURL 绑定库，支持通过curl_multi 接口同时进行多个传输。
* [NETStandard.HttpListener](https://github.com/StefH/NETStandard.HttpListener) - 适用于 .NET Core (NETStandard) 的 HttpListener。
* [Networker](https://github.com/MarkioE/Networker) - 一个简单易用的 .NET TCP 和 UDP 网络库，设计灵活、可扩展且快速。
* [SharpPcap](https://github.com/chmorgan/sharppcap) - 完全托管的跨平台（Windows、Mac、Linux）.NET 库，用于从实时设备和基于文件的设备捕获数据包。

### 办公室
* [EPPlus](https://github.com/EPPlusSoftware/EPPlus) - 使用 .NET 创建高级 Excel 电子表格。
* [npoi](https://github.com/tonyqus/npoi) - .NET 库，无需安装 Microsoft Office 即可读取/写入 Office 格式。没有 COM+，就没有互操作。
* [Open-XML-SDK](https://github.com/OfficeDev/Open-XML-SDK) - Open XML SDK 提供了用于处理 Office Word、Excel 和 PowerPoint 文档的工具。

### 操作系统
* [CosmosOS](https://github.com/CosmosOS/Cosmos) - Cosmos 是一个操作系统“构建工具包”。使用 C#、VB.NET 等托管语言构建您自己的操作系统！

### ORM
* [Chloe](https://github.com/shuxinqin/Chloe) - 适用于 .NET 的轻量级高性能对象/关系映射 (ORM) 库。
* [Entity Framework Core](https://github.com/aspnet/EntityFramework) - 熟悉 EF 早期版本的开发人员经验，包括 LINQ、POCO 和 Code First 支持。
  * [EFCore.BulkExtensions](https://github.com/borisdj/EFCore.BulkExtensions) - 用于插入更新删除读取 (CRUD) 操作的 EntityFrameworkCore 批量扩展
  * [EFCore.Visualizer](https://marketplace.visualstudio.com/items?itemName=GiorgiDalakishvili.EFCoreVisualizer) - 直接在 Visual Studio 中查看 Entity Framework Core 查询计划。
  * [EntityFramework-Plus](https://github.com/zzzprojects/EntityFramework-Plus) - 实体框架实用程序 |批量操作 |批量删除 |批量更新 |查询缓存 |查询过滤器 |查询未来 |查询包括 |审计。
  * [EntityFramework.Exceptions](https://github.com/Giorgi/EntityFramework.Exceptions) - 当 SQL 查询违反 SqlServer、MySql 或 PostgreSQL 中的数据库约束时，请使用 EntityFrameworkCore 的类型化异常。
  * [EntityFramework.Triggers](https://github.com/NickStrupat/EntityFramework.Triggers) - EF 的触发事件。
  * [EntityFramework.Rx](https://github.com/NickStrupat/EntityFramework.Rx) - EF 操作的反应式**热**可观察值。
  * [Npgsql.EntityFrameworkCore.PostgreSQL](https://github.com/npgsql/Npgsql.EntityFrameworkCore.PostgreSQL) - PostgreSQL 的 Entity Framework Core 提供程序。
  * [EntityFramework.PrimaryKey](https://github.com/NickStrupat/EntityFramework.PrimaryKey) - 轻松获取任何实体的主键（包括组合键）。
  * [EntityFramework.TypedOriginalValues](https://github.com/NickStrupat/EntityFramework.TypedOriginalValues) - 获取实体原始值的代理对象（对 Property("...").OriginalValue 进行类型化访问）。
  * [EntityFramework.VersionedProperties](https://github.com/NickStrupat/EntityFramework.VersionedProperties) - 自动神奇地保留指定属性更改的审核历史记录的类。
  * [EntityFrameworkCore.SqlServer.SimpleBulks](https://github.com/phongnguyend/EntityFrameworkCore.SqlServer.SimpleBulks) - 简单的库，可以帮助将内存中的大量记录同步到数据库中。支持 Lambda 表达式。
  * [LINQKit](https://github.com/scottksmith95/LINQKit) - 面向 LINQ to SQL 和实体框架高级用户的一组免费扩展。
  * [Pomelo.EntityFrameworkCore.MySql](https://github.com/PomeloFoundation/Pomelo.EntityFrameworkCore.MySql) - MySql 的 Entity Framework Core 提供程序构建在 mysql-net/MySqlConnector 之上。
  * [spectre.query](https://github.com/spectresystems/spectre.query) - Entity Framework Core 的简单查询语言。
* [Dapper](https://github.com/StackExchange/Dapper) - .NET 的简单对象映射器。
  * [Dapper-FluentMap](https://github.com/henkmollema/Dapper-FluentMap) - 提供简单的 API，以便在使用 Dapper 时流畅地将 POCO 属性映射到数据库列。
  * [Dommel](https://github.com/henkmollema/Dommel) - Dapper 的简单 CRUD 操作。
  * [MicroOrm.Dapper.Repositories](https://github.com/phnx47/MicroOrm.Dapper.Repositories) - 适合 Dapper 的 CRUD。
* [FreeSql](https://github.com/2881099/FreeSql) - dotnet 中方便的 ORM，支持 Mysql、Postgresql、SqlServer、Oracle 和 Sqlite。
* [Limebean](https://nick-lucas.github.io/LimeBean/) - 混合 ORM，设计为易于使用且不完全隐藏 SQL，同时具有您期望从 ORM 获得的所有好处。受到 RedBeanPHP 的启发。
* [LINQ to DB (linq2db)](https://linq2db.github.io/) - 最快的 LINQ 数据库访问库，在 POCO 对象和数据库之间提供简单、轻量级、快速且类型安全的层，适用于 10 多个数据库引擎，并具有完整的 SQL 支持。
* [nhibernate-core](https://github.com/nhibernate/nhibernate-core) - NHibernate 对象关系映射器。
* [NEventStore](https://github.com/NEventStore/NEventStore) - 当使用事件源作为存储机制时，持久性库用于抽象不同的存储实现。该库的开发专门针对 DDD/CQRS 应用程序。
* [NPoco](https://github.com/schotime/NPoco) - 将查询结果映射到 POCO 对象的简单 microORM。基于 Schotime 的 PetaPoco 分支的项目。
* [NReco.Data](https://github.com/nreco/data) - 独立于提供商的轻量级 DAL，用于 SQL 命令生成、CRUD 操作和简单的 POCO 映射。
* [PetaPoco](https://github.com/CollaboratingPlatypus/PetaPoco) - 一个适合 POCO 的类似 ORM 的小东西。
* [querybuilder](https://github.com/sqlkata/querybuilder) - SqlKata Query Builder 是一个用 C# 编写的功能强大的 Sql 查询生成器。
* [RepoDb](https://github.com/mikependon/RepoDb) - .NET 的混合 ORM 库。
* [ServiceStack.OrmLite](https://github.com/ServiceStack/ServiceStack.OrmLite) - 轻量、简单且快速的基于约定的 POCO ORM。
* [SqlFu](https://github.com/sapiens/SqlFu) - 快速且多功能的 Micro-ORM。
* [SmartSql](https://github.com/Ahoo-Wang/SmartSql) - SmartSql = MyBatis + Cache(内存 | Redis) + ZooKeeper + 读写分离 + 动态存储库 ....
* [SQLStreamStore](https://github.com/SQLStreamStore/SQLStreamStore) - Stream Store 库针对 .NET 的基于 SQL 的实现。

### 分析
* [Glimpse](https://github.com/Glimpse/Glimpse.Prototype) - 适用于 .NET 的轻量级、开源、实时诊断和见解分析器。 `不稳定的版本`
* [MiniProfiler](https://github.com/MiniProfiler/dotnet) - 一个简单但有效的 ASP.NET 网站迷你分析器。

### 查询生成器
* [SqlKata](https://github.com/sqlkata/querybuilder) - 优雅的 Sql 查询生成器，支持复杂查询、联接、子查询、嵌套 where 条件、供应商引擎目标等

### 队列和消息传递
* [emitter](https://emitter.io/) - 连接所有设备的免费开源实时消息服务。此发布-订阅消息传递 API 专为速度和安全性而构建。
* [EasyNetQ](https://github.com/EasyNetQ/EasyNetQ) - 易于使用的 RabbitMQ .NET API。
* [EventStore](https://github.com/EventStore/EventStore) - 开源功能数据库，具有 JavaScript 中的复杂事件处理功能。
* [Foundatio](https://github.com/exceptionless/Foundatio#queues) - 内存、redis 和 azure 实现的通用接口。
* [MediatR](https://github.com/jbogard/MediatR) - .NET 中简单、简单的中介实现。
 * [MediatR.Extensions.Microsoft.DependencyInjection](https://github.com/jbogard/MediatR.Extensions.Microsoft.DependencyInjection) - Microsoft.Extensions.DependencyInjection 的 MediatR 扩展。
* [Mediator.Net](https://github.com/mayuanyang/Mediator.Net) - .Net 的简单中介，用于发送命令、发布事件和请求响应，并支持管道。
* [MicroBus](https://github.com/Lavinski/Enexure.MicroBus) - .NET 的简单进程内中介。
* [MQTTnet](https://github.com/chkr1011/MQTTnet) - MQTTnet 是一个用于基于 MQTT 通信的高性能 .NET 库。
* [netmq](https://github.com/zeromq/netmq) - 适用于 .NET 的 ZeroMQ 100% 原生 C# 实现。
* [NServiceBus](https://github.com/particular/nservicebus) - NServiceBus 是[特定服务平台](https://preferred.net/service-platform) 的一部分，其中包含用于构建、监控和调试分布式系统的工具。
* [OpenCQRS](https://github.com/OpenCQRS/OpenCQRS) - .NET Core 库，用于与 Azure 服务总线集成的 DDD、CQRS 和事件溯源。命令和事件存储支持的数据库提供程序包括：DocumentDB、MongoDB、SQL Server、MySQL、PostgreSQL 和 SQLite。
* [rabbitmq-dotnet-client](https://github.com/rabbitmq/rabbitmq-dotnet-client) - RabbitMQ .NET 客户端 [https://www.rabbitmq.com](https://www.rabbitmq.com)。
* [RawRabbit](https://github.com/pardahlman/RawRabbit) - 用于通过 RabbitMq 进行通信的现代 .NET 框架。
* [Rebus](https://github.com/rebus-org/Rebus) - .NET 的简单而精益的服务总线实现。
* [Restbus](http://restbus.org) - RabbitMq 的消息传递库。
* [Silverback](https://github.com/BEagle1984/silverback) - 用于构建事件驱动应用程序的框架（支持 Kafka、RabbitMQ、MQTT）。
* [Tossit](https://github.com/turgayozgur/tossit) - 简单、易于使用的分布式作业/工作者逻辑库。由内置 RabbitMQ 实现处理的分布式消息。

### 报告
* [FastReport](https://github.com/FastReports/FastReport) - 适用于 .NET Core 2.x/.Net Framework 4.x 的开源报告生成器。 FastReport可用于MVC、Web API应用程序。

### 调度程序和作业
* [Chroniton.NetCore](https://github.com/leosperry/Chroniton) - 用于按计划运行任务（作业）的轻量级健壮库。
* [Coravel](https://github.com/jamesmh/coravel) - .Net Core 与 Laravel 的结合：调度、队列等。
* [FluentScheduler](https://github.com/fluentscheduler/FluentScheduler) - 具有流畅界面的自动化作业调度程序。
* [Gofer.NET](https://github.com/brthor/Gofer.NET) - 用于 .NET Core 分布式后台任务/作业的简单 C# API。受到 python 芹菜的启发。
* [HangfireIO](https://github.com/HangfireIO/Hangfire) - 在 ASP.NET 应用程序中执行即发即忘、延迟和重复任务的简单方法 [http://hangfire.io](http://hangfire.io)。
* [LiquidState](https://github.com/prasannavl/LiquidState) - 适用于 .NET 的高效异步和同步状态机。
* [NCrontab](https://github.com/atifaziz/NCrontab) - .NET 的 Crontab。
* [quartznet](https://github.com/quartznet/quartznet/) - Quartz Enterprise Scheduler .NET [http://www.quartz-scheduler.net](http://www.quartz-scheduler.net)。
* [stateless](https://github.com/dotnet-state-machine/stateless) - 用于在 C# 代码中创建状态机的简单库。

### 软件开发工具包
* [AWS SDK](https://github.com/aws/aws-sdk-net) - Amazon Web Services (AWS) .NET Core SDK 组件。每个 AWS 服务都有自己的 NuGet 包。
* [azure-event-hubs-dotnet](https://github.com/azure/azure-event-hubs-dotnet) - 适用于 Azure 事件中心的 .NET 标准客户端库。
* 区块链客户端
  * [Bittrex.Net](https://github.com/JKorf/Bittrex.Net) - Bittrex Web API 的 C# .Net 包装器，包括易于访问和使用的所有功能。
  * [Binance.Net](https://github.com/JKorf/Binance.Net) - Binance Web API 的 .Net API 包装器。
* [CakeMail.RestClient](https://github.com/Jericho/CakeMail.RestClient) - CakeMail 的 API 客户端。允许您发送交易电子邮件、批量电子邮件、管理列表和联系人等。
* [consuldotnet](https://github.com/PlayFab/consuldotnet/tree/develop) - Consul 的 .NET API。
* [csharp-nats](https://github.com/nats-io/csharp-nats) - 用于 NATS 消息系统的 C# .NET 客户端。
* [DarkSkyCore](https://github.com/amweiss/dark-sky-core) - [Dark Sky API](https://darksky.net/dev/docs) 的 .NET Standard 包装器。
* [Docker.DotNet](https://github.com/Microsoft/Docker.DotNet) - 用于 Docker API 的 .NET (C#) 客户端库。
* [firebase-admin-dotnet](https://github.com/firebase/firebase-admin-dotnet) - Firebase 管理 .NET SDK
* [google-cloud-dotnet](https://github.com/GoogleCloudPlatform/google-cloud-dotnet) - 适用于 .NET 的 Google Cloud 客户端库。
* [Manatee.Trello](https://github.com/gregsdennis/Manatee.Trello) - 用 C# 编写的 Trello RESTful API 的完全面向对象的 .Net 包装器。
* [Microphone](https://github.com/rogeralsing/Microphone) - 轻量级框架，用于在 Consul 或 ETCD 集群上使用 Web Api 或 NancyFx 运行自托管 REST 服务。
* [octokit.net](https://github.com/octokit/octokit.net) - 适用于 .NET 的 GitHub API 客户端库。
* [PreStorm](https://github.com/jshirota/PreStorm) - ArcGIS Server 的并行 REST 客户端。
* [SendGrid-csharp](https://github.com/sendgrid/sendgrid-csharp) - 用于使用完整 SendGrid API 的 C# 客户端库。
* [statsd-csharp-client](https://github.com/Pereingo/statsd-csharp-client) - .NET Standard 兼容 C# 客户端，可与 Etsy 优秀的 [statsd](https://github.com/etsy/statsd) 服务器交互。
* [tweetinvi](https://github.com/linvi/tweetinvi) - 用于访问 Twitter REST 和 STREAM API 的直观 .NET C# 库。

### 安全性
* [aspnetcore-security-headers](https://github.com/juunas11/aspnetcore-security-headers) - 用于向 ASP.NET Core 应用程序添加安全标头的中间件。
* [HtmlSanitizer](https://github.com/mganss/HtmlSanitizer) - 清理 HTML 以避免 XSS 攻击。
* [jose-jwt](https://github.com/dvsekhvalnov/jose-jwt) - 用于处理 JOSE 对象（JWT、JWA、JWS 及相关）的库。
* [Jwt.Net](https://github.com/jwt-dotnet/jwt) - Jwt.Net，.NET 的 JWT（JSON Web 令牌）实现。
* [JWT Simple Server](https://github.com/Xabaril/JWTSimpleServer) - 适用于 ASP.NET Core 的轻量级动态 jwt 服务器。
* [NWebsec](https://github.com/NWebsec/NWebsec) - ASP.NET 的安全库 [http://www.nwebsec.com](http://www.nwebsec.com)。
* [reCAPTCHA](https://github.com/PaulMiami/reCAPTCHA) - 适用于 ASP.NET Core 的 reCAPTCHA 2.0。
* [roslyn-security-guard](https://github.com/dotnet-security-guard/roslyn-security-guard) - Roslyn 分析器旨在帮助对 .NET 应用程序进行安全审核。
* [OwaspHeaders](https://github.com/GaProgMan/OwaspHeaders.Core) - .NET Core 中间件，用于注入 Owasp 推荐的 HTTP 标头以提高安全性。
* [Security](https://github.com/aspnet/Security) - 用于 Web 应用程序安全和授权的中间件。
* [SecurityHeaders](https://github.com/andrewlock/NetEscapades.AspNetCore.SecurityHeaders) - 允许向 ASP.NET Core 网站添加安全标头的小包。

### 搜寻中
* [Algolia.Search](https://github.com/algolia/algoliasearch-client-csharp) - 官方 Algolia .NET 客户端的存储库。
* [AutoComplete](https://github.com/omerfarukz/autocomplete) - 持久、简单、强大且可移植的自动完成库。
* [Elasticsearch.Net & NEST](https://github.com/elastic/elasticsearch-net) - NEST 和 Elasticsearch.NET（两个官方的 elasticsearch .NET 客户端）的存储库。
* [ElasticsearchCRUD](https://github.com/damienbod/ElasticsearchCRUD) - Elasticsearch .NET API。
* [SearchExtensions](https://github.com/ninjanye/SearchExtensions) - IQueryable 接口的高级搜索功能，例如实体框架查询。
* [SimMetrics.Net](https://github.com/StefH/SimMetrics.Net) - 相似度度量库，例如从编辑距离（Levenshtein、Gotoh、Jaro 等）到其他指标（例如 Soundex、Chapman）
* [SolrExpress](https://github.com/solr-express/solr-express) - 用于 Solr 的简单轻量级查询 .NET 库，以受控、可构建和快速失败的方式。

### 序列化
* [BinarySerializer](https://github.com/jefffhaynes/BinarySerializer) - 自定义数据包和协议格式的序列化支持位旋转。
* [bond](https://github.com/Microsoft/bond) - 用于处理模式化数据的跨平台框架。它支持跨语言反/序列化和强大的通用机制，可有效地操作数据。 Bond 在 Microsoft 的大规模服务中广泛使用。
* [Channels](https://github.com/davidfowl/Channels) - 基于推送的 .NET 流。
* [CsvHelper](https://github.com/JoshClose/CsvHelper) - 帮助读取和写入 CSV 文件的库。
* [Edi.Net](https://github.com/indice-co/EDI.Net) - EDI 串行器/解串器。支持 EDIFact、X12 和 TRADACOMS 格式。
* [ExtendedXmlSerializer](https://github.com/wojtpl2/ExtendedXmlSerializer) - 适用于 .NET 的扩展 Xml 序列化程序。
* [Jil](https://github.com/kevin-montrose/Jil) - 快速 .NET JSON (De)Serializer，构建于 Sigil 之上。
* 消息包
  * [msgpack-cli](https://github.com/msgpack/msgpack-cli) - 公共语言基础结构的 MessagePack 实现 / [msgpack.org](http://msgpack.org)。
  * [MessagePack-CSharp](https://github.com/neuecc/MessagePack-CSharp) - 适用于 C#（.NET、.NET Core、Unity、Xamarin）的极快 MessagePack 序列化器。
* [Newtonsoft.Json](https://github.com/JamesNK/Newtonsoft.Json) - 适用于 .NET 的流行高性能 JSON 框架。
* [protobuf-net](https://github.com/mgravell/protobuf-net/) - 适用于惯用的 .NET 的 Protocol Buffers 库。
* [Schema.NET](https://github.com/RehanSaeed/Schema.NET) - Schema.org 对象转换为强类型 C# POCO 类，以便在 .NET 中使用。所有类都可以序列化为 JSON/JSON-LD 和 XML，通常用于表示 html 页面的 head 部分中的结构化数据。
* [ServiceStack.Text](https://github.com/ServiceStack/ServiceStack.Text) - JSON、JSV 和 CSV 文本序列化器。
* [TinyCsvParser](https://github.com/bytefish/TinyCsvParser) - 易于使用、易于扩展的高性能库，用于使用 .NET 进行 CSV 解析。
* [Wire](https://github.com/rogeralsing/Wire) - POCO 对象的二进制序列化器。
* [YamlDotNet](https://github.com/aaubry/YamlDotNet) - .NET
* [ZeroFormatter](https://github.com/neuecc/ZeroFormatter) - 适用于 .NET 的快速二进制（反）序列化器。
* [Utf8Json](https://github.com/neuecc/Utf8Json) - 适用于 C#（NET、.NET Core、Unity、Xamarin）的绝对最快且零分配的 JSON 序列化器。
* [YAXLib](https://github.com/sinairv/YAXLib) - 适用于 .NET Framework 和 .NET Core 的 XML 序列化库。极其灵活且强大。

### 模板引擎
* [dotliquid](https://github.com/dotliquid/dotliquid) - Tobias Lütke 的 Liquid 模板语言的 .NET 端口。
* [fluid](https://github.com/sebastienros/fluid) - 尽可能接近 Liquid 模板语言的开源 .NET 模板引擎。
* [Portable.Xaml](https://github.com/cwensley/Portable.Xaml) - 用于读取/写入 xaml 文件的可移植 .NET 库。
* [Razor](https://github.com/aspnet/Razor) - MVC Web 应用程序视图页面中使用的 CSHTML 文件的解析器和代码生成器。
* [RazorLight](https://github.com/toddams/RazorLight) - 基于 Microsoft .NET Core 的 Razor 解析引擎的模板引擎。
* [Scriban](https://github.com/lunet-io/scriban) - 一种快速、强大、安全且轻量级的 .NET 文本模板语言和引擎。

### 测试
* [Atata](https://github.com/atata-framework/atata) - 基于Selenium WebDriver的Web UI测试自动化全功能框架。 [https://atata.io](https://atata.io)
* [Bogus](https://github.com/bchavez/Bogus) - 用于 C# 的简单而合理的假数据生成器。基于并移植自著名的 faker.js。
* [CoreBDD](https://github.com/stevenknox/CoreBDD) - xUnit.net 的 BDD 框架
* [FakeItEasy](https://github.com/FakeItEasy/FakeItEasy) - .NET 的简单模拟库。
* [FluentAssertions](https://github.com/fluentassertions/fluentassertions) - 一组 .NET 扩展方法，允许您更自然地指定 TDD 或 BDD 样式测试的预期结果。
* [GenFu](https://github.com/MisterJames/GenFu) - 您可以使用库来生成真实的测试数据。
* [LightBDD](https://github.com/LightBDD/LightBDD) - BDD 框架允许创建易于阅读和维护的测试。
* [mockhttp](https://github.com/richardszalay/mockhttp) - Microsoft HttpClient 库的测试层。
* [moq.netcore](https://github.com/Moq/moq4) - 最流行、最友好的 .NET 模拟框架。
* [MSpec](https://github.com/machine/machine.specifications) - 用于编写 BDD 风格测试的流行测试框架。
* [MyTested.AspNetCore.Mvc](https://github.com/ivaylokenov/MyTested.AspNetCore.Mvc) - 流畅的测试
ASP.NET Core MVC 框架。
* [Netling](https://github.com/hallatore/Netling) - 负载测试器客户端可轻松进行 Web 测试。
* [NSpec](https://github.com/nspec/NSpec) - 久经考验的 C# 测试框架，深受 Mocha 和 RSpec 的启发。
* [NSubstitute](https://github.com/nsubstitute/NSubstitute) - .NET 模拟框架的友好替代品。
* [nunit](https://github.com/nunit/dotnet-test-nunit) - .NET Core 的 NUnit 测试运行器。
* [shouldly](https://github.com/shouldly/shouldly) - 应该测试 .NET - 断言“应该”的方式！ [http://shouldly.readthedocs.org/en/latest](http://shouldly.readthedocs.org/en/latest)
* [SpecFlow](https://github.com/techtalk/SpecFlow) - 适用于 .NET 的实用 BDD 解决方案。它使用 Gherkin 规范语言并集成到 Visual Studio。
* [Storyteller](https://github.com/storyteller/Storyteller) - .NET 的可执行规范 [http://storyteller.github.io](http://storyteller.github.io)。
* [Stubbery](https://markvincze.github.io/Stubbery/) - 用于在 .NET 中创建和运行 Api 存根的简单库。
* [Testavior](https://github.com/geeklearningio/Testavior) - Testavior 是一个轻量级解决方案，可帮助您开发 ASP.NET Core 的行为测试。
* [TestStack.BDDfy](https://github.com/TestStack/TestStack.BDDfy) - 有史以来最简单的 BDD 框架！
* [xBehave.net](https://github.com/xbehave/xbehave.net) - 一个 xUnit.net 扩展，用于使用自然语言描述您的测试。 [http://xbehave.github.io](http://xbehave.github.io)
* [xUnit.net](https://github.com/xunit/xunit) - 适用于 .NET Framework 的免费、开源、以社区为中心的单元测试工具。

### 工具
* [CliFx](https://github.com/Tyrrrz/CliFx) - 用于构建命令行界面的声明性框架。
* [CommandLineUtils](https://github.com/natemcmaster/CommandLineUtils) - .NET Core 和 .NET Framework 的命令行解析和实用程序。
* [docfx](https://github.com/dotnet/docfx) - 用于为 .NET 项目构建和发布 API 文档的工具 [http://dotnet.github.io/docfx](http://dotnet.github.io/docfx)
* [dotnetfiddle](https://dotnetfiddle.net) - .NET 沙箱，供开发人员快速尝试代码并共享代码片段。
* [dotnet-tools](https://github.com/natemcmaster/dotnet-tools) - .NET Core 命令行 (dotnet CLI) 的工具扩展列表。
  * [LibMan CLI](https://github.com/aspnet/LibraryManager) - Web 应用程序的客户端内容管理器。
* [EntryPoint](https://github.com/Nick-Lucas/EntryPoint) - 适用于 .Net Core 和 .Net Framework 4.5+ 的可组合 CLI（命令行）参数解析器。
* [Fake JSON Server](https://github.com/ttu/dotnet-fake-json-server) - 用于原型设计或作为 CRUD 后端的假 REST API。无需定义类型，使用动态类型。数据存储到单个 JSON 文件中。具有身份验证、WebSocket 通知、异步长时间运行操作、错误/延迟随机生成以及实验性 GraphQL 支持。
* [gitignore.io](https://github.com/joeblau/gitignore.io) - 为您的项目创建有用的 .gitignore 文件 [https://www.gitignore.io](https://www.gitignore.io)。
* [ICanHasDotnetCore](https://github.com/OctopusDeploy/ICanHasDotnetCore) - 扫描上传的 packages.config 文件或 GitHub 存储库，并确定 nuget 包是否面向 .NET Standard。
* [json2csharp](http://json2csharp.com) - 从 JSON 生成 C# 类。
* [letsencrypt-win-simple](https://github.com/Lone-Coder/letsencrypt-win-simple) - 适用于 Windows 的简单 ACME 客户端。
* [Linq_Faster](https://github.com/jackmott/LinqFaster) - 用于数组、Span<T> 和 List<T> 的类似于 Linq 的扩展函数，速度更快且分配更少。
 
* [mRemoteNG](https://github.com/mRemoteNG/mRemoteNG) - 下一代 mRemote、开源、选项卡式、多协议、远程连接管理器
* [NJsonSchema](https://github.com/RSuter/NJsonSchema) - NJsonSchema 是一个 .NET 库，用于读取、生成和验证 JSON Schema 草案 v4+ 架构。
* [NuKeeper](https://github.com/NuKeeperDotNet/NuKeeper) - 自动更新 .NET 项目中的 nuget 包。
* [NuGetPackageExplorer](https://github.com/NuGetPackageExplorer/NuGetPackageExplorer) - 使用 GUI 创建、更新和部署 Nuget 包。
* [NugetVisualizer](https://github.com/sepharg/NugetVisualizer) - 可视化一组给定 git 存储库或文件夹的所有 nuget 包及其相应版本。
* [OctoLinker](https://github.com/OctoLinker/browser-extension) - 使用 GitHub 的 OctoLinker 浏览器扩展有效地浏览“projects.json”文件。
* [posh-dotnet](https://github.com/bergmeister/posh-dotnet) - [dotnet CLI](https://github.com/dotnet/cli) 的“PowerShell”选项卡补全。
* [Rin](https://github.com/mayuki/Rin) - ASP.NET Core 的请求/响应检查器中间件。就像一瞥。
* [scoop](https://github.com/lukesampson/scoop) - 适用于 Windows 的命令行安装程序。
* [SerilogAnalyzer](https://github.com/Suchiman/SerilogAnalyzer) - 使用 Serilog 日志记录库进行基于 Roslyn 的代码分析。检查常见错误和使用问题。
* [SharpZipLib](https://github.com/icsharpcode/SharpZipLib) - #ziplib 是一个完全用 C# 为 .NET 平台编写的 Zip、GZip、Tar 和 BZip2 库。
* [ShareX](https://github.com/ShareX/ShareX) - 免费开源程序，可让您捕获或记录屏幕的任何区域，并只需按一下键即可共享它。它还允许将图像、文本或其他类型的文件上传到 80 多个受支持的目的地，您可以从中选择。 [https://getsharex.com](https://getsharex.com)
* [SharpLab](https://github.com/ashmind/SharpLab) - .NET 代码游乐场，显示代码编译的中间步骤和结果。 [https://sharplab.io](https://sharplab.io)
* [SmartCode](https://github.com/Ahoo-Wang/SmartCode) - SmartCode= IDataSource -> IBuildTask -> IOutput => 构建一切！！！ （包括[代码生成器]）
* [sourcelink](https://github.com/dotnet/sourcelink) - SourceLink 是一个与语言和源代码控制无关的系统，用于为二进制文件提供一流的源代码调试体验。
* [System.CommandLine](https://github.com/dotnet/command-line-api) - System.CommandLine，一组用于命令行解析、调用和呈现终端输出的库。
* [Typin](https://github.com/adambajguz/Typin) - 易于使用的交互式 CLI 应用程序和命令行工具（直接模式）的声明性框架，其根源于 CliFx。
* [X.Web.Sitemap](https://github.com/dncuug/X.Web.Sitemap) - 适用于 .NET 和 .NET Core 的简单站点地图生成器
* [X.Web.RSS](https://github.com/dncuug/X.Web.RSS) - 适用于 .NET 和 .NET Core 的简单 RSS Feed 生成器

### 网络框架
* 网络组装
  * [Blazor](https://github.com/SteveSanderson/Blazor) - 通过 WebAssembly 在浏览器中运行 .NET 的 UI 框架。
    * [Awesome Blazor](https://github.com/AdrienTorris/awesome-blazor) - 有关 Blazor 的精彩资源（示例、组件、文章、视频等）集合。
    * [Blazor Redux](https://github.com/torhovland/blazor-redux) - 将 Redux 状态存储与 Blazor 连接。
  * [Ooui](https://github.com/praeclarum/Ooui) - 小型跨平台 UI 库，为 Web 带来了本机 UI 开发的简单性。
* [ReactJS.NET](https://github.com/reactjs/React.NET) - 用于 JSX 编译和 React 组件服务器端渲染的 .NET 库。
* [redux.NET](https://github.com/GuillaumeSalles/redux.NET) - .NET 应用程序的可预测状态容器。受到 [https://github.com/reactjs/redux](https://github.com/reactjs/redux) 的启发。

### 网络套接字
* [Fleck](https://github.com/statianzo/Fleck) - Fleck 是 C# 中的 WebSocket 服务器实现。 Fleck 不需要继承、容器或其他引用。
* [SignalR Server](https://github.com/aspnet/signalr) - Web 应用程序的实时 Web 功能，包括服务器端推送。
* [SuperSocket](https://github.com/kerryjiang/SuperSocket) - 轻量级、跨平台和可扩展的套接字服务器应用程序框架。
* [WampSharp](https://github.com/Code-Sharp/WampSharp) - [Web 应用程序消息传递协议](http://wamp-proto.org/) 的 C# 实现 - 提供远程过程调用和通过 WebSocket 发布/订阅的消息传递模式的协议。
* [websocket-manager](https://github.com/radu-matei/websocket-manager) - ASP .NET Core 的实时库。

### 视窗服务
* [dotnet-win32-service](https://github.com/dasMulli/dotnet-win32-service) - 直接从 .NET Core 设置并作为 Windows 服务运行。
* [Topshelf](https://github.com/Topshelf/Topshelf) - 用于使用 .NET 构建 Windows 服务的简单服务托管框架。

### 工作流程
* [CoreWF](https://github.com/dmetzgar/corewf/) - Windows Workflow Foundation (WF) 到 .NET Core 的端口。
* [workflow-core](https://github.com/danielgerlag/workflow-core) - .NET Standard 的轻量级工作流引擎。
* [WorkflowEngine.NET](https://github.com/optimajet/WorkflowEngine.NET) - 在您的应用程序中添加工作流程的组件。
* [Wexflow](https://github.com/aelassas/Wexflow) - 高性能、可扩展、模块化和跨平台的工作流引擎。

## 路线图
* [ASP.NET Core Developer Roadmap](https://github.com/MoienTajik/AspNetCore-Developer-Roadmap) - 2019 年成为 ASP.NET Core 开发人员的路线图。

## 入门套件
* [Arch](https://github.com/Arch) - .NET Core 库的集合，由拥抱 .NET Core 中所有新功能的软件架构师创建。
  * [AutoHistory](https://github.com/Arch/AutoHistory) - Microsoft.EntityFrameworkCore 的插件，支持自动记录数据更改历史记录。
* [AspNetCore-Angular2-Universal](https://github.com/MarkPieszak/aspnetcore-angular2-universal) - 跨平台 - 带服务器端渲染，用于 SEO、Bootstrap、i18n 国际化 (ngx-translate)、Webpack、TypeScript、带 Karma 的单元测试、WebAPI REST 设置、SignalR、Swagger 文档等等！
* [ASP.NET Core Starter Kit](https://github.com/kriasoft/aspnet-starter-kit) - 后端基于 .NET Core、Kestrel、GraphQL 和前端基于 Babel、Webpack、React 和 Redux 的 Web 开发的固定样板。该样板有 C# 和 F# 风格。
* [aspnetcore-spa generator](https://github.com/aspnet/JavaScriptServices) - Yeoman 生成器用于构建全新的 ASP.NET Core 单页应用程序，该应用程序在客户端上使用 Angular 2 / React / React With Redux / Knockout / Aurelia。
* [ASP.Net Core Vue Starter](https://github.com/MarkPieszak/aspnetcore-Vue-starter) - Asp.NETCore 2.0 Vue 2 (ES6) SPA 入门套件，包含路由、Vuex 等！
* [bitwarden-core](https://github.com/bitwarden/core) - 核心基础设施后端（API、数据库等）[https://bitwarden.com](https://bitwarden.com)。
* [dotNetify](https://github.com/dsuryd/dotNetify) - 构建实时 HTML5/C# .NET Web 应用程序的简单、轻量级但功能强大的方法。
* [generator-aspnet](https://github.com/OmniSharp/generator-aspnet) - yo ASP.NET Core 生成器。
* [Nucleus](https://github.com/alirizaadiyahsi/Nucleus) - Vue启动应用程序模板，后端使用ASP.NET Core API分层架构和基于JWT的身份验证
* [react-aspnet-boilerplate](https://github.com/pauldotknopf/react-aspnet-boilerplate) - 使用 ASP.NET Core 1 构建同构 React 应用程序的起点，利用现有技术。
* [saaskit](https://github.com/saaskit/saaskit) - 用于构建 SaaS 应用程序的开发人员工具包。
* [serverlessDotNetStarter](https://github.com/pharindoko/serverlessDotNetStarter) 入门套件，用于基于无服务器框架在 AWS 云中开发和部署 lambda 函数。

## 示例项目
* 微服务和服务网格
  * [clean-architecture-dotnet](https://github.com/thangchung/clean-architecture-dotnet) - 在电子商务示例业务领域应用具有 DDD-lite、CQRS-lite 和足够的云原生模式的最小清洁架构
  * [coolstore-microservices ](https://github.com/vietnam-devs/coolstore-microservices) - 具有 Istio 服务网格的基于 Kubernetes 的多语言微服务应用程序
  * [distributed-playground](https://github.com/jvandevelde/distributed-playground) - 包含 Vagrant、Consul、Docker 和 ASP.NET Core 的分布式服务游乐场。
  * [DNC-DShop](https://github.com/devmentors) - 分布式 .NET Core 项目和免费课程。 （DDD、CQRS、RabbitMQ、MongoDB、Redis、监控、日志记录、CI、CD）
  * [dotnetcore-microservices-poc](https://github.com/asc-lab/dotnetcore-microservices-poc) - 使用 .NET Core（EF Core、MediatR、Marten、Eureka、Ocelot、RabbitMQ、Polly、ElasticSearch、Dapper）在微服务架构中制作的简化保险销售系统以及博客文章系列。
  * [eShop](https://github.com/dotnet/eShop) - 实现电子商务站点的参考 .NET 应用程序。
  * [InMemoryCQRSReplication](https://github.com/Aaronontheweb/InMemoryCQRSReplication) - Akka.NET 参考架构 - CQRS + 分片 + 内存复制
  * [magazine-website](https://github.com/thangchung/magazine-website) - 应用 DDD、CQRS、微服务、异步编程的杂志网站（使用 .NET Core、ASP.NET Core、EF Core）。
  * [microservices-in-dotnetcore](https://github.com/horsdal/microservices-in-dotnet-book-second-edition) - 代码示例来自 [.NET Core 中的微服务](https://www.manning.com/books/microservices-in-net-core-second-edition) 第二版。
  * [Practical.CleanArchitecture](https://github.com/phongnguyend/Practical.CleanArchitecture) - 全栈 .Net 8 Clean 架构（微服务、模块化整体、整体）、Blazor、Angular 18、React 18、Vue 3、BFF with YARP、域驱动设计、CQRS、SOLID、Asp.Net Core 身份自定义存储、OpenID Connect、Entity Framework Core、OpenTelemetry、SignalR、托管服务、运行状况检查、速率限制、云服务（Azure、AWS、GCP）。
  * [practical-dapr](https://github.com/thangchung/practical-dapr) - 基于 Dapr 和 Tye 构建的全栈 .NET 微服务。
  * [ReactiveTraderCloud](https://github.com/AdaptiveConsulting/ReactiveTraderCloud) - 实时交易平台演示展示了在整个应用程序堆栈中应用的反应式编程原理。
* 巨石
  * [AlbumViewerVNext](https://github.com/RickStrahl/AlbumViewerVNext) - 西风专辑查看器 ASP.NET 5 示例。
  * [allReady](https://github.com/HTBox/allReady) - 开源解决方案专注于提高当地社区的人道主义和救灾组织开展的备灾活动的意识、效率和影响力。 [http://www.htbox.org/projects/allready](http://www.htbox.org/projects/allready)
  * [AspNet5GeoElasticsearch](https://github.com/damienbod/AspNet5GeoElasticsearch) - ASP.NET Core MVC Geo Elasticsearch Swashbuckle Swagger。
  * [aspnet-servicediscovery-patterns](https://github.com/cecilphillip/aspnet-servicediscovery-patterns) - 使用 ASP.NET Core 实现服务发现模式的示例。
  * [AspNetAuthorizationWorkshop](https://github.com/blowdart/AspNetAuthorizationWorkshop) - 介绍 ASP.NET Core 授权中各种新内容的研讨会
* [来自 Microsoft 的 BikeSharing360 应用程序套件](https://blogs.msdn.microsoft.com/visualstudio/2016/12/14/connectdemos-2016-bikesharing360-on-github/) 在 Connect 2016 年 12 月会议上提出，这是一套面向企业用户和消费者（自行车骑手）的综合性互操作应用程序：[移动应用程序](https://github.com/Microsoft/BikeSharing360_MobileApps)、[后端服务](https://github.com/Microsoft/BikeSharing360_BackendServices)、[网站](https://github.com/Microsoft/BikeSharing360_Websites)、[单容器应用程序](https://github.com/Microsoft/BikeSharing360_SingleContainer)、[多容器应用程序](https://github.com/Microsoft/BikeSharing360_MultiContainer)、[认知服务亭应用程序](https://github.com/Microsoft/BikeSharing360_CognitiveServicesKioskApp)、
[Azure 机器人应用程序](https://github.com/Microsoft/BikeSharing360_BotApps)。
  * [Clean Architecture Manga](https://github.com/ivanpaulovich/clean-architecture-manga) - 使用 .NET Core 3.0 和 C# 8 的干净架构示例。用例作为中心组织结构，完全可测试，与框架分离。
  * [cloudscribe](https://github.com/cloudscribe/cloudscribe) - ASP.NET Core 多租户 Web 应用程序基础。
  * [CoreCodeCamp](https://github.com/shawnwildermuth/CoreCodeCamp) - 用于举办小型本地开发活动的开源网站。
  * [DotNetClub](https://github.com/scheshan/DotNetClub) - 用 ASP.NET Core 编写的小型俱乐部。
  * [eShopOnWeb](https://github.com/dotnet-architecture/eShopOnWeb) - 具有整体部署模型的分层应用程序架构。
  * [Entropy](https://github.com/aspnet/Entropy) - 新功能和想法的混乱实验游乐场 - 在此处查看各个功能的小而简单的示例。
  * [EquinoxProject](https://github.com/EduardoPires/EquinoxProject) - 具有 DDD、CQRS 和事件源的完整 ASP.NET Core 2.0 应用程序。
  * [GenVue](https://github.com/herbat73/GenVue) - 一个可托管的 Web 应用程序，允许机密用户上传和共享基于 Vue.js、Vuetifyjs 和 NetCore WebAPI 堆栈构建的私人文件
  * [guidance-identity-management-for-multitenant-apps](https://github.com/Azure-Samples/guidance-identity-management-for-multitenant-apps) - 如何使用 Azure Active Directory 进行身份验证，在 Microsoft Azure 上的多租户应用程序中管理用户身份。
  * [JustA.ML](https://github.com/mustakimali/JustA.ML) - 一个 Web 应用程序，可让您在使用 ASP.NET Core 2.0 编写的设备之间共享文件/URL/文本。开源，位于 [https://justa.ml](https://justa.ml)
  * [MegaMine](https://github.com/Nootus/MegaMine) - 开源挖矿解决方案，帮助矿工提取黄金、石英、花岗岩等。该解决方案使用 ASP.NET Core 和 AngularJS 构建，并以微服务方式利用多个轻量级组件。
  * [MusicStore](https://github.com/dotnet/aspnetcore/tree/master/src/MusicStore) - 使用 MVC 和实体框架的示例 MusicStore 应用程序。
  * [NLayerAppV3](https://github.com/cesarcastrocuba/nlayerappv3) - NLayerAppV3 N 层架构与 .NET Core Preview 2。
  * [NorthwindTraders](https://github.com/JasonGT/NorthwindTraders) - Northwind Traders 是一个使用 ASP.NET Core 和 Entity Framework Core 构建的示例应用程序。
  * [Orchard Core - Modular and Multi-tenant applications](https://github.com/OrchardCMS/OrchardCore.Samples) - 使用 Orchard Core Framework 创建模块化和多租户应用程序。
  * [PhotoGallery](https://github.com/chsakell/aspnet5-angular2-typescript) - 使用 ASP.NET Core、Angular 2 和 TypeScript 的跨平台单页应用程序 [http://wp.me/p3mRWu-11L](http://wp.me/p3mRWu-11L)。
  * [PokeR](https://github.com/halomademeapc/pokeR) - 在 ASP.NET Core 的 SPA 托管中使用 SignalR 和 Angular 进行实时 scrum 扑克游戏。  包括 Docker 支持。 [演示](https://planning.halomademeapc.com)
  * [Practical ASP.NET Core](https://github.com/dodyg/practical-aspnetcore) - 每日更新 ASP.NET Core 功能和设施的微示例。
  * [Practical.CleanArchitecture](https://github.com/phongnguyend/Practical.CleanArchitecture) - 全栈 .Net 8 Clean 架构（微服务、模块化整体、整体）、Blazor、Angular 18、React 18、Vue 3、BFF with YARP、域驱动设计、CQRS、SOLID、Asp.Net Core 身份自定义存储、OpenID Connect、Entity Framework Core、OpenTelemetry、SignalR、托管服务、运行状况检查、速率限制、云服务（Azure、AWS、GCP）。
  * [Sample .NET Core CQRS REST API](https://github.com/kgrzybek/sample-dotnet-core-cqrs-api) - 使用 Clean Architecture 的原始 SQL 和 DDD 实现 .NET Core REST API CQRS 实现。
  * [StarWars](https://github.com/JacekKosciesza/StarWars) - 使用 GraphQL for .NET、ASP.NET Core、Entity Framework Core 的 GraphQL“星球大战”示例。
 
## 文章
* 基础知识
  * [Microsoft 全面的 BikeSharing360 演示应用程序套件的架构概述以及相关视频](https://blogs.msdn.microsoft.com/visualstudio/2016/12/14/connectdemos-2016-bikesharing360-on-github/)
  * [将 .NET Framework 库移植到 .NET Core](https://www.codeproject.com/Articles/1190475/Porting-a-NET-Framework-library-to-NET-Core)
  * [CLR 在执行单行代码之前执行的 68 件事](http://mattwarren.org/2017/02/07/The-68-things-the-CLR-does-before-executing-a-single-line-of-your-code/)
* .NET Core 和 Nodejs 之间的比较位于[此处](https://manuel-rauber.com/2016/03/07/node-js-asp-net-core-1-0-a-usage-comparison/)、[此处](https://gist.github.com/ilyaigpetrov/f6df3e6f825ae1b5c7e2) 和[此处](https://github.com/thinktecture/nodejs-aspnetcore-webapi)
  * [了解 ASP.NET Core 初始化](http://developer.telerik.com/featured/understanding-asp-net-core-initialization/)
  * [为什么你应该加入 .NET Core 和 ASP.NET Core 培训](https://codingblast.com/why-you-should-join-asp-net-core/)
* 云开发
  * [在 .NET Core 中配置 AWS 开发工具包](https://aws.amazon.com/blogs/developer/configuring-aws-sdk-with-net-core/)
  * [使用 C# 和 AWS Amazon Gateway Api/Lambda 的无服务器架构](https://www.codeproject.com/Articles/1178781/Serverless-Architecture-using-Csharp-and-AWS-Amazo)
  * [在 Amazon Web Services (AWS) Lambda 中使用 C# 和 .NET Core](https://aws.amazon.com/blogs/compute/announcing-c-sharp-support-for-aws-lambda/)
* 配置和部署
  * [.NET项目结构](https://gist.github.com/davidfowl/ed7564297c61fe9ab814)
  * [将 Travis CI 构建添加到 .NET Core 应用程序](http://andrewlock.net/adding-travis-ci-to-a-net-core-app/)
  * [ASP.NET Core 1.0 - 配置 ApplicationInsights](http://social.technet.microsoft.com/wiki/contents/articles/35918.asp-net-core-1-0-configure-applicationinsights.aspx)
  * [haproxy、nginx、Angular 2、ASP.NET Core、Redis 和 Docker](http://tattoocoder.azurewebsites.net/legion-of-heroes-haproxy-nginx-angular2-aspnetcore-redis-docker/)
  * [Project.json 到 MSBuild 转换指南](http://www.natemcmaster.com/blog/2017/01/19/project-json-to-csproj/)
  * [使用 Appveyor 和 NuGet 发布 .NET 项目](https://few-lines-of-code.blogspot.com/2016/03/publishing-net-project-with-appveyor.html)
  * [ASP.NET Core 中的新配置模型](http://developer.telerik.com/featured/new-configuration-model-asp-net-core/)
* 实体框架核心
  * [.NET Core 数据访问](https://blogs.msdn.microsoft.com/dotnet/2016/11/09/net-core-data-access/)
  * [关于 EF Core 的一个很好的例子](https://github.com/rowanmiller/Demo-EFCore)
  * [使用 EF Core 连接到 Postgres](http://en.otomatikmuhendis.com/2017/05/05/connect-to-postgres-with-ef-core/)
* 神奇的
  * [开始使用 Orchard Core 作为 NuGet 包](http://www.ideliverable.com/blog/getting-started-with-orchard-core-as-a-nuget-package)
  * [如何在 ASP.NET Core 中将 HTML 导出为 PDF](https://code.msdn.microsoft.com/How-to-export-HTML-to-PDF-c5afd0ce)
  * [使用 ASP.NET Core 进行 Vue.js 服务器端渲染](http://mgyongyosi.com/2016/Vuejs-server-side-rendering-with-aspnet-core/)
* 安全
  * [.NET 持续交付微服务](http://stackshare.io/tomstaijen/net-continuous-delivery-microservices)
  * [ASP.NET Core 2.0 身份验证和授权系统揭秘](https://digitalmccullough.com/posts/aspnetcore-auth-system-demystified.html)
  * [ASP.NET 授权实验室演练](https://github.com/blowdart/AspNetAuthorizationWorkshop)
  * [ASP.NET Core 中的身份验证](https://stormpath.com/blog/authentication-asp-net-core)
* 测试
  * [Selenium 与 .NET Core](http://www.dotnetcatch.com/2016/11/23/selenium-with-net-core/)
- [InfoQ .NET articles](https://www.infoq.com/dotnet) - InfoQ 网站上的最佳 .NET 文章集合

## 书籍
* [.NET Core 实际应用](https://manning.com/books/dotnet-core-in-action)
* [ASP.NET Core 应用程序开发：在四个冲刺中构建应用程序（开发人员参考）](https://www.amazon.com/ASP-NET-Core-Application-Development-application/dp/1509304061)
* [ASP.NET Core 实际应用](https://www.manning.com/books/asp-net-core-in-action)
* [ASP.NET Core 1.0 高性能](https://www.amazon.com/ASP-NET-Core-1-0-High-Performance/dp/1785881892)
* [使用 ASP.NET Core 构建微服务：在云中开发、测试和部署跨平台服务](https://www.amazon.com/Building-Microservices-ASP-NET-Core-Cross-Platform/dp/1491961732)
* [C# 6 和 .NET Core 1.0：现代跨平台开发](https://www.amazon.com/NET-Core-1-0-Cross-Platform-Development/dp/1785285696)
* [C# 深入探讨 4](https://www.amazon.com/C-Depth-Jon-Skeet/dp/1617294535)
* [.NET Core 中的依赖注入，第二版](https://www.manning.com/books/dependency-injection-in-dot-net-second-edition)
* [C# 7.0 基础](https://www.amazon.com/Essential-7-0-Addison-Wesley-Microsoft-Technology/dp/1509303588)
* [利用微服务、ASP.NET Core 和 Entity Framework Core 探索 .NET Core - 免费电子书采样器](https://www.manning.com/books/exploring-dot-net-core)
* [.NET Core 中的微服务：使用 C#、Nancy 框架和 OWIN 中间件](https://www.amazon.com/Microservices-NET-Core-framework-middleware/dp/1617293377)
* [专业 C# 6 和 .NET Core 1.0](https://www.amazon.com/Professional-NET-Core-Christian-Nagel/dp/111909660X)
* [小小的 ASP.NET Core](https://www.recaffeinate.co/book)


## 视频
* [Channel9](https://channel9.msdn.com) - 微软软件定义网络
* [Channel9](https://www.youtube.com/channel/UCsMica-v34Irf9KVTh6xx-g) - YouTube
* [微软学习中心](https://dotnet.microsoft.com/learn/aspnet)
 * [ASP.NET 怪物](https://channel9.msdn.com/Series/aspnetmonsters)
* [视觉工作室](https://www.youtube.com/user/VisualStudio/channels)

## 播客
* [.NET 摇滚](https://www.dotnetrocks.com)
* [合并冲突](http://www.mergeconflict.fm/)
* [.NET 的声音](http://thesoundof.net/?q=.NET+Core)

## 社区
* [.NET基金会](http://forums.dotnetfoundation.org)
* [.NET 博客](https://devblogs.microsoft.com/dotnet/)
* [/r/CoolGithubProjects](https://www.reddit.com/r/coolgithubprojects)
* [ASP.NET](https://forums.asp.net)
* [Channel9](https://channel9.msdn.com)
* [很棒的 .NET 开源和社区资源](https://discoverdot.net)
* [Slack](http://tattoocoder.com/aspnet-slack-sign-up)
* [BuiltWithDot.Net](https://builtwithdot.net)
* [awesome-copilot](https://github.com/github/awesome-copilot)
* 堆栈溢出
  * [.NET核心](https://stackoverflow.com/questions/tagged/.net-core)
  *  [CoreCLR](https://stackoverflow.com/questions/tagged/coreclr)
  * [ASP.NET 核心](https://stackoverflow.com/questions/tagged/asp.net-core)
  * [ASP.NET Core MVC](https://stackoverflow.com/questions/tagged/asp.net-core-mvc)
  * [ASP.NET 核心 1.0](https://stackoverflow.com/questions/tagged/asp.net-core-1.0)
  * [实体框架核心](https://stackoverflow.com/questions/tagged/entity-framework-core)
* [当今 GitHub 上的热门 .NET 存储库](https://github.com/trending?l=csharp)

## 许可证

[![CC0](http://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

在法律允许的范围内，[thangchung](http://weblogs.asp.net/thangchung) 已放弃本作品的所有版权以及相关或邻接权。

