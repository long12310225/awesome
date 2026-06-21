* **[SupportUkraineNow.org — “帮助乌克兰的真正方法”](https://supportukrainenow.org)**

----

### 举措

在我们[深入](#dive-into-machine-learning)之前，这里有一些您可能也会感兴趣的值得注意的项目和计划。

#### 与机器学习相关

* [AlgorithmWatch](https://algorithmwatch.org/en/) - [newsletter](https://algorithmwatch.org/en/newsletter/) — “一个非营利性研究和倡导组织，致力于观察、解压和分析自动决策 (ADM) 系统及其对社会的影响。”
* [`daviddao/awful-ai`](https://github.com/daviddao/awful-ai) - “可怕的人工智能是一个精心策划的列表，旨在跟踪当前人工智能的可怕用途——希望提高人们的认识”
* [`humanetech-community/awesome-humane-tech`](https://github.com/humanetech-community/awesome-humane-tech) - “推广改善福祉、自由和社会的解决方案”

#### 应对气候变化守则

* [`ProjectDrawdown/solutions`](https://github.com/ProjectDrawdown/solutions) - [Project Drawdown](https://www.drawdown.org/) — “随着 2017 年书籍的出版，Project Drawdown 进入了气候对话。通过 2020 年的《The Drawdown Review》，该项目继续其激发和交流解决方案的使命。” Python 和 Jupyter 笔记本。
* [`philsturgeon/awesome-earth`](https://github.com/philsturgeon/awesome-earth)
* [`daviddao/code-against-climate-change`](https://github.com/daviddao/code-against-climate-change)
* [`protontypes/open-sustainable-technology`](https://github.com/protontypes/open-sustainable-technology)

----

[![深入了解机器学习](./banner.png)](#dive-into-machine-learning)

# 深入研究机器学习

你好！如果出现以下情况，您可能会发现此资源很有帮助：

* 你了解Python或[你](https://github.com/alexmojaki/futurecoder) [学习](https://nbviewer.org/github/jakevdp/WhirlwindTourOfPython/blob/master/Index.ipynb) [它](https://github.com/vinta/awesome-python#resources) [:snake:](https://github.com/ossu/computer-science#introduction-to-programming)
* 您是[机器学习](https://en.wikipedia.org/wiki/Machine_learning)的新手
* 你关心[机器学习的道德规范](https://github.com/EthicalML/awesome-artificial-intelligence-guidelines)
* **[8 项负责任的机器学习原则](https://ethical.institute/principles.html)**
  * [开放的道德画布](https://openethics.ai/canvas/)
* 你通过实践来学习

对于一些不错的替代方案，[跳到最后](https://github.com/hangtwenty/dive-into-machine-learning#more-ways-to-dive-into-machine-learning)或[查看 Nam Vu 的指南，软件工程师的机器学习](https://github.com/ZuzooVn/machine-learning-for-software-engineers)。

当然，获得专业知识并不容易。另外，_我不是专家！_我只是想为您提供一些来自_专家的优质资源。机器学习的应用无处不在。我认为让更多的人更多地了解 ML，尤其是动手实践，符合公共利益，因为有很多不同的学习方式。

无论您投入机器学习的动机是什么，如果您了解一点 Python，现在您就可以在几分钟内上手机器学习“Hello World！”。

# 让我们开始吧

## 您需要的工具

### 如果您喜欢本地安装

* [Python](https://www.python.org/)。 Python 3 是最好的选择。
* [Jupyter 笔记本](https://jupyter.org/)。 （以前称为 IPython Notebook。）
* 一些科学计算包：
* 麻木
* 熊猫
* scikit学习
* matplotlib

您可以使用 [Anaconda Python 发行版](https://www.anaconda.com/download/) 只需单击几下即可安装 Python 3 和所有这些软件包。 Anaconda 在数据科学和机器学习社区中很受欢迎。 （使用适合您的工具。[如果您不确定或需要更多有关使用 conda/virtualenv/poetry/pipenv 的上下文，这里有一个非常有用的指南](https://web.archive.org/web/20211226071314/https://brainsteam.co.uk/2021/04/01/opinionated-guide-to-virtualenvs/)）

### 基于云的选项

您可以从浏览器使用一些选项：

- **[Binder](https://mybinder.org/) 是 Jupyter Notebook 的官方选择 [尝试 JupyterLab](https://jupyter.org/try)**
- [Deepnote](https://deepnote.com/) 允许实时协作
- [Google Colab](https://colab.research.google.com/) 提供“免费”GPU

对于其他选项，请参阅：

- [markusschanta/awesome-jupyter，“托管笔记本解决方案”](https://github.com/markusschanta/awesome-jupyter#hosted-notebook-solutions)
- [ml-tooling/best-of jupyter，“笔记本环境”](https://github.com/ml-tooling/best-of-jupyter)

## 我们走吧！

**[了解如何使用 Jupyter Notebook](http://opentechschool.github.io/python-data-intro/core/notebook.html)（5-10 分钟）。**（您可以[通过截屏视频学习](https://www.youtube.com/watch?v=qb7FT68tcA8)。）

现在，按照这个简短的练习进行操作：**[scikit-learn 机器学习简介](http://scikit-learn.org/stable/tutorial/basic/tutorial.html)**。在“ipython”或 Jupyter Notebook 中执行此操作，在笔记本中编码并执行代码。

[![I'll wait.](https://user-images.githubusercontent.com/2420688/29441281-00eff0c4-837f-11e7-9666-d653a1cd2372.jpeg)](http://scikit-learn.org/stable/tutorial/basic/tutorial.html)

### 刚刚发生了什么？

您刚刚使用 [scikit-learn](http://scikit-learn.org/stable/index.html) 对一些手写数字进行了分类。整洁吧？

# 潜入

## 机器学习的视觉介绍

让我们更多地了解机器学习以及一些常见的想法和担忧。阅读 [Stephanie Yee](https://twitter.com/stephaniejyee) 和 [Tony Chu](https://twitter.com/tonyhschu/) 的[“机器学习视觉简介，第 1 部分”](http://www.r2d3.us/visual-intro-to-machine-learning-part-1/)。

[![A Visual Introduction to Machine Learning, Part 1](https://user-images.githubusercontent.com/2420688/29441234-a2028c98-837e-11e7-88f2-1ca5a94684f6.gif)](http://www.r2d3.us/visual-intro-to-machine-learning-part-1/)

不会花很长时间的。这是一个美丽的介绍......尽量不要流太多口水！

## “关于机器学习的一些有用的知识”

好的。让我们深入探讨一下。

阅读 **[“关于机器学习的一些有用的知识”](http://homes.cs.washington.edu/~pedrod/papers/cacm12.pdf)** 作者：[Prof.佩德罗·多明戈斯](https://homes.cs.washington.edu/~pedrod/)。它充满了有价值的信息，但并非不透明。 （如果您还不完全理解，请不要担心。）花一些时间来理解这一点。

## 行话注释

* [数据分析、数据分析、数据挖掘、数据科学、机器学习和大数据之间有什么区别？](http://www.quora.com/What-is-the-difference-between-Data-Analytics-Data-Analysis-Data-Mining-Data-Science-Machine-Learning-and-Big-Data-1)
* 另一个方便的术语：[“数据工程”。](https://www.coursera.org/articles/what-does-a-data-engineer-do-and-how-do-i-become-one)
* [“MLOps”](https://ml-ops.org/) 与 Data Eng 重叠，并且[本指南后面有介绍性 MLOps 部分](#product-deployment-mlops)。

----

## 探索另一台笔记本

接下来，使用一个或多个笔记本进行编码。

- 笔记本系列：
- **2022：** [`rasbt/machine-learning-book`](https://github.com/rasbt/machine-learning-book) — 来自 [_Machine Learning with PyTorch and Scikit-Learn_ by Sebastian Raschka, Yuxi (Hayden) Liu, and Vahid Mirjalili](https://sebastianraschka.com/blog/2022/ml-pytorch-book.html) 的笔记本
- [博士。 Randal Olson 的示例机器学习笔记本](https://github.com/rhiever/Data-Analysis-and-Machine-Learning-Projects/blob/master/example-data-science-notebook/Example%20Machine%20Learning%20Notebook.ipynb)：“假设我们正在为一家初创公司工作，该公司刚刚获得资金来创建一款智能手机应用程序，该应用程序可以从智能手机拍摄的照片中自动识别花朵的种类。我们的数据科学主管要求我们创建一个演示机器学习模型，该模型对花朵进行四种测量（萼片长度、萼片宽度、花瓣长度和花瓣宽度），并仅根据这些测量值来识别物种。”
  - [在 Binder 中启动，无需安装步骤](https://mybinder.org/v2/gh/rhiever/Data-Analysis-and-Machine-Learning-Projects/master?filepath=example-data-science-notebook%2FExample%20Machine%20Learning%20Notebook.ipynb)
- 各种主题笔记本：
  - [trekhleb/machine-learning-experiments](https://github.com/trekhleb/machine-learning-experiments)
  - [trekhleb/homemade-machine-learning](https://github.com/trekhleb/homemade-machine-learning)

准备好后，查找更多精彩的 Jupyter Notebook：

* **[Jupyter 官方有趣的 Jupyter 笔记本图库：统计、机器学习和数据科学](https://github.com/jupyter/jupyter/wiki)** （[永久链接]（https://github.com/jupyter/jupyter/wiki/A-gallery-of-interesting-Jupyter-Notebooks/ae03c01ed25024aa06a4479ea600895d59b38bc4））

----

#让自己沉浸其中

选择以下课程之一并开始您的旅程。

## Andrew Ng 教授在 Coursera 上的_机器学习_

**[教授。 Andrew Ng 的](https://hai.stanford.edu/people/andrew-ng) [_机器学习_](https://www.coursera.org/learn/machine-learning) 是一门受欢迎且受人尊敬的免费在线课程。我见过[推荐](https://www.quora.com/How-do-I-learn-machine-learning-1/answer/Cory-Hicks-1)[经常](https://www.quora.com/How-do-I-learn-machine-learning-1/answer/Xavier-Amatriain)[并且强调。](https://www.forbes.com/sites/anthonykosner/2013/12/29/why-is-machine-learning-cs-229-the-most-popular-course-at-stanford/)**

建议购买一本教科书作为深入的参考。我最常看到推荐的两个是_[理解机器学习](https://web.archive.org/web/20210717194345/http://www.cs.huji.ac.il/~shais/UnderstandMachineLearning/copy.html)_
和_[统计学习的要素](https://web.stanford.edu/~hastie/Papers/ESLII.pdf)_。 【您只需使用两个选项之一作为您的主要参考；这里有一些上下文/比较，可以帮助您选择最适合您的一个。](https://github.com/hangtwenty/dive-into-machine-learning/issues/29)

### 公共数据集和宠物项目

你可能想兼职做一个自己喜欢的项目。当你准备好时，你
可以探索其中之一：[很棒的公共数据集](https://github.com/caesar0301/awesome-public-datasets)、[paperswithcode.com/datasets](https://paperswithcode.com/datasets)、[datasetlist.com](https://www.datasetlist.com/)、 [`KKulma/climate-change-data`](https://github.com/KKulma/climate-change-data#open-data)

### 本课程的提示

* [吴恩达教授课程的学习技巧，作者：Ray Li](https://rayli.net/blog/data/coursera-machine-learning-review/)
* 如果您想知道_这仍然是一门相关课程吗？_或者想弄清楚它是否适合您个人，请查看以下评论：
  * [评论：吴恩达的机器学习课程](https://towardsdatascience.com/review-andrew-ngs-machine-learning-course-b905aafdb7d9)
  * [Coursera 上的用户评论](https://www.coursera.org/learn/machine-learning/reviews)

### 在繁忙的日程中学习的提示

每周都能腾出时间是很困难的。因此，您可以尝试在可用的时间内更_有效地_学习。以下是一些方法：

* [Barbara Oakley 的《学习如何学习》](https://www.coursera.org/learn/learning-how-to-learn/)，Barbara Oakley 的《学习如何学习》，Coursera 上的免费视频课程。
* 喜欢书籍/有声读物？这些都是不错的选择：
* [Barbara Oakley 的书_A Mind for Numbers: How to Excel at Math and Science_](https://barbaraoakley.com/books/a-mind-for-numbers) ([评论](https://www.goodreads.com/book/show/18693655-a-mind-for-numbers)) — “我们都有能力在那些看似不自然的领域取得优异成绩第一”
* [_让它坚持：成功学习的科学_](https://www.retrievalpractice.org/make-it-stick) ([评论](https://www.goodreads.com/book/show/18770267-make-it-stick))

### 对我的建议持保留态度

我不是机器学习专家。我只是一名软件开发人员，这些资源/技巧对我很有用，因为我还学习了一些机器学习知识。

## 其他课程

* **作为 Jupyter Notebook 的数据科学课程：**
  * [实用数据科学](http://radimrehurek.com/data_science_python/)
  * [Python 数据科学手册，作为 Jupyter Notebooks](https://jakevdp.github.io/PythonDataScienceHandbook/)
* [`microsoft/Data-Science-For-Beginners`](https://github.com/microsoft/Data-Science-For-Beginners) - [2021 年添加](https://dev.to/azure/free-data-science-for-beginners-curriculum-on-github-1hme) — “10 周、20 节课的课程，全部都是关于数据科学的。每节课都包括课前和课后测验、完成课程的书面说明、解决方案和作业。我们基于项目的教学法让您可以边学习边构建，这是一种行之有效的新技能学习方法‘坚持’。”
* 另请参阅 [`microsoft/ML-For-Beginners`](https://github.com/microsoft/ML-For-Beginners)

<详情>
<summary>我见过的更多免费在线课程推荐。 （机器学习、数据科学和相关主题。）</summary>

* Coursera 的[数据科学专业](https://www.coursera.org/specializations/jhu-data-science)
* [教授。 Pedro Domingos 的介绍性视频系列](https://www.youtube.com/playlist?list=PLTPQEx-31JXgtDaC6-3HxWcp7fq4N8YGr)。 [教授。 Pedro Domingos](https://homes.cs.washington.edu/~pedrod/) 写了一篇论文 [“关于机器学习需要了解的一些有用的事情”](https://homes.cs.washington.edu/~pedrod/papers/cacm12.pdf)，您可能还记得指南前面的内容。
* [`ossu/data-science`](https://github.com/ossu/data-science) (另见 [`ossu/computer-science`](https://github.com/ossu/computer-science))
* [斯坦福 CS229：机器学习](https://github.com/afshinea/stanford-cs-229-machine-learning)
* [哈佛 CS109：数据科学](https://cs109.github.io/2015/)
* [高级统计计算（Vanderbilt BIOS8366）](http://stronginference.com/Bios8366/lectures.html)。交互的。
* Kevin Markham 的视频系列，[scikit-learn 机器学习简介](http://blog.kaggle.com/2015/04/08/new-video-series-introduction-to-machine-learning-with-scikit-learn/)，从我们已经介绍过的内容开始，然后在一个舒适的地方继续。
* [加州大学伯克利分校的 Data 8：数据科学基础](http://data8.org/) 课程和教科书 [计算和推理思维](https://www.inferentialthinking.com/) 教授数据科学中的关键概念。
* Mark A. Girolami 教授的[机器学习模块 (GitHub Mirror)。](https://github.com/josephmisiti/machine-learning-module)“适合具有强大数学背景的人。”
* [Quora 的一个史诗主题：我怎样才能成为一名数据科学家？](https://www.quora.com/How-can-I-become-a-data-scientist?redirected_qid=59455)
* [`ujjwalkarn/Machine-Learning-Tutorials`](https://github.com/ujjwalkarn/Machine-Learning-Tutorials)
* [本指南底部] 有更多替代方案链接（#more-ways-to-dive-into-machine-learning）

</详情>

## 获取帮助：问题、解答、聊天

从与您正在学习的课程相关的支持论坛和聊天开始。

查看 [datascience.stackexchange.com](https://datascience.stackexchange.com/) 和 [stats.stackexchange.com – 例如标签 _machine-learning_。](https://stats.stackexchange.com/questions/tagged/machine-learning) 还有一些 subreddits，例如 [/r/LearningMachineLearning](https://www.reddit.com/r/learningmachinelearning) 和[/r/MachineLearning](https://www.reddit.com/r/machinelearning)。

不要忘记聚会。还要在项目页面等上查找聊天邀请。

### 一些值得了解的社区！

* [/r/LearnMachineLearning](https://www.reddit.com/r/learnmachinelearning/)
* [/r/MachineLearning](https://reddit.com/r/MachineLearning)
* [/r/DataIsBeautiful](https://reddit.com/r/DataIsBeautiful)
* [/r/DataScience](https://reddit.com/r/DataScience)
* [交叉验证：stats.stackexchange.com](https://stats.stackexchange.com/)
* [`ossu/data-science` 有一个 Discord 服务器和新闻通讯](https://github.com/ossu/data-science#:~:text=Discord%20server)

## 补充：学好Pandas

<details><summary>您会想更加熟悉 Pandas。</summary>

* **必备**：[我希望早点知道 Pandas 中的东西](http://nbviewer.jupyter.org/github/rasbt/python_reference/blob/master/tutorials/things_in_pandas.ipynb)（作为 Jupyter Notebook）
* **必备**：[10 分钟到达 Pandas](http://pandas.pydata.org/pandas-docs/stable/10min.html)
* 另一个有用的教程：[使用 Python 和 Pandas 进行真实世界数据清理](https://trendct.org/2016/08/05/real-world-data-cleanup-with-python-and-pandas/)
* [来自 Data School 的关于 Pandas 的视频系列](https://www.youtube.com/playlist?list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y)。 “30 个常见 Pandas 任务的参考指南（外加 6 小时的支持视频）。”
* 以下是我在继续学习时发现特别有帮助的一些文档：
  * [Cookbook](http://pandas.pydata.org/pandas-docs/stable/cookbook.html)
* [数据结构](http://pandas.pydata.org/pandas-docs/stable/dsintro.html)，特别是。 [数据帧](http://pandas.pydata.org/pandas-docs/stable/dsintro.html#dataframe) 部分
  * [通过旋转 DataFrame 进行重塑](https://pandas.pydata.org/pandas-docs/stable/user_guide/reshaping.html)
* [计算工具](http://pandas.pydata.org/pandas-docs/stable/computation.html) 和 [StackExchange 线程：“普通语言中的协方差是什么？”](https://stats.stackexchange.com/questions/29713/what-is-covariance-in-plain-language)
  * [Group By（分割、应用和组合数据帧）](http://pandas.pydata.org/pandas-docs/stable/groupby.html)
  * [可视化您的数据框](https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html)
* 用于缩放“pandas”和替代方案的书签
* [`dask`](https://dask.org/)：类似于 Pandas 的接口，但适用于大于内存的数据和“底层”并行性。
* [`vaex`](https://vaex.io)：“用于 Python、ML 的核外混合 Apache Arrow/NumPy DataFrame，以每秒 10 亿行的速度可视化和探索大型表格数据”
</详情>

## 补充：故障排除

这些调试工具可以在 Jupyter Notebook 内部（或外部）使用：

* [`birdseye`](https://birdseye.readthedocs.io/en/latest/integrations.html#jupyter-ipython-notebooks),
[`snoop`](https://github.com/alexmojaki/snoop)
* [`pandas-log`](https://github.com/eyaltrabelsi/pandas-log.git)

还有更多的工具，但这些可能会帮助您入门，或者可能是
在学习时特别有用。除了学习之外，故障排除不仅仅是
当然，日志或调试器...[本指南后面还有一些 MLOps 链接](#product-deployment-mlops)。

# 各种技巧和资源

### 风险——一些出发点

“机器学习系统自动从数据中学习程序。” Pedro Domingos，在[“关于机器学习的一些有用的事情”](http://homes.cs.washington.edu/~pedrod/papers/cacm12.pdf) 您生成的程序将需要维护。与任何更快地创建程序的方法一样，您可能会积累[技术债务](https://en.wikipedia.org/wiki/Technical_debt)。

以下是[机器学习：技术债务的高息信用卡](https://research.google/pubs/pub43146/)的摘要：

> 机器学习提供了一个非常强大的工具包，用于快速构建复杂的系统。本文认为，认为这些快速胜利是免费的是危险的。使用技术债务框架，我们注意到，在应用机器学习时，很容易在系统级别产生大量持续维护成本。本文的目标是强调几个机器学习特定的风险因素和尽可能避免或重构的设计模式。其中包括边界侵蚀、纠缠、隐藏的反馈循环、未声明的消费者、数据依赖性、外部世界的变化以及各种系统级反模式。

如果您正在阅读本指南，您应该阅读该论文。您还可以[收听采访本文作者之一的播客节目](https://softwareengineeringdaily.com/2015/11/17/machine-learning-and-technical-debt-with-d-sculley/)。

* **[Awesome Production Machine Learning](https://github.com/EthicalML/awesome-Production-machine-learning)，“用于部署、监控、版本化和扩展机器学习的优秀开源库的精选列表。”** 顺便说一下，它包括关于[隐私保护 ML](https://github.com/EthicalML/awesome-Production-machine-learning#privacy-preserving-machine-learning) 的部分！
* **[“机器学习规则：[可靠] ML 工程的最佳实践”](http://martin.zinkevich.org/rules_of_ml/rules_of_ml.pdf)** 作者：Martin Zinkevich，关于 ML 工程实践。
* [维护机器学习系统的高昂成本](http://www.kdnuggets.com/2015/01/high-cost-machine-learning-technical-debt.html)
* [过拟合与欠拟合：概念解释](https://towardsdatascience.com/overfitting-vs-underfitting-a-conceptual-explanation-d94ee20ca7f9)
* [11 种巧妙的过度拟合方法以及如何避免它们](http://hunch.net/?p=22)
* [“那么，你想建立一个道德算法吗？”促进讨论的交互式工具](https://cdt.info/ddtool/) [(source)](https://github.com/numfocus/algorithm-ethics)

当然，这不是一个完整的列表！它们只是一些门户和起点。 _知道一些其他资源吗？请分享它们，欢迎拉取请求！_

### 同行评审

**[OpenReview.net](https://openreview.net/about)**“旨在促进科学交流的开放性，特别是同行评审过程。”

<详情>
<summary><em>有关 OpenReview.net 的更多信息</em></summary>

> * **开放同行评审：** 我们提供了一个可配置的同行评审平台，概括了许多微妙的开放性等级，允许会议组织者、期刊和其他“评审实体”配置他们选择的具体政策。我们打算充当不同政策的试验台，帮助科学界试验开放学术，同时解决有关保密性、归属和偏见的合理担忧。
> * **开放出版：** 跟踪提交内容，协调编辑、审稿人和作者的工作，并托管……为了速度和可靠性而进行分片和分发。
> * **开放获取：** 所有人免费获取论文，免费提交论文。不收取任何费用。
> * **公开讨论：** 托管已接受的论文及其评论和意见。与论文接受后相关的持续讨论论坛。出版场所主席/编辑可以控制评论/评论表格的结构、读/写访问及其时间安排。
> * **开放目录：** 具有利益冲突信息的人员集合，包括机构和关系，例如共同作者、共同 PI、同事、顾问/受顾问和家庭关系。
> * **开放推荐：** 科学主题和专业知识的模型。人员名录包括科学专业知识。为有数千份提交的会议提供审稿人-论文匹配，结合专业知识、投标、限制和各种审稿人平衡。向用户推荐论文。
> * **开放 API：** 我们提供一个简单的 REST API [...]
> * **开源：** 我们致力于开源。 OpenReview 的许多部分已经在 [GitHub 上的 OpenReview 组织](https://github.com/openreview) 中。一些进一步的版本正在等待对代码库的专业安全审查。

> * [OpenReview.net](https://openreview.net/) 由马萨诸塞大学阿默斯特分校信息与计算机科学学院 Andrew McCallum 的信息提取和综合实验室创建
>
> * [OpenReview.net](https://openreview.net/) 是在 [ICML 2013 同行评审研讨会](https://openreview.net/group?id=ICML.cc/2013/PeerReview) 上发表的论文 [开放奖学金和同行评审：实验时间](https://openreview.net/forum?id=xf0zSBd2iufMg) 中描述的早期版本构建的。
>
> * OpenReview 是一个长期项目，旨在通过改进同行评审来推进科学发展，并通过《科学与社会准则》获得合法的非营利地位。我们衷心感谢[OpenReview 赞助商](https://openreview.net/sponsors) 的广泛支持——科学同行评审是神圣不可侵犯的，不应该由任何一个赞助商拥有。

</详情>

### 生产、部署、MLOps

如果您正在学习 MLOps 但发现它令人不知所措，这些资源可能会帮助您了解方向：

* [MLOps 堆栈模板](https://valohai.com/blog/the-mlops-stack/)，作者：Henrik Skogström
* [来自 Netflix、DoorDash、Spotify 等的 ML 平台课程](https://towardsdatascience.com/lessons-on-ml-platforms-from-netflix-doordash-spotify-and-more-f455400115c7)，作者：Ernest Chan，《迈向数据科学》
* [MLOps 堆栈画布](https://ml-ops.org/content/mlops-stack-canvas) 位于 [ml-ops.org](https://ml-ops.org/)

推荐保存/加注星标/观看的精彩列表：

* **[EthicalML/awesome-artificial-intelligence-guidelines](https://github.com/EthicalML/awesome-artificial-intelligence-guidelines)**
* **[EthicalML/awesome-product-machine-learning](https://github.com/EthicalML/awesome-product-machine-learning#privacy-preserving-machine-learning)**
* **[visenger/awesome-ml-model-governance](https://github.com/visenger/Awesome-ML-Model-Governance)**
* **[visenger/awesome-MLOps](https://github.com/visenger/awesome-mlops)**
* **[eugeneyan/applied-ml](https://github.com/eugeneyan/applied-ml)**

### 更轻松地共享深度学习模型和演示

* 🐣 **[Replicate](https://replicate.com)“可以轻松共享正在运行的机器学习模型”**
* 通过浏览器轻松尝试深度学习模型
* 如果您想深入研究并了解某些内容是如何工作的，则演示链接到 GitHub 上的论文/代码
* 模型在由 **[`cog`](https://github.com/replicate/cog),**“机器学习容器”构建的容器中运行。
* 它是一个开源工具，用于将模型放入可复制的 Docker 容器中。
* 您可以仅使用 Python 和 YAML 将模型放入容器中。
* 有一个用于 Replicate 的 API 可以为您运行预测

----

## 深度学习

请注意：一些专家警告我们不要太过超前，并鼓励我们在进入深度学习之前学习机器学习基础知识。这是对本指南中一些相关课程的释义——例如，Andrew Ng 教授鼓励在学习 DL 之前先打好 ML 基础。也许您现在已经准备好了，或者您可能想尽快开始并在学习其他 ML 的同时学习一些 DL。

当您准备好深入学习深度学习时，这里有一些有用的资源。

* **[_深入深度学习_](https://d2l.ai/) - 一本关于深度学习的互动书**（[在 GitHub 上查看](https://github.com/d2l-ai/d2l-en)）
* 快速入门：
    * [使用 Jupyter Notebooks 在本地运行本书](https://d2l.ai/chapter_installation/index.html)
    * [使用 Google Colab 在浏览器中运行本书](https://d2l.ai/chapter_appendix-tools-for-deep-learning/colab.html)
*“整本书都是在 Jupyter 笔记本中起草的，将说明图、数学和交互式示例与独立代码无缝集成。”
*“您可以修改代码并调整超参数以获得即时反馈，从而积累深度学习的实践经验。”

<details><summary>更多深度学习链接</summary>

* **[教授。 Andrew Ng 的](https://scholar.google.com/itations?user=mG4imMEAAAAJ&hl=en) [深度学习课程](https://www.coursera.org/specializations/deep-learning)！** 有五门课程，作为 [Coursera 深度学习专业化](https://www.coursera.org/specializations/deep-learning) 的一部分。这些课程是他的新企业 [deeplearning.ai](https://www.deeplearning.ai) 的一部分
* 一些关于它的课程笔记：[ashishpatel26/Andrew-NG-Notes](https://github.com/ashishpatel26/Andrew-NG-Notes)
* **[_深度学习_](https://www.deeplearningbook.org/)，麻省理工学院出版社出版的免费书籍。** 作者：Ian Goodfellow、Yoshua Bengio 和 Aaron Courville。
* 一个值得注意的推荐在这里：[“作为一名工程师，获得深度学习技能的最佳方法是什么？”](https://www.quora.com/What-are-the-best-ways-to-pick-up-Deep-Learning-skills-as-an-engineer)
* [`fastai/fastbook`](https://github.com/fastai/fastbook)，作者：Jeremy Howard 和 Sylvain Gugger —“深度学习、fastai 和 PyTorch 简介。”
* [`explosion/thinc`](https://github.com/explosion/thinc) 是一个有趣的库，它包装了 **PyTorch**、**TensorFlow** 和 **MXNet** 模型。
*“模型定义的简洁函数式编程方法，使用组合而不是继承。”
*“用于描述对象树和超参数的集成配置系统。”
* [paperswithcode.com](https://paperswithcode.com/) - “论文与代码的使命是创建一个包含机器学习论文、代码、数据集、方法和评估表的免费开放资源。”
* [`labmlai/annotated_deep_learning_paper_implementations`](https://github.com/labmlai/annotated_deep_learning_paper_implementations) - “带有并排注释的深度学习论文的实现/教程。”其中 50 多个！确实有很好的注释和解释。
* [Distill.pub](https://distill.pub/about/) 发布了可探索的解释，绝对值得探索和关注！

</详情>

----

## 与领域专家合作

机器学习可以很强大，但它并不是魔法。

每当您应用机器学习来解决问题时，您都会在某个特定的问题领域中工作。为了获得好的结果，您或您的团队将需要“实质性专业知识”/“领域知识”。为自己学习你能学到的东西......但你也应该**与专家合作。**如果与[主题专家和领域专家](https://en.wikipedia.org/wiki/Subject-matter_expert#Domain_expert_(software))合作，你会得到更好的结果。

### 机器学习和用户体验 (UX)

我不能说得更好：

> **机器学习不会弄清楚要解决什么问题。** 如果你不符合人类的需求，你只会构建一个非常强大的系统来解决一个非常小的（或者可能不存在的）问题。

这句话来自[乔什·洛夫乔伊的《人工智能的用户体验》](https://design.google/library/ux-ai/)。换句话说，**[你不是用户](https://www.nngroup.com/articles/false-consensus/)。**建议阅读：[Martin Zinkevich 的“ML 工程规则”，规则 #23：“你不是典型的最终用户”](https://developers.google.com/machine-learning/guides/rules-of-ml/# human_analysis_of_the_system)

## 技能提升

有哪些方法可以练习？

<详情>
<summary><strong>一种方法：</strong>竞争和挑战</summary>

你需要**练习。** [在Hacker News上，用户olympus评论说你可以通过比赛来练习和评估自己](https://news.ycombinator.com/item?id=10508565)。 [Kaggle](https://www.kaggle.com/competitions) 和 [ChaLearn](http://www.chalearn.org/) 是机器学习竞赛的中心。 （您可以在[此处](https://github.com/paperswithcode/releasing-research-code#results-leaderboards)或[此处](https://towardsdatascience.com/12-data-science-ai-competitions-to-advance-your-skills-in-2021-32e3fcb95d8c)找到更多竞赛。）

您还需要 **理解。** 您应该查看 Kaggle 竞赛获奖者对他们的解决方案的评价，[例如，“No Free Hunch”博客](http://blog.kaggle.com/)。一开始这些可能会让你难以理解，但一旦你开始理解并欣赏这些，你就会知道你已经有所收获。

比赛和挑战只是练习的一种方式！ [机器学习不仅仅是 Kaggle 竞赛](https://jvns.ca/blog/2014/06/19/machine-learning-isnt-kaggle-competitions)。

</详情>

<详情>
<summary><strong>另一种方法：</strong>尝试做一些实践研究</summary>

这是一种补充性的练习方法：**进行实践研究。**

1. **问一个问题。开始探索一些数据。** [“数据科学中最重要的事情就是问题”](https://github.com/DataScienceSpecialization/courses/blob/master/01_DataScientistToolbox/03_02_whatIsData/index.Rmd#the-data-is-the-second-most-important-thing) ([Jeff T. Leek 博士](https://github.com/jtleek))。那么从一个问题开始吧。然后，找到[真实数据](https://github.com/caesar0301/awesome-public-datasets)。分析一下吧然后...
2. **传达结果。** 当您认为自己有新颖的发现时，请请求审查。当您仍在学习时，请在非正式社区中提问（有些[链接如下](#some-communities-to-know-about)）。
3. **从反馈中学习。** 考虑[公开学习](https://www.swyx.io/learn-in-public/)，它对某些人来说非常有效。 （不过，不要给自己施加压力！每个人都是不同的，了解自己的学习风格是件好事。）

怎样才能提出有趣的问题呢？这是一种方法。每周选择一天[查找公共数据集](https://github.com/caesar0301/awesome-public-datasets)并写下想到的一些问题。另外，请订阅 [Data is Plural](https://tinyletter.com/data-is-plural)，这是一份有趣的数据集的新闻通讯。当某个问题激发您的灵感时，尝试用您正在学习的技能来探索它。

这个进行实践研究并从回顾中学习的建议是基于与 [Dr.兰德尔·奥尔森](http://www.randalolson.com/)。以下是奥尔森的更多建议，[经许可引用：](https://github.com/hangtwenty/dive-into-machine-learning/issues/11#issuecomment-154135498)

> 我认为最好的建议是告诉人们始终清楚地展示他们的方法并避免过度解释他们的结果。成为专家的一部分就是知道很少有明确的答案，尤其是当您处理真实数据时。

当你重复这个过程时，你的实践研究将变得更加科学、有趣和集中。另外，[这里有一个关于数据科学中的科学方法的视频。](https://101.datascience.community/2012/06/27/the-data-scientific-method/))

</详情>

<详情>
<summary>更多机器学习职业相关链接</summary>

* [“关于建立机器学习职业和阅读吴恩达教授的研究论文的建议”](https://www.kdnuggets.com/2019/09/advice-building-machine-learning-career-research-papers-andrew-ng.html)
* 一些查找/关注有趣论文/代码的链接：
* [Papers With Code](https://paperswithcode.com/) 是一个值得关注的热门网站，它可以引导您找到其他资源。 [github.com/paperswithcode](https://github.com/paperswithcode)
  * [MIT: Papers + Code](https://mitibmwatsonailab.mit.edu/research/papers-code/) - “同行评审是科学验证的命脉，也是防止人工智能炒作失控的护栏。我们对在顶级场所发表论文的承诺反映了我们对真实、可重复和真正创新的基础。”
* [papers.labml.ai/papers/weekly](https://papers.labml.ai/papers/weekly), [每月](https://papers.labml.ai/papers/monthly/)
* 欢迎拉取请求！

</详情>

---

## 更多数据科学材料

以下是一些额外的数据科学资源：

* **[Python 数据科学手册，作为 Jupyter Notebooks](https://jakevdp.github.io/PythonDataScienceHandbook/)**
* [`r0f1/datascience`](https://github.com/r0f1/datascience) - “使用 Python 练习数据科学的精选资源列表，不仅包括库，还包括教程、代码片段、博客文章和讲座的链接。”

### 旁白：贝叶斯统计和机器学习

来自[Metacademy 上的“贝叶斯机器学习”概述](https://metacademy.org/roadmaps/rgrosse/bayesian_machine_learning)：

> ...贝叶斯思想在过去 20 年左右的时间里对机器学习产生了巨大影响，因为它们在构建现实世界现象的结构化模型方面提供了灵活性。算法的进步和计算资源的增加使得适应以前被认为难以处理的丰富的、高度结构化的模型成为可能。

<详情>
<summary>这里有一些学习贝叶斯方法的很棒的资源。</summary>

* **免费书籍** _[黑客的概率编程和贝叶斯方法](http://camdavidsonpilon.github.io/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers/)_。以“计算/理解第一，数学第二的观点”制作。使用 [PyMC](https://github.com/pymc-devs/pymc)。它也有印刷版！
* 喜欢边玩边学？我也是。尝试[19个问题](https://github.com/fulldecent/19-questions)，“一个机器学习游戏，它会问你问题并猜测你正在思考的物体”，并**解释它使用的是哪种贝叶斯统计技术！**
* [_Michael Grogan 使用贝叶斯建模进行时间序列预测_](https://www.manning.com/liveprojectseries/time-series-forecasting-with-bayesian-modeling)，一个包含 5 个项目的系列 - 付费，但第一个项目是免费的。
* [Python 中的贝叶斯建模](https://github.com/markdregan/Bayesian-Modelling-in-Python)。也使用 [PyMC](https://github.com/pymc-devs/pymc)。

</详情>

[(↑ 返回顶部)](#dive-into-machine-learning)

----

## “深入机器学习”的更多方法

以下是学习机器学习的一些其他指南。

* [软件工程师的机器学习，作者：Nam Vu](https://github.com/ZuzooVn/machine-learning-for-software-engineers)。用他们的话说，这是一种“为软件工程师设计的自上而下、结果优先的方法”。一定要添加书签并使用它。它可以回答许多问题并为您提供丰富的资源。
* [`ujjwalkarn/Machine-Learning-Tutorials`](https://github.com/ujjwalkarn/Machine-Learning-Tutorials)
* [`josephmisiti/awesome-machine-learning`](https://github.com/josephmisiti/awesome-machine-learning)
* 云供应商提供的课程。这些通常是高质量的内容，但会严重引导您使用特定于供应商的工具/服务。为了避免陷入供应商的具体情况，您可以确保您也从其他资源中学习。
* [`microsoft/ML-For-Beginners`](https://github.com/microsoft/ML-For-Beginners), [`microsoft/Data-Science-For-Beginners`](https://github.com/microsoft/Data-Science-For-Beginners)
* [Google 机器学习速成课程](https://developers.google.com/machine-learning/crash-course/)（[更多选项](https://cloud.google.com/training/machinelearning-ai)）
* [Amazon AWS](https://aws.amazon.com/machine-learning/mlu/)（[更多选项](https://aws.amazon.com/machine-learning/learn/)）
* **2022：** [_使用 PyTorch 和 Scikit-Learn 进行机器学习_ 作者：Sebastian Raschka、Yuxi (Hayden) Liu 和 Vahid Mirjalili](https://github.com/rasbt/machine-learning-book)

[(↑ 返回顶部)](#dive-into-machine-learning)
