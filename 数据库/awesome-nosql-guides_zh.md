# 很棒的 NoSQL 指南 [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> 关于*使用*NoSQL 数据库以及决定使用数据库时需要查找的内容的精选资源和链接列表。

NoSQL 数据库的基本定义可以在维基百科上找到：

> “NoSQL（最初指‘非 SQL’或‘非关系’）数据库提供了一种存储和检索数据的机制，该机制以关系数据库中使用的表格关系以外的方式建模。”

对于实际的NoSQL数据库，你可以去
[此处](https://github.com/sindresorhus/awesome#databases)，
[此处](https://hostingdata.co.uk/nosql-database/)，
[此处](https://db-engines.com/en/ranking),
[此处](https://dbdb.io/),
[此处](https://github.com/igorbarinov/awesome-data-engineering#databases)，或
[此处](https://github.com/kahun/awesome-sysadmin#nosql)。另外，不要与关系数据库管理系统 [NoSQL](http://www.strozzi.it/cgi-bin/CSA/tw7/I/en_US/nosql/Home%20Page) 混淆。


## 内容

- [NoSQL 概述](#overview-of-nosql)
- [数据结构和建模](#data-structures-and-modeling)
- [CAP/布鲁尔定理的权衡](#trade-offs-in-capbrewers-theorem)
- [众包信息](#crowd-sourced-information)
- [图数据库](#graph-databases)
- [批评与辩论](#criticisms-and-debates)
- [Miscellaneous](#miscellaneous)


## NoSQL 概述

- [Introduction To NoSQL - Martin Fowler (54:52)](https://www.youtube.com/watch?v=qI_g07C_Q5I) - GOTO 2012 上的演讲对 NoSQL 数据库、NoSQL 数据库的类型、它们的历史、优缺点以及如何以及何时使用它们进行了精彩的介绍。
- [NoSQL Distilled](https://martinfowler.com/books/nosql.html) - 非常易于理解且价格实惠的书，描述了不同的 NoSQL 数据库，并帮助您决定使用 NoSQL 数据库是否适合您的项目。
- [Seven Databases in Song (1:43)](https://www.youtube.com/watch?v=jyx8iP5tfCI) - 2012 年的一首有趣的歌曲，关于七个（六个是 NoSQL）数据库，非常简洁地概述了它们各自的工作原理。
- [NoSQL Databases: a Survey and Decision Guidance (2016)](https://medium.baqend.com/nosql-databases-a-survey-and-decision-guidance-ea7823a822d) - “这个 NoSQL 工具箱使我们能够导出一个简单的决策树，以帮助从业者和研究人员根据中心应用程序需求筛选潜在的系统候选者”。
- [Data Management in the Cloud: Limitations and Opportunities (PDF)](http://www.cs.umd.edu/~abadi/papers/abadi-cloud-ieee09.pdf) - Abadi (2009) 讨论了云中数据管理和数据分析的局限性和机遇。
- [10 NoSQL Misconceptions](https://web.archive.org/web/20210701080816/https://www.dummies.com/programming/big-data/10-nosql-misconceptions/) - 关于 NoSQL 数据库的一些误解，涉及到什么是 NoSQL 数据库、ACID 合规性和安全性等主题。
- [10 Reasons Developers Love NoSQL](https://web.archive.org/web/20210701080841/https://www.dummies.com/programming/big-data/10-reasons-developers-love-nosql/) - 列出了为什么开发人员喜欢使用 NoSQL 数据库的十个论据。
- [Distribution, Data, Deployment: Software Architecture Convergence in Big Data Systems (PDF)](https://resources.sei.cmu.edu/library/asset-view.cfm?assetID=90909) - Gorton 和 Klein (2014) 发表论文讨论了处理大数据系统时在分布、数据和部署方面的软件工程问题。也可访问[此处](https://doi.org/10.1109/MS.2014.51)。
- [Use cases for NoSQL (2017)](https://stackoverflow.com/questions/2875432/use-cases-for-nosql) - Stack Overflow 上关于使用 NoSQL 数据库而非传统 SQL 数据库的最佳用例的讨论。
- [Five Common Data Stores and When to Use Them (2019)](https://shopify.engineering/five-common-data-stores-usage) - 文章介绍了五种常见的数据存储（关系数据库、非关系（“NoSQL”）数据库、键值存储、全文搜索引擎、消息队列）及其属性。
- [NoSQL Databases (PDF)](https://web.archive.org/web/20190927222738/https://www.christof-strauch.de/nosqldbs.pdf) - 一份 149 页的文档，概述了 NoSQL 数据库的动机和基本原理，以及这些数据库之间的常见概念、技术和模式；最后更新于 2011 年左右。
- [NoSQL Data Architecture & Data Governance: Everything You Need to Know (2018)](https://www.dataversity.net/nosql-data-architecture-data-governance-everything-need-know/) - 通过图表概述不同的 NoSQL 数据库架构。
- [NoSQL vs SQL: Demystifying NoSQL Databases (2019)](https://build5nines.com/nosql-vs-sql-demystifying-nosql-databases/) - NoSQL 数据库模式类型的总体概述和示例，同时涵盖 CAP 定理权衡。
- [Comparing Database Types: How Database Types Evolved to Meet Different Needs](https://www.prisma.io/dataguide/intro/comparing-database-types) - 很好地概述了数据库的总体情况以及 NoSQL 数据库类型的差异和有用之处。
- [The NoSQL Ecosystem](https://www.aosabook.org/en/nosql.html) - 本章是 Adam Marcus 在《开源应用程序的架构》一书中撰写的一章，主要面向需要更深入地了解这些系统的构建方式的系统架构师。
- [What is NoSQL - Amazon AWS](https://aws.amazon.com/nosql/) - 对 NoSQL 数据库及其与 SQL 数据库技术和术语的比较进行了高度概括。  用作 Amazon AWS 服务的登陆页面，用于键值 (Amazon DynamoDB)、文档 (Amazon DocumentDB)、图形 (Amazon Neptune)、内存 (Amazon ElastiCache) 和搜索引擎 (Amazon Elasticsearch) 数据库的 NoSQL 选项。
- [NoSQL vs. SQL: Important Differences & Which One Is Best for Your Project (2021) - Upwork](https://www.upwork.com/resources/nosql-vs-sql) - 解释比较 SQL 和 NoSQL 数据库，并就哪种数据库解决方案适合您的用例提供一些建议。
- [NoSQL Database Tutorial – Full Course for Beginners (2:54:52)](https://www.youtube.com/watch?v=xh4gy1lbL2k) - Ania Kubow 回顾了四种类型的 NoSQL 数据库，并提供了两个实践项目来试验所回顾的内容。


## 数据结构和建模

- [Structure Your Database](https://firebase.google.com/docs/database/android/structure-data) - 如果您的数据库使用 JSON，则构建数据的最佳实践（截至 2018 年）。
- [NoSQL Data Modeling Techniques (2012)](https://highlyscalable.wordpress.com/2012/03/01/nosql-data-modeling-techniques/) - 本文从数据建模的角度对 NoSQL 系统系列进行了简短的比较，并总结了几种常见的建模技术。
- [Data Models For MongoDB](https://www.mongodb.com/docs/manual/data-modeling/) - 特定于 MongoDB 的数据建模帮助，包括架构验证和示例模式。但是，这些概念可能会延续到其他文档 NoSQL 数据库。
- [Data Models Will Be Beautiful Again (2016)](https://tdwi.org/articles/2016/11/22/data-models-will-be-beautiful-again.aspx) - Essay 认为，尽管现有无模式数据库，但深思熟虑的数据库建模对于使用算法获取知识和见解非常重要。
- [Unified Data Modeling for Relational and NoSQL Databases](https://www.infoq.com/articles/unified-data-modeling-for-relational-and-nosql-databases/) - 使用统一数据建模技术管理 NoSQL 和关系数据库的解决方案。
- [Unifying Relational, Document, Graph, and Temporal Data Models](https://fauna.com/blog/unifying-relational-document-graph-and-temporal-data-models) - 用于在同一数据库中跨多个范例进行查询的模式。
- [How To Design Schema For Your NoSQL Database?](https://www.dataversity.net/how-to-design-schema-for-your-nosql-database/#) - 尽管人们普遍认为 NoSQL 是无模式的，但本文概述了 NoSQL 数据库如何遵循“查询驱动设计”以及这种模式灵活性的注意事项。
- [Best Practices for NoSQL Database Design (2012)](https://softwareengineering.stackexchange.com/q/158790/) - NoSQL 数据库设计的几个答案和链接。


## CAP/布鲁尔定理的权衡

- [Visual Guide To NoSQL Systems (2010)](http://blog.nahurst.com/visual-guide-to-nosql-systems) - 可视化显示不同 NoSQL 数据库之间 CAP 定理的权衡。
- [How to Choose The Right NoSQL Database For Your Application? (2018)](https://www.dataversity.net/choose-right-nosql-database-application/) - 回顾 CAP 定理并将常见的 NoSQL 数据库映射到 CAP 类别以帮助选择一个。


## 众包信息

- [/r/nosql](https://www.reddit.com/r/nosql/) - NoSQL 上的 Reddit 页面，介绍人们可能对 NoSQL 数据库存在的一般问题和讨论。
- [[nosql] 堆栈溢出标记](https://stackoverflow.com/tags/nosql/info)
- [Ask HN: Learning NoSQL, Papers and Books (2017)](https://news.ycombinator.com/item?id=15427932) - “您认为，要真正理解 NoSQL 主题，哪些论文和书籍是必需的？”
- [Difference Between Scaling Horizontally And Vertically For Databases](https://stackoverflow.com/q/11707879/6873133) - 数据库世界中讨论的常用术语，这里是其他人的答案。
- [NoSQL - Wikipedia](https://en.wikipedia.org/wiki/NoSQL) - 有关 NoSQL 数据库所有内容的维基百科条目。


## 图数据库

- [Graph Databases Use Cases](https://neo4j.com/use-cases/) - 尽管文档面向 Neo4j，但概念适用于所有图形数据库。
- [How The ICIJ Used Neo4j To Unravel The Panama Papers - Mar Cabra (32:02)](https://www.youtube.com/watch?v=S20XMQyvANY) - 了解图数据库如何成为探索与避税天堂公司相关的主要人物的关键，其中包括 50 多个国家的 140 名政治家。
- [Graph Databases For Beginners: The Basics Of Data Modeling](https://neo4j.com/blog/data-modeling-basics/) - 讨论数据建模的基础知识以及应采用哪种方法。
- [Graph Data Modeling Guidelines](https://neo4j.com/developer/guide-data-modeling/) - 与 Neo4j 直接相关，但可能适用于任何图形数据库。
- [Graph Data Modeling Visualize Structure and Meaning](http://www.graphdatamodeling.com) - 图数据建模简介，是对 Thomas Frisendal 所著的《NoSQL 和 SQL 的图数据建模》一书的介绍。


## 批评与辩论

- [Addressing the NoSQL Criticism (2011)](https://www.bradley-holt.com/2011/07/addressing-the-nosql-criticism/) - 反对对 NoSQL 数据库的九项批评，因为它们适用于 CouchDB，但也可能适用于其他数据库。
- [Thank You For Your Help NoSQL, But We Got It From Here (2020)](https://web.archive.org/web/20200913032621/https://www.memsql.com/blog/why-nosql-databases-wrong-tool-for-modern-application/) - 有人认为，考虑到扩展问题，NoSQL 数据库推动了数据库的发展，但现在 NewSQL 已经解决了这些问题（从 MemSQL 的角度来看）。
- [The Five Stages Of NoSQL (2016)](https://sookocheff.com/post/opinion/the-five-stages-of-nosql/) - 选择和使用 NoSQL 数据库的各个阶段反映了悲伤的五个阶段。
- [The Biggest Challenges Of Moving To NoSQL (2017)](https://dzone.com/articles/the-biggest-challenges-of-moving-to-nosql) - 速度、可扩展性和开发人员的喜悦是忍受迁移到 NoSQL 的挑战所获得的收益。


## 杂项

- [What As A NoSQL Database? Learn By Writing One In Python](https://web.archive.org/web/20201109032031/https://jeffknupp.com/blog/2014/09/01/what-is-a-nosql-database-learn-by-writing-one-in-python/) - 通过使用 Python 构建玩具数据库来学习 NoSQL 与 RDBMS 的优秀教程。
- [Dynamo Vs Cassandra : Systems Design Of NoSQL Databases](https://sujithjay.com/data-systems/dynamo-cassandra/) - 博客文章比较和对比两个著名的 NoSQL 数据库的系统设计。
- [Why You Should Build Your Wwn NoSQL Database](https://medium.com/@marceloboeira/why-you-should-build-your-own-nosql-database-9bbba42039f5) - NoSQL 数据库和架构范围的简要概述，以及使用 Crystal 编程语言的 NoSQL 数据库的非常基本的实现。
- [PostgreSQL, The NoSQL Database (2015)](https://www.linuxjournal.com/content/postgresql-nosql-database) - 有人认为 PostgreSQL 是 NoSQL 数据库的替代品，具有类似 NoSQL 的功能，使用其新功能，如从版本 9.4 开始的 HStore（键值存储）和 JSONB（基于文档）。

