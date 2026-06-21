# 很棒的ESP [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
很棒的 ESP8266/32 项目和代码的精选列表。

<a href="http://espressif.com/en/products/hardware/esp8266ex/overview"><img src="img/esp8266.jpg" alt="ESP8266" align="left" style="margin-right: 25px" height=150></a>
<a href="http://espressif.com/en/products/hardware/esp32/overview"><img src="https://pbs.twimg.com/profile_images/863510403120222208/rjVOiTe3.jpg" alt="ESP32" align="left" style="margin-right: 25px" height=150></a>
> [ESP8266](http://espressif.com/en/products/hardware/esp8266ex/overview) 和 [ESP32](http://espressif.com/en/products/hardware/esp32/overview) 都是低成本 Wi-Fi 微芯片，具有完整的 TCP/IP 堆栈和微控制器功能，由上海制造商 Espressif Systems 生产。
><br/>
> 有关如何为此列表做出贡献的信息，请参阅 [Contributing](contributing.md)。
><br/><br/>
---

## 内容
- [Firmware](#firmware)
- [Tools](#tools)
- [Projects](#projects)
  - [智能家居和物联网](#smart-home-and-iot)
  - [InfoSec](#infosec)
  - [Biomedical](#biomedical)
  - [LoRa](#lora)
  - [音乐和音频](#music-and-audio)
  - [Smartwatches](#smartwatches)
  - [Others](#others)
- [Libraries](#libraries)

## 固件
- [Espressif AT](http://bbs.espressif.com/) - ESP8266 的默认普通固件。
- [NodeMCU](https://github.com/nodemcu/nodemcu-firmware) - 适用于 ESP8266 的基于 eLua 的固件。
- [ESPBasic](http://www.esp8266basic.com/) - 用于轻松无线编程的 BASIC 固件，适用于 8266。
- [MicroPython](https://github.com/micropython/micropython/) - 用于 ESP8266 和 32 的 Python3 实现。
- [ESP3D](https://github.com/luc-github/ESP3D) - 适用于 3D 打印机（ESP32 和 8266）的实验性固件。
- [Frankenstein](https://github.com/nekromant/esp8266-frankenstein) - ESP8266 的一个快速而肮脏的固件，具有很酷的功能。
- [MongooseOS](https://github.com/cesanta/mongoose-os) - 物联网专用固件，包含 C 和 JS。适用于 ESP32/8266。
- [DeviceHive](https://devicehive.com/) - 作为 DeviceHive 物联网数据平台客户端的固件，仅适用于 8266。
- [RT-Thread](https://github.com/RT-Thread/rt-thread) - 适用于 ESP32 的中文开源固件。
- [Sming Framework](https://github.com/SmingHub/Sming) - 出色的 C/C++ IoT 框架，支持 ESP8266 和 ESP32。

## 工具
- [ESP Flash Tool](http://espressif.com/en/support/download/other-tools) - 适用于两个 ESP 的普通固件刷新程序。
- [Arduino Core/8266](https://github.com/esp8266/arduino) - ESP8266 的 Arduino 核心。
- [Arduino Core/32](https://github.com/espressif/arduino-esp32) - ESP32 的另一个 Arduino 核心。
- [ESPTool](https://github.com/espressif/esptool) - Espressif 的命令行工具，用于在两个 ESP 中进行引导加载程序通信。
- [ESP-Open-SDK](https://github.com/pfalcon/esp-open-sdk) - 适用于 ESP8266 的开放 SDK。
- [ESPTool-ck](https://github.com/igrr/esptool-ck) - 用于烧录 ESP8266 的 CLI 工具。
- [ESPTool-gui](https://github.com/Rodmg/esptool-gui) - 一款基于 ESPTool-ck 的刷机 GUI 工具。
- [LuaNode](https://github.com/Nicholas3388/LuaNode) - 适用于 32/8266 的仅 lua SDK。
- [Tuya-Convert](https://github.com/ct-Open-Source/tuya-convert) - 预装涂鸦固件的 Wi-Fi 固件刷写器 ESP8266。
- [NodeMCU Flasher](https://github.com/nodemcu/nodemcu-flasher) - NodeMCU 操作系统的官方刷写工具。
- [Tasmotizer](https://github.com/tasmota/tasmotizer) - Tasmota 固件的图形刷新工具。可以管理 Wi-Fi 和 MQTT 设置、模块和模板。
- [Arduino FS Plugin](https://github.com/esp8266/arduino-esp8266fs-plugin) - 用于 8266 中文件系统上传的 Arduino 插件。
- [PlatformIO](https://github.com/platformio/platformio-core) - 同时支持 ESP32 和 ESP8266 的跨平台 IDE 和调试器。

## 项目
### 智能家居和物联网
- [OpenMQTTGateway](https://github.com/1technophile/OpenMQTTGateway) - 用于 ESP 和其他设备的多协议 MQTT 网关的实现。
- [ESPHome](https://esphome.io/) - 一个功能齐全的系统，用于通过简单而强大的配置文件和家庭自动化系统来控制 ESP。
- [Tasmota](https://tasmota.github.io/docs/) - Sonoff 和其他 ESP8266/ESP32 设备的替代固件。包括大量传感器驱动程序，并以本机或通过 MQTT 与 [Home Assistant](https://www.home-assistant.io/) 集成。
- [ESPEasy](https://github.com/letscontrolit/ESPEasy) - 轻松将 ESP 模块转变为家庭自动化系统的多功能传感器设备。
- [Sonoff-Homekit](https://github.com/Gruppio/Sonoff-Homekit) - Sonoff 设备（和其他 8266 设备）的替代固件，允许通过 Apple 的 Homekit 进行控制。
- [DoorsignEPD](https://github.com/jamct/DoorsignEPD) - 使用 ESP32 的带有电子纸显示屏的智能门牌。
- [EPaperWeatherDisplay](https://github.com/henri98/esp32-e-paper-weatherdisplay) - 使用 ESP32 的非常可爱的电子墨水天气显示器。
- [HomePoint](https://github.com/sieren/Homepoint) - 从 ESP32 供电的屏幕控制 MQTT/HomeKit 智能家居设备。
- [openHASP](https://www.openhasp.com/) - 通过 MQTT 连接的可定制触摸屏 UI 控制您的家庭自动化设备。
- [SuperGreenOS](https://github.com/supergreenlab/SuperGreenOS) - 适用于 ESP32 的全功能家庭农业自动化软件。
- [CanAirIO](https://github.com/kike-canaries/canairio_firmware#canairio-firmware) - 公民科学项目，使用移动和固定站通过 ESP32 和智能手机测量空气质量。

### 信息安全
- [ESP32-BLECollector](https://github.com/tobozo/ESP32-BLECollector) - 一款 Wardrive 设备，可显示 BLE 设备并从中收集数据，所有这些都在漂亮的屏幕界面中进行。
- [ESP32Marauder](https://github.com/justcallmekoko/ESP32Marauder) - 适用于 WiFi 和蓝牙的集成攻击和防御工具套件。
- [ArduinoPcap](https://github.com/spacehuhn/ArduinoPcap) - 一个库，允许为两个 ESP 生成具有网络流量的 .pcap 文件。
- [WiFi Satellite](https://hackaday.io/project/28831-wifi-satellite-34c3) - 一个巨大的 Wifi“卫星”，可以使用 14 个 ESP32 监控所有 14 个 2.4Ghz 通道。
- [ESP8266 Deauther](https://github.com/spacehuhn/esp8266_deauther) - 一个非常酷的 Wifi 网络伪干扰器（deauther），使用 ESP8266。
- [PacketMonitor](https://github.com/spacehuhn/PacketMonitor32) - 漂亮的 OLED 监视器，用于监控 WiFi 通道中的数据包活动。每个 ESP 有两个版本。
- [WiFiDuck](https://github.com/spacehuhn/WiFiDuck) - 无线击键注入器，类似，但比橡胶鸭子更棒。
- [ESP8266 Beacon Spam](https://github.com/spacehuhn/esp8266_beaconSpam) - 想迷惑人吗？该设备创建了数百个假 WiFi 网络。
- [DeauthDetector](https://github.com/spacehuhn/DeauthDetector) - 一种小型设备，如果检测到 WiFi 解除认证攻击，就会发光。与过去六个项目是由同一个人制作的。

### 生物医学
- [HeartyPatch](https://heartypatch.protocentral.com/) - 使用 ESP32 的可穿戴 BLE 和 WiFi 连接 ECG-HR 贴片。
- [HealthyPi v4](https://www.crowdsupply.com/protocentral/healthypi-v4-unplugged) - 一款令人惊叹的开源生命体征监测仪，可以监测心电图、呼吸、脉搏血氧饱和度和体温，全部由 ESP32 运行。

### 洛拉

- [Meshtastic](https://www.meshtastic.org/) - ESP32 LoRA 板作为安全、电池寿命长的网状 GPS 通信器。
- [ESP32-Paxcounter](https://github.com/cyberman54/ESP32-Paxcounter#esp32-paxcounter) - Wifi 和蓝牙驱动、支持 LoRaWAN、电池供电的迷你 Paxcounter，构建在廉价的 ESP32 LoRa IoT 板上。
- [Disaster Radio](https://disaster.radio/) - 由太阳供电的抗灾通信网络。

### 音乐和音频

- [Alles](https://github.com/bwhitman/alles) - 一个多扬声器分布式音乐合成器，使用 WiFi 上的 UDP 多播，以 alles machine/AMY 为模型。
- [ESP32-Radio](https://github.com/Edzelf/ESP32-Radio) - 基于 ESP32、VS1053 和 TFT 屏幕的网络收音机。
- [ESPuino](https://github.com/biologist79/ESPuino) - 由 ESP32 供电的 RFID 控制音乐播放器。
- [Knobby](https://github.com/quadule/knobby) - 手持式 Spotify 遥控器可鼓励您探索不熟悉的音乐。
- [PedalinoMini](https://github.com/alf45tar/PedalinoMini) - 一款适用于吉他手的无线 MIDI 踏板控制器，采用 ESP32 构建。
- [Squeezelite-esp32](https://github.com/sle118/squeezelite-esp32) - 具有多房间同步、AirPlay、蓝牙、硬件按钮、显示屏等功能的流媒体音频接收器。
- [ThingPulse esp8266-spotify-remote](https://github.com/ThingPulse/esp8266-spotify-remote) - 通过带有彩色触摸显示屏的 ESP8266 控制您的 Spotify 播放器。

### 智能手表

- [mutantW_V1](https://mutantcybernetics.com/mutantW_V1.html) - 一款基于 ESP32 的开源智能手表，具有 1.7 英寸显示屏、WiFi、蓝牙、NeoPixel 和振动。
- [Open SmartWatch](https://open-smartwatch.github.io/) - 一款配备 GPS、惯性装置和极其酷的 3D 打印表壳的 FOSS 智能手表。
- [StickWatch](https://github.com/eggfly/StickWatch) - 基于 M5Stick 的智能手表模块，使用 ESP32。
- [Watchy](https://watchy.sqfmi.com) - 一款开源电子纸手表，具有多种定制选项。

### 其他
- [SoftRF](https://github.com/lyusupov/SoftRF) - 一个可用于无人机项目的 DIY 航空接近感知系统。
- [Retro ESP32](https://github.com/retro-esp32/RetroESP32) - 一款非常酷的 Odroid Go 启动器（带有 ESP32），可以模拟多种复古游戏机。
- [DroneBridge](https://github.com/DroneBridge/ESP32) - DroneBridge 的实现，是 ESP32 上无人机和无人机的信号链路。
- [E-TKT](https://github.com/andreisperid/E-TKT) - 一款由 ESP32 驱动的 DIY 标签制作器，融合了老式技术和现代技术。
- [FreeTouchDeck](https://github.com/DustinWatts/FreeTouchDeck) - 开源触摸宏板和带有内置 Web 配置器的流控制面板。
- [SmartSpin2k](https://github.com/doudar/SmartSpin2k) - 通过 Zwift 等健身应用程序中的自动阻力旋钮控制，将您的动感单车转变为智能训练器。
- [WirelessPrinting](https://github.com/probonopd/WirelessPrinting) - 从 Cura、PrusaSlicer 或 Slic3r 到连接到 ESP 模块的 3D 打印机进行无线打印。
- [WLED](https://kno.wled.ge/) - 通过 WiFi 使用 ESP8266 或 ESP32 控制多种类型的 RGB(W) LED 灯带。

## 图书馆
- [Wasm3](https://github.com/wasm3/wasm3) - 专为嵌入式设备设计的闪电般快速的 WebAssembly 解释器，与两种 ESP 兼容。
- [Homie8266](https://github.com/marvinroger/homie-esp8266) - 8266 的 Homie 协议的框架实现。
- [ESP-Dash](https://github.com/ayushsharma82/ESP-DASH) - 用于在 8266/32 中创建远程仪表板的美观且快速的框架。无需互联网。
- [ESP_mqtt](https://github.com/tuanpmt/esp_mqtt) - 适用于 ESP8266 的 MQTT 帮助程序库。
- [GUIslice](https://github.com/ImpulseAdventure/GUIslice) - 适用于多种设备和屏幕控制器的拖放 GUI 框架。兼容8266和32。
- [LVGL](https://lvgl.io) - 开源图形库提供创建嵌入式 GUI 所需的一切，具有易于使用的图形元素、美观的视觉效果和低内存占用。
- [MicroWebSrv2](https://github.com/jczic/MicroWebSrv2) - 一个非常强大的 MicroPython Web 服务器，可在 ESP32 中使用。
- [IRremoteESP8266](https://github.com/markszabo/IRremoteESP8266) - 在 ESP8266 中发射和接收 IR 信号。
- [esphomelib](https://github.com/OttoWinter/esphomelib) - 与 8266 中的 HomeAssistant 集成的框架。
- [TTS](https://github.com/jscrane/TTS) - 一个不错的文本到语音库，适用于多种 Arduino 设备，包括 ESP。
- [Free802.11](https://github.com/Jeija/esp32free80211) - 使用 ESP32 发出任意 802.11 信号的库。
- [Koyn](https://github.com/elkrem/koyn) - 适用于 ESP32 和 ESP8266 的去中心化比特币库。
- [TFTLibrary](https://github.com/loboris/ESP32_TFT_library) - ESP32 的 TFT 兼容性。
- [UTFT-ESP](https://github.com/gnulabis/UTFT-ESP) - 对 ESP32/8266 的 UTFT 支持。
- [ESPAudio](https://github.com/earlephilhower/ESP8266Audio) - 用于在 ESP8266/ESP32 中播放各种音频格式的库。
- [ESP32-audioI2S](https://github.com/schreibfaul1/ESP32-audioI2S) - 播放 SD 卡中的 mp3、m4a 和 wav 文件或通过 I2S 接口播放流。
- [AsyncTCP](https://github.com/me-no-dev/ESPAsyncTCP) - 适用于 8266 和 32 的异步 TCP 库。
- [ESP-HomeKit](https://github.com/maximkulkin/esp-homekit) - RTOS 上 8266 的 Homekit 实现。
- [HomeSpan](https://github.com/HomeSpan/HomeSpan) - 一个强大且极其易于使用的 Arduino 库，用于创建您自己的基于 ESP32 的 HomeKit 设备。
- [ESPHelper](https://github.com/ItKindaWorks/ESPHelper) - 适用于 8266 的 MQTT 和 Wi-fi 自动化库。
- [ESPHelper/32](https://github.com/ItKindaWorks/ESPHelper32) - 32 的 ESPHelper 库的端口。
- [ESP8266Wifi](https://github.com/ekstrand/ESP8266wifi) - 适用于 8266 的简单 Arduino Wifi 库。
- [WiFiESP](https://github.com/bportaluri/WiFiEsp) - 用于 Wifi 管理的 Arduino 库，8266 板的客户端/服务器。
- [TinyGSM](https://github.com/vshymanskyy/TinyGSM) - 一个快速简单的 Arduino 库，用于与 GSM 模块交互，还可以通过 AT 命令控制 8266。
- [mJS](https://github.com/cesanta/mjs) - MongooseOS 使用的轻量级且受限制的 JS 引擎，兼容 32 和 8266。
- [ESPUI](https://github.com/s00500/ESPUI) - 一个简单的库，用于为两个 ESP 制作交互式 Web 界面。
- [ESP32 ePaper](https://github.com/loboris/ESP32_ePaper_example) - 用于将 ePaper 模块与 ESP32 结合使用的全功能库。
- [TinyUPnP](https://github.com/ofekp/TinyUPnP) - 用于 8266 和 32 上自动端口转发的轻量级 UPnP IGD 库。
- [Esp32SSHClient](https://github.com/J-Rios/Arduino-esp32sshclient) - 在 ESP32 中实现 SSH 客户端的库。
- [painlessMesh](https://github.com/gmag11/painlessMesh) - 该库负责处理使用 ESP8266 和 ESP32 硬件创建简单网状网络的细节。
- [WifiEspNow](https://github.com/yoursunny/WifiEspNow) - [ESP-NOW](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/network/esp_now.html) 的 Arduino 库，这是 [Espressif](https://github.com/espressif) 定义的无连接 WiFi 通信协议。
- [go-mcu](https://github.com/matiasinsaurralde/go-mcu) - 用于与基于 NodeMCU 的板进行交互的 Golang 包。
- [CanAirIO SensorLib](https://github.com/kike-canaries/canairio_sensorlib#canairio-air-quality-sensors-library) - ESP32/8266 库可自动配置多个 PM2.5、CO2 和环境传感器。
- [Dhyara](https://github.com/neel/dhyara) - 用于使用 ESP Now 创建移动自组织网络 (MANET) 的 C/C++ 库。
- [LedFx](https://github.com/LedFx/LedFx) - 使用音频输入创建实时灯光秀的库。 LedFx 可以控制多个设备，并且可以与廉价的 ESP8266 节点配合使用。
