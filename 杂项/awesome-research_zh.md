# 很棒的研究工具

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

研究工具列表。也可在 [https://tools.kausalflow.com/tools/](https://tools.kausalflow.com/tools/) 上获取。

## 总有机碳

* [有条理](#be-organized)
  * [版本控制系统](#version-control-system)
  * [Pomodoro](#pomodoro)
  * [GTD-任务管理器](#gtd-task-manager)
* [云服务](#cloud-services)
  * [数学和编程](#math-and-programming-online)
  * [Plots](#plotting-and-charting-online)
  * [Data](#datasets)
  * [Colors](#colors)
* [发布与分享](#publishing-and-sharing)
  * [Writing](#writing)
  * [Hosting](#hosting)
  * [博客和内容管理系统](#blog-and-cms)
  * [静态站点生成器](#static-site-generator)
* [做笔记](#note-taking)
  * [Editors](#editors)
  * [Markdown](#markdown)
  * [LaTeX](#latex)
  * [iPython 笔记本](#ipython-notebook)
  * [Mindmap](#mindmap)
  * [概念图和图表](#concept-map-and-diagrams)
  * [保留笔记](#keep-the-notes)
* [演示工具](#presentation-tools)
  * [在线加载和编辑](#online-load-and-edit)
  * [使用来源](#use-the-source)
  * [IPython笔记本](#ipython-notebook)
  * [乳胶投影仪](#latex-beamer)
  * [Mathematica](#mathematica)
  * [SVG 的力量](#the-power-of-svg)
  * [分享幻灯片](#sharing-slides)
* [Programming](#programming)
  * [Softwares](#softwares)
  * [代码编辑器](#code-editors)
  * [科学计算](#scientific-computing)
  * [编码很有趣](#coding-is-fun)
* [Academic](#academic)
  * [Self-plagiarism](#self-plagiarism)
  * [调查论文](#investigate-papers)
  * [为自己获取任何可引用的代码](#get-yourself-a-citable-code-for-anything)
  * [开放科学](#open-science)
  * [给研究人员的建议](#tips-for-researchers)
* [Pacifier](#pacifier)
* [在线讨论](#online-discussions)
* [开源](#open-source)
  * [开放许可证](#open-licenses)
  * [使用许可证](#use-licenses)
  * [Bibliography](#bibliography)
* [数据可视化和图表制作](#data-visualization-and-graph-making)
  * [数据可视化](#data-visualization)
  * [图表制作](#graph-making)
* [LaTeX](#latex-1)
  * [Tips](#tips)
  * [Symbols](#symbols)
  * [Graphing](#graphing)
  * [Fonts](#fonts)
  * [Templates](#templates)
  * [References](#references)
* [MISC](#misc)
  * [Terminal](#terminal)
  * [免费多媒体](#free-multimedia)
  * [有趣的期刊](#interesting-journals)
  * [More](#more)


## 有组织


### 版本控制系统

> 首先，每个人都应该了解版本控制系统，又名 VCS。 VCS 帮助我们跟踪文档中的更改以及文档上的协作。不用说，版本控制是科学家最有用的工具之一。

* **git**
* SVN
* 善变的


#### 在线 Git 服务

* [GitHub](https://github.com/)：最流行的内置社交和协作功能的 git 平台。
* GitHub 还提供 GitHub Actions。通过操作，我们可以实现流程自动化。
* GitHub 提供 GitHub 页面。借助 GitHub Pages，可以托管静态文件以及 [Jekyll](https://jekyllrb.com) 构建的网站。
* [GitLab](https://about.gitlab.com/)：与 GitHub 类似，GitLab 提供 git 托管、协作、社交、自动化等。 GitLab 既可以基于云，也可以使用其开源代码进行自托管。
* GitLab 包含无限的免费私人存储库。
* GitLab 附带了比 GitHub Actions 更强大的持续集成工具。
* [BitBucket](https://bitbucket.org)：替代 GitHub 和 GitLab，提供免费的私有存储库。


#### 自托管 Git 服务器

* [GitLab](http://gitlab.org/)：参见上面的[在线 Git 服务](#online-git-service)。
* [Gitea](https://gitea.io/en-us/)：用 Go 编写的无痛自托管 Git 服务。
* [Gogs](https://gogs.io/)：一个轻松的自托管 Git 服务。


#### 企业Git服务

* [RhodeCode](https://rhodecode.com/)：分布式存储库的集中控制。 Mercurial、Git 和 Subversion 在同一屋檐下。


### 番茄钟

> [番茄工作法](https://en.wikipedia.org/wiki/Pomodoro_Technique) 可用于提高您的工作效率并可能改善您的健康。工具的选择几乎是无限的。

* [Pomotodo](https://pomotodo.com/) (`Cloud`,`Mac`,`Win`,`Android`,`iOS`,`Chrome`)：待办事项列表和番茄计时器的混合，跨设备同步和每周报告[免费]。
* [Tadam](https://tadamapp.com/) (`Mac`)：简单优雅的番茄计时器 [USD$ 4.99]。
* [生产力挑战计时器](https://play.google.com/store/apps/details?id=com.wlxd.pomochallenge&hl=en) (`Android`)：具有出色游戏化功能的番茄计时器[免费]。


### GTD-任务管理器

> GTD（完成任务）方法通过使用外部工具记录待办事项列表，从而将其从头脑中卸载。它允许人们专注于一项活动任务，而不是所有任务（[维基百科](https://en.wikipedia.org/wiki/Getting_Things_Done)）。
> 任务可以按上下文（@home、@computer、@office 等）、操作时间（现在、下一步、计划或某天）和项目进行分类。 [此处](https://hamberg.no/gtd/) 我们有一份很好的 GTD 实用指南，[此处](https://gettingthingsdone.com/pdfs/tt_workflow_chart.pdf) 是一个流程图。

* [微软待办](https://todo.microsoft.com/tasks) (`Cloud`,`Mac`,`Win`,`Android`,`iOS`,`Win Store`,`Chrome OS`): 近乎完美的待办事项列表，具有协作和共享功能。
* [Google Keep](https://keep.google.com/)(`云`、`Android`、`iOS`、`Chrome 操作系统`)
* [Evernote](https://evernote.com/)（`Cloud`、`Mac`、`Win`、`Android`、`iOS`、`Win Store`）：不是那么轻量级，但仍然非常适合管理生活，特别是因为它与许多其他服务进行了大量集成。
* [Anydo](https://www.any.do/) (`Cloud`,`Mac`,`Android`,`iOS`)：很好，因为它有很好的每日回顾，可以帮助用户记住要做什么。
* [Todoist](https://todoist.com/)（`Cloud`、`Mac`、`Win`、`Android`、`iOS`）：Todoist 发明了业力系统，可以跟踪已完成的任务。
* [Taskade](https://taskade.com/)（`Cloud`、`Mac`、`Win`、`Chrome OS`、`Firefox`、`Android`、`iOS`）：Taskade 是团队项目的协作任务列表和大纲。
* [议程](https://agenda.com/)(`Mac`)：以日期为中心的笔记。


## 云服务

*对于自托管服务，请查看 GitHub 上的 [awesome-selfhosted](https://github.com/Kickball/awesome-selfhosted)。*


### 在线数学和编程

> 有许多工具允许使用代码、在线进行数值计算或分析推导。

* [Google Colab](https://colab.research.google.com/)：免费的在线 jupyter 笔记本。 Google Colab 还提供免费的 GPU 时间。
* 免费且功能强大。
* 在同一笔记本上共享和协作。
* 可以保存在 GitHub 或 Google Drive 中。
* [NextJournal](https://nextjournal.com/)：用于可重复研究的笔记本。
* 基本上，NextJournal 几乎可以运行任何内容。
* 注重再现性。
* [Kaggle](https://www.kaggle.com/)：kaggle 内置免费的 jupyter 笔记本。
* 还可以连接Google BigQuery来访问大数据。
* [Azure Notebooks](https://notebooks.azure.com/)：在线 jupyter 笔记本。
* [Datalore](https://datalore.io/)：JetBrains 的在线 jupyter 笔记本。
* [CoCalc (SageMathCloud)](https://cocalc.com/)：LaTeX、R、iPython Notebook 等。
* [SageMaker](https://aws.amazon.com/sagemaker/)：集成了很多工具的AWS服务。 Sagemaker 附带 Sagemake Studio，它为程序员提供 jupyter 笔记本以及其他图表和数据管理工具。
* [WolframAlpha](https://www.wolframalpha.com/)：优秀的在线数学推导和搜索引擎。
* [Mathematica Online](https://www.wolfram.com/mathematica/online/)：在云中将 Mathematica 变为现实。



### 在线绘图和制图

> 虽然可以使用上面提到的这些在线 jupyter 笔记本来绘制绘图，但也有许多易于使用的笔记本可以用于简单的绘图。

* [plot.ly](https://plot.ly/)：集成了许多云服务的在线绘图。
* [Desmos](https://www.desmos.com/calculator)：函数图表。
* [GeoGebra](https://www.geogebra.org)：很旧，但仍然非常好。 GeoGebra 可用于精确制图和计算。
* [graph.tk](http://graph.tk/)：功能丰富的在线绘图。
* [Wolfram Alpha](http://www.wolframalpha.com/)：根据您的数据甚至更多数据制作函数图表。
* [SankeyDiagram.net](https://sankeydiagram.net/)：用于从数据创建和共享 Sankey 图的基于 Web 的工具（开源）


### 数据集

> Nature 在[此处](https://www.nature.com/sdata/policies/repositories) 托管了推荐的数据存储库列表。

#### 普通和跨学科

* [DRYAD](http://datadryad.org/)（`Storage`、`Lookup`）：Dryad 数字存储库存储精选数据。
* [Figshare](https://figshare.com/) (`Storage`, `Lookup`)：数据共享和存储
* [Data.gov](https://data.gov) (`Lookup`)：美国联邦政府的数据

#### 生命科学

* [GenBank](https://www.ncbi.nlm.nih.gov/genbank/) (`Lookup`)：基因序列数据库
* [国家环境信息中心](https://www.ncei.noaa.gov/) (`Lookup`)：天气、气候、海岸、海洋和地球物理等
* [GEOSS Portal](http://www.geoportal.org) (`Lookup`)：地球科学数据

#### 物理科学

* [美国虚拟天文台](http://www.usvao.org/) (`Lookup`)
* [MAST：Barbara A. Mikulski 太空望远镜档案](https://mast.stsci.edu/portal/Mashup/Clients/Mast/portal.html) (`Lookup`)
* [米库斯基太空望远镜档案](http://archive.stsci.edu/) (`Lookup`)

#### 艺术与人文

* [考古数据服务](http://archaeologydataservice.ac.uk/) (`Lookup`)：认证存储库

#### 工程

* [开放能源信息 (OpenEI)](http://en.openei.org/wiki/Main_Page) (`Lookup`)：能源信息集合的 Wiki

#### 社会科学

* [大学间政治与社会研究联盟 (ICPSR)](https://www.icpsr.umich.edu/web/pages/) (`Lookup`)
* [定量社会科学研究所 (IQSS)](http://library.harvard.edu/gdc) (`Lookup`)
* [Voidly Censorship Index](https://voidly.ai/data)（`Lookup`、`API`）：全球互联网审查的开放数据集 — 1960 万个实时 OONI 样本、160 万条跨越 119 个以上国家/地区的历史记录、5,356 个可引用事件以及 16,822 个证据项。 CC BY 4.0、REST/MCP API、[HuggingFace 镶木地板导出](https://huggingface.co/datasets/emperor-mew/global-censorship-index)。


### 颜色

> 为您的演示文稿和笔记选择一种令人愉悦的颜色。
> 参考【数据可视化与图表制作】(#data-visualization-and-graph-making)

* [ColorBrewer](http://colorbrewer2.org)
* [Paletton](http://paletton.com)
* [颜色计算器](https://www.sessions.edu/color-calculator/)


## 发布与分享


> 利用[GitHub](http://github.com)与他人合作。 [GitHub 页面](https://pages.github.com/) 也适合托管静态内容。
> GitHub 提供教育福利，以便学生可以获得带有私人存储库的免费专业版。


### 写作

**Markdown 是最好的写作语言之一。** 在 [Markdown 部分](#markdown) 中查看这些编辑器。

**利用这些程序进行发布：**

* [Sphinx](http://sphinx-doc.org)：RestructedText作为源文件，功能强大、灵活且模块化。
* [Gitbook](https://www.gitbook.com/)：一个新的但有前途的 HTML、pdf 和 epub 工具，具有在线编辑器和本地编辑器。测验和数学等插件有助于撰写科学文章。
* [Git-scribe](https://github.com/schacon/git-scribe)：适合编写电子书。
* [静态站点生成器](#static-site-generator): 更多信息请参阅[静态站点生成器](#static-site-generator)。


**Sphinx 主题和配置**

* [rtd 主题](https://github.com/snide/sphinx_rtd_theme)：由 ReadtheDocs.org 开发
* [Alabaster](https://github.com/bitprophet/alabaster)：干净简单
* [引导主题](https://ryan-roemer.github.io/sphinx-bootstrap-theme/)


**使用 Sphinx 的科学书籍**

> 以下是有关如何使用 sphinx 进行研究的一些示例。

* [理论物理](https://github.com/certik/theoretical-physics)
* [统计物理](https://github.com/emptymalei/statisticalphysics)
* [中微子物理学](https://github.com/NeuPhysics/neutrino)


**书写工具**

> 只需使用 [Visual Studio Code](https://code.visualstudio.com/)。

* [Hemingway App](https://hemingwayapp.com/)：突出显示复杂句子，指出被动语态，并建议替代词。
* [proselint](https://github.com/amperser/proselint)：使用 *Garner 的现代美国用法* 等建议的英语散文的 linter。
* [write good](https://github.com/btford/write-good)：用于英语散文的 Naive JavaScript linter。
* [artbollocks-mode](https://github.com/sachac/artbollocks-mode)：Emacs 次要模式，用于在撰写有关艺术（或其他主题）时避免陈词滥调和错误的语法。
* [`cut_the_crap.py`](https://jugad2.blogspot.com/2015/07/cut-crap-absolutely-essential-tool-for.html)：简单的 Python 脚本，用于标记冗余单词并提供替代建议。
* [Rousseau](https://github.com/GitbookIO/rousseau)：用 JavaScript 编写的轻量级校对器。
* [textlint-rule-rousseau](https://github.com/azu/textlint-rule-rousseau): 使用 Rousseau 检查英语句子的 textlint 规则。
* [De-Jargonizer](http://scienceandpublic.com/)：粘贴您的文章或上传文件以分析您的写作中的行话数量。


### 托管

> 托管您的文章、笔记等。研究还涉及通信。

* [ReadtheDocs](http://readthedocs.org/)：将您的 reStructuredText 源文件转换为 HTML、PDF 和 epub，全部在线完成。
* [GitHub 页面](https://pages.github.com/)：与 Jekyll 集成并自动转 Markdown 帖子。 Jekyll 是一个博客工具。
* [GitHub](http://github.com): 只需将 markdown、reStructuredText、PDF 或 IPython/Jupyter 笔记本文件放在 GitHub 上即可。所有这些格式都可以在线预览。 **值得一提的是，IPython Notebook 中的数学可以在 GitHub 上呈现。**
* [Surge](https://surge.sh/)：一个命令上传您的静态网站以使其上线。 Surge 还集成了 GitHub hooks。
* [Heroku](https://www.heroku.com/)：无需解释的。
* [AWS](https://aws.amazon.com/)：亚马逊 AWS 提供学生福利。

> 其他服务，例如 [Digital Ocean](https://www.digitalocean.com/) 在动态网站和云计算方面也很有用。


### 博客和内容管理系统

> 在进行平台调查之前，提醒自己：
>
> **我想写作，而不是运行博客软件。**


**博客/CMS 软件**

> 这些程序在服务器上运行，并且可以[使用这些服务托管](#hosting)。

* [GitBook](https://www.gitbook.com/) (`Cloud`)：用 Markdown 编写并与团队协作。 GitBook 与 GitHub 集成，因此不会丢失任何内容。
* [Ghost](https://github.com/tryghost/Ghost) (`Node.js`)：开放、简单、非营利；使用 Markdown 和实时预览进行编写。
* [Pico](https://github.com/picocms/Pico) (`PHP`)：轻量级cms，开源，无数据库。
* [Dropplets](https://github.com/circa75/dropplets) (`PHP`)：开源、简单、优雅的博客系统；用 Markdown 写。
* [Wordpress](https://wordpress.org/) (`PHP`)：非常流行，但需要大量维护。


**这些博客/CMS软件可以托管在[Digital Ocean](https://www.digitalocean.com/)上。**


### 静态站点生成器

> [这是一个不错的网站](https://staticsitegenerators.net/)，它告诉您所有静态站点生成器。尽管如此，这里还是最受欢迎的列表。

* [Jekyll](http://jekyllrb.com/) (用 `Ruby` 编写)(`Markdown`)：Jekyll 是使用最广泛的一种。 Jekyll 最好的部分是，只需将源代码推送到 GitHub 即可部署到 GitHub Pages。
* [Octopress](http://octopress.org/) (Written in `Ruby`)(`Markdown`)：与 Jekyll 相比，Octopress 更容易使用，同时与 Jekyll 有一定的兼容性。
* [Hexo](https://hexo.io/)（用 `Node.js` 编写）(`Markdown`)：正如他们在网站上所说的“一个快速、简单且强大的博客框架”。支持GFM。
* [Pelican](http://getpelican.com)（用 `Python` 编写）(`reStructuredText`,`Markdown`,`AsciiDoc`)：Pelican 是一个模块化框架，非常适合博客。
  * [鹈鹕 Svbtle 主题](https://github.com/wting/pelican-svbtle)
* [Nikola](https://getnikola.com/)（用 `Python` 编写）（`reStructuredText`、`Markdown`、`IPython Notebook/Jupyter`、`PHP` 等）：它采用多种输入格式，包括 reStructuredText 和许多其他格式。
* [Hugo](http://gohugo.io/)(用 `Go` 编写)(`Markdown`)：易于使用且速度非常快。它还通过插件支持更多的输入格式。
* [Hyperdraft](https://hyperdraft.rosano.ca)(用 `JavaScript` 编写)(`Markdown`)：在您输入纯文本或 Markdown 时自动生成网站。


> 这些程序生成的站点可以托管在 [GitHub Pages](https://pages.github.com/) 上。


## 做笔记

### 研究人员笔记本

* [Findings](https://findingsapp.com)：您的研究助理和实验室笔记本，尽在一个应用程序中。
* [Learnly AI](https://learnlyai.co.uk/)：为学生提供人工智能驱动的学术助手，具有智能讲座、PDF 和视频笔记、带有文献综述的论文写作以及人工智能演示生成器。

### 编辑

> Markdown、LaTeX 和 reStructuredText 是三种有用的语言。
> **在大多数情况下，可调整的文本编辑器，例如 [Visual Studio Code，又名 vscode](https://code.visualstudio.com) 就足够了。** 事实上，vscode 附带了大量扩展，可用于构建您自己的 IDE。


#### 降价

* [Hackmd.io](https://hackmd.io) (`Cloud`)：基本上提供了您对最完整的在线 Markdown 编辑器的所有期望。
* [StackEdit](https://stackedit.io/)(`Cloud`)：StackEdit 是一个 Markdown 编辑器，集成了许多服务，例如数学 (MathJax)、Google Drive、Dropbox 和 GitHub。
* [CMD markdown](https://www.zybuluo.com/mdeditor)(`Cloud`): CMD 是一个支持数学 (MathJax) 的 Markdown 编辑器。特殊之处在于它保留编辑历史记录。 （中文用户界面。）
* [Penflip](https://www.penflip.com/)(`Cloud`)：Penflip 旨在成为作家的 GitHub。它基于 Markdown，类似于 git，没有数学支持。
* [Authorea](https://www.authorea.com/)(`Cloud`)：一个更强大的 Markdown 和 LaTeX 在线编辑器，可用于生成优秀的学术论文。
* [Dillinger](http://dillinger.io/)(`Cloud`)：Markdown 编辑器，但没有数学模式。
* [Pandoc Markdown](http://pandoc.herokuapp.com/)(`Cloud`)：另一个支持数学 (MathJax) 的 Markdown 编辑器。
* [Marxico](http://marxi.co/)(`Cloud`,`Mac`,`Win`,`Chrome`): Markdown editor that integrates with Evernote, generates pdf and works offline. [马克飞象](https://maxiang.io/)(`Cloud`,`Mac`,`Win`,`Chrome`) is the Chinese version。
* [Madoko](https://www.madoko.net/)(`Cloud`,`Chrome`)：一款支持数学的 Markdown 编辑器，一键轻松插入图像，同时您的文件保存在 Dropbox、GitHub、OneDrive 或本地磁盘上。它生成 pdf 和 HTML 页面，并使用浏览器的本地存储离线工作。甚至可以导入 LaTeX 文件。
* [Markx](http://markx.herokuapp.com/)(`Cloud`)：用于科学写作的 Markdown 编辑器。含电池。
* [typora](https://www.typora.io/)(`Mac`,`Win`)：漂亮的用户界面和现场实时预览。
* [Haroopad](http://pad.haroopress.com/)(`Mac`,`Win`,`Linux`)：一个强大的 github 风格的 Markdown 编辑器，具有有用的扩展。支持数学 (mathjax)。
* [jbt/markdown-editor](http://jbt.github.io/markdown-editor/)(`Cloud`)：只是另一个没有数学支持的在线 Markdown 编辑器。
* [MarkdownPad](http://markdownpad.com/) (`Win`)：如果你对.NET没有不好的感觉，这相当不错。
* [ReText](https://github.com/retext-project/retext) (`Mac`,`Win`,`Linux`)：ReText 是最好的之一，即使在 Linux 上也是如此。它还支持 reStructuredText 输入。
* [Madoko](https://www.madoko.net/) (`Cloud`): **LaTeX** ×; Markdown &sup2;
* [eme](https://github.com/egoist/eme) (`Win`,`Mac`,`Linux`)：数学支持。
* [Moeditor](https://moeditor.org/) (`Win`,`Mac`,`Linux`)：通用 Markdown 编辑器。

可以用 Markdown 编写的笔记本软件：

* [boostnote](https://boostnote.io/) (`Win`,`Mac`,`Linux`)：Math + Markdown，支持片段注释。
* [Quiver](http://happenapps.com/) (`Mac`,`iOS`)：程序员的笔记本，数学+ Markdown，代码片段。
* [Findings](http://findingsapp.com/) (`Mac`)：实验者笔记本，整理研究材料和笔记。
* [Notion](https://www.notion.so/) (`Win`,`Mac`,`iOS`,`Android`): 用看板、数学、日历、表格等做笔记。
* [议程](https://agenda.com/)（`Mac`、`iOS`）：注释和 GTD。


#### 乳胶


* [Overleaf](https://www.overleaf.com/)(`Cloud`)：内置版本控制、Dropbox 和 GitHub 集成、预览、协作、简单的 UI。它还提供了很多模板。
* [Authorea](https://www.authorea.com/)(`Cloud`)：易于使用的用户界面。支持 Markdown 和 LaTeX。
* [Papeeria](https://www.papeeria.com)(`Cloud`)：另一个带有绘图编译器和协作的在线 LaTeX 和 Markdown。
* [JaxEdit](http://jaxedit.com/)(`Cloud`)：JaxEdit 不提供完整的 LaTeX 支持，但对于简单的 LaTeX 文档和幻灯片来说已经足够了。
* [SpicyChai LaTeX](https://latex.spicychai.com/)(`Cloud`)：在线 LaTeX 编辑器，具有 AI 驱动的模板填充、实时 PDF 预览以及用于简历、论文等的预构建模板。无需注册即可免费匿名渲染。


**您也可以使用自己的机器托管一个。**


* [Overleaf 源代码](https://github.com/overleaf/overleaf): Overleaf 开源了他们的代码。我想说，这是一个伟大的举动。
* [TeXStudio](http://www.texstudio.org) - 源自 TeXMaker 的跨平台 LaTeX 编辑器。
* [WinEdt](http://www.winedt.com) - 许多人都信赖的 LaTeX 编辑器。
* [TeXnicCenter](http://www.texniccenter.org) - 一个相当古老但免费且不错的 LaTeX 编辑器。
* [LyX](https://www.lyx.org) - 跨平台所见即所得编辑器，在幕后使用 LaTeX 来渲染文档。
* [TeXshop](http://pages.uoregon.edu/koch/texshop/) - MacTeX 中包含的 LaTeX 文档的严肃编辑器。
* [TeXWorks](https://www.tug.org/texworks/) - 这是一款实用的 LaTeX 代码编辑器，以 TeXShop 为蓝本，但它是跨平台的。

**您还可以直接在学术论文中添加注释**

* [Synthical](https://synthical.com) - 聚合来自 arXiv、medRxiv、bioRxiv 和 chemRxiv 的所有论文，并能够突出显示和留下注释。

### IPython笔记本

使用 IPython Notebook 来帮助您进行研究。 IPython Notebook可以直接在GitHub上预览。以下是如何使用 IPython Notebook 的一些示例。

* [科学Python讲座](https://github.com/jrjohansson/scientific-python-lectures)
* [转载论文](http://reproduced-papers.github.io/)
* [更多](https://github.com/ipython/ipython/wiki/A-gallery-of-interesting-IPython-Notebooks)：有关 GitHub 上的更多 IPython 笔记本，请阅读这个庞大的列表。



### 思维导图

**独立**

* 心灵经理
* XMind
* 多西尔

**在线**

* [KityMinder 来自百度](https://github.com/fex-team/kityminder) : 中文界面
* [my-mind](http://my-mind.github.io/)：repo [此处](https://github.com/ondras/my-mind)。
* [美丽心灵](http://beautifulmind.io/): repo [此处](https://github.com/ierror/BeautifulMind.io)
* [Mindmup](https://www.mindmup.com/)：repo [此处](https://github.com/mindmup)
* [思维导图](http://drichard.org/mindmaps/)：repo [此处](https://github.com/drichard/mindmaps)


**思维导图 HTML**

* [gojs](http://gojs.net/latest/samples/mindMap.html)
* [jsmind](https://github.com/hizzgdev/jsmind)
* [jsmind](http://sourceforge.net/projects/jsmind/)
* [mindmaps](https://github.com/drichard/mindmaps)


### 概念图和图表

1. [Gliffy](https://www.gliffy.com/)：各种图表
2. [ProcessOn](http://www.processon.com/)：各种图表
3. [Draw.io](http://www.draw.io/)：各种图表


### 保留笔记


> 跟踪笔记的更改总是更好，**git** 是一个不错的选择。因此，[GitHub](http://github.com) 是近乎完美的地方。
>
> 对于 LaTeX，[latexdiff](http://www.ctan.org/tex-archive/support/latexdiff/) 是一个检查差异的工具。

> **某些程序允许您将 Markdown 笔记保存在服务器上。**

* [Raneto](http://raneto.com/)：Raneto 是一个开源知识库平台，它使用静态 Markdown 文件来支持您的知识库。这个看起来很好看。
* [Realms](http://realms.io/)：受 Gollum、Ghost 和 Dillinger 启发，用 Python 编写的基于 Git 的 wiki。包括基本身份验证和注册。
* [Tiddlywiki](http://tiddlywiki.com/)：一个独特的非线性笔记本，用于捕获、组织和共享复杂信息。
* 一些其他[静态站点生成器](#static-generator)。

为了进行实验研究，eLabFTW制作了一个在线实验笔记系统：[eLabFTW](https://www.elabftw.net/)。




## 演示工具

### 让你的电脑保持清醒

> 在演示过程中保持计算机处于唤醒状态非常重要。除了更改电源选项之外，以下工具也可以完成这项工作。


* [咖啡因](https://itunes.apple.com/us/app/caffeine/id411246225) (`Mac`)：只需单击一下即可。
* [安非他明](https://itunes.apple.com/us/app/amphetamine/id937984704?mt=12) (`Mac`)：涉及更多配置，更智能。


### 在线加载和编辑


* 如果可以的话，[Prezi](https://prezi.com/)。
* [slides.com](http://slides.com/)：易于使用，可远程控制页面演示。
* [Slideas](https://www.slideas.app/)：创建精美 Markdown 演示文稿的最简单方法，具有您需要的所有功能。
* [Google Drive](https://drive.google.com/)：无需介绍
* [Sway](https://sway.com/)：微软
* [Strut](https://github.com/tantaman/Strut)
* [Impressionist](https://github.com/harish-io/Impressionist)
* [hovercraft](https://github.com/regebro/hovercraft)



### 使用来源

> 需要一些前端技术。

#### HTML+CSS+JS

> 使用 [颜色](https://github.com/mrmrs/colors) 让您的 HTML 感觉更好。

* [Impress.js](http://impress.github.io/impress.js/)：更多相关信息 [impress wiki 页面](https://github.com/impress/impress.js/wiki)。
* [Jimpress](http://jmpressjs.github.io/jmpress.js/): impress.js 的 jQuery 版本
* [Reveal.js](https://github.com/hakimel/reveal.js)
* [Beckpoke.js](https://github.com/bespokejs/bespoke)
* [CSSS](https://github.com/LeaVerou/CSSS)
* [Scrolldeck](https://github.com/johnpolacek/scrolldeck.js)
* [Deck.js](https://github.com/imakewebthings/deck.js)
* [Shower](https://github.com/shower/shower)
* [Flowtime.js](https://github.com/marcolago/flowtime.js)
* [Slides](https://github.com/briancavalier/slides)
* [remark](https://remarkjs.com)


### IPython/Jupyter 笔记本

> [IPython/Jupyter Notebook](https://jupyter.org/) 支持 Python、Julia、R、Scala 等语言，也可用于进行演示。
>
> 有关基于云的 Jupyter Notebook，请参阅[在线数学和编程](#math-and-programming-online)。


### 乳胶投影仪

* [Beamer](https://bitbucket.org/rivanvx/beamer/wiki/Home)：随标准 LaTeX 安装一起提供。发明了很多主题。一键开始编辑 [Overleaf](https://www.overleaf.com/)

### 数学

* [Mathematica 幻灯片](http://reference.wolfram.com/language/howto/CreateASlideShow.html) 可以进行交互。


### SVG 的力量

**在线 SVG 编辑器：**

* [ext-sozi](https://github.com/asyazwan/ext-sozi)

**本地 SVG 编辑器：**

* [Inkscape](https://inkscape.org)(`Mac`、`Win`、`Linux`)
* [GIMP](https://www.gimp.org)(`Mac`,`Win`,`Linux`)


### 分享幻灯片

* [GitHub 页面](https://pages.github.com/)：适用于基于 Html 的幻灯片。
* [Speaker Deck](https://speakerdeck.com/) by GitHub：PDF 幻灯片。可以在线显示或嵌入。


## 编程

### 代码编辑器


* [Visual Studio Code，又名 VS Code](https://code.visualstudio.com/)(`Free`、`Cross-platform`、`Plugins`)：与 Atom 相同的技术，但比 Atom 更快，微软制作。
* [Atom](https://atom.io/)(`免费`、`跨平台`、`插件`)：基于电子的编辑器，具有大量插件且易于修改。跨平台，通过 [sync-settings](https://atom.io/packages/sync-settings) 插件同步设置和插件。
* [Sublime Text](https://www.sublimetext.com/)(`免费评估`、`跨平台`、`插件`)：跨平台、快速、带插件。不是免费的，但可以永久免费使用。
* [JetBrains](https://www.jetbrains.com/)（“学生免费”、“跨平台”、“插件”）：漂亮的 IDE，集成了许多调试和编辑模式。
* [vim](https://github.com/vim/vim)(`免费`,`跨平台`,`插件`): 没有任何言语可以描述万能的vim。
* [Vundle](https://github.com/VundleVim/Vundle.vim): vim 插件管理器
* [来自 amix 的 vimrc](https://github.com/amix/vimrc): "终极 Vim 配置：vimrc"


### 软件

* [Synthical](https://synthical.com)：人工智能驱动的协作研究环境
* [Mathematica](http://www.wolfram.com/mathematica/)：一款统治一切的软件
* [iPython Notebook](http://ipython.org/notebook.html) (`Python`)：一个用于内联计算、制作图表和书写笔记的有用工具。
* [wakari.io](https://wakari.io/) 是一个主要用于数据分析的商业网站。
* [jiffylab](https://github.com/ptone/jiffylab) 是一个开源的，但做得不是很好。
* [supervised-ipython-nbserver](https://github.com/writefaruq/supervised-ipython-nbserver) 是使用 Django/Pinax 的笔记本的多用户版本。
* [Matlab](http://www.mathworks.com/products/matlab/)
* [Maple](https://www.maplesoft.com/index.aspx?L=E)
* [RStudio](https://www.rstudio.com/) (`R`)


### 科学计算

* [Python](https://www.python.org/)
* [scipy](https://www.scipy.org/)：科学计算变得简单
* [SnakeViz](https://jiffyclub.github.io/snakeviz/)：一个很好的Python调试和性能改进工具。
* [Julia](http://julialang.org/)
* [R](http://www.r-project.org/)
* [Rust](https://www.rust-lang.org/en-US/)
* [dna-claude-analysis](https://github.com/shmlkv/dna-claude-analysis)：个人基因组分析工具包，带有 Python 脚本，可分析 17 个类别的原始 DNA 数据，并生成用于科学研究的终端式 HTML 可视化。

### 编码很有趣

* [代码之战](https://codefights.com/)


## 学术


### 自我抄袭

> 这可能不是那么简单，但请记住这一点。重复使用自己的作品并不能保护您免受剽窃！阅读更多内容

* [维基百科：抄袭#自我抄袭](https://en.wikipedia.org/wiki/Plagiarism#自我抄袭)。

### 调查论文

* [Synthical](https://synthical.com)：人工智能驱动的协作研究环境。您可以使用它来根据阅读历史获取文章推荐、简化论文、找出热门文章、按含义（不仅仅是关键字）搜索文章、创建和共享文章文件夹、查看特定公司和大学的文章列表以及添加亮点。
* [Paperscape](http://paperscape.org/)：寻找有趣的论文。
* [Peerus](https://peer.us/)：监控特定主题或期刊中的新论文和相关论文。
* [SciRate](https://scirate.com/)：带有读者评分的 arXiv 前端。
* [ArXiv Sanity Preserver](http://arxiv-sanity.com/)：通过 Andrej Karpathy 专门针对许多机器学习的 arXiv 加速研究。
* [Iris.ai](https://the.iris.ai/)：探索科学论文以及它们如何与您选择的论文联系起来。
* [Publish or Perish](https://harzing.com/resources/publish-or-perish)：检索和分析学术引文，旨在使个别学者能够充分展示其研究影响力的案例。
* [PubChase](http://pubchase.com/)：生命科学和医学文献推荐引擎。
* [关联论文](https://www.connectedpapers.com/)：可视化关联论文，支持节点颜色、大小和距原点的距离，以区分论文是否有用以及相关性如何。
* [未引用](https://uncited.org)：跟上文献的步伐。
* [ODataMap](https://github.com/CherishChenCherish/odatamap) - 全球科学研究的互动地图。通过 AI 研究助手可视化 7 个知识大陆的 2.5 亿多篇论文。 [演示](https://odatamap.cherishchen2510.workers.dev)
* [citracer](https://github.com/marcpinet/citracer)：跟踪研究论文中任何概念的引用链。给定源 PDF（或 arXiv/DOI），递归遍历引文图并生成交互式 HTML 可视化。支持正向和反向跟踪。
* [BGPT MCP API](https://bgpt.pro/mcp/)：搜索具有结构化全文实验数据的科学论文（方法、结果、结论、样本量、局限性、质量分数 - 每篇论文 25 个以上领域）。通过模型上下文协议与 Claude、Cursor 和其他 AI 工具一起工作。免费套餐：50 次搜索，无需身份验证。 [存储库](https://github.com/connerlambden/bgpt-mcp)。 MCP 注册表：`io.github.connerlambden/bgpt-mcp`。

### 为自己获取任何可引用的代码

* [Zenodo](https://zenodo.org/)：通过在此处获取 DOI 代码，使 GitHub 上的任何内容都可引用。

### 为自己打造一个独特且持久的数字标识符

* [orcid](http://orcid.org/)：在任何研究工作流程中使用您的 ORCID 标识符，以确保您的工作获得认可。


### 将引用添加到您的代码中

* [duecredit](https://github.com/duecredit/duecredit)：允许您向编码书目详细信息的 Python 函数添加装饰器。

### 开放科学

* [开放科学框架](https://osf.io/)：一个具有大量集成的开放科学工具。

### 参考书目

* [ReadCube/Papers](https://www.readcube.com/)：一款用于参考管理、笔记等的全平台应用程序。以前的论文已重新命名为 ReadCube 论文。
* [Mendeley](https://www.mendeley.com/)：具有云存储和 BibTeX 支持的参考书目参考管理器。
* [Zotero](https://www.zotero.org/)：一个开源参考书目参考管理器，具有同步和 BibTeX 支持。
* [Zotero 样式库](https://www.zotero.org/styles)：找到您需要的任何样式。
* [JabRef](https://www.jabref.org/)：BibTeX 格式的开源参考书目参考管理器。
* [doi2bib](https://www.doi2bib.org/)：从 DOI 检索 BibTeX 条目。
* [crossref](https://www.crossref.org/)：使研究成果易于查找、引用、链接和评估。
* [CiteMe](https://citeme.app)：人工智能驱动的引文生成器，可搜索 11 多个学术数据库并以 43 多种风格格式化参考文献，包括 APA、哈佛大学、芝加哥、温哥华和 IEEE。
* [org-ref](https://github.com/jkitchin/org-ref)：Emacs 中 org-mode 的引用、交叉引用、索引、术语表和 bibtex 实用程序。
* [ScholarRef](https://github.com/brodie-neuro/ScholarRef)：直接在 Word `.docx` 文件内转换引文样式（APA 7、哈佛、温哥华）。

### 给研究人员的建议

* [PLoS One 的十项简单规则](http://collections.plos.org/ten-simple-rules)：一系列快速的“十项简单规则”文章，供研究科学家应对职业生涯中的挑战。文章数量是特定于生命科学的，但其余文章对于任何研究人员来说都足够通用。
* 查看[Awesome开源情报列表](https://github.com/jivoi/awesome-osint)的[学术资源和灰色文献列表](https://github.com/jivoi/awesome-osint#-academic-resources-and-grey-literature)供搜索引擎搜索论文。

## 安抚奶嘴

> **推荐使用[Rainy Mood](http://www.rainymood.com/)、[Coffitivity](https://coffitivity.com/) 和[Noisli](http://www.noisli.com/)。**

* [Rainy Mood](http://www.rainymood.com/)(`iOS`, `Android`, `Web`)：雨天雨天心情，简单但白噪音极佳；每天都有新的优美配乐
* [Coffitivity](http://coffitivity.com/)(`iOS`, `Android`, `Web`, `Mac`)：一个相当简单但有用的咖啡厅噪音库；高级版还有另外三首配乐；优雅的用户界面；科学研究动力
* [Brain.fm](https://www.brain.fm/)(`Web`)：通过音频脑波训练提高注意力、放松和睡眠。不是免费的，但值得每一分钱。
* [Noizio](http://noiz.io/)(`iOS`, `Mac`)：一个方便的白噪音工具，位于 Mac 状态栏中。
* [Noisli](http://www.noisli.com/)（`iOS`、`Android`、`Web`、`Chrome`）：自由混合多个曲目（与 Soundrown 类似，但具有更好的 UI）。用户可以保存自定义设置以供以后使用。我个人认为这个的火音轨比soundrown更好。
* [Soundrown](http://soundrown.com/)(`Web`)：多轨自由混音
* [Muji Sleep](http://sleep.muji.net/)(`iOS`, `Android`)
* [A Soft Murmur](http://asoftmurmur.com/)(`Web`)：多轨自由混音；简单的用户界面；提供定时器；可用蜿蜒
* [mynoise](https://mynoise.net/noiseMachines.php)(`iOS`, `Web`)：噪声发生器；很多选择（实际上太多了）；详细的均衡器
* [Rainy Cafe](http://rainycafe.com/)(`Web`)：没什么好说的，只是雨天心情和咖啡的结合
* [睡眠枕头](http://www.clearskyapps.com/portfolio/sleep)(`iOS`, `Mac`)：点击播放风格预加载场景；便于使用;美丽的设计
* [咖啡店的 YouTube 音轨（很长）](https://www.youtube.com/watch?v=KZV9FmHOsRg)
* [一段 10 小时降雨的 YouTube 音轨](https://www.youtube.com/watch?v=s_2FDRtFOAw)
* [TaoMix](https://play.google.com/store/apps/details?id=air.com.demute.TaoMix) (`Android`)：集中混音
* [Calm](http://www.calm.com/)(`iOS`, `Android`, `Web`): 帮助您平静下来
* [Raining](http://raining.fm)(`iOS`, `Android`, `Web`): 下雨和打雷
* [focus@will](https://www.focusatwill.com)(`iOS`、`Android`、`Web`)：促进大脑的音乐；现在付费服务


**其他一些相关的东西**

* [iSerenity](http://www.iserenity.com/)：有多种选择，但不太好（只是我的感觉）。
* [Rany by simple Noise](https://rain.simplynoise.com/)：只是下雨。
* [自然声音播放器](http://www.naturesoundplayer.com/)：许多自然声音，很酷。
* [NatureSoundsFor.Me](http://naturesoundsfor.me/)：制作自己的曲目，多种声音。
* [White.Noise](http://whitenoise247.net/): 几个不同的曲目
* [环境混音器](http://www.ambient-mixer.com/)：轻松制作环境声
* [白噪声mp3s](http://whitenoisemp3s.com/): 收听和下载



## 在线讨论

### 论坛和问答

> StackExchange.com 是进行专业讨论的好地方。这是一个例子。

* [Physics.StackExchange](http://physics.stackexchange.com/)
* [Biostars](https://www.biostars.org/)：StackOverflow 风格的生物信息学问答网站。
* [NeuroStars](https://neurostars.org/)：StackOverflow 风格的神经信息学问答网站。
* [SEQanswers](http://seqanswers.com/)：下一代测序社区论坛。


## 开源

> 开源很棒。使用 git。

### 开放许可证

> 一般来说，开放许可证是

* [开放定义](http://opendefinition.org/)：阅读[此处](http://opendefinition.org/licenses/) 的许可证并选择您喜欢的许可证。


### 使用许可证

> 要选择许可证，一个简单的方法是使用

* [选择许可证](http://choosealicense.com/) 可帮助您通过几个步骤决定使用哪个许可证。

> CC 许可证可以在 [知识共享](http://creativecommons.org/) 中找到。对于替代徽章或图标，请检查以下内容。

* [Guokr Badge](https://github.com/opentf/GuokrBadge)：绿色CC许可证徽章。 (**文档为中文。**)


## 数据可视化和图表制作

### 数据可视化

**JS 和 jQuery**

* [D3 js](http://d3js.org/) (`js`)
* [Highcharts](http://www.highcharts.com/demo/bar-stacked) (`js`)：折线图、面积图、柱形图和条形图、饼图、散点图和气泡图等。
* [Flot](http://www.flotcharts.org/flot/examples/) (`jQuery`)
* [拉斐尔](http://raphaeljs.com/) (`js`)
* [JavaScript InfoVis 工具包](http://philogb.github.io/jit/demos.html) (`js`)
* [Paper.js](http://paperjs.org/) (`js`)


**Python**

* [matplotlib](https://github.com/jbmouret/matplotlib_for_papers)
* [seaborn](https://seaborn.pydata.org/): 统计数据可视化
* [Plotnine](https://plotnine.readthedocs.io)：Python 图形语法
* [python 的 ggplot](http://ggplot.yhathq.com/)
* [plot.ly](https://plot.ly/ipython-notebooks/)：需要互联网，交互式绘图。
* [bokeh](http://bokeh.pydata.org/en/latest/docs/quickstart.html#quickstart)：需要互联网，交互式绘图。

* [itermplot](https://github.com/daleroberts/itermplot)：Matplotlib 的一个很棒的 iTerm2 后端，因此您可以直接在终端中绘图。


### 图表制作

> 专业图表应使用专业工具制作。

* [GeoGebra](http://www.geogebra.org/)(`Cloud`,`Mac`,`Win`,`Linux`,`Android`,`iOS`,`Win Store`): Geogebra 是一个非常酷的工具，可以制作 2D 和 3D 数学图。
* [LaTeXDraw](https://github.com/arnobl/latexdraw)(`Linux`)：“LaTeX 的矢量绘图编辑器。”
* [TikZ](http://www.texample.net/tikz/)(`LaTeX`)
* [BoxPlotR](http://shiny.chemgrid.org/boxplotr/)(`Web`)：用于生成箱线图的网络工具。
* [Graphviz](https://www.graphviz.org/)(`Linux,Win,Max,Solaris,FreeBSD`)：开源图形可视化软件。

> 为您的研究绘图选择准确度较高的颜色。为什么？ （[1]（https://github.com/holoviz/colorcet/blob/master/examples/index.ipynb），[2]（https://bids.github.io/colormap/））

* [colorcet](https://github.com/holoviz/colorcet) 可用于研究颜色图。

## 乳胶

> 比 Microsoft Word 好得多。

### 温馨提示

* [wikibooks - LaTeX](https://en.wikibooks.org/wiki/LaTeX)：一本很好的手册。
* [上面列出的笔记程序](#latex)


### 符号

* [Detexify](http://detexify.kirelabs.org/classify.html)：通过在线绘画找出符号是什么


### 绘图

* [TeX 示例](http://www.texample.net/) (Tikz/PGF)


### 字体

* [字体目录](http://www.tug.dk/FontCatalogue/seriffonts.html)

### 模板

* [乳胶模板](http://www.latextemplates.com/)



### 参考文献

**数学排版**

* [Math into Type](ftp://ftp.ams.org/pub/author-info/documentation/howto/mit-2.pdf)：这是一本关于数学相关排版的好书。这是版权材料。请不要重新分发。


## 管理信息中心


### 终端

* [在终端中绘制](https://github.com/glamp/bashplotlib)
* [asciinema](https://asciinema.org/): 命令行录制。
* [bashplot](https://github.com/glamp/bashplotlib)：在终端中绘图。
* [fuck](https://github.com/EricFreeman/fuck)：通过输入“fuck”来更正命令。

### 免费多媒体

* [CC Search](https://ccsearch.creativecommons.org/)：CC 许可下的图像搜索引擎。
* [Unsplash](https://unsplash.com/)：免费高分辨率图像。
* [Academicons](https://jpswalsh.github.io/academicons/)
* [Phylopic](http://phylopic.org/)



### 更多

* [二维码生成器](https://www.unitag.io/qrcode)：在海报中添加二维码可以帮助您吸引更多观众。
* [SHIELDS.io](http://shields.io/)：自己制作一个漂亮的徽章。
* [TitleCap](http://titlecapitalization.com/): 不确定标题中哪个单词要大写？ [TitleCap](http://titlecapitalization.com/) 适合您。
* [关于成为科学家](https://www.nap.edu/read/12192/)：负责任的研究行为指南。
* [DiRT Directory](http://dirtdirectory.org/)：供学术使用的数字研究工具的注册表。
* [在线白板](https://awwapp.com)：一个简单的在线白板，用户可以进行协作；适合在线会议。
* [MapInSeconds.com](http://www.mapinseconds.com/)：通过从电子表格复制粘贴来快速创建具有相应数据的地图。
* [Unpay Wall](http://unpaywall.org/)：合法免费下载研究论文。

-----

这是一个 CC BY-SA 许可项目。使用源码！保持源码开放！

![CC BY-SA](https://raw.githubusercontent.com/emptymalei/awesome-research/master/assets/cc_bysa.flat.guokr.png)
