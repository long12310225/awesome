# 很棒的 Laravel [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

> 来自 Laravel 生态系统的精彩书签、包、教程、视频和其他酷资源的精选列表。

灵感来自 [ziadoz/awesome-php](https://github.com/ziadoz/awesome-php)

## 目录

- [Essentials](#essentials)
- [Packages](#packages)
- [热门套餐](#popular-packages)
- [开发设置](#development-setup)
- [应用程序托管](#application-hosting)
- [应用部署](#application-deployment)
- [代码片段](#code-snippets)
- [教程和博客](#tutorials--blogs)
- [Videos](#videos)
- [Conferences](#conferences)
- [Books](#books)
- [入门项目](#starter-projects)
- [参考代码库](#codebases-for-reference)
- [内容管理系统](#content-management-systems)
- [Podcasts](#podcasts)
- [Community](#community)
- [Jobs](#jobs)
- [托管开发工具](#hosted-development-tools)
- [Miscellaneous](#miscellaneous)

## 必需品

* [Laravel](https://laravel.com) ([文档](https://laravel.com/docs))
* [Laravel API 参考](https://laravel.com/api/master/)
* [流明](https://lumen.laravel.com) ([文档](https://lumen.laravel.com/docs))
* [Laracasts](https://laracasts.com)
* [Laravel 新闻](https://laravel-news.com) ([存档](https://laravel-news.com/archive/))

## 套餐

* [Packagist](https://packagist.org/)
* [Laravel 集体](https://laravelcollective.com/)
* [Packalyst](http://packalyst.com/)
* [Spatie](https://spatie.be/en/opensource/laravel)

## 热门套餐

> 这是 Laravel 项目中经常使用的记录良好、经过测试的包的列表。如果您正在寻找 PHP 软件包的详尽列表，请查看上面提到的软件包存储库。

##### 开发者工具

* [Scaffold Interface](https://github.com/amranidev/scaffold-interface) - Laravel 的智能 CRUD 生成器
* [IDE Helper](https://github.com/barryvdh/laravel-ide-helper) - 生成 IDE 自动完成的帮助文件
* [Laravel 5 Extended Generators](https://github.com/laracasts/Laravel-5-Generators-Extended) - 扩展内置文件生成器
* [Laravel API/Scaffold/CRUD Generator](https://github.com/InfyOmLabs/laravel-generator) - API、CRUD 脚手架等的生成器。
* [Laravel Tinx](https://github.com/furey/tinx) - 从 Tinker 内部重新加载 Laravel Tinker 会话
* [Laravel API Documentation Generator](https://github.com/mpociot/laravel-apidoc-generator) - 自动生成您的API文档
* [Laravel Packager](https://github.com/Jeroen-G/Laravel-Packager) - 用于创建 Laravel 包的 CLI 工具
* [Workbench Export to Migrations](https://github.com/beckenrode/mysql-workbench-export-laravel-5-migrations) - 用于将模型导出到 Laravel 迁移的工作台插件
* [Laravel Decomposer](https://github.com/lubusIN/laravel-decomposer) - 列出所有已安装的软件包、它们的依赖项、应用程序和服务器详细信息
* [LaRecipe](https://github.com/saleem-hadad/larecipe) - 在 Laravel 应用程序中使用 Markdown 为您的产品编写精美的文档。
* [Prequel](https://github.com/Protoqol/Prequel/) - 为 Laravel 调整的清晰简洁的数据库管理 GUI。

##### 测试与调试

* [Laravel TestTools](https://chrome.google.com/webstore/detail/laravel-testtools/ddieaepnbjhgcbddafciempnibnfnakl) - Chrome 扩展程序可在使用您的应用程序时生成 Laravel 集成测试
* [Laravel Test Factory Generator](https://github.com/mpociot/laravel-test-factory-helper) - 从现有模型生成 Laravel 测试工厂
* [Clockwork](https://github.com/itsgoingd/clockwork) - 集成 Clockwork Chrome 扩展，用于调试和分析应用程序
* [Debug Bar](https://github.com/barryvdh/laravel-debugbar) - 将 PHP 调试栏与 Laravel 集成
* [Ignition](https://github.com/facade/ignition) - Laravel 应用程序的漂亮错误页面
* [Laravel 5 Log Viewer](https://github.com/rap2hpoutre/laravel-log-viewer) - 日志查看器
* [LogViewer](https://github.com/ARCANEDEV/LogViewer) - 提供日志查看器
* [LERN](https://github.com/tylercd100/lern#lern-laravel-exception-recorder-and-notifier) - 将异常情况记录到数据库中并向您发送通知
* [Mail Preview](https://github.com/themsaid/laravel-mail-preview) - 在网络浏览器或邮件客户端中预览发送的邮件
* [Laravel Tracy](https://github.com/recca0120/laravel-tracy) - 用于集成 Nette Tracy 调试器的 Laravel 包
* [Laravel Terminal](https://github.com/recca0120/laravel-terminal) - 在网络浏览器中运行 artisan
* [Laravel API Tester](https://github.com/asvae/laravel-api-tester) - 类似 Postman 的 Laravel 路由工具
* [Laravel Tail](https://github.com/spatie/laravel-tail) - 缺少尾部命令
* [Laravel Telescope](https://github.com/laravel/telescope) - Laravel Telescope 是 Laravel 框架的优雅调试助手

##### 认证与授权

* [Bouncer](https://github.com/JosephSilber/bouncer) - 角色和权限
* [Laratrust](https://github.com/santigarcor/laratrust) - 角色、权限和团队
* [Entrust](https://github.com/Zizaco/entrust) - 基于角色的权限
* [JWT Auth](https://github.com/tymondesigns/jwt-auth) - API 的 JSON Web 令牌身份验证
* [Laravel Permission](https://github.com/spatie/laravel-permission) - 将用户与角色和权限关联起来
* [Defender](https://github.com/artesaos/defender) - 角色和权限
* [OAuth2 Server Laravel](https://github.com/lucadegasperi/oauth2-server-laravel) - OAuth 2.0授权服务器和资源服务器
* [Socialite](https://github.com/laravel/socialite) - 使用 Facebook、Google、Twitter 等进行 OAuth 身份验证。
* [Socialite Providers 2.0](http://socialiteproviders.github.io/) - 100 多个社交认证提供商为社交名流提供 Lumen 支持
* [Google2FA](https://github.com/antonioribeiro/google2fa) - 谷歌双因素身份验证模块
* [Laravel User Verification](https://github.com/jrean/laravel-user-verification) - 处理用户验证流程并验证电子邮件
* [Adldap2 Laravel](https://github.com/Adldap2/Adldap2-Laravel) - LDAP 身份验证和 Active Directory 管理
* [Doorman](https://github.com/clarkeash/doorman) - 使用邀请码限制对 Laravel 应用程序的访问
* [Laravel Heyman](https://github.com/imanghafoori1/laravel-heyman) - Heyman 继续上述角色权限包的内容

##### 公用事业

* [Awes.io](https://github.com/awes-io/awes-io) - 基于 Vue (Nuxt.js)、TailwindCSS 和 Laravel 作为后端的 CRM、SaaS、ERP 的样板。
* [Artisan View](https://github.com/svenluijten/artisan-view) - 通过 artisan 管理 Laravel 项目中的视图
* [Bootstrapper](https://github.com/patricktalmadge/bootstrapper/) - 用于创建 Bootstrap 3 标记的类集
* [Captcha](https://github.com/mewebstudio/captcha) - 反机器人图像验证码系统
* [Charts](https://github.com/ConsoleTVs/Charts) - 多库图表包，用于创建交互式图表
* [Lavacharts](https://github.com/kevinkhill/lavacharts) - 由 Google Chart API 提供支持的 PHP 图表和图形
* [Eloquent Filter](https://github.com/Tucker-Eric/EloquentFilter) - 过滤器模型及其关系
* [Eloquent Sluggable](https://github.com/cviebrock/eloquent-sluggable) - 为 Eloquent 模型创建 slugs
* [Eloquent Sortable](https://github.com/spatie/eloquent-sortable) - Eloquent 模型的可排序行为
* [HTML](https://github.com/LaravelCollective/html) - Laravel 的 HTML 和表单生成器
* [Multi-tenant](https://github.com/hyn/multi-tenant) - 灵活的多租户，安全分离路由、资产和数据库
* [Laravel Form Builder](https://github.com/kristijanhusak/laravel-form-builder) - 表单生成器的灵感来自 Symfony 的表单生成器
* [Laravel Activitylog](https://github.com/spatie/laravel-activitylog) - 记录 Laravel 应用程序内的活动
* [Laravel Auditing](https://github.com/owen-it/laravel-auditing) - Eloquent 模型的审计
* [Laravel Breadcrumbs](https://github.com/davejamesmiller/laravel-breadcrumbs) - 创建和管理面包屑
* [Laravel Collection Macros](https://github.com/spatie/laravel-collection-macros) - 一组方便的集合宏
* [Laravel Cookie Consent](https://github.com/spatie/laravel-cookie-consent) - 让你的 Laravel 应用程序遵守疯狂的欧盟 cookie 法
* [Laravel Datatables](https://github.com/yajra/laravel-datatables) - jQuery 数据表 API
* [Laravel GeoIP](https://github.com/Torann/laravel-geoip) - 根据 IP 地址确定网站访问者的位置
* [Laravel Hashids](https://github.com/vinkla/laravel-hashids) - 使用 [Hashids](http://hashids.org/php/) 生成唯一的、非连续的 id
* [Laravel Impersonate](https://github.com/404labfr/laravel-impersonate) - 用于验证您的用户之一的包
* [Laravel Mailbox](https://github.com/beyondcode/laravel-mailbox) - 处理传入电子邮件的包
* [Laravel Markdown](https://github.com/GrahamCampbell/Laravel-Markdown) - CommonMark 降价解析器
* [Laravel Menu](https://github.com/spatie/laravel-menu) - Laravel 的 Html 菜单生成器
* [Laravel Talk](https://github.com/nahid/talk) - 实时用户消息系统
* [Laravel Messenger](https://github.com/cmgmyr/laravel-messenger) - 用户消息系统
* [Laravel Moderation](https://github.com/hootlex/laravel-moderation) - 批准或拒绝帖子、评论、用户等资源。
* [Laravel Tags](https://github.com/spatie/laravel-tags) - 添加标签和可标记行为
* [Laravel Stats Tracker](https://github.com/antonioribeiro/tracker) - 从请求中收集信息以进行识别和存储
* [Listify](https://github.com/lookitsatravis/listify) - 向任何 Eloquent 模型添加排序/排序功能
* [noCAPTCHA](https://github.com/ARCANEDEV/noCAPTCHA) - Google 新的 noCAPTCHA (reCAPTCHA) 助手
* [Purifier](https://github.com/mewebstudio/purifier) - HTML过滤器
* [Revisionable](https://github.com/VentureCraft/revisionable) - 创建 Eloquent 模型的修订历史记录
* [SEOTools](https://github.com/artesaos/seotools) - 一些常见 SEO 技术的助手
* [Page Cache](https://github.com/JosephSilber/page-cache) - 将响应缓存为磁盘上的静态文件，以实现闪电般的快速页面加载
* [Laravel Setting](https://github.com/anlutro/laravel-settings) - 存储在 JSON 文件中的持久配置设置
* [Friendship](https://github.com/hootlex/laravel-friendships) - 友情管理系统
* [Teamwork](https://github.com/mpociot/teamwork) - 通过邀请系统进行用户与团队关联
* [Validating](https://github.com/dwightwatson/validating) - 用于验证 Eloquent 模型的 Trait
* [VAT Calculator](https://github.com/mpociot/vat-calculator) - 处理与 EU MOSS 增值税法规相关的所有难题
* [Laravel UUID](https://github.com/webpatser/laravel-uuid) - 根据RFC 4122标准生成UUID
* [Laravel Installer](https://github.com/RachidLaasri/LaravelInstaller) - 允许用户只需按照安装向导安装您的应用程序，例如 WordPress
* [Laravel Modules](https://github.com/nWidart/laravel-modules) - 轻松的模块管理
* [Laravel Phone](https://github.com/Propaganistas/Laravel-Phone) - 电话号码验证器和格式化器
* [Laravel Ban](https://github.com/cybercog/laravel-ban) - 简化屏蔽和禁止 Eloquent 模型
* [Laravel Proxy](https://github.com/fideloper/TrustedProxy) - 在负载均衡器或其他中介后面处理会话。
* [Laravel Video Chat](https://github.com/PHPJunior/laravel-video-chat) - 使用 Socket.IO 和 WebRTC 进行视频聊天
* [Widgets for Laravel](https://github.com/arrilot/laravel-widgets) - 查看作曲家的强大替代方案。
* [Secure Headers](https://github.com/BePsvPT/secure-headers) - 将安全相关标头添加到 HTTP 响应
* [Laravel Nova](https://nova.laravel.com/) - Nova 是 Laravel 设计精美的管理面板
* [Laravel Love](https://github.com/cybercog/laravel-love) - 它让人们表达他们对内容的感受。对 Eloquent 模型做出喜欢或不喜欢的反应。
* [stancl/tenancy](https://github.com/stancl/tenancy) - 自动租赁您的 Laravel 应用程序。无需更改代码。

##### 媒体和文档管理

* [Intervention Image](https://github.com/Intervention/image) - 用于创建、编辑和合成图像的图像处理库
* [Laravel ImageUp](https://github.com/qcod/laravel-imageup) - 另一个图像处理包，增加了大量额外的功能
* [Laravel Glide](https://github.com/spatie/laravel-glide) - 使用 Glide 轻松转换图像
* [Laravel MediaLibrary](https://github.com/spatie/laravel-medialibrary) - 将文件与 Eloquent 模型关联
* [Laravel Snappy](https://github.com/barryvdh/laravel-snappy) - 使用 wkhtmltopdf 生成 HTML 到 PDF
* [Laravel DOMPDF](https://github.com/barryvdh/laravel-dompdf) - 使用 [dompdf](https://github.com/dompdf/dompdf) 的 HTML 到 PDF 生成器
* [Laravel Stapler](https://github.com/CodeSleeve/laravel-stapler) - 基于ORM的文件上传管理器
* [Laravel Excel](https://github.com/Maatwebsite/Laravel-Excel) - 导入和导出 Excel 和 CSV 文件
* [Fast Excel](https://github.com/rap2hpoutre/fast-excel) - Laravel 的快速 XLSX、CSV 和 ODT 导入和导出
* [Laravolt Avatar](https://github.com/laravolt/avatar) - 即插即用头像，将姓名、电子邮件和任何其他字符串变成漂亮的头像（或头像），毫不费力。
* [Laravel FFmpeg](https://github.com/pascalbaljetmedia/laravel-ffmpeg) - 该软件包为 Laravel 5.8 提供了与 FFmpeg 的集成。

##### 与 JavaScript 集成

* [Laroute](https://github.com/aaronlord/laroute) - 从 JavaScript 生成 Laravel 路由 URL
* [PHP Vars to JavaScript Transformer](https://github.com/laracasts/PHP-Vars-To-Js-Transformer) - 将服务器端字符串/数组/集合/任何内容传递给 JavaScript
* [Javascript Validation](https://github.com/proengsoft/laravel-jsvalidation) - 使用验证规则、消息、FormRequest 和验证器来验证客户端的表单
* [Laravel Pjax](https://github.com/spatie/laravel-pjax) - Pjax中间件
* [Laravel Blade Javascript](https://github.com/spatie/laravel-blade-javascript) - 将变量导出到 JavaScript 的 Blade 指令
* [Ziggy](https://github.com/tightenco/ziggy) - 在 JavaScript 中使用 Laravel 命名路由
* [LiveWire](https://github.com/livewire/livewire) - 一个神奇的 Laravel 前端框架

##### 数据库、ORM、迁移和播种

* [Backup Manager](https://github.com/backup-manager/laravel) - 从 S3、Dropbox、SFTP 等备份和恢复数据库。
* [Laravel Nestedset](https://github.com/lazychaser/laravel-nestedset) - 嵌套集模式实现
* [ClosureTable](https://github.com/franzose/ClosureTable) - 闭包表模式实现
* [Eloquence](https://github.com/kirkbushell/eloquence) - Eloquent 模型的额外功能
* [iSeed](https://github.com/orangehill/iseed) - 从现有数据库表生成新的种子文件
* [Laravel OCI8](https://github.com/yajra/laravel-oci8) - 通过 OCI8 的 Oracle DB 驱动程序
* [Laravel Backup](https://github.com/spatie/laravel-backup) - 备份您的应用程序
* [Laravel Doctrine](https://github.com/laravel-doctrine/orm) - 原则 2 ORM 实现
* [Laravel MongoDB](https://github.com/jenssegers/laravel-mongodb) - 支持 MongoDB 的 Eloquent 模型和查询构建器
* [Migrations Generator](https://github.com/Xethron/migrations-generator) - 从现有数据库生成迁移
* [Sofa/Eloquence](https://github.com/jarektkaczyk/eloquence) - Eloquent ORM 的扩展
* [Tenanti](https://github.com/orchestral/tenanti) - 多租户数据库模式管理器
* [Laravel Repository](https://github.com/andersao/l5-repository) - 用于抽象数据库层的存储库
* [Lada Cache](https://github.com/spiritix/lada-cache) - 基于 Redis 的完全自动化且可扩展的数据库缓存层
* [Laravel MySQL Spatial extension](https://github.com/grimzy/laravel-mysql-spatial) - 轻松使用 MySQL Spatial 数据类型和 MySQL Spatial 函数

##### 搜索

* [Algolia Search](https://github.com/algolia/algoliasearch-laravel) - 将 Algolia 搜索 API 集成到 Laravel Eloquent ORM
* [Elasticquent](https://github.com/elasticquent/Elasticquent) - Elasticsearch 用于 Eloquent 模型
* [Plastic](https://github.com/sleimanx2/plastic) - 流畅地映射和搜索 Elasticsearch
* [Laravel Search](https://github.com/mmanos/laravel-search) - Elasticsearch、Algolia 和 ZendSearch 的统一 API
* [SearchIndex](https://github.com/spatie/searchindex) - 从 Algolia 或 Elasticsearch 存储和检索对象
* [Searchable](https://github.com/nicolaslopezj/searchable) - 为 Eloquent 模型添加简单搜索功能的 Trait
* [TNTSearch](https://github.com/teamtnt/tntsearch) - 用 PHP 编写的功能齐全的全文搜索引擎
* [TNTSearch driver](https://github.com/teamtnt/laravel-scout-tntsearch-driver) - 基于 TNTSearch 的 [Laravel Scout](https://github.com/laravel/scout) 搜索包驱动
* [Laravel-Searchy](https://github.com/TomLingham/Laravel-Searchy) - 模糊搜索、基本字符串匹配、编辑距离

##### API

* [ApiGuard](https://github.com/chrisbjr/api-guard) - 允许使用 API 密钥进行 API 身份验证
* [Dingo API](https://github.com/dingo/api) - 用于开发 RESTful API 的多用途工具包
* [Laravel CORS](https://github.com/barryvdh/laravel-cors) - 添加 CORS（跨源资源共享）标头支持
* [Laravel Fractal](https://github.com/spatie/laravel-fractal) - 使用 Fractal 输出复杂、灵活、AJAX/RESTful 数据结构
* [Laravel GraphQL](https://github.com/rebing/graphql-laravel) - 支持 Relay、eloquent 模型、验证和 GraphiQL
* [Lighthouse](https://github.com/nuwave/lighthouse) - 即将推出的 Laravel GraphQL 库
* [Laravel Responder](https://github.com/flugger/laravel-responder) - 使用 Fractal 构建自定义 API 响应

##### 任务、命令和调度

* [Dispatcher](https://github.com/indatus/dispatcher) - Artisan 命令的调度程序
* [Elixir](https://github.com/laravel/elixir) - 用于运行 Gulp 任务的 Node (NPM) 包
* [Mix](https://github.com/JeffreyWay/laravel-mix) - 用于定义基本 webpack 构建步骤的 Fluent API
* [Envoy](https://github.com/laravel/envoy) - SSH 任务运行程序

##### 付款方式

* [Cashier](https://github.com/laravel/cashier) - 使用 Stripe 进行订阅计费
* [Omnipay for Laravel](https://github.com/ignited/laravel-omnipay) - 集成 [Omnipay](https://github.com/thephpleague/omnipay) PHP 库

##### 优化

* [Intervention Image Cache](https://github.com/Intervention/imagecache) - 干预图像类的缓存扩展
* [Laravel HTMLMin](https://github.com/GrahamCampbell/Laravel-HTMLMin) - Blade/HTML/CSS/javascript 压缩器
* [Rememberable](https://github.com/dwightwatson/rememberable) - Eloquent 的查询缓存
* [Widgetize](https://github.com/imanghafoori1/laravel-widgetize) - 页面部分缓存
* [Laravel Responsecache](https://github.com/spatie/laravel-responsecache) - 通过缓存整个响应来加速应用程序

##### 监控

* [Horizon](https://github.com/laravel/horizon) - 使用简单的 Web UI 监控和配置队列
* [Laravel Failed Job Monitor](https://github.com/spatie/laravel-failed-job-monitor) - 当排队作业失败时收到通知
* [Laravel Uptime Monitor](https://github.com/spatie/laravel-uptime-monitor) - 功能强大且易于配置的正常运行时间和 ssl 监视器
* [Larametrics](https://github.com/aschmelyun/larametrics) - 适用于 Laravel 应用程序的自托管指标和通知平台

##### 本地化

* [Language Files](https://github.com/caouecs/Laravel-lang) - 37 种语言的验证、分页和提醒语言行
* [Laravel Localization](https://github.com/mcamara/laravel-localization) - 通过路由添加 i18n 支持
* [Laravel Translatable](https://github.com/spatie/laravel-translatable) - 通过将翻译存储为 JSON 来使 Eloquent 模型可翻译
* [Laravel Translatable](https://github.com/dimsav/laravel-translatable) - 检索并存储可翻译的 Eloquent 模型实例
* [Laravel Translator](https://github.com/vinkla/laravel-translator) - 将 Eloquent 模型翻译成多种语言
* [Laravel Date](https://github.com/jenssegers/date) - 一个基于 Carbon 的库，可帮助您处理多种语言的日期
* [Laravel Langman](https://github.com/themsaid/laravel-langman) - 从 Artisan Console 管理语言文件
* [Laravel Translation](https://github.com/waavi/translation) - 翻译和本地化管理
* [Linguist](https://github.com/keevitaja/linguist) - Laravel 的 i18n 本地化支持

##### 第三方服务集成

* [Laravel Analytics](https://github.com/spatie/laravel-analytics) - 从 Google Analytics 检索浏览量和其他数据
* [Laravel DigitalOcean](https://github.com/GrahamCampbell/Laravel-DigitalOcean) - DigitalOceanV2桥
* [Laravel GitHub](https://github.com/GrahamCampbell/Laravel-GitHub) - PHP GitHub API 桥
* [Laravel Instagram](https://github.com/vinkla/laravel-instagram) - Instagram API 桥
* [Laravel Newsletter](https://github.com/spatie/laravel-newsletter) - 使用 Mailchimp 发送新闻通讯
* [Laravel Pusher](https://github.com/vinkla/laravel-pusher) - Pusher API 桥

## 开发设置

* [Homestead](https://laravel.com/docs/master/homestead) - Laravel 官方 Vagrant 盒子
* [Valet](https://laravel.com/docs/master/valet) - Mac用户的开发环境
* [Valet Linux](https://github.com/cpriego/valet-linux) - Linux用户的开发环境
* [LaraDock](https://github.com/LaraDock/laradock) - 在 Docker 上运行 Laravel（类似于 Homestead，但用于 Docker 而不是 Vagrant）
* [LaraEdit Docker](https://github.com/laraedit/laraedit-docker) - 单个 Docker 容器中的 Homestead 环境
* [Laragon](https://laragon.org/) - Windows 上的隔离开发环境
* [Stacker](https://github.com/Maxlab/stacker) - Docker上的本地Web开发环境
* [Devilbox](https://github.com/cytopia/devilbox) - 适用于每个 PHP 版本的 dockerized 通用 LAMP/MEAN 堆栈
* [Vessel](https://vessel.shippingdocker.com) - Laravel 的简单 Docker 开发环境
* [Lando](https://docs.lando.dev/config/laravel.html) - 基于Docker构建的本地开发环境工具

## 应用程序托管

* [Vapor](https://vapor.laravel.com)
* [Forge](https://forge.laravel.com/) ([ForgeRecipes](https://forgerecipes.com/))
* [FortRabbit](https://www.fortrabbit.com/laravel-hosting)
* [Heroku](https://www.heroku.com/) ([文档](https://devcenter.heroku.com/articles/getting-started-with-laravel))
* [AWS Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/) ([教程](http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/php-laravel-tutorial.html))
* [Cloudways](https://www.cloudways.com/en/laravel-hosting.php)
* [Ploi](https://ploi.io/)
* [CodePier](https://codepier.io?ref=awesome-laravel)
* [RunCloud](https://runcloud.io/)

## 应用部署

* [Deployer](https://deployer.org/) - 开箱即用的支持 Laravel 的部署工具
* [Envoyer](https://envoyer.io/) - 适用于 PHP 和 Laravel 项目的零停机部署程序
* [Rocketeer](https://github.com/rocketeers/rocketeer) - 任务运行器和部署包

## 代码片段

* [Laravel LTS 备忘单](https://summerblue.github.io/laravel5-cheatsheet/) ([中文版](https://cs.phphub.org/))
* [Laravel 技巧](http://laravel-tricks.com/)

## 教程和博客

* [泰勒·奥特威尔](http://taylorotwell.com/)
* [Tuts+](https://code.tutsplus.com/categories/laravel)
* [Medium](https://medium.com/tag/laravel/latest)
* [Laravel 日报](https://laraveldaily.com/)
* [Scotch](https://scotch.io/tag/laravel)
* [数字海洋](https://www.digitalocean.com/community/search?q=laravel&primary_filter=newest&type=tutorials)
* [马特·斯托弗](https://mattstauffer.co/blog)
* [素食比特](https://vegibit.com/tag/laravel/)
* [霓虹海啸](https://www.neontsunami.com/tags/laravel)
* [Dor.ky](https://dor.ky/tag/laravel/)
* [Stillat](https://stillat.com/explore/categories/laravel-5)
* [简单的 Laravel 图书博客](http://www.easylaravelbook.com/blog/)
* [Laraveles](http://laraveles.com/blog/) (ES)
* [Styde](https://styde.net/category/laravel-5/) (ES)
* [Cloudways Laravel 博客](http://cloudways.com/blog/laravel)
* [Laravel 最佳实践](https://github.com/alexeymezenin/laravel-best-practices)
* [Pusher Laravel 教程](https://pusher.com/tutorials?tag=Laravel)
* [LaraShout](https://larashout.com/)

## 视频

* [Laracasts](https://laracasts.com/)
* [Codecourse](https://www.codecourse.com/) ([YouTube](https://www.youtube.com/user/phpacademy/playlists))
* [Tuts+](http://code.tutsplus.com/categories/laravel/courses)
* [黑客服务器](https://serversforhackers.com/laravel-perf)
* [测试驱动的 Laravel](https://course.testdrivenlaravel.com/)
* [Duilio Palacios](https://www.youtube.com/user/silencedsg/videos) (ES)
* [CodigoFacilito](https://codigofacilito.com/courses/laravel) (ES)
* [DevDojo](https://devdojo.com/search?value=laravel)
* [阿米塔夫·罗伊](https://www.youtube.com/channel/UC4gijXR8cM4gmEt9Olse-TQ/videos)
* [Laracademy](https://laracademy.co/)
* [开发营销人员](https://www.youtube.com/channel/UC6kwT7-jjZHHF1s7vCfg2CA/playlists)
* [Udemy](https://www.udemy.com/courses/search/?q=laravel)
* [Lynda](https://www.lynda.com/search?q=laravel)
* [Pluralsight](https://www.pluralsight.com/search?q=laravel&categories=course)
* [Bitfumes](https://www.youtube.com/bitfumes)
* [ConfidentLaravel](https://confidentlaravel.com/)

## 会议

* [拉拉康美国](http://laracon.us/)
* [拉拉康欧盟](http://laracon.eu/)
* [拉拉康在线](https://laracon.net/)
* [Laraconf 巴西](http://laraconfbrasil.com.br/)
* [澳大利亚](https://laracon.com.au/)
* [Laravel Live 英国](https://laravellive.uk/)
* [Laravel 现场印度](https://laravellive.in/)
* [Laravel 尼日利亚](https://laravelnigeria.com)

##### 视频

* [Laracon 欧盟 2018](https://www.youtube.com/playlist?list=PLMdXHJK-lGoC64wnqvm6v1R5dsuAV-MpS)
* [Laracon 美国 2018](https://www.youtube.com/playlist?list=PL-yJve--iT5oM2LgF37VXsBb8Os4ZulIc)
* [Laracon 欧盟 2017](https://www.youtube.com/playlist?list=PLMdXHJK-lGoBFZgG2juDXF6LiikpQeLx2)
* [Laracon 美国 2017](https://www.youtube.com/playlist?list=PL-yJve--iT5oaLQA6OI8TWLVSOBP1qhs3)
* [Laracon 欧盟 2016](https://www.youtube.com/playlist?list=PLMdXHJK-lGoCMkOxqe82hOC8tgthqhHCN)
* [Laracon 美国 2016](https://www.youtube.com/playlist?list=PL-yJve--iT5o9fH_cRY0u6P751pcF59GK)
* [Laracon 欧盟 2015](https://www.youtube.com/playlist?list=PLMdXHJK-lGoA9SIsuFy0UWL8PZD1G3YFZ)
* Laracon 美国 2015
* [Laracon 欧盟 2014](https://www.youtube.com/playlist?list=PLMdXHJK-lGoCYhxlU3OJ5bOGhcKtDMkcN)
* [Laracon 美国 2014](https://www.youtube.com/channel/UCRawXmZv30Vf_MivyPYb_GQ/videos)
* [Laracon 欧盟 2013](https://www.youtube.com/playlist?list=PLMdXHJK-lGoB-CIVsiQt0WU8WcYrb5eoe)
* [Laracon 美国 2013](https://www.youtube.com/playlist?list=PLkwAlZpjHQbLcox_S_AgGU24QUfKgXayN)

## 书籍

* [Laravel 入门](https://www.amazon.com/Laravel-Starter-Shawn-McCool-ebook/dp/B00ABFQ0AS) 作者：Shawn McCool
* [Laravel：快乐代码](https://leanpub.com/codehappy) 作者：Dayle Rees
* [Laravel: Code Bright](https://leanpub.com/codebright) 作者：Dayle Rees
* [Laravel：智能代码](https://leanpub.com/codesmart) 作者：Dayle Rees
* [Laravel：从学徒到工匠](https://leanpub.com/laravel) 作者：Taylor Otwell
* [Laravel 4 Cookbook](https://leanpub.com/laravel4cookbook) 作者：Christopher Pitt 和 Taylor Otwell
* [Laravel 测试解码](https://leanpub.com/laravel-testing-decoded) 作者：Jeffrey Way
* [重构到集合](https://adamwathan.me/refactoring-to-collections/) 作者：Adam Wathan
* [实现 Laravel](https://leanpub.com/implementinglaravel) 作者：Chris Fidao
* [使用 Laravel 4 完成工作](https://leanpub.com/gettingstuffdonelaravel) 作者：Chuck Heintzelman
* [Laravel 应用程序开发蓝图](https://www.packtpub.com/web-development/laravel-application-development-blueprints)，作者：Arda Kılıçdağı 和 Halil ibrahim Yılmaz
* [构建你不会讨厌的 API](https://leanpub.com/build-apis-you-wont-hate) 作者：Phil Sturgeon
* [将前端组件与 Web 应用程序集成](https://leanpub.com/frontend) 作者：Maksim Surguy
* [Laravel 设计模式和最佳实践](https://www.packtpub.com/web-development/laravel-design-patterns-and-best-practices) 作者：Arda Kılıçdağı 和 Halil ibrahim Yılmaz
* [学习 Laravel 4 应用程序开发](https://www.packtpub.com/web-development/learning-laravel-4-application-development) 作者：Hardik Dangar
* [Laravel 4 入门](https://www.packtpub.com/web-development/getting-started-laravel-4) 作者：Raphaël Saunier
* [Laravel 应用程序开发手册](https://www.packtpub.com/web-development/laravel-application-development-cookbook) 作者：Terry Matula
* [使用 Parse REST API 构建 Web 应用程序](https://leanpub.com/building-web-applications-using-parse-rest-api) 作者：Mhd Zaher Ghaibeh
* [Laravel - 我的第一个框架](https://leanpub.com/laravel-first-framework) 作者：Maksim Surguy
* [Easy Laravel 5](https://leanpub.com/easylaravel/) 作者：W. Jason Gilmore
* [Laravel 5 Essentials](https://www.packtpub.com/web-development/laravel-5-essentials) 作者：Martin Bean
* [使用 Laravel 和 Stripe 的轻松电子商务](https://leanpub.com/easyecommerce) 作者：W. Jason Gilmore 和 Eric L. Barnes
* [Laravel 5.1 Beauty](https://leanpub.com/l5-beauty) 作者：Chuck Heintzelman
* [使用 PHP 和 Laravel 的设计模式](https://leanpub.com/larasign) 作者：Kelt Dockins
* [掌握 Laravel](https://www.packtpub.com/web-development/mastering-laravel) 作者：Christopher John Pecoraro
* [如何使用 Pusher 构建实时 Laravel 应用程序](http://pusher-community.github.io/real-time-laravel/) by Pusher
* [学习 Laravel 的 Eloquent](https://www.amazon.com/Learning-Laravels-Eloquent-Francesco-Malatesta-ebook/dp/B00YSILQ6C) 作者：Francesco Malatesta
* [Laravel 5 轻松学习](https://leanpub.com/laravel5learneasy) 作者：Sanjib Sinha
* [Laravel 和 AngularJS](https://leanpub.com/laravel-and-angularjs) 作者：Daniel Schmitz 和 Daniel Pedrinha Georgii
* [Laravel Collections Unraveled](https://leanpub.com/laravelcollectionsunraveled) 作者：Jeff Madsen
* [使用 Lumen 编写 API](https://leanpub.com/lumen-apis) 作者：Paul Redmond
* [Laravel 生存指南](https://leanpub.com/laravelsurvivalguide) 作者：Tony Lea
* [Laraboot：Laravel 5 初学者](https://leanpub.com/laravel-5-for-beginners-laraboot) 作者：Bill Keck
* [Laravel 5.4 初学者](https://leanpub.com/laravel-5-4-for-beginners) 作者：Bill Keck
* [Laravel 启动和运行](https://www.amazon.com/gp/product/1491936088) 作者：Matt Stauffer
* [Laravel Companion](https://leanpub.com/laravelcompanion-secondedition) 作者：Johnathon Koster
* [使用 CloudFormation 在 AWS 上部署 Laravel](https://leanpub.com/laravel-aws) 作者：Lionel Martin
* [React Native 和 Laravel 用于未来移动开发](https://leanpub.com/rn_laravel) 作者：Ega Radiegtya
* [黑客服务器](https://book.serversforhackers.com) 作者：Chris Fidao
* [全栈 Vue.js 2 和 Laravel 5](https://www.amazon.com/Full-Stack-Vue-js-Laravel-frontend-together/dp/1788299582) 作者：Anthony Gore
* [使用 Laravel 构建 API](https://buildanapi.com) 由 Wacky Studio 提供

## 入门项目

* [Spark](https://spark.laravel.com/)
* [LaraAdmin](https://github.com/dwijitsolutions/laraadmin)
* [石墨生成器](https://github.com/GrafiteInc/Builder)
* [Laravel 样板文件](https://github.com/rappasoft/laravel-5-boilerplate)
* [Laravel Angular 材质入门](https://github.com/jadjoubran/laravel5-angular-material-starter)
* [AdminLTE Laravel](https://github.com/acacha/adminlte-laravel)
* [Laravel 黑客马拉松入门者](https://github.com/unicodeveloper/laravel-hackathon-starter)
* [Laravel API 入门套件](https://github.com/joselfonseca/laravel-api)
* [Laravel 背包](https://github.com/Laravel-Backpack/Base)
* [SomelineStarter](https://github.com/someline/someline-starter)
* [Laravel 管理员](https://github.com/z-song/laravel-admin)
* [Voyager](https://github.com/the-control-group/voyager)
* [Orchid](https://github.com/TheOrchid/Platform)
* [Laravel REST API 样板](https://github.com/francescomalatesta/laravel-api-boilerplate-jwt)
* [你好API](https://github.com/Porto-SAP/Hello-API)
* [REST API 与 Lumen](https://github.com/hasib32/rest-api-with-lumen)
* [Laravel Zero - 控制台应用程序](https://github.com/laravel-zero/laravel-zero)
* [Apiato](https://github.com/apiato/apiato)
* [Laravel 管理面板](https://github.com/viralsolani/laravel-adminpanel)
* [Laravel Vue 样板](https://github.com/alefesouza/laravel-vue-boilerplate)
* [拉拉维尔·恩索](https://github.com/laravel-enso/enso)
* [Laravel 模板与 Vue](https://github.com/wmhello/laravel_template_with_vue)

## 参考代码库

* [Cachet](https://github.com/cachethq/Cachet) - 网站和 API 的状态页面系统
* [Deployer](https://github.com/REBELinBLUE/deployer) - 应用部署系统
* [GitScrum](https://github.com/renatomarinho/laravel-gitscrum) - 使用 Git 和 Scrum 进行任务管理
* [Invoice Ninja](https://github.com/invoiceninja/invoiceninja) - 发票、费用和时间跟踪应用程序
* [Koel](https://github.com/phanan/koel) - 个人音乐流媒体服务器
* [Laravel.io](https://github.com/laravelio/portal) - Laravel.io 社区门户的来源
* [Attendize](https://github.com/Attendize/Attendize) - 门票销售和活动管理平台
* [Antvel](https://github.com/ant-vel/App) - 电商平台
* [Jigsaw](https://github.com/tightenco/jigsaw) - 静态站点生成器
* [Canvas](https://github.com/cnvs/canvas) - Laravel 发布平台
* [Vuedo](https://github.com/Vuedo/vuedo) - Vuedo 是博客平台，使用 Laravel 和 Vue.js 构建
* [Screeenly](https://github.com/stefanzweifel/screeenly) - 通过 API 创建网站屏幕截图
* [Voten](https://github.com/voten-co/voten) - 21 世纪的实时社交书签
* [Monica](https://github.com/monicahq/monica) - 个人关系管理系统
* [Snipe-IT](https://github.com/snipe/snipe-it) - IT资产/许可证管理系统
* [Akaunting](https://github.com/akaunting/akaunting) - 适合小型企业和自由职业者的会计软件
* [Torch](https://github.com/mattstauffer/Torch) - 在非 Laravel 应用程序中使用每个 Illuminate 组件的示例
* [Pixelfed](https://github.com/pixelfed/pixelfed) - 一个免费且符合道德的照片共享平台，由 ActivityPub 联盟提供支持


## 内容管理系统

* [OctoberCMS](https://github.com/octobercms/october)
* [SleepingOwlAdmin](https://github.com/LaravelRUS/SleepingOwlAdmin)
* [PyroCMS](https://github.com/pyrocms/pyrocms)
* [Lavalite](https://github.com/LavaLite/cms)
* [TypiCMS](https://github.com/typicms/base)
* [阿斯加德内容管理系统](https://github.com/AsgardCms/Platform)
* [Microweber](https://github.com/microweber/microweber)
* [杯垫CMS](https://github.com/web-feet/coastercms)
* [Statamic](https://statamic.com/)
* [博格特CMS](https://github.com/odirleiborgert/borgert-cms/)
* [睡衣博客](https://github.com/jcc/blog/)
* [Laralum](https://github.com/Laralum/Laralum)
* [Twill](https://github.com/area17/twill)

## 播客

* [Laravel 播客](http://www.laravelpodcast.com/)
* [Laravel 新闻播客](https://laravel-news.com/podcast/ )
* [Laracasts 片段](https://laracasts.simplecast.fm/)
* [Hecho en Laravel（西班牙语）](http://hechoenlaravel.com)

## 社区

* [Laracasts 论坛](https://laracasts.com/discuss)
* [Laravel.io 论坛](http://laravel.io/forum)
* [Larachat Slack](https://larachat.slack.com/) ([注册](https://larachat.co/register))
* [Gitter](https://gitter.im/laravel/laravel)
* [IRC频道](http://laravel.io/chat)
* [StackOverflow](http://stackoverflow.com/questions/tagged/laravel)
* [Twitter](https://twitter.com/laravelphp)
* [Google+](https://plus.google.com/communities/106838454910116161868)
* [Reddit](https://www.reddit.com/r/laravel)
* [Quora](https://www.quora.com/topic/Laravel)
* [Facebook](https://www.facebook.com/LaravelCommunity)
* [LinkedIn](https://www.linkedin.com/groups/4419933/profile)

##### 本地用户组

* [Laravel 全球社区](https://www.facebook.com/groups/group.laravel/)
* [LaravelES Slack](https://laraveles.slack.com) ([注册](http://laraveles.com/blog/wp-login.php?action=slack-invitation))
* [Laravel 印度](https://laravelive.in/)、[Slack注册](https://laraveliveindia.slack.com/join/shared_invite/enQtNjQyMDE4NDA3MDQzLWM yZmIxNGZkNGVkNGFmMzE1MTgyOGNiZGY1ZmU1ZDQ3Mzk2ODBlZGJlODk3ZmI0OWNlZmI5MzQyZDJhYzg1NjE), [Twitter](https://twitter.com/LaravelLiveIN)、[Facebook](https://www.facebook.com/laravellive/)、[Youtube](https://www.youtube.com/channel/UC6TxYSHI7g9FMJ7VlHk72Yg)
* [Laravel 英国](https://laravelphp.uk/), [Slack 注册](https://laravelphp.uk/login/slack)
* [Laravel 俄罗斯](https://laravel.ru/) ([VK group](http://m.vk.com/laravel_rus))
* [Laravel 法国](https://laravel.fr/)
* [Laravel 孟加拉国](https://www.facebook.com/groups/LaravelBanglaDesh/)
* [Laravel 印度尼西亚](http://id-laravel.com/) ([Facebook](https://www.facebook.com/groups/laravel/), [Telegram](https://t.me/laravelindonesia))
* [Laravel 巴西](http://www.laravel.com.br/) ([Facebook](https://www.facebook.com/groups/laravelbrasil/)、[Slack](http://slack.laravel.com.br)、[Telegram](https://telegram.me/laravelbr)、[GitHub](https://github.com/laravelbrasil)、 [不和谐](https://discord.gg/9dpuWeZ))
* [Laravel 土耳其](http://www.laravel.gen.tr/) ([Facebook](https://www.facebook.com/groups/laravelturkiye/))
* [Laravel 尼日利亚](http://www.laravelnigeria.com/) ([Facebook](https://www.facebook.com/groups/laravelnigeria/))
* [Laravel 中国](https://phphub.org/)
* [Laravel 台湾](https://laravel.tw/) ([Facebook](https://www.facebook.com/groups/laravel.tw/))
* [Laravel 西班牙语](http://laraveles.com/foro/)
* [Laravel 韩国](https://www.laravel.co.kr/) ([Facebook](https://www.facebook.com/groups/laravelkorea/))
* [Laravel 日本](http://laravel.jp/) ([Facebook](https://www.facebook.com/groups/laravel.jp/))
* [Laravel 马来西亚](https://www.facebook.com/groups/laravel.my/)
* [Laravel 阿尔及利亚](https://www.facebook.com/groups/LaravelAlgeria/)
* [Laravel 希腊](http://www.laravel.gr) ([Facebook](https://www.facebook.com/laravelgr))
* [Laravel 中东](http://laravelme.com/) ([Facebook](https://www.facebook.com/laravelme))
* [Laravel 格鲁吉亚](https://www.facebook.com/groups/laravel.georgia/)
* [Laravel 意大利](http://laravel-italia.it)
* [Laravel 越南](https://www.facebook.com/groups/vietnam.laravel/)
* [Laravel 斯洛文尼亚](https://www.facebook.com/groups/laravelslovenija/)
* [Laravel 匈牙利](https://laravel.hu)
* [Laravel 喀麦隆](https://laravelcm.com/) ([Slack](https://laravelcm.slack.com)、[GitHub](https://github.com/laravelcm)、[Facebook](https://www.facebook.com/laravelcm)、[Twitter](https://twitter.com/laravelcm))
* [Laravel 菲律宾](https://www.facebook.com/groups/laravelph)

##### 聚会

* [所有聚会](http://www.meetup.com/topics/laravel/)
* [伦敦聚会](https://www.meetup.com/London-Laravel/)
* [布宜诺斯艾利斯聚会](https://www.meetup.com/Laravel-Buenos-Aires/)
* [雅典-希腊聚会](https://www.meetup.com/athens-laravel-meetup/)
* [哥本哈根聚会](https://www.meetup.com/Copenhagen-Laravel-Meetup/)
* [底特律聚会](https://www.meetup.com/Laravel-Detroit/)
* [巴黎聚会](https://www.meetup.com/fr-FR/Paris-Laravel-Meetup/)
* [墨尔本聚会](https://www.meetup.com/Melbourne-laravel-Meetup/)
* [布达佩斯聚会](https://www.meetup.com/Laravel-Hungary-Meetup/)

## 工作机会

* [LaraJobs](https://larajobs.com/)
* [Laravel 大师](https://laravelgurus.com/)

## 托管开发工具

* [Laravel Shift](https://laravelshift.com/) - Laravel 项目的自动升级工具
* [Laravel Schema Designer](http://laravelsd.com/) - 创建、导出和共享数据库模式
* [StyleCI](https://styleci.io) - PHP 编码风格服务

## 杂项

* [CodeCanyon](https://codecanyon.net/tags/laravel?term=laravel) - 付费脚本和插件
* [Laravel Collections](https://laravelcollections.com) - 每个 Laravel 开发人员都转到资源站点
* [LaravelLinks](https://telegram.me/laravellinks) - 致力于分享优秀 Laravel 资源的 Telegram 频道

## 贡献

找到了很棒的软件包、博客、课程或视频？向我发送拉取请求！

#### 指南

* 请为每个建议提出单独的拉取请求
* 确保 Travis 测试通过您的拉取请求
* 使用以下格式作为链接：\[资源\]\(URL\)
* 想要推荐套餐吗？阅读【贡献指南】(https://github.com/chiraggude/awesome-laravel/blob/master/CONTRIBUTING.md)
* 欢迎新类别或对现有类别的改进

## 许可证

[![CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](https://creativecommons.org/licenses/by/4.0/)

Awesome Laravel 已根据 [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/) 获得许可。
