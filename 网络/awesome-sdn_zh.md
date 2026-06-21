# 很棒的SDN [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

关于软件定义网络 (SDN) 的精彩列表

- [很棒的SDN](#awesome-sdn)
  - [Introduction](#introduction)
  - [网络操作系统](#network-operating-system)
  - [安装环境](#install-environment)
  - [软件开关](#software-switch)
  - [网络虚拟化](#network-virtualization)
  - [Protocol](#protocol)
  - [Controller](#controller)
  - [Simulator/Emulator](#simulatoremulator)
  - [Language](#language)
  - [Library](#library)
  - [Test](#test)
  - [NFV](#nfv)
  - [覆盖网络](#overlay-network)
  - [Router](#router)
  - [Misc](#misc)
  - [高性能网络](#high-performance-network)
  - [用户空间网络堆栈](#userspace-network-stack)
  - [Analytics](#analytics)
- [Resources](#resources)
  - [Books](#books)
  - [Paper](#paper)

# 简介
软件定义网络 (SDN) 是一种计算机网络方法，允许网络管理员通过抽象更高级别的功能来管理网络服务。
Wiki：[软件定义网络](https://en.wikipedia.org/wiki/Software-defined_networking)

# 网络操作系统

- [Beluganos](https://github.com/beluganos/beluganos) - Beluganos是一款专为白盒交换机（OF-DPA）设计的新型网络操作系统，可以应用大规模网络。
- [Cumulus Linux](https://cumulusnetworks.com) - Cumulus Linux 是一个功能强大的开放网络操作系统，允许您使用网络规模原理（如世界上最大的数据中心）进行自动化、自定义和扩展。
- [FlexSwitch](https://snaproute.com/) - 第一个开源网络协议套件，提供完整的第 2 层/第 3 层功能，可加速白盒网络设备的开发和部署
- [Mion](https://github.com/opencomputeproject/mion) - 基于ONLP API和Yocto项目的交换机操作系统。
- [OcNOS](https://www.ipinfusion.com/) - 广泛的交换和路由协议支持以及 MPLS 和 SDN 等高级功能
- [Open Network Linux, ONL](https://opennetlinux.org) - “裸机”交换机的 Linux 发行版，即由商品组件构建的网络转发设备。
- [OpenSwitch](http://www.openswitch.net) - Dell EMC 的 Linux 网络操作系统。
- [OpenWrt](https://openwrt.org/) - 是一个针对嵌入式设备的Linux操作系统。
- [PicOS](http://www.pica8.com/products/picos) - 适用于白盒交换机第 2/3 层功能集的 SDN 操作系统，支持 OpenFlow、OVSDB 和其他协议。
- [SONiC](https://azure.github.io/SONiC/) - 云端开放网络软件 SONiC
- [Stratum](https://stratumproject.org/) - 用于软件定义网络的开源、独立于芯片的交换机操作系统

# 安装环境

- [ONIE](http://onie.org/) - ONIE 支持裸机网络交换机生态系统，最终用户可以在不同的网络操作系统之间进行选择。

# 软件开关

- [BESS](https://github.com/NetSys/bess) - 伯克利可扩展软件交换机，BESS 是软件交换机的模块化框架。
- [bmv2](https://github.com/p4lang/behavioral-model) - P4软件开关，通常用作验证开发人员用P4语言描述的功能的工具。
- [CPqD](https://github.com/CPqD/ofsoftswitch13) - 兼容 OpenFlow 1.3 的用户空间软件交换机实现
- [FD.IO](https://fd.io/) - 不懈地关注数据 IO 速度和效率，以实现更灵活和可扩展的网络和存储
- [Indigo](https://github.com/floodlight/indigo) - Indigo 是一个开源项目，旨在支持物理交换机和虚拟机管理程序交换机上的 OpenFlow。
- [Lagopus](https://lagopus.github.io) - 高性能软件 OpenFlow 1.3 交换机。
- [LINC-Switch](https://github.com/FlowForwarding/LINC-Switch) - 用 Erlang 编写的纯 OpenFlow 软件交换机
- [Open vSwitch](http://openvswitch.org/) - Open vSwitch 是一款生产质量的多层虚拟交换机。
- [PISCES](https://www.cs.princeton.edu/~jrex/papers/pisces16.pdf) - 可编程、独立于协议的软件开关。
- [snabbswitch](https://github.com/SnabbCo/snabbswitch) - 开源虚拟化以太网网络堆栈。
- [ZeroTier](https://github.com/zerotier/ZeroTierOne) - ZeroTier 是一款适用于地球的基于软件的托管以太网交换机。

# 网络虚拟化

- [FlowVisor](https://github.com/opennetworkinglab/flowvisor) - 充当交换机和多个控制器之间的管理程序/代理的 OpenFlow 控制器。可以并行对多个交换机进行切片，从而有效地对网络进行切片。
- [OpenVirtex](https://github.com/opennetworkinglab/OpenVirteX) - 网络管理程序可以在单个物理基础设施之上创建多个虚拟和可编程网络。

# 协议

- [OpenFlow](https://www.opennetworking.org/sdn-resources/openflow) - 一种通信协议，可通过网络访问网络交换机或路由器的转发平面。
- [OF-Config](https://www.opennetworking.org/technical-communities/areas/specification/of-config/) - OpenFlow管理和配置协议
- [OVSDB](https://tools.ietf.org/html/rfc7047) - 用于管理 OpenvSwitch 数据库的通信协议。
- [NETCONF](https://en.wikipedia.org/wiki/NETCONF)
- [OpFlex](http://www.cisco.com/c/en/us/solutions/collateral/data-center-virtualization/application-centric-infrastructure/white-paper-c11-731302.html)
- [路径计算元素协议，PCEP](https://www.juniper.net/documentation/en_US/junos/topics/concept/mpls-pcep-overview.html)
- [可扩展消息传递和状态协议，XMPP](https://en.wikipedia.org/wiki/XMPP)
- [P4运行时](https://p4.org/api/p4-runtime-putting-the-control-plane-in-charge-of-the-forwarding-plane.html)
- [gNMI](https://github.com/openconfig/gnmi/) - gRPC 网络管理接口
- [gNOI](https://github.com/openconfig/gnoi) - gRPC 网络操作接口

# 控制器

- [Beehive Network Controller](https://github.com/kandoo/beehive-netctrl) - 构建在 Beehive 之上的分布式 SDN 控制器。它支持 OpenFlow，但可以轻松扩展为其他南向协议。
- [Floodlight](https://github.com/floodlight/floodlight) - 基于java的OpenFlow控制器。
- [IRIS](http://openiris.etri.re.kr/) - 由 ETRI SDN 研究部门创建的递归 SDN Openflow 控制器。
- [lighty.io core](https://github.com/PantheonTechnologies/lighty-core) - lighty.io 核心组件 - 用于构建基于 Java 的 SDN 控制器的开源开发框架。
- [Netrack](https://github.com/netrack/openflow) - Go 中的 OpenFlow 控制器框架。
- [NodeFlow](https://github.com/gaberger/NodeFLow) - OpenFlow 控制器节点样式。
- [NOX](https://github.com/noxrepo/nox) - 用于基于 C++ 的软件定义网络 (*SDN*) 控制应用程序的开源开发平台。
- [OESS](https://github.com/globalnoc/oess) - Open Exchange 软件套件，用于配置和控制支持 OpenFlow 的交换机。
- [ONOS](http://onosproject.org) - 开放网络操作系统。
- [Open MUL](http://www.openmul.org/openmul-controller.html) - 一个几乎完全用 C 从头开始​​编写的轻量级 SDN/Openflow 控制器。
- [Open Security Controller](https://www.opensecuritycontroller.org/) - 软件定义的安全编排解决方案，可自动部署虚拟化网络安全功能，例如下一代防火墙、入侵防御系统和应用程序数据控制器
- [OpenContrail](https://tungsten.io/opencontrail-is-now-tungsten-fabric/) - SDN 项目利用 SDN 和 NFV，并提供网络虚拟化所需的所有组件。
- [OpenDaylight](https://www.opendaylight.org) - 开放日光平台
- [OVN](http://www.openvswitch.org//support/slides/OVN-Vancouver.pdf) - OVN：Open vSwitch 的开放虚拟网络
- [POX](https://github.com/noxrepo/pox) - 用于基于 Python 的软件定义网络 (*SDN*) 控制应用程序的开源开发平台。
- [Ravel](https://github.com/ravel-net/ravel) - 使用标准 SQL 数据库来表示网络的软件定义网络 (SDN) 控制器。
- [Ryu](https://ryu-sdn.org/) - 基于组件的软件定义网络框架。
- [Trema](https://trema.github.io/trema/) - 一个易于使用的全栈框架，用于用 Ruby 和 C 语言开发 OpenFlow 控制器。
- [Vyatta](https://github.com/BRCDcomm/BVC/) - 第一个直接从 OpenDaylight 构建的商业控制器。

# 模拟器/模拟器

- [Containernet](https://github.com/containernet/containernet) - Mininet 分支允许使用 Docker 容器作为模拟网络中的主机
- [EstiNet](http://www.estinet.com/products.php?lv1=13&sn=13) - 全球知名的网络规划软件工具
- [MaxiNet](http://maxinet.github.io) - MaxiNet 扩展了著名的 Mininet 仿真环境，以跨多个物理机器进行仿真。这允许模拟非常大的软件定义网络。
- [Mininet](http://mininet.org/) - 笔记本电脑（或其他 PC）上的即时虚拟网络
- [ns-3](https://www.nsnam.org/) - 支持OpenFlow环境的离散事件网络模拟器。
- [OpenNet](http://github.com/dlinknctu/opennet) - 软件定义无线局域网模拟器
- [Tinynet](https://github.com/John-Lin/tinynet) - 用于快速原型设计 SDN 的轻量级即时虚拟网络

# 语言

- [Frenetic](https://github.com/frenetic-lang/frenetic) - Frenetic 编程语言和运行时系统
- [NEMO](https://wiki.onosproject.org/display/ONOS/NEMO+Language) - 基于网络模型抽象和操作模式总结的领域特定语言（DSL）。
- [P4](http://p4.org/) - 一种声明性语言，用于表达网络转发元件（例如交换机、NIC、路由器或网络功能设备）的管道如何处理数据包。
- [POF](https://dl.acm.org/citation.cfm?id=2491190) - 协议不经意转发
- [Pyretic](http://www.frenetic-lang.org/pyretic/) - Pyretic 是 SDN 编程语言 Frenetic 家族的成员之一。

# 图书馆

- [loxigen](https://github.com/floodlight/loxigen) - LoxiGen 是一个为多种语言生成 OpenFlow 协议库的工具。
- [nettle](https://github.com/AndreasVoellmy/openflow) - 用于使用 OpenFlow 协议的 Haskell 库。
- [OCaml OpenFlow](https://github.com/frenetic-lang/ocaml-openflow) - OpenFlow 的序列化和协议库。
- [oflib-node](https://github.com/TrafficLab/oflib-node) - Oflib-node 是 Node.js 的 OpenFlow 协议库。它在 OpenFlow 有线协议消息和 Javascript 对象之间进行转换。
- [openfaucet](https://github.com/rlenglet/openfaucet) - openfaucet 是 OpenFlow 1.0.0 协议的纯 Python 实现，基于 Twisted。
- [OpenFlowJ](https://bitbucket.org/openflowj/openflowj) - 低级 OpenFlow 数据包编组/解组和 IO 操作的 Java 实现。
- [Scapy](http://www.secdev.org/projects/scapy/) - Scapy 是一个功能强大的交互式数据包操作程序。

# 测试

- [Cbenech](https://github.com/mininet/oflops/tree/master/cbench) - 控制器基准测试工具
- [nice-of](https://code.google.com/archive/p/nice-of/) - 用于测试 NOX 控制器平台的 OpenFlow 控制器应用程序的工具。
- [oftest](https://github.com/floodlight/oftest) - OpenFlow测试框架
- [OpenSDNCore](http://www.opensdncore.org/) - NFV/SDN 环境的虚拟化测试平台。
- [ptf](https://github.com/p4lang/ptf) - 一个基于unittest的基于python的dataplane测试框架。
- [STS](https://ucb-sts.github.com/sts/) - SDN 故障排除系统，模拟网络设备，允许以编程方式生成测试用例。

# 网络功能虚拟化

- [OPNFV](https://www.opnfv.org) - 通过集成的开放平台加速 NFV 的演进。

# 覆盖网络

- [GENEVE](https://www.redhat.com/en/blog/what-geneve) - 什么是日内瓦？
- [NVGRE](https://tools.ietf.org/html/draft-sridharan-virtualization-nvgre-00) - NVGRE-使用通用路由封装的网络虚拟化
- [VXLAN](https://en.wikipedia.org/wiki/Virtual_Extensible_LAN) - 虚拟可扩展局域网

# 路由器

- [bgp4r](https://github.com/jesnault/bgp4r) - BGP4R 是一个 ruby 库，可以创建和操作 BGP 消息。在 BGP4R 中，所有众所周知的 BGP 构造都是在类中定义的。
- [BGPFeeder](https://github.com/BytemarkHosting/bgpfeeder)
- [Bird](http://bird.network.cz/) - BIRD 项目旨在开发一个功能齐全的动态 IP 路由守护程序，主要针对（但不限于）Linux、FreeBSD 和其他类 UNIX 系统，并在 GNU 通用公共许可证下分发。
- [FreeRouter](http://freerouter.nop.hu/) - 基于Java的虚拟路由器
- [FRRouting](https://frrouting.org/) - 适用于 Linux 和 Unix 平台的 IP 路由协议套件，其中包括 BGP4、BGP4+、OSPFv2、OSPFv3、RIPv1、RIPv2、RIPng、PIM-SM/MSDP 和 LDP 的协议守护程序，以及对 IS-IS、EIGRP 和 NHRP 的早期支持。
- [gobgp](https://github.com/osrg/gobgp) - GoBGP 是一个开源 BGP 实现，专为现代环境而设计，并以现代编程语言 Go 编程语言实现。
- [Quagga](http://www.quagga.net/) - Quagga 是一个路由软件套件，为 Unix 平台（特别是 FreeBSD、Linux、Solaris 和 NetBSD）提供 OSPFv2、OSPFv3、RIP v1 和 v2、RIPng 和 BGP-4 的实现。 Quagga 是 GNU Zebra 的一个分支，由 Kunihiro Ishiguro 开发。
- [yabgp](https://github.com/smartbgp/yabgp) - YABGP 是 BGP 协议的另一个 Python 实现。它可用于与各种路由器（包括真实的 Cisco/HuaWei/Juniper 路由器和一些路由器模拟器（如 GNS3））建立 BGP 连接，并接收/解析 BGP 消息以供将来分析。

# 杂项

- [Aether Project](https://www.opennetworking.org/aether/) - 第一个开源企业 5G/LTE 边缘云即服务平台 (ECaaS)。
- [Central Office Re-architected as a Datacenter, CORD](http://opencord.org) - 提供云经济性和敏捷性的服务交付平台的参考实现。
- [Mininet Spear Narmox](http://mininet.spear.narmox.com) - 在线 Web 服务提供 Mininet 拓扑的可视化
- [Open Network Automation Platform, ONAP](https://www.onap.org/) - 这两个项目的结合为虚拟网络功能的实时、策略驱动的软件自动化创建了一个协调且全面的框架，使软件、网络、IT 和云提供商和开发人员能够快速创建新服务。
- [开源 MANO 社区、OSM](https://osm.etsi.org/welcome/)
- [OPEN-Orchestrator 项目，Open-O](https://www.open-o.org)

# 高性能网络

- [ASAP2](http://www.mellanox.com/blog/2016/12/three-ways-asap2-beats-dpdk-for-cloud-and-nfv/) - ASAP2 加速器构建在 eSwitch NIC 硬件之上，允许将整个虚拟交换机或虚拟交换机或分布式虚拟路由器 (DVR) 操作的重要部分卸载到 Mellanox NIC
- [DPDK](http://dpdk.org/) - DPDK 是一组用于快速数据包处理的库和驱动程序。
- [RDMA](https://en.wikipedia.org/wiki/Remote_direct_memory_access) - 远程直接内存访问 (RDMA) 是从一台计算机的内存到另一台计算机的内存的直接内存访问，而不涉及任一计算机的操作系统。这允许高吞吐量、低延迟的网络
- [XDP](https://www.iovisor.org/technology/xdp) - XDP 或 eXpress 数据路径作为 IO Visor 项目的一部分，在 Linux 内核中提供高性能、可编程网络数据路径。
它被设计为在任何处理器上运行。第一个支持的 CPU 是 Intel x86，现在已扩展到 IBM POWER 和 ARM。


# 用户空间网络堆栈

- [drv-netif-dpdk](https://github.com/rumpkernel/drv-netif-dpdk) - drv-netif-dpdk 是用于 rump 内核的 DPDK 网络接口。组合结果是用户空间 TCP/IP 堆栈通过 DPDK 执行数据包 I/O。
- [f-stack](https://github.com/F-Stack/f-stack) - F-Stack是一个基于DPDK、FreeBSD TCP/IP堆栈和协程API的高性能用户空间网络开发套件。
- [mTCP](https://github.com/eunyoung14/mtcp) - mTCP 是用于多核系统的高度可扩展的用户级 TCP 堆栈。 mTCP 源代码根据修改版 BSD 许可证分发。有关更多详细信息，请参阅许可证。 io_engine 驱动程序和移植应用程序的许可条款可能与 mTCP 的不同。
- [net-next-nuse](https://github.com/libos-nuse/net-next-nuse) - 用户空间中的网络堆栈 (NUSE) NUSE 允许我们使用 Linux 网络堆栈作为一个库，任何应用程序都可以通过链接该库来目录使用。每个应用程序都有自己的网络堆栈，因此它提供了除主机操作系统之外的即时虚拟化环境。
- [nff-go](https://github.com/intel-go/nff-go) - NFF-Go 成为 Linux 基金会下 DPDK 项目伞的一部分！镜像仓库可以在这里找到：http://dpdk.org/browse/apps/nff-go/。我们也将通过 DPDK 邮件列表和标准 DPDK 贡献流程接受补丁。

# 分析

- [Apache Spot](http://spot.incubator.apache.org/) - 社区驱动的网络安全项目，从头开始构建，旨在为开放、可扩展的平台上的所有 IT 遥测数据提供高级分析
- [PNDA](http://pnda.io/) - 适用于网络和服务的可扩展开源大数据分析平台。
- [SNAS](http://www.snas.io/) - 流网络分析系统（项目SNAS）是一个实时收集、跟踪和访问数千万个路由对象（路由器、对等点、前缀）的框架。

# 资源
## 书籍

- [网络 DevOps](https://www.packtpub.com/networking-and-servers/devops-networking)
- [网络算法：设计快速网络设备的跨学科方法](https://doc.lagout.org/network/Network%20Algorithmics%20An%20Interdisciplinary%20Approach%20to%20Designing%20Fast%20Networked%20Devices.pdf)
- [下一代网络工程师的网络可编程性和自动化技能](http://shop.oreilly.com/product/0636920042082.do)
- [SDN：软件定义网络：网络可编程技术的权威评论](https://www.oreilly.com/library/view/sdn-software-defined/9781449342425/)
- [SDN网络指南](https://feisky.gitbooks.io/sdn/)(OpenSource Book in Chinese by Pengfei Ni)
- [SDN核心技术剖析和实战指南](http://www.sdnlab.com/book/9480.html)
- [使用 OpenFlow 的软件定义网络](https://www.packtpub.com/networking-and-servers/software-defined-networking-openflow)
- [圖解OpenFlow](http://www.books.com.tw/products/CN11301942)
- [重构网络-SDN架构与实现](http://www.sdnlab.com/book/18762.html)
- [深度解析SDN: 利益、战略、技术、实践](http://www.sdnlab.com/book/9470.html)
- [软件定义网络:SDN与OpenFlow解析](http://www.sdnlab.com/book/9473.html)

## 纸

- [数据中心网络导览](http://static.googleusercontent.com/media/research.google.com/zh-CN//pubs/archive/40404.pdf)
- [有状态SDN数据平面的安全性调查](https://ieeexplore.ieee.org/document/7890396)
- [高性能数据中心网络：架构、算法和机遇](https://static.googleusercontent.com/media/research.google.com/zh-TW//pubs/archive/37069.pdf)
- [重新架构数据中心网络和堆栈以实现低延迟和高性能](http://dl.acm.org/citation.cfm?id=3098825)
- [SDN 综合调查](https://arxiv.org/pdf/1406.0440.pdf)

## 很棒的帖子
- [VXLAN L3应用EVPN，呈现完整overlay网络](https://www.sdnlab.com/19879.html)
