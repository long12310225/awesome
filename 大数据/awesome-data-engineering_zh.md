# 很棒的数据工程 [![Awesome](https://awesome.re/badge-flat2.svg)](https://github.com/sindresorhus/awesome)

> 与数据工程相关的精彩内容的精选列表。

## 内容

- [Databases](#databases)
- [数据对比](#data-comparison)
- [数据摄取](#data-ingestion)
- [文件系统](#file-system)
- [序列化格式](#serialization-format)
- [流处理](#stream-processing)
- [批处理](#batch-processing)
- [图表和仪表板](#charts-and-dashboards)
- [Workflow](#workflow)
- [数据湖管理](#data-lake-management)
- [ELK Elastic Logstash Kibana](#elk-elastic-logstash-kibana)
- [Docker](#docker)
- [Datasets](#datasets)
  - [Realtime](#realtime)
  - [数据转储](#data-dumps)
- [Monitoring](#monitoring)
  - [Prometheus](#prometheus)
- [Profiling](#profiling)
  - [数据分析器](#data-profiler)
- [Testing](#testing)
- [Community](#community)
  - [Forums](#forums)
  - [Conferences](#conferences)
  - [Podcasts](#podcasts)
  - [Books](#books)

## 数据库

- 关系型
  - [RQLite](https://github.com/rqlite/rqlite) - 使用 Raft 共识协议复制 SQLite。
  - [MySQL](https://www.mysql.com/) - 世界上最受欢迎的开源数据库。
    - [TiDB](https://github.com/pingcap/tidb) - 兼容MySQL协议的分布式NewSQL数据库。
    - [Percona XtraBackup](https://www.percona.com/software/mysql-database/percona-xtrabackup) - 适用于所有版本的 Percona Server、MySQL® 和 MariaDB® 的免费、开源、完整的在线备份解决方案。
    - [mysql_utils](https://github.com/pinterest/mysql_utils) - Pinterest MySQL 管理工具。
  - [MariaDB](https://mariadb.org/) - MySQL 的增强型直接替代品。
  - [PostgreSQL](https://www.postgresql.org/) - 世界上最先进的开源数据库。
  - [Rivestack](https://rivestack.io/) - 使用 pgvector 管理用于 AI 工作负载的 PostgreSQL。 HNSW 索引、低于 4 毫秒的延迟以及具有自动嵌入生成功能的内置 SQL 编辑器。
  - [Amazon RDS](https://aws.amazon.com/rds/) - 可以轻松地在云中设置、操作和扩展关系数据库。
  - [Crate.IO](https://crate.io/) - 具有 NOSQL 功能的可扩展 SQL 数据库。
- 键值
  - [Redis](https://redis.io/) - 一个开源、BSD 许可的高级键值缓存和存储。
  - [Riak](https://docs.basho.com/riak/kv/) - 分布式数据库，旨在通过将数据分布在多个服务器上来提供最大的数据可用性。
  - [AWS DynamoDB](https://aws.amazon.com/dynamodb/) - 快速灵活的 NoSQL 数据库服务，适用于任何规模都需要一致的个位数毫秒延迟的所有应用程序。
  - [HyperDex](https://github.com/rescrv/HyperDex) - 可扩展、可搜索的键值存储。已弃用。
  - [SSDB](https://ssdb.io) - 支持多种数据结构的高性能NoSQL数据库，是Redis的替代品。
  - [Kyoto Tycoon](https://github.com/alticelabs/kyoto) - 京都内阁键值数据库之上的轻量级网络服务器，专为高性能和并发性而构建。
  - [IonDB](https://github.com/iondbproject/iondb) - 用于微控制器和物联网应用的键值存储。
- 专栏
  - [Cassandra](https://cassandra.apache.org/) - 当您需要可扩展性和高可用性而不影响性能时，这是正确的选择。
    - [Cassandra Calculator](https://www.ecyrd.com/cassandracalculator/) - 这个简单的表单允许您尝试 Apache Cassandra 集群的不同值，并查看对您的应用程序的影响。
    - [CCM](https://github.com/pcmanus/ccm) - 用于在本地主机上轻松创建和销毁 Apache Cassandra 集群的脚本。
    - [ScyllaDB](https://github.com/scylladb/scylla) - NoSQL数据存储采用seastar框架，兼容Apache Cassandra。
  - [HBase](https://hbase.apache.org/) - Hadoop 数据库，一种分布式、可扩展的大数据存储。
  - [AWS Redshift](https://aws.amazon.com/redshift/) - 快速、完全托管的 PB 级数据仓库，使使用现有商业智能工具分析所有数据变得简单且经济高效。
  - [FiloDB](https://github.com/filodb/FiloDB) - 分布式。柱状。版本化。流媒体。 SQL。
  - [Vertica](https://www.vertica.com) - 具有广泛分析 SQL 的分布式 MPP 列式数据库。
  - [ClickHouse](https://clickhouse.tech) - 用于 OLAP 的分布式列式 DBMS。 SQL。
- 文件
  - [MongoDB](https://www.mongodb.com) - 一个开源文档数据库，旨在简化开发和扩展。
    - [Percona Server for MongoDB](https://www.percona.com/software/mongo-database/percona-server-for-mongodb) - Percona Server for MongoDB® 是 MongoDB® Community Edition 的免费、增强、完全兼容、开源、直接替代品，包含企业级特性和功能。
    - [MemDB](https://github.com/rain1017/memdb) - 分布式事务内存数据库（基于 MongoDB）。
  - [Elasticsearch](https://www.elastic.co/) - 实时搜索和分析数据。
  - [Couchbase](https://www.couchbase.com/) - 性能最高的 NoSQL 分布式数据库。
  - [RethinkDB](https://rethinkdb.com/) - 实时网络的开源数据库。
  - [RavenDB](https://ravendb.net/) - 完全事务性 NoSQL 文档数据库。
- 图表
  - [ArcadeDB](https://arcadedb.com/) - 具有本机图形、文档、键值和向量支持的开源多模型数据库。 SQL、Cypher 和 Gremlin 查询语言。阿帕奇 2.0 许可证。
  - [Neo4j](https://neo4j.com/) - 全球领先的图数据库。
  - [Omnigraph](https://github.com/ModernRelay/omnigraph) - 类型化图形数据库，其中代理像 Git 一样进行分支和合并。 S3 原生、Rust、遍历 + 矢量 + BM25 在一个运行时中。
  - [OrientDB](https://orientdb.com) - 第二代分布式图形数据库，在一个产品中具有文档的灵活性，并具有开源商业友好许可证。
  - [ArangoDB](https://www.arangodb.com/) - 分布式免费开源数据库，具有灵活的文档、图形和键值数据模型。
  - [Titan](https://titan.thinkaurelius.com) - 一个可扩展的图形数据库，经过优化，可存储和查询包含分布在多机集群中的数千亿个顶点和边的图形。
  - [FlockDB](https://github.com/twitter-archive/flockdb) - Twitter 的分布式容错图形数据库。已弃用。
  - [Actionbase](https://github.com/kakao/actionbase) - 以图表形式表示的用户交互（点赞、查看、关注）的数据库，并实时提供预先计算的读取。
- 分布式
  - [DAtomic](https://www.datomic.com) - 完全事务性、云就绪、分布式数据库。
  - [Apache Geode](https://geode.apache.org/) - 用于横向扩展应用程序的开源分布式内存数据库。
  - [Gaffer](https://github.com/gchq/Gaffer) - 大型图数据库。
- 时间序列
  - [InfluxDB](https://github.com/influxdata/influxdb) - 用于指标、事件和实时分析的可扩展数据存储。
  - [OpenTSDB](https://github.com/OpenTSDB/opentsdb) - 可扩展的分布式时间序列数据库。
  - [QuestDB](https://questdb.io/) - 面向列的关系数据库，专为时间序列和事件数据的实时分析而设计。
  - [kairosdb](https://github.com/kairosdb/kairosdb) - 快速可扩展的时间序列数据库。
  - [Heroic](https://github.com/spotify/heroic) - Spotify 推出的基于 Cassandra 和 Elasticsearch 的可扩展时间序列数据库。
  - [Druid](https://github.com/apache/incubator-druid) - 面向列的分布式数据存储非常适合为交互式应用程序提供支持。
  - [Riak-TS](https://basho.com/products/riak-ts/) - Riak TS 是唯一专门针对物联网和时间序列数据进行优化的企业级 NoSQL 时间序列数据库。
  - [Akumuli](https://github.com/akumuli/Akumuli) - 数字时间序列数据库。它可用于实时捕获、存储和处理时间序列数据。 “akumuli”这个词可以从世界语翻译为“积累”。
  - [Rhombus](https://github.com/Pardot/Rhombus) - Cassandra 的时间序列对象存储，可处理构建宽行索引的所有复杂性。
  - [Dalmatiner DB](https://github.com/dalmatinerdb/dalmatinerdb) - 快速分布式指标数据库。
  - [Blueflood](https://github.com/rackerlabs/blueflood) - 旨在摄取和处理时间序列数据的分布式系统。
  - [Timely](https://github.com/NationalSecurityAgency/timely) - 一个时间序列数据库应用程序，提供基于 Accumulo 和 Grafana 的时间序列数据的安全访问。
- 其他
  - [Tarantool](https://github.com/tarantool/tarantool/) - 内存数据库和应用程序服务器。
  - [GreenPlum](https://github.com/greenplum-db/gpdb) - Greenplum 数据库 (GPDB) - 一个先进的、功能齐全的开源数据仓库。它提供对 PB 级数据量的强大而快速的分析。
  - [cayley](https://github.com/cayleygraph/cayley) - 一个开源图形数据库。谷歌。
  - [Snappydata](https://github.com/SnappyDataInc/snappydata) - 基于 Apache Spark 构建的 OLTP + OLAP 数据库。
  - [TimescaleDB](https://www.timescale.com/) - TimescaleDB 作为 PostgreSQL 之上的扩展构建，是一个时间序列 SQL 数据库，提供快速分析、可扩展性，并在经过验证的存储引擎上提供自动化数据管理。
  - [DuckDB](https://duckdb.org/) - 快速的进程内分析数据库，具有零外部依赖性，在 Linux/macOS/Windows 上运行，提供丰富的 SQL 方言，并且免费且可扩展。
  - [SlothDB](https://github.com/SouravRoy-ETL/slothdb) - 用 C++20 编写的进程内分析 SQL 数据库。直接读取 Parquet、CSV、JSON、Avro、Arrow、SQLite 和 Excel。浏览器的单个二进制、Python 包和 1.3 MB WASM 构建。
  - [chDB](https://chdb.io) - 嵌入式 ClickHouse — 完整的 ClickHouse SQL 方言、约 80 种数据格式和 12+ 核心源连接器（S3、Postgres、MongoDB、Kafka、Iceberg）。 Python、Go、Rust、Node、Bun、Zig 和 Ruby 绑定。

## 数据对比

- [datacompy](https://github.com/capitalone/datacompy) - 一个 Python 库，有助于比较 Pandas、Polars、Spark 等中的两个 DataFrame。该库超越了基本的相等性检查，提供了对行和列级别差异的详细见解。
- [dvt](https://github.com/GoogleCloudPlatform/professional-services-data-validator) - 数据验证工具比较源表和目标表中的数据以确保它们匹配。它提供列验证、行验证、架构验证、自定义查询验证和即席 SQL 探索。
- [koala-diff](https://github.com/godalida/koala-diff) - 一个高性能 Python 库，用于使用 Rust 和 Polars 在本地比较大型数据集（CSV、Parquet）。它具有零拷贝流式传输功能，可防止 OOM 错误并生成交互式 HTML 数据质量报告。
- [FutureSearch SDK](https://github.com/futuresearch/futuresearch-python) - Python SDK，可跨系统调度并行网络研究代理
表行，将多代理结果合成到结构化列中。

## 数据摄取

- [DataSpoc Pipe](https://github.com/dataspoclab/dataspoc-pipe) - 数据摄取引擎，可将 400 多个 Singer Tap 连接到云存储桶（S3、GCS、Azure）中的 Parquet 文件。流式、增量式、带自动目录。
- [Enrich.sh](https://enrich.sh) - 托管事件摄取服务，可将发送到 REST API 的 JSON 转换为 Cloudflare R2 上的 Hive 分区 Parquet，可从 DuckDB、ClickHouse、BigQuery、Snowflake 和 Python 进行查询。
- [ingestr](https://github.com/bruin-data/ingestr) - CLI 工具，可使用单个命令在数据库之间复制数据。支持 50 多个来源，包括 PostgreSQL、MySQL、MongoDB、Salesforce、Shopify 到任何数据仓库。
- [Kafka](https://kafka.apache.org/) - 发布-订阅消息传递被重新考虑为分布式提交日志。
  - [BottledWater](https://github.com/confluentinc/bottledwater-pg) - 将数据捕获从 PostgreSQL 更改为 Kafka。已弃用。
  - [kafkat](https://github.com/airbnb/kafkat) - 简化了 Kafka 代理的命令行管理。
  - [kafkacat](https://github.com/edenhill/kafkacat) - 通用命令行非 JVM Apache Kafka 生产者和消费者。
  - [pg-kafka](https://github.com/xstevens/pg_kafka) - 用于向 Apache Kafka 生成消息的 PostgreSQL 扩展。
  - [librdkafka](https://github.com/edenhill/librdkafka) - Apache Kafka C/C++ 库。
  - [kafka-docker](https://github.com/wurstmeister/kafka-docker) - Docker 中的卡夫卡。
  - [kafka-manager](https://github.com/yahoo/kafka-manager) - 用于管理 Apache Kafka 的工具。
  - [kafka-node](https://github.com/SOHU-Co/kafka-node) - Apache Kafka 0.8 的 Node.js 客户端。
  - [Secor](https://github.com/pinterest/secor) - Pinterest 的 Kafka 到 S3 分布式消费者。
  - [Kafka-logger](https://github.com/uber/kafka-logger) - 来自 Uber 的 Node.js Kafka-winston 记录器。
  - [Kroxylicious](https://github.com/kroxylicious/kroxylicious) - Kafka 代理，解决静态加密 Kafka 数据等问题。
- [AWS Kinesis](https://aws.amazon.com/kinesis/) - 一种完全托管的基于云的服务，用于对大型分布式数据流进行实时数据处理。
- [RabbitMQ](https://www.rabbitmq.com/) - 强大的应用程序消息传递。
- [dlt](https://www.dlthub.com) - 一个针对Python数据开发人员的快速简单的管道构建库，可以在笔记本、云函数、气流等中运行。
- [drt](https://github.com/drt-hub/drt) - OSS 反向 ETL CLI。通过 YAML 将数据从仓库同步到业务工具。
- [FluentD](https://www.fluentd.org) - 用于统一日志记录层的开源数据收集器。
- [Embulk](https://www.embulk.org) - 开源批量数据加载器，可帮助在各种数据库、存储、文件格式和云服务之间传输数据。
- [Apache Sqoop](https://sqoop.apache.org) - 一种设计用于在 Apache Hadoop 和结构化数据存储（例如关系数据库）之间高效传输批量数据的工具。
- [Heka](https://github.com/mozilla-services/heka) - 数据采集​​和处理变得简单。已弃用。
- [Gobblin](https://github.com/apache/incubator-gobblin) - LinkedIn 的 Hadoop 通用数据摄取框架。
- [Nakadi](https://nakadi.io) - 一个开源事件消息传递平台，在类似 Kafka 的队列之上提供 REST API。
- [Pravega](https://www.pravega.io) - 为连续且无界的数据提供新的存储抽象 - 流。
- [Apache Pulsar](https://pulsar.apache.org/) - 开源分布式发布-订阅消息系统。
- [AWS Data Wrangler](https://github.com/awslabs/aws-data-wrangler) - 用于处理 AWS 上数据的实用带。
- [Airbyte](https://airbyte.io/) - 适合现代数据团队的开源数据集成。
- [DBConvert Streams](https://streams.dbconvert.com) - 具有内置 SQL IDE 的自托管数据库迁移和变更数据捕获 (CDC) 工具。
- [Artie](https://www.artie.com/) - 利用变更数据捕获的实时数据摄取工具。
- [Sling](https://slingdata.io/) - CLI 数据集成工具专门用于在数据库和存储系统之间移动数据。
- [Meltano](https://meltano.com/) - CLI 和代码优先 ELT。
  - [Singer SDK](https://sdk.meltano.com) - 构建符合 Singer Spec 的自定义数据提取器和加载器的最快方法。
- [Google Sheets ETL](https://github.com/fulldecent/google-sheets-etl) - 将所有 Google 表格实时导入到数据仓库中。
- [CsvPath Framework](https://www.csvpath.org/) - 一个分隔数据预登框架，填补了 MFT 和数据湖之间的空白。
- [Estuary Flow](https://estuary.dev) - 无代码/低代码数据管道平台，可处理批量和实时数据摄取。
- [db2lake](https://github.com/bahador-r/db2lake) - 用于数据库→数据湖/仓库的轻量级 Node.js ETL 框架。
- [data-genie](https://github.com/pujansrt/data-genie) - 适用于 Node.js 和 TypeScript 的高性能、流优先 ETL 引擎，具有恒定的内存占用量。
- [Kreuzberg](https://github.com/kreuzberg-dev/kreuzberg) - 具有 Rust 核心和 Python、TypeScript、Go 等绑定的多语言文档智能库。从 62 多种文档格式中提取文本、表格和元数据以进行数据管道摄取。
- [pdfmux](https://github.com/NameetP/pdfmux) - Python PDF 到 Markdown 协调器。对每个页面进行分类并路由到最佳后端（PyMuPDF、Docling、RapidOCR、Gemini Flash），发出 Markdown 以及每页置信度分数，以便摄取管道可以在提供 LLM 或检索之前隔离低信任页面。
- [DataRaven](https://dataraven.io/) - 用于摄取工作流程的托管云对象存储传输。
- [Xquik](https://xquik.com) - 实时 X (Twitter) 数据提取平台，具有 REST API（76 个端点）、20 个批量提取工具、帐户监控、HMAC 签名的 Webhooks 和用于 AI 代理集成的 MCP 服务器。
- [Arpe.io](https://www.arpe.io/) - 用于数据库导出、导入、复制和迁移的高速 CLI 工具，可并行流式传输到 CSV、Parquet、JSON 和云存储，支持 PostgreSQL、MySQL、Oracle、SQL Server 和 80 多个源。
- [Crustdata](https://crustdata.com) - 用于公司和人员智能的实时 B2B 数据 API，通过 REST API 和用于数据丰富管道的 Webhook 提供公司统计、员工人数信号、职位列表、网络流量和融资事件。
- [crdt-merge](https://github.com/mgillr/crdt-merge) - DataFrame、JSON、ML 模型和分布式代理的无冲突合并 — 由 CRDT 提供支持。
- [LinkedIn Jobs Scraper](https://apify.com/cryptosignals/linkedin-jobs-scraper) - 基于 Crawlee 的参与者无需 API 密钥即可大规模提取结构化 LinkedIn 职位列表。
- [CARQ](https://github.com/whispering3/CARQ) - 上下文感知 RAG 处理队列，实现高可用性和自适应速率限制。

## 文件系统

- [HDFS](https://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-hdfs/HdfsDesign.html) - 设计用于在商用硬件上运行的分布式文件系统。
  - [Snakebite](https://github.com/spotify/snakebite) - 一个纯Python HDFS 客户端。
- [AWS S3](https://aws.amazon.com/s3/) - 对象存储旨在从任何地方检索任意数量的数据。
  - [smart_open](https://github.com/RaRe-Technologies/smart_open) - 用于流式传输大文件的实用程序（S3、HDFS、gzip、bz2）。
- [Alluxio](https://www.alluxio.org/) - 以内存为中心的分布式存储系统，能够跨集群框架（例如 Spark 和 MapReduce）以内存速度可靠地共享数据。
- [CEPH](https://ceph.com/) - 统一的分布式存储系统，旨在实现卓越的性能、可靠性和可扩展性。
- [JuiceFS](https://github.com/juicedata/juicefs) - 由对象存储驱动的高性能云原生文件系统，用于大规模数据存储。
- [OrangeFS](https://www.orangefs.org/) - Orange文件系统是并行虚拟文件系统的一个分支。
- [SnackFS](https://github.com/tuplejump/snackfs-release) - 一个基于 Cassandra 构建的小型、轻量级 HDFS 兼容文件系统。
- [GlusterFS](https://www.gluster.org/) - Gluster 文件系统。
- [XtreemFS](https://www.xtreemfs.org/) - 满足所有存储需求的容错分布式文件系统。
- [SeaweedFS](https://github.com/chrislusf/seaweedfs) - Seaweed-FS 是一个简单且高度可扩展的分布式文件系统。有两个目标：存储数十亿个文件！快速提供文件！ Seaweed-FS 选择仅实现密钥到文件映射，而不是支持完整的 POSIX 文件系统语义。与“NoSQL”一词类似，您可以将其称为“NoFS”。
- [S3QL](https://github.com/s3ql/s3ql/) - 使用 Google Storage、Amazon S3 或 OpenStack 等存储服务在线存储所有数据的文件系统。
- [LizardFS](https://lizardfs.com/) - 软件定义存储是一种分布式、并行、可扩展、容错、地理冗余和高可用的文件系统。

## 序列化格式

- [AKF](https://github.com/HMAKT99/AKF) - AI 原生文件格式。嵌入 20 多种格式（DOCX、PDF、图像、代码）的信任分数、来源来源和合规性元数据。 AI 的 EXIF。
- [Apache Avro](https://avro.apache.org) - Apache Avro™ 是一个数据序列化系统。
- [Apache Parquet](https://parquet.apache.org) - 一种可用于 Hadoop 生态系统中任何项目的列式存储格式，无论选择何种数据处理框架、数据模型或编程语言。
  - [Snappy](https://github.com/google/snappy) - 快速压缩器/解压缩器。与镶木地板一起使用。
  - [PigZ](https://zlib.net/pigz/) - 适用于现代多处理器、多核机器的 gzip 并行实现。
- [Apache ORC](https://orc.apache.org/) - 适用于 Hadoop 工作负载的最小、最快的列式存储。
- [Apache Thrift](https://thrift.apache.org) - Apache Thrift 软件框架，用于可扩展的跨语言服务开发。
- [ProtoBuf](https://github.com/protocolbuffers/protobuf) - Protocol Buffers - Google 的数据交换格式。
- [SequenceFile](https://wiki.apache.org/hadoop/SequenceFile) - 由二进制键/值对组成的平面文件。它在 MapReduce 中广泛用作输入/输出格式。
- [Kryo](https://github.com/EsotericSoftware/kryo) - 一个快速高效的 Java 对象图序列化框架。
- [PFC-JSONL](https://github.com/ImpossibleForge/pfc-jsonl) - 具有块级时间戳索引和 DuckDB 集成的专用 JSONL 日志压缩器。通过时间范围随机访问查询实现约 9% 的压缩率（优于 gzip）。

## 流处理

- [Apache Beam](https://beam.apache.org/) - 一种统一的编程模型，可实现在许多执行引擎上运行的批处理和流数据处理作业。
- [Spark Streaming](https://spark.apache.org/streaming/) - 可以轻松构建可扩展的容错流应用程序。
- [Apache Flink](https://flink.apache.org/) - 流数据流引擎，为数据流上的分布式计算提供数据分发、通信和容错。
- [Apache Storm](https://storm.apache.org) - 一个免费开源的分布式实时计算系统。
- [Apache Samza](https://samza.apache.org) - 分布式流处理框架。
- [Apache NiFi](https://nifi.apache.org/) - 一个易于使用、功能强大且可靠的系统，用于处理和分发数据。
- [Apache Hudi](https://hudi.apache.org/) - 一个用于管理实时处理存储的开源框架，最有趣的功能之一是 Upsert。
- [CocoIndex](https://github.com/cocoindex-io/cocoindex) - 一个开源 ETL 框架，用于为 AI 构建新索引。
- [VoltDB](https://voltdb.com/) - 符合 ACID 的 RDBMS，使用[无共享架构](https://en.wikipedia.org/wiki/Shared-nothing_architecture)。
- [PipelineDB](https://github.com/pipelinedb/pipelinedb) - 流式 SQL 数据库。
- [Spring Cloud Dataflow](https://cloud.spring.io/spring-cloud-dataflow/) - Spring Boot 应用程序之间的流传输和任务执行。
- [Bonobo](https://www.bonobo-project.org/) - 适用于 python 3.5+ 的数据处理工具包。
- [Robinhood's Faust](https://github.com/faust-streaming/faust) - 永远可扩展的事件处理和内存中持久的 K/V 存储作为具有异步和静态类型的库。
- [HStreamDB](https://github.com/hstreamdb/hstream) - 专为物联网数据存储和实时处理而构建的流数据库。
- [Kuiper](https://github.com/emqx/kuiper) - 由Golang实现的边缘轻量级物联网数据分析/流媒体软件，可以在各种资源受限的边缘设备上运行。
- [Zilla](https://github.com/aklivity/zilla) - - 专为事件驱动架构和流媒体构建的 API 网关，支持 HTTP、SSE、gRPC、MQTT 和本机 Kafka 协议等标准协议。
- [SwimOS](https://github.com/swimos/swim-rust) - 用于构建支持各种摄取源的实时流数据处理应用程序的框架。
- [Pathway](https://github.com/pathwaycom/pathway) - 具有 Rust 运行时的高性能开源 Python ETL 框架，支持 300 多个数据源。

## 批处理

- [Hadoop MapReduce](https://hadoop.apache.org/docs/current/hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapReduceTutorial.html) - 一种软件框架，用于轻松编写应用程序，以可靠、容错的方式在大型集群（数千个节点）上并行处理商品硬件的大量数据（多 TB 数据集）。
- [Spark](https://spark.apache.org/) - 用于在单节点机器或集群上执行数据工程、数据科学和机器学习的多语言引擎。
  - [Spark Packages](https://spark-packages.org) - Apache Spark 软件包的社区索引。
  - [Deep Spark](https://github.com/Stratio/deep-spark) - 将 Apache Spark 与不同的数据存储连接。已弃用。
  - [Spark RDD API Examples](https://homepage.cs.latrobe.edu.au/zhe/ZhenHeSparkRDDAPIExamples.html) - 何振的例子。
  - [Livy](https://livy.incubator.apache.org) - REST Spark 服务器。
  - [Delight](https://github.com/datamechanics/delight) - 一个免费的跨平台监控工具（Spark UI / Spark History Server 替代品）。
- [AWS EMR](https://aws.amazon.com/emr/) - 一种 Web 服务，可以轻松快速且经济高效地处理大量数据。
- [Data Mechanics](https://www.datamechanics.co) - 部署在 Kubernetes 上的基于云的平台，使 Apache Spark 对开发人员更加友好且更具成本效益。
- [Tez](https://tez.apache.org/) - 一个应用程序框架，允许使用复杂的有向无环任务图来处理数据。
- [Bistro](https://github.com/asavinov/bistro) - 用于通用数据处理（包括批处理和流分析）的轻量级引擎。它基于一种新颖独特的数据模型，该模型通过“函数”表示数据并通过“列操作”处理数据，而不是像 MapReduce 或 SQL 等传统方法中仅进行设置操作。
- [Substation](https://github.com/brexhq/substation) - 用 Go 编写的云原生数据管道和转换工具包。
- [dna-claude-analysis](https://github.com/shmlkv/dna-claude-analysis) - 带有 Python 脚本的个人基因组分析工具包，可分析 17 个类别（健康风险、血统、药物基因组学、营养、心理学等）的原始 DNA 数据，并生成终端式单页 HTML 可视化。
- 批量机器学习
  - [H2O](https://www.h2o.ai/) - 快速可扩展的机器学习 API，适用于更智能的应用程序。
  - [Mahout](https://mahout.apache.org/) - 用于快速创建可扩展的高性能机器学习应用程序的环境。
  - [Spark MLlib](https://spark.apache.org/docs/latest/ml-guide.html) - Spark 的可扩展机器学习库由常见的学习算法和实用程序组成，包括分类、回归、聚类、协作过滤、降维以及底层优化原语。
  - [Datatrax](https://github.com/rbmuller/datatrax) - Pure-Go 经典机器学习工具包和数据工程实用程序。八种零外部依赖性的算法。
  - [Zingg](https://www.zingg.ai/) - 使用机器学习进行大规模实体解析的开源主数据管理平台。原生于 Databricks、Microsoft Fabric、Snowflake、AWS 和 GCP。黄金记录通过跨所有系统和来源的持久 Zingg ID 进行维护。
- 批次图
  - [GraphLab Create](https://turi.com/products/create/docs/) - 一个机器学习平台，使数据科学家和应用程序开发人员能够轻松地大规模创建智能应用程序。
  - [Giraph](https://giraph.apache.org/) - 专为高可扩展性而构建的迭代图形处理系统。
  - [Spark GraphX](https://spark.apache.org/graphx/) - Apache Spark 用于图和图并行计算的 API。
- 批量SQL
  - [Presto](https://prestodb.github.io/docs/current/index.html) - 一种分布式 SQL 查询引擎，旨在查询分布在一个或多个异构数据源上的大型数据集。
  - [Hive](https://hive.apache.org) - 数据仓库软件有助于查询和管理分布式存储中的大型数据集。
    - [Hivemall](https://github.com/apache/incubator-hivemall) - 适用于 Hive/Hadoop 的可扩展机器学习库。
    - [PyHive](https://github.com/dropbox/PyHive) - Hive 和 Presto 的 Python 接口。
  - [Drill](https://drill.apache.org/) - 适用于 Hadoop、NoSQL 和云存储的无架构 SQL 查询引擎。

## 图表和仪表板

- [Highcharts](https://www.highcharts.com/) - 用纯 JavaScript 编写的图表库，提供了一种向网站或 Web 应用程序添加交互式图表的简单方法。
- [ZingChart](https://www.zingchart.com/) - 适用于任何数据集的快速 JavaScript 图表。
- [C3.js](https://c3js.org) - 基于 D3 的可重用图表库。
- [D3.js](https://d3js.org/) - 用于基于数据操作文档的 JavaScript 库。
  - [D3Plus](https://d3plus.org) - D3 更简单，更容易使用。大多数是预定义的模板，您只需插入数据即可。
- [SmoothieCharts](https://smoothiecharts.org) - 用于流数据的 JavaScript 图表库。
- [PyXley](https://github.com/stitchfix/pyxley) - 使用 Flask 和 React 构建仪表板的 Python 助手。
- [Plotly](https://github.com/plotly/dash) - Flask、JS 和 CSS 样板，用于 Python 中基于 Web 的交互式可视化应用程序。
- [Apache Superset](https://github.com/apache/incubator-superset) - 一个现代的、企业级的商业智能 Web 应用程序。
- [Redash](https://redash.io/) - 让您的公司由数据驱动。连接到任何数据源，轻松可视化和共享您的数据。
- [Metabase](https://github.com/metabase/metabase) - 一种简单的开源方式，可供公司中的每个人提出问题并从数据中学习。
- [stratif.io](https://stratif.io) - 开源、自托管、仓库本机产品分析。直接在 DuckDB、Postgres、Snowflake 或 ClickHouse 上运行渠道、保留和路径。
- [PyQtGraph](https://www.pyqtgraph.org/) - 一个基于 PyQt4 / PySide 和 numpy 构建的纯 python 图形和 GUI 库。它旨在用于数学/科学/工程应用。
- [Seaborn](https://seaborn.pydata.org) - 一个基于matplotlib的Python可视化库。它提供了一个高级接口来绘制有吸引力的统计图形。
- [QueryGPT](https://github.com/MKY508/QueryGPT) - 自然语言数据库查询界面，自动生成图表，支持中英文查询。
- [AI for Database](https://aifordatabase.com/) - 代理AI平台，可连接任何数据库（PostgreSQL、MySQL、MongoDB等）并用简单的英语进行查询；包括由数据变化触发的自刷新智能仪表板和操作工作流程。
- [Dekart](https://github.com/dekart-xyz/dekart) - 用于 BigQuery、Snowflake 和 PostGIS 的开源 SQL 地图平台。

## 工作流程

- [Bonnard](https://bonnard.dev/) - 具有受控指标、React SDK 和多仓库支持的代理本机语义层。将人工智能代理和仪表板连接到单一事实来源。
- [OrionBelt Semantic Layer](https://github.com/ralfbecher/orionbelt-semantic-layer) - 开源语义 sidecar，可将 YAML 定义的维度、度量和指标编译为跨 8 个引擎（BigQuery、ClickHouse、Databricks、Dremio、DuckDB、MySQL、PostgreSQL、Snowflake）的优化 SQL。统一 REST、MCP 和 Postgres 有线协议；一种模型为 AI 代理、分析、DQ 规则和 KPI 提供支持。
- [Bruin](https://github.com/bruin-data/bruin) - 端到端数据管道工具，在单个 CLI 中结合了摄取、转换 (SQL + Python) 和数据质量。连接到 BigQuery、Snowflake、PostgreSQL、Redshift 等。包括带有实时预览的 VS Code 扩展。
- [DataFlow](https://github.com/OpenDCAI/DataFlow) - 用于数据准备、合成数据生成和人工智能/数据管道的开源平台。包括跨数据和人工智能任务自动化工作流程步骤的可重用技能。
- [Luigi](https://github.com/spotify/luigi) - 一个 Python 模块，可帮助您构建复杂的批处理作业管道。
- [CronQ](https://github.com/seatgeek/cronq) - 一个类似 cron 的应用程序系统。 [使用](https://chairnerd.seatgeek.com/building-out-the-seatgeek-data-pipeline/) w/Luigi。已弃用。
- [Cascading](https://www.cascading.org/) - 基于Java的应用程序开发平台。
- [Airflow](https://github.com/apache/airflow) - 一个以编程方式创作、调度和监控数据管道的系统。
- [Azkaban](https://azkaban.github.io/) - 在 LinkedIn 创建的批处理工作流作业调度程序，用于运行 Hadoop 作业。 Azkaban 通过作业依赖关系解决排序问题，并提供易于使用的 Web 用户界面来维护和跟踪您的工作流程。
- [Oozie](https://oozie.apache.org/) - 用于管理 Apache Hadoop 作业的工作流调度程序系统。
- [Pinball](https://github.com/pinterest/pinball) - 基于 DAG 的工作流管理器。作业流是在 Python 中以编程方式定义的。支持作业之间的输出传递。
- [Dagster](https://github.com/dagster-io/dagster) - 用于构建数据应用程序的开源 Python 库。
- [Hamilton](https://github.com/dagworks-inc/hamilton) - 一个轻量级库，用于将数据转换定义为有向无环图 (DAG)。如果您喜欢用于 SQL 转换的 dbt，那么您也会喜欢用于 Python 处理的 Hamilton。
- [Kedro](https://kedro.readthedocs.io/en/latest/) - 该框架通过提供统一的项目模板、数据抽象、配置和管道组装，可以轻松构建强大且可扩展的数据管道。
- [Dataform](https://dataform.co/) - 用于管理数据集及其依赖项的开源框架和基于 Web 的 IDE。 SQLX 扩展了现有的 SQL 仓库方言，添加了支持依赖项管理、测试、文档等的功能。
- [Dotflow](https://github.com/dotflow-io/dotflow) - 一个轻量级 Python 库，用于构建具有重试、并行执行、cron 调度和异步支持的执行管道。
- [Census](https://getcensus.com/) - 反向 ETL 工具，可让您将云数据仓库中的数据同步到 Salesforce、Marketo、HubSpot、Zendesk 等 SaaS 应用程序。无需任何工程支持，只需 SQL。
- [dbt](https://getdbt.com/) - 一种命令行工具，使数据分析师和工程师能够更有效地转换仓库中的数据。
- [Kestra](https://github.com/kestra-io/kestra) - 可扩展、事件驱动、与语言无关的编排和调度平台，可在代码中以声明方式管理数百万个工作流程。
- [RudderStack](https://github.com/rudderlabs/rudder-server) - 仓库优先的客户数据平台，使您能够从每个应用程序、网站和 SaaS 平台收集数据，然后在仓库和业务工具中激活它。
- [PACE](https://github.com/getstrm/pace) - 一个开源框架，允许您强制执行关于如何访问、使用和转换数据的协议，无论数据平台如何（Snowflake、BigQuery、DataBricks 等）
- [Prefect](https://prefect.io/) - 一个编排和可观察性平台。有了它，开发人员可以快速构建和扩展弹性代码，并轻松地对中断进行分类。
- [Multiwoven](https://github.com/Multiwoven/multiwoven) - 开源逆向ETL，面向现代数据团队的数据激活平台。
- [SuprSend](https://www.suprsend.com/products/workflows) - 使用 API 为您的通知服务创建自动化工作流程和逻辑。添加模板、批处理、首选项、应用内收件箱以及工作流程，以直接从数据仓库触发通知。
- [Mage](https://www.mage.ai) - 用于转换和集成数据的开源数据管道工具。
- [SQLMesh](https://sqlmesh.readthedocs.io) - 一个开源数据转换框架，用于管理、测试和部署基于 SQL 和 Python 的数据管道，具有版本控制、环境隔离和自动依赖性解析功能。

## 数据湖管理

- [lakeFS](https://github.com/treeverse/lakeFS) - 一个开源平台，可为基于对象存储的数据湖提供弹性和可管理性。
- [Project Nessie](https://github.com/projectnessie/nessie) - 具有类似 Git 语义的数据湖事务目录。适用于 Apache Iceberg 表。
- [Ilum](https://ilum.cloud/) - 模块化 Data Lakehouse 平台，可简化跨 Kubernetes 和 Hadoop 环境的 Apache Spark 集群的管理和监控。
- [Gravitino](https://github.com/apache/gravitino) - 用于数据湖、数据仓库和外部目录的开源、统一元数据管理。
- [FlightPath Data](https://www.flightpathdata.com) - FlightPath 是通往数据湖青铜层的网关，作为受信任的发布者保护其免受无效外部数据文件源的影响。
- [rawquery](https://rawquery.dev) - Apache Iceberg 上的托管 Lakehouse 平台，具有 DuckDB 查询计算、S3 存储、Postgres 有线协议和 SQL 转换。

## ELK Elastic Logstash Kibana

- [docker-logstash](https://github.com/pblittle/docker-logstash) - 高度可配置的 Logstash (1.4.4) - 运行 Elasticsearch (1.7.0) 的 Docker 映像 - 和 Kibana (3.1.2)。
- [elasticsearch-jdbc](https://github.com/jprante/elasticsearch-jdbc) - Elasticsearch 的 JDBC 导入器。
- [ZomboDB](https://github.com/zombodb/zombodb) - PostgreSQL 扩展，允许创建由 Elasticsearch 支持的索引。

## 码头工人

- [Gockerize](https://github.com/redbooth/gockerize) - 将 golang 服务打包到最小的 Docker 容器中。
- [Flocker](https://github.com/ClusterHQ/flocker) - 轻松管理 Docker 容器及其数据。
- [Rancher](https://rancher.com/rancher-os/) - RancherOS 是一个 20mb 的 Linux 发行版，将整个操作系统作为 Docker 容器运行。
- [Kontena](https://www.kontena.io/) - 大众应用程序容器。
- [Weave](https://github.com/weaveworks/weave) - 将 Docker 容器编织到应用程序中。
- [Zodiac](https://github.com/CenturyLinkLabs/zodiac) - 一个轻量级工具，用于轻松部署和回滚 Docker 化应用程序。
- [cAdvisor](https://github.com/google/cadvisor) - 分析运行容器的资源使用情况和性能特征。
- [Micro S3 persistence](https://github.com/figadore/micro-s3-persistence) - 用于将卷数据保存/恢复到 S3 的 Docker 微服务。
- [Rocker-compose](https://github.com/grammarly/rocker-compose) - 具有幂等性功能的 Docker 组合工具，用于部署由多个容器组成的应用程序。已弃用。
- [Nomad](https://github.com/hashicorp/nomad) - 集群管理器，专为长期服务和短期批处理工作负载而设计。
- [ImageLayers](https://imagelayers.io/) - 可视化 Docker 镜像以及组成它们的层。

## 数据集

### 实时

- [DexPaprika](https://api.dexpaprika.com) - 通过 SSE 在 34 个区块链上传输的免费实时 DEX 数据。超过 3000 万个矿池、超过 2700 万个代币、约 1 秒价格更新。没有 API 密钥，没有速率限制。 [文档](https://docs.dexpaprika.com)
- [Helium MCP](https://github.com/connerlambden/helium-mcp) - 远程 MCP 服务器，用于实时金融数据、320 万多篇新闻文章、ML 期权定价和新闻偏差分析。免费，无 API 密钥。 [MCP](https://heliumtrades.com/mcp)
- [Twitter Realtime](https://developer.twitter.com/en/docs/tweets/filter-realtime/overview) - Streaming API 使开发人员能够低延迟地访问 Twitter 的全球推文数据流。
- [Sorsa API](https://api.sorsa.io) - 实时 X (Twitter) 数据 API 提供推文、个人资料、搜索、社区和参与度指标。比官方 X API 便宜 50 倍，速率限制为 20 个请求/秒，JSON 输出。
- [Eventsim](https://github.com/Interana/eventsim) - 事件数据模拟器。从一组用户生成伪随机事件流，旨在模拟 Web 流量。
- [Eventum](https://eventum.run) - 用于生成具有复杂相关性的合成事件流的数据生成平台。
- [Reddit](https://www.reddit.com/r/datasets/comments/3mk1vg/realtime_data_is_available_including_comments/) - 提供实时数据，包括评论、提交内容和发布到 Reddit 的链接。

### 数据转储

- [GitHub Archive](https://www.gharchive.org/) - GitHub 自 2011 年以来的公开时间表，每小时更新一次。
- [Common Crawl](https://commoncrawl.org/) - 网络爬行数据的开源存储库。
- [Wikipedia](https://dumps.wikimedia.org/enwiki/latest/) - 维基百科所有 wiki 的完整副本，采用嵌入 XML 的维基文本源和元数据的形式。还提供许多 SQL 形式的原始数据库表。
- [The Quiet-Broke Index](https://jeevesagency.github.io/quiet-broke-index/) - 根据人口普查 ACS、BLS 消费者支出调查和 HUD 公平市场租金汇总的 30 大城市美国家庭成本负担（住房、税收、儿童保育、医疗保健、交通）综合数据。开放方法，免费，没有电子邮件门。
- [FirstData](https://github.com/MLT-OSS/FirstData) - 全球最全面的权威数据源知识库。来自政府、国际组织和研究机构的 160 多个精选资源，具有 MCP 集成。
- [Mindweave Synthetic Business Data](https://github.com/MindweaveTech/sme-sim-sample) - 42 表综合中小企业数据集，具有复式记账、税务合规性（澳大利亚/美国/英国）和时间现实性。 CSV、SQL、Parquet、SQLite。非常适合 ETL 管道测试。

## 监控

### 普罗米修斯

- [Prometheus.io](https://github.com/prometheus/prometheus) - 开源的服务监控系统和时间序列数据库。
- [HAProxy Exporter](https://github.com/prometheus/haproxy_exporter) - 简单的服务器，用于抓取 HAProxy 统计信息并通过 HTTP 导出它们以供 Prometheus 使用。
- [Signals CLI](https://github.com/sortlist/signals-cli) - 意图信号监控 CLI。跟踪 LinkedIn 参与者、关键词海报、换工作者、资助活动。数据管道的 JSON 输出。

## 分析

### 数据分析器
- [Data Profiler](https://github.com/capitalone/dataprofiler) - DataProfiler 是一个 Python 库，旨在简化数据分析、监控和敏感数据检测。
- [YData Profiling](https://docs.profiling.ydata.ai/latest/) - 用于对数据集进行高级分析的通用开源数据分析器。
- [Desbordante](https://github.com/desbordante/desbordante-core) - 开源数据分析器专门致力于发现和验证数据中的复杂模式。


## 测试

- [Aegis DQ](https://github.com/aegis-dq/aegis-dq) - 开源代理数据质量框架，具有 LLM 支持的诊断、根本原因分析、SQL 自动修复建议和 31 种规则类型 - DuckDB、Postgres、BigQuery、Databricks、Athena、Snowflake。
- [Grai](https://github.com/grai-io/grai-core/) - 一种数据目录工具，可集成到 CI 系统中，公开数据更改的下游影响测试。这些测试可防止可能破坏数据管道或 BI 仪表板进入生产环境的数据更改。
- [DQOps](https://github.com/dqops/dqo) - 一个开源数据质量平台，适用于从分析新数据源到应用数据质量监控的完全自动化的整个数据平台生命周期。
- [DataKitchen](https://datakitchen.io/) - 用于端到端数据旅程可观察性、数据分析、异常检测和自动创建的数据质量验证测试的开源数据可观察性。
- [GreatExpectation](https://greatexpectations.io/) - 用于管理数据质量的开源数据验证框架。用户可以定义并记录有关数据外观和行为的“期望”规则。
- [Provero](https://github.com/provero-org/provero) - 供应商中立的声明性数据质量引擎。在 YAML 中定义检查，在任何地方运行。包括 16 种内置检查类型、SQL 批量优化器、异常检测和数据契约。
- [Scherlok](https://github.com/rbmuller/scherlok) - 零配置数据质量 CLI。在第一次运行时分析每个表，然后在后续运行中自动检测异常（数量下降、模式漂移、新鲜度缺失、分布变化）。没有 YAML，无需编写规则。适用于 Postgres、BigQuery、Snowflake 和 dbt。
- [RunSQL](https://runsql.com/) - 适用于 MySQL、PostgreSQL 和 SQL Server 的免费在线 SQL 游乐场。创建数据库结构、运行查询并立即共享结果。
- [Spark Playground](https://www.sparkplayground.com/) - 在 Spark Playground 的在线编译器上编写、运行和测试 PySpark 代码。访问真实世界的示例数据集并解决面试问题，以增强您担任数据工程角色的 PySpark 技能。
- [daffy](https://github.com/vertti/daffy/) - 函数边界处的装饰者优先的 DataFrame 契约/验证（列/数据类型/约束）。支持 Pandas/Polars/PyArrow/Modin。
- [Snowflake Emulator](https://github.com/nnnkkk7/snowflake-emulator) - 用于本地开发和测试的 Snowflake 兼容模拟器。
- [DataScreenIQ](https://datascreeniq.com) - 适用于管道和 API 的实时数据质量防火墙。通过 PASS / WARN / BLOCK 决策以毫秒为单位筛选行中的架构漂移、空峰值、类型不匹配和数据异常。
- [DataDriven](https://www.datadriven.io/) - 面试练习包括 SQL 查询执行、Python 和数据建模练习。
- [Fixzi](https://fixzi.ai) - JSON/XML 验证和 API 合约监控工具，用于调试和测试结构化数据。

## 社区

### 论坛

- [/r/dataengineering](https://www.reddit.com/r/dataengineering/) - 有关数据工程的新闻、技巧和背景。
- [/r/etl](https://www.reddit.com/r/ETL/) - Reddit 子版块专注于 ETL。
- [AI Dev Jobs](https://aidevboard.com) - 求职板专注于人工智能、机器学习和数据工程职位，包含 7,400 多个列表、薪资数据和免费的 REST API。

### 会议

- [Data Council](https://www.datacouncil.ai/about) - 首届弥合数据科学家、数据工程师和数据分析师之间差距的技术会议。

### 播客

- [Chain of Thought](https://www.chainofthought.show/) - 就构建生产系统采访人工智能和数据基础设施领导者。
- [Data Engineering Podcast](https://www.dataengineeringpodcast.com/) - 关于现代数据基础设施的节目。
- [Latent Space](https://www.latent.space/podcast) - 从模型训练到部署，对人工智能工程进行技术深入研究。
- [Practical AI](https://practicalai.fm/) - 让人工智能变得实用、高效且可供每个人使用。
- [Software Engineering Daily](https://softwareengineeringdaily.com/) - 关于技术软件主题（包括数据基础设施）的每日采访。
- [The Analytics Engineering Podcast](https://roundup.getdbt.com/s/the-analytics-engineering-podcast) - 分析工程师如何大规模构建和维护数据管道。
- [The Data Stack Show](https://datastackshow.com/) - 在这个节目中，他们与数据工程师、分析师和数据科学家谈论他们在构建和维护数据基础设施、交付数据和数据产品以及利用数据推动整个业务取得更好成果方面的经验。

### 书籍

- [Snowflake Data Engineering](https://www.manning.com/books/snowflake-data-engineering) - Snowflake云数据平台上数据工程的实用介绍。
- [Best Data Science Books](https://www.appliedaicourse.com/blog/data-science-books/) - 该博客提供了顶级数据科学书籍的精选列表，按主题和学习阶段进行分类，以帮助读者构建基础知识并及时了解行业趋势。
- [Architecting an Apache Iceberg Lakehouse](https://www.manning.com/books/architecting-an-apache-iceberg-lakehouse) - 从头开始设计阿帕奇冰山湖屋的指南。
- [Learn AI Data Engineering in a Month of Lunches](https://www.manning.com/books/learn-ai-data-engineering-in-a-month-of-lunches) - 将大型语言模型集成到数据工作流程中的快速、友好的指南。
