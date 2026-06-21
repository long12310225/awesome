# 很棒的 Clojure [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

- [Clojure 中很棒的产品](#awesome-products-in-clojure)
- [OneKeePass](https://github.com/OneKeePass/desktop)：安全密码管理器和[ClojureScript 中的移动应用程序](https://github.com/OneKeePass/mobile)
- [Penpot](https://penpot.app/)：设计和原型平台
- [LightTable (IDE)](http://lighttable.com/)（已存档）
  - [Maria.cloud（适合初学者的在线 IDE）](https://www.maria.cloud/)
  - [黎曼（监控）](http://riemann.io/)
  - [Precursor（在线原型设计工具）](https://precursorapp.com/)
  - [傀儡服务器](https://github.com/puppetlabs/puppet-server)
  - [PuppetDB](https://github.com/puppetlabs/puppetdb)
  - [Metabase](https://github.com/metabase/metabase)
  - [元数据库 Datomic](https://github.com/lambdaisland/metabase-datomic)
  - [CircleCI](https://circleci.com/)
  - [Avi（vim 重写）](https://github.com/maitria/avi)
  - [液体（文本编辑器）](https://github.com/mogenslund/liquid)
  - [Clojupyter](https://github.com/clojupyter/clojupyter)
  - [meins](https://github.com/matthiasn/meins)
  - [Jepsen](https://github.com/jepsen-io/jepsen)
- [Braid](https://github.com/braidchat/braid)：一款团队聊天应用程序，具有新颖的 UI，可以带来更好的对话
- [Accelerated Text](https://github.com/tokenmill/accelerated-text)：自然语言生成环境（后端：Clojure，前端：JS）
- [Ziggurat](https://github.com/gojek/ziggurat)：一个为简化 Kafka 上的流处理而构建的框架
- [Nightcode](https://github.com/oakes/Nightcode)：Clojure 的 IDE（已存档）
- [Nightlight](https://github.com/oakes/Nightlight)：文本编辑器（已存档）
- [Atea](https://github.com/pkamenarsky/atea)：MacOS 的简约菜单栏时间跟踪器（旧版，需要 jvm 1.6）
  - [herfi](https://github.com/ertugrulcetin/herfi) - 用 Clojure 和 ClojureScript 编写的 3D 多人游戏原型
  - [racing-game-cljs](https://github.com/ertugrulcetin/racing-game-cljs) - 使用 ClojureScript、React 和 ThreeJS 构建的 3D 赛车游戏
- [Clojure 中很棒的 SaaS（部分 OSS）](#awesome-saas-in-clojure)
- [Logseq](https://github.com/logseq/logseq)：知识管理和协作（开放前端）
- [用 Clojure 编写的语言](#languages-written-with-clojure)
  - [jank](https://github.com/jeaye/jank)
  - [lux](https://github.com/LuxLang/lux)
  - [mal](https://github.com/kanaka/mal/tree/master/impls/clojure)
  - [scheje](https://github.com/turbopape/scheje)
  - [eden](https://github.com/benzap/eden)
  - [ferret](https://ferret-lang.org)
- [Clojure 中很棒的工具](#awesome-tools-in-clojure)
  - [很棒的宏用法](#awesome-macros-usage)
  - [高级数据结构](#advanced-datastructures)
  - [网络框架](#web-framework)
  - [依赖注入](#dependency-injection)
  - [构建自动化和包管理](#build-automation-and-package-management)
  - [版本控制管理](#version-control-management)
  - [日期和时间](#date-and-time)
  - [GUI](#gui)
  - [Audio](#audio)
  - [HTTP](#http)
  - [Database](#database)
  - [连接池](#connection-pools)
  - [结构迁移](#structural-migrations)
  - [Redis](#redis)
  - [JSON](#json)
  - [协议缓冲区和 gRPC](#protocol-buffers-and-grpc)
  - [ORM 和 SQL 生成](#orm-and-sql-generation)
  - [Security](#security)
  - [RESTful API](#restful-api)
  - [GraphQL API](#graphql-api)
  - [Emails](#emails)
  - [HTML操作](#html-manipulation)
  - [数据验证](#data-validation)
  - [类型系统](#type-system)
  - [模式匹配](#pattern-matching)
  - [异步处理](#async-processing)
  - [Monads](#monads)
  - [WebSocket](#websocket)
  - [Testing](#testing)
  - [Webdriver自动化](#webdriver-automation)
  - [代码分析和 Linter](#code-analysis-and-linter)
  - [科学与数据分析](#science-and-data-analysis)
  - [机器学习](#machine-learning)
  - [计算机视觉](#computer-vision)
  - [文本处理](#text-processing)
  - [Parsing](#parsing)
  - [编辑器插件](#editor-plugins)
  - [Documentation](#documentation)
  - [文学编程](#literate-programming)
  - [档案和压缩](#archives-and-compression)
  - [Miscellaneous](#miscellaneous)
  - [调试工具](#debugging)
  - [CI](#ci)
  - [项目管理](#project-management)
  - [终端用户界面](#terminal-ui)
  - [Graphviz](#graphviz)

- [Resources](#resources)
  - [Guides](#guides)
  - [视频教程](#video-tutorials)
  - [Websites](#websites)
  - [Twitter](#twitter)
  - [Exercises](#exercises)

## 很棒的宏用法

*解答为什么 lisp 如此出色，杀手级功能正在发挥作用*

  * [core.async](https://github.com/clojure/core.async) - 将 AST 转换为 CSP 程序
  * [cloroutine](https://github.com/leonoel/cloroutine) - 暂停和继续（协程）
  * [missionary](https://github.com/leonoel/missionary) - 反应式数据流编程工具包
  * [photon](https://github.com/venantius/photon) - 实时网络，类似于 Meteor，但适用于 Clojure（脚本）
  * [metaclj](https://github.com/brandonbloom/metaclj) - 分阶段编译
  * [meander](https://github.com/noprompt/meander) - 使用数据结构模式匹配的透明数据转换
  * [proteus](https://github.com/ztellman/proteus) - 引入可变变量（不要使用，只是学习如何将你的思维映射到不可变的世界）
## 高级数据结构

* [specter](https://github.com/redplanetlabs/specter)：一个优雅的 API，用于查询和转换嵌套和递归数据
* [meander](https://github.com/noprompt/meander)：透明数据转换（定义为模式匹配）
* [持久 AVL 树](https://github.com/clojure/data.avl)：具有日志时间排名查询的持久排序映射和集合
* [手指树](https://github.com/clojure/data.finger-tree): 双列表、计数双列表、计数排序集
* [Hitchhiker Tree](https://github.com/datacrypt-project/hitchhiker-tree)：创建快速、可快照、大规模可扩展的数据库
  * [层次集](https://github.com/llasram/hier-set)
* [Ordered](https://github.com/amalloy/ordered): 有序集和映射
* [Lazy Map](https://github.com/Malabarba/lazy-map-clojure)：其值仅在访问时计算
* [Duratom](https://github.com/jimpil/duratom): 持久化原子
* [持久队列](https://github.com/Factual/durable-queue): 队列持久化在磁盘上
* [bifurcan](https://github.com/lacuna/bifurcan): 线性映射/集合/列表(在内存中连续存储条目)，;用java编写，但测试套件(阅读：使用示例)[在clojure中](https://github.com/lacuna/bifurcan/blob/master/test/bifurcan)
  
## 网络框架

*其实这里不要搜索rails/django，而是自己编写*
  * [Compojure](https://github.com/weavejester/compojure)
  * [Compojure-api](https://github.com/metosin/compojure-api)
  * [Luminus](http://www.luminusweb.net/)
  * [Duct](https://github.com/weavejester/duct)
  * [Pedestal](https://github.com/pedestal/pedestal)
  * [Datsys](https://github.com/metasoarous/datsys)
  * [yada](https://github.com/juxt/yada)
  * [Hoplon](http://hoplon.io/)
  * [Fulcro](https://github.com/fulcrologic/fulcro)
  * [Coast](http://coastonclojure.com/)
  * [Reitit](https://github.com/metosin/reitit)
  * [Tadam](https://www.tadam-framework.dev/)
  * [Column](https://gitlab.com/demonshreder/column)
  * [Biff](https://biffweb.com/)

## 依赖注入

*有状态对象的托管生命周期*

  * [Component](https://github.com/stuartsierra/component)
  * [System](https://github.com/danielsz/system)
  * [mount](https://github.com/tolitius/mount)
  * [Integrant](https://github.com/weavejester/integrant)
  * [clip](https://github.com/juxt/clip)
  * [piotr-yuxuan/closeable-map](https://github.com/piotr-yuxuan/closeable-map)
  * [darkleaf/di](https://github.com/darkleaf/di)

## 构建自动化和包管理

*用于项目构建自动化和包/依赖项管理的库。*

  * [Leiningen](https://github.com/technomancy/leiningen)
  * [Boot](https://github.com/boot-clj/boot)
  * [tools.build](https://www.clojure.org/guides/tools_build)
    * [build.simple](https://github.com/gnl/build.simple)
* [clojurephant](https://github.com/clojurephant/clojurephant) (Gradle 插件)
* [shadow-cljs](https://github.com/thheller/shadow-cljs) (Clojurescript)

## 版本控制管理

*用于与 VCS 软件交互的代码实用程序*

  * [clj-jgit](https://github.com/clj-jgit/clj-jgit)

## 日期和时间

*用于处理日期和时间的库。*

  * [clj-time](https://github.com/clj-time/clj-time)
  * [clojure.java-time](https://github.com/dm3/clojure.java-time) - Java 8 日期时间 API
  * [holi](https://github.com/luciolucio/holi) - 考虑周末和节假日的日历操作
  * [timewords](https://github.com/tokenmill/timewords)
* [tick](https://github.com/juxt/tick): Clojure(Script) 库，旨在替代 clj-time

## 图形用户界面

  * [seesaw](https://github.com/daveray/seesaw)
  * [trikl](https://github.com/lambdaisland/trikl)
  * [fx-clj](https://github.com/aaronc/fx-clj)

## 音频

  * [Overtone](http://overtone.github.io/)
  * [Alda](https://github.com/alda-lang/alda)

## HTTP协议

*用于使用 HTTP 的库。*

* [clj-http](https://github.com/dakrone/clj-http) : Apache HttpComponents 客户端包装器
* [http-kit](https://github.com/http-kit/http-kit) : 简单、高性能的事件驱动的 HTTP 客户端和服务器
* [ring](https://github.com/ring-clojure/ring) : HTTP 服务器抽象
* [kvlt](https://github.com/nervous-systems/kvlt) ：跨 JVM / Node / 浏览器的 HTTP 统一异步客户端接口
* [aleph](https://github.com/clj-commons/aleph) : 基于 Netty 的异步客户端/服务器，默认为 HTTP、TCP 和 UDP
* [hato](https://github.com/gnarroway/hato) : Clojure 的 HTTP 客户端，包装 JDK 11 的 HttpClient

## 数据库

*数据库和数据库客户端库*

  * [Datomic](http://www.datomic.com/)
* [xtdb](https://github.com/xtdb/xtdb)：用于 SQL、数据日志和图形查询的双时态数据库
  * [Datahike](https://github.com/replikativ/datahike)
  * [Datascript](https://github.com/tonsky/datascript)
  * [Datalevin](https://github.com/juji-io/datalevin)
  * [next.jdbc](https://github.com/seancorfield/next-jdbc)
  * [clojure.java.jdbc](https://github.com/clojure/java.jdbc)
  * [clojure.jdbc](https://github.com/funcool/clojure.jdbc)
  * [cravendb](https://github.com/robashton/cravendb)
* [Monger](http://clojuremongodb.info/): 用于 MongoDB
* [Monglorious](https://baumandm.github.io/monglorious/): 用于 MongoDB
* [cmql](https://github.com/tkaryadis/cmql-core): 用于 MongoDB
* [clj-rethinkdb](https://github.com/apa512/clj-rethinkdb): 用于 RethinkDB
* [修订](https://github.com/bitemyapp/revise)：用于 RethinkDB
* [Spandex](https://github.com/mpenet/spandex)：用于 ElasticSearch
* [Elastisch](http://clojureelasticsearch.info/)：用于 ElasticSearch
* [neocons](http://clojureneo4j.info/)：用于 Neo4j
* [Alia](https://github.com/mpenet/alia): 对于 Cassandra
* [aerospike-clj](https://github.com/AppsFlyer/aerospike-clj)：用于 Aerospike

## 连接池

*数据库连接池*

  * [hikari-cp](https://github.com/tomekw/hikari-cp)
  * [metabase/connection-pool](https://github.com/metabase/connection-pool)

## 结构迁移

*保持数据库和其他同步*

  * [Lobos](https://github.com/budu/lobos)
  * [Ragtime](https://github.com/weavejester/ragtime)
  * [Joplin](https://github.com/juxt/joplin)
  * [Migratus](https://github.com/yogthos/migratus)
  * [Drift](https://github.com/macourtney/drift)

## 雷迪斯

  * [carmine](https://github.com/ptaoussanis/carmine)
  * [celtuce](https://github.com/lerouxrgd/celtuce)

## JSON

  * [cheshire](https://github.com/dakrone/cheshire)
  * [jsonista](https://github.com/metosin/jsonista)

## 协议缓冲区和 gRPC

  * [pronto](https://github.com/AppsFlyer/pronto)
  * [lein-protodeps](https://github.com/AppsFlyer/lein-protodeps)
  * [protojure](https://github.com/metosin/protojure)

## 数据库命令行

## ORM 和 SQL 生成

*用于 SQL 生成的 DSL。*
  * [Walkable](https://github.com/walkable-server/walkable)
  * [Korma](https://github.com/korma/Korma)
  * [Specql](https://github.com/tatut/specql/)
  * [stch-library/sql](https://github.com/stch-library/sql)
  * [sqlingvo](https://github.com/r0man/sqlingvo)
  * [sqlium](https://github.com/TheLadders/sqlium/)
  * [honeysql](https://github.com/jkk/honeysql)
  * [Toucan](https://github.com/metabase/toucan)

## 安全性

*身份验证、授权和其他安全相关的库。*

  * [Buddy](https://github.com/funcool/buddy)
* [caesium](https://github.com/lvh/caesium)（libsodium 绑定）
  * [Friend](https://github.com/cemerick/friend)
  * [secrets.clj](https://github.com/lk-geimfari/secrets.clj)
  * [bolt](https://github.com/juxt/bolt)
* [EACL](https://github.com/theronic/eacl)：基于 SpiceDB 的 ReBAC 授权库，由 Datomic 支持

## RESTful API

*用于开发 RESTful API 的库。*

  * [Liberator](http://clojure-liberator.github.io/liberator/)
  * [Compojure-api](https://github.com/metosin/compojure-api)
  * [Friboo](https://github.com/zalando/friboo)
  * [yada](https://github.com/juxt/yada)
  * [router](https://github.com/darkleaf/router)
  * [reitit](https://github.com/metosin/reitit)

## GraphQL API

*用于开发 GraphQL API 的库。*

  * [Lacinia](https://lacinia.readthedocs.io/en/latest/)

## 电子邮件

  * [postal](https://github.com/drewr/postal)

## HTML操作

*用于处理 HTML 的库。*

  * [Enlive](https://github.com/cgrand/enlive/wiki)
  * [hiccup](https://github.com/weavejester/hiccup)
  * [clostache](https://github.com/fhd/clostache)
  * [selmer](https://github.com/yogthos/Selmer)

## 数据验证

*用于验证数据的库。*

  * [Guardrails](https://github.com/fulcrologic/guardrails)
  * [Malli](https://github.com/metosin/malli)
  * [Validateur](http://clojurevalidations.info/)
  * [Prismatic 的架构](https://github.com/plumatic/schema)
  * [Bouncer](https://github.com/leonardoborges/bouncer)
  * [clova](https://github.com/markwoodhall/clova)
  * [Orchestra](https://github.com/jeaye/orchestra)
  * [struct](https://github.com/funcool/struct)
  * [domaintypes](https://github.com/friemen/domaintypes)

## 类型系统
*Clojure 的可选类型系统*

  * [core.typed](https://github.com/clojure/core.typed)

## 模式匹配

  * [core.match](https://github.com/clojure/core.match)
  * [defun](https://github.com/killme2008/defun)
  * [cats.match](https://github.com/zalando/cats.match)
  * [Akar](https://github.com/missingfaktor/akar)
  * [Meander](https://github.com/noprompt/meander)
  * [Verbal-Exprejon](https://github.com/WeshGuillaume/Verbal-Exprejon)

## 异步处理

  * [core.async](https://github.com/clojure/core.async/)
  * [pulsar](https://github.com/puniverse/pulsar)
  * [manifold](https://github.com/ztellman/manifold)
  * [goose](https://github.com/nilenso/goose)

## 单子

  * [cats](https://github.com/funcool/cats)
  * [algo.monads](https://github.com/clojure/algo.monads)
  * [Fluokitten](https://github.com/uncomplicate/fluokitten)

## WebSocket

  * [Chord](https://github.com/jarohen/chord)
  * [Sente](https://github.com/ptaoussanis/sente)
  * [aleph](https://github.com/ztellman/aleph)

## 测试

  * [Expectations](https://github.com/clojure-expectations/expectations)
  * [Midje](https://github.com/marick/Midje)
  * [test-doubles](https://github.com/GreenPowerMonitor/test-doubles) 
  * [kaocha](https://github.com/lambdaisland/kaocha)
  * [StateFlow](https://github.com/nubank/state-flow)
  * [Datest](https://github.com/amokfa/datest)

## Webdriver自动化

  * [Etaoin](https://github.com/igrishaev/etaoin)

## 代码分析和 Linter

  * [Slamhound](https://github.com/technomancy/slamhound)
  * [eastwood](https://github.com/jonase/eastwood)
  * [kibit](https://github.com/jonase/kibit)
  * [yagni](https://github.com/venantius/yagni)
  * [lein-bikeshed](https://github.com/dakrone/lein-bikeshed)
  * [spectrum](https://github.com/arohner/spectrum)
  * [cloverage](https://github.com/cloverage/cloverage)
  * [clj-kondo](https://github.com/borkdude/clj-kondo)
  * [splint](https://github.com/NoahTheDuke/splint)

## 科学与数据分析

*库、扩展 REPL 以及其他科学和统计数据工具
分析和可视化。*

  * [Incanter](https://github.com/incanter/incanter)
  * [Cascalog](http://cascalog.org/)
  * [Onyx](https://github.com/onyx-platform/onyx)
  * [sparklling](https://github.com/gorillalabs/sparkling)
  * [flambo](https://github.com/yieldbot/flambo)
  * [Neanderthal](https://github.com/uncomplicate/neanderthal)
  * [流媒体直方图](https://github.com/bigmlcom/histogram)
  * [大猩猩REPL](http://gorilla-repl.org/)
  * [Bayadera - GPU 上的贝叶斯数据分析](https://github.com/uncomplicate/bayadera)
  * [ClojureCUDA](https://github.com/uncomplicate/clojurecuda)
  * [尼安德特人 - 快速矩阵和线性代数](https://github.com/uncomplicate/neanderthal)
  * [ClojureCL - 使用 OpenCL 并行计算](https://github.com/uncomplicate/clojurecl)
  * [Loom - Clojure 图形库](https://github.com/aysylu/loom)

## 机器学习

* [neanderthal](https://github.com/uncomplicate/neanderthal): 快速矩阵库
  * [clojurecuda](https://github.com/uncomplicate/clojurecuda)
  * [clojurecl](https://github.com/uncomplicate/clojurecl)
* [bayadera](https://github.com/uncomplicate/bayadera): GPU 上的贝叶斯数据分析
  * [cortex](https://github.com/originrose/cortex)
  * [Flare](https://github.com/aria42/flare)
  * [MXNet - Clojure API](https://mxnet.apache.org/versions/1.7.0/api/clojure)
  * [clj-bigml](https://github.com/bigmlcom/clj-bigml)
  * [Deeplearning4j](https://github.com/deeplearning4j/deeplearning4j)
  * [Enclog](https://github.com/jimpil/enclog)
  * [lambda-ml](https://github.com/cloudkj/lambda-ml)
  * [clojure-tensorflow](https://github.com/kieranbrowne/clojure-tensorflow)
  * [dl4clj（deeplearning4j 到 clojure）](https://github.com/yetanalytics/dl4clj)
  * [Anglican](https://probprog.github.io/anglican/)
  * [clj-ml](https://github.com/antoniogarrote/clj-ml)
  * [Clatern](https://github.com/rinuboney/clatern)
  * [k9](https://github.com/gigasquid/k9)
  * [Statistiker](https://github.com/clojurewerkz/statistiker)
  * [Synaptic](https://github.com/japonophile/synaptic)
  * [Infer](https://github.com/aria42/infer)
  * [clj-synapses](https://github.com/mrdimosthenis/clj-synapses)
  * [scicloj.ml](https://github.com/scicloj/scicloj.ml)

## 计算机视觉

* [origami](https://github.com/hellonico/origami): OpenCV 4 包装器
  * [clj-tesseract](https://github.com/antoniogarrote/clj-tesseract)
  * [vision](http://nakkaya.com/vision.html)

## 文本处理

  * [clojure-opennlp](https://github.com/dakrone/clojure-opennlp)
  * [postagga](https://github.com/turbopape/postagga)
  * [beagle](https://github.com/tokenmill/beagle)
  * [lmgrep](https://github.com/dainiusjocas/lucene-grep)

## 解析

  * [Instaparse](https://github.com/Engelberg/instaparse)
  * [kern](https://github.com/blancas/kern)
  * [duckling](https://github.com/wit-ai/duckling)
  * [buran](https://github.com/alekseysotnikov/buran) - RSS/Atom feed 消费者和生产者
  
## 异常和错误处理
  * [Ex](https://github.com/mpenet/ex)
  * [Perseverance](https://github.com/grammarly/perseverance)
  * [Dire](https://github.com/MichaelDrogalis/dire)

## 基于规则的编程
  * [奥多伊尔规则](https://github.com/oakes/odoyle-rules)
  * [克拉拉规则](https://github.com/cerner/clara-rules)
  * [Arete](https://github.com/yipeeio/arete)

## 编辑器插件

  * [卡尔瓦 (VSCode)](https://github.com/BetterThanTomorrow/calva)
  * [clojure-lsp（多个编辑器）](https://github.com/clojure-lsp/clojure-lsp)
  * [苹果酒 (Emacs)](https://github.com/clojure-emacs/cider)
  * [智能父母 (Emacs)](https://github.com/Fuco1/smartparens)
  * [彩虹分隔符 (Emacs)](https://github.com/Fanael/rainbow-delimiters)
  * [激进缩进 (Emacs)](https://github.com/Malabarba/aggressive-indent-mode)
  * [召唤 (Neovim)](https://github.com/Olical/conjure)
  * [vim-cljfmt (Vim)](https://github.com/venantius/vim-cljfmt)
  * [vim-伊斯特伍德 (Vim)](https://github.com/venantius/vim-eastwood)
  * [vim-壁炉 (Vim)](https://github.com/tpope/vim-fireplace)
  * [vim-redl (Vim)](https://github.com/dgrnbrg/vim-redl)
  * [vim-leiningen (Vim)](https://github.com/tpope/vim-salve)
  * [Rainbow_parentheses.vim (Vim)](https://github.com/junegunn/rainbow_parentheses.vim)
  * [vim-iced (Vim)](https://github.com/liquidz/vim-iced)
  * [草书（IntelliJ）](https://cursive-ide.com/)
  * [原始复制（Atom）](https://atom.io/packages/proto-repl)
  * [Parinfer（多名编辑）](http://shaunlebron.github.io/parinfer/)
  * [括号对着色器 (VSCode)](https://marketplace.visualstudio.com/items?itemName=CoenraadS.bracket-pair-colorizer)
  * [clojureVSCode（VSCode）](https://github.com/avli/clojureVSCode)
* [Notepad++](https://github.com/linpeng Cheng/ClojureBoxNpp): 修改Lisp的配置文件

## 文档

*用于（非 LP）代码和项目文档的实用程序和库*

 * [codox](https://github.com/weavejester/codox)

## 文学编程

  * [marginalia](https://github.com/gdeer81/marginalia)
  * [klipse](https://github.com/viebel/klipse)
  * [blackfog](https://github.com/neromous/blackfog.dsl)

## 档案和压缩

  * [swindon（java.util.zip 包装器）](https://github.com/AeroNotix/swindon)

## 杂项

 * [potemkin](https://github.com/ztellman/potemkin) - 在另一个 ns 中重新导出变量/就像 clojure 映射一样
 * [clj-tuple](https://github.com/ztellman/clj-tuple)
 * [slingshot](https://github.com/scgilardi/slingshot)
 * [virgil](https://github.com/ztellman/virgil)
 * [javastar](https://github.com/tailrecursion/javastar)
 * [riddley](https://github.com/ztellman/riddley)
 * [kezban](https://github.com/ertugrulcetin/kezban)
 * [clj-grpc](https://github.com/otwieracz/clj-grpc)

## 调试

  * [flow-storm-debugger](https://github.com/flow-storm/flow-storm-debugger)
  * [playback](https://github.com/gnl/playback)
  * [tools.trace](https://github.com/clojure/tools.trace)
  * [debugger](https://github.com/razum2um/clj-debugger)
  * [debug-repl](https://github.com/GeorgeJahad/debug-repl)
  * [ritz](https://github.com/pallet/ritz)
  * [redl](https://github.com/dgrnbrg/redl)
  * [limit-break](https://github.com/technomancy/limit-break)
  * [spyscope](https://github.com/dgrnbrg/spyscope)
  * [aprint](https://github.com/razum2um/aprint)
  * [packed-printer](https://github.com/cgrand/packed-printer)
  * [pretty](https://github.com/AvisoNovate/pretty)
  * [prone](https://github.com/magnars/prone)
  * [figwheel](https://github.com/bhauman/lein-figwheel)
  * [ultra](https://github.com/venantius/ultra)
  * [mate-clj](https://github.com/AppsFlyer/mate-clj)
  * [scope-capture](https://github.com/vvvvalvalval/scope-capture)

## CI

  * [lambdacd](https://github.com/flosell/lambdacd)
  
## 项目管理
  
  * [milestones](https://github.com/turbopape/milestones)

## 终端用户界面

  * [clojure-lanterna](https://github.com/MultiMUD/clojure-lanterna)
  * [triki](https://github.com/lambdaisland/trikl)
  * [zaffre](https://github.com/aaron-santos/zaffre)
  * [closh](https://github.com/dundalek/closh)
  * [piotr-yuxuan/malli-cli](https://github.com/piotr-yuxuan/malli-cli)
  
## 图形可视化

  * [zipper-viz](https://github.com/lambdaisland/zipper-viz)
  * [dorothy](https://github.com/daveray/dorothy)
  * [viz.cljc](https://github.com/jebberjeb/viz.cljc)
  * [fsmviz](https://github.com/jebberjeb/fsmviz)
  * [rhizome](https://github.com/ztellman/rhizome)
  * [re-frame-flow](https://github.com/ertugrulcetin/re-frame-flow) - 基于图形的可视化工具，用于重新构建事件链 (ClojureScript)

## 游戏开发
  * [jme-clj](https://github.com/ertugrulcetin/jme-clj) - Clojure 3D 游戏引擎（包装器），由 jMonkeyEngine 提供支持
  * [play-cljc](https://github.com/oakes/play-cljc) - Clojure 和 ClojureScript 游戏库

## 指南

  * [Clojure 风格指南](https://github.com/bbatsov/clojure-style-guide)
  * [Clojure 蒸馏](http://yogthos.github.io/ClojureDistilled.html)
  * [clojure-cookbook](https://github.com/clojure-cookbook/clojure-cookbook)
  * [Clojure 初学者简要指南](http://www.unexpected-vortices.com/clojure/brief-beginners-guide/index.html)
  * [Clojure 为勇敢而真实的人服务](http://www.braveclojure.com/)
  * [Clojure 从头开始](https://aphyr.com/tags/Clojure-from-the-ground-up)
  * [错误信息目录](https://github.com/yogthos/clojure-error-message-catalog)
  * [Clojure 示例](https://kimh.github.io/clojure-by-example/)

## 视频教程

### YouTube

* [Misophistful 的频道](https://www.youtube.com/user/Misophistful/videos)：了解列表理解、线程宏、生成测试、解构、core.match 等概念，以及 Light Table、Datomic 和使用 Clojure 进行游戏开发的介绍
* [Fred Overflow 的频道](https://www.youtube.com/channel/UC9m7D4XKPJqTPCLSBym3BCg/search?query=Clojure)：Clojure 函数式编程和 TDD 简介
* [Clojure Pills 截屏视频](https://www.youtube.com/channel/UCH0CkLvbv6yEyrUnw9qujpQ/videos)：一次介绍 Clojure 的一个功能
* [Clojure Pills 截屏视频](https://www.youtube.com/c/onthecodeagain/videos)：与整个 clojure 生态系统相关的有趣且适合初学者的内容
  * [使用 Postgres、Clojure 和 JDBC 进行数据持久化](https://www.youtube.com/channel/UCrwwOZ4h2FQhAdTMfjyQfQA/playlists)
* [Timothy Baldridge 的 Clojure 教程](https://www.youtube.com/channel/UC6yONKYeoE2P3bsahDtsimg/videos)：有关 core.async、传感器、瞬态、逻辑编程和“每日函数”系列的更多高级视频。

## 网站

  * [Clojure](http://clojure.org/)
  * [Clojure 松弛](http://clojurians.net/)
  * [clojuredocs](http://clojuredocs.org)
  * [clojure-doc](http://clojure-doc.org/)
  * [Clojure 工具箱](http://www.clojure-toolbox.com/)
  * [ZEEF/Clojure](https://clojure.zeef.com/vlad.bokov)
  * [Clojure 土地](https://clojure.land)

## 推特

  * [oss_clj](https://twitter.com/oss_clj)

## 练习

  * [rich4clojure](https://github.com/PEZ/rich4clojure)
  * [仙境 Clojure Katas](https://github.com/gigasquid/wonderland-clojure-katas)
  * [Clojure 公案](http://clojurekoans.com)
  * [exercism.io](http://exercism.io/languages/clojure)
  * [Codewars](https://www.codewars.com/kata/search/clojure)
