# 很棒的智能电视 [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

> 用于构建智能电视应用程序的精选资源列表

<a href="https://github.com/vitalets/awesome-smart-tv"><img align="right" width="150" src="https://user-images.githubusercontent.com/1473072/27913047-7c3a5e60-6267-11e7-8bd1-bef2bf3cd753.png"/></a>

[智能电视](https://en.wikipedia.org/wiki/Smart_TV) 是一个不断发展的电视平台，可以访问互联网并允许浏览网站和安装应用程序。它拥有自己的生态系统，主要参与者有三星、LG、Android TV 和 Apple TV。在此列表中，您将找到用于开发智能电视应用程序以及从远程设备与电视通信的官方和第三方资源。

## 内容
* [Platforms](#platforms)
  * [三星Tizen](#samsung-tizen)
  * [LG网络操作系统](#lg-webos)
  * [安卓电视](#android-tv)
  * [苹果电视操作系统](#apple-tvos)
  * [谷歌Chromecast](#google-chromecast)
* [跨平台框架](#cross-platform-frameworks)
* [远程控制协议](#remote-control-protocols)
* [跨平台工具](#cross-platform-tools)
* [导航库](#navigation-libraries)
* [Testing](#testing)
* [Misc](#misc)
* [Community](#community)

## 平台
以下是最流行的智能电视平台。完整列表位于[此处](https://en.wikipedia.org/wiki/List_of_smart_TV_platforms_and_middleware_software)。

### 三星Tizen
#### 官方资源
* [Samsung TV Developers site](http://developer.samsung.com/tv) - 新闻、文档和 SDK 下载。
* [Tizen TV Developers site](https://developer.tizen.org/tizen/tv) - 用于开发 Tizen TV 应用程序的完整 API 文档和指南。
* [Tizen Studio](https://developer.tizen.org/development/tizen-studio/download) - 用于电视应用程序开发的 IDE，包括 Tizen TV Emulator。
* [Smart View SDK](http://developer.samsung.com/tv/develop/extension-libraries/smart-view-sdk/download/) - 官方 Android、IOS 和 JavaScript SDK，用于远程设备和三星智能电视之间的通信。
* [Samsung TV Developers Forum](http://developer.samsung.com/forum/?topCtgy=06) - 使用 Samsung SDK 开发应用程序时提出问题并分享技巧。
* [Samsung Smart TV Bug Bounty](https://samsungtvbounty.com) - 如果您发现 Samsung TV 中的错误，请在此处提交并获得 1000+ 美元的奖励。
* [vscode-extension-tizentv](https://marketplace.visualstudio.com/items?itemName=tizensdk.tizentv) - 一个 Visual Studio Code 扩展，为 Tizen 应用程序开发人员提供轻量级 IDE。
* [Wits](https://github.com/Samsung/Wits) - 一种用于重新加载电视应用程序的 JavaScript/CSS 的工具，而无需在每次进行更改时重新安装应用程序。

#### 第三方远程控制库
* [samsungctl](https://github.com/Ape/samsungctl) - 用于通过 TCP/IP 连接远程控制三星电视的库和命令行工具。目前，它支持 2016 年之前的电视以及大多数具有以太网或 Wi-Fi 连接 (Python) 的现代 Tizen-OS 电视。
* [samsung-tv-remote](https://github.com/Badisi/samsung-tv-remote) - 从 2016 年开始使用 Node.js 模块远程控制三星智能电视 (JavaScript)。
* [homebridge-samsungtv2016](https://github.com/kyleaa/homebridge-samsungtv2016) - [Homebridge](https://github.com/nfarina/homebridge) 的插件，可让您使用 HomeKit 和 Siri (JavaScript) 控制 2016 款三星电视。
* [homebridge-samsung-tizen](https://github.com/tavicu/homebridge-samsung-tizen) - [Homebridge](https://github.com/nfarina/homebridge) 的插件，允许您使用 HomeKit 和 Siri (JavaScript) 控制您的 Samsung Tizen 电视。
* [samsung-remote-models-2014-and-newer](https://github.com/tdudek/samsung-remote-models-2014-and-newer) - 与 Samsung TV 型号 2014+ 的内部 Web 服务进行加密通信。
* [SmartCrypto](https://github.com/sectroyer/SmartCrypto) - SmartView2 加密握手 API 在 C/Python 中的实现。
* [samsung-messagebox](https://github.com/shantanugoel/samsung-messagebox) - 用于在三星电视上显示通知的 Python 脚本。
* [samsung-tv-control](https://github.com/Toxblh/samsung-tv-control) - 在 Node.js 中远程控制三星电视的库

#### 其他
* [Identification of Samsung TV models 2008-2017](http://en.tab-tv.com/?page_id=7123) - 如何从三星电视型号名称获取屏幕尺寸、矩阵类型、开发年份、系列等参数。
* [Tizen Studio development references](https://github.com/claromes/tizenstudio) - 基于个人研究的文档重点关注智能电视和专业显示器的网络应用程序。
* [TizenBrew] (https://github.com/reisxd/TizenBrew) - 一种体验修改网站的方式，您可以安装更新的应用程序，而无需与 Tizen Studio 对抗
* [TizenTube] (https://github.com/reisxd/TizenTube) - TizenBrew 模块，通过删除广告和添加对 Sponsorblock 的支持来增强您最喜欢的流媒体网站的观看体验。

### LG网络操作系统
#### 官方资源
* [webOS TV Developers Site](http://webostv.developer.lge.com) - WebOS TV 应用开发原理、教程、API 文档和打包工具。
* [webOS TV IDE + SDK](http://webostv.developer.lge.com/sdk/download/download-sdk/) - 用于应用程序开发的 IDE，包括命令行界面和模拟器。
* [Connect SDK](http://www.svlconnectsdk.com/) - LG 开发的开源框架可将您的移动应用程序与多个媒体设备平台连接起来。目前支持8个平台。但似乎[已放弃](https://github.com/ConnectSDK/Connect-SDK-Android/issues/364)。
* [webOS TV Developers Forum](http://developer.lge.com/community/forums/RetrieveForumList.dev?prodTypeCode=TV) - 与其他开发者提出问题、分享信息并了解智能电视应用程序开发。

#### 第三方远程控制库
* [lgtv2](https://github.com/hobbyquaker/lgtv2) - Node.js 模块，用于通过 WebSocket 消息 (JavaScript) 远程控制 LG webOS TV。
* [node-red-contrib-lgtv](https://github.com/hobbyquaker/node-red-contrib-lgtv) - [Node-RED](https://nodered.org) 模块允许远程控制 LG webOS 智能电视 (JavaScript)。
* [node-webos](https://github.com/WeeJeWel/node-webos) - 用于发现和控制 webOS 电视的 Node.js 模块 (JavaScript)。
* [lgtv2mqtt](https://github.com/hobbyquaker/lgtv2mqtt) - LG WebOS 智能电视和 MQTT (JavaScript) 之间的接口。
* [ares-webos-sdk](https://github.com/stevenvong/ares-webos-sdk) - webOS [CLI](http://webostv.developer.lge.com/sdk/using-webos-tv-cli/) 作为单独的 NPM 模块 (JavaScript)。
* [pylgtv](https://github.com/TheRealLink/pylgtv) - 用于控制基于 webOS 的 LG 电视设备的库 (Python)。
* [LGWebOSRemote](https://github.com/klattimer/LGWebOSRemote) - 用于 LG 电视 webOS 远程控制的命令行工具 (Python)。
* [homebridge-webos-tv](https://github.com/merdok/homebridge-webos-tv) - [Homebridge](https://github.com/nfarina/homebridge) 的插件，可让您控制 webOS 电视。
* [PyWebOSTV](https://github.com/supersaiyanmode/PyWebOSTV) - 通用且可扩展的 WebOS 3.0 客户端库（Python2、Python3）。
* [go-webos](github.com/kaperys/go-webos) - 用于与 webOS 电视（golang）交互的小型 Go 库。

#### 视频
* [LG Magic Motion Remote - Point, Click, and Control](https://youtu.be/yxu0G7jM_us) - 像电脑鼠标一样操作电视。

#### 其他
* [openlgtv.org.ru](http://openlgtv.org.ru) - 一个针对 LG 电视固件的合法逆向工程和研究的非商业项目。看起来有点过时，但包含很多信息。
* [Identification of LG TV models 2011-2017](http://en.tab-tv.com/?page_id=7111) - 如何从 LG 电视型号名称获取屏幕尺寸、矩阵类型、开发年份、系列等参数。

### 安卓电视
#### 官方资源
* [Android TV Developers site](https://developer.android.com/training/tv/start/start.html) - 有关构建 Android TV 应用的文档、教程和最佳实践。

#### 文章
* [How to develop Android TV App?](https://medium.com/@halilozel1903/how-to-develop-android-tv-app-5e251f3aa56b) - 一篇有关为 Android TV 开发应用程序的文章。

### 苹果电视操作系统
#### 官方资源
* [tvOS Developers Site](https://developer.apple.com/tvos/) - 用于开发 tvOS 应用程序的 SDK、文档和教程。
* [TVML](https://developer.apple.com/documentation/tvml) - 用于创建 tvOS 应用程序的 Apple TV 标记语言。

### 谷歌Chromecast
#### 官方资源
* [Google Cast SDK](https://developers.google.com/cast/) - 官方 Google Cast SDK 文档和教程。
* [TVs with Chromecast built-in](https://www.google.com/chromecast/built-in/tv/) - 支持内置 Chromecast 的供应商列表以及相对于传统电视遥控器的优势。

## 跨平台框架
* [react-tv](https://github.com/raphamorim/react-tv) - TV 的 React 开发：低内存应用程序的渲染器和 WebOS、Tizen、Orsay 的打包器。
* [TOAST](http://developer.samsung.com/tv/develop/extension-libraries/toast/) - 三星用于多平台电视应用程序开发的开源框架。
* [Enyo](http://enyojs.com) - LG 框架用于开发适用于所有主要平台（从手机和平板电脑到 PC 和电视）的应用程序。
* [Smartbox](https://github.com/immosmart/smartbox) - 适用于三星、LG、飞利浦、SmartTV Aliance、STB Mag 应用程序开发的智能电视通用库。
* [Mautilus Smart TV SDK](https://github.com/mautilus/sdk) - 用于开发电视应用程序的平台无关框架。支持三星、LG、飞利浦、索尼、松下和 VESTEL 智能电视。
* [BBC TAL](https://bbc.github.io/tal/) - 由 BBC 工程师开发的用于构建智能电视应用程序的开源库。
* [PureQML TV](https://github.com/pureqml/qmlcore-tv) - 用于基于 Web 的 SmartTV/STB 平台的声明性前端框架。已实验性支持 Android TV。
* [ZombieBox](https://github.com/interfaced/zombiebox) - 开源智能电视框架。强类型 JavaScript、基于组件、内置 D-PAD 导航管理、适用于所有平台的具有 DRM 的抽象视频 API。支持许多平台，如 Tizen、webOS、Android TV 等。

## 远程控制协议
* [DLNA](https://en.wikipedia.org/wiki/Digital_Living_Network_Alliance) - 通过家庭网络共享数据的行业标准。根据您拥有的 DLNA 兼容设备，您也许能够将电影从笔记本电脑流式传输到电视，通过高保真系统播放手机上存储的 MP3，或者在家用打印机上打印平板电脑上的照片。
* [DIAL](http://www.dial-multiscreen.org/) - 该协议由 Netflix 和 Google 开发，允许客户端设备（如智能手机、平板电脑或计算机）发现服务器设备（如智能电视或流媒体盒）上的应用程序并在其上启动内容。
* [Wi-Fi Direct](https://en.wikipedia.org/wiki/Wi-Fi_Direct) - 标准使设备能够轻松地相互连接，而无需无线接入点。
* [Miracast](https://en.wikipedia.org/wiki/Miracast) - 从设备（例如笔记本电脑、平板电脑或智能手机）到显示器（例如电视、显示器或投影仪）的无线连接标准。通过 Wi-Fi Direct 工作。

## 跨平台工具
* [smartest-tv](https://github.com/Hybirdss/smartest-tv) - CLI 和 MCP 服务器，用于在任何智能电视上按名称播放 Netflix、YouTube 和 Spotify。深度链接 LG、三星、Android TV 和 Roku 上的内容 — 说“Frieren S2E8”，它就会播放 (Python)。
* [Fluxcast](https://github.com/IlyaP358/fluxcast) - 一个用户友好的 Python 实用程序，用于通过 Miracast 和 DLNA 将 Linux 桌面镜像到智能电视，支持 GNOME、KDE ​​和 wlroots/Wayland。

## 导航库
* [lrud](https://github.com/stuart-williams/lrud) - 左、右、上、下。用于通过方向控制进行输入的设备的空间导航库。
* [js-spatial-navigation](https://github.com/luke-chang/js-spatial-navigation) - 基于 JavaScript 的空间导航实现。
* [react-js-spatial-navigation](https://github.com/dead/react-js-spatial-navigation) - js-spatial-navigation 的包装器，用于响应组件。
* [react-key-navigation](https://github.com/dead/react-key-navigation) - React 的空间导航组件。类似于 [BBC TAL](https://bbc.github.io/tal/) 的[“焦点管理”](http://bbc.github.io/tal/widgets/focus-management.html)。
* [react-spatial-navigation](https://github.com/NoriginMedia/react-spatial-navigation) - React 的基于 HOC 的空间导航（按键导航）解决方案。

## 测试
* [Suitest](https://suite.st) - 智能电视、游戏机、流媒体棒等的测试自动化解决方案。
* [stb-tester](https://github.com/stb-tester/stb-tester) - 机顶盒和智能电视的自动化用户界面测试 (python)。

## 杂项
* [LIRC](http://lirc.org) - 该软件包允许您解码和发送许多（但不是全部）常用遥控器的红外信号。
* [awesome-smarttv](https://github.com/linuxenko/awesome-smarttv) - 另一个智能电视资源列表。在这一项已经完成后发现:roll_eyes:。
* [docker-tizen-webos-sdk](https://github.com/vitalets/docker-tizen-webos-sdk) - 使用 Samsung Tizen CLI 和 LG webOS CLI 的 Docker 映像。允许开发、构建、启动和调试智能电视应用程序，而无需安装 Tizen Studio 和 webOS SDK。

## 社区
* [堆栈溢出](http://stackoverflow.com/questions/tagged/smart-tv)
* [Reddit](https://www.reddit.com/r/smarttv)

## 贡献
欢迎通过创建[新问题](https://github.com/vitalets/awesome-smart-tv/issues)或[拉取请求](https://github.com/vitalets/awesome-smart-tv/pulls)来分享您的经验并贡献有用的扩展资源。
请先阅读[贡献指南](CONTRIBUTING.md)。谢谢！

## 执照
[![CC0](http://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)
