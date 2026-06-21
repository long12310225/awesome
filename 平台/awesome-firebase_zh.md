<!-- badges -->
<div align="center">

<!-- title -->
<!--lint ignore no-dead-urls-->
# Awesome Firebase [![Awesome](https://awesome.re/badge.svg)](https://awesome.re) ![Lint Awesome List](https://github.com/jthegedus/awesome-firebase/workflows/lint/badge.svg)

<!-- subtitle -->

The most **up to date** list of Firebase docs, talks, tools, examples & articles the internet has to offer.

<!-- image -->

<a href="https://firebase.google.com/docs/" target="_blank" rel="noopener noreferrer">
  <img src="images/firebase-services.gif" />
</a>

<!-- translations -->

翻译: [🇬🇧 en](readme.md) · [🇰🇷 ko](readme-ko.md) · [🇷🇺 ru](readme-ru.md) <!-- · [🇪🇸 es](readme-es.md) · [🇮🇩 id](readme-id.md) · [🇯🇵 ja](readme-ja.md) · [🇵🇹 pt](readme-pt.md) · [🇨🇳 zh](readme-zh.md) -->

[Firebase](https://firebase.google.com) 是一个基于 [Google Cloud Platform](https://cloud.google.com/products) 构建的应用开发平台，提供服务和跨平台 SDK！

</div>

<!-- toc -->

## 内容

- [精选（新发布）](#featured-new-releases)
- [官方文档和快速入门](#official-docs--quickstarts)
- [Firebase 扩展](#firebase-extensions)
- [Web](#web)
- [Mobile](#mobile)
- [Games](#games)
- [服务器端（云函数、BigQuery 等）](#server-side-cloud-functions-bigquery-etc)
- [CLI 和编辑器](#cli--editor)
- [Other](#other)
- [Follow](#follow)

**图例**：📝博客文章·💡示例·📖文档·🔌库·🔧工具·📹演讲/视频·🔊播客

<!-- START content -->

## 精选（新发布）

- 🔧 [（非官方）适用于 PHP 的 Firebase Admin SDK](https://github.com/kreait/firebase-php) - Firebase Admin PHP SDK 支持从 PHP 中的特权环境（例如服务器或云）访问 Firebase 服务。
- 📖 [App Check](https://firebase.google.com/docs/app-check) - 保护您的后端资源免遭滥用，例如计费欺诈或网络钓鱼。
- 📖 [Firestore 数据包](https://firebase.google.com/docs/firestore/bundles) - 数据包是 CDN 缓存的静态查询结果，可加快首页加载速度。
- 📖 [模块化 Web SDK (v9)](https://firebase.google.com/docs/web/learn-more#modular-version) - 仅导入您需要的内容，将 SDK 大小最多减少 80%。

## 官方文档和快速入门

- 📖 [Firebase 文档](https://firebase.google.com/docs) - Firebase 官方文档。
- 🔧 [Firebase 状态仪表板](https://status.firebase.google.com) - 此页面提供有关 Firebase 一部分的服务的状态信息。
- 💡 [Firebase 快速入门](https://github.com/firebase?utf8=%E2%9C%93&q=quickstart&type=&language=) - 官方 Firebase 快速入门。
- 💡 [谷歌代码实验室 | Firebase](https://codelabs.developers.google.com/?cat=Firebase) - Google 开发人员 Codelab 提供指导性教程、实践编码体验。
- 📖 [Firebase for Games](https://firebase.google.com/games) - 新的 Firebase for Games 登陆页面，其中包含面向游戏开发者的 Firebase/Google 资源的链接。

## Firebase 扩展

- 🔧 [Firebase 扩展](https://firebase.google.com/products/extensions) - Firebase 扩展为您的应用提供扩展功能，无需您自己研究、编写或调试代码。
- 🔧 [Experimental Firebase Extensions](https://github.com/FirebaseExtended/experimental-extensions) - Firebase 创建的新扩展的实验室。
- 🔧 [Stripe 扩展](https://github.com/stripe/stripe-firebase-extensions) - 官方 Stripe 订阅和发票扩展。
- 🔧 [MessageBird Extensions](https://github.com/messagebird/firestore-send-msg) - 官方 MessageBird 扩展，用于通过 MessageBird Conversations API 发送消息。
- 🔧 [Algolia 扩展](https://github.com/algolia/firestore-algolia-search) - 官方 Algolia 扩展，可使用 Algolia 对 Cloud Firestore 进行全文搜索。
- 🔧 [Mailchimp 扩展](https://github.com/mailchimp/Firebase) - 官方 Mailchimp 扩展，用于同步 Firebase 身份验证事件，以使用 Mailchimp 创建成员标签、合并字段和成员事件。
- 🔧 [用于全文搜索的 Typesense 扩展](https://github.com/typesense/firestore-typesense-search) - 官方 Typesense 扩展，通过将数据同步到 [Typesense](https://github.com/typesense/typesense)（Algolia 的 OSS 替代品）在 Firestore 中添加全文搜索。

## 网络

- 🔌 [Firestore Lite](https://github.com/samuelgozi/firebase-firestore-lite) - 适用于浏览器的轻量级 Cloud Firestore 库。
- 🔌 [SvelteFire](https://github.com/codediodeio/sveltefire) - 控制论增强的 Firebase 应用程序。
- 🔌 [React Fire](https://github.com/FirebaseExtended/reactfire) - 官方 Firebase React 库，带有 Hooks、上下文提供程序和组件，可以轻松与 Firebase 交互。
- 🔧 [带有远程配置的远程样式](https://github.com/firebaseextended/remote-styles/) - 动态/条件加载存储在远程配置中的 CSS。 （[发布帖子](https://medium.com/firebase-developers/introducing-remote-styles-conditional-css-loading-made-easy-daddbbcce050)）。
- 🔌 [React Firebase Hooks](https://github.com/CSFrequency/react-firebase-hooks) - 用于 Firebase 服务的 React Hooks。
- 🔌 [Firebase UI](https://github.com/firebase/firebaseui-web) - FirebaseUI 是一个面向 Web 的开源 JavaScript 库，它在 Firebase SDK 之上提供简单、可自定义的 UI 绑定，以消除样板代码并推广最佳实践。
- 🔌 [React 的 Firebase UI](https://github.com/firebase/firebaseui-web-react) - firebaseUI Web 的 React 包装器。
- 🔌 [GeoFire for JavaScript](https://github.com/firebase/geofire-js) - 使用 Firebase 进行实时位置查询。
- 💡 [FirePad](https://github.com/FirebaseExtended/firepad) - 由 Firebase 提供支持的协作文本编辑器。
- 🔌 [Ember Fire](https://github.com/firebase/emberFire) - Firebase 的官方 Ember 数据适配器。
- 🔌 [Firebase Dart](https://github.com/FirebaseExtended/firebase-dart) - Firebase 的 Dart 包装器。
- 🔌 [PolymerFire](https://github.com/FirebaseExtended/polymerfire) - Firebase 的聚合物 Web 组件。
- 🔌 [VueFire](https://github.com/vuejs/vuefire) - Vue.js 的 Firebase 绑定。
- 🔌 [Angular Fire 2](https://github.com/angular/angularfire2) - Firebase 和 Angular 的官方库。
- 🔌 [Re-base](https://github.com/tylermcginnis/re-base) - 用于构建 React.js + Firebase 应用程序的 Relay 启发库。
- 🔌 [React Redux Firebase](https://github.com/prescottprue/react-redux-firebase) - Firebase 的 Redux 绑定。包括与 React 一起使用的高阶组件。
- 🔌 [GatsbyJS Firebase 数据源](https://www.gatsbyjs.org/packages/) - 使用 Gatsby 直接在静态生成的页面中查询 Firebase 数据。
- 🔌 [Apollo Link Firebase](https://github.com/Canner/apollo-link-firebase) - 为 RealtimeDB 提供本地 GraphQL 接口。数据库本地同步到设备，Apollo Link 提供对本地数据库的查询。
- 🔌 [Firebase 的 BuckleScript 绑定](https://github.com/avohq/bs-firebase) - Firebase 的 BuckleScript 绑定，用于 ReasonML 项目。
- 💡 [Angular Firebase PWA](https://github.com/codediodeio/angular-firestarter) - 是由 Firebase 提供支持的 Angular PWA。它可以作为学习该堆栈并推出更复杂功能的基础。
- 🔌 [FireSQL](https://github.com/jsayol/FireSQL) - 使用 SQL 语法查询 Firestore。发出获取您请求的数据所需的最少量的查询。
- 📖 [托管版本历史记录](https://firebase.google.com/docs/hosting/deploying#set_limit_for_retained_versions) - 自动删除站点部署的旧版本。
- 🔌 [Firestorter](https://github.com/IjzerenHein/firestorter) - 使用 MobX（也适用于 React-native）在 ​​React 中零费力地使用 Firestore。
- 💡 [Nextbase](https://github.com/martyan/nextbase) - Next.js、Redux 和 Firebase 的样板，适合想要快速启动项目的开发人员。
- 🔧 [Typesaurus](https://github.com/kossnocorp/typesaurus) - Firestore 的类型安全 TypeScript 优先 ODM。
- 🔌 [firebase-kotlin-sdk](https://github.com/GitLiveApp/firebase-kotlin-sdk/) - Kotlin-first SDK for Firebase 支持多平台项目（`ios`、`android` 和 `js`）。
- 🔌 [GeoFirestore](https://github.com/MichaelSolati/geofirestore-js) - 使用 Firebase Firestore 进行基于位置的查询和过滤。
- 🔧 [FirelordJS](https://github.com/tylim88/FirelordJS) - Firestore Web 的超高精度 Typescript 包装器。 ([管理员版本](https://github.com/tylim88/Firelord))
- 🔧 [FireSageJS](https://github.com/tylim88/FireSageJS) - 对于实时数据库 Web 来说极端类型安全。

## 手机

- 📝 [App Distribution App Bundles](https://firebase.googleblog.com/2021/05/app-distribution-adds-support-to-android-app-bundles.html) - App Distribution 正式支持 Android App Bundles (AAB)。
- 📖 [Firebase Flutter 文档](https://firebase.google.com/docs/flutter/setup) - 官方 Firebase Flutter 设置。
- 🔌 [NativeScript 插件 Firebase](https://github.com/EddyVerbruggen/nativescript-plugin-firebase) - Firebase 的 NativeScript 插件。
- 🔌 [FlutterFire](https://github.com/FirebaseExtended/flutterfire) - [Flutter](https://flutter.io/) 应用程序的 Firebase 插件集合。
- 🔌 [React Native Firebase](https://github.com/invertase/react-native-firebase) - 经过充分测试、功能丰富的 React Native 模块化 Firebase 实现。支持 iOS 和 Android 平台。
- 🔌 [React Native Firebase 云消息传递](https://github.com/evollu/react-native-fcm) -
用于 Firebase 云消息传递和本地通知的 React Native 模块。
- 💡 [Expo Native Firebase](https://github.com/EvanBacon/expo-native-firebase) - 用于 Firestore、通知、分析、存储、消息传递、数据库的本机 Firebase Expo 应用程序（iOS、Android）演示。
- 💡 [Flutter 日历应用程序](https://github.com/mattgraham1/FlutterCalendar) -
新的 Flutter 应用程序实现了一个简单的移动日历应用程序，用于将基本事件存储到 Firebase 云数据库中。
- 🔧 [Firebase 应用程序分发](https://firebase.google.com/products/app-distribution/) - 将应用程序的预发布版本分发给值得信赖的测试人员。
- 🔌 [Flamingo](https://github.com/hukusuke1007/flamingo) - Dart 的 Firebase Firestore 模型框架。

### 安卓

- 🔌 [GeoFire for Java](https://github.com/firebase/geofire-java) - 使用 Firebase 进行实时位置查询。
- 🔌 [Firebase UI](https://github.com/firebase/firebaseui-android) - 针对 Firebase 优化的 UI 组件。
- 🔌 [FireXtensions](https://github.com/rosariopfernandes/firextensions) - Firebase Android SDK 的非官方 Kotlin 扩展。
- 🔌 [Firecoil](https://github.com/rosariopfernandes/firecoil) - 使用图像加载库 Coil 从 Android 应用程序中的 GCS 加载图像。

### iOS系统

- 🔌 [GeoFire for Objective-C](https://github.com/firebase/geofire-objc) - 使用 Firebase 进行实时位置查询。
- 🔌 [Firebase UI](https://github.com/firebase/firebaseui-ios) - Firebase 的 iOS UI 绑定。
- 💡 [MLKit - ARCore](https://github.com/FirebaseExtended/MLKit-ARCore) - 检测对象并在增强现实中用 3D 标签标记它们的示例。使用 Firebase ML Kit、ARCore 和 Firebase RTDB。
- 💡 [MLKit - ARKit](https://github.com/FirebaseExtended/MLKit-ARKit) - 使用 Firebase ML Kit 检测对象并在增强现实中用 3D 标签标记它们的示例。

## 游戏

- 📖 [适用于 C++ 和 Unity 的 Firestore](https://firebase.google.com/docs/firestore) - 适用于 C++ 和 Unity 的 C++ 和 Unity SDK（通过 Unity Package Manager 提供 Firebase Unity SDK）。

## 服务器端（云函数、BigQuery 等）

- 📖 [Firebase 管理文档](https://firebase.google.com/docs/admin/setup) - 官方 Firebase 管理 SDK 服务器设置。
- 💡 [Functions Samples](https://github.com/firebase/functions-samples) - 示例应用程序集合，展示使用 Cloud Functions for Firebase 的流行用例。
- 💡 [Cloud Functions 上的 Express 服务器](https://github.com/jthegedus/firebase-gcp-examples/tree/main/functions-express) - 在 Cloud Functions 上托管 Express 服务器。
- 📝 [Cloud Functions 上的 GraphQL Server](https://codeburst.io/graphql-server-on-cloud-functions-for-firebase-ae97441399c0) - 在 Cloud Functions 上托管带有 GraphQL 中间件的 Express 服务器。
- 💡 [使用 Cloud Functions 编译代码](https://github.com/jthegedus/firebase-gcp-examples/tree/main/functions-w-parcel) - 使用 Babel、TypeScript Compiler 或 ParcelJS 将 Flow、TypeScript 或 ReasonML 编译到正确的 Node 运行时。
- 📝 [BigQuery 和 Google Analytics](https://medium.com/firebase-developers/how-do-i-create-a-close-funnel-in-google-analytics-for-firebase-using-bigquery-6eb2645917e1) - 如何使用 BigQuery 在 Google Analytics for Firebase 中创建封闭漏斗。
<!--lint ignore double-link-->
- 📹 [官方云函数 #Firecasts](https://www.youtube.com/watch?v=2mjfI0FYP7Y&list=PLl-K7zZEsYLm9A9rcHb1IkyQUu6QwbjdM) - 有关了解云函数如何工作的 YouTube 视频系列。
- 📝 [Firebase Hosting for Cloud Run Services](https://firebase.googleblog.com/2019/04/firebase-hosting-and-cloud-run.html) - 具有托管重写和 Cloud Run 服务的动态内容。
- 📝 [Firebase 的计划 (Cron) 云函数](https://firebase.googleblog.com/2019/04/schedule-cloud-functions-firebase-cron.html) - Firebase 云函数的 Firebase 原生 Cron 触发器。
- 🔌 [Integrify](https://github.com/anishkny/integrify) - 使用预装的 Cloud Functions 触发器在 Firestore 中强制执行引用和数据完整性。
- 🔌 [使用 Firebase + BigQuery + Rakam 进行免费产品分析](https://rakam.io/blog/free-product-analytics-with-firebase---bigquery---rakam/) - 如何通过 BigQuery Export 和 Rakam 对 Firebase 事件数据进行行为和细分分析。
- 🔌 [Firestore 队列系统](https://github.com/sbarbat/firestore-queuer) - 使用 Firestore 和 Cloud Functions 的简单队列系统。
- 🔌 [Pyrebase](https://github.com/thisbejim/Pyrebase) - Firebase API 的简单 python 包装器。
- 🔌 [Firecode](https://github.com/kafkas/firecode) - 用于 Firestore 和 Node.js 的轻量、快速且内存高效的集合遍历库。

## CLI 和编辑器

- 📖 [Firebase 工具 UI](https://github.com/firebase/firebase-tools-ui) - Firebase 模拟器套件的 Web UI。
- 📖 [模拟器套件中的存储](https://firebase.google.com/docs/emulator-suite/connect_storage) - 模拟器套件现已完成！
- 🔧 [VSCode Firebase Explorer](https://github.com/jsayol/vscode-firebase-explorer) - 探索和管理您的 Firebase 项目。
- 🔧 [Firebase 工具](https://github.com/firebase/firebase-tools) - Firebase 命令行工具。
- 🔧 [Firebase CI](https://github.com/prescottprue/firebase-ci) - 简化 Firebase 交互以实现持续集成。
- 🔧 [Firecode](https://github.com/ChFlick/firecode) - VS Code Firestore 规则扩展。
- 🔧 [Firebase Firestore Snippets](https://github.com/peterhdd/firebase-firestore-snippets) - 包含 VS Code 编辑器中 Firebase 和 Firestore 的代码片段。
- 🔧 [Fuego](https://github.com/sgarciac/fuego) - Firestore 客户端 CLI 支持文档添加/更新/查询，并具有过滤和分页功能。
- 🔧 [Firestore 规则生成器](https://github.com/FirebaseExtended/protobuf-rules-gen) - 基于 Google 的 Protocol Buffer 格式的 Cloud Firestore 官方（但实验性）Firebase 规则生成器。
- 🔧 [Firepit](https://github.com/abehaskins/firepit) - Firepit 是 Firebase CLI 的独立便携式版本，没有依赖项（包括 Node.js）。
- 🔧 [Fireward](https://github.com/bijoutrouvaille/fireward) - Firestore 规则的易于使用的语言，类似于 Firebase Bolt。
- 🔧 [Svarog](https://github.com/dantothefuture/svarog) - 使用 JSON 架构生成的安全规则辅助函数进行 Cloud Firestore 架构验证。
- 🔧 [Firetable](https://github.com/AntlerVC/firetable) - Excel/Google Sheets，例如 Firebase/Firestore 的 UI。不再有管理门户！
- 🔧 [VSFire](https://github.com/toba/vsfire) - 已弃用 ~VSCode 扩展，用于使用 Firestore 安全规则和索引进行语法突出显示和代码补全。~
- 📝 [Refi App](https://refiapp.io/) - 一个 GUI 工具，可以让开发人员在与 Firestore DB 交互时减轻痛苦
- 🔧 [Firefoo](https://firefoo.app) - 具有 JSON/CSV 导出和 JavaScript 查询外壳的 Cloud Firestore GUI 管理工具。
- 🔧 [asdf-firebase](https://github.com/jthegedus/asdf-firebase) - `firebase-tools` 的 [asdf-vm](https://asdf-vm.com/) 插件。无需 Node.js 或“npm”即可管理您的 Firebase CLI！非常适合“python”、“golang”、“c++”和“java” Firebase 项目。

## 其他

- 🔧 [FireCMS](https://firecms.co/docs/) - FireCMS 是一个开源无头 CMS 和管理面板，由开发人员为开发人员构建。它根据您的配置生成 CRUD 视图。
- 🔧 [Flank](https://github.com/flank/flank/) - Firebase 测试实验室的大规模并行 Android 和 iOS 测试运行器。
- 🔌 [Firestore 查询浏览器](https://firestore-query-browser.firebaseapp.com) - 通过应用程序和用户切换进行查询、（批量）编辑和导出文档的 Web 应用程序。
- 🔌 [FireDrill](https://github.com/scottlepp/fire-drill) - 查找、编辑、添加、删除、导入、导出和报告您的 Firebase 数据。
- 💡 [Unity 解决方案](https://github.com/FirebaseExtended/unity-solutions) - 使用 Firebase 工具将常用功能合并到您的游戏中。
- 🔌 [Firebase AIR Native Extension](https://github.com/myflashlab/Firebase-ANE) - Firebase ANE 集合让您可以访问 Android 和 iOS 上支持的 Adob​​eAir 项目中的 Google Firebase 项目，并具有 100% 相同的 ActionScript API。
- 🔌 [QtFirebase](https://github.com/Larpon/QtFirebase) - 将 Google 的 Firebase C++ API 引入 Qt + QML 的努力。
- 📝 [StackBlitz 到 Firebase 托管部署](https://medium.com/@ericsimons/announcing-split-second-static-deploys-for-firebase-7440d8e84879) - StackBlitz（在线代码编辑器）到 Firebase 托管静态部署。
- 🔧 [Flamelink](https://flamelink.io/) - Firebase 的 CMS。支持 Firestore、实时数据库和存储。
- 📹 [Firebase 峰会 2018](https://www.youtube.com/watch?v=lN0VXVXsj9k&list=PLl-K7zZEsYLnqdlmz7iFe9Lb6cRU3Nv4R) - 所有 Firebase 峰会 2018 演讲。
- 📹 [Firebase @ Google Cloud Next '18](https://www.youtube.com/watch?v=OPj26MY16F8&list=PLl-K7zZEsYLmYx3MkJRIUPH_JVFHLTlwL) - 所有 Firebase 演讲 @ Google Cloud Next 2018。
- 📹 [Firebase @ Google IO '18](https://www.youtube.com/watch?v=e-8fiv-vteQ&list=PLl-K7zZEsYLn1omgx_VUhCDFsQMA7PRDd) - 所有 Firebase 演讲 @ Google IO 2018。
- 📹 [#AskFirebase YouTube 播放列表](https://www.youtube.com/watch?v=TSzhzR4wzSE&list=PLl-K7zZEsYLkkCFs6T9mlqG8v6NCs38pA) - YouTube 上的官方 #AskFirebase 播放列表。
- 📝 [Firebase 状态（2019 年中）](https://codeburst.io/the-state-of-firebase-mid-2019-2b002c458d70) - Cloud Next 和 Google I/O 2019 更新！
- 📹 [Firebase @ Google IO '19](https://www.youtube.com/playlist?list=PLl-K7zZEsYLlo2L4rfPds-fFLEtOWheoO) - 所有 Firebase 演讲 @ Google IO 2019。
- 📹 [Firebase 峰会 2019](https://www.youtube.com/watch?v=YKZ6rP4kwV8&list=PLl-K7zZEsYLk2OolaVXVyYrFErctrZXSX) - 所有 Firebase 演讲均@ Firebase 峰会 2019。
- 📹 [Firebase Live 2020](https://www.youtube.com/playlist?list=PLl-K7zZEsYLnw0-bXz2f9zo6745VQ_2ep) - Firebase Live 是一个面向应用开发者的网络系列，其中包括旨在提高他们的工作效率、知识和协作的讲座、技巧和技术教程。
- 📹 [Firebase 峰会 2020](https://goo.gle/firebasesummit2020) - 所有 Firebase 演讲均@ Firebase 峰会 2020。
- 🔧 [Dynaboard](https://dynaboard.com) - 使用 AI 从 Firebase 生成低代码 Web 应用程序。

<!-- END content -->

## 关注

### 官方

- 📹 [Firebase YouTube](https://www.youtube.com/user/Firebase)
- 📝 [Firebase 博客](https://firebase.googleblog.com/)
- 🐦 [@firebase](https://twitter.com/firebase)
- 👤 [Firebase Facebook](https://www.facebook.com/Firebase)
- 🔊 [Firebase 播客](https://podcasts.google.com/feed/aHR0cDovL2ZpcmViYXNlcG9kY2FzdC5nb29nbGVkZXZlbG9wZXJzLmxpYnN5bnByby5jb20vcnNz) - 在这里，我们深入了解 Firebase 产品并学习新的提示和技巧方式。

### 社区

- :fire: [Firebase Developers Discord](https://discord.gg/BN2cgc3) - 一个致力于 Firebase 及其服务的开放社区，您可以在其中进行社交并帮助来自世界各地的其他 Web 和应用程序开发人员。
- 📹 [Fireship](https://www.youtube.com/channel/UCsBjURrPoezykLs9EqgamOA) - 由 Jeff Delaney 制作的 YouTube 频道，Jeff Delaney 是 Google Firebase 专家，也是著名的“100 秒内的 X”视频的创作者。
- 📹 ru [@firebase_ru - Telegram 友好聊天](https://t.me/firebase_ru)

我们还应该关注谁！？

## 贡献

[欢迎任何形式的贡献，只需遵循指南](contributing.md)！

### 贡献者

[感谢这些贡献者](https://github.com/jthegedus/awesome-firebase/graphs/contributors)！
