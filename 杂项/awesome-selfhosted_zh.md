# 很棒-自托管

[![Awesome](_static/awesome.png)](https://github.com/sindresorhus/awesome) [![](https://github.com/awesome-selfhosted/awesome-selfhosted-data/actions/workflows/check-dead-links.yml/badge.svg)](https://github.com/awesome-selfhosted/awesome-selfhosted-data/issues/1) [![](https://github.com/awesome-selfhosted/awesome-selfhosted-data/actions/workflows/check-unmaintained-projects.yml/badge.svg)](https://github.com/awesome-selfhosted/awesome-selfhosted-data/issues/1) [![](https://img.shields.io/liberapay/goal/awesome-selfhosted?logo=liberapay)](https://liberapay.com/awesome-selfhosted/)

自托管是在您自己的服务器上托管和管理应用程序的做法，而不是从 [SaaSS](https://www.gnu.org/philosophy/who-does-that-server-really-serve.html) 提供商使用应用程序。

这是可以托管在您自己的服务器上的[免费](https://en.wikipedia.org/wiki/Free_software)软件[网络服务](https://en.wikipedia.org/wiki/Network_service)和[网络应用程序](https://en.wikipedia.org/wiki/Web_application)的列表。非自由软件列在 [非自由](https://github.com/awesome-selfhosted/awesome-selfhosted/blob/master/non-free.md) 页面上。

**[HTML 版本](https://awesome-selfhosted.net/)（推荐）**，[Markdown 版本](https://github.com/awesome-selfhosted/awesome-selfhosted)（旧版）。

请参阅[贡献](#contributing)。

--------------------

## 目录

- [Software](#software)
  - [Analytics](#analytics)
  - [归档和数字保存 (DP)](#archiving-and-digital-preservation-dp)
  - [Automation](#automation)
  - [Backup](#backup)
  - [博客平台](#blogging-platforms)
  - [预订和安排](#booking-and-scheduling)
  - [书签和链接共享](#bookmarks-and-link-sharing)
  - [日历和联系人](#calendar--contacts)
  - [通讯 - 定制通讯系统](#communication---custom-communication-systems)
  - [通讯 - 电子邮件 - 完整解决方案](#communication---email---complete-solutions)
  - [通讯 - 电子邮件 - 邮件递送代理](#communication---email---mail-delivery-agents)
  - [通讯 - 电子邮件 - 邮件传输代理](#communication---email---mail-transfer-agents)
  - [通讯 - 电子邮件 - 邮件列表和时事通讯](#communication---email---mailing-lists-and-newsletters)
  - [通讯 - 电子邮件 - 网络邮件客户端](#communication---email---webmail-clients)
  - [通讯-IRC](#communication---irc)
  - [通讯-SIP](#communication---sip)
  - [沟通 - 社交网络和论坛](#communication---social-networks-and-forums)
  - [通讯 - 视频会议](#communication---video-conferencing)
  - [通信 - XMPP - 服务器](#communication---xmpp---servers)
  - [通信 - XMPP - Web 客户端](#communication---xmpp---web-clients)
  - [社区支持农业 (CSA)](#community-supported-agriculture-csa)
  - [会议管理](#conference-management)
  - [内容管理系统 (CMS)](#content-management-systems-cms)
  - [客户关系管理（CRM）](#customer-relationship-management-crm)
  - [数据库管理](#database-management)
  - [DNS](#dns)
  - [文件管理](#document-management)
  - [文档管理 - 电子书](#document-management---e-books)
  - [文档管理 - 机构存储库和数字图书馆软件](#document-management---institutional-repository-and-digital-library-software)
  - [文档管理 - 综合图书馆系统 (ILS)](#document-management---integrated-library-systems-ils)
  - [E-commerce](#e-commerce)
  - [联合身份和认证](#federated-identity--authentication)
  - [饲料读者](#feed-readers)
  - [文件传输和同步](#file-transfer--synchronization)
  - [文件传输 - 分布式文件系统](#file-transfer---distributed-filesystems)
  - [文件传输 - 对象存储和文件服务器](#file-transfer---object-storage--file-servers)
  - [文件传输 - 点对点文件共享](#file-transfer---peer-to-peer-filesharing)
  - [文件传输 - 单击和拖放上传](#file-transfer---single-click--drag-n-drop-upload)
  - [文件传输 - 基于 Web 的文件管理器](#file-transfer---web-based-file-managers)
  - [Games](#games)
  - [游戏 - 管理实用程序和控制面板](#games---administrative-utilities--control-panels)
  - [Genealogy](#genealogy)
  - [生成人工智能（GenAI）](#generative-artificial-intelligence-genai)
  - [Groupware](#groupware)
  - [健康与健身](#health-and-fitness)
  - [人力资源管理（HRM）](#human-resources-management-hrm)
  - [身份管理](#identity-management)
  - [物联网 (IoT)](#internet-of-things-iot)
  - [库存管理](#inventory-management)
  - [知识管理工具](#knowledge-management-tools)
  - [学习和课程](#learning-and-courses)
  - [Manufacturing](#manufacturing)
  - [地图和全球定位系统 (GPS)](#maps-and-global-positioning-system-gps)
  - [媒体管理](#media-management)
  - [媒体流](#media-streaming)
  - [媒体流 - 音频流](#media-streaming---audio-streaming)
  - [媒体流 - 多媒体流](#media-streaming---multimedia-streaming)
  - [媒体流 - 视频流](#media-streaming---video-streaming)
  - [Miscellaneous](#miscellaneous)
  - [资金、预算和管理](#money-budgeting--management)
  - [监控和状态页面](#monitoring--status-pages)
  - [网络实用程序](#network-utilities)
  - [笔记和编辑](#note-taking--editors)
  - [办公套房](#office-suites)
  - [密码管理器](#password-managers)
  - [Pastebins](#pastebins)
  - [个人仪表板](#personal-dashboards)
  - [照片画廊](#photo-galleries)
  - [民意调查和活动](#polls-and-events)
  - [Proxy](#proxy)
  - [菜谱管理](#recipe-management)
  - [远程访问](#remote-access)
  - [资源规划](#resource-planning)
  - [搜索引擎](#search-engines)
  - [自托管解决方案](#self-hosting-solutions)
  - [软件开发](#software-development)
  - [软件开发-API管理](#software-development---api-management)
  - [软件开发 - 持续集成和部署](#software-development---continuous-integration--deployment)
  - [软件开发 - FaaS 和无服务器](#software-development---faas--serverless)
  - [软件开发 - 功能切换](#software-development---feature-toggle)
  - [软件开发 - IDE 和工具](#software-development---ide--tools)
  - [软件开发 - 本地化](#software-development---localization)
  - [软件开发 - 低代码](#software-development---low-code)
  - [软件开发-项目管理](#software-development---project-management)
  - [软件开发-测试](#software-development---testing)
  - [静态站点生成器](#static-site-generators)
  - [任务管理和待办事项列表](#task-management--to-do-lists)
  - [Ticketing](#ticketing)
  - [时间追踪](#time-tracking)
  - [网址缩短器](#url-shorteners)
  - [视频监控](#video-surveillance)
  - [VPN](#vpn)
  - [网络服务器](#web-servers)
  - [Wikis](#wikis)
- [许可证清单](#list-of-licenses)
- [Anti-features](#anti-features)
- [外部链接](#external-links)
- [Contributing](#contributing)
- [License](#license)

--------------------

## 软件

### 分析

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

[分析](https://en.wikipedia.org/wiki/Analytics) 是对数据或统计数据的系统计算分析。它用于发现、解释和交流数据中有意义的模式。

_相关：[数据库管理](#database-management)、[个人仪表板](#personal-dashboards)_

- [ANALOG](https://github.com/orangecoloured/analog) - 一个最小的分析工具。跟踪 10-30 天内的事件。 `MIT` `Nodejs/Docker`
- [Aptabase](https://aptabase.com/) - 隐私第一以及针对移动和桌面应用程序的简单分析。 ([源代码](https://github.com/aptabase/aptabase)) `AGPL-3.0` `Docker`
- [AWStats](http://www.awstats.org/) - 从 Web、流媒体、FTP 或邮件服务器日志文件生成统计数据。 ([演示](https://www.awstats.org/#DEMO), [源代码](https://github.com/eldy/awstats)) `GPL-3.0` `Perl`
- [Countly Community Edition](https://count.ly) - 实时移动和网络分析、崩溃报告和推送通知平台。 ([源代码](https://github.com/Countly/countly-server)) `AGPL-3.0` `Nodejs/Docker`
- [d8a.tech](https://d8a.tech) - 一种数据收集服务，可与您现有的 Google Analytics 设置配合使用，捕获用户活动并将其直接发送到您自己的私人数据库。 ([演示](https://lookerstudio.google.com/u/0/reporting/0e4102b6-c38b-4f55-aa25-c1fe91d1c1e9), [源代码](https://github.com/d8a-tech/d8a)) `MIT` `Go/Docker`
- [Daily Stars Explorer](https://emanuelef.github.io/daily-stars-explorer) `⚠` - 通过每日明星洞察跟踪 GitHub 存储库趋势，以了解随着时间的推移的增长和社区兴趣。 ([演示](https://emanuelef.github.io/daily-stars-explorer), [源代码](https://github.com/emanuelef/daily-stars-explorer)) `MIT` `Go/Nodejs/Docker`
- [Druid](https://druid.apache.org) - 分布式、面向列的实时分析数据存储。 ([源代码](https://github.com/apache/druid)) `Apache-2.0` `Java/Docker`
- [EDA](https://github.com/jortilles/EDA) - 用于数据分析和可视化的 Web 应用程序。 `AGPL-3.0` `Nodejs/Docker`
- [GoAccess](http://goaccess.io/) - 在终端中运行的实时 Web 日志分析器和交互式查看器。 ([源代码](https://github.com/allinurl/goaccess)) `GPL-2.0` `C`
- [GoatCounter](https://www.goatcounter.com) - 轻松进行网络统计，无需跟踪个人数据。 ([源代码](https://github.com/arp242/goatcounter)) `EUPL-1.2` `Go`
- [HitKeep](https://hitkeep.com/) - 隐私优先的 Web 分析，在带有嵌入式 DuckDB（替代 Google Analytics、Plausible、Umami）的单个二进制文件中提供目标、渠道、电子商务跟踪和团队管理。 ([源代码](https://github.com/pascalebeier/hitkeep)) `MIT` `Go/Docker`
- [Litlyx](https://litlyx.com) - 一体化分析解决方案。 30 秒内完成设置。在人工智能驱动的仪表板上显示您的所有数据。完全自我托管且符合 GDPR。 ([源代码](https://github.com/Litlyx/litlyx)) `Apache-2.0` `Docker`
- [Liwan](https://liwan.dev/) - 隐私第一的网络分析。 ([演示](https://demo.liwan.dev/p/liwan.dev), [源代码](https://github.com/explodingcamera/liwan)) `Apache-2.0` `Rust/Docker`
- [Matomo](https://matomo.org/) - 保护您的数据和客户隐私的网络分析（替代 Google Analytics）。 ([源代码](https://github.com/matomo-org/matomo)) `GPL-3.0` `PHP`
- [Medama Analytics](https://oss.medama.io) - 隐私第一的网站分析。小巧、简单且无 cookie。 ([演示](https://demo.medama.io), [源代码](https://github.com/medama-io/medama)) `Apache-2.0/MIT` `Docker/Go`
- [Metabase](https://metabase.com/) - 公司中的每个人都可以轻松提问并从数据中学习。 ([源代码](https://github.com/metabase/metabase)) `AGPL-3.0` `Java/Docker`
- [Middleware](https://middlewarehq.com/) - 旨在帮助工程领导者使用 DORA 指标衡量和分析其团队效率的工具。 ([源代码](https://github.com/middlewarehq/middleware)) `Apache-2.0` `Docker/Python/Nodejs`
- [Netron](https://netron.app/) - 用于神经网络和机器学习模型的可视化工具。 ([源代码](https://github.com/lutzroeder/netron)) `MIT` `Python/Nodejs`
- [Offen](https://www.offen.dev/) - 公平、轻量级和开放的网络分析工具。当您的用户可以完全访问其数据时获得见解。 ([演示](https://www.offen.dev/try-demo/), [源代码](https://github.com/offen/offen)) `Apache-2.0` `Go/Docker`
- [Plausible Analytics](https://plausible.io/) - 简单、轻量级 (< 1 KB) 且保护隐私的网络分析。 ([源代码](https://github.com/plausible/analytics/)) `AGPL-3.0` `Elixir`
- [PostHog](https://posthog.com) - 您可以自行托管产品分析、会话记录、功能标记和 A/B 测试（替代 Mixpanel、Amplitude、Heap、HotJar、Optimizely）。 ([源代码](https://github.com/posthog/posthog)) `MIT` `Python`
- [Postiz](https://postiz.com) `⚠` - 安排帖子、跟踪内容的表现并在一处管理所有社交媒体帐户（Buffer、Hootsuite、Sprout Social 的替代方案）。 ([源代码](https://github.com/gitroomhq/postiz-app)) `AGPL-3.0` `Docker`
- [Prisme Analytics](https://www.prismeanalytics.com) - 基于 Grafana 的注重隐私的渐进式分析服务。 ([源代码](https://github.com/prismelabs/analytics)) `AGPL-3.0/MIT` `Docker`
- [Redash](http://redash.io) - 连接和查询您的数据源，构建仪表板以可视化数据并与您的公司共享它们。 ([源代码](https://github.com/getredash/redash)) `BSD-2-Clause` `Docker`
- [Rybbit](https://rybbit.com/) - 易于设置且更直观的网络和产品分析（替代 Google Analytics）。 ([演示](https://demo.rybbit.com/1), [源代码](https://github.com/rybbit-io/rybbit)) `AGPL-3.0` `Docker`
- [Shaper](https://taleshape.com/shaper/docs) - 全部使用 SQL 构建数据仪表板。由 DuckDB 提供支持。 ([演示](https://demo.taleshape.com/view/pvggvdpiwb9wlyppuqbyx0nt), [源代码](https://github.com/taleshape-com/shaper)) `MPL-2.0` `Docker/Nodejs/Python/Go`
- [Socioboard](https://github.com/socioboard/Socioboard-5.0) `⚠` - 社交媒体管理、分析和报告平台，支持九个开箱即用的社交媒体网络。 `GPL-3.0` `Nodejs`
- [Strava 统计](https://github.com/robiningelbrecht/statistics-for-strava) `⚠` - 根据 Strava 数据生成的统计仪表板。 ([演示](https://statistics-for-strava.robiningelbrecht.be/)) `AGPL-3.0` `Docker`
- [Superset](http://superset.apache.org/) - 现代数据探索和可视化平台。 ([源代码](https://github.com/apache/superset)) `Apache-2.0` `Python`
- [Swetrix](https://swetrix.com/) - 终极开源网络分析可满足您的所有需求。 ([演示](https://swetrix.com/projects/STEzHcB1rALV), [源代码](https://github.com/Swetrix/selfhosting)) `AGPL-3.0` `Docker`
- [Umami](https://umami.is/) - 简单、快速、注重隐私的 Google Analytics 替代方案。 ([演示](https://cloud.umami.is/share/LGazGOecbDtaIwDr), [源代码](https://github.com/umami-software/umami)) `MIT` `Nodejs/Docker`
- [Vince](https://www.vinceanalytics.com/) - 网络分析和仪表板（Google Analytics 的替代方案）。 ([源代码](https://github.com/vinceanalytics/vince)) `AGPL-3.0` `Go/Docker/K8S/deb`


### 归档和数字保存 (DP)

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

数字[归档](https://en.wikipedia.org/wiki/Archival_science)和[保存](https://en.wikipedia.org/wiki/Digital_preservation)软件。

_相关：[备份](#backup)、[内容管理系统 (CMS)](#content-management-systems-cms)_

_另请参阅：[awesome-web-archiving](https://github.com/iipc/awesome-web-archiving)_

- [ArchiveBox](https://archivebox.io/) - 从书签、浏览历史记录、RSS 提要或其他来源（替代 Wayback Machine）创建网站的 HTML 和屏幕截图存档。 ([演示](https://demo.archivebox.io/), [源代码](https://github.com/ArchiveBox/ArchiveBox)) `MIT` `Python/Docker`
- [ArchivesSpace](https://archivesspace.org/) - 档案信息管理应用程序，用于管理和提供对档案、手稿和数字对象的 Web 访问。 ([演示](https://archivesspace.org/application/sandbox), [源代码](https://github.com/archivesspace/archivesspace)) `ECL-2.0` `Ruby`
- [Bichon](https://github.com/rustmailer/bichon) - 电子邮件存档服务器，从 IMAP 帐户同步、索引电子邮件以进行全文搜索并提供 REST API。无需外部数据库，包括具有多帐户支持的 WebUI。 `AGPL-3.0` `Rust/Docker`
- [bitmagnet](https://bitmagnet.io) - BitTorrent 索引器、DHT 爬虫、内容分类器和 Torrent 搜索引擎，具有 Web UI、GraphQL API 和 Servarr 堆栈集成。 ([源代码](https://github.com/bitmagnet-io/bitmagnet)) `MIT` `Go/Docker`
- [CKAN](https://ckan.org) - 制作开放数据网站。 ([源代码](https://github.com/ckan/ckan)) `AGPL-3.0` `Python`
- [Collective Access - Providence](https://collectiveaccess.org/) - 高度可配置的基于 Web 的框架，用于管理、描述和发现数字和物理馆藏，支持各种元数据标准、数据类型和媒体格式。 ([源代码](https://github.com/collectiveaccess/providence)) `GPL-3.0` `PHP`
- [Eonvelope](https://dacid99.gitlab.io/eonvelope) - 电子邮件存档软件可让您无限期地长期保存电子邮件。 ([源代码](https://gitlab.com/dacid99/eonvelope)) `AGPL-3.0` `K8S/Docker`
- [Ganymede](https://github.com/Zibbp/ganymede) `⚠` - Twitch VOD 和直播流存档平台。包括每个存档的渲染聊天。 `GPL-3.0` `Docker`
- [mail-archiver](https://github.com/s1t5/mail-archiver) - 用于从多个帐户（IMAP、M365 或导入）归档、搜索和导出电子邮件的 Web 应用程序。具有文件夹同步、附件支持、邮箱迁移和仪表板。 `GPL-3.0` `Docker`
- [Omeka S](https://omeka.org/s/) - 下一代网络出版平台，适合有兴趣将数字文化遗产藏品与其他在线资源连接起来的机构。 ([源代码](https://github.com/omeka/omeka-s)) `GPL-3.0` `Nodejs`
- [Open Archiver](https://openarchiver.com/) - 具有全文搜索和电子数据展示搜索功能的电子邮件归档解决方案。 ([演示](https://github.com/LogicLabs-OU/OpenArchiver?tab=readme-ov-file#-live-demo), [源代码](https://github.com/LogicLabs-OU/OpenArchiver)) `AGPL-3.0` `Docker`
- [Piler](https://www.mailpiler.org/) - 功能丰富的电子邮件归档解决方案。 ([源代码](https://github.com/jsuto/piler/)) `GPL-3.0` `C/Docker/deb`
- [Wallabag](https://www.wallabag.org) - Wallabag（以前称为 Poche）是一个 Web 应用程序，允许您保存文章以供以后阅读，并提高可读性。 ([源代码](https://github.com/wallabag/wallabag)) `MIT` `PHP`
- [Wayback](https://github.com/wabarc/wayback) - 一个自托管工具包，用于将网页存档到互联网档案馆、archive.today、IPFS 和本地文件系统。 `GPL-3.0` `开始`


### 自动化

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

[自动化](https://en.wikipedia.org/wiki/Automation) 旨在减少流程中的人为干预的软件。

_相关：[物联网 (IoT)](#internet-of-things-iot)、[软件开发 - 持续集成和部署](#software-development---持续集成--部署)、[媒体管理](#media-management)_

- [Activepieces](https://www.activepieces.com) - 无代码业务自动化工具，例如 Zapier 或 Tray。例如，您可以为每张新的 Trello 卡发送 Slack 通知。 ([源代码](https://github.com/activepieces/activepieces)) `MIT` `Docker`
- [Apache Airflow](https://airflow.apache.org/) - 以编程方式创作、安排和监控工作流程的平台。 ([源代码](https://github.com/apache/airflow/)) `Apache-2.0` `Python/Docker`
- [Automatisch](https://automatisch.io) - 业务自动化工具，可让您连接 Twitter、Slack 等不同服务来自动化您的业务流程（Zapier 的替代方案）。 ([源代码](https://github.com/automatisch/automatisch)) `AGPL-3.0` `Docker`
- [BookBounty](https://github.com/TheWicklowWolf/BookBounty) `⚠` - 从 Library Genesis 中检索丢失的 Readarr 书籍。 `MPL-2.0` `Docker`
- [changedetection.io](https://changedetection.io/) - 及时了解网站内容的变化。 ([源代码](https://github.com/dgtlmoon/changedetection.io)) `Apache-2.0` `Python/Docker`
- [ChiefOnboarding](https://chiefonboarding.com) - 员工入职平台，允许您配置用户帐户并使用待办事项、资源、文本/电子邮件/Slack 消息等创建序列！可作为门户网站和 Slack 机器人使用。 ([源代码](https://github.com/chiefonboarding/ChiefOnboarding)) `AGPL-3.0` `Docker`
- [Cronicle](https://cronicle.net/) - 简单的分布式任务调度程序和运行程序，具有基于 Web 的 UI。 ([源代码](https://github.com/jhuckaby/Cronicle)) `MIT` `Nodejs`
- [Cronmaster](https://github.com/fccview/cronmaster) - Cronjob 管理 UI 具有人类可读的语法、实时日志记录和 cronjobs 的日志历史记录。 `AGPL-3.0` `Docker`
- [Dagu](https://docs.dagu.cloud/) - 具有 Web UI 的强大 Cron 替代方案。它允许您以声明性 YAML 格式将命令之间的依赖关系定义为有向无环图 (DAG)。 ([源代码](https://github.com/dagucloud/dagu)) `GPL-3.0` `Go/Docker`
- [Discount Bandit](https://discount-bandit.cybrarist.com/) `⚠` - 跟踪 Amazon、Ebay、Walmart 等多个商店的产品定价、库存状态。（[源代码](https://github.com/Cybrarist/Discount-Bandit)) `GPL-3.0` `PHP/Docker`
- [Dittofeed](https://www.dittofeed.com) - 全渠道客户参与和消息自动化平台（Braze、Customer.io、Iterable 的替代品）。 ([演示](https://demo.dittofeed.com/dashboard/journeys), [源代码](https://github.com/dittofeed/dittofeed)) `MIT` `Docker`
- [feedmixer](https://github.com/cristoper/feedmixer) - 微型 Web 服务，获取提要 URL 列表并返回一个新提要，该新提要由每个给定提要中的最新 n 个条目组成（返回 Atom、RSS 或 JSON）。 ([演示](https://mretc.net/feedmixer/json?f=https://hnrss.org/newest&f=https://americancynic.net/atom.xml&n=1)) `WTFPL` `Python`
- [flowctl](https://flowctl.net) - 具有审批、远程执行和调度功能的自助工作流程执行平台。 ([演示](https://demo.flowctl.net), [源代码](https://github.com/cvhariharan/flowctl)) `Apache-2.0` `Go/Docker`
- [Fredy](https://fredy.orange-coding.net/) `⚠` - 在 ImmoScout24、Immowelt 等平台上搜索德国的新公寓、房屋和公寓，并通过 Slack、Telegram 等立即将结果发送给您。 ([演示](https://fredy-demo.orange-coding.net), [源代码](https://github.com/orangecoding/fredy)) `Apache-2.0` `Nodejs/Docker`
- [Github Ntfy](https://github.com/BreizhHardware/ntfy_alerts) `⚠` - 当 Docker Hub 或 Github 上有新版本可用时，将通知推送到 NTFY、Gotify、Discord 或 Slack。 ([客户端](https://github.com/binwiederhier/ntfy)) `GPL-3.0` `Rust/Docker`
- [gocron](https://github.com/flohoss/gocron) - 任务调度程序允许用户通过简单的 YAML 配置文件指定重复作业。 `麻省理工学院` `Docker`
- [HandBrake Web](https://github.com/TheNickOfTime/handbrake-web) - 通过 Web 界面在无头设备上使用一个或多个 HandBrake 视频转码器实例。 `AGPL-3.0` `Docker`
- [Healthchecks](https://healthchecks.io/) - 监听 ping 并在 ping 延迟时发送警报。 ([源代码](https://github.com/healthchecks/healthchecks)) `BSD-3-Clause` `Python/Docker`
- [Huginn](https://github.com/huginn/huginn) - 建立代表您进行监控和行动的代理。 “麻省理工学院”“红宝石”
- [Kestra](https://kestra.io) - 事件驱动、与语言无关的平台，用于创建、安排和监控工作流程。在代码中。协调数据管道和任务，例如 ETL 和 ELT。 ([源代码](https://github.com/kestra-io/kestra)) `Apache-2.0` `Docker`
- [Kibitzr](https://kibitzr.github.io) - 具有强大集成功能的轻量级个人网络助手。 ([源代码](https://github.com/kibitzr/kibitzr)) `MIT` `Python`
- [LazyLibrarian](https://gitlab.com/LazyLibrarian/LazyLibrarian) `⚠` - 关注作者并获取元数据以满足您的所有数字阅读需求。它结合使用 Goodreads、Librarything 和可选的 GoogleBooks 作为作者信息和图书信息的来源。 `GPL-3.0` `Python`
- [Leon](https://getleon.ai) - 可以驻留在您的服务器上的私人助理。 ([源代码](https://github.com/leon-ai/leon)) `MIT` `Nodejs`
- [Matchering](https://github.com/sergree/matchering) - 自动音乐母带处理（替代 LANDR、eMastered 和 MajorDecibel）。 `GPL-3.0` `Docker`
- [Mylar3](https://mylarcomics.com/) - 用于 NZB 和 torrent 的自动漫画书 (cbr/cbz) 下载程序。 ([源代码](https://github.com/mylar3/mylar3)) `GPL-3.0` `Python/Docker`
- [OliveTin](https://www.olivetin.app/) - 用于运行 Linux shell 命令的 Web 界面。 ([源代码](https://github.com/OliveTin/OliveTin)) `AGPL-3.0` `Go`
- [pyLoad](https://pyload.net/) - 轻量级、可定制且可远程管理的下载器，适用于rapidshare.com或uploaded.to等一键托管网站。 ([源代码](https://github.com/pyload/pyload)) `AGPL-3.0` `Python`
- [StackStorm](https://stackstorm.com) - StackStorm（又名_IFTTT for Ops_）是事件驱动的自动化，用于自动修复、安全响应、故障排除、部署等。包括规则引擎、工作流程、160 个集成包（包含 6000 多个操作）和 ChatOps。 ([源代码](https://github.com/StackStorm/st2)) `Apache-2.0` `Python`
- [µTask](https://github.com/ovh/utask) - 对 yaml 中声明的业务流程进行建模和执行的自动化引擎。 `BSD-3-Clause` `Go/Docker`


### 备份

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

[备份](https://en.wikipedia.org/wiki/Backup)软件。

**请访问[awesome-sysadmin/Backups](https://github.com/awesome-foss/awesome-sysadmin#backups)**

_相关：[归档和数字保存 (DP)](#archiving-and-digital-preservation-dp)_



### 博客平台

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

[博客](https://en.wikipedia.org/wiki/Blog) 是一个由离散的日记式文本条目（帖子）组成的讨论或信息网站。

_相关：[静态站点生成器](#static-site-generators)、[内容管理系统 (CMS)](#content-management-systems-cms)_

_另请参阅：[WeblogMatrix](https://www.weblogmatrix.org/)_

- [Antville](https://antville.org) - 免费的开源项目旨在开发高性能、功能丰富的博客托管软件。 ([源代码](https://github.com/antville/antville)) `Apache-2.0` `Javascript`
- [Castopod](https://castopod.org) - 播客管理托管平台，包括最新的播客 2.0 标准、自动 Fediverse 源、分析、嵌入式播放器等。 ([源代码](https://code.castopod.org/adaures/castopod)) `AGPL-3.0` `PHP/Docker`
- [Chyrp Lite](https://chyrplite.net) - 超棒、超轻量级的博客引擎。 ([源代码](https://github.com/xenocrat/chyrp-lite)) `BSD-3-Clause` `PHP`
- [Dotclear](https://git.dotclear.org/dev/dotclear) - 掌控您的博客。 `GPL-2.0` `PHP`
- [Ech0](https://echo.soopy.cn/) - 专注于个人想法共享的轻量级联合发布平台（中文文档）。 ([演示](https://memo.vaaat.com/), [源代码](https://github.com/lin-snow/Ech0)) `AGPL-3.0` `Docker/K8S`
- [FlatPress](https://flatpress.org/) - 一个轻量级、易于设置的平面文件博客引擎。 ([源代码](https://github.com/flatpressblog/flatpress)) `GPL-2.0` `PHP`
- [fx](https://github.com/rikhuijzer/fx) - 微博工具，提供内置语法突出显示、移动发布等功能（替代 Twitter、Bluesky）。 `麻省理工学院` `Docker`
- [Ghost](https://ghost.org/) - 只是一个博客平台。 ([源代码](https://github.com/TryGhost/Ghost)) `MIT` `Nodejs`
- [Haven](https://havenweb.org/) - 带有 Markdown 编辑功能和内置 RSS 阅读器的私人博客系统。 ([演示](https://havenweb.org/demo.html), [源代码](https://github.com/havenweb/haven)) `MIT` `Ruby`
- [HTMLy](https://www.htmly.com/) - 无数据库 PHP 博客平台。平面文件 CMS，可让您在几秒钟内创建快速、安全且功能强大的网站或博客。 ([演示](http://demo.htmly.com/), [源代码](https://github.com/danpros/htmly)) `GPL-2.0` `PHP`
- [Known](https://withknown.com/) - 协作社交发布平台。 ([源代码](https://github.com/idno/idno)) `Apache-2.0` `PHP`
- [Mataroa](https://mataroa.blog/) - 极简主义者的裸体博客平台。 ([源代码](https://github.com/mataroablog/mataroa)) `MIT` `Python`
- [PluXml](https://pluxml.org) - 基于 XML 的博客/CMS 平台。 ([源代码](https://github.com/pluxml/PluXml)) `GPL-3.0` `PHP`
- [Serendipity](https://docs.s9y.org/) - Serendipity (s9y) 是一个使用 Smarty 模板的高度可扩展和可定制的 PHP 博客引擎。 ([源代码](https://github.com/s9y/serendipity)) `BSD-3-Clause` `PHP`
- [WriteFreely](https://writefreely.org) - 编写用于创建极简主义联合博客或整个社区的软件。 ([源代码](https://github.com/writefreely/writefreely)) `AGPL-3.0` `Go`


### 预订和安排

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

活动安排、预订和约会管理软件。

_相关：[民意调查和活动](#polls-and-events)、[群件](#groupware)_

- [Alf.io](https://alf.io/) - 门票预订系统。 ([演示](https://demo.alf.io/authentication), [源代码](https://github.com/alfio-event/alf.io)) `GPL-3.0` `Java`
- [Cal.diy](https://cal.diy/) - 在线预约安排系统。 ([源代码](https://github.com/calcom/cal.diy)) `MIT` `Nodejs`
- [Easy!Appointments](https://easyappointments.org/) - 允许您的客户通过网络与您预约。 ([演示](https://demo.easyappointments.org/), [源代码](https://github.com/alextselegidis/easyappointments)) `GPL-3.0` `PHP`
- [Hi.Events](https://hi.events) - 适用于会议、音乐会等的活动管理和票务平台。提供可定制的活动页面和可嵌入的票证小部件。 ([演示](https://demo.hi.events/event/1/dog-conf-2030), [源代码](https://github.com/HiEventsDev/hi.events)) `AGPL-3.0` `Docker`
- [LibreBooking](https://librebooking.readthedocs.io/) - 资源调度解决方案为组织提供灵活、移动友好且可扩展的界面来管理资源预留。 ([演示](https://librebooking-demo.fly.dev/), [源代码](https://github.com/LibreBooking/librebooking)) `GPL-3.0` `PHP/Docker`
- [QloApps](https://qloapps.com/) - 可定制且直观的基于网络的酒店预订系统和预订引擎。 ([演示](https://demo.qloapps.com/), [源代码](https://github.com/Qloapps/QloApps)) `OSL-3.0` `PHP/Nodejs`
- [Rallly](https://rallly.co) - 创建民意调查以对日期和时间进行投票（替代 Doodle）。 ([演示](https://app.rallly.co), [源代码](https://github.com/lukevella/rallly)) `AGPL-3.0` `Nodejs/Docker`
- [Seatsurfing](https://seatsurfing.app/) - 基于网络的应用程序，用于预订办公室的座位、办公桌和房间。 ([源代码](https://github.com/seatsurfing/seatsurfing)) `GPL-3.0` `Docker`


### 书签和链接共享

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

该软件允许用户添加、注释、编辑和共享网络文档的[书签](https://en.wikipedia.org/wiki/Bookmark_(digital))。

- [Betula](https://joinbetula.org) - 具有 Fediverse 支持和存档的单用户联合书签管理器。 ([源代码](https://codeberg.org/bouncepaw/betula)) `AGPL-3.0` `Go`
- [Buku](https://github.com/jarun/Buku) - 强大的书签管理器和个人文本迷你网络。 `GPL-3.0` `Python/deb`
- [Digibunch](https://ladigitale.dev/digibunch/#/) - 创建大量链接以与您的学习者或同事共享。 ([演示](https://ladigitale.dev/digibunch/#/b/5f67b12092b60), [源代码](https://codeberg.org/ladigitale/digibunch)) `AGPL-3.0` `Nodejs/PHP`
- [Espial](https://github.com/jonschoning/espial) - 一个开源的、基于网络的书签服务器。 `AGPL-3.0` `哈斯克尔`
- [Faved](https://faved.dev/) - 手工制作的书签管理器结合了强大的标签、即时搜索和干净、无干扰的界面。专为大型馆藏和高级工作流程而构建，针对效率和易用性进行了优化。 ([演示](https://demo.faved.dev/), [源代码](https://github.com/denho/faved)) `MIT` `Docker`
- [Firefox Account Server](https://mozilla-services.readthedocs.io/en/latest/howtos/run-fxa.html) - 托管您自己的 Firefox 帐户服务器。 ([源代码](https://github.com/mozilla/fxa)) `MPL-2.0` `Nodejs/Java`
- [Karakeep](https://karakeep.app/) - 为数据囤积者提供带有人工智能功能的书签应用程序。 ([演示](https://try.karakeep.app/signin), [源代码](https://github.com/karakeep-app/karakeep)) `AGPL-3.0` `Docker`
- [LinkAce](https://www.linkace.org/) - 书签归档，自动备份到互联网档案、链接监控和完整的 REST API。安装是通过 Docker 完成的，或者作为简单的 PHP 应用程序完成。 ([演示](https://demo.linkace.org/guest/links), [源代码](https://github.com/Kovah/LinkAce/)) `GPL-3.0` `Docker/PHP`
- [linkding](https://linkding.link/) - 最少的书签管理和快速、干净的用户界面。通过 Docker 安装简单，可以在 Raspberry Pi 上运行。 ([演示](https://demo.linkding.link/login/), [源代码](https://github.com/sissbruecker/linkding)) `MIT` `Docker`
- [LinkWarden](https://linkwarden.app/) - 书签和存档管理器可存储您有用的链接。 ([源代码](https://github.com/linkwarden/linkwarden)) `MIT` `Docker/Nodejs`
- [NeonLink](https://github.com/AlexSciFier/neonlink) - 书签服务具有独特的设计和简单的 Docker 安装。 `麻省理工学院` `Docker`
- [Readeck](https://readeck.org/en/) - 保存您喜欢并想要永久保留的网页的宝贵可读内容。将其视为书签管理器和稍后阅读工具。 ([源代码](https://codeberg.org/readeck/readeck), [客户端](https://codeberg.org/readeck/browser-extension)) `AGPL-3.0` `Go/Docker`
- [Servas](https://github.com/beromir/Servas) - 自托管书签管理工具。它允许使用标签、组和专门供以后访问的列表进行组织。它通过 2FA 支持多个用户。配套浏览器扩展适用于 Firefox 和 Chrome。 ([客户端](https://github.com/beromir/Servas#browser-extensions)) `GPL-3.0` `Docker/Nodejs/PHP`
- [Shaarli](https://github.com/shaarli/Shaarli) - 个人、简约、超快、无数据库书签和链接共享平台。 ([演示](https://demo.shaarli.org)) `Zlib` `PHP/deb`
- [Shiori](https://github.com/go-shiori/shiori) - 用 Go 构建的简单书签管理器。 `麻省理工学院``Go/Docker`
- [Slash](https://github.com/yourselfhosted/slash) - 一个开源、自托管的书签和链接共享平台。 `GPL-3.0` `Docker`
- [SyncMarks](https://codeberg.org/Offerel/SyncMarks-Webapp) - 同步和管理来自 Edge、Firefox 和 Chromium 的浏览器书签。 ([客户端](https://codeberg.org/Offerel/SyncMarks-Extension)) `AGPL-3.0` `PHP`


### 日历和联系人

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

[CalDAV](https://en.wikipedia.org/wiki/CalDAV) 和 [CardDAV](https://en.wikipedia.org/wiki/CardDAV) 用于[电子日历](https://en.wikipedia.org/wiki/Calendaring_software)、[通讯录](https://en.wikipedia.org/wiki/Address_book) 和 [联系人] 的协议服务器和 Web 客户端/界面管理](https://en.wikipedia.org/wiki/Contact_manager)。

_相关：[群件](#groupware)_

- [Baïkal](https://sabre.io/baikal/) - 基于 sabre/dav 的轻量级 CalDAV 和 CardDAV 服务器。 ([源代码](https://github.com/sabre-io/Baikal)) `GPL-3.0` `PHP`
- [DAViCal](https://www.davical.org/) - 使用 PostgreSQL 数据库作为数据存储的日历共享服务器 (CalDAV)。 ([源代码](https://gitlab.com/davical-project/davical)) `GPL-2.0` `PHP/deb`
- [Davis](https://github.com/tchapi/davis) - 一个简单、可 Docker 化且完全可翻译的 sabre/dav 管理界面，基于 Symfony 5 和 Bootstrap 4，很大程度上受到贝加尔湖的启发。 `麻省理工学院``PHP`
- [Keeper.sh](https://keeper.sh/) - 日历同步工具，可通过 iCal/ICS 或 OAuth 在日历源和目的地之间拉取和推送事件，并支持匿名繁忙/空闲事件。 ([源代码](https://github.com/ridafkih/keeper.sh)) `AGPL-3.0` `Docker`
- [Manage My Damn Life](https://intri.in/manage-my-damn-life/) - Manage my Damn Life (MMDL) 是一个自托管前端，用于管理您的 CalDAV 任务和日历。 ([源代码](https://github.com/intri-in/manage-my-damn-life-nextjs)) `GPL-3.0` `Nodejs/Docker`
- [Radicale](https://radicale.org/) - 简单的日历和联系人服务器，管理开销极低。 ([源代码](https://github.com/Kozea/Radicale)) `GPL-3.0` `Python/deb`
- [SabreDAV](https://sabre.io/) - 开源 CardDAV、CalDAV 和 WebDAV 框架和服务器。 ([源代码](https://github.com/sabre-io/dav)) `MIT` `PHP`
- [Xandikos](https://github.com/jelmer/xandikos) - 开源 CardDAV 和 CalDAV 服务器具有最小的管理开销，并由 Git 存储库支持。 `GPL-3.0` `Python/deb`


### 通讯 - 定制通讯系统

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

[通信软件](https://en.wikipedia.org/wiki/Communication_software) 用于提供对系统的远程访问，并使用自己的自定义协议在不同计算机或用户之间交换文本、音频和/或视频格式的文件和消息。

- [AnyCable](https://anycable.io/) - 实时服务器，用于通过 WebSocket、服务器发送事件等进行可靠的双向通信。（[演示](https://demo.anycable.io)、[源代码](https://github.com/anycable/anycable)) `MIT` `Go/Docker`
- [Apprise](https://github.com/caronc/apprise) - Apprise 允许您向当今我们可用的几乎所有最流行的通知服务发送通知，例如：Telegram、Discord、Slack、Amazon SNS、Gotify 等。 `MIT` `Python/Docker/deb`
- [Centrifugo](https://centrifugal.dev/) - 与语言无关的实时消息传递（Websocket 或 SockJS）服务器。 ([演示](https://github.com/centrifugal/centrifugo#demo), [源代码](https://github.com/centrifugal/centrifugo)) `MIT` `Go/Docker/K8S`
- [Chitchatter](https://chitchatter.im/) - 无服务器、去中心化且短暂的点对点聊天应用程序。 ([源代码](https://github.com/jeremyckahn/chitchatter)) `GPL-2.0` `Nodejs`
- [Conduit](https://conduit.rs/) - 由 Matrix 提供支持的简单、快速且可靠的聊天服务器。 ([源代码](https://gitlab.com/famedly/conduit)) `Apache-2.0` `Rust`
- [Continuwuity](https://continuwuity.org/) - 社区驱动的 Matrix homeserver，conduwuit 的延续，专注于用户体验和新功能（Conduit 的分支）。 ([源代码](https://forgejo.ellis.link/continuwuation/continuwuity)) `Apache-2.0` `Rust/Docker/K8S/deb`
- [Databag](https://github.com/balzack/databag) - 适用于 Web、iOS 和 Android 的联合端到端加密消息传递服务，支持文本、照片、视频以及 WebRTC 视频和音频通话。 ([演示](https://databag.coredb.org/#/create)) `Apache-2.0` `Docker`
- [Element](https://element.io) - 适用于 Web、iOS 和 Android 的全功能 Matrix 客户端。 ([源代码](https://github.com/element-hq/element-web)) `Apache-2.0` `Nodejs`
- [GlobaLeaks](https://www.globaleaks.org/) - 举报软件使任何人都可以轻松设置和维护安全的报告平台。 ([演示](https://demo.globaleaks.org), [源代码](https://github.com/globaleaks/globaleaks-whistleblowing-software)) `AGPL-3.0` `Python/deb/Docker`
- [GNUnet](https://gnunet.org/) - 用于分散式点对点网络的软件框架。 ([源代码](https://gnunet.org/git/)) `GPL-3.0` `C`
- [Gotify](https://gotify.net/) - 带有 Android 和 CLI 客户端的通知服务器（替代 PushBullet）。 ([源代码](https://github.com/gotify/server), [客户端](https://github.com/gotify/android)) `MIT` `Go/Docker`
- [Hyphanet](https://hyphanet.org/) - 匿名共享文件、浏览和发布_freesites_（只能通过 Hyphanet 访问的网站）并在论坛上聊天。 ([源代码](https://github.com/hyphanet/fred)) `GPL-2.0` `Java`
- [Jami](https://jami.net/) - 保护用户隐私和自由的通用通信平台。 ([源代码](https://git.jami.net/savoirfairelinux?sort=latest_activity_desc&filter=jami)) `GPL-3.0` `C++`
- [Live Helper Chat](https://livehelperchat.com/) - 您网站的实时支持聊天。 ([源代码](https://github.com/LiveHelperChat/livehelperchat)) `Apache-2.0` `PHP`
- [Mumble](https://wiki.mumble.info/wiki/Main_Page) - 低延迟、高质量的语音/文本聊天软件。 ([源代码](https://github.com/mumble-voip/mumble), [客户端](https://wiki.mumble.info/wiki/3rd_Party_Applications)) `BSD-3-Clause` `C++/deb`
- [Notifo](https://github.com/notifo-io/notifo) - 多通道通知服务器，支持电子邮件、移动推送、Web 推送、SMS、消息传递和 JavaScript 插件。 “麻省理工学院”“C#”
- [Novu](https://novu.co/) - 开发人员的通知基础设施。 ([源代码](https://github.com/novuhq/novu/)) `MIT` `Docker/Nodejs`
- [ntfy](https://ntfy.sh/) - 使用 HTTP PUT/POST、Android 应用程序、CLI 和 Web 应用程序将通知推送到手机或桌面，类似于 Pushover 和 Gotify。 ([演示](https://ntfy.sh/app), [源代码](https://github.com/binwiederhier/ntfy), [客户端](https://github.com/binwiederhier/ntfy-android)) `Apache-2.0/GPL-2.0` `Go/Docker/K8S`
- [One Time Secret](https://docs.onetimesecret.com) - 通过只能查看一次的自毁链接安全地共享敏感信息。 ([演示](https://onetimesecret.com), [源代码](https://github.com/onetimesecret/onetimesecret)) `MIT` `Docker/Ruby/Nodejs`
- [OTS](https://ots.fyi/) - 一次性秘密共享平台，在浏览器中具有对称 256 位 AES 加密。 ([源代码](https://github.com/Luzifer/ots)) `Apache-2.0` `Go`
- [PushBits](https://github.com/pushbits/server) - 用于通过 Matrix 中继推送通知的通知服务器，类似于 PushBullet 和 Gotify。 `ISC``去`
- [RetroShare](https://retroshare.cc) - 安全且分散的通信系统。提供分散的聊天、论坛、消息传递、文件传输。 ([源代码](https://github.com/RetroShare/RetroShare)) `GPL-2.0` `C++`
- [Rocket.Chat](https://rocket.chat/) - 将数据保护放在首位的通信平台（替代 Gitter.im 和 Slack）。 ([源代码](https://github.com/RocketChat/Rocket.Chat)) `MIT` `Nodejs/Docker/K8S`
- [SAMA](https://samacloud.io) - 下一代自托管聊天服务器和客户端。 ([演示](https://app.samacloud.io/demo), [源代码](https://github.com/SAMA-Communications/sama-server), [客户端](https://github.com/SAMA-Communications/sama-client)) `GPL-3.0` `Nodejs/Docker`
- [Screego](https://screego.net) - Screego 是一款简单的工具，可通过网络浏览器将您的屏幕快速共享给一个或多个人。 ([演示](https://app.screego.net/), [源代码](https://github.com/screego/server)) `GPL-3.0` `Docker/Go`
- [Shhh](https://github.com/smallwat3r/shhh) - 保护电子邮件或聊天日志中的秘密，并使用带有密码和到期日期的安全链接来共享它们。 “麻省理工学院”“Python”
- [SimpleX Chat](https://github.com/simplex-chat/simplex-chat) - 最私密、最安全的聊天和应用程序平台 - 现在具有双棘轮端到端加密。 `AGPL-3.0` `哈斯克尔`
- [Spectrum 2](https://spectrum.im/) - Spectrum 2 是一种开源即时消息传输。  即使用户使用不同的 IM 网络，它也允许他们一起聊天。 ([源代码](https://github.com/SpectrumIM/spectrum2)) `GPL-3.0` `C++`
- [Stoat](https://stoat.chat/) - Stoat 是一个采用现代网络技术构建的用户至上的聊天平台。 ([源代码](https://github.com/stoatchat/self-hosted)) `AGPL-3.0/MIT` `Rust`
- [Synapse](https://element-hq.github.io/synapse/latest/index.html) - [Matrix](https://matrix.org/) 服务器，一种用于去中心化持久通信的开放标准。 ([源代码](https://github.com/element-hq/synapse)) `Apache-2.0` `Python/deb`
- [Tiledesk](https://tiledesk.com) - 从潜在客户开发到售后，从 WhatsApp 到您的网站的一体化客户互动平台。拥有全渠道实时代理和人工智能驱动的聊天机器人（Intercom、Zendesk、Tawk.to 和 Tidio 的替代品）。 ([源代码](https://github.com/Tiledesk/tiledesk)) `MIT` `Docker/K8S`
- [Tinode](https://github.com/tinode) - 即时通讯平台。 Go 中的后端。客户端：Swift iOS、Java Android、JS webapp、可编写脚本的命令行；聊天机器人。 ([演示](https://sandbox.tinode.co/), [源代码](https://github.com/tinode/chat), [客户端](https://github.com/tinode/webapp)) `GPL-3.0` `Go`
- [Tox](https://tox.chat/) - 具有音频和视频聊天功能的分布式安全信使。 ([源代码](https://github.com/TokTok/c-toxcore)) `GPL-3.0` `C`
- [Tuwunel](https://tuwunel.chat) - Matrix 的高性能且功能丰富的聊天服务器，以及 conduwuit（Conduit 的分支）的后继者。 ([演示](https://try.tuwunel.chat/), [源代码](https://github.com/matrix-construct/tuwunel)) `Apache-2.0` `deb/Docker/Nix/Rust`
- [Typebot](https://typebot.io) - 对话式应用程序构建器（Typeform 和 Landbot 的替代品）。 ([源代码](https://github.com/baptisteArno/typebot.io)) `AGPL-3.0` `Docker`
- [WBO](https://github.com/lovasoa/whitebophir) - Web 白板可针对架构、绘图和注释进行实时协作。 ([演示](https://wbo.ophir.dev/)) `AGPL-3.0` `Nodejs/Docker`
- [Zulip](https://zulip.org) - Zulip 是一款功能强大的开源群聊应用程序。 ([源代码](https://github.com/zulip/zulip)) `Apache-2.0` `Python`


### 通讯 - 电子邮件 - 完整解决方案

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

简单部署[电子邮件](https://en.wikipedia.org/wiki/Email)服务器，例如对于缺乏经验或不耐烦的管理员。

- [AnonAddy](https://anonaddy.com) - 用于创建别名的电子邮件转发服务。 ([源代码](https://github.com/anonaddy/anonaddy)) `MIT` `PHP/Docker`
- [b1gMail](https://www.b1gmail.eu) - 使用 PHP 和 MariaDB 在任何网络空间上运行的完整电子邮件解决方案。它支持 POP3 包罗万象的邮箱，如果您运行自己的服务器，还可以与 Postfix 或 b1gMailServer 集成。 ([源代码](https://codeberg.org/b1gMail/b1gMail), [客户端](https://www.b1gmail.eu/en/start/addon-b1gmailserver/)) `GPL-2.0` `PHP`
- [DebOps](https://docs.debops.org/) - 您的基于 Debian 的盒装数据中心。一组通用 Ansible 角色，可用于管理 Debian 或 Ubuntu 主机。 ([源代码](https://github.com/debops/debops)) `GPL-3.0` `Ansible/Python`
- [docker-mailserver](https://docker-mailserver.github.io/docker-mailserver/edge/) - 生产就绪的全栈但在容器内运行的简单邮件服务器（SMTP、IMAP、LDAP、反垃圾邮件、防病毒等）。只有配置文件，没有SQL数据库。 ([源代码](https://github.com/docker-mailserver/docker-mailserver)) `MIT` `Docker`
- [Dovel](https://dovel.email) - SMTP 服务器根据简单的配置文件发送和接收电子邮件，并具有可用于浏览电子邮件的可选 Web 界面。 ([源代码](https://dovel.email/server/tree.html)) `LGPL-3.0` `Go`
- [Inboxen](https://inboxen.org) - 让您拥有无限数量的独特收件箱。 ([源代码](https://codeberg.org/Inboxen/Inboxen)) `GPL-3.0` `Python`
- [iRedMail](https://www.iredmail.org/) - 基于 Postfix 和 Dovecot 的全功能邮件服务器解决方案。 ([源代码](https://github.com/iredmail/iRedMail)) `GPL-3.0` `Shell`
- [Maddy Mail Server](https://maddy.email/) - 实现 SMTP（MTA 和 MX）和 IMAP 的一体化邮件服务器。用单个守护程序替换 Postfix、Dovecot、OpenDKIM、OpenSPF、OpenDMARC。 ([源代码](https://github.com/foxcpp/maddy)) `GPL-3.0` `Go`
- [Mail-in-a-Box](https://mailinabox.email/) - 只需一个命令即可将任何 Ubuntu 服务器变成功能齐全的邮件服务器。 ([源代码](https://github.com/mail-in-a-box/mailinabox)) `CC0-1.0` `Shell`
- [Mailcow](https://mailcow.email/) - 基于 Dovecot、Postfix 和其他开源软件的邮件服务器套件，提供现代化的 Web UI 管理。 ([源代码](https://github.com/mailcow/mailcow-dockerized)) `GPL-3.0` `Docker/PHP`
- [Mailu](https://mailu.io/) - 简单但功能齐全的邮件服务器作为一组 Docker 镜像。 ([源代码](https://github.com/Mailu/Mailu)) `MIT` `Docker/Python`
- [Modoboa](https://modoboa.org/en/) - 邮件托管和管理平台，包括现代且简化的 Web 用户界面。 ([源代码](https://github.com/modoboa/modoboa)) `ISC` `Python`
- [Mox](https://www.xmox.nl/) - 完整的电子邮件解决方案，包括 IMAP4、SMTP、SPF、DKIM、DMARC、MTA-STS、DANE 和 DNSSEC、基于信誉和基于内容的垃圾过滤、国际化 (IDNA)、使用 ACME 和 Let's Encrypt 的自动 TLS、帐户自动配置和 Web 邮件。 ([源代码](https://github.com/mjl-/mox)) `MIT` `Go`
- [Postal](https://docs.postalserver.io/) - 完整且功能齐全的邮件服务器，供网站和网络服务器使用。 ([源代码](https://github.com/postalserver/postal)) `MIT` `Docker/Ruby`
- [Simple NixOS Mailserver](https://gitlab.com/simple-nixos-mailserver/nixos-mailserver) - 利用 Nix 生态系统的完整邮件服务器解决方案。 `GPL-3.0` `尼克斯`
- [SimpleLogin](https://simplelogin.io) - 开源电子邮件别名解决方案可保护您的电子邮件地址。附带浏览器扩展和移动应用程序。 ([源代码](https://github.com/simple-login/app)) `MIT` `Docker/Python`
- [Stalwart Mail Server](https://stalw.art) - 一体化邮件服务器，支持 JMAP、IMAP4 和 SMTP，并具有多种现代功能。 ([源代码](https://github.com/stalwartlabs/stalwart)) `AGPL-3.0` `Rust/Docker`
- [wildduck](https://wildduck.email/) - 可扩展的无 SPOF IMAP/POP3 邮件服务器。 ([源代码](https://github.com/zone-eu/wildduck)) `EUPL-1.2` `Nodejs/Docker`


### 通讯 - 电子邮件 - 邮件递送代理

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

[邮件传送代理](https://en.wikipedia.org/wiki/Message_delivery_agent) (MDA) - [IMAP](https://en.wikipedia.org/wiki/Internet_Message_Access_Protocol)/[POP3](https://en.wikipedia.org/wiki/Post_Office_Protocol) 服务器软件。

- [Cyrus IMAP](https://www.cyrusimap.org/) - 电子邮件 (IMAP/POP3)、联系人和日历服务器。 ([源代码](https://github.com/cyrusimap/cyrus-imapd)) `BSD-3-Clause-Attribution` `C`
- [DavMail](https://davmail.sourceforge.net/) `⚠` - POP/IMAP/SMTP/Caldav/Carddav/LDAP 交换网关允许用户通过 Exchange 服务器使用任何邮件/日历客户端，甚至可以通过 Outlook Web Access 从 Internet 或防火墙后面使用。 ([源代码](https://github.com/mguessan/davmail)) `GPL-2.0` `Java`
- [Dovecot](https://www.dovecot.org/) - IMAP 和 POP3 服务器的编写主要考虑到安全性。 ([源代码](https://github.com/dovecot/core)) `MIT/LGPL-2.1` `C/deb`


### 通讯 - 电子邮件 - 邮件传输代理

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

[邮件传输代理](https://en.wikipedia.org/wiki/Message_transfer_agent) (MTA) - [SMTP](https://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol) 服务器。

- [chasquid](https://blitiri.com.ar/p/chasquid/) - SMTP（电子邮件）服务器注重简单性、安全性和易于操作。 ([源代码](https://blitiri.com.ar/git/r/chasquid/)) `Apache-2.0` `Go`
- [Courier MTA](https://www.courier-mta.org/) - 快速、可扩展的企业邮件/群件服务器，提供 ESMTP、IMAP、POP3、Web 邮件、邮件列表、基本的基于 Web 的日历和日程安排服务。 ([源代码](https://www.courier-mta.org/repo.html)) `GPL-3.0` `C/deb`
- [DragonFly](https://github.com/corecode/dma) - 适合家庭和办公室使用的小型 MTA。适用于 Linux 和 FreeBSD。 `BSD-3-子句` `C`
- [EmailRelay](https://emailrelay.sourceforge.net/) - 适用于 Windows 和 Linux 的小型且易于配置的 SMTP 和 POP3 服务器。 ([源代码](https://sourceforge.net/p/emailrelay/code/HEAD/tree/)) `GPL-3.0` `C++`
- [Exim](https://www.exim.org/) - 消息传输代理（MTA）由剑桥大学开发。 ([源代码](https://git.exim.org/exim.git)) `GPL-3.0` `C/deb`
- [Haraka](https://haraka.github.io/) - 快速、高度可扩展且事件驱动的 SMTP 服务器。 ([源代码](https://github.com/haraka/Haraka)) `MIT` `Nodejs`
- [OpenSMTPD](https://opensmtpd.org/) - OpenBSD 项目的安全 SMTP 服务器实现。 ([源代码](https://github.com/OpenSMTPD/OpenSMTPD/)) `ISC` `C/deb`
- [OpenTrashmail](https://github.com/HaschekSolutions/opentrashmail) - 完整的垃圾邮件解决方案，公开 SMTP 服务器并具有 Web 界面来管理收到的电子邮件。适用于多个域和通配符域，并且完全基于文件（不需要数据库）。包括 RSS 源和 JSON API。 `Apache-2.0` `Python/PHP/Docker`
- [Postfix](http://www.postfix.org/) - 快速、易于管理且安全的 Sendmail 替换。 `IPL-1.0` `C/deb`
- [Sendmail](https://www.proofpoint.com/us/products/email-protection/open-source-email-solution) - 消息传输代理 (MTA)。 `Sendmail` `C/deb`


### 通讯 - 电子邮件 - 邮件列表和时事通讯

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

[邮件列表](https://en.wikipedia.org/wiki/Mailing_list) 服务器和群发邮件软件 - 一封邮件发送给多个收件人。

- [HyperKitty](https://wiki.list.org/HyperKitty) - 访问 GNU Mailman v3 档案。 ([演示](https://lists.mailman3.org/), [源代码](https://gitlab.com/mailman/hyperkitty)) `GPL-3.0` `Python`
- [Keila](https://www.keila.io) - 可靠且易于使用的新闻通讯工具（Mailchimp 和 Sendinblue 的替代品）。 ([演示](https://app.keila.io), [源代码](https://github.com/pentacent/keila)) `AGPL-3.0` `Docker`
- [Listmonk](https://listmonk.app/) - 具有现代化仪表板的高性能、自托管新闻通讯和邮件列表管理器。 ([演示](https://demo.listmonk.app/), [源代码](https://github.com/knadh/listmonk)) `AGPL-3.0` `Go/Docker`
- [Mailman](https://www.list.org/) - 管理电子邮件讨论和电子通讯列表。 ([源代码](https://gitlab.com/mailman/)) `GPL-3.0` `Python`
- [Mautic](https://www.mautic.org/) - 营销自动化软件（电子邮件、社交等）。 ([源代码](https://github.com/mautic/mautic)) `GPL-3.0` `PHP`
- [mlmmj](https://mlmmj.org/) - 邮件列表管理变得快乐。 ([源代码](https://codeberg.org/mlmmj/mlmmj)) `MIT` `C`
- [phpList](https://www.phplist.org) - 时事通讯和电子邮件营销，具有对订阅者、退回邮件和插件的高级管理。 ([源代码](https://github.com/phpList/phplist3)) `AGPL-3.0` `PHP`
- [Postorius](https://docs.mailman3.org/projects/postorius/en/latest/) - 用于访问 GNU Mailman 的 Web 用户界面。 ([源代码](https://gitlab.com/mailman/postorius/)) `GPL-3.0` `Python`
- [Schleuder](https://schleuder.nadir.org/) - 支持 GPG 的邮件列表管理器，具有重新发送功能。 ([源代码](https://0xacab.org/schleuder/schleuder/tree/master)) `GPL-3.0` `Ruby`
- [Sympa](https://www.sympa.community/) - 邮件列表管理器。 ([源代码](https://github.com/sympa-community/sympa)) `GPL-2.0` `Perl`


### 通讯 - 电子邮件 - 网络邮件客户端

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

[Webmail](https://en.wikipedia.org/wiki/Webmail) 客户端。

- [Cypht](https://cypht.org) - 您的电子邮件帐户的供稿阅读器。 ([源代码](https://github.com/cypht-org/cypht)) `LGPL-2.1` `PHP`
- [Roundcube](https://roundcube.net) - 基于浏览器的 IMAP 客户端，具有类似应用程序的用户界面。 ([源代码](https://github.com/roundcube/roundcubemail)) `GPL-3.0` `PHP/deb`
- [SnappyMail](https://snappymail.eu/) - 简单、现代、轻量且快速的基于网络的电子邮件客户端（RainLoop 的分支）。 ([演示](https://snappymail.eu/demo/), [源代码](https://github.com/the-djmaze/snappymail), [客户端](https://snappymail.eu/repository/v2/plugins/)) `AGPL-3.0` `PHP`
- [SquirrelMail](https://squirrelmail.org) - 另一个基于浏览器的 IMAP 客户端。 ([源代码](https://sourceforge.net/p/squirrelmail/code/HEAD/tree/)) `GPL-2.0` `PHP`


### 通讯-IRC

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

[IRC](https://en.wikipedia.org/wiki/Internet_Relay_Chat) 通讯软件。

- [Ergo](https://ergo.chat/) - 用 Go 编写的现代 IRCv3 服务器，结合了 ircd、服务框架和保镖的功能。 ([源代码](https://github.com/ergochat/ergo)) `MIT` `Go/Docker`
- [Glowing Bear](https://github.com/glowing-bear/glowing-bear) - 微信的网络前端。 ([演示](https://www.glowing-bear.org)) `GPL-3.0` `Nodejs`
- [InspIRCd](https://www.inspircd.org/) - 用 C++ 编写的适用于 Linux、BSD、Windows 和 macOS 的模块化 IRC 服务器。 ([源代码](https://github.com/inspircd/inspircd)) `GPL-2.0` `C++/Docker`
- [Kiwi IRC](https://kiwiirc.com/) - 具有主题支持的响应式 Web IRC 客户端。 ([演示](https://kiwiirc.com/nextclient/), [源代码](https://github.com/kiwiirc/kiwiirc)) `Apache-2.0` `Nodejs`
- [ngircd](https://ngircd.barton.de/) - 适用于小型或专用网络的便携式轻量级互联网中继聊天服务器。 ([源代码](https://github.com/ngircd/ngircd)) `GPL-2.0` `C/deb`
- [Quassel IRC](https://quassel-irc.org/) - 分布式 IRC 客户端，这意味着一个（或多个）客户端可以附加到中央核心或从中央核心分离。 ([源代码](https://github.com/quassel/quassel)) `GPL-2.0` `C++`
- [Robust IRC](https://robustirc.net/) - 无网络分割的 IRC。分布式IRC服务器，基于RobustSession协议。 ([源代码](https://github.com/robustirc/robustirc)) `BSD-3-Clause` `Go`
- [The Lounge](https://thelounge.chat/) - 自托管 Web IRC 客户端。 ([演示](https://demo.thelounge.chat/), [源代码](https://github.com/thelounge/thelounge)) `MIT` `Nodejs/Docker`
- [UnrealIRCd](https://www.unrealircd.org/) - 用 C 语言编写的模块化、高级且高度可配置的 IRC 服务器，适用于 Linux、BSD、Windows 和 macOS。 ([源代码](https://github.com/unrealircd/unrealircd)) `GPL-2.0` `C`
- [Weechat](https://weechat.org/) - 快速、轻便且可扩展的聊天客户端。 ([源代码](https://github.com/weechat/weechat)) `GPL-3.0` `C/Docker/deb`
- [ZNC](https://wiki.znc.in/ZNC) - 高级 IRC 保镖。 ([源代码](https://github.com/znc/znc)) `Apache-2.0` `C++/deb`


### 通讯-SIP

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

[SIP](https://en.wikipedia.org/wiki/Session_Initiation_Protocol)/[IPBX](https://en.wikipedia.org/wiki/IP_PBX)电话软件。

- [Asterisk](https://www.asterisk.org/) - 易于使用且先进的 IP PBX 系统、VoIP 网关和会议服务器。 ([源代码](https://github.com/asterisk/asterisk)) `GPL-2.0` `C/deb`
- [Flexisip](https://www.linphone.org/en/flexisip-sip-server/) - 完整、模块化和可扩展的 SIP 服务器，包括推送网关，可在移动设备平台上传送 SIP 来电或短信，当应用程序在前台未处于活动状态时，需要推送通知才能接收信息。 ([源代码](https://github.com/BelledonneCommunications/flexisip)) `AGPL-3.0` `C/Docker`
- [Freepbx](https://www.freepbx.org) - 基于 Web 的开源 GUI，用于控制和管理 Asterisk。 ([源代码](https://git.freepbx.org/projects/FREEPBX)) `GPL-2.0` `PHP`
- [FreeSWITCH](https://freeswitch.org/) - 可扩展的开源跨平台电话平台。 ([源代码](https://github.com/signalwire/freeswitch)) `MPL-2.0` `C`
- [FusionPBX](https://www.fusionpbx.com/) - 用于多平台语音切换的 Web 界面称为 FreeSWITCH。 ([源代码](https://github.com/fusionpbx/fusionpbx)) `MPL-1.1` `PHP`
- [Kamailio](https://www.kamailio.org/w/) - 模块化 SIP 服务器（注册器/代理/路由器/等）。 ([源代码](https://github.com/kamailio/kamailio)) `GPL-2.0` `C/deb`
- [openSIPS](https://opensips.org/) - 用于语音、视频、IM、状态和任何其他 SIP 扩展的 SIP 代理/服务器。 ([源代码](https://github.com/OpenSIPS/opensips)) `GPL-2.0` `C`
- [Routr](https://routr.io) - 轻量级 SIP 代理、位置服务器和注册器，用于可靠且可扩展的 SIP 基础设施。 ([源代码](https://github.com/fonoster/router)) `MIT` `Docker/K8S`
- [SIP3](https://sip3.io/) - VoIP 故障排除和监控平台。 ([演示](https://demo.sip3.io), [源代码](https://github.com/sip3io/)) `Apache-2.0` `Java`
- [SIPCAPTURE Homer](https://www.sipcapture.org/) - VoIP 呼叫故障排除和监控。 ([源代码](https://github.com/sipcapture/homer)) `AGPL-3.0` `Nodejs/Go/Docker`
- [Wazo](https://wazo-platform.org/) - 功能齐全的 IPBX 解决方案构建在 Asterisk 之上，具有集成的 Web 管理界面和 REST-ful API。 ([源代码](https://github.com/wazo-platform)) `GPL-3.0` `Python`
- [Yeti-Switch](https://yeti-switch.org/) - 具有集成计费和路由引擎以及 REST API 的 Transit class4 软交换机 (SBC)。 ([演示](https://demo.yeti-switch.org/), [源代码](https://github.com/yeti-switch)) `GPL-2.0` `C++/Ruby`


### 沟通 - 社交网络和论坛

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

[社交网络](https://en.wikipedia.org/wiki/Social_networking_service) 和[论坛](https://en.wikipedia.org/wiki/Internet_forum) 软件。

- [Akkoma](https://akkoma.social/) - 具有 Mastodon、GNU 社交和 ActivityPub 兼容性的联合微博服务器。 ([源代码](https://akkoma.dev/AkkomaGang/akkoma)) `AGPL-3.0` `Elixir/Docker`
- [Answer](https://answer.apache.org) - 基于知识的社区软件。您可以使用它快速构建您的问答社区，以进行产品技术支持、客户支持、用户交流等。 ([源代码](https://github.com/apache/answer)) `Apache-2.0` `Docker/Go`
- [Artalk](https://artalk.js.org/) - 用 Golang 构建的评论系统，提供了一个轻量级且高度可定制的解决方案，用于向您的网站添加评论。 ([源代码](https://github.com/ArtalkJS/Artalk)) `MIT` `Go/Docker`
- [AsmBB](https://board.asm32.info) - 用 ASM 编写的快速、由 SQLite 支持的论坛引擎。 ([源代码](https://asm32.info/fossil/asmbb/index)) `EUPL-1.2` `汇编`
- [BuddyPress](https://buddypress.org/about/) - 强大的插件，使您的 WordPress.org 支持的网站超越博客，具有用户配置文件、活动流、用户组等社交网络功能。 ([源代码](https://github.com/buddypress/BuddyPress)) `GPL-2.0` `PHP`
- [Chirpy](https://chirpy.dev) - 隐私友好且可定制的 Disqus（评论系统）替代品。 ([演示](https://chirpy.dev/play), [源代码](https://github.com/devrsi0n/chirpy)) `AGPL-3.0` `Docker/Nodejs`
- [Coral](https://coralproject.net/) - Vox Media 提供更好的评论体验。 ([源代码](https://github.com/coralproject/talk)) `Apache-2.0` `Docker/Nodejs`
- [diaspora*](https://diasporafoundation.org/) - 分布式社交网络服务器。 ([源代码](https://github.com/diaspora/diaspora)) `AGPL-3.0` `Ruby`
- [Discourse](https://www.discourse.org/) - 基于Ruby和JS的高级论坛/社区解决方案。 ([演示](https://try.discourse.org/), [源代码](https://github.com/discourse/discourse)) `GPL-2.0` `Docker`
- [Elgg](https://elgg.org/) - 强大的开源社交网络引擎。 ([源代码](https://github.com/Elgg/Elgg)) `GPL-2.0` `PHP`
- [Enigma 1/2 BBS](https://nuskooler.github.io/enigma-bbs/) - Enigma 1/2 是一款现代化的多平台 BBS 引擎，具有无限的“呼叫者”和传统 DOS 门游戏支持。 ([源代码](https://github.com/NuSkooler/enigma-bbs)) `BSD-2-Clause` `Shell/Docker/Nodejs`
- [Flarum](https://flarum.org) - 令人愉快的简单论坛。 Flarum 是下一代论坛软件，让在线讨论再次变得有趣。 ([源代码](https://github.com/flarum/flarum)) `MIT` `PHP`
- [Friendica](https://friendi.ca/) - 社交通信服务器。 ([源代码](https://github.com/friendica/friendica)) `AGPL-3.0` `PHP`
- [GoToSocial](https://docs.gotosocial.org/en/latest/) - ActivityPub 联合社交网络服务器实现 Mastodon 客户端 API。 ([源代码](https://codeberg.org/superseriousbusiness/gotosocial)) `AGPL-3.0` `Docker/Go`
- [Hatsu](https://hatsu.cli.rs/) - 代表您的静态站点与 Fediverse 交互的桥接器。 ([源代码](https://github.com/importantimport/hatsu)) `AGPL-3.0` `Docker/Rust`
- [Hubzilla](https://hubzilla.org) - 去中心化的身份、隐私、发布、共享、云存储和通信/社交平台。 ([源代码](https://framagit.org/hubzilla/core)) `MIT` `PHP`
- [HumHub](https://www.humhub.org/) - 适用于私人社交网络的灵活套件。 ([源代码](https://github.com/humhub/humhub)) `AGPL-3.0` `PHP`
- [Iceshrimp.NET](https://iceshrimp.net) - 通过 ActivityPub 进行通信的联合微博服务器。 ([源代码](https://iceshrimp.dev/iceshrimp/iceshrimp.net)) `EUPL-1.2` `.NET/C#/Docker`
- [Isso](https://isso-comments.de/) - 用 Python 和 Javascript 编写的轻量级评论服务器。它的目标是成为 Disqus 的直接替代品。 ([源代码](https://github.com/isso-comments/isso)) `MIT` `Python/Docker`
- [Lemmy](https://join-lemmy.org/) - fediverse 的链接聚合器（Reddit 的替代品）。 ([源代码](https://github.com/LemmyNet/lemmy)) `AGPL-3.0` `Docker/Rust`
- [Loomio](https://www.loomio.org/) - 协作决策工具，使任何人都可以轻松参与影响他们的决策。 ([源代码](https://github.com/loomio/loomio)) `AGPL-3.0` `Docker`
- [Mastodon](https://joinmastodon.org/) - 联合微博服务器。 ([源代码](https://github.com/mastodon/mastodon), [客户端](https://github.com/hyperupcall/awesome-mastodon)) `AGPL-3.0` `Ruby`
- [Misago](https://misago-project.org/) - 功能齐全的现代论坛应用程序，快速、可扩展且响应迅速。 ([源代码](https://github.com/rafalp/Misago)) `GPL-2.0` `Docker`
- [Misskey](https://misskey.io/) - Fediverse 的去中心化应用程序式微博服务器/SNS，使用 ActivityPub 协议，如 GNU 社交和 Mastodon。 ([源代码](https://github.com/misskey-dev/misskey)) `AGPL-3.0` `Nodejs/Docker`
- [Movim](https://movim.eu/) - 基于 XMPP 的现代联合社交网络，具有功能齐全的群聊、订阅和微博。 ([源代码](https://github.com/movim/movim)) `AGPL-3.0` `PHP/Docker`
- [MyBB](https://mybb.com/) - 免费的、可扩展的论坛软件包。 ([源代码](https://github.com/mybb/mybb)) `LGPL-3.0` `PHP`
- [NodeBB](https://nodebb.org/) - 为现代网络构建的论坛软件。 ([演示](https://try.nodebb.org/), [源代码](https://github.com/NodeBB/NodeBB)) `GPL-3.0` `Nodejs/Docker`
- [OSSN](https://www.opensource-socialnetwork.org/) - 社交网络软件允许您创建社交网站并帮助您的会员与具有相似专业或个人兴趣的人建立社交关系。 ([源代码](https://github.com/opensource-socialnetwork/opensource-socialnetwork)) `CAL-1.0` `PHP`
- [phpBB](https://www.phpbb.com/) - 扁平论坛公告板软件解决方案，可用于与一群人保持联系或为您的整个网站提供支持。 ([源代码](https://github.com/phpbb/phpbb)) `GPL-2.0` `PHP`
- [PieFed](https://join.piefed.social) - fediverse 的链接聚合器/reddit 克隆（Reddit 的替代品）。 ([演示](https://piefed.social), [源代码](https://codeberg.org/rimu/pyfedi)) `AGPL-3.0` `Python/Docker`
- [PixelFed](https://pixelfed.social) - 道德照片共享平台，由 ActivityPub 联盟（Instagram 的替代品）提供支持。 ([源代码](https://github.com/pixelfed/pixelfed)) `AGPL-3.0` `PHP`
- [Pleroma](https://pleroma.social) - 联合微博服务器、Mastodon、GNU 社交和 ActivityPub 兼容。 ([源代码](https://git.pleroma.social/pleroma/pleroma)) `AGPL-3.0` `Elixir`
- [qpixel](https://codidact.com/) - 基于问答的社区知识共享软件。 ([源代码](https://github.com/codidact/qpixel)) `AGPL-3.0` `Ruby`
- [Redlib](https://github.com/redlib-org/redlib) `⚠` - Reddit 的替代私有前端，起源于 Libreddit。 `AGPL-3.0` `铁锈`
- [remark42](https://remark42.com/) - 轻量级、简单的评论引擎，不会监视用户。它可以嵌入到博客、文章或任何其他读者添加评论的地方。 ([演示](https://remark42.com/demo/), [源代码](https://github.com/umputun/remark42)) `MIT` `Docker/Go`
- [Scoold](https://scoold.com) - JAR 中的堆栈溢出。企业级问答平台，具有全文搜索、SAML、LDAP 集成和社交登录支持。 ([演示](https://live.scoold.com), [源代码](https://github.com/Erudika/scoold)) `Apache-2.0` `Java/Docker/K8S`
- [Simple Machines Forum](https://www.simplemachines.org/) - 免费的专业级软件包可让您在几分钟内建立自己的在线社区。 ([源代码](https://github.com/SimpleMachines/SMF)) `BSD-3-Clause` `PHP`
- [Socialhome](https://socialhome.network) - 联合和分散的配置文件构建器和社交网络引擎。 ([演示](https://socialhome.network/), [源代码](https://github.com/jaywink/socialhome)) `AGPL-3.0` `Docker/Python`
- [Talkyard](https://www.talkyard.io/) - 创建一个社区，您的用户可以在其中提出想法并获得问题解答。并进行友好的开放式讨论和聊天（Slack/StackOverflow/Discourse/Reddit/Disqus 混合）。 ([演示](https://www.talkyard.io/forum/latest), [源代码](https://github.com/debiki/talkyard)) `AGPL-3.0` `Docker/Scala`
- [yarn.social](https://yarn.social) - 自托管、类似 Twitter™ 的去中心化微日志平台。没有广告，没有跟踪，您的内容，您的数据。 ([源代码](https://git.mills.io/yarnsocial/yarn)) `MIT` `Go`


### 通讯 - 视频会议

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

[视频/网络会议](https://en.wikipedia.org/wiki/Web_conferencing)工具和软件。

_相关：[会议管理](#conference-management)_

- [BigBlueButton](https://bigbluebutton.org/) - 支持音频、视频、幻灯片（带白板控件）、聊天、屏幕的实时共享。教师可以通过投票、表情符号和分组讨论室与远程学生互动。 ([源代码](https://github.com/bigbluebutton/bigbluebutton)) `LGPL-3.0` `Java`
- [Galene](https://galene.org/) - 易于部署、对服务器资源要求适中的视频会议服务器。 ([源代码](https://github.com/jech/galene)) `MIT` `Go`
- [Janus](https://janus.conf.meetecho.com/) - 通用、轻量级、简约的 WebRTC 服务器。 ([演示](https://janus.conf.meetecho.com/demos/), [源代码](https://github.com/meetecho/janus-gateway)) `GPL-3.0` `C`
- [Jitsi Meet](https://jitsi.org/Projects/JitsiMeet) - WebRTC 应用程序使用 Jitsi Videobridge 提供高质量、可扩展的视频会议。 ([演示](https://meet.jit.si), [源代码](https://github.com/jitsi/jitsi-meet)) `Apache-2.0` `Nodejs/Docker/deb`
- [Jitsi Video Bridge](https://jitsi.org/Projects/JitsiVideobridge) - WebRTC 兼容选择性转发单元 (SFU)，允许多用户视频通信。 ([源代码](https://github.com/jitsi/jitsi-videobridge)) `Apache-2.0` `Java/deb`
- [MiroTalk C2C](https://c2c.mirotalk.com) - 实时 cam-2-cam 视频通话和屏幕共享，端到端加密，可通过简单的 iframe 嵌入任何网站。 ([源代码](https://github.com/miroslavpejic85/mirotalkc2c)) `AGPL-3.0` `Nodejs/Docker`
- [MiroTalk P2P](https://p2p.mirotalk.com) - 简单、安全、快速的实时视频会议，高达 4k 和 60fps，兼容所有浏览器和平台。 ([演示](https://p2p.mirotalk.com/newcall), [源代码](https://github.com/miroslavpejic85/mirotalk)) `AGPL-3.0` `Nodejs/Docker`
- [MiroTalk SFU](https://sfu.mirotalk.com) - 简单、安全、可扩展的实时视频会议，最高可达 4k，兼容所有浏览器和平台。 ([演示](https://sfu.mirotalk.com/newroom), [源代码](https://github.com/miroslavpejic85/mirotalksfu)) `AGPL-3.0` `Nodejs/Docker`
- [plugNmeet](https://www.plugnmeet.org/) - 可扩展的高性能网络会议系统。 ([演示](https://demo.plugnmeet.com/login.html), [源代码](https://github.com/mynaparrot/plugNmeet-server)) `MIT` `Docker/Go`


### 通信 - XMPP - 服务器

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

[可扩展消息传递和状态协议](https://en.wikipedia.org/wiki/XMPP) 服务器。

- [ejabberd](https://www.ejabberd.im/) - XMPP 即时消息服务器。 ([源代码](https://github.com/processone/ejabberd)) `GPL-2.0` `Erlang/Docker`
- [MongooseIM](https://www.erlang-solutions.com/products/mongooseim.html) - 注重性能和可扩展性的移动消息传递平台。 ([源代码](https://github.com/esl/MongooseIM)) `GPL-2.0` `Erlang/Docker/K8S`
- [Openfire](https://www.igniterealtime.org/projects/openfire/) - 实时协作 (RTC) 服务器。 ([源代码](https://github.com/igniterealtime/Openfire)) `Apache-2.0` `Java`
- [Prosody IM](https://prosody.im/) - 功能丰富且易于配置的 XMPP 服务器。 ([源代码](https://hg.prosody.im/)) `MIT` `Lua`
- [Snikket](https://snikket.org/) - 一体化 Dockerized 简单 XMPP 解决方案，包括 Web 管理和客户端。 ([源代码](https://github.com/snikket-im/snikket-server), [客户端](https://snikket.org/app/)) `Apache-2.0` `Docker`
- [Tigase](https://tigase.net/xmpp-server) - Java 中的 XMPP 服务器实现。 ([源代码](https://github.com/tigase/tigase-server)) `GPL-3.0` `Java`


### 通信 - XMPP - Web 客户端

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

[可扩展消息传递和状态协议](https://en.wikipedia.org/wiki/XMPP) Web 客户端/接口。

- [Converse.js](https://conversejs.org/) - 浏览器中的 XMPP 聊天客户端。 ([源代码](https://github.com/conversejs/converse.js)) `MPL-2.0` `Javascript`
- [Libervia](https://repos.goffi.org/libervia-web) - 来自 Salut à Toi 的 Web 前端。 `AGPL-3.0` `Python`
- [Salut à Toi](https://www.salut-a-toi.org/) - 多用途、多前端、自由且去中心化的通信工具。 ([源代码](https://repos.goffi.org/libervia-backend)) `AGPL-3.0` `Python`


### 社区支持农业 (CSA)

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

社区支持的农业和粮食合作社的管理和行政工具。

_相关：[电子商务](#电子商务)_

- [ACP Admin](https://acp-admin.ch/) - CSA 管理。管理会员、订阅、交付、投递地点、会员参与、发票和电子邮件（法语文档）。 ([源代码](https://github.com/csa-admin-org/csa-admin)) `MIT` `Ruby`
- [E-Label](https://filipecarneiro.github.io/ELabel/) - 在欧盟境内销售的酒瓶上带有二维码的电子标签解决方案。 ([源代码](https://github.com/filipecarneiro/ELabel)) `MIT` `Docker`
- [FoodCoopShop](https://www.foodcoopshop.com/) - 用户友好的食品合作社软件。 ([源代码](https://github.com/foodcoopshop/foodcoopshop)) `AGPL-3.0` `PHP/Docker`
- [Foodsoft](https://foodcoops.net/) - 管理非营利性食品合作社（产品目录、订购、会计、工作安排）。 ([源代码](https://github.com/foodcoops/foodsoft)) `AGPL-3.0` `Docker/Ruby`
- [Hive-Pal](https://hivepal.app) - 移动优先的养蜂管理应用程序，用于跟踪蜂箱、检查、蜂王记录和设备，并提供针对现场使用优化的简化数据输入。 ([演示](https://hivepal.app), [源代码](https://github.com/martinhrvn/hive-pal)) `MIT` `Nodejs/Docker`
- [juntagrico](https://juntagrico.org/) - 社区菜园、蔬菜合作社管理平台。 ([源代码](https://github.com/juntagrico/juntagrico)) `LGPL-3.0` `Python`
- [Open Food Network](https://www.openfoodnetwork.org/) - 当地食品的在线市场。它建立了一个独立的在线食品商店网络，将农民和食品中心与个人和当地企业联系起来。 ([源代码](https://github.com/openfoodfoundation/openfoodnetwork)) `AGPL-3.0` `Ruby`
- [OpenOlitor](https://openolitor.org/) - 社区支持农业团体的管理平台。 ([源代码](https://github.com/OpenOlitor/openolitor-server)) `AGPL-3.0` `Scala`
- [teikei](https://github.com/teikei/teikei) - 一个网络应用程序，根据众包数据规划社区支持的农业。 ([演示](https://ernte-teilen.org/karte/#/)) `AGPL-3.0` `Nodejs`


### 会议管理

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

用于提交[摘要](https://en.wikipedia.org/wiki/Abstract_management)和学术会议准备/管理的软件。

- [indico](https://getindico.io/) - 功能丰富的事件管理系统，@CERN，Web 的诞生地。 ([演示](https://sandbox.getindico.io/), [源代码](https://github.com/indico/indico)) `MIT` `Python`
- [motion.tools (Antragsgrün)](https://motion.tools/) - 管理（政治）公约的动议和修正案。 ([演示](https://sandbox.motion.tools/createsite), [源代码](https://github.com/CatoTH/antragsgruen)) `AGPL-3.0` `PHP/Docker`
- [OpenSlides](https://openslides.com/) - 演示和集会系统，用于管理和预测集会的议程、动议和选举。 ([演示](https://demo.openslides.org/login), [源代码](https://github.com/OpenSlides/OpenSlides)) `MIT` `Docker`
- [osem](https://osem.io/) - 专为免费软件会议量身定制的活动管理。 ([源代码](https://github.com/openSUSE/osem)) `MIT` `Ruby/Docker`
- [pretalx](https://pretalx.org) - 基于网络的活动管理，包括运行论文征集、审查提交的内容和安排演讲。各种相关工具的出口和进口。 ([源代码](https://github.com/pretalx/pretalx)) `Apache-2.0` `Python`


### 内容管理系统 (CMS)

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

[内容管理系统](https://en.wikipedia.org/wiki/Content_management_system) 提供了一种实用的方法来设置具有许多功能的网站，使用易于添加和自定义的第三方插件、主题和功能。

_相关：[博客平台](#blogging-platforms)、[静态站点生成器](#static-site-generators)、[照片画廊](#photo-galleries)_

- [Alfresco Community Edition](https://www.alfresco.com/products/community/download) - 开源企业内容管理软件可处理任何类型的内容，使用户能够轻松共享和协作内容。 ([源代码](https://github.com/Alfresco/alfresco-community-repo)) `LGPL-3.0` `Java`
- [Apostrophe](https://apostrophecms.com/) - CMS 专注于可扩展的上下文编辑工具。 ([演示](https://apostropecms.com/demo), [源代码](https://github.com/apostropecms/apostrope)) `MIT` `Nodejs`
- [Automad](https://automad.org/) - 平面文件内容管理系统和模板引擎。 ([演示](https://try.automad.org/), [源代码](https://github.com/marcantondahmen/automad)) `MIT` `PHP/Docker`
- [Backdrop CMS](https://backdropcms.org/) - 适用于中小型企业和非营利组织的综合 CMS。 ([源代码](https://github.com/backdrop/backdrop)) `GPL-2.0` `PHP`
- [Bludit](https://www.bludit.com/) `⚠` - 在几秒钟内构建网站或博客。 Bludit 使用平面文件（JSON 格式的文本文件）来存储帖子和页面。 ([源代码](https://github.com/bludit/bludit)) `MIT` `PHP`
- [Bolt CMS](https://boltcms.io/) - 内容管理工具，力求尽可能简单明了。 ([源代码](https://github.com/bolt/core)) `MIT` `PHP`
- [CMS Made Simple](https://www.cmsmadesimple.org/) - 更快、更轻松地管理网站内容，可从小型企业扩展到大型公司。 ([源代码](http://svn.cmsmadesimple.org/svn/cmsmadesimple/trunk/)) `GPL-2.0` `PHP`
- [Cockpit](https://getcockpit.com) - 用于管理任何结构化内容的简单内容平台。 ([源代码](https://github.com/Cockpit-HQ/Cockpit)) `MIT` `PHP`
- [Concrete 5 CMS](https://www.concretecms.com) - 开源内容管理系统。 ([源代码](https://github.com/concretecms/concretecms)) `MIT` `PHP`
- [Contao](https://contao.org/) - 功能强大的 CMS，可让您创建专业网站和可扩展的 Web 应用程序。 ([演示](https://demo.contao.org/contao), [源代码](https://github.com/contao/contao/)) `LGPL-3.0` `PHP`
- [CouchCMS](https://www.couchcms.com/) - 设计师的 CMS。 ([源代码](https://github.com/CouchCMS/CouchCMS)) `CPAL-1.0` `PHP`
- [Drupal](https://www.drupal.org/) - 先进的开源内容管理平台。 ([源代码](https://git.drupalcode.org/project/drupal)) `GPL-2.0` `PHP`
- [eLabFTW](https://www.elabftw.net) - 研究实验室的在线实验室笔记本。存储实验、使用数据库查找试剂或方案、使用可信时间戳为实验合法添加时间戳、导出为 pdf 或 zip 存档、与合作者共享……。 ([演示](https://demo.elabftw.net), [源代码](https://github.com/elabftw/elabftw)) `AGPL-3.0` `PHP`
- [Expressa](https://github.com/thomas4019/expressa) - 使用 JSON 模式为数据库驱动的网站提供支持的内容管理系统。提供权限管理和自动REST API。 `麻省理工学院` Nodejs`
- [Joomla!](https://www.joomla.org/) - 先进的内容管理系统（CMS）。 ([源代码](https://github.com/joomla/joomla-cms)) `GPL-2.0` `PHP`
- [KeystoneJS](https://keystonejs.com/) - CMS 和 Web 应用程序平台。 ([源代码](https://github.com/keystonejs/keystone)) `MIT` `Nodejs`
- [Localess](https://localess.org/home) `⚠` - 强大的翻译管理和内容管理系统。管理您的网站或应用程序内容并将其翻译为多种语言，使用 AI 加快翻译速度。 ([源代码](https://github.com/Lessify/localess)) `MIT` `Docker`
- [MODX](https://modx.com/) - 先进的内容管理和发布平台。当前版本称为“革命”。 ([源代码](https://github.com/modxcms/revolution)) `GPL-2.0` `PHP`
- [Neos](https://www.neos.io) - Neos 或 TYPO3 Neos（版本 1）是一种现代的开源 CMS。 ([源代码](https://github.com/neos)) `GPL-3.0` `PHP`
- [Noosfero](https://gitlab.com/noosfero/noosfero) - 社会和团结经济网络平台，在同一系统中提供博客、电子档案、CMS、RSS、主题讨论、活动议程和团结经济集体智慧。 `AGPL-3.0` `红宝石`
- [Omeka](https://omeka.org) - 创建复杂的叙述并分享丰富的馆藏，遵守都柏林核心标准，在您的服务器上使用 Omeka，专为学者、博物馆、图书馆、档案馆和爱好者而设计。 ([演示](https://omeka.org/classic/showcase/), [源代码](https://github.com/omeka/Omeka)) `GPL-3.0` `PHP`
- [Payload CMS](https://payloadcms.com/) - 开发人员优先的无头 CMS 和应用程序框架。 ([源代码](https://github.com/payloadcms/payload)) `MIT` `Nodejs`
- [Pimcore](http://www.pimcore.com/) - 多渠道体验和参与管理平台。 ([源代码](https://github.com/pimcore/pimcore)) `GPL-3.0` `PHP/Docker`
- [Plone](https://plone.org/) - 强大的开源CMS系统。 ([源代码](https://github.com/plone)) `ZPL-2.0` `Python/Docker`
- [Publify](https://publify.github.io/) - 简单但功能齐全的网络发布软件。 ([源代码](https://github.com/publify/publify)) `MIT` `Ruby`
- [REDAXO](https://www.redaxo.org) - 简单、灵活且有用的内容管理系统（德语文档）。 ([源代码](https://github.com/redaxo/core)) `MIT` `PHP/Docker`
- [SilverStripe](https://www.silverstripe.org) - 易于使用的 CMS，具有强大的 MVC 框架底层。 ([演示](https://demo.silverstripe.org/), [源代码](https://github.com/silverstripe)) `BSD-3-Clause` `PHP`
- [SPIP](https://www.spip.net/fr) - 互联网出版系统旨在实现协作工作、多语言环境以及网络作者的简单使用。 ([源代码](https://git.spip.net/)) `GPL-3.0` `PHP`
- [Squidex](https://squidex.io) - Headless CMS，基于 MongoDB、CQRS 和事件源。 ([演示](https://cloud.squidex.io), [源代码](https://github.com/Squidex/squidex)) `MIT` `.NET`
- [Strapi](https://strapi.io/) - 最先进的开源内容管理框架 (headless-CMS)，可轻松构建强大的 API。 ([源代码](https://github.com/strapi/strapi)) `MIT` `Nodejs`
- [Superdesk](https://superdesk.org/) `⚠` - 端到端新闻创作、制作、管理、分发和发布平台。 ([源代码](https://github.com/superdesk/superdesk)) `AGPL-3.0` `Docker/Python/PHP`
- [Textpattern](https://textpattern.com/) - 灵活、优雅且易于使用的 CMS。 ([演示](https://textpattern.co/demo), [源代码](https://github.com/textpattern/textpattern)) `GPL-2.0` `PHP`
- [Typemill](https://typemill.net/) - 作者友好的平面文件 cms，带有基于 vue.js 的可视化 Markdown 编辑器。 ([源代码](https://github.com/typemill/typemill)) `MIT` `PHP`
- [TYPO3](https://typo3.org/) - 功能强大且先进的 CMS，拥有庞大的社区。 ([源代码](https://github.com/TYPO3/typo3)) `GPL-2.0` `PHP`
- [Umbraco](https://umbraco.com/) - 友好的 CMS。免费且开源，拥有令人惊叹的社区。 ([源代码](https://github.com/umbraco/Umbraco-CMS)) `MIT` `.NET`
- [Vvveb CMS](https://www.vvveb.com) - 功能强大且易于使用的 CMS 可以构建网站、博客或电子商务商店。 ([演示](https://demo.vvveb.com), [源代码](https://github.com/givanz/Vvveb)) `AGPL-3.0` `PHP/Docker`
- [Wagtail](https://wagtail.io/) - Django 内容管理系统注重灵活性和用户体验。 ([源代码](https://github.com/wagtail/wagtail)) `BSD-3-Clause` `Python`
- [WinterCMS](https://wintercms.com/) - 基于 Laravel PHP 框架构建的快速且安全的内容管理系统。 ([源代码](https://github.com/wintercms/winter)) `MIT` `PHP`
- [WonderCMS](https://www.wondercms.com) - WonderCMS 是自 2008 年以来最小的平面文件 CMS。 ([演示](https://www.wondercms.com/demo), [源代码](https://github.com/WonderCMS/wondercms)) `MIT` `PHP`
- [WordPress](https://wordpress.org/) - 世界上最常用的博客和 CMS 引擎。 ([源代码](https://github.com/WordPress/WordPress)) `GPL-2.0` `PHP`


### 客户关系管理（CRM）

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

[客户关系管理 (CRM)](https://en.wikipedia.org/wiki/Customer_relationship_management) 是组织用来管理、分析和改进与客户互动的战略流程。

_相关：[通信 - 电子邮件 - 邮件列表和新闻通讯](#通信---电子邮件---邮件列表和新闻通讯)、[分析](#analytics)、[日历和联系人](#calendar--contacts)_

- [Corteza](https://docs.cortezaproject.org) - CRM 包括统一的工作空间、企业消息传递和低代码环境，用于快速、安全地交付基于记录的管理解决方案。 ([演示](https://latest.cortezaproject.org), [源代码](https://github.com/cortezaproject/corteza)) `Apache-2.0` `Go`
- [Django-CRM](https://DjangoCRM.github.io/info/) - 具有任务管理、电子邮件营销等功能的分析型 CRM。 Django CRM 专为个人使用、任何规模的企业或自由职业者而构建，旨在提供轻松的定制和快速开发。 ([源代码](https://github.com/DjangoCRM/django-crm)) `AGPL-3.0` `Python`
- [EspoCRM](https://www.espocrm.com/) - 具有设计为单页应用程序的前端和 REST API 的 CRM。 ([演示](https://demo.espocrm.com/), [源代码](https://github.com/espocrm/espocrm)) `AGPL-3.0` `PHP`
- [Krayin](https://krayincrm.com/) - 面向中小企业和企业的完整客户生命周期管理的 CRM 解决方案。 ([演示](https://demo.krayincrm.com/), [源代码](https://github.com/krayin/laravel-crm)) `MIT` `PHP`
- [Monica](https://monicahq.com/) - 个人关系管理器和一种新型 CRM，用于组织与朋友和家人的互动。 ([源代码](https://github.com/monicahq/monica)) `AGPL-3.0` `PHP/Docker`
- [SuiteCRM](https://suitecrm.com) - 屡获殊荣的企业级开源 CRM。 ([源代码](https://github.com/SuiteCRM/SuiteCRM)) `AGPL-3.0` `PHP`
- [Twenty](https://twenty.com) - 现代 CRM 提供开源的灵活性、高级功能和时尚的设计。 ([源代码](https://github.com/twentyhq/twenty)) `AGPL-3.0` `Docker`


### 数据库管理

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

用于[数据库](https://en.wikipedia.org/wiki/Database)管理的Web界面。包括数据库分析和可视化工具。

_相关：[分析](#analytics)、[自动化](#automation)_

_另请参阅：[dbdb.io - 数据库的数据库](https://dbdb.io/)_

- [Adminer](https://www.adminer.org/) - 在单个 PHP 文件中进行数据库管理。适用于 MySQL、MariaDB、PostgreSQL、SQLite、MS SQL、Oracle、Elasticsearch、MongoDB 等。 ([源代码](https://github.com/vrana/adminer)) `Apache-2.0/GPL-2.0` `PHP`
- [Azimutt](https://azimutt.app) - 为现实世界的数据库（大而混乱）设计的可视化数据库探索。探索您的数据库架构和数据，记录它们，扩展它们，甚至获得分析和指南。 ([演示](https://azimutt.app/gallery/gospeak), [源代码](https://github.com/azimuttapp/azimutt)) `MIT` `Elixir/Nodejs/Docker`
- [Baserow](https://baserow.io/) - 无需技术经验即可创建您自己的数据库（替代 Airtable）。 ([源代码](https://gitlab.com/baserow/baserow)) `MIT` `Docker`
- [Bytebase](https://www.bytebase.com/) - 为 DevOps 团队提供安全的数据库架构更改和版本控制，支持 MySQL、PostgreSQL、TiDB、ClickHouse 和 Snowflake。 ([演示](https://demo.bytebase.com), [源代码](https://github.com/bytebase/bytebase)) `MIT` `Docker/K8S/Go`
- [Chartbrew](https://chartbrew.com) - 直接连接到数据库和 API，并使用数据创建漂亮的图表。 ([演示](https://app.chartbrew.com/live-demo), [源代码](https://github.com/chartbrew/chartbrew)) `MIT` `Nodejs/Docker`
- [ChartDB](https://chartdb.io/) - 数据库图表编辑器允许您通过单个查询可视化和设计数据库。 ([演示](https://app.chartdb.io), [源代码](https://github.com/chartdb/chartdb)) `AGPL-3.0` `Nodejs/Docker`
- [CloudBeaver](https://dbeaver.com/) - 管理数据库，支持PostgreSQL、MySQL、SQLite等。 DBeaver 的网络/托管版本。 ([源代码](https://github.com/dbeaver/cloudbeaver)) `Apache-2.0` `Docker`
- [d9](https://d9.webcapsule.io) - 通过直观的管理界面将 SQL 数据库转变为安全的 API。数据平台和无头 CMS（Directus 的分支）。 ([源代码](https://github.com/LaWebcapsule/d9)) `GPL-3.0` `Nodejs`
- [Databunker](https://databunker.org/) - 基于网络、自托管、符合 GDPR 的个人数据或 PII 安全数据库。 ([源代码](https://github.com/securitybunker/databunker)) `MIT` `Docker`
- [Datasette](https://datasette.io/) - 通过轻松的导入和导出以及数据库管理来探索和发布数据。 ([源代码](https://github.com/simonw/datasette)) `Apache-2.0` `Python/Docker`
- [Evidence](https://evidence.dev) - 基于代码的 BI 工具。使用 SQL 和 Markdown 编写报告，并将它们呈现为网站。 ([源代码](https://github.com/evidence-dev/evidence)) `MIT` `Nodejs`
- [Kottster](https://kottster.app/) - 低代码管理面板，连接到您的数据库并自动生成页面来查看和管理您的数据。 ([演示](https://demo.kottster.app/), [源代码](https://github.com/kottster/kottster)) `Apache-2.0` `Nodejs/Docker`
- [Limbas](https://www.limbas.com/en/) - 用于创建数据库驱动的业务应用程序的数据库框架。作为图形数据库前端，它可以高效处理数据库存并灵活开发舒适的数据库应用程序。 ([源代码](https://github.com/limbas/limbas)) `GPL-2.0` `PHP`
- [Mathesar](https://mathesar.org/) - 直观的 UI 可协作管理数据，适合所有技术水平的用户。基于 Postgres 构建 - 连接现有数据库或设置新数据库。 ([源代码](https://github.com/mathesar-foundation/mathesar)) `GPL-3.0` `Docker/Python`


### 域名系统

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

[DNS](https://en.wikipedia.org/wiki/Domain_Name_System) 具有广告拦截功能的服务器和管理工具，主要针对家庭或小型网络。

_另请参阅：[awesome-sysadmin/DNS - 服务器](https://github.com/awesome-foss/awesome-sysadmin#dns---servers)、[awesome-sysadmin/DNS - 控制面板和域管理](https://github.com/awesome-foss/awesome-sysadmin#dns---control-panels--domain-management)_

- [AdGuard Home](https://adguard.com/en/adguard-home/overview.html) - 用户友好的广告和跟踪器阻止 DNS 服务器。 ([源代码](https://github.com/AdguardTeam/AdGuardHome)) `GPL-3.0` `Docker`
- [blocky](https://0xerr0r.github.io/blocky/latest/) - 快速、轻量级的 DNS 代理作为本地网络的广告拦截器，具有多种功能（替代 Pi-hole）。 ([源代码](https://github.com/0xERR0R/blocky)) `Apache-2.0` `Go/Docker`
- [Maza ad blocking](https://maza-ad-blocking.andros.dev/) - 本地广告拦截器。与 Pi-hole 类似，但位于本地并使用您的操作系统。 ([源代码](https://github.com/tanrax/maza-ad-blocking)) `Apache-2.0` `Shell`
- [Pi-hole](https://pi-hole.net/) - Blackhole 用于互联网广告，具有用于管理和监控的 GUI。 ([源代码](https://github.com/pi-hole/pi-hole)) `EUPL-1.2` `Shell/PHP/Docker`
- [Technitium DNS Server](https://technitium.com/dns/) - 具有广告拦截功能的权威/递归 DNS 服务器。 ([源代码](https://github.com/TechnitiumSoftware/DnsServer)) `GPL-3.0` `Docker/C#`


### 文件管理

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

[文档管理系统](https://en.wikipedia.org/wiki/Document_management_system) (DMS) 是一个用于接收、跟踪、管理和存储文档并减少纸张的系统。

- [BentoPDF](https://bentopdf.com) `⚠` - 功能强大、隐私第一的客户端 PDF 工具包，允许您直接在浏览器中操作、编辑、合并和处理 PDF 文件。 ([演示](https://bentopdf.com), [源代码](https://github.com/alam00000/bentopdf)) `AGPL-3.0` `Nodejs/Docker`
- [Docspell](https://docspell.org) - 自动标记文档组织者和存档。 ([源代码](https://github.com/eikek/docspell)) `GPL-3.0` `Scala/Java/Docker`
- [Documenso](https://documenso.com) - 数字文档签名平台（DocuSign 的替代方案）。 ([源代码](https://github.com/documenso/documenso)) `AGPL-3.0` `Nodejs/Docker`
- [Docuseal](https://www.docuseal.co) - 创建、填写和签署数字文档（DocuSign 的替代方案）。 ([演示](https://demo.docuseal.tech/), [源代码](https://github.com/docusealco/docuseal)) `AGPL-3.0` `Docker`
- [EveryDocs](https://github.com/jonashellmann/everydocs-core) - 供私人使用的简单文档管理系统，具有以数字方式组织文档的基本功能。 `GPL-3.0` `Docker/Ruby`
- [Gotenberg](https://gotenberg.dev) - 开发人员友好的 API，可与 Chromium 和 LibreOffice 等强大工具进行交互，将多种文档格式（HTML、Markdown、Word、Excel 等）转换为 PDF 文件等。 ([源代码](https://github.com/gotenberg/gotenberg)) `MIT` `Docker`
- [I, Librarian](https://i-librarian.net) - 整理 PDF 论文和办公文档。它为工业界和学术界的学生和研究小组提供了许多额外的功能。 ([演示](https://eu1.i-librarian.net/demo), [源代码](https://github.com/mkucej/i-librarian-free)) `GPL-3.0` `PHP`
- [Mayan EDMS](https://www.mayan-edms.com) - 用于文档的电子文档管理系统，具有预览生成、OCR 和自动分类等功能。 ([源代码](https://gitlab.com/mayan-edms/mayan-edms)) `GPL-2.0` `Docker/K8S`
- [OpenSign](https://www.opensignlabs.com) `⚠` - 文档签名软件（DocuSign 的替代品）。 ([源代码](https://github.com/opensignlabs/opensign)) `AGPL-3.0` `Nodejs/Docker`
- [Paperless-ngx](https://docs.paperless-ngx.com/) - 使用改进的界面（无纸化的分支）扫描、索引和归档所有纸质文档。 ([演示](https://demo.paperless-ngx.com/), [源代码](https://github.com/paperless-ngx/paperless-ngx)) `GPL-3.0` `Python/Docker`
- [Papermerge](https://papermerge.com) - 文档管理系统专注于扫描文档（电子档案）。以与 dropbox/google Drive 类似的方式浏览文件。 OCR、全文搜索、文本覆盖/选择。 ([源代码](https://github.com/papermerge/papermerge-core)) `Apache-2.0` `Docker/K8S`
- [Papra](https://papra.app) - 简约的文档存储、管理和归档平台旨在易于使用且可供每个人访问。 ([演示](https://demo.papra.app/), [源代码](https://github.com/papra-hq/papra/)) `AGPL-3.0` `Docker`
- [PdfDing](https://www.pdfding.com) - PDF 管理器、查看器和编辑器可在多个设备上提供无缝的用户体验。它被设计为最小化、快速且易于使用 Docker 设置。 ([演示](https://demo.pdfding.com), [源代码](https://github.com/mrmn2/PdfDing)) `AGPL-3.0` `Docker/K8S`
- [SeedDMS](https://www.seeddms.org) - 具有工作流程、访问权限、全文搜索等的文档管理系统。 ([演示](https://www.seeddms.org/about/), [源代码](https://sourceforge.net/p/seeddms/code/ci/master/tree/))​​ `GPL-2.0` `PHP`
- [Signature PDF](https://github.com/24eme/signaturepdf) - 通过协作、组织、压缩和元数据编辑来签署和操作 PDF。 ([演示](https://pdf.24eme.fr/)) `AGPL-3.0` `PHP/deb/Docker`
- [SimpleDMS](https://simpledms.eu) - 易于使用、元数据驱动的开源文档管理系统 (DMS)，适用于小型企业，几乎可以自行对文档进行排序。 ([源代码](https://github.com/simpledms/simpledms), [客户端](https://simpledms.eu/en/product/integrations)) `AGPL-3.0` `Docker`
- [Stirling-PDF](https://github.com/Stirling-Tools/Stirling-PDF) - 本地托管的 Web 应用程序，允许您对 PDF 文件执行各种操作，例如合并、拆分、文件转换和 OCR。 `Apache-2.0` `Docker/Java`


### 文档管理 - 电子书

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

[电子书](https://en.wikipedia.org/wiki/Ebook)图书馆管理软件。

- [Atsumeru](https://atsumeru.xyz) - 漫画/漫画/轻小说媒体服务器，带有适用于 Windows、Linux、macOS 和 Android 的客户端。 ([源代码](https://github.com/Atsumeru-xyz/Atsumeru), [客户端](https://atsumeru.xyz/guides/#how-does-it-work)) `MIT` `Java/Docker`
- [BookLogr](https://github.com/Mozzo1000/booklogr) - 轻松管理您的个人图书库。 ([演示](https://demo.booklogr.app/)) `Apache-2.0` `Docker`
- [Calibre Web Automated](https://github.com/crocodilestick/Calibre-Web-Automated) - 一体化解决方案，将 Calibre-Web 的现代轻量级 Web UI 与 Calibre（Calibre Web 的分支）强大、多功能的功能集相结合。 `GPL-3.0` `Docker`
- [Calibre Web](https://github.com/janeczku/calibre-web) - 使用现有的 Calibre 数据库浏览、阅读和下载电子书。 `GPL-3.0` `Python`
- [Calibre](https://calibre-ebook.com/) - 电子书库管理器，可以查看、转换和编目大多数主要电子书格式的电子书，并为远程客户端提供内置 Web 服务器。 ([演示](https://calibre-ebook.com/demo), [源代码](https://github.com/kovidgoyal/calibre)) `GPL-3.0` `Python/deb`
- [Inkheart](https://gitlab.com/Nystik/inkheart) - 轻量级 PDF 库和阅读器。 `Apache-2.0` `Docker`
- [Kapowarr](https://casvt.github.io/Kapowarr/) - 建立和管理漫画书库。根据您的喜好下载、重命名、移动和转换该卷的问题。 ([源代码](https://github.com/Casvt/Kapowarr)) `GPL-3.0` `Docker/Python`
- [Kavita](https://www.kavitareader.com/) - 跨平台电子书/漫画/漫画/pdf 服务器和网络阅读器，具有用户管理、评级和评论以及元数据支持。 ([演示](https://www.kavitareader.com/#demo), [源代码](https://github.com/Kareadita/Kavita)) `GPL-3.0` `.NET/Docker`
- [kiwix-serve](https://github.com/kiwix/kiwix-tools) - 用于通过 ZIM 文件为 wiki 提供服务的 HTTP 守护进程。 `GPL-3.0` `C++`
- [Komga](https://komga.org) - 用于漫画/漫画/BD 的媒体服务器，具有 API 和 OPDS 支持、用于探索图书馆的现代 Web 界面以及 Web 阅读器。 ([源代码](https://github.com/gotson/komga)) `MIT` `Java/Docker`
- [MyMangaDB](https://github.com/FabianRolfMatthiasNoll/MyMangaDB) `⚠` - 漫画收藏管理器，具有自动元数据、MyAnimeList 导入和详细的收藏统计信息。 `GPL-3.0` `Docker`
- [Stump](https://www.stumpapp.dev) - 一个快速、免费、开源的漫画、漫画和数字图书服务器，支持 OPDS。 ([源代码](https://github.com/stumpapp/stump)) `MIT` `Rust`


### 文档管理 - 机构存储库和数字图书馆软件

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

[机构知识库](https://en.wikipedia.org/wiki/Institutional_repository)和[数字图书馆](https://en.wikipedia.org/wiki/Digital_library)管理软件。

- [DSpace](http://www.dspace.org/) - 交钥匙存储库应用程序提供对数字资源的持久访问。 ([源代码](https://github.com/DSpace/DSpace)) `BSD-3-Clause` `Java`
- [EPrints](https://www.eprints.org/) - 具有灵活的元数据和工作流程模型的数字文档管理系统主要针对学术机构。 ([演示](http://tryme.demo.eprints-hosting.org/), [源代码](https://github.com/eprints/eprints3.4)) `GPL-3.0` `Perl`
- [Fedora Commons Repository](https://wiki.lyrasis.org/display/FF/Fedora+Repository+Home) - 强大的模块化存储库系统，用于管理和传播数字内容，特别适合数字图书馆和档案馆的访问和保存。 ([源代码](https://github.com/fcrepo/fcrepo)) `Apache-2.0` `Java`
- [InvenioRDM](https://inveniordm.docs.cern.ch/) - 高度可扩展的交钥匙研究数据管理平台，具有良好的用户体验。 ([演示](https://inveniordm.web.cern.ch/), [源代码](https://github.com/inveniosoftware/invenio-app-rdm), [客户端](https://inveniosoftware.org/products/rdm/)) `MIT` `Python`
- [Islandora](https://www.islandora.ca/) - 用于浏览和管理基于 Fedora 的数字存储库的 Drupal 模块。 ([演示](https://sandbox.islandora.ca/), [源代码](https://github.com/Islandora/islandora)) `GPL-3.0` `PHP`
- [Samvera Hyrax](https://samvera.org/) - Samvera 框架的前端，它本身是一个 Ruby on Rails 应用程序，用于浏览和管理基于 Fedora 的数字存储库。 ([源代码](https://github.com/samvera/hyrax)) `Apache-2.0` `Ruby`


### 文档管理 - 综合图书馆系统 (ILS)

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

[集成图书馆系统](https://en.wikipedia.org/wiki/Integrated_library_system) 是图书馆的企业资源规划系统，用于跟踪拥有的图书、订单、支付的账单和借阅的读者。

_相关：[内容管理系统 (CMS)](#content-management-systems-cms)、[归档和数字保存 (DP)](#archiving-and-digital-preservation-dp)_

- [Evergreen](https://evergreen-ils.org) - 高度可扩展的图书馆软件，可帮助图书馆用户查找图书馆资料，并帮助图书馆管理、编目和分发这些资料。 ([源代码](https://github.com/evergreen-library-system/Evergreen)) `GPL-2.0` `PLpgSQL`
- [Koha](https://koha-community.org/) - 企业级 ILS，具有用于采购、流通、编目、标签打印、无法访问互联网时的离线流通等模块。 ([演示](https://koha-community.org/demo/), [源代码](https://github.com/Koha-Community/Koha)) `GPL-3.0` `Perl`
- [RERO ILS](https://rero21.ch/) - 大型 ILS，可以作为具有联盟功能的服务运行，主要用于图书馆网络。包括大多数标准模块（流通、采购、编目……）以及基于网络的公共和专业界面。 ([演示](https://ils.test.rero.ch/), [源代码](https://github.com/rero/rero-ils)) `AGPL-3.0` `Python/Docker`


### 电子商务

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

[电子商务](https://en.wikipedia.org/wiki/E-commerce)软件。

_相关：[社区支持农业 (CSA)](#community-supported-agriculture-csa)_

- [Aimeos](https://aimeos.org/) - 用于使用 Laravel 构建自定义在线商店、市场和复杂 B2B 应用程序的电子商务框架，可扩展到数十亿个项目。 ([演示](https://demo.aimeos.org/), [源代码](https://github.com/aimeos/aimeos)) `LGPL-3.0/MIT` `PHP`
- [Bagisto](https://bagisto.com/en/) - 领先的 Laravel 开源电子商务框架，具有多库存来源、税收、本地化、直销和更多令人兴奋的功能。 ([演示](https://demo.bagisto.com/), [源代码](https://github.com/bagisto/bagisto)) `MIT` `PHP`
- [CoreShop](https://www.coreshop.org) - Pimcore 的电子商务插件。 ([源代码](https://github.com/coreshop/CoreShop)) `GPL-3.0` `PHP`
- [Drupal Commerce](https://drupalcommerce.org) - Drupal CMS 的流行电子商务模块，支持数十种支付、运输和购物相关模块。 ([源代码](https://git.drupalcode.org/project/commerce)) `GPL-2.0` `PHP`
- [EverShop](https://evershop.io/) `⚠` - 具有基本商务功能的电子商务平台。模块化架构且完全可定制。 ([演示](https://demo.evershop.io/), [源代码](https://github.com/evershopcommerce/evershop)) `GPL-3.0` `Docker/Nodejs`
- [Magento Open Source](https://business.adobe.com/products/magento/magento-commerce.html) - 开放式全渠道创新的领先提供商。 ([源代码](https://github.com/magento/magento2)) `OSL-3.0` `PHP`
- [MedusaJs](https://medusajs.com/) - 无头商务引擎，使开发人员能够创造令人惊叹的数字商务体验。 ([演示](https://next.medusajs.com/), [源代码](https://github.com/medusajs/medusa)) `MIT` `Nodejs`
- [Microweber](https://microweber.com/) - 拖放 CMS 和在线商店。 ([源代码](https://github.com/microweber/microweber)) `MIT` `PHP`
- [myCart](https://github.com/shurco/mycart) `⚠` - 1 个文件中的购物车（支持通过卡或加密货币付款）。 `麻省理工学院``Go/Docker`
- [Open Source POS](https://github.com/opensourcepos/opensourcepos) - 开源销售点是一个基于网络的销售点系统。 `麻省理工学院``PHP`
- [OpenCart](https://www.opencart.com) - 购物车解决方案。 ([源代码](https://github.com/opencart/opencart)) `GPL-3.0` `PHP`
- [PrestaShop](https://www.prestashop.com/) - 完全可扩展的电子商务解决方案。 ([演示](https://demo.prestashop.com/), [源代码](https://github.com/PrestaShop/PrestaShop)) `OSL-3.0` `PHP`
- [Pretix](https://pretix.eu/) - 活动门票销售平台。 ([源代码](https://github.com/pretix/pretix)) `AGPL-3.0` `Python/Docker`
- [s-cart](https://s-cart.org/) - 面向个人和企业的电子商务网站，构建在 Laravel 框架之上。 ([演示](https://demo.s-cart.org/), [源代码](https://github.com/gp247net/s-cart)) `MIT` `PHP`
- [Saleor](https://saleor.io) - 基于 Django 的开源电子商务店面。 ([演示](https://demo.saleor.io/), [源代码](https://github.com/saleor/saleor)) `BSD-3-Clause` `Docker/Python`
- [Shopware Community Edition](https://www.shopware.com/en/community/community-edition/) - 德国制造的基于 PHP 的开源电子商务软件。 ([演示](https://www.shopware.com/en/test-demo/), [源代码](https://github.com/shopware/shopware)) `MIT` `PHP`
- [Solidus](https://solidus.io/) - 一个免费的开源电子商务平台，让您可以完全控制您的商店。 ([源代码](https://github.com/solidusio/solidus)) `BSD-3-Clause` `Ruby/Docker`
- [Spree Commerce](https://spreecommerce.org) - Spree 是一个完整的、模块化的、API 驱动的开源电子商务解决方案，适用于 Ruby on Rails。 ([演示](https://demo.spreecommerce.org/), [源代码](https://github.com/spree/spree)) `BSD-3-Clause` `Ruby`
- [Sylius](https://sylius.com) - Symfony2 为电子商务提供支持的开源全栈平台。 ([演示](https://sylius.com/try/), [源代码](https://github.com/Sylius/Sylius)) `MIT` `PHP`
- [Thelia](https://thelia.net/) - Thelia 是一个开源且灵活的电子商务解决方案。 ([演示](https://demo.thelia.net/), [源代码](https://github.com/thelia/thelia)) `LGPL-3.0` `PHP`
- [Vendure](https://www.vendure.io) - 无头商务框架。 ([演示](https://demo.vendure.io), [源代码](https://github.com/vendurehq/vendure)) `MIT` `Nodejs`
- [WooCommerce](https://woocommerce.com/) - 基于 WordPress 的电子商务解决方案。 ([源代码](https://github.com/woocommerce/woocommerce)) `GPL-3.0` `PHP`


### 联合身份和认证

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

[联合身份](https://en.wikipedia.org/wiki/Federated_identity)和[身份验证](https://en.wikipedia.org/wiki/Electronic_authentication)软件。

**请访问[awesome-sysadmin/身份管理](https://github.com/awesome-foss/awesome-sysadmin#identity-management)**



### 饲料读者

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

[新闻聚合器](https://en.wikipedia.org/wiki/News_aggregator)，也称为提要聚合器、提要阅读器、新闻阅读器、[RSS](https://en.wikipedia.org/wiki/RSS) 阅读器，是一种将报纸/博客/视频日志/播客等 Web 内容聚合到一个位置以便于查看的应用程序。

- [Bubo Reader](https://github.com/georgemandis/bubo-rss) - 不合理的最小 RSS 提要阅读器。 ([演示](https://bubo-rss-demo.netlify.app/)) `MIT` `Nodejs`
- [CommaFeed](https://www.commafeed.com/) - Google Reader 启发了自托管 RSS 阅读器。 ([演示](https://www.commafeed.com/#/app/category/all), [源代码](https://github.com/Athou/commafeed)) `Apache-2.0` `Java/Docker`
- [FeedCord](https://github.com/Qolors/FeedCord) `⚠` - 适用于您的 Discord 服务器的简单、轻量级且可定制的 RSS 新闻源。 `麻省理工学院` `Docker`
- [Feeds Fun](https://feeds.fun/) - 带有标签、评分和人工智能的新闻阅读器。 ([源代码](https://github.com/Tiendil/feeds.fun)) `BSD-3-Clause` `Python`
- [FreshRSS](https://freshrss.org/) - 自托管 RSS 提要聚合器。 ([演示](https://demo.freshrss.org/i/), [源代码](https://github.com/FreshRSS/FreshRSS)) `AGPL-3.0` `PHP/Docker`
- [Fusion](https://github.com/0x2E/fusion) - 轻量级 RSS 聚合器和阅读器。 `麻省理工学院``Go/Docker`
- [JARR](https://1pxsolidblack.pl/jarr-en.html) - JARR（Just Another RSS Reader）是一个基于网络的新闻聚合器和阅读器（Newspipe 的分支）。 ([演示](https://www.jarr.info/), [源代码](https://github.com/jaesivsm/JARR)) `AGPL-3.0` `Docker/Python`
- [Kriss Feed](https://github.com/tontof/kriss_feed) - 简单而聪明（或愚蠢）的提要阅读器。 `CC0-1.0` `PHP`
- [Leed](https://github.com/LeedRSS/Leed) - Leed（Light Feed）是一个免费且简约的 RSS 聚合器。 `AGPL-3.0` `PHP`
- [Miniflux](https://miniflux.app/) - 极简新闻阅读器。 ([源代码](https://github.com/miniflux/v2)) `Apache-2.0` `Go/deb/Docker`
- [NewsBlur](https://www.newsblur.com/) - 个人新闻阅读器，让人们聚集在一起谈论世界。旧乐器的新声音。 ([源代码](https://github.com/samuelclay/NewsBlur)) `MIT` `Python`
- [Newspipe](https://git.sr.ht/~cedric/newspipe) - 网络新闻阅读器。 ([演示](https://www.newspipe.org/signup)) `AGPL-3.0` `Python`
- [reader](https://github.com/lemon24/reader) - Feed 阅读器 Web 应用程序和库（因此您可以使用它来构建自己的），仅具有标准库和纯 Python 依赖项。 `BSD-3-子句` `Python`
- [Readflow](https://readflow.app) - 具有现代界面和功能的轻量级新闻阅读器：全文搜索、自动分类、存档、离线支持、通知。 ([源代码](https://github.com/ncarlier/readflow)) `AGPL-3.0` `Go/Docker`
- [RSS-Bridge](https://github.com/RSS-Bridge/rss-bridge) - 为没有 RSS/ATOM 提要的网站生成 RSS/ATOM 提要。 `取消许可` `PHP/Docker`
- [RSS Monster](https://github.com/pietheinstrengholt/rssmonster) - 易于使用的基于网络的 RSS 聚合器和阅读器，与 Fever API 兼容（替代 Google Reader）。 `麻省理工学院``PHP`
- [RSS2EMail](https://github.com/rss2email/rss2email) - 获取 RSS/Atom 源并将新内容推送到任何电子邮件接收器，支持 OPML。 `GPL-2.0` `Python/deb`
- [RSSHub](https://docs.rsshub.app) - 易于使用且可扩展的 RSS 提要聚合器能够从社交媒体到大学部门等几乎所有内容生成 RSS 提要。 ([演示](https://rsshub.app), [源代码](https://github.com/DIYgod/RSSHub)) `MIT` `Nodejs/Docker`
- [Selfoss](https://selfoss.aditu.de/) - 新的多用途 RSS 阅读器、直播、混搭、聚合 Web 应用程序。 ([源代码](https://github.com/fossar/selfoss)) `GPL-3.0` `PHP`
- [Stringer](https://github.com/stringer-rss/stringer) - 正在进行中的自托管、反社交 RSS 阅读器。 “麻省理工学院”“红宝石”
- [Tiny Tiny RSS](https://tt-rss.org) - 基于网络的新闻源 (RSS/Atom) 阅读器和聚合器。 ([源代码](https://github.com/tt-rss/tt-rss)) `GPL-3.0` `Docker/PHP`
- [TinyFeed](https://feed.lovergne.dev/) - 使用简单的 CLI 从提要集合中生成静态 HTML 页面。 ([演示](https://feed.lovergne.dev/demo), [源代码](https://github.com/TheBigRoomXXL/tinyfeed)) `MIT` `Go/Docker`
- [Upvote RSS](https://www.upvote-rss.com/) `⚠` - 从 Reddit、Hacker News、Lemmy、Mbin 等生成丰富的 RSS 提要。 ([演示](https://www.upvote-rss.com/), [源代码](https://github.com/johnwarne/upvote-rss)) `MIT` `Docker/PHP`
- [Yarr](https://github.com/nkanaev/yarr) - Yarr（又一个 RSS 阅读器）是一个基于 Web 的提要聚合器，它既可以用作桌面应用程序，也可以用作个人自托管服务器。 “麻省理工学院”“走吧”


### 文件传输和同步

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

[文件传输](https://en.wikipedia.org/wiki/File_transfer)、[共享](https://en.wikipedia.org/wiki/File_sharing)和[同步软件](https://en.wikipedia.org/wiki/File_synchronization)软件。

_相关：[群件](#groupware)_

- [bewCloud](https://bewcloud.com) - 文件共享+同步、笔记和照片（替代 Nextcloud 和 ownCloud 的 RSS 阅读器）。 ([源代码](https://github.com/bewcloud/bewcloud), [客户端](https://github.com/bewcloud)) `AGPL-3.0` `Docker`
- [Cloudreve](https://cloudreve.org/) - 文件管理和共享系统，支持多个存储提供商。 ([演示](https://demo.cloudreve.org), [源代码](https://github.com/cloudreve/cloudreve)) `GPL-3.0` `Docker/Go`
- [Git Annex](https://git-annex.branchable.com/) - 计算机、服务器、外部驱动器之间的文件同步。 ([源代码](https://git.joeyh.name/index.cgi/git-annex.git/)) `GPL-3.0` `Haskell`
- [Kinto](https://kinto.readthedocs.org) - 具有同步和共享功能的极简 JSON 存储服务。 ([源代码](https://github.com/Kinto/kinto)) `Apache-2.0` `Python`
- [Nextcloud](https://nextcloud.com/) - 按照您的要求，从任何设备访问和共享您的文件、日历、联系人、邮件和[更多](https://apps.nextcloud.com/)。 ([演示](https://try.nextcloud.com/), [源代码](https://github.com/nextcloud/server)) `AGPL-3.0` `PHP/deb`
- [OpenCloud](https://docs.opencloud.eu/) - 文件共享和协作平台。 ([源代码](https://github.com/opencloud-eu/opencloud)) `Apache-2.0` `Docker/Go/Nodejs`
- [OpenSSH SFTP server](https://www.openssh.com/) - 安全文件传输程序。 ([源代码](https://cvsweb.openbsd.org/cgi-bin/cvsweb/src/usr.bin/ssh/)) `BSD-2-Clause` `C/deb`
- [ownCloud](https://owncloud.org/) - 用于保存、同步、查看、编辑和共享文件、日历、地址簿等的一体化解决方案。 ([源代码](https://github.com/owncloud/core), [客户端](https://github.com/owncloud/core/wiki/Apps)) `AGPL-3.0` `PHP/Docker/deb`
- [Peergos](https://peergos.org) - 安全且私密的在线空间，您可以在其中存储、共享和查看您的照片、视频、音乐和文档。还包括日历、新闻源、任务列表、聊天和电子邮件客户端。 ([源代码](https://github.com/Peergos/Peergos)) `AGPL-3.0` `Java`
- [Puter](https://puter.com/) - 基于 Web 的操作系统，旨在功能丰富、速度极快且可高度扩展。 ([演示](https://puter.com/), [源代码](https://github.com/heyputer/puter)) `AGPL-3.0` `Nodejs/Docker`
- [Pydio](https://pydio.com/) - 将任何 Web 服务器转变为强大的文件管理系统和主流云存储提供商的替代方案。 ([演示](https://pydio.com/en/demo), [源代码](https://github.com/pydio/cells)) `AGPL-3.0` `Go`
- [Samba](https://www.samba.org/) - Samba 是适用于 Linux 和 Unix 的标准 Windows 互操作程序套件。它为所有使用SMB/CIFS协议的客户端提供安全、稳定、快速的文件和打印服务。 ([源代码](https://git.samba.org/samba.git/)) `GPL-3.0` `C`
- [Seafile](https://www.seafile.com/en/home/) - 主要针对团队和组织的文件托管和共享解决方案。 ([源代码](https://github.com/haiwen/seafile)) `GPL-2.0/GPL-3.0/AGPL-3.0/Apache-2.0` `C`
- [Sync-in](https://sync-in.com) - 文件存储、同步、共享以及与实时编辑、权限管理和桌面/CLI 客户端的协作。 ([演示](https://sync-in.com/docs/demo), [源代码](https://github.com/Sync-in/server), [客户端](https://github.com/Sync-in/desktop)) `AGPL-3.0` `Nodejs/Docker`
- [Syncthing](https://syncthing.net/) - Syncthing 是一个开源的点对点文件同步工具。 ([源代码](https://github.com/syncthing/syncthing)) `MPL-2.0` `Go/Docker/deb`
- [Unison](https://www.cis.upenn.edu/~bcpierce/unison/) - Unison 是一个适用于 OSX、Unix 和 Windows 的文件同步工具。 ([源代码](https://github.com/bcpierce00/unison)) `GPL-3.0` `deb/OCaml`


### 文件传输 - 分布式文件系统

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

网络分布式文件系统。

**请访问[awesome-sysadmin/Distributed Filesystems](https://github.com/awesome-foss/awesome-sysadmin#distributed-filesystems)**



### 文件传输 - 对象存储和文件服务器

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

[对象存储](https://en.wikipedia.org/wiki/Object_storage) 是一种将数据作为对象进行管理的计算机数据存储，这与其他存储架构不同，例如将数据作为文件层次结构进行管理的文件系统，以及将数据作为扇区和磁道内的块进行管理的块存储。

- [GarageHQ](https://garagehq.deuxfleurs.fr/) - 地理分布式、S3 兼容的存储服务，可以满足多种需求。 ([源代码](https://git.deuxfleurs.fr/Deuxfleurs/garage)) `AGPL-3.0` `Docker/Rust`
- [Harbor](https://goharbor.io/) - 用于存储、签名和扫描内容的云本机图像注册表。 ([源代码](https://github.com/goharbor/harbor)) `Apache-2.0` `Docker/K8S`
- [SeaweedFS](https://github.com/seaweedfs/seaweedfs) - SeaweedFS是一个开源分布式文件系统，支持WebDAV、S3 API、FUSE挂载、HDFS等，针对大量小文件进行了优化，并且易于添加容量。 `Apache-2.0` `开始`
- [Zenko CloudServer](https://www.zenko.io/cloudserver) - Zenko CloudServer，处理 Amazon S3 协议的服务器的开源实现。 ([源代码](https://github.com/scality/cloudserver)) `Apache-2.0` `Docker/Nodejs`
- [ZOT OCI Registry](https://zotregistry.dev) - 生产就绪、供应商中立的 OCI 本机容器映像注册表。 ([演示](https://zothub.io), [源代码](https://github.com/project-zot/zot)) `Apache-2.0` `Go/Docker`


### 文件传输 - 点对点文件共享

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

[点对点文件共享](https://en.wikipedia.org/wiki/Peer-to-peer_file_sharing)是使用[点对点](https://en.wikipedia.org/wiki/Peer-to-peer)(P2P)网络技术来分发和[共享](https://en.wikipedia.org/wiki/File_sharing)数字媒体。

- [bittorrent-tracker](https://webtorrent.io/) - 简单、强大的 BitTorrent 跟踪器（客户端和服务器）实现。 ([源代码](https://github.com/webtorrent/bittorrent-tracker)) `MIT` `Nodejs`
- [Deluge](https://deluge-torrent.org/) - 轻量级、跨平台的 BitTorrent 客户端。 ([源代码](https://git.deluge-torrent.org/deluge/tree/?h=develop)) `GPL-3.0` `Python/deb`
- [PrivyDrop](https://www.privydrop.app) - 基于WebRTC的简单易用、可断点续传的点对点文本、图像和文件传输工具。 ([源代码](https://github.com/david-bai00/PrivyDrop)) `MIT` `Docker/Nodejs`
- [qBittorrent](https://www.qbittorrent.org/) - 免费的跨平台 BitTorrent 客户端，具有功能丰富的 Web UI，可用于远程访问。 ([源代码](https://github.com/qbittorrent/qBittorrent)) `GPL-2.0` `C++`
- [Send](https://gitlab.com/timvisee/send) - 简单、私密、端到端加密的临时文件共享，最初由 Mozilla 构建。 ([演示](https://send.vis.ee/), [客户端](https://gitlab.com/timvisee/send#clients)) `MPL-2.0` `Nodejs/Docker`
- [slskd](https://github.com/slskd/slskd) `⚠` - 用于 Soulseek 文件共享网络的现代客户端-服务器应用程序。 `AGPL-3.0` `Docker/C#`
- [Transmission](https://transmissionbt.com/) - 快速、简单、免费的 Bittorrent 客户端。 ([源代码](https://github.com/transmission/transmission)) `GPL-3.0` `C++/deb`
- [Webtor](https://github.com/webtor-io/self-hosted) - 基于网络的 torrent 客户端，具有即时音频/视频流。 ([演示](https://webtor.io)) `MIT` `Docker`


### 文件传输 - 单击和拖放上传

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

用于共享一次性/短期/临时文件的简化文件服务器，提供单击或[拖放](https://en.wikipedia.org/wiki/Drag_and_drop)上传功能。

- [015](https://send.fudaoyuan.icu) - 一个临时文件共享平台。专注于提供一次性、临时文件和文本上传、处理和共享服务。 ([源代码](https://github.com/keven1024/015)) `AGPL-3.0` `Docker`
- [Chibisafe](https://chibisafe.app) - 文件上传服务旨在易于使用和设置。它接受文件、照片、文档以及您想象的任何内容，并返回一个可共享的链接供您发送给其他人。 ([源代码](https://github.com/chibisafe/chibisafe)) `MIT` `Docker/Nodejs`
- [Digirecord](https://ladigitale.dev/digirecord/) - 录制和共享音频文件（法语文档）。 ([源代码](https://codeberg.org/ladigitale/digirecord)) `AGPL-3.0` `Nodejs/PHP`
- [elixire](https://gitlab.com/elixire/elixire) - 简单而先进的屏幕截图上传和链接缩短服务。 ([客户端](https://gitlab.com/elixire/elixiremanager)) `AGPL-3.0` `Python`
- [Enclosed](https://enclosed.cc/) - 专为发送私密且安全的笔记而设计的简约 Web 应用程序。 ([演示](https://enheld.cc/), [源代码](https://github.com/CorentinTh/enheld)) `Apache-2.0` `Docker/Nodejs`
- [Files Sharing](https://github.com/axeloz/filesharing) - 基于唯一和临时链接的文件共享应用程序。 `GPL-3.0` `PHP/Docker`
- [Flare](https://github.com/FlintSH/Flare) - 一个不臃肿、现代且高度可配置的文件/屏幕截图保管库服务器，支持 ShareX、Flameshot 和 Spectacle。提供 OCR 搜索等。 `麻省理工学院` `Docker/Nodejs`
- [Gokapi](https://github.com/Forceu/gokapi) - 用于共享文件的轻量级服务器，文件在一定的下载量或天数后就会过期。与已停产的 Firefox Send 类似，不同之处在于仅允许管理员上传文件。 `GPL-3.0` `Go/Docker`
- [goploader](https://depado.github.io/goploader/) - 通过服务器端加密轻松共享文件，兼容curl/httpie/wget。 ([源代码](https://github.com/Depado/goploader)) `MIT` `Go`
- [GoSƐ](https://codeberg.org/stv0g/gose) - 现代文件上传器注重可扩展性和简单性。它仅依赖于 S3 存储后端，因此可以水平扩展，无需额外的数据库或缓存。 `Apache-2.0` `Go/Docker`
- [Jirafeau](https://gitlab.com/jirafeau/Jirafeau) - 一键文件共享项目。选择您的文件，上传并共享链接。就是这样。 `AGPL-3.0` `PHP/Docker`
- [OnionShare](https://github.com/onionshare/onionshare) - 安全、匿名地共享任何大小的文件。 `GPL-3.0` `Python/deb`
- [PicoShare](https://github.com/mtlynch/picoshare) - 用于共享图像和其他文件的极简、易于托管的服务。 `AGPL-3.0` `Go/Docker`
- [Picsur](https://github.com/CaramelFur/Picsur) - 简单的图像托管平台，让您轻松托管、编辑和共享图像。 `AGPL-3.0` `Docker`
- [PictShare](https://www.pictshare.net/) - 多语言图像托管服务，具有简单的调整大小和上传 API。 ([源代码](https://github.com/HaschekSolutions/pictshare)) `Apache-2.0` `PHP/Docker`
- [Pingvin Share X](https://github.com/smp46/pingvin-share-x) - 文件共享平台，支持登录、反向共享、共享过期、S3 存储桶、高级身份验证、用于安全扫描的 ClamAV 等（Pingvin Share 的分支）。 `BSD-2-Clause` `Docker/Nodejs`
- [Plik](https://github.com/root-gg/plik) - 可扩展且友好的临时文件上传系统。 ([演示](https://plik.root.gg/)) `MIT` `Go/Docker`
- [ProjectSend](https://www.projectsend.org/) - 上传文件并将其分配给您创建的特定客户端。向您的客户授予对这些文件的访问权限。 ([源代码](https://github.com/projectsend/projectsend)) `GPL-2.0` `PHP`
- [PsiTransfer](https://github.com/psi-4ward/psitransfer) - 简单的文件共享解决方案，具有强大的上传/下载恢复和密码保护功能。 `BSD-2-子句` `Nodejs`
- [QuickShare](https://ihexxa.github.io/quickshare.site/) - 在不同设备之间快速简单地共享文件。 ([源代码](https://github.com/ihexxa/quickshare)) `LGPL-3.0` `Docker/Go`
- [Safebucket](https://docs.safebucket.io/) - 具有可插拔基础设施的文件共享平台，上传和下载直接在客户端和 S3 兼容存储之间进行。 ([源代码](https://github.com/safebucket/safebucket)) `Apache-2.0` `Go/Docker`
- [Sharry](https://github.com/eikek/sharry) - 通过可恢复的上传和下载，通过互联网在经过身份验证的用户和匿名用户（双向）之间轻松共享文件。 `GPL-3.0` `Scala/Java/deb/Docker`
- [Shifter](https://github.com/TobySuch/Shifter) - 一个简单的、自托管的文件共享 Web 应用程序，由 Django 提供支持。 `麻省理工学院` `Docker`
- [Slink](https://docs.slinkapp.io/) - 图像共享平台旨在让用户完全控制他们的媒体共享体验。 ([源代码](https://github.com/andrii-kryvoviaz/slink)) `AGPL-3.0` `Docker`
- [transfer.sh](https://github.com/dutchcoders/transfer.sh) - 从命令行轻松共享文件。 “麻省理工学院”“走吧”
- [Uguu](https://github.com/nokonoko/uguu) - 存储文件并在 X 时间后删除。 `麻省理工学院``PHP`
- [XBackBone](https://xbackbone.app/) - 一个简单、快速、轻量级的文件管理器，集成了即时共享工具，例如 ShareX（适用于 Windows 的免费开源屏幕截图实用程序）。 ([源代码](https://github.com/SergiX44/XBackBone)) `AGPL-3.0` `PHP/Docker`
- [Zipline](https://github.com/diced/zipline) - 一个轻量级、快速且可靠的文件共享服务器，通常与 ShareX 一起使用，提供基于 React 的 Web UI 和快速 API。 `麻省理工学院` `Docker/Nodejs`


### 文件传输 - 基于 Web 的文件管理器

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

基于网络的[文件管理器](https://en.wikipedia.org/wiki/File_manager)。

_相关：[群件](#groupware)_

- [Apaxy](https://oupala.github.io/apaxy/) - 主题旨在增强浏览 Web 目录的体验，使用 mod_autoindex Apache 模块和一些 CSS 来覆盖目录列表的默认样式。 ([源代码](https://github.com/oupala/apaxy)) `GPL-3.0` `Javascript`
- [copyparty](https://github.com/9001/copyparty) - 便携式文件服务器，在单个文件中具有加速可恢复上传、重复数据删除、WebDAV、FTP、zeroconf、媒体索引器、视频缩略图、音频转码和只写文件夹，没有强制依赖性。 ([演示](https://a.ocv.me/pub/demo/)) `MIT` `Python`
- [Directory Lister](https://www.directorylister.com/) - 基于 PHP 的简单目录列表器，列出目录及其所有子目录并允许您在其中导航。 ([源代码](https://github.com/DirectoryLister/DirectoryLister)) `MIT` `PHP/Docker`
- [filebrowser](https://filebrowser.org/) - 具有 Material Design Web 界面的 Web 文件浏览器。 ([源代码](https://github.com/filebrowser/filebrowser)) `Apache-2.0` `Go`
- [FileGator](https://filegator.io/) - FileGator 是一款功能强大的多用户文件管理器，具有单页面前端。 ([演示](https://demo.filegator.io), [源代码](https://github.com/filegator/filegator)) `MIT` `PHP/Docker`
- [FileRise](https://github.com/error311/FileRise) - Web 文件管理器，具有上传、标记、共享链接、图库/表格视图和浏览器内编辑器。 ([演示](https://github.com/error311/FileRise?tab=readme-ov-file#live-demo)) `MIT` `Docker/PHP`
- [Filestash](https://www.filestash.app/) - Web 文件管理器可让您管理位于任何位置的数据：FTP、SFTP、WebDAV、Git、S3、Minio、Dropbox 或 Google Drive。 ([演示](https://demo.filestash.app/), [源代码](https://github.com/mickael-kerjean/filestash)) `AGPL-3.0` `Docker`
- [Gossa](https://github.com/pldubouilh/gossa) - 适用于您的文件的轻量且简单的网络服务器。 “麻省理工学院”“走吧”
- [IFM](https://github.com/misterunknown/ifm) - 单脚本文件管理器。 `麻省理工学院``PHP`
- [mikochi](https://github.com/zer0tonin/Mikochi) - 浏览远程文件夹、上传文件、删除、重命名、下载文件并将文件流式传输到 VLC/mpv。 `麻省理工学院` `Go/Docker/K8S`
- [miniserve](https://github.com/svenstaro/miniserve) - 通过 HTTP 提供文件和目录的 CLI 工具。 “麻省理工学院”“铁锈”
- [ResourceSpace](https://www.resourcespace.com) - 简单、快速、免费地组织您的数字资产。 ([演示](https://www.resourcespace.com/Trial), [源代码](https://www.resourcespace.com/svn)) `BSD-4-Clause` `PHP`
- [slcl](https://gitea.privatedns.org/xavi/slcl) - 简单、轻量级的网络云存储。 ([源代码](https://codeberg.org/xavidcr/slcl)) `AGPL-3.0` `C`
- [Surfer](https://git.cloudron.io/cloudron/surfer) - 简单的静态文件服务器，带有 webui 来管理文件。 `麻省理工学院` Nodejs`
- [TagSpaces](https://www.tagspaces.org/) - TagSpaces 是一款离线、跨平台的文件管理器和组织器，也可以用作笔记应用程序。该应用程序的 WebDAV 版本可以安装在 WebDAV 服务器（例如 Nextcloud 或 ownCloud）之上。 ([演示](https://demo.tagspaces.com), [源代码](https://github.com/tagspaces/tagspaces)) `AGPL-3.0` `Nodejs`
- [Tiny File Manager](https://tinyfilemanager.github.io) - PHP 中基于 Web 的文件管理器，简单、快速且小型的单个文件文件管理器。 ([演示](https://tinyfilemanager.github.io/demo/), [源代码](https://github.com/prasathmani/tinyfilemanager)) `GPL-3.0` `PHP`


### 游戏

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

多人游戏服务器和[浏览器游戏](https://en.wikipedia.org/wiki/Browser_game)。

_相关：[游戏 - 管理实用程序和控制面板](#games---管理实用程序--控制面板)_

- [0 A.D.](https://play0ad.com/) - 跨平台古代战争即时战略游戏。 ([源代码](https://gitea.wildfiregames.com/0ad/0ad)) `MIT/GPL-2.0/Zlib` `C++/C/deb`
- [A Dark Room](https://github.com/doublespeakgames/adarkroom) - 适用于您的浏览器的极简文字冒险游戏。 ([演示](https://adarkroom.doublespeakgames.com/)) `MPL-2.0` `Javascript`
- [DDraceNetwork](https://ddnet.org/) - DDRace 的合作平台游戏版本是 Teeworlds 的修改版本，具有独特的合作游戏玩法。 ([源代码](https://github.com/ddnet/ddnet)) `Zlib` `C++`
- [Digibuzzer](https://digibuzzer.app/) - 围绕连接的蜂鸣器创建一个虚拟游戏室（法语文档）。 ([演示](https://digibuzzer.app/), [源代码](https://codeberg.org/ladigitale/digibuzzer)) `AGPL-3.0` `Nodejs`
- [Hypersomnia](https://github.com/TeamHypersomnia/Hypersomnia) - 融合了《反恐精英》和《迈阿密热线》的竞技自上而下射击游戏。可在 Linux、Windows、MacOS 和 Web 上运行。 ([演示](https://hypersomnia.io)) `AGPL-3.0` `C++/Docker`
- [Lila](https://lichess.org/) - 为 lichess.org 提供支持的无广告国际象棋服务器，配有官方 iOS 和 Android 客户端应用程序。 ([源代码](https://github.com/lichess-org/lila)) `AGPL-3.0` `Scala`
- [Luanti](https://www.luanti.org/) - 体素游戏引擎（以前称为 Minetest）。玩我们的众多游戏之一，根据您的喜好修改游戏，制作您自己的游戏，或在多人服务器上玩。 ([源代码](https://github.com/luanti-org/luanti)) `LGPL-2.1/MIT/Zlib` `C++/Lua/deb`
- [Mindustry](https://mindustrygame.github.io/) - 类似异星工厂的塔防游戏。建立生产链以聚集更多资源，并建造复杂的设施。 ([源代码](https://github.com/Anuken/Mindustry)) `GPL-3.0` `Java`
- [MTA:SA](https://multitheftauto.com/) `⚠` - 在 Rockstar North 的 Grand Theft Auto 游戏系列中添加网络游戏功能，该功能最初在该系列游戏中并未找到。 ([源代码](https://github.com/multitheftauto/mtasa-blue)) `GPL-3.0` `C++`
- [OpenTTD](https://www.openttd.org/) - 运输大亨模拟游戏。 ([源代码](https://github.com/OpenTTD/OpenTTD), [客户端](https://bananas.openttd.org/)) `GPL-2.0` `C++/Docker`
- [piqueserver](https://github.com/piqueserver/piqueserver) - openspades 的服务器，可破坏体素世界中的第一人称射击游戏。 ([客户端](https://github.com/yvt/openspades)) `GPL-3.0` `Python/C++`
- [Posio](https://github.com/abrenaut/posio) - 地理多人游戏。 “麻省理工学院”“Python”
- [Razzia](https://github.com/Ralex91/Razzia) - 测验游戏平台，专为小型自办活动而设计（Kahoot 的替代品！）。 `MIT` `Nodejs/Docker`
- [Red Eclipse 2](https://www.redeclipse.net/) - 类似于《虚幻竞技场》的竞技场第一人称射击游戏。 ([源代码](https://github.com/redeclipse/base)) `Zlib/MIT/CC-BY-SA-4.0` `C/C++/deb`
- [Scribble.rs](https://github.com/scribble-rs/scribble.rs) - 一款基于网络的图画游戏。 ([演示](https://scribblers.fly.dev)) `BSD-3-Clause` `Go/Docker`
- [Suroi](https://suroi.io/) - 一款受 surviv.io 启发的开源 2D 大逃杀游戏。 ([演示](https://suroi.io/), [源代码](https://github.com/HasangerGames/suroi)) `GPL-3.0` `Nodejs`
- [The Battle for Wesnoth](https://github.com/wesnoth/wesnoth) - 《韦诺之战》是一款开源、回合制战术策略游戏，具有高度幻想主题，具有单人游戏和在线/热门多人战斗功能。 `GPL-2.0` `C++/deb`
- [Veloren](https://veloren.net/) - 多人角色扮演游戏。开源游戏的灵感来自《魔方世界》、《塞尔达传说》、《矮人要塞》和《我的世界》。 ([源代码](https://gitlab.com/veloren/veloren)) `GPL-3.0` `Rust`
- [Zero-K](https://zero-k.info/) - Springrts 引擎开源。 Zero-K 是一款传统的实时策略游戏，注重通过地形操纵、物理和大量独特单位来发挥玩家的创造力，同时保持平衡以支持竞争性游戏。 ([源代码](https://github.com/ZeroK-RTS/Zero-K)) `GPL-2.0` `Lua`


### 游戏 - 管理实用程序和控制面板

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

用于管理游戏服务器和游戏库的实用程序。

_相关：[游戏](#games)_

- [auto-mcs](https://www.auto-mcs.com) - 跨平台 Minecraft 服务器管理器。 ([源代码](https://github.com/macarooni-man/auto-mcs)) `AGPL-3.0` `Python`
- [Calagopus](https://calagopus.com) - 现代游戏服务器管理面板。部署、监控和管理 Minecraft、Hytale 和其他具有行业领先性能的游戏服务器。 ([源代码](https://github.com/calagopus/panel)) `MIT` `Rust/Docker/deb`
- [Crafty Controller](https://craftycontrol.com/) - Minecraft 启动器和管理器，允许用户从用户友好的界面启动和管理 Minecraft 服务器。 ([源代码](https://gitlab.com/crafty-controller/crafty-4)) `GPL-3.0` `Docker/Python`
- [Drop](https://droposs.org) - 游戏分发平台，专为高效分发和共享无 DRM 的游戏而设计（替代 Steam、GameVault）。 ([源代码](https://github.com/Drop-OSS/drop), [客户端](https://github.com/Drop-OSS/drop-app)) `AGPL-3.0` `Docker`
- [EasyWI](https://easy-wi.com) - Easy-Wi 是一个 Web 界面，允许您管理游戏服务器等服务器守护程序。此外，它还为您提供了一个 CMS，其中包括全自动游戏和语音服务器借出服务。 ([源代码](https://github.com/easy-wi/developer/)) `GPL-3.0` `PHP/Shell`
- [GameAP](https://gameap.com/) - 游戏管理面板用于管理 Linux 和 Windows 上的游戏服务器。 ([演示](https://demo.gameap.com/), [源代码](https://github.com/gameap/gameap), [客户端](https://plugins.gameap.dev/)) `MIT` `Go/Docker`
- [Gameyfin](https://gameyfin.org) - 视频游戏库管理器，具有自动扫描、网络访问、下载和插件支持。 ([源代码](https://github.com/gameyfin/gameyfin)) `AGPL-3.0` `Docker`
- [Gaseous Server](https://github.com/gaseous-project/gaseous-server) `⚠` - 游戏 ROM 管理器，带有内置的基于 Web 的模拟器，使用多个源来识别和提供元数据。 `AGPL-3.0` `Docker/.NET`
- [Lancache](https://lancache.net) `⚠` - LAN 派对游戏缓存变得简单。 ([源代码](https://github.com/lancachenet/monolithic)) `MIT` `Docker/Shell`
- [LinuxGSM](https://linuxgsm.com/) - 用于在 Linux 上部署和管理专用游戏服务器的 CLI 工具：支持 120 多种游戏。 ([源代码](https://github.com/GameServerManagers/LinuxGSM)) `MIT` `Shell`
- [Minus Games](https://accessory.github.io/minus_games_user_guide) - 跨多个设备同步游戏并保存文件。 ([源代码](https://github.com/Accessory/minus_games)) `MIT` `Rust`
- [Ownfoil](https://github.com/a1ex4/ownfoil) - Nintendo Switch 库管理器，具有自动化管理任务（文件识别和组织、缺少更新/DLC），为 Switch 上的多个受支持的客户端提供库服务，并具有商店自定义和多用户身份验证。 `AGPL-3.0` `Docker/Python`
- [Pelican Panel](https://pelican.dev/) - 用于轻松管理游戏服务器的 Web 应用程序，提供用于部署、配置和管理服务器、服务器监控工具和广泛的自定义选项（Pterodactyl 的分支）的用户友好界面。 ([源代码](https://github.com/pelican-dev/panel)) `AGPL-3.0` `PHP/Docker`
- [Pterodactyl](https://pterodactyl.io/) - 游戏服务器的管理面板，为最终用户提供直观的 UI。 ([源代码](https://github.com/pterodactyl/panel)) `MIT` `PHP`
- [PufferPanel](https://www.pufferpanel.com/) - 游戏服务器管理面板专为小型网络和游戏服务器提供商而设计。 ([源代码](https://github.com/pufferpanel/pufferpanel)) `Apache-2.0` `Go`
- [Retrom](https://github.com/JMBeresford/retrom) - 私有云游戏库分发服务器+前端/启动器。 `GPL-3.0` `Docker/Rust`
- [RomM](https://romm.app/) `⚠` - 用于组织、丰富和玩复古游戏的 ROM 管理器，支持 400 多个平台。 ([演示](https://demo.romm.app/), [源代码](https://github.com/rommapp/romm)) `AGPL-3.0` `Docker`
- [SourceBans++](https://sbpp.github.io/) - 在 Source 引擎上运行的游戏的管理、禁止和通信管理系统。 ([源代码](https://github.com/sbpp/sourcebans-pp)) `CC-BY-SA-4.0` `PHP`
- [Sunshine](https://app.lizardbyte.dev/Sunshine/) - Moonlight 的远程游戏流主机，支持高达 120 帧/秒和 4K 分辨率。 ([源代码](https://github.com/LizardByte/Sunshine)) `GPL-3.0` `C++/deb/Docker`


### 家谱

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

[家谱软件](https://en.wikipedia.org/wiki/Genealogy_software)用于记录、组织和发布家谱数据。

- [Genea.app](https://www.genea.app/) - 家谱工具的设计充分考虑了隐私，任何人都可以使用它来创作或编辑他们的家谱。数据以 GEDCOM 格式存储，所有处理都在浏览器中完成。 ([源代码](https://github.com/genea-app/genea-app)) `MIT` `Javascript`
- [Genealogy](https://genealogy.kreaweb.be/) - 记录家庭成员及其关系并建立家谱。 ([演示](https://genealogy.kreaweb.be/), [源代码](https://github.com/MGeurts/genealogy)) `MIT` `PHP`
- [GeneWeb](https://geneweb.tuxfamily.org/wiki/GeneWeb) - 可以离线使用或作为 Web 服务使用的家谱软件。 ([源代码](https://github.com/geneweb/geneweb)) `GPL-2.0` `OCaml`
- [Gramps Web](https://www.grampsweb.org/) - 用于协作家谱的 Web 应用程序，基于开源家谱桌面应用程序 Gramps 并可与 Gramps 互操作。 ([演示](https://gramps-project.github.io/gramps-web-api/), [源代码](https://github.com/gramps-project/gramps-web-api)) `AGPL-3.0` `Docker`
- [webtrees](https://www.webtrees.net) - Webtrees 是网络领先的在线协作家谱应用程序。 ([演示](https://dev.webtrees.net/demo-stable/index.php?ctype=gedcom&ged=demo), [源代码](https://github.com/fisharebest/webtrees)) `GPL-3.0` `PHP`


### 生成人工智能（GenAI）

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

[生成人工智能 (GenAI)](https://en.wikipedia.org/wiki/Generative_artificial_intelligence) 是[人工智能](https://en.wikipedia.org/wiki/Artificial_intelligence) 的一个子集，它使用生成模型来生成文本、图像、视频或其他形式的数据。

- [Agenta](https://agenta.ai/) - 用于即时管理、LLM 评估和可观察性的 LLMOps 平台。通过协作提示工程构建、评估和监控生产级 LLM 应用程序。 ([源代码](https://github.com/agenta-ai/agenta)) `MIT` `Docker`
- [AnythingLLM](https://anythingllm.com/) - 一体化桌面和 Docker AI 应用程序，具有内置 RAG、AI 代理、无代码代理生成器、MCP 兼容性等。 ([源代码](https://github.com/Mintplex-Labs/anything-llm)) `MIT` `Nodejs/Docker`
- [Khoj](https://khoj.dev/) - 你的人工智能第二大脑。从网络或文档中获取答案。构建自定义代理、安排自动化、进行深入研究。将任何在线或本地法学硕士转变为您个人的、自主的人工智能。 ([演示](https://app.khoj.dev/), [源代码](https://github.com/khoj-ai/khoj)) `AGPL-3.0` `Python/Docker`
- [LibreChat](https://www.librechat.ai) `⚠` - 增强的 ChatGPT 兼容 AI 聊天界面，支持多个 AI 提供商，具有多用户身份验证、消息搜索和插件支持。 ([演示](https://chat.librechat.ai), [源代码](https://github.com/danny-avila/LibreChat)) `MIT` `Nodejs/Docker`
- [LLM Harbor](https://github.com/av/harbor) - 容器化 LLM 工具包。通过简洁的 CLI 运行 LLM 后端、API、前端和其他服务。 `Apache-2.0` `Docker/Shell`
- [LLMKube](https://llmkube.com) - 用于 llama.cpp 原生 LLM 推理的 Kubernetes 运算符，具有 GPU 调度、Apple Silicon Metal 支持和 OpenAI 兼容 API。 ([源代码](https://github.com/defilantech/LLMKube)) `Apache-2.0` `Go/Docker/K8S`
- [Local Deep Research](https://github.com/LearningCircuit/local-deep-research) - 由 AI 驱动的深度研究工具，具有多源搜索（arXiv、PubMed、Web）、PDF 文本提取和加密本地存储。 `麻省理工学院` `Docker/Python`
- [LocalAI](https://localai.io/) - 在本地运行您的 AI 模型并生成图像和音频（替代 OpenAI 和 Claude）。 ([源代码](https://github.com/mudler/LocalAI), [客户端](https://localai.io/gallery.html)) `MIT` `Docker/K8S`
- [Ollama](https://ollama.com/) - 启动并运行 Llama 3.3、DeepSeek-R1、Phi-4、Gemma 3 和其他大型语言模型。 ([源代码](https://github.com/ollama/ollama)) `MIT` `Docker/Python`
- [Onyx Community Edition](https://onyx.app) - 适用于任何 LLM 的聊天 UI。它配备了高级功能，如代理、网络搜索、RAG、MCP、深度研究、40 多个知识源的连接器等等。 ([源代码](https://github.com/onyx-dot-app/onyx)) `MIT` `Docker/K8S`
- [Open-WebUI](https://openwebui.com) - 人性化的AI接口，支持Ollama、OpenAI API。 ([源代码](https://github.com/open-webui/open-webui)) `BSD-3-Clause` `Docker/Python`
- [Vane](https://github.com/ItzCrazyKns/Vane) - AI 驱动的搜索引擎（Perplexity AI 的替代品）。 `麻省理工学院` `Docker`


### 群件

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

协作软件或[群件](https://en.wikipedia.org/wiki/Collaborative_software)旨在帮助人们完成共同任务以实现他们的目标。组件通常将文件共享、日历/事件管理、约会安排、地址簿等多种服务重新组合到一个集成的应用程序中。

_相关：[预订和安排](#booking-and-scheduling)_

- [Citadel](https://www.citadel.org/) - 群件包括电子邮件、日历/日程安排、地址簿、论坛、邮件列表、IM、wiki 和博客引擎、RSS 聚合等。 ([源代码](https://www.citadel.org/source.html)) `GPL-3.0` `C/Docker/Shell`
- [Colanode](https://colanode.com) - 具有实时消息传递、富文本页面、文件管理和动态数据库的协作套件 - 专为离线工作而构建（替代 Slack、Notion）。 ([源代码](https://github.com/colanode/colanode)) `Apache-2.0` `K8S/Docker`
- [Cozy Cloud](https://cozy.io/) - 个人云，您可以在其中管理和同步您的文件、笔记、联系人、密码和文档。 ([源代码](https://github.com/cozy/), [客户端](https://github.com/cozy/cozy-store)) `GPL-3.0` `Nodejs`
- [Digipad](https://digipad.app/) - 用于创建协作数字记事本的在线自托管应用程序（法语文档）。 ([源代码](https://codeberg.org/ladigitale/digipad)) `AGPL-3.0` `Nodejs`
- [Digistorm](https://digistorm.app/) - 创建协作调查、测验、头脑风暴和词云（法语文档）。 ([演示](https://digistorm.app/), [源代码](https://codeberg.org/ladigitale/digistorm)) `AGPL-3.0` `Nodejs`
- [Digiwall](https://digiwall.app/) - 创建用于面对面或远程工作的多媒体协作墙（法语文档）。 ([源代码](https://codeberg.org/ladigitale/digiwall)) `AGPL-3.0` `Nodejs`
- [egroupware](https://www.egroupware.org/) - 软件套件包括日历、地址簿、记事本、项目管理工具、客户关系管理工具 (CRM)、知识管理工具、wiki 和 CMS。 ([源代码](https://github.com/EGroupware/egroupware)) `GPL-2.0` `PHP`
- [Group Office](https://www.group-office.com) - 企业 CRM 和群件工具。与同事和客户在线共享项目、日历、文件和电子邮件。 ([源代码](https://github.com/Intermesh/groupoffice/)) `AGPL-3.0` `PHP`
- [Openmeetings](https://openmeetings.apache.org/index.html) - 使用 Red5 Streaming Server 的 API 功能进行远程处理和流媒体处理的视频会议、即时消息、白板、协作文档编辑和其他群件工具。 ([源代码](https://github.com/apache/openmeetings)) `Apache-2.0` `Java`
- [SOGo](https://www.sogo.nu/) - SOGo 提供多种方式来访问日历和消息数据。 CalDAV、CardDAV、GroupDAV 以及 ActiveSync，包括本机 Outlook 兼容性和 Web 界面。 ([演示](https://demo.sogo.nu/SOGo/), [源代码](https://github.com/Alinto/sogo)) `LGPL-2.1` `Objective-C`
- [Tine](https://www.tine-groupware.de/) - 用于公司和组织数字协作的软件。从强大的组件功能到巧妙的附加组件，tine 结合了一切，使日常团队协作变得更加轻松。 ([源代码](https://github.com/tine-groupware/tine)) `AGPL-3.0` `Docker`
- [Tracim](https://github.com/tracim/tracim) - 团队协作的协作平台：文件、线程、笔记、议程等。 `AGPL-3.0/LGPL-3.0/MIT` `Python`
- [Zimbra Collaboration](https://www.zimbra.com/) - 电子邮件、日历、带有 Web 界面的协作服务器和大量集成。 ([源代码](https://github.com/zimbra)) `GPL-2.0/CPAL-1.0` `Java`


### 健康与健身

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

[医疗](https://en.wikipedia.org/wiki/Medical_software)、[健康](https://en.wikipedia.org/wiki/Health_information_technology)和[健身](https://en.wikipedia.org/wiki/Fitness_tracker)软件。

- [Endurain](https://docs.endurain.com/) - 健身跟踪服务旨在让用户完全控制其数据和托管环境。 ([源代码](https://codeberg.org/endurain-project/endurain)) `AGPL-3.0` `Docker`
- [Fasten Health](https://github.com/fastenhealth/fasten-onprem/) `⚠` - 个人/家庭电子病历聚合器，旨在与美国数十万家保险/医院/诊所集成。 `GPL-3.0` `Go/Docker`
- [FitTrackee](https://docs.fittrackee.org/) - 简单的锻炼/活动跟踪器。 ([源代码](https://github.com/SamR1/FitTrackee)) `AGPL-3.0` `Python/Docker`
- [Mere Medical](https://meremedical.co/) `⚠` - 在一个地方管理来自 Epic MyChart、Cerner 和 OnPatient 患者门户的所有医疗记录。注重隐私、自托管、离线优先。 ([演示](https://demo.meremedical.co), [源代码](https://github.com/cfu288/mere-medical)) `GPL-3.0` `Docker/Nodejs`
- [OpenEMR](https://www.open-emr.org/) - 电子健康记录和医疗实践管理解决方案。 ([演示](https://www.open-emr.org/demo/), [源代码](https://github.com/openemr/openemr)) `GPL-3.0` `PHP/Docker`
- [wger](https://wger.de/) - 基于网络的个人锻炼、健身和体重记录器/跟踪器。它还可以用作简单的健身房管理实用程序，并提供完整的 REST API。 ([演示](https://wger.de/en/dashboard), [源代码](https://github.com/wger-project/wger)) `AGPL-3.0` `Python/Docker`
- [Wingfit](https://wingfit.fr) - 极简健身应用程序，用于计划您的锻炼、跟踪您的个人记录并利用智能手表数据。 ([演示](https://wingfit.fr/home), [源代码](https://github.com/itskovacs/wingfit)) `CC-BY-SA-4.0` `Python/Docker`


### 人力资源管理（HRM）

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

[人力资源管理系统](https://en.wikipedia.org/wiki/Human_resource_management_system)结合了许多系统和流程，以确保[人力资源](https://en.wikipedia.org/wiki/Human_resources)、业务流程和数据的轻松管理。

- [admidio](https://www.admidio.org/) - 组织和团体网站的用户管理系统。该系统具有灵活的角色模型，因此可以反映您组织的结构和权限。 ([演示](https://www.admidio.org/demo/), [源代码](https://github.com/Admidio/admidio)) `GPL-2.0` `PHP/Docker`
- [Frappe HR](https://frappe.io/hr) - 完整的 HRMS 解决方案包含超过 13 个不同的模块，从员工管理、入职、休假到工资、税务等。 ([源代码](https://github.com/frappe/hrms)) `GPL-3.0` `Docker/Python/Nodejs`
- [MintHCM](https://minthcm.org/) - 基于两个流行的知名商业应用程序 SugarCRM Community Edition 和 SuiteCRM 的人力资本管理工具。 ([源代码](https://github.com/minthcm/minthcm)) `AGPL-3.0` `PHP`


### 身份管理

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

[身份管理](https://en.wikipedia.org/wiki/Identity_management) (IdM)，也称为身份和访问管理（IAM 或 IdAM），是一个策略和技术框架，用于确保正确的用户拥有对技术资源的适当访问权限。

**请访问[awesome-sysadmin/身份管理](https://github.com/awesome-foss/awesome-sysadmin#identity-management)**



### 物联网 (IoT)

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

[物联网](https://en.wikipedia.org/wiki/Internet_of_things) 描述了具有传感器、处理能力、软件和其他通过互联网与其他设备连接和交换数据的技术的物理对象。

- [Domoticz](https://www.domoticz.com/) - 家庭自动化系统，可让您监控和配置各种设备，例如：灯、开关、各种传感器/仪表（例如温度、雨、风、紫外线、Electra、气体、水等）。 ([源代码](https://github.com/domoticz/domoticz), [客户端](https://github.com/domoticz/domoticz-android)) `GPL-3.0` `C/C++/Docker/Shell`
- [EMQX](https://www.emqx.io/) - 可扩展的 MQTT 代理。在一个集群中连接超过 1 亿个物联网设备，以 1M 消息/秒吞吐量和 1 毫秒延迟移动和处理实时物联网数据。 ([演示](https://www.emqx.com/en/mqtt/public-mqtt5-broker), [源代码](https://github.com/emqx/emqx)) `Apache-2.0` `Docker/Erlang`
- [evcc](https://evcc.io/) - 可扩展的电动汽车充电控制器和家庭能源管理系统。 ([源代码](https://github.com/evcc-io/evcc)) `MIT` `deb/Docker/Go`
- [FHEM](https://fhem.de/fhem.html) - 自动执行家庭中的常见任务，例如开关灯和供暖。它还可用于记录温度或功耗等事件。您可以通过网络或智能手机前端、telnet 或 TCP/IP 直接控制它。 ([源代码](https://svn.fhem.de/trac)) `GPL-3.0` `Perl`
- [FlowForge](https://flowforge.com/) - 以可靠、可扩展且安全的方式部署 Node-RED 应用程序。 FlowForge 平台为 Node-RED 开发团队提供 DevOps 功能。 ([源代码](https://github.com/FlowFuse/flowfuse)) `Apache-2.0` `Nodejs/Docker/K8S`
- [FMD Server](https://fmd-foss.org) - 与 FMD（查找我的设备）Android 应用程序通信的服务器，以定位和控制您的设备。 ([源代码](https://gitlab.com/fmd-foss/fmd-server), [客户端](https://gitlab.com/fmd-foss/fmd-android)) `GPL-3.0` `Docker/Go`
- [Gladys](https://gladysassistant.com/) - 隐私第一的家庭助理。 ([源代码](https://github.com/GladysAssistant/Gladys)) `Apache-2.0` `Nodejs/Docker`
- [Home Assistant](https://home-assistant.io/) - 家庭自动化平台。 ([演示](https://home-assistant.io/demo/), [源代码](https://github.com/home-assistant/core)) `Apache-2.0` `Python/Docker`
- [ioBroker](https://www.iobroker.net/) - 物联网集成平台，专注于楼宇自动化、智能计量、环境辅助生活、过程自动化、可视化和数据记录。 ([源代码](https://github.com/ioBroker/ioBroker)) `MIT` `Nodejs`
- [LHA](https://github.com/javalikescript/lha) - 轻型家庭自动化应用程序可使用 Blockly、HTML 或 Lua 完全扩展。它包括 ConBee、Philips Hue 或 Z-Wave JS 等扩展。 `麻省理工学院` `Lua`
- [Node RED](https://nodered.org/) - 基于浏览器的流程编辑器可帮助您连接硬件设备、API 和在线服务以创建 IoT 解决方案。 ([源代码](https://github.com/node-red/node-red)) `Apache-2.0` `Nodejs/Docker`
- [Onloc](https://onloc.app) - 实时跟踪和分享您的位置。控制和锁定被盗或丢失的手机。 ([源代码](https://github.com/onloc-app/onloc-api), [客户端](https://github.com/onloc-app/onloc-android)) `AGPL-3.0` `Docker`
- [openHAB](https://www.openhab.org) - 用于家庭自动化的与供应商和技术无关的开源软件。 ([源代码](https://github.com/openhab/openhab-core)) `EPL-2.0` `Java`
- [OpenRemote](https://openremote.io) - IoT 资产管理、流规则和 WHEN-THEN 规则、数据可视化、Edge Gateway。 ([演示](https://demo.openremote.io/), [源代码](https://github.com/openremote/openremote)) `AGPL-3.0` `Java`
- [SIP Irrigation Control](https://dan-in-ca.github.io/SIP/) - 用于喷水/灌溉控制的开源软件。 ([源代码](https://github.com/Dan-in-CA/SIP)) `GPL-3.0` `Python`
- [SOLECTRUS](https://solectrus.de) - 光伏仪表板显示能源生产和消耗以及成本和节省计算。 ([演示](https://demo.solectrus.de), [源代码](https://github.com/solectrus/solectrus)) `AGPL-3.0` `Docker`
- [Tasmota](https://tasmota.com) - ESP 设备的开源固件。完全本地控制，可快速设置和更新。使用 MQTT、Web UI、HTTP 或串行进行控制。使用计时器、规则或脚本实现自动化。与家庭自动化解决方案集成。 ([源代码](https://github.com/arendst/Tasmota)) `GPL-3.0` `C/C++`
- [Thingsboard](https://thingsboard.io/) - 开源物联网平台 - 设备管理、数据收集、处理和可视化。 ([演示](https://demo.thingsboard.io/signup), [源代码](https://github.com/thingsboard/thingsboard)) `Apache-2.0` `Java/Docker/K8S`
- [WebThings Gateway](https://webthings.io/gateway/) - WebThings 是 Web of Things 的开源实现，包括 WebThings 网关和 WebThings 框架。 ([源代码](https://github.com/WebThingsIO/gateway)) `MPL-2.0` `Nodejs`


### 库存管理

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

[库存管理软件](https://en.wikipedia.org/wiki/Inventory_management_software)。

_相关：[金钱、预算和管理](#money-budgeting--management)、[资源规划](#resource-planning)_

_另请参阅：[awesome-sysadmin/IT 资产管理](https://github.com/awesome-foss/awesome-sysadmin#it-asset-management)_

- [Cannery](https://cannery.app) - 枪支和弹药追踪应用程序。 ([源代码](https://codeberg.org/shibao/cannery)) `AGPL-3.0` `Docker`
- [HomeBox (SysAdminsMedia)](https://homebox.software/) - 为家庭用户构建的库存和组织系统。 ([演示](https://demo.homebox.software/), [源代码](https://github.com/sysadminsmedia/homebox)) `AGPL-3.0` `Docker/Go`
- [Inventaire](https://inventaire.io/welcome) - 协作资源映射器项目，但仅专注于探索使用维基数据和 ISBN 进行图书映射。 ([源代码](https://codeberg.org/inventaire/inventaires)) `AGPL-3.0` `Nodejs`
- [Inventree](https://docs.inventree.org/en/latest/) - 库存管理系统提供直观的零件管理和库存控制。 ([演示](https://inventree.org/demo), [源代码](https://github.com/inventree/InvenTree)) `MIT` `Python`
- [Open QuarterMaster](https://openquartermaster.com/) - 强大的库存管理系统，设计灵活且可扩展。 ([源代码](https://github.com/Epic-Breakfast-Productions/OpenQuarterMaster)) `GPL-3.0` `deb/Docker`
- [Part-DB](https://docs.part-db.de/) - 电子元件的库存管理系统。 ([演示](https://demo.part-db.de/en/), [源代码](https://github.com/Part-DB/Part-DB-server)) `AGPL-3.0` `Docker/PHP/Nodejs`
- [Shelf](https://www.shelf.nu) - 重视清晰度的团队使用的资产和设备跟踪软件。 Shelf 是一个资产数据库和 QR 资产标签生成器，可让您跨位置创建、管理和概览资产。无限资产，永久免费。 ([源代码](https://github.com/Shelf-nu/shelf.nu)) `AGPL-3.0` `Nodejs`
- [Spoolman](https://github.com/Donkie/Spoolman) - 跟踪 3D 打印机耗材线轴的库存。 `麻省理工学院` `Docker/Python`


### 知识管理工具

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

[知识管理](https://en.wikipedia.org/wiki/Knowledge_management)是与创建、共享、使用和管理知识和信息相关的方法的集合。

_相关：[笔记和编辑](#note-take--editors)、[Wikis](#wikis)、[数据库管理](#database-management)_

- [AFFiNE Community Edition](https://affine.pro/) - 下一代知识库将规划、排序和创建结合在一起。隐私第一、可定制且随时可用（替代 Notion 和 Miro）。 ([演示](https://app.affine.pro/), [源代码](https://github.com/toeverything/AFFiNE)) `MIT/AGPL-3.0` `Docker`
- [Atomic Server](https://atomicserver.eu/) - 知识图数据库，包含文档（类似于 Notion）、表格、搜索和强大的链接数据 API。轻量级、非常快并且没有运行时依赖性。 ([演示](https://atomicdata.dev/), [源代码](https://github.com/ontola/atomic-server)) `MIT` `Docker/Rust`
- [Digimindmap](https://ladigitale.dev/digimindmap/#/) - 创建简单的思维导图（法语文档）。 ([演示](https://ladigitale.dev/digimindmap/#/), [源代码](https://codeberg.org/ladigitale/digimindmap)) `AGPL-3.0` `Nodejs/PHP`
- [LibreKB](https://librekb.com/) - 基于网络的知识库解决方案。一个简单的 Web 应用程序，它几乎可以在任何使用 PHP 和 MySQL 的 Web 服务器或托管提供商上运行。 ([源代码](https://github.com/michaelstaake/LibreKB/)) `GPL-3.0` `PHP`
- [memEx](https://codeberg.org/shibao/memEx) - 受 zettlekasten 和 org-mode 启发的结构化个人知识库。 `AGPL-3.0` `Docker`
- [SiYuan](https://b3log.org/siyuan/) - 隐私第一的个人知识管理软件，用 typescript 和 golang 编写。 ([源代码](https://github.com/siyuan-note/siyuan)) `AGPL-3.0` `Docker/Go`
- [TeamMapper](https://github.com/b310-digital/teammapper) - 主持并创建您自己的思维导图。与您的团队分享您的思维导图会议并就思维导图进行实时协作。 ([演示](https://map.kits.blog)) `MIT` `Docker/Nodejs`


### 学习和课程

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

帮助教育和学习的工具和软件。

- [Canvas LMS](https://www.instructure.com/canvas/) - 学习管理系统 (LMS) 正在彻底改变我们的教育方式。 ([演示](https://canvas.instruct.com/register), [源代码](https://github.com/instruct/canvas-lms)) `AGPL-3.0` `Ruby`
- [Chamilo LMS](https://chamilo.org/) - 创建虚拟校园以提供在线或半在线培训。 ([源代码](https://github.com/chamilo/chamilo-lms)) `GPL-3.0` `PHP`
- [Digiscreen](https://ladigitale.dev/digiscreen/) - 适用于课堂的交互式白板/壁纸，可亲自或远程使用（法语文档）。 ([演示](https://ladigitale.dev/digiscreen/), [源代码](https://codeberg.org/ladigitale/digiscreen)) `AGPL-3.0` `Nodejs/PHP`
- [Digitools](https://ladigitale.dev/digitools) - 一套简单的工具，可亲自或远程辅助课程动画。 （法语文档）。 ([演示](https://ladigitale.dev/digitools/), [源代码](https://codeberg.org/ladigitale/digitools)) `AGPL-3.0` `PHP`
- [edX](https://www.edx.org/) - Open edX 平台是为 edX.org 提供支持的开源代码。 ([源代码](https://github.com/edx/)) `AGPL-3.0` `Python`
- [Gibbon](https://gibbonedu.org/) - 灵活的学校管理平台，旨在让教师、学生、家长和领导的生活更美好。 ([源代码](https://github.com/GibbonEdu/core)) `GPL-3.0` `PHP`
- [Helium](https://www.heliumedu.com) - 使用颜色编码的学生计划表，可用于课程、作业、成绩和笔记，并具有智能通知和多设备同步功能。 ([演示](https://app.heliumedu.com), [源代码](https://github.com/HeliumEdu/platform)) `MIT` `Python/Docker`
- [ILIAS](https://www.ilias.de) - 学习管理系统可以应对您扔给它的任何事情。 ([演示](https://demo.ilias.de), [源代码](https://github.com/ILIAS-eLearning/ILIAS)) `GPL-3.0` `PHP`
- [INGInious](https://inginious.org/?lang=en) - 智能评分器，允许对学生编写的代码进行安全和自动化的测试。 ([源代码](https://github.com/INGInious/INGInious), [客户端](https://github.com/INGInious/plugins)) `AGPL-3.0` `Python/Docker`
- [Moodle](https://moodle.org/) - 学习和课程平台拥有全球最大的开源社区之一。 ([演示](https://moodle.org/demo/), [源代码](https://git.moodle.org/gw)) `GPL-3.0` `PHP`
- [Open eClass](https://www.openeclass.org/) - Open eClass 是一种先进的电子学习解决方案，可以增强教学过程。 ([演示](https://demo.openeclass.org/), [源代码](https://github.com/gunet/openeclass)) `GPL-2.0` `PHP`
- [OpenOLAT](https://www.openolat.com/?lang=en) - 用于教学、教育、评估和交流的学习管理系统。 ([演示](https://learn.olat.com), [源代码](https://github.com/OpenOLAT/OpenOLAT)) `Apache-2.0` `Java`
- [QST](https://qstonline.org) - 在线评估软件。从手机上的快速测验到大规模、高风险、有人监督的桌面测试，简单、安全且经济。 ([演示](https://qstonline.org/free_account.htm), [源代码](https://sourceforge.net/projects/qstonline/)) `GPL-2.0` `Perl`
- [RELATE](https://documen.tician.de/relate/) - 课件包包括以下功能：灵活的规则、统计、多课程支持、课程日历。 ([源代码](https://github.com/inducer/relate)) `MIT` `Python`
- [RosarioSIS](https://www.rosariosis.org/) - 用于学校管理的学生信息系统。包含学生人口统计、成绩、日程安排、出勤、学生账单、纪律和餐饮服务模块。 ([演示](https://www.rosariosis.org/demo/), [源代码](https://gitlab.com/francoisjacquet/rosariosis/)) `GPL-2.0` `PHP`


### 制造

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

用于管理 [3D 打印机](https://en.wikipedia.org/wiki/3D_printing)、[数控机床](https://en.wikipedia.org/wiki/Numerical_control) 和其他物理制造工具的软件。

- [CNCjs](https://cnc.js.org/) - 运行 Grbl、Smoothieware 或 TinyG 的 CNC 铣削控制器的 Web 界面。 ([源代码](https://github.com/cncjs/cncjs/)) `MIT` `Nodejs`
- [Fluidd](https://docs.fluidd.xyz/) - 适用于 3D 打印机固件 Klipper 的轻量级响应式用户界面。 ([源代码](https://github.com/fluidd-core/fluidd)) `GPL-3.0` `Docker/Nodejs`
- [Mainsail](https://docs.mainsail.xyz/) - Klipper 3D 打印机固件的现代且响应灵敏的用户界面。随时随地通过任何设备控制和监控您的打印机。 ([源代码](https://github.com/mainsail-crew/mainsail)) `GPL-3.0` `Docker/Python`
- [Manyfold](https://manyfold.app) - 3D 打印文件的数字资产管理器； STL、OBJ、3MF 等。 ([源代码](https://github.com/manyfold3d/manyfold)) `MIT` `Docker`
- [Octoprint](https://octoprint.org/) - 用于控制消费级 3D 打印机的 Snappy Web 界面。 ([源代码](https://github.com/OctoPrint/OctoPrint)) `AGPL-3.0` `Docker/Python`


### 地图和全球定位系统 (GPS)

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

[地图](https://en.wikipedia.org/wiki/Map)、[制图](https://en.wikipedia.org/wiki/Cartography)、[GIS](https://en.wikipedia.org/wiki/Geographic_information_system)和[GPS](https://en.wikipedia.org/wiki/Global_Positioning_System)软件。

_另请参阅：[awesome-openstreetmap](https://github.com/osmlab/awesome-openstreetmap)、[awesome-gis](https://github.com/sshuair/awesome-gis)_

- [AdventureLog](https://adventurelog.app) - 旅行追踪器和旅行计划器。 ([演示](https://demo.adventurelog.app/signup), [源代码](https://github.com/seanmorley15/AdventureLog)) `GPL-3.0` `Docker`
- [AirTrail](https://airtrail.johan.ohly.dk) - 个人飞行跟踪系统。 ([源代码](https://github.com/johanohly/AirTrail)) `GPL-3.0` `Docker/Nodejs`
- [Bicimon](https://github.com/knrdl/bicimon) - 作为渐进式 Web 应用程序的自行车车速表。 ([演示](https://knrdl.github.io/bicimon/)) `MIT` `Javascript`
- [Dawarich](https://dawarich.app/) - 可视化您的位置历史记录、跟踪您的活动并分析您的旅行模式，并提供完全的隐私和控制（替代 Google 时间线，又称 Google 位置历史记录）。 ([源代码](https://github.com/Freika/dawarich)) `AGPL-3.0` `Docker`
- [Geo2tz](https://github.com/noandrea/geo2tz) - 从地理坐标（纬度、经度）获取时区。 `麻省理工学院``Go/Docker`
- [GraphHopper](https://graphhopper.com/) - 使用 OpenStreetMap 的快速路由库和服务器。 ([源代码](https://github.com/graphhopper/graphhopper)) `Apache-2.0` `Java`
- [Nominatim](https://nominatim.org/) - 用于对 OpenStreetMap 数据进行地理编码（地址 -> 坐标）和反向地理编码（坐标 -> 地址）的服务器应用程序。 ([源代码](https://github.com/osm-search/Nominatim)) `GPL-2.0` `C`
- [Open Source Routing Machine (OSRM)](http://project-osrm.org/) - 高性能路由引擎设计用于在 OpenStreetMap 数据上运行，并提供 HTTP API、C++ 库接口和 Nodejs 包装器。 ([演示](https://map.project-osrm.org/), [源代码](https://github.com/Project-OSRM/osrm-backend)) `BSD-2-Clause` `C++`
- [OpenRouteService](https://openrouteservice.org/) - 路线服务，包括方向、等时线、时间距离矩阵、路线优化等。 ([演示](https://openrouteservice.org/dev/#/api-docs/introduction), [源代码](https://github.com/GIScience/openrouteservice)) `GPL-3.0` `Docker/Java`
- [OpenStreetMap](https://www.openstreetmap.org/) - 创建免费可编辑世界地图的合作项目。 ([源代码](https://github.com/openstreetmap/openstreetmap-website), [客户端](https://wiki.openstreetmap.org/wiki/Software)) `GPL-2.0` `Ruby`
- [OpenTripPlanner](https://www.opentripplanner.org/) - 多式联运行程规划软件基于 OpenStreetMap 数据并使用已发布的 GTFS 格式数据来建议使用当地公共交通系统的路线。 ([源代码](https://github.com/opentripplanner/OpenTripPlanner)) `LGPL-3.0` `Java/Javascript`
- [OwnTracks Recorder](https://github.com/owntracks/recorder) `⚠` - 存储和访问 [OwnTracks](https://owntracks.org/) 位置跟踪应用程序发布的数据。 `GPL-2.0` `C/Lua/deb/Docker`
- [TileServer GL](https://tileserver.readthedocs.io/) - 具有 GL 样式的矢量和栅格地图。由 Mapbox GL Native 进行服务器端渲染。用于 Mapbox GL JS、Android、iOS、Leaflet、OpenLayers、通过 WMTS 的 GIS 等的地图图块服务器。（[源代码](https://github.com/maptiler/tileserver-gl)） `BSD-2-Clause` `Nodejs/Docker`
- [Traccar](https://www.traccar.org/) - 用于跟踪 GPS 位置的 Java 应用程序。支持大量跟踪设备和协议，拥有 Android 和 iOS 应用程序。有一个网络界面来查看您的行程。 ([演示](https://demo.traccar.org/), [源代码](https://github.com/traccar)) `Apache-2.0` `Java`
- [TRIP](https://itskovacs-trip.netlify.app/) - 极简 POI 地图跟踪器和旅行规划器。 ([演示](https://itskovacs-trip.netlify.app/home), [源代码](https://github.com/itskovacs/trip)) `MIT` `Docker`
- [wanderer](https://github.com/open-wanderer/wanderer) - 轨迹数据库，您可以在其中上传录制的曲目或创建新曲目并添加各种元数据以构建易于搜索的目录。 ([演示](https://demo.wanderer.to)) `AGPL-3.0` `Docker/Go/Nodejs`


### 媒体管理

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

[数字媒体](https://en.wikipedia.org/wiki/Digital_media)管理工具和软件。

_相关：[自动化](#automation)、[媒体流](#media-streaming)、[媒体流-音频流](#media-streaming---audio-streaming)、[媒体流-多媒体流](#media-streaming---multimedia-streaming)、[媒体流-视频流](#media-streaming---video-streaming)_

- [ChannelTube](https://github.com/TheWicklowWolf/ChannelTube) `⚠` - 通过 yt-dlp 按计划从 YouTube 频道下载视频或音频。 `AGPL-3.0` `Docker`
- [Deleterr](https://github.com/rfsbraz/deleterr) - 自动媒体清理工具，可根据可配置的规则从 Plex、Sonarr 和 Radarr 中删除已观看和过时的内容。 `麻省理工学院` `Docker`
- [Downtify](https://downtify.henriquesebastiao.com) `⚠` - 下载带有专辑封面和元数据的 Spotify 音乐。 ([源代码](https://github.com/henriquesebastiao/downtify)) `GPL-3.0` `Docker`
- [Lidarr](https://lidarr.audio/) - Usenet 和 BitTorrent 用户的音乐收藏管理器。 ([源代码](https://github.com/Lidarr/Lidarr)) `GPL-3.0` `C#/Docker`
- [LidaTube](https://github.com/TheWicklowWolf/LidaTube) `⚠` - 通过 yt-dlp 查找并获取丢失的 Lidarr 专辑。 `GPL-3.0` `Docker`
- [Lidify](https://github.com/TheWicklowWolf/Lidify) `⚠` - 音乐发现工具，使用 Spotify 或 LastFM 根据选定的 Lidarr 艺术家提供推荐。 `麻省理工学院` `Docker`
- [Medusa](https://github.com/pymedusa/Medusa) - 电视节目的自动视频库管理器。它会监视您最喜欢的节目的新剧集，当它们发布时，它就会发挥其魔力。 ([客户端](https://github.com/medusajs/nextjs-starter-medusa)) `GPL-3.0` `Python`
- [MeTube](https://github.com/alexta69/metube) - youtube-dl 的 Web GUI，支持播放列表。允许从数十个网站下载视频。 `AGPL-3.0` `Python/Nodejs/Docker`
- [MKVPriority](https://github.com/kennethsible/mkvpriority) - 使用可配置的优先级分数选择首选音频和字幕轨道，并设置适当的默认和强制标志。 `麻省理工学院` `Python/Docker`
- [MyTube](https://github.com/franklioxygen/MyTube) `⚠` - yt-dlp 支持网站的下载器和播放器，具有频道订阅、云上传支持和本地库组织。 ([演示](https://mytube-demo.vercel.app)) `MIT` `Nodejs/Docker`
- [nefarious](https://lardbit.github.io/nefarious/) - 自动下载电影和电视节目。 ([源代码](https://github.com/lardbit/nefarious)) `GPL-3.0` `Python`
- [Ombi](https://ombi.io/) - Plex/Emby 的内容请求系统连接到 SickRage、CouchPotato、Sonarr，具有不断增长的功能集。 ([演示](https://app.ombi.io/), [源代码](https://github.com/Ombi-app/Ombi)) `GPL-2.0` `C#/deb`
- [Pinchflat](https://github.com/kieraneglin/pinchflat) `⚠` - 下载使用 yt-dlp 构建的 YouTube 内容。 `AGPL-3.0` `Docker`
- [PodFetch](https://samtv12345.github.io/PodFetch) - 时尚高效的播客下载器。 ([源代码](https://github.com/SamTV12345/PodFetch)) `Apache-2.0` `Docker/Rust`
- [Radarr](https://radarr.video/) - 通过 Usenet 和 BitTorrent（Sonarr 的分支）自动下载电影。 ([源代码](https://github.com/Radarr/Radarr)) `GPL-3.0` `C#/Docker`
- [Reaparr](https://www.reaparr.rocks/) `⚠` - 跨平台 Plex 媒体下载器，可将其他 Plex 服务器中的媒体无缝添加到您自己的服务器中。 ([源代码](https://github.com/Reaparr/Reaparr)) `GPL-3.0` `Docker`
- [Seerr](https://github.com/seerr-team/seerr) - 管理媒体库请求，支持 Plex、Jellyfin 和 Emby 媒体服务器（Overseerr 的分支）。 `麻省理工学院` `Docker/Nodejs`
- [Sonarr](https://sonarr.tv/) - Usenet 和 BitTorrent 的自动电视节目下载器和管理器。它可以抓取、排序和重命名新剧集，并在出现更好质量的格式时自动升级已下载文件的质量。 ([源代码](https://github.com/Sonarr/Sonarr)) `GPL-3.0` `C#/Docker`
- [TrackWatch](https://trackwatch.emlopezr.com) `⚠` - Spotify 的自动音乐发布跟踪器，带有电子邮件通知、唱片生成器和幽灵曲目清理器（替代发布雷达）。 ([源代码](https://github.com/emlopezr/trackwatch)) `MIT` `Docker`
- [tubesync](https://github.com/meeb/tubesync) `⚠` - 将 YouTube 频道和播放列表同步到本地托管的媒体服务器。 `AGPL-3.0` `Docker/Python`
- [Watcharr](https://github.com/sbondCo/Watcharr) - 添加并跟踪您正在观看的所有节目和电影。具有用户身份验证、现代且干净的用户界面以及非常简单的设置。 ([演示](https://beta.watcharr.app/)) `MIT` `Docker`
- [ydl_api_ng](https://github.com/Totonyus/ydl_api_ng) - 简单的 youtube-dl REST API 可在远程服务器上启动下载。 `GPL-3.0` `Python`
- [Youtarr](https://github.com/DialmasterOrg/Youtarr) `⚠` - 通过 yt-dlp 按计划从 YouTube 频道下载视频，并通过 Web UI 浏览和选择性下载视频。与 Plex 媒体服务器集成并为 Jellyfin、Kodi 和 Emby 生成 NFO 元数据。 `ISC` `Docker`
- [YoutubeDL-Server](https://github.com/nbr23/youtube-dl-server) - Youtube-DL 的 Web 和 REST 接口，用于将视频下载到服务器上。 `麻省理工学院` `Python/Docker`
- [yt-dlp Web UI](https://github.com/marcopiovanello/yt-dlp-web-ui) - yt-dlp 的 Web GUI。 `MPL-2.0` `Docker/Go/Nodejs`


### 媒体流

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

[流媒体](https://en.wikipedia.org/wiki/Streaming_media) 是从源以连续方式传送和消费的多媒体，在网络元素中很少或没有中间存储。

**请访问[媒体流-音频流](#media-streaming---audio-streaming)、[媒体流-多媒体流](#media-streaming---multimedia-streaming)、[媒体流-视频流](#media-streaming---video-streaming)、[媒体管理](#media-management)**

_另请参阅：[流媒体系统列表 - 维基百科](https://en.wikipedia.org/wiki/List_of_streaming_media_systems)、[流媒体系统比较 - 维基百科](https://en.wikipedia.org/wiki/Comparison_of_streaming_media_systems)_



### 媒体流 - 音频流

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

[音频](https://en.wikipedia.org/wiki/Audio) 流媒体工具和软件。

_相关：[媒体管理](#media-management)_

- [Ampache](https://ampache.org/) - 基于网络的音频/视频流应用程序。 ([演示](https://play.dogmazic.net/), [源代码](https://github.com/ampache/ampache)) `AGPL-3.0` `PHP`
- [Audiobookshelf](https://www.audiobookshelf.org/) - 有声读物和播客服务器。它可以传输所有音频格式，跨设备保持和同步进度。附带适用于 Android 和 iOS 的开源应用程序。 ([源代码](https://github.com/advplyr/audiobookshelf), [客户端](https://github.com/advplyr/audiobookshelf-app)) `GPL-3.0` `Docker/deb/Nodejs`
- [Audioserve](https://github.com/izderadicka/audioserve) - 简单的个人服务器，用于提供目录中的音频文件（有声读物、音乐、播客...）。注重简单性并支持客户端之间的游戏位置同步。 “麻省理工学院”“铁锈”
- [AzuraCast](https://www.azuracast.com/) - 现代且易于访问的网络无线电管理套件。 ([源代码](https://github.com/AzuraCast/AzuraCast)) `Apache-2.0` `Docker`
- [Beets](https://beets.io/) - 音乐库管理器和 MusicBrainz 标记器（命令行和 Web 界面）。 ([源代码](https://github.com/beetbox/beets)) `MIT` `Python/deb`
- [Black Candy](https://github.com/blackcandy-org/blackcandy) - 音乐流媒体服务器。 `麻省理工学院` `Docker/Ruby`
- [BotWave](https://botwave.dpip.lol) - 具有服务器-客户端架构的 FM 广播系统，用于远程管理多个 Raspberry Pi 发射器。 ([源代码](https://github.com/dpipstudio/botwave)) `GPL-3.0` `Python`
- [Funkwhale](https://dev.funkwhale.audio/funkwhale) - 现代、基于网络、欢乐、多用户且免费的音乐服务器。 `BSD-3-子句` `Python`
- [gonic](https://github.com/sentriz/gonic) - 轻量级音乐流媒体服务器。亚音速兼容。 `GPL-3.0` `Go/Docker`
- [koel](https://koel.dev/) - 有效的个人音乐流媒体服务器。 ([演示](https://demo.koel.dev/), [源代码](https://github.com/koel/koel)) `MIT` `PHP`
- [LibreTime](https://libretime.org) - 在网络上广播流媒体广播（[Airtime](https://github.com/sourcefabric/Airtime) 的分支）。 ([源代码](https://github.com/LibreTime/libretime)) `AGPL-3.0` `Docker/PHP`
- [LMS](https://github.com/epoupon/lms) - 使用网络界面访问您的自托管音乐。 `GPL-3.0` `Docker/deb/C++`
- [Lyrion Music Server](https://lyrion.org/) - 服务器软件，用于控制各种 Squeezebox/Slim Devices 音频播放器和兼容硬件（以前称为 Logitech Media Server）。 ([源代码](https://github.com/lms-community/slimserver), [客户端](https://lyrion.org/extensions/applications/)) `GPL-2.0` `deb/Docker/Perl`
- [moOde Audio](https://moodeaudio.org/) - 为精彩的 Raspberry Pi 系列单板计算机提供发烧级品质的音乐播放。 ([源代码](https://github.com/moode-player/moode)) `GPL-3.0` `PHP`
- [Mopidy](https://docs.mopidy.com/) `⚠` - 可扩展的音乐服务器。提供 mpd API 的超集，以及与 Spotify、SoundCloud 等第三方服务的集成。（[源代码](https://github.com/mopidy/mopidy)） `Apache-2.0` `Python/deb`
- [mpd](https://www.musicpd.org/) - 用于远程播放音乐、流式传输音乐、处理和组织播放列表的守护进程。许多客户可用。 ([源代码](https://github.com/MusicPlayerDaemon/MPD), [客户端](https://www.musicpd.org/clients/)) `GPL-2.0` `C++`
- [mStream](https://mstream.io/) - 带有 GUI 管理工具的音乐流媒体服务器。可在 Mac、Windows 和 Linux 上运行。 ([源代码](https://github.com/IrosTheBeggar/mStream)) `GPL-3.0` `Nodejs`
- [multi-scrobbler](https://foxxmd.github.io/multi-scrobbler) - Scrobble 从多个源播放到多个 scrobble 服务。 ([源代码](https://github.com/FoxxMD/multi-scrobbler)) `MIT` `Nodejs/Docker`
- [musikcube](https://musikcube.com/) - 带有 Linux/macOS/Windows/Android 客户端的流媒体音频服务器。 ([源代码](https://github.com/clangen/musikcube)) `BSD-3-Clause` `C++/deb`
- [Navidrome Music Server](https://www.navidrome.org) - 现代音乐服务器和流媒体，与 Subsonic/Airsonic 兼容。 ([演示](https://www.navidrome.org/demo), [源代码](https://github.com/navidrome/navidrome), [客户端](https://www.navidrome.org/docs/overview/#apps)) `GPL-3.0` `Docker/Go`
- [Pinepods](https://www.pinepods.online/) - 具有多用户支持的播客管理系统。 Pinepods 利用中央数据库，因此收听时间和主题等方面在不同设备上都遵循。 ([演示](https://try.pinepods.online), [源代码](https://github.com/madeofpendletonwool/PinePods)) `GPL-3.0` `Docker`
- [Polaris](https://github.com/agersant/polaris) - 音乐浏览和流媒体应用程序针对大型音乐收藏进行了优化，易于使用且高性能。 `麻省理工学院` `Rust/Docker`
- [Snapcast](https://github.com/snapcast/snapcast) - 同步多房间音频服务器。 `GPL-3.0` `C++/deb`
- [Stretto](https://github.com/benkaiser/stretto) `⚠` - 具有 Youtube/Soundcloud 导入和 iTunes/Spotify 发现功能的音乐播放器。 ([演示](https://next.kaiserapps.com), [客户端](https://github.com/benkaiser/stretto-mobile-next)) `MIT` `Nodejs`
- [Supysonic](https://github.com/spl0k/supysonic) - Subsonic 服务器 API 的 Python 实现。 `AGPL-3.0` `Python/deb`
- [SwingMusic](https://swingmusic.vercel.app/) - Swing Music 是一个漂亮的、自托管的音乐播放器和本地音频文件的流媒体服务器。就像更酷的 Spotify...但带上你自己的音乐。 ([源代码](https://github.com/swingmx/swingmusic)) `MIT` `Python/Docker`
- [vod2pod-rss](https://github.com/madiele/vod2pod-rss) `⚠` - 将 YouTube 和 Twitch 频道转换为播客，无需存储。将 VoD 即时转码为 MP3 192k，生成 RSS 源以在播客客户端中使用。 `麻省理工学院` `Docker`


### 媒体流 - 多媒体流

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

[多媒体](https://en.wikipedia.org/wiki/Multimedia) 流媒体工具和软件。

_相关：[媒体流-视频流](#media-streaming---video-streaming)、[媒体流-音频流](#media-streaming---audio-streaming)、[媒体管理](#media-management)_

- [ClipBucket](https://clipbucket.fr/) - 只需几分钟即可启动您自己的视频共享网站（YouTube/Netflix 克隆）。 ([演示](https://demo.clipbucket.oxygenz.fr/), [源代码](https://github.com/MacWarrior/clipbucket-v5)) `AAL` `Docker/PHP`
- [cmyflix](https://github.com/farfalleflickan/cmyflix) - 流视频的极简 Plex/Jellyfin 替代方案。 `AGPL-3.0` `C/deb`
- [Gerbera](https://gerbera.io/) - UPnP 媒体服务器，允许您在整个家庭网络中流式传输数字媒体，并在各种 UPnP 兼容设备上收听/观看。 ([源代码](https://github.com/gerbera/gerbera)) `GPL-2.0` `Docker/deb/C++`
- [Icecast 2](https://icecast.org) - 流音频/视频服务器可用于创建互联网广播电台或私人运行的自动点唱机以及介于两者之间的许多东西。 ([源代码](https://gitlab.xiph.org/xiph/icecast-server), [客户端](https://icecast.org/apps/)) `GPL-2.0` `C`
- [Jellyfin](https://jellyfin.org) - 适用于音频、视频、书籍、漫画和照片的媒体服务器，具有时尚的界面和强大的转码功能。几乎所有现代平台都有客户端，包括 Roku、Android TV、iOS 和 Kodi。 ([演示](https://demo.jellyfin.org/stable), [源代码](https://github.com/jellyfin/jellyfin), [客户端](https://github.com/awesome-jellyfin/awesome-jellyfin)) `GPL-2.0` `C#/deb/Docker`
- [Karaoke Eternal](https://www.karaoke-eternal.com) - 举办精彩的卡拉 OK 派对，每个人都可以通过手机浏览器轻松查找和排列歌曲。该播放器还完全基于浏览器，支持 MP3+G、MP4 和 WebGL 可视化。 ([源代码](https://github.com/bhj/KaraokeEternal)) `ISC` `Docker/Nodejs`
- [Kodi](https://kodi.tv/) - 多媒体/娱乐中心，以前称为 XBMC。可在 Android、BSD、Linux、macOS、iOS 和 Windows 上运行。 ([源代码](https://github.com/xbmc/xbmc)) `GPL-2.0` `C++/deb`
- [Kyoo](https://github.com/zoriya/kyoo) - 创新的媒体浏览器专为无缝流式传输动漫、连续剧和电影而设计，提供动态转码、自动观看历史记录和智能元数据检索等高级功能。 ([演示](https://kyoo.zoriya.dev)) `GPL-3.0` `Docker`
- [MediaMTX](https://mediamtx.org) - 即用型、零依赖性实时媒体服务器和代理，用于通过 SRT、WebRTC、RTSP、RTMP、HLS、MPEG-TS、RTP 发布、读取、记录、播放和路由视频/音频流。 ([源代码](https://github.com/bluenviron/mediamtx), [客户端](https://mediamtx.org/docs/kickoff/introduction)) `MIT` `Go/Docker`
- [Meelo](https://github.com/Arthi-chaud/Meelo) - 个人音乐服务器，专为收藏家和音乐狂人而设计。 `GPL-3.0` `Docker`
- [MistServer](https://mistserver.org/) - 适用于任何设备和任何格式的公共域流媒体服务器。 ([源代码](https://github.com/DDVTECH/mistserver)) `Unlicense` `C++`
- [NymphCast](http://nyanko.ws/nymphcast.php) - 将您选择的支持 Linux 的硬件转变为电视或有源扬声器（Chromecast 的替代方案）的音频和视频源。 ([源代码](https://github.com/MayaPosch/NymphCast)) `BSD-3-Clause` `C++`
- [Rygel](https://gnome.pages.gitlab.gnome.org/rygel/) - UPnP AV MediaServer 可让您轻松共享音频、视频和图片。媒体播放器软件可以使用 Rygel 成为可以由 UPnP 或 DLNA 控制器远程控制的 MediaRenderer。 ([源代码](https://gitlab.gnome.org/GNOME/rygel/)) `LGPL-2.1` `C`
- [Stash](https://stashapp.cc) - 一个基于网络的图书馆组织者和播放器，用于您的成人媒体收藏，具有自动标记和元数据抓取支持。 ([源代码](https://github.com/stashapp/stash)) `AGPL-3.0` `Docker/Go`
- [µStreamer](https://github.com/pikvm/ustreamer) - 轻量且非常快速的服务器，可将 MJPEG 视频从任何 V4L2 设备流式传输到网络。 `GPL-3.0` `C/deb`
- [üWave](https://u-wave.net/) `⚠` - 自托管协作聆听平台。用户轮流播放来自 YouTube 和 SoundCloud 等各种媒体源的媒体（歌曲、演讲、游戏视频或其他任何内容）。 ([演示](https://wlk.yt/), [源代码](https://github.com/u-wave)) `MIT` `Nodejs`


### 媒体流 - 视频流

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

[视频](https://en.wikipedia.org/wiki/Video) 流媒体工具和软件。

_相关：[视频监控](#video-surveillance)、[媒体流-多媒体流](#media-streaming---multimedia-streaming)、[照片画廊](#photo-galleries)、[媒体管理](#media-management)_

- [CyTube](https://github.com/calzoneman/sync) - 为任意数量的频道同步媒体、聊天等。 ([演示](https://cytu.be)) `MIT` `Nodejs`
- [Invidious](https://github.com/iv-org/invidious) `⚠` - 替代 YouTube 前端。 ([演示](https://docs.invidious.io/instances/)) `AGPL-3.0` `Docker/Crystal`
- [MediaCMS](https://mediacms.io) - 现代、功能齐全的开源视频和媒体 CMS，用 Python/Django/React 编写，具有 REST API。 ([源代码](https://github.com/mediacms-io/mediacms)) `AGPL-3.0` `Python/Docker`
- [OvenMediaEngine](https://github.com/OvenMediaLabs/OvenMediaEngine) - 具有亚秒级延迟的流媒体服务器。 ([演示](https://demo.ovenplayer.com)) `AGPL-3.0` `C++/Docker`
- [Owncast](https://owncast.online/) - 去中心化的单用户实时视频流和聊天服务器，用于运行您自己的实时流，其风格与大型主流选项类似。 ([源代码](https://github.com/owncast/owncast)) `MIT` `Go`
- [PeerTube](https://joinpeertube.org/en/) - 直接在网络浏览器中使用 P2P (BitTorrent) 的去中心化视频流平台。 ([源代码](https://github.com/Chocobozzz/PeerTube)) `AGPL-3.0` `Nodejs`
- [Rapidbay](https://github.com/hauxir/rapidbay/) - 视频流服务/Torrent 客户端，允许在浏览器中或 Chromecast/AppleTV/Smart TV 中搜索和播放 Torrent 中的视频。 `麻省理工学院` `Python/Docker`
- [Restreamer](https://datarhei.github.io/restreamer/) - 无需流媒体提供商即可在您的网站上访问 H.264 实时视频流。 ([源代码](https://github.com/datarhei/restreamer)) `Apache-2.0` `Nodejs/Docker`
- [SRS](https://ossrs.io/) - 一个简单、高效、实时的视频服务器，支持RTMP、WebRTC、HLS、HTTP-FLV和SRT。 ([源代码](https://github.com/ossrs/srs)) `MIT` `Docker/C++`
- [SyncTube](https://github.com/RblSb/SyncTube) - 轻量且设置非常简单的 CyTube 替代方案，可以与朋友一起观看视频和聊天。 `MIT` `Nodejs/Haxe`
- [Tube Archiveist](https://tubearchivist.com/) `⚠` - 整理、搜索并欣赏您的 YouTube 收藏。通过元数据索引和用户友好的界面订阅、下载和跟踪查看的内容。 （[源代码]（https://github.com/tubearchivist/tubearchivist），[客户端]（https://docs.tubearchivist.com/faq/#how-do-i-import-my-videos-to-emby-plex-jellyfin-kodi））`GPL-3.0``Docker`
- [Tube](https://git.mills.io/prologic/tube) - 用 Go 编写的类似 YouTube 的（_没有审查和你不需要的功能！_）视频共享应用程序，还支持自动转码为 MP4 H.265 AAC、多个收藏和 RSS 提要。 ([演示](https://tube.mills.io)) `MIT` `Go`
- [VideoLAN Client (VLC)](https://www.videolan.org/) - 跨平台多媒体播放器客户端和服务器，支持大多数多媒体文件以及 DVD、音频 CD、VCD 和各种流媒体协议。 ([源代码](https://code.videolan.org/videolan/vlc)) `GPL-2.0` `C/deb`


### 杂项

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

不适合其他部分的软件。

- [2FAuth](https://github.com/Bubka/2FAuth) - 管理您的双因素身份验证 (2FA) 帐户并生成其安全代码。 ([演示](https://demo.2fauth.app/)) `AGPL-3.0` `PHP/Docker`
- [Anchr](https://anchr.io) - 用于互联网上小型任务的工具箱，包括书签收集、URL 缩短和（加密）图像上传。 ([源代码](https://github.com/muety/anchr)) `GPL-3.0` `Nodejs`
- [Anubis](https://anubis.techaro.lol/) - Web AI 防火墙实用程序，可保护上游资源免受爬虫程序的侵害。 ([源代码](https://github.com/TecharoHQ/anubis)) `MIT` `Docker/deb/Go`
- [asciinema](https://asciinema.org/) - 用于托管 asciicast 的 Web 应用程序。 ([演示](https://asciinema.org/explore), [源代码](https://github.com/asciinema/asciinema-server)) `Apache-2.0` `Elixir/Docker`
- [Baby Buddy](https://github.com/babybuddy/babybuddy) - 帮助护理人员跟踪婴儿睡眠、喂养、尿布更换和趴着时间。 ([演示](https://github.com/babybuddy/babybuddy#-demo)) `BSD-2-Clause` `Python`
- [ClipCascade](https://github.com/Sathvik-Rao/ClipCascade) - 立即在多个设备上同步剪贴板，无需按任何按钮。它可在 Windows、macOS、Linux 和 Android 上使用，通过端到端数据加密提供无缝、安全的剪贴板共享。 `GPL-3.0` `Java/Docker`
- [Cloudlog](https://magicbug.co.uk/cloudlog/) - 随时随地记录您的业余无线电联系人。 ([源代码](https://github.com/magicbug/cloudlog)) `MIT` `PHP/Docker`
- [ConvertX](https://github.com/C4illin/ConvertX) - 在线文件转换器，支持超过一千种不同的格式。 `AGPL-3.0` `Docker`
- [CUPS](https://www.cups.org/) - 通用 Unix 打印系统使用 Internet 打印协议 (IPP) 支持打印到本地和网络打印机。 ([源代码](https://github.com/OpenPrinting/cups)) `GPL-2.0` `C`
- [CyberChef](https://github.com/gchq/CyberChef) - 在 Web 浏览器中执行各种操作，例如 AES、DES 和 Blowfish 加密和解密、创建十六进制转储、计算哈希值等等。 ([演示](https://gchq.github.io/CyberChef)) `Apache-2.0` `Javascript`
- [Digiboard](https://digiboard.app/) - 创建协作白板（法语文档）。 ([源代码](https://codeberg.org/ladigitale/digiboard)) `AGPL-3.0` `Nodejs`
- [Digicard](https://codeberg.org/ladigitale/digicard) - 创建简单的图形组合（法语文档）。 ([演示](https://ladigitale.dev/digicard/)) `AGPL-3.0` `Nodejs`
- [Digicut](https://ladigitale.dev/digicut/) - 使用 FFMPEG.wasm（法语文档）剪切音频和视频文件。 ([源代码](https://codeberg.org/ladigitale/digicut)) `AGPL-3.0` `Nodejs`
- [Digiface](https://ladigitale.dev/digiface/) - 使用 Avataaars 库（法语文档）创建头像。 ([演示](https://ladigitale.dev/digiface/), [源代码](https://codeberg.org/ladigitale/digiface)) `AGPL-3.0` `Nodejs`
- [Digiflashcards](https://ladigitale.dev/digiflashcards/) - 用于创建抽认卡的在线应用程序（法语文档）。 ([源代码](https://codeberg.org/ladigitale/digiflashcards)) `AGPL-3.0` `Nodejs/PHP`
- [Digimerge](https://ladigitale.dev/digimerge/) - 直接在浏览器中组合音频和视频文件（法语文档）。 ([演示](https://ladigitale.dev/digimerge/), [源代码](https://codeberg.org/ladigitale/Digimerge)) `AGPL-3.0` `Nodejs`
- [Digiquiz](https://ladigitale.dev/digiquiz/) - 用于发布使用 H5P 创建的内容的在线应用程序（法语文档）。 ([源代码](https://codeberg.org/ladigitale/digiquiz)) `AGPL-3.0` `Nodejs`
- [Digiread](https://ladigitale.dev/digiread/) `⚠` - 使用 Mozilla 的 Readability 清理在线页面和文章（法语文档）。 ([源代码](https://codeberg.org/ladigitale/digiread)) `AGPL-3.0` `Nodejs/PHP`
- [Digisteps](https://ladigitale.dev/digisteps/) - 用于创建在线教育路径的简单应用程序（法语文档）。 ([源代码](https://codeberg.org/ladigitale/digisteps)) `AGPL-3.0` `Nodejs/PHP`
- [Digitranscode](https://ladigitale.dev/digitranscode) - 直接在浏览器中转换音频文件和视频（法语文档）。 ([演示](https://ladigitale.dev/digitranscode), [源代码](https://codeberg.org/ladigitale/digitranscode)) `AGPL-3.0` `Nodejs`
- [Digiview](https://ladigitale.dev/digiview/) `⚠` - 在无干扰的界面中观看 YouTube 视频（法语文档）。 ([演示](https://ladigitale.dev/digiview/), [源代码](https://codeberg.org/ladigitale/digiview)) `AGPL-3.0` `Nodejs/PHP`
- [Digiwords](https://ladigitale.dev/digiwords/) - 用于创建词云的简单在线应用程序（法语文档）。 ([源代码](https://codeberg.org/ladigitale/digiwords)) `AGPL-3.0` `Nodejs/PHP`
- [DOCAT](https://github.com/docat-org/docat) - 托管您的文档。简单的。版本化。想要。 `麻省理工学院` `Python/Docker`
- [Domain Locker](https://domain-locker.com) - 域名组合管理和跟踪器。 ([演示](https://demo.domain-locker.com), [源代码](https://github.com/lissy93/domain-locker)) `MIT` `Deno/Docker`
- [DOMJudge](https://www.domjudge.org/) - 用于举办编程竞赛的系统，例如 ICPC 地区和世界冠军编程竞赛。 ([演示](https://www.domjudge.org/demo), [源代码](https://github.com/DOMjudge/domjudge)) `GPL-2.0/BSD-3-Clause/MIT` `PHP`
- [ESMira](https://esmira.kl.ac.at) - 开展纵向研究（ESM、AA、EMA），以完全匿名的方式收集数据并与参与者进行沟通。 ([演示](https://demo-esmira.kl.ac.at/#admin,用户名:demo,密码:demodemodemo), [源代码](https://github.com/KL-Psychological-Methodology/ESMira)) `AGPL-3.0` `PHP`
- [F-Droid](https://f-droid.org) - 用于维护 F-Droid 存储库系统的服务器工具。 ([源代码](https://gitlab.com/fdroid/fdroidserver)) `AGPL-3.0` `Python/Docker/deb`
- [Flyimg](https://flyimg.io) - 即时调整图像大小和裁剪图像。使用 ImageMagick 和高效的缓存系统获取 MozJPEG、WebP 或 PNG 的优化图像。 ([演示](https://demo.flyimg.io), [源代码](https://github.com/flyimg/flyimg)) `MIT` `Docker`
- [Geeftlist](https://codeberg.org/nanawel/geeftlist) - 用于在朋友和家人之间管理、共享和预订礼物的协作平台。 `GPL-3.0` `Docker`
- [google-webfonts-helper](https://github.com/majodev/google-webfonts-helper) `⚠` - 自行托管 Google 字体的轻松方式。获取 eot、ttf、svg、woff 和 woff2 文件 + CSS 片段。 ([演示](https://gwfh.mranftl.com/fonts)) `MIT` `Nodejs`
- [Habitica](https://habitica.com/) - 习惯跟踪器应用程序将您的目标视为角色扮演游戏。 ([源代码](https://github.com/HabitRPG/habitica)) `GPL-3.0/CC-BY-SA-3.0` `Nodejs/Docker`
- [HortusFox](https://hortusfox.github.io) - 适合植物爱好者的协作植物管理和跟踪系统。 ([源代码](https://github.com/danielbrendel/hortusfox-web)) `MIT` `PHP/Docker`
- [ImgCompress](https://imgcompress.karimzouine.com) - 完全在 Docker 中运行的图像处理工具。使用本地 AI 压缩、转换、调整大小、批处理图像并删除背景，无需依赖云。 ([源代码](https://github.com/karimz1/imgcompress)) `GPL-3.0` `Docker`
- [Infisical Community Edition](https://infisical.com/) - 用于秘密、证书和特权访问管理的平台。 ([源代码](https://github.com/Infisical/infisical)) `MIT` `Docker/K8S/deb`
- [iSponsorBlockTV](https://github.com/dmunozv04/iSponsorBlockTV) `⚠` - 阻止和跳过赞助商，同时还可以静音和跳过 YouTube 上的广告。 `GPL-3.0` `Docker/Python`
- [IT-Tools by sharevb](https://github.com/sharevb/it-tools) - 为开发人员提供的便捷在线工具集合（[it-tools](https://github.com/CorentinTh/it-tools) 的分支）。 ([演示](https://sharevb-it-tools.vercel.app/)) `GPL-3.0` `Docker`
- [Jelu](https://bayang.github.io/jelu-web) - 已读和待读列表图书跟踪器。 ([源代码](https://github.com/bayang/jelu)) `MIT` `Java/Docker`
- [jetlog](https://github.com/pbogre/jetlog) - 个人飞行跟踪器和查看器。 `GPL-2.0` `Docker`
- [Kasm Workspaces](https://kasmweb.com/) - 将容器化应用程序和桌面流式传输给最终用户。示例包括浏览器中的 Ubuntu，或者只是单个应用程序，例如 Chrome、OpenOffice、Gimp、Filezilla 等。（[演示](https://www.kasmweb.com/#demo)、[源代码](https://github.com/kasmtech)) `GPL-3.0` `Docker`
- [Koillection](https://koillection.github.io/) - Koillection 是一项允许用户管理任何类型集合的服务。 ([源代码](https://github.com/benjaminjonard/koillection)) `MIT` `Docker/PHP`
- [LanguageTool](https://languagetool.org/) - 校对超过 20 种语言。它可以发现许多简单的拼写检查器无法检测到的错误。 ([源代码](https://github.com/languagetool-org/languagetool), [客户端](https://languagetool.org/insights/post/product-windows-app/)) `LGPL-2.1` `Java/Docker`
- [Libre Translate](https://libretranslate.com/) - 机器翻译 API。 ([源代码](https://github.com/LibreTranslate/LibreTranslate)) `AGPL-3.0` `Docker/Python`
- [LubeLogger](https://lubelogger.com) - 基于网络的车辆维护和燃油里程跟踪器。 ([演示](https://github.com/hargata/lubelog?tab=readme-ov-file#demo), [源代码](https://github.com/hargata/lubelog)) `MIT` `Docker/K8S/C#`
- [mosparo](https://mosparo.io/) - 现代垃圾邮件防护工具。它用简单易用的垃圾邮件防护解决方案取代了其他验证码方法。 ([源代码](https://github.com/mosparo/mosparo)) `MIT` `PHP`
- [Movary](https://github.com/leepeuker/movary) `⚠` - 用于跟踪和评价您观看的电影的网络应用程序。 ([演示](https://github.com/leepeuker/movary?tab=readme-ov-file#demo)) `MIT` `Docker/PHP`
- [Neko](https://neko.m1k1o.net) - 在 docker 中运行并使用 WebRTC 的虚拟浏览器。 ([源代码](https://github.com/m1k1o/neko)) `Apache-2.0` `Docker/Go`
- [OmniTools](https://omnitools.app/) - 用于日常任务（编码、操作图像/视频、PDF 或处理数字...）的强大的基于网络的工具集合。 ([源代码](https://github.com/iib0011/omni-tools)) `MIT` `Docker`
- [Open-Meteo](https://open-meteo.com/) - 天气 API 包含来自所有主要国家气象服务的开放数据预报、历史和气候数据。 ([演示](https://open-meteo.com/en/docs), [源代码](https://github.com/open-meteo/open-meteo)) `AGPL-3.0` `Docker`
- [OpenReader](https://openreader.richardr.dev/) - EPUB、PDF、DOCX、MD 和 TXT 文件文本转语音文档阅读器。高品质 TTS 实时阅读文档；或提取有声读物。 ([演示](https://openreader.richardr.dev/), [源代码](https://github.com/richardr1126/openreader)) `MIT` `Docker`
- [OpenZiti](https://openziti.io/) - 功能齐全、零信任、全网状覆盖网络。包括开箱即用的 2FA 支持以及适用于所有主要桌面/移动操作系统的客户端。 ([源代码](https://github.com/openziti/ziti)) `Apache-2.0` `Go`
- [Operational.co](https://operational.co) - 在实时时间轴中接收来自您产品的警报。 ([演示](https://app.operational.co/?signinas=kevin), [源代码](https://github.com/operational-co/operational.co)) `AGPL-3.0` `Nodejs/Docker`
- [penpot](https://penpot.app/) - 面向跨领域团队的基于 Web 的设计和原型平台。 ([源代码](https://github.com/penpot/penpot)) `MPL-2.0` `Docker`
- [POMjs](https://password.oppetmoln.se/) - 随机密码生成器。 ([源代码](https://github.com/joho1968/POMjs)) `GPL-2.0` `Javascript`
- [Pønskelisten](https://github.com/aunefyren/poenskelisten) - 分享愿望清单并就礼品和礼物进行合作。 `GPL-3.0` `Docker/Go`
- [Reactive Resume](https://rxresu.me/) - 独一无二的简历创建工具，牢记您的隐私。完全安全、可定制、可移植、开源且永久免费。 ([演示](https://rxresu.me/), [源代码](https://github.com/AmruthPillai/Reactive-Resume)) `MIT` `Docker/Nodejs`
- [revealjs](https://revealjs.com) - 使用 HTML 轻松创建精美演示文稿的框架。 ([演示](https://revealjs.com/), [源代码](https://github.com/hakimel/reveal.js)) `MIT` `Javascript`
- [Revive Adserver](https://www.revive-adserver.com/) - 广告投放系统。以前称为 OpenX Adserver 和 phpAdsNew。 ([源代码](https://github.com/revive-adserver/revive-adserver)) `GPL-2.0` `PHP`
- [SANE Network Scanning](http://sane-project.org/) - 允许远程客户端访问本地主机上可用的图像采集设备（扫描仪）。 ([源代码](http://www.sane-project.org/cvs.html)) `GPL-2.0` `C`
- [string.is](https://string.is/) - 为开发人员提供的开源、隐私友好的在线字符串工具包。 ([源代码](https://github.com/recurser/string-is)) `AGPL-3.0` `Nodejs`
- [Teleport](https://goteleport.com/) - SSH、Kubernetes、Web 应用程序和数据库的证书颁发机构和访问平面。 ([源代码](https://github.com/gravitational/teleport)) `Apache-2.0` `Go/Docker/K8S`
- [TeslaMate](https://github.com/teslamate-org/teslamate) - 适用于 Tesla 车辆的强大数据记录器。 `麻省理工学院` `Elixir/Docker`
- [URL-to-PNG](https://github.com/jasonraimondi/url-to-png) - URL 到 PNG 实用程序，具有使用 Playwright 进行屏幕截图并行渲染以及通过 Local、S3 或 CouchDB 进行存储缓存的功能。 `MIT` `Nodejs/Docker`
- [Usertour](https://www.usertour.io/) - 用户入门平台可让您在几分钟内轻松创建应用内产品导览、清单和调查。 ([源代码](https://github.com/usertour/usertour/)) `AGPL-3.0` `Docker`
- [Warracker](https://warracker.com) - 保修跟踪器可让您监控到期日期、上传收据/文件并在保修到期前获取警报。 ([源代码](https://github.com/sassanix/Warracker)) `AGPL-3.0` `Docker`
- [Wavelog](https://www.wavelog.org) - 面向无线电爱好者的基于网络的记录软件。增强浏览器的 QSO 日志记录、统计数据和地图。 ([演示](https://demo.wavelog.org), [源代码](https://github.com/wavelog/wavelog)) `MIT` `PHP/Docker`
- [WeeWX](https://weewx.com/) - 适用于气象站的开源软件。 ([演示](https://weewx.com/showcase.html), [源代码](https://github.com/weewx/weewx)) `GPL-3.0` `Python/deb`
- [WeTTY](https://butlerx.github.io/wetty/#/) - 浏览器中的终端通过 http/https。 ([源代码](https://github.com/butlerx/wetty)) `MIT` `Docker/Nodejs`
- [Wishlist](https://github.com/cmintey/wishlist) - 您可以与朋友和家人分享的愿望清单应用程序。 `麻省理工学院` `Docker/K8S`
- [Yamtrack](https://github.com/FuzzyGrim/Yamtrack) `⚠` - 电影、电视节目、动漫、漫画、视频游戏和书籍的媒体跟踪器。 ([演示](https://github.com/FuzzyGrim/Yamtrack?tab=readme-ov-file#demo)) `AGPL-3.0` `Docker/Python`
- [Zero-TOTP](https://zero-totp.com) - 基于零知识加密的完整、可靠、安全和零信任的网络应用程序，用于存储您的 TOTP 代码。 ([源代码](https://github.com/SeaweedbrainCY/zero-totp)) `GPL-3.0` `Docker`


### 资金、预算和管理

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

[资金管理](https://en.wikipedia.org/wiki/Money_management) 和预算软件。

_相关：[库存管理](#inventory-management)、[资源计划](#resource-planning)_

- [Actual](https://actualbudget.org) - 基于零和预算的本地优先个人理财工具，支持跨设备同步、自定义规则、手动交易导入（从 QIF、OFX 和 QFX 文件）以及可选的与多家银行的自动同步。 ([源代码](https://github.com/actualbudget/actual)) `MIT` `Nodejs/Docker`
- [Bigcapital](https://bigcapital.app/) - 适用于中小型企业的财务会计和库存管理软件。 ([源代码](https://github.com/bigcapitalhq/bigcapital)) `AGPL-3.0` `Docker`
- [Bitcart](https://bitcart.ai) - 加密货币支付处理器和开发平台。 ([演示](https://admin.bitcart.ai), [源代码](https://github.com/bitcart/bitcart)) `MIT` `Docker/Python/Nodejs`
- [BTCPay Server](https://btcpayserver.org/) - 比特币和其他加密货币支付处理器。 ([演示](https://mainnet.demo.btcpayserver.org/), [源代码](https://github.com/btcpayserver/btcpayserver)) `MIT` `C#`
- [DePay](https://depay.com) - 直接在您的钱包中接受 Web3 付款。点对点、免费、自托管和开源。 ([演示](https://depay.com/products/ payments), [源代码](https://github.com/depayfi/widgets)) `MIT` `Nodejs`
- [Econumo](https://econumo.com) - 用于管理个人和家庭财务、支持多种货币、联名账户和预算的预算应用程序。 ([演示](https://demo.econumo.com), [源代码](https://github.com/econumo/econumo)) `MIT` `Docker`
- [ExpenseOwl](https://github.com/tanq16/expenseowl) - 极其简单的费用跟踪器，具有漂亮的用户界面。 `麻省理工学院` `Go/Docker/K8S`
- [ezbookkeeping](https://ezbookkeeping.mayswind.net/) - 您自己托管的轻量级个人记账应用程序。 ([演示](https://ezbookkeeping-demo.mayswind.net/), [源代码](https://github.com/mayswind/ezbookkeeping)) `MIT` `Go/Docker`
- [Family Accounting Tool](https://github.com/nymanjens/facto) - 基于网络的财务管理工具，适合部分分担费用的合作伙伴。 `Apache-2.0` `Scala`
- [Fava](https://beancount.github.io/fava/) - Beancount 的 Web 前端，一个基于文本的复式记账系统。 ([演示](https://fava.pythonanywhere.com/example-with-budgets/venue_statement/), [源代码](https://github.com/beancount/fava)) `MIT` `Python`
- [Firefly III](https://firefly-iii.org/) - 萤火虫三世是一位现代理财经理。它可以帮助您跟踪您的资金并进行预算预测。它支持信用卡，拥有先进的规则引擎，可以从多家银行导入数据。 ([演示](https://demo.firefly-iii.org/), [源代码](https://github.com/firefly-iii/firefly-iii)) `AGPL-3.0` `PHP/Docker`
- [FOSSBilling](https://fossbilling.org/) - 托管和计费自动化。与 WHM、CWP、cPanel 和 HestiaCP 集成。完整的API且易于扩展。 ([演示](https://fossbilling.org/demo), [源代码](https://github.com/FOSSBilling/FOSSBilling)) `Apache-2.0` `PHP/Docker`
- [Galette](https://galette.eu/) - 面向非营利组织的会员管理网络应用程序。 ([源代码](https://github.com/galette/galette)) `GPL-3.0` `PHP`
- [Ghostfolio](https://ghostfol.io/) - 用于跟踪股票、ETF 和加密货币的财富管理软件。 ([源代码](https://github.com/ghostfolio/ghostfolio)) `AGPL-3.0` `Docker/Nodejs`
- [GRR](https://grr.devome.com/?lang=en) - 中小型企业的资产管理和预订。 ([源代码](https://github.com/JeromeDevome/GRR)) `GPL-2.0` `PHP`
- [HyperSwitch](https://hyperswitch.io/) `⚠` - 支付开关，使支付快速、可靠且经济实惠。与多个支付处理器连接并轻松路由流量，所有这些都通过单个 API 集成完成。 ([源代码](https://github.com/juspay/hyperswitch)) `Apache-2.0` `Docker/Rust`
- [IHateMoney](https://ihatemoney.org/) - 轻松管理您的共享费用。 ([演示](https://ihatemoney.org/demo/), [源代码](https://github.com/spiral-project/ihatemoney)) `BSD-3-Clause` `Docker/Python`
- [InvoicePlane](https://www.invoiceplane.com/) - 管理小型企业的报价、发票、付款和客户。 ([源代码](https://github.com/InvoicePlane/InvoicePlane)) `MIT` `PHP`
- [InvoiceShelf](https://invoiceshelf.com/) - 跟踪费用、付款并创建专业发票和估算（Crater 的叉子）。 ([源代码](https://github.com/InvoiceShelf/InvoiceShelf)) `AGPL-3.0` `PHP/Docker`
- [Kill Bill](https://killbill.io/) - 订阅计费和支付平台。可以访问实时分析和财务报告。 ([源代码](https://github.com/killbill/killbill)) `Apache-2.0` `Java/Docker`
- [Kresus](https://kresus.org/) - 个人理财经理。 ([演示](https://kresus.org/en/demo.html), [源代码](https://github.com/kresusapp/kresus)) `AGPL-3.0` `Nodejs/Docker`
- [Lago](https://www.getlago.com/) - 计量和基于使用的计费。 ([源代码](https://github.com/getlago/lago)) `AGPL-3.0` `Docker`
- [monetr](https://monetr.app/) - 预算应用程序侧重于规划经常性费用。 ([源代码](https://github.com/monetr/monetr)) `FSL-1.1-MIT` `Docker/K8S`
- [Mybucks.online](https://mybucks.online) - 安全、基于浏览器、仅密码的自我托管加密货币钱包。 ([演示](https://app.mybucks.online), [源代码](https://github.com/mybucks-online/app)) `MIT` `Nodejs`
- [MyFin Budget](https://myfinbudget.com) - 个人财务平台（Web + REST API + Android）将帮助您制定预算、跟踪您的收入/支出并预测您的财务未来。 ([演示](https://github.com/afaneca/myfin?tab=readme-ov-file#demo-account---try-it-for-yourself), [源代码](https://github.com/afaneca/myfin), [客户端](https://github.com/afaneca/myfin-api)) `GPL-3.0` `Nodejs/Docker`
- [OctoBot](https://www.octobot.cloud/) - 加密货币交易机器人。 ([源代码](https://github.com/Drakkar-Software/OctoBot)) `GPL-3.0` `Python/Docker`
- [Ocular](https://simonwep.github.io/ocular/) - 简单明了的预算应用程序可跟踪您数月和数年的预算。 ([演示](https://simonwep.github.io/looking/demo/#demo), [源代码](https://github.com/simonwep/looking)) `MIT`Docker`
- [OpenBudgeteer](https://github.com/TheAxelander/OpenBudgeteer) - 基于桶预算原则的预算应用程序。 `AGPL-3.0` `Docker/C#`
- [Receipt Wrangler](https://receiptwrangler.io) `⚠` - 易于使用的收据管理器，由 AI 提供支持。允许用户轻松快速地创建收据、分类等。 ([演示](https://demo.receiptwrangler.io), [源代码](https://github.com/Receipt-Wrangler/receipt-wrangler)) `AGPL-3.0` `Docker`
- [REI3](https://rei3.de/home_en/) - 管理企业内的任务、时间、资产等。 ([演示](https://rei3.de/demo_en/), [源代码](https://github.com/r3-team/r3)) `MIT` `Go`
- [SHKeeper](https://shkeeper.io/) - 加密货币支付处理器具有网关和商家的独特组合，允许您接受多种加密货币付款，无需费用和中介。 ([演示](https://github.com/vsys-host/shkeeper.io?tab=readme-ov-file#11-demo), [源代码](https://github.com/vsys-host/shkeeper.io)) `GPL-3.0` `Python`
- [SolidInvoice](https://solidinvoice.co) - 开源发票和报价应用程序。 ([源代码](https://github.com/SolidInvoice/SolidInvoice)) `MIT` `PHP`
- [Sure](https://github.com/we-promise/sure) - 适合所有人的个人理财应用程序（Maybe 的分支）。 `AGPL-3.0` `Docker`
- [VoucherVault](https://github.com/l4rm4nd/VoucherVault) - 以数字方式存储和管理优惠券、优惠券、会员卡和礼品卡。支持到期通知、交易历史、文件上传和 OIDC SSO。 `GPL-3.0` `Docker`
- [Wallos](https://wallosapp.com) - 具有统计数据和可选通知的轻量级个人订阅跟踪器。 ([演示](https://github.com/ellite/wallos?tab=readme-ov-file#demo), [源代码](https://github.com/ellite/wallos)) `GPL-3.0` `PHP/Docker`
- [WYGIWYH](https://github.com/eitchtee/WYGIWYH) - 简单而强大的财务追踪器。 ([演示](https://wygiwyh-demo.herculino.com/)) `AGPL-3.0` `Docker/Python`
- [YAFFA](https://www.yaffa.cc) - 个人理财 Web 应用程序，可用于跟踪您的资金、支出、预算和投资。它还有助于长期财务规划。 ([演示](https://sandbox.yaffa.cc), [源代码](https://github.com/kantorge/yaffa)) `MIT` `PHP`


### 监控和状态页面

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

用于[监控](https://en.wikipedia.org/wiki/Monitoring#Computing)系统、网络、应用程序和网站的软件。

**请访问 [awesome-sysadmin/Monitoring](https://github.com/awesome-foss/awesome-sysadmin#monitoring--status-pages)、[awesome-sysadmin/Metrics 和 Metric Collection](https://github.com/awesome-foss/awesome-sysadmin#metrics--metric-collection)**



### 网络实用程序

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

网络实用程序是帮助管理、监控计算机网络和排除故障的工具和软件。

_另请参阅：[awesome-sysadmin/Monitoring](https://github.com/awesome-foss/awesome-sysadmin#monitoring)_

- [beelzebub](https://beelzebub-honeypot.com/) `⚠` - 蜜罐框架，旨在为检测和分析网络攻击提供高度安全的环境。 ([源代码](https://github.com/beelzebub-labs/beelzebub)) `MIT` `Docker/K8S/Go`
- [Canary Tokens](https://canarytokens.org) - 生成称为金丝雀令牌的轻量级嵌入式蜜罐触发器，用于检测未经授权的访问。 ([源代码](https://github.com/thinkst/opencanary)) `BSD-3-Clause` `Docker/Python`
- [MyIP](https://ipcheck.ing) `⚠` - 全部在一个 IP 工具箱中。轻松检查您的 IP、IP 地理位置、检查 DNS 泄漏、检查 WebRTC 连接、速度测试、ping 测试、MTR 测试、检查网站可用性等。 ([演示](https://ipcheck.ing), [源代码](https://github.com/jason5ng32/MyIP)) `MIT` `Nodejs/Docker`
- [MySpeed](https://myspeed.dev/) - 速度测试分析软件可显示您长达 30 天的互联网速度。 ([源代码](https://github.com/gnmyt/myspeed)) `MIT` `Docker/Nodejs`
- [NetAlertX](https://netalertx.com/) - 网络入侵者和存在检测器。扫描连接到网络的设备，并在发现新设备和未知设备时向您发出警报。 ([源代码](https://github.com/netalertx/NetAlertX)) `GPL-3.0` `Docker`
- [Speed Test by OpenSpeedTest™](https://openspeedtest.com/) - 免费开源 HTML5 网络性能评估工具。 ([源代码](https://github.com/openspeedtest/Speed-Test)) `MIT` `Docker`
- [Speedtest Tracker](https://docs.speedtest-tracker.dev/) - 监控互联网连接的性能和正常运行时间。 ([源代码](https://github.com/alexjustesen/speedtest-tracker)) `MIT` `Docker/K8S`
- [Upsnap](https://github.com/seriousm4x/UpSnap) - 一个简单的 LAN 唤醒 (WOL) 仪表板应用程序。唤醒网络上的设备并查看当前状态。 `麻省理工学院``Go/Docker`
- [Wakupator](https://github.com/Gibus21250/Wakupator) - 基于网络流量的 LAN 唤醒机器管理器。 “麻省理工学院”“C”
- [WatchYourLAN](https://github.com/aceberg/WatchYourLAN) - 轻量级网络 IP 扫描器，具有通知、历史记录、导出到 Grafana。 `MIT` `Docker/Go/deb`


### 笔记和编辑

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

[笔记](https://en.wikipedia.org/wiki/Note-keeping) 编辑。

_相关：[维基百科](#wikis)_

- [Blinko](https://blinko.space/) - 具有AI功能的个人笔记工具。 ([源代码](https://github.com/blinkospace/blinko)) `AGPL-3.0` `Docker`
- [DailyTxT](https://github.com/PhiTux/DailyTxT) - 加密日记 Web 应用程序可保存您每天的个人记忆。包括搜索功能和加密文件上传。 ([演示](https://dailytxt.phitux.de)) `MIT` `Docker`
- [Docs](https://docs.numerique.gouv.fr/) - 可扩展的协作笔记、维基和文档平台。 ([源代码](https://github.com/suitenumerique/docs)) `MIT` `K8S`
- [draw.io](https://draw.io) - 用于制作流程图、流程图、组织结构图、UML、ER 和网络图的图表软件。 ([源代码](https://github.com/jgraph/drawio)) `Apache-2.0` `Javascript/Docker`
- [flatnotes](https://github.com/dullage/flatnotes) - 无数据库笔记 Web 应用程序，利用 Markdown 文件的平面文件夹进行存储。 ([演示](https://demo.flatnotes.io)) `MIT` `Docker`
- [HedgeDoc](https://hedgedoc.org/) - 所有平台上的实时协作 Markdown 笔记，以前称为 CodiMD 和 HackMD CE。 ([演示](https://demo.hedgedoc.org/), [源代码](https://github.com/hedgedoc/hedgedoc)) `AGPL-3.0` `Docker/Nodejs`
- [Joplin](https://joplinapp.org/) - 带有 Markdown 编辑器的笔记应用程序以及针对移动和桌面平台的加密支持。运行客户端并通过自托管 Nextcloud 实例或类似实例（Evernote 的替代方案）进行同步。 ([源代码](https://github.com/laurent22/joplin)) `MIT` `Nodejs`
- [Jotty](https://jotty.page) - 轻量级但功能强大的替代方案，用于管理您的个人、基于文件的笔记和清单。 ([源代码](https://github.com/fccview/jotty)) `AGPL-3.0` `Docker`
- [Livebook](https://livebook.dev) - 基于 Markdown 的实时协作笔记本应用程序，支持运行 Elixir 代码片段、TeX 和 Mermaid 图。使用 Docker 或 Elixir 轻松部署。 ([源代码](https://github.com/livebook-dev/livebook)) `Apache-2.0` `Elixir/Docker`
- [Many Notes](https://github.com/brufdev/many-notes) - Markdown 笔记 Web 应用程序，专为简单性而设计。 `麻省理工学院` `Docker`
- [Memos](https://usememos.com/) - 使用 SQLite 数据库文件的知识库。 ([演示](https://demo.usememos.com/explore), [源代码](https://github.com/usememos/memos)) `MIT` `Docker/Go`
- [Note Mark](https://notemark.docs.enchantedcode.co.uk/) - 最小的基于网络的 Markdown 笔记应用程序。 ([源代码](https://github.com/enchant97/note-mark)) `AGPL-3.0` `Docker`
- [Overleaf](https://www.overleaf.com/) - 基于 Web 的协作 LaTeX 编辑器。 ([源代码](https://github.com/overleaf/overleaf)) `AGPL-3.0` `Ruby`
- [Plainpad](https://alextselegidis.com/get/plainpad/) - 现代云笔记应用程序，利用渐进式网络应用程序技术的最佳功能。 ([演示](https://alextselegidis.com/try/plainpad/), [源代码](https://github.com/alextselegidis/plainpad)) `GPL-3.0` `PHP`
- [plumio](https://plumio.app/) - Markdown 笔记应用程序具有实时预览、文档加密、多用户支持、多组织功能等。 ([演示](https://demo.plumio.app/homepage), [源代码](https://github.com/albertasaftei/plumio)) `AGPL-3.0` `Nodejs/Docker`
- [SilverBullet](https://silverbullet.md/) - 为具有黑客心态的人优化的笔记应用程序。 ([演示](https://play.silverbullet.md/), [源代码](https://github.com/silverbulletmd/silverbullet), [客户端](https://silverbullet.md/Libraries)) `MIT` `Docker/Deno`
- [Standard Notes](https://docs.standardnotes.com/self-hosting/getting-started) - 简单且私人的笔记应用程序。保护您的隐私，同时完成更多工作。这就是标准注释。 ([演示](https://app.standardnotes.com/), [源代码](https://github.com/standardnotes/app)) `GPL-3.0` `Ruby`
- [TriliumNext Notes](https://github.com/TriliumNext/Trilium) - 跨平台分层笔记应用程序，专注于构建大型个人知识库（Trilium Notes 的分支）。 `AGPL-3.0` `Nodejs/Docker/K8S`
- [Turtl](https://turtl.it/) - 完全私人的个人数据库和笔记应用程序。 ([源代码](https://github.com/turtl)) `GPL-3.0` `CommonLisp`
- [Writing](https://josephernest.github.io/writing/) - 浏览器中的轻量级无干扰文本编辑器（支持 Markdown 和 LaTeX）。书写时不卡顿。 ([源代码](https://github.com/josephernest/writing)) `MIT` `Javascript`


### 办公套房

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

[办公套件](https://en.wikipedia.org/wiki/List_of_office_suites) 是生产力软件的集合，通常至少包含文字处理器、电子表格和演示程序。

- [Collabora Online Development Edition](https://www.collaboraoffice.com/code) - Collabora Online Development Edition (CODE) 是一款功能强大的基于 LibreOffice 的在线办公软件，支持所有主要文档、电子表格和演示文件格式，您可以将其集成到您自己的基础设施中。 ([源代码](https://cgit.freedesktop.org/libreoffice/online/)) `MPL-2.0` `C++`
- [CryptPad](https://cryptpad.org) - 协作套件旨在实现协作，实时同步文档更改。 ([源代码](https://github.com/cryptpad/cryptpad)) `AGPL-3.0` `Nodejs/Docker`
- [Digislides](https://ladigitale.dev/digislides/) - 以快速、简单的方式创建多媒体演示文稿。 （法语文档）。 ([演示](https://ladigitale.dev/digislides/), [源代码](https://codeberg.org/ladigitale/Digislides)) `AGPL-3.0` `Nodejs/PHP`
- [Etherpad](https://etherpad.org/) - 高度可定制的在线编辑器提供实时协作编辑。 ([演示](https://demo.sandstorm.io/appdemo/h37dm17aa89yrd8zuqpdn36p6zntumtv08fjpu8a8zrte7q1cn60), [源代码](https://github.com/ether/etherpad)) `Apache-2.0` `Nodejs/Docker`
- [Grist](https://getgrist.com/) - 下一代电子表格，具有关系结构、基于公式的访问控制和便携式独立格式（Airtable 的替代方案）。 ([演示](https://docs.getgrist.com), [源代码](https://github.com/gristlabs/grist-core)) `Apache-2.0` `Nodejs/Python/Docker`
- [ONLYOFFICE](https://helpcenter.onlyoffice.com/faq/server-opensource.aspx) - Office 套件使您能够在一个地方管理文档、项目、团队和客户关系。 ([源代码](https://github.com/ONLYOFFICE/DocumentServer)) `AGPL-3.0` `Nodejs/Docker`


### 密码管理器

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

[密码管理器](https://en.wikipedia.org/wiki/Password_manager) 允许用户存储、生成和管理本地应用程序和在线服务的密码。

- [AliasVault](https://www.aliasvault.net) - 具有内置电子邮件别名生成器和服务器的端到端加密密码管理器。 ([源代码](https://github.com/aliasvault/aliasvault)) `MIT` `Docker`
- [Bitwarden](https://bitwarden.com/) `⚠` - 带有网络应用程序、浏览器扩展程序和移动应用程序的密码管理器。 ([源代码](https://github.com/bitwarden/server)) `AGPL-3.0` `Docker/C#`
- [Passbolt](https://www.passbolt.com/) - 协作密码管理器。 ([源代码](https://github.com/passbolt/passbolt_api)) `AGPL-3.0` `PHP/deb/K8S/Docker`
- [PassIt](https://passit.io/) - 简单的密码管理，具有按组和用户共享的功能，但没有管理界面。 ([演示](https://app.passit.io/), [源代码](https://gitlab.com/passit)) `AGPL-3.0` `Docker/Python`
- [Psono](https://psono.com/) - 公司密码管理器。 ([演示](https://www.psono.pw), [源代码](https://gitlab.com/esaqa/psono/psono-fileserver)) `Apache-2.0` `Python`
- [Teampass](https://teampass.net/) - 专门用于以协作方式管理密码的密码管理器。一个对称密钥用于加密所有共享/团队密码并存储在文件和数据库中的服务器端。适用于任何 Apache、MySQL 和 PHP 服务器。 ([源代码](https://github.com/nilsteampassnet/TeamPass)) `GPL-3.0` `PHP`
- [Vaultwarden](https://github.com/dani-garcia/vaultwarden) - 用 Rust 编写的轻量级 Bitwarden 服务器 API 实现。 `GPL-3.0` `Rust/Docker`


### 巴斯德宾

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

[pastebin](https://en.wikipedia.org/wiki/Pastebin) 是一种在线内容托管服务，用于共享和存储代码和文本。

- [BinPastes](https://github.com/querwurzel/BinPastes) - 最小的 Pastebin，支持客户端加密、全文搜索、一次性消息。适用于寻求简单的 Pastebin 部署的一到少数用户。 `Apache-2.0` `Java`
- [ByteStash](https://github.com/jordan-dalby/ByteStash) - Pastebin 和文件存储服务具有简单的 Web 界面。支持语法高亮、可选的用户身份验证和公共共享。 ([演示](https://github.com/jordan-dalby/ByteStash?tab=readme-ov-file#demo)) `GPL-3.0` `Docker`
- [Chiyogami](https://github.com/rhee876527/chiyogami) - Pastebin 具有 API、客户端加密、用户帐户、语法突出显示、Markdown 渲染等。 ([演示](https://chiyogami.myaddr.dev/)) `BSD-3-Clause` `Docker`
- [dpaste](https://dpaste.org/) - 简单的 Pastebin，具有多个文本和代码选项，网址结果短，易于记忆。 ([源代码](https://github.com/DarrenOfficial/dpaste)) `MIT` `Docker/Python`
- [Hemmelig](https://hemmelig.app) - 跨组织或作为私人共享加密秘密。 ([源代码](https://github.com/HemmeligOrg/Hemmelig.app)) `MIT` `Docker/Nodejs`
- [lesma](https://lesma.eu) - 简单的粘贴应用程序与浏览器和命令行友好。 ([演示](https://lesma.eu), [源代码](https://gitlab.com/ogarcia/lesma)) `GPL-3.0` `Rust/Docker`
- [Local Content Share](https://github.com/Tanq16/local-content-share) - 在本地网络中存储和共享文本片段和文件。 `麻省理工学院` `Docker/Go`
- [not-th.re](https://not-th.re) - 简单的粘贴共享平台，具有客户端加密功能，具有基于摩纳哥浏览器的代码编辑器。 ([演示](https://not-th.re), [源代码](https://github.com/not- Three/main)) `AGPL-3.0` `Nodejs/Docker`
- [Opengist](https://opengist.io) - Pastebin 由 Git 提供支持。 ([演示](https://demo.opengist.io), [源代码](https://github.com/thomiceli/opengist)) `AGPL-3.0` `Docker/Go/Nodejs`
- [paaster](https://paaster.io) - 端到端加密的 Pastebin 是为了简单性而构建的。 ([源代码](https://github.com/WardPearce/paaster)) `AGPL-3.0` `Docker`
- [pacebin](https://git.crueter.xyz/crueter/pacebin) - 超最小的 Pastebin 和文件上传服务，专注于较小的可执行文件大小、可移植性和易于配置。 ([演示](https://paste.crueter.xyz)) `AGPL-3.0` `C`
- [Password Pusher](https://pwpush.com) - 用于通过网络安全地传递密码（或文本）的极其简单的应用程序。密码在经过一定数量的查看和/或时间后自动过期。 ([源代码](https://github.com/pgombardo/PasswordPusher)) `Apache-2.0` `Docker/K8S/Ruby`
- [Pastefy](https://pastefy.app/) - 美观、简单且易于部署 Pastebin，具有可选的客户端加密、多选项卡粘贴、API、突出显示的编辑器等。 ([源代码](https://github.com/interaapps/pastefy), [客户端](https://github.com/topics/pastefy-addon)) `MIT` `Docker/K8S/Java`
- [PrivateBin](https://privatebin.info/) - 极简主义的粘贴箱/讨论板，其中服务器对托管数据的了解为零。 ([演示](https://privatebin.net/), [源代码](https://github.com/PrivateBin/PrivateBin)) `Zlib` `PHP`
- [rustypaste](https://github.com/orhun/rustypaste) - 最少的文件上传/pastebin 服务。 “麻省理工学院”“铁锈”
- [SnyPy](https://snypy.com) - 开源本地代码片段管理器。 ([演示](https://app.snypy.com), [源代码](https://github.com/snypy)) `MIT` `Docker`
- [Sup3rS3cretMes5age](https://github.com/algolia/sup3rS3cretMes5age) - 使用 Hashicorp Vault 作为秘密存储的秘密消息服务非常简单（部署和使用）。 “麻省理工学院”“走吧”
- [Wastebin](https://github.com/matze/wastebin) - 具有 SQLite 后端的轻量级、最小化和快速的 Pastebin。 ([演示](https://bin.bloerg.net)) `MIT` `Rust/Docker`
- [Yopass](https://github.com/jhaals/yopass) - 安全共享秘密、密码和文件。 ([演示](https://yopass.se/)) `Apache-2.0` `Go/Docker`


### 个人仪表板

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

用于访问信息和应用程序的仪表板。

_相关：[监控和状态页面](#monitoring--status-pages)、[书签和链接共享](#bookmarks-and-link-sharing)_

- [Dashy](https://dashy.to/) - 为您的家庭实验室提供功能丰富的主页，并具有简单的 YAML 配置。 ([演示](https://demo.dashy.to/), [源代码](https://github.com/lissy93/dashy)) `MIT` `Nodejs/Docker`
- [Glance](https://github.com/glanceapp/glance) - 高度可定制的仪表板，将您的所有源放在一处。 `AGPL-3.0` `Docker/Go`
- [gobookmarks](https://github.com/arran4/gobookmarks) - 用于显示存储在 GitHub、GitLab 或本地 Git 中的书签的登陆页面。 `AGPL-3.0` `Go/Docker`
- [Heimdall](https://heimdall.site/) - 用于组织所有 Web 应用程序的优雅解决方案。 ([源代码](https://github.com/linuxserver/Heimdall)) `MIT` `PHP`
- [Hiccup](https://designedbyashw.in/test/hiccup/) - 漂亮的静态主页可快速访问您的链接和服务。它具有内置搜索、编辑、PWA 支持和本地存储缓存，可轻松组织您的起始页。 ([源代码](https://github.com/ashwin-pc/hiccup)) `MIT` `Javascript/Docker`
- [Homarr](https://homarr.dev) - 时尚、现代的仪表板，具有许多集成和基于 Web 的配置。 ([源代码](https://github.com/homarr-labs/homarr)) `MIT` `Docker/Nodejs`
- [Homepage by gethomepage](https://github.com/gethomepage/homepage) - 高度可定制的主页（或起始页/应用程序仪表板），具有 Docker 和服务 API 集成。 `GPL-3.0` `Docker/Nodejs`
- [Homepage by tomershvueli](https://github.com/tomershvueli/homepage) - 简单、独立、自托管的 PHP 页面是您通往服务器和网络的窗口。 `麻省理工学院``PHP`
- [Homer](https://github.com/bastienwirtz/homer) - 非常简单的静态主页，通过简单的 yaml 配置和连接检查来公开您的服务器服务。 ([演示](https://homer-demo.netlify.app)) `Apache-2.0` `Docker/K8S/Nodejs`
- [Hubleys](https://github.com/knrdl/hubleys-dashboard) - 个人仪表板可通过中央 yaml 配置为多个用户组织链接。 `麻省理工学院` `Docker`
- [LinkStack](https://linkstack.org/) - 在一页上轻松链接所有社交媒体平台，可通过直观、易于使用的用户/管理界面（Linktree 和 Manylink 的替代方案）进行自定义。 ([演示](https://linksta.cc/), [源代码](https://github.com/LinkStackOrg/LinkStack)) `AGPL-3.0` `PHP/Docker`
- [LittleLink](https://littlelink.io/) - 具有 100 多个品牌按钮的生物链接的简单方法（替代 Linktree）。 ([演示](https://littlelink.io/), [源代码](https://github.com/sethcottle/littlelink)) `MIT` `Javascript`
- [Mafl](https://mafl.hywax.space/) - 简约灵活的主页。 ([源代码](https://github.com/hywax/mafl)) `MIT` `Docker/Nodejs`
- [Nimbus](https://nimbus.turboot.com/) - 现代拖放式家庭实验室仪表板，具有可视化编辑器和简单的配置。 ([演示](https://nimbus.turboot.com/), [源代码](https://github.com/Turbootzz/Nimbus)) `AGPL-3.0` `Docker`
- [Personal Management System](https://volmarg.github.io/) - 整理日常生活的必需品，从简单的待办事项列表、笔记到付款和日程安排。 ([演示](https://github.com/Volmarg/personal-management-system#documentation--demo), [源代码](https://github.com/Volmarg/personal-management-system)) `MIT` `Docker`
- [portkey](https://portkey.page) - 简单的 Web 门户，用作启动页面，显示链接和 URL 的编译，同时还允许添加自定义页面，所有这些都通过单个配置文件进行管理。 ([演示](https://demo.portkey.page), [源代码](https://github.com/kodehat/portkey)) `AGPL-3.0` `Go/Docker`
- [ryot](https://github.com/ignisda/ryot) - 跟踪您生活的各个方面 - 媒体、健身等。（[演示](https://github.com/IgnisDa/ryot?tab=readme-ov-file#-demo)） `GPL-3.0` `Docker`
- [Starbase 80](https://github.com/notclickable-jordan/starbase-80) - 带有 iPad 风格应用程序网格的简单主页，适用于移动设备和桌面设备。一个 JSON 配置文件。 `麻省理工学院` `Docker`
- [您的 Spotify](https://github.com/Yooooomi/your_spotify) `⚠` - 允许您记录您的 Spotify 收听活动并通过 Web 应用程序获取有关它们的统计数据。 `MIT` `Nodejs/Docker`


### 照片画廊

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

[图库](https://en.wikipedia.org/wiki/Gallery_Software) 是帮助用户发布或共享照片、图片、视频或其他数字媒体的软件。

_相关：[静态站点生成器](#static-site-generators)、[媒体流 - 视频流](#media-streaming---video-streaming)、[内容管理系统 (CMS)](#content-management-systems-cms)_

- [Chevereto](https://chevereto.com/) - 终极图像共享软件。只需几分钟即可创建您自己的个人图像托管网站。 ([源代码](https://github.com/chevereto/chevereto)) `AGPL-3.0` `PHP/Docker`
- [ChronoFrame](https://chronoframe.bh8.ga/) - 具有在线照片管理功能的个人图库应用程序，支持实时/动态照片以及探索地图。 ([演示](https://lens.bh8.ga/), [源代码](https://github.com/HoshinoSuzumi/chronoframe)) `MIT` `Nodejs/Docker`
- [Damselfly](https://damselfly.info) - 基于服务器的快速照片管理系统，适用于大量图像。包括人脸检测、人脸和物体识别、强大的搜索以及 EXIF 关键字标记。可在 Linux、MacOS 和 Windows 上运行。 ([源代码](https://github.com/webreaper/damselfly)) `GPL-3.0` `Docker/C#/.NET`
- [Ente](https://ente.io/) - 端到端加密照片共享平台（替代 Google Photos、Apple Photos）。 ([源代码](https://github.com/ente-io/ente)) `AGPL-3.0` `Docker/Nodejs/Go`
- [HomeGallery](https://home-gallery.org) - 浏览带有标签、适合移动设备且由人工智能驱动的图像发现功能的个人照片和视频。 ([演示](https://demo.home-gallery.org), [源代码](https://github.com/xemle/home-gallery)) `MIT` `Nodejs/Docker`
- [Immich Kiosk](https://github.com/damongolding/immich-kiosk) - 用于在使用 Immich 作为数据源的信息亭设备和浏览器上运行的轻量级幻灯片。 `GPL-3.0` `Docker/Go`
- [Immich](https://immich.app/) - 直接从您的手机备份照片和视频的解决方案（替代 Google Photos）。 ([演示](https://github.com/immich-app/immich#demo), [源代码](https://github.com/immich-app/immich)) `AGPL-3.0` `Docker`
- [LibrePhotos](https://github.com/LibrePhotos/librephotos) - 照片管理服务，稍微关注酷图（替代 Google Photos）。 ([客户](https://docs.librephotos.com/docs/user-guide/mobile/)) `MIT` `Python/Docker`
- [Lychee](https://lycheeorg.github.io/) - 基于网格和相册的照片管理系统。 ([源代码](https://github.com/LycheeOrg/Lychee)) `MIT` `PHP/Docker`
- [Mediagoblin](https://mediagoblin.org) - 任何人都可以运行的媒体发布平台（替代 Flickr、YouTube、SoundCloud）。 ([源代码](https://git.savannah.gnu.org/cgit/mediagoblin.git/tree/)) `AGPL-3.0` `Python`
- [Memtly](https://docs.memtly.com/) - 活动照片共享平台和带有幻灯片的画廊，让客人可以通过二维码查看和分享回忆。 ([演示](https://demo.memtly.com/), [源代码](https://github.com/Memtly/Memtly.Community)) `GPL-3.0` `C#/Docker`
- [Nextcloud Memories](https://memories.gallery/) - 快速、现代且先进的照片管理套件。作为 Nextcloud 应用程序运行。 ([演示](https://demo.memories.gallery/apps/memories/), [源代码](https://github.com/pulsejet/memories)) `AGPL-3.0` `PHP`
- [Photofield](https://github.com/SmilyOrg/photofield) - 实验性快速照片查看器。 `麻省理工学院` `Docker/Go`
- [PhotoPrism](https://photoprism.org) - 由 Go 和 Google TensorFlow 提供支持的个人照片管理。  使用最新技术自动标记和查找图片，浏览、组织和共享您的个人照片集。 ([演示](https://demo.photoprism.app/library/browse), [源代码](https://github.com/photoprism/photoprism)) `AGPL-3.0` `Go/Docker`
- [Photoview](https://photoview.github.io/) - 适用于个人服务器的简单且用户友好的照片库。它是为摄影师设计的，旨在提供一种简单快捷的方式来浏览包含数千张高分辨率照片的目录。 ([演示](https://photoview.github.io/), [源代码](https://github.com/photoview/photoview)) `GPL-3.0` `Go/Docker`
- [PiGallery 2](https://bpatrik.github.io/pigallery2/) - 目录优先的照片库网站，具有丰富的 UI，针对在低资源服务器上运行进行了优化。 ([源代码](https://github.com/bpatrik/pigallery2)) `MIT` `Docker/Nodejs`
- [Piwigo](https://piwigo.org/) - 网络照片库软件，由活跃的用户和开发人员社区构建。 ([源代码](https://github.com/Piwigo/Piwigo)) `GPL-2.0` `PHP`
- [sigal](https://github.com/saimn/sigal) - 另一个简单的静态画廊生成器。 “麻省理工学院”“Python”
- [SPIS](https://github.com/gbbirkisson/spis) - 一个简单、轻量级、快速的媒体服务器，具有良好的移动支持。 `GPL-3.0` `Docker/Rust`
- [This week in past](https://github.com/RouHim/this-week-in-past) - 汇总本周拍摄的前几年的图像，并通过简单的幻灯片将它们呈现在网页上。 `麻省理工学院` `Docker/Rust`
- [Thumbor](http://thumbor.org/) - 智能成像服务，支持按需裁剪、调整大小、应用滤镜和优化图像。 ([源代码](https://github.com/thumbor/thumbor)) `MIT` `Python/Docker`
- [Zenphoto](https://www.zenphoto.org/) - 开源画廊和 CMS 项目。 ([源代码](https://github.com/zenphoto/zenphoto)) `GPL-2.0` `PHP`


### 民意调查和活动

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

用于组织[民意调查](https://en.wikipedia.org/wiki/Opinion_poll)和[活动](https://en.wikipedia.org/wiki/Event)的软件。

_相关：[预订和安排](#booking-and-scheduling)_

- [Bitpoll](https://github.com/fsinfuhh/Bitpoll) - 就日期、时间或一般问题进行民意调查。 ([演示](https://bitpoll.de/)) `GPL-3.0` `Docker/Python`
- [Bracket](https://docs.bracketapp.nl/) - 灵活的锦标赛系统，用于构建锦标赛设置、添加球队、安排比赛、跟踪比分并向公众实时展示排名。 ([演示](https://www.bracketapp.nl/demo), [源代码](https://github.com/evroon/bracket)) `AGPL-3.0` `Docker/Nodejs`
- [Christmas Community](https://github.com/Wingysam/Christmas-Community) - 创建一个简单的地方，供您的全家人用来寻找人们想要的礼物，并避免重复赠送礼物。 `AGPL-3.0` `Docker/Nodejs`
- [Claper](https://claper.co/) - 与观众互动的终极工具（Slido、AhaSlides 和 Mentimeter 的替代品）。 ([源代码](https://github.com/ClaperCo/Claper)) `GPL-3.0` `Elixir/Docker`
- [ClearFlask](https://clearflask.com) - 用于管理传入反馈并确定公共路线图优先级的社区反馈工具（替代 Canny、UserVoice、Upvoty）。 ([演示](https://product.clearflask.com), [源代码](https://github.com/clearflask/clearflask)) `AGPL-3.0` `Docker`
- [docassemble](https://docassemble.org/) - 一个免费的开源专家系统，用于指导访谈和文档组装，基于 Python、YAML 和 Markdown。 ([演示](https://demo.docassemble.org/run/legal), [源代码](https://github.com/jhpyle/docassemble)) `MIT` `Docker/Python`
- [Fider](https://fider.io) - 用于收集反馈并确定优先级的开放平台（替代 UserVoice）。 ([演示](https://demo.fider.io), [源代码](https://github.com/getfider/fider)) `MIT` `Docker`
- [Formbricks](https://formbricks.com) - 体验管理套件建立在全球最大的开源调查堆栈之上。在客户旅程的每一步都优雅地收集反馈，以了解客户的需求。 ([演示](https://app.formbricks.com), [源代码](https://github.com/formbricks/formbricks)) `AGPL-3.0` `Nodejs/Docker`
- [Framadate](https://framadate.org/abc/) - 用于快速轻松地计划约会或做出决定的在线服务：进行民意调查，定义要选择的日期或主题，将民意调查链接发送给您的朋友或同事，讨论并做出决定。 ([演示](https://framadate.org/aqg259dth55iuhwm), [源代码](https://framagit.org/framasoft/framadate?)) `CECILL-B` `PHP`
- [Gancio](https://gancio.org/) - 当地社区活动和议程共享。 ([演示](https://demo.gancio.org/), [源代码](https://framagit.org/les/gancio)) `AGPL-3.0` `Nodejs`
- [gathio](https://docs.gath.io/) - 自毁、可共享、无需注册的活动页面。 ([演示](https://gath.io/), [源代码](https://github.com/lowercasename/gathio)) `GPL-3.0` `Nodejs/Docker`
- [HeyForm](https://heyform.net) - 表单生成器，允许任何人为调查、问卷、测验和民意调查创建引人入胜的对话表单。 ([源代码](https://github.com/heyform/heyform)) `AGPL-3.0` `Docker`
- [hitobito](https://hitobito.com) - 管理复杂的群组层次结构，包括成员、活动等。 ([演示](https://demo.hitobito.com/en/users/sign_in), [源代码](https://github.com/hitobito/hitobito)) `AGPL-3.0` `Ruby`
- [LimeSurvey](https://www.limesurvey.org) - 功能丰富的基于网络的投票软件。支持广泛的调查逻辑。 ([演示](https://demo.limesurvey.org), [源代码](https://github.com/LimeSurvey/LimeSurvey)) `GPL-2.0` `PHP`
- [Meetable](https://events.indieweb.org) - 最小事件聚合器。 ([源代码](https://github.com/aaronpk/Meetable)) `MIT` `PHP`
- [Mobilizon](https://mobilizon.org) - 联合工具可帮助您查找、创建和组织活动和群组。 ([源代码](https://framagit.org/framasoft/mobilizon/)) `AGPL-3.0` `Elixir/Docker`
- [OpnForm](https://opnform.com) - 漂亮的开源表单生成器。 ([演示](https://opnform.com/forms/create/guest), [源代码](https://github.com/OpnForm/OpnForm)) `AGPL-3.0` `PHP/Nodejs/Docker`
- [Revel](https://www.letsrevel.io) `⚠` - 以社区为中心的活动管理和票务平台。 ([演示](https://demo.letsrevel.io), [源代码](https://github.com/letsrevel/revel-backend), [客户端](https://github.com/letsrevel)) `MIT` `Python/Docker`


### 代理

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

[代理](https://en.wikipedia.org/wiki/Proxy_server) 是一个服务器应用程序，充当请求资源的客户端和提供该资源的服务器之间的中介。本节介绍转发（即传出）代理。对于反向代理，请参阅 Web 服务器部分。

_相关：[网络服务器](#web-servers)_

- [g3proxy](https://g3-project.readthedocs.io/projects/g3proxy/en/latest/) - 转发代理服务器支持代理链接、协议检查、MITM 拦截、ICAP 适配和透明代理。 ([源代码](https://github.com/bytedance/g3/tree/master/g3proxy)) `Apache-2.0` `Rust/deb`
- [imgproxy](https://imgproxy.net/) - 快速、安全的独立服务器，用于调整远程图像的大小和转换。 ([源代码](https://github.com/imgproxy/imgproxy)) `MIT` `Go/Docker/K8S`
- [iodine](https://code.kryo.se/iodine/) - IPv4 over DNS 隧道解决方案，使您能够启动socks5 代理侦听器。 ([源代码](https://github.com/yarrick/iodine)) `ISC` `C/deb`
- [Outline Server](https://getoutline.org/) - 为每个访问密钥运行 Shadowsocks 实例的代理服务器以及用于管理访问密钥的 REST API。 ([源代码](https://github.com/OutlineFoundation/outline-server)) `Apache-2.0` `Docker/Nodejs`
- [Privoxy](https://www.privoxy.org) - 非缓存 Web 代理具有高级过滤功能，可增强隐私、修改网页数据和 HTTP 标头、控制访问以及删除广告和其他令人讨厌的互联网垃圾。 `GPL-2.0` `C/deb`
- [sish](https://github.com/antoniomika/sish) - 仅使用 SSH（serveo/ngrok 替代）到本地主机的 HTTP(S)/WS(S)/TCP 隧道。 `麻省理工学院``Go/Docker`
- [socks5-proxy-server](https://github.com/nskondratev/socks5-proxy-server) - SOCKS5 代理服务器具有内置身份验证和 Telegram-bot，用于用户管理和用户数据消耗统计（当您按 GB 数据付费时很方便）。它是码头化的并且安装简单。 `Apache-2.0` `Docker`
- [Squid](http://www.squid-cache.org/) - 支持 HTTP、HTTPS、FTP 等的 Web 缓存代理。它通过缓存和重用经常请求的网页来减少带宽并提高响应时间。 ([源代码](https://code.launchpad.net/squid)) `GPL-2.0` `C/deb`
- [Tinyproxy](https://tinyproxy.github.io/) - 轻量级 HTTP/HTTPS 代理守护进程。 ([源代码](https://github.com/tinyproxy/tinyproxy)) `GPL-2.0` `C/deb`


### 菜谱管理

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

用于管理[食谱]的软件和工具(https://en.wikipedia.org/wiki/Recipe)。

- [Bar Assistant](https://barassistant.app/) - 管理您的家庭酒吧，同时添加原料、搜索鸡尾酒和创建定制鸡尾酒配方。 ([演示](https://demo.barassistant.app/), [源代码](https://github.com/karlomikus/bar-assistant)) `MIT` `PHP/Docker`
- [CookCLI](https://cooklang.org) - 用于使用 Cooklang 食谱自动进行膳食计划和购物的命令行工具，可针对 UNIX 工作流程编写脚本，包括 Web 服务器。 ([源代码](https://github.com/cooklang/CookCLI)) `MIT` `Rust`
- [Fork Recipes](https://mikebgrep.github.io/forkapi/latest/clients/) - 轻松管理您的食物食谱。 ([源代码](https://github.com/mikebgrep/fork.recipes)) `BSD-3-Clause` `Docker`
- [ManageMeals](https://managemeals.com/) - 管理食谱、通过 URL 导入食谱并组织它们，没有任何广告或不必要的文本。 ([演示](https://demo.managemeals.com/), [源代码](https://github.com/managemeals/manage-meals-web)) `GPL-3.0` `Docker`
- [Mealie](https://nightly.mealie.io/) - 材料设计启发了食谱经理的类别和标签管理、购物清单、膳食计划和网站定制。 Mealie 专注于简单的用户交互，以确保全家人都使用该应用程序。 ([演示](https://demo.mealie.io), [源代码](https://github.com/mealie-recipes/mealie)) `MIT` `Python`
- [RecipeSage](https://github.com/julianpoy/recipesage) - 食谱管理器、膳食计划组织者和购物清单管理器，可以直接从任何 URL 导入食谱。 ([演示](https://recipesage.com)) `AGPL-3.0` `Nodejs`
- [Recipya](https://recipes.musicavis.ca) - 干净、简单且功能强大的食谱管理器，您的全家人都会喜欢。 ([演示](https://recipes.musicavis.ca/guide/login), [源代码](https://github.com/reaper47/recipya)) `GPL-3.0` `Docker/Go`
- [Specifically Clementines](https://davideshay.github.io/groceries/) - 杂货购物应用程序（以前称为 Groceries），提供与多个用户/设备（网络/Android/iOS）、食谱和与 Tandoor 集成的可靠同步。 ([源代码](https://github.com/davideshay/groceries)) `MIT` `Docker`
- [Tamari](https://tamariapp.com) - 食谱管理器 Web 应用程序，带有内置食谱集合。按收藏夹和类别进行组织、创建购物清单并计划膳食。 ([演示](https://app.tamariapp.com), [源代码](https://github.com/alexbates/Tamari)) `GPL-3.0` `Docker/Python`
- [Vanilla Cookbook](https://vanilla-cookbook.readthedocs.io/en/) - 菜谱管理器的设计具有复杂性，尽可能保持用户体验整洁、简单。 ([源代码](https://github.com/jt196/vanilla-cookbook)) `GPL-3.0` `Docker/Nodejs`
- [What To Cook?](https://github.com/kassner/whattocook) - 根据您家里现有的食材，获取今天的烹饪食谱。 `AGPL-3.0` `Docker`


### 远程访问

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

[远程桌面](https://en.wikipedia.org/wiki/Remote_desktop_software) 和 [SSH](https://en.wikipedia.org/wiki/Secure_Shell) 服务器和 Web 界面，用于远程管理计算机系统。

- [Cardea](https://github.com/hectorm/cardea) - SSH 堡垒服务器，具有访问控制、会话记录和可选的 TPM 支持的密钥保护。 `EUPL-1.2` `Go/Docker`
- [Engity's Bifröst](https://bifroest.engity.org/) - 高度可定制的 SSH 服务器，具有多种授权用户的方法以及执行用户会话的位置和方式的选项。 ([源代码](https://github.com/engity-com/bifroest)) `Apache-2.0` `Go/Docker`
- [Firezone](https://www.firezone.dev/) - 支持 WireGuard 协议的安全远程访问网关。它提供 Web GUI、1 行安装脚本、多重身份验证 (MFA) 和 SSO。 ([源代码](https://github.com/firezone/firezone)) `Apache-2.0` `Elixir/Docker`
- [Guacamole](https://guacamole.apache.org) - 无客户端远程桌面网关支持 VNC 和 RDP 等标准协议。 ([源代码](https://github.com/apache/guacamole-server)) `Apache-2.0` `Java/C`
- [MeshCentral](https://meshcentral.com/) - 运行您自己的 Web 服务器来远程管理和控制本地网络或互联网上任何位置的计算机。 ([源代码](https://github.com/Ylianst/MeshCentral)) `Apache-2.0` `Nodejs`
- [ShellHub](https://www.shellhub.io) - 现代 SSH 服务器，用于通过命令行（使用任何 SSH 客户端）或基于 Web 的用户界面（替代 sshd）远程访问 Linux 设备。 ([源代码](https://github.com/shellhub-io/shellhub)) `Apache-2.0` `Docker`
- [Sshwifty](https://github.com/nirui/sshwifty) - Sshwifty 是专为 Web 设计的 SSH 和 Telnet 连接器。 ([演示](https://sshwifty-demo.nirui.org)) `AGPL-3.0` `Go/Docker`
- [Termix](https://docs.termix.site/) - 基于 Web 的无客户端服务器管理平台，具有 SSH 终端、隧道和文件编辑功能。 ([源代码](https://github.com/Termix-SSH/Termix)) `Apache-2.0` `Docker`
- [Warpgate](https://github.com/warp-tech/warpgate) - 智能 SSH 和 HTTPS 堡垒，可与任何 SSH 客户端配合使用。 `Apache-2.0` `Rust/Docker`


### 资源规划

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

帮助进行[资源和供应规划](https://en.wikipedia.org/wiki/Resource_planning)的软件和工具，包括[企业资源和供应规划(ERP)](https://en.wikipedia.org/wiki/Enterprise_resource_planning)。

_相关：[金钱、预算和管理](#money-budgeting--management)、[库存管理](#inventory-management)_

- [Dolibarr](https://www.dolibarr.org/) - 现代 CRM 软件包用于管理您的公司或基金会活动（联系人、供应商、发票、订单、库存、议程、会计等）。 ([演示](https://www.dolibarr.org/onlinedemo.php), [源代码](https://github.com/Dolibarr/dolibarr)) `GPL-3.0` `PHP/deb`
- [ERPNext](https://frappe.io/erpnext) - ERP 系统可帮助您运营业务。 ([源代码](https://github.com/frappe/erpnext)) `GPL-3.0` `Python/Docker`
- [farmOS](https://farmos.org/) - 基于网络的农场记录保存应用程序。 ([演示](https://farmos-demo.rootedsolutions.io/), [源代码](https://github.com/farmOS/farmOS)) `GPL-2.0` `PHP/Docker`
- [grocy](https://grocy.info/) - ERP 超越您的冰箱。适合您家庭的杂货和家庭管理解决方案。 ([演示](https://en.demo.grocy.info/), [源代码](https://github.com/grocy/grocy)) `MIT` `PHP/Docker`
- [LedgerSMB](https://ledgersmb.org/) - 适用于中小型企业的集成会计和 ERP 系统，具有复式记账、预算、发票、报价、项目、订单和库存管理、运输等功能。 ([源代码](https://github.com/ledgersmb/LedgerSMB)) `GPL-2.0` `Docker/Perl`
- [Odoo](https://www.odoo.com) - 免费开源 ERP 系统。 ([演示](https://demo.odoo.com/), [源代码](https://github.com/odoo/odoo)) `LGPL-3.0` `Python/deb/Docker`
- [OFBiz](https://ofbiz.apache.org/) - 企业资源规划系统具有一套足够灵活的业务应用程序，可以在任何行业中使用。 ([源代码](https://github.com/apache/ofbiz-framework)) `Apache-2.0` `Java`
- [Tryton](https://www.tryton.org/) - 免费的开源业务解决方案。 ([演示](https://www.tryton.org/demo), [源代码](https://foss.heptapod.net/tryton/tryton)) `GPL-3.0` `Python`


### 搜索引擎

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

[搜索引擎](https://en.wikipedia.org/wiki/Search_engine_(computing))是一个[信息检索系统](https://en.wikipedia.org/wiki/Information_retrieval)，旨在帮助查找存储在计算机系统上的信息。这包括[网络搜索引擎](https://en.wikipedia.org/wiki/Web_search_engine)。

- [Aleph](https://aleph.occrp.org/) - 用于索引大量文档（PDF、Word、HTML）和结构化（CSV、XLS、SQL）数据的工具，以便于浏览和搜索。它以调查报告为主要用例构建。 ([演示](https://aleph.occrp.org/), [源代码](https://github.com/alephdata/aleph)) `MIT` `Docker/K8S`
- [Apache Solr](https://lucene.apache.org/solr/) - 企业搜索平台，具有全文搜索、命中突出显示、分面搜索、实时索引、动态集群和丰富文档（例如 Word、PDF）处理。 ([源代码](https://github.com/apache/solr)) `Apache-2.0` `Java/Docker/K8S`
- [Fess](https://fess.codelibs.org/) - 功能强大且易于部署的企业搜索服务器。 ([演示](https://search.n2sm.co.jp/), [源代码](https://github.com/codelibs/fess)) `Apache-2.0` `Java/Docker`
- [Hister](https://hister.org/) - 个人网络搜索引擎，可自动为访问过的网站编制索引。支持离线本地结果预览、本地文件、多用户处理和可选的语义搜索。 ([演示](https://demo.hister.org/), [源代码](https://github.com/asciimoo/hister)) `AGPL-3.0` `Go/Docker`
- [Manticore Search](https://github.com/manticoresoftware/manticoresearch/) - 全文搜索和数据分析，对小、中、大数据具有快速响应时间（替代 Elasticsearch）。 `GPL-3.0` `Docker/deb/C++/K8S`
- [MeiliSearch](https://www.meilisearch.com) - 超相关、即时且容错的全文搜索 API。 ([源代码](https://github.com/meilisearch/MeiliSearch)) `MIT` `Rust/Docker/deb`
- [Meme Search](https://github.com/neonwatty/meme-search) - 人工智能驱动的模因搜索引擎。使用视觉语言模型自动从图像中提取描述，然后使用向量嵌入进行索引以进行语义和关键字搜索。 `Apache-2.0` `Docker`
- [OpenSearch](https://opensearch.org) - 分布式 RESTful 搜索引擎。 ([源代码](https://github.com/opensearch-project/OpenSearch)) `Apache-2.0` `Java/Docker/K8S/deb`
- [SearXNG](https://docs.searxng.org/) `⚠` - 互联网元搜索引擎，聚合来自各种搜索服务和数据库的结果（Searx 的分支）。 ([源代码](https://github.com/searxng/searxng/)) `AGPL-3.0` `Python/Docker`
- [sist2](https://github.com/sist2app/sist2) - 快如闪电的文件系统索引器和搜索工具。 `GPL-3.0` `C/Docker`
- [Sosse](https://sosse.readthedocs.io/en/stable/) - 基于 Selenium 的搜索引擎和爬虫，具有离线归档功能。 ([源代码](https://gitlab.com/biolds1/sosse)) `AGPL-3.0` `Python/Docker`
- [Typesense](https://typesense.org) - 速度极快、容错的开源搜索引擎针对开发人员的快乐和易用性进行了优化。 ([源代码](https://github.com/typesense/typesense)) `GPL-3.0` `C++/Docker/K8S/deb`
- [Websurfx](https://github.com/neon-mmd/websurfx) `⚠` - 聚合来自其他搜索引擎（元搜索引擎）的结果，不含广告，同时牢记隐私和安全。它速度极快，并提供高水平的定制（SearX 的替代方案）。 `AGPL-3.0` `Rust/Docker`
- [Yacy](https://yacy.net/en/index.html) - 基于对等的分散式搜索引擎服务器。 ([源代码](https://github.com/yacy/yacy_search_server)) `GPL-2.0` `Java/Docker/K8S`
- [ZincSearch](https://zincsearch.com) - 需要最少资源的搜索引擎（Elasticsearch 的替代方案）。 ([演示](https://github.com/zinclabs/zinc#playground-server), [源代码](https://github.com/zincsearch/zincsearch)) `Apache-2.0` `Go/Docker/K8S`


### 自托管解决方案

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

用于轻松安装、管理和配置自托管服务和应用程序的软件。

- [CasaOS](https://casaos.zimaspace.com/) - 简单、易用、优雅的家庭云系统。 ([源代码](https://github.com/IceWhaleTech/CasaOS)) `Apache-2.0` `Go/Docker`
- [DietPi](https://dietpi.com/) - 针对单板计算机优化的最小 Debian 操作系统，使您可以轻松安装和管理多种在家自托管的服务。 ([源代码](https://github.com/MichaIng/DietPi)) `GPL-2.0` `Shell`
- [DockSTARTer](https://dockstarter.com/) - DockSTARTer 可帮助您开始使用在 Docker 中运行的家庭服务器应用程序。 ([源代码](https://github.com/GhostWriters/DockSTARTer)) `MIT` `Shell`
- [Dropserver](https://dropserver.org) - 个人网络服务的应用程序平台。 ([源代码](https://github.com/teleclimber/Dropserver/)) `Apache-2.0` `Go/Deno`
- [FreedomBox](https://freedombox.org/) - 社区项目开发、设计和推广运行免费软件的个人服务器，用于私人、个人通信。 ([源代码](https://salsa.debian.org/freedombox-team/freedombox)) `AGPL-3.0` `Python/deb`
- [HomelabOS](https://homelabos.com) - 以隐私为中心的离线数据中心。使用几个命令即可部署 100 多个服务。 ([源代码](https://gitlab.com/NickBusey/HomelabOS)) `MIT` `Docker`
- [HomeServerHQ](https://www.homeserverhq.com/) - 一体化家庭服务器基础设施和安装程序。在不到一个小时的时间内就可以建立完全配置的电子邮件服务器、VPN 和公共网站，甚至在 CGNAT 后面。 ([源代码](https://github.com/homeserverhq/hshq)) `GPL-3.0` `Shell`
- [LibreServer](https://libreserver.org/) - 基于Debian的家庭服务器配置。 ([源代码](https://github.com/bashrc2/libreserver)) `AGPL-3.0` `Shell`
- [NextCloudPi](https://github.com/nextcloud/nextcloudpi) - Nextcloud 已预安装和预配置，具有文本和 Web 管理界面以及自行托管私有数据所需的所有工具。包含 Raspberry Pi、Odroid、Rock64、Docker 的安装映像以及 Armbian/Debian 的curl 安装程序。 `GPL-2.0` `Shell/PHP`
- [Nirvati](https://nirvati.org) - 通过便捷的 Web 界面，一键轻松启动流行的自托管应用程序。 ([源代码](https://gitlab.com/nirvati-ug/nirvati/backend)) `AGPL-3.0` `Rust/K8S`
- [OpenMediaVault](https://www.openmediavault.org/) - 基于 Debian Linux 的网络附加存储 (NAS) 解决方案。它包含 SSH、(S)FTP、SMB/CIFS、DAAP 媒体服务器、RSync、BitTorrent 客户端等服务。 ([源代码](https://github.com/openmediavault/openmediavault)) `GPL-3.0` `PHP`
- [Sandstorm](https://sandstorm.io/) - 用于轻松安全地运行自托管应用程序的个人服务器。 ([演示](https://demo.sandstorm.io/), [源代码](https://github.com/sandstorm-io/sandstorm)) `Apache-2.0` `C++/Shell`
- [Self Host Blocks](https://github.com/ibizaman/selfhostblocks) `⚠` - 基于 NixOS 模块并专注于最佳实践的模块化服务器管理。 `AGPL-3.0` `尼克斯`
- [StartOS](https://start9.com) - 基于浏览器的图形操作系统 (OS)，使运行个人服务器像运行个人计算机一样简单。 ([源代码](https://github.com/Start9Labs/start-os)) `MIT` `Rust`
- [Syncloud](https://syncloud.org/) - 您自己的在线文件存储、社交网络或电子邮件服务器。 ([源代码](https://github.com/syncloud/platform)) `GPL-3.0` `Go/Shell`
- [Tipi](https://runtipi.io/) - 家庭服务器经理。一键设置，一键安装您最喜爱的自托管应用程序。 ([源代码](https://github.com/runtipi/runtipi)) `GPL-3.0` `Shell`
- [UBOS](https://ubos.net/) - 在独立设备（个人服务器和物联网设备）上运行的 Linux 发行版。单命令安装和管理应用程序 - Jenkins、Mediawiki、Owncloud、WordPress 等以及其他功能。 `GPL-3.0` `Perl`
- [Websoft9](https://www.websoft9.com) `⚠` - GitOps 驱动的云服务器和家庭服务器多应用程序托管，一键部署 200 多个开源应用程序。 ([演示](https://www.websoft9.com/demo), [源代码](https://github.com/websoft9/websoft9), [客户端](https://www.websoft9.com/apps)) `LGPL-3.0` `Shell/Python`
- [WikiSuite](https://wikisuite.org) - 最全面、集成的免费/自由/开源企业软件套件。 ([源代码](https://wikisuite.org/Source-Code)) `GPL-3.0/LGPL-2.1/Apache-2.0/MPL-2.0/MPL-1.1/MIT/AGPL-3.0` `Shell/Perl/deb`
- [xsrv](https://xsrv.readthedocs.io/) - 在您自己的服务器上安装和管理自托管服务/应用程序。 ([源代码](https://github.com/nodiscc/xsrv)) `GPL-3.0` `Ansible/Shell`
- [YunoHost](https://yunohost.org/) - 服务器操作系统旨在让每个人都可以使用自托管。 ([演示](https://yunohost.org/#/try), [源代码](https://github.com/YunoHost)) `AGPL-3.0` `Python/Shell`


### 软件开发

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

[软件开发](https://en.wikipedia.org/wiki/Software_development) 是涉及创建和维护应用程序、框架或其他软件组件的构思、指定、设计、编程、记录、测试和错误修复的过程。

**请访问[软件开发-API管理](#software-development---api-management)、[软件开发-持续集成和部署](#software-development---持续集成--deployment)、[软件开发-FaaS和Serverless](#software-development---faas--serverless)、[软件开发-IDE和工具](#software-development---ide--tools)、[软件开发-本地化](#software-development---localization)、[软件开发 - 低代码](#software-development---low-code)、[软件开发 - 项目管理](#software-development---project-management)、[软件开发 - 测试](#software-development---testing)、[软件开发 - 功能切换](#software-development---feature-toggle)**



### 软件开发-API管理

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

[API 管理](https://en.wikipedia.org/wiki/API_management) 是创建和发布[应用程序编程接口 (API)](https://en.wikipedia.org/wiki/API)、执行其使用策略、控制访问、培育订阅者社区、收集和分析使用统计数据以及报告性能的过程。

- [Aastro](https://starwalkn.github.io/aastro-docs) - 用 Go 编写的可扩展 API 网关。 ([源代码](https://github.com/starwalkn/aastro)) `Apache-2.0` `Go/Docker`
- [DreamFactory](https://www.dreamfactory.com/) - 将任何 SQL/NoSQL/结构化数据转换为 Restful API。 ([源代码](https://github.com/dreamfactorysoftware/dreamfactory)) `Apache-2.0` `PHP/Docker/K8S`
- [form.io](https://form.io) - 一个 REST API 构建平台，利用拖放表单构建器，并且与应用程序框架无关。包含开源版和企业版。 ([演示](https://portal.form.io), [源代码](https://github.com/formio)) `MIT` `Nodejs/Docker`
- [Fusio](https://www.fusio-project.org/) - 开源 API 管理平台，有助于构建和管理 REST API。 ([演示](https://fusio-project.org/demo), [源代码](https://github.com/apioo/fusio)) `AGPL-3.0` `PHP/Docker`
- [Graphweaver](https://graphweaver.com/) - 将多个数据源转换为单个 GraphQL API。 ([源代码](https://github.com/exogee-technology/graphweaver)) `MIT` `Nodejs`
- [Hasura](https://hasura.io) - Postgres 上快速、即时的实时 GraphQL API 具有细粒度的访问控制，还可触发数据库事件的 Webhooks。 ([源代码](https://github.com/hasura/graphql-engine)) `Apache-2.0` `Haskell/Docker/K8S`
- [Hoppscotch Community Edition](https://hoppscotch.io) - 快速且美观的 API 请求生成器。 ([源代码](https://github.com/hoppscotch/hoppscotch)) `MIT` `Nodejs/Docker`
- [Kong](https://konghq.com/kong/) - 微服务API网关和平台。 ([源代码](https://github.com/Kong/kong)) `Apache-2.0` `Lua/Docker/K8S/deb`
- [Lura](https://luraproject.org/) - 高性能API网关。 ([源代码](https://github.com/luraproject/lura)) `Apache-2.0` `Go`
- [Opik](https://www.comet.com/site/products/opik/) `⚠` - 使用一套可观察性工具评估、测试和交付 LLM 应用程序，以在整个开发和生产生命周期中校准语言模型输出。 ([源代码](https://github.com/comet-ml/opik)) `Apache-2.0` `Docker/Python`
- [Para](https://paraio.org) - 用于对象持久化、API 开发和身份验证的灵活且模块化的后端框架/服务器。 ([源代码](https://github.com/erudika/para)) `Apache-2.0` `Java/Docker`
- [Svix](https://svix.com) - 开源 Webhooks 作为一项服务，使 API 提供商可以非常轻松地发送 Webhooks。 ([源代码](https://github.com/svix/svix-webhooks)) `MIT` `Docker/Rust`
- [Tyk](https://tyk.io) - 快速且可扩展的开源 API 网关。 Tyk 提供开箱即用的 API 管理平台，其中包含 API 网关、API 分析、开发人员门户和 API 管理仪表板。 ([源代码](https://github.com/TykTechnologies/tyk)) `MPL-2.0` `Go/Docker/K8S`


### 软件开发 - 持续集成和部署

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

[持续集成](https://en.wikipedia.org/wiki/Continously_integration)和[持续部署](https://en.wikipedia.org/wiki/Continously_deployment)软件和工具。

**请访问[awesome-sysadmin/持续集成和持续部署](https://github.com/awesome-foss/awesome-sysadmin#continuous-integration--continuous-deployment)**

_相关：[自动化](#automation)_



### 软件开发 - FaaS 和无服务器

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

[无服务器计算](https://en.wikipedia.org/wiki/Serverless_computing)、[函数即服务(FaaS)](https://en.wikipedia.org/wiki/Function_as_a_service)和[平台即服务(Paas)](https://en.wikipedia.org/wiki/Platform_as_a_service)管理软件。

**请访问[awesome-sysadmin/PaaS](https://github.com/awesome-foss/awesome-sysadmin#paas)**



### 软件开发 - 功能切换

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

软件开发中的[功能切换](https://en.wikipedia.org/wiki/Feature_toggle)提供了在源代码中维护多个功能分支的替代方法。

_相关：[软件开发-IDE和工具](#software-development---ide--tools)_

- [Featbit](https://www.featbit.co/) - 您可以自行托管的企业级功能标志平台。 ([源代码](https://github.com/featbit/featbit)) `MIT` `Docker/K8S`
- [Flagsmith](https://flagsmith.com) - 用于向应用程序添加功能标志的仪表板、API 和 SDK（替代 LaunchDarkly）。 ([源代码](https://github.com/flagsmith/flagsmith)) `BSD-3-Clause` `Docker/K8S`
- [Flipt](https://flipt.io) - 支持多个数据后端的功能标志解决方案（替代 LaunchDarkly）。 ([源代码](https://github.com/flipt-io/flipt)) `GPL-3.0` `Docker/K8S/Go`
- [GO Feature Flag](https://gofeatureflag.org) - 简单、完整、轻量级的功能标志解决方案（LaunchDarkly 的替代方案）。 ([源代码](https://github.com/thomaspoignant/go-feature-flag)) `MIT` `Go`


### 软件开发 - IDE 和工具

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

[集成开发环境 (IDE)](https://en.wikipedia.org/wiki/Integrated_development_environment) 是一种软件应用程序，为计算机程序员提供全面的软件开发工具。

_相关：[软件开发-低代码](#software-development---low-code)_

- [Atheos](https://www.atheos.io) - 基于 Web 的 IDE 框架，占用空间小，要求最低，继承自 Codiad。 ([源代码](https://github.com/Atheos/Atheos)) `MIT` `PHP/Docker`
- [code-server](https://github.com/coder/code-server) - 浏览器中的 VS Code 托管在远程服务器上。 `MIT` `Nodejs/Docker`
- [Coder](https://coder.com/) - 您自己的基础设施上的远程开发机器。 ([源代码](https://github.com/coder/coder)) `AGPL-3.0` `Go/Docker/K8S/deb`
- [Eclipse Che](https://www.eclipse.org/che/) - 开源工作区服务器和云 IDE。 ([源代码](https://github.com/eclipse-che/che)) `EPL-1.0` `Docker/Java`
- [Judge0 CE](https://judge0.com) - 用于编译和运行源代码的API。 ([源代码](https://github.com/judge0/judge0)) `GPL-3.0` `Docker`
- [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/) - 基于网络的交互式和可重复计算环境。 ([演示](https://mybinder.org/v2/gh/jupyterlab/jupyterlab-demo/try.jupyter.org?urlpath=lab), [源代码](https://github.com/jupyterlab/jupyterlab/)) `BSD-3-Clause` `Python/Docker`
- [Langfuse](https://langfuse.com) - 用于模型追踪、提示管理和应用评估的LLM工程平台。 Langfuse 帮助团队协作调试、分析和迭代其 LLM 应用程序（例如聊天机器人或 AI 代理）。 ([演示](https://langfuse.com/docs/demo), [源代码](https://github.com/langfuse/langfuse), [客户端](https://langfuse.com/docs/integrations/overview)) `MIT` `Docker`
- [LiveCodes](https://livecodes.io/docs/features/self-hosting) `⚠` - 功能丰富的客户端代码游乐场，适用于 React、Vue、Svelte、Solid、Typescript、Python、Go、Ruby、PHP 和 90 多种其他语言。 ([演示](https://livecodes.io), [源代码](https://github.com/live-codes/livecodes)) `MIT` `Nodejs`
- [Lowdefy](https://www.lowdefy.com/) - 在自托管的开源平台上使用 YAML / JSON 在几分钟内构建内部工具、BI 仪表板、管理面板、CRUD 应用程序和工作流程。连接到您的数据源，通过 Serverless、Netlify 或 Docker 进行托管。 ([源代码](https://github.com/lowdefy/lowdefy)) `Apache-2.0` `Nodejs/Docker`
- [RapidForge](https://rapidforge.io/) - 用于构建网络钩子、计划任务和页面的轻量级平台。使用 Bash 或 Lua 实现您的逻辑。 ([源代码](https://github.com/rapidforge-io/rapidforge)) `Apache-2.0` `Go/Nodejs`
- [RStudio Server](https://www.rstudio.com/products/rstudio/#Server) - 基于 Web 浏览器的 R IDE。（[源代码](https://github.com/rstudio/rstudio)） `AGPL-3.0` `Java/C++`


### 软件开发 - 本地化

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

[本地化](https://en.wikipedia.org/wiki/Internationalization_and_localization) 是将代码和软件改编为其他语言的过程。

- [Accent](https://www.accent.reviews/) - 面向开发人员的翻译工具。 ([源代码](https://github.com/mirego/accent)) `BSD-3-Clause` `Elixir/Docker`
- [Tolgee](https://tolgee.io) - 开发人员和翻译人员友好的基于网络的本地化平台使用户可以直接在他们开发的应用程序中进行翻译。 ([源代码](https://github.com/tolgee/tolgee-platform)) `Apache-2.0` `Docker/Java`
- [Traduora](https://traduora.co) - 团队翻译管理平台。 ([源代码](https://github.com/ever-co/ever-traduora)) `AGPL-3.0` `Docker/K8S/Nodejs`
- [Weblate](https://weblate.org) - 基于网络的翻译工具，具有紧密的版本控制集成。 ([源代码](https://github.com/WeblateOrg/weblate)) `GPL-3.0` `Python/Docker/K8S`


### 软件开发 - 低代码

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

[低代码](https://en.wikipedia.org/wiki/Low-code_development_platform)开发平台(LCDP)提供了用于通过图形用户界面创建应用程序软件的开发环境。

_相关：[软件开发-IDE和工具](#software-development---ide--tools)_

- [Appsmith](https://www.appsmith.com/) - 构建管理面板、CRUD 应用程序和工作流程。构建您需要的一切，速度提高 10 倍。 ([源代码](https://github.com/appsmithorg/appsmith)) `Apache-2.0` `Java/Docker/K8S`
- [Appwrite](https://appwrite.io) - 面向 Web、本机和移动开发人员的端到端后端服务器🚀。 ([源代码](https://github.com/appwrite/appwrite)) `BSD-3-Clause` `Docker`
- [autokitteh](https://autokitteh.com/) - 只需几行代码即可实现持久的工作流程自动化。 ([源代码](https://github.com/autokitteh/autokitteh)) `Apache-2.0` `Go/Docker`
- [Halo](https://www.halo.run) - 一款功能强大且易于使用的网站建设工具（中文文档）。 ([演示](https://docs.halo.run/#%E5%9C%A8%E7%BA%BF%E4%BD%93%E9%AA%8C), [源代码](https://github.com/halo-dev/halo), [客户端](https://github.com/halo-sigs/awesome-halo)) `GPL-3.0` `Java/Docker`
- [Manifest](https://manifest.build) - 适合 1 个 YAML 文件的完整后端。 ([演示](https://manifest.new), [源代码](https://github.com/mnfst/manifest)) `MIT` `Nodejs`
- [PocketBase](https://pocketbase.io/) - 一个文件中的下一个 SaaS 和移动应用程序的后端。 ([源代码](https://github.com/pocketbase/pocketbase)) `MIT` `Go/Docker`
- [Saltcorn](https://saltcorn.com/) - 适用于 Web 和移动应用程序的无代码数据库应用程序构建器。一个用于用户界面、数据后端、持久工作流程、电子邮件、PDF 生成和人工智能应用程序的平台。 ([源代码](https://github.com/saltcorn/saltcorn)) `MIT` `Docker/Nodejs`
- [SQLPage](https://sql-page.com) - 仅 SQL 动态网站构建器。 ([源代码](https://github.com/sqlpage/SQLPage)) `MIT` `Rust/Docker`
- [ToolJet](https://tooljet.io/) - 低代码框架，用于以最少的工程工作量构建和部署内部工具（Retool 和 Mendix 的替代方案）。 ([源代码](https://github.com/ToolJet/ToolJet)) `GPL-3.0` `Nodejs/Docker/K8S`
- [TrailBase](https://trailbase.io/) - 开放式、亚毫秒级、单一可执行的 FireBase 替代方案，具有类型安全的 REST 和实时 API、内置 JS/TS 运行时、身份验证和管理 UI。 ([演示](https://demo.trailbase.io), [源代码](https://github.com/trailbaseio/trailbase)) `OSL-3.0` `Rust/Docker`


### 软件开发-项目管理

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

用于[软件项目管理]的工具和软件(https://en.wikipedia.org/wiki/Software_project_management)。

_相关：[工单](#ticketing)、[任务管理和待办事项列表](#task-management--to-do-lists)_

- [Cgit](https://git.zx2c4.com/cgit/about/) - 用于 git 存储库的快速轻量级 Web 界面。 ([源代码](https://git.zx2c4.com/cgit/tree/)) `GPL-2.0` `C`
- [Forgejo](https://forgejo.org) - 专注于扩展、联合和隐私的轻量级软件锻造（Gitea 的分支）。 ([演示](https://next.forgejo.org), [源代码](https://codeberg.org/forgejo/forgejo/), [客户端](https://codeberg.org/forgejo-contrib/delightful-forgejo)) `MIT` `Docker/Go`
- [Fossil](https://www.fossil-scm.org/index.html/doc/trunk/www/index.wiki) - 具有 wiki 和错误跟踪器的分布式版本控制系统。 `BSD-2-子句-FreeBSD` `C`
- [Gerrit](https://www.gerritcodereview.com/) - 适用于基于 Git 的项目的代码审查和项目管理工具。 ([源代码](https://github.com/GerritCodeReview/gerrit)) `Apache-2.0` `Java/Docker`
- [gitbucket](https://gitbucket.github.io/) - Git 平台具有易于安装、高可扩展性和 GitHub API 兼容性（替代 GitHub）。 ([源代码](https://github.com/gitbucket/gitbucket)) `Apache-2.0` `Scala/Java`
- [Gitea](https://gitea.com) - 喝杯茶吧！无痛自托管一体化软件开发服务，包括 Git 托管、代码审查、团队协作、包注册和 CI/CD。 ([演示](https://demo.gitea.com), [源代码](https://github.com/go-gitea/gitea)) `MIT` `Go/Docker/K8S`
- [GitLab](https://about.gitlab.com) - 自托管 Git 存储库管理、代码审查、问题跟踪、活动源和 wiki。 ([演示](https://gitlab.com/), [源代码](https://gitlab.com/gitlab-org/gitlab-foss)) `MIT` `Ruby/deb/Docker/K8S`
- [Gogs](https://gogs.io/) - 用 Go 编写的无痛自托管 Git 服务。 ([源代码](https://github.com/gogs/gogs)) `MIT` `Go`
- [Huly](https://huly.io) - 一体化项目管理平台（替代 Linear、Jira、Slack、Notion、Motion）。 ([演示](https://app.huly.io), [源代码](https://github.com/hcengineering/platform)) `EPL-2.0` `Docker/K8S/Nodejs`
- [Ideon](https://www.theideon.com) - 围绕无限画布构建的项目工作区；将 GitHub、GitLab、Gitea 和 Forgejo 存储库与注释、链接和任务一起嵌入，并进行实时协作。 ([源代码](https://github.com/3xpyth0n/ideon)) `AGPL-3.0` `Docker`
- [Kaneo](https://kaneo.app/) - 项目管理平台注重简单性和效率。 ([演示](https://demo.kaneo.app/), [源代码](https://github.com/usekaneo/kaneo)) `MIT` `K8S/Docker`
- [Leantime](https://leantime.io) - 适用于小型团队和初创公司的精益项目管理系统，帮助管理项目从构思到交付的整个过程。 ([源代码](https://github.com/leantime/leantime)) `AGPL-3.0` `PHP/Docker`
- [Mindwendel](https://www.mindwendel.com/) - 在团队内集思广益并投票赞成想法和想法。 ([演示](https://www.mindwendel.com), [源代码](https://github.com/b310-digital/mindwendel)) `AGPL-3.0` `Docker/Elixir`
- [minimal-git-server](https://github.com/mcarbonne/minimal-git-server) - 轻量级 git 服务器，具有基本的 CLI 来管理存储库，支持多个帐户并在容器中运行。 `麻省理工学院` `Docker`
- [Octobox](https://octobox.io/) `⚠` - 收回对 GitHub 通知的控制权。 ([源代码](https://github.com/octobox/octobox)) `AGPL-3.0` `Ruby/Docker`
- [OneDev](https://onedev.io/) - 一体化 DevOps 平台。具有 Git 管理、问题跟踪和 CI/CD。简单而强大。 ([源代码](https://code.onedev.io/projects/160)) `MIT` `Java/Docker/K8S`
- [OpenProject](https://www.openproject.org) - 管理您的项目、任务和目标。通过工作包进行协作，并将它们链接到 Github 上的拉取请求。 ([源代码](https://github.com/opf/openproject)) `GPL-3.0` `Ruby/deb/Docker`
- [Pagure](https://pagure.io/pagure) - 轻量级、强大且灵活的以 git 为中心的锻造，其功能为联合和去中心化开发奠定了基础。 ([演示](https://pagure.io/)) `GPL-2.0` `Docker/Python/deb`
- [Phorge](https://we.phorge.it/) - 用于协作、管理、组织和审查软件开发项目的社区驱动平台。 ([源代码](https://we.phorge.it/source/phorge/)) `Apache-2.0` `PHP`
- [Plane](https://plane.so) - 以尽可能简单的方式跟踪问题、史诗和产品路线图（替代 JIRA、线性和高度）。 ([演示](https://app.plane.so), [源代码](https://github.com/makeplane/plane)) `AGPL-3.0` `Docker`
- [ProjeQtOr](https://www.projeqtor.org/) - 完整、成熟的多用户项目管理系统，具有适用于项目所有阶段的广泛功能。 ([演示](https://demo.projeqtor.org/), [源代码](https://sourceforge.net/p/projectorria/code/HEAD/tree/branches/)) `AGPL-3.0` `PHP`
- [Redmine](https://www.redmine.org/) - 灵活的项目管理 Web 应用程序。 ([源代码](https://svn.redmine.org/redmine/)) `GPL-2.0` `Ruby`
- [Review Board](https://www.reviewboard.org/) - 适用于各种规模的项目和公司的可扩展且友好的代码审查工具。 ([演示](https://demo.reviewboard.org/), [源代码](https://github.com/reviewboard/reviewboard)) `MIT` `Python/Docker`
- [RhodeCode](https://rhodecode.com/) - 统一并简化 Git、Subversion 和 Mercurial 的存储库管理。 ([源代码](https://code.rhodecode.com/)) `AGPL-3.0` `Python`
- [Rukovoditel](https://www.rukovoditel.net/) - 可配置的开源项目管理、基于网络的应用程序。 ([源代码](https://www.rukovoditel.net/download.php)) `GPL-2.0` `PHP`
- [SCM Manager](https://www.scm-manager.org/) - 通过 http 共享和管理 Git、Mercurial 和 Subversion 存储库的最简单方法。 ([源代码](https://github.com/scm-manager/scm-manager)) `BSD-3-Clause` `Java/deb/Docker/K8S`
- [ShipShipShip](https://shipshipship.io) - 连接项目管理和客户沟通的变更日志和路线图平台。 ([演示](https://demo.shipshipship.io/admin), [源代码](https://github.com/GauthierNelkinsky/ShipShipShip)) `Apache-2.0` `Docker`
- [Smederee](https://smeder.ee) - 一个节俭的平台，致力于帮助人们利用 Darcs 版本控制系统的强大功能共同构建出色的软件。 ([源代码](https://smeder.ee/~jan0sch/smederee)) `AGPL-3.0` `Scala`
- [Sourcehut](https://sourcehut.org/) - 没有 JavaScript 的完整 Web git 界面。 ([演示](https://sr.ht/), [源代码](https://git.sr.ht/~sircmpwn/git.sr.ht/tree)) `GPL-2.0` `Go`
- [Taiga](https://www.taiga.io/) - 基于看板和 Scrum 方法的敏捷项目管理工具。 ([源代码](https://github.com/kaleidos-ventures)) `MPL-2.0` `Docker/Python/Nodejs`
- [Titra](https://titra.io/) - 适用于自由职业者和小型团队的时间跟踪解决方案。 ([源代码](https://github.com/titraio/titra)) `GPL-3.0` `Javascript/Docker`
- [Trac](https://trac.edgewall.org/) - Trac 是一个用于软件开发项目的增强型 wiki 和问题跟踪系统。 `BSD-3-Clause` `Python/deb`
- [Traq](https://traq.io/) - 用 PHP 编写的项目管理和问题跟踪系统。 ([源代码](https://github.com/nirix/traq)) `GPL-3.0` `PHP/Nodejs`
- [Tuleap](https://www.tuleap.org/) - Tuleap 是一个自由套件，用于规划、跟踪、编码和协作软件项目。 ([源代码](https://tuleap.net/plugins/git/tuleap/tuleap/stable?p=tuleap%2Fstable.git&a=tree)) `GPL-2.0` `PHP`
- [UVDesk](https://www.uvdesk.com/) - UVDesk 社区是一个面向服务、事件驱动的可扩展开源帮助台系统，您的组织可以使用它以任何您想象的方式轻松地为您的客户提供有效的支持。 ([演示](https://demo.uvdesk.com/), [源代码](https://github.com/uvdesk/community-sculpture)) `MIT` `PHP`
- [ZenTao](https://www.zentao.pm/) - 敏捷（scrum）项目管理系统/工具。 ([源代码](https://github.com/easysoft/zentaopms)) `AGPL-3.0` `PHP`


### 软件开发-测试

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

用于[软件测试]的工具和软件(https://en.wikipedia.org/wiki/Software_testing)。

- [Bencher](https://bencher.dev/) - 旨在捕获 CI 中性能回归的连续基准测试工具套件。 ([源代码](https://github.com/bencherdev/bencher)) `MIT/Apache-2.0` `Rust`
- [Request Inbox](https://request-inbox.com/) - 收集并检查 HTTP 请求以进行测试和调试。创建和管理收件箱、捕获详细的请求数据、配置自定义响应。 ([演示](https://request-inbox.com/), [源代码](https://github.com/jesusnoseq/request-inbox)) `Apache-2.0` `Docker`
- [WebHook Tester](https://github.com/tarampampam/webhook-tester) - 用于测试 WebHook 等的强大工具。 `麻省理工学院` `Docker/Go/deb/K8S`


### 静态站点生成器

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

[静态站点生成器](https://en.wikipedia.org/wiki/Web_template_system#Static_site_generators) 基于原始数据、纯文本文件和一组模板生成完整的静态 HTML 网站。

**请访问 [staticsitegenerators.bevry.me](https://staticsitegenerators.bevry.me)、[staticgen.com](https://www.staticgen.com)**

_相关：[博客平台](#blogging-platforms)、[照片画廊](#photo-galleries)、[内容管理系统 (CMS)](#content-management-systems-cms)_



### 任务管理和待办事项列表

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

[任务管理](https://en.wikipedia.org/wiki/Task_management#Task_management_software)软件。

_相关：[软件开发-项目管理](#软件开发---项目管理)、[票务](#ticketing)_

- [4ga Boards](https://4gaboards.com) - 简单的实时看板管理可实现直观的任务跟踪。具有优雅的深色模式、可折叠的待办事项列表和多任务处理工具，可提高团队的工作效率。 ([演示](https://demo.4gaboards.com), [源代码](https://github.com/RARgames/4gaBoards)) `MIT` `Nodejs/Docker/K8S`
- [AppFlowy](https://appflowy.io/) - 为不同项目构建详细的待办事项列表，同时跟踪每个项目的状态。开源概念替代方案。 ([源代码](https://github.com/AppFlowy-IO/appflowy)) `AGPL-3.0` `Rust/Dart/Docker`
- [Donetick](https://donetick.com) - 适合个人和家庭使用的任务和家务管理工具，具有先进的调度、灵活的分配和小组共享功能、详细的历史记录、通过 API 实现自动化、简单而现代的设计。 ([演示](https://app.donetick.com/), [源代码](https://github.com/donetick/donetick)) `AGPL-3.0` `Go/Docker`
- [HamsterBase Tasks](https://tasks.hamsterbase.com) - 一个帮助组织想法和构建伟大事物的工具。规划、组织、构建和运输。 ([演示](https://tasks-app.hamsterbase.com), [源代码](https://github.com/hamsterbase/tasks)) `AGPL-3.0` `Docker`
- [Kanboard](https://kanboard.org/) - 简单的视觉任务板。 ([源代码](https://github.com/kanboard/kanboard)) `MIT` `PHP`
- [Listaway](https://github.com/jeffrpowell/listaway/) - 用于创建和公开共享项目列表的列表管理应用程序。支持身份验证、管理工具、项目注释和优先级，以及选择带有随机 URL 的公共只读链接（替代亚马逊列表）。 ([源代码](https://github.com/jeffrpowell/listaway)) `MIT` `Docker`
- [myTinyTodo](https://www.mytinytodo.net/) - 以 AJAX 风格管理待办事项列表的简单方法。使用 PHP、jQuery、SQLite/MySQL。符合 GTD。 ([演示](https://www.mytinytodo.net/demo/), [源代码](https://github.com/maxpozdeev/mytinytodo/)) `GPL-2.0` `PHP`
- [Nullboard](https://github.com/apankrat/nullboard) - 单页极简看板；紧凑、可读性强、使用快捷。 ([演示](https://nullboard.io/preview)) `BSD-2-Clause` `Javascript`
- [OpenHabitTracker](https://openhabittracker.net) - 通过时间跟踪、日历视图和完成情况统计来跟踪习惯、任务和笔记。 ([演示](https://pwa.openhabittracker.net), [源代码](https://github.com/Jinjinov/OpenHabitTracker)) `GPL-3.0` `Docker`
- [Our Shopping List](https://github.com/nanawel/our-shopping-list) - 简单的共享列表应用程序，包括购物列表和任何其他需要协作使用的小型待办事项列表。 ([演示](https://osl.lanterne-rouge.info/)) `AGPL-3.0` `Docker`
- [Super Productivity](https://super-productivity.com) - 高级待办事项列表应用程序，具有集成的时间盒和时间跟踪功能。与 Jira、GitHub、GitLab、Redmine 和 OpenProject 集成。 ([源代码](https://github.com/super-productivity/super-productivity)) `MIT` `Docker`
- [Task Keeper](https://github.com/nymanjens/piga) - 面向高级用户的列表编辑器，由自托管服务器支持。 `Apache-2.0` `Scala`
- [Tasks.md](https://github.com/BaldissaraMatheus/Tasks.md) - 一个自托管、基于文件的任务管理板，支持 Markdown 语法。 `麻省理工学院` `Docker`
- [Taskwarrior](https://taskwarrior.org/) - Taskwarrior 是免费开源软件，可从命令行管理您的 TODO 列表。它灵活、快速、高效且不引人注目。它完成它的工作然后就不再妨碍你了。 ([源代码](https://taskwarrior.org/download/#git)) `MIT` `C++`
- [Tracks](https://www.getontracks.org/) - 基于 Web 的应用程序可帮助您实施 David Allen 的 [Getting Things Done™](https://en.wikipedia.org/wiki/Getting_Things_Done) 方法。 ([源代码](https://github.com/TracksApp/tracks)) `GPL-2.0` `Ruby`
- [tududi](https://tududi.com/) - 具有分层结构、智能重复任务和无缝 Telegram 集成的任务管理工具。 ([源代码](https://github.com/chrisvel/tududi)) `MIT` `Docker`
- [Vikunja](https://vikunja.io/) - 用于组织您的生活的待办事项应用程序。 ([演示](https://try.vikunja.io/login), [源代码](https://github.com/go-vikunja/vikunja)) `AGPL-3.0/GPL-3.0` `Go`
- [Wekan](https://wekan.github.io/) - 类似 Trello 的开源看板。 ([源代码](https://github.com/wekan/wekan)) `MIT` `Nodejs`


### 票务

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

[帮助台](https://en.wikipedia.org/wiki/Help_desk_software)、[bug](https://en.wikipedia.org/wiki/Bug_tracking_system) 和[问题](https://en.wikipedia.org/wiki/Issue_tracking_system) 跟踪软件可帮助跟踪用户请求、错误和缺失的功能。

_相关：[任务管理和待办事项列表](#task-management--to-do-lists)、[软件开发-项目管理](#software-development---project-management)_

- [Bugzilla](https://www.bugzilla.org/) - 最初由 Mozilla 项目开发和使用的通用错误跟踪器和测试工具。 ([源代码](https://github.com/bugzilla/bugzilla)) `MPL-2.0` `Perl`
- [Frappe Helpdesk](https://frappe.io/helpdesk) - 帮助台软件可帮助您简化公司的支持，提供简单的设置、简洁的用户界面和自动化工具，以有效解决客户的疑问。 ([源代码](https://github.com/frappe/helpdesk)) `AGPL-3.0` `Docker`
- [FreeScout](https://freescout.net/) - 基于电子邮件的客户支持应用程序、帮助台和共享邮箱（Zendesk 和 Help Scout 的替代方案）。 ([演示](https://demo.freescout.net/login), [源代码](https://github.com/freescout-help-desk/freescout)) `AGPL-3.0` `PHP/Docker`
- [GlitchTip](https://glitchtip.com) - 错误跟踪应用程序收集您的应用程序报告的错误。 ([源代码](https://gitlab.com/glitchtip/glitchtip)) `MIT` `Python/Docker/K8S`
- [ITFlow](https://itflow.org) - MSP（托管服务提供商）的客户 IT 文档、票务、发票和会计。 ([演示](https://demo.itflow.org), [源代码](https://github.com/itflow-org/itflow)) `GPL-3.0` `PHP`
- [Libredesk](https://libredesk.io/) - 现代全渠道客户支持台。实时聊天、电子邮件等都集中在一个二进制文件中。 ([演示](https://demo.libredesk.io), [源代码](https://github.com/abhinavxd/libredesk)) `AGPL-3.0` `Docker/Go/Nodejs`
- [MantisBT](https://www.mantisbt.org/) - 错误跟踪器，最适合软件开发。 ([演示](https://www.mantisbt.org/bugs/my_view_page.php), [源代码](https://github.com/mantisbt/mantisbt)) `GPL-2.0` `PHP`
- [OTOBO](https://otobo.io/en/) - 灵活的基于网络的票务系统，用于客户服务、帮助台、IT 服务管理。 ([演示](https://otobo.io/en/service-management-plattform/otobo-demo/), [源代码](https://github.com/RotherOSS/otobo)) `GPL-3.0` `Perl/Docker`
- [Request Tracker](https://www.bestpractical.com/rt/) - 企业级问题跟踪系统。 ([源代码](https://github.com/bestpractical/rt)) `GPL-2.0` `Perl`
- [Roundup Issue Tracker](https://www.roundup-tracker.org/) - 易于使用和安装的问题跟踪系统，具有命令行、Web、REST、XML-RPC 和电子邮件界面。设计时考虑到了灵活性——而不仅仅是另一个错误跟踪器。 ([源代码](https://www.roundup-tracker.org/code.html)) `MIT/ZPL-2.0` `Python/Docker`
- [Zammad](https://zammad.org/) - 易于使用但功能强大的开源支持和票务系统。 ([源代码](https://github.com/zammad/zammad)) `AGPL-3.0` `Ruby/deb`


### 时间追踪

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

[时间跟踪软件](https://en.wikipedia.org/wiki/Time-tracking_software) 是一类计算机软件，允许用户记录在任务或项目上花费的时间。

- [ActivityWatch](https://activitywatch.net) - 自动跟踪您在设备上花费的时间。 ([源代码](https://github.com/ActivityWatch/activitywatch)) `MPL-2.0` `Python`
- [Beaver Habit Tracker](https://github.com/daya0576/beaverhabits) - 习惯跟踪应用程序可以保存您短暂的生活中的宝贵时刻。 ([演示](https://beaverhabits.com/demo)) `BSD-3-Clause` `Docker`
- [Ever Gauzy](https://gauzy.co) - 面向协作、按需和共享经济的开放式业务管理平台（ERP/CRM/HRM/ATS/PM）。 ([演示](https://demo.gauzy.co), [源代码](https://github.com/ever-co/ever-gauzy)) `AGPL-3.0` `Docker/Nodejs`
- [Kimai](https://www.kimai.org/) - 跟踪工作时间并按需打印活动摘要。 ([演示](https://www.kimai.org/demo/), [源代码](https://github.com/kimai/kimai)) `AGPL-3.0` `PHP`
- [solidtime](https://www.solidtime.io) - 适用于自由职业者和机构的现代跟踪应用程序。 ([源代码](https://github.com/solidtime-io/solidtime)) `AGPL-3.0` `Docker`
- [TimeTagger](https://timetagger.app) - 一个基于交互式时间线和强大报告的开源时间跟踪器。 ([演示](https://timetagger.app/app/demo), [源代码](https://github.com/almarklein/timetagger)) `GPL-3.0` `Python`
- [Traggo](https://traggo.net/) - Traggo 是一个基于标签的时间跟踪工具。 Traggo 中没有任务，只有标记的时间跨度。 ([源代码](https://github.com/traggo/server)) `GPL-3.0` `Docker/Go`
- [Wakapi](https://wakapi.dev/) - 用于编码统计的跟踪工具，与WakaTime兼容。 ([源代码](https://github.com/muety/wakapi)) `GPL-3.0` `Go/Docker`
- [Ziit](https://ziit.app) - 代码时间跟踪的瑞士军刀（WakaTime 的替代品）。 ([源代码](https://github.com/0pandadev/ziit)) `AGPL-3.0` `Docker`


### 网址缩短器

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

[URL 缩短](https://en.wikipedia.org/wiki/URL_shortening) 是缩短 [URL](https://en.wikipedia.org/wiki/Uniform_Resource_Locator) 的操作，使其变得更短，但仍直接指向所需页面。在托管之前，请参阅 URL 缩短器的[缺点](https://en.wikipedia.org/wiki/URL_shortening#Disadvantages)。

- [bit](https://github.com/sjdonado/bit) - 快速、轻量级、资源高效、已编译的 URL 缩短器。 `麻省理工学院` `Docker/Crystal`
- [Chhoto URL](https://github.com/SinTan1729/chhoto-url) - 简单、快如闪电的 URL 缩短器，没有任何膨胀（simple-shorten 的分支）。 ([演示](https://github.com/SinTan1729/chhoto-url?tab=readme-ov-file#demo), [客户端](https://github.com/SinTan1729/chhoto-url/blob/main/TOOLS.md)) `MIT` `Rust/Docker`
- [clink](https://git.crueter.xyz/crueter/clink) - 用纯 C 语言编写的超最小链接缩短服务，专注于较小的可执行文件大小、可移植性和易于配置。 ([演示](https://short.crueter.xyz)) `AGPL-3.0` `C`
- [Flink](https://gitlab.com/rtraceio/web/flink) - 创建 QR 码、网站的可嵌入链接预览以及抓取/抓取元数据。 ([演示](https://flink.is)) `MIT` `Docker`
- [Kutt](https://kutt.to) - 现代 URL 缩短器，支持自定义域和自定义 URL。 ([演示](https://kutt.to), [源代码](https://github.com/thedevs-network/kutt)) `MIT` `Nodejs/Docker`
- [rs-short](https://git.42l.fr/42l/rs-short) - 用 Rust 编写的轻量级链接缩短器，具有缓存、垃圾邮件防护和网络钓鱼检测等功能。 ([演示](https://s.42l.fr/)) `MPL-2.0` `Rust`
- [Shlink](https://shlink.io) - 具有 REST API 和命令行界面的 URL 缩短器。包括官方渐进式 Web 应用程序和 docker 镜像。 ([源代码](https://github.com/shlinkio/shlink), [客户端](https://shlink.io/apps)) `MIT` `PHP/Docker`
- [Simple-URL-Shortener](https://github.com/azlux/Simple-URL-Shortener) - KISS URL 缩短器，公共或私人（带有帐户）。简约且轻便。没有依赖性。 ([演示](https://u.azlux.fr)) `MIT` `PHP`
- [YOURLS](https://yourls.org/) - YOURLS 是一组 PHP 脚本，可让您运行您自己的 URL 缩短程序。功能包括密码保护、URL 自定义、书签、统计、API、插件、jsonp。 ([源代码](https://github.com/YOURLS/YOURLS)) `MIT` `PHP`


### 视频监控

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

视频监控，也称为[闭路电视 (CCTV)](https://en.wikipedia.org/wiki/Closed- Circuit_television)，是在需要额外安全或持续监控的区域使用摄像机进行监控。

_相关：[媒体流-视频流](#media-streaming---video-streaming)_

- [Bluecherry](https://www.bluecherrydvr.com/) - 支持 IP 和模拟摄像机的闭路电视 (CCTV) 软件应用程序。 ([源代码](https://github.com/bluecherrydvr/bluecherry-apps)) `GPL-2.0` `PHP`
- [Frigate](https://frigate.video/) - 使用本地处理的人工智能监控您的安全摄像头。 ([源代码](https://github.com/blakeblackshear/frigate)) `MIT` `Docker/Python/Nodejs`
- [motionEye](https://github.com/motioneye-project/motioneye) - Motion 软件的在线界面，一种具有运动检测功能的视频监控程序。 `GPL-3.0` `Python/Docker`
- [Secluso](https://secluso.com) - 适用于 Raspberry Pi 的私人 DIY 家庭安全摄像头系统，具有端到端加密远程访问和用于实时视频、警报和录音回放的移动应用程序。 ([源代码](https://github.com/secluso/core)) `GPL-3.0` `Rust`
- [SentryShot](https://codeberg.org/SentryShot/sentryshot) - 视频监控管理系统。 `GPL-2.0` `Docker/Rust`
- [Strix](https://github.com/eduard256/Strix) - 自动发现 IP 摄像机的工作流 URL 并生成即用型 Frigate 和 go2rtc 配置。 `麻省理工学院``Go/Docker`
- [Viseron](https://viseron.netlify.app/) - 自托管、仅限本地的 NVR 和 AI 计算机视觉软件。凭借物体检测、运动检测、人脸识别等功能，它使您能够密切关注您的家、办公室或您想要监控的任何其他地方。 ([源代码](https://github.com/roflcoopter/viseron)) `MIT` `Docker`
- [Zoneminder](https://www.zoneminder.com/) - 支持 IP、USB 和模拟摄像机的闭路电视 (CCTV) 软件应用程序。 ([源代码](https://github.com/ZoneMinder/ZoneMinder)) `GPL-2.0` `PHP/deb`


### VPN

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

[虚拟专用网络 (VPN)](https://en.wikipedia.org/wiki/Virtual_private_network) 将专用网络扩展到公共网络，使用户能够跨共享或公共网络发送和接收数据，就好像他们的计算设备直接连接到专用网络一样。

**请访问[awesome-sysadmin/VPN](https://github.com/awesome-foss/awesome-sysadmin#vpn)**



### 网络服务器

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

Web 服务器和反向代理。 [Web 服务器](https://en.wikipedia.org/wiki/Web_server) 是一个软件和底层硬件，它通过 [HTTP](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol)（为分发 Web 内容而创建的网络协议）或其安全变体 [HTTPS](https://en.wikipedia.org/wiki/HTTPS) 接受请求。 [反向代理](https://en.wikipedia.org/wiki/Reverse_proxy) 是一种代理服务器，在任何客户端看来都是普通的 Web 服务器，但实际上仅充当将请求转发到一个或多个普通 Web 服务器的中介。

_相关：[代理](#proxy)_

- [Algernon](https://algernon.roboticoverlords.org/) - 小型独立的纯 Go Web 服务器，支持 Lua、Markdown、HTTP/2、QUIC、Redis 和 PostgreSQL。 ([源代码](https://github.com/xyproto/algernon)) `BSD-3-Clause` `Go/Docker`
- [Apache HTTP Server](https://httpd.apache.org/) - 安全、高效且可扩展的服务器，提供与当前 HTTP 标准同步的 HTTP 服务。 ([源代码](https://svn.apache.org/repos/asf/httpd/httpd/trunk/)) `Apache-2.0` `C/deb/Docker`
- [BunkerWeb](https://www.bunkerweb.io) - 下一代 Web 应用程序防火墙 (WAF) 将保护您的 Web 服务。 ([演示](https://demo.bunkerweb.io), [源代码](https://github.com/bunkerity/bunkerweb), [客户端](https://docs.bunkerweb.io/latest/plugins/)) `AGPL-3.0` `deb/Docker/K8S/Python`
- [Caddy](https://caddyserver.com/) - 功能强大、企业级、开源 Web 服务器，具有自动 HTTPS。 ([源代码](https://github.com/caddyserver/caddy)) `Apache-2.0` `Go/deb/Docker`
- [Ferron](https://ferron.sh/) - 用 Rust 编写的快速、内存安全的 Web 服务器。 ([源代码](https://github.com/ferronweb/ferron)) `MIT` `Rust/Docker/deb`
- [go-doxy](https://github.com/yusing/godoxy) - 轻量级、简单且高性能的反向代理，具有 WebUI、Docker 集成、基于流量的容器自动关闭/启动。 `麻省理工学院` `Docker/Go`
- [godoxy](https://docs.godoxy.dev/) - 适用于自托管者的高性能反向代理和容器编排器。 ([演示](https://demo.godoxy.dev/), [源代码](https://github.com/yusing/godoxy)) `MIT` `Docker/Go`
- [HAProxy](https://www.haproxy.org/) - 非常快速且可靠的反向代理，为基于 TCP 和 HTTP 的应用程序提供高可用性、负载平衡和代理。 ([源代码](https://git.haproxy.org/?p=haproxy.git;a=tree)) `GPL-2.0` `C/deb/Docker`
- [Lighttpd](https://www.lighttpd.net/) - 安全、快速、合规且非常灵活的 Web 服务器，已针对高性能环境进行了优化。 ([源代码](https://git.lighttpd.net/lighttpd/lighttpd1.4)) `BSD-3-Clause` `C/deb/Docker`
- [Nginx Proxy Manager](https://nginxproxymanager.com/) - Docker 容器，用于通过简单而强大的界面管理 Nginx 代理主机。 ([源代码](https://github.com/NginxProxyManager/nginx-proxy-manager)) `MIT` `Docker`
- [NGINX](https://nginx.org/en/) - HTTP 和反向代理服务器、邮件代理服务器以及通用 TCP/UDP 代理服务器。 ([源代码](https://github.com/nginx/nginx)) `BSD-2-Clause` `C/deb/Docker`
- [Pangolin](https://digpangolin.com/) - 身份感知隧道反向代理，具有仪表板 UI、访问控制和基于 WireGuard 的隧道（替代 Cloudflare Tunnel、Tailscale）。 ([源代码](https://github.com/fosrl/pangolin)) `AGPL-3.0` `Docker`
- [Pomerium](https://www.pomerium.io) - 身份识别反向代理，现已过时的 oauth_proxy 的后继者。它会在将您的请求代理到后端之前插入 OAuth 步骤，以便您可以安全地将自托管网站公开到公共互联网。 ([源代码](https://github.com/pomerium/pomerium)) `Apache-2.0` `Go/Docker`
- [SafeLine](https://waf.chaitin.com/) - Web 应用程序防火墙/反向代理可保护您的 Web 应用程序免受攻击和利用。 ([演示](https://demo.waf.chaitin.com/), [源代码](https://github.com/chaitin/SafeLine)) `GPL-3.0`Docker`
- [Static Web Server](https://static-web-server.net/) - 用于静态文件服务的跨平台、高性能、异步 Web 服务器。 ([源代码](https://github.com/static-web-server/static-web-server)) `Apache-2.0/MIT` `Rust/Docker`
- [SWAG (Secure Web Application Gateway)](https://github.com/linuxserver/docker-swag) - Nginx Web 服务器和反向代理，支持 PHP、内置 Certbot (Let's Encrypt) 客户端和fail2ban 集成。 `GPL-3.0` `Docker`
- [Traefik](https://traefik.io/) - HTTP 反向代理和负载均衡器，使部署微服务变得容易。 ([源代码](https://github.com/traefik/traefik)) `MIT` `Go/Docker`
- [UUSEC WAF](https://waf.uusec.com/) - 业界领先的高性能、人工智能和语义技术的Web应用防火墙和API安全网关（nginx的fork）。 ([源代码](https://github.com/Safe3/uusec-waf)) `GPL-3.0` `C/Lua/Docker`
- [Vinyl Cache](https://vinyl-cache.org/) - Web 应用程序加速器/缓存 HTTP 反向代理（以前称为 Varnish）。 ([源代码](https://code.vinyl-cache.org/vinyl-cache/vinyl-cache)) `BSD-2-Clause` `Go/deb/Docker`
- [Zoraxy](https://zoraxy.aroz.org/) - 通用 HTTP 反向代理和转发工具。 ([源代码](https://github.com/tobychui/zoraxy)) `AGPL-3.0` `Go/Docker`


### 维基百科

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

[wiki](https://en.wikipedia.org/wiki/Wiki) 是由其自己的受众直接使用网络浏览器协作编辑和管理的出版物。

_相关：[笔记和编辑器](#note-keeping--editors)、[静态站点生成器](#static-site-generators)、[知识管理工具](#knowledge-management-tools)_

_另请参阅：[Wikimatrix](https://www.wikimatrix.org/)、[wiki 软件列表 - 维基百科](https://en.wikipedia.org/wiki/List_of_wiki_software)、[wiki 软件比较 - 维基百科](https://en.wikipedia.org/wiki/Comparison_of_wiki_software)_

- [AmuseWiki](https://amusewiki.org/) - Amusewiki 基于 Emacs Muse 标记，大部分与原始实现兼容。它可以作为只读站点、受监管的 wiki、完全开放的 wiki 甚至私人站点。 ([演示](https://sandbox.amusewiki.org), [源代码](https://github.com/melmothx/amusewiki)) `GPL-1.0` `Perl/Docker`
- [BookStack](https://www.bookstackapp.com/) - 组织和存储信息。像时尚一样将文档存储在书中。 ([演示](https://www.bookstackapp.com/#demo), [源代码](https://codeberg.org/bookstack/bookstack)) `MIT` `PHP/Docker`
- [django-wiki](https://github.com/django-wiki/django-wiki) - Wiki 系统具有复杂的功能、简单的集成和出色的界面。以风格存储您的知识：使用 django 模型。 ([演示](https://demo.django-wiki.org/)) `GPL-3.0` `Python`
- [docmost](https://docmost.com/) - 协作 wiki 和文档软件（Confluence、Notion 的替代品）。 ([源代码](https://github.com/docmost/docmost)) `AGPL-3.0` `Docker/Nodejs`
- [Documize](https://documize.com) - 现代 Docs + Wiki 软件，具有内置工作流程，单个二进制可执行文件，只需带 MySQL/Percona。 ([源代码](https://github.com/documize/community)) `AGPL-3.0` `Go`
- [Dokuwiki](https://www.dokuwiki.org/DokuWiki) - 易于使用、轻量级、符合标准的 wiki 引擎，具有简单的语法，允许读取 wiki 之外的数据。所有数据都存储在纯文本文件中，因此不需要数据库。 ([源代码](https://github.com/dokuwiki/dokuwiki)) `GPL-2.0` `PHP`
- [Feather Wiki](https://feather.wiki) - 一个闪电般快速且可无限扩展的工具，用于创建个人非线性笔记本、数据库和 wiki，它完全独立，在浏览器中运行，大小仅为 58 KB。 ([演示](https://feather.wiki/?page=gallery#wikis)、[源代码](https://codeberg.org/Alamantus/FeatherWiki)、[客户端](https://feather.wiki/?page=gallery#extensions)) `AGPL-3.0` `Javascript`
- [Gitit](https://github.com/jgm/gitit) - Wiki 程序，将页面和上传的文件存储在 git 存储库中，然后可以使用 VCS 命令行工具或 wiki 的 Web 界面进行修改。 `GPL-2.0` `Haskell`
- [Gollum](https://github.com/gollum/gollum) - 简单、由 Git 驱动的 wiki，具有良好的 API 和本地前端。 “麻省理工学院”“红宝石”
- [LeafWiki](https://github.com/perber/leafwiki) - 一个快速 wiki，适合那些在文件夹而不是提要中思考的人。快速编辑。树状导航。磁盘上的降价。 ([演示](https://demo.leafwiki.com)) `MIT` `Docker/Go`
- [Mediawiki](https://www.mediawiki.org/wiki/MediaWiki) - Wiki 软件包为维基百科和所有其他维基媒体项目提供支持，每月为数亿用户提供服务。 ([演示](https://en.wikipedia.org/wiki/Main_Page), [源代码](https://phabricator.wikimedia.org/source/mediawiki/)) `GPL-2.0` `PHP`
- [Mycorrhiza Wiki](https://mycorrhiza.wiki/) - 使用 Mycomarkup 作为主要标记语言，用 Go 编写的文件系统和基于 git 的 wiki 引擎。 ([源代码](https://github.com/bouncepaw/mycorriza/)) `AGPL-3.0` `Go`
- [Oddmuse](https://oddmuse.org/) - 用 Perl 编写的简单 wiki 引擎。无需数据库。 ([源代码](https://github.com/kensanata/oddmuse)) `GPL-3.0` `Perl`
- [Otter Wiki](https://otterwiki.com/) - 使用 Markdown 的简单、易于使用的 wiki 软件。 ([源代码](https://github.com/redimp/otterwiki)) `MIT` `Docker`
- [PmWiki](https://www.pmwiki.org) - 基于 Wiki 的系统，用于协作创建和维护网站。 `GPL-3.0` `PHP`
- [Raneto](https://raneto.com/) - 使用静态 Markdown 文件的知识库平台。 ([源代码](https://github.com/ryanlelek/Raneto)) `MIT` `Nodejs`
- [TiddlyWiki](https://tiddlywiki.com/) - 可重复使用的非线性个人网络笔记本。 ([源代码](https://github.com/TiddlyWiki/TiddlyWiki5)) `BSD-3-Clause` `Nodejs`
- [Tiki](https://tiki.org/HomePage) - 具有最多内置功能的 Wiki CMS 组件。 ([演示](https://tiki.org/Try-Tiki), [源代码](https://gitlab.com/tikiwiki/tiki)) `LGPL-2.1` `PHP`
- [W](https://w.club1.fr) - 轻量级、多用户、平面文件数据库 Wiki 引擎。使用 Mardown/HTML/CSS/JS 快速创建页面并在 Web 浏览器中编辑它们。与其他 wiki 的主要区别在于，我们鼓励您单独自定义每个页面样式。 ([源代码](https://github.com/vincent-peugnet/wcms)) `AGPL-3.0` `PHP`
- [WackoWiki](https://wackowiki.org/) - WackoWiki 是一个轻便且易于安装的多语言 Wiki 引擎。 ([源代码](https://github.com/WackoWiki/wackowiki)) `BSD-3-Clause` `PHP`
- [Wiki-Go](https://leomoon.com/downloads/web-apps/wiki-go/) - 一个现代的、功能丰富的、无数据库的平面文件 wiki 平台。 ([演示](https://wikigo.leomoon.com), [源代码](https://github.com/leomoon-studios/wiki-go)) `GPL-3.0` `Go/Docker`
- [Wiki.js](https://js.wiki/) - 使用 Git 和 Markdown 的现代、轻量级且功能强大的 wiki 应用程序。 ([演示](https://docs.requarks.io), [源代码](https://github.com/Requarks/wiki)) `AGPL-3.0` `Nodejs/Docker/K8S`
- [WikiDocs](https://www.wikidocs.app/) - 无数据库 Markdown 平面文件 wiki 引擎。 ([源代码](https://github.com/Zavy86/WikiDocs)) `MIT` `PHP/Docker`
- [WiKiss](https://wikiss.tuxfamily.org/) - Wiki，易于使用和安装。 ([源代码](https://svnweb.tuxfamily.org/listing.php?repname=wikiss/svn&path=%2F&sc=0)) `GPL-2.0` `PHP`
- [XWiki](https://www.xwiki.org) - 第二代 wiki 允许用户通过强大的基于扩展的架构来扩展其功能。 ([演示](https://www.xwikiplayground.org/xwiki/bin/view/Main/), [源代码](https://github.com/xwiki/xwiki-platform)) `LGPL-2.1` `Java/Docker/deb`
- [Zim](https://zim-wiki.org/) - 用于维护 wiki 页面集合的图形文本编辑器。每个页面都可以包含其他页面的链接、简单的格式和图像。 ([源代码](https://github.com/zim-desktop-wiki/zim-desktop-wiki)) `GPL-2.0` `Python/deb`


--------------------

## 许可证清单

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

- `0BSD` - [BSD 零条款许可证](https://spdx.org/licenses/0BSD.html)
- `AAL` - [归属保证许可证](https://spdx.org/licenses/AAL.html)
- `AGPL-3.0` - [GNU Affero 通用公共许可证 3.0](https://spdx.org/licenses/AGPL-3.0.html)
- `Apache-2.0` - [Apache，版本 2.0](https://spdx.org/licenses/Apache-2.0.html)
- `APSL-2.0` - [Apple 公共源代码许可证，版本 2.0](https://spdx.org/licenses/APSL-2.0.html)
- `Artistic-2.0` - [Artistic 许可证版本 2.0](https://spdx.org/licenses/Artistic-2.0.html)
- `Beerware` - [Beerware 许可证](https://spdx.org/licenses/Beerware.html)
- `BSD-2-Clause` - [BSD 2-clause“简化”](https://spdx.org/licenses/BSD-2-Clause.html)
- `BSD-2-Clause-FreeBSD` - [BSD 2-Clause FreeBSD 许可证](https://spdx.org/licenses/BSD-2-Clause-FreeBSD.html)
- `BSD-3-Clause` - [BSD 3-Clause“新”或“修订”](https://spdx.org/licenses/BSD-3-Clause.html)
- `BSD-3-Clause-Attribution` - [带归属的 BSD](https://spdx.org/licenses/BSD-3-Clause-Attribution.html)
- `BSD-4-Clause` - [BSD 4-clause“原始”](https://spdx.org/licenses/BSD-4-Clause.html)
- `CAL-1.0` - [加密自治许可证 1.0](https://spdx.org/licenses/CAL-1.0.html)
- `CC-BY-SA-3.0` - [知识共享署名-相同方式共享 3.0 许可证](https://spdx.org/licenses/CC-BY-SA-3.0.html)
- `CC-BY-SA-4.0` - [知识共享署名-相同方式共享 4.0 许可证](https://spdx.org/licenses/CC-BY-SA-4.0.html)
- `CC0-1.0` - [公共领域/创意通用零 1.0](https://spdx.org/licenses/CC0-1.0.html)
- `CDDL-1.0` - [通用开发和分发许可证](https://spdx.org/licenses/CDDL-1.0.html)
- `CECILL-B` - [CEA CNRS INRIA Logiciel Libre](https://spdx.org/licenses/CECILL-B.html)
- `CPAL-1.0` - [通用公共归属许可证版本 1.0](https://spdx.org/licenses/CPAL-1.0.html)
- `ECL-2.0` - [教育社区许可证，版本 2.0](https://spdx.org/licenses/ECL-2.0.html)
- `EPL-1.0` - [Eclipse 公共许可证，版本 1.0](https://spdx.org/licenses/EPL-1.0.html)
- `EPL-2.0` - [Eclipse 公共许可证，版本 2.0](https://spdx.org/licenses/EPL-2.0.html)
- `EUPL-1.2` - [欧盟公共许可证 1.2](https://spdx.org/licenses/EUPL-1.2.html)
- `GPL-1.0` - [GNU 通用公共许可证 1.0](https://spdx.org/licenses/GPL-1.0.html)
- `GPL-2.0` - [GNU 通用公共许可证 2.0](https://spdx.org/licenses/GPL-2.0.html)
- `GPL-3.0` - [GNU 通用公共许可证 3.0](https://spdx.org/licenses/GPL-3.0.html)
- `IPL-1.0` - [IBM 公共许可证](https://spdx.org/licenses/IPL-1.0.html)
- `ISC` - [互联网系统联盟许可证](https://spdx.org/licenses/ISC.html)
- `LGPL-2.1` - [较宽松的通用公共许可证 2.1](https://spdx.org/licenses/LGPL-2.1.html)
- `LGPL-3.0` - [较宽松的通用公共许可证 3.0](https://spdx.org/licenses/LGPL-3.0.html)
- `MIT` - [MIT 许可证](https://spdx.org/licenses/MIT.html)
- `MPL-1.1` - [Mozilla 公共许可证版本 1.1](https://spdx.org/licenses/MPL-1.1.html)
- `MPL-2.0` - [Mozilla 公共许可证](https://spdx.org/licenses/MPL-2.0.html)
- `OSL-3.0` - [开放软件许可证 3.0](https://spdx.org/licenses/OSL-3.0.html)
- `Sendmail` - [Sendmail 许可证](https://spdx.org/licenses/Sendmail.html)
- `Ruby` - [Ruby 许可证](https://spdx.org/licenses/Ruby.html)
- `未授权` - [未授权](https://spdx.org/licenses/Unlicense.html)
- `WTFPL` - [做你他妈想要公共许可证的事](https://spdx.org/licenses/WTFPL.html)
- `Zlib` - [Zlib/libpng 许可证](https://spdx.org/licenses/Zlib.html)
- `ZPL-2.0` - [Zope 公共许可证 2.0](https://spdx.org/licenses/ZPL-2.0.html)


--------------------

## 反特征

- `⚠ ` - 取决于用户无法控制的专有服务

--------------------

## 外部链接

**[`^ 回到顶部 ^`](#awesome-selfhosted)**

- 用于发现/过滤 Awesome-selfhosted 应用程序的替代前端/门户：[awweso.me](https://awweso.me/)、[awesome-web.theravenhub](https://awesome-web.theravenhub.com/browse.html)、[awesomehub.web.app](https://awesomehub.js.org/list/selfhosted)
- [Awesome Sysadmin](https://github.com/awesome-foss/awesome-sysadmin) - 令人惊叹的开源系统管理资源的精选列表。
- 以某种形式实现隐私和去中心化的软件列表：[PRISM Break](https://prism-break.org/en/)、[privacytools.io](https://www.privacytools.io/)、[Alternative Internet](https://redecentralize.github.io/alternative-internet/)、[Libre Projects](https://libreprojects.net/)、[Easy Indie应用程序](https://easyindie.app)
- 其他很棒的列表：[很棒的大数据](https://github.com/0xnr/awesome-bigdata)、[很棒的公共数据集](https://github.com/awesomedata/awesome-public-datasets)
- 动态域名服务：[Afraid.org](https://freedns.afraid.org/domain/registry/)、[Pagekite](https://pagekite.net/)
- 社区/论坛：[lemmy.world 上的/c/selfhosted](https://lemmy.world/c/selfhosted)、[lemmy.ml 上的/c/selfhost](https://lemmy.ml/c/selfhost)、[reddit 上的/r/selfhosted](https://old.reddit.com/r/selfhosted/)、[/r/selfhosted 矩阵频道](https://matrix.to/#/#selfhosted:selfhosted.chat)、[reddit 上的/r/homelab](https://old.reddit.com/r/homelab/)、[IndieWeb](https://indieweb.org/)
- [theme.park](https://theme-park.dev/) - 50 个自托管应用程序的主题/皮肤集合！ ([源代码](https://github.com/GilbN/theme.park/)) `MIT` `CSS`

--------------------

## 贡献

贡献指南可以在[此处](https://github.com/awesome-selfhosted/awesome-selfhosted-data/blob/master/CONTRIBUTING.md)找到。

## 许可证

此列表遵循 [Creative Commons Attribution-ShareAlike 3.0 Unported](https://github.com/awesome-selfhosted/awesome-selfhosted/blob/master/LICENSE) 许可证。
许可条款总结于[此处](https://creativecommons.org/licenses/by-sa/3.0/)。
作者列表可以在 [AUTHORS](https://github.com/awesome-selfhosted/awesome-selfhosted-data/blob/master/AUTHORS) 文件中找到。
