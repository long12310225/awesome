# 很棒的 TinkerPop [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

![alt tag](https://raw.githubusercontent.com/mohataher/awesome-tinkerpop/master/tinkerpop-splash.png)


Github 上精选的 TinkerPop 库列表。

>Apache TinkerPop™ 是一个适用于图数据库 (OLTP) 和图分析系统 (OLAP) 的图计算框架。

### 目录
* [TinkerPop3](#tinkerpop3)
	- [Implementations](#tinkerpop3-implementations)
	- [Wrappers/Clients](#wrappers)
	- [查询语言](#qlang)
* [TinkerPop2](#tinkerpop2)
* [Communites](#communites)
* [值得关注的人](#people-to-follow)
* [教程和资源](#tutorials-and-resources)
* [如何贡献](#contributing)
* [License](#license)

### <A NAME="tinkerpop3"></A>TinkerPop3 库
#### <A NAME="tinkerpop3-implementations"></A>实现
* [TinkerPop3 implementation](https://github.com/apache/tinkerpop) - Apache TinkerPop 的镜像。
* [sqlg](https://github.com/pietermartin/sqlg) - Sqlg 是 TinkerPop3 在 RDBMS 上的实现。
* [blazegraph](https://github.com/blazegraph/database) - Blaze Graph 的 TinkerPop3 [实现](https://github.com/blazegraph/tinkerpop3)；高性能图数据库。
* [tinkergraph-js](https://github.com/jbmusso/tinkergraph-js) - TinkerPop 的 TinkerGraph 内存图形数据库的纯 JavaScript 实现。
* [gremlin-javascript](https://github.com/jbmusso/gremlin-javascript) - TinkerPop3 Gremlin 服务器的 JavaScript 图形数据库客户端。
* [Elastic Gremlin](https://github.com/rmagen/elastic-gremlin) - Elasticsearch 后端的 TinkerPop3 实现。
* [Hadoop (Giraph)](http://tinkerpop.apache.org/docs/current/reference/#giraphgraphcomputer) - 使用 Giraph 的 OLAP 图形处理器。
* [Hadoop (Spark)](http://tinkerpop.apache.org/docs/current/reference/#sparkgraphcomputer) - 使用 Spark 的 OLAP 图形处理器。
* [IBM Graph](https://console.ng.bluemix.net/catalog/services/ibm-graph/) - OLTP 图形数据库即服务。
* [Neo4j](http://tinkerpop.apache.org/docs/currentg/#neo4j-gremlin) - OLTP 图形数据库。
* [Stardog](http://stardog.com/) - 支持 OLTP 和 OLAP 的 RDF 图形数据库。
* [TinkerGraph](http://tinkerpop.apache.org/docs/current/reference/#tinkergraph-gremlin) - 内存中 OLTP 和 OLAP 参考实现。
* [Unipop](https://github.com/rmagen/unipop) - OLTP Elasticsearch 和 JDBC 支持图。
* [DuctileDB](https://github.com/PureSolTechnologies/DuctileDB) - Ductile DB 是一个基于 Hadoop/HBase 的图形数据库，提供了大量的功能。
* [hgraphdb](https://github.com/rayokota/hgraphdb) - HBase 作为 TinkerPop 图形数据库。
* [JanusGraph](https://github.com/JanusGraph/janusgraph) - JanusGraph：一个开源的分布式图形数据库 http://janusgraph.org
* [JanusGraph for DynamoDB (Amazon)](https://github.com/awslabs/dynamodb-janusgraph-storage-backend) - JanusGraph 的 Amazon DynamoDB 存储后端。
* [orientdb-gremlin](https://github.com/orientechnologies/orientdb-gremlin) - OrientDB 的 TinkerPop3 图结构实现。


#### <A NAME="wrappers"></A>包装器/客户端
##### C# .NET
* [Teva Gremlin](https://www.nuget.org/packages/Teva.Common.Data.Gremlin/) (.NET - C#) - 适用于 .NET 的 Gremlin 服务器驱动程序。

##### 克洛尤尔
* [ogre](https://github.com/clojurewerkz/ogre) - 用于查询 TinkerPop 图的 Clojure 库。
* [scalajs-gremlin-client](https://github.com/viagraphs/scalajs-gremlin-client) (scala) - 具有临时可扩展、反应式、基于类型类的 API 的 Gremlin-Server 客户端。

##### 去
* [go-gremlin](https://github.com/go-gremlin/gremlin) - TinkerPop3 Gremlin Server 的 Go 图形数据库客户端。
* [Gremgo](https://github.com/qasaur/gremgo) - 用于 TinkerPop 图形数据库堆栈的快速、高效且易于使用的 Go 客户端。
* [grammes](https://github.com/northwesternmutual/grammes) - 一个 Go 包，旨在使用 Gremlin 与 Apache TinkerPop™ 图形计算框架进行通信。

##### 哈斯克尔
* [greskell-websocket](https://github.com/debug-ito/greskell) - TinkerPop3 Gremlin 服务器的 Haskell 客户端。

##### 爪哇
* [gremlin-driver](http://tinkerpop.apache.org/docs/current/reference/#connecting-via-java) (java) - 适用于 Java 的 Gremlin 服务器驱动程序。
* [neo4j-tinkerpop-api](https://github.com/neo4j-contrib/neo4j-tinkerpop-api) - TinkerPop3 的 Apache 许可 Neo4j API。
* [neo4j-gremlin-bolt](https://github.com/SteelBridgeLabs/neo4j-gremlin-bolt) - 允许使用 BOLT 协议将 Apache Tinkerpop Java API 与 neo4j 服务器结合使用。
* [Ferma](https://github.com/Syncleus/Ferma) - TinkerPop 图形堆栈的 ORM / OGM。

##### JavaScript
* [ts-tinkerpop](https://github.com/RedSeal-co/ts-tinkerpop) - 通过 Typescript 中的 node-java API 使用 TinkerPop3 的实用程序。
* [gremlin-javascript](https://github.com/jbmusso/gremlin-javascript) (js) - JavaScript 的 Gremlin 服务器驱动程序。

##### PHP
* [gremlin-php](https://github.com/PommeVerte/gremlin-php) - gremlin-server php 驱动程序与 TinkerPop3 兼容。它将允许您连接到 gremlin-server 及其后端（Neo4J、Titan 等）。

##### 蟒蛇
* [Mogwai](https://github.com/platinummonkey/mogwai) - 适用于 Python 的 TinkerPop3 图形数据库库。
* [python-gremlin-rest](https://github.com/windj007/python-gremlin-rest) - Gremlin Server 基于 REST 的客户端。
* [gremlinclient](https://github.com/davebshow/gremlinclient) - Gremlin Server 的异步 Python 2/3 客户端，允许灵活的协程语法 - Trollius、Tornado、Asyncio。
* [aiogremlin](https://github.com/davebshow/aiogremlin) (python) - 基于 asyncio 和 aiohttp 的 Python 3 库，使用 websockets 与 Gremlin 服务器通信。
* [gremlinrestclient](http://gremlinrestclient.readthedocs.org/en/latest/) (python) - 使用 HTTP 通过 REST 与 Gremlin 服务器进行通信的 Python 2/3 库。
* [goblin](https://github.com/ZEROFAIL/goblin) - TinkerPop3 Gremlin 服务器的 OGM。
* [goblin 3.5](https://github.com/davebshow/goblin) - TinkerPop 3 OGM Goblin 的 Python 3.5 重写。

##### 反应性
* [reactive-gremlin](https://github.com/coreyauger/reactive-gremlin) (scala) - Akka HTTP Websocket 连接器。

##### 斯卡拉
* [Gremlin Scala](https://github.com/mpollmeier/gremlin-scala) - Apache TinkerPop3 Graph DSL 的 Scala 包装器。
* [blueprints-scala](https://github.com/anvie/blueprints-scala) - Tinkerpop 蓝图 Scala。

#### <A NAME="qlang"></A>查询语言
* [gremlin-py](https://github.com/emehrkay/gremlinpy) - 编写可以发送到 Gremlin Server 的纯 Python Gremlin。
* [gremlin-scala](https://github.com/mpollmeier/gremlin-scala) - TinkerPop3 的 Scala 语言包装器。
* [gremlin-template-string](https://github.com/jbmusso/gremlin-template-string) - Javascript Gremlin 语言构建器。
* [ipython-gremlin](https://github.com/davebshow/ipython-gremlin) - IPython 和 Jupyter 中的 Gremlin。
* [ogre](http://ogre.clojurewerkz.org/) - TinkerPop3 的 Clojure 语言包装器。
* [Peapod](https://github.com/bayofmany/peapod) - Tinkerpop3 图形堆栈的新对象图形包装器。
* [sparql-gremlin](https://github.com/dkuppitz/sparql-gremlin) - SPARQL 到 Gremlin 的遍历编译器。
* [sql-gremlin](https://github.com/twilmes/sql-gremlin) - SQL 到 Gremlin 遍历编译器。
* [greskell](https://github.com/debug-ito/greskell) - Gremlin 图查询语言的 Haskell 绑定
* [Cypher for Gremlin](https://github.com/opencypher/cypher-for-gremlin) - Cypher for Gremlin 向任何 Gremlin 图形数据库添加了 Cypher 支持。

### <A NAME="tinkerpop2"></A>TinkerPop 2 库
* [Ferma](https://github.com/Syncleus/Ferma) - TinkerPop 图形堆栈的 ORM / OGM。
* [Frames](https://github.com/tinkerpop/frames) - 对象到图框架。
* [Archimedes](https://github.com/clojurewerkz/archimedes) - 蓝图的 Clojure 库（TinkerPop 图形堆栈的一部分）。
* [AccumuloGraph](https://github.com/JHUAPL/AccumuloGraph) - 使用 Accumulo 实现 TinkerPop 蓝图。
* [Frontenac](https://github.com/Loupi/Frontenac) - TinkerPop Stack 的 .NET 端口。
* [Mogwai](https://github.com/platinummonkey/mogwai) - 适用于 Python 的 TinkerPop 2 图形数据库库。
* [spring-data-gremlin](https://github.com/gjrwebber/spring-data-gremlin) - Spring data gremlin 使得实现基于图的存储库变得更加容易。该模块扩展了 Spring Data，以支持任何实现 TinkerPop Blueprints 2.x API 的潜在图形数据库。
* [blueprints-scala](https://github.com/anvie/blueprints-scala) - TinkerPop 蓝图 Scala。

## <A NAME="communites"></A>社区
* [Gremlin-users](https://groups.google.com/forum/#!forum/gremlin-users) - Gremlin 用户的邮件列表。
* [Stack Overflow](http://stackoverflow.com/questions/tagged/tinkerpop3) - Stack Overflow 有一个相对活跃的社区。
* [TinkerPop-dev](http://mail-archives.apache.org/mod_mbox/incubator-tinkerpop-dev/) - TP3 开发者的邮件列表。

## <A NAME="people-to-follow"></A>要关注的人
* [Marko Rodriguez](https://markorodriguez.com/) - TinkerPop 和 Aurelius 的创始人。
* [Stephen Mallette](https://twitter.com/spmallette?lang=en-gb) - Gremlin、TinkerPop 和 Titan DB 的高级开发人员。
* [Daniel Kuppitz](https://about.me/daniel.kuppitz) - Gremlin 的主要开发者之一。
* [Jason Plurad](https://github.com/pluradj) - IBM 高级开发人员。 TinkerPop 提交者并且活跃于社区。

## <A NAME="tutorials-and-resources"></A>教程和资源
* [Introduction to Gremlin](http://tinkerpop.apache.org/gremlin.html) - Gremlin 语言的官方介绍。
* [Datastax Introduction](https://academy.datastax.com/resources/getting-started-tinkerpop-and-gremlin) - Datastax 为 Gremlin 和 TinkerPop3 提供的教程。
* [TinkerPop Book](http://www.tinkerpopbook.com/) - Tinkeprop 许诺要写的一本书，但直到现在才实现。您可以请求通知。
* [Linux Foundation Presentation](http://events.linuxfoundation.org/sites/events/files/slides/ApacheCon2015TinkerPop3.pdf) - David Robinson 在 IBM aboit Apache TinkerPop3 上由 Linux 基金会发表的演讲。
* [Getting Started with TinkerPop](http://tinkerpop.apache.org/docs/current/tutorials/getting-started/) - 了解 TinkerPop 的入门和使用基础知识。
* [The Gremlin Console](http://tinkerpop.apache.org/docs/current/tutorials/the-gremlin-console/) - 讨论 Gremlin 控制台的使用案例和使用模式。
* [Gremlin Recipes](http://tinkerpop.apache.org/docs/3.2.1-SNAPSHOT/recipes/) - 常见遍历模式和风格的参考。
* [Gremlin Language Variants](http://tinkerpop.apache.org/docs/3.2.1-SNAPSHOT/tutorials/gremlin-language-variants/) - 了解如何将 Gremlin 嵌入到主机编程语言中。
* [SQL2Gremlin](http://sql2gremlin.com/) - 使用使用 SQL 查询数据时发现的典型模式来学习 Gremlin。
* [Getting Started with Graph Databases](https://academy.datastax.com/demos/getting-started-graph-databases) - 将关系数据库与图形数据库进行比较，将 SQL 与 Gremlin 进行比较。
* [Graph](https://github.com/krlawrence/graph) - 图数据库、Gremlin 和 TinkerPop - 教程。


## <A NAME="contributing"></A>如何贡献
![alt 标签](awesome-tinkerpop.jpg)

请遵循[此处的指南](contributing.md)。请确保您的贡献和公关很棒！

## <A NAME="license"></A>许可证
[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](http://creativecommons.org/publicdomain/zero/1.0/)

在法律允许的范围内，[@mohataher](https://github.com/mohataher) 已放弃本作品的所有版权以及相关或邻接权。
