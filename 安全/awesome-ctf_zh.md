# 很棒的CTF [![Build Status](https://travis-ci.org/apsdehal/awesome-ctf.svg?branch=master)](https://travis-ci.org/apsdehal/awesome-ctf)

[Capture The Flag](https://en.wikipedia.org/wiki/Capture_the_flag#Computer_security) (CTF) 框架、库、资源、软件和教程的精选列表。此列表旨在帮助初学者以及经验丰富的 CTF 玩家在一个地方找到与 CTF 相关的所有内容。

### 贡献

请先快速浏览一下[贡献指南](https://github.com/apsdehal/ctf-tools/blob/master/CONTRIBUTING.md)。

#### _如果您知道此处没有的工具，请随时打开拉取请求。_

### 为什么？

建立 CTF 中使用的工具集合并记住它们需要时间。该存储库有助于将所有这些分散的工具保留在一个地方。

### 内容

- [很棒的CTF](#awesome-ctf)
  - [Create](#create)
    - [Forensics](#forensics)
    - [Platforms](#platforms)
    - [Steganography](#steganography)
    - [Web](#web)
  - [Solve](#solve)
    - [Attacks](#attacks)
    - [Bruteforcers](#bruteforcers)
    - [Cryptography](#crypto)
    - [Exploits](#exploits)
    - [Forensics](#forensics-1)
    - [Networking](#networking)
    - [Reversing](#reversing)
    - [Services](#services)
    - [Steganography](#steganography-1)
    - [Web](#web-1)

- [Resources](#resources)
  - [操作系统](#operating-systems)
  - [入门包](#starter-packs)
  - [Tutorials](#tutorials)
  - [Wargames](#wargames)
  - [Websites](#websites)
  - [Wikis](#wikis)
  - [写文集](#writeups-collections)


# 创建

*用于创建CTF挑战的工具*

- [Kali Linux CTF Blueprints](https://www.packtpub.com/eu/networking-and-servers/kali-linux-ctf-blueprints) - 有关构建、测试和定制您自己的夺旗挑战的在线书籍。


## 法证学

*用于创建取证挑战的工具*

- [Dnscat2](https://github.com/iagox86/dnscat2) - 通过 DNS 进行主机通信。
- [Kroll Artifact Parser and Extractor (KAPE)](https://learn.duffandphelps.com/kape) - 分诊计划。
- [Magnet AXIOM](https://www.magnetforensics.com/downloadaxiom) - 以工件为中心的 DFIR 工具。
- [Registry Dumper](http://www.kahusecurity.com/posts/registry_dumper_find_and_dump_hidden_registry_keys.html) - 转储您的注册表。

## 平台

*可用于举办 CTF 的项目*

- [CTFd](https://github.com/isislab/CTFd) - 用于托管纽约大学 Tandon ISISLab 危险风格 CTF 的平台。
- [echoCTF.RED](https://github.com/echoCTF/echoCTF.RED) - 开发、部署和维护您自己的 CTF 基础设施。
- [FBCTF](https://github.com/facebook/fbctf) - Facebook 举办夺旗比赛的平台。
- [Haaukins](https://github.com/aau-network-security/haaukins) - 用于安全教育的高度可访问且自动化的虚拟化平台。
- [HackTheArch](https://github.com/mcpa-stlouis/hack-the-arch) - CTF评分平台。
- [Mellivora](https://github.com/Nakiami/mellivora) - 用 PHP 编写的 CTF 引擎。
- [MotherFucking-CTF](https://github.com/andreafioraldi/motherfucking-ctf) - 用于托管 CTF 的 Badass 轻量级平台。不涉及 JS。
- [NightShade](https://github.com/UnrealAkama/NightShade) - 一个简单的安全CTF框架。
- [OpenCTF](https://github.com/easyctf/openctf) - CTF 装在盒子里。需要最少的设置。
- [PicoCTF](https://github.com/picoCTF/picoCTF) - 用于运行 picoCTF 的平台。一个托管任何 CTF 的优秀框架。
- [PyChallFactory](https://github.com/pdautry/py_chall_factory) - 用于创建/管理/打包危险 CTF 挑战的小型框架。
- [RootTheBox](https://github.com/moloch--/RootTheBox) - 黑客游戏（CTF 记分板和游戏管理器）。
- [Scorebot](https://github.com/legitbs/scorebot) - Legitbs (Defcon) 的 CTF 平台。
- [SecGen](https://github.com/cliffe/SecGen) - 安全场景生成器。创建随机易受攻击的虚拟机。

## 隐写术

*用于创建隐写挑战的工具*

检查隐写术的解决部分。

## 网络

*用于创建网络挑战的工具*

*JavaScript 混淆器*

- [Metasploit JavaScript 混淆器](https://github.com/rapid7/metasploit-framework/wiki/How-to-obfuscate-JavaScript-in-Metasploit)
- [Uglify](https://github.com/mishoo/UglifyJS)


# 解决

*用于解决CTF挑战的工具*

## 攻击

*用于执行各种攻击的工具*

- [Bettercap](https://github.com/bettercap/bettercap) - 执行 MITM（中间人）攻击的框架。
- [Yersinia](https://github.com/tomac/yersinia) - 攻击第 2 层的各种协议。

## 加密货币

*用于解决加密挑战的工具*

- [CyberChef](https://gchq.github.io/CyberChef) - 用于分析和解码数据的 Web 应用程序。
- [FeatherDuster](https://github.com/nccgroup/featherduster) - 一种自动化、模块化的密码分析工具。
- [Hash Extender](https://github.com/iagox86/hash_extender) - 用于执行哈希长度扩展攻击的实用工具。
- [padding-oracle-attacker](https://github.com/KishanBagaria/padding-oracle-attacker) - 用于执行 padding oracle 攻击的 CLI 工具。
- [PkCrack](https://www.unix-ag.uni-kl.de/~conrad/krypto/pkcrack.html) - 破解 PkZip 加密的工具。
- [QuipQuip](https://quipqiup.com) - 用于破解替换密码或维吉尼亚密码（无密钥）的在线工具。
- [RSACTFTool](https://github.com/Ganapati/RsaCtfTool) - 一种通过各种攻击恢复RSA私钥的工具。
- [RSATool](https://github.com/ius/rsatool) - 根据 p 和 q 的知识生成私钥。
- [XORTool](https://github.com/hellman/xortool) - 分析多字节异或密码的工具。

## 暴力破解者

*用于各种暴力破解的工具（密码等）*

- [Hashcat](https://hashcat.net/hashcat/) - 密码破解器
- [Hydra](https://tools.kali.org/password-attacks/hydra) - 并行登录破解器，支持多种协议攻击
- [John The Jumbo](https://github.com/magnumripper/JohnTheRipper) - 开膛手约翰的社区增强版。
- [John The Ripper](http://www.openwall.com/john/) - 密码破解者。
- [Nozzlr](https://github.com/intrd/nozzlr) - Nozzlr 是一个强力框架，真正的模块化且脚本友好。
- [Ophcrack](http://ophcrack.sourceforge.net/) - 基于彩虹表的 Windows 密码破解程序。
- [Patator](https://github.com/lanjelot/patator) - Patator 是一款多用途暴力破解器，采用模块化设计。
- [Turbo Intruder](https://portswigger.net/research/turbo-intruder-embracing-the-billion-request-attack) - Burp Suite 扩展用于发送大量 HTTP 请求

## 功绩

*用于解决漏洞利用挑战的工具*

- [DLLInjector](https://github.com/OpenSecurityResearch/dllinjector) - 在进程中注入 dll。
- [libformatstr](https://github.com/hellman/libformatstr) - 简化格式字符串的利用。
- [Metasploit](http://www.metasploit.com/) - 渗透测试软件。
  - [Cheatsheet](https://www.comparitech.com/net-admin/metasploit-cheat-sheet/)
- [one_gadget](https://github.com/david942j/one_gadget) - 一种用于查找单个小工具“execve('/bin/sh', NULL, NULL)”调用的工具。
- `gem install one_gadget`
- [Pwntools](https://github.com/Gallopsled/pwntools) - 用于编写漏洞利用的 CTF 框架。
- [Qira](https://github.com/BinaryAnalysisPlatform/qira) - QEMU 交互式运行时分析器。
- [ROP Gadget](https://github.com/JonathanSalwan/ROPgadget) - ROP 利用框架。
- [V0lt](https://github.com/P1kachu/v0lt) - 安全 CTF 工具包。

## 法证学

*用于解决取证挑战的工具*

- [Aircrack-Ng](http://www.aircrack-ng.org/) - 破解 802.11 WEP 和 WPA-PSK 密钥。
- `apt-get install aircrack-ng`
- [Audacity](http://sourceforge.net/projects/audacity/) - 分析声音文件（mp3、m4a 等）。
- `apt-get install audacity`
- [Bkhive and Samdump2](http://sourceforge.net/projects/ophcrack/files/samdump2/) - 转储 SYSTEM 和 SAM 文件。
- `apt-get install samdump2 bkhive`
- [CFF Explorer](http://www.ntcore.com/exsuite.php) - PE编辑器。
- [Creddump](https://github.com/moyix/creddump) - 转储 Windows 凭据。
- [DVCS Ripper](https://github.com/kost/dvcs-ripper) - 撕裂网络可访问（分布式）版本控制系统。
- [Exif Tool](http://www.sno.phy.queensu.ca/~phil/exiftool/) - 读取、写入和编辑文件元数据。
- [Extundelete](http://extundelete.sourceforge.net/) - 用于从可安装映像中恢复丢失的数据。
- [Fibratus](https://github.com/rabbitstack/fibratus) - 用于探索和跟踪 Windows 内核的工具。
- [Foremost](http://foremost.sourceforge.net/) - 使用标头提取特定类型的文件。
- `apt-get install 最重要`
- [Fsck.ext4](http://linux.die.net/man/8/fsck.ext3) - 用于修复损坏的文件系统。
- [Malzilla](http://malzilla.sourceforge.net/) - 恶意软件狩猎工具。
- [NetworkMiner](http://www.netresec.com/?page=NetworkMiner) - 网络取证分析工具。
- [PDF Streams Inflater](http://malzilla.sourceforge.net/downloads.html) - 查找并解压缩 PDF 文件中的 zlib 文件。
- [Pngcheck](http://www.libpng.org/pub/png/apps/pngcheck.html) - 验证 PNG 的完整性并以人类可读的形式转储所有块级信息。
- `apt-get install pngcheck`
- [ResourcesExtract](http://www.nirsoft.net/utils/resources_extract.html) - 从 exe 中提取各种文件类型。
- [Shellbags](https://github.com/williballenthin/shellbags) - 调查 NT\_USER.dat 文件。
- [Snow](https://sbmlabs.com/notes/snow_whitespace_steganography_tool) - 空白隐写术工具。
- [USBRip](https://github.com/snovvcrash/usbrip) - 简单的 CLI 取证工具，用于在 GNU/Linux 上跟踪 USB 设备工件（USB 事件的历史记录）。
- [Volatility](https://github.com/volatilityfoundation/volatility) - 调查内存转储。
- [Wireshark](https://www.wireshark.org) - 用于分析 pcap 或 pcapng 文件

*注册表查看器*
- [OfflineRegistryView](https://www.nirsoft.net/utils/offline_registry_view.html) - 适用于 Windows 的简单工具，允许您从外部驱动器读取脱机注册表文件并以 .reg 文件格式查看所需的注册表项。
- [Registry Viewer®](https://accessdata.com/product-download/registry-viewer-2-0-0) - 用于查看 Windows 注册表。

## 网络

*用于解决网络挑战的工具*

- [Masscan](https://github.com/robertdavidgraham/masscan) - 海量IP端口扫描器、TCP端口扫描器。
- [Monit](https://linoxide.com/monitoring-2/monit-linux/) - 用于检查网络上的主机（以及其他非网络活动）的 Linux 工具。
- [Nipe](https://github.com/GouveaHeitor/nipe) - Nipe 是一个使 Tor 网络成为默认网关的脚本。
- [Nmap](https://nmap.org/) - 用于网络发现和安全审核的开源实用程序。
- [Wireshark](https://www.wireshark.org/) - 分析网络转储。
-`apt-get安装wireshark`
- [Zeek](https://www.zeek.org) - 开源网络安全监视器。
- [Zmap](https://zmap.io/) - 开源网络扫描仪。

## 倒车

*用于解决逆向挑战的工具*

- [Androguard](https://github.com/androguard/androguard) - 对 Android 应用程序进行逆向工程。
- [Angr](https://github.com/angr/angr) - 与平台无关的二进制分析框架。
- [Apk2Gold](https://github.com/lxdvs/apk2gold) - 又一个 Android 反编译器。
- [ApkTool](http://ibotpeaches.github.io/Apktool/) - 安卓反编译器。
- [Barf](https://github.com/programa-stic/barf-project) - 二进制分析和逆向工程框架。
- [Binary Ninja](https://binary.ninja/) - 二进制分析框架。
- [BinUtils](http://www.gnu.org/software/binutils/binutils.html) - 二进制工具的集合。
- [BinWalk](https://github.com/devttys0/binwalk) - 分析、逆向工程和提取固件映像。
- [Boomerang](https://github.com/BoomerangDecompiler/boomerang) - 将 x86/SPARC/PowerPC/ST-20 二进制文件反编译为 C。
- [ctf_import](https://github.com/docileninja/ctf_import) - 从跨平台的剥离二进制文件运行基本功能。
- [cwe_checker](https://github.com/fkie-cad/cwe_checker) - cwe_checker 在二进制可执行文件中查找易受攻击的模式。
- [demovfuscator](https://github.com/kirschju/demovfuscator) - 一个正在进行的用于 movfuscated 二进制文件的反混淆器。
- [Frida](https://github.com/frida/) - 动态代码注入。
- [GDB](https://www.gnu.org/software/gdb/) - GNU 项目调试器。
- [GEF](https://github.com/hugsy/gef) - GDB 插件。
- [Ghidra](https://ghidra-sre.org/) - 逆向工程工具的开源套件。  与 IDA Pro 类似。
- [Hopper](http://www.hopperapp.com/) - 适用于 OSX 和 Linux 的逆向工程工具（反汇编程序）。
- [IDA Pro](https://www.hex-rays.com/products/ida/) - 最常用的倒车软件。
- [Jadx](https://github.com/skylot/jadx) - 反编译Android文件。
- [Java Decompilers](http://www.javadecompilers.com) - Java 和 Android APK 的在线反编译器。
- [Krakatau](https://github.com/Storyyeller/Krakatau) - Java 反编译器和反汇编器。
- [Objection](https://github.com/sensepost/objection) - 运行时移动探索。
- [PEDA](https://github.com/longld/peda) - GDB插件（仅限python2.7）。
- [Pin](https://software.intel.com/en-us/articles/pin-a-dynamic-binary-instrumentation-tool) - Intel 的动态二进制检测工具。
- [PINCE](https://github.com/korcankaraokcu/PINCE) - GDB 前端/逆向工程工具，专注于游戏黑客和自动化。
- [PinCTF](https://github.com/ChrisTheCoolHut/PinCTF) - 一个使用 intel pin 进行旁路分析的工具。
- [Plasma](https://github.com/joelpx/plasma) - 适用于 x86/ARM/MIPS 的交互式反汇编程序，可以生成具有彩色语法的缩进伪代码。
- [Pwndbg](https://github.com/pwndbg/pwndbg) - 一个 GDB 插件，提供了一套实用程序来轻松破解 GDB。
- [radare2](https://github.com/radare/radare2) - 便携式倒车框架。
- [Triton](https://github.com/JonathanSalwan/Triton/) - 动态二进制分析 (DBA) 框架。
- [Uncompyle](https://github.com/gstarnberger/uncompyle) - 反编译 Python 2.7 二进制文件 (.pyc)。
- [WinDbg](http://www.windbg.org/) - 由 Microsoft 分发的 Windows 调试器。
- [Xocopy](http://reverse.lostrealm.com/tools/xocopy.html) - 可以复制具有执行权限但没有读取权限的可执行文件的程序。
- [Z3](https://github.com/Z3Prover/z3) - 来自微软研究院的定理证明者。

*JavaScript 反混淆器*

- [Detox](http://relentless-coding.org/projects/jsdetox/install) - 一个 Javascript 恶意软件分析工具。
- [Revelo](http://www.kahusecurity.com/posts/revelo_javascript_deobfuscator.html) - 分析混淆的 Javascript 代码。

*SWF 分析器*
- [RABCDAsm](https://github.com/CyberShadow/RABCDAsm) - 实用程序的集合，包括 ActionScript 3 汇编器/反汇编器。
- [Swftools](http://www.swftools.org/) - 用于处理 SWF 文件的实用程序集合。
- [Xxxswf](https://bitbucket.org/Alexander_Hanel/xxxswf) - 用于分析 Flash 文件的 Python 脚本。

## 服务

*通过互联网提供各种有用的服务*

- [CSWSH](http://cow.cat/cswsh.html) - 跨站点 WebSocket 劫持测试器。
- [Request Bin](https://requestbin.com/) - 允许您检查对特定 url 的 http 请求。

## 隐写术

*用于解决隐写术挑战的工具*

- [AperiSolve](https://aperisolve.fr/) - Aperi'Solve 是一个对图像进行图层分析的平台（开源）。
- [Convert](http://www.imagemagick.org/script/convert.php) - 转换图像黑白格式并应用滤镜。
- [Exif](http://manpages.ubuntu.com/manpages/trusty/man1/exif.1.html) - 显示 JPEG 文件中的 EXIF 信息。
- [Exiftool](https://linux.die.net/man/1/exiftool) - 读取和写入文件中的元信息。
- [Exiv2](http://www.exiv2.org/manpage.html) - 图像元数据处理工具。
- [Image Steganography](https://sourceforge.net/projects/image-steg/) - 通过可选加密将文本和文件嵌入图像中。易于使用的用户界面。
- [Image Steganography Online](https://incoherency.co.uk/image-steganography) - 这是一个客户端 Javascript 工具，用于以隐写方式将图像隐藏在其他图像的较低“位”内
- [ImageMagick](http://www.imagemagick.org/script/index.php) - 用于操作图像的工具。
- [Outguess](https://www.freebsd.org/cgi/man.cgi?query=outguess+&apropos=0&sektion=0&manpath=FreeBSD+Ports+5.1-RELEASE&format=html) - 通用隐写工具。
- [Pngtools](https://packages.debian.org/sid/pngtools) - 用于与 PNG 相关的各种分析。
- `apt-get install pngtools`
- [SmartDeblur](https://github.com/Y-Vladimir/SmartDeblur) - 用于去模糊和修复散焦图像。
- [Steganabara](https://www.openhub.net/p/steganabara) - 用 Java 编写的隐写分析工具。
- [SteganographyOnline](https://stylesuxx.github.io/steganography/) - 在线隐写编码器和解码器。
- [Stegbreak](https://linux.die.net/man/1/stegbreak) - 对 JPG 图像发起暴力字典攻击。
- [StegCracker](https://github.com/Paradoxis/StegCracker) - 隐写术强力实用程序可发现文件内的隐藏数据。
- [stegextract](https://github.com/evyatarmeged/stegextract) - 检测图像中的隐藏文件和文本。
- [Steghide](http://steghide.sourceforge.net/) - 将数据隐藏在各种图像中。
- [StegOnline](https://georgeom.net/StegOnline/upload) - 进行广泛的图像隐写操作，例如隐藏/显示隐藏在位中的文件（开源）。
- [Stegsolve](http://www.caesum.com/handbook/Stegsolve.jar) - 将各种隐写技术应用于图像。
- [Zsteg](https://github.com/zed-0xff/zsteg/) - PNG/BMP 分析。

## 网络

*用于解决网络挑战的工具*

- [BurpSuite](https://portswigger.net/burp) - 用于测试网站安全性的图形工具。
- [Commix](https://github.com/commixproject/commix) - 自动化一体化操作系统命令注入和利用工具。
- [Hackbar](https://addons.mozilla.org/en-US/firefox/addon/hackbartool/) - Firefox 插件可轻松进行网络利用。
- [OWASP ZAP](https://www.owasp.org/index.php/Projects/OWASP_Zed_Attack_Proxy_Project) - 拦截代理以重放、调试和模糊 HTTP 请求和响应
- [Postman](https://chrome.google.com/webstore/detail/postman/fhbjgbiflinjbdggehcddcbncdddomop?hl=en) - 为 Chrome 添加用于调试网络请求。
- [Raccoon](https://github.com/evyatarmeged/Raccoon) - 用于侦察和漏洞扫描的高性能进攻性安全工具。
- [SQLMap](https://github.com/sqlmapproject/sqlmap) - 自动 SQL 注入和数据库接管工具。
  ```pip install sqlmap```
- [W3af](https://github.com/andresriancho/w3af) -  Web Application Attack and Audit Framework.
- [XSSer](http://xsser.sourceforge.net/) - Automated XSS testor.


# Resources

*Where to discover about CTF*

## Operating Systems

*Penetration testing and security lab Operating Systems*

- [Android Tamer](https://androidtamer.com/) - Based on Debian.
- [BackBox](https://backbox.org/) - Based on Ubuntu.
- [BlackArch Linux](https://blackarch.org/) - Based on Arch Linux.
- [Fedora Security Lab](https://labs.fedoraproject.org/security/) - Based on Fedora.
- [Kali Linux](https://www.kali.org/) - Based on Debian.
- [Parrot Security OS](https://www.parrotsec.org/) - Based on Debian.
- [Pentoo](http://www.pentoo.ch/) - Based on Gentoo.
- [URIX OS](http://urix.us/) - Based on openSUSE.
- [Wifislax](http://www.wifislax.com/) - Based on Slackware.

*Malware analysts and reverse-engineering*

- [Flare VM](https://github.com/fireeye/flare-vm/) - Based on Windows.
- [REMnux](https://remnux.org/) - Based on Debian.

## Starter Packs

*Collections of installer scripts, useful tools*

- [CTF Tools](https://github.com/zardus/ctf-tools) - Collection of setup scripts to install various security research tools.
- [LazyKali](https://github.com/jlevitsk/lazykali) - A 2016 refresh of LazyKali which simplifies install of tools and configuration.

## Tutorials

*Tutorials to learn how to play CTFs*

- [CTF Field Guide](https://trailofbits.github.io/ctf/) - Field Guide by Trails of Bits.
- [CTF Resources](http://ctfs.github.io/resources/) -  Start Guide maintained by community.
- [How to Get Started in CTF](https://www.endgame.com/blog/how-get-started-ctf) - Short guideline for CTF beginners by Endgame
- [Intro. to CTF Course](https://www.hoppersroppers.org/courseCTF.html) - A free course that teaches beginners the basics of forensics, crypto, and web-ex.
- [IppSec](https://www.youtube.com/channel/UCa6eh7gCkpPo5XXUDfygQQA) - Video tutorials and walkthroughs of popular CTF platforms.
- [LiveOverFlow](https://www.youtube.com/channel/UClcE-kVhqyiHCcjYwcpfj9w) - Video tutorials on Exploitation.
- [MIPT CTF](https://github.com/xairy/mipt-ctf) - A small course for beginners in CTFs (in Russian).


## Wargames

*Always online CTFs*

- [Backdoor](https://backdoor.sdslabs.co/) - Security Platform by SDSLabs.
- [Crackmes](https://crackmes.one/) - Reverse Engineering Challenges.
- [CryptoHack](https://cryptohack.org/) - Fun cryptography challenges.
- [echoCTF.RED](https://echoctf.red/) - Online CTF with a variety of targets to attack.
- [Exploit Exercises](https://exploit-exercises.lains.space/) - Variety of VMs to learn variety of computer security issues.
- [Exploit.Education](http://exploit.education) - Variety of VMs to learn variety of computer security issues.
- [Gracker](https://github.com/Samuirai/gracker) - Binary challenges having a slow learning curve, and write-ups for each level.
- [Hack The Box](https://www.hackthebox.eu) - Weekly CTFs for all types of security enthusiasts.
- [Hack This Site](https://www.hackthissite.org/) - Training ground for hackers.
- [Hacker101](https://www.hacker101.com/) - CTF from HackerOne
- [Hacking-Lab](https://hacking-lab.com/) - Ethical hacking, computer network and security challenge platform.
- [Hone Your Ninja Skills](https://honeyourskills.ninja/) - Web challenges starting from basic ones.
- [IO](http://io.netgarage.org/) - Wargame for binary challenges.
- [Microcorruption](https://microcorruption.com) - Embedded security CTF.
- [Over The Wire](http://overthewire.org/wargames/) - Wargame maintained by OvertheWire Community.
- [PentesterLab](https://pentesterlab.com/) - Variety of VM and online challenges (paid).
- [PicoCTF](https://2019game.picoctf.com) - All year round ctf game. Questions from the yearly picoCTF competition.
- [PWN Challenge](http://pwn.eonew.cn/) - Binary Exploitation Wargame.
- [Pwnable.kr](http://pwnable.kr/) - Pwn Game.
- [Pwnable.tw](https://pwnable.tw/) - Binary wargame.
- [Pwnable.xyz](https://pwnable.xyz/) - Binary Exploitation Wargame.
- [Reversin.kr](http://reversing.kr/) - Reversing challenge.
- [Ringzer0Team](https://ringzer0team.com/) - Ringzer0 Team Online CTF.
- [Root-Me](https://www.root-me.org/) - Hacking and Information Security learning platform.
- [ROP Wargames](https://github.com/xelenonz/game) - ROP Wargames.
- [SANS HHC](https://holidayhackchallenge.com/past-challenges/) - Challenges with a holiday theme
  released annually and maintained by SANS.
- [SmashTheStack](http://smashthestack.org/) - A variety of wargames maintained by the SmashTheStack Community.
- [Viblo CTF](https://ctf.viblo.asia) - Various amazing CTF challenges, in many different categories. Has both Practice mode and Contest mode.
- [VulnHub](https://www.vulnhub.com/) - VM-based for practical in digital security, computer application & network administration.
- [W3Challs](https://w3challs.com) - A penetration testing training platform, which offers various computer challenges, in various categories.
- [WebHacking](http://webhacking.kr) - Hacking challenges for web.


*Self-hosted CTFs*
- [Damn Vulnerable Web Application](http://www.dvwa.co.uk/) - PHP/MySQL web application that is damn vulnerable.
- [Juice Shop CTF](https://github.com/bkimminich/juice-shop-ctf) - Scripts and tools for hosting a CTF on [OWASP Juice Shop](https://www.owasp.org/index.php/OWASP_Juice_Shop_Project) easily.

## Websites

*Various general websites about and on CTF*

- [Awesome CTF Cheatsheet](https://github.com/uppusaikiran/awesome-ctf-cheatsheet#awesome-ctf-cheatsheet-) - CTF Cheatsheet.
- [CTF Time](https://ctftime.org/) - General information on CTF occuring around the worlds.
- [Reddit Security CTF](http://www.reddit.com/r/securityctf) - Reddit CTF category.

## Wikis

*Various Wikis available for learning about CTFs*

- [Bamboofox](https://bamboofox.github.io/) - Chinese resources to learn CTF.
- [bi0s Wiki](https://teambi0s.gitlab.io/bi0s-wiki/) - Wiki from team bi0s.
- [CTF Cheatsheet](https://uppusaikiran.github.io/hacking/Capture-the-Flag-CheatSheet/) - CTF tips and tricks.
- [ISIS Lab](https://github.com/isislab/Project-Ideas/wiki) - CTF Wiki by Isis lab.
- [OpenToAll](https://github.com/OpenToAllCTF/Tips) - CTF tips by OTA CTF team members.

## Writeups Collections

*Collections of CTF write-ups*

- [0e85dc6eaf](https://github.com/0e85dc6eaf/CTF-Writeups) - Write-ups for CTF challenges by 0e85dc6eaf
- [Captf](http://captf.com/) - Dumped CTF challenges and materials by psifertex.
- [CTF write-ups (community)](https://github.com/ctfs/) - CTF challenges + write-ups archive maintained by the community.
- [CTFTime Scrapper](https://github.com/abdilahrf/CTFWriteupScrapper) - Scraps all writeup from CTF Time and organize which to read first.
- [HackThisSite](https://github.com/HackThisSite/CTF-Writeups) - CTF write-ups repo maintained by HackThisSite team.
- [Mzfr](https://github.com/mzfr/ctf-writeups/) - CTF competition write-ups by mzfr
- [pwntools writeups](https://github.com/Gallopsled/pwntools-write-ups) - A collection of CTF write-ups all using pwntools.
- [SababaSec](https://github.com/SababaSec/ctf-writeups) - A collection of CTF write-ups by the SababaSec team
- [Shell Storm](http://shell-storm.org/repo/CTF/) - CTF challenge archive maintained by Jonathan Salwan.
- [Smoke Leet Everyday](https://github.com/smokeleeteveryday/CTF_WRITEUPS) - CTF write-ups repo maintained by SmokeLeetEveryday team.

### LICENSE

CC0 :)
