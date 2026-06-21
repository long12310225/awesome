# 很棒的 Erlang [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
受 [awesome-elixir](https://github.com/h4cc/awesome-elixir) 启发的令人惊叹的 Erlang 库、资源和闪亮事物的精选列表。

- [很棒的 Erlang](#awesome-Erlang)
    - [包管理](#package-management)
    - [发布管理](#release-management)
    - [配置管理](#configuration-management)
    - [代码库维护](#codebase-maintenance)
    - [网络框架](#web-frameworks)
    - [Web 框架组件](#web-framework-components)
    - [HTTP](#http)
    - [Testing](#testing)
    - [Logging](#logging)
    - [Monitoring](#monitoring)
    - [Deployment](#deployment)
    - [分布式系统](#distributed-systems)
    - [代码分析](#code-analysis)
    - [构建工具](#build-tools)
    - [Geolocation](#geolocation)
    - [Debugging](#debugging)
    - [Actors](#actors)
    - [日期和时间](#date-and-time)
    - [ORM 和数据映射](#orm-and-datamapping)
    - [Queue](#queue)
    - [Authentication](#authentication)
    - [文字和数字](#text-and-numbers)
    - [休息和API](#rest-and-api)
    - [Caching](#caching)
    - [第三方API](#third-party-apis)
    - [Networking](#networking)
    - [物联网](#internet-of-things)
    - [算法和数据结构](#algorithms-and-datastructures)
    - [翻译和国际化](#translations-and-internationalizations)
    - [Miscellaneous](#miscellaneous)
- [Resources](#resources)
    - [Websites](#websites)
    - [Books](#books)
    - [网络阅读](#web-reading)
    - [二郎阅读](#Erlang-reading)
    - [Screencasts](#screencasts)
- [其他很棒的清单](#other-awesome-lists)
- [Contributing](#contributing)

## 包管理
*用于包和依赖管理的库和工具。*

* [hex.pm](https://hex.pm/) - Erlang 生态系统的包管理器。

## 发布管理
*用于发布管理的库和工具。*

* [relx](https://github.com/erlware/relx) - Erlang 的发布汇编程序。

## 配置管理
*与配置管理相关的库和工具。*

* [stillir](https://github.com/heroku/stillir) - 将环境变量缓存为 Erlang 应用程序变量。

## 代码库维护
*维护干净代码库的库和工具。*

* [elvis](https://github.com/inaka/elvis) - Erlang 风格审阅者。

## 网络框架
*网络开发框架。*

* [Axiom](https://github.com/tsujigiri/axiom) - 一个微框架，灵感来自 Ruby 的 [Sinatra](https://github.com/sinatra/sinatra)。
* [ChicagoBoss](https://github.com/ChicagoBoss/ChicagoBoss) - 受 Rails 启发并用 Erlang 编写的服务器框架。
* [cowboy](https://github.com/ninenines/cowboy) - 一个简单的 HTTP 服务器。
* [Giallo](https://github.com/kivra/giallo) - 一个基于 [Cowboy](https://github.com/ninenines/cowboy) 的小型灵活的 Web 框架。
* [MochiWeb](https://github.com/mochi/mochiweb) - 用于构建轻量级 HTTP 服务器的 Erlang 库。
* [N2O](https://github.com/synrc/n2o) - WebSocket 应用服务器。
* [Nitrogen](https://github.com/nitrogen/nitrogen) - 在纯 Erlang 中构建 Web 应用程序（包括前端）的框架。
* [Zotonic](https://github.com/zotonic/zotonic) - 高速、实时的网络框架和内容管理系统。

## Web 框架组件
*来自 Web 开发框架的独立组件。*

* [cb_admin](https://github.com/ChicagoBoss/cb_admin) - 芝加哥老板的管理界面。
* [cb_websocket_controller](https://github.com/dkuhlman/cb_websocket_controller) - 用于为 ChicagoBoss 实现 Websocket 控制器的模板。
* [giallo_session](https://github.com/kivra/giallo_session) - Giallo Web 框架的会话管理库。
* [simple_bridge](https://github.com/nitrogen/simple_bridge) - 一个抽象层，为流行的 Erlang Web 服务器（Cowboy、Inets、Mochiweb、Webmachine 和 Yaws）提供统一的接口。

## HTTP协议
*用于处理 HTTP 和抓取网站的库。*

* [bullet](https://github.com/ninenines/bullet) - 简单、可靠、高效的 Cowboy 流媒体。
* [gun](https://github.com/ninenines/gun) - Erlang HTTP 客户端支持 HTTP/1.1、SPDY 和 Websocket。
* [hackney](https://github.com/benoitc/hackney) - Erlang 中的简单 HTTP 客户端。
* [ibrowse](https://github.com/cmullaparthi/ibrowse) - Erlang HTTP 客户端。
* [lhttpc](https://github.com/esl/lhttpc) - 在 Erlang 中实现的轻量级 HTTP/1.1 客户端。
* [shotgun](https://github.com/inaka/shotgun) - 现在你需要的不仅仅是一把枪。

## 测试
*用于测试代码库和生成测试数据的库。*

* [PropEr](https://github.com/manopapad/proper) - 一个受 QuickCheck 启发的 Erlang 基于属性的测试工具。
* [tracerl](https://github.com/esl/tracerl) - Erlang/OTP 的动态跟踪测试和实用程序

## 记录
*用于生成和使用日志文件的库。*

* [lager](https://github.com/basho/lager) - Erlang/OTP 的日志框架。
* [lager_amqp_backend](https://github.com/jbrisbin/lager_amqp_backend) - AMQP RabbitMQ Lager 后端。
* [lager_hipchat](https://github.com/synlay/lager_hipchat) - HipChat 啤酒后端。
* [lager_loggly](https://github.com/kivra/lager_loggly) - Loggly 啤酒后端。
* [lager_smtp](https://github.com/blinkov/lager_smtp) - 啤酒的 SMTP 后端。
* [lager_slack](https://github.com/furmanOFF/lager_slack) - 啤酒的简单 Slack 后端。
* [logplex](https://github.com/heroku/logplex) - Heroku 日志路由器。

## 监控
*用于收集指标和监控的库。*

* [entop](https://github.com/mazenharake/entop) - 一个类似top的Erlang节点监控工具。
* [eper](https://github.com/massemanet/eper) - Erlang 性能相关工具的松散集合。
* [Exometer](https://github.com/Feuerlabs/exometer) - 一个 Erlang 仪器包。
* [folsom](https://github.com/boundary/folsom) - 受 Coda Hale 的 [metrics](https://github.com/codahale/metrics) 启发的基于 Erlang 的指标系统。
* [statsderl](https://github.com/lpgauth/statsderl) - 一个 statsd Erlang 客户端。
* [vmstats](https://github.com/ferd/vmstats) - 微型 Erlang 应用程序与 statsderl 结合使用，以便在 Erlang VM 上生成石墨日志的信息。

## 部署
*与 Erlang/OTP 应用程序部署相关的库和工具。*

* [docker-erlang](https://github.com/synlay/docker-erlang) - Erlang/OTP 的基本 Docker 容器镜像。

## 分布式系统
*跨微服务进行压力/负载测试、延迟问题等的工具。*

 * [Typhoon](https://github.com/fogfish/typhoon) - 适用于分布式系统的压力和负载测试工具，可模拟从测试集群到被测系统 (SUT) 的流量并可视化相关延迟。
## 代码分析
*用于分析、解析和操作代码库的库和工具。*

* [Concuerror](https://github.com/parapluu/Concuerror) - Concuerror是一个针对并发Erlang程序的系统测试工具。
* [eflame](https://github.com/proger/eflame) - Erlang 的火焰图分析器。
* [geas](https://github.com/crownedgrouse/geas) - Geas 是一个工具，它将检测您的项目的可运行官方 Erlang 发布窗口，包括其依赖项，并提供许多有用的信息。

## 构建工具
*项目构建和自动化工具。*

* [rebar](https://github.com/rebar/rebar) - Erlang 构建工具可以轻松编译和测试 Erlang 应用程序、端口驱动程序和版本。
* [rebar3](https://github.com/rebar/rebar3) - Erlang 的构建工具，可以管理来自 [Hex.pm](https://hex.pm/) 的 Erlang 包。如需了解更多信息，请访问 [rebar3.org](https://www.rebar3.org/)
* [sync](https://github.com/rustyio/sync) - Erlang 的即时重新编译。

## 地理定位
*用于对地址进行地理编码并处理纬度和经度的库。*

* [erl-rstar](https://github.com/armon/erl-rstar) - R* 树空间数据结构的 Erlang 实现。
* [GeoCouch](https://github.com/couchbase/geocouch) - Couchbase 和 Apache CouchDB 的空间扩展。
* [Teles](https://github.com/armon/teles) - 用于操作地理数据的 Erlang 网络服务。

## 调试
*用于调试代码和应用程序的库和工具。*

* [tx](https://github.com/kvakvs/tx) - HTML Erlang 术语查看器启动自己的网络服务器并显示您从 Erlang 节点提供的任何术语。

## 演员
*用于与演员等合作的库和工具。*

* [poolboy](https://github.com/devinus/poolboy) - 一个帅气的 Erlang 工人池工厂。

## 日期和时间
*用于处理日期和时间的库。*

* [erlang_localtime](https://github.com/dmitryme/erlang_localtime) - 用于从一个本地时间转换为另一个本地时间的 Erlang 库。
* [qdate](https://github.com/choptastic/qdate) - Erlang 日期、时间和时区管理：格式化、转换和日期算术。

## ORM 和数据映射
*实现对象关系映射或数据映射技术的库。*

* [boss_db](https://github.com/ErlyORM/boss_db) - Erlang 的分片、缓存、池化、事件 ORM。
* [epgsql](https://github.com/epgsql/epgsql) - Erlang 的 PostgreSQL 驱动程序。
* [mysql-otp](https://github.com/mysql-otp/mysql-otp) - MySQL/OTP – 适用于 Erlang/OTP 的 MySQL 驱动程序。
* [pgsql_migration](https://github.com/artemeff/pgsql_migration) - Erlang 的 PostgreSQL 迁移。

## 队列
*用于处理事件和任务队列的库。*

* [dq](https://github.com/darach/dq) - 分布式容错队列库。
* [ebqueue](https://github.com/rgrinberg/ebqueue) - Erlang 中的小型简单阻塞队列。
* [pqueue](https://github.com/okeuday/pqueue) - Erlang 优先级队列。
* [tinymq](https://github.com/ChicagoBoss/tinymq) - Erlang 的小型内存消息队列。

## 认证
*用于实现身份验证方案的库。*

* [oauth2](https://github.com/kivra/oauth2) - Erlang Oauth2 实现。

## 文字和数字
*用于解析和操作文本和数字的库。*

* [ejsv](https://github.com/patternmatched/ejsv) - Erlang JSON 模式验证器。
* [eql](https://github.com/artemeff/eql) - Erlang 是否带有 SQL。
* [jiffy](https://github.com/davisp/jiffy) - Erlang 的 JSON NIF。
* [jsx](https://github.com/talentdeficit/jsx) - 一个用于消费、生成和操作 json 的 erlang 应用程序。
* [miffy](https://github.com/expelledboy/miffy) - Jiffy 包装器返回漂亮的地图。
* [qsp](https://github.com/artemeff/qsp) - 增强的 Erlang 查询字符串解析器。
* [rec2json](https://github.com/lordnull/rec2json) - 从记录规范生成 JSON 编码器/解码器。

## 休息和API
*用于开发 REST-ful API 的库和 Web 工具。*

* [leptus](https://github.com/s1n4/leptus) - Leptus 是一个运行在牛仔之上的 Erlang REST 框架。
* [rooster](https://github.com/FelipeBB/rooster) - Rooster 是一个运行在 mochiweb 之上的轻量级 REST 框架。

## 缓存
*用于缓存数据的库。*

* [cache](https://github.com/fogfish/cache) - 内存分段缓存

## 第三方API
*用于访问第三方 API 的库。*

* [google-token-erlang](https://github.com/ruel/google-token-erlang) - Erlang 的 Google ID 令牌验证器。
* [restc](https://github.com/kivra/restclient) - Erlang REST 客户端
* [oauth2c](https://github.com/kivra/oauth2_client) - Erlang oAuth 2 客户端（使用restc）

## 网络
*用于使用网络相关内容的库和工具。*

* [barrel_tcp](https://github.com/benoitc-attic/barrel_tcp) - barrel_tcp 是 Erlang 中低延迟的通用 TCP 接受器池。
* [gen_rpc](https://github.com/priestjim/gen_rpc) - 用于基于 Erlang-VM 的语言的可扩展 RPC 库。
* [gen_tcp_server](https://github.com/rpt/gen_tcp_server) - 该库采用 gen_server 的概念并引入了用于操作 TCP 服务器的相同机制。
* [gossiperl](https://github.com/gossiperl/gossiperl) - 用 Erlang 编写的与语言无关的八卦中间件和消息总线。
* [nat_upnp](https://github.com/benoitc/nat_upnp) - Erlang 库使用 UNP IGD 将内部端口映射到外部端口。
* [ranch](https://github.com/ninenines/ranch) - TCP 协议的套接字接受器池。

## 物联网
*用于与物理世界交互的库和工具。*

* [GRiSP](https://grisp.org/) - 使用名为 RTEMS 的小型实时 unikernel 在具有许多硬件接口和低级驱动程序的 IoT 板上运行 Erlang VM
* [lemma_erlang](https://github.com/noam-io/lemma_erlang) - IDEO 的 Noam 物联网原型平台的引理。

## 算法和数据结构
*算法和数据结构的库和实现。*

* [datum](https://github.com/fogfish/datum) - Erlang 的纯函数式泛型编程
* [erlando](https://github.com/travelping/erlando) - 一组语法扩展，例如 Erlang 的柯里化和 monad。
* [statebox](https://github.com/mochi/statebox) - Erlang 状态“monad”具有合并/冲突解决功能。
* [riak_dt](https://github.com/basho/riak_dt) - 基于状态的 CRDT 的 Erlang 库。

## 翻译和国际化
*提供翻译或国际化的图书馆。*

## 杂项
*不属于上述类别的有用库或工具。*

* [erlang-history](https://github.com/ferd/erlang-history) - 将 shell 历史记录添加到 Erlang 的 shell 中的技巧。
* [erld](https://github.com/ShoreTel-Inc/erld) - erld 是一个小程序，旨在解决将 Erlang 程序作为 UNIX 守护进程运行的问题。

# 资源
用于提高您的 Erlang 开发技能和知识的各种资源，例如书籍、网站和文章。

## 网站
*有用的网络和 Erlang 相关网站和新闻通讯。*

* [Erlang Bookmarks](https://github.com/0xAX/erlang-bookmarks/wiki/Erlang-bookmarks) - 关于 erlang 编程语言的所有内容 [由社区提供支持]。
* [Erlang Central](https://erlangcentral.org/) - 很棒的 erlang 资源集合以及用于讨论和寻求帮助的实时社区聊天。
* [Planet Erlang](http://www.planeterlang.com/) - Planet 站点/博客文章的 RSS 源，涵盖整个 Erlang 生态系统的主题。
* [Spawned Shelter](http://spawnedshelter.com/) - Erlang 生成的庇护所。与 Erlang 相关的最佳文章、视频和演示文稿的集合。

## 书籍
*精彩的书籍和电子书。*

* [Erlang and Elixir for Imperative Programmers](https://leanpub.com/erlangandelixirforimperativeprogrammers) - Wolfgang Loder 在函数概念背景下介绍 Erlang 和 Elixir (2016)
* [Learn You Some Erlang](http://learnyousomeerlang.com/) - 学点 Erlang——大有裨益！非常全面的资源，涵盖从 Erlang 编程入门到大规模开发和部署的所有内容。
* [Stuff Goes Bad - ERLANG IN ANGER](http://www.erlang-in-anger.com/) - 本书旨在成为一个关于如何在战争时期成为 Erlang 军医的小指南。

## 网络阅读
*与网络开发相关的一般阅读材料。*

## 二郎阅读
*Erlang相关阅读材料。*

* [The Joy of Erlang; Or, How To Ride A Toruk](http://www.evanmiller.org/joy-of-erlang.html) - Erlang 的乐趣；或者，How To Ride A Toruk 对 Erlang 的快速介绍，通过几个示例项目来教授该语言。

## 截屏视频
*很酷的视频教程。*

# 贡献
有关详细信息，请参阅[贡献](https://github.com/drobakowski/awesome-erlang/blob/master/CONTRIBUTING.md)。
