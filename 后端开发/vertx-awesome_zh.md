# 很棒的 Ver.x [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

[<img src=“vertx-logo.svg”align=“right”width=“250”alt=“Vert.x 徽标”>](http://vertx.io)

*Awesome Vert.x* 是与以下相关的很棒的框架、库或其他组件的列表
[Vert.x](https://github.com/eclipse/vert.x)。

如果您希望您的组件出现在此处，请向此存储库发送拉取请求以添加它。

请注意，我们无法保证此列表中所有内容的稳定性或生产价值，除非它具有
图标 <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px">
在它旁边。该图标表示该组件是官方的一部分
[Vert.x 堆栈](https://vertx.io/docs/)。

## 内容

* [Books](#books)
* [构建工具](#build-tools)
* [网络框架](#web-frameworks)
* [认证授权](#authentication-authorisation)
* [数据库客户端](#database-clients)
* [Integration](#integration)
* [Middleware](#middleware)
* [语言支持](#language-support)
* [Reactive](#reactive)
* [同步线程非阻塞](#sync-thread-non-block)
* [Vert.x 事件总线客户端](#vertx-event-bus-clients)
* [Vert.x 事件总线扩展](#vertx-event-bus-extensions)
* [集群管理器](#cluster-managers)
* [云支持](#cloud-support)
* [Microservices](#microservices)
* [游戏开发](#game-development)
* [搜索引擎](#search-engines)
* [服务工厂](#service-factory)
* [Config](#config)
* [依赖注入](#dependency-injection)
* [Testing](#testing)
* [开发工具](#development-tools)
* [Miscellaneous](#miscellaneous)
* [Distribution](#distribution)
* [Examples](#examples)
* [Deployment](#deployment)
* [Utilities](#utilities)
* [Articles](#articles)
* [Front-End](#front-end)

## 书籍

* [用 Java 构建反应式微服务](https://www.oreilly.com/library/view/building-reactive-microservices/9781491986295/) 作者：Clément Escoffier
* [Vert.x 实践](https://www.manning.com/books/vertx-in-action) 作者：Julien Ponge

## 构建工具

* [Vert.x Maven 插件](https://github.com/reactiverse/vertx-maven-plugin)
* [Vert.x Gradle 插件](https://plugins.gradle.org/plugin/io.vertx.vertx-plugin)
* [Vert.x Codegen Gradle plugin](https://github.com/bulivlad/vertx-codegen-plugin) - 一个 Gradle 插件，可促进 Vert.x Java 项目的代码生成使用。

## 网络框架

* [Vert.x Web](https://github.com/vert-x3/vertx-web) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - 适用于 Vert.x 的全功能 Web 工具包。
* [Vert.x Jersey](https://github.com/englishtown/vertx-jersey) - 在 Vert.x 中创建 JAX-RS [Jersey](https://eclipse-ee4j.github.io/jersey/) 资源。
* [Kovert](https://github.com/kohesive/kovert) - Kotlin + Vert.x Web 的隐形 REST 框架。
* [Handlers](https://github.com/spriet2000/vertx-handlers-http) - Vert.x 的开放 Web 框架。
* [QBit](https://github.com/advantageous/qbit) - REST 和 WebSocket 方法调用封送和反应式库。
* [vertx-rest-storage](https://github.com/swisspush/vertx-rest-storage) - 文件系统或 Redis 数据库中 REST 资源的持久性。
* [Jubilee](https://github.com/isaiah/jubilee) - 基于 Vert.x 3 构建的机架兼容 Ruby HTTP 服务器。
* [Knot.x](https://github.com/Cognifide/knotx) - 高效、高性能的集成平台，适用于基于 Vert.x 3 构建的现代网站。
* [Irked](https://github.com/GreenfieldTech/irked) - Vert.x Web 基于注释的配置，具有控制器框架和用于 REST 的富有表现力的 API。
* [REST.VertX](https://github.com/zandero/rest.vertx) - 适用于 Vert.x 垂直领域的轻量级 JAX-RS (RestEasy) 类注释处理器。
* [Atmosphere Vert.x](https://github.com/Atmosphere/atmosphere-vertx) - 适用于 JVM 的实时客户端服务器框架，支持 WebSocket 和具有跨浏览器回退功能的服务器发送事件。
* [Vert.x Vaadin](https://github.com/mcollovati/vertx-vaadin) - 在 Vert.x 上运行 Vaadin 应用程序。
* [Serverx](https://github.com/lukehutch/serverx) - 允许您仅使用路由处理程序注释快速轻松地设置 Vert.x 支持的服务器。
* [Cloudopt Next](https://github.com/cloudoptlab/cloudopt-next) - Cloudopt Next 是一个非常轻量级、现代的、基于 JVM 的全栈 kotlin 框架，旨在构建模块化、易于测试的 JVM 应用程序，支持 Java、Kotlin 语言，由最好的 Java 库和标准精心打造。
* [Donkey](https://github.com/AppsFlyer/donkey) - 现代 Clojure HTTP 服务器和客户端是为了易于使用和提高性能而构建的。
* [SCX](https://github.com/scx567888/scx) - 一个开放且易于使用的Web框架，大部分功能都是基于注解的。
* [vertx-rest](https://github.com/dream11/vertx-rest) - 对 Resteasy-vertx 进行抽象，以简化基于 JAX-RS 注释的 Vert.x REST 应用程序的编写。

## 认证授权

* [Vert.x Auth SQL](https://github.com/eclipse-vertx/vertx-auth) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - 基于 Vert.x SQL 客户端和关系数据库的 Vert.x 身份验证/授权。
* [Vert.x Auth JWT](https://github.com/eclipse-vertx/vertx-auth/tree/master/vertx-auth-jwt) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - 基于 JSON Web 令牌的 Vert.x 授权。
* [Vert.x Auth htdigest](https://github.com/eclipse-vertx/vertx-auth/tree/master/vertx-auth-htdigest) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - 基于 [Apache] 的 Vert.x 授权/身份验证htdigest](https://httpd.apache.org/docs/2.4/programs/htdigest.html)。
* [Vert.x Auth Mongo](https://github.com/vert-x3/vertx-auth/tree/master/vertx-auth-mongo) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - 基于 [MongoDB](https://www.mongodb.com/) 的 Vert.x 授权/身份验证。
* [Vert.x Auth OAuth2](https://github.com/eclipse-vertx/vertx-auth/tree/master/vertx-auth-oauth2) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - 基于 [OAuth 2](https://oauth.net/2/) 的 Vert.x 授权/身份验证。
* [Vert.x Auth htpasswd](https://github.com/eclipse-vertx/vertx-auth/tree/master/vertx-auth-htpasswd) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - 基于 Vert.x 授权/身份验证[htpasswd](https://httpd.apache.org/docs/2.4/programs/htpasswd.html)。

* [Vert.x-Pac4j](https://github.com/pac4j/vertx-pac4j) - Vert.x 身份验证/授权使用 [pac4j](http://www.pac4j.org/) 实现。

## 数据库客户端

*用于连接数据库的客户端*

* 关系数据库
* [反应式 SQL 客户端](https://github.com/eclipse-vertx/vertx-sql-client) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - 高性能反应式 SQL 客户端。
* [JDBC](https://github.com/vert-x3/vertx-jdbc-client) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - 围绕 JDBC 数据源的异步接口。
* [MySQL / PostgreSQL](https://github.com/vert-x3/vertx-mysql-postgresql-client) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - MySQL/PostgreSQL 异步客户端。
  * [PostgreSQL](https://github.com/vietj/reactive-pg-client) - 反应式 PostgreSQL 客户端。
  * [database](https://github.com/susom/database) - 适用于 Oracle、PostgreSQL、SQL Server、HyperSQL 等的客户端，专为安全性、正确性和易用性而设计。
  * [jOOQ](https://github.com/jklingsporn/vertx-jooq) - 使用 jOOQ 执行类型安全、异步 SQL 并生成代码。
  * [jOOQx](https://github.com/zero88/jooqx) - 利用“jOOQ DSL”中类型安全 SQL 的强大功能，并使用 Vert.x 中的反应式非阻塞 SQL 驱动程序。
  * [Exposed Vert.x SQL Client](https://github.com/huanshankeji/exposed-vertx-sql-client) - Kotlin 的 [Exposed](https://github.com/JetBrains/Exposed) 位于 [Vert.x Reactive SQL Client](https://github.com/eclipse-vertx/vertx-sql-client) 之上。

* NoSQL 数据库
* [MongoDB](https://github.com/vert-x3/vertx-mongo-client) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - 用于与 MongoDB 数据库交互的异步客户端。
* [Redis](https://github.com/vert-x3/vertx-redis-client) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - 与 Redis 交互的异步 API。
* [Cassandra](https://github.com/vert-x3/vertx-cassandra-client) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - 允许应用程序与 Cassandra 服务交互的 Vert.x 客户端。
  * [Cassandra](https://github.com/englishtown/vertx-cassandra) - 用于与 Cassandra 和 Cassandra 映射交互的异步 API。
  * [Neo4j Java Driver Vert.x](https://github.com/romanbsd/neo4j-java-driver-vertx) - Neo4j Java 驱动程序的 Vert.x 包装器。
  * [OrientDB](https://github.com/cstamas/vertx-orientdb) - 非阻塞 OrientDB 服务器集成。
  * [Bitsy](https://github.com/cstamas/vertx-bitsy) - 非阻塞 Bitsy Graph 服务器集成。
  * [MarkLogic](https://github.com/etourdot/vertx-marklogic) - Marklogic 数据库服务器的异步客户端。
  * [SirixDB](https://github.com/sirixdb/sirix/tree/master/bundles/sirix-rest-api) - 非阻塞 SirixDB HTTP 服务器。
  * [DGraph](https://github.com/aesteve/vertx-dgraph-client) - 有关如何构建 Vert.x gRPC 兼容客户端的示例。这里针对 [dgraph](https://docs.dgraph.io)
  * [RxFirestore](https://github.com/pjgg/rxfirestore) - 以反应式方式编写的非阻塞 Firestore SDK。
  * [MongoDB](https://github.com/imrafaelmerino/vertx-mongo-effect) - 基于 [Vert.x Effect](https://github.com/imrafaelmerino/vertx-mongo-effect) 的纯函数式和反应式 MongoDB 客户端。完全支持重试、回退和恢复操作。
  * [Aerospike](https://github.com/dream11/vertx-aerospike-client) - 用于与 Aerospike 服务器交互的异步和非阻塞 API。在内部使用 [AerospikeClient's](https://github.com/aerospike/aerospike-client-java) 异步命令并处理 Vert.x 上下文上的结果。

* [vertx-pojo-mapper](https://github.com/BraintagsGmbH/vertx-pojo-mapper) - MySQL 和 MongoDB 的非阻塞 POJO 映射。
* [vertx-mysql-binlog-client](https://github.com/guoyu511/vertx-mysql-binlog-client) - 用于利用 MySQL 复制流的 Vert.x 客户端。

## 整合

* 服务器发送的事件
  * [jEaSSE](https://github.com/mariomac/jeasse) - Java 简单 SSE。 SSE 的简单、轻量级实现。
  * [vertx-sse](https://github.com/aesteve/vertx-sse) - Vert.x SSE 实现 + 事件总线 SSE 桥。

* 邮件
* [SMTP](https://github.com/vert-x3/vertx-mail-client) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - 异步 SMTP 客户端。

* 休息
  * [Retrofit adapter for Vert.x](https://github.com/vietj/retrofit-vertx) - 用于使用 Vert.x 进行 Retrofit 的高度可扩展的适配器。
  * [openapi4j adapter for Vert.x](https://github.com/openapi4j/openapi4j/tree/master/openapi-operation-adapters/openapi-operation-vertx) - OpenAPI 3 请求验证器和路由器工厂替代方案。
  * [Vert.x Effect HTTP client](https://github.com/imrafaelmerino/vertx-effect) - 使用 [Vert.x Effect](https://github.com/imrafaelmerino/vertx-effect) 的纯函数式和反应式 HTTP 客户端，具有 OAuth 支持以及重试、回退和恢复操作。

* 文件服务器
  * [Vert.x TFTP Client](https://github.com/OneManCrew/vertx-tftp-client) - Vert.x 的 TFTP 客户端支持下载/上传文件。
* 消息传递
* [AMQP 1.0](https://github.com/vert-x3/vertx-amqp-bridge) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - 使用 Vert.x 生产者和消费者 API 与 AMQP 1.0 服务器交互。
* [MQTT](https://github.com/vert-x3/vertx-mqtt) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - 提供两个不同的组件：一个 MQTT 服务器，用于处理所有 MQTT 通信以及与客户端的消息交换；一个 MQTT 客户端，用于向 MQTT 代理发送和接收消息。
* [RabbitMQ](https://github.com/vert-x3/vertx-rabbitmq-client) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - RabbitMQ 客户端 (AMQP 0.9.1)。
* [Kafka 客户端](https://github.com/vert-x3/vertx-kafka-client) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - Kafka 客户端。
  * [kafka](https://github.com/cyngn/vertx-kafka) - 用于消费和生成消息的 Kafka 客户端。
* [STOMP](https://github.com/vert-x3/vertx-stomp) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - Kafka 客户端和服务器。
  * [ZeroMQ](https://github.com/dano/vertx-zeromq) - ZeroMQ 事件总线桥。
  * [Azure ServiceBus](https://github.com/TextBack/vertx-azure-servicebus) - Azure [ServiceBus](https://azure.microsoft.com/en-us/products/service-bus/) 生产者和消费者（完全异步，不使用 Microsoft Azure SDK）。
  * [AMQP 1.0 - Kafka bridge](https://github.com/rhiot/amqp-kafka-bridge) - 用于使用 AMQP 1.0 协议向 Apache Kafka 发送消息/从 Apache Kafka 接收消息的桥接器。
* [Vert.x Kafka 客户端](https://github.com/vert-x3/vertx-kafka-client) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - Apache Kafka 客户端，用于从 Apache Kafka 集群读取消息并向其发送消息。
  * [The White Rabbit](https://github.com/viartemev/the-white-rabbit) - 基于 Kotlin 协程的异步 RabbitMQ (AMQP) 客户端。
  * [WAMP Broker](https://github.com/i22-digitalagentur/vertx-wamp) - 您可以将 WAMP 代理嵌入到 Vert.x 应用程序中。

* JavaEE
* [JCA 适配器](https://github.com/vert-x3/vertx-jca) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - 用于 Vert.x 事件总线的 Java 连接器架构适配器。
  * [Weld](https://github.com/weld/weld-vertx) - 将 CDI 编程模型引入 Vert.x 生态系统（将 CDI 观察者方法注册为 Vert.x 消息消费者、CDI 支持的 Verticles、以声明性方式定义路由等）。

* 流星
  * [Meteor](https://github.com/jmusacchio/vertxbus/) - 通过 Vert.x 事件总线支持 Meteor 集成。

* 指标
  * [Hawkular metrics](https://github.com/tsegismont/vertx-monitor) - [Hawkular](http://www.hawkular.org/) Vert.x Metrics SPI 的实现。
* [DropWizard 指标](https://github.com/vert-x3/vertx-dropwizard-metrics) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - 使用 DropWizard 指标实现指标。
* [Micrometer 指标](https://github.com/vert-x3/vertx-micrometer-metrics) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - 使用 Micrometer 指标实现指标。
  * [OpenTsDb Metrics](https://github.com/cyngn/vertx-opentsdb) - [OpenTsDb](http://opentsdb.net/) Vert.x 指标客户端。
  * [Bosun Monitoring](https://github.com/cyngn/vertx-bosun) - [Bosun](https://bosun.org/) Vert.x 客户端库。

* Netflix - Hystrix
  * [Hystrix Metrics Stream](https://github.com/kennedyoliveira/hystrix-vertx-metrics-stream.git) - 使用 [Hystrix](https://github.com/Netflix/Hystrix) 从 Vert.x 应用程序发出 Hystrix 仪表板的指标。

* 飞镖
  * [Vert.x Dart SockJS](https://github.com/wem/vertx-dart-sockjs) - [Dart](https://www.dartlang.org/) 集成 [Vert.x SockJS 桥](http://vertx.io/docs/vertx-web/java/#_sockjs_event_bus_bridge) 和使用 dart:js 的普通 SockJS。

* 推送通知
  * [Onesignal](https://github.com/jklingsporn/vertx-push-onesignal) - 使用 [OneSignal](https://onesignal.com/) 从 Vert.x 应用程序向（移动/网络）应用程序发送推送通知。

* CNCF 云活动
  * [CloudEvents.io Java SDK](https://github.com/cloudevents/sdk-java) - 使用 CloudEvents 的 [Vert.x HTTP Transport](https://github.com/cloudevents/sdk-java/blob/master/http/vertx/README.md) 发送和接收 [CloudEvents](https://cloudevents.io/)。

## 中间件

* [Apache Camel](https://camel.apache.org/components/vertx-component.html) - [Apache Camel](http://camel.apache.org/) 用于桥接 Camel 与 Vert.x 事件总线的组件。
* [Gateleen](https://github.com/swisspush/gateleen) - 基于 Vert.x 的中间件库，用于构建高级 JSON/REST 通信服务器。
* [Gravitee.io](https://gravitee.io) - OSS API平台包括API网关和基于Vert.x Core / Vert.x Web等模块的OAuth2 / OIDC授权服务器。
* [API Framework](https://github.com/vinscom/api-framework) - 基于 Vert.x 和 Glue 的微服务框架消除了独立应用程序和无服务应用程序之间的区别。所有服务都可以在独立服务器中运行，但是，如果需要，可以使用相同的代码库将任何服务作为无服务器应用程序运行。

## 语言支持

*对 Vert.x 的编程语言支持*

* [Ceylon](https://github.com/vert-x3/vertx-lang-ceylon) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - 锡兰支持。
* [Groovy](https://github.com/vert-x3/vertx-lang-groovy) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - Groovy 支持。
* [Java](https://github.com/eclipse/vert.x) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - Vert.x 主存储库（包括 Java API）。
* [JavaScript](https://github.com/vert-x3/vertx-lang-js) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - JavaScript 支持。
* [Python](https://github.com/vert-x3/vertx-lang-python) - Python 支持。
* [Ruby](https://github.com/vert-x3/vertx-lang-ruby) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - Ruby 支持。
* [Scala](https://github.com/vert-x3/vertx-lang-scala) - <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - Scala 支持。
* [Kotlin](https://github.com/vert-x3/vertx-lang-kotlin) - <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - Kotlin 支持。
* [EcmaScript](https://github.com/reactiverse/es4x) - EcmaScript >=6 (JavaScript) 支持。
* [Php](https://github.com/vert-x-cn/vertx-lang-jphp) - PHP支持。

*语言扩展*

* [Grooveex](https://github.com/aesteve/grooveex) - [vertx-lang-groovy](https://github.com/vert-x3/vertx-lang-groovy) 之上的语法糖 + 实用程序（DSL 构建器等）。

## 反应性

* [反应流](https://github.com/vert-x3/vertx-reactive-streams) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - Vert.x 反应流。
* [Vert.x Rx](https://github.com/vert-x3/vertx-rx) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - Vert.x 反应式扩展。
* [Vert.x 同步](https://github.com/vert-x3/vertx-sync) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - Vert.x 光纤支持。
* [Kotlin 协程](https://github.com/vert-x3/vertx-lang-kotlin/tree/master/vertx-lang-kotlin-coroutines) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - Vert.x 对 Kotlin 协程的支持。
* [vertx-util](https://github.com/cyngn/vertx-util) - Vert.x 的轻量级承诺和闩锁。
* [QBit](https://github.com/advantageous/qbit) - 类似异步类型的 actor 库，可以在 Vert.x 异步回调中轻松运行。回调管理。
* [VxRifa](https://nsforth.github.io/vxrifa) - Vert.X 的实用程序库，允许通过 EventBus 在通信中使用强类型接口。
* [Vert.x Effect](https://github.com/imrafaelmerino/vertx-effect) - 基于 IO Monad 的纯函数式和反应式库，可实现任何复杂的流程。完全支持重试、回退和恢复操作。
* [SmallRye Mutiny](https://smallrye.io/smallrye-mutiny/) - 用于 Java 的直观事件驱动反应式编程库，具有 [Vert.x 的绑定](https://smallrye.io/smallrye-mutiny-vertx-bindings/)。

## 同步线程非阻塞

* [Sync](https://github.com/vert-x3/vertx-sync) - 同步但非操作系统线程阻塞的 verticle。

## Vert.x 事件总线客户端

*将应用程序连接到 Vert.x 事件总线的客户端*

* [C++11](https://github.com/julien3/vertxbuspp) - C++11 事件总线客户端。
* [Java](https://github.com/saffron-technology/vertx-eventbusbridge) - vertxbus.js 的 Java 实现。
* [Java](https://github.com/abdlquadri/vertx-eventbus-java) - Java 和 Android 事件总线客户端。
* [Java](https://github.com/danielstieger/javaxbus) - 使用普通 TCP 套接字 I/O 的简单 Java 事件总线客户端。
* [CLI](https://github.com/cinterloper/vxc) - Vert.x 事件总线的命令行二进制客户端 - JSON 中的管道，发出 JSON。
* [Swift](https://github.com/tobias/vertx-swift-eventbus) - 使用 [基于 TCP 的协议](https://github.com/vert-x3/vertx-tcp-eventbus-bridge) 的 [Apple Swift](https://swift.org) 事件总线客户端。
* [Python](https://github.com/jaymine/TCP-eventbus-client-Python) - 使用 [基于 TCP 的协议](https://github.com/vert-x3/vertx-tcp-eventbus-bridge) 的 Python 事件总线客户端。
* [C#](https://github.com/jaymine/TCP-eventbus-client-C-Sharp) - 使用 [基于 TCP 的协议](https://github.com/vert-x3/vertx-tcp-eventbus-bridge) 的 C# 事件总线客户端。
* [C](https://github.com/jaymine/TCP-eventbus-client-C) - 使用 [基于 TCP 的协议](https://github.com/vert-x3/vertx-tcp-eventbus-bridge) 的 C99 事件总线客户端。
* [Go](https://github.com/jponge/vertx-go-tcp-eventbus-bridge) - 使用 [基于 TCP 的协议](https://github.com/vert-x3/vertx-tcp-eventbus-bridge) 的 Go-lang 事件总线客户端。
* [Smalltalk](https://github.com/mumez/VerStix) - 使用 [基于 TCP 的协议](https://github.com/vert-x3/vertx-tcp-eventbus-bridge) 的 [Pharo Smalltalk](http://pharo.org/) 事件总线客户端。
* [Java](https://github.com/nielsbaloe/vertxui/tree/master/vertxui-core/src/main/java/live/connector/vertxui/client/transport) - 通过 Java 代码支持 JavaScript 中的事件总线。
* [Elixir](https://github.com/PharosProduction/ExVertx) - 使用 TCP 套接字的 Elixir 应用程序的事件总线支持。
* [Rust](https://github.com/aesteve/vertx-eventbus-client-rs) - 通过 TCP 的 Rust 应用程序的事件总线客户端。

## Vert.x 事件总线扩展

* [Eventbus Service](https://github.com/wowselim/eventbus-service) - 通过简单的 Kotlin 接口进行类型安全事件总线通信的代码生成器。

## 集群管理器

*Vert.x 集群管理器 SPI 的实现*

* [Hazelcast 集群管理器](https://github.com/vert-x3/vertx-hazelcast) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - Hazelcast 集群管理器。
* [Ignite 集群管理器](https://github.com/vert-x3/vertx-ignite) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - Ignite 集群管理器。
* [JGroups Cluster Manager](https://github.com/vert-x3/vertx-jgroups) - JGroups 集群管理器。
* [Zookeeper 集群管理器](https://github.com/vert-x3/vertx-zookeeper) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - Zookeeper 集群管理器。
* [Infinispan 集群管理器](https://github.com/vert-x3/vertx-infinispan) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - Infinispan 集群管理器。
* [Consul Cluster Manager](https://github.com/reactiverse/consul-cluster-manager) - 领事集群管理器。

## 云支持

* [OpenShift DIY 墨盒](https://github.com/vert-x3/vertx-openshift-diy-quickstart) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - 使用 Vert.x 的 OpenShift DIY 墨盒。
* [OpenShift Vert.x 盒](https://github.com/vert-x3/vertx-openshift-cartridge) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - 使用 Vert.x 的 OpenShift Vert.x 盒。
* [AWS SDK](https://github.com/reactiverse/aws-sdk) - 将 AWS Java SDK v2（异步）与 Vert.x 结合使用

## 微服务

* [服务发现](https://github.com/vert-x3/vertx-service-discovery) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x 服务发现" height="16px"> - Vert.x 服务发现。
* [断路器](https://github.com/vert-x3/vertx- Circuit-breaker) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x 断路器" height="16px"> - Vert.x 断路器。
* [服务发现 - Consul](https://github.com/vert-x3/vertx-service-discovery) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x 服务发现 - Consul" height="16px"> - [Consul](https://www.consul.io/) Vert.x 服务发现扩展。
* [服务发现 - Docker 链接](https://github.com/vert-x3/vertx-service-discovery) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x 服务发现 - Docker 链接" height="16px"> - [Docker](https://www.docker.com/) 扩展至 Vert.x 服务发现。
* [服务发现 - Kubernetes](https://github.com/vert-x3/vertx-service-discovery) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x 服务发现 - Kubernetes" height="16px"> - [Kubernetes](http://kubernetes.io/) 对 Vert.x 服务发现的扩展。
* [服务发现 - Redis 后端](https://github.com/vert-x3/vertx-service-discovery) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x 服务发现 - Redis 后端" height="16px"> - Vert.x 服务发现的 [Redis](http://redis.io/) 存储后端。
* [Vert.x GraphQL Service Discovery](https://github.com/engagingspaces/vertx-graphql-service-discovery) - [GraphQL](http://graphql.org/) 服务发现和查询 Vert.x 微服务。
* [Resilience4j](https://github.com/resilience4j/resilience4j) - Resilience4j 是一个专为 Java8 和函数式编程设计的容错库。 Resilience4j 提供用于熔断、速率限制、Bulkheading、自动重试、响应缓存和指标测量的模块。
* [Failsafe](https://failsafe.dev/) - Failsafe 是一个轻量级、“零依赖”库，用于处理 Java 8+ 中的故障。简洁的API。与使用自己的调度程序进行异步执行的库集成，例如 Akka 或 Vert.x。 [Vert.x 示例](https://github.com/failsafe-lib/failsafe/blob/master/examples/src/main/java/dev/failsafe/examples/VertxExample.java)
* [Autonomous Services](https://github.com/mikand13/autonomous-services) - 用于创建自治服务的工具包。该架构利用 vert.x 和 nannoq-tools 提供基于事件的反应式架构，无需集中式组件，既不用于通信也不用于数据，从而在整个架构中提供理论上的线性可扩展性。
* [Apache ServiceComb Java Chassis](https://github.com/apache/servicecomb-java-chassis) - ServiceComb Java Chassis是一个用于用Java快速开发微服务的软件开发工具包（SDK），提供服务注册、服务发现、动态路由和服务管理功能。
* [SmallRye Fault Tolerance](https://github.com/smallrye/smallrye-fault-tolerance) - SmallRye 容错是 Eclipse MicroProfile 容错的实现，具有规范中未定义的附加功能。本机支持 [Vert.x](https://smallrye.io/docs/smallrye-fault-tolerance/6.2.6/integration/event-loop.html) 和 [Mutiny](https://smallrye.io/docs/smallrye-fault-tolerance/6.2.6/reference/asynchronous.html#async-types)。

## 游戏开发

* [Orbital](https://github.com/tfkfan/orbital) - 基于 Vert.x 的反应式分布式游戏服务器和大逃杀多人游戏开发工具。 Orbital 包含基本的可扩展匹配器、游戏/游戏室管理、Websocket 集成和游戏生命周期管理功能。最接近“Colyseus”游戏引擎的竞争对手。 [文档](https://tfkfan.github.io/orbital)。

## 搜索引擎

* [Vert.x Elasticsearch Service](https://github.com/englishtown/vertx-elasticsearch-service) - 具有事件总线代理的 Vert.x 3 [Elasticsearch](https://www.elastic.co/) 服务。
* [Vert.x Solr Service](https://github.com/englishtown/vertx-solr-service) - 具有事件总线代理的 Vert.x 3 Solr 服务。

## 服务工厂

* [服务工厂](https://github.com/vert-x3/vertx-service-factory) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - Vert.x 服务工厂。
* [Maven 服务工厂](https://github.com/vert-x3/vertx-maven-service-factory) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - Maven Vert.x 服务工厂。
* [HTTP 服务工厂](https://github.com/vert-x3/vertx-http-service-factory) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - Vert.x HTTP 服务工厂。
* [Node.js Service Factory](https://github.com/mellster2012/vertx-nodejs-service-factory) - Vert.x Node.js 服务工厂。
* [Eclipse SISU Service Factories](https://github.com/cstamas/vertx-sisu) - Vert.x 与 [Eclipse SISU](https://www.eclipse.org/sisu/) DI 容器集成，提供“vertx-service-factory”和“vertx-maven-service-factory”的替代方案。

## 配置

* [Vert.x Config AWS SSM Store](https://github.com/Finovertech/vertx-config-aws-ssm) - 用于从 [AWS EC2 SSM Parameter Store](https://aws.amazon.com/ec2/systems-manager/parameter-store/) 检索配置值的 [config store](http://vertx.io/docs/vertx-config/java/) 实现。
* [Vert.x Boot](https://github.com/jponge/vertx-boot) - 从 HOCON 配置部署 verticle。

## 依赖注入

* [Vert.x Guice](https://github.com/englishtown/vertx-guice) - 用于 Guice 依赖注入的 Vert.x verticle 工厂。
* [Vert.x HK2](https://github.com/englishtown/vertx-hk2) - 用于 HK2 依赖注入的 Vert.x verticle 工厂。
* [Spring Vert.x Extension](https://github.com/amoAHCP/spring-vertx-ext) - 用于 Spring DI 注入的 Vert.x verticle 工厂。
* [Vert.x Beans](https://github.com/rworsnop/vertx-beans) - 将 Vert.x 对象作为 bean 注入到 Spring 应用程序中。
* [QBit](https://github.com/advantageous/qbit) - QBit 可与 Spring DI 和 Spring Boot（当然还有 Vert.x）配合使用。允许您在同一应用程序中使用 QBit、Vert.x、Spring DI 和 Spring Boot。
* [Vert.x Eclipse SISU](https://github.com/cstamas/vertx-sisu) - Vert.x 与 [Eclipse SISU](https://www.eclipse.org/sisu/) DI 容器集成。
* [Vert.x Spring Verticle Factory](https://github.com/juanavelez/vertx-spring-verticle-factory) - Vert.x Verticle Factory，使用 Spring 来获取和配置 Verticles。
* [Glue](https://github.com/vinscom/glue) - 针对基于 Java 和 Vert.x 的应用程序的经过验证且固执己见的编程和配置模型。受到 ATG Nucleus 的启发，使用简单的属性文件提供强大的基于层的配置管理。

## 测试

* [Vert.x Unit](https://github.com/vert-x3/vertx-unit) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - Vert.x 的异步多语言单元测试。
* [Vert.x JUnit5](https://github.com/vert-x3/vertx-junit5) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - 使用 junit5 对 Vert.x 进行异步单元测试。
* [Vert.x WireMongo](https://github.com/noenv/vertx-wiremongo) - Vert.x 的轻量级 MongoDB 模拟

## 开发工具

* [Vert.x shell](https://github.com/vert-x3/vertx-shell) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - 允许从命令行与 Vert.x 交互。
* [Vert.x health check](https://github.com/vert-x3/vertx-health-check) - 允许在 Vert.x 项目中进行远程健康检查。
* [Vert.x Hot](https://github.com/dazraf/vertx-hot) - 用于热部署 Maven Vert.x 项目的 Maven 插件。
* [Vert.x for Visual Studio Code](https://github.com/pmlopes/VertxSnippet) - 适用于 Vert.x 的 Visual Studio Code（多语言）插件。也可从 [市场](https://marketplace.visualstudio.com/items?itemName=pmlopes.vertxsnippet) 获取。
* [Vert.x Starter](http://www.jetdrone.xyz/vertx-starter/) - 适用于 Vert.x 应用程序的基于浏览器的项目启动器和项目模板。
* [Vert.x LiveReload](https://github.com/ybonnel/vertx-livereload) - 用于 Vert.x 应用程序的简单 livereload 服务器。
* [openapi-generator](https://github.com/OpenAPITools/openapi-generator) - OpenAPI 生成器允许在给定 OpenAPI 规范（v2、v3）的情况下自动生成 API 客户端库（SDK 生成）、服务器存根、文档和配置。

## 杂项

* [Vert.x Child Process](https://github.com/vietj/vertx-childprocess) - 从 Vert.x 生成子进程。
* [vertx-redisques](https://github.com/swisspush/vertx-redisques) - 适用于 Vert.x 的高度可扩展的 redis 持久队列系统。
* [Simple File Server](https://github.com/pitchpoint-solutions/sfs) - 一个与 OpenStack Swift 兼容的分布式对象存储服务器，可以使用 Vert.x 实现的最少资源来服务和安全地存储数十亿个大小文件。
* [Vert.x Boot](https://github.com/jponge/vertx-boot) - 从 HOCON 配置部署 verticle。
* [GDH](https://github.com/maxamel/GDH) - 构建在 Vert.x 之上的通用 Diffie-Hellman 密钥交换 Java 库。
* [vertx-values](https://github.com/imrafaelmerino/vertx-values) - 通过事件总线从 [json-values](https://github.com/imrafaelmerino/json-values) 发送不可变且持久的 JSON。

## 分布

* [Vert.x Stack](https://github.com/vert-x3/vertx-stack) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - Vert.x + 认可的模块。

## 示例

* [Vert.x 蓝图 - 微服务应用程序](https://github.com/sczyh30/vertx-blueprint-microservice) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - 官方 Vert.x 蓝图展示了如何构建复杂的微服务应用程序。
* [Vert.x 蓝图 - 作业队列](https://github.com/sczyh30/vertx-blueprint-job-queue) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - 官方 Vert.x 蓝图展示了如何构建分布式作业处理应用程序。
* [Vert.x 蓝图 - TODO 后端](https://github.com/sczyh30/vertx-blueprint-todo-backend) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - 官方 Vert.x 蓝图展示了如何为 TODO 应用程序构建后端。
* [Vert.x 示例](https://github.com/vert-x3/vertx-examples) <img src="vertx-favicon.svg" alt="(stack)" title="Vert.x Stack" height="16px"> - 官方 Vert.x 示例，包括 Web 示例、如何使用官方数据库客户端等。
* [Vert.x feeds](https://github.com/aesteve/vertx-feeds) - 使用 Vert.x、Gradle、MongoDB、Redis、Handlebars 模板、AngularJS、事件总线和 SockJS 构建的 RSS 聚合器示例。
* [Vert.x Markdown service](https://github.com/aesteve/vertx-markdown-service) - 有关如何在 Gradle 中使用 [service-proxy](https://github.com/vert-x3/vertx-service-proxy) 的示例。
* [Example using event bus and service proxies to connect vertx and node](https://github.com/advantageous/vertx-node-ec2-eventbus-example) - 带有 wiki 描述的分步示例展示了如何使用事件总线和服务代理连接 Vert.x 和 Node。
* [Vert.x Todo-Backend implementation](https://github.com/aesteve/todo-backend-vertx) - Todo MVC 后端的纯 Java 8 实现。使用 Vert.x LocalMap 进行存储。
* [Kotlin Todo-Backend implementation](https://github.com/aesteve/vertx-kotlin-todomvc) - Todo MVC 后端的 Kotlin 实现。
* [Scala Todo-Backend implementation](https://github.com/aesteve/vertx-scala-todomvc) - Todo MVC 后端的 Scala 实现。
* [Grooveex Todo-Backend implementation](https://github.com/aesteve/todo-backend-grooveex) - Todo MVC 后端实现采用 Vert.x + Groovy + 一些语法糖 + DSL 路由设施。
* [Vert.x Gradle Starter](https://github.com/yyunikov/vertx-gradle-starter) - Java 8 入门应用程序，包含使用 Vert.x 与 Gradle 构建系统、配置文件配置和 SLF4J 的示例。
* [Vert.x Gentics Mesh Example](https://github.com/gentics/mesh-vertx-example) - 有关如何使用 Gentics Mesh 和车把构建基于模板的 Web 服务器的示例。
* [HTTP/2 showcase](https://github.com/aesteve/http2-showcase) - 一个简单的演示，展示了 HTTP/2 如何在涉及巨大延迟时显着改善用户体验。
* [Vert.x Music Store](https://github.com/tsegismont/vertx-musicstore) - 有关如何使用 RxJava 构建 Vert.x 应用程序的示例应用程序。
* [Crabzilla](https://github.com/crabzilla/crabzilla) - 又一个事件溯源实验。一个探索 Vert.x 来开发事件溯源/CQRS 应用程序的项目。
* [Vert.x PostgreSQL Starter](https://github.com/BillyYccc/vertx-postgresql-starter) - 使用 Vert.x 堆栈和 PostgreSQL 构建整体 CRUD RESTful Web 服务的入门者。
* [Cloud Foundry](https://github.com/amdelamar/vertx-cloudfoundry) - 用于部署到 [Cloud Foundry](https://www.cloudfoundry.org/) 服务提供商的 Vert.x 示例。
* [Knative](https://github.com/knative/docs/tree/main/code-samples/community/serving/helloworld-vertx) - 有关如何将 [Reactive Extensions Vert.x](https://github.com/vert-x3/vertx-rx) 与 [Knative](https://github.com/knative) 结合使用的示例应用程序。
* [Starter Single Verticle API](https://github.com/jgarciasm/ssv-api) - REST API Starter 和项目模板可随时部署，包含大量管道代码、示例和文档，可快速开发 API，几乎无需了解 vert.x，且不会浪费任何时间。
* [AI model output API based on PMML with Vert.x](https://github.com/immusen/vertx-pmml) - 基于 Vert.x 的高性能 PMML 评估器 API。支持通过 JSON 对多个 PMML 模型进行动态路由配置。

## 部署

* [Vert.x Deploy Application](https://github.com/msoute/vertx-deploy-tools) - （无缝）部署到基于 AWS 的 Vert.x 应用程序集群。

## 公用事业

* [Chime](https://github.com/LisiLisenok/Chime) - 在 Vert.x 事件总线上工作的时间调度程序允许使用 *cron-style* 和 *interval* 计时器进行调度。
* [Vert.x Cron](https://github.com/diabolicallabs/vertx-cron) - 使用 cron 规范安排事件。有事件总线和可观察版本。
* [Vert.x CronUtils](https://github.com/NoEnv/vertx-cronutils) - vertx 调度程序的 cron-utils 的抽象。支持 Unix、Cron4j 和 Quartz 样式表达式。
* [Vert.x Scheduler](https://github.com/zero88/vertx-scheduler) - 一个基于普通 Vert.x 核心的轻量级可插拔调度程序，无需任何外部库，可使用 *cron 式* 和 *interval* 计时器进行调度，并在同步和异步任务上提供详细的 *monitor*。
* [Vert.x POJO config](https://github.com/aesteve/vertx-pojo-config) - 允许标准 JSON 配置和（类型安全）配置 Java bean 之间的映射。还允许通过 JSR 303 验证配置 bean。
* [Vert.x Async](https://github.com/gchauvet/vertx-async) - 将 caolan/async Nodejs 模块移植到 Vert.x 框架，为常见的异步模式提供帮助器方法。
* [Vert.x JOLT](https://github.com/lusoalex/vertx-jolt) - 基于原始 bazaarvoice JOLT 项目的 JSON 到 JSON 转换工具。有助于将不同的 json 结构转换为期望的 json 格式。
* [Vert.x Dependent Verticle Deployer](https://github.com/juanavelez/vertx-dependent-verticle-deployer) - Vert.x Verticle 旨在部署 verticle 及其依赖的 verticle。
* [Vert.x Dataloader](https://github.com/engagingspaces/vertx-dataloader) - Vert.x 的 Facebook Dataloader 的 Java 端口。数据层的高效批处理和缓存。
* [Vert.x Util](https://github.com/juanavelez/vertx-util) - Vert.x 实用方法的集合。
* [Vert.x Web Accesslog](https://github.com/romanpierson/vertx-web-accesslog) - 只是一个简单的处理程序，用于在 Vert.x Web 中生成访问日志。
* [Vert.x GraphQL Utils](http://github.com/tibor-kocsis/vertx-graphql-utils) - 路由处理程序和 Vert.x 兼容接口，用于处理 Vert.x 和 Vert.x Web 中的 GraphQL 查询。
* [Nannoq-Tools](https://noriginmedia.github.io/nannoq-tools/) - Nannoq-Tools 是一个工具包，用于利用 Vert.x 构建强大、可扩展的分布式应用程序，包括身份验证、集群管理、Firebase 云消息传递、DynamoDB、完全通用查询、REST 等模块。
* [Contextual logging](https://github.com/reactiverse/reactiverse-contextual-logging) - 与 Vert.x 事件循环模型配合使用的映射诊断上下文 (MDC)。
* [Vert.x JsonPath](https://github.com/NoEnv/vertx-jsonpath) - 使用 Vert.x 的 JsonObject 和 JsonArray 的 JsonPath 的一个非常基本的实现，模仿它们的 getX、containsKey、put 和 remove 方法。

## 演讲

* [Vert.x YouTube 频道](https://www.youtube.com/channel/UCGN6L3tRhs92Uer3c6VxOSA)

## 社区

* [User Group](https://groups.google.com/forum/?fromgroups#!forum/vertx) - 讨论与*使用* Vert.x 相关的所有用户问题。
* [Developer Group](https://groups.google.com/forum/?fromgroups#!forum/vertx-dev) - Vert.x 核心*开发人员*和*贡献者*的小组。
* [Discord Server](https://discord.gg/KzEMwP2) - 讨论任何与 Vert.x 相关的主题。
* [Issues](https://github.com/vert-x3/issues/issues) - Vert.x 核心问题跟踪器。
* [Wiki](https://github.com/vert-x3/wiki/wiki) - 包含有关 Vert.x 的有用信息。
* [Blog](http://vertx.io/blog/) - Vert.x 官方博客包含许多教程和其他信息。

## 文章

* [在 JVM 上拥抱反应式应用程序：深入探讨现代 I/O 模型和 Vert.x](https://www.infoq.com/articles/reactive-java-vertx-deep-dive/)
* [使用 Eclipse Vert.x 和 RX Java 实现响应式](https://blogs.oracle.com/javamagazine/post/going-reactive-with-eclipse-vertx-and-rxjava)
* [Vert.x 3.3.0 具有增强的网络微服务、测试等功能](https://www.infoq.com/news/2016/06/Vert.x-3.3.0-release-features)
* [Tim Fox 关于 Vert.x 3 的采访，Vert.x 3 是 JVM 的原始反应式微服务工具包](http://www.infoq.com/articles/vertx-3-tim-fox)

## 教程

* [Vert.x 简介](https://vertx.io/get-started/)

## 前端

* [VertxUI](https://github.com/nielsbaloe/vertxui) - 纯 Java 前端工具包，具有描述性的流畅模型视图、POJO 流量、虚拟 DOM 上的 JUnit 测试或真实 DOM 上的混合语言等等。

## 贡献

欢迎投稿！首先阅读[贡献指南](CONTRIBUTING.md)。
