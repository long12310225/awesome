# 朱莉娅.jl

[Julia.jl](http://svaksha.github.io/Julia.jl) 聚合和整理了用于在 [Julia](https://github.com/JuliaLang) 中进行编程的知识资源的 decibans<sup>[?](https://github.com/svaksha/Julia.jl/issues/150#issuecomment-483116981)</sup>，这是一种通用编程语言，可满足高性能数值计算的需求分析和计算科学。

+ [§1。索引](#1-索引)
+ [§2。许可证](#2-许可证)
+ [§2.1。 ODbL 和 AGPLv3](#2-1-ODbL-和-AGPLv3)
+ [§2.2。镜子](#2-2-镜子)
+ [贡献](#contribute)
+ [指南](#guidelines)
+ [BugReport-PullRequest](#bugreport-pullrequest)
+ [包裹状态](#package-status)
+ [观星者](#观星者)

----

# §1.索引 <span id="1-INDEX"><span>

+ [AI](https://github.com/svaksha/Julia.jl/blob/master/AI.md) :: 算法、数据挖掘、数据结构、HMM、ML、NLP、...
+ [精算科学](https://github.com/svaksha/Julia.jl/blob/master/ActuarialScience.md) :: 与计量经济学、金融等子类别相关的软件。
+ [API](https://github.com/svaksha/Julia.jl/blob/master/API.md) :: 语言 API - C++、Fortran、Go、Java、JavaScript、MATLAB、Perl、Python、R、...
+ [生物学](https://github.com/svaksha/Julia.jl/blob/master/Biology.md) :: 生物信息学、基因组学、农业、食品科学、医学、基因工程、神经科学等。阿尔...
+ [桌面应用程序](https://github.com/svaksha/Julia.jl/blob/master/DesktopApplications.md) :: 前端客户端应用程序软件，即。调试器、文档生成器、文字处理器桌面用户界面、GUI 电子表格等。
+ [DevOps](https://github.com/svaksha/Julia.jl/blob/master/DevOps.md) :: 用于基础设施管理、持续集成 (CI)、持续交付 (CD)、包管理、发布工程 (RE)、发布管理 (RM)、软件配置管理 (SCM)、测试驱动开发、沙箱、功能/单元测试、...质量相关工具等的 DevOps 工具。
+ [化学](https://github.com/svaksha/Julia.jl/blob/master/Chemistry.md) :: 分析化学、化学信息学、晶体学、纳米化学、核化学...
+ [数据库](https://github.com/svaksha/Julia.jl/blob/master/Database.md) :: NoSQL、RDBMS 和中间件 API。
+ [数据科学](https://github.com/svaksha/Julia.jl/blob/master/DataScience.md) :: OpenData + OpenScience、免费数据集、可重复性研究、RDM、临床研究数据、元数据、图书馆数据、计算可重复性等。
+ [地球科学](https://github.com/svaksha/Julia.jl/blob/master/Earth-Science.md) :: 与制图学、气候学、地球生物学、地球化学、地理学、地理信息学、地质学、地球物理学、地球科学/GIS、地球数学、气象学、海洋学等子类别相关的软件...
+ [FileIO](https://github.com/svaksha/Julia.jl/blob/master/FileIO.md) :: 文件 IO（输入/输出）功能以及对各种数据类型和文件格式的支持。
+ [图形](https://github.com/svaksha/Julia.jl/blob/master/Graphics.md) :: 绘图、图形和其他可视化工具。
+ [i18n-L10n](https://github.com/svaksha/Julia.jl/blob/master/i18n-L10n.md) :: 音译、国际化 (i18n) 和本地化 (L10n)
+ [Machines](https://github.com/svaksha/Julia.jl/blob/master/Machines.md) :: 用于跨平台硬件、机器人和其他机器相关软件的 API 库的软件。
+ [数学](https://github.com/svaksha/Julia.jl/blob/master/Mathematics.md) :: 代数、几何……任何与数学相关的内容。
+ [优化](https://github.com/svaksha/Julia.jl/blob/master/Optimization.md) :: 数学优化。
+ [物理](https://github.com/svaksha/Julia.jl/blob/master/Physics.md) :: 与物理相关的 Julia 软件。
+ [编程范式](https://github.com/svaksha/Julia.jl/blob/master/Programming-Paradigms.md) :: 类型系统、数据类型等中使用的编程范式和语言概念。
+ [出版物](https://github.com/svaksha/Julia.jl/blob/master/Publications.md) :: 研究论文（期刊和会议出版物）。
+ [QA](https://github.com/svaksha/Julia.jl/blob/master/QA.md) :: Julia 的质量保证。
+ [资源](https://github.com/svaksha/Julia.jl/blob/master/Resources.md) :: 社区资源列表、开发链接，包括活动、（非）会议、论坛/聚会小组、新闻、博客、食谱、备忘单、IJulia NoteBooks 和其他有用资源。
+ [服务器](https://github.com/svaksha/Julia.jl/blob/master/Server.md) :: HTTP/Web、网络和其他服务器端实用程序...
+ [空间科学](https://github.com/svaksha/Julia.jl/blob/master/Space-Science.md) :: 天文学、成像、行星和[空间科学](https://en.wikipedia.org/wiki/Outline_of_space_science) 相关软件包。
+ [概率与统计](https://github.com/svaksha/Julia.jl/blob/master/Probability-Statistics.md) :: 精算科学、金融、经济学、随机、保险统计、运筹学以及基准和优化工具包...
+ [超级计算](https://github.com/svaksha/Julia.jl/blob/master/Super-Computing.md) :: HPC、分布式计算、云计算、集群计算、网格计算、内核和架构，如 ARM、MIPS、GPU、CUDA 等...
+ [实用程序](https://github.com/svaksha/Julia.jl/blob/master/Utilities.md) :: 方便的工具包和其他桌面通用实用程序。

**免责声明：** 作为科学计算领域的一种新语言，由于新库的添加，它经常处于不断变化的状态，导致频繁的更改和页面重新排序。由于 **Julia.jl** 存储库仅提供 Julia 软件包的列表（链接），因此不应将其视为对任何特定软件包的软件质量、技术功能、编码风格/组织等的认可...

----

#§2.许可证 <span id="2-LICENSE"><span>

+ 版权 © 2012-Now [SVAKSHA](http://svaksha.com/pages/Bio)，特此分别获得数据 (ODbL-v1.0+) 和软件 (AGPLv3+) 的双重许可。

## §2.1。 AGPLv3 和 ODbL <span id="2-1-AGPLv3-and-ODbL"><span>
该存储库使用数据和代码的多个许可证，即。 [ODbL](https://opendatacommons.org/licenses/odbl/1-0/) 和 [AGPLv3](http://www.gnu.org/licenses/agpl-3.0.html)

+ 此存储库 (`Julia.jl`) 中的 __data__ （Julia 语言知识资源的聚合和整理分贝）是根据 [开放数据库许可证](https://opendatacommons.org/licenses/odbl/1-0/) (ODbL-v1.0) 发布的。开放数据库许可证 (ODbL) 授予任何人共享、创建和改编数据或数据库的自由，并具有许可证中指定的适当的__信用归属__，并__在相同条款下提供任何新作品__，以及__如果将新作品用于商业目的__则发布公共副本__。
+ `Julia.jl` 中使用的 __software__ 是根据 [AGPLv3 许可证](http://www.gnu.org/licenses/agpl-3.0.html) 及以上版本发布的，详见 [LICENSE-AGPLv3.md](https://github.com/svaksha/Julia.jl/blob/master/LICENSE-AGPLv3.md) 文件。
+ 本作品的所有副本和分支必须在新作品的所有副本或主要部分中保留版权、程序代码 (AGPLv3) 和数据 (ODbL) 的相应许可文件以及本许可声明。

这一变化的动机是让人们更容易地重复使用这些数据作为数据库中的知识资源。例如，[julia-observer](https://juliaobserver.com) 是一个可视化工具，用于浏览从“Julia.jl”、“General”和各种来源提取数据的包。通过[公开](https://github.com/djsegal/julia_observer)发布网站代码，这是一个关于如何构建或转换数据以使社区受益的示例。

## §2.2。镜子 <span id="2-2-Mirrors"><span>

+ [Bitbucket](https://bitbucket.org/svaksha/Julia.jl) :: git 克隆 git@bitbucket.org:svaksha/Julia.jl.git
+ [GitLab](https://gitlab.com/svaksha/Julia.jl) :: git 克隆 git@gitlab.com:svaksha/Julia.jl.git

----

# 贡献

欢迎以拉取请求 (PR) 的形式对“Julia.jl”进行[贡献](https://github.com/svaksha/Julia.jl/graphs/contributors)。以下是有关如何提交错误报告 (BR) 和/或 [PR](https://github.com/svaksha/Julia.jl/pulls) 的一些准则和提示：


## 指南

1. Julia 社区制定了旨在尊重版权、许可和归属标准<sup>{1}和{2}</sup>的[道德准则](http://julialang.org/community/standards/)，要求您在提交要列出的材料时遵循这些准则。此外，如果您发现任何违反这些道德标准的材料（或代码库），请提交错误报告，以便将其从“Julia.jl”中删除。
+ 参考文献：
+ {1} https://github.com/JuliaLang/julialang.github.com/issues/200
+ {2} https://github.com/JuliaLang/julialang.github.com/issues/194
2. __商业链接__：本仓库中的资源几乎都是Free/Libre软件资源，因此为了继续维护“Libre”软件精神，请仅提交那些免费且无付费/商业利益的资源。


## BugReport-PullRequest

1. 根据主题子部分中的顶级类别页面，按_字母顺序_添加链接，并在 Markdown 文件中添加注释（如果有）。在各个类别中创建新的顶级标签之前，请先查看维基百科或其他资源。如果您无法决定，请通过 BR（而不是 PR ;-)）进行讨论。
2. 在 CLI 中，输入“julia Julia.jl”，这将运行 [scraper](https://github.com/svaksha/Julia.jl/blob/master/src/scrape.jl)。也提交“db.csv”文件。
3. 对于损坏的链接或过时的信息，请提交错误报告 (BR)，或进行必要的更改并提交 PR。两者都受到欢迎。请为添加的每个链接或更改提交单独的 PR。
4. 对于文档和食谱，检查它是否与列出的类别匹配，否则，将其列在 [Resources.md](https://github.com/svaksha/Julia.jl/blob/master/Resources.md) 页面上。
5. 对于那些无法使用 git 的人，请创建一个 github 帐户，然后在用户界面上分叉 `Julia.jl` 存储库。然后通过[单击 Markdown 页面上的“铅笔”图标](https://help.github.com/articles/editing-files-in-your-repository) 编辑页面，然后单击“保存”并提交 PR。 Github [通过 8 个步骤自动完成](https://help.github.com/articles/editing-files-in-another-user-s-repository)。


## 包裹状态

请注意，此存储库列出了过时的和/或适用于旧版本 Julia 的软件包。这些仍然被列为公开可用，并希望有人可能希望继续将这项工作作为一个分支，因为它与他们的研究或工作相一致。这些[评论](https://github.com/svaksha/Julia.jl/commit/a884fe9e921d57b87d85e970c2f57b8f21025641#commitcomment-15802037)导致[BR讨论](https://github.com/svaksha/Julia.jl/issues/55)添加元数据标签，这将使程序员和包用户能够轻松区分处于不同开发阶段的各种 Julia 包的状态。目前，METADATA 有一个标签系统，但并非所有软件包作者都使用它，这使得非专业用户更难知道软件包维护是否处于活动状态。

让我们尝试要求包作者和核心提交者根据以下标准标记他们的 Julia 包：

请按照 1 到 5 的等级（1=最低，..5=最高）对您的包裹进行排名，

+ `可用性`：该软件包是否按照其所说的那样工作？容易弄清楚吗？软件包是否已做好生产准备并积极维护（问题/PR 得到及时响应和解决，维护和测试与 Julia 发布周期一致）。
+ `质量`：该包是否经过测试？有很多错误吗？你有好的文档吗？它可以用于需要及时提供安全补丁的生产环境吗？
+ `Activity` ：第 3 方用户是否应该费心使用您的库，或者它真的仅供包作者使用？比方说，一个实验性的“一次性玩具回购”，其开发现已被放弃。
+ `许可证` ：您使用哪个软件许可证？如果您没有许可证，请注明“无”。


## 观星者

[![Stargazers over time](https://starchart.cc/svaksha/Julia.jl.svg)](https://starchart.cc/svaksha/Julia.jl)
      
