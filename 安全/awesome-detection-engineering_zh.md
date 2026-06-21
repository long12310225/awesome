# 很棒的检测工程 [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

检测工程是网络安全防御计划的一项战术功能，涉及检测控制的设计、实施和操作，其目标是在恶意或未经授权的活动对个人或组织产生负面影响之前主动识别它们。

欢迎所有贡献，请在提交拉取请求之前仔细查看[贡献指南](https://github.com/infosecB/awesome-detection-engineering/blob/main/contributing.md)。

## 内容

- [概念与框架](#concepts--frameworks)
- [检测内容及签名](#detection-content--signatures)
- [记录、监控和数据源](#logging-monitoring--data-sources)
- [一般资源](#general-resources)

## 概念与框架

- [MITRE ATT&CK](https://attack.mitre.org/) - 基于现实世界观察的对手战术、技术和程序的基本框架。
- [Alerting and Detection Strategies (ADS) Framework | Palantir](https://github.com/palantir/alerting-detection-strategy-framework) - 创建和记录有效检测内容的蓝图。
- [Detection Engineering Maturity Matrix | Kyle Bailey](https://detectionengineering.io) - 一个详细的矩阵，用作衡量组织检测工程计划整体成熟度的工具。
- [Detection Maturity Level (DML) Model | Ryan Stillions](http://ryanstillions.blogspot.com/2014/04/the-dml-model_21.html) - 定义并描述组织威胁检测计划成熟度的 8 个不同级别。
- [The Pyramid of Pain | David J Bianco](http://detect-respond.blogspot.com/2013/03/the-pyramid-of-pain.html) - 用于描述危害指标的各种分类及其检测威胁行为者的有效性水平的模型。
- [Cyber Kill Chain | Lockheed Martin](https://www.lockheedmartin.com/en-us/capabilities/cyber/cyber-kill-chain.html) - 洛克希德·马丁公司的框架概述了网络攻击中常见的 7 个阶段。
- [MaGMa (Management, Growth and Metrics & Assessment) Use Case Defintion Model](https://www.betaalvereniging.nl/wp-content/uploads/2026/03/FI-ISAC-use-case-framework-verkorte-versie.pdf) - 用于定义威胁检测用例的以业务为中心的方法。
- [Synthetic Adversarial Log Objects (SALO) | Splunk](https://github.com/splunk/salo) - 综合对抗日志对象 (SALO) 是一个用于生成日志事件的框架，无需基础设施或操作来启动导致日志事件的事件。
- [The Zen of Security Rules | Justin Ibarra](https://br0k3nlab.com/resources/zen-of-security-rules/) - 概述了作为创建高质量检测内容的普遍原则的 19 条格言。
- [Blue-team-as-Code - the Spiral of Joy | Den Iuzvyk, Oleg Kolesnikov](https://sansorg.egnyte.com/dl/KTc16ldiqv) - 蓝队即代码：来自使用日志的现实红队检测自动化的经验教训。
- [Detection Development Lifecycle | Haider Dost et al.](https://medium.com/snowflake/detection-development-lifecycle-af166fffb3bc) - Snowflake 的检测开发生命周期的实现。
- [Threat Detection Maturity Framework | Haider Dost of Snowflake](https://medium.com/snowflake/threat-detection-maturity-framework-23bbb74db2bc) - 用于衡量威胁检测计划是否成功的成熟度矩阵。
- [Elastic's Detection Engineering Behavior Maturity Model](https://www.elastic.co/security-labs/elastic-releases-debmm) - Elastic 用于衡量威胁检测程序成熟度的定性和定量方法。
- [Detection Engineering AI Maturity Framework | Brendan Chamberlain](https://infosecb.github.io/detection-engineering-ai-maturity/) - 一个社区框架，具有跨十个维度的四个成熟度级别，用于评估组织如何在检测工程项目（从基础到检测生命周期）中应用人工智能和法学硕士。
- [Prioritizing Detection Engineering | Ryan McGeehan](https://medium.com/starting-up-security/prioritizing-detection-engineering-b60b46d55051) - 一位资深检测工程师概述了如何从头开始构建检测工程程序。
- [Detection Engineering Field Manual | Zack Allen](https://www.detectionengineering.net/s/field-manual) - 一系列探索检测工程的各种基础组成部分的帖子。
- [Open Threat Informed Detection Engineering aka OpenTide'](https://github.com/OpenTideHQ) - 由欧盟委员会创建和维护的一体化检测工程运营框架，可将您的 CTI 转换为将威胁向量与检测目标相结合的可操作的检测覆盖图，并通过检测即代码部署系统从中央存储库管理您的整个检测库。 OpenTide格式旨在测量和扩大检测覆盖范围，其规则部署引擎是完全可扩展的，并支持多个平台并行（利用所有技术功能和本机查询语言）。 OpenTide 既可以在单个 DE 团队内作为主框架运行，又可以作为跨 SOC 的通用格式来促进数据交换。
- [ThreatMapper | Andrey Pautov](https://github.com/anpa1200/threatmapper) - CTI 到检测工作台，用于将威胁报告映射到 ATT&CK、比较 TTP 与组和活动的重叠、识别检测差距以及导出可供分析人员使用的输出。
- [ZettelForge](https://github.com/rolandpg/zettelforge) - 代理内存系统将 Sigma 和 YARA 规则视为一流的内存实体，具有 LLM 规则解释器、CTI 实体的 STIX 2.1 知识图以及将规则连接到它们检测到的参与者和技术的离线优先 RAG。 Python，麻省理工学院。

## 检测内容及签名

- [Rulehound](https://rulehound.com) - 公开可用的开源威胁检测规则集的索引。
- [MITRE Cyber Analytics Repository (CAR)](https://car.mitre.org) - MITRE 维护良好的检测内容存储库。
- [CAR Coverage Comparision](https://car.mitre.org/coverage/) - MITRE ATT&CK 技术 ID 矩阵以及可用 Splunk 安全内容、Elastic 检测规则、Sigma 规则和 CAR 内容的链接。
- [Sigma Rules](https://github.com/SigmaHQ/sigma) - Sigma 的交钥匙检测内容存储库。可以转换内容以用于大多数 SIEM。
- [Sigma rule converter](https://sigconverter.io/) - 一种开源工具，可以转换检测内容以用于大多数 SIEM。
- [AttackRuleMap](https://attackrulemap.com) - 开源检测规则和原子测试的映射。
- [Splunk Security Content](https://github.com/splunk/security_content) - Splunk 的开源且经常更新的检测内容可以进行调整以用于其他工具。
- [Elastic Detection Rules](https://github.com/elastic/detection-rules/tree/main/rules) - Elastic 的检测规则是为 Elastic SIEM 原生编写的。可以使用 Uncoder 轻松转换以供其他 SIEM 使用。
- [Elastic Endpoint Behavioral Rules](https://github.com/elastic/protections-artifacts/tree/main/behavior/rules) - Elastic 的端点行为（预防）规则以 EQL 编写，本身适用于 Elastic 端点​​代理。
- [Elastic Yara Signatures](https://github.com/elastic/protections-artifacts/tree/main/yara/rules) - Elastic 的 YARA 签名，在 Elastic 端点​​代理上运行。
- [Elastic Endpoint Ransomware Artifact](https://github.com/elastic/protections-artifacts/blob/main/ransomware/artifact.lua) - Elastic 的勒索软件工件，在 Elastic 端点​​代理上运行。
- [Chronicle (GCP) Detection Rules](https://github.com/chronicle/detection-rules) - Chronicle 的检测规则是为 Chronicle 平台原生编写的。
- [Exabeam Content Library](https://github.com/ExabeamLabs/Content-Library-CIM2) - Exabeam 的开箱即用检测内容与 Exabeam 通用信息模型兼容。
- [Panther Labs Detection Rules](https://github.com/panther-labs/panther-analysis/tree/main/rules) - Panther Lab 的原生检测规则。
- [Anvilogic Detection Armory](https://github.com/anvilogic-forge/armory) - Anvilogic 的开源和公开可用的检测内容。
- [AWS GuardDuty Findings](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-active.html) - 所有 AWS GuardDuty 调查结果、其描述以及关联数据源的列表。
- [GCP Security Command Center Findings](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#threats) - 所有 GCP 安全指挥中心调查结果、其描述以及关联数据源的列表。
- [Azure Defender for Cloud Security Alerts](https://learn.microsoft.com/en-us/azure/defender-for-cloud/alerts-reference) - 所有 Azure 云安全警报、其描述以及关联数据源的列表。
- [Center for Threat Informed Defense Security Stack Mappings](https://github.com/center-for-threat-informed-defense/security-stack-mappings) - 描述云计算平台（Azure、AWS）的内置检测功能及其与 MITRE ATT&CK 框架的映射。
- [Detection Engineering with Splunk](https://github.com/west-wind/Threat-Hunting-With-Splunk) - 致力于在 SPL 中共享检测分析的 GitHub 存储库。
- [Google Cloud Security Analytics](https://github.com/GoogleCloudPlatform/security-analytics) - 此存储库充当社区驱动的示例安全分析列表，用于审核云使用情况以及检测对 Google Cloud 中数据和工作负载的威胁。
- [KQL Advanced Hunting Queries & Analytics Rules](https://github.com/Bert-JanP/Hunting-Queries-Detection-Rules) - Microsoft Defender for Endpoint、Defender For Identity 和 Defender For Cloud Apps 的终结点检测和搜寻查询列表。
- [Sigma2KQL](https://github.com/Khadinxc/Sigma2KQL) - 所有 SIGMA 规则的存储库均转换为 KQL，每周运行一次以更新存储库并与 SIGMA 规则存储库的最新版本保持一致。
- [TerraSigma](https://github.com/Khadinxc/TerraSigma) - 转换为 Microsoft Sentinel Terraform 计划分析资源的所有 SIGMA 规则的存储库。该存储库按每周计划运行，以更新存储库并与 SIGMA 规则存储库的最新版本保持一致。为规则完成正确的实体映射，以确保存储库是即插即用的。
- [Detections Digest | Sergey Polzunov](https://detections-digest.rulecheck.io) - 一份时事通讯，其中包含此处列出的许多流行检测内容源的更新。

## 记录、监控和数据源

- [Windows Logging Cheatsheets](https://www.malwarearchaeology.com/cheat-sheets) - 多个备忘单概述了不同粒度级别的 Windows 事件日志记录的建议。
- [Linux auditd Detection Ruleset](https://github.com/Neo23x0/auditd/blob/master/audit.rules) - Linux Auditd 规则集可生成威胁检测用例所需的遥测数据。
- [MITRE ATT&CK Data Sources Blog Post](https://medium.com/mitre-attack/defining-attack-data-sources-part-i-4c39e581454f) - MITRE 描述了各种数据源以及它们如何与 MITRE ATT&CK 框架中的 TTP 相关。
- [MITRE ATT&CK Data Sources List](https://attack.mitre.org/datasources/) - 作为 v10 的一部分添加到 MITRE ATT&CK 的数据源对象。
- [Splunk Common Information Model (CIM)](https://docs.splunk.com/Documentation/CIM/5.0.0/User/Overview) - Splunk 的专有模型用作标准化安全数据的框架。
- [Elastic Common Schema](https://www.elastic.co/docs/reference/ecs/ecs-getting-started) - Elastic 的专有模型用作标准化安全数据的框架。
- [Exabeam Common Information Model](https://github.com/ExabeamLabs/CIMLibrary) - Exabeam 的专有模型用作标准化安全数据的框架。
- [Open Cybersecurity Schema Framework (OCSF)](https://schema.ocsf.io/categories?extensions) - 开源安全数据源和事件架构。
- [osquery | Facebook](https://osquery.io) - 一种基于 SQL 的操作系统检测、监控和分析框架，将操作系统数据公开为关系表以供查询和检测。
- [Loghub](https://github.com/logpai/loghub) - 用于研究和测试的开源且免费的安全数据源。
- [Elastalert | Yelp](https://github.com/YelpArchive/elastalert) - ElastAlert 是一个简单的框架，用于针对 Elasticsearch 中的数据中的异常、峰值或其他感兴趣的模式发出警报。
- [Matano](https://github.com/matanolabs/matano) - 开源云原生安全湖平台（SIEM 替代方案），用于 AWS 上的威胁追踪、Python 检测即代码和事件响应。
- [Microsoft XDR 高级搜寻架构](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-schema-tables) 为了帮助进行多表查询，您可以使用高级搜寻架构，其中包含带有事件信息以及有关设备、警报、身份和其他实体类型的详细信息的表和列。
- [InnerWarden](https://github.com/InnerWarden/innerwarden) - 适用于 Linux 的自主安全代理，通过 38 个 eBPF 挂钩、48 个检测器和 23 个关联规则进行实时威胁检测和响应。
- [Rustinel | Karib0u](https://github.com/Karib0u/rustinel) - 适用于 Windows 和 Linux 的开源端点检测引擎，可收集 ETW/eBPF 遥测数据并评估 Sigma、YARA 和 IOC 检测。

## 一般资源
 
- [ATT&CK Navigator | MITRE](https://mitre-attack.github.io/attack-navigator/enterprise/) - MITRE 的开源工具，可用于跟踪检测覆盖范围、可见性和其他工作及其与 ATT&CK 框架的关系。
- [Detection Engineering Weekly | Zack Allen](https://www.detectionengineering.net) - 专门介绍检测工程新闻和操作方法的时事通讯。
- [Detection Engineering Twitter List | Zack Allen](https://x.com/i/lists/1629936556298436608) - 检测工程思想领袖的 Twitter 列表。
- [DETT&CT: MAPPING YOUR BLUE TEAM TO MITRE ATT&CK™](https://www.mbsecure.nl/blog/2019/5/dettact-mapping-your-blue-team-to-mitre-attack) - 概述了根据 MITRE ATT&CK 框架衡量安全数据可见性和检测覆盖范围的方法。
- [Awesome Kubernetes (K8s) Threat Detection](https://github.com/jatrost/awesome-kubernetes-threat-detection) - 另一个致力于 Kubernetes (K8s) 威胁检测的很棒列表。
- [Detection and Response Pipeline](https://github.com/0x4D31/detection-and-response-pipeline) - 用于检测和响应管道的每个组件的工具列表，其中包括实际示例。
- [Living Off the Living Off the Land](https://lolol.farm) - 为土地繁荣而收集的资源。
- [Detection at Scale Podcast | Jack Naglieri](https://podcasts.apple.com/us/podcast/detection-at-scale/id1582584270) - 一个以检测工程为重点的播客，其中包括该专业领域的许多思想领袖。
- [Cloud Threat Landscape | Wiz](https://threats.wiz.io/all-techniques) - 一个以云检测工程为中心的数据库，其中列出了已知已危害云环境的威胁参与者、其武器库中的工具和技术以及他们首选的目标技术。
- [CTI Analyst Field Manual | Andrey Pautov](https://1200km.com/cti-analyst-field-manual/) - 实用的 CTI 到检测参考，涵盖证据标签、来源可靠性、ATT&CK 映射门、狩猎假设和检测积压工作流程。
- [Splunk ES Correlation Searches Best Practices | OpsTune](https://github.com/inodee/threathunting-spl/blob/master/Splunk%20ES%20Correlation%20Searches%20Best%20Practices%20v1.3.pdf) - 有关在 Splunk Enterprise Security 应用程序中生成高质量检测内容的非常详细的指南。
- [How Google Does It: Making threat detection high-quality, scalable, and modern | Anton Chuvakin, Tim Nguyen](https://cloud.google.com/transform/how-google-does-it-modernizing-threat-detection) - Google 团队强调了构建高质量、可扩展的现代威胁检测程序的 5 个关键原则。
- [SOCLabs](https://www.soc-labs.top/) - 蓝队成​​员和检测工程师的实验室，拥有真实的威胁数据并支持流行的 SIEM 查询语言，可以在检测规则编写和威胁狩猎方面进行动手学习和实践。
