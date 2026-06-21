# 很棒的树莓派

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
[![All Contributors](https://img.shields.io/badge/all_contributors-43-orange.svg)](https://github.com/thibmaek/awesome-raspberry-pi/blob/main/CONTRIBUTORS.md)

<a href="https://www.raspberrypi.org"><img src="https://www.raspberrypi.org/wp-content/uploads/2012/03/raspberry-pi-logo.png" alt="Raspberry Pi Logo" align="left" style="margin-right: 25px" height=150></a>

> Raspberry Pi 是由 Raspberry Pi 基金会在英国开发的一系列信用卡大小的单板计算机，旨在促进学校和发展中国家的基础计算机科学教学。官方链接：[Raspberry Pi 基金会主页](https://raspberrypi.org)、[Raspberry Pi 计算机主页](https://www.raspberrypi.com)

此列表是符合 [Awesome Manifesto](https://github.com/sindresorhus/awesome/blob/main/awesome.md) 的工具、项目、图像和资源的集合

贡献*非常欢迎*但首先看到[贡献](#contributing)

## 内容

- [Models](#models)
- [操作系统映像](#os-images)
- [Tools](#tools)
- [Projects](#projects)
- [Resources](#resources)

## 型号

完整的（消费级）Raspberry Pi 型号系列包括：

- Raspberry Pi 1、型号 A 和型号 B（2012 年，已停产）
- [Raspberry Pi 1，型号 B+](https://www.raspberrypi.org/products/raspberry-pi-1-model-b-plus/)（2014 年 7 月）
- [Raspberry Pi 1，型号 A+](https://www.raspberrypi.org/products/raspberry-pi-1-model-a-plus/)（2014 年 11 月）
- [Raspberry Pi 2，型号 B](https://www.raspberrypi.org/products/raspberry-pi-2-model-b/)（2015 年 2 月）
- [Raspberry Pi Zero](https://www.raspberrypi.org/products/raspberry-pi-zero/)（2015 年 11 月）
- [Raspberry Pi 3，型号 B](https://www.raspberrypi.org/products/raspberry-pi-3-model-b/)（2016 年 3 月）
- [Raspberry Pi Zero W](https://www.raspberrypi.org/products/raspberry-pi-zero-w/)（2017 年 2 月）
- [Raspberry Pi 3，型号 B+](https://www.raspberrypi.org/products/raspberry-pi-3-model-b-plus/)（2018 年 3 月）
- [Raspberry Pi 3，型号 A+](https://www.raspberrypi.org/products/raspberry-pi-3-model-a-plus/)（2018 年 11 月）
- [Raspberry Pi 4，型号 B](https://www.raspberrypi.org/products/raspberry-pi-4-model-b/)（2019 年 6 月）
- [Raspberry Pi 5](https://www.raspberrypi.com/products/raspberry-pi-5/)（2023 年 10 月）
- [Raspberry Pi 400](https://www.raspberrypi.org/products/raspberry-pi-400/)（2020 年 11 月）
- [Raspberry Pi 500](https://www.raspberrypi.com/products/raspberry-pi-500/)（2024 年 12 月）
- [Raspberry Pi 500+](https://www.raspberrypi.com/products/raspberry-pi-500-plus/)（2025 年 9 月）
- [Raspberry Pi Pico](https://www.raspberrypi.com/products/raspberry-pi-pico/?variant=raspberry-pi-pico)（2021 年 1 月）
- [Raspberry Pi Pico 2](https://www.raspberrypi.com/products/raspberry-pi-pico-2/)（2024 年 8 月）
- [Raspberry Pi Zero 2 W](https://www.raspberrypi.com/products/raspberry-pi-zero-2-w/)（2021 年 10 月）
- [Raspberry Pi Pico W](https://www.raspberrypi.com/products/raspberry-pi-pico/?variant=raspberry-pi-pico-w)（2022 年 6 月）

## 操作系统映像

- [Alpine Linux](https://wiki.alpinelinux.org/wiki/Raspberry_Pi) - 基于 musl libc 和 busybox 的面向安全的轻量级 Linux 发行版。
- [Anthias](https://anthias.screenly.io/) - 世界上最受欢迎的开源数字标牌项目。
- [Arch Linux ARM](https://archlinuxarm.org/) - 轻量且灵活的 Linux 发行版力求保持简单。
- [Armbian](https://www.armbian.com/rpi4b/) - 一个用于单板计算机 (SBC) 的基本操作系统平台，其他项目可以信任在此基础上进行构建。
- [balenaOS](https://www.balena.io/os/) - 用于在嵌入式设备上运行 Docker 容器的开源操作系统，其设计旨在提高可靠性并在生产中得到验证。
- [BerryBoot](http://www.berryterminal.com/doku.php/berryboot) - 引导加载程序/通用操作系统安装程序，支持 VNC 和 HDMI-CEC。
- [chilipie-kiosk](https://github.com/futurice/chilipie-kiosk) - 直接启动进入全屏 Chrome 的图像，非常适合仪表板和构建监视器。 ![支持树莓派2+](/media/badges/rpi-2+.png)
- [Channels DVR Server](https://getchannels.com/raspberry-pi/) - Channels DVR 服务器的自定义映像，提供整个家庭 DVR 系统。
- [Debian](https://raspi.debian.net) - Raspberry Pi 的非官方 Debian 映像（由 Debian 开发人员维护）。
- [DietPi](https://github.com/Fourdee/DietPi) - 最小的图像设计适合 2GB SD 卡，具有大量可配置的设置和脚本。
- [DroneBridge](https://github.com/seeul8er/DroneBridge) - WifiBroadcast 扩展，可真正替代 DJI Lightbridge 和其他类似系统。 ![支持树莓派3](/media/badges/rpi-3.png)
- [EZ-WifiBroadcast](https://github.com/bortek/EZ-WifiBroadcast/wiki) - 经济实惠的无线数字高清视频传输变得简单。 ![支持 Raspberry Pi 3](/media/badges/rpi-3.png) ![支持 Raspberry Pi Zero](/media/badges/rpi-0.png)
- [Fedora](https://fedoraproject.org/wiki/Raspberry_Pi#Preparing_the_SD_card) - 为 Pi 构建的 Linux Fedora 发行版。 ![支持树莓派2+](/media/badges/rpi-2+.png)
- [FreeBSD](https://wiki.freebsd.org/arm/Raspberry%20Pi) - FreeBSD 是一种先进的计算机操作系统，用于为现代服务器、台式机和嵌入式平台提供支持。
- [FreedomBox](https://www.freedombox.org) - FreedomBox 是一款面向非专家的私人家庭服务器。 ![支持树莓派2+](/media/badges/rpi-2+.png)
- [Gentoo](https://wiki.gentoo.org/wiki/Raspberry_Pi) - 适用于 Raspberry Pi 的 Gentoo Stage 3 tarball。
- [Gladys Assistant](https://gladysassistant.com) - Gladys，隐私第一的开源家庭助理。 ![支持树莓派3](/media/badges/rpi-3.png)
- [GlowBarn OS](https://github.com/bad-antics/glowbarn-os) - 基于 Buildroot 的 Linux 发行版，用于通过 EMF 传感器、环境监测、网络仪表板和自动数据记录进行超自然现象研究。 ![支持树莓派4+](/media/badges/rpi-4.png)
- [HamPi](https://sourceforge.net/projects/hampi/) - 以前称为 Ham Radio 的 W3DJS Raspberry Pi。
- [Hass.io](https://home-assistant.io/hassio/installation/) - 适用于嵌入式设备的家庭自动化操作系统/应用程序，也可独立使用。
- [HypriotOS](http://blog.hypriot.com/about/) - 基于 Debian 的最小操作系统，针对运行 Docker 进行了优化。
- [Kali Linux](https://www.offensive-security.com/kali-linux-arm-images/) - 适用于 ARM 设备的渗透测试和道德黑客 Linux 发行版。
- [KonstaKANG](https://konstakang.com/devices/rpi4/) - 专为 Raspberry Pi 构建的非官方 LineageOS 和 AOSP。 ![支持树莓派3](/media/badges/rpi-3.png)
- [Lakka](http://lakka.tv) - Raspberry Pi 上的复古游戏完全基于 RetroArch 构建。
- [LibreELEC](https://libreelec.tv/) - 足以运行 Kodi 的操作系统
- [Mainsail OS](https://github.com/mainsail-crew/MainsailOS) - 3D 打印机发行版，包含 Klipper 固件和 Mainsail 入门所需的一切内容。
- [Manjaro](https://manjaro.org/download/) - 适用于 Raspberry Pi 的友好开源 Linux 发行版。
- [Minibian](https://minibianpi.wordpress.com/) - 最小的 Raspbian（比 Jessie Lite 轻）。
- [moOde](https://moodeaudio.org/) - moOde 音频播放器可充当发烧友流媒体播放器，为旧接收器提供 DLNS、Spotify Connect 和 AirPlay 支持。 ![支持 Raspberry Pi 3](/media/badges/rpi-2+.png) ![支持 Raspberry Pi Zero](/media/badges/rpi-0.png)
- [MoodleBox](https://moodlebox.net/) - MoodleBox 在 Raspberry Pi 上提供了 Moodle 学习管理系统。 ![支持树莓派3](/media/badges/rpi-3.png)
- [motionEyeOS](https://github.com/ccrisan/motioneyeos/wiki) - 将单板计算机转变为视频监控系统的 Linux 发行版。
- [NetBSD](https://wiki.netbsd.org/ports/evbarm/raspberry_pi/) - NetBSD 是一个免费、快速、安全且高度可移植的类 Unix 开源操作系统。
- [NextCloudPi](https://github.com/nextcloud/nextcloudpi) - 基于 Raspbian 的 Nextcloud 就绪镜像。具有在 Raspbian 8 上运行的 Nextcloud 11，以及支持 PHP 7 和 HTTP2 的 Apache 服务器。
- [NOOBS](https://www.raspberrypi.org/downloads/noobs/) - 新的开箱即用软件，适合初学者的简单操作系统安装程序。
- [OctoPi](https://octopi.octoprint.org/) - 3D 打印机分销。
- [OpenHABian](https://www.openhab.org/docs/installation/openhabian.html) - OpenHAB 家庭自动化软件的预配置版本。 ![支持树莓派2+](/media/badges/rpi-2+.png)
- [OpenMediaVault](https://www.openmediavault.org/) - OpenMediaVault 是基于 Debian Linux 的下一代网络附加存储 (NAS) 解决方案，包含 SSH、(S)FTP、SMB/CIFS、DAAP 媒体服务器、RSync、BitTorrent 客户端等服务。 ![支持树莓派3](/media/badges/rpi-3.png)
- [openSUSE](https://en.opensuse.org/HCL:Raspberry_Pi) - openSUSE 是一个主要的 Linux 发行版，其镜像基于其稳定版本 Leap 和滚动版本 Tumbleweed。可以找到许多 Pi 的图像，包括 [Raspberry Pi 3](https://en.opensuse.org/HCL:Raspberry_Pi3) 和 [Raspberry Pi 4](https://en.opensuse.org/HCL:Raspberry_Pi4)。
- [OpenWRT](https://openwrt.org/toh/raspberry_pi_foundation/raspberry_pi) - OpenWrt 被描述为用于嵌入式设备网络管理的 Linux 发行版。
- [OSMC](https://osmc.tv/) - 基于 Kodi 的开源媒体中心。
- [PiDeck](http://pideck.com/) - 小型 DVS 系统允许您使用时间码黑胶唱片控制数字音乐文件。
- [PiFi](https://pifi.org) - 在几秒钟内将 Raspberry Pi 变成高速 VPN 路由器⚡️（支持 Raspberry Pi 4 和 5）。
- [PiNet](http://pinet.org.uk/) - 管理 Raspberry Pi 教室的系统。
- [PirateBox](https://piratebox.cc/doku.php?id=raspberry_pi:diy) - 匿名离线移动文件共享和通信系统。
- [RasComm RaspberryPi MorseCode Translator](https://github.com/Defcon27/RasComm-RaspberryPi-MorseCode-Translator) - RasComm 是一种将纯文本以视觉或听觉方式转换为摩尔斯电码 (IMC) 的通信设备。
- [Raspberry Pi OS](https://www.raspberrypi.org/downloads/) - 官方支持 Raspberry Pi 操作系统（以前称为“Raspbian”），基于 Debian，并提供精简版本。
- [Raspbian](http://www.raspbian.org/) - Raspbian 是一个基于 Debian 的免费操作系统，针对 Raspberry Pi 硬件进行了优化。
- [RasPlex](http://www.rasplex.com/) - Raspberry Pi 的 Plex 客户端。
- [Recalbox](https://www.recalbox.com) - 将轻量级复古游戏和媒体中心拖放到 Raspberry Pi 上。
- [RetroPie](https://retropie.org.uk/) - 在 Raspberry Pi 上进行复古游戏。
- [Risc OS](https://www.riscosopen.org/content/downloads/raspberry-pi) - 非Linux操作系统起源于开发ARM微处理器的小组。
- [Rocket Show](https://rocketshow.net) - 在舞台上实时播放同步背景音乐、视频和 DMX 灯光序列。 ![支持树莓派3](/media/badges/rpi-3.png)
- [RuneAudio](http://www.runeaudio.com/) - 免费开源操作系统，可将嵌入式硬件转变为 Hi-Fi 音乐播放器。
- [SamplerBox](http://www.samplerbox.org/makeitsoftware) - Drop'n'play 采样器：将 .WAV 样本放到 SD 卡上，然后播放！
- [Twister OS](https://twisteros.com/) - Raspberry Pi 操作系统的皮肤版本，预装了 box86 和 Retropie 等应用程序，向新手介绍 Linux 和 Raspberry Pi。 ![支持树莓派3](/media/badges/rpi-3.png)
- [Ubuntu Core](https://ubuntu.com/download/raspberry-pi-core) - IoT 的官方（最小）Ubuntu 发行版。支持Raspberry Pi Zero 2 W。![支持Raspberry Pi 2+](/media/badges/rpi-2+.png)
- [Ubuntu Desktop](https://ubuntu.com/raspberry-pi/desktop) - 适用于 Raspberry Pi 的 Ubuntu 桌面发行版。支持树莓派 4 和 5。
- [Ubuntu MATE](https://ubuntu-mate.org/raspberry-pi/) - 基于 MATE 桌面的 Raspberry Pi 的 Ubuntu 发行版。 ![支持树莓派2+](/media/badges/rpi-2+.png)
- [Ubuntu Server](https://ubuntu.com/raspberry-pi/server) - 适用于 Raspberry Pi 的 Ubuntu 服务器发行版。支持Raspberry Pi Zero 2 W。![支持Raspberry Pi 2+](/media/badges/rpi-2+.png)
- [Volumio](https://volumio.org/) - 无头发烧级音乐播放器，旨在以尽可能高的保真度播放音乐。
- [Windows 10 IoT Core](https://docs.microsoft.com/nl-nl/windows/iot-core/downloads) - 适用于 IoT 的 Windows 10 发行版。 ![支持树莓派2+](/media/badges/rpi-2+.png)

## 工具

- [Alpha](https://github.com/farjump/raspberry-pi) - 通过此系统级 GDB 服务器使用 GDB 远程加载、调试和测试裸机程序。
- [ApplePi Baker](https://www.tweaking4all.com/hardware/raspberry-pi/applepi-baker-v2/) - macOS 应用程序可轻松将图像安装/备份/恢复到 SD 卡上。
- [Armbian Imager](https://imager.armbian.com) - 一款开源映像工具，可轻松安装 Armbian OS。
- [Atlas toolkit](https://github.com/epeios-q37/atlas-python) - 非常轻量且易于安装的工具包，可使用 Python 编写单页 Web 应用程序来试用您的 RPi，而无需安装 Web 服务器。
- [balenaEtcher](https://www.balena.io/etcher/) - SD 卡刻录应用程序对最终用户来说很简单，对开发人员来说可扩展，并且可以在任何平台上运行。
- [n01d-forge](https://github.com/bad-antics/n01d-forge) - 具有 LUKS/VeraCrypt 加密支持的原生 Rust 映像刻录器，非常适合为 Raspberry Pi 创建安全的可启动 SD 卡。
- [Drago](https://seashell.github.io/drago) - 适用于 Wireguard 网络的灵活配置管理器，非常适合建立跨多个 Raspberry Pi 的安全覆盖。
- [Embedible](https://embedible.io/) - 人工智能可将您的电子创意转化为可行的 Raspberry Pi Pico 项目。
- [Hardened Kernel Builder for RPi](https://github.com/tschaffter/raspberry-pi-kernel-hardened) - 使用单个命令交叉编译适用于 Raspberry Pi 的 Linux 内核，增强安全性。
- [HealthyPi](https://github.com/Protocentral/protocentral-healthypi-v3) - HAT 包括重要的健康监测，如心电图、呼吸、脉搏血氧饱和度以及可选的血压和体温传感。 ![支持树莓派2+](/media/badges/rpi-2+.png)
- [iotwifi](https://github.com/cjimti/iotwifi) - 8MB [Docker 容器](https://hub.docker.com/r/cjimti/iotwifi/) 中的 Wifi AP + 客户端管理，具有用于同时控制 wifi 客户端和工作站模式的 REST API。 ![支持树莓派3](/media/badges/rpi-3.png)
- [ndm](https://github.com/gitbls/ndm) - 用于轻松管理 DNS 和 DHCP 服务器的命令行工具。
- [Orangetool](https://github.com/Moduland/Orangetool) - Python 中单板计算机的控制功能。
- [OSMC Installer](https://osmc.tv/download/) - 基于 GUI 的实用程序，用于将 OSMC 下载并安装到各种平台上。
- [Pi Temperature Exporter](https://github.com/s-nagaev/pi-temperature-exporter) - 用于 Prometheus 消耗的 CPU 和 GPU 温度导出器。
- [pi-gen](https://github.com/RPi-Distro/pi-gen) - 用于创建 raspberrypi.org Raspbian 映像的工具。这可用于创建您自己的自定义映像并安装特定的软件包等。
- [Raspberry Pi GPIO Pinout](https://raspberry.tips/en/raspberry-pi-gpio-pinout) - 所有 40 个 GPIO 引脚的交互式引脚排列参考，包括 BCM 编号、功能、电压规格和 HAT 覆盖。针对 Pi 5（RP1 控制器）进行了更新。
- [Raspberry Pi SD Card Lifespan Calculator](https://raspberry.tips/en/calculate-raspberry-pi-sd-card-lifespan-test-now) - 交互式工具可根据 P/E 周期和写入放大系数 (WAF) 估计 SD 卡何时出现故障。
- [Pieman](https://github.com/tolstoyevsky/pieman) - 用于创建基于 Raspbian、Devuan、Ubuntu 和 Alpine Linux 的自定义映像的脚本。
- [PiKISS](https://github.com/jmcerrejon/PiKISS) - 一堆带菜单的脚本，让您的生活更轻松。
- [Pimod](https://github.com/Nature40/pimod) - 使用简单的、类似 Docker 的配置文件重新配置 Raspberry Pi 映像。
- [PiShrink](https://github.com/Drewsif/PiShrink/) - Bash 脚本会自动缩小 pi 映像，然后在启动时将其大小调整为 SD 卡的最大大小。
- [pistrong](https://github.com/gitbls/pistrong) - 管理受证书保护的 StrongSwan VPN。适用于客户端-服务器、站点到站点和主机到主机 VPN 的安装程序和命令行工具。
- [PiVPN](https://pivpn.io) - 使用单个 bash 命令创建功能齐全的 OpenVPN/WireGuard VPN 服务器。
- [PiGro](https://github.com/actionschnitzel/PiGro-Aid-) - PiGro 执行许多命令，这些命令必须通过单击一两次按钮通过终端输入。
- [Pi-Apps](https://github.com/Botspot/pi-apps) - Raspberry Pi 计算机上最受欢迎的应用程序商店，100% 开源 bash 脚本。
- [Processing](https://pi.processing.org/get-started/) - 在 Raspberry Pi 上运行的处理开发环境。
- [Pwnagotchi](https://github.com/evilsocket/pwnagotchi) - Pwnagotchi 是一款基于 AI 的 Wi-Fi 破解工具，可以从周围的 WiFi 环境中学习，以最大限度地利用其捕获的可破解 WPA 密钥材料。
- [RaspAP-webgui](https://github.com/billz/raspap-webgui) - 一个简单、响应式的 Web 界面，用于控制 Raspberry Pi 上的 wifi、hostapd 和相关服务。
- [Raspberry Pi Imager](https://www.raspberrypi.org/blog/raspberry-pi-imager-imaging-utility/) - 将 Raspberry Pi 操作系统和其他操作系统安装到可与 Raspberry Pi 一起使用的 SD 卡的简单方法
- [Raspbian QEMU with network](https://ownyourbits.com/2017/02/06/raspbian-on-qemu-with-network-access/) - 在 Raspbian 上启动 QEMU 的简单工具，并对系统和内核进行所需的修改。自动网络访问。方便在您的电脑中创建图像。
- [Resin Bridge](https://github.com/resin-io-playground/resin-bridge) - 简单的应用程序/存储库，用于将 Raspberry Pi 的 wlan0 接口桥接到通过以太网 (eth0) 插入的设备。
- [RPi Monitor Dashboard](https://github.com/nekromoff/rpi-monitor-dashboard) - 带有仪表板的简单监控工具，适合监控多个 RPi 设备（CPU 温度、网络、ping、浏览器、X 显示屏幕截图等）。
- [Rpi MQTT Monitor](https://github.com/hjelev/rpi-mqtt-monitor) - 在 Home Assistant 中跟踪和控制 Raspberry Pi 或 Ubuntu 计算机系统健康状况和性能的最简单方法。
- [rpi-cookstrap](https://github.com/heeplr/rpi-cookstrap) - 一个轻量级、基于插件的面包店 shell 脚本框架，用于自定义、引导和配置树莓派操作系统磁盘映像。
- [sdm](https://github.com/gitbls/sdm) - 轻松、完全自定义 RasPiOS 映像。安装应用程序、配置设置等，然后从单个映像为许多不同的系统刻录 SSD/SD 卡，每个系统都会启动完全配置并准备好工作。或者玩。
- [stressberry](https://github.com/nschloe/stressberry) - 对 Raspberry Pi 进行压力测试并绘制温度。
- [TorTiPi](https://github.com/r0hi7/tortipi) - Shell 脚本可自动执行将 Raspberry Pi 转换为基于 Tor 的 WiFi 热点的任务。
- [WebStation SYSMON](https://github.com/t0xic0der/sysmon) - 直观的远程访问系统性能监控和任务管理工具，适用于服务器和无头 Raspberry Pi 设置。
- [WiFi config generator](https://steveedson.co.uk/tools/wpa/) - 使用 wifi 设置生成 wpa_supplicant.conf 文件的简单工具

## 项目

- [40-node Raspberry Pi Cluster](http://hackaday.com/2014/02/17/40-node-raspi-cluster/) - 集群的目标是小于全塔式桌面的大小。
- [AdGuard Home](https://github.com/AdguardTeam/AdGuardHome) - DNS 中继站，具有广告/跟踪器/其他拦截、IP 地址重定向和 DNS-over-HTTPS 功能。
- [BeeMonitor](https://beemonitor.org/setup/) - 蜂蜜蜂箱监控项目。
- [Bitcoin Tracker](https://github.com/jonathanrjpereira/Bitcoin-Bar) - 实时显示比特币统计数据的物理仪表板。 ![支持 Raspberry Pi 3](/media/badges/rpi-3.png) ![支持 Raspberry Pi Zero](/media/badges/rpi-0.png)
- [BlackRoad OS](https://blackroad.io) - 自托管边缘人工智能操作系统，在具有 Hailo-8 加速器、WireGuard 网状网络和自我修复自动化功能的 Raspberry Pi 5 集群上运行 52 TOPS 推理。
- [ble-scale-sync](https://github.com/KristianP26/ble-scale-sync) - 通过内置蓝牙读取 BLE 智能体重秤（23 个品牌），计算身体成分，并导出到 Garmin Connect、MQTT/Home Assistant、InfluxDB 等。 [网站](https://blescalesync.dev)。
- [BotWave](https://github.com/dpipstudio/botwave/) - 具有服务器-客户端架构的 FM 广播系统，用于远程管理多个 Raspberry Pi 发射器。 ![支持 Raspberry Pi Zero](/media/badges/rpi-0.png) ![支持 Raspberry Pi 2](/media/badges/rpi-2.png) ![支持 Raspberry Pi 3](/media/badges/rpi-3.png)
- [Building a Ceph Cluster on Raspberry Pi](http://bryanapperson.com/blog/the-definitive-guide-ceph-cluster-on-raspberry-pi/) - 高度冗余和低功耗 RADOS 家庭存储解决方案。
- [Building Timelapse with Resin](https://steveedson.co.uk/project-matilda/) - 使用 Docker、Resin 和 3G 互联网远程部署延时摄影机。
- [Cama-Camel Pack](https://github.com/Barqawiz/iot_watering_system) - 使用物联网实现高效植物护理的家庭灌溉系统。
- [Chromebook Charger Kiosk](https://www.reddit.com/r/raspberry_pi/comments/53nj1z/chromebook_charger_kiosk_last_minute_charge_for/) - 为在学校使用 Chromebook 的学生提供定时充电站。
- [Ceil](https://github.com/helmuthva/ceil) - 在裸机上运行 K8S 的自动配置 RPi 集群。 ![支持树莓派3](/media/badges/rpi-3.png)
- [Circle](https://github.com/rsta2/circle) - 适用于 Raspberry Pi 的 C++ 裸机环境。
- [clockOS](https://github.com/iGerli/clockOS) - 使用 Raspberry Pi 显示屏的简单智能桌面时钟。
- [CookCLI](https://github.com/cooklang/CookCLI) - 将您的 Raspberry Pi 变成自托管菜谱服务器。通过 Web UI、购物清单和膳食计划以纯文本 Cooklang 格式管理食谱。
- [CocktailMaker](https://github.com/alex9849/pi-cocktail-maker) - 先进的鸡尾酒制作机，可通过浏览器和触摸屏控制。
- [CocktailTDI](https://github.com/SimonWaldherr/CocktailTDI) - 另一台鸡尾酒机（由 Raspberry Pi 4、Golang、气动泵和阀门提供动力）。
- [Coder for Raspberry Pi](http://googlecreativelab.github.io/coder/) - Google 员工的一个开源项目，旨在将 Raspberry Pi 转变为简单、微型、个人网络服务器和基于网络的开发环境。
- [Display_Lib_RPI](https://github.com/gavinlyonsrepo/Display_Lib_RPI) - 一个共享的可安装 C++ 库，用于将各种电子显示器连接到 Raspberry Pi 单板计算机。
- [DIY Arcade Machine](https://github.com/SimonWaldherr/DIY-Arcade-Machine) - 一款复古风格的街机，基于 Raspberry Pi Pico、Hub75 LED 矩阵和其他一些东西（Wii Nunchucks、3D 打印零件……）
- [DIY USB Rubber Ducky](https://hackaday.io/project/17598-diy-usb-rubber-ducky) - Raspberry Pi Zero Rubber Ducky 几乎可以被任何带有 USB 端口的设备识别为 USB HID，从而允许您像键盘一样运行自定义脚本。 ![支持树莓派零](/media/badges/rpi-0.png)
- [docsis-cable-load-monitor](https://github.com/sp4rkie/docsis-cable-load-monitor) - 用于监控 DOCSIS 有线网络上下游负载的工具。
- [Drumbooth controller with touch interface](https://github.com/FDelporte/DrumBoothController) - 项目使用 Java、JavaFX、Pi4J 和 Arduino 来控制 8 个继电器和 LED 灯带。
- [FistBump BLE Edition](https://github.com/eliddell1/Project-Blue-Fist/blob/master/README.md) - WPA 哈希抓取蓝牙外设/Android 应用程序。
- [FruitNanny](https://ivadim.github.io/2017-08-21-fruitnanny/) - 婴儿监视器包括定制案例、服务器和客户端源代码。 ![支持树莓派3](/media/badges/rpi-3.png)
- [Gaussmeter](https://github.com/gaussmeter/gaussmeter) - 该项目利用 Raspberry Pi Zero W、WS2812B LED 和 Tesla API 来收集和显示 Tesla 的状态。 ![支持树莓派零](/media/badges/rpi-0.png)
- [Harry Potter and the real life Daily Prophet](https://www.raspberrypi.org/blog/harry-potter-and-the-real-life-daily-prophet/) - 使用 7 英寸 Raspberry Pi 显示屏模仿《哈利·波特》中的预言家日报。
- [Haven](https://github.com/havenweb/haven) - 在 Rasperry Pi 上托管私人博客，而不是使用 Facebook。
- [HookProbe](https://github.com/hookprobe/hookprobe) - 具有 eBPF/XDP 数据包过滤和 ML 威胁分类功能的 AI 原生入侵检测系统。在 Pi 5 上处理超过 880 万个安全事件。
- [Hearing aid prototoype](https://github.com/m-r-s/hearingaid-prototype) - Raspberry Pi 驱动的助听器原型。 ![支持树莓派3](/media/badges/rpi-3.png)
- [idle-less](https://github.com/tvup/idle-less) - 基于 Docker 的 nginx 反向代理，可通过 LAN 唤醒唤醒休眠服务器，非常适合节能的 Raspberry Pi 家庭实验室。
- [Internet Chronometer](https://github.com/rothman857/chronometer) - 将您的 Raspberry Pi 变成互联网计时器。
- [Jasper](https://jasperproject.github.io/) - 灵活的开源个人助理。
- [LocalKin](https://localkin.dev) - 适用于 Raspberry Pi 和边缘设备的 23MB 单二进制 AI 代理。自我锻造技能，用于自动硬件发现的创世协议（GPIO、I2C、USB、摄像头）、离线优先并支持 Ollama。
- [Kubernetes on ARM](https://github.com/luxas/kubernetes-on-arm) - 在不到十分钟的时间内让您的 ARM 设备启动并运行 Kubernetes。
- [Lomorage](https://github.com/lomorage/homepage) - Raspberry Pi 上的私人照片云主机，带有 Android/iOS/Web 客户端。
- [Looper/synth/drum thing](https://github.com/otem/Raspberry-Pi-Looper-synth-drum-thing) - 音序器/鼓垫，如 Native Instruments 的 Maschine for the Pi。
- [Lumos](https://www.instructables.com/id/LUMOS-Smart-Lamp-for-Better-Health/) - 智能灯，改善睡眠。 ![支持 Raspberry Pi 3](/media/badges/rpi-3.png) ![支持 Raspberry Pi Zero](/media/badges/rpi-0.png)
- [Magic Mirror](http://magicmirror.builders) - 独创开源模块化智能镜子平台。 ![支持树莓派2+](/media/badges/rpi-2+.png)
- [Mini OONTZ](https://cdn-learn.adafruit.com/downloads/pdf/mini-oontz-3d-printed-midi-controller.pdf) - 3D 打印迷你 MIDI 控制器。
- [Movel](https://github.com/stevelacy/movel) - 树莓派车载电脑。
- [Multi-Datacenter Cassandra on 32 Raspberry Pi’s](http://www.datastax.com/dev/blog/32-node-raspberry-pi-cassandra-cluster) - 使用 Raspberry Pi 集群板展示 Cassandra 始终在线、容错的特性。
- [NALIVATOR-9000](https://github.com/fote/nalivator9000) - 机器人调酒师，用于使用 Telegram-bot 界面和 Golang 上的语音合成来制作鸡尾酒。
- [Nerves Project](https://github.com/nerves-project) - 在 Elixir 中制作和部署防弹嵌入式软件。
- [Network Presence Detector](https://github.com/initialstate/pi-sensor-free-presence-detector/wiki) - 设置 Pi Zero 来扫描 WiFi 网络上的设备，并使用它来确定谁在“家里”。
- [NTP driven Nixie Clock](http://www.mjoldfield.com/atelier/2012/08/ntp-nixie.html) - 由 Raspberry Pi 供电的辉光管时钟。
- [Occu-Pi](https://github.com/bww/occu-pi) - Occu-pi 的控制器软件，这是一款非常棒的浴室门传感器。
- [P4wnP1](https://github.com/mame82/P4wnP1) - P4wnP1 是一个高度可定制的 USB 攻击平台，基于低成本 Raspberry Pi Zero 或 Raspberry Pi Zero W（HID 后门所需）。 ![支持树莓派零](/media/badges/rpi-0.png)
- [Pi Image Capturer](https://github.com/rajeshkumarkhadka/Pi-Image-Capturer) - 捕获图像，与 Google IOT 云平台生态系统集成。
- [pi_payments](https://github.com/anshulahuja98/pi_payments) - 基于RFID的支付模块。
- [Pi-hole](https://pi-hole.net/) - 互联网广告的黑洞。
- [Pi-KVM](https://github.com/pikvm/pikvm) - DIY KVM over IP 通过 Web UI 或 VNC 管理远程计算机，包括全高清视频、鼠标、虚拟驱动器、IPMI、LAN 唤醒和许多其他功能。
- [pi-timolo](https://github.com/pageauc/pi-timolo) - 来自 Rclone 远程存储服务等的远程无头多功能 PiCamera 操作。
- [Pi4j Project](http://pi4j.com) - Raspberry Pi 的 Java I/O 库。
- [PiAware](https://uk.flightaware.com/adsb/piaware/install) - 使用 Raspberry Pi 进行实时航班跟踪。
- [PiClock](https://github.com/n0bel/PiClock) - 围绕显示器和 Raspberry Pi 构建的精美时钟。
- [PiE-Ink](http://www.htxt.co.za/2017/02/07/pie-ink-is-a-raspberry-pi-name-tag-that-uses-an-e-ink-display/) - 在 Pi Zero 上运行的电子墨水名牌显示。 ![支持树莓派零](/media/badges/rpi-0.png)
- [PiFanTuner](https://github.com/winkidney/PIFanTuner) - CPU-fan-tuner 守护进程，仅根据需要启用风扇。 ![支持树莓派3](/media/badges/rpi-3.png)
- [PiFmRds](https://github.com/ChristopheJacquet/PiFmRds) - 使用 Raspberry Pi 的 FM-RDS 发射器。
- [PiScan](http://denis.papathanasiou.org/posts/2015.05.30.post.html) - 使用 Raspberry PI + EAN 扫描仪临时制作 Amazon Dash 订单。
- [PiSpot-Show](https://github.com/GeiserX/PiSpot-Show) - WiFi 优惠券显示系统具有天气集成和 PiJuice 电池管理功能。 ![支持树莓派3](/media/badges/rpi-3.png)
- [PiSpot Watch](https://github.com/GeiserX/PiSpot-Watch) - 腕戴式 Pi Zero 智能手表配有电子墨水显示屏，可通过按下按钮按需生成 Wi-Fi 优惠券代码。 ![支持树莓派零](/media/badges/rpi-0.png)
- [Planning lunch with a Slackbot on resin.io](https://resin.io/blog/planning-lunch-with-a-slackbot-on-resin-io/) - Node.js Slackbot（午餐机器人），托管在 Resin 上。
- [PoisonTap](https://github.com/samyk/poisontap) - 通过 USB 利用锁定/密码保护的计算机，删除基于 WebSocket 的持久后门，暴露内部路由器，并使用 Raspberry Pi Zero 和 Node.js 虹吸 cookie。 ![支持树莓派零](/media/badges/rpi-0.png)
- [Power Sniffing Strip](https://hackaday.com/2012/10/04/malicious-raspberry-pi-power-strip-looks-a-bit-scary/) - 配电盘中的外壳，嗅探网络数据。
- [Project MyHouse](https://maxoffsky.com/research-progress/project-myhouse-a-smart-dollhouse-with-gesture-recognition/) - 具有手势识别功能的智能娃娃屋，使用 Raspberry Pi 3 或 Pi Zero 和 PSMove 运动控制器。
- [Raspberry Pi Dashboard](https://github.com/femto-code/Raspberry-Pi-Dashboard) - 功能齐全的基于网络的仪表板界面，用于检查和管理 Raspberry Pi 硬件和软件，无需额外的软件。
- [Raspberry Pi Erlang Cluster](https://medium.com/@pieterjan_m/erlang-pi2-arm-cluster-vs-xeon-vm-40871d35d356#.bpao66cm8) - Raspberry Pi 2 上的 Erlang 集群。
- [Raspberry PI Hadoop Cluster](http://www.widriksson.com/raspberry-pi-hadoop-cluster/) - 运行在 Raspberry Pi 上的大数据集群。
- [Raspberry Pi Setup](https://github.com/atao/raspberrypi-setup) - ⚡ 快速设置我的 Raspberry Pi。
- [Raspberry Pi Telegram Bot](https://github.com/GraveEaterMadison/Raspberry_pi_telegram_bot) - 使用 Telegram 远程控制您的 Raspberry Pi，支持 GPIO、系统命令、自定义模块和实时交互。
- [RaspiBlitz](https://github.com/rootzoll/raspiblitz) - 让您自己的闪电节点运行的最快且最便宜的方式。
- [RaspiBolt](https://raspibolt.org/) - Raspberry Pi 上的️⚡Lightning️⚡初学者指南。
- [Receiving GOES-16 Images on a Raspberry Pi](https://gist.github.com/lxe/c1756ca659c3b78414149a3ea723eae2#file-goes16-rtlsdr-md) - 这是一个使用软件定义无线电 (SDR) 从 GOES-16 卫星接收天气图像的高级项目。
- [Relayboard Control](https://github.com/leinir/relayboard-control) - 用于将 Waveshare 8 通道中继板连接到 MQTT 服务器的 Qt 应用程序。
- [RGB-LED-Matrix](https://github.com/SimonWaldherr/RGB-LED-Matrix) - 128x128 像素 RGB LED 矩阵，用于显示图像、动画、康威生命游戏和其他内容。
- [Rhasspy](https://rhasspy.readthedocs.io) - 一套完全离线的开源语音助手服务，可与 Home Assistant、Node-RED、MQTT 等完美配合。
- [RPi-eth-display](https://pierre-couy.dev/tinkering/2023/03/turning-rpi-into-external-monitor-driver.html) - 开源 DisplayLink 替代方案，以太网转 HDMI 适配器。
- [RPi Motor Library](https://github.com/gavinlyonsrepo/RpiMotorLib) - 用于将各种电机和伺服系统连接到 Pi 的 Python 3 库。
- [RPI tempmon](https://github.com/gavinlyonsrepo/raspberrypi_tempmon) - CPU GPU 温度监控器具有多种功能，如 LED GPIO、图形输出、电子邮件、警报限制、通知和日志记录。
- [SecPi](https://github.com/SecPi/SecPi) - 基于 Raspberry Pi 的家庭报警系统。
- [Skate-o-Meter](http://www.instructables.com/id/Skate-o-Meter/) - 带有 RFID 用户系统的滑板里程表和速度表。
- [SkyJack](https://samy.pl/skyjack/) - 接管并完全控制无线距离内的任何 Parrot AR 无人机。
- [Smart Mirror](https://github.com/evancohen/smart-mirror) - 具有物联网集成的语音控制智能镜子。 ![支持树莓派2+](/media/badges/rpi-2+.png)
- [Smart Security Camera](https://www.pyimagesearch.com/2019/03/25/building-a-raspberry-pi-security-camera-with-opencv/) - 使用 OpenCV、Twilio 和网络摄像头/picam。
- [Sonic Pi](https://github.com/samaaron/sonic-pi) - 适合所有人的现场编码音乐合成器。
- [Sonus](https://github.com/evancohen/sonus) - Node.js 语音控制您的 Pi（以及其他一切），具有可定制的离线热词检测功能。
- [speed-camera](https://github.com/pageauc/speed-camera) - 对象运动跟踪使用 python、openCV、USB Cam 或 picamera 模块来记录速度数据。
- [Stratux](https://github.com/cyoung/stratux) - 开源 ADS-B 接收器，可通过 WiFi 将天气、交通、GPS 和 AHRS 数据传输至电子飞行包软件。
- [StreamPi](https://stream-pi.com/) - Elgato Stream Deck 的强大替代品，可以启动应用程序、脚本、网站和 OBS 等控制应用程序。
- [TelePi](https://github.com/besoeasy/telepi) - Telepi 允许您通过 Telegram 监视和控制您的 Raspberry Pi，具有文件下载、系统监视、网络洞察、速度测试以及打开 Web 隧道的功能。
- [TeslaCam](https://github.com/LelandSindt/teslacam) - 项目利用 Raspberry Pi Zero W 进行 USB 大容量存储模拟，并使用 PiJuice 来收集和存档 TeslaCam 视频。 ![支持树莓派零](/media/badges/rpi-0.png)
- [Ultimate DNS Shield](https://github.com/cherifon/Ultimate-DNS-Shield) - 在 Raspberry Pi 4 上使用 Pi-hole、Unbound 和 Docker 的自托管递归 DNS 服务器。
- [USB Proxy](https://github.com/AristoChen/usb-proxy) - 一个 USB 中间人项目，允许用户监视和修改主机和设备之间的 USB 数据包流。
- [Vinyl Shelf Finder](https://valentingalea.github.io/vinyl-shelf-finder/) - 使用倾斜和平移激光在唱片集中查找唱片。
- [Voice Kit](https://aiyprojects.withgoogle.com/voice) - 来自 Google 的 AIY Voice Kit，可使用 Google Assistant 构建独立的语音识别系统，或将语音识别和自然语言处理添加到基于 Raspberry Pi 的项目中。
- [Waves](https://github.com/euniceylee/waves) - 通过麦克风、波形和热敏打印机将口头语言的短暂性转化为具体和物理的东西。
- [Whispering Mirror](http://whisperingwallproject.com/whisperingmirror/) - 使用 Hi Fiberry DAC 的交互式声音艺术装置。
- [Wordpress using Docker](https://github.com/rothgar/rpi-wordpress) - 在具有动态 DNS 的容器中运行 WordPress 站点。
- [Zelda Home Automation](https://www.raspberrypi.org/blog/zelda-home-automation/) - 基于陶笛演奏音符的声音识别的家庭自动化。

## 资源

### 有用的应用程序

#### 安卓

- **AndFTP** - 替代 FTP 客户端应用程序。 [Android](https://play.google.com/store/apps/details?id=lysesoft.andftp)
- **EtchDroid** - 是一个开源应用程序，可将磁盘映像写入 USB 驱动器。 [Android](https://play.google.com/store/apps/details?id=eu.depau.etchdroid)
- **Kore Remote** - 控制 Kodi 的官方遥控器。 [Android](https://play.google.com/store/apps/details?id=org.xbmc.kore)
- **PiGo** - 轻松地随时随地探索和管理多个 Pi 服务器。 [Android](https://play.google.com/store/apps/details?id=com.tejasgajjar.pigo)
- **RaspController** - 远程管理您的 Raspberry Pi、控制 GPIO 端口、直接通过终端发送命令、查看连接的摄像头的图像并从不同的传感器获取数据。 [Android](https://play.google.com/store/apps/details?id=it.Ettore.raspcontroller)
- **Raspicast** - 从 Android 设备投射 YouTube 视频、媒体内容，播放本地媒体文件，在 Raspberry Pi 上播放播放列表（m3u，请）中的流。 [Android](https://play.google.com/store/apps/details?id=at.huber.raspicast)
- **屏幕流镜像** - 将手机屏幕直接流式传输到 Pi。 [Android](https://play.google.com/store/apps/details?id=com.mobzapp.screenstream.Trial)
- **TeamViewer** - 在路上时远程访问 Raspberry Pi！ [Android](https://play.google.com/store/apps/details?id=com.teamviewer.teamviewer.market.mobile)
- **Termius** - 最干净的 Pi SSH 客户端之一。 [Android](https://play.google.com/store/apps/details?id=com.server.auditor.ssh.client)，[iOS](https://itunes.apple.com/us/app/termius-ssh-shell-console-terminal/id549039908?mt=8)
- **Tubio** - 将网络视频直接投射到 Pi。 [Android](https://play.google.com/store/apps/details?id=com.aesoftware.tubio)
- **Turbo FTP** - 一个很好的 FTP 客户端应用程序，用于访问树莓派上的文件。 [Android](https://play.google.com/store/apps/details?id=turbo.client)
- **VNC Viewer** - 远程控制 Raspberry Pi 桌面。 [Android](https://play.google.com/store/apps/details?id=com.realvnc.viewer.android&hl=en)

#### iOS系统

- **RaspController** - 允许您轻松远程管理您的 Raspberry Pi、控制 GPIO 端口、直接通过终端发送命令等等。 [iOS](https://apps.apple.com/app/raspcontroller/id1584315865)

### 文章

- [10 Years of Raspberry Pi](https://kandi.openweaver.com/collections/educational-service-providers/10-years-of-raspberry-pi) - Raspberry Pi 10 年的集合，展示了爱好者用例、家庭自动化、物联网、操作系统和实用程序中最受欢迎的库。
- [Raspberry Pi A to Z List](https://github.com/wtsxDev/Raspberry-Pi) - 包含常见问题和陷阱链接的综合列表。
- [Raspberry Pi and why do I need one?](https://www.liquidlight.co.uk/blog/article/raspberry-pi-what-is-it-and-why-do-i-need-one/) - 介绍 Raspberry Pi 以及可以用它做什么。
- [Raspberry Pi Beginners](https://medium.com/@anshul.ahu/how-to-setup-raspberry-pi-for-beginners-aeedc2cb994a) - 初学者设置 Raspberry Pi 的指南。
- [The Ultimate Raspberry Pi Security Guide](http://www.nhatqbui.com/assets/TheUltimateRaspberryPiSecurityGuide.pdf) - 有关 Pi ie 安全最佳实践的广泛指南。暴露在互联网上。


### 书籍

- [Control Your Home with Raspberry Pi](https://koen.vervloesem.eu/books/control-your-home-with-raspberry-pi/) - 教您如何使用 Docker Compose、MQTT 和 TLS 将 Raspberry Pi 转变为安全、模块化、开源和自托管的家庭自动化网关。
- [Essentials - AIY Voice Projects](https://magpi.raspberrypi.com/books/essentials-aiy-v1) - 使用 Google 的 AIY 项目套件，了解如何在 Raspberry Pi 上使用人工智能。 ![支持树莓派零](/media/badges/rpi-0.png)
- [Essentials - Code Music with Sonic Pi](https://magpi.raspberrypi.com/books/essentials-sonic-pi-v1) - 了解如何通过在 Raspberry Pi 上使用 Sonic Pi 进行编码来创作音乐。
- [Essentials - Conquer the Command Line (Version 2)](https://magpi.raspberrypi.com/books/command-line-second-edition) - 了解如何使用 Raspbian 在 Raspberry Pi 上命令和征服命令行，简化复杂的任务，同时自动执行简单的任务。
- [Essentials - GPIO Zero Electronics](https://magpi.raspberrypi.com/books/essentials-gpio-zero-v1) - 使用 Raspberry Pi 上的 GPIO 引脚和 GPIO 零库创建电子作品。
- [Essentials - Learn to Code with C](https://magpi.raspberrypi.com/books/essentials-c-v1) - 了解如何在 Raspberry Pi 上使用构建大部分 Linux 的语言和 Raspbian（C 编程语言）进行编码。
- [Essentials - Learn to Code with Scratch](https://magpi.raspberrypi.com/books/essentials-scratch-v1) - 使用 Scratch 编码块语言学习 Raspberry Pi 上的编程基础知识。
- [Essentials - Make Games with Python](https://magpi.raspberrypi.com/books/essentials-games-vol1) - 通过使用 Python 制作游戏，从简单的基于文本的游戏到带有声音和动画的成熟游戏，使用 Raspberry Pi 创建您自己的娱乐。
- [Essentials - Making with Minecraft](https://magpi.raspberrypi.com/books/essentials-minecraft-v1) - 了解如何使用 API、GPIO 引脚、程序等与 Minecraft 的特殊 Raspberry Pi 版本进行交互。
- [Essentials - Sense HAT Experiments](https://magpi.raspberrypi.com/books/essentials-sense-hat-v1) - 这是一本有用的实验书，其中介绍了与 Sense HAT 一起使用的实验以及如何充分发挥其潜力。
- [Getting Started with Java on the Raspberry Pi](https://leanpub.com/gettingstartedwithjavaontheraspberrypi/) - 有关 Java 本身以及如何在 Raspberry Pi 上安装和使用它的大量信息和历史，以及大量示例项目。
- [Getting Started with Raspberry Pi](https://magpi.raspberrypi.com/books/get-started) - 了解如何开始使用 **Raspberry Pi 3A+**。 ![支持树莓派3](/media/badges/rpi-3.png)
- [Raspberry Pi Annual 2018](https://magpi.raspberrypi.com/books/annual-2018) - 一本针对所有年龄段孩子的教育书籍，介绍 Raspberry Pi。
- [Raspberry Pi Beginner's Book 1](https://magpi.raspberrypi.com/books/beginners-1) - 官方的 Raspberry Pi 初学者书籍，涵盖如何开始使用 Raspberry Pi 并开始利用不同的软件和硬件项目。
- [Raspberry Pi Beginner's Guide](https://magpi.raspberrypi.com/books/beginners-guide) - 了解如何开始使用 **Raspberry Pi 3B+**。 ![支持树莓派3](/media/badges/rpi-3.png)
- [Raspberry Pi Beginner's Guide v2](https://magpi.raspberrypi.com/books/beginners-guide-2nd-ed) - 了解如何开始使用 **Raspberry Pi 4**。
- [Raspberry Pi Beginner's Guide v3](https://magpi.raspberrypi.com/books/beginners-guide-3rd-ed) - 了解如何开始使用 **Raspberry Pi 4**。
- [Raspberry Pi Beginner's Guide v4](https://magpi.raspberrypi.com/books/beginners-guide-4th-ed) - 了解如何开始使用 **Raspberry Pi 4 和 Raspberry Pi 400**。
- [Raspberry Pi Projects Book 1](https://magpi.raspberrypi.com/books/projects-1) - Raspberry Pi 项目集合，包含项目指南和 Raspberry Pi 产品评论。
- [Raspberry Pi Projects Book 2](https://magpi.raspberrypi.com/books/projects-2) - Raspberry Pi 项目的第二个集合，包含项目指南和 Raspberry Pi 产品评论。
- [Raspberry Pi Projects Book 3](https://magpi.raspberrypi.com/books/projects-3) - Raspberry Pi 项目的第三个集合，包含项目指南和 Raspberry Pi 产品评论。
- [Raspberry Pi Projects Book 4](https://magpi.raspberrypi.com/books/projects-4) - Raspberry Pi 项目的第四个集合，包含项目指南和 Raspberry Pi 产品评论。
- [Raspberry Pi Projects Book 5](https://magpi.raspberrypi.com/books/projects-5) - Raspberry Pi 项目的第五个集合，包含 Raspberry Pi 产品的项目指南和评论。
- [Retro Gaming with Raspberry Pi](https://magpi.raspberrypi.com/books/retro-gaming) - 有关如何设置 Raspberry Pi 来玩经典游戏以及如何制作自己的游戏的指南。
- [The Official Raspberry Pi Handbook 2021](https://magpi.raspberrypi.com/books/handbook-2021) - 帮助您充分利用 Raspberry Pi 计算机、基本信息、项目想法、教程和评论的指南。
- [The Official Raspberry Pi Handbook 2022](https://magpi.raspberrypi.com/books/handbook-2022) - 帮助您充分利用 Raspberry Pi 计算机、基本信息、项目想法、教程和评论的指南。 **针对 Raspberry Pi Pico 进行了更新。**

### 教程

- [Auto Mount USB](https://medium.com/@anshul.ahu/guide-to-setup-auto-mount-usb-on-raspberry-pi-4f343761627f) - 在 Raspberry Pi 上设置自动安装 USB 的指南。
- [Bridging Wifi to the Raspberry Pi over Ethernet](https://thibmaek.com/posts/bridging-wifi-to-the-raspberry-pi-over-ethernet) - 在 macOS 和 Raspberry Pi 之间设置联机网络。
- [Build a $35 Time Capsule](https://raymii.org/s/articles/Build_a_35_dollar_Time_Capsule_-_Raspberry_Pi_Time_Machine.html) - 时间机器备份服务器。
- [Controlling Spotify with Slack and a Raspberry Pi](https://thesocietea.org/2016/03/controlling-spotify-with-slack-and-a-raspberry-pi/) - Node.js 项目使用 libspotify 控制 Spotify 和 Slack。
- [DC++ Hub](https://medium.com/@anshul.ahu/guide-to-setup-an-adc-dc-hub-on-raspberry-pi-4dbf86ca8547) - 在 Raspberry Pi 上设置 ADC (DC++) 集线器的指南。
- [DIY Neural Network](http://hackaday.com/2017/06/14/diy-raspberry-neural-network-sees-all-recognizes-some/) - 使用图像识别和 Google 的 Inception 来识别特定对象。
- [Docker Swarm with LetsEncrypt](https://aaron.haurwitz.com/#!/posts/raspberry-pi-docker-swarm-with-lets-encrypt) - 关于如何使用 Docker 设置集群、使用 Docker Compose 分发服务以及使用 Letsencrypt 签署有效的 SSL 证书的明确指南。
- [How To Make a Raspberry Pi Turn on a Lamp with iBeacon™ Technology](http://developer.radiusnetworks.com/2014/04/27/how-to-make-a-raspberry-pi-turn-on-a-lamp-with-an-ibeacon.html) - 使用 Beacon 技术的良好初学者指南。
- [Moonlight](https://github.com/irtimmer/moonlight-embedded) - Nvidia GameStream 实施可将您的完整 Steam 游戏集从桌面流式传输到 Raspberry Pi。
- [Raspberry Pi 5 SSD Boot Guide](https://raspberry.tips/raspberry-pi-5-zubehoer-test) - 使用 NVMe SSD 升级 RPi 5 的综合指南，包括基准测试和硬件兼容性测试（2026 更新）。
- [Raspbereum](https://github.com/jim380/Raspbereum) - 在 Raspberry Pi 上运行您自己的以太坊节点。
- [Raspberry Pi Game Console](https://lifehacker.com/how-to-turn-your-raspberry-pi-into-a-retro-game-console-498561192) - 如何以 35 美元构建 Raspberry Pi 复古游戏机。
- [Raspberry Pi login with SSH keys](https://thibmaek.com/posts/raspberry-pi-login-with-ssh-keys) - Raspberry Pi 上 ssh 会话的无密码登录。
- [Raspberry Pi Media Server Guides](http://www.htpcguides.com/category/raspberry-pi/) - HTPC 指南中的媒体服务器和 NAS 教程。
- [Turn a Raspberry Pi into a Plex Media Server](https://www.codedonut.com/raspberry-pi/raspberry-pi-plex-media-server/) - 设置 Plex 媒体服务器以流式传输所有媒体内容的初学者指南。
- [Turn the Raspberry Pi Zero into a mini dongle computer](https://n-o-d-e.net/pi_zero_dongle.html) - 设置 pi0 以便能够通过 USB 进行 ssh 和 vnc。 ![支持树莓派零](/media/badges/rpi-0.png)
- [Use a Raspberry Pi with multiple WiFi networks](https://www.mikestreety.co.uk/blog/use-a-raspberry-pi-with-multiple-wifi-networks) - 有关在多个网络中使用 Raspberry Pi 的教程。
- [Use a Raspberry Pi with Netflix](https://thepi.io/how-to-watch-netflix-on-the-raspberry-pi/) - 有关在 Raspberry Pi 上观看 Netflix 的教程。
- [在 Raspberry Pi 上使用 openSUSE 的 YaST](https://www.raspberry-pi-geek.com/Archive/2017/22/Using-openSUSE-s-YaST-on-the-Raspberry-Pi)。

### 快速编程

- [BuildSwiftOnARM](https://github.com/uraimo/buildSwiftOnARM) - 在 RaspberryPi 或其他 ARM 板上构建 Swift 所需的一切，已更新至 Swift 4.1.3。
- [Compile Swift for Raspberry Pi by Visual Studio Code](https://medium.com/@programmingpassion/compile-swift-for-raspberry-pi-by-visual-studio-code-3f303e32d34e) - 快速教程分享如何使用 Visual Studio Code 帮助设置编译 Raspberry Pi 代码。
- [Compile Swift for Raspberry Pi by Xcode](https://medium.com/@programmingpassion/compile-swift-for-raspberry-pi-by-xcode-406ac26b63ec) - 快速教程分享如何使用 Xcode 帮助设置编译 Raspberry Pi 代码。
- [Setup Swift environment on Raspbian](https://medium.com/@programmingpassion/set-up-swift-environment-on-raspberry-pi-part-2-2-56f7f33b00d) - 帮助在 Raspbian Stretch（精简版）上设置 Swift 环境的快速指南。
- [SwiftyGPIO](https://github.com/uraimo/SwiftyGPIO) - 用于 Linux/ARM 板上硬件项目的 Swift 库，支持 GPIO/SPI/I2C/PWM/UART/1Wire。
- [Swish](https://github.com/thomaspaulmann/Swish) - 在 Xcode 中的远程计算机上构建 Swift 项目。

## 社区

- [Twitter 上的“@Raspberry_Pi”](https://twitter.com/Raspberry_Pi)
- [Mastodon 上的“@Raspberry_Pi@raspberrypi.social”](https://raspberrypi.social/@Raspberry_Pi)
- [Freenode 上的“#raspberrypi”](https://webchat.freenode.net/?channels=%23raspberrypi)
- [YouTube 上的“树莓派”](https://www.youtube.com/channel/UCFIjVWFZ__KhtTXHDJ7vgng)
- [eLinux 中心](http://elinux.org/RPi_Hub)
- [在 YouTube 上制作](https://www.youtube.com/channel/UChtY6O8Ahw2cz05PS2GhUbg)
- [YouTube 上的 Novaspirittech](https://www.youtube.com/channel/UCrjKdwxaQMSV_NDywgKXVmw)
- [官方博客](https://www.raspberrypi.org/blog/)
- [官方论坛](https://www.raspberrypi.org/forums/)
- [Raspberry Pi Jam — 官方会议](https://www.raspberrypi.org/jam/)
- [红迪项目](https://www.reddit.com/r/RASPBERRY_PI_PROJECTS)
- [Reddit](https://www.reddit.com/r/raspberry_pi)
- [StackExchange](https://raspberrypi.stackexchange.com/)

### 贡献

贡献指南可以在[此处](https://github.com/thibmaek/awesome-raspberry-pi/blob/main/CONTRIBUTING.md)找到

### 许可证

[![CC0](http://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)
