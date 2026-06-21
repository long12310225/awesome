简介
------------

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

该项目不包含任何源代码或文件。我只想列出一个在网络流量研究中处理 pcap 文件的工具列表。有关更多精彩列表，请参阅 https://github.com/sindresorhus/awesome

**许可证**：CC0 1.0 通用 (CC0 1.0)。


> * [Linux 命令](#linuxcmds)
> * [流量捕获](#capture)
> * [流量分析/检查](#analysis)
> * [DNS 实用程序](#dnstools)
> * [文件提取](#fileextraction)
> * [相关项目](#others)



Linux 命令<a name="linuxcmds"></a>
--------------------------------------

* **Bmon**：（带宽监视器）是一个类似于 nload 的工具，可以显示系统上所有网络接口上的流量负载。输出还包含一个图表和一个包含数据包级别详细信息的部分。 [截图](https://www.binarytides.com/blog/wp-content/uploads/2014/03/bmon-640x480.png)

* **Bwm-ng**：（下一代带宽监视器）是另一个非常简单的实时网络负载监视器，它报告数据传入和传出系统上所有可用网络接口的速度摘要。 [截图](https://a.fsdn.com/con/app/proj/bwmng/screenshots/10965.jpg/245/183/1)

* **CBM**：（彩色带宽计）一个微小的简单带宽监视器，显示通过网络接口的流量。没有更多选项，只是实时显示和更新流量统计数据。 [截图](https://www.binarytides.com/blog/wp-content/uploads/2014/03/cbm.png)

* **Collectl**：以类似于 dstat 的方式报告系统统计信息，与 dstat 一样，它收集有关各种不同系统资源（如 cpu、内存、网络等）的统计信息。这里是一个如何使用它来报告网络使用情况/带宽的简单示例。 [截图](https://www.cse.wustl.edu/~jain/cse567-08/ftp/hw/collectl.png)

* **Dstat**：是一个多功能工具（用 python 编写），可以监视不同的系统统计信息并以批处理样式模式报告它们或将数据记录到 csv 或类似文件。此示例展示如何使用 dstat 报告网络带宽 [截图](https://www.howtoing.com/wp-content/uploads/2016/09/Dstat-Linux-Monitoring.png)

* **Ifstat**：以批处理方式报告网络带宽。输出的格式易于使用其他程序或实用程序进行记录和解析。 [截图](https://community.linuxmint.com/img/screenshots/ifstat.png)

* **Iftop**：测量流经各个套接字连接的数据，其工作方式与 Nload 不同。 iftop 使用 pcap 库捕获进出网络适配器的数据包，然后对大小和计数进行求和以找到正在使用的总带宽。尽管 iftop 报告各个连接使用的带宽，但它无法报告特定套接字连接中涉及的进程名称/ID。但基于 pcap 库，iftop 能够过滤流量并报告过滤器指定的选定主机连接上的带宽使用情况。 [截图](https://www.binarytides.com/blog/wp-content/uploads/2014/03/iftop.png)

* **Iptraf-ng**：是一款交互式且丰富多彩的 IP LAN 监视器。  它显示各个连接以及主机之间流动的数据量。已不复存在的 iptraf 的维护分支。 [屏幕截图](https://wiki.ipfire.org/addons/iptraf-ng/iptraf-ng_monitor.png)

* **Jnettop**：[Jnettop](https://sourceforge.net/projects/jnettop/) 是一个流量可视化工具，它捕获通过运行它的主机的流量，并显示按其使用的带宽排序的流。 [截图](https://web.archive.org/web/20130509072433if_/http://jnettop.kubs.info/wiki/?binary=internal%3A%2F%2F76195466cc3bca92f8de7b404e240844.gif)

* **Nethogs**：是一个小型“网络顶部”工具，它显示各个进程使用的带宽，并对列表进行排序，将最密集的进程放在顶部。如果出现带宽突然激增的情况，请快速打开 nethogs 并找到负责的进程。 Nethogs 报告程序的 PID、用户和路径。 [截图](https://www.binarytides.com/blog/wp-content/uploads/2014/03/nethogs.png)

* **Netload**：显示当前流量负载的小报告，以及自程序启动以来传输的字节总数。没有更多的功能了。它是 netdiag 的一部分。 [截图](https://www.binarytides.com/blog/wp-content/uploads/2014/03/netload.png)

* **Netwatch**：是 netdiag 工具集合的一部分，它也显示本地主机和其他远程主机之间的连接，以及每个连接上数据传输的速度。 [截图](https://www.binarytides.com/blog/wp-content/uploads/2014/03/netwatch.png)

* **Nload**：是一个命令行工具，允许用户分别监控传入和传出流量。它还绘制了一个图表来表示相同的情况，其比例可以调整。使用方便简单，并且不支持很多选项。 [截图](https://www.binarytides.com/blog/wp-content/uploads/2014/03/nload.png)

* **Pktstat**：实时显示所有活动连接，以及通过它们传输数据的速度。它还显示连接的类型，即 tcp 或 udp，以及有关 http 请求（如果涉及）的详细信息。 [截图](https://www.binarytides.com/blog/wp-content/uploads/2014/03/pktstat.png)

* **Slurm**：是另一个网络负载监视器，它显示设备统计信息以及 ascii 图表。它支持 3 种不同样式的图表，每种样式都可以使用 c、s 和 l 键激活。 slurm 功能简单，不会显示有关网络负载的任何进一步详细信息。 [截图](https://www.binarytides.com/blog/wp-content/uploads/2014/03/slurm.png)

* **速度计**：另一个小而简单的工具，只需通过给定接口绘制出漂亮的传入和传出流量图表。 [截图](https://www.binarytides.com/blog/wp-content/uploads/2014/03/speedometer.png)

* **Tcptrack**：与iftop类似，使用pcap库来捕获数据包并计算各种统计数据，例如每个连接使用的带宽。它还支持可用于监视特定连接的标准 pcap 过滤器。 [截图](https://www.binarytides.com/blog/wp-content/uploads/2014/03/tcptrack.png)

* **Trafshow**：报告当前活动连接、其协议以及每个连接上的数据传输速度。它可以使用 pcap 类型过滤器过滤掉连接。 [截图](https://www.binarytides.com/blog/wp-content/uploads/2014/03/trafshow.png)

* **Vnstat**：与大多数其他工具有点不同。它实际上运行一个后台服务/守护进程，并一直记录数据传输的大小。接下来，它可用于生成网络使用历史记录的报告。 [截图](https://www.howtoforge.com/images/vnstat/big/vnstat9.png)



流量捕获<a name="capture"></a>
---------------

* [Libpcap/Tcpdump](https://www.tcpdump.org/): tcpdump的官方网站，一个强大的命令行数据包分析器； libpcap，一个用于网络流量捕获的可移植 C/C++ 库。

* [Deepfence PacketStreamer](https://github.com/deepfence/PacketStreamer)：高性能远程数据包捕获和收集工具，适用于云原生环境的分布式 tcpdump。

* [Ngrep](https://github.com/jpr5/ngrep/)：努力提供GNU grep的大部分通用功能，并将它们应用到网络层。 ngrep 是一个 pcap 感知工具，允许您指定扩展的正则或十六进制表达式来匹配数据包的数据有效负载。目前，它可以跨以太网、PPP、SLIP、FDDI、令牌环和空接口识别 TCP、UDP 和 ICMP，并以与 tcpdump 和 snoop 等更常见的数据包嗅探工具相同的方式理解 bpf 过滤器逻辑。 [截图](https://www.cyberciti.biz/media/new/cms/2012/12/ngrep.png)

* [clj-net-pcap](https://github.com/ruedigergad/clj-net-pcap): `clj-net-pcap` 是 Clojure 的数据包捕获库。 clj-net-pcap 使用 jNetPcap 并在 jNetPcap 周围添加了便利功能以简化可用性。 [关于 clj-net-pcap 的论文](http://ieeexplore.ieee.org/xpl/articleDetails.jsp?tp=&arnumber=6903107) 已在 COMPSACW 2014 范围内发表。

* [jNetPcap](https://sourceforge.net/projects/jnetpcap/)：jNetPcap 是一个适用于 Linux 和 Windows 的 Java 数据包捕获库。 jNetPcap 分别利用 libpcap 和 WinPcap，并采用 Java 本机接口 (JNI) 来使用 libpcap/WinPcap 提供的功能。

* [Arkime](https://arkime.com/) Arkime（以前称为 Moloch）是一个大规模、开源、索引数据包捕获和搜索工具。

* [n2disk](https://www.ntop.org/products/traffic-recording-replay/n2disk/)（商业）：具有索引功能的多千兆网络流量记录器。 n2disk 是一个网络流量记录器应用程序。使用 n2disk，您可以从实时网络接口以多千兆位速率（在足够的硬件上超过 10 千兆位/秒）捕获全尺寸网络数据包，并将它们写入文件，而不会丢失任何数据包。

* [Netis Packet Agent](https://github.com/Netis/packet-agent)：它是一个通过 GRE 隧道的远程数据捕获实用程序，使您可以轻松地从 NIC 接口捕获数据包，用 GRE 封装它们并将它们发送到远程计算机进行监控和分析。

* [OpenFPC](https://github.com/leonward/OpenFPC)：OpenFPC 是一组脚本，它们组合在一起提供轻量级全包网络流量记录器和缓冲工具。其设计目标是允许非专家用户在 COTS 硬件上部署分布式网络流量记录器，同时集成到现有的警报和日志工具中。

* [PCAPdroid](https://github.com/emanuele-f/PCAPdroid)：PCAPdroid 是一款 Android 应用程序，可让您无需 root 即可监控和导出设备的网络流量。流量可以转储为 PCAP 格式，以便使用 Wireshark 等流行工具进行分析，甚至可以实时分析。内置流量监视器可让您检测用户和系统应用程序建立的可疑连接。

* [PF_RING](https://www.ntop.org/products/packet-capture/pf_ring/): PF_RING 是一种新型网络套接字，可显着提高数据包捕获速度。适用于 Linux 内核 2.6.32 及更高版本。无需修补内核。 PF_RING 感知驱动程序可提高数据包捕获加速。

* [pmacct](https://github.com/pmacct/pmacct)：是一小组多用途被动网络监控工具。它可以计算、分类、聚合、复制和导出转发平面数据，即。 IPv4 和 IPv6 流量；通过 BGP 和 BMP 收集并关联控制平面数据；收集并关联 RPKI 数据；通过流式遥测收集基础设施数据。

* [softflowd](https://github.com/irino/softflowd)：是一个基于流的网络监视器，它使用 libpcap 混杂监听网络接口并导出 NetFlow 数据。

* [TTT](https://www2.sonycsl.co.jp/person/kjc/kjc/software.html#ttt)：(Tele Traffic Tapper) 是 tcpdump 的另一个后代，但它能够进行实时、图形和远程流量监控。 ttt 不会取代 tcpdump，相反，它可以帮助您找出要使用 tcpdump 查看的内容。 ttt 监控网络并自动找出时间窗口内流量的主要贡献者。默认情况下，图表每秒更新一次。

* [Yaf](https://tools.netsa.cert.org/yaf/yaf.html)：这是一个可靠的软件，非常可靠，能够从 pcap 生成流记录。这对于索引巨大的 pcap 甚至进行数据包捕获非常有用。最新版本甚至可以提取有效负载并放入流记录中。

* [sharppcap](https://github.com/dotpcap/sharppcap)：完全托管的跨平台（Windows、Mac、Linux）.NET 库，用于从实时和基于文件的设备捕获数据包。 libpcap 和 npcap 的可靠且强大的包装器。

流量分析/检查<a name="analysis"></a>
--------------------------------------------------
* [Brim](https://www.brimsecurity.com/)：Brim 将 Zeek 日志的丰富性与数据包的详细信息融合在一起。这是两全其美的。虽然 Zeek 日志可以快速回答您的大多数问题，但当您需要深入了解详细信息时，您仍然可以快速访问数据包。 Wireshark 始终只需点击一下即可。

* [BruteShark](https://github.com/odedshimon/BruteShark)：是一款开源、跨平台的网络取证分析工具，具有多种功能。它包括：密码提取、显示可视化网络图、重建 TCP 会话、提取加密密码的哈希值，甚至将其转换为 Hashcat 格式以执行离线暴力攻击。

* [AIEngine](https://bitbucket.org/camp0/aiengine)：是下一代交互式/可编程数据包检查引擎，具有无需任何人工干预的学习能力、NIDS 功能、DNS 域分类、网络收集器等。 AIEngine 还帮助网络/安全专业人员识别流量并开发签名以在 NIDS、防火墙、流量分类器等上使用。

* [CapAnalysis](http://www.capanalysis.net/ca/) - CapAnalysis 是一款 Web 可视化工具，适用于信息安全专家、系统管理员和所有需要分析大量捕获的网络流量的人。 [可用](http://pcap.capanalysis.net/) 进行实时网络演示以进行测试。

* [CapTipper](https://github.com/omriher/CapTipper)：恶意 HTTP 流量浏览器

* [Chopshop](https://github.com/MITRECND/chopshop)：是一个 MITRE 开发的框架，用于帮助分析师创建和执行基于 pynids 的 APT 间谍技术解码器和检测器。

* [CoralReef](https://www.caida.org/tools/measurement/coralreef/)：是 CAIDA 开发的软件套件，用于分析被动互联网流量监视器收集的数据。它提供了一个编程库 libcoral，类似于 libpcap，具有 ATM 和其他网络类型的扩展，可以从 C 和 Perl 获得。

* [DPDK](https://www.dpdk.org/)：是一组用于快速数据包处理的库和驱​​动程序。它被设计为在任何处理器上运行。第一个支持的 CPU 是 Intel x86，现在已扩展到 IBM Power 8、EZchip TILE-Gx 和 ARM。它主要运行在 Linux 用户区。 FreeBSD 端口可用于 DPDK 功能的子集。

* [DPKT](https://github.com/kbandla/dpkt): Python 数据包创建/解析库。

* [ECap](https://web.archive.org/web/20170715080351/https://bitbucket.org/nathanj/ecap/wiki/Home)：（外部捕获）是一个带有 Web 前端的分布式网络嗅探器。 Ecap 是多年前在 2005 年编写的，但是 tcpdump-workers 邮件列表上的一个帖子请求类似的应用程序......所以就在这里。如果有兴趣的话，更新它并再次研究它会很有趣。

* [EtherApe](https://etherape.sourceforge.io/)：是一个模仿 etherman 的 Unix 图形网络监视器。它具有链路层、IP 和 TCP 模式，以图形方式显示网络活动。主机和链接的大小随流量而变化。颜色编码协议显示。它支持以太网、FDDI、令牌环、ISDN、PPP 和 SLIP 设备。它可以过滤要显示的流量，并且可以从文件中读取流量以及从网络中实时读取流量。

* [Ettercap](https://github.com/Ettercap/ettercap)：是一套使用 ARP 中毒进行流量捕获和分析的工具（MitM 攻击的一种形式，仅在您控制的网络上使用）

* [HttpSniffer](https://github.com/caesar0301/http-sniffer)：一个多线程工具，用于从 PCAP 文件中嗅探 TCP 流量统计信息和嵌入的 HTTP 标头。每个携带 HTTP 的 TCP 流都以 JSON 格式导出到文本文件。

* [Ipsumdump](https://github.com/kohler/ipsumdump)：将 TCP/IP 转储文件汇总为易于人类和程序读取的自描述 ASCII 格式。 Ipsumdump 可以从网络接口、tcpdump 文件和现有 ipsumdump 文件读取数据包。必要时它将透明地解压缩 tcpdump 或 ipsumdump 文件。它可以随机采样流量、根据流量内容过滤流量、匿名 IP 地址以及按时间戳对多个转储中的数据包进行排序。此外，它还可以选择创建包含实际数据包数据的 tcpdump 文件。将 CLICK 作为插入模块使用也很方便。

* [ITA](https://web.archive.org/web/20181016104652/http://ita.ee.lbl.gov/html/traces.html)：互联网流量档案库是一个受监管的存储库，支持广泛访问互联网网络流量痕迹，由 ACM SIGCOMM 赞助。这些痕迹可用于研究网络动态、使用特征和增长模式，并为痕迹驱动的模拟提供依据。该存档还向用于将原始跟踪数据减少为更易于管理的形式、用于生成合成跟踪以及用于分析跟踪的程序开放。

* [Joy](https://github.com/cisco/joy)：joy是一款开发的流量分析和解析工具。部分是为了协助对加密流量进行分类，例如 HTTPS 流量。它能够将 pcap 文件解析为可用的 json 文件，其中包含有关捕获统计信息和功能的详细信息。

* [Libcrafter](https://github.com/pellegre/libcrafter)：是一个 C++ 高级库，旨在简化网络数据包的创建和解码。它能够制作或解码最常见网络协议的数据包，通过网络发送它们，捕获它们并匹配请求和回复。

* [Libnet](https://github.com/libnet/libnet)：是帮助构建和处理网络数据包的例程集合。它为低级网络数据包整形、处理和注入提供了一个可移植的框架。 Libnet 在 IP 层和链路层具有可移植的数据包创建接口，以及许多补充和补充功能。使用 libnet，可以毫不费力地构建快速而简单的数据包组装应用程序。

* [Libnids](http://libnids.sourceforge.net/)：由 Rafal Wojtczuk 设计，是网络入侵检测系统 E 组件的实现。它模拟 Linux 2.0.x 的 IP 堆栈。 Libnids 提供 IP 碎片整理、TCP 流组装和 TCP 端口扫描检测。 libnids 最有价值的特性是可靠性。进行了大量测试，结果证明 libnids 能够尽可能准确地预测受保护 Linux 主机的行为。

* [Multitail](https://www.vanheusden.com/multitail/)：现在包含一个颜色方案，用于监视 tcpdump 输出。它还可以过滤、将时间戳转换为时间字符串等等。

* [Netsniff-ng](https://www.github.com/borkmann/netsniff-ng)：Netsniff-ng 是一个免费的 Linux 网络实用程序工具包，如果您愿意的话，它是您日常 Linux 网络管道的瑞士军刀。

* [NetDude](http://netdude.sourceforge.net/): (NETwork DUmp 数据显示和编辑器)。从他们的网页来看，“它是一个基于 GUI 的工具，允许您对 tcpdump 跟踪文件中的数据包进行详细更改。”

* [Network Expect](https://www.netexpect.org/)：是一个框架，允许轻松构建可以与网络流量交互的工具。按照脚本，可以将流量注入网络，并且可以根据接收到的网络流量做出决策并采取行动。解释性语言提供分支和高级控制结构来指导与网络的交互。 Network Expect 使用 libpcap 进行数据包捕获，使用 libwireshark（来自 Wireshark 项目）进行数据包解析任务。 （GPL、BSD/Linux/OSX）。

* [nfdump](https://github.com/phaag/nfdump)：是一套功能强大的工具，用于收集、处理和分析来自网络设备的流数据。

* [NFStream](https://github.com/nfstream/nfstream)：是一个 Python 框架，提供快速、灵活且富有表现力的数据结构，旨在使在线或离线网络数据的处理变得简单直观。它的目标是成为使用 Python 进行实际、真实世界网络数据分析的基本高级构建块。此外，它还有更广泛的目标，即成为研究人员的通用网络数据分析框架，为实验提供数据可重复性。

* [Ntop](http://www.ntop.org/)：Ntop 是一个网络流量探测器，显示网络使用情况，类似于流行的 top Unix 命令的作用。 ntop 基于 libpcap，并且以可移植的方式编写，以便几乎可以在每个 Unix 平台和 Win32 上运行。

* [Ntopng](https://www.ntop.org/products/traffic-analysis/ntop/)：Ntopng 是原始 ntop 的下一代版本，是一个显示网络使用情况的网络流量探测器，类似于流行的 top Unix 命令的作用。 ntop 基于 libpcap，并且以可移植的方式编写，以便几乎可以在每个 Unix 平台、MacOSX 和 Win32 上运行。

* [Ostinato](https://ostinato.org/)：Ostinato 是一款多功能数据包制作器、pcap 编辑器/播放器和流量生成器，具有直观的 GUI。附加组件包括高速 10/25/40G 流量生成和脚本/自动化 Python API。适用于所有平台 - Windows、MacOS、Linux 和实验室平台 - CML、EVE-NG 和 GNS3。

* [packemon](https://github.com/ddddddO/packemon): Packet monster (っ‘-’)╮=͟͟͞͞◒ ヽ( '-'ヽ) TUI tool for sending packets of arbitrary input and monitoring packets on any network interfaces (default: eth0).

* [PacketQ](https://github.com/dotse/PacketQ)：为 PCAP 文件提供基本 SQL 前端的工具。输出 JSON、CSV 和 XML，并包含一个带有 JSON-api 的内置 Web 服务器和一个漂亮的 AJAX GUI。

* [Pcap2har](https://github.com/andrewf/pcap2har)：使用库 dpkt 将 .pcap 网络捕获文件转换为 HTTP 存档文件的程序。

* [PcapPlusPlus](https://github.com/seladb/PcapPlusPlus)：PcapPlusPlus 是一个多平台 C++ 网络嗅探和数据包解析和操作框架。它应该是轻量级、高效且易于使用的。它是流行引擎（如 libpcap、WinPcap、DPDK 和 PF_RING）的 C++ 包装器。它还包含许多协议的解析和编辑功能，包括以太网、IPv4、IPv6、ARP、VLAN、MPLS、PPPoE、GRE、TCP、UDP、ICMP、DNS 以及 HTTP 和 SSL/TLS 等第 7 层协议

* [pcaptoparquet](https://github.com/nokia/pcaptoparquet)：pcaptoparquet 是一个 Python 包，设计用于将 PCAP 或 PCAPNG 文件转换为结构化数据格式，主要是 Apache Parquet。该工具专注于网络流量分析，通过提取、解码数据包数据并将其转换为适合分析和可视化的可查询数据集。该工具支持命令行和编程接口，能够集成到各种网络分析工作流程中。

* [pkt2flow](https://github.com/caesar0301/pkt2flow)：一个将数据包分类为流的简单实用程序。它是如此简单，以至于只需要完成一项任务。  对于深度数据包检测或流分类，分析一个特定流的特征是很常见的。我尝试使用现成的工具，如 tcpflows、tcpslice、tcpsplit，但所有这些工具都尝试减少跟踪量（根据要求）或将数据包模拟为流有效负载（超过要求）。我还没有找到一个简单的工具来将数据包分类为流而无需进一步处理。

* [potiron](https://github.com/CIRCL/potiron)：标准化、索引、丰富和可视化网络捕获。

* [pyshark](https://kiminewt.github.io/pyshark/)：tshark的Python包装器，允许使用wireshark解析器进行python数据包解析。 python 数据包解析模块有很多，这个不同，因为它实际上不解析任何数据包，它只是使用 tshark（wireshark 命令行实用程序）导出 XML 的功能来使用其解析。

* [Sanitize](https://web.archive.org/web/20190210101529/http://ita.ee.lbl.gov/html/contrib/sanitize.html)：Sanitize 是五个 Bourne shell 脚本的集合，用于通过重新编号主机和剥离数据包内容来减少 tcpdump 跟踪，以解决安全和隐私问题。每个脚本都采用 tcpdump 跟踪文件作为输入，并生成固定列格式的简化 ASCII 文件以输出到标准输出。

* [Scapy](http://www.secdev.org/projects/scapy/)：Scapy 是一个功能强大的交互式数据包操作程序。它能够伪造或解码多种协议的数据包、通过网络发送、捕获它们、匹配请求和回复等等。它可以轻松处理大多数经典任务，如扫描、跟踪路由、探测、单元测试、攻击或网络发现（它可以替代 hping、85% 的 nmap、arpspoof、arp-sk、arping、tcpdump、tethereal、p0f 等）。它还在大多数其他工具无法处理的许多其他特定任务上表现出色，例如发送无效帧、注入您自己的 802.11 帧、组合技术（VLAN 跳跃+ARP 缓存中毒、WEP 加密通道上的 VOIP 解码等）等。

* [SiLK](https://tools.netsa.cert.org/silk/)：SiLK（互联网级知识系统）是一组流量分析工具，旨在促进大型网络的安全分析。 SiLK工具套件支持网络流数据的高效采集、存储和分析。

* [Sniff](http://www.thedumbterminal.co.uk/software/sniff.html)：使 tcpdump 程序的输出更易于阅读和解析。

* [Snort](https://www.snort.org/)：Snort 是由 Sourcefire 开发的开源网络入侵防御和检测系统 (IDS/IPS)，现归思科所有。 Snort 结合了签名、协议和基于异常的检查的优点，是全球部署最广泛的 IDS/IPS 技术。凭借数百万次下载和大约 500,000 名注册用户，Snort 已成为 IPS 的事实上的标准。

* [Socket Sentry](https://github.com/rhasselbaum/socket-sentry)：Socket Sentry 是 KDE Plasma 的实时网络流量监视器，与 iftop 和 netstat 等工具的精神相同。

* [Squey](https://squey.org)：交互式可视化软件，旨在探索大型PCAP以检测异常/微弱信号。

* [Suricata](https://suricata-ids.org)：Suricata 是一款免费开源、成熟、快速且强大的网络威胁检测引擎。  Suricata 引擎能够进行实时入侵检测 (IDS)、内联入侵防御 (IPS)、网络安全监控 (NSM) 和离线 pcap 处理。

* [TCP-Reduce](http://ita.ee.lbl.gov/html/contrib/tcp-reduce.html)：TCP-Reduce 是 Bourne shell 脚本的集合，用于将 tcpdump 跟踪减少为跟踪中存在的每个 TCP 连接的一行摘要。这些脚本仅查看 TCP SYN/FIN/RST 数据包。跟踪中没有 SYN 数据包的连接（例如在跟踪开始时正在进行的连接）将不会出现在摘要中。垃圾数据包（丢失部分内容的数据包）会作为 bogon 报告给 stderr 并被丢弃。有时，脚本会被更改序列号的重传所欺骗，并报告错误的大连接大小 - 始终检查大连接（例如 100 MB 或更多）的合理性。

* [Tcpdpriv](http://ita.ee.lbl.gov/html/contrib/tcpdpriv.html)：Tcpdpriv 是用于从网络接口上收集的数据包（或从使用 tcpdump 的 -w 参数创建的跟踪文件）中消除机密信息（用户数据和地址）的程序。 Tcpdpriv 删除 TCP 和 UDP 的有效负载，以及其他协议的整个 IP 有效负载。它实现了多种地址加扰方法；顺序编号方法及其变体，以及保留地址前缀的哈希方法。

* [Tcpflow](https://github.com/simsong/tcpflow)：捕获作为 TCP 连接（流）一部分传输的数据的程序，并以方便协议分析或调试的方式存储数据。像“tcpdump”这样的程序显示在线路上看到的数据包的摘要，但通常不存储实际传输的数据。相反，tcpflow 重建实际的数据流并将每个流存储在单独的文件中以供以后分析。然而，它也可以选择隔离每个 tcp 流的 pcap 流以进行粒度检查。 [原始链接](http://www.circlemud.org/jelson/software/tcpflow/)。

* [Tcplook](http://ita.ee.lbl.gov/html/contrib/tracelook.html)：Tracelook 是一个 Tcl/TK 程序，用于以图形方式查看使用 tcpdump 的 -w 参数创建的跟踪文件的内容。 Tracelook 应该查看所有协议，但目前仅查看 TCP 连接。该程序运行缓慢并且占用大量系统资源。

* [Tcpreplay](https://github.com/appneta/tcpreplay)：使用 libnet 在接口上重播 pcap 文件。

* [Tcpslice](https://github.com/pyke369/tcpsplice): Tcpslice 是一个工具，用于提取使用 tcpdump 的 -w 标志生成的数据包跟踪文件的部分。它可以组合多个跟踪文件，和/或根据时间提取一个或多个跟踪的部分。

* [Tcpsplit](https://github.com/pmcgleenon/tcpsplit)：一种工具，用于将单个 libpcap 数据包跟踪分解为一定数量的子跟踪，沿着 TCP 连接边界分解跟踪，以便 TCP 连接最终不会分成两个子跟踪。这对于使大型跟踪文件易于处理以进行深入分析以及对跟踪进行子集化以仅对跟踪的一部分进行分析非常有用。

* [Tcpstat](https://frenchfries.net/paul/tcpstat/)：Tcpstat 报告某些网络接口统计信息，就像 vmstat 报告系统统计信息一样。 tcpstat 通过监视特定接口或从文件中读取先前保存的 tcpdump 数据来获取其信息。

* [Tcptrace](https://github.com/blitz/tcptrace)：俄亥俄大学 Shawn Ostermann 编写的工具，用于分析 TCP 转储文件。它可以将几种流行的数据包捕获程序生成的文件作为输入，包括 tcpdump、snoop、etherpeek、HP Net Metrix 和 WinDump。 tcptrace 可以生成几种不同类型的输出，其中包含有关所见每个连接的信息，例如经过的时间、发送和接收的字节和段、重传、往返时间、窗口广告、吞吐量等。它还可以生成许多图表以供进一步分析。

* [TraceWrangler](https://www.tracewrangler.com/)：TraceWrangler 是一个运行在 Windows（或 Linux 上，使用 WINE）的网络捕获文件工具包，支持 PCAP 以及新的 PCAPng 文件格式，该格式现在是 Wireshark 使用的标准文件格式。 TraceWrangler 最突出的用例是 PCAP 和 PCAPng 文件（有时称为“跟踪文件”、“捕获文件”或“数据包捕获”）的轻松清理和匿名化，删除或替换敏感数据，同时易于使用。

* [Tstat](http://tstat.tlc.polito.it/)：一种被动嗅探器，能够通过大量的流量功能提供对网络和传输级别流量模式的多种洞察。

* [WAND](https://research.wand.net.nz/)：基于 libtrace 构建的用于处理网络流量的精彩工具集合，来自怀卡托大学。我喜欢这个项目！

* [WinDivert](https://github.com/basil00/WinDivert)：是一个用于用户模式数据包拦截的Windows库。

* [WinDump](https://www.winpcap.org/windump/)：是 tcpdump 的 Windows 等效项，使用 WinPcap。

* [WinPcap](https://www.winpcap.org/)：Guy Harris 关于 WinPcap 和 WinDump 状态的消息摘录。

* [WireEdit](https://wireedit.com/)：WireEdit 是一款免费的桌面所见即所得网络数据包编辑器。它允许将任何堆栈层编辑为“富文本”，而无需了解数据包语法和编码规则。输入和输出文件格式为Pcap。

* [Wireshark suite](https://wiki.wireshark.org/Tools): 众所周知的工具套件，支持数据包分析器和协议解码器。它还包括一些实用的工具和脚本来支持大多数常见用法。

* [Xplot](http://www.xplot.org/)：xplot 程序是在 20 世纪 80 年代末编写的，用于支持 TCP 数据包跟踪分析。

* [yaraPcap](https://github.com/kevthehermit/YaraPcap)：使用 YARA 处理 HTTP Pcap

* [yaraprocessor](https://github.com/MITRECND/yaraprocessor)：使用 yaraprocessor，YARA 可以针对单个数据包有效负载以及部分或全部有效负载的串联运行。它最初是为在 Chopshop 中使用而编写的，但也可以在没有它的情况下使用。

* [Zeek](https://zeek.org/)：（以前称为 Bro）是一个开源软件平台，为从最小的家庭办公室到最大、最快的研究和商业网络的分析师提供紧凑、高保真交易日志、文件内容和完全定制的输出。来自常见问题解答：
“Zeek 提供了一个用于网络流量分析的综合平台，特别关注大规模的语义安全监控。虽然经常与经典的入侵检测/防御系统进行比较，但 Zeek 采取了一种完全不同的方法，为用户提供了一个灵活的框架，该框架有利于定制、深入的监控，远远超出了传统系统的功能。Zeek 的初始版本已在 90 年代中期投入运营部署，Zeek 发现自己扎根于 20 多年的研究。有关更多信息，请参阅 Zeek 概述和我们的宣传文档《为什么选择》泽克？”

DNS 实用程序<a name="dnstools"></a>
--------------------------------------------

* [dnsgram](https://doc.powerdns.com/authoritative/manpages/dnsgram.1.html)：dnsgram 是用于间歇性解析器故障的调试工具。它需要一个或多个输入 PCAP 文件并生成 5 秒片段的统计数据，以便研究间歇性解析器问题。

* [dnsreplay](https://doc.powerdns.com/authoritative/manpages/dnsreplay.1.html)：Dnsreplay 记录问题和答案并将其重播到指定的名称服务器，然后报告匹配的答案百分比、更差或更好。然后将答案和其他一些指标与实际的指标和转储文件中找到的指标进行比较。

* [dnsscan](https://doc.powerdns.com/authoritative/manpages/dnsscan.1.html)：dnsscan 采用 PCAP 格式的一个或多个 INFILE，并生成每个查询类型的查询数量列表。

* [dnsscope](https://doc.powerdns.com/authoritative/manpages/dnsscope.1.html)：dnsscope 接受输入 PCAP 并生成一些简单的统计数据并将其输出到控制台。

* [dnswasher](https://doc.powerdns.com/authoritative/manpages/dnswasher.1.html)：dnswasher 获取 PCAP 格式的输入文件并写出 PCAP 文件，同时混淆最终用户 IP 地址。这对于在尝试保护用户隐私的同时与第三方共享数据非常有用。


文件提取<a name="fileextraction"></a>
--------------------------------------------

* [Chaosreader](https://github.com/brendangregg/Chaosreader)：一个免费软件工具，用于跟踪 TCP/UDP/... 会话并从 snoop 或 tcpdump 日志中获取应用程序数据。这是一种“any-snarf”程序，因为它将从网络流量日志中捕获的数据中获取 telnet 会话、FTP 文件、HTTP 传输（HTML、GIF、JPEG...）、SMTP 电子邮件等。创建一个 html 索引文件，链接到所有会话详细信息，包括 telnet、rlogin、IRC、X11 和 VNC 会话的实时重播程序；以及图像报告和 HTTP GET/POST 内容报告等报告。

* [Dsniff](https://www.monkey.org/~dugsong/dsniff/)：Dsniff 是用于网络审计和渗透测试的工具集合。 dsniff、filesnarf、mailsnarf、msgsnarf、urlsnarf 和 webspy 被动监视网络中感兴趣的数据（密码、电子邮件、文件等）。 arpspoof、dnsspoof 和 macof 有助于拦截攻击者通常无法获得的网络流量（例如，由于第 2 层交换）。 sshmitm 和 webmitm 通过利用 ad-hoc PKI 中的弱绑定，对重定向的 SSH 和 HTTPS 会话实施主动中间人攻击。

* [Foremost](https://github.com/jonstewart/foremost)：是一个控制台程序，用于根据页眉、页脚和内部数据结构恢复文件。此过程通常称为数据雕刻。 Foremost 可以处理图像文件，例如由 dd、Safeback、Encase 等生成的图像文件，或直接在驱动器上处理。页眉和页脚可以通过配置文件指定，也可以使用命令行开关指定内置文件类型。这些内置类型查看给定文件格式的数据结构，从而实现更可靠、更快速的恢复。

* [Justniffer](https://onotelli.github.io/justniffer/)：Justniffer 是一个网络协议分析器，可以捕获网络流量并以自定义方式生成日志，可以模拟 Apache Web 服务器日志文件、跟踪响应时间并从 HTTP 流量中提取所有“拦截”的文件。

* [NetworkMiner](https://www.netresec.com/index.ashx?page=NetworkMiner)：NetworkMiner 是一款适用于 Windows 的网络取证分析工具 (NFAT)（但也适用于 Linux / Mac OS X / FreeBSD）。 NetworkMiner 可以用作被动网络嗅探器/数据包捕获工具，以便检测操作系统、会话、主机名、开放端口等，而无需在网络上放置任何流量。 NetworkMiner 还可以解析 PCAP 文件以进行离线分析，并从 PCAP 文件重新生成/重新组装传输的文件和证书。

* [pcapfex](https://github.com/vikwin/pcapfex) - Packet CAPture Forensic Evidence eXtractor (pcapfex) 是一种从数据包捕获文件中查找并提取文件的工具。它的力量在于它的易用性。只需为其提供一个 pcap 文件，它就会尝试提取所有文件。它是一个可扩展的平台，因此可以轻松添加要识别和提取的其他文件类型。

* [Scalpel](https://github.com/sleuthkit/scalpel): Scalpel 是一个开源的数据雕刻工具。

* [Snort](https://www.snort.org/)：是由Sourcefire开发的开源网络入侵防御和检测系统(IDS/IPS)，现归思科所有。 Snort 结合了签名、协议和基于异常的检查的优点，是全球部署最广泛的 IDS/IPS 技术。

* [Tcpick](http://tcpick.sourceforge.net/)：是一个基于 libpcap 的文本模式嗅探器，可以跟踪、重新组装和重新排序 tcp 流。 Tcpick 能够将捕获的流保存在不同的文件中或将它们显示在终端中，因此它对于嗅探通过 ftp 或 http 传输的文件很有用。当连接关闭时，它可以在终端上以不同的显示模式显示所有流，如hexdump、hexdump + ascii、仅可打印字符、原始模式等。

* [Tcpxtract](http://tcpxtract.sourceforge.net/)：是一个根据文件签名从网络流量中提取文件的工具。根据文件类型页眉和页脚提取文件（有时称为“雕刻”）是一种古老的数据恢复技术。

* [Xplico](http://www.xplico.org/about)：Xplico 的目标是从互联网流量中提取所包含的应用程序数据。例如，Xplico 从 pcap 文件中提取每封电子邮件（POP、IMAP 和 SMTP 协议）、所有 HTTP 内容、每个 VoIP 呼叫 (SIP)、FTP、TFTP 等。 Xplico 不是网络协议分析器。 Xplico 是一个开源网络取证分析工具 (NFAT)。 Xplico 根据 GNU 通用公共许可证发布，部分脚本根据 Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported (CC BY-NC-SA 3.0) 许可证发布。

USB
---
### 捕捉工具
* [usbmon](https://www.kernel.org/doc/Documentation/usb/usbmon.txt) - Linux 内核的一个子系统，用于捕获 USB 数据包。
* [USBPcap](https://github.com/desowin/usbpcap) - 适用于 Windows 的解决方案。

### 分析
* [USBPcapOdinDumper](https://github.com/KOLANICH/USBPcapOdinDumper) - 将使用 Odin 或 [Heimdall](https://gitlab.com/BenjaminDobell/Heimdall) 刷新 Android 手机捕获的“usbmon”和“USBPcap”帧格式的 .pcap 文件转换为一组具有帧有效负载的文件。对于逆向工程很有用。具有模块化架构，可轻松转换为其他应用程序格式。


相关项目<a name="others"></a>
--------------------------------------

* [BPF for Ultrix](https://www.tcpdump.org/other/bpfext42.tar.Z)：BPF for Ultrix 4.2 的发行版，包含源代码和二进制模块。

* [BPF+](https://andrewbegel.com/papers/bpf.pdf)：在通用数据包过滤器架构中利用全局数据流优化 作者：Andrew Begel、Steven McCanne 和 Susan Graham。

* [FFT-FGN-C](ftp://ita.ee.lbl.gov/html/contrib/fft_fgn_c.html)：是一个用于合成一种称为分数高斯噪声的自相似过程的程序。该程序速度很快但很近似。分数高斯噪声只是自相似过程的一种。当使用此程序合成网络流量时，您必须记住，您所寻求的流量可能可以使用其他进程之一更好地建模。

* [Haka](http://www.haka-security.org/)：一种面向安全的开源语言，允许描述协议并对（实时）捕获的流量应用安全策略。哈卡语的范围是双重的。首先，它允许编写安全规则，以便过滤/更改/丢弃不需要的数据包并记录和报告恶意活动。其次，Haka 具有能够指定网络协议及其底层状态机的语法。

* [RIPE-NCC Hadoop for PCAP](https://github.com/RIPE-NCC/hadoop-pcap)：用于读取数据包捕获 (PCAP) 文件的 Hadoop 库。捆绑用于读取 PCAP 的代码。可在 MapReduce 作业中使用以本机读取 PCAP 文件。还具有 Hive 串行器/解串器 (SerDe)，可使用类似 SQL 的命令查询 PCAP。

* [WIDE项目的流量数据存储库](https://www2.sonycsl.co.jp/person/kjc/papers/freenix2000/)：对于网络研究人员和运营商来说，了解网络流量的趋势并发现网络流量的异常变得越来越重要。本文描述了 WIDE 项目中正在进行的一项工作，即收集一组免费工具来构建包含骨干流量详细信息的流量数据存储库。流量痕迹由 tcpdump 收集，删除隐私信息后，痕迹向公众开放。我们回顾了用户隐私问题，然后回顾了用于构建 WIDE 流量存储库的工具。我们将在 IPv6 部署的早期阶段报告当前状态和调查结果。

* [Usenix93 Paper on BPF](https://www.tcpdump.org/papers/bpf-usenix93.pdf): libpcap 接口支持基于 BSD 数据包过滤器架构的过滤机制。 BPF 在 1993 年 Winter Usenix 论文“The BSD Packet Filter: A New Architecture for User-level Packet Capture”中进行了描述。


贡献者
------------

感谢所有贡献者❤

[![awesome-pcaptools contributors](https://contrib.rocks/image?repo=caesar0301/awesome-pcaptools "awesome-pcaptools contributors")](https://github.com/caesar0301/awesome-pcaptools/graphs/contributors)
