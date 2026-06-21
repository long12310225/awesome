[<img src="https://cdn.rawgit.com/awesome-spark/awesome-spark/f78a16db/spark-logo-trademark.svg"align="right">](https://spark.apache.org/)

# 令人敬畏的火花 [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

精彩的 [Apache Spark](https://spark.apache.org/) 软件包和资源的精选列表。

_Apache Spark 是一个开源集群计算框架。 Spark 代码库最初由[加州大学](https://www.universityofcalifornia.edu/)、[伯克利分校的 AMPLab](https://amplab.cs.berkeley.edu/) 开发，后来捐赠给[Apache 软件基金会](https://www.apache.org/)，并一直由该基金会维护。 Spark 提供了一个接口，用于通过隐式数据并行性和容错性对整个集群进行编程（[Wikipedia 2017](#wikipedia-2017)）。

Apache Spark 用户可以选择不同的 Python、R、Scala 和 Java 编程语言来与 Apache Spark API 进行交互。

## 套餐

### 语言绑定

* [Kotlin for Apache Spark](https://github.com/Kotlin/kotlin-spark-api) <img src="https://img.shields.io/github/last-commit/Kotlin/kotlin-spark-api.svg"> - Kotlin API 绑定和扩展。
* [.NET for Apache Spark](https://github.com/dotnet/spark) <img src="https://img.shields.io/github/last-commit/dotnet/spark.svg"> - .NET 绑定。
* [sparklyr](https://github.com/rstudio/sparklyr) <img src="https://img.shields.io/github/last-commit/rstudio/sparklyr.svg"> - 使用 [`dplyr`](https://github.com/hadley/dplyr) 的替代 R 后端。
* [sparkle](https://github.com/tweag/sparkle) <img src="https://img.shields.io/github/last-commit/tweag/sparkle.svg"> - Apache Spark 上的 Haskell。
* [spark-connect-rs](https://github.com/sjrusso8/spark-connect-rs) <img src="https://img.shields.io/github/last-commit/sjrusso8/spark-connect-rs.svg"> - Rust 绑定。
* [spark-connect-go](https://github.com/apache/spark-connect-go) <img src="https://img.shields.io/github/last-commit/apache/spark-connect-go.svg"> - Golang 绑定。
* [spark-connect-csharp](https://github.com/mdrakiburrahman/spark-connect-csharp) <img src="https://img.shields.io/github/last-commit/mdrakiburrahman/spark-connect-csharp.svg"> - C# 绑定。

### 笔记本电脑和 IDE
* [almond](https://almond.sh/) <img src="https://img.shields.io/github/last-commit/almond-sh/almond.svg"> - [Jupyter](https://jupyter.org/) 的 scala 内核。
* [Apache Zeppelin](https://zeppelin.incubator.apache.org/) <img src="https://img.shields.io/github/last-commit/apache/zeppelin.svg"> - 基于 Web 的笔记本，可通过可插入后端、集成绘图和广泛的开箱即用 Spark 支持来实现交互式数据分析。
* [Polynote](https://polynote.org/) <img src="https://img.shields.io/github/last-commit/polynote/polynote.svg"> - Polynote：一款受 IDE 启发的多语言笔记本。它支持在一个笔记本中混合多种语言，并在它们之间无缝共享数据。它通过其不可变的数据模型鼓励可复制的笔记本。源自 [Netflix](https://medium.com/netflix-techblog/open-source-polynote-an-ide-inspired-polyglot-notebook-7f929d3f447)。
* [sparkmagic](https://github.com/jupyter-incubator/sparkmagic) <img src="https://img.shields.io/github/last-commit/jupyter-incubator/sparkmagic.svg"> - [Jupyter](https://jupyter.org/) 用于处理远程 Spark 集群的魔法和内核，用于通过以下方式与远程 Spark 集群交互工作[Livy](https://github.com/cloudera/livy)，在 Jupyter 笔记本中。

### 通用库

* [itachi](https://github.com/yaooqinn/itachi) <img src="https://img.shields.io/github/last-commit/yaooqinn/itachi.svg"> - 一个库，将现代数据库管理系统中的有用功能引入 Apache Spark。
* [spark-daria](https://github.com/mrpowers-io/spark-daria) <img src="https://img.shields.io/github/last-commit/mrpowers-io/spark-daria.svg"> - 一个 Scala 库，具有基本的 Spark 功能和扩展，可提高您的工作效率。
* [quinn](https://github.com/mrpowers-io/quinn) <img src="https://img.shields.io/github/last-commit/mrpowers-io/quinn.svg"> - Spark-Daria 的本机 PySpark 实现。
* [Apache DataFu](https://github.com/apache/datafu/tree/master/datafu-spark) <img src="https://img.shields.io/github/last-commit/apache/datafu.svg"> - 通用函数和 UDF 的库。
* [Joblib Apache Spark 后端](https://github.com/joblib/joblib-spark) <img src="https://img.shields.io/github/last-commit/joblib/joblib-spark.svg"> - [`joblib`](https://github.com/joblib/joblib) 用于在 Spark 集群上运行任务的后端。

### SQL数据源

SparkSQL 有多个内置数据源用于文件。其中包括“csv”、“json”、“parquet”、“orc”和“avro”。它还支持 JDBC 数据库以及 Apache Hive。可以通过包含下面列出的包或编写您自己的包来添加其他数据源。

* [Spark XML](https://github.com/databricks/spark-xml) <img src="https://img.shields.io/github/last-commit/databricks/spark-xml.svg"> - XML 解析器和编写器。
* [Spark Cassandra 连接器](https://github.com/datastax/spark-cassandra-connector) <img src="https://img.shields.io/github/last-commit/datastax/spark-cassandra-connector.svg"> - Cassandra 支持，包括数据源和 API 以及对任意查询的支持。
* [Mongo-Spark](https://github.com/mongodb/mongo-spark) <img src="https://img.shields.io/github/last-commit/mongodb/mongo-spark.svg"> - 官方 MongoDB 连接器。

### 存储

* [Delta Lake](https://github.com/delta-io/delta) <img src="https://img.shields.io/github/last-commit/delta-io/delta.svg"> - 具有 ACID 事务的存储层。
* [Apache Hudi](https://github.com/apache/hudi) <img src="https://img.shields.io/github/last-commit/apache/hudi.svg"> - 大数据的更新插入、删除和增量处理..
* [Apache Iceberg](https://github.com/apache/iceberg) <img src="https://img.shields.io/github/last-commit/apache/iceberg.svg"> - 大数据的更新插入、删除和增量处理..
* [lakeFS](https://docs.lakefs.io/integrations/spark.html) <img src="https://img.shields.io/github/last-commit/treeverse/lakefs.svg"> - 与 LakeFS 原子版本化存储层集成。

### 生物信息学

* [ADAM](https://github.com/bigdatagenomics/adam) <img src="https://img.shields.io/github/last-commit/bigdatagenomics/adam.svg"> - 旨在分析基因组数据的工具集。
* [Hail](https://github.com/hail-is/hail) <img src="https://img.shields.io/github/last-commit/hail-is/hail.svg"> - 遗传分析框架。

### 地理信息系统

* [Apache Sedona](https://github.com/apache/incubator-sedona) <img src="https://img.shields.io/github/last-commit/apache/incubator-sedona.svg"> - 用于处理大规模空间数据的集群计算系统。

### 图形处理

* [GraphFrames](https://github.com/graphframes/graphframes) <img src="https://img.shields.io/github/last-commit/graphframes/graphframes.svg"> - 基于数据框架的图形 API。
* [neo4j-spark-connector](https://github.com/neo4j-contrib/neo4j-spark-connector) <img src="https://img.shields.io/github/last-commit/neo4j-contrib/neo4j-spark-connector.svg"> - 基于 Bolt 协议的 Neo4j 连接器，支持 RDD、DataFrame 和 GraphX / GraphFrames。

### 机器学习扩展

* [Apache SystemML](https://systemml.apache.org/) <img src="https://img.shields.io/github/last-commit/apache/systemml.svg"> - Spark 之上的声明式机器学习框架。
* [Mahout Spark Bindings](https://mahout.apache.org/users/sparkbindings/home.html) \[状态未知\] - 线性代数 DSL 和具有类似 R 语法的优化器。
* [KeystoneML](http://keystone-ml.org/) - 使用 RDD 构建安全的机器学习管道。
* [JPMML-Spark](https://github.com/jpmml/jpmml-spark) <img src="https://img.shields.io/github/last-commit/jpmml/jpmml-spark.svg"> - Spark ML 的 PMML 转换器库。
* [ModelDB](https://mitdbg.github.io/modeldb) <img src="https://img.shields.io/github/last-commit/mitdbg/modeldb.svg"> - 管理 `spark.ml` 和 [`scikit-learn`](https://github.com/scikit-learn/scikit-learn) 机器学习模型的系统 <img src =“https://img.shields.io/github/last-commit/scikit-learn/scikit-learn.svg”>。
* [Sparkling Water](https://github.com/h2oai/sparkling-water) <img src="https://img.shields.io/github/last-commit/h2oai/sparkling-water.svg"> - [H2O](http://www.h2o.ai/) 互操作层。
* [BigDL](https://github.com/intel-analytics/BigDL) <img src="https://img.shields.io/github/last-commit/intel-analytics/BigDL.svg"> - 分布式深度学习库。
* [MLeap](https://github.com/combust/mleap) <img src="https://img.shields.io/github/last-commit/combust/mleap.svg"> - 支持部署 `o.a.s.ml` 模型而不依赖于 `SparkSession` 的执行引擎和序列化格式。
* [Microsoft ML for Apache Spark](https://github.com/Azure/mmlspark) <img src="https://img.shields.io/github/last-commit/Azure/mmlspark.svg"> - 分布式机器学习库，支持 LightGBM、Vowpal Wabbit、OpenCV、深度学习、认知服务和模型部署。
* [MLflow](https://mlflow.org/docs/latest/python_api/mlflow.spark.html#module-mlflow.spark) <img src="https://img.shields.io/github/last-commit/mlflow/mlflow.svg"> - 机器学习编排平台。

### 中间件

* [Livy](https://github.com/apache/incubator-livy) <img src="https://img.shields.io/github/last-commit/apache/incubator-livy.svg"> - 具有广泛语言支持（Python、R、Scala）的 REST 服务器，能够维护交互式会话和对象共享。
* [spark-jobserver](https://github.com/spark-jobserver/spark-jobserver) <img src="https://img.shields.io/github/last-commit/spark-jobserver/spark-jobserver.svg"> - 简单的 Spark 即服务，支持使用所谓的命名对象共享对象。仅限 JVM。
* [Apache Toree](https://github.com/apache/incubator-toree) <img src="https://img.shields.io/github/last-commit/apache/incubator-toree.svg"> - 基于 IPython 协议的交互式应用程序中间件。
* [Apache Kyuubi](https://github.com/apache/kyuubi) <img src="https://img.shields.io/github/last-commit/apache/kyuubi.svg"> - 用于大规模数据处理和分析的分布式多租户 JDBC 服务器，构建于 Apache Spark 之上。

### 监控

* [Data Mechanics Delight](https://github.com/datamechanics/delight) <img src="https://img.shields.io/github/last-commit/datamechanics/delight.svg"> - 跨平台监控工具（Spark UI / Spark History Server 替换）。

### 公用事业

* [sparkly](https://github.com/Tubular/sparkly) <img src="https://img.shields.io/github/last-commit/Tubular/sparkly.svg"> - PySpark 的助手和语法糖。
* [Flintrock](https://github.com/nchammas/flintrock) <img src="https://img.shields.io/github/last-commit/nchammas/flintrock.svg"> - 用于在 EC2 上启动 Spark 集群的命令行工具。
* [Optimus](https://github.com/ironmussa/Optimus/) <img src="https://img.shields.io/github/last-commit/ironmussa/Optimus.svg"> - 数据清理和探索实用程序，旨在简化数据清理。

### 自然语言处理

* [spark-nlp](https://github.com/JohnSnowLabs/spark-nlp) <img src="https://img.shields.io/github/last-commit/JohnSnowLabs/spark-nlp.svg"> - 基于 Apache Spark ML 构建的自然语言处理库。

### 流媒体

* [Apache Bahir](https://bahir.apache.org/) <img src="https://img.shields.io/github/last-commit/apache/bahir.svg"> - Spark 2.0 中排除的流连接器集合（Akka、MQTT、Twitter、ZeroMQ）。

### 接口

* [Apache Beam](https://beam.apache.org/) <img src="https://img.shields.io/github/last-commit/apache/beam.svg"> - 支持批处理和流应用程序的统一数据处理引擎。 Apache Spark 是受支持的执行环境之一。
* [Koalas](https://github.com/databricks/koalas) <img src="https://img.shields.io/github/last-commit/databricks/koalas.svg"> - Apache Spark 之上的 Pandas DataFrame API。

### 数据质量

* [deequ](https://github.com/awslabs/deequ) <img src="https://img.shields.io/github/last-commit/awslabs/deequ.svg"> - Deequ 是一个构建在 Apache Spark 之上的库，用于定义“数据单元测试”，用于测量大型数据集中的数据质量。
* [python-deequ](https://github.com/awslabs/python-deequ) <img src="https://img.shields.io/github/last-commit/awslabs/python-deequ.svg"> - Deequ 的 Python API。

### 测试

* [spark-testing-base](https://github.com/holdenk/spark-testing-base) <img src="https://img.shields.io/github/last-commit/holdenk/spark-testing-base.svg"> - 基础测试类的集合。
* [spark-fast-tests](https://github.com/mrpowers-io/spark-fast-tests) <img src="https://img.shields.io/github/last-commit/mrpowers-io/spark-fast-tests.svg"> - 一个轻量级快速测试框架。
* [chispa](https://github.com/MrPowers/chispa) <img src="https://img.shields.io/github/last-commit/MrPowers/chispa.svg"> - PySpark 测试助手，带有漂亮的错误消息。

### 网络档案

* [Archives Unleashed Toolkit](https://github.com/archivesunleashed/aut) <img src="https://img.shields.io/github/last-commit/archivesunleashed/aut.svg"> - 用于分析网络档案的开源工具包。

### 工作流程管理

* [Cromwell](https://github.com/broadinstitute/cromwell#spark-backend) <img src="https://img.shields.io/github/last-commit/broadinstitute/cromwell.svg"> - 具有 [Spark 后端](https://github.com/broadinstitute/cromwell#spark-backend) 的工作流程管理系统。

## 资源

### 书籍

* [Learning Spark, 2nd Edition](https://www.oreilly.com/library/view/learning-spark-2nd/9781492050032/) - Spark API 简介，涵盖 Spark 3.0。有关基本概念的良好知识来源。
* [Advanced Analytics with Spark](http://shop.oreilly.com/product/0636920035091.do) - Spark 处理模式的有用集合。随附的 GitHub 存储库：[sryza/aas](https://github.com/sryza/aas)。
* [Mastering Apache Spark](https://jaceklaskowski.gitbooks.io/mastering-apache-spark/) - [Jacek Laskowski](https://github.com/jaceklaskowski) 有趣的笔记汇编。重点关注 Spark 内部结构的不同方面。
* [Spark in Action](https://www.manning.com/books/spark-in-action) - 曼宁“行动”家族的新书，超过 400 页。开头温和、循序渐进，涵盖大量主题。有关如何[设置 Eclipse 以进行 Spark 应用程序开发](http://freecontent.manning.com/how-to-start-developing-spark-applications-in-eclipse/) 以及如何使用提供的 Maven Archetype 引导新应用程序的免费摘录。您可以在[此处](https://github.com/spark-in-action/first-edition)找到随附的 GitHub 存储库。

### 论文

* [Large-Scale Intelligent Microservices](https://arxiv.org/pdf/2009.08044.pdf) - Microsoft 论文提出了一个基于 Apache Spark 的微服务编排框架，该框架扩展了数据库操作以包含 Web 服务原语。
* [Resilient Distributed Datasets: A Fault-Tolerant Abstraction for In-Memory Cluster Computing](https://people.csail.mit.edu/matei/papers/2012/nsdi_spark.pdf) - 介绍核心分布式内存抽象的论文。
* [Spark SQL: Relational Data Processing in Spark](https://amplab.cs.berkeley.edu/wp-content/uploads/2015/03/SparkSQLSigmod2015.pdf) - 介绍关系基础、代码生成和 Catalyst 优化器的论文。
* [Structured Streaming: A Declarative API for Real-Time Applications in Apache Spark](https://cs.stanford.edu/~matei/papers/2018/sigmod_structured_streaming.pdf) - Structured Streaming 是一种新的高级流 API，它是一种基于自动增量静态关系查询的声明式 API。

### 慕课

* [Data Science and Engineering with Apache Spark (edX XSeries)](https://www.edx.org/xseries/data-science-engineering-apache-spark) - 系列五门课程（[Apache Spark 简介](https://www.edx.org/course/introduction-apache-spark-uc-berkeleyx-cs105x)、[使用 Apache Spark 进行分布式机器学习](https://www.edx.org/course/distributed-machine-learning-apache-uc-berkeleyx-cs120x)、[使用 Apache 进行大数据分析Spark](https://www.edx.org/course/big-data-analysis-apache-spark-uc-berkeleyx-cs110x)、[用于数据科学和数据工程的高级 Apache Spark](https://www.edx.org/course/advanced-apache-spark-data-science-data-uc-berkeleyx-cs115x)、[使用 Apache 进行高级分布式机器学习Spark](https://www.edx.org/course/advanced-distributed-machine-learning-uc-berkeleyx-cs125x))涵盖了软件工程和数据科学的不同方面。面向Python。
* [Big Data Analysis with Scala and Spark (Coursera)](https://www.coursera.org/learn/big-data-analysys) - 面向Scala的入门课程。 [Scala 函数式编程专业化](https://www.coursera.org/specializations/scala) 的一部分。

### 工作坊

* [AMP Camp](http://ampcamp.berkeley.edu) - [加州大学伯克利分校 AMPLab](https://amplab.cs.berkeley.edu/) 组织的定期培训活动。有用练习和录制的研讨会的来源，涵盖 [伯克利数据分析堆栈](https://amplab.cs.berkeley.edu/software/) 中的不同工具。

### 使用 Spark 的项目

* [Oryx 2](https://github.com/OryxProject/oryx) - [Lambda 架构](http://lambda-architecture.net/) 平台基于 Apache Spark 和 [Apache Kafka](http://kafka.apache.org/) 构建，专门用于实时大规模机器学习。
* [Photon ML](https://github.com/linkedin/photon-ml) - 支持经典广义混合模型和广义加性混合效应模型的机器学习库。
* [PredictionIO](https://prediction.io/) - 机器学习服务器供开发人员和数据科学家在短时间内构建和部署预测应用程序。
* [Crossdata](https://github.com/Stratio/Crossdata) - 具有扩展 DataSource API 和多用户环境的数据集成平台。


### Docker 镜像

- [apache/spark](https://hub.docker.com/r/apache/spark) - Apache Spark 官方 Docker 镜像。
- [jupyter/docker-stacks/pyspark-notebook](https://github.com/jupyter/docker-stacks/tree/master/pyspark-notebook) - PySpark 与 Jupyter Notebook 和 Mesos 客户端。
- [sequenceiq/docker-spark](https://github.com/sequenceiq/docker-spark) - 纱线图像来自 [SequenceIQ](http://www.sequenceiq.com/)。
- [datamechanics/spark](https://hub.docker.com/r/datamechanics/spark) - 来自 [Data Mechanics](https://www.datamechanics.co/) 的 Apache Spark 的易于设置的 Docker 映像。

### 杂项

- [Spark with Scala Gitter channel](https://gitter.im/spark-scala/Lobby) - “_讨论和询问有关使用 Scala 进行 Spark 编程的问题的地方_”由 [@deanwampler](https://github.com/deanwampler) 发起。
- [Apache Spark 用户列表](http://apache-spark-user-list.1001560.n3.nabble.com/) 和 [Apache Spark 开发人员列表](http://apache-spark-developers-list.1001551.n3.nabble.com/) - 分别专门用于使用问题和开发主题的邮件列表。

## 参考文献

<p id="wikipedia-2017">Wikipedia. 2017. “Apache Spark — Wikipedia, the Free Encyclopedia.” <a href="https://en.wikipedia.org/w/index.php?title=Apache_Spark&amp;oldid=781182753" class="uri">https://en.wikipedia.org/w/index.php?title=Apache_Spark&amp;oldid=781182753</a>.</p>

## License

<p xmlns:dct="http://purl.org/dc/terms/">
<a rel="license" href="http://creativecommons.org/publicdomain/mark/1.0/">
<img src="https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/publicdomain.svg"
     style="border-style: none;" alt="Public Domain Mark" />
</a>
<br />
This work (<span property="dct:title">Awesome Spark</span>, by <a href="https://github.com/awesome-spark/awesome-spark" rel="dct:creator">https://github.com/awesome-spark/awesome-spark</a>), identified by <a href="https://github.com/zero323" rel="dct:publisher"><span property="dct:title">Maciej Szymkiewicz</span></a>, is free of known copyright restrictions.
</p>

Apache Spark、Spark、Apache 和 Spark 徽标是以下公司的<a href="https://www.apache.org/foundation/marks/">商标</a>
  <a href="http://www.apache.org">The Apache Software Foundation</a>. This compilation is not endorsed by The Apache Software Foundation.

Inspired by [sindresorhus/awesome](https://github.com/sindresorhus/awesome).
