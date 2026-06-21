# 很棒的 ColdFusion [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

精选的 ColdFusion 框架、库和软件列表。受到 [awesome-javascript](https://github.com/sorrycc/awesome-javascript) 的启发。

非常欢迎请求请求。

* [很棒的 ColdFusion](https://github.com/seancoyne/awesome-coldfusion)
	* [Engines](#engines)
	* [应用框架](#application-frameworks)
	* [Testing](#testing)
	* [依赖注入](#dependency-injection)
	* [内容管理系统](#cms)
	* [NoSQL](#nosql)
	* [REST](#rest)
	* [其他图书馆](#other-libraries)
	* [Editors](#editors)
	* [Tools](#tools)
	* [References](#references)
	* [Resources](#resources)
	* [Documentation](#documentation)
	
----

## 发动机

* [Adobe ColdFusion](http://www.adobe.com/products/coldfusion-family.html)
* [Lucee](http://lucee.org/) - 免费、开源 CFML 引擎

## 应用框架

* [CFWheels](https://cfwheels.org) - 受 Ruby on Rails 启发的开源 CFML 框架。
* [ColdBox](http://www.coldbox.org) - 企业 ColdFusion MVC 开发平台
* [FarCry](http://www.farcrycore.org) - FarCry Core 是一个 Web 应用程序框架，可帮助 CFML 开发人员快速构建定制的内容解决方案。
* [FW/1 - Framework One](https://github.com/framework-one/fw1) - 一个轻量级的、约定优于配置的 MVC 应用程序框架

## 测试

* [CFSelenium](https://github.com/teamcfadvance/CFSelenium) - ColdFusion 的原生 Selenium RC 绑定
* [MockBox](https://testbox.ortusbooks.com/mocking/mockbox) - ColdFusion 模拟/存根框架
* [MXUnit](https://github.com/mxunit/mxunit) - xUnit风格的单元测试框架
* [mxunit-watch](https://github.com/atuttle/mxunit-watch) - 监视目录中的文件更改（.cfc、.cfm、.xml）以触发 mxunit 测试套件完全运行，并在控制台中显示结果
* [TestBox](https://github.com/Ortus-Solutions/TestBox) - BDD风格的单元测试框架

## 依赖注入

* [ColdSpring](https://github.com/coldspringframework/coldspring1) - ColdSpring 使 CFC 的配置和依赖项更易于管理。 ColdSpring 将流行的 Java Spring 框架的强大功能引入 ColdFusion。
* [DI/1 - Inject One](https://github.com/framework-one/di1) - 一个非常轻量级的、约定优于配置、依赖注入（控制反转）框架
* [Wirebox](https://wirebox.ortusbooks.com/) - 企业依赖注入框架

## 内容管理系统

* [CONTENS CMS](http://www.contens.com/) - 专业内容管理
* [ContentBox](https://github.com/Ortus-Solutions/ContentBox) - 强大的模块化内容管理引擎
* [孤岛惊魂 CMS](https://github.com/farcrycore/plugin-farcrycms)
* [Mura](https://www.murasoftware.com/)
* [Preside CMS](https://github.com/pixl8/Preside-CMS) - Railo 语言的开源 CMS
* [Slatwall](https://www.slatwallcommerce.com/) - 开源商务平台

## NoSQL

* [CFArango](https://github.com/dajester2013/CFArango) - 适用于 ColdFusion 的 ArangoDB 客户端
* [CFCouchbase](https://github.com/Ortus-Solutions/cfcouchbase-sdk) - Couchbase NoSQL 和 ColdFusion 的缓存客户端包装器
* [cfmongodb](https://github.com/marcesher/cfmongodb) - ColdFusion 的 MongoDB 客户端包装器

## 休息

* [ColdBox REST](https://coldbox.ortusbooks.com/digging-deeper/recipes/building-rest-apis) - 原生 REST 路由和渲染功能
* [FW/1 REST](https://github.com/framework-one/fw1/wiki/Developing-Applications-Manual#controllers-for-rest-apis) - 原生 REST 路由和渲染功能
* [Taffy](http://taffy.io) - ColdFusion 和 Railo 的 REST Web 服务框架
* [CFWheels RESTful](https://guides.cfwheels.org/docs/routing) - CFWheels 鼓励采用传统的 RESTful 和足智多谋的请求处理方式。

## 其他图书馆

* [CacheBox](https://cachebox.ortusbooks.com/) - 企业 ColdFusion 缓存引擎、聚合器和 API
* [cfbackport](https://github.com/misterdai/cfbackport) - 新版本 ColdFusion 中包含的向后移植功能。
* [cfpayment](https://github.com/ghidinelli/cfpayment) - ColdFusion 支付处理库使电子商务应用程序变得简单。信用卡收费从未如此简单。受到 Ruby 的 ActiveMerchant 的启发。
* [BugLogHQ](https://github.com/oarevalo/BugLogHQ) - 异常追踪
* [JavaLoader](https://github.com/markmandel/JavaLoader) - JavaLoader 是一个库，旨在简化 ColdFusion 应用程序中 Java 的使用、开发和集成。
* [LogBox](https://logbox.ortusbooks.com/) - 企业 ColdFusion 日志库
* [Moment.cfc](https://github.com/AlumnIQ/momentcfc) - Moment.js 启发的 CFML 日期/时间操作库（不是直接端口）
* [Mustache.cfc](https://github.com/rip747/Mustache.cfc) - [{{ Mustache }}](http://mustache.github.io) 用于 ColdFusion
* [UnderscoreCF](https://github.com/russplaysguitar/UnderscoreCF) - Coldfusion 的 UnderscoreJS 端口。函数式编程库。

## 编辑

* [CFML Package for Sublime Text 3](https://github.com/jcberquist/sublimetext-cfml) - [Sublime Text 3](http://www.sublimetext.com) 的 CFML 语法突出显示以及函数和标签补全
* [CFML Extension for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=KamasamaK.vscode-cfml) - [VSCode](https://code.visualstudio.com/) 的 CFML 语言扩展
* [CFML Language for Atom](https://github.com/atuttle/atom-language-cfml) - [Atom](https://atom.io/) 的 CFML 语言插件
* [Adobe ColdFusion Builder 3](http://www.adobe.com/products/coldfusion-builder.html) - Adobe 基于 Eclipse 的 ColdFusion IDE
* [IntelliJ Idea](http://www.jetbrains.com/idea/) - Java IDE、CFML 支持可通过 [插件](https://github.com/JetBrains/intellij-plugins/tree/master/CFML) 获得
* [cfbrackets](http://cfbrackets.org) - [Brackets 代码编辑器](http://brackets.io/) 添加了对 ColdFusion 标记语言 (CFML) 的支持
* [CFEclipse](http://cfeclipse.org) - [Eclipse] 的 CFML 插件(http://www.eclipse.org/)
* [TextMate](https://github.com/textmate/coldfusion.tmbundle) - [TextMate](http://macromates.com) 对 ColdFusion 的支持

## 工具

* [CommandBox](https://www.ortussolutions.com/products/commandbox) - ColdFusion (CFML) CLI、包管理器、REPL 等
* [Unofficial Updater](http://www.uu-2.info/) - 帮助安装 ColdFusion 修补程序的实用程序

## 参考文献

* [CF411](http://carehart.org/cf411/) - CF411：Charlie Arehart 为 CFers 提供的 1,800 多个工具和资源（超过 150 个类别）
* [CFLib](http://cflib.org/) - 通用函数库项目
* [ColdFusion Koans](https://github.com/nodoherty/ColdFusion-Koans) - ColdFusion Koans 是一组单元测试，用户必须通过填写值来通过
* [ColdFusion UI the Right Way](https://github.com/cfjedimaster/ColdFusion-UI-the-Right-Way) - 演示如何在后端使用 ColdFusion 进行 UI 的文章列表。
* [Learn CF in a Week](http://www.learncfinaweek.com) - 社区驱动的培训计划，可在一周内教授您成为一名 ColdFusion 开发人员所需的所有基础知识。
* [Try ColdFusion](http://trycf.com/) - CFML实时互动学习工具

## 资源
* [CFRepo](http://www.cfmlrepo.com/) - 由 Gavin Pickin 创建的 ColdFusion 安装程序存储库
* [lucee5-heroku](https://github.com/mikesprague/lucee5-heroku) - 用于将 Lucee 5 应用程序部署到 Heroku 的应用程序模板，作者：Mike Sprague
* [Vagrant LEMTL](https://github.com/mikesprague/vagrant-lemtl) - Vagrant box 配备 Linux、Nginx、MariaDB（或 MySQL）、Tomcat 和 Lucee，用于使用 CFML 进行本地开发，作者：Mike Sprague
* [Amazon ECR](https://gallery.ecr.aws/adobe/coldfusion) 和 [Docker Hub](https://hub.docker.com/u/adobecoldfusion) 上的 ACF Docker 映像 - 来自 Adobe 的官方 Docker 映像
* Lucee Docker 镜像 [Docker Hub](https://hub.docker.com/u/lucee) - 来自 Lucee 的官方 Docker 镜像

## 文档

* [Adobe ColdFusion Documentation](https://helpx.adobe.com/coldfusion/home.html) - Adobe ColdFusion 官方文档
* [CFDocs](http://cfdocs.org/) - UltraFast CFML 文档参考。
* [CFML Tags to CFScript Reference](https://github.com/cfchef/cfml-tag-to-script-conversions) - CFML 标签到脚本的转换 作者：Tony Junkes
* [CFScript Reference](https://github.com/daccfml/cfscript/blob/master/cfscript.md) - Adam Cameron 的 CFScript 文档
* [Lucee Wiki](https://bitbucket.org/lucee/lucee/wiki/Home) - Lucee 官方文档
* [Official Lucee Server Documentation](http://docs.lucee.org/) - 新 Lucee 文档
* [Railo Documentation](https://github.com/getrailo/railo/wiki) - Railo 官方文档

## 许可证

[![CC0](http://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

在法律允许的范围内，[Sean Coyne](https://github.com/seancoyne/awesome-coldfusion) 已放弃本作品的所有版权以及相关或邻接权。
