<h3对齐=“中心”>
	<img width="120" src="https://github.com/d3viant0ne/awesome-rethinkdb/blob/master/media/rethinkdb.jpg" alt="RethinkDB">
	<br>
</h3>
## 很棒的 RethinkDB

> 精彩的 RethinkDB 资源、库、工具和应用程序的精选列表

受到 [awesome](https://github.com/sindresorhus/awesome) 列表的启发。请随意通过[贡献](CONTRIBUTING.md) 来改进此列表！

### 目录
 - [Resources](#resources)
  - [Documentation](#documentation)
  - [Community](#community)
 - [JavaScript](#javascript-libraries)
 - [Python](#python-libraries)
 - [Ruby](#ruby-libraries)
 - [Java](#java-libraries)
 - [其他语言](#additional-languages)
  - [社区支持](#community-supported-drivers)
 - [研究与培训](#research-and-training)
  - [Articles](#articles)
  - [Talks](#talks)
  - [RethinkDB 示例](#rethinkdb-examples)
  - [社区示例](#community-examples)
 - [Tools](#tools)
  - [Administration](#administrative-tools)
  - [Deployment](#deployment)

<br>
> <h3>RethinkDB 生态系统</h3>

#### 文档

- [RethinkDB](http://rethinkdb.com/docs/) - RethinkDB 文档
- [ReQL API](http://rethinkdb.com/api/javascript/) - JavaScript ReQL 命令参考

#### 社区

- [请求 Slack 邀请](http://slack.rethinkdb.com/)
- [RethinkDB StackOverflow](http://stackoverflow.com/tags/rethinkdb)
- [RethinkDB 博客](https://www.rethinkdb.com/blog/)
- [RethinkDB 谷歌集团](https://groups.google.com/forum/#!forum/rethinkdb)
- [RethinkDB YouTube 频道](https://www.youtube.com/channel/UC1kJkmSWt_snLDfuXgJnLnQ)
- [RethinkDB Reddit](https://www.reddit.com/r/rethinkdb/)

<br>
> <h3>JavaScript 库</h3>

##### 司机

- [RethinkDB JavaScript](https://www.rethinkdb.com/docs/install-drivers/javascript/) - 官方支持的 JavaScript 驱动程序。
- 维护者：`RethinkDB 团队` [![Github](https://github.com/encharm/Font-Awesome-SVG-PNG/blob/master/black/png/16/github.png)]( https://github.com/rethinkdb) [![Twitter](https://github.com/encharm/Font-Awesome-SVG-PNG/blob/master/black/png/16/twitter.png)](https://twitter.com/rethinkdb)
- [RethinkDB Dash](https://github.com/neumino/rethinkdbdash) - 用于 RethinkDB 的高级 Node.js 驱动程序，具有连接池和流支持。
- 维护者：`Michel` [![Github](https://github.com/encharm/Font-Awesome-SVG-PNG/blob/master/black/png/16/github.png)](https://github.com/neumino) [![Twitter](https://github.com/encharm/Font-Awesome-SVG-PNG/blob/master/black/png/16/twitter.png)](https://twitter.com/neumino)

##### ORM

- [Thinky](https://github.com/neumino/thinky) - RethinkDB 的 JavaScript ORM
- 维护者：`Michel` [![Github](https://github.com/encharm/Font-Awesome-SVG-PNG/blob/master/black/png/16/github.png)](https://github.com/neumino) [![Twitter](https://github.com/encharm/Font-Awesome-SVG-PNG/blob/master/black/png/16/twitter.png)](https://twitter.com/neumino)
- [JSData RethinkDB](https://github.com/js-data/js-data-rethinkdb) - 用于 js-data ORM 的 RethinkDB 适配器。
- 维护者：`JS 数据组织` [![Github](https://github.com/encharm/Font-Awesome-SVG-PNG/blob/master/black/png/16/github.png)](https://github.com/js-data)

##### 扩展库

- [RethinkDB Pool](https://github.com/hden/rethinkdb-pool) - RethinkDB 的连接池。
- 维护者：`Hao-kang Den` [![Github](https://github.com/encharm/Font-Awesome-SVG-PNG/blob/master/black/png/16/github.png)](https://github.com/hden)
- [Express Session RethinkDB](https://github.com/armenfilipetyan/express-session-rethinkdb) - Express 4.x 的 RethinkDB 会话存储。
- 维护者：`@armenfilipetyan` [![Github](https://github.com/encharm/Font-Awesome-SVG-PNG/blob/master/black/png/16/github.png)](https://github.com/armenfilipetyan)
 
##### 技术整合

- [Hapi RethinkDB CRUD](https://github.com/athlite/hapi-rethinkdb-crud) - 用于 Hapi 与 Rethinkdb 交互的 CRUD 处理程序。
- 维护者：`Thomas Eng` [![Github](https://github.com/encharm/Font-Awesome-SVG-PNG/blob/master/black/png/16/github.png)](https://github.com/athlite)
- [Sails Hook Thinky](https://github.com/mwielbut/sails-hook-thinky) - 为 Sails 中的 RethinkDB 启用 Thinky ORM 的挂钩。
- 维护者：`Matt Wielbut` [![Github](https://github.com/encharm/Font-Awesome-SVG-PNG/blob/master/black/png/16/github.png)](https://github.com/mwielbut) [![Twitter](https://github.com/encharm/Font-Awesome-SVG-PNG/blob/master/black/png/16/twitter.png)](https://twitter.com/mwielbut)
- [KOA RethinkDB](https://github.com/hden/koa-rethinkdb) - Koa 中间件为您提供 RethinkDB 客户端。
- 维护者：`Hao-kang Den` [![Github](https://github.com/encharm/Font-Awesome-SVG-PNG/blob/master/black/png/16/github.png)](https://github.com/hden)
- [RabbitMQ](http://rethinkdb.com/docs/rabbitmq/javascript/) - 将 RethinkDB 与 RabbitMQ 集成
- 维护者：`RethinkDB 团队` [![Github](https://github.com/encharm/Font-Awesome-SVG-PNG/blob/master/black/png/16/github.png)]( https://github.com/rethinkdb) [![Twitter](https://github.com/encharm/Font-Awesome-SVG-PNG/blob/master/black/png/16/twitter.png)](https://twitter.com/rethinkdb)

**[返回顶部](#目录)**

<br>
> <h3>Python 库</h3>

##### 司机

- [RethinkDB Python](https://www.rethinkdb.com/docs/install-drivers/python/) - 官方支持的 JavaScript 驱动程序。
- 维护者：`RethinkDB 团队` [![Github](https://github.com/encharm/Font-Awesome-SVG-PNG/blob/master/black/png/16/github.png)]( https://github.com/rethinkdb) [![Twitter](https://github.com/encharm/Font-Awesome-SVG-PNG/blob/master/black/png/16/twitter.png)](https://twitter.com/rethinkdb)

##### ORM

- [Remodel](https://github.com/linkyndy/remodel) - RethinkDB 的对象文档映射器非常简单但功能强大且可扩展，用 Python 编写。
- 维护者：`Andrei Horak` [![Github](https://github.com/encharm/Font-Awesome-SVG-PNG/blob/master/black/png/16/github.png)](https://github.com/linkyndy) [![Twitter](https://github.com/encharm/Font-Awesome-SVG-PNG/blob/master/black/png/16/twitter.png)](https://twitter.com/linkyndy)
- [Rethink](https://github.com/caoimhghin/rethink) - Python RethinkDB 对象映射器接口受 Appengine NDB 启发。
- 维护者：`Kevin Amerson` [![Github](https://github.com/encharm/Font-Awesome-SVG-PNG/blob/master/black/png/16/github.png)](https://github.com/caoimhghin) [![Twitter](https://github.com/encharm/Font-Awesome-SVG-PNG/blob/master/black/png/16/twitter.png)](https://twitter.com/kevinamerson)

##### 技术整合

- [flask-rethinkdb](https://github.com/linkyndy/flask-rethinkdb) - 向 Flask 添加 RethinkDB 支持。
- 维护者：`Andrei Horak` [![Github](https://github.com/encharm/Font-Awesome-SVG-PNG/blob/master/black/png/16/github.png)](https://github.com/linkyndy) [![Twitter](https://github.com/encharm/Font-Awesome-SVG-PNG/blob/master/black/png/16/twitter.png)](https://twitter.com/linkyndy)
- [RabbitMQ](https://www.rethinkdb.com/docs/rabbitmq/python/) - 将 RethinkDB 与 RabbitMQ 集成
- 维护者：`RethinkDB 团队` [![Github](https://github.com/encharm/Font-Awesome-SVG-PNG/blob/master/black/png/16/github.png)]( https://github.com/rethinkdb) [![Twitter](https://github.com/encharm/Font-Awesome-SVG-PNG/blob/master/black/png/16/twitter.png)](https://twitter.com/rethinkdb)

**[返回顶部](#目录)**

<br>
> <h3>Ruby 库</h3>

##### 司机

- [RethinkDB Ruby](http://rethinkdb.com/docs/install-drivers/ruby/) - 官方支持 Ruby 驱动程序。
- 维护者：`RethinkDB 团队` [![Github](https://github.com/encharm/Font-Awesome-SVG-PNG/blob/master/black/png/16/github.png)]( https://github.com/rethinkdb) [![Twitter](https://github.com/encharm/Font-Awesome-SVG-PNG/blob/master/black/png/16/twitter.png)](https://twitter.com/rethinkdb)

##### ORM

- [NoBrainer](https://github.com/nviennot/nobrainer) - 用于 RethinkDB 的 Ruby ORM。
- 维护者：`Nicolas Viennot` [![Github](https://github.com/encharm/Font-Awesome-SVG-PNG/blob/master/black/png/16/github.png)](https://github.com/nviennot) [![Twitter](https://github.com/encharm/Font-Awesome-SVG-PNG/blob/master/black/png/16/twitter.png)](https://twitter.com/nviennot)

##### 技术整合

- [Epiphy](https://github.com/kureikain/epiphy) - 轻量级 RethinkDB ORM。
- 维护者：`Vinh Quốc Nguyễn` [![Github](https://github.com/encharm/Font-Awesome-SVG-PNG/blob/master/black/png/16/github.png)](https://github.com/kureikain) [![Twitter](https://github.com/encharm/Font-Awesome-SVG-PNG/blob/master/black/png/16/twitter.png)](https://twitter.com/kureikain)
- [lotus-rethinkdb](https://github.com/angeloashmore/lotus-rethinkdb) - Lotus::Model 的 RethinkDB 适配器。
- 维护者：`Angelo Ashmore` [![Github](https://github.com/encharm/Font-Awesome-SVG-PNG/blob/master/black/png/16/github.png)](https://github.com/angeloashmore) [![Twitter](https://github.com/encharm/Font-Awesome-SVG-PNG/blob/master/black/png/16/twitter.png)](https://twitter.com/angeloashmore)
- [RabbitMQ](https://www.rethinkdb.com/docs/rabbitmq/ruby/) - 将 RethinkDB 与 RabbitMQ 集成
- 维护者：`RethinkDB 团队` [![Github](https://github.com/encharm/Font-Awesome-SVG-PNG/blob/master/black/png/16/github.png)]( https://github.com/rethinkdb) [![Twitter](https://github.com/encharm/Font-Awesome-SVG-PNG/blob/master/black/png/16/twitter.png)](https://twitter.com/rethinkdb)

**[返回顶部](#目录)**

<br>
> <h3>Java 库</h3>

##### 司机

- [RethinkDB Java](http://rethinkdb.com/docs/install-drivers/java/) - 官方支持的 Java 驱动程序。
- 维护者：`RethinkDB 团队` [![Github](https://github.com/encharm/Font-Awesome-SVG-PNG/blob/master/black/png/16/github.png)]( https://github.com/rethinkdb) [![Twitter](https://github.com/encharm/Font-Awesome-SVG-PNG/blob/master/black/png/16/twitter.png)](https://twitter.com/rethinkdb)
- [Rethinker](https://github.com/futurechimp/rethinker) - 一个简单的序列化库，可与官方 RethinkDb Java 驱动程序一起使用。
- 维护者：`Dave Hrycyszyn` [![Github](https://github.com/encharm/Font-Awesome-SVG-PNG/blob/master/black/png/16/github.png)](https://github.com/futurechimp) [![Twitter](https://github.com/encharm/Font-Awesome-SVG-PNG/blob/master/black/png/16/twitter.png)](https://twitter.com/futurechimp)
- [Rethinkdb4j](https://github.com/tony-brewerio/rethinkdb4j) - 适用于 Java 的基于异步 Netty 的 RethinkDB 驱动程序。
- 维护者：`Anton Ustyuzhanin` [![Github](https://github.com/encharm/Font-Awesome-SVG-PNG/blob/master/black/png/16/github.png)](https://github.com/tony-brewerio)


##### ORM

- [RethinkDB Java ORM](https://github.com/PeterKnego/rethinkdb-java-orm) - RethinkDB Java 驱动程序的自定义 POJO 转换器。
- 维护者：`Peter Knego` [![Github](https://github.com/encharm/Font-Awesome-SVG-PNG/blob/master/black/png/16/github.png)](https://github.com/PeterKnego) [![Twitter](https://github.com/encharm/Font-Awesome-SVG-PNG/blob/master/black/png/16/twitter.png)](https://twitter.com/peterknego)

##### 技术整合

- [RabbitMQ](https://www.rethinkdb.com/docs/rabbitmq/java/) - 将 RethinkDB 与 RabbitMQ 集成
- 维护者：`RethinkDB 团队` [![Github](https://github.com/encharm/Font-Awesome-SVG-PNG/blob/master/black/png/16/github.png)]( https://github.com/rethinkdb) [![Twitter](https://github.com/encharm/Font-Awesome-SVG-PNG/blob/master/black/png/16/twitter.png)](https://twitter.com/rethinkdb)

**[返回顶部](#目录)**

<br>
> <h3>其他语言</h3>

#### 社区支持的驱动程序

- [C#](https://github.com/bchavez/RethinkDb.Driver) - C#/.NET RethinkDB 驱动程序致力于实现 100% ReQL API 覆盖率。
- [C++](https://github.com/AtnNn/librethinkdbxx) - 适用于 C++ 的 RethinkDB 驱动程序。
- [Clojure](https://github.com/apa512/clj-rethinkdb) - Clojure 的 RethinkDB 客户端。
- [Dart](https://github.com/billysometimes/rethinkdb) - RethinkDB v2.0.3 的 Dart 驱动程序。
- [Elixir](https://github.com/hamiltop/rethinkdb-elixir) - 纯 Elixir 中的多路复用 RethinkDB 客户端。
- [Go](https://github.com/dancannon/gorethink) - RethinkDB 的 Go 语言驱动程序。
- [Haskell](https://github.com/AtnNn/haskell-rethinkdb) - Haskell 的 RethinkDB 客户端库。
- [Lisp](https://github.com/orthecreedence/cl-rethinkdb) - Common Lisp 的 RethinkDB 驱动程序。
- [Lua](https://github.com/grandquista/Lua-ReQL) - Lua 中的 Rethinkdb 驱动程序。
- [Objective-C](https://github.com/dparnell/rethink-db-client) - 用 Objective-C 编写的 RethinkDB 客户端。
- [Perl](https://github.com/njlg/perl-rethinkdb) - 纯 Perl RethinkDB 驱动程序。
- [PHP](https://github.com/danielmewes/php-rql) - RethinkDB 查询语言 (ReQL) 的 PHP 客户端驱动程序。
- [Scala](https://github.com/kclay/rethink-scala) - RethinkDB 的 Scala 驱动程序。

**[返回顶部](#目录)**

<br>
> <h3> 研究和培训</h3>

#### 文章

- [Shahid Shaikh | 08-Mar-16](https://codeforgeek.com/2016/03/building-real-time-polling-app-rethinkdb-nodejs/) - 使用 RethinkDB 和 Nodejs 构建实时投票应用程序。
- [Dr. Gleb Bahmutov PhD | 08-Feb-16](https://glebbahmutov.com/blog/redux-and-rethinkdb/) - Redux 和 RethinkDB
- [Scott Hasbrouck | 13-Mar-16](http://www.scotthasbrouck.com/blog/2016/3/13/using-socketio-with-rethinkdb-changefeeds-to-build-a-reactive-backend) - 使用 Socket.Io 与 RethinkDB Changefeeds 构建响应式 JavaScript 堆栈
- [Khalid Abuhakmeh | 15-Nov-15](http://www.khalidabuhakmeh.com/getting-started-with-rethinkdb-and-asp-net-5) - RethinkDB 和 ASP.NET 5 入门。
- [Slava Akhmechet | 01-Sept-15](http://www.infoworld.com/article/2975838/database/build-real-time-web-apps-with-rethinkdb.html) - 使用 RethinkDB 构建实时 Web 应用程序。
- [Justin for Fanout | 20-May-15](http://blog.fanout.io/2015/05/20/building-a-realtime-api-with-rethinkdb/) - 使用 RethinkDB 构建实时 API。
- [Nicholas Duffy | 30-Apr-15](https://strongloop.com/strongblog/rethinkdb-connector-loopback-node-js-framework/) - 用于 LoopBack 的 RethinkDB 连接器入门。
- [Rob Conery | 17-Apr-15](http://rob.conery.io/2015/04/17/rethinkdb-2-0-is-amazing/) - RethinkDB 2.0 太棒了。
- [Gordon Dent | 01-Apr-15](https://www.airpair.com/rethinkdb/posts/moving-from-sql-to-rethinkdb) - 从 SQL 迁移到 RethinkDB 的综合指南。
- [Gordon Dent | 11-Mar-15](http://blog.workshape.io/we-use-rethinkdb-at-workshapeio/) - 我们在 Workshape.io 使用 RethinkDB。

#### 会谈

- [Michael Glukhovsky at Clevertech | 30-Mar-16](https://www.youtube.com/watch?v=28XKxLPv0Hs) - RethinkDB 向 Clevertech 的演示。
- [Ryan Paul at ForwardJS | 21-Jan-16](https://www.youtube.com/watch?v=xCU9RHDWXIY) - RethinkDB：​​实时应用程序的数据库。
- [Rob Conery at DevDay 2015 | 17-Sept-15](https://www.youtube.com/watch?v=Ee1v_SuECRk) - 重新思考 NoSQL。
- [Jorge Silva at RethinkDB Meetup | 29-June-15](https://www.youtube.com/watch?v=vJtDNRsUozk) - RethinkDB 中的数据建模。
- [Ben Tranter | 05-Apr-15](https://www.youtube.com/watch?v=d01rLeIjTLE) - 带有 Express、RethinkDB 和 Thinky 的简单 REST API。
 - [相关来源](https://github.com/bentranter/ampersand-rethink-express)
- [Ryan Paul at Mattermark | 17-Feb-15](https://www.youtube.com/watch?v=dhb63boH8E8) - 使用实时图表构建实时 RethinkDB 集群监控应用程序。
 - [Associated Blog Post](http://rethinkdb.com/blog/realtime-cluster-monitoring/) - 带有实时图表的实时 RethinkDB 集群监控应用程序。

#### RethinkDB 示例

- [RethinkDB NodeJS Chat](https://github.com/rethinkdb/rethinkdb-example-nodejs-chat) - 在 rethinkdb 上运行的 Node.js 聊天应用程序。
- [RethinkDB Flask Backbone ToDo](https://github.com/rethinkdb/rethinkdb-example-flask-backbone-todo) - 在 Flask 和 RethinkDB 上运行的规范主干待办事项应用程序。
- [RethinkDB ccoenraets/nodecellar Fork](https://github.com/rethinkdb/nodecellar-rethinkdb) - 使用 Backbone.js、Bootstrap、Node.js、Express、RethinkDB 构建的示例应用程序。
- [RethinkDB PubNub Live Blog](https://github.com/rethinkdb/rethinkdb-pubnub-liveblog) - PubNub / Express 博客示例应用程序。
- [RethinkDB Angular Express Promise](https://github.com/rethinkdb/rethinkdb-example-nodejs/tree/master/todo-angular-express-promise) - 基于 Promise 的 Todo 示例，包含 RethinkDB、ExpressJS 和 AngularJS。
- [RethinkDB Angular Express](https://github.com/rethinkdb/rethinkdb-example-nodejs/tree/master/todo-angular-express) - RethinkDB、ExpressJS 和 AngularJS 的待办事项示例。
- [RethinkDB Angular KOA](https://github.com/rethinkdb/rethinkdb-example-nodejs/tree/master/todo-angular-koa) - 使用 RethinkDB、KoaJS 和 AngularJS 的 Todo 示例。

#### 社区示例

- [RethinkDB Chat](https://github.com/thejsj/rethinkdb-chat) - 使用 RethinkDB + Sockets 构建的简单聊天应用程序。
- [RethinkDB Reactjs](https://github.com/arkency/rethinkdb-reactjs) - rethinkdb + React.js + ActionController::Live (Rails) + 服务器端事件。
- [Realtime Chat RethinkDB](https://github.com/Unrestricted-Coding/realtime-chat-RethinkDB) - 使用 RethinkDB 构建的实时聊天室
- [Boot RethinkDB](https://github.com/geowarin/boot-rethinkdb) - 使用 Spring Boot 和 RethinkDB 的聊天示例。
- [Go RethinkDB ToDo](https://github.com/dancannon/GoRethink_TodoDemo) - Go RethinkDB Todo List 示例应用程序。
- [Meguca](https://github.com/bakape/meguca) - Go、TypeScript 和 RethinkDB 中的高性能实时图像板。
- [VueJS RethinkDB](https://github.com/alexcheninfo/vuejs-rethinkdb-example) - Vuejs + Express + RethinkDB 示例。
- [3ree](https://github.com/GordyD/3ree) - 使用 3REE 堆栈、React + Redux + RethinkDB + Express 编写的通用 JS 应用程序示例。
- [Meteor GraphQL](https://github.com/AdamBrodzinski/Meteor-RethinkDB-GraphQL) - 使用 GraphQL 的 Meteor 和 RethinkDB 示例。

**[返回顶部](#目录)**

<br>
> <h3>工具</h3>

#### 管理工具

- [Chateau](https://github.com/neumino/chateau) - RethinkDB 的另一个（很棒的）数据浏览器。
- [RethinkDB CLI](https://github.com/athlite/rethinkdb-cli) - Rethinkdb 的 CLI 和 REPL。
- [RethinkDB Nightly](https://github.com/robconery/rethinkdb_nightly) - 一个节点模块，将执行夜间备份并将其推送到 S3。

#### 部署

- [Vagrant](https://github.com/RyanAmos/rethinkdb-vagrant) - 使用 Vagrant 安装 RethinkDB。
- [Puppet](https://github.com/tmont/puppet-rethinkdb) - RethinkDB 的 Puppet 模块。
- [Chef](https://github.com/AVVSDevelopment/chef-rethinkdb) - Chef RethinkDB 食谱。
- [Wrecker](https://github.com/mies/box-rethinkdb) - RethinkDB 的 Wercker 盒子。
- [Docker](https://github.com/crosbymichael/Dockerfiles/blob/master/rethinkdb/Dockerfile) - 单节点 Dockerfile。

<br>
> <h3>许可证</h3>

[![CC0](http://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)
