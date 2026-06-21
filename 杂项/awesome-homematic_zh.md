# 很棒的家庭用品 [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

> Homematic 相关链接的精选列表

[Homematic](https://www.homematic.com/) 是制造商 [eQ-3](https://www.eq-3.de) 的一系列智能家居设备，在德国尤其受欢迎。


## 内容

- [Community](#community)
- [Documentation](#documentation)
- [移动应用程序](#mobile-apps)
- [CCU 替代方案](#ccu-alternatives)
- [替代传感器和执行器](#alternative-sensors-and-actuators)
- [CCU 插件](#ccu-addons)
- [接口软件](#interfacing-software)
- [杂项软件](#misc-software)
- [软件模块](#software-modules)
- [智能家居软件](#smart-home-software-supporting-homematic)
- [Verschiedenes](#misc)
- [License](License)


## 社区资源（主要是德语）

* [Haus Automatisierung](https://haus-automatisierung.com/) - 新闻、博客、Youtube、教程...
* [Homematic Forum](https://homematic-forum.de/forum/) - 讨论-Foren
* [Homematic Forum: Link/Skript-Sammlung](https://homematic-forum.de/forum/viewtopic.php?f=26&t=27907) - AndiN 策划的链接列表。
* [Homematic Forum: HomeMatic - Tipps für Anfänger](https://homematic-forum.de/forum/viewtopic.php?f=31&t=22801) - 萨米的行为分析
* [Homematic Guru](https://homematic-guru.de/) - 新闻、博客、教程等等。
* [Homematic Inside](https://www.homematic-inside.de/) - 新闻、博客、教程等等。
* [Homematic Blog Lison](https://homematic-blog.lison.ch/) - 博客、教程和其他内容..
* [Technikkram](https://technikkram.net) - 新闻、博客、教程等等。
* [OwnSmartHome](https://ownsmarthome.de/category/homematic/) - 新闻、博客、教程等等。
* [Verdrahtet](https://www.verdrahtet.info/) - 新闻、博客、Youtube、教程...
* [Wikimatic](http://www.wikimatic.de/wiki/Hauptseite) - 社区维基。


## 文档

* [Dissecting HomeMatic AES](https://git.zerfleddert.de/hmcfgusb/AES/) - BidCos 协议 AES 握手描述。
* [Direktverknüpfungen im Expertenmodus](https://www.youtube.com/watch?v=1B4iwtK1Rmo) - 弗特拉格·冯·弗兰克·格拉斯。
* [Virtuelle Aktorkanäle](https://www.youtube.com/watch?v=Cwxwtig6Q1I) - 弗特拉格·冯·弗兰克·格拉斯。
* [Script Documentation](http://www.wikimatic.de/wiki/Script_Dokumentation) - Inoffizielle Homematic 脚本参考。
* [Keymatic Konfiguration](https://homematic-forum.de/forum/viewtopic.php?f=31&t=19196) - Beitrag von rewe0815 在 Homematic 论坛上。

## 移动应用程序

* [@home](https://www.athomeapp.de/) - iOS - (💵 inApp-Purchase um Werbung zu entfernen)
* [HistClient](https://www.sa-com.de/smarthome-special/histclient-handbuch/) - （💵 应用程序内购买） - CCU-Historian 客户端具有适用于 iOS 和 Android 的 erweitereten 功能
* [Home-24](http://www.home-24.net/index.php?page=sites/home.php&app=home24) - 💵 安卓
* [HomeControl](http://www.ksquare.de/myhomecontrol/) - 💵 iOS
* [TinyMatic](https://www.tinymatic.de/) - 💵 Android（主要：HomeDroid）
* [Pocket Control](https://www.penzler.de) - 💵 iOS
* [Battery Status for HomeMatic](https://zeezide.com/en/products/hmbattery/) - 💵 iOS


## CCU 替代方案

* [debmatic](https://github.com/alexreinert/debmatic) - 在基于 Debian 的 amd64、armhf 和 arm64 系统（Debian、Ubuntu、Raspbian、Armbian）上安装 Homematic OCCU
* [docker-ccu](https://github.com/angelnu/docker-ccu) - Homematic CCU 固件作为 [Docker](https://www.docker.com) 容器在 Arm 和（模拟）x86 上运行。
* [Homegear](https://homegear.eu/index.php/Main_Page) - 免费开源程序，用于将您的智能家居设备与您的家庭自动化软件或您自己的脚本连接起来。
* [piVCCU](https://github.com/alexreinert/piVCCU) - 在 Raspbian 或 Armbian 上的虚拟化容器 (lxc) 内安装原始 Homematic CCU 固件。
* [RaspberryMatic](https://github.com/jens-maus/RaspberryMatic) - 轻量级、OCCU 和基于 Linux/buildroot 的发行版，用于在 RaspberryPi 等嵌入式设备上运行 HomeMatic CCU。


## 替代传感器、执行器和硬件修改

* [AskSinPPCollection](https://jp112sdl.github.io/AskSinPPCollection/) - 与 AskSinPP 一起自行构建的项目、文档和项目
* [Beispiel_AskSinPP](https://github.com/jp112sdl/Beispiel_AskSinPP) - [AskSinPP](https://github.com/pa-pa/AskSinPP) 图书馆草图
* [HAUS-BUS.DE](http://www.haus-bus.de/) - 💵 Homematic 有线兼容 Geräte。
* [Homematic Wired Hombrew Hardware](https://github.com/jfische) - Verschiedene Homebrew Sensoren/Aktoren für Homematic 有线。
* [stall.biz](https://www.stall.biz/) - 💵 替代天线，多传感器 für das Wohnzimmer，Wetterstation，...


## CCU 插件

* [CCU Historian](https://ccu-historian.de/) - Langzeit Archive 和 Graphen。
* [CUxD](https://www.homematic-inside.de/software/tag/Zusatzsoftware ) - CCU 的“Leatherman”。 Verbindet FS20，...（💵 EnOcean，...），stellt virtlle Geräte 和 hilfreiche Tools zur Verfügung。
* [Email](https://github.com/jens-maus/hm_email) - 用于电子邮件 Versand 的 HomeMatic CCU 插件。
* [HAP-HomeMatic](https://github.com/thkl/hap-homematic) - RaspberryMatic / CCU3 插件可从 HomeKit 访问您的 HomeMatic 设备。它很像 https://github.com/thkl/homebridge-homematic 但没有 homebridge。
* [hm-print](https://github.com/litti/hm-print) - CCU 程序陷入困境。
* [hm-tools](https://github.com/fhetty/hm-tools) - RaspberryMatic 工具集。
* [hm_pdetect](https://github.com/jens-maus/hm_pdetect) - Anwesenheitserkennung über die FRITZ!-Box
* [Homeputer](https://www.contronics.de/shop/HomeMatic-System/Zentralen-und-Software.html) - 💵
* [Homematic-addon-hue](https://github.com/j-a-n/homematic-addon-hue) - Philips Hue 的 HomeMatic 插件。
* [homematic_check_mk](https://github.com/alexreinert/homematic_check_mk) - Homematic CCU2 或 Raspberrymatic 设备的插件，充当 check_mk_agent。
* [jq](https://github.com/hobbyquaker/ccu-addon-jq) - jq 打包为 Homematic CCU3 的插件。
* [Mosquitto](https://github.com/hobbyquaker/ccu-addon-mosquitto) - Mosquitto 打包为 Homematic CCU3 和 RaspberryMatic 的插件
* [Patcher](https://github.com/hobbyquaker/Patcher) - CCU3 附加组件可方便地安装补丁。
* [rmupdate](https://github.com/j-a-n/raspberrymatic-addon-rmupdate) - RaspberryMatic 插件 RaspberryMatic 可以自行启动、使用 GUI 进行 WLAN 配置并查看其他插件或重新启动安装和启动
* [Redis](https://github.com/hobbyquaker/ccu-addon-redis) - Redis 打包为 Homematic CCU3 和 RaspberryMatic 的插件
* [RedMatic](https://github.com/rdmtc/RedMatic) - [Node-RED](https://nodered.org/) 是 Homematic CCU3 和 RaspberryMatic 的插件。利弗特 U.A.舒适的 HomeKit 集成和 CCU 与 MQTT MIT 的特殊节点。
* [XML-API](https://github.com/hobbyquaker/xml-api) - Vereinfachter CCU Zugriff 通过 HTTP/XML。


## 接口软件

* [CCU-Jack](https://github.com/mdzio/ccu-jack) - CCU-Jack 是 CCU 上的 REST-basierten Zugriff，以及 Addon verfügbar。
* [homebridge-homematic](https://github.com/thkl/homebridge-homematic) - [Homebridge](https://github.com/nfarina/homebridge) HomeKit 中的 Homematic Geräten 插件。
* [homebridge-homematicip](https://github.com/marcsowen/homebridge-homematicip) - [Homebridge](https://github.com/nfarina/homebridge) 通过云通过 HmIP-HAP 实现 Homematic IP 的插件。
* [hvl - Homematic Virtual Interface](https://github.com/thkl/Homematic-Virtual-Interface) - Bindet Fremdgeräte（z.B. Hue、Harmony、Netatmo、Sonos）是插件，也是插件版本。
* [node-red-contrib-ccu](https://github.com/rdmtc/node-red-contrib-ccu) - [Node-RED](https://nodered.org) Homematic CCU 的节点。



## 杂项软件

* [check_homematic](https://github.com/hobbyquaker/check_homematic) - 用于检查 Homematic CCU 的 Nagios/Icinga 插件。
* [hm-simulator](https://github.com/hobbyquaker/hm-simulator) - （部分）模拟 Homematic CCU。
* [hmcfgusb](https://git.zerfleddert.de/cgi-bin/gitweb.cgi/hmcfgusb) - 在 Linux/Unix 上使用 HM-CFG-USB(2) 的实用程序。
* [HomeHub](https://github.com/Gerti1972/homehub) - PHP/XML-API 是 Web 前端的基础。 [论坛](https://homematic-forum.de/forum/viewtopic.php?f=41&t=50538)
* [homematic-manager](https://github.com/hobbyquaker/homematic-manager) - 管理 homematic 接口进程 (rfd/hs485d/homegear)。
* [language-homematic](https://github.com/Ayngush/language-homematic) - 向 Atom 中的 HomeMatic 脚本文件添加语法突出显示和片段。
* [occu-test](https://github.com/hobbyquaker/occu-test) - ReGaHss 的自动化系统测试 - HomeMatic (O)CCU“逻辑层”。
* [HMScriptEditor](https://zeezide.com/en/products/hmscripteditor/) - 一个非常简单的 macOS 编辑器和 HomeMatic（“Rega”）脚本运行程序。

## 软件模块

* [binrpc](https://github.com/hobbyquaker/binrpc) - Xmlrpc_bin 协议客户端和服务器 Node.js 模块。
* [hm-discover](https://github.com/hobbyquaker/hm-discover) - 用于发现 Homematic CCU 和接口的 Node.js 模块。
* [homematic-rega](https://github.com/hobbyquaker/homematic-rega) - Node.js Homematic CCU ReGaHSS 远程脚本接口。
* [homematicip-rest-api](https://github.com/coreGreenberet/homematicip-rest-api) - homematicIP REST API（基于云/接入点）的 Python 包装器。
* [homematic-gqls](https://github.com/martin-riedl/homematic-gqls) - 基于 [homematicip-rest-api](https://github.com/coreGreenberet/homematicip-rest-api) 查询 Homematic IP 组件的 GraphQL 服务。
* [homematic-xmlrpc](https://github.com/hobbyquaker/homematic-xmlrpc) - Xmlrpc 客户端和服务器 Node.js 模块。
* [pmatic](https://github.com/LarsMichelsen/pmatic) - 用于 Homematic 的 Python API。便于使用。
* [pyhomematic](https://github.com/danielperna84/pyhomematic) - 用于与 Homematic 设备交互的 Python 3 接口。

## 支持Homematic的智能家居软件

* [everHome](https://everhome.de) - 💵
* [FHEM](https://fhem.de/)
* [家庭助理](https://www.home-assistant.io/)
* [ioBroker](https://www.iobroker.net/?lang=de)
* [IP-Symcon](https://www.symcon.de/) - 💵
* [Mediola](https://www.mediola.com/) - 💵
* [OpenHAB](https://www.openhab.org/)
* [Pimatic](https://pimatic.org/)

## 杂项

* [AskSinAnalyzer](https://github.com/jp112sdl/AskSinAnalyzer) - Funktelegramm-Dekodierer für den Einsatz in HomeMatic Umgebungen, hilfreich zur Fehlersuche, z.B.参见最高的 DutyCycle。
* [AskSinAnalyzerXS](https://github.com/psi-4ward/AskSinAnalyzerXS) - AskSinAnalyzer 是桌面应用程序，是 Einsatz eines ESP 的版本。
* [eagle-homematic](https://github.com/dersimn/eagle-homematic) - Homematic Modul Eagle 图书馆。
* [Tablet Wallmount](https://homematic-forum.de/forum/viewtopic.php?f=18&t=49421) - Rahmen für Unterputzmontage von Tablets。
* [Homematic 3D Druck Collection auf Thingiverse](https://www.thingiverse.com/hobbyquaker/collections/homematic) - 多样化的Teile rund um Homematic zum self drucken。


## 贡献

欢迎投稿！首先阅读[贡献指南](contributing.md)。


## 许可证

[公共领域 CC0](https://creativecommons.org/publicdomain/zero/1.0/)
