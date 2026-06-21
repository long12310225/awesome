# 很棒的交通 [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

##### 围绕公共交通开源技术的数据标准、API、应用程序、工具、数据集和研究的社区列表。

开放技术为各利益相关者提供了合作改善公共交通的机会。

开放技术的要素包括：
- 开放标准
- 开放数据
- 开源软件（既是面向消费者的应用程序，如 OpenTripPlanner，又是开发工具，如 GTFS Validator）

该列表重点关注公共交通的开放技术生态系统。所包含的技术本身可能是开源的和/或依赖于开放标准和/或开放数据。

有什么要添加或更改的吗？在 [MobilityData/awesome-transit](https://github.com/MobilityData/awesome-transit) 上打开 [pull request](https://github.com/MobilityData/awesome-transit/pulls) 或 [issue](https://github.com/MobilityData/awesome-transit/issues)。

------------------------------

### 目录
- [生产数据](#producing-data)
  - [GTFS](#gtfs)
    - [GTFS 库](#gtfs-libraries)
    - [GTFS 转换器](#gtfs-converters)
    - [GTFS 数据收集和维护工具](#gtfs-data-collection-and-maintenance-tools)
    - [GTFS 合并工具](#gtfs-merge-tools)
    - [GTFS 分析工具](#gtfs-analysis-tools)
    - [GTFS 时间表发布工具](#gtfs-timetable-publishing-tools)
    - [GTFS 验证器](#gtfs-validators)
  - [GTFS实时](#gtfs-realtime)
    - [GTFS 实时库和演示应用程序](#gtfs-realtime-libraries--demo-apps)
    - [GTFS 实时验证器](#gtfs-realtime-validators)
    - [GTFS Realtime（和其他实时 API）归档工具](#gtfs-realtime-and-other-real-time-api-archival-tools)
    - [GTFS 实时转换器](#gtfs-realtime-convertors)
    - [GTFS 实时实用程序](#gtfs-realtime-utilities)
  - [SIRI](#siri)
  - [其他多模态数据格式](#other-multimodal-data-formats)
- [共享数据](#sharing-data)
- [使用数据](#using-data)
  - [消费者应用程序](#consumer-apps)
    - [网络应用程序（开源）](#web-apps-open-source)
    - [网络应用程序（闭源）](#web-apps-closed-source)
    - [本机应用程序（开源）](#native-apps-open-source)
    - [本机应用程序（闭源）](#native-apps-closed-source)
  - [Hardware](#hardware)
  - [用于创建 API 的软件](#software-for-creating-apis)
  - [SDKs](#sdks)
  - [Visualizations](#visualizations)
  - [代理工具](#agency-tools)
- [Resources](#resources)
  - [Community](#community)

## 产生数据

### GTFS

- [GTFS.org](https://gtfs.org) 通用传输馈送规范的官方文档网站。

#### GTFS课程

- [MobilityData - "Understanding GTFS: An intro and overview"](https://www.youtube.com/watch?v=SDz2460AjNo) - 视频概述了通用交通供给规范 (GTFS) 以及它为何对交通机构、乘客和政策制定者有用。
- [World Bank - "Intro. to GTFS" online course](https://olc.worldbank.org/content/introduction-general-transit-feed-specification-gtfs-and-informal-transit-system-mapping) - 用于学习 GTFS 和 GTFS-realtime 的免费在线自定进度课程。
- [Open Transit Data Toolkit](http://transitdatatoolkit.com/) - 帮助人们利用开放交通数据的一系列课程。
- [ArcGIS - GTFS 简介](https://www.youtube.com/watch?v=8OQKHhu1VgQ&t=148s)
- [GTFS-books](https://github.com/MobilityData/GTFS-books) - GTFS 和 GTFS Realtime 的综合指南。这些书由 [Quentin Zervaas](https://github.com/HendX) 撰写，并已捐赠给 [MobilityData](https://mobilitydata.org/) 并开放获取。
- [MBTA GTFS Onboarding](https://mybinder.org/v2/gh/mbta/gtfs_onboarding/main?urlpath=lab/tree/GTFS_Onboarding.ipynb) - MBTA 为 GTFS 静态创建的交互式教程。 GitHub 上提供了[独立 Docker 映像](https://github.com/mbta/gtfs_onboarding) 以及 Jupyter Notebook 的[托管/无安装版本](https://mybinder.org/v2/gh/mbta/gtfs_onboarding/main?urlpath=lab/tree/GTFS_Onboarding.ipynb)。
- [Planetizen "Building a Transit Map Web App" course](https://courses.planetizen.com/course/building-transit-map-app) - 有关设置您自己的基于 Web 的地图应用程序的视频教程，无需任何编码经验。

#### GTFS 消费者应用程序指南

- [Google Transit Developers](https://developers.google.com/transit/gtfs/) - GTFS 的其他 Google 特定文档。
- [Transit app Guidelines for Producing GTFS Static Data](https://resources.transitapp.com/article/458-guidelines-for-producing-gtfs-static-data-for-transit) - GTFS 的其他 Transit 应用程序特定文档。
- [Bing Maps Transit - Add your transit data to Bing Maps](https://www.bing.com/maps/transitcontentproviders) - GTFS 的附加 Bing 特定文档。
- [Yandex Maps - Transport integration](https://yandex.ru/support/m-maps/transport.html?lang=en#connect-display) - GTFS 的其他特定于 Yandex 的文档。

#### GTFS 库

该软件可以轻松使用多种语言的 GTFS 数据。

##### C
- [CGTFS](https://github.com/rakhack/cgtfs) - 用于读取静态 GTFS 源的 C 库。支持将解压的 feed 读取到应用程序内存或 SQLite 数据库中。
- [RRRR Rapid Real-time Routing](https://github.com/bliksemlabs/rrrr) - RRRR（通常发音为 R4）是 RAPTOR 公共交通路由算法的 C 语言实现。

##### C++
- [just_gtfs](https://github.com/mesozoic-drones/just_gtfs) - 用于读写 GTFS 的 C++17 仅标头库（在 [Valhalla](https://github.com/valhalla/valhalla) 中使用）。主要功能：快速读取和写入 GTFS 源、支持[扩展 GTFS 路线类型](https://developers.google.com/transit/gtfs/reference/extended-route-types)、简单地使用 GTFS 日期和时间格式。

##### C#
- [GTFS Feed Parser](https://github.com/OsmSharp/GTFS) - GTFS 解析器的 .Net/Mono 实现。

##### 去
- [Go GTFS Parser](https://github.com/geops/gtfsparser) - Go 的 GTFS 解析库。

##### 爪哇
- [OneBusAway GTFS Modules](https://github.com/OneBusAway/onebusaway-gtfs-modules/wiki) - 一个基于 Java 的库，用于读取、写入和转换 GTFS 格式的公共交通数据，包括数据库支持。

##### JavaScript
- [gtfs-sequelize](https://github.com/evansiroky/gtfs-sequelize) - Node.js 库使用sequelize.js 对静态 GTFS 进行建模。
- [gtfs-utils](https://github.com/public-transport/gtfs-utils) - 处理 GTFS 数据集的实用程序（例如，“扁平化”`calendar.txt` 和 `calendar_dates.txt`，计算行程的到达/出发时间）。
- [gtfs-via-postgres](https://github.com/derhuerst/gtfs-via-postgres) - 另一个使用 PostgreSQL 处理 GTFS 的工具。
- [Node-GTFS](https://github.com/BlinkTagInc/node-gtfs) - 从 GTFS 文件加载交通数据，解压缩并将其存储到 SQLite 数据库。提供一些查询机构、路线、站点、时间的方法。

##### PostgreSQL
- [gtfs-schema](https://github.com/tyleragreen/gtfs-schema) - GTFS 源的 PostgreSQL 架构。
- [gtfs-via-postgres](https://github.com/derhuerst/gtfs-via-postgres) - 另一个使用 PostgreSQL 处理 GTFS 的工具。

##### 鸭数据库

- [gtfs-via-duckdb](https://github.com/public-transport/gtfs-via-duckdb) - 通过将 GTFS 计划数据导入 DuckDB 数据库来分析它。

##### 蟒蛇
- [gtfsdb](https://github.com/OpenTransitTools/gtfsdb) - 用于将 GTFS 文件转换为关系数据库的 Python 库。
- [gtfs_functions](https://github.com/Bondify/gtfs_functions) - Python 包包含有用的函数，可从 GTFS 源创建地理空间可视化。
- [gtfs-segments](https://github.com/UTEL-UIUC/gtfs_segments) - Python 包，使用段以简洁的表格方式表示总线的 GTFS 数据。
- [gtfslib-python](https://github.com/afimb/gtfslib-python) - Python 中的开源库，用于读取 GTFS 文件并计算有关公共交通网络的各种统计数据和指标。
- [gtfsman](https://github.com/geops/gtfsman) - Python 中类似存储库的工具，用于管理和更新大量 GTFS 源。
- [gtfspy](https://github.com/CxAalto/gtfspy) - 使用 Python3 进行公共交通网络分析和旅行时间计算。与 Postgres/PostGIS、Oracle、MySQL 和 SQLite 兼容。由 [gtfspy-webviz](https://github.com/CxAalto/gtfspy-webviz) 使用。
- [GTFS Kit](https://github.com/mrcagney/gtfs_kit) - 用于分析通用运输供给规范 (GTFS) 数据的 Python 3.8+ 工具包。取代 GTFSTK。
- [Make GTFS](https://github.com/mrcagney/make_gtfs) - 一个 Python 库，用于根据基本路线信息生成 GTFS 源。
- [Mapzen GTFS](https://github.com/transitland/mapzen-gtfs) - 一个 Python GTFS 库，支持读取单个 GTFS 表，或构建图表来表示 Feed 中的每个机构。
- [multigtfs](https://github.com/tulsawebdevs/django-multi-gtfs) - 用于导入和导出 GTFS 的 Django 应用程序。
- [partridge](https://github.com/remix/partridge) - 一个基于 pandas DataFrames 构建的快速、宽容的 Python GTFS 阅读器。
- [transit_service_analyst](https://github.com/psrc/transit_service_analyst) - 支持交通服务分析的 Python 库。
- [TransitGPT](https://github.com/UTEL-UIUC/TransitGPT) - TransitGPT 是一款由 AI 驱动的生成式聊天机器人，使交通爱好者能够通过自然语言指令访问和分析通用交通馈送规范 (GTFS) 数据。

##### R
- [r-transit](https://github.com/r-transit) - R 中的 GTFS 工具集合。
- [gtfsio](https://github.com/r-transit/gtfsio) - 在 R 中读取和写入 GTFS 的功能快速且灵活。
- [mobdb](https://github.com/jasonad123/mobdb) - R 的功能是从 [Mobility Database](https://mobilitydatabase.org/) 中搜索、发现和访问交通源数据。
- [tidytransit](https://github.com/r-transit/tidytransit) - 使用 tidytransit 绘制公交站点和路线图、计算出行时间和公交频率并验证公交动态。 tidytransit 将通用交通馈送规范读取到 tidyverse 和简单特征数据帧中。

##### 红宝石
- [GTFS-viz](https://github.com/vasile/GTFS-viz) - 将一组 GTFS 文件转换为 SQLite 数据库 + GeoJSON 的 Ruby 脚本（[公交地图](https://github.com/vasile/transit-map) Web 应用程序所需）

##### 铁锈
- [gtfs-structure](https://github.com/rust-transit/gtfs-structure) - 该包提供 GTFS 结构和读取 GTFS 档案的帮助程序。

#### GTFS 转换器

各种静态计划格式与 GTFS 之间的转换器。

- [Chouette](https://enroute.atlassian.net/wiki/spaces/PUBLIC/pages/539426886/Chouette+Convert) - 在法语 Transmodel [NeTEX](https://transmodel-cen.eu/index.php/netex/) 和 GTFS 之间进行转换。
- [extract-gtfs-pathways](https://github.com/derhuerst/extract-gtfs-pathways) - 用于从 GTFS 数据集中以 GeoJSON 形式提取路径的命令行工具。
- [extract-gtfs-shapes](https://github.com/derhuerst/extract-gtfs-shapes) - 用于从 GTFS 数据集中将形状提取为 GeoJSON 的命令行工具。
- [GTFS-OSM-Sync](https://github.com/CUTR-at-USF/gtfs-osm-sync) - 一个 Java 工具，用于将 GTFS 格式的数据与 [OpenStreetMap.org](http://www.openstreetmap.org/) 同步。
- [gtfs-parser](https://github.com/ioTransit/gtfs-parser) - GTFS-PARSER 库是一个允许 javascript 解析 gtfs 并在客户端或服务器上创建 geojson 的库。
- [gtfs-service-area](https://github.com/cal-itp/gtfs-service-area) - 根据静态 GTFS 计算公交服务区。结果输出为单层 .geojson 文件。 [gtfs-to-geojson](https://github.com/BlinkTagInc/gtfs-to-geojson) 的 Docker 化版本。
- [GTFS-route-shapes](https://github.com/kotrc/GTFS-route-shapes) - 一个 Python 脚本，用于为 GTFS 存档中的每条公交路线生成单个 geoJSON 形状。
- [gtfs-to-geojson](https://github.com/BlinkTagInc/gtfs-to-geojson) - Javascript 工具，可将 GTFS 形状和停靠点中的交通数据转换为 geoJSON。这对于创建公交路线地图很有用。
- [gtfs2gps](https://github.com/ipeaGIT/gtfs2gps) - 一个 R 包，将 GTFS 格式的公共交通数据转换为“data.table”中类似 GPS 的记录，其中每行代表给定空间分辨率下每辆车的时间戳。
- [gtfs2emis](https://github.com/ipeaGIT/gtfs2emis) - 一个 R 包，用于根据通用交通供给规范 (GTFS) 数据估算公共交通车辆的排放水平。
- [gtsf](https://github.com/r-gtfs/gtsf) - R 中的通用交通 (GTFS) 简单（地理）特征 (sf) 可用于通过 GDAL 将 GTFS 转换为 Shapefile、GeoJSON 和其他格式。
- [hafas-generate-gtfs](https://github.com/derhuerst/hafas-generate-gtfs) *(work-in-progress)* – 用于从 HAFAS 端点生成 GTFS 转储的 Javascript 工具。
- [Hafas2GTFS](https://github.com/geops/hafas2gtfs) - Hafas2GTFS 转换器用 Python 编写，针对 SBB HAFAS 源进行了优化。
- [kml-to-gtfs-shapes](https://github.com/bdferris/kml-to-gtfs-shapes/tree/gh-pages) - 用于将折线从 KML 文件转换为 GTFS Shapes.txt 文件的 Javascript 工具。托管在 GitHub [此处](http://bdferris.github.io/kml-to-gtfs-shapes/)。
- [NeTEx-to-GTFS Converter Java](https://github.com/entur/netex-gtfs-converter-java) - 将 NeTEX 数据集转换为 GTFS 数据集。输入 NeTEx 数据集需要遵循 Nordic NeTEx Profile。
- [o2g](https://github.com/hiposfer/o2g) - 一个从 OpenStreetMap 中提取 GTFS 源的简单工具。
- [Open-Transport SYNTHESE Convertors](https://github.com/Open-Transport/synthese/wiki) - 转换 French-Transmodel、SIRI、NETeX、HAFAS、HASTUS、VDV452 等。
- [onebusaway-gtfs-to-barefoot](https://github.com/OneBusAway/onebusaway-gtfs-to-barefoot) - 一个 Java 工具，用于从 GTFS 文件创建 [Barefoot](https://github.com/bmwcarit/barefoot) 地图文件。
- [onebusaway-vdv-modules](https://github.com/OneBusAway/onebusaway-vdv-modules) - 用于处理 VDV 格式的交通数据的 Java 库，包括将 VDV-452 时间表数据转换为 GTFS。
- [osm2gtfs](https://github.com/grote/osm2gtfs) - 将 OpenStreetMap 数据和时间表信息转换为 GTFS。
- [transit_model](https://github.com/hove-io/transit_model) - 一个 Rust 库，用于与以下格式相互转换：GTFS、NTFS（对于 Navitia，请参阅[用于创建 API 的软件](#software-for-creating-apis)）、TransXChange（英国规范）、KV1（荷兰规范）、NeTEx（欧盟规范）。
- [Transmodel and IFF to GTFS](https://github.com/bliksemlabs/bliksemintegration) - 导入和同步 (Transmodel) BISON Koppelvlak1、IFF（由 HP/EDS 编写的格式，有点类似于 ATCO CIF）以导入铁路网络的时间表。内部伪 NETeX 数据结构允许导出到 GTFS，并且有概念验证可以导出到其他格式，例如 NETeX、GTFS 和 IFF。
- [Transporter-Project transxchange-to-gtfs](https://github.com/Transporter-Project/transxchange-to-gtfs) 用 Objective-C 编写的 TransXChange 到 GTFS 转换器。
- [TXC TransXChange publisher (UK Department for Transport)](https://www.gov.uk/government/publications/transxchange-publisher) - TXC TransXChange 发布器是一个独立的软件工具，可用于以易于阅读和打印的格式发布符合 TransXChange 的 XML 文档。
- [UK2GTFS](https://itsleeds.github.io/UK2GTFS/) - R 软件包，可将英国格式的 TransXchange（公共汽车、地铁、电车、渡轮）和 CIF（铁路）时间表转换为 GTFS。
- [OSMTracker](https://wiki.openstreetmap.org/wiki/OSMTracker_(Android)) - OSMTracker 是一款离线 GPS 跟踪应用程序，旨在收集兴趣点 (POI) 并记录 GPX 轨迹以供协作使用。

#### GTFS 数据收集和维护工具

- [AddTransit](https://addtransit.com/gtfs-transit-file.php) - SaaS（软件即服务）平台，用于以 GTFS 格式创建、编辑和发布时间表。
- [bus-router](https://github.com/atlregional/bus-router) - 使用 [Google Maps Directions API](https://developers.google.com/maps/documentation/directions/) 或 [OSRM](https://github.com/Project-OSRM/osrm-backend/wiki/Server-api) 的路由为 GTFS 生成缺失的 Shapes.txt 的 Python 脚本。
- [gtfs-blocks-to-transfers](https://github.com/TransitApp/GTFS-blocks-to-transfers) - 一个用于转换 GTFS 块的 Python 工具，通过将 [trip.block\_id](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md#example-blocks-and-service-day) 设置为一系列 [trip-to-trip 传输（提案）](https://github.com/google/transit/pull/303) 来定义。
- [GTFS Diff](https://transport.data.gouv.fr/tools/gtfs_diff) - GTFS Diff 是由transport.data.gouv.fr 创建的规范，旨在提供一种简单且统一的方式来表达 GTFS 文件之间的差异。
- [GTFS 编辑器](https://github.com/conceyal/gtfs-editor) 和 [Gtfs 数据管理器](https://github.com/conceyal/gtfs-data-manager) - 一个（自托管）基于 Web 的 GTFS 编辑框架。 （注意：该项目已被弃用，取而代之的是 [IBI 数据工具](https://github.com/ibi-group/datatools-ui)。）
- [GTFS Editor for Vagrant](https://github.com/laidig/vagrant-gtfs-editor) - 使用 [Vagrant](https://www.vagrantup.com/) 快速设置 GTFS 编辑器（上图）
- [static-GTFS-manager](https://github.com/WRI-Cities/static-GTFS-manager) - 一个（自托管）基于浏览器的用户界面，用于创建、编辑、导出静态 GTFS（请参阅[相关文章](https://groups.google.com/forum/#!topic/transit-developers/GFz5rTJTB0I)）。
- [TransitWand](https://github.com/conveyal/transit-wand) - 用于收集交通数据的开源网络和移动应用程序。使用它来创建 GTFS 源、捕获乘客数量或生成 GIS 数据集。
- [IBI Data Tools](https://github.com/ibi-group/datatools-ui) - 一个 Web 应用程序，用于处理 GTFS 编辑、验证、质量检查和部署到 OpenTripPlanner。 （结合并建立在已弃用的功能之上
- [Data-Tools Server](https://github.com/ibi-group/datatools-server) - IBI GTFS 数据管理平台的服务器。
- [IBI Data Tools Infra](https://github.com/cal-itp/ibi-datatools-infra) - 用于快速设置和运行上述 IBI Data Tools 项目的本地实例的工具。
- [GTFS.html](https://gtfs.pleasantprogrammer.com) - 一个完全基于浏览器的工具，用于查看 GTFS 源。用它来查看路线、站点、时刻表等。
- [pfaedle](https://github.com/ad-freiburg/pfaedle) - 使用 OpenStreetMap 数据对 GTFS 进行精确地图匹配
- [GTFS shape mapfit](https://github.com/HSLdevcom/gtfs_shape_mapfit) - Python 工具，适合 GTFS 形状文件并停止到给定的 OSM 映射文件。使用 [pymapmatch](https://github.com/tru-hy/pymapmatch) 进行匹配。
- [GTFS Builder](http://nationalrtap.org/Web-Apps/GTFS-Builder) - 一个免费的基于 Web 的应用程序，可帮助您创建 GTFS 文件。由国家农村交通援助计划 (RTAP) 维护。
- [gtfs-station-builder](https://github.com/kostjerry/gtfs-station-builder) - UI工具帮助构建车站内部结构（包括pathways.txt）
- [GTFS Text-to-Speech Tester](https://github.com/BlinkTagInc/node-gtfs-tts) - 一个命令行工具，使用文本转语音大声读取 GTFS 停靠站名称，以确定 stops.txt 中的 tts_stop_name 需要文本转语音值。
- [Spare GTFS-Flex Builder](https://sparelabs.com/en/spare-gtfs-flex-builder) - 一款免费工具，可帮助交通机构以 GTFS-Flex 格式轻松创建、管理和导出交通数据。
- [Swiftly](https://goswift.ly/) - 工具生成实时交通数据。
- [Chouette SaaS](https://bitbucket.org/enroute-mobi/chouette-core) - 生成GTFS Schedule数据的工具
- [Ara SaaS](https://bitbucket.org/enroute-mobi/ara) - 生成 GTFS 实时数据的工具。
- [Amarillo](https://github.com/mfdz/amarillo) - 聚合并增强拼车服务并将其发布为 GTFS(-RT)
- [GTFS Studio](https://gtfs.studio) - GTFS 源的在线编辑器
- [Uttu](https://github.com/entur/uttu) - Nplan 的后端，一个简单的时间表编辑器。
- [GTFS Express](https://gtfsexpress.com) - 用于编辑、验证和分析 GTFS 源（包括 Fares v2 和 GTFS-Flex）的 Web 应用程序，具有交互式时间表网格和地图编辑器、具有 AI 辅助自然语言查询的 SQL 控制台，以及通过 [MobilityData 的 gtfs-validator](https://github.com/MobilityData/gtfs-validator) 进行严格规范验证。

#### GTFS 合并工具
- [combine_gtfs_feeds](https://github.com/psrc/combine_gtfs_feeds) - 一种 Python 工具，用于将多个 gtfs feed 组合成一个 feed/数据集。
- [GTFS Kit](https://github.com/mrcagney/gtfs_kit) - 用于分析和合并通用交通供给规范 (GTFS) 数据的 Python 3.8+ 工具包。 [此处提供的有关如何聚合和清理提要的信息](https://mrcagney.github.io/gtfs_kit_docs/index.html#module-gtfs_kit.cleaners)。
- [Transitfeed merge function](https://github.com/google/transitfeed/wiki/Merge) - 一个 Python 库，具有合并两个不同 GTFS feed 的功能。
- [gtfsmerge](https://github.com/now8-org/gtfsmerge) - 用于将 GTFS ZIP 存档合并为一个的 Python 脚本。

#### GTFS 分析工具

- [GTFS Kit](https://github.com/mrcagney/gtfs_kit) - 用于分析通用运输饲料规范 (GTFS) 数据的 Python 3.6+ 工具包。取代 [GTFSTK](https://github.com/araichev/gtfstk)。
- [gtfstools](https://github.com/ipeaGIT/gtfstools) - 一组方便的工具，用于在 R 中编辑和分析 GTFS 格式的传输源。
- [transit_service_analyst](https://github.com/psrc/transit_service_analyst) - 支持交通服务分析的 Python 库。
- [Peartree](https://github.com/kuanb/peartree) - 一个 Python 库，用于将交通数据转换为有向图以进行网络分析。
- [R5: Rapid Realistic Routing on Real-world and Reimagined networks](https://github.com/conveyal/r5) - Conveyal 为多模式（公交/自行车/步行/汽车）网络开发的基于 Java 的路由引擎。目前，出于场景规划和分析目的，它在一个时间窗口内计划了多次旅行。相关的R包装包（[r5r](https://github.com/ipeaGIT/r5r/)）由IPEA独立开发。另请参阅 Higgins 等人的性能比较。 （2022），链接如下。
- [tidytransit](https://github.com/r-transit/tidytransit) - 用于将 GTFS 数据读入 tibbles 和简单功能数据帧的 R 包，用于绘制公交站点和路线、计算出行时间和公交频率以及验证公交提要。
- [transitr](https://github.com/tmelliott/transitr) - 用于实时构建交通网络并对其进行建模以获得车辆预计到达时间的 R 包
- [transit-intensity](https://github.com/ioTransit/transit-intensity) - 一个用 Go 编写的测量传输强度的简单项目。
- [Busbuzzard](https://github.com/bmander/busbuzzard) - 根据公交车辆的经验数据推断概率时间表。
- [City2Graph](https://github.com/c2g-dev/city2graph) - 一个 Python 库，用于将 GTFS 数据转换为用于网络分析和图神经网络 (GNN) 的图形表示。支持加载 GTFS 源、构建交通图、网络中心性分析以及多模式（街道 + 交通）网络上基于等时线的可达性分析。 [参见资源](https://city2graph.net/latest/examples/gtfs.html)
- [ESRI ArcGIS Public Transit Tools (GTFS)](https://github.com/Esri/public-transit-tools) - 在 ArcGIS 中处理公共交通数据的工具
- [GTFS-to-Chart](https://github.com/BlinkTagInc/gtfs-to-chart) - 根据 GTFS 数据创建显示公交路线上所有车辆的弦线图。
- [GTFS Display](https://codeberg.org/dancingCycle/gtfs-display) - 分析、监控和维护 GTFS 数据（[示例实例](https://www.swingbe.de/activity/gtfs-display/)）。
- [PTNA](https://wiki.openstreetmap.org/wiki/Public_Transport_Network_Analysis) - 公共交通网络分析是一个开源系统，用于查找和聚合 OSM 中映射的公共交通线路的信息。
- [Trak.Tools](https://github.com/SparksTheFolf/trak.tools) - 允许以选定的比例查看原始 GTFS 数据，以进一步增强可视化数据编辑并更轻松地查看。

#### GTFS 时间表发布工具

- [GTFS-to-HTML](https://gtfstohtml.com) - 直接从 GTFS 生成 HTML 或 PDF 格式的人类可读时间表。
- [Timetable Kit](https://github.com/neroden/timetable_kit) - 依赖于 [GTFS Kit](https://github.com/mrcagney/gtfs_kit) 的开源 Python 3.10 模块和脚本，旨在创建具有灵活布局的复杂打印/PDF 时间表。目前仅适用于 Amtrak 的 GTFS，但正在积极开发中。
- [TimeTablePublisher (TTPUB)](https://github.com/OpenTransitTools/ttpub) - TriMet 开发的网络发布系统，允许运输机构检查、修改原始调度数据并将其转换为易于阅读的时间表，以供客户参考

#### GTFS 验证器

- [Conveyal's gtfs-validator](https://github.com/conveyal/gtfs-validator) - 一种基于 OneBusAway GTFS 模块的基于 Java 的 GTFS 验证器，在 Java 中运行，比 Google 提供的验证器更快。
- [Conveyal's gtfs-lib](https://github.com/conveyal/gtfs-lib/) - Conveyal 是他们自己的 [gtfs-validator](https://github.com/conceyal/gtfs-validator) 的后继者，这是一个基于 Java 的库，用于通过磁盘支持的存储加载和保存任意大小的 GTFS 提要。
- [Google's feedValidator](https://github.com/google/transitfeed/wiki/FeedValidator) - Google 支持的基于 Python 的 GTFS 验证器。
- [GTFS Data Package Specification](https://github.com/Stephen-Gates/GTFS) - 使用 Good Tables 完成验证的数据包规范。包括数据包、模式、测试，并使用昆士兰东南部 GTFS 数据作为示例。
- [gtfstidy](https://github.com/patrickbr/gtfstidy) - 一个基于 Go 的工具，用于整理和验证 GTFS 源。
- [gtfsclean](https://github.com/public-transport/gtfsclean) - 用于检查、清理和最小化 GTFS 源的工具。 gtfstidy 的分支，带有一些尚未合并到上游的附加修复。
- [gtfs-validator-api](https://github.com/cal-itp/gtfs-validator-api) - 这个 Python 包是 [MobilityData/gtfs-validator](https://github.com/MobilityData/gtfs-validator) 的一个薄包装，它处理生成的中间文件并查找 gtfs-validator 的输出文件，以便可以为其指定特定名称或作为字符串返回。
- [GTFSVTOR](https://github.com/mecatran/gtfsvtor) - 一个用 Java 实现的开源 GTFS 验证器，根据 GPLv3 授权，由 [Mecatran](https://www.mecatran.com/) 维护。
- [MobilityData's gtfs-validator](https://github.com/MobilityData/gtfs-validator) - 开源 GTFS 验证器，规范地遵循由 [MobilityData](https://mobilitydata.org/) 维护的 Apache v2.0 许可的 Java 实现的 GTFS 规范。
- [gtfs-validator-metrics-service](https://github.com/mobidata-bw/gtfs-validator-metrics-service) - 使用 MobilityData 的 GTFS 验证器验证 GTFS 计划数据集，并将结果公开为 Prometheus/OpenTelemetry 指标。
- [Reflect GTFS Validator (hosted by Foursquare ITP)](https://reflect.foursquareitp.com) - [Foursquare ITP](https://www.foursquareitp.com) 提供的运输时间表和 GTFS 验证平台，其中包括基于 [gtfs-lib](https://github.com/conceyal/gtfs-lib/) 的免费、基于 Web 的 GTFS 验证器。
- [Transit App's gtfs-fares-v2-validator](https://github.com/TransitApp/gtfs-fares-v2-validator) - 一个 Python 工具，可根据 [草案规范](https://docs.google.com/document/d/19j-f-wZ5C_kYXmkLBye1g42U-kvfSVgYLkkG5oyBauY/edit#) 验证 GTFS-Fares-v2 数据。
- [Transport Validator](https://github.com/etalab/transport-validator/) - 在 [Rust](https://www.rust-lang.org/) 中实现的开源验证器。由[法国国家接入点](https://transport.data.gouv.fr/validation/) 使用。
- [gtfs-accessiblity-validator](https://github.com/BlinkTagInc/gtfs-accessibility-validator) - 验证 GTFS 文件中是否存在与可访问性相关的字段和文件。可以是命令行工具或node.js包。


### GTFS实时

- [GTFS-实时文档](https://github.com/google/transit/tree/master/gtfs-realtime)。
- [GTFS-realtime Autodoc](https://laidig.github.io/gtfs-rt-autodoc/index.html) - 自动生成 GTFS-realtime 文档，从官方 [GTFS-realtime 协议缓冲区规范](https://github.com/google/transit/blob/master/gtfs-realtime/proto/gtfs-realtime.proto) 生成，并包括一些扩展。

#### GTFS 实时库和演示应用程序

- [gtfs-realtime-bindings](https://github.com/google/gtfs-realtime-bindings) - 从官方 [GTFS-realtime 协议缓冲区规范](https://github.com/google/transit/blob/master/gtfs-realtime/proto/gtfs-realtime.proto) 生成的 Java、.NET、Node.js、Python 和 Ruby 的官方绑定。
- [gtfs-rt](https://crates.io/crates/gtfs-rt) - 用于读取、写入和操作 GTFS 实时数据的 Rust 箱
- [GTFS-realtime Exporter](https://github.com/OneBusAway/onebusaway-gtfs-realtime-exporter/wiki) - 一种基于 Java 的工具，可帮助生成和共享 GTFS 相关提要。
- [GTFS-realtime Alerts Producer Demo](https://github.com/OneBusAway/onebusaway-gtfs-realtime-alerts-producer-demo/wiki) - 一个基于 Java 的演示项目，用于生成 GTFS 实时服务警报。
- [GTFS-realtime Alerts Producer Web Application](https://github.com/OneBusAway/onebusaway-service-alerts) - 一个基于 Java 的 Web 应用程序，用于生成 GTFS 实时服务警报。
- [GTFS-realtime TripUpdates & VehiclePositions Producer Demo](https://github.com/OneBusAway/onebusaway-gtfs-realtime-trip-updates-producer-demo/wiki) - 一个基于 Java 的演示项目，用于生成 GTFS 实时 TripUpdates（预计到达）和车辆位置。
- [GTFS-realtime Vehicle Positions Consumer/Visualizer Demo](https://github.com/OneBusAway/onebusaway-gtfs-realtime-visualizer) - 一个基于 Java 的演示项目，用于使用 GTFS 实时车辆位置源并在地图上显示此信息。

#### GTFS 实时验证器

- [gtfs-realtime-validator](https://github.com/MobilityData/gtfs-realtime-validator) - GTFS 实时验证工具最初由南佛罗里达大学的[城市交通研究中心](https://www.cutr.usf.edu/) 开发，现在由 [MobilityData](https://mobilitydata.org/) 维护。

#### GTFS Realtime（和其他实时 API）归档工具

- [gtfsrdb](https://github.com/CUTR-at-USF/gtfsrdb) - 一个 Python 工具，支持读取 GTFS 实时数据并将其存档到数据库中
- [retro-gtfs](https://github.com/SAUSy-Lab/retro-gtfs) - 一个 Python 应用程序，从 Nextbus API 收集实时数据并将其存档为 GTFS 格式（即追溯 GTFS）。
- [Transi](https://gitlab.com/cutr-at-usf/transi) - 云原生 GTFS-RT/GTFS 归档系统。
- [GTFS-Realtime-Capsule](https://github.com/tsdataclinic/gtfs-realtime-capsule) - 一个命令行工具，用于抓取、规范化和归档实时公共交通数据。
- [gtfsdb_realtime](https://github.com/OpenTransitTools/gtfsdb_realtime) - 实时GTFS数据库加载器和ORM库

#### GTFS 实时转换器

- [SIRI to GTFS-realtime](https://github.com/OneBusAway/onebusaway-gtfs-realtime-from-siri-cli) - 一个基于 Java 的命令行实用程序，用于从 [SIRI 格式](https://www.siri.org.uk/) 转换为 GTFS-realtime
- [OrbCAD SQL Server to GTFS-realtime](https://github.com/CUTR-at-USF/HART-GTFS-realtimeGenerator/) - 一个基于 Java 的命令行实用程序，可从 OrbCAD SQL Server 提取车辆位置和行程更新信息，并将其导出为 GTFS 实时 TripUpdates 和 VehiclePositions 格式。
- [NextBus API to GTFS-realtime](https://github.com/OneBusAway/onebusaway-gtfs-realtime-from-nextbus-cli/wiki) - 一个基于 Java 的命令行实用程序，用于从 [NextBus API 格式](http://www.nextbus.com/xmlFeedDocs/NextBusXMLFeed.pdf) 转换为 GTFS-realtime。  请注意，NextBus 现在直接为其产品提供 GTFS 实时 API。  请参阅[Cubic 网站](http://nextbus.cubic.com/Products/Real-Time-Rider-Information) 和[此常见问题解答](https://medium.com/omnimodal/want-more-riders-open-up-your-nextbus-api-with-gtfs-realtime-7387c80f31e1#.pkuzizhl5)。
- [Syncromatics API to GTFS-realtime](https://github.com/CUTR-at-USF/bullrunner-gtfs-realtime-generator) - 一个基于 Java 的命令行实用程序，用于将 [Syncromatics API](http://www.syncromatics.com/) 格式转换为 GTFS 实时 TripUpdates 和 VehiclePositons。
- [KV6,15,17, and ARNU to GTFS-realtime](https://github.com/bliksemlabs/bliksemintegration-realtime) - 基于 Java 的工具，用于处理传入的 KV6、15、17 和 ARNU，并将它们与 RID 集成数据库中存在的静态传输数据进行匹配。然后继续将此数据导出为 ARNU RITinfo、GTFS（实时）和 KV78turbo
- [WMATA BusPositions API to GTFS-realtime](https://github.com/kurtraschke/wmata-gtfsrealtime) - 基于 Java 的工具，用于从 WMATA 的 [BusPositions API](https://developer.wmata.com/docs/services/54763629281d83086473f231/operations/5476362a281d830c946a3d68) 和警报 RSS 源进行转换[MetroAlerts](http://www.wmata.com/rider_tools/metro_service_status/rail_bus.cfm?) 到 GTFS 实时行程更新、车辆位置和警报源。
- [SEPTA API to GTFS-realtime](https://github.com/kurtraschke/septa-gtfsrealtime) - 基于 Java 的工具，用于将 [SEPTA](http://www.septa.org/) [实时公交车和铁路数据](http://www3.septa.org/hackathon/) 转换为 GTFS-realtime
- [CTA API to GTFS-realtime](https://github.com/kurtraschke/ctatt-gtfsrealtime) - 基于 Java 的工具，用于将 [CTA](http://www.transitchicago.com/) [Train Tracker 数据](http://www.transitchicago.com/developers/traintracker.aspx) 转换为 GTFS 实时。
- [Detroit DOT to GTFS-realtime](https://github.com/prashtx/ddot-avl) - 从 [DDOT's](http://www.detroitmi.gov/How-Do-I/Locate-Transportation/Bus-Schedules) TransitMaster 安装（数据库）中提取实时信息并转换为 GTFS-realtime
- [Live Transit Event Trigger](https://github.com/ipublic/live_transit_event_trigger) - 从 [Ride On's](http://www.montgomerycountymd.gov/dot-transit/) OrbCAD 数据库提取数据并导出为 GTFS-realtime。
- [SoundTransit to GTFS-realtime](https://github.com/bdferris/onebusaway-sound-transit-realtime) - 将文本文件源从 [Sound Transit](http://www.soundtransit.org/) 转换为 GTFS-realtime
- [Civic Transit](https://github.com/jestin/CivicTransit) - 屏幕抓取 [KCATA 的](http://www.kcata.org/) TransitMaster WebWatch 安装以生成 GTFS 实时源。
- [gtfs-realtime-translators](https://github.com/Intersection/gtfs-realtime-translators) - 一个基于 Python 的工具，用于将自定义到达 API 格式转换为 GTFS 实时格式。  截至 2019 年 7 月，它支持 LA Metro 和 SEPTA。
- [hafas-gtfs-rt-feed](https://github.com/derhuerst/hafas-gtfs-rt-feed) - 一个 Javascript 工具，用于从 HAFAS 端点生成 GTFS 实时源。
- [GTFS-realtime to SIRI-Lite](https://github.com/etalab/transpo-rt/) - 一个 [Rust](https://www.rust-lang.org/) 网络服务器，用于将多个 GTFS-RT 源转换为 SIRI-Lite API。
- [TransitClock](https://thetransitclock.github.io/) - Java 应用程序，可以使用原始车辆位置并以 GTFS 实时等格式生成预测时间。  以前称为“运输时间”。

#### GTFS 实时实用程序

- [bus_kalman](https://github.com/cmoscardi/bus_kalman) - 卡尔曼滤波器用于使用 NYC MTA 实时数据插值公交车行程时间。
- [Concentrate](https://github.com/mbta/concentrate) - 将多个来源的实时交通信息合并到单个输出文件中。维护者 [
马萨诸塞湾交通管理局 (MBTA)](https://github.com/mbta)。
- [gtfs-mcp](https://github.com/jdamcd/gtfs-mcp) - 实验性 MCP（模型上下文协议）服务器使法学硕士能够查询 GTFS 时间表和 GTFS-RT 数据，以回答交通问题或运行分析。
- [gtfs-realtime-test-service](https://github.com/CUTR-at-USF/gtfs-realtime-test-service) - 用于模拟 GTFS 实时提要内容的工具（例如，用于测试 GTFS 实时消费应用程序）。
- [GTFS-realtime Munin Plugin](https://github.com/OneBusAway/onebusaway-gtfs-realtime-munin-plugin) - 提供 [Munin](http://munin-monitoring.org/) 插件，用于记录有关 GTFS 实时源的信息。
- [GTFS-realtime Nagio Plugin](https://github.com/OneBusAway/onebusaway-gtfs-realtime-nagios-plugin) - 提供 [Nagios](https://www.nagios.org/) 插件用于监控 GTFS 实时源
- [GTFS-realtime Printer](https://github.com/laidig/gtfs-rt-printer) - 基于 Java 的实用程序，用于从 GTFS 实时文件或 URL 打印信息。
- [gtfs-rt-admin](https://github.com/conveyal/gtfs-rt-admin) - 用于管理 GTFS-RT 服务警报（JavaScript 和 Java）的管理工具。
- [gtfs-rt-differential-to-full-dataset](https://github.com/derhuerst/gtfs-rt-differential-to-full-dataset) - Javascript 工具，用于将“DIFFERENTIAL”增量数据的连续 GTFS 实时流转换为“FULL_DATASET”转储。
- [gtfs-rt-dump](https://github.com/kurtraschke/gtfs-rt-dump) - 将协议缓冲区格式转换为纯文本，以便于以纯文本形式轻松查看 GTFS 实时提要（用于调试目的）
- [gtfs-rt-inspector](https://public-transport.github.io/gtfs-rt-inspector/) - 用于检查和分析任何（启用 CORS 的）GTFS 实时源的 Web 应用程序。 [GitHub](https://github.com/public-transport/gtfs-rt-inspector) 上开源。
- [GTFS Data Pipeline for TfNSW Bus Datasets](https://github.com/teckkean/GTFS-Data-Pipeline-TfNSW-Bus) - 为 TfNSW 的 GTFS 静态和实时数据集开发的数据管道。使用该管道生成的数据集已用于验证 TfNSW 通过公共交通信息和优先系统 (PTIPS) 的交通信号优先请求的性能。
- [manual-gtfsrt](https://github.com/pailakka/manual-gtfsrt) - 一个基于 Go 的工具，提供从可编辑 JSON 创建的 GTFS-RT 提要。
- [print-gtfs-rt-cli](https://github.com/derhuerst/print-gtfs-rt-cli) - Javascript 工具，用于从标准输入读取 GTFS 实时提要，打印人类可读的或作为 JSON。
- [transitcast](https://github.com/OpenTransitTools/transitcast) - 使用 GTFS 和 GTFS-RT 车辆位置反馈生成每辆车从计划停车移动到计划停车所需的估计过渡时间，并将这些时间记录在“observed_stop_time”表中。这些记录稍后可用于训练机器学习模型以进行车辆行驶预测。由 TriMet 创建，作为 [FTA IMI 项目](https://trimet.org/imi/program.htm) 的一部分。
- [transit-feed-quality-calculator](https://github.com/CUTR-at-USF/transit-feed-quality-calculator) - 一个 Java 项目，使用 [gtfs-realtime-validator](https://github.com/CUTR-at-USF/gtfs-realtime-validator) 评估大量交通源的质量，从全局目录 ([TransitFeeds.com/OpenMobilityData.org](https://openmobilitydata.org/)) 获取源 URL。
- [Transit Network Model](https://github.com/tmelliott/TransitNetworkModel) - 一种使用 GTFS 实时车辆位置、粒子滤波器和卡尔曼滤波器生成预测的工具。
- [GTFS Realtime Display](https://codeberg.org/dancingCycle/gtfs-rt-display) - 分析、监控和维护 GTFS 实时数据。 [示例实例](https://www.swingbe.de/activity/gtfs-rt-display/)
- [GTFS Realtime Prediction Accuracy metrics](https://docs.google.com/document/d/1-AOtPaEViMcY6B5uTAYj7oVkwry3LfAQJg3ihSRTVoU/edit#heading=h.j27shba7rlk6) - GTFS-Realtime 的有用性能指标。

### 西瑞

- [SIRI API](https://github.com/OneBusAway/onebusaway/wiki/SIRI-Resources) - 从 v1.0 和 v1.3 [SIRI](https://www.siri.org.uk/) 模式生成的 Java 类。
- [SIRI 2.0 API](https://github.com/laidig/siri-20-java) - 从 v2.0 [SIRI](https://www.siri.org.uk/) 模式生成的 Java 类。
- [SIRI to GTFS-realtime](https://github.com/OneBusAway/onebusaway-gtfs-realtime-from-siri-cli/wiki) - 一个基于 Java 的命令行实用程序，用于从 [SIRI 格式](https://www.siri.org.uk/) 转换为 GTFS-realtime。
- [SIRI 2.0 Autodoc](https://laidig.github.io/siri-20-java/doc/) - 从带注释的 SIRI 2.0 架构定义（非常好）自动生成文档。
- [King County Metro Legacy AVL to SIRI](https://github.com/bdferris/onebusaway-king-county-metro/tree/master/onebusaway-king-county-metro-legacy-avl-to-siri) - 基于 Java 的工具，用于将 [King County Metro](http://metro.kingcounty.gov/) 旧版 AVL 格式转换为 SIRI。
- [SIRI REST Client](https://github.com/CUTR-at-USF/SiriRestClient/wiki) - 一个开源 Android 库，用于与实时交通数据的 RESTful SIRI 接口进行交互，例如 [MTA Bus Time API](http://bustime.mta.info/wiki/Developers/SIRIIntro) 当前使用的库。
- [SIRI 1.3 POJOs (Android-compatible)](https://github.com/CUTR-at-USF/onebusaway-siri-api-v13-pojos/wiki) - Android 兼容的普通旧 Java 对象 (POJOS)，用于 SIRI v1.3 API 的数据绑定（反序列化 XML/JSON）响应。  由 [SIRI REST 客户端](https://github.com/CUTR-at-USF/SiriRestClient/wiki) 使用。
- [pysiri2validator](https://github.com/laidig/pysiri2validator) - 用 Python 3 编写的 SIRI 2.0 简单验证器。
- [Edwig](https://github.com/af83/edwig) - 用于实时公共交通数据交换的 golang 服务器，使用 SIRI 协议。
- [BISON](https://bison.dova.nu/standaarden/nederlands-siri-profiel) - 荷兰实施 SIRI。

### 其他多模态数据格式

#### 广泛采用
- [APDS](https://www.allianceforparkingdatastandards.org/) - 停车数据标准联盟：由[国际停车协会(IPI)](https://www.parking.org/)、[英国停车协会(BPA)](http://www.britishparking.co.uk/)和[欧洲停车协会(EPA)](http://www.europeanparking.eu/)组成。 APDS 是一个非营利组织，其使命是开发、推广、管理和维护统一的全球标准，使组织能够在全球范围内跨平台共享停车数据。
- [DATEX](https://datex2.eu/) - 道路交通和旅行信息的欧盟数据标准。
- [GBFS](https://gbfs.org/) - 通用自行车共享规范：共享自行车、共享踏板车、共享轻便摩托车和共享汽车实时信息的开放数据标准。
- [MDS](https://github.com/openmobilityfoundation/mobility-data-specification) - 移动数据规范：一种为市政当局和移动服务提供商实施实时数据共享、测量和监管的格式。其目的是确保政府有能力执行、评估和管理提供商。由[开放移动基金会](https://www.openmobilityfoundation.org/) 维护。
- [NeTex](http://netex-cen.eu/) - 一种通用 XML 格式，设计用于在 [CEN 标准流程](https://www.cencenelec.eu/european-standardization/european-standards/) 管理的分布式系统之间交换复杂的静态传输数据。
- [TODS](https://ods.calitp.org/) - 交通运营数据标准：司机、调度员和规划人员执行交通运营所使用的交通时间表的标准格式。
- [TOMP](https://github.com/TOMP-WG/TOMP-API) - 交通运营商移动即服务提供商 API：供交通运营商和移动即服务提供商使用的 API 标准，用于运营商发现、行程规划、最终用户交互、预订和支付。

#### 试点或开发阶段
- [CurbLR](https://github.com/curblr/curblr-spec) - 路边法规规范。
- [Dyno-Demand](https://github.com/osplanning-data-standards/dyno-demand) - 一种基于 GTFS 的出行需求数据格式，专注于个人乘客*需求*，适用于动态网络建模，由旧金山县交通管理局、LMZ LLC 和 UrbanLabs LLC 开发。
- [Dyno-Path](https://github.com/osplanning-data-standards/dyno-path) - （正在开发中 - 请参阅[这篇文章](https://github.com/osplanning-data-standards/GTFS-PLUS/pull/52#issuecomment-331231000)）个人乘客*轨迹*的数据。
- [GTFS-plus](https://github.com/osplanning-data-standards/GTFS-PLUS) - 基于 GTFS 的交通网络格式，适用于由普吉特海湾地区委员会、UrbanLabs LLC、LMZ LLC 和旧金山县交通管理局开发的动态交通建模的“车辆和容量数据”。
- [GTFS-ride](https://github.com/ODOT-PTS/GTFS-ride) - 俄勒冈州交通部和俄勒冈州立大学合作开发的开放、固定路线公交乘客数据标准。
- [GTFS-stat](https://github.com/osplanning-data-standards/GTFS-STAT) - GTFS 交通网络的扩展，包含包含由 UrbanLabs LLC 和旧金山县交通管理局开发的性能数据的附加文件。
- [GMNS](https://github.com/zephyr-data-specs/GMNS) - 通用建模网络规范：一种共享可路由道路网络文件的格式，设计用于多模式静态和动态交通规划和运营模型。 Volpe/FHWA 与 Zephyr 基金会合作。
- [GTNS](https://zephyrtransport.org/trb17projects/7-general-travel-network-specification/) - 通用出行网络规范：用于共享出行需求模型网络的规划数据规范。
- [IXSI](https://github.com/RWTH-i5-IDSG/ixsi) - 用于在出行信息系统和共享系统（共享汽车、共享单车）之间交换信息的接口。
- [MTLFS](https://github.com/vta/Managed-and-Tolled-Lanes-Feed-Specification) - 管理和收费车道供给规范：关于架构的提案，该模式包含管理和收费车道收费供给规范 (MTLFS)，并定义[圣克拉拉谷交通管理局](http://www.vta.org/) 开发的所有这些文件中使用的字段。
- [MaaS API](https://github.com/maasglobal/maas-tsp-api/blob/master/specs/Booking.md) - 一组开放文档和测试套件，定义了与 MaaS 兼容的 API。
- [NCHRP 08-119](http://apps.trb.org/cmsfeed/TRBNetProjectDisplay.asp?ProjectID=4543) - 本研究的目的是制定交通界在收集、管理和共享交通规划和运营的静态和实时数据时使用和采用的标准和/或指南。
- [OMX: The Open Matrix data file format](https://github.com/osPlanning/omx) - 二维数组对象和相关元数据的结构化集合，可用于交通建模行业。
- [OJP](https://github.com/VDVde/OJP) - 打开旅程规划器。
- [OSDM](https://github.com/UnionInternationalCheminsdeFer/OSDM) - 开放式销售和分销模式：旨在大幅简化铁路旅行客户的预订流程，并降低分销商和铁路承运商的复杂性和分销成本。包含离线模型和在线 API 的规范。由[国际铁路联盟 (UIC)](https://github.com/UnionInternationalCheminsdeFer) 维护。
- [SAE Shared and Digital Mobility Committee](http://articles.sae.org/15799/) - 似乎正在为汽车共享和交通网络公司（TNC）/拼车制定数据标准。
- [shared-row](https://github.com/d-wasserman/shared-row) - SharedStreets Reference 的通行权 (ROW) 规范。
- [TCRP G-16](http://apps.trb.org/cmsfeed/TRBNetProjectDisplay.asp?ProjectID=4120) - 本研究的目的是为参与提供需求响应型运输的实体制定交易数据的技术规范。  预计完工日期为 2018 年底。
- [TIDES](https://github.com/TIDES-transit/TIDES) - 交通 ITS 数据交换规范 (TIDES) 是一项拟议工作，旨在为历史交通 ITS 数据（包括 AVL、APC 和 AFC 数据）创建标准数据结构、API 和数据管理工具。
- [OpenStop](https://wiki.openstreetmap.org/wiki/OpenStop) - OpenStop 是一款免费应用程序，可将有关公共交通站点的障碍物和其他无障碍属性的信息添加到 OpenStreetMap。
- [JOSM Plugins - PT Assistant](https://wiki.openstreetmap.org/wiki/JOSM/Plugins/PT_Assistant) - 该插件根据一组标准验证公共交通路线，并在可能的情况下提出修复它们的方法。
- [JOSM Validator Rules](https://josm.openstreetmap.de/wiki/Rules) - JOSM验证器（标签检查器）可以基于MapCSS定制不同的规则。
- [OSM Relatify](https://wiki.openstreetmap.org/wiki/Relatify) - OSM Relatify 是一种简化维护公共交通关系流程的工具。
- [OpenStreetMap Route Editor](https://osm-simple-route-editor.kyle.kiwi/) - OpenStreetMap 中高效编辑路线关系的工具 - OSM
- [Prism](https://github.com/Jungle-Bus/prism) - Prism 是一个从 OpenStreetMap 中提取公共交通数据的工具。
- [Open Street Map Public Transport Parser](https://github.com/cualbondi/osmptparser) - 打开街道地图公共交通解析器
- [Sketch Line](http://www.overpass-api.de/public_transport.html) - 一种根据 OSM 数据创建传输图的工具。

### 用于创建 API 的软件

您可以设置该软件来提供交通和多式联运数据的 API。

- [GraphHopper 路由引擎](https://github.com/graphhopper/graphhopper/#public-transit) OpenStreetMap 的开源路由引擎。将其用作 Java 库或服务器。
- [gtfs-server](https://github.com/denysvitali/gtfs-server) - 一个用 Rust 编写的 Web 服务器，使用 PostGIS 作为后端，通过 HTTP 端点提供 GTFS 数据
- [hafas-rest-api](https://github.com/public-transport/hafas-rest-api) - 将 [HAFAS](https://de.wikipedia.org/wiki/HAFAS) 端点公开为 REST API。
- [Linked Connections](http://linkedconnections.org/) - 开源、可扩展的多式联运路线规划引擎，允许客户端执行路线规划算法（而不是服务器）。使用 GTFS 数据。
- [Mobroute](http://sr.ht/~mil/mobroute) - Mobroute 是一种通用 FOSS 公共交通路由器（例如行程规划器）Go 库和 CLI，通过直接从交通机构本身获取时间表 (GTFS) 数据（源自 [Mobility Database](https://database.mobilitydata.org/)）来工作。它可用于基于设备上的 GTFS 数据快速运行和测试路由请求（通过其 CLI），也可以作为库嵌入以将 GTFS 路由添加到现有导航应用程序中。
- [MOTIS](https://motis-project.org) - MOTIS 专为处理大规模时间表和 OpenStreetMap 数据而开发，集成了步行、骑自行车、共享出行（电动滑板车、自行车共享、汽车共享）和公共交通等多种交通方式，以提供优化的路线解决方案。 MOTIS 针对高性能和低内存使用量进行了优化。这使得能够在经济实惠的硬件上进行全球规模的部署。它支持 GTFS、GTFS-RT、NeTEx、SIRI、GBFS 和 OpenStreetMap 数据。
- [Navitia](https://github.com/hove-io/navitia) 是 [Navitia.io](http://www.navitia.io/) live API 背后的开源引擎。
- [OneBusAway](http://onebusaway.org/) - 一个 Java 应用程序，它使用 GTFS 和 GTFS-Realtime（以及[其他格式](https://github.com/OneBusAway/onebusaway-application-modules/wiki/Real-Time-Data-Configuration-Guide)）并将它们转换为易于使用的 REST API。
- [OpenTripPlanner](http://www.opentripplanner.org/) - 一个开源平台，用于多模式和多机构旅程规划，以及返回有关多模式图的信息（使用 GTFS 和 [OpenStreetMap](http://www.openstreetmap.org/) 等数据源）。
- [pyBikes](https://github.com/eskerda/pybikes) - 为 [CityBikes](http://api.citybik.es) 提供支持的软件，可获取全球自行车共享系统信息
- [Simple Transit Api](https://github.com/ioTransit/simple-transit-api) - 在 Golang 中开始使用 GTFS api 的简单方法。
- [Transitous](https://transitous.org) - 社区运营的免费开放的公共交通路线服务。
- [Iran Railway-Trains](https://github.com/keyone2693/IRTrainDotNet) - 伊朗铁路列车 (Raja-Fadak-Safir) 全部为 DotNet (Api-WebService) 的一揽子服务
  

## 共享数据

访问 GTFS 以及其他交通和多式联运数据集合的位置。

#### 第 3 方 GTFS URL 目录
- [The Mobility Database](https://mobilitydatabase.org/) - JSON 和 CSV 文件 [在 GitHub 上](https://github.com/MobilityData/mobility-database-catalogs)，是全球 2000 多个移动数据集的存储库。包含 OpenMobilityData/TransitFeeds.com 的内容。
- [Transitland](https://transit.land/) - 许多交通机构 GTFS 数据集的社区可编辑列表。还提供了一个 API 来访问 JSON/GeoJSON 数据，以及一个尝试数据的平台。
- [TransitData.io](https://transitdata.io/) - 拉丁美洲部分地区的 GTFS 数据列表。必须直接联系网站维护人员才能访问提要，因为它们不公开。
- [~~OpenMobilityData~~ (Deprecated)](https://openmobilitydata.org/) - GTFS 和 [GTFS-RT](https://openmobilitydata.org/search?q=gtfsrt) 源列表。 [存档和验证](https://openmobilitydata.org/p/capital-metro/24) GTFS 提供并允许您通过浏览器预览 [GTFS](https://openmobilitydata.org/p/capital-metro/24/latest) 和 [GTFS-RT](https://openmobilitydata.org/p/capital-metro/495)。以前称为 TransitFeeds.com。 [MobilityData 宣布](https://database.mobilitydata.org/#h.u71vp6xgkckf) 该产品将于 2022 年初终止，关闭日期待确定。

#### 交通运输机构数据档案
- [CapMetrics](https://github.com/scascketta/CapMetrics) - 奥斯汀交通机构 (CapMetro) 的历史车辆位置。数据由 Go 守护进程 [capmetricsd](https://github.com/scascketta/capmetricsd) 收集。
- [Bus Observatory API](https://api.busobservatory.org/) - 从世界各地的交通系统收集的有关车辆移动和状态的实时数据的公共档案。

#### 国家政府数据集
- [National Transit Database (USA)](https://www.transit.dot.gov/ntd) - 由联邦运输管理局管理的美国运输系统的信息和统计数据。
- [transport.data.gouv (France)](https://transport.data.gouv.fr/) - 法国交通生态系统的数据平台。
- [European long-distance transport operators (EU) *(Unofficial)*](https://github.com/public-transport/european-transport-operators) - 可用 API 端点、GTFS 源和客户端库的非官方列表

#### 专有（非标准）供应商 API
- [Transport API](https://www.transportapi.com/) - 用于英国聚合交通数据的 REST API。  收费访问。
- [NextBus API](http://www.nextbus.com/xmlFeedDocs/NextBusXMLFeed.pdf) - REST API，为购买 NextBus 硬件和/或软件的机构提供实时车辆、路线、停靠站和到达数据。
- [Navitia.io](http://www.navitia.io/) - REST API，用于美国和欧盟的行程规划、停靠时刻表、等时线等。 [Navitia](https://github.com/hove-io/navitia) 是实时 API 背后的开源引擎。
- [CityBikes](http://api.citybik.es) - 用于聚合来自世界各地的共享单车数据的 REST API。由 [pyBikes](https://github.com/eskerda/pybikes) 提供支持。
- [HAFAS](https://de.wikipedia.org/wiki/HAFAS) - [HaCon](https://www.hacon.de) 的专有公共交通管理软件（[端点列表](https://gist.github.com/derhuerst/2b7ed83bfa5f115125a5)）
- [Citymapper API](https://docs.external.citymapper.com/api/) - 用于交通行程规划、实时交通数据以及步行、骑自行车、踏板车出行时间的 REST API。
- [TripGo API](https://developer.tripgo.com) - [SkedGo](https://skedgo.com) 用于多模式旅程规划和实时数据的 REST API。

#### 众包交通数据
- [Citylines.co](https://www.citylines.co) - 绘制交通系统地图的协作平台，重点关注其历史演变。可以从 [citylines.co/data](https://www.citylines.co/data) 下载 GeoJSON 或 CSV 格式的数据。
- [OpenStreetMap (OSM)](https://www.openstreetmap.org) - 用于绘制世界地图的协作平台，包括交通、运输和路线数据。
- [GTFS-Hub](https://github.com/mfdz/gtfs-hub) - 经过社区测试，可能质量/内容得到增强，部分合并或过滤了（目前是德国）运输机构的 GTFS 源。由 [MITFAHR|DE|ZENTRALE](https://github.com/mfdz) 维护。

#### 用于软件测试的示例 GTFS 和 GTFS Realtime 数据集
- [sample-gtfs-feed](https://github.com/public-transport/sample-gtfs-feed) - 用于测试的虚构 GTFS 数据集。
- [Transitland GTFS and GTFS Realtime unit tests](https://github.com/interline-io/transitland-lib) - 用于测试 Transitland 处理 GTFS 和 GTFS 实时解析和验证的 [transitland-lib](https://github.com/interline-io/transitland-lib) 库：

## 使用数据

### 消费者应用程序

人们在乘坐公共交通工具时使用的应用程序。

#### 网络应用程序（开源）
- [MOTIS](https://motis-project.org) - MOTIS 移动平台的 Web UI（路线、地理编码、实时交通地图等）。
- [Catenary Maps](https://catenarymaps.org) - 实时和时间表全球公共交通地图和导航软件，用 Rust 和 Svelte 编写。
- [Instabus](http://instabus.org) - 奥斯汀 (CapMetro) 公共交通的实时地图。完全没有服务器/后端依赖，并且完全在 GitHub 页面上运行。
- [OpenTripPlanner Client GWT](https://github.com/mecatran/OpenTripPlanner-client-gwt) - OpenTripPlanner 的基于 Google Web Toolkit 的 Web 界面
- [OpenTripPlanner.js](https://github.com/conveyal/otp.js) - 基于 Javascript 的 OpenTripPlanner 客户端（不再开发）
- [OTP-UI React Component Library](https://github.com/opentripplanner/otp-ui) - React Javascript 组件库，可用于构建旅行计划 Web 应用程序。请参阅 [Storybook](http://www.opentripplanner.org/otp-ui) 进行演示。
- [GTFS-realtime Alerts Producer Web Application](https://github.com/OneBusAway/onebusaway-service-alerts) - 一个基于 Java 的 Web 应用程序，用于生成 GTFS 实时服务警报。
- [HRT BUS Web app](https://github.com/Code4HR/hrt-bus-api) - HRT Bus API 通过应用程序编程接口发布来自 Hampton Roads Transit 的实时公交数据，供开发人员从中制作应用程序。
- [Transit-Map](https://github.com/vasile/transit-map) - Web 应用程序，使用公共交通时间表在地图上对车辆（标记）进行动画处理，以插入其沿路线（折线）的位置。
- [Transitive.js](https://github.com/conveyal/transitive.js) - 使用 Leaflet 或 D3 创建公交路线的可自定义 Web 地图图层。
- [Google I/O Transport Tracker](https://github.com/googlemaps/transport-tracker) - 显示 Google I/O 会议的班车到达时间，基于开源 [transport-tracker 项目](https://github.com/googlemaps/transport-tracker)。  注意：要自行实施此操作，您需要 [Google Maps API 高级计划许可证](https://developers.google.com/maps/pricing-and-plans/)。
- [1-Click]([http://camsys.software/products/1-click](https://github.com/camsys/oneclick)) - 虚拟“行程聚合器”，汇集各种可用模式的信息：公共交通、私人交通、铁路、拼车、拼车、志愿者、辅助交通以及步行和骑自行车。
- [Bustime](https://busti.me) - 通过 WebSocket 更新进行公共交通实时监控。开源 [在 GitHub 上](https://github.com/norn/bustime)。
- [Transit Tracker](https://transittracker.ca/#/) - 加拿大大蒙特利尔和多伦多的实时车辆位置
- [GTFS Builder](http://nationalrtap.org/Web-Apps/GTFS-Builder) - 一个免费的基于 Web 的应用程序，可帮助您创建 GTFS 文件。由国家农村交通援助计划 (RTAP) 维护。
- Dede - 独立且通用的乘客信息系统 (PIS) 绘制实时移动地图。带有 GTFS-Realtime 格式的车辆位置实体的消息源或 [Dede 应用程序](https://github.com/dancesWithCycles/dede-android) 可以用作数据源。
- [MBTA tile-server](https://github.com/mbta/tile-server) - 用于创建 Docker 容器的脚本，该容器封装了开发用于 MBTA.com 的地图图块所需的所有元素
- [Cadê Meu Busão](https://tarifazerobh.org/cade-meu-busao/) - 实时跟踪从巴西贝洛奥里藏特出发的公交巴士。 [GitHub](https://github.com/tarifazero/monitoramento) 上开源。
- [Tiramisu Transit](https://github.com/CMU-RERC-APT/tiramisu3-pr) - 由卡内基梅隆大学开发和部署的自适应移动交通应用程序，可显示实时公交车到达信息。不再维护。
- [OsmAnd](https://wiki.openstreetmap.org/wiki/OsmAnd) - OsmAnd 是一款 GPS 导航和地图应用程序，可在许多 Android 和 iOS 智能手机和平板电脑上运行，具有可选的离线地图和转向...

#### 网络应用程序（闭源）
- [TransitScreen](http://transitscreen.com/) - 所有当地交通选择的自定义实时显示
- [Citylines.co](https://www.citylines.co) - 绘制交通系统地图的协作平台，重点关注其历史演变。
- [Bikeshare Map](http://bikes.oobrien.com/) - 全球所有共享单车站点的现状
- [Bongo](http://ebongo.org) - 爱荷华市、科拉尔维尔和爱荷华大学的实时交通跟踪。将三个不同的交通系统合并到一个 UI 中。
- [CityMapper Webapp](https://citymapper.com/nyc) - 真正精美的网络应用程序，包含 30 多个城市的旅行计划和路线状态。
- [TransSee](https://www.transsee.ca/) - 基于实际出行时间、车辆位置、时间表和地图的实时交通预测。高级版可让您访问时间表、车辆位置、停靠站、时间表遵守情况、图表和图表的详细历史记录。支付额外费用即可对此数据运行自定义查询。
- [YourStop](http://yourstop.info) - 适合移动设备的网络应用程序，它使用 GTFS 源并显示实时和预定的停靠站行程。与 MBTA、YRT/Viva 和马里兰州 MTA 共同推出。
- [DC MetroHero](https://dcmetrohero.net) - 华盛顿特区 WMATA Metrorail 和 Metrobus 系统的实时车辆位置以及到达和出发信息。提供 WebApp、Android 和 iOS 应用程序。

#### 本机应用程序（开源）

- [Arrivals KMP](https://github.com/jdamcd/arrivals-kmp) - Kotlin 多平台实时交通到达应用程序，带有 macOS 工具栏、CLI 和桌面目标。支持例如MTA、TfL、英国国家铁路或任何 GTFS-RT 源。
- [Home Assistant](https://github.com/home-assistant/core/tree/dev/homeassistant/components/gtfs) Home Assistant 0.17 中引入了通用传输源规范 (GTFS) 集成，已被 70 个活跃安装使用。
- [KDE Itinerary](https://apps.kde.org/itinerary/) - 用于计划旅行的应用程序（桌面版和安卓版）。它可以查找公共交通路线、离线存储、为您的行程添加活动、查看火车站的平面图等等。 [源代码](https://invent.kde.org/pim/itinerary), [GitHub](https://github.com/KDE/itinerary)
- [MACS Transit Android App](https://github.com/yeSpud/MACSTransitApp) - 一款适用于阿拉斯加费尔班克斯 MACS Transit 系统的 Android 设备的公交车追踪应用程序。使用 RouteMatch API。
- [Next Train - Connecticut](https://github.com/data-creative/NextTrainCT) - 一个 React-native 移动应用程序，用于搜索康涅狄格州 Shore Line East 运输机构发布的火车时刻表。依赖于 [Next Train API](https://github.com/data-creative/next-train-api) 的部署。
- [Offi Directions](https://gitlab.com/oeffi/oeffi) - 一款 Android 应用程序，可为欧洲及其他地区的交通当局提供行程计划、时间表、实时出发时间和中断信息。
- OneBusAway 应用程序 - [Android](https://play.google.com/store/apps/details?id=com.joulespersecond.seattlebusbot) [*(源代码)*](https://github.com/OneBusAway/onebusaway-android), [Fire Phone](http://www.amazon.com/gp/mas/dl/android?p=com.joulespersecond.seattlebusbot) [*(源代码）*]（https://github.com/OneBusAway/onebusaway-android），[iOS]（https://itunes.apple.com/us/app/onebusaway/id329380089）[*（源代码）*]（https://github.com/OneBusAway/onebusaway-ios），[Windows电话](https://www.microsoft.com/en-us/store/apps/onebusaway/9nblggh0cbd9) [*(源代码)*](https://github.com/OneBusAway/onebusaway-windows-phone)，[Google Glass GDK](https://github.com/OneBusAway/onebusaway-android/pull/219) [*(源代码）*]（https://github.com/OneBusAway/onebusaway-android/pull/219），[Alexa技能]（https://www.amazon.com/OneBusAway/dp/B01ELVUYCW/）[*（源代码）*]（https://github.com/OneBusAway/onebusaway-alexa）
- [OpenTripPlanner Android](https://github.com/CUTR-at-USF/OpenTripPlanner-for-Android/wiki) - [OpenTripPlanner](http://www.opentripplanner.org/) 的 Android 应用程序
- [OpenTripPlanner iOS](https://github.com/opentripplanner/OpenTripPlanner-iOS) - [OpenTripPlanner](http://www.opentripplanner.org/) 的 iOS 应用程序
- [opentripplanner-client-library](https://github.com/CUTR-at-USF/opentripplanner-client-library) - 一个 Kotlin 多平台库，用于发出 API 请求并解析来自 OpenTripPlanner v2 服务器的响应，以获取适用于 Android、iOS 和 Web 的旅行计划、自行车租赁信息和服务器元数据。
- [Transito](http://git.sr.ht/~mil/transito) - 自由和开放源码软件与数据提供商无关的公共交通应用程序，让您可以使用公开可用的公共 GTFS 源（源自 [移动数据库](https://database.mobilitydata.org/)）在不同地点之间进行路线选择。利用 [Mobroute Go API](http://sr.ht/~mil/mobroute)，Transito 应用程序可让您直接在手机上执行路由计算。跨平台应用程序目前支持 Android 和 Linux。
- [Tiramisu Transit](https://github.com/CMU-RERC-APT/tiramisu3-pr#mobile-app-client) - 由卡内基梅隆大学开发和部署的自适应移动交通应用程序，可显示实时公交车到达信息。使用 Ionic 框架编写。不再维护。
- [Transportr](https://github.com/grote/Transportr) 一款 Android 应用程序，使用 [public-transport-enabler](https://github.com/schildbach/public-transport-enabler) 连接到全球许多不同的交通网络。
- [Trufi App](https://github.com/trufi-association/trufi-app) - 使用 [OpenTripPlanner](http://www.opentripplanner.org/) 的跨平台 Flutter 应用程序

#### 本机应用程序（闭源）

- [Transit](http://transitapp.com/)
- [CityMapper](https://citymapper.com/)
- [Moovit](http://moovitapp.com/)
- [Transit Display](http://transitdisplay.com/) - 多模式和实时交通显示软件。
- [Ualabee](https://ualabee.com/company/) - 社区驱动的行程规划器，注重用户交互，用户可以报告异常情况、上传图片、编辑公交数据以及与其他乘客聊天。
- [ÖPNV 导航器](https://navigatorapp.net/)
- [TripGo](https://tripgo.com/)

### 硬件

实验和生产运输硬件。

- [Arrivals LED](https://github.com/jdamcd/arrivals-led) - Python 渲染器可驱动 Raspberry Pi 上的 128×32 HUB75 LED 矩阵来显示实时公交到达情况。
- [Bus Tracking GPS](https://github.com/herrdragon/busTrackingGps) - 迈阿密跟踪公交巴士的廉价开源解决方案原型的代码。
- [Train departure Display](https://github.com/chrisys/train-departure-display) - 基于 Raspberry Pi Zer0 的近乎实时的微型英国火车站火车出发标志复制品。

### 软件开发工具包
- [motis-client](https://www.npmjs.com/package/@motis-project/motis-client) - MOTIS API TypeScript 客户端
- [motis-java-client](https://github.com/bileto/motis-java-client) - MOTIS API Java 客户端
- [motis-fptf-client](https://www.npmjs.com/package/@motis-project/motis-fptf-client) - [MOTIS](https://github.com/motis-project/motis) 的 [友好公共交通格式 (FPTF)](https://github.com/public-transport/Friendly-public-transport-format) 客户端是 [hafas-client](https://github.com/public-transport/hafas-client/) 的直接替代品和/或[db-vendo-client](https://github.com/public-transport/db-vendo-client/)。
- [TripKit](https://github.com/alexander-albers/tripkit) - TripKit 是一个 Swift 库，用于从公共交通提供商获取数据。
- [KPublicTransport](https://invent.kde.org/libraries/kpublictransport) - 用于访问实时公共交通数据和执行公共交通旅程查询的 C++ 库。
- [SkedGo's TripKit SDKs](https://developer.tripgo.com) - 适用于 Android、iOS 和 React 的开源 SDK，用于访问 [SkedGo](https://skedgo.com) 的 TripGo API，包括行程规划 UI 组件。

### 可视化
#### 基于 GTFS 的可视化

- [All Transit](https://all-transit.com) - 使用 Mapbox GL JS、Deck.gl 和 Transitland 实现交互式 GTFS 路线和时间表动画（针对美国城市）。 Github 存储库[此处](https://github.com/kylebarron/all-transit)。
- [BusGraphs Access Analyzer](https://gitlab.com/publictransitanalytics-pub/readme) - 用于测量真实和假设的固定路线公共交通网络提供的访问，并以多种方式可视化和分解该访问的 Web 应用程序。
- [fastest-bus-analysis-in-the-west](https://github.com/vta/fastest-bus-analysis-in-the-west) - 一个 python Pandas 脚本，结合了乘客量/APC、Swiftly 速度和停留数据、公交车站库存、GTFS 和地理空间形状，以创建逐站、逐条路线、时间分组的可过滤数据集以进行交叉分析。  然后，该数据集在 [Tableau](https://public.tableau.com/profile/vivek7797#!/vizhome/stopsandspeedanalysiss/Story1) 中进行可视化，以帮助 VTA 规划人员找到通过站点合并和专用车道等提速方法使公交和铁路网络更快、更可靠的地方。
- [GTFS City](https://github.com/ttezer/gtfs-city) - 开源 GTFS 可视化和分析工具，具有行程模拟、等时线分析、热图、停靠点连接和路线规划。
- [gtfspy-webviz](https://github.com/CxAalto/gtfspy-webviz) - 使用 [gtfspy](https://github.com/CxAalto/gtfspy) 对 GTFS 数据进行动画和可视化的 Web 应用程序。
- [gtfs-to-geojson](https://www.transit.chat/gtfs-to-geojson) - 一个简单的在线转换器，用于将 gtfs 转换为带有提要列表的 geojson。
- [gtfs-visualizations](https://github.com/cmichi/gtfs-visualizations) - 用于可视化 GTFS 数据集路径的开源 NodeJS 应用程序。
- [Local Transit](https://www.localtransit.app) - 使用 QGIS 创建的公共交通频率的地图可视化。
- [Mapnificent](https://www.mapnificent.net/) - 显示在给定时间内您可以乘坐公共交通工具到达的区域。开源 [在 GitHub 上](https://github.com/mapnificent/mapnificent)，位于 https://www.mapnificent.net/。
- [MIT COAXS](http://mittransportanalyst.github.io/) - 使用基于可达性的利益相关者参与共同创意规划交通走廊（使用 [OpenTripPlanner Analyst](http://www.opentripplanner.org/analyst/) 显示路线场景）。
- [MOTIS](https://motis-project.org/) - 多式联运移动信息系统，由 [Transitous.org 社区](https://transitous.org) 运行的全球服务器
- [MTA Frequency](http://www.tyleragreen.com/maps/new_york/) - 使用 [Transitland](https://transit.land/) 构建的纽约市地铁和公交车的频率可视化。
- [Pantograph](https://pantographapp.com) - 一种实时探索交通系统的方法。
- [SEPTA Rail OTP Report](https://apps.phor.net/septa/) - 使用 GTFS 的在线实时性能报告和深入分析工具。
- [简单公交地图]([https://transit.chat/simple-transit-map](https://github.com/ioTransit/simple-transit-map)) - 如何托管和更新网络地图的在线示例。
- [Simple Transit Site](https://transit.chat/simple-transit-site) - 有关如何从 gtfs 创建公交网站的在线示例 [Github](https://github.com/ioTransit/simple-transit-site)
- [TNExT](https://github.com/ODOT-PTS/TNExT) - Transit Network Explorer Tool (TNExT) 是一款基于 Web 的软件工具，专为俄勒冈州区域和全州交通网络的可视化、分析和报告而开发。
- [Toronto Transit Explorer](https://github.com/sidewalklabs/totx) - 一个 Java 应用程序，可可视化多伦多市的交通、自行车和步行可达性。使用 [R5](https://github.com/conceyal/r5) 的修改版本进行路由。
- [Transit Vis](https://github.com/zackAemmer/transit_vis) - 一种可视化工具，用于显示源自 King County Metro GTFS-RT 源 (OneBusAway API) 的性能指标。可在[此处](https://www.transitvis.com/)查看。用于[本文](https://link.springer.com/article/10.1007/s12469-022-00291-7)。
- [TransitFlow](https://github.com/transitland/transitland-processing-animation) 使用Processing 和Transitland 对世界各地的GTFS 数据进行动画处理。
- [TransitLens](https://transit-lens.com/gtfs-map-viewer/) - 基于浏览器的 GTFS 查看器，用于在交互式地图上可视化路线、停靠点和形状。包括服务日历分析、结构化数据表和 GeoJSON/KML 叠加支持。无需设置。
- [TRAVIC Transit Visualization Client](http://tracker.geops.ch/) - 基于静态 GTFS 数据（有时是实时数据）可视化车辆移动。支持260多个城市。  geOps 组织的 Github 帐户位于[此处](https://github.com/geops)。
- [Traze](https://traze.app/) by [Veridict](https://www.veridict.com) - 来自世界各地的公共交通车辆的可视化。即使代理机构无法提供实时更新，也可以与其他用户协作获取实时更新。基于许多来源，包括 GTFS 和 GTFS-RT。 （以前称为 Livemap24）。
- [Visualizing MBTA Data](http://mbtaviz.github.io/) - 显示人们如何使用波士顿地铁系统的交互式图表。
- [GTFS Viz 🚉](https://github.com/gabrielAHN/gtfs-viz) - 一个 Web 应用程序，使用 [duckdb-wasm 🦆](https://duckdb.org/docs/api/wasm/overview.html) 在浏览器上大规模可视化 GTFS 数据，而无需客户端后端。
- [QGIS - GTFS plugins](https://plugins.qgis.org/search/?q=gtfs) - QGIS GTFS 插件列表

#### 公交地图创建
- [Brand New Subway](https://jpwright.github.io/subway/) - 一款互动交通规划游戏，让玩家可以随心所欲地改变纽约地铁系统。
- [BENO Metro Mapm Creator](https://beno.uk/metromapcreator/#) - 一个非常老式但经典的交通地图创建者。
- [Tennessine Metro Designer](https://tennessine.co.uk/metro/) - 一位现代且美观的交通地图设计师。
- [loom](https://github.com/ad-freiburg/loom) - 用于自动生成地理正确或示意性交通地图的软件套件。
- [Metro Map Maker](https://metromapmaker.com/) - 一个开源且简单的地铁地图制作软件。
- [MetroDreamin'](https://metrodreamin.com/explore) - 一种现代的开源软件，允许用户创建、保存、点赞以及与代理共享交互式交通地图。
- [Rail Map Generators](https://wongchito.github.io/RailMapGenerator) - 用于生成各种城市公共交通系统风格的铁路地图和信息面板的工具。
- [MetroSets](https://metrosets.ac.tuwien.ac.at/) - 一个灵活的网络工具，可以使用地铁地图隐喻来可视化集合系统。基于这篇[论文](https://www.computer.org/csdl/journal/tg/2021/02/09224192/1nV7Me0F3Lq)
##### 用于制作交通可视化的通用绘图应用程序

- [Adobe illustrator](https://www.adobe.com/ca/products/illustrator.html) - 业界领先的矢量图形软件（需要会员计划）。
- [Inkscape](https://inkscape.org/) - 类似于 Adob​​e Illustrator 的免费设计工具。
##### 用于制作交通可视化的通用 GIS 应用程序
 - [Felt](https://felt.com/) - 一款美观的现代 GIS 软件。
 - [Google Mymaps](https://www.google.ca/maps/about/mymaps/) - 使用“Google 我的地图”创建和共享自定义地图。
 - [Google Earth](https://www.google.com/earth/about/) - 使用世界上最详细的国家级应用程序之一创建和共享自定义地图。

#### 公交地图聚合
 - [UrbanRail.Net](http://www.urbanrail.net/) - 全球城市轨道交通（地铁、有轨电车、通勤铁路）参考地图，包含详细的最新信息。
 - [OpenRailwayMap](https://www.openrailwaymap.org/) - 使用 OpenStreetMap 数据绘制的全球铁路地图。
 - [AllRailMap](https://www.allrailmap.com/) - 另一张使用 OpenStreetMap 数据的全球铁路地图。
 - [European Railway Atlas](https://europeanrailwayatlas.com/) - 可供购买的欧洲铁路地图参考书。
 - [Rail Transit Maps](http://www-personal.umich.edu/~yopopov/rrt/railroadmaps/) - 覆盖欧洲（尤其是俄罗斯）的铁路地图集。
 - [Tramscale](https://alexander.co.tz/tramscale/) - 网站概述了显示世界各地有轨电车系统规模的地图。
 - [Timelines](https://alexander.co.tz/timelines/) - 比较世界各地快速交通项目的时间表。
 - [Metrolinemap](https://www.metrolinemap.com/) - 世界地铁系统的交互式地图。
 - [Metrocyclopaedia](https://blog.csaladen.es/metro/ ) - 世界各地地铁系统的 3D 地图（使用 Metrolinemap 中的数据）。
 - [RailFansCanada](https://map.railfans.ca/) - 交互式系统地图详细介绍了加拿大不同城市铁路系统的现在和未来。
 - [North American Transit](https://www.google.com/maps/d/u/0/viewer?mid=1GAXiiEp8a62LvZNDueYN76NPTCoUxvdx&ll=43.71257881237152%2C-79.385523993394&z=11) - 北美所有客运铁路地图，包括（城际铁路、地铁、有轨电车和旅游线路）
 - [Intercity Rail map](https://asm.transitdocs.com/) - Amtrak 和 Via 列车的实时位置和时刻表信息地图
 - [Indian Railways Map](https://indiarailinfo.com/atlas) - 印度主要铁路网络的交互式地图。
 - [National Rail Network Map](https://www.arcgis.com/apps/mapviewer/index.html?webmap=96ec03e4fc8546bd8a864e39a2c3fc41) - 该地图显示了美国铁路线的范围和所有权，包括客运和货运线。
 - [Ferrocarta](https://ferrocarta.net/) - 一系列地图，涵盖巴西、加拿大和法国的所有客运铁路网络。
 - [Train Lookout](https://trainlookout.com/) - 一款可轻松记录、绘制地图和分享您的火车旅程的工具。
 - [Australian Rail Maps](http://www.railmaps.com.au/) - 国家、州和城市级别的详细澳大利亚铁路地图。
 - [Steam Engine "IS"](https://parovoz.com/maps/supermap/) - 苏联铁路地图。
 - [Carto.Metro](https://cartometro.com/) - 全球城市（尤其是法国）的地铁和有轨电车网络的详细地图。
 - [Railway Stations](https://map.railway-stations.org/) - 世界各地火车站的照片。
 - [INAT](https://www.inat.fr/maps/) - 全球地铁系统美观的静态地图。
 - [Transit Maps](https://transitmap.net/) - 对世界各地交通地图设计的批评和评论。
 - [Transit Explorer](https://www.thetransportpolitic.com/transitexplorer/) - 包含世界各地固定导轨交通的地图。
- [英国铁路](https://www.merrittcartgraphic.co.uk/british_railways.html) 英国铁路网络的交互式地图。
- [TransitLand Map](https://www.transit.land/map) - 公交服务的全球地图（具有 GTFS Feed）。
 - [DB InfraGO](https://geovdbn.deutschebahn.com/pgv/public/map/isr.xhtml) - 德国铁路基础设施互动地图。
 - [SNCF Carte interactive](https://www.sncf-reseau.com/fr/carte/carte-interactive-reseau-ferre-francais-0) - 法国铁路基础设施交互式地图。
 - [Project Mapping](https://www.projectmapping.co.uk/index.html) - 英国和全球铁路网络的示意图。
 - [China Railway Map](http://cnrail.geogv.org/enus/about) - 中国铁路客运系统在线互动地图，显示车站和铁路信息。
 - [Canadian Rail Atlas](https://rac.jmaponline.net/canadianrailatlas/) - 加拿大近 43,000 公里铁路网的用户友好型交互式地图。
 - [The Rail Map](https://www.therailmap.com/) - 使用来自 OpenStreetMap 的数据制作的包含北美火车线路的交互式地图。
 - [JR pass](https://www.jrpass.com/map#) - 日本干线铁路交互式地图。
- [Openptmap](https://wiki.openstreetmap.org/wiki/Openptmap) - openptmap 显示公共交通线路。
- [OSMTransportViewer](https://gileri.github.io/OSMTransportViewer/) - 使用OSM Overpass API获取网络数据
- [PTMap](https://ptmap.plepe.at/#lat=48.20200&lon=16.33800&zoom=15) - PTMap 显示输入 OpenStreetMap 的公共交通路线。
- [Unroll](https://jungle-bus.github.io/unroll/) - 公共交通路线
- [Jungle Bus Map](https://jungle-bus.github.io/map/#15/48.8584/2.34846) - 用于在 OpenStreetMap 中查看交通站点详情的网络地图。
- [AccraMobile3](https://wiki.openstreetmap.org/wiki/AccraMobile3) - Accra Mobile 3 是一个于 2017 年 7 月启动的项目，旨在为阿克拉交通部 (DoT) 绘制加纳阿克拉所有 Tro tro 线路的地图...
- [OpenStationMap](https://openstationmap.org/#17/52.51022/13.43477/8.8/55) - 公共交通车站（包括轨道和站台）室内的展示。
- [gbfs R package](https://github.com/simonpcouch/gbfs) - 与 R 中的 GBFS 源接口的函数，允许用户为指定城市/自行车共享项目保存和积累整洁的 .rds 数据集。

### 代理工具

交通机构的工具。  另请参阅 [GTFS 数据收集和维护工具](#gtfs-data-collection-and-maintenance-tools) 了解 GTFS 特定的工具。

- [Remix by Via](https://ridewithvia.com/solutions/remix) - 一个网络应用程序，可让交通机构轻松规划路线。
- [Next Train API](https://github.com/data-creative/next-train-api) - 将任何 GTFS 源作为 JSON API 提供服务。交通机构和开发人员都可以将开源代码部署到他们自己的 Heroku 服务器上。
- [AC Transit RestroomFinder](https://github.com/actransitorg/ACTransit.RestroomFinder) - 使用 GPS 和屏幕地图为公交车运营商和现场工作人员精确定位最近的授权卫生间。
- [AC Transit Training and Education Department (TED) application](https://github.com/actransitorg/ACTransit.Training) - 尽管该系统支持新课程和学徒计划，但该应用程序支持学区对运输和维护员工的培训操作，主要是公交车运营商和重型客车机械师（学徒和旅程）的职位。
- [AC Transit Customer Relations application (CusRel)](https://github.com/actransitorg/ACTransit.CusRel) - 用于处理客户问题和反馈的公共交通票务系统：带通知的部门间路由、部门/人员分配、简单的工作流程、票务搜索、预制报告、每日提醒等。
- [PTV Lines](https://www.ptvgroup.com/en/products/ptv-lines) - 基于云的公共交通软件，用于线路规划和公共交通服务优化
- [TransAM]([http://camsys.software/products/transam](https://github.com/camsys/transam_core)) - 公共交通机构的开源资产管理平台。
- [RidePilot](https://github.com/camsys/ridepilot) - 开源计算机辅助调度和调度 (CASD) 软件系统，可满足小型人力服务运输机构的需求。
- [TNExT](https://github.com/ODOT-PTS/TNExT) - Transit Network Explorer Tool (TNExT) 是一款基于 Web 的软件工具，专为俄勒冈州区域和全州交通网络的可视化、分析和报告而开发。
- 路线趋势（[webapp](https://metrotransitmn.shinyapps.io/route-trends/)、[GitHub](https://github.com/metrotransit/route-trends)) - 一个 R Shiny 应用程序，用于提取客流时间序列，并根据 [STL 方法](https://otexts.com/fpp2/stl.html) 返回季节性、趋势和剩余分量，并进行预测，包括基于这些分量的不确定性。  由 [Metro Transit](https://www.metrotransit.org/)（明尼阿波利斯-圣保罗）赞助。
- [TBEST](https://tbest.org/) - TBEST（公交登机估计和模拟工具）致力于开发一种基于 GIS 的多方面建模、规划和分析工具，它将社会经济、土地利用和公交网络数据集成到一个平台中，用于基于场景的公交客流量估计和分析。由佛罗里达州交通部资助。免费使用但不开源。
- [RideSheet](https://docs.ridesheet.org) - 一种基于电子表格的简单工具，适用于小型需求响应型交通 (DRT) 服务。

## 资源

### 社区

提问和查找其他社区资源的地方。

- [MobilityData Slack chat](https://share.mobilitydata.org/slack) - 聊天室包括频道 #gtfs、#gtfs-validators #mobility-database #gtfs-realtime #gtfs_best-practices #gtfs-pathways #gtfs-fares #gtfs-flex #trb-transit-data。
- [交通开发商邮件列表](https://groups.google.com/forum/#!forum/transit-developers)
- [OpenTripPlanner](https://github.com/opentripplanner/OpenTripPlanner) 社区
    - [OpenTripPlanner 用户邮件列表](https://groups.google.com/forum/#!forum/opentripplanner-users)
    - [OpenTripPlanner 开发人员邮件列表](https://groups.google.com/forum/#!forum/opentripplanner-dev)
- OneBusAway
    - [OneBusAway 开发者邮件列表](http://groups.google.com/group/onebusaway-developers)
    - [OneBusAway API 邮件列表](http://groups.google.com/group/onebusaway-api)

#### 地方和区域团体
- [Transit Techies NYC](https://transittechies.nyc/) - 纽约市的面对面/在线混合聚会。 [演讲者名单](https://transittechies.nyc/past) 包括此存储库的许多贡献者。
- [German Open Transport Meetup](https://github.com/transportkollektiv/meetup/wiki) - [双周](https://hackmd.okfn.de/opentransportmeetup#) 德语开放交通社区在线聚会。
- [German Open Transport Data Quality Meetup](https://github.com/transportkollektiv/meetup/wiki) - 德语开放交通社区每两个月一次的在线聚会，致力于数据质量。
- [Open Train Community](https://github.com/hasadna/OpenTrainCommunity) - Opentrain 存储库，用于以色列铁路列车延误数据的社区数据分析。

### 研究与评论

与开放交通数据相关的博客文章和报告。

#### 博客文章

- [When(ish) is my bus? Data and code](https://github.com/mjskay/when-ish-is-my-bus) - Whenish后面的数据和代码（R）是我的总线？数据包括三天的历史车辆位置和调查结果。
- ["Legacy AVL system? It's okay, join the club." by Kurt Raschke](https://kurtraschke.com/2015/01/legacy-avl-export) - 讨论将遗留 AVL 系统数据转换为 GTFS 实时格式的选项。
- ["GTFS Best Practices now available!" by Sean Barbeau](https://medium.com/@sjbarbeau/gtfs-best-practices-now-available-88ac67194233) - 讨论 GTFS 等开放数据格式的一些挑战以及 2017 年初推出的 GTFS 最佳实践，以帮助解决数据质量问题。
- ["What's new in GTFS-realtime v2.0" by Sean Barbeau](https://medium.com/@sjbarbeau/whats-new-in-gtfs-realtime-v2-0-cd45e6a861e9) - 讨论 GTFS-realtime v1.0 的不足以及 v2.0 的改进。
- ["AVL, CAD, and Real-Time Passenger Info for Beginners" by Tony Laidig](http://transitdata.net/avl-cad-and-real-time-passenger-info-for-beginners/) - 概述用于跟踪车辆的技术。
- ["Visualizing Better Transportation: Data & Tools" by Steve Pepple](https://medium.com/@stevepepple/visualizing-better-transportation-data-tools-e48b8317a21c) - 旧金山湾区和北美其他城市的交通相关数据和工具的集合，最初是在旧金山 ARUP 的 2018 年交通周活动中收集和讨论的。
- ["How to use GTFS data to track transit vehicles in realtime" by Tom Camp](https://www.ably.io/blog/gtfs-data-track-transit-vehicles-realtime) - 使用GTFS和GTFS Realtime提供持续的实时更新。

#### 学术论文

- [Tang et al. - "Ridership effects of real-time bus information system: A case study in the City of Chicago"](https://www.sciencedirect.com/science/article/pii/S0968090X12000022) - 在伊利诺伊州芝加哥进行的实验表明，当乘客可以通过短信或电子邮件获取实时信息时，乘客数量略有增加。
- [Kay et al. - "When(ish) is my bus? User-centered Visualizations of Uncertainty in Everyday, Mobile Predictive Systems"](https://www.mjskay.com/papers/chi_2016_uncertain_bus.pdf) - 论文试图回答“我们如何传达交通预测中的不确定性？”的问题。解释问题、现有解决方案并设计一个[更好的界面，让用户知道何时到达公交车站](https://github.com/mjskay/when-ish-is-my-bus/blob/master/quantile-dotplots.md#quantile-dotplots)。
- [Watkins et al. - "Where Is My Bus? Impact of mobile real-time information on the perceived and actual wait time of transit riders"](https://www.sciencedirect.com/science/article/pii/S0965856411001030) - 在华盛顿州西雅图进行的实验表明，当乘客通过移动应用程序访问实时信息时，他们会感觉公交车等待时间更短。
- [Brakewood et al. - “An experiment evaluating the impacts of real-time transit information on bus riders in Tampa, Florida”](https://www.sciencedirect.com/science/article/pii/S0965856414002146) - 佛罗里达州坦帕市的对照实验表明，与没有实时信息的乘客相比，通过移动应用程序访问实时信息的乘客的等待时间减少了近 2 分钟。  掌握实时信息的乘客的焦虑和挫败感也有所减少，并且对代理的接受度也更好。
- [Brakewood et al. - "The impact of real-time information on bus ridership in New York City"](https://www.sciencedirect.com/science/article/pii/S0968090X15000297) - 纽约市的实验表明，当向乘客提供实时信息时，长途路线的乘客量会增加。
- [Brakewood 和 Watkins - “实时交通信息给乘客带来的好处的文献综述”](https://www.tandfonline.com/doi/full/10.1080/01441647.2018.1472147?scroll=top&needAccess=true) (2018) - 许多不同研究的概述，着眼于实时交通信息的好处。
- [Gramacki et al. - "gtfs2vec - Learning GTFS Embeddings for comparing Public Transport Offer in Microregions"](2021) - 使用 Uber 的 H3 空间索引和机器学习的方法来识别城市中公共交通服务质量“相似”的区域。源代码可在[GitHub](https://github.com/pwr-inf/gtfs2vec)获取。
- [Higgins et al. - "Calculating place-based transit accessibility: Methods, tools and algorithmic dependence" (2022)](https://doi.org/10.5198/jtlu.2022.2012) - 比较用于计算步行和公共交通可达性的软件工具，包括 ArcGIS Pro、Emme、R5R 和 OpenTripPlanner。
- [Aemmer et al. - "Measurement and classification of transit delays using GTFS-RT data"](https://link.springer.com/article/10.1007/s12469-022-00291-7) - 提出了一种从通用交通供给规范的实时 (GTFS-RT) 组件中提取交通性能指标并将其聚合到道路段的方法。与 [Transit Vis](https://github.com/zackAemmer/transit_vis) 一起使用，可在[此处](https://www.transitvis.com/)查看。

#### 政府报告
- [APTA Policy Development and Research - Public Transportation Embracing Open Data](http://www.apta.com/resources/reportsandpublications/Documents/APTA-Embracing-Open-Data.pdf) - APTA 关于开放交通数据的好处和挑战的讨论（以下 TCRP 报告的简短摘要）。
- [TCRP Synthesis 115 - 开放数据：交通机构的挑战和机遇](http://onlinepubs.trb.org/Onlinepubs/tcrp/tcrp_syn_115.pdf) (2015) - 一份探讨开放交通数据的好处和挑战的综合报告。
- [TCRP 研究报告 213：公共交通机构数据共享指南 – 现在和未来](http://www.trb.org/Main/Blurbs/180188.aspx) (2020) - 该报告旨在帮助机构做出有关共享数据的决策，包括如何评估收益、成本和风险。
- [TCRP G-16 Development of Transactional Data Specifications for Demand-Responsive Transportation (In progress)](http://apps.trb.org/cmsfeed/TRBNetProjectDisplay.asp?ProjectID=4120) - 本研究的目的是为参与提供需求响应型运输的实体制定交易数据的技术规范。  预计完工日期为 2018 年底。

#### 社区维护的列表
- [Vendors Providing GTFS Creation/Maintenance services](https://docs.google.com/spreadsheets/u/1/d/1Gc9mu4BIYC8ORpv2IbbVnT3q8VQ3xkeY7Hz068vT_GQ/pubhtml) - [此处](http://goo.gl/forms/YDbPSPmufS) 添加新供应商。
- [Entities Providing Transportation Software Development Consulting Services](https://docs.google.com/spreadsheets/u/1/d/1n44CNMCK1vt1nyrsdYz-KD_hYxUMNIm6Me69M6ROBIg/pubhtml) - 添加新实体[此处](http://goo.gl/forms/cc6kcVERuP)。

## 许可证

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png)](http://creativecommons.org/publicdomain/zero/1.0/)

在法律允许的范围内，[MobilityData](https://mobilitydata.org/)、[南佛罗里达大学](http://www.usf.edu/) 的[城市交通研究中心](https://www.cutr.usf.edu/) 和 [Luqmaan Dawoodjee](https://github.com/luqmaan) 已放弃本作品的所有版权以及相关或邻接权。

## 关于
这是仅供参考的社区资源 - 列出项目/产品并不意味着认可。

该列表是由像您这样的开源社区贡献者构建和维护的！ [MobilityData](https://mobilitydata.org/) 负责管理该项目。

#Awesome-transit 最初由 [Luqmaan Dawoodjee](https://github.com/luqmaan) 创建，并由[南佛罗里达大学](http://www.usf.edu/) 的[城市交通研究中心](https://www.cutr.usf.edu/) 管理了几年，然后该项目转移到 MobilityData。


