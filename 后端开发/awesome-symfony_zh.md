# 很棒的交响乐 [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
很棒的 [Symfony](http://symfony.com) 捆绑包、实用程序和资源列表。

目录：

* [Administration](#administration)
* [Certification](#certification)
* [Community](#community)
* [Development](#development)
* [Distributions](#distributions)
* [Ecommerce](#ecommerce)
* [Forms](#forms)
* [Internationalization](#internationalization)
* [Miscellaneous](#miscellaneous)
* [Monitoring](#monitoring)
* [付款管理](#payments-management)
* [Queues](#queues)
* [Reading](#reading)
* [Recipes](#recipes)
* [Resources](#resources)
* [服务容器](#service-container)
* [Storage](#storage)
* [模板引擎](#template-engine)
* [第三方API](#third-party-apis)
* [用户管理](#user-management)
* [Validation](#validation)
* [网络服务](#web-services)

## 行政管理

* [AdminCrudBundle](https://github.com/MWSimple/AdminCrudBundle) - AdminCrudBundle - 使用 SensioGeneratorBundle。扩展控制器，添加分页器、过滤器等。
* [AdmingeneratorGeneratorBundle](https://github.com/symfony2admingenerator/AdmingeneratorGeneratorBundle) - Symfony2的Admingenerator，解析generator.yml文件来构建类
* [EasyAdminBundle](https://github.com/javiereguiluz/EasyAdminBundle) - Symfony 应用程序的简单管理生成器
* [SonataAdminBundle](https://github.com/sonata-project/SonataAdminBundle) - AdminBundle - 缺少的 Symfony2 管理生成器
* [AdminLTEBundle](https://github.com/kevinpapst/AdminLTEBundle) - 基于 AdminLTE 模板的管理主题
* [Umbrella framework](https://github.com/acantepie/umbrella) - 用于创建管理后端的管理组件和主题。
* [TablerBundle](https://github.com/kevinpapst/TablerBundle) - 基于 Tabler 模板的管理主题。它附带了许多 twig 助手（函数、过滤器、嵌入、宏和包含）。

## 认证
* [用于培训认证的 CLI 工具](https://github.com/certificationy/certificationy-cli)
* [Symfony 3 认证指南](https://github.com/raulconti/symfony-3-certification-guide)
* [Symfony 认证准备清单](https://github.com/ThomasBerends/symfony-certification-preparation-list)

## 社区

* Facebook - 著名、大型且活跃的 Facebook 群组：
    * [1](https://fb.com/groups/7672226565)
    * [2](https://fb.com/groups/symfony2.framework)
* IRC：
    * [#symfony](http://irc.lc/freenode/symfony) - Symfony 支持的官方 IRC 频道。
    * [#symfony-docs](http://irc.lc/freenode/symfony) - 讨论 Symfony 文档的频道。
* 本地：
    * [Community events](http://symfony.com/events/) - 查找您附近的 Symfony 活动。
    * [Meetup](http://www.meetup.com/topics/symfony/) - 参与本地活动并找到您当地的 Symfony 用户。
* [Telegram](https://telegram.me/symfony_php) - Telegram 上的 Symfony 小组。
* [Quora](https://www.quora.com/topic/Symfony) - Quora 上的 Symfony 主题。
* [Reddit](https://www.reddit.com/r/symfony) - 提出问题并回答问题，进行讨论。
* [SensioLabs Connect](https://connect.sensiolabs.com/login) - 开发社交网络，为您的社区参与和承诺赢得成就。
* [Slack](https://symfony.com/slack-invite) - Symfony on Slack，团队沟通平台。
* [Stack Overflow](http://stackoverflow.com/questions/tagged/symfony2) - Stack Overflow 上的 Symfony 支持。
* [Twitter](https://twitter.com/symfony) - 以类似于 Twitter 的方式了解 Symfony 新闻。

## 发展

* [AccessibleBundle](https://github.com/antares993/AccessibleBundle) - 使用强大的注释定义类的 getter、setter 和构造函数。
* [ApiExceptionBundle](https://github.com/M6Web/ApiExceptionBundle) - 异常 API 包。
* [AvAjaxBundle](https://github.com/AppVentus/AvAjaxBundle) - 这个包提供了一个简单的结构来运行 ajax 操作。
* [BeelabTestBundle](https://github.com/Bee-Lab/BeelabTestBundle) - 该捆绑包仅包含 Symfony WebTestCase 的固执己见的扩展。
* [CacheAdministrationBundle](https://github.com/yamiko-ninja/CacheAdministrationBundle) - 该捆绑包包含一个控制器，具有清除各种缓存的操作。
* [ControllerExtraBundle](https://github.com/mmoreram/ControllerExtraBundle) - 一组有用的控制器注释。
* [DunglasActionBundle](https://github.com/dunglas/DunglasActionBundle) - 基于 Action-Domain-Responder 模式的 Symfony 控制器系统的替代品。
* [http-bundle](https://github.com/iltar/http-bundle) - 提供额外的 HTTP 相关功能。
* [JMSDebuggingBundle](http://jmsyst.com/bundles/JMSDebuggingBundle) - 提供先进的调试工具。
* [LadybugBundle](https://github.com/raulfraile/LadybugBundle) - 简单且可扩展的 PHP 转储程序。
* [LiipCodeBundle](https://github.com/liip/LiipCodeBundle) - 一组 Symfony2 控制台命令，帮助开发人员处理识别类、模板、捆绑包、服务等的各种方式。
* [LiipFunctionalTestBundle](https://github.com/liip/LiipFunctionalTestBundle) - 一些用于在 Symfony 2 中编写功能测试的帮助器类。
* [ListenersDebugCommandBundle](https://github.com/egulias/ListenersDebugCommandBundle) - 用于调试侦听器的控制台命令。
* [ParamConverterBundle](https://github.com/jakzal/ParamConverterBundle) - 该包为 Symfony 提供了额外的参数转换器。
* [PhpMetricsCollectorBundle](https://github.com/phpmetrics/PhpMetricsCollectorBundle) - 将 PhpMetrics 集成到 Symfony2 调试工具栏中。
* [PsyshBundle](https://github.com/theofidry/PsyshBundle) - 提供加载了 Symfony 上下文的增强型 PHP 交互式 shell。
* [PUGXGeneratorBundle](https://github.com/PUGX/PUGXGeneratorBundle) - SensioGeneratorBundle 的增强。
* [redaktilo-bundle](https://github.com/gnugat/redaktilo-bundle) - 将 Redaktilo 集成到 Symfony 2 中。
* [SandboxBundle](https://github.com/danrevah/sandbox-bundle) - 在沙盒环境中覆盖控制器逻辑和响应。
* [StatsDClientBundle](https://github.com/liuggio/StatsDClientBundle) - 通过即用型统计信息轻松监控您的 symfony2 生产环境。
* [TagDebugCommandBundle](https://github.com/egulias/TagDebugCommandBundle) - 集成 TagDebug 库以检查和调试标签。
* [TwigReflectionBundle](https://github.com/arnaud-lb/TwigReflectionBundle) - 显示 Twig 中的内容。
* [WebfactoryExceptionsBundle](https://github.com/webfactory/exceptions-bundle) - 轻松开发自定义的、用户友好的错误页面。
* [WebProfilerExtraBundle](https://github.com/Elao/WebProfilerExtraBundle) - 在 Web Profiler 中添加路由、容器、资产和树枝信息。
* [XhprofBundle](https://github.com/jonaswouters/XhprofBundle) - XHProf 捆绑包。

## 发行版

* [API平台框架](https://github.com/api-platform/api-platform)
* [Kunstmaan 捆绑包标准版](https://github.com/Kunstmaan/KunstmaanBundlesStandardEdition)
* [Symfony CMF 标准版](https://github.com/symfony-cmf/standard-edition)
* [Symfony 标准版](https://github.com/symfony/symfony-standard)

## 电子商务

* [Aimeos](https://aimeos.org/Symfony/) - #gigacommerce 的超快速 PHP 电子商务框架
* [Bamboo](https://github.com/elcodi/bamboo) - 基于 Symfony 和 Elcodi 组件的全栈电子商务应用程序
* [Elcodi](https://github.com/elcodi/elcodi) - 电子商务 PHP 组件和 Symfony 捆绑包
* [Sylius](https://github.com/Sylius/Sylius) - 电子商务 PHP 框架构建在 Symfony 之上，具有基于组件的架构和格式无关的渲染

## 表格

* [CraueFormFlowBundle](https://github.com/craue/CraueFormFlowBundle) - 多步骤形式。
* [InfiniteFormBundle](https://github.com/infinite-networks/InfiniteFormBundle) - 有用的表单类型和扩展的集合。
* [IvoryCKEditorBundle](https://github.com/egeloen/IvoryCKEditorBundle) - Symfony 中的 CKEditor 集成。
* [IvoryOrderedFormBundle](https://github.com/egeloen/IvoryOrderedFormBundle) - 提供表单订购支持。
* [KarserRecaptcha3Bundle](https://github.com/karser/KarserRecaptcha3Bundle) - 将 Google ReCAPTCHA v3 集成到 Symfony 中。
* [LexikFormFilterBundle](https://github.com/lexik/LexikFormFilterBundle) - Lexik 表单过滤器包。

## 国际化

* [BazingaJsTranslationBundle](https://github.com/willdurand/BazingaJsTranslationBundle) - 这是一种向客户端应用程序公开 Symfony2 翻译消息的好方法。
* [JMSI18nRoutingBundle](http://jmsyst.com/bundles/JMSI18nRoutingBundle) - 多语言网站捆绑包，支持国际航线。
* [JMSTranslationBundle](http://jmsyst.com/bundles/JMSTranslationBundle) - 轻松翻译您的网站 - 提取消息并通过基于网络的 UI 进行翻译。
* [LexikTranslationBundle](https://github.com/lexik/LexikTranslationBundle) - 允许将翻译文件内容导入数据库并提供 GUI 来编辑翻译。
* [LuneticsLocaleBundle](https://github.com/lunetics/LocaleBundle) - 从不同的参数猜测访客的区域设置。
* [TimezoneBundle](https://github.com/lunetics/TimezoneBundle) - 服务器端时区检测。
* [TranslationFormBundle](https://github.com/a2lix/TranslationFormBundle) - 翻译字段以方便使用 Translatable Doctrine 扩展。

## 杂项

* [AnhTaggableBundle](https://github.com/hilobok/AnhTaggableBundle) - Bundle提供了doctrine-extensions-taggable的集成，添加了用于编辑标签和标记的表单类型。
* [AntennaBundle](https://github.com/flint/AntennaBundle) - 使集成 Antenna（以及通过它的 JWT）身份验证变得更加容易。
* [APYBreadcrumbTrailBundle](https://github.com/Abhoryo/APYBreadcrumbTrailBundle) - 该捆绑包提供了注释和 PHP 方法来生成痕迹痕迹。
* [APYDataGridBundle](https://github.com/APY/APYDataGridBundle) - 数据网格包。
* [AvAlertifyBundle](https://github.com/AppVentus/AvAlertifyBundle) - 该捆绑包允许您轻松协调警报和其他通知。
* [AviaryBundle](https://github.com/AppVentus/AviaryBundle) - 该捆绑包基于 BlueImp jQuery 文件上传程序包提供多个文件上传。它还提供 Aviary 编辑图像功能。
* [AvListBundle](https://github.com/AppVentus/AvListBundle) - 在 Symfony2 中轻松制作分页和可排序列表。
* [BackupManagerBundle](https://github.com/lhpalacio/BackupManagerBundle) - Symfony2 的简单数据库备份管理器，支持 S3、Rackspace、Dropbox、FTP、SFTP。
* [BazingaFakerBundle](https://github.com/willdurand/BazingaFakerBundle) - 将很棒的 Faker 库放入 Symfony2 DIC 中，并用假数据填充您的数据库。
* [BazingaGeocoderBundle](https://github.com/geocoder-php/BazingaGeocoderBundle) - 地理编码器库的集成。
* [BCCMyrrixBundle](https://github.com/michelsalib/BCCMyrrixBundle) - Myrrix 是一个基于 Apache Mahout 库构建的推荐引擎。
* [BGBarcodeBundle](https://github.com/paterik/BGBarcodeBundle) - 使用我们的条形码生成器基础库进行条形码渲染的捆绑包。
* [BlogBundle](https://github.com/stfalcon/BlogBundle) - 简单的博客模块。
* [bootstrap-bundle](https://github.com/braincrafted/bootstrap-bundle) - 通过提供模板、Twig 扩展、服务和命令将 Bootstrap 集成到 Symfony2 中。
* [BreadcrumbsBundle](https://github.com/mhujer/BreadcrumbsBundle) - 一个小面包屑包。
* [BrowscapBundle](https://github.com/browscap/BrowscapBundle) - 捆绑以访问 browscap 信息。
* [CacheToolBundle](https://github.com/gordalina/CacheToolBundle) - 捆绑在 Symfony2 中集成 cachetool 库（从命令行清除 acp/opcache）。
* [CarbonBundle](https://github.com/lightsuner/CarbonBundle) - 该包提供了将请求数据转换为 Carbon 对象的机会。
* [CheckBundles](https://github.com/wjzijderveld/CheckBundles) - 检查 AppKernel 捆绑包中已安装但未激活的情况。
* [CloudBackupBundle](https://github.com/dizda/CloudBackupBundle) - 能够备份您的数据库并将其上传到云端。
* [ConsoleBundle](https://github.com/CoreSphere/ConsoleBundle) - 浏览器中的命令行界面。
* [EightPointsGuzzleBundle](https://github.com/8p/EightPointsGuzzleBundle) - 将 PHP HTTP 客户端 Guzzle 6.x 集成到 Symfony 2-4 中，并提供插件来扩展基本功能。
* [CsaGuzzleBundle](https://github.com/csarrazi/CsaGuzzleBundle) - 在 Symfony 中集成 Guzzle >=4.0 的捆绑包。
* [CsvBundle](https://github.com/EGYG33K/CsvBundle) - 将 thephpleague/csv 集成到 Symfony 中。
* [DomainParserBundle](https://github.com/EGYG33K/DomainParserBundle) - 将域解析器集成到 Symfony 中。
* [EasyAuditBundle](http://xiidea.github.io/EasyAuditBundle/) - 该捆绑包为您的应用程序提供审核日志记录 - 与 Doctrine2 实体配合使用并允许记录选择性事件。
* [EmbedlyBundle](https://github.com/EmanueleMinotto/EmbedlyBundle) - embed.ly 库的捆绑包。
* [ExcelBundle](https://github.com/liuggio/ExcelBundle) - 感谢 https://github.com/PHPOffice/PHPExcel 库将 Excel 集成到 Symfony2 中。
* [FeatureToggleBundle](https://github.com/marekkalnik/FeatureToggleBundle) - 通过向 twig 添加一些简单的标签并扩展其配置来配置 Symfony2 中的功能切换。
* [ffmpeg-bundle](https://github.com/pulse00/ffmpeg-bundle) - 该包为 PHP_FFmpeg 库提供了一个简单的包装器，将该库公开为 Symfony 服务。
* [FlorianvSwapBundle](https://github.com/florianv/FlorianvSwapBundle) - 该捆绑包集成了 Swap 库。
* [FMBbCodeBundle](https://github.com/helios-ag/FMBbCodeBundle) - 向 Symfony 项目添加 BBCode 支持。
* [FMElfinderBundle](https://github.com/helios-ag/FMElfinderBundle) - 提供 Elfinder 文件浏览器与流行的所见即所得编辑器的集成。
* [GnugatWizardBundle](https://github.com/gnugat/GnugatWizardBundle) - 神奇地将捆绑包安装步骤压缩为单个命令。
* [godfather](https://github.com/PUGX/godfather) - PHP 中策略模式的库。
* [guzzle-bundle](https://github.com/misd-service-development/guzzle-bundle) - 集成 Guzzle。
* [highcharts-bundle](https://github.com/misd-service-development/highcharts-bundle) - 集成 PHP Highcharts。
* [HTMLPurifierBundle](https://github.com/arnaud-lb/HTMLPurifierBundle) - HTML Purifier 是一个用 PHP 编写的符合标准的 HTML 过滤器库。
* [IbrowsWizardAnnotationBundle](https://github.com/ibrows/IbrowsWizardAnnotationBundle) - 为 Symfony2 控制器提供一个带有注释的简单向导/工作流程。
* [ImageCropBundle](https://github.com/anacona16/ImageCropBundle) - ImageCrop 允许您在 Symfony 应用程序中裁剪图像，此捆绑包添加了新的表单字段类型。
* [JMDUnoconvBundle](https://github.com/mops1k/JMDUnoconvBundle) - 捆绑包提供了通过 php-unoconv 库通过 unoconv (LibreOffice) 将文件从一种格式转换为另一种格式的入口。
* [KayueEssenceBundle](https://github.com/kayue/KayueEssenceBundle) - 该捆绑包将 Essence 库（oEmbed 库）集成到 Symfony 2 中。
* [KitpagesDataGridBundle](https://github.com/kitpages/KitpagesDataGridBundle) - 该捆绑包提供了一个简单的数据网格捆绑包。
* [KnpMarkdownBundle](https://github.com/KnpLabs/KnpMarkdownBundle) - PHP markdown 的包装。
* [KnpSnappyBundle](https://github.com/KnpLabs/KnpSnappyBundle) - 通过使用 webkit 转换 html 轻松创建 PDF 和图像。
* [LexikMaintenanceBundle](https://github.com/lexik/LexikMaintenanceBundle) - 这个 Symfony2 捆绑包允许您通过在控制台中调用两个命令将您的网站置于维护模式。
* [LiipImagineBundle](https://github.com/liip/LiipImagineBundle) - 图像处理包，基于 Imagine 库。
* [LiipUrlAutoConverterBundle](https://github.com/liip/LiipUrlAutoConverterBundle) - 为模板添加 Twig 扩展，并使用新的过滤器自动将字符串中的 url 和电子邮件转换为 html 链接。
* [marshaller-bundle](https://github.com/gnugat/marshaller-bundle) - 从一种格式转换为另一种格式的 PHP 库。
* [metrics](https://github.com/beberlei/metrics) - 抽象不同指标收集器的简单库。
* [MhorMediaInfoBundle](https://github.com/mhor/MhorMediaInfoBundle) - 将 php-mediainfo 库集成到 Symfony2 全栈框架中。
* [MobileDetectBundle](https://github.com/suncat2000/MobileDetectBundle) - 用于检测移动设备、管理移动视图并重定向到移动和平板电脑版本的捆绑包。
* [MultiParamBundle](https://github.com/jaytaph/MultiParamBundle) - 多参数注释包。
* [ObHighchartsBundle](https://github.com/marcaube/ObHighchartsBundle) - 旨在简化使用 highcharts 来显示丰富的图形和图表。
* [OneupUploaderBundle](https://github.com/1up-lab/OneupUploaderBundle) - 为多个多文件上传器提供服务器实现。
* [phone-number-bundle](https://github.com/misd-service-development/phone-number-bundle) - 集成 libphonenumber。
* [prezent-grid-bundle](https://github.com/Prezent/prezent-grid-bundle) - 在 Symfony2 中集成 prezent/grid 库。
* [query-bus-bundle](https://github.com/gnugat/query-bus-bundle) - Symfony 中的 QueryBus 集成。
* [request-object-resolver-bundle](https://github.com/mops1k/request-object-resolver-bundle) - 对 DTO 对象中的传入请求进行反规范化和验证。
* [rss-atom-bundle](https://github.com/alexdebril/rss-atom-bundle) - RSS 和 Atom 捆绑包。
* [Search-SphinxsearchBundle](https://github.com/timewasted/Search-SphinxsearchBundle) - Sphinx 搜索包。
* [SettingsBundle](https://github.com/dmishh/SettingsBundle) - 以数据库为中心的配置管理。支持全局和每用户设置。
* [shorturl-bundle](https://github.com/fabstei/shorturl-bundle) - 为您的项目提供短 URL。
* [SimpleArrayBundle](https://github.com/EmanueleMinotto/SimpleArrayBundle) - Symfony 2 捆绑包用于简单标签管理，基于原则 2 simple_array 类型。
* [sphinx-realtime-bundle](https://github.com/camdram/sphinx-realtime-bundle) - 一个自动将 Doctrine 实体同步到 Sphinx 实时索引的包。
* [SphinxsearchBundle](https://github.com/IAkumaI/SphinxsearchBundle) - 提供使用Sphinx搜索。
* [StringGeneratorBundle](https://github.com/vivait/StringGeneratorBundle) - 该捆绑包允许您在实体属性上自动生成唯一的随机字符串，这对于创建键很有用。
* [TbbcCacheBundle](https://github.com/TheBigBrainsCompany/TbbcCacheBundle) - 缓存抽象包。
* [TbbcMoneyBundle](https://github.com/TheBigBrainsCompany/TbbcMoneyBundle) - 该捆绑包用于将 mathiasverraes 的 Money 库集成到 symfony2 项目中。
* [TemplatedUriBundle](https://github.com/hautelook/TemplatedUriBundle) - 公开 hautelook/TemplatedUriRouter。
* [ThruwayBundle](https://github.com/voryx/ThruwayBundle) - 用于在 Symfony 中构建实时应用程序的捆绑包。
* [timeline-bundle](https://github.com/stephpy/timeline-bundle) - Symfony2 捆绑制作时间线。
* [TransmissionBundle](https://github.com/labzone/TransmissionBundle) - Transmission API 客户端的捆绑包。
* [versioning-bundle](https://github.com/shivas/versioning-bundle) - 简单的版本控制方法（语义版本控制 2.0.0）。
* [VisithorBundle](https://github.com/Visithor/VisithorBundle) - PHP 包访问者的 Symfony Bundle。
* [BabDevPagerfantaBundle](https://github.com/BabDev/BabDevPagerfantaBundle) - 捆绑使用 Pagerfanta。
* [WidopFrameworkExtraBundle](https://github.com/widop/WidopFrameworkExtraBundle) - 添加控制器类的注释配置。
* [WozbeRedirectBundle](https://github.com/wozbe/WozbeRedirectBundle) - 一个短包即可管理多个域。

## 监控

* [LiipMonitorBundle](https://github.com/liip/LiipMonitorBundle) - Bundle 提供了一种运行一系列应用程序相关健康检查的方法。
* [SoclozMonitoringBundle](https://github.com/SoCloz/SoclozMonitoringBundle) - 用于生产服务器的监控包

## 付款管理

* [CartBundle](https://github.com/leaphly/CartBundle) - 为开发人员提供的高质量购物车。
* [JMSPaymentCoreBundle](http://jmsyst.com/bundles/JMSPaymentCoreBundle) - 该捆绑包为各种支付插件提供了基础。
* [JMSPaymentPaypalBundle](https://github.com/schmittjoh/JMSPaymentPaypalBundle) - 提供对 PayPal API 的访问的付款捆绑包。
* [MangopayBundle](https://github.com/AppVentus/MangopayBundle) - Symfony2 的 Mangopay API 实现。
* [PaymentAdyenBundle](https://github.com/ruudk/PaymentAdyenBundle) - 提供对 Adyen API 的访问。基于 JMSPaymentCoreBundle。
* [PayumBundle](https://github.com/Payum/PayumBundle) - symfony2 丰富的支付解决方案。 Paypal、Stripe、Payex、Authorize.NET、Be2bill、Klarna、定期付款、即时通知等等

## 队列

* [BernardBundle](https://github.com/bernardphp/BernardBundle) - Bernard 是一个多后端 PHP 库，用于创建后台作业以供后续处理。
* [GearmanBundle](http://gearmanbundle.readthedocs.org/en/latest/) - 该捆绑包旨在提供一种简单的方法来支持需要使用作业队列的开发人员。
* [HeriJobQueueBundle](https://github.com/heristop/HeriJobQueueBundle) - 这个 Symfony 包提供了 Zend Framework 中 Zend Queue 的使用。
* [JMSJobQueueBundle](http://jmsyst.com/bundles/JMSJobQueueBundle) - 允许将控制台命令安排为作业。
* [LeezyPheanstalkBundle](https://github.com/armetiz/LeezyPheanstalkBundle) - Pheanstalk 捆绑包，beanstalkd 队列的 PHP 客户端。
* [qpush-bundle](http://qpush-bundle.readthedocs.org/en/latest/) - QPush Bundle 依赖于消息队列的推送队列模型在您的应用程序中提供异步处理。
* [RabbitMqBundle](https://github.com/videlalvaro/RabbitMqBundle) - RabbitMQ 捆绑包。
* [RSQueueBundle](https://github.com/mmoreram/RSQueueBundle) - 基于Redis的队列基础设施，具有生产者-消费者和发布者-订阅者
* [Enqueue](https://github.com/php-enqueue/enqueue-dev) - 为程序提供创建、发送、读取消息的通用方法。受到 Java JMS 的启发

## 阅读

* [Symfony 5: The Fast Track](https://symfony.com/book) - 由 Symfony 的创建者编写的书，免费在线。
* [使用 Symfony2 的高性能网站](http://slides.seld.be/?file=2011-10-20+High+Performance+Websites+with+Symfony2.html)
* [Symfony - 项目被驯服](http://clearcode.cc/2014/03/symfony-project/)
* [Symfony 4.1 Jobeet 教程](https://jobeet-tutorial.readthedocs.io/en/latest/)

## 食谱
* [Symfony Recipes](https://github.com/symfony/recipes) - Symfony 配方允许通过 Symfony Flex Composer 插件自动化 Composer 包配置。
* [Symfony Recipes (Contrib)](https://github.com/symfony/recipes-contrib) - Symfony 配方允许通过 Symfony Flex Composer 插件自动化 Composer 包配置。

## 资源

* [Symfony2 Service Config Converter](http://converter.rosstuck.com/) - 一个简单的服务，用于在 YAML、XML 和 INI 之间转换服务配置。
* [Twigfiddle](http://twigfiddle.com/) - 用于在线开发、运行、存储和访问 Twig 代码的小型开发环境。
* [Modern PHP cheatsheet](https://github.com/smknstd/modern-php-cheatsheet) - 现代项目中经常遇到的一些 PHP 知识备忘单。

## 服务容器

* [CraueConfigBundle](https://github.com/craue/CraueConfigBundle) - 管理存储在数据库中的配置设置，并使其可通过 Symfony 2 项目中的服务进行访问。
* [JMSDiExtraBundle](http://jmsyst.com/bundles/JMSDiExtraBundle) - 提供高级依赖注入功能。
* [KutnyAutowiringBundle](https://github.com/kutny/autowiring-bundle) - 为服务参数提供自动装配的包。
* [PHP-DI](http://php-di.org) - 人类的依赖注入容器。

## 存储

* [AliceBundle](https://github.com/hautelook/AliceBundle) - 一个 Symfony2 包，用于帮助与 Alice 一起加载 Doctrine Fixtures。
* [AliceFixturesBundle](https://github.com/h4cc/AliceFixturesBundle) - 一个 Symfony2 捆绑包，用于将 Alice 和 Faker 与数据装置一起使用。
* [AvSpoolMailerBundle](https://github.com/AppVentus/AvSpoolMailerBundle) - 将您的邮件存储为假脱机并发送事务直接邮件或将其存储在数据库中。
* [doctrine-routing-bundle](https://github.com/eschmar/doctrine-routing-bundle) - 动态数据库路由。
* [DoctrineEncryptBundle](https://github.com/vmelnik-ukraine/DoctrineEncryptBundle) - Bundle 允许您创建带有受 AES 等加密算法保护的字段的学说实体。
* [DoctrineEnumBundle](https://github.com/fre5h/DoctrineEnumBundle) - 为 Doctrine2 提供 MySQL ENUM 类型的支持。
* [DoctrineFixturesBundle](https://github.com/doctrine/DoctrineFixturesBundle) - 集成 Doctrine2 数据夹具库。
* [DoctrineMigrationsBundle](https://github.com/doctrine/DoctrineMigrationsBundle) - 集成 Doctrine2 迁移库。
* [elastica-query-bundle](https://github.com/mapado/elastica-query-bundle) - ElasticSearch 的查询构建器包。
* [FeedBundle](https://github.com/eko/FeedBundle) - 用于从您的实体构建 RSS 源的捆绑包。
* [FPNTagBundle](https://github.com/FabienPennequin/FPNTagBundle) - 该捆绑包添加了标签，能够将标签与任意数量的不同实体相关联。
* [GaufretteBrowserBundle](https://github.com/digitalkaoz/GaufretteBrowserBundle) - 该捆绑包允许您像 Doctrine Connection 一样浏览 Gaufrette 文件系统。
* [KnpGaufretteBundle](https://github.com/KnpLabs/KnpGaufretteBundle) - 集成 Gaufrette。
* [MysqlDoctrineFunctions](https://github.com/mapado/MysqlDoctrineFunctions) - MySQL 函数原则：RAND()、ROUND()、DATE()、DATE_FORMAT()。
* [OneupFlysystemBundle](https://github.com/1up-lab/OneupFlysystemBundle) - 集成飞行系统。
* [RelationBundle](https://github.com/Ph3nol/RelationBundle) - 用于管理模型/实体之间关系的捆绑包。 （不再维护）
* [SncRedisBundle](https://github.com/snc/SncRedisBundle) - 将 Redis 集成到您的应用程序中的捆绑包。
* [StofDoctrineExtensionsBundle](https://github.com/stof/StofDoctrineExtensionsBundle) - 该捆绑包提供了 DoctrineExtensions 的集成。
* [VichGeographicalBundle](https://github.com/dustin10/VichGeographicalBundle) - 一个包，为 ORM 和 ODM 实体提供地理特征以及面向对象的 javascript 地图渲染。
* [WizadDoctrineDocBundle](https://github.com/wpottier/WizadDoctrineDocBundle) - 允许您为您的学说模型架构生成一个像样的文档。

## 模板引擎

* [CgKintBundle](https://github.com/carlos-granados/CgKintBundle) - 该捆绑包允许您在 Twig 模板中使用 Kint 库。
* [FlashAlertBundle](https://github.com/rasanga/FlashAlertBundle) - 处理（添加/显示）Symfony flash 消息的简化方法。
* [GravatarBundle](https://github.com/henrikbjorn/GravatarBundle) - 头像 API 的简单包装。
* [KnpTimeBundle](https://github.com/KnpLabs/KnpTimeBundle) - 为时间操纵提供帮助。
* [swift-css-inliner-bundle](https://github.com/toretto460/swift-css-inliner-bundle) - 一个 Swiftmailer 插件，提供 css 内联功能。
* [TwigCacheBundle](https://github.com/EmanueleMinotto/TwigCacheBundle) - asm89/twig-cache-extension 的捆绑包。
* [TwigExtraBundle](https://github.com/csanquer/TwigExtraBundle) - Twig 额外工具扩展。
* [TwigInflectionBundle](https://github.com/EmanueleMinotto/TwigInflectionBundle) - 通过 Twig 扩展应用变形。
* [TwigJackBundle](https://github.com/boekkooi/TwigJackBundle) - Twig 方便的附加功能。
* [TwitalBundle](https://github.com/goetas/twital-bundle) - 一个建立在 Twig 之上的属性模板引擎，100% 兼容所有 twig 的功能。
* [UcoTwigExtensionsBundle](https://github.com/sgomez/UcoTwigExtensionsBundle) - 提供一些过滤器。

## 第三方API

* [AlgoliaSearchBundle](https://github.com/algolia/AlgoliaSearchBundle) - 将 Algolia Search 无缝集成到您的 Symfony 项目中。
* [CoopTilleulsOvhBundle](https://github.com/coopTilleuls/CoopTilleulsOvhBundle) - 使用 OVH API 发送短信。
* [GordalinaMixpanelBundle](https://github.com/gordalina/GordalinaMixpanelBundle) - Symfony2 中的 Mixpanel 集成。
* [SwarrotBundle](https://github.com/swarrot/SwarrotBundle) - 用于 swarrot 集成的捆绑包。
* [SwmMailHookBundle](https://github.com/ScullWM/MailHookBundle/) - 用于捕获来自不同邮件服务（Mailjet、Mandrill、自定义）的 API Webhook 的捆绑包
* [YuccaPrerenderBundle](https://github.com/rjanot/YuccaPrerenderBundle) - Symfony2 捆绑包使用 prerender.io。

## 用户管理

* [HWIOAuthBundle](https://github.com/hwi/HWIOAuthBundle) - OAuth 客户端集成。同时支持OAuth1.0a和OAuth2。
* [JmikolaAutoLoginBundle](https://github.com/jmikola/JmikolaAutoLoginBundle) - 该捆绑包将 AutoLogin 库与 Symfony2 集成，后者实现了安全防火墙侦听器，以根据单个查询参数对用户进行身份验证。
* [JMSSecurityExtraBundle](http://jmsyst.com/bundles/JMSSecurityExtraBundle) - 通过多项新功能增强了安全组件。
* [SamlBundle](https://github.com/pdias/SamlBundle) - SamlBundle 在 Symfony2 中添加了对 SAML 2.0 服务提供程序的支持。
* [two-factor-bundle](https://github.com/scheb/two-factor-bundle) - 此 Symfony2 捆绑包为您的网站提供双因素身份验证。

## 验证

* [dms-filter-bundle](https://github.com/rdohms/dms-filter-bundle) - 提供FilterService，允许用户使用Annotations在实体中实现输入过滤。
* [PasswordStrengthBundle](https://github.com/jbafford/PasswordStrengthBundle) - 确保强密码的验证器。
* [vatin-bundle](https://github.com/ddeboer/vatin-bundle) - VATIN 库的 Symfony2 捆绑包（验证增值税识别号）。

## 网络服务

* [api2symfony-bundle](https://github.com/creads/api2symfony-bundle) - Symfony 2 捆绑包允许根据标准 API 规范自动生成控制器。
* [BazingaHateoasBundle](https://github.com/willdurand/BazingaHateoasBundle) - 集成 Hateoas 库。
* [DunglasAngularCsrfBundle](https://github.com/dunglas/DunglasAngularCsrfBundle) - 对与 AngularJS 和其他主要 AJAX 库一起使用的 Symfony API 进行自动 CSRF 保护
* [DunglasApiBundle](https://github.com/dunglas/DunglasApiBundle) - 用于构建超媒体驱动的 REST API 的捆绑包。
* [FOSOAuthServerBundle](https://github.com/FriendsOfSymfony/FOSOAuthServerBundle) - 服务器端 OAuth2 捆绑包。
* [FOSRestBundle](https://github.com/FriendsOfSymfony/FOSRestBundle) - 提供各种工具来快速开发 RESTful API 和应用程序。
* [JMSSerializerBundle](https://github.com/schmittjoh/JMSSerializerBundle) - 轻松序列化和反序列化任何复杂性的数据。
* [JSONApiBundle](https://github.com/nilportugues/symfony-jsonapi) - 捆绑包，支持格式化 REST 响应以遵循 JSON API 规范。
* [KnpJsonSchemaBundle](https://github.com/KnpLabs/KnpJsonSchemaBundle) - 提供一项服务，允许您根据验证元数据生成 json 模式。
* [LemonRestBundle](https://github.com/stanlemon/rest-bundle) - 一个固执己见的捆绑包，为 Doctrine 实体提供 REST 端点。
* [LexikJWTAuthenticationBundle](https://github.com/lexik/LexikJWTAuthenticationBundle) - 该捆绑包使用 lcobucci/jwt 库为您的 REST API 提供 JWT（Json Web 令牌）身份验证。
* [NelmioApiDocBundle](https://github.com/nelmio/NelmioApiDocBundle) - 从注释生成 REST API 的文档。
* [NelmioCorsBundle](https://github.com/nelmio/NelmioCorsBundle) - 添加了基于简单 ACL 样式的每 URL 配置添加 CORS 相关标头的功能。
* [RateLimitBundle](https://github.com/jaytaph/RateLimitBundle) - 通过注释轻松为控制器/操作添加速率限制。
* [RequestLimitBundle](https://github.com/zim32/Symfony2-RequestLimitBundle) - 使用此捆绑包，您可以轻松限制对应用程序的请求。
* [ResourceBundle](https://github.com/ProgrammingAreHard/ResourceBundle) - 有助于开发 REST API 的捆绑包。
* [SerializedResponseBundle](https://github.com/Pulpmedia/SerializedResponseBundle) - 一个简单的捆绑包，提供一种简单的方法来发送带注释的序列化对象的 json/xml/yaml 响应。
* [SRIORestUploadBundle](https://github.com/sroze/SRIORestUploadBundle) - 一个 symfony 包，用于处理 REST API 上的多种上传方式。

## 许可证

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](http://creativecommons.org/publicdomain/zero/1.0/)

在法律允许的范围内，[Emanuele Minotto](http://emanueleminotto.github.io)（存储库的原始创建者）和 [SitePoint](http://www.sitepoint.com/) 已放弃本作品的所有版权以及相关或邻接权。
