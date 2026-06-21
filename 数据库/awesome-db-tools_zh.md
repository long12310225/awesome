# 很棒的数据库工具 [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> 社区驱动的数据库工具列表

在这里，我们将收集有关非常有用和很棒的实验工具的信息，这些工具可以简化 DBA、DevOps、开发人员和普通人的数据库工作。

请随意添加有关您自己的数据库工具或您最喜欢的第三方数据库工具的信息。

有关“awesome-db-tools”的更新以及有关数据库/工具/SQL 的想法/新闻请关注我 [@GraminMaksim](https://twitter.com/GraminMaksim)

## 内容
- [IDE](#ide)
- [GUI](#gui)
- [CLI](#cli)
- [Schema](#schema)
  - [Changes](#changes)
  - [代码生成](#code-generation)
  - [Diagrams](#diagrams)
  - [Documentations](#documentations)
  - [Design](#design)
  - [Samples](#samples)
- [API](#api)
- [应用平台](#application-platforms)
- [Backup](#backup)
- [Cloning](#cloning)
- [Monitoring/Statistics/Perfomance](#monitoringstatisticsperfomance)
  - [Prometheus](#prometheus)
  - [Zabbix](#zabbix)
- [Testing](#testing)
- [HA/Failover/Sharding](#hafailoversharding)
- [Kubernetes](#kubernetes)
- [配置调优](#configuration-tuning)
- [DevOps](#devops)
- [Reporting](#reporting)
- [Distributions](#distributions)
- [Security](#security)
- [SQL](#sql)
  - [Analyzers](#analyzers)
  - [代码生成器](#code-generators)
  - [Extensions](#extensions)
  - [Frameworks](#frameworks)
  - [Formatters](#formatters)
  - [Games](#games)
  - [Parsers](#parsers)
  - [超级SQL](#über-sql)
  - [语言服务器协议](#language-server-protocol)
  - [Learning](#learning)
  - [Plan](#plan)
  - [Scripts](#scripts)
- [Data](#data)
  - [Catalog](#catalog)
  - [Lineage](#lineage) 
  - [Generation/Masking/Subsetting](#generationmaskingsubsetting)
  - [数据分析器](#data-profilers)
  - [Replication](#replication) 
  - [Compare](#compare) 
- [Papers](#papers)
- [机器学习](#machine-learning)

## 集成开发环境
- [AnySQL Maestro](https://www.sqlmaestro.com/products/anysql/maestro) - 用于数据库管理、控制和开发的首要多功能管理工具。
- [Aqua Data Studio](https://www.aquafold.com/aquadatastudio) - 面向数据库开发人员、DBA 和分析师的生产力软件。
- [Coginiti Pro](https://www.coginiti.co/products/coginiti-pro/) - 面向分析师和分析工程师的现代 IDE，具有强大的脚本和网格功能。
- [Database .net](http://fishcodelib.com/Database.htm) - 多数据库管理工具，支持 20 多个数据库。
- [Database Workbench](https://www.upscene.com/database_workbench/) - 用于 Oracle、SQL Server、PostgreSQL、MySQL、MariaDB、Firebird、InterBase、SQLite 和 NexusDB 的数据库设计、开发和测试的完整 IDE。
- [DataGrip](https://www.jetbrains.com/datagrip) - JetBrains 的数据库和 SQL 跨平台 IDE。
- [DataStation](https://github.com/multiprocessio/datastation) - 轻松查询、编写脚本和可视化来自每个数据库、文件和 API 的数据。
- [DBeaver](https://github.com/dbeaver/dbeaver) - 免费的通用数据库管理器和 SQL 客户端。
- [dbForge Edge](https://www.devart.com/dbforge/edge/) - 用于 MySQL、MariaDB、SQL Server、Oracle、PostgreSQL 数据库和各种云服务的数据库开发、设计、管理和管理的多数据库解决方案。
- [dbForge Studio for MySQL](https://www.devart.com/dbforge/mysql/studio) - 用于 MySQL 和 MariaDB 数据库开发、管理和管理的通用 IDE。
- [dbForge Studio for Oracle](https://www.devart.com/dbforge/oracle/studio) - 用于 Oracle 管理、管理和开发的强大 IDE。
- [dbForge Studio for PostgreSQL](https://www.devart.com/dbforge/postgresql/studio) - 用于管理和开发数据库和对象的 GUI 工具。
- [dbForge Studio for SQL Server](https://www.devart.com/dbforge/sql/studio) - 用于 SQL Server 开发、管理、管理、数据分析和报告的强大集成开发环境。
- [DBHawk](https://www.datasparc.com/) - Datasparc 提供数据库安全、数据库管理、数据库治理和数据分析——全合一解决方案。
- [dbKoda](https://github.com/SouthbankSoftware/dbkoda) - Modern（JavaScript/Electron 框架），MongoDB 的开源 IDE。它具有支持 MongoDB 数据库的开发、管理和性能调整的功能。
- [IBExpert](http://www.ibexpert.net/ibe) - 适用于 Firebird 和 InterBase 的综合 GUI 工具。
- [HeidiSQL](https://github.com/HeidiSQL/HeidiSQL) - 用于管理 MySQL、MSSQL 和 PostgreSQL 的轻量级客户端，用 Delphi 编写。
- [Kangaroo](https://github.com/dbkangaroo/kangaroo) - 一款基于人工智能的 SQL 客户端和管理工具，适用于 Windows / macOS / Linux 上的流行数据库（SQLite / MySQL / PostgreSQL / 等），支持表设计、查询、模型、同步、导出/导入等，注重舒适、有趣和开发人员友好。
- [KeepTool](https://keeptool.com) - 面向 Oracle 数据库开发人员、管理员和高级应用程序用户的专业工具套件。
- [MySQL Workbench](https://www.mysql.com/products/workbench) - 面向数据库架构师、开发人员和 DBA 的统一可视化工具。
- [Navicat](https://www.navicat.com/en/products#navicat) - 一种数据库开发工具，允许您从单个应用程序同时连接到 MySQL、MariaDB、SQL Server、Oracle、PostgreSQL 和 SQLite 数据库。
- [Oracle SQL Developer](http://www.oracle.com/technetwork/developer-tools/sql-developer) - 免费的集成开发环境，可简化传统部署和云部署中 Oracle 数据库的开发和管理。
- [pgAdmin](https://www.pgadmin.org) - 世界上最先进的开源数据库 PostgreSQL 最受欢迎且功能丰富的开源管理和开发平台。
- [pgAdmin3](https://www.bigsql.org/pgadmin3) - 对 pgAdmin3 的长期支持。
- [PL/SQL Developer](https://www.allroundautomations.com/products/pl-sql-developer) - 专门针对 Oracle 数据库存储程序单元开发的 IDE。
- [PostgreSQL Maestro](https://www.sqlmaestro.com/products/postgresql/maestro) - 完整且强大的 PostgreSQL 数据库管理、管理和开发工具。
- [Querybook](https://github.com/pinterest/querybook) - Pinterest 开源大数据查询 UI，结合了并置表元数据和简单的笔记本 IDE 界面。
- [Slashbase](https://github.com/slashbaseide/slashbase) - 适用于您的数据库的开源协作 IDE。直接从浏览器连接到您的数据库、浏览数据、运行一堆 SQL 命令或与您的团队共享 SQL 查询。
- [Sql Server Management Studio](https://docs.microsoft.com/en-us/sql/ssms/sql-server-management-studio-ssms) - 用于管理 SQL Server 和 Azure SQL 数据库的任何 SQL 基础架构的集成环境。
- [Toad](https://www.quest.com/toad/) - 面向开发人员、管理员和数据分析师的首要数据库解决方案。使用单一数据库管理工具管理复杂的数据库更改。
- [Toad Edge](https://www.toadworld.com/products/toad-edge) - 适用于 MySQL 和 PostgreSQL 的简化数据库开发工具。
- [TOra](https://github.com/tora-tool/tora) - 适用于 Oracle、MySQL 和 PostgreSQL 数据库的开源 SQL IDE。
- [Valentina Studio](https://www.valentina-db.com/en/valentina-studio-overview) - 免费创建、管理、查询和探索 Valentina DB、MySQL、MariaDB、PostgreSQL 和 SQLite 数据库。
- [WebDB](https://webdb.app) - 免费高效的数据库 IDE。具有服务器发现、ERD、数据生成器、AI、NoSQL 结构管理器、数据库版本控制等功能。


## 图形用户界面
- [Adminer](https://github.com/vrana/adminer) - 在单个 PHP 文件中进行数据库管理。
- [Another Redis Desktop Manager](https://github.com/qishibo/AnotherRedisDesktopManager) - 免费开源 Redis 管理器。适用于 Mac、Linux、Windows、Homebrew、Snap、winget 等。
- [Antares SQL](https://github.com/antares-sql/antares) - 一个现代、快速、生产力驱动的 SQL 客户端，重点关注用户体验。适用于 Mac、Linux 和 Windows。
- [Azure Data Studio](https://github.com/microsoft/azuredatastudio) - 一种数据管理工具，支持在 Windows、macOS 和 Linux 上使用 SQL Server、PostgreSQL、Azure SQL DB 和 SQL DW。
- [Beekeeper Studio](https://github.com/beekeeper-studio/beekeeper-studio) - 开源 SQL 编辑器和数据库管理器，并在其使命声明中做出了隐私承诺。
- [Clidey WhoDB](https://github.com/clidey/whodb) - 一款轻量级数据库浏览器，具有适用于所有 SQL、NoSQL、缓存和队列的下一代用户体验。
- [DbGate](https://github.com/dbgate/dbgate) - MySQL、PostgreSQL、SQL Server、MongoDB、SQLite 等数据库管理器。在 Windows、Linux、Mac 下运行或作为 Web 应用程序运行。
- [DB Lens](https://github.com/dblens/app) - 开源 PostgreSQL GUI - 自动 ER 图、内部数据库洞察、磁盘利用率、性能指标、索引使用情况、顺序扫描计数等。
- [DbVisualizer](https://www.dbvis.com) - 面向开发人员、DBA 和分析师的通用数据库工具。
- [JackDB](https://www.jackdb.com) - 直接 SQL 访问所有数据，无论数据位于何处。
- [Jailer](https://github.com/Wisser/Jailer) - 数据库子集和关系数据浏览工具/客户端。
- [Malewicz](https://github.com/mgramin/malewicz) - 另一个用于数据库模式探索和性能分析的 WEB 客户端，但最初是专门为黑客攻击和扩展而创建的。
- [MissionKontrol](https://www.missionkontrol.io) - 现代拖放管理面板/客户端，为非技术用户提供完整的用户权限。
- [ocelotgui](https://github.com/ocelot-inc/ocelotgui) - 适用于 MySQL、MariaDB 和 Tarantool。为 Linux 开发，但可以在 Windows 上运行。
- [OmniDB](https://github.com/OmniDB/OmniDB) - 用于数据库管理的 Web 工具。
- [Pgweb](https://github.com/sosedoff/pgweb) - 基于 Web 的 PostgreSQL 数据库浏览器，用 Go 编写，可在 macOS、Linux 和 Windows 计算机上运行。
- [phpLiteAdmin](https://www.phpliteadmin.org) - 用 PHP 编写的基于 Web 的 SQLite 数据库管理工具，支持 SQLite3 和 SQLite2。
- [phpMyAdmin](https://github.com/phpmyadmin/phpmyadmin) - MySQL 和 MariaDB 的 Web 界面。
- [psequel](http://www.psequel.com) - 提供干净简单的界面，供您快速执行常见的 PostgreSQL 任务。
- [PopSQL](https://popsql.com) - 适合您团队的现代协作 SQL 编辑器。
- [Postico](https://eggerapps.at/postico) - 适用于 Mac 的现代 PostgreSQL 客户端。
- [Robo 3T](https://github.com/Studio3T/robomongo) - 以 Shell 为中心的跨平台 MongoDB 管理工具。
- [Sequel Ace](https://github.com/Sequel-Ace/Sequel-Ace) - 适用于 macOS 的 MySQL/MariaDB 数据库管理。
- [Sequel Pro](https://github.com/sequelpro/sequelpro) - 快速、易于使用的 Mac 数据库管理应用程序，用于处理 MySQL 和 MariaDB 数据库。
- [SQLite Expert](http://www.sqliteexpert.com/index.html) - 图形界面支持所有 SQLite 功能。
- [sqlite-tui](https://github.com/mathaou/sqlite-tui) - 用于查看 SQLite 数据库的 TUI，用 Go 编写。
- [sqlpad](https://github.com/rickbergfalk/sqlpad) - 基于 Web 的 SQL 编辑器在您自己的私有云中运行。
- [SQLPro](https://www.macpostgresclient.com) - 适用于 macOS 的简单而强大的 PostgreSQL 管理器。
- [SQuirreL](https://sourceforge.net/projects/squirrel-sql) - 用 Java 编写的图形 SQL 客户端，允许您查看 JDBC 兼容数据库的结构、浏览表中的数据、发出 SQL 命令等。
- [SQLTools](https://github.com/mtxr/vscode-sqltools) - VSCode 的数据库管理。
- [SQLyog](https://www.webyog.com/product/sqlyog) - 最完整且易于使用的 MySQL GUI。
- [Tabix](https://github.com/tabixio/tabix) - SQL 编辑器和 Clickhouse 的开源简单商业智能。
- [TablePlus](https://github.com/TablePlus/TablePlus) - 适用于关系数据库的现代、原生且友好的 GUI 工具：MySQL、PostgreSQL、SQLite 等。
- [TeamPostgreSQL](http://www.teampostgresql.com) - PostgreSQL Web 管理 GUI - 通过丰富、快速的 AJAX Web 界面，随时随地使用 PostgreSQL 数据库。
- [Query.me](https://query.me) - Notebook 格式的协作 SQL 编辑器。让您使用 JINJA 引用查询结果、可视化数据并计划运行和导出。


## 命令行界面
- [ipython-sql](https://github.com/catherinedevlin/ipython-sql) - 连接到数据库以在 IPython 或 IPython Notebook 中发出 SQL 命令。
- [iredis](https://github.com/laixintao/iredis) - 具有自动完成和语法突出显示功能的 Redis CLI。
- [pgcenter](https://github.com/lesovsky/pgcenter) - 类似 Top 的 PostgreSQL 管理工具。
- [pg_activity](https://github.com/julmon/pg_activity) - 用于 PostgreSQL 服务器活动监控的顶级应用程序。
- [pg_top](https://github.com/markwkm/pg_top) - PostgreSQL 的顶级。
- [pspg](https://github.com/okbob/pspg) - PostgreSQL 寻呼机。
- [diesel-guard](https://github.com/ayarotsky/diesel-guard) - 针对危险的 PostgreSQL 迁移模式的 Linter。它与 PostgreSQL SQL 文件无缝协作，并与使用 Diesel 和 SQLx 的项目本地集成。
- [SQLcl](http://www.oracle.com/technetwork/developer-tools/sqlcl/overview/index.html) - Oracle SQL Developer 命令行 (SQLcl) 是 Oracle 数据库的免费命令行界面。
- [sqlite-utils](https://github.com/simonw/sqlite-utils) - 用于操作 SQLite 数据库文件的 CLI 工具 - 插入数据、运行查询、创建索引、配置全文搜索等。
- [SQLLine](https://github.com/julianhyde/sqlline) - 用于通过 JDBC 向关系数据库发出 SQL 的命令行 shell。
- [usql](https://github.com/xo/usql) - 适用于 PostgreSQL、MySQL、Oracle 数据库、SQLite3、Microsoft SQL Server 和许多其他数据库（包括 NoSQL 和非关系数据库）的通用命令行界面！

### 数据库管理工具
- [athenacli](https://github.com/dbcli/athenacli) - 适用于 AWS Athena 服务的 CLI 工具，可以自动完成和语法突出显示。
- [litecli](https://github.com/dbcli/litecli) - 用于 SQLite 数据库的 CLI，具有自动完成和语法突出显示功能。
- [mssql-cli](https://github.com/dbcli/mssql-cli) - 具有自动完成和语法突出显示功能的 SQL Server 命令行客户端。
- [mycli](https://github.com/dbcli/mycli) - 具有自动完成和语法突出显示功能的 MySQL 终端客户端。
- [pgcli](https://github.com/dbcli/pgcli) - 具有自动完成和语法突出显示功能的 PostgreSQL CLI。
- [vcli](https://github.com/dbcli/vcli) - Vertica CLI 具有自动完成和语法突出显示功能。


## 模式

### 变化
- [2bass](https://github.com/CourseOrchestra/2bass) - 数据库配置即代码工具，利用幂等 DDL 脚本的概念。
- [Atlas](https://github.com/ariga/atlas) - 检查并将更改应用到数据库架构。
- [Bytebase](https://github.com/bytebase/bytebase) - 面向团队的基于 Web、零配置、无依赖性的数据库架构更改和版本控制工具。
- [flyway](https://github.com/flyway/flyway) - 数据库迁移工具。
- [gh-ost](https://github.com/github/gh-ost) - MySQL 的在线架构迁移。
- [liquibase](https://github.com/liquibase/liquibase) - 独立于数据库的库，用于跟踪、管理和应用数据库模式更改。
- [migra](https://github.com/djrobstep/migra) - 与 diff 类似，但适用于 PostgreSQL 模式。
- [node-pg-migrate](https://github.com/salsita/node-pg-migrate) - 专为 PostgreSQL 构建的 Node.js 数据库迁移管理。 （但也可以用于符合 SQL 标准的其他数据库 - 例如 CockroachDB。）
- [pg-osc](https://github.com/shayonj/pg-osc) - 用于在 PostgreSQL 中进行零停机架构更改和回填的简单 CLI 工具。
- [Prisma Migrate](https://github.com/prisma/migrate) - 声明性数据库架构迁移工具，使用声明性数据建模语法来描述数据库架构。
- [Pyrseas](https://github.com/perseas/Pyrseas) - 提供将 PostgreSQL 数据库架构描述为 YAML 的实用程序。
- [Reshape](https://github.com/fabianlindfors/reshape) - 一个易于使用、零停机的 Postgres 架构迁移工具。
- [SchemaHero](https://github.com/schemahero/schemahero) - 用于声明性数据库模式管理的 Kubernetes 运算符（用于数据库模式的 gitops）。
- [Skeema](https://github.com/skeema/skeema) - 适用于 MySQL 和 MariaDB 的声明式纯 SQL 模式管理系统，支持分片和外部在线模式更改工具。
- [Sqitch](https://github.com/sqitchers/sqitch) - 明智的数据库本机变更管理，用于无框架开发和可靠部署。
- [sqldef](https://github.com/k0kubun/sqldef) - MySQL、PostgreSQL 等的幂等模式管理。
- [yuniql](https://github.com/rdagumampan/yuniql) - 另一个架构版本控制和迁移工具刚刚使用本机 .NET Core 3.0+ 制作，希望更好。

### 代码生成
- [ddl-generator](https://github.com/catherinedevlin/ddl-generator) - 从表数据推断 SQL DDL（数据定义语言）。
- [scheme2ddl](https://github.com/qwazer/scheme2ddl) - 用于将 Oracle 模式导出到一组 ddl 初始化脚本的命令行实用程序，能够过滤不需要的信息、在不同文件中分离 DDL、漂亮的格式输出。

### 图表
- [Azimutt](https://github.com/azimuttapp/azimutt) - 实体关系图 (ERD) 可视化工具，具有各种过滤器和输入，可帮助您了解数据库架构。
- [ChartDB](https://github.com/chartdb/chartdb) - 免费开源数据库图表编辑器，通过单个查询可视化和设计您的数据库。
- [DrawDB](https://github.com/drawdb-io/drawdb) - 免费、简单、直观的在线数据库设计工具和 SQL 生成器。
- [DrawSQL](https://drawsql.app) - 在线数据库架构图编辑器，具有 SQL 导入、AI 生成和实时团队协作功能。
- [ERAlchemy](https://github.com/Alexis-benoist/eralchemy) - 实体关系图生成工具。
- [ERD Lab](https://www.erdlab.io/) - 为开发人员打造的免费基于云的实体关系图 (ERD) 工具。
- [Liam ERD](https://github.com/liam-hq/liam) - 开源工具，可从数据库和 ORM 生成美观且易于阅读的实体关系图。
- [QuickDBD](https://www.quickdatabasediagrams.com/) - 简单的在线工具，可快速绘制数据库图表。

### 文档
- [dbdocs](https://dbdocs.io/) - 使用 DSL 代码创建基于 Web 的数据库文档。
- [DBML](https://github.com/holistics/dbml) - 数据库标记语言，旨在定义和记录数据库结构。
- [SchemaCrawler](https://github.com/schemacrawler/SchemaCrawler) - 一个免费的数据库模式发现和理解工具。
- [Schema Spy](https://github.com/schemaspy/schemaspy) - 将数据库生成为 HTML 文档，包括实体关系图。
- [tbls](https://github.com/k1LoW/tbls) - 用于记录数据库的 CI 友好工具，用 Go 编写。

### 设计
- [Database Design](https://github.com/alextanhongpin/database-design) - 设计强大的数据库模式的有用技巧。
- [DBDiagram](https://dbdiagram.io) - 一个免费、简单的工具，只需编写代码即可绘制 ER 图。
- [DbSchema](https://dbschema.com/) - 通用数据库设计器，用于开箱即用的模式管理、模式文档、团队设计以及在多个数据库上的部署。 DbSchema 提供用于编写​​和执行查询、探索数据、生成数据和构建报告的工具。
- [ERBuilder Data Modeler](https://soft-builder.com/erbuilder-data-modeler) - 易于使用的数据库建模软件，用于高质量的数据模型。它是面向数据建模者和数据架构师的完整数据建模解决方案。
- [Moon Modeler](https://www.datensen.com) - 适用于 noSQL 和关系数据库的数据建模工具。适用于 Windows、Linux 和 macOS。
- [Navicat Data Modeler](https://www.navicat.com/en/products/navicat-data-modeler) - 一款功能强大且经济高效的数据库设计工具，可帮助您构建高质量的概念、逻辑和物理数据模型。
- [Oracle SQL Developer Data Modeler](http://www.oracle.com/technetwork/developer-tools/datamodeler/overview/index.html) - 免费的图形工具，可提高生产力并简化数据建模任务。
- [pgmodeler](https://github.com/pgmodeler/pgmodeler) - 专为 PostgreSQL 设计的数据建模工具。
- [WWW SQL Designer](https://github.com/ondras/wwwsqldesigner) - 在线 SQL 图表工具。

### 样品
- [Oracle Database Sample Schemas](https://github.com/oracle/db-sample-schemas) - Oracle 数据库的示例架构。


## 应用程序编程接口
为您的数据构建 API
- [Datasette](https://github.com/simonw/datasette) - 用于探索和发布数据的工具。
- [DreamFactory](https://github.com/dreamfactorysoftware/dreamfactory) - 适用于移动、Web 和 IoT 应用程序的开源 REST API 后端。
- [Graphweaver](https://github.com/exogee-technology/graphweaver) - 将多个数据源转换为单个 GraphQL API。
- [Hasura GraphQL Engine](https://github.com/hasura/graphql-engine) - PostgreSQL 上超快、即时的实时 GraphQL API 具有细粒度的访问控制，还可触发数据库事件的 Webhook。
- [JdbcREST](https://github.com/synthesized-io/jdbcrest/) - 适用于任何 JDBC 支持的数据库的 REST API，用 Java 编写的 PostgREST 克隆。
- [Oracle REST Data Services](http://www.oracle.com/technetwork/developer-tools/rest-data-services) - ORDS 是一个中间层 Java 应用程序，将 HTTP(S) 动词（GET、POST、PUT、DELETE 等）映射到数据库事务，并返回使用 JSON 格式化的任何结果。
- [Prisma](https://github.com/prismagraphql/prisma) - 将您的数据库转变为实时 GraphQL API。
- [PostGraphile](https://github.com/graphile/postgraphile) - 通过将 PostGraphile 指向现有 PostgreSQL 数据库，立即启动 GraphQL API 服务器。
- [PostgREST](https://github.com/PostgREST/postgrest) - 适用于任何 PostgreSQL 数据库的 REST API。
- [prest](https://github.com/prest/prest) - 是一种从任何用 Go 编写的数据库提供 RESTful API 的方法。
- [Remult](https://github.com/remult/remult) - 通过 REST API 为您的数据库提供端到端类型安全的 CRUD，并具有细粒度的访问控制。
- [restSQL](https://github.com/restsql/restsql) - 具有 Java 和 HTTP API 的 SQL 生成器，使用带有 XML 或 JSON 序列化的简单 RESTful HTTP API。
- [resquel](https://github.com/formio/resquel) - 轻松将 SQL 数据库转换为 REST API。
- [sandman2](https://github.com/jeffknupp/sandman2) - 自动为您的旧数据库生成 RESTful API 服务。
- [soul](https://github.com/thevahidal/soul) - 自动 SQLite RESTful 和实时 API 服务器。
- [VulcanSQL](https://github.com/Canner/vulcan-sql) - 编写模板化 SQL 以自动从数据库/数据仓库/数据湖公开 RESTful API。

## 应用平台
用于构建应用程序的低代码和无代码平台
- [Appsmith](https://github.com/appsmithorg/appsmith) - 强大的开源低代码框架，可以非常快速地构建内部应用程序。
- [Budibase](https://github.com/Budibase/budibase) - 用于在几分钟内创建内部应用程序的低代码平台。
- [ILLA Cloud](https://github.com/illacloud/illa-builder) - 低代码内部工具构建平台。
- [Nhost](https://github.com/nhost/nhost) - GraphQL 的开源 Firebase 替代方案。
- [Saltcorn](https://github.com/saltcorn/saltcorn) - 用于 Web 数据库应用程序的开源无代码构建器。服务器和拖放式 UI 构建器，数据存储在 PostgreSQL 或 SQLite 中。
- [SQLPage](https://github.com/sqlpage/SQLPage) - 快速的纯 SQL 数据应用程序构建器。在 SQL 查询之上自动构建 UI。
- [Tooljet](https://github.com/ToolJet/ToolJet) - 用于构建内部工具的开源低代码平台。


## 备份
- [BaRMan](https://github.com/2ndquadrant-it/barman) - PostgreSQL 的备份和恢复管理器。
- [Databasus](https://github.com/databasus/databasus) - 通过 Web UI 进行预定 PostgreSQL 备份的工具，具有外部存储（本地、S3、FTP、Google Drive 等）、通知（webhook、Discord、Slack 等）和团队管理。
- [pgbackrest](https://github.com/pgbackrest/pgbackrest) - 可靠的 PostgreSQL 备份和恢复。
- [pgcopydb](https://github.com/dimitri/pgcopydb) - 将 PostgreSQL 数据库复制到目标 PostgreSQL 服务器（pg_dump | pg_restore on steroids）。
- [pg_probackup](https://github.com/postgrespro/pg_probackup) - PostgreSQL 的备份和恢复管理器。
- [Portabase](https://github.com/Portabase/portabase) - 基于代理的 PostgreSQL 备份和恢复平台，具有分散执行和集中编排功能。

## 克隆
- [Database Lab Engine](https://gitlab.com/postgres-ai/database-lab) - PostgreSQL 的即时精简克隆可扩展开发流程。
- [clone_schema](https://github.com/denishpatel/pg-clone-schema) - PostgreSQL 克隆模式实用程序，无需离开数据库。
- [Spawn](https://spawn.cc/) - 用于创建用于开发和 CI 的即时数据库副本的云服务。不再需要本地数据库安装、即时恢复到任意保存点、每个功能分支或测试的独立副本。无论数据库大小如何，即时配置。


## 监控/统计/性能
- [ASH Viewer](https://github.com/akardapolov/ASH-Viewer) - 提供 Oracle 和 PostgreSQL 数据库中活动会话历史数据的图形视图。
- [Metis](https://www.metisdata.io/product/troubleshooting) - 为 SQL 数据库提供可观察性和性能调优。
- [Monyog](https://www.webyog.com/product/monyog) - 无代理且经济高效的 MySQL 监控工具。
- [mssql-monitoring](https://github.com/microsoft/mssql-monitoring) - 使用collectd、InfluxDB 和 Grafana 监控 Linux 上的 SQL Server 性能。
- [Navicat Monitor](https://www.navicat.com/en/products/navicat-monitor) - 一个安全、简单、无代理的远程服务器监控工具，具有强大的功能，使您的监控尽可能有效。
- [Percona Monitoring and Management](https://github.com/percona/pmm) - 用于管理和监控 MySQL 和 MongoDB 性能的开源平台。
- [pganalyze collector](https://github.com/pganalyze/collector) - Pganalyze 统计收集器，用于收集 PostgreSQL 指标和日志数据。
- [pgbadger](https://github.com/dalibo/pgbadger) - 快速 PostgreSQL 日志分析器。
- [pgDash](https://pgdash.io) - 测量和跟踪 PostgreSQL 数据库的各个方面。
- [PgHero](https://github.com/ankane/pghero) - PostgreSQL 的性能仪表板 - 运行状况检查、建议的索引等。
- [pgmetrics](https://github.com/rapidloop/pgmetrics) - 从正在运行的 PostgreSQL 服务器收集并显示信息和统计信息。
- [pgMonitor](https://github.com/CrunchyData/pgmonitor) - 一款一体化工具，可轻松创建一个环境来可视化 PostgreSQL 集群的运行状况和性能。
- [pgMustard](https://www.pgmustard.com) - PostgreSQL 的用户界面解释计划，以及提高性能的提示。
- [pgstats](https://github.com/gleu/pgstats) - 收集 PostgreSQL 统计信息，并将其保存在 CSV 文件中或在标准输出上打印。
- [pgwatch2](https://github.com/cybertec-postgresql/pgwatch2) - 灵活的独立 PostgreSQL 指标监控/仪表板解决方案。
- [PostgreSQL Metrics](https://github.com/spotify/postgresql-metrics) - 用于提取 PostgreSQL 数据库并提供指标的服务。
- [PostgreSQL Monitor](https://postgresmonitor.com) - 易于使用的 PostgreSQL 监控服务，提供警报、仪表板、查询统计信息和动态建议。
- [postgres-checkup](https://gitlab.com/postgres-ai/postgres-checkup) - 新一代诊断工具，允许用户对 PostgreSQL 数据库的健康状况进行深入分析。
- [Promscale](https://github.com/timescale/promscale) - 由 SQL 支持的指标和跟踪的开源可观察性后端。
- [Releem](https://releem.com) - 适用于 MySQL 和 MariaDB 的性能监控和优化工具，针对配置错误、查询缓慢、架构问题和死锁提供可操作的见解和安全自动化，从而大规模减少手动工作。
- [Telegraf PostgreSQL plugin](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/postgresql) - 提供 PostgreSQL 数据库的指标。

### 普罗米修斯
- [pgSCV](https://github.com/weaponry/pgscv) - PostgreSQL 和 PostgreSQL 相关服务的指标导出器。
- [postgres_exporter](https://github.com/wrouesnel/postgres_exporter) - 用于 PostgreSQL 服务器指标的 Prometheus 导出器。
- [pg_exporter](https://github.com/Vonng/pg_exporter) - 适用于 PostgreSQL 和 Pgbouncer 的完全可定制的 Prometheus 导出器，具有细粒度的执行控制。

### 扎比克斯
- [Mamonsu](https://github.com/postgrespro/mamonsu) - PostgreSQL 的监控代理。
- [Orabbix](http://www.smartmarmot.com/wiki/index.php?title=Orabbix) - 该插件旨在与 Zabbix Enterprise Monitor 配合使用，为 Oracle 数据库提供多层监控、性能和可用性报告和测量以及服务器性能指标。
- [pg_monz](https://github.com/pg-monz/pg_monz) - 这是 PostgreSQL 数据库的 Zabbix 监控模板。
- [Pyora](https://github.com/bicofino/Pyora) - 用于监控 Oracle 数据库的 Python 脚本。
- [ZabbixDBA](https://github.com/anetrusov/ZabbixDBA) - 快速、灵活且持续开发的插件来监控您的 RDBMS。


## 测试
- [DbFit](https://github.com/dbfit/dbfit) - 一个数据库测试框架，支持对数据库代码进行轻松的测试驱动开发。
- [pgTAP](https://github.com/theory/pgtap) - PostgreSQL 的单元测试。
- [RegreSQL](https://github.com/dimitri/regresql) - 回归测试您的 SQL 查询。
- [SQLancer](https://github.com/sqlancer/sqlancer) - 自动测试 DBMS 以发现其实现中的逻辑错误。


## HA/故障转移/分片
- [Citus](https://github.com/citusdata/citus) - PostgreSQL 扩展，可跨多个节点分发数据和查询。
- [patroni](https://github.com/zalando/patroni) - 使用 ZooKeeper、etcd 或 Consul 实现 PostgreSQL 高可用性的模板。
- [Percona XtraDB Cluster](https://github.com/percona/percona-xtradb-cluster) - MySQL 集群和高可用性的高可扩展性解决方案。
- [ShardingSphere](https://github.com/apache/shardingsphere) - 分布式 SQL 事务和查询引擎，可在任何数据库上进行数据分片、扩展、加密等。
- [stolon](https://github.com/sorintlab/stolon) - 用于 PostgreSQL 高可用性的云原生 PostgreSQL 管理器。
- [pg_auto_failover](https://github.com/citusdata/pg_auto_failover) - 用于自动故障转移和高可用性的 PostgreSQL 扩展和服务。
- [pglookout](https://github.com/aiven/pglookout) - PostgreSQL 复制监控和故障转移守护进程。
- [pgslice](https://github.com/ankane/pgslice) - PostgreSQL 分区就像馅饼一样简单。
- [PostgreSQL Automatic Failover](https://github.com/ClusterLabs/PAF) - PostgreSQL 的高可用性，基于行业参考 Pacemaker 和 Corosync。
- [autobase](https://github.com/vitabaks/autobase) - 开源 DBaaS，可自动部署和管理高度可用的 PostgreSQL 集群。
- [Vitess](https://github.com/vitessio/vitess) - 通过通用分片实现 MySQL 水平扩展的数据库集群系统。


## 库伯内斯
- [KubeDB](https://kubedb.com) - 使在 Kubernetes 上运行生产级数据库变得容易。
- [PostgreSQL operator](https://github.com/zalando/postgres-operator) - PostgreSQL Operator 可在由 Patroni 提供支持的 Kubernetes (Kubernetes) 上实现高可用的 PostgreSQL 集群。
- [Spilo](https://github.com/zalando/spilo) - 使用 Docker 实现高可用性 PostgreSQL 集群。
- [StackGres](https://gitlab.com/ongresinc/stackgres) - Kubernetes 上的企业级全栈 PostgreSQL。


## 配置调优
- [MySQLTuner-perl](https://github.com/major/MySQLTuner-perl) - 用 Perl 编写的脚本允许您快速检查 MySQL 安装并进行调整以提高性能和稳定性。
- [PGConfigurator](https://pgconfigurator.cybertec-postgresql.com) - 用于生成优化的“postgresql.conf”的免费在线工具。
- [pgtune](https://github.com/gregs1104/pgtune) - PostgreSQL 配置向导。
- [postgresqltuner.pl](https://github.com/jfcoz/postgresqltuner) - 用于分析 PostgreSQL 数据库配置并提供调整建议的简单脚本。


## 开发运营
- [DBmaestro](https://www.dbmaestro.com) - 加快发布周期并支持整个 IT 生态系统的敏捷性。
- [Toad DevOps Toolkit](https://www.quest.com/products/toad-devops-toolkit/) - 在 DevOps 工作流程中执行关键数据库开发功能，而不会影响质量、性能或可靠性。


## 报告
- [Chartbrew](https://chartbrew.com) - 从多个数据库和服务创建实时仪表板、图表和客户报告。
- [Poli](https://github.com/shzlw/poli) - 专为 SQL 爱好者打造的易于使用的 SQL 报告应用程序。


## 发行版
- [DBdeployer](https://github.com/datacharmer/dbdeployer) - 轻松部署MySQL数据库服务器的工具。
- [dbatools](https://github.com/sqlcollaborative/dbatools) - 您可能会将其视为命令行 SQL Server Management Studio 的 PowerShell 模块。
- [Postgres.app](https://github.com/PostgresApp/PostgresApp) - 全功能 PostgreSQL 安装打包为标准 Mac 应用程序。
- [BigSQL](https://www.bigsql.org) - 开发人员友好的 PostgreSQL 发行版。
- [Elephant Shed](https://github.com/credativ/elephant-shed) - 基于 Web 的 PostgreSQL 管理前端，捆绑了多个与 PostgreSQL 一起使用的实用程序和应用程序。
- [Pigsty](https://github.com/Vonng/pigsty) - 包含电池的 PostgreSQL 开源发行版，为开发人员提供终极可观察性和数据库即代码工具箱。


## 安全性
- [Acra](https://github.com/cossacklabs/acra) - 数据库安全套件。具有字段级加密的数据库代理、加密数据搜索、SQL 注入防护、入侵检测、蜜罐。支持客户端和代理端（“透明”）加密。 SQL、NoSQL。
- [Databunker](https://github.com/securitybunker/databunker) - 符合 GDPR 的特殊安全保管库，用于在常规数据库之上构建客户记录。
- [Inspektor](https://github.com/poonai/inspektor) - 数据库的访问控制层。 Inspektor 利用开放策略代理来做出策略决策。


## SQL

### 分析仪
- [Holistic.dev](https://holistic.dev) - 针对数据库性能、安全和架构问题的自动检测服务。
- [SQLCheck](https://github.com/jarulraj/sqlcheck) - 自动检测常见的 SQL 反模式。
- [SQLFluff](https://github.com/sqlfluff/sqlfluff) - 方言灵活且可配置的 SQL linter。
- [SQLLineage](https://github.com/reata/sqllineage) - 由 Python 提供支持的 SQL 沿袭分析工具。
- [TSQLLint](https://github.com/tsqllint/tsqllint) - 用于描述、识别和报告 TSQL 脚本中反模式存在的工具。

### 代码生成器
- [sqlc](https://sqlc.dev) - SQL-first 代码生成器为各种语言和各种数据库生成类型安全的绑定。
- [SQLDelight](https://sqldelight.github.io/sqldelight) - SQL-first 代码生成器为 Kotlin 和各种数据库生成类型安全的绑定。
- [pGenie](https://pgenie.io) - SQL-first 代码生成器为各种语言生成类型安全的绑定，并专门针对 PostgreSQL 数据库。

### 扩展
- [PartiQL](https://partiql.org) - 对关系数据、半结构化数据和嵌套数据的 SQL 兼容访问。

### 框架
- [Apache Calcite](https://calcite.apache.org) - 具有高级 SQL 功能的动态数据管理框架。
- [ZetaSQL](https://github.com/google/zetasql) - SQL 分析器框架。

### 格式化程序
- [CodeBuff](https://github.com/antlr/codebuff) - 通过机器学习进行与语言无关的漂亮打印。
- [JSQLFormatter](https://github.com/manticore-projects/jsqlformatter) - 适用于许多基于 JSqlParser 的 RDBMS 的开源 Java SQL 格式化程序。
- [SQL Online](https://sqlonline.in) - 一个免费工具，用于格式化您的 SQL 查询，然后为分析师提供内容。
- [pgFormatter](https://github.com/darold/pgFormatter) - PostgreSQL SQL 语法美化器。
- [Poor SQL](https://poorsql.com) - 即时免费开源 T-SQL 格式化。
- [SQL Formatter](https://github.com/zeroturnaround/sql-formatter) - 用于漂亮打印 SQL 查询的 JavaScript 库。

### 游戏
- [Lost at SQL](https://lost-at-sql.therobinlord.com) - 一款 SQL 学习游戏，可帮助您掌握基本的 SQL 技能 - 以便您可以使用查询来获取信息。
- [Querymon](https://codepip.com/games/querymon/) - 学习在 Querydex 上使用 SQL 查询，Querydex 是一个包含从普通到传奇的怪物的数据库。
- [Schemaverse](https://datalemur.com/blog/games-to-learn-sql#schemaverse) - 完全在 PostgreSQL 数据库中实现的基于太空的策略游戏。
- [SQL Island](https://sql-island.informatik.uni-kl.de) - 在飞机失事中幸存后，你将暂时被困在 SQL 岛上。通过在游戏中取得进展，你将找到逃离这座岛屿的方法。
- [SQL Murder Mystery](https://mystery.knightlab.com) - 旨在成为学习 SQL 概念和命令的自学课程，以及适合经验丰富的 SQL 用户解决有趣犯罪的有趣游戏。
- [SQL Police Department](https://sqlpd.com) - 在 SQLPD 中，您可以在学习 SQL 的同时解决犯罪问题。

### 解析器
- [General SQL Parser](https://www.sqlparser.com) - SQL 的解析、格式化、修改和分析。
- [jOOQ](https://github.com/jOOQ/jOOQ) - 解析 SQL，将其转换为其他方言，并允许表达式树转换。
- [JSqlParser](https://github.com/JSQLParser/JSqlParser) - 解析 SQL 语句并将其转换为 Java 类的层次结构。
- [libpg_query](https://github.com/pganalyze/libpg_query) - 用于在服务器环境之外访问 PostgreSQL 解析器的 C 库。
- [More SQL Parsing!](https://github.com/klahnakoski/mo-sql-parsing) - 将 SQL 解析为 JSON。
- [sqlparse](https://github.com/andialbrecht/sqlparse) - Python 的非验证 SQL 解析器。
- [SQLGlot](https://github.com/tobymao/sqlglot) - 纯 Python SQL 解析器、转译器和构建器。

### 超级SQL
针对任何内容运行 SQL 查询
- [CloudQuery](https://github.com/cloudquery/cloudquery) - 提取、转换您的云资产并将其加载到规范化的 PostgreSQL 表中。
- [csvq](https://github.com/mithrandie/csvq) - 用于 CSV 的类似 SQL 的查询语言。
- [dsq](https://github.com/multiprocessio/dsq) - 用于针对 JSON、CSV、Excel、Parquet 等运行 SQL 查询的命令行工具。
- [MAT Calcite plugin](https://github.com/vlsi/mat-calcite-plugin) - Eclipse Memory Analyzer 的这个插件允许通过 SQL 查询堆转储。
- [OctoSQL](https://github.com/cube2222/octosql) - 查询工具，允许您使用 SQL 连接、分析和转换来自多个数据库和文件格式的数据。
- [osquery](https://github.com/osquery/osquery) - SQL 支持的操作系统检测、监控和分析。
- [Resmo](https://www.resmo.com) - 使用 SQL 审核和评估资源。
- [sq](https://github.com/neilotoole/sq) - 命令行工具，提供对结构化数据源的 jq 式访问：SQL 数据库或 CSV 或 Excel 等文档格式。它是sql+jq的私生子。
- [Steampipe](https://github.com/turbot/steampipe) - 使用 SQL 即时查询您的云服务（AWS、Azure、GCP 等）。
- [TextQL](https://github.com/dinedal/textql) - 针对 CSV 或 TSV 等结构化文本执行 SQL。
- [trdsql](https://github.com/noborus/trdsql) - CLI 工具，可以对 CSV、LTSV、JSON 和 TBLN 执行 SQL 查询。
- [Trino](https://github.com/trinodb/trino) - 分布式 SQL 查询引擎，旨在查询分布在一个或多个异构数据源上的大型数据集。

### 语言服务器协议
- [SQLLanguageServer](https://github.com/joe-re/sql-language-server) - SQL 语言服务器。
- [sqls](https://github.com/lighttiger2505/sqls) - 用 Go 编写的 SQL 语言服务器。

### 学习
SQL的学习与困惑
- [Advanced SQL Puzzles](https://github.com/smpetersgithub/AdvancedSQLPuzzles) - 困难的基于集合的 SQL 谜题。
- [Hackerrank](https://www.hackerrank.com/domains/sql) - 练习编码、准备面试并获得聘用。
- [Learn SQL in a Month of Lunches](https://www.manning.com/books/learn-sql-in-a-month-of-lunches) - 一本关于如何使用 SQL 检索、过滤和分析数据的书。
- [LeetCode](https://leetcode.com/problemset/database) - 提高您的技能，扩展您的知识并为技术面试做好准备。
- [Select Star SQL](https://selectstarsql.com) - 免费的交互式书籍，旨在成为互联网上学习 SQL 的最佳场所。
- [StrataScratch](https://www.stratascratch.com/blog/categories/sql) - 数据科学教育资源。
- [SQL Murder Mystery](https://github.com/NUKnightLab/sql-mysteries) - 学习 SQL 概念和命令的自学课程，以及适合经验丰富的 SQL 用户解决有趣犯罪的有趣游戏。

### 计划
- [pev2](https://github.com/dalibo/pev2) - 一个 Vue.js 组件，用于显示 PostgreSQL 执行计划的图形可视化。
- [pg_flame](https://github.com/mgartner/pg_flame) - 用于 PostgreSQL“EXPLAIN ANALYZE”输出的火焰图生成器。

### 脚本
用于各种目的的有用 SQL 脚本
- [DBA MultiTool](https://github.com/LowlyDBA/dba-multitool) - 长期的 T-SQL 脚本：优化 SQL Server 的存储、动态文档和一般管理需求。
- [pgx_scripts](https://github.com/pgexperts/pgx_scripts) - 用于数据库分析和管理的有用小脚本的集合，由我们的 PostgreSQL Experts 团队创建。
- [pgsql-bloat-estimation](https://github.com/ioguix/pgsql-bloat-estimation) - 用于测量 PostgreSQL 索引和表中统计膨胀的查询。
- [pgWikiDont](https://gitlab.com/depesz/pgWikiDont) - SQL 测试，检查您的数据库是否遵循 <https://wiki.postgresql.org/wiki/Dont_Do_This> 中的规则。
- [pg-utils](https://github.com/dataegret/pg-utils) - 有用的 PostgreSQL 实用程序。
- [PostgreSQL cheat sheet](https://postgrescheatsheet.com) - <timescale.com> 提供的有用 SQL 脚本和命令。
- [postgres_dba](https://github.com/NikolayS/postgres_dba) - PostgreSQL DBA 和所有工程师缺少的一组有用工具。
- [postgres_queries_and_commands.sql](https://gist.github.com/rgreenjr/3637525) - 有用的 PostgreSQL 查询和命令。
- [TPT](https://github.com/tanelpoder/tpt-oracle) - 这些 sqlplus 脚本用于 Oracle 数据库性能优化和故障排除。


## 数据
- [dbt](https://github.com/dbt-labs/dbt-core) - 只需编写 select 语句即可转换数据，而 dbt 则负责将这些语句转换为数据仓库中的表和视图。
- [QuickTable](https://quicktable.io) - 使每个人都能够无需代码即可访问、清理、分析、转换和建模数据。

### 目录
- [Amundsen](https://github.com/amundsen-io/amundsen) - 元数据驱动的应用程序可提高数据分析师、数据科学家和工程师与数据交互时的工作效率。
- [DataHub](https://github.com/datahub-project/datahub) - 现代数据堆栈的元数据平台。
- [Marquez](https://github.com/MarquezProject/marquez) - 收集、聚合和可视化数据生态系统的元数据。

### 血统
- [Dwh.dev](https://dwh.dev) - Snowflake 的 Nexgen 数据沿袭。

### 生成/屏蔽/子集化
- [Benerator](https://github.com/rapiddweller/rapiddweller-benerator-ce) - 生成、混淆（匿名/假名）和迁移数据以用于开发、测试和培训目的。
- [dbForge Data Generator for MySQL](https://www.devart.com/dbforge/mysql/data-generator) - 强大的 GUI 工具，用于创建大量真实的测试数据。
- [dbForge Data Generator for Oracle](https://www.devart.com/dbforge/oracle/data-generator) - 小而强大的 GUI 工具，用于使用大量实际测试数据填充 Oracle 模式。
- [dbForge Data Generator for SQL Server](https://www.devart.com/dbforge/sql/data-generator) - 强大的 GUI 工具，可快速生成有意义的数据库测试数据。
- [Faker](https://github.com/faker-js/faker) - 在浏览器和 Node.js 中生成大量虚假数据。
- [Greenmask](https://github.com/GreenmaskIO/greenmask) - 适用于 MySQL 和 PostgreSQL 的数据库匿名化和合成数据生成工具。
- [myanon](https://github.com/ppomes/myanon) - MySQL 转储文件的流式匿名器。从 stdin 读取 mysqldump，将匿名版本写入 stdout。支持确定性哈希、固定值、JSON 字段匿名化和 Python 扩展。
- [Noisia](https://github.com/lesovsky/noisia) - PostgreSQL 的有害工作负载生成器。
- [quick-seed](https://github.com/miit-daga/quick-seed) - 与数据库无关的播种工具，用于生成真实的测试数据，支持 PostgreSQL、MySQL、SQLite、Prisma 和 Drizzle ORM。
- [SB Data Generator](https://soft-builder.com/sb-data-generator) - 简单而强大的工具，可为您的应用程序生成并填充选定的表或整个数据库，并使用真实的测试数据。生成以下测试数据：Oracle、MS SQL Server、MySQL、PostgreSQL、Firebird、SQLite、Azure SQL 数据库、Amazon Redshift 和 Amazon RDS。
- [SQLable](https://sqlable.com/generator/) - 在浏览器中生成虚假数据。
- [Synthesized TDK](https://docs.synthesized.io/tdk/latest) - DevOps 数据库屏蔽和生成的最佳朋友。

### 数据分析器
- [Data Profiler](https://github.com/capitalone/dataprofiler) - DataProfiler 是一个 Python 库，旨在简化数据分析、监控和敏感数据检测。
- [Desbordante](https://github.com/desbordante/desbordante-core) - 开源数据分析器专门致力于发现和验证数据中的复杂模式。
- [YData Profiling](https://github.com/ydataai/ydata-profiling) - 用于对数据集进行高级分析的通用开源数据分析器。

### 复制
- [dtle](https://github.com/actiontech/dtle) - MySQL 的分布式数据传输服务。
- [Litestream](https://github.com/benbjohnson/litestream) - SQLite 的流式复制。
- [pgsync](https://github.com/ankane/pgsync) - 在数据库之间同步 PostgreSQL 数据。
- [pg_chameleon](https://github.com/the4thdoctor/pg_chameleon) - 用 Python 3 编写的 MySQL 到 PostgreSQL 副本系统。该系统使用 mysql-replication 库从 MySQL 中提取行图像，并将其作为 JSONB 存储到 PostgreSQL 中。
- [PGDeltaStream](https://github.com/hasura/pgdeltastream) - 一个 Golang Web 服务器，使用 PostgreSQL 逻辑解码功能，通过 Websockets 流式传输 PostgreSQL 至少一次更改。
- [repmgr](https://github.com/2ndQuadrant/repmgr) - 最受欢迎的 PostgreSQL 复制管理器。

### 比较
- [data-diff](https://github.com/datafold/data-diff) - 命令行工具和 Python 库可有效区分两个不同数据库之间的行。
- [KS DB Merge Tools](https://ksdbmerge.tools) - 用于比较和同步数据库架构和数据的 GUI。适用于 Oracle 数据库、MySQL、MariaDB、SQL Server、PostgreSQL、SQLite、MS Access 和跨 DBMS。

## 论文
有关数据库工具的文档、文章、宣言和其他理论材料
- [The "Database as Code" Manifesto](https://github.com/mgramin/database-as-code) - 将您的数据库视为代码。
- [Grokking Relational Database Design](https://www.manning.com/books/grokking-relational-database-design) - 设计和实现第一个数据库的友好图解指南。

## 机器学习
- [MindsDB](https://github.com/mindsdb/mindsdb) - 数据库内机器学习。
- [SQLFlow](https://github.com/sql-machine-learning/sqlflow) - 将 SQL 和 AI 结合在一起。

## 贡献
- 随时欢迎您的贡献！请先阅读[贡献指南](contributing.md)。
