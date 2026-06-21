[![SWUbanner](https://raw.githubusercontent.com/vshymanskyy/StandWithUkraine/main/banner-direct.svg)](https://github.com/vshymanskyy/StandWithUkraine/blob/main/docs/README.md)

<palign="center"><img src="logo/logotype_horizontal.jpg" alt="awesome-crystal"></p>

# 很棒的水晶
[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

很棒的 Crystal 代码和资源的精选列表。受到 [awesome](https://github.com/sindresorhus/awesome) 和 [awesome-awesomeness](https://github.com/bayandin/awesome-awesomeness) 的启发。
目标是让项目基本稳定且对社区有用。

在 [shards.info](https://shards.info) 上搜索分片以了解更多信息。

欢迎贡献。请先快速浏览一下[贡献指南](https://github.com/veelenga/awesome-crystal/blob/master/.github/CONTRIBUTING.md)。

* [很棒的水晶](#awesome-crystal)
  * [算法和数据结构](#algorithms-and-data-structures)
  * [Blockchain](#blockchain)
  * [C 绑定](#c-bindings)
  * [Caching](#caching)
  * [CLI 构建器](#cli-builders)
  * [CLI 实用程序](#cli-utils)
  * [代码分析和指标](#code-analysis-and-metrics)
  * [Compression](#compression)
  * [Configuration](#configuration)
  * [Converters](#converters)
  * [Cryptography](#cryptography)
  * [数据格式](#data-formats)
  * [数据生成器](#data-generators)
  * [数据库驱动程序/客户端](#database-driversclients)
  * [数据库工具](#database-tools)
  * [Debugging](#debugging)
  * [依赖注入](#dependency-injection)
  * [Email](#email)
  * [环境管理](#environment-management)
  * [例子和有趣的事情](#examples-and-funny-stuff)
  * [框架组件](#framework-components)
  * [游戏开发](#game-development)
  * [图形用户界面开发](#gui-development)
  * [HTML 生成器](#html-builders)
  * [HTML/XML 解析](#htmlxml-parsing)
  * [HTTP](#http)
  * [图像处理](#image-processing)
  * [Implementations/Compilers](#implementationscompilers)
  * [Internationalization](#internationalization)
  * [记录和监控](#logging-and-monitoring)
  * [机器学习](#machine-learning)
  * [Markdown/文本处理器](#markdowntext-processors)
  * [Misc](#misc)
  * [网络协议](#network-protocols)
  * [Networking](#networking)
  * [ORM/ODM 扩展](#ormodm-extensions)
  * [包管理](#package-management)
  * [进程和线程](#processes-and-threads)
  * [项目生成器](#project-generators)
  * [队列和消息传递](#queues-and-messaging)
  * [Routing](#routing)
  * [Scheduling](#scheduling)
  * [科学与数据分析](#science-and-data-analysis)
  * [Search](#search)
  * [Security](#security)
  * [无服务器计算](#serverless-computing)
  * [System](#system)
  * [任务管理](#task-management)
  * [模板引擎](#template-engine)
  * [Testing](#testing)
  * [第三方API](#third-party-apis)
  * [Validation](#validation)
  * [网络框架](#web-frameworks)
* [Community](#community)
  * [Unofficial](#unofficial)
* [Resources](#resources)
  * [官方文档翻译](#official-documentation-translations)
* [服务和应用程序](#services-and-apps)
* [Tools](#tools)
  * [DevOps](#devops)
  * [编辑器插件](#editor-plugins)
  * [LSP语言服务器协议实现](#lsp-language-server-protocol-implementations)
  * [外壳插件](#shell-plugins)

## 算法和数据结构
 * [bisect](https://github.com/spider-gazelle/bisect) - 将值插入已排序的数组中
 * [blurhash.cr](https://github.com/Sija/blurhash.cr) - [BlurHash](https://github.com/woltapp/blurhash) 实现
 * [crie](https://github.com/c910335/crie) - 编译时特里树
 * [CrOTP](https://github.com/philnash/crotp) - 双因素身份验证的 HOTP 和 TOTP 实现
 * [crystal-linked-list](https://github.com/abvdasker/crystal-linked-list) - 链表的实现
 * [crystaledge](https://github.com/unn4m3d/crystaledge) - 纯向量数学库
 * [crystalg](https://github.com/tobyapi/crystalg) - 通用算法库
 * [crystalline](https://github.com/jtomschroeder/crystalline) - 容器和算法的集合
 * [csuuid](https://github.com/wyhaines/csuuid.cr) - 按时间顺序排序的 UUID
 * [edits.cr](https://github.com/tcrouch/edits.cr) - 编辑距离算法合集
 * [fzy](https://github.com/hugopl/fzy) - 很棒的 Fzy 项目模糊查找器算法的 Crystal 端口
 * [Goban](https://github.com/soya-daizu/goban) - 快速高效的 QR 码实施
 * [graphlb](https://github.com/mettuaditya/graphlb) - 图数据结构与算法合集
 * [haversine](https://github.com/geocrystal/haversine) - 半正矢公式的实现
 * [HKDF](https://github.com/spider-gazelle/HKDF) - 基于 HMAC 的提取和扩展密钥派生函数 [rfc5869](https://www.rfc-editor.org/rfc/rfc5869)
 * [kd_tree](https://github.com/geocrystal/kd_tree) - “K维树”和“N最近邻”的实现
 * [ksuid.cr](https://github.com/Sija/ksuid.cr) - K 可排序全局唯一 ID
 * [markov](https://github.com/mccallofthewild/markov) - 构建马尔可夫链并运行马尔可夫过程
 * [multiset.cr](https://github.com/tcrouch/multiset.cr) - 多重集的实现
 * [named_information](https://github.com/spider-gazelle/named_information) - 用哈希命名事物 [rfc6920](https://datatracker.ietf.org/doc/html/rfc6920)
 * [qr-code](https://github.com/spider-gazelle/qr-code) - 二维码生成器
 * [radix](https://github.com/luislavena/radix) - 基数树的实现
 * [s2_cells](https://github.com/spider-gazelle/s2_cells) - [S2 Geometry](https://s2geometry.io/devguide/s2cell_hierarchy.html) 用于空间索引
 * [secure-remote-password](https://github.com/spider-gazelle/secure-remote-password) - 用于通过不安全网络进行身份验证的 SRP-6a 协议
 * [SPAKE2+](https://github.com/spider-gazelle/SPAKE2_plus) - 密码验证密钥交换 (PAKE) 协议，与 SRP-6a 相当
 * [splay_tree_map](https://github.com/wyhaines/splay_tree_map.cr) - 符合Hash ducktype的Splay Tree实现
 * [verhoeff](https://github.com/spider-gazelle/verhoeff) - Verhoeff 校验和算法的实现

## 区块链
 * [Axentro](https://github.com/Axentro/Axentro) - 定制区块链平台
 * [Cocol](https://github.com/cocol-project/cocol) - 最小的区块链测试平台
 * [secp256k1.cr](https://github.com/q9f/secp256k1.cr) - 公私钥密码学中使用的椭圆曲线

## C 绑定
 * [augeas.cr](https://github.com/fernandes/augeas.cr) - [Augeas](https://augeas.net/) 的绑定
 * [clang.cr](https://github.com/crystal-lang/clang.cr) - Libclang 绑定
 * [crt.cr](https://github.com/maiha/crt.cr) - libncursesw 和 crt 的绑定
 * [crystal-gsl](https://github.com/konovod/crystal-gsl) - [GNU 科学图书馆](https://www.gnu.org/software/gsl/) 的绑定
 * [crystal-hunspell](https://github.com/mamantoha/crystal-hunspell) - [Hunspell](https://hunspell.github.io/) 的绑定
 * [duktape.cr](https://github.com/jessedoyle/duktape.cr) - [Duktape](https://github.com/svaarala/duktape) JavaScript 引擎的绑定
 * [fftw.cr](https://github.com/firejox/fftw.cr) - [FFTW](https://fftw.org/) 库的绑定
 * [gphoto2.cr](https://github.com/Sija/gphoto2.cr) - [libgphoto2](http://www.gphoto.org/) 库的绑定
 * [gpio.cr](https://github.com/spider-gazelle/gpio.cr) - gpiod 库的绑定（通用 IO 控制和反馈）
 * [icu.cr](https://github.com/olbat/icu.cr) - [ICU](http://site.icu-project.org/) 库的绑定
 * [libnotify.cr](https://github.com/splattael/libnotify.cr) - Libnotify 的绑定
 * [nlopt.cr](https://github.com/konovod/nlopt.cr) - [NLOpt] 的绑定(https://nlopt.readthedocs.io/en/latest/)
 * [pcap.cr](https://github.com/maiha/pcap.cr) - libpcap 的绑定
 * [pledge.cr](https://github.com/chris-huxtable/pledge.cr) - OpenBSD 的 `pledge(2)` 的绑定
 * [ssh2.cr](https://github.com/spider-gazelle/ssh2.cr) - libssh2 库的绑定
 * [syslog.cr](https://github.com/chris-huxtable/syslog.cr) - `syslog` 的绑定
 * [v4l2.cr](https://github.com/spider-gazelle/v4l2.cr) - [Video4Linux2](https://en.wikipedia.org/wiki/Video4Linux) 的绑定
 * [wasmer-crystal](https://github.com/naqvis/wasmer-crystal) - “wasmer” WebAssembly 运行时的绑定
 * [win32cr](https://github.com/mjblack/win32cr) - Win32 API 的绑定
 * [x_do.cr](https://github.com/woodruffw/x_do.cr) - libxdo 的绑定 ([`xdotool`](https://github.com/jordansissel/xdotool))

## 缓存
 * [apt-larder](https://github.com/jbox-web/apt-larder) - APT 包存储库的 HTTP 缓存代理
 * [cache](https://github.com/crystal-cache/cache) - 键/值存储，其中对可以在指定的时间间隔后过期
 * [crystal-memcached](https://github.com/comandeo/crystal-memcached) - memcached 客户端的实现

## CLI 构建器
 * [admiral](https://github.com/jwaldrip/admiral.cr) - 用于编写命令行接口的强大 DSL
 * [Athena Console](https://github.com/athena-framework/console) - 允许创建基于 CLI 的命令
 * [clicr](https://github.com/j8r/clicr) - 一个简单的声明式命令行界面构建器
 * [clim](https://github.com/at-grandpa/clim) - Slim 命令行界面生成器
 * [Cling](https://github.com/devnote-dev/cling) - 模块化、非基于宏的命令行界面库
 * [commander](https://github.com/mrrooijen/commander) - 命令行界面生成器
 * [Keimeno](https://github.com/robacarp/keimeno) - Crystal 中的轻量级文本用户界面库
 * [OptionParser](https://crystal-lang.org/api/OptionParser.html) - 命令行选项处理（Crystal stdlib）
 * [Phreak](https://github.com/shinzlet/phreak) - OptionParser 风格的高度灵活的 Crystal CLI 构建器

## CLI 实用程序
 * [climate](https://github.com/Sija/climate.cr) - 让 CLI 输出🌈 彩色化的小工具
 * [coin](https://github.com/caian-org/coin) - 通过 [Fixer API](https://fixer.io) 执行货币转换的命令行应用程序
 * [cride](https://github.com/j8r/cride) - 一个轻量级 CLI 文本编辑器/IDE
 * [git-repository](https://github.com/place-labs/git-repository) - git cli 包装器以最少的数据传输查询和克隆远程存储库
 * [hetzner-k3s](https://github.com/vitobotta/hetzner-k3s) - 用于在 Hetzner Cloud 中快速创建和管理 Kubernetes 集群的 CLI 工具
 * [lff](https://github.com/mkdika/lff-cr) - 命令行中简单直接的大文件查找实用程序
 * [meet](https://github.com/ryanprior/meet) - 从舒适的命令行快速开始 jitsi 会议
 * [oq](https://github.com/Blacksmoke16/oq) - 一个高性能、可移植的 jq 包装器，以方便使用和输出 JSON 以外的格式；使用 [jq](https://github.com/stedolan/jq) 过滤器来转换数据
 * [progress_bar.cr](https://github.com/TPei/progress_bar.cr) - 一个简单且可定制的进度条
 * [tablo](https://github.com/hutou/tablo) - 灵活的端子表生成器
 * [tallboy](https://github.com/epoch/tallboy) - 生成支持跨越多列的单元格的 ASCII 字符表

## 代码分析和指标
 * [ameba](https://github.com/crystal-ameba/ameba) - 静态代码分析工具
 * [cruml](https://github.com/tamdaz/cruml) - 为任何 Crystal 项目提供 UML 类图生成器的工具
 * [linguist.cr](https://github.com/microgit-com/linguist.cr) - 使用多种方式查找文件中使用的编程语言，基于Github的Linguist

## 压缩
 * [Crystar](https://github.com/naqvis/crystar) - Tar 归档格式的读者和作者
 * [Gzip](https://crystal-lang.org/api/Compress/Gzip.html) - gzip 格式的读取器和写入器（Crystal stdlib）
 * [polylines.cr](https://github.com/BuonOmo/polylines.cr) - 坐标系的压缩
 * [snappy](https://github.com/naqvis/snappy) - Crystal 的 Snappy 压缩格式读写器
 * [Zip](https://crystal-lang.org/api/Compress/Zip.html) - zip 格式的读取器和写入器 (Crystal stdlib)
 * [Zlib](https://crystal-lang.org/api/Compress/Zlib.html) - zlib 格式的读取器和写入器（Crystal stdlib）
 * [zstd.cr](https://github.com/didactic-drunk/zstd.cr) - [Zstandard](https://github.com/facebook/zstd) 压缩库的绑定

## 配置
 * [cr-dotenv](https://github.com/gdotdesign/cr-dotenv) - 加载 .env 文件
 * [Envy](https://github.com/grottopress/envy) - 从 YAML 加载环境变量
 * [envyable](https://github.com/philnash/envyable.cr) - 一个简单的 YAML 到 ENV 配置加载器
 * [habitat](https://github.com/luckyframework/habitat) - 类和模块的类型安全配置
 * [totem](https://github.com/icyleaf/totem) - 加载并解析 JSON、YAML、dotenv 格式的配置

## 转换器
 * [base62.cr](https://github.com/Sija/base62.cr) - Base62 编码器/解码器，非常适合 url 缩短
 * [crunits](https://github.com/spider-gazelle/crunits) - 用于转换测量单位的工具（英里到公里，摄氏度到华氏度等）
 * [money](https://github.com/crystal-money/money) - 轻松处理金钱和货币转换（[RubyMoney](https://github.com/RubyMoney/money) 的几乎完整移植）
 * [sass.cr](https://github.com/straight-shoota/sass.cr) - 将 SASS/SCSS 编译为 CSS（[libsass](https://github.com/sass/libsass/) 绑定）
 * [tssc.cr](https://github.com/Sija/tssc.cr) - `Time::Span` 字符串转换器（包括 JSON 和 YAML 支持）

## 密码学
 * [cmac](https://github.com/spider-gazelle/cmac) - 基于密码的消息验证代码 (CMAC) 的 Crystal 实现
 * [ed25519](https://github.com/spider-gazelle/ed25519) - Ed25519 椭圆曲线公钥签名系统
[RFC 8032] 中描述
 * [monocypher.cr](https://github.com/konovod/monocypher.cr) - Monocypher 加密库的水晶包装器
 * [sodium.cr](https://github.com/didactic-drunk/sodium.cr) - libsodium 加密 API 的水晶包装器

## 数据格式
 * [BinData](https://github.com/spider-gazelle/bindata) - 带有 [ASN.1](https://en.wikipedia.org/wiki/Abstract_Syntax_Notation_One) 解析器的二进制数据解析器助手
 * [config.cr](https://github.com/chris-huxtable/config.cr) - 易于使用的配置格式解析器
 * [crinder](https://github.com/c910335/crinder) - 基于类的 json 渲染器
 * [Crystalizer](https://github.com/j8r/crystalizer) - （反）序列化任何 Crystal 对象；开箱即用地支持 JSON、YAML 和 Byte 格式
 * [CSV](https://crystal-lang.org/api/CSV.html) - 解析和生成逗号分隔值（Crystal stdlib）
 * [front_matter.cr](https://github.com/chris-huxtable/front_matter.cr) - 将文件的前面内容与其内容分开
 * [geoip2.cr](https://github.com/delef/geoip2.cr) - GeoIP2 阅读器
 * [HAR](https://github.com/NeuraLegion/har) - HAR（HTTP 存档）解析器
 * [INI](https://crystal-lang.org/api/INI.html) - INI 文件解析器（Crystal stdlib）
 * [jmespath.cr](https://github.com/qequ/jmespath.cr) - JMESPath（一种 JSON 查询语言）的 Crystal 实现
 * [JSON](https://crystal-lang.org/api/JSON.html) - 解析并生成 JSON 文档（Crystal stdlib）
 * [json-schema](https://github.com/spider-gazelle/json-schema) - 将 JSON 可序列化类转换为 [JSON Schema](https://json-schema.org/) 表示形式
 * [JSON::OnSteroids](https://github.com/anykeyh/json_on_steroids) - 轻松处理和修改 JSON 文档
 * [maxminddb.cr](https://github.com/delef/maxminddb.cr) - MaxMindDB 阅读器
 * [toml.cr](https://github.com/crystal-community/toml.cr) - TOML解析器
 * [toon-crystal](https://github.com/mamantoha/toon-crystal) - TOON（面向标记的对象表示法）解析器
 * [XML](https://crystal-lang.org/api/XML.html) - 解析和生成 XML 文档 (Crystal stdlib)
 * [YAML](https://crystal-lang.org/api/YAML.html) - 解析和生成 YAML 文档（Crystal stdlib）

## 数据生成器
 * [faker](https://github.com/askn/faker) - 用于生成假数据的库
 * [hashids.cr](https://github.com/splattael/hashids.cr) - 一个从一个或多个数字生成类似 YouTube 的 ID 的库
 * [prime](https://github.com/wontruefree/prime) - 质数生成器

## 数据库驱动程序/客户端
 * [couchdb.cr](https://github.com/TechMagister/couchdb.cr) - CouchDB 客户端
 * [cryomongo](https://github.com/elbywan/cryomongo) - MongoDB 驱动程序
 * [crystal-db](https://github.com/crystal-lang/crystal-db) - 常用数据库API
 * [crystal-ldap](https://github.com/spider-gazelle/crystal-ldap) - LDAP客户端
 * [crystal-mysql](https://github.com/crystal-lang/crystal-mysql) - Crystal 的 MySQL 连接器
 * [crystal-pg](https://github.com/will/crystal-pg) - Postgres 驱动程序
 * [crystal-redis](https://github.com/stefanwille/crystal-redis) - 全功能 Redis 客户端
 * [crystal-rethinkdb](https://github.com/kingsleyh/crystal-rethinkdb) - RethinkDB / RebirthDB 驱动程序
 * [crystal-sqlite3](https://github.com/crystal-lang/crystal-sqlite3) - SQLite3 绑定
 * [leveldb](https://github.com/crystal-community/leveldb) - LevelDB 的水晶绑定
 * [rocksdb.cr](https://github.com/maiha/rocksdb.cr) - RocksDB客户端
 * [surrealdb.cr](https://github.com/yorci/surrealdb.cr) - 非官方 SurrealDB HTTP 和 Websocket 客户端

## 数据库工具
 * [migrate](https://github.com/vladfaust/migrate.cr) - 更简单的带有事务的数据库迁移工具

## 调试
* [backtracer.cr](https://github.com/Sija/backtracer.cr) - 分片旨在帮助将回溯解析为结构化形式
* [debug.cr](https://github.com/Sija/debug.cr) - 用于“pp”式调试的“debug!(…)”宏

## 依赖注入
 * [Athena Dependency Injection](https://github.com/athena-framework/dependency-injection) - 健壮的依赖注入服务容器框架
 * [Crystal-DI](https://github.com/funk-yourself/crystal-di) - 轻量级 DI 容器
 * [HardWire](https://github.com/jerometwell/hardwire) - 编译时非侵入式依赖注入系统
 * [syringe](https://github.com/Bonemind/syringe) - 一个简单且基本的水晶依赖注入分片

## 电子邮件
 * [carbon](https://github.com/luckyframework/carbon) - 有趣、可测试且基于适配器的电子邮件库
 * [crystal-email](https://github.com/arcage/crystal-email) - 简单的电子邮件发送库
 * [CrystalEmail](https://git.sceptique.eu/Sceptique/CrystalEmail) - 符合 RFC 的电子邮件验证器
 * [sendgrid.cr](https://github.com/dlanileonardo/sendgrid.cr) - 简单的 Sendgrid 客户端

## 环境管理
 * [asdf-crystal](https://github.com/marciogm/asdf-crystal) - asdf 版本管理器插件
 * [crenv](https://github.com/crenv/crenv) - 水晶版本管理器
 * [rcm.cr](https://github.com/maiha/rcm.cr) - Redis集群管理器
 * [vfox-crystal](https://github.com/yanecc/vfox-crystal) - vfox 版本管理器插件

## 例子和有趣的事情
 * [blackjack-cr](https://github.com/gdonald/blackjack-cr) - 控制台二十一点
 * [crystal-patterns](https://github.com/crystal-community/crystal-patterns) - GOF 模式示例
 * [crystalworld](https://github.com/vladfaust/crystalworld) - [realworld.io](https://realworld.io) 后端 API 实现
 * [exercism-crystal](https://github.com/exercism/crystal) - 运动练习
 * [try.cr](https://github.com/maiha/try.cr) - 尝试单子

## 框架组件
 * [Athena Event Dispatcher](https://github.com/athena-framework/event-dispatcher) - 中介者和观察者模式事件库
 * [Athena Negotiation](https://github.com/athena-framework/negotiation) - 与框架无关的内容协商库
 * [device_detector](https://github.com/creadone/device_detector) - 用于通过用户代理字符串检测设备的分片
 * [Exception Page](https://github.com/crystal-loot/exception_page) - Crystal Web 库和框架的特殊异常页面
 * [graphql](https://github.com/graphql-crystal/graphql) - 类型安全的 [GraphQL](http://graphql.org) 服务器实现
 * [graphql-crystal](https://github.com/ziprandom/graphql-crystal) - [GraphQL](http://graphql.org) 实现
 * [kemal-session](https://github.com/kemalcr/kemal-session) - Kemal 的会话处理程序
 * [mochi](https://github.com/awcrotwell/mochi) - 受 Devise 支持启发的身份验证分片：可验证、可确认、可邀请等
 * [motion.cr](https://github.com/awcrotwell/motion.cr) - Amber 的面向对象前端库
 * [multi-auth](https://github.com/msa7/multi_auth) - 标准化多提供商 OAuth2 身份验证（受到omniauth 的启发）
 * [praetorian](https://github.com/ilanusse/praetorian) - 受 Pundit 启发的极简授权库
 * [Shield](https://github.com/grottopress/shield) - *Lucky* 框架的全面安全性
 * [shrine.cr](https://github.com/jetrockets/shrine.cr) - 用于 Crystal 应用程序的文件附件工具包。深受 Ruby Shrine 的启发
 * [tourmaline](https://github.com/protoncr/tourmaline) - Telegram 机器人框架，其 API 松散地基于 [telegraf.js](https://telegraf.js.org/)

## 游戏开发
 * [CrSFML](https://github.com/oprypin/crsfml) - 绑定到 [SFML](https://www.sfml-dev.org/) 多媒体/游戏库
 * [crystal-chipmunk](https://github.com/oprypin/crystal-chipmunk) - 绑定到 [Chipmunk](http://chipmunk-physicals.net/)，一个快速且轻量级的 2D 游戏物理库
 * [crystal-imgui-sfml](https://github.com/oprypin/crystal-imgui-sfml) - 将 [Dear ImGui](https://github.com/ocornut/imgui) 集成到 [SFML](https://www.sfml-dev.org/) 项目中的绑定
 * [entitas.cr](https://github.com/spoved/entitas.cr) - Crystal的实体组件系统框架
 * [MyECS](https://github.com/konovod/myecs) - Crystal的稀疏实体组件系统框架
 * [Raylib-cr](https://github.com/sol-vin/raylib-cr) - 直接绑定[Raylib](https://raylib.com)，支持Linux、Windows和Mac
 * [SDL-Crystal-Bindings](https://github.com/Hadeweka/SDL-Crystal-Bindings) - 直接（不安全）绑定到 [SDL2](https://www.libsdl.org/)，用于编写自己的游戏库

## 图形用户界面开发
 * [CrymbleUI](https://github.com/wolfgang371/crymbleui) - 一个漂亮且快速的 Crystal GUI 框架。声明式 DSL、反应式状态、高性能、丰富的小组件集，包括 VirtualMatrix 和 RecursiveGrid
 * [crystal-imgui](https://github.com/oprypin/crystal-imgui) - 绑定到 [Dear ImGui](https://github.com/ocornut/imgui)，一个即时模式图形 UI 库
 * [GTK4.cr](https://github.com/hugopl/gtk4.cr) - 使用 Crystalized API 绑定 [GTK4](https://docs.gtk.org/gtk4/overview.html)
 * [Iu](https://github.com/grkek/iu) - 基于 [Fusion/libui.cr](https://github.com/Fusion/libui.cr) 库的 UI 框架，具有来自 [hedron-crystal/hedron](https://github.com/hedron-crystal/hedron) 的自定义元素和修改后的绑定
 * [Ultimate GTK4 Crystal Guide](https://ultimate-gtk4-crystal-guide.geopjr.dev/) - 了解如何在 Crystal 中创建优质 GTK4 应用程序

## HTML 生成器
 * [blueprint](https://github.com/gunbolt/blueprint) - 使用纯 Crystal 编写可重用且可测试的 HTML 模板
 * [form_builder.cr](https://github.com/westonganger/form_builder.cr) - Crystal 的极其简单的 HTML 表单生成器，内置对许多流行 UI 库（例如 Bootstrap）的支持
 * [to_html](https://github.com/sbsoftware/to_html.cr) - Crystal 最快的 HTML 构建器引擎
 * [Water](https://github.com/shootingfly/water) - 一个用纯 Crystal 编写 HTML 的库

## HTML/XML 解析
 * [docx_cr_converter](https://github.com/aristotelesbr/docx_cr_converter) - 解析 DOCX 字
 * [lexbor](https://github.com/kostya/lexbor) - 包含 CSS 选择器的快速 HTML5 解析器

## HTTP协议
 * [Cable](https://github.com/cable-cr/cable) - ActionCable“移植”到 Crystal，与框架无关，与 ActionCable JS 客户端 100% 兼容
 * [cossack](https://github.com/crystal-community/cossack) - 简单灵活的 HTTP 客户端
 * [crest](https://github.com/mamantoha/crest) - 简单的 HTTP 和 REST 客户端，灵感来自 Ruby 的 RestClient gem
 * [crul](https://github.com/porras/crul) - 命令行 HTTP 客户端
 * [cryload](https://github.com/sdogruyol/cryload) - ryload 是一个强大、快速、实用的 HTTP 基准测试工具，用于压力测试 API 和 Web 服务
 * [digest-auth](https://github.com/spider-gazelle/digest-auth) - 摘要式认证
 * [halite](https://github.com/icyleaf/halite) - 具有可链接 REST API、内置会话和记录器的 Crystal HTTP 请求
 * [http-multiserver.cr](https://github.com/vladfaust/http-multiserver.cr) - 通过路由挂载多个服务器（又名 URL 映射）
 * [http-params-serializable](https://github.com/vladfaust/http-params-serializable) - HTTP 参数（反）序列化，适用于 URL 查询和 URL 编码表单
 * [http-protection](https://github.com/rogeriozambon/http-protection) - 防御典型网络攻击
 * [http2](https://github.com/ysbaddaden/http2) - HTTP/2 协议实现
 * [HTTP::Client](https://crystal-lang.org/api/HTTP/Client.html) - HTTP 客户端（Crystal stdlib）
 * [HTTP::Server](https://crystal-lang.org/api/HTTP/Server.html) - HTTP 服务器（Crystal stdlib）
 * [HTTP::WebSocket](https://crystal-lang.org/api/HTTP/WebSocket.html) - HTTP WebSocket 客户端（Crystal stdlib）
 * [link-header](https://github.com/spider-gazelle/link-header) - HTTP 链接头解析器
 * [ntlm](https://github.com/spider-gazelle/ntlm) - NTLM认证
 * [proxy-fetcher.cr](https://github.com/nbulaj/proxy-fetcher.cr) - 代理列表获取和验证库
 * [sse.cr](https://github.com/y2k2mt/sse.cr) - [服务器发送事件](https://html.spec.whatwg.org/multipage/server-sent-events.html) 客户端

## 图像处理
 * [celestine](https://github.com/celestinecr/celestine) - 使用 DSL 创建 SVG 图像
 * [ffmpeg](https://github.com/spider-gazelle/ffmpeg) - 与 StumpyPNG 一起提取帧的 FFmpeg 绑定
 * [Pluto](https://github.com/phenopolis/pluto) - 快速便捷的图像处理库
 * [stumpy_png](https://github.com/stumpycr/stumpy_png) - 读取和写入 PNG 图像

## 实现/编译器
 * [charly](https://github.com/charly-lang) - Charly编程语言
 * [cltk](https://github.com/ziprandom/cltk) - Ruby 语言工具包的水晶端口
 * [crisp](https://github.com/rhysd/Crisp) - 用 Crystal 实现的 Lisp 方言
 * [GiavaScript](https://github.com/memburg/GiavaScript) - 开源、跨平台 JavaScript 运行时
 * [LinCAS-lang](https://github.com/LinCAS-lang) - 用于科学计算的编程语言
 * [mint-lang](https://github.com/mint-lang/mint) - 一种令人耳目一新的 Web 前端编程语言
 * [myst-lang](https://github.com/myst-lang/) - 一种实用的动态语言，旨在尽可能轻松高效地编写和理解
 * [novika](https://github.com/novika-lang/novika) - 一种自由形式、可塑性、解释性编程语言
 * [runic-lang](https://github.com/runic-lang) - 设计中的玩具语言

## 国际化

 * [crystal-i18n](https://github.com/crystal-i18n/i18n) - 受 Ruby-I18n 启发的国际化库
 * [i18n.cr](https://github.com/vladfaust/i18n.cr) - 国际化分片
 * [Lens](https://github.com/syeopite/lens) - Crystal 的多格式国际化 (i18n) 分片。支持Gettext、Ruby YAML等。
 * [Rosetta](https://github.com/wout/rosetta) - 一个极快的国际化 (i18n) 库，具有支持 YAML 和 JSON 格式的编译时密钥查找

## 记录和监控
 * [crafana](https://github.com/spoved/crafana.cr) - 帮助自动生成仪表板的 [Grafana](https://grafana.com/) 库
 * [fiber_metrics.cr](https://github.com/didactic-drunk/fiber_metrics.cr) - 跟踪每个“Fiber”、方法或块的运行时间、等待时间或内存分配
 * [Log](https://crystal-lang.org/api/Log.html) - 日志记录实用程序（Crystal stdlib）
 * [statsd.cr](https://github.com/miketheman/statsd.cr) - [Statsd](https://github.com/etsy/statsd) 客户端库

## 机器学习
 * [ai4cr](https://github.com/drhuffman12/ai4cr) - 人工智能（基于https://github.com/SergioFierens/ai4r）
 * [Cadmium](https://github.com/cadmiumcr/cadmium) - NLP 库很大程度上基于 [natural](https://github.com/NaturalNode/natural)
 * [crystal-fann](https://github.com/NeuraLegion/crystal-fann) - FANN（快速人工神经网络）绑定
 * [mxnet.cr](https://github.com/toddsundsted/mxnet.cr) - [MXNet](https://mxnet.incubator.apache.org/) 的绑定
 * [shainet](https://github.com/NeuraLegion/shainet) - SHAInet（纯水晶神经网络）

## Markdown/文本处理器
 * [cr-cmark-gfm](https://github.com/amauryt/cr-cmark-gfm) - cmark-gfm 的 Crystal C 绑定可与 Commonmark 和 Github Flavored Markdown 配合使用
 * [markd](https://github.com/icyleaf/markd) - 另一种为提高速度而构建的 Markdown 解析器，符合 CommonMark 规范

## 杂项
 * [aasm.cr](https://github.com/veelenga/aasm.cr) - 易于使用的 Crystal 类有限状态机
 * [any_hash.cr](https://github.com/Sija/any_hash.cr) - 具有更好的 JSON::Any 的递归哈希
 * [anyolite](https://github.com/Anyolite/anyolite) - 具有简单绑定的完整 mruby 解释器，允许在项目中轻松支持脚本
 * [burocracia.cr](https://github.com/vinibrsl/burocracia.cr) - burocracia.cr 用于验证、生成和格式化巴西 burocracia（例如 CPF、CNPJ 和 CEP）的独立分片
 * [callbacks](https://github.com/vladfaust/callbacks.cr) - 表达回调模块
 * [circuit_breaker](https://github.com/TPei/circuit_breaker) - 断路器模式的实现
 * [cpf_cnpj](https://codeberg.org/gunbolt/cpf_cnpj) - 提供用于验证和格式化 CPF 和 CNPJ 标识符的实用程序
 * [CrSignals](https://github.com/firejox/CrSignals) - 信号/槽通知库
 * [crystal-binary_parser](https://github.com/DanSnow/crystal-binary_parser) - 二进制解析器
 * [crystal-web-framework-stars](https://github.com/isaced/crystal-web-framework-stars) - Crystal 的 Web 框架，Github 上最受关注的
 * [crz](https://github.com/dhruvrajvanshi/crz) - 函数式编程库
 * [defined](https://github.com/wyhaines/defined.cr) - 基于常量定义、版本要求或环境变量设置的条件编译宏
 * [emoji.cr](https://github.com/veelenga/emoji.cr) - 表情符号库
 * [gphoto2-web.cr](https://github.com/Sija/gphoto2-web.cr) - libgphoto2 的 Web API
 * [immutable](https://github.com/lucaong/immutable) - 线程安全、持久、不可变集合的实现
 * [iterm2](https://github.com/toddsundsted/iterm2) - 使用 ITerm2 内联图像协议在终端内显示图像
 * [lua.cr](https://github.com/veelenga/lua.cr) - 与 liblua 的绑定及其周围的包装器
 * [luajit.cr](https://github.com/mdwagner/luajit.cr) - Crystal 的 LuaJIT 绑定
 * [monads](https://github.com/alex-lairan/monads) - Monad 实现
 * [observable](https://github.com/TPei/observable) - 观察者模式的实现
 * [pinger](https://github.com/spider-gazelle/pinger) - Ping IP 地址和 DNS 条目，无需 sudo
 * [port_midi](https://github.com/jimm/crystal_port_midi) - PortMIDI 跨平台 MIDI I/O 库的 Crystal C 绑定
 * [retriable.cr](https://github.com/Sija/retriable.cr) - 用于重试失败代码块的简单 DSL
 * [sentry](https://github.com/crystal-china/sentry) - 构建/运行您的水晶应用程序，监视文件，并在文件更改时重建/重新启动应用程序。
 * [serf-handler.cr](https://github.com/wyhaines/serf-handler.cr) - 用于构建 Serf 处理程序的框架，具有一套有用的内置功能
 * [simple_retry](https://github.com/spider-gazelle/simple_retry) - 用于重试失败代码块的简单工具
 * [sslscan.cr](https://github.com/NeuraLegion/sslscan.cr) - 水晶碎片包装 rbsec/sslscan 实用程序
 * [version_tools](https://github.com/anicholson/crystal-version-tools) - 版本相关的行为，在编译时指定
 * [wafalyzer](https://github.com/NeuraLegion/wafalyzer) - Web 应用程序防火墙 (WAF) 检测器 - shard + cli
 * [zaru_crystal](https://github.com/szTheory/zaru_crystal) - 文件名清理

## 网络协议
 * [amqp-client.cr](https://github.com/cloudamqp/amqp-client.cr) - AMQP 0-9.1，一种消息传递协议，由例如实现。 RabbitMQ
 * [connect-proxy](https://github.com/spider-gazelle/connect-proxy) - HTTP隧道/HTTP代理的Connect方法风格
 * [cr-xmpp](https://github.com/naqvis/cr-xmpp) - XMPP/Jabber 库
 * [Crirc](https://github.com/Meoowww/Crirc) - IRC 协议实现（客户端、服务器、机器人）
 * [crystal-bacnet](https://github.com/spider-gazelle/crystal-bacnet) - 使用 BACnet/IP 客户端实现 BACnet 协议
 * [crystal-json-socket](https://github.com/foi/crystal-json-socket) - JSON 套接字客户端和服务器实现。受到 [node-json-socket](https://github.com/sebastianseilund/node-json-socket/) 和 [ruby-json-socket](https://github.com/foi/ruby-json-socket) 的启发并兼容
 * [crystal-mqtt](https://github.com/spider-gazelle/crystal-mqtt) - MQTT 客户端
 * [crystal-snmp](https://github.com/spider-gazelle/crystal-snmp) - 支持版本 1、2c 和 3 的 SNMP 实现
 * [dns](https://github.com/spider-gazelle/dns) - DNS协议实现和解析器
 * [fast_irc.cr](https://github.com/RX14/fast_irc.cr) - 快速 IRC 解析器/生成器
 * [jwt](https://github.com/crystal-community/jwt) - JWT（JSON Web Token）的实现
 * [knx](https://github.com/spider-gazelle/knx) - KNX 协议实现支持多播、单播和 TCP/IP 隧道
 * [Matter](https://github.com/Crystal-Matter/matter) - 适用于智能家居和物联网 (IoT) 设备的 Matter 协议
 * [mDNS](https://github.com/spider-gazelle/mdns) - DNS 服务发现和组播 DNS
 * [mqtt-client.cr](https://github.com/84codes/mqtt-client.cr) - 快速、轻量级的 MQTT 客户端
 * [msgpack-crystal](https://github.com/crystal-community/msgpack-crystal) - 消息包库
 * [OAuth](https://crystal-lang.org/api/OAuth.html) - OAuth 使用者（Crystal stdlib）
 * [OAuth2](https://crystal-lang.org/api/OAuth2.html) - OAuth2 客户端（Crystal stdlib）
 * [OpenSSL](https://crystal-lang.org/api/OpenSSL.html) - 绑定到 libssl (Crystal stdlib)
 * [simple_rpc](https://github.com/kostya/simple_rpc) - Crystal 的 RPC 服务器和客户端。实现msgpack-rpc协议
 * [stomp](https://github.com/spider-gazelle/stomp) - STOMP协议
 * [telnet.cr](https://github.com/spider-gazelle/telnet.cr) - 远程登录协议
 * [transfer_more](https://git.sceptique.eu/Sceptique/transfer_more) - 克隆transfer.sh来上传文件

## 网络
 * [ipaddress.cr](https://github.com/Sija/ipaddress.cr) - 处理 IPv4 和 IPv6 地址的库
 * [mac-address](https://github.com/automatico/mac-address) - 用于处理 MAC 地址的库

## ORM/ODM 扩展
 * [avram](https://github.com/luckyframework/avram) - 用于读取、写入和迁移 Postgres 数据库的数据库包装器
 * [clear](https://github.com/anykeyh/clear) - ORM 仅适用于 PostgreSQL，但具有高级功能
 * [crecto](https://github.com/Crecto/crecto) - 数据库包装器，基于Ecto
 * [granite](https://github.com/amberframework/granite) - Postgres、Mysql、Sqlite 的 ORM
 * [jennifer.cr](https://github.com/imdrasil/jennifer.cr) - 使用灵活的查询可链接构建器和迁移系统实现 Active Record 模式
 * [lustra](https://github.com/crystal-garage/lustra) - 具有 ActiveRecord 模式、全文搜索、几何类型等的高级 PostgreSQL ORM
 * [rethinkdb-orm](https://github.com/spider-gazelle/rethinkdb-orm) - RethinkDB / RebirthDB 的 ORM

## 包管理
 * [shards](https://github.com/crystal-lang/shards) - Crystal 的依赖管理器

## 进程和线程
 * [await_async](https://github.com/anykeyh/await_async) - 在 Crystal Lang 中添加关键字等待和异步
 * [concurrent.cr](https://github.com/didactic-drunk/concurrent.cr) - 使用流/管道、等待组、信号量、smores 等简化并发
 * [neph](https://github.com/tbrand/neph) - 可以同时执行作业的现代命令行作业处理器
 * [promise](https://github.com/spider-gazelle/promise) - 带有类型推断的 Promise 实现
 * [werk](https://github.com/marghidanu/werk) - 非常简单的任务运行程序，具有并发支持，非常适合本地 CI

## 项目生成器
 * [crygen](https://github.com/tamdaz/crygen) - 允许生成 Crystal 代码的库
 * [crystal_lib](https://github.com/crystal-lang/crystal_lib) - 本机库的自动绑定生成器
 * [fez](https://github.com/jwoertink/fez) - Kemal 应用程序生成器
 * [libgen](https://github.com/olbat/libgen) - 使用 JSON/YAML 文件配置的自动绑定生成器

## 队列和消息传递
 * [crafka](https://github.com/BT-OpenSource/crafka) - 使用“librdkafka”的 Apache Kafka 库
 * [mosquito](https://github.com/mosquito-cr/mosquito/) - Redis 支持定期和临时作业处理
 * [NATS.io](https://github.com/nats-io/nats.cr) - NATS客户端
 * [sidekiq.cr](https://github.com/mperham/sidekiq.cr) - 简单、高效的作业处理

## 路由
 * [orion](https://github.com/obsidian/orion) - 一个最小的、类似 Rails 的路由库
 * [router.cr](https://github.com/tbrand/router.cr) - 用于 HTTP::Server 的最小但功能强大的 http 路由器

## 调度
 * [crystime](https://gitlab.com/crystallabs/crystime) - 高级时间、日历、日程和提醒库
 * [schedule.cr](https://github.com/hugoabonizio/schedule.cr) - 运行周期性任务
 * [tasker](https://github.com/spider-gazelle/tasker) - 高精度调度程序，包括时区感知 cron 作业

## 科学与数据分析
 * [alea](https://github.com/nin93/alea) - 可重复采样、CDF 和其他处理概率分布的实用程序
 * [ishi](https://github.com/toddsundsted/ishi) - 具有小型 API 和由 gnuplot 支持的合理默认值的图形绘制包
 * [linalg](https://github.com/konovod/linalg) - 受 MATLAB 和 SciPy.linalg 启发的线性代数库
 * [num.cr](https://github.com/crystal-data/num.cr) - 支持N维数据的数值计算库
 * [predict.cr](https://github.com/RX14/predict.cr) - 使用sgp4模型的卫星预测库
 * [quartz](https://github.com/RomainFranceschini/quartz) - 建模与仿真框架

## 搜索
 * [hermes](https://github.com/imdrasil/hermes.cr) - ElastiSearch 的数据映射器模式实现

## 安全性
 * [cyclonedx-cr](https://github.com/hahwul/cyclonedx-cr) - 用于 Crystal 项目的 CycloneDX SBOM（软件物料清单）生成器
 * [OWASP Noir](https://github.com/owasp-noir/noir) - 通过静态分析识别端点的攻击面检测器
 * [XSSMaze](https://github.com/hahwul/xssmaze) - XSSMaze 是一项使用各种 XSS 案例测试安全工具的 Web 服务

## 无服务器计算
 * [crystal_openfaas](https://github.com/TPei/crystal_openfaas/) - 使 Crystal 成为 OpenFaaS 中一等公民的模板
 * [secrets-env](https://github.com/spider-gazelle/secrets-env) - 扩展 ENV 模块以读取 docker / kubernetes 机密和其他编排工具注入的值

## 系统
 * [baked_file_system](https://github.com/schovi/baked_file_system) - 虚拟文件系统的实现
 * [hardware](https://github.com/crystal-community/hardware) - 获取正在运行的操作系统及其进程的CPU、内存和网络信息

## 任务管理
 * [cake](https://github.com/axvm/cake) - 生产就绪的类似 Make 的实用工具
 * [sam](https://github.com/imdrasil/sam.cr) - 另一种类似 Rake 的任务管理器，具有命名空间和参数系统

## 模板引擎
 * [crinja](https://github.com/straight-shoota/crinja) - [Jinja2模板引擎](http://jinja.pocoo.org/)的实现
 * [crustache](https://github.com/MakeNowJust/crustache) - Crystal 的 [{{Mustache}}](https://mustache.github.io)
 * [ECR (Embedded Crystal)](https://crystal-lang.org/api/ECR.html) - 使用普通水晶表达式的编译时模板语言（Crystal stdlib）
 * [Jbuilder](https://github.com/shootingfly/jbuilder) - 受 jbuilder 启发，使用 Builder 风格的 DSL 生成 JSON 对象
 * [Kilt](https://github.com/jeromegn/kilt) - 模板引擎的抽象层
 * [Slang](https://github.com/jeromegn/slang) - 受 Ruby 的 Slim 启发的轻量级、简洁的模板语言
 * [teeplate](https://github.com/mosop/teeplate) - 用于渲染多个模板文件的库

## 测试
 * [Athena Spec](https://github.com/athena-framework/spec) - 常见/有用的 [Spec](https://crystal-lang.org/api/Spec.html) 兼容测试实用程序
 * [crotest](https://github.com/emancu/crotest) - 一个微小而简单的测试框架
 * [crytic](https://github.com/hanneskaeufler/crytic) - 突变测试框架
 * [hashr](https://github.com/crystal-china/hashr) - 一个小类使 JSON 响应测试变得更容易
 * [LuckyFlow](https://github.com/luckyframework/lucky_flow) - 类似于 Capybara 的自动化浏览器测试
 * [mass-spec](https://github.com/c910335/mass-spec) - Web API 测试库
 * [microtest](https://github.com/Ragmaanir/microtest) - 专注于功率断言的小型固执己见的测试库
 * [minitest.cr](https://github.com/ysbaddaden/minitest.cr) - 用于单元测试和断言的库
 * [mocks.cr](https://github.com/waterlink/mocks.cr) - Crystal 的模拟库
 * [selenium.cr](https://github.com/crystal-loot/selenium.cr) - Selenium 客户端用于与网页交互以实现浏览器自动化
 * [Spec](https://crystal-lang.org/api/Spec.html) - 规范框架（Crystal stdlib）
 * [spectator](https://gitlab.com/arctic-fox/spectator) - 使用现代期望语法的功能丰富的规范框架
 * [timecop.cr](https://github.com/crystal-community/timecop.cr) - 用于使用“Time.now”进行模拟的库。受到 [timecop ruby gem](https://github.com/travisjeffery/timecop) 的启发
 * [vcr](https://github.com/spoved/vcr.cr) - crystal 的 HTTP 捕获和重放实现
 * [webdriver_pump](https://github.com/bwilczek/webdriver_pump) - 页面对象库。受到 Ruby 的 [WatirPump](https://github.com/bwilczek/watir_pump) 的启发
 * [webmock.cr](https://github.com/manastech/webmock.cr) - 用于存根“HTTP::Client”请求的库

## 第三方API
 * [amazonite](https://github.com/rjnienaber/amazonite) - 支持流行的 AWS API 的非官方 SDK
 * [aws-signer.cr](https://github.com/beanieboi/aws-signer.cr) - 该库使用 AWS v4 签署您的 HTTP 请求
 * [awscr-s3](https://github.com/taylorfinnell/awscr-s3) - AWS S3 接口
 * [awscr-signer](https://github.com/taylorfinnell/awscr-signer) - 签署 HTTP::Request 对象并生成预签名的帖子表单
 * [crystal-consul](https://github.com/rogerwelin/crystal-consul) - 领事API客户端
 * [crystal-darksky](https://github.com/sb89/crystal-darksky) - [Dark Sky](https://darksky.net) API 的包装器
 * [crystal-swapi](https://github.com/sb89/crystal-swapi) - 星球大战 API (SWAPI) 包装器
 * [crystal_slack](https://github.com/manastech/crystal_slack) - 解析 Slack 斜杠命令或发送传入 Web 挂钩的工具
 * [GDAX](https://github.com/mccallofthewild/gdax) - 具有请求签名功能的 GDAX REST 和 WebSocket API 包装器
 * [gitlab.cr](https://github.com/icyleaf/gitlab.cr) - GitLab API 包装器
 * [google](https://github.com/PlaceOS/google) - 谷歌 API 包装器
 * [host_meta](https://github.com/toddsundsted/host_meta) - Web 主机元数据 (https://tools.ietf.org/html/rfc6415) 客户端
 * [kube-client.cr](https://github.com/spoved/kube-client.cr) - Kubernetes API 客户端
 * [mixpanel-crystal](https://github.com/petoem/mixpanel-crystal) - 用于将事件发送到 Mixpanel 的库
 * [mollie.cr](https://github.com/wout/mollie.cr) - [Mollie](https://www.mollie.com/en/) 支付 API 包装器（信用卡、PayPal、Apple Pay、Sofort、Klarna 等）
 * [office365](https://github.com/PlaceOS/office365) - Microsoft Graph API 包装器
 * [pinboard.cr](https://github.com/oz/pinboard.cr) - [插板](https://pinboard.in) API
 * [raven.cr](https://github.com/sija/raven.cr) - Raven 是 [Sentry](https://github.com/getsentry/sentry) 的客户端
 * [stripe.cr](https://github.com/confact/stripe.cr) - Stripe api 包装器
 * [tmdb.cr](https://github.com/mmacia/tmdb.cr) - 电影数据库 (TMDb) API 包装器
 * [twitter-crystal](https://github.com/sferik/twitter-crystal) - 用于访问 Twitter API 的库
 * [web_finger](https://github.com/toddsundsted/web_finger) - WebFinger (https://tools.ietf.org/html/rfc7033) 客户端
 * [ynab.cr](https://github.com/jaredsmithse/ynab.cr) - 与 YNAB 数据交互的库

## 验证
 * [accord](https://github.com/neovintage/accord) - Crystal Objects 的可共享验证库
 * [Athena Validator](https://github.com/athena-framework/validator) - 强大且灵活的验证框架
 * [validations](https://github.com/vladfaust/validations.cr) - 验证混合
 * [validator](https://github.com/Nicolab/crystal-validator) - 数据检查和验证

## 网络框架
 * [amber](https://github.com/amberframework/amber) - 开源高效且具有凝聚力的 Web 应用程序框架
 * [Athena](https://github.com/athena-framework/athena) - 由可重用的独立组件组成的 Web 框架
 * [grip](https://github.com/grip-framework/grip) - 用于编写功能强大的 Web 应用程序的微框架
 * [kemal](https://github.com/kemalcr/kemal) - 闪电般快速、超级简单的 Web 框架。受到西纳特拉的启发
 * [lucky](https://github.com/luckyframework/lucky) - 及早发现错误，忘记大多数性能问题，并将更多时间花在代码上，而不是调试和编写测试
 * [marten](https://github.com/martenframework/marten) - 一个 Web 框架，使构建 Web 应用程序变得简单、高效且有趣
 * [runcobo](https://github.com/runcobo/runcobo) - 一个具有简单、直观和一致 DSL 的 api 框架，使用 jbuilder 渲染 json
 * [Shivneri](https://github.com/ujjwalguptaofficial/shivneri) - Crystal 的基于组件的 MVC Web 框架，目标是良好的代码结构、模块化和性能
 * [spider-gazelle](https://github.com/spider-gazelle/spider-gazelle) - 一个 Rails 式的 Web 框架，注重速度和可扩展性

# 社区
 * [水晶论坛](https://forum.crystal-lang.org/)
 * [水晶通讯](https://crystal-lang.org/#newsletter)
 * [Gitter](https://gitter.im/crystal-lang/crystal)
 * [IRC](ircs://irc.libera.chat:6697#crystal-lang) - Libera 上的 #crystal-lang
 * [Reddit](https://www.reddit.com/r/crystal_programming/)
 * [Stackoverflow](https://stackoverflow.com/tags/crystal-lang/info)

## 非官方
 * [Crystal Programming Discord Server](https://discord.gg/YS7YvQy) - 专用于 Crystal 编程语言的非官方 Discord 服务器
 * [Portuguese-speaking Telegram Group](https://t.me/crystalbrasil) - Bem vindos ao 水晶巴西！
 * [Russian-speaking Telegram Group](https://t.me/crystal_ru) - Добро пожаловать, товарищ！

# 资源
 * [Crystal for Rubyists](http://www.crystalforrubyists.com/) - 免费书籍引导您的水晶之旅
 * [Crystal Shards for Ruby Gems](https://github.com/crystal-lang/crystal/wiki/Crystal-Shards-for-Ruby-Gems) - 红宝石及其水晶碎片的列表
 * [crystal-koans](https://github.com/ilmanzo/crystal-koans) - 通过编写单元测试来学习 Crystal
 * [crystal-lang.org](https://crystal-lang.org) - 官方语言网站
 * [devdocs.io](https://devdocs.io/crystal/) - 支持 Crystal 的 API 文档浏览器
 * [Learn X in Y minutes](https://learnxinyminutes.com/docs/crystal/) - 水晶快速教程
 * [Programming Crystal](https://pragprog.com/book/crystal/programming-crystal) - PragProg 书籍开启您的水晶之旅
 * [Usability of Programming Languages](https://gergelyk.github.io/prog-lang-usability/) - Python、Rust、Crystal 的比较

## 官方文档翻译
 * [br.crystal-lang.org](http://br.crystal-lang.org/) - 巴西人
 * [ja.crystal-lang.org](http://ja.crystal-lang.org/) - 日语
 * [kr.crystal-lang.org](https://kr.crystal-lang.org/) - 韩语
 * [ru.crystal-lang.org](http://ru.crystal-lang.org/) - 俄语
 * [tw.crystal-lang.org](http://tw.crystal-lang.org/) - 繁体中文

# 服务和应用程序
 * [carc.in](https://carc.in/) - 运行您的代码并显示结果的 Web 服务
 * [Crank](https://github.com/arktisklada/crank) - 基于 Procfile 的应用程序管理器（如 Foreman）
 * [cry](https://github.com/elorest/cry) - 能够以类似于 Ruby 的 pry edit 的方式执行水晶代码
 * [DeBot](https://github.com/jhass/DeBot) - 用 Crystal 编写的 IRC 机器人
 * [icr](https://github.com/crystal-community/icr) - Crystal 的交互式控制台（如 Ruby 的 IRB）
 * [Invidious](https://github.com/iv-org/invidious) - Invidious 是 YouTube 的替代前端
 * [mpngin](https://github.com/thewalkingtoast/mpngin) - 具有简单统计信息的 URL 缩短器
 * [procodile](https://github.com/crystal-china/procodile) - 从 Procfile 在 Mac 和 Linux 上的后台（和前台）运行进程（适用于生产和/或开发环境）
 * [quicktype](https://quicktype.io/) - 从 JSON、JSON Schema、GraphQL 和 TypeScript 生成模型和序列化器
 * [shards.info](http://shards.info/) - Web 服务，列出 GitHub 上包含 Crystal 代码的所有存储库。源代码可在 [GitHub](https://github.com/mamantoha/shards-info) 上找到

# 工具
 * [ast_helper](https://github.com/bcardiff/crystal-ast-helper) - 调试解析器和格式化程序的帮助工具
 * [crystal-base](https://github.com/ruivieira/crystal-base) - 用于 Crystal 开发的 CentOS 基础 docker 镜像
 * [crystal-dash-docset](https://github.com/Sija/crystal-dash-docset) - [Dash](https://kapeli.com/dash) 文档集生成器
 * [port_ruby_to_crystal](https://github.com/crystal-china/port_ruby_to_crystal) - 正则表达式替换 ruby 脚本，用于将 ruby 代码移植到水晶更容易，减少摩擦
 * [public_suffix](https://github.com/toddsundsted/public_suffix) - 一个小型库，旨在使公共后缀列表 (https://publicsuffix.org/) 更易于使用

## 开发运营
 * [ansible-crystal](https://github.com/CorbanR/ansible-crystal) - 用于安装 Crystal 的 Ansible 剧本
 * [DPPM](https://github.com/DFabric/dppm) - 以包的形式安装和管理应用程序的简单、通用的方法（主要是 Linux）

## 编辑器插件
* 极致：
   * [acmecrystal](https://github.com/ilanpillemer/acmecrystal) - 在 acme 中重新格式化水晶代码
* 原子
   * [crystal-tools](https://atom.io/packages/crystal-tools) - 启用 Crystal 编译器中的内置工具
   * [language-crystal-actual](https://atom.io/packages/language-crystal-actual) - Atom 中的 Crystal 语言支持
* Emacs
   * [crystal-mode](https://melpa.org/#/crystal-mode) - Emacs 的 Crystal 语言支持 ([crystal-lang-tools/emacs-crystal-mode](https://github.com/crystal-lang-tools/emacs-crystal-mode))
* 吉尼
   * [geany-crystal](https://github.com/crystal-lang-tools/geany-crystal) - 对 [Geany 编辑器](https://www.geany.org/) 的水晶支持
* IntelliJ IDEA
   * [intellij-crystal-lang](https://github.com/asedunov/intellij-crystal-lang) - 对 JetBrains IDE 的水晶支持
* 精简版-XL
   * [lite-plugin-crystal](https://github.com/Tamnac/lite-plugin-crystal) - 对 [Lite-XL](https://lite-xl.com/en/) 编辑器的 Crystal 支持
* 太空麦克斯
   * [crystal-spacemacs-layer](https://github.com/juanedi/crystal-spacemacs-layer) - Crystal 的 Spacemacs 贡献层
* 崇高
   * [sublime-crystal](https://github.com/crystal-lang-tools/sublime-crystal) - Sublime Text 的水晶语法高亮
* 文本伴侣
   * [Crystal.tmbundle](https://github.com/crystal-lang-tools/Crystal.tmbundle) - Crystal 语法高亮、编译、格式化命令、片段
*维姆
   * [vim-crystal](https://github.com/vim-crystal/vim-crystal) - Vim 对 Crystal 的文件类型支持
   * [vim-slang](https://github.com/elorest/vim-slang) - Vim 对俚语模板引擎的文件类型支持
* 视觉工作室代码
   * [vscode-crystal-lang](https://github.com/crystal-lang-tools/vscode-crystal-lang) - `cr` 和 `ecr` 文件的格式化程序、linter 和语法突出显示

## LSP语言服务器协议实现
 * [crystalline](https://github.com/elbywan/crystalline) - Crystalline 是用 Crystal 语言编写并针对 Crystal 语言编写的语言服务器协议的实现
 * [scry](https://github.com/crystal-lang-tools/scry) - Crystal 的代码分析服务器实现[语言服务器协议](https://microsoft.github.io/language-server-protocol/)

## 外壳插件
 * [crun](https://github.com/Val/crun) - Crystal Run：Crystal 的 shebang 包装
 * [crystal-zsh](https://github.com/veelenga/crystal-zsh) - .oh-my-zsh 插件
