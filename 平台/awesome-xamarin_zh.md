~~# Awesome-Xamarin [![Awesome](https://awesome.re/badge.svg)](https://github.com/sindresorhus/awesome) [![PR 欢迎](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)~~


该仓库现已**归档**，请参阅[awesome-dotnet-maui](https://github.com/jsuarezruiz/awesome-dotnet-maui)


~~精心挑选的书签集合，包含主观上现代/有趣且理想的 Xamarin Android/iOS/Windows/OSX 开源库/工具~~


## 内容
- [General](#general)
- [Architecture](#architecture)
- [Async](#async)
- [Charts](#charts)
- [Cloud](#cloud)
- [Database](#database)
- [Fody](#fody)
- [Framework](#framework)
- [游戏引擎](#game-engine)
- [IO/Storage](#iostorage)
- [IOC/DI](#iocdi)
- [Internationalization](#internationalization)
- [Layout](#layout)
- [Media](#media)
- [MVVM](#mvvm)
- [Network](#network)
- [Reactive](#reactive)
- [Security](#security)
- [Serialization](#serialization)
- [TDD/BDD](#tddbdd)
- [Tools](#tools)
- [UI](#ui)
- [Wearable](#wearable)
- [Xamarin.Forms](#xamarinforms)
- [XPlat API](#xplat-apis)
- [其他清单](#other-lists)
- [Websites](#websites)


## 一般

- [AutoMapper ★5,724](https://github.com/AutoMapper/AutoMapper) - .NET 中基于约定的对象到对象映射器。
- [Fluent Validation ★3,570](https://github.com/FluentValidation/FluentValidation) - 用于构建验证规则的流畅接口和 lambda 表达式。
- [Humanizer ★3,426](https://github.com/Humanizr/Humanizer) - 操作和显示字符串、枚举、日期、时间、时间跨度、数字和数量。
- [NodaTime ★970](https://github.com/nodatime/nodatime) - .NET 的替代日期和时间 API。
- [Polly ★4,666](https://github.com/App-vNext/Polly) - 异常处理策略，例如重试、永远重试、等待并重试或断路器。


## 建筑

- [Behaviors Toolkit ★34](https://github.com/ThomasLebrun/XamarinBehaviorsToolkit) - 一种使用最少的代码向 Xamarin 应用程序添加常见且可重用的交互性的方法。
- [Conditions ★48](https://github.com/ghuntley/conditions) - 帮助开发人员以流畅的方式编写前置条件和后置条件验证的库。
- [Stateless ★2,294](https://github.com/dotnet-state-machine/stateless) - 状态机。


## 异步

- [AsyncEx ★1,253](https://github.com/StephenCleary/AsyncEx) - 用于异步/等待的辅助库。
- [LinqToAwait ★99](https://github.com/anaisbetts/LinqToAwait) - 基于任务的 LINQ，旨在与异步/等待配合使用。


## 图表

- [MicroCharts ★1052](https://github.com/microcharts-dotnet/Microcharts) - 创建跨平台（Xamarin、Windows...）简单图表。
- [MPAndroidChart/iOSCharts ★6](https://github.com/bulubuloa/Ultimate-Xamarin-Forms-KIT) - MPAndroidChart/iOSCharts 绑定支持在 Xamarin Forms 中使用。
- [OxyPlot ★1,311](https://github.com/oxyplot/oxyplot) - .NET 的跨平台绘图库。


## 云

- [Azure](https://docs.microsoft.com/en-us/xamarin/cross-platform/data-cloud/) - 微软Azure。
- [Bugfender ★10](https://github.com/bugfender/bugfender-xamarin) - 将您的应用程序日志存储在云端（iOS 和 Android）。
- [FireSharp ★479](https://github.com/ziyasal/FireSharp) - Firebase REST API 包装器。


## 数据库

- [Akavache ★1,692](https://github.com/reactiveui/akavache) - 用于本机应用程序的异步键值存储。
- [Breeze ★63](https://github.com/Breeze/breeze.sharp) - 面向富客户端应用程序开发人员的数据管理库。
- [Couchbase.Lite ★299](https://github.com/couchbase/couchbase-lite-net) - 轻量级嵌入式NoSQL数据库。
- [Lager ★2](https://github.com/ghuntley/Lager) - 使用 Akavache 作为存储后端的跨平台设置存储。
- [Massive ★1,708](https://github.com/FransBouma/Massive) - 数据库表的“包装器”并广泛使用 System.Dynamic。
- [Realm ★690](https://github.com/realm/realm-dotnet) - 直接在手机、平板电脑或可穿戴设备内运行的移动数据库。
- [Settings ★58](https://github.com/aritchie/settings) - 适用于 Xamarin 和 Windows 的跨平台设置插件。
- [SQLite.Net-PCL ★340](https://github.com/oysteinkrog/SQLite.Net-PCL) - SQLite 3 数据库支持、PCL、异步。
- [LiteDB ★4245](https://github.com/mbdavid/LiteDB) - 单个数据文件中的 .NET NoSQL 文档存储。
- [DB4O-GPL ★8](https://github.com/iboxdb/db4o-gpl) - 支持面向对象的数据库、嵌入式和远程连接。

## 福迪

- [Fody ★2,150](https://github.com/Fody/Fody) - 用于编织 .net 程序集的可扩展工具。
	- [AutoDependencyProperty.Fody](https://bitbucket.org/robertvazan/autodependencyproperty.fody/src) - 从简单的 C# 属性自动生成 DependencyProperty 样板。
	- [PropertyChanged.Fody ★820](https://github.com/Fody/PropertyChanged/) - 在编译时将 INotifyPropertyChanged 代码注入到属性中。
	- [ReactiveUI.Fody ★105](https://github.com/kswoll/ReactiveUI.Fody) - 为属性和 ObservableAsPropertyHelper 属性生成 RaisePropertyChange 通知。


## 框架

- [Ammy](http://www.ammyui.com/) - XAML 平台的现代 UI 语言。免费用于非商业开发。
- [Appercode.UIFramework ★13](https://github.com/Appercode/Appercode.UIFramework) - 允许使用单一 XAML 布局构建跨平台移动应用程序的用户界面。
- [Invention](https://gitlab.com/hodgskin-callan/Invention) - 使用 Visual Studio 和 C#.NET 开发适用于 iOS、Android 和 Windows 的本机应用程序，并实现 100% 代码共享。
- [SimplyMobile ★103](https://github.com/sami1971/SimplyMobile) - 抽象移动功能的集合。
- [Xamu-Infrastructure ★104](https://github.com/xamarinhq/xamu-infrastructure) - 扩展、MVVM 类、行为和其他杂项。来自 Xamarin 大学的有用代码位。

## 游戏引擎

- [CocosSharp ★463](https://github.com/mono/CocosSharp) - Cocos2D 和 Cocos3D API 的 CSharp 实现。
- [MonoGame ★5,276](https://github.com/MonoGame/MonoGame) - Microsoft XNA 4.x 框架的开源实现。
- [Paradox ★1,706](https://github.com/SiliconStudio/xenko) - Paradox3D + Silicon Studio .NET。
- [UrhoSharp ★275](https://github.com/xamarin/urho) - 跨平台高级 3D 和 2D 引擎。
- [CocosCreator ★2](https://github.com/toanlcgift/xamarin-cocos-creator) - CocosCreator 引擎的 Xamarin 绑定。


## IO/存储

- [IO ★6](https://github.com/aritchie/io) - 使用熟悉的 API 访问系统文件夹和文件。
- [PCL Storage ★270](https://github.com/dsplaisted/PCLStorage) - 适用于 .NET 的一致、可移植的本地文件 IO API 集。
- [FilePicker-Plugin-for-Xamarin ★37](https://github.com/jfversluis/FilePicker-Plugin-for-Xamarin-and-Windows) - 简单的跨平台插件，允许您选择文件并使用它们。


## 国际奥委会/DI

- [Autofac ★2,169](https://github.com/autofac/Autofac) - 令人上瘾的 .NET IoC 容器。
- [DryIoc](https://github.com/dadhi/DryIoc) - 适用于 .NET 的快速、小型、功能齐全的 IoC 容器。
- [Funq ★2](https://github.com/thiagoromam/FunqPortable) - 通过使用 lambda 和泛型函数作为工厂来消除所有运行时反射，从而实现高性能 DI 框架。
- [LightInject ★320](https://github.com/seesharper/LightInject) - 适用于 .NET 的轻量、简单且速度惊人的 IoC 容器。
- [Ninject ★2,034](https://github.com/ninject/Ninject) - .net 依赖注入器的忍者。
- [Stiletto ★36](https://github.com/benjamin-bader/stiletto) - Dagger 的 .NET 端口，来自 Square 的轻量级 Android 依赖注入器。
- [TinyIoC ★585](https://github.com/grumpydev/TinyIoC) - 单类简单 IoC 容器。


## 国际化

- [I18NPortable ★49](https://github.com/xleon/I18N-Portable) - Xamarin 和 .NET 的简单跨平台国际化/翻译。
- [Resxible ★9](https://github.com/apcurium/resxible) - 用于从单个 RESX 文件自动生成多个依赖于平台的资源文件的工具。
- [Vernacular ★167](https://github.com/rdio/vernacular) - 跨平台本地化，转换标准字符串格式的工具。
- [SimpleLocalize ★19](https://github.com/simplelocalize/simplelocalize-cli) - 用于管理 Xmarin 项目中的 i18n 密钥的开源工具。


## 布局

- [Flex ★128](https://github.com/xamarin/flex) - 灵活的盒子布局系统。


## 媒体

- [EZ-Compress ★11](https://github.com/VictorGrunn/EZ-Compress-for-Xamarin) - 一个简单的 Xamarin 图像流压缩插件。
- [Fast & Furious Image Loading ★820](https://github.com/luberda-molinet/FFImageLoading) - Xamarin 库可快速轻松地加载图像。
- [Lottie ★643](https://github.com/Baseflow/LottieXamarin) - 在 Android 和 iOS 上为 Xamarin 原生渲染 After Effects 动画。
- [LibVLCSharp ★174](https://github.com/videolan/libvlcsharp) - libvlc 的 Xamarin 绑定，libvlc 是为 VideoLAN 制作的 VLC 应用程序提供支持的多媒体框架。
- [MediaManager ★269](https://github.com/Baseflow/XamarinMediaManager) - 用于播放 PCL 媒体的跨平台 Xamarin 插件。
- [NGraphics ★482](https://github.com/praeclarum/NGraphics) - 用于渲染矢量图形的跨平台库。
- [PDFReader ★51](https://github.com/AlexanderMac/mTouch-PDFReader) - 用于在 iPad 和 iPhone 上显示 PDF 文档的 iOS（仅限）库。
- [Screenshot Plugin ★21](https://github.com/wilsonvargas/ScreenshotPlugin) - 一个用于 Xamarin 和 Windows 的简单屏幕截图插件，用于在您的应用程序中获取和保存屏幕截图。
- [SkiaSharp ★920](https://github.com/mono/SkiaSharp) - 用于处理 2D 图形的强大 C# API。它由 Google 的 Skia 库提供支持。
- [Splat ★590](https://github.com/reactiveui/splat) - 跨平台图像加载、颜色等等。
- [SimpleAudioPlayer ★14](https://github.com/adrianstevens/Xamarin-Plugins/tree/master/SimpleAudioPlayer) - 用于以流形式播放本地文件和音频数据的简单插件。
- [ZXing.Net.Mobile ★570](https://github.com/Redth/ZXing.Net.Mobile) - 适用于 MonoTouch、Mono for Android 和 Windows Phone 的条码扫描库。
- [SupportMediaXF ★2](https://github.com/bulubuloa/SupportMediaXF) - 简单的跨平台插件，用于拍照或从共享代码的图库中挑选照片


## MVVM

- [Bind ★158](https://github.com/praeclarum/Bind) - Bind 为您提供了对象属性之间轻松的双向数据绑定。
- [EBind](https://github.com/SIDOVSKY/EBind) - 简洁、快速且功能丰富的 .NET 数据与一些 Xamarin 功能绑定。
- [FreshMvvm ★324](https://github.com/rid00z/FreshMvvm) - 专为 Xamarin.Forms 设计的超轻 Mvvm 框架。
- [Infinite Scroll Plugin ★24](https://github.com/HBSequence/Sequence.Plugins) - 一个插件，可促进分页数据源的仅向前增量滚动。
- [MVVMCross ★2,657](https://github.com/MvvmCross/MvvmCross) - 跨平台 mvvm 移动开发框架。
  - [Cheesebaron.MvxPlugins ★79](https://github.com/Cheesebaron/Cheesebaron.MvxPlugins) - 插件的集合。
  - [MvxAms ★1](https://github.com/MobiliTips/MvxPlugins/tree/master/MvxAms) - MVVMCross Azure 移动服务插件。
  - [MvxForms ★1](https://github.com/MobiliTips/MvxPlugins/tree/master/MvxForms) - 用于使用 Xamarin.Forms 的 MVVMCross 插件。
- [MugenMvvmToolkit ★127](https://github.com/MugenMvvmToolkit/MugenMvvmToolkit) - 跨平台 MVVM 工具包。
- [MVVMLight](https://github.com/lbugnion/mvvmlight) - 跨平台MVVM开发框架。
- [MvvmNano ★46](https://github.com/aspnetde/MvvmNano) - 使用 ❤ 为 Xamarin.Forms 制作的小型智能 MVVM 框架。
- [Prism ★2,365](https://github.com/prismlibrary/prism) - 跨平台MVVM开发框架。
- [ReactiveUI ★3,917](https://github.com/reactiveui/ReactiveUI) - Rx MVVM 框架。
- [Wires ★28](https://github.com/dotnet-ad/Wires) - Wires 是一个简单的绑定库。


## 网络

- [Apizr ★4](https://github.com/Respawnsive/Apizr) - 基于 Refit 的 Web API 客户端，但具有弹性（重试、连接、缓存、身份验证、日志、优先级等）。
- [Connectivity ★200](https://github.com/jamesmontemagno/ConnectivityPlugin) - 跨平台网络/连接状态。
- [CrossDownloadManager ★67](https://github.com/SimonSimCity/Xamarin-CrossDownloadManager) - Xamarin 的跨平台下载管理器。
- [Flurl ★1,295](https://github.com/tmenier/Flurl) - Flurl 是一个现代、流畅、异步、可测试、可移植、充满流行语的 URL 构建器和 HTTP 客户端库。
- [Fusillade ★216](https://github.com/reactiveui/Fusillade) - 一组 HttpMessageHandler，使您的移动应用程序更加高效和响应。
- [Messaging ★1](https://github.com/cjlotz/Xamarin.Plugins/tree/master/Messaging) - 使用默认消息应用程序拨打电话、发送短信或发送电子邮件。
- [ModernHttpClient](https://github.com/alexrainman/ModernHttpClient) - 使用移动优化库 (NSURLSession / OkHttp) 加速 HTTP 请求。
- [NFC ★14](https://github.com/smstuebe/xamarin-nfc) - 用于读取 NFC 标签的 Xamarin 插件。
- [Push Notification ★1](https://github.com/rdelrosario/xamarin-plugins/tree/master/PushNotification) - 简单的跨平台插件，用于处理推送通知事件，例如 Android 和 iOS 上的注册、取消注册和消息到达。
- [Reachability ★25](https://github.com/has-taiar/Reachability.Net) - 在线/离线连接检查。
- [Refit ★2,762](https://github.com/reactiveui/refit) - 适用于 Xamarin 和 .NET 的自动类型安全 REST 库。
- [RestEase ★339](https://github.com/canton7/RestEase) - 改装类固醇，更简单的身份验证，解析......
- [RestLess ★57](https://github.com/letsar/RestLess) - 适用于 .Net Standard 的自动类型安全无反射 REST API 客户端库。
- [RestSharp ★6,994](https://github.com/restsharp/RestSharp) - 适用于 .NET 的简单 REST 和 HTTP API 客户端。
- [Sockets ★185](https://github.com/rdavisau/sockets-for-pcl) - 对 .NET 和 WinRT 的套接字帮助器类的抽象。
- [Tiny.RestClient ★31](https://github.com/jgiacomini/Tiny.RestClient) - 适用于 Xamarin 和 .NET 的最简单的 Fluent REST 客户端。


## 反应性

- [Akavache ★1,692](https://github.com/reactiveui/Akavache) - 用于本机应用程序的异步键值存储。
- [ReactiveUI ★3,917](https://github.com/reactiveui/ReactiveUI) - Rx MVVM 框架。
- [Refit ★2,762](https://github.com/reactiveui/refit) - Refit 是一个深受 Square 的 Retrofit 库启发的库，它将您的 REST API 转变为实时界面。
- [ReactiveProperty ★361](https://github.com/runceel/ReactiveProperty) - 在 Reactive Extensions 下提供 MVVM 和异步支持功能。
- [RxFlow ★18](https://github.com/ugaya40/RxFlow) - 带有 Rx（反应式扩展）的简单流量控制库。
- [Sensors](https://github.com/aritchie/sensors) - 适用于 Xamarin 和 Windows 的 ACR 反应传感器插件。
- [CrossPlatformLiveData](https://github.com/jakdor/CrossPlatformLiveData) - Android LiveData 启发了 .NET 实现 - 生命周期感知的 rx 流。


## 安全性

- [Portable.BouncyCastle ★136](https://github.com/novotnyllc/bc-csharp) - Bouncy Castle 的便携式版本，支持 .NET 4、.NET Standard 2.0、MonoAndroid、Xamarin.iOS、.NET Core。
- [BreachDetector ★11](https://github.com/nmilcoff/BreachDetector) - 检测 Xamarin 应用程序中的 root、模拟、调试模式和其他安全问题。
- [Cryoprison](https://github.com/padresmurfa/cryoprison) - Xamarin 越狱/Root 检测
- [Fingerprint Plugin ★165](https://github.com/smstuebe/xamarin-fingerprint) - 用于访问指纹传感器的 Xamarin 和 MvvMCross 插件。
- [PCLCrypto ★184](https://github.com/AArnott/PCLCrypto) - 可移植类库的密码学（MD5，...）。
- [Permissions ★255](https://github.com/jamesmontemagno/PermissionsPlugin) - 简单的跨平台插件，用于检查移动设备的连接状态、收集连接类型、带宽等。


## 序列化

- [Newtonsoft.Json ★5,812](https://github.com/JamesNK/Newtonsoft.Json) - 适用于 .NET 的流行高性能 JSON 框架。
- [Quicktype ★886](https://app.quicktype.io/?l=cs) - 立即从 JSON 生成类和 JSON 序列化代码。


## 时分双工/业务双工

- [FluentAssertions](https://fluentassertions.com) - TDD/BDD 流畅断言。
- [NBehave ★47](https://github.com/nbehave/NBehave) - 行为驱动开发框架。
- [VSMac-CodeCoverage](https://github.com/ademanuele/VSMac-CodeCoverage) - 从 Visual Studio for Mac 收集单元测试项目的代码覆盖率结果。


## 工具

- [Cheeseknife ★53](https://github.com/MarcelBraghetto/Cheeseknife) - Xamarin.Android 的视图注入库。
- [IconFont2Code ★52](https://github.com/andreinitescu/IconFont2Code) - 使用字体文件 (.ttf/.otf) 中的字形 Unicode 值生成 C# 类。
- [GradleBindings ★103](https://github.com/EgorBo/Xamarin.GradleBindings) - Visual Studio 扩展，用于在 Android 项目中引用 gradle 库。
- [Material icons generator plugin - Xamarin Studio ★14](https://github.com/interisti/xs-material-icons-generator) - 添加材质图标到android项目。
- [Material icons generator plugin - Visual Studio](https://github.com/interisti/vs-material-icons-generator) - 添加材质图标到android项目。
- [Mutatio ★18](https://github.com/yuv4ik/Mutatio) - Visual Studio for Mac 加载项/扩展，用于自动将旧 PCL 转换为 .NET Standard 2.0 目标项目。
- [PushSharp ★3,990](https://github.com/Redth/PushSharp) - 一个服务器端库，用于将推送通知发送到 iOS (iPhone/iPad APNS)、Android（C2DM 和 GCM - Google Cloud Message）、Windows Phone、Windows 8、Amazon、Blackberry 和（即将推出）FirefoxOS 设备！
- [Twin Tools Add-In ★20](https://github.com/twintechs/TwinToolsForXamarin) - Xamarin Studio 的生产力插件。
- [Xamaridea ★69](https://github.com/EgorBo/Xamaridea) - Visual Studio 扩展，在 Android Studio 中打开 *.axml 文件。
- [Xavtool ★15](https://github.com/gabrielrobert/xavtool) - 自动增加 iOS / Android / UWP 应用程序版本的命令行实用程序。
- [Xamarin-APRTextFieldSuggestions](https://github.com/aproram/Xamarin-APRTextFieldSuggestions) - Xamarin.iOS iOS 中 UITextfield 的自动完成建议。
- [VSMac-CodeDistribution](https://github.com/ademanuele/VSMac-CodeDistribution) - 一个 Visual Studio for Mac 扩展，可可视化项目之间的代码分配。对于 Xamarin 项目了解平台之间共享的代码量特别有用。


## 用户界面
- [Xamarin.Forms.Breadcrumb](https://github.com/IeuanWalker/Xamarin.Forms.Breadcrumb) - 自动生成面包屑控件的控件
- [Xamarin.Forms.StateButton](https://github.com/IeuanWalker/Xamarin.Forms.StateButton) - 使用此控件，您可以创建任何样式的按钮。这是可能的，因为它充当 XAML 的包装器，并为您提供要绑定的事件/命令和属性。
- [Passcode ★13](https://github.com/kevinskrei/XamarinPasscode) - 用于使用密码锁定应用程序的 Xamarin 组件。
- [SignaturePad ★117](https://github.com/xamarin/SignaturePad) - Signature Pad 使得在 Xamarin.iOS、Xamarin.Android 和 Windows 上捕获、保存、导出和显示签名变得极其简单。
- [XamEffects ★53](https://github.com/mrxten/XamEffects) - Xamarin.Forms 的触摸效果。
- [Showcase View](https://github.com/DigitalSa1nt/Xama.JTPorts.ShowcaseView) - _Xamarin.Android_ 本机展示视图。易于使用的可定制展示案例视图，带有圆形显示动画。
- [Animated Circle Loading View](https://github.com/DigitalSa1nt/Xama.JTPorts.AnimatedCircleLoadingView) - 确定/不确定加载视图动画。
- [Animated Icon Button](https://github.com/HankiDesign/DOFavoriteButton.Xamarin) - Xamarin.iOS 的动画图标按钮。
- [SimpleBottomDrawer](https://github.com/galadril/Xam.Plugin.SimpleBottomDrawer) - 只是一个适合您的 Xamarin Forms 项目的漂亮而简单的 BottomDrawer
- [SimpleColorPicker](https://github.com/galadril/Xam.Plugin.SimpleColorPicker) - 只是一个适合您的 Xamarin Forms 项目的漂亮且简单的 ColorPicker
- [SimpleAppIntro](https://github.com/galadril/Xam.Plugin.SimpleAppIntro) - 只是一个适用于您的 Xamarin Forms 项目的漂亮且简单的 AppIntro
- [SimpleStaticMap](https://github.com/galadril/Xam.Plugin.SimpleStaticMap) - 只是一个基于 Google 地图静态 API 的简单静态地图控件，适用于您的 Xamarin Forms 项目
- [TEdito2](https://github.com/bulubuloa/TEditor2) - TEditor2 是 Xamarin 的 HTML 编辑器，它具有许多内置功能并且易于使用。
- [IridescentView](https://github.com/alexandrehtrb/IridescentView) - 具有虹彩效果的自定义 Xamarin.Android ImageView。


## 穿戴式

- [WormHoleSharp ★25](https://github.com/Clancey/WormHoleSharp) - Watch 和 iDevice 之间的通信。


## Xamarin.Forms

- [Acr-xamarin-forms ★244](https://github.com/aritchie/acr-xamarin-forms) - 相机/图库、条形码扫描、用户对话框、地理位置、网络实用程序、设备信息、设置、电子邮件、电话、短信全部适用于 Xamarin.Forms。
- [AdvancedTimer ★35](https://github.com/ufuf/AdvancedTimer) - Timer 对象及其方法的实现是为了扩展对计时器的支持。
- [Android AppCompat ★34](https://github.com/nativecode-dev/oss-xamarin) - 现在为 Xamarin.Forms 应用程序原生提供 Material Design 主题，无需破解。
- [BadgeView ★31](https://github.com/SuavePirate/BadgeView) - 一个简单的 Xamarin.Forms 控件，用于显示圆形徽章。
- [Circle Image Control](https://github.com/jamesmontemagno/ImageCirclePlugin) - 在 Xamarin.Forms 项目中显示圆形图像的简单而优雅的方式。
- [Compass ★19](https://github.com/JarleySoft/CompassPlugin) - 提供从 Xamarin.Forms 项目访问 Windows Phone、iOS 和 Android 上的指南针的简单方法。
- [Device Orientation ★28](https://github.com/wcoder/Xamarin.Plugin.DeviceOrientation) - 简单的跨平台插件，可与移动设备的屏幕方向配合使用。
- [Device Orientation ★1](https://github.com/aliozgur/Xamarin.Plugins/tree/master/DeviceOrientation) - 获取设备方向或收到 Xamarin.Forms 项目中的方向更改通知的简单方法。
- [NControl ★243](https://github.com/chrfalch/NControl) - NGraphics 的 Xamarin.Forms 控件。
- [Magic Gradients ★128](https://github.com/mgierlasinski/MagicGradients) - 提供了一种在 Xamarin.Forms 中实现各种渐变的简单方法。
- [MvxForms ★8](https://github.com/MobiliTips/MvxPlugins) - 用于使用 Xamarin.Forms 的 MVVMCross 插件。
- [PancakeView ★454](https://github.com/sthewissen/Xamarin.Forms.PancakeView) - Xamarin.Forms 的扩展 ContentView，具有圆角、边框、阴影、渐变等。
- [PullToRefreshLayout ★134](https://github.com/jamesmontemagno/Xamarin.Forms-PullToRefreshLayout) - [已弃用] 拉动以刷新 Xamarin.Forms 中的 ScrollView 或 ListView。
- [Rb.Forms.Barcode ★34](https://github.com/rebuy-de/rb-forms-barcode) - 用于扫描条形码的 Xamarin.Forms 视图。
- [Rg.Plugins.Popup](https://github.com/rotorgames/Rg.Plugins.Popup) - Xamarin.Forms 的跨平台插件，允许以弹出窗口的形式打开 Xamarin.Forms 页面。
- [SharedTransitions ★223](https://github.com/GiampaoloGabba/Xamarin.Plugin.SharedTransitions) - Xamarin.Forms (IOS/Android) 中页面之间的共享元素转换。
- [Sharpnado.Presentation.Forms ★28](https://github.com/roubachof/Sharpnado.Presentation.Forms) - Horizo​​ntalListView、TaskViewLoader 和分页器。
- [SolTech Xamarin Forms Toolkit ★31](https://github.com/soltechinc/soltechxf) - Xamarin Forms 框架的一组有用扩展。
- [Store Rating Plugin ★7](https://github.com/voxdev/Xamarin.Plugins) - 评价应用程序弹出窗口。
- [SVG ★1](https://github.com/paulpatarinski/Xamarin.Forms.Plugins/tree/master/SVG) - SVG 文件格式支持。
- [Swipecards ★80](https://github.com/robinmanuelthiel/swipecards) - Xamarin.Forms 的类似于 Tinder 的滑动控件。
- [Toasts Plugin ★208](https://github.com/EgorBo/Toasts.Forms.Plugin) - 在 Xamarin.Forms 应用程序中显示一些通知的简单方法。
- [TwinTechsFormsLib ★187](https://github.com/twintechs/TwinTechsFormsLib) - FastCell、FastImage、FastGridCell。
- [XamarinControls ★17](https://github.com/Intelliabb/XamarinControls) - Xamarin 和 Xamarin.Forms 的跨平台控件（使用 SkiaSharp 的复选框）。
- [Xamarin-Forms-Labs ★1,392](https://github.com/XLabs/Xamarin-Forms-Labs) - 强大的跨平台控件和助手集。
- [xamarin-forms-xna ★7](https://github.com/jvlppm/xamarin-forms-xna) - Xamarin.Forms 的 Monogame 包装器。
- [Xamarin.Forms.GoogleMaps ★250](https://github.com/amay077/Xamarin.Forms.GoogleMaps) - 使用 Google Mapps API 的 Xamarin.Forms 地图库。
- [XamFormsMvxTemplate ★19](https://github.com/JTOne123/XamFormsMvxTemplate) - MVVMCross.Forms Visual Studio 2017 项目模板（iOS、Android、UWP）。
- [Xamarin.Essentials](https://docs.microsoft.com/en-us/xamarin/essentials/) - Xamarin.Essentials 为开发人员的移动应用程序提供跨平台 API。
- [Xamarin.Forms.EntryAutoComplete](https://github.com/krzysztofstepnikowski/Xamarin.Forms.EntryAutoComplete) - 自定义控制哪些功能可以在打字时为您提供建议。建议有多种模式。建议的文本可以显示在下拉列表中，以便您可以从不同的选项中进行选择。
- [Xamarin.Forms.Skeleton](https://github.com/HorusSoftwareUY/Xamarin.Forms.Skeleton) - Xamarin Forms 应用中加载方法的最新趋势。可以在 Xaml 中包含的每个视图上轻松实现骨架。
- [MaterialDesignControlsPlugin](https://github.com/HorusSoftwareUY/MaterialDesignControlsPlugin) - Xamarin Forms 的 MaterialDesignControls 插件是应用材料设计指南的 Xamarin.Forms 控件的集合。

## XPlat API

大多数支持 Android 和 iOS，部分支持 Windows Phone 8

- [Calendars ★49](https://github.com/TheAlmightyBob/Calendars) - 适用于 Xamarin 和 Windows Phone 的日历 API 插件，支持日历和事件的基本 CRUD 操作。
- [Device Motion ★1](https://github.com/rdelrosario/xamarin-plugins/tree/master/DeviceMotion) - 简单的跨平台插件，用于读取设备运动传感器的运动矢量值，例如：加速度计、陀螺仪、磁力计、指南针。
- [Estimote ★37](https://github.com/aritchie/estimotes-xplat) - 信标估计库的跨平台实现。
- [Fingerprint ★165](https://github.com/smstuebe/xamarin-fingerprint) - 用于访问指纹传感器的 Xamarin 和 MvvMCross 插件。
- [HybridKit ★21](https://github.com/chkn/HybridKit) - Simple C# – 用于构建混合 iOS 和 Android 应用程序的 JavaScript 桥。
- [Lamp ★1](https://github.com/kphillpotts/Xamarin.Plugins/tree/master/Lamp) - 通过 Xamarin 和 Xamarin.Forms 项目控制手机背面的灯/LED 的简单方法。
- [ManageSleep ★15](https://github.com/molinch/Xam.Plugins.ManageSleep) - 管理所有平台中的自动睡眠/自动锁定。这在处理长时间运行的进程时非常有用。
- [Messaging ★88](https://github.com/cjlotz/Xamarin.Plugins) - 消息插件可以使用不同移动平台上的默认消息应用程序拨打电话、发送短信或发送电子邮件。
- [Notifications ★79](https://github.com/aritchie/notifications) - 适用于 Xamarin 和 Windows 的通知插件。
- [Pontoon ★27](https://github.com/inthehand/Pontoon) - 通向通用 Windows 平台的灵活桥梁。
- [Shiny ★428](https://github.com/shinyorg/shiny) - 用于后台和设备硬件服务的 Xamarin 框架。
- [Telephony ★17](https://github.com/ghuntley/telephony) - 电子邮件、短信、语音和视频通话功能。
- [userdialogs ★510](https://github.com/aritchie/userdialogs) - 来自共享/可移植库的标准用户对话框。
- [Version ★1](https://github.com/mtrinder/Xamarin.Plugins/tree/master/Version) - 从捆绑包中获取应用程序版本。
- [Xamarin.Badge ★33](https://github.com/B1naryStudio/Xamarin.Badge) - 简单的跨平台插件，可与应用程序徽章一起使用。
- [Xamarin.Essentials ★560](https://github.com/xamarin/Essentials) - Xamarin 团队提供适用于 iOS 和 Android 的基本跨平台 API。提供轻松访问或使用：加速度计、应用程序信息、电池、剪贴板、指南针、连接、数据传输（共享）、设备显示信息、设备信息、电子邮件、文件系统助手、手电筒、地理编码、地理定位、陀螺仪、磁力计、打开浏览器、方向传感器、电源、电话拨号器、首选项、屏幕锁定、安全存储、短信、文本转语音、版本跟踪、振动。
- [Xamarin.LocalNotifications ★40](https://github.com/B1naryStudio/Xamarin.LocalNotifications) - 简单的跨平台插件，可处理移动本地通知。
- [Xamarin.Mobile ★237](https://github.com/xamarin/Xamarin.Mobile) - 读取用户的地址簿并使用相机。
- [Xamarin-plugins ★39](https://github.com/domaven/xamarin-plugins) - 设备运动、地理围栏、推送通知（测试版）。


## 其他清单

- [Awesome Xamarin Bookmarks ★9](https://github.com/wcoder/awesome-xamarin-bookmarks) - 为 Xamarin 开发人员精心挑选的有趣（必须有）链接的书签。
- [Open Source Xamarin Apps ★11](https://github.com/wcoder/open-source-xamarin-apps) - 开源 Xamarin 应用程序列表。
- [Xamarin Bindings ★112](https://github.com/aloisdeniel/Xamarin.Bindings) - 现有库绑定的列表。
- [Xamarin Components ★1,338](https://github.com/xamarin/XamarinComponents) - 在这里，您将找到 Xamarin 的跨平台插件列表，这些插件通过单个 API 支持 Xamarin.iOS、Xamarin.Android、Xamarin.Forms 和 Windows 平台。
- [Xamarin Universal Library ★3](https://github.com/xamarinuniverse/XamarinUniversalLibrary/) - 这是一个通用库，包含我们需要了解的有关 Xamarin 宇宙的所有信息。


## 网站

- [Planet Xamarin](https://www.planetxamarin.com) - 来自 Xamarin 社区成员的内容聚合器。当您可以订阅一个方便的 RSS 源时，为什么还要单独订阅呢？如果您不喜欢 RSS，请关注 [Twitter](https://twitter.com/PlanetXamarin) 或 [Facebook](https://www.facebook.com/login/?next=https%3A%2F%2Fwww.facebook.com%2Fplanetxamarin%2F) 帐户，这些帐户会自动更新为社区的最新内容。
- [Programming Community Curated Resources For Learning Xamarin](https://hackr.io/tutorials/learn-xamarin) - 用于学习 Xamarin 的精选资源列表。
- [Weekly Xamarin](https://weeklyxamarin.com/) - 每周精心挑选的最佳 Xamarin 开发链接。由杰弗里·亨特利策划，每周五出版。自由的。
- [Xamarin Online Courses](https://classpert.com/search/xamarin) - Classpert 在线课程搜索中包含 60 多个在线课程（免费和付费）的列表。


## 许可证

请参阅[许可证]（许可证）
