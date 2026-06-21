# 出色的 IP 音频 [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[<img src="./resources/aes67-logo.png" alt="AES67 徽标"align="centre">](https://wikipedia.org/wiki/AES67)

> 精彩的 [IP 音频](https://www.avid.com/resource-center/audio-over-ip-avb-and-dante-what-todays-music- Producer-should-know ) 和 AES67 工具和资源的精选列表。

在专业音频领域，IP 音频 (AoIP) 是指通过 IP（第 3 层）网络传输未压缩、低延迟的音频。流行的协议示例有 [Dante](https://en.wikipedia.org/wiki/Dante_(networking))、[AES67](https://en.wikipedia.org/wiki/AES67) 和 [Ravenna](https://en.wikipedia.org/wiki/Ravenna_(networking))。

该列表很短，部分原因是排除了未维护的项目。如果您更喜欢更宽松的方法，请查看底部的 [脚注](#footnotes) 部分和 [awesome-but-inactive](awesome-but-inactive.md)。总的来说，AoIP 生态系统仍在增长，目前可用的工具相当稀疏。因此，如果您发现缺少任何内容，如果您打开 PR 来添加它，我会很高兴。

欢迎投稿！首先阅读[贡献指南](contributing.md)。

---

## 内容

- [Tools](#tools)
- [Organizations](#organizations)
- [Education](#education)
- [Standards](#standards)

## 工具

- [Network Audio Controller](https://github.com/chris-ritsen/network-audio-controller) - 在命令行上对 Dante 控制器进行逆向工程。
- [Pipewire AES67](https://gitlab.freedesktop.org/pipewire/pipewire/-/wikis/AES67) - 在 Linux 上将 AES67 流显示为本机音频设备。
- [Merging ALSA RAVENNA/AES67 Driver](https://bitbucket.org/MergingTechnologies/ravenna-alsa-lkm/src/master/) - 不接受贡献的开源驱动程序。
- [AES67 Linux Daemon](https://github.com/bondagit/aes67-linux-daemon) - Merging 驱动程序与开源 Web 服务器的分叉。
- [AES67 Monitor](https://github.com/philhartung/aes67-monitor) - 跨平台 AES67 监控应用程序。
- [JackTrip](https://jacktrip.github.io/jacktrip/) - 一种用于通过 LAN 和 WAN 传输实时音频的开源工具。
- [LinuxPTP](https://linuxptp.sourceforge.net/) - 适用于 Linux 的 PTP IEEE 1588。提供各种工具，例如`ptp4l` 和 `phc2sys`。
- [PAM](https://github.com/martim01/pam) - 支持 FOSS AES67 的音频监视器。
- [Snapcast](https://github.com/badaix/snapcast/tree/develop) - FOSS 项目用于类似 Sonos 的多房间解决方案，使用基于 TCP 的自定义协议。
- [Ravennakit SDK](https://github.com/soundondigital/ravennakit) - 为使用 AES67、RAVENNA 和 ST2110-30 的专业网络音频提供跨平台 C++ SDK。
- [Inferno](https://gitlab.com/lumifaza/inferno) - Rust 中 Dante AoIP 的开源实现（[GitHub 镜像](https://github.com/teodly/inferno/)）。
- [ROC-streaming](https://roc-streaming.org/) - 一种使用 UDP 或 RTP 通过 IP 网络传输音频的工具，专门用于实时流传输。您将流写入一端并从另一端读取它。 Roc 处理所有的复杂性。

### 闭源

- [Aneman](https://www.merging.com/aneman/) - **A**udio **NE**twork **MAN**ager，相当于 Ravenna 的 Dante 控制器。
- [PTP Track Hound](https://www.ptptrackhound.com/) - PTP网络流量分析工具（跨平台，基本免费版可用）。

## 组织机构

- [IPMX](https://ipmx.io/about/) - 一套拟议的控制、复制保护、连接管理和安全性开放标准和规范。
- [Audinate](https://audinate.com) - 其专有的 Dante 技术是迄今为止最受欢迎的 AoIP 解决方案。
- [Ravenna](https://www.ravenna-network.com/) - 第二受欢迎的 AoIP 解决方案，比 Dante 更开放。

## 教育

- [Networked Audio Products](https://rhconsulting.uk/blog/) - 每年进行一次 AoIP 产品普查（当前：[2025](https://rhconsulting.uk/blog/networked-audio-products-2025/)）。
- [Dante Certification](https://www.getdante.com/resources/training/dante-certification-program/) - 了解 Dante 有助于了解 AoIP。培训需要一个帐户。我推荐lv 1和lv 2。
- [Ravenna Resources](https://www.ravenna-network.com/resources/) - Andreas Hildebrand 举办的关于 Ravenna、AES67、SMPTE 2110、PTP 和 IPMX 的网络研讨会和幻灯片。
- [Connecting Dante with AES67](https://download.yamaha.com/files/tcm:39-868466/) - 设置与 Dante 设备之间的 AES67。 Yamaha 的本指南包含 Audinate 文档中缺少的复杂内容。

## 标准

- [AES67](https://www.aes.org/publications/standards/search.cfm?docID=96), public [draft](https://aes2.org/standards-blog/call-for-comment-on-draft-revised-aes67-xxxx-high-performance-streaming-audio-over-ip-interoperability/) - IP 音频的开放标准。
- [NMOS](https://github.com/AMWA-TV/nmos) - 用于控制网络媒体设备的 REST API。
- [SMPTE ST 2110-30](https://www.smpte.org/standards/st2110)，公共[版本](https://pub.smpte.org/latest/st2110-30/st2110-30-2017.pdf) - 视频流中基于 AES67 的音频传输。向 AES67 添加一些包含。

## 脚注

- [AES67 Wishlist](https://gist.github.com/njh/c9196c465ea33ae9f97db782870464ef) - AES67 软件的热门愿望清单启发了这个清单。
- [Curated Web Page](https://aes67.app/resources) - Philipp Hartung 的只读“AES67 资源精选列表”。
- [Awesome Audiovisual](https://github.com/stingalleman/awesome-audiovisual) - 包含一点 AoIP 的 AV 列表。
- [Awesome Broadcasting](https://github.com/ebu/awesome-broadcasting) - EBU 列表包含一些 AoIP。
