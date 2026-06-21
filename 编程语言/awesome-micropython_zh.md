<p对齐=“中心”>
  <a href="https://awesome-micropython.com/" style="display:block"><img src="https://raw.githubusercontent.com/mcauser/awesome-micropython/master/docs/img/logo.svg"></a>
</p>
<p对齐=“中心”>
  <a href="https://awesome.re">
    <img alt="Awesome" src="https://awesome.re/badge-flat.svg">
</a>
</p>
<hr>

精彩的 MicroPython 库、框架、软件和资源的精选列表。

[MicroPython](https://micropython.org/) 是 Python 3 编程语言的精简且高效的实现，其中包含 Python 标准库的一小部分，并针对在微控制器和受限环境中运行进行了优化。

## 内容

* [Libraries](#libraries)
  * [AI](#ai)
  * [Audio](#audio)
  * [Communications](#communications)
  * [Cryptography](#cryptography)
  * [Display](#display)
  * [IO](#io)
  * [Mathematics](#mathematics)
  * [Motion](#motion)
  * [Sensors](#sensors)
  * [Scheduling](#scheduling)
  * [Storage](#storage)
  * [Threading](#threading)
  * [用户界面](#user-interface)
  * [Utilities](#utilities)
* [Community](#community)
* [Tutorials](#tutorials)
* [Books](#books)
* [Frameworks](#frameworks)
* [Resources](#resources)
* [Development](#development)
  * [代码生成](#code-generation)
  * [Debugging](#debugging)
  * [Firmware](#firmware)
  * [IDEs](#ides)
  * [Logging](#logging)
  * [Shells](#shells)
  * [Tools](#tools)
* [Miscellaneous](#miscellaneous)
* [Contributing](#contributing)

## 图书馆

您可以在其他地方查找 MicroPython 库：

* [PyPi](https://pypi.org/search/?c=Programming+Language+%3A%3A+Python+%3A%3A+Implementation+%3A%3A+MicroPython) - 此过滤器仅显示 PyPi 上的 MicroPython 库。注意：您无法“pip install”MicroPython 库。有关使用 MicroPython 管理包的更多信息，请参阅 [MicroPython 文档](https://docs.micropython.org/en/latest/reference/packages.html)。
* [GitHub Search](https://github.com/search?q=micropython) - 在 GitHub 中搜索包含 MicroPython 的存储库。
* [GitHub Topic - MicroPython](https://github.com/topics/micropython) - 浏览 GitHub 主题以查找带有 MicroPython 标记的项目。
* [Libraries.io](https://libraries.io/search?q=micropython) - Libraries.io 查询 MicroPython。
* [GitLab Explore](https://gitlab.com/explore?sort=latest_activity_desc&utf8=%E2%9C%93&name=micropython&sort=latest_activity_desc) - 探索 GitLab 上的存储库。
* [Codeberg Explore](https://codeberg.org/explore/repos?tab=&sort=recentupdate&q=micropython) - 探索 Codeberg 上的存储库。

### 人工智能

* [MicroMLP](https://github.com/jczic/MicroMLP) - 适用于 MicroPython 的微神经网络多层感知器（用于 ESP32 和 Pycom 模块）。
* [MicroPython-NeuralNetwork](https://gitlab.com/olivierlenoir/MicroPython-NeuralNetwork) - MicroPython 的神经网络。
* [upython-chat-gpt](https://github.com/karlsoderby/upython-chat-gpt) - 适用于 MicroPython 的 ChatGPT。
* [emlearn-micropython](https://github.com/emlearn/emlearn-micropython) - 适用于 MicroPython 的高效机器学习引擎。
* [mp_esp_dl_models](https://github.com/cnadler86/mp_esp_dl_models) - MicroPython 绑定用于 ESP DL 视觉模型，例如人脸检测。

### 音频

* [micropython-jq6500](https://github.com/rdagger/micropython-jq6500) - JQ6500 UART MP3 模块的驱动程序。
* [KT403A-MP3](https://github.com/jczic/KT403A-MP3) - KT403A 的驱动程序，由 DFPlayer Mini 和 Grove MP3 v2.0 使用。
* [micropython-buzzer](https://github.com/fruch/micropython-buzzer) - 在蜂鸣器上播放诺基亚撰写和中间文件。
* [micropython-dfplayer](https://github.com/redoxcode/micropython-dfplayer) - 控制 DFPlayer 迷你 MP3 播放器模块的库。
* [micropython-dfplayer](https://github.com/ShrimpingIt/micropython-dfplayer) - 使用 UART 的 DFPlayer Mini 驱动程序。
* [micropython-longwave](https://github.com/MattMatic/micropython-longwave) - 适用于 MicroPython 板的 WAV 播放器。
* [micropython-vs1053](https://github.com/peterhinch/micropython-vs1053) - VS1053b MP3 播放器的异步驱动程序。
* [micropython-midi](https://github.com/EMATech/micropython-midi) - MicroPython 的 MIDI 实现示例。
* [upy-rtttl](https://github.com/dhylands/upy-rtttl) - 用于铃声文本传输语言 (RTTTL) 的 Python 解析器。
* [micropython-i2s-examples](https://github.com/miketeachman/micropython-i2s-examples) - 运行 MicroPython 的微控制器上的 I2S 支持示例。
* [micropython-osc](https://github.com/SpotlightKid/micropython-osc) - 适用于 MicroPython 的最小 OSC 客户端和服务器库。
* [micropython-sgtl5000](https://github.com/rdagger/micropython-sgtl5000) - 带耳机放大器的 SGTL5000 低功耗立体声编解码器库。
* [umidiparser](https://github.com/bixb922/umidiparser) - 适用于 MicroPython、CircuitPython 和 Python 的 MIDI 文件解析器。
* [micropython-tas2505](https://github.com/miketeachman/micropython-tas2505) - 适用于 Texas Instruments TAS2505 数字输入 D 类扬声器放大器的 MicroPython 驱动程序。
* [yx5300](https://github.com/QuirkyCort/IoTy/blob/main/public/extensions/yx5300.py) - 可通过串行接口控制的 MP3 播放器。
* [micropython_nonblocking_buzzer](https://github.com/jornamon/micropython_nonblocking_buzzer) - 蜂鸣器类的非阻塞实现，允许您在播放声音时播放基本旋律或声音模式，而不会阻塞主循环。
* [multi-midi](https://github.com/HLammers/multi-midi) - RP2 板的库，为基于 UART 和 PIO 的硬件 MIDI 和 USB MIDI 1.0 提供接口。
* [IoTy vs1003](https://github.com/QuirkyCort/IoTy/blob/main/public/extensions/vs1003.py) - VS1003 MP3 解码器/编码器的驱动程序。支持MP3、WMA、MIDI、ADPCM的播放以及ADPCM的录音。

### 通讯

#### API

* [micropython-utelegram](https://github.com/jordiprats/micropython-utelegram) - MicroPython 的 Telegram API 包装器。
* [uEagle](https://github.com/jcalbert/uEagle) - MicroPython Rainforest EAGLE 客户端。
* [micropython-youtube-api](https://github.com/UnexpectedMaker/micropython-youtube-api) - MicroPython 中的 YouTube API。
* [micropython_esp8266_tweetbot](https://github.com/ayoko/micropython_esp8266_tweetbot) - 适用于 MicroPython v1.8.4 (ESP8266) 的推文机器人。
* [telegram-upy](https://github.com/gabrielebarola/telegram-upy) - MicroPython 的 Telegram API 包装器。
* [micropython-thingspeak](https://github.com/radeklat/micropython-thingspeak) - 用于从运行 MicroPython 的 IoT 设备（例如 ESP8266）向 thingspeak.com 发送数据的库。
* [micropython_pushbullet](https://github.com/gsampallo/micropython_pushbullet) - 如何在 ESP8266 上将 PushBullet 与 MicroPython 结合使用的简单示例。
* [esp32-youtube-display](https://github.com/alvarowolfx/esp32-youtube-display) - 使用 Google API 和 MicroPython 显示 YouTube 指标。
* [micropython-spotify-web-api](https://github.com/tltx/micropython-spotify-web-api) - 用于通过 MicroPython 从 IoT 设备使用 Spotify Web API 的库。
* [micropython_demo_bot](https://github.com/gsampallo/micropython_demo_bot) - 关于如何为 Telegram 创建机器人的小例子。
* [micropython-basicdweet](https://github.com/jacklinquan/micropython-basicdweet) - 一个 Python 模块，用于免费 dweet 服务的非常基本的 API。
* [micropython-dweeter](https://github.com/jacklinquan/micropython-dweeter) - 用于通过免费 dweet 服务发送消息的 python 模块。
* [micropython-cryptodweet](https://github.com/jacklinquan/micropython-cryptodweet) - 一个 Python 模块，用于带加密的免费 dweet 服务的非常基本的 API。
* [micropython-linenotify](https://github.com/PerfecXX/micropython-linenotify) - MicroPython 库，用于使用 ESP8266 和 ESP32 向 Line Notify 发送通知。
* [micropython-telegram-bot](https://github.com/antirez/micropython-telegram-bot) - MicroPython telegram bot 库：将 IoT 项目放在云端的简单方法。
* [MicroPython-GoogleSheet](https://github.com/PerfecXX/MicroPython-GoogleSheet) - 使用 Google Apps 脚本 API 获取、更新或附加 Google 表格中的数据。

#### 认证

* [micropython-firebase-auth](https://github.com/WoolDoughnut310/micropython-firebase-auth) - MicroPython 的 Firebase Auth 实现。

#### 蓝牙

* [PyBoard-HC05-Android](https://github.com/KipCrossing/PyBoard-HC05-Android) - Pyboard HC05 蓝牙适配器示例应用程序。
* [uble](https://github.com/dmazzella/uble) - 用纯 Python 为 MicroPython 编写的轻量级蓝牙低功耗驱动程序。
* [MicroPythonBLEHID](https://github.com/Heerkog/MicroPythonBLEHID) - 适用于 MicroPython 的基于蓝牙低功耗 (BLE) 的人机接口设备 (HID) GATT 库。
* [upyble](https://github.com/Carglglz/upyble) - 用于低功耗蓝牙 MicroPython 设备的命令行工具。
* [micropython-xiaomi-ble-adv-parse](https://codeberg.org/scy/micropython-xiaomi-ble-adv-parse) - 从某些小米蓝牙低功耗 (BLE) 传感器被动检索传感器数据。
* [mijia-temphum-upy](https://codeberg.org/scy/mijia-temphum-upy) - 用于读取某些小米米家BLE温度和湿度传感器的MicroPython库。
* [micropython-aioble-itag](https://github.com/mcauser/micropython-aioble-itag) - 使用 aioble 与 iTag BLE 钥匙串标签交互的示例。
* [micropython_aioble_examples](https://github.com/ekspla/micropython_aioble_examples) - 使用 ESP32 的 MicroPython 的几个 aioble（asyncio BLE）示例。
* [BTHome-MicroPython](https://github.com/DavesCodeMusings/BTHome-MicroPython) - MicroPython 模块用于格式化 BTHome BLE 广告有效负载的传感器读数。

#### CAN

* [micropython-spacecan](https://gitlab.com/alphaaomega/micropython-spacecan) - Spacecan 是针对嵌入式系统的 SpaceCAN 协议的 MicroPython 实现。
* [Robomaster-Micropython](https://github.com/JohnieBraaf/Robomaster-Micropython) - Robomaster S1 - MicroPython CAN 总线控制器。
* [micropython-mcp2515](https://github.com/jxltom/micropython-mcp2515) - MicroPython MCP2515 驱动程序，从 Arduino MCP2515 CAN 接口库移植。
* [microPython_MCP2515](https://github.com/capella-ben/microPython_MCP2515) - 用于 MCP2515 CAN 总线控制器的 MicroPython 库。

#### 压缩

* [ufastlz](https://github.com/dmazzella/ufastlz) - FastLZ 的 MicroPython 包装器，这是一个闪电般快速的无损压缩库。
* [tamp](https://github.com/BrianPugh/tamp) - 一个低内存、MicroPython 优化、受 DEFLATE 启发的无损压缩库。
* [micropython-zipfile](https://github.com/jonnor/micropython-zipfile) - 读取/写入 ZIP 存档文件。从CPython移植，支持DEFLATE压缩。
* [bitstruct-micropython](https://github.com/peterzuger/bitstruct-micropython) - [bitstruct](https://github.com/eerimoq/bitstruct) 的 MicroPython 端口。

#### 密码学

* [ucryptography](https://github.com/dmazzella/ucryptography) - 基于 ARM Mbed TLS 将 pyca/cryptography 轻量级移植到 MicroPython。
* [mpyaes](https://github.com/iyassou/mpyaes) - 用于 AES 加密的 MicroPython 模块。
* [micropython-aes](https://github.com/piaca/micropython-aes) - 纯Python实现的AES算法。
* [ucrypto](https://github.com/dmazzella/ucrypto) - MicroPython 包，用于执行快速 RSA 和椭圆曲线加密，特别是数字签名。 ECDSA API 设计灵感来自 fastecdsa 并基于 tomsfastmath 实现。
* [ucryptoauthlib](https://github.com/dmazzella/ucryptoauthlib) - 使用纯 Python 为 MicroPython 编写的 Microchip 加密身份验证安全元素的轻量级驱动程序。
* [embit](https://github.com/diybitcoinhardware/embit) - 适用于 MicroPython 和 Python 3 的最小比特币库，重点关注嵌入式系统。
* [microotp](https://github.com/gdassori/microotp) - ESP8266 MicroPython OTP 生成器。
* [micropython-rsa-signing](https://github.com/artem-smotrakov/micropython-rsa-signing) - MicroPython 上的 RSA 签名。
* [micropython-cryptomsg](https://github.com/jacklinquan/micropython-cryptomsg) - 使用 AES CBC 模式加密和解密消息的 MicroPython 模块。
* [mprsa](https://github.com/git-n-pissed/mprsa) - MicroPython 模块，用于使用 PKCS#1、PKCS#8 和 X.509/SPKI 结构创建、导入和导出 DER 和 PEM 格式的 RSA 密钥，并使用盲法以及 SHA-1 和 SHA-256 哈希算法进行签名/验证和加密/解密。
* [mpy-mbedtls](https://github.com/Carglglz/mpy-mbedtls) - 一些 MbedTLS EC 和 x509 cert/csr 函数的 MicroPython 绑定。
* [micropython-cryptocfb](https://github.com/jacklinquan/micropython-cryptocfb) - 使用 AES-128 CFB 模式加密和解密数据的 Python 模块。
* [tscp](https://github.com/shariltumin/tscp) - 基于 Diffie-Hellman-Merkle 的端点到端点加密，并使用 MicroPython 进行 TLS1.3 式握手。
* [usigv4](https://github.com/vhespanha/usigv4) - 用于 MicroPython/嵌入式使用的最小 AWS 签名版本 4 (SigV4) 实现。

#### 域名系统

* [aiodns](https://github.com/vshymanskyy/aiodns) - 一个小型、多功能的 DNS 客户端，提供异步版本的“getaddrinfo”并适用于任何连接。
* [ICantBelieveItsNotDNS](https://github.com/yschaeff/ICantBelieveItsNotDNS) - “我不敢相信这不是 DNS！” (ICBIND) 是用 MicroPython 编写的 ESP8266 权威 DNS 服务器。
* [MicroDNSSrv](https://github.com/jczic/MicroDNSSrv) - MicroPython 的微型 DNS 服务器，可简单地响应带或不带通配符的多域上的 A 查询（用于 Pycom 模块和 ESP32）。
* [tinydns](https://github.com/belyalov/tinydns) - 非常简单的 MicroPython DNS 异步服务器。
* [micropython-captiveportal](https://github.com/metachris/micropython-captiveportal) - MicroPython 的最小异步强制门户（与 uasyncio v3/MicroPython 1.13+ 以及早期版本兼容）。
* [Micropython-DNSServer-Captive-Portal](https://github.com/p-doyle/Micropython-DNSServer-Captive-Portal) - 带有 DNS 和 Web 服务器的 MicroPython WiFi AP 强制门户。

#### ESP-NOW

* [mesh-espnow-micropython](https://github.com/shariltumin/mesh-espnow-micropython) - 用于物联网设备协作节点的动态安全网格。
* [mp_espnow_wrapper](https://github.com/cnadler86/mp_espnow_wrapper) - 通过 ESP-NOW 在 ESP 之间发送和接收数据，无需担心。

#### 以太网

* [Official WIZnet5k](https://github.com/andrewleech/wiznet_ioLibrary_Driver) - WIZnet5x00 系列以太网控制器的驱动程序。
* [micropy-ENC28J60](https://github.com/przemobe/micropy-ENC28J60) - 适用于 MicroPython (RP2) 的 ENC28J60 以太网芯片驱动程序。
* [RP2040 Ethernet example](https://github.com/SteveSEK/Raspberry-Pi-Pico-MicroPython-Ethernet) - 以太网驱动程序，示例 Python 代码和 YouTube。
* [micropython-ch9121](https://github.com/wybiral/micropython-ch9121) - 用于控制 CH9121 以太网模块的 MicroPython 库。

#### 文件传输协议

* [micropython-ftplib](https://github.com/SpotlightKid/micropython-ftplib) - MicroPython 的 FTP 客户端库。
* [FTP-Server-for-ESP8266-ESP32-and-PYBD](https://github.com/robert-hh/FTP-Server-for-ESP8266-ESP32-and-PYBD) - MicroPython 平台上适用于 ESP8266/ESP32/Pyboard 的小型 FTP 服务器。
* [MicroFTPServer](https://github.com/cpopp/MicroFTPServer) - 可在带有 MicroPython 的 ESP8266 上运行的最小 FTP 服务器。
* [micropython-uaioftp](https://github.com/cwyark/micropython-uaioftp) - 适用于 MicroPython 的轻量级 FTP 库。
* [FtpTiny-Micropython](https://github.com/MZachmann/FtpTiny-Micropython) - 在线程中运行的非常小的 FTP 服务器。

#### 全球定位系统

* [micropyGPS](https://github.com/inmcm/micropyGPS) - 全功能 GPS NMEA 句子解析器。
* [micropython-gnssl76l](https://github.com/tuupola/micropython-gnssl76l) - 适用于移远 GNSS L76-L (GPS) 的 MicroPython I2C 驱动程序。
* [mpy-agps](https://github.com/pulkin/mpy-agps) - 辅助定位服务 (AGPS) 的 MicroPython 实现。
* [Asynchronous GPS driver](https://github.com/peterhinch/micropython-async/blob/master/v3/docs/GPS.md) - 作为 uasyncio 任务接收和解析 GPS 数据。

#### 全球移动通信系统

* [micropython-upyphone](https://github.com/jeffmer/micropython-upyphone) - 使用 Pyboard 和 SIM800l 的 GSM 手机。
* [micropython-sim800](https://github.com/olablt/micropython-sim800) - SIM800 的 MicroPython 驱动程序。
* [sim800](https://github.com/basanovase/sim800) - 用于与 MicroPython 中的 SIM800 模块连接的库。
* [MicroPython-AM7020](https://github.com/JiekangHuang/MicroPython-AM7020) - AM7020 窄带物联网 (NBIoT) 模块的 MicroPython 驱动程序。
* [SIM800L-micropython](https://github.com/aleppax/SIM800L-micropython) - 用于常见 SIM800L AT 命令的 MicroPython 包装器。
* [sim7600](https://github.com/basanovase/sim7600) - SIM7600 模块的 MicroPython 库。
* [sim900](https://github.com/basanovase/sim900) - SIM900 GSM/GPRS 模块的 MicroPython 库。

#### HTTP协议

* [mrequests](https://github.com/SpotlightKid/mrequests) - 用于 MicroPython 的 HTTP 客户端模块（不仅如此），具有类似于请求的 API。
* [uht](https://github.com/nmattia/uht) - MicroPython 的轻量级 HTTP 服务器（提供网站服务并处理请求）。

#### 物联网

* [aiomqttc](https://github.com/Tangerino/aiomqttc) - 适用于 MicroPython 和 CPython 的异步 MQTT 客户端。
* [microhomie](https://github.com/microhomie/microhomie) - IoT 的 Homie MQTT 约定的 MicroPython 实现。
* [uPyEcho](https://github.com/lemariva/uPyEcho) - 模拟 Belkin WeMo 设备，可在 ESP32 上使用 MicroPython 与 Amazon Echo (Alexa) 配合使用。
* [SonosRemote](https://github.com/foosel/SonosRemote) - 在 ESP8266 上运行并使用 Sonos HTTP API 的 Sonos 安装遥控器。
* [micropython-home-assistant](https://gitlab.com/aapjeisbaas/micropython-home-assistant) - 基于 MicroPython 的脚本可扩展您的 Home Assistant 驱动的家庭自动化项目。
* [micropython-iot](https://github.com/peterhinch/micropython-iot) - 一种使用 ESP8266、ESP32 或 Pyboard D 端点设计 IoT 应用程序的方法。
* [iot-core-micropython](https://github.com/GoogleCloudPlatform/iot-core-micropython) - 使用 MicroPython 连接到 Google Cloud IoT Core。
* [SmartUPy](https://github.com/lemariva/SmartUPy) - 使用MicroPython控制“涂鸦式”智能电源插座。
* [aws-iot-GET-POST-loop](https://github.com/manningt/aws-iot-GET-POST-loop) - 使用 AWS IoT REST API 获取/发布设备状态信息的 MicroPython 代码。
* [sensor-mqtt-homeassistant](https://github.com/DougWilkinson/sensor-mqtt-homeassistant) - 基于 ESP8266/ESP32 MicroPython 的传感器平台，适用于 GPIO、DHT、模拟、LED 等。包括来自 Web 服务器和 MQTT/Home Assistant 集成的 .py 代码的远程更新。
* [micropython-ha-mqtt-device](https://github.com/agners/micropython-ha-mqtt-device) - MicroPython 模块，允许使用 MQTT Discovery 创建 HomeAssistant 实体。
* [ESP8266-Home-Assistant-Smart-Socket](https://github.com/AnthonyKNorman/ESP8266-Home-Assistant-Smart-Socket) - 这个 MicroPython 项目是破解 Hyleton313 廉价 WiFi 智能插座。
* [ESP8266-Home-Assistant-RGB-Bulb](https://github.com/AnthonyKNorman/ESP8266-Home-Assistant-RGB-Bulb) - 这个 MicroPython 项目旨在破解廉价 WiFi RGB 灯泡中的 TYWE3S 板。
* [uPyIoT](https://github.com/lemariva/uPyIoT) - 将运行 MicroPython 的 M5Stack ATOM 连接到 Google 云平台 (GCP)，以收集从读取传感器获得的空气质量变量。
* [micropython-switchbot-thermometer-hygrometer](https://github.com/hilch/micropython-switchbot-thermometer-hygrometer) - 通过蓝牙读取 SwitchBot 温度计/湿度计。

#### 红外

* [micropython-necir](https://github.com/MattMatic/micropython-necir) - 用于 TL1838 红外接收器 LED 的 NEC 红外捕获。
* [Micropython-IR](https://github.com/designerPing/Micropython-IR) - Pyboard 红外远程嗅探和重放。
* [micropython_ir](https://github.com/peterhinch/micropython_ir) - 用于从红外遥控器和红外“blaster”应用程序接收信息的非阻塞设备驱动程序。
* [micropython-amg88xx](https://github.com/peterhinch/micropython-amg88xx) - Grid-EYE 热红外阵列传感器 (Adafruit 3538) 的驱动程序。
* [micropython-ys-irtm](https://github.com/mcauser/micropython-ys-irtm) - YS-IRTM 5V NEC 红外 UART 收发器的 MicroPython 示例。
* [esp8266_ir](https://github.com/ruoyu0088/esp8266_ir) - 通过WebSocket控制红外信号。
* [micropython_espX_IR_Transceiver](https://github.com/gamefunc/micropython_espX_IR_Transceiver) - MicroPython ESP32 红外收发器。
* [pico-ir](https://github.com/bartoszadamczyk/pico-ir) - Raspberry Pi Pico 的 IR 库。
* [esp32-ir-remote](https://github.com/cbrand/esp32-ir-remote) - 用于运行 ESP32 IR 遥控器的 MicroPython 项目。

#### 洛拉

* [loraE22](https://github.com/matthias-bs/loraE22) - Ebyte E22 系列 LoRa 模块的 MicroPython 类。
* [micropython-lora](https://github.com/wybiral/micropython-lora) - 用于通过 SPI 控制 Semtech SX127x LoRa 模块的 MicroPython 库。
* [micropython-aiolora](https://github.com/wybiral/micropython-aiolora) - MicroPython 库，用于使用 asyncio API 控制 Semtech SX127x LoRa 模块。
* [micropython-rylr](https://github.com/wybiral/micropython-rylr) - 用于控制 Reyax LoRa 模块（RYLR896、RYLR406）的 MicroPython 库。
* [silvergeko_rfm9x](https://github.com/scopelemanuele/silvergeko_rfm9x) - 移植到 adafruit_rfm9x.py 库的 MicroPython。
* [EByte_LoRa_E220_micropython_library](https://github.com/xreef/EByte_LoRa_E220_micropython_library) - MicroPython LoRa EBYTE E220 设备。
* [EByte_LoRa_E22_micropython_library](https://github.com/xreef/EByte_LoRa_E22_micropython_library) - MicroPython LoRa EBYTE E22 设备。
* [EByte_LoRa_E32_micropython_library](https://github.com/xreef/EByte_LoRa_E32_micropython_library) - MicroPython LoRa EBYTE E32 设备。

#### 洛拉万

* [uPyLoRaWAN](https://github.com/lemariva/uPyLoRaWAN) - 使用 MicroPython 的 ESP32 满足 LoRa 和 LoRaWAN 的要求。
* [SX127x_driver_for_MicroPython_on_ESP8266](https://github.com/Wei1234c/SX127x_driver_for_MicroPython_on_ESP8266) - 适用于 ESP8266/ESP32/Raspberry Pi 上 (Micro)Python 的 SX127x（LoRa 收发器）驱动程序。
* [LightLora_MicroPython](https://github.com/MZachmann/LightLora_MicroPython) - 适用于 MicroPython 的轻量级中断驱动 Semtech SX127x 库。
* [u-lora](https://github.com/martynwheeler/u-lora) - 适用于 MicroPython 的 Raspi-lora。
* [sx127x_esp](https://github.com/azorg/sx127x_esp) - 将基于 LoRaTM sx127x 芯片的 Ra-01 模块连接到 MicroPython 下的 ESP8266/ESP32。
* [nanoserver](https://github.com/gradoj/nanoserver) - MicroPython 嵌入式 LoRaWAN 服务器。
* [micropySX126X](https://github.com/ehong-tl/micropySX126X) - 适用于 MicroPython 和 CircuitPython 的 Semtech SX126X LoRa 驱动程序。

#### 移动域名系统

* [micropython-mdns](https://github.com/cbrand/micropython-mdns) - MDNS 的纯 Python 实现，支持服务发现。

#### MODBUS

* [micropython-modbus](https://gitlab.com/extel-open-source/micropython-modbus) - modbus-tk 的 MicroPython 端口。
* [micropython-modbus](https://github.com/techbase123/micropython-modbus) - 适用于 MicroPython ESP32 设备的 Modbus Master 库。基于 Pycom 的 pycom-modbus。
* [mp_modbus](https://github.com/eydam-prototyping/mp_modbus) - MicroPython 的 Modbus 库。
* [micropython-modbus](https://github.com/brainelectronics/micropython-modbus) - ModBus TCP 和 RTU 库支持客户端和主机模式。基于 Pycom 的 pycom-modbus。

#### MQTT

* [micropython-mqtt](https://github.com/peterhinch/micropython-mqtt) - “弹性”异步 MQTT 客户端：从 WiFi 和代理中断中恢复。
* [MQBoard](https://github.com/tve/mqboard) - 一个微框架，用于在 MicroPython 板上（主要在 ESP32 上）使用 MQTT 和 asyncio。
* [pysmartnode](https://github.com/kevinkk525/pysmartnode) - MicroPython 智能家居框架。
* [umqtt_aws_iot](https://github.com/juwul/umqtt_aws_iot) - 使用 MicroPython 将 UMQTT 消息发布到 AWS IoT。
* [sonoff-mqtt by davea](https://github.com/davea/sonoff-mqtt) - 使用 MQTT 控制 Sonoff/ESP8266 的 MicroPython 脚本。
* [micropython-sonoff-switch](https://github.com/kfricke/micropython-sonoff-switch) - 使用 MicroPython 为 iTead Sonoff Switch 实现 MQTT 可控开关。
* [micropython-thingspeak-mqtt-esp8266](https://github.com/miketeachman/micropython-thingspeak-mqtt-esp8266) - 使用 MQTT 和在 ESP8266/ESP32 平台上运行的 MicroPython 发布和订阅 ThingSpeak。
* [uMQTT](https://github.com/andrewmk/uMQTT) - MQTT 在 WiPy 板上发布 MicroPython。
* [micropython-mqtt](https://github.com/chrismoorhouse/micropython-mqtt) - 具有自动重新连接功能的异步 MQTT 库，适用于 MicroPython 设备（例如 ESP32 或 Pycom 设备）。
* [micropython-adafruit-mqtt-esp8266](https://github.com/miketeachman/micropython-adafruit-mqtt-esp8266) - 使用 MQTT 发布/订阅 Adafruit IO。 ESP8266/ESP32 上的 MicroPython/CircuitPython 实现。
* [mqtt_upython](https://github.com/matbgn/mqtt_upython) - 在 ESP8266 上使用 MicroPython 的 MQTT 客户端。
* [tinymqtt](https://github.com/belyalov/tinymqtt) - MicroPython 的异步 MQTT 客户端。
* [micropython-mqtt-thingspeak](https://github.com/miketeachman/micropython-mqtt-thingspeak) - 使用 MQTT 和 MicroPython 发布和订阅 ThingSpeak。
* [micropython-sparkplugb](https://github.com/sciotaio/micropython-sparkplugb) - Eclipse Sparkplug B 规范的 MicroPython 兼容实现。

#### NBD

* [unbd](https://github.com/pulkin/unbd) - MicroPython 的网络块设备 (NBD) 的微实现。

#### 近场通信

* [micropython-nfc](https://github.com/rolandvs/micropython-nfc) - 将 NFC 与 MicroPython 结合使用。
* [micropython_pn532](https://github.com/luiz-brandao/micropython_pn532) - 基于 Adafruit CircuitPython (UART) 的 PN532 NFC/RFID 分线板驱动程序。
* [NFC_PN532_SPI](https://github.com/Carglglz/NFC_PN532_SPI) - Adafruit CircuitPython 到 PN532 NFC/RFID 控制库 (SPI) 的 MicroPython 的部分移植。

#### NTP

* [esp8266_ntp_webserver](https://github.com/Roterfux/esp8266_ntp_webserver) - MicroPython + ESP8266 + NTP + 网络服务器。
* [micropython-ntpd](https://github.com/dave2/micropython-ntpd) - MicroPython 中 NTP 守护进程的实现。
* [micropython_ntpserver](https://github.com/GrantGMiller/micropython_ntpserver) - 为 MicroPython 编写的 NTP 服务器。
* [micropython-ntpclient](https://github.com/wieck/micropython-ntpclient) - 使用 uasyncio 的 MicroPython NTP 客户端。
* [micropython-ntp](https://github.com/ekondayan/micropython-ntp) - 适用于 MicroPython 的强大 NTP 库。
* [micropython-simple-async-ntpclient](https://codeberg.org/dsiggi/micropython-simple_async_ntpclient) - 非常简单的异步 MicroPython 模块，用于从 NTP 服务器接收当前时间。

#### 对象存储

* [uminio](https://github.com/paluigi/uminio) - 用于将文件上传到 MinIO 对象存储服务器的 MicroPython 库。

#### 单线

* [Official OneWire](https://github.com/micropython/micropython-lib/tree/master/micropython/drivers/bus/onewire) - 适用于使用 OneWire 总线的设备，例如 Dallas DS18x20。
* [Onewire_DS18X20](https://github.com/robert-hh/Onewire_DS18X20) - 用于使用 Pycom MicroPython 的 OneWire 协议驱动 DS18x20 传感器的类。
* [micropython_arduino_control](https://github.com/kevinkk525/micropython_arduino_control) - MicroPython 库可通过相应的 Arduino 代码远程控制 Arduino。

#### 安桥EISCP

* [eiscp-micropython](https://github.com/cbrand/eiscp-micropython) - Pioneer 等公司使用的 Onkyo-EISCP 协议的 MicroPython 端口。

#### 在线旅行社

* [micropython-ota-updater](https://github.com/rdehuyss/micropython-ota-updater) - MicroPython 的 OTA 更新程序。
* [Micropython-ESP32-OTA](https://github.com/AkhileshThorat/Micropython-ESP32-OTA) - 基于 rdehuyss/micropython-ota-updater 的 MicroPython 更新程序。
* [senko](https://github.com/RangerDigital/senko) - 适用于 MicroPython 项目的最简单的 OTA 更新解决方案。

#### 代理

* [uProxy](https://github.com/shawwwn/uProxy) - 适用于 MicroPython 的基于异步、内存高效的 HTTP/HTTPS/SOCKS4/SOCKS5 转发代理服务器，与 CPython 兼容。

#### 收音机

* [micropython-radio](https://github.com/peterhinch/micropython-radio) - nRF24L01 2.4GHz 无线电模块的协议。
* [micropython-rfsocket](https://github.com/wuub/micropython-rfsocket) - MicroPython 实现了流行的基于 433MHz 的 RFSocket。
* [Official nRF24L01](https://github.com/micropython/micropython-lib/tree/master/micropython/drivers/radio/nrf24l01) - nRF24L01 2.4GHz 无线电模块的官方驱动程序。
* [micropython_remote](https://github.com/peterhinch/micropython_remote) - 捕获并重放 433MHz 遥控代码。控制远程开关电源适配器。
* [micropython-ys-rf34t](https://github.com/mcauser/micropython-ys-rf34t) - 使用 YS-RF34T 433MHz ASK/OOK UART 收发器的 MicroPython 示例。
* [FM_Talkie](https://github.com/Wei1234c/FM_Talkie) - 使用 RDA5820N 的 FM 对讲机。
* [micropython-TEA5767](https://github.com/alankrantas/micropython-TEA5767) - 适用于 TEA5767 FM 收音机模块的 MicroPython ESP8266/ESP32 驱动程序。
* [micropython-ppm-decoder](https://github.com/dastultz/micropython-ppm-decoder) - 用于解码 R/C 接收器 PPM 帧信号的实用程序。
* [ESP32-433Mhz-Receiver-and-Tools](https://github.com/Aschhoff/ESP32-433Mhz-Receiver-and-Tools) - 用 MicroPython 和 Windows 工具编写的 ESP32 433MHz 接收器。
* [ESP32-433Mhz-Transmitter](https://github.com/Aschhoff/ESP32-433Mhz-Transmitter) - 纯 MicroPython RF 发射器。您可以创建并添加自己的编码器。
* [pico_jjy_tx](https://github.com/elehobica/pico_jjy_tx) - 适用于 Raspberry Pi Pico W 的 JJY 发射器。
* [pico_dcf77_tx](https://github.com/elehobica/pico_dcf77_tx) - 适用于 Raspberry Pi Pico W 的 DCF77 发射器。
* [micropython_dcf77](https://codeberg.org/dsiggi/micropython-dcf77) - DCF77接收器和解码器。
* [MicroPython-BresserWeatherSensorReceiver](https://github.com/matthias-bs/MicroPython-BresserWeatherSensorReceiver) - Bresser 5-in-1/6-in-1/7-in-1 868 MHz 天气传感器无线电接收器和解码器。

#### 遥控接收器

* [micropython-ppm_reader](https://github.com/redoxcode/micropython-ppm_reader) - 用于解码来自 RC 接收器的 PPM 信号的库。

#### REPL

* [webrepl](https://micropython.org/webrepl) - MicroPython WebREPL。
* [zepl](https://gitlab.com/zepl1/zepl) - 使用 ZeroMQ 的 MicroPython WebREPL 控制台应用程序。
* [jupyter_micropython_remote](https://gitlab.com/alelec/jupyter_micropython_remote) - Jupyter 内核通过串行/网络 REPL 直接在 MicroPython 板上执行代码。
* [FBConsole](https://github.com/boochow/FBConsole) - MicroPython 的帧缓冲区控制台类。

#### 射频识别

* [micropython-mfrc522](https://github.com/wendlers/micropython-mfrc522) - NXP MFRC522 RFID 读写器的驱动程序。
* [micropython-wiegand](https://github.com/pjz/micropython-wiegand) - 韦根协议阅读器。
* [urdm6300](https://github.com/membermatters/urdm6300) - 适用于流行的 RDM6300 RFID 读卡器的 MicroPython 驱动程序。

#### 远程过程调用

* [ujrpc](https://github.com/zcattacz/ujrpc) - MicroPython 的 JSON RPC。

#### 实时时钟

* [micropython-tinyrtc-i2c](https://github.com/mcauser/micropython-tinyrtc-i2c) - DS1307 RTC 和 AT24C32N EEPROM 的驱动程序。
* [Micropython_TinyRTC](https://github.com/AnthonyKNorman/Micropython_TinyRTC) - DS1307 RTC 驱动程序。
* [micropython-mcp7940](https://github.com/mattytrentini/micropython-mcp7940) - Microchip MCP7940 RTC 的驱动程序。
* [micropython-ds1302-rtc](https://github.com/omarbenhamid/micropython-ds1302-rtc) - 适用于 MicroPython 的 DS1302 RTC 时钟驱动程序。
* [DS3231micro](https://github.com/notUnique/DS3231micro) - DS3231 的 MicroPython 库。
* [micropython-ds1307](https://github.com/brainelectronics/micropython-ds1307) - DS1307 RTC 的 MicroPython 驱动程序。
* [esp-ds3231-micropython](https://github.com/HAIZAKURA/esp-ds3231-micropython) - 适用于 ESP8266/ESP32 的 DS3231 库，采用 MicroPython。
* [PCF8563_PythonLibrary](https://github.com/lewisxhe/PCF8563_PythonLibrary) - 适用于 NXP PCF8563 实时时钟/日历的 MicroPython 库。
* [DS3231](https://github.com/octaprog7/DS3231) - 适用于 Maxim Integrated 的 DS3231 时钟的 MicroPython 模块。
* [DS1307](https://github.com/peter-l5/DS1307) - DS1307 实时时钟的 MicroPython 驱动程序。
* [micropython-DS3231-AT24C32](https://github.com/pangopi/micropython-DS3231-AT24C32) - DS3231 RTC 的 MicroPython 驱动程序。
* [micropython_rx-8035](https://github.com/ekspla/micropython_rx-8035) - 适用于 Seiko Epson 的 RTC、RX-8035SA/LC 的 MicroPython 驱动程序。
* [micropython-ds1302-rtc](https://github.com/PaszaVonPomiot/micropython-ds1302-rtc) - 适用于 MicroPython 的 DS1302 RTC 时钟驱动程序。

#### 串行

* [mpy-miniterm](https://github.com/jeffmakes/mpy-miniterm) - 通过串行 REPL 与 MicroPython 设备进行无缝串行调试和文件同步的工具。
* [MicroPython-MorseCode](https://gitlab.com/olivierlenoir/MicroPython-MorseCode) - 使用带有 MicroPython 的微控制器的国际摩尔斯电码。
* [I2C Slave](https://github.com/peterhinch/micropython-async/blob/master/v3/docs/I2C.md) - 使用Pyboard的I2C从机模式实现全双工异步链路。主要用例是 ESP8266，它只有一个 UART。
* [microSDI12](https://github.com/insighio/microSDI12) - 迷你 SDI-12 实现，用于通过 RS-485 获取传感器信息。

#### 序列化

* [micropython-msgpack](https://github.com/peterhinch/micropython-msgpack) - 针对 MicroPython 优化的 MessagePack 序列化库。
* [micropython-uprotobuf](https://github.com/jazzycamel/micropython-uprotobuf) - 适用于 MicroPython 的 Google Protocol Buffers (protobuf) 的轻量级实现。
* [minipb](https://github.com/dogtopus/minipb) - 纯 Python 中的迷你 Protobuf {de}序列化器。
* [ucbor](https://github.com/dmazzella/ucbor) - MicroPython 的 cbor 轻量级实现。
* [upy-msgpack](https://github.com/SpotlightKid/upy-msgpack) - 用于 MicroPython 的轻量级 MessagePack（反）序列化库（不仅如此）。
* [micropython-msgpack](https://github.com/gitcnd/micropython-msgpack) - 针对 MicroPython 优化的 MessagePack 序列化库。

#### 邮件传输协议

* [uMail](https://github.com/shawwwn/uMail) - 一个轻量级、可扩展的 SMTP 客户端，用于在 MicroPython 中发送电子邮件。

#### 插座

* [XAsyncSockets](https://github.com/jczic/XAsyncSockets) - XAsyncSockets 是一个高效的 Python/MicroPython 托管异步套接字库。

#### 袜子

* [micropython-socks](https://github.com/kost/micropython-socks) - 实现 SOCKS 服务器的 MicroPython 库。

#### 传输控制协议

* [us2n](https://github.com/tiagocoutinho/us2n) - ESP32 的 UART 和 TCP 之间的 MicroPython 桥接器。

#### 远程登录

* [MicroTelnetServer](https://github.com/cpopp/MicroTelnetServer) - 适用于 MicroPython 和 ESP8266 的简单 telnet 服务器允许 telnet 客户端访问 REPL。
* [telnetd](https://github.com/gitcnd/telnetd) - 强大的 telnetd 服务器可访问 MicroPython REPL（具有强大的密码支持和无限连接）。

#### 文字转语音

* [micropython-SYN6988](https://github.com/scruss/micropython-SYN6988) - 用于 VoiceTX SYN6988 文本转语音模块的 MicroPython 库。
* [micropython-samtts](https://github.com/jacklinquan/micropython-samtts) - 软件自动口文本转语音程序的 MicroPython 端口。

#### 时间

* [ustrftime](https://github.com/iyassou/ustrftime) - time.strftime 的 MicroPython 实现。

#### 网络电话

* [uPyVoip](https://github.com/RetepRelleum/uPyVoip) - 适用于 MicroPython ESP32 的 VoIP，具有交互式语音响应。

#### 网络

* [MicroWebSrv](https://github.com/jczic/MicroWebSrv) - 一个微型 HTTP Web 服务器，支持 WebSocket、HTML/Python 语言模板和路由处理程序，适用于 MicroPython（用于 Pycom 模块和 ESP32）。
* [MicroWebSrv2](https://github.com/jczic/MicroWebSrv2) - 最后一款用于物联网 (MicroPython) 或大型服务器 (CPython) 的微型 Web 服务器，支持 WebSocket、路由、模板引擎并具有真正优化的架构（内存分配、异步 I/O）。
* [tinyweb](https://github.com/belyalov/tinyweb) - 适用于 MicroPython 的简单且轻量级的 HTTP 异步服务器。
* [upy-websocket-server](https://github.com/BetaRavener/upy-websocket-server) - MicroPython (ESP8266) WebSocket 服务器实现。
* [micropython-captive-portal](https://github.com/amora-labs/micropython-captive-portal) - MicroPython 的强制门户演示。
* [uPyPortal](https://github.com/lemariva/uPyPortal) - 使用 ESP32 (Wemos) 的 MicroPython 强制门户。
* [ESP8266WebServer](https://github.com/codemee/ESP8266WebServer) - 适用于 MicroPython 的 ESP8266 Web 服务器。
* [microCoAPy](https://github.com/insighio/microCoAPy) - CoAP（约束应用协议）在 MicroPython 中的迷你客户端/服务器实现。
* [micropyserver](https://github.com/troublegum/micropyserver) - MicroPyServer 是一个用于 MicroPython 项目的简单 HTTP 服务器。
* [MicroRESTCli](https://github.com/jczic/MicroRESTCli) - 基于 MicroWebCli for MicroPython 的微型 JSON REST Web 客户端（用于 Pycom 模块和 ESP32）。
* [micropython-noggin](https://github.com/larsks/micropython-noggin) - 一个非常简单的 MicroPython Web 服务器。
* [uwebsockets](https://github.com/danni/uwebsockets) - ESP8266 的 MicroPython WebSocket 实现。
* [microdot](https://github.com/miguelgrinberg/microdot) - MicroPython 的超小型 Web 框架。
* [micropython-nanoweb](https://github.com/hugokernel/micropython-nanoweb) - 完全异步 MicroPython Web 服务器，内存占用小。
* [MicroWebCli](https://github.com/jczic/MicroWebCli) - 适用于 MicroPython 的微型 HTTP Web 客户端（用于 Pycom 模块和 ESP32）。
* [micropython-configserver](https://github.com/carstenblt/micropython-configserver) - MicroPython 的强制门户包括一个哑 DNS 服务器和一个用于配置 WiFi 网络的 Web 服务器。
* [micropython-aioweb](https://github.com/wybiral/micropython-aioweb) - 适用于 MicroPython 的简约异步 Web 框架。
* [thimble](https://github.com/DavesCodeMusings/thimble) - MicroPython 的小型 Web 框架。
* [CaptiveWebServer](https://github.com/joewez/CaptiveWebServer) - 简单的 MicroPython Web 服务器，用于从强制门户为网站提供服务。
* [micropython-urouter](https://github.com/majoson-chen/micropython-urouter) - 一个基于MicroPython的轻量级HTTP请求路由处理支持库。以前的名字叫微路由。
* [wlan-relays](https://github.com/oliver-joos/wlan-relays) - 用 MicroPython 编写的非常简单的 HTTP 服务器，用于控制 ESP32 板的引脚。
* [micropidash](https://github.com/kritishmohapatra/micropidash) - 简单的 Web 仪表板直接由 MicroPython 板（ESP32、Pico W）提供服务。
* [microsky](https://github.com/nakagami/microsky) - 适用于 Python 和 MicroPython 的 [Bluesky](https://bsky.app/) 客户端。

#### 无线网络

* [HueBridge](https://github.com/FRC4564/HueBridge) - 飞利浦色调桥。
* [micropython-wifimanager](https://github.com/mitchins/micropython-wifimanager) - ESP8266 板上 MicroPython 的简单网络配置实用程序。
* [WiFiManager](https://github.com/tayfunulu/WiFiManager) - 适用于 ESP8266 - ESP12 - ESP32 - MicroPython 的 WiFi 管理器。
* [Micropython-ESP-WiFi-Manager](https://github.com/brainelectronics/Micropython-ESP-WiFi-Manager) - WiFi 管理器用于配置和连接到网络。
* [mpy-wpa_supplicant](https://github.com/Carglglz/mpy-wpa_supplicant) - MicroPython 模块用于连接到最近的已知 Wifi AP。
* [micropython-wifi_manager](https://github.com/ferreira-igor/micropython-wifi_manager) - 使用 MicroPython 的 ESP8266 和 ESP32 WiFi 管理器。

#### 紫蜂

* [ZbPy](https://github.com/osresearch/ZbPy) - MicroPython IEEE802.15.4 / Zigbee 解析器。

### 密码学

#### 历史

* [enigmapython](https://github.com/denismaggior8/micropython-enigma-python) - 一个简单但可靠的库，用于使用 MicroPython 模拟不同的 Enigma 机器模型。

### 显示

#### 电子纸

* [micropython-ili9341](https://github.com/mcauser/deshipu-micropython-ili9341) - SSD1606 有源矩阵电子纸显示屏 128x180。
* [micropython-waveshare-epaper](https://github.com/mcauser/micropython-waveshare-epaper) - 各种 Waveshare ePaper 模块的驱动程序。
* [micropython-waveshare-epd](https://github.com/ayoy/micropython-waveshare-epd) - Waveshare ePaper Display 驱动程序，适用于运行 Pycom 风格的 MicroPython 的设备。
* [ssd1675a](https://github.com/mattytrentini/ssd1675a) - 基于 SSD1675 的电子纸显示器的驱动程序。
* [Inkplate-micropython](https://github.com/SolderedElectronics/Inkplate-micropython) - Inkplate 板的 MicroPython 驱动程序。
* [micropython-inkplate6](https://github.com/tve/micropython-inkplate6) - 适用于 Inkplate 6 的 MicroPython 驱动程序。
* [eInk-micropython](https://github.com/dhallgb/eInk-micropython) - MicroPython 上适用于 Waveshare 4.3 英寸设备的电子墨水库。
* [eink](https://github.com/chevdor/eink) - 适用于 MicroPython 和 ESP32 的电子墨水、电子纸显示驱动程序。
* [micropython_DEPG0213BN](https://github.com/Inqbus/micropython_DEPG0213BN) - 适用于 TTGO T5 V2.3 ESP32 板上 DEPG0213BN 电子墨水显示屏的纯 MicroPython 驱动程序。
* [uPyEINK](https://github.com/lemariva/uPyEINK) - 使用运行 MicroPython 的 ESP32 控制 Waveshare 7.5" E-INK 显示器。
* [MicroPython-2.9-inch-ePaper-Library](https://github.com/rdagger/MicroPython-2.9-inch-ePaper-Library) - 用于 WaveShare 2.9 英寸电子纸显示器的 MicroPython 显示驱动程序 (B)。
* [uc8151_micropython](https://github.com/antirez/uc8151_micropython) - UC8151 / IL0373 MicroPython 电子纸显示驱动程序，支持灰度和快速更新。

#### 字体

* [micropython-font-to-py](https://github.com/peterhinch/micropython-font-to-py) - 一个 Python 3 实用程序，用于将字体转换为能够冻结为字节码的 Python 源代码。
* [writer](https://github.com/peterhinch/micropython-font-to-py/blob/master/writer/WRITER.md) - 渲染上述 Python 字体以显示其驱动程序是“framebuf”子类的简单方法。
* [ssd1306big](https://github.com/nickpmulder/ssd1306big) - 128x64 像素 SSD1306 OLED 显示屏上的 MicroPython 字体。
* [framebuf2](https://github.com/peter-l5/framebuf2) - MicroPython FrameBuffer 扩展：更大且旋转的字体、三角形和圆形。
* [micropython_GT30L24T3Y_big5_font](https://github.com/alankrantas/micropython_GT30L24T3Y_big5_font) - MicroPython驱动程序，用于从GT30L24T3Y / ER3303-1 SPI模块读取BIG-5汉字。
* [ttgo-hershey-fonts](https://github.com/russhughes/ttgo-hershey-fonts) - 适用于 TTGO-LCD 板的 MicroPython Hershey 字体演示。
* [packed-font](https://github.com/mark-gladding/packed-font) - 适用于 Pico Pi 和 SSD1306 OLED 显示屏的内存高效 MicroPython 字体。
* [microfont](https://github.com/antirez/microfont) - MicroPython 帧缓冲区的文本绘制库。

#### 图形

* [micropython-stage](https://github.com/python-ugame/micropython-stage) - Stage 游戏库的 MicroPython 端口。
* [micropython-png](https://github.com/Ratfink/micropython-png) - PyPNG 的衍生版本，可与 MicroPython 一起使用。
* [mpy-img-decoder](https://github.com/remixer-dec/mpy-img-decoder) - 纯 MicroPython 中的 PNG 和 JPEG 解码器/解析器/渲染器。
* [micropython-oled-progressbars](https://github.com/follower46/micropython-oled-progressbars) - 与 OLED 显示屏上的 ESP8266 和 ESP32 配合使用的进度条集合。
* [microplot](https://github.com/romilly/microplot) - 简单的 MicroPython 绘图包。
* [micropython-microbmp](https://github.com/jacklinquan/micropython-microbmp) - 用于 BMP 图像处理的小型 Python 模块。
* [MicroPython_UPLOT](https://github.com/jposada202020/MicroPython_UPLOT) - MicroPython 小型图形框架。
* [Tempe](https://github.com/unital/tempe) - 构建在“framebuf”之上的高效 MicroPython 图形库。
* [mp_jpeg](https://github.com/cnadler86/mp_jpeg) - 适用于 ESP32 的非常快速的 MicroPython JPEG 编码器和解码器。

#### 图形用户界面

* [lvgl](https://github.com/lvgl/lv_binding_micropython) - 具有 MicroPython 绑定的面向对象、基于组件的高级 GUI 库。
* [micropython-lcd160cr-gui](https://github.com/peterhinch/micropython-lcd160cr-gui) - 适用于 Pyboard 和 LCD160CR 彩色显示屏的简单触摸驱动事件 GUI。
* [micropython_ra8875](https://github.com/peterhinch/micropython_ra8875) - 用于基于 RA8875 的显示器的 MicroPython 设备驱动程序和 nano-GUI。
* [micropython-nano-gui](https://github.com/peterhinch/micropython-nano-gui) - 一个小型的仅显示 GUI，具有一组有限的 GUI 对象（小部件），用于显示驱动程序是“framebuf”类的子类的显示器。具有 TFT、电子纸和 OLED 显示器的驱动程序。
* [micro-gui](https://github.com/peterhinch/micropython-micro-gui) - 源自 nano-gui 并支持相同的显示器和主机，它通过按钮或导航操纵杆和可选的旋转编码器提供用户输入。
* [micropython-touch](https://github.com/peterhinch/micropython-touch) - 源自 nano-gui 并支持相同的显示器和主机，它提供触摸输入。支持各种触摸控制器。
* [TFT-GUI](https://github.com/peterhinch/micropython-tft-gui) - 适用于大型显示器的快速触摸 GUI，基于 SSD1963 控制器和 XPT2046 触摸控制器。
* [micropython-nextion](https://github.com/brainelectronics/micropython-nextion) - 使用 MicroPython 控制 Nextion 显示。
* [mp_lvgl_widgets](https://github.com/kdschlosser/mp_lvgl_widgets) - LVGL 的 MicroPython 端口的小部件。
* [micropython-core2](https://github.com/lemariva/micropython-core2) - 使用 MPU6886、ILI9342C、BM8563 和 AXP192 驱动程序扩展适用于 M5Stack CORE2 的 LV-MicroPython。

#### 液晶字符

* [Grove_RGB_LCD](https://github.com/dda/MicroPython/blob/master/Grove_RGB_LCD.py) - SeeedStudio Grove RGB LCD 的驱动程序。
* [lcdi2c](https://github.com/slothyrulez/lcdi2c) - 适用于 HD44780 兼容点阵 LCD 的驱动程序。
* [micropython-charlcd](https://github.com/rdagger/micropython-charlcd) - HD44780 兼容 LCD 的驱动程序。
* [micropython-i2c-lcd](https://github.com/Bucknalla/micropython-i2c-lcd) - I2C 2x16 LCD 屏幕驱动程序。
* [pyboard-LCD-character-display](https://github.com/scitoast/pyboard-LCD-character-display) - 适用于 HDD44780 兼容 1602 LCD 的 Pyboar 驱动程序。
* [python_lcd](https://github.com/dhylands/python_lcd) - 适用于 HD44780 兼容点阵 LCD 的驱动程序。
* [micropython-lcd](https://github.com/wjdp/micropython-lcd) - 用于从 MicroPython Pyboard 控制 HD44780 的类。
* [HD44780-lcd-upy](https://gitlab.com/rafalosa/HD44780-lcd-upy) - 用于控制通用 HD44780 LCD 的 MicroPython 模块。
* [LCM1602-14_LCD_Library](https://github.com/Bhavithiran97/LCM1602-14_LCD_Library) - AIP31068L [3.3 V I2C 和 SPI 1602 串行字符 LCD](https://www.cytron.io/p-3v3-i2c-and-spi-1602-serial-character-lcd) 的驱动程序。
* [micropython-i2c-lcd](https://github.com/brainelectronics/micropython-i2c-lcd) - MicroPython 包通过 I2C 控制 HD44780 LCD 显示器 1602 和 2004。
* [micropython_i2c_lcd](https://github.com/Thomascountz/micropython_i2c_lcd) - MicroPython 库，用于通过 PCF8574 I/O 扩展器与基于 HD44780 的 LCD 显示器进行交互。它为 LCD 控制提供高级 API，包括文本显示、光标操作和背光设置，同时还提供对 PCF8574 上 GPIO 操作的低级访问。

#### 液晶图形

* [micropython-lcd-AQM1248A](https://github.com/forester3/micropython-lcd-AQM1248A) - 用于 AQM1248A 图形 LCD 的 ESP8266 驱动程序。
* [micropython-pcd8544](https://github.com/mcauser/micropython-pcd8544) - 适用于诺基亚 5110 PCD8544 84x48 LCD 模块的驱动程序。
* [micropython-st7565](https://github.com/nquest/micropython-st7565) - ST7565 128x64 LCD 驱动程序。
* [micropython-st7920](https://github.com/ShrimpingIt/micropython-st7920) - 使用 ESP8266 和 SPI 在 ST7920 128x64 单色 LCD 面板上使用简单图形基元的库。
* [MicroPython_PCD8544](https://github.com/AnthonyKNorman/MicroPython_PCD8544) - 适用于诺基亚 5110 PCD8544 的 ESP8266 驱动程序。
* [Official LCD160CR](https://github.com/micropython/micropython-lib/tree/master/micropython/drivers/display/lcd160cr) - 带电阻式触摸传感器的官方 MicroPython LCD160CR 显示屏的驱动程序。
* [micropython-hx1230](https://github.com/mcauser/micropython-hx1230) - 适用于 HX1230 96x68 LCD 模块的 MicroPython 库。
* [micropython-SHARP_Memory_Display](https://github.com/pramasoul/micropython-SHARP_Memory_Display) - 用于 SHARP 内存显示的 MicroPython 驱动程序。

#### 液晶显示屏

* [micropython-ili9341](https://github.com/mcauser/deshipu-micropython-ili9341) - TFT 显示器、ILI9341、SH1106、SSD1606、ST7735 的驱动程序集合。
* [micropython-ili934x](https://github.com/tuupola/micropython-ili934x) - 用于基于 ILI934X 系列的 TFT/LCD 显示器的 SPI 驱动程序。
* [MicroPython-ST7735](https://github.com/boochow/MicroPython-ST7735) - GuyCarvers 的 ST7735 TFT LCD 驱动器的 ESP32 版本。
* [micropython-st7735](https://github.com/hosaka/micropython-st7735) - ST7735 TFT LCD 驱动程序。
* [MicroPython_ST7735](https://github.com/AnthonyKNorman/MicroPython_ST7735) - ST7735 128x128 TFT 驱动程序。
* [SSD1963-TFT-Library-for-PyBoard-and-RP2040](https://github.com/robert-hh/SSD1963-TFT-Library-for-PyBoard-and-RP2040) - 适用于 Pyboard 和 Raspberry Pi Pico 的 SSD1963 TFT 库。
* [micropython-ili9341](https://github.com/rdagger/micropython-ili9341) - MicroPython ILI9341 显示屏和 XPT2046 触摸屏驱动程序。
* [st7789_mpy](https://github.com/devbis/st7789_mpy) - 适用于 MicroPython 的快速纯 C 驱动程序，可处理 ST7789 芯片上的显示模块。
* [st7789py_mpy](https://github.com/devbis/st7789py_mpy) - 来自 AliExpress 的慢速 MicroPython 驱动程序，适用于 240x240 ST7789 显示屏，不带 CS 引脚，用 MicroPython 编写。
* [micropython-ili9341](https://github.com/jeffmer/micropython-ili9341) - 用于 ILI9341 显示器的 MicroPython 驱动程序。
* [micropython-ili9341](https://github.com/tkurbad/micropython-ili9341) - 适用于 ESP32 上 MicroPython 的 ILI9341 TFT 驱动程序。
* [st7789_mpy](https://github.com/russhughes/st7789_mpy) - 用 C 语言编写的用于 ST7789 显示模块的快速 MicroPython 驱动程序。
* [st7789py_mpy](https://github.com/russhughes/st7789py_mpy) - 用 MicroPython 编写的 320x240、240x240 和 135x240 ST7789 显示器驱动程序。
* [ili9342c_mpy](https://github.com/russhughes/ili9342c_mpy) - ILI9342C 适用于 MicroPython（M5Stack 核心）的快速“C”驱动程序。
* [gc9a01py](https://github.com/russhughes/gc9a01py) - GC9A01 MicroPython 中的显示驱动程序。
* [gc9a01_mpy](https://github.com/russhughes/gc9a01_mpy) - 用 C 编写的用于 GC9A01 显示模块的快速 MicroPython 驱动程序。
* [st7735-esp8266-micropython](https://github.com/cheungbx/st7735-esp8266-micropython) - 适用于 ST7735 160x80、128x128、128x160 TFT LCD 显示屏的 ESP8266 MicroPython 库。
* [TTGO-ST7789-MicroPython](https://github.com/schumixmd/TTGO-ST7789-MicroPython) - 适用于 TTGO T-Display ESP32 CP2104 WiFi 蓝牙模块 1.14 英寸 LCD 的 MicroPython ST7789 显示驱动程序。
* [st7735_micropython](https://github.com/cheungbx/st7735_micropython) - 适用于 ESP8266 的 80x160、128x128、128x160 的 ST7735 MicroPython 驱动程序。
* [ili934x-micropython](https://gitlab.com/mhepp63/ili934x-micropython) - 用于通过 MicroPython 使用 ILI9341 显示驱动程序的库。
* [micropython-st7735-esp8266](https://gitlab.com/mo_krauti/micropython-st7735-esp8266) - 适用于 ESP8266 上 ST7735 TFT 显示屏的 MicroPython 驱动程序。
* [st7789s3_esp_lcd](https://github.com/russhughes/st7789s3_esp_lcd) - 基于快速 ESP_LCD 的 MicroPython 驱动程序，适用于用 C 编写的 TTGO T-Display-S3 st7789 显示屏。
* [s3lcd](https://github.com/russhughes/s3lcd) - 基于 ESP_LCD 的 MicroPython 驱动程序，适用于带有 ST7789 或兼容显示器的 ESP32-S3 设备。
* [thmi_py](https://github.com/russhughes/thmi_py) - 用 Python 编写的用于 LILYGO T-HMI 的 MicroPython 显示驱动程序。
* [wt32sc01py](https://github.com/russhughes/wt32sc01py) - WT32SC01 Plus MicroPython 显示驱动程序。
* [st7789s3_mpy](https://github.com/russhughes/st7789s3_mpy) - 用 C 语言编写的适用于 TTGO T-Display-S3 ST7789 的 MicroPython 显示驱动程序。
* [t-display-s3](https://github.com/russhughes/t-display-s3) - 用 Python 编写的用于 TTGO T-Display-S3 ST7789 的 MicroPython 显示驱动程序。
* [mp-ili9341](https://github.com/tkurbad/mp-ili9341) - 适用于 ILI9341 TFT 显示屏的 MicroPython 驱动程序。
* [lvgl_esp32_gc9a01](https://github.com/minyiky/lvgl_esp32_gc9a01) - 使用 GC901 驱动程序与 LVGL MicroPython 配合使用的显示器驱动程序。
* [ST77xx-pure-MP](https://github.com/antirez/ST77xx-pure-MP) - 适用于 ST77xx 显示器的纯 MicroPython 驱动程序。内存要求低。
* [upy-st7789](https://github.com/OneMadGypsy/upy-st7789) - 用 MicroPython 编写的简单 ST7789 驱动程序。

#### LED矩阵

* [micropython-ht1632c](https://github.com/vrialland/micropython-ht1632c) - HT1632C 32x16 双色 LED 矩阵驱动器。
* [micropython-matrix8x8](https://github.com/JanBednarik/micropython-matrix8x8) - 带 HT16K33 背包的 Adafruit 8x8 LED 矩阵显示屏驱动程序。
* [micropython-max7219](https://github.com/mcauser/micropython-max7219) - MAX7219 8x8 LED 矩阵模块的驱动器。
* [micropython-wemos-led-matrix-shield](https://github.com/mattytrentini/micropython-wemos-led-matrix) - Wemos D1 Mini Matrix LED 屏蔽驱动器，采用 TM1640 芯片。
* [micropython-max7219](https://github.com/vrialland/micropython-max7219) - 适用于 MAX7219 8x8 LED 矩阵的 MicroPython 驱动程序。
* [MatrixDisplay](https://github.com/octaprog7/MatrixDisplay) - MicroPython 模块适用于 MAX7219 LED 矩阵 8x8 显示屏。
* [LED_panel_upy](https://github.com/CatMeowByte/LED_panel_upy) - 适用于 Panel P10 32x16 矩阵显示器及其变体的 MicroPython 驱动程序模块。

#### LED段

* [LKM1638](https://github.com/arikb/LKM1638) - 基于TM1638控制器的JY-LKM1638显示器驱动程序。
* [max7219_8digit](https://github.com/pdwerryhouse/max7219_8digit) - MAX7219 8 位 7 段 LED 模块的驱动器。
* [micropython-max7219](https://github.com/JulienBacquart/micropython-max7219) - MAX7219 8 位 7 段 LED 模块的驱动器。
* [micropython-my9221](https://github.com/mcauser/micropython-my9221) - MY9221 10 段 LED 条形图模块的驱动器。
* [micropython-tm1637](https://github.com/mcauser/micropython-tm1637) - TM1637 四路 7 段 LED 模块的驱动器。
* [micropython-tm1638](https://github.com/mcauser/micropython-tm1638) - 带开关的 TM1638 双四 7 段 LED 模块驱动器。
* [micropython-tm1640](https://github.com/mcauser/micropython-tm1640) - TM1740 8x8 LED 矩阵模块的驱动器。
* [micropython-tm1640](https://gitlab.com/robhamerling/micropython-tm1640) - MicroPython 库，用于由 TM1640 控制的 16 位 7 段显示器。
* [TM74HC595](https://github.com/Sakartu/TM74HC595) - 用于移位寄存器控制的 5 针显示模块的驱动器。
* [micropython-tm1638spi](https://gitlab.com/robhamerling/micropython-tm1638spi) - 适用于流行板的 MicroPython 库，具有 8 个 7 段数字、8 个独立 LED 和 8 个由 TM1638 控制的按钮。
* [micropython-hpdl1414](https://github.com/rdagger/micropython-hpdl1414) - MicroPython HPDL-1414 显示驱动程序。
* [micropython-sevenseg](https://github.com/kritishmohapatra/micropython-sevenseg) - 用于单位数 7 段显示器（共阳极和阴极）的轻量级 MicroPython 库，支持 ESP32、ESP8266 和 RP2040。
* [max7219_8digit](https://github.com/GM-Script-Writer-62850/max7219_8digit) - 用于带有 8 x 7 段显示屏的 MAX7219 的 MicroPython 驱动程序。

#### LED

* [micropython-morsecode](https://github.com/mampersat/micropython-morsecode) - LED 闪烁并显示摩尔斯电码信息。
* [micropython-p9813](https://github.com/mcauser/micropython-p9813) - SeeedStudio 的 Grove 可链接 RGB LED 中使用的 P9813 RGB LED 驱动器。
* [micropython-ws2812-7seg](https://github.com/HubertD/micropython-ws2812-7seg) - 使用 WS2812 RGB LED 的 7 段显示器。
* [micropython-ws2812](https://github.com/JanBednarik/micropython-ws2812) - WS2812 RGB LED 驱动器。
* [Official APA102](https://docs.micropython.org/en/latest/esp8266/quickref.html#apa102-driver) - ESP8266 APA102/DotStar RGB LED 驱动器。
* [Official WS2811](https://docs.micropython.org/en/latest/esp8266/quickref.html#neopixel-driver) - ESP8266 WS2811/NeoPixel RGB LED 驱动器。
* [tlc5940-micropython](https://github.com/oysols/tlc5940-micropython) - TLC5940 16 通道 LED 驱动器的驱动器。
* [ws2812-SPI](https://github.com/nickovs/ws2812-SPI) - 高效的 MicroPython WS2812 (NeoPixel) 驱动程序。
* [micropython-ws2801](https://github.com/HeMan/micropython-ws2801) - 用于与 WS2801 RGB LED 串连接的 MicroPython 库。
* [tlc5947-rgb-micropython](https://gitlab.com/peterzuger/tlc5947-rgb-micropython) - TLC5947 24 通道 12 位 PWM LED 驱动器的驱动器。
* [micropython-ht16k33](https://github.com/hybotix/micropython-ht16k33) - 适用于 HT16K33 的 MicroPython 驱动程序，这是一款 LED 矩阵、7 段数字和 14 段字母数字显示驱动器 IC。
* [micropython-rgbled](https://github.com/Warringer/micropython-rgbled) - 该包装器模块旨在减少使用 NeoPixel (WS2812) 和 DotStar (APA102) RGB LED 灯条和矩阵所需的工作。
* [micropython_fastled](https://github.com/kdschlosser/micropython_fastled) - FastLED 到 MicroPython 的移植。
* [micropython-rgb-led-driver](https://gitlab.com/Athanaze/micropython-rgb-led-driver) - 用于通过 PWM 控制 RGB LED 的微型驱动器。
* [micropython-dotstar](https://github.com/mattytrentini/micropython-dotstar) - Adafruit CircuitPython APA102/DotStar 库的 MicroPython 端口。
* [micropython-aw210xx](https://github.com/eosti/micropython-aw210xx) - 适用于 Awinic AW210xx 系列 8 位 LED 驱动器的驱动器。
* [IS31FL3197](https://github.com/omeErik/IS31FL3197) - IS31FL3197 芯片的 I2C 驱动程序，可在 Arduino GIGA Display Shield 上找到。

#### 有机发光二极管

* [Grove_OLED](https://github.com/dda/MicroPython/blob/master/Grove_OLED.py) - SeeedStudio 的 Grove OLED 显示屏 1.12" v1.0 使用的 SSD1327 驱动程序。
* [micropython-oled](https://github.com/mcauser/deshipu-micropython-oled) - 适用于单色 OLED 显示器、PCD8544、SH1106、SSD1306、UC1701X 的驱动程序集合。
* [micropython-ssd1327](https://github.com/mcauser/micropython-ssd1327) - SSD1327 128x128 4 位灰度 OLED 显示器的驱动程序。
* [micropython-ssd1351](https://github.com/rdagger/micropython-ssd1351) - SSD1351 OLED 显示器的驱动程序。
* [MicroPython_SSD1306](https://github.com/AnthonyKNorman/MicroPython_SSD1306) - 适用于 SSD1306 OLED 128x64 显示屏的 ESP8266 驱动程序。
* [Official SSD1306](https://github.com/micropython/micropython-lib/tree/master/micropython/drivers/display/ssd1306) - SSD1306 128x64 OLED 显示器的驱动程序。
* [SH1106](https://github.com/robert-hh/SH1106) - SH1106 OLED 显示屏的驱动程序。
* [micropython-ssd1309](https://github.com/rdagger/micropython-ssd1309) - MicroPython SSD1309 单色 OLED 显示驱动器。
* [sh1107-micropython](https://github.com/nemart69/sh1107-micropython) - 用于基于 SH1107 的 OLED 显示屏 (64x128) 的 MicroPython 驱动程序。
* [SH1107](https://github.com/peter-l5/SH1107) - SH1107 OLED 显示器（128x128 和 128x64 像素）的驱动程序。
* [micropython-ssd1322](https://github.com/rdagger/micropython-ssd1322) - 适用于 SSD1322 灰度 OLED 的 MicroPython 显示驱动程序。
* [micropython-ssd1306](https://github.com/rdagger/micropython-ssd1306) - 适用于 SSD1306 单色 OLED 的 MicroPython SPI 和 I2C 显示驱动程序。

#### 打印机

* [micropython-thermal-printer](https://github.com/ayoy/micropython-thermal-printer) - Adafruit 的 Python 热敏打印机的 MicroPython 端口。

### IO

#### 模数转换器

* [ads1x15](https://github.com/robert-hh/ads1x15) - ADS1015/ADS1115 ADC、I2C 接口的驱动程序。
* [micropython-ads1015](https://github.com/mcauser/deshipu-micropython-ads1015) - ADS1015 12 位和 ADS1115 16 位 ADC，4 个通道，具有可编程增益，I2C 接口。
* [Micropython_ADS1115](https://github.com/AnthonyKNorman/Micropython_ADS1115) - ADS1115 16 位 ADC，4 通道，具有可编程增益，I2C 接口。
* [ADS7818](https://github.com/robert-hh/ADS7818) - 连接 ADS7818 AD 转换器的 Python 类。
* [micropython-ads1219](https://github.com/miketeachman/micropython-ads1219) - 适用于 Texas Instruments ADS1219 ADC 的 MicroPython 模块。
* [MicroPython-ADC_Cal](https://github.com/matthias-bs/MicroPython-ADC_Cal) - ESP32 ADC 驱动器使用来自 efuse 的参考电压校准值。
* [micropython-pcf8591](https://gitlab.com/cediddi/micropython-pcf8591) - 适用于 PCF8591 ADC/DAC、I2C 接口的 MicroPython 驱动程序。
* [MCP342x_LoPy](https://github.com/jajberni/MCP342x_LoPy) - 适用于 MCP342x ADC 的 MicroPython 驱动程序。
* [micropython-ads1220](https://github.com/rdagger/micropython-ads1220) - 适用于 ADS1220 24 位模数转换器的 MicroPython 库。
* [PCF8591_micropython_library](https://github.com/xreef/PCF8591_micropython_library) - 适用于 PCF8591 8 位 ADC/DAC 的 MicroPython 库。
* [CS1237](https://github.com/robert-hh/CS1237) - CS1237 ADC 的 MicroPython 驱动程序。
* [ads1115](https://github.com/octaprog7/ads1115) - MicroPython 模块，用于管理 TI 的 ADS1115 多通道差分 I2C ADC。
* [mcp3421](https://github.com/octaprog7/mcp3421) - MicroPython 模块，用于控制带 I2C 接口的 MCP342X 18 位模数转换器。
* [micropython-MCP3001](https://github.com/scruss/micropython-MCP3001) - 用于具有 SPI 接口的 MCP3001 1 通道 10 位 ADC 的 MicroPython 驱动程序。
* [ADS1256](https://github.com/robert-hh/ADS1256) - ADS1256 24 位低噪声 ADC 的驱动程序，既作为通用 MicroPython 版本，又使用 RP2040/RP2350 PIO。

#### 数模转换器

* [micropython-mcp4725](https://github.com/wayoda/micropython-mcp4725) - MCP4725 I2C DAC 驱动程序。
* [mcp4728](https://github.com/openfablab/mcp4728) - Microchip MCP4728 I2C 12 位四路 DAC 的辅助库。
* [mpyDAC](https://github.com/octaprog7/mpyDAC) - MicroPython 模块，用于控制带有 EEPROM 存储器的 MCP4725、12 位数字模拟转换器 (CAP)。

#### 通用输入输出接口

* [micropython-inputs](https://github.com/alanmitchell/micropython-inputs) - 用于对 MicroPython 板进行脉冲计数、数字输入去抖以及计算模拟输入移动平均值的类。
* [ubutton](https://gitlab.com/WiLED-Project/ubutton) - 一个 MicroPython 库，用于控制按钮输入的读取和去抖，包括“短按”和“长按”回调。
* [micropython-debounce-switch](https://github.com/selfhostedhome/micropython-debounce-switch) - 用于去抖开关的 MicroPython 类。

#### IO扩展器

* [micropython-mcp230xx](https://github.com/ShrimpingIt/micropython-mcp230xx) - MCP23017 和 MCP23008 GPIO 扩展器的驱动程序。
* [micropython-mcp230xx](https://codeberg.org/dsiggi/micropython-mcp230xx) - MCP23017 和 MCP23008 GPIO 扩展器的驱动程序，通过中断处理进行扩展。
* [micropython-mcp23017](https://github.com/mcauser/micropython-mcp23017) - 适用于 MCP23017 16 位 I/O 扩展器的 MicroPython 驱动程序。
* [micropython-pcf8574](https://github.com/mcauser/micropython-pcf8574) - 适用于带中断的 PCF8574 8 位 I2C I/O 扩展器的 MicroPython 驱动程序。
* [micropython-pcf8575](https://github.com/mcauser/micropython-pcf8575) - 适用于带中断的 PCF8575 16 位 I2C I/O 扩展器的 MicroPython 驱动程序。
* [ESP8266_MCP23S17](https://github.com/AnthonyKNorman/ESP8266_MCP23S17) - MicroPython 库，用于将 MCP23S17 16 位 I/O 扩展器与 ESP8266 结合使用。
* [pcf8574](https://github.com/octaprog7/pcf8574) - MicroPython 模块，用于与 NXP 的 PCF8574(A) I2C 8 位 I/O 扩展器配合使用。
* [mcp23017](https://github.com/octaprog7/mcp23017) - 适用于 MCP23017 的 MicroPython 模块，带串行接口的 16 位 I/O 扩展器。
* [micropython-sx1509](https://github.com/rdagger/micropython-sx1509) - MicroPython SX1509 I/O 扩展器库。

#### 操纵杆

* [micropython-nunchuck](https://github.com/kfricke/micropython-nunchuck) - Nunchuk 游戏控制器驱动程序，I2C 接口。
* [esp32-microgamepad-ble](https://github.com/insighio/esp32-microgamepad-ble) - 使用 MicroPython 通过 BLE（北欧 UART 服务 - NUS）在 ESP32 上实现双模拟操纵杆。
* [micropython-joystick-2-unit](https://github.com/HowManyOliversAreThere/micropython-joystick-2-unit) - [M5Stack Joystick 2 Unit](https://docs.m5stack.com/en/unit/Unit-JoyStick2) 的驱动程序。
* [Micropython_Joystick](https://github.com/cnadler86/Micropython_Joystick) - 一个简单快速的 ADC 操纵杆库。

#### 键盘

* [micropython-keyboard](https://github.com/mcameron/micropython-keyboard) - 在 MicroPython Pyboard 上运行的 47 键键盘。
* [pico-rgbkeypad](https://github.com/martinohanlon/pico-rgbkeypad) - 用于控制 Raspberry Pi Pico 的 Pimoroni RGB 键盘的 Python 类。
* [micropython-aiobutton](https://github.com/jacklinquan/micropython-aiobutton) - 用于异步按钮的 MicroPython 模块。
* [MicroPython-SimpleKeypad](https://github.com/PerfecXX/MicroPython-SimpleKeypad) - 用于与键盘矩阵连接的 MicroPython 库。

#### 多路复用器

* [micropython-tca9548a](https://github.com/mcauser/micropython-tca9548a) - 使用 TCA9548A I2C 多路复用器的 MicroPython 示例。
* [tca9548a](https://github.com/QuirkyCort/IoTy/blob/main/public/extensions/tca9548a.py) - 适用于 TCA9548A I2C 多路复用器的 MicroPython 驱动程序。

#### 电位器

* [micropython-ad840x](https://codeberg.org/dsiggi/micropython-ad840x) - 基于 MicroPython SPI 的 AD 系列数字电位器 AD8400、AD8402 和 AD8403 操控。
* [mcp4131](https://github.com/scruss/mcp4131) - MicroPython 模块用于控制 MicroChip 的 MCP4131 SPI 数字电位器。
* [MicroPython_DS1841](https://github.com/jposada202020/MicroPython_DS1841) - DS1841 电位计的 MicroPython 驱动程序。
* [MicroPython_DS3502](https://github.com/jposada202020/MicroPython_DS3502) - DS3502 电位计的 MicroPython 驱动程序。

#### 电源管理

* [AXP202_PythonLibrary](https://github.com/lewisxhe/AXP202_PythonLibrary) - MicroPython AXP202 库。
* [micropython_hourly_sleeper_library](https://github.com/costastf/micropython_hourly_sleeper_library) - 一个 MicroPython 库，可让 ESP8266 在设定的小时数内按每小时增量休眠。

#### 脉宽调制

* [upwmcontroller](https://gitlab.com/WiLED-Project/upwmcontroller) - 一个 MicroPython 库，用于控制异步循环中的 PWM 输出，具有淡入淡出和闪烁等功能。

#### 继电器

* [micropython-xl9535-kxv5-relay](https://github.com/mcauser/micropython-xl9535-kxv5-relay) - 适用于 jxl XL9535-KxV5 I2C 继电器板的 MicroPython 库。

#### 旋转编码器

* [micropython-rotary](https://github.com/miketeachman/micropython-rotary) - 用于读取旋转编码器的 MicroPython 模块。
* [uencoder](https://gitlab.com/WiLED-Project/uencoder) - 用于从旋转编码器读取数据的 MicroPython 库。
* [encodermenu](https://github.com/sgall17a/encodermenu) - 使用旋转编码器和基本显示的 MicroPython 的简单 GUI 菜单。
* [encoderLib](https://github.com/BramRausch/encoderLib) - 用于处理旋转编码器的 MicroPython 库。
* [rotary-encoder](https://github.com/gurgleapps/rotary-encoder) - 用于驱动 KY-040 旋转编码器的 MicroPython 代码。
* [micropython-encoder-knob](https://github.com/infinite-tree/micropython-encoder-knob) - 一个非常简单的轻量级编码器旋钮库，带有按钮支持。
* [encoders](https://github.com/peterhinch/micropython-samples/blob/master/encoders/ENCODERS.md) - 解释编码器技术相关问题的简短文档。
* [asynchronous encoder driver](https://github.com/peterhinch/micropython-async/blob/master/v3/primitives/encoder.py) - 将编码器连接到 uasyncio 代码。
* [micropython-8encoder](https://github.com/HowManyOliversAreThere/micropython-8encoder) - I2C [M5Stack 8 编码器单元](https://shop.m5stack.com/products/8-encoder-unit-stm32f030) 驱动程序。
* [micropython-quiic-twist](https://github.com/rdagger/micropython-quiic-twist) - 用于 Quiic Twist RGB 旋转编码器的 MicroPython 驱动程序。
* [AS5600](https://github.com/sgall17a/AS5600) - 用于读取该磁传感器的 AS5600 MicroPython 库。
* [AS5600](https://github.com/octaprog7/AS5600) - 用于控制单圈磁性编码器 AS5600 的 MicroPython 模块。

#### 移位寄存器

* [micropython-74hc595](https://github.com/mcauser/micropython-74hc595) - 适用于 74HC595 8 位移位寄存器的 MicroPython 驱动程序。
* [MicroPython-SN74HCS264](https://gitlab.com/olivierlenoir/MicroPython-SN74HCS264) - 适用于具有施密特触发器输入和反相输出的 SN74HCS264 8 位并行输出串行移位寄存器的 MicroPython 驱动程序。

#### 波形发生器

* [Micropython-AD9833](https://github.com/KipCrossing/Micropython-AD9833) - AD9833的Pyboard驱动程序，SPI接口。
* [Clock_Generators](https://github.com/Wei1234c/Clock_Generators) - 时钟发生器（目前为 Si5351）工具箱。
* [Signal_Generators](https://github.com/Wei1234c/Signal_Generators) - 信号发生器（AD9833、AD9834、AD9850、ADF4351）工具箱。
* [pico-wave-vibration-generator](https://github.com/gurgleapps/pico-wave-vibration-generator) - 适用于 Raspberry Pi Pico 的基于 MicroPython 的频率发生器，旨在在螺线管或扬声器上产生振动，从而实现在家中进行波实验和探索。
* [micropython-m5stack-dds](https://github.com/mattytrentini/micropython-m5stack-dds) - M5Stack DDS 频率发生器的 MicroPython 驱动程序。
* [AD9833-MicroPython-Module](https://github.com/owainm713/AD9833-MicroPython-Module) - MicroPython 模块使用 AD9833 可编程波形发生器。

### 数学

* [uMath](https://github.com/albaEDA/uMath) - 微控制器的计算机代数。
* [micropython-ulab](https://github.com/v923z/micropython-ulab) - 适用于 MicroPython 的类似 NumPy 的快速向量模块。
* [micropython-fourier](https://github.com/peterhinch/micropython-fourier) - MicroPython 内联 ARM 汇编器中的快速傅里叶变换。
* [Filters](https://github.com/peterhinch/micropython-filters) - 使用 ARM Thumb 汇编器的 FIR 滤波器。使用在线实用程序，您可以从所需频率响应图到滤波器实现。
* [ulinalg](https://github.com/jalawson/ulinalg) - 小尺寸矩阵处理模块，具有一些专门针对 MicroPython (Python 3) 的线性代数运算。
* [micropython-mtx](https://gitlab.com/nickoala/micropython-mtx) - MicroPython 上的快速矩阵乘法和线性求解器。
* [micropython-vec](https://gitlab.com/nickoala/micropython-vec) - MicroPython 上的向量运算。
* [MicroPython_Statistics](https://github.com/rcolistete/MicroPython_Statistics) - MicroPython 的统计模块。
* [MicroPython-Matrix](https://gitlab.com/olivierlenoir/MicroPython-Matrix) - MicroPython 基本矩阵运算。
* [uumpy](https://github.com/nickovs/uumpy) - MicroPython 的 NumPy 子集。
* [upyuncertainties](https://github.com/rcolistete/upyuncertainties) - MicroPython 的不确定性计算。
* [umatrix](https://github.com/iyassou/umatrix) - MicroPython 语言的矩阵库。
* [micropython-fractions](https://github.com/mattytrentini/micropython-fractions) - CPython 标准分数库的 MicroPython 端口。
* [Sun and Moon](https://github.com/peterhinch/micropython-samples/blob/master/astronomy/README.md) - 确定太阳和月亮的升起和落下时间以及月相。
* [micropython-npyfile](https://github.com/jonnor/micropython-npyfile/) - Numpy .npy 文件支持 MicroPython，支持读/写/流。
* [Micropython Perlin](https://github.com/sjaak31367/micropython_perlin) - Perlin 噪声发生器模块。

### 运动

* [MicroPython Motor Kit](https://github.com/cnadler86/MicroPython_Motor) - 通用电机控制库。

#### 直流电机

* [MicroPython-L298](https://gitlab.com/olivierlenoir/MicroPython-L298) - 使用 MicroPython 驱动 L298 双 H 桥。
* [pyl298](https://github.com/marcio-pessoa/pyl298) - L298 双全桥电机控制器的驱动器。

#### 伺服

* [micropython-pca9685](https://github.com/mcauser/deshipu-micropython-pca9685) - 16通道12位PWM/伺服驱动器。
* [micropython-servo](https://github.com/redoxcode/micropython-servo) - 使用直接 PWM 输出以简洁的方式控制 RC 伺服系统的库。
* [MicroPython_PCA9685](https://github.com/jposada202020/MicroPython_PCA9685) - PCA9685 PWM 控制 IC 的 MicroPython 驱动程序，通常用于控制伺服系统、LED 和电机。
* [MicroPython_MOTOR](https://github.com/jposada202020/MicroPython_MOTOR) - MicroPython Helper 用于控制基于 PWM 的电机。
* [pca9685](https://github.com/octaprog7/pca9685) - 用于管理 16 通道 SHIM 控制器 PCA9685 的 MicroPython 模块

#### 步进机

* [AccelStepper-MicroPython](https://github.com/pedromneto97/AccelStepper-MicroPython) - 适用于 MicroPython 的 AccelStepper 库 - ESP32。
* [microPython_AMIS-30543](https://github.com/capella-ben/microPython_AMIS-30543) - 使用 AMIS-30543 驱动程序进行步进驱动器控制的 MicroPython 库。
* [microPython_TMC5160](https://github.com/capella-ben/microPython_TMC5160) - 适用于 Trinamic TMC5160 运动控制器的 MicroPython 库。
* [micropython-drv8825](https://gitlab.com/robhamerling/micropython-drv8825) - MicroPython 中的驱动程序和示例，用于通过 DRV8825 控制器板控制步进电机。
* [micropython-multiaxis](https://gitlab.com/olivierlenoir/micropython-multiaxis) - 采用 MicroPython ESP32 和 DRV8825 的多轴。
* [micropython-rp2-smartStepper](https://github.com/bikeNomad/micropython-rp2-smartStepper) - RP2040/RP2350 库使用 PIO 和 DMA 来控制步进电机。
* [micropython-stepper-motor](https://github.com/larsks/micropython-stepper-motor) - 驱动连接到 ULN2003 驱动器的 28BYJ-48 电机。
* [micropython-stepper](https://github.com/redoxcode/micropython-stepper) - 以简洁的方式控制常见步进驱动器的库。
* [micropython-upybbot](https://github.com/jeffmer/micropython-upybbot) - 用于双极步进电机的 A4988 驱动器。
* [pystepper](https://github.com/marcio-pessoa/pystepper) - MicroPython 步进电机顺序控制。
* [ticlib](https://github.com/jphalip/ticlib) - Pololu Tic 步进电机控制器的驱动程序。
* [uln2003](https://github.com/IDWizard/uln2003) - 5V 28BYJ-48 步进电机驱动器。
* [uPySteppers](https://github.com/lemariva/uPySteppers) - 使用连接 WiFi 的 ESP32 DIY 旋转平台。

### 传感器

#### 数字加速度计

* [ADXL345-with-Pyboard](https://github.com/AbhinayBandaru/ADXL345-with-Pyboard) - ADXL345 16g 3 轴加速度计驱动程序。
* [adxl345_micropython](https://github.com/fanday/adxl345_micropython) - ADXL345 16g 3 轴加速度计驱动程序。
* [MicroPython-LIS3DH](https://github.com/tinypico/tinypico-micropython/tree/master/lis3dh%20library) - LIS3DH 3 轴加速度计的 I2C 驱动程序。
* [micropython-lis2hh12](https://github.com/tuupola/micropython-lis2hh12) - LIS2HH12 3 轴加速度计的 I2C 驱动程序。
* [MMA7660](https://github.com/Bucknalla/MicroPython-3-Axis-Accelerometer/blob/master/MMA7660.py) - MMA7660 1.5g 3 轴加速度计驱动程序。
* [ADXL345_spi_micropython](https://github.com/AlekseyFedorovich/ADXL345_spi_micropython) - 用于通过 SPI 协议与来自使用 MicroPython 闪存的 MCU 的“Analog Devices ADXL345”加速度计进行交互的库。
* [MicroPython_ADXL343](https://github.com/jposada202020/MicroPython_ADXL343) - Analog Devices ADXL343 加速度计的 MicroPython 驱动程序。
* [MicroPython_BMA220](https://github.com/jposada202020/MicroPython_BMA220) - 适用于博世 BMA220 加速度计的 MicroPython 驱动程序。
* [MicroPython_BMA400](https://github.com/jposada202020/MicroPython_BMA400) - 适用于博世 BMA400 加速度计的 MicroPython 驱动程序。
* [bma423-pure-mp](https://github.com/antirez/bma423-pure-mp) - 适用于 Bosch 423 加速度计的 MicroPython 驱动程序。包括 FIFO 支持。 ⏩
* [MicroPython_LIS3DH](https://github.com/jposada202020/MicroPython_LIS3DH) - LIS3DH 3 轴加速度计的 MicroPython 驱动程序。
* [MicroPython_KX132](https://github.com/jposada202020/MicroPython_KX132) - 适用于 Kionix KX132 加速度计的 MicroPython 驱动程序。
* [MicroPython_H3LIS200DL](https://github.com/jposada202020/MicroPython_H3LIS200DL) - ST H3LIS200DL 加速度计的 MicroPython 驱动程序。
* [MicroPython_QMC5883L](https://github.com/jposada202020/MicroPython_QMC5883L) - QMC5883L 加速度计的 MicroPython 驱动程序。
* [Micropython_MC3479](https://github.com/jposada202020/Micropython_MC3479) - MC3479 加速度计的 MicroPython 驱动程序。
* [MicroPython_MMA8451](https://github.com/jposada202020/MicroPython_MMA8451) - 适用于 MMA8451 3 轴加速度计的 MicroPython 模块。
* [MicroPython_MMA8452Q](https://github.com/jposada202020/MicroPython_MMA8452Q) - 适用于 NXP MMA8452Q 加速计的 MicroPython 驱动程序。
* [msa301-micropython-driver](https://github.com/wojciech-szmyt/msa301-micropython-driver) - 用于 MSA301 3 轴加速度计的自制 MicroPython 驱动程序。在 Raspberry Pico 上测试。

#### 空气质量

* [CCS811](https://github.com/Ledbelly2142/CCS811) - CCS811 空气质量传感器。
* [upython-aq-monitor](https://github.com/ayoy/upython-aq-monitor) - 使用 PMS5003 传感器和 WiPy 的空气质量监测器。
* [micropython-pms7003](https://github.com/pkucmus/micropython-pms7003) - PMS7003 空气质量传感器的 MicroPython 驱动程序。
* [pms5003_micropython](https://github.com/kevinkk525/pms5003_micropython) - 适用于 MicroPython 的 PMS5003 空气质量传感器驱动程序。
* [micropython-pms5003-minimal](https://github.com/miketeachman/micropython-pms5003-minimal) - MicroPython 的 P 空气质量传感器驱动程序。
* [polly](https://github.com/g-sam/polly) - SDS011污染传感器+Wemos D1 mini pro+MicroPython。
* [micropython-SNGCJA5](https://github.com/aleppax/micropython-SNGCJA5) - 适用于 Panasonic SN-GCJA5 颗粒物 (PM) 传感器的 MicroPython 驱动程序。

#### 气压计 - 气压和水压

* [MicroPython-BMPxxx](https://github.com/bradcar/MicroPython_BMPxxx) - BMP585、BMP581、BMP390、BMP280 博世温度/压力传感器的驱动程序。
* [mp-bmp3xx-full](https://github.com/jornamon/mp-bmp3xx-full) - 适用于博世 BMP3xx 系列气压传感器的 MicroPython 驱动程序。包括 FIFO 支持。 ⏩
* [micropython-bme280](https://github.com/kevbu/micropython-bme280) - Bosch BME280 温度/压力/湿度传感器的驱动程序。
* [micropython-bmp180](https://github.com/micropython-IMU/micropython-bmp180) - Bosch BMP180 温度、压力和高度传感器的驱动程序。
* [mpy_bme280_esp8266](https://github.com/catdog2/mpy_bme280_esp8266) - 博世 BME280 温度/压力/湿度传感器。
* [BME280](https://github.com/robert-hh/BME280) - BME280 传感器的 MicroPython 驱动程序，目标平台 Pycom 设备。
* [ms5803-micropython](https://github.com/minyiky/ms5803-micropython) - MS5803 空气/水压力和温度传感器驱动程序的 MicroPython 实现。
* [MPL3115A2_MicroPython](https://github.com/PinsonJonas/MPL3115A2_MicroPython) - 适用于 MPL3115A2 高度计的 MicroPython 库。
* [D6F-PH](https://github.com/ekspla/D6F-PH) - 用于差压传感器 D6F-PH (OMRON) 的 MicroPython 模块。
* [micropython-bmp280](https://github.com/dafvid/micropython-bmp280) - BMP280 传感器模块。
* [micropython_bme280_i2c](https://github.com/triplepoint/micropython_bme280_i2c) - 用于与 Bosch BME280 温度、湿度和压力传感器通信的 MicroPython 模块。
* [MicroPython-BME280](https://github.com/neliogodoi/MicroPython-BME280) - 温度、压力和湿度数字传​​感器的驱动程序。
* [micropython-bmp180](https://gitlab.com/flowolf/micropython-bmp180) - MicroPython 的模块，为 BMP180 压力传感器提供类。
* [bmp581](https://github.com/octaprog7/bmp581) - 适用于 Bosch Sensortec 的 BMP581 压力和环境温度传感器的 MicroPython 模块。
* [BMP390](https://github.com/octaprog7/BMP390) - 用于 BMP390 压力和温度传感器的 MicroPython 模块。
* [BMP180](https://github.com/octaprog7/BMP180) - 用于 BMP180 压力和温度传感器的 MicroPython 模块。
* [MicroPython_DPS310](https://github.com/jposada202020/MicroPython_DPS310) - DPS310 传感器的 MicroPython 驱动程序。 （已存档）
* [MicroPython_ICP10111](https://github.com/jposada202020/MicroPython_ICP10111) - 用于 TDK ICP-10111 气压和温度传感器的 MicroPython 驱动程序。 （已存档）
* [MicroPython_BMP581](https://github.com/jposada202020/MicroPython_BMP581) - 适用于 Bosch BMP581 压力和温度传感器的 MicroPython 驱动程序。 （已存档）
* [MicroPython_MMR902](https://github.com/jposada202020/MicroPython_MMR902) - 适用于 Mitsumi MMR902 微型压力传感器的 MicroPython 驱动程序。 （已存档）
* [MicroPython_MPL3115A2](https://github.com/jposada202020/MicroPython_MPL3115A2) - 适用于 NXP MPL3115A2 压力和温度传感器的 MicroPython 驱动程序。 （已存档）
* [MicroPython_MS5611](https://github.com/jposada202020/MicroPython_MS5611) - 适用于 TE MS5611 压力和温度传感器的 MicroPython 驱动程序。 （已存档）

#### 电池

* [Micropython-LC709203F](https://github.com/scopelemanuele/Micropython-LC709203F) - 用于 LC709293F 电量计的简单 MicroPython 库。

#### 生物识别

* [micropython-fingerprint](https://github.com/chrisb2/micropython-fingerprint) - 用于读取 Grow 和zhianTec 指纹传感器的 MicroPython 库。
* [MAX30102-MicroPython-driver](https://github.com/n-elia/MAX30102-MicroPython-driver) - 移植到 MicroPython 的 MAX30102 驱动程序。它也应该适用于 MAX30105。
* [max30102](https://github.com/QuirkyCort/IoTy/blob/main/public/extensions/max30102.py) - 适用于 MAX30102 的 MicroPython 驱动程序，具有心跳检测和 BPM 测量功能。

#### 相机

* [micropython-camera-API](https://github.com/cnadler86/micropython-camera-API) - 该项目的目标是支持 MicroPython 中各种端口的摄像头，从 ESP32 端口和 Omnivision 摄像头（OV2640 和 OV5640）开始。
* [micropython-ov2640](https://github.com/namato/micropython-ov2640) - OV2640 相机的 MicroPython 类。
* [Nikon-Trigger-for-MicroPython](https://github.com/Thekegman/Nikon-Trigger-for-MicroPython) - 使用 IR LED 远程触发尼康相机。对于 Pyboard v1.1。
* [micropython-camera-driver](https://github.com/lemariva/micropython-camera-driver) - 适用于 ESP32 上 MicroPython 的 OV2640 摄像头驱动程序。
* [esp32-cam-micropython](https://github.com/shariltumin/esp32-cam-micropython) - MicroPython ESP32-CAM。
* [uPyCam](https://github.com/lemariva/uPyCam) - 使用运行 MicroPython 的 ESP32-CAM 拍照。
* [OV2640_uPy](https://github.com/FunPythonEC/OV2640_uPy) - 适用于 MicroPython 的 OV2640 相机库。
* [MQTT-Cam](https://github.com/jono-allen/MQTT-Cam) - ESP32-CAM MicroPython MQTT AWS S3 上传器。
* [IoTy huskylib](https://github.com/QuirkyCort/IoTy/blob/main/public/extensions/huskylib.py) - 适用于 DFRobot Husky Lens 的 MicroPython 驱动程序。易于使用的AI相机/视觉传感器，具有人脸识别、物体跟踪、物体识别、线路跟踪、颜色识别和二维码识别功能。
* [IoTy mv](https://github.com/QuirkyCort/IoTy/blob/main/public/extensions/mv.py) - 一个简单的机器视觉库，提供斑点和圆形检测。

#### 颜色

* [micropython-tcs34725](https://gitlab.com/robhamerling/micropython-tcs34725) - TCS34725 和 TCS34727 颜色传感器的驱动程序类。
* [micropython-as7341](https://gitlab.com/robhamerling/micropython-as7341) - AS7341 的 MicroPython 库。
* [MicroPython_ISL29125](https://github.com/jposada202020/MicroPython_ISL29125) - Intersil ISL29125 颜色传感器的 MicroPython 驱动程序。
* [TCS3200-MicroPython](https://github.com/uraich/TCS3200-MicroPython) - TCS3200 颜色传感器的 MicroPython 驱动程序和测试程序。
* [MicroPython_TCS3430](https://github.com/jposada202020/MicroPython_TCS3430) - 适用于 AMS TCS3430 颜色和 ALS 传感器的 MicroPython 驱动程序。
* [micropython-gy33](https://github.com/QuirkyCort/micropython-gy33) - GY-33 模块（TCS3472 颜色传感器）的 UART 和 I2C 驱动程序。
* [veml6040](https://github.com/octaprog7/veml6040) - 用于管理 Vishay 颜色传感器 RGBW VEML6040 的 MicroPython 模块。

#### 指南针

* [micropython-esp8266-hmc5883l](https://github.com/gvalkov/micropython-esp8266-hmc5883l) - ESP8266 上的 3 轴数字指南针。
* [QMC5883](https://github.com/robert-hh/QMC5883) - QMC5883 三轴数字罗盘 IC 的 Python 类。
* [microPython_AS5600L](https://github.com/capella-ben/microPython_AS5600L) - 用于 AS5600L 磁铁旋转位置传感器的 MicroPython 驱动程序。
* [QMC5883](https://github.com/octaprog7/QMC5883) - 用于控制 QMC5883L 地磁传感器的 MicroPython 模块。

#### 当前

* [micropythonINA219](https://github.com/kabel42/micropythonINA219) - INA219 电流传感器驱动程序。
* [pyb_ina219](https://github.com/chrisb2/pyb_ina219) - INA219 电流传感器驱动程序。
* [INA219](https://github.com/robert-hh/INA219) - INA219 MicroPython 驱动程序。
* [TI_INA226_micropython](https://github.com/elschopi/TI_INA226_micropython) - 适用于 Texas Instruments INA226 功率测量 IC 的 MicroPython 驱动程序。
* [micropython-current-monitor](https://gitlab.com/n.rj.powers/micropython-current-monitor) - 当前使用 INA219 和 SSD1306 OLED 的监视器。
* [INA_TI](https://github.com/octaprog7/INA_TI) - 用于控制 INA219、INA226 的 MicroPython 模块 - 具有 I2C 接口的双向电流/功率监视器。

#### 距离红外

* [micropython-gp2y0e03](https://github.com/mcauser/deshipu-micropython-gp2y0e03) - IR-LED测距传感器采用Sharp GP2Y0E03。
* [micropython-vl6180](https://github.com/mcauser/deshipu-micropython-vl6180) - 飞行时间传感器、环境光传感器和红外发射器。
* [GP2Y0A21YK](https://github.com/basanovase/GP2Y0A21YK) - GP2Y0A21YK MicroPython 库。

#### 距离激光

* [micropython-vl53l0x](https://github.com/mcauser/deshipu-micropython-vl53l0x) - 飞行时间激光测距传感器。
* [Qwiic_TOF_Module_RFD77402](https://github.com/ZIOCC/Qwiic_TOF_Module_RFD77402) - Qwiic TOF 模块 (RFD77402) 飞行时间测距模块。
* [VL53L0X](https://github.com/uceeatz/VL53L0X) - 适用于 LiDAR 传感器 VL53L0X 的 MicroPython 库。
* [vl53l1x_pico](https://github.com/drakxtwo/vl53l1x_pico) - 适用于 VL53L1X ToF 传感器的 MicroPython 驱动程序。
* [tf-luna-micropython](https://github.com/davmoz/tf-luna-micropython) - 用于 TF-Luna LiDAR 模块的简单 MicroPython I2C 库。
* [vl53l5cx](https://github.com/mp-extras/vl53l5cx) - 适用于 [VL53L5CX](https://www.st.com/en/imaging-and-photonics-solutions/vl53l5cx.html)（4x4/8x8 ToF 传感器阵列）的 MicroPython 和 CircuitPython 软件包。
* [VL6180X](https://github.com/Ledbelly2142/VL6180X) - 适用于 ESP32 上 VL6180X 传感器的 MicroPython 驱动程序。
* [LidarLight_v3HP_micropython](https://github.com/Dnapert/LidarLight_v3HP_micropython) - 适用于 Garmin Lidar Lite v3HP 的 MicroPython 库。
* [vl53l1x](https://github.com/QuirkyCort/IoTy/blob/main/public/extensions/vl53l1x.py) - 适用于 VL53L1X ToF 传感器的 MicroPython 驱动程序。
* [vl53l0x-nb](https://github.com/antirez/vl53l0x-nb) - vl53l0x TOF 传感器的 MicroPython 驱动程序的分支，以添加非阻塞模式。
* [IoTy lds02rr](https://github.com/QuirkyCort/IoTy/blob/main/public/extensions/lds02rr.py) - LDS02RR 360 度 LiDAR 驱动器。
* [IoTy coind4](https://github.com/QuirkyCort/IoTy/blob/main/public/extensions/coind4.py) - COIN-D4 360 度 LiDAR 驱动程序。
* [IoTy delta2d](https://github.com/QuirkyCort/IoTy/blob/main/public/extensions/delta2d.py) - Delta-2D 360 度 LiDAR 驱动程序。

#### 远距离超声波

* [micropython-hcsr04](https://github.com/rsc1975/micropython-hcsr04) - HC-SR04超声波距离传感器驱动程序。
* [micropython-us100](https://github.com/kfricke/micropython-us100) - US-100 声纳距离传感器的 MicroPython 驱动程序。
* [micropython-i2c-ultrasonic](https://github.com/HowManyOliversAreThere/micropython-i2c-ultrasonic) - 用于基于 RCWL-9620 的 M5 I2C 超声波距离单元的 MicroPython 驱动程序。
* [micropython-grove-ultrasonic-ranger](https://github.com/mores/TheMissingLink/tree/main/Seeed_MicroPython_UltrasonicRanger) - SeeedStudio 的 Grove 超声波测距仪的驱动程序。

#### 灰尘

* [pyGP2Y](https://github.com/amigcamel/pyGP2Y) - 适用于 Sharp GP2Y1014AU0F 灰尘传感器的 MicroPython 库。

#### 能源

* [ATM90E26_Micropython](https://github.com/whatnick/ATM90E26_Micropython) - ATM90E26电能计量装置的驱动程序。
* [MCP39F521](https://github.com/warpme/MCP39F521) - 用于读取 MCP39F521 功率监视器的 ESP8266 脚本。
* [micropython-p1meter](https://github.com/Josverl/micropython-p1meter) - 一个 ESP32 传感器，用于读取 p1 电表并将其发布到 MQTT 和 Home Assistant，用 MicroPython 编写。
* [esp32-solar2](https://github.com/octopusengine/esp32-solar2) - 简单的太阳能调节器 - MicroPython 项目。
* [cs5490_micropython](https://github.com/whatnick/cs5490_micropython) - 用于 CS5490 能量监控器 IC 的 MicroPython 驱动程序。

#### 气态

* [micropython-MQ](https://github.com/kartun83/micropython-MQ) - MQ 系列气体传感器驱动程序。
* [MQ135](https://github.com/rubfi/MQ135) - MQ135气体传感器驱动程序。
* [CCS811](https://github.com/Notthemarsian/CCS811) - ESP8266 板上 CCS811 的基本 MicroPython 驱动程序。
* [micropython-scd30](https://github.com/agners/micropython-scd30) - 适用于 Sensirion SCD30 CO2 传感器模块的 MicroPython I2C 驱动程序。
* [MicroPython_SCD4X](https://github.com/peter-l5/MicroPython_SCD4X) - 适用于 Sensirion SCD40 和 SCD41 CO2 传感器的 MicroPython I2C 驱动程序。
* [micropython-sgp40](https://github.com/agners/micropython-sgp40) - 适用于 SGP40 VOC 传感器模块的 MicroPython I2C 驱动程序。
* [MICS6814-Micropython-driver](https://gitlab.com/DanNduati/MICS6814-Micropython-driver) - 适用于 Pimoroni MICS6814 分线板的 ESP32 MicroPython 驱动程序。
* [MicroPython_AGS02MA](https://github.com/jposada202020/MicroPython_AGS02MA) - AGS02MA TVOC 传感器的 MicroPython 驱动程序。
* [SCD4x](https://github.com/octaprog7/SCD4x) - MicroPython 模块可与 Sensirion 的 SCD4x（SCD40、SCD41）低功耗 CO2、温度和湿度电声传感器配合使用。
* [ens160](https://github.com/octaprog7/ens160) - MicroPython 模块可与 ENS160 数字金属氧化物多种气体传感器配合使用。

#### 人类存在

* [ld2410](https://github.com/QuirkyCort/IoTy/blob/main/public/extensions/ld2410.py) - 24GHz人体存在感应模块，能够检测移动和静止目标，并提供大致范围。

#### 湿度

* [MicroPython_HTS221](https://github.com/jposada202020/MicroPython_HTS221) - HTS221 湿度传感器的 MicroPython 驱动程序。

#### 光

* [MicroPython-SI1145](https://github.com/neliogodoi/MicroPython-SI1145) - SI1145 紫外线指数、红外线、可见光和接近传感器。
* [micropython-tsl2561](https://github.com/kfricke/micropython-tsl2561) - TAOS/ams 的 TSL2561 照明传感器驱动程序。
* [mpy_bh1750fvi_esp8266](https://github.com/catdog2/mpy_bh1750fvi_esp8266) - BH1750FVI 传感器的 ESP8266 驱动程序。
* [bh1750](https://github.com/PinkInk/upylib/tree/master/bh1750) - BH1750 I2C 数字光传感器驱动器。
* [micropython-max44009](https://github.com/mcauser/micropython-max44009) - 用于 MAX44009 环境光传感器的 MicroPython 驱动程序。
* [veml7700](https://github.com/palouf34/veml7700) - 适用于 VEML7700 光传感器的 MicroPython 库。
* [MicroPython_MAX44009_driver](https://github.com/rcolistete/MicroPython_MAX44009_driver) - MAX44009 光传感器的 MicroPython 驱动程序。
* [MicroPython-VEML6075](https://github.com/neliogodoi/MicroPython-VEML6075) - VEML6075 紫外线传感器的驱动器底座。
* [BH1750](https://github.com/octaprog7/BH1750) - 适用于 BH1750 环境光传感器 (ALS) 的 MicroPython 模块。
* [veml7700](https://github.com/octaprog7/veml7700) - 适用于 Vishay VEML7700 环境光传感器 (ALS) 的 MicroPython 模块。
* [opt3001](https://github.com/octaprog7/opt3001) - 适用于 OPT3001（德州仪器 (TI) 的外部照明传感器）的 MicroPython 模块。
* [ltr390uv](https://github.com/octaprog7/ltr390uv) - 适用于 LTR390UV 的 MicroPython 模块，LTR390UV 是可见光和紫外线范围内的环境光传感器。
* [bh1750.py](https://github.com/adyavanapalli/bh1750.py) - MicroPython BH1750 环境光传感器驱动程序。

#### 称重传感器

* [micropython-hx711](https://github.com/SergeyPiskunov/micropython-hx711) - 适用于 HX711 24 位模数转换器的 MicroPython 驱动程序。
* [hx711_mpy-driver](https://github.com/HowManyOliversAreThere/hx711_mpy-driver) - HX711 称重传感器的 MicroPython 驱动程序。
* [hx710](https://github.com/QuirkyCort/IoTy/blob/main/public/extensions/hx710.py) - HX710 的 MicroPython 驱动程序。
* [hx711](https://github.com/robert-hh/hx711) - HX711 称重传感器接口的 MicroPython 驱动程序。
* [hx710](https://github.com/robert-hh/hx710) - HX710 称重传感器接口的 MicroPython 驱动程序。

#### 磁力计

* [MicroPython_LIS2MDL](https://github.com/jposada202020/MicroPython_LIS2MDL) - ST LIS2MDL 磁力计传感器的 MicroPython 驱动程序。
* [MicroPython_LIS3MDL](https://github.com/jposada202020/MicroPython_LIS3MDL) - ST LIS3MDL 磁力计的 MicroPython 驱动程序。
* [MicroPython_MLX90393](https://github.com/jposada202020/MicroPython_MLX90393) - MLX90393 磁力计的 MicroPython 驱动程序。
* [MicroPython_MMC5603](https://github.com/jposada202020/MicroPython_MMC5603) - Memsic MMC5603 磁力计的 MicroPython 驱动程序。
* [MicroPython_BMM150](https://github.com/jposada202020/MicroPython_BMM150) - 适用于 Bosch BMM150 磁力计的 MicroPython 驱动程序。
* [MicroPython_MMC5983](https://github.com/jposada202020/MicroPython_MMC5983) - 适用于 Memsic MMC5983 磁力计的 MicroPython 库。
* [MMC5603](https://github.com/octaprog7/MMC5603) - 适用于 MMC5603 地磁传感器的 MicroPython 模块。
* [HSCDTD008A](https://github.com/octaprog7/HSCDTD008A) - 适用于 HSCDTD008A 地磁传感器的 MicroPython 模块。
* [RM3100](https://github.com/octaprog7/RM3100) - 适用于 RM3100 地磁传感器的 MicroPython 模块。

#### 运动惯性

* [flight_controller](https://github.com/wagnerc4/flight_controller) - MicroPython 飞行控制器。
* [micropython-bmx055](https://github.com/micropython-IMU/micropython-bmx055) - 博世 BMX055 IMU 传感器驱动程序。
* [micropython-bno055](https://github.com/micropython-IMU/micropython-bno055) - 适用于 MicroPython 的博世 BNO055 驱动程序。具有硬件传感器融合的 IMU。
* [micropython-bno055](https://github.com/deshipu/micropython-bno055) - Bosch Sensortec BNO055 9DOF IMU 传感器，I2C 接口。
* [micropython-bno08x-rvc](https://github.com/rdagger/micropython-bno08x-rvc) - BNO08x 的 MicroPython 库。
* [micropython-fusion](https://github.com/micropython-IMU/micropython-fusion) - 传感器融合根据运动跟踪设备的输出计算航向、俯仰和滚动。
* [micropython-lsm9ds0](https://github.com/micropython-IMU/micropython-lsm9ds0) - LSM9DS0 g-force 线性加速度、高斯磁和 DPS 角速率传感器。
* [micropython-mpu6050](https://github.com/wybiral/micropython-mpu6050) - 用于读取 MPU-6050 加速度计和陀螺仪模块的 MicroPython 库。
* [micropython-mpu6050-mqtt-streamer](https://github.com/mozanunal/micropython-mpu6050-mqtt-streamer) - 在 ESP8266 上使用 MicroPython 将数据从 MPU6050 流式传输到 MQTT 服务器。
* [micropython-mpu6886](https://github.com/tuupola/micropython-mpu6886) - 用于 MPU6886 6 轴运动跟踪设备的 MicroPython I2C 驱动程序。
* [micropython-mpu9250](https://github.com/tuupola/micropython-mpu9250) - MPU9250 9 轴运动跟踪设备的 I2C 驱动程序。
* [micropython-mpu9250](https://gitlab.com/nnayo/micropython-mpu9250) - MicroPython MPU-9250 (MPU-6500 + AK8963) I2C 驱动程序。
* [micropython-mpu9x50](https://github.com/micropython-IMU/micropython-mpu9x50) - InvenSense MPU9250 惯性测量单元的驱动程序。
* [MPU6050-ESP8266-MicroPython](https://github.com/adamjezek98/MPU6050-ESP8266-MicroPython) - 用于 MPU6050 加速度计/陀螺仪的 ESP8266 驱动程序。
* [py-mpu6050](https://github.com/larsks/py-mpu6050) - 用于 MPU6050 加速度计/陀螺仪的 ESP8266 驱动程序。
* [upy-motion](https://github.com/OneMadGypsy/upy-motion) - 用 MicroPython 编写的简单 MPU6050 驱动程序。
* [MPU6050-ESP32-MicroPython](https://github.com/gitcnd/MPU6050-ESP32-MicroPython) - MPU6050（加速度计/陀螺仪）驱动程序，适用于 ESP32。
* [MicroPython_BMI160](https://github.com/jposada202020/MicroPython_BMI160) - 已存档。适用于 Bosch BMI160 加速度计/陀螺仪传感器的 MicroPython 驱动程序。
* [MicroPython_BMI270](https://github.com/jposada202020/MicroPython_BMI270) - 已存档。适用于 Bosch BMI270 加速度计/陀螺仪传感器的 MicroPython 驱动程序。
* [MicroPython_ICG20660](https://github.com/jposada202020/MicroPython_ICG20660) - 已存档。适用于 TDK ICG20660 加速度计/陀螺仪传感器的 MicroPython 驱动程序。
* [MicroPython_ICM20948](https://github.com/jposada202020/MicroPython_ICM20948) - 已存档。适用于 TDK ICM20948 加速度计/陀螺仪传感器的 MicroPython 驱动程序。
* [MicroPython_LSM6DSOX](https://github.com/jposada202020/MicroPython_LSM6DSOX) - 已存档。适用于 ST LSM6DSOX 加速度计/陀螺仪传感器的 MicroPython 库。

#### 邻近性

* [uPy_APDS9960](https://github.com/rlangoy/uPy_APDS9960) - 使用 APDS9960 的适用于 ESP8266 的 MicroPython 邻近库。
* [MicroPython_VCNL4010](https://github.com/jposada202020/MicroPython_VCNL4010) - 适用于 Vishay VCNL4010 接近和环境光传感器的 MicroPython 驱动程序。
* [apds9960](https://github.com/QuirkyCort/IoTy/blob/main/public/extensions/apds9960.py) - 适用于 APDS9960 的 MicroPython 驱动程序，具有简单的手势检测功能。

#### 辐射

* [micropython-geiger](https://github.com/Wangzhaotian725/micropython-geiger) - 带 MicroPython 卡的盖革计数器。
* [ESPGeiger](https://github.com/biemster/ESPGeiger) - 用于 ESP8266 盖革计数器的 MicroPython 库。

#### 土壤湿度

* [micropython-chirp](https://github.com/robberwick/micropython-chirp) - Chirp 土壤湿度传感器的驱动程序。
* [MicroPython-MiFlora](https://github.com/matthias-bs/MicroPython-MiFlora) - 小米 Mi Flora（又称花卉护理）BLE 植物传感器（土壤湿度/电导率/光强度/温度）。
* [micropython-miflora](https://github.com/agners/micropython-miflora) - 适用于小米 Mi Flora BLE 植物传感器的 MicroPython 库。

#### 光谱

* [AS726X_LoPy](https://github.com/jajberni/AS726X_LoPy) - AS726X 光谱传感器的 MicroPython 驱动程序。
* [MicroPython_AS7262X_driver](https://github.com/rcolistete/MicroPython_AS7262X_driver) - 适用于 AS7262/AS7263 纳米光谱仪传感器的 MicroPython 驱动程序。

#### 温度模拟

* [micropython-max31855](https://github.com/mcauser/deshipu-micropython-max31855) - 热电偶放大器，SPI接口。
* [max31856](https://github.com/alinbaltaru/max31856) - 具有线性化、SPI 接口的精密热电偶数字转换器。
* [max31865](https://github.com/sufyanaslam198/max31865) - 针对铂电阻温度探测器、SPI 接口优化的精密电阻数字转换器。
* [mcp9700](https://gitlab.com/CrispyCrafter/mcp9700) - MCP9700 的通用 MicroPython 驱动程序。
* [micropython-generic-thermistor](https://github.com/Trexation/micropython-generic-thermistor) - MicroPython 通用热敏电阻库，用于使用带分压器的 NTC 热敏电阻简化温度传感。
* [micropython-simple-thermistor](https://github.com/scruss/micropython-simple-thermistor) - 读取分压器中接线的 NTC 热敏电阻温度。

#### 温度数字

* [bme680-mqtt-micropython](https://github.com/robmarkcole/bme680-mqtt-micropython) - BME680 气体、压力、温度和湿度传感器的驱动程序。
* [LM75-MicroPython](https://github.com/OldhamMade/LM75-MicroPython) - LM75 数字温度传感器驱动程序，I2C 接口。
* [micropython-am2320](https://github.com/mcauser/micropython-am2320) - 奥松AM2320温湿度传感器，I2C接口。
* [micropython-dht12](https://github.com/mcauser/micropython-dht12) - 奥松DHT12温湿度传感器，I2C接口。
* [micropython-hdc1008](https://github.com/kfricke/micropython-hdc1008) - Texas Instruments HDC1008 湿度和温度传感器的驱动程序。
* [micropython-mcp9808](https://github.com/kfricke/micropython-mcp9808) - Microchip MCP9808 温度传感器的驱动程序。
* [micropython-mpl115a2](https://github.com/khoulihan/micropython-mpl115a2) - MPL115A2 气压传感器的 Pyboard 驱动程序。
* [micropython-sht30](https://github.com/rsc1975/micropython-sht30) - SHT30温湿度传感器驱动程序。
* [micropython-sht31](https://github.com/kfricke/micropython-sht31) - SHT31温湿度传感器驱动程序。
* [micropython-Si7005](https://github.com/Smrtokvitek/micropython-Si7005) - Si7005 相对湿度和温度传感器的驱动程序。
* [micropython-si7021](https://github.com/mcauser/deshipu-micropython-si7021) - SI7021温湿度传感器，I2C接口。
* [micropython-si7021](https://github.com/chrisbalmer/micropython-si7021) - SI7021温湿度传感器，I2C接口。
* [micropython-Si705x](https://github.com/billyrayvalentine/micropython-Si705x) - Silicon Labs Si705x 系列温度传感器，I2C 接口。
* [micropython-Si70xx](https://github.com/billyrayvalentine/micropython-Si70xx) - Silicon Labs Si70xx 系列相对湿度和温度传感器，I2C 接口。
* [micropython-tmp102](https://github.com/khoulihan/micropython-tmp102) - TMP102 数字温度传感器驱动程序。
* [Official DHT11+DHT12](https://github.com/micropython/micropython-lib/tree/master/micropython/drivers/sensor/dht) - 用于 DHT11 和 DHT12 温湿度传感器的 ESP8266 驱动程序。
* [sht25-micropython](https://github.com/Miceuz/sht25-micropython) - SHT25温湿度传感器驱动程序。
* [micropython-tmp1075](https://github.com/mattytrentini/micropython-tmp1075) - TI TMP1075 温度传感器的驱动程序。
* [micropython-sht11](https://github.com/2black0/micropython-sht11) - Sensirion SHT11 温度和湿度传感器的驱动程序。
* [micropython-lm75a](https://github.com/mcauser/micropython-lm75a) - NXP LM75A 数字温度传感器的驱动程序。
* [BME680-Micropython](https://github.com/robert-hh/BME680-Micropython) - BME680 传感器的 MicroPython 驱动程序。
* [htu21d-esp8266](https://github.com/julianhille/htu21d-esp8266) - 这是一个 MicroPython 模块/类，用于测量来自 HTU21D 的数据。
* [HTU21D](https://github.com/peterhinch/micropython-async/blob/master/v3/docs/HTU21D.md) - HTU21D温湿度传感器异步驱动器。
* [esp-sht3x-micropython](https://github.com/HAIZAKURA/esp-sht3x-micropython) - 用于带有 MicroPython 的 ESP8266/ESP32 的 SHT3x (SHT30/31/35) 库。
* [sht25-micropython](https://gitlab.com/miceuz/sht25-micropython) - SHT25温湿度传感器API的MicroPython实现。
* [micropython-sht30](https://github.com/schinckel/micropython-sht30) - 基于I2C总线的纯Python SHT30传感器驱动。
* [micropython_ahtx0](https://github.com/targetblank/micropython_ahtx0) - 适用于 AHT10 和 AHT20 温度和湿度传感器的 MicroPython 驱动程序。
* [sht85](https://github.com/octaprog7/sht85) - 适用于 [Sensiron SHT85](https://sensirion.com/products/catalog/SHT85/) 湿度和温度传感器的 MicroPython 驱动程序。
* [micropython-zacwire](https://github.com/mdaeron/micropython-zacwire) - 适用于 TSic 506F 温度传感器中使用的 ZACwire 协议的 MicroPython 驱动程序。
* [MicroPython_HTU31D](https://github.com/jposada202020/MicroPython_HTU31D) - 适用于 TE HTU31D 温度和湿度传感器的 MicroPython 库。
* [MicroPython_SHTC3](https://github.com/jposada202020/MicroPython_SHTC3) - 适用于 Sensirion SHTC3 温度和湿度传感器的 MicroPython 驱动程序。
* [MicroPython_TMP117](https://github.com/jposada202020/MicroPython_TMP117) - TMP117 温度传感器的 MicroPython 驱动程序。
* [MicroPython_SI7021](https://github.com/jposada202020/MicroPython_SI7021) - 用于温度和湿度 SI7021 传感器的 MicroPython 库。
* [MicroPython_ADT7410](https://github.com/jposada202020/MicroPython_ADT7410) - Analog Devices ADT7410 温度传感器的 MicroPython 驱动程序。
* [MicroPython_WSENTIDS](https://github.com/jposada202020/MicroPython_WSENTIDS) - 用于 WSEN WSEN-TIDS 温度传感器的 MicroPython 库。
* [MicroPython_HS3003](https://github.com/jposada202020/MicroPython_HS3003) - 适用于瑞萨 HS3003 温度和湿度传感器的 MicroPython 驱动程序。
* [MicroPython_STTS22H](https://github.com/jposada202020/MicroPython_STTS22H) - STTS22H 温度传感器的 MicroPython 驱动程序。
* [MicroPython_HTU21DF](https://github.com/jposada202020/MicroPython_HTU21DF) - MicroPython HTU21D-F 温度和湿度驱动程序。
* [MicroPython_SHT4X](https://github.com/jposada202020/MicroPython_SHT4X) - 适用于 Sensirion 温度和湿度 SHT40 和 SHT45 传感器的 MicroPython 驱动程序。
* [MicroPython_SHT20](https://github.com/jposada202020/MicroPython_SHT20) - 适用于 Sensirion SHT20 温度传感器的 MicroPython 驱动程序。
* [MicroPython_MCP9808](https://github.com/jposada202020/MicroPython_MCP9808) - Microchip MCP9808 温度传感器的 MicroPython 驱动程序。
* [MicroPython_HDC1080](https://github.com/jposada202020/MicroPython_HDC1080) - 适用于 TI HDC1080 温度和湿度传感器的 MicroPython 驱动程序。
* [TMP117](https://github.com/octaprog7/TMP117) - 适用于 Texas Instruments 的 TMP117 温度传感器的 MicroPython 模块。
* [BME680](https://github.com/octaprog7/BME680) - 适用于博世低功耗气体、压力、温度和湿度传感器 BME680 的 MicroPython 模块。
* [SHT30](https://github.com/robert-hh/SHT30) - 适用于 Sensirion SHT3x 传感器的 MicroPython 驱动程序。
* [MicroPython_AS6212](https://github.com/jposada202020/MicroPython_AS6212) - 用于 ASM AS6212 温度传感器的 MicroPython 库。
* [MicroPython_PCT2075](https://github.com/jposada202020/MicroPython_PCT2075) - NXP Semiconductors PCT2075 温度传感器的 MicroPython 驱动程序。
* [micropython-hdc1080](https://github.com/mcauser/micropython-hdc1080) - HDC1080 温度和湿度传感器的 MicroPython 驱动程序。
* [bme680-pure-mp](https://github.com/antirez/bme680-pure-mp) - 纯 MicroPython Bosch BME680 传感器驱动程序。
* [SHT4X](https://github.com/octaprog7/SHT4X) - 用于控制 SHT4x - 第四代相对湿度和温度传感器的 MicroPython 模块。

#### 温度红外

* [micropython-mlx90614](https://github.com/mcauser/micropython-mlx90614) - Melexis MLX90614 红外温度传感器驱动程序。
* [MicroPython_MLX90615_driver](https://github.com/rcolistete/MicroPython_MLX90615_driver) - 适用于 Melexis MLX90615 红外温度传感器的 MicroPython 驱动程序。

#### 电容触摸

* [micropython-mpr121](https://github.com/mcauser/micropython-mpr121) - MPR121 电容式触摸键盘和分线板的驱动程序。
* [micropython-ttp223](https://github.com/mcauser/micropython-ttp223) - 使用TTP223电容式触摸模块的示例。
* [micropython-TTP229-BSF](https://github.com/alankrantas/micropython-TTP229-BSF) - 适用于串行接口模式下 TTP229-BSF 16 键电容式键盘的 MicroPython ESP8266/ESP32 驱动程序。
* [uFT6336U](https://github.com/fantasticdonkey/uFT6336U) - 适用于 Focus LCD FT6336U 电容式触摸屏控制器 IC 的 MicroPython I2C 驱动程序。
* [MicroPythonTrill](https://github.com/Heerkog/MicroPythonTrill) - 适用于 MicroPython 的 Trill 触摸传感器库。
* [L58Touch](https://github.com/russhughes/L58Touch) - L58 多点触控 MicroPython 模块。
* [micropython-ft6x06](https://github.com/antirez/micropython-ft6x06) - 纯 Python 中 FT6x06 电容式触摸传感器的简单驱动程序。

#### 电阻式触摸

* [XPT2046-touch-pad-driver](https://github.com/robert-hh/XPT2046-touch-pad-driver) - 许多 TFT 模块中使用的 XPT2046 触摸板控制器的驱动程序。

### 调度

* [micropython-mcron](https://github.com/fizista/micropython-mcron) - MicroCRON 是 MicroPython 的基于时间的任务调度程序。
* [micropython-scron](https://github.com/fizista/micropython-scron) - SimpleCRON 是一个基于时间的任务调度程序，其灵感来自于 Unix 系统著名的 cron 程序。
* [Schedule](https://github.com/peterhinch/micropython-async/blob/master/v3/docs/SCHEDULE.md) - 基于 asyncio 的应用程序的调度程序。在指定的时间和日期或参考太阳和月亮的升起和落下安排活动。
* [micropython-aioschedule](https://github.com/ThinkTransit/micropython-aioschedule) - 持久 uasyncio 调度程序，支持任务运行之间的深度睡眠。
* [Suntime](https://github.com/lorcap/micropython-suntime) - 日出和日落时间的近似计算。给定地球上某个地点的“日期”和坐标对“（纬度，经度）”，该库会计算当天太阳在该地点升起和落下的时间。

### 存储

#### 配置文件

* [uPyftsConf](https://github.com/aleppax/upyftsconf) - MicroPython 的配置文件太简单了。将配置写入自身的单个文件库。
* [toml](https://github.com/gitcnd/toml) - 读取和写入 .toml 文件。适用于 MicroPython 和 CircuitPython。

#### 数据库

* [uPyMySQL](https://github.com/dvrhax/uPyMySQL) - 纯 MicroPython MySQL 客户端。
* [micropython-redis](https://github.com/dwighthubbard/micropython-redis) - 专为与 MicroPython 一起使用而设计的 Redis 客户端实现。
* [picoredis](https://github.com/SpotlightKid/picoredis) - 一个非常小的 Redis 客户端（不仅仅是），适用于 MicroPython。
* [micropg](https://github.com/nakagami/micropg) - 适用于 MicroPython 的 PostgreSQL 数据库驱动程序。
* [micropg_lite](https://github.com/TimonW-Dev/micropg_lite) - micropg 的轻量级版本，有一些轻微的限制（例如错误处理），以便在低 RAM 微控制器上运行（与 ESP8266 配合使用）。
* [micropg_superlite](https://github.com/TimonW-Dev/micropg_superlite) - 基于 micropg_lite/micropg 的最轻量级的 MicroPython PostgreSQL 数据库驱动程序，但在功能上有更强的限制，并且只关注绝对必要的功能。
* [micropython-cratedb](https://github.com/crate/micropython-cratedb/) - CrateDB 数据库的 MicroPython 驱动程序。
* [nmongo](https://github.com/nakagami/nmongo) - 适用于 CPython 和 MicroPython 的 MongoDB 客户端，具有类似于 MongoDB shell 的 API。
* [MicroPyDatabase](https://github.com/sungkhum/MicroPyDatabase) - 适用于 MicroPython 的基于 JSON 的低内存数据库。
* [micropython-firebase-realtime-database](https://github.com/ckoever/micropython-firebase-realtime-database) - 针对 ESP32 优化的 MicroPython 的 Firebase 实现。
* [micropython-firebase-firestore](https://github.com/WoolDoughnut310/micropython-firebase-firestore) - MicroPython 的 Firebase Firestore 实现。
* [uSQLite](https://github.com/spatialdude/usqlite) - MicroPython 的 SQLite 库模块。
* [simple-db](https://github.com/ctimmer/simple-db) - 使用 B 树的 MicroPython 关系数据库。

#### EEPROM

* [micropython_eeprom](https://github.com/peterhinch/micropython_eeprom) - 适用于存储芯片（EEPROM、FRAM、闪存、PSRAM）的跨平台 MicroPython 设备驱动程序。
* [mb_24x256_512](https://github.com/MarksBench/mb_24x256_512) - 适用于 Microchip 24x256 和 24x512 I2C EEPROM 设备的非常简单的 MicroPython 模块/驱动程序。
* [micropython-eeprom](https://github.com/brainelectronics/micropython-eeprom) - AT24Cxx EEPROM 的 MicroPython 驱动程序。

#### 闪光灯

* [micropython_data_to_py](https://github.com/peterhinch/micropython_data_to_py) - 一个 Python 3 实用程序，用于将任意二进制文件转换为 Python 源代码，以便在 Flash 中冻结为字节码。
* [micropython-winbond](https://github.com/brainelectronics/micropython-winbond) - 通过SPI与Winbond W25Q Flash芯片交互。
* [freezeFS](https://github.com/bixb922/freezeFS) - 为 MicroPython 创建自解压压缩或自安装存档。

#### 铁电存储器

* [micropython-fram](https://github.com/rolandvs/micropython-fram) - 铁电 RAM 模块的 Pyboard 驱动程序。

#### PSRAM

* [mb_PSRAM_64Mb_SPI](https://github.com/MarksBench/mb_PSRAM_64Mb_SPI) - 非常简单的 MicroPython 模块，可将通用 64Mbit PSRAM（即 Adafruit 4677）与 Raspberry Pi Pico (RP2040) 结合使用。

#### 标清

* [mp-sdcard-littleFS](https://github.com/jornamon/mp-sdcard-littleFS) - 与 LittleFS2 配合使用的 MicroPython SD 卡驱动程序（实现扩展接口）。

#### 静态随机存储器

* [mb_23LC1024](https://github.com/MarksBench/mb_23LC1024) - 非常简单的 MicroPython 模块，可将 Microchip 23LC1024 SPI SRAM 与 Raspberry Pi Pico (RP2040) 结合使用。
* [mb_47x16](https://github.com/MarksBench/mb_47x16) - 适用于 Microchip 47x16 EERAM 设备 (47L/47C) 的非常简单的 MicroPython 模块/驱动程序。

### 螺纹加工

* [MicroWorkers](https://github.com/jczic/MicroWorkers) - 一个微型工人类，可轻松管理线程池以优化同时作业和作业结束，适用于 MicroPython（用于 Pycom 模块和 ESP32）。

### 用户界面

* [upymenu](https://github.com/jplattel/upymenu) - 用于 LCD 显示器的 MicroPython 菜单。

### 公用事业

* [micropython-hexdump](https://github.com/mattytrentini/micropython-hexdump) - MicroPython 的 Hexdump 实现。
* [mp_wcwidth](https://github.com/Josverl/mp_wcwidth) - Python port of [wcwidth](https://github.com/jquast/wcwidth) to handle wide unicode characters such as "你好世界" in terminal output.
* [micropython-units](https://github.com/WoolleySheep/micropython-units) - 用于在 MicroPython 中处理物理量的库。

## 社区

* [MicroPython Discussions on GitHub](https://github.com/orgs/micropython/discussions) - 与 MicroPython 相关的所有内容的 GitHub 讨论。
* [MicroPython Forum (archive)](https://forum.micropython.org/) - 关于与 MicroPython 相关的所有事情的存档社区对话。
* [Discord](https://micropython.org/discord) - 获得 MicroPython Discord 服务器的邀请。
* [MicroPython on Mastodon / Fediverse](https://fosstodon.org/@MicroPython) - 在 Fediverse 中关注 MicroPython。
* [MicroPython on Twitter](https://twitter.com/micropython) - 在 Twitter 上关注 MicroPython 了解最新新闻和更新。
* [MicroPython on Facebook](https://www.facebook.com/micropython) - 喜欢 Facebook 上的 MicroPython，了解竞赛、新闻和更新。
* [Melbourne MicroPython Meetup](https://www.meetup.com/en-au/micropython-meetup/) - 在澳大利亚墨尔本 CCHS 定期聚会。

## 教程
* [100 Days 100 IoT Projects](https://github.com/kritishmohapatra/100_Days_100_IoT_Projects) - 为期 100 天的挑战，在 ESP32、ESP8266 和 Raspberry Pi Pico 2W 上使用 MicroPython 构建现实世界的物联网项目。为初学者提供了逐步记录的接线图和代码。
* [asyncio](https://github.com/peterhinch/micropython-async/blob/master/v3/docs/TUTORIAL.md) - 编写与硬件设备交互的异步代码。
* [Asynchronous drivers](https://github.com/peterhinch/micropython-async/blob/master/v3/docs/DRIVERS.md) - 开关、按钮、编码器和 ADC 异步接口的教程和代码。
* [Pyboard micropower](https://github.com/peterhinch/micropython-micropower) - Pyboard 1.x 和 Pyboard D 上的低功耗应用程序的教程和代码。
* [3D rotation with quaternions](https://github.com/peterhinch/micropython-samples/blob/master/QUATERNIONS.md) - 进行 3D 旋转的简单方法的教程和代码。
* [Miguel Grinberg](https://blog.miguelgrinberg.com/category/MicroPython) - MicroPython 和物联网。
* [Bhavesh Kakwani](https://bhave.sh/) - MicroPython 视频 + 书面教程。
* [CoderDojo Twin Cities MicroPython](https://github.com/CoderDojoTC/micropython) - 用于向儿童教授 MicroPython 的完整编码课程。
* [MicroPython Tutorials for ESP32 boards](https://www.upesy.com/blogs/tutorials/tutorials-for-esp32-with-micropython-code) - 带有代码示例的教程，用于学习 MicroPython 与 ESP32 板的基础知识。
* [Learn MicroPython with a Pi Pico board](https://www.upesy.com/blogs/tutorials/tutorials-for-rpi-pi-pico-with-micropython-code) - 使用 Raspberry Pi Pico / RP240 板的 MicroPython 教程。

## 书籍

* [Programming with MicroPython: Embedded Programming with Microcontrollers and Python](https://www.oreilly.com/library/view/programming-with-micropython/9781491972724/) - 作者：尼古拉斯·H·托勒维。国际标准书号 9781491972731。
* [MicroPython for the Internet of Things: A Beginner's Guide to Programming with Python on Microcontrollers](https://link.springer.com/book/10.1007/978-1-4842-3123-4) - 作者：查尔斯·贝尔。国际标准书号 9781484231227。
* [Beginning MicroPython with the Raspberry Pi Pico: Build Electronics and IoT Projects](https://link.springer.com/book/10.1007/978-1-4842-8135-2) - 作者：查尔斯·贝尔。国际标准书号 9781484281345。
* [MicroPython Cookbook](https://www.packtpub.com/en-us/product/micropython-cookbook-9781838641955) - 作者：马尔万·阿尔萨巴格。国际标准书号 9781838649951。
* [Python for Microcontrollers: Getting Started with MicroPython](https://www.mhprofessional.com/python-for-microcontrollers-getting-started-with-micropython-9781259644535-usa-group) - 作者：唐纳德·诺里斯。国际标准书号 9781259644535。
* [Advanced Programming in MicroPython By Example](https://www.amazon.com/Advanced-Programming-MicroPython-Example-Magda/dp/1090900937) - 作者：尤里·玛格达。国际标准书号 9781090900937。
* [MicroPython Projects](https://www.packtpub.com/en-us/product/micropython-projects-9781789952537) - 作者：雅各布·贝宁戈。国际标准书号 9781789958034。
* [Get Started with MicroPython on Raspberry Pi Pico 2nd Edition](https://store.rpipress.cc/collections/books/products/get-started-with-micropython-on-raspberry-pi-pico-2nd-edition) - 作者：加雷斯·哈法里 (Gareth Halfacree) 和本·埃弗拉德 (Ben Everard)。国际标准书号 9781912047291。
* [MicroPython for Microcontrollers](https://www.elektor.com/micropython-for-microcontrollers-e-book) - 作者：君特·斯潘纳。国际标准书号 9783895764370。
* [MicroPython for the Raspberry Pi Pico W: A gentle introduction to programming digital circuits with Python](https://www.amazon.com/MicroPython-Raspberry-Pico-introduction-programming/dp/B0BKSCV18D) - 作者：米格尔·格林伯格。国际标准书号 9798361302710。
* [Programming ESP32: Learn MicroPython Coding and Electronics](https://www.amazon.com/Programming-ESP32-MicroPython-Coding-Electronics/dp/1739487451/) - 作者：西蒙·蒙克。国际标准书号 9781739487454。

## 框架

* [micrOS](https://github.com/BxNxM/micrOS) - 基于 MicroPython 的物联网框架。
* [terkin-datalogger](https://github.com/hiveeyes/terkin-datalogger) - 适用于 MicroPython 和 CPython 的灵活数据记录器应用程序。
* [perthensis](https://codeberg.org/scy/perthensis) - Perthensis：MicroPython 的异步框架。
* [meerkat](https://github.com/crdietrich/meerkat) - 适用于 MicroPython 和 Raspberry Pi 的 I2C 数据采集。
* [public-micropython-iot-platform](https://github.com/wolfen351/public-micropython-iot-platform) - Fred MicroPython 物联网平台项目，用于控制继电器、温度传感器、按钮、触摸屏、GPS 等的代码。具有响应式 Web UI、MQTT、家庭助理和 ThingsBoard 支持。

## 资源

* [MicroPython](https://micropython.org) - 项目网站。测试驱动 Pyboard。通过 Unicorn 在线尝试 MicroPython。
* [MicroPython on GitHub](https://github.com/micropython/micropython) - 在 GitHub 上提交错误报告、关注并参与开发。
* [MicroPython Official Documentation](https://docs.micropython.org/) - 适用于各种端口，包括快速参考、一般信息、示例和教程。
* [MicroPython Wiki](https://github.com/micropython/micropython/wiki) - 社区生成的有关 MicroPython 和 Pyboard 功能的文档和示例。
* [MicroPython Newsletter](https://micropython.org/newsletter) - 订阅 MicroPython 时事通讯，了解新闻和公告，包括新功能和新产品。
* [MicroPython Store](https://store.micropython.org/) - 您可以在其中购买 Pyboard、外壳、皮肤、书籍、连接器和外围设备。
* [MicroPython on Wikipedia](https://en.wikipedia.org/wiki/MicroPython) - 维基百科上的 MicroPython。
* [awesome-micropythons](https://github.com/adafruit/awesome-micropythons) - MicroPython 的许多分支和端口。

## 发展

### 代码生成

* [micropy-cli](https://github.com/BradenM/micropy-cli) - Micropy CLI 是一个项目管理/生成工具，用于在现代 IDE（例如 Visual Studio Code）中编写 MicroPython 代码。
* [micropython-stubber](https://github.com/Josverl/micropython-stubber) - 为不同的 MicroPython 固件生成并使用存根，以与 Visual Studio Code 或任何 IDE 和 linter 结合使用。
* [micropython-stubs](https://github.com/Josverl/micropython-stubs) - 大多数 MicroPython 端口、板和版本的存根，使编写代码变得更加简单。
* [micropy-stubs](https://github.com/BradenM/micropy-stubs) - 为 Micropy-Cli 和其他人自动生成存根包。
* [micropython-extmod-generator](https://github.com/prusnak/micropython-extmod-generator) - 用 C 编写的 MicroPython 外部模块生成器。
* [micropython-package-template](https://github.com/brainelectronics/micropython-package-template) - GitHub 工作流支持 MicroPython 包模板，在推送到主分支时部署到 [Python 包索引](https://pypi.org/)，并在 PR 上测试部署到 [测试 Python 包索引](https://test.pypi.org/)。
* [micropython-usermod](https://micropython-usermod.readthedocs.io) - 关于用 C 编写的 MicroPython 外部模块的在线书籍。
* [wasm2mpy](https://github.com/vshymanskyy/wasm2mpy) - 将 WebAssembly 编译为本机 MicroPython `.mpy` 文件。允许使用各种静态编译语言编写代码，并将其转换为 C 以获得接近本机的性能。

### 调试

* [esp32-backtrace](https://github.com/tve/esp32-backtrace) - ESP32 异常堆栈回溯分析器。
* [micropython-aiosentry](https://github.com/devbis/micropython-aiosentry) - 适用于 MicroPython 的异步 Sentry.io 微客户端。
* [micropython-usyslog](https://github.com/kfricke/micropython-usyslog) - 适用于 MicroPython 的简单远程系统日志客户端。
* [Asynchronous monitor](https://github.com/peterhinch/micropython-monitor) - 使用 Raspberry Pico 和逻辑分析仪或示波器来监视异步代码。

### 固件

* [micropython-builder](https://github.com/jonahbron/micropython-builder) - 用于构建和刷新自定义 MicroPython 固件的工具。
* [mpflash](https://pypi.org/project/mpflash/) - ⚡您的终极 MicroPython 闪存伴侣，适用于 stm32、rp2、esp32、esp8266、samd。

### IDE

* [BIPES](https://bipes.net.br/ide/) - 基于 Web 的 MicroPython IDE，具有文件管理器、编辑器、块代码生成、IoT 仪表板和 Web 浏览器上的串行/USB/蓝牙/WebREPL 控制台。来源：[https://github.com/BIPES](https://github.com/BIPES)。
* [Embedible](https://embedible.io/) - AI 硬件副驾驶，可帮助您为 ESP32 和 Raspberry Pi Pico W 设计、连接和编码 MicroPython 项目。
* [ESP32-MPY-Jama](https://github.com/jczic/ESP32-MPY-Jama) - 用于使用 MicroPython 管理 Espressif ESP32 微控制器的工具。
* [JetBrains IntelliJ/PyCharm MicroPython Plugin](https://plugins.jetbrains.com/plugin/9777-micropython) - IntelliJ 和 PyCharm 中 MicroPython 设备的插件。
* [MicroPython IDE for VSCode](https://marketplace.visualstudio.com/items?itemName=dphans.micropython-ide-vscode) - 适用于 Visual Studio Code 的 MicroPython IDE。
* [MicroPython-REPLink for VSCode](https://marketplace.visualstudio.com/items?itemName=SWC-Fablab.micropython-replink) - 与 MicroPython REPL 终端交互的便捷快捷方式。
* [MPRemote for VSCode](https://marketplace.visualstudio.com/items?itemName=DavesCodeMusings.mpremote) - 一个扩展，可让您从 Visual Studio Code 中轻松访问 mremote 的某些功能。
* [Mu Editor](https://codewith.mu/) - Code with Mu：适合初学者的简单 Python/MicroPython/CircuitPython 编辑器。
* [Thonny IDE](https://thonny.org/) - Thonny：适合初学者的 Python IDE。
* [ViperIDE](https://viper-ide.org) - 适用于 Web 和移动设备的创新 MicroPython / CircuitPython IDE。无需安装。
* [Pyboard File Manager](https://github.com/joewez/PyboardFileManager) - Pyboard 文件管理器：适用于 Pyboard.py 兼容设备的 Windows GUI。
* [uPIDE](https://github.com/harbaum/upide) - µPIDE 是一个简单的 MicroPython IDE。
* [pye](https://github.com/robert-hh/Micropython-Editor) - 在设备编辑器上。

### 记录

* [micropython-ulogger](https://github.com/majoson-chen/micropython-ulogger) - 为MicroPython定制的轻量级日志模块。
* [scd30logger](https://github.com/agners/scd30logger) - 基于 Sensirion SCD30 的 MicroPython 二氧化碳、湿度和温度记录仪。
* [sht15logger](https://github.com/agners/sht15logger) - 使用 Sensirion SHT15 的 MicroPython 温度和湿度记录仪。

### 贝壳

#### 朱皮特

* [micropython-magic](https://github.com/josverl/micropython-magic) - MicroPython 集成到 Jupyter 笔记本中。
* [jupyter_upydevice_kernel](https://github.com/Carglglz/jupyter_upydevice_kernel) - Jupyter 内核通过其 REPL 接口与 MicroPython 板进行交互。

#### 在设备上

* [upy-shell](https://github.com/dhylands/upy-shell) - 适用于 MicroPython 的简单的基于命令行的 shell。
* [Micropython-Editor](https://github.com/robert-hh/Micropython-Editor) - 用 Python 编写的适用于 Pyboard、WiPy、ESP8266、ESP32、PyCom 和 Adafruit 设备的小型板载编辑器。
* [mpy_shell](https://github.com/gitcnd/mpy_shell) - 适用于 MicroPython 的类似 Linux 的 shell。功能齐全，非常轻巧。

#### 在主机上

* [rshell](https://github.com/dhylands/rshell) - 将文件复制或同步到开发板，从终端输入 REPL。
* [ampy](https://github.com/scientifichackers/ampy) - 通过串行连接与 MicroPython 板交互的实用程序。
* [mpbridge](https://github.com/AmirHmZz/mpbridge) - 一个文件系统桥，用于同步和管理运行 MicroPython 的设备上的文件。
* [mpfshell](https://github.com/wendlers/mpfshell) - 一个简单的基于 shell 的文件浏览器，适用于 ESP8266 和 WiPy。
* [mpsync](https://github.com/thilomichael/mpsync) - 一种自动将代码同步到 MicroPython 板的工具。
* [mpremote](https://github.com/micropython/micropython/blob/master/tools/mpremote/README.md) - 强大的官方shell，支持将主机当前目录挂载到目标上。运行代码而不更改目标的文件系统。
* [MPRemoteEditor](https://github.com/joewez/MPRemoteEditor) - 一个简单的 Windows IDE，用于使用 MicroPython MPRemote 设备进行开发。
* [uPyExplorer](https://github.com/RetepRelleum/uPyExplorer) - MicroPython 设备的资源管理器。
* [mpr](https://github.com/bulletmark/mpr) - MicroPython mpremote 工具的包装器。

### 工具

* [belay](https://github.com/BrianPugh/belay) - Belay 是一个 Python 库，可以快速开发通过 MicroPython 兼容板与硬件交互的项目。
* [ESP-File_manager](https://github.com/mispacek/ESP-File_manager) - 基于 Web 的文件管理器，直接在 MicroPython 中的 ESP32 上运行。
* [mcu_serial](https://github.com/gitcnd/mcu_serial) - 用于连接到 MicroPython 板的命令行串行仿真器。

## 杂项

* [MicroPython Kickstarter](https://www.kickstarter.com/projects/214379695/micro-python-python-for-microcontrollers) - 1,931 位支持者承诺捐赠 97,803 英镑来帮助实现该项目。
* [MicroPython on the ESP8266 Kickstarter](https://www.kickstarter.com/projects/214379695/micropython-on-the-esp8266-beautifully-easy-iot) - 1,399 位支持者承诺捐赠 28,534 英镑来帮助实现该项目。

## 贡献

随时欢迎您的贡献和建议！请先查看[贡献指南](https://github.com/mcauser/awesome-micropython/blob/master/contributing.md)。

如果我不确定这些库是否很棒，我将保留一些拉取请求，您可以通过添加 👍 来投票给它们。
