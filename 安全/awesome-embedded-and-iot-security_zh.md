<!--lint ignore awesome-license-->
<div align="center">
	<img width="500" height="350" src="iot_awesome_logo.svg" alt="Awesome">
  <br />
</div>

# 出色的嵌入式和物联网安全性 [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> 有关嵌入式和物联网安全的精彩资源的精选列表。该列表包含软件和硬件工具、书籍、研究论文等。

像 Mirai 这样的僵尸网络已经证明嵌入式和物联网设备需要更高的安全性。该列表将帮助初学者和专家找到有关该主题的有用资源。
如果您是初学者，您应该查看<ins>_Books_</ins>和<ins>_Case Studies_</ins>部分。
如果您想立即开始自己的分析，您应该尝试<ins>_分析框架_</ins>。
它们易于使用，您无需成为专家即可获得第一个有意义的结果。

> 标有：欧元：的商品为商业产品。

## 内容

- [软件工具](#software-tools)
  - [分析框架](#analysis-frameworks)
  - [分析工具](#analysis-tools)
  - [提取工具](#extraction-tools)
  - [支持工具](#support-tools)
  - [其他工具](#misc-tools)
- [五金工具](#hardware-tools)
  - [蓝牙 BLE 工具](#bluetooth-ble-tools)
  - [ZigBee 工具](#zigbee-tools)
  - [特别提款权工具](#sdr-tools)
  - [RFID NFC 工具](#rfid-nfc-tools)
- [Books](#books)
- [研究论文](#research-papers)
- [案例研究](#case-studies)
- [免费培训](#free-training)
- [Websites](#websites)
  - [Blogs](#blogs)
  - [教程和技术背景](#tutorials-and-technical-background)
  - [YouTube 频道](#youtube-channels)
- [Conferences](#conferences)
- [Contribute](#contribute)
- [License](#license)

## 软件工具

用于分析嵌入式/物联网设备和固件的软件工具。

### 分析框架

- [EXPLIoT](https://gitlab.com/expliot_framework/expliot) - Pentest 框架类似于 Metasploit，但专门用于物联网。
- [FACT - The Firmware Analysis and Comparison Tool](https://fkie-cad.github.io/FACT_core/) - 全功能静态分析框架，包括固件提取、利用不同插件进行分析以及不同固件版本的比较。
  - [Improving your firmware security analysis process with FACT](https://passthesalt.ubicast.tv/videos/improving-your-firmware-security-analysis-process-with-fact/) - 会议谈论事实：电视：。
- [FwAnalyzer](https://github.com/cruise-automation/fwanalyzer) - 根据定制规则分析固件的安全性。旨在作为 DevSecOps 中的附加步骤，类似于 CI。
- [HAL – The Hardware Analyzer](https://github.com/emsec/hal) - 用于门级网表的全面逆向工程和操作框架。
- [HomePWN](https://github.com/ElevenPaths/HomePWN) - 用于物联网设备渗透测试的瑞士军刀。
- [IoTSecFuzz](https://gitlab.com/invuls/iot-projects/iotsecfuzz) - 物联网层安全分析自动化框架：硬件、软件和通信。
- [Killerbee](https://github.com/riverloopsec/killerbee) - 用于测试和审核 ZigBee 和 IEEE 802.15.4 网络的框架。
- [PRET](https://github.com/RUB-NDS/PRET) - 打印机利用工具包。
- [Routersploit](https://github.com/threat9/routersploit) - 专用于利用嵌入式设备的框架。

### 分析工具

- [Binwalk](https://github.com/ReFirmLabs/binwalk) - 在二进制文件中搜索“有趣”的内容，并提取任意文件。
- [cwe\_checker](https://github.com/fkie-cad/cwe_checker) - 查找二进制可执行文件中的易受攻击模式 - 对 x86、ARM 和 MIPS 的 ELF 支持、实验性裸机支持。
- [emba](https://github.com/e-m-b-a/emba) - 分析基于 Linux 的嵌入式设备固件。
- [Firmadyne](https://github.com/firmadyne/firmadyne) - 尝试模拟和渗透测试固件。
- [Firmwalker](https://github.com/craigz28/firmwalker) - 搜索提取的固件映像以查找有趣的文件和信息。
- [Firmware Slap](https://github.com/ChrisTheCoolHut/Firmware_Slap) - 通过一致性分析和功能聚类发现固件中的漏洞。
- [Ghidra](https://ghidra-sre.org/) - 软件逆向工程套件；如果您提供 CPU 架构和二进制文件的字节顺序，则可以处理任意二进制文件。
- [Radare2](https://github.com/radare/radare2) - 软件逆向工程框架还可以处理流行的格式和任意二进制文件，并具有广泛的命令行工具集。
- [Trommel](https://github.com/CERTCC/trommel) - 搜索提取的固件映像以查找有趣的文件和信息。

### 提取工具

- [FACT Extractor](https://github.com/fkie-cad/fact_extractor) - 自动检测容器格式并执行相应的提取工具。
- [Firmware Mod Kit](https://github.com/rampageX/firmware-mod-kit/wiki) - 适用于多种容器格式的提取工具。
- [The SRecord package](http://srecord.sourceforge.net/) - 用于操作 EPROM 文件的工具集合（可以转换大量二进制格式）。

### 支持工具

- [JTAGenum](https://github.com/cyphunk/JTAGenum) - 向 Arduino 添加 JTAG 功能。
- [OpenOCD](http://openocd.org/) - 免费和开放的片上调试、在系统编程和边界扫描测试。

### 其他工具

- [Cotopaxi](https://github.com/Samsung/cotopaxi) - 使用特定网络物联网协议对物联网设备进行安全测试的工具集。
- [dumpflash](https://github.com/ohjeongwook/dumpflash) - 低级 NAND 闪存转储和解析实用程序。
- [flashrom](https://github.com/flashrom/flashrom) - 用于检测、读取、写入、验证和擦除闪存芯片的工具。
- [Samsung Firmware Magic](https://github.com/chrivers/samsung-firmware-magic) - 解密三星SSD固件更新。

## 五金工具

- [Bus Blaster](http://dangerousprototypes.com/docs/Bus_Blaster) - 检测硬件调试端口并与之交互，例如 [UART](https://en.wikipedia.org/wiki/Universal_asynchronous_receiver-transmitter) 和 [JTAG](https://en.wikipedia.org/wiki/JTAG)。
- [Bus Pirate](http://dangerousprototypes.com/docs/Bus_Pirate) - 检测 UART 和 JTAG 等硬件调试端口并与之交互。
- [Shikra](https://int3.cc/products/the-shikra) - 检测 UART 和 JTAG 等硬件调试端口并与之交互。除其他协议外。
- [JTAGULATOR](http://www.grandideastudio.com/jtagulator/) - 快速检测 JTAG 引脚排列。
- [Saleae](https://www.saleae.com/) - 易于使用的逻辑分析仪，支持多种协议：欧元：。
- [Ikalogic](https://www.ikalogic.com/pages/logic-analyzer-sp-series-sp209) - Saleae 逻辑分析仪的替代品：欧元：。
- [HydraBus](https://hydrabus.com/hydrabus-1-0-specifications/) - 与 BusPirate 类似的开源多功能工具硬件，但具有 NFC 功能。
- [ChipWhisperer](https://newae.com/chipwhisperer/) - 检测毛刺/旁道攻击。
- [Glasgow](https://github.com/GlasgowEmbedded/Glasgow) - 用于探索和调试不同数字接口的工具。
- [J-Link](https://www.segger.com/products/debug-probes/j-link/models/model-overview/) - J-Link 为多个不同的 CPU 内核提供 USB 供电的 JTAG 调试探针：euro：。

### 蓝牙 BLE 工具

- [UberTooth One](https://greatscottgadgets.com/ubertoothone/) - 适用于蓝牙实验的开源 2.4 GHz 无线开发平台。
- [Bluefruit LE Sniffer](https://www.adafruit.com/product/2269) - 易于使用的蓝牙低功耗嗅探器。

### ZigBee 工具

- [ApiMote](http://apimote.com) - ZigBee 安全研究硬件，用于了解和评估 IEEE 802.15.4/ZigBee 系统的安全性。杀人蜂兼容。
- Atmel RZUSBstick - 停产产品。如果你有的话就很幸运了！ - 用于开发、调试和演示各种低功耗无线应用（包括 IEEE 802.15.4、6LoWPAN 和 ZigBee 网络）的工具。杀人蜂兼容。
- [Freakduino](https://freaklabsstore.com/index.php?main_page=product_info&cPath=22&products_id=219&zenid=fpmu2kuuk4abjf6aurt3bjnfk4) - 低成本电池供电无线 Arduino 板，可转变为 IEEE 802.15.4 协议嗅探器。

### 特别提款权工具

- [RTL-SDR](https://www.rtl-sdr.com/buy-rtl-sdr-dvb-t-dongles/) - 适合初学者的最便宜的 SDR。它是一种基于计算机的无线电扫描仪，用于接收频率从 500 kHz 到 1.75 GHz 的实时无线电信号。
- [HackRF One](https://greatscottgadgets.com/hackrf/) - 软件定义无线电外设能够传输或接收 1 MHz 至 6 GHz（半双工）的无线电信号。
- [YardStick One](https://greatscottgadgets.com/yardstickone/) - 半双工低于 1 GHz 无线收发器。
- [LimeSDR](https://www.crowdsupply.com/lime-micro/limesdr) - 软件定义无线电外设能够传输或接收 100 KHz 至 3.8 GHz（全双工）的无线电信号。
- [BladeRF 2.0](https://www.nuand.com/bladerf-2-0-micro/) - 软件定义无线电外设能够传输或接收 47 MHz 至 6 GHz（全双工）的无线电信号。
- [USRP B Series](https://www.ettus.com/product-categories/usrp-bus-series/) - 软件定义无线电外设能够传输或接收 70 MHz 至 6 GHz（全双工）的无线电信号。

### RFID NFC 工具

- [Proxmark 3 RDV4](https://www.proxmark.com/) - 强大的通用 RFID 工具。从低频 (125kHz) 到高频 (13.56MHz) 标签。
- [ChamaleonMini](http://chameleontiny.com/) - 用于 NFC 安全分析的可编程便携式工具。
- [HydraNFC](https://hydrabus.com/hydranfc-1-0-specifications/) - 强大的 13.56MHz RFID/NFC 平台。读/写/破解/嗅探/模拟。

## 书籍

- 2020 年，Fotios Chantzis、Evangel Deirme、Ioannis Stais、Paulino Calderon、Beau Woods：[实用物联网黑客](https://www.amazon.com/Fotios-Chantzis-ebook/dp/B085BVVSN6/)
- 2020 年，Jasper van Woudenberg、Colin O'Flynn：[硬件黑客手册：通过硬件攻击破坏嵌入式安全](https://nostarch.com/hardwarehacking)
- 2019 年，Yago Hansen：[黑客的硬件工具包：红队黑客、渗透测试人员和安全研究人员的最佳硬件小工具集合](https://github.com/yadox666/The-Hackers-Hardware-Toolkit/blob/master/TheHackersHardwareToolkit.pdf)
- 2019 年，Aditya Gupta：[物联网黑客手册：黑客物联网实用指南](https://www.apress.com/us/book/9781484242995)
- 2018 年，Mark Swarup Tehranipoor：[硬件安全：实践学习方法](https://www.elsevier.com/books/hardware-security/bhunia/978-0-12-812477-2)
- 2018 年，Mark Carney：[渗透测试硬件 - 实用手册（草案）](https://github.com/unprovable/PentestHardware)
- 2018，杨庆，黄林 [广播内幕：攻防指南](https://link.springer.com/book/10.1007/978-981-10-8447-8)
- 2017 年，Aditya Gupta、Aaron Guzman：[物联网渗透测试手册](https://www.packtpub.com/networking-and-servers/iot-penetration-testing-cookbook)
- 2017 年，Andrew Huang：[硬件黑客：制造和破坏硬件的冒险](https://nostarch.com/hardwarehackerpaperback)
- 2016 年，Craig Smith：[汽车黑客手册：渗透测试仪指南](https://nostarch.com/carhacking)
- 2015年，Keng Tiong Ng：[PCB逆向工程的艺术](https://visio-for-engineers.blogspot.com/p/order.html)
- 2015 年，Nitesh Dhanjan：[滥用物联网：停电、异常和监视](https://shop.oreilly.com/product/0636920033547.do)
- 2015 年，Joshua Wright、Johnny Cache：[黑客无线暴露](https://www.mhprofessional.com/9780071827638-usa-hacking-expose-wireless-third-edition-group)
- 2014 年，Debdeep Mukhopadhyay：[硬件安全：设计、威胁和保障](https://www.taylorfrancis.com/books/9780429066900)
- 2014 年，Jack Ganssle：[固件手册（嵌入式技术）](https://www.elsevier.com/books/the-firmware-handbook/ganssle/978-0-7506-7606-9)
- 2013年，Andrew Huang：[黑客XBOX](https://nostarch.com/xboxfree)

## 研究论文

<!--lint ignore match-punctuation-->

- 2020 年，Oser 等人：[SAFER：跨国组织中物联网设备风险评估框架的开发和评估](https://dl.acm.org/doi/abs/10.1145/3414173)
- 2019 年，Agarwal 等人：[检测物联网设备以及它们如何使大型异构网络面临安全风险](https://www.mdpi.com/1424-8220/19/19/4107)
- 2019 年，Almakhdhub 等人：[BenchIoT：物联网安全基准](https://nebelwelt.net/publications/files/19DSN.pdf)
- 2019 年，Alrawi 等人：[SoK：基于家庭的物联网部署的安全评估](https://alrawi.github.io/static/papers/alrawi_sok_sp19.pdf)
- 2019 年，Abbasi 等人：[为深度嵌入式系统设计漏洞缓解措施的挑战](https://ieeexplore.ieee.org/abstract/document/8806725)
- 2019 年，Song 等人：[PeriScope：针对硬件操作系统边界的有效探测和模糊测试框架](https://www.ndss-symposium.org/wp-content/uploads/2019/02/ndss2019_04A-1_Song_paper.pdf)
- 2018 年，Muench 等人：[你损坏的不是你崩溃的：模糊嵌入式设备的挑战](http://www.eurecom.fr/en/publication/5417/download/sec-publi-5417.pdf)
- 2017 年，O'Meara 等人：[使用 Trommel 的嵌入式设备漏洞分析案例研究](https://resources.sei.cmu.edu/library/asset-view.cfm?assetid=509271)
- 2017 年，Jacob 等人：[如何通过恶意硬件破坏 FPGA SoC 上的安全启动](https://eprint.iacr.org/2017/625.pdf)
- 2017 年，Costin 等人：[迈向固件映像自动分类和嵌入式设备识别](http://s3.eurecom.fr/docs/ifip17_costin.pdf)
- 2016 年，Kammerstetter 等人：[使用外围设备缓存和运行时程序状态近似进行嵌入式安全测试](https://www.thinkmind.org/download.php?articleid=securware_2016_2_10_30082)
- 2016 年，Chen 等人：[面向基于 Linux 的嵌入式固件的自动动态分析](https://www.dcddcc.com/docs/2016_paper_firmadyne.pdf)
- 2016 年，Costin 等人：[大规模自动动态固件分析：嵌入式 Web 界面案例研究](http://s3.eurecom.fr/docs/asiaccs16_costin.pdf)
- 2015 年，Shoshitaishvili 等人：[Firmalice - 自动检测二进制固件中的身份验证绕过漏洞](https://www.ndss-symposium.org/wp-content/uploads/2017/09/11_1_2.pdf)
- 2015 年，Papp 等人：[嵌入式系统安全：威胁、漏洞和攻击分类](http://www.cse.psu.edu/~pdm12/cse597g-f15/readings/cse597g-embedded_systems.pdf)
- 2014 年，Zaddach 等人：[Avatar：支持嵌入式系统固件动态安全分析的框架](http://www.eurecom.fr/en/publication/4158/download/rs-publi-4158.pdf)
- 2014年，Alimi等人：[通过进化模糊测试分析嵌入式应用程序](http://ieeexplore.ieee.org/document/6903734/)
- 2014 年，Costin 等人：[嵌入式固件安全性的大规模分析](http://www.s3.eurecom.fr/docs/usenixsec14_costin.pdf)
- 2013 年，Davidson 等人：[关于固件的 FIE：使用符号执行查找嵌入式系统中的漏洞](https://www.usenix.org/system/files/conference/usenixsecurity13/sec13-paper_davidson.pdf)

## 案例研究

<!--lint ignore no-repeat-punctuation-->

- [物联网产品中的二进制强化](https://cyber-itl.org/2019/08/26/iot-data-writeup.html)
- [破解 Linksys“加密”](http://www.devttys0.com/2014/02/cracking-linksys-crypto/)
- [Deadly Sins Of Development](https://youtu.be/nXyglaY9N9w) - 会议演讲展示了几个关于真正糟糕的实现的现实例子:tv:。
- [使用buspirate从设备的SPI闪存转储固件](https://www.iotpentest.com/2019/06/dumping-firmware-from-device-using.html)
- [再次破解 DSP-W215](http://www.devttys0.com/2014/05/hacking-the-dspw215-again/)
- [Hacking the PS4](https://cturt.github.io/ps4.html) - PS4 安全性简介。
- [物联网安全@CERN](https://doi.org/10.5281/zenodo.1035034)
- [D-link DWR-932B 中发现多个漏洞](https://pierrekim.github.io/blog/2016-09-28-dlink-dwr-932b-lte-routers-vulnerabilities.html)
- [攻克Dlink 850L路由器并滥用MyDlink Cloud协议](https://pierrekim.github.io/blog/2017-09-08-dlink-850l-mydlink-cloud-0days-vulnerabilities.html)
- [PWN Xerox 打印机（...再次）](https://www.fkie.fraunhofer.de/content/dam/fkie/de/documents/xerox_phaser_6700_white_paper.pdf)
- [使用 Radare 逆向固件](https://www.bored-nerds.com/reversing/radare/automotive/2019/07/07/reversing-firmware-with-radare.html)
- [倒车华为HG533](http://jcjc-dev.com/2016/04/08/reversing-huawei-router-1-find-uart/)

## 免费培训

- [CSAW Embedded Security Challenge 2019](https://github.com/TrustworthyComputing/csaw_esc_2019) - CSAW 2019 嵌入式安全挑战赛 (ESC)。
- [Embedded Security CTF](https://microcorruption.com) - 微腐败：嵌入式安全 CTF。
- [Hardware Hacking 101](https://github.com/rdomanski/hardware_hacking/tree/master/my_talks/Hardware_Hacking_101) - 研讨会@ BSides 慕尼黑 2019。
- [IoTGoat](https://github.com/scriptingxss/IoTGoat) - IoTGoat 是一个基于 OpenWrt 的故意不安全的固件。
- [Rhme-2015](https://github.com/Riscure/RHme-2015) - 第一个 riscure Hack me 硬件 CTF 挑战。
- [Rhme-2016](https://github.com/Riscure/Rhme-2016) - Riscure Hack me 2 是一项低级别硬件 CTF 挑战。
- [Rhme-2017/2018](https://github.com/Riscure/Rhme-2017) - Riscure Hack Me 3 嵌入式硬件 CTF 2017-2018。

## 网站

- [Hacking Printers Wiki](http://hacking-printers.net/wiki/index.php/Main_Page) - 所有东西打印机。
- [OWASP Embedded Application Security Project](https://owasp.org/www-project-embedded-application-security/) - 开发最佳实践以及硬件和软件工具列表。
- [OWASP Internet of Things Project](https://owasp.org/www-project-internet-of-things/) - 物联网常见漏洞和攻击面。
- [Router Passwords](https://192-168-1-1ip.mobi/default-router-passwords-list/) - 默认登录凭据数据库按制造商排序。
- [Siliconpr0n](https://siliconpr0n.org/) - IC 逆向所有内容的 Wiki/档案。

### 博客

<!--lint ignore no-repeat-punctuation-->

- [RTL-SDR](https://www.rtl-sdr.com/)
- [/dev/ttyS0 的嵌入式设备黑客攻击](http://www.devttys0.com/blog/)
- [Exploiteers](https://www.exploitee.rs/)
- [Hackaday](https://hackaday.com)
- [jcjc 的 Hack The World](https://jcjc-dev.com/)
- [Quarkslab](https://blog.quarkslab.com/)
- [波特率错误](https://wrongbaud.github.io/)
- [固件安全](https://firmwaresecurity.com/)
- [PenTestPartners](https://www.pentestpartners.com/internet-of-things/)
- [Attify](https://blog.attify.com/)
- [Patayu](https://payatu.com/blog)
- [GracefulSecurity - 硬件标签](https://gracefulsecurity.com/category/hardware/)
- [Black Hills - 硬件黑客标签](https://www.blackhillsinfosec.com/tag/hardware-hacking/)

### 教程和技术背景

- [Azeria Lab](https://azeria-labs.com/) - 其他 ARM 相关教程。
- [JTAG Explained](https://blog.senr.io/blog/jtag-explained#) - 涵盖 UART 和 JTAG 的演练，绕过受保护的登录 shell。
- [Reverse Engineering Serial Ports](http://www.devttys0.com/2012/11/reverse-engineering-serial-ports/) - 有关如何在 PCB 上发现调试焊盘的详细教程。
- [UART explained](https://www.mikroe.com/blog/uart-serial-communication) - UART协议的深入解释。

### YouTube 频道

- [Flashback Team](https://www.youtube.com/c/FlashbackTeam) - 两位黑客逐步解释了他们查找和利用嵌入式设备漏洞的方法。
- [StackSmashing](https://www.youtube.com/c/stacksmashing) - 嵌入式设备的逆向工程和硬件黑客。

## 会议

会议重点关注嵌入式和/或物联网安全。

- [Hardwear.io](https://hardwear.io/)
- 欧盟，海牙，九月。
- 美国，圣克拉拉，六月。

## 贡献

欢迎投稿！首先阅读[贡献指南](contributing.md)。

## 许可证

[![CC0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

在法律允许的范围内，Fraunhofer FKIE 已放弃所有版权和
本作品的相关或邻接权。
