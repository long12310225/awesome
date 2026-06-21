# 很棒的实证软件工程 [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
精心策划的数据集和工具存储库，可用于对软件系统进行基于证据的数据驱动研究。
这种研究方法通常被称为[实验或经验软件工程](https://en.wikipedia.org/wiki/Experimental_software_engineering)。
许多数据集也可用于使用[基于搜索的软件工程](https://en.wikipedia.org/wiki/Search-based_software_engineering)方法的研究。
该存储库以[挖矿软件存储库 (MSR)](https://www.msrconf.org/) 会议系列命名。
有关此类工作的示例，请参阅 MSR 会议的[名人堂](http://2016.msrconf.org/#/hall-of-fame)。


- 此列表需要您的投入才能不断改进。
阅读[贡献指南](contributing.md) 以获取有关如何进行的说明
你可以做出贡献。
或者，您可以给我发送一封[电子邮件](mailto:dds@aueb.gr)
如果您发现该过程过于繁琐或令人困惑。
- 有关更多精彩列表，请参阅 [awesome](https://github.com/sindresorhus/awesome)。

## 内容
- [Repositories](#repositories)
- [数据集](#data-sets)
- [Tools](#tools)
- [研究网点](#research-outlets)

## 存储库

- [ESEUR](https://github.com/Derek-Jones/ESEUR-code-data) 公开书籍 [Evidence-based Software Engineering](http://www.knosof.co.uk/ESEUR/index.html) 中使用的所有数据
- [MSR 数据集目录](https://authecesofteng.github.io/directory-msr-datasets/)
- [FLOSSmole](https://flossmole.org/collection_details) - 免费/自由/开源项目数据的协作收集和分析。
- [PROMISE](http://promise.site.uottawa.ca/SERepository/datasets-page.html) - 大约 20 个与软件工程研究相关的数据集。
- [SIR](http://sir.unl.edu/portal/index.php) - 软件工件基础设施存储库； Java、C、C++ 和 C# 软件以及测试套件和故障数据。
- [Zenodo](http://zenodo.org/) - CERN 开放访问存储库中的软件数据集合。
  - [软件工程工件可以真正帮助未来的任务](http://zenodo.org/communities/seacraft)
  - [实证软件工程](https://zenodo.org/communities/empirical-software-engineering/)
  - [采矿软件存储库](https://zenodo.org/communities/msr/)

## 数据集

- [AndroidTimeMachine](https://androidtimemachine.github.io) - 基于图形的数据集，包含 8,431 个真实 Android 应用程序的提交历史记录。
- [AndroZoo](https://androzoo.uni.lu/) - Android 应用程序集合。
- [Bug Prediction Dataset](http://bug.inf.usi.ch/index.php) - 来自 Eclipse JDT Core、PDE UI、Equinox Framework、Lucene、Mylyn 及其历史记录的模型和指标集合。
- [Code Reviews](http://kin-y.github.io/miningReviewRepo/) - OpenStack、LibreOffice、AOSP、Qt、Eclipse 的代码审查。
- [CoREBench](http://www.comp.nus.edu.sg/%7Erelease/corebench/) - 收集了 70 个实际复杂的回归错误，这些错误是从四个开源软件项目的存储库和错误报告中系统提取的：Make、Grep、Findutils 和 Coreutils。
- [Cryptocurrency GitHub Activity and Market Cap Dataset](https://rvantonder.github.io/CryptOSS/) - 随着时间的推移，GitHub 上 200 多个加密货币项目的提交、星级、价格和市值等活动。原始历史数据也是[可用](https://zenodo.org/record/2595588#.XRuzuBNKhSM)。
- [Defects4J](https://github.com/rjust/defects4j) - 收集了 395 个可重现的错误，旨在推进软件测试研究。
- [Eclipse AERI stacktraces](http://download.eclipse.org/scava/datasets/aeri_stacktraces/aeri_stacktraces.html) - Eclipse IDE 用户遇到的异常堆栈跟踪的集合，由 AERI 报告系统检索。
- [Enron Spreadsheets and Emails](https://figshare.com/articles/Enron_Spreadsheets_and_Emails/1221767) - “安然的电子表格和相关电子邮件：数据集和分析”一文中使用的所有电子表格和电子邮件。
- [Findbugs-maven](https://github.com/istlab/maven_bug_catalog) - [Maven 存储库](https://maven.apache.org) 的 Java 项目的 FindBugs 报告集。
- [GHTorrent](http://ghtorrent.org/) - 通过 GitHub REST API 提供的可扩展、可查询、离线数据镜像。
- [GitHub Bug Dataset](http://www.inf.u-szeged.hu/~ferenc/papers/GitHubBugDataSet/) - 以静态源代码指标为特征的 15 个 Java 开源项目的 Bug 数据集。
- [GitHub on Google BigQuery](https://cloud.google.com/bigquery/public-data/github) - GitHub 数据可通过 Google 的 BigQuery 平台访问。
- [Grammar Zoo](http://slebok.github.io/zoo/) - DSL 和 GPL 语法的集合，其中一些是从元模型和文档模式中提取的。
- [KaVE](http://www.kave.cc/datasets) - 开发者工具交互数据。
- [Linux Kernel 4.21 Call Graphs](https://zenodo.org/record/2652487#.XRnvomUzb0o) - 使用 [CScout](https://github.com/dspinellis/cscout/) 生成的 Linux 内核 4.21 调用图。
- [Maven metrics](https://github.com/bkarak/data_msr2015) - [Maven 存储库](https://maven.apache.org) 的软件复杂性和大小指标集合。
- [Maven Dependency Graph](https://zenodo.org/record/1489120) - 2018 年 9 月 6 日拍摄的整个 Maven Central 的快照，存储在图形数据库中。
- [mzdata](https://github.com/jxshin/mzdata) - Mozilla 问题跟踪历史记录的多提取和多级别数据集。
- [npm-miner](https://github.com/AuthEceSoftEng/msr-2018-npm-miner) - 该数据集包含 5 个开源软件质量工具 eslint、escomplex、nsp、jsinspect 和 sonarjs 对 2000 个流行（按星数和下载量计算）npm 包的分析结果。
- [OCL Expressions on GitHub](https://github.com/tue-mdse/ocl-dataset) - 9188 个 OCL 表达式的数据集源自 245 个系统选择的 GitHub 存储库中的 504 个 EMF 元模型。
- [RepoReapers Data Set](https://reporeapers.github.io) - 数据集包含来自 GHTorrent 的_工程软件项目_的集合。
- [Software Heritage Graph Dataset](https://doi.org/10.5281/zenodo.2583978) - 来自不同来源（GitHub、Gitlab、Debian、PyPI、Google Code 等）的超过 8000 万个软件项目的开发历史和文件元数据图，采用重复数据删除且统一的表示形式（[本文](https://dl.acm.org/itation.cfm?id=3341907)）。
- [STAMINA](http://stamina.chefbe.net/download) - （状态机推理方法）数据用于对学习确定性有限状态机 (FSM) 的技术进行基准测试。
- [Stack Exchange](https://archive.org/details/stackexchange) - Stack Exchange 网络上所有用户贡献内容的匿名转储。
- [SWE-bench](https://www.swebench.com) - SWE-bench 是一个基准测试，旨在通过为开源代码存储库中发现的问题生成修复程序来评估人工智能模型解决现实世界软件工程问题的能力。
- [TravisTorrent](http://travistorrent.testroots.org) - 提供免费且易于使用的 Traivs CI 构建分析。
- [Ultimate Debian Database (UDD)](https://wiki.debian.org/UltimateDebianDatabase) - 同一 SQL 数据库中有关 Debian 各个方面的数据（例如软件包、错误、维护者）。
- [Unified Bug Dataset](http://www.inf.u-szeged.hu/~ferenc/papers/UnifiedBugDataSet/) - 基于静态源代码的数据集，包括 Bugcatchers Bug 数据集、[Bug 预测数据集](http://bug.inf.usi.ch/index.php)、[Eclipse Bug 数据集](https://www.st.cs.uni-saarland.de/softevo/bug-data/eclipse/)、[GitHub Bug数据集](http://www.inf.u-szeged.hu/~ferenc/papers/GitHubBugDataSet/)，来自 [PROMISE](http://promise.site.uottawa.ca/SERepository/datasets-page.html) 存储库的一些数据集。
- [Unix history](https://github.com/dspinellis/unix-history-repo) - Git 存储库具有 46 年 Unix 历史演变。

## 工具
- [astminer](https://github.com/JetBrains-Research/astminer) - 用于挖掘基于路径的代码表示和源自 AST 的其他数据的库和工具。
- [Boa](http://boa.cs.iastate.edu/) - 特定于领域的语言和基础设施，可简化软件存储库的挖掘。
- [buckwheat](https://github.com/JetBrains-Research/buckwheat) - 用于从源代码中提取标识符的多语言标记器。
- [ckjm](http://www.spinellis.gr/sw/ckjm/) - Chidamber 和 Kemerer Java 指标。
- [Coming](https://github.com/SpoonLabs/coming/) - 一个 Java 框架，用于分析代码更改并从 Git 存储库中挖掘更改模式的实例。
- [CryptOSS](https://github.com/rvantonder/CryptOSS) - 挖掘加密货币项目的 GitHub 活动和市值数据。
- [DbDeo](https://github.com/tushartushar/DbDeo) - 提取嵌入的 SQL 语句并检测数据库模式气味。
- [Designite](http://www.designite-tools.com) - 计算源代码指标并检测 C# 的各种实现、设计和架构气味。
- [DesigniteJava](https://github.com/tushartushar/DesigniteJava) - 计算源代码指标并检测 Java 的各种实现和设计气味。
- [Diggit](https://github.com/jrfaller/diggit) - 用于分析 Git 存储库的敏捷 Ruby 工具。
- [GitEvo](https://github.com/andrehora/gitevo) - Git 存储库的代码演化分析。
- [GrimoireLab](http://grimoirelab.github.io/) - 用于软件开发分析的免费/自由/开源工具。
- [MetricMiner](http://www.github.com/mauricioaniche/metricminer2) - 精益 Java DSL 从 Git 和 SVN 存储库中挖掘和提取数据（例如提交、开发人员、修改、差异）。
- [Maven-miner](https://github.com/diverse-project/maven-miner) - 用于解析整个 Maven 依赖关系图的 Java 工具和基础设施，以 [Neo4j](https://neo4j.com/) 图的形式托管在 Maven Central 中。
- [Perceval](https://github.com/chaoss/grimoirelab-perceval) - 从数十个后端获取存储库数据。
- [Puppeteer](https://github.com/tushartushar/Puppeteer) - 检测 Puppet 代码中的配置气味。
- [PyDriller](https://github.com/ishepard/pydriller) - 用于分析 Git 存储库的 Python 框架。
- [qmcalc](https://github.com/dspinellis/cqmetrics) - 从 C 源代码计算质量指标。
- [reaper](https://github.com/RepoReapers/reaper) - 用于计算 GHTorrent 存储库分数的 Python 工具。该分数量化了存储库中包含的项目的_设计_程度。
- [RefactoringMiner](https://github.com/tsantalis/RefactoringMiner) - 用于检测 Java 代码更改中的重构的库/API。
- [TestMiner](https://andrehora.github.io/testminer) - GitHub 存储库的软件测试分析。
- [VulData7](https://github.com/electricalwind/data7) - Java 框架支持自动收集修复 NVD 中报告的漏洞的提交（将 NVD 与 Git 链接起来）。

## 研究网点
- 专门致力于实证软件工程研究的渠道
  - [实证软件工程杂志](https://link.springer.com/journal/10664)
  - [MSR：采矿软件存储库会议](https://www.msrconf.org/)
  - [PROMISE：软件工程中的预测模型和数据分析会议](http://promise.site.uottawa.ca/SERepository/)
- 发布实证软件工程研究的渠道
  - [ACM 软件工程和方法学汇刊 (TOSEM)](https://dl.acm.org/citation.cfm?id=J790)
  - [ESEC/FSE：ACM 欧洲软件工程联合会议暨软件工程基础研讨会](https://www.esec-fse.org/)
  - [ICSE：软件工程国际会议](http://www.icse-conferences.org/)
  - [IEEE 软件杂志](https://publications.computer.org/software-magazine/)
  - [IEEE 软件工程汇刊](https://www.computer.org/csdl/journal/ts)
  - [系统与软件杂志](https://www.journals.elsevier.com/journal-of-systems-and-software)
  - [SANER：IEEE 软件分析、演化和再工程国际会议](https://ieeexplore.ieee.org/xpl/conhome.jsp?punumber=1000695)


## 许可证

[![CC0](http://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

在法律允许的范围内，[Diomidis Spinellis](http://www.spinellis.gr) 已放弃本作品的所有版权以及相关或邻接权。
