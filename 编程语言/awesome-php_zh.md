# 很棒的 PHP [![Awesome](https://cdn.jsdelivr.net/gh/sindresorhus/awesome@d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

精彩的 PHP 库、资源和有用工具的精选列表。

## 贡献与协作
请参阅[贡献](https://github.com/ziadoz/awesome-php/blob/master/CONTRIBUTING.md)、[CODE-OF-CONDUCT](https://github.com/ziadoz/awesome-php/blob/master/CODE-OF-CONDUCT.md) 和[协作](https://github.com/ziadoz/awesome-php/blob/master/COLLABORATING.md) 了解详细信息。

## 目录
- [很棒的 PHP](#awesome-php)
  - [作曲家存储库](#composer-repositories)
  - [依赖管理](#dependency-management)
  - [依赖管理附加功能](#dependency-management-extras)
  - [Frameworks](#frameworks)
  - [框架附加功能](#framework-extras)
  - [内容管理系统](#content-management-systems-cms)
  - [Components](#components)
  - [微框架](#micro-frameworks)
  - [微框架附加功能](#micro-framework-extras)
  - [Routers](#routers)
  - [Templating](#templating)
  - [静态站点生成器](#static-site-generators)
  - [HTTP](#http)
  - [Scraping](#scraping)
  - [Middlewares](#middlewares)
  - [URL](#url)
  - [Email](#email)
  - [Files](#files)
  - [Streams](#streams)
  - [依赖注入](#dependency-injection)
  - [Imagery](#imagery)
  - [Testing](#testing)
  - [持续集成](#continuous-integration)
  - [Documentation](#documentation)
  - [Security](#security)
  - [Passwords](#passwords)
  - [代码分析](#code-analysis)
  - [代码质量](#code-quality)
  - [静态分析](#static-analysis)
  - [Architectural](#architectural)
  - [调试和分析](#debugging-and-profiling)
  - [错误跟踪和监控服务](#error-tracking-and-monitoring-services)
  - [构建工具](#build-tools)
  - [任务运行器](#task-runners)
  - [Navigation](#navigation)
  - [资产管理](#asset-management)
  - [Geolocation](#geolocation)
  - [日期和时间](#date-and-time)
  - [Event](#event)
  - [Logging](#logging)
  - [E-commerce](#e-commerce)
  - [PDF](#pdf)
  - [Office](#office)
  - [Database](#database)
  - [Migrations](#migrations)
  - [NoSQL](#nosql)
  - [Queue](#queue)
  - [Search](#search)
  - [命令行](#command-line)
  - [认证与授权](#authentication-and-authorization)
  - [标记和 CSS](#markup-and-css)
  - [JSON](#json)
  - [Strings](#strings)
  - [Numbers](#numbers)
  - [过滤、净化和验证](#filtering-sanitizing-and-validation)
  - [API](#api)
  - [缓存和锁定](#caching-and-locking)
  - [数据结构和存储](#data-structure-and-storage)
  - [Notifications](#notifications)
  - [Deployment](#deployment)
  - [国际化和本地化](#internationalisation-and-localisation)
  - [Serverless](#serverless)
  - [Configuration](#configuration)
  - [LLMs](#llms)
  - [第三方API](#third-party-apis)
  - [Extensions](#extensions)
  - [Miscellaneous](#miscellaneous)
- [Software](#software)
  - [PHP安装](#php-installation)
  - [开发环境](#development-environment)
  - [虚拟机](#virtual-machines)
  - [文本编辑器和 IDE](#text-editors-and-ides)
  - [网络应用程序](#web-applications)
  - [Infrastructure](#infrastructure)
- [Resources](#resources)
  - [PHP 网站](#php-websites)
  - [PHP 书籍](#php-books)
  - [PHP 视频](#php-videos)
  - [PHP 会议](#php-conferences)
  - [PHP 播客](#php-podcasts)
  - [PHP 通讯](#php-newsletters)
  - [PHP阅读](#php-reading)
  - [PHP 内部原理阅读](#php-internals-reading)

### 作曲家存储库
*作曲家存储库。*

* [Firegento](https://packages.firegento.com/) - Magento 模块 Composer 存储库。
* [Packagist](https://packagist.org/) - PHP 包存储库。
* [Packalyst](https://packalyst.com/) - Laravel 包存储库。
* [Private Packagist](https://packagist.com/) - Composer 包存档作为 PHP 的服务。
* [WordPress Packagist](https://wpackagist.org/) - 使用 Composer 管理您的插件。

### 依赖管理
*用于依赖项和包管理的库。*

* [Composer](https://getcomposer.org/) - 包和依赖项管理器。
* [Composer Installers](https://github.com/composer/installers) - 多框架 Composer 库安装程序。
* [Phive](https://phar.io/) - PHAR 经理。
* [Pickle](https://github.com/FriendsOfPHP/pickle) - PHP 扩展安装程序。
* [Pie](https://github.com/php/pie) - 用于扩展的官方 PHP 安装程序。

### 依赖管理附加功能
*与依赖管理相关的额外内容。*

* [Composer Merge Plugin](https://github.com/wikimedia/composer-merge-plugin) - 一个用于合并多个“composer.json”文件的作曲家插件。
* [Composer Normalize](https://github.com/ergebnis/composer-normalize) - 用于规范“composer.json”文件的插件。
* [Composer Patches](https://github.com/cweagans/composer-patches) - Composer 应用补丁的插件。
* [Composer Prefer Lowest Validator](https://github.com/dereuromark/composer-prefer-lowest) - 用于检查是否可以安装和测试最小依赖项的插件。
* [Composer Require Checker](https://github.com/maglnet/ComposerRequireChecker) - CLI 工具，用于分析 Composer 依赖关系并验证包源中是否未使用未知符号。
* [Composer Unused](https://github.com/composer-unused/composer-unused) - 用于扫描未使用的 Composer 包的 CLI 工具。
* [Repman](https://repman.io) - 私有 PHP 包存储库管理器和 Packagist 代理。
* [Satis](https://github.com/composer/satis) - 静态 Composer 存储库生成器。

### 框架
*网络开发框架。*

* [CakePHP](https://cakephp.org/) - 快速应用程序开发框架。
* [CodeIgniter](https://codeigniter.com/) - 一个强大的 PHP 框架，占用空间非常小。
* [Ecotone](https://docs.ecotone.tech/) - 基于 DDD CQRS 和事件源架构原则的 PHP 服务总线。
* [Laminas](https://getlaminas.org/) - 由各个组件组成的框架（以前称为 Zend Framework）。
* [Laravel](https://laravel.com/) - 具有富有表现力、优雅语法的 Web 应用程序框架。
* [Nette](https://nette.org) - 由成熟组件组成的 Web 框架。
* [Phalcon](https://phalcon.io/en-us) - 作为 C 扩展实现的框架。
* [Spiral](https://spiral.dev/) - 高性能 PHP/Go 框架。
* [Symfony](https://symfony.com/) - 一组可重用组件和一个 Web 框架。
* [Tempest](https://github.com/tempestphp/tempest-framework) - 一个不妨碍你的框架。
* [Yii2](https://github.com/yiisoft/yii2/) - 快速、安全、高效的 Web 框架。

### 框架附加功能
*与 Web 开发框架相关的其他内容。*

* [CakePHP CRUD](https://github.com/friendsofcake/crud) - CakePHP 的快速应用程序开发 (RAD) 插件。
* [Filament PHP](https://filamentphp.com/) - 一个强大的 Laravel 开源 UI 框架。
* [Inertia.js](https://inertiajs.com/) - 用于使用服务器端路由和控制器构建单页应用程序的适配器，无需单独的 API。
* [LaravelS](https://github.com/hhxsv5/laravel-s) - Laravel/Lumen 和 Swoole 之间的开箱即用适配器。
* [Livewire](https://livewire.laravel.com/) - 无需离开 PHP 即可实现强大、动态的前端 UI。

### 内容管理系统 (CMS)
*管理数字内容的工具。*

* [Backdrop](https://backdropcms.org) - 针对中小型企业和非营利组织的 CMS（Drupal 的一个分支）。
* [Concrete5](https://www.concretecms.com/) - 针对具有最低技术技能的用户的 CMS。
* [CraftCMS](https://github.com/craftcms/cms) - 灵活、用户友好的 CMS，用于在网络及其他领域创建自定义数字体验。
* [Drupal](https://new.drupal.org/home) - 企业级 CMS。
* [Grav](https://github.com/getgrav/grav) - 现代平面文件 CMS。
* [Joomla](https://www.joomla.org/) - 另一个领先的 CMS。
* [Kirby](https://getkirby.com/) - 适合任何项目的平面文件 CMS。
* [Magento](https://github.com/magento/magento2) - 一个广泛使用的开源电子商务平台。
* [Moodle](https://moodle.org/) - 一个开源学习平台。
* [OctoberCMS](https://octobercms.com/) - 基于 Laravel 构建的 CMS。
* [OpenMage](https://github.com/OpenMage/magento-lts) - EoL Magento 1 电子商务平台的分叉。
* [Pico CMS](https://picocms.org/) - 轻量级平面文件 CMS。
* [Silverstripe](https://www.silverstripe.org/) - 简单、灵活且安全的 CMS。
* [Statamic](https://statamic.com/) - 基于 Laravel 构建的平面文件和基于 Git 的 CMS。
* [Sulu](https://sulu.io/) - 基于 Symfony 框架构建的用户和开发人员友好的 CMS。
* [TYPO3](https://typo3.org) - 企业级 CMS。
* [WinterCMS](https://wintercms.com) - 基于 Laravel 构建的 OctoberCMS 的社区维护分支。
* [WordPress](https://github.com/WordPress/WordPress) - 博客平台和 CMS。

### 组件
*来自 Web 开发框架和开发小组的独立组件。*

* [Aura](https://auraphp.com/) - 独立的组件，彼此之间以及与任何框架完全解耦。
* [CakePHP Plugins](https://plugins.cakephp.org/) - CakePHP 插件的目录。
* [Laminas Components](https://docs.laminas.dev/components/) - 构成 Laminas 框架的组件。
* [Laravel Components](https://github.com/illuminate) - Laravel 框架组件。
* [League of Extraordinary Packages](https://thephpleague.com/) - 一个 PHP 包开发小组。
* [Spatie Open Source](https://spatie.be/open-source) - 开源 PHP 和 Laravel 包的集合。
* [Symfony Packages](https://symfony.com/packages) - PHP 应用程序的解耦库。

### 微框架
*微型框架和路由器。*

* [Laravel Zero](https://laravel-zero.com) - 控制台应用程序的微框架。
* [Mezzio](https://getexpressive.org/) - Laminas 的微框架。
* [Minicli](https://github.com/minicli/minicli) - 用于构建以 CLI 为中心的 PHP 应用程序的极简、无依赖框架。
* [Silly](https://github.com/mnapoli/silly) - CLI 应用程序的微框架。
* [Slim](https://www.slimframework.com/) - 另一个简单的微框架。

### 微框架附加功能
*与微框架和路由器相关的额外内容。*

* [Slim Skeleton](https://github.com/slimphp/Slim-Skeleton) - 斯利姆的骨架。
* [Slim PHP View](https://github.com/slimphp/PHP-View) - 一个简单的 Slim PHP 渲染器。

### 路由器
*用于处理应用程序路由的库。*

* [Aura.Router](https://github.com/auraphp/Aura.Router) - 一个全功能的路由库。
* [Fast Route](https://github.com/nikic/FastRoute) - 一个快速路由库。
* [Klein](https://github.com/klein/klein.php) - 灵活的路由器。
* [Route](https://github.com/thephpleague/route) - 构建在 Fast Route 之上的路由库。

### 模板化
*用于模板和词法分析的库和工具。*

* [Latte](https://latte.nette.org/) - 最安全且真正直观的 PHP 模板。
* [MtHaml](https://github.com/arnaud-lb/MtHaml) - HAML 模板语言的 PHP 实现。
* [Mustache](https://github.com/bobthecow/mustache.php) - Mustache 模板语言的 PHP 实现。
* [PHPTAL](https://phptal.org/) - [TAL](https://en.wikipedia.org/wiki/Template_Attribute_Language) 模板语言的 PHP 实现。
* [Plates](https://platesphp.com/) - 原生 PHP 模板库。
* [Smarty](https://www.smarty.net/) - 一个补充 PHP 的模板引擎。
* [Twig](https://twig.symfony.com/) - 一种综合的模板语言。

### 静态站点生成器
*用于预处理内容以生成网页的工具。*

* [Cecil](https://cecil.app/) - 一个简单而强大的内容驱动静态站点生成器。
* [Couscous](https://couscous.io) - 一个将 Markdown 文档转换为网站的工具。
* [Jigsaw](https://jigsaw.tighten.com/) - 使用 Laravel 的 Blade 的简单静态站点。
* [Sculpin](https://sculpin.io) - 一个将 Markdown 和 Twig 转换为静态 HTML 的工具。

### HTTP协议
*用于使用 HTTP 的库。*

* [Buzz](https://github.com/kriswallsmith/Buzz) - 另一个 HTTP 客户端。
* [Guzzle](https://github.com/guzzle/guzzle) - 一个全面的 HTTP 客户端。
* [HTTPlug](https://httplug.io) - 不绑定到特定实现的 HTTP 客户端抽象。
* [Nyholm PSR-7](https://github.com/Nyholm/psr7) - 超轻量级 PSR-7 实现。非常严格而且非常快。
* [PHP VCR](https://php-vcr.github.io/) - 用于记录和重放 HTTP 请求的库。
* [Requests](https://github.com/WordPress/Requests) - 一个简单的 HTTP 库。
* [Retrofit](https://github.com/tebru/retrofit-php) - 用于简化 REST API 客户端创建的库。
* [Saloon](https://github.com/saloonphp/saloon) - 用于构建漂亮的 API 集成和 SDK 的框架。
* [Symfony HTTP Client](https://github.com/symfony/http-client) - 用于同步或异步获取 HTTP 资源的组件。
* [Laminas Diactoros](https://github.com/laminas/laminas-diactoros) - PSR-7 HTTP 消息实现。

### 刮痧
*用于抓取网站和检测爬虫的库。*

* [Chrome PHP](https://github.com/chrome-php/chrome) - 来自 PHP 的仪器无头 Chrome/Chromium 实例。
* [CrawlerDetect](https://github.com/JayBizzle/Crawler-Detect) - 用于通过用户代理检测机器人/爬虫/蜘蛛的 PHP 类。
* [DiDOM](https://github.com/Imangazaliev/DiDOM) - 超快的 HTML 抓取器和解析器。
* [Embed](https://github.com/php-embed/Embed) - 来自任何网络服务或页面的信息提取器。
* [PHP Spider](https://github.com/mvdbos/php-spider) - 一个可配置且可扩展的 PHP 网络蜘蛛。
* [Symfony Panther](https://github.com/symfony/panther) - PHP 和 Symfony 的浏览器测试和网络爬行库。

### 中间件
*使用中间件构建应用程序的库。*

* [PSR-15 Middlewares](https://github.com/middlewares/psr15-middlewares) - 鼓舞人心的方便中间件集合。
* [Stack](https://github.com/stackphp) - Symfony 的可堆栈中间件库。
* [Laminas Stratigility](https://github.com/laminas/laminas-stratigility) - 构建在 PSR-7 之上的 PHP 中间件。

### 网址
*用于解析 URL 的库。*

* [PHP Domain Parser](https://github.com/jeremykendall/php-domain-parser) - 域名后缀解析器库。
* [sabre/uri](https://github.com/sabre-io/uri) - 一个功能性 URI 操作库。
* [Uri](https://github.com/thephpleague/uri) - 另一个 URL 操作库。

### 电子邮件
*用于发送和解析电子邮件的库。*

* [CssToInlineStyles](https://github.com/tijsverkoyen/CssToInlineStyles) - 在电子邮件模板中内联 CSS 的库。
* [ddeboer/imap](https://github.com/ddeboer/imap) - 面向对象、经过全面测试的 PHP IMAP 库。
* [Email Reply Parser](https://github.com/willdurand/EmailReplyParser) - 电子邮件回复解析器库。
* [Fetch](https://github.com/tedious/Fetch) - IMAP 库。
* [Mautic](https://github.com/mautic/mautic) - 电子邮件营销自动化。
* [PHPMailer](https://github.com/PHPMailer/PHPMailer) - 另一个邮件解决方案。
* [Stampie](https://github.com/Stampie/Stampie) - 用于电子邮件服务的库，例如 [SendGrid](https://www.twilio.com/en-us/sendgrid)、[PostMark](https://postmarkapp.com)、[MailGun](https://www.mailgun.com/) 和 [MailChimp](https://mailchimp.com/features/transactional-email/)。
* [Symfony Mailer](https://github.com/symfony/mailer) - 用于创建和发送电子邮件的强大库。

### 文件
*用于文件操作和 MIME 类型检测的库。*

* [CSV](https://github.com/thephpleague/csv) - CSV 数据操作库。
* [Flysystem](https://github.com/thephpleague/Flysystem) - 本地和远程文件系统的抽象。
* [Gaufrette](https://github.com/KnpLabs/Gaufrette) - 文件系统抽象层。
* [PHP FFmpeg](https://github.com/PHP-FFmpeg/PHP-FFmpeg/) - [FFmpeg](https://www.ffmpeg.org/) 视频库的包装器。
* [UnifiedArchive](https://github.com/wapmorgan/UnifiedArchive) - 压缩档案的统一读取器和写入器。
* [Parquet](https://github.com/flow-php/parquet) - Parquet 文件格式的 PHP 实现。

### 流
*用于处理流的库。*

* [ByteStream](https://amphp.org/byte-stream) - 异步流抽象。

### 依赖注入
*实现依赖注入设计模式的库。*

* [Aura.Di](https://github.com/auraphp/Aura.Di) - 一个可序列化的依赖注入容器，具有构造函数和设置器注入、接口和特征感知、配置继承等等。
* [Acclimate](https://github.com/AcclimateContainer/acclimate-container) - 依赖注入容器和服务定位器的通用接口。
* [Auryn](https://github.com/rdlowrey/Auryn) - 递归依赖注入器。
* [Container](https://github.com/thephpleague/container) - 另一个灵活的依赖注入容器。
* [Disco](https://github.com/bitExpert/disco) - 兼容 PSR-11、基于注释的依赖项注入容器。
* [PHP-DI](https://php-di.org/) - 支持自动装配的依赖注入容器。
* [Pimple](https://github.com/silexphp/Pimple) - 一个微小的依赖注入容器。
* [Symfony DI](https://github.com/symfony/dependency-injection) - 依赖注入容器组件。

### 图像
*用于操作图像的库。*

* [Color Extractor](https://github.com/thephpleague/color-extractor) - 用于从图像中提取颜色的库。
* [Glide](https://github.com/thephpleague/glide) - 按需图像处理库。
* [Image Hash](https://github.com/jenssegers/imagehash) - 用于生成感知图像哈希的库。
* [Image Optimizer](https://github.com/psliwa/image-optimizer) - 用于优化图像的库。
* [Imagine](https://imagine.readthedocs.io/en/latest/index.html) - 图像处理库。
* [Intervention Image](https://github.com/Intervention/image) - 另一个图像处理库。
* [PHP Image Workshop](https://github.com/Sybio/ImageWorkshop) - 另一个图像处理库。
* [PHP QR Code](https://github.com/chillerlan/php-qrcode/) - QR 码生成器和阅读器。

### 测试
*用于测试代码库和生成测试数据的库。*

* [Alice](https://github.com/nelmio/alice) - 富有表现力的夹具生成库。
* [Behat](https://docs.behat.org/en/latest/) - 行为驱动开发 (BDD) 测试框架。
* [Codeception](https://github.com/Codeception/Codeception) - 全栈测试框架。
* [Faker](https://github.com/fakerphp/faker) - 一个假数据生成器库。
* [Foundry](https://github.com/zenstruck/foundry) - Doctrine 的夹具工厂生成库。
* [Infection](https://github.com/infection/infection) - 一个基于 AST 的 PHP 突变测试框架。
* [Kahlan](https://github.com/kahlan/kahlan) - 全栈单元/BDD 测试框架，具有内置存根、模拟和代码覆盖支持。
* [Mink](https://mink.behat.org/en/latest/) - 网络验收测试。
* [Mockery](https://github.com/mockery/mockery) - 用于测试的模拟对象库。
* [Nette Tester](https://github.com/nette/tester) - 一个高效且令人愉快的并行单元测试框架。
* [ParaTest](https://github.com/paratestphp/paratest) - PHPUnit 的并行测试库。
* [Pest](https://pestphp.com/) - 注重简单性的测试框架。
* [Phake](https://github.com/phake/phake) - 另一个用于测试的模拟对象库。
* [PHP-Mock](https://github.com/php-mock/php-mock) - 用于内置 PHP 函数（例如 time()）的模拟库。
* [PHP MySQL Engine](https://github.com/vimeo/php-mysql-engine) - 用纯 PHP 编写的 MySQL 引擎。
* [PHPSpec](https://github.com/phpspec/phpspec) - 按规范设计的单元测试库。
* [PHPT](https://php.github.io/php-src/miscellaneous/writing-tests.html) - PHP本身使用的测试工具。
* [PHPUnit](https://github.com/sebastianbergmann/phpunit) - 一个单元测试框架。
* [PHPUnit Polyfills](https://github.com/Yoast/PHPUnit-Polyfills/) - 简化在多个 PHPUnit 版本上运行 PHPUnit 测试。
* [Prophecy](https://github.com/phpspec/prophecy) - 一个高度固执己见的模拟框架。
* [VFS Stream](https://github.com/bovigo/vfsStream) - 用于测试的虚拟文件系统流包装器。

### 持续集成
*用于持续集成的库和应用程序。*

* [CircleCI](https://circleci.com) - 一个持续集成平台。
* [GitLab CI](https://about.gitlab.com/solutions/continuous-integration/) - 一个持续集成平台。
* [Jenkins](https://www.jenkins.io/) - 具有[PHP支持](https://www.jenkins.io/solutions/php/)的持续集成平台。
* [SemaphoreCI](https://semaphore.io/) - 适用于开源和私有项目的持续集成平台。
* [Travis CI](https://www.travis-ci.com) - 一个持续集成平台。
* [Setup PHP](https://github.com/shivammathur/setup-php) - PHP 的 GitHub 操作。

### 文档
*用于生成项目文档的库。*

* [APIGen](https://github.com/apigen/apigen) - 另一个 API 文档生成器。
* [daux.io](https://github.com/dauxio/daux.io) - 使用 Markdown 文件的文档生成器。
* [phpDocumentor](https://phpdoc.org/) - 文档生成器。
* [Scramble](https://github.com/dedoc/scramble) - 从您的代码自动生成 OpenAPI 文档，无需注释。
* [zircote/swagger-php](https://github.com/zircote/swagger-php) - 为您的 RESTful API 生成 OpenAPI 文档。

### 安全性
*用于生成安全随机数、加密数据以及扫描和测试漏洞的库。*

* [AntiXSS](https://github.com/voku/anti-xss) - 尝试通过黑名单防止跨站脚本 (XSS) 攻击的库。
* [Halite](https://paragonie.com/project/halite) - 使用 [libsodium](https://github.com/jedisct1/libsodium) 进行加密的简单库。
* [Optimus](https://github.com/jenssegers/optimus) - 基于 Knuth 乘法哈希方法的 ID 混淆。
* [OWASP](https://owasp.org/) - 探索网络安全的世界。
* [PHPGGC](https://github.com/ambionics/phpggc) - PHP 不可序列化有效负载的库以及生成它们的工具。
* [PHP Encryption](https://github.com/defuse/php-encryption) - 安全的 PHP 加密库。
* [PHPSecLib](https://github.com/phpseclib/phpseclib) - 一个纯 PHP 安全通信库。
* [Roave Security Advisories](https://github.com/Roave/SecurityAdvisories) - 此包可确保您的应用程序没有安装具有已知安全漏洞的依赖项。
* [Secure Headers](https://github.com/BePsvPT/secure-headers) - 一个将安全相关标头添加到 HTTP 响应的包。
* [SQLMap](https://github.com/sqlmapproject/sqlmap) - 一个自动 SQL 注入和数据库接管工具。
* [Zap](https://github.com/zaproxy/zaproxy) - 用于 Web 应用程序的集成渗透测试工具。

### 密码
*用于使用和存储密码的库和工具。*

* [GenPhrase](https://github.com/timoh6/GenPhrase) - 用于生成安全随机密码的库。
* [Password Validator](https://github.com/jeremykendall/password-validator) - 用于验证和升级密码哈希的库。
* [Password-Generator](https://github.com/hackzilla/password-generator) - 用于生成随机密码的 PHP 库。
* [phpass](https://www.openwall.com/phpass/) - 便携式密码哈希框架。
* [Zxcvbn PHP](https://github.com/bjeavons/zxcvbn-php) - 一个基于Zxcvbn JS的真实PHP密码强度估计库。

### 代码分析
*用于分析、解析和操作代码库的库和工具。*

* [Better Reflection](https://github.com/Roave/BetterReflection) - 一个基于 AST 的反射库，允许分析和操作代码。
* [Bladestan](https://github.com/bladestan/bladestan) - 用于 Blade 模板静态分析的 PHPStan 扩展。
* [Code Climate](https://codeclimate.com) - 自动代码审查。
* [Editorconfig-Checker](https://github.com/editorconfig-checker/editorconfig-checker.php) - 一个命令行实用程序，用于验证您的文件是否实现了“.editorconfig”规则。
* [GrumPHP](https://github.com/phpro/grumphp) - PHP 代码质量工具。
* [PHP AST Viewer](https://php-ast-viewer.com/) - 用于查看 PHP 代码抽象语法树的工具。
* [PHP Magic Number Detector](https://github.com/povils/phpmnd) - 检测代码中幻数的库。
* [PHP Parser](https://github.com/nikic/PHP-Parser) - 用 PHP 编写的 PHP 解析器。
* [PHP Semantic Versioning Checker](https://github.com/tomzx/php-semver-checker) - 一个命令行实用程序，用于比较两个源集并确定要应用的适当语义版本控制。
* [Phpactor](https://github.com/phpactor/phpactor) - PHP 补全、重构和自省工具。
* [PHPQA](https://github.com/EdgedesignCZ/phpqa) - 用于运行 QA 工具（phploc、phpcpd、phpcs、pdepend、phpmd、phpmetrics）的工具。
* [Rector](https://github.com/rectorphp/rector) - 升级和重构代码的工具。
* [Scrutinizer](https://scrutinizer-ci.com/) - 用于[检查 PHP 代码](https://github.com/scrutinizer-ci/php-analyzer) 的 Web 工具。
* [UBench](https://github.com/devster/ubench) - 一个简单的微基准库。

### 代码质量
*用于管理代码质量、格式和 linting 的库。*

* [CaptainHook](https://github.com/captainhook-git/captainhook) - 一个易于使用且灵活的 Git 挂钩库。
* [Laravel Pint](https://github.com/laravel/pint) - Laravel 的编码标准修复程序库。
* [PHP CodeSniffer](https://github.com/PHPCSStandards/PHP_CodeSniffer) - 一个可以检测并自动修复 PHP、CSS 和 JS 编码标准违规行为的库。
* [PHP CS Fixer](https://github.com/PHP-CS-Fixer/PHP-CS-Fixer) - 编码标准修复程序库。
* [PHP CS Fixer Configurator](https://mlocati.github.io/php-cs-fixer-configurator/) - 帮助配置 PHP CS Fixer 规则集的 Web 应用程序。
* [PHP Mess Detector](https://github.com/phpmd/phpmd) - 一个扫描代码中错误、次优代码、未使用的参数等的库。
* [PHPCheckstyle](https://github.com/PHPCheckstyle/phpcheckstyle) - 帮助遵守某些编码约定的工具。

### 静态分析
*用于执行 PHP 代码静态分析的库。*

* [Dead Code Detector](https://github.com/shipmonk-rnd/dead-code-detector) - 用于查找未使用的 PHP 代码的 PHPStan 扩展。
* [Deptrac](https://github.com/deptrac/deptrac) - 用于在架构层之间强制执行依赖关系规则的静态分析工具。
* [Exakat](https://github.com/exakat/exakat) - PHP 的静态分析引擎。
* [Larastan](https://github.com/larastan/larastan) - Laravel 的 PHPStan 包装器，为 Laravel 项目添加静态分析。
* [Mago](https://github.com/carthage-software/mago) - 旨在改善开发人员体验的 PHP 工具链。
* [phan](https://github.com/phan/phan) - 基于 PHP 7+ 和 php-ast 扩展的静态分析器。
* [PHP Architecture Tester](https://github.com/carlosas/phpat) - 易于使用的 PHP 架构测试工具。
* [PHPCompatibility](https://github.com/PHPCompatibility/PHPCompatibility) - PHP CodeSniffer 的 PHP 兼容性检查器。
* [PHPDoc Parser](https://github.com/phpstan/phpdoc-parser) - 下一代 phpDoc 解析器，支持交集类型和泛型。
* [PHP Metrics](https://github.com/phpmetrics/PhpMetrics) - 静态度量库。
* [PHPStan](https://github.com/phpstan/phpstan) - PHP静态分析工具。
* [Psalm](https://github.com/vimeo/psalm) - 用于查找 PHP 应用程序中错误的静态分析工具。

### 建筑
*与设计模式、编程方法和组织代码方式相关的库。*

* [Design Patterns PHP](https://github.com/DesignPatternsPHP/DesignPatternsPHP) - 用 PHP 实现的软件模式存储库。
* [Finite](https://github.com/yohang/Finite) - 一个简单的 PHP 有限状态机。
* [Functional PHP](https://github.com/lstrojny/functional-php) - 一个函数式编程库。
* [Iter](https://github.com/nikic/iter) - 使用生成器提供迭代原语的库。
* [IterTools PHP](https://github.com/markrogoyski/itertools-php) - 提供使用可迭代实体的功能的库（类似于 Python 中的 itertools 库）。
* [Pipeline](https://github.com/thephpleague/pipeline) - 管道模式实现。
* [Porter](https://github.com/ScriptFUSION/Porter) - 用于使用 Web API 和其他数据源的数据导入抽象库。
* [RulerZ](https://github.com/K-Phoen/rulerz) - 强大的规则引擎和规范模式的实现。

### 调试和分析
*用于调试错误和分析代码的库和工具。*

* [APM](https://pecl.php.net/package/APM) - 监控扩展将错误和统计信息收集到 SQLite/MySQL/StatsD 中。
* [Barbushin PHP Console](https://github.com/barbushin/php-console) - 另一个使用 Google Chrome 的 Web 调试控制台。
* [Kint](https://github.com/kint-php/kint) - 调试和分析工具。
* [LaraDumps](https://github.com/laradumps/laradumps) - 具有专用桌面应用程序的 Laravel 调试工具。
* [Metrics](https://github.com/beberlei/metrics) - 一个简单的指标 API 库。
* [PCOV](https://github.com/krakjoe/pcov) - 一个独立的代码覆盖兼容驱动程序。
* [PHP Console](https://github.com/Seldaek/php-console) - Web 调试控制台。
* [PHP Debug Bar](https://php-debugbar.com/) - 调试工具栏。
* [PHPBench](https://github.com/phpbench/phpbench) - 基准测试框架。
* [PHPSpy](https://github.com/adsr/phpspy) - 低开销采样分析器。
* [Symfony VarDumper](https://github.com/symfony/var-dumper) - 可变转储器组件。
* [Tracy](https://github.com/nette/tracy) - 一个简单的错误检测、记录和时间测量库。
* [Trap](https://github.com/buggregator/trap) - 带有 Web 界面和 IDE 插件的扩展变量转储程序。
* [Whoops](https://github.com/filp/whoops) - 一个漂亮的错误处理库。
* [xDebug](https://github.com/xdebug/xdebug) - PHP 的调试和分析工具。
* [XHProf](https://github.com/phacility/xhprof) - 最初由 Facebook 开发的分析工具。
* [Z-Ray](https://www.zend.com/products/z-ray) - Zend Server 的调试和配置工具。

### 错误跟踪和监控服务
*自托管或基于云的应用程序性能监控和错误跟踪工具*

* [Blackfire](https://www.blackfire.io) - 低开销的代码分析器。
* [Buggregator](https://buggregator.dev) - 聚合 var-dump、分析数据、电子邮件、日志和 Sentry 事件的调试服务器。
* [BugSnag](https://www.bugsnag.com/) - 错误和真实用户监控。
* [Honeybadger](https://www.honeybadger.io/) - 开发人员的错误跟踪和应用程序监控。
* [Rollbar](https://rollbar.com/) - 面向软件团队的错误记录和跟踪服务。
* [Sentry](https://sentry.io/welcome/) - 应用程序性能监控和错误跟踪软件。
* [Tideways](https://tideways.com/) - 监控和分析工具。

### 构建工具
*项目构建和自动化工具。*

* [Box](https://github.com/box-project/box) - 构建 PHAR 文件的实用程序。
* [PHPacker](https://github.com/phpacker/phpacker) - PHAR 构建器，可将 PHP 应用程序编译为独立的可执行文件。
* [Phing](https://www.phing.info/) - 受 Apache Ant 启发的 PHP 项目构建系统。
* [RMT](https://github.com/liip/RMT) - 用于版本控制和发布软件的库。

### 任务运行器
*用于自动化和运行任务的库。*

* [Jobby](https://github.com/jobbyphp/jobby) - 无需修改 crontab 的 PHP cron 作业管理器。
* [Robo](https://github.com/consolidation/Robo) - 具有面向对象配置的 PHP 任务运行程序。

### 导航
*用于构建导航结构的工具。*

* [KnpMenu](https://github.com/KnpLabs/KnpMenu) - 菜单库。
* [Menu](https://github.com/spatie/menu) - 具有流畅界面的灵活菜单库。

### 资产管理
*用于管理、压缩和缩小网站资产的工具。*

* [JShrink](https://github.com/tedious/JShrink) - JavaScript 压缩器库。
* [Laravel Mix](https://github.com/laravel-mix/laravel-mix) - 一个优雅的 Webpack 包装器，适用于 80% 的用例。
* [Symfony Asset](https://github.com/symfony/asset) - 管理 Web 资产的 URL 生成和版本控制。
* [Symfony Encore](https://github.com/symfony/webpack-encore) - 一个简单但功能强大的 API，用于处理和编译围绕 Webpack 构建的资产。

### 地理定位
*用于对地址进行地理编码并处理纬度和经度的库。*

* [Country List](https://github.com/umpirsky/country-list) - 所有国家/地区及其名称和 ISO 3166-1 代码的列表。
* [GeoCoder](https://geocoder-php.org/) - 地理编码库。
* [GeoJSON](https://github.com/jmikola/geojson) - GeoJSON 实现。
* [GeoTools](https://github.com/thephpleague/geotools) - 地理相关工具库。
* [PHPGeo](https://github.com/mjaschen/phpgeo) - 一个简单的地理库。

### 日期和时间
*用于处理日期和时间的库。*

* [Business Time](https://github.com/kylekatarnls/business-time) - 用于处理营业时间和工作日的 Carbon 扩展。
* [CalendR](https://github.com/yohang/CalendR) - 日历管理库。
* [Carbon](https://github.com/briannesbitt/Carbon) - 一个简单的 DateTime API 扩展。
* [Chronos](https://github.com/cakephp/chronos) - DateTime API 扩展支持可变和不可变日期/时间。
* [Moment.php](https://github.com/fightbulc/moment.php) - Moment.js 启发了具有 i18n 支持的 PHP DateTime 处理程序。
* [PHP RRule](https://github.com/rlanvin/php-rrule) - 一个基于 iCalendar RRule 规范处理重复日期和时间的库。
* [Yasumi](https://github.com/azuyalabs/yasumi) - 帮助您计算假期日期和名称的库。

### 活动
*事件驱动或实现非阻塞事件循环的库。*

* [Amp](https://github.com/amphp/amp) - 事件驱动的非阻塞 I/O 库。
* [Broadway](https://github.com/broadway/broadway) - 事件源和 CQRS 库。
* [CakePHP Event](https://github.com/cakephp/event) - 事件调度程序库。
* [Elephant.io](https://github.com/ElephantIO/elephant.io) - 另一个网络套接字库。
* [Evenement](https://github.com/igorw/evenement) - 事件调度程序库。
* [Event](https://github.com/thephpleague/event) - 专注于领域事件的事件库。
* [Fast CGI Client](https://github.com/hollodotme/fast-cgi-client) - 客户端通过 php-fpm 套接字发出同步/异步请求。
* [FrankenPHP](https://frankenphp.dev/) - 用 Go 编写的现代 PHP 应用服务器。
* [Pawl](https://github.com/ratchetphp/Pawl) - 异步 Web 套接字客户端。
* [Prooph Event Store](https://github.com/prooph/event-store) - 用于保存事件消息的事件源组件。
* [PHP Defer](https://github.com/php-defer/php-defer) - Golang 针对 PHP 的 defer 语句。
* [Ratchet](https://github.com/ratchetphp/Ratchet) - 一个网络套接字库。
* [ReactPHP](https://github.com/reactphp/reactphp) - 事件驱动的非阻塞 I/O 库。
* [RxPHP](https://github.com/ReactiveX/RxPHP) - 反应式扩展库。
* [Swoole](https://github.com/swoole/swoole-src) - 一个用 C 语言编写的高性能 PHP 事件驱动异步并发网络通信框架。
* [Workerman](https://github.com/walkor/Workerman) - 事件驱动的非阻塞 I/O 库。

### 记录
*用于生成和使用日志文件的库。*

* [Monolog](https://github.com/Seldaek/monolog) - 综合记录器。

### 电子商务
*用于接受付款和建立在线电子商务商店的库和应用程序。*

* [Money](https://github.com/moneyphp/money) - Fowler 货币模式的 PHP 实现。
* [Brick Money](https://github.com/brick/money) - PHP 货币库，支持上下文、现金舍入、货币转换。
* [OmniPay](https://github.com/thephpleague/omnipay) - 与框架无关的多网关支付处理库。
* [Payum](https://github.com/payum/payum) - 支付抽象库。
* [Shopsys Framework](https://github.com/shopsys/shopsys/) - 面向内部开发团队的开源电子商务平台。
* [Shopware](https://github.com/shopware/shopware) - 高度可定制的电子商务软件。
* [Swap](https://github.com/florianv/swap) - 汇率库。
* [Sylius](https://sylius.com/) - 开源电子商务解决方案。

### PDF
*用于处理 PDF 文件的库和软件。*

* [Browsershot](https://github.com/spatie/browsershot) - 将 HTML 转换为图像、PDF 或字符串。
* [Dompdf](https://github.com/dompdf/dompdf) - HTML 到 PDF 转换器。
* [Gotenberg](https://github.com/gotenberg/gotenberg-php) - 用于与 Gotenberg 交互的 PHP 客户端。
* [Snappy](https://github.com/KnpLabs/snappy) - PDF 和图像生成库。
* [TCPDF](https://tcpdf.org/) - 用于生成 PDF 文档的开源 PHP 类。

### 办公室
*用于处理办公套件文档的库。*

* [PHPPowerPoint](https://github.com/PHPOffice/PHPPresentation) - 用于处理 Microsoft PowerPoint 演示文稿的库。
* [PHPWord](https://github.com/PHPOffice/PHPWord) - 用于处理 Microsoft Word 文档的库。
* [PHPSpreadsheet](https://github.com/PHPOffice/PhpSpreadsheet) - 用于读取和写入电子表格文件的纯 PHP 库（PHPExcel 的继承者）。
* [OpenSpout](https://github.com/openspout/openspout) - 社区驱动的“box/spout”分支，是一个 PHP 库，用于以快速且可扩展的方式读取和写入电子表格文件（CSV、XLSX 和 ODS）。

### 数据库
*使用对象关系映射（ORM）或数据映射技术与数据库交互的库。*

* [Atlas.Orm](https://github.com/atlasphp/Atlas.Orm) - PHP 中持久模型的数据映射器实现。
* [Aura.Sql](https://github.com/auraphp/Aura.Sql) - 提供对本机 PDO 的扩展以及分析器和连接定位器。
* [Aura.SqlQuery](https://github.com/auraphp/Aura.SqlQuery) - 适用于 MySQL、PostgreSQL、SQLite 和 Microsoft SQL Server 的独立查询构建器。
* [Baum](https://github.com/etrepat/baum) - Eloquent 的嵌套集实现。
* [CakePHP ORM](https://github.com/cakephp/orm) - 对象关系映射器，使用 DataMapper 模式实现。
* [Cycle ORM](https://github.com/cycle/orm) - PHP 数据映射器、ORM。
* [Doctrine Extensions](https://github.com/doctrine-extensions/DoctrineExtensions) - Doctrine 行为扩展的集合。
* [Doctrine](https://www.doctrine-project.org/) - 全面的 DBAL 和 ORM。
* [Laravel Eloquent](https://github.com/illuminate/database) - 一个简单的 ORM。
* [ProxyManager](https://github.com/Ocramius/ProxyManager) - 一组用于为数据映射器生成代理对象的实用程序。
* [RedBean](https://redbeanphp.com/index.php) - 一个轻量级、无配置的 ORM。
* [Slimdump](https://github.com/webfactory/slimdump) - 一个简单的 MySQL 转储工具。
* [Spot2](https://github.com/spotorm/spot2) - MySQL 数据映射器 ORM。

### 迁移
*帮助管理数据库模式和迁移的库。*

* [Doctrine Migrations](https://www.doctrine-project.org/projects/migrations.html) - Doctrine 的迁移库。
* [Phinx](https://github.com/cakephp/phinx) - 另一个数据库迁移库。
* [PHPMig](https://github.com/davedevelopment/phpmig) - 另一个迁移管理库。
* [Ruckusing](https://github.com/ruckus/ruckusing-migrations) - PHP 的数据库迁移和 ActiveRecord 迁移，支持 MySQL、Postgres、SQLite。

### NoSQL
*用于使用“NoSQL”后端的库。*

* [MongoDB](https://github.com/mongodb/mongo-php-driver) - MongoDB PHP 驱动程序。
* [MongoDB PHP Library](https://github.com/mongodb/mongo-php-library) - 官方高级 MongoDB PHP 库构建在 MongoDB PHP 驱动程序之上。
* [Predis](https://github.com/predis/predis) - 功能齐全的 Redis 库。

### 队列
*用于处理事件和任务队列的库。*

* [BunnyPHP](https://github.com/jakubkulhan/bunny) - 一个高性能的纯 PHP AMQP (RabbitMQ) 同步和异步 (ReactPHP) 库。
* [Pheanstalk](https://github.com/pheanstalk/pheanstalk) - Beanstalkd 客户端库。
* [PHP AMQP](https://github.com/php-amqplib/php-amqplib) - 一个纯 PHP AMQP 库。
* [Tarantool Queue](https://github.com/tarantool-php/queue) - Tarantool 队列的 PHP 绑定。
* [Thumper](https://github.com/php-amqplib/Thumper) - RabbitMQ 模式库。
* [Enqueue](https://github.com/php-enqueue/enqueue-dev) - PHP 的消息队列包，支持 RabbitMQ、AMQP、STOMP、Amazon SQS、Redis 和 Doctrine 传输。

### 搜索
*用于对数据进行索引和执行搜索查询的库和软件。*

* [Elastica](https://github.com/ruflin/Elastica) - ElasticSearch 的客户端库。
* [ElasticSearch PHP](https://github.com/elastic/elasticsearch-php) - [ElasticSearch](https://www.elastic.co/) 的官方客户端库。
* [Solarium](https://www.solarium-project.org/) - [Solr](https://solr.apache.org/) 的客户端库。
* [SphinxQL Query Builder](https://foolcode.github.io/SphinxQL-Query-Builder/) - 用于 [Sphinx](https://sphinxsearch.com/) 和 [Manticore](https://manticoresearch.com/) 搜索引擎的查询库。

### 命令行
*与命令行相关的库。*

* [Aura.Cli](https://github.com/auraphp/Aura.Cli) - 为命令行界面提供相当于请求 ( Context ) 和响应 ( Stdio ) 对象，包括 Getopt 支持，以及用于描述命令的独立帮助对象。
* [CLI Menu](https://github.com/php-school/cli-menu) - 用于构建 CLI 菜单的库。
* [CLIFramework](https://github.com/c9s/CLIFramework) - 一个支持 zsh/bash 补全生成、子命令和选项约束的命令行框架。它还为 phpbrew 提供支持。
* [CLImate](https://github.com/thephpleague/climate) - 用于输出颜色和特殊格式的库。
* [Commando](https://github.com/nategood/commando) - 另一个简单的命令行选项解析器。
* [Cron Expression](https://github.com/mtdowling/cron-expression) - 计算 cron 运行日期的库。
* [GetOpt](https://github.com/getopt-php/getopt-php) - 命令行 opt 解析器。
* [GetOptionKit](https://github.com/c9s/GetOptionKit) - 另一个命令行选项解析器。
* [PsySH](https://github.com/bobthecow/psysh) - 另一个 PHP REPL。
* [ShellWrap](https://github.com/MrRio/shellwrap) - 一个简单的命令行包装库。

### 认证与授权
*用于实现用户身份验证和授权的库。*

* [Aura.Auth](https://github.com/auraphp/Aura.Auth) - 使用各种适配器提供身份验证功能和会话跟踪。
* [SocialConnect Auth](https://github.com/socialConnect/auth) - 开源社交标志 (OAuth1\OAuth2\OpenID\OpenIDConnect)。
* [Json Web Token](https://github.com/lcobucci/jwt) - 用于验证和传输信息的 Json 令牌。
* [OAuth 1.0 Client](https://github.com/thephpleague/oauth1-client) - OAuth 1.0 客户端库。
* [OAuth 2.0 Client](https://github.com/thephpleague/oauth2-client) - OAuth 2.0 客户端库。
* [OAuth2 Server](https://bshaffer.github.io/oauth2-server-php-docs/) - 另一个 OAuth2 服务器实现。
* [OAuth2 Server](https://oauth2.thephpleague.com/) - OAuth2 身份验证服务器、资源服务器和客户端库。
* [Paseto](https://github.com/paragonie/paseto) - 与平台无关的安全令牌。
* [PHP oAuthLib](https://github.com/daviddesberg/PHPoAuthLib) - 另一个 OAuth 库。
* [TwitterOAuth](https://github.com/abraham/twitteroauth) - Twitter OAuth 库。

### 标记和 CSS
*用于处理标记和 CSS 格式的库。*

* [Cebe Markdown](https://github.com/cebe/markdown) - 一个快速且可扩展的 Markdown 解析器。
* [CommonMark PHP](https://github.com/thephpleague/commonmark) - 高度可扩展的 Markdown 解析器，完全支持 [CommonMark 规范](https://spec.commonmark.org/)。
* [Decoda](https://github.com/milesj/decoda) - 一个轻量级标记解析器库。
* [Djot](https://github.com/php-collective/djot-php) - [Djot](https://djot.net/) 的 PHP 解析器，一种现代轻标记语言（Markdown 的继承者）。
* [Essence](https://github.com/essence/essence) - 用于提取网络媒体的库。
* [Embera](https://github.com/mpratt/Embera) - Oembed 消费者库。
* [HTML to Markdown](https://github.com/thephpleague/html-to-markdown) - 将 HTML 转换为 Markdown。
* [HTML5 PHP](https://github.com/Masterminds/html5-php) - HTML5 解析器和序列化器库。
* [Parsedown](https://github.com/erusev/parsedown) - 另一个 Markdown 解析器。
* [PHP CSS Parser](https://github.com/MyIntervals/PHP-CSS-Parser) - 用 PHP 编写的 CSS 文件解析器。
* [PHP Markdown](https://github.com/michelf/php-markdown) - 一个 Markdown 解析器。
* [Shiki PHP](https://github.com/spatie/shiki-php) - PHP 中的 [Shiki](https://github.com/shikijs/shiki) 代码高亮包。
* [VObject](https://github.com/sabre-io/vobject) - 用于解析 VCard 和 iCalendar 对象的库。

### JSON
*用于使用 JSON 的库。*

* [JSON Lint](https://github.com/Seldaek/jsonlint) - 一个 JSON lint 实用程序。
* [JSONMapper](https://github.com/JsonMapper/JsonMapper) - 用于将 JSON 映射到 PHP 对象的库。
* [Lazy JSON](https://github.com/cerbero90/lazy-json) - 适用于大型 JSON 文件的内存高效惰性解析器。

### 弦乐
*用于解析和操作字符串的库。*

* [Agent](https://github.com/jenssegers/agent) - 一个基于 MobileDetect 的 PHP 桌面/移动用户代理解析器。
* [ANSI to HTML5](https://github.com/sensiolabs/ansi-to-html) - ANSI 到 HTML5 转换器库。
* [Color Jizz](https://github.com/mikeemoo/ColorJizz-PHP) - 用于操作和转换颜色的库。
* [Device Detector](https://github.com/matomo-org/device-detector) - 另一个用于解析用户代理字符串的库。
* [Hyphenation](https://github.com/heiglandreas/Org_Heigl_Hyphenator) - 基于 TeX 连字符算法的文本连字符。
* [Jieba-PHP](https://github.com/fukuball/jieba-php) - Python jieba 的 PHP 移植。用于自然语言处理的中文文本分割。
* [Mobile-Detect](https://github.com/serbanghita/Mobile-Detect) - 用于检测移动设备（包括平板电脑）的轻量级 PHP 类。
* [Patchwork UTF-8](https://github.com/nicolas-grekas/Patchwork-UTF8) - 用于处理 UTF-8 字符串的可移植库。
* [Portable ASCII](https://github.com/voku/portable-ascii) - 将字符串转换为 ASCII 的库。
* [Portable UTF-8](https://github.com/voku/portable-utf8) - 具有 UTF-8 安全替换方法的字符串操作库。
* [Slugify](https://github.com/cocur/slugify) - 将字符串转换为 slugs 的库。
* [SQL Formatter](https://github.com/jdorn/sql-formatter/) - 用于格式化 SQL 语句的库。
* [Stringy](https://github.com/voku/Stringy) - 具有多字节支持的字符串操作库。
* [Url highlight](https://github.com/vstelmakh/url-highlight) - 用于从文本中解析 URL 并将其转换为可点击链接的库。
* [URLify](https://github.com/jbroadway/urlify) - Django 的 URLify.js 的 PHP 端口。
* [UUID](https://github.com/ramsey/uuid) - 用于生成 UUID 的库。

### 数字
*用于处理数字的库。*

* [Brick Math](https://github.com/brick/math) - 提供大量支持的库：“BigInteger”、“BigDecimal”和“BigRational”。
* [ByteUnits](https://github.com/gabrielelana/byte-units) - 用于解析、格式化和转换二进制和公制字节单位的库。
* [DecimalObject](https://github.com/php-collective/decimal-object) - 一个值对象，可以轻松且更精确地处理小数/浮点数。
* [IP](https://github.com/darsyn/ip) - 用于处理 IPv4 和 IPv6 地址的不可变值对象。
* [PHP Conversion](https://github.com/cniska/php-conversion) - 另一个用于在测量单位之间进行转换的库。
* [PHP Units of Measure](https://github.com/triplepoint/php-units-of-measure) - 用于在测量单位之间进行转换的库。
* [MathPHP](https://github.com/markrogoyski/math-php) - PHP 的数学库。

### 过滤、净化和验证
*用于过滤、清理和验证数据的库。*

* [Assert](https://github.com/beberlei/assert) - 具有丰富断言集的验证库。支持断言链接和惰性断言。
* [Aura.Filter](https://github.com/auraphp/Aura.Filter) - 提供用于验证和清理对象和数组的工具。
* [CakePHP Validation](https://github.com/cakephp/validation) - 另一个验证库。
* [Filterus](https://github.com/ircmaxell/filterus) - 一个简单的 PHP 过滤库。
* [HTML Purifier](https://github.com/ezyang/htmlpurifier) - 符合标准的 HTML 过滤器。
* [ISO-codes](https://github.com/ronanguilloux/IsoCodes) - 一个根据 ISO、国际金融、公共管理、GS1、图书行业、许多国家的电话号码和邮政编码的标准验证输入的库。
* [JSON Schema](https://github.com/jsonrainbow/json-schema) - 一个 [JSON Schema](https://json-schema.org/) 验证库。
* [LibPhoneNumber for PHP](https://github.com/giggsey/libphonenumber-for-php) - Google 电话号码处理库的 PHP 实现。
* [MetaYaml](https://github.com/romaricdrigon/MetaYaml) - 支持 YAML、JSON 和 XML 的模式验证库。
* [Respect Validation](https://github.com/Respect/Validation) - 一个简单的验证库。
* [Symfony HTML Sanitizer](https://github.com/symfony/html-sanitizer) - 一个 HTML 清理程序库。
* [Valitron](https://github.com/vlucas/valitron) - 另一个验证库。
* [Valinor](https://github.com/CuyZ/Valinor) - 用于映射到强类型值对象的库。
* [Volan](https://github.com/serkin/Volan) - 另一个简化的验证库。

### 应用程序编程接口
*用于开发 API 的库和网络工具。*

* [API Platform](https://api-platform.com) - 在几分钟内公开一个包含 JSON-LD、Hydra 格式的超媒体 REST API。
* [Laminas API Tool Skeleton](https://github.com/laminas-api-tools/api-tools-skeleton) - 使用 Laminas 框架构建的 API 构建器。
* [HAL](https://github.com/blongden/hal) - 超文本应用程序语言 (HAL) 构建器库。
* [Hateoas](https://github.com/willdurand/Hateoas) - HATEOAS REST Web 服务库。
* [Jane](https://github.com/janephp/janephp/) - 具有验证支持的 OpenApi 客户端生成器。
* [Negotiation](https://github.com/willdurand/Negotiation) - 内容协商库。
* [Restler](https://github.com/Luracast/Restler) - 一个轻量级框架，将 PHP 方法公开为 RESTful Web API。
* [PackageGenerator](https://github.com/WsdlToPhp/PackageGenerator) - 包生成器从任何 WSDL 生成 PHP SDK。

### 缓存和锁定
*用于缓存数据和获取锁的库。*

* [APIx Cache](https://github.com/apix/cache) - 各种缓存后端的精简 PSR-6 缓存包装器，强调缓存标记和索引。
* [CacheTool](https://github.com/gordalina/cachetool) - 从命令行清除 APC/操作码缓存的工具。
* [CakePHP Cache](https://github.com/cakephp/cache) - 一个缓存库。
* [Doctrine Cache](https://github.com/doctrine/cache) - 一个缓存库。
* [Metaphore](https://github.com/sobstel/metaphore) - 使用信号量进行缓存猛击防御来防止狗堆效应。
* [Stash](https://github.com/tedious/Stash) - 另一个用于缓存的库。
* [Laminas Cache](https://github.com/laminas/laminas-cache) - 另一个缓存库。
* [Lock](https://github.com/php-lock/lock) - 提供独占执行的锁库。

### 数据结构和存储
*实现数据结构或存储技术的库。*

* [CakePHP Collection](https://github.com/cakephp/collection) - 一个简单的集合库。
* [Fractal](https://github.com/thephpleague/fractal) - 用于将复杂数据结构转换为 JSON 输出的库。
* [JsonMapper](https://github.com/cweiske/jsonmapper) - 将嵌套 JSON 结构映射到 PHP 类的库。
* [JSON Machine](https://github.com/halaxa/json-machine) - 使用简单的“foreach”提供对巨大 JSON 的迭代。
* [msgpack.php](https://github.com/rybakit/msgpack.php) - [MessagePack](https://msgpack.org/) 序列化格式的纯 PHP 实现。
* [Serializer](https://github.com/schmittjoh/serializer) - 用于序列化和反序列化数据的库。
* [YaLinqo](https://github.com/Athari/YaLinqo) - 另一个 PHP 的 LINQ to Objects。
* [Laminas Serializer](https://github.com/laminas/laminas-serializer) - 另一个用于序列化和反序列化数据的库。

### 通知
*用于使用通知软件的库。*

* [JoliNotif](https://github.com/jolicode/JoliNotif) - 用于桌面通知的跨平台库（支持 Growl、通知发送、烤面包机等）。

### 部署
*用于项目部署的库。*

* [Deployer](https://github.com/deployphp/deployer) - 一个部署工具。
* [Envoy](https://github.com/laravel/envoy) - 一个使用 PHP 运行 SSH 任务的工具。

### 国际化和本地化
*国际化 (I18n) 和本地化 (L10n) 库。*

* [Aura.Intl](https://github.com/auraphp/Aura.Intl) - 提供国际化 (I18N) 工具，特别是面向包的按区域设置消息翻译。
* [CakePHP I18n](https://github.com/cakephp/i18n) - 日期和数字的消息翻译和本地化。

### 无服务器
*帮助构建无服务器 Web 应用程序的库和工具。*

* [Bref](https://bref.sh/) - AWS Lambda 上的无服务器 PHP。
* [OpenWhisk](https://openwhisk.apache.org/) - 开源无服务器云平台。
* [Serverless Framework](https://www.serverless.com/framework) - 用于构建无服务器应用程序的开源框架。
* [Laravel Vapor](https://vapor.laravel.com/) - 由 AWS 提供支持的 Laravel 无服务器部署平台。

### 配置
*用于配置的库和工具。*

* [PHP Dotenv](https://github.com/vlucas/phpdotenv) - 从“.env”文件解析并加载环境变量。
* [Symfony Dotenv](https://github.com/symfony/dotenv) - 从“.env”文件解析并加载环境变量。
* [Toml](https://github.com/php-collective/toml) - 具有 AST 访问和错误恢复功能的 TOML 解析器和编码器。

### 法学硕士
*用于处理大型语言模型的库。*

* [Anthropic](https://github.com/mozex/anthropic-php) - Anthropic API 的 PHP 客户端，支持消息、流、工具使用和批处理。
* [Anthropic for Laravel](https://github.com/mozex/anthropic-laravel) - 用于 Anthropic PHP 客户端的 Laravel 包装器，具有外观、配置发布和测试假货。
* [Instructor for PHP](https://github.com/cognesy/instructor-php) - 法学硕士以 PHP 进行结构化数据输出。
* [LLPhant](https://github.com/LLPhant/LLPhant) - 使用 OpenAI GPT 4 的综合 PHP 生成式 AI 框架。受到 Langchain 的启发。
* [OpenAI Client](https://github.com/openai-php/client) - OpenAI PHP 是一个由社区维护的强大 PHP API 客户端，可让您与 OpenAI API 进行交互。
* [OpenAI Client for Laravel](https://github.com/openai-php/laravel) - OpenAI PHP for Laravel 是一个强大的 PHP API 客户端，可让您与 OpenAI API 进行交互。
* [PHP Mistral AI SDK](https://github.com/SoftCreatR/php-mistral-ai-sdk) - 适用于 Mistral AI API 的强大且易于使用的 PHP SDK，允许将先进的 AI 驱动功能无缝集成到您的 PHP 项目中。

### 第三方API
*用于访问第三方 API 的库。*

* [Amazon Web Service SDK](https://github.com/aws/aws-sdk-php) - 官方 PHP AWS SDK 库。
* [AsyncAWS](https://async-aws.com/) - 一个非官方的异步 PHP AWS SDK。
* [Campaign Monitor](https://campaignmonitor.github.io/createsend-php/) - 官方 Campaign Monitor PHP 库。
* [Github](https://github.com/KnpLabs/php-github-api) - 与 Github API 交互的库。
* [Mailgun](https://github.com/mailgun/mailgun-php) - 官方 Mailgun PHP API。
* [Stripe](https://github.com/stripe/stripe-php) - 官方 Stripe PHP 库。
* [Twilio](https://github.com/twilio/twilio-php) - 官方 Twilio PHP REST API。

### 扩展
*帮助构建 PHP 扩展的库。*

* [PHP CPP](https://www.php-cpp.com/) - 用于开发 PHP 扩展的 C++ 库。
* [Zephir](https://github.com/zephir-lang/zephir) - 一种介于 PHP 和 C++ 之间的编译语言，用于开发 PHP 扩展。

### 杂项
*不属于上述类别的有用的库或实用程序。*

* [Annotations](https://github.com/doctrine/annotations) - 注释库（Doctrine 的一部分）。
* [BotMan](https://github.com/botman/botman) - 一个与框架无关的 PHP 库，用于构建跨平台聊天机器人。
* [ClassPreloader](https://github.com/ClassPreloader/ClassPreloader) - 用于优化自动加载的库。
* [Ganesha](https://github.com/ackintosh/ganesha) - 断路器模式的 PHP 实现。
* [Hprose-PHP](https://github.com/hprose/hprose-php) - 跨语言 RPC。
* [Laravel Serializable Closure](https://github.com/laravel/serializable-closure) - 允许序列化闭包的库。
* [noCAPTCHA](https://github.com/ARCANEDEV/noCAPTCHA) - Google noCAPTCHA (reCAPTCHA) 的助手。
* [Pagerfanta](https://github.com/whiteoctober/Pagerfanta) - 一个分页库。
* [Safe](https://github.com/thecodingmachine/safe) - 所有 PHP 函数都被重写为抛出异常而不是返回 false。

# 软件
*用于创建开发环境的软件。*

### PHP安装
*帮助在计算机上安装和管理 PHP 的工具。*

* [Brew PHP Switcher](https://github.com/philcook/brew-php-switcher) - Brew PHP 切换器。
* [Homebrew](https://brew.sh/) - 适用于 macOS 的包管理器。
* [PHP Brew](https://github.com/phpbrew/phpbrew) - PHP 版本管理器和安装程序。
* [PHP Build](https://github.com/php-build/php-build) - 另一个 PHP 版本安装程序。
* [Static PHP CLI](https://github.com/crazywhalecc/static-php-cli) - 构建或[下载](https://dl.static-php.dev/static-php-cli/) PHP CLI 和 FPM 的静态版本。

### 开发环境
*用于创建和共享开发环境的软件和工具。*

* [Ansible](https://www.redhat.com/en/ansible-collaborative) - 一个极其简单的编排框架。
* [DDEV](https://github.com/ddev/ddev) - PHP的本地Web开发环境系统。
* [Docker](https://www.docker.com/) - 容器化平台。
* [Docker PHP Extension Installer](https://github.com/mlocati/docker-php-extension-installer) - 在 Docker 容器中轻松安装 PHP 扩展。
* [Docksal](https://github.com/docksal/docksal) - 统一的 Docker :whale：支持 macOS、Windows 和 Linux 的 Web 开发环境。
* [Expose](https://github.com/exposedev/expose) - 开源 PHP 隧道服务。
* [Lando](https://lando.dev/) - 按钮式开发环境。
* [Laravel Homestead](https://laravel.com/docs/master/homestead) - Laravel 的本地开发环境。
* [Laravel Herd](https://herd.laravel.com/windows) - 适用于 macOS 和 Windows 的一键式 PHP 开发环境。
* [Laradock](https://laradock.io/) - 基于Docker的完整PHP开发环境。
* [PHPMon](https://phpmon.app/) - 用于管理 PHP 安装的 macOS 菜单栏应用程序（与 [Laravel Valet](https://laravel.com/docs/master/valet) 配合使用）。
* [Puppet](https://www.puppet.com) - 服务器自动化框架和应用程序。
* [Solo](https://github.com/soloterm/solo) - 用于管理 Laravel 应用程序进程的终端应用程序。
* [Takeout](https://github.com/tighten/takeout) - 基于 Docker 的仅供开发的依赖管理器。
* [Vagrant](https://developer.hashicorp.com/vagrant) - 便携式开发环境实用程序。

### 虚拟机
*替代 PHP 虚拟机。*

* [Hack](https://hacklang.org/) - HHVM 的编程语言。
* [HHVM](https://github.com/facebook/hhvm) - Facebook 的 PHP 虚拟机、运行时和 JIT。
* [PeachPie](https://github.com/peachpiecompiler/peachpie) - 适用于 .NET 和 .NET Core 的 PHP 编译器和运行时。

### 文本编辑器和 IDE
*支持 PHP 的文本编辑器和集成开发环境 (IDE)。*

* [Eclipse for PHP Developers](https://www.eclipse.org/downloads/) - 基于Eclipse平台的PHP IDE。
* [Apache NetBeans](https://netbeans.apache.org/front/main/index.html) - 支持 PHP 和 HTML5 的 IDE。
* [PhpEd](https://www.nusphere.com/products/phped.htm) - 带有专业商业调试器的IDE。
* [PhpStorm](https://www.jetbrains.com/phpstorm/) - 商业 PHP IDE。
* [VS Code](https://code.visualstudio.com/) - 一个开源代码编辑器。

### 网络应用程序
*基于网络的应用程序和工具。*

* [3V4L](https://3v4l.org/) - 在线 PHP 和 HHVM shell。
* [Adminer](https://www.adminer.org/en/) - 在单个 PHP 文件中进行数据库管理。
* [Cachet](https://github.com/cachethq/cachet) - 开源状态页面系统。
* [Lychee](https://github.com/electerious/Lychee) - 一个易于使用且美观的照片管理系统。
* [Leantime](https://leantime.io) - 适用于非项目经理的战略项目管理系统。
* [MailCatcher](https://github.com/sj26/mailcatcher) - 用于捕获和查看电子邮件的网络工具。
* [Mailpit](https://github.com/axllent/mailpit) - 面向开发人员的电子邮件和 SMTP 测试工具。
* [phpMyAdmin](https://github.com/phpmyadmin/phpmyadmin) - MySQL/MariaDB 的 Web 界面。
* [PHP Queue](https://github.com/CoderKungfu/php-queue) - 用于管理排队后端的应用程序。
* [phpRedisAdmin](https://github.com/ErikDubbelboer/phpRedisAdmin) - 用于管理 [Redis](https://redis.io/) 数据库的简单 Web 界面。
* [PHPSandbox](https://phpsandbox.io) - 浏览器中的 PHP 在线 IDE。

### 基础设施
*提供 PHP 应用程序和服务的基础设施。*

* [appserver.io](https://github.com/appserver-io/appserver) - PHP 的多线程应用程序服务器，用 PHP 编写。
* [php-pm](https://github.com/php-pm/php-pm) - PHP 应用程序的进程管理器、增压器和负载平衡器。
* [RoadRunner](https://github.com/roadrunner-server/roadrunner) - 高性能 PHP 应用服务器、负载均衡器和进程管理器。

# 资源
用于提高 PHP 开发技能和知识的各种资源，例如书籍、网站和文章。

### PHP 网站
*有用的 PHP 相关网站。*

* [Nomad PHP](https://nomadphp.com/) - 在线 PHP 学习资源。
* [Laravel News](https://laravel-news.com/) - Laravel 官方博客。
* [PHP Annotated Monthly](https://blog.jetbrains.com/phpstorm/tag/php-annotated-monthly/) - PHP 新闻每月摘要。
* [PHP FIG](https://www.php-fig.org/) - PHP 框架互操作性小组。
* [PHP Package Development Standards](https://php-pds.com/) - PHP 的包开发标准。
* [PHP School](https://www.phpschool.io/) - PHP 开源学习。
* [PHP The Right Way](https://phptherightway.com/) - PHP 最佳实践快速参考指南。
* [PHP UG](https://php.ug) - 一个帮助人们找到离他们最近的 PHP 用户组 (UG) 的网站。
* [PHP Watch](https://php.watch/) - PHP 文章、新闻、即将发生的更改、RFC 等。
* [Unit Testing Tips](https://testing-tips.sarvendev.com/) - PHP 中的单元测试提示示例。

### PHP 书籍
*精彩的 PHP 相关书籍。*

* [Domain-Driven Design in PHP](https://leanpub.com/ddd-in-php) - 用 PHP 编写的真实示例展示了 DDD 架构风格。
* [Functional Programming in PHP](https://www.functionalphp.com/) - 一本关于在 PHP 中应用函数式编程原理和技术的书。
* [Mastering Object-Orientated PHP](https://masteringobjectorientedphp.com/) - Brandon Savage 撰写的一本有关面向对象 PHP 的书。
* [PHP Cookbook](https://www.oreilly.com/library/view/php-cookbook/9781098121310/) - 本食谱提供了代码配方来帮助您解决各种编码问题。
* [Modernizing Legacy Applications in PHP](https://leanpub.com/mlaphp) - Paul M. Jones 撰写的一本关于现代化遗留 PHP 应用程序的书。
* [Scaling PHP Applications](https://www.scalingphpbook.com) - Steve Corona 撰写的一本有关扩展 PHP 应用程序的电子书。
* [Securing PHP: Core Concepts](https://leanpub.com/securingphp-coreconcepts) - Chris Cornutt 撰写的一本有关 PHP 常见安全术语和实践的书。
* [Signaling PHP](https://leanpub.com/signalingphp) - Cal Evans 撰写的一本关于在 CLI 脚本中捕获 PCNTL 信号的书。
* [XML Parsing with PHP](https://www.phparch.com/books/xml-parsing-with-php/) - 本书涵盖了解析和验证 XML 文档、利用 XPath 表达式、使用命名空间以及如何以编程方式创建和修改 XML 文件。

### PHP 视频
*精彩的 PHP 相关视频。*

* [Laracasts](https://laracasts.com) - 有关 Laravel、Vue JS 等的截屏视频。
* [Laravel YouTube Channel](https://www.youtube.com/channel/UCfO2GiQwb-cwJTb1CuRSkwg) - Laravel YouTube 官方频道。
* [Program With Gio](https://www.youtube.com/playlist?list=PLr3d3QYzkw2xabQRUpcZ_IBk9W50M9pe-) - Gio 的 PHP 8 课程。
* [Programming with Anthony](https://www.youtube.com/playlist?list=PLM-218uGSX3DQ3KsB5NJnuOqPqc5CW2kW) - 安东尼·费拉拉的视频系列。
* [SymfonyCasts](https://symfonycasts.com/) - 有关 PHP 和 Symfony 的截屏视频和教程。

### PHP 会议
*PHP 会议。*

* [Laracon EU](https://www.youtube.com/@LaraconEU) - Laracon EU 是一个为期 2 天的活动，适合有兴趣学习 Laravel 和相关技术或想要与他人分享知识的人们。
* [PHP[TEK]](https://phptek.io/) - 美国历史最悠久的 Web 开发者会议，重点关注 PHP 编程语言。
* [PHP UK Conference](https://www.youtube.com/user/phpukconference/videos) - PHP UK 会议的视频集。

### PHP 播客
*重点关注 PHP 主题的播客。*

* [Laravel News Podcast](https://podcast.laravel-news.com/) - Laravel 新闻播客为您带来与 Laravel PHP 框架相关的所有最新新闻和活动。
* [Mostly Technical](https://mostlytechnical.com/) - 由 Ian Landsman 和 Aaron Francis 主持，Mostly Technical 是关于 Laravel、商业以及各种相关主题的热烈讨论。
* [No Compromises](https://show.nocompromises.io/) - 两位经验丰富的咸味编程老手谈论了基于多年与 Laravel SaaS 团队合作的最佳实践。
* [North Meets South Web Podcast](https://www.northmeetssouth.audio/) - Jacob Bennett 和 Michael Dyrynda 克服 14.5 小时的时差，谈论 Web 开发人员的生活。
* [Over Engineered](https://overengineered.fm/) - 迷你系列播客，我们非常详细地探讨不重要的编程问题。
* [PHP Internals News](https://phpinternals.news) - 关于 PHP 内部原理的播客。
* [PHP Town Hall](https://phptownhall.com/) - Ben Edmunds 和 Phil Sturgeon 的休闲 PHP 播客。
* [来自 php[architect] 的 php[podcast] 剧集](https://www.phparch.com/podcast/) - php[architect] 的官方播客，该行业领先的技术杂志和出版商专注于 PHP 和 Web 开发。
* [PHPUgly](https://www.phpugly.com/) - 一些过度劳累的 PHP 开发人员的胡言乱语。
* [The Laracasts Snippet](https://laracasts.simplecast.com) - Laracasts 片段的每一集都提供了关于 Web 开发某些方面的单一想法。
* [The Laravel Podcast](https://laravelpodcast.com/) - Laravel 和 PHP 开发新闻和讨论。
* [The PHP Roundtable](https://phproundtable.com/) - PHP 圆桌会议是开发人员的休闲聚会，讨论 PHP 书呆子关心的话题。

### PHP 通讯
*PHP 相关新闻直接发送到您的收件箱。*

* [PHP Weekly](https://www.phpweekly.com/) - 有关 PHP 的每周时事通讯。

### PHP阅读
*PHP相关阅读材料。*

* [php[architect]](https://www.phparch.com/magazine/) - 一本专门介绍 PHP 的月刊。

### PHP 内部原理阅读
*阅读与 PHP 内部结构或性能相关的材料。*

* [PHP RFCs](https://wiki.php.net/rfc) - PHP RFC（征求意见）的主页。
* [Externals](https://externals.io/) - PHP 内部讨论。
* [PHP RFC Watch](https://github.com/beberlei/php-rfc-watch) - 观看最新的 PHP [RFC](https://wiki.php.net/rfc)。
* [PHP Internals Book](https://www.phpinternalsbook.com/) - 一本关于 PHP 内部原理的在线书籍，由三位核心开发人员撰写。
