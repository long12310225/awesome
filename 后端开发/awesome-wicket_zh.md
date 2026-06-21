# 很棒的检票门 [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
[<img src="https://upload.wikimedia.org/wikipedia/ru/5/5d/Apache_Wicket_logo.png"align="right"width="100">](http://wicket.apache.org/)

由 [Apache Wicket](http://wicket.apache.org) 支持的精彩项目精选列表

随时欢迎您的贡献！

> Wicket 是一个开源、面向组件的服务器端 Java Web 应用程序框架。拥有十多年的历史，它仍然发展强劲，前景光明。

## 目录

- [一般信息](#generic-info)
- [Libraries](#libraries)
  - [WicketStuff](#wicketstuff)
- [网络框架](#web-frameworks)
- [Solutions](#solutions)
- [IDE 插件和工具](#ide-plugins-and-tools)

## 一般信息

- [Apache Wicket](http://wicket.apache.org/) - 检票口官方网站。
- [Wicket on Github](https://github.com/apache/wicket) - [GitHub](https://github.com) 上的 Wicket 官方镜像。
- [Wicket on Twitter](https://twitter.com/apache_wicket) - Wicket 的官方帐号。
- [Wicket wiki](https://cwiki.apache.org/confluence/display/WICKET/Index) - Wiki 上有关 Wicket 的官方知识库。
- [Build With Wicket](https://builtwithwicket.tumblr.com/) - Wicket 的官方 [Tumblr](https://www.tumblr.com/) 帐户。
- [Wicket User Guide](http://ci.apache.org/projects/wicket/guide/7.x/) - 7.x 版本的 Wicket 用户指南。
- [Wicket JavaDocs](http://ci.apache.org/projects/wicket/apidocs/7.x/index.html) - Wicket JavaDocs 版本 7.x。
- [Wicket in Action](http://wicketinaction.com/) - 关于 Wicket 的博客和书籍。

## 图书馆
可在您的应用程序中使用的库和组件列表

- [JNPM](https://github.com/OrienteerBAP/JNPM) - JS 节点包管理器 (NPM) 的 Java 库。提供Wicket资源，用于透明获取NPM包并从中提供所需文件。
- [wicket-akka](https://github.com/l0rdn1kk0n/wicket-akka) - 为 Wicket 集成 Akka。
- [wicket-autowire](https://github.com/wicket-acc/wicket-autowire) - 根据提供的注释自动创建组件，让您的生活更轻松。
- [wicket-bootstrap](https://github.com/l0rdn1kk0n/wicket-bootstrap) - 集成 Wicket 的 Bootstrap 工具包。
- [wicket-clientside-logging](https://github.com/l0rdn1kk0n/wicket-clientside-logging) - 允许在客户端进行 JavaScript 日志记录的帮助程序库，所有日志消息也将存储在服务器端。
- [wicket-console](https://github.com/PhantomYdn/wicket-console) - 支持 AJAX 的轻量级 Web 控制台，用于在服务器端运行时执行 JS 脚本。
- [wicket-crudifier](https://github.com/premium-minds/wicket-crudifier) - 使用 wicket 轻松创建 CRUD 的库。
- [wicket-dnd](https://github.com/svenmeier/wicket-dnd) - Wicket 的通用拖放框架。
- [wicket-extjs-integration](https://github.com/onehippo/wicket-extjs-integration) - 将 Wicket 与 ExtJS 集成，进行事件处理，并重点关注使 Java-API 尽可能接近 JS-API。
- [wicket-fullcalendar](https://github.com/42Lines/wicket-fullcalendar) - [FullCalendar](http://fullcalendar.io/) javascript lib 与 Wicket 集成。
- [wicket-jersey](https://github.com/OrienteerBAP/wicket-jersey) - 用于在 Wicket 下的 [Jersey2](https://jersey.github.io/) 上运行 JAR-RX 资源的适配器。
- [wicket-jquery-selectors](https://github.com/l0rdn1kk0n/wicket-jquery-selectors) - 用于使用 JQuery 和 Wicket 的库。
- [wicket-jquery-ui](http://www.7thweb.net/wicket-jquery-ui/) - Wicket 1.5.x、Wicket 6.x 和 Wicket7.x 中的 JQuery UI 集成。
- [wicket-modelfactory](http://wicketeer.org/wicket-modelfactory/) - Wicket-modelfactory 是一个 API，用于以类型安全和重构安全的方式创建 Wicket PropertyModel。
- [wicket-mustache](https://github.com/l0rdn1kk0n/wicket-mustache) - 提供专门的面板和一些相关实用程序，使用户能够使用 Mustache 和 Wicket。
- [wicket-orientdb](https://github.com/OrienteerDW/wicket-orientdb) - Wicket 与 [OrientDB](http://orientdb.com/) 集成。
- [wicket-requirejs](https://github.com/l0rdn1kk0n/wicket-requirejs) - 在 Wicket 应用程序中使用 require.js 的帮助程序。
- [wicket-shieldui](https://github.com/shieldui/wicket-shieldui) - 利用 [Shield UI](http://www.shieldui.com/) JavaScript 库的组件。
- [wicket-source](https://github.com/42Lines/wicket-source) - 通过提供从浏览器 HTML 到源中原始 Wicket 组件的点击，加快 Wicket 开发速度。
- [wicket-spring-boot](https://github.com/MarcGiffing/wicket-spring-boot) - 通过使用 Sprint Boot，可以轻松地以最少的配置工作创建 Wicket 项目。
- [wicket-webjars](https://github.com/l0rdn1kk0n/wicket-webjars) - Wicket 的 webjar 集成。
- [wicked-charts](https://github.com/thombergs/wicked-charts) - 用于基于 Java 的 Web 应用程序的漂亮且交互式的 javascript 图表。

### 检票门东西
基于 [WicketStuff](https://github.com/wicketstuff/core) 的库

- [Annotation](https://github.com/wicketstuff/core/wiki/Annotation) - 通过 java 注释以声明方式挂载您的页面。
- [Annotation Event Dispatcher](https://github.com/wicketstuff/core/tree/master/annotationeventdispatcher-parent) - 通过注释改进 Wicket 中的事件处理。
- [Async Tasks](https://github.com/wicketstuff/core/wiki/Async-tasks) - 控制 Wicket 应用程序中的后台进程。
- [Autocomplete TagIt](https://github.com/wicketstuff/core/wiki/Autocomplete-TagIt) - [TagIt](http://aehlke.github.com/tag-it/) 与 Wicket 集成。
- [BrowserId](https://github.com/wicketstuff/core/wiki/BrowserId) - [Mozilla Persona](https://login.persona.org/) 与 Wicket 集成。
- [Console](https://github.com/wicketstuff/core/wiki/Console) - 提供对动态执行代码（在运行时）的支持。
- [Context](https://github.com/wicketstuff/core/wiki/Context) - 用于使用 @Context 注释以声明方式定位组件、模型和模型对象。
- [Dashboard](https://github.com/wicketstuff/core/tree/master/dashboard-parent) - 支持 Wicket 仪表板，以便快速访问小部件中所需的信息。
- [DataStores](https://github.com/wicketstuff/core/wiki/DataStores) - [IDataStore](https://github.com/apache/wicket/blob/master/wicket-core/src/main/java/org/apache/wicket/pageStore/IDataStore.java)的各种实现的集合：[MemCached](http://memcached.org/)、[Apache Cassandra](http://cassandra.apache.org/)、[Redis](http://redis.io/)、 [Hazelcast](http://www.hazelcast.com/)。
- [Datatable Autocomplete](https://github.com/wicketstuff/core/wiki/Datatable-Autocomplete) - 提供称为 [Trie](http://en.wikipedia.org/wiki/Trie) 的搜索数据结构，允许在大型数据集上快速进行 AJAX 搜索。
- [DataTables](https://github.com/wicketstuff/core/wiki/DataTables) - [DataTables jQuery](http://www.datatables.net/) 插件集成。
- [Editable Grid](https://github.com/wicketstuff/core/wiki/Editable-Grid) - 除了支持排序/过滤/分页之外，还具有添加/编辑/删除功能的网格组件。
- [Eidogo](https://github.com/wicketstuff/core/wiki/Eidogo) - 用于 GO 游戏（也称为围棋、igo 或围棋）的 SGF 查看器和编辑器。
- [Facebook](https://github.com/wicketstuff/core/wiki/Facebook) - 包含 wicket 组件和使用 [Facebook](https://facebook.com) 社交插件与 wicket 的行为。
- [Fast Serializer](https://github.com/wicketstuff/core/wiki/FastSerializer) - 使用 Fast 1.x (FST) 库的 Wicket 序列化器。
- [Fast Serializer 2](https://github.com/wicketstuff/core/wiki/FastSerializer2) - 使用 Fast 2.x (FST) 库的 Wicket 序列化器。
- [GMap3](https://github.com/wicketstuff/core/wiki/Gmap3) - 提供在 Wicket 应用程序中使用 Google 地图 v3 的组件。
- [Google AppEngine Initializer](https://github.com/wicketstuff/core/wiki/Google-AppEngine-Initializer) - 提供 Wicket 的 org.apache.wicket.IInitializer 实现，自动将 Wicket 应用程序配置为可在 Google AppEngine 上运行。
- [Google Charts](https://github.com/wicketstuff/core/wiki/GoogleCharts) - 允许使用 [Google Chart API](https://developers.google.com/chart/) 创建图表。
- [HTML5](https://github.com/wicketstuff/core/wiki/Html5) - 包含为 wicket 支持使用令人兴奋的新 Html5 功能的类。
- [HTML Compressor](https://github.com/wicketstuff/core/wiki/Htmlcompressor) - Wicket 和 [htmlcompressor](http://code.google.com/p/htmlcompressor) 的集成库。
- [InMethodGrid](https://github.com/wicketstuff/core/wiki/InMethodGrid) - 数据网格组件。
- [Java EE Inject](https://github.com/wicketstuff/core/wiki/Java-EE-Inject) - 通过 Java EE 5 资源注入提供集成。
- [JEE Web Integration](https://github.com/wicketstuff/core/wiki/JEE-Web-Integration) - 将 Servlet、JSP abd JSF 内容嵌入到邪恶的 HTML 页面中。
- [JqPlot Plugin Integration](https://github.com/wicketstuff/core/wiki/JqPlot-Plugin-Integration) - 生成具有许多功能的漂亮折线图、条形图和饼图。
- [JWicket UI Toolip](https://github.com/wicketstuff/core/wiki/jWicket-UI-Tooltip) - 生成为 Wicket 组件提供 jQuery UI 工具提示所需的 JavaScript。
- [Kryo Serializer](https://github.com/wicketstuff/core/wiki/Kryo-Serializer) - Wicket 的 org.apache.wicket.serialize.ISerializer 实现。
- [Kryo2 Serializer](https://github.com/wicketstuff/core/tree/master/serializer-kryo2) - Wicket 的 org.apache.wicket.serialize.ISerializer 实现。
- [LazyModel](https://github.com/wicketstuff/core/wiki/LazyModel) - 类型安全模型实现。
- [Lightbox2 Plugin Integration](https://github.com/wicketstuff/core/wiki/Lightbox2-Plugin-Integration) - 简单、不引人注目的脚本，用于将图像覆盖在当前页面的顶部。
- [Logback](https://github.com/wicketstuff/core/wiki/Logback) - 可以帮助同时使用 wicket 和 [logback](http://logback.qos.ch/) 的课程主页。
- [MBeanView](https://github.com/wicketstuff/core/wiki/MBeanView) - JMX面板，用于查看和操作应用程序mbean。
- [Minis](https://github.com/wicketstuff/core/wiki/Minis) - 各种组件和行为的集合，这些组件和行为太小，无法保证自己的项目。
- [ModalX](https://github.com/wicketstuff/core/wiki/ModalX) - Wicket ModalWindow 功能的轻量级扩展，附带标准化 MessageBox 类，并允许轻松定义模态对话框类。
- [OSGI](https://github.com/wicketstuff/core/wiki/Osgi) - 允许您在 OSGi 环境中使用 Wicket。
- [Open Layers 3](https://github.com/wicketstuff/core/tree/master/openlayers3-parent) - 提供一组可用于将交互式地图添加到 Wicket 应用程序的组件。
- [POI](https://github.com/wicketstuff/core/wiki/POI) - 将 Wicket 项目集成到 Apache POI。
- [Progressbar](https://github.com/wicketstuff/core/wiki/Progressbar) - 为 Wicket 提供进度条组件。
- [Push](https://github.com/wicketstuff/core/wiki/Push) - 在 Wicket 应用程序中提供对反向 AJAX 的支持，并允许它们将部分网页更新“推送”到 Web 浏览器。
- [Scala Extensions](https://github.com/wicketstuff/core/wiki/ScalaExtensions) - 改进了使用 Scala 编程语言时 Wicket 模型的语法。
- [Select2](https://github.com/wicketstuff/core/tree/master/select2-parent) - 提供 Apache Wicket 组件，利用 [Select2](http://ivaynberg.github.com/select2) JavaScript 库来构建提供 Ajax 选择过滤、自定义渲染等的选择框。
- [Servlet Container Authentication and Authorization](https://github.com/wicketstuff/core/wiki/Servlet-Container-Authentication-and-Authorization) - 简化 wicket-auth-roles 与 servlet 3 安全容器的集成。
- [Spring Reference](https://github.com/wicketstuff/core/wiki/SpringReference) - 可用于将 wicket Web 应用程序与 spring 集成。
- [Stateless](https://github.com/wicketstuff/core/tree/master/stateless-parent) - 添加了一些组件，为 Wicket 提供更全面的无状态功能。
- [TinyMCE Integration](https://github.com/wicketstuff/core/wiki/TinyMCE-Integration) - 在 Wicket 中集成著名的 TinyMCE WYSIWYG 编辑器。
- [Twitter](https://github.com/wicketstuff/core/wiki/Twitter) - 包含将 Twitter 小部件与 wicket 一起使用的 wicket 组件和行为。
- [UrlFragment](https://github.com/wicketstuff/core/tree/master/urlfragment-parent) - 通过此功能，您可以构建可添加书签的 AJAX 功能，并且仍然支持后退按钮。
- [WHighCharts](https://github.com/wicketstuff/wiquery-highcharts) - 为 HighCharts 提供 WiQuery 绑定。
- [Whiteboard](https://github.com/wicketstuff/core/wiki/Whiteboard) - 提供可集成到任何检票口应用程序中的白板。
- [wicket-foundation](https://github.com/wicketstuff/core/tree/master/wicket-foundation) - 集成 Wicket 和 [Zurb 基金会](http://foundation.zurb.com/)。
- [Wicket Rest Annotations](https://github.com/wicketstuff/core/tree/master/wicketstuff-restannotations-parent) - 提供一个特殊的资源类和一组注释来实现 REST API/服务，其方式与我们使用 Spring MVC 或标准 JAX-RS 的方式大致相同。
- [WiQuery](https://github.com/wicketstuff/wiquery) - Wicket 与 jQuery 和 jQuery UI 集成。
- [WqPlot](https://github.com/wicketstuff/wiquery-jqplot) - 为 JqPlot 提供 WiQuery 绑定。

## 网络框架
Web 框架位于 wicket 之上，可让您轻松流畅地构建系统

- [Apache Isis](https://isis.apache.org/) - 用于使用 Java 快速开发领域驱动应用程序的框架。
- [BrixCMS](http://www.brixcms.org/) - 基于 Wicket 的 CMS（似乎已经死了）。
- [Hippo CMS](http://www.onehippo.com/en) - 使企业能够通过快速响应内容绩效指标来不断完善其在线业务策略。
- [Nocket](https://github.com/Nocket/nocket) - 基于裸对象的检票框架。
- [NoWicket](http://invesdwin.de/nowicket/) - Wicket 的裸对象框架，使开发人员能够在复杂网站的实现过程中编写更少的样板 Wicket 代码。
- [Orienteer](https://github.com/OrienteerDW/Orienteer) - 基于 Wicket 和 [OrientDB](http://orientdb.com/) 的 Web 框架，用于构建您自己的 CRM、CMS、ERP、移动应用后端或普通网站。
- [Vuecket](https://github.com/OrienteerBAP/vuecket) - 集成了 VueJS 和 Wicket 的 Web 框架以及两者最自然的方式
- [Wicketopia](https://github.com/jwcarman/Wicketopia) - Wicket 的快速应用程序开发 (RAD) 库。

## 解决方案
基于 wicket 和衍生的 [Web 框架](#web-frameworks) 的端到端解决方案

- [eFaps](http://www.efaps.org/) - 模块和应用程序的列表，它们共同构成了可配置 ERP 实施的基础。
- [eHour](https://ehour.nl/index.phtml) - 开源时间跟踪工具。
- [Estatio](https://github.com/estatio/estatio) - 基于 Apache Isis 和 wicket 构建的开源资产管理。
- [GeoServer](https://github.com/geoserver/geoserver) - 用 Java 编写的开源软件服务器，允许用户共享和编辑地理空间数据。
- [NextReports](http://www.next-reports.com/) - 智能商业报告。
- [Orienteer](https://github.com/OrienteerDW/Orienteer) - 开源业务应用平台，用于实施数据仓库、CRM、ERP、应用程序/网站后端系统和其他业务应用程序。
- [ProjectForge](https://www.projectforge.org/) - 用于项目管理的开源软件。
- [Yes Cart](https://github.com/inspire-software/yes-cart) - 纯电商平台。

## IDE 插件和工具

- [qwickie](https://marketplace.eclipse.org/content/qwickie) - [Eclipse](http://www.eclipse.org/) Java Webframework Wicket 插件
- [WicketForge](https://github.com/minman/wicketforge) - [IntelliJ IDEA](https://www.jetbrains.com/idea/) 的 IDE 插件旨在帮助开发人员使用 Apache Wicket 创建应用程序。

＃ 执照

 [![CC0](http://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)
