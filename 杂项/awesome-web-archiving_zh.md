<!--lint ignore awesome-github-->
# 很棒的网络存档 [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

网络归档是收集万维网部分内容的过程，以确保信息保存在档案中，供未来的研究人员、历史学家和公众使用。由于网络规模庞大，网络档案管理员通常使用网络爬虫进行自动捕获。不断发展的 Web 标准要求归档工具不断发展，以跟上 Web 技术的变化，从而确保可靠且有意义地捕获和重放已归档的网页。


## 内容

* [Training/Documentation](#trainingdocumentation)
  * [Web 归档概念简介](#introductions-to-web-archiving-concepts)
  * [培训材料](#training-materials)
  * [WARC 标准](#the-warc-standard)
  * [对于使用网络档案的研究人员](#for-researchers-using-web-archives)
* [网络出版商资源](#resources-for-web-publishers)
* [工具和软件](#tools--software)
  * [Acquisition](#acquisition)
  * [Replay](#replay)
  * [搜索与发现](#search--discovery)
  * [Utilities](#utilities)
  * [WARC I/O 库](#warc-io-libraries)
  * [Analysis](#analysis)
  * [品质保证](#quality-assurance)
  * [Curation](#curation)
* [社区资源](#community-resources)
  * [其他很棒的清单](#other-awesome-lists)
  * [博客和奖学金](#blogs-and-scholarship)
  * [邮件列表](#mailing-lists)
  * [Slack](#slack)
  * [Discord](#discord)
  * [Twitter](#twitter)
* [网络归档服务提供商](#web-archiving-service-providers)
  * [自托管、开源](#self-hostable-open-source)
  * [托管、闭源](#hosted-closed-source)
* [公开数据](#public-data)

## 培训/文档

本节为有兴趣了解网络归档实践、方法和工具的人员提供了精选的培训材料、文档和教育资源列表。

### Web 归档概念简介

* [What is a web archive?](https://youtu.be/ubDHY-ynWi0) - 来自[英国网络档案馆 YouTube 频道](https://www.youtube.com/channel/UCJukhTSw8VRj-VNTpBcqWkw) 的视频
* [维基百科的网络归档计划列表](https://en.wikipedia.org/wiki/List_of_Web_archiving_initiatives)
* [Archive-It 和网络归档术语词汇表](https://support.archive-it.org/hc/en-us/articles/208111686-Glossary-of-Archive-It-and-Web-Archiving-Terms)
* [The Web Archiving Lifecycle Model](https://archive-it.org/blog/post/announcing-the-web-archiving-life-cycle-model/) - 尝试将网络归档的技术和程序化部分纳入一个框架，该框架将与任何寻求从网络归档内容的组织相关。 Archive-It 是互联网档案馆的网络归档服务，根据与世界各地的记忆机构的合作开发了该模型。
* [从网站检索和存档信息 作者：Wael Eskandar 和 Brad Murray](https://kit.exposingtheinvisible.org/en/web-archive.html/)

### 培训材料

* [IIPC 和 DPC 培训材料：初学者模块（8 节）](https://netpreserve.org/web-archiving/training-materials/)
* [UNT 网络归档课程](https://github.com/vphill/web-archiving-course)
* [推进网络归档的继续教育 (CEDWARC)](https://cedwarc.github.io/)
* [使用 Python 快速浏览 Common Crawl 数据集](https://github.com/commoncrawl/whirlwind-python/)
* [作为 Python 笔记本的 Common Crawl 数据集旋风之旅](https://github.com/commoncrawl/whirlwind-python-notebook)
* [使用 Java 旋风浏览 Common Crawl 数据集](https://github.com/commoncrawl/whirlwind-java/)

### WARC 标准

* [The warc-specifications](https://iipc.github.io/warc-specifications/) - 官方规范的社区 HTML 版本和新提案中心。
* [ISO 28500 WARC 官方规范主页](http://bibnum.bnf.fr/WARC/)

### 对于使用网络档案的研究人员

* [GLAM Workbench: Web Archives](https://glam-workbench.github.io/web-archives/) - 另请参阅[有关“向网络档案提出问题”的相关博客文章](https://netpreserveblog.wordpress.com/2020/05/28/asking-questions-with-web-archives/)。
* [归档 Unleashed Toolkit 文档](https://aut.docs.archivesunleashed.org/)
* [为人文学科研究人员提供的关于如何探索 Arquivo.pt 的教程](https://sobre.arquivo.pt/en/tutorial-for-humanities-researchers-about-how-to-use-arquivo-pt/)

## 网络出版商资源

当与在网络上发布内容并希望确保其网站可以存档的个人或组织合作时，这些资源可以提供帮助。

* [Definition of Web Archivability](https://nullhandle.org/web-archivability/index.html) - 这描述了保存网页内容的容易程度。 （[斯坦福大学图书馆的存档版本](https://web.archive.org/web/20230728211501/https://library.stanford.edu/projects/web-archiving/archivability))
* [Archive Ready](http://archiveready.com/) 工具，用于估计网页成功存档的可能性。


## 工具和软件

此工具和软件列表旨在简要描述一些与网络归档相关的最重要和最广泛使用的工具。有关更多详细信息，我们建议您参考（并贡献！）来自其他团体的这些优秀资源：

* [网络归档软件比较](https://github.com/archivers-space/research/tree/master/web_archiving)
* [很棒的网站变更监控](https://github.com/edgi-govdata-archiving/awesome-website-change-monitoring)

### 收购

* [ArchiveBox](https://github.com/ArchiveBox/ArchiveBox) - 一种使用 wget、Chrome headless 和其他方法维护 RSS 提要、书签和链接的附加存档的工具（以前称为“Bookmark Archiver”）。 *（开发中）*
* [archivenow](https://github.com/oduwsdl/archivenow) - 一个 [Python 库](http://ws-dl.blogspot.com/2017/02/2017-02-22-archive-now-archivenow.html)，用于将 Web 资源推送到按需 Web 存档中。 *（稳定）*
* [ArchiveWeb.Page](https://webrecorder.net/archivewebpage/) - 适用于 Chrome 和其他基于 Chromium 的浏览器的插件，可让您以交互方式存档网页、重播网页并将其导出为 WARC 和 WACZ 文件。也可作为基于 Electron 的桌面应用程序使用。
* [Auto Archiver](https://github.com/bellingcat/auto-archiver) - 用于自动存档 Google Sheets 文档中的社交媒体帖子、视频和图像的 Python 脚本。阅读 [bellingcat.com 上有关自动存档器的文章](https://www.bellingcat.com/resources/2022/09/22/preserve-vital-online-content-with-bellingcats-auto-archiver-tool/)。
* [Browsertrix Crawler](https://github.com/webrecorder/browsertrix-crawler) - 基于 Chromium 的高保真爬行系统，旨在在单个 Docker 容器中运行复杂的、可定制的基于浏览器的爬行。 *（稳定）*
* [Brozzler](https://github.com/internetarchive/brozzler) - A distributed web crawler (爬虫) that uses a real browser (Chrome or Chromium) to fetch pages and embedded urls and to extract links. *(Stable)*
* [Cairn](https://github.com/wabarc/cairn) - 用于保存网页的 npm 包和 CLI 工具。 *（稳定）*
* [Chronicler](https://github.com/CGamesPlay/chronicler) - 具有记录和重播功能的网络浏览器。 *（开发中）*
* [Community Archive](https://www.community-archive.org/) - 使用用于构建存档 Twitter 数据的工具和资源打开 Twitter 数据库和 API。
* [crau](https://github.com/turicas/crau) - crau 是（大多数）巴西人发音“crawl”的方式，它是用于归档网络和播放档案的最简单的命令行工具：您只需要一个 URL 列表。 *（稳定）*
* [Crawl](https://git.autistici.org/ale/crawl) - Golang 中的一个简单的网络爬虫。 *（稳定）*
* [crocoite](https://github.com/PromyLOPh/crocoite) - 使用无头 Google Chrome/Chromium 抓取网站，并将资源、静态 DOM 快照和页面屏幕截图保存到 WARC 文件中。 *（开发中）*
* [DiskerNet](https://github.com/DO-SAY-GO/dn) - 一种非基于 WARC 的工具，可连接到 Chrome 浏览器并存档您浏览的所有内容，使其可用于离线重播。 *（开发中）*
* [F(b)arc](https://github.com/justinlittman/fbarc) - 一个命令行工具和 Python 库，用于使用 [Graph API](https://developers.facebook.com/docs/graph-api) 从 [Facebook](https://www.facebook.com/) 归档数据。 *（稳定）*
* [freeze-dry](https://github.com/WebMemex/freeze-dry) - JavaScript 库将页面转换为静态、独立的 HTML 文档；对于浏览器扩展很有用。 *（开发中）*
* [grab-site](https://github.com/ArchiveTeam/grab-site) - 档案管理员的网络爬虫：WARC 输出、所有爬网的仪表板、动态忽略模式。 *（稳定）*
* [Heritrix](https://github.com/internetarchive/heritrix3/wiki) - 一个开源、可扩展、网络规模、存档质量的网络爬虫。 *（稳定）*
  * [Heritrix Q&A](https://github.com/internetarchive/heritrix3/discussions/categories/q-a) - 一个讨论论坛，用于提出有关使用 Heritrix 的问题并获得答案。
* [Heritrix 演练](https://github.com/web-archive-group/heritrix-walkthrough) *（开发中）*
* [html2warc](https://github.com/steffenfritz/html2warc) - 一个简单的脚本，用于将离线数据转换为单个 WARC 文件。 *（稳定）*
* [HTTrack](http://www.httrack.com/) - 一个开源网站复制实用程序。 *（稳定）*
* [monolith](https://github.com/Y2Z/monolith) - 用于将网页保存为单个 HTML 文件的 CLI 工具。 *（稳定）*
* [Obelisk](https://github.com/go-shiori/obelisk) - 用于将网页保存为单个 HTML 文件的 Go 包和 CLI 工具。 *（稳定）*
* [Scoop](https://github.com/harvard-lil/scoop) - 高保真、基于浏览器的单页 Web 归档库和 CLI，用于见证 Web。 *（稳定）*
* [SingleFile](https://github.com/gildas-lormeau/SingleFile) - Firefox/Chrome 浏览器扩展和 CLI 工具可将完整页面的忠实副本保存为单个 HTML 文件。 *（稳定）*
* [SiteStory](http://mementoweb.github.io/SiteStory/) - 一种事务存档，有选择地捕获和存储 Web 客户端（浏览器）和 Web 服务器之间发生的事务。 *（稳定）*
* [Social Feed Manager](https://gwu-libraries.github.io/sfm-ui/) - 开源软件，使用户能够通过 Twitter、Tumblr、Flickr 和新浪微博公共 API 创建社交媒体集合。 *（稳定）*
* [Squidwarc](https://github.com/N0taN3rd/Squidwarc) - 直接使用 Chrome 或 Chrome Headless 的[开源、高保真、页面交互](http://ws-dl.blogspot.com/2017/07/2017-07-24-replacing-heritrix-with.html)档案爬虫。 *（开发中）*
* [StormCrawler](http://stormcrawler.net/) - 用于在 Apache Storm 上构建低延迟、可扩展的网络爬虫的资源集合。 *（稳定）*
* [twarc](https://github.com/DocNow/twarc) - 用于归档 Twitter JSON 数据的命令行工具和 Python 库。 *（稳定）*
* [WAIL](https://github.com/machawk1/wail) - 多个网络归档工具之上的图形用户界面（GUI），旨在为任何人提供保存和重播网页的简单方法； [Python](https://machawk1.github.io/wail/)、[Electron](https://github.com/n0tan3rd/wail)。 *（稳定）*
* [Warcprox](https://github.com/internetarchive/warcprox) - WARC 编写的 MITM HTTP/S 代理。 *（稳定）*
* [WARCreate](http://matkelly.com/warcreate/) - 用于将单个网页或网站存档到 WARC 文件的 [Google Chrome](https://www.google.com/intl/en/chrome/browser/) 扩展。 *（稳定）*
* [Warcworker](https://github.com/peterk/warcworker) - 一个开源、dockerized、排队、高保真 Web 存档器，基于 Squidwarc，具有简单的 Web GUI。 *（稳定）*
* [Wayback](https://github.com/wabarc/wayback) - 用于将网页快照到 Internet Archive、archive.today、IPFS 等的工具包。 *（稳定）*
* [Waybackpy](https://github.com/akamhy/waybackpy) - Wayback Machine Save、CDX 和 Python 中的可用性 API 接口以及命令行工具 *（稳定）*
* [Web2Warc](https://github.com/helgeho/Web2Warc) - 一个易于使用且高度可定制的爬虫程序，使任何人都可以创建自己的小型 Web 档案 (WARC/CDX)。 *（稳定）*
* [Web Curator Tool](https://webcuratortool.org) - 用于选择性网络归档的开源工作流程管理。 *（稳定）*
* [WebMemex](https://github.com/WebMemex) - Firefox 和 Chrome 的浏览器扩展可让您存档您访问的网页。 *（开发中）*
* [Wget](http://www.gnu.org/software/wget/) - 一个开源文件检索实用程序，[版本 1.14 支持编写 warcs](http://www.archiveteam.org/index.php?title=Wget_with_WARC_output)。 *（稳定）*
* [Wget-lua](https://github.com/alard/wget-lua) - 带 Lua 扩展的 Wget。 *（稳定）*
* [Wpull](https://github.com/ArchiveTeam/wpull) - 兼容 Wget（或重制/克隆/替换/替代）的网络下载器和爬虫。 *（稳定）*

### 重播

* [InterPlanetary Wayback (ipwb)](https://github.com/oduwsdl/ipwb) - 使用 [IPFS](https://ipfs.io/) 进行网络存档 (WARC) 索引和重放。
* [OpenWayback](https://github.com/iipc/openwayback/) - 该开源项目旨在开发 Wayback Machine，这是全球网络档案馆用来在用户浏览器中回放存档网站的关键软件。 *（稳定的）*
* [PYWB](https://github.com/webrecorder/pywb) - Web 档案重放工具的 Python 3 实现，有时也称为“Wayback Machine”。 *（稳定）*
* [Reconstructive](https://oduwsdl.github.io/Reconstructive/) - Reconstructive 是一个 ServiceWorker 模块，用于通过将资源请求重新路由到相应的存档副本 (JavaScript) 来客户端重建复合纪念品。
* [ReplayWeb.page](https://webrecorder.net/replaywebpage/) - 基于浏览器的完全客户端重放引擎，适用于本地和远程 WARC 和 WACZ 文件。也可作为基于 Electron 的桌面应用程序使用。 *（稳定）*
* [warc2html](https://github.com/iipc/warc2html) - 将 WARC 文件转换为适合离线浏览或重新托管的静态 HTML。

### 搜索与发现

* [hyphe](https://github.com/medialab/hyphe) - 为研究而构建的网络爬虫使用图形用户界面来构建由网络参与者列表和它们之间的链接地图组成的网络语料库。 *（稳定）*
* [Mink](https://github.com/machawk1/Mink) - 一个 [Google Chrome](https://www.google.com/intl/en/chrome/) 扩展，用于在浏览和集成实时存档的网络导航时查询 Memento 聚合器。 *（稳定）*
* [PANDORÆ](https://github.com/Guillaume-Levrier/PANDORAE) - 一款插入 Solr 端点的桌面研究软件，用于查询、检索、规范化和直观地探索 Web 档案。 *（稳定）*
* [playback](https://github.com/wabarc/playback) - 用于从 <!--lint 忽略双链接-->[Internet Archive](https://web.archive.org)、[archive.today](https://archive.today)、[Memento](http://timetravel.mementoweb.org) 等搜索存档网页的工具包。 *（开发中）*
* [SecurityTrails](https://securitytrails.com/) - 基于网络的 WHOIS 和 DNS 记录存档。免费提供 REST API。
* [Tempas v1](http://tempas.L3S.de/v1) - 基于 [Delicious](https://en.wikipedia.org/wiki/Delicious_(website)) 标签的时态网络档案搜索。 *（稳定）*
* [Tempas v2](http://tempas.L3S.de/v2) - 基于 1996 年至 2013 年从德国网络中提取的链接和锚文本的时态网络档案搜索（结果不限于德语页面，例如 [Obama@2005-2009 in Tempas](http://tempas.l3s.de/v2/query?q=obama&from=2005&to=2009)）。 *（稳定）*
* [webarchive-discovery](https://github.com/ukwa/webarchive-discovery) - WARC 和 ARC 全文索引和发现工具，以及许多能够使用如下所示索引的关联工具。 *（稳定）*
* [Shine](https://github.com/ukwa/shine) - 原型网络档案探索 UI，与研究人员一起开发，作为 [英国艺术和人文领域大数据项目](https://buddah.projects.history.ac.uk/) 的一部分。 *（稳定）*
* [SolrWayback](https://github.com/netarchivesuite/solrwayback) - 后端 Java 和前端 VUE JS 项目，具有自由文本搜索和内置播放引擎。要求 Warc 文件已使用 Warc-Indexer 建立索引。该网络应用程序还具有广泛的数据可视化工具和数据导出工具，可以在整个网络存档上使用。 [SolrWayback 4 Bundle 版本](https://github.com/netarchivesuite/solrwayback/releases) 包含易于安装的开箱即用解决方案中的所有软件和依赖项。
* [Warclight](https://github.com/archivesunleashed/warclight) - 基于 Project Blacklight 的 Rails 引擎，支持发现以 WARC 和 ARC 格式保存的 Web 档案。 *（开发中）*
* [Wasp](https://github.com/webis-de/wasp) - 个人[网络存档和搜索系统]的全功能原型(http://ceur-ws.org/Vol-2167/paper6.pdf)。 *（开发中）*
* 构建前端的其他可能选项列在“webarchive-discovery”wiki 中，[此处](https://github.com/ukwa/webarchive-discovery/wiki/Front-ends)。

### 公用事业

* [ArchiveTools](https://github.com/recrm/ArchiveTools) - 用于提取 WARC 文件并与之交互的工具集合 (Python)。
* [bagnabit2warc](https://github.com/internetarchive/bagnabit2warc) - 将存储在 ZIP 中的 [bag-nabit](https://github.com/harvard-lil/bag-nabit) 数据集转换为完整内容的 WARC。
* [cdx-toolkit](https://pypi.org/project/cdx-toolkit/) - 用于查询 cdx 索引并创建子集的 WARC 提取的库和 CLI。抽象出 Common Crawl 不寻常的爬行结构。 *（稳定）*
* [duckdb_warc](https://github.com/midwork-finds-jobs/duckdb_warc) - 用于查询 WARC 文件的 DuckDB 扩展。 *（开发中）*
* [duckdb-web-archive-cdx](https://github.com/midwork-finds-jobs/duckdb-web-archive) - DuckDB 扩展可直接从 SQL 查询 Internet Archive 和 CommonCrawl CDX API。 *（开发中）*
* [Go Get Crawl](https://github.com/karust/gogetcrawl) - 使用 <!--lint 忽略双链接-->[Wayback Machine](https://web.archive.org/) 和 [Common Crawl](https://commoncrawl.org/) 提取 Web 存档数据。 *（稳定）*
* [gowarcserver](https://github.com/nlnwa/gowarcserver) - [BadgerDB](https://github.com/dgraph-io/badger) 基于捕获索引 (CDX) 和 WARC 记录服务器，用于索引和服务 WARC 文件 (Go)。
* [har2warc](https://github.com/webrecorder/har2warc) - 转换 HTTP 存档 (HAR) -> Web 存档 (WARC) 格式 (Python)。
<!--lint ignore double-link-->
* [httpreserve.info](https://httpreserve.info) - 返回网页状态或将其保存到互联网档案馆的服务。 HTTPreserve 包括消除众所周知的短链接服务的歧义。它通过浏览器或命令行使用 GET 通过 CURL 返回 JSON。使用互联网档案馆中最早和最新的日期描述网站，并演示使用该范围在其输出中构建稳健链接。 （戈兰）。 *（稳定的）*
* [HTTPreserve linkstat](https://github.com/httpreserve/linkstat) - 命令行实现 <!--lintignore double-link-->[httpreserve.info](https://httpreserve.info) 来描述网页的状态。可以轻松编写脚本并提供 JSON 输出，以便通过 JQ 等工具进行查询。 HTTPreserve Linkstat 描述了当前状态，以及 <!--lint 忽略双链接-->[archive.org](https://archive.org/) 上的最早和最新链接。 （戈兰）。 *（稳定）*
* [Internet Archive Library](https://github.com/jjjake/internetarchive) - 用于直接与 <!--lint 忽略双链接-->[archive.org](https://archive.org) 交互的命令行工具和 Python 库。 （Python）。 *（稳定）*
* [httrack2warc](https://github.com/nla/httrack2warc) - 将 HTTrack 存档转换为 WARC 格式 (Java)。
* [MementoMap](https://github.com/oduwsdl/MementoMap) - 总结网络档案馆藏的工具 (Python)。 *（开发中）*
* [MemGator](https://github.com/oduwsdl/MemGator) - Memento 聚合器 CLI 和服务器 (Golang)。 *（稳定）*
* [node-cdxj](https://github.com/N0taN3rd/node-cdxj) - [CDXJ](https://github.com/oduwsdl/ORS/wiki/CDXJ) 文件解析器 (Node.js)。 *（稳定）*
* [OutbackCDX](https://github.com/nla/outbackcdx) - 基于 RocksDB 的捕获索引 (CDX) 服务器支持增量更新和压缩。可用作 OpenWayback、PyWb 和 [Heritrix](https://github.com/ukwa/ukwa-heritrix/blob/master/src/main/java/uk/bl/wap/modules/uriuniqfilters/OutbackCDXRecentlySeenUriUniqFilter.java) 的后端。 *（稳定）*
* [py-wasapi-client](https://github.com/unt-libraries/py-wasapi-client) - 用于从 WASAPI (Python) 下载爬网的命令行应用程序。 *（稳定）*
* [The Unarchiver](https://theunarchiver.com/) - 用于将多种存档格式（包括 WARC）的内容提取到文件系统的程序。存档浏览器的免费版本（仅限 macOS，专有应用程序）。
* [tikalinkextract](https://github.com/httpreserve/tikalinkextract) - 从可由 Apache Tika（Golang、Apache Tika Server）解析的文档类型文件夹中提取超链接作为 Web 归档的种子。 *（开发中）*
* [wasapi-downloader](https://github.com/sul-dlss/wasapi-downloader) - 用于从 WASAPI 下载爬网的 Java 命令行应用程序。 *（稳定）*
* [Warchaeology](https://nlnwa.github.io/warchaeology/) - Warchaeology 是用于检查、操作、重复数据删除和验证 WARC 文件的工具集合。 *（稳定）*
* [warcdb](https://github.com/florents-Tselai/warcdb) - 用于将 WARC 文件导入 SQLite 数据库的命令行实用程序 (Python)。 *（稳定）*
* [warcbench](https://github.com/harvard-lil/warcbench) - 用于探索、分析、转换、重组和从 WARC (Web ARChive) 文件中提取数据的工具。
* [warcdedupe](https://gitlab.com/taricorp/warcdedupe) - 用 Rust 编写的 WARC 重复数据删除工具（和 WARC 库）。 *（开发中）*
* [warc-safe](https://github.com/natliblux/warc-safe) - 自动检测 WARC 文件中的病毒和 NSFW 内容。
* [WarcPartitioner](https://github.com/helgeho/WarcPartitioner) - 按 MIME 类型和年份对 (W)ARC 文件进行分区。 *（稳定）*
* [warcrefs](https://github.com/arcalex/warcrefs) - Web 归档重复数据删除工具。 *（稳定）*
* [webarchive-indexing](https://github.com/ikreymer/webarchive-indexing) - 用于在 Hadoop、EMR 或本地文件系统上对 WARC/ARC 文件进行批量索引的工具。
* [wikiteam](https://github.com/WikiTeam/wikiteam) - 下载和保存 wiki 的工具。 *（稳定）*

### WARC I/O 库

* [FastWARC](https://github.com/chatnoir-eu/chatnoir-resiliparse) - 高性能 WARC 解析库（Python）。
* [HadoopConcatGz](https://github.com/helgeho/HadoopConcatGz) - 用于串联 GZIP 文件（和“*.warc.gz”）的可拆分 Hadoop 输入格式。 *（稳定）*
* [jwarc](https://github.com/iipc/jwarc) - 使用类型安全的 API (Java) 读写 WARC 文件。
* [Jwat](https://github.com/netarchivesuite/jwat) - 用于读取/写入/验证 WARC/ARC/GZIP 文件的库 (Java)。 *（稳定）*
* [Jwat-Tools](https://github.com/netarchivesuite/jwat-tools) - 用于读取/写入/验证 WARC/ARC/GZIP 文件的工具 (Java)。 *（稳定）*
* [node-warc](https://github.com/N0taN3rd/node-warc) - 使用 [Electron](https://electron.atom.io/) 或 [chrome-remote-interface](https://github.com/cyrus-and/chrome-remote-interface) (Node.js) 解析 WARC 文件或创建 WARC 文件。 *（稳定）*
* [Sparkling](https://github.com/internetarchive/Sparkling) - 互联网档案馆的闪闪发光的数据处理库。 *（稳定）*
* [Unwarcit](https://github.com/emmadickson/unwarcit) - 用于解压缩 WARC 和 WACZ 文件的命令行界面 (Python)。
* [warc](https://github.com/jedireza/warc) - 用于读写 WARC 文件的 Rust 库。 *（稳定）*
* [Warcat](https://github.com/chfoo/warcat) - 用于处理 Web ARChive (WARC) 文件 (Python) 的工具和库。 *（稳定）*
* [Warcat-rs](https://github.com/chfoo/warcat-rs) - 用于处理 Web ARChive (WARC) 文件的命令行工具和 Rust 库。 *（开发中）*
* [warcio](https://github.com/webrecorder/warcio) - 用于快速 Web 存档 IO (Python) 的流式 WARC/ARC 库。 *（稳定）*
* [warctools](https://github.com/internetarchive/warctools) - 用于处理 ARC 和 WARC 文件的库 (Python)。
* [webarchive](https://github.com/richardlehane/webarchive) - ARC 和 WARC webarchive 格式的 Golang 阅读器 (Golang)。

### 分析

* [Archives Research Compute Hub](https://github.com/internetarchive/arch) - 用于 Archive-It Web 档案馆藏的分布式计算分析的 Web 应用程序。 *（稳定）*
* [ArchiveSpark](https://github.com/helgeho/ArchiveSpark) - 用于 Web Archives 的 Apache Spark 框架（不仅如此），可以轻松进行数据处理、提取和派生。 *（稳定）*
* [Archives Unleashed Notebooks](https://github.com/archivesunleashed/notebooks) - 用于使用 Archives Unleashed Toolkit 处理网络档案的笔记本，以及由 Archives Unleashed Toolkit 生成的衍生产品。 *（稳定）*
* [Archives Unleashed Toolkit](https://github.com/archivesunleashed/aut) - Archives Unleashed Toolkit (AUT) 是一个使用 Apache Spark 分析 Web 档案的开源平台。 *（稳定）*
* [Common Crawl Columnar Index](https://commoncrawl.org/tag/columnar-index/) - SQL 可查询索引，带有 CDX 信息和语言分类。 *（稳定）*
* [Common Crawl Web Graph](https://commoncrawl.org/category/web-graph/) - 网络的主机或域级图表，包含排名信息。 *（稳定）*
* [Common Crawl Jupyter notebooks](https://github.com/commoncrawl/cc-notebooks) - 使用 Common Crawl 的各种数据集的笔记本集合。 *（稳定）*
* [Tweet Archvies Unleashed Toolkit](https://github.com/archivesunleashed/twut) - 一个开源工具包，用于使用 Apache Spark 分析面向行的 JSON Twitter 档案。 *（开发中）*
* [Web Data Commons](http://webdatacommons.org/) - 从 Common Crawl 中提取的结构化数据。 *（稳定）*

### 品质保证

* [Chrome Check My Links](https://chromewebstore.google.com/detail/check-my-links/ojkcdipcgfaekbeaelaapakgnjflfglf) - 浏览器扩展：具有更多选项的链接检查器。
* [Chrome link checker](https://chromewebstore.google.com/detail/link-checker/aibjbgmpmnidnmagaefhmcjhadpffaoi) - 浏览器扩展：基本链接检查器。
* [Chrome link gopher](https://chromewebstore.google.com/detail/bpjdkodgnbfalgghnbeggfbfjpcfamkf/publish-accepted?hl=en-US&gl=US) - 浏览器扩展：页面上的链接收集器。
* [Chrome Open Multiple URLs](https://chromewebstore.google.com/detail/open-multiple-urls/oifijhaokejakekmnjmphonojcfkpbbh?hl=de) - 浏览器扩展：打开多个 URL，还可以从文本中提取 URL。
* [Chrome Revolver](https://chromewebstore.google.com/detail/revolver-tabs/dlknooajieciikpedpldejhhijacnbda) - 浏览器扩展：在浏览器选项卡之间切换。
* [FlameShot](https://github.com/flameshot-org/flameshot) - Ubuntu 上的屏幕截图和注释。
* [PlayOnLinux](https://www.playonlinux.com/en/) - 用于在 Ubuntu 上运行 Xenu 和 Notepad++。
* [PlayOnMac](https://www.playonmac.com/en/) - 用于在 macOS 上运行 Xenu 和 Notepad++。
* [Windows Snipping Tool](https://support.microsoft.com/en-gb/help/13776/windows-use-snipping-tool-to-capture-screenshots) - 内置 Windows，用于部分屏幕捕获和注释。在 macOS 上，您可以使用 Command + Shift + 4（用于截取部分屏幕的键盘快捷键）。
* [WineBottler](http://winebottler.kronenberg.org/) - 用于在 macOS 上运行 Xenu 和 Notepad++。
* [xDoTool](https://github.com/jordansissel/xdotool) - 单击 Ubuntu 上的自动化。
* [Xenu](http://home.snafu.de/tilman/xenulink.html) - Windows 桌面链接检查器。

### 策展

* [Zotero Robust Links Extension](https://robustlinks.mementoweb.org/zotero/) - 一个 [Zotero](https://www.zotero.org/) 扩展，用于提交和读取网络档案。来源[GitHub](https://github.com/lanl/Zotero-Robust-Links-Extension)。取代 [leonkt/zotero-memento](https://github.com/leonkt/zotero-memento)。

## 社区资源

### 其他很棒的清单

* [网络存档社区](https://github.com/ArchiveBox/ArchiveBox/wiki/Web-Archiving-Community)
* [很棒的纪念品](https://github.com/machawk1/awesome-memento)
* [WARC 生态系统](http://www.archiveteam.org/index.php?title=The_WARC_Ecosystem)
* [COPTR 的网络爬虫部分](http://coptr.digipres.org/Category:Web_Crawl)

### 博客和奖学金

* [IIPC 博客](https://netpreserveblog.wordpress.com/)
* [Web Archiving Roundtable](https://webarchivingrt.wordpress.com/) - [美国档案工作者协会](https://www2.archivists.org/) 网络归档圆桌会议的非官方博客，由网络归档圆桌会议成员维护。
* [The Web as History](https://www.uclpress.co.uk/products/84010) - 一本开源书籍，提供了网络归档研究的概念概述以及一些案例研究。
* [WS-DL Blog](https://ws-dl.blogspot.com/) - 网络科学和数字图书馆研究小组关于各种网络归档相关主题、学术工作和学术旅行报告的博客。
* [DSHR's Blog](https://blog.dshr.org/) - David Rosenthal 定期回顾和总结数字保存领域所做的工作。
* [英国网络档案博客](https://blogs.bl.uk/webarchive/)
* [Common Crawl Foundation Blog](https://commoncrawl.org/blog) - [rss](http://commoncrawl.org/blog/rss.xml)

### 邮件列表

* [普通爬行](https://groups.google.com/g/common-crawl)
* [IIPC](http://netpreserve.org/about-us/iipc-mailing-list/)
* [OpenWayback](https://groups.google.com/g/openwayback-dev)
* [WASAPI](https://groups.google.com/g/wasapi-community)

### 松弛

* [IIPC Slack](https://iipc.slack.com/) - 请求 [@netpreserve](https://twitter.com/NetPreserve?s=20) 获取访问权限。
* [Archives Unleashed Slack](https://archivesunleashed.slack.com/) - [填写此申请表](http://slack.archivesunleashed.org/)，以访问从事网络档案工作的研究人员小组。
* [Archivers Slack](https://archivers.slack.com) - [邀请自己](https://archivers-slack.herokuapp.com/) 参与与 [EDGI](https://envirodatagov.org/archiving/) 和 [Data Together](http://datatogether.org/) 合作运行的多学科归档项目。
* [Common Crawl 基金会合作伙伴](https://ccfpartners.slack.com/)（向 greg zat commoncrawl zot org 索要邀请）

### 不和谐

* [通用爬行基金会](https://discord.gg/njaVFh7avF)

### 推特

* [@commoncrawl](https://twitter.com/commoncrawl) - Common Crawl 基金会官方句柄。
* [@NetPreserve](https://twitter.com/NetPreserve) - IIPC 官方手柄。
* [@WebSciDL](https://twitter.com/WebSciDL) - ODU 网络科学和数字图书馆研究组。
* [#WebArchiving](https://twitter.com/search?q=%23webarchiving)
* [#WebArchiveWednesday](https://twitter.com/hashtag/webarchivewednesday)

## 网络归档服务提供商

我们的目的是仅列出允许以标准格式（WARC 或 WACZ）导出 Web 档案的服务。但这并不是对这些服务的认可，读者应该根据自己的需求检查和评估这些选项。

### 自托管、开源

* [Browsertrix](https://webrecorder.net/browsertrix/) - 来自 [Webrecorder](https://webrecorder.net/)，源代码位于 <https://github.com/webrecorder/browsertrix>。
* [Conifer](https://conifer.rhizome.org/) - 来自 [Rhizome](https://rhizome.org/)，来源可在 <https://github.com/Rhizome-Conifer> 获取。

### 托管、闭源

* [Archive-It](https://archive-it.org/) - 来自互联网档案馆。
* [Arkiwera](https://arkiwera.se/wp/websites/)
*	[Hanzo](https://www.hanzo.co/chronicle)
*	[MirrorWeb](https://www.mirrorweb.com/solutions/capabilities/website-archiving)
*	[PageFreezer](https://www.pagefreezer.com/)
*	[Smarsh](https://www.smarsh.com/platform/compliance-management/web-archive)

## 公开数据

这是公开可用的 WARC、Wayback Machine、CDX API 端点、其他索引等的列表。

* [Common Crawl files](https://data.commoncrawl.org/) - WARC、CDX 文件、parquet url 索引、parquet 主机索引等。
* [通用抓取 CDX API](https://index.commoncrawl.org/)
* [End of Term Archive](https://eotarchive.org/) - WARC、CDX 文件、parquet url 索引
* [互联网档案馆回顾](https://web.archive.org/)
* [Webrecorder US GovArchive](https://govarchive.us/) - 高保真回放
* [UK Government Web Archive](https://www.nationalarchives.gov.uk/webarchive/) - 回溯
