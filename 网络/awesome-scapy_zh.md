# 太棒了 Scapy [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
<p align="center">
  <a href="https://scapy.net/"><img src="https://github.com/secdev/scapy/blob/master/doc/scapy_logo.png" width="200" alt="Scapy" /></a>
</p>

使用 **[Scapy](https://scapy.net)**（基于 Python 的交互式数据包操作程序和库）的工具、附加组件、文章或炫酷漏洞的精选列表。
请随意[贡献](https://github.com/login?return_to=https%3A%2F%2Fgithub.com%2Fsecdev%2Fawesome-scapy%2Fedit%2Fmain%2FREADME.md)！

您还可以在 GitHub 上[探索 Scapy 主题](https://github.com/topics/scapy)！

## 内容

- [Tools](#tools)
- [Exploits](#exploits)

## 工具

（大量）使用 Scapy 或扩展它的工具。

乐趣
- [pwnagotchi](https://github.com/evilsocket/pwnagotchi) - 你的 AI 宠物可以通过破解 WiFI 来成长。超级可爱。

分布式拒绝服务
- [ufonet](https://github.com/epsylon/ufonet) - 创建您自己的僵尸网络来发送无法追踪的 DDoS 攻击。

无线上网。
- [trackerjacker](https://github.com/calebmadrigal/trackerjacker) - 通过原始 802.11 监控来映射和跟踪 Wi-Fi 网络和设备。
- [wifiphisher](https://github.com/wifiphisher/wifiphisher) - 创建恶意接入点。

无线
- [WHAD](https://github.com/whad-team/whad-client) - 执行各种无线攻击的强大框架。

IPv6
- [Chiron](https://github.com/aatlasis/Chiron) - IPv6 安全评估框架。
- [mitm6](https://github.com/fox-it/mitm6) - 对 IPv6 执行 MiTM。

测量值
- [mtraceroute](https://github.com/rwhalb/mtraceroute) - 通过多个跟踪路由分析创建很酷的图表。
- [Network Security Toolkit (NST)](https://wiki.networksecuritytoolkit.org/nstwiki/index.php?title=HowTo_Use_The_Scapy:_Multi-Traceroute_-_MTR) - 包括具有 IP 地理定位和 GUI 管理功能的增强版“mtraceroute”。
- [netprobify](https://github.com/criteo/netprobify) - 专为数据中心（但不仅限于）而设计的网络探测工具。使用 TCP、UDP 或 ICMP 进行探测。

协议
- [Cotopaxi](https://github.com/Samsung/cotopaxi) - 使用特定网络 IoT 协议（AMQP、CoAP、DTLS、HTCPCP、KNX、mDNS、MQTT、MQTT-SN、QUIC、RTSP、SSDP）对物联网设备进行安全测试的工具集。
- [project-memoria-detector](https://github.com/Forescout/project-memoria-detector) - 确定网络设备是否运行特定的嵌入式 TCP/IP 堆栈。
- [routopsy](https://github.com/sensepost/routopsy) - 攻击 DRP 和 FHRP 的工具包。
- [TorPylle](https://github.com/cea-sec/TorPylle) - OR (TOR) 协议的实施。

单元测试
- [Linux Kernel](https://github.com/torvalds/linux/blob/master/tools/testing/selftests/tc-testing/plugin-lib/scapyPlugin.py) - Linux 流量控制 (tc) 测试套件。
- [OpenBSD](https://github.com/login?return_to=https%3A%2F%2Fgithub.com%2Fsearch%3Fq%3Dscapy%2Brepo%253Aopenbsd%252Fsrc%2Bpath%253Aregress%252F%26type%3DCode%26ref%3Dadvsearch%26l%3D%26l%3D) - IPv6 堆栈测试套件。
- [RIOT-OS](https://github.com/RIOT-OS/RIOT/search?l=Python&q=scapy&type=Code) - RIOT OS 网络测试套件。

可视化
- [Scapy-Packet-Viewer](https://pypi.org/project/scapy-packet-viewer/) - 类似于 tshark/mitmproxy 的最小数据包查看器。基于urwid。

杂项
- [aioblescan](https://github.com/frawau/aioblescan) - 扫描并解码广告的 BLE 信息。
- [fenrir](https://github.com/Orange-Cyberdefense/fenrir-ocd) - 绕过有线 802.1x 保护。
- [flowsynth](https://github.com/secureworks/flowsynth) - 用于快速建模网络流量的工具。
- [Fragscapy](https://github.com/AMOSSYS/Fragscapy) - 通过自动修改传出网络数据包来模糊网络协议。
- [Habu](https://github.com/fportantier/habu) - 带有很多小黑客工具的工具包。他们中的许多人使用 Scapy。
- [mirage](https://redmine.laas.fr/projects/mirage) - 强大的模块化框架，专用于无线通信的安全分析。
- [netenum](https://github.com/redcode-labs/Netenum) - 一种被动发现网络上活动主机的工具。
- [net-creds](https://github.com/DanMcInerney/net-creds) - 嗅探并捕获接口上的所有敏感数据。
- [packetweaver](https://github.com/ANSSI-FR/packetweaver) - 用于脚本归档和任务排序的 Python 框架。
- [p0f3plus](https://github.com/FlUxIuS/p0f3plus) - 具有额外分析功能的实现。
- [pysap](https://github.com/SecureAuthCorp/pysap) - 使用定制框架和工具与 SAP 进行交互。
- [Responder](https://github.com/SpiderLabs/Responder) - LLMNR、NBT-NS 和 MDNS 中毒者。
- [scapy\_unroot](https://github.com/scapy-unroot/scapy_unroot) - 无需 root 权限即可使用 Scapy 的工具。
- [scapy-benchmarks](https://github.com/gpotter2/scapy-benchmarks) - 一个跟踪 Scapy 性能演变的小型测试套件。
- [sshame](https://github.com/HynekPetrak/sshame) - 暴力破解 SSH 公钥身份验证的工具。
- [TIDoS Framework](https://github.com/0xInfection/TIDoS-Framework) - 进攻性手动 Web 应用程序渗透测试框架。
- [h2spacex](https://github.com/nxenon/h2spacex) - 基于 Scapy 的 HTTP/2 低级库，可用于单包攻击（H2 上的竞争条件）。

## 功绩

使用 Scapy 的漏洞利用。这不包括默认包含的

2024

- [CVE-2024-20674](https://github.com/gpotter2/CVE-2024-20674) - Windows Kerberos 绕过导致 RCE。
- [PPPwn (CVE-2006-4304)](https://github.com/TheOfficialFloW/PPPwn) - Playstation 4 PPPoE RCE。

2022

- [CVE-2021-28444](http://blog.champtar.fr/VLAN0_LLC_SNAP) - Windows Hyper-V 安全功能绕过漏洞。

2021

- [CVE-2021-24086](https://blog.quarkslab.com/analysis-of-a-windows-ipv6-fragmentation-vulnerability-cve-2021-24086.html) - Windows IPv6碎片漏洞分析。
- [fragattacks](https://github.com/vanhoefm/fragattacks) - 碎片和聚合攻击。

2020

- [CVE-2020-25577](https://blog.quarkslab.com/bad-neighbor-on-freebsd-ipv6-router-advertisement-vulnerabilities-in-rtsold-cve-2020-25577.html) - FreeBSD 上的坏邻居：rtsold 中的 IPv6 路由器通告漏洞。
- [CVE-2020-16898](https://blog.quarkslab.com/beware-the-bad-neighbor-analysis-and-poc-of-the-windows-ipv6-router-advertisement-vulnerability-cve-2020-16898.html) - 当心坏邻居：Windows IPv6 路由器通告漏洞的分析和 PoC。

2019
- [CVE-2019-5597](https://www.synacktiv.com/ressources/Synacktiv_OpenBSD_PacketFilter_CVE-2019-5597_ipv6_frag.pdf) - OpenBSD 数据包过滤器中的 IPv6 碎片漏洞。

2018

- [CVE-2018-4407](https://github.com/r3dxpl0it/CVE-2018-4407) - XNU 操作系统内核（iOS 和 macOS）中的网络代码中存在堆缓冲区溢出。

2017
- [krackattacks-scripts](https://github.com/vanhoefm/krackattacks-scripts) - 测试客户端或接入点 (AP) 是否受到针对 WPA2 的 KRACK 攻击的影响。

2016
- [CVE-2016-6366](https://github.com/RiskSense-Ops/CVE-2016-6366) - EXTRABACON 漏洞是由 Equation Group (NSA) 编写并由 Shadow Brokers 泄露的 Cisco ASA 远程代码执行。

杂项
- [isf](https://github.com/dark-lbp/isf) - ISF（工业控制系统开发框架）。提供利用各种工业协议的套件。

