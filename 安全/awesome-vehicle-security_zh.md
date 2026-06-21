# 出色的车辆安全性 [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)


*精选的资源、书籍、硬件、软件、应用程序、关注的人以及有关车辆安全、汽车黑客和修补汽车功能的更酷的内容的精选列表。*

![](资产/car_hacking_jeep.gif)

---

我希望得到尽可能多的帮助。 [开始贡献！](https://github.com/jaredmichaelsmith/awesome-vehicle-security/blob/master/contributing.md)

在 [Twitter](https://twitter.com/jaredthecoder) 上关注我以获得更多安全优势。

---

# 内容

- [相关列表](#related-lists)
- [Learn](#learn)
    - [Articles](#articles)
    - [Presentations](#presentations)
    - [Books](#books)
    - [研究论文](#research-papers)
    - [Courses](#courses)
    - [Blogs](#blogs)
    - [Websites](#websites)
    - [Newsletters](#newsletters)
    - [Conferences](#conferences)
    - [关注谁](#who-to-follow)
    - [播客和剧集](#podcasts-and-episodes)
        - [Podcasts](#podcasts)
        - [Episodes](#episodes)
    - [Miscellaneous](#miscellaneous)
- [Projects](#projects)
- [Hardware](#hardware)
- [Software](#software)
  - [Applications](#applications)
  - [库和工具](#libraries-and-tools)
    - [C](#c)
    - [Java](#java)
    - [C++](#c++)
    - [Python](#python)
    - [Go](#go)
    - [JavaScript](#javascript)
- [公司和职位](#companies-and-jobs)
    - [协调披露](#coordinated-disclosure)
- [其他很棒的（非车辆相关）列表](#other-awesome-lists)
- [Contributing](#contributing)

# 相关列表

这些列表与您在汽车黑客世界中找到的特定协议相关。

- [Awesome CAN Bus - 一个很棒的 CAN 总线相关工具（硬件、软件等）列表](https://github.com/iDoka/awesome-canbus)
- [Awesome LIN Bus - LIN 总线相关工具（硬件、软件等）的很棒列表](https://github.com/iDoka/awesome-linbus)

# 学习

## 文章

- [How to hack a car — a quick crash-course](https://medium.freecodecamp.org/hacking-cars-a-guide-tutorial-on-how-to-hack-a-car-5eafcfbbb7ec) - 汽车爱好者肯尼·库切拉 (Kenny Kuchera) 举例说明了足够的信息来帮助您入门和运行。对于初学者来说是一个极好的资源！
- [Stopping a Jeep Cherokee on the Highway Remotely](https://www.wired.com/2015/07/hackers-remotely-kill-jeep-highway/) - Chris Valasek 和 Charlie Miller 在 2015 年 DEFCON 上发表了有关吉普车黑客攻击的关键研究。
- [Troy Hunt on Controlling Nissans](https://www.troyhunt.com/controlling-vehicle-features-of-nissan/) - 特洛伊·亨特开始控制日产汽车。
- [Tesla hackers explain how they did it at Defcon](http://www.cnet.com/roadshow/news/tesla-hackers-explain-how-they-did-it-at-def-con-23/) - DEFCON 23 有关黑客入侵特斯拉汽车的演示概述。
- [Anatomy of the Rolljam Wireless Car Hack](http://makezine.com/2015/08/11/anatomy-of-the-rolljam-wireless-car-hack/) - RollJam 滚动代码利用设备概述。
- [IOActive's Tools and Data](http://blog.ioactive.com/2013/08/car-hacking-content.html) - Chris Valasek 和 Charlie Miller 发布了一些用于入侵车辆的工具和数据，以吸引更多人参与车辆安全研究。
- [Developments in Car Hacking](https://www.sans.org/reading-room/whitepapers/ICS/developments-car-hacking-36607) - 通过 SANS 阅览室，Currie 的论文分析了智能汽车技术的风险和危险。
- [Car Hacking on the Cheap](http://www.ioactive.com/pdfs/IOActive_Car_Hacking_Poories.pdf) - Chris Valasek 和 IOActive 撰写的一份白皮书，内容涉及在您没有大量可用资源时黑客攻击您的汽车。
- [Car Hacking: The definitive source](http://illmatics.com/carhacking.html) - Charlie Miller 和 Chris Valasek 免费为所有人发布所有工具、数据、研究笔记和论文
- [Car Hacking on the cheap](https://community.rapid7.com/community/transpo-security/blog/2017/02/08/car-hacking-on-the-cheap) - Craig Smith 撰写了一篇关于使用 ELM327 蓝牙适配器与 Metasploit 的 HWBrige 配合使用的简短文章
- [Researchers tackle autonomous vehicle security](https://phys.org/news/2017-05-tackle-autonomous-vehicle.html) - 德克萨斯农工大学的研究人员开发了智能系统原型。
- [Reverse engineering of the Nitro OBD2](https://blog.quarkslab.com/reverse-engineering-of-the-nitro-obd2.html) - CAN 诊断工具的逆向工程。
- [Analysis of an old Subaru Impreza - Subaru Select Monitor v1 (SSM1)](https://p1kachu.pluggi.fr/project/automotive/2018/12/28/subaru-ssm1/) - 通过旧协议挖掘旧 ECU 并禁用 1997 年斯巴鲁翼豹的限速器。
- [Car Hacking in 30 Minutes or Less](https://brysonpayne.com/2018/10/20/start-car-hacking-in-30-minutes-or-less/) - 使用 VirtualBox 和 Kali Linux，您可以使用完全免费的开源软件和工具（包括 can-utils、ICSim、ScanTool、Wireshark 和 tcpdump）开始汽车黑客攻击

## 演讲

- ["Hopping on the CAN Bus" from BlackHat Asia 2015](https://www.blackhat.com/asia-15/briefings.html#hopping-on-the-can-bus) - BlackHat Asia 2015 的一次演讲旨在让观众“了解汽车系统，同时也拥有攻击它们的工具”。
- ["Drive It Like You Hacked It" from DEFCON 23](https://samy.pl/defcon2015/) - Samy Kamkar 的 DEFCON 23/2015 演讲中的演讲和幻灯片包括黑客车库、利用汽车移动应用程序以及破解滚动代码以使用低成本工具解锁任何车辆。
- [Samy Kamkar on Hacking Vehicles with OnStar](https://www.youtube.com/watch?v=3olXUbS-prU&feature=youtu.be) - Samy Kamkar 是 MySpace 上 Samy 蠕虫病毒背后的多产黑客，他探索如何侵入装有 OnStar 系统的车辆。
- [Remote Exploitation of an Unaltered Passenger Vehicle](https://www.youtube.com/watch?v=OobLb1McxnI) - DEFCON 23 演讲克里斯·瓦拉塞克 (Chris Valasek) 和查理·米勒 (Charlie Miller) 发表了他们现在著名的演讲，内容是远程侵入吉普车并阻止其行驶。
- [Adventures in Automotive Networks and Control Units](https://www.youtube.com/watch?v=n70hIu9lcYo) - Chris Valasek 和 Charlie Miller 在 DEFCON 21 上关于汽车网络的演讲。
- [Can You Trust Autonomous Vehicles?](https://www.youtube.com/watch?v=orWqKWvIW_0) - DEFCON 24 演讲者：Jianhao Liu、Chen Yan、Wenyuan Xu
- [Ken Munro & Dave Lodge - Hacking the Mitsubishi Outlander & IOT](https://www.youtube.com/watch?v=YLBQdO6a5IQ) - [Pen Test Partners] 的 Ken 和 Dave 在 BSides 曼彻斯特 2016 上的演讲(#who-tofollow)
- [FREE-FALL: HACKING TESLA FROM WIRELESS TO CAN BUS](https://www.blackhat.com/docs/us-17/thursday/us-17-Nie-Free-Fall-Hacking-Tesla-From-Wireless-To-CAN-Bus-wp.pdf) - Zeronights 2016 及之后的 BlackHat 演讲，由来自腾讯和 KEEN 安全实验室的 Sen Nie、Ling Liu 和 Yuefeng Du 进行
- [Car Hacking 101](https://www.youtube.com/watch?v=P-mzo2X47sg) - Bugcrowd LevelUp 2017 作者：Alan Mond
- [State of Automotive Cyber Safety, 2015](https://www.youtube.com/watch?v=g-a20ORka-A) - 汽车黑客现状、政策、行业变化等，来自 BSides 拉斯维加斯的《I Am The Cavalry》赛道，2015 年。
- [State of Automotive Cyber Safety, 2016](https://www.youtube.com/watch?v=WcObDVy2-1I) - 汽车黑客现状、政策、行业变化等，摘自 2016 年拉斯维加斯 BSides 的《I Am The Cavalry》赛道。
- [How to Hack a Tesla Model S](https://www.youtube.com/watch?v=KX_0c9R4Fng) - 马克·罗杰斯 (Marc Rogers) 和凯文·马哈菲 (Kevin Mahaffey) 在 DEF CON 23 上发表了关于黑客攻击特斯拉的演讲。 Tesla 联合创始人兼首席技术官 JB Straubel 与他们一起向他们表示感谢，并赠送了一枚挑战币。
- [Car Hacking Videos](http://tekeye.uk/automotive/cyber-security/car-hacking-videos) - 该网页包含一长串与汽车黑客主题相关的在线视频（40 多个）。从 2007 年 DEF CON 关于改装引擎 ECUS 的演讲开始（例如 2017 年 Keen Security Tesla 黑客事件）。
- [Self-Driving and Connected Cars: Fooling Sensors and Tracking Drivers](https://www.youtube.com/watch?v=C29UGFsIWVI) - Jonathan Petit 的黑帽演讲。自动互联车辆是交通运输的下一个发展方向，将提高安全性、交通效率和驾驶体验。本次演讲将分为两个部分：1）自动驾驶车辆的安全性和 2）联网车辆的隐私。 2015年
- [A Survey of Remote Automotive Attack Surfaces](https://www.youtube.com/watch?v=MAGacjNw0Sw) - 查理·米勒 (Charlie Miller) 和克里斯·瓦拉塞克 (Chris Valasek) 的黑帽演讲。汽车安全问题已从边缘走向主流，安全研究人员表明现代车辆容易受到本地和远程攻击。车辆攻击面的讨论。 2014年。
- [Pentesting vehicles with YACHT (Yet Another Car Hacking Tool)](https://www.blackhat.com/docs/eu-16/materials/eu-16-Sintsov-Pen-Testing-Vehicles-With-Cantoolz.pdf) - 该演示讨论了车辆的不同攻击面，然后继续描述了汽车黑客攻击的方法以及分析和收集有用信息所需的工具。
- [How to drift with any car](https://www.youtube.com/watch?v=KU7gl1n1tIs) - CAN 黑客攻击简介以及使用真实汽车作为 Xbox 控制器。
- [Car Infotainment Hacking Methodology and Attack Surface Scenario](https://www.youtube.com/watch?v=F0mYkI2FJ_4) - Jay Turla 编写的有关如何攻击、寻找错误或破解 IVI 的指南，在 DEF CON 26 期间在 Packet Hacking Village/Wall of Sheep 上发布。
- [TR19: Automotive Penetration Testing with Scapy](https://www.youtube.com/watch?v=7D7uNqPWrXw) - 在 2019 年 Troopers Conference 上概述如何使用 Scapy 进行汽车渗透测试。
- [Analysis and Defense of Automotive Networks](https://www.youtube.com/watch?v=a1huGwMjjd4) - BSides Knoxville 2020 上的 CAN、安全性和潜在入侵检测方法概述
- [Remote Exploitation of Honda Cars](https://www.youtube.com/watch?v=y4Uzm-CTa0I&ab_channel=CarHackingVillage) - 第五代 Honda City 使用的 Honda Connect 应用程序在其 API 中使用薄弱的安全机制进行访问控制，这将允许恶意用户通过与其远程信息处理控制单元 (TCU) 交互来远程执行启动汽车、锁定/解锁汽车等操作
- [TR22: UDS Fuzzing and the Path to Game Over](https://www.youtube.com/watch?v=c_DqxHmH7kc) - UDS 诊断协议模糊测试方法是汽车行业众多渗透测试项目的结果，并在 2022 年 Troopers Conference 期间提出了现实世界的利用 PoC。
- [CCC - Horror Stories From the Automotive Industry](https://www.youtube.com/watch?v=rAA-agcNeeg) - 汽车行业常见漏洞的可怕示例，是针对一级供应商和 OEM 进行的 100 多项渗透测试的结果，最终目标是提高人们对当前汽车安全状况的认识。此外，通过在重型车辆中使用电池隔离器和 UDS 协议，自动化周种子随机性利用在汽车零部件中的 PoC 可以完全破坏目标。在 Chaos Communication Camp、DeepSec 2023 和 Troopers Conference 23 中发表。
- [Car Hacking Scene in the PH: How Far We've Come](https://www.youtube.com/watch?v=JaF-_KYQ46A) - Car Hacking Village PH 在 ROOTCON 的主赛道上首次尝试。这是 CHVPH 过去的安全研究到当前研究的概要 - 从黑客信息娱乐系统到 CAN 总线协议，以及菲律宾可用的容易被盗的汽车的摘要。
- [Analysis of an In-vehicular network: From CAN bus to infotainment](https://www.youtube.com/watch?v=4d-uhs2VLCQ) - 本演讲将介绍 Div0 CSQ 的 3 个测试台，他们将探索联网车辆的更多功能。这是在 ROOTCON 17 汽车黑客村中展示的。
- [An overview of Automotive Defensive Engineering](https://www.youtube.com/watch?v=MfTNv9SXd-o) - 本演讲旨在让汽车黑客了解 ECU 和车辆架构中添加的现代防御措施。这是在 ROOTCON 17 汽车黑客村中展示的。
- [Hacking Back Your Car](https://www.youtube.com/watch?v=akMok3Hb-pE) - Kamel Ghali 在 ROOTCON 17 上的演讲，内容涉及攻击者如何看待黑客攻击汽车、此类攻击的起源、这些年来不同国家如何使用这些攻击，并探讨了使此类攻击成为可能的技术细节。
- [TR23: V2GEvil: Ghost in the wires](https://www.youtube.com/watch?v=JVWFfSmIlRY) - 这项研究致力于增强电动汽车的网络安全，特别关注识别电动汽车通信控制器（EVCC）中的漏洞，并介绍工具 V2GEvil。可通过车载充电 (OBC) 端口进行访问，使得这种攻击媒介对于未来车辆的安全非常重要。
- [DEF CON CHV - V2GEvil: Ghost in the wires](https://www.youtube.com/watch?v=Ui2etjRyrUE) - 由 Pavel Khunt 和 Thomas Sermpinis 主持的 DEF CON 32 汽车黑客村演讲《V2GEvil：电线中的幽灵》的缩短和总结版本。
- [The hack, the crash and two smoking barrels. (And all the times I (almost) killed an engineer.)](https://www.youtube.com/watch?v=MDndWJxfP-U) - Thomas Sermpinis 负责任地披露了影响世界上最大的原始设备制造商之一当前 MY 车辆盲点检测传感器的调查结果，导致他被指控该原始设备制造商与敌对国家合作。在 DEF CON 32 的舞台上讲述汽车制造商如何对待安全行业、我们的发展方向以及如何做得更好的故事。

## 书籍

- [2014 Car Hacker's Handbook](https://www.amazon.com/Car-Hackers-Manual-Craig-Smith/dp/0990490106) - 2014 年起黑客攻击车辆的免费指南。
- [2016 Car Hacker's Handbook](https://www.amazon.com/Car-Hackers-Handbook-Penetration-Tester/dp/1593277032) - 最新版本的汽车黑客手册，包含破解您自己的车辆和学习车辆安全的更新信息。如需本书的实体副本以及无限量的 PDF、MOBI 和 EPUB 副本，请在 [No Starch Press](https://www.nostarch.com/carhacking) 购买。各部分可在线获取[此处](https://books.google.com/books?id=Ao_QCwAAQBAJ&lpg=PP1&dq=car%20hacking&pg=PP1#v=onepage&q&f=false)。
- [A Comprehensible Guide to Controller Area Network](https://www.amazon.com/Comprehensible-Guide-Controller-Area-Network/dp/0976511606/ref=pd_sim_14_1?ie=UTF8&dpID=41-D9UhlE9L&dpSrc=sims&preST=_AC_UL160_SR124%2C160_&psc=1&refRID=3FH8N10610H0RX8SMB6K) - 这是一本 2005 年的旧书，但仍然是有关 CAN 总线和车辆网络的综合指南。
- [智能汽车安全攻防大揭秘](https://www.amazon.cn/dp/B075QZXY7W)This book first introduced some basic knowledge of security for automotive R&D personnel, such as encryption and decryption, security authentication, digital signatures, common attack types, and methods. Then it introduced the working principles of some smart cars for security researchers, such as the automotive intranet. Protocol, network architecture, principle of X-By-Wire remote control system, common potential attack surface, etc. Finally, a detailed analysis of some actual automotive attack or security test cases, and defense analysis of the loopholes involved in the case during the analysis process.
- [Controller Area Network Prototyping with Arduino](https://www.amazon.com/Controller-Area-Network-Prototyping-Arduino/dp/1938581164/ref=pd_sim_14_2?ie=UTF8&dpID=51J27ZEcl9L&dpSrc=sims&preST=_AC_UL160_SR123%2C160_&psc=1&refRID=V42FKNW09QGVGHW7ZFRR) - 本书将指导您在 Arduino 上制作 CAN 应用程序原型，这对于在您自己的汽车上使用 CAN 时会有所帮助。
- [Embedded Networking with CAN and CANopen](https://www.amazon.com/Embedded-Networking-CANopen-Olaf-Pfeiffer/dp/0929392787/ref=pd_sim_14_37?ie=UTF8&dpID=41UnLKYFpmL&dpSrc=sims&preST=_AC_UL160_SR122%2C160_&psc=1&refRID=V42FKNW09QGVGHW7ZFRR) - 从 2003 年开始，这本书填补了 CAN 文献的空白，并将进一步指导您了解 CAN 网络和嵌入式系统的使用。
- [Inside Radio: An Attack and Defense Guide](https://www.amazon.com/Inside-Radio-Attack-Defense-Guide/dp/9811084467)这本书讨论了广泛的无线设备和系统中的安全问题，第4章433/315MHz通信（4.3 4.4 4.5是关于车钥匙安全的）

## 研究论文

- [科舍尔等人。现代汽车的实验安全分析，2010](http://www.autosec.org/pubs/cars-oakland2010.pdf)
- [汽车攻击面综合实验分析，2011](http://static.usenix.org/events/sec11/tech/full_papers/Checkoway.pdf)
- [Miller and Valasek](http://illmatics.com/carhacking.html) - 自称“汽车黑客攻击的最终来源”。
  - [汽车网络和控制单元的冒险（又名汽车黑客）](http://illmatics.com/car_hacking.pdf)
  - [穷人的汽车黑客](http://illmatics.com/car_hacking_poories.pdf)
  - [2014 年远程汽车攻击面调查](http://illmatics.com/remote%20attack%20surfaces.pdf)
  - [未经改动的乘用车的远程攻击（又名吉普车黑客），2015 年](http://illmatics.com/Remote%20Car%20Hacking.pdf)
  - [高级 CAN 消息注入，2016](http://illmatics.com/can%20message%20injection.pdf)
- [2015 年五星级汽车网络安全框架](https://iamthecavalry.org/5star)
- [现代汽车标准中的漏洞以及我们如何利用它](https://documents.trendmicro.com/assets/A-Vulnerability-in-Modern-Automotive-Standards-and-How-We-Exploited-It.pdf)
- [汽车黑客实验：当连接遇到漏洞时](http://ieeexplore.ieee.org/abstract/document/7413993/)
- [联网汽车系统的安全问题和漏洞](http://ieeexplore.ieee.org/abstract/document/7223297/)
- [汽车驾驶员指纹识别，2016](http://www.autosec.org/pubs/fingerprint.pdf)
- [基于CAN报文时间间隔分析的车载网络入侵检测系统，2016](https://ieeexplore.ieee.org/document/7427089)
- [对信号间到达时间进行建模，以准确检测 CAN 总线信号注入攻击](https://dl.acm.org/citation.cfm?id=3064816)
- [联网汽车 - 未经授权的访问方式和潜在影响，2018 年](https://www.computest.nl/documents/9/The_Connected_Car._Research_Rapport_Computest_april_2018.pdf)
- [CAN-D：用于全面解码控制器局域网数据的模块化四步管道](https://arxiv.org/pdf/2006.05993.pdf)
- [基于时间的 CAN 入侵检测基准](https://arxiv.org/pdf/2101.05781.pdf)
- [解决 CAN 入侵检测研究中缺乏可比性和测试的问题：CAN IDS 数据综合指南和 ROAD 数据集介绍](https://arxiv.org/pdf/2012.14600.pdf)
- [论车辆针对协议级蓝牙威胁的不安全性](https://hexhive.epfl.ch/publications/files/22WOOT.pdf)
- [Pavel, K. 车载充电安全扫描仪，2024 年](https://dspace.cvut.cz/bitstream/handle/10467/113764/F8-DP-2024-Khunt-Pavel-thesis.pdf)

## 课程

- [Udacity's Self Driving Car Engineer Course](https://github.com/udacity/self-driving-car) - Udacity 自动驾驶汽车软件工程师课程的内容。 Udacity 网站上的实际课程位于[此处](https://www.udacity.com/course/self-driven-car-engineer-nano Degree--nd013)。

## 博客

- [Keen Security Lab Blog](http://keenlab.tencent.com/en/) - 腾讯科恩安全实验室创建的博客，发布有关汽车安全的研究。

## 网站

- [Automotive Security Research Group](https://asrg.io/knowledge/) - 汽车安全研究小组 (ASRG) 是一个非营利性组织，旨在促进汽车产品安全解决方案的开发。
- [OpenGarages](https://github.com/opengarages) - 提供了解当今现代车辆系统所需的公共访问、文档和工具。
- [DEFCON Car Hacking Village](http://www.carhackingvillage.com/) - DEFCON 24 中的汽车黑客练习。
- [canbushack: Hack Your Car](http://www.canbushack.com/blog/index.php) - 车辆黑客方法课程。
- [OWASP Internet of Things Project](https://www.owasp.org/index.php/OWASP_Internet_of_Things_Project#tab=Community) - OWASP 的项目旨在确保从汽车到医疗设备等物联网的安全。
- [I Am The Cavalry](https://www.iamthecavalry.org/) - 全球草根（例如志愿者）倡议重点关注安全与人类生命/公共安全问题的交叉点，例如汽车。来自安全研究人员、原始设备制造商 (OEM)、一级供应商等的参与。发布[汽车五星级网络安全框架](https://iamthecavalry.org/5star)。
- [Carloop Community](https://community.carloop.io/) - 对汽车黑客攻击和将车辆连接到云感兴趣的人们的社区。
- [Python Security](http://www.pythoncarsecurity.com/) - 一个用于浏览和购买具有某些车辆安全功能的集成 python 的汽车的网站。
- [NIST Automotive Cybersecurity Community of Interest](https://csrc.nist.gov/Projects/auto-cybersecurity-coi) - NIST 是 NVD CVE 数据库和现代加密标准背后的组织，运营着一个汽车网络安全利益社区小组，旨在“为 NIST 提供一种促进讨论并接收来自汽车行业、学术界和政府的评论和反馈的方式”。

## 时事通讯

[欢迎贡献](https://github.com/jaredmichaelsmith/awesome-vehicle-security/blob/master/contributing.md)！


## 会议

- [美国汽车网络安全峰会](http://www.automotivecybersecurity.com/) [欧洲汽车网络安全峰会](https://automotive-cyber-security.iqpc.de/) - 致力于汽车网络安全的系列会议，涉及许多 OEM、一级供应商、学者、顾问等。
- [escar conference](https://www.escar.info/) - 汽车中的嵌入式安全。欧洲赛事已经举办了 10 多年，现在还有美国和亚洲赛事。
- [IT Security for Vehicles](https://www.vdi-wissensforum.de/en/event/it-security-for-vehicles/) - 会议由德国工程师协会 (VDI) 主办，美国和欧洲 OEM、一级供应商等参加。
- [Cyber Truck Challenge](https://www.cybertruckchallenge.org/) - 会议重点关注重型车辆网络安全问题。包括重型车辆和子系统的实际评估。


## 关注谁

- Chris Valasek：[UberATC] 的安全主管(#companies-and-jobs)
    - [Twitter](https://twitter.com/nudehaberdasher)
    - [Website](http://chris.illmatics.com/about.html)
- Charlie Miller：黑掉了第一部苹果 iPhone，现在负责汽车安全。
    - [Twitter](https://twitter.com/0xcharlie)
- Samy Kamkar：创建了 MySpace Worm、RollJam、OwnStar。
    - [Twitter](https://twitter.com/samykamkar)
    - [Website](https://samy.pl)
- Justin Seitz：《Black Hat Python》（No Starch Press）的作者。
    - [Twitter](https://twitter.com/jms_dot_py)
- Troy Hunt：Pluralsight 作者。 Microsoft 区域总监和开发人员安全 MVP。 [haveibeenpwned](https://haveibeenpwned.com/) 的创建者。
    - [Twitter](https://twitter.com/troyhunt)
    - [Website](https://www.troyhunt.com/)
- Ken Munro：英国研究员，在 Pen Test Partners 工作；对车辆安全的主要兴趣
    - [Twitter](https://twitter.com/TheKenMunroShow)
- OpenGarages：倡议在世界各地创建车辆研究实验室。
    - [Twitter](https://twitter.com/opengarages)
    - [Website](http://opengarages.org/index.php/Main_Page)
- Hackaday：黑客协作项目托管 - 这里经常有汽车项目。
    - [Twitter](https://twitter.com/hackaday)
- Pen Test Partners：英国渗透测试公司；一些帖子涉及他们披露的汽车安全漏洞
    - [Twitter](https://twitter.com/pentestpartners)
    - [Website](https://www.pentestpartners.com/blog)
- 我是骑兵：全球草根（例如志愿者）倡议，重点关注安全和人类生命/公共安全问题的交叉点，例如汽车。
    - [Twitter](https://twitter.com/iamthecavalry)
    - [Website](https://iamthecavalry.org)
    - [讨论组](https://groups.google.com/forum/#!forum/iamthecavalry)
- 汽车黑客村
    - [Twitter](https://twitter.com/CarHackVillage)
    - [Website](https://www.carhackingvillage.com/)
- carfucar：汽车黑客村创始人兼演讲者或培训师
    - [Twitter](https://twitter.com/CarHackVillage)
- Ian Tabor / mintynet：汽车黑客、汽车黑客村工作人员
    - [Twitter](https://twitter.com/mintynet)
    - [Website](https://www.mintynet.com/)    
- Daniel Öster：Dala 的电动汽车维修、电动汽车 CAN 黑客/升级
    - [Youtube](https://www.youtube.com/channel/UCc3g-KhOBoicgOrB4KkMeew)
    - [Website](https://dalasevrepair.fi/)

## 播客和剧集

播客和播客剧集，要么直接关注车辆安全，要么有一些剧集。

### 播客
- [Security Weekly](http://securityweekly.com/) - 优秀的播客涵盖了所有安全领域，其中一些剧集重点关注从汽车到无人机的车辆安全。
- [TrustedSec Podcast](https://podcasts.apple.com/us/podcast/security-noise/id1428851782) - 来自社会工程领域的领导者 TrustedSec 的人们，他们的事件经常涉及最近的车辆漏洞和漏洞利用。
- [SANS Internet Storm Center](https://isc.sans.edu/) - ISC 定期举办播客，介绍最新的漏洞和安全新闻。
- [Security Ledger](https://soundcloud.com/securityledger) - 一个播客，重点采访安全专家，了解与安全相关的主题。

### 剧集数
- [Car Hacking with Craig Smith](http://softwareengineeringdaily.com/2015/09/02/car-hacking-with-craig-smith/) - 《软件工程日报》与《汽车黑客手册》（上图）的作者克雷格·史密斯一起制作了一期精彩的节目，讲述了黑客入侵车辆的问题。
- [Big Bugs Podcast Episode 1: Auto Bugs - Critical Vulns found in Cars with Jason Haddix](https://blog.bugcrowd.com/big-bugs-podcast-episode-1) - Jason Haddix 探讨了汽车中发现的主要漏洞。
- [Hacking Under the Hood and Into Your Car](http://www.npr.org/2013/08/02/208270026/hacking-under-the-hood-and-into-your-car) - 克里斯·瓦拉塞克 (Chris Valasek) 和查理·米勒 (Charlie Miller) 与 NPR 讨论了他们如何侵入车辆。
- [Hacking Connected Vehicles with Chris Valasek of IOActive](https://soundcloud.com/securityledger/chris-valasek-of-ioactive) - 克里斯·瓦拉塞克 (Chris Valasek) 谈论入侵联网车辆。

## 杂项
- [逆向工程资源](https://github.com/ps1337/automotive-security-research)
- [真实 ORNL 汽车测功机 (ROAD) CAN 入侵数据集](https://0xsam.com/road/)
- [CAN DoS 模糊攻击视频](https://www.youtube.com/shorts/80A5IhvwsJU)
- [ECU 刷新检测器演示](https://www.youtube.com/watch?v=HPpGzwWQY5Y)

# 项目

- [Open Vehicle Monitoring System](https://github.com/openvehicles/Open-Vehicle-Monitoring-System) - 一个社区项目，为您的汽车构建硬件模块、与之通信的服务器以及与服务器通信的移动应用程序，以便开发人员和爱好者能够为他们的汽车添加更多功能并远程控制它。
- [Open Source Car Control Project](https://github.com/PolySync/OSCC) - 开源汽车控制项目是一个硬件和软件项目，详细介绍了将新型车辆转换为自动驾驶研发车辆的过程。
- [Uptane](https://uptane.github.io/overview.html) - Uptane 是一种开放且安全的软件更新系统设计，可保护通过无线方式传输到汽车计算机化单元的软件，并且即使面对国家攻击者的最大努力也能保持弹性。

# 硬件

进行车辆安全研究时可以使用的硬件概述（开源和专有）。 [本文](http://makezine.com/2016/04/08/car-hacking-tools-trade/) 介绍了以下许多选项。

- [Arduino](https://www.arduino.cc/) - Arduino 板有许多扩展板，您可以连接到支持 CAN 的设备。
    - [CANdiy-Shield](https://github.com/watterott/CANdiy-Shield)
    - [适用于 Arduino 的 DFRobot CAN-BUS 扩展板](http://www.dfrobot.com/index.php?route=product/product&product_id=1444)
    - [SparkFun CAN-BUS 扩展板](https://www.sparkfun.com/products/13262)
    - [arduino-canbus-monitor](https://github.com/latonita/arduino-canbus-monitor) - 无论选择哪种防护罩，您都需要自己的嗅探器。这是标准 Lawicel/SLCAN 协议的实现，适用于 Arduino + 任何 MCP CAN Shield，可与许多标准 CAN 总线分析软件包或 SocketCAN 一起使用
- [CANtact](https://cantact.io/cantact/users-guide.html) - “开源汽车工具”旨在帮助您破解您的汽车。您可以购买一个或按照此处的指南自行制作。
- [Freematics OBD-II Telematics Kit](http://freematics.com/pages/products/arduino-telematics-kit-3/) - 基于 Arduino 的 OBD-II 蓝牙适配器套件包含 OBD-II 设备和数据记录器，并配有 GPS、加速度计和陀螺仪以及温度传感器。
- [ELM327](https://www.elmelectronics.com/obdic.html) - 事实上的芯片组非常便宜，可用于连接 CAN 设备。
- [GoodThopter12](http://goodfet.sourceforge.net/hardware/goodthopter12/) - 该板由知名硬件黑客打造，是一款可用于探索汽车网络的通用板。
- [USB2CAN](http://www.8devices.com/products/usb2can/) - 廉价的 USB 转 CAN 连接器，将在 Linux 上注册一个设备，您可以使用该设备从 CAN 网络获取数据。
- [Rinho Telematics](https://rinho.com.ar/en) - 具有本机 CAN 总线 (J1939/FMS)、用于离线数据下载的 WiFi 回退以及 BLE 5.0 传感器的 GPS 跟踪器。与 Traccar 和 Wialon 兼容。
- [Intrepid Tools](http://store.intrepidcs.com/) - 昂贵但用途极其广泛的工具，专为反转 CAN 和其他车辆通信协议而设计。
- [Red Pitaya](http://redpitaya.com/) - 取代示波器、信号发生器和频谱分析仪等昂贵的测量工具。 Red Pitaya 具有 LabView 和 Matlab 界面，您可以为其编写自己的工具和应用程序。它甚至支持 Arduino 扩展板等扩展。
- [ChipWhisperer](http://newae.com/tools/chipwhisperer/) - 用于侧信道攻击的系统，例如功率分析和时钟故障。
- [HackerSDR](https://greatscottgadgets.com/hackrf/) - 一种软件定义无线电外设，能够传输或接收 1 MHz 至 6 GHz 的无线电信号。旨在支持现代和下一代无线电技术的测试和开发。
- [Carloop](https://www.carloop.io/) - 开源开发套件可让您轻松将汽车连接到互联网。成本最低的汽车黑客工具，与 SocketCAN 和 can-utils 兼容。  无需 OBD-II 转串行电缆。
- [CANBadger](https://gutenshit.github.io/CANBadger/) - 用于逆向工程和测试汽车系统的工具。 CANBadger 由硬件和软件组成。主接口是安装在定制 PCB 上的 LPC1768/LPC1769 处理器，提供两个 CAN 接口、SD 卡、闪烁 LED、一些 GPIO 引脚、外设电源和以太网端口。
- [CANSPY](https://bitbucket.org/jcdemay/canspy) - 为安全审核员提供审核 CAN 设备的平台。它可用于自主地以及交互地实时阻止、转发或修改 CAN 帧。
- [CANBus Triple](https://canb.us/) - 通用控制器局域网瑞士军刀和开发平台。
- [USBtin](http://www.fischl.de/usbtin/) - USBtin 是一个简单的 USB 转 CAN 接口。它可以监控CAN总线并传输CAN消息。 USBtin 实现 USB CDC 类并在主机上创建虚拟端口。
- [OpenXC](http://openxcplatform.com/hardware.html) - OpenXC 是开源硬件和软件的组合，可让您通过自定义应用程序和可插拔模块扩展您的车辆。它使用标准的、众所周知的工具向开发人员开放车辆中的大量数据。它由福特研究人员发起，适用于所有 2002 年及更新的 MY 车辆（标准 OBD-II 接口）。福特汽车公司的研究人员联手创建了一种创建车辆售后软件和硬件的标准方法。
- [Macchina M2](https://www.macchina.cc/m2-introduction) - Macchina 2.0 是对 1.X 代 Macchina 的彻底革新。目标仍然是一样的：创建一个易于使用、完全开放、超级兼容的汽车接口。
- [PandwaRF](https://pandwarf.com/) - PandwaRF 是一款口袋大小的便携式射频分析工具，工作频率低于 1 GHz。它允许通过 Android 设备或 Linux PC 捕获、分析和重新传输 RF。从 300-928 MHz 频段捕获 ASK/OOK/MSK/2-FSK/GFSK 调制中的任何数据。
- [CAN MITM Bridge by MUXSCAN](https://www.tindie.com/products/muxsan/can-mitm-bridge-3-port-rev-25/) - MITM CAN 消息的工具，可轻松与您的汽车交互。
- [PiCCANTE](https://github.com/Alia5/PiCCANTE) - 基于 Raspberry Pi Pico 的开源 CAN 黑客工具 [2] (W) - 多达 3 个 CAN 接口，包括 ELM327 仿真器。
- [AutoPi](https://github.com/autopi-io/autopi-core) - AutoPi 加密狗的开源核心软件，这是一种基于 Raspberry Pi 的 OBD-II 设备，用于车辆远程信息处理、CAN 总线数据收集和汽车物联网应用。

# 软件

软件概述，包括开源软件和专有软件，以及各种编程语言的库。 [本文](http://makezine.com/2016/04/08/car-hacking-tools-trade/) 介绍了以下许多选项。

## 应用领域

软件应用程序将帮助您破解您的汽车、调查其信号以及对其进行一般修补。

- [Wireshark](https://www.wireshark.org/) - WireShark 可用于反向 CAN 通信。
- [Kayak](http://kayak.2codeornot2code.org/) - 用于 CAN 总线诊断和监控的 Java 应用程序。
- [UDSim](https://github.com/zombieCraig/UDSim/) - GUI 工具可以监控 CAN 总线并通过观察通信自动了解连接到其上的设备。
- [RomRaider](http://www.romraider.com/) - 适用于斯巴鲁发动机控制单元的开源调整套件，可让您查看和记录数据并调整 ECU。
- [Intrepid Tools](http://store.intrepidcs.com/) - 昂贵但用途极其广泛的工具，专为反转 CAN 和其他车辆通信协议而设计。
- [O2OO](http://web.archive.org/web/20201108091723/https://www.vanheusden.com/O2OO/) - 与 ELM327 配合使用，将数据记录到 SQLite 数据库中以用于绘图。它还支持读取GPS数据。您可以将其连接到您的汽车，并使用您驾驶地点的 Google 地图 KML 数据绘制地图。
- [CANToolz](https://github.com/eik00d/CANToolz) - CANToolz 是一个用于分析 CAN 网络和设备的框架。它基于可以组装在管道中的多个模块。
- [BUSMASTER](https://rbei-etas.github.io/busmaster/) - 用于模拟、分析和测试 CAN、LIN、FlexRay 等数据总线系统的开源工具。
- [BlackFlag ECU](https://github.com/bad-antics/blackflag-ecu) - 专业 ECU 诊断和调整套件，具有 OBD-II 扫描、DTC 读取、实时传感器监控和刷新功能。
- [OpenXC](http://openxcplatform.com/getting-started/index.html) - 目前，OpenXC 可与“Python”和“Android”配合使用，并提供了入门库。
- [openpilot](https://github.com/commaai/openpilot) - openpilot 是一个开源驾驶代理，可为本田和讴歌执行自适应巡航控制 (ACC) 和车道保持辅助系统 (LKAS) 的功能。
- [openalpr](https://github.com/openalpr/openalpr) - 一个用 C++ 编写的开源自动车牌识别库，绑定了 C#、Java、Node.js、Go 和 Python。
- [metasploit](https://community.rapid7.com/community/transpo-security/blog/2017/02/02/exiting-the-matrix) - 流行的metasploit框架现在支持硬件桥会话，将框架的功能扩展到硬件设备，例如socketcan和SDR无线电。
- [Mazda AIO Tweaks](https://mazdatweaks.com/) - 适用于许多可用的马自达 MZD 信息娱乐系统调整的一体化安装程序/卸载程序。
- [mazda_getInfo](https://github.com/shipcod3/mazda_getInfo) - PoC 表明 USB 端口是马自达汽车信息娱乐系统的攻击面，以及马自达黑客是如何进行的（CMU 中的已知错误）。
- [talking-with-cars](https://github.com/P1kachu/talking-with-cars) - CAN相关脚本，以及将汽车用作游戏手柄的脚本
- [CANalyzat0r](https://github.com/schutzwerk/CANalyzat0r) - 用于专有汽车协议的安全分析工具包。
- [Tesla Mod](https://github.com/hypery11/flipper-tesla-fsd) - 适用于 Flipper Zero 和 ESP32 的 Tesla CAN 总线工具包。 Nag Killer、FSD 区域解锁、跟踪模式、BMS 仪表板、盲点警报、远光灯频闪以及 30 多个 CAN 处理程序。开源（GPL-3.0）。

## 库和工具

不属于上述较大类别的应用程序的库和工具。

[Mazda Connect 信息娱乐系统的自定义应用程序 SDK](https://github.com/flyandi/mazda-custom-application-sdk) - 一个微型框架，允许您为 Mazda 信息娱乐系统编写和部署自定义应用程序。

### C

- [SocketCAN Utils](https://github.com/linux-can/can-utils) - Linux 上 SocketCAN 的用户空间实用程序。
- [vircar](https://github.com/dn5/vircar) - 基于 SocketCAN 发送 CAN 消息的虚拟汽车用户空间
- [dbcc](https://github.com/howerj/dbcc) - “dbcc 是一个程序，主要用于将 DBC 文件转换为可以序列化和反序列化 CAN 消息的 C 代码。”对于车辆中的现有 DBC 文件，此文件允许您将它们转换为 C 代码，以提取 CAN 消息和 CAN 环境的属性。

### C++

- [High Level ViWi Service](https://github.com/iotbzh/high-level-viwi-service) - 高层大众 CAN 信号协议实施。
- [CanCat](https://github.com/atlas0fd00m/CanCat) - 用于与实时 CAN 数据交互的“瑞士军刀”。主要 API 接口使用 Python，但使用 C++ 编写。
- [CANdevStudio](https://github.com/GENIVI/CANdevStudio) - CAN总线仿真开发工具。 CANdevStudio 能够让每个汽车开发人员模拟 CAN 信号，例如点火状态、车门状态或倒档。
- [UnlockECU](https://github.com/jglim/UnlockECU) - 免费、开源 ECU 种子密钥解锁工具。

### 爪哇
- [ITS Geonetworking](https://github.com/alexvoronov/geonetworking) - ETSI ITS G5 GeoNetworking 堆栈，Java 版本：CAM-DENM / ASN.1 PER / BTP / GeoNetworking

### 蟒蛇

- [CANard](https://github.com/ericevenchick/canard) - 用于控制器局域网应用程序的 Python 框架。
- [Caring Caribou](https://github.com/CaringCaribou/caringcaribou/) - 旨在成为*车辆安全地图*。
- [c0f](https://github.com/zombieCraig/c0f/) - 一种用于 CAN 通信的指纹识别工具，可用于在测试与车辆的交互时查找 CAN 网络上的特定信号。
- [Python-CAN](https://github.com/hardbyte/python-can) - 各种 CAN 实现的 Python 接口，包括 SocketCAN。允许您使用 Python 2.7.x 或 3.3.x+ 通过 CAN 网络进行通信。
- [Python-OBD](https://github.com/brendan-w/python-OBD) - 用于处理来自 OBD-II 车辆端口的实时传感器数据的 Python 模块。与 ELM327 OBD-II 适配器配合使用，适用于 Raspberry Pi。
- [CanCat](https://github.com/atlas0fd00m/CanCat) - 用于与实时 CAN 数据交互的“瑞士军刀”。主要 API 接口使用 Python，但使用 C++ 编写。
- [Scapy](https://github.com/secdev/scapy) - 用于发送、接收、编辑原始数据包的 python 库。支持 CAN 和汽车协议：请参阅[汽车文档](https://scapy.readthedocs.io/en/latest/layers/automotive.html)
- [CanoPy](https://github.com/tbruno25/canopy) - 用于实时可视化和绘制消息有效负载的 python gui。
- [canTot](https://github.com/shipcod3/canTot) - 基于 sploitkit 的基于 python 的 cli 框架，易于使用，因为它类似于使用 Metasploit。这类似于漏洞利用框架，但专注于已知的 CAN 总线漏洞或有趣的 CAN 总线黑客攻击。
- [SocketCAN](https://python-can.readthedocs.io/en/master/interfaces/socketcan.html) SocketCAN 的 Python 接口
- [canmatrix](https://github.com/ebroecker/canmatrix) 用于处理 CAN 矩阵文件的 Python 模块
- [Jumpstarter](https://github.com/jumpstarter-dev/jumpstarter) - 硬件在环测试框架，具有适用于 UDS、DoIP 和 CAN 总线协议的汽车诊断驱动程序。
- [canopen](https://canopen.readthedocs.io/en/latest/) Python 模块与 CANopen 设备通信
- [cantools](https://github.com/eerimoq/cantools) 使用 DBC 文件解码和编码 CAN 消息的 Python 模块
- [Caring Caribou Next](https://github.com/Cr0wTom/caringcaribounext) - 原Caring Caribou项目的升级优化版本。
- [canarchy](https://github.com/hexsecs/canarchy) - CANarchy 是一个流优先的 CAN 分析和操作运行时，专为自动化、安全研究和代理驱动的工作流程而设计。


### 去

- [CANNiBUS](https://github.com/Hive13/CANiBUS/) - Go 服务器允许一屋子的研究人员同时在同一辆车上工作，无论是出于教学目的还是团队倒车会议。
- [CAN Simulator](https://github.com/carloop/simulator-program) - 用于 Raspberry Pi 的基于 Go 的 CAN 模拟器，可与 PiCAN2 或开源 [CAN Simulator board](https://github.com/carloop/simulator) 一起使用

### JavaScript

- [NodeJS extension to SocketCAN](https://github.com/sebi2k1/node-can) - 允许您使用简单的 JavaScript 函数通过 CAN 网络进行通信。

# 公司和职位

车辆安全领域的公司和就业机会。

- [UberATC](https://www.uber.com/us/en/autonomous/) - Uber 先进技术中心，现为 Uber AV - <info@uberatc.com>。
- [Tesla](https://www.tesla.com/careers/search#/filter/?keyword=security&department=1) - 特斯拉聘请安全专业人员担任各种职务，特别是保护车辆的安全。
- [Intrepid Control Systems](https://www.intrepidcs.com/jobs/) - 嵌入式安全公司构建倒车工具。
- [Rapid7](https://www.rapid7.com/company/careers.jsp) - Rapid7 致力于信息、计算机和嵌入式安全领域。
- [IOActive](http://www.ioactive.com/) - 从事渗透测试硬件和嵌入式系统的安全咨询公司。
- [Cohda Wireless](https://cohdawireless.com/) - V2X DSRC 无线电和软件
- [VicOne](https://www.vicone.com/) - 趋势科技旗下专注于汽车安全的子公司

## 协调披露

- HackerOne 上的 [通用汽车](https://hackerone.com/gm) - 接受协调披露提交
- Bugcrowd 上的 [Stellantis](https://bugcrowd.com/stellantis) - 接受协调披露提交，提供付费赏金
- Bugcrowd 上的 [特斯拉汽车](https://bugcrowd.com/tesla) - 接受协调披露提交，提供付费赏金
- [ASRG](https://asrg.io/disclosure/) - ASRG 披露流程旨在在无法与责任公司直接沟通或未做出回应时支持负责任的披露。
- [Zeekr](https://security.zeekrlife.com/vulnerability) - Zeekr 和吉利责任披露计划


# 其他很棒的列表

列表的列表。

- 安全
  - [应用安全](https://github.com/paragonie/awesome-appsec)
  - [Security](https://github.com/sbilly/awesome-security)
  - [夺旗](https://github.com/apsdehal/awesome-ctf)
  - [恶意软件分析](https://github.com/rshipp/awesome-malware-analysis)
  - [安卓安全](https://github.com/ashishb/android-security-awesome)
  - [Hacking](https://github.com/carpedm20/awesome-hacking)
  - [Honeypots](https://github.com/paralax/awesome-honeypots)
  - [事件响应](https://github.com/meirwah/awesome-incident-response)
- 元
  - [awesome](https://github.com/sindresorhus/awesome)
  - [lists](https://github.com/jnv/lists)

# 贡献

随时欢迎您的贡献！请先查看[贡献指南](https://github.com/jaredmichaelsmith/awesome-vehicle-security/blob/master/contributing.md)。
