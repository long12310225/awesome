[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
# [![awesome-tor-logo](https://github.com/Polycarbohydrate/awesome-tor/assets/169401794/d8c7415e-1874-49f5-a1c6-04b3a8aa689f)](https://www.torproject.org)
> Awesome Tor 是与 Tor 网络相关的资源、工具和应用程序的精选列表。

> [!注意]
> 本产品独立于 Tor® 匿名软件制作，Tor 项目不提供有关质量、适用性或其他任何方面的保证。

Tor 是一个免费的覆盖网络，用于实现匿名通信。基于免费开源软件和全球七千多个志愿者操作的中继，用户可以通过网络的随机路径路由其互联网流量。

在阅读之前，如果您想在浏览器中托管一个 Snowflake 桥来帮助审查地区的用户绕过审查制度，请[单击此处](https://polycarbonate.github.io/awesome-tor/selfhost-snowflake)。谢谢。
## 内容
- [官方手册](#official-manual)
- [Applications](#applications)
  - [Tails](#tails)
  - [Tor / Tor 浏览器](#tor--tor-browser)
  - [其他应用](#other-applications)
- [Bridges](#bridges)
- [绕过审查制度](#bypass-censorship)
- [公众接受、影响、新闻和立法](#public-reception-impact-news-and-legislation)
- [洋葱的现状](#state-of-the-onion)
- [Whistleblowing](#whistleblowing)
## 官方手册
- [About Tor Browser](https://tb-manual.torproject.org/about/) - 了解 Tor 浏览器可以采取哪些措施来保护您的隐私和匿名。
- [Anti-fingerprinting](https://tb-manual.torproject.org/anti-fingerprinting/) - Tor 浏览器如何减少浏览器指纹识别。
- [Bridges](https://tb-manual.torproject.org/bridges/) - 大多数可插拔传输（例如 obfs4）依赖于“桥接”继电器的使用。
- [Circumvention](https://tb-manual.torproject.org/circumvention/) - 如果 Tor 网络被阻止该怎么办。
- [Downloading](https://tb-manual.torproject.org/downloading/) - 如何下载 Tor 浏览器。
- [Installation](https://tb-manual.torproject.org/installation/) - 安装 Tor 浏览器。
- [Known Issues](https://tb-manual.torproject.org/known-issues/) - Tor 的问题。
- [Make Tor Browser Portable](https://tb-manual.torproject.org/make-tor-portable/) - 如何将 Tor 浏览器安装到可移动媒体上。
- [Managing Identities](https://tb-manual.torproject.org/managing-identities/) - 了解如何在 Tor 浏览器中控制个人识别信息。
- [Mobile Tor](https://tb-manual.torproject.org/mobile-tor/) - 了解适用于移动设备的 Tor。
- [Onion Services](https://tb-manual.torproject.org/onion-services/) - 只能使用 Tor 访问的服务。
- [Plugins, add-ons, and JavaScript](https://tb-manual.torproject.org/plugins/) - Tor 浏览器如何处理附加组件、插件和 JavaScript。
- [Running Tor Browser](https://tb-manual.torproject.org/running-tor-browser/) - 了解如何首次使用 Tor 浏览器。
- [Secure Connections](https://tb-manual.torproject.org/secure-connections/) - 了解如何使用 Tor 浏览器和 HTTPS 保护您的数据。
- [Security Settings](https://tb-manual.torproject.org/security-settings/) - 配置 Tor 浏览器的安全性和可用性。
- [Support](https://tb-manual.torproject.org/support/) - 如何获得帮助、报告错误或提供反馈。
- [Troubleshooting](https://tb-manual.torproject.org/troubleshooting/) - 如果 Tor 浏览器无法正常工作该怎么办。
- [Updating](https://tb-manual.torproject.org/updating/) - 如何更新 Tor 浏览器。
- [Uninstalling](https://tb-manual.torproject.org/uninstalling/) - 如何从系统中删除 Tor 浏览器。
## 应用领域
### 尾巴
*基于 Debian 的便携式操作系统，从 RAM 运行，不留痕迹。使用 Tor 浏览器作为主要浏览器。*
- [Contribute](https://tails.net/contribute/index.en.html)
- [Documentation](https://tails.net/doc/index.en.html)
- [Download](https://tails.net/install/index.en.html)
- [Homepage](https://tails.net/)
- [它是如何运作的](https://tails.net/about/index.en.html)
- [News](https://tails.net/news/index.en.html)
- [Support](https://tails.net/support/index.en.html)
### Tor / Tor 浏览器
*开源网络浏览器，通过免费的、全球性的、志愿者的覆盖网络引导互联网流量来实现匿名通信，以向任何进行网络监视或流量分析的人隐藏位置和使用情况。*
- [About](https://www.torproject.org/about/history/)
- [Commmunity](https://community.torproject.org/)
- [Donate](https://donate.torproject.org/)
- [Download](https://www.torproject.org/download/)
- [Support](https://support.torproject.org/)
- [News](https://blog.torproject.org/)
- 核心 Tor / Little-t-tor
  - [安装/验证源代码](https://support.torproject.org/little-t-tor/)
  - [论坛/支持](https://forum.torproject.org/c/support/core-tor/18)
### 其他应用
- [ansible-relayor](https://github.com/nusenu/ansible-relayor) - 对于 Tor 中继运营商来说，这是一个可靠的角色。
- [bine](https://github.com/cretz/bine) - 用于访问和嵌入 Tor 客户端和服务器的 Go 库。
- [Briar](https://briarproject.org/) - 绕过集中式服务器的点对点消息传递。通过蓝牙、Wi-Fi 或 Tor 连接。
- [Bulk Tor Exit Exporter](https://check.torproject.org/api/bulk) - 通过显示出口节点 IPv4 和指纹信息来识别 Tor 出口节点。
- [Chutney](https://gitlab.torproject.org/tpo/core/chutney/) - 配置 Tor 网络、启动并监控它，然后对其运行测试。
- [dnscrypt-proxy](https://github.com/DNSCrypt/dnscrypt-proxy) - 灵活的 DNS 代理，支持加密的 DNS 协议。
- [dos-over-tor](https://github.com/skizap/dos-over-tor) - Tor 压力测试工具的概念拒绝服务证明。
- [DocTor](https://gitlab.torproject.org/tpo/network-health/doctor/) - 一种通知服务，用于监视新发布的描述符信息是否存在问题。
- [eotk](https://github.com/alecmuffett/eotk) - 用于部署 HTTP/Onion 站点以为流行网站提供官方洋葱网络的工具。
- [exitmap](https://www.cs.kau.se/philwint/spoiled_onions/) - Tor 扫描仪可检测不良出口（变质的洋葱）。
- [haskell-tor](https://github.com/GaloisInc/haskell-tor) - Tor 协议的 Haskell 实现。
- [HTTPS Everywhere](https://www.eff.org/https-everywhere) - 只允许浏览器使用 HTTPS 进行连接，内置 Tor。
- [kalitorify](https://github.com/brainfucksec/kalitorify) - 通过 Tor 为 Kali Linux 操作系统创建透明代理的 Shell 脚本。
- [Tor Metrics](https://metrics.torproject.org/) - 可调整的图表以可视化 Tor 的统计数据。
- [multitor](https://github.com/trimstray/multitor) - 创建多个具有负载平衡的 Tor 实例。
- [mini-tor](https://github.com/wbenny/mini-tor) - 访问互联网内容和隐藏服务内容时应用程序尺寸最小。
- [node-Tor](https://github.com/Ayms/node-Tor) - Tor 协议在服务器端和浏览器上的 JavaScript 开源实现。
- [nyx](https://nyx.torproject.org/) - CLI 界面，其中包含有关继电器的详细实时信息。
- [offensive-tor-toolkit](https://github.com/atorrescogollo/offensive-tor-toolkit) - 在 Go 中通过 Tor 绑定/反向 Shell、SOCKS 等。
- [onion-grater](https://github.com/Whonix/onion-grater) - 针对危险的 Tor 控制协议命令的白名单过滤器。
- [Onionbalance](https://onionbalance.readthedocs.io/en/latest/) - 一种在多个后端 Tor 实例之间平衡洋葱服务负载的方法。
- [Onionoo](https://metrics.torproject.org/onionoo.html) - 一个基于网络的协议，用于了解当前运行的 Tor 中继和网桥。
- [OnionScan](https://onionscan.org/) - 帮助隐藏服务的运营商发现并解决其服务的运营安全问题。
- [OnionShare](https://onionshare.org/) - 使用 Tor 网络匿名共享文件、托管网站和聊天。
- [OONI](https://ooni.org/) - 测试网站和应用程序的阻止。测量网络的速度和性能。
- [Orbot](https://guardianproject.info/apps/org.torproject.android/) - Android 上的 Tor。
- [Orfox](https://guardianproject.info/apps/info.guardianproject.orfox/) - 修改后的 Android 版 Tor 浏览器。需要 Orbot。
- [php-torcontrol](https://github.com/dunglas/php-torcontrol) - TorControl 是一个用于控制 Tor 服务器的 PHP 库。
- [Relay Search](https://metrics.torproject.org/rs.html) - 搜索有关继电器信息的简单方法。
- [Ricochet Refresh](https://www.ricochetrefresh.net/) - Ricochet Refresh 是一款使用 Tor 连接客户端的点对点通讯应用程序。
- [rotating-proxy](https://github.com/mattes/rotating-proxy) - 使用 Docker 轮换 Tor 代理。
- [sbws](https://gitlab.torproject.org/tpo/network-health/sbws) - Tor 带宽扫描器，生成供目录权限使用的带宽文件。
- [Stormy](https://github.com/glamrock/stormy) - Stormy 是一个向导，只需单击几下即可帮助人们创建 Tor Onion 服务。
- [setup-tor](https://github.com/tor-actions/setup-tor) - 使用特定版本的 Tor 设置 GitHub Actions 工作流程。
- [Stem](https://stem.torproject.org/) - Stem 是 Tor 的 Python 控制器库。
- [Shadow](https://shadow.github.io/) - Shadow 是一个离散事件网络模拟器，它作为插件运行真正的 Tor 软件。
- [Tallow](https://github.com/basil00/TorWall) - 一个通过 Tor 匿名网络重定向来自 Windows 计算机的所有出站流量的程序。
- [tor_box](https://github.com/CMoncur/tor_box) - 适用于 Raspberry Pi 的全包 Tor 配置，用作中继和个人 Tor 网络。
- [Tor_Onion_Proxy](https://github.com/thaliproject/Tor_Onion_Proxy_Library) - 提供 .JAR 和 .AAR 文件，用于将 Tor 嵌入到 Java 或 Android 程序中。
- [tor_ssh.sh](https://gitlab.com/grownetics/devops/blob/master/tor_ssh.sh) - 允许使用 Tor 进行 SSH 访问任何服务器的命令。
- [tor-browser-selenium](https://github.com/webfp/tor-browser-selenium) - 一个使用 Selenium WebDriver 自动化 Tor 浏览器的 Python 库。
- [tor-controller](https://github.com/kragniz/tor-controller) - 在 Kubernetes 上运行 Tor Onion 服务。
- [tor-hidden-service](https://hub.docker.com/r/goldy/tor-hidden-service) - 为 v2 或 v3 版本的 Onion Services 制作的 Docker 容器。
- [tor-relay-bootstrap](https://github.com/coldhakca/tor-relay-bootstrap) - 用于引导 Debian 服务器成为一劳永逸的 Tor 中继的脚本。
- [Tor.framework](https://github.com/iCepa/Tor.framework) - Tor.framework 是将 Tor 嵌入 iOS 应用程序的最简单方法。
- [tor.rb](https://github.com/dryruby/tor.rb) - 这是一个用于与 Tor 匿名网络交互的 Ruby 库。
- [Tor2web](https://github.com/tor2web/Tor2web) - HTTP 代理软件，允许通过常见的 Web 浏览器访问 Tor 隐藏服务。
- [TorBot](https://github.com/DedSecInside/TorBot) - 用于数据收集的洋葱网站爬虫。
- [TorChat-Mac](https://github.com/javerous/TorChat-Mac) - macOS 原生 TorChat 客户端。
- [TorChat](https://github.com/prof7bit/TorChat) - 基于 Tor 隐藏服务的去中心化匿名即时通讯工具。
- [TorCheck](https://check.torproject.org/) - 确定访问者是否正在使用 Tor。
- [torDDoS](https://github.com/r3nt0n/torDDoS) - TorDDos 是一个 Python 工具，用于自动从 Tor 网络对网站进行 DDoS 攻击。
- [toriptabkes2](https://github.com/ruped24/toriptables2) - 一个匿名器，用于设置 iptables 和 Tor 以通过 Tor 网络路由所有流量。
- [torps](https://github.com/torps/torps) - Tor 路径模拟器 (TorPS) 是一个用于高效模拟 Tor 中路径选择的工具。
- [Torsocks](https://gitlab.torproject.org/tpo/core/torsocks/) - 允许您通过 Tor 安全地使用大多数应用程序。
- [Tortilla](https://www.crowdstrike.com/resources/community-tools/tortilla-tool/) - 通过 Tor 安全、匿名、透明地路由所有 TCP/IP 和 DNS 流量的工具。
- [tun2tor](https://github.com/iCepa/tun2tor) - Rust 库，创建 utun（用户空间隧道）接口，并将其连接到基于流的代理。
- [txtorcon](https://txtorcon.readthedocs.io/en/latest/) - 使用 Python 的 Twisted 网络库实现 Tor 的控制规范。
- [Vanguards](https://github.com/mikeperry-tor/vanguards) - 该插件可防止防护发现和相关流量分析攻击。
- [Whonix](https://www.whonix.org/) - 操作系统专为使用 Tor 网络的桌面范围内的高级安全性和隐私性而设计。
- [ZeroNet](https://zeronet.io/) - 免费且不受审查的网站，使用比特币加密技术、BitTorrent 网络和 Tor 支持。
## 桥梁
- [BridgeDB](https://pythonhosted.org/bridgedb/) - BridgeDB 是用于分发 Tor Bridge 的后端服务器的集合。
- [Conjure](https://gitlab.torproject.org/tpo/anti-censorship/pluggable-transports/conjure) - Conjure 是绕行系统折射网络（又名诱饵路由）谱系中的一种反审查工具。
- [Flash Proxies](https://crypto.stanford.edu/flashproxy/) - 过时且已弃用的桥接类型。它是一个在网络浏览器中运行的微型代理。
- [fteproxy](https://fteproxy.org/) - 过时且已弃用的桥接类型。 Tor 流量类似于纯 HTTP。该名称代表“格式转换加密”。
- [meek](https://support.torproject.org/glossary/meek/) - 这些可插拔传输让您看起来像是在浏览一个主要网站而不是使用 Tor。
- [obsf2](https://gitlab.torproject.org/tpo/anti-censorship/pluggable-transports/trac/-/issues/10314) - 过时且已弃用的桥接类型。 obsf3 的前身。
- [obsf3](https://support.torproject.org/glossary/obfs3/) - 过时且已弃用的桥接类型。 obsf4 的前身。
- [obsf4](https://support.torproject.org/glossary/obfs4/) - 一种可插拔的传输方式，使 Tor 流量看起来是随机的，还可以防止审查员通过互联网扫描找到桥接器。
- [ScrambleSuit](https://github.com/NullHypothesis/scramblesuit) - 过时且已弃用的桥接类型。 obfsproxy 的可插入传输协议。它是用纯 Python 编写的。
- [Snowflake](https://snowflake.torproject.org/) - 让您的互联网活动看起来就像您正在使用互联网进行常规视频或语音通话一样。
- [Webtunnel](https://blog.torproject.org/introducing-webtunnel-evading-censorship-by-hiding-in-plain-sight/) - WebTunnel 是一种抗审查的可插拔传输，旨在模仿受 HTTPT 启发的加密 Web 流量 (HTTPS)。
## 绕过审查制度
- [Firefly](https://github.com/yinghuocho/firefly-proxy) - 帮助绕过防火墙的代理软件。
- [FWlite](https://github.com/v3aqb/fwlite) - 具有内置 Shadowsocks 支持的反审查 HTTP 代理。
- [Google Fi Wireless](https://fi.google.com/) - 出色的电话解决方案，允许拨打电话、发送短信和使用蜂窝数据，绕过中国的防火墙。
- [Lantern](https://github.com/getlantern/lantern) - 审查规避工具可在任何操作系统上免费下载。
- [MTProxy](https://github.com/TelegramMessenger/MTProxy) - 允许审查区域的用户连接到 Telegram。
- [NaïveProxy](https://github.com/klzgrad/naiveproxy) - NaïveProxy 使用 Chromium 的网络堆栈来伪装流量，具有很强的抗审查性和低可检测性。
- [nodeunblocker](https://github.com/nfriedly/nodeunblocker.com) - 使用 Node.js 托管您的 nodeunblocker.com 副本，以绕过互联网审查制度。
- [PrivadoVPN](https://privadovpn.com/) - 总部位于瑞士并遵守瑞士隐私法的 VPN。即使在中国也可以绕过。
- [ProtonVPN](https://protonvpn.com/) - 即使在中国也可以规避审查制度的 VPN。免费计划绕过以及多个服务器和协议。无日志政策。
- [Private Bridges](https://bridges.torproject.org/) - 转到“我需要另一种获取桥梁的方法！”部分。按照说明进行操作。
- [Runet Censorship Bypass](https://github.com/anticensority/runet-censorship-bypass) - Chromium 和 Firefox 的浏览器扩展，有助于绕过俄罗斯的审查制度。
- [StegoTorus](https://github.com/SRI-CSL/stegotorus) - Tor 匿名系统的伪装代理。
- [trojan](https://github.com/trojan-gfw/trojan) - 一种无法识别的机制，可帮助您绕过 GFW。
## 公众接受、影响、新闻和立法
- [A close look at the Great Firewall of China](https://blog.torproject.org/closer-look-great-firewall-china/) - 有关中国境内 Tor 审查的一些信息。
- [Analyzing China's Blocking of Unpublished Tor Bridges](https://www.usenix.org/conference/foci18/presentation/dunna) - 研究中国如何阻止未列出的 Tor 桥以及如何防止这种情况。
- [Anarcho-Tech NYC Wiki](https://github.com/AnarchoTechNYC/meta/wiki) - 解释如何保持在线隐私和匿名的 Wiki。
- [Anonymity Bibliography](https://www.freehaven.net/anonbib/) - 1977 年至 2020 年匿名论文选集。
- [Dropping Docs on Darknet](https://www.youtube.com/watch?v=eQ2OZKitRwc) - DEF CON 22 - Adrian Crenshaw - 在暗网上丢弃文档：人们是如何被捕的。
- [How governments have tried to block Tor](https://www.youtube.com/watch?v=DX46Qv_b7F4) - 政府如何尝试通过 28c3 阻止 Tor。
- [How the Great Firewall of China is blocked in China](https://www.usenix.org/system/files/conference/foci12/foci12-final2.pdf) - 论文解释了 Tor 在中国如何被禁止以及规避它的方法。
- [Learning more about the GFW's active probing system](https://blog.torproject.org/learning-more-about-gfws-active-probing-system/) - 有关 GFW 审查系统及其运作方式的页面。
- [My Experience With the Great Firewall of China](http://blog.zorinaq.com/my-experience-with-the-great-firewall-of-china/) - 一位信息安全专业人士在一次访问期间撰写的有关中国 CFW 的博客。
- [Protocol Misidentification Made Easy with Format-Transforming Encryption](https://kpdyer.com/publications/ccs2013-fte.pdf) - FTE 如何运作。
- [Russia Passes Bill Banning Tor](https://www.themoscowtimes.com/2021/12/08/russia-blocks-tor-anonymity-service-a75760) - 关于俄罗斯禁止 VPN 和 Tor 的文章。
- [Scaling Tor hidden services](https://www.benthamsgaze.org/2015/11/17/scaling-tor-hidden-services/) - 如何扩展隐藏服务。
- [ScrambleSuit: A Polymorph Network Protocol to Circumvent Censorship](http://arxiv.org/pdf/1305.3199) - ScrambleSuit 如何运作。
- [Snowden Revelations](https://www.theguardian.com/world/interactive/2013/nov/01/snowden-nsa-files-surveillance-revelations-decoded) - 斯诺登泄密事件对此进行了解释。
- [State of the Onion - 2023](https://blog.torproject.org/event/state-of-the-onion-2023/) - Tor 项目的年度虚拟活动，我们在其中分享团队和社区的最新动态，重点介绍他们的工作及其在这一年中在全球范围内产生的影响。
- [StegoTorus: A Camouflage Proxy for the Tor Anonymity System](https://www.freehaven.net/anonbib/cache/ccs2012-stegotorus.pdf) - 关于 StegoTorus 如何工作的论文。
- [Technical and Legal Overview of Tor](https://ccdcoe.org/uploads/2018/10/TOR_Anonymity_Network.pdf) - 从技术角度介绍了 Tor 的概述，并分析了与其使用相关的几个法律问题。
- [Tor after the Snowden revelations](https://blog.torproject.org/tor-in-2023/) - 关于斯诺登泄密事件以及 Tor 在 2024 年将做什么。
- [Tor Browser Afforded CDA Immunity for Dark Web Transactions](https://www.govinfo.gov/content/pkg/USCOURTS-utd-2_18-cv-00712/pdf/USCOURTS-utd-2_18-cv-00712-0.pdf) - 关于一名未成年人因在 Tor 上购买毒品而死亡的法庭文件。
- [Tor Hidden Services and Deanonyminization](https://www.youtube.com/watch?v=HQXRURfrf8w) - 讨论如何利用 Tor 及其服务来暴露用户的信息以及如何防止攻击。
- [Tor Overview](https://www.privacyguides.org/en/advanced/tor-overview/) - Privacyguides 对 Tor 的概述。
- [Understanding The Onion Router in 2024](https://www.privacyjournal.net/privacy/tor-network/) - 解释 Tor 是什么； 2024 年更新。
- [What is Tor?](https://www.amnesty.org/en/latest/campaigns/2024/02/what-is-tor-and-how-does-it-advance-human-rights/) - 对 Tor、洋葱服务及其如何促进人权给出了很好的解释。
## 洋葱的现状
- [2025](https://blog.torproject.org/state-of-the-onion-2025/) - 2025 年洋葱状况报告。
- [2024](https://blog.torproject.org/state-of-the-onion-2024/) - 2024 年洋葱状况报告。
- [2023](https://blog.torproject.org/state-of-the-onion-2023/) - 2023 年洋葱状况报告。
- [2022](https://blog.torproject.org/state-of-the-onion-2022/) - 2022 年洋葱状况报告。
- [2021](https://blog.torproject.org/state-of-the-onion-2021/) - 2021 年洋葱状况报告。
- [2020](https://blog.torproject.org/state-of-the-onion-2020/) - 2020 年洋葱状况报告。
- [2019](https://www.youtube.com/watch?v=W0NR6M_08oM) - 2019 年洋葱状况报告。
## 举报
- [GlobaLeaks](https://www.globaleaks.org/) - GlobaLeaks 是免费的开源软件，任何人都可以轻松设置和维护安全的举报平台。
- [SecureDrop](https://securedrop.org/) - SecureDrop 是一个开源举报人提交系统，媒体组织和非政府组织可以安装该系统以安全地接受来自匿名来源的文件。
- [WikiLeaks](https://wikileaks.org/) - 维基解密专注于分析和发布涉及战争、间谍和腐败的经过审查或其他限制的官方材料的大型数据集。
