# android-security-awesome ![很棒](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)

[![Star History Rank](https://api.star-history.com/badge?repo=ashishb/android-security-awesome&theme=dark)](https://www.star-history.com/ashishb/android-security-awesome)

[![Link Liveness Checker](https://github.com/ashishb/android-security-awesome/actions/workflows/validate-links.yml/badge.svg)](https://github.com/ashishb/android-security-awesome/actions/workflows/validate-links.yml)

[![Lint Shell scripts](https://github.com/ashishb/android-security-awesome/actions/workflows/lint-shell-script.yaml/badge.svg)](https://github.com/ashishb/android-security-awesome/actions/workflows/lint-shell-script.yaml)
[![Lint Markdown](https://github.com/ashishb/android-security-awesome/actions/workflows/lint-markdown.yaml/badge.svg)](https://github.com/ashishb/android-security-awesome/actions/workflows/lint-markdown.yaml)
[![Lint YAML](https://github.com/ashishb/android-security-awesome/actions/workflows/lint-yaml.yaml/badge.svg)](https://github.com/ashishb/android-security-awesome/actions/workflows/lint-yaml.yaml)
[![Lint GitHub Actions](https://github.com/ashishb/android-security-awesome/actions/workflows/lint-github-actions.yaml/badge.svg)](https://github.com/ashishb/android-security-awesome/actions/workflows/lint-github-actions.yaml)
![GitHub contributors](https://img.shields.io/github/contributors/ashishb/android-security-awesome)

Android 安全相关资源的集合。

1. [工具](#tools)
1. [学术/研究/出版物/书籍](#academic)
1. [漏洞利用/漏洞/错误](#exploits)

## 工具

### 在线分析仪

1. [Appknox](https://www.appknox.com/) - 不是免费的
1. [Virustotal](https://www.virustotal.com/)
1. [NowSecure Lab Automated](https://www.nowsecure.com/blog/2016/09/19/announcing-nowsecure-lab-automated/) - 用于移动应用程序安全测试 Android 和 iOS 移动应用程序的企业工具。 Lab Automated 具有对云端真实设备进行动态和静态分析的功能，可在几分钟内返回结果。不免费
1. [App Detonator](https://appdetonator.run/) - Detonate APK 二进制文件以提供源代码级别详细信息，包括应用程序作者、签名、构建和清单信息。 3 分析/天免费配额。
1. [Pithus](https://beta.pithus.org/) - 开源 APK 分析器。仍处于测试阶段，目前仅限于静态分析。可以使用 Yara 规则来追捕恶意软件。更多信息[此处](https://beta.pithus.org/about/)。
1. [Oversecured](https://oversecured.com/) - 适用于 Android 和 iOS 应用程序的企业漏洞扫描器；它使应用程序所有者和开发人员能够通过将 Oversecured 集成到开发过程中来保护移动应用程序的每个新版本。不是免费的。
1. [AppSweep by Guardsquare](https://appsweep.guardsquare.com/) - 为开发人员提供免费、快速的 Android 应用程序安全测试
1. [Koodous](https://koodous.com) - 对大量 Android 样本存储库执行静态/动态恶意软件分析，并根据公共和私有 Yara 规则检查它们。
1. [Immuniweb](https://www.immuniweb.com/mobile/)。进行“OWASP 移动前 10 名测试”、“移动应用程序隐私检查”和应用程序权限测试。免费套餐为每天 4 次测试，包括注册后的报告
1. [ANY.RUN](https://app.any.run/) - 一个基于云的交互式恶意软件分析平台，支持 Android 应用程序分析。提供有限的免费计划。
1. ~~[BitBaan](https://malab.bitbaan.com/)~~
1. ~~[AVC UnDroid](http://undroid.av-comparatives.info/)~~
1. ~~[AMAaaS](https://amaaas.com) - 免费 Android 恶意软件分析服务。裸机服务具有对 Android 应用程序进行静态和动态分析的功能。 [MalwarePot](https://malwarepot.com/index.php/AMAaaS) 的产品~~。
1. ~~[AppCritique](https://appcritique.boozallen.com) - 上传您的 Android APK 并获得全面的免费安全评估~~
1. ~~[NVISO ApkScan](https://apkscan.nviso.be/) - 2019年10月31日日落~~
1. ~~[移动恶意软件沙箱](http://www.mobilemalware.com.br/analysis/index_en.php)~~
1. ~~[IBM Security AppScan Mobile Analyzer](https://appscan.bluemix.net/mobileAnalyzer) - 不是免费的~~
1. ~~[Visual Threat](https://www.visualthreat.com/) - 不再是Android应用分析器~~
1. ~~[Tracedroid](http://tracedroid.few.vu.nl/)~~
1. ~~[habo](https://habo.qq.com/) - 10/天~~
1. ~~[CopperDroid](http://copperdroid.isg.rhul.ac.uk/copperdroid/)~~
1. ~~[SandDroid](http://sanddroid.xjtu.edu.cn/)~~
1. ~~[偷渡](http://www.android-permissions.org/)~~
1. ~~[阿努比斯](http://anubis.iseclab.org/)~~
1. ~~[移动应用洞察](http://www.mobile-app-insight.org)~~
1. ~~[Mobile-Sandbox](http://mobile-sandbox.com)~~
1. ~~[ijiami](http://safe.ijiami.cn/)~~
1. ~~[Comdroid](http://www.comdroid.org/)~~
1. ~~[Android沙盒](http://www.androidsandbox.net/)~~
1. ~~[Foresafe](http://www.foresafe.com/scan)~~
1. ~~[Dexter](https://dexter.dexlabs.org/)~~
1. ~~[MobiSec Eacus](http://www.mobiseclab.org/eacus.jsp)~~
1. ~~[Fireeye](https://fireeye.ijinshan.com/)- 最大 60MB 15/天~~
1. ~~[approver](https://approver.talos-sec.com/) - Approver 是一个针对 Android 和 iOS 应用程序的全自动安全分析和风险评估平台。不是免费的~~
1. ~~[Fraunhofer App-ray](http://app-ray.co/) - 域名过期~~
1. ~~[AndroTotal](http://andrototal.org/) - 死了~~

### 静态分析工具

1. [Androwarn](https://github.com/maaaaz/androwarn/) - 检测并警告用户 Android 应用程序开发的潜在恶意行为。
1. [ApkAnalyser](https://github.com/sonyxperiadev/ApkAnalyser)
1. [APKInspector](https://github.com/honeynet/apkinspector/)
1.【针对信息泄露的Droid Intent数据流分析】(https://insights.sei.cmu.edu/library/didfail/)
1. [DroidLegacy](https://bitbucket.org/srl/droidlegacy)
1. [FlowDroid](https://blogs.uni-paderborn.de/sse/tools/flowdroid/)
1. [Android反编译器](https://www.pnfsoftware.com/) – 不是免费的
1. [PSCout](https://security.csl.toronto.edu/pscout/) - 使用静态分析从 Android 操作系统源代码中提取权限规范的工具
1. [Amandroid](http://amandroid.sireum.org/)
1. [SmaliSCA](https://github.com/dorneanu/smalisca) - Smali静态代码分析
1. [CFGScanDroid](https://github.com/douggard/CFGScanDroid) - 扫描CFG并将其与恶意应用程序的CFG进行比较
1. [Madrolyzer](https://github.com/maldroid/maldrolyzer) - 提取可操作的数据，如 C&C、电话号码等。
1. [ConDroid](https://github.com/JulianSchuette/ConDroid) - 执行应用程序的符号+具体执行的组合
1. [DroidRA](https://github.com/serval-snt-uni-lu/DroidRA)
1. [RiskInDroid](https://github.com/ClaudiuGeorgiu/RiskInDroid) - 一种根据 Android 应用程序的权限计算风险的工具，提供在线演示。
1. [SUPER](https://github.com/SUPERAndroidAnalyzer/super) - 安全、统一、强大且可扩展的 Rust Android 分析器
1. [ClassyShark](https://github.com/google/android-classyshark) - 一个独立的二进制检查工具，可以浏览任何 Android 可执行文件并显示重要信息。
1. [StaCoAn](https://github.com/vincentcox/StaCoAn) - 跨平台工具，可帮助开发人员、漏洞赏金猎人和道德黑客对移动应用程序执行静态代码分析。该工具的创建非常注重用户界面的可用性和图形指导。
1. [JAADAS](https://github.com/flankerhqd/JAADAS) - 联合过程内和过程间程序分析工具，用于查找 Android 应用程序中的漏洞，基于 Soot 和 Scala 构建
1. [Quark-Engine](https://github.com/quark-engine/quark-engine) - 混淆忽略的 Android 恶意软件评分系统
1. [一步反编译](https://github.com/b-mueller/apkx) - 懒人之Android APK反编译
1. [APKLeaks](https://github.com/dwisiswant0/apkleaks) - 扫描 APK 文件中的 URI、端点和机密。
1. [Mobile Audit](https://github.com/mpast/mobileAudit) - 用于执行静态分析和检测 Android APK 中的恶意软件的 Web 应用程序。
1. [Detekt](https://github.com/detekt/detekt) - Kotlin 静态代码分析
1. [APKdevastate](https://github.com/rafigk2v9c/APKdevastate/) - 针对 RAT 创建的 APK 有效负载的高级分析软件。
1. ~~[Smali CFG生成器](https://github.com/EugenioDelfa/Smali-CFGs)~~
1. ~~[PSU的几个工具](http://siis.cse.psu.edu/tools.html)~~
1. ~~[SPARTA](https://www.cs.washington.edu/sparta) - 验证（证明）应用程序满足信息流安全策略；建立在[Checker框架](https://types.cs.washington.edu/checker-framework/)~~

### 应用程序漏洞扫描程序

1. [QARK](https://github.com/linkedin/qark/) - LinkedIn 提供的 QARK 供应用程序开发人员扫描应用程序是否存在安全问题
1. [AndroBugs](https://github.com/AndroBugs/AndroBugs_Framework)
1. [Nogotofail](https://github.com/google/nogotofail)
1. [Ostorlab](https://ostorlab.co) - Ostorlab 免费版扫描以下应用程序：Android playstore、iOS Appstore、华为 AppGallery
1. ~~[Devknox](https://devknox.io/) - 用于构建安全 Android 应用程序的 IDE 插件。不再维护了~~

### 动态分析工具

1. [Android DBI框架](http://www.mulliner.org/blog/blosxom.cgi/security/androiddbiv02.html)
1. [Androl4b](https://github.com/sh4hin/Androl4b) - 用于评估 Android 应用程序、逆向工程和恶意软件分析的虚拟机
1. [House](https://github.com/nccgroup/house)- House：带有 Web GUI 的运行时移动应用程序分析工具包，由 Frida 提供支持，用 Python 编写。
1. [Mobile-Security-Framework MobSF](https://github.com/MobSF/Mobile-Security-Framework-MobSF) - 移动安全框架是一款智能、一体式开源移动应用程序 (Android/iOS) 自动化笔测试框架，能够执行静态、动态分析和 Web API 测试。
1. [Droidbox](https://github.com/pjlantz/droidbox)
1.【德罗泽】(https://github.com/mwrlabs/drozer)
1. [Xposed](https://forum.xda-developers.com/xposed/xposed-installer-versions-changelog-t2714053) - 相当于进行基于存根的代码注入，但无需对二进制文件进行任何修改
1. [Inspeckage](https://github.com/ac-pm/Inspeckage) - Android Package Inspector - 使用 API 挂钩进行动态分析、启动未导出的活动等。 （Xpose模块）
1. [Android Hooker](https://github.com/AndroidHooker/hooker) - 动态Java代码检测（需要Substrate框架）
1. [ProbeDroid](https://github.com/ZSShen/ProbeDroid) - 动态Java代码检测
1. [DECAF](https://github.com/sycurelab/DECAF) - 基于 QEMU 的动态可执行代码分析框架（DroidScope 现在是 DECAF 的扩展）
1. [CuckooDroid](https://github.com/idanr1986/cuckoo-droid) - Cuckoo 沙箱的 Android 扩展
1. [Mem](https://github.com/MobileForensicsResearch/mem) - Android内存分析（需要root）
1. [Crowdroid](http://www.ida.liu.se/labs/rtslab/publications/2011/spsm11-burguera.pdf) – 找不到实际的工具
1. [AuditdAndroid](https://github.com/nwhusted/AuditdAndroid) –auditd 的 Android 端口，不再积极开发
1. [Android 安全评估框架](https://code.google.com/p/asef/) - 不再积极开发
1. [Aurasium](https://github.com/xurubin/aurasium) – 通过字节码重写和就地引用监控对 Android 应用程序实施实用的安全策略。
1. [Android Linux 内核模块](https://github.com/strazzere/android-lkms)
1. [StaDynA](https://github.com/zyrikby/StaDynA) - 在存在动态代码更新功能（动态类加载和反射）的情况下支持安全应用程序分析的系统。该工具结合了 Android 应用程序的静态和动态分析，以揭示隐藏/更新的行为并利用此信息扩展静态分析结果。
1. [DroidAnalytics](https://github.com/zhengmin1989/DroidAnalytics) - 不完整
1. [Vezir Project](https://github.com/oguzhantopgul/Vezir-Project) - 用于移动应用程序渗透测试和移动恶意软件分析的虚拟机
1. [MARA](https://github.com/xtiankisutsa/MARA_Framework) - 移动应用逆向工程与分析框架
1. [Taintdroid](http://appanalysis.org) - 需要 AOSP 编译
1. [ARTist](https://artist.cispa.saarland) - 一个灵活的开源工具和混合分析框架，适用于 Android 应用程序和 Android 的 Java 中间件。它基于 Android 运行时 (ART) 编译器，并在设备上编译期间修改代码。
1. [Android恶意软件沙箱](https://github.com/Areizen/Android-Malware-Sandbox)
1. [AndroPyTool](https://github.com/alexMyG/AndroPyTool) - 从Android APK中提取静态和动态特征的工具。它结合了不同的知名Android应用程序分析工具，例如DroidBox、FlowDroid、Strace、AndroGuard和VirusTotal分析。
1. [Runtime Mobile Security (RMS)](https://github.com/m0bilesecurity/RMS-Runtime-Mobile-Security) - 是一个功能强大的 Web 界面，可帮助您在运行时操作 Android 和 iOS 应用程序
1. [PAPIMonitor](https://github.com/Dado1513/PAPIMonitor) – PAPIMonitor（适用于 Android 应用程序的 Python API 监视器）是一个基于 Frida 的 Python 工具，用于在应用程序执行期间监视用户选择的 API。
1. [Android_application_analyzer](https://github.com/NotSoSecure/android_application_analyzer) - 该工具用于分析本地存储中Android应用程序的内容。
1. [Decompiler.com](https://www.decompiler.com/) - 在线APK和Java反编译器
1. [friTap](https://github.com/fkie-cad/friTap)- 拦截与 Frida 的 SSL/TLS 连接；允许在 Android 上实时提取 TLS 密钥并将 TLS 有效负载解密为 PCAP。
1. [HacknDroid](https://github.com/RaffaDNDM/HacknDroid) - 一款旨在自动化各种移动应用程序渗透测试 (MAPT) 任务并促进与 Android 设备交互的工具。
1. [adbsploit](https://github.com/mesquidar/adbsploit) - 通过ADB利用设备的工具
1. [Brida](https://github.com/federicodotta/Brida) - Burp Suite 扩展，作为 Burp 和 Frida 之间的桥梁，允许您使用和操作应用程序自己的方法，同时篡改应用程序及其后端服务/服务器之间交换的流量。
1. [MPT](https://github.com/ByteSnipers/mobile-pentest-toolkit) - MPT (Mobile Pentest Toolkit) 是 Android 渗透测试工作流程的必备解决方案。该工具允许您自动执行安全任务。
1. [Andriller](https://github.com/den4uk/andriller) - 软件实用程序，包含一系列适用于智能手机的取证工具。它从 Android 设备执行只读、取证合理、非破坏性的采集。
1. [Mira](https://github.com/vwww-droid/Mira) - 针对第三方 Android 和 iOS 应用程序的运行时保护分析平台，使 AI 能够使用主机应用程序端 shell、Java、Native 和 Frida 功能进行环境风险检测和强化验证。
1. ~~[AppUse](https://appsec-labs.com/AppUse/) – 渗透测试的自定义构建~~
1. ~~[Appie](https://manifestsecurity.com/appie/) - Appie 是一个已预先配置为 Android 渗透测试环境的软件包。它完全便携，可以通过 USB 记忆棒或智能手机携带。这是 Android 应用程序安全评估所需的所有工具的一站式答案，也是现有虚拟机的绝佳替代方案。~~
1. ~~[Android Tamer](https://androidtamer.com/) - Android安全专业人员的虚拟/实时平台~~
1. ~~[Android恶意软件分析工具包](http://www.mobilemalware.com.br/amat/download.html) - (Linux发行版) 早些时候，它曾经是一个[在线分析器](http://dunkelheit.com.br/amat/analysis/index_en.php)~~
1. ~~[Android逆向工程](https://redmine.honeynet.org/projects/are/wiki) – ARE（android逆向工程）不再处于积极开发状态~~
1. ~~[ViaLab社区版](https://www.nowsecure.com/blog/2014/09/09/introducing-vialab-community-edition/)~~
1. ~~[水星](https://labs.mwrinfosecurity.com/tools/2012/03/16/mercury/)~~
1. ~~[Cobradroid](https://thecobraden.com/projects/cobradroid/) – 用于恶意软件分析的自定义图像~~

### 逆向工程

1. [Smali/Baksmali](https://github.com/JesusFreke/smali) – apk反编译
1. [smali 文件的 emacs 语法着色](https://github.com/strazzere/Emacs-Smali)
1. [smali文件的vim语法着色](http://codetastrophe.com/smali.vim)
1. [AndBug](https://github.com/swdunlop/AndBug)
1. [Androguard](https://github.com/androguard/androguard) – 功能强大，与其他工具集成良好
1. [Apktool](https://github.com/iBotPeaches/Apktool) – 对于编译/反编译非常有用（使用 smali）
1. [Android开发框架](https://github.com/appknox/AFE)
1. [绕过IPC的签名和权限检查](https://github.com/iSECPartners/Android-KillPermAndSigChecks)
1. [Android OpenDebug](https://github.com/iSECPartners/Android-OpenDebug) – 使设备上的任何应用程序可调试（使用 Cydia Substrate）。
1. [Dex2Jar](https://github.com/pxb1988/dex2jar) - dex 到 jar 转换器
1. [Enjarify](https://github.com/google/enjarify) - 来自 Google 的 dex 到 jar 转换器
1. [Dedexer](https://sourceforge.net/projects/dedexer/)
1. [菲诺](https://github.com/sysdream/fino)
1. [Frida](https://www.frida.re/) - 注入 JavaScript 来探索应用程序及其 [GUI 工具](https://github.com/antojoseph/diff-gui)
1. [Indroid](https://bitbucket.org/aseemjakhar/indroid) – 线程注入套件
1. [Introspy](https://github.com/iSECPartners/Introspy-Android)
1. [Jad]( https://varaneckas.com/jad/) - Java 反编译器
1. [JD-GUI](https://github.com/java-decompiler/jd-gui) - Java反编译器
1. [CFR](http://www.benf.org/other/cfr/) - Java反编译器
1. [Krakatau](https://github.com/Storyyeller/Krakatau) - Java反编译器
1. [FernFlower](https://github.com/fesh0r/fernflower) - Java反编译器
1. [Redexer](https://github.com/plum-umd/redexer) – apk操作
1. [简化Android反混淆器](https://github.com/CalebFenton/simplify)
1. [字节码查看器](https://github.com/Konloch/bytecode-viewer)
1. [Radare2](https://github.com/radare/radare2)
1. [Jadx](https://github.com/skylot/jadx)
1. [Dwarf](https://github.com/iGio90/Dwarf) - 用于逆向工程的 GUI
1. [Andromeda](https://github.com/secrary/Andromeda) - 另一个基本的命令行逆向工程工具
1. [apk-mitm](https://github.com/shroudedcode/apk-mitm) - 准备 Android APK 文件以进行 HTTPS 检查的 CLI 应用程序
1. [Noia](https://github.com/0x742/noia) - 简单的Android应用程序沙箱文件浏览器工具
1. [Obfuscapk](https://github.com/ClaudiuGeorgiu/Obfuscapk) — Obfuscapk 是一个模块化 Python 工具，用于混淆 Android 应用程序，而不需要其源代码。
1. [ARMANDroid](https://github.com/Mobile-IoT-Security-Lab/ARMANDroid) - ARMAND（通过多模式防重新打包，基于本机检测的防篡改）是一种新颖的防篡改保护方案，它将逻辑炸弹和 AT 检测节点直接嵌入到 apk 文件中，而不需要其源代码。
1. [MVT（移动验证工具包）](https://github.com/mvt-project/mvt) - 一系列实用程序，用于简化和自动化收集取证跟踪的过程，有助于识别 Android 和 iOS 设备的潜在危害
1. [Dexmod](https://github.com/google/dexmod) - 一个工具，用于举例说明在 DEX（Dalvik 可执行文件）文件中修补 Dalvik 字节码并协助 Android 应用程序的静态分析。
1. [odex-patcher](https://github.com/giacomoferretti/odex-patcher) - 通过修补 OAT 文件运行任意代码
1. [PhoneSpolit-Pro](https://github.com/AzeemIdrisi/PhoneSploit-Pro) - 一款一体化黑客工具，可使用 ADB 和 Metasploit Framework 远程利用 Android 设备来获取 Meterpreter 会话。
1. [APKLab](https://github.com/APKLab/APKLab) - VS code分析APK的插件
1. ~~[IntentSniffer](https://www.nccgroup.com/us/our-research/intent-sniffer/)~~
1. ~~[Procyon](https://bitbucket.org/mstrobel/procyon/wiki/Java%20Decompiler) - Java反编译器~~
1. ~~[Smali查看器](http://blog.avlyun.com/wp-content/uploads/2014/04/SmaliViewer.zip)~~
1. ~~[ZjDroid](https://github.com/BaiduSecurityLabs/ZjDroid)~~, ~~[fork/mirror](https://github.com/yangbean9/ZjDroid)~~
1. ~~[Dare](http://siis.cse.psu.edu/dare/index.html) – .dex 到 .class 转换器~~

### 模糊测试

1. [Radamsa 模糊器](https://github.com/anestisb/radamsa-android)
1. [honggfuzz](https://github.com/google/honggfuzz)
1. [Melkor ELF 模糊器的 Android 端口](https://github.com/anestisb/melkor-android)
1. [Android 媒体模糊测试框架](https://github.com/fuzzing/MFFA)
1. [AndroFuzz](https://github.com/jonmetz/AndroFuzz)
1. [QuarksLab 的 Android 模糊测试](https://github.com/quarkslab/android-fuzzing)
1. ~~[IntentFuzzer](https://www.nccgroup.trust/us/about-us/resources/intent-fuzzer/)~~

### 应用程序重新打包检测器

1. [FSquaDRA](https://github.com/zyrikby/FSquaDRA) - 一个基于应用程序资源哈希比较来检测重新打包的 Android 应用程序的工具。

### 市场爬行者

1. [Google Play 爬虫（Java）](https://github.com/Akdeniz/google-play-crawler)
1. [Google Play 爬虫（Python）](https://github.com/egirault/googleplay-api)
1. [Google Play 爬虫（Node）](https://github.com/dweinstein/node-google-play) - 获取应用详细信息并从官方 Google Play 商店下载应用。
1. [Aptoide下载器(Node)](https://github.com/dweinstein/node-aptoide) - 从Aptoide第三方Android市场下载应用程序
1. [Appland下载器(Node)](https://github.com/dweinstein/node-appland) - 从Appland第三方Android市场下载应用程序
1. [PlaystoreDownloader](https://github.com/ClaudiuGeorgiu/PlaystoreDownloader) - PlaystoreDownloader 是一个直接从 Google Play 商店下载 Android 应用程序的工具。初始（一次性）配置后，可以通过指定应用程序包名称来下载应用程序。
1. [APK 下载器](https://apkcombo.com/apk-downloader/) 在线服务，用于从 Play 商店下载针对特定 Android 设备配置的 APK
1. ~~[Apkpure](https://apkpure.com/) - 在线apk下载器。另外，它还提供了自己的应用程序可供下载。~~

### 其他工具

1. [smalihook](http://androidcracking.blogspot.com/2011/03/original-smalihook-java-source.html)
1. [AXMLPrinter2](http://code.google.com/p/android4me/downloads/detail?name=AXMLPrinter2.jar) - 将二进制 XML 文件转换为人类可读的 XML 文件
1. [adb 自动完成](https://github.com/mbrubeck/android-completion)
1. [mitmproxy](https://github.com/mitmproxy/mitmproxy)
1. [dockerfile/androguard](https://github.com/dweinstein/dockerfile-androguard)
1. [Android 漏洞测试套件](https://github.com/AndroidVTS/android-vts) - android-vts 扫描设备是否存在一组漏洞
1. [AppMon](https://github.com/dpnishant/appmon) - AppMon 是一个自动化框架，用于监控和篡改本机 macOS、iOS 和 Android 应用程序的系统 API 调用。它是基于弗里达。
1. [Internal Blue](https://github.com/seemoo-lab/internalblue) - 基于Broadcom蓝牙控制器逆向工程的蓝牙实验框架
1. [Android 移动设备强化](https://github.com/SecTheTech/AMDH) - AMDH 扫描并强化设备的设置，并根据权限列出有害的已安装应用程序。
1. [NullKia](https://github.com/bad-antics/nullkia) - 全面的移动安全框架，支持 18 家制造商提供基带开发、蜂窝安全、TEE/TrustZone 研究和 BootROM 提取工具。
1. [Firmware Extractor](https://github.com/AndroidDumps/Firmware_extractor) - 将给定的存档提取到图像
1. [在 MediaTek bootloader 上提供任意代码执行的 ARMv7 有效负载](https://github.com/R0rt1z2/kaeru)
1. [DroidGround](https://github.com/SECFORCE/droidground) - Android CTF 挑战的灵活游乐场
1. [sundaysec/Android-Exploits](https://github.com/sundaysec/Android-Exploits) - android 漏洞和黑客的集合
1. ~~[Android设备安全数据库](https://www.android-device-security.org/client/datatable) - Android设备安全特性数据库~~
1. ~~[快速参考操作码表](http://ww38.xchg.info/corkami/opcodes_tables.pdf)~~
1. ~~[APK-Downloader](http://codekiem.com/2012/02/24/apk-downloader/)~~ - 现在似乎已经死了
1. ~~[Dalvik操作码](http://pallergabor.uw.hu/androidblog/dalvik_opcodes.html)~~

### 易受攻击的应用程序练习

1. [该死的不安全漏洞应用程序（DIVA）](https://github.com/payatu/diva-android)
1. [Vuldroid](https://github.com/jaiswalakshansh/Vuldroid)
1. [ExploitMe Android 实验室](http://securitycompass.github.io/AndroidLabs/setup.html)
1. [GoatDroid](https://github.com/jackMannino/OWASP-GoatDroid-Project)
1. [Android InsecureBank](https://github.com/dineshshetty/Android-InsecureBankv2)
1. [Insecureshop](https://github.com/optiv/insecureshop)
1. [过度安全的易受攻击的 Android 应用程序 (OVAA)](https://github.com/oversecured/ovaa)
1.【受伤的安卓-CTF】(https://github.com/B3nac/InjuredAndroid)

## 学术/研究/出版物/书籍

### 研究论文

1. [利用数据库](https://www.exploit-db.com/papers/)
1. [Android安全相关演示](https://github.com/jacobsoo/AndroidSlides)
1.【静态分析论文好合集】(https://tthtlc.wordpress.com/2011/09/01/static-analysis-of-android-applications/)

### 书籍

1. [SEI CERT Android 安全编码标准](https://wiki.sei.cmu.edu/confluence/display/android/Android+Secure+Coding+Standard)

### 其他

1.【OWASP移动安全测试指导手册】(https://github.com/OWASP/owasp-mstg)
1. [doridori/Android-Security-Reference](https://github.com/doridori/Android-Security-Reference)
1. [android应用程序安全检查表](https://github.com/b-mueller/android_app_security_checklist)
1. [移动应用 Pentest 备忘单](https://github.com/tanprathan/MobileApp-Pentest-Cheatsheet)
1. [Daniele Altomare 的 Android 逆向工程 101（网络存档链接）](https://web.archive.org/web/20180721134044/http://www.fasteque.com:80/android-reverse-engineering-101-part-1/)
1. ~~[移动安全阅览室](https://mobile-security.zeef.com) - 一个阅览室，包含有关移动渗透测试、移动恶意软件、移动取证以及各种移动安全相关主题的分类良好的技术阅读材料~~

## 漏洞利用/漏洞/错误

### 列表

1. [Android安全公告](https://source.android.com/security/bulletin/)
1. [Android报告的安全漏洞](https://www.cvedetails.com/vulnerability-list/vendor_id-1224/product_id-19997/Google-Android.html)
1. [2016 年 OWASP 移动排名前 10 名](https://www.owasp.org/index.php/Mobile_Top_10_2016-Top_10)
1. [利用数据库](https://www.exploit-db.com/search/?action=search&q=android) - 点击搜索
1. [漏洞Google文档](https://docs.google.com/spreadsheet/pub?key=0Am5hHW4ATym7dGhFU1A4X2lqbUJtRm1QSWNRc3E0UlE&single=true&gid=0&output=html)
1. [Google Android 安全团队对潜在有害应用程序（恶意软件）的分类](https://source.android.com/security/reports/Google_Android_Security_PHA_classifications.pdf)
1. ~~[Android设备安全补丁状态](https://kb.androidtamer.com/Device_Security_Patch_tracker/)~~

### 恶意软件

1. [androguard - 数据库 Android 恶意软件 wiki](https://code.google.com/p/androguard/wiki/DatabaseAndroidMalwares)
1. [Android 恶意软件 Github 存储库](https://github.com/ashishb/android-malware)
1. [Android 恶意软件基因组计划](http://www.malgenomeproject.org/) - 包含 1260 个恶意软件样本，分为 49 个不同的恶意软件家族，免费用于研究目的。
1. [Contagio 移动恶意软件迷你转储](http://contagiominidump.blogspot.com)
1. [德雷宾](https://www.sec.tu-bs.de/~danarp/drebin/)
1. [Hudson Rock](https://www.hudsonrock.com/threat-intelligence-cybercrime-tools) - 一个免费的网络犯罪情报工具集，可以指示特定的 APK 包是否在 Infostealer 恶意软件攻击中受到损害。
1. [Kharon 恶意软件数据集](http://kharon.gforge.inria.fr/dataset/) - 7 个经过逆向工程并记录的恶意软件
1. [Android 广告软件和一般恶意软件数据集](https://www.unb.ca/cic/datasets/android-adware.html)
1. [AndroZoo](https://androzoo.uni.lu/) - AndroZoo 是一个不断增长的 Android 应用程序集合，来自多个来源，包括官方 Google Play 应用程序市场。
1. ~~[Android PRAGuard 数据集](http://pralab.diee.unica.it/en/AndroidPRAGuardDataset) - 该数据集包含 10479 个样本，是通过使用七种不同的混淆技术对 MalGenome 和 Contagio Minidump 数据集进行混淆而获得的。~~
1.~~[佩服](http://admire.necst.it/)~~

### 赏金计划

1. [Android安全奖励计划](https://www.google.com/about/appsecurity/android-rewards/)

### 如何报告安全问题

1. [Android - 报告安全问题](https://source.android.com/security/overview/updates-resources.html#report-issues)
1. [Android Reports and Resources](https://github.com/B3nac/Android-Reports-and-Resources) - Android Hackerone披露的报告和其他资源列表

## 贡献

随时欢迎您的贡献！

## 📖 引文

```bibtex
@misc{
  author = {Ashish Bhatia - ashishb.net},
  title = {The most comprehensive collection of Android Security related resources},
  year = {2025},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/ashishb/android-security-awesome}}
}
```

该存储库已被[10多篇论文]引用(https://scholar.google.com/scholar?q=github.com%2Fashishb%2Fandroid-security-awesome)
