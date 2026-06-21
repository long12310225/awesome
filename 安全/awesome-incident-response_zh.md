# 出色的事件响应 [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

> 用于安全事件响应的工具和资源的精选列表，旨在帮助安全分析师和 [DFIR](http://www.acronymfinder.com/Digital-Forensics%2c-Incident-Response-%28DFIR%29.html) 团队。

数字取证和事件响应 (DFIR) 团队是组织中负责管理安全事件响应的人员群体，包括收集事件证据、补救其影响以及实施控制措施以防止事件再次发生。

## 内容

- [对手模拟](#adversary-emulation)
- [多合一工具](#all-in-one-tools)
- [Books](#books)
- [Communities](#communities)
- [磁盘映像创建工具](#disk-image-creation-tools)
- [证据收集](#evidence-collection)
- [事件管理](#incident-management)
- [知识库](#knowledge-bases)
- [Linux 发行版](#linux-distributions)
- [Linux 证据收集](#linux-evidence-collection)
- [日志分析工具](#log-analysis-tools)
- [内存分析工具](#memory-analysis-tools)
- [内存映像工具](#memory-imaging-tools)
- [OSX 证据收集](#osx-evidence-collection)
- [其他清单](#other-lists)
- [其他工具](#other-tools)
- [Playbooks](#playbooks)
- [进程转储工具](#process-dump-tools)
- [沙箱/逆向工具](#sandboxingreversing-tools)
- [扫描仪工具](#scanner-tools)
- [时间轴工具](#timeline-tools)
- [Videos](#videos)
- [Windows 证据收集](#windows-evidence-collection)

## IR 工具集

### 对手模拟

* [APTSimulator](https://github.com/NextronSystems/APTSimulator) - Windows 批处理脚本使用一组工具和输出文件使系统看起来像是受到了威胁。
* [Atomic Red Team (ART)](https://github.com/redcanaryco/atomic-red-team) - 映射到 MITRE ATT&CK 框架的小型且高度便携的检测测试。
* [AutoTTP](https://github.com/jymcheong/AutoTTP) - 自动化战术技术和程序。手动重新运行复杂序列以进行回归测试、产品评估，为研究人员生成数据。
* [Caldera](https://github.com/mitre/caldera) - 自动对手模拟系统，可在 Windows Enterprise 网络中执行入侵后的对抗行为。它在操作过程中使用规划系统和基于对抗战术、技术和常识 (ATT&CK™) 项目的预配置对手模型生成计划。
* [DumpsterFire](https://github.com/TryCatchHCF/DumpsterFire) - 模块化、菜单驱动、跨平台工具，用于构建可重复、延时、分布式安全事件。轻松创建用于蓝队演习和传感器/警报映射的自定义事件链。红队可以制造诱饵事件、干扰和诱惑来支持和扩大其行动。
* [Metta](https://github.com/uber-common/metta) - 用于进行对抗性模拟的信息安全准备工具。
* [Network Flight Simulator](https://github.com/alphasoc/flightsim) - 用于生成恶意网络流量并帮助安全团队评估安全控制和网络可见性的轻量级实用程序。
* [Red Team Automation (RTA)](https://github.com/endgameinc/RTA) - RTA 提供了一个脚本框架，旨在允许蓝队测试其针对恶意间谍活动的检测能力，以 MITRE ATT&CK 为模型。
* [RedHunt-OS](https://github.com/redhuntlabs/RedHunt-OS) - 用于对手模拟和威胁搜寻的虚拟机。

### 多合一工具

* [Belkasoft Evidence Center](https://belkasoft.com/ec) - 该工具包将通过分析硬盘驱动器、驱动器映像、内存转储、iOS、黑莓和 Android 备份、UFED、JTAG 和芯片转储，快速从多个来源提取数字证据。
* [CimSweep](https://github.com/PowerShellMafia/CimSweep) - 基于 CIM/WMI 的工具套件，能够跨所有版本的 Windows 远程执行事件响应和搜寻操作。
* [CIRTkit](https://github.com/byt3smith/CIRTKit) - CIRTKit 不仅仅是工具的集合，而且还是一个有助于持续统一事件响应和取证调查流程的框架。
* [Cyber Triage](http://www.cybertriage.com) - Cyber​​ Triage 收集并分析主机数据以确定其是否受到损害。它的评分系统和推荐引擎可让您快速关注重要的工件。它可以从其收集工具、磁盘映像和其他收集器（例如 KAPE）导入数据。它可以在审查员的桌面上或服务器模型中运行。由 Sleuth Kit Labs 开发，该实验室也生产尸检。
* [Dissect](https://github.com/fox-it/dissect) - Dissect 是一个数字取证和事件响应框架和工具集，可让您快速访问和分析各种磁盘和文件格式的取证文物，由 Fox-IT（NCC 集团的一部分）开发。
* [Doorman](https://github.com/mwielgoszewski/doorman) - osquery 队列管理器，允许远程管理节点检索的 osquery 配置。它利用 osquery 的 TLS 配置、记录器和分布式读/写端点，为管理员提供跨设备群的可见性，并以最小的开销和侵入性。
* [Falcon Orchestrator](https://github.com/CrowdStrike/falcon-orchestrator) - 可扩展的基于 Windows 的应用程序，提供工作流程自动化、案例管理和安全响应功能。
* [Flare](https://github.com/fireeye/flare-vm) - 完全可定制的、基于 Windows 的安全发行版，用于恶意软件分析、事件响应、渗透测试。
* [Fleetdm](https://github.com/fleetdm/fleet) - 为安全专家量身定制的最先进的主机监控平台。利用 Facebook 久经考验的 osquery 项目，Fleetdm 提供持续更新、功能和对重大问题的快速解答。
* [GRR Rapid Response](https://github.com/google/grr) - 专注于远程实时取证的事件响应框架。它由安装在目标系统上的 python 代理（客户端）和可以管理代理并与代理通信的 python 服务器基础设施组成。除了附带的 Python API 客户端之外，[PowerGRR](https://github.com/swisscom/PowerGRR) 在 PowerShell 中提供了一个 API 客户端库，可在 Windows、Linux 和 macOS 上运行，以实现 GRR 自动化和脚本编写。
* [IRIS](https://github.com/dfir-iris/iris-web) - IRIS 是一个供事件响应分析师使用的网络协作平台，允许在技术层面共享调查结果。
* [Kuiper](https://github.com/DFIRKuiper/Kuiper) - 数字取证调查平台
* [Limacharlie](https://www.limacharlie.io/) - 端点安全平台由一系列协同工作的小项目组成，为您提供跨平台（Windows、OSX、Linux、Android 和 iOS）低级环境，用于管理附加模块并将其推送到内存中以扩展其功能。
* [Matano](https://github.com/matanolabs/matano)：AWS 上的开源无服务器安全湖平台，可让您将 PB 级安全数据摄取、存储和分析到 Apache Iceberg 数据湖中，并以代码形式运行实时 Python 检测。
* [MozDef](https://github.com/mozilla/MozDef) - 自动化安全事件处理流程并促进事件处理程序的实时活动。
* [MutableSecurity](https://github.com/MutableSecurity/mutablesecurity) - 用于自动设置、配置和使用网络安全解决方案的 CLI 程序。
* [nightHawk](https://github.com/biggiesmallsAG/nightHawkResponse) - 使用 ElasticSearch 作为后端为异步取证数据呈现构建的应用程序。它旨在摄取 Redline 集合。
* [Open Computer Forensics Architecture](http://sourceforge.net/projects/ocfa/) - 另一个流行的分布式开源计算机取证框架。该框架建立在Linux平台上，使用postgreSQL数据库来存储数据。
* [osquery](https://osquery.io/) - 使用类似 SQL 的查询语言轻松询问有关 Linux 和 macOS 基础设施的问题；提供的*事件响应包*可帮助您检测和响应违规行为。
* [Redline](https://www.fireeye.com/services/freeware/redline.html) - 为用户提供主机调查功能，以通过内存和文件分析以及威胁评估配置文件的开发来查找恶意活动的迹象。
* [SOC Multi-tool](https://github.com/zdhenard42/SOC-Multitool) - 功能强大且用户友好的浏览器扩展，可简化安全专业人员的调查。
* [The Sleuth Kit & Autopsy](http://www.sleuthkit.org) - 基于 Unix 和 Windows 的工具，有助于对计算机进行取证分析。它配备了有助于数字取证的各种工具。这些工具有助于分析磁盘映像、对文件系统进行深入分析以及各种其他操作。
* [TheHive](https://thehive-project.org/) - 可扩展的三合一开源免费解决方案，旨在让 SOC、CSIRT、CERT 以及任何处理需要快速调查和采取行动的安全事件的信息安全从业人员的工作变得更加轻松。
* [Velociraptor](https://github.com/Velocidex/velociraptor) - 端点可见性和收集工具
* [X-Ways Forensics](http://www.x-ways.net/forensics/) - 用于磁盘克隆和成像的取证工具。它可用于查找已删除的文件和磁盘分析。
* [Zentral](https://github.com/zentralopensource/zentral) - 将 osquery 强大的端点清单功能与灵活的通知和操作框架相结合。这使得人们能够识别 OS X 和 Linux 客户端上的更改并做出反应。

### 书籍

* [Applied Incident Response](https://www.amazon.com/Applied-Incident-Response-Steve-Anson/dp/1119560268/) - 史蒂夫·安森（Steve Anson）关于事件响应的书。
* [Art of Memory Forensics](https://www.amazon.com/Art-Memory-Forensics-Detecting-Malware/dp/1118825098/) - 检测 Windows、Linux 和 Mac 内存中的恶意软件和威胁。
* [Crafting the InfoSec Playbook: Security Monitoring and Incident Response Master Plan](https://www.amazon.com/Crafting-InfoSec-Playbook-Security-Monitoring/dp/1491949406) - 作者：杰夫·博林格、布兰登·恩莱特和马修·瓦利特。
* [Digital Forensics and Incident Response: Incident response techniques and procedures to respond to modern cyber threats](https://www.amazon.com/Digital-Forensics-Incident-Response-techniques/dp/183864900X) - 作者：杰拉德·约翰森。
* [Introduction to DFIR](https://medium.com/@sroberts/introduction-to-dfir-d35d5de4c180/) - 作者：斯科特·J·罗伯茨。
* [Incident Response & Computer Forensics, Third Edition](https://www.amazon.com/Incident-Response-Computer-Forensics-Third/dp/0071798684/) - 事件响应的权威指南。
* [Incident Response Techniques for Ransomware Attacks](https://www.amazon.com/Incident-Response-Techniques-Ransomware-Attacks/dp/180324044X) - 构建勒索软件攻击事件响应策略的重要指南。作者：奥列格·斯库尔金。
* [Incident Response with Threat Intelligence](https://www.amazon.com/Incident-response-Threat-Intelligence-intelligence-based/dp/1801072957) - 对于构建基于威胁情报的事件响应计划很有参考价值。罗伯托·马丁内斯著。
* [Intelligence-Driven Incident Response](https://www.amazon.com/Intelligence-Driven-Incident-Response-Outwitting-Adversary-ebook-dp-B074ZRN5T7/dp/B074ZRN5T7) - 作者：斯科特·J·罗伯茨，丽贝卡·布朗。
* [Operator Handbook: Red Team + OSINT + Blue Team Reference](https://www.amazon.com/Operator-Handbook-Team-OSINT-Reference/dp/B085RR67H5/) - 对于事件响应者来说是很好的参考。
* [Practical Memory Forensics](https://www.amazon.com/Practical-Memory-Forensics-Jumpstart-effective/dp/1801070334) - 记忆取证实践的权威指南。作者：斯维特兰娜·奥斯特洛夫斯卡娅和奥列格·斯库尔金。
* [The Practice of Network Security Monitoring: Understanding Incident Detection and Response](http://www.amazon.com/gp/product/1593275099) - Richard Bejtlich 的关于 IR 的书。

### 社区

* [Digital Forensics Discord Server](https://discordapp.com/invite/JUqe9Ek) - 由来自执法部门、私营部门和法医供应商的 8,000 多名专业人士组成的社区。此外，还有很多学生和爱好者！指南[此处](https://aboutdfir.com/a-beginners-guide-to-the-digital-forensics-discord-server/)。
* [Slack DFIR channel](https://dfircommunity.slack.com) - Slack DFIR 社区频道 - [在此注册](https://start.paloaltonetworks.com/join-our-slack-community)。

### 磁盘映像创建工具

* [AccessData FTK Imager](http://accessdata.com/product-download/?/support/adownloads#FTKImager) - 取证工具，其主要目的是预览任何类型磁盘中的可恢复数据。 FTK Imager 还可以获取 32 位和 64 位系统上的实时内存和分页文件。
* [Bitscout](https://github.com/vitaly-kamluk/bitscout) - Vitaly Kamluk 的 Bitscout 可帮助您构建完全可信的可定制 LiveCD/LiveUSB 映像，用于远程数字取证（或您选择的任何其他任务）。它应该是透明的、可由系统所有者监控、取证合理、可定制且紧凑。
* [GetData Forensic Imager](http://www.forensicimager.com/) - 基于 Windows 的程序，将获取、转换或验证以下常见取证文件格式之一的取证图像。
* [Guymager](http://guymager.sourceforge.net) - 用于 Linux 上媒体采集的免费取证成像仪。
* [Magnet ACQUIRE](https://www.magnetforensics.com/magnet-acquire/) - ACQUIRE by Magnet Forensics 允许在 Windows、Linux 和 OS X 以及移动操作系统上执行各种类型的磁盘采集。

### 证据收集

* [Acquire](https://github.com/fox-it/acquire) - Acquire 是一种工具，可将磁盘映像或实时系统中的取证工件快速收集到轻量级容器中。这使得 Acquire 成为一个出色的工具，可以加速数字取证分类的过程。如果可能的话，它使用 [Dissect](https://github.com/fox-it/dissect) 从原始磁盘收集该信息。
* [artifactcollector](https://github.com/forensicanalysis/artifactcollector) - artifactcollector 项目提供了一个在系统上收集取证工件的软件。
* [bulk_extractor](https://github.com/simsong/bulk_extractor) - 计算机取证工具，可扫描磁盘映像、文件或文件目录并提取有用信息，而无需解析文件系统或文件系统结构。由于忽略了文件系统结构，该程序在速度和彻底性方面脱颖而出。
* [Cold Disk Quick Response](https://github.com/rough007/CDQR) - 简化的解析器列表，可快速分析取证图像文件（“dd”、E01、“.vmdk”等）并输出九个报告。
* [CyLR](https://github.com/orlikoski/CyLR) - CyLR 工具快速、安全地从具有 NTFS 文件系统的主机收集取证工件，并最大限度地减少对主机的影响。
* [Forensic Artifacts](https://github.com/ForensicArtifacts/artifacts) - 数字取证工件存储库
* [ir-rescue](https://github.com/diogo-fernan/ir-rescue) - Windows Batch 脚本和 Unix Bash 脚本可在事件响应期间全面收集主机取证数据。
* [Live Response Collection](https://www.brimorlabs.com/tools/) - 从 Windows、OSX 和基于 \*nix 的操作系统收集易失性数据的自动化工具。
* [Margarita Shotgun](https://github.com/ThreatResponse/margaritashotgun) - 用于并行化远程内存获取的命令行实用程序（无论是否使用 Amazon EC2 实例）。
* [SPECTR3](https://github.com/alpine-sec/SPECTR3) - 通过便携式 iSCSI 只读访问获取、分类和调查远程证据
* [UAC](https://github.com/tclahr/uac) - UAC（类 Unix 工件收集器）是用于事件响应的实时响应收集脚本，它利用本机二进制文件和工具来自动收集 AIX、Android、ESXi、FreeBSD、Linux、macOS、NetBSD、NetScaler、OpenBSD 和 Solaris 系统工件。

### 事件管理

* [Catalyst](https://github.com/SecurityBrewery/catalyst) - 免费的 SOAR 系统，有助于自动化警报处理和事件响应流程。
* [CyberCPR](https://www.cybercpr.com) - 内置“需要了解”的社区和商业事件管理工具，可在处理敏感事件时支持 GDPR 合规性。
* [Cyphon](https://medevel.com/cyphon/) - Cyphon 通过单一平台简化大量相关任务，消除了事件管理的难题。它接收、处理和分类事件，为您的分析工作流程提供全面的解决方案 - 聚合数据、捆绑警报并确定其优先级，并使分析师能够调查和记录事件。
* [CORTEX XSOAR](https://www.paloaltonetworks.com/cortex/xsoar) - Paloalto 安全编排、自动化和响应平台，具有完整的事件生命周期管理和许多集成以增强自动化。
* [DFTimewolf](https://github.com/log2timeline/dftimewolf) - 用于协调取证收集、处理和数据导出的框架。
* [DFIRTrack](https://github.com/dfirtrack/dfirtrack) - 事件响应跟踪应用程序通过具有大量受影响系统和工件的案例和任务处理一个或多个事件。
* [Fast Incident Response (FIR)](https://github.com/certsocietegenerale/FIR/) - 网络安全事件管理平台的设计考虑了敏捷性和速度。它可以轻松创建、跟踪和报告网络安全事件，对于 CSIRT、CERT 和 SOC 等都很有用。
* [RTIR](https://www.bestpractical.com/rtir/) - 事件响应请求跟踪器 (RTIR) 是面向计算机安全团队的首要开源事件处理系统。我们与世界各地的十多个 CERT 和 CSIRT 团队合作，帮助您处理不断增加的事件报告量。 RTIR 建立在 Request Tracker 的所有功能之上。
* [Sandia Cyber Omni Tracker (SCOT)](https://github.com/sandialabs/scot) - 事件响应协作和知识捕获工具注重灵活性和易用性。我们的目标是在不给用户带来负担的情况下为事件响应流程增加价值。
* [Shuffle](https://github.com/frikky/Shuffle) - 专注于可访问性的通用安全自动化平台。
* [threat_note](https://github.com/defpoint/threat_note) - 轻量级调查笔记本，使安全研究人员能够注册和检索与其研究相关的指标。
* [Zenduty](https://www.zenduty.com) - Zenduty 是一个新颖的事件管理平台，提供端到端事件警报、待命管理和响应编排，使团队能够更好地控制和自动化事件管理生命周期。

### 知识库

* [Digital Forensics Artifact Knowledge Base](https://github.com/ForensicArtifacts/artifacts-kb) - 数字取证文物知识库
* [Windows Events Attack Samples](https://github.com/sbousseaden/EVTX-ATTACK-SAMPLES) - Windows 事件攻击样本
* [Windows Registry Knowledge Base](https://github.com/libyal/winreg-kb) - Windows 注册表知识库

### Linux 发行版

* [The Appliance for Digital Investigation and Analysis (ADIA)](https://forensics.cert.org/#ADIA) - 基于 VMware 的设备用于数字调查和采集，完全由公共领域软件构建。 ADIA 中包含的工具包括 Autopsy、Sleuth Kit、Digital Forensics Framework、log2timeline、Xplico 和 Wireshark。大部分系统维护使用Webmin。它专为中小型数字调查和收购而设计。该设备在 Linux、Windows 和 Mac OS 下运行。 i386（32 位）和 x86_64（64 位）版本均可用。
* [Computer Aided Investigative Environment (CAINE)](http://www.caine-live.net/index.html) - 包含许多可以帮助调查人员进行分析的工具，包括法医证据收集。
* [CCF-VM](https://github.com/rough007/CCF-VM) - CyLR CDQR 取证虚拟机 (CCF-VM)：一种解析收集数据的一体化解决方案，可通过内置的常见搜索轻松搜索数据，并可同时搜索单个和多个主机。
* [NST - Network Security Toolkit](https://sourceforge.net/projects/nst/files/latest/download?source=files) - Linux 发行版包含大量对网络安全专业人士有用的最佳开源网络安全应用程序。
* [NullSec Linux](https://github.com/bad-antics/nullsec-linux) - 以安全为中心的 Linux 发行版，具有 140 多个预装的取证和攻击性安全工具、自定义强化内核以及集成的事件响应工作流程。
* [PALADIN](https://sumuri.com/software/paladin/) - 修改了 Linux 发行版，以合理的取证方式执行各种取证任务。它附带了许多开源取证工具。
* [Security Onion](https://github.com/Security-Onion-Solutions/security-onion) - 针对网络安全监控的特殊 Linux 发行版，具有先进的分析工具。
* [SANS Investigative Forensic Toolkit (SIFT) Workstation](http://digital-forensics.sans.org/community/downloads) - 证明可以使用免费提供且经常更新的尖端开源工具来实现先进的事件响应能力和针对入侵的深入数字取证技术。

### Linux 证据收集

* [FastIR Collector Linux](https://github.com/SekoiaLab/Fastir_Collector_Linux) - FastIR for Linux 收集实时 Linux 上的不同工件并将结果记录在 CSV 文件中。
* [MAGNET DumpIt](https://github.com/MagnetForensics/dumpit-linux) - 用 Rust 编写的 Linux 快速内存获取开源工具。生成 Linux 机器的完整内存崩溃转储。

### 日志分析工具

* [AppCompatProcessor](https://github.com/mbevilacqua/appcompatprocessor) - AppCompatProcessor 旨在从企业范围内的 AppCompat / AmCache 数据中提取超出经典堆栈和 grep 技术的附加价值。
* [APT Hunter](https://github.com/ahmedkhlief/APT-Hunter) - APT-Hunter 是针对 Windows 事件日志的威胁搜寻工具。
* [Chainsaw](https://github.com/countercept/chainsaw) - Chainsaw 提供强大的“第一响应”功能，可以快速识别 Windows 事件日志中的威胁。
* [Event Log Explorer](https://eventlogxp.com/) - 开发用于快速分析日志文件和其他数据的工具。
* [Event Log Observer](https://lizard-labs.com/event_log_observer.aspx) - 使用此 GUI 工具查看、分析和监视 Microsoft Windows 事件日志中记录的事件。
* [Hayabusa](https://github.com/Yamato-Security/hayabusa) - Hayabusa 是由日本 Yamato 安全小组创建的 Windows 事件日志快速取证时间线生成器和威胁搜寻工具。
* [Kaspersky CyberTrace](https://support.kaspersky.com/13850) - 威胁情报融合和分析工具，将威胁数据源与 SIEM 解决方案集成。用户可以立即利用威胁情报在现有安全操作的工作流程中进行安全监控和事件报告 (IR) 活动。
* [Log Parser Lizard](https://lizard-labs.com/log_parser_lizard.aspx) - 针对结构化日志数据执行 SQL 查询：服务器日志、Windows 事件、文件系统、Active Directory、log4net 日志、逗号/制表符分隔文本、XML 或 JSON 文件。还为 Microsoft LogParser 2.2 提供了一个 GUI，具有强大的 UI 元素：语法编辑器、数据网格、图表、数据透视表、仪表板、查询管理器等。
* [Lorg](https://github.com/jensvoid/lorg) - 用于高级 HTTPD 日志文件安全分析和取证的工具。
* [Logdissect](https://github.com/dogoncouch/logdissect) - 用于分析日志文件和其他数据的 CLI 实用程序和 Python API。
* [NullSec LogReaper](https://github.com/bad-antics/nullsec-logreaper) - 高速日志分析和取证工具，具有多格式解析、模式匹配、时间线重建和事件响应异常检测。
* [LogonTracer](https://github.com/JPCERTCC/LogonTracer) - 通过可视化和分析 Windows 事件日志来调查恶意 Windows 登录的工具。
* [Sigma](https://github.com/SigmaHQ/sigma) - SIEM 系统的通用签名格式已包含广泛的规则集。
* [StreamAlert](https://github.com/airbnb/streamalert) - 无服务器、实时日志数据分析框架，能够摄取自定义数据源并使用用户定义的逻辑触发警报。
* [SysmonSearch](https://github.com/JPCERTCC/SysmonSearch) - SysmonSearch 通过聚合事件日志，使 Windows 事件日志分析更加有效且耗时更少。
* [WELA](https://github.com/Yamato-Security/WELA) - Windows 事件日志分析器旨在成为 Windows 事件日志的瑞士军刀。
* [Zircolite](https://github.com/wagga40/Zircolite) - 用于 EVTX 或 JSON 的独立且快速的基于 SIGMA 的检测工具。

### 内存分析工具

* [AVML](https://github.com/microsoft/avml) - 适用于 Linux 的便携式易失性内存采集工具。
* [Evolve](https://github.com/JamesHabben/evolve) - 波动性内存取证框架的 Web 界面。
* [inVtero.net](https://github.com/ShaneK2/inVtero.net) - 具有嵌套虚拟机管理程序支持的 Windows x64 高级内存分析。
* [LiME](https://github.com/504ensicsLabs/LiME) - 可加载内核模块 (LKM)，允许从 Linux 和基于 Linux 的设备获取易失性内存，以前称为 DMD。
* [MalConfScan](https://github.com/JPCERTCC/MalConfScan) - MalConfScan 是一个 Volatility 插件，可提取已知恶意软件的配置数据。 Volatility 是一个用于事件响应和恶意软件分析的开源内存取证框架。该工具在内存映像中搜索恶意软件并转储配置数据。此外，该工具还具有列出恶意代码引用的字符串的功能。
* [Memoryze](https://www.fireeye.com/services/freeware/memoryze.html) - 免费的内存取证软件，可帮助事件响应人员发现实时内存中的邪恶。 Memoryze 可以获取和/或分析内存映像，并且在实时系统上，可以在其分析中包含分页文件。
* [Memoryze for Mac](https://www.fireeye.com/services/freeware/memoryze.html) - 适用于 Mac 的 Memoryze 是 Memoryze，但适用于 Mac。然而，功能数量较少。
* [MemProcFS] (https://github.com/ufrisk/MemProcFS) - MemProcFS 是一种将物理内存视为虚拟文件系统中的文件的简单便捷的方法。
* [Orochi](https://github.com/LDO-CERT/orochi) - Orochi 是一个用于协作取证内存转储分析的开源框架。
* [Rekall](http://www.rekall-forensic.com/) - 用于从易失性存储器 (RAM) 样本中提取数字工件的开源工具（和库）。
* [Volatility](https://github.com/volatilityfoundation/volatility) - 高级内存取证框架。
* [Volatility 3](https://github.com/volatilityfoundation/volatility3) - 易失性内存提取框架（Volatility 的后继者）
* [VolatilityBot](https://github.com/mkorman90/VolatilityBot) - 研究人员的自动化工具消除了二进制提取阶段的所有猜测和手动任务，或者帮助研究人员执行内存分析调查的第一步。
* [VolDiff](https://github.com/aim4r/VolDiff) - 基于波动性的恶意软件内存足迹分析。
* [WindowsSCOPE](http://www.windowsscope.com/windowsscope-cyber-forensics/) - 用于分析易失性内存的内存取证和逆向工程工具，提供分析 Windows 内核、驱动程序、DLL 以及虚拟和物理内存的功能。

### 内存映像工具

* [Belkasoft Live RAM Capturer](http://belkasoft.com/ram-capturer) - 微型免费取证工具，即使受到主动反调试或反倾销系统的保护，也能可靠地提取计算机易失性存储器的全部内容。
* [Linux Memory Grabber](https://github.com/halpomeranz/lmg/) - 用于转储 Linux 内存和创建波动性配置文件的脚本。
* [MAGNET DumpIt](https://www.magnetforensics.com/resources/magnet-dumpit-for-windows) - 适用于 Windows（x86、x64、ARM64）的快速内存获取工具。生成 Windows 计算机的完整内存故障转储。
* [Magnet RAM Capture](https://www.magnetforensics.com/free-tool-magnet-ram-capture/) - 免费成像工具，旨在捕获嫌疑人计算机的物理内存。支持最新版本的 Windows。
* [OSForensics](http://www.osforensics.com/) - 用于获取 32 位和 64 位系统上的实时内存的工具。可以转储单个进程的内存空间或物理内存转储。

### OSX 证据收集

* [Knockknock](https://objective-see.com/products/knockknock.html) - 显示设置为在 OSX 上自动执行的持久项目（脚本、命令、二进制文件等）。
* [macOS Artifact Parsing Tool (mac_apt)](https://github.com/ydkhatri/mac_apt) - 基于插件的取证框架，用于快速 mac 分类，适用于实时计算机、磁盘映像或单个工件文件。
* [OSX Auditor](https://github.com/jipegit/OSXAuditor) - 免费的 Mac OS X 计算机取证工具。
* [OSX Collector](https://github.com/yelp/osxcollector) - 用于实时响应的 OSX Auditor 分支。
* [The ESF Playground](https://themittenmac.com/the-esf-playground/) - 实时查看 Apple Endpoint Security Framework (ESF) 中的事件的工具。

### 其他清单

* [Awesome Event IDs](https://github.com/stuhli/awesome-event-ids) - 对数字取证和事件响应有用的事件 ID 资源集合。
* [Awesome Forensics](https://github.com/cugu/awesome-forensics) - 精彩的取证分析工具和资源的精选列表。
* [Didier Stevens Suite](https://github.com/DidierStevens/DidierStevensSuite) - 工具集合
* [Eric Zimmerman Tools](https://ericzimmerman.github.io/) - 由 SANS 研究所讲师 Eric Zimmerman 创建的取证工具的更新列表。
* [List of various Security APIs](https://github.com/deralexxx/security-apis) - 用于安全性的公共 JSON API 的集体列表。

### 其他工具

* [Cortex](https://thehive-project.org) - Cortex 允许您使用 Web 界面一一或批量模式分析 IP 和电子邮件地址、URL、域名、文件或哈希值等可观察数据。分析师还可以使用其 REST API 自动执行这些操作。
* [Crits](https://crits.github.io/) - 基于网络的工具，将分析引擎与网络威胁数据库相结合。
* [Diffy](https://github.com/Netflix-Skunkworks/diffy) - DFIR 工具由 Netflix 的 SIRT 开发，允许调查人员在事件期间快速确定跨云实例（目前 AWS 上的 Linux 实例）的妥协范围，并通过显示与基线的差异来有效地对这些实例进行后续操作分类。
* [domfind](https://github.com/diogo-fernan/domfind) - Python DNS 爬虫用于查找不同 TLD 下的相同域名。
* [Fileintel](https://github.com/keithjjones/fileintel) - 提取每个文件哈希的情报。
* [HELK](https://github.com/Cyb3rWard0g/HELK) - 威胁狩猎平台。
* [Hindsight](https://github.com/obsidianforensics/hindsight) - Google Chrome/Chromium 的互联网历史取证。
* [Hostintel](https://github.com/keithjjones/hostintel) - 每个主机提取情报。
* [IPASIS](https://ipasis.com/) - 用于调查可疑交互的实时 IP 信誉和电子邮件验证 API。在单个 API 调用中返回将 VPN/代理/Tor 检测与电子邮件风险评估相结合的交互信任评分 (0-100)。
* [imagemounter](https://github.com/ralphje/imagemounter) - 命令行实用程序和 Python 包可简化取证磁盘映像的安装（卸载）。
* [Kansa](https://github.com/davehull/Kansa/) - PowerShell 中的模块化事件响应框架。
* [MFT Browser](https://github.com/kacos2000/MFT_Browser) - MFT目录树重建和记录信息。
* [Munin](https://github.com/Neo23x0/munin) - VirusTotal 和其他服务的在线哈希检查器。
* [PowerSponse](https://github.com/swisscom/PowerSponse) - PowerSponse 是一个 PowerShell 模块，专注于安全事件响应期间的有针对性的遏制和修复。
* [PyaraScanner](https://github.com/nogoodconfig/pyarascanner) - 非常简单的多线程多规则到多文件 YARA 扫描恶意软件动物园和 IR 的 Python 脚本。
* [rastrea2r](https://github.com/rastrea2r/rastrea2r) - 允许在 Windows、Linux 和 OS X 上使用 YARA 扫描磁盘和内存中的 IOC。
* [RaQet](https://raqet.github.io/) - 非常规的远程采集和分类工具，允许对使用专门构建的取证操作系统重新启动的远程计算机（客户端）的磁盘进行分类。
* [Raccine](https://github.com/Neo23x0/Raccine) - 简单的勒索软件保护
* [Stalk](https://www.percona.com/doc/percona-toolkit/2.2/pt-stalk.html) - 当问题发生时收集有关 MySQL 的取证数据。
* [Scout2](https://nccgroup.github.io/Scout2/) - 安全工具，可让 Amazon Web Services 管理员评估其环境的安全状况。
* [Stenographer](https://github.com/google/stenographer) - 数据包捕获解决方案旨在快速将所有数据包假脱机到磁盘，然后提供对这些数据包子集的简单、快速访问。它存储尽可能多的历史记录，管理磁盘使用情况，并在达到磁盘限制时删除。它非常适合在事件发生之前和期间捕获流量，而无需明确需要存储所有网络流量。
* [sqhunter](https://github.com/0x4d31/sqhunter) - 基于 osquery 和 Salt Open (SaltStack) 的威胁猎手，可以发出临时或分布式查询，而不需要 osquery 的 tls 插件。 sqhunter 允许您查询开放的网络套接字并根据威胁情报源检查它们。
* [sysmon-config](https://github.com/SwiftOnSecurity/sysmon-config) - 具有默认高质量事件跟踪的 Sysmon 配置文件模板
* [sysmon-modular](https://github.com/olafhartong/sysmon-modular) - sysmon 配置模块的存储库
* [traceroute-circl](https://github.com/CIRCL/traceroute-circl) - 扩展跟踪路由以支持 CSIRT（或 CERT）操作员的活动。通常，CSIRT 团队必须根据收到的 IP 地址来处理事件。由卢森堡计算机应急响应中心创建。
* [X-Ray 2.0](https://www.raymond.cc/blog/xray/) - 用于向 AV 供应商提交病毒样本的 Windows 实用程序（维护不良或不再维护）。

### 剧本

* [AWS Incident Response Runbook Samples](https://github.com/aws-samples/aws-incident-response-runbooks/tree/0d9a1c0f7ad68fb2c1b2d86be8914f2069492e21) - AWS IR Runbook 示例旨在为每个使用它们的实体进行定制。这三个样本是：“DoS 或 DDoS 攻击”、“凭证泄漏”和“意外访问 Amazon S3 存储桶”。
* [Counteractive Playbooks](https://github.com/counteractive/incident-response-plan-template/tree/master/playbooks) - 反作用剧本集合。
* [GuardSIght Playbook Battle Cards](https://github.com/guardsight/gsvsoc_cirt-playbook-battle-cards) - 网络事件响应手册战斗卡合集
* [IRM](https://github.com/certsocietegenerale/IRM) - CERT 法国兴业银行的事件响应方法。
* [PagerDuty Incident Response Documentation](https://response.pagerduty.com/) - 描述 PagerDuty 事件响应流程的部分内容的文档。它不仅提供了有关为事件做好准备的信息，还提供了事件发生期间和事件发生后应该做什么的信息。源代码可在 [GitHub](https://github.com/PagerDuty/incident-response-docs) 上找到。
* [Phantom Community Playbooks](https://github.com/phantomcyber/playbooks) - 适用于 Splunk 的 Phantom 社区手册，也可定制用于其他用途。
* [ThreatHunter-Playbook](https://github.com/OTRF/ThreatHunter-Playbook) - 帮助制定狩猎活动技术和假设的手册。

### 进程转储工具

* [Microsoft ProcDump](https://docs.microsoft.com/en-us/sysinternals/downloads/procdump) - 即时转储任何正在运行的 Win32 进程内存映像。
* [PMDump](http://www.ntsecurity.nu/toolbox/pmdump/) - 允许您将进程的内存内容转储到文件而不停止进程的工具。

### 沙箱/逆向工具

* [Any Run](https://app.any.run/) - 交互式在线恶意软件分析服务，用于使用任何环境对大多数类型的威胁进行动态和静态研究。
* [CAPA](https://github.com/mandiant/capa) - 检测可执行文件中的功能。您针对 PE、ELF、.NET 模块或 shellcode 文件运行它，它会告诉您它认为该程序可以做什么。
* [CAPEv2](https://github.com/kevoreilly/CAPEv2) - 恶意软件配置和有效负载提取。
* [Cuckoo](https://github.com/cuckoosandbox/cuckoo) - 开源高度可配置的沙箱工具。
* [Cuckoo-modified](https://github.com/spender-sandbox/cuckoo-modified) - 由社区开发的经过大量修改的 Cuckoo 叉。
* [Cuckoo-modified-api](https://github.com/keithjjones/cuckoo-modified-api) - 用于控制经过 Cuckoo 修改的沙箱的 Python 库。
* [Cutter](https://github.com/rizinorg/cutter) - 由 rizin 提供支持的免费开源逆向工程平台。
* [Ghidra](https://github.com/NationalSecurityAgency/ghidra) - 软件逆向工程框架。
* [Hybrid-Analysis](https://www.hybrid-analysis.com/) - CrowdStrike 提供的免费、强大的在线沙箱。
* [Intezer](https://analyze.intezer.com/#/) - Intezer Analytics 深入研究 Windows 二进制文件，检测与已知威胁的微代码相似性，以提供准确且易于理解的结果。
* [Joe Sandbox (Community)](https://www.joesandbox.com/) - Joe Sandbox 检测并分析 Windows、Android、Mac OS、Linux 和 iOS 上的潜在恶意文件和 URL 是否存在可疑活动；提供全面、详细的分析报告。
* [Mastiff](https://github.com/KoreLogicSecurity/mastiff) - 静态分析框架，可自动执行从多种不同文件格式中提取关键特征的过程。
* [Metadefender Cloud](https://www.metadefender.com) - 免费的威胁情报平台提供多重扫描、数据清理和文件漏洞评估。
* [Radare2](https://github.com/radareorg/radare2) - 逆向工程框架和命令行工具集。
* [Reverse.IT](https://www.reverse.it/) - CrowdStrike 提供的混合分析工具的替代域。
* [Rizin](https://github.com/rizinorg/rizin) - 类 UNIX 逆向工程框架和命令行工具集
* [StringSifter](https://github.com/fireeye/stringsifter) - 一种机器学习工具，根据字符串与恶意软件分析的相关性对字符串进行排名。
* [Threat.Zone](https://app.threat.zone) - 基于云的威胁分析平台，包括沙箱、CDR 和研究人员的交互式分析。
* [Valkyrie Comodo](https://valkyrie.comodo.com) - Valkyrie 使用运行时行为和文件中的数百个功能来执行分析。
* [Viper](https://github.com/viper-framework/viper) - 基于Python的二进制分析和管理框架，与Cuckoo和YARA配合良好。
* [Virustotal](https://www.virustotal.com) - 免费在线服务，可分析文件和 URL，识别病毒、蠕虫、特洛伊木马以及防病毒引擎和网站扫描程序检测到的其他类型的恶意内容。
* [Visualize_Logs](https://github.com/keithjjones/visualize_logs) - 开源可视化库和日志命令行工具（Cuckoo、Procmon 等）。
* [Yomi](https://yomi.yoroi.company) - 由 Yoroi 管理和托管的免费 MultiSandbox。

### 扫描仪工具

* [Fenrir](https://github.com/Neo23x0/Fenrir) - 简单的 IOC 扫描仪。它允许在普通 bash 中扫描任何 Linux/Unix/OSX 系统的 IOC。由《雷神》和《洛基》的创作者创建。
* [LOKI](https://github.com/Neo23x0/Loki) - 免费的红外扫描仪，用于使用 yara 规则和其他指标（IOC）扫描端点。
* [Spyre](https://github.com/spyre-project/spyre) - 用 Go 编写的简单的基于 YARA 的 IOC 扫描器

### 时间轴工具

* [Aurora Incident Response](https://github.com/cyb3rfox/Aurora-Incident-Response) - 开发平台可以轻松构建事件的详细时间表。
* [Highlighter](https://www.fireeye.com/services/freeware/highlighter.html) - Fire/Mandiant 提供的免费工具将描述日志/文本文件，可以突出显示图形上与关键字或短语相对应的区域。有助于确定感染的时间以及妥协后所做的事情。
* [Morgue](https://github.com/etsy/morgue) - Etsy 的 PHP Web 应用程序，用于管理事后分析。
* [Plaso](https://github.com/log2timeline/plaso) - 用于 log2timeline 工具的基于 Python 的后端引擎。
* [Timesketch](https://github.com/google/timesketch) - 用于协作取证时间线分析的开源工具。

### 视频

* [The Future of Incident Response](https://www.youtube.com/watch?v=bDcx4UNpKNc) - 由 Bruce Schneier 在 OWASP AppSecUSA 2015 上发表。

### Windows 证据收集

* [AChoir](https://github.com/OMENScan/AChoir) - 框架/脚本工具，用于标准化和简化 Windows 实时采集实用程序的脚本编写过程。
* [Crowd Response](http://www.crowdstrike.com/community-tools/) - 轻量级 Windows 控制台应用程序，旨在帮助收集系统信息以进行事件响应和安全活动。它具有众多模块和输出格式。
* [Cyber Triage](http://www.cybertriage.com) - Cyber​​ Triage 有一个免费使用的轻量级收集工具。它收集源文件（例如注册表配置单元和事件日志），但也在实时主机上解析它们，以便它还可以收集启动项、计划、任务等引用的可执行文件。它的输出是一个 JSON 文件，可以导入到免费版本的 Cyber​​ Triage 中。 Cyber​​ Triage 由 Sleuth Kit Labs 制作，该公司也制作 Autopsy。
* [DFIR ORC](https://dfir-orc.github.io/) - DFIR ORC 是专门工具的集合，专用于可靠地解析和收集关键工件，例如 MFT、注册表配置单元或事件日志。 DFIR ORC 收集数据，但不分析数据：它的目的不是对机器进行分类。它提供运行 Microsoft Windows 的计算机的取证相关快照。代码可以在[GitHub](https://github.com/DFIR-ORC/dfir-orc)上找到。
* [FastIR Collector](https://github.com/SekoiaLab/Fastir_Collector) - 用于收集实时 Windows 系统上的不同工件并将结果记录在 csv 文件中的工具。通过对这些工件的分析，可以检测到早期的危害。
* [Fibratus](https://github.com/rabbitstack/fibratus) - 用于探索和跟踪 Windows 内核的工具。
* [Hoarder](https://github.com/muteb/Hoarder) - 收集最有价值的文物用于取证或事件响应调查。
* [IREC](https://binalyze.com/products/irec-free/) - 一体化 IR 证据收集器，可捕获 RAM 映像、$MFT、事件日志、WMI 脚本、注册表配置单元、系统还原点等。它是免费的、快如闪电且易于使用。
* [Invoke-LiveResponse](https://github.com/mgreen27/Invoke-LiveResponse) - Invoke-LiveResponse是一个用于定向收集的实时响应工具。
* [IOC Finder](https://www.fireeye.com/services/freeware/ioc-finder.html) - Mandiant 提供的免费工具，用于收集主机系统数据并报告妥协指标 (IOC) 的存在。仅支持 Windows。不再维护。仅完全支持 Windows 7 / Windows Server 2008 R2。
* [IRTriage](https://github.com/AJMartel/IRTriage) - 事件响应分类 - 用于取证分析的 Windows 证据收集。
* [KAPE](https://www.kroll.com/en/services/cyber-risk/incident-response-litigation-support/kroll-artifact-parser-extractor-kape) - Eric Zimmerman 的 Kroll Artifact 解析器和提取器 (KAPE)。一种分类工具，可以找到最流行的数字工件，然后快速解析它们。当时间紧迫时，伟大而彻底。
* [LOKI](https://github.com/Neo23x0/Loki) - 免费的红外扫描仪，用于使用 yara 规则和其他指标（IOC）扫描端点。
* [MEERKAT](https://github.com/TonyPhipps/Meerkat) - 适用于 Windows 的基于 PowerShell 的分类和威胁搜寻。
* [Panorama](https://github.com/AlmCo/Panorama) - 实时 Windows 系统上的快速事件概述。
* [PowerForensics](https://github.com/Invoke-IR/PowerForensics) - Live磁盘取证平台，使用PowerShell。
* [PSRecon](https://github.com/gfoss/PSRecon/) - PSRecon 使用 PowerShell（v2 或更高版本）从远程 Windows 主机收集数据，将数据组织到文件夹中，对所有提取的数据进行哈希处理，对 PowerShell 和各种系统属性进行哈希处理，然后将数据发送给安全团队。数据可以推送到共享、通过电子邮件发送或保留在本地。
* [RegRipper](https://github.com/keydet89/RegRipper3.0) - 用 Perl 编写的开源工具，用于从注册表中提取/解析信息（键、值、数据）并将其呈现以供分析。
