真棒飞镖 [![真棒](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
============

精选的 Dart 框架、库和软件列表。列表中的项目在 Dart 社区中得到积极维护、记录良好且很受欢迎。受到 [awesome](https://github.com/sindresorhus/awesome) 列表的启发。

### 贡献

请先快速浏览一下[贡献指南](/CONTRIBUTING.md)。如果您在此处看到不再维护或不合适的包或项目，请提交拉取请求以改进此文件。感谢所有[贡献者](https://github.com/yissachar/awesome-dart/graphs/contributors)；你摇滚！

### 内容

* 图书馆
  * [客户端 Web 应用程序框架](#client-web-app-frameworks)
  * [服务器框架](#server-frameworks)
  * [游戏开发](#game-development)
  * [Animation](#animation)
  * [Template](#template)
  * [Database](#database)
  * [包管理器](#package-managers)
  * [Utilities](#utilities)
  * [依赖注入](#dependency-injection)
  * [Parsers](#parsers)
  * [Validation](#validation)
  * [ORM](#orm)
  * [Image](#image)
  * [Algorithms](#algorithms)
  * [Testing](#testing)
  * [Unions](#unions)
* [Tools](#tools)
* [IDE、编辑器和插件](#ides-editors-and-plugins)
* [Tutorials](#tutorials)
* [Community](#community)
* [其他一切](#everything-else)

----

## 客户端 Web 应用程序框架

* [AngularDart Community](https://github.com/angulardart-community) - 社区维护的 AngularDart 网站、软件包、工具等等！
* [Flutter](https://flutter.dev/) - Flutter 是一个用于构建高性能、跨平台移动应用程序的框架，允许为 Android、iOS 和 Web 应用程序编写应用程序。
* [MDL/Dart](http://mdl.mikemitterer.at//) - Material Design Lite for Dart 是一个基于 Google Material Design 理念的 Web 开发人员组件框架。
* [OverReact](https://workiva.github.io/over_react/) - 用于构建静态类型 React UI 组件的库。

## 服务器框架

* [Jaguar](https://github.com/Jaguar-dart/jaguar) - 专为速度、简单性和可扩展性而构建的服务器框架。
* [Start](https://github.com/lvivski/start) - Sinatra 启发了 Web 框架来提供静态文件、处理动态请求、Websockets 并创建 JSON 响应。
* [Shelf](https://pub.dartlang.org/packages/shelf) - Shelf 可以轻松创建和组合 Web 服务器以及 Web 服务器的一部分。
* 有很多为 Shelf 编写的包。按照惯例，它们以 [shelf_](https://pub.dartlang.org/search?q=shelf_) 开头。
* [Vane](https://github.com/Scorpiion/Vane) - 内置服务器运行环境和中间件系统的框架。
* [Rikulo Stream](https://github.com/rikulo/stream) - 具有请求路由、过滤、模板引擎、WebSocket、MVC 设计模式和基于文件的静态资源的轻量级 Web 服务器。
* [Alfred](https://github.com/rknell/alfred) - 受 ExpressJS 启发的最小服务器，带有路由和中间件。
* [Dart Frog](https://github.com/VeryGoodOpenSource/dart_frog) - 快速、简约的 Dart 后端框架。

## 网络框架

* [Jaspr](https://docs.page/schultek/jaspr) - Jaspr 是一个现代 Web 框架，用于在 Dart 中构建网站，支持客户端和服务器端渲染。

## 其他框架
* [Rapid Open Hardware Development (ROHD) Framework](https://github.com/intel/rohd) - 用于描述和验证硬件的框架。

## 跨平台开发
* [universal_io](https://github.com/terrier989/universal_io) - _dart:io_ 也适用于浏览器。
* [universal_html](https://github.com/terrier989/universal_html) - _dart:html_ 也适用于 VM/Flutter。

## 游戏开发

* [Flame](https://github.com/luanpotter/flame#readme) - 极简主义的 Flutter 游戏引擎。
* [StageXL](http://www.stagexl.org/) - StageXL 提供易于使用且完整的 API（基于 Flash API），用于令人印象深刻的 2D 内容，例如游戏和其他丰富的应用程序。
* [DartRocket](https://github.com/StrykerKKD/dartrocket) - DartRocket 是一个用 Dart 编写的 HTML5 游戏框架，它使用 StageXL 渲染引擎。
* [Pixi Dart](https://github.com/FedeOmoto/pixi) - pixi.js 渲染引擎的端口。
* [Ranger](https://github.com/wdevore/Ranger-Dart) - 一个以 HTML5 Canvas 和场景图为中心的游戏引擎。

## 动画

* [Universal Tween Engine](https://github.com/xaguzman/tween-engine-dart) - 由 Aurelien Ribbon 创建的原始 java 通用补间引擎的端口。
* [Spine Dart](https://github.com/FedeOmoto/spine) - Esoteric Software Spine 运行时的实现。

## 模板

* [mustache_template](https://pub.dev/packages/mustache_template) - 一个支持dart2js和dart2native的mustache模板库。
* [jaded](https://github.com/dartist/jaded) - 优秀的 Jade 视图引擎的端口。
* [mason](https://github.com/felangel/mason) - 允许开发人员创建和使用称为“bricks”的可重用模板的工具。

## 数据库

* [Postgres](https://github.com/stablekernel/postgresql-dart) - PostgreSQL 数据库驱动程序，使用扩展的二进制协议来实现更高效、更安全的查询。
* [SQLJockey](https://github.com/jamesots/sqljocky) - MySQL 连接器。
* [PostgreSQL](https://github.com/xxgreg/dart_postgresql) - PostgreSQL 数据库驱动程序。

## 包管理器

* [Pub](https://pub.dartlang.org/) - Pub用于管理包。
* [Cloudsmith](https://cloudsmith.io/l/dart-repository/) - 完全托管的包管理 SaaS，支持 Dart、Flutter 等。 **[免费供公众/OSS]** **[$]**

## 公用事业

* [Archive](https://pub.dartlang.org/packages/archive) - 用于编码和解码各种存档和压缩格式的库。
* [built_collection](https://github.com/google/built_collection.dart) - 通过构建器模式的不可变集合。
* [built_value](https://github.com/google/built_value.dart) - 不可变值类型、枚举类和序列化。
* [Frappe](https://pub.dartlang.org/packages/frappe) - Dart 的函数式反应式编程库。 Frappé 扩展了 Dart 流的功能，并引入了属性/信号等新概念。
* [Quiver](https://github.com/google/quiver-dart) - 一组实用程序库，使许多库的使用更加容易和方便，或添加附加功能。
* [route_hierarchical](https://github.com/angular/route.dart) - Route 是 Dart 的客户端路由库，可帮助构建单页 Web 应用程序。
* [Darq](https://pub.dev/packages/darq) - 来自 .NET 库的功能 LINQ 的端口。
* [Basics](https://github.com/google/dart-basics) - 一个 Dart 库，包含基本 Dart 对象的便捷扩展方法。

## 依赖注入

* [Angular DI](https://webdev.dartlang.org/angular/guide/dependency-injection) - Angular 的依赖注入框架。
* [Dependencies](https://github.com/marcguilera/dependencies.dart) - 一个简单且模块化的依赖注入系统，不使用镜像。
* [package: inject](https://github.com/google/inject.dart) - Dart 和 Flutter 的编译时依赖注入

## 解析器

* [html](https://pub.dartlang.org/packages/html) - 用于处理 HTML 文档的库。以前称为 html5lib。
* [markdown](https://github.com/dart-lang/markdown) - 在客户端和服务器上将 markdown 解析为 HTML。
* [PetitParser](https://github.com/petitparser/dart-petitparser) - PetitParser 结合了无扫描器解析、解析器组合器、解析表达式语法和 Packrat 解析器的思想，将语法和解析器建模为可以动态重新配置的对象。
* [XML](https://pub.dartlang.org/packages/xml) - 用于解析、遍历、查询和构建 XML 文档的轻量级库。
* [xmlstream](https://pub.dartlang.org/packages/xml) - 基于流事件的 XML 解析器。
* [YAML](https://pub.dartlang.org/packages/yaml) - YAML 的解析器。
* [Dart Tags](https://pub.dartlang.org/packages/dart_tags) - 用于解析 ID3 标签的库，用纯 Dart 编写。


## 验证

* [Constrain](https://pub.dartlang.org/packages/constrain) - 提供基于约束的验证库，其灵感来自 Java Bean Validation，但利用了 Dart 的卓越语言功能。
* [validator.dart](https://github.com/karan/validator.dart) - Dart 的字符串验证和清理。

## ORM

* [Objectory](https://github.com/vadimtsushko/objectory) - Objectory 提供类型化、检查的环境来建模、保存和查询 MongoDb 上持久的数据。

## 图片

* [image](https://github.com/brendan-duncan/image) - 为服务器和 Web 应用程序提供加载、操作和保存各种图像文件格式（包括 PNG、JPEG、GIF、WebP、TIFF、TGA、PSD、PVR 和 OpenEXR）图像的能力。

## 测试

* [Guinness](https://github.com/vsavkin/guinness) - Jasmine 图书馆的一个端口。
* [test](https://pub.dartlang.org/packages/test) - 提供在 Dart 中编写和运行测试的标准方法。
* [spec](https://pub.dev/packages/spec) - Dart 和 Flutter 的简化测试框架。

## 工会

* [Freezed](https://github.com/rrousselGit/freezed) - 不可变类的代码生成具有简单的语法/API，且不影响功能。

## 碰撞监控

* [Sentry](https://github.com/getsentry/sentry-dart) - Sentry 提供自托管和基于云的错误监控，帮助所有软件团队实时发现、分类和确定错误的优先级。

## 工具

* [DevTools](https://dart.dev/tools/dart-devtools) - 一套用于 Dart 和 Flutter 的调试和性能工具。
* [dart2js](https://www.dartlang.org/tools/dart2js/) - 将 Dart 代码编译为 JavaScript。
* [js2dart](https://github.com/vojtajina/js2dart) - 将 Javascript 代码编译为 Dart。
* [Stagehand](https://github.com/dart-lang/stagehand) - 项目脚手架生成器，受到 Web Starter Kit 和 Yeoman 等工具的启发。
* [Crossdart](https://crossdart.info) - 来自 Pub 的软件包的交叉引用源代码。
* [Crossdart Github Chrome Extension](https://chrome.google.com/webstore/detail/crossdart-chrome-extensio/jmdjoliiaibifkklhipgmnciiealomhd) - 向 Github 上的 Dart 项目添加“转到声明”和“查找用法”功能（在树视图和拉取请求中）。
* [gulp-dart](https://github.com/agudulin/gulp-dart) - 一个 gulp 插件，用于使用 dart2js 将 Dart 代码编译为 JavaScript。
* [dev_compiler](https://github.com/dart-lang/dev_compiler) - Dart to JavaScript 编译器旨在创建惯用的、可读的 JavaScript 输出。
* [json2dart](https://javiercbk.github.io/json_to_dart) - 给定一个 json，它会生成 dart 类来解析并生成具有给定结构的 json。
* [webdev_proxy](https://github.com/Workiva/webdev_proxy) - 围绕 [webdev](https://github.com/dart-lang/webdev) 的代理包装器，它添加了对将 404 重新路由到索引的支持，允许在本地运行时进行基于 HTML 推送的路由。
* [Dart Code Metrics](https://github.com/dart-code-checker/dart-code-metrics) - 附加的 linter 报告代码指标、检查反模式并为分析器提供附加规则。
* [m2cgen](https://github.com/BayesWitnesses/m2cgen) - 一个 CLI 工具，用于将经过训练的经典 ML 模型转换为零依赖的本机 Dart 代码。
* [Lakos](https://pub.dev/packages/lakos) - 在 Graphviz 中可视化内部库依赖关系并检测依赖循环。
* [FlutterTrends](https://fluttertrends.dev/) - pub.dev 上 20k 多个 Flutter 包的每日下载趋势、排名和存储库运行状况。

## 多线程

* [isolator](https://pub.dev/packages/isolator) - Isolator 为您提供了一种简单的方法来创建具有隔离部分和任何类型前端部分的双组件状态 - BLoC、MobX、ChangeNotifier 等

## 教程

* [Hello Dart](http://code.makery.ch/library/hello-dart/) - 对 Dart 的有趣介绍。
* [Dart 和 React 入门](https://www.leejamesrobinson.com/blog/getting-started-with-dart-and-react/)
* [Tour of Heroes](https://webdev.dartlang.org/angular/tutorial) - 一个涵盖 AngularDart 核心基础知识的应用程序。
* [Dart for beginner](https://www.myfreax.com/tag/dart/) - Dart 初学者中文教程。
* [Resolving Dart package version conflicts, faster than ever](https://iiro.dev/2018/08/28/resolving-dart-package-version-conflicts/) - 如何使用 pub 中的任意包版本来解决包版本冲突。

## 社区

* [Dartlang Reddit 子版块](https://www.reddit.com/r/dartlang/)
* [Gitter 聊天频道](https://gitter.im/dart-lang/home)
* [谷歌集团](https://groups.google.com/a/dartlang.org/d/forum/misc)
* [堆栈溢出](https://stackoverflow.com/tags/dart)
* [Facebook 群组 (pt-BR)](https://www.facebook.com/groups/dartlangbr)
* [电报聊天 (ru-RU)](https://t.me/rudart)
* [电报聊天 (id-ID)](https://t.me/dart_web)

## IDE、编辑器和插件

* [IntelliJ Plugin](https://www.dartlang.org/tools/webstorm/) - 来自 JetBrains 的 Dart 插件，适用于 WebStorm、IntelliJ IDEA、PhpStorm、PyCharm 和 RubyMine。
* [Sublime Text Package](https://github.com/guillermooo/dart-sublime-bundle) - Sublime Text 3 Dart 包。
* [Emacs Plugin](https://github.com/nex3/dart-mode) - Dart 语言的 Emacs 模式。
* [Vim Plugin](https://github.com/dart-lang/dart-vim-plugin) - Vim 中 Dart 的语法高亮显示。
* [Atom Plugin](https://atom.io/packages/atom-dart) - Dart 对 Atom 的支持。
* [VSCode Plugin](https://dartcode.org/) - Dart 对 Visual Studio Code 的支持。
* [DartPad](https://dartpad.dartlang.org/) - 在线轻量级编辑器。
* [Dart Code](https://marketplace.visualstudio.com/items?itemName=Dart-Code.dart-code) - Dart 对 Visual Studio Code 的支持。
* [Module Linker](http://fiatjaf.alhur.es/module-linker/#/dart) - Chrome 扩展添加了指向 GitHub 上模块导入语句的直接链接。
* [Dart Barrel File Generator](https://github.com/mikededo/dartBarrelFileGenerator) - VSCode 扩展，可为 Dart 项目生成桶文件。

## 其他一切

[Pub](https://pub.dartlang.org/) 一直在添加许多很棒的库。如果您在此列表中找不到满足您需求的库，请继续在 Pub 上搜索。如果您最终找到了一个很棒的库，我们希望您能提出包含该信息的拉取请求，以便其他人也可以发现它。请务必先阅读[贡献指南](https://github.com/yissachar/awesome-dart/blob/master/CONTRIBUTING.md)。

## 执照

[![CC0](https://i.creativecommons.org/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)
