# 很棒的 HBase [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

[<img src="https://cdn.rawgit.com/rayokota/awesome-hbase/c197f415/hbase_logo_with_orca-2.png"align="right"width="150">](http://hbase.apache.org/)

精彩 HBase 项目和资源的精选列表。

[HBase](http://hbase.apache.org) 是一个分布式、可扩展的大数据存储。

## 内容

- [Projects](#projects)
    - [Clients](#clients)
    - [Cloud](#cloud)
    - [Frameworks](#frameworks)
        - [Datasets](#datasets)
        - [Document](#document)
        - [Entity/JPA](#entityjpa)
        - [Geospatial](#geospatial)
        - [Graph](#graph)
        - [SQL/OLAP](#sqlolap)
        - [时间序列](#time-series)
    - [Infrastructure](#infrastructure)
        - [二级指数](#secondary-indices)
        - [Transactions](#transactions)
    - [Integrations](#integrations)
    - [Tools](#tools)
    - [Miscellaneous](#miscellaneous)

- [Resources](#resources)
    - [Books](#books)
    - [Papers](#papers)
    - [Community](#community)

    
## 项目

### 客户

* [asynchbase](https://github.com/OpenTSDB/asynchbase) - 完全异步、非阻塞的 HBase 客户端。
* [gohbase](https://github.com/tsuna/gohbase) - HBase 的 Pure Go 客户端。
* [happybase](https://github.com/wbolster/happybase) - HBase 的 Python 客户端。


### 云

* [Amazon EMR](https://aws.amazon.com/emr/) - AWS 上的 Amazon Hadoop/HBase 产品。
* [Azure HDInsight](https://azure.microsoft.com/en-us/services/hdinsight/) - Azure 上的 Microsoft Hadoop/HBase 产品。
* [Cloudera Director](https://www.cloudera.com/products/product-components/cloudera-director.html) - 在 AWS、Azure 或 Google Cloud 上运行 Hadoop/HBase 集群。
* [Google Cloud Bigtable](https://cloud.google.com/bigtable/) - 可通过 HBase 客户端 API 访问高性能 NoSQL 数据库服务。
* [Hortonworks Cloudbreak](https://hortonworks.com/open-source/cloudbreak/) - 在 AWS、Azure、Google Cloud 或 OpenStack 上配置 Hadoop/HBase 集群。

### 框架

#### 数据集

* [Kite](http://kitesdk.org) - Hadoop/HBase 的高级数据层。

#### 文件

* [HDocDB](https://github.com/rayokota/hdocdb) - HBase 作为 JSON 文档数据库。

#### 实体/JPA

* [DataNucleus](http://www.datanucleus.org) - 支持 HBase 的 JPA 持久层。
* [Gora](http://gora.apache.org) - 支持 HBase 的大数据持久性库。
* [HBase ORM](https://github.com/flipkart-incubator/hbase-orm) - 生产级 HBase ORM 库。
* [HEntityDB](https://github.com/rayokota/hentitydb) - HBase作为实体数据库。
* [Kundera](https://github.com/impetus-opensource/Kundera) - 支持 HBase 的 JPA 客户端。

#### 地理空间

* [GeoMesa](http://www.geomesa.org/) - 支持 Accumulo、HBase、Cassandra 和 Kafka 的时空数据库。

#### 图
* [Gradoop](https://github.com/dbs-leipzig/gradoop) - 基于 Flink 和 HBase 构建的可扩展图形分析研究框架。
* [HGraphDB](https://github.com/rayokota/hgraphdb) - HBase 作为 TinkerPop 图形数据库。
* [HugeGraph](https://github.com/apache/incubator-hugegraph) - 支持超过10+十亿数据的图数据库，高性能、可扩展。
* [JanusGraph](http://janusgraph.org/) - 可扩展的图形数据库，支持 Cassandra、HBase、Google Cloud Bigtable 和 BerkeleyDB。
* [NebulaGraph](https://github.com/vesoft-inc/nebula) - 高性能分布式图数据库。
* [S2Graph](http://s2graph.incubator.apache.org) - 基于HBase构建的高性能分布式图数据库。
* [Actionbase](https://github.com/kakao/actionbase) - 以图表形式表示的用户交互（点赞、查看、关注）的数据库，并实时提供预先计算的读取。

#### SQL/OLAP

* [AntsDB](http://antsdb.com/) - AntsDB 是 HBase 的低延迟、高并发、兼容 MySQL 的 SQL 层。
* [EsgynDB](https://esgyn.com/) - 商业 SQL 引擎基于 Trafodian，在 Hadoop 之上提供 ACID 事务和 BI 分析。
* [Kylin](http://kylin.apache.org) - 用于将数据存储在 HBase 中的大数据的 Extreme OLAP 引擎。
* [LeanXScale](http://www.leanxcale.com) - 基于 Hadoop/HBase 构建的商业完整 ACID 完整 SQL 产品。
* [Phoenix](https://phoenix.apache.org) - HBase 之上的 SQL 层。
* [Splice Machine](https://www.splicemachine.com) - 构建在 HBase 之上的商业 RDBMS。
* [Trafodian](http://trafodion.apache.org) - Hadoop/HBase 上的事务 SQL。

#### 时间序列

* [Axibase](http://axibase.com/products/axibase-time-series-database/) - 基于HBase构建的分布式时序数据库。
* [OpenTSDB](http://opentsdb.net) - 基于 HBase 构建的可扩展时间序列数据库。
* [Warp 10](http://www.warp10.io) - 传感器数据的时间序列数据库。

### 基础设施

#### 二级指数

* [hindex](https://github.com/Huawei-Hadoop/hindex) - HBase 的二级索引。
* [Lily HBase Indexer](http://ngdata.github.io/hbase-indexer/) - 快速轻松地搜索 HBase 中存储的内容。

#### 交易

* [Haeinsa](https://github.com/VCNC/haeinsa) - HBase 的多行/多表事务库。
* [HBase-QoD](https://github.com/algarecu/hbase-0.94.8-qod) - HBase 细粒度事务 DC 间复制的向量场一致性。
* [Omid](https://github.com/apache/incubator-omid) - HBase 的事务支持。
* [Tephra](http://tephra.incubator.apache.org) - HBase 之上的全局一致事务。
* [Themis](https://github.com/XiaoMi/themis) - 基于Google Percolator的HBase上的跨行/跨表事务。

### 集成

* [Apex](https://github.com/apache/apex-malhar/tree/master/contrib/src/test/java/org/apache/apex/malhar/contrib/hbase) - Apex-HBase 连接器。
* [Beam](https://github.com/apache/beam/tree/master/sdks/java/io/hbase) - Beam HBase 集成。
* [Camel](http://camel.apache.org/hbase.html) - 骆驼 HBase 组件。
* [Cascading](https://github.com/Cascading/cascading.hbase) - 用于级联的 HBase 适配器。
* [Cascalog](https://github.com/sorenmacbeth/hbase-cascalog) - Cascading.HBase 的包装，用于 Cascalog。
* [Crunch](https://github.com/apache/crunch/tree/master/crunch-hbase) - 适用于 Crunch 的 HBase 适配器。
* [Drill](https://drill.apache.org/docs/querying-hbase/) - Drill 的 HBase 存储插件。
* [Elasticsearch](https://github.com/mallocator/Elasticsearch-HBase-River) - Elasticsearch 为 HBase 导入河流。
* [Flink](https://github.com/apache/flink/tree/master/flink-connectors/flink-connector-hbase-2.2) - Flink-HBase 连接器。
* [Gearpump](https://github.com/apache/incubator-gearpump/tree/master/external/hbase) - HBase 的齿轮泵集成。
* [Giraph](https://github.com/apache/giraph/tree/trunk/giraph-hbase) - HBase 的 Giraph 输入和输出格式。
* [HAWQ](https://hawq.apache.org/docs/userguide/2.3.0.0-incubating/pxf/HBasePXF.html) - HBase 上的 HAWQ PXF 外部表。
* [Hive](https://cwiki.apache.org/confluence/display/Hive/HBaseIntegration) - Hive HBase 集成。
* [Impala](https://www.cloudera.com/documentation/enterprise/latest/topics/impala_hbase.html) - Impala 支持查询 HBase 表。
* [Kafka](https://github.com/apache/hbase-connectors/tree/master/kafka) - HBase Kafka 代理。
* [Pig](https://github.com/apache/pig/tree/trunk/src/org/apache/pig/backend/hadoop/hbase) - Pig HBase 集成。
* [Presto](https://github.com/analysys/presto-hbase-connector) - Presto-HBase 连接器。
* [Pulsar](http://pulsar.apache.org/docs/en/io-hbase/) - Pulsar 的 HBase 连接器。
* [Ranger](https://cwiki.apache.org/confluence/display/RANGER/HBase+Plugin) - Apache Ranger 的 HBase 插件。
* [Spark](https://github.com/hortonworks-spark/shc) - Spark-HBase 连接器。
* [Spring for Apache Hadoop](https://projects.spring.io/spring-hadoop/) - Spring-Hadoop 集成，包括 HBase 支持。
* [Storm](https://github.com/apache/storm/tree/master/external/storm-hbase) - HBase 的 Storm/Trident 集成。
* [Tajo](https://tajo.apache.org/docs/current/hbase_integration.html) - Tajo 与 HBase 集成。
* [Zeppelin](https://zeppelin.apache.org/docs/0.6.2/interpreter/hbase.html) - Apache Zeppelin 的 HBase shell 解释器。

### 工具

* [Ambari](https://ambari.apache.org) - 用于配置、管理和监控 Hadoop/HBase 集群的软件。
* [Cloudera Manager](https://www.cloudera.com/products/product-components/cloudera-manager.html) - 用于在生产环境中管理 Hadoop/HBase 的工具。
* [DbSchema](http://www.dbschema.com/index.html) - 面向图表的数据库设计器，支持 HBase。
* [Hannibal](https://github.com/sentric/hannibal) - 用于监控和维护 HBase 集群的工具。
* [h-rider](https://github.com/NiceSystems/hrider) - 用于查看和操作 HBase 中数据的 GUI。
* [Hue](http://gethue.com) - 包含 HBase 浏览器的智能分析工作台。
* [Sematext SPM](http://sematext.com/spm) - 用于[监控HBase](http://sematext.com/spm/integrations/hbase-monitoring)、HDFS等的工具。

### 杂项

* [HubSpot HBase support](https://github.com/HubSpot/hbase-support) - HubSpot 上的 HBase 配置和工具，包括 Hystrix 集成和协处理器。

## 资源

### 书籍

* [HBase in Action](https://www.manning.com/books/hbase-in-action) - 经验驱动的指南，向您展示如何使用 HBase。
* [HBase: The Definitive Guide](http://shop.oreilly.com/product/0636920014348.do) - HBase 综合指南。
* [Architecting HBase Applications](http://shop.oreilly.com/product/0636920035688.do) - 包括 HBase 原理、集群指南和深入的案例研究。
* [HBase Administration Cookbook](https://www.packtpub.com/big-data-and-business-intelligence/hbase-administration-cookbook) - 如何掌握 HBase 配置和管理。
* [HBase Essentials](https://www.packtpub.com/big-data-and-business-intelligence/hbase-essentials) - 使用 HBase 的实用指南。
* [HBase Design Patterns](https://www.packtpub.com/big-data-and-business-intelligence/hbase-design-patterns) - 使用 HBase 开发可扩展应用程序的成功模式。
* [Learning HBase](https://www.packtpub.com/big-data-and-business-intelligence/learning-hbase) - 了解 HBase 管理和开发的基础知识。
* [HBase High Performance Cookbook](https://www.packtpub.com/big-data-and-business-intelligence/hbase-high-performance-cookbook) - 教您如何使用 HBase 的激动人心的项目。
* [Apache HBase Primer](http://www.apress.com/us/book/9781484224236) - HBase 要点的紧凑指南。
* [Pro Apache Phoenix](http://www.apress.com/us/book/9781484223697) - 使用 Phoenix 的基本和最佳实践。
* [Mathematics of Big Data](https://mitpress.mit.edu/9780262038393/mathematics-of-big-data/) - HBase 等宽列存储背后的数学理论。

### 论文

* [Bigtable: A Distributed Storage System for Structured Data](https://static.googleusercontent.com/media/research.google.com/en//archive/bigtable-osdi06.pdf) - HBase 的灵感。
* [Apache Hadoop Goes Realtime at Facebook](https://pdfs.semanticscholar.org/865a/215390cd49af9e4941e03107120e631dcaa0.pdf) - Facebook 如何将 HBase 部署到生产中。

### 社区

* [Blog](https://blogs.apache.org/hbase/)
* [邮件列表](http://hbase.apache.org/mail-lists.html)
* [Reddit](https://www.reddit.com/r/hbase/)
* [堆栈溢出](https://stackoverflow.com/questions/tagged/hbase)
* [Twitter](https://twitter.com/HBase)

## 许可证

<p xmlns:dct="http://purl.org/dc/terms/">
<a rel="license" href="http://creativecommons.org/publicdomain/mark/1.0/">
<img src="https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/publicdomain.svg"
样式=“边框样式：无；” alt="公共领域标记"/>
</a>
