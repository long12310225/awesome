# 很棒的物联网

<img src="iot-logo.png" align="right" width="100">

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome) [![Build Status](https://travis-ci.org/HQarroum/awesome-iot.svg?branch=master)](https://travis-ci.org/HQarroum/awesome-iot)

> 精彩的物联网项目和资源的精选列表。

受到 [awesome](https://github.com/sindresorhus/awesome) 列表的启发。

## 目录

- [Hardware](#hardware)
- [Software](#software)
  - [操作系统](#operating-systems)
  - [编程语言](#programming-languages)
  - [Frameworks](#frameworks)
  - [Middlewares](#middlewares)
  - [库和工具](#libraries-and-tools)
  - [Miscellaneous](#miscellaneous)
- [协议和网络](#protocols-and-networks)
- [Technologies](#technologies)
- [标准和联盟](#standards-and-alliances)
- [Resources](#resources)
  - [Books](#books)
  - [Articles](#articles)
  - [Papers](#papers)

### 硬件

- [Arduino](https://www.arduino.cc/) - Arduino 是一个基于易于使用的硬件和软件的开源电子平台。它适用于任何制作交互式项目的人。
- [BeagleBoard](http://beagleboard.org/) - BeagleBoard 是德州仪器 (TI) 与 Digi-Key 和 Newark element14 合作生产的低功耗开源硬件单板计算机。
- [Dragonboard](https://developer.qualcomm.com/hardware/dragonboard-410c) - DragonBoard 410c 是 Arrow Electronics 的产品，是基于中端 Qualcomm® Snapdragon™ 410E 处理器的开发板。它具有先进的处理能力、Wi-Fi、蓝牙连接和 GPS，全部封装在信用卡大小的电路板上。
- [ESP32](https://www.espressif.com/en/products/hardware/esp32/overview) - ESP32，ESP8266 的后继者。 ESP32 具有强大的硬件功能。高速双核处理器以及众多内置外设将取代互联产品中的微控制器。
- [HomeMaster](https://www.home-master.eu/) - DIN 导轨上基于 ESP32 的开源模块化智能家居平台。包括 MiniPLC 和 MicroPLC 控制器以及继电器、调光器、RGBCCT、电能计量、漏水和报警模块 - 所有这些都通过 ESPHome 和 Home Assistant 在本地运行。 [GitHub](https://github.com/isystemsautomation/homemaster-dev) 上的固件和原理图。
- [HummingBoard](https://www.solid-run.com/freescale-imx6-family/hummingboard/) - HummingBoard 是一个由三个支持 Linux 和 Android 的开源 SBC 组成的系列，基于 1GHz Freescale i.MX6 SoC，具有类似 Pi 的 26 引脚 I/O 连接器。
- [Intel Galileo](https://www-ssl.intel.com/content/www/us/en/do-it-yourself/galileo-maker-quark-board.html) - 英特尔® Galileo Gen 2 开发板是基于英特尔® 架构的 Arduino* 认证开发和原型开发板系列中的首款开发板，专为创客、学生、教育工作者和 DIY 电子爱好者而设计。
- [Microduino](https://www.microduino.cc/) - Microduino 和 mCookie 为各个年龄段的创客、设计师、工程师、学生和好奇的修补匠带来了功能强大、小型、​​可堆叠的电子硬件。构建开源项目或创建创新的新项目。
- [Node MCU (ESP 8266)](http://www.nodemcu.com/index_en.html) - NodeMCU 是一个开源物联网平台。它使用Lua脚本语言。它基于 eLua 项目，并基于 ESP8266 SDK 0.9.5 构建。
- [OLinuXino](https://www.olimex.com/Products/OLinuXino/open-source-hardware) - OLinuXino 是一款开源软件和开源硬件低成本（30 欧元）Linux 工业级单板计算机，具有 GPIO，能够在 -25°C 至 +85°C 的温度范围内运行。
- [Odroid](http://www.hardkernel.com/) - ODROID 的意思是“开放+Droid”。它是一个硬件和软件的开发平台。
- [Particle](https://www.particle.io) - 一套硬件和软件工具，可帮助您设计原型、扩展和管理物联网产品。
- [Pinoccio](https://www.open-electronics.org/pinoccio-wifi-mesh-networking-for-arduino-and-iot-available-now/) - Pinoccio 是一个为所有 IoT 设备添加网状网络功能和 WiFi 互联网访问的解决方案，并且与 Arduino 兼容。
- [PiSpot Show](https://github.com/GeiserX/PiSpot-Show) - 具有天气集成和 PiJuice 电池管理功能的 Raspberry Pi WiFi 优惠券显示系统。
- [PiSpot Watch](https://github.com/GeiserX/PiSpot-Watch) - 用于为 GPConnect 公司运行 PiSpot Watch（由 Raspberry Pi Zero 和 PaPiRus Zero 组成）的软件。
- [AutoPi](https://github.com/autopi-io/autopi-core) - AutoPi 加密狗的开源核心软件，这是一款基于 Raspberry Pi 的 OBD-II 设备，用于联网车辆远程信息处理、CAN 总线数据收集和汽车物联网应用。
- [Raspberry Pi](https://www.raspberrypi.org/) - Raspberry Pi 是一款低成本、信用卡大小的计算机，可插入计算机显示器或电视，并使用标准键盘和鼠标。它能够完成您期望台式计算机执行的所有操作，从浏览互联网和播放高清视频，到制作电子表格、文字处理和玩游戏。
- [Tessel](https://tessel.io/) - Tessel 是一个完全开源且社区驱动的物联网和机器人开发平台。它包含开发板、硬件模块附加组件以及在其上运行的软件。
- [UDOO](http://www.udoo.org) - UDOO 是一款带有集成 Arduino 2 兼容微控制器的单板计算机，专为计算机科学教育、创客世界和物联网而设计。
- [Raspberry Pi Pico](https://www.raspberrypi.com/products/raspberry-pi-pico/) - Raspberry Pi Pico 是一款小型、快速且多功能的开发板，配备了 Raspberry Pi 基金会开发的 RP2040 微控制器芯片。它还配备了 2.4GHz 802.11n 无线 LAN 变体，这使其非常适合物联网。
- [Rinho Telematics](https://rinho.com.ar/en) - 具有本机 CAN 总线 (J1939/FMS)、用于离线数据下载的 WiFi 回退以及 BLE 5.0 传感器的 GPS 跟踪器。与 Traccar 和 Wialon 兼容。
- [WisBlock](https://www.rakwireless.com/en-us/products/wisblock) - WisBlock 是一个模块化系统，可以轻松地将低功耗广域网 (LPWAN) 实施到物联网解决方案中。 WisBlock由基板、核心计算模块和多个传感器模块的组合组成。

### 软件

#### 操作系统

 - [Apache Mynewt](https://mynewt.apache.org/) - Apache Mynewt 是一个实时、模块化操作系统，适用于需要在电源、内存和存储限制下长时间运行的联网物联网设备。第一个提供的连接堆栈是 BLE 4.2。
 - [ARM mbed](http://www.mbed.com/) - ARM® mbed™ 物联网设备平台提供操作系统、云服务、工具和开发人员生态系统，使大规模创建和部署基于标准的商业物联网解决方案成为可能。
 - [Contiki](http://www.contiki-os.org/) - Contiki 是一个物联网开源操作系统。 Contiki 将微型低成本、低功耗微控制器连接到互联网。
 - [FreeRTOS](http://www.freertos.org/) - FreeRTOS 是一种流行的嵌入式设备实时操作系统内核，已被移植到 35 个微控制器上。
 - [Android Things](https://developer.android.com/things/) - **注意：Android Things 已被折旧。** Android Things 将 Android 平台扩展到所有连接的设备，因此它们易于设置，并且彼此之间以及与您的智能手机无缝协作。
 - [OpenWrt](https://openwrt.org/) - OpenWrt是一个基于Linux内核的操作系统（特别是嵌入式操作系统），主要用于嵌入式设备上路由网络流量。主要组件是 Linux 内核、util-linux、uClibc 或 musl 以及 BusyBox。所有组件都针对尺寸进行了优化，足够小，可以适应家庭路由器中有限的存储和内存。
 - [Snappy Ubuntu](https://wiki.ubuntu.com/Snappy) - Snappy Ubuntu Core 是带有事务更新的 Ubuntu 的新版本。  它提供了一个最小的服务器映像，具有与当今的 Ubuntu 相同的库，但应用程序是通过更简单的机制提供的。
 - [Mbed OS](https://os.mbed.com/) - 适用于物联网 (IoT) Cortex-M 板的开源操作系统：低功耗、受限且互联。 Mbed OS 为其运行的微控制器提供了一个抽象层，以便开发人员可以编写在任何支持 Mbed 的板上运行的 C/C++ 应用程序。
 - [NodeOS](http://node-os.com/) - NodeOS 是一个完全用 Javascript 编写的操作系统，并由 Linux 内核之上的 npm 进行管理。
 - [Raspbian](https://raspbian.org/) - Raspbian 是一个基于 Debian 的免费操作系统，针对 Raspberry Pi 硬件进行了优化。
 - [RIOT](http://www.riot-os.org/) - 友好的物联网操作系统。
 - [Tiny OS](https://github.com/tinyos/tinyos-main) - TinyOS 是一款获得 BSD 许可的开源操作系统，专为低功耗无线设备而设计，例如传感器网络、普适计算、个域网、智能建筑和智能电表中使用的设备。
 - [Toit](https://toit.io/) - Toit 平台结合了以强大、有弹性的方式为您的设备提供服务的功能，让您可以控制您的设备和数据，以及网络连接的嵌入式设备上即用型无线固件和应用程序更新。
 - [UBOS](https://ubos.net/) - UBOS 是一个 Linux 发行版，专注于使运行 Web 应用程序的家庭服务器和独立物联网设备的系统管理变得更加简单。它是 Arch Linux 的衍生版本，可以在 PC、Raspberry Pi、ESPRESSObin 和云上运行。
 - [Windows 10 IoT Core](https://dev.windows.com/en-us/iot) - Windows 10 IoT 是 Windows 10 版本系列，面向广泛的智能设备，从小型工业网关到大型更复杂的设备（例如销售点终端和 ATM）。
  - [Zephyr Project](https://www.zephyrproject.org/) - Zephyr™ 项目是一个可扩展的实时操作系统 (RTOS)，支持多种硬件架构，针对资源受限的设备进行了优化，并在构建时考虑了安全性。

#### 编程语言

> 本节重新组合了与嵌入式开发相关的每种出色的编程语言，无论是编译型、解释型还是 DSL。

 - [AtomVM](https://atomvm.org/) - 将 Erlang、Elixir、Gleam 和其他函数式语言引入微控制器。
- [C](https://en.wikipedia.org/wiki/C_(programming_language)) - 一种通用的命令式计算机编程语言，支持结构化编程、词法变量范围和递归，而静态类型系统可以防止许多意外操作。
 - [C++](https://en.wikipedia.org/wiki/C%2B%2B) - 一种通用编程语言。它具有命令式、面向对象和通用编程功能，同时还提供低级内存操作的设施。
 - [Groovy](http://www.groovy-lang.org/) - Groovy 是一种强大的、可选类型和动态语言，具有静态类型和静态编译功能，适用于 Java 平台，旨在通过简洁、熟悉且易于学习的语法来提高开发人员的工作效率。 SmartThings 开发环境使用它来创建智能应用程序。
 - [Lua](http://www.lua.org/) - Lua 是一种强大、快速、轻量级、可嵌入的脚本语言。 Lua 是动态类型的，通过解释基于寄存器的虚拟机的字节码来运行，并具有带增量垃圾收集的自动内存管理功能，使其成为配置、脚本和快速原型设计的理想选择。
 - [eLua](http://www.eluaproject.net/) - eLua 代表嵌入式 Lua，该项目为嵌入式世界提供了 Lua 编程语言的完整实现，并通过特定功能对其进行了扩展，以实现高效、可移植的软件嵌入式开发。
 - [ELFE](http://c3d.github.io/elfe/) - ELFE 是一种非常简单且小型的编程语言。虽然它是一种通用编程语言，但它经过专门调整以方便配置和控制大量小型设备（例如传感器或执行器）。
 - [MicroPython](https://docs.micropython.org/) - 适用于微控制器和受限系统的精益且高效的 Python 实现
 - [PikaPython](https://github.com/pikastech/pikapython) - Python仅用4KB RAM运行，零依赖，易于与C绑定。
 - [PharoThings](https://github.com/pharo-iot/PharoThings) - 基于 [Pharo](https://pharo.org/) 的物联网项目实时编程平台（一种纯粹的面向对象编程语言和强大的环境，专注于简单性和即时反馈）。
 - [Rust](https://www.rust-lang.org/) - Rust 是一种专注于性能、可靠性和生产力的语言。它以其安全性而闻名，它是内存安全的，它使用借用检查器，并且并发性也是安全的。
 - [TinyGo](https://tinygo.org/) - TinyGo 是一个通过创建基于 LLVM 的新编译器将 Go 编程语言引入微控制器和现代 Web 浏览器的项目。您可以在许多不同的微控制器板上编译和运行 TinyGo 程序，例如 BBC micro:bit 和 Arduino Uno。
 - [Toitlang](https://toitlang.org/) - 是一种高级语言，其语法非常接近 Python。由于它是根据微控制器的第一原理构建的，因此它的速度至少比 MicroPython 快 20 倍。他们还构建了一个灵活的 IDE 集成。

#### 框架

 - [AllJoyn](https://openconnectivity.org/developer/reference-implementation/alljoyn) - AllJoyn 是一个开源软件框架，使设备和应用程序可以轻松地相互发现和通信。
 - [Apple HomeKit](https://developer.apple.com/homekit/) - HomeKit 是一个用于与用户家中连接的配件进行通信和控制的框架。
 - [homebridge-blink-security](https://github.com/BitWise-0x/homebridge-blink-security) - 一个 Homebridge 插件，用于将 Blink 摄像头、门铃和警报器与 Apple HomeKit 集成，具有实时流媒体、布防/撤防和运动检测功能。
 - [homebridge-smartrent](https://github.com/BitWise-0x/homebridge-smartrent) - 一个 Homebridge 插件，用于通过实时 WebSocket 连接将 SmartRent 锁、恒温器、泄漏传感器和开关与 Apple HomeKit 集成。
 - [AREG SDK](https://github.com/aregtech/areg-sdk) - AREG SDK 是一个以接口为中心的实时异步通信引擎，可实现分布式计算和 [mist-](https://csrc.nist.gov/publications/detail/sp/500-325/final)计算，其中连接的事物进行交互并提供服务，就好像它们像瘦分布式服务器一样运行。
 - [Astarte](https://github.com/astarte-platform/astarte) - Astarte 是一个用 Elixir 编写的开源物联网平台。它是一个交钥匙解决方案，包含将设备群连接到一组远程应用程序所需的一切。它执行数据建模、自动数据缩减、实时事件，并为您提供现代物联网平台中可能期望的任何功能。目前，使用提供的 SDK 即可开箱即用地支持 Linux 和 ESP32 设备。
 - [Blynk](http://www.blynk.cc) - Blynk 是一个为互联事物创建 iOS 和 Android 应用程序的平台。您只需拖放小部件（直接在智能手机上）即可轻松为所有项目构建图形界面。支持以太网、WiFi、蓝牙、GSM/GPRS、USB/串行连接，与 Arduino、Raspberry、ARM mbed、Particle、RedBear 等各种原型平台连接。
 - [Countly IoT Analytics](http://github.com/countly/countly-server) - Countly 是一个适用于移动和物联网设备的通用分析平台，以开源形式提供。
 - [Eclipse Ditto™](https://eclipse.org/ditto/) - Eclipse Ditto 是一个用于构建所谓“数字孪生”的框架。它提供基于云的表示和 API 来与连接的物理设备进行交互。 Ditto 提供内置授权、搜索和连接功能，可与 MQTT 代理、HTTP 端点和 Apache Kafka 等外部系统集成。
 - [Eclipse Smarthome](https://eclipse.org/smarthome/) - Eclipse SmartHome 框架设计为在嵌入式设备上运行，例如 Raspberry Pi、BeagleBone Black 或 Intel Edison。它需要符合 Java 7 的 JVM 和 OSGi (4.2+) 框架，例如 Eclipse Equinox。
 - [Freedomotic](http://www.freedomotic.com) - Freedomotic 是一个开源、灵活、安全的物联网 (IoT) 开发框架，可用于构建和管理现代智能空间。它针对个人（家庭自动化）以及商业用户（智能零售环境、环境感知营销、监控和分析等）。它用 Java 编写，可以与众所周知的标准楼宇自动化协议以及“自己动手”解决方案进行交互。
 - [Iotivity](https://iotivity.org/) - IoTivity 是一个开源软件框架，可实现设备到设备的无缝连接，以满足物联网的新兴需求。
 - [Iotellect](https://iotellect.com) - 用于设备集成、数据收集和实时可视化的低代码物联网平台。通过拖放式 UI 构建器支持 MQTT、OPC UA、Modbus 和 50 多个工业协议。
 - [Jumpstarter](https://github.com/jumpstarter-dev/jumpstarter) - 开源硬件在环测试框架，用于通过 CI/CD 集成对真实和虚拟 IoT 硬件进行自动化测试。
 - [Kura](https://eclipse.org/kura/) - Kura 旨在为服务网关中运行的 M2M 应用程序提供基于 Java/OSGi 的容器。 Kura 提供或在可用时聚合 M2M 应用程序所需的最常见服务的开源实现。
 - [Lelylan](http://www.lelylan.com/) - Lelylan是一个基于轻量级微服务架构的物联网云平台。 Lelylan 平台与硬件和平台无关。这意味着您可以连接任何硬件，从 ESP8266 到最专业的嵌入式硬件解决方案以及介于两者之间的所有硬件 - 并且它可以在任何公共云、您自己的私有数据中心，甚至在混合环境中运行，无论是虚拟化还是裸机。
 - [Macchina.io](https://github.com/macchina-io/macchina.io) - macchina.io EDGE 是一个丰富的软件框架，用于快速构建在基于 Linux 的设备上运行的 IoT 设备应用程序。 macchina.io EDGE 实现了一个基于网络的、安全的、模块化的、可扩展的 JavaScript 和 C++ 运行时环境，并提供了即用型且经过行业验证的软件构建块。这些使设备能够与各种传感器、其他设备和云服务进行通信，并在本地、边缘设备或本地网络内处理、分析和过滤传感器数据。
 - [Mihini](https://wiki.eclipse.org/Mihini) - Mihini 的主要目标是提供在 Linux 之上运行的嵌入式运行时，该运行时公开用于构建 M2M 应用程序的高级 API。 Mihini 旨在通过促进对 M2M 系统 I/O 的访问、提供通信层等来实现轻松、可移植的开发。
 - [OpenHAB](http://www.openhab.org/) - openHAB 运行时是部署在 OSGi 框架 (Equinox) 上的一组 OSGi 捆绑包。因此，它是一个纯 Java 解决方案，需要 JVM 才能运行。基于 OSGi，它提供了高度模块化的架构，甚至允许在运行时添加和删除功能而无需停止服务。
 - [Gobot](http://gobot.io/) - Gobot 是一个用于机器人、物理计算和物联网的框架，用 Go 编程语言编写。
 - [Home Assistant](https://github.com/home-assistant/home-assistant) - Home Assistant 是一个运行在 Python 3 上的家庭自动化平台。Home Assistant 的目标是能够跟踪和控制家里的所有设备，并提供一个自动化控制的平台。
 - [Lightweight MQTT Machine Network](http://lwmqn.github.io/) - LWMQN 是一个开源项目，遵循 OMA LWM2M v1.0 规范的一部分，并使用基于 IP 的智能对象模型来满足机器网络管理的最低要求。它提供服务器端和机器端库，使使用 JavaScript 和 Node.js 进行全栈 IoT 开发成为可能。另请参阅：IPSO 联盟 [技术档案](http://www.ipso-alliance.org/ipso-community/resources/technical-archive/)。
 - [Thingsboard IoT Gateway](https://github.com/thingsboard/thingsboard-gateway) - 开源物联网网关 - 使用 OPC-UA 和 MQTT 协议将连接到旧系统和第三方系统的设备与 Thingsboard 物联网平台集成。
 - [Pimatic](https://pimatic.org/) - Pimatic 是一个在 Node.js 上运行的家庭自动化框架。它为家庭控制和自动化任务提供了一个通用的可扩展平台。
 - [IOTA](https://iota.org/) - 用于物联网的开源分布式账本协议。使用有向无环图（DAG）而不是区块链。
 - [MyController](https://github.com/mycontroller-org/mycontroller) - 开源控制器。 MyController.org 是一个适用于家庭、办公室或任何地方的物联网自动化控制器。
 - [Mozilla WebThings](https://iot.mozilla.org/) - 用于通过网络监视和控制设备的开放平台。
 - [HStreamDB](https://github.com/hstreamdb/hstream) - 专为物联网数据存储和实时处理而构建的流数据库。
 - [IoTSharp.Gateways](https://github.com/IoTSharp/Gateways) - 开源物联网网关 - 使用 ModBus、OPC-UA、BACNet 和 MQTT 协议将连接到传统系统和第三方系统的设备与 IoTSharp 物联网平台集成。
 - [ForestHub](https://foresthub.ai) - 边缘人工智能代理平台。其开源运行时 [edge-agents](https://github.com/ForestHubAI/edge-agents) 在 Linux 边缘网关（Raspberry Pi、Jetson）上离线运行 AI 代理，其中本地 SLM 与云 LLM、GPIO/UART/MQTT 作为一流节点以及可视化构建器。

#### 中间件

 - [Corlysis](https://corlysis.com/) - Corlysis 是一个帮助您存储和可视化时间序列数据的平台。它基于 SpaceX 也使用的开源项目 Grafana 和 InfluxDB。
 - [IFTTT](https://ifttt.com/) - IFTTT 是一项基于 Web 的服务，允许用户创建称为“食谱”的简单条件语句链，这些条件语句是根据 Gmail、Facebook、Instagram 和 Pinterest 等其他 Web 服务的更改而触发的。 IFTTT 是“If This then That”的缩写（发音类似于“gift”，但没有“g”）。
 - [OPC Router](https://www.opc-router.com/opc-router-details/) - 具有各种插件的物联网网关（OPC UA、Mqtt、SQL、REST、SAP、InfluxDB、打印机...）
 - [Huginn](https://github.com/cantino/huginn) - Huginn 是一个用于构建代理的系统，可以为您在线执行自动化任务。
 - [Kaa](http://www.kaaproject.org/) - 用于快速创建物联网解决方案的开源中间件平台。
 - [Losant](https://losant.com) - Losant 是一个易于使用且功能强大的开发者平台，旨在帮助您快速、安全地构建复杂的互联解决方案。 Losant 使用 REST 和 MQTT 等开放通信标准来提供从一台到数百万台设备的连接。 Losant 提供强大的数据收集、聚合和可视化功能，帮助理解和量化大量传感器数据。 Losant 的拖放工作流程编辑器允许您触发操作、通知和机器对机器通信，而无需编程。
 - [MicroServiceBus.com](https://microservicebus.com) - MicroServiceBus.com 是一个适用于 Azure、AWS 和 IBM IoT Hub 的设备管理平台，集成了 GitHub、ServiceNow、Cisco Jasper 等。它有免费（有限）版本以及企业产品。
 - [DreamFactory](http://www.dreamfactory.com) - DreamFactory 是一个免费的开源 REST API 平台，适用于移动、Web 和 IoT 应用程序。
 - [HiveMQ](https://www.hivemq.com/) - 企业级 MQTT 代理，可扩展以连接数百万个 IoT 设备。
 - [I1820](https://i1820.github.io/) - I1820是一个免费的开源平台，提供基于MQTT的发现、数据收集和配置服务。 I1820 实现了一个 REST API 来控制事物，并将所有收集到的数据存储在名为 InfluxDB 的时间序列数据库中。
 - [IOStash](https://iostash.io) - IOSTash 是一个高性能物联网平台，免费供 DIY 开发人员和非营利应用程序使用。它具有多种连接选项，可轻松开发 M2M 或 M2A 应用程序。 IOSTash 提供 Nodejs 和 Android 库，以便轻松创建应用程序。
 - [Thingsboard](https://thingsboard.io) - 一个开源物联网平台。适用于您的 IoT 解决方案的设备管理、数据收集、处理和可视化。
 - [Thingspeak](https://thingspeak.com/) - 开源 IoT 分析平台服务，可让您在云中聚合、可视化和分析实时数据流。您可以从设备将数据发送到 ThingSpeak、创建实时数据的即时可视化并发送警报。
 - [VerneMQ](https://github.com/erlio/vernemq) - VerneMQ 是一种高性能、分布式 MQTT 代理，可连接 IoT、M2M、移动和 Web 应用程序。它可以在商用硬件上水平和垂直扩展，以支持大量并发发布者和消费者，同时保持低延迟和容错能力。
 - [Kuzzle](https://github.com/kuzzleio/kuzzle) - 开源后端，具有实时发布/订阅或地理围栏等高级功能，以及支持 MQTT、LoRaWAN 等的多协议接口。 （[网站]（https://kuzzle.io/solutions/technologies/iot-backend/））
 - [DevicePilot](https://www.devicepilot.com) - 连接设备的运营分析（包括永久免费层）。
 - [EMQX](https://www.emqx.io/) - 超可扩展的开源 MQTT 代理。在一个集群中连接超过 1 亿个物联网设备，以 1M 消息/秒吞吐量和 1 毫秒延迟移动和处理实时物联网数据。
 - [Waterstream](https://waterstream.io/) - MQTT 代理利用 Apache Kafka 作为自己的存储和分发引擎。
 - [NanoMQ](https://github.com/nanomq/nanomq) - 适用于 IoT Edge 平台的轻量级且快速的 MQTT 代理。
 - [Kuiper](https://github.com/emqx/kuiper) - 由Golang实现的边缘轻量级物联网数据分析/流媒体软件，可以在各种资源受限的边缘设备上运行。
 - [t6](https://github.com/mathcoll/t6) - 数据优先的物联网平台，用于将物理对象与时序数据库连接并进行数据分析。
 - [IoTSharp](https://github.com/IoTSharp/IoTSharp) - IoTSharp 是一个用于数据收集、处理、可视化和设备管理的开源物联网平台。
 - [Husarnet](https://husarnet.com/) - Husarnet 是一个全球点对点网络层，可以通过互联网直接进行 MCU-Server 或 MCU-MCU 连接，无需桥接。
 - [Zilla](https://github.com/aklivity/zilla) - 多协议事件原生边缘/服务代理，支持 HTTP、SSE、gRPC、MQTT 和原生 Kafka 协议等标准协议。

#### 库和工具

 - [aem-modbus-simulator](https://github.com/leaberg69/aem-modbus-simulator) - 开源 Python Modbus RTU/TCP 从站模拟器，模拟 LRI AEM-60DC8 工业直流监视器。镜像 147 个保持寄存器、8 个 DC 通道、6 个波特率 (4,800-115,200)。适用于无需物理硬件的 SCADA/PLC 集成测试。
 - [ble-scale-sync](https://github.com/KristianP26/ble-scale-sync) - 跨平台 Node.js CLI，可读取 BLE 智能秤（23 个品牌）、计算身体成分并导出到 Garmin Connect、MQTT、InfluxDB、Webhook 和 Ntfy。可在 Raspberry Pi、Linux、macOS 和 Windows 上运行。
 - [Cylon.js](http://cylonjs.com/) - Cylon.js 是一个用于机器人、物理计算和物联网的 JavaScript 框架。它使得命令机器人和设备变得异常容易。
 - [Luvit](https://luvit.io/) - Luvit 实现了与 Node.js 相同的 API，但是是在 Lua 中！虽然该框架不直接参与 IoT 开发，但它仍然是快速构建功能强大且内存高效的嵌入式 Web 应用程序的“绝佳”方法。
 - [Johnny-Five](http://johnny-five.io/) - Johnny-Five 是最初的 JavaScript 机器人编程框架。 Johnny-Five 由 Bocoup 于 2012 年发布，由充满热情的软件开发人员和硬件工程师社区维护。
 - [Pi4J](http://pi4j.com/) - Pi4j 旨在为 Java 程序员提供友好的面向对象 I/O API 和实现库，以访问 Raspberry Pi 平台的完整 I/O 功能。
 - [WiringPi](http://wiringpi.com/) - WiringPi 是一个用 C 语言编写的 GPIO 访问库，适用于 Raspberry Pi 中使用的 BCM2835。
 - [Node-RED](http://nodered.org/) - 用于连接物联网的可视化工具。
 - [MIMIC IoT Simulator](https://www.gambitcomm.com/site/iot_simulator.php) - 模拟大型 IoT 环境，以实现基于 MQTT、CoAP、REST 的 IoT 应用程序的敏捷开发/测试/概念验证/培训
 - [MQTT Explorer](https://thomasnordquist.github.io/MQTT-Explorer/) - 用于在主题层次结构中可视化 MQTT 主题的工具，就像一把 MQTT 瑞士军刀。
 - [MQTT X](https://mqttx.app/) - MQTT X 是 EMQ 开源的跨平台 MQTT 5.0 客户端工具，支持 macOS、Linux 和 Windows。
 - [ops](https://ops.city/) - 一个免费的开源工具，用于将 Linux 应用程序构建、运行和部署为 unikernel。
 - [SmartObject](https://github.com/PeterEB/smartobject) - 智能对象类，可帮助您在 JavaScript 应用程序中创建 IPSO 智能对象。另请参阅：IPSO 联盟 [技术档案](http://www.ipso-alliance.org/ipso-community/resources/technical-archive/)。
 - [United Manufacturing Hub](https://github.com/united-manufacturing-hub/united-manufacturing-hub) - 开源制造应用平台（结合了各种开源解决方案并将它们封装在 Helm 图表中，例如 Nodered、VerneMQ 和 timescaleDB）
 - [QuestDB](https://github.com/questdb/questdb) - 用于实时分析和高性能应用程序的开源时间序列数据库。支持通过 InfluxDB 线路协议和 SQL 作为查询语言进行高吞吐量摄取。
 - [Chaos Genius](https://github.com/chaos-genius/chaos_genius) - 一个开源 ML 支持的分析引擎，用于异常值/异常检测和根本原因分析。连接传感器数据，监控异常行为并发出警报。
 - [Explore IoT Libraries](https://kandi.openweaver.com/explore/internet-of-things) - 发现并查找 kandi 上流行和新图书馆、顶级作者、热门项目工具包、讨论、教程和学习资源的精选列表。
 - [ThingsOn MQTT Bench](https://github.com/volkanalkilic/ThingsOn.MQTT.Bench) - ThingsOn MQTT Bench 是一款适用于 MQTT 代理的简单跨平台 .NET Core 基准测试工具。它测量在指定时间内可以发送到代理的最大消息数。


#### 杂项

 - [Amazon Dash](https://fresh.amazon.com/dash/) - Amazon Dash Button 是一款连接 Wi-Fi 的设备，只需按一下按钮即可重新订购您喜爱的商品。
 - [BirdNET-Go](https://github.com/tphakala/birdnet-go) - 具有多模型 AI 推理功能的实时野生动物声景分析器、具有 Home Assistant 发现功能的 MQTT 发布以及 Web 仪表板。
 - [Electrum](https://github.com/yoelf22/electrum) - 一个结构化的人工智能辅助工具包，用于定义内置软件的硬件产品——从概念到工程规范再到可演示的材料，分八个阶段。
 - [Freeboard](http://freeboard.io/) - 实时交互式仪表板和可视化创建器，实现直观的拖放界面。
 - [Nebula](http://nebula.readthedocs.io) - 旨在管理物联网设备的 Docker 编排器。
 - [Gladys](https://gladysassistant.com) - Gladys 是一个开源程序，运行在 Raspberry Pi 上并集成到整个家庭网络系统中。
 - [authBroker](https://github.com/authbroker/authbroker) - Keycloak HTTP/MQTT/CoAP IoT 代理适配器，例如 Aedes。
 - [MQTT File Uploader](https://github.com/volkanalkilic/Mqtt-File-Uploader) - MQTT 文件上传器是一个简单的跨平台 .NET Core 应用程序，它监视本地目录的更改并将新的或修改的文件上传到 MQTT 代理。
 - [PiSpot-Show](https://github.com/GeiserX/PiSpot-Show) - 具有天气集成和 PiJuice 电池管理功能的 Raspberry Pi WiFi 优惠券显示系统。
- [SIGNL4 – Mobile Alerting](https://www.signl4.com/iot-service-alerting/) - SIGNL4 为您的物联网项目提供可靠的移动警报，包括应用程序推送、短信和语音通话，以及升级和值班安排。

## 协议和网络

### 物理层

#### <img width="50" src="http://www.ieee802.org/15/pub/ieee802-15%20logo.jpg" /> - 802.15.4 (IEEE)

IEEE 802.15.4 是一项标准，指定低速率无线个域网 (LR-WPAN) 的物理层和媒体访问控制。它由 IEEE 802.15 工作组维护，并于 2003 年对其进行了定义。它是 ZigBee、ISA100.11a、WirelessHART 和 MiWi 规范的基础，每个规范都通过开发 IEEE 802.15.4 中未定义的上层来进一步扩展该标准。或者，它可以与 6LoWPAN 和标准互联网协议一起使用来构建无线嵌入式互联网。 - [维基百科](https://en.wikipedia.org/wiki/IEEE_802.15.4)

> IEEE 标准 802.15.4 旨在提供一种无线个域网 (WPAN) 的基本较低网络层，重点关注设备之间低成本、低速的无处不在的通信。它可以与 Wi-Fi 等其他方法形成对比，后者提供更多带宽，但需要更多电量。重点是附近设备之间的通信成本非常低，几乎没有底层基础设施，旨在利用这一点来进一步降低功耗。

#### <img width="50" src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/fc/BluetoothLogo.svg/770px-BluetoothLogo.svg.png" /> - 蓝牙（蓝牙特殊兴趣组）

蓝牙是一种无线技术标准，用于从固定和移动设备短距离交换数据（使用 2.4 至 2.485 GHz ISM 频段的短波长 UHF 无线电波）以及构建个域网 (PAN)。它由电信供应商爱立信于 1994 年发明，最初被设想为 RS-232 数据线的无线替代品。它可以连接多个设备，克服同步问题。 - [维基百科](https://en.wikipedia.org/wiki/Bluetooth)

> 蓝牙由蓝牙特别兴趣组 (SIG) 管理，该组织在电信、计算、网络和消费电子领域拥有超过 25,000 家成员公司。

#### <img width="50" src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/20/Bluetooth_Smart_Logo.svg/241px-Bluetooth_Smart_Logo.svg.png" /> - 低功耗蓝牙（蓝牙特殊兴趣小组）

低功耗蓝牙（Bluetooth LE、BLE，以“Bluetooth Smart”销售）是一种无线个人区域网络技术，由蓝牙特别兴趣小组设计和销售，旨在医疗保健、健身、信标、安全和家庭娱乐行业中的新颖应用。 - [维基百科](https://en.wikipedia.org/wiki/Bluetooth_low_energy)

> 与经典蓝牙相比，智能蓝牙旨在显着降低功耗和成本，同时保持相似的通信范围。蓝牙 SIG 预测，到 2018 年，超过 90% 的蓝牙智能手机将支持蓝牙智能。

#### EC-GSM-IoT（EC-GSM-IoT 组）

扩展覆盖 GSM IoT (EC-GSM-IoT) 是一种基于标准的低功耗广域技术。它基于 eGPRS，设计为高容量、远距离、低能耗和低复杂性的物联网通信蜂窝系统。

> EC-GSM-IOT 网络试验已经开始，计划于 2017 年首次商用。在所有主要移动设备、芯片组和模块制造商的支持下，EC-GSM-IoT 网络将与 2G、3G 和 4G 移动网络共存。它还将受益于所有安全和隐私移动网络功能，例如支持用户身份机密性、实体身份验证、机密性、数据完整性和移动设备识别。

#### <img width="50" src="https://intelilight.eu/wp-content/uploads/2017/02/technology_lorawan.png" /> - LoRaWAN（LoRa 联盟）

LoRaWAN 广域网允许与连接的对象进行低比特率通信，从而参与物联网、机器对机器 M2M 和智能城市。 - [维基百科](https://en.wikipedia.org/wiki/LoRaWAN)

> 该技术由 LoRa 联盟标准化。它最初由 Cycleo 开发，该公司于 2012 年被 Semtech 收购。LoRaWAN 是远程广域网的缩写。

#### 窄带物联网 (3GPP)

窄带物联网 (NB-IoT) 是一种低功耗广域网 (LPWAN) 无线电技术标准，旨在支持使用蜂窝电信频段连接各种设备和服务。 - [维基百科](https://en.wikipedia.org/wiki/NarrowBand_IOT)

> NB-IoT 是一种专为物联网 (IoT) 设计的窄带无线电技术，是第三代合作伙伴计划 (3GPP) 标准化的一系列移动物联网 (MIoT) 技术之一。

#### <img width="50" src="http://www.silvereco.fr/wp-content/uploads/2015/02/logo510f703a4647f1.jpg" /> - Sigfox (Sigfox)

Sigfox 是一家法国公司，致力于构建无线网络来连接电表、智能手表和洗衣机等低能耗物体，这些物体需要持续开启并发射少量数据。其基础设施旨在为所谓的物联网 (IoT) 做出贡献。 - [维基百科](https://en.wikipedia.org/wiki/Sigfox)

> SIGFOX 将自己描述为“第一家也是唯一一家为物联网提供全球蜂窝连接的公司”。其基础设施“完全独立于现有网络，例如电信网络”。 SIGFOX 致力于提供“部署数十亿个对象和数千种新用途”的方法，其长期目标是“拥有日常对象产生的 PB 级数据”。

#### <img width="50" src="https://upload.wikimedia.org/wikipedia/commons/f/f8/Wi-FI_Alliance_Logo.png" /> - Wi-Fi（Wi-Fi 联盟）

Wi-Fi（或WiFi）是一种允许电子设备联网的局域无线计算机网络技术，主要使用2.4吉赫兹（12厘米）UHF和5吉赫兹（6厘米）SHF ISM无线电频段。 - [维基百科](https://en.wikipedia.org/wiki/Wi-Fi)

> Wi-Fi 联盟将 Wi-Fi 定义为基于电气和电子工程师协会 (IEEE) 802.11 标准的任何“无线局域网”(WLAN) 产品。[1]然而，术语“Wi-Fi”在一般英语中用作“WLAN”的同义词，因为大多数现代 WLAN 都基于这些标准。 “Wi-Fi”是 Wi-Fi 联盟的商标。 “Wi-Fi Certified”商标只能由成功完成Wi-Fi联盟互操作性认证测试的Wi-Fi产品使用。

### 网络/传输层

#### <img width="50" src="http://www.tonex.com/wp-content/uploads/6lowpan.jpg" /> - 6LowPan (IETF)

6LoWPAN 是低功耗无线个人区域网络 IPv6 的缩写。 6LoWPAN 是 IETF 互联网领域一个已结束的工作组的名称。 - [维基百科](https://en.wikipedia.org/wiki/6LoWPAN)

> 6LoWPAN 概念源于“互联网协议甚至可以而且应该应用于最小的设备”的想法，并且处理能力有限的低功耗设备应该能够参与物联网。
6LoWPAN 小组定义了封装和标头压缩机制，允许通过基于 IEEE 802.15.4 的网络发送和接收 IPv6 数据包。 IPv4 和 IPv6 是局域网、城域网和互联网等广域网数据传输的主力。同样，IEEE 802.15.4 设备提供无线域中的传感通信能力。然而，这两个网络的固有性质是不同的。

#### <img width="50" src="https://www.threadgroup.org/portals/0/images/contact/img1.svg" /> - 线程（线程组）

Thread 是一种基于 IPv6 的协议，用于“智能”家用设备在网络上进行通信。

> 2014 年 7 月，谷歌公司的 Nest Labs 宣布与三星、ARM Holdings、飞思卡尔、Silicon Labs、Big Ass Fans 和锁具公司耶鲁等公司成立工作组，试图通过为产品提供 Thread 认证，使 Thread 成为行业标准。目前使用的其他协议包括 ZigBee 和蓝牙智能。
Thread 使用 6LoWPAN，而 6LoWPAN 又使用 IEEE 802.15.4 无线协议进行网状通信，ZigBee 和其他系统也是如此。然而，Thread 是可 IP 寻址的，具有云访问和 AES 加密功能。它支持网络上超过 250 个设备。

#### <img width="50" src="https://zigbeealliance.org/wp-content/uploads/2019/11/zb_logo-b_color_rgb_icon-e1573775155251.png" /> - ZigBee（ZigBee 联盟）

ZigBee 是基于 IEEE 802.15.4 的规范，适用于一套高级通信协议，用于创建具有小型、低功耗数字无线电的个人区域网络。 - [维基百科](https://en.wikipedia.org/wiki/ZigBee)

> ZigBee 规范定义的技术旨在比其他无线个域网 (WPAN)（例如蓝牙或 Wi-Fi）更简单、更便宜。应用包括无线灯开关、带家用显示器的电表、交通管理系统以及其他需要短距离低速率无线数据传输的消费和工业设备。

#### <img width="50" src="https://upload.wikimedia.org/wikipedia/commons/0/08/Z-Wave_logo.jpg" /> - Z-Wave（Z-Wave 联盟）

Z-Wave 是一种无线通信规范，旨在允许家庭中的设备（例如照明、访问控制、娱乐系统和家用电器）相互通信以实现家庭自动化。 - [维基百科](https://en.wikipedia.org/wiki/Z-Wave)

> Z-Wave 技术最大限度地降低功耗，因此适用于电池供电的设备。 Z-Wave 旨在以高达 100kbit/s 的数据速率提供小数据包的可靠、低延迟传输，这与主要为高数据速率设计的 Wi-Fi 和其他基于 IEEE 802.11 的无线 LAN 系统不同。 Z-Wave 工作在亚千兆赫兹频率范围，大约 900 MHz。

### 应用层

#### 合作协议 (IETF)

约束应用协议 (CoAP) 是一种软件协议，旨在用于非常简单的电子设备，允许它们通过互联网进行交互通信。 - [维基百科](https://en.wikipedia.org/wiki/Constrained_Application_Protocol)

> CoAP 特别针对需要通过标准互联网网络进行远程控制或监控的小型低功耗传感器、开关、阀门和类似组件。 CoAP 是一种应用层协议，旨在用于资源受限的互联网设备，例如 WSN 节点。

#### 数据传输层安全 (IETF)

数据报传输层安全 (DTLS) 通信协议为数据报协议提供通信安全。  - [维基百科](https://fr.wikipedia.org/wiki/Datagram_Transport_Layer_Security)

> DTLS 允许基于数据报的应用程序以[由谁设计？] 的方式进行通信，以防止窃听、篡改或消息伪造。 DTLS 协议基于面向流的传输层安全 (TLS) 协议，旨在提供类似的安全保证。

#### <img width="50" src="https://cdn.arstechnica.net/wp-content/uploads/2015/07/2015-07-13_16-46-26.jpg" /> - Eddystone）（Google）

Eddystone 是 Google 于 2015 年 7 月发布的信标技术配置文件。这款开源跨平台软件通过蓝牙低能耗信标格式为用户提供位置和接近数据。 - [维基百科](https://en.wikipedia.org/wiki/Eddystone_(Google))

> 虽然与 Apple 2013 年发布的 iBeacon 类似，Eddystone 可在 Android 和 iOS 上运行，而 iBeacon 仅限于 iOS 平台。这两款软件的实际应用是，企业主可以根据智能手机的实时位置来定位潜在客户。

#### <img width="50" src="http://www.httptechnology.com.au/logo.jpg" /> - HTTP (IETF)

超文本传输协议 (HTTP) 是分布式协作超媒体信息系统的应用协议。 HTTP 是万维网数据通信的基础。 - [维基百科](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol)

> HTTP 标准的开发由互联网工程任务组 (IETF) 和万维网联盟 (W3C) 协调，最终发布了一系列征求意见 (RFC)。 HTTP/1.1（常用的 HTTP 版本）的第一个定义出现在 1997 年的 RFC 2068 中，尽管它已被 1999 年的 RFC 2616 废弃。

#### <img width="50" src="https://developer.apple.com/ibeacon/images/ibeacon-logo.svg" /> - iBeacon（苹果）

iBeacon 是 Apple 标准化的协议，并于 2013 年在 Apple 全球开发者大会上推出。 - [维基百科](https://en.wikipedia.org/wiki/IBeacon)

> iBeacon 使用蓝牙低功耗接近感测来传输由兼容应用程序或操作系统拾取的通用唯一标识符。该标识符可用于确定设备的物理位置、跟踪客户或触发设备上基于位置的操作，例如在社交媒体上签到或推送通知。

#### <img width="50" src="https://raw.githubusercontent.com/mqtt/mqttorg-graphics/master/mqtticon-large.png" /> - MQTT (IBM)

MQTT（以前称为 MQ Telemetry Transport）是一种基于发布-订阅的“轻量级”消息传递协议，在 TCP/IP 协议之上使用。它专为与需要“小代码占用空间”或网络带宽有限的远程位置的连接而设计。 - [维基百科](https://en.wikipedia.org/wiki/MQTT)

> 发布-订阅消息传递模式需要消息代理。代理负责根据消息主题将消息分发给感兴趣的客户端。 Cirrus Link Solutions 的 Andy Stanford-Clark 和 Arlen Nipper 于 1999 年编写了该协议的第一个版本。

#### <img width="50" src="https://www.pjon.org/assets/images/PJON-logo-devices.jpg" /> - PJON

PJON®（填充抖动操作网络）是一种 Arduino 兼容、多主控、多媒体网络协议。它提出了一个标准，它被设计为一个框架，并实现了一个完全软件模拟的网络协议栈，可以在许多架构上轻松交叉编译，如 ATtiny、ATmega、ESP8266、ESP32、STM32、Teensy、Raspberry Pi、Linux、Windows x86 和 Apple 机器。它是快速、全面地构建设备网络的有效工具。访问 wiki 和文档以了解有关 PJON 标准的更多信息。

> PJON 被用于数千种设备，其社区已遍布全球，因为以下 6 个关键因素：新技术、多媒体支持、增强的安全性、增强的可靠性、高灵活性和低成本。

#### <img width="50" src="https://stomp.github.io/images/project-logo.png" /> - STOMP

简单（或流）文本导向消息协议 (STOMP)，以前称为 TTMP，是一种基于简单文本的协议，设计用于与面向消息的中间件 (MOM) 配合使用。 - [维基百科](https://en.wikipedia.org/wiki/Streaming_Text_Oriented_Messaging_Protocol)

> STOMP 提供可互操作的有线格式，允许 STOMP 客户端与支持该协议的任何消息代理进行通信。因此，它与语言无关，这意味着为一种编程语言或平台开发的经纪人可以接收来自用另一种语言开发的客户端软件的通信。

#### <img width="50" src="https://www.rabbitmq.com/wp-uploads/2012/02/HTML5_Logo_256.png" /> - Websocket

WebSocket 是一种通过单个 TCP 连接提供全双工通信通道的协议。 - [维基百科](https://en.wikipedia.org/wiki/WebSocket)

> WebSocket 设计为在 Web 浏览器和 Web 服务器中实现，但它可以由任何客户端或服务器应用程序使用。 WebSocket 协议是一个独立的基于 TCP 的协议。 WebSocket 协议使浏览器和网站之间的更多交互成为可能，从而促进实时内容和实时游戏的创建。这是通过为服务器提供一种标准化方式来将内容发送到浏览器而无需客户端请求，并允许在保持连接打开的同时来回传递消息来实现的。

#### <img width="50" src="https://upload.wikimedia.org/wikipedia/commons/9/95/XMPP_logo.svg" /> - XMPP (IETF)

可扩展消息传递和状态协议（XMPP）是一种基于 XML（可扩展标记语言）的面向消息的中间件的通信协议。 - [维基百科](https://en.wikipedia.org/wiki/XMPP)

> 它支持在任何两个或多个网络实体之间近乎实时地交换结构化但可扩展的数据。该协议设计可扩展，还可用于发布-订阅系统、VoIP 信令、视频、文件传输、游戏、智能电网等物联网 (IoT) 应用以及社交网络服务。

## 技术

> 本节重新整理了与物联网世界密切相关的出色技术的精选列表。

### <img width="50" src="http://vectorlogofree.com/wp-content/uploads/2012/12/nfc-logo-vector-400x400.png" /> - NFC

近场通信 (NFC) 是一组协议，使电子设备能够通过将设备接触在一起或将它们靠近到通常 10 厘米或更小的距离来相互建立无线电通信。 - [维基百科](https://en.wikipedia.org/wiki/Near_field_communication)

### <img width="50" src="https://opcfoundation.org/wp-content/themes/opc/images/logo.jpg"/>- OPCUA
OPC-UA不仅是一种工业自动化协议，也是一种允许工业环境语义描述和对象建模的技术。
[维基百科](https://en.wikipedia.org/wiki/OPC_Unified_Architecture)


## 标准和联盟

### 标准

- [ETSI M2M](http://www.etsi.org/technologies-clusters/technologies/m2m) - ETSI 技术委员会正在制定机器对机器通信的标准。
- [OneM2M](http://www.onem2m.org/) - oneM2M 的目的和目标是开发技术规范，以满足对通用 M2M 服务层的需求，该服务层可以轻松嵌入到各种硬件和软件中，并依靠该规范将现场的无数设备与全球的 M2M 应用服务器连接起来。
- [OPCUA](https://opcfoundation.org/) - OPC 统一架构 (OPC UA) 是 OPC 基金会开发的用于互操作性的工业 M2M 通信协议。
- [OCF](https://openconnectivity.org/) - OCF（开放连接基金会）基于约束应用协议 (CoAP) 为涉及物联网 (IoT) 的设备制定标准和认证。
- [W3C WoT](https://www.w3.org/WoT/) - W3C 物联网工作组 (WoT) 致力于通过使用和扩展现有的标准化 Web 技术来应对 IoT 的碎片化问题。通过提供标准化元数据和其他可重复使用的技术构建块，W3C WoT 可以轻松实现跨 IoT 平台和应用程序域的集成。

### 联盟

- [AIOTI](http://www.meet-iot.eu/Alliance-for-Internet-of-Things-Innovation-AIOTI.html) - 物联网创新 (AIOTI) 旨在加强不同物联网参与者（工业、中小企业、初创企业）和部门之间的联系并建立新的关系。
- [Bluetooth Special Interest Group](https://www.bluetooth.com/) - 蓝牙特别兴趣小组 (SIG) 是监督蓝牙标准开发以及向制造商授予蓝牙技术和商标许可的机构。
- [IPSO Alliance](http://www.ipso-alliance.org/) - IPSO 联盟通过提高意识、提供教育、促进行业发展、开展研究以及更好地了解知识产权及其在物联网中的作用，为行业发展奠定了基础。
- [LoRa Alliance](https://www.lora-alliance.org/) - LoRa联盟是一个开放的、非盈利的会员协会，相信物联网时代已经来临。它由行业领导者发起，其使命是对世界各地部署的低功耗广域网 (LPWAN) 进行标准化，以实现物联网 (IoT)、机器对机器 (M2M)、智慧城市和工业应用。
- [OPC Foundation](https://opcfoundation.org/about/opc-foundation/mission-statement/) - OPC 基金会的使命是管理一个全球组织，在该组织中，用户、供应商和联盟合作创建数据传输标准，以实现工业自动化中的多供应商、多平台、安全可靠的互操作性。为了支持这一使命，OPC 基金会
创建和维护规范，通过认证测试确保符合 OPC 规范，并与行业领先的标准组织合作。
- [Thread Group](http://threadgroup.org/) - Thread Group 由来自 Nest、三星、ARM、飞思卡尔、Silicon Labs、Big Ass Fans 和耶鲁大学的成员组成，推动了 Thread 网络协议的开发。
- [Wi-Fi Alliance](https://www.wi-fi.org/) - Wi-Fi Alliance® 是一个由多家公司组成的全球网络，这些公司组成了一个全球非营利协会，其目标是通过新的无线网络技术（无论品牌如何）推动最佳用户体验。
- [Zigbee Alliance](http://www.zigbee.org/) - ZigBee 联盟是一个开放的非营利协会，拥有约 450 名成员，致力于推动创新、可靠且易于使用的 ZigBee 标准的开发。
- [Z-Wave Alliance](http://z-wavealliance.org/) - Z-Wave 联盟成立于 2005 年，由全球行业领导者组成，致力于开发和扩展 Z-Wave 作为“智能”家居和商业应用的关键支持技术。

## 资源

### 书籍

#### 滥用物联网：停电、异常和监视 (2015) *作者：Nitesh Dhanjani* [5.0]

> 未来有数十亿个相互连接的“事物”，其中包括巨大的安全问题。这本实用的书探讨了恶意攻击者如何滥用流行的基于物联网的设备，包括无线 LED 灯泡、电子门锁、婴儿监视器、智能电视和联网汽车。

#### 构建无线传感器网络：使用 ZigBee、XBee、Arduino 和处理 (2011) *作者：Robert Faludi* [4.5]

> 准备使用 ZigBee 无线网络协议和 Series 2 XBee 无线电创建分布式传感器系统和智能交互设备。当您完成本快节奏的实践指南的一半时，您将构建一系列有用的项目，包括提供遥感数据的完整 ZigBee 无线网络。

#### 数字孪生在行动 (2013) *作者：Greg Biegel* [4.0]

> 《数字孪生实践》是设计和构建有效数字孪生的实践指南。在其中，您将从头开始构建家庭规模的数字孪生。

#### 设计物联网 (2013) *Adrian McEwen 和 Hakim Cassimally* [4.0]

> 无论是物理计算、普适计算还是物联网，都是科技界的热门话题：如何引导内心的乔布斯，成功地将硬件、嵌入式软件、网络服务、电子产品和炫酷的设计结合起来，创造出有趣、互动、实用的尖端设备。如果您想创造下一个必备产品，这本独特的书是完美的起点。

#### 边缘计算技术与应用（2023）*作者：Perry Lea

> 资深技术专家 Perry Lea 撰写的这本严肃的指南剖析了流行语，揭示了边缘计算如何影响您的业务和 IT 决策，从硬件和软件系统到您与顾客、客户和员工互动的方式。

#### 低功耗蓝牙入门：低功耗网络工具和技术 (2014) *作者：Kevin Townsend、Carles Cufí、Akiba 和 Robert Davidson* [4.5]

> 本书对设备如何使用 Ble 相互通信提供了可靠、高级的概述。您将学习用于开发和测试支持 Ble 的移动应用程序和嵌入式固件的实用低成本工具，并获取使用各种开发平台的示例，包括适用于应用程序开发人员的 iO 和 Android 以及适用于产品设计师和硬件工程师的嵌入式平台。

#### IoT Inc：您的公司如何利用物联网赢得成果经济 (2017) *作者：Bruce Sinclair* [4.6]

> 这本重要指南深入探讨了物联网——它是如何工作的以及它如何改变业务；通过物联网视角看待自己的业务、客户和竞争对手的方法，以及深入探讨如何制定和实施强大的物联网战略。

#### 智能事物：普适计算用户体验设计 (2010) *作者：Mike Kuniavsky* [4.5]

> 智能事物提出了一种解决问题的方法来满足设计师的需求，并专注于流程而不是技术细节，以避免很快过时。它密切关注相关媒介的功能和局限性，并讨论商业环境中设计的权衡和挑战。

#### JavaScript on Things：Web 开发人员的硬件（2018 年 - 预计）*作者 Lyza Danger Gardner* [抢先体验书]

> JavaScript on Things 是您进入激动人心且充满娱乐性的小型电子产品编程世界的第一步。如果你了解足够的 JavaScript 来一起破解一个网站，你就会让东西发出哔哔声、闪烁声和旋转速度，速度比你说“nodebot”还要快。这本图文并茂的实践书籍向您展示了如何使用 Arduino、Tessel 和 Raspberry Pi 等平台。

### 文章

- [A Simple Explanation Of 'The Internet Of Things' (Forbes)](http://www.forbes.com/sites/jacobmorgan/2014/05/13/simple-explanation-internet-things-that-anyone-can-understand/) - 本文试图回答“物联网”到底是什么以及它会对我们产生什么影响。
- [IoT security. Is there an app for that ?](http://embedded-computing.com/21517-iot-security-is-there-an-app-for-that/) - 物联网世界会议研究物联网应用程序开发、安全性和商业模式。
- [The IoT Testing Atlas](http://iamqa.in/2015/10/04/The-IoT-Testing-Atlas/) - 一种用于在测试基于物联网的产品时管理参数排列的测试方法。
- [How to begin with the Amazon Timestream](https://itnext.io/how-to-begin-with-the-amazon-timestream-in-5-simple-steps-19c129040d9c/) - AWS Timestream 的分步指南 - 一个用于随时间收集 IoT 数据的时间序列数据库。

### 论文

- [A Reference Architecture for the Internet of Things](http://wso2.com/wso2_resources/wso2_whitepaper_a-reference-architecture-for-the-internet-of-things.pdf) - 本白皮书介绍了物联网 (IoT) 的参考架构：其中包括设备以及与设备交互和管理设备所需的服务器端和云架构。
- [Developing solutions for the Internet of Things](https://www-ssl.intel.com/content/dam/www/public/us/en/documents/white-papers/developing-solutions-for-iot.pdf) - 英特尔致力于为物联网 (IoT) 提供安全、无缝的解决方案。
- [Evaluation of indoor positioning based on Bluetooth Smart technology](http://publications.lib.chalmers.se/records/fulltext/199826/199826.pdf) - 计算机系统和网络项目的理学硕士论文。
- [IoT: A Vision, Architectural Elements, and Future Directions](http://arxiv.org/pdf/1207.0203.pdf) - 本文提出了在全球范围内实施物联网的以云为中心的愿景。讨论了在不久的将来可能推动物联网研究的关键支持技术和应用领域。
- [Realizing the Potential of the Internet of Things](https://www.tiaonline.org/wp-content/uploads/2018/05/Realizing_the_Potential_of_the_Internet_of_Things_-_Recommendations_to_Policymakers.pdf) - 电信行业协会 (TIA) 的一份白皮书，以向政策制定者提出的一系列有关利用和实现物联网市场潜力的建议的形式编写。
- [The Internet of Things: Evolution or Revolution ?](http://www.aig.com/Chartis/internet/US/en/AIG%20White%20Paper%20-%20IoT%20English%20DIGITAL_tcm3171-677828_tcm3171-698578.pdf) - 本白皮书将当前物联网市场的兴起与其他工业革命、其带来的挑战及其对我们日常生活的影响进行了比较。


## 执照

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](http://creativecommons.org/publicdomain/zero/1.0/)

在法律允许的范围内，[Halim Qarroum](https://github.com/HQarroum/) 已放弃本作品的所有版权以及相关或邻接权。
