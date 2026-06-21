# 很棒的大数据

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

精彩的大数据框架、资源和其他精彩内容的精选列表。灵感来自 [awesome-php](https://github.com/ziadoz/awesome-php)、[awesome-python](https://github.com/vinta/awesome-python)、[awesome-ruby](https://github.com/Sdogruyol/awesome-ruby)、[hadoopecosystemtable](http://hadoopecosystemtable.github.io/) & [大数据](http://usefulstuff.io/big-data/)。

随时欢迎您的贡献！

- [很棒的大数据](#awesome-big-data)
  - [RDBMS](#rdbms)
  - [Frameworks](#frameworks)
  - [分布式编程](#distributed-programming)
  - [分布式文件系统](#distributed-filesystem)
  - [分布式索引](#distributed-index)
  - [文档数据模型](#document-data-model)
  - [键映射数据模型](#key-map-data-model)
  - [键值数据模型](#key-value-data-model)
  - [图数据模型](#graph-data-model)
  - [列式数据库](#columnar-databases)
  - [新SQL数据库](#newsql-databases)
  - [时间序列数据库](#time-series-databases)
  - [Lakehouse 表格式](#lakehouse-table-formats)
  - [类似SQL的处理](#sql-like-processing)
  - [矢量数据库](#vector-databases)
  - [数据摄取](#data-ingestion)
  - [数据质量和可观察性](#data-quality-and-observability)
  - [服务编程](#service-programming)
  - [Scheduling](#scheduling)
  - [机器学习](#machine-learning)
  - [Benchmarking](#benchmarking)
  - [Security](#security)
  - [系统部署](#system-deployment)
  - [Applications](#applications)
  - [搜索引擎和框架](#search-engine-and-framework)
  - [MySQL 的分支和演变](#mysql-forks-and-evolutions)
  - [PostgreSQL 的分叉和演变](#postgresql-forks-and-evolutions)
  - [Memcached 分叉和演变](#memcached-forks-and-evolutions)
  - [嵌入式数据库](#embedded-databases)
  - [商业智能](#business-intelligence)
  - [数据可视化](#data-visualization)
  - [物联网和传感器数据](#internet-of-things-and-sensor-data)
  - [有趣的读物](#interesting-readings)
  - [有趣的论文](#interesting-papers)
    - [2015 - 2016](#2015---2016)
    - [2013 - 2014](#2013---2014)
    - [2011 - 2012](#2011---2012)
    - [2001 - 2010](#2001---2010)
  - [Videos](#videos)
  - [Books](#books)
      - [Streaming](#streaming)
      - [分布式系统](#distributed-systems)
      - [基于图的方法](#graph-based-approach)
    - [数据可视化](#data-visualization-1)
- [其他很棒的清单](#other-awesome-lists)

## 关系型数据库管理系统
* [MySQL](https://www.mysql.com/) 全球最流行的开源数据库。
* [PostgreSQL](https://www.postgresql.org/) 世界上最先进的开源数据库。
* [Oracle Database](http://www.oracle.com/us/corporate/features/database-12c/index.html) - 对象关系数据库管理系统。
* [Teradata](http://www.teradata.com/products-and-services/teradata-database/) - 高性能MPP数据仓库平台。

## 框架

* [Bistro](https://github.com/facebook/bistro) - 用于批处理和流分析的通用数据处理引擎。它基于一种新颖的数据模型，通过“函数”表示数据并通过“列操作”处理数据，而不是像 MapReduce 或 SQL 等传统方法中仅进行设置操作。
* [IBM Streams](https://www.ibm.com/analytics/us/en/technology/stream-computing/) - 用于分布式处理和实时分析的平台。  与大数据生态系统中的许多流行技术集成（Kafka、HDFS、Spark等）
* [Apache Hadoop](http://hadoop.apache.org/) - 分布式处理框架。集成 MapReduce（并行处理）、YARN（作业调度）和 HDFS（分布式文件系统）。
* [Tigon](https://github.com/caskdata/tigon) - 高吞吐量实时流处理框架。
* [Numaflow](https://github.com/numaproj/numaflow) - Kubernetes-原生流处理平台。
* [Pachyderm](http://pachyderm.io/) - Pachyderm 是一个基于 Docker 和 Kubernetes 构建的数据存储平台，提供可重复的数据处理和分析。
* [Polyaxon](https://github.com/polyaxon/polyaxon) - 一个用于可重复和可扩展的机器学习和深度学习的平台。
* [Smooks](https://github.com/smooks/smooks) - 用于构建 XML 和非 XML（CSV、EDI、Java 等）流应用程序的可扩展 Java 框架。

## 分布式编程

* [AddThis Hydra](https://github.com/addthis/hydra) - 分布式数据处理和存储系统最初是在 AddThis 开发的。
* [AMPLab SIMR](http://databricks.github.io/simr/) - 在 Hadoop MapReduce v1 上运行 Spark
* [Apache APEX](https://apex.apache.org/) - 用于大数据流和批处理的统一企业平台。
* [Apache Beam](https://beam.apache.org/) - 用于定义和执行数据处理工作流程的统一模型和一组特定于语言的 SDK。
* [Apache Crunch](http://crunch.apache.org/) - 一个简单的 Java API，用于执行连接和数据聚合等任务，这些任务在普通 MapReduce 上实现起来很繁琐。
* [Apache DataFu](http://incubator.apache.org/projects/datafu.html) - 由 LinkedIn 开发的 Hadoop 和 Pig 的用户定义函数集合。
* [Apache Flink](http://flink.apache.org/) - 高性能运行时，自动程序优化。
* [Apache Gearpump](https://gearpump.github.io/gearpump/) - 基于Akka的实时大数据流引擎。
* [Apache Gora](http://gora.apache.org/) - 内存数据模型和持久性框架。
* [Apache Hama](http://hama.apache.org/) - BSP（批量同步并行）计算框架。
* [Apache MapReduce](https://wiki.apache.org/hadoop/MapReduce/) - 用于在集群上使用并行分布式算法处理大型数据集的编程模型。
* [Apache Pig](https://pig.apache.org/) - 用于表达 Hadoop 数据分析程序的高级语言。
* [Apache REEF](http://reef.apache.org/) - 可保留的评估器执行框架，用于简化和统一大数据系统的较低层。
* [Apache S4](http://incubator.apache.org/projects/s4.html) - 流处理框架，S4 的实现。
* [Apache Spark](http://spark.apache.org/) - 内存集群计算框架。
* [Apache Spark Streaming](https://spark.apache.org/docs/latest/streaming-programming-guide.html) - 流处理框架，Spark 的一部分。
* [Apache Storm](http://storm.apache.org) - Twitter 也在 YARN 上提供流处理框架。
* [Apache Samza](http://samza.apache.org/) - 流处理框架，基于Kafka和YARN。
* [Apache Tez](http://tez.apache.org/) - 用于执行基于 YARN 的复杂 DAG（有向无环图）任务的应用程序框架。
* [Apache Twill](https://incubator.apache.org/projects/twill.html) - 对 YARN 的抽象，降低了开发分布式应用程序的复杂性。
* [Baidu Bigflow](http://bigflow.cloud/en/index.html) - 一个允许编写分布式计算程序的接口，提供大量简单、灵活、强大的 API 来轻松处理任何规模的数据。
* [Cascalog](http://cascalog.org/) - 数据处理和查询库。
* [Cheetah](http://vldbarc.org/pvldb/vldb2010/pvldb_vol3/I08.pdf) - 基于 MapReduce 的高性能、自定义数据仓库。
* [Concurrent Cascading](http://www.cascading.org/) - Hadoop 上的数据管理/分析框架。
* [Damballa Parkour](https://github.com/damballa/parkour) - Clojure 的 MapReduce 库。
* [Datasalt Pangool](https://github.com/datasalt/pangool) - 另一种 MapReduce 范式。
* [DataTorrent StrAM](https://www.datatorrent.com/) - 实时引擎旨在以尽可能畅通无阻的方式实现分布式、异步、实时内存中大数据计算，同时将开销和对性能的影响降至最低。
* [Facebook Corona](https://www.facebook.com/notes/facebook-engineering/under-the-hood-scheduling-mapreduce-jobs-more-efficiently-with-corona/10151142560538920) - Hadoop 增强功能消除了单点故障。
* [Facebook Peregrine](http://peregrine_mapreduce.bitbucket.org/) - 映射减少框架。
* [Facebook Scuba](https://www.facebook.com/notes/facebook-engineering/under-the-hood-data-diving-with-scuba/10150599692628920) - 分布式内存数据存储。
* [Google Dataflow](https://googledevelopers.blogspot.it/2014/06/cloud-platform-at-google-io-new-big.html) - 创建数据管道来帮助他们摄取、转换和分析数据。
* [Google MapReduce](https://research.google.com/archive/mapreduce.html) - 地图缩减框架。
* [Google MillWheel](https://research.google.com/pubs/pub41378.html) - 容错流处理框架。
* [IBM Streams](https://www.ibm.com/analytics/us/en/technology/stream-computing/) - 用于分布式处理和实时分析的平台。  提供开箱即用的高级分析工具包，例如地理空间、时间序列等。
* [JAQL](https://code.google.com/p/jaql/) - 用于处理结构化、半结构化和非结构化数据的声明性编程语言。
* [Kite](http://kitesdk.org/docs/current/) - 是一组库、工具、示例和文档，致力于让您更轻松地在 Hadoop 生态系统之上构建系统。
* [Metamarkets Druid](http://druid.io/) - 大型数据集实时分析框架。
* [Netflix PigPen](https://github.com/Netflix/PigPen) - Clojure 的 map-reduce，可编译为 Apache Pig。
* [Nokia Disco](http://discoproject.org/) - MapReduce 框架由诺基亚开发。
* [Onyx](http://www.onyxplatform.org/) - 云的分布式计算。
* [Pinterest Pinlater](https://medium.com/@Pinterest_Engineering/pinlater-an-asynchronous-job-execution-system-b8664cb8aa7d) - 异步作业执行系统。
* [Pydoop](http://crs4.github.io/pydoop/) - 适用于 Hadoop 的 Python MapReduce 和 HDFS API。
* [Ray](https://github.com/ray-project/ray) - 用于构建和运行分布式应用程序的快速而简单的框架。
* [Rackerlabs Blueflood](http://blueflood.io/) - 多租户分布式度量处理系统
* [Skale](https://github.com/skale-me/skale-engine) - NodeJS 中的高性能分布式数据处理。
* [Stratosphere](http://stratosphere.eu/) - 通用集群计算框架。
* [Streamdrill](https://streamdrill.com/) - 对于计算不同时间窗口内事件流的活动并找到最活跃的活动非常有用。
* [streamsx.topology](https://github.com/IBMStreams/streamsx.topology) - 支持使用 Java、Python 或 Scala 构建 IBM Streams 应用程序的库。
* [Tuktu](https://github.com/UnderstandLingBV/Tuktu) - 易于使用的批处理和流计算平台，使用 Scala、Akka 和 Play 构建！
* [Twitter Heron](https://github.com/twitter/heron) - Heron 是 Twitter 推出的实时、分布式、容错流处理引擎，取代了 Storm。
* [Twitter Scalding](https://github.com/twitter/scalding) - 用于 MapReduce 作业的 Scala 库，基于 Cascading 构建。
* [Twitter Summingbird](https://github.com/twitter/summingbird) - 使用 Scalding 和 Storm 流式传输 MapReduce，作者：Twitter。
* [Twitter TSAR](https://blog.twitter.com/engineering/en_us/a/2014/tsar-a-timeseries-aggregator.html) - Twitter 的 TimeSeries AggregatoR。
* [Wallaroo](http://www.wallaroolabs.com/community) - 超快且富有弹性的数据处理引擎。大数据或快速数据 - 无需大惊小怪，无需 Java。

## 分布式文件系统

* [Ambry](https://github.com/linkedin/ambry) - 分布式对象存储，支持存储数万亿个小型不可变对象以及数十亿个大型对象。
* [Apache HDFS](http://hadoop.apache.org/) - 一种跨多台机器存储大文件的方法。
* [Apache Kudu](http://kudu.apache.org/) - Hadoop 的存储层可实现对快速数据的快速分析。
* [BeeGFS](https://www.beegfs.io/content/) - 以前称为FhGFS，并行分布式文件系统。
* [Ceph Filesystem](http://ceph.com/ceph-storage/file-system/) - 软件存储平台设计。
* [Disco DDFS](http://disco.readthedocs.org/en/latest/howto/ddfs.html) - 分布式文件系统。
* [Facebook Haystack](https://www.facebook.com/note.php?note_id=76191543919) - 对象存储系统。
* [Google GFS](http://static.googleusercontent.com/media/research.google.com/en//archive/gfs-sosp2003.pdf) - 分布式文件系统。
* [Google Megastore](https://research.google.com/pubs/pub36971.html) - 可扩展、高可用的存储。
* [GridGain](https://www.gridgain.com/) - GGFS，兼容 Hadoop 的内存文件系统。
* [JuiceFS](https://github.com/juicedata/juicefs) - 基于对象存储构建的分布式 POSIX 文件系统。
* [Lustre file system](http://wiki.lustre.org/) - 高性能分布式文件系统。
* [Microsoft Azure Data Lake Store](https://hadoop.apache.org/docs/current/hadoop-azure-datalake/index.html) - Azure 云中与 HDFS 兼容的存储
* [Quantcast File System QFS](https://www.quantcast.com/about-us/quantcast-file-system/) - 开源分布式文件系统。
* [Red Hat GlusterFS](http://gluster.org/) - 横向扩展网络附加存储文件系统。
* [Seaweed-FS](https://github.com/chrislusf/seaweedfs) - 简单且高度可扩展的分布式文件系统。
* [Alluxio](http://www.alluxio.org/) - 跨集群框架以内存速度可靠地共享文件。
* [Tahoe-LAFS](https://www.tahoe-lafs.org/trac/tahoe-lafs) - 去中心化的云存储系统。
* [Baidu File System](https://github.com/baidu/bfs) - 分布式文件系统。

## 分布式索引

* [Pilosa](https://github.com/pilosa/pilosa) 开源分布式位图索引，可显着加速跨多个海量数据集的查询。

## 文档数据模型

* [Actian Versant](https://www.actian.com/data-management/ingres-sql-rdbms/) - 商业面向对象的数据库管理系统。
* [Crate Data](https://crate.io/) - 是一个开源的可大规模扩展的数据存储。它需要零管理。
* [Facebook Apollo](http://www.infoq.com/news/2014/06/facebook-apollo) - Facebook 的类似 Paxos 的 NoSQL 数据库。
* [jumboDB](http://comsysto.github.io/jumbodb/) - Hadoop 上的面向文档的数据存储。
* [LinkedIn Espresso](https://engineering.linkedin.com/data) - 水平可扩展的面向文档的 NoSQL 数据存储。
* [MarkLogic](http://www.marklogic.com/) - 与架构无关的企业 NoSQL 数据库技术。
* [Microsoft Azure DocumentDB](https://azure.microsoft.com/en-us/services/cosmos-db/) - 具有 MongoDB 协议支持的 NoSQL 云数据库服务
* [MongoDB](https://www.mongodb.com/) - 面向文档的数据库系统。
* [RavenDB](https://ravendb.net/) - 事务性开源文档数据库。
* [RethinkDB](https://rethinkdb.com/) - 支持表连接和分组等查询的文档数据库。

## 键映射数据模型

**注意**：业界存在一些术语混淆，有两种不同的东西被称为“列式数据库”。这里列出的一些是围绕“键映射”数据模型构建的分布式持久数据库：所有数据都有一个（可能是复合的）键，与键值对的映射相关联。在一些系统中，多个这样的值映射可以与一个键相关联，并且这些映射被称为“列族”（值映射键被称为“列”）。

另一组技术也可以称为“列式数据库”，其特征在于它如何在磁盘或内存中存储数据，而不是以传统方式存储数据，即给定键的所有列值“逐行”地彼此相邻存储，这些系统将所有“列”值彼此相邻存储。因此，需要更多的工作来获取给定键的所有列，但需要更少的工作来获取给定列的所有值。

前一组在此被称为“键映射数据模型”。这些和[键值数据模型](#key-value-data-model)存储之间的界限相当模糊。

后者更多地涉及存储格式而不是数据模型，列在[列式数据库](#columnar-databases)下。

您可以在 Daniel Abadi 教授的博客上了解有关这种区别的更多信息：[区分列存储的两种主要类型](http://dbmsmusings.blogspot.com/2010/03/distinguishing-two-major-types-of_29.html)。

* [Apache Accumulo](http://accumulo.apache.org/) - 基于 Hadoop 构建的分布式键/值存储。
* [Apache Cassandra](http://cassandra.apache.org/) - 受 BigTable 启发的面向列的分布式数据存储。
* [Apache HBase](http://hbase.apache.org/) - 受 BigTable 启发的面向列的分布式数据存储。
* [Baidu Tera](https://github.com/baidu/tera) - 受 BigTable 启发的互联网规模数据库。
* [Facebook HydraBase](https://code.facebook.com/posts/321111638043166/hydrabase-the-evolution-of-hbase-facebook/) - Facebook 制作的 HBase 的演变。
* [Google BigTable](http://static.googleusercontent.com/media/research.google.com/en//archive/bigtable-osdi06.pdf) - 面向列的分布式数据存储。
* [Google Cloud Datastore](https://cloud.google.com/datastore/docs/concepts/overview) - 是一个完全托管的无模式数据库，用于通过 BigTable 存储非关系数据。
* [Hypertable](http://www.hypertable.org/) - 受 BigTable 启发的面向列的分布式数据存储。
* [InfiniDB](https://github.com/infinidb/infinidb/) - 通过MySQL接口访问并使用大规模并行处理来并行化查询。
* [Tephra](https://github.com/caskdata/tephra) - HBase 的事务。
* [Twitter Manhattan](https://blog.twitter.com/engineering/en_us/a/2014/manhattan-our-real-time-multi-tenant-distributed-database-for-twitter-scale.html) - Twitter 规模的实时、多租户分布式数据库。
* [ScyllaDB](http://www.scylladb.com/) - 用 C++ 编写的面向列的分布式数据存储，与 Apache Cassandra 完全兼容。


## 键值数据模型

* [Aerospike](http://www.aerospike.com/) - NoSQL 闪存优化、内存中。开源和“‘C’（不是 Java 或 Erlang）服务器代码经过精确调整，以避免上下文切换和内存复制。”
* [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) - 分布式键/值存储，Dynamo paper 的实现。
* [Badger](https://open.dgraph.io/post/badger/) - 一个用 Go 原生编写的快速、简单、高效且持久的键值存储。
* [Bolt](https://github.com/boltdb/bolt) - Go 的嵌入式键值数据库。
* [BTDB](https://github.com/Bobris/BTDB) - .Net 中的键值数据库，具有对象 DB 层、RPC、动态 IL 等
* [BuntDB](https://github.com/tidwall/buntdb) - 一个用于 Go 的快速、可嵌入、内存中键/值数据库，具有自定义索引和地理空间支持。
* [Edis](https://github.com/cbd/edis) - 是 Redis 的协议兼容服务器替代品。
* [ElephantDB](https://github.com/nathanmarz/elephantdb) - 专门从 Hadoop 导出数据的分布式数据库。
* [EventStore](https://geteventstore.com/) - 分布式时间序列数据库。
* [GhostDB](https://github.com/jakekgrog/GhostDB) - 分布式、内存中、通用键值数据存储，可在任何规模下提供微秒级性能。
* [Graviton](https://github.com/deroproject/graviton) - 纯 Go(lang) 中的简单、快速、版本控制、经过身份验证、可嵌入的键值存储数据库。
* [GridDB](https://github.com/griddb/griddb_nosql) - 适用于存储在时间序列中的传感器数据。
* [HyperDex](https://github.com/rescrv/HyperDex) - 可扩展的下一代键值和文档存储，具有广泛的功能，包括一致性、容错性和高性能。
* [Ignite](https://ignite.apache.org/index.html) - 是一种内存中键值数据存储，提供完全符合 SQL 的数据访问，可以选择由磁盘存储支持。
* [LinkedIn Krati](https://github.com/linkedin-sna/sna-page/tree/master/krati) - 是一个简单的持久数据存储，具有非常低的延迟和高吞吐量。
* [Linkedin Voldemort](http://www.project-voldemort.com/voldemort/) - 分布式键/值存储系统。
* [Oracle NoSQL Database](http://www.oracle.com/technetwork/database/database-technologies/nosqldb/overview/index.html) - Oracle 公司的分布式键值数据库。
* [Redis](https://redis.io/) - 内存中的键值数据存储。
* [Riak](https://github.com/basho/riak) - 分散的数据存储。
* [Storehaus](https://github.com/twitter/storehaus) - Twitter 提供的用于处理异步键值存储的库。
* [SummitDB](https://github.com/tidwall/summitdb) - 内存中的 NoSQL 键/值数据库，具有磁盘持久性并使用 Raft 共识算法。
* [Tarantool](https://github.com/tarantool/tarantool) - 高效的NoSQL数据库和Lua应用服务器。
* [TiKV](https://github.com/pingcap/tikv) - 由 Rust 提供支持并受到 Google Spanner 和 HBase 启发的分布式键值数据库。
* [Tile38](https://github.com/tidwall/tile38) - 地理位置数据存储、空间索引和实时地理围栏，支持各种对象类型，包括纬度/经度点、边界框、XYZ 切片、Geohashes 和 GeoJSON
* [TreodeDB](https://github.com/Treode/store) - 可复制和分片并提供原子多行写入的键值存储。


## 图数据模型

* [Actionbase](https://github.com/kakao/actionbase) - 用于用户交互（喜欢、查看、关注）并预先计算读取的数据库，支持 HBase。
* [AgensGraph](https://github.com/bitnine-oss/agensgraph) - 基于 PostgreSQL 的事务型图数据库。
* [ArcadeDB](https://arcadedb.com/) - 具有图形、文档、键值、时间序列和向量支持的多模型数据库。
* [Apache Spark Bagel](http://spark.apache.org/docs/0.7.3/bagel-programming-guide.html) - Pregel 的实现，是 Spark 的一部分。
* [ArangoDB](https://www.arangodb.com/) - 多模型分布式数据库。
* [DGraph](https://github.com/dgraph-io/dgraph) - 一个可扩展、分布式、低延迟、高吞吐量的图形数据库，旨在提供 Google 生产级别的规模和吞吐量，并以足够低的延迟为超过 TB 的结构化数据提供实时用户查询服务。
* [EliasDB](https://github.com/krotik/eliasdb) - 一个基于图形的轻量级数据库，不需要任何第三方库。
* [Facebook TAO](https://engineering.fb.com/2013/06/25/core-infra/tao-the-power-of-the-graph/) - TAO 是 Facebook 广泛使用的分布式数据存储，用于存储和服务社交图谱。
* [GCHQ Gaffer](https://github.com/gchq/Gaffer) - GCHQ 的 Gaffer 是一个框架，可以轻松存储节点和边具有统计数据的大规模图。
* [Google Cayley](https://github.com/cayleygraph/cayley) - 开源图数据库。
* [Google Pregel](http://kowshik.github.io/JPregel/pregel_paper.pdf) - 图处理框架。
* [GraphX](https://amplab.cs.berkeley.edu/publication/graphx-grades/) - Spark 上的弹性分布式图系统。
* [Gremlin](https://github.com/tinkerpop/gremlin) - 图遍历语言。
* [Infovore](https://github.com/paulhoule/infovore) - 以 RDF 为中心的 Map/Reduce 框架。
* [JanusGraph](http://janusgraph.org) - 开源分布式图数据库
具有多种存储后端选项（Bigtable、HBase、Cassandra 等）
和索引后端（Elasticsearch、Solr、Lucene）。
* [Microsoft Graph Engine](https://github.com/Microsoft/GraphEngine) - 分布式内存数据处理引擎，由强类型内存键值存储和通用分布式计算引擎支撑。
* [Nebula Graph](https://www.nebula-graph.io/) - 用于低延迟查询的大规模图形的分布式图形数据库。
* [Neo4j](https://neo4j.com/) - 完全用 Java 编写的图形数据库。
* [OrientDB](http://orientdb.com/) - 文档和图形数据库。
* [Phoebus](https://github.com/xslogic/phoebus) - 大规模图形处理框架。
* [Titan](http://thinkaurelius.github.io/titan/) - 分布式图形数据库，基于 Cassandra 构建。


## 列式数据库

**注意** 请阅读 [Key-Map Data Model](#key-map-data-model) 部分的注释。

* [Columnar Storage](http://the-paper-trail.org/blog/columnar-storage/) - 解释什么是列式存储以及何时需要它。
* [Actian Vector](http://www.actian.com/) - 面向列的分析数据库。
* [ClickHouse](https://clickhouse.com/) - 一个面向列的开源数据库管理系统，可以实时生成分析数据报告。
* [EventQL](http://eventql.io/) - 专为大规模事件收集和分析而构建的分布式、面向列的数据库。
* [MonetDB](https://www.monetdb.org/) - 列存储数据库。
* [Parquet](http://parquet.apache.org/) - Hadoop 的列式存储格式。
* [Pivotal Greenplum](https://pivotal.io/pivotal-greenplum) - 专门构建的专用分析数据仓库，提供列式引擎以及传统的基于行的引擎。
* [Vertica](https://www.vertica.com/) - 旨在管理大量快速增长的数据，并在用于数据仓库时提供非常快的查询性能。
* [SQream DB](http://sqream.com/) - 由 GPU 驱动的大数据数据库，专为分析和数据仓储而设计，采用符合 ANSI-92 的 SQL，适用于 10TB 到 1PB 的数据集。
* [Google BigQuery](https://cloud.google.com/bigquery/what-is-bigquery) - Google 的云产品以 Dremel 的开创性工作为后盾。
* [Amazon Redshift](https://aws.amazon.com/redshift/) - 亚马逊的云产品也基于列式数据存储后端。
* [IndexR](https://github.com/shunfei/indexr) - 一种开源列式存储格式，用于快速实时分析大数据。
* [LocustDB](https://github.com/cswinter/LocustDB) - 一个实验性分析数据库，旨在为商用硬件上的查询性能设定新标准。

## 新SQL数据库

* [Actian Ingres](http://www.actian.com/products/operational-databases/) - 商业支持的开源 SQL 关系数据库管理系统。
* [ActorDB](https://github.com/biokoda/actordb) - 分布式 SQL 数据库，具有 KV 存储的可扩展性，同时保留关系数据库的查询功能。
* [Amazon RedShift](http://aws.amazon.com/redshift/) - 数据仓库服务，基于PostgreSQL。
* [BayesDB](https://github.com/probcomp/BayesDB) - 面向统计的 SQL 数据库。
* [Bedrock](http://bedrockdb.com/) - 构建在 SQLite 之上的简单、模块化、网络化和分布式事务层。
* [CitusDB](https://www.citusdata.com/) - 通过分片和复制横向扩展 PostgreSQL。
* [Cockroach](https://github.com/cockroachdb/cockroach) - 可扩展、地理复制、事务性数据存储。
* [Comdb2](https://github.com/bloomberg/comdb2) - 基于乐观并发控制技术的集群 RDBMS。
* [Datomic](http://www.datomic.com/) - 分布式数据库旨在支持可扩展、灵活和智能的应用程序。
* [FoundationDB](https://foundationdb.com/) - 分布式数据库，灵感来自 F1。
* [Google F1](https://research.google.com/pubs/pub41344.html) - 基于 Spanner 构建的分布式 SQL 数据库。
* [Google Spanner](https://research.google.com/archive/spanner.html) - 全球分布式半关系数据库。
* [H-Store](http://hstore.cs.brown.edu/) - 是一个实验性主存并行数据库管理系统，针对联机事务处理 (OLTP) 应用程序进行了优化。
* [Haeinsa](https://github.com/VCNC/haeinsa) - 基于 Percolator 的 HBase 线性可扩展多行、多表事务库。
* [HandlerSocket](https://www.percona.com/doc/percona-server/5.5/performance/handlersocket.html) - MySQL/MariaDB 的 NoSQL 插件。
* [InfiniSQL](http://www.infinisql.org/) - 无限可扩展的 RDBMS。
* [KarelDB](https://github.com/rayokota/kareldb) - 由 Apache Kafka 支持的关系数据库。
* [Map-D](https://www.mapd.com/) - GPU内存数据库、大数据分析与可视化平台。
* [MemSQL](http://www.memsql.com/) - 内存中的 SQL 数据库，在闪存上具有优化的列式存储。
* [NuoDB](http://www.nuodb.com/) - SQL/ACID 兼容的分布式数据库。
* [Oracle TimesTen in-Memory Database](http://www.oracle.com/technetwork/database/database-technologies/timesten/overview/index.html) - 具有持久性和可恢复性的内存中关系数据库管理系统。
* [Pivotal GemFire XD](https://gemfire.docs.pivotal.io/93/gemfire/getting_started/gemfire_overview.html) - 低延迟、内存中、分布式 SQL 数据存储。为内存表数据提供 SQL 接口，可持久保存在 HDFS 中。
* [SAP HANA](https://hana.sap.com/abouthana.html) - 是一个内存中、面向列的关系数据库管理系统。
* [SenseiDB](http://senseidb.github.io/sensei/) - 分布式、实时、半结构化数据库。
* [Sky](http://skydb.io/) - 用于对行为数据进行灵活、高性能分析的数据库。
* [SymmetricDS](http://www.symmetricds.org/) - 用于文件和数据库同步的开源软件。
* [TiDB](https://github.com/pingcap/tidb) - TiDB 是一个分布式 SQL 数据库。灵感源自 Google F1 的设计。
* [VoltDB](https://www.voltdb.com/) - 声称是最快的内存数据库。
* [yugabyteDB](https://github.com/YugaByte/yugabyte-db) - 与 PostgreSQL 兼容的开源、高性能、分布式 SQL 数据库。

## 时间序列数据库

* [Axibase Time Series Database](http://axibase.com/products/axibase-time-series-database/) - HBase 之上的集成时间序列数据库，具有内置可视化、规则引擎和 SQL 支持。
* [Chronix](http://chronix.io/) - 时间序列存储，用于存储高度压缩的时间序列并实现快速访问。
* [Cube](http://square.github.io/cube/) - 使用MongoDB来存储时间序列数据。
* [Heroic](https://spotify.github.io/heroic/#!/index) - 是一个基于 Cassandra 和 Elasticsearch 的可扩展时间序列数据库。
* [InfluxDB](https://www.influxdata.com/) - 具有优化 IO 和查询的时间序列数据库，支持 pgsql 和 influx 线协议。
* [QuestDB](https://questdb.io/) - 高性能、开源 SQL 数据库，适用于金融服务、物联网、机器学习、DevOps 和可观测性领域的应用。
* [IronDB](https://www.circonus.com/irondb/) - 可扩展的通用时间序列数据库。
* [Kairosdb](https://github.com/kairosdb/kairosdb) - 与 OpenTSDB 类似，但允许使用 Cassandra。
* [M3DB](https://m3db.io/) - 分布式时间序列数据库，可用于长期保留实时指标。
* [Newts](https://opennms.github.io/newts/) - 基于 Apache Cassandra 的时间序列数据库。
* [TDengine](https://github.com/taosdata/TDengine/) - 具有高性能摄取、SQL 支持和面向 IoT 的存储的开源时间序列数据库。
* [OpenTSDB](http://opentsdb.net) - HBase 之上的分布式时间序列数据库。
* [Prometheus](https://prometheus.io/) - 时间序列数据库和服务监控系统。
* [Beringei](https://github.com/facebookincubator/beringei) - Facebook 的内存时间序列数据库。
* [TrailDB](http://traildb.io/) - 用于存储和查询一系列事件的有效工具。
* [Druid](https://github.com/druid-io/druid/) 面向列的分布式数据存储，非常适合为交互式应用程序提供动力
* [Riak-TS](http://basho.com/products/riak-ts/) Riak TS 是唯一专门针对物联网和时间序列数据优化的企业级 NoSQL 时间序列数据库。
* [Akumuli](https://github.com/akumuli/Akumuli) Akumuli 是一个数字时间序列数据库。它可用于实时捕获、存储和处理时间序列数据。 “akumuli”这个词可以从世界语翻译为“积累”。
* [Rhombus](https://github.com/Pardot/Rhombus) Cassandra 的时间序列对象存储，可处理构建宽行索引的所有复杂性。
* [Dalmatiner DB](https://github.com/dalmatinerdb/dalmatinerdb) 快速分布式指标数据库
* [Blueflood](https://github.com/rackerlabs/blueflood) 一个旨在摄取和处理时间序列数据的分布式系统
* [Timely](https://github.com/NationalSecurityAgency/timely) Timely是一个时间序列数据库应用程序，提供基于Accumulo和Grafana的时间序列数据的安全访问。
* [SiriDB](https://github.com/transceptor-technology/siridb-server) 高度可扩展、强大且快速的开源时间序列数据库，具有集群功能。
* [Thanos](https://github.com/improbable-eng/thanos) - Thanos 是一组组件，用于使用多个（现有）Prometheus 部署创建具有无限存储容量的高度可用的度量系统。
* [VictoriaMetrics](https://github.com/VictoriaMetrics/VictoriaMetrics) - 与 Prometheus 兼容的快速、可扩展且资源高效的开源 TSDB。包括单节点和集群版本

## Lakehouse 表格式

* [Apache Hudi](https://hudi.apache.org/) - 用于高吞吐量增量数据管道的开放数据 Lakehouse 平台和表格式。
* [Apache Iceberg](https://iceberg.apache.org/) - 用于具有模式演化、隐藏分区和时间旅行的大型分析数据集的开放表格式。
* [Apache Paimon](https://paimon.apache.org/) - Lake 格式，用于使用 Flink 和 Spark 构建实时 Lakehouse 架构。
* [Apache XTable](https://xtable.apache.org/) - 正在孵化 Apache 项目，以实现 Lakehouse 表格式之间的互操作性。
* [Delta Lake](https://delta.io/) - 用于在数据湖上构建 Lakehouse 架构的开源存储框架。

## 类似SQL的处理

* [Actian SQL for Hadoop](http://www.actian.com/analytic-database/vectorh-sql-hadoop) - 对所有 Hadoop 数据的高性能交互式 SQL 访问。
* [Apache Doris](https://doris.apache.org/) - 用于高并发 SQL 分析、搜索和仓储的实时分析数据库。
* [Apache Drill](http://drill.apache.org/) - 受 Dremel 启发的交互式分析框架。
* [Apache HCatalog](https://cwiki.apache.org/confluence/display/Hive/HCatalog) - Hadoop 的表和存储管理层。
* [Apache Hive](http://hive.apache.org/) - 用于 Hadoop 的类似 SQL 的数据仓库系统。
* [Apache Calcite](http://calcite.apache.org/) - 允许高效转换涉及异构和联合数据的查询的框架。
* [Apache Phoenix](http://phoenix.apache.org/index.html) - HBase 上的 SQL 皮肤。
* [Aster Database](http://www.teradata.com/products-and-services/Teradata-Aster/teradata-aster-database) - MapReduce 的类 SQL 分析处理。
* [Cloudera Impala](https://www.cloudera.com/products/apache-hadoop/impala.html) - 交互式分析框架，灵感来自 Dremel。
* [Concurrent Lingual](http://www.cascading.org/projects/lingual/) - 用于级联的类似 SQL 的查询语言。
* [Datasalt Splout SQL](http://www.datasalt.com/products/splout-sql/) - 适用于大数据集的完整 SQL 查询引擎。
* [Dremio](https://www.dremio.com/) - 一个基于 Apache Arrow 的开源、类似 SQL 的数据即服务平台。
* [DuckDB](https://duckdb.org/) - 进程内分析 SQL 数据库，用于对文件、数据湖和数据框架进行本地分析。
* [Facebook PrestoDB](https://prestodb.io/) - 分布式SQL查询引擎。
* [Google BigQuery](https://research.google.com/pubs/pub36632.html) - 交互式分析框架，Dremel 的实现。
* [Materialize](https://github.com/materializeinc/materialize) - 是一个用于实时应用程序的流数据库，使用 SQL 进行查询并支持大部分 PostgreSQL。
* [Invantive SQL](https://documentation.invantive.com/2017R2/invantive-sql-grammar/invantive-sql-grammar-17.30.html) - 用于在线和本地使用的 SQL 引擎，具有集成的本地数据复制和 70 多个连接器。
* [PipelineDB](https://www.pipelinedb.com/) - 一个开源关系数据库，它在流上连续运行 SQL 查询，并将结果增量存储在表中。
* [Pivotal HDB](https://pivotal.io/pivotal-hdb) - 适用于 Hadoop 的类似 SQL 的数据仓库系统。
* [rawquery](https://rawquery.dev/) - 使用 DuckDB 通过对象存储上的 Apache Iceberg 表来管理 Lakehouse 查询服务。
* [RainstorDB](http://rainstor.com/products/rainstor-database/) - 用于存储 PB 级结构化和半结构化数据的数据库。
* [Spark Catalyst](https://github.com/apache/spark/tree/master/sql) - 是 Spark 和 Shark 的查询优化框架。
* [SparkSQL](https://databricks.com/blog/2014/03/26/spark-sql-manipulating-structured-data-using-spark-2.html) - 使用 Spark 操作结构化数据。
* [Splice Machine](https://www.splicemachine.com/) - 具有 ACID 事务的全功能 SQL-on-Hadoop RDBMS。
* [StarRocks](https://www.starrocks.io/) - 用于实时分析和 Lakehouse 查询的高性能 MPP SQL 引擎。
* [Stinger](https://hortonworks.com/innovation/stinger/) - Hive 的交互式查询。
* [Tajo](http://tajo.apache.org/) - Hadoop 上的分布式数据仓库系统。
* [Trafodion](https://wiki.trafodion.org/wiki/index.php/Main_Page) - 针对大数据事务或操作工作负载的企业级 SQL-on-HBase 解决方案。
* [Trino](https://trino.io/) - 分布式 SQL 查询引擎，用于跨异构数据源查询大型数据集。

## 矢量数据库

* [Chroma](https://www.trychroma.com/) - 用于人工智能应用的开源嵌入数据库。
* [Infinity](https://github.com/infiniflow/infinity) - 用于混合向量、稀疏向量、张量、全文和结构化搜索的 AI 原生数据库。
* [LanceDB](https://www.lancedb.com/) - 基于 Lance 柱状格式构建的开源嵌入式矢量数据库。
* [Milvus](https://github.com/milvus-io/milvus) - 用于可扩展相似性搜索的开源矢量数据库。
* [Qdrant](https://qdrant.tech/) - 具有 REST、gRPC 和客户端 SDK 的矢量数据库和相似性搜索引擎。
* [Weaviate](https://weaviate.io/) - 用于具有结构化过滤的语义搜索的开源矢量数据库。

## 数据摄取
* [redpanda](https://vectorized.io/redpanda) - 任务关键型系统的 Kafka® 替代品；速度提高 10 倍。用 C++ 编写。
* [Airbyte](https://airbyte.com/) - 用于 ELT 管道和基于连接器的复制的开源数据移动平台。
* [Amazon Kinesis](https://aws.amazon.com/kinesis/) - 大规模流数据的实时处理。
* [Amazon Web Services Glue](https://aws.amazon.com/glue/) - 无服务器完全托管的提取、转换和加载 (ETL) 服务
* [Apache Chukwa](http://chukwa.apache.org/) - 数据收集系统。
* [Apache Flume](http://flume.apache.org/) - 管理大量日志数据的服务。
* [Apache Kafka](http://kafka.apache.org/) - 分布式发布订阅消息系统。
* [Apache NiFi](https://nifi.apache.org/) - Apache NiFi 是一个集成数据物流平台，用于自动化不同系统之间的数据移动。
* [Apache Pulsar](https://github.com/apache/pulsar) - 一个分布式发布-订阅消息平台，具有非常灵活的消息模型和直观的客户端 API。
* [Apache SeaTunnel](https://seatunnel.apache.org/) - 用于批量和流同步的高性能分布式数据集成平台。
* [Apache Sqoop](http://sqoop.apache.org/) - 在 Hadoop 和结构化数据存储之间传输数据的工具。
* [Bruin](https://github.com/bruin-data/bruin) - 端到端数据管道工具，结合了摄取、转换和数据质量检查。
* [Census](https://getcensus.com/) - 反向 ETL 产品，可让您将数据从数据仓库同步到 SaaS 应用程序。不需要任何工程支持——只需要 SQL。
* [DataRaven](https://dataraven.io/) - 用于数据摄取工作流程的托管云对象存储传输。
* [DBConvert Streams](https://streams.dbconvert.com/cdc-replication/) - 自托管 CDC 复制和数据库迁移工具。
* [Debezium](https://debezium.io/) - 用于捕获变更数据的开源分布式平台。
* [Embulk](http://www.embulk.org) - 开源批量数据加载器，有助于在各种数据库、存储、文件格式和云服务之间传输数据。
* [Estuary](https://estuary.dev) - 基于 Gazette 的 SaaS 平台，具有即插即用连接器。
* [Facebook Scribe](https://github.com/facebookarchive/scribe) - 流式日志数据聚合器。
* [Flink CDC](https://nightlies.apache.org/flink/flink-cdc-docs-stable/) - 由 Apache Flink 提供支持的流数据集成工具。
* [Fluentd](http://www.fluentd.org) - 收集事件和日志的工具。
* [Gazette](https://github.com/gazette/core) - 基于云存储构建的分布式流媒体基础设施，可以轻松混合和匹配批处理和流媒体范例。
* [Google Photon](https://research.google.com/pubs/pub41318.html) - 地理分布式系统，用于实时连接多个连续流动的数据流，具有高可扩展性和低延迟。
* [Graylog](https://www.graylog.org/) - 用于收集、存储、搜索和警报机器数据的日志管理平台。
* [Heka](https://github.com/mozilla-services/heka) - 开源流处理软件系统。
* [Hevo](https://hevodata.com/) - 托管数据管道平台，用于从数据库、SaaS 应用程序、云存储、SDK 和流服务移动数据。
* [Hightouch](https://hightouch.com/) - 用于将仓库数据同步到业务应用程序的反向 ETL 平台。
* [HIHO](https://github.com/sonalgoyal/hiho) - 用于将不同数据源与 Hadoop 连接的框架。
* [ingestr](https://github.com/bruin-data/ingestr) - 用于在源和目标之间复制数据的 CLI 工具。
* [Kestrel](https://github.com/papertrail/kestrel) - 分布式消息队列系统。
* [LinkedIn Databus](https://engineering.linkedin.com/data) - 数据库的更改捕获事件流。
* [LinkedIn Kamikaze](https://github.com/linkedin/kamikaze) - 用于压缩排序整数数组的实用程序包。
* [LinkedIn White Elephant](https://github.com/linkedin/white-elephant) - 日志聚合器和仪表板。
* [Logstash](https://www.elastic.co/products/logstash) - 用于管理事件和日志的工具。
* [Metricbeat](https://www.elastic.co/beats/metricbeat) - 用于系统和服务指标的轻量级托运人。
* [Netflix Suro](https://github.com/Netflix/suro) - 基于 Chukwa 的日志聚合器，例如 Storm 和 Samza。
* [Pinterest Secor](https://github.com/pinterest/secor) - 是一个实现Kafka日志持久化的服务。
* [Linkedin Gobblin](https://github.com/linkedin/gobblin) - linkedin 的通用数据摄取框架。
* [Skizze](https://github.com/skizzehq/skizze) - 草图数据存储可使用概率数据结构处理有关计数和草图的所有问题。
* [StreamSets Data Collector](https://github.com/streamsets/datacollector) - 通过简单易用的 IDE 持续摄取大数据基础设施。
* [Alooma](https://www.alooma.com/integrations/mysql) - 数据管道即服务，支持将 MySQL 等数据源移动到数据仓库中。
* [RudderStack](https://github.com/rudderlabs/rudder-server) - 用 go 编写的开源客户数据基础设施（segment、mParticle 替代方案）。
* [Zilla](https://github.com/aklivity/zilla) - 专为事件驱动架构和流媒体构建的 API 网关，支持 HTTP、SSE、gRPC、MQTT 和本机 Kafka 协议等标准协议。

## 数据质量和可观察性

* [DataKitchen Open Source Data Observability](https://docs.datakitchen.io/observability/get-started/) - 用于监控数据旅程、数据质量和管道事件的开源数据可观察性。
* [Great Expectations](https://greatexpectations.io/) - 用于验证、记录和测试数据质量的开源框架。
* [OpenLineage](https://openlineage.io/) - 用于从数据管道收集沿袭元数据的开放标准和参考实现。
* [Soda Core](https://docs.soda.io/soda-core/overview-main.html) - 用于数据质量测试的开源 Python 库和 CLI。

## 服务编程

* [Akka Toolkit](http://akka.io/) - JVM 上的分布式、容错事件驱动应用程序的运行时。
* [Apache Avro](http://avro.apache.org/) - 数据序列化系统。
* [Apache Curator](http://curator.apache.org/) - Apache ZooKeeper 的 Java 库。
* [Apache Karaf](http://karaf.apache.org/) - 在任何 OSGi 框架之上运行的 OSGi 运行时。
* [Apache Thrift](http://thrift.apache.org//) - 构建二进制协议的框架。
* [Apache Zookeeper](http://zookeeper.apache.org/) - 流程管理的集中服务。
* [Google Chubby](https://research.google.com/archive/chubby.html) - 松耦合分布式系统的锁服务。
* [Hydrosphere Mist](https://github.com/Hydrospheredata/mist) - 用于将 Apache Spark 分析作业和机器学习模型公开为实时、批处理或反应式 Web 服务的服务。
* [Linkedin Norbert](https://engineering.linkedin.com/data) - 集群管理器。
* [Mara](https://github.com/mara/data-integration) - 一个轻量级的固执己见的 ETL 框架，介于普通脚本和 Apache Airflow 之间
* [OpenMPI](https://www.open-mpi.org/) - 消息传递框架。
* [Serf](https://www.serf.io/) - 用于服务发现和编排的去中心化解决方案。
* [Spotify Luigi](https://github.com/spotify/luigi) - 用于构建复杂的批处理作业管道的 Python 包。它处理依赖性解析、工作流管理、可视化、处理故障、命令行集成等等。
* [Spring XD](https://github.com/spring-projects/spring-xd) - 用于数据摄取、实时分析、批处理和数据导出的分布式和可扩展系统。
* [Twitter Elephant Bird](https://github.com/twitter/elephant-bird) - 用于处理 LZOP 压缩数据的库。
* [Twitter Finagle](https://twitter.github.io/finagle/) - JVM 的异步网络堆栈。

## 调度

* [Apache Airflow](https://github.com/apache/incubator-airflow) - 一个以编程方式创作、安排和监控工作流程的平台。
* [Apache Aurora](http://aurora.apache.org/) - 是一个运行在 Apache Mesos 之上的服务调度程序。
* [Apache Falcon](http://falcon.apache.org/) - 数据管理框架。
* [Apache Oozie](http://oozie.apache.org/) - 工作流作业调度程序。
* [Azure Data Factory](https://docs.microsoft.com/en-us/azure/data-factory/data-factory-introduction) - 适用于本地、云和 HDInsight 的基于云的管道编排
* [Chronos](http://mesos.github.io/chronos/) - 分布式和容错调度器。
* [Cronicle](https://github.com/jhuckaby/Cronicle) - 分布式、易于安装、基于 NodeJS、任务调度程序
* [Dagster](https://github.com/dagster-io/dagster) - 用于机器学习、分析和 ETL 的数据协调器。
* [Linkedin Azkaban](https://azkaban.github.io/) - 批处理工作流作业调度程序。
* [Schedoscope](https://github.com/ottogroup/schedoscope) - 用于敏捷调度 Hadoop 作业的 Scala DSL。
* [Sparrow](https://github.com/radlab/sparrow) - 调度平台。


## 机器学习

* [Aim](https://github.com/aimhubio/aim) - 用于实验和训练运行的开源人工智能元数据跟踪器。
* [Azure ML Studio](https://studio.azureml.net/) - 基于云的 AzureML、R、Python 机器学习平台
* [brain](https://github.com/harthur/brain) - JavaScript 中的神经网络。
* [Oryx](https://github.com/OryxProject/oryx) - Apache Spark、Apache Kafka 上的 Lambda 架构用于实时大规模机器学习。
* [Concurrent Pattern](http://www.cascading.org/projects/pattern/) - Cascading 机器学习库。
* [convnetjs](https://github.com/karpathy/convnetjs) - JavaScript 中的深度学习。在浏览器中训练卷积神经网络（或普通网络）。
* [DataVec](https://github.com/deeplearning4j/DataVec) - 用于 Java 和 Scala 深度学习的矢量化和数据预处理库。 Deeplearning4j 生态系统的一部分。
* [Deeplearning4j](https://github.com/deeplearning4j) - 适用于 JVM（Java、Scala、Clojure）的快速、开放的深度学习。由 C++ 库提供支持的神经网络配置层。使用 Spark 和 Hadoop 在多个 GPU 和 CPU 上训练网络。
* [Decider](https://github.com/danielsdeleo/Decider) - Ruby 中灵活且可扩展的机器学习。
* [ENCOG](http://www.heatonresearch.com/encog/) - 机器学习框架，支持各种高级算法，并支持规范化和处理数据的类。
* [etcML](http://www.etcml.com/) - 使用机器学习进行文本分类。
* [Etsy Conjecture](https://github.com/etsy/Conjecture) - Scalding 中的可扩展机器学习。
* [Feast](https://github.com/gojek/feast) - 用于管理、发现和访问机器学习功能的功能存储。 Feast 为模型训练和模型服务提供一致的特征数据视图。
* [GraphLab Create](https://dato.com/products/create/) - Python 机器学习平台，包含广泛的 ML 工具包、数据工程和部署工具。
* [H2O](https://github.com/h2oai/h2o-3/) - 使用 Hadoop 进行统计、机器学习和数学运行时。 R 和 Python。
* [isolation-forest](https://github.com/linkedin/isolation-forest) - 用于无监督异常值检测的隔离森林的分布式 Spark 和 Scala 实现。
* [Karate Club](https://github.com/benedekrozemberczki/karateclub) - 用于图结构化数据的无监督机器学习库。蟒蛇
* [Keras](https://github.com/fchollet/keras) - 受 Torch 启发的直观神经网络 API，运行在 Theano 和 Tensorflow 之上。
* [Lambdo](https://github.com/johnsonc/lambdo) - Lambdo 是一个工作流引擎，通过统一特征工程和机器学习操作，显着简化了分析过程。
* [Little Ball of Fur](https://github.com/benedekrozemberczki/littleballoffur) - 用于图结构化数据的子采样库。蟒蛇
* [Mahout](http://mahout.apache.org/) - 一个 Apache 支持的 Hadoop 机器学习库。
* [MLbase](http://www.mlbase.org/) - BDAS 堆栈的分布式机器学习库。
* [MLPNeuralNet](https://github.com/nikolaypavlov/MLPNeuralNet) - 适用于 iOS 和 Mac OS X 的快速多层感知器神经网络库。
* [ML Workspace](https://github.com/ml-tooling/ml-workspace) - 专门用于机器学习和数据科学的基于 Web 的一体化 IDE。
* [MOA](http://moa.cms.waikato.ac.nz) - MOA 实时执行大数据流挖掘和大规模机器学习。
* [MonkeyLearn](https://monkeylearn.com/) - 文本挖掘变得简单。从文本中提取数据并对其进行分类。
* [ND4J](https://github.com/deeplearning4j/nd4j) - JVM 的矩阵库。用于 Java 的 Numpy。
* [Neptune](https://neptune.ai/) - 研究和生产机器学习团队的实验跟踪和模型注册。
* [nupic](https://github.com/numenta/nupic) - Numenta 智能计算平台：一个受大脑启发的机器智能平台，以及基于皮质学习算法的生物精确神经网络。
* [PredictionIO](http://predictionio.incubator.apache.org/index.html) - 基于 Hadoop、Mahout 和 Cascading 构建的机器学习服务器。
* [PyTorch Geometric Temporal](https://github.com/benedekrozemberczki/pytorch_geometric_temporal) - PyTorch Geometric 的时间扩展库。
* [RL4J](https://github.com/deeplearning4j/rl4j) - Java 和 Scala 的强化学习。包括 Deep-Q 学习和 A3C 算法，并与 Open AI 的 Gym 集成。在 Deeplearning4j 生态系统中运行。
* [SAMOA](http://samoa.incubator.apache.org/) - 分布式流式机器学习框架。
* [scikit-learn](https://github.com/scikit-learn/scikit-learn) - scikit-learn：Python 中的机器学习。
* [Shapley](https://github.com/benedekrozemberczki/shapley) - 一个数据驱动的框架，用于量化机器学习集成中分类器的价值。
* [Spark MLlib](http://spark.apache.org/docs/0.9.0/mllib-guide.html) - 一些常见机器学习 (ML) 功能的 Spark 实现。
* [Sibyl](https://users.soe.ucsc.edu/~niejiazhong/slides/chandra.pdf) - 谷歌的大规模机器学习系统。
* [TensorFlow](https://github.com/tensorflow/tensorflow) - Google 的库，用于使用数据流图进行机器学习。
* [Theano](https://github.com/theano) - 由蒙特利尔大学支持的以 Python 为中心的机器学习库。
* [Torch](https://github.com/torch) - 具有 Lua API 的深度学习库，由纽约大学和 Facebook 支持。
* [Velox](https://github.com/amplab/velox-modelserver) - 用于服务机器学习预测的系统。
* [Vowpal Wabbit](https://github.com/JohnLangford/vowpal_wabbit/wiki) - 由微软和雅虎赞助的学习系统。
* [WEKA](http://www.cs.waikato.ac.nz/ml/weka/) - 机器学习软件套件。
* [BidMach](https://github.com/BIDData/BIDMach) - CPU 和 GPU 加速的机器学习库。

## 标杆管理

* [Apache JMeter](https://jmeter.apache.org/) - 用于测量服务和分布式系统性能的负载测试工具。
* [Berkeley SWIM Benchmark](https://github.com/SWIMProjectUCB/SWIM/wiki) - 现实世界的大数据工作负载基准。
* [Estuary Benchmark Report](https://github.com/estuary/estuary-warehouse-benchmark) - 可重复的、供应商中立的数据仓库基准。
* [Intel HiBench](https://github.com/intel-hadoop/HiBench) - Hadoop 基准测试套件。
* [PUMA Benchmarking](https://issues.apache.org/jira/browse/MAPREDUCE-5116) - MapReduce 应用程序的基准测试套件。
* [Yahoo Gridmix3](http://yahoohadoop.tumblr.com/post/98294079296/gridmix3-emulating-production-workload-for) - 雅虎工程师团队的 Hadoop 集群基准测试。
* [Deeplearning4j 基准测试](https://github.com/deeplearning4j/dl4j-benchmark)
* [UCSB](https://github.com/unum-cloud/ucsb) - 扩展了 NoSQL 数据库的雅虎云服务基准。

## 安全性
* [Apache Ranger](http://ranger.apache.org/) - Hadoop 的中央安全管理和细粒度授权
* [Apache Eagle](http://eagle.apache.org/) - 实时监控解决方案
* [Apache Knox Gateway](http://knox.apache.org/) - Hadoop 集群的单点安全访问。
* [Apache Sentry](http://incubator.apache.org/projects/sentry.html) - Hadoop 中存储数据的安全模块。
* [BDA](https://github.com/kotobukki/BDA/) - Hadoop 和 Spark 的漏洞检测器
* [FileShot](https://github.com/FileShot/FileShotZKE) - 用于共享大型数据集的零知识加密文件传输。

## 系统部署

* [Apache Ambari](http://ambari.apache.org/) - Hadoop 管理的操作框架。
* [Apache Bigtop](http://bigtop.apache.org//) - Hadoop生态系统的系统部署框架。
* [Apache Helix](http://helix.apache.org/) - 集群管理框架。
* [Apache Mesos](http://mesos.apache.org/) - 集群管理器。
* [Apache Slider](https://github.com/apache/incubator-slider) - 是一个 YARN 应用程序，用于在 YARN 上部署现有的分布式应用程序。
* [Apache Whirr](http://whirr.apache.org/) - 用于运行云服务的库集。
* [Apache YARN](https://hortonworks.com/hadoop/yarn/) - 集群管理器。
* [Brooklyn](http://brooklyncentral.github.io/) - 简化应用程序部署和管理的库。
* [Buildoop](http://buildoop.github.io/) - 类似于基于Groovy语言的Apache BigTop。
* [Cloudera HUE](http://gethue.com/) - 用于与 Hadoop 交互的 Web 应用程序。
* [Facebook Prism](http://www.wired.com/2012/08/facebook-prism/) - 多数据中心复制系统。
* [Google Borg](https://www.wired.com/2013/03/google-borg-twitter-mesos/all/) - 作业调度和监控系统。
* [Google Omega](https://www.youtube.com/watch?v=0ZFMlO98Jkc) - 作业调度和监控系统。
* [Hortonworks HOYA](https://hortonworks.com/blog/introducing-hoya-hbase-on-yarn/) - 可以在YARN上部署HBase集群的应用程序。
* [Kubernetes](https://kubernetes.io/) - 用于自动化部署、扩展和管理容器化应用程序的系统。
* [Marathon](https://github.com/mesosphere/marathon) - 用于长期运行服务的 Mesos 框架。
* [Linkis](https://github.com/WeBankFinTech/Linkis) - Linkis 有助于轻松连接到各种后端计算/存储引擎。
* [Terraform](https://www.terraform.io/) - 基础设施即代码工具，用于配置和管理云和本地基础设施。

## 应用领域

* [411](https://github.com/etsy/411) - 一个 Web 应用程序，用于管理由 Elasticsearch 中的计划搜索产生的警报。
* [Adobe spindle](https://github.com/adobe-research/spindle) - 使用 Scala、Spark 和 Parquet 进行下一代 Web 分析处理。
* [Apache Metron](http://metron.apache.org/) - 一个集成了各种开源大数据技术的平台，旨在提供集中的安全监控和分析工具。
* [Apache Nutch](http://nutch.apache.org/) - 开源网络爬虫。
* [Apache OODT](http://oodt.apache.org/) - 为美国宇航局科学档案捕获、处理和共享数据。
* [Apache Tika](https://tika.apache.org/) - 内容分析工具包。
* [Argus](https://github.com/salesforce/Argus) - 时间序列监控报警平台。
* [AthenaX](https://github.com/uber/AthenaX) - 一个流分析平台，使用户能够使用结构化查询语言 (SQL) 运行生产质量的大规模流分析。
* [Atlas](https://github.com/Netflix/atlas) - 用于管理维度时间序列数据的后端。
* [Countly](https://count.ly/) - 基于 Node.js 和 MongoDB 的开源移动和 Web 分析平台。
* [Comet](https://www.comet.com/site/) - Comet 为 AI 开发人员提供端到端模型评估平台，提供一流的 LLM 评估、实验跟踪和生产监控。
* [Domino](https://www.dominodatalab.com/) - 无需任何基础设施即可运行、扩展、共享和部署模型。
* [Eclipse BIRT](http://www.eclipse.org/birt/) - 基于 Eclipse 的报告系统。
* [ElastAert](https://github.com/Yelp/elastalert) - ElastAlert 是一个简单的框架，用于针对 ElasticSearch 中的数据中的异常、峰值或其他感兴趣的模式发出警报。
* [Eventhub](https://github.com/Codecademy/EventHub) - 开源事件分析平台。
* [Gigasheet](https://www.gigasheet.com/) - 用于探索和分析大型数据集的云电子表格。
* [HASH](https://hash.ai) - 开源仿真和可视化平台。
* [Hermes](https://github.com/allegro/hermes) - 构建在 Kafka 之上的异步消息代理。
* [Hunk](https://www.splunk.com/en_us/download/hunk.html) - 适用于 Hadoop 的 Splunk 分析。
* [Indicative](https://www.indicative.com/) - Web 和移动分析工具，与数据仓库（AWS、BigQuery）集成。
* [Jupyter](https://jupyter.org/) - 跨所有编程语言的交互式数据科学和科学计算的笔记本和项目应用程序。
* [MADlib](http://madlib.incubator.apache.org/community/) - 用于分析数据的 RDBMS 的数据处理库。
* [Kapacitor](https://github.com/influxdata/kapacitor) - 用于处理、监控和警报时间序列数据的开源框架。
* [Kylin](http://kylin.apache.org/) - 来自 eBay 的开源分布式分析引擎。
* [PivotalR](https://github.com/pivotalsoftware/PivotalR) - Pivotal HD / HAWQ 和 PostgreSQL 上的 R。
* [Opik](https://www.comet.com/site/products/opik/) - 通过全面的跟踪、自动评估和生产就绪的仪表板来调试、评估和监控您的 LLM 应用程序、RAG 系统和代理工作流程。
* [Rakam](https://github.com/rakam-io/rakam) - 由 Postgresql、Kinesis 和 PrestoDB 提供支持的开源实时自定义分析平台。
* [Qubole](https://www.qubole.com/) - 自动扩展 Hadoop 集群，内置数据连接器。
* [SnappyData](https://github.com/SnappyDataInc/snappydata) - 用于实时操作分析的分布式内存数据存储，在单个集成集群中基于 Spark 提供流分析、OLTP（在线事务处理）和 OLAP（在线分析处理）。
* [Snowplow](https://github.com/snowplow/snowplow) - 企业级 Web 和事件分析，由 Hadoop、Kinesis、Redshift 和 Postgres 提供支持。
* [SparkR](http://amplab-extras.github.io/SparkR-pkg/) - Spark 的 R 前端。
* [Splunk](https://www.splunk.com/) - 机器生成数据的分析器。
* [Sumo Logic](https://www.sumologic.com/) - 基于云的机器生成数据分析器。
* [Substation](https://github.com/brexhq/substation) - Substation 是一个用 Go 编写的云原生数据管道和转换工具包。
* [Talend](http://www.talend.com/products/big-data/) - 适用于 YARN、Hadoop、HBASE、Hive、HCatalog 和 Pig 的统一开源环境。

## 搜索引擎和框架

* [Apache Lucene](http://lucene.apache.org/) - 搜索引擎库。
* [Apache Solr](http://lucene.apache.org/solr/) - Apache Lucene 的搜索平台。
* [Elassandra](https://github.com/strapdata/elassandra) - 是 Elasticsearch 的一个分支，经过修改，可以在可扩展且有弹性的点对点架构中在 Apache Cassandra 之上运行。
* [ElasticSearch](https://www.elastic.co/) - 基于 Apache Lucene 的搜索和分析引擎。
* [Enigma.io](https://www.enigma.com/) - 免费增值强大的网络应用程序，用于探索、过滤、分析、搜索和导出从网络上抓取的大量数据集。
* [Google Caffeine](https://googleblog.blogspot.it/2010/06/our-new-search-index-caffeine.html) - 连续索引系统。
* [Google Percolator](https://research.google.com/pubs/pub36726.html) - 连续索引系统。
* [HBase Coprocessor](https://blogs.apache.org/hbase/entry/coprocessor_introduction) - Percolator 的实现，它是 HBase 的一部分。
* [Lily HBase Indexer](http://ngdata.github.io/hbase-indexer/) - 快速轻松地搜索 HBase 中存储的任何内容。
* [LinkedIn Bobo](http://senseidb.github.io/bobo/) - 是一个纯粹用 Java 编写的分面搜索实现，是 Apache Lucene 的扩展。
* [LinkedIn Cleo](https://github.com/linkedin/cleo) - 是一个灵活的软件库，用于快速开发部分、无序和实时预输入搜索。
* [LinkedIn Galene](https://engineering.linkedin.com/search/did-you-mean-galene) - LinkedIn 的搜索架构。
* [LinkedIn Zoie](https://github.com/senseidb/zoie) - 是一个用 Java 编写的实时搜索/索引系统。
* [MG4J](http://mg4j.di.unimi.it/) - MG4J（Managing Gigabytes for Java）是一个用 Java 编写的大型文档集合的全文搜索引擎。它具有高度可定制性、高性能，并提供最先进的功能和新的研究算法。
* [Sphinx Search Server](http://sphinxsearch.com/) - 全文搜索引擎。
* [Vespa](http://vespa.ai/) - 是一个针对大型数据集进行低延迟计算的引擎。它存储并索引您的数据，以便可以在服务时对数据执行查询、选择和处理。
* [Facebook Faiss](https://github.com/facebookresearch/faiss) - 是一个用于高效相似性搜索和密集向量聚类的库。它包含的算法可以搜索任意大小的向量集，甚至可能无法容纳在 RAM 中的向量集。它还包含用于评估和参数调整的支持代码。 Faiss 是用 C++ 编写的，带有 Python/numpy 的完整包装器。
* [Annoy](https://github.com/spotify/annoy) - 是一个带有 Python 绑定的 C++ 库，用于搜索空间中接近给定查询点的点。它还创建基于文件的大型只读数据结构，这些数据结构被映射到内存中，以便许多进程可以共享相同的数据。

## MySQL 的分支和演变

* [Amazon RDS](https://aws.amazon.com/rds/) - 亚马逊云中的 MySQL 数据库。
* [Drizzle](http://www.drizzle.org/) - MySQL 6.0 的演变。
* [Google Cloud SQL](https://cloud.google.com/sql/docs/) - Google 云中的 MySQL 数据库。
* [MariaDB](https://mariadb.org/) - MySQL 的增强型、直接替代品。
* [MySQL Cluster](https://www.mysql.com/products/cluster/) - MySQL使用NDB Cluster存储引擎实现。
* [Percona Server](https://www.percona.com/software/mysql-database/percona-server) - MySQL 的增强型、直接替代品。
* [ProxySQL](https://github.com/renecannao/proxysql) - MySQL 的高性能代理。
* [TokuDB](https://www.percona.com/) - TokuDB 是 MySQL 和 MariaDB 的存储引擎。
* [WebScaleSQL](http://webscalesql.org/) - 是来自多家公司的工程师之间的合作，这些公司在大规模运行 MySQL 方面面临着类似的挑战。

## PostgreSQL 的分叉和演变

* [HadoopDB](http://db.cs.yale.edu/hadoopdb/hadoopdb.html) - MapReduce 和 DBMS 的混合体。
* [IBM Netezza](http://www-01.ibm.com/software/data/netezza/) - 高性能数据仓库设备。
* [Postgres-XL](http://www.postgres-xl.org/) - 基于 PostgreSQL 的可扩展开源数据库集群。
* [RecDB](http://www-users.cs.umn.edu/~sarwat/RecDB/) - 完全构建在 PostgreSQL 内部的开源推荐引擎。
* [Stado](http://www.stormdb.com/community/stado) - 开源MPP数据库系统，仅针对数据仓库和数据集市应用程序。
* [Yahoo Everest](https://www.scribd.com/doc/3159239/70-Everest-PGCon-RT) - 由 PostgreSQL 派生的多 PB 数据库 / MPP。
* [TimescaleDB](http://www.timescale.com/) - 针对快速摄取和复杂查询进行优化的开源时间序列数据库
* [PipelineDB](https://www.pipelinedb.com/) - 流式 SQL 数据库。一个开源关系数据库，可在流上连续运行 SQL 查询，并将结果增量存储在表中

## Memcached 分叉和演变

* [Facebook McDipper](https://www.facebook.com/notes/facebook-engineering/mcdipper-a-key-value-cache-for-flash-storage/10151347090423920) - 用于闪存存储的键/值缓存。
* [Facebook Memcached](https://www.facebook.com/notes/facebook-engineering/scaling-memcache-at-facebook/10151411410803920) - Memcache 的分叉。
* [Twemproxy](https://github.com/twitter/twemproxy) - 用于 memcached 和 redis 的快速、轻量级代理。
* [Twitter Fatcache](https://github.com/twitter/fatcache) - 用于闪存存储的键/值缓存。
* [Twitter Twemcache](https://github.com/twitter/twemcache) - Memcache 的分叉。

## 嵌入式数据库

* [Actian PSQL](http://www.actian.com/products/operational-databases/) - 由 Pervasive Software 开发的符合 ACID 的 DBMS，针对嵌入应用程序进行了优化。
* [BerkeleyDB](https://www.oracle.com/database/berkeley-db/index.html) - 一个软件库，为键/值数据提供高性能嵌入式数据库。
* [HanoiDB](https://github.com/krestenkrab/hanoidb) - Erlang LSM BTree 存储。
* [LevelDB](https://github.com/google/leveldb) - Google 编写的快速键值存储库，提供从字符串键到字符串值的有序映射。
* [LMDB](https://symas.com/mdb/) - Symas 开发的超快速、超紧凑的键值嵌入式数据存储。
* [RocksDB](http://rocksdb.org/) - 基于 LevelDB 的嵌入式持久键值存储，用于快速存储。

## 商业智能

* [BIME Analytics](https://www.bimeanalytics.com/?lang=en) - 云中的商业智能平台。
* [Blazer](https://github.com/ankane/blazer) - 商业智能变得简单。
* [Chartio](https://chartio.com) - 精益商业智能平台可可视化和探索您的数据。
* [Count](https://count.co) - 使用 SQL 或拖放的基于笔记本的分析和可视化平台。
* [datapine](https://www.datapine.com/) - 云中的自助式商业智能工具。
* [Dekart](https://dekart.xyz/) - 基于 Kepler.gl 的 Google BigQuery 大规模地理空间分析。
* [GoodData](https://www.gooddata.com/) - 数据产品和嵌入式分析平台。
* [Jaspersoft](https://www.jaspersoft.com/) - 强大的商业智能套件。
* [Jedox Palo](https://www.jedox.com/en/) - 可定制的商业智能平台。
* [Jethrodata](https://jethro.io/) - 交互式大数据分析。
* [intermix.io](https://intermix.io/) - Amazon Redshift 性能监控
* [Lightdash](https://github.com/lightdash/lightdash) - 基于 dbt 构建的开源 Looker 替代方案
* [Metabase](https://github.com/metabase/metabase) - 以最简单、最快的方式为公司中的每个人提供商业智能和分析。
* [Microsoft](http://www.microsoft.com/en-us/server-cloud/solutions/business-intelligence/default.aspx) - 商业智能软件和平台。
* [Microstrategy](https://www.microstrategy.com/) - 用于商业智能、移动智能和网络应用的软件平台。
* [Numeracy](https://numeracy.co/) - 快速、干净的 SQL 客户端和商业智能。
* [Pentaho](http://www.pentaho.com/) - 商业智能平台。
* [Qlik](http://www.qlik.com/us/) - 商业智能和分析平台。
* [Query.me](https://query.me/) - 用于查询、调度和共享报告工作流程的协作 SQL 笔记本。
* [Redash](https://redash.io/) - 开源商业智能平台，支持多种数据源和计划查询。
* [Datapallas](https://datapallas.com/) - 具有人工智能探索、仪表板和像素完美报告生成功能的商业智能和数据平台；以前称为 ReportBurster。
* [Saiku Analytics](https://www.meteorite.bi/) - 开源分析平台。
* [Knowage](https://www.knowage-suite.com/) - 开源商业智能平台。 （前 [SpagoBi](http://www.spagobi.org/)）
* [SparklineData SNAP](http://sparklinedata.com/) - 由 Apache Spark 提供支持的现代 B.I 平台。
* [Tableau](https://www.tableau.com/) - 商业智能平台。
* [Zoomdata](https://www.zoomdata.com/) - 大数据分析。


## 数据可视化

* [Airpal](https://github.com/airbnb/airpal) - PrestoDB 的 Web UI。
* [AnyChart](http://www.anychart.com) - 快速、简单且灵活的 JavaScript (HTML5) 图表库，具有纯 JS API。
* [Arbor](https://github.com/samizdatco/arbor) - 使用 Web Worker 和 jQuery 的图形可视化库。
* [Banana](https://github.com/LucidWorks/banana) - 可视化存储在 Solr 中的日志和时间戳数据。基巴纳港。
* [Bloomery](https://github.com/ufukomer/bloomery) - Impala 的 Web UI。
* [Bokeh](http://bokeh.pydata.org/en/latest/) - 一个强大的 Python 交互式可视化库，针对现代 Web 浏览器进行演示，其目标是以 D3.js 的风格提供优雅、简洁的新颖图形结构，同时在非常大的数据集或流数据集上提供高性能交互性。
* [C3](http://c3js.org/) - 基于D3的可重用图表库
* [CartoDB](https://github.com/CartoDB/cartodb) - 地理空间数据库的开源或免费增值托管，具有强大的前端编辑功能和强大的 API。
* [chartd](http://chartd.co/) - 响应式、视网膜兼容的图表，只需一个 img 标签。
* [Chart.js](http://www.chartjs.org/) - 开源 HTML5 图表可视化。
* [Chartist.js](https://github.com/gionkunz/chartist-js) - 另一个开源 HTML5 图表可视化。
* [Crossfilter](http://square.github.io/crossfilter/) - 用于在浏览器中探索大型多元数据集的 JavaScript 库。与 dc.js 和 d3.js 配合良好。
* [Cubism](https://github.com/square/cubism) - 用于时间序列可视化的 JavaScript 库。
* [Cytoscape](http://cytoscape.github.io/) - 用于可视化复杂网络的 JavaScript 库。
* [DC.js](http://dc-js.github.io/dc.js/) - 构建维度图表，与使用 d3.js 渲染的交叉过滤器一起本地工作。非常适合将图表/附加元数据连接到 D3 中的悬停事件。
* [D3](https://d3js.org/) - 用于操作文档的 javaScript 库。
* [D3.compose](https://github.com/CSNW/d3.compose) - 从可重复使用的图表和组件中构建复杂的、数据驱动的可视化效果。
* [D3Plus](http://d3plus.org) - d3.js 的一组相当强大的可重用图表和样式。
* [Dash](https://github.com/plotly/dash) - 适用于 Python、R、Julia 和 Jupyter 的分析 Web 应用程序。构建在plotly之上，不需要JS
* [Dekart](https://dekart.xyz/) - 基于 Kepler.gl 的 Google BigQuery 大规模地理空间分析。
* [DevExtreme React Chart](https://devexpress.github.io/devextreme-reactive/react/chart/) - 用于 Bootstrap 和 Material Design 的基于插件的高性能 React 图表。
* [Echarts](https://github.com/ecomfe/echarts) - 百度企业排行榜。
* [Envisionjs](https://github.com/HumbleSoftware/envisionjs) - 动态 HTML5 可视化。
* [Flexmonster Pivot Table & Charts](https://www.flexmonster.com/) - 用于数据透视表、图表和 Web 报告的 JavaScript 组件。
* [FnordMetric](https://metrictools.org/) - 编写返回 SVG 图表而不是表格的 SQL 查询
* [Frappe Charts](https://frappe.io/charts) - 受 GitHub 启发的简单而现代的 SVG 图表，适用于网络，零依赖。
* [Freeboard](https://github.com/Freeboard/freeboard) - 用于物联网和其他网络混搭的笔源实时仪表板构建器。
* [Gephi](https://github.com/gephi/gephi) - 一个屡获殊荣的开源平台，用于可视化和操作大型图形和网络连接。它就像 Photoshop，但用于图形。适用于 Windows 和 Mac OS X。
* [Google Charts](https://developers.google.com/chart/) - 简单的图表 API。
* [Grafana](https://grafana.com/) - 石墨仪表板前端、编辑器和图形编辑器。
* [Graphite](http://graphiteapp.org/) - 可扩展的实时绘图。
* [Highcharts](https://www.highcharts.com/) - 简单灵活的图表API。
* [IPython](http://ipython.org/) - 为交互式计算提供了丰富的架构。
* [Kibana](https://www.elastic.co/products/kibana) - 可视化日志和时间戳数据
* [Lumify](http://lumify.io/) - 开源大数据分析与可视化平台
* [Matplotlib](https://github.com/matplotlib/matplotlib) - 用Python绘图。
* [Metricsgraphic.js](https://metricsgraphicsjs.org/) - 一个基于 D3 构建的库，针对时间序列数据进行了优化
* [NVD3](http://nvd3.org/) - d3.js 的图表组件。
* [Peity](https://github.com/benpickles/peity) - 渐进式 SVG 条形图、折线图和饼图。
* [Plot.ly](https://plot.ly/) - 易于使用的 Web 服务，可快速创建从热图到直方图的复杂图表。上传数据以使用 Plotly 的在线电子表格创建图表并设置图表样式。叉掉别人的地块。
* [Plotly.js](https://github.com/plotly/plotly.js) 为plotly提供支持的开源JavaScript图形库。
* [Recline](https://github.com/okfn/recline) - 简单但功能强大的库，用于用纯 Javascript 和 HTML 构建数据应用程序。
* [Redash](https://github.com/getredash/redash) - 用于查询和可视化数据的开源平台。
* [ReCharts](http://recharts.org/) - 基于 React 组件构建的可组合图表库
* [Shiny](http://shiny.rstudio.com/) - R 的 Web 应用程序框架。
* [Sigma.js](https://github.com/jacomyal/sigma.js) - 专用于图形绘制的 JavaScript 库。
* [Superset](https://github.com/apache/incubator-superset) - 一个旨在可视化、直观和交互式的数据探索平台，可以轻松地对数据进行切片、切块和可视化，并以思考的速度执行分析。
* [Vega](https://github.com/vega/vega) - 可视化语法。
* [WebDataRocks](https://www.webdatarocks.com/) - 免费的网络数据透视表组件，用于在应用程序中嵌入分析。
* [Zeppelin](https://github.com/ZEPL/zeppelin) - 笔记本式协作数据分析。
* [Zing Charts](https://www.zingchart.com/) - 用于大数据的 JavaScript 图表库。
* [DataSphere Studio](https://github.com/WeBankFinTech/DataSphereStudio) - 一站式数据应用开发管理门户。

## 物联网和传感器数据
* [Apache Edgent (Incubating)](http://edgent.apache.org/) - 编程模型和微内核样式运行时，可以嵌入网关和小型边缘设备中，从而在边缘设备上实现本地实时分析。
* [Azure IoT Hub](https://azure.microsoft.com/en-us/services/iot-hub/) - 基于云的双向监控和消息传递中心
* [TempoIQ](https://www.tempoiq.com/) - 基于云的传感器分析。
* [2lemetry](http://2lemetry.com/) - 物联网平台。
* [Pubnub](https://www.pubnub.com/) - 数据流网络
* [ThingWorx](https://www.thingworx.com/) - 智能系统快速开发与连接
* [IFTTT](https://ifttt.com/) - 如果这个那么那个
* [Evrything](https://evrythng.com/) - 让产品智能化
* [NetLytics](https://github.com/marty90/netlytics/) - 用于在 Spark 上处理网络数据的分析平台。
* [Ably](https://ably.com/) - 适用于物联网的发布/订阅消息传递平台

## 有趣的读物

* [Big Data Benchmark](https://amplab.cs.berkeley.edu/benchmark/) - Redshift、Hive、Shark、Impala 和 Stiger/Tez 的基准。
* [NoSQL Comparison](https://kkovacs.eu/cassandra-vs-mongodb-vs-couchdb-vs-redis) - Cassandra、MongoDB、CouchDB、Redis、Riak、HBase、Couchbase、Neo4j、Hypertable、ElasticSearch、Accumulo、VoltDB、Scalaris 比较。
* [Monitoring Kafka performance](https://www.datadoghq.com/blog/monitoring-kafka-performance-metrics?ref=awesome) - 监控 Apache Kafka 的指南，包括用于指标收集的本机方法。
* [Monitoring Hadoop performance](https://www.datadoghq.com/blog/monitor-hadoop-metrics?ref=awesome) - 监控 Hadoop 的指南，概述 Hadoop 架构以及指标收集的本机方法。
* [Monitoring Cassandra performance](https://www.datadoghq.com/blog/how-to-monitor-cassandra-performance-metrics/?ref=awesome) - Cassandra 监控指南，包括指标收集的本机方法。

## 有趣的论文

### 2015 - 2016
* [2015](http://www.vldb.org/pvldb/vol8/p1804-ching.pdf) - **Facebook** - 一万亿边缘：Facebook 规模的图形处理。

### 2013 - 2014
* [2014](http://infolab.stanford.edu/~ullman/mmds/book.pdf) - **斯坦福** - 海量数据集的挖掘。
* [2013](https://amplab.cs.berkeley.edu/wp-content/uploads/2013/03/eurosys13-paper83.pdf) - **AMPLab** - Presto：使用稀疏矩阵的分布式机器学习和图形处理。
* [2013](https://amplab.cs.berkeley.edu/wp-content/uploads/2013/01/dmx1.pdf) - **AMPLab** - MLbase：分布式机器学习系统。
* [2013](https://amplab.cs.berkeley.edu/wp-content/uploads/2013/02/shark_sigmod2013.pdf) - **AMPLab** - Shark：大规模 SQL 和丰富分析。
* [2013](https://amplab.cs.berkeley.edu/wp-content/uploads/2013/05/grades-graphx_with_fonts.pdf) - **AMPLab** - GraphX：Spark 上的弹性分布式图形系统。
* [2013](http://static.googleusercontent.com/media/research.google.com/en//pubs/archive/40671.pdf) - **Google** - HyperLogLog 实践：最先进的基数估计算法的算法工程。
* [2013](http://research.microsoft.com/pubs/200169/now-vldb.pdf) - **Microsoft** - 云中大数据的可扩展渐进式分析。
* [2013](http://static.druid.io/docs/druid.pdf) - **Metamarkets** - Druid：实时分析数据存储。
* [2013](http://db.disi.unitn.eu/pages/VLDBProgram/pdf/industry/p764-rae.pdf) - **Google** - F1 中的在线异步架构更改。
* [2013](http://static.googleusercontent.com/media/research.google.com/en/us/pubs/archive/41344.pdf) - **Google** - F1：可扩展的分布式 SQL 数据库。
* [2013](http://db.disi.unitn.eu/pages/VLDBProgram/pdf/industry/p734-akidau.pdf) - **Google** - MillWheel：互联网规模的容错流处理。
* [2013](http://db.disi.unitn.eu/pages/VLDBProgram/pdf/industry/p767-wiener.pdf) - **Facebook** - 潜水：深入了解 Facebook 的数据。
* [2013](http://db.disi.unitn.eu/pages/VLDBProgram/pdf/industry/p871-curtiss.pdf) - **Facebook** - Unicorn：用于搜索社交图谱的系统。
* [2013](https://www.usenix.org/system/files/conference/nsdi13/nsdi13-final170_update.pdf) - **Facebook** - 扩展 Facebook 的 Memcache。

### 2011 - 2012

* [2012](http://vldb.org/pvldb/vol5/p1771_georgelee_vldb2012.pdf) - **Twitter** - 统一日志基础设施
Twitter 的数据分析。
* [2012](https://amplab.cs.berkeley.edu/wp-content/uploads/2013/04/blinkdb_vldb12_demo.pdf) - **AMPLab** - 眨眼就完成了：超大数据的交互式查询。
* [2012](https://www.usenix.org/system/files/login/articles/zaharia.pdf) - **AMPLab** - 使用 Spark 对 Hadoop 数据进行快速交互式分析。
* [2012](https://amplab.cs.berkeley.edu/wp-content/uploads/2012/03/mod482-xin1.pdf) - **AMPLab** - Shark：使用粗粒度分布式内存进行快速数据分析。
* [2012](https://www.usenix.org/legacy/event/nsdi11/tech/full_papers/Bolosky.pdf) - **Microsoft** - Paxos 复制状态机作为高性能数据存储的基础。
* [2012](http://research.microsoft.com/pubs/178045/ppaoxs-paper29.pdf) - **微软** - Paxos 并行。
* [2012](https://arxiv.org/pdf/1203.5485.pdf) - **AMPLab** - BlinkDB：​​对非常大的数据进行有限错误和有限响应时间的查询。
* [2012](http://vldb.org/pvldb/vol5/p1436_alexanderhall_vldb2012.pdf) - **Google** - 每次鼠标点击处理一万亿个单元格。
* [2012](http://static.googleusercontent.com/media/research.google.com/en//archive/spanner-osdi2012.pdf) - **Google** - Spanner：Google 的全球分布式数据库。
* [2011](https://amplab.cs.berkeley.edu/wp-content/uploads/2011/06/euro118-ananthanarayanan.pdf) - **AMPLab** - Scarlett：应对 MapReduce 集群中流行内容的倾斜。
* [2011](https://amplab.cs.berkeley.edu/wp-content/uploads/2011/06/Mesos-A-Platform-for-Fine-Grained-Resource-Sharing-in-the-Data-Center.pdf) - **AMPLab** - Mesos：数据中心细粒度资源共享的平台。
* [2011](http://static.googleusercontent.com/media/research.google.com/en//pubs/archive/36971.pdf) - **Google** - Megastore：为交互式服务提供可扩展、高度可用的存储。

### 2001 - 2010

* [2010](https://www.usenix.org/legacy/event/osdi10/tech/full_papers/Beaver.pdf) - **Facebook** - 大海捞针：Facebook 的照片存储。
* [2010](https://amplab.cs.berkeley.edu/wp-content/uploads/2011/06/Spark-Cluster-Computing-with-Working-Sets.pdf) - **AMPLab** - Spark：使用工作集的集群计算。
* [2010](http://kowshik.github.io/JPregel/pregel_paper.pdf) - **Google** - Pregel：大规模图形处理系统。
* [2010](http://static.googleusercontent.com/media/research.google.com/en//pubs/archive/36726.pdf) - **Google** - 使用分布式事务和 Percolator 和 Caffeine 的通知库进行大规模增量处理。
* [2010](http://static.googleusercontent.com/media/research.google.com/en//pubs/archive/36632.pdf) - **Google** - Dremel：网络规模数据集的交互式分析。
* [2010](http://leoneu.github.io/) - **雅虎** - S4：分布式流计算平台。
* [2009](http://www.cs.umd.edu/~abadi/papers/hadoopdb.pdf) - HadoopDB：用于分析工作负载的 MapReduce 和 DBMS 技术的架构混合。
* [2008](https://cwiki.apache.org/confluence/download/attachments/120729877/chukwa_cca08.pdf?version=1&modificationDate=1562667399000&api=v2) - **AMPLab** - Chukwa：大型监控系统。
* [2007](http://www.read.seas.harvard.edu/~kohler/class/cs239-w08/decandia07dynamo.pdf) - **亚马逊** - Dynamo：亚马逊的高可用键值存储。
* [2006](http://static.googleusercontent.com/media/research.google.com/en//archive/chubby-osdi06.pdf) - **Google** - 用于松散耦合分布式系统的 Chubby 锁服务。
* [2006](http://static.googleusercontent.com/external_content/untrusted_dlcp/research.google.com/en//archive/bigtable-osdi06.pdf) - **Google** - Bigtable：结构化数据的分布式存储系统。
* [2004](http://static.googleusercontent.com/media/research.google.com/en//archive/mapreduce-osdi04.pdf) - **Google** - MapReduce：大型集群上的简化数据处理。
* [2003](http://static.googleusercontent.com/media/research.google.com/en//archive/gfs-sosp2003.pdf) - **Google** - 谷歌文件系统。

## 视频

* [Spark in Motion](https://www.manning.com/livevideo/spark-in-motion) - Spark in Motion 教您如何使用 Spark 进行批量和流数据分析。
* [Machine Learning, Data Science and Deep Learning with Python ](https://www.manning.com/livevideo/machine-learning-data-science-and-deep-learning-with-python) - 实时视频教程，涵盖机器学习、Tensorflow、人工智能和神经网络。
* [Data warehouse schema design - dimensional modeling and star schema](https://snir.dev/talks/data-warehouse-schema-design) - 介绍使用星型模式方法进行数据仓库的模式设计。
* [Elasticsearch 7 and Elastic Stack](https://www.manning.com/livevideo/elasticsearch-7-and-elastic-stack) - 直播视频教程，涵盖使用 Elasticsearch、Logstash、Beats、Kibana 等在集群上搜索、分析和可视化大数据。

## 书籍

#### 流媒体
* [Data Science at Scale with Python and Dask](https://www.manning.com/books/data-science-at-scale-with-python-and-dask) - 使用 Python 和 Dask 进行大规模数据科学教您如何构建可以处理大量数据的分布式数据项目。
* [Streaming Data](https://www.manning.com/books/streaming-data) - 流数据介绍了流和实时数据系统的概念和要求。
* [Storm Applied](https://www.manning.com/books/storm-applied) - Storm Applied 是使用 Apache Storm 执行与处理和分析实时数据流相关的实际任务的实用指南。
* [Fundamentals of Stream Processing: Application Design, Systems, and Analytics](http://www.cambridge.org/us/academic/subjects/engineering/communications-and-signal-processing/fundamentals-stream-processing-application-design-systems-and-analytics) - 这本全面的实践指南结合了流处理的基本构建模块和新兴研究，非常适合应用程序设计人员、系统构建人员、分析开发人员以及该领域的学生和研究人员。
* [Stream Data Processing: A Quality of Service Perspective](http://www.springer.com/us/book/9780387710020) - 提出了一种适用于流和复杂事件处理的新范例。
* [Unified Log Processing](https://www.manning.com/books/event-streams-in-action) - 统一日志处理是在您的企业中实现事件流（Kafka 或 Kinesis）统一日志的实用指南
* [Kafka Streams in Action](https://www.manning.com/books/kafka-streams-in-action) - Kafka Streams in Action 教您对流入 Kafka 平台的数据实施流处理所需了解的一切，让您能够专注于从数据中获取更多信息，而无需牺牲时间或精力。
* [Big Data](https://www.manning.com/books/big-data) - 大数据教您使用一种架构构建大数据系统，该架构利用集群硬件以及专门为捕获和分析网络规模数据而设计的新工具。
* [Spark in Action](https://www.manning.com/books/spark-in-action) 和 [Spark in Action 第二版](https://www.manning.com/books/spark-in-action-second-edition) - Spark in Action 教您使用 Spark 有效处理批处理和流数据所需的理论和技能。 Spark 2.0 全面更新。
* [Kafka in Action](https://www.manning.com/books/kafka-in-action) - 《Kafka 实战》快速介绍了使用 Kafka 的各个方面，您需要真正获得它的好处。
* [Fusion in Action](https://www.manning.com/books/fusion-in-action-cx) - Fusion in Action 教您构建功能齐全的数据分析管道，包括文档和数据搜索以及分布式数据集群。
* [Reactive Data Handling](https://www.manning.com/books/reactive-data-handling) - 《反应式数据处理》是 Manuel Bernhardt 精选的五个章节的集合，向您介绍如何构建能够处理大数据负载实时处理的反应式应用程序 - 免费电子书！
* [Azure Data Engineering](https://www.manning.com/books/azure-data-engineering) - 一本关于一般数据工程和具体 Azure 平台的书
* [Grokking Streaming Systems](https://www.manning.com/books/grokking-streaming-systems) - Grokking 流媒体系统可帮助您了解流媒体系统是什么、它们如何工作以及它们是否适合您的业务。编写的内容与工具无关，无论您选择哪种框架，您都可以应用您所学到的知识。
* [Data Analysis with Python and PySpark](https://www.manning.com/books/data-analysis-with-python-and-pyspark) - 使用 PySpark 大规模构建数据驱动应用程序的教程。
* [Data Pipelines with Apache Airflow](https://www.manning.com/books/data-pipelines-with-apache-airflow) - 使用 Airflow 构建和维护数据管道的实用指南。

#### 分布式系统
* [Distributed Systems for fun and profit](http://book.mixu.net/distsys/) - 分布式系统理论。包括有关时间和排序、复制和不可能结果的部分。

#### 基于图的方法
* [Graph-Powered Machine Learning](https://www.manning.com/books/graph-powered-machine-learning) - 亚历山德罗·内格罗.结合图论和模型来改进机器学习项目

### 数据可视化
 * [数据可视化之美](https://www.youtube.com/watch?v=5Zg-C8AAIGg)
 * [与 Noah Iliinsky 一起设计数据可视化](https://www.youtube.com/watch?v=R-oiKt7bUU8)
 * [汉斯·罗斯林的 200 个国家，200 年，4 分钟](https://www.youtube.com/watch?v=jbkSRLYSojo)
 * [冰桶挑战数据可视化](https://www.youtube.com/watch?v=qTEchen97rQ)


# 其他很棒的列表
- 其他很棒的列表 [awesome-awesomeness](https://github.com/bayandin/awesome-awesomeness)。
- 更多列表[真棒](https://github.com/sindresorhus/awesome)。
- 另一个清单？ [列表](https://github.com/jnv/lists)。
- WTF！ [真棒-真棒-真棒](https://github.com/t3chnoboy/awesome-awesome-awesome)。
- 分析 [awesome-analytics](https://github.com/onurakpolat/awesome-analytics)。
- 公共数据集 [awesome-public-datasets](https://github.com/awesomedata/awesome-public-datasets)。
- 图分类 [awesome-graph-classification](https://github.com/benedekrozemberczki/awesome-graph-classification)。
- 网络嵌入 [awesome-network-embedding](https://github.com/chihming/awesome-network-embedding)。
- 社区检测 [awesome-community-detection](https://github.com/benedekrozemberczki/awesome-community-detection)。
- 决策树论文 [awesome-decision-tree-papers](https://github.com/benedekrozemberczki/awesome-decision-tree-papers)。
- 欺诈检测论文 [awesome-fraud-detection-papers](https://github.com/benedekrozemberczki/awesome-fraud-detection-papers)。
- 梯度增强论文 [awesome-gradient-boosting-papers](https://github.com/benedekrozemberczki/awesome-gradient-boosting-papers)。
- 蒙特卡洛树搜索论文 [awesome-monte-carlo-tree-search-papers](https://github.com/benedekrozemberczki/awesome-monte-carlo-tree-search-papers)。
- 卡夫卡 [awesome-kafka](https://github.com/monksy/awesome-kafka)。
- [Google Bigtable](https://github.com/zrosenbauer/awesome-bigtable)。
- 数据注释和标签工具 [awesome-open-data-annotation](https://github.com/zenml-io/awesome-open-data-annotation)。
