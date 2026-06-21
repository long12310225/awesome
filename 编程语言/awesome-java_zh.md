# 很棒的Java [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

精选的精彩 Java 框架、库和软件列表。

[请在此处找到不同类型的布局](https://github.com/akullpp/awesome-java/tree/test)。

我们正在评估将其设为默认值，您可以在 [#1171](https://github.com/akullpp/awesome-java/issues/1171) 中提供反馈。

## 内容

- [很棒的Java](#awesome-java-)
  - [Contents](#contents)
  - [Projects](#projects)
    - [Architecture](#architecture)
    - [人工智能](#artificial-intelligence)
    - [Bean 映射](#bean-mapping)
    - [Build](#build)
    - [字节码操作](#bytecode-manipulation)
    - [Caching](#caching)
    - [CLI](#cli)
      - [参数解析](#argument-parsing)
      - [基于文本的用户界面](#text-based-user-interfaces)
    - [Cloud](#cloud)
    - [代码分析](#code-analysis)
    - [代码覆盖率](#code-coverage)
    - [代码生成器](#code-generators)
    - [Compiler-compiler](#compiler-compiler)
    - [计算机视觉](#computer-vision)
    - [Configuration](#configuration)
    - [约束满足问题求解器](#constraint-satisfaction-problem-solver)
    - [CSV](#csv)
    - [数据结构](#data-structures)
    - [Database](#database)
    - [日期和时间](#date-and-time)
    - [Decentralization](#decentralization)
    - [依赖注入](#dependency-injection)
    - [Development](#development)
    - [分布式应用程序](#distributed-applications)
    - [分布式事务](#distributed-transactions)
    - [Distribution](#distribution)
    - [文件处理](#document-processing)
    - [Financial](#financial)
    - [形式验证](#formal-verification)
    - [函数式编程](#functional-programming)
    - [游戏开发](#game-development)
    - [Geospatial](#geospatial)
    - [GUI](#gui)
    - [高性能](#high-performance)
    - [HTTP 客户端](#http-clients)
    - [超媒体类型](#hypermedia-types)
    - [IDE](#ide)
    - [Imagery](#imagery)
    - [Introspection](#introspection)
    - [作业调度](#job-scheduling)
    - [JSON](#json)
    - [JVM 和 JDK](#jvm-and-jdk)
    - [Logging](#logging)
    - [机器学习](#machine-learning)
    - [Messaging](#messaging)
    - [Microservice](#microservice)
    - [Miscellaneous](#miscellaneous)
    - [移动开发](#mobile-development)
    - [Monitoring](#monitoring)
    - [Native](#native)
    - [自然语言处理](#natural-language-processing)
    - [Networking](#networking)
    - [ORM](#orm)
    - [PaaS](#paas)
    - [Pathfinding](#pathfinding)
    - [PDF](#pdf)
    - [性能分析](#performance-analysis)
    - [Platform](#platform)
      - [阿帕奇共享区](#apache-commons)
      - [Other](#other)
    - [Processes](#processes)
    - [反应式库](#reactive-libraries)
    - [REST 框架](#rest-frameworks)
    - [Science](#science)
    - [Search](#search)
    - [Security](#security)
    - [Serialization](#serialization)
    - [Server](#server)
    - [模板引擎](#template-engine)
    - [Testing](#testing)
      - [Asynchronous](#asynchronous)
      - [BDD](#bdd)
      - [Fixtures](#fixtures)
      - [Frameworks](#frameworks)
      - [Matchers](#matchers)
      - [Miscellaneous](#miscellaneous-1)
      - [Mocking](#mocking)
    - [Utility](#utility)
    - [版本管理器](#version-managers)
    - [网络爬行](#web-crawling)
    - [网络框架](#web-frameworks)
    - [工作流编排引擎](#workflow-orchestration-engines)
  - [Resources](#resources)
    - [相关精彩列表](#related-awesome-lists)
    - [Communities](#communities)
    - [Frontends](#frontends)
    - [有影响力的书籍](#influential-books)
    - [播客和截屏视频](#podcasts-and-screencasts)
    - [People](#people)
      - [Socials](#socials)
    - [Websites](#websites)
  - [Contributing](#contributing)

## 项目

### 建筑

_帮助实现和验证设计和架构概念的框架和库。_

- [ArchUnit](https://github.com/TNG/ArchUnit) - 用于指定和断言架构规则的测试库。
- [jMolecules](https://github.com/xmolecules/jmolecules) - 在代码中表达设计和架构概念的注释和接口。

### 人工智能

_帮助您利用法学硕士和人工智能的框架。_

- [JamJet](https://github.com/jamjet-labs/jamjet) - 具有 Java SDK 的代理运行时，用于构建 AI 代理，支持基于图形的工作流编排、多代理协调和 MCP/A2A 协议。
- [LangChain4j](https://github.com/langchain4j/langchain4j) - 通过统一的 API 和综合工具箱简化法学硕士的集成。
- [MCP Java SDK](https://github.com/modelcontextprotocol/java-sdk) - 使应用程序能够通过标准化接口（即模型上下文协议）与人工智能模型和工具交互，支持同步和异步通信模式。
- [simple-openai](https://github.com/sashirestela/simple-openai) - 以最简单的方式使用 OpenAI API（和兼容的 API）的库。
- [Spring AI](https://spring.io/projects/spring-ai) - Spring 的人工智能工程应用框架。

### Bean 映射

_简化 bean 映射的框架._

- [dOOv](https://github.com/doov-io/doov) - 为类型安全域模型验证和映射提供流畅的 API。它使用注释、代码生成和类型安全 DSL 来使 Bean 验证和映射变得快速而简单。
- [JMapper](https://github.com/jmapper-framework/jmapper-core) - 使用字节码操作实现闪电般的快速映射。支持注释和 API 或 XML 配置。
- [MapStruct](https://github.com/mapstruct/mapstruct) - 基于约定优于配置的方法，简化不同 Bean 类型之间映射的代码生成器。
- [ModelMapper](https://github.com/modelmapper/modelmapper) - 智能对象映射库，自动将对象相互映射。
- [Orika](https://github.com/orika-mapper/orika) - JavaBean 映射框架，可将数据（以及其他功能）从一个对象递归复制到另一个对象。
- [reMap](https://github.com/remondis-it/remap) - 如果对象具有不同名称，则基于 Lambda 和方法句柄的映射需要代码而不是注释。
- [Selma](https://github.com/xebia-france/selma) - 基于注释处理器的 bean 映射器。

### 构建

_处理应用程序的构建周期和依赖项的工具。_

- [Apache Maven](https://maven.apache.org) - 声明式构建和依赖关系管理有利于约定优于配置。它可能比 Apache Ant 更好，后者使用相当程序化的方法并且可能难以维护。
- [Bazel](https://bazel.build) - 来自 Google 的工具，可快速可靠地构建代码。
- [Buck2](https://github.com/facebook/buck2) - 鼓励创建由代码和资源组成的小型、可重用模块。
- [Gradle](https://gradle.org) - 通过 Groovy 进行增量构建，而不是声明 XML。与 Maven 的依赖管理配合良好。

- [ReleaseRun](https://releaserun.com) - pom.xml 和 Gradle 项目的依赖关系运行状况检查器，可扫描 CVE 和过时的包。
### 字节码操作

_以编程方式操作字节码的库._

- [ASM](https://asm.ow2.io) - 通用的低级字节码操作和分析。
- [Byte Buddy](https://bytebuddy.net) - 通过流畅的 API 进一步简化了字节码生成。
- [bytecode-viewer](https://github.com/Konloch/bytecode-viewer) - Java 8 Jar 和 Android APK 逆向工程套件。 （仅限 GPL-3.0）
- [Byteman](https://byteman.jboss.org) - 通过 DSL（规则）在运行时操作字节码；主要用于测试/故障排除。 （LGPL-2.1-或更高版本）
- [cglib](https://github.com/cglib/cglib) - 字节码生成库。
- [Javassist](https://github.com/jboss-javassist/javassist) - 尝试简化字节码编辑。
- [Maker](https://github.com/cojen/maker) - 提供低级字节码生成。
- [Mixin](https://github.com/SpongePowered/Mixin) - 使用真实的 Java 代码在运行时操作字节码。
- [Perses](https://github.com/nicolasmanic/perses) - 根据混沌工程原理，在字节码级别动态注入故障/延迟。
- [Recaf](https://www.coley.software/Recaf/) - JVM 逆向工程工具包，本质上是 Java 字节码的 IDE。

### 缓存

_提供缓存设施的库._

- [cache2k](https://cache2k.org) - 内存中高性能缓存库。
- [Caffeine](https://github.com/ben-manes/caffeine) - 高性能、近乎最佳的缓存库。
- [Ehcache](http://www.ehcache.org) - 分布式通用缓存。
- [Infinispan](https://infinispan.org) - 用于缓存的高并发键/值数据存储。

### 命令行界面

_与 CLI 相关的所有内容的库。_

#### 参数解析

_协助解析命令行参数的库。_

- [Airline](https://rvesse.github.io/airline/) - 基于注释的框架，用于解析类似 Git 的命令行参数。
- [JCommander](http://jcommander.org) - 具有自定义类型和通过实现接口进行验证的命令行参数解析框架。
- [jbock](https://github.com/jbock-java/jbock) - 无反射命令行解析器。
- [JLine](https://github.com/jline/jline3) - 包括现代 shell 的功能，例如完成度或历史记录。
- [picocli](https://picocli.info) - ANSI 颜色和样式的使用有助于基于注释的 POSIX/GNU/any 语法、子命令、选项和位置参数的强类型。

#### 基于文本的用户界面

_提供 TUI 框架或构建块相关功能的库。_

- [AliveJTUI](https://github.com/yehorsyrin/alivejTUI) - 声明式、React 风格的 TUI 库，用于将终端 UI 构建为具有基于差异的渲染、焦点管理和主题的组件树。
- [Jansi](https://github.com/fusesource/jansi) - 用于格式化控制台输出的 ANSI 转义码。
- [Jexer](https://gitlab.com/AutumnMeowMeow/jexer) - 高级控制台（和 Swing）文本用户界面（TUI）库，具有可鼠标拖动的窗口、内置终端窗口管理器和 Sixel 图像支持。看起来像[Turbo Vision](https://en.wikipedia.org/wiki/Turbo_Vision)。
- [Text-IO](https://github.com/beryx/text-io) - 帮助创建完整的基于控制台的应用程序。
- [Lanterna](https://github.com/mabe02/lanterna) - 简单的控制台文本GUI库，类似于curses。 （仅限 LGPL-3.0）

### 云

_集成或使用特定于云的功能的库。_

- [AWS SDK for Java](https://github.com/aws/aws-sdk-java) - 提供用于与 Amazon Web Services 交互的 Java API。
- [Google Cloud Client Libraries](https://github.com/googleapis/google-cloud-java) - 用于从 Java 应用程序访问 Google Cloud 服务的客户端库。

### 代码分析

_提供指标和质量测量的工具。_

- [Checkstyle](https://github.com/checkstyle/checkstyle) - 编码约定和标准的静态分析。 （LGPL-2.1-或更高版本）
- [Error Prone](https://github.com/google/error-prone) - 将常见的编程错误捕获为编译时错误。
- [Error Prone Support](https://github.com/PicnicSupermarket/error-prone-support) - 容易出错的扩展：额外的错误检查器和大量的 Refaster 模板。
- [Infer](https://github.com/facebook/infer) - 用于验证代码正确性的现代静态分析工具。
- [jQAssistant](https://jqassistant.org) - 使用基于 Neo4J 的查询语言进行静态代码分析。 （仅限 GPL-3.0）
- [NullAway](https://github.com/uber/NullAway) - 以较低的构建时间开销消除 NullPointerExceptions。
- [PMD](https://github.com/pmd/pmd) - 源代码分析用于查找不良编码实践。
- [p3c](https://github.com/alibaba/p3c) - 提供阿里巴巴PMD、IDEA、Eclipse的编码指南。
- [RefactorFirst](https://github.com/jimbethancourt/RefactorFirst) - 识别上帝类和高度耦合类并确定其优先级。
- [SonarJava](https://github.com/SonarSource/sonar-java) - SonarQube 和 SonarLint 的静态分析器。 （仅限 LGPL-3.0）
- [Spoon](https://github.com/INRIA/spoon) - 用于分析和转换 Java 源代码的库。
- [Spotbugs](https://github.com/spotbugs/spotbugs) - 字节码的静态分析以发现潜在的错误。 （仅限 LGPL-2.1）
- [ToolsHref](https://toolshref.com) - 在线 Java 代码分析器和 JSON 到 Mermaid 可视化工具。

### 代码覆盖率

_支持测试套件代码覆盖率指标收集的框架和工具。_

- [Clover](https://www.atlassian.com/software/clover) - 依赖于源代码检测而不是字节码检测。
- [Cobertura](https://cobertura.github.io/cobertura/) - 依靠离线（或静态）字节码检测和类加载来收集代码覆盖率指标。 （仅限 GPL-2.0）
- [Delta Coverage](https://github.com/gw-kit/delta-coverage-plugin) - 根据提供的差异计算新代码和修改代码的代码覆盖率，支持 JaCoCo 和 IntelliJ 覆盖率引擎。
- [JaCoCo](https://www.eclemma.org/jacoco/) - 使用离线和运行时字节码检测来收集代码覆盖率指标的框架。

### 代码生成器

_为重复代码生成模式以减少冗长和错误倾向的工具。_

- [ADT4J](https://github.com/sviperll/adt4j) - 用于代数数据类型的 JSR-269 代码生成器。
- [Auto](https://github.com/google/auto) - 生成工厂、服务和值类。
- [Avaje Http Server](https://avaje.io/http/) - 使用 Javalin 或 Helidon (Nima) SE 生成轻量级 JAX-RS 风格的 http 服务器。
- [Bootify ![c]](https://bootify.io) - 使用 JPA 模型和 REST API 生成基于浏览器的 Spring Boot 应用程序。
- [EasyEntityToDTO](https://github.com/Marcel091004/EasyEntityToDTO) - 用于自动 DTO 和映射器生成的注释处理器，具有零样板。
- [FreeBuilder](https://github.com/inferred/FreeBuilder) - 自动生成Builder模式。
- [Geci](https://github.com/verhas/javageci) - 发现需要生成代码的文件，自动更新并使用方便的 API 写入源。
- [Immutables](https://immutables.github.io) - 注释处理器生成简单、安全且一致的值对象。
- [JavaPoet](https://github.com/square/javapoet) - 用于生成源文件的API。
- [JHipster](https://github.com/jhipster/generator-jhipster) - 适用于 Spring Boot 和 AngularJS 的 Yeoman 源代码生成器。
- [Joda-Beans](https://www.joda.org/joda-beans/) - 向 Java 添加可查询属性、增强 JavaBean 的小型框架。
- [JPA Buddy ![c]](https://www.jpa-buddy.com) - IntelliJ IDEA 插件。提供用于生成 JPA 实体、Spring Data JPA 存储库、Liquibase 变更日志和 SQL 脚本的可视化工具。通过将模型与数据库进行比较，以及从数据库表逆向工程 JPA 实体，提供自动 Liquibase/Flyway 脚本生成。
- [JSpecify Package-Info Generator](https://github.com/bcaillard/jspecify-packageinfo-generator) - Maven 插件，可自动生成带有 JSpecify 注释（@NullMarked 和 @NullUnmarked）的 package-info.java 文件，帮助您管理 Java 项目中的 null 边界，而无需手动样板。
- [Lombok](https://projectlombok.org) - 旨在减少冗长的代码生成器。
- [Record-Builder](https://github.com/Randgalt/record-builder) - Java 文件的配套构建器类、withers 和模板。
- [Spring CRUD Generator](https://github.com/mzivkovicdev/spring-crud-generator) - 用于从 YAML/JSON 规范生成 Spring Boot CRUD 应用程序的 Maven 插件。
- [Telosys](https://www.telosys.org/) - 简单而轻量的代码生成器可作为 Eclipse 插件和 CLI 使用。

### 编译器-编译器

_帮助创建解析器、解释器或编译器的框架。_

- [ANTLR](https://www.antlr.org) - 用于自顶向下解析的复杂的全功能框架。
- [JavaCC](https://javacc.github.io/javacc/) - 生成自顶向下解析器的解析器生成器。允许词法状态切换并允许扩展 BNF 规范。
- [JFlex](https://jflex.de) - 词法分析器生成器。

### 计算机视觉

_寻求从图像和视频中获取高级信息的图书馆。_

- [BoofCV](https://boofcv.org) - 用于图像处理、相机校准、跟踪、SFM、MVS、3D 视觉、QR 码等的库。
- [ImageJ](https://imagej.net/ImageJ) - 具有 API 的医学图像处理应用程序。
- [JavaCV](https://github.com/bytedeco/javacv) - OpenCV、FFmpeg 等的 Java 接口。

### 配置

_提供外部配置的库._

- [avaje config](https://avaje.io/config/) - 加载 yaml 和属性文件，支持动态配置、插件、文件监视和配置事件侦听器。
- [centraldogma](https://github.com/line/centraldogma) - 基于Git、ZooKeeper和HTTP/2的高可用版本控制服务配置存储库。
- [ClearConfig](https://github.com/japgolly/clear-config-java) - 类型安全、可组合的配置库，重点关注运行时清晰度。
- [config](https://github.com/lightbend/config) - 支持 Java 属性、JSON 或其人类优化超集 HOCON 的配置库。
- [Configurate](https://github.com/SpongePowered/Configurate) - 支持各种配置格式和转换的配置库。
- [Curator Framework](https://curator.apache.org/) - Apache ZooKeeper 的高级 API。
- [dotenv](https://github.com/shyiko/dotenv) - 使用特定于环境的文件的十二因素配置库。
- [Externalized Properties](https://github.com/joel-jeremy/externalized-properties) - 简单、轻量级但功能强大的配置库，支持解析来自外部源（例如文件、数据库、git 存储库和任何自定义源）的属性，以及可扩展的后处理/转换机制。
- [Gestalt](https://github.com/gestalt-config/gestalt) - Gestalt 提供了一个全面的解决方案来应对配置管理的挑战。它允许您从多个输入中获取配置数据，智能地合并它们，并以结构化、类型安全的方式呈现它们。
- [ini4j](http://ini4j.sourceforge.net) - 提供用于处理 Windows 的 INI 文件的 API。
- [KAConf](https://github.com/mariomac/kaconf) - 用于 Java 和 Kotlin 的基于注释的配置系统。
- [microconfig](https://microconfig.io) - 专为微服务设计的配置系统，有助于将配置与代码分离。不同服务的配置可以具有公共部分和特定部分，并且可以动态分布。
- [owner](https://github.com/lviggiano/owner) - 减少属性的样板。

### 约束满足问题求解器

_帮助实现优化和可满足性问题的库。_

- [Choco](https://choco-solver.org) - 使用约束规划技术的现成约束满足问题求解器。
- [JaCoP](https://github.com/radsz/jacop) - 包括 FlatZinc 语言的接口，使其能够执行 MiniZinc 模型。 (AGPL-3.0)
- [OptaPlanner](https://www.optaplanner.org) - 业务规划和资源调度优化求解器。
- [Timefold](https://timefold.ai/docs) - 灵活的求解器，支持 Spring/Quarkus 以及车辆路线问题、维护计划、员工轮班计划等快速入门。

### CSV

_简化读取/写入 CSV 数据的框架和库。_

- [FastCSV](https://github.com/osiegmar/FastCSV) - 性能优化、无依赖性且符合 RFC 4180。
- [jackson-dataformat-csv](https://github.com/FasterXML/jackson-dataformat-csv) - 用于读取和写入 CSV 的 Jackson 扩展。
- [opencsv](http://opencsv.sourceforge.net) - 简单的 CSV 解析器。
- [Super CSV](https://super-csv.github.io/super-csv/) - 强大的 CSV 解析器，支持 Dozer、Joda-Time 和 Java 8。
- [uniVocity-parsers](https://github.com/uniVocity/univocity-parsers) - 最快、功能最齐全的解析器之一。还附带 TSV 和固定宽度记录的解析器。

### 数据结构

_高效且特定的数据结构._

- [Apache Avro](https://avro.apache.org) - 具有动态类型、无标记数据且无需手动分配 ID 的数据交换格式。
- [Apache Orc](https://orc.apache.org) - 适用于基于 Hadoop 的工作负载的快速高效的列式存储格式。
- [Apache Parquet](https://parquet.apache.org) - 基于 Google 关于 Dremel 论文的汇编算法的列式存储格式。
- [Apache Thrift](https://thrift.apache.org) - 起源于 Facebook 的数据交换格式。
- [Big Queue](https://github.com/bulldog2011/bigqueue) - 基于内存映射文件的快速持久队列。
- [HyperMinHash-java](https://github.com/LiveRamp/HyperMinHash-java) - 用于计算对数空间中的并集、交集和集合基数的概率数据结构。
- [Persistent Collection](https://github.com/hrldcpr/pcollections) - Java Collections Framework 的持久且不可变的类似物。
- [Protobuf](https://github.com/protocolbuffers/protobuf) - Google 的数据交换格式。
- [RoaringBitmap](https://github.com/RoaringBitmap/RoaringBitmap) - 快速高效的压缩位图。
- [SBE](https://github.com/real-logic/simple-binary-encoding) - 简单二进制编码，最快的消息格式之一。
- [Tape](https://github.com/square/tape) - 快如闪电、事务性、基于文件的 FIFO。
- [Wire](https://github.com/square/wire) - 干净、轻量级的协议缓冲区。

### 数据库

_简化与数据库交互的一切。_

- [Apache Calcite](https://calcite.apache.org) - 动态数据管理框架。它包含构成典型数据库管理系统的许多部分。
- [Apache Drill](https://drill.apache.org) - 用于大数据探索的分布式动态模式 ANSI SQL 查询引擎。
- [Apache Phoenix](https://phoenix.apache.org) - HBase 上的高性能关系数据库层，适用于低延迟应用程序。
- [ArcadeDB](https://arcadedb.com) - 支持图形、文档、键值、时间序列和向量嵌入的多模型数据库，兼容 SQL、Cypher、Gremlin、MongoDB 和 Redis API。
- [ArangoDB](https://github.com/arangodb/arangodb-java-driver) - ArangoDB Java 驱动程序。
- [Chronicle Map](https://github.com/OpenHFT/Chronicle-Map) - 高效、内存中（选择持久化到磁盘）、堆外键值存储。
- [Debezium](https://debezium.io/) - 用于捕获变更数据的低延迟数据流平台。
- [druid](https://druid.apache.org) - 高性能、面向列的分布式数据存储。
- [eXist](https://github.com/eXist-db/exist) - NoSQL文档数据库和应用平台。 （仅限 LGPL-2.1）
- [FlexyPool](https://github.com/vladmihalcea/flexy-pool) - 将指标和故障转移策略引入最常见的连接池解决方案。
- [Flyway](https://flywaydb.org) - 简单的数据库迁移工具。
- [H2](https://h2database.com) - 小型 SQL 数据库以其内存功能而闻名。
- [HikariCP](https://github.com/brettwooldridge/HikariCP) - 高性能 JDBC 连接池。
- [HSQLDB](https://hsqldb.org/) - HyperSQL 100% Java 数据库。
- [JDBI](http://jdbi.org) - 方便的 JDBC 抽象。
- [Jedis](https://github.com/xetorthio/jedis) - 用于与 Redis 交互的小型客户端，具有命令方法。
- [Jest](https://github.com/searchbox-io/Jest) - Elasticsearch REST API 的客户端。
- [jetcd](https://github.com/justinsb/jetcd) - etcd 的客户端库。
- [Jinq](https://github.com/my2iu/Jinq) - 通过 Java 8 Lambda 的符号执行（在 JPA 或 jOOQ 之上）进行类型安全的数据库查询。
- [jOOQ](https://www.jooq.org) - 基于 SQL 架构生成类型安全代码。
- [Leaf](https://github.com/Meituan-Dianping/Leaf) - 分布式ID生成服务。
- [Lettuce](https://lettuce.io/) - Lettuce 是一个可扩展的 Redis 客户端，用于构建非阻塞响应式应用程序。
- [Liquibase](http://www.liquibase.org) - 独立于数据库的库，用于跟踪、管理和应用数据库模式更改。
- [MapDB](http://www.mapdb.org) - 嵌入式数据库引擎，提供支持在磁盘或堆外内存中的并发集合。
- [MariaDB4j](https://github.com/vorburger/MariaDB4j) - MariaDB 的启动器，无需安装或外部依赖项。
- [Modality](https://github.com/arkanovicz/modality) - 具有数据库逆向工程功能的轻量级 ORM。
- [Open J Proxy](https://github.com/Open-J-Proxy/ojp) - Type 3 JDBC 驱动程序和第 7 层代理服务器，用于将应用程序与关系数据库连接管理解耦。
- [OpenDJ](https://github.com/OpenIdentityPlatform/OpenDJ) - 符合 LDAPv3 的目录服务，为 Java 平台开发，为身份提供高性能、高可用性且安全的存储。
- [Querydsl](http://www.querydsl.com) - 类型安全的统一查询。
- [QueryStream](https://github.com/querystream/querystream) - 使用类似 Stream 的 API 构建 JPA Criteria 查询。
- [QuestDB](https://github.com/questdb/questdb) - 用于时间序列的高性能 SQL 数据库。支持 InfluxDB 线路协议、PostgreSQL 线路协议和 REST。
- [Realm](https://github.com/realm/realm-java) - 移动数据库直接在手机、平板电脑或可穿戴设备内运行。
- [Redisson](https://github.com/redisson/redisson) - 允许在 Redis 服务器之上使用分布式且可扩展的数据结构。
- [requery](https://github.com/requery/requery) - 现代、轻量级但功能强大的对象映射和 SQL 生成器。轻松映射或创建数据库，或从任何使用 Java 的平台执行查询和更新。
- [Speedment](https://github.com/speedment/speedment) - 利用 Java 8 的 Stream API 进行查询的数据库访问库。
- [Spring Data Dynamic Query](https://github.com/tdilber/spring-data-dynamic-query) - Spring Data JPA、MongoDB 和 Elasticsearch 的统一动态查询接口，支持高级 JOIN、OR 逻辑、范围条件、强大的投影和零样板的高级功能。
- [Spring Data JPA MongoDB Expressions](https://github.com/mhewedy/spring-data-jpa-mongodb-expressions) - 允许您使用 MongoDB 查询语言来查询您的关系数据库。
- [Trino](https://trino.io) - 适用于大数据的分布式 SQL 查询引擎。
- [Vibur DBCP](https://www.vibur.org) - 具有高级性能监控功能的 JDBC 连接池库。
- [Xodus](https://github.com/JetBrains/xodus) - 高度并发的无模式事务且符合 ACID 的嵌入式数据库。
- [CosId](https://github.com/Ahoo-Wang/CosId) - 通用、灵活、高性能的分布式 ID 生成器。
- [Apache ShardingSphere](https://github.com/apache/shardingsphere) - 分布式 SQL 事务和查询引擎，允许在任何数据库上进行数据分片、扩展、加密等。

### 日期和时间

_与处理日期和时间相关的库._

- [iCal4j](https://github.com/ical4j/ical4j) - 解析和构建 iCalendar [RFC 5545](https://tools.ietf.org/html/rfc5545) 数据模型。
- [Jollyday](https://github.com/focus-shift/jollyday) - 确定给定年份、国家/名称以及最终州/地区的假期。
- [ThreeTen-Extra](https://github.com/ThreeTen/threeten-extra) - 补充 JDK 8 中的附加日期时间类。
- [Time4J](https://github.com/MenoData/Time4J) - 高级日期和时间库。 （仅限 LGPL-2.1）

### 去中心化

_处理去中心化任务的库._

- [java-tron](https://github.com/tronprotocol/java-tron) Tron 协议的实现，利用区块链开发去中心化应用程序。

### 依赖注入

_有助于实现[控制反转](https://en.wikipedia.org/wiki/Inversion_of_control)范例的库。_

- [Apache DeltaSpike](https://deltaspike.apache.org) - CDI 扩展框架。
- [Avaje Inject](https://avaje.io/inject/) - 以微服务为中心的无反射编译时注入框架。
- [Dagger](https://dagger.dev/) - 无反射的编译时注入框架。
- [Dimension-DI](https://github.com/akardapolov/dimension-di) - 使用 JDK 类文件 API 的 JSR-330 运行时依赖项注入。
- [Feather](https://github.com/zsoltherpai/feather) - 超轻量级、符合 JSR-330 的依赖注入库。
- [Governator](https://github.com/Netflix/governator) - 增强 Google Guice 的扩展和实用程序。
- [Guice](https://github.com/google/guice) - 轻量级且固执己见的框架完善了 Dagger。
- [HK2](https://eclipse-ee4j.github.io/glassfish-hk2/) - 轻量级动态依赖注入框架。
- [JayWire](https://github.com/vanillasource/jaywire) - 轻量级依赖注入框架。 （仅限 LGPL-3.0）

### 发展

_从根本上增强开发过程。_

- [AspectJ](https://www.eclipse.org/aspectj/) - 无缝的面向方面的编程扩展。
- [DCEVM](https://dcevm.github.io) - JVM 修改允许在运行时无限制地重新定义加载的类。 （仅限 GPL-2.0）
- [Faux Pas](https://github.com/zalando/faux-pas) - 该库通过规避默认情况下不允许 Java 运行时中的任何函数接口抛出已检查异常的问题来简化错误处理。
- [HotswapAgent](https://github.com/HotswapProjects/HotswapAgent) - 无限制的运行时类和资源重新定义。 （仅限 GPL-2.0）
- [JavaParser](https://github.com/javaparser/javaparser) - 解析、修改和生成 Java 代码。
- [JavaSymbolSolver](https://github.com/javaparser/javasymbolsolver) - 符号求解器。
- [Manifold](https://github.com/manifold-systems/manifold) - 通过类型安全元编程、结构类型和扩展方法等强大功能为 Java 重新注入活力。
- [NoException](https://noexception.machinezoo.com) - 允许在函数接口中检查异常并将异常转换为可选返回。
- [SneakyThrow](https://github.com/rainerhahnekamp/sneakythrow) - 忽略已检查的异常而不进行字节码操作。也可以在 Java 8 流操作中使用。
- [Tail](https://nrktkt.github.io/tail/) - 使用尾调用优化启用无限递归。

### 分布式应用程序

_用于编写分布式和容错应用程序的库和框架。_

- [Apache Geode](https://geode.apache.org) - 内存数据管理系统，提供可靠的异步事件通知和有保证的消息传递。
- [Apache Storm](https://storm.apache.org) - 实时计算系统。
- [Apache ZooKeeper](https://zookeeper.apache.org) - 大型分布式系统的分布式配置、同步和命名注册表的协调服务。
- [Atomix](https://atomix.io) - 容错分布式协调框架。
- [Axon](https://axoniq.io) - 用于创建 CQRS 应用程序的框架。
- [Dropwizard Circuit Breaker](https://github.com/mtakaki/dropwizard-circuitbreaker) - Dropwizard 的断路器设计模式。 （仅限 GPL-2.0）
- [Failsafe](https://github.com/jhalterman/failsafe) - 通过重试和断路器进行简单的故障处理。
- [Hazelcast](https://github.com/hazelcast/hazelcast) - 具有免费开源版本的高度可扩展的内存数据网格。
- [JGroups](http://www.jgroups.org) - 用于可靠消息传递和集群创建的工具包。
- [Quasar](http://docs.paralleluniverse.co/quasar/) - JVM 的轻量级线程和参与者。
- [resilience4j](https://github.com/resilience4j/resilience4j) - 功能容错库。
- [OpenIG](https://github.com/OpenIdentityPlatform/OpenIG) - 具有专门会话管理和凭证重播功能的高性能反向代理服务器。
- [ScaleCube Services](https://github.com/scalecube/scalecube-services) - 基于 SWIM 和 gossip 协议的嵌入式集群成员库。
- [Zuul](https://github.com/Netflix/zuul) - 提供动态路由、监控、弹性、安全性等的网关服务。

### 分布式事务

_分布式事务提供了一种在并发访问和部分失败的情况下确保数据更新一致性的机制。_

- [Atomikos](https://www.atomikos.com) - 为 REST、SOA 和微服务提供事务，并支持 JTA 和 XA。
- [Bitronix](https://github.com/bitronix/btm) - JTA 1.1 API 的简单但完整的实现。
- [Narayana](https://narayana.io) - 提供对传统ACID和补偿事务的支持，同时符合JTA、JTS等标准。 （仅限 LGPL-2.1）
- [Seata](https://github.com/seata/seata) - 在微服务架构下提供高性能且易于使用的分布式事务服务。

### 分布

_处理本机格式应用程序分发的工具。_

- [Artipie](https://github.com/artipie/artipie) - 将它们托管在文件系统或 S3 上的二进制工件管理工具包。
- [Boxfuse ![c]](https://boxfuse.com) - 使用不可变基础设施的原则将 JVM 应用程序部署到 AWS。
- [Capsule](https://github.com/puniverse/capsule) - 简单而强大的打包和部署。类固醇的胖 JAR，或支持 JVM 优化容器的“Docker for Java”。
- [Central Repository](https://search.maven.org) - 最大的二进制组件存储库可作为开源社区的免费服务。默认由 Apache Maven 使用，并且可在所有其他构建工具中使用。
- [Cloudsmith ![c]](https://cloudsmith.io) - 完全托管的包管理 SaaS，支持 Maven/Gradle/SBT 并提供免费套餐。
- [Getdown](https://github.com/threerings/getdown) - 用于将 Java 应用程序部署到最终用户计算机并使其保持最新的系统。开发作为 Java Web Start 的替代方案。
- [IzPack](http://izpack.org) - 设置跨平台部署的创作工具。
- [JavaPackager](https://github.com/fvarrui/JavaPackager) - Maven 和 Gradle 插件提供了一种简单的方法来将 Java 应用程序打包到本机 Windows、macOS 或 GNU/Linux 可执行文件中，并为其生成安装程序。
- [jDeploy](https://www.jdeploy.com) - 将桌面应用程序部署为本机 Mac、Windows 或 Linux 捆绑包。
- [jlink.online](https://github.com/AdoptOpenJDK/jlink.online) - 通过 HTTP 构建优化的运行时。
- [Nexus ![c]](https://www.sonatype.com) - 具有代理和缓存功能的二进制管理。
- [packr](https://github.com/libgdx/packr) - 打包 JAR、资产和 JVM，以便在 Windows、Linux 和 macOS 上进行本机分发。
- [really-executable-jars-maven-plugin](https://github.com/brianm/really-executable-jars-maven-plugin) - 用于制作自动执行 JAR 的 Maven 插件。

### 文件处理

_协助处理办公文档格式的库。_

- [Apache POI](https://poi.apache.org) - 支持 OOXML（XLSX、DOCX、PPTX）以及 OLE2（XLS、DOC 或 PPT）。
- [documents4j](https://documents4j.com/#/) - 使用第三方转换器（例如 MS Word）进行文档格式转换的 API。
- [docx4j](https://www.docx4java.org/trac/docx4j) - 创建和操作 Microsoft Open XML 文件。
- [fastexcel](https://github.com/dhatim/fastexcel) - 用于读取和写入大型 Excel (XLSX) 工作表的高性能库。
- [Sheetz](https://github.com/chitralabs/sheetz) - 用于读取和写入 Excel 和 CSV 文件的库，具有基于注释的映射、流支持和内置验证。
- [zerocell](https://github.com/creditdatamw/zerocell) - 基于注释的 API，用于将数据从 Excel 工作表读取到 POJO，重点是减少开销。

### 金融

_与金融领域相关的图书馆._

- [Cassandre](https://github.com/cassandre-tech/cassandre-trading-bot) - 交易机器人框架。
- [Parity](https://github.com/paritytrading/parity) - 交易场所平台。
- [Philadelphia](https://github.com/paritytrading/philadelphia) - 低延迟的金融信息交换。
- [Square](https://github.com/square/connect-java-sdk) - 与 Square API 集成。
- [Stripe](https://github.com/stripe/stripe-java) - 与 Stripe API 集成。
- [ta4j](https://github.com/ta4j/ta4j) - 用于技术分析的库。

### 形式验证

_形式化方法工具：证明助手、模型检查、符号执行等_

- [CATG](https://github.com/ksen007/janala2) - Concolic 单元测试引擎。使用形式化方法自动生成单元测试。
- [Checker Framework](https://checkerframework.org) - 可插拔类型系统。包括空类型、物理单位、不变性类型等等。 （仅限 GPL-2.0，带有 Classpath-exception-2.0）
- [Daikon](https://plse.cs.washington.edu/daikon/) - 检测可能的程序不变量并根据这些不变量生成 JML 规范。
- [Java Path Finder (JPF)](https://github.com/javapathfinder/jpf-core) - JVM 形式验证工具，包含模型检查器等。由美国宇航局创建。
- [JMLOK 2.0](https://massoni.computacao.ufcg.edu.br/home/jmlok) - 通过反馈引导的随机测试生成来检测代码和 JML 规范之间的不一致，并建议检测到的每个不符合项的可能原因。 （仅限 GPL-3.0）
- [KeY](https://www.key-project.org) - 形式化软件开发工具，旨在尽可能无缝地集成面向对象软件的设计、实现、形式化规范和形式化验证。使用 JML 进行规范并使用符号执行进行验证。 （GPL-2.0 或更高版本）
- [OpenJML](http://www.openjml.org) - 将 JML 规范转换为 SMT-LIB 格式，并将程序隐含的证明问题传递给后端求解器。 （仅限 GPL-2.0）

### 函数式编程

_促进函数式编程的库._

- [Cyclops](https://github.com/aol/cyclops) - Monad 和流实用程序、推导式、模式匹配、所有 JDK 集合的功能扩展、未来流、蹦床等等。
- [derive4j](https://github.com/derive4j/derive4j) - Java 8 注释处理器和框架，用于派生代数数据类型构造函数、模式匹配和态射。 （仅限 GPL-3.0）
- [Fugue](https://bitbucket.org/atlassian/fugue) - Guava 的功能扩展。
- [Functional Java](http://www.functionaljava.org) - 实现许多基本和高级编程抽象，以帮助面向组合的开发。
- [jOOλ](https://github.com/jOOQ/jOOL) - Java 8 的扩展，旨在通过提供大量缺失的类型和一组丰富的顺序 Stream API 添加来修复 lambda 中的缺陷。
- [Packrat](https://github.com/jhspetersson/packrat) - Java Stream API 的收集器库。收集者可以通过自定义中间操作来增强流。
- [Parallel Collectors](https://github.com/pivovarit/parallel-collectors) - Stream API 收集器，用于使用自定义线程池进行并行处理，专为 I/O 密集型工作负载而设计。
- [protonpack](https://github.com/poetix/protonpack) - 流实用程序的集合。
- [StreamEx](https://github.com/amaembo/streamex) - 增强 Java 8 流。
- [Vavr](https://www.vavr.io) - 提供持久数据类型和功能控制结构的功能组件库。

### 游戏开发

_支持游戏开发的框架._

- [FXGL](https://almasb.github.io/FXGL/) - JavaFX 游戏开发框架。
- [input4j](https://gurkenlabs.github.io/input4j/) - 用于游戏手柄和操纵杆输入处理的轻量级跨平台库。
- [JBox2D](http://www.jbox2d.org/) - 著名的 C++ 2D 物理引擎的端口。
- [jMonkeyEngine](https://jmonkeyengine.org) - 现代 3D 开发的游戏引擎。
- [libGDX](https://libgdx.com) - 全方位跨平台、高层框架。
- [Litiengine](https://litiengine.com/) - 基于 AWT 的轻量级 2D 游戏引擎。
- [LWJGL](https://www.lwjgl.org) - 强大的框架，抽象 OpenGL/CL/AL 等库。
- [Mini2Dx](https://mini2dx.org) - 初学者友好、大师级的框架，用于快速原型设计和构建 2D 游戏。
- [Void2D](https://github.com/xzripper/Void2D) - 基于 Swing 的具有内置物理功能的高级 2D 游戏引擎。
- [vulkan4j](https://github.com/chuigda/vulkan4j) - Vulkan、OpenGL ES2 和 GLFW 内存分配器绑定。

### 地理空间

_用于处理地理空间数据和算法的库。_

- [Apache SIS](https://sis.apache.org) - 用于开发地理空间应用程序的库。
- [ArcGIS Maps SDK for Java![c]](https://github.com/Esri/arcgis-maps-sdk-java-samples/) - 用于向桌面应用程序添加地图和 GIS 功能的 JavaFX 库。
- [Geo](https://github.com/davidmoten/geo) - Java 中的 GeoHash 实用程序。
- [GeoTools](https://geotools.org) - 提供地理空间数据工具的库。 （仅限 LGPL-2.1）
- [GraphHopper](https://github.com/graphhopper/graphhopper) - 道路路由引擎。用作 Java 库或独立的 Web 服务。
- [H2GIS](http://www.h2gis.org) - H2数据库的空间扩展。 （仅限 LGPL-3.0）
- [Jgeohash](https://astrapi69.github.io/jgeohash/) - 使用 GeoHash 算法的库。
- [Mapsforge](https://github.com/mapsforge/mapsforge) - 基于OpenStreetMap数据的地图渲染。 （仅限 LGPL-3.0）
- [Spatial4j](https://github.com/locationtech/spatial4j) - 通用空间/地理空间库。

### 图形用户界面

_创建现代图形用户界面的库._

- [JavaFX](https://wiki.openjdk.java.net/display/OpenJFX/Main) - 摇摆的继承者。
- [Scene Builder](https://gluonhq.com/products/scene-builder/) - JavaFX 应用程序的可视化布局工具。
- [SnapKit](https://github.com/reportmill/SnapKit) - 适用于桌面和 Web 的现代 Java UI 库。
- [Sierra](https://github.com/HTTP-RPC/Sierra) - 用于快速开发 Swing 应用程序的 Lightwiegh 声明式 DSL。
- [SWT](https://www.eclipse.org/swt/) - 图形小部件工具包。

### 高性能

_有关高性能计算的一切，从集合到特定库。_

- [Agrona](https://github.com/real-logic/Agrona) - 高性能应用程序中常见的数据结构和实用方法。
- [Disruptor](https://lmax-exchange.github.io/disruptor/) - 线程间消息传递库。
- [Eclipse Collections](https://github.com/eclipse/eclipse-collections) - 集合框架的灵感来自 Smalltalk。
- [fastutil](http://fastutil.di.unimi.it) - 快速且紧凑的特定类型集合。
- [HPPC](https://labs.carrotsearch.com/hppc.html) - 原始收藏。
- [JCTools](https://github.com/JCTools/JCTools) - JDK 目前缺少并发工具。
- [Koloboke](https://github.com/leventov/Koloboke) - 精心设计的 Java 集合框架扩展，具有原始专业化等功能。

### HTTP 客户端

_帮助创建 HTTP 请求和/或绑定响应的库。_

- [Apache HttpComponents](https://hc.apache.org/) - 专注于 HTTP 和相关协议的低级 Java 组件工具集。
- [Async Http Client](https://github.com/AsyncHttpClient/async-http-client) - 异步 HTTP 和 WebSocket 客户端库。
- [Avaje Http Client](https://avaje.io/http-client) - JDK 11 的 HttpClient 的包装器，在其他增强功能中添加了类似 Feign 的接口。
- [Feign](https://github.com/OpenFeign/feign) - HTTP 客户端绑定器受到 Retrofit、JAXRS-2.0 和 WebSocket 的启发。
- [Google HTTP Client](https://github.com/googleapis/google-http-java-client) - 可插入的 HTTP 传输抽象，支持 java.net.HttpURLConnection、Apache HTTP Client、Android、Google App Engine、XML、Gson、Jackson 和 Protobuf。
- [methanol](https://github.com/mizosoft/methanol) - HTTP 客户端扩展库。
- [Retrofit](https://square.github.io/retrofit/) - 类型安全的 REST 客户端。
- [Ribbon](https://github.com/Netflix/ribbon) - 在云端经过实战测试的客户端 IPC 库。
- [Riptide](https://github.com/zalando/riptide) - Spring RestTemplate 的客户端响应路由。
- [unirest-java](https://github.com/Kong/unirest-java) - 简化的轻量级 HTTP 客户端库。

### 超媒体类型

_处理超媒体类型序列化的库。_

- [hate](https://github.com/blackdoor/hate) - 根据 HAL 规范构建超媒体友好的对象。
- [JSON-LD](https://github.com/jsonld-java/jsonld-java) - JSON-LD 实现。
- [Siren4J](https://github.com/eserating-chwy/siren4j) - Siren 规范库。
- [Spring HATEOAS](https://github.com/spring-projects/spring-hateoas) - 独立和 Spring 支持使用 HAL、HAL FORMS、Collection+JSON、ALPS 和 UBER 构建基于超媒体的 API。

### 集成开发环境

_尝试简化开发多个方面的集成开发环境。_

- [Eclipse](https://www.eclipse.org) - 建立了支持大量插件和语言的开源项目。
- [IntelliJ IDEA ![c]](https://www.jetbrains.com/idea/) - 支持多种 JVM 语言，为 Android 开发提供良好的选择。商业版针对企业部门。
- [jGRASP](https://www.jgrasp.org) - 创建的目的是提供与调试器结合使用的软件可视化，例如控制结构图、UML 类图和对象查看器。
- [NetBeans](https://netbeans.apache.org) - 提供多种 Java SE 和 EE 功能的集成，从数据库访问到 HTML5。
- [SnapCode](https://reportmill.com/SnapCode/) - 现代 IDE for Java 在浏览器中运行，专注于教育。
- [Visual Studio Code](https://code.visualstudio.com/docs/languages/java) - 通过使用内部市场的扩展，通过简单、现代的工作流程为轻量级项目提供 Java 支持。

### 图像

_帮助创建、评估或操作图形图像的库。_

- [Barcode-Lib4J](https://github.com/vws-java/Barcode-Lib4J) - 将 QR 码、DataMatrix 和其他 1D/2D 条形码生成为矢量（PDF、EPS、SVG）和光栅（PNG、BMP、JPG）图像，具有 DPI 感知、高精度和 CMYK 颜色模型支持。
- [Imgscalr](https://github.com/rkalla/imgscalr) - 以纯 Java 2D 实现的简单、高效且硬件加速的图像缩放库。
- [Tess4J](https://github.com/nguyenq/tess4j) - Tesseract OCR API 的 JNA 包装器。
- [Thumbnailator](https://github.com/coobird/thumbnailator) - 高品质缩略图生成库。
- [TwelveMonkeys](https://github.com/haraldk/TwelveMonkeys) - 扩展支持的图像文件格式数量的插件集合。
- [ZXing](https://github.com/zxing/zxing) - 多格式一维/二维条码图像处理库。
- [image-comparison](https://github.com/romankh3/image-comparison) - 比较 2 个相同尺寸的图像并通过绘制矩形直观地显示差异的库。图像的某些部分可以从比较中排除。
- [vips-ffm](https://github.com/lopcode/vips-ffm) - 使用 Java 的“外部函数和内存”API 全面绑定 libvips。
- [scrimage](https://sksamuel.github.io/scrimage) - 用于操作图像的不可变、功能性和高性能 JVM 库。

### 内省

_有助于使 Java 内省和反射 API 更容易、更快速地使用的库。_

- [ClassGraph](https://github.com/classgraph/classgraph) - ClassGraph（以前称为 FastClasspathScanner）是一个超快、超轻量级、并行的类路径扫描器和模块扫描器，适用于 Java、Scala、Kotlin 和其他 JVM 语言。
- [jOOR](https://github.com/jOOQ/jOOR) - jOOR 代表 jOOR 面向对象反射。它是 java.lang.reflect 包的简单包装器。
- [Mirror](http://projetos.vidageek.net/mirror/mirror/) - Mirror 的创建是为了解决一个简单的问题，通常命名为 ReflectionUtil，它几乎适用于所有依赖反射来完成高级任务的项目。
- [Objenesis](http://objenesis.org) - 允许动态实例化，无需默认构造函数，例如具有必需参数、副作用或抛出异常的构造函数。
- [ReflectASM](https://github.com/EsotericSoftware/reflectasm) - ReflectASM 是一个非常小的 Java 库，它通过使用代码生成来提供高性能反射。
- [Reflections](https://github.com/ronmamo/reflections) - Reflections 扫描您的类路径，索引元数据，允许您在运行时查询它，并可以保存和收集项目中许多模块的信息。

### 作业调度

_用于调度后台作业的库._

- [JobRunr](https://github.com/jobrunr/jobrunr) - 作业调度库，利用 lambda 执行即发即忘、延迟和重复作业。使用乐观锁定保证单个调度程序实例的执行。具有持久性、最小依赖性和可嵌入的特性。
- [Quartz](https://github.com/quartz-scheduler/quartz) - 功能丰富的开源作业调度库，几乎可以集成到任何 Java 应用程序中。
- [Sundial](https://github.com/knowm/Sundial) - 轻量级框架，用于简单地定义作业、定义触发器和启动调度程序。
- [Wisp](https://github.com/Coreoz/Wisp) - 具有最小占用空间和简单 API 的简单库。
- [db-scheduler](https://github.com/kagkarlsson/db-scheduler) - 持久且集群友好的调度程序。
- [easy-batch](https://github.com/j-easy/easy-batch) - 使用简单的处理管道设置批处理作业。记录从数据源按顺序读取，在管道中处理并批量写入数据接收器。
- [shedlock](https://github.com/lukas-krecan/ShedLock) - 确保您的计划任务最多同时执行一次。如果一个任务正在一个节点上执行，它会获取一个锁，以防止从另一个节点或线程执行同一任务。

### JSON

_用于将 JSON 序列化到 Java 对象以及从 Java 对象反序列化 JSON 的库。_

- [Avaje Jsonb](https://avaje.io/jsonb/) - 通过源代码生成和类似 Jackson 的注释进行无反射 Json 绑定。
- [DSL-JSON](https://github.com/ngs-doo/dsl-json) - 具有高级编译时数据绑定的 JSON 库。
- [Genson](http://genson.io) - 功能强大且易于使用的 Java 到 JSON 转换库。
- [Gson](https://github.com/google/gson) - 将对象序列化为 JSON，反之亦然。即时使用时性能良好。
- [HikariJSON](https://github.com/brettwooldridge/HikariJSON) - 高性能 JSON 解析器，比 Jackson 快 2 倍。
- [jackson-modules-java8](https://github.com/FasterXML/jackson-modules-java8) - 用于 Java 8 数据类型和功能的 Jackson 模块集。
- [Jackson-datatype-money](https://github.com/zalando/jackson-datatype-money) - 开源 Jackson 模块，支持 JavaMoney 数据类型的 JSON 序列化和反序列化。
- [Jackson](https://github.com/FasterXML/jackson) - 与 GSON 类似，但如果您需要更频繁地实例化库，则可以提高性能。
- [JSON-io](https://github.com/jdereg/json-io) - 将 Java 转换为 JSON/TOON 并返回。支持复杂的对象图、循环引用和 TOON 格式，可节省 40-50% 的 LLM 令牌。
- [jsoniter](http://jsoniter.com) - 快速灵活的库，带有迭代器和惰性解析 API。
- [LoganSquare](https://github.com/bluelinelabs/LoganSquare) - 基于 Jackson 的流 API 的 JSON 解析和序列化库。优于 GSON 和 Jackson 的库。
- [Moshi](https://github.com/square/moshi) - 现代 JSON 库，不那么固执己见，并使用 List 和 Map 等内置类型。
- [Yasson](https://github.com/eclipse-ee4j/yasson) - 类和 JSON 文档之间的绑定层，类似于 JAXB。
- [fastjson](https://github.com/alibaba/fastjson) - 非常快的处理器，没有额外的依赖性和完整的数据绑定。
- [Jolt](https://github.com/bazaarvoice/jolt) - JSON 到 JSON 转换工具。
- [JsonPath](https://github.com/json-path/JsonPath) - 使用类似 XPATH 的语法从 JSON 中提取数据。
- [JsonSurfer](https://github.com/jsurfer/JsonSurfer) - 流式 JsonPath 处理器专用于处理大型且复杂的 JSON 数据。

### JVM 和 JDK

_JVM/JDK 的当前实现._

- [Which JDK](https://whichjdk.com/) - 常见 JVM 的概述及其优缺点。
- [Adopt Open JDK](https://adoptopenjdk.net) - 社区驱动的 OpenJDK 构建，包括 HotSpot 和 OpenJ9。
- [Corretto](https://aws.amazon.com/corretto/) - Amazon 提供的免费、多平台、生产就绪的 OpenJDK 分发。 （仅限 GPL-2.0，带有 Classpath-exception-2.0）
- [Dragonwell8](https://github.com/alibaba/dragonwell8) - OpenJDK 的下游版本针对在线电子商务、金融、物流应用进行了优化。
- [Graal](https://github.com/oracle/graal) - 多语言嵌入式 JVM。 （仅限 GPL-2.0，带有 Classpath-exception-2.0）
- [Liberica JDK](https://bell-sw.com) - 使用 OpenJDK 构建，经过彻底测试并通过了 JCK。 （仅限 GPL-2.0，带有 Classpath-exception-2.0）
- [OpenJ9](https://github.com/eclipse/openj9) - 高性能、企业级、灵活许可、开放管理的跨平台 JVM 扩展和增强了 Eclipse OMR 和 OpenJDK 项目的运行时技术组件。
- [Open JDK](https://openjdk.java.net) - 打开 JDK 社区主页。 （仅限 GPL-2.0，带有 Classpath-exception-2.0）
- [ParparVM](https://github.com/codenameone/CodenameOne/tree/master/vm) - 适用于 iOS 的具有非阻塞并发 GC 的 VM。 （仅限 GPL-2.0，带有 Classpath-exception-2.0）
- [RedHat Open JDK](https://developers.redhat.com/products/openjdk/overview) - RedHat 的 OpenJDK 发行版。 （仅限 GPL-2.0，带有 Classpath-exception-2.0）
- [SAP Machine](https://sap.github.io/SapMachine/) - SAP 的免费、经过严格测试和 JCK 验证的 OpenJDK 友好分支。 （仅限 GPL-2.0，带有 Classpath-exception-2.0）
- [Zulu](https://www.azul.com/products/zulu-community/) - OpenJDK 专为 Windows、Linux 和 macOS 构建。 （仅限 GPL-2.0，带有 Classpath-exception-2.0）
- [Microsoft JDK](https://github.com/microsoft/openjdk) - Microsoft Build of OpenJDK，免费、开源、新鲜酿造！

### 记录

_记录应用程序行为的库._

- [Apache Log4j 2](https://logging.apache.org/log4j/) - 使用强大的插件和配置架构进行完全重写。
- [Echopraxia](https://github.com/tersesystems/echopraxia) - API 围绕结构化日志记录、丰富上下文和条件日志记录而设计。有 Logback 和 Log4J2 实现，但 Echopraxia 的 API 完全无依赖性，这意味着它可以使用任何日志记录 API 来实现。
- [Graylog](https://www.graylog.org) - 适合扩展角色和权限管理的开源聚合器。 （仅限 GPL-3.0）
- [Kibana](https://www.elastic.co/kibana) - 分析和可视化日志文件。有些功能需要付费。
- [Logback](http://logback.qos.ch) - 强大的日志记录库，通过 Groovy 提供有趣的配置选项。
- [Logbook](https://github.com/zalando/logbook) - 用于 HTTP 请求和响应日志记录的可扩展开源库。
- [Logstash](https://www.elastic.co/logstash) - 用于管理日志文件的工具。
- [p6spy](https://github.com/p6spy/p6spy) - 为所有 JDBC 事务启用日志记录，而无需更改代码。
- [SLF4J](http://www.slf4j.org) - 抽象层/简单的日志记录门面。
- [tinylog](https://tinylog.org/v2/) - 具有静态记录器类的轻量级日志记录框架。
- [OpenTracing Toolbox](https://github.com/zalando/opentracing-toolbox) - 构建在 OpenTracing 之上并为现有仪器提供扩展和插件的库集合。
- [Flogger](https://google.github.io/flogger/) - Flogger 是一个流畅的 Java 日志记录 API。它支持多种功能，并且比现有的日志记录 API 具有许多优势。

### 机器学习

_提供用于从数据中学习的特定统计算法的工具。_

- [Apache Flink](https://flink.apache.org) - 快速、可靠、大规模的数据处理引擎。
- [Apache Mahout](https://mahout.apache.org) - 可扩展算法专注于协同过滤、聚类和分类。
- [DatumBox](http://www.datumbox.com) - 提供多种用于自然语言处理的算法和预训练模型。
- [Deeplearning4j](https://deeplearning4j.org) - 分布式多线程深度学习库。
- [DJL](https://djl.ai) - 用于深度学习的高级且与引擎无关的框架。
- [H2O ![c]](https://www.h2o.ai) - 用于大数据统计的分析引擎。
- [Intelligent java](https://github.com/Barqawiz/IntelliJava) - 以编程方式与远程深度学习和语言模型无缝集成。
- [JSAT](https://github.com/EdwardRaff/JSAT) - 支持多线程执行的预处理、分类、回归和聚类算法。 （仅限 GPL-3.0）
- [m2cgen](https://github.com/BayesWitnesses/m2cgen) - 用于将模型转换为本机代码的 CLI 工具。
- [Neureka](https://github.com/Gleethos/neureka) - 一个轻量级、独立于平台、OpenCL 加速的 nd 数组/张量库。
- [oj! Algorithms](https://www.ojalgo.org/) - 数据科学、机器学习和科学计算所需的高性能数学、线性代数和优化。
- [Oryx 2](https://github.com/OryxProject/oryx) - 用于构建实时、大规模机器学习应用程序的框架。包括用于协作过滤、分类、回归和聚类的端到端应用程序。
- [Siddhi](https://github.com/siddhi-io/siddhi) - 云原生流和复杂事件处理引擎。
- [Smile](https://github.com/haifengl/smile) - 统计机器智能和学习引擎提供了一组机器学习算法和可视化库。
- [Tribuo](https://tribuo.org/) - 提供用于分类、回归、聚类、模型开发的工具以及与其他库（例如 scikit-learn、pytorch 和 TensorFlow）的接口。
- [Weka](https://www.cs.waikato.ac.nz/ml/weka/) - 用于从预处理到可视化的数据挖掘任务的算法集合。 （仅限 GPL-3.0）

### 消息传递

_帮助在客户端之间发送消息以确保协议独立性的工具。_

- [Aeron](https://github.com/real-logic/Aeron) - 高效、可靠的单播和组播消息传输。
- [Apache ActiveMQ](https://activemq.apache.org) - 实现 JMS 并将同步通信转换为异步通信的消息代理。
- [Apache Camel](https://camel.apache.org) - 通过企业集成模式将不同的传输 API 粘合在一起。
- [Apache Kafka](https://kafka.apache.org) - 高吞吐量分布式消息系统。
- [Apache Pulsar](https://pulsar.apache.org) - 分布式发布/子消息系统。
- [Apache RocketMQ](https://rocketmq.apache.org) - 快速、可靠且可扩展的分布式消息传递平台。
- [Apache Qpid](https://qpid.apache.org) - Apache Qpid 制作了使用 AMQP 并支持多种语言和平台的消息传递工具。
- [AutoMQ](https://github.com/AutoMQ/automq-for-kafka) - AutoMQ 是一种云原生、无服务器的重新设计的 Kafka，易于扩展、无需管理且经济高效。
- [Emissary](https://github.com/joel-jeremy/emissary) - 简单、轻量级且快速的消息传递库，用于解耦消息（请求和事件）和消息处理程序。
- [EventBus](https://github.com/greenrobot/EventBus) - 简单的发布/订阅事件总线。
- [Hermes](http://hermes.allegro.tech) - 构建在 Kafka 之上的快速可靠的消息代理。
- [JeroMQ](https://github.com/zeromq/jeromq) - ZeroMQ 的实现。
- [Nakadi](https://github.com/zalando/nakadi) - 在 Kafka 之上提供 RESTful API。
- [RabbitMQ Java client](https://github.com/rabbitmq/rabbitmq-java-client) - RabbitMQ 客户端。
- [Smack](https://github.com/igniterealtime/Smack) - 跨平台 XMPP 客户端库。
- [NATS client](https://github.com/nats-io/nats.java) - NATS 客户端。

### 微服务

_用于创建和管理微服务的工具。_

- [ActiveRPC](https://rpc.activej.io) - 用于复杂高负载分布式应用程序和类似 Memcached 的解决方案的轻量级快速库。
- [Armeria](https://github.com/line/armeria) - 基于 Java 8、Netty、HTTP/2、Thrift 和 gRPC 构建的异步 RPC/REST 客户端/服务器库。
- [consul-api](https://github.com/Ecwid/consul-api) - Consul API 的客户端：分布式、高度可用且数据中心感知的注册/发现服务。
- [Eureka](https://github.com/Netflix/eureka) - 基于 REST 的服务注册表，用于弹性负载平衡和故障转移。
- [Helidon](https://helidon.io) - 编写微服务的两种风格的方法：功能反应式和作为 MicroProfile 的实现。
- [JDA](https://github.com/DV8FromTheWorld/JDA) - 包装 Discord REST API 及其 WebSocket 事件。
- [KeenType](https://github.com/DaveJarvis/KeenType) - 新排版系统的基于 Java 实现的现代化版本，很大程度上基于 Donald E. Knuth 的原始 TeX。
- [kubernetes-client](https://github.com/fabric8io/kubernetes-client) - 客户端通过流畅的 DSL 提供对完整 Kubernetes 和 OpenShift REST API 的访问。
- [Micronaut](https://micronaut.io) - 现代全栈框架，注重模块化、最小内存占用和启动时间。
- [Nacos](https://nacos.io) - 用于构建云原生应用程序的动态服务发现、配置和服务管理平台。
- [OpenAI-Java](https://github.com/TheoKanning/openai-java) - 用于使用 OpenAI 的 GPT-3 API 的 Java 库。
- [Quarkus](https://quarkus.io) - 专为 HotSpot 和 Graal VM 定制的 Kubernetes 堆栈。
- [Sentinel](https://github.com/alibaba/Sentinel) - 流控制组件可实现微服务的可靠性、弹性和监控。

### 杂项

_其他一切._

- [CQEngine](https://github.com/npgall/cqengine) - 对 Java 集合进行超快速、类似 SQL 的查询。
- [Design Patterns](https://github.com/iluwatar/java-design-patterns) - 最常见设计模式的实现和解释。
- [FF4J](https://github.com/ff4j/ff4j) - Java 的功能标志。
- [FizzBuzz Enterprise Edition](https://github.com/EnterpriseQualityCoding/FizzBuzzEnterpriseEdition) - 由严肃的商人出于严肃的商业目的而进行的 FizzBu​​zz 的严肃实施。 （无明确许可）
- [IP2Location.io Java SDK](https://github.com/ip2location/ip2location-io-java) - IP2Location.io 地理位置 API 和 IP2WHOIS 域 WHOIS API 的包装器。
- [ISBN core](https://github.com/ladutsko/isbn-core) - 一个小型库，包含 ISBN-10 和 ISBN-13 的表示对象以及解析、验证和格式化对象的工具。
- [J2ObjC](https://github.com/google/j2objc) - Java 到 Objective-C 的转换器，用于将 Android 库移植到 iOS。
- [JBake](https://jbake.org) - 静态网站生成器。
- [JBang](https://www.jbang.dev/) - JBang 使使用 Java 编写脚本变得容易。它允许您使用单个文件进行代码和依赖项管理，并允许您直接运行它。
- [JBot](https://github.com/rampatra/jbot) - 用于构建聊天机器人的框架。 （仅限 GPL-3.0）
- [JCuda](http://jcuda.org) - JCuda 为 CUDA 和 CUDA 相关库提供 Java 绑定。
- [JEmoji](https://github.com/felldo/JEmoji) - 自动生成的表情符号库，提供对表情符号的类型安全直接访问以及对 Discord、Slack、GitHub 和更多功能的别名支持。
- [Jimfs](https://github.com/google/jimfs) - 内存中的文件系统。
- [JObfuscator![c]](https://www.pelock.com/products/jobfuscator) - 源代码混淆器。
- [Joda-Money](https://www.joda.org/joda-money/) - JDK 未提供基本货币和货币类和算法。
- [jOOX](https://github.com/jooq/joox) - org.w3c.dom 包的简单包装器，允许使用受 jQuery 启发的 API 进行流畅的 XML 文档创建和操作。
- [JPad](http://jpad.io) - 片段跑步者。
- [jsweet](https://github.com/cincheo/jsweet) - TypeScript/JavaScript 的源代码转换器。
- [Maven Wrapper](https://github.com/takari/maven-wrapper) - Gradle Wrapper for Maven 的类似物，允许在不安装 Maven 的情况下构建项目。
- [Membrane Service Proxy](https://github.com/membrane/service-proxy) - 开源的反向代理框架。
- [MinimalFTP](https://github.com/Guichaguri/MinimalFTP) - 轻量级、小型且可定制的 FTP 服务器。
- [LittleProxy](https://github.com/adamfisk/LittleProxy) - Netty 基于事件的网络库之上的高性能 HTTP 代理。
- [Modern Java - A Guide to Java 8](https://github.com/winterbe/java8-tutorial) - 流行的 Java 8 指南。
- [Modernizer](https://github.com/gaul/modernizer-maven-plugin) - 检测旧版 Java API 的使用。
- [Nyagram](https://github.com/kaleert/nyagram) - 基于 Spring Boot 3 和 Java 21 的 Telegram 机器人的反应式、类型安全框架。
- [OctoLinker](https://github.com/OctoLinker/OctoLinker) - 浏览器扩展允许更有效地浏览 GitHub 上的代码。
- [OpenRefine](http://openrefine.org) - 用于处理混乱数据的工具：清理、转换、使用 Web 服务扩展数据并将其链接到数据库。
- [PipelinR](https://github.com/sizovs/pipelinr) - 用于通过管道使用处理程序和命令的小型实用程序库。
- [Polyglot for Maven](https://github.com/takari/polyglot-maven) - Maven 3.3.1+ 的扩展，允许使用 XML 以外的方言编写 POM 模型。
- [Rollgate](https://rollgate.io) - 具有 Java SDK 的云管理功能标志平台，支持逐步推出、A/B 测试和实时更新。
- [RR4J](https://github.com/Kartikvk1996/RR4J) - RR4J是一个记录java字节码执行情况并允许开发人员在本地重放的工具。
- [Simple Java Mail](https://github.com/bbottema/simple-java-mail) - 使用干净流畅的 API 进行邮件发送。
- [Smooks](https://github.com/smooks/smooks) - 基于片段的消息处理框架。 （Apache-2.0 或 LGPL-3.0 或更高版本）
- [Svix](https://github.com/svix/svix-webhooks/tree/main/java) - Svix API 发送 webhook 和验证签名的库。
- [Togglz](https://www.togglz.org) - 功能切换模式的实现。
- [TypeTools](https://github.com/jhalterman/typetools) - 用于解析泛型类型的工具。
- [webcam-capture](https://github.com/sarxos/webcam-capture) - 用于直接在 Java 中使用内置和外部网络摄像头的库。
- [XMLBeam](https://github.com/SvenEwald/xmlbeam) - 通过在代码中使用注释或 XPath 来处理 XML。
- [yGuard](https://github.com/yWorks/yGuard) - 通过重命名和收缩进行混淆。

### 移动开发

_用于创建或管理移动应用程序的工具。_

- [Codename One](https://www.codenameone.com) - 用于编写本机移动应用程序的跨平台解决方案。 （仅限 GPL-2.0，带有 Classpath-exception-2.0）
- [MobileUI](https://mobileui.dev) - 用于开发具有 Java 和 Kotlin 原生 UI 的移动应用程序的跨平台框架。
- [Multi-OS Engine](https://multi-os-engine.org) - 用于开发本机移动（iOS、Android 等）应用程序的开源跨平台引擎。

### 监控

_通过提供遥测来观察/监控生产中的应用程序的工具。_

- [Apitally](https://github.com/apitally/apitally-java) - Spring Boot 应用程序的简单、注重隐私的 API 监控、分析和请求日志记录。
- [Automon](https://github.com/stevensouza/automon) - 将 AOP 的强大功能与监控和/或日志记录工具相结合。
- [Boot Usage Spring Boot Starter](https://github.com/dhruv-15-03/boot-usage) - Spring Boot Actuator 扩展提供应用程序启动和运行时指标，包括 JVM 正常运行时间、内存使用情况和 CPU 负载。
- [Datadog ![c]](https://github.com/DataDog/dd-trace-java) - 现代监控和分析。
- [Dropwizard Metrics](https://github.com/dropwizard/metrics) - 通过 JMX 或 HTTP 公开指标并将其发送到数据库。
- [Failsafe Actuator](https://github.com/zalando/failsafe-actuator) - Spring-Boot 环境中故障安全断路器的开箱即用监控。
- [Glowroot](https://glowroot.org) - 开源 Java APM。
- [HertzBeat](https://github.com/dromara/hertzbeat) - 具有自定义监控和无代理的实时监控系统。
- [hippo4j](https://github.com/opengoofy/hippo4j/blob/develop/README-EN.md) - 动态且可观察的线程池框架。
- [inspectIT](https://www.inspectit.rocks) - 通过可以动态更改的钩子捕获详细的运行时信息。它支持通过 OpenTracing API 在多个系统上进行跟踪，并且可以将数据与最终用户监控相关联。
- [Instrumental ![c]](https://instrumentalapp.com) - 实时 Java 应用程序性能监控。具有免费开发帐户的商业服务。
- [Jaeger client](https://github.com/jaegertracing/jaeger-client-java) - 耶格客户端。
- [JavaMelody](https://github.com/javamelody/javamelody) - 性能监控和分析。
- [jmxtrans](https://github.com/jmxtrans/jmxtrans) - 连接到多个 JVM 并通过 JMX 查询它们的属性。它的查询语言基于 JSON，允许非 Java 程序员访问 JVM 属性。支持不同的输出写入，包括 Graphite、Ganglia 和 StatsD。
- [Jolokia](https://jolokia.org) - JMX 优于 REST。
- [Micrometer](https://github.com/micrometer-metrics/micrometer) - 供应商中立的指标/可观察性外观，适用于最流行的指标/可观察性库。
- [Micrometer Tracing](https://github.com/micrometer-metrics/tracing) - 适用于最流行的跟踪器库的供应商中立的分布式跟踪外观。
- [nudge4j](https://github.com/lorenzoongithub/nudge4j) - 通过字节码注入从 Java 8 浏览器远程开发控制台。
- [OpenTelemetry](https://github.com/open-telemetry/opentelemetry-java) - 检测、生成、收集和导出遥测数据，以帮助您分析软件的性能和行为。
- [Pinpoint](https://github.com/naver/pinpoint) - 开源 APM 工具。
- [Prometheus](https://github.com/prometheus/client_java) - 提供多维数据模型、DSL、自治服务器节点等等。
- [Sentry ![c]](https://github.com/getsentry/sentry-java) - 与应用程序错误跟踪和性能分析平台 [Sentry](https://github.com/getsentry/sentry) 集成。
- [SPM ![c]](https://github.com/sematext/sematext-agent-java) - 具有 JVM 应用程序分布式事务跟踪的性能监视器。
- [Stagemonitor](https://github.com/stagemonitor/stagemonitor) - JVM 应用程序的开源性能监控和事务跟踪。
- [Sysmon](https://github.com/palantir/Sysmon) - 用于 Java VM 的轻量级平台监控工具。
- [zipkin](https://zipkin.io) - 分布式跟踪系统，收集解决微服务架构中的延迟问题所需的计时数据。

### 本地人

_用于使用特定于平台的本机库。_

- [Aparapi](https://github.com/Syncleus/aparapi) - 将字节码转换为 OpenCL，允许在 GPU 上执行。
- [JavaCPP](https://github.com/bytedeco/javacpp) - 提供对本机 C++ 的高效且轻松的访问。
- [JNA](https://github.com/java-native-access/jna) - 使用本机库而无需编写 JNI。还提供通用系统库的接口。
- [JNR](https://github.com/jnr/jnr-ffi) - 使用本机库而无需编写 JNI。还提供通用系统库的接口。与 JNA 目标相同，但速度更快，并作为即将推出的 [巴拿马项目](http://openjdk.java.net/projects/panama) 的基础。
- [native-lib-loader](https://github.com/scijava/native-lib-loader) - 用于从 Java 中提取和加载本机库的本机库加载器。

### 自然语言处理

_专门处理文本的库._

- [CogCompNLP](https://github.com/CogComp/cogcomp-nlp) - 为纯文本输入提供通用注释器。 （研究和学术使用许可）
- [CoreNLP](https://nlp.stanford.edu/software/corenlp.shtml) - 为标记、命名实体识别和情感分析等任务提供一组基本工具。 （GPL-3.0 或更高版本）
- [DKPro](https://dkpro.github.io) - 可重复使用的 NLP 工具集合，用于语言预处理、机器学习、词汇资源等。
- [Hypherator](https://github.com/ejossev/hypherator-java) - 具有类似迭代器接口的 Java 连字符库。可以开箱即用 - 捆绑了多种语言的词典。
- [LingPipe](http://alias-i.com/lingpipe/) - 用于从 POS 标记到情感分析等任务的工具包。

### 网络

_用于构建网络服务器的库._

- [Commons-networking](https://github.com/CiscoSE/commons-networking) - 服务器发送事件的客户端 (SSE)。
- [Comsat](https://github.com/puniverse/comsat) - 将标准 Java Web 相关 API 与 Quasar 光纤和参与者集成。
- [Dubbo](https://github.com/apache/dubbo) - 高性能RPC框架。
- [Grizzly](https://javaee.github.io/grizzly/) - 蔚来框架。用作 Glassfish 中的网络层。
- [gRPC-java](https://github.com/grpc/grpc-java) - 基于protobuf和HTTP/2的RPC框架。
- [KryoNet](https://github.com/EsotericSoftware/kryonet) - 提供干净简单的 API，使用 NIO 和 Kryo 实现高效的 TCP 和 UDP 客户端/服务器网络通信。
- [MINA](https://mina.apache.org) - 抽象的、事件驱动的异步 I/O API，用于通过 Java NIO 通过 TCP/IP 和 UDP/IP 进行网络操作。
- [Netty](https://netty.io) - 用于构建高性能网络应用程序的框架。
- [Drift](https://github.com/airlift/drift) - 易于使用、基于注释的库，用于创建 Thrift 客户端和可序列化类型。
- [ServiceTalk](https://github.com/apple/servicetalk) - 基于 Netty 构建的框架，具有针对特定协议定制的 API 并支持多种编程范例。
- [sshj](https://github.com/hierynomus/sshj) - 以编程方式使用 SSH、SCP 或 SFTP。
- [TLS Channel](https://github.com/marianobarrios/tls-channel) - 通过 SSLEngine 实现 ByteChannel 接口，从而实现易于使用（类似套接字）的 TLS。
- [Undertow](http://undertow.io) - 基于 NIO 提供阻塞和非阻塞 API 的 Web 服务器。在 WildFly 中用作网络层。 （仅限 LGPL-2.1）
- [urnlib](https://github.com/slub/urnlib) - 表示、解析和编码 URN，如 RFC 2141 中所示。（仅限 GPL-3.0）
- [Fluency](https://github.com/komamitsu/fluency) - Fluentd 和 Fluent Bit 的高吞吐量数据摄取记录器。

### ORM

_处理对象持久性的API._

- [Apache Cayenne](https://cayenne.apache.org) - 提供干净、静态的数据访问 API。还包括一个 GUI 建模器，用于处理数据库映射、数据库逆向工程和生成。
- [Doma](https://github.com/domaframework/doma) - 数据库访问框架，使用注释处理以及称为双向 SQL 的本机 SQL 模板在编译时验证和生成源代码。
- [Ebean](https://ebean.io) - 提供简单、快速的数据访问。
- [EclipseLink](https://www.eclipse.org/eclipselink/) - 支持多种持久性标准：JPA、JAXB、JCA 和 SDO。
- [Hibernate](http://hibernate.org/orm/) - 强大且广泛使用，拥有活跃的社区。 （仅限 LGPL-2.1）
- [MyBatis](https://github.com/mybatis/mybatis-3) - 将对象与存储过程或 SQL 语句结合起来。
- [mybatis-dynamic](https://github.com/myacelw/mybatis-dynamic) - MyBatis 的代码优先动态 ORM，具有运行时模式修改。
- [MyBatis-Plus](https://github.com/baomidou/mybatis-plus) - MyBatis 的一个强大的增强工具包，用于简化开发。
- [ObjectiveSql](https://github.com/braisdom/ObjectiveSql) - ActiveRecord ORM 用于快速开发和约定优于配置。
- [Permazen](https://github.com/permazen/permazen) - 语言自然持久层。
- [SimpleFlatMapper](https://github.com/arnaudroger/SimpleFlatMapper) - 简单的数据库和 CSV 映射器。

### 平台即服务

_Java 平台即服务._

- [AWS Elastic Beanstalk ![c]](https://aws.amazon.com/elasticbeanstalk/) - 基于 AWS，支持 Tomcat 和 Jetty。
- [AWS Lambda ![c]](https://aws.amazon.com/lambda/) - 无服务器计算。
- [Google Cloud ![c]](https://cloud.google.com) - Google 的云基础设施。
- [Heroku ![c]](https://www.heroku.com) - 抽象计算环境。
- [Microsoft Azure ![c]](https://azure.microsoft.com/en-us/) - Microsoft 的云基础设施。
- [OpenShift ![c]](https://www.openshift.com) - 额外提供本地解决方案。

### 寻路

_用于在图形和空间环境中查找路线的算法和库。_

- [Pathetic](https://github.com/bsommerfeld/pathetic) - 高度可配置的 3D A\* 寻路库，使用特定的优化来实现高性能。

### PDF

_帮助处理 PDF 文件的工具。_

- [Apache FOP](https://xmlgraphics.apache.org/fop/) - 从 XSL-FO 创建 PDF。
- [Apache PDFBox](https://pdfbox.apache.org) - 用于创建和操作 PDF 的工具箱。
- [Dynamic Jasper](https://intive-fdv.github.io/DynamicJasper/) - JasperReports 的抽象层。 （仅限 LGPL-3.0）
- [DynamicReports](https://github.com/dynamicreports/dynamicreports) - 简化 JasperReports。 （仅限 LGPL-3.0）
- [Eclipse BIRT](https://www.eclipse.org/birt) - 使用基于 Eclipse 的可视化编辑器创建 PDF 和其他格式（DOCX、XLSX、HTML 等）的报告引擎。
- [flyingsaucer](https://github.com/flyingsaucerproject/flyingsaucer) - XML/XHTML 和 CSS 2.1 渲染器。 （LGPL-2.1-或更高版本）
- [iText ![c]](https://itextpdf.com/en) - 以编程方式创建 PDF 文件。
- [JasperReports](https://community.jaspersoft.com/project/jasperreports-library) - 复杂的报告引擎。 （仅限 LGPL-3.0）
- [Open HTML to PDF](https://github.com/openhtmltopdf/openhtmltopdf) - 正确支持基于 Flyingsaucer 和 Apache PDFBox 的现代 PDF 标准。
- [OpenPDF](https://github.com/LibrePDF/OpenPDF) - 开源 iText 分支。 （仅限 LGPL-3.0 和 MPL-2.0）
- [Tabula](https://github.com/tabulapdf/tabula-java) - 从 PDF 文件中提取表格。

### 性能分析

_性能分析、分析和基准测试工具。_

- [fastThread ![c]](https://fastthread.io) - 使用基于云的免费上传界面分析和可视化线程转储。
- [GCeasy ![c]](https://gceasy.io) - 分析和可视化 GC 日志的工具。它提供了一个免费的基于云的上传接口。
- [honest-profiler](https://github.com/jvm-profiling-tools/honest-profiler) - 低开销、无偏差采样分析器。
- [Heap Seance](https://github.com/SegfaultSorcerer/heap-seance) - 内存泄漏诊断，将 jcmd、jmap、jstat、JFR、Eclipse MAT 和 async-profiler 编排到结构化调查工作流程中，并提供基于置信度的结论。
- [jHiccup](https://github.com/giltene/jHiccup) - 记录和记录平台 JVM 停顿。
- [JITWatch](https://github.com/AdoptOpenJDK/jitwatch) - 分析 HotSpot JVM 进行的 JIT 编译器优化。
- [JMH](http://openjdk.java.net/projects/code-tools/jmh/) - 用于构建、运行和分析以 Java 和其他针对 JVM 的语言编写的纳/微米/毫/宏观基准测试的工具。 （GPL-2.0 仅适用于 Classpath-exception-2.0）
- [LatencyUtils](https://github.com/LatencyUtils/LatencyUtils) - 用于延迟测量和报告的实用程序。
- [JVM Hotpath](https://github.com/sfkamath/jvm-hotpath) - 用于行级执行频率分析的 Java 代理，以识别算法瓶颈。

### 平台

_框架是包含多个类别的多个库的套件。_

#### 阿帕奇共享区

- [BCEL](http://commons.apache.org/proper/commons-bcel/) - 字节码工程库 - 分析、创建和操作 Java 类文件。
- [BeanUtils](http://commons.apache.org/proper/commons-beanutils/) - 围绕 Java 反射和内省 API 的易于使用的包装器。
- [BeanUtils2](http://commons.apache.org/sandbox/commons-beanutils2/) - 重新设计 Commons BeanUtils。
- [BSF](http://commons.apache.org/proper/commons-bsf/) - Bean 脚本框架 - 脚本语言的接口，包括 JSR-223。
- [Chain](http://commons.apache.org/proper/commons-chain/) - 责任链模式实施。
- [ClassScan](http://commons.apache.org/sandbox/commons-classscan/) - 无需加载即可查找类接口、方法、字段和注释。
- [CLI](http://commons.apache.org/proper/commons-cli/) - 命令行参数解析器。
- [CLI2](http://commons.apache.org/sandbox/commons-cli2/) - 重新设计 Commons CLI。
- [Codec](http://commons.apache.org/proper/commons-codec/) - 通用编码/解码算法，例如语音、base64 或 URL。
- [Collections](http://commons.apache.org/proper/commons-collections/) - 扩展或增强 Java 集合框架。
- [Compress](http://commons.apache.org/proper/commons-compress/) - 定义用于处理 tar、zip 和 bzip2 文件的 API。
- [Configuration](http://commons.apache.org/proper/commons-configuration/) - 读取各种格式的配置/首选项文件。
- [Convert](http://commons.apache.org/sandbox/commons-convert/) - Commons-Convert 旨在提供一个专用于将一种类型的对象转换为另一种类型的任务的单一库。
- [CSV](http://commons.apache.org/proper/commons-csv/) - 用于读取和写入逗号分隔值文件的组件。
- [Daemon](http://commons.apache.org/proper/commons-daemon/) - 类似 unix-daemon 的 java 代码的替代调用机制。
- [DBCP](http://commons.apache.org/proper/commons-dbcp/) - 数据库连接池服务。
- [DbUtils](http://commons.apache.org/proper/commons-dbutils/) - JDBC 帮助程序库。
- [Digester](http://commons.apache.org/proper/commons-digester/) - XML 到 Java 对象的映射实用程序。
- [Email](http://commons.apache.org/proper/commons-email/) - 用于从 Java 发送电子邮件的库。
- [Exec](http://commons.apache.org/proper/commons-exec/) - Java 中用于处理外部进程执行和环境管理的 API。
- [FileUpload](http://commons.apache.org/proper/commons-fileupload/) - Servlet 和 Web 应用程序的文件上传功能。
- [Finder](http://commons.apache.org/sandbox/commons-finder/) - Java 库的灵感来自 UNIX find 命令。
- [Flatfile](http://commons.apache.org/sandbox/commons-flatfile/) - 用于处理平面数据结构的 Java 库。
- [Functor](http://commons.apache.org/proper/commons-functor/) - 可以作为对象或代表单个通用函数的对象进行操作的函数。
- [Graph](http://commons.apache.org/sandbox/commons-graph/) - 通用图形 API 和算法。
- [I18n](http://commons.apache.org/sandbox/commons-i18n/) - 添加本地化消息包的功能，该消息包由一个或多个属于在一起的本地化文本组成。
- [Id](http://commons.apache.org/sandbox/commons-id/) - id 是用于生成标识符的组件。
- [Imaging](http://commons.apache.org/proper/commons-imaging/) - 图片库。
- [IO](http://commons.apache.org/proper/commons-io/) - I/O 实用程序的集合。
- [Javaflow](http://commons.apache.org/sandbox/commons-javaflow/) - 继续实现以捕获应用程序的状态。
- [JCI](http://commons.apache.org/proper/commons-jci/) - Java 编译器接口。
- [JCS](http://commons.apache.org/proper/commons-jcs/) - Java 缓存系统。
- [Jelly](http://commons.apache.org/proper/commons-jelly/) - 基于 XML 的脚本和处理引擎。
- [Jexl](http://commons.apache.org/proper/commons-jexl/) - 表达式语言扩展了 JSTL 的表达式语言。
- [JNet](http://commons.apache.org/sandbox/commons-jnet/) - JNet 允许通过 java.net API 动态注册 url 流处理程序。
- [JXPath](http://commons.apache.org/proper/commons-jxpath/) - 使用 XPath 语法操作 Java Bean 的实用程序。
- [Lang](http://commons.apache.org/proper/commons-lang/) - 为 java.lang 中的类提供额外的功能。
- [Logging](https://commons.apache.org/proper/commons-logging/) - 围绕各种日志记录 API 实现的包装。
- [Math](http://commons.apache.org/proper/commons-math/) - 轻量级、独立的数学和统计组件。
- [Monitoring](http://commons.apache.org/sandbox/commons-monitoring/) - 监控旨在为Java应用程序提供一个简单但可扩展的监控解决方案。
- [Nabla](http://commons.apache.org/sandbox/commons-nabla/) - Nabla 提供自动微分类，可以生成用 Java 语言实现的任何函数的导数。
- [Net](http://commons.apache.org/proper/commons-net/) - 网络实用程序和协议实现的集合。
- [OGNL](http://commons.apache.org/proper/commons-ognl/) - 对象图导航语言。
- [OpenPGP](http://commons.apache.org/sandbox/commons-openpgp/) - 使用 OpenPGP 签署和验证数据的接口。
- [Performance](http://commons.apache.org/sandbox/commons-performance/) - 用于微基准测试客户端的小型框架，具有 Commons DBCP 和 Pool 的实现。
- [Pipeline](http://commons.apache.org/sandbox/commons-pipeline/) - 提供一组围绕工作队列设计的管道实用程序，这些实用程序并行运行以顺序处理数据对象。
- [Pool](http://commons.apache.org/proper/commons-pool/) - 通用对象池组件。
- [Proxy](http://commons.apache.org/proper/commons-proxy/) - 用于创建动态代理的库。
- [RDF](https://commons.apache.org/proper/commons-rdf/) - RDF 1.1 的常见实现，可以由 JVM 上的系统实现。
- [RNG](https://commons.apache.org/proper/commons-rng/) - Commons Rng 提供伪随机数生成器的实现。
- [SCXML](http://commons.apache.org/proper/commons-scxml/) - 状态图 XML 规范的实现旨在创建和维护 Java SCXML 引擎。
- [Validator](http://commons.apache.org/proper/commons-validator/) - 在 xml 文件中定义验证器和验证规则的框架。
- [VFS](http://commons.apache.org/proper/commons-vfs/) - 虚拟文件系统组件，用于将文件、FTP、SMB、ZIP 等视为单个逻辑文件系统。
- [Weaver](http://commons.apache.org/proper/commons-weaver/) - 提供一种简单的方法来增强（编织）已编译的字节码。

#### 其他

- [CUBA Platform](https://www.cuba-platform.com/) - 用于开发具有丰富 Web 界面的企业应用程序的高级框架，基于 Spring、EclipseLink 和 Vaadin。
- [Light-4J](https://github.com/networknt/light-4j/) - 快速、轻量级且高效的微服务框架，具有内置的[安全性](https://github.com/networknt/light-oauth2/)。
- [Orienteer](https://github.com/OrienteerBAP/Orienteer/) - 开源业务应用平台，用于快速配置/开发 CRM、ERP、LMS 和其他应用程序。
- [Spring](https://spring.io/projects/) - 提供了许多用于依赖注入、面向方面编程、安全性等的包。

### 流程

_帮助管理操作系统进程的库。_

- [ch.vorburger.exec](https://github.com/vorburger/ch.vorburger.exec) - 围绕 Apache Commons Exec 的便捷 API。
- [zt-exec](https://github.com/zeroturnaround/zt-exec) - 为 Apache Commons Exec 和 ProcessBuilder 提供统一的 API。
- [zt-process-killer](https://github.com/zeroturnaround/zt-process-killer) - 停止从 Java 启动的进程或通过 PID 的系统进程。

### 反应式库

_用于开发反应式应用程序的库._

- [Akka](https://akka.io) - 用于构建并发、分布式、容错和事件驱动应用程序的工具包和运行时。
- [Reactive Streams](https://github.com/reactive-streams/reactive-streams-jvm) - 提供具有非阻塞背压的异步流处理标准。
- [Reactor](https://github.com/reactor/reactor) - 用于在 JVM 上构建非阻塞应用程序的框架，提供对反应式编程的支持。
- [RxJava](https://github.com/ReactiveX/RxJava) - 允许使用可观察序列编写异步和基于事件的程序。
- [vert.x](https://vertx.io) - 多语言事件驱动的应用程序框架。

### REST 框架

_专门用于创建 RESTful 服务的框架。_

- [Dropwizard](https://github.com/dropwizard/dropwizard) - 用于使用 Jetty、Jackson、Jersey 和 Metrics 设置现代 Web 应用程序的自定框架。
- [Elide](https://elide.io) - 基于 JPA 数据模型的 JSON 或 GraphQL-API 的自定框架。
- [Jersey](https://jersey.github.io) - JAX-RS 参考实现。
- [Microserver](https://github.com/aol/micro-server) - 适用于 Spring 和 Spring Boot 的方便、可扩展的微服务插件系统。它拥有 30 多个插件并且还在不断增加，支持微单体和纯微服务风格。
- [Rapidoid](https://www.rapidoid.org) - 简单、安全且极其快速的框架，由嵌入式 HTTP 服务器、GUI 组件和依赖项注入组成。
- [rest.li](https://github.com/linkedin/rest.li) - 使用类型安全绑定和异步、非阻塞 IO 以及端到端开发人员工作流程构建健壮、可扩展的 RESTful 架构的框架，可促进清洁实践、统一的接口设计和一致的数据建模。
- [RESTEasy](https://resteasy.github.io) - JAX-RS 规范的完全认证和可移植实施。
- [RestExpress](https://github.com/RestExpress/RestExpress) - JBoss Netty HTTP 堆栈上的瘦包装器提供扩展和性能。
- [Restlet Framework](https://github.com/restlet/restlet-framework-java) - 开创性的框架，具有强大的路由和过滤功能，以及统一的客户端和服务器 API。
- [Spark](http://sparkjava.com) - Sinatra 启发的框架。
- [Crnk](http://www.crnk.io) - 实施 JSON API 规范，以构建面向资源的 REST 端点，包括排序、过滤、分页、链接、对象图、类型安全、批量更新、集成等。
- [springdoc-openapi](https://github.com/springdoc/springdoc-openapi) - 使用 Spring Boot 项目自动生成 API 文档。
- [Swagger](https://swagger.io) - 与语言无关的标准 REST API 接口。
- [openapi-generator](https://github.com/OpenAPITools/openapi-generator) - 允许根据 OpenAPI 规范自动生成 API 客户端库、SDK、服务器存根、文档和配置。

### 科学

_用于科学计算、分析和可视化的库。_

- [BioJava](https://biojava.org/) - 通过提供生物信息学中常用的算法、文件格式解析器、测序和 3D 可视化来促进生物数据的处理。
- [Chart-FX](https://github.com/GSI-CS-CO/chart-fx) - 科学图表库，重点关注大型数据集以 25 Hz 更新率进行性能优化的实时数据可视化。
- [DataMelt](https://datamelt.org/) - 科学计算、数据分析和数据可视化的环境。 （GPL-3.0 或更高版本）
- [Erdos](https://github.com/Erdos-Graph-Framework/Erdos) - 用于理论算法的模块化、轻量级和简单的图形框架。
- [GraphStream](http://graphstream-project.org) - 用于建模和分析动态图的库。
- [JFreeChart](http://www.jfree.org/jfreechart/) - 用于 Swing、JavaFX 和服务器端应用程序的 2D 图表库。 （仅限 LGPL-2.1）
- [JGraphT](https://github.com/jgrapht/jgrapht) - 提供数学图论对象和算法的图库。
- [JGraphX](https://github.com/jgraph/jgraphx) - 用于可视化（主要是 Swing）并与节点边缘图交互的库。
- [jSciPy](https://github.com/hissain/jscipy) - jSciPy 是一个专为科学计算而设计的 Java 库，提供受流行科学计算库启发的功能。它目前提供信号处理模块，包括巴特沃斯滤波器、寻峰算法和常微分方程的 RK4 求解器。
- [LogicNG](https://github.com/logic-ng/LogicNG) - 用于创建、操作和求解布尔和伪布尔公式的库。
- [Mines Java Toolkit](https://github.com/MinesJTK/jtk) - 用于地球物理科学计算、可视化和数字信号分析的库。
- [Morpheus](https://github.com/zavtech/morpheus-core) - 提供称为 DataFrame 的通用二维内存高效表格数据结构，为 JVM 上的科学计算提供高效的内存分析。
- [Orekit](https://www.orekit.org/) - 一个低级太空飞行动力学库，提供基本元素（轨道、日期、姿态、框架...）和各种算法（转换、传播、指向...）来处理它们。
- [Orson-Charts](https://github.com/jfree/orson-charts) - 生成各种 3D 图表，可以使用 Swing 和 JavaFX 显示或导出为 PDF、SVG、PNG 和 JPEG。 （仅限 GPL-3.0）
- [Tablesaw](https://github.com/jtablesaw/tablesaw) - 包括数据框架、嵌入式列存储以及数百种转换、汇总或筛选数据的方法。
- [XChart](https://github.com/knowm/XChart) - 用于绘制数据的轻量级库。有许多可定制的图表类型可用。

### 搜索

_索引文档以进行搜索和分析的引擎。_

- [Apache Lucene](https://lucene.apache.org) - 高性能、全功能、跨平台的文本搜索引擎库。
- [Apache Solr](https://lucene.apache.org/solr/) - 针对大流量优化的企业搜索引擎。
- [Elasticsearch](https://www.elastic.co) - 分布式、支持多租户的全文搜索引擎，具有 RESTful Web 界面和无架构 JSON 文档。
- [Indexer4j](https://github.com/haeungun/indexer4j) - 简单、轻便的全文索引和搜索库。

### 安全性

_处理安全、身份验证、授权或会话管理的库。_

- [Apache Shiro](https://shiro.apache.org) - 执行身份验证、授权、加密和会话管理。
- [Ayza](https://github.com/Hakky54/ayza) - 高级 SSL 配置生成器，用于使用 SSL/TLS 配置 HTTP 客户端和服务器。
- [Bouncy Castle](https://www.bouncycastle.org/java.html) - 通用加密库和 JCA 提供程序提供广泛的功能，从基本帮助程序到 PGP/SMIME 操作。
- [Certificate Ripper](https://github.com/Hakky54/certificate-ripper) - 用于从 HTTPS 端点提取和导出服务器证书的 CLI 工具和库。
- [DependencyCheck](https://github.com/jeremylong/DependencyCheck) - 检测项目依赖项中包含的公开披露的漏洞。
- [Cryptomator](https://cryptomator.org) - 云中文件的多平台、透明、客户端加密。 （仅限 GPL-3.0）
- [Hdiv](https://github.com/hdiv/hdiv) - 运行时应用程序可抵御 OWASP Top 10 中包含的应用程序安全风险，包括 SQL 注入、跨站点脚本、跨站点请求伪造、数据篡改和暴力攻击。
- [jjwt](https://github.com/jwtk/jjwt) - 适用于 Java 和 Android 的 JSON Web 令牌。
- [jwt-java](https://github.com/BastiaanJansen/jwt-java) - 使用流畅的 API 轻松创建和解析 JSON Web 令牌并创建自定义 JWT 验证器。
- [Jwks RSA](https://github.com/auth0/jwks-rsa-java) - JSON Web 密钥集解析器。
- [Kalium](https://github.com/abstractj/kalium) - 网络和密码学 (NaCl) 库的绑定。
- [Keycloak](https://www.keycloak.org) - 用于浏览器应用程序和 RESTful Web 服务的集成 SSO 和 IDM。
- [Keywhiz](https://github.com/square/keywhiz) - 用于分发和管理秘密的系统。
- [Nbvcxz](https://github.com/GoSimpleLLC/nbvcxz) - 高级密码强度估计。
- [OACC](http://oaccframework.org) - 提供基于权限的授权服务。
- [OpenAM](https://github.com/OpenIdentityPlatform/OpenAM) - 访问管理解决方案，包括身份验证、SSO、授权、联合、权利和 Web 服务安全。
- [OTP-Java](https://github.com/BastiaanJansen/OTP-Java) - 符合 RFC 4226 (HOTP) 和 RFC 6238 (TOTP) 的一次性密码生成器库。
- [pac4j](https://github.com/pac4j/pac4j) - 安全引擎。
- [Passay](http://www.passay.org/) - 通过根据可配置的规则集验证候选密码来实施密码策略。
- [Password4j](https://github.com/Password4j/password4j) - 用户友好的加密库，支持 Argon2、Bcrypt、Scrypt、PBKDF2 和各种其他加密哈希函数。
- [SecurityBuilder](https://github.com/tersesystems/securitybuilder) - 适用于 JCA 和 JSSE 类，尤其是 X.509 证书的 Fluent Builder API。
- [Themis](https://github.com/cossacklabs/themis) - 多平台高级加密库提供易于使用的加密来保护敏感数据：前向保密的安全消息传递、安全数据存储 (AES256GCM)；适合构建端到端加密应用程序。
- [Tink](https://github.com/google/tink) - 为常见加密任务提供简单且防误用的 API。
- [Topaz](https://www.topaz.sh) - 支持 RBAC、ABAC 和 ReBAC 的应用程序细粒度授权。
- [MOSS](https://central.sonatype.com/artifact/com.mosscomputing/moss-sdk) - 使用 ML-DSA-44 后量子签名对 AI 代理进行加密签名，创建归因和合规性审计跟踪。

### 序列化

_高效处理序列化的库._

- [FlatBuffers](https://github.com/google/flatbuffers) - 内存高效的序列化库，无需解包和解析即可访问序列化数据。
- [FST](https://github.com/RuedigerMoeller/fast-serialization) - 兼容 JDK 的高性能对象图序列化。
- [Fury](https://github.com/alipay/fury) - 由 JIT 和零拷贝支持的极快的对象图序列化框架。
- [Kryo](https://github.com/EsotericSoftware/kryo) - 快速高效的对象图序列化框架。
- [MessagePack](https://github.com/msgpack/msgpack-java) - 高效的二进制序列化格式。
- [PHP Serializer](https://github.com/marcospassos/java-php-serializer) - 以 PHP 序列化格式序列化对象。

### 服务器

_专门用于部署应用程序的服务器。_

- [Apache Tomcat](https://tomcat.apache.org) - 适用于 Servlet 和 JSP 的强大、全能服务器。
- [Apache TomEE](https://tomee.apache.org) - Tomcat 加 Java EE。
- [Jetty](https://www.eclipse.org/jetty/) - 提供 Web 服务器和 javax.servlet 容器，并支持 HTTP/2、WebSocket、OSGi、JMX、JNDI、JAAS 和许多其他集成。
- [nanohttpd](https://github.com/NanoHttpd/nanohttpd) - 微型、易于嵌入的 HTTP 服务器。
- [WildFly](https://www.wildfly.org) - 以前称为 JBoss，由 Red Hat 开发，具有广泛的 Java EE 支持。 （仅限 LGPL-2.1）

### 模板引擎

_替换模板中表达式的工具._

- [Freemarker](https://freemarker.apache.org) - 基于模板和更改数据生成文本输出（HTML 网页、电子邮件、配置文件、源代码等）的库。
- [Handlebars.java](https://jknack.github.io/handlebars.java/) - 无逻辑和语义胡子模板。
- [Jade4J](https://github.com/neuland/jade4j) - Pug（以前称为 Jade）的实现。
- [Jamal](https://github.com/verhas/jamal) - 嵌入到 Maven/JavaDoc 中的可扩展模板引擎，支持多种扩展（Groovy、Ruby、JavaScript、JShell、PlantUml），并支持片段处理。
- [jstachio](https://github.com/jstachio/jstachio) - Typesafe Mustache 模板引擎。
- [jte](https://github.com/casid/jte) - 编译为类，并使用简单的语法和多种功能，使开发更容易，并提供快速执行和较小的占用空间。
- [Jtwig](https://github.com/jtwig/jtwig) - 模块化、可配置且经过全面测试的模板引擎。
- [Pebble](https://pebbletemplates.io) - 受到 Twig 的启发，并以其继承功能和易于阅读的语法而与众不同。它带有内置的自动转义功能以确保安全，并且包括对国际化的集成支持。
- [Rocker](https://github.com/fizzed/rocker) - 经过优化、内存高效且快速的模板引擎，可生成静态类型的普通对象。
- [StringTemplate](https://github.com/antlr/stringtemplate4) - 用于生成源代码、网页、电子邮件或任何其他格式化文本输出的模板引擎。
- [Thymeleaf](https://www.thymeleaf.org) - 旨在替代 JSP，适用于 XML 文件。

### 测试

_从模型到视图进行测试的工具。_

#### 异步

_简化异步服务测试的工具。_

- [Awaitility](https://github.com/awaitility/awaitility) - 用于同步异步操作的DSL。
- [ConcurrentUnit](https://github.com/jhalterman/concurrentunit) - 用于测试多线程和异步应用程序的工具包。
- [GreenMail](https://greenmail-mail-test.github.io/greenmail/) - 用于集成测试的内存中电子邮件服务器。支持 SMTP、POP3 和 IMAP（包括 SSL）。 （仅限 GPL-2.0）
- [Hoverfly Java](https://github.com/SpectoLabs/hoverfly-java) - Hoverfly 的本机绑定，它是一个允许您模拟 HTTP 服务的代理。
- [Karate](https://github.com/intuit/karate) - DSL 结合了 API 测试自动化、模拟和性能测试，使测试 REST/HTTP 服务变得容易。
- [REST Assured](https://github.com/rest-assured/rest-assured) - 用于轻松测试 REST/HTTP 服务的 DSL。
- [WebTau](https://github.com/testingisdocumenting/webtau) - 使用一致的匹配器和概念集跨 REST-API、Graph QL、浏览器、数据库、CLI 和业务逻辑进行测试。

#### BDD

_测试源自 TDD 并深受 DDD 和 OOAD 影响的软件开发过程。_

- [Cucumber](https://github.com/cucumber/cucumber-jvm) - 提供一种以客户可以理解的简单语言描述功能的方法。
- [Cukes-REST](https://github.com/ctco/cukes) - 使用 Cucumber 进行 REST 服务测试的 Gherkin 步骤集合。
- [J8Spec](https://github.com/j8spec/j8spec) - 遵循类似 Jasmine 的语法。
- [JBehave](https://jbehave.org) - 描述故事的可广泛配置的框架。
- [JGiven](http://jgiven.org) - 提供流畅的 API，允许更简单的组合。
- [Kensa](https://github.com/kensa-dev/kensa) - 适用于 Java 和 Kotlin 的代码优先 BDD 框架，可从测试代码生成交互式 HTML 报告和序列图。
- [Lamdba Behave](https://github.com/RichardWarburton/lambda-behave) - 旨在提供一个流畅的 API，用读起来像简单英语的长描述性句子编写测试。
- [Serenity BDD](https://github.com/serenity-bdd/serenity-core) - 自动验收测试和报告库，可与 Cucumber、JBehave 和 JUnit 配合使用，使编写高质量的可执行规范变得更加容易。

#### 固定装置

_与随机数据的创建和处理相关的一切。_

- [AutoParams](https://github.com/AutoParams/AutoParams) - 支持生成测试数据或组合场景进行参数化测试。
- [Beanmother](https://github.com/keepcosmos/beanmother) - 从 YAML 装置设置 bean。
- [Datafaker](https://github.com/datafaker-net/datafaker) - 现代假数据生成器源自 Java Faker。
- [Fixture Factory](https://github.com/six2six/fixture-factory) - 从模板生成假对象。
- [jFairy](https://github.com/Devskiller/jfairy) - 假数据生成器。
- [Instancio](https://github.com/instancio/instancio) - 通过生成完全填充的、可重现的对象，自动执行单元测试中的数据设置。包括 JUnit 5 扩展。
- [Randomized Testing](https://github.com/randomizedtesting/randomizedtesting) - JUnit 测试运行程序和插件，用于以伪随机性运行 JUnit 测试。
- [Java Faker](https://github.com/DiUS/java-faker) - Ruby 假数据生成器的端口。
- [Mockneat](https://github.com/nomemory/mockneat) - 另一个假数据生成器。
- [JMock](https://github.com/xcancloud/JMock) - JMock是一个用Java实现的高性能数据生成和模拟组件库。

#### 框架

_提供环境来运行特定用例的测试。_

- [Apache JMeter](http://jmeter.apache.org) - 功能测试和性能测量。
- [JMeter DSL.java](https://abstracta.github.io/jmeter-java-dsl/) - 使用 JMeter 进行负载测试就像 JUnit 测试一样简单。
- [Arquillian](http://arquillian.org) - Java EE 容器的集成和功能测试平台。
- [BitDive ![c]](https://bitdive.io) - 零代码集成测试平台，可根据运行时应用程序行为生成测试。
- [cdi-test](https://github.com/guhilling/cdi-test) - JUnit 扩展可轻松高效地测试 CDI 组件。
- [Citrus](https://citrusframework.org) - 专注于客户端和服务器端消息传递的集成测试框架。
- [Gatling](https://gatling.io) - 负载测试工具专为易用性、可维护性和高性能而设计。
- [JUnit](https://junit.org/junit5/) - 通用测试框架。
- [jqwik](https://jqwik.net) - 基于 JUnit 5 构建的基于属性的测试引擎。
- [Pact JVM](https://github.com/DiUS/pact-jvm) - 消费者驱动的合同测试。
- [PIT](http://pitest.org) - 用于评估现有 JUnit 或 TestNG 测试套件的故障检测能力的快速突变测试框架。
- [weld-testing](https://github.com/weld/weld-testing) - 一组测试框架扩展（JUnit 4、JUnit 5、Spock），用于通过 Weld 增强 CDI 组件的测试。支持焊接 5。
- [selenium](https://github.com/SeleniumHQ/selenium) - 浏览器自动化框架和生态系统。

#### 匹配器

_提供自定义匹配器的库._

- [AssertJ](https://joel-costigliola.github.io/assertj/) - 流畅的断言可以提高可读性。
- [Hamcrest](http://hamcrest.org/JavaHamcrest/) - 可以组合匹配器来创建灵活的意图表达。
- [JSONAssert](http://jsonassert.skyscreamer.org) - 简化 JSON 字符串的测试。
- [JsonUnit](https://github.com/lukas-krecan/JsonUnit) - 简化测试中 JSON 比较的库。
- [Truth](https://truth.dev) - 谷歌流畅的断言和命题框架。
- [XMLUnit](https://github.com/xmlunit/xmlunit) - 简化 XML 输出的测试。

#### 杂项

_与测试相关的其他内容。_

- [ConsoleCaptor](https://github.com/Hakky54/console-captor) - 捕获控制台输出以进行单元测试。
- [junit-dataprovider](https://github.com/TNG/junit-dataprovider) - JUnit 的类似于 TestNG 的数据提供程序/运行程序。
- [junit-pioneer](https://junit-pioneer.org/) - JUnit 5 扩展包，推动 Jupiter 的发展。
- [LogCaptor](https://github.com/Hakky54/log-captor) - 捕获日志条目以进行单元测试。
- [log-capture](https://github.com/dm-drogeriemarkt/log-capture) - 捕获日志条目并为单元和集成测试提供断言。
- [Mutability Detector](https://github.com/MutabilityDetector/MutabilityDetector) - 报告给定类的实例是否是不可变的。
- [pojo-tester](https://www.pojo.pl) - 自动对基本 POJO 方法执行测试。 （仅限 LGPL-3.0）
- [raml-tester](https://github.com/nidi3/raml-tester) - 测试请求/响应是否与给定的 RAML 定义匹配。
- [Selfie](https://github.com/diffplug/selfie) - 快照测试（内联和磁盘上）。
- [skipper-java](https://github.com/get-skipper/skipper-java) - 通过 Google Spreadsheet 进行实时测试执行控制，无需更改代码即可实现即时切换。
- [Stebz](https://github.com/stebz/stebz) - 用于管理测试步骤的多方法框架。
- [Testcontainers](https://github.com/testcontainers/testcontainers-java) - 提供通用数据库、Selenium Web 浏览器或可以在 Docker 容器中运行的任何其他内容的一次性实例。
- [Java Evolved](https://javaevolved.github.io/) - 传统 Java 模式和现代 Java 模式的并排比较。

#### 嘲笑

_模拟协作者以帮助测试单个孤立单元的工具。_

- [JMockit](http://jmockit.github.io) - 集成测试、API 模拟和伪造以及代码覆盖率。
- [Mockito](https://github.com/mockito/mockito) - 模拟框架可让您使用干净、简单的 API 编写测试。
- [MockServer](https://www.mock-server.com) - 允许模拟与 HTTPS 集成的系统。
- [Moco](https://github.com/dreamhead/moco) - 用于存根和模拟的简洁 Web 服务。
- [PowerMock](https://github.com/powermock/powermock) - 模拟静态方法、构造函数、最终类和方法、私有方法以及静态初始值设定项的删除。
- [WireMock](http://wiremock.org) - 存根和模拟 Web 服务。
- [EasyMock](https://github.com/easymock/easymock) - EasyMock 是一个 Java 库，它提供了一种在单元测试中使用 Mock 对象的简单方法。

### 实用性

_提供通用实用函数的库._

- [Arthas](https://github.com/alibaba/arthas) - 允许在不修改代码或重新启动服务器的情况下解决应用程序的生产问题。
- [bucket4j](https://github.com/vladimir-bukhtoyarov/bucket4j) - 基于令牌桶算法的限速库。
- [cactoos](https://github.com/yegor256/cactoos) - 面向对象原语的集合。
- [Chocotea](https://github.com/cleopatra27/chocotea) - 从 java 代码生成 postman 集合、环境和集成测试。
- [CRaSH](http://www.crashub.org) - 为运行 CRaSH 的 JVM 提供 shell。由 Spring Boot 等使用。 （LGPL-2.1-或更高版本）
- [Dex](https://github.com/PatMartin/Dex) - Java/JavaFX工具能够提供强大的ETL和数据可视化功能。
- [dregex](https://github.com/marianobarrios/dregex) - 使用确定性有限自动机的正则表达式引擎。它支持一些 Perl 风格的功能，但保留了线性匹配时间，并且还提供集合操作。
- [Embulk](https://github.com/embulk/embulk) - 批量数据加载器，帮助在各种数据库、存储、文件格式和云服务之间传输数据。
- [fswatch](https://github.com/vorburger/ch.vorburger.fswatch) - 用于监视目录文件系统更改的微型库，简化了 java.nio.file.WatchService。
- [Gephi](https://github.com/gephi/gephi) - 用于可视化和操作大型图网络的跨平台。 （仅限 GPL-3.0）
- [Guava](https://github.com/google/guava) - 集合、缓存、原语支持、并发库、通用注释、字符串处理、I/O 等等。
- [JADE](https://jade.tilab.com) - 用于构建和调试多代理系统的框架和环境。 （仅限 LGPL-2.0）
- [Javadoc Publisher](https://github.com/MathieuSoysal/Javadoc-publisher.yml) - 从您的 maven/gradle 项目生成 Javadoc 并将其自动部署到 GitHub 页面上。
- [Java Diff Utils](https://java-diff-utils.github.io/java-diff-utils/) - 用于文本或数据比较和修补的实用程序。
- [java-util](https://github.com/jdereg/java-util) - 零依赖、高性能实用程序，具有 Converter（通用类型转换）、DeepEquals、CaseInsensitiveMap、TTLCache、CompactMap、MultiKeyMap 和对象图遍历。
- [JavaVerbalExpressions](https://github.com/VerbalExpressions/JavaVerbalExpressions) - 帮助构建困难的正则表达式的库。
- [Jctx](https://github.com/Shashwat-Gupta57/jctx) - 读取 Java 项目并生成结构化上下文文件，以便 AI 工具可以理解并帮助规划代码库。
- [JGit](https://www.eclipse.org/jgit/) - 实现 Git 版本控制系统的轻量级纯 Java 库。
- [JKScope](https://github.com/evpl/jkscope) - Java 作用域函数受到 Kotlin 的启发。
- [java-refined](https://github.com/JunggiKim/java-refined) - Java 8+ 的零依赖细化类型，具有涵盖数字、字符串和集合的类型安全包装器。
- [minio-java](https://github.com/minio/minio-java) - 提供简单的 API 来访问任何与 Amazon S3 兼容的对象存储服务器。
- [Protégé](https://protege.stanford.edu) - 提供本体编辑器和构建基于知识的系统的框架。
- [Semver4j](https://github.com/semver4j/semver4j) - 轻量级库可帮助您处理不同模式的语义版本控制。
- [Sift](https://github.com/Mirkoddd/Sift) - 类型安全、基于 AST 的 Regex Builder 专注于可读性和 ReDoS 预防。
- [Underscore-java](https://github.com/javadev/underscore-java) - Underscore.js 函数的端口。

### 版本管理器

_帮助创建开发 shell 环境并在不同 Java 版本之间切换的实用程序。_

- [jabba](https://github.com/shyiko/jabba) - Java 版本管理器受到 nvm 的启发。支持 macOS、Linux 和 Windows。
- [jenv](https://github.com/jenv/jenv) - Java 版本管理器受到 rbenv 的启发。可以全局配置或按项目配置。在 Debian 和 macOS 上测试。
- [SDKMan](https://github.com/sdkman/sdkman-cli) - Java 版本管理器受到 RVM 和 rbenv 的启发。支持基于 UNIX 的平台和 Windows。

### 网络爬行

_分析网站内容的库。_

- [Apache Nutch](https://nutch.apache.org) - 适用于生产环境的高度可扩展、高度可伸缩的网络爬虫。
- [Crawler4j](https://github.com/yasserg/crawler4j) - 简单、轻量级的网络爬虫。
- [jsoup](https://jsoup.org) - 抓取、解析、操作和清理 HTML。
- [StormCrawler](http://stormcrawler.net) - 用于构建低延迟且可扩展的网络爬虫的 SDK。
- [webmagic](https://github.com/code4craft/webmagic) - 可扩展的爬虫，具有下载、url 管理、内容提取和持久化功能。

### 网络框架

_处理 Web 应用程序各层之间通信的框架。_

- [ActiveJ](https://activej.io) - 从头开始构建的轻量级异步框架，用于开发高性能 Web 应用程序。
- [Apache Tapestry](https://tapestry.apache.org) - 面向组件的框架，用于创建动态、健壮、高度可扩展的 Web 应用程序。
- [Apache Wicket](https://wicket.apache.org) - 基于组件的 Web 应用程序框架类似于 Tapestry，具有状态 GUI。
- [Blade](https://github.com/lets-blade/blade) - 轻量级、模块化的框架，旨在优雅和简单。
- [Bootique](https://bootique.io) - 可运行应用程序的最小固执己见的框架。
- [Firefly](http://www.fireflysource.com) - 用于快速开发高性能 Web 应用程序的异步框架。
- [Javalin](https://javalin.io/) - Web 应用程序的微框架。
- [Jooby](http://www.jooby.org) - 可扩展、快速、模块化的微框架，提供多种编程模型。
- [Ninja](http://www.ninjaframework.org) - 全栈网络框架。
- [Pippo](http://www.pippo.ro) - 小型、高度模块化、类似 Sinatra 的框架。
- [Play](https://www.playframework.com) - 它基于 Akka 构建，为 Java 和 Scala 中的高度可扩展应用程序提供可预测且最小的资源消耗（CPU、内存、线程）。
- [PrimeFaces](https://www.primefaces.org) - JSF 框架具有免费和商业/支持版本以及前端组件。
- [Ratpack](https://ratpack.io) - 一组库，可促进快速、高效、可发展且经过良好测试的 HTTP 应用程序。
- [Takes](https://github.com/yegor256/takes) - 围绕真正的面向对象编程和不变性概念构建的固执己见的 Web 框架。
- [tinystruct](https://github.com/tinystruct/tinystruct) - 用于构建具有 CLI、HTTP 和模块化扩展支持的 Java 应用程序的轻量级可插拔框架。
- [Vaadin](https://vaadin.com) - 可简化 Web 应用程序开发的全栈开源 Java 框架。单独使用 Java 构建复杂的交互式应用程序，并使用 TypeScript 和 React 组件进行增强，无需深厚的 JavaScript、CSS 或 HTML 专业知识。
- [WebForms Core](https://github.com/webforms-core) - 一种从服务器管理 HTML 标签的技术。
- [Erupt](https://github.com/erupts/erupt) - 注解驱动的低代码和 JPA 可视化

### 工作流编排引擎

- [Cadence](https://cadenceworkflow.io) - Uber 的有状态代码平台。
- [flowable](https://github.com/flowable/flowable-engine) - 紧凑高效的工作流程和业务流程管理平台。
- [Temporal](https://temporal.io) - 微服务编排平台，源自 Cadence，但基于 gRPC。

## 资源

### 相关精彩列表

_与 Java 和 JVM 生态系统相关的精彩列表。_

- [很棒的注释处理](https://github.com/gunnarmorling/awesome-annotation-processing)
- [很棒的格拉尔](https://github.com/neomatrix369/awesome-graal)
- [很棒的 Gradle 插件](https://github.com/ksoichiro/awesome-gradle)
- [很棒的 Java 库和隐藏的宝石](https://libs.tech/java)
- [很棒的 J2ME](https://github.com/hstsethi/awesome-j2me)
- [AwesomeJavaFX](https://github.com/mhrimaz/AwesomeJavaFX)
- [很棒的 JVM](https://github.com/deephacks/awesome-jvm)
- [很棒的微服务](https://github.com/mfornos/awesome-microservices)
- [很棒的休息](https://github.com/marmelab/awesome-rest)
- [很棒的硒](https://github.com/christian-bromann/awesome-selenium)
- [令人敬畏的杂交](https://github.com/eminyagiz42/awesome-hybris)
- [ciandcd](https://github.com/ciandcd/awesome-ciandcd)
- [有用的 Java 链接](https://github.com/Vedenin/useful-java-links)
- [Java 并发检查表](https://github.com/code-review-checklists/java-concurrency)
- [Java 开发者路线图](https://github.com/s4kibs4mi/java-developer-roadmap)

### 社区

_积极讨论._

- [r/java](https://www.reddit.com/r/java/) - Java 社区的 Reddit 子版块。
- [Stack Overflow](https://stackoverflow.com/questions/tagged/java) - 问答平台。

### 前端

_为此列表提供前端的网站。请注意，不会有官方网站。我们不与特定网站关联，每个人都可以创建一个网站。_

- [java.libhunt.com](https://java.libhunt.com)

### 有影响力的书籍

_产生了巨大影响且仍然值得一读的书籍。_

- [核心 Java 第 I 卷——基础知识](https://www.amazon.com/Core-Java-I-Fundamentals-10th/dp/0134177304)
- [核心 Java，第二卷——高级特性](https://www.amazon.com/Core-Java-II-Advanced-Features-10th/dp/0134177290)
- [有效的Java（第三版）](https://www.amazon.com/Effective-Java-3rd-Joshua-Bloch/dp/0134685997)
- [Head First Java（第三版）](https://www.oreilly.com/library/view/head-first-java/9781492091646/)
- [Java 并发实践](https://www.amazon.com/Java-Concurrency-Practice-Brian-Goetz/dp/0321349601)
- [基础扎实的 Java 开发人员（第二版）](https://www.manning.com/books/the-well-grounded-java-developer-second-edition)
- [用Java思考](https://www.amazon.com/Thinking-Java-Edition-Bruce-Eckel/dp/0131872486)

### 播客和截屏视频

_编程时可以看或听的东西。_

- [140 Second Ducklings](https://twitter.com/debugagent/status/1491075324805001219) - Twitter 上的简短视频深入解释了 Java 调试。
- [一个丰富的播客](https://bootifulpodcast.fm)
- [富杰播客](https://foojay.io/today/category/podcast/)
- [Java 内部](https://inside.java/podcast)（官方）
- [Java 堆外](http://www.javaoffheap.com)
- [The Java Posse](http://www.javaposse.com) - 自 2015 年 2 月起停产。

### 人

#### 社交

_要关注的活跃帐户。来自他们社交的描述._

- [Adam Bien](https://twitter.com/AdamBien) - 自由作者、JavaOne Rockstar 演讲者、顾问、Java Champion。
- [Aleksey Shipilëv](https://twitter.com/shipilev) - 性能极客、基准测试沙皇、并发错误猎人。
- [Antonio Goncalves](https://twitter.com/agoncal) - Java Champion、JUG Leader、Devoxx France、Java EE 6/7、JCP、作者。
- [Arun Gupta](https://twitter.com/arungupta) - Java Champion、JavaOne Rockstar、JUG Leader、Devoxx4Kids-er、Couchbase 开发人员宣传副总裁。
- [Brian Goetz](https://bsky.app/profile/briangoetz.bsky.social) - Oracle 的 Java 语言架构师。
- [Bruno Borges](https://twitter.com/brunoborges) - Oracle 产品经理/Java Jock。
- [Chris Engelbert](https://twitter.com/noctarius2k) - TimescaleDB 的开源爱好者、演讲者、开发者、开发者倡导者。
- [Chris Richardson](https://bsky.app/profile/crichardson.bsky.social) - 软件架构师、顾问和连续创业者、Java Champion、JavaOne Rock Star、\*POJOs in Action- 作者。
- [Ed Burns](https://twitter.com/edburns) - Oracle 技术人员顾问成员。
- [Eugen Paraschiv](https://twitter.com/baeldung) - Spring Security 课程的作者。
- [Heinz Kabutz](https://twitter.com/heinzkabutz) - Java Champion，演讲者，The Java Specialists' Newsletter 的作者，并发性能专家。
- [Holly Cummins](https://twitter.com/holly_cummins) - IBM 伦敦 Bluemix Garage 的技术主管、Java Champion、开发人员、作者、JavaOne 明星。
- [James Weaver](https://twitter.com/JavaFXpert) - Java/JavaFX/IoT 开发人员、作者和演讲者。
- [Java](https://twitter.com/java) - 官方 Java Twitter 帐户。
- [Javin Paul](https://twitter.com/javinpaul) - 知名Java博主。
- [Josh Long](https://twitter.com/starbuxman) - Pivotal 的 Spring 倡导者，O'Reilly 的 Cloud Native Java 和 Building Microservices with Spring Boot、JavaOne Rock Star 的作者。
- [Lukas Eder](https://bsky.app/profile/lukaseder.bsky.social) - Java Champion、演讲者、Data Geekery (jOOQ) 创始人兼首席执行官。
- [Mani Sarkar](https://twitter.com/theNeomatrix369) - Java 冠军、多语言专家、参与@graalvm、AI/ML/DL、数据科学、开发者社区、演讲者和博主的软件工匠。像这样的几个很棒的列表的创建者。
- [Mario Fusco](https://twitter.com/mariofusco) - RedHatter，JUG 协调员、经常演讲者和作家。
- [Mark Heckler](https://twitter.com/MkHeck) - Pivotal 首席技术专家和开发者倡导者、会议发言人、出版作家和 Java 冠军，专注于物联网和云。
- [Markus Eisele](https://twitter.com/myfear) - Java EE 传播者，红帽。
- [Martijn Verburg](https://twitter.com/karianna) - London JUG 联合领导者、演讲者、作家、Java Champion 等等。
- [Martin Thompson](https://twitter.com/mjpt777) - 脸色苍白的表演黑帮。
- [Monica Beckwith](https://twitter.com/mon_beck) - 性能顾问，JavaOne 摇滚明星。
- [OpenJDK](https://twitter.com/OpenJDK) - 官方 OpenJDK 帐户。
- [Peter Lawrey](https://twitter.com/PeterLawrey) - Peter Lawrey，Java 性能专家。
- [Randy Shoup](https://twitter.com/randyshoup) - Stitch Fix 工程副总裁、演讲者、JavaOne Rock Star。
- [Reza Rahman](https://twitter.com/reza_rahman) - Java EE/GlassFish/WebLogic 传播者、作家、演讲者、开源黑客。
- [Sander Mak](https://twitter.com/Sander_Mak) - Java Champion，作者。
- [Simon Maple](https://twitter.com/sjmaple) - Java Champion、VirtualJUG 创始人、LJC 领导者、RebelLabs 作者。
- [Spencer Gibb](https://twitter.com/spencerbgibb) - 软件工程师、爸爸、极客、Spring Cloud Core @pivotal 的联合创始人和负责人。
- [Stephen Colebourne](https://bsky.app/profile/jodastephen.bsky.social) - Java 冠军、演讲者。
- [Trisha Gee](https://twitter.com/trisha_gee) - Java 冠军和演讲者。
- [Venkat Subramaniam](https://twitter.com/venkat_s) - 作者、休斯顿大学教授、Microsoft MVP 奖获得者、JavaOne 摇滚明星、Java 冠军。
- [Vlad Mihalcea](https://twitter.com/vlad_mihalcea) - Java Champion 致力于 Hypersistence Optimizer，数据库爱好者，《High-Performance Java Persistence》一书的作者。

### 网站

_要阅读的网站._

- [Baeldung](https://www.baeldung.com)
- [Dzone](https://dzone.com)
- [foojay.io](https://foojay.io)
- [谷歌Java风格](https://google.github.io/styleguide/javaguide.html)
- [InfoQ](https://www.infoq.com)
- [Java 算法和客户端](https://algs4.cs.princeton.edu/code)
- [Java、SQL 和 jOOQ](https://blog.jooq.org)
- [Java.net](https://community.oracle.com/community/java)
- [Javalobby](https://dzone.com/java-jdk-development-tutorials-tools-news)
- [TheCodeForge Java 教程](https://thecodeforge.io/java/)
- [JavaWorld](https://www.javaworld.com)
- [JAXenter](https://jaxenter.com)
- [RebelLabs](https://zeroturnaround.com/rebellabs)
- [OverOps 博客](https://blog.overops.com)
- [TheServerSide.com](http://www.theserverside.com)
- [香草爪哇](https://vanilla-java.github.io)
- [Voxxed](https://www.voxxed.com)
- [爪哇周刊](https://discu.eu/weekly/java/)

## 贡献

非常欢迎您的贡献！

请查看[贡献](https://github.com/akullpp/awesome-java/blob/master/CONTRIBUTING.md)指南和[验证工具](https://github.com/akullpp/awesome-java-lint)。

[c]：https://cdn.rawgit.com/akullpp/23246ca832bda82bb505230bf3538e2a/raw/d9bcdb769bf025292f9c6bc1290f01f1fcd1f864/commercial.svg
