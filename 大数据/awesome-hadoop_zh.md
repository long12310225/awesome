# 很棒的 Hadoop [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

令人惊叹的 Hadoop 和 Hadoop 生态系统资源的精选列表。受到 [Awesome PHP](https://github.com/ziadoz/awesome-php)、[Awesome Python](https://github.com/vinta/awesome-python) 和 [Awesome Sysadmin](https://github.com/kahun/awesome-sysadmin) 的启发

- [很棒的 Hadoop](#awesome-hadoop)
	- [Hadoop](#hadoop)
	- [YARN](#yarn)
	- [NoSQL](#nosql)
	- [Hadoop 上的 SQL](#sql-on-hadoop)
	- [数据管理](#data-management)
	- [工作流程、生命周期和治理](#workflow-lifecycle-and-governance)
	- [数据摄取和集成](#data-ingestion-and-integration)
	- [DSL](#dsl)
	- [库和工具](#libraries-and-tools)
	- [实时数据处理](#realtime-data-processing)
	- [分布式计算与编程](#distributed-computing-and-programming)
	- [打包、配置和监控](#packaging-provisioning-and-monitoring)
	- [Monitoring](#monitoring)
	- [Search](#search)
	- [Security](#security)
	- [Benchmark](#benchmark)
	- [机器学习和大数据分析](#machine-learning-and-big-data-analytics)
	- [Misc.](#misc)
- [Resources](#resources)
	- [Websites](#websites)
	- [Presentations](#presentations)
	- [Books](#books)
	- [Hadoop 和大数据事件](#hadoop-and-big-data-events)
- [其他很棒的清单](#other-awesome-lists)

## Hadoop

* [Apache Hadoop](http://hadoop.apache.org/) - 阿帕奇Hadoop
* [Apache Hadoop Ozone](http://hadoop.apache.org/ozone/) - Apache Hadoop 的对象存储
* [Apache Tez](http://tez.apache.org/) - Hadoop 中基于 YARN 的数据处理应用程序框架
* [SpatialHadoop](http://spatialhadoop.cs.umn.edu/) - SpatialHadoop 是 Apache Hadoop 的 MapReduce 扩展，专门设计用于处理空间数据。
* [GIS Tools for Hadoop](http://esri.github.io/gis-tools-for-hadoop/) - Hadoop 框架的大数据空间分析
* [Elasticsearch Hadoop](https://github.com/elastic/elasticsearch-hadoop) - Elasticsearch 实时搜索和分析与 Hadoop 原生集成。支持 Map/Reduce、Cascading、Apache Hive 和 Apache Pig。
* [hadoopy](https://github.com/bwhite/hadoopy) - 用 Cython 编写的 Python MapReduce 库。
* [mrjob](https://github.com/Yelp/mrjob/) - mrjob 是一个 Python 2.5+ 包，可帮助您编写和运行 Hadoop Streaming 作业。
* [pydoop](http://pydoop.sourceforge.net/) - Pydoop 是一个为 Hadoop 提供 Python API 的包。
* [hdfs-du](https://github.com/twitter/hdfs-du) - HDFS-DU是Hadoop分布式文件系统的交互式可视化。
* [White Elephant](https://github.com/linkedin/white-elephant) - Hadoop 日志聚合器和仪表板
* [Genie](https://github.com/Netflix/genie) - Genie 提供 REST-ful API 来运行 Hadoop、Hive 和 Pig 作业，并管理多个 Hadoop 资源并在它们之间执行作业提交。
* [Apache Kylin](http://kylin.incubator.apache.org/) - Apache Kylin 是 eBay Inc. 的开源分布式分析引擎，在 Hadoop 上提供 SQL 接口和多维分析 (OLAP)，支持超大数据集
* [Crunch](https://github.com/jondot/crunch) - 基于 Go 的工具包，用于 Hadoop 上的 ETL 和特征提取
* [Apache Ignite](http://ignite.apache.org/) - 分布式内存平台

## 纱线

* [Apache Slider](http://slider.incubator.apache.org/) - Apache Slider 是 Apache 软件基金会正在孵化的一个项目，其目标是使现有应用程序能够轻松地部署到 YARN 集群上。
* [Apache Twill](http://twill.incubator.apache.org/) - Apache Twill 是 Apache Hadoop® YARN 的抽象，可降低开发分布式应用程序的复杂性，使开发人员能够更多地关注其应用程序逻辑。
* [mpich2-yarn](https://github.com/alibaba/mpich2-yarn) - 在 Yarn 上运行 MPICH2

## NoSQL
*下一代数据库主要解决一些问题：非关系型、分布式、开源和水平可扩展。*

* [Apache HBase](http://hbase.apache.org) - 阿帕奇HBase
* [Apache Phoenix](http://phoenix.apache.org/) - HBase 上的 SQL 皮肤支持二级索引
* [happybase](https://github.com/wbolster/happybase) - 一个开发人员友好的 Python 库，用于与 Apache HBase 交互。
* [Hannibal](https://github.com/sentric/hannibal) - Hannibal 是帮助监控和维护配置为手动拆分的 HBase 集群的工具。
* [Haeinsa](https://github.com/VCNC/haeinsa) - Haeinsa 是 HBase 的可线性扩展的多行、多表事务库
* [hindex](https://github.com/Huawei-Hadoop/hindex) - HBase 二级索引
* [Apache Accumulo](https://accumulo.apache.org/) - Apache Accumulo™ 排序的分布式键/值存储是一个强大的、可扩展的、高性能的数据存储和检索系统。
* [OpenTSDB](http://opentsdb.net/) - 可扩展的时间序列数据库
* [阿帕奇卡桑德拉](http://cassandra.apache.org/)

## Hadoop 上的 SQL
*Hadoop 上的 SQL*

* [Apache Hive](http://hive.apache.org) - Apache Hive 数据仓库软件有助于使用 SQL 读取、写入和管理驻留在分布式存储中的大型数据集
* [Apache Phoenix](http://phoenix.apache.org) HBase 上支持二级索引的 SQL 皮肤
* [Apache HAWQ (incubating)](http://hawq.incubator.apache.org/) - Apache HAWQ 是一个 Hadoop 原生 SQL 查询引擎，结合了 MPP 数据库的关键技术优势和 Hadoop 的可扩展性和便利性
* [Lingual](http://www.cascading.org/projects/lingual/) - 用于级联的 SQL 接口（MR/Tez 作业生成器）
* [Apache Impala](https://impala.apache.org/) - Apache Impala 是一个开源大规模并行处理 (MPP) SQL 查询引擎，用于存储在运行 Apache Hadoop 的计算机集群中的数据。 Impala 被描述为相当于 Google F1 的开源版本，这启发了它在 2012 年的开发。
* [Presto](https://prestodb.io/) - 用于大数据的分布式 SQL 查询引擎。由 Facebook 开源。
* [Apache Tajo](http://tajo.apache.org/) - Apache Hadoop 的数据仓库系统
* [Apache Drill](https://drill.apache.org/) - 无模式 SQL 查询引擎
* [阿帕奇Trafodion](http://trafodion.apache.org/)

## 数据管理

* [Apache Calcite](http://calcite.apache.org/) - 动态数据管理框架
* [Apache Atlas](http://atlas.incubator.apache.org/) - 元数据标记和沿袭捕获支持复杂的业务数据分类
* [Apache Kudu](https://kudu.apache.org/) - Kudu 提供快速插入/更新和高效列式扫描的组合，可在单个存储层上实现多个实时分析工作负载，从而补充 HDFS 和 Apache HBase。
* [Confluent Schema registry for Kafka](https://github.com/confluentinc/schema-registry) - 架构注册表为您的元数据提供服务层。它提供了一个用于存储和检索 Avro 模式的 RESTful 接口。
* [Hortonworks Schema Registry](https://github.com/hortonworks/registry) - SchemaRegistry是一个构建元数据存储库的框架。

## 工作流程、生命周期和治理

* [Apache Oozie](http://oozie.apache.org) - 阿帕奇 Oozie
* [Azkaban](http://azkaban.github.io/)
* [Apache Falcon](http://falcon.apache.org/) - 数据管理与处理平台
* [Apache NiFi](http://nifi.apache.org/) - 数据流系统
* [Apache AirFlow](https://github.com/apache/incubator-airflow) - Airflow 是一个工作流自动化和调度系统，可用于创作和管理数据管道
* [Luigi](http://luigi.readthedocs.org/en/latest/) - Python 包可帮助您构建复杂的批处理作业管道

## 数据摄取和集成

* [Apache Flume](http://flume.apache.org) - 阿帕奇水槽
* [Suro](https://github.com/Netflix/suro) - Netflix 的分布式数据管道
* [Apache Sqoop](http://sqoop.apache.org) - 阿帕奇·史考普
* [Apache Kafka](http://kafka.apache.org/) - 阿帕奇·卡夫卡
* [Gobblin from LinkedIn](https://github.com/linkedin/gobblin) - Hadoop 的通用数据摄取框架

## DSL

* [Apache Pig](http://pig.apache.org) - 阿帕奇猪
* [Apache DataFu](http://datafu.incubator.apache.org/) - 用于在 Hadoop 中处理大规模数据的库集合
* [vahara](https://github.com/thedatachef/varaha) - 使用 Apache Pig 进行机器学习和自然语言处理
* [packetpig](https://github.com/packetloop/packetpig) - 开源大数据安全分析
* [akela](https://github.com/mozilla-metrics/akela) - Mozilla 的 Hadoop、HBase、Pig 等实用程序库。
* [seqpig](http://seqpig.sourceforge.net/) - Hadoop 中大型测序数据集（例如：生物信息）的简单且可扩展的脚本编写
* [Lipstick](https://github.com/Netflix/Lipstick) - Pig工作流程可视化工具。 [A(pache) Pig 口红介绍](http://techblog.netflix.com/2013/06/introducing-lipstick-on-apache-pig.html)
* [PigPen](https://github.com/Netflix/PigPen) - PigPen 是 Clojure 或分布式 Clojure 的映射缩减。它编译为 Apache Pig，但您无需了解太多 Pig 即可使用它。

## 库和工具

* [Kite Software Development Kit](http://kitesdk.org/) - 一组库、工具、示例和文档
* [gohadoop](https://github.com/hortonworks/gohadoop) - Apache Hadoop YARN 的本机 go 客户端。
* [Hue](http://gethue.com/) - 用于使用 Apache Hadoop 分析数据的 Web 界面。
* [Apache Zeppelin](https://zeppelin.incubator.apache.org/) - 基于网络的笔记本，支持交互式数据分析
* [阿帕奇节俭](http://thrift.apache.org/)
* [Apache Avro](http://avro.apache.org/) - Apache Avro 是一个数据序列化系统。
* [Elephant Bird](https://github.com/twitter/elephant-bird) - Twitter 的 LZO 和 Protocol Buffer 相关 Hadoop、Pig、Hive 和 HBase 代码的集合。
* [Apache Hadoop 的 Spring](http://projects.spring.io/spring-hadoop/)
* [hdfs - HDFS 的原生 go 客户端](https://github.com/colinmarc/hdfs)
* [Oozie Eclipse Plugin](https://marketplace.eclipse.org/content/oozie-eclipse-plugin) - 用于在 Eclipse 内编辑 Apache Oozie 工作流程的图形编辑器。
* [snakebite](https://pypi.python.org/pypi/snakebite/) - 一个纯Python的HDFS客户端
* [Apache Parquet](https://parquet.apache.org/) - Apache Parquet 是一种列式存储格式，适用于 Hadoop 生态系统中的任何项目，无论选择何种数据处理框架、数据模型或编程语言。
* [Apache Superset (incubating)](https://superset.incubator.apache.org/) - Apache Superset（正在孵化）是一个现代的企业级商业智能 Web 应用程序
* [Schema Registry UI](https://github.com/Landoop/schema-registry-ui) - Confluence 模式注册表的 Web 工具，用于创建/查看/搜索/发展/查看历史记录并配置 Kafka 集群的 Avro 模式。

## 实时数据处理

* [阿帕奇风暴](http://storm.apache.org/)
* [阿帕奇萨姆扎](http://samza.apache.org/)
* [阿帕奇火花](http://spark.apache.org/streaming/)
* [Apache Flink](https://flink.apache.org) - Apache Flink 是一个高效、分布式、通用数据处理平台。它支持Exactly Once流处理。
* [Apache Pulsar (incubating)](http://pulsar.incubator.apache.org/) - Apache Pulsar（正在孵化）是一个在商用硬件上运行的高度可扩展、低延迟的消息传递平台。它提供了关于主题的简单发布-订阅语义、保证至少一次的消息传递、订阅者的自动游标管理以及跨数据中心复制。
* [Apache Druid (incubating)](http://druid.incubator.apache.org/) - 高性能、面向列的分布式数据存储。

## 分布式计算与编程

* [阿帕奇火花](http://spark.apache.org/)
 * [Spark Packages](http://spark-packages.org/) - Apache Spark 软件包的社区索引
 * [SparkHub](https://sparkhub.databricks.com/) - Apache Spark 社区网站
* [阿帕奇紧缩](http://crunch.apache.org)
* [Cascading](http://www.cascading.org/) - Cascading 是经过验证的应用程序开发平台，用于在 Hadoop 上构建数据应用程序。
* [Apache Flink](http://flink.apache.org/) - Apache Flink 是一个高效、分布式、通用数据处理平台。
* [Apache Apex (incubating)](http://apex.incubator.apache.org/) - 企业级统一流批处理引擎。
* [Apache Livy (incubating)](https://livy.incubator.apache.org/) - Apache Livy（孵化中）是一种 Web 服务，它公开一个 REST 接口，用于管理集群中长期运行的 Apache Spark 上下文。借助 Livy，可以在 Apache Spark 之上构建需要与许多 Spark 上下文进行细粒度交互的新应用程序。

## 打包、配置和监控

* [Apache Bigtop](http://bigtop.apache.org/) - Apache Bigtop：Apache Hadoop 生态系统的打包和测试
* [Apache Ambari](http://ambari.apache.org/) - 阿帕奇·安巴里
* [Ganglia监控系统](http://ganglia.sourceforge.net/)
* [ankush](https://github.com/impetus-opensource/ankush) - 一个大数据集群管理工具，用于创建和管理不同技术的集群。
* [Apache Zookeeper](http://zookeeper.apache.org/) - 阿帕奇动物园管理员
* [Apache Curator](http://curator.apache.org/) - ZooKeeper 客户端包装器和丰富的 ZooKeeper 框架
* [inviso](https://github.com/Netflix/inviso) - Inviso 是一个轻量级工具，提供搜索 Hadoop 作业、可视化性能和查看集群利用率的功能。
* [Logit.io](https://logit.io/) - 将日志从 Hadoop 发送到 Elasticsearch 以进行监控和警报。


## 搜索

* [ElasticSearch](https://www.elastic.co/)
* [Apache Solr](http://lucene.apache.org/solr/) - Apache Solr 是一个基于名为 Lucene 的 Java 库构建的开源搜索平台。
* [Banana](https://github.com/LucidWorks/banana) - Apache Solr 的 Kibana 端口

## 搜索引擎框架

* [Apache Nutch](http://nutch.apache.org/) - Apache Nutch 是一个高度可扩展和可扩展的开源网络爬虫软件项目。

## 安全性

* [Apache Ranger](http://ranger.incubator.apache.org/) - Ranger 是一个用于在 Hadoop 平台上启用、监控和管理全面数据安全性的框架。
* [Apache Sentry](https://sentry.incubator.apache.org/) - Hadoop 的授权模块
* [Apache Knox Gateway](https://knox.apache.org/) - 用于与 Hadoop 集群交互的 REST API 网关。

## 基准测试

* [大数据基准](https://amplab.cs.berkeley.edu/benchmark/)
* [HiBench](https://github.com/intel-hadoop/HiBench)
* [YCSB](https://github.com/brianfrankcooper/YCSB) - 雅虎！云服务基准（YCSB）是一个开源规范和程序套件，用于评估计算机程序的检索和维护能力。它通常用于比较 NoSQL 数据库管理系统的相对性能。

## 机器学习和大数据分析

* [阿帕奇马胡特](http://mahout.apache.org)
* [Oryx 2](https://github.com/OryxProject/oryx) - Spark、Kafka 上的 Lambda 架构用于实时大规模机器学习
* [MLlib](https://spark.apache.org/mllib/) - MLlib 是 Apache Spark 的可扩展机器学习库。
* [R](http://www.r-project.org/) - R 是一个用于统计计算和图形的免费软件环境。
* [RHadoop](https://github.com/RevolutionAnalytics/RHadoop/wiki) 包括 RHDFS、RHBase、RMR2、plyrmr
* [阿帕奇镜头](http://lens.apache.org/)
* [Apache SINGA (incubating)](https://singa.incubator.apache.org/) - SINGA 是一个通用分布式深度学习平台，用于在大型数据集上训练大型深度学习模型
* [BigDL](https://bigdl-project.github.io/) - BigDL 是 Apache Spark 的分布式深度学习库；借助 BigDL，用户可以将深度学习应用程序编写为标准 Spark 程序，这些程序可以直接在现有 Spark 或 Hadoop 集群之上运行。
* [Apache Hivemall (incubating)](http://hivemall.incubator.apache.org/) - Apache Hivemall 是一个可扩展的机器学习库，运行在 Apache Hive、Spark 和 Pig 上。

## 杂项。

* Hive 插件
* UDF
* https://github.com/edwardcapriolo/hive_cassandra_udfs
* https://github.com/livingsocial/HiveSwarm
* https://github.com/ThinkBigAnalytics/Hive-Extensions-from-Think-Big-Analytics
* https://github.com/twitter/elephant-bird - 推特
* https://github.com/lovelysystems/ls-hive
* https://github.com/klout/brickhouse
* 存储处理程序
* https://github.com/dvasilen/Hive-Cassandra
* https://github.com/yc-huang/Hive-mongo
* https://github.com/balshor/gdata-storagehandler
* https://github.com/chimpler/hive-solr
* https://github.com/bfemiano/accumulo-hive-storage-manager
* 库和工具
* https://github.com/forward3d/rbhive
* https://github.com/synctree/activerecord-hive-adapter
* https://github.com/hrp/sequel-hive-adapter
* https://github.com/forward/node-hive
* https://github.com/recruitcojp/WebHive
     * [shib](https://github.com/tagomoris/shib) - 用于查询引擎的 WebUI：Hive 和 Presto
* https://github.com/dmorel/Thrift-API-HiveClient2（Perl - HiveServer2）
     * [PyHive](https://github.com/dropbox/PyHive) - Hive 和 Presto 的 Python 接口
* https://github.com/recruitcojp/OdbcHive
     * [HiveRunner](https://github.com/klarna/HiveRunner) - 基于 JUnit4 的 hadoop hive 查询的开源单元测试框架
     * [Beetest](https://github.com/kawaa/Beetest) - 一个超级简单的实用程序，用于为非 Java 开发人员本地测试 Apache Hive 脚本。
     * [Hive_test](https://github.com/edwardcapriolo/hive_test) - hive 和 hive-service 的单元测试框架
* Flume插件
  * [Flume MongoDB 接收器](https://github.com/leonlee/flume-ng-mongodb-sink)
  * [Flume RabbitMQ 源和接收器](https://github.com/jcustenborder/flume-ng-rabbitmq)
  * [Flume UDP 源](https://github.com/whitepages/flume-udp-source)
  * [.Net FlumeNG 客户端](https://github.com/marksl/DotNetFlumeNG.Clients)

# 资源
各种资源，例如书籍、网站和文章。

## 网站
*有用的网站和文章*

* [Hadoop 周刊](http://www.hadoopweekly.com/)
* [Hadoop 生态系统表](http://hadoopecosystemtable.github.io/)
* [Hadoop illuminated](http://hadoopilluminated.com/) - 开源 Hadoop 书籍
* [AWS 大数据博客](http://blogs.aws.amazon.com/bigdata/)
* [Hadoop360](http://www.hadoop360.com/)
* [如何监控 Hadoop 指标](https://www.datadoghq.com/blog/monitor-hadoop-metrics/)

## 演讲

* [Apache Hadoop 的理论与实践](http://www.slideshare.net/AdamKawa/hadoop-intheoryandpractice)
* [LinkedIn 的 Hadoop 运营](http://www.slideshare.net/allenwittenauer/2013-hadoopsummitemea)
* [LinkedIn 的 Hadoop 性能](http://www.slideshare.net/allenwittenauer/2012-lihadoopperf)
* [基于 Docker 的 Hadoop 配置](http://www.slideshare.net/JanosMatyas/docker-based-hadoop-provisioning)

## 书籍

* [Hadoop：权威指南](http://www.amazon.com/gp/product/1449311520/ref=as_li_ss_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=1449311520&linkCode=as2&tag=matratsblo-20)
* [Hadoop 操作](http://www.amazon.com/gp/product/1449327052/ref=as_li_ss_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=1449327052&linkCode=as2&tag=matratsblo-20)
* [Apache Hadoop 纱线](http://www.amazon.com/dp/0321934504?tag=matratsblo-20)
* [HBase：权威指南](http://shop.oreilly.com/product/0636920014348.do)
* [编程猪](http://shop.oreilly.com/product/0636920018087.do)
* [蜂巢编程](http://shop.oreilly.com/product/0636920023555.do)
* [Hadoop 实践，第二版](http://www.manning.com/holmes2/)
* [Hadoop 实战，第二版](http://www.manning.com/lam2/)

## Hadoop 和大数据事件
* [ApacheCon](http://www.apachecon.com/)
* [Strata + Hadoop 世界](http://conferences.oreilly.com/strata)
* [数据工场峰会](https://dataworkssummit.com/)
* [星火峰会](https://databricks.com/sparkaisummit)

# 其他很棒的列表
其他令人惊叹的很棒的列表可以在 [awesome-awesomeness](https://github.com/bayandin/awesome-awesomeness) 和 [awesome](https://github.com/sindresorhus/awesome) 列表中找到。
