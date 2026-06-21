# 很棒的 Drupal [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

[<img src="https://raw.githubusercontent.com/nirgn975/awesome-drupal/master/icon-drupal.png"align="right" width="90">](https://www.drupal.org)

> [Drupal](https://www.drupal.org) 是一个用 PHP 编写的免费开源 CMS，根据 GNU 通用公共许可证分发，为全球网站提供后端 - 范围从个人博客到公司、政治和政府网站。

您可能还喜欢 [awesome-php](https://github.com/ziadoz/awesome-php)。


## 内容

- [Tools](#tools)
- [Modules](#modules)
- [Documentation](#documentation)
- [Articles](#articles)
- [Distributions](#distributions)
- [Books](#books)
- [Videos](#videos)
- [Podcasts](#podcasts)
- [Community](#community)
- [Tips](#tips)


## 工具

- [Drupal Console](https://drupalconsole.com/) - Drupal CLI。生成样板代码、与 Drupal 交互和调试的工具。
- [DrupalVM](https://www.drupalvm.com/) - Drupal VM 使构建 Drupal 开发环境变得快速、简单，并向开发人员介绍了在虚拟机或 Docker 容器上进行 Drupal 开发的美妙世界（而不是基于旧的 MAMP/WAMP 开发）。
- [Drush](http://www.drush.org/) - Drush 是 Drupal 的命令行 shell 和 Unix 脚本接口。 Drush 核心附带了许多有用的命令，用于与模块/主题/配置文件等代码进行交互。同样，它运行 update.php，执行 sql 查询和数据库迁移，以及运行 cron 或清除缓存等其他实用程序。
- [Yo Hedley!](https://github.com/Gizra/generator-hedley) - 搭建无头 Drupal 后端、Angular 应用程序客户端和 Behat 测试的支架。
- [DDEV-Local](https://github.com/drud/ddev) - 一个基于 Docker 的工具，用于创建和管理本地开发环境。也可用于其他 PHP 应用程序。另请参阅[入门指南](https://www.drud.com/get-started/)


## 模块

- [Administration menu](https://www.drupal.org/project/admin_menu) - 提供独立于主题的管理界面（又名导航、后端）。
- [Administration views](https://www.drupal.org/project/admin_views) - 用实际视图替换管理概述/列表页面，以实现卓越的可用性。
- [Backup and Migrate](https://www.drupal.org/project/backup_migrate) - 备份和恢复 Drupal MySQL 数据库、代码和文件，或在环境之间迁移站点。备份和迁移支持 gzip、bzip 和 zip 压缩以及自动计划备份。
- [Better Exposed Filters](https://www.drupal.org/project/better_exposed_filters) - 备份和恢复 Drupal MySQL 数据库、代码和文件，或在环境之间迁移站点。备份和迁移支持 gzip、bzip 和 zip 压缩以及自动计划备份。
- [CKEditor - WYSIWYG HTML editor](https://www.drupal.org/project/ckeditor) - 该模块将允许 Drupal 用 CKEditor 替换文本区域字段——CKEditor 是一个可视化 HTML 编辑器，通常称为 WYSIWYG 编辑器。
- [Colorbox](https://www.drupal.org/project/colorbox) - Colorbox 是一个轻量级可定制的 jQuery 灯箱插件。该模块允许将 Colorbox 集成到 Drupal 中。
- [Context](https://www.drupal.org/project/context) - 上下文允许您管理站点不同部分的上下文条件和反应。您可以将每个上下文视为代表站点的一个“部分”。
- [Display Suite](https://www.drupal.org/project/ds) - Display Suite 允许您使用拖放界面完全控制内容的显示方式。
- [RESTful module](https://www.drupal.org/project/restful) - 允许 Drupal 通过 RESTful HTTP 请求进行操作，使用安全性、性能和可用性的最佳实践。
- [Organic groups module](https://www.drupal.org/project/og) - 使用户能够创建和管理自己的“组”。
- [Message](https://www.drupal.org/project/message) - 允许在许多不同的用例中记录和显示系统事件。
- [Message Notify](https://www.drupal.org/project/message_notify) - 当消息生成时转发消息。
- [Message Subscribe](https://www.drupal.org/project/message_subscribe) - 注册以在针对特定内容生成消息时收到通知。
- [Module Filter](https://www.drupal.org/project/module_filter) - 当处理相当大的站点甚至只是一个用于测试正在考虑的新模块和各种模块的开发站点时，模块列表页面可能会变得相当大。
- [Entities Diagram Graph](https://www.drupal.org/sandbox/bricel/2654176) - 生成 Drupal 7 特定安装的实体、字段及其关系的图表。
- [Owl Carousel](https://www.drupal.org/project/OwlCarousel) - 该模块集成了 OwlFonk 构建的精彩 Owl Carousel 滑块。
- [csv2sql](https://www.drupal.org/project/csv2sql) - 将 CSV 转换为 SQL 并在 Drupal 安装中创建一个表。
- [Logs HTTP](https://www.drupal.org/project/logs_http) - 提供通过 tag/http 端点推送到日志的 JSON 事件。
- [Features](https://www.drupal.org/project/features) - 启用 Drupal 中功能的捕获和管理。功能是 Drupal 实体的集合，它们一起满足特定的用例。
- [Commerce](https://www.drupal.org/project/commerce) - 用于构建各种规模的电子商务网站和应用程序。
- [Views](https://www.drupal.org/project/views) - 允许管理员和站点设计者创建、管理和显示内容列表。
- [Panels](https://www.drupal.org/project/panels) - 允许站点管理员创建用于多种用途的自定义布局。
- [Panelizer](https://www.drupal.org/project/panelizer) - 允许站点管理员创建用于多种用途的自定义布局。
- [Pathauto](https://www.drupal.org/project/pathauto) - Pathauto 模块自动为各种内容（节点、分类术语、用户）生成 URL/路径别名，而不需要用户手动指定路径别名。
- [Ctools](https://www.drupal.org/project/ctools) - 该套件主要是一组用于改善开发人员体验的 API 和工具。
- [Search API](https://www.drupal.org/project/search_api) - 提供一个框架，可以使用任何类型的搜索引擎在 Drupal 已知的任何实体上轻松创建搜索。
- [Slick](https://www.drupal.org/project/slick) - Slick 是一个强大且高性能的幻灯片/轮播解决方案，利用 Ken Wheeler 的 Slick 轮播。请参阅http://kenwheeler.github.io/slick
- [Token](https://www.drupal.org/project/token) - 提供核心不支持的附加令牌（尤其是字段），以及用于浏览令牌的 UI。
- [Ubercart](https://www.drupal.org/project/ubercart) - Ubercart 是您网站上最受欢迎的 Drupal 电子商务平台。它实现了开始在线销售产品所需的一切。
- [Rules](https://www.drupal.org/project/rules) - 规则模块允许站点管理员根据发生的事件定义有条件执行的操作（称为反应式或 ECA 规则）。
- [Entity API](https://www.drupal.org/project/entity) - 扩展了 Drupal 核心的实体 API，以提供统一的方式来处理实体及其属性。
- [Entity cache](https://www.drupal.org/project/entitycache) - 将核心实体放入 Drupal 的缓存 API 中。
- [elFinder file manager](https://www.drupal.org/project/elfinder) - elFinder 是一个开源 AJAX 文件管理器
- [IMCE](https://www.drupal.org/project/imce) - IMCE 是一个图像/文件上传器和浏览器，支持个人目录和配额。
- [Date](https://www.drupal.org/project/date) - 包含灵活的日期/时间字段类型日期字段和其他模块可以使用的日期 API。
- [Devel](https://www.drupal.org/project/devel) - 包含模块开发人员和主题爱好者乐趣的模块套件。
- [Migrate](https://www.drupal.org/project/migrate) - 提供灵活的框架，用于将内容从其他来源迁移到 Drupal。
- [Entity validator](https://www.drupal.org/project/entity_validator) - 允许您定义插件并设置方法来验证您正在处理的对象。
- [Webform](https://www.drupal.org/project/webform) - Webform 是 Drupal 中用于制作表单和调查的模块。
- [WYSIWYG](https://www.drupal.org/project/wysiwyg) - 允许使用客户端编辑器来编辑内容。


## 文档

- [安装指南 ](https://www.drupal.org/docs/7/install)
- [网站建设指南](https://www.drupal.org/documentation/build)
- [管理和安全指南](https://www.drupal.org/docs/7/administering-drupal-7-site)
- [结构指南](https://www.drupal.org/docs/7/nodes-content-types-and-fields)
- [多语言指南](https://www.drupal.org/docs/7/multilingual)
- [主题指南](https://www.drupal.org/docs/7/theming)
- [手机指南](https://www.drupal.org/docs/7/mobile)
- [API参考](https://api.drupal.org/api/drupal)
- [开发人员示例](https://www.drupal.org/project/examples)
- [Troubleshooting](https://www.drupal.org/troubleshooting)
- [Drupal Cookbook（针对初学者）](https://www.drupal.org/documentation/customization/tutorials/beginners-cookbook)


## 文章

- [我们来谈谈解耦身份验证](http://www.gizra.com/content/restful-access-token/)
- [在 Drupal 中创建动态电子邮件模板](http://www.gizra.com/content/dynamic-email-template/)
- [核心计划入门](http://www.gizra.com/content/getting-started-with-drupal-core-initiative/)
- [Drupal 8：轻松迁移带附件的节点](http://www.gizra.com/content/drupal-8-attachment-migration/)
- [迁移最佳实践](http://www.gizra.com/content/migration-best-practices/)
- [跨站脚本攻击检测](http://www.gizra.com/content/xss-attack/)
- [使用 Behat 进行 Drupal 8 的 simpleTest](http://www.gizra.com/content/simpletest-behat-drupal-8/)
- [日志，简单的方法](http://www.gizra.com/content/logs-easy-way/)
- [具有 RESTful 后端的 Todo 应用程序](http://www.gizra.com/content/todo-restful-backend/)
- [消息订阅——新的订阅系统](http://www.gizra.com/content/message-subscribe-new-subscription-system/)
- [什么是消息模块及其新功能](http://www.gizra.com/content/what-message-module-and-its-new-features/)
- [消息通知 - 多语言电子邮件通知](http://www.gizra.com/content/message-notify-multilingual-email-notifications/)
- [数据迁移 - 第 1 部分](http://www.gizra.com/content/data-migration-part-1/)
- [数据迁移 - 第 2 部分](http://www.gizra.com/content/data-migration-part-2/)
- [如何使用 Composer 安装 Drupal](http://whaaat.com/installing-drush-9-using-composer)
- [使用 Composer 设置 Drupal 8](https://www.lullabot.com/articles/goodbye-drush-make-hello-composer)
- [Drupal Headless 架构与 Inferno.js [现场演示]](https://snipcart.com/blog/drupal-headless-architecture-tutorial)


## 发行版

- [Commerce kickstart](https://www.drupal.org/project/commerce_kickstart) - Commerce Kickstart 是启动和运行 Drupal Commerce 的最快方式。
- [OpenScholar](https://www.drupal.org/project/openscholar) - 为您机构的所有网站提供支持的最简单方法。
- [Open Atrium](https://www.drupal.org/project/openatrium) - Open Atrium 由 Phase2 Technology 维护，是一个 Drupal 发行版，可让您通过便捷的协作自信地与同事互动。
- [OpenPublic](https://www.drupal.org/project/openpublic) - 对于政府和公共政策组织来说，开源只有在满足公共部门的安全性、可访问性和灵活性要求的情况下才有效。
- [OpenPublish](https://www.drupal.org/project/openpublish) - OpenPublish 是专为在线新闻行业设计的 Drupal 7 打包发行版。它部署在各种媒体网站中，包括杂志、报纸、期刊、贸易出版物、广播、有线服务、多媒体网站和会员出版物。

## 书籍

- [Drupal 7 要点 - Johan Falk](https://archive.org/details/Drupal7TheEssentials)


## 视频

- [Drupal 8 基础知识 - LevelUpTuts](https://www.youtube.com/playlist?list=PLLnpHn493BHE9mfp6z5--UowO-6SOzcuI)
- [Drupal 7 教程 - LevelUpTuts](https://www.youtube.com/playlist?list=PL15BE2E8313A4E809)
- [解耦 Drupal：何时、为何以及如何](https://www.youtube.com/watch?v=bLWa3SbEEa8)
- [使用 RESTful 构建现代 API](https://www.youtube.com/playlist?list=PLZOQ_ZMpYrZv8_c7jd_CkO_93-DnyVFY5)
- [DrupalCon 波特兰 2013 - 有机团体 \\ 消息](https://www.youtube.com/watch?v=XglUUroifsg)
- [Drupal化我](https://drupalize.me)


## 播客

- [摇篮曲播客](https://www.lullabot.com/podcasts)
- [DrupalEasy 播客](https://www.drupaleasy.com/podcast)
- [会说话的 Drupal](http://www.talkingdrupal.com)
- [阿奎亚参与](https://dev.acquia.com/learn?type_1=podcast)


## 社区

- [Reddit](https://www.reddit.com/r/drupal/)
- [堆栈溢出](http://stackoverflow.com/questions/tagged/drupal)
- [Twitter 上的“@drupal”](https://twitter.com/drupal)
- [Freenode 上的“#drupal”](http://webchat.freenode.net/?channels=drupal)
- [Freenode 上的“#drupal-contribute”](http://webchat.freenode.net/?channels=drupal-contribute)
- [Freenode 上的“#drupal-support”](http://webchat.freenode.net/?channels=drupal-support)
- [Drupal 以色列聚会小组](https://www.meetup.com/Drupal-Israel/) *（希伯来语）*
- [Drupal 纽约聚会小组](https://www.meetup.com/drupalnyc/)


## 温馨提示

- [Solr Script](https://github.com/RoySegall/solr-script) - 用于安装 Apache Solr 的便捷脚本。
- [Ubuntu development environment setup](https://github.com/Gizra/KnowledgeBase/wiki/Ubuntu-and-development-environment-setup) - 提供配置 ubuntu 的步骤，以便为 PHP 和 Drupal 开发做好准备。
- [MacOS: New Machine configuration](https://github.com/Gizra/KnowledgeBase/wiki/MacOS:-New-Machine) - 提供用于配置 MacOS 进行开发的文件和脚本。


## 贡献

欢迎投稿！首先阅读[贡献指南](contributing.md)。


## 许可证

[![CC0](http://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

在法律允许的范围内，[Nir Galon](http://nirgn.com) 已放弃本作品的所有版权以及相关或邻接权。
