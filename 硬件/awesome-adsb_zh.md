<!-- GITHUB LOGO PLACEHOLDER -->

<div align="center">

<!-- title -->

<!--lint ignore double-link-->

# <a style="color: inherit" href="https://github.com/rickstaa/awesome-adsb">Awesome ADS-B</a> [![Awesome](https://awesome.re/badge.svg)](https://awesome.re) [![GitHub contributors](https://img.shields.io/github/contributors/rickstaa/awesome-adsb?color=geen)](https://github.com/rickstaa/awesome-adsb/graphs/contributors) [![GitHub Repo stars](https://img.shields.io/github/stars/rickstaa/awesome-adsb)](https://github.com/rickstaa/awesome-adsb/stargazers) <!-- omit in toc -->

> **Note**
> Just type `adsb.cool` to go here.

<!-- subtitle -->

A curated list of awesome [ASD-B](https://en.wikipedia.org/wiki/Automatic_Dependent_Surveillance%E2%80%93Broadcast) tools, projects, Docker images, resources and other shiny things 📡.

<!-- image -->

<a href="https://www.sportys.com/blog/ads-b-101-what-you-need-know" target="_blank" rel="noopener noreferrer">
  <img width="600" src="https://www.sportys.com//media/wysiwyg/blog/13_-_Navigating_and_Automation_in_the_21st_Century.png" alt="ADSB.cool Logo"/>
</a>

<!-- description -->

**广播式自动相关监视 (ADS-B)** 是一种监视技术和电子[显眼](https://en.wikipedia.org/wiki/Airborne_collision_avoidance_system#Aircraft_collision_avoidance)形式，其中[飞机](https://en.wikipedia.org/wiki/Aircraft)通过[卫星]确定其位置导航](https://en.wikipedia.org/wiki/Satellite_navigation) 或其他传感器并定期广播它，使其能够被跟踪。

</div>

<!-- TOC -->

<!-- omit in toc -->
## 内容

- [文档和快速入门](#docs-and-quickstarts)
- [书籍和文章](#books-and-articles)
- [ADS-B 聚合器](#ads-b-aggregators)
  - [面向开源](#open-source-orientated)
  - [社区驱动](#community-driven)
  - [Non-profits](#non-profits)
  - [Commercial](#commercial)
  - [Other](#other)
- [Software](#software)
  - [General](#general)
  - [Feeding](#feeding)
  - [Visualisation](#visualisation)
  - [Apps](#apps)
  - [Social](#social)
- [ADS-B 衍生数据](#ads-b-derived-data)
- [Hardware](#hardware)
  - [SBC](#sbc)
  - [Receivers](#receivers)
  - [Filters](#filters)
  - [Antennas](#antennas)
- [Follow](#follow)

<!-- CONTENT -->

## 文档和快速入门

<!-- List ADS-B documentation and quickstarter guides -->

- [ADS-B Docker guide](https://sdr-enthusiasts.gitbook.io/ads-b/) - 您想了解的有关 ADS-B 接收、解码和共享的一切。
- [ADS-B equipment guide](https://sdr-enthusiasts.gitbook.io/ads-b/intro/equipment-needed) - 由社区编写的优秀 ADS-B 硬件指南。
- [PiAware ADS-B tutorial](https://flightaware.com/adsb/piaware/build/) - FlightAware 的 ADS-B 设置教程。
- [ADSB-B transponders guide](https://www.sportys.com/blog/ads-b-out-questions-1090-978/) - 解释 978 和 1090 MHz 应答器之间差异的指南。

## 书籍和文章

<!-- List interesting ADS-B books and articles -->

- [The 1090 Megahertz Riddle - Junzi Sun](https://mode-s.org/decode/index.html) - S 模式和 ADS-B 信号解码指南。

## ADS-B 聚合器

<!--lint ignore double-link-->

> **注意**
> 以下聚合器根据 **17-01-2026** 上的供给者数量按类别显示。如果支线数量不可用，则根据跟踪的飞机数量对站点进行比较。如果您认为订单需要更新，请随时打开[创建拉取请求](https://github.com/rickstaa/awesome-adsb/pulls)。

<!-- List ADS-B aggregators. -->

### 面向开源

<!-- List open source ADS-B aggregators. -->

- [airplanes.live](https://airplanes.live) - Airplanes.Live 的使命是聚合并提供对未经过滤的航空数据的综合存储库的访问。  提供地图和免费 API。
- [ADSB One](https://adsb.one) - 所有航空相关信息的一站式资源，以及合法致力于公共利益的航空饲料数据的社区驱动聚合器。
- [adsb.fi](https://adsb.fi) - 社区驱动的航班跟踪器，在全球拥有数百个支线，提供对全球空中交通数据的开放且未经过滤的访问。
- [ADSB.lol](https://adsb.lol) - 完全开源且由社区驱动的航班跟踪器，通过[免费 API](https://api.adsb.lol/) 显示和提供[ODbL 许可](https://opendatacommons.org/licenses/odbl/summary/) 数据以及[免费历史数据](https://github.com/adsbol/globe_history)。

### 社区驱动

<!-- List community driven ADS-B aggregators. -->

- [ADSBHub.org](https://www.adsbhub.org) - 一项在飞机跟踪爱好者、飞机观测员、无线电业余爱好者和对开发 ADS-B 相关软件感兴趣的专业人士之间提供实时 ADS-B 数据共享和交换的服务。
- [TheAirTraffic](https://theairtraffic.com) - 一个社区驱动的 ADS-B 聚合器，致力于保持其网站上的空中跟踪数据开放且未经过滤。
- [PlaneSpotters.net](https://www.planespotters.net) - 民航数据库和聚合器，收集了大量飞机照片和信息。
- [Plane.watch](https://plane.watch) - 社区托管的航班跟踪器。
- [www.live-military-mode-s.eu](https://www.live-military-mode-s.eu) - 社区驱动的飞行跟踪器，专注于跟踪军用飞机。
- [adsb.chaos-consulting.de](https://adsb.chaos-consulting.de) - 由爱好者管理的航班、船舶和无线电探空仪的非商业跟踪器。重点关注各个喂食站的贡献。

### 非营利组织

<!-- List non-profit ADS-B aggregators. -->

- [Opensky Network](https://opensky-network.org) - OpenSky Network 是一家总部位于瑞士的非营利协会，提供对航班跟踪控制数据的开放访问。它是由几所大学和政府实体设立的一个研究项目，旨在提高空域的安全性、可靠性和效率。

### 商业

<!-- List commercial ADS-B aggregators. -->

<!--TODO: Remove when awesome-lint/issues/160 is fixed. -->
<!--lint ignore no-undefined-references awesome-list-item-->

- [FlightAware](https://flightaware.com)[^1] - 一家美国跨国科技公司，提供实时、历史和预测性航班跟踪数据和产品。
- [FlightRadar24](https://www.flightradar24.com)[^1] - 一项瑞典基于互联网的服务，可在地图上显示实时飞机飞行跟踪信息。
- [RadarBox](https://www.radarbox.com)[^1] - 一家位于坦帕的全球航班跟踪和数据服务公司，提供全球商业和通用航空航班跟踪。
- [ADS-B Exchange](https://www.adsbexchange.com/) - 一家提供高保真、稳定、安全的航班跟踪服务的航班跟踪公司。它是由志愿者和飞行爱好者发起的，但最近被 [JETNET](https://www.jetnet.com/) 收购。
- [PlaneFinder.net](https://planefinder.net)[^1] - 英国的实时航班跟踪服务显示全球航班数据，例如航班号、飞机移动速度、海拔和旅行目的地。
- [AvDelphi](https://www.avdelphi.com) - 一家航空数据和服务公司，显示机身、注册、类型、机场和航班、雷达和导航点以及所有者和飞行历史记录。
- [RadarVirtuel](https://www.radarvirtuel.com) - 提供高级功能的飞行数据收集器。其主要重点是收集有关全球小型机场周围交通的信息。

<!--TODO: Remove when awesome-lint/issues/160 is fixed. -->
<!--lint ignore no-undefined-references-->

[^1]：遵守 [FAA](https://www.faa.gov/) 的 [飞机尾号封锁/解除封锁列表](https://www.faa.gov/pilots/ladd/request) 列表。因此，在此平台上找到的数据经过过滤，可能不包括在其他聚合器上找到的所有数据。

### 其他

- [Airframes.io](https://app.airframes.io/) - Airframes 是一项与飞机相关的聚合服务，可接收来自世界各地志愿者的 ACARS、VDL、HFDL 和 SATCOM 数据。它与 ADS-B 聚合器密切合作，并在内部处理 ADS-B 数据。
- [gcmb.io](https://gcmb.io/adsb/adsb) - 来自 ABSBHub.org 的 ADS-B 数据通过 MQTT 协议发布。

## 软件

<!-- list ADS-B software, apps and docker containers. -->

### 一般

- [readsb](https://github.com/wiedehopf/readsb) - ADS-B解码器瑞士刀。
- [dump1090](https://github.com/MalcolmRobb/dump1090) - 适用于 RTLSDR 设备的简单 S 模式解码器。
- [flightmon](https://github.com/mik3y/flightmon) - 用于显示当前 dump1090/readsb 数据的简单命令行“GUI”。
- [sdr-enthusiasts/plane-alert-db](https://github.com/sdr-enthusiasts/plane-alert-db) - 一系列令人兴奋的飞机 - 政府、独裁者、军事、历史和纯粹的奇怪飞机。
- [junzis/pyModeS](https://github.com/junzis/pyModeS) - 用于 S 模式和 ADS-B 信号的 python 解码器。
- [adsb_actions](https://github.com/eastham/adsb_actions) - 用于检测、处理和可视化 ADS-B 流量和事件的 Python 工具。

### 喂养

- [sdr-enthusiasts/docker-adsb-ultrafeeder](https://github.com/sdr-enthusiasts/docker-adsb-ultrafeeder) - 一体化 ADSB 容器，内置 readsb、tar1090、graphs1090、autogain、multi-feeder 和 mlat-hub。
- [adsbfi/adsb-fi-scripts](https://github.com/adsbfi/adsb-fi-scripts) - 易于使用的 feeder 安装脚本，用于向 adsb.fi 提供数据。
- [adsblol/feed](https://github.com/adsblol/feed) - 易于使用、基于容器的 MLAT/ADS-B/ACARS/VDL2 多源客户端。由 [SDR-Enthusiasts](https://github.com/sdr-enthusiasts) 图片提供支持。
- [adsb.im](https://adsb.im/home) - 易于使用的 ADS-B 馈线图像。设置单板计算机（例如 Raspberry Pi）来接收和共享飞机 ADS-B 位置报告，无需命令行/终端技能。允许与开源和商业航班跟踪网站共享数据。

### 可视化

- [wiedehopf/tar1090](https://github.com/wiedehopf/tar1090) - 查看 ADS-B 数据的好方法。
- [amnesica/BelugaProject](https://github.com/amnesica/BelugaProject) - 一种 Web 应用程序，可在浏览器的地图界面上显示一个或多个本地 ADS-B 馈线和 AIS 数据的数据以及附加信息。
- [Grafana](https://grafana.com/) - 适用于每个数据库的开源分析和监控解决方案。

### 应用程序

- [d4rken/adsb-meta-tracker](https://github.com/d4rken/adsb-meta-tracker) - Android ADS-B 元跟踪器，显示有关 ADS-B 聚合器的元数据。
- [AirPing](https://airping.app) - 一款 iOS 应用程序，可将您的 tar1090 或 Readsb 实例转变为移动航班跟踪器。

### 社交

- [docker-planefence](https://github.com/kx1t/docker-planefence) - 一个小工具，可用于记录、显示和推文位于接收器范围内（即围栏）的飞机。
- [Jxck-S/plane-notify](https://github.com/Jxck-S/plane-notify) - 使用 OpenSky 或 ADS-B 交换数据通知所选飞机是否已起飞或降落。

## ADS-B 衍生数据
- [aircraft-flight-schedules](https://github.com/MrAirspace/aircraft-flight-schedules) - 开源数据集，包含从全球飞机 ADS-B 位置传输（2024 年以上）中提取的全球高级航班时刻表。涵盖 [ADSBol](https://adsb.lol/) 计划覆盖范围内的全球所有航班。

## 硬件

<!-- List ADS-B hardware resources. -->

### 小型计算机公司

- [Raspberry Pi](https://www.raspberrypi.org/) - 英国开发的小型单板计算机。
- [Orange Pi](http://www.orangepi.org/html/hardWare/computerAndMicrocontrollers/details/Orange-Pi-5.html) - 使用操作系统经济高效的硬件创建的单板计算机。
- [Banana Pi](https://banana-pi.org/) - 由中国开源硬件社区创建的单板计算机。

### 接收器

- [FlightAware ADS-B USB receivers](https://flightaware.store/collections/radio-dongles) - FlightAware 制造的 ADS-B USB 接收器。
- [AirNav RadarBox ADS-B USB receivers](https://www.radarbox.com/store) - RadarBox 制造的 ADS-B USB 接收器。
- [RTL-SDR DONGLES](https://www.rtl-sdr.com/buy-rtl-sdr-dvb-t-dongles/) - 一家优质 RTL-SDR 加密狗提供商，致力于维持公平的零售价格。

### 过滤器

> **警告**
> 某些 ADS-B USB 接收器已包含板载滤波器。

- [FlightAware Signal filters](https://flightaware.store/collections/signal-filters) - FlightAware 制造的不同信号滤波器。

### 天线

- [Vinnant antennas](https://vinnant.sk/) - 斯洛伐克制造的专业优质天线。
- [DPD antennas](https://dpdproductions.com/) - 美国生产的用于各种无线电服务的高品质天线。

## 关注

<!-- List people worth following on social sites (Twitter, LinkedIn, GitHub, YouTube etc.) -->

<!--lint ignore double-link-->

> **待办事项：**
> 如果您认识 ADS-B 领域值得关注的人，请[创建拉取请求](https://github.com/rickstaa/awesome-adsb/pulls)。

我们还应该关注谁（https://github.com/rickstaa/awesome-adsb/issues/new?assignees=&labels=&template=suggestion.yaml）？

<!-- END CONTENT -->

**[⬆ 回到顶部](#contents)**

<!-- REPO INFO -->

<!-- omit in toc -->
## 贡献

欢迎任何形式的贡献💙！请查看[贡献指南](contributing.md)。

[![CC0](https://i.creativecommons.org/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

<!-- omit in toc -->
### 贡献者

<!--lint ignore double-link-->

这个项目的存在要感谢所有[做出贡献]的人(https://github.com/rickstaa/awesome-adsb/graphs/contributors)！

<!--lint ignore double-link-->
<a href="https://github.com/rickstaa/awesome-adsb/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=rickstaa/awesome-adsb" />
</a>
</br>
</br>
