# 很棒的 Postgres [![awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

[<img src="https://wiki.postgresql.org/images/a/a4/PostgreSQL_logo.3colors.svg"align="right" width="100">](https://www.postgresql.org/)

> 受 [awesome-mysql](http://shlomi-noach.github.io/awesome-mysql/) 启发的精选的 [PostgreSQL](https://www.postgresql.org/) 软件、库、工具和资源列表

[PostgreSQL](https://en.wikipedia.org/wiki/PostgreSQL)，通常简称为 Postgres，是一个[对象关系数据库](https://en.wikipedia.org/wiki/Object-relational_database) (ORDBMS)。 PostgreSQL 是[ACID 兼容](https://en.wikipedia.org/wiki/ACID) 和[事务](https://en.wikipedia.org/wiki/Transaction_processing)。 （查看更多：[wikipedia:PostgreSQL](https://en.wikipedia.org/wiki/PostgreSQL)、[PostgreSQL.org](https://www.postgresql.org))

:elephant: 欢迎贡献。通过 [pull requests](https://github.com/dhamaniasad/awesome-postgres/pulls) 添加链接或创建 [issue](https://github.com/dhamaniasad/awesome-postgres/issues) 以开始讨论。请查看[贡献指南](CONTRIBUTING.md)。

## 内容

- [很棒的 Postgres](#awesome-postgres-)
    - [High-Availability](#high-availability)
    - [Backups](#backups)
    - [GUI](#gui)
    - [Distributions](#distributions)
    - [CLI](#cli)
    - [Server](#server)
    - [Monitoring](#monitoring)
    - [Extensions](#extensions)
    - [Platforms](#platforms)
    - [工作队列](#work-queues)
    - [Optimization](#optimization)
    - [Utilities](#utilities)
    - [语言绑定](#language-bindings)
    - [PaaS（PostgreSQL 即服务）](#paas-postgresql-as-a-service)
    - [Docker 镜像](#docker-images)
    - [Kubernetes](#kubernetes)
- [Resources](#resources)
    - [Tutorials](#tutorials)
    - [Blogs](#blogs)
    - [Documentation](#documentation)
    - [Newsletters](#newsletters)
    - [Videos](#videos)
    - [Community](#community)
    - [Roadmaps](#roadmaps)
    - [外部列表](#external-lists)

### 高可用性
* [autobase](https://github.com/vitabaks/autobase) - Autobase for PostgreSQL® 是一种开源 DBaaS，可自动部署和管理高度可用的 PostgreSQL 集群。
* [BDR](https://github.com/2ndQuadrant/bdr) - 双向复制 - PostgreSQL 的多主复制系统
* [Patroni](https://github.com/zalando/patroni) - 使用 ZooKeeper 或 etcd 的 PostgreSQL HA 模板。
* [Spock](https://github.com/pgEdge/spock) - 100% 开源逻辑多主 PostgreSQL 复制。
* [Stolon](https://github.com/sorintlab/stolon) - PostgreSQL HA 基于 Consul 或 etcd，并与 Kubernetes 集成。
* [pglookout](https://github.com/aiven/pglookout) - 复制监控和故障转移守护进程。
* [repmgr](https://github.com/2ndQuadrant/repmgr) - 用于管理 PostgreSQL 服务器集群中的复制和故障转移的开源工具套件。
* [Slony-I](https://slony.info/) - 具有级联和故障转移的“主到多个从”复制系统。
* [PAF](https://github.com/ClusterLabs/PAF) - PostgreSQL 自动故障转移：Postgres 的高可用性，基于 Pacemaker 和 Corosync。
* [SkyTools](https://github.com/pgq/skytools-legacy) - 复制工具，包括 PgQ（一个排队系统）和 Londiste（一个比 Slony 更容易管理的复制系统）。
* [pg_auto_failover](https://github.com/citusdata/pg_auto_failover) - 用于自动故障转移和高可用性的 Postgres 扩展和服务。
* [pgrwl](https://github.com/hashmap-kz/pgrwl) - 从 PostgreSQL 服务器实时传输预写日志 (WAL)。 pg_receivewal 的直接、容器友好的替代方案。
* [pg-status](https://github.com/krylosov-aa/pg-status) - 提供 HTTP 端点以立即检索当前主控主机或满足各种条件的副本的微服务。

### 备份
* [Barman](https://www.pgbarman.org/index.html) - 2ndQuadrant 的 PostgreSQL 备份和恢复管理器。
* [Databasus](https://databasus.com) - 通过 Web UI 进行预定 PostgreSQL 备份的工具，具有外部存储（本地、S3、FTP、Google Drive 等）、通知（webhook、Discord、Slack 等）和团队管理。
* [OmniPITR](https://github.com/omniti-labs/omnipitr) - PostgreSQL 的高级 WAL 文件管理工具。
* [pg\_probackup](https://github.com/postgrespro/pg_probackup) - pg\_arman 的一个分支，由 @PostgresPro 改进，支持增量备份、从副本备份、多线程备份和恢复以及无需存档命令的匿名备份。
* [pgBackRest](https://pgbackrest.org/) - 可靠的 PostgreSQL 备份和恢复。
* [pgbackweb](https://github.com/eduardolat/pgbackweb) - 一个完整的基于 Docker 的 Postgres 备份和维护工具，带有 Web UI。
* [pg\_back](https://github.com/orgrim/pg_back/) - pg\_back 是一个简单的备份脚本
* [pghoard](https://github.com/aiven/pghoard) - 用于云对象存储（AWS S3、Azure、Google Cloud、OpenStack Swift）的备份和恢复工具。
* [postgres-backup-oss](https://github.com/isaced/postgres-backup-oss) - 一个方便的 Docker 容器，用于定期将 PostgreSQL 备份到阿里云对象存储服务 (OSS)
* [wal-e](https://github.com/wal-e/wal-e)（已过时） - Heroku 将 PostgreSQL 简单连续存档到 S3、Azure 或 Swift。
* [wal-g](https://github.com/wal-g/wal-g) - WAL-E 的后继者用 Go 重写。目前支持 AWS (S3)、Google Cloud (GCS)、Azure 以及 OpenStack Swift、MinIO 和文件系统存储的云对象存储服务。支持块级增量备份，将备份任务卸载到备用服务器，提供并行化和限制选项。除了 Postgres 之外，WAL-G 还可用于 MySQL 和 MongoDB 数据库。
* [pitrery](https://dalibo.github.io/pitrery/) - pitrery 是一组 Bash 脚本，用于管理 PostgreSQL 的时间点恢复 (PITR) 备份。
* [pgbackup-sidecar](https://github.com/Musab520/pgbackup-sidecar) - `pgbackup-sidecar` 是一个轻量级的 Docker sidecar 容器，旨在使用 `pg_dump`、`cron` 和 bash 脚本自动定期备份 PostgreSQL 数据库，同时还将输出发送到 webhook。
* [pg-backups-to-s3](https://github.com/Saicheg/pg-backups-to-s3) - 基于 pg_dump 的 Docker 优先解决方案，支持基于环境的预定 PostgreSQL 备份配置，具有可选压缩、GPG 加密、Webhooks、自动上传到 Amazon S3。

### 图形用户界面
* [Adminer](https://www.adminer.org/) - 用 PHP 编写的全功能数据库管理工具。
* [Beekeeper Studio](https://www.beekeeperstudio.io) - 免费开源 SQL 客户端，具有现代 UI 和出色的 Postgres 支持。跨平台。
* [Bytebase](https://www.bytebase.com) - 面向开发人员、安全性、DBA 和平台工程团队的数据库 DevSecOps 解决方案。
* [Chartbrew](https://chartbrew.com) - 从 PostgreSQL 数据创建实时仪表板、图表和客户报告。具有与 SQL 配合使用的查询工具。
* [Count](https://count.co/) - 基于 Web 的分析平台，具有连接到 PostgreSQL（商业软件）的笔记本界面。
* [DataGrip](https://www.jetbrains.com/datagrip/) - 具有先进工具集和良好跨平台体验的IDE（商业软件）。
* [Datazenit](https://datazenit.com/) - 基于 Web 的 PostgreSQL GUI（商业软件）。
* [DataRow](https://www.datarow.com/) - 适用于 Amazon Redshift 的跨平台 SQL 客户端：简单、轻松、可扩展。
* [DBConvert Streams](https://streams.dbconvert.com/) - 一个云原生平台，用于跨各种云环境的 PostgreSQL 和 MySQL 数据库之间的实时数据迁移和 CDC 复制。 （商业软件）。
* [DBeaver](https://dbeaver.io/) - 通用数据库管理器，对 PostgreSQL 提供出色的支持。
* [dbForge Edge](https://www.devart.com/dbforge/edge/) - 一体化多数据库解决方案，支持 PostgreSQL、MySQL、MariaDB、SQL Server、Oracle 和各种相关云服务（商业软件）。
* [DbVisualizer](http://www.dbvis.com) - 面向开发人员、DBA 和分析师的跨平台数据库客户端（商业软件）。
* [Holistics](https://www.holistics.io/) - 在线跨平台数据库管理工具和 SQL 查询报告 GUI，具有强大的 PostgreSQL 支持（商业软件）。
* [JackDB](https://www.jackdb.com/) - 基于Web的SQL查询界面（商业软件）。
* [Luna Modeler](http://www.datensen.com) - 跨平台桌面数据建模工具（商业软件）。
* [Mathesar](https://mathesar.org/) - Web 应用程序为数据库提供直观的用户体验。
* [Metabase](https://www.metabase.com/) - 适用于 PostgreSQL 的简单仪表板、图表和查询工具。
* [Numeracy](https://numeracy.co/) - 带有 PostgreSQL 图表和仪表板的快速 SQL 编辑器（商业软件）。
* [pgAdmin](https://www.pgadmin.org/) - PostgreSQL 管理和管理 GUI。
* [pgMagic🪄](https://pgmagic.app/?ref=awesomepostgres) - 用自然语言与 Postgres 聊天（商业软件）。
* [PgManage](https://github.com/commandprompt/pgmanage) - 一个以 Postgres 为中心的现代多平台数据库客户端/管理工具。
* [pgModeler](https://pgmodeler.io/) - pgModeler 是一个开源 PostgreSQL 数据库建模器。
* [pgweb](https://github.com/sosedoff/pgweb) - 用 Go 编写的基于 Web 的 PostgreSQL 数据库浏览器。
* [phpPgAdmin](https://github.com/phppgadmin/phppgadmin) - 首要的 PostgreSQL 基于 Web 的管理工具。
* [Postbird](https://github.com/Paxa/postbird) - 适用于 macOS 的 PostgreSQL 客户端。
* [PostgresCompare](https://www.postgrescompare.com) - 跨平台数据库比较和部署工具（商业软件）。
* [Postico](https://eggerapps.at/postico/) - 适用于 macOS 的现代 PostgreSQL 客户端（商业软件）。
* [QueryGlow](https://queryglow.com/) - 自托管、基于 Web 的数据库 GUI，具有 AI SQL 生成、EXPLAIN 可视化工具和模式感知自动完成功能（商业软件）。
* [PSequel](http://www.psequel.com/) - 干净简单的界面，可快速执行常见的 PostgreSQL 任务（商业软件）。
* [Redash](https://github.com/getredash/redash) - 连接到任何数据源，轻松可视化和共享您的数据。
* [SQL Tabs](http://www.sqltabs.com/) - 用 JS 编写的 PostgreSQL 跨平台桌面客户端。
* [SQLPro for Postgres](http://macpostgresclient.com/) - 适用于 macOS（商业软件）的简单、强大的 PostgreSQL 管理器。
* [temBoard](https://github.com/dalibo/temboard) - 基于 Web 的 PostgreSQL GUI 和监控。
* [Teable](https://github.com/teableio/teable) - 超快速、实时、专业、开发人员友好、无代码数据库。
* [TablePlus](https://tableplus.com/) - 本机应用程序可让您编辑数据库和结构。确保高端安全（商业软件）。
* [Valentina Studio](https://www.valentina-db.com/en/valentina-studio-overview) - 跨平台数据库管理工具（免费/商业）
* [DbGate](https://dbgate.org) - 最智能的（非）SQL 数据库客户端
* [WebDB](https://webdb.app) - 高效的数据库 IDE。

### 发行版
* [Postgres.app](https://postgresapp.com/) - 在 macOS 上开始使用 PostgreSQL 的最简单方法。
* [Pigsty](https://github.com/Vonng/pigsty) - 包含电池的 PostgreSQL 开源发行版，为开发人员提供终极可观察性和数据库即代码工具箱。

### 命令行界面
* [atlas](https://github.com/ariga/atlas) - Atlas 是一个使用现代 DevOps 原则管理和迁移数据库模式的工具。
* [pgcli](https://github.com/dbcli/pgcli) - 具有自动完成和语法突出显示功能的 Postgres CLI
* [pgplan](https://github.com/JacobArthurs/pgplan) - 从 CLI 比较和分析 PostgreSQL EXPLAIN 计划
* [pgschema](https://www.pgschema.com) - Postgres 的 Terraform 风格声明式架构迁移
* [pg-schema-diff](https://github.com/stripe/pg-schema-diff) - CLI（和 Golang 库）用于比较 Postgres 架构并以最少的锁定生成 SQL 迁移。
* [MigrationPilot](https://github.com/mickelsamuel/migrationpilot) - PostgreSQL 迁移安全 CLI，可在生产前捕获危险的 DDL — 80 条规则、锁定分类、自动修复、GitHub Action。
* [pgsh](https://github.com/sastraxi/pgsh) - 像 Git 一样对 PostgreSQL 数据库进行分支
* [psql](https://www.postgresql.org/docs/current/static/app-psql.html) - 内置 PostgreSQL CLI 客户端
* [psql2csv](https://github.com/fphilipe/psql2csv) - 在 psql 中运行查询并将结果输出为 CSV
* [sabiql](https://github.com/riii111/sabiql) - 一个快速、无驱动程序的 TUI，用于浏览、查询和编辑 PostgreSQL 数据库。
* [schemaspy](https://github.com/schemaspy/schemaspy) - SchemaSpy 是一个兼容 JAVA JDBC 的工具，用于将数据库生成 HTML 文档，包括实体关系图
* [pdot](https://gitlab.com/dmfay/pdot) - 在 shell 中可视化和探索数据库结构，从外键图的高上下文视图到触发级联、角色继承和权限等等
* [squix](https://github.com/eduardofuncao/squix) - 具有查询管理和交互式结果的 SQL 命令行客户端。

### 服务器
* [AgensGraph](https://bitnine.net/) - 基于PostgreSQL的强大图数据库。
* [Apache Cloudberry](https://github.com/apache/cloudberry) - 以及 MPP PostgreSQL 分支。 Greenplum 数据库的开源替代方案。
* [FerretDB](https://www.ferretdb.io) - PostgreSQL 之上的真正开源 MongoDB 替代品。
* [Postgres-XL](https://www.postgres-xl.org/) - 基于 PostgreSQL 的可扩展开源数据库集群。
* [YugabyteDB](https://yugabyte.com/) - 在分布式存储和事务之上使用 PostgreSQL 分支的开源分布式 SQL

### 安全性
* [Acra](https://github.com/cossacklabs/acra) - SQL 数据库安全套件：数据保护代理，具有透明的“动态”数据加密、SQL 防火墙（SQL 注入预防）、入侵检测系统。

### 监控
* [check\_pgactivity](https://github.com/OPMDG/check_pgactivity) - check\_pgactivity 旨在从 Nagios 监控 PostgreSQL 集群。它提供了许多选项来测量和监控有用的性能指标。
* [Check\_postgres](https://github.com/bucardo/check_postgres) - Nagios check\_postgres 插件用于检查 PostgreSQL 数据库的状态。
* [coroot](https://github.com/coroot/coroot) - Coroot 是一个开源 APM 和可观察性工具，是 DataDog 和 NewRelic 的替代品。由 eBPF 提供支持，可快速洞察系统性能。
* [Datadog](https://www.datadoghq.com/product/database-monitoring/) - SaaS 监控，收集和可视化指标、查询和解释计划，并在遇到问题时发送警报（商业软件）。
* [Instrumental](https://github.com/Instrumental/instrumentald) - 实时性能监控，包括[预制图表](https://instrumentalapp.com/docs/instrumentald/postgresql#suggested-graphs)，以便于设置（商业软件）
* [libzbxpgsql](https://github.com/cavaliercoder/libzbxpgsql) - 适用于 Zabbix 的综合 PostgreSQL 监控模块。
* [myDBA](https://mydba.dev) - PostgreSQL 性能监控，具有 75 多个自动运行状况检查、集群感知索引顾问、查询分析以及 TimescaleDB、pgvector 和 PostGIS（商业软件）的扩展监控。
* [PMM](https://github.com/percona/pmm) - Percona 监控和管理 (PMM) 是一个免费开源平台，用于监控和管理 PostgreSQL、MySQL 和 MongoDB。
* [Pome](https://github.com/rach/pome) - Pome 代表 PostgreSQL 指标。 Pome 是一个 PostgreSQL 指标仪表板，用于跟踪数据库的运行状况。
* [pgmetrics](https://pgmetrics.io/) - pgmetrics 是一个开源、零依赖、单二进制工具，可以从正在运行的 PostgreSQL 服务器收集大量信息和统计数据，并以易于阅读的文本格式显示或将其导出为 JSON 和 CSV 以用于脚本编写。
* [pg\_view](https://github.com/zalando/pg_view) - 开源命令行工具，显示全局系统统计信息、每个分区信息、内存统计信息和其他信息。
* [pgwatch2](https://github.com/cybertec-postgresql/pgwatch2) - 灵活且易于入门 PostgreSQL 指标监控器专注于 Grafana 仪表板。
* [pgbench](https://www.postgresql.org/docs/devel/static/pgbench.html) - 在 PostgreSQL 上运行基准测试。
* [opm.io](http://opm.io) - Open PostgreSQL Monitoring 是一款免费软件套件，旨在帮助您管理 PostgreSQL 服务器。它可以收集统计数据、显示仪表板并在出现问题时发送警告。
* [okmeter.io](https://okmeter.io/pg) - 基于商业 SaaS 代理的监控，带有非常详细的 PostgreSQL 插件。它会自动收集数百个统计数据，显示各个方面的仪表板，并在出现问题时发送警报（商业软件）。
* [dexter](https://github.com/ankane/dexter) - Postgres 的自动索引器。检测慢速查询并创建索引（如果配置为这样做）。
* [pg_ash](https://github.com/NikolayS/pg_ash) - PostgreSQL 的活动会话历史记录。通过 pg_cron 每秒对 pg_stat_activity 进行一次采样，存储编码快照，并提供 32 个 SQL 函数用于等待事件分析。纯 SQL，无扩展，适用于托管提供商（RDS、Cloud SQL、Supabase 等）。
* [pg_exporter](https://github.com/Vonng/pg_exporter) - 适用于 PostgreSQL 和 Pgbouncer 的完全可定制的 Prometheus 导出器，具有细粒度的执行控制。
* [postgres_exporter](https://github.com/wrouesnel/postgres_exporter) - 用于 PostgreSQL 服务器指标的 Prometheus 导出器。
* [StatsMgr](https://codeberg.org/data-bene/statsmgr) - 开源 PostgreSQL 扩展，专为高效且有组织的高级统计管理而设计。

### 扩展
* [pgxn](https://pgxn.org/) PostgreSQL 扩展网络 - 许多开源 PostgreSQL 扩展的中央分发点。
* [Extensions listing by joelonsql](https://gist.github.com/joelonsql/e5aa27f8cc9bd22b8999b7de8aee9d47) - 1000 多个 PostgreSQL 扩展。
* [Pigsty extensions catalogue](https://ext.pigsty.io/list/) - 400 多个 PostgreSQL 扩展。
* [AGE](https://github.com/apache/age) - 添加全功能图形数据库支持，包括 Cypher 查询。
* [OrioleDB](https://www.orioledb.com/) - PostgreSQL 的云原生存储引擎。 OrioleDB 是一个 PostgreSQL 扩展，结合了磁盘引擎和内存引擎的优点。
* [Citus](https://github.com/citusdata/citus) - 用于实时工作负载的可扩展 PostgreSQL 集群。
* [cstore\_fdw](https://github.com/citusdata/cstore_fdw) - 用于使用 PostgreSQL 进行分析的列式存储。
* [cyanaudit](https://pgxn.org/dist/cyanaudit/) - Cyan Audit 逐列提供所有 DML 活动的数据库内日志记录。
* [pg_search](https://github.com/paradedb/paradedb) - pg_search 是一个 PostgreSQL 扩展，它支持使用 BM25 算法对 SQL 表进行全文搜索，BM25 算法是最先进的全文搜索排名函数。
* [pg_cron](https://github.com/citusdata/pg_cron) - 在 PostgreSQL 中运行定期作业。
* [pglogical](https://github.com/2ndQuadrant/pglogical) - 提供逻辑流复制的扩展。
* [pgcat](https://github.com/kingluo/pgcat) - 增强的 PostgreSQL 逻辑复制
* [pg\_barcode](https://github.com/btouchard/pg_barcode/) - PostgreSQL SVG QRcode 和 Datamatrix 生成器。
* [pg\_partman](https://github.com/pgpartman/pg_partman) - PostgreSQL 的分区管理扩展。
* [pg\_paxos](https://github.com/citusdata/pg_paxos/) - PostgreSQL 节点集群的 Paxos 和基于 Paxos 的表复制的基本实现。
* [pg\_shard](https://github.com/citusdata/pg_shard) - 用于横向扩展实时读取和写入的扩展。
* [pg\_stat\_monitor](https://github.com/percona/pg_stat_monitor) - PostgreSQL 的查询性能监控工具。
* [pg\_squeeze](https://github.com/cybertec-postgresql/pg_squeeze) - 具有最小锁定的自动膨胀清理扩展。
* [PGStrom](https://wiki.postgresql.org/wiki/PGStrom) - 将 CPU 密集型工作负载卸载到 GPU 的扩展。
* [PipelineDB](https://www.confluent.io/blog/pipelinedb-team-joins-confluent/) - PostgreSQL 扩展，可在流上连续运行 SQL 查询，并将结果增量存储在表中。
* [plpgsql\_check](https://github.com/okbob/plpgsql_check) - 允许检查 plpgsql 源代码的扩展。
* [PostGIS](http://postgis.net/) - PostgreSQL 的空间和地理对象。
* [PG\_Themis](https://github.com/cossacklabs/pg_themis) - Postgres 绑定作为加密库 Themis 的扩展，在 PgSQL 端提供各种安全服务。
* [zomboDB](https://github.com/zombodb/zombodb) - 通过使用 Elasticsearch 支持的索引实现高效全文搜索的扩展。
* [pgMemento](https://github.com/pgMemento/pgMemento) - 使用以 PL/pgSQL 编写的触发器和服务器端函数为 PostgreSQL 数据库内的数据提供审计跟踪。
* [TimescaleDB](https://www.timescale.com/) - 与 Postgres 完全兼容的开源时序数据库，作为扩展分发
* [pgTAP](https://pgtap.org/) - Postgres 的数据库测试框架
* [HypoPG](https://github.com/HypoPG/hypopg) - HypoPG 提供假设/虚拟索引功能。
* [pgRouting](https://github.com/pgRouting/pgrouting) - pgRouting 扩展了 PostGIS/PostgreSQL 地理空间数据库，以提供地理空间路由和其他网络分析功能。
* [PGroonga](https://pgroonga.github.io/) - PGroonga 提供了一种新的索引访问方法，该方法使用 Groonga 允许针对所有语言的超快速全文搜索功能。
* [PGAudit](https://www.pgaudit.org/) - PostgreSQL 审计扩展（或 pgaudit）通过 PostgreSQL 提供的标准日志记录工具提供详细的会话和/或对象审计日志记录。
* [PostgresML](https://postgresml.org/) - 数据库内的机器学习和 AI，包括向量、LLM 和经典 ML。仅使用 SQL 来训练、预测和管理机器学习模型的整个生命周期。
* [ParadeDB](https://github.com/paradedb/paradedb) - 用于搜索和分析的 Postgres
* [PostgreSQL Anonymizer](https://postgresql-anonymizer.readthedocs.io/en/stable/) - 通过 PG 安全标签屏蔽或替换 Postgres 数据库中的个人身份信息 (PII) 或商业敏感数据的扩展。

### 平台
* [Atlas4D](https://github.com/crisbez/atlas4d-base) - 开源 4D 时空平台，结合 PostGIS、TimescaleDB、pgvector 和 H3，实现统一的地理空间和时间序列智能。

### 工作队列
* [BeanQueue](https://github.com/LaunchPlatform/bq) - 基于SKIP LOCKED、LISTEN和NOTIFY的Python工作队列框架
* [pgmq](https://github.com/pgmq/pgmq) - 轻量级消息队列。类似于 AWS SQS 和 RSMQ，但在 Postgres 上。
* [river](https://github.com/riverqueue/river) - 适用于 Go 和 Postgres 的高性能作业处理系统。
* [pgBoss](https://github.com/timgit/pg-boss) - 像老板一样从 Node.js 在 Postgres 中排队作业。
* [dbos](https://www.dbos.dev/) - Typescript 和 Python 中的持久工作流程
* [Graphile Worker](https://worker.graphile.org) - 用 Node.js 编写的 PostgreSQL 高性能作业队列
* [@andyrmitchell/pg-queue](https://www.npmjs.com/package/@andyrmitchell/pg-queue) - Node.js 的“免维护”Postgres 队列

### 优化
* [EverSQL](https://www.eversql.com/) - 自动化查询优化工具、监控分析工具、索引推荐工具。 （商业软件）
* [PEV2](https://github.com/dalibo/pev2) - 在线 Postgres 解释可视化工具。
* [pg_flame](https://github.com/mgartner/pg_flame) - 用于查询计划的火焰图生成器。
* [PgHero](https://github.com/ankane/pghero) - PostgreSQL 见解变得简单。
* [pgMustard](https://www.pgmustard.com/) - 现代用户界面
对于“EXPLAIN”，还提供了性能提示（商业软件）。
* [pgtune](https://github.com/gregs1104/pgtune/) - PostgreSQL 配置向导。
* [pgtune](https://github.com/le0pard/pgtune) - PostgreSQL 配置向导的在线版本。
* [pgconfig.org](https://github.com/sebastianwebber/pgconfig) - PostgreSQL在线配置工具（也基于pgtune）。
* [PoWA](https://powa.readthedocs.io/en/latest/) - PostgreSQL 工作负载分析器收集性能统计数据并提供实时图表和图形，以帮助监控和调整 PostgreSQL 服务器。
* [pg_web_stats](https://github.com/kirs/pg_web_stats) - 用于查看 pg_stat_statements 的 Web UI。
* [TimescaleDB Tune](https://github.com/timescale/timescaledb-tune) - 一个程序，用于根据主机资源（例如内存和 CPU 数量）调整 TimescaleDB 数据库以使其发挥最佳性能。
* [Metis](https://www.metisdata.io/product/troubleshooting) - Metis 为包括 PostgreSQL 在内的 SQL 数据库提供可观察性和性能调优。 （商业软件）
* [aqo](https://github.com/postgrespro/aqo) - PostgreSQL 的自适应查询优化。
* [pgassistant](https://github.com/beh74/pgassistant-community) - 一个 PostgreSQL 工具，帮助开发人员通过 LLM 和 pgTune 集成来帮助理解、优化数据库。

### 公用事业
* [apgdiff](https://www.apgdiff.com/) - 比较两个数据库转储文件并使用 DDL 语句创建输出，这些语句可用于将旧数据库架构更新为新数据库架构。
* [bemi](https://github.com/BemiHQ/bemi) - PostgreSQL 的自动数据更改跟踪
* [ERAlchemy](https://github.com/Alexis-benoist/eralchemy) - ERAlchemy 从数据库生成实体关系 (ER) 图。
* [flyway](https://flywaydb.org/) - Postgres 等的架构迁移工具。
* [GatewayD](https://github.com/gatewayd-io/gatewayd) - 用于构建数据驱动应用程序的云原生数据库网关和框架。就像数据库的 API 网关一样。
* [Greenmask](https://github.com/GreenmaskIO/greenmask) - 适用于 MySQL 和 PostgreSQL 的数据库匿名化和合成数据生成工具。
* [Hasura GraphQL Engine](https://github.com/hasura/graphql-engine) - Postgres 上超快、即时的实时 GraphQL API 具有细粒度的访问控制，还可触发数据库事件的 Webhooks。
* [ldap2pg](https://github.com/dalibo/ldap2pg) - 同步 YML 和 LDAP 中的角色和权限。
* [migra](https://github.com/djrobstep/migra) - 与 diff 类似，但适用于 Postgres 模式。
* [mysql-postgresql-converter](https://github.com/lanyrd/mysql-postgresql-converter) - Lanyrd 的 MySQL 到 PostgreSQL 转换脚本。
* [NServiceBus.Transport.PostgreSql](https://github.com/Particular/NServiceBus.SqlServer) - NServiceBus.Transport.PostgreSql 库允许 .NET 开发人员[使用 PostgreSQL 数据库作为消息代理](https://docs.pspecial.net/transports/postgresql)。 （商业软件）
* [ora2pg](http://ora2pg.darold.net) - 用于将 Oracle 数据库模式导出到 PostgreSQL 兼容模式的 Perl 模块。
* [pg\_activity](https://github.com/dalibo/pg_activity) - 用于 PostgreSQL 服务器活动监控的顶级应用程序。
* [pg-formatter](https://github.com/gajus/pg-formatter) - PostgreSQL SQL 语法美化器 (Node.js)。
* [pg-safe-migrate](https://github.com/defnotwig/pg-safe-migrate) - 安全第一的 Node.js 迁移引擎，具有咨询锁、SHA-256 漂移检测和 10 条内置 PostgreSQL lint 规则。
* [pganalyze](https://pganalyze.com) - PostgreSQL 性能监控（商业软件）。
* [pgbadger](https://github.com/darold/pgbadger) - 快速 PostgreSQL 日志分析器。
* [PgBouncer](http://www.pgbouncer.org/) - PostgreSQL 的轻量级连接池。
* [pgCenter](https://github.com/lesovsky/pgcenter) - 为各种统计、管理任务、重新加载服务、查看日志文件以及取消或终止数据库后端提供方便的界面。
* [pg_chameleon](https://github.com/the4thdoctor/pg_chameleon) - 从 MySQL 到 PostgreSQL 的实时副本，具有可选的类型覆盖迁移和迁移功能。
* [pgclimb](https://github.com/lukasmartinelli/pgclimb) - 将 PostgreSQL 中的数据导出为不同的数据格式。
* [pg_docs_bot](https://github.com/mchristofides/pg_docs_bot/) - 用于将 PostgreSQL 文档链接重定向到当前版本的浏览器扩展。
* [pgfutter](https://github.com/lukasmartinelli/pgfutter) - 以简单的方式将 CSV 和 JSON 导入 PostgreSQL。
* [PGInsight](http://pginsight.io/) - CLI 工具可轻松深入了解 PostgreSQL 数据库。
* [pg_insights](https://github.com/lob/pg_insights) - 用于监控 Postgres 数据库运行状况的便捷 SQL。
* [pgloader](https://github.com/dimitri/pgloader) - 使用 COPY 流协议将数据加载到 PostgreSQL 中，并使用单独的线程来读取和写入数据。
* [pgMonitor](https://github.com/CrunchyData/pgmonitor) - Postgres 指标收集和可视化可以部署到裸机、虚拟机或 Kubernetes。
* [pgpool-II](https://www.pgpool.net/mediawiki/index.php/Main_Page) - 提供连接池、复制、负载平衡和限制超出连接的中间件。
* [pgspot](https://github.com/timescale/pgspot) - 发现 PostgreSQL 扩展脚本中的漏洞。
* [pg-spot-operator](https://github.com/pg-spot-ops/pg-spot-operator) - 在廉价的 AWS Spot VM 上运行有状态 Postgres 的守护进程
* [pgsync](https://github.com/ankane/pgsync) - 将 PostgreSQL 数据同步到本地计算机的工具。
* [PGXN client](https://github.com/pgxn/pgxnclient) - 与 PostgreSQL 扩展网络交互的命令行工具
* [postgresql-metrics](https://github.com/spotify/postgresql-metrics) - 为 PostgreSQL 数据库提取并提供指标的工具。
* [PostgREST](https://github.com/PostgREST/postgrest) - 从任何现有的 PostgreSQL 数据库提供完全 RESTful API。
* [pREST](https://github.com/prest/prest) - 从任何 PostgreSQL 数据库 (Golang) 提供 RESTful API
* [PostGraphile](https://github.com/graphile/postgraphile) - 适用于 PostgreSQL 数据库的即时 GraphQL API 或 GraphQL 架构
* [yoke](https://github.com/nanopack/yoke) - 具有自动故障转移和自动集群恢复功能的 PostgreSQL 高可用性集群。
* [pglistend](https://github.com/kabirbaidhya/pglistend) - 一个轻量级的 PostgresSQL `LISTEN`/`NOTIFY` 守护进程，构建在 `node-postgres` 之上。
* [ZSON](https://github.com/postgrespro/zson) - 用于透明 JSONB 压缩的 PostgreSQL 扩展
* [pg_bulkload](http://ossc-db.github.io/pg_bulkload/index.html) - 它是 PostgreSQL 的高速数据加载实用程序。
* [pg_migrate](https://github.com/jwdeitch/pg_migrate) - 管理 PostgreSQL 代码库并使 VCS 变得简单。
* [pg_timetable](https://github.com/cybertec-postgresql/pg_timetable) - PostgreSQL 的高级作业调度程序。
* [sqitch](https://github.com/sqitchers/sqitch) - 用于管理版本化架构部署的工具
* [pgmigrate](https://github.com/yandex/pgmigrate) - 用于发展架构迁移的 CLI 工具，由 Yandex 开发。
* [pgcmp](https://github.com/cbbrowne/pgcmp) - 比较数据库模式的工具，能够接受一些持久的差异
* [pg-differ](https://github.com/multum/pg-differ) - 用于轻松初始化/更新 PostgreSQL 表结构的工具，迁移替代方案 (Node.js)。
* [Qail](https://github.com/qail-io/qail) - 用于 PostgreSQL 的 rust-first 类型 AST 管道，具有编译时查询检查和内置租户范围。
* [sqlcheck](https://github.com/jarulraj/sqlcheck) - 自动检测常见的 SQL 反模式。此类反模式通常会减慢查询速度。因此，解决这些问题将有助于加快查询速度。
* [postgres-checkup](https://gitlab.com/postgres-ai/postgres-checkup) - 新一代诊断工具，允许用户收集 Postgres 数据库健康状况的深入分析。
* [Pyrseas](https://github.com/perseas/Pyrseas) - Postgres 数据库架构版本控制。
* [ScaffoldHub.io](https://scaffoldhub.io) - 使用 Angular、Vue 或 React（商业软件）生成全栈 PostgreSQL 应用程序。
* [planter](https://github.com/achiku/planter) - 从 PostgreSQL 表生成 PlantUML ER 图文本描述
* [pgroll](https://github.com/xataio/pgroll) - Postgres 的零停机、可逆模式迁移
* [RegreSQL](https://github.com/dimitri/regresql) - 用于构建、维护和执行 SQL 查询回归测试套件的工具。
* [diesel-guard](https://github.com/ayarotsky/diesel-guard) - Diesel 和 SQLx 中危险的 Postgres 迁移模式的 Linter。

### 语言绑定
* Common Lisp：[后现代](https://github.com/marijnh/Postmodern)
* Clojure：[clj-postgresql](https://github.com/remodoy/clj-postgresql)
* Elixir：[postgrex](https://github.com/elixir-ecto/postgrex)
* 转到：[pq](https://github.com/lib/pq)、[pgx](https://github.com/jackc/pgx)、[go-pg](https://github.com/go-pg/pg)
* Haskell：[postgresql-simple](http://hackage.haskell.org/package/postgresql-simple)
* Java：[PostgreSQL JDBC 驱动程序](https://jdbc.postgresql.org/)、[Vert.x PostgreSQL 客户端](https://vertx.io/docs/vertx-pg-client/java/)
* Lua: [luapgsql](https://github.com/arcapos/luapgsql)
* .Net/.Net Core: [Npgsql](https://github.com/npgsql/npgsql)
* 节点: [node-postgres](https://github.com/brianc/node-postgres), [pg-promise](https://github.com/vitaly-t/pg-promise), [pogi](https://github.com/holdfenytolvaj/pogi), [slonik](https://github.com/gajus/slonik), [postgres](https://github.com/porsager/postgres)
* Perl：[DBD-Pg](https://metacpan.org/pod/distribution/DBD-Pg/Pg.pm)
* PHP: [Pomm](http://www.pomm-project.org), [pecl/pq](https://github.com/m6w6/ext-pq)
* Python：[psycopg2](https://pypi.org/project/psycopg2/)、[asyncpg](https://pypi.org/project/asyncpg/)、[pg8000](https://pypi.org/project/pg8000/)
* R: [RPostgres](https://github.com/r-dbi/RPostgres), [RPostgreSQL](https://github.com/tomoakin/RPostgreSQL)
* 红宝石：[pg](https://github.com/ged/ruby-pg)
* Rust: [rust-postgresql](https://github.com/sfackler/rust-postgres), [pgx](https://github.com/tcdi/pgx), [wtx](https://github.com/c410-f3r/wtx)
* TypeScript：[zapatos](https://github.com/jawj/zapatos)
* Zig: [pg.zig](https://github.com/karlseguin/pg.zig), [qail-zig](https://github.com/qail-io/qail-zig)

### PaaS *（PostgreSQL 即服务）*
* [Aiven PostgreSQL](https://aiven.io/postgresql) - PostgreSQL 作为 AWS、Azure、DigitalOcean、Google Cloud 和 UpCloud 中的服务；计划范围从 19 美元/月的单节点实例到大型高可用设置，免费试用两周。
* [Amazon RDS for PostgreSQL](https://aws.amazon.com/rds/postgresql/) - 适用于 PostgreSQL 的 Amazon Relational Database Service (RDS)
* [Azure Database for PostgreSQL](https://azure.microsoft.com/en-us/services/postgresql/) - Azure Database for PostgreSQL 提供完全托管、企业就绪的社区 PostgreSQL 数据库即服务。它提供内置 HA、弹性扩展以及与 Azure 生态系统的本机集成。
* [Crunchy Bridge](https://www.crunchydata.com/products/crunchy-bridge/) - 由 Postgres 专家全面管理的 Postgres。适用于所有主要云提供商：Amazon AWS、Google GCP、Microsoft Azure。没有锁定，拥有完整的超级用户支持。
* [Database Labs](https://www.databaselabs.io) - 只需几分钟即可获得可用于生产的云 PostgreSQL 服务器，每月 20 美元起，包括备份、监控、补丁和 24/7 技术支持。
* [DigitalOcean Managed Databases](https://www.digitalocean.com/products/managed-databases/) - 完全托管的 PostgreSQL 数据库。没有免费计划。起价为 15 美元/月。每日备份和时间点恢复。具有自动故障转移功能的备用节点。
* [Google Cloud SQL for PostgreSQL](https://cloud.google.com/sql/docs/postgres/) - 完全托管的数据库服务，让您可以轻松地在 Google Cloud Platform 上设置、维护、管理和管理 PostgreSQL 关系数据库。
* [Heroku Postgres](https://elements.heroku.com/addons/heroku-postgresql) - 从免费到大型的计划，由 PostgreSQL 专家运营。不需要在 Heroku 上运行您的应用程序。免费计划包括 10,000 行、20 个连接、最多两个备份，并具有 PostGIS 支持。
* [OVHcloud Cloud Databases](https://www.ovhcloud.com/en/public-cloud/databases/) - 高度可用、可扩展且安全的 PostgreSQL。每日备份与时间点恢复，无锁定，免费传入和传出流量。
* [Render Managed PostgreSQL](https://render.com/docs/databases) - 安全、可靠且完全不受干涉的托管 PostgreSQL。所有计划均包含静态加密、自动备份和可扩展 SSD 存储。 256MB RAM 和 1GB 存储空间的套餐起价为每月 7 美元（前 90 天免费）。
* [ScaleGrid PostgreSQL DBaaS](https://scalegrid.io/postgresql.html) - 完全托管的 PostgreSQL 托管具有高可用性、专用服务器以及对 #1 多云 Amazon RDS 替代方案的超级用户控制。
* [Scaleway Managed Database](https://www.scaleway.com/en/database/) - 完全托管的 PostgreSQL 数据库，具有 HA、扩展和自动备份功能，托管在欧盟。每月 10 欧元起。
* [Supabase](https://www.supabase.com) - 完全托管的 Postgres，具有只读副本、时间点恢复、支持包、基于浏览器的 GUI 和慷慨的免费套餐。
* [Neon](https://neon.tech) - 完全托管的无服务器 PostgreSQL。 Neon 将存储和计算分开，为现代开发人员提供无服务器、分支、无底存储等功能。
* [Nile](https://www.thenile.dev/) - 完全托管的 PostgreSQL。 Nile 将存储与计算分离，并对租户进行虚拟化，以快速、安全且无限规模地交付多租户 AI 应用程序。免费套餐提供无限的数据库。
* [PlanetScale](https://planetscale.com/postgres) - PlanetScale for Postgres 提供基于现代云基础设施构建的完全托管、高可用性 PostgreSQL 数据库集群。
* [Vela](https://vela.run) - 专为现代人工智能应用程序构建的基于 Postgres 的后端即服务。提供即时数据库分支和克隆、类似生产的测试环境以及无服务器扩展。
* [Thalassa Cloud DBaaS](https://thalassa.cloud/products/databases/postgresql/) - 完全托管的 PostgreSQL 数据库、多可用区、自动备份，托管在荷兰。

### Docker 镜像
* [citusdata/citus](https://hub.docker.com/r/citusdata/citus/) - 带有 citus 扩展的 Citus 官方图像。基于官方 Postgres 容器。
* [mdillon/postgis](https://hub.docker.com/r/mdillon/postgis/) - Postgres 9 上的 PostGIS 2.3。基于官方 Postgres 容器。
* [paradedb/paradedb](https://hub.docker.com/r/paradedb/paradedb/) - ParadeDB 是用于搜索和分析的 Postgres。基于带有 pg_search 扩展的官方 Postgres 容器。
* [postgres](https://hub.docker.com/_/postgres/) - 官方 postgres 容器（来自 Docker）

### 库伯内斯
* [Crunchy Operator](https://github.com/CrunchyData/postgres-operator) - 适用于 Kubernetes 的生产 PostgreSQL，从高可用性 Postgres 集群到全面的数据库即服务。
* [Fujitsu Enterprise Postgres for Kubernetes](https://www.postgresql.fastware.com/) - OpenShift 容器平台上的企业级 PostgreSQL（商业软件）。
* [Kubegres Operator](https://github.com/reactive-tech/kubegres) - Kubegres 是一个 Kubernetes 操作器，允许部署一个或多个 PostgreSql 实例集群并管理数据库复制、故障转移和备份。
* [StackGres Operator](https://github.com/ongres/stackgres/) - Kubernetes 上的全栈 PostgreSQL。
* [Zalando Operator](https://github.com/zalando/postgres-operator) - 创建和管理在 Kubernetes 中运行的 PostgreSQL 集群。
* [CloudNativePG operator](https://github.com/cloudnative-pg/cloudnative-pg) - 一个综合平台，旨在无缝管理 Kubernetes 环境中的 PostgreSQL 数据库。
* [KubeDB operator](https://kubedb.com/) - 在 Kubernetes（商业软件）上运行生产级数据库。
* [Percona PostgreSQL Operator](https://github.com/percona/percona-postgresql-operator) - Percona Operator for PostgreSQL 基于 Crunchy Data 运算符。
* [Percona Everest Operator](https://github.com/percona/everest-operator) - Everest Operator 是一个 Kubernetes Operator，负责管理 MySQL、MongoDB 和 PostgreSQL 数据库的生命周期。它在底层利用了 Percona 的 Kubernetes Operators for MySQL、MongoDB 和 PostgreSQL，但提供了统一的 API 和单一管理平台来管理所有三种数据库类型。

## 资源

### 教程
* [Backup and recover a PostgreSQL DB using wal-e](https://coderwall.com/p/cwe2_a/backup-and-recover-a-postgres-db-using-wal-e) - 有关使用 wal-e 在 PostgreSQL 中设置连续归档的教程。
* [Operations cheat sheet](https://wiki.postgresql.org/wiki/Operations_cheat_sheet) - 来自 PostgreSQL Wiki 的操作备忘单。
* [PG Casts](https://www.pgcasts.com) - Hashrocket 提供的每周免费 PostgreSQL 截屏视频。
* [Postgres Guide](http://postgresguide.com/) - 指南旨在帮助初学者和经验丰富的用户查找特定技巧并探索 PostgreSQL 中可用的工具。
* [PostgreSQL Exercises](https://pgexercises.com/) - 通过练习轻松学习 PostgreSQL 的网站。
* [tutorialspoint PostgreSQL tutorial](http://www.tutorialspoint.com/postgresql/) - 非常广泛的 PostgreSQL 教程集合
* [postgresDBSamples](https://github.com/morenoh149/postgresDBSamples) - 示例 postgres 模式的集合
* [PostgreSQL Primer for Busy People](https://zaiste.net/posts/postgresql-primer-for-busy-people/) - PostgreSQL 中最常用命令的集合
* [pg-utils](https://github.com/dataegret/pg-utils) - Data Egret 提供的有用的 DBA 工具
* [pagila](https://github.com/xzilla/pagila) - Pagila，Postgres 示例数据库
* [SQL Syntax Cheat Sheet](https://github.com/mergisi/sql-syntax-cheat-sheet) - 全面的 SQL 语法参考，涵盖窗口函数、CTE 和 PostgreSQL 特定语法（UPSERT、JSON 查询、数组操作）。

### 博客
* [Planet PostgreSQL](https://planet.postgresql.org/) - PostgreSQL 的博客聚合服务。
* [Andrew Dunstan 的 PostgreSQL 和技术博客](http://adpgtech.blogspot.com/search/label/PostgreSQL/)
* [Bruce Momjian 的 PostgreSQL 博客](https://momjian.us/main/blogs/pgblog.html)
* [Craig Kerstiens PostgreSQL posts](http://www.craigkerstiens.com/categories/postgres/) - 关于 PostgreSQL 炫酷功能、提示和技巧的一组帖子。
* [Database Soup](http://www.databasesoup.com/search/label/postgresql/) - 乔什·伯库斯的博客。
* [迈克尔·帕奎尔的博客](https://paquier.xyz/)
* [Percona 的 PostgreSQL 博客文章](https://www.percona.com/blog/category/postgresql/)
* [罗伯特·哈斯的博客](http://rhaas.blogspot.com/search/label/postgresql/)
* [select * from depesz;](https://www.depesz.com/tag/postgresql/) - 休伯特·卢巴切夫斯基的博客。
* [Metis Blog](https://www.metisdata.io/blog) - 关于 PostgreSQL、SQL 数据库、性能和调优的帖子集。
* [Digoal的PostgreSQL及技术博客（中文）](https://github.com/digoal/blog/blob/master/README.md)
* [Pigsty blog / PostgreSQL](https://pigsty.io/blog/pg/) - PIGSTY 作者的博客，其中包含有关 PostgreSQL（以及数据库和云基础设施）的富有洞察力的文章。
* [BigData Boutique Blog / PostgreSQL](https://bigdataboutique.com/blog/tagged/postgresql) - BigData Boutique 团队的博客，主要关注分析）。

### 书籍
* [PostgreSQL 错误以及如何避免它们](https://www.manning.com/books/postgresql-mistakes-and-how-to-avoid-them)
* [The Internals of PostgreSQL](https://www.interdb.jp/pg/index.html) - 铃木博信的免费电子书
* [PostgreSQL 14 Internals](https://postgrespro.com/community/books/internals) - 叶戈尔·罗戈夫 (Egor Rogov) 的免费电子书
* [Lift the Elephant](https://leanpub.com/lift-the-elephant) - 在生产中扩展 Postgres 的实用指南，涵盖调优、连接池、分区和高可用性。


### 文档
* [Wiki](https://wiki.postgresql.org/wiki/Main_Page) - 用户文档、操作方法和技巧
* [pgPedia](https://pgpedia.info/) - 与 postgreSQL 相关的百科全书。
* [create_pg_super_document](https://ryogrid.github.io/create_pg_super_document/index.html) - 旨在使用 AI 代理为 PostgreSQL 代码库中的所有符号生成文档的项目

### 时事通讯

* [Postgres Weekly](https://postgresweekly.com/) - 包含与 PostgreSQL 相关的文章、新闻和存储库的每周新闻通讯。
* [pgMustard newsletter](https://www.pgmustard.com/newsletter) - 包含 Postgres 性能文章和视频的每月通讯。
* [pgsql-hackers Weekly Digest](https://ryogrid.net/pgsql-hackers-digest/) - pgsql-hackers 邮件列表的每周摘要，提供活动线程列表、线程摘要等。

### 播客
* [PostgresFM](https://postgres.fm/) - 关于 Postgres 主题的每周讨论。
* [Scaling Postgres](https://www.scalingpostgres.com/) - 每周汇总 PostgreSQL 相关内容。
* [Path to Citus Con](https://www.citusdata.com/podcast/path-to-citus-con/) - 每月对 Postgres 世界中的人们进行采访。

### 视频
* [Citus Data Youtube channel](https://www.youtube.com/channel/UC8jpoK1BqQhDh6HDGFnM_DA/videos) - Citus 相关视频
* [EnterpriseDB Youtube channel](https://www.youtube.com/channel/UCkIPoYyNr1OHgTo0KwE9HJw) - EnterpriseDB 相关视频
* [Postgres Conference Youtube channel](https://www.youtube.com/channel/UCsJkVvxwoM7R9oRbzvUhbPQ/videos) - 会议视频
* [Scaling Postgres](https://www.scalingpostgres.com/) - Creston Jamison 的 Postgres 视频博客系列
* [PostgresTV Youtube channel](https://www.youtube.com/@PostgresTV) - Postgres 讲座、黑客会议、访谈和播客节目

### 社区
* [Mailing lists](https://www.postgresql.org/list/) - Postgres 的官方邮件列表，提供支持、外展等服务。 Postgres 社区的主要沟通渠道之一。
* [Reddit](https://www.reddit.com/r/PostgreSQL/) - 拥有超过 12000 名用户的 PostgreSQL 用户 Reddit 社区
* [Slack](https://pgtreats.info/slack-invite) - 拥有超过 20,000 名成员的 Postgres Slack 工作区
* Telegram - 多个不同语言的 PostgreSQL 群组：[俄语](https://t.me/pgsql) >4200 人，[巴西葡萄牙语](https://t.me/postgresqlbr) >2300 人，[印度尼西亚语](https://t.me/postgresql_id) ~1000 人，[英语](https://t.me/postgreschat) >750 人
* [#postgresql on Freenode](https://webchat.freenode.net/#postgresql) - Freenode 上最受欢迎的关于 Postgres 的 IRC 频道，拥有超过 1000 个用户
* [Discord](https://discord.gg/bW2hsax8We) - 拥有超过 6000 名成员的 Postgres Discord 服务器

### 路线图
* [PostgreSQL Roadmap](https://roadmap.sh/postgresql-dba) - 提供 PostgreSQL 逐步指南的路线图。

### 外部列表
* [Wikipedia admin tools list](https://en.wikipedia.org/wiki/Comparison_of_database_tools) - 维基百科上数据库管理工具的比较
* [PostgreSQL Wiki GUI tools list](https://wiki.postgresql.org/wiki/Community_Guide_to_PostgreSQL_GUI_Tools) - PostgreSQL GUI 工具社区指南
* [PostgreSQL Wiki Foreign Data Wrappers list](https://wiki.postgresql.org/wiki/Foreign_data_wrappers) - 外部数据包装器
