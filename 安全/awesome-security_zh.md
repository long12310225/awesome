# 出色的安全性

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

一系列很棒的软件、库、文档、书籍、资源和有关安全的精彩内容。

受到 [awesome-php](https://github.com/ziadoz/awesome-php)、[awesome-python](https://github.com/vinta/awesome-python) 的启发。

感谢所有[贡献者](https://github.com/sbilly/awesome-security/graphs/contributors)，你们太棒了，没有你们就不可能！目标是建立一个分类的、由社区驱动的知名资源集合。

- [出色的安全性](#awesome-security)
  - [Network](#network)
    - [扫描/渗透测试](#scanning--pentesting)
    - [监控/记录](#monitoring--logging)
    - [IDS / IPS / 主机 IDS / 主机 IPS](#ids--ips--host-ids--host-ips)
    - [蜜罐/蜜网](#honey-pot--honey-net)
    - [全数据包捕获/取证](#full-packet-capture--forensic)
    - [Sniffer](#sniffer)
    - [安全信息和事件管理](#security-information--event-management)
    - [VPN](#vpn)
    - [快速数据包处理](#fast-packet-processing)
    - [Firewall](#firewall)
    - [Anti-Spam](#anti-spam)
    - [Docker](#docker-images-for-penetration-testing--security)
  - [Endpoint](#endpoint)
    - [防病毒/防恶意软件](#anti-virus--anti-malware)
    - [内容解除武装和重建](#content-disarm--reconstruct)
    - [配置管理](#configuration-management)
    - [Authentication](#authentication)
    - [手机/安卓/iOS](#mobile--android--ios)
    - [Forensics](#forensics)
  - [威胁情报](#threat-intelligence)
  - [社会工程](#social-engineering)
  - [Web](#web)
    - [Organization](#organization)
    - [网络应用防火墙](#web-application-firewall)
    - [扫描/渗透测试](#scanning--pentesting-1)
    - [运行时应用程序自我保护](#runtime-application-self-protection)
    - [Development](#development)
  - [红队基础设施部署](#red-team-infrastructure-deployment)
  - [漏洞利用和有效负载](#exploits--payloads)
  - [Usability](#usability)
  - [大数据](#big-data)
  - [DevOps](#devops)
  - [Terminal](#terminal)
  - [操作系统](#operating-systems)
    - [在线资源](#online-resources)
  - [Datastores](#datastores)
  - [预防欺诈](#fraud-prevention)
  - [EBooks](#ebooks)
  - [其他很棒的清单](#other-awesome-lists)
    - [其他很棒的安全列表](#other-security-awesome-lists)
    - [其他常见的很棒的列表](#other-common-awesome-lists)
  - [Contributing](#contributing)

------

## 网络

### 网络架构

- [Network-segmentation-cheat-sheet](https://github.com/sergiomarotco/Network-segmentation-cheat-sheet) - 创建该项目的目的是发布任何公司的企业网络分段的最佳实践。总的来说，本项目的方案适合任何公司。

### 扫描/渗透测试

- [OpenVAS](http://www.openvas.org/) - OpenVAS 是一个由多种服务和工具组成的框架，提供全面且强大的漏洞扫描和漏洞管理解决方案。
- [Metasploit Framework](https://github.com/rapid7/metasploit-framework) - 用于针对远程目标计算机开发和执行漏洞利用代码的工具。其他重要的子项目包括操作码数据库、shellcode 存档和相关研究。
- [Kali](https://www.kali.org/) - Kali Linux 是一个源自 Debian 的 Linux 发行版，专为数字取证和渗透测试而设计。 Kali Linux 预装了许多渗透测试程序，包括 nmap（端口扫描器）、Wireshark（数据包分析器）、John the Ripper（密码破解器）和 Aircrack-ng（用于渗透测试无线 LAN 的软件套件）。
- [tsurugi](https://tsurugi-linux.org/) - 高度定制的 Linux 发行版，旨在支持 DFIR 调查、恶意软件分析和 OSINT 活动。它基于Ubuntu 20.04（64位，带有5.15.12自定义内核）
- [pig](https://github.com/rafael-santiago/pig) - 一个 Linux 数据包制作工具。
- [scapy](https://github.com/gpotter2/awesome-scapy) - Scapy：基于 python 的交互式数据包操作程序和库。
- [Pompem](https://github.com/rfunix/Pompem) - Pompem 是一个开源工具，旨在自动搜索主要数据库中的漏洞。用Python开发，具有高级搜索系统，从而方便了渗透测试人员和道德黑客的工作。在当前版本中，在数据库中执行搜索：Exploit-db、1337day、Packetstorm Security...
- [Nmap](https://nmap.org) - Nmap 是一个免费的开源实用程序，用于网络发现和安全审核。
- [Amass](https://github.com/owasp-amass/amass) - Amass 通过抓取最大数量的不同数据源、递归暴力破解、网络档案爬行、排列和更改名称、反向 DNS 扫描和其他技术来执行 DNS 子域枚举。
- [Anevicon](https://github.com/rozgo/anevicon) - 最强大的基于 UDP 的负载生成器，用 Rust 编写。
- [Finshir](https://github.com/isgasho/finshir) - 一个协程驱动的低速流量生成器，用 Rust 编写。
- [Legion](https://github.com/GoVanguard/legion) - 开源半自动发现和侦察网络渗透测试框架。
- [Lonkero](https://github.com/bountyyfi/lonkero) - 企业级 Web 漏洞扫描器，具有 60 多个攻击模块，采用 Rust 内置，用于渗透测试和安全评估。
- [Sublist3r](https://github.com/aboul3la/Sublist3r) - 渗透测试人员的快速子域枚举工具
- [RustScan](https://github.com/RustScan/RustScan) - 使用 Rust 加快 Nmap 扫描速度。将 17 分钟的 Nmap 扫描缩短至 19 秒。
- [Boofuzz](https://github.com/jtpereyda/boofuzz) - 模糊测试引擎和模糊测试框架。
- [monsoon](https://github.com/RedTeamPentesting/monsoon) - 非常灵活且快速的交互式 HTTP 枚举/模糊测试。
- [Netz](https://github.com/spectralops/netz) - 使用 zgrab2 等发现互联网范围内的错误配置。
- [Deepfence ThreatMapper](https://github.com/deepfence/ThreatMapper) - Apache v2，适用于 kubernetes、虚拟机和无服务器的强大运行时漏洞扫描器。
- [Deepfence SecretScanner](https://github.com/deepfence/SecretScanner) - 在容器映像和文件系统中查找秘密和密码。
- [Cognito Scanner](https://github.com/padok-team/cognito-scanner) - 用于渗透测试 Cognito AWS 实例的 CLI 工具。它实施三种攻击：不需要的帐户创建、帐户预言机和身份池升级

### 监控/记录
- [BoxyHQ](https://github.com/retracedhq/retraced) - 用于安全性和合规性审核日志记录的开源 API。
- [justniffer](http://justniffer.sourceforge.net/) - Justniffer 是一款网络协议分析器，可以捕获网络流量并以自定义方式生成日志，可以模拟 Apache Web 服务器日志文件、跟踪响应时间并从 HTTP 流量中提取所有“拦截”的文件。
- [httpry](http://dumpsterventures.com/jason/httpry/) - httpry 是一个专门的数据包嗅探器，设计用于显示和记录 HTTP 流量。它本身并不是为了执行分析，而是为了捕获、解析和记录流量以供以后分析。它可以实时运行，显示解析的流量，也可以作为记录到输出文件的守护进程。它被编写得尽可能轻量和灵活，以便它可以轻松适应不同的应用程序。
- [ngrep](http://ngrep.sourceforge.net/) - ngrep 努力提供 GNU grep 的大部分通用功能，并将它们应用到网络层。 ngrep 是一个 pcap 感知工具，允许您指定扩展的正则或十六进制表达式来匹配数据包的数据有效负载。它目前可识别跨以太网、PPP、SLIP、FDDI、令牌环和空接口的 IPv4/6、TCP、UDP、ICMPv4/6、IGMP 和 Raw，并以与更常见的数据包嗅探工具（例如 tcpdump 和 snoop）相同的方式理解 BPF 过滤器逻辑。
- [passivedns](https://github.com/gamelinux/passivedns) - 一种被动收集 DNS 记录以帮助事件处理、网络安全监控 (NSM) 和一般数字取证的工具。 PassiveDNS 嗅探来自接口的流量或读取 pcap 文件并将 DNS 服务器答案输出到日志文件。 PassiveDNS 可以在内存中缓存/聚合重复的 DNS 答案，限制日志文件中的数据量，而不会丢失 DNS 答案中的本质。
- [sagan](http://sagan.quadrantsec.com/) - Sagan 使用“Snort like”引擎和规则来分析日志（syslog/事件日志/snmptrap/netflow/等）。
- [ntopng](http://www.ntop.org/products/traffic-analysis/ntop/) - Ntopng 是一个网络流量探测器，显示网络使用情况，类似于流行的 top Unix 命令的作用。
- [Fibratus](https://github.com/rabbitstack/fibratus) - Fibratus 是一个用于探索和跟踪 Windows 内核的工具。它能够捕获大部分 Windows 内核活动 - 进程/线程创建和终止、文件系统 I/O、注册表、网络活动、DLL 加载/卸载等等。 Fibratus 有一个非常简单的 CLI，它封装了启动内核事件流收集器、设置内核事件过滤器或运行称为filaments 的轻量级 Python 模块的机制。
- [opensnitch](https://github.com/evilsocket/opensnitch) - OpenSnitch 是 Little Snitch 应用防火墙的 GNU/Linux 端口
- [wazuh](https://github.com/wazuh/wazuh) - Wazuh 是一个免费的开源平台，用于威胁预防、检测和响应。它能够监视文件系统更改、系统调用和库存更改。
- [Matano](https://github.com/matanolabs/matano)：AWS 上的开源无服务器安全湖平台，可让您将 PB 级安全数据摄取、存储和分析到 Apache Iceberg 数据湖中，并以代码形式运行实时 Python 检测。
- [Falco](https://falco.org/) - 云原生运行时安全项目和事实上的 Kubernetes 威胁检测引擎现已成为 CNCF 的一部分。
- [VAST](https://github.com/tenzir/vast) - 用于结构化事件数据的开源安全数据管道引擎，支持大容量遥测摄取、压缩和检索；专为安全内容执行、引导威胁搜寻和大规模调查而构建。
- [Substation](https://github.com/brexhq/substation) - Substation 是一个用 Go 编写的云原生数据管道和转换工具包。
- [Sigma2KQL](https://github.com/Khadinxc/Sigma2KQL) - 所有 SIGMA 规则的存储库均转换为 KQL，每周运行一次以更新存储库并与 SIGMA 规则存储库的最新版本保持一致。
- [Sigma2SPL](https://github.com/Khadinxc/Sigma2SPL) - 所有 SIGMA 规则的存储库均转换为 SPL，每周运行一次以更新存储库并与 SIGMA 规则存储库的最新版本保持一致。
- [TerraSigma](https://github.com/Khadinxc/TerraSigma) - 转换为 Microsoft Sentinel Terraform 计划分析资源的所有 SIGMA 规则的存储库。该存储库按每周计划运行，以更新存储库并与 SIGMA 规则存储库的最新版本保持一致。为规则完成正确的实体映射，以确保存储库是即插即用的。

### IDS / IPS / 主机 IDS / 主机 IPS

- [Snort](https://www.snort.org/) - Snort是一个免费开源的网络入侵防御系统（NIPS）和网络入侵检测系统（NIDS），由Martin Roesch于1998年创建。Snort现在由Sourcefire开发，Roesch是Sourcefire的创始人和CTO。 2009 年，Snort 作为“有史以来最伟大的开源软件”之一进入 InfoWorld 的开源名人堂。
- [Zeek](https://zeek.org/) - Zeek 是一个功能强大的网络分析框架，与您可能知道的典型 IDS 有很大不同。
  - [zeek2es](https://github.com/corelight/zeek2es) - 一个将 Zeek 日志转换为 Elastic/OpenSearch 的开源工具。  您还可以从 Zeek 的 TSV 日志输出纯 JSON！
- [DrKeithJones.com](https://drkeithjones.com) - 关于网络安全和网络安全监控的博客。
- [OSSEC](https://ossec.github.io/) - 全面的开源 HIDS。不适合胆小的人。需要花一些时间来了解它是如何工作的。执行日志分析、文件完整性检查、策略监控、rootkit 检测、实时警报和主动响应。它可以在大多数操作系统上运行，包括 Linux、MacOS、Solaris、HP-UX、AIX 和 Windows。大量合理的文档。最佳点是中型到大型部署。
- [Suricata](http://suricata-ids.org/) - Suricata 是一款高性能网络 IDS、IPS 和网络安全监控引擎。开源并由社区运营的非营利基金会开放信息安全基金会 (OISF) 所有。 Suricata 由 OISF 及其支持供应商开发。
- [Security Onion](http://blog.securityonion.net/) - Security Onion 是一个用于入侵检测、网络安全监控和日志管理的 Linux 发行版。它基于 Ubuntu，包含 Snort、Suricata、Zeek、OSSEC、Sguil、Squert、Snorby、ELSA、Xplico、NetworkMiner 和许多其他安全工具。易于使用的设置向导使您可以在几分钟内为您的企业构建一支分布式传感器大军！
- [sshwatch](https://github.com/marshyski/sshwatch) - 用于 SSH 的 IPS 类似于用 Python 编写的 DenyHosts。  它还可以在日志中收集攻击期间有关攻击者的信息。
- [Stealth](https://fbb-git.gitlab.io/stealth/) - 文件完整性检查器几乎不留下任何沉积物。控制器从另一台机器运行，这使得攻击者很难知道正在通过 SSH 以定义的伪随机间隔检查文件系统。强烈推荐用于中小型部署。
- [AIEngine](https://bitbucket.org/camp0/aiengine) - AIEngine是下一代交互式/可编程Python/Ruby/Java/Lua数据包检测引擎，具有无需人工干预的学习能力、NIDS（网络入侵检测系统）功能、DNS域分类、网络收集器、网络取证等功能。
- [Denyhosts](http://denyhosts.sourceforge.net/) - 阻止基于 SSH 字典的攻击和暴力攻击。
- [Fail2Ban](http://www.fail2ban.org/wiki/index.php/Main_Page) - 扫描日志文件并对显示恶意行为的 IP 采取操作。
- [SSHGuard](http://www.sshguard.net/) - 一个除了SSH之外还可以保护服务的软件，用C语言编写
- [Lynis](https://cisofy.com/lynis/) - 适用于 Linux/Unix 的开源安全审计工具。
- [CrowdSec](https://github.com/crowdsecurity/crowdsec) - CrowdSec 是一款免费、现代的协作行为检测引擎，并配有全球 IP 信誉网络。它继承了 Fail2Ban 的理念，但与 IPV6 兼容并且速度提高了 60 倍（Go 与 Python），使用 Grok 模式来解析日志并使用 YAML 场景来识别行为。 CrowdSec 专为基于现代云/容器/虚拟机的基础设施而设计（通过解耦检测和修复）。一旦检测到，您可以使用各种保镖（防火墙块、nginx http 403、验证码等）来补救威胁，而攻击性 IP 可以发送到 CrowdSec 进行管理，然后在所有用户之间共享，以进一步加强社区
- [wazuh](https://github.com/wazuh/wazuh) - Wazuh 是一个免费开源 XDR 平台，用于威胁预防、检测和响应。它能够保护本地、虚拟化、容器化和基于云的环境中的工作负载。适用于各种部署的出色工具，它包括 SIEM 功能（索引 + 搜索 + WUI）。

### 蜜罐/蜜网

- [awesome-honeypots](https://github.com/paralax/awesome-honeypots) - 规范的很棒的蜜罐列表。
- [HoneyPy](https://github.com/foospidy/HoneyPy) - HoneyPy 是一个低到中等交互的蜜罐。它旨在易于：部署、使用插件扩展功能以及应用自定义配置。
- [Conpot](http://conpot.org/) - ICS/SCADA 蜜罐。 Conpot 是一个低交互服务器端工业控制系统蜜罐，旨在易于部署、修改和扩展。通过提供一系列通用工业控制协议，我们创建了构建您自己的系统的基础知识，能够模拟复杂的基础设施，让对手相信他刚刚发现了一个巨大的工业综合体。为了提高欺骗能力，我们还提供了服务自定义人机界面的可能性，以增加蜜罐的攻击面。可以人为地延迟服务的响应时间，以模仿系统在恒定负载下的行为。因为我们提供完整的协议栈，所以可以通过高效的 HMI 访问 Conpot 或通过实际硬件进行扩展。 Conpot 是在蜜网项目的保护下、在几个非常大的巨头的肩膀上开发的。
- [Amun](https://github.com/zeroq/amun) - Amun 基于 Python 的低交互蜜罐。
- [Glastopf](http://glastopf.org/) - Glastopf 是一个蜜罐，它模拟数千个漏洞，从针对 Web 应用程序的攻击中收集数据。其背后的原理非常简单：向利用 Web 应用程序的攻击者回复正确的响应。
- [Kippo](https://github.com/desaster/kippo) - Kippo 是一个中等交互的 SSH 蜜罐，旨在记录暴力攻击，最重要的是，记录攻击者执行的整个 shell 交互。
- [Kojoney](http://kojoney.sourceforge.net/) - Kojoney 是一个模拟 SSH 服务器的低级交互蜜罐。该守护进程是使用 Twisted Conch 库用 Python 编写的。
- [HonSSH](https://github.com/tnich/honssh) - HonSSH是一个高交互性的蜜罐解决方案。 HonSSH 将位于攻击者和蜜罐之间，在它们之间创建两个独立的 SSH 连接。
- [Bifrozt](http://sourceforge.net/projects/bifrozt/) - Bifrozt 是一款带有 DHCP 服务器的 NAT 设备，通常部署有一个直接连接互联网的网卡和一个连接内部网络的网卡。 Bifrozt 与其他标准 NAT 设备的区别在于它能够充当攻击者和蜜罐之间的透明 SSHv2 代理。如果您在 Bifrozt 的内部网络上部署了 SSH 服务器，它会将所有交互以纯文本形式记录到 TTY 文件中，以便稍后查看并捕获已下载的任何文件的副本。您无需在内部 SSH 服务器上安装任何其他软件、编译任何内核模块或使用特定版本或类型的操作系统即可实现此功能。它将限制出站流量到一定数量的端口，并在超过某些限制时开始丢弃这些端口上的出站数据包。
- [HoneyDrive](http://bruteforce.gr/honeydrive) - HoneyDrive 是首屈一指的蜜罐 Linux 发行版。它是安装了 Xubuntu Desktop 12.04.4 LTS 版本的虚拟设备 (OVA)。它包含超过 10 个预安装和预配置的蜜罐软件包，例如 Kippo SSH 蜜罐、Dionaea 和 Amun 恶意软件蜜罐、Honeyd 低交互蜜罐、Glastopf Web 蜜罐和 Wordpot、Conpot SCADA/ICS 蜜罐、Thug 和 PhoneyC honeyclients 等等。此外，它还包括许多有用的预配置脚本和实用程序，用于分析、可视化和处理它可以捕获的数据，例如 Kippo-Graph、Honeyd-Viz、DionaeaFR、ELK 堆栈等等。最后，该发行版中还提供了近 90 个知名的恶意软件分析、取证和网络监控相关工具。
- [Cuckoo Sandbox](http://www.cuckoosandbox.org/) - Cuckoo Sandbox 是一款用于自动分析可疑文件的开源软件。为此，它利用自定义组件来监视恶意进程在隔离环境中运行时的行为。
- [T-Pot Honeypot Distro](http://dtag-dev-sec.github.io/mediator/feature/2017/11/07/t-pot-17.10.html) - T-Pot 基于 Ubuntu Server 16/17.x LTS 的网络安装程序。蜜罐守护进程以及所使用的其他支持组件已使用 docker 进行容器化。这允许我们在同一网络接口上运行多个蜜罐守护进程，同时保持较小的占用空间并将每个蜜罐限制在其自己的环境中。在 vanilla Ubuntu 上安装 - [T-Pot Autoinstall](https://github.com/dtag-dev-sec/t-pot-autoinstall) - 此脚本将在新的 Ubuntu 16.04.x LTS（64 位）上安装 T-Pot 16.04/17.10。它旨在用于托管服务器，其中提供了 Ubuntu 基础映像，并且无法安装自定义 ISO 映像。在 VMware 中的 vanilla Ubuntu 16.04.3 上成功进行了测试。

### 全数据包捕获/取证

- [tcpflow](https://github.com/simsong/tcpflow) - tcpflow 是一个捕获作为 TCP 连接（流）一部分传输的数据的程序，并以方便协议分析和调试的方式存储数据。每个 TCP 流都存储在其自己的文件中。因此，典型的 TCP 流将存储在两个文件中，每个文件对应一个方向。 tcpflow 还可以处理存储的“tcpdump”数据包流。
- [Deepfence PacketStreamer](https://github.com/deepfence/PacketStreamer) - 高性能远程数据包捕获和收集工具，适用于云原生环境的分布式tcpdump。
- [Xplico](http://www.xplico.org/) - Xplico 的目标是从互联网流量中提取所包含的应用程序数据。例如，Xplico 从 pcap 文件中提取每封电子邮件（POP、IMAP 和 SMTP 协议）、所有 HTTP 内容、每个 VoIP 呼叫 (SIP)、FTP、TFTP 等。 Xplico 不是网络协议分析器。 Xplico 是一个开源网络取证分析工具 (NFAT)。
- [Moloch](https://github.com/aol/moloch) - Moloch 是一个开源的大规模 IPv4 数据包捕获 (PCAP)、索引和数据库系统。提供了一个简单的 Web 界面用于 PCAP 浏览、搜索和导出。公开的 API 允许直接下载 PCAP 数据和 JSON 格式的会话数据。简单的安全性是通过使用 HTTPS 和 HTTP 摘要密码支持或通过在前面使用 apache 来实现的。 Moloch 并不是要取代 IDS 引擎，而是与它们一起工作，以标准 PCAP 格式存储和索引所有网络流量，从而提供快速访问。 Moloch 旨在跨多个系统部署，并且可以扩展以处理每秒数千兆位的流量。
- [OpenFPC](http://www.openfpc.org) - OpenFPC 是一组工具，结合起来提供轻量级全包网络流量记录器和缓冲系统。它的设计目标是允许非专家用户在 COTS 硬件上部署分布式网络流量记录器，同时集成到现有的警报和日志管理工具中。
- [Dshell](https://github.com/USArmyResearchLab/Dshell) - Dshell 是一个网络取证分析框架。实现插件的快速开发以支持网络数据包捕获的解析。
- [stenographer](https://github.com/google/stenographer) - Stenographer 是一种数据包捕获解决方案，旨在快速将所有数据包存储到磁盘，然后提供对这些数据包子集的简单、快速访问。

### 嗅探器

- [wireshark](https://www.wireshark.org) - Wireshark 是一款免费的开源数据包分析器。它用于网络故障排除、分析、软件和通信协议开发以及教育。 Wireshark 与 tcpdump 非常相似，但具有图形前端，以及一些集成的排序和过滤选项。
- [netsniff-ng](http://netsniff-ng.org/) - netsniff-ng 是一个免费的 Linux 网络工具包，如果您愿意的话，它是您日常 Linux 网络管道的瑞士军刀。它的性能增益是通过零复制机制实现的，因此在数据包接收和传输时，内核不需要将数据包从内核空间复制到用户空间，反之亦然。
- [Live HTTP headers ](https://addons.mozilla.org/en-US/firefox/addon/http-header-live/) - Live HTTP headers 是一个免费的 Firefox 插件，可以实时查看您的浏览器请求。它显示请求的完整标头，可用于查找实现中的安全漏洞。

### 安全信息和事件管理

- [Prelude](https://www.prelude-siem.org/) - Prelude 是一个通用的“安全信息和事件管理”(SIEM) 系统。 Prelude 收集、规范化、排序、汇总、关联和报告所有与安全相关的事件，与引发此类事件的产品品牌或许可证无关； Prelude是“无代理”的。
- [OSSIM](https://www.alienvault.com/open-threat-exchange/projects) - OSSIM 提供了安全专业人员所需的 SIEM 产品的所有功能 - 事件收集、标准化和关联。
- [FIR](https://github.com/certsocietegenerale/FIR) - 快速事件响应，一个网络安全事件管理平台。
- [LogESP](https://github.com/dogoncouch/LogESP) - 开源 SIEM（安全信息和事件管理系统）。
- [wazuh](https://github.com/wazuh/wazuh) - Wazuh 是一款免费、开源、企业级安全监控解决方案，用于威胁检测、完整性监控、事件响应和合规性。它可以处理 OpenSearch 分支和自定义 WUI 支持的大量数据。
- [VAST](https://github.com/tenzir/vast) - 用于结构化事件数据的开源安全数据管道引擎，支持大容量遥测摄取、压缩和检索；专为安全内容执行、引导威胁搜寻和大规模调查而构建。
- [Matano](https://github.com/matanolabs/matano) - AWS 上的开源无服务器安全湖平台可让您将 PB 级安全数据摄取、存储和分析到 Apache Iceberg 数据湖中，并以代码形式运行实时 Python 检测。

### VPN

- [OpenVPN](https://openvpn.net/) - OpenVPN 是一种开源软件应用程序，它实现虚拟专用网络 (VPN) 技术，用于在路由或桥接配置和远程访问设施中创建安全的点对点或站点到站点连接。它使用自定义安全协议，利用 SSL/TLS 进行密钥交换。
- [Firezone](https://github.com/firezone/firezone) - 基于 WireGuard 构建的适用于 Linux 的开源 VPN 服务器和出口防火墙，可以轻松管理对公司专用网络的安全远程访问。 Firezone 易于设置（所有依赖项都通过 Chef Omnibus 捆绑在一起）、安全、高性能且可自托管。
- [TorForge](https://github.com/jery0843/torforge) - 高级透明 Tor 代理，具有内核级 iptables 路由、后量子加密 (Kyber768)、终止开关、隐写模式和 AI 驱动的电路选择。

### 快速数据包处理

- [DPDK](http://dpdk.org/) - DPDK 是一组用于快速数据包处理的库和驱动程序。
- [PFQ](https://github.com/pfq/PFQ) - PFQ 是一个专为 Linux 操作系统设计的功能网络框架，可实现高效的数据包捕获/传输（10G 及以上）、内核内功能处理以及跨套接字/端点的数据包引导。
- [PF_RING](http://www.ntop.org/products/packet-capture/pf_ring/) - PF_RING 是一种新型网络套接字，可显着提高数据包捕获速度。
- [PF_RING ZC (Zero Copy)](http://www.ntop.org/products/packet-capture/pf_ring/pf_ring-zc-zero-copy/) - PF_RING ZC（零复制）是一种灵活的数据包处理框架，允许您以任何数据包大小实现 1/10 Gbit 线速数据包处理（RX 和 TX）。它实现零复制操作，包括进程间和虚拟机间 (KVM) 通信的模式。
- [PACKET_MMAP/TPACKET/AF_PACKET](https://elixir.bootlin.com/linux/latest/source/Documentation/networking/packet_mmap.rst) - 使用PACKET_MMAP来提高Linux中捕获和传输过程的性能是可以的。
- [netmap](http://info.iet.unipi.it/~luigi/netmap/) - netmap 是高速数据包 I/O 的框架。与其配套的 VALE 软件开关一起，它作为单个内核模块实现，可用于 FreeBSD、Linux，现在也可用于 Windows。

### 防火墙

- [pfSense](https://www.pfsense.org/) - 防火墙和路由器 FreeBSD 发行版。
- [OPNsense](https://opnsense.org/) - 是一个开源、易于使用且易于构建的基于 FreeBSD 的防火墙和路由平台。 OPNsense 包含昂贵的商业防火墙中可用的大部分功能，在许多情况下甚至更多。它带来了商业产品的丰富功能集以及开放和可验证来源的优势。
- [fwknop](https://www.cipherdyne.org/fwknop/) - 通过防火墙中的单数据包授权保护端口。

### 反垃圾邮件

- [Spam Scanner](https://github.com/spamscanner) - 反垃圾邮件扫描服务和反垃圾邮件 API，作者：[@niftylettuce](https://github.com/niftylettuce)。
- [rspamd](https://github.com/rspamd/rspamd) - 快速、免费、开源的垃圾邮件过滤系统。
- [SpamAssassin](https://spamassassin.apache.org/) - 一款强大且流行的电子邮件垃圾邮件过滤器，采用多种检测技术。
- [Scammer-List](https://scammerlist.now.sh/) - 基于免费开源 AI 的诈骗和垃圾邮件查找器，具有免费 API

### 用于渗透测试和安全的 Docker 镜像

- `docker pull kalilinux/kali-linux-docker` [官方 Kali Linux](https://hub.docker.com/r/kalilinux/kali-linux-docker/)
- `docker pull owasp/zap2docker-stable` - [官方 OWASP ZAP](https://github.com/zaproxy/zaproxy)
- `docker pull wpscanteam/wpscan` - [官方 WPScan](https://hub.docker.com/r/wpscanteam/wpscan/)
- `docker pull remnux/metasploit` - [docker-metasploit](https://hub.docker.com/r/remnux/metasploit/)
- `docker pull Citizenstig/dvwa` - [该死的易受攻击的 Web 应用程序 (DVWA)](https://hub.docker.com/r/citizenstig/dvwa/)
- `docker pull wpscanteam/vulnerablewordpress` - [有漏洞的 WordPress 安装](https://hub.docker.com/r/wpscanteam/vulnerablewordpress/)
- `docker pull hmlio/vaas-cve-2014-6271` - [漏洞即服务：Shellshock](https://hub.docker.com/r/hmlio/vaas-cve-2014-6271/)
- `docker pull hmlio/vaas-cve-2014-0160` - [漏洞即服务：Heartbleed](https://hub.docker.com/r/hmlio/vaas-cve-2014-0160/)
- `docker pull opendns/security-ninjas` - [安全忍者](https://hub.docker.com/r/opendns/security-ninjas/)
- `docker pull diogomonica/docker-bench-security` - [Docker 安全工作台](https://hub.docker.com/r/diogomonica/docker-bench-security/)
- `docker pull ismisepaul/securityshepherd` - [OWASP Security Shepherd](https://hub.docker.com/r/ismisepaul/securityshepherd/)
- `docker pull danmx/docker-owasp-webgoat` - [OWASP WebGoat 项目 docker 镜像](https://hub.docker.com/r/danmx/docker-owasp-webgoat/)
- `docker-compose build && docker-compose up` - [OWASP NodeGoat](https://github.com/owasp/nodegoat#option-3---run-nodegoat-on-docker)
- `docker pull Citizentig/nowasp` - [OWASP Mutillidae II Web 渗透测试实践应用](https://hub.docker.com/r/citizenstig/nowasp/)
- `docker pull bkimminich/juice-shop` - [OWASP 果汁店](https://hub.docker.com/r/bkimminich/juice-shop)
- `docker pull jeroenwillemsen/wrongsecrets`- [OWASP WrongSecrets](https://hub.docker.com/r/jeroenwillemsen/wrongsecrets)
- `docker run -dit --name trd -p 8081:80 cylabs/cy-threat-response` - [Cyware 威胁响应 Docker](https://hub.docker.com/r/cylabs/cy-threat-response)
- `docker-compose -d up` - [cicd-goat](https://github.com/cider-security-research/cicd-goat)

## 端点

### 防病毒/防恶意软件

- [Fastfinder](https://github.com/codeyourweb/fastfinder) - 快速可定制的跨平台可疑文件查找器。支持 md5/sha1/sha256 哈希、垃圾/通配符字符串、正则表达式和 YARA 规则。可以轻松打包部署在任何 Windows / Linux 主机上。
- [Linux Malware Detect](https://www.rfxn.com/projects/linux-malware-detect/) - 针对 Linux 的恶意软件扫描程序，针对共享托管环境中面临的威胁而设计。
- [LOKI](https://github.com/Neo23x0/Loki) - 简单的妥协指标和事件响应扫描仪
- [rkhunter](http://rkhunter.sourceforge.net/) - Linux 下的 Rootkit 猎人
- [ClamAv](http://www.clamav.net/) - ClamAV® 是一款开源防病毒引擎，用于检测木马、病毒、恶意软件和其他恶意威胁。

### 内容解除武装和重建

- [DocBleach](https://github.com/docbleach/DocBleach) - 开源内容解除和重建软件，可清理 Office、PDF 和 RTF 文档。

### 配置管理

- [Fleet device management](https://github.com/fleetdm/fleet) - Fleet 是适用于服务器和工作站的轻量级可编程遥测平台。从您的所有设备和操作系统获取全面、可定制的数据。
- [Rudder](http://www.rudder-project.org/) - Rudder 是一种易于使用、网络驱动、基于角色的 IT 基础设施自动化和合规性解决方案。自动执行常见的系统管理任务（安装、配置）；随着时间的推移强制配置（配置一次就好，确保配置有效并自动修复更好）；所有被管理节点的清单；用于配置和管理节点及其配置的 Web 界面；按配置和/或按节点进行合规性报告。

### 认证

- [google-authenticator](https://github.com/google/google-authenticator) - Google Authenticator 项目包括针对多个移动平台的一次性密码生成器的实现，以及可插入身份验证模块 (PAM)。一次性密码是使用开放身份验证计划 (OATH)（与 OAuth 无关）开发的开放标准生成的。这些实现支持 RFC 4226 中指定的基于 HMAC 的一次性密码 (HOTP) 算法和 RFC 6238 中指定的基于时间的一次性密码 (TOTP) 算法。 [教程：如何在 Linux 上设置 SSH 登录的双因素身份验证](http://xmodulo.com/two-factor-authentication-ssh-login-linux.html)
- [Stegcloak](https://github.com/kurolabs/stegcloak) - 安全地为任何书面文本分配数字真实性

### 手机/安卓/iOS

- [android-security-awesome](https://github.com/ashishb/android-security-awesome) - Android安全相关资源集合。学术界和工业界正在开展大量工作，开发用于对 Android 应用程序进行动态分析、静态分析和逆向工程的工具。
- [SecMobi Wiki](http://wiki.secmobi.com/) - 移动安全资源的集合，包括文章、博客、书籍、小组、项目、工具和会议。 *
- [OWASP Mobile Security Testing Guide](https://github.com/OWASP/owasp-mstg) - 移动应用程序安全测试和逆向工程的综合手册。
- [OSX Security Awesome](https://github.com/kai5263499/osx-security-awesome) - OSX 和 iOS 安全资源的集合
- [Themis](https://github.com/cossacklabs/themis) - 用于保护敏感数据的高级多平台加密框架：具有前向保密和安全数据存储的安全消息传递（AES256GCM），适合构建端到端加密应用程序。
- [Mobile Security Wiki](https://mobilesecuritywiki.com/) - 移动安全资源的集合。
- [Apktool](https://github.com/iBotPeaches/Apktool) - 一款对 Android apk 文件进行逆向工程的工具。
- [jadx](https://github.com/skylot/jadx) - 用于从 Android Dex 和 Apk 文件生成 Java 源代码的命令行和 GUI 工具。
- [enjarify](https://github.com/Storyyeller/enjarify) - 用于将 Dalvik 字节码转换为等效 Java 字节码的工具。
- [Android Storage Extractor](https://github.com/51j0/Android-Storage-Extractor) - 一款一键提取 Android 应用程序本地数据存储的工具。
- [Quark-Engine](https://github.com/quark-engine/quark-engine) - 一种忽略混淆的 Android 恶意软件评分系统。
- [dotPeek](https://www.jetbrains.com/decompiler/) - 基于 ReSharper 捆绑反编译器的免费独立工具。
- [hardened_malloc](https://github.com/GrapheneOS/hardened_malloc) - 专为现代系统设计的强化分配器。它已集成到 Android 的 Bionic libc 中，并且可以与 musl 和 glibc 一起作为动态库在外部使用，以便在其他基于 Linux 的平台上使用。随着时间的推移，它将获得更多的可移植性/集成性。
- [AMExtractor](https://github.com/ir193/AMExtractor) - 即使没有内核源代码，AMExtractor 也可以转储 Android 设备的物理内容。
- [frida](https://github.com/frida/frida) - 面向开发人员、逆向工程师和安全研究人员的动态检测工具包。
- [UDcide](https://github.com/UDcide/udcide) - Android 恶意软件行为编辑器。
- [reFlutter](https://github.com/ptswarm/reFlutter) - Flutter逆向工程框架

### 法证学

- [grr](https://github.com/google/grr) - GRR 快速响应是一个专注于远程实时取证的事件响应框架。
- [Volatility](https://github.com/volatilityfoundation/volatility) - 基于Python的内存提取和分析框架。
- [mig](http://mig.mozilla.org/) - MIG 是一个在远程端点上执行调查手术的平台。它使调查人员能够并行地从大量系统中获取信息，从而加快事件调查和日常运营安全。
- [ir-rescue](https://github.com/diogo-fernan/ir-rescue) - *ir-rescue* 是一个 Windows Batch 脚本和 Unix Bash 脚本，用于在事件响应期间全面收集主机取证数据。
- [Logdissect](https://github.com/dogoncouch/logdissect) - 用于分析日志文件和其他数据的 CLI 实用程序和 Python API。
- [Meerkat](https://github.com/TonyPhipps/Meerkat) - 基于 PowerShell 的 Windows 工件收集，用于威胁搜寻和事件响应。
- [Rekall](https://github.com/google/rekall) - Rekall 框架是一个完全开放的工具集合，在 Apache 和 GNU 通用公共许可证下用 Python 实现，用于提取和分析数字工件计算机系统。
- [LiME](https://github.com/504ensicsLabs/LiME.git) - Linux 内存提取器
- [Maigret](https://github.com/soxoj/maigret) - Maigret 仅通过用户名收集个人档案，检查大量网站上的帐户并从网页收集所有可用信息。

## 威胁情报

- [abuse.ch](https://www.abuse.ch/) - ZeuS Tracker / SpyEye Tracker / Palevo Tracker / Feodo Tracker 跟踪世界各地的命令与控制服务器（主机），并为您提供域和 IP 阻止列表。
- [Cyware Threat Intelligence Feeds](https://cyware.com/community/ctix-feeds) - Cyware 的威胁情报源为您提供来自各种开放且可信来源的宝贵威胁数据，以提供有价值且可操作的威胁情报的整合流。我们的威胁情报源与 STIX 1.x 和 2.0 完全兼容，为您实时提供有关全球发现的恶意软件哈希、IP 和域的最新信息。
- [Emerging Threats - Open Source](http://doc.emergingthreats.net/bin/view/Main/EmergingFAQ) - Emerging Threats 成立于 10 年前，是一个收集 Suricata 和 SNORT® 规则、防火墙规则和其他 IDS 规则集的开源社区。开源社区在互联网安全方面仍然发挥着积极作用，每天有超过 20 万活跃用户下载规则集。 ETOpen 规则集对任何用户或组织开放，只要您遵循一些基本准则即可。我们的 ETOpen 规则集可供随时下载。
- [PhishTank](http://www.phishtank.com/) - PhishTank 是一个协作交换所，用于收集有关互联网上网络钓鱼的数据和信息。此外，PhishTank 还为开发人员和研究人员提供开放 API，将反网络钓鱼数据免费集成到他们的应用程序中。
- [SBL / XBL / PBL / DBL / DROP / ROKSO](http://www.spamhaus.org/) - Spamhaus 项目是一个国际非营利组织，其使命是跟踪互联网的垃圾邮件操作和来源，为互联网网络提供可靠的实时反垃圾邮件保护，与执法机构合作识别和追捕全球垃圾邮件和恶意软件团伙，并游说政府制定有效的反垃圾邮件立法。
- [Internet Storm Center](https://www.dshield.org/reports.html) - 在成功检测、分析 Li0n 蠕虫并发出广泛警告后，ISC 于 2001 年创建。如今，ISC 为数以千计的互联网用户和组织提供免费的分析和警告服务，并积极与互联网服务提供商合作，反击最恶意的攻击者。
- [AutoShun](https://www.autoshun.org/) - AutoShun 是一个 Snort 插件，允许您将 Snort IDS 日志发送到集中式服务器，该服务器会将来自您的传感器日志的攻击与来自世界各地的其他 Snort 传感器、蜜罐和邮件过滤器关联起来。
- [DNS-BH](http://www.malwaredomains.com/) - DNS-BH 项目创建并维护已知用于传播恶意软件和间谍软件的域列表。该项目创建了 Bind 和 Windows 区域文件，以便为对这些内容的任何请求提供对 localhost 的虚假回复，从而防止许多间谍软件安装和报告。
- [AlienVault Open Threat Exchange](http://www.alienvault.com/open-threat-exchange/dashboard) - AlienVault Open Threat Exchange (OTX)，可帮助您保护网络免受恶意 IP 地址导致的数据丢失、服务中断和系统危害。
- [Tor Bulk Exit List](https://metrics.torproject.org/collector.html) - Collector，Tor 网络中您友好的数据收集服务。 Collector 从公共 Tor 网络中的各个节点和服务获取数据，并将其提供给全世界。如果您正在研究 Tor 网络，或者正在开发使用 Tor 网络数据的应用程序，那么这里就是您的起点。 [TOR 节点列表](https://www.dan.me.uk/tornodes) / [DNS 黑名单](https://www.dan.me.uk/dnsbl) / [Tor 节点列表](http://torstatus.blutmagie.de/)
- [leakedin.com](http://www.leakedin.com/) - leakedin.com 的主要目的是让访问者了解丢失数据的风险。该博客只是编译了在pastebin.com 等网站上丢失或披露的数据样本。
- [FireEye OpenIOCs](https://github.com/fireeye/iocs) - FireEye 公开共享的妥协指标 (IOC)
- [OpenVAS NVT Feed](http://www.openvas.org/openvas-nvt-feed.html) - 网络漏洞测试 (NVT) 的公共源。它包含超过 35,000 个 NVT（截至 2014 年 4 月），并且每天都在增长。此源被配置为 OpenVAS 的默认设置。
- [Project Honey Pot](http://www.projecthoneypot.org/) - Project Honey Pot 是第一个也是唯一一个用于识别垃圾邮件发送者和他们用来从您的网站抓取地址的垃圾邮件机器人的分布式系统。使用 Project Honey Pot 系统，您可以安装自定义标记为站点访问者的时间和 IP 地址的地址。如果这些地址之一开始接收电子邮件，我们不仅可以判断这些邮件是垃圾邮件，还可以判断该地址被收集的确切时间以及收集该地址的 IP 地址。
- [virustotal](https://www.virustotal.com/) - VirusTotal 是 Google 的子公司，是一项免费在线服务，可分析文件和 URL，识别病毒、蠕虫、特洛伊木马以及防病毒引擎和网站扫描程序检测到的其他类型的恶意内容。同时，它可以用作检测误报的一种手段，即被一个或多个扫描器检测为恶意的无害资源。
- [IntelMQ](https://github.com/certtools/intelmq/) - IntelMQ 是 CERT 的一种解决方案，用于使用消息队列协议收集和处理安全源、pastebin、推文。这是一个社区驱动的计划，称为 IHAP（事件处理自动化项目），该计划是由欧洲 CERT 在几次信息安全活动期间设计的概念。其主要目标是为事件响应人员提供一种简单的方法来收集和处理威胁情报，从而改进 CERT 的事件处理流程。 [ENSIA 主页](https://www.enisa.europa.eu/activities/cert/support/incident-handling-automation)。
- [CIFv2](https://github.com/csirtgadgets/massive-octo-spice) - CIF 是一个网络威胁情报管理系统。 CIF 允许您组合来自多个来源的已知恶意威胁信息，并使用该信息进行识别（事件响应）、检测 (IDS) 和缓解（空路由）。
- [MISP - Open Source Threat Intelligence Platform ](https://www.misp-project.org/) - MISP威胁共享平台是一款免费开源软件，有助于共享威胁情报（包括网络安全指标）的信息。  一个威胁情报平台，用于收集、共享、存储和关联目标攻击的妥协指标、威胁情报、金融欺诈信息、漏洞信息甚至反恐信息。 MISP 项目包括软件、通用库（[分类](https://www.misp-project.org/taxonomies.html)、[威胁参与者和各种恶意软件](https://www.misp-project.org/galaxy.html)）、一个使用[对象](https://www.misp-project.org/objects.html) 和默认值共享新信息的广泛数据模型[提要](https://www.misp-project.org/feeds/)。
- [PhishStats](https://phishstats.info/) - 通过搜索 IP、域名和网站标题进行网络钓鱼统计。
- [Threat Jammer](https://threatjammer.com) - REST API 服务允许开发人员、安全工程师和其他 IT 专业人员访问来自各种来源的精选威胁情报数据。
- [Cyberowl](https://github.com/karimhabush/cyberowl) - 当前从不同来源报告的最常见安全事件类型的每日更新摘要。

## 社会工程

- [Gophish](https://getgophish.com/) - 开源网络钓鱼框架。

## 网络

### 组织机构

- [OWASP](http://www.owasp.org) - 开放 Web 应用程序安全项目 (OWASP) 是一个 501(c)(3) 全球非营利慈善组织，致力于提高软件安全性。
- [Portswigger](https://portswigger.net) - PortSwigger 提供用于 Web 应用程序安全、测试和扫描的工具。从各种安全工具中进行选择并识别最新的漏洞。

### 网络应用防火墙

- [ModSecurity](http://www.modsecurity.org/) - ModSecurity 是一个用于实时 Web 应用程序监控、日志记录和访问控制的工具包。
- [BunkerWeb](https://github.com/bunkerity/bunkerweb) - BunkerWeb 是一款功能齐全的开源 Web 服务器，具有 ModeSecurity WAF、带有透明 Let's Encrypt 更新的 HTTPS、基于 HTTP 代码自动禁止奇怪行为、机器人和不良 IP 阻止、连接限制、最先进的安全预设、Web UI 等等。
- [NAXSI](https://github.com/nbs-system/naxsi) - NAXSI 是 NGINX 的开源、高性能、低规则维护 WAF，NAXSI 的意思是 Nginx Anti Xss & Sql Injection。
- [sql_firewall](https://github.com/uptimejp/sql_firewall) PostgreSQL 的 SQL 防火墙扩展
- [ironbee](https://github.com/ironbee/ironbee) - IronBee 是一个开源项目，旨在构建通用 Web 应用程序安全传感器。 IronBee 作为开发 Web 应用程序安全系统的框架 - 用于构建 Web 应用程序防火墙 (WAF) 的框架。
- [Curiefense](https://github.com/curiefense/curiefense) - Curiefense 添加了一组广泛的自动化 Web 安全工具，包括 WAF 到 Envoy 代理。
- [open-appsec](https://github.com/openappsec/openappsec) - open-appsec 是一个开源机器学习安全引擎，可先发制人地自动防止针对 Web 应用程序和 API 的威胁。

### 扫描/渗透测试

- [Spyse](https://spyse.com/) - Spyse 是一个 OSINT 搜索引擎，提供有关整个网络的最新数据。所有数据都存储在自己的数据库中，以便即时访问，并相互互连以进行灵活的搜索。
提供的数据：IPv4 主机、子/域/whois、端口/横幅/协议、技术、操作系统、AS、广泛的 SSL/TLS 数据库等。
- [sqlmap](http://sqlmap.org/) - sqlmap 是一个开源渗透测试工具，可以自动执行检测和利用 SQL 注入缺陷以及接管数据库服务器的过程。它配备了强大的检测引擎、最终渗透测试仪的许多利基功能以及广泛的开关，从数据库指纹识别、从数据库获取数据，到访问底层文件系统并通过带外连接在操作系统上执行命令。
- [ZAP](https://www.owasp.org/index.php/OWASP_Zed_Attack_Proxy_Project) - Zed Attack Proxy (ZAP) 是一种易于使用的集成渗透测试工具，用于查找 Web 应用程序中的漏洞。它旨在供具有广泛安全经验的人员使用，因此非常适合刚接触渗透测试的开发人员和功能测试人员。 ZAP 提供自动扫描程序以及一组允许您手动查找安全漏洞的工具。
- [OWASP Testing Checklist v4](https://www.owasp.org/index.php/Testing_Checklist) - Web 漏洞评估期间要测试的一些控件的列表。 Markdown 版本可以在[此处](https://github.com/amocrenco/owasp-testing-checklist-v4-markdown/blob/master/README.md)找到。
- [w3af](http://w3af.org/) - w3af 是一个 Web 应用程序攻击和审核框架。该项目的目标是创建一个框架，通过查找和利用所有 Web 应用程序漏洞来帮助您保护 Web 应用程序。
- [Recon-ng](https://github.com/lanmaster53/recon-ng) - Recon-ng 是一个用 Python 编写的全功能 Web 侦察框架。 Recon-ng 的外观和感觉与 Metasploit 框架相似。
- [PTF](https://github.com/trustedsec/ptf) - 渗透测试框架 (PTF) 是一种为最新工具提供模块化支持的方法。
- [Infection Monkey](https://github.com/guardicore/monkey) - 用于映射/渗透测试网络的半自动渗透测试工具。模拟人类攻击者。
- [ACSTIS](https://github.com/tijme/angularjs-csti-scanner) - ACSTIS 可帮助您扫描某些 Web 应用程序是否存在 AngularJS 客户端模板注入（有时称为 CSTI、沙箱逃逸或沙箱旁路）。它支持扫描单个请求，也支持抓取整个 Web 应用程序以查找 AngularJS CSTI 漏洞。
- [padding-oracle-attacker](https://github.com/KishanBagaria/padding-oracle-attacker) - padding-oracle-attacker 是一个 CLI 工具和库，用于轻松执行 padding oracle 攻击（解密以 CBC 模式加密的数据），支持并发网络请求和优雅的 UI。
- [is-website-vulnerable](https://github.com/lirantal/is-website-vulnerable) - 发现网站前端 JavaScript 库中公开的安全漏洞。
- [PhpSploit](https://github.com/nil0x42/phpsploit) - 全功能的 C2 框架，通过邪恶的 PHP oneliner 默默地保留在网络服务器上。专为隐秘持久性而构建，具有许多特权升级和利用后功能。
- [Keyscope](https://github.com/SpectralOps/keyscope) - Keyscope 是一个可扩展的密钥和秘密验证，用于检查 Rust 中构建的多个 SaaS 供应商的活动秘密
- [Cyclops](https://github.com/v8blink/Chromium-based-XSS-Taint-Tracking) - Cyclops 是一个具有 XSS 检测功能的 Web 浏览器，它是基于 chromium 的 XSS 检测，用于查找从源到接收器的流量。
- [Scanmycode CE (Community Edition)](https://github.com/marcinguy/scanmycode-ce) - 使用多种工具/扫描仪和一份报告进行代码扫描/SAST/静态分析/Linting。目前支持：PHP、Java、Scala、Python、Ruby、Javascript、GO、秘密扫描、依赖混淆、木马源代码、开源和专有检查（总共约 1000 个检查）
- [recon](https://github.com/rusty-ferris-club/recon) - 基于 Rust 的快速 CLI，使用 SQL 查询文件、代码或恶意软件，并为安全专家提供内容分类和处理
- [CakeFuzzer](https://github.com/Zigrin-Security/CakeFuzzer) - 用于基于 CakePHP 的 Web 应用程序的终极 Web 应用程序安全测试工具。 CakeFuzzer 采用一组预定义的攻击，这些攻击在执行前会随机修改。利用对 Cake PHP 框架的深入了解，Cake Fuzzer 对所有潜在的应用程序入口点发起攻击。
- [Artemis](https://github.com/CERT-Polska/Artemis/) - 具有自动报告生成功能的模块化漏洞扫描器。
- [Trust Scan](https://github.com/undeadlist/trust-scan) - URL 安全扫描器，具有 WHOIS、SSL、威胁情报（URLhaus、PhishTank、Spamhaus）和 40 多种诈骗/网络钓鱼模式检测。包括通过 Ollama 进行的可选 AI 分析。 ([演示](https://aibuilds.net))
- [react2shell-scanner](https://github.com/nxgn-kd01/react2shell-scanner) - 检测 React Server 组件中的 CVE-2025-55182 (React2Shell) RCE 漏洞。扫描 React 19.x 和 Next.js 项目是否存在关键的远程代码执行缺陷。
- [shai-hulud-scanner](https://github.com/nxgn-kd01/shai-hulud-scanner) - 检测 Shai Hulud 2.0 npm 供应链攻击中的妥协迹象，该攻击损害了 796 个以上的软件包。对恶意文件、哈希值和模式执行全面的安全检查。


### 运行时应用程序自我保护

- [Sqreen](https://www.sqreen.io/) - Sqreen 是一款面向软件团队的运行时应用程序自我保护 (RASP) 解决方案。应用程序内代理检测并监控应用程序。报告可疑的用户活动，并在运行时阻止攻击，无需修改代码或流量重定向。
- [OpenRASP](https://github.com/baidu/openrasp) - 由百度公司积极维护的开源 RASP 解决方案。通过上下文感知检测算法，该项目几乎实现了无误报。在服务器负载较重的情况下，观察到性能下降不到 3%。

### 发展

- [API Security in Action](https://www.manning.com/books/api-security-in-action) - 本书涵盖 API 安全性，包括安全开发、基于令牌的身份验证、JSON Web 令牌、OAuth 2 和马卡龙。 （抢先体验，持续发布，最终版将于 2020 年夏季发布）
- [Secure by Design](https://www.manning.com/books/secure-by-design?a_aid=danbjson&a_bid=0b3fac80) - 本书确定了设计模式和编码风格，这些设计模式和编码风格可以降低许多安全漏洞的可能性。 （抢先体验，持续发布，最终版本 2017 年秋季）
- [Understanding API Security](https://www.manning.com/books/understanding-api-security) - 免费电子书采样器通过展示 API 的组合方式以及如何使用 OAuth 协议来保护它们，为 API 安全性在现实世界中的工作原理提供一些背景信息。
- [OAuth 2 in Action](https://www.manning.com/books/oauth-2-in-action) - 本书从客户端、授权服务器和资源服务器的角度教您实际使用和部署 OAuth 2。
- [OWASP ZAP Node API](https://github.com/zaproxy/zap-api-nodejs) - 通过此官方 API 在 NodeJS 应用程序中利用 OWASP Zed 攻击代理 (ZAP)。
- [GuardRails](https://github.com/apps/guardrails) - 一个在拉取请求中提供安全反馈的 GitHub 应用程序。
- [Bearer](https://github.com/Bearer/bearer) - 扫描代码以查找导致敏感数据泄露的安全风险和漏洞。
- [Checkov](https://github.com/bridgecrewio/checkov/) - 基础设施即代码的静态分析工具 (Terraform)。
- [TFSec](https://github.com/tfsec/tfsec/) - 基础设施即代码的静态分析工具 (Terraform)。
- [KICS](https://github.com/Checkmarx/kics) - 扫描 IaC 项目是否存在安全漏洞、合规性问题和基础设施配置错误。目前正在处理 Terraform 项目、Kubernetes 清单、Dockerfile、AWS CloudFormation 模板和 Ansible playbook。
- [Insider CLI](https://github.com/insidersec/insider) - 使用 GoLang 编写的开源静态应用程序安全测试工具 (SAST)，适用于 Java（Maven 和 Android）、Kotlin (Android)、Swift (iOS)、.NET Full Framework、C# 和 Javascript (Node.js)。
- [Full Stack Python Security](https://www.manning.com/books/full-stack-python-security) - 全面了解 Python 开发人员的网络安全
- [Making Sense of Cyber Security](https://www.manning.com/books/making-sense-of-cyber-security) - 这是一本关于网络安全关键概念、术语和技术的无行话实用指南，非常适合规划或实施安全策略的任何人。 （抢先体验，持续发布，最终版本 2022 年初）
- [Security Checklist by OWASP](https://owasp.org/www-project-application-security-verification-standard/) - OWASP 的清单，用于根据保证级别测试 Web 应用程序。涵盖架构、IAM、清理、加密和安全配置等多个主题。
- [Pompelmi](https://github.com/pompelmi/pompelmi) - Node.js 文件上传恶意软件扫描程序，具有 MIME 嗅探、ZIP 炸弹防护和可选的 YARA 规则。

## 漏洞利用和有效负载

- [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings) - Web 应用程序安全和 Pentest/CTF 的有用有效负载和绕过列表

## 红队基础设施部署

- [Redcloud](https://github.com/khast3x/Redcloud) - 使用 Docker 进行自动化红队基础设施部署。
- [Axiom](https://github.com/pry0cc/axiom) - Axiom 是一个动态基础设施框架，可有效地处理多云环境，构建和部署专注于进攻和防御安全的可重复基础设施。

## 蓝队基础设施部署

- [MutableSecurity](https://github.com/MutableSecurity/mutablesecurity) - 用于自动设置、配置和使用网络安全解决方案的 CLI 程序。

## 可用性

- [Usable Security Course](https://pt.coursera.org/learn/usable-security) - coursera 上的可用安全课程。对于那些寻找安全性和可用性如何交叉的人来说非常好。

## 大数据

- [data_hacking](https://github.com/ClickSecurity/data_hacking) - 使用 IPython、Pandas 和 Scikit 的示例 了解如何充分利用您的安全数据。
- [hadoop-pcap](https://github.com/RIPE-NCC/hadoop-pcap) - 用于读取数据包捕获 (PCAP) 文件的 Hadoop 库。
- [Workbench](http://workbench.readthedocs.org/) - 适用于安全研究和开发团队的可扩展 Python 框架。
- [OpenSOC](https://github.com/OpenSOC/opensoc) - OpenSOC集成了多种开源大数据技术，为安全监控和分析提供集中式工具。
- [Apache Metron (incubating)](https://github.com/apache/incubator-metron) - Metron集成了多种开源大数据技术，以提供集中的安全监控和分析工具。
- [Apache Spot (incubating)](https://github.com/apache/incubator-spot) - Apache Spot 是一款开源软件，用于利用流量和数据包分析的见解。
- [binarypig](https://github.com/endgameinc/binarypig) - Hadoop 中的可扩展二进制数据提取。通过 Pig 进行恶意软件处理和分析，通过 Django、Twitter Bootstrap 和 Elasticsearch 进行探索。
- [Matano](https://github.com/matanolabs/matano) - AWS 上的开源无服务器安全湖平台可让您将 PB 级安全数据摄取、存储和分析到 Apache Iceberg 数据湖中，并以代码形式运行实时 Python 检测。
- [VAST](https://github.com/tenzir/vast) - 用于结构化事件数据的开源安全数据管道引擎，支持大容量遥测摄取、压缩和检索；专为安全内容执行、引导威胁搜寻和大规模调查而构建。

## 开发运营

- [Securing DevOps](https://manning.com/books/securing-devops) - 一本关于 DevOps 安全技术的书，回顾了用于保护 Web 应用程序及其基础设施的最先进实践。
- [ansible-os-hardening](https://github.com/dev-sec/ansible-os-hardening) - Ansible 在操作系统强化中的作用
- [Trivy](https://github.com/aquasecurity/trivy) - 一个简单而全面的漏洞扫描器，适用于容器和其他工件，适合 CI。
- [Preflight](https://github.com/spectralops/preflight) - 帮助您验证脚本和可执行文件，以减轻 CI 和其他系统中的供应链攻击。
- [Teller](https://github.com/spectralops/teller) - 面向开发人员和开发人员的秘密管理工具 - 从一个位置管理多个保管库和密钥库的秘密。
- [cve-ape](https://github.com/baalmor/cve-ape) - 用于嵌入测试和 CI 环境的非侵入式 CVE 扫描器，可以通过本地存储的 CVE 数据库扫描包列表和单个包中的现有 CVE。还可以用作离线 CVE 扫描仪，例如OT/ICS。
- [Selefra](https://github.com/selefra/selefra) - 一款开源策略即代码软件，可为多云和 SaaS 提供分析。

## 终端

* [shellfirm](https://github.com/kaplanelad/shellfirm) - 它是一个方便的实用程序，可帮助避免通过额外的批准步骤运行危险的命令。您将立即收到一个小的提示挑战，当检测到风险模式时，该挑战将双重验证您的操作。
* [shellclear](https://github.com/rusty-ferris-club/shellclear) - 它可以通过在所有历史命令中查找敏感命令并允许您清理它们来帮助您保护 shell 历史命令的安全。


## 操作系统

### 隐私与安全

- [Qubes OS](https://www.qubes-os.org/) - Qubes OS 是一款免费、开源、面向安全的操作系统，适用于单用户桌面计算。
- [Whonix](https://www.whonix.org) - 专为匿名而设计的操作系统。
- [Tails OS](https://tails.boum.org/) - Tails 是一种便携式操作系统，可以防止监视和审查。

### 在线资源

- [Security related Operating Systems @ Rawsec](https://inventory.raw.pm/operating_systems.html) - 安全相关操作系统的完整列表
- [Best Linux Penetration Testing Distributions @ CyberPunk](https://www.cyberpunk.rs/category/pentest-linux-distros) - 主要渗透测试发行版的描述
- [Security @ Distrowatch](http://distrowatch.com/search.php?category=Security) - 致力于讨论、回顾和了解开源操作系统最新动态的网站
- [Hardening Windows 10](https://www.hardenwindows10forsecurity.com/) - Windows 10 强化指南

## 数据存储

- [databunker](https://databunker.org/) - Databunker 是一个用于存储个人数据的地址簿。 GDPR 和加密是开箱即用的。
- [acra](https://github.com/cossacklabs/acra) - 数据库安全套件：数据保护代理，具有透明的“动态”数据加密、数据脱敏和标记化、SQL 防火墙（SQL 注入预防）、入侵检测系统。
- [blackbox](https://github.com/StackExchange/blackbox) - 使用 GPG 将机密安全地存储在 VCS 存储库中
- [confidant](https://github.com/lyft/confidant) - 将机密存储在 AWS DynamoDB 中，静态加密并与 IAM 集成
- [dotgpg](https://github.com/ConradIrwin/dotgpg) - 一种用于安全、轻松地备份生产机密或共享密码并对其进行版本控制的工具。
- [redoctober](https://github.com/cloudflare/redoctober) - 用于两人规则样式文件加密和解密的服务器。
- [aws-vault](https://github.com/99designs/aws-vault) - 将 AWS 凭证存储在 OSX 钥匙串或加密文件中
- [credstash](https://github.com/fugue/credstash) - 使用 AWS KMS 和 DynamoDB 存储机密
- [chamber](https://github.com/segmentio/chamber) - 使用 AWS KMS 和 SSM Parameter Store 存储密钥
- [Safe](https://github.com/starkandwayne/safe) - Vault CLI 使读取和写入 Vault 变得更加容易。
- [Sops](https://github.com/mozilla/sops) - 加密文件编辑器，支持 YAML、JSON 和 BINARY 格式，并使用 AWS KMS 和 PGP 进行加密。
- [passbolt](https://www.passbolt.com/) - 您的团队正在等待的密码管理器。免费、开源、可扩展、基于OpenPGP。
- [passpie](https://github.com/marcwebbie/passpie) - 多平台命令行密码管理器
- [Vault](https://www.vaultproject.io/) - 加密的数据存储足够安全，可以保存环境和应用程序机密。
- [LunaSec](https://github.com/lunasec-io/lunasec) - PII 数据库，具有自动加密/标记化、用于处理数据的沙盒组件以及集中授权控制。

## 预防欺诈

- [FingerprintJS](https://github.com/fingerprintjs/fingerprintjs) - 即使浏览器和混合移动应用程序用户清除数据存储，也能识别他们。允许您检测帐户接管、帐户共享和重复的恶意活动。
- [FingerprintJS Android](https://github.com/fingerprintjs/fingerprint-android) - 即使 Android 应用程序用户清除数据存储，也能识别他们。允许您检测帐户接管、帐户共享和重复的恶意活动。

## 电子书

- [Holistic Info-Sec for Web Developers](https://holisticinfosecforwebdevelopers.com/) - 免费且可下载的书籍系列，广泛而深入地涵盖了 Web 开发人员和 DevOps 工程师需要了解的知识，以便创建强大、可靠、可维护和安全的软件、网络等，并且持续、按时交付，不会出现令人讨厌的意外情况
- [Docker Security - Quick Reference: For DevOps Engineers](https://binarymist.io/publication/docker-security/) - 一本关于理解 Docker 安全默认设置、如何改进它们（理论和实践）以及许多工具和技术的书。
- [How to Hack Like a Pornstar](https://books2read.com/u/bWzdBx) - 闯入银行的分步过程，Sparc Flow，2017
- [How to Hack Like a Legend](https://amzn.to/2uWh1Up) - 黑客闯入秘密离岸公司 Sparc Flow 的故事，2018 年
- [How to Investigate Like a Rockstar](https://books2read.com/u/4jDWoZ) - 经历真正的危机，掌握法医分析的秘密，Sparc Flow，2017
- [Real World Cryptography](https://www.manning.com/books/real-world-cryptography) - 这本早期阅读书籍教您应用加密技术来理解和应用系统和应用程序各个级别的安全性。
- [AWS Security](https://www.manning.com/books/aws-security?utm_source=github&utm_medium=organic&utm_campaign=book_shields_aws_1_31_20) - 这本早期访问书籍涵盖了常见的 AWS 安全问题以及访问策略、数据保护、审计、持续监控和事件响应的最佳实践。
- [The Art of Network Penetration Testing](https://www.manning.com/books/the-art-of-network-penetration-testing) - 本书是在企业网络上运行您自己的渗透测试的实践指南。 （抢先体验，持续发布，2020 年 12 月最终发布）
- [Spring Boot in Practice](https://www.manning.com/books/spring-boot-in-practice) - 这本书是一本实用指南，以方便的问题-解决方案-讨论的形式呈现了数十个相关场景。（抢先体验，持续出版，最终版于 2021 年秋季发布）
- [Self-Sovereign Identity](https://www.manning.com/books/self-sovereign-identity) - 这本书介绍了 SSI 如何使我们能够接收数字签名的凭据，将其存储在私人钱包中，并安全地证明我们的在线身份。 （抢先体验，持续发布，最终版将于 2021 年秋季发布）
- [Data Privacy](https://www.manning.com/books/data-privacy) - 这本书教您大规模实施技术隐私解决方案和工具。 （早期访问，持续发布，最终版本 2022 年 1 月）
- [Cyber Security Career Guide](https://www.manning.com/books/cyber-security-career-guide) - 通过学习如何调整现有的技术和非技术技能来开启网络安全职业生涯。 （抢先体验，持续发布，最终版本 2022 年夏季）
- [Secret Key Cryptography](https://www.manning.com/books/secret-key-cryptography) - 一本关于密码技术和密钥方法的书。 （抢先体验，持续发布，最终版本 2022 年夏季）
- [The Security Engineer Handbook](https://securityhandbook.io/) - 这是一篇简短的读物，讨论了在安全团队中工作的注意事项，以及可以帮助您作为安全工程师进行日常工作的许多技巧和技巧。
- [Cyber Threat Hunting](https://www.manning.com/books/cyber-threat-hunting) - 网络威胁搜寻实用指南。
- [Edge Computing Technology and Applications](https://www.manning.com/books/edge-computing-technology-and-applications) - 一本关于创建边缘计算策略所需的业务和技术基础的书。
- [Spring Security in Action, Second Edition](https://www.manning.com/books/spring-security-in-action-second-edition) - 一本关于设计和开发从一开始就安全的 Spring 应用程序的书。
- [Azure Security](https://www.manning.com/books/azure-security-2) - Microsoft Azure 原生安全服务的实用指南。
- [Node.js Secure Coding: Defending Against Command Injection Vulnerabilities](https://www.nodejs-security.com) - 通过对现实世界的 npm 包执行命令注入攻击并分析易受攻击的代码，学习 Node.js 中的安全编码约定。
- [Node.js Secure Coding: Prevention and Exploitation of Path Traversal Vulnerabilities](https://www.nodejs-security.com/book/path-traversal) - 掌握 Node.js 中具有真实脆弱依赖项的安全编码，并体验针对路径遍历漏洞的第一手安全编码技术。
- [Grokking Web Application Security](https://www.manning.com/books/grokking-web-application-security) - 一本关于构建可应对任何攻击并具有弹性的 Web 应用程序的书。

## 其他很棒的清单

### 其他很棒的安全列表

- [Android Security Awesome](https://github.com/ashishb/android-security-awesome) - Android安全相关资源集合。
- [Awesome ARM Exploitation](https://github.com/HenryHoggard/awesome-arm-exploitation) - ARM 开发资源的精选列表。
- [Awesome CTF](https://github.com/apsdehal/awesome-ctf) - CTF 框架、库、资源和软件的精选列表。
- [Awesome Cyber Skills](https://github.com/joe-shenouda/awesome-cyber-skills) - 精选的黑客环境列表，您可以在其中合法、安全地训练您的网络技能。
- [Awesome Personal Security](https://github.com/Lissy93/personal-security-checklist) - 数字安全和隐私提示的精选列表，以及更多资源的链接。
- [Awesome Hacking](https://github.com/carpedm20/awesome-hacking) - 精选的精彩黑客教程、工具和资源列表。
- [Awesome Honeypots](https://github.com/paralax/awesome-honeypots) - 一个很棒的蜜罐资源列表。
- [Awesome Malware Analysis](https://github.com/rshipp/awesome-malware-analysis) - 很棒的恶意软件分析工具和资源的精选列表。
- [Awesome Security Newsletters](https://github.com/TalEliyahu/awesome-security-newsletters) - 精选的精彩新闻通讯列表，可通过电子邮件了解最新的安全新闻。
- [Awesome PCAP Tools](https://github.com/caesar0301/awesome-pcaptools) - 由计算机科学领域的其他研究人员开发的用于处理网络跟踪的工具集合。
- [Awesome Pentest](https://github.com/enaqx/awesome-pentest) - 一系列很棒的渗透测试资源、工具和其他闪亮的东西。
- [Awesome Privacy](https://github.com/lissy93/awesome-privacy) - 尊重隐私的软件和服务的精选列表。
- [Awesome Linux Containers](https://github.com/Friz-zy/awesome-linux-containers) - 精彩的 Linux 容器框架、库和软件的精选列表。
- [Awesome Incident Response](https://github.com/meirwah/awesome-incident-response) - 用于事件响应的精选资源列表。
- [Awesome Web Hacking](https://github.com/infoslack/awesome-web-hacking) - 此列表适用于任何希望了解 Web 应用程序安全性但没有起点的人。
- [Awesome Electron.js Hacking](https://github.com/doyensec/awesome-electronjs-hacking) - 有关 Electron.js 安全性的精彩资源精选列表
- [Awesome Threat Intelligence](https://github.com/hslatman/awesome-threat-intelligence) - 威胁情报资源的精选列表。
- [Awesome Threat Modeling](https://github.com/redshiftzero/awesome-threat-modeling) - 威胁建模资源的精选列表。
- [Awesome Pentest Cheat Sheets](https://github.com/coreb1t/awesome-pentest-cheat-sheets) - 对渗透测试有用的备忘单集合
- [Awesome Industrial Control System Security](https://github.com/mpesen/awesome-industrial-control-system-security) - 与工业控制系统 (ICS) 安全相关的精选资源列表。
- [Awesome YARA](https://github.com/InQuest/awesome-yara) - 精选的 YARA 规则、工具和人员列表。
- [Awesome Threat Detection and Hunting](https://github.com/0x4D31/awesome-threat-detection) - 很棒的威胁检测和狩猎资源的精选列表。
- [Awesome Container Security](https://github.com/kai5263499/container-security-awesome) - 与容器构建和运行时安全相关的精彩资源的精选列表
- [Awesome Crypto Papers](https://github.com/pFarb/awesome-crypto-papers) - 密码学论文、文章、教程和指南的精选列表。
- [Awesome Shodan Search Queries](https://github.com/jakejarvis/awesome-shodan-queries) - 插入 Shodan.io 的有趣、有趣和令人沮丧的搜索查询的集合。
- [Awesome Censys Queries](https://github.com/thehappydinoa/awesome-censys-queries) - 一系列令人着迷且奇异的 Censys 搜索查询。
- [Awesome Anti Forensics](https://github.com/remiflavien1/awesome-anti-forensic) - 用于对抗取证活动的一系列出色工具。
- [Awesome Security Talks & Videos](https://github.com/PaulSec/awesome-sec-talks) - 精彩安全会谈的精选列表，按年份和会议组织。
- [Awesome Bluetooth Security](https://github.com/engn33r/awesome-bluetooth-security) - 蓝牙安全资源精选列表。
- [Awesome WebSocket Security](https://github.com/PalindromeLabs/awesome-websocket-security) - WebSocket 安全资源的精选列表。
- [Security Acronyms](https://github.com/cloudsecurelab/security-acronyms) - 安全相关首字母缩略词和概念的精选列表
- [Awesome SOAR](https://github.com/correlatedsecurity/Awesome-SOAR) - 精心策划的网络“安全编排、自动化和响应 (SOAR)”资源列表。
- [Awesome Security Hardening](https://github.com/decalage2/awesome-security-hardening) - 一系列精彩的安全强化指南、最佳实践、清单、基准、工具和其他资源。

### 其他常见的很棒的列表

其他令人惊叹的精彩列表：

- [awesome-awesomeness](https://github.com/bayandin/awesome-awesomeness) - Awesome-* 或 *-awesome 列表。
- [lists](https://github.com/jnv/lists) - GitHub 上整理的（很棒的）最终列表。
- [Movies For Hacker](https://github.com/k4m4/movies-for-hackers) - 每个黑客和赛博朋克都必须观看的精选电影列表。
- [很棒的自托管](https://github.com/awesome-selfhosted/awesome-selfhosted)
- [很棒的分析](https://github.com/0xnr/awesome-analytics)
- [很棒的系统管理员](https://github.com/awesome-foss/awesome-sysadmin)

## 贡献

随时欢迎您的贡献！
