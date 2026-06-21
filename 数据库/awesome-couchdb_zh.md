<p>
  <br>
  <img width="300" src="https://rawgit.com/quangv/awesome-couchdb/master/logo--couch.png" alt="awesome couchdb logo">
  <br>
</p>

# 很棒的 CouchDB [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

> CouchDB 的精选元资源和最佳实践列表。

**[CouchDB](http://couchdb.apache.org/)** 是一个面向文档的同步 NoSQL 数据库。

欢迎请求。

## 内容
- [新闻和博客文章](#news--blog-posts)
- [模式和最佳实践](#patterns--best-practices)
  - [Map/Reduce](#mapreduce)
  - [Joins](#joins)
  - [文档版本控制](#document-versioning)
- [Blogs](#blogs)
- [Docs](#docs)
- [Books](#books)
- [Videos](#videos)
- [Libraries](#libraries)
- [Community](#community)
  - [邮件列表](#mailing-list)
  - [Companies](#companies)
    - [Hosting](#hosting)
  - [相关项目](#related-projects)
- [Misc/Technical](#misctechnical)
  - [Attachments](#attachments)
  - [Backups](#backups)
  - [CouchApps](#couchapps)
  - [Scaling](#scaling)
- [资源列表](#resource-lists)
- [License](#license)

## 新闻和博客文章

- [Rust 中的 MiniCouchDB](https://www.garrensmith.com/blogs/mini-couch-hack-week)
- [CouchDB 3.0之路：为4.0做准备](https://blog.couchdb.org/2020/02/26/the-road-to-couchdb-3-0-prepare-for-4-0/)_(02-26-2020)_

## 模式和最佳实践

- [Best Practices](http://ehealthafrica.github.io/couchdb-best-practices/) - 最佳实践，非洲电子医疗。
- [PouchDB 的分页策略 ](https://pouchdb.com/2014/04/14/pagination-strategies-with-pouchdb.html)
- [使用 PouchDB 编写更好代码的 12 个专业技巧](https://pouchdb.com/2014/06/17/12-pro-tips-for-better-code-with-pouchdb.html)
- [Linux 调优以获得更好的 CouchDB 性能](https://github.com/assafmo/couchdb-linux-performance)


### 映射/缩小

- [PouchDB - 二级索引](https://pouchdb.com/2014/05/01/secondary-indexes-have-landed-in-pouchdb.html)
- [Cloudant - MapReduce Primer](https://cloudant.com/blog/mapreduce-from-the-basics-to-the-actually-useful/#.WIDBfRsrKUl) - 关于reduce、group、group_level 的精彩介绍。
- [Using View Collation](http://docs.couchdb.org/en/2.0.0/couchapp/views/joins.html#using-view-collation) - 用于数据连接的索引映射（发出）。
- [Views Collation](http://docs.couchdb.org/en/2.0.0/couchapp/views/collation.html) - 有关“查看排序规则”的更多文档。
- [Cloudant - MapReduce and the Secondary Index (Video)](https://developer.ibm.com/clouddataservices/docs/cloudant/get-started/mapreduce-and-the-secondary-index/) - 这里有关于 mapReduce、二级索引和复杂键的精彩视频。
- [Cloudant - Design Documents](https://docs.cloudant.com/design_documents.html) - Cloudant 的文档也是学习 CouchDB 概念的重要资源。
- [Cloudant - Design Document Management](https://docs.cloudant.com/design_document_management.html) - 如何管理生产中的设计文档变更。


### 加入

- [Joins with Views](http://docs.couchdb.org/en/2.0.0/couchapp/views/joins.html#joins-with-views) - 必须阅读以了解对 CouchDB/PouchDB 进行有效连接的方法。
- [Grouping related documents together in Cloudant](https://docs.cloudant.com/transactions.html) - 一种利用 CouchDB 高可用性特性的方法。


### 文档版本控制

- [文档修订（来自 wiki）](https://wiki.apache.org/couchdb/Document_revisions?action=show&redirect=DocumentRevisions)
- [简单的文档版本控制](http://web.archive.org/web/20100701165612/http://blog.couch.io/post/632718824/simple-document-versioning-with-couchdb)


## 博客

- [官方博客](https://blog.couchdb.org/)


## 文档

- [官方文档](http://docs.couchdb.org/)
- [FAQ (old wiki)](https://wiki.apache.org/couchdb/Frequently_asked_questions) - 似乎比[新维基](https://cwiki.apache.org/confluence/display/COUCHDB/Frequently+Asked+Questions)有更多的常见问题解答。

## 书籍

- [The Definitive Guide](http://guide.couchdb.org/) - CouchDB 的_“狗”_ 书。
- [维基百科上的书籍列表](https://cwiki.apache.org/confluence/display/COUCHDB/Books)


## 视频

- [10 Common Misconceptions](https://www.youtube.com/watch?v=BKQ9kXKoHS810) - 本次[会议](http://conf.couchdb.org/) 的更多视频。
- [The NoSQL Tapes](http://nosqltapes.com) - CouchDB 在[第 5 卷 - CouchDB](http://nosqltapes.com/video/hoffman-and-kocoloski-on-cloudant-and-couchdb)、[第 8 卷 - MapReduce](http://nosqltapes.com/video/understand-mapreduce-with-mike-miller) 上进行了讨论。
- [Scaling Out with BigCouch](http://www.oreilly.com/pub/e/1760) - O'Reilly 关于使用 BigCouch 进​​行扩展的视频。
- [IBM - 新构建者网络研讨会系列](https://event.on24.com/eventRegistration/EventLobbyServlet?target=reg20.jsp&partnerref=cdc&eventid=1240121&sessionid=1&key=9E23B44802902EAD0BB2603F0434742E&regTag=35370&sourcepage=register)

## 图书馆

- [Jaki](https://github.com/pandeiro/jaki) - 一个简单的 ClojureScript CouchDB 客户端

## 社区

- [IRC](http://webchat.freenode.net/?channels=couchdb) - `irc://irc.freenode.net/couchdb`
- [Apache CouchDB Conf](http://conf.couchdb.org/) - 很多视频链接。
- [章程](http://couchdb.apache.org/bylaws.html), [会议纪要](https://whimsy.apache.org/board/minutes/CouchDB.html)


### 邮件列表

> -dev是couchdb开发者聊天的地方，-user是couchdb用户聊天的地方
> 并且有一些串扰ofc
> 如果您正在谈论对 couchdb 本身的更改，则 -dev 是合适的（“开发人员”并不意味着您必须有提交位或任何内容） -rnewson

- [邮件列表](https://mail-archives.apache.org/mod_mbox/#couchdb)
- [邮件列表说明](http://svn.apache.org/repos/asf/couchdb/site/htdocs/community/lists.html?p=900000)
- [Grokbase](http://grokbase.com/s/couchdb) - 类似于 [Stack Overflow](http://stackoverflow.com/questions/tagged/couchdb) 的界面中的邮件列表。


[:star2:**** ***惊人*** **CouchDB 提交者** *和* **项目经理** :heart_eyes_cat:](http://people.apache.org/committers-by-project.html#couchdb)


### 公司

- [eHealth Africa](https://github.com/eHealthAfrica) - CouchDB 的大用户，请查看他们的[最佳实践](https://github.com/eHealthAfrica/couchdb-best-practices)。


#### 托管

- [Cloudant](https://cloudant.com/) - 分布式数据库即服务 (DBaaS)。
- [Fly.io](https://fly.io) 使用此[指南](https://www.canrau.com/en/fly-couchdb) 进行托管
- [Bitnami Launchpad for Google Cloud Platform](https://bitnami.com/stack/couchdb/cloud/google) - 在 Google Cloud Platform 上托管 CouchDB。


### 相关项目

- [PouchDB](https://pouchdb.com/) - 袖珍数据库。
- [FoundationDB](https://www.foundationdb.org/) - CouchDB 4.0 将利用 FoundationDB。
- [Hoodie](http://hood.ie/) - 离线优先应用程序的后端。
- [Couchbase](https://www.couchbase.com/) - NoSQL 数据库。
  - [Migrating from Apache CouchDB](https://docs.couchbase.com/server/current/install/migrate-couchdb.html) - CouchDB 和 CouchBase 的比较
- [RxDB](https://rxdb.info/) - JavaScript 应用程序的 NoSQL 数据库。 RxDB 提供了用于与任何 CouchDB 兼容端点以及自定义 GraphQL 端点进行实时复制的模块。


## 杂项/技术

- [Dynamo and CouchDB Clusters](https://web.archive.org/web/20160311144130/https://cloudant.com/blog/dynamo-and-couchdb-clusters/#.WIEp4xsrKUk) - 关于使用集群扩展 CouchDB 的文章。
- [Google’s paper on Sawzall](http://research.google.com/archive/sawzall.html) - 奇异的还原示例。
- [What Every Developer Should Know About CouchDB](http://www.dimagi.com/blog/what-every-developer-should-know-about-couchdb/) - 关于经验教训的文章。
- [CouchDB 最大数据库大小](http://www.nosql.se/2011/09/couchdb-maximum-database-size/)
- [NOSQL 模式](http://horicky.blogspot.com/2009/11/nosql-patterns.html)
- [git、Clojure 和 CouchDB 中的持久树](https://eclipsesource.com/blogs/2009/12/13/persistent-trees-in-git-clojure-and-couchdb-data-structure-convergence/)
- [CouchDB - JSON、B 树和 REST，天哪！](https://pozorvlak.livejournal.com/176385.html)

### 附件

- [PouchDB - Attachments are overrated](https://pouchdb.com/2014/06/17/12-pro-tips-for-better-code-with-pouchdb.html) - _“更新：自从写这篇文章以来，PouchDB 中附件的稳定性和性能已大大提高。...”_
- [Cloudant - 附件性能注意事项](https://docs.cloudant.com/attachments.html#performance-considerations)
- [Are attachments duplicated for each revision?](http://grokbase.com/t/couchdb/user/14a1phbzrb/are-attachments-duplicated-for-each-revision-as-well) - 关于跨修订版附件的邮件列表讨论。


### 备份

- [Simple CouchDB and Cloudant Backup](https://developer.ibm.com/clouddataservices/2016/03/22/simple-couchdb-and-cloudant-backup/) - IBM 关于备份的文章。
- [Cloudant Backup Guide](https://docs.cloudant.com/backup-guide.html) - 有关备份的 Cloudant 文档。


### 沙发应用程序

- [CouchApps 列表](https://couchapp.readthedocs.io/en/latest/user/list-of-couchapps.html)
- [Ddoc Lab](http://ddoc.me/) - 直接在浏览器中创建 couchapps 和 CouchDB 设计文档。


### 缩放

- [Bitnami CouchDB](https://bitnami.com/stack/couchdb) - Bitnami 使在云中运行 CouchDB 变得容易。


## 资源列表

- [官方 CouchDB 维基](https://cwiki.apache.org/confluence/display/COUCHDB/Apache+CouchDB+Wiki)
- [Official CouchDB Wiki (old)](https://wiki.apache.org/couchdb/) - 有些东西还没有出现在新的维基上。
- [Cloudant Official Guides](https://docs.cloudant.com/guides.html) - 适用于 CouchDB。
- [CouchDB 客户端列表](https://cwiki.apache.org/confluence/display/COUCHDB/CouchDB+clients)
- [CouchDB 有用实用程序列表](https://cwiki.apache.org/confluence/display/COUCHDB/Useful+utilities)
- [旧 Wiki 的相关项目列表](https://wiki.apache.org/couchdb/Related_Projects)

## 许可证
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/by.svg" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.
