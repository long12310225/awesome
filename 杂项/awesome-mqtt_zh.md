# 很棒的 MQTT [![Awesome](https://awesome.re/badge-flat2.svg)](https://awesome.re)

> MQTT 相关内容的精选列表。

MQTT 是一种轻量级客户端-服务器发布/订阅消息传递协议，针对高延迟或不可靠的网络进行了优化。该协议是物联网应用、遥测、传感器网络、智能计量、家庭自动化、消息传递和通知服务的不错选择。

## 内容

<!--lint disable double-link-->
- [社区资源](#community-resources)
- [Brokers](#brokers)
- [Cloud](#cloud)
- [Platforms](#platforms)
- [Tools](#tools)
- [Clients](#clients)
- [Scripting](#scripting)
- [Interfaces](#interfaces)
    - [Makers](#makers)
    - [Industry](#industry)
    - [电话、集团电话](#telephony-pbx)
    - [操作系统](#operating-system)
    - [Monitoring](#monitoring)
    - [位置追踪](#location-tracking)
    - [Logging](#logging)
    - [智能家居硬件接口](#smart-home-hardware-interfaces)
    - [智能家居集成软件](#smart-home-integration-software)
    - [Lighting](#lighting)
    - [家庭娱乐](#home-entertainment)
    - [智能抄表](#smart-metering)
    - [Messaging](#messaging)
    - [Misc](#misc)
- [可视化、仪表板](#visualization-dashboards)
- [建筑、会议](#architecture-convention)
- [安全、加密](#security-encryption)
<!--lint enable double-link-->

### 贡献

欢迎投稿！首先阅读[贡献指南](contributing.md)。

## 社区资源

- [mqtt.org](https://mqtt.org/)
- [MQTT 社区维基](https://github.com/mqtt/mqtt.org/wiki)
- [Google 网上论坛：MQTT](https://groups.google.com/g/mqtt)
- [freenode 网络上的 IRC 频道 #mqtt](irc://irc.freenode.net/mqtt)
- [公共经纪人名单](https://moxd.io/2015/10/17/public-mqtt-brokers/)

### 博客

- [本·哈迪尔](https://www.hardill.me.uk/wordpress/tag/mqtt/)
- [扬-皮特男士](https://jpmens.net/)
- [尼克·奥利里](https://knolleary.net/)
- [HiveMQ](https://www.hivemq.com/blog/)
- [EMQ](https://www.emqx.com/en/blog)
- [亚马逊 AWS IoT 博客](https://aws.amazon.com/blogs/iot/tag/mqtt/)

### 会谈

- [An Introduction to MQTT: Why HTTP isn't the King of the Internet of Things](https://www.youtube.com/watch?v=LKz1jYngpcU) - Shinji Kim、Robert Bird - Akamai，2017 年三星开发者大会。
- [Einführung in MQTT](https://www.youtube.com/watch?v=INYG4-xsa9c) - Dominik Obermaier 和 Jens Deters，2016 年 [Building IoT](https://www.buildingiot.de/index.php) 会议（德语）。

## 经纪人

- [Ably](https://www.ably.io/documentation/mqtt) - MQTT 代理服务和协议适配器。
- [ActiveMQ](https://activemq.apache.org/) - 快速 Java 多协议消息传递和集成模式服务器。
- [Aedes](https://github.com/moscajs/aedes) - Barebone MQTT 代理可以以节点方式在任何流服务器上运行。
- [Bevywise MQTTRoute](https://www.bevywise.com/mqtt-broker/) - MQTTRoute 是一个可扩展的 MQTT 代理，具有可定制的 UI、灵活的存储和安全选项，适用于所有 IoT/IIoT 实施。
- [BifroMQ](https://bifromq.apache.org) - 基于 Java 的高性能 MQTT 代理，具有适用于大规模 IoT 的本机多租户。
- [comqtt](https://github.com/wind-c/comqtt) - 一个轻量级、高性能的支持分布式集群的go mqtt服务器(v3.0|v3.1.1|v5.0)。
- [Eclipse Amlen](https://github.com/eclipse/amlen) - 一个可扩展、安全、易于使用的消息代理，可用于物联网、网络和移动用例。从 IBM MessageSight 开源。
- [Emitter](https://github.com/emitter-io/emitter) - 一个基于MQTT协议、具有消息存储功能的分布式、可扩展、容错的发布订阅消息平台。
- [EMQ X](https://github.com/emqx/emqx) - 适用于 5G 时代物联网的可扩展且可靠的实时 MQTT 消息传递引擎。
- [esp_uMQTT_broker](https://github.com/martin-ger/esp_mqtt) - ESP8266 上的基本 MQTT 代理。
<!--lint disable double-link-->
- [hbmqtt Broker](https://github.com/beerfactory/hbmqtt) - 使用 asyncio 的 Python MQTT 代理。
<!--lint enable double-link-->
- [HiveMQ](https://www.hivemq.com/) - 支持 MQTT 3.1、3.1.1 和 5.0 的 Java MQTT 代理。提供商业和开源版本。
- [hrotti](https://github.com/alsm/hrotti) - 用 Go 编写的 MQTT 代理。
- [KMQTT](https://github.com/davidepianca98/KMQTT) - Kotlin 多平台 MQTT 代理，可嵌入和独立。
- [Moquette](https://github.com/moquette-io/moquette) - Java MQTT 轻量级代理。
- [Mosca](https://www.mosca.io/) - Node.js MQTT 代理，可以独立使用或嵌入到另一个 Node.js 应用程序中。
- [Mosquitto](https://mosquitto.org/) - *“*The”** 开源 MQTT 代理。
- [mqtt5](https://github.com/LabOverWire/mqtt-lib) - Rust 中的异步 MQTT v5.0 代理，具有 TCP、TLS、WebSocket 和 QUIC 传输，以及身份验证、ACL、桥接和会话持久性。
- [MyQttHub](https://myqtthub.com) - 云 MQTT 代理。
- [Mystique](https://github.com/TheThingsIndustries/mystique) - 用 Go 编写的可扩展 MQTT 代理，具有 HTTP 可观察性功能。实施 MQTT v3.1.1。
- [RabbitMQ](https://www.rabbitmq.com/mqtt.html) - 具有 MQTT 适配器的高性能消息传递代理。
- [RobustMQ](http://robustmq.com) - 用 Rust 编写的多协议代理。
- [SurgeMQ](https://zhen.org/categories/surgemq/) - Go 中的高性能 MQTT 服务器和客户端库。
- [tbmq](https://github.com/thingsboard/tbmq) - 适用于数百万物联网设备的开源、可扩展、容错且持久的消息传递代理。
- [VerneMQ](https://vernemq.com/) - Apache2 许可的分布式 MQTT 代理，用 Erlang 开发。
<!--lint disable double-link-->
- [Vert.x MQTT Server](https://github.com/vert-x3/vertx-mqtt) - Vert.x 组件用于处理与远程 MQTT 客户端的连接、通信和消息交换。
<!--lint enable double-link-->
- [Waterstream](https://waterstream.io/) - MQTT 代理利用 Apache Kafka 作为自己的存储和分发引擎。
- [NanoMQ](https://github.com/nanomq/nanomq) - 适用于 IoT Edge 平台的轻量级且极快的 MQTT 代理。


## 云

- [Adafruit IO](https://io.adafruit.com) - 面向数据的物联网框架和库。
- [Alibaba Cloud IoT Platform](https://www.alibabacloud.com/product/iot) - 在设备和物联网平台之间提供安全可靠的通信，使您可以在单个物联网平台上管理大量设备。
- [AWS IoT Core](https://aws.amazon.com/iot-core/) - 支持 MQTT、基于 WSS 的 MQTT、HTTPS 和 LoRaWAN 的托管云代理服务。
- [Azure IoT Hub](https://azure.microsoft.com/en-us/services/iot-hub/) - 在您的 IoT 应用程序与其管理的设备之间实现高度安全且可靠的通信。 Azure IoT 中心提供云托管解决方案后端来连接几乎任何设备。通过每设备身份验证、内置设备管理和扩展配置，将您的解决方案从云端扩展到边缘。
- [CloudMQTT](https://www.cloudmqtt.com/) - 物联网托管消息代理。为物联网完美配置和优化的消息队列，几秒钟内即可准备就绪。
- [CloudAMQP](https://www.cloudamqp.com/docs/mqtt.html) - 具有 MQTT 支持的托管 AMQP 代理。
- [CrystalMQ](https://www.bevywise.com/hosted-mqtt-server/) - 适用于大规模部署的完全托管云 MQTT 代理。
- [flespi](https://flespi.com/mqtt-broker) - 免费且安全的云 MQTT 代理，具有私有命名空间、MQTT 3.1.1 和 MQTT 5.0 支持以及华丽的限制。
- [Google Cloud IoT](https://cloud.google.com/solutions/iot/) - 云管理的 MQTT 服务。
- [HiveMQ Cloud](https://www.hivemq.com/cloud/) - 云管理的 MQŚT 服务。

## 平台

- [Iotellect](https://iotellect.com/) - 用于工业自动化、SCADA、BMS 和远程监控的低代码 IoT/IIoT 平台。支持 MQTT、OPC-UA、Modbus 和 100 多个协议，具有可视化开发工具和边云集成。
- [mainflux](https://www.mainflux.com/) - 设备管理、数据聚合、数据管理、数据分析、连接和消息路由以及事件管理。由 Linux 软件基金会支持。
- [thingsboard](https://thingsboard.io/) - IoT 项目的设备管理、数据收集、处理、事件管理和可视化。
- [ForestHub](https://foresthub.ai) - 边缘AI代理平台；其开源运行时 [edge-agents](https://github.com/ForestHubAI/edge-agents) 在 Linux 边缘网关上编排 AI 代理，使用 MQTT 作为一流的工作流传输，与本地 SLM 和云 LLM 一起离线运行。


## 工具
- [hivemq-mqtt-web-client](https://github.com/hivemq/hivemq-mqtt-web-client) - 基于浏览器的 MQTT 客户端，通过 Websocket 使用 MQTT。 [直接链接](https://www.hivemq.com/demos/websocket-client/)
- [homie-home-assistant-discovery](https://github.com/labodj/homie-home-assistant-discovery) - Node.js CLI 和库，将 Homie MQTT 元数据映射到 Home Assistant MQTT 发现负载。
- [imqtt](https://github.com/shafreeck/imqtt) - 基于 IPython 的交互式 MQTT 数据包操作 shell。
- [IoT-Testware](https://projects.eclipse.org/projects/technology.iottestware) - Eclipse IoT-Testware 是 IoT 协议一致性测试套件的集合，其中包含用于模糊测试和性能测试的附加工具。
- [LabOverWire](https://laboverwire.com/features) - 用于设计 MQTT 拓扑的可视化图表编辑器，使用 Rust (WASM) 和 TypeScript 构建。具有实时浏览器内模拟、代码生成和 AsyncAPI 导出功能。
- [Mer-cli](https://github.com/iotmertech/iot-data-generator) - 用 Rust 编写的高性能物联网数据生成器。支持 MQTT、HTTP 和 TCP，以便使用 Handlebars 模板模拟真实的传感器负载。
- [mockd](https://github.com/getmockd/mockd) - 多协议模拟服务器，具有内置 MQTT 代理，支持 QoS 0-2、保留消息、主题模式和用于 IoT 开发和测试的设备模拟。
- [moxy](https://github.com/jvermillard/moxy) - Golang MQTT 代理提供有用的输出跟踪来监控 MQTT 通信并对其进行故障排除。
- [MQTT Board](https://github.com/flespi-software/MQTT-Board) - 面向诊断的开源 MQTT 客户端工具。
- [mqtt-admin](https://github.com/hobbyquaker/mqtt-admin/) - 基于 Web 的 MQTT 前端。 [直接链接](https://hobbyquaker.github.io/mqtt-admin/)。
- [mqtt-benchmark](https://github.com/chirino/mqtt-benchmark) - MQTT 服务器的基准测试工具。
- [MQTT CLI](https://github.com/hivemq/mqtt-cli) - 用于连接支持 MQTT 5.0 和 3.1.1 的各种 MQTT 客户端的命令行界面。
- [mqtt-client](https://github.com/sdeancos/mqtt-client) - 简单的 MQTT 客户端命令行 (Python)（使用 paho lib）。
- [mqtt-forget](https://github.com/hobbyquaker/mqtt-forget) - 用于通过通配符删除保留的 MQTT 主题的命令行工具。
- [mqtt-fuzz](https://github.com/F-Secure/mqtt_fuzz) - MQTT 协议的简单模糊器。
- [mqtt-malaria](https://github.com/etactica/mqtt-malaria) - 适用于 MQTT 环境的可扩展性和负载测试实用程序。
- [mqtt-mirror](https://github.com/4nte/mqtt-mirror) - 将 MQTT 流量从一个代理镜像到另一个代理。可作为 CLI 工具、Helm 图表或 Docker 映像使用。
- [mqtt_recorder](https://github.com/rpdswtk/mqtt_recorder) - 用于记录和重放 MQTT 消息的简单 cli 工具。
- [mqtt-shell](https://github.com/pidster-dot-org/mqtt-shell) - MQTT 的简单交互式 shell。
- [mqtt-spy](https://kamilfb.github.io/mqtt-spy/) - 基于 Java 的 MQTT 前端。支持脚本。
- [mqtt-studio](https://www.mqttstudio.com) - 实用的 MQTT 工具，具有创新的 UI，专为开发人员高效创建、测试和管理基于 MQTT 的应用程序而设计，从而增强他们的开发和支持工作流程。
- [mqtt_tree](https://github.com/poggenpower/mqtt_tree) - 在可展开的树中显示所有主题，如果您有很多客户发布，有助于获得概览。 （蟒蛇，tkinter）
- [mqtt-utils](https://github.com/dsell/mqtt-utils) - MQTT 实用程序的集合。
- [mqtt-wall](https://github.com/bastlirna/mqtt-wall) - 仅订阅基于 Web 的客户端 – 例如 MQTT 的 Twitter wall。
- [mqtt-wildcard](https://github.com/hobbyquaker/mqtt-wildcard) - 用于将 MQTT 主题与通配符进行匹配的 Node.js 模块。
- [MQTT.fx](https://mqttfx.jensd.de/) - 基于 Eclipse Paho 用 Ja​​va 编写的 MQTT 客户端。支持脚本。
- [mqttcli](https://github.com/shirou/mqttcli) - 用于 shell 脚本编写的 MQTT 客户端。
- [MQTTInspector](https://github.com/ckrey/MQTTInspector) - 适用于 iOS（iPhone 和 iPad）的通用 MQTT 测试应用程序。
- [MQTTLens](https://chrome.google.com/webstore/detail/mqttlens/hemojaaeigabkbcookmlgmdigohjobjm) - 一个 Google Chrome 应用程序，连接到 MQTT 代理并能够订阅和发布 MQTT 主题。
- [MQTT Explorer](https://mqtt-explorer.com/) - 用于在主题层次结构中可视化 MQTT 主题的工具，就像一把 MQTT 瑞士军刀。
- [MQTT TUI](https://github.com/EdJoPaTo/mqttui) - 基于简单轻量级终端的 MQTT 监控器和发布器。
- [Python MQTT Client Shell](https://github.com/bapowell/python-mqtt-client-shell) - 基于文本控制台的交互式 shell，用于执行与 MQTT 客户端通信相关的各种任务。
- [SimpleMQTT](https://simplemqtt.theoi.de/) - 一个 Slack 应用程序，用于使用斜杠命令将消息从 Slack 发送到 MQTT 代理。
- [Wireshark-MQTT](https://github.com/menudoproblema/Wireshark-MQTT) - Wireshark 的 MQTT 解析器。
- [VSMQTT](https://github.com/rpdswtk/vsmqtt) - 集成在 Visual Studio Code 中的简单 MQTT 客户端。
- [MQTTX](https://github.com/emqx/MQTTX) - EMQ 开源的跨平台 MQTT 桌面客户端，支持 macOS、Linux 和 Windows。
- [MIMIC MQTT Simulator](https://www.gambitcomm.com/site/mqttsimulator.php) - 每台服务器模拟多达 100,000 个 MQTT 客户端，用于物联网应用程序的开发/测试/部署。
- [mqtt-stats](https://github.com/gambitcomminc/mqtt-stats) - 订阅者客户端监控 MQTT 主题统计信息。
- [mqtt_monitor](https://github.com/filipsPL/mqtt-monitor) - 用于 mqtt 主题的简单轻量级控制台监视器，具有养眼效果，采用 python 3 语言。
- [mqttcommander](https://github.com/vroomfondel/mqttcommander) - 基于控制台的 MQTT 客户端和命令器，对于 IoT、Tasmota 和 Node-RED 设置特别有用。
- [mqttv5](https://github.com/LabOverWire/mqtt-lib) - 统一 MQTT v5.0 CLI，用于发布、订阅、运行代理以及通过多传输支持进行基准测试。

## 客户


### 多平台

- [Paho](https://www.eclipse.org/paho/) - 适用于 C、C++、Java、Python、JavaScript、GoLang、C#、Rust、Android 和嵌入式 (Arduino/mbed) 的开源客户端实现。
- [mosquitto-clients](https://mosquitto.org/download/) - [mosquitto_pub](https://mosquitto.org/man/mosquitto_pub-1.html) 和 [mosquitto_sub](https://mosquitto.org/man/mosquitto_sub-1.html) 适用于大多数操作系统的 CLI 客户端，以及 [libmosquitto](https://mosquitto.org/man/libmosquitto-3.html) 用于集成。

### 蟒蛇

- [aiomqtt](https://github.com/empicano/aiomqtt) - 惯用的 asyncio MQTT 客户端。
- [gmqtt](https://github.com/wialon/gmqtt) - Python MQTT v5.0 客户端（基于异步）。
<!--lint disable double-link-->
- [hbmqtt Client](https://github.com/beerfactory/hbmqtt) - 使用 asyncio 的 Python MQTT 客户端。
<!--lint enable double-link-->
- [MiniMQTT](https://github.com/adafruit/Adafruit_CircuitPython_MiniMQTT) - CircuitPython 的 MQTT 客户端库。

### JavaScript

- [MQTT.js](https://github.com/mqttjs) - Node.js 的 MQTT 客户端。
- [mqtt-elements](https://github.com/mqttjs/mqtt-elements) - 用于 MQTT 的聚合物元件。
- [mqtt-wrapper](https://www.webcomponents.org/element/hobbyquaker/mqtt-wrapper/elements/mqtt-wrapper) - 聚合元素，包装其他元素并将它们链接到 MQTT 主题。
<!--lint disable double-link-->
- [Vert.x Client](https://github.com/vert-x3/vertx-mqtt) - Vert.x 组件提供连接/断开与代理、发布消息和订阅主题的方法。
<!--lint enable double-link-->

### 爪哇

- [hivemq-mqtt-client](https://github.com/hivemq/hivemq-mqtt-client) - 高性能 Java MQTT 客户端库，具有适用于 MQTT 5.0 和 3.1.1 的不同 API 风格。

### Erlang 或 Elixir

- [emqttc](https://github.com/emqx/emqtt) - 异步 Erlang MQTT 客户端。
- [mqttex](https://github.com/alfert/mqttex) - Elixir 中的 MQTT 实现。

### 芭蕾舞女演员

- [ballerina-mqtt](https://github.com/ballerina-platform/module-ballerina-mqtt) - 基于 paho-mqtt 的 Ballerina MQTT 客户端。

### C 或 C++

- [mqtt_cpp](https://github.com/redboltz/mqtt_cpp) - 基于 Boost.Asio 的 C++14 MQTT 客户端。
- [MQTT-C](https://github.com/LiamBindle/MQTT-C) - 适用于嵌入式系统和 PC 等的便携式 MQTT C 客户端。
- [wolfMQTT](https://www.wolfssl.com/products/wolfmqtt/) - 用 C 编写的 MQTT 客户端实现，供嵌入式使用。它通过 WolfSSL 库支持 SSL/TLS。

### 克洛尤尔

- [Machine Head](https://github.com/clojurewerkz/machine_head) - Clojure MQTT 客户端。

### 飞镖

- [mqtt.dart](https://github.com/jnguillerme/mqtt.dart) - Dart MQTT 客户端。

### C#/.NET

- [HiveMQtt](https://github.com/hivemq/hivemq-mqtt-client-dotnet) - 符合 MQTT 5.0 标准的安全客户端，具有自动背压管理和 TCP 和 WebSocket 传输支持。
- [MQTTnet](https://github.com/chkr1011/MQTTnet) - MQTT 客户端和代理 .NET 实现。

### 德尔福

- [delphi-mqtt](https://github.com/pjde/delphi-mqtt) - MQTT 服务器和客户端组件。
- [TMQTTClient](https://github.com/jamiei/Delphi-TMQTT2) - Delphi 的 MQTT 客户端库。 Alpha 且长期未维护。

### Go语言

- [go-mqtt](https://github.com/go-mqtt/mqtt) - MQTT 客户端。
- [MQTT for Go](https://github.com/jeffallen/mqtt) - Go 中的 MQTT 客户端、服务器和负载测试器。

### 卢阿

- [luamqtt](https://github.com/xHasKx/luamqtt/) - Pure-lua MQTT v3.1.1 和 v5.0 客户端。
- [mqtt_lua](https://geekscape.github.io/mqtt_lua/) - Lua 语言的 MQTT 客户端库。

### Objective-C

- [MQTT-Client-Framework](https://github.com/novastone-media/MQTT-Client-Framework) - iOS、macOS、tvOS 原生 ObjectiveC MQTT 客户端框架。
- [MQTTKit](https://github.com/mobile-web-messaging/MQTTKit) - 适用于 iOS 的 MQTT Objective-C 客户端。

### PHP

- [Mosquitto-PHP](https://github.com/mgdm/Mosquitto-PHP) - PHP 的 Mosquitto MQTT 客户端库的包装器。

### 红宝石

- [ruby-mqtt](https://github.com/njh/ruby-mqtt) - 实现 MQTT 协议的纯 Ruby gem。

### 铁锈

- [mqtt-rs](https://github.com/zonyitoo/mqtt-rs) - Rust 的 MQTT 协议库。
- [rumqtt](https://github.com/AtherEnergy/rumqtt) - 一个快速、无锁的纯 Rust MQTT 客户端。
- [mqtt5](https://github.com/LabOverWire/mqtt-lib) - 适用于 Rust 的完整异步 MQTT v5.0 客户端和代理库，支持 TCP、TLS、WebSocket 和 QUIC。

### 斯威夫特

- [CocoaMQTT](https://github.com/emqx/CocoaMQTT) - 使用 Swift 编写的适用于 iOS 和 macOS 的 MQTT。
- [Moscapsule](https://github.com/flightonary/Moscapsule) - 用 Swift 编写的 iOS MQTT 客户端。

### TCL

- [tcl-mqtt](https://github.com/Tingenek/tcl-mqtt) - 用于连接到 MQTT 代理的小型库。非常非常基本，而且没有维护。

## 脚本编写

- [logic4mqtt](https://github.com/owagner/logic4mqtt) - 基于 Java 的逻辑和脚本引擎，可与 MQTT 一起使用。使用 Java 的通用脚本接口，因此可以用多种语言编写脚本，例如 JavaScript、Groovy 等。
- [mqtt-scripts](https://github.com/hobbyquaker/mqtt-scripts/) - 基于 Node.js 的脚本运行器。
- [Node-RED](https://nodered.org/) - 用于连接物联网的可视化工具。

## 接口

### 创客

- [arduinoTemps2mqtt](https://github.com/matbor/arduinoTemps2mqtt) - Arduino 草图，获取单线温度并发布到 MQTT 代理。
- [Basecamp](https://github.com/ct-Open-Source/Basecamp) - 一个 Arduino 库，可简化 ESP32 在 IoT 项目中的使用。请参阅 [c't Magazin 2'2018（德语）](https://www.heise.de/select/ct/2018/2/1515452111258448)。
- [deskmate](https://github.com/rbaron/deskmate) - 可破解且便携式、由 MQTT 驱动的迷你仪表板和控制中心。
- [MySensors](https://www.mysensors.org/) - 基于 Arduino NRF24L01 的传感器网络，支持 MQTT 网关。
- [RFM69-MQTT-client](https://github.com/computourist/RFM69-MQTT-client) - 基于 Arduino RFM69 的传感器和 MQTT 网关。
- [rpi2mqtt](https://github.com/hobbyquaker/rpi2mqtt) - 将 RaspberryPis GPIO 和 1-Wire 温度传感器连接到 MQTT。
- [xbee2mqtt](https://github.com/xoseperez/xbee2mqtt) - XBee 到 MQTT 网关。

#### ESP
- [pubsubclient](https://github.com/knolleary/pubsubclient) - Arduino 以太网扩展板的客户端库，提供 MQTT 支持。
- [ESP32-BLE2MQTT](https://github.com/shmuelzon/esp32-ble2mqtt) - BLE 到 MQTT 桥接器，将 BLE GATT 特性公开为用于双向通信的 MQTT 主题。
- [ESP8266MQTTMesh](https://github.com/PhracturedBlue/ESP8266MQTTMesh) - 适用于 ESP8266 的 MQTT over mesh WiFi 集成库。
- [esp_mqtt](https://github.com/tuanpmt/esp_mqtt) - 适用于 ESP8266 的 MQTT 客户端库。
- [mqtt-ir-transceiver](https://github.com/piotrC4/mqtt-ir-transceiver) - 基于 ESP8266 的 MQTT 和 IR 之间的双向网关。与 PlatformIO 一起使用。
- [mqtt-with-micropython](https://docs.pycom.io/tutorials/networkprotocols/mqtt/) - 使用 micropython 和 wipy/其他（内置 ESP32）连接到 MQTT。
- [nodemcu-gpiomqtt](https://github.com/hobbyquaker/nodemcu-gpiomqtt) - 用于将 ESP8266 GPIO 连接到 MQTT 的 Lua 脚本。


#### 基于 ESP 的设备的固件

有许多基于廉价 ESP8266 芯片的廉价智能家居 Wi-Fi 设备*（参见：[1](https://templates.blakadder.com/index.html)、[2](https://github.com/xoseperez/espurna/wiki/Hardware)、[3](https://www.letscontrolit.com/wiki/index.php?title=ESP_Hardware))*。其中大多数都可以使用自定义固件进行刷新。
以下是将它们变成 MQTT 控制的智能家居节点的完整固件：

- [ESPEasy](https://www.letscontrolit.com/wiki/index.php?title=ESPEasy) - 将 ESP 转变为多功能传感器设备，用于具有基于 Web 配置的 <abbr title="家庭自动化">HA</abbr> 解决方案。
- [ESPHome](https://esphome.io/) - 根据简洁的 YAML 描述构建 ESP8266/ESP32 固件，上传到闪存设备并进行管理。
- [Espurna](https://github.com/xoseperez/espurna) - <abbr title="家庭自动化">HA</abbr> 固件，适用于基于 ESP8266 的设备，具有丰富的 Web UI 和开箱即用的支持 ≈120 台设备。
<!--lint disable double-link-->
- [HomeGenie Mini](https://homegenie.it/) - 适用于 ESP8266/ESP32 的智能设备固件，支持通过 MQTT 进行远程监控和端到端加密控制。该固件是开源的，可以直接从网站上传到ESP设备。
<!--lint enable double-link-->
- [OpenMQTTGateway](https://github.com/1technophile/OpenMQTTGateway) - 适用于 ESP8266、ESP32、Sonoff RF Bridge 或 Arduino 的 MQTT 网关，具有双向 433mhz/315mhz/868mhz、红外通信、BLE、信标检测、mi flora、mi jia、LYWSD02、LYWSD03MMC、Mi Scale 兼容性、SMS 和 LORA。
- [Sonoff-Tasmota](https://github.com/arendst/Tasmota) - 具有基于 Web 配置的 ESP8266 设备的固件。支持约 500 个设备（不仅仅是 Sonoffs）。
- [WiFi-IoT](https://wifi-iot.com/p/wiki/) - ESP8266/ESP32 固件生成器。部分是俄语。免费功能有限。


### 工业

- [CODESYS-MQTT](https://github.com/stefandreyer/CODESYS-MQTT) - CODESYS PLC 的 MQTT 客户端。
- [spicierModbus2mqtt](https://github.com/mbs38/spicierModbus2mqtt) - Modbus 主站通过 MQTT 发布寄存器值。
- [mqtt2opcua](https://github.com/nzfarmer1/mqtt2opcua) - 双向 MQTT 到 OPCUA 桥。
- [OPC Router](https://www.opc-router.com/4_1-mqtt-client-opc-router-plug-in-en/) - 带有各种插件（OPC UA Bridge、SQL Bridge、REST Bridge、SAP Bridge）的 MQTT 网关（发布者/订阅者）。


### 电话、集团电话

- [agi-mqtt](https://github.com/zeha/agi-mqtt) - Asterisk 和 MQTT 之间的接口。
- [fritz2mqtt](https://github.com/akentner/fritz2mqtt) - 将 FRITZ!Box 连接到 MQTT。
- [sip2mqtt](https://github.com/MartyTremblay/sip2mqtt) - 一个 SIP 监控脚本，将带有 CallerID 的来电发布到 MQTT。
- [sms2mqtt](https://github.com/Domochip/sms2mqtt) - Docker 网关使用 USB GSM 加密狗 (gammu) 通过 MQTT 发送/接收 SMS。


### 操作系统

- [updates2mqtt](https://updates2mqtt.rhizomatics.org.uk) - 检查 Docker 镜像更新并发布到 MQTT，以支持 Home Assistant 的自动更新和发现。
- [mqtt-os-status](https://github.com/oskarhagberg/mqtt-os-status) - 操作系统相关数据，以固定时间间隔发布到 MQTT 代理。
- [mqttlauncher](https://github.com/jpmens/mqtt-launcher) - 执行由已发布的 MQTT 消息触发的 shell 命令。
- [mqttpc](https://github.com/hobbyquaker/mqttpc) - 通过 MQTT 控制流程。能够通过 MQTT 发送信号并发布 stdout/stderr 或将 MQTT 有效负载通过管道传输到 stdin。
- [mqttwatchdir](https://github.com/jpmens/mqtt-watchdir) - 递归地监视目录的修改并将文件内容发布到 MQTT 代理。
- [psmqtt](https://github.com/eschava/psmqtt) - 实用程序通过 MQTT 报告系统运行状况和状态。
- [WinThing](https://github.com/msiedlarek/winthing) - 通过 MQTT 远程控制 Windows。


### 监控

- [mqttwarn](https://mqttwarn.readthedocs.io/en/latest/) - 使用 70 多个用于数据库、消息传递和其他通知接收器的内置适配器来路由和转换 MQTT 通知。
- [snmp2mqtt](https://c0d3.sh/andre/snmp2mqtt) - 基于 Python 的 SNMP v2 和 v3 桥接到 MQTT，该项目将于 2025 年末活跃。
- [ccusage-mqtt](https://github.com/george-vice/ccusage-mqtt) - 通过 Home Assistant 自动发现将 Claude Code（Anthropic 的 AI 编码代理）使用情况遥测发布到 MQTT。 15 个传感器，情绪分类器。
- [check-mqtt](https://github.com/jpmens/check-mqtt) - 用于检查 MQTT 代理连接的 Nagios/Icinga 插件。
- [nag2mqtt](https://github.com/DE-IBH/nag2mqtt) - Nagios 事件代理到 MQTT 网关。
- [notify-by-mqtt](https://github.com/jpmens/notify-by-mqtt) - Nagios/Icinga 通知模块将数据包装成 JSON 并将其发送到 MQTT 代理。
- [mqtt2notifysend](https://github.com/David-Lor/MQTT2NotifySend) - 订阅主题并在 Ubuntu 和其他通知发送兼容的 Linux 发行版上显示来自 MQTT 消息的通知。


### 位置追踪

- [OwnTracks](https://owntracks.org/) - MQTT 的位置跟踪和地理围栏。

### 记录

- [graylog-plugin-mqtt](https://github.com/graylog-labs/graylog-plugin-mqtt) - Graylog 的 MQTT 输入插件。
- [influx4mqtt](https://github.com/hobbyquaker/influx4mqtt) - 订阅 MQTT 主题并插入到 InfluxDB 中。
- [mqtt2elasticsearch](https://github.com/hobbyquaker/mqtt2elasticsearch) - 将 MQTT 消息发送到 Elasticsearch。
<!--lint disable double-link-->
- [mqttwarn](https://github.com/jpmens/mqttwarn) - 与 [carbon](https://mqttwarn.readthedocs.io/en/latest/notifier-catalog.html#carbon) 插件一起使用。
<!--lint enable double-link-->
- [mqttcollect](https://github.com/jpmens/mqttcollect) - MQTT 的collectd“Exec”插件。
- [mqtthandler](https://github.com/changyuheng/MQTTHandler) - 用于 MQTT 的 Python 日志处理程序模块。
- [mqtt2mongodb](https://github.com/David-Lor/MQTT2MongoDB) - 订阅 MQTT 主题并插入到 MongoDB 中。


### 智能家居硬件接口

- [airrohr2mqtt](https://c0d3.sh/smarthome/airrohr2mqtt) - 空气质量监测集成。
- [amcrest2mqtt](https://github.com/dchesterton/amcrest2mqtt) - Amcrest 门铃到 MQTT 桥接器。使用 Home Assistant 的 MQTT 发现协议。
- [ble-scale-sync](https://github.com/KristianP26/ble-scale-sync) - 用于智能秤（23 个品牌）的 BLE 至 MQTT 桥接器，具有 Home Assistant 自动发现功能。读取体重 + 阻抗，计算身体成分，发布所有 11 个带有 LWT 的指标并显示精度。 [网站](https://blescalesync.dev)。
- [aqara-mqtt](https://github.com/monster1025/aqara-mqtt) - Aqara（小米）MQTT 桥接器的网关。
- [aqara2mqtt](https://github.com/hobbyquaker/aqara2mqtt) - 将 [Aqara](https://www.aqara.com) 智能集线器连接到 MQTT。
- [Bambuddy](https://github.com/maziggy/bambuddy) - 使用 MQTT 的 Bambu Lab 3D 打印机自托管管理工具，具有实时监控、调度和家庭助理集成功能。
- [can2mqtt](https://github.com/c3re/can2mqtt) - CAN-Bus - MQTT 桥（反之亦然）。
- [coe2mqtt](https://c0d3.sh/smarthome/coe2mqtt) - 双向 CAN 总线至 MQTT。
- [cul2mqtt](https://github.com/hobbyquaker/cul2mqtt) - [Busware CUL](https://shop.busware.de/product_info.php/cPath/1/products_id/29)（868MHz RF 设备，如 ELV FS20、HMS、EM 等）和 MQTT 之间的接口。
- [domiqtt](https://github.com/etobi/domiqtt) - 连接到 Domiq Base (LCN) 并在 MQTT 之间进行转换。
- [eno2mqtt](https://github.com/owagner/eno2mqtt) - Enocean USB300 (TCM310) 适配器和 MQTT 之间的接口。
- [Evohome2mqtt](https://github.com/svrooij/evohome2mqtt) - Honeywell Evohome 系统的 MQTT 接口。
- [fronius2mqtt](https://c0d3.sh/smarthome/fronius2mqtt) - Fronius SolarAPI 的 MQTT 集成。
- [gardena2mqtt](https://github.com/Domochip/gardena2mqtt) - Docker Gateway 通过 MQTT 控制 GARDENA 智能系统设备（Sileno 割草机、灌溉控制等）。
- [helios2mqtt](https://github.com/mreschka/helios2mqtt) - 用于将 helios easy 控制系统（例如我的 KWL EC 220D）同步到 MQTT 的守护进程。
- [hm2mqtt.js](https://github.com/hobbyquaker/hm2mqtt.js) - EQ-3 的 Homematic 系列智能家居设备与 MQTT 之间的接口。支持家庭IP。
- [homeeToMqtt](https://github.com/odig/homeeToMqtt) - homee 和 MQTT 之间的双向接口。
- [HS100toMQTT](https://github.com/dersimn/HS100toMQTT) - TPLink HS100/HS110 和 MQTT 之间的网关。
- [huABus](https://github.com/arboeh/huABus) - 适用于华为太阳能逆变器 (SUN2000/3000/5000) 的家庭助理应用程序（附加）和 MQTT 桥。
- [ipcam2mqtt](https://github.com/svrooij/ipcam2mqtt) - 一个小型 FTP 服务器，用于接收来自 ipcameras 的运动图像并将其转换为 MQTT 警报。
- [knx-mqtt-bridge](https://github.com/pakerfeldt/knx-mqtt-bridge) - 使用 knx.js 库桥接 KNX 和 MQTT。
- [knx2mqtt](https://github.com/owagner/knx2mqtt) - KNX 家庭自动化标准和 MQTT 之间的接口。
- [mcsMQTT](https://shop.homeseer.com/products/mcsmqtt-software-plug-in-for-hs3) - HS3 (HomeSeer) 插件。
- [mqtt-dss-bridge](https://github.com/cgHome/mqtt-dss-bridge) - MQTT digitalSTROM 服务器桥。
- [mqtt-unifi-protect-bridge](https://github.com/terafin/mqtt-unifi-protect-bridge) - 将运动状态从 UniFi Protect 相机添加到 MQTT。
<!--lint disable double-link-->
- [mqtt2homekit](https://github.com/forty2/mqtt2homekit) - 与 [homekit2mqtt](https://github.com/hobbyquaker/homekit2mqtt) 大致相反：使用 MQTT 控制支持 HomeKit 的设备，无需 Siri 或 iPhone。
<!--lint enable double-link-->
- [node-lox-mqtt-gateway](https://github.com/alladdin/node-lox-mqtt-gateway) - Loxone™ 迷你服务器与 MQTT 代理通信的网关。
- [smartthings-mqtt-bridge](https://github.com/stjohnjohnson/smartthings-mqtt-bridge) - [SmartThings](https://www.smartthings.com/) 和 MQTT 之间的桥梁。
- [xiaomi2mqtt](https://github.com/svrooij/node-xiaomi2mqtt) - 小米智能家居网关 Aquara 和 MQTT 服务器之间的桥梁。
- [zigbee2mqtt](https://github.com/Koenkk/zigbee2mqtt) - 允许您在没有供应商（Xiaomi/TRADFRI/Hue）桥/网关的情况下使用 Zigbee 设备。
- [zwavejs2mqtt](https://github.com/zwave-js/zwavejs2mqtt) - Zwave 到 Mqtt 网关和控制面板 Web UI。


### 智能家居集成软件

- [Home Assistant](https://www.home-assistant.io) - 具有原生 MQTT 支持的家庭自动化系统，以及世界上最大的非商业开源项目。
- [Domoticz](https://www.domoticz.com/) - 支持 MQTT 的家庭自动化系统。
- [FHEM](https://fhem.de/fhem.html) - 自 V5.6 起包含 [MQTT 模块](https://fhem.de/commandref.html#MQTT)。
- [Home.Pi](https://github.com/denschu/home.pi) - 基于MQTT。
- [Homegear](https://homegear.eu/index.php/Main_Page) - 内置 MQTT 支持。
<!--lint disable double-link-->
- [HomeGenie](https://homegenie.it/) - 支持通过端到端加密的 MQTT 进行远程控制和监控。
- [homekit2mqtt](https://github.com/hobbyquaker/homekit2mqtt) - [HAP-NodeJS](https://github.com/homebridge/HAP-NodeJS) 和 MQTT 之间的接口。使用 Siri 或 HomeKit 应用程序控制 MQTT 连接的设备。
<!--lint enable double-link-->
- [ioBroker](https://github.com/ioBroker) - 包括 [MQTT 适配器](https://github.com/ioBroker/ioBroker.mqtt)。
- [openHAB](https://github.com/openhab) - 包括 [MQTT 绑定](https://github.com/openhab/openhab1-addons/wiki/MQTT-Binding)。
- [openLuup](https://github.com/akbooer/openLuup) - 使用 MQTT 对 Vera Luup 家庭自动化环境进行纯 Lua 开源仿真。
- [pimatic](https://pimatic.org/) - 包含 MQTT 插件。
- [shopsavvy-mqtt](https://github.com/shopsavvy/shopsavvy-mqtt) - MQTT 桥，通过 Home Assistant MQTT 发现支持发布产品价格数据。
- [knx2mqtt](https://c0d3.sh/smarthome/knx2mqtt) - Telegram 双向集成作为 HomeAssistant 内置支持的替代方案。


### 照明

- [Arilux_AL-LC0X](https://github.com/mertenats/Arilux_AL-LC0X) - 这是使用 MQTT 的 Arilux LED 控制器的替代固件。
- [chromoflex2mqtt](https://github.com/owagner/chromoflex2mqtt) - 通过 MQTT 控制 Chromoflex USP3 RGB LED 模块。
- [hue2mqtt.js](https://github.com/hobbyquaker/hue2mqtt.js) - Philips Hue 桥和 MQTT 之间的接口。
- [MQTT DMX Controller](https://github.com/hobbyquaker/mqtt-dmx-controller) - 支持 MQTT 的 DMX 控制器。
- [mqtt-dmx-sequencer](https://github.com/hobbyquaker/mqtt-dmx-sequencer) - MQTT DMX 控制器的无头对应物 - 使用从 MQTT DMX 控制器导出的场景和序列并通过 MQTT 控制它们。
- [sunricher-wifi-mqtt](https://github.com/magcode/sunricher-wifi-mqtt) - 使用 MQTT 控制 Sunricher LED 设备。
- [TRADFRI2MQTT](https://github.com/hardillb/TRADFRI2MQTT) - 适用于宜家 TRÅDFRI 灯光网关的 MQTT 桥。


### 家庭娱乐

- [airtunes2mqtt](https://github.com/hobbyquaker/airtunes2mqtt) - MQTT 通过 Airplay/Airtunes 设备控制多房间音频。
- [bravia2mqtt](https://github.com/forty2/bravia2mqtt) - 使用 MQTT 控制您的 Sony Bravia 电视。
- [broadlink-mqtt](https://github.com/eschava/broadlink-mqtt) - 用于控制 BroadLink RM 设备的 MQTT 客户端。
- [chromecast-mqtt-connector](https://github.com/nohum/chromecast-mqtt-connector) - 使用 MQTT 控制您的 Google Chromecast 设备。
- [harmony-api](https://github.com/maddox/harmony-api) - 一个简单的服务器，允许您通过 HTTP 或 MQTT 查询/控制多个本地 Harmony Home Hub。
- [htd2mqtt](https://github.com/TheOriginalAndrobot/htd2mqtt) - HTD Lync 音频系统和 MQTT 之间的桥梁。
- [kodi2mqtt](https://github.com/owagner/kodi2mqtt) - Kodi 媒体中心实例与 MQTT 之间的接口。
- [lgtv2mqtt](https://github.com/hobbyquaker/lgtv2mqtt) - LG WebOS 智能电视和 MQTT 之间的接口。
- [lirc2mqtt](https://github.com/hobbyquaker/lirc2mqtt) - 通过 [LIRC](https://www.lirc.org) 发送和接收红外线。
- [mopidy-mqtt](https://github.com/magcode/mopidy-mqtt) - Mopidy 的 MQTT 功能。
- [MQTT-DashCast-Docker](https://github.com/mukowman/MQTT-DashCast-Docker) - MQTT Docker 在 Chromecast 上启动 DashCast 会话。
- [mqtt2atlonamatrix](https://github.com/forty2/mqtt2atlonamatrix) - 使用 MQTT 控制 Atlona HDMI 矩阵开关。
- [mqtt2tivoremote](https://github.com/forty2/mqtt2tivoremote) - 通过 MQTT 智能家居风格界面实现 TiVo DVR 远程控制。
- [onkyo2mqtt](https://github.com/owagner/onkyo2mqtt) - Onkyo AVR 的 EISCP 网络远程协议和 MQTT 之间的接口。使用 onkyo-eiscp 库。
- [sonos2mqtt](https://github.com/svrooij/sonos2mqtt) - Sonos 和 MQTT 之间的桥梁。
- [VLC MQTT Module](https://wiki.videolan.org/Documentation:Modules/mqtt/) - 通过 MQTT 控制 VLC。
- [xbmc2mqtt](https://github.com/gordonjcp/xbmc-mqtt) - XBMC 的一个简单插件，用于侦听 MQTT 代理上的特定主题，并显示弹出消息。
- [yamaha-avr2mqtt](https://github.com/akentner/yamaha-avr2mqtt) - 用于将 Yamaha AVR 连接到 MQTT 的简单适配器。


### 智能抄表

- [bcontrol2mqtt](https://github.com/hobbyquaker/bcontrol2mqtt) - 将 TQ Energy Manager / [Busch-Jäger Energy Monitor](https://www.busch-jaeger.de/files/files_ONLINE/Brosch%c3%bcre_EnergyMonitor_druck.pdf) 的测量结果发布到 MQTT。
- [rpi-mqtt-monitor](https://github.com/hjelev/rpi-mqtt-monitor) - 通过 MQTT 在 Home Assistant 中跟踪 Raspberry Pi 或 Ubuntu 计算机系统运行状况和性能的最简单方法。


### 消息传递

- [mqtt-irc-bot](https://github.com/dobermai/mqtt-irc-bot) - MQTT 到 IRC / IRC 到 MQTT 桥或机器人。
<!--lint disable double-link-->
- [mqttwarn](https://github.com/jpmens/mqttwarn) - 订阅 MQTT 主题（带通配符）并通知可插入服务。
<!--lint enable double-link-->
- [twitter-to-mqtt](https://github.com/knolleary/twitter-to-mqtt) - 一个 python 守护程序，使用 Twitter Streaming API 访问推文并将其重新发布到 MQTT 主题。


### 杂项

- [AlexaMqttBridge](https://github.com/mhdawson/AlexaMqttBridge) - Amazon Alexa 和 MQTT 之间的桥梁。
- [anpr2mqtt](https://anpr2mqtt.rhizomatics.org.uk) - 监听文件服务器上的图像，通过 MQTT Discovery 分析和创建 Home Assistant 实体。
- [bt-mqtt-gateway](https://github.com/zewelor/bt-mqtt-gateway) - 可轻松扩展蓝牙至MQTT网关，目前支持：EQ3智能恒温器、小米体重秤、Linak Desk、MySensors和小米Flora植物传感器。
- [buderus2mqtt](https://github.com/krambox/buderus2mqtt) - Buderus KM200 互联网网关和 MQTT 之间的桥梁。
- [chrome2mqtt](https://github.com/tbowmo/chrome2mqtt) - 用于启用 chromecast（音频和视频）的 MQTT 控制端点的 Python 程序。
- [dashbutton2mqtt](https://github.com/hobbyquaker/dashbutton2mqtt) - 将 Amazon Dash 按钮按下操作发布到 MQTT。
- [flowerpower2mqtt](https://github.com/hobbyquaker/flowerpower2mqtt) - 将 Parrot Flower Power 发电厂传感器的测量结果发布到 MQTT。
- [gBridge](https://github.com/kservices/gBridge) - 使用 Google Assistant 控制（几乎）任何智能家居设备、任何智能家居软件。因此，它将通过语音命令从 Google 收到的操作转换为 MQTT 消息。
- [haiku2mqtt](https://github.com/forty2/haiku2mqtt) - Haiku 智能粉丝和 MQTT 之间的桥梁。
- [homely](https://github.com/baol/homely) - 用于连接 Domoticz 和其他东西的 Go 守护进程的集合。
- [kobold2mqtt](https://github.com/krambox/kobold2mqtt) - Vorwerk Kobold Vr200 互联网网关和 MQTT 之间的桥梁。
- [leaf-python-mqtt](https://github.com/glynhudson/leaf-python-mqtt) - 从 Nissan Leaf API 提取数据并发布到 MQTT。
- [miflora-mqtt-daemon](https://github.com/ThomDietrich/miflora-mqtt-daemon) - 用于将小米 Mi Flora 植物传感器数据发送到 MQTT 代理的 Linux 服务。
- [MQTT.Cool](https://mqtt.cool) - 一个 Web 网关，可在通过自动限制向 Web 客户端发送实时数据时优化任何 MQTT 代理。
- [mqtt2ble](https://github.com/hardillb/mqtt2ble) - 一种将 MQTT 主题与 BLE Gatt 特性联系起来的方法。
- [mqttclpro](https://github.com/dc297/mqttclpro) - 带有任务集成 Android 应用程序的 MQTT 客户端。
- [mqttDB](https://github.com/hobbyquaker/mqttDB) - 具有 MQTT 接口的 JSON 存储。
- [mqtt-camera-streamer](https://github.com/robmarkcole/mqtt-camera-streamer) - 通过 MQTT 从连接的摄像机流式传输图像并使用 Streamlit 进行查看。
- [MQTT Joystick Controller](https://github.com/Vincenzo-Petrolo/MQTT-Joystick-Controller) - 开源 Android 应用程序可让您用智能手机控制一切。从 Google Play 下载。
- [mqtt-transformer](https://github.com/tg44/mqtt-transformer) - 一个简单的服务，它在 MQTT 上使用、转换并定期重新发布 json 消息。
- [node-mqtt-for-anki-overdrive](https://github.com/IBM-Cloud/node-mqtt-for-anki-overdrive) - 用于 Anki Overdrive 的 Node.js 控制器和 MQTT API。
- [parrot-sample](https://github.com/IBM-Cloud/parrot-sample) - 使用 MQTT 控制 Parrot AR 无人机的示例代码。
- [QuIXI](https://github.com/ixian-platform/QuIXI) - Ixian 去中心化 P2P 网络和 MQTT/REST 之间的桥梁。为具有后量子安全性的物联网设备启用加密的点对点消息传递（ML-KEM + AES-256 + ChaCha20）。
- [serial2mqtt](https://github.com/vortex314/serial2mqtt) - 仅通过串行端口将低成本微控制器连接到 MQTT 的 Linux 网关。
- [snowboy2mqtt](https://github.com/hobbyquaker/snowboy2mqtt) - 在 Snowboy 热词检测上发布 MQTT 消息。
- [speedtest2mqtt](https://github.com/hobbyquaker/speedtest2mqtt) - 运行 speedtest-cli 并通过 MQTT 发布结果。
- [unifi2mqtt](https://github.com/hobbyquaker/unifi2mqtt) - 将连接的客户端从 Ubiquiti Unifi 发布到 MQTT。
- [Valetudo](https://github.com/Hypfer/Valetudo) - 带有 MQTT 和 Web 界面的小米（Roborock）真空机器人固件。
- [wlan-thermo-mqtt-addon](https://bitbucket.org/IOcastor/wlan-thermo-mqtt-addon/) - 流行的 DIY 烧烤温度计的插件。
- [mqtt-tasker](https://github.com/stesie/TaskerMqtt) - Android Tasker mqtt 插件。
- [MQTT2ETCD](https://github.com/David-Lor/MQTT2ETCD) - MQTT-ETCD网关：通过MQTT将密钥PUT到ETCD上，并在MQTT主题上观察ETCD密钥变化。


## 可视化、仪表板

- [awtSCADA](https://github.com/larionovavi-stack/awtscada) - 支持 MQTT 的工业 SCADA/HMI 系统（加上 IEC 61850、OPC UA、Modbus TCP）。在任何浏览器中从单个 HTML 文件运行，零安装。 53个功能块，65个图形元素，实时趋势。
- [MQTT-Tiles](https://github.com/flespi-software/MQTT-Tiles) - 基于 MQTT 的物联网仪表板可视化工具。允许轻松共享仪表板。可与任何支持 WSS 协议的 MQTT 代理配合使用。
- [Crouton](https://github.com/edfungus/Crouton) - 仅使用 MQTT 和 JSON 接入您的 IOT 网络的仪表板。
- [d3-MQTT-Topic-Tree](https://github.com/hardillb/d3-MQTT-Topic-Tree) - 使用 d3 可折叠树和基于 Websockets 的 MQTT 的 MQTT 主题树查看器。
- [HelloIoT](https://github.com/adrianromero/helloiot) - MQTT 客户端和仪表板应用程序。
- [HOMR-REACT](https://github.com/klauserber/homr-react) - 可配置的 MQTT 可视化。
- [Linear MQTT Dashboard](https://github.com/ravendmaster/linear-mqtt-dashboard) - 简单、可定制的控制面板 - MQTT 客户端。
- [MMM-mqtt](https://github.com/javiergayala/MMM-mqtt) - 这是 MagicMirror² 的扩展。它提供了订阅 MQTT 主题并显示它们的功能。
- [MQTT Dash](https://play.google.com/store/apps/details?id=net.routix.mqttdash&hl=de) - Android 应用程序：使用该应用程序，您可以为支持 MQTT 的 IoT 智能家居设备和应用程序创建仪表板。
- [MQTT-Hyperdash](https://github.com/kollokollo/MQTT-Hyperdash) - 适用于 Linux/Raspberry Pi 的通用独立 MQTT 仪表板。
- [MQTT.Cool Test Client](https://testclient-cloud.mqtt.cool) - 用于测试 MQTT.Cool 和任何 MQTT 代理之间交互的 Web 界面。
- [mqtt-panel](https://github.com/fabaff/mqtt-panel) - MQTT 的 Web 界面。
- [mqtt-prometheus-message-exporter](https://github.com/tg44/mqtt-prometheus-message-exporter) - 一个小型服务，它将 mqtt 消息转换为 prometheus 指标。
- [mqtt-svg-dash](https://github.com/jpmens/mqtt-svg-dash) - 订阅 MQTT，从消息中提取 JSON 并使 SVG 页面上的灯光闪烁。
- [mqtt2highcharts](https://github.com/matbor/mqtt2highcharts) - 使用 Highcharts 绘制来自订阅的 MQTT 主题的实时编号数据。
- [MYHELLOIOT](https://adrianromero.github.io/myhelloiot/) - MQTT 仪表板应用程序。
- [node-red-dashboard](https://github.com/node-red/node-red-dashboard) - Node-RED 的仪表板 UI。
- [PlotJuggler](https://github.com/facontidavide/PlotJuggler) - 可视化时间序列（来源如：MQTT、Websockets、ZeroMQ、UDP等，支持JSON、CBOR、BSON、Message Pack等数据格式）。它是一个快速、强大且直观的跨平台工具。


<!--lint disable double-link-->
其他可用于创建可视化/仪表板的工具可以在[平台](#platforms)和[智能家居集成软件](#smart-home-integration-software)下找到。
<!--lint enable double-link-->

## 建筑、会议

- [mqtt-smarthome](https://github.com/mqtt-smarthome/mqtt-smarthome) - 以 MQTT 作为中央消息总线的智能家居自动化 - 架构提案。
- [The Homie Convention](https://github.com/homieiot/convention) - 适用于 IoT 的轻量级 MQTT 约定。

## 安全、加密

- [Let's Encrypt Mosquitto Docker Container](https://hub.docker.com/r/pythonlinks/letsencrypt-mosquitto) - 为经纪商提供更轻松的 TLS 证书管理。
- [mqttsa](https://github.com/stfbk/mqttsa) - 用于网络保护的代理错误配置检测。
- [MQTT-PWN](https://github.com/akamai-threat-research/mqtt-pwn) - IoT Broker 渗透测试和安全评估操作。
- [Teserakt E4](https://teserakt.io/) - MQTT 和其他 M2M 协议的端到端加密和密钥管理 – 开源和付费计划。
