# 很棒的家庭助理 [![Awesome](https://awesome.re/badge-flat2.svg)](https://awesome.re)
<!--lint disable double-link-->

<div align="center">
  <a href="https://awesome-ha.com">
    <img width="400" src="https://www.awesome-ha.com/images/awesome-home-assistant.svg" alt="Awesome Home Assistant">
  </a>
  <br>
  <a href="https://awesome-ha.com"><strong>https://awesome-ha.com</strong></a>
</div>

Home Assistant 是开源家庭自动化，可进行本地控制和
隐私第一。它可与数千种开箱即用的设备配合使用，运行于
您自己的硬件，并且不需要任何编码来设置。无论你
正在自动化单个房间或整个房子，一切都保持在本地
和私人的。

好奇它是什么样子的？尝试一下
[家庭助理在线演示](https://demo.home-assistant.io)。

Awesome Home Assistant 是一份精选的最佳家庭助理列表
[家庭助理](https://www.home-assistant.io)资源：自定义
集成、仪表板卡、主题、应用程序、教程等等。

以下大部分项目都可以一键安装
[HACS](https://hacs.xyz)，家庭助理社区商店，在您之后
安装家庭助理本身。家庭助理的所有者是
[开放之家基金会](https://www.openhomefoundation.org)，该基金会还
管家 ESPHome、音乐助手、Z-Wave JS 和您的开放语音工具
将在整个列表中看到。如果您要购买智能家居设备，
[与 Home Assistant 配合使用](https://works-with.home-assistant.io) 程序
隐私、本地控制和长期支持测试。

该列表分为几类。这些类别中的链接没有
预先制定的订单；该订单是为了贡献。如果您想做出贡献，
请阅读[指南](https://github.com/frenck/awesome-home-assistant/blob/main/.github/CONTRIBUTING.md)
或提出[问题](https://github.com/frenck/awesome-home-assistant/issues/new/choose)
建议添加、更新或删除。

## 内容

- [如何使用](#how-to-use)
- [Installing](#installing)
- [如果您需要帮助](#in-case-you-need-help)
  - [🤝 官方社区](#-official-communities)
  - [🌍 用您的语言](#-in-your-language)
  - [🧩 围绕社区项目](#-around-community-projects)
  - [💬 其他社区空间](#-other-community-spaces)
- [公共配置](#public-configurations)
- [定制集成](#custom-integrations)
  - [🤖 人工智能和法学硕士](#-ai--llms)
  - [💡 照明](#-lighting)
  - [🌡️气候](#-climate)
  - [⚡ 能源与太阳能](#-energy--solar)
  - [📹 相机和视频](#-cameras--video)
  - [🚨 安全与警报](#-security--alarm)
  - [🔊 语音和媒体播放](#-voice--media-playback)
  - [🚗 汽车和电动汽车充电](#-cars--ev-charging)
  - [📍 存在和位置](#-presence--location)
  - [🧹 吸尘器](#-vacuums)
  - [🔵 蓝牙和BLE](#-bluetooth--ble)
  - [🔋电池监控](#-battery-monitoring)
  - [🏷️供应商和品牌](#-vendor--brand)
  - [🛠️自动化工具](#-automation-tooling)
  - [🏘️ 民用及家居](#-civic--household)
  - [🔐 网络和身份验证](#-network--authentication)
  - [🔗 联邦和多实例](#-federation--multi-instance)
  - [📊 日志记录和分析](#-logging--analytics)
- [仪表板卡](#dashboard-cards)
  - [🧱 仪表板框架](#-dashboard-frameworks)
  - [📐 布局助手](#-layout-helpers)
  - [📈 图表和图形](#-charts--graphs)
  - [📋 状态和信息行](#-status--info-rows)
  - [☀️天气卡](#-weather-cards)
  - [🎵 媒体卡](#-media-cards)
  - [🌡️气候卡](#-climate-cards)
  - [⚡ 能量卡](#-energy-cards)
  - [💡 灯光卡](#-lighting-cards)
  - [🗺️ 地图和位置](#-maps--location)
  - [📸 相机卡](#-camera-cards)
  - [🧹真空卡](#-vacuum-cards)
  - [📅 日历和动态](#-calendar--feed)
  - [📡 远程控制](#-remote-control)
  - [🍃 空气质量](#-air-quality)
  - [🖥️ 信息亭和墙板](#-kiosk--wallpanel)
- [Dashboards](#dashboards)
- [Themes](#themes)
- [图标包](#icon-packs)
- [Apps](#apps)
  - [🛡️ 官方应用程序](#-official-apps)
  - [📦 第三方应用程序](#-third-party-apps)
- [DIY](#diy)
  - [🧩 独立项目](#-standalone-projects)
  - [🌉 DIY 网关](#-diy-gateways)
  - [🔨 DIY 项目](#-diy-projects)
- [工具和实用程序](#tools--utilities)
- [在线资源](#online-resources)
  - [✍️博客](#-blogs)
  - [📺 YouTube 频道](#-youtube-channels)
  - [🎙️ 播客](#-podcasts)
  - [📱 社交](#-social)
- [替代家庭自动化软件](#alternative-home-automation-software)
- [其他很棒的清单](#other-awesome-lists)
- [商标法律声明](#trademark-legal-notice)

## 如何使用

Awesome Home Assistant 是家庭最佳资源的精选列表
助理。用它来查找应用程序、自定义卡、集成和教程
社区推荐的内容，无论您是刚刚入门还是
正在寻找您的下一个项目。

您可以通过以下方式浏览列表：

- 只需按<kbd>command/ctrl</kbd> + <kbd>F</kbd>即可搜索关键字
- 浏览我们的[_内容列表_](#contents)
- 或者，使用我们网站上的搜索：<https://www.awesome-ha.com>

## 安装中

刚接触家庭助理，不确定从哪里开始？最简单的路径是
拿起 [Home Assistant Green](https://www.home-assistant.io/green/) 并插入
如果您更愿意使用您已经拥有的硬件（Raspberry Pi、
迷你电脑，旧笔记本电脑），下面的官方指南涵盖了每个选项。
无论您选择哪一个，您最终都会运行相同的家庭助理。一旦是
安装 [HACS](https://hacs.xyz) 以及此列表中的大部分项目
只需点击一下即可。

- [Home Assistant Installation](https://www.home-assistant.io/installation/) - 官方安装指南。
- [Compare Installation Methods](https://www.home-assistant.io/installation/#compare-installation-methods) - 比较可用的安装方法。

## 如果您需要帮助

卡在配置上，想知道为什么设备无法配对，或者只是
想看看其他人正在建造什么？家庭助理有其中之一
互联网上最活跃的家庭自动化社区，其中大部分
可以免费加入。官方渠道如下；再往下你会
查找使用您的语言并围绕特定项目的社区
更广泛的生态系统。

### 🤝 官方社区

- [Home Assistant Discord](https://discord.com/invite/c5DvZ4e) - 主要聊天，我们大部分人都在。
- [Home Assistant Community](https://community.home-assistant.io/?u=frenck) - 讨论论坛。
- [Home Assistant Subreddit](https://www.reddit.com/r/homeassistant/) - 官方子版块。
- [Home Assistant Facebook Group](https://www.facebook.com/groups/HomeAssistant/) - 爱好者的 Facebook 群组。

### 🌍 用您的语言

_英语以外语言的社区。每种语言可以存在多个组；通过拉取请求添加您的。按语言字母顺序排序._

- 🇧🇷 [Home Assistant Brasil](https://t.me/homeassistant_brasil) - 适合所有技能水平用户的巴西葡萄牙语电报群。
- 🇨🇳 [Hassbian论坛](https://bbs.hassbian.com/forum.php) - 智能家居爱好者的中文论坛。
- 🇨🇿 [Home Assistant CZ](https://www.homeassistant-cz.cz/) - 拥有活跃用户群的捷克语论坛。
- 🇩🇰 [Dansk Home Assistant group](https://www.facebook.com/groups/209025039666209/) - 丹麦语 Facebook 群组。
- 🇳🇱 [荷兰语 Domotics Discord](https://discord.gg/Ee5X7T7) - 荷兰语家庭自动化 Discord。
- 🇳🇱 [Home Assistant NL](https://t.me/home_assistant_nl) - 荷兰语 Telegram 群组。
- 🇫🇮 [Home Assistant Suomi](https://www.facebook.com/groups/hasuomi/) - 芬兰语 Facebook 群组。
- 🇫🇷 [HACF 论坛](https://forum.hacf.fr) - 法语协会 HACF（家庭助理法语社区）的讨论论坛。
- 🇫🇷 [HACF Discord](https://discord.com/invite/PaZFEjX) - 由 HACF 社区运行的法语 Discord。
- 🇩🇪 [Home Assistant DE](https://t.me/home_assistant_de) - 用于讨论、提示和帮助的德语 Telegram 群组。
- 🇩🇪 [simon42 社区论坛](https://community.simon42.com/) - 智能家居主题的德语论坛。
- 🇬🇷 [Home Assistant GR](https://www.facebook.com/groups/472308593754940/) - 希腊语 Facebook 群组。
- 🇮🇱 [Home-Assistant.io Israel](https://www.facebook.com/groups/303751386650107/) - 希伯来语 Facebook 群组。
- 🇭🇺 [匈牙利家庭助理](https://www.facebook.com/groups/HomeAssistantHU/) - 匈牙利语 Facebook 群组。
- 🇮🇹 [Home Assistant Italia](https://t.me/HomeAssistantItalia) - 用于分享想法和项目的意大利 Telegram 群组。
- 🇮🇹 [HassioHelp](https://t.me/HassioHelp) - 用于故障排除和支持的意大利语 Telegram 群组。
- 🇯🇵 [Home Assistant Japan](https://www.facebook.com/groups/homeassistantjapan/) - 日语 Facebook 群组。
- 🇰🇷 [HomeAssistant Cafe](https://cafe.naver.com/koreassistant) - Naver 上的韩语社区。
- 🇳🇴 [Home Assistant Norge](https://www.facebook.com/groups/680252689011262/) - 挪威语 Facebook 群组。
- 🇵🇱 [Home Assistant Polska](https://www.facebook.com/groups/homeassistantpolska/) - 波兰语 Facebook 群组。
- 🇵🇹 [CPHA 论坛](https://forum.cpha.pt/) - 由 Comunidade Portuguesa de Home Assistant 提供的葡萄牙语论坛。
- 🇷🇴 [罗马尼亚家庭助理](https://www.facebook.com/groups/HomeAssistantRomania/) - 罗马尼亚语 Facebook 群组。
- 🇷🇺 [Home Assistant RU Telegram](https://t.me/HomeAssistantRU) - 俄语 Telegram 群组。
- 🇪🇸 [Domoteca en casa](https://foro.domoticaencasa.es/) - 家庭自动化爱好者的西班牙语论坛。
- 🇸🇪 [Svenska Home Assistant-gruppen](https://www.facebook.com/groups/737654973088984/) - 瑞典语 Facebook 群组。
- 🇹🇼 [台湾家庭助理](https://www.facebook.com/groups/151166072456061/) - 繁体中文Facebook群组。
- 🇹🇭 [泰国家庭助理](https://www.facebook.com/groups/769724336851998/) - 泰语 Facebook 群组。

### 🧩 围绕社区项目

_由社区项目运行的不和谐、论坛和聊天，您将在此列表的其他位置看到。按项目字母顺序排序._

- [AppDaemon Discord](https://discord.gg/sgSr79jW5x) - 帮助与核心一起运行的 Python 自动化框架。
- [ESPHome Discord](https://discord.gg/KhAMKrd) - 帮助使用基于 ESP 的 DIY 设备及其 YAML 固件。
- [Frigate Discussions](https://github.com/blakeblackshear/frigate/discussions) - 本地 NVR / 对象检测项目的 GitHub 讨论。
- [HACS Discord](https://discord.gg/apgchf8) - 帮助使用 Home Assistant 社区商店。
- [Music Assistant Discord](https://discord.gg/kaVm8hGpne) - 多房间音乐服务器聊天。
- [NetDaemon Discord](https://discord.gg/K3xwfcX) - 帮助用 C# / .NET 编写自动化。
- [Tasmota Discord](https://discord.gg/Ks2Kzd4) - 聊天了解为许多 Sonoff 和 eWeLink 设备提供支持的 ESP 固件。
- [Z-Wave JS Discord](https://discord.gg/HFqcyFNfWd) - 讨论 Z-Wave 集成所使用的 Z-Wave JS 堆栈。
- [Zigbee2MQTT Discussions](https://github.com/Koenkk/zigbee2mqtt/discussions) - 流行的 Zigbee 桥的 GitHub 讨论。

### 💬 其他社区空间

_不依赖于特定语言或项目的独立团体。_

- [Home Assistant International Telegram](https://t.me/home_assistant_international) - 面向更广泛的国际社区的英语 Telegram 群组。
- [r/homeautomation](https://www.reddit.com/r/homeautomation/) - 最大的与平台无关的家庭自动化 subreddit，涵盖所有集线器、协议和项目想法。
- [r/smarthome](https://www.reddit.com/r/smarthome/) - 以产品为中心的智能家居子版块，提供购买建议、评论和设置问题。
- [r/selfhosted](https://www.reddit.com/r/selfhosted/) - 用于自托管软件的 Reddit 子版块，与家庭自动化和本地控制有很大的交叉。
- [Home Assistant on Lemmy](https://lemmy.world/c/homeassistant) - 对于注重隐私的用户来说，Fediverse 是 Reddit 子版块的替代品。
- [Home Automation on Lemmy](https://lemmy.world/c/homeautomation) - Fediverse 上的一般家庭自动化社区。
- [Everything Smart Home Discord](https://discord.com/invite/everythingsmarthome) - 由 Lewis Barclay 运行的通用智能家居讨论服务器。
- [Home Operations Discord](https://discord.com/invite/home-operations) - 适合使用 GitOps 和 Kubernetes 管理智能家居基础设施的人们。
- [#Home-Assistant on Matrix](https://matrix.to/#/#Home-Assistant:matrix.org) - 矩阵室，用于基于开放、联合协议的实时聊天。
- [CocoonTech](https://cocoontech.com/) - 网络上最古老的家庭自动化论坛之一，涵盖所有平台已有 20 多年的历史。

## 公共配置

_想知道更有经验的用户如何设置他们的恒温器时间表、存在检测或自动化？这些是 GitHub 上发布的完整 Home Assistant 配置。像食谱书一样阅读它们，复制看起来有用的部分，然后跳过其余部分。_

- [Carlo Costanzo](https://github.com/CCOSTAN/Home-AssistantConfig#logo) - 可能是记录最多的配置（5,208★）。
- [DubhAd](https://github.com/DubhAd/Home-AssistantConfig) - 也称为 Tinkerer，分享他的配置文件 (688★)。
- [geekofweek](https://github.com/geekofweek/homeassistant) - 拥有 300 多个自动化（1,477★）。
- [Alok Saboo](https://github.com/arsaboo/homeassistant-config) - 也称为阿萨布。定期更新（1,953★）。
- [Franck Nijhof](https://github.com/frenck/home-assistant-config) - 基于家庭助理操作系统，与其他操作系统相比，配置结构非常不同（2,009★）。
- [Klaas Schoute](https://github.com/klaasnicolaas/Student-homeassistant-config) - 基于家庭助理操作系统、Intel NUC、Ubuntu Server、Docker 并定期更新 (223★)。
- [Ryan Warner](https://github.com/rwarner/Home-Assistant-Config) - Ubuntu HA Config 上的 Docker，从早期 HA 开始维护。详细记录并定期更新 (5★)。

## 定制集成

_Integrations Home Assistant 并非开箱即用，由社区编写。只需点击几下即可通过 HACS 安装它们。_

### 🤖 人工智能和法学硕士

_将 Home Assistant 连接到大型语言模型，让它读取您的设备、构建仪表板、编写自动化操作或描述您的相机所看到的内容。_

- [LLM Vision](https://github.com/valentinfrlch/ha-llmvision) - 为您的自动化添加视觉智能：为相机快照添加标题、总结正在发生的事情、对特定事件做出反应 (1,373★)。
- [AI Automation Suggester](https://github.com/ITSpecialist111/ai_automation_suggester) - 扫描您的实体并向人工智能提供商（OpenAI、Anthropic、Google、Groq、Ollama）询问定制的自动化建议，这些建议以通知形式出现（749★）。

### 💡 照明

_位于灯光之上的效果、时间表和行为层。_

- [Circadian Lighting](https://github.com/claytonjn/hass-circadian_lighting) - 慢慢地将变色灯与全天天空自然发生的色温同步（886★）。
- [Adaptive Lighting](https://github.com/basnijholt/adaptive-lighting) - 根据太阳的位置慢慢调整灯光的亮度和色温（3,324★）。
- [Govee](https://github.com/LaggAt/hacs-govee) - Govee Wi-Fi 灯光和灯泡的本地控制，包括效果和颜色模式 (352★)。

### 🌡️气候

_更智能的恒温器、舒适传感器和 HVAC 集成，超越内置功能。_

- [Better Thermostat](https://github.com/KartoffelToby/better_thermostat) - 更智能的恒温器，具有窗户检测、加热曲线和恒温散热器阀的每个房间的舒适度配置文件 (1,443★)。
- [Versatile Thermostat](https://github.com/jmcollin78/versatile_thermostat) - 全功能恒温器，具有预设、窗户检测、基于运动的舒适性和存在性 (1,075★)。
- [Midea Air Appliances LAN](https://github.com/nbogojevic/homeassistant-midea-air-appliances-lan) - 通过局域网对美的空调、除湿机等电器进行本地控制（460★）。
- [Smart Autotune Thermostat (SAT)](https://github.com/Alexwijn/SAT) - 自调节恒温器，可与 OpenTherm、ESPHome 或 MQTT 网关通信，并随着时间的推移调整供暖曲线以适应您的家 (246★)。
- [Dual Smart Thermostat](https://github.com/swingerman/ha-dual-smart-thermostat) - 增强版内置通用恒温器，具有独立加热和冷却、地板温度限制和湿度控制（225★）。

### ⚡ 能源与太阳能

_将您的太阳能逆变器、智能电表、家用电池或公用电费拉入家庭助理并输入能源仪表板。_

- [Powercalc](https://github.com/bramstroker/homeassistant-powercalc) - 计算灯和其他设备的估计功耗，即使是那些本身不报告的设备 (1,503★)。
- [Anker Solix](https://github.com/thomluther/ha-anker-solix) - 将 Anker Solix 阳台太阳能系统、电池和发电站拉入能源仪表板，其中包含实时状态、历史记录和充电控制 (1,005★)。
- [Octopus Energy](https://github.com/BottlecapDave/HomeAssistant-OctopusEnergy) - 将八达通能源费率、智能电表读数、智能调度时段和保存会话拉入您的仪表板 (940★)。
- [Huawei Solar](https://github.com/wlcrs/huawei_solar) - 通过Modbus读取和控制华为太阳能逆变器和家用电池，包括电网充电窗口（899★）。
- [SolaX Modbus](https://github.com/wills106/homeassistant-solax-modbus) - 通过 Modbus 与 SolaX、Sointeg、Sofar、Growatt 和其他逆变器通信，包括只读和逆变器控制模式 (490★)。
- [Solarman](https://github.com/davidrapan/ha-solarman) - 通过 Solarman 棒式记录仪 (483★) 读取 Deye、Sofar 和其他 Solarman 品牌逆变器。
- [OCPP](https://github.com/lbbrhzn/ocpp) - 将支持 OCPP 的电动汽车充电器引入能源仪表板，并提供启动、停止和按会话计量 (372★)。
- [Solcast PV Forecast](https://github.com/BJReplay/ha-solcast-solar) - 提取 Solcast 太阳能产量预测，以便您可以查看当天的预期发电量，以及最新的置信区间 (420★)。
- [EPEX Spot](https://github.com/mampfes/ha_epex_spot) - 将每小时 EPEX 现货电价带入您的仪表板，以便您可以将负荷转移到最便宜的时段 (310★)。
- [ENTSO-e Day-Ahead Prices](https://github.com/JaccoR/hass-entso-e) - 从大多数欧洲国家的 ENTSO-e 透明度平台获取日前电价 (265★)。
- [SolarEdge Modbus Multi](https://github.com/WillCodeForCats/solaredge-modbus-multi) - 通过 Modbus/TCP 本地读取 SolarEdge 逆变器、仪表和电池，支持多逆变器和三相 (303★)。
- [FoxESS Modbus](https://github.com/nathanmarlor/foxess_modbus) - 通过 Modbus 直接连接到 FoxESS 太阳能逆变器，无需云端往返，实现实时状态和控制 (308★)。
- [Victron GX](https://github.com/sfstar/hass-victron) - 通过 Modbus/TCP 从 Victron GX 设备读取数据，暴露逆变器、电池、太阳能充电器和交流输入 (317★)。
- [Solis Sensor](https://github.com/hultenvp/solis-sensor) - 与 SolisCloud PV 监控门户对话，以便您可以将 Solis 逆变器发电、电池和电网数据拉入能源仪表板 (320★)。
- [GoodWe Inverter](https://github.com/mletenay/home-assistant-goodwe-inverter) - 通过本地网络从固德威太阳能逆变器提取实时数据，用于能源仪表板 (213★)。
- [Solar Optimizer](https://github.com/jmcollin78/solar_optimizer) - 根据太阳能剩余产量启动和停止您的设备，以便您自用而不是出口（228★）。
- [Dynamic Energy Cost](https://github.com/martinarva/dynamic_energy_cost) - 根据 Nord Pool 或 EPEX (189★) 等动态价格源跟踪实时和累计能源成本。
- [Energi Data Service](https://github.com/MTrab/energidataservice) - 从 Energi 数据服务 API 获取丹麦电力现货价格，用于价格感知自动化 (275★)。

### 📹 相机和视频

_配对 Home Assistant 不支持的特定相机品牌和视频源。_

- [HASS Aarlo](https://github.com/twrecked/hass-aarlo) - 异步 Arlo 集成。类似于 Arlo 网站；监控所有基站、摄像头和门铃的事件和状态 (470★)。
- [WebRTC Camera](https://github.com/AlexxIT/WebRTC) - 通过带有平移/缩放控件的 WebRTC 或 MSE 实时查看来自 IP 摄像机的 RTSP 流 (2,134★)。
- [Frigate](https://github.com/blakeblackshear/frigate-hass-integration) - 将 Frigate NVR 与本地对象检测集成到您的仪表板、警报和快照中 (1,181★)。
- [Eufy Security](https://github.com/fuatakgun/eufy_security) - 通过实时流和事件通知管理 Eufy Security 摄像头、门铃和基站 (1,338★)。
- [Tapo Control](https://github.com/JurajNyiri/HomeAssistant-Tapo-Control) - 通过 PTZ、运动事件和实时 RTSP 流控制 TP-Link Tapo 摄像机 (1,912★)。
- [Dahua](https://github.com/rroller/dahua) - 将大华摄像机和门铃与运动事件、快照、警报器和 PTZ 控制配对 (541★)。

### 🚨 安全与警报

_将家庭助理变成功能齐全的报警系统，具有布防和撤防流程、用户代码、防区和恐慌功能。_

- [Alarmo](https://github.com/nielsfaber/alarmo) - 易于使用的报警系统，具有布防/撤防流程、用户代码、防区和紧急模式 (2,148★)。
- [Keymaster](https://github.com/FutureTense/keymaster) - 管理 Z-Wave 智能锁上的用户代码，包括每用户计划、一次性代码和通知 (334★)。

### 🔊 语音和媒体播放

_向语音扬声器和媒体播放器发送命令，或将他们听到的内容转发给 Home Assistant。_

- [Spotcast](https://github.com/fondberg/spotcast) - 在空闲的 Chromecast 设备上启动 Spotify 播放以及控制 Spotify 连接设备 (809★)。
- [Alexa Media Player](https://github.com/alandtse/alexa_media_player) - 控制 Amazon Alexa 设备：宣布、播放媒体并将设备状态拉入您的自动化 (1,948★)。
- [YandexStation](https://github.com/AlexxIT/YandexStation) - 通过Alice (1,868★) 控制Yandex Station 扬声器和其他智能家居设备。
- [Yandex Smart Home](https://github.com/dext0r/yandex_smart_home) - 将您的设备暴露给 Yandex Alice 和 Yandex 智能家居应用程序 (1,066★)。
- [View Assist Companion](https://github.com/msp1974/ViewAssist_Companion_App) - 配套的 Android 应用程序和集成可将平板电脑变成免提语音和仪表板卫星 (374★)。

### 🚗 汽车和电动汽车充电

_跟踪汽车的电池、位置和充电状态，或控制充电的地点和时间。_

- [Kia Uvo & Hyundai Bluelink](https://github.com/Hyundai-Kia-Connect/kia_uvo) - 在欧盟、加拿大和美国跟踪和控制起亚 Connect (Uvo) 和现代 Bluelink 汽车，包括充电、气候和锁定状态 (870★)。
- [Tesla](https://github.com/alandtse/tesla) - 使用第三方登录应用程序 (740★) 的刷新令牌跟踪 Tesla 汽车和 Powerwall 的充电、气候、位置和安全状态。
- [Volkswagen Carnet](https://github.com/robinostlund/homeassistant-volkswagencarnet) - 在 Carnet 平台 (643★) 上跟踪大众汽车的充电状态、气候预处理以及远程锁定和鸣喇叭。
- [Audi Connect](https://github.com/audiconnect/audi_connect_ha) - 通过 Audi Connect API 跟踪奥迪汽车，包括充电状态、里程、锁和气候预处理 (338★)。
- [Polestar](https://github.com/pypolestar/polestar_api) - 通过 Polestar 应用程序 API 读取 Polestar EV 的行驶里程、充电和位置数据 (249★)。
- [Stellantis Vehicles](https://github.com/andreadegiovine/homeassistant-stellantis-vehicles) - 在制造商 API 上添加了 Stellantis 汽车（标致、雪铁龙、菲亚特、欧宝、沃克斯豪尔、DS）的里程、锁和气候 (231★)。
- [evcc](https://github.com/marq24/ha-evcc) - 连接到 evcc 实例以进行表面充电会话、太阳能匹配和每个负载点状态 (410★)。
- [Easee EV Charger](https://github.com/nordicopen/easee_hass) - 添加了具有实时充电状态、动态负载平衡和每次会话计量功能的 Easee EV 充电器 (272★)。
- [EV Smart Charging](https://github.com/jonasbkarlsson/ev_smart_charging) - 规划电动汽车在动态电价最便宜时段的充电时间表，与大多数充电器和价格传感器配合使用 (297★)。

### 📍 存在和位置

_找出谁在家以及他们在哪里，通常比内置设备跟踪器更准确。_

- [iCloud3](https://github.com/gcobb321/icloud3) - iCloud 设备跟踪器组件的改进版本，具有很多功能（855★）。
- [iPhone Detect](https://github.com/mudape/iphonedetect) - 通过发送 UDP 探测并观察回复，无需应用程序即可检测本地 Wi-Fi 上的 iPhone（和其他手机）(625★)。
- [Flightradar24](https://github.com/AlexandrErohin/home-assistant-flightradar24) - 使用 Flightradar24 (468★) 跟踪飞越您家周围可配置边界框的飞机。
- [Places](https://github.com/custom-components/places) - 通过 OpenStreetMap 对设备跟踪器位置进行反向地理编码，以便自动化可以对“在超市”而不是原始坐标做出反应 (191★)。

### 🧹 吸尘器

_控制特定的机器人真空吸尘器并显示其地图数据，超出内置数据。_

- [Xiaomi Cloud Map Extractor](https://github.com/PiotrMachowski/Home-Assistant-custom-components-Xiaomi-Cloud-Map-Extractor) - 呈现小米（Roborock/Viomi/Roidmi/Dreame）吸尘器地图的实时视图，无需生根（1,405★）。
- [Dreame Vacuum](https://github.com/Tasshack/dreame-vacuum) - Dreame 扫地机器人具有完整的地图支持，包括禁区和选择性房间清洁（1,999★）。

### 🔵 蓝牙和BLE

_从通过蓝牙广播的传感器中提取数据，或使用蓝牙本身进行房间级存在检测。_

- [BLE Monitor](https://github.com/custom-components/ble_monitor) - 被动读取小米MiBeacon、Govee、ATC、Inkbird、Qingping和许多其他BLE传感器的传感器数据（2,214★）。
- [Bermuda](https://github.com/agittins/bermuda) - 通过对多个 ESPHome 接收器上的 BLE 信号进行三角测量来进行房间级存在检测 (1,798★)。
- [BLE Battery Management Systems](https://github.com/patman15/BMS_BLE-HA) - 读取来自许多供应商的低功耗蓝牙电池管理系统 (BMS)，显示每节电池的电压、平衡和 SOC (328★)。
- [EcoFlow BLE](https://github.com/rabits/ha-ef-ble) - 通过低功耗蓝牙拉动 EcoFlow 发电站和配件，无需云帐户 (304★)。

### 🔋电池监控

_密切关注所有设备中的电池，并在电量耗尽之前收到警告。_

- [Battery Notes](https://github.com/andrew-codechimp/HA-Battery-Notes) - 为每台设备添加电池类型和数量注释，然后跟踪更换情况、低电量警告和历史记录 (1,105★)。

### 🏷️供应商和品牌

_将特定制造商的设备拉入家庭助理，通常比内置设备具有更多功能或更好的本地控制。_

- [SmartIR](https://github.com/smartHomeHub/SmartIR) - 使用 Broadlink IR 集成设备 (2,733★)。
- [Sonoff LAN](https://github.com/AlexxIT/SonoffLAN) - 通过 LAN 和/或云 (3,257★) 使用 eWeLink（原始）固件控制 Sonoff 设备。
- [Xiaomi MIoT](https://github.com/al-one/hass-xiaomi-miot) - 使用 MIoT 规范协议通过 Wi-Fi、BLE 和 Zigbee 自动集成小米智能家居设备 (5,911★)。
- [Xiaomi Gateway 3](https://github.com/AlexxIT/XiaomiGateway3) - 通过局域网本地控制小米多模网关和Aqara Hub E1，无需云端往返（2,757★）。
- [Midea AC LAN](https://github.com/wuwentao/midea_ac_lan) - 本地控制美的空调、热泵等M-Smart设备（1,684★）。
- [SmartThinQ Sensors](https://github.com/ollo69/ha-smartthinq-sensors) - LG 电器（洗衣机、烘干机、空调、冰箱）通过 SmartThinQ 连接，具有丰富的状态和远程启动功能 (1,310★)。
- [Home Connect Alt](https://github.com/ekutner/home-connect-hass) - 适用于博世、西门子、NEFF 和嘉格纳烤箱、洗碗机和洗衣机的替代 Home Connect 集成，其状态比官方集成 (970★) 更丰富。
- [Tapo Devices](https://github.com/petretiandrea/home-assistant-tapo-p100) - 通过 LAN (954★) 的 TP-Link Tapo 插头、开关、灯泡和能源监控（P100、P105、P110、L510、L530、L900）。
- [Meross](https://github.com/albertogeniola/meross-homeassistant) - 通过 Meross IoT 云 (848★) 控制 Meross 插头、开关、灯泡、车库门开启器和加湿器。
- [HomeMatic IP Local](https://github.com/SukramJ/homematicip_local) - 通过 OpenCCU 或 RaspberryMatic 对 HomeMatic 和 HomeMatic IP 设备进行本地控制，无需云往返 (572★)。
- [Nest Protect](https://github.com/iMicknl/ha-nest-protect) - 跟踪 Nest Protect 烟雾和一氧化碳警报器的电池状态、最近发生的事件以及每个房间的安全状态 (468★)。
- [Meross LAN](https://github.com/krahabb/meross_lan) - 对 Meross 插头、开关、灯和车库开门器进行本地控制，仅在需要时返回云端 (718★)。
- [LocalTuya](https://github.com/rospogrigio/localtuya) - 通过局域网本地控制涂鸦设备，无需云端往返，支持插头、灯光、气候、盖子（3,857★）。
- [SamsungTV Smart](https://github.com/ollo69/ha-samsungtv-smart) - 改进了三星电视与 SmartThings 支持、源切换、应用程序启动和每个应用程序图标的集成 (652★)。
- [Dyson](https://github.com/libdyson-wg/ha-dyson) - Wi-Fi 连接的戴森风扇、净化器和加湿器，可通过本地网络按模式进行全面控制 (418★)。
- [PetKit](https://github.com/RobertD502/home-assistant-petkit) - 在制造商云上添加 PetKit 喂食器、喷泉和垃圾箱，具有完整的状态和喂食控制 (340★)。
- [Miele](https://github.com/astrandb/miele) - 可与 Miele 洗衣机、烘干机、洗碗机、烤箱和咖啡机配对，并带有详细的程序状态 (267★)。
- [Home Connect Local](https://github.com/chris-mc1/homeconnect_local_hass) - 直接通过本地网络与博世、西门子、NEFF 和嘉格纳设备对话，无需绕道云 (390★)。
- [hOn](https://github.com/gvigroux/hon) - 从官方 hOn 云中提取 Haier、Candy 和 Hoover 电器，公开应用程序显示的每个状态和参数 (253★)。
- [PETLIBRO](https://github.com/jjjonesjr33/petlibro) - 添加 PELIBRO 智能宠物喂食器和饮水器，包括喂食时间表、分配事件和电池电量 (319★)。

### 🛠️自动化工具

_使自动化更易于编写、调试和维护的帮助器。_

- [The Watchman](https://github.com/dummylabs/thewatchman) - 跟踪配置文件中丢失的实体和服务 (655★)。
- [Browser Mod](https://github.com/thomasloven/hass-browser_mod) - 将每个浏览器变成一个可控制的实体：弹出卡片、导航视图、播放声音或检测谁正在查看仪表板 (1,748★)。
- [Pyscript](https://github.com/custom-components/pyscript) - 使用 Python 而不是 YAML 编写自动化和模板 (1,159★)。
- [Spook](https://github.com/frenck/spook) - 一个包含有用传感器、服务和模板的工具箱，可显示 UI 通常隐藏的内容 (1,138★)。
- [Scheduler Component](https://github.com/nielsfaber/scheduler-component) - 通过卡片驱动的 UI 为任何实体构建每周计划，无需 YAML (883★)。
- [Node-RED Companion](https://github.com/zachowj/hass-node-red) - node-red-contrib-home-assistant-websocket 项目的配套组件，将服务、传感器和二进制传感器暴露回仪表板 (573★)。
- [Magic Areas](https://github.com/jseidl/magic-areas) - 自动构建每个房间的存在、气候和媒体区域实体，具有运动触发的场景和亮/暗检测（493★）。
- [Auto Backup](https://github.com/jcwillox/hass-auto-backup) - 使用自定义计划、保留规则、加密和上传到远程存储来自动执行备份 (462★)。
- [Multiscrape](https://github.com/danieldotnl/ha-multiscrape) - 在一次请求中从页面中抓取多个值（HTML、XML 或 JSON）并将它们转换为传感器 (437★)。
- [Retry Service](https://github.com/amitfin/retry) - 包装任何服务调用，以便瞬态故障通过指数退避自动重试 (163★)。

### 🏘️ 民用及家居

_变成传感器和日历的本地服务：垃圾收集时间表、学校假期、交通、天气警报等。_

- [Mail and Packages](https://github.com/moralmunky/Home-Assistant-Mail-And-Packages) - 用于传入和投递包裹的传感器以及 USPS Informed Delivery 预览图像，全部来自您现有的电子邮件帐户 (844★)。
- [Irrigation Unlimited](https://github.com/rgc99/irrigation_unlimited) - 多区域灌溉控制器，具有时间表、顺序、天气调整和手动运行支持（435★）。
- [Moonraker (Klipper)](https://github.com/marcolivierarsenault/moonraker-home-assistant) - 跟踪运行 Moonraker（Mainsail、Fluidd）的基于 Klipper 的 3D 打印机，包括打印进度、温度和网络摄像头快照 (469★)。
- [Smart Irrigation](https://github.com/jeroenterheerdt/HAsmartirrigation) - 根据蒸散量、近期降雨量和天气预报计算每个灌溉区的运行时间（509★）。
- [UK Bin Collection](https://github.com/robbrad/UKBinCollectionData) - 英国地方当局的议会垃圾箱收集时间表，显示为每个废物流的下一个收集传感器（328★）。

### 🔐 网络和身份验证

_通过单点登录登录 Home Assistant、通过隧道路由或将网络硬件拉入仪表板。_

- [OIDC Auth](https://github.com/christiaangoossens/hass-oidc-auth) - 通过任何 OpenID Connect 提供商（包括 Authelia、Authentik、Keycloak 和 Pocket ID (936★)）进行单点登录。
- [OpenID Connect Auth](https://github.com/cavefire/hass-openid) - 通过任何 OpenID Connect 提供商登录，包括 Authelia、Keycloak 和 Authentik (201★)。
- [TP-Link Router](https://github.com/AlexandrErohin/home-assistant-tplink-router) - 通过传感器、重启按钮、交换机和每个客户端设备跟踪来管理 TP-Link 和 Mercusys 路由器 (348★)。
- [Mikrotik Router](https://github.com/tomaae/homeassistant-mikrotik_router) - 将 Mikrotik 路由器和接入点拉入您的仪表板，并提供每个客户端流量、DHCP 租用和 PoE 控制 (453★)。

### 🔗 联邦和多实例

_将多个 Home Assistant 实例链接在一起，跨家庭共享实体，或在它们之间进行中继。_

- [Remote Home Assistant](https://github.com/custom-components/remote_homeassistant) - 将多个实例链接在一起，以便实体、服务和事件在它们之间流动 (1,232★)。

### 📊 日志记录和分析

_将 Home Assistant 数据发送到外部系统以进行长期存储、更丰富的仪表板或分析。_

- [Elasticsearch](https://github.com/legrego/homeassistant-elasticsearch) - 将事件发布到 Elasticsearch (165★)。
- [TrueNAS](https://github.com/tomaae/homeassistant-truenas) - 将 TrueNAS Scale 和 Core 统计数据、数据集、虚拟机和应用程序拉入传感器和交换机 (370★)。
- [Monitor Docker](https://github.com/ualex73/monitor_docker) - 监视主机上每个 Docker 容器（包括远程容器）的 CPU、内存、网络和正常运行时间，并通过自动化启动或停止它们 (401★)。
- [Unraid](https://github.com/ruaan-deysel/ha-unraid) - 监控Unraid NAS，包括CPU、内存、磁盘、虚拟机和Docker容器（240★）。

## 仪表板卡

_Lovelace 插件可放入您的仪表板中。大致按他们所做的事情分组。_

### 🧱 仪表板框架

_完整的卡片集合可以改变仪表板的外观和感觉。蘑菇、泡泡卡、平面图和类似的一体化工具包。_

- [Mushroom](https://github.com/piitaya/lovelace-mushroom) - 完整的卡片系列，具有柔和、移动优先的美感，您可以将其放入现有的仪表板中 (5,018★)。
- [Bubble Card](https://github.com/Clooos/Bubble-Card) - 具有弹出式触摸和丰富定制功能的极简卡片系列（4,323★）。
- [Floorplan](https://github.com/ExperienceLovelace/ha-floorplan) - 将实体映射到您房子的 SVG 上，并根据状态变化对它们进行动画处理 (1,553★)。
- [UI Lovelace Minimalist](https://github.com/UI-Lovelace-Minimalist/UI) - 嵌入式仪表板集合在您的所有视图中具有统一的简约外观，包括现成的卡片和按钮卡库 (2,036★)。

### 📐 布局助手

_改变其他卡片出现位置和方式的卡片：堆叠、折叠、有条件显示、重新设计样式或模板。_

- [Auto-Entities Card](https://github.com/thomasloven/lovelace-auto-entities) - 动态添加实体：🔮 Magic (1,756★)。
- [Card Modder](https://github.com/thomasloven/lovelace-card-mod) - 设计您的 Lovelace 卡片 (1,722★)。
- [Restriction Card](https://github.com/iantrich/restriction-card) - 一张卡提供对Lovelace卡的限制（317★）内定义。
- [Config Template Card](https://github.com/iantrich/config-template-card) - 允许在 Lovelace 中使用模板 (552★)。
- [Button card](https://github.com/custom-cards/button-card) - 为您的实体提供高度可定制的按钮（2,456★）。
- [Expander Card](https://github.com/Alia5/lovelace-expander-card) - 可展开和折叠的卡片可将其他卡片分组并隐藏在标题后面 (415★)。
- [Layout Card](https://github.com/thomasloven/lovelace-layout-card) - 精细控制卡片在仪表板上的放置方式，包括砖石风格和网格布局 (1,246★)。
- [Vertical Stack In Card](https://github.com/ofekashery/vertical-stack-in-card) - 将多张卡片组合成一张具有共享边框的时尚卡片 (968★)。
- [Fold Entity Row](https://github.com/thomasloven/lovelace-fold-entity-row) - 一个可折叠的行，将额外的实体隐藏在标题后面，直到单击为止 (705★)。
- [State Switch](https://github.com/thomasloven/lovelace-state-switch) - 根据实体的状态、一天中的时间或用户查看情况动态地将一张卡交换为另一张卡 (463★)。
- [Swipe Navigation](https://github.com/zanna-37/hass-swipe-navigation) - 在移动设备上使用滑动手势在仪表板视图之间切换 (543★)。
- [Custom Card Features](https://github.com/Nerwyn/custom-card-features) - 添加按钮、下拉菜单、滑块、旋转框、选择器和开关，您可以将其附加到磁贴卡以调用任何服务 (426★)。
- [Custom Sidebar](https://github.com/elchininet/custom-sidebar) - 根据用户或设备个性化侧边栏、隐藏页面、重新排序或重新设计外观 (278★)。
- [Paper Buttons Row](https://github.com/jcwillox/lovelace-paper-buttons-row) - 高度可配置的按钮行，可以调用操作、触发触觉并按状态重新设置样式 (359★)。
- [Streamline Card](https://github.com/brunosabot/streamline-card) - 定义一次卡片模板，然后在具有不同实体的仪表板中重复使用它，无需复制粘贴 YAML (258★)。

### 📈 图表和图形

_随着时间的推移可视化传感器数据。仪表、折线图、条形图和桑基图。_

- [Mini Graph Card](https://github.com/kalkih/mini-graph-card) - 简约的传感器图形卡（3,830★）。
- [Canvas Gauge Card](https://github.com/custom-cards/canvas-gauge-card) - 使用canvas-gauges.com (216★) 提供的很棒的仪表。
- [Dual Gauge Card](https://github.com/custom-cards/dual-gauge-card) - 两个仪表合二为一 (220★)。
- [ApexCharts Card](https://github.com/RomRider/apexcharts-card) - 由 ApexChartsJS 支持的高级图形和图表，带有时间线、多轴和事件标记 (1,797★)。
- [Sankey Chart](https://github.com/MindFreeze/ha-sankey-chart) - 桑基式流程图，用于可视化家庭中的电力、水或任何其他流量 (660★)。
- [Modern Circular Gauge](https://github.com/selvalt7/modern-circular-gauge) - 现代外观的圆形仪表卡，具有流畅的动画、色标和模板支持 (269★)。
- [Flex Table Card](https://github.com/custom-cards/flex-table-card) - 高度灵活的表卡，具有任意列、正则表达式匹配的实体和每行样式，对于 AppDaemon 和模板化内容非常有用 (268★)。

### 📋 状态和信息行

_紧凑的行将更多信息打包到实体卡样式列表中。_

- [Slider Entity Row](https://github.com/thomasloven/lovelace-slider-entity-row) - 添加滑块进行调整，例如lovelace实体卡片中灯光的亮度（912★）。
- [Battery State Card](https://github.com/maxwroc/battery-state-card) - 在整洁的卡片中列出设备及其电池电量，并进行排序和颜色编码 (1,246★)。
- [Scheduler Card](https://github.com/nielsfaber/scheduler-card) - 直接从仪表板构建和编辑任何实体的每周计划 (1,236★)。
- [Entity Progress Card](https://github.com/francois-le-ko4la/lovelace-entity-progress-card) - 适用于任何数字实体的进度条卡，带有阈值、渐变和模板化图标 (257★)。
- [Vehicle Status Card](https://github.com/ngocjohn/vehicle-status-card) - 仪表板卡显示燃油或充电水平、里程、车门、锁状态以及汽车的可定制图像 (262★)。
- [Timer Bar Card](https://github.com/rianadon/timer-bar-card) - 适用于任何计时器实体的进度条卡，具有倒计时、格式化剩余时间和可配置颜色 (578★)。

### ☀️天气卡

_具有您真正想要的外观的天气小部件。_

- [Weather Chart Card](https://github.com/mlamberts78/weather-chart-card) - 带有图表式每小时天气预报和可自定义布局的天气卡 (435★)。
- [Hourly Weather](https://github.com/decompil3d/lovelace-hourly-weather) - 将今天的每小时天气预报显示为彩色水平条，以便您一目了然地了解情况何时发生变化 (393★)。
- [Weather Radar](https://github.com/Makin-Things/weather-radar-card) - 使用公共 RainViewer 磁贴服务的动画降雨雷达卡，具有国家级和区域缩放功能 (384★)。
- [Clock Weather Card](https://github.com/pkissling/clock-weather-card) - 将日期、时间和天气预报卡与未来几天的 iOS 风格布局相结合 (841★)。
- [Horizon Card](https://github.com/rejuvenate/lovelace-horizon-card) - 可视化全天太阳在地平线上的位置，并带有日出、日落和黄昏标记 (652★)。

### 🎵 媒体卡

_通过专辑封面、队列和每个房间的存在来控制媒体播放器的更好方法。_

- [Mini Media Player](https://github.com/kalkih/mini-media-player) - 简约的媒体播放器卡（1,701★）。

### 🌡️气候卡

_具有不同外观或感觉的替换恒温器卡。_

- [Thermostat Card](https://github.com/ciotlosm/lovelace-thermostat-dark-card) - 恒温器控制卡看起来像 Nest 恒温器 (745★)。
- [Simple Thermostat](https://github.com/nervetattoo/simple-thermostat) - 更简单、更灵活的恒温卡（806★）。
- [Mini Climate](https://github.com/artem-sedykh/mini-climate-card) - 紧凑型气候卡，具有当前温度、目标和每种模式控件，尺寸适合小型仪表板和移动设备 (322★)。

### ⚡ 能量卡

_可视化太阳能发电、电网进口、电池状态和消耗流量。_

- [Sunsynk Power Flow](https://github.com/slipx06/sunsynk-power-flow-card) - 可视化Sunsynk和Deye逆变器的实时能量流，镜像逆变器屏幕的布局（384★）。

### 💡 灯光卡

_灯光、色温和效果的专门控制。_

- [RGB Light Card](https://github.com/bokub/rgb-light-card) - 彩色按钮控制 RGB 灯 (563★)。
- [Hue-Like Light Card](https://github.com/Gh61/lovelace-hue-like-light-card) - 灯卡的风格和布局类似于飞利浦 Hue 应用程序，具有分组场景和每个灯泡控制 (368★)。
- [Light Entity Card](https://github.com/ljmerza/light-entity-card) - 紧凑卡可控制任何灯光或开关实体，具有亮度、色温和颜色选择器（282★）。

### 🗺️ 地图和位置

_显示您的设备和人员所在位置的地图，以及历史轨迹和自定义叠加层。_

- [ha-map-card](https://github.com/nathan-gs/ha-map-card) - 基于传单的地图卡，包含历史轨迹、自定义图块图层和点击操作 (116★)。

### 📸 相机卡

_通过叠加、控件、事件时间线和弹出查看器以您想要的方式显示相机流。_

- [Advanced Camera Card](https://github.com/dermotduffy/advanced-camera-card) - 全面的相机卡，包含时间线、画廊、快照、剪辑和每个事件的回放 (1,077★)。

### 🧹真空卡

_在仪表板中显示真空状态、房间地图和启动/停止控件。_

- [Vacuum Map Card](https://github.com/PiotrMachowski/lovelace-xiaomi-vacuum-map-card) - 该卡提供了一种用户友好的方式来完全控制小米（Roborock/Viomi/Dreame/Roidmi）和Neato（+可能其他）真空吸尘器（1,885★）。
- [Vacuum Card](https://github.com/denysdovhan/vacuum-card) - 一张用于控制扫地机器人的卡（1,211★）。
- [Valetudo Map](https://github.com/Hypfer/lovelace-valetudo-map-card) - 直接在仪表板上显示运行 Valetudo（无云固件）的扫地机器人的实时地图 (304★)。

### 📅 日历和动态

_即将发生的事件的日历视图和滚动提要。_

- [Atomic Calendar Revive](https://github.com/totaldebug/atomic-calendar-revive) - 具有高级设置的日历卡（629★）。
- [Week Planner Card](https://github.com/FamousWolf/week-planner-card) - 即将发生的事件、警报和提醒的响应式多日概述 (514★)。
- [Trash Card](https://github.com/idaho/hassio-trash-card) - 基于日历实体显示下一个垃圾收集类型（纸质、塑料、有机），并带有颜色编码图标 (356★)。
- [Calendar Card Pro](https://github.com/alexpfau/calendar-card-pro) - 可定制的日历卡，具有事件分组、位置指示器和简洁现代的外观 (1,122★)。

### 📡 远程控制

_电视、流媒体和 AV 设备的虚拟遥控器。_

- [LG WebOS Remote Control](https://github.com/madmicio/LG-WebOS-Remote-Control) - LG 电视 WebOS (551★) 的远程控制。
- [HA Firemote](https://github.com/PRProd/HA-Firemote) - 适用于 Apple TV、Fire TV、Chromecast、Homatics、Shield、onn.、Roku、小米等的虚拟遥控器 (987★)。
- [Universal Remote Card](https://github.com/Nerwyn/universal-remote-card) - 适用于任何媒体设备的完全可定制的虚拟遥控器，支持自定义按钮和触觉 (569★)。

### 🍃 空气质量

_显示净化器和空气质量传感器的读数。_

- [Purifier Card](https://github.com/denysdovhan/purifier-card) - 空气净化器控制卡（342★）。

### 🖥️ 信息亭和墙板

_隐藏镶边、全屏运行，或者将墙上的旧平板电脑变成专用的触摸面板。_

- [Wall Panel](https://github.com/j-a-n/lovelace-wallpanel) - 适用于安装在墙上的平板电脑的壁挂式面板模式和照片屏幕保护程序 (842★)。
- [Kiosk Mode](https://github.com/NemesisRE/kiosk-mode) - 隐藏标题、侧边栏和溢出菜单，以获得干净的信息亭式视图 (738★)。

## 仪表板

_用不同的外观和感觉替换或扩展默认 Home Assistant 仪表板的框架。_

- [Dwains Dashboard](https://github.com/dwainscheeren/dwains-lovelace-dashboard) - 适用于台式机、平板电脑和移动设备的全自动生成仪表板 (2,048★)。
- [Mushroom Strategy](https://github.com/DigiLive/mushroom-strategy) - 使用蘑菇卡自动生成仪表板的策略（648★）。

## 主题

_一切都与外观有关，应用一些风格。_

- [Midnight](https://community.home-assistant.io/t/midnight-theme/28598?u=frenck) - 马塞尔霍夫斯的黑暗主题。
- [Dark Cyan](https://community.home-assistant.io/t/dark-cyan-theme/28594?u=frenck) - 由 Ryoen Deprouw 设计的带有青色色调的深色主题。
- [Grey Night](https://community.home-assistant.io/t/grey-night-theme/30848?u=frenck) - ksya 的带有灰色调的深色主题。
- [Dark Red](https://community.home-assistant.io/t/dark-red-theme/28592?u=frenck) - 由 Ryoen Deprouw 设计的带有红色点缀的深色主题。
- [Halloween](https://community.home-assistant.io/t/halloween-theme/30872?u=frenck) - 马哈斯里·卡拉瓦拉 (Mahasri Kalavala) 为南瓜上色。
- [Black and Green](https://community.home-assistant.io/t/black-and-green-theme/28602?u=frenck) - 由 GreenTurtwig 设计的带有浅绿色口音的深色主题。
- [Vintage](https://community.home-assistant.io/t/vintage-theme/42806?u=frenck) - 使用 Anup Surendran 的这个主题为您的前端带来复古外观。
- [Carbon Green](https://community.home-assistant.io/t/share-your-themes/22018/95?u=frenck) - Reua 的轻碳主题与绿色点缀。
- [Slate](https://github.com/seangreen2/slate_theme) - 接近香草外观的深色主题（137★）。
- [Synthwave](https://github.com/bbbenji/synthwave-hass) - 主题受到现代 Synthwave 乐队（200★）封面艺术的影响。
- [Frosted Glass](https://github.com/wessamlauf/homeassistant-frosted-glass-themes) - 现代磨砂玻璃深色和浅色主题，带有半透明卡片（907★）。
- [iOS Themes](https://github.com/basnijholt/lovelace-ios-themes) - 主题灵感来自 iOS 深色和浅色模式 (868★)。
- [LCARS](https://github.com/th3jesta/ha-lcars) - 受《星际迷航》LCARS 启发的桥感主题 (534★)。
- [Material You](https://github.com/Nerwyn/material-you-theme) - 适应您的强调色的 Material Design 3 主题 (452★)。
- [Graphite](https://github.com/TilmanGriesel/graphite) - 平静、干净的主题，具有集中、低对比度的感觉(442★)。
- [Catppuccin](https://github.com/catppuccin/home-assistant) - 舒缓的柔和主题与编辑器和应用程序中流行的 Catppuccin 调色板相匹配 (427★)。
- [Mushroom Themes](https://github.com/piitaya/lovelace-mushroom-themes) - 专为与蘑菇卡系列 (304★) 搭配而设计的其他主题。
- [visionOS](https://github.com/Nezz/homeassistant-visionos-theme) - 主题灵感来自苹果的visionOS (313★)。
- [Nordic](https://github.com/coltondick/nordic-theme-main) - 北欧调色板中的浅色和深色主题，有多种蓝色调变体 (43★)。

## 图标包

_您通过 HACS 安装的自定义图标集，用于替换或扩展仪表板中的默认图标。_

- [Font Awesome Icons](https://github.com/thomasloven/hass-fontawesome) - 在您的前端使用 Font Awesome 的免费图标 (339★)。
- [Hass Hue Icons](https://github.com/arallsopp/hass-hue-icons) - 其他飞利浦 Hue 灯泡和灯具图标 (377★)。
- [simpleicons](https://github.com/vigonotion/hass-simpleicons) - 使用 simpleicons 集中的免费图标 (167★)。

## 应用程序

_需要数据库、反向代理、MQTT 代理（许多智能家居设备使用的消息服务）或与 Home Assistant 一起运行的其他工具？应用程序（以前称为附加组件）可让您将它们直接安装到 Home Assistant OS 中。没有 Docker，没有单独的服务器，不需要命令行。_

### 🛡️ 官方应用程序

_由家庭助理团队创建和维护。_

- [DuckDNS](https://github.com/home-assistant/hassio-addons/blob/master/duckdns/DOCS.md) - 更新您的 Duck DNS IP 地址并使用 Let's Encrypt 生成 SSL。
- [File editor](https://github.com/home-assistant/hassio-addons/blob/master/configurator/DOCS.md) - 基于浏览器的配置文件编辑器。
- [Mosquitto](https://github.com/home-assistant/hassio-addons/blob/master/mosquitto/DOCS.md) - 快速可靠的 MQTT 代理。
- [Terminal & SSH](https://github.com/home-assistant/hassio-addons/blob/master/ssh/DOCS.md) - 允许使用 Web 终端或 SSH 客户端远程登录。
- [Samba](https://github.com/home-assistant/hassio-addons/blob/master/samba/DOCS.md) - 使用 Windows 网络共享访问您的配置文件。
- [NGINX SSL proxy](https://github.com/home-assistant/hassio-addons/blob/master/nginx_proxy/DOCS.md) - 带 SSL 终止的反向代理。
- [deCONZ](https://github.com/home-assistant/hassio-addons/blob/master/deconz/DOCS.md) - 使用 Dresden Elektronik 的 ConBee 或 RaspBee 硬件控制 ZigBee 网络。
- [Let's Encrypt](https://github.com/home-assistant/hassio-addons/blob/master/letsencrypt/DOCS.md) - 从 Let's Encrypt 获取免费的 SSL 证书；开放且自动化的证书颁发机构 (CA)。
- [MariaDB](https://github.com/home-assistant/hassio-addons/blob/master/mariadb/DOCS.md) - 开源关系数据库（MySQL 的分支）。

### 📦 第三方应用程序

_任何人都可以创建应用程序，以下是由社区创建的。_

- [SSH & Web Terminal](https://github.com/hassio-addons/app-ssh) - SSH 和基于 Web 的终端，带有大量预装的有用工具 (501★)。
- [UniFi Controller](https://github.com/hassio-addons/app-unifi) - UniFi 控制器允许您使用网络浏览器管理您的 UniFi 网络 (374★)。
- [Node-RED](https://github.com/hassio-addons/app-node-red) - 基于流的物联网编程（639★）。
- [Plex Media Server](https://github.com/hassio-addons/app-plex) - 您录制的媒体组织精美并准备好进行流式传输 (190★)。
- [InfluxDB](https://github.com/hassio-addons/addon-influxdb) - 用于指标、事件和实时分析的可扩展数据存储（196★）。
- [Grafana](https://github.com/hassio-addons/addon-grafana) - 用于精美分析和监控的开放平台（279★）。
- [Tor](https://github.com/hassio-addons/app-tor) - 保护您的隐私并通过 Tor (62★) 访问您的实例。
- [Spotify Connect](https://github.com/hassio-addons/app-spotify-connect) - 将音乐从 Spotify 直接传输到您的 Home Assistant 设备 (250★)。
- [zigbee2mqtt](https://github.com/Koenkk/zigbee2mqtt) - Zigbee 到 MQTT 桥接器，摆脱您专有的 Zigbee 桥接器 (15,213★)。
- [AppDaemon](https://github.com/AppDaemon/appdaemon) - 用于编写自动化应用程序的松散耦合、多线程、沙箱 Python 执行环境 (961★)。
- [TasmoAdmin](https://github.com/hassio-addons/addon-tasmoadmin) - 集中管理您的所有 Sonoff-Tasmota 设备 (256★)。
- [Aircast](https://github.com/hassio-addons/app-aircast) - 适用于 Chromecast 播放器的 AirPlay 功能 (397★)。
- [AirSonos](https://github.com/hassio-addons/app-airsonos) - 适用于 Sonos 播放器的 AirPlay 功能 (121★)。
- [Log Viewer](https://github.com/hassio-addons/addon-log-viewer) - 基于浏览器的实时日志查看实用程序（94★）。
- [Tautulli](https://github.com/hassio-addons/addon-tautulli) - 监控并从您的 Plex 服务器获取统计数据 (46★)。
- [motionEye](https://github.com/hassio-addons/addon-motioneye) - 简单、优雅且功能丰富的闭路电视/NVR，适合您的摄像机 (332★)。
- [JupyterLab](https://github.com/hassio-addons/addon-jupyterlab) - 创建包含实时代码、方程、可视化和解释性文本的文档 (68★)。
- [Glances](https://github.com/hassio-addons/app-glances) - 用Python编写的跨平台系统监控工具（186★）。
- [AdGuard Home](https://github.com/hassio-addons/app-adguard-home) - 具有家长控制功能的全网络广告和跟踪器拦截 DNS 服务器 (520★)。
- [Traccar](https://github.com/hassio-addons/addon-traccar) - 现代GPS跟踪平台（158★）。
- [Hass.io Google Drive Backup](https://github.com/sabeechen/hassio-google-drive-backup) - 用于备份到 Google 云端硬盘的完整且易于配置的解决方案 (3,553★)。
- [Grocy](https://github.com/hassio-addons/app-grocy) - ERP 超越您的冰箱！适合您家庭的杂货和家庭管理解决方案 (433★)。
- [CrowdSec](https://github.com/crowdsecurity/home-assistant-addons) - 下一代协作 IPS/IDS 可保护您免受入侵 (94★)。
- [C-Gate Web Bridge](https://github.com/dougrathbone/cgateweb-homeassistant) - 通过具有自动发现功能的 MQTT 将奇胜 C-Bus 照明和自动化系统桥接到家庭助理 (4★)。

## DIY

_一些最好的智能家居小工具并不作为您可以购买的产品存在，但其他人已经找到了如何构建它们。下面的项目涵盖了从焊接您自己的多传感器到重新利用已停产设备的所有内容。大多数都是周末项目，其零件成本比一次咖啡还低。_

### 🧩 独立项目

- [ESPHome](https://esphome.io/) - 使用 YAML 对 ESP8266 板和 ESP32 板进行编程。
- [Tasmota](https://github.com/arendst/Tasmota) - ESP8266 板和设备的固件 (24,475★)。
- [Sonoff NSPanel](https://github.com/joBr99/nspanel-lovelace-ui) - 适用于 Sonoff NSPanel 触摸屏的定制固件，具有 Lovelace 风格的 UI (988★)。
- [CODESYS V3 Home Automation](https://github.com/MichielVanwelsenaere/HomeAutomation.CoDeSys3) - PLC 家庭自动化软件，通过 MQTT 进行通信，用于有线自动化设置 (144★)。

### 🌉 DIY 网关

- [OpenMQTTGateway](https://github.com/1technophile/OpenMQTTGateway) - 适用于 IR、RF、BLE、MiFlora、SMS 和许多传感器的灵活 MQTT 网关 (4,023★)。
- [esp8266 Milight Hub](https://github.com/sidoh/esp8266_milight_hub) - 使用 MQTT 的 Milight/LimitlessLED 设备的替代集线器 (1,040★)。

### 🔨 DIY 项目

- [HA SwitchPlate](https://community.home-assistant.io/t/ha-switchplate-diy-lcd-touchscreen-wall-switch-replacement/25464?u=frenck) - 液晶触摸屏墙壁开关更换。
- [$10 WiFi RGB Bulb](https://community.home-assistant.io/t/how-to-inexpensive-10-us-wifi-rgb-bulb-that-works-with-home-assistant/14735?u=frenck) - 一款可在 WiFi 上工作的廉价 RGB 灯泡。
- [433mhz/IR Bidirectional Gateway](https://community.home-assistant.io/t/433mhz-infrared-ir-to-and-from-mqtt-on-esp8266/6779?u=frenck) - 使用 ESP8266 和 MQTT 进行 IR 和 433mhz 双向传输。
- [esp8266MQTTBlinds](https://community.home-assistant.io/t/esp8266-window-blinds-mqtt/14863?u=frenck) - 使用 ESP8266、伺服系统和 MQTT 实现百叶窗自动化。
- [Home Assistant's Hackster.io](https://www.hackster.io/home-assistant?f=1#_=_) - 一个包含多个 DIY 项目的 Hackster 频道。
- [Bed Presence Detection](https://selfhostedhome.com/diy-bed-presence-detection-home-assistant/) - 基于 ESP8266 的床存在检测。
- [QuinLED](https://quinled.info/) - 使用 ESP32 板 DIY Wi-Fi LED 调光器和控制器。

## 工具和实用程序

_助手、守护程序和开发人员工具位于 Home Assistant 旁边，而不是位于 Home Assistant 内部。对于编辑配置、调试数据、通过 MQTT 发送设备数据或将 HA 连接到更广泛的工作流程非常有用。_

- [HASS Configurator](https://github.com/danielperna84/hass-configurator) - 基于浏览器的配置文件编辑器（334★）。
- [HA-Dockermon](https://github.com/philhawthorne/ha-dockermon) - 用于 RESTful 开关的 Node.js 服务来控制 Docker 容器 (291★)。
- [Home Assistant Device Database](https://www.hadevices.com/) - 支持/确认的工作设备的数据库。
- [Jinja Scripts for Curious Minds](https://github.com/skalavala/mysmarthome/tree/master/jinja_helpers) - 一堆 Jinja2 脚本可以帮助您更好地理解它。
- [GitLab CI/CD](https://about.gitlab.com/2018/08/02/using-the-gitlab-ci-slash-cd-for-smart-home-configuration-management/) - 如何使用 GitLab CI/CD 简化您的智能家居配置。
- [Monitor](https://github.com/andrewjfreyer/monitor) - 通过 MQTT 报告分布式基于广告的 BTLE 存在检测 (2,104★)。
- [HASS-data-detective](https://github.com/robmarkcole/HASS-data-detective) - 探索和分析您的数据库数据（204★）。
- [ADB Intents](https://gist.github.com/mcfrojd/9e6875e1db5c089b1e3ddeb7dba0f304) - 控制 Android 设备的 ADB 意图列表。
- [Home Assistant Config Helper for VSCode](https://marketplace.visualstudio.com/items?itemName=keesschollaart.vscode-home-assistant) - Visual Studio Code 扩展，在编辑配置时提供自动完成、配置验证和片段。
- [Home Assistant Taskbar Menu](https://github.com/PiotrMachowski/Home-Assistant-Taskbar-Menu) - Windows 客户端，可以显示 Lovelace 视图、控制实体并显示持久通知 (342★)。

## 在线资源

_Home Assistant 拥有一个蓬勃发展的社区，由博主、YouTuber、播客以及喜欢分享自己构建的内容的人们组成。下面的人是一些值得关注的常规声音，特别是当有新东西发布并且你想在决定是否自己挖掘之前亲自尝试时。_

### ✍️博客

#### 英语

- [DIY Futurism](https://diyfuturism.com/) - Brad 为新用户提供了清晰的分步说明的文章。
- [Smart Home Hobby](https://smarthomehobby.com/) - 提供经济实惠的指南和信息。
- [Self Hosted Home](https://selfhostedhome.com/) - 有关 DIY 家庭自动化项目和自托管服务的文章。
- [Tinkering with Home Automation](https://blog.ceard.tech/) - Tinkerer 的博客和指南。
- [HomeTechHacker](https://hometechhacker.com/) - DIY 智能家居指南、评论和建议。
- [Intermittent Technology](https://blog.quindorian.org/) - Quindor 的个人博客涵盖智能家居、网络和邻近技术。
- [SmartHomeScene](https://smarthomescene.com/) - 适合初学者的教程、智能家居设备评论和 DIY 自动化项目。
- [KPeyanski](https://peyanski.com/) - Kiril Peyanski 提供的教程和演练涵盖自动化、AI 集成和能源管理。
- [fixtse](https://fixtse.com/) - Sergio Romero 提供的存在检测、语音助手和本地 AI 的硬件评论和 DIY 指南。
- [Michael Leen](https://michaelsleen.com/) - 实用的设置建议和装备评论旨在帮助人们构建他们的第一个智能家居。
- [Phil Hawthorne](https://philhawthorne.com/) - 来自一位长期播客的关于集成、存在检测和家庭自动化的现场笔记。
- [Frenck](https://frenck.dev/) - Franck Nijhof 撰写的关于开源、项目领导力和个人自动化实验的幕后帖子。

#### 🌍 用其他语言

_按语言字母顺序排序。_

- 🇩🇪 [simon42](https://www.simon42.com/) - Simon Müller 提供的有关安装、集成和自动化的初学者友好指南。
- 🇩🇪 [smarterkram](https://smarterkram.de/) - Oliver Kluth 提供的有关 Zigbee、Matter、ESPHome 和硬件的详细教程。
- 🇩🇪 [SmartHome myself](https://smarthomeyourself.de/) - Daniel Scheidler 的发布报道、设备评论和集成指南。

### 📺 YouTube 频道

_坐下来，放松，观看，学习。_

#### 英语

_首先是官方频道，然后按订阅人数排序。每晚刷新._

- [Home Assistant](https://www.youtube.com/channel/UCbX3YkedQunLt7EQAdVxh7w) - 新产品发布和直播的官方频道（7.37 万订阅者）。
- [The Hook Up](https://www.youtube.com/channel/UC2gyzKcHbYfqoXA5xbyGXtQ) - Robert Tait 的智能家居教程、小工具评论和家庭自动化实验（577K 订阅者）。
- [Everything Smart Home](https://www.youtube.com/c/EverythingSmartHome) - 智能家居和技术评论、指南和分步 DIY 项目（245K 订阅者）。
- [Home Automation Guy](https://www.youtube.com/@HomeAutomationGuy) - Alan Byrne（113K 订阅者）的智能家居教程、自动化和装备评论。
- [Smart Home Junkie](https://www.youtube.com/@smarthomejunkie) - Ed de Tollenaer 为初学者和高级用户提供的操作方法视频和教程（85.7K 订阅者）。
- [digiblurDIY](https://www.youtube.com/channel/UC5ZdPKE2ckcBhljTc2R_qNA) - 硬件项目教程和 Tasmota 自动化（74.1K 低音炮）。
- [Intermit.Tech](https://www.youtube.com/channel/UCv7UOhZ2XuPwm9SN5oJsCjA) - 教程和评论涵盖相机、家庭网络、ESP 板和 Node-RED（62.5K sub）。
- [BeardedTinker](https://www.youtube.com/channel/UCuqokNoK8ZFNQdXxvlE129g) - 智能家居教程和 3D 打印（44.9K 订阅内容）。
- [JuanMTech](https://www.youtube.com/juanmtech) - 易于理解的操作视频和产品评论（42.6K 订阅者）。
- [mostlychris](https://www.youtube.com/@mostlychris) - Chris West 的智能家居教程和小工具评论（40.2K 订阅者）。
- [KPeyanski](https://www.youtube.com/@kpeyanski) - Kiril Peyanski（33.7K 订阅者）编写的硬件项目、仪表板和集成实践教程。
- [This Smart House](https://www.youtube.com/@thissmarthouse) - Ryan Holland（33.8K subs）提供适合初学者的设置演练和产品评论。
- [SlackerLabs](https://www.youtube.com/@SlackerLabs) - Jeffrey Stone 的自动化、脚本编写和修补演练（30.6K 字幕）。
- [Michael Leen](https://www.youtube.com/@michaelsleen) - 智能家居教程和集成演练（26.7K 字幕）。
- [Technithusiast](https://www.youtube.com/@technithusiast) - Michael Montaque 的教程、集成和自动化（22.8K 低音炮）。
- [3ATIVE VFX](https://www.youtube.com/@3ATIVE) - 视觉特效艺术家 David Martin 的智能家居自动化和集成（20,500 名低音炮）。
- [Smart Home Australia](https://www.youtube.com/@smart_home_australia) - Paul Toner 撰写的澳大利亚风味智能家居评论和教程（20,700 订阅者）。
- [CTech&Media](https://www.youtube.com/@CTechMedia) - Charly Schulte 的智能家居评论和教程（18K 订阅者）。
- [Frenck | Home Assistant & Smart Home](https://www.youtube.com/@frenck) - 家庭助理项目的负责人，偶尔发布有关他自己的经验和家庭助理世界中正在发生的事情的内部观点的视频（9.8K 字幕）。

#### 🌍 用其他语言

_按语言字母顺序排序，然后按订户数量排序。_

- 🇸🇦 [智能技术阿拉伯语](https://www.youtube.com/@SmartTechArabic) - Shady Nafie 的阿拉伯语教程（99.1K 订阅者）。
- 🇧🇷 [Descomplicando Tech](https://www.youtube.com/@DescomplicandoTech) - Fabricio Goncalves 的智能家居指南（15900 订阅者）。
- 🇫🇷 [AyLabs](https://www.youtube.com/@ay_labs) - Aymeric Le Feyer 的教程、集成和自动化演练（12K 字幕）。
- 🇩🇪 [simon42](https://www.youtube.com/@simon42) - Simon Müller 的教程、自动化和仪表板指南（20.5 万订阅者）。
- 🇩🇪 [haus:automation](https://www.youtube.com/@haus_automation) - Matthias Kleine 的教程、集成和自动化演练（136K 字幕）。
- 🇩🇪 [SmartHome myself](https://www.youtube.com/@Smarthomeyourself) - Daniel Scheidler 的 DIY 智能家居构建和指南（35K 订阅者）。
- 🇩🇪 [Tristans Smartes Heim](https://www.youtube.com/@tristanssmartesheim) - Tristan Küsters 的智能家居设置指南和集成（13.8K 字幕）。
- 🇮🇹 [DinamoTech](https://www.youtube.com/@DinamoTech) - Francesco Cova 的智能家居教程和评论（78K 订阅者）。
- 🇮🇹 [Ipensieridellarchitetto](https://www.youtube.com/@ipensieridellarchitetto) - 家庭自动化、技术和人工智能演练（14.8K 字幕）。
- 🇪🇸 [Home Assistant y Domótica Fácil](https://www.youtube.com/@HomeAssistantFacil) - Luis del Valle 的智能家居教程和自动化（139K 订阅者）。
- 🇪🇸 [Tecnoyfoto](https://www.youtube.com/@Tecnoyfoto) - Albert Barnosell 的教程和产品评论（45K 订阅者）。

### 🎙️ 播客

_在通勤时、做早晨的例行公事或在健身房时获得灵感！_

- [Home Assistant Podcast](https://hasspodcast.io) - 每两周一次的播客，提供最新新闻和有趣的嘉宾。

### 📱 社交

_值得关注的帐户，可获取新闻、提示和灵感，涵盖各个领域
社区活跃的网络._

#### 官方

- **家庭助理** ([X](https://x.com/home_assistant)、[Bluesky](https://bsky.app/profile/home-assistant.io)、[Mastodon](https://fosstodon.org/@homeassistant)、[Facebook](https://www.facebook.com/homeassistantio/)、[Instagram](https://www.instagram.com/homeassistant/)、 [LinkedIn](https://www.linkedin.com/company/home-assistant)) - 开源家庭自动化，将本地控制和隐私放在首位。
- **Home Assistant 开发人员** ([X](https://x.com/hass_devs)、[Bluesky](https://bsky.app/profile/developers.home-assistant.io)) - 有关贡献者开发的最新消息。
- **Open Home Foundation** ([X](https://x.com/openhomefndn)、[Bluesky](https://bsky.app/profile/openhomefoundation.org)、[Mastodon](https://fosstodon.org/@openhomefoundation)、[Instagram](https://www.instagram.com/openhomefoundation/)) - 保护智能家居的隐私、选择和可持续性。
- **ESPHome** ([X](https://x.com/esphome_), [Bluesky](https://bsky.app/profile/esphome.io)) - 用于控制 ESP 板和智能家居设备的开源系统。
- **Nabu Casa** ([X](https://x.com/NabuCasa)) - 云服务背后的公司。
- **Rhasspy** ([X](https://x.com/rhasspy), [Mastodon](https://fosstodon.org/@rhasspy)) - Michael Hansen 的开源语音助手工具包。

#### 社区

- **Paulus Schoutsen** ([X](https://x.com/balloob)、[Bluesky](https://bsky.app/profile/paulusschoutsen.nl)、[Mastodon](https://fosstodon.org/@balloob)、[Threads](https://www.threads.com/@balloob)) - 该项目和 Nabu Casa 的创始人。
- **Franck Nijhof** ([X](https://x.com/frenck)、[Bluesky](https://bsky.app/profile/frenck.social)、[Mastodon](https://fosstodon.org/@frenck)、[Threads](https://www.threads.com/@frenck)、[Instagram](https://www.instagram.com/frenck/)、 [YouTube](https://www.youtube.com/@frenck)、[LinkedIn](https://www.linkedin.com/in/frenck)) - 项目负责人和此精彩列表的创建者。
- **Everything Smart Home** ([X](https://x.com/EverySmartHome)、[Bluesky](https://bsky.app/profile/lewisbarclay.bsky.social)、[Mastodon](https://fosstodon.org/@everythingsmarthome)、[Threads](https://www.threads.com/@everythingsmarthome)) - Lewis 的智能家居和技术评论、指南和 DIY 项目巴克莱。
- **JuanMTech** ([X](https://x.com/JuanMTech)、[Bluesky](https://bsky.app/profile/juanmtech.com)、[Threads](https://www.threads.com/@juanmtech)) - 易于遵循的操作方法内容和产品评论。
- **家庭自动化专家** ([X](https://x.com/alanmbyrne)、[Bluesky](https://bsky.app/profile/burnsie.com)、[Mastodon](https://mastodon.social/@burnsie)) - Alan Byrne 的智能家居教程和自动化。
- **mostlychris** ([X](https://x.com/mostlychris2)、[Bluesky](https://bsky.app/profile/mostlychris.com)、[Mastodon](https://fosstodon.org/@mostlychris)) - Chris West 的智能家居教程和小工具评论。
- **BeardedTinker** ([X](https://x.com/BeardedTinker), [Bluesky](https://bsky.app/profile/beardedtinker.bsky.social)) - 智能家居教程和 3D 打印。
- **Mark Watt Tech** ([Bluesky](https://bsky.app/profile/markwatttech.bsky.social)、[Mastodon](https://fosstodon.org/@MarkWattTech)) - 软件开发人员和智能家居内容创建者。
- **Smart Home Junkie** ([X](https://x.com/smarth0mejunkie)、[Threads](https://www.threads.com/@smarthomejunkie)) - Ed de Tollenaer 为初学者和高级用户提供的操作方法内容。
- **智能家居求解器**（[X](https://x.com/smarthomesolver)、[Threads](https://www.threads.com/@smarthomesolver)) - Reed Kleinman 的智能家居提示和评论。

#### 🌍 用其他语言

_按语言字母顺序排序。_

- 🇧🇷 **LNPBR** ([Instagram](https://www.instagram.com/lnp_br/)、[Threads](https://www.threads.com/@lnp_br)、[TikTok](https://www.tiktok.com/@lnpbr)) - Leandro 的智能家居教程和产品评论。
- 🇩🇪 **simon42** ([Instagram](https://www.instagram.com/simon42.official/)、[Facebook](https://www.facebook.com/simon42official/)) - Simon Müller 的初学者友好型智能家居指南和自动化。
- 🇩🇪 **haus:automation** ([Instagram](https://www.instagram.com/haus_automation/), [Facebook](https://www.facebook.com/HausAutomatisierungCom/)) - Matthias Kleine 的 DIY 智能家居教程。
- 🇪🇸 **Un loco y su tecnología** ([X](https://x.com/unlocoysutec)、[Instagram](https://www.instagram.com/unlocoysutecnologia/)、[Threads](https://www.threads.com/@unlocoysutecnologia)、 [TikTok](https://www.tiktok.com/@unlocoysutecnologia)) - Carlos Cordero 的智能家居内容。
- 🇪🇸 **Tecnoyfoto** ([X](https://x.com/tecnoyfoto), [Instagram](https://www.instagram.com/barnosell/)) - Albert Barnosell 的教程和产品评论。
- 🇪🇸 **La Choza Digital** ([X](https://x.com/LaChozaDigital), [Bluesky](https://bsky.app/profile/lachozadigital.bsky.social)) - 有关智能家居和 DIY 自动化的简短教程。
- 🇫🇷 **HACF** ([X](https://x.com/hacf_fr)) - 法语社区共享教程和资源。
- 🇮🇹 **inDomus** ([X](https://x.com/indomusit), [TikTok](https://www.tiktok.com/@indomusit)) - 意大利个人家庭自动化社区。
- 🇳🇱 **Denie van Kleef** ([X](https://x.com/disney79), [Instagram](https://www.instagram.com/denievankleef/)) - 荷兰智能家居和能源指南。
- 🇵🇹 **CPHA** ([Facebook](https://www.facebook.com/cpha.pt/)) - 家庭自动化爱好者的葡萄牙语社区。

## 替代家庭自动化软件

_Home Assistant 并不是唯一的家庭自动化平台。如果您想进行比较，或者您有 Home Assistant 未涵盖的特定需求，那么以下项目是最活跃的替代方案。有些是商业的，有些是开源的，还有一些解决非常不同的问题。_

- [openHAB](https://github.com/openhab) - 基于Java，旨在成为通用集成平台。
- [Domoticz](https://github.com/domoticz/domoticz) - 轻型家庭自动化系统（3,773★）。
- [Gladys](https://github.com/GladysAssistant/Gladys) - 在 Raspberry Pi (3,066★) 上运行的开源程序。
- [SmartThings](https://www.smartthings.com/) - 三星的商业家庭自动化中心。
- [Homey](https://homey.app/) - Athom 的商业多协议平台，通过 Homey Pro 将本地控制放在首位，并以 Homey Cloud 作为托管选项。
- [Homebridge](https://github.com/homebridge/homebridge) - 轻量级 Node.js 服务器将非 HomeKit 设备桥接到 Apple Home，具有大型插件生态系统 (25,384★)。
- [Node-RED](https://github.com/node-red/node-red) - 基于流程的可视化编程工具，用于将设备、API 和服务连接在一起，由 OpenJS 基金会 (23,277★) 支持。
- [ioBroker](https://github.com/ioBroker/ioBroker) - 物联网集成平台，具有数百个适配器以及对 KNX 和 HomeMatic 的强大欧洲协议支持 (1,371★)。
- [FHEM](https://fhem.de/) - 基于 Perl 的服务器，具有 430 多个模块，并深度支持 KNX、EnOcean 和 HomeMatic 等欧洲协议。
- [Jeedom](https://github.com/jeedom/core) - 源自法国的无云平台，带有插件市场，可在任何 Linux 系统上运行 (414★)。
- [Hubitat](https://hubitat.com/) - 商业本地优先集线器支持 Z-Wave、Zigbee 和 Matter，所有自动化功能都在设备上运行。
- [HomeSeer](https://homeseer.com/) - 拥有 25 年以上开发经验的商业平台、强大的 Z-Wave 支持和广泛的插件生态系统。

## 其他很棒的清单

_喜欢这个列表，但是对于相邻的主题？下面的列表涵盖了更广泛的智能家居类别、特定协议和一般的自托管软件。当某些东西不直接适合家庭助理但可能会解决您的部分难题时，它们是查看的好地方。_

- [awesome-iot](https://github.com/HQarroum/awesome-iot) - 精彩的物联网项目和资源精选列表（3,948★）。
- [awesome-mqtt](https://github.com/awesome-mqtt/awesome-mqtt#readme) - MQTT 相关内容的精选列表（2,350★）。
- [awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) - 精选的优秀自托管软件列表（298,647★）。

## 贡献

这个很棒的列表是一个活跃的开源项目，并且始终向
想要为此做出贡献的人。我们建立了一个单独的文件
包含我们的[贡献指南](https://github.com/frenck/awesome-home-assistant/blob/main/.github/CONTRIBUTING.md)。

这个很棒的列表的原始设置是由 [Franck Nijhof](https://x.com/frenck) 完成的。

有关所有作者和贡献者的完整列表，请查看
[贡献者页面](https://github.com/frenck/awesome-home-assistant/graphs/contributors)。

感谢您的参与！ 😍

## 商标法律声明

Awesome Home Assistant 是一个独立的、社区策划的索引。它不是
创建、认可、赞助或附属于
[家庭助理](https://www.home-assistant.io) 或
[开放之家基金会](https://www.openhomefoundation.org)。 “家庭助理”
和 Home Assistant 徽标是 Open Home Foundation 的商标。

所有其他产品名称、徽标、品牌、商标和注册商标
此列表中引用的财产均为其各自所有者的财产。
对特定制造商、产品、集成、附加组件的引用，
服务和社区项目仅用于识别目的，并且不会
并不意味着其所有者的认可。

此列表的内容已根据[知识共享署名
4.0 国际](https://creativecommons.org/licenses/by/4.0/) (CC-BY-4.0)。
全文请参阅 [LICENSE.md](LICENSE.md)。
