# 令人敬畏的蒸汽 [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[<img src=“img/vapor-logo.png”align=“right”width=“150”>](https://vapor.codes)

[Vapor](https://vapor.codes) 是目前最流行的服务器端 Swift 框架之一。它允许您采用您曾经开发过 iOS 应用程序时已经了解的语言，并以全新的方式使用它，来开发快速、可扩展且可靠的后端系统，这些系统可以轻松地与各种第三方服务集成。这是一个精心策划的列表：

- 现代库可以轻松与 Vapor 集成，并遵循 Vapor 提供简单、干净但功能强大的 API 的理念；
- 精心编写的教程、书籍、视频和教育材料；
- 使您的开发过程更简单、更愉快的工具；
- 还有更多！

## 内容

- [如何使用](#how-to-use)
- [Libraries](#libraries)
- [Tools](#tools)
- [Services](#services)
- [Education](#education)
  - [Articles](#articles)
  - [Books](#books)
  - [Newsletters](#newsletters)
  - [Videos](#videos)
- [开源项目](#open-source-projects)
- [License](#license)

## 如何使用

只需按 <kbd>Command</kbd> + <kbd>F</kbd> 即可搜索关键字。如果您只对与 [Vapor 3](https://github.com/Cellane/awesome-vapor/blob/filtered/vapor-3.md) 或 [Vapor 4](https://github.com/Cellane/awesome-vapor/blob/filtered/vapor-4.md) 相关的条目感兴趣，您可以通过访问这句话中的链接来使用“filtered”分支上自动生成的过滤列表。您还可以在“legacy”文件夹中找到旧的存档内容。

## 图书馆

- ![v3](img/vapor-3.png) [API 错误中间件](https://github.com/skelpo/APIErrorMiddleware) – Vapor 中间件，用于将抛出的错误转换为 JSON 响应。
- ![v3](img/vapor-3.png) [APNS](https://github.com/vapor-community/apns) – 适用于 iOS 的 Vapor APNS。
- ![v3](img/vapor-3.png) [Bugsnag](https://github.com/nodes-vapor/bugsnag) – 使用 Bugsnag 报告错误。
- ![v3](img/vapor-3.png) [CouchDB 客户端](https://github.com/makoni/couchdb-vapor) – Vapor 的简单 CouchDB 客户端。
- ![v3](img/vapor-3.png) [CrudRouter](https://github.com/twof/VaporCRUDRouter) – 为任何 Fluent 模型自动生成 RESTful CRUD 路由器。
- ![v3](img/vapor-3.png) [CSRF](https://github.com/vapor-community/CSRF) – 一个为 Vapor 添加针对 CSRF 攻击的保护的软件包。
- ![v3](img/vapor-3.png) [CSV 框架](https://github.com/skelpo/CSV) – 一个用于读写 CSV 文件的简单框架。
- ![v3](img/vapor-3.png) [Ferno](https://github.com/vapor-community/ferno) – Vapor Firebase 实时数据库提供商。
- ![v3](img/vapor-3.png) [Flash](https://github.com/nodes-vapor/flash) – 视图之间的 Flash 消息。
- ![v3](img/vapor-3.png) [FluentQuery](https://github.com/MihaelIsaev/FluentQuery) – 构建复杂的原始 SQL 查询，同时仍然使用 Swift keypath。
- ![v3](img/vapor-3.png) [Gatekeeper](https://github.com/nodes-vapor/gatekeeper) – Vapor 的速率限制中间件。
- ![v3](img/vapor-3.png) [Google Cloud Provider](https://github.com/vapor-community/google-cloud-provider) – 与 Vapor 项目中的 Google Cloud Platform API 进行交互。
- ![v3](img/vapor-3.png) [Guardian](https://github.com/Jinxiansen/Guardian) – 现代限速中间件。
- ![v3](img/vapor-3.png) [Imperial](https://github.com/vapor-community/Imperial) – 与 OAuth 提供商的联合身份验证。
- ![v3](img/vapor-3.png) [JWT 钥匙串](https://github.com/nodes-vapor/jwt-keychain) – 使用 JWT for Vapor 轻松搭建钥匙串。
- ![v3](img/vapor-3.png) [JWT Middleware](https://github.com/skelpo/JWTMiddleware) – 在 Vapor 中对请求进行身份验证和授权的中间件。
- ![v3](img/vapor-3.png) [Leaf Error Middleware](https://github.com/brokenhandsio/leaf-error-middleware) – 为您的 Vapor 应用程序提供自定义 404 和服务器错误页面。
- ![v3](img/vapor-3.png) [Leaf Markdown](https://github.com/vapor-community/leaf-markdown) – Vapor 的 Markdown 渲染器。
- ![v3](img/vapor-3.png) [Lingo Vapor](https://github.com/vapor-community/Lingo-Vapor) – Lingo 的 Vapor 提供程序 – Swift 本地化库。
- ![v3](img/vapor-3.png) [本地存储](https://github.com/gperdomor/local-storage) – 使用本地文件系统的存储驱动程序。
- ![v3](img/vapor-3.png) [MailCore](https://github.com/LiveUI/MailCore) – 通过 SMTP、MailGun 和 SendGrid 发送电子邮件。
- ![v3](img/vapor-3.png) [Meow](https://github.com/OpenKitten/Meow) – MongoDB 的替代可编码 ORM。
- ![v3](img/vapor-3.png) [MongoKitten](https://github.com/OpenKitten/MongoKitten) – Swift 中的 MongoDB 驱动程序。
- ![v3](img/vapor-3.png) [分页](https://github.com/vapor-community/pagination) – 简单的 Vapor 3 分页。
- ![v3](img/vapor-3.png) [Paginator](https://github.com/nodes-vapor/paginator) – Vapor 和 Fluent 的查询分页。
- ![v3](img/vapor-3.png) [S3](https://github.com/LiveUI/S3) – 用于访问 Amazon S3 服务（和兼容）的库，支持最常用的操作。
- ![v3](img/vapor-3.png) [S3 Storage](https://github.com/anthonycastelli/s3-storage) – 用于简单访问 Amazon S3 服务的库。
- ![v3](img/vapor-3.png) [Sanitize](https://github.com/gperdomor/sanitize) – 从 Vapor JSON 请求中提取强大的模型。
- ![v3](img/vapor-3.png) [SendGrid Provider](https://github.com/vapor-community/sendgrid-provider) – 由 SendGrid 驱动的 Vapor 邮件后端。
- ![v3](img/vapor-3.png) [SimpleFileLogger](https://github.com/hallee/vapor-simple-file-logger) – Vapor 的简单文件日志记录提供程序。
- ![v3](img/vapor-3.png) [Slugify](https://github.com/nodes-vapor/slugify) – 方便地拖拽你的琴弦。
- ![v3](img/vapor-3.png) [存储](https://github.com/nodes-vapor/storage) – 简化多个存储和 CDN 服务的使用。
- ![v3](img/vapor-3.png) [Stripe Provider](https://github.com/vapor-community/stripe-provider) – Vapor 的 Stripe 提供商。
- ![v3](img/vapor-3.png) [提交](https://github.com/nodes-vapor/submissions) – 方便创建表单和验证（表单）提交。
- ![v3](img/vapor-3.png) [Sugar](https://github.com/nodes-vapor/sugar) – Vapor 的糖包。
- ![v3](img/vapor-3.png) [SwifQL](https://github.com/MihaelIsaev/SwifQL) – 使用纯 Swift 轻松构建灵活且类型安全的 SQL。
- ![v3](img/vapor-3.png) [SwiftyBeaver Provider](https://github.com/vapor-community/swiftybeaver-provider) – Vapor（服务器端 Swift Web 框架）的 SwiftyBeaver 日志提供程序。
- ![v3](img/vapor-3.png) [Telesign Provider](https://github.com/vapor-community/telesign-provider) – Vapor 的 Telesign 提供商。
- ![v3](img/vapor-3.png) [Vapor Mailgun Service](https://github.com/vapor-community/VaporMailgunService) – 与 Vapor 一起使用来发送电子邮件的服务。
- ![v3](img/vapor-3.png) [Vapor reCAPTCHA](https://github.com/gotranseo/vapor-recaptcha) – 使用 Vapor 验证 Google reCAPTCHA。
- ![v3](img/vapor-3.png) [Vapor 请求存储](https://github.com/skelpo/vapor-request-storage) – Vapor 1 和 2 中可用的 `request.storage` 的替代品。
- ![v3](img/vapor-3.png) [Vapor 安全标头](https://github.com/brokenhandsio/VaporSecurityHeaders) – 强化 Vapor 的安全标头。
- ![v3](img/vapor-3.png) [Vapor 测试工具](https://github.com/LiveUI/VaporTestTools) – 旨在让您在 Vapor 3 中轻松测试端点的帮助程序。
- ![v3](img/vapor-3.png) [VaporExt](https://github.com/vapor-community/vapor-ext) – 适用于各种 Vapor 数据类型和类的 Swift 扩展集合。
- ![v3](img/vapor-3.png) [WKHTMLTOPDF](https://github.com/MihaelIsaev/wkhtmltopdf) – 通过 `wkhtmltopdf` CLI 工具从 Leaf 模板或网页构建 PDF 文件。
- ![v3](img/vapor-3.png) [XMLCoding](https://github.com/LiveUI/XMLCoding) – XML 编码器和解码器。

## 工具

- [Ether](https://github.com/Ether-CLI/Ether) - Swift 包管理器的命令行界面。
- [Heroku buildpack：带有 HTTP/2 支持的curl](https://github.com/vzsg/heroku-buildpack-curl-http2)
- [Ice](https://github.com/jakeheis/Ice) - 一个开发者友好的 Swift 包管理器；与 Swift 包管理器 100% 兼容。
- [Sourcery](https://github.com/krzysztofzablocki/Sourcery) - Swift 元编程，停止编写样板代码。
- ![v3](img/vapor-3.png) [Sublimate](https://github.com/gabrielepalma/sublimate) – 基于 Sourcery 的同步和身份验证快速原型设计。
- [Swifter](https://github.com/LiveUI/Swifter) - 一款 macOS 工具，可帮助您管理 Xcode 项目，并让您快速访问 DerivedData 文件夹清理和管理。

## 服务

- [蒸气云](https://vapor.cloud)
- [蒸气红](https://vapor.red)

## 教育

### 文章

- ![v3](img/vapor-3.png) [深入了解 Heroku 和 Ubuntu 的设置和部署](https://learningswift.brightdigit.com/vapor-heroku-ubuntu-setup-deploy/)
- ![v3](img/vapor-3.png) [如何通过模拟 Vapor 3 和 Swift 中的依赖关系来测试控制器](https://mikemikina.com/blog/how-to-test-controllers-by-mocking-dependency-in-vapor-3-and-swift/)
- ![v3](img/vapor-3.png) [Vapor 3 教程](https://mihaelamj.github.io/Vapor%20%203%20Tutorial/) – 小教程的大集合。
- ![v3](img/vapor-3.png) [从 Vapor 2 转换到 Vapor 3](https://www.skelpo.com/blog/vapor2-to-vapor3/) – 通过真实项目从 Vapor 2 转换到 Vapor 3。
- ![v3](img/vapor-3.png) [初学者到高级教程](https://medium.com/@martinlasek) – 初学者到高级的书面教程。
- ![v3](img/vapor-3.png) [使用依赖注入框架在 Vapor 3 和 Swift 中进行测试](https://mikemikina.com/blog/using-the-dependency-injection-framework-for-testing-in-vapor-3-and-swift/) – 如何使用依赖注入框架，它将帮助您管理依赖项并在测试中模拟它们。
- ![v3](img/vapor-3.png) [在 macOS 和 Linux 上使用 ImageMagick、Vapor 3 和 Swift 对照片添加水印](https://mikemikina.com/blog/watermarking-photos-with-imagemagick-vapor-3-and-swift-on-macos-and-linux/) – 有关如何在 Swift 中使用 ImageMagick 库的教程。
- ![v4](img/vapor-4.png) [Vapor 4 有什么新功能？](https://theswiftdev.com/2019/08/26/whats-new-in-vapor-4/)

### 书籍

- ![v3](img/vapor-3.png) [带 Vapor 的服务器端 Swift](https://store.raywenderlich.com/products/server-side-swift-with-vapor)
- ![v3](img/vapor-3.png) [服务器端 Swift (Vapor 版)](https://www.hackingwithswift.com/store/server-side-swift)

### 时事通讯

- [VaporNation](http://vapornation.news) - 每周蒸汽时事通讯，包含有关蒸汽的所有内容。

### 视频

- ![v3](img/vapor-3.png) [带 Vapor 的服务器端 Swift](https://www.raywenderlich.com/4493-server-side-swift-with-vapor/lessons/1)
- ![v3](img/vapor-3.png) [Vapor - 初级到高级](https://www.youtube.com/channel/UCoLEXFUHIKXunm9QJjsAftw/videos)

## 开源项目

- ![v3](img/vapor-3.png) [SteamPress](https://github.com/brokenhandsio/SteamPress) – 用 Swift 编写的博客引擎和平台，与 Vapor 框架一起使用。
- ![v3](img/vapor-3.png) [用户管理器服务](https://github.com/skelpo/UserManager) – 一个小型、有用的用户管理器，用于生产应用程序设置。

## 许可证

[![CC0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

在法律允许的范围内，_Milan Vit_ 已放弃本作品的所有版权以及相关或邻接权。
