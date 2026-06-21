# 很棒的模糊测试 [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> [模糊测试](https://en.wikipedia.org/wiki/Fuzzing) 或模糊测试是一种自动化软件测试技术，涉及提供无效、意外或随机数据作为计算机程序的输入。然后监视程序是否存在异常，例如崩溃、内置代码断言失败或潜在的内存泄漏。通常，模糊器用于测试采用结构化输入的程序。

用于安全测试的出色模糊测试的精选参考列表。此外，还有一系列免费提供的学术论文、工具等。

您最喜欢的工具或您自己的论文没有列出？分叉并创建拉取请求来添加它！


## 内容

- [Books](#books)
- [Talks](#talks)
- [Papers](#papers)
- [Tools](#tools)
- [Contribute](#contribute)


## 书籍
- [针对机器进行模糊测试：使用 QEMU 上的模拟 IoT 设备自动进行漏洞研究](https://a.co/d/0bXISQgZ) (2023)
- [Fuzzing-101](https://github.com/antonio-morales/Fuzzing101)
- [模糊测试书](https://www.fuzzingbook.org/) (2019)
- [模糊测试的艺术、科学和工程：调查](https://ieeexplore.ieee.org/document/8863940) (2019) - 实际上，这篇文档是一篇论文，但它包含比任何其他书更重要和本质的内容。
- [用于软件安全测试和质量保证的模糊测试，第二版](https://www.amazon.com/Fuzzing-Software-Security-Testing-Assurance/dp/1608078507/) (2018)
- [模糊测试：暴力漏洞发现，第一版](https://www.amazon.com/Fuzzing-Brute-Force-Vulnerability-Discovery/dp/0321446119/) (2007)
- [开源模糊测试工具，第一版](https://www.amazon.com/Open-Source-Fuzzing-Tools-Rathaus/dp/1597491950/) (2007)


## 会谈
- [Fuzzing Labs - Patrick Ventuzelo](https://www.youtube.com/channel/UCGD1Qt2jgnFRjrfAITGdNfQ) - YouTube。
- [Effective File Format Fuzzing](https://youtu.be/qTTwqFRD1H8) - 2016 年欧洲黑帽。
- [Adventures in Fuzzing](https://www.youtube.com/watch?v=SngK4W4tVc0) - 2018 年纽约大学演讲。
- [Fuzzing with AFL](https://www.youtube.com/watch?v=DFQT1YxvpDo) - 2018 年国家数据中心会议。

## 论文
为了实现明确的范围，我选择纳入来自 4 个顶级主要安全会议（2008-2025）的模糊测试出版物：(i) 网络和分布式系统安全研讨会 (NDSS)、(ii) IEEE 安全和隐私研讨会 (S&P)、(iii) USENIX 安全研讨会 (USEC) 和 (iv) ACM 计算机和通信安全会议 (CCS)。

> **注意：** 根据标题是否包含关键字“fuzz”来选择论文。如果一篇论文与模糊测试相关，但其标题中不包含“模糊测试”，则该论文可能已被错过。在这种情况下，请打开 [Pull Request](https://github.com/cpuu/awesome-fuzzing/pulls)，我们将对其进行审核以将其包含在内。


### 网络与分布式系统安全研讨会（NDSS）

<详细><摘要>2025年（10篇论文）</摘要>

- [通过 API 关系演化进行自动库模糊测试，2025](https://www.ndss-symposium.org/wp-content/uploads/2025-750-paper.pdf)
- [具有多维输入和基于对称性的反馈修剪的分布式系统的黑盒模糊测试，2025](https://www.ndss-symposium.org/wp-content/uploads/2025-1912-paper.pdf)
- [DUMPLING：细粒度差分 JavaScript 引擎模糊测试，2025](https://www.ndss-symposium.org/wp-content/uploads/2025-1411-paper.pdf)
- [FUZZUER：在 EDK-2 上启用 UEFI 接口模糊测试，2025](https://www.ndss-symposium.org/wp-content/uploads/2025-400-paper.pdf)
- [ICSQuartz：工业控制系统的扫描周期感知和供应商无关的模糊测试，2025](https://www.ndss-symposium.org/wp-content/uploads/2025-795-paper.pdf)
- [MALintent：适用于 Android 的覆盖引导意图模糊测试框架，2025](https://www.ndss-symposium.org/wp-content/uploads/2025-125-paper.pdf)
- [Moneta：通过调用体内执行状态进行体外 GPU 驱动程序模糊测试，2025 年](https://www.ndss-symposium.org/wp-content/uploads/2025-218-paper.pdf)
- [MSan：在模糊测试期间有效检测未初始化的内存错误，2025](https://www.ndss-symposium.org/wp-content/uploads/2025-1133-paper.pdf)
- [Truman：构建从操作系统驱动程序到模糊虚拟设备的设备行为模型，2025 年](https://www.ndss-symposium.org/wp-content/uploads/2025-301-paper.pdf)
- [TWINFUZZ：视频硬件加速堆栈的差异测试，2025](https://www.ndss-symposium.org/wp-content/uploads/2025-526-paper.pdf)

</详情>

<详细信息><摘要>2024年（7篇论文）</摘要>

- [DeepGo：预测定向灰盒模糊测试，2024](https://www.ndss-symposium.org/wp-content/uploads/2024-514-paper.pdf)
- [EnclaveFuzz：查找 SGX 应用程序中的漏洞，2024 年](https://www.ndss-symposium.org/wp-content/uploads/2024-819-paper.pdf)
- [大型语言模型引导的协议模糊测试，2024](https://www.ndss-symposium.org/wp-content/uploads/2024-556-paper.pdf)
- [MOCK：利用上下文感知依赖性优化内核模糊突变，2024 年](https://www.ndss-symposium.org/wp-content/uploads/2024-131-paper.pdf)
- [预测性上下文相关模糊测试，2024](https://www.ndss-symposium.org/wp-content/uploads/ndss2024_f113_paper.pdf)
- [ReqsMiner：使用基于语法的模糊测试自动发现 CDN 转发请求不一致和 DoS 攻击，2024 年](https://www.ndss-symposium.org/wp-content/uploads/2024-31-paper.pdf)
- [ShapFuzz：通过 Shapley 引导字节选择进行高效模糊测试，2024 年](https://www.ndss-symposium.org/wp-content/uploads/2024-134-paper.pdf)

</详情>

<详细信息><摘要>2023年（4篇论文）</摘要>

- [达尔文：适者生存模糊变异，2023](https://www.ndss-symposium.org/wp-content/uploads/2023-159-paper.pdf)
- [FUZZILLI：JavaScript JIT 编译器漏洞的模糊测试，2023 年](https://www.ndss-symposium.org/wp-content/uploads/2023-290-paper.pdf)
- [LOKI：用于实施区块链共识协议的状态感知模糊测试框架，2023 年](https://www.ndss-symposium.org/wp-content/uploads/2023-78-paper.pdf)
- [没有语法，没有问题：在没有系统调用描述的情况下模糊化 Linux 内核，2023 年](https://www.ndss-symposium.org/wp-content/uploads/2023-688-paper.pdf)

</详情>

<详细信息><摘要>2022年（4篇论文）</摘要>

- [无需硬件设备和模拟器的语义知情驱动程序模糊测试，2022](https://www.ndss-symposium.org/wp-content/uploads/2022-345-paper.pdf)
- [MobFuzz：灰盒模糊测试中的自适应多目标优化，2022](https://www.ndss-symposium.org/wp-content/uploads/2022-314-paper.pdf)
- [用于数据争用检测的上下文敏感和定向并发模糊测试，2022](https://www.ndss-symposium.org/wp-content/uploads/2022-296-paper.pdf)
- [EMS：基于覆盖范围的模糊测试的历史驱动突变，2022](https://www.ndss-symposium.org/wp-content/uploads/2022-162-paper.pdf)

</详情>

<详细信息><摘要>2021年（4篇论文）</摘要>

- [WINNIE：利用 Harness Synthesis 和快速克隆对 Windows 应用程序进行模糊测试，2021 年](https://taesoo.kim/pubs/2021/jung:winnie.pdf)
- [基于强化学习的灰盒模糊测试分层种子调度，2021](https://www.cs.ucr.edu/~heng/pubs/afl-hier.pdf)
- [PGFUZZ：政策引导的机器人车辆模糊测试，2021](https://beerkay.github.io/papers/Berkay2021PGFuzzNDSS.pdf)
- [Favocado：使用语义正确的测试用例模糊 JavaScript 引擎的绑定代码，2021](https://www.ndss-symposium.org/wp-content/uploads/ndss2021_6A-2_24224_paper.pdf)

</详情>

<详细><摘要>2020年（4篇论文）</摘要>

- [HFL：Linux 内核上的混合模糊测试，2020](https://www.unexploitable.systems/publication/kimhfl/)
- [HotFuzz：通过引导式微模糊测试发现算法拒绝服务漏洞，2020 年](https://www.researchgate.net/publication/339164746_HotFuzz_Discovering_Algorithmic_Denial-of-Service_Vulnerabilities_Through_Guided_Micro-Fuzzing)
- [HYPER-CUBE：高维虚拟机管理程序模糊测试，2020](https://www.syssec.ruhr-uni-bochum.de/media/emma/veroeffentlichungen/2020/02/07/Hyper-Cube-NDSS20.pdf)
- [并非所有覆盖率测量都相同：2020 年通过覆盖率核算对输入优先级进行模糊测试](https://www.ndss-symposium.org/wp-content/uploads/2020/02/24422.pdf)

</详情>

<详细><摘要>2019年（5篇论文）</摘要>

- [CodeAlchemist：语义感知代码生成以查找 JavaScript 引擎中的漏洞，2019 年](https://daramg.gift/paper/han-ndss2019.pdf)
- [PeriScope：针对硬件操作系统边界的有效探测和模糊测试框架，2019 年](https://people.cs.kuleuven.be/~stijn.volckaert/papers/2019_NDSS_PeriScope.pdf)
- [REDQUEEN：使用输入到状态对应进行模糊测试，2019](https://www.syssec.ruhr-uni-bochum.de/media/emma/veroeffentlichungen/2018/12/17/NDSS19-Redqueen.pdf)
- [以我的方式发送最困难的问题：混合模糊测试的概率路径优先级，2019](https://www.cs.ucr.edu/~heng/pubs/digfuzz_ndss19.pdf)
- [语音识别后的生活：模糊语音助手应用程序的语义误解，2019](https://www.ndss-symposium.org/wp-content/uploads/2019/02/ndss2019_08-4_Zhang_paper.pdf)

</详情>

<详情><摘要>2018年（4篇论文）</摘要>

- [INSTRIM：用于覆盖引导模糊测试的轻量级仪器，2018](https://www.ndss-symposium.org/wp-content/uploads/2018/07/bar2018_14_Hsu_paper.pdf)
- [IoTFuzzer：通过基于应用程序的模糊测试发现物联网中的内存损坏，2018 年](http://wp.internetsociety.org/ndss/wp-content/uploads/sites/25/2018/02/ndss2018_01A-1_Chen_paper.pdf)
- [你损坏的并不是你崩溃的：模糊测试嵌入式设备的挑战，2018](http://s3.eurecom.fr/docs/ndss18_muench.pdf)
- [增强大规模应用程序的内存错误检测和模糊测试，2018](https://lifeasageek.github.io/papers/han:meds.pdf)

</详情>

<详情><摘要>2017年（2篇论文）</摘要>

- [Vuzzer：应用程序感知的进化模糊测试，2017](https://www.ndss-symposium.org/ndss2017/ndss-2017-programme/vuzzer-application-aware-evolutionary-fuzzing/)
- [DELTA：软件定义网络的安全评估框架，2017 年](https://www.ndss-symposium.org/wp-content/uploads/2017/09/ndss201702A-1LeePaper.pdf)

</详情>

<详情><摘要>2016年（1篇论文）</摘要>

- [Driller：通过选择性符号执行增强模糊测试，2016 年](https://cancer.shtech.org/wiki/uploads/2016---NDSS---driller-augmenting-fuzzing-through-selective-symbolic-execution.pdf)

</详情>

<详情><摘要>2008年（1篇论文）</摘要>

- [自动白盒模糊测试，2008](https://www.ndss-symposium.org/wp-content/uploads/2017/09/Automated-Whitebox-Fuzz-Testing-paper-Patrice-Godefroid.pdf)

</详情>


### IEEE 安全与隐私研讨会 (IEEE S&P)

<详细信息><摘要>2025年（7篇论文）</摘要>

- [CHIMERA：用于多平面错误检测和漏洞发现的模糊 P4 网络基础设施，2025 年](https://www.computer.org/csdl/proceedings-article/sp/2025/223600c865/26hiVb0gXUA)
- [FirmRCA：通过基于事件的高效故障定位对 ARM 嵌入式固件进行后模糊分析，2025 年](https://www.computer.org/csdl/proceedings-article/sp/2025/223600a002/21B7PVDny6I)
- [模糊测试与基于 LLM 的代理的结合：用于越狱文本到图像生成模型的自动化高效框架，2025 年](https://www.computer.org/csdl/proceedings-article/sp/2025/223600a336/26hiTETXKow)
- [HouseFuzz：用于基于 Linux 的固件中的漏洞检测的服务感知灰盒模糊测试，2025](https://www.computer.org/csdl/proceedings-article/sp/2025/223600d507/26hiVy3bGHm)
- [Predator：用于高效漏洞验证的定向 Web 应用程序模糊测试，2025 年](https://www.computer.org/csdl/proceedings-article/sp/2025/223600a066/21B7Ray6BkA)
- [RGFuzz：适用于 WebAssembly 运行时的规则引导模糊器，2025 年](https://www.computer.org/csdl/proceedings-article/sp/2025/223600a003/21B7PWv1JGU)
- [商用基带固件的状态分析和模糊测试，2025](https://www.computer.org/csdl/proceedings-article/sp/2025/223600b120/26EkFox5zyg)

</详情>

<详细信息><摘要>2024年（14篇论文）</摘要>

- [AFGen：应用程序和库的全功能模糊测试，2024 年](https://www.computer.org/csdl/proceedings-article/sp/2024/313000a011/1RjE9PjiDss)
- [Chronos：通过具有瞬态延迟的深度优先级模糊测试来查找实际分布式系统中的超时错误，2024 年](https://www.computer.org/csdl/proceedings-article/sp/2024/313000a109/1Ub23heRtUA)
- [DY 模糊测试：正式的 Dolev-Yao 模型满足加密协议模糊测试，2024 年](https://www.computer.org/csdl/proceedings-article/sp/2024/313000a096/1Ub234bjuWA)
- [一切都有好处：通过可能不变推理进行反例引导的定向模糊测试，2024](https://www.computer.org/csdl/proceedings-article/sp/2024/313000a142/1Ub23ZRRhRu)
- [LABRADOR：针对黑盒物联网设备的响应引导定向模糊测试，2024 年](https://www.computer.org/csdl/proceedings-article/sp/2024/313000a127/1Ub23HQTJ1C)
- [LLMIF：用于模糊物联网设备的增强型大型语言模型，2024 年](https://www.computer.org/csdl/proceedings-article/sp/2024/313000a196/1WPcYnhN15u)
- [前驱感知定向灰盒模糊测试，2024](https://www.computer.org/csdl/proceedings-article/sp/2024/313000a040/1RjEaeMELbq)
- [SATURN：主机-小工具协同 USB 驱动程序模糊测试，2024](https://www.computer.org/csdl/proceedings-article/sp/2024/313000a051/1RjEaqzRsfC)
- [SoK：模糊测试的审慎评估实践，2024](https://www.computer.org/csdl/proceedings-article/sp/2024/313000a137/1Ub23V26Svm)
- [SyzGen++：用于增强内核驱动程序模糊测试的依赖推理，2024 年](https://www.computer.org/csdl/proceedings-article/sp/2024/313000e661/1ZZvBxFudzi)
- [SyzTrust：专为物联网设备设计的可信操作系统上的状态感知模糊测试，2024 年](https://www.computer.org/csdl/proceedings-article/sp/2024/313000a070/1RjEaG9OpTa)
- [Titan：高效的多目标定向灰盒模糊测试，2024](https://www.computer.org/csdl/proceedings-article/sp/2024/313000a059/1RjEaxqvmQ8)
- [大胆探索模糊器未曾涉足的领域：通过 VirtIO 设备查找 Linux 无线堆栈中的错误，2024 年](https://www.computer.org/csdl/proceedings-article/sp/2024/313000a024/1RjEa0y9RMQ)
- [迈向 GPU 上的智能合约模糊测试，2024 年](https://www.computer.org/csdl/proceedings-article/sp/2024/313000a195/1WPcYmDLzKo)

</详情>

<详细信息><摘要>2023年（10篇论文）</摘要>

- [TEEzz：对 COTS Android 设备上的可信应用程序进行模糊测试，2023 年](https://hexhive.epfl.ch/publications/files/23Oakland.pdf)
- [SEGFUZZ：分段线程交错以通过模糊测试发现内核并发错误，2023](https://lifeasageek.github.io/papers/jeong-segfuzz.pdf)
- [RSFuzzer：使用混合模糊测试发现 UEFI 固件中的深层 SMI 处理程序漏洞，2023 年](https://www.computer.org/csdl/proceedings-article/sp/2023/933600b765/1OXH123kRcQ)
- [把错误扔给你的巫师：应用灰盒覆盖引导的变异模糊测试来检测 SQL 和命令注入漏洞，2023 年](https://www.computer.org/csdl/proceedings-article/sp/2023/933600a116/1He7XPiaynS)
- [UTOPIA：使用单元测试自动生成模糊驱动程序，2023](https://www.computer.org/csdl/proceedings-article/sp/2023/933600a746/1OXH6X6Fexi)
- [SelectFuzz：通过选择性路径探索进行高效定向模糊测试，2023](https://www.computer.org/csdl/proceedings-article/sp/2023/933600b050/1OXGOF6jNp6)
- [通过模糊测试寻找规范盲点，2023 年](https://www.computer.org/csdl/proceedings-article/sp/2023/933600c708/1OXH7BohI2Y)
- [ODDFUZZ：通过结构感知定向灰盒模糊测试发现 Java 反序列化漏洞，2023 年](https://www.computer.org/csdl/proceedings-article/sp/2023/933600c726/1OXH0xA0Lrq)
- [VIDEZZO：依赖感知虚拟设备模糊测试，2023](https://www.computer.org/csdl/proceedings-article/sp/2023/933600d228/1OXH4y2HyuI)
- [DEVFUZZ：自动设备模型引导的设备驱动程序模糊测试，2023](https://www.computer.org/csdl/proceedings-article/sp/2023/933600d246/1OXH2Xsv2Du)

</详情>

<详细信息><摘要>2022年（5篇论文）</摘要>

- [PATA：使用路径感知污点分析进行模糊测试，2022](http://www.wingtecher.com/themes/WingTecherResearch/assets/papers/sp22.pdf)
- [Jigsaw：高效且可扩展的路径约束模糊测试，2022](https://www.cs.ucr.edu/~csong/oakland22-jigsaw.pdf)
- [FuzzUSB：USB 小工具堆栈的混合状态模糊测试，2022 年](https://github.com/purseclab/fuzzusb/blob/main/paper/fuzzusb.pdf)
- [通过图中心性分析进行模糊测试的有效种子调度，2022](https://arxiv.org/pdf/2203.12064.pdf)
- [BEACON：具有可证明路径修剪的定向灰盒模糊测试，2022](https://qingkaishi.github.io/public_pdfs/SP22.pdf)

</详情>

<详细信息><摘要>2021年（5篇论文）</摘要>

- [STOCHFUZZ：通过增量和随机重写对剥离的二进制文件进行健全且经济有效的模糊测试，2021](https://www.cs.purdue.edu/homes/zhan3299/res/SP21b.pdf)
- [一个引擎即可模糊所有内容：带有语义验证的通用语言处理器测试，2021 年](https://huhong789.github.io/papers/polyglot-oakland2021.pdf)
- [NTFUZZ：通过静态二进制分析在 Windows 上启用类型感知内核模糊测试，2021](https://softsec.kaist.ac.kr/~jschoi/data/oakland2021.pdf)
- [DIFUZZRTL：用于查找 CPU 错误的差异模糊测试，2021 年](https://lifeasageek.github.io/papers/jaewon-difuzzrtl.pdf)
- [DIANE：识别应用程序中的模糊触发器，为物联网设备生成不受约束的输入，2021 年](https://conand.me/publications/redini-diane-2021.pdf)

</详情>

<详细><摘要>2020年（5篇论文）</摘要>

- [使用保留方面的突变模糊 JavaScript 引擎，2020](https://jakkdu.github.io/pubs/2020/park:die.pdf)
- [IJON：通过模糊测试探索深层状态空间，2020](https://www.syssec.ruhr-uni-bochum.de/media/emma/veroeffentlichungen/2020/02/27/IJON-Oakland20.pdf)
- [Krace：内核文件系统的数据竞赛模糊测试，2020](https://www.cc.gatech.edu/~mxu80/pubs/xu:krace.pdf)
- [Pangolin：增量混合模糊测试与多面体路径抽象，2020](https://qingkaishi.github.io/public_pdfs/SP2020.pdf)
- [RetroWrite：静态检测 COTS 二进制文件以进行模糊测试和清理，2020](https://www.semanticscholar.org/paper/RetroWrite%3A-Statically-Instrumenting-COTS-Binaries-Dinesh-Burow/845cafb153b0e4b9943c6d9b6a7e42c14845a0d6)

</详情>

<详细><摘要>2019年（4篇论文）</摘要>

- [全速模糊测试：通过覆盖范围引导的跟踪减少模糊测试开销，2019](https://www.computer.org/csdl/proceedings-article/sp/2019/666000b122/19skgbGVFEQ)
- [通过二维输入空间探索模糊文件系统，2019](https://www.computer.org/csdl/proceedings-article/sp/2019/666000a594/19skfLYOpaw)
- [NEUZZ：利用神经程序平滑进行高效模糊测试，2019](https://www.computer.org/csdl/proceedings-article/sp/2019/666000a900/19skg5XghG0)
- [Razzer：通过模糊测试查找内核竞争错误，2019](https://www.computer.org/csdl/proceedings-article/sp/2019/666000a296/19skfwZLirm)

</详情>

<详情><摘要>2018年（3篇论文）</摘要>

- [Angora：通过原则搜索进行高效模糊测试，2018](http://web.cs.ucdavis.edu/~hchen/paper/chen2018angora.pdf)
- [CollAFL：路径敏感模糊测试，2018](http://chao.100871.net/papers/oakland18.pdf)
- [T-Fuzz：通过程序转换进行模糊测试，2018](https://nebelwelt.net/publications/files/18Oakland.pdf)

</详情>

<详情><摘要>2017年（1篇论文）</摘要>

- [Skyfire：数据驱动的模糊测试种子生成，2017](https://www.ieee-security.org/TC/SP2017/papers/42.pdf)

</详情>

<详情><摘要>2015年（1篇论文）</摘要>

- [程序自适应突变模糊测试，2015](https://softsec.kaist.ac.kr/~sangkilc/papers/cha-oakland15.pdf)

</详情>

<详情><摘要>2010年（1篇论文）</摘要>

- [TaintScope：一种用于自动软件漏洞检测的校验和定向模糊测试工具，2010 年](https://ieeexplore.ieee.org/abstract/document/5504701)

</详情>



### USENIX 安全

<详细><摘要>2025年（14篇论文）</摘要>

- [AidFuzzer：通过运行时状态识别进行自适应中断驱动的固件模糊测试，2025](https://www.usenix.org/system/files/usenixsecurity25-wang-jianqiang.pdf)
- [ChainFuzz：利用开源供应链中的上游漏洞，2025 年](https://www.usenix.org/system/files/usenixsecurity25-deng.pdf)
- [CoreCrisis：5G 核心网络的威胁引导和情境感知迭代学习和模糊测试，2025 年](https://www.usenix.org/system/files/usenixsecurity25-dong-yilu.pdf)
- [通过分层调度进行有效的定向模糊测试，用于 Web 漏洞检测，2025 年](https://www.usenix.org/system/files/usenixsecurity25-lin-zihan.pdf)
- [Encarsia：通过自动错误注入评估 CPU 模糊器，2025 年](https://www.usenix.org/system/files/usenixsecurity25-bolcskei.pdf)
- [从警报到真正的错误：用于静态分析结果验证的多目标多步骤定向灰盒模糊测试，2025](https://www.usenix.org/system/files/usenixsecurity25-bao-andrew.pdf)
- [通过 Dataflow Fusion 模糊 PHP 解释器，2025](https://www.usenix.org/system/files/usenixsecurity25-jiang-yuancheng.pdf)
- [GenHuzz：高效的生成硬件模糊器，2025](https://www.usenix.org/system/files/usenixsecurity25-wu-lichao.pdf)
- [迷失在翻译中：使用 TransFuzz 对 EDA 软件进行混乱的代理攻击，2025](https://www.usenix.org/system/files/usenixsecurity25-solt.pdf)
- [使用 LLM 合成输入生成器进行低成本且全面的非文本输入模糊测试，2025 年](https://www.usenix.org/system/files/usenixsecurity25-zhang-kunpeng.pdf)
- [MBFuzzer：适用于 MQTT 代理的多方协议模糊器，2025 年](https://www.usenix.org/system/files/usenixsecurity25-song-xiangpu.pdf)
- [PAPILLON：法学硕士的高效、隐秘的模糊测试支持越狱，2025 年](https://www.usenix.org/system/files/usenixsecurity25-gong-xueluan.pdf)
- [针对 COTS 二进制文件的稳健、高效且广泛可用的灰盒模糊测试，具有系统调用模式反馈，2025 年](https://www.usenix.org/system/files/usenixsecurity25-xiao-jifan.pdf)
- [Waltzz：使用堆栈不变转换进行 WebAssembly 运行时模糊测试，2025 年](https://www.usenix.org/system/files/usenixsecurity25-zhang-lingming.pdf)

</详情>

<详细信息><摘要>2024年（12篇论文）</摘要>

- [Atropos：针对服务器端漏洞的 Web 应用程序的有效模糊测试，2024 年](https://www.usenix.org/system/files/usenixsecurity24-guler.pdf)
- [Cascade：通过复杂程序生成进行 CPU 模糊测试，2024 年](https://www.usenix.org/system/files/usenixsecurity24-solt.pdf)
- [关键代码引导的定向灰盒模糊测试，2024 年](https://www.usenix.org/system/files/usenixsecurity24-xiang-yi.pdf)
- [EL3XIR：模糊 COTS 安全监视器，2024 年](https://www.usenix.org/system/files/usenixsecurity24-lindenmeier.pdf)
- [对 BusyBox 进行模糊测试：利用 LLM 和崩溃重用来挖掘嵌入式错误，2024 年](https://www.usenix.org/system/files/usenixsecurity24-asmita.pdf)
- [HYPERPILL：利用硬件虚拟化接口模糊虚拟机管理程序错误，2024 年](https://www.usenix.org/system/files/usenixsecurity24-bulekov.pdf)
- [MultiFuzz：用于测试单片固件的多流模糊器，2024](https://www.usenix.org/system/files/usenixsecurity24-chesser.pdf)
- [ResolverFuzz：通过查询响应模糊测试自动发现 DNS 解析器漏洞，2024 年](https://www.usenix.org/system/files/usenixsecurity24-zhang-qifan.pdf)
- [SDFuzz：目标状态驱动的定向模糊测试，2024](https://www.usenix.org/system/files/usenixsecurity24-li-penghui.pdf)
- [SHiFT：嵌入式应用程序的半托管模糊测试，2024 年](https://www.usenix.org/system/files/usenixsecurity24-mera.pdf)
- [迈向通用数据库管理系统模糊测试，2024 年](https://www.usenix.org/system/files/usenixsecurity24-yang-yupeng.pdf)
- [WhisperFuzz：用于检测和定位处理器时序漏洞的白盒模糊测试，2024 年](https://www.usenix.org/system/files/usenixsecurity24-borkar.pdf)

</详情>

<详细><摘要>2023年（19篇论文）</摘要>

- [AIFORE：基于自动输入格式逆向工程的智能模糊测试，2023](https://www.usenix.org/system/files/usenixsecurity23-shi-ji.pdf)
- [autofz：运行时自动模糊器组合，2023](https://www.usenix.org/system/files/usenixsecurity23-fu-yu-fu.pdf)
- [自动机引导的控制流敏感模糊驱动程序生成，2023](https://www.usenix.org/system/files/usenixsecurity23-zhang-cen.pdf)
- [通过操作距离引导模糊测试自动生成可利用的堆布局以解决堆溢出问题，2023 年](https://www.usenix.org/system/files/usenixsecurity23-zhang-bin.pdf)
- [Bleem：面向协议实现的数据包序列模糊测试，2023 年](https://www.usenix.org/system/files/usenixsecurity23-luo-zhengxiong.pdf)
- [BoKASAN：用于有效内核模糊测试的纯二进制内核地址清理程序，2023](https://www.usenix.org/system/files/usenixsecurity23-cho.pdf)
- [CarpetFuzz：从模糊测试文档中自动提取程序选项约束，2023](https://www.usenix.org/system/files/usenixsecurity23-wang-dawei.pdf)
- [DDRace：通过定向模糊测试查找 Linux 驱动程序中的并发 UAF 漏洞，2023 年](https://www.usenix.org/system/files/usenixsecurity23-yuan-ming.pdf)
- [DynSQL：针对数据库管理系统进行状态模糊测试，生成复杂且有效的 SQL 查询，2023 年](https://www.usenix.org/system/files/usenixsecurity23-jiang-zu-ming.pdf)
- [形成更快的固件模糊器，2023](https://www.usenix.org/system/files/usenixsecurity23-seidel.pdf)
- [FuzzJIT：针对 JavaScript 引擎 JIT 编译器的 Oracle 增强模糊测试，2023 年](https://www.usenix.org/system/files/usenixsecurity23-wang-junjie.pdf)
- [Fuzztruction：使用基于故障注入的模糊测试来利用隐式领域知识，2023](https://www.usenix.org/system/files/usenixsecurity23-bars.pdf)
- [GLeeFuzz：通过错误消息引导突变模糊 WebGL，2023](https://www.usenix.org/system/files/usenixsecurity23-peng.pdf)
- [Intender：使用意图状态转换指南模糊基于意图的网络，2023](https://www.usenix.org/system/files/usenixsecurity23-kim-jiwon.pdf)
- [KextFuzz：通过利用缓解措施在 Apple Silicon 上模糊 macOS 内核扩展，2023 年](https://www.usenix.org/system/files/usenixsecurity23-yin.pdf)
- [MINER：一种混合数据驱动的 REST API 模糊测试方法，2023 年](https://www.usenix.org/system/files/usenixsecurity23-lyu.pdf)
- [MorFuzz：通过运行时指令变形增强可同步协同仿真的模糊处理器，2023](https://www.usenix.org/system/files/usenixsecurity23-xu-jinyan.pdf)
- [MTSan：一种可行且实用的内存清理工具，用于模糊 COTS 二进制文件，2023 年](https://www.usenix.org/system/files/usenixsecurity23-chen-xingman.pdf)
- [PolyFuzz：多语言系统的整体灰盒模糊测试，2023](https://www.usenix.org/system/files/usenixsecurity23-li-wen.pdf)

</详情>

<详细信息><摘要>2022年（14篇论文）</摘要>

- [StateFuzz：基于系统调用的状态感知 Linux 驱动程序模糊测试，2022](https://www.usenix.org/system/files/sec22-zhao-bodong.pdf)
- [FIXREVERTER：一种用于基准模糊测试的现实错误注入方法，2022 年](https://www.usenix.org/system/files/sec22-zhang-zenong.pdf)
- [SGXFuzz：高效合成 SGX Enclave 模糊测试的嵌套结构，2022 年](https://www.usenix.org/system/files/sec22-cloosters.pdf)
- [AmpFuzz：针对放大 DDoS 漏洞的模糊测试，2022 年](https://www.usenix.org/system/files/sec22-krupp.pdf)
- [状态灰盒模糊测试，2022](https://www.usenix.org/system/files/sec22-ba.pdf)
- [BrakTooth：通过定向模糊测试对蓝牙链接管理器造成严重破坏，2022 年](https://www.usenix.org/system/files/sec22-garbelini.pdf)
- [模糊测试类似软件的硬件，2022 年](https://www.usenix.org/system/files/sec22-trippel.pdf)
- [Drifuzz：从金种子中收集设备驱动程序中的错误，2022 年](https://www.usenix.org/system/files/sec22-shen-zekun.pdf)
- [FuzzOrigin：通过 Origin 模糊测试检测浏览器中的 UXSS 漏洞，2022 年](https://www.usenix.org/system/files/sec22-kim.pdf)
- [TheHuzz：使用黄金参考模型对处理器进行指令模糊测试以查找软件可利用漏洞，2022 年](https://www.usenix.org/system/files/sec22-kande.pdf)
- [MundoFuzz：具有统计覆盖率测试和语法推理的虚拟机管理程序模糊测试，2022](https://www.usenix.org/system/files/sec22-myung.pdf)
- [Fuzzware：使用精确的 MMIO 建模进行有效的固件模糊测试，2022 年](https://www.usenix.org/system/files/sec22-scharnowski.pdf)
- [SyzScope：揭示 Linux 内核中 Fuzzer 暴露的错误的高风险安全影响，2022 年](https://www.usenix.org/system/files/sec22-zou.pdf)
- [Morphuzz：弯曲（输入）空间以模糊虚拟设备，2022](https://www.usenix.org/system/files/sec22-bulekov.pdf)

</详情>

<详细><摘要>2021年（6篇论文）</摘要>

- [突破二进制：编译器质量的工具可实现更好的纯二进制模糊测试，2021](https://www.usenix.org/conference/usenixsecurity21/presentation/nagy)
- [ICSFuzz：操纵 I/O 和重新利用二进制代码以在 ICS 控制应用中启用仪表化模糊测试，2021 年](https://www.usenix.org/conference/usenixsecurity21/presentation/tychalas)
- [通过日志引导模糊测试发现 Android 智能电视漏洞，2021 年](https://www.usenix.org/conference/usenixsecurity21/presentation/aafer)
- [约束引导的定向灰盒模糊测试，2021](https://www.usenix.org/conference/usenixsecurity21/presentation/lee-gwangmu)
- [Nyx：使用快速快照和仿射类型的灰盒虚拟机管理程序模糊测试，2021 年](https://www.usenix.org/conference/usenixsecurity21/presentation/schumilo)
- [UNIFUZZ：用于评估模糊器的全面且务实的指标驱动平台，2021 年](https://www.usenix.org/conference/usenixsecurity21/presentation/li-yuwei)

</详情>

<详细><摘要>2020年（10篇论文）</摘要>

- [粉丝：通过自动接口分析模糊 Android 本机系统服务，2020](https://www.usenix.org/conference/usenixsecurity20/presentation/liu)
- [使用协议状态模糊测试的 DTLS 实现分析，2020](https://www.usenix.org/conference/usenixsecurity20/presentation/fiterau-brostean)
- [EcoFuzz：自适应节能灰盒模糊测试作为对抗性多臂强盗的变体，2020](https://www.usenix.org/conference/usenixsecurity20/presentation/yue)
- [使用上下文相关软件故障注入模糊错误处理代码，2020](https://www.usenix.org/conference/usenixsecurity20/presentation/jiang)
- [FuzzGen：自动模糊器生成，2020](https://www.usenix.org/conference/usenixsecurity20/presentation/ispoglou)
- [ParmeSan：消毒剂引导的灰盒模糊测试，2020](https://www.usenix.org/conference/usenixsecurity20/presentation/osterlund)
- [SpecFuzz：将 Spectre 类型的漏洞暴露出来，2020 年](https://www.usenix.org/conference/usenixsecurity20/presentation/oleksenko)
- [FuzzGuard：通过深度学习过滤掉定向灰盒模糊测试中无法到达的输入，2020](https://www.usenix.org/conference/usenixsecurity20/presentation/zong)
- [Montage：神经网络语言模型引导的 JavaScript 引擎模糊器，2020](https://www.usenix.org/conference/usenixsecurity20/presentation/lee-suyoung)
- [GREYONE：数据流敏感模糊测试，2020](https://www.usenix.org/conference/usenixsecurity20/presentation/gan)

</详情>

<详情><摘要>2019年（2篇论文）</摘要>

- [模糊化：反模糊技术，2019](https://www.usenix.org/conference/usenixsecurity19/presentation/jung)
- [AntiFuzz：阻碍二进制可执行文件的模糊审计，2019](https://www.usenix.org/conference/usenixsecurity19/presentation/guler)

</详情>

<详情><摘要>2018年（3篇论文）</摘要>

- [魅力：促进移动系统设备驱动程序的动态分析，2018](https://www.usenix.org/conference/usenixsecurity18/presentation/talebi)
- [MoonShine：通过微量蒸馏优化操作系统模糊器种子选择，2018](https://www.usenix.org/conference/usenixsecurity18/presentation/pailoor)
- [QSYM：专为混合模糊测试而定制的实用 Concolic 执行引擎，2018](https://www.usenix.org/conference/usenixsecurity18/presentation/yun)

</详情>

<详情><摘要>2017年（2篇论文）</摘要>

- [OSS-Fuzz - Google 针对开源软件的持续模糊测试服务，2017 年](https://www.usenix.org/conference/usenixsecurity17/technical-sessions/presentation/serebryany)
- [kAFL：操作系统内核的硬件辅助反馈模糊测试，2017 年](https://www.usenix.org/conference/usenixsecurity17/technical-sessions/presentation/schumilo)

</详情>

<详情><摘要>2015年（1篇论文）</摘要>

- [TLS 实现的协议状态模糊测试，2015 年](https://www.usenix.org/conference/usenixsecurity15/technical-sessions/presentation/de-ruiter)

</详情>

<详情><摘要>2014年（1篇论文）</摘要>

- [优化模糊测试的种子选择，2014 年](https://softsec.kaist.ac.kr/~sangkilc/papers/rebert-usenixsec14.pdf)

</详情>

<详情><摘要>2013年（1篇论文）</摘要>

- [探测溢出：用于查找缓冲区边界违规的引导模糊器，2013 年](http://enigma.usenix.org/sites/default/files/sec13_proceedings_interior.pdf#page=57)

</详情>

<详情><摘要>2012年（1篇论文）</摘要>

- [使用代码片段进行模糊测试，2012 年](https://www.usenix.org/system/files/conference/usenixsecurity12/sec12-final73.pdf)

</详情>


### ACM 计算机与通信安全会议 (ACM CCS)

<详细><摘要>2025年（11篇论文）</摘要>

- [模糊器可用性和挑战的定性分析，2025 年](https://dl.acm.org/doi/10.1145/3719027.3765055)
- [ConTest：用控制理论驯服模糊测试中的网络物理输入空间，2025](https://dl.acm.org/doi/10.1145/3719027.3765129)
- [DiveFuzz：通过多样化指令构造增强 CPU 模糊测试，2025](https://dl.acm.org/doi/10.1145/3719027.3765167)
- [模糊测试错误消息：检测 Windows 打印组件中的 XPS 解析漏洞，2025 年](https://dl.acm.org/doi/10.1145/3719027.3744807)
- [零知识电路的模糊处理管道，2025](https://dl.acm.org/doi/10.1145/3719027.3744791)
- [Android 强化应用程序的意图感知模糊测试，2025 年](https://dl.acm.org/doi/10.1145/3719027.3744858)
- [PromeFuzz：利用大型语言模型生成模糊测试工具的知识驱动方法，2025](https://dl.acm.org/doi/10.1145/3719027.3765222)
- [用于有效模糊测试嵌入式网络堆栈的协议感知固件重新托管，2025 年](https://dl.acm.org/doi/10.1145/3719027.3765125)
- [RVISmith：RVV 内在函数的模糊编译器，2025](https://dl.acm.org/doi/10.1145/3719027.3744790)
- [SyzParam：将运行时参数纳入内核驱动程序模糊测试，2025](https://dl.acm.org/doi/10.1145/3719027.3744838)
- [SyzSpec：通过欠约束符号执行生成 Linux 内核模糊测试规范，2025 年](https://dl.acm.org/doi/10.1145/3719027.3744811)

</详情>

<详细><摘要>2024年（19篇论文）</摘要>

- [像纸牌屋一样倒塌：通过模糊测试入侵楼宇自动化系统，2024 年](https://dl.acm.org/doi/10.1145/3658644.3690216)
- [倒计时：用于暴露 Linux 内核中临时内存错误的引用计数引导模糊测试，2024 年](https://dl.acm.org/doi/10.1145/3658644.3690320)
- [CrossFire：在 Apple Silicon 上模糊 macOS Cross-XPU 内存，2024 年](https://dl.acm.org/doi/10.1145/3658644.3690376)
- [DarthShader：模糊测试 WebGPU 着色器翻译器和编译器，2024 年](https://dl.acm.org/doi/10.1145/3658644.3690209)
- [FOX：覆盖率引导的模糊测试作为在线随机控制，2024](https://dl.acm.org/doi/10.1145/3658644.3670362)
- [面向未来的模糊测试：通过稳健的模糊测试发现被遮挡的未来漏洞，2024 年](https://dl.acm.org/doi/10.1145/3658644.3690278)
- [FuzzCache：通过基于软件的数据缓存优化 Web 应用程序模糊测试，2024 年](https://dl.acm.org/doi/10.1145/3658644.3670278)
- [使用基于图的 IR 模糊 JavaScript 引擎，2024 年](https://dl.acm.org/doi/10.1145/3658644.3690336)
- [利用二进制覆盖率在内核模糊测试中提供有效的生成指导，2024 年](https://dl.acm.org/doi/10.1145/3658644.3690232)
- [LIFTFUZZ：通过 GPT 的上下文感知模糊测试验证二进制 Lifters，2024](https://dl.acm.org/doi/10.1145/3658644.3670276)
- [没有同行，就没有哭泣：通过故障注入进行网络应用程序模糊测试，2024 年](https://dl.acm.org/doi/10.1145/3658644.3690274)
- [关于通过静态分析理解和预测模糊器性能，2024 年](https://dl.acm.org/doi/10.1145/3658644.3670348)
- [OSmart：白盒程序选项模糊测试，2024](https://dl.acm.org/doi/10.1145/3658644.3690228)
- [程序环境模糊测试，2024](https://dl.acm.org/doi/10.1145/3658644.3690229)
- [快速模糊测试以生成模糊驱动程序，2024 年](https://dl.acm.org/doi/10.1145/3658644.3670396)
- [ProphetFuzz：通过大型语言模型仅通过文档对高风险选项组合进行全自动预测和模糊测试，2024 年](https://dl.acm.org/doi/10.1145/3658644.3690231)
- [RANsacked：一种用于模糊 LTE 和 5G RAN 核心接口的领域知情方法，2024 年](https://dl.acm.org/doi/10.1145/3658644.3670320)
- [RIoTFuzzer：配套应用程序辅助远程模糊测试，用于检测物联网设备中的漏洞，2024 年](https://dl.acm.org/doi/10.1145/3658644.3670342)
- [向 BpfChecker 抛出错误：通过差异模糊测试揭示 eBPF 运行时的实现缺陷，2024 年](https://dl.acm.org/doi/10.1145/3658644.3690237)

</详情>

<详细信息><摘要>2023年（9篇论文）</摘要>

- [DSFuzz：通过依赖状态探索检测深层状态错误，2023](https://dl.acm.org/doi/10.1145/3576915.3616594)
- [海滩上的 Fuzz：模糊 Solana 智能合约，2023 年](https://dl.acm.org/doi/10.1145/3576915.3623178)
- [分布式系统的灰盒模糊测试，2023](https://dl.acm.org/doi/10.1145/3576915.3623097)
- [Hopper：图书馆的解释性模糊测试，2023](https://dl.acm.org/doi/10.1145/3576915.3616610)
- [通过安全应用将网络协议实现提升到精确的格式规范，2023 年](https://dl.acm.org/doi/10.1145/3576915.3616614)
- [NestFuzz：通过全面理解输入处理逻辑来增强模糊测试，2023](https://dl.acm.org/doi/10.1145/3576915.3623103)
- [用于加速灰盒模糊测试的配置文件引导系统优化，2023](https://dl.acm.org/doi/10.1145/3576915.3616636)
- [PyRTFuzz：通过两级协作模糊测试检测 Python 运行时中的错误，2023 年](https://dl.acm.org/doi/10.1145/3576915.3623166)
- [SyzDirect：Linux 内核的定向灰盒模糊测试，2023 年](https://dl.acm.org/doi/10.1145/3576915.3623146)

</详情>

<详细信息><摘要>2022年（6篇论文）</摘要>

- [SpecDoctor：用于查找瞬态执行漏洞的差异模糊测试，2022 年](https://compsec.snu.ac.kr/papers/jaewon-specdoctor.pdf)
- [SFuzz：实时操作系统基于切片的模糊测试，2022](https://huhong789.github.io/papers/chen:sfuzz.pdf)
- [MC^2：严格高效的定向灰盒模糊测试，2022](https://arxiv.org/pdf/2208.14530.pdf)
- [LibAFL：构建模块化和可重用模糊器的框架，2022 年](https://www.s3.eurecom.fr/docs/ccs22_fioraldi.pdf)
- [JIT-Picking：JavaScript 引擎的差异模糊测试，2022](https://publications.cispa.saarland/3773/1/2022-CCS-JIT-Fuzzing.pdf)
- [DriveFuzz：通过驾驶质量引导模糊测试发现自动驾驶错误，2022 年](https://chungkim.io/doc/ccs22-drivefuzz.pdf)

</详情>

<详细信息><摘要>2021年（8篇论文）</摘要>

- [SoFi：JavaScript 引擎的反射增强模糊测试，2021](https://dl.acm.org/doi/pdf/10.1145/3460120.3484823)
- [T-Reqs：使用差异模糊测试的 HTTP 请求走私，2021](https://bahruz.me/papers/ccs2021treqs.pdf)
- [V-SHUTTLE：可扩展和语义感知的虚拟机监控程序模糊测试，2021](https://nesa.zju.edu.cn/download/ppt/pgn_slides_V-SHUTTLE.pdf)
- [相同的覆盖率，更少的膨胀：通过保留覆盖率的覆盖率引导跟踪加速纯二进制模糊测试，2021](https://people.cs.vt.edu/snagy2/papers/21CCS.pdf)
- [HyperFuzzer：适用于虚拟 CPU 的高效混合模糊器，2021 年](https://www.microsoft.com/en-us/research/uploads/prod/2021/09/hyperfuzzer-ccs21.pdf)
- [回归灰盒模糊测试，2021](https://mboehme.github.io/paper/CCS21.pdf)
- [提高模糊测试性能和精度的硬件支持，2021 年](https://gts3.org/assets/papers/2021/ding:snap.pdf)
- [SNIPUZZ：通过消息片段推理对物联网固件进行黑盒模糊测试，2021](https://arxiv.org/pdf/2105.05445.pdf)

</详情>

<详细信息><摘要>2020年（1篇论文）</摘要>

- [FREEDOM：设计最先进的 DOM 模糊器，2020](https://gts3.org/assets/papers/2020/xu:freedom.pdf)

</详情>

<详细><摘要>2019年（3篇论文）</摘要>

- [Intriguer：混合模糊测试的字段级约束求解，2019](https://dl.acm.org/citation.cfm?id=3354249)
- [学习从符号执行到智能合约的模糊测试，2019](https://files.sri.inf.ethz.ch/website/papers/ccs19-ilf.pdf)
- [Matryoshka：模糊深层嵌套分支，2019](https://web.cs.ucdavis.edu/~hchen/paper/chen2019matryoshka.pdf)

</详情>

<详情><摘要>2018年（2篇论文）</摘要>

- [评估模糊测试，2018](http://www.cs.umd.edu/~mwh/papers/fuzzeval.pdf)
- [鹰眼：走向理想的定向灰盒模糊器，2018](https://chenbihuan.github.io/paper/ccs18-chen-hawkeye.pdf)

</详情>

<详细><摘要>2017年（7篇论文）</摘要>

- [IMF：基于推断模型的模糊器，2017](http://daramg.gift/paper/han-ccs2017.pdf)
- [SemFuzz：基于语义的概念验证漏洞自动生成，2017 年](https://www.informatics.indiana.edu/xw7/papers/p2139-you.pdf)
- [使用 Kelinci 对 Java 进行基于 AFL 的模糊测试，2017 年](https://dl.acm.org/citation.cfm?id=3138820)
- [设计新的操作原语以提高模糊测试性能，2017 年](http://iisp.gatech.edu/sites/default/files/images/designing_new_operating_primitives_to_improve_fuzzing_performance_vt.pdf)
- [指导灰盒模糊测试，2017](https://dl.acm.org/citation.cfm?id=3134020)
- [SlowFuzz：算法复杂性漏洞的自动域独立检测，2017](https://arxiv.org/pdf/1708.08437.pdf)
- [DIFUZE：内核驱动程序的接口感知模糊测试，2017](https://acmccs.github.io/papers/p2123-corinaA.pdf)

</详情>

<详情><摘要>2016年（3篇论文）</摘要>

- [TLS 库的系统模糊测试和测试，2016 年](https://www.nds.rub.de/media/nds/veroeffentlichungen/2016/10/19/tls-attacker-ccs16.pdf)
- [基于覆盖范围的灰盒模糊测试作为马尔可夫链，2016](https://ieeexplore.ieee.org/abstract/document/8233151)
- [eFuzz：DLMS/COSEM 电表的模糊器，2016 年](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.817.5616&rep=rep1&type=pdf)

</详情>

<详情><摘要>2013年（2篇论文）</摘要>

- [调度黑盒突变模糊测试，2013](https://softsec.kaist.ac.kr/~sangkilc/papers/woo-ccs13.pdf)
- [驯服编译器模糊器，2013](https://www.cs.utah.edu/~regehr/papers/pldi13.pdf)

</详情>

<详情><摘要>2012年（1篇论文）</摘要>

- [SAGE：用于安全测试的白盒模糊测试，2012 年](https://dl.acm.org/citation.cfm?id=2094081)

</详情>

<详情><摘要>2008-2009（2篇论文）</摘要>

- [基于污点的定向白盒模糊测试，2009](https://dl.acm.org/citation.cfm?id=1555061)
- [基于语法的白盒模糊测试，2008](https://dl.acm.org/citation.cfm?id=1375607)

</详情>


### ArXiv（人工智能和机器学习模糊测试）
- [MEUZZ：混合模糊测试的智能种子调度，2020](https://arxiv.org/abs/2002.08568)
- [2019 年机器学习在模糊测试中的应用回顾](https://arxiv.org/abs/1906.11133)
- [2019 年 Android 操作系统供应商系统服务的进化模糊测试](https://arxiv.org/abs/1906.00621)
- [MoonLight：通过近乎最优的语料库蒸馏进行有效的模糊测试，2019](https://arxiv.org/abs/1905.13055)
- [深度神经网络的覆盖引导模糊测试，2018](https://arxiv.org/abs/1809.01266)
- [DLFuzz：深度学习系统的差分模糊测试，2018](https://arxiv.org/abs/1808.09413)
- [TensorFuzz：使用覆盖率引导模糊测试来调试神经网络，2018](https://arxiv.org/abs/1807.10875)
- [NEUZZ：通过神经程序学习进行高效模糊测试，2018](https://arxiv.org/abs/1807.05620)
- [EnFuzz：从集成学习到集成模糊测试，2018](https://arxiv.org/abs/1807.00182)
- [REST-ler：自动智能 REST API 模糊测试，2018](https://arxiv.org/abs/1806.09739)
- [深度强化模糊测试，2018](https://arxiv.org/abs/1801.04589)
- [并非所有字节都相等：用于模糊测试的神经字节筛，2017 年](https://arxiv.org/abs/1711.04596)
- [更快的模糊测试：使用深度神经模型重新初始化，2017](https://arxiv.org/abs/1711.02807)
- [Learn&Fuzz：用于输入模糊测试的机器学习，2017 年](https://arxiv.org/abs/1701.07232)
- [用基于变异的模糊测试补充模型学习，2016](https://arxiv.org/abs/1611.02429)

### 其他人
- [Fuzzle：为模糊器制作拼图，2022](https://softsec.kaist.ac.kr/~sangkilc/papers/lee-ase22.pdf)
- [Ifuzzer：使用遗传编程的进化解释器模糊器，2016](https://www.cs.vu.nl/~herbertb/download/papers/ifuzzer-esorics16.pdf)
- [混合模糊测试：通过模糊测试和符号执行发现软件错误，2012 年](https://pdfs.semanticscholar.org/488a/b1e313f5109153f2c74e3b5d86d41e9b4b71.pdf)
- [Windows 系统安全性的调用流感知 API 模糊测试，2008 年](https://www.computer.org/csdl/proceedings/iccsa/2008/3243/00/3243a019-abs.html)
- [反馈导向随机测试生成，2007 年](https://dl.acm.org/citation.cfm?id=1248841)
- [MTF-Storm：Modbus/TCP 的高性能模糊器，2018](https://doi.org/10.1109/ETFA.2018.8502600)
- [用于测试互联工业系统的 Modbus/TCP 模糊器，2015](https://doi.org/10.1109/ETFA.2015.7301400)



## 工具
开源模糊测试工具的精选集合，根据 [fuzzing-survey.org](https://fuzzing-survey.org/) 的分类法按目标类别进行组织。工具的选择基于多种因素，包括 GitHub 的受欢迎程度、新近度、原作者官方存储库的可用性以及项目是否得到积极维护。
### 文件
- [AFL++](https://github.com/AFLplusplus/AFLplusplus) - 是 Google AFL 的高级分支，具有更快的速度、更多更好的突变、更多更好的工具以及自定义模块支持。
- [Angora](https://github.com/AngoraFuzzer/Angora) - 基于突变的覆盖引导模糊器，通过解决路径约束而无需符号执行来增加分支覆盖率。
### 内核
- [ACTOR](https://github.com/ucsb-seclab/actor) (2023) - 一个动作引导的内核模糊框架，利用触发的动作及其时间关系生成输入。
- [NTFuzz](https://github.com/SoftSec-KAIST/NTFuzz) (2021) - 一种类型感知的 Windows 内核模糊器，可静态分析系统二进制文件以推断系统调用类型，从而实现更有效的模糊测试。
- [KRACE](https://github.com/sslab-gatech/krace) (2020) - 一种覆盖引导的模糊测试框架，通过多线程系统调用序列探索并发性来检测内核文件系统中的数据竞争。
- [Razzer](https://github.com/compsec-snu/razzer) (2019) - 一个内核模糊器，使用静态分析和两阶段模糊测试来检测 Linux 内核中的竞争条件和并发错误。
- [Hydra](https://github.com/sslab-gatech/Hydra) (2019) - 一个模糊测试框架，用于使用输入变异器、反馈引擎和可定制的检查器自动发现文件系统中的语义错误。
- [Janus](https://github.com/sslab-gatech/janus) (2019) - 一种文件系统模糊器，通过同时改变文件系统映像和系统调用序列来查找 Linux 内核文件系统中的内存损坏。
- [DIFUZE](https://github.com/ucsb-seclab/difuze) (2017) - 用于 Linux 内核驱动程序的接口感知模糊器，可通过 LLVM 分析自动恢复 ioctl 接口并生成目标测试用例。
- [IMF](https://github.com/SoftSec-KAIST/IMF) (2017) - 一个内核 API 模糊器，利用自动 API 模型推理来发现 macOS 内核 API 中的漏洞。
- [kAFL](https://github.com/rub-syssec/kafl) (2017) - 硬件辅助的 x86-64 VM 内核模糊测试框架，具有高性能 VM 重新加载功能，用于查找操作系统内核漏洞。
- [syzkaller](https://github.com/google/syzkaller) (2015) - 一个无监督的覆盖引导内核模糊器，支持 FreeBSD、Fuchsia、gVisor、Linux、NetBSD、OpenBSD 和 Windows。
- [Trinity](https://github.com/kernelslacker/trinity) (2012) - 一个 Linux 系统调用模糊器，它为系统调用生成半智能随机参数，包括有效的文件描述符、标志和范围偏差值。
### 网络
### 应用程序编程接口
- [WuppieFuzz](https://github.com/TNO-S3/WuppieFuzz) - 在 LibAFL 之上开发的覆盖率引导的 REST API 模糊器。
- [IvySyn](https://gitlab.com/brown-ssl/ivysyn) - 用于发现深度学习 (DL) 框架中内存错误漏洞的全自动框架。
- [MINER](https://github.com/puppet-meteor/MINER) - 一个 REST API 模糊器，利用三种数据驱动设计协同工作来指导序列生成、提高请求生成质量并捕获因参数使用不正确而导致的独特错误。
- [RestTestGen](https://github.com/SeUniVr/RestTestGen) - 一个强大的工具和框架，专为 RESTful Web API 的自动化黑盒测试而设计。
- [GraphFuzz](https://github.com/ForAllSecure/GraphFuzz) - 用于构建结构感知的库 API 模糊器的实验框架。
- [Minerva](https://github.com/ChijinZ/Minerva) - 通过 API mod-ref 关系增强的浏览器模糊器，旨在在每个测试用例中合成高度相关的浏览器 API 调用。
- [FANS](https://github.com/iromise/fans) - 一个针对 Android 原生系统服务的模糊测试工具，由四个组件组成：接口收集器、接口模型提取器、依赖推断器和模糊器引擎。
### JavaScript
### 固件
### 管理程序
### 中央处理器
- [DifuzzRTL](https://github.com/compsec-snu/difuzz-rtl) - 用于 CPU 验证的差分模糊测试方法。
- [MorFuzz](https://github.com/sycuricon/MorFuzz) - 通用 RISC-V 处理器模糊测试框架，可以有效检测软件可触发的功能错误。
- [SpecFuzz](https://github.com/tudinfse/SpecFuzz) - 用于对 Spectre 漏洞进行模糊测试的工具。
- [Transynther](https://github.com/vernamlab/Medusa) - 自动生成和测试具有各种故障和微代码辅助的 Meltdown 攻击的构建块。
### 库
### 网络
- [TEFuzz](https://github.com/seclab-fudan/TEFuzz/) - 定制的基于模糊测试的框架，有助于检测和利用模板转义错误。
- [Witcher](https://github.com/sefcom/Witcher) - 一种 Web 应用程序模糊测试器，利用变异模糊测试来探索 Web 应用程序，并利用故障升级来检测命令和 SQL 注入漏洞。
- [CorbFuzz](https://github.com/shouc/corbfuzz) - 状态感知模糊器，用于从 Web 应用程序生成尽可能多的响应，而无需设置数据库。
### DOM
### 论证
### 区块链
- [Fluffy](https://github.com/snuspl/fluffy) - 用于发现以太坊中共识错误的多交易差分模糊器。
- [LOKI](https://github.com/ConsensusFuzz/LOKI) - 区块链共识协议模糊测试框架，可检测共识内存相关和逻辑错误。
### 数据库管理系统
- [Squirrel](https://github.com/s3team/Squirrel) - 用于数据库管理系统 (DBMS) 的模糊器。


## 贡献

欢迎投稿！首先阅读[贡献指南](contributing.md)。


