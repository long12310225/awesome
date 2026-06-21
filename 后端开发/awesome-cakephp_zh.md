# 很棒的 CakePHP [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> CakePHP 插件、资源和工具的精选列表。

[CakePHP](https://cakephp.org/) 是一个快速开发的 PHP 框架，它使用 MVC 和 ORM 等众所周知的设计模式。它为构建具有约定优于配置的 Web 应用程序提供了坚实的基础。

如果您正在寻找以前的 CakePHP 资源，请访问：
- 这个很棒的列表的 [CakePHP 2.x 版本](https://github.com/FriendsOfCake/awesome-cakephp/tree/cake2)
- 这个很棒的列表的 [CakePHP 3.x 版本](https://github.com/FriendsOfCake/awesome-cakephp/tree/cake3)
- 这个很棒的列表的 [CakePHP 4.x 版本](https://github.com/FriendsOfCake/awesome-cakephp/tree/cake4)
- 这个维基有一个[尚未升级的插件列表](https://github.com/FriendsOfCake/awesome-cakephp/wiki#plugins-not-yet-upgraded-from-2x-to-3x)

您可能会发现有用的其他列表：
- [CakePHP 插件](https://plugins.cakephp.org)
- [很棒的 PHP](https://github.com/ziadoz/awesome-php)
- [令人敬畏的令人敬畏的](https://github.com/bayandin/awesome-awesomeness)

> 对于那些想知道的人；该列表与plugins.cakephp.org 的不同之处在于支持
> 插件子部分（而不是整个插件/存储库），更细粒度
> 分组并主要关注特定于任务的功能。

## 内容

- [Plugins](#plugins)
	- [人工智能工具](#ai-tools)
	- [Architecture](#architecture)
	- [资产管理](#asset-management)
	- [审计/日志记录](#auditing--logging)
	- [认证与授权](#authentication-and-authorization)
	- [Caching](#caching)
	- [代码分析](#code-analysis)
    - [Console](#console)
	- [Debugging](#debugging)
	- [Email](#email)
	- [文件操作](#file-manipulation)
	- [过滤和验证](#filtering-and-validation)
	- [Geolocation](#geolocation)
	- [I18n](#i18n)
	- [Imagery](#imagery)
	- [Libs](#libs)
	- [Markup](#markup)
	- [Migration](#migration)
	- [Miscellaneous](#miscellaneous)
	- [Navigation](#navigation)
	- [通知和实时通信](#notifications-and-real-time-communication)
	- [ORM / 数据库 / 数据映射](#orm--database--datamapping)
	- [PDF](#pdf)
	- [Queue](#queue)
	- [休息和API](#rest-and-api)
	- [Search](#search)
	- [Security](#security)
	- [SEO](#seo)
	- [Skeleton](#skeleton)
	- [Social](#social)
	- [Templating](#templating)
	- [Testing](#testing)
	- [第三方API](#third-party-apis)
- [Software](#software)
	- [开发环境](#development-environment)
	- [网络应用程序](#web-applications)
	- [基于 CakePHP 构建的 CMS 和应用程序](#cms-and-applications-built-on-cakephp)
	- [Demo](#demo)
- [Resources](#resources)
	- [Help](#help)
	- [CakePHP 网站](#cakephp-websites)
	- [CakePHP 书籍和文章](#cakephp-books-and-articles)
	- [CakePHP 视频](#cakephp-videos)
	- [CakePHP 教程](#cakephp-tutorials)
	- [CakePHP 阅读和听力](#cakephp-reading-and-listening)
	- [CakePHP 内部原理阅读](#cakephp-internals-reading)
- [Conferences](#conferences)

## 插件

### 人工智能工具
*用于集成人工智能和机器学习工具的插件和库。*

- [Crustum/OpenRouter plugin](https://github.com/crustum/cakephp-open-router) - 与 OpenRouter 服务集成，实现统一的 LLM 访问，支持多种 AI 模型，包括聊天完成、流媒体、工具调用和网络搜索。
- [Synapse plugin](https://github.com/josbeir/cakephp-synapse) - 通过 MCP 公开您的应用程序功能，并使用内置工具和文档搜索来帮助您发现应用程序的功能并与之交互。

### 建筑

- [Burzum/CakeServiceLayer plugin](https://github.com/burzum/cakephp-service-layer) - 服务层和领域/业务模型实现。

### 资产管理
*管理、压缩和缩小网站资产。*

- [AssetCompress plugin](https://github.com/markstory/asset_compress) - CakePHP 的完整资产管理器。
- [AssetMix plugin](https://github.com/ishanvyas22/asset-mix) - 提供与 [Laravel Mix](https://laravel-mix.com) 资源编译的集成。
- [CakeVite plugin](https://github.com/josbeir/cakephp-vite) - 一个功能齐全的 [Vite](https://vite.dev/) 插件（[brandcom/cakephp-vite](https://github.com/brandcom/cakephp-vite) 的精神继承者）。

### 审计/日志记录
*跟踪应用程序中的更改和事件。*

- [AuditStash plugin](https://github.com/dereuromark/cakephp-audit-stash) - 灵活且坚如磐石的审计日志跟踪。
- [Bouncer plugin](https://github.com/dereuromark/cakephp-bouncer) - AuditStash 的挂件允许在应用实际更改之前审核和批准添加/编辑/删除操作。
- [DatabaseLog plugin](https://github.com/dereuromark/CakePHP-DatabaseLog) - 简单且独立的日志记录到数据库而不是文件。
- [Muffin/Footprint plugin](https://github.com/UseMuffin/Footprint) - 允许将当前登录的用户传递到模型层的插件。
- [Version plugin](https://github.com/josegonzalez/cakephp-version) - 一个促进版本化数据库实体的插件。

### 认证与授权
*用于实现身份验证和授权的插件和库。*

- [ADmad/SocialAuth plugin](https://github.com/ADmad/cakephp-social-auth) - 该插件允许您使用 Facebook/Google/Twitter 等社交提供商使用 [SocialConnect/auth](https://github.com/SocialConnect/auth) 社交登录库进行身份验证。
- [ApiTokenAuthenticator plugin](https://github.com/rrd108/api-token-authenticator) - 用于 CakePHP REST API 的简单令牌身份验证插件。
- [Authentication plugin](https://github.com/cakephp/authentication) - 官方 CakePHP 身份验证中间件插件。
- [Authorization plugin](https://github.com/cakephp/authorization) - 官方 CakePHP 授权堆栈。
- [CakeDC/Users plugin](https://github.com/CakeDC/users) - 完整的用户管理（管理面板、记住我等）、社交登录（FB、Twitter、LinkedIn、Google、Instagram）、RBAC、API 等。
- [CakeVerification plugin](https://github.com/salines/cakephp-verification) - 支持电子邮件 OTP、电子邮件 Magic Link、短信 OTP 和 TOTP（Google 身份验证器）的二因素验证。

- [TinyAuth plugin](https://github.com/dereuromark/cakephp-tinyauth) - 身份验证和基于角色（单/多）授权是非常轻量级的方法。
- [Tools:Passwordable](https://github.com/dereuromark/cakephp-tools) - 包含 [Passwordable 行为](https://dereuromark.github.io/cakephp-tools/behavior/passwordable)，用于密码哈希的 DRY 方法。
- [TwoFactorAuth plugin](https://github.com/andrej-griniuk/cakephp-two-factor-auth) - 允许使用 Google Authenticator 或类似应用程序进行两因素身份验证以生成一次性代码。基于 [RobThree/TwoFactorAuth](https://github.com/RobThree/TwoFactorAuth) 库。

### 缓存
*存储数据以便更快地检索。*

- [Cache plugin](https://github.com/dereuromark/cakephp-cache) - 用于将视图（HTML、CSV、JSON、XML...）缓存为静态缓存文件。
- [CakeDC/CachedRouting plugin](https://github.com/CakeDC/cakephp-cached-routing) - 提供路由中间件的缓存版本，以提高路由的加载时间。

### 代码分析
*分析、解析和操作代码库。*

- [cakedc/cakephp-phpstan](https://github.com/CakeDC/cakephp-phpstan) - PHPStan 扩展，用于解决静态分析器 getter 返回类型周围的 CakePHP 魔法。
- [IdeHelper plugin](https://github.com/dereuromark/cakephp-ide-helper) - 通过向现有代码添加注释（类似于烘焙对新代码的作用），有助于更好地支持 IDE。
- [IdeHelperExtra plugin](https://github.com/dereuromark/cakephp-ide-helper-extra) - 适用于其他插件或自定义用例的有用 IdeHelper 插件。
- [lordsimal/cakephp-psalm](https://github.com/LordSimal/cakephp-psalm) - 一个 Psalm 扩展，用于解决 CakePHP 静态分析器 getter 返回类型的魔力。
- [TestHelper plugin](https://github.com/dereuromark/cakephp-test-helper) - 提供测试增强功能和 TDD 支持作为浏览器后端。

### 控制台
*命令行工具和改进。*

- [SignalHandler plugin](https://github.com/skie/SignalHandler) - CakePHP 控制台命令的跨平台信号处理，具有零外部依赖性。支持Linux (pcntl)、Windows (本机API)。
- [Scheduling plugin](https://github.com/skie/cakephp-scheduling) - 该插件提供亚分钟精度的任务调度功能，允许您使用单个 crontab 入口点以每秒的频率调度任务。它允许任务监控。

### 调试
*调试和本地开发。*

- [AssociationsDebugger plugin](https://github.com/zunnu/associations-debugger) - 一个将模型关联绘制为图表的插件。
- [CakephpWhoops plugin](https://github.com/dereuromark/cakephp-whoops) - 使用 [filp/whoops](https://github.com/filp/whoops) 为酷孩子提供 PHP 错误和异常。
- [DebugKit plugin](https://github.com/cakephp/debug_kit) - 调试的事实上的标准。
- [Execution order](https://github.com/dereuromark/executionorder) - 一个演示应用程序，用于显示文件、方法和回调的执行顺序。
- [Sentry plugin](https://github.com/lordsimal/cakephp-sentry) - 一个无缝集成 Sentry 错误和异常的插件。
- [Setup plugin](https://github.com/dereuromark/cakephp-setup) - 一个轻量级设置插件，包含健康检查、调试和维护工具。

### 电子邮件
*用于电子邮件处理的传输和工具。*

- [Queue plugin](https://github.com/dereuromark/cakephp-queue) - 使用 Mailer/Email 类的无依赖性基于队列的邮件解决方案，允许在（网络）故障时重新排队。
- [SendGrid plugin](https://github.com/sprintcube/cakephp-sendgrid) - 用于通过 SendGrid API 发送电子邮件的电子邮件传输插件。

### 文件操作
*上传、存储和文件处理。*

- [FileStorage plugin](https://github.com/dereuromark/cakephp-file-storage) - 灵活的文件存储和上传插件。
- [Josegonzalez/Upload plugin](https://github.com/FriendsOfCake/cakephp-upload) - 一个可定制的插件，使用 [Flysystem](https://flysystem.thephpleague.com/) 写入多个后端（Dropbox、FTP、S3、本地等）。

### 过滤和验证
*数据清理和验证规则。*

- 请参阅下面的 Cake/本地化插件。
- 请参阅下面的工具插件。
- [RuleFlow plugin](https://github.com/skie/rule-flow) - 一个插件，可将服务器端验证规则无缝转换为客户端 JSON 逻辑验证，提供自动表单验证，无需单独的客户端验证代码。


### 地理定位
*对地址进行地理编码并使用纬度和经度。*

- [Geo plugin](https://github.com/dereuromark/cakephp-geo) - 包含[地理编码器行为](https://www.dereuromark.de/2012/06/12/geocoding-with-cakephp/)和[GoogleMaps helper](https://www.dereuromark.de/2010/12/21/googlemapsv3-cakephp-helper/)。

### 国际化
*I18n（国际化）和 L10n（本地化）。*

- [ADmad/I18n plugin](https://github.com/ADmad/cakephp-i18n) - 带有 I18n 相关工具的插件。
- [Cake/Localized plugin](https://github.com/cakephp/localized) - 本地化验证和即用型翻译 PO 文件。
- [Translate plugin](https://github.com/dereuromark/cakephp-translate) - 轻松在后端翻译您的翻译。

### 图像
*图像处理和操作库。*

- [ADmad/Glide plugin](https://github.com/ADmad/cakephp-glide) - 一个使用 [Glide](https://glide.thephpleague.com/) 图像处理库的插件。
- [file-storage-image-processor](https://github.com/php-collective/file-storage-image-processor) 通过 [FileStorage 插件](https://github.com/dereuromark/cakephp-file-storage) 作为“干预/图像”包装器。
- [QrCode plugin](https://github.com/dereuromark/cakephp-qrcode/) - 轻松为您的应用渲染 SVG/PNG QR 代码。

### 库
*不属于任何其他类别的有用的库或工具。*

- [Chronos](https://github.com/cakephp/chronos) - 一个简单的独立 DateTime API 扩展（Carbon 的后继者）。
- [Composer Installers](https://github.com/composer/installers) - 多框架 Composer 库安装程序。
- [Composer](https://getcomposer.org/)/[Packagist](https://packagist.org/) - 包和依赖项管理器。
- [Graphviz](https://github.com/alexandresalome/graphviz) - Graphviz 库。
- [Rocketeer](https://github.com/rocketeers/rocketeer) - PHP 任务运行程序和部署包。

### 标记
*语法突出显示和标记处理。*

- [Markup plugin](https://github.com/dereuromark/cakephp-markup) - 允许使用基于 PHP 或 JS 的语法突出显示。

### 迁移
*有关迁移和升级的插件和资源。*

- [Migrations plugin](https://github.com/cakephp/migrations) - (DB) 迁移插件。
- [Upgrade app](https://github.com/cakephp/upgrade) - 3.x=>4.x 和 4.x=>5.x 的官方升级应用程序。
- [Upgrade app (extended)](https://github.com/dereuromark/upgrade) - 3.x=>4.x 和一些 5.x 片段的扩展升级应用程序。
- [Upgrade/Migration Guide](https://book.cakephp.org/5/en/appendices.html) - 官方迁移指南。

### 杂项
*杂项插件和库。*

- [Ajax plugin](https://github.com/dereuromark/cakephp-ajax) - 用于简化处理 AJAX 请求的插件。
- [AttributeRegistry plugin](https://github.com/josbeir/cakephp-attribute-registry) - 一个强大的 CakePHP 插件，用于跨应用程序和插件发现、缓存和查询 PHP 8 属性。
- [CakeDC/Enum plugin](https://github.com/CakeDC/enum) - 一个为您的应用程序添加枚举列表支持的插件。
- [CakeDto plugin](https://github.com/dereuromark/cakephp-dto) - 快速为您的应用程序生成有用的数据传输对象（可变/不可变），替换杂乱的数组并通过类型提示和自动完成来利用您的 IDE。
- [CakeHtmx plugin](https://github.com/zunnu/cake-htmx) - [htmx](https://htmx.org/) 的 CakePHP 集成。
- [Calendar plugin](https://github.com/dereuromark/cakephp-calendar) - 用于生成基本日历。包括用于生成 ICS 日历文件的 IcalView。
- [DatabaseBackup plugin](https://github.com/mirko-pagliai/cakephp-database-backup) - 用于导出、导入和管理数据库备份的插件。目前，该插件支持 MySQL、PostgreSQL 和 SQLite 数据库。
- [Feedback plugin](https://github.com/dereuromark/cakephp-feedback) - 允许访问者发送快速、简单的反馈，包括。通过侧边栏形式的屏幕截图。
- [Flash plugin](https://github.com/dereuromark/cakephp-flash) - 为您的应用程序提供更强大的闪存消息。
- [Inertia plugin](https://github.com/CakeDC/cakephp-inertia) - 用于连接 Vue 3 应用程序并通过中间件使用 API 接口的插件。
- [OPCache Preloader](https://github.com/cnizzardini/cakephp-preloader) - CakePHP 应用程序的 OPCache 预加载器。
- [Setup:Maintenance](https://github.com/dereuromark/cakephp-setup/blob/master/docs/Maintenance/Maintenance.md) - 维护 shell 通过可选的 IP 白名单进入所有请求的维护模式。
- [Shim plugin](https://github.com/dereuromark/cakephp-shim) - 一个包含有用的垫片和改进的插件，作为您的应用程序的基础。
- [Tools plugin](https://github.com/dereuromark/cakephp-tools) - 包含许多有用的帮助器、行为、组件、命令、帮助器、库等等。
- [Workflow plugin](https://github.com/dereuromark/cakephp-workflow) - 包含电池的状态机插件，具有 PHP 8 属性、YAML 配置、审计跟踪和可视化管理仪表板。

### 导航
*构建导航结构。*

- [Icings/Menu plugin](https://github.com/icings/menu) - 用于 CakePHP 的 [KnpMenu](https://github.com/KnpLabs/KnpMenu) 经验丰富的菜单插件。
- [Menu plugin](https://github.com/dereuromark/cakephp-menu) - 可组合的菜单生成器和渲染器，用于嵌套导航、活动状态匹配和面包屑 - 以及零依赖性。

### 通知和实时通信
*使用通知软件。*

- [Crustum/Broadcasting plugin](https://github.com/crustum/broadcasting) - 广播插件使用与 Pusher 协议或 Redis pub/sub 兼容的 WebSocket 连接为 CakePHP 应用程序提供实时事件广播。
- [Crustum/Notification plugin](https://github.com/crustum/notification) - 通知插件支持通过各种传递渠道发送通知。
- [Mercure plugin](https://github.com/josbeir/cakephp-mercure) - 使用 Mercure 协议向客户端推送实时更新。

### ORM / 数据库 / 数据映射
*实现对象关系映射或数据映射技术的插件。*

- [ADmad/Sequence plugin](https://github.com/ADmad/cakephp-sequence) - 维护有序记录列表的行为。
- [CakeDecimal plugin](https://github.com/dereuromark/cakephp-decimal) - 处理小数的值对象方法。
- [CakeUid](https://github.com/josbeir/cakephp-uid) - 表的 UID 字段类型的集合（UUIDV4、UUIDV6、UUIDV7、ULID）。
- [Duplicatable plugin](https://github.com/riesenia/cakephp-duplicatable) - 复制实体（包括相关数据）的行为。
- [Lampager/Cake plugin](https://github.com/lampager/lampager-cakephp) - 无需使用 OFFSET 即可快速分页。
- [Muffin/Orderly plugin](https://github.com/usemuffin/orderly) - 允许为表设置默认顺序。
- [Muffin/Trash plugin](https://github.com/usemuffin/trash) - CakePHP 的软删除行为。
- [Itosho/EasyQuery plugin](https://github.com/itosho/easy-query) - 轻松生成一些复杂查询的行为，例如（批量）插入/更新插入等。
- [Icings/Partitionable plugin](https://github.com/icings/partitionable) - 可分区关联允许对每个组进行基本限制。

### PDF
*用于处理 PDF 文件的插件和软件。*

- [CakePdf plugin](https://github.com/FriendsOfCake/CakePdf) - 一个围绕 PDF 生成的插件。

### 队列
*使用事件和任务队列。*

- [Queue plugin](https://github.com/cakephp/queue) - CakePHP 核心队列系统是 [php-queue](https://php-enqueue.github.io) 队列库。
- [Cake/Enqueue plugin](https://github.com/CakeDC/cakephp-enqueue) - 使用 CakePHP 队列插件的 Enqueue 库进行数据库驱动的消息队列集成。
- [Crustum/BatchQueue plugin](https://github.com/crustum/batch-queue) - 用于管理具有并行执行和顺序链的批处理作业处理的统一系统。
- [Crustum/Temporal plugin](https://github.com/crustum/cakephp-temporal) - 工作流编排插件，可实现持久执行、可靠的后台作业以及具有自动重试功能的长时间运行的流程。
- [Queue plugin](https://github.com/dereuromark/cakephp-queue) - 最小且无依赖性的队列解决方案。
- [QueueScheduler plugin](https://github.com/dereuromark/cakephp-queue-scheduler) - 一个无依赖性的类似 crontab 的调度程序，作为数据库驱动的解决方案和队列 (dereuromark) 插件的插件。

### 休息和API
*用于开发 REST-ful API 的插件和 Web 工具。*

- [CRUD plugin](https://github.com/FriendsOfCake/crud) - CakePHP 类固醇应用程序开发 - 快速原型设计/脚手架和生产就绪代码。
- [CakeDC/Api plugin](https://github.com/CakeDC/cakephp-api) - 一体化解决方案提供完整的 API。它包括版本控制、渲染器、CRUD、身份验证、扩展（分页、过滤器、HATEOAS）等等。
- [FractalTransformerView plugin](https://github.com/andrej-griniuk/cakephp-fractal-transformer-view) - 一个允许使用 [Fractal Transformers](https://fractal.thephpleague.com/transformers/) 进行 API 输出的插件。
- [MixerApi](https://mixerapi.com) - 为您团队的 CakePHP 项目简化现代 RESTful API 的开发。
- [SwaggerBake plugin](https://github.com/cnizzardini/cakephp-swagger-bake) - 该插件会自动根据现有模型和路线构建 OpenAPI，以便在 Swagger 和 Redoc 中显示。

### 搜索
*用于对数据进行索引和执行搜索查询的插件和软件。*

- [Cake/Elasticsearch plugin](https://github.com/cakephp/elastic-search) - 使用 [Elasticsearch](https://www.elastic.co/) 作为后端的替代 ORM。
- [CakeDC/SearchFilter plugin](https://github.com/CakeDC/search-filter) - 用于实现高级搜索功能的强大而灵活的解决方案。提供了一组强大的工具，可以轻松创建动态、用户友好的搜索界面。
- [PlumSearch plugin](https://github.com/skie/plum_search) - 实施自定义、灵活且可扩展的搜索策略。实现 PRG 模式。
- [Search plugin](https://github.com/FriendsOfCake/search) - 使用 PRG 模式为分页视图提供轻松的搜索/过滤。
- [Tags plugin](https://github.com/dereuromark/cakephp-tags) - 用于标记和查找标记记录。

### 安全性
*有关安全的插件和信息，防止漏洞并防范 XSS 等。*

- [Captcha plugin](https://github.com/dereuromark/cakephp-captcha) - 简单、不显眼且可扩展的验证码解决方案默认提供基于图像的数学验证码。
- [Expose plugin](https://github.com/dereuromark/cakephp-expose) - 通过额外的 UUID 而不是 AIID 主键来公开实体，以混淆与这些数字排序值关联的 ID 和数据。
- [Muffin/Obfuscate plugin](https://github.com/usemuffin/obfuscate) - 使用 UUID、HashId、Optimus、Tiny 和/或自定义混淆策略进行主键混淆/缩短。
- [Muffin/Throttle plugin](https://github.com/usemuffin/throttle) - 用于速率限制 (API) 请求的插件。
- [Recaptcha plugin](https://github.com/ctlabvn/Recaptcha) - 简单、轻量级的 Google Recaptcha v2。

### 搜索引擎优化
*搜索引擎优化。*

- [Muffin/Slug plugin](https://github.com/UseMuffin/Slug) - 一个用于生成 slug 并通过 slug 查找记录的插件。使用可插入架构，允许使用您自己的 slug 生成器类。
- [Tools:Slugged](https://github.com/dereuromark/cakephp-tools) - 包含 Slugged 行为，从标题自动生成 URL 兼容的 slugs。

### 骷髅
*围绕应用程序骨架的插件和存储库。*

- [App template](https://github.com/cakephp/app) - 一个与 Composer 一起使用的空 CakePHP 项目。
- [BS flavored App template](https://github.com/dereuromark/cakephp-app) - 一个空的 CakePHP 项目，带有 BS5 和开箱即用的 FontAwesome。

### 社交
*围绕社交功能的插件。*

- [Comments plugin](https://github.com/dereuromark/cakephp-comments) - 允许用户评论记录，支持不同格式。
- [Favorites plugin](https://github.com/dereuromark/cakephp-favorites) - 允许用户对记录加注星标/点赞/收藏。
- [Ratings plugin](https://github.com/dereuromark/cakephp-ratings) - 允许用户对记录进行评分并显示评分。

### 模板化
*模板引擎和视图生成。*

- [Bake plugin](https://github.com/cakephp/bake) - 提供代码生成功能。
- [BootstrapUI plugin](https://github.com/friendsofcake/bootstrap-ui) - Bootstrap 4/5 集成。
- [CsvView plugin](https://github.com/FriendsOfCake/cakephp-csvview) - 用于轻松生成 CSV 的视图类。
- [Feed plugin](https://github.com/dereuromark/cakephp-feed) - 包含 RssView 类以轻松生成（复杂）RSS 提要。
- [LatteView plugin](https://github.com/josbeir/cakephp-latte-view) - 提供 Latte 模板引擎集成的插件。
- [Meta plugin](https://github.com/dereuromark/cakephp-meta) - 使处理元标记和 SEO 相关的 HTML 标记变得干燥而简单。
- [TailwindUi plugin](https://github.com/dereuromark/cakephp-tailwind-ui) - Tailwind CSS / DaisyUI（或 KTUI/Metronic）集成，用于表单、分页、flash 和面包屑帮助程序。
- [TemplaterDefaults plugin](https://github.com/josbeir/cakephp-templater-defaults) - 允许在 CakePHP 的字符串模板系统中使用默认的 HTML 属性。
- [Templating](https://github.com/dereuromark/cakephp-templating) - HTML 片段作为值对象、（字体）图标和模板化主题。
- [Tools:Tree](https://github.com/dereuromark/cakephp-tools) - 树助手用于处理核心树行为并处理树结构输出。
- [TwigView plugin](https://github.com/cakephp/twig-view) - 使用 Twig 模板语言创建视图的插件。
- [XlsView plugin](https://github.com/impronta48/cakephp-xlsview) - 使用 PHPSpreadsheet 轻松生成 XLS 的视图类。

### 测试
*用于测试代码库和生成测试数据的插件/工具。*

- [CakePHP CodeSniffer rules](https://github.com/cakephp/cakephp-codesniffer) - CakePHP CS 官方规则。
- [CakephpFixtureFactories plugin](https://github.com/dereuromark/cakephp-fixture-factories) - 在测试的基础上动态创建您的装置，加速测试的编写和维护。
- [FriendsOfCake/Fixturize plugin](https://github.com/FriendsOfCake/fixturize) - 通过减少插入量（仅限 MySQL）运行测试套件时更有效地插入固定装置。

### 第三方API
*访问第三方API。*


## 软件

*用于创建开发环境的软件。*

### 开发环境
*用于创建沙盒开发环境的软件和工具。*

- [CakePHP Docker](https://github.com/cnizzardini/cakephp-docker) - Docker 的 cakephp/app 模板。
- [CakePHP Vagrant Setup](https://github.com/cpierce/cakephp-vagrant-setup) - 使用 Vagrant 启动多个 CakePHP 原生开发环境的工具。
- [CakePHP Docker Setup](https://github.com/cpierce/cakephp-docker-setup) - 使用 Docker 启动多个 CakePHP 原生开发环境的工具。
- [DDEV](https://ddev.readthedocs.io/en/stable/) - 基于 Docker 的本地环境。
- [Devilbox](https://devilbox.readthedocs.io/en/latest/) - 用于自动设置（CakePHP）应用程序的 Docker 开发环境，包括许多工具。
- [Docker](https://github.com/stefanvangastel/docker-cakephp) - Docker 容器环境中的 CakePHP。
- [Galley](https://gitlab.com/amayer5125/galley) - 用于 CakePHP 开发的小型 Docker 开发环境，其中包括一个简单的命令行实用程序。
- [NetBeans](https://github.com/junichi11/cakephp3-netbeans) - 该软件包在 NetBeans 8.1+ 中提供对 CakePHP 的支持。
- [Puppet](https://puppetlabs.com/) - 服务器自动化框架和应用程序。
- [Vagrant](https://developer.hashicorp.com/vagrant) - 便携式开发环境实用程序。

IDE 特定兼容性信息和提示可以在[此处](https://github.com/dereuromark/cakephp-ide-helper/wiki#ide-support-and-tips) 找到。

### 网络应用程序

- [Toolbox](https://toolbox.dereuromark.de) - 在线工具箱，其中包含适用于现代 CakePHP 应用程序的有用工具。为出色的 CI/linter 提供支持。

### 基于 CakePHP 构建的 CMS 和应用程序

- [baserCMS](https://github.com/baserproject/basercms) - 这是一个带有 RESTful API 的网站开发框架。可作为 CakePHP 的插件安装。

### 演示

*基于网络（演示）的应用程序和工具。*

- [BlogMVC](https://github.com/Kareylo/BlogMVC-CakePHP3) - 基于 [BlogMVC 项目](https://github.com/Grafikart/BlogMVC) 的 CakePHP 的简单博客示例。
- [Bookmarkr](https://github.com/lorenzo/cakephp3-bookmarkr) - 使用 CRUD 插件构建的书签应用程序。
- [Fluentd + Grafana Loki demo application](https://github.com/ishanvyas22/cakephp-loki-demo) - 一个演示应用程序，用于通过 [Fluentd](https://www.fluentd.org/) 将 CakePHP Docker 容器日志发送到 [Grafana Loki](https://grafana.com/)。
- [RealWorld](https://github.com/gothinkster/cakephp-realworld-example-app) - 示例 CakePHP 代码库包含遵循 [RealWorld](https://github.com/gothinkster/realworld-example-apps) 规范和 API 的真实世界示例（CRUD、身份验证、高级模式等）。
- [Sandbox](https://sandbox.dereuromark.de) - 一个沙箱 CakePHP 应用程序，包含大量演示和插件展示。
- [TinyAuth demo](https://github.com/dereuromark/cakephp-tinyauth-demo) - 完整的交互身份验证（TinyAuth 包括身份验证和授权核心插件）演示。
- [Query examples](https://github.com/lorenzo/cakephp3-examples) - 高级查询构建示例。
- [Xeta](https://github.com/XetaIO/Xeta) - 帮助人们开始使用 CakePHP 的资源。
- [Vue.js demo app](https://github.com/ishanvyas22/cakephpvue-spa) - CakePHP + Vue.js 单页面应用程序框架。

## 资源

用于提高 CakePHP 开发技能和知识的各种资源，例如书籍、网站和文章。

### 帮助
*从哪里获得帮助。*

- [Official CakePHP Forum](https://discourse.cakephp.org/) - 这是针对一般性问题等。
- [stackoverflow.com/questions/tagged/cakephp](https://stackoverflow.com/questions/tagged/cakephp) - 这是针对特定问题的，最好还有一些示例代码。

### CakePHP 网站
*有用且最新的 CakePHP 相关网站和博客。*

- [CakeDC](https://www.cakedc.com/articles) - 有关 CakePHP 的文章。
- [dereuromark.de](https://www.dereuromark.de) - 内容丰富的 CakePHP 核心开发博客。
- [josediazgonzalez.com](https://josediazgonzalez.com/) - 主要与 CakePHP 相关的核心开发博客。
- [mark-story.com](https://mark-story.com) - CakePHP 首席开发博客。

### CakePHP 书籍和文章
*Fantastic CakePHP 相关（电子）书籍和其他阅读材料。*

### CakePHP 视频
*精彩的 CakePHP 相关视频。*

- [CakePHP](https://www.youtube.com/user/CakePHP) - 有关 CakePHP 视频的频道。


### CakePHP 教程
*必做教程。*

- [官方内容管理教程](https://book.cakephp.org/5/en/tutorials-and-examples/cms/installation.html)

### CakePHP 阅读和听力
*文档和CakePHP相关的阅读和听力材料。*

- [CakePHP Cookbook(!)](https://book.cakephp.org/) - CakePHP 官方文档。

### CakePHP 内部原理阅读
*阅读与 CakePHP 内部结构和决策相关的材料。*

- [Top 10 (and more) core contributors](https://github.com/cakephp/cakephp/graphs/contributors) - 帮他们一把。

## 会议

### 官方
*国际会议。*

- [cakefest.org](https://cakefest.org/) - 年度 CakePHP 会议。

### 聚会
*区域聚会。*

- [CakePHP-DE](https://www.meetup.com/CakePHP-DE) - 德国聚会。

## 脚注
Awesome-cakephp 由 [dereuromark](https://github.com/dereuromark) 创建，目前由他和 FriendsOfCake 小组维护。也感谢所有[贡献者](https://github.com/FriendsOfCake/awesome-cakephp/graphs/contributors)。
