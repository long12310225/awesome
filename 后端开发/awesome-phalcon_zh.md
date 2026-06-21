# 很棒的菲尔肯

[![Awesome](https://cdn.jsdelivr.net/gh/sindresorhus/awesome@d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
[![Actions Status](https://github.com/phalcon/awesome-phalcon/workflows/CI/badge.svg)](https://github.com/phalcon/awesome-phalcon/actions)


很棒的 Phalcon 库和资源的精选列表。受到 [awesome-go](https://github.com/avelino/awesome-go) 的启发。



### 贡献

请先快速浏览一下[贡献指南](CONTRIBUTING.md)。感谢所有[贡献者](https://github.com/phalcon/awesome-phalcon/graphs/contributors)；你摇滚！

加入我们的 [Discord](https://discord.com/invite/kRc2N2M) 与其他 Awesome-phalcon 维护者聊天！

### 内容

- [很棒的菲尔肯](#awesome-phalcon)
    - [ACL](#acl)
    - [应用骨架](#application-skeleton)
    - [身份验证和 OAuth](#authentication--oauth)
    - [内容管理系统和博客](#cms--blogs)
    - [命令行](#command-line)
    - [Dashboard](#dashboard)
    - [Debug](#debug)
    - [i18n](#i18n)
    - [Integration](#integration)
    - [IDE](#ide)
    - [Miscellaneous](#miscellaneous)
    - [ORM](#orm)
    - [ODM](#odm)
    - [Provisioning](#provisioning)
    - [RESTful](#restful)
    - [Routing](#routing)
    - [Searching](#searching)
    - [SEO](#seo)
    - [商店和电子商务](#shop--ecommerce)
    - [Talks](#talks)
    - [Templating](#templating)
    - [Testing](#testing)

- [服务器应用程序](#server-applications)

- [Resources](#resources)
    - [Conferences](#conferences)
        - [Communities](#communities)
    - [Books](#books)
    - [E-Books](#e-books)
    - [Magazines](#magazines)
    - [Websites](#websites)
        - [Tutorials](#tutorials)

## 前交叉韧带

*访问控制列表。*

* [PhalconUserPlugin](https://github.com/calinrada/PhalconUserPlugin) - 基于 Vökuró ACL 理念的插件


## 应用骨架

*各种应用程序框架。*

* [Album O'Rama](https://github.com/phalcon/album-o-rama) - Phalcon 框架的模块化应用程序示例
* [Base App](https://github.com/mruz/base-app) - Phalcon框架中的基础应用
* [INVO Application](https://github.com/phalcon/invo) - Phalcon 框架的示例应用程序
* [MVC](https://github.com/phalcon/mvc) - Phalcon MVC 文件结构示例
* [Phalcon Composer](https://github.com/xxtime/phalcon) - Phalcon with Composer 支持 MySql MongoDb Redis，干净+美观
* [Vökuró](https://github.com/phalcon/vokuro) - Phalcon 框架的示例应用程序（Acl、Auth、安全性）
* [Webird](https://github.com/perchlabs/webird) - 创建 Webird 的目的是将最新的 PHP 和 Node.js 创新合并到单个应用程序堆栈中
* [NovaMOOC](https://github.com/les-enovateurs/phalcon-nova-mooc) - 具有 API/后端和前端的示例应用程序 + 使用 JWT 进行身份验证 + 使用 GitHub Actions + Docker 进行 Cypress 测试。
* [PhalconTool](https://github.com/corentin-begne/phalconTool) - Phalcon 开发工具的替代方案，具有完整的前端堆栈，无需任何框架，但帮助系统允许使用 Phalcon 5、PHP 8、Apache、MYSQL、SASS、ES6 和 jQuery 自动绑定 HTML 事件。


## 身份验证和 OAuth

*用于实现身份验证方案的库。*

* [Padlock](https://github.com/tegaphilip/padlock) - 构建在 PHP OAuth 2.0 服务器之上的基于 docker 的 phalcon 身份验证服务器
* [phalcon-authmiddleware](https://github.com/SidRoberts/phalcon-authmiddleware) - 将中间件事件添加到调度程序。与 ACL 或自定义身份验证库兼容的通用设计。
* [Phalcon Auth](https://github.com/sinbadxiii/phalcon-auth) - 基于守卫和提供者的开箱即用的身份验证组件。


## 内容管理系统和博客

*内容管理系统和博客。*

* [giada-www](https://github.com/monocasual/giada-www) - 【Giada Loop Machine】官网(https://www.giadamusic.com/)
* [KikCMS](https://github.com/krazzer/kikcms) - 基于 Phalcon 框架的 CMS
* [Skopy Blog Engine](https://github.com/yuriygr/skopy) - 一个简单的博客引擎，适合那些想要开始学习 Phalcon 的人
* [Yona CMS](https://github.com/alexander-torosh/yona-cms) - 基于Phalcon框架的CMS，模块化结构
* [PhalconCMS](https://github.com/KevinJay/PhalconCMS) - 基于 Phalcon 框架构建的博客
* [Hummingbird CMS](https://github.com/mvanvu/hummingbird-cms) - 基于Phalcon 4的CMS，具有许多强大的功能
* [Element CMF](https://github.com/odvapro/element) - 一切管理面板 [演示](https://element-demo.odva.pro/element/) (admin | adminpass)


## 命令行

*命令行应用程序和工具。*

* [phalcon-console](https://github.com/viebig/phalcon-console) - 使用出色的 Phalcon 框架的命令行应用程序的示例引导应用程序
* [phalcon-cron](https://github.com/SidRoberts/phalcon-cron) - Phalcon 的 Cron 组件


## 配置

* [Phalcon Config Loader for Yaml](https://github.com/ienaga/PhalconConfig) - 加载app/config目录下的所有yml。


## 仪表板

*管理面板和仪表板。*

* [PhalconTime](https://github.com/Videles/PhalconTime) - 计时工具/仪表板骨架


## 调试

*调试和分析工具。*

* [dd](https://github.com/phalcon/dd) - 这个包将添加 `dd` 和 `dump` 帮助器到你的 Phalcon 应用程序中
* [Phalcon BB Debugger](https://github.com/ismail0234/Phalcon-BB-Debugger) - Phalcon BB 调试器 强大且易于安装。
* [Phalcon Debugbar](https://github.com/snowair/phalcon-debugbar) - 将 [PHP 调试栏](http://phpdebugbar.com) 与 Phalcon 框架集成
* [Prophiler](https://github.com/fabfuel/prophiler) - PHP 分析器和开发人员工具栏（为 Phalcon 构建）


## 国际化

*国际化和本地化图书馆及服务列表。*

* [xgettext-template](https://github.com/gmarty/xgettext) - 使用与 xgettext 调用相同的命令行程序从 Volt 模板中提取 gettext 消息。


## 整合

*与第三方服务集成*

* [phalcon-logentries](https://github.com/phalcon-orphanage/phalcon-logentries) - 将日志消息发送到 [Logentries](https://logentries.com/) 日志管理服务

## 集成开发环境
*IDE 扩展列表*
 
 * [volt-phalcon-language](https://marketplace.visualstudio.com/items?itemName=fbclol.volt-phalcon-language) - VS Code 的扩展，提供对 Phalcon Volt 语法和自动补全的支持
 

## 杂项

*这些库被放置在这里是因为其他类别似乎都不适合*

* [Breadcrumbs](https://github.com/sergeyklay/breadcrumbs) - 用于在 Phalcon 2+ 中构建站点面包屑的强大而灵活的组件。
* [Feedback](https://quasipickle.github.io/feedback/) - 旨在替代 Phalcon 的内置 Flash 和消息功能
* [Incubator](https://github.com/phalcon/incubator) - 用于发布/共享/试验可能合并到 Phalcon 框架中的新适配器、原型或功能的存储库
* [Upgrade Adviser](https://github.com/diplopito/Phalcon-Upgrade-Adviser) - 命令行工具可帮助将 Phalcon 应用程序从 3.4.x 升级到 4.1.3、3.4.x 到 5.1.3、4.1.3 到 5.1.3。
* [yarak](https://github.com/zachleigh/yarak) - Laravel 启发 Phalcon 开发工具
* [phalcon-data-table](https://github.com/maslo2017/phalcon-data-table) - 允许您简化与 Phalcon 中引导表的交互


## ORM

*实现对象关系映射或数据映射技术的库。*

* [phalcon-boundmodels](https://github.com/SidRoberts/phalcon-boundmodels) - Phalcon框架内根据调度程序参数自动获取模型
* [phalcon-repositories](https://github.com/micheleangioni/phalcon-repositories) - Phalcon 的简单存储库模式
* [phalcon-seeder](https://github.com/SidRoberts/phalcon-seeder) - Phalcon 的数据库播种器组件
* [phalcon-redis-model](https://github.com/ienaga/RedisPlugin) - 基于redis的ORM和Easy Criteria（MySQL分片的对应）

## 原始设计制造商

*实现对象文档映射器技术的库。*

* [phalcon-collection-paginator](https://github.com/angelxmoreno/phalcon-collection-paginator) - 用于扩展 `Phalcon\Mvc\Collection` 的类的 [分页适配器](https://docs.phalcon.io/3.4/db-pagination#data-adapters)

## 配置
*用于为 Phalcon 应用程序配置系统的工具。*
 
* [ansible-phalcon](https://github.com/HanXHX/ansible-phalcon) - Ansible Role在Debian中安装Phalcon Framework（提供PHP 5.6和PHP 7.0软件包）
* [setupify](https://github.com/perchlabs/setupify) - bash 脚本的集合，用于配置基于 Zephir 和 Phalcon 的系统以进行部署或开发

## 宁静的

*代表性状态转移。*

* [phalcon-json-api-package](https://github.com/gte451f/phalcon-json-api-package) - 一个 Composer 包，旨在帮助您在 Phalcon 中创建 JSON:API
* [PhREST API](https://github.com/phrest/api) - Phalcon 框架 REST API 包
* [REST API](https://github.com/phalcon/rest-api) - 使用 Phalcon 实现 API 应用程序


## 路由

*各种路由库和扩展。*

* [Phalcon-autorouter](https://github.com/kahur/Phalcon-autorouter) - 自动加载模块的简单方法，无需复杂的路由定义
* [Phalcon Routing for Yaml](https://github.com/ienaga/PhalconRouter) - 使用yaml可以轻松配置路由


## 搜寻中

*搜索工具和库。*

* [ElasticsearchIndexer](https://github.com/SidRoberts/phalcon-elasticsearchindexer) - Phalcon 的 Elasticsearch 索引器组件


## 搜索引擎优化

*搜索引擎优化工具。*

* [Phalcon meta tags](https://github.com/izica/phalcon-meta-tags) - 用于处理元标记的工具。


## 商店和电子商务

* [Shopping Cart](https://github.com/sinbadxiii/phalcon-cart) - 在线商店的简单购物车


## 会谈

*会议、聊天、论坛等..*

* [Phanbook](https://github.com/phanbook/phanbook/) - phanbook.com 网站代码来源
* [Phosphorum](https://github.com/phalcon/forum) - 来源为 Phalcon 官方论坛


## 模板化

*用于模板的库和工具。*

* [twig-phalcon](https://github.com/vinyvicente/phalcon-twig) - Phalcon 框架的 Twig 模板引擎


## 测试

*测试工具和解决方案。*

* [phalcon-demo](https://github.com/Codeception/phalcon-demo) - 修改后的 Phalcon INVO 应用程序，用于演示 Codeception 测试的基础知识。


# 服务器应用程序

* [phalcon-docker-nginx](https://github.com/viebig/phalcon-docker-nginx) - Phalcon 3、PHP7、Docker 示例入门应用程序
* [phalcon-vm](https://github.com/eugene-manuilov/phalcon-vm) - 适用于 Phalcon 3.x 和 PHP7.0 开发的 Vagrant 配置 + MySQL/PostgreSQL/MongoDB、Redis/Memcached、Gearman/RabbitMQ、Elasticsearch/Sphinxsearch 供您选择
* [phalcon3-compose](https://github.com/linxlad/phalcon3-compose) - Docker Phalcon 3 开发环境


# 资源

*在哪里发现新的 Phalcon 库。*


## 会议

*会议、IRC、论坛等..*

### 社区

* [Gab](https://gab.com/phalcon) - Phalcon 上 Gab
* [MeWe](https://mewe.com/join-front/phalcon) - Phalcon 上 MeWe
* [Phalcon Forums](https://forum.phalcon.io/) - Phalcon 论坛
* [Phalcon Russian Community Chat](https://app.gitter.im/#/room/#phalcon-rus_chat:gitter.im) - Gitter.im 中的俄语社区聊天
* [Stack Overflow](https://stackoverflow.com/questions/tagged/phalcon) - StackOverflow 标记问题
* [Telegram](https://t.me/phalcon_news) - Phalcon 在 Telegram 上
* [Twitter](https://twitter.com/phalconphp) - Phalcon 在 Twitter 上

## 书籍

* [Phalcon Book (in French)](https://www.editions-eni.fr/livre/phalcon-3-developpez-des-applications-web-complexes-et-performantes-en-php-version-en-ligne-9782409022753) - Phalcon：用 PHP 开发复杂而强大的 Web 应用程序

## 电子书

* [Phalcon PDF Documentation](https://buildmedia.readthedocs.org/media/pdf/phalcon-php-framework-documentation/latest/phalcon-php-framework-documentation.pdf) - Phalcon 框架文档

## 杂志

* [French magazine - Programmez n°239](https://www.programmez.com/magazine/article/les-10-commandements-de-lecoconception) - 生态设计的 10 条戒律（文章提到 Phalcon 作为轻质生态框架）
* [French magazine - Programmez n°241](https://www.programmez.com/magazine/article/phalcon-un-framework-performant-et-robuste-compile-en-c) - Phalcon：新的必须了解的 PHP 框架

## 网站

* [Built With](https://builtwith.phalcon.io/) - 使用 Phalcon 框架构建的应用程序、演示和项目库
* [Phalcon Blog](https://blog.phalcon.io/) - Phalcon 博客
* [Phalconist](https://github.com/phalcon/phalconist) - Phalconist 上 Phalcon 框架的资源目录


### 教程

* [Phalcon Documentation](https://docs.phalcon.io/4.0/en/introduction) - Phalcon 文档
* [Sitepoint](https://www.sitepoint.com/?s=phalcon) - 文章、教程等
