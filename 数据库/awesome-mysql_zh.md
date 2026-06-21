# 很棒的mysql

精彩的 MySQL 免费和开源软件、库和资源的精选列表。 [![真棒](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

该列表接受并鼓励拉取请求。请参阅[贡献](https://github.com/shlomi-noach/awesome-mysql/blob/master/CONTRIBUTING.md)

### 内容

- [很棒的 MySQL](#awesome-mysql)
    - [Analysis](#analysis)
    - [Backup](#backup)
    - [Benchmarking](#benchmarking)
    - [二进制日志复制](#binlog-replication)
    - [ChatOps](#chatops)
    - [Configuration](#configuration)
    - [Connectors](#connectors)
    - [Deployment](#deployment)
    - [Development](#development)
    - [GUI](#gui)
    - [HA](#ha)
    - [MCP](#mcp)
    - [Proxy](#proxy)
    - [Replication](#replication)
    - [Schema](#schema)
    - [Security](#security)
    - [Server](#server)
    - [Sharding](#sharding)
    - [Toolkits](#toolkits)

- [Resources](#resources)
    - [E-Books](#e-books)


## 分析

*性能、结构和数据分析工具*

- [Anemometer](https://github.com/box/Anemometer) - Box SQL 慢查询监视器。
- [innodb-ruby](https://github.com/jeremycole/innodb_ruby) - Ruby 中的 InnoDB 文件格式解析器。
- [innotop](https://github.com/innotop/innotop) - MySQL 的“顶级”克隆，具有许多功能和灵活性。
- [MySQL Explain Analyzer](https://github.com/Preetam/explain-analyzer) - 基于 Web 的“EXPLAIN FORMAT = JSON”输出分析器，为保存的示例提供注释、可扩展性分析和永久链接。
- [mysql-statsd](https://github.com/db-art/mysql-statsd) - 一个 Python 守护进程，用于从 MySQL 收集信息并通过 StatsD 将其发送到 Graphite。
- [MySQLTuner-perl](https://github.com/major/MySQLTuner-perl) - 该脚本允许您快速检查 MySQL 安装并进行调整以提高性能和稳定性。
- [Prometheus](https://github.com/prometheus/prometheus)/[mysqld_exporter](https://github.com/prometheus/mysqld_exporter) - 用于实时监控和警报的时间序列数据库。
- [pstop](https://github.com/sjmudd/ps-top) - 一个类似 top 的 MySQL 程序，收集、聚合和显示来自 Performance_schema 的信息。
- [ReliaDB EXPLAIN Analyzer](https://github.com/Mughees52/mysql-explain-analyzer) - 基于浏览器的 MySQL 和 MariaDB EXPLAIN 可视化工具，具有问题检测、索引建议和查询重写功能。 100% 客户端。
- [Wireshark](https://gitlab.com/wireshark/wireshark/) - 一个可以解码MySQL协议的协议分析器。
- [Dolphie](https://github.com/charles-001/dolphie) - 用于实时分析 MySQL/MariaDB 和 ProxySQL 的现代终端工具
- [sql-tap](https://github.com/mickamy/sql-tap) - 实时 SQL 流量查看器。

## 备份

*备份/恢复/恢复工具*

- [Databasus](https://github.com/databasus/databasus) - 通过 Web UI 进行计划 MySQL 备份的工具，具有外部存储（本地、S3、FTP、Google Drive 等）、通知（webhook、Discord、Slack 等）和团队管理。
- [Dumpling](https://github.com/pingcap/tidb/tree/master/dumpling) - 用 GoLang 编写的 MySQL/TiDB 逻辑并行备份/转储工具 - 支持 csv 格式输出并集成为库
- [MyDumper](https://github.com/mydumper/mydumper) - MySQL 的逻辑并行备份/转储工具
- [Percona Xtrabackup](https://github.com/percona/percona-xtrabackup) - 用于基于 MySQL 的服务器的开源热备份实用程序，在备份期间不会锁定数据库。
- [Portabase](https://github.com/Portabase/portabase) - 基于代理的 MySQL 备份和恢复平台，具有分散执行和集中编排功能。

## 标杆管理

*给服务器施加压力的工具*

- [HammerDB](https://github.com/TPC-Council/HammerDB) - MySQL/MariaDB 和其他开源和商业数据库的开源数据库基准测试。
- [go-tpc](https://github.com/pingcap/go-tpc) - MySQL 的 [TPCC](http://www.tpc.org/tpcc/) 和 [TPCH](http://www.tpc.org/tpch/) 基准的 golang 端口。
- [iibench-mysql](https://github.com/tmcallaghan/iibench-mysql) - MySQL/Percona/MariaDB 的基于 Java 的索引插入基准版本。
- [Sysbench](https://github.com/akopytov/sysbench) - 模块化、跨平台和多线程基准测试工具。
- [TPCC-MySQL](https://github.com/Percona-Lab/tpcc-mysql)（已存档） - 流行的 [TPCC](http://www.tpc.org/tpcc/) MySQL 基准测试的端口。

## 二进制日志复制

- [DM](https://github.com/pingcap/tiflow) - 高可用的数据迁移平台，支持MySQL/MariaDB数据迁移到TiDB并合并分表
- [Kingbus](https://github.com/flike/kingbus) - 基于Raft构建的分布式MySQL binlog存储系统
- [mysql-ripple](https://github.com/google/mysql-ripple) (已存档) - Ripple，一个可以充当 MySQL 复制中间人的服务器

## 聊天操作

*集成到聊天室的脚本*

- [Hubot MySQL ChatOps](https://github.com/samlambert/hubot-mysql-chatops)

## 配置

*MySQL 示例配置和顾问*

- [mysql-compatibility-config](https://github.com/morgo/mysql-compatibility-config) - 使 MySQL 配置的行为更像 MySQL 的较新（或较旧）版本。

## 连接器

*适用于各种编程语言的 MySQL 连接器*

- [ballerinax/mysql](https://github.com/ballerina-platform/module-ballerinax-mysql) - MySQL 的官方 Ballerina 连接器。
- [DBD::MariaDB](https://github.com/perl5-dbi/DBD-MariaDB) - 用于 Perl5 数据库接口的 MariaDB 和 MySQL 驱动程序。
- [DBD::mysql](https://github.com/perl5-dbi/DBD-mysql) - Perl5 数据库接口的 MySQL 驱动程序。
- [go-sql-driver](https://github.com/go-sql-driver/mysql) - 一个轻量级且快速的 MySQL 驱动程序，适用于 Go 的 (golang) 数据库/sql 包。
- [libAttachSQL](https://github.com/libattachsql/libattachsql) - libAttachSQL 是一个用于 MySQL 服务器的轻量级、非阻塞 C API。
- [MariaDB Connector/J](https://github.com/mariadb-corporation/mariadb-connector-j) - LGPL 许可的用于 Java 应用程序的 MariaDB 客户端库。
- [mex-mariadb](https://github.com/markuman/mex-mariadb) - 麻省理工学院为 GNU Octave 和 Matlab 授权了 MariaDB/MySQL 客户端库。
- [MySQL C API](https://dev.mysql.com/downloads/c-api/) - MySQL 的官方 C 驱动程序。
- [MySQL Connector/C++](https://github.com/mysql/mysql-connector-cpp) - MySQL 的官方 C/C++ 驱动程序。
- [MySQL Connector/J](https://github.com/mysql/mysql-connector-j) - 用于 Java 平台和开发的标准化数据库驱动程序。
- [MySQL Connector/NET](https://github.com/mysql/mysql-connector-net) - 用于.Net 平台和开发的标准化数据库驱动程序。
- [MySQL Connector/Node.js](https://github.com/mysql/mysql-connector-nodejs) - MySQL 的官方 Node.js 驱动程序。
- [MySQL Connector/Python](https://github.com/mysql/mysql-connector-python) - 用于 Python 平台和开发的标准化数据库驱动程序。
- [mysqlclient-python](https://github.com/PyMySQL/mysqlclient) - 适用于 Python 的 MySQL 数据库连接器。
- [node-mysql](https://github.com/mysqljs/mysql) - 一个实现 MySQL 协议的纯 Nodejs Javascript 客户端。
- [PHP mysqlnd](https://www.php.net/manual/en/book.mysqlnd.php) - PHP 的 MySQL 本机驱动程序。
- [PyMySQL](https://github.com/PyMySQL/PyMySQL) - 适用于 Python 的 MySQL 数据库连接器。
- [Ruby Mysql2 gem](https://github.com/brianmario/mysql2) - 用于 Ruby 和 Rails 项目的 MySQL 驱动程序。
- [MyZql](https://github.com/speed2exe/myzql) - 本机 Zig 中的 MySQL 和 MariaDB 驱动程序。
- [wtx](https://github.com/c410-f3r/wtx) - 用 Rust 编写的 MySQL/MariaDB/Percona 客户端

## 部署

*MySQL部署工具*

- [MariaDB4j](https://github.com/MariaDB4j/MariaDB4j) - 无需安装或外部依赖即可运行 MariaDB 的 Java 启动器。


## 发展

*支持MySQL相关开发的工具*

- [Flywaydb](https://github.com/flyway/flyway) - 数据库迁移；在所有实例中轻松可靠地发展您的数据库架构
- [dbsafe](https://github.com/nethalo/dbsafe) - MySQL DDL/DML操作执行前安全分析
- [Liquibase](https://github.com/liquibase/liquibase) - 数据库的源代码控制
- [Shift](https://github.com/square/shift) - 帮助您在 MySQL 数据库上运行架构迁移的应用程序
- [Skeema](https://github.com/skeema/skeema) - 适用于 MySQL 和 MariaDB 的声明式纯 SQL 模式管理系统，支持分片和外部在线模式更改工具
- [SQLE](https://github.com/actiontech/sqle/blob/main/README_en.md) - SQLE是一个面向DBA或开发人员的SQL审计平台
- [Test database](https://github.com/datacharmer/test_db) - 带有集成测试套件的示例 MySQL 数据库，用于测试应用程序和服务器
- [cover_me](https://github.com/verizonconnect/database-development) - mysql存储过程和函数的代码覆盖率工具

## 图形用户界面

*GUI 前端和应用程序*

- [Adminer](https://github.com/vrana/adminer/) - 在单个 PHP 文件中进行数据库管理。
- [DBeaver](https://github.com/dbeaver/dbeaver/) - 跨平台 SQL 和 NoSQL 数据库客户端。
- [HeidiSQL](https://github.com/HeidiSQL/HeidiSQL) - 适用于 Windows 的 MySQL GUI 前端。
- [ILLA Cloud](https://github.com/illacloud/illa-builder) - 与Mysql集成的低代码内部工具构建器，可以用作Mysql的GUI。
- [mycli](https://github.com/dbcli/mycli) - 具有自动完成和语法突出显示功能的 MySQL 终端客户端。
- [MySQL Shell](https://github.com/mysql/mysql-shell/) - MySQL 的高级客户端和代码编辑器，支持通过交互式 JavaScript、Python 或 SQL 界面开发和管理 MySQL Server 和 MySQL InnoDB 集群 (AdminAPI)。
- [MySQL Workbench](https://github.com/mysql/mysql-workbench) - 为 DBA 和开发人员提供用于数据库设计和建模的集成工具环境； SQL开发；数据库管理。
- [Ocelot GUI](https://github.com/ocelot-inc/ocelotgui) - MySQL 或 MariaDB 的 GUI 客户端，包括调试器。
- [OmniDB：用于数据库管理的 Web 工具](https://github.com/OmniDB/OmniDB)
- [Percona Monitoring and Management](https://github.com/percona/pmm) - 用于管理和监控 MySQL 性能的开源平台。
- [phpMyAdmin](https://github.com/phpmyadmin/phpmyadmin) - 一个用 PHP 编写的免费软件工具，旨在通过 Web 处理 MySQL 的管理。
- [pspg](https://github.com/okbob/pspg) - 为寻呼机提供增强的表格数据可视化和导航功能。最初是为 PostgreSQL 实现的，但也支持 MySQL。
- [Sequel Ace](https://github.com/Sequel-Ace/Sequel-Ace) - 用于处理 MySQL 数据库的 Mac 数据库管理应用程序。
- [TablePro](https://github.com/TableProApp/TablePro) - 适用于 MySQL 和许多其他数据库的本机 macOS 客户端，具有内联编辑、SSH 隧道和 AI 助手。免费且开源。
- [SQLyog Community edition](https://github.com/webyog/sqlyog-community) - SQLyog 社区版。对于 Windows，在 Mac 和 Linux 下的 wine 下运行良好
- [squix](https://github.com/eduardofuncao/squix) - 具有查询管理和交互式结果的 SQL 命令行客户端。
- [WebDB](https://github.com/WebDB-App/app) - 开源且高效的数据库 IDE。具有简单的服务器连接、现代 ERD、智能数据生成器、AI 助手、NoSQL 结构管理器、时间机器和强大的查询编辑器

## HA

*高可用性解决方案*

- [Galera Cluster](https://github.com/codership/galera) - 基于同步复制的真正的多主集群。
- [mha4mysql-node](https://github.com/yoshinorim/mha4mysql-node) 和 [mha4mysql-manager](https://github.com/yoshinorim/mha4mysql-manager)（均未维护） - 掌握 MySQL 的高可用性管理器和工具。
- [Orchestrator](https://github.com/openark/orchestrator)（已存档） - MySQL 复制拓扑管理和高可用性解决方案。
- [Percona Replication Manager](https://github.com/percona/replication-manager) - Pacemaker 的异步 MySQL 复制管理器代理。使用 Booth 支持基于文件和 GTID 的复制、地理分布式集群。
- [replication-manager](https://github.com/signal18/replication-manager) - 用于管理 MariaDB 10.x 和 MySQL & Percona Server 5.7 GTID 复制拓扑的高可用性解决方案。

## MCP

- [MCP MariaDB Server](https://github.com/MariaDB/mcp) - 官方 MariaDB MCP 服务器。
- [MySQL MCP Server](https://github.com/askdba/mysql-mcp-server) - 高级 MCP 服务器通过模型上下文协议公开 MySQL
- [TiDB MCP Server](https://pingcap.github.io/ai/integrations/tidb-mcp-server/) - TiDB 的 MCP 服务器。

## 代理

*MySQL 代理*

- [MySQL Router](https://dev.mysql.com/doc/mysql-router/en/) - MySQL Router 是 InnoDB 集群的一部分，是一个轻量级中间件，可在应用程序和后端 MySQL 服务器之间提供透明路由。
- [ProxySQL](https://github.com/sysown/proxysql) - MySQL 的高性能代理。

## 复制

*复制相关软件*

* [data-diff](https://github.com/datafold/data-diff)（已存档） - 命令行工具和 Python 库可有效区分两个不同数据库之间的行。


## 模式

*附加架构*

- [common_schema](https://github.com/shlomi-noach/common_schema) - DBA的MySQL框架，提供函数库、视图库和QueryScript解释器。
- [sys](https://github.com/mysql/mysql-sys)（已存档）- 一系列视图、函数和过程，可帮助 MySQL 管理员深入了解 MySQL 数据库的使用情况。请参阅[系统架构文档](https://dev.mysql.com/doc/refman/8.4/en/sys-schema.html)


## 安全性

*防止数据库泄露敏感数据的工具（加密、屏蔽和标记化、蜜罐等）*

- [Acra](https://github.com/cossacklabs/acra) - SQL数据库保护套件：强选择性加密、SQL注入预防、入侵检测系统。
- [myanon](https://github.com/ppomes/myanon) - MySQL 转储文件的流式匿名器，从 stdin 读取 mysqldump 输出并将匿名数据写入 stdout。支持确定性哈希、固定值、JSON 字段匿名化和 Python 扩展。
- [myldapsync](https://github.com/6eh01der/myldapsync) - 将 MySQL 或 MariaDB 用户与 LDAP 目录中的用户同步。

## 服务器

*MySQL 服务器风格*

- [MariaDB](https://github.com/MariaDB/server) - 社区开发了 MySQL 服务器的分支。
- [MySQL Server & MySQL Cluster](https://github.com/mysql/mysql-server) - Oracle 的官方 MySQL 服务器和 MySQL Cluster 发行版。
- [MyVector](https://github.com/askdba/myvector) - MySQL 的本机矢量搜索插件，作为服务器插件提供。
- [Percona Server](https://github.com/percona/percona-server) - 增强的、直接的 MySQL 替代品。
- [TiDB](https://github.com/pingcap/tidb) - 兼容MySQL协议的分布式HTAP数据库。

## 分片

*分片解决方案/框架*

- [Jetpants](https://github.com/tumblr/jetpants) - 由 Tumblr 开发的用于管理大范围分片集群的自动化套件。
- [Vitess](https://github.com/vitessio/vitess) - vitess 提供有助于扩展 MySQL 数据库以实现大规模 Web 服务的服务器和工具。


## 工具包

*工具包、通用脚本*

- [gh-ost](https://github.com/github/gh-ost/) - GitHub 的 MySQL 在线架构迁移。
- [go-mysql](https://github.com/go-mysql-org/go-mysql) - 一个纯 Go 库，用于处理 MySQL 网络协议和复制。
- [MySQL 实用程序](https://github.com/mysql/mysql-utilities)（已弃用） - 用 Python 编写的命令行实用程序集合，用于单独或在复制层次结构中维护和管理 MySQL 服务器。
- [Percona Toolkit](https://github.com/percona/percona-toolkit) - 一组高级命令行工具，用于执行各种难以手动执行的 MySQL 服务器和系统任务。
- [sql-splitter](https://github.com/HelgeSverre/sql-splitter) - 用于分割、合并、转换、验证和采样 mysqldump 文件的高性能 CLI。
- [Swoof](https://github.com/StirlingMarketingGroup/swoof) - 超快的 MySQL 表导入器，可通过临时表进行交换并支持文件/剪贴板目标。
- [UnDROP](https://github.com/twindb/undrop-for-innodb)（已存档）- 一种从删除或损坏的 InnoDB 表中恢复数据的工具。

# 资源

*现阶段“资源”将不包括网站、博客、幻灯片、演示视频等，因为担心列表大小*

## 电子书

*有关 MySQL 的电子书以及相关材料*

- [Database Systems Lecture Notes](http://spots.augusta.edu/caubert/db/ln/) - 关于数据库系统的讲义（以 pdf、html、odt 和 markdown 形式提供），包括关于 SQL 的一章，其中涵盖基本设置、练习和问题。
- [SQL-exercise](https://github.com/XD-DENG/SQL-exercise) - 包含多个SQL练习，包括模式描述图、构建模式的SQL代码、SQL中的问题和解决方案。基于 wikibook [SQL 练习](https://en.wikibooks.org/wiki/SQL_Exercises)。

## 孵化

已知为非生产性项目，但具有值得曝光的吸引力或实质内容。

- [VillageSQL](https://github.com/villagesql/villagesql-server) - MySQL 的直接替代品，具有代理 AI 时代的扩展。
