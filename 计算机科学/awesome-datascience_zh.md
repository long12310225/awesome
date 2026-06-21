<divalign="center"><img src="./assets/head.jpg"></div>

# 出色的数据科学

[![Awesome](https://cdn.jsdelivr.net/gh/sindresorhus/awesome@d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome) 

欢迎贡献 - 请参阅 [`CONTRIBUTING.md`](CONTRIBUTING.md)。

**一个开源数据科学存储库，用于学习和应用概念来解决现实世界的问题。**

这是开始学习**数据科学**的捷径。只需按照步骤回答“什么是数据科学，我应该学习什么来学习数据科学？”的问题。

<br>

## $ 学术

```
$ brew tap academic/tap
$ brew install academic
```

## 赞助商

成为第一个赞助者！ `github@academic.io`



## 目录

- [什么是数据科学？](#what-is-data-science)
- [我从哪里开始？](#where-do-i-start)
- [Agents](#agents)
- [培训资源](#training-resources)
  - [Tutorials](#tutorials)
  - [免费课程](#free-courses)
  - [大规模开放在线课程](#moocs)
  - [强化课程](#intensive-programs)
  - [Colleges](#colleges)
- [数据科学工具箱](#the-data-science-toolbox)

  - [Algorithms](#algorithms)
    - [监督学习](#supervised-learning)
    - [无监督学习](#unsupervised-learning)
    - [半监督学习](#semi-supervised-learning)
    - [强化学习](#reinforcement-learning)
    - [数据挖掘算法](#data-mining-algorithms)
    - [深度学习架构](#deep-learning-architectures)
  - [通用机器学习包](#general-machine-learning-packages)
  - [模型评估与监控](#model-evaluation--monitoring)
    - [显然是人工智能](#evidently-ai)
  - [深度学习包](#deep-learning-packages)
    - [PyTorch 生态系统](#pytorch-ecosystem)
    - [TensorFlow 生态系统](#tensorflow-ecosystem)
    - [Keras 生态系统](#keras-ecosystem)
  - [可视化工具](#visualization-tools)
  - [杂项工具](#miscellaneous-tools)
- [文学与媒体](#literature-and-media)
  - [Books](#books)
    - [图书优惠（附属）](#book-deals-affiliated)
  - [期刊、出版物和杂志](#journals-publications-and-magazines)
  - [Newsletters](#newsletters)
  - [Bloggers](#bloggers)
  - [Presentations](#presentations)
  - [Podcasts](#podcasts)
  - [YouTube 视频和频道](#youtube-videos--channels)
- [Socialize](#socialize)
  - [脸书帐户](#facebook-accounts)
  - [推特账户](#twitter-accounts)
  - [电报频道](#telegram-channels)
  - [松弛社区](#slack-communities)
  - [GitHub 群组](#github-groups)
  - [数据科学竞赛](#data-science-competitions)
- [Fun](#fun)
  - [Infographics](#infographics)
  - [Datasets](#datasets)
  - [Comics](#comics)
- [其他很棒的清单](#other-awesome-lists)
  - [Hobby](#hobby)

## 什么是数据科学？
**[`^ 回到顶部 ^`](#awesome-data-science)**

数据科学是当今计算机和互联网领域最热门的话题之一。直到今天，人们已经从应用程序和系统中收集了数据，现在是分析它们的时候了。接下来的步骤是根据数据提出建议并创建对未来的预测。 [在这里](https://www.quora.com/Data-Science/What-is-data-science)您可以找到**数据科学**的最大问题以及专家的数百个答案。


|链接 |预览 |
| --- | --- |
| [数据科学初学者](https://github.com/microsoft/Data-Science-For-Beginners) | Microsoft 很高兴提供为期 10 周、20 课时的数据科学课程。 |
| [什么是数据科学@O'reilly](https://www.oreilly.com/ideas/what-is-data-science) | _数据科学家将创业精神与耐心、逐步构建数据产品的意愿、探索能力以及迭代解决方案的能力结合起来。它们本质上是跨学科的。他们可以解决问题的各个方面，从最初的数据收集和数据调节到得出结论。他们可以跳出框框思考，想出新的方法来看待问题，或者解决非常广泛定义的问题：“这里有很多数据，你能从中得到什么？”_ |
| [什么是数据科学@Quora](https://www.quora.com/Data-Science/What-is-data-science) |数据科学是结合数据技术、算法开发、数据干扰等多个方面来研究数据、分析数据并找到困难问题的创新解决方案。基本上，数据科学就是通过寻找创造性的方法来分析数据并推动业务增长。 |
| 【21世纪最性感的工作】(https://hbr.org/2012/10/data-scientist-the-sexiest-job-of-the-21st- century) | _今天的数据科学家类似于 20 世纪 80 年代和 90 年代的华尔街“宽客”。那时，具有物理和数学背景的人们涌入投资银行和对冲基金，在那里他们可以设计全新的算法和数据策略。随后，多所大学开设了金融工程硕士课程，培养了主流公司更容易接触到的第二代人才。这种模式在 20 世纪 90 年代后期在搜索工程师中得到了重复，他们的精湛技能很快就在计算机科学课程中得到教授。
| [维基百科](https://en.wikipedia.org/wiki/Data_science) | _数据科学是一个跨学科领域，它使用科学方法、流程、算法和系统从许多结构化和非结构化数据中提取知识和见解。数据科学与数据挖掘、机器学习和大数据有关。_ |
| 【如何成为数据科学家】(https://www.mastersindatascience.org/careers/data-scientist/) | _数据科学家是大数据管理员，收集和分析大量结构化和非结构化数据。数据科学家的角色结合了计算机科学、统计学和数学。他们对数据进行分析、处理和建模，然后解释结果，为公司和其他组织制定可行的计划。
| [#datascience 的简短历史](https://www.forbes.com/sites/gilpress/2013/05/28/a-very-short-history-of-data-science/) | _数据科学家如何变得性感的故事主要是成熟的统计学学科与非常年轻的学科（计算机科学）结合的故事。  “数据科学”一词最近才出现，专门指代一种有望理解海量大数据的新职业。但理解数据有着悠久的历史，科学家、统计学家、图书馆员、计算机科学家和其他人多年来一直在讨论这一问题。以下时间线追溯了“数据科学”一词的演变及其使用，尝试定义它以及相关术语。_ |
|[数据科学家的软件开发资源](https://www.rstudio.com/blog/software-development-resources-for-data-scientists/)|_数据科学家专注于通过探索性分析、统计和模型来理解数据。软件开发人员使用不同的工具应用一组单独的知识。尽管他们的重点似乎无关，但数据科学团队可以从采用软件开发最佳实践中受益。版本控制、自动化测试和其他开发技能有助于创建可重复的、可用于生产的代码和工具。_|
|[数据科学家路线图](https://www.scaler.com/blog/how-to-become-a-data-scientist/)|_在当今数据驱动的世界中，每天生成约 3.2877 亿 TB 的数据，数据科学是一个绝佳的职业选择。而且这个数字还在日益增加，这反过来又增加了对能够利用这些数据来推动业务增长的熟练数据科学家的需求。_|
|[探索成为数据科学家的道路](https://www.appliedaicourse.com/blog/how-to-become-a-data-scientist/)|_数据科学是当今最受欢迎的职业之一。随着企业越来越依赖数据来做出决策，对熟练数据科学家的需求迅速增长。无论是科技公司、医疗保健组织，甚至是政府机构，数据科学家在将原始数据转化为有价值的见解方面都发挥着至关重要的作用。但是，如何成为一名数据科学家，尤其是如果您刚刚起步呢？ _|

## 我从哪里开始？
**[`^ 回到顶部 ^`](#awesome-data-science)**

虽然不是绝对必要的，但拥有一门编程语言是成为一名有效的数据科学家的一项关键技能。目前，最流行的语言是_Python_，紧随其后的是_R_。 Python 是一种通用脚本语言，可应用于各个领域。 R 是一种用于统计的领域特定语言，其中包含许多开箱即用的常用统计工具。

[Python](https://python.org/) 是迄今为止科学界最流行的语言，这在很大程度上归功于它的易用性以及用户生成的包的充满活力的生态系统。要安装包，有两种主要方法：Pip（称为“pip install”），与 Python 捆绑在一起的包管理器；以及 [Anaconda](https://www.anaconda.com)（称为“conda install”），这是一个功能强大的包管理器，可以安装 Python、R 的包，并可以下载 Git 等可执行文件。

与 R 不同，Python 并不是从头开始构建时就考虑到了数据科学，但有大量第三方库可以弥补这一点。在本文档后面可以找到更详尽的包列表，但这四个包是开始数据科学之旅的一组不错的选择： [Scikit-Learn](https://scikit-learn.org/stable/index.html) 是一个通用数据科学包，它实现了最流行的算法 - 它还包括丰富的文档、教程和它实现的模型的示例。即使您更喜欢编写自己的实现，Scikit-Learn 也是您会发现的许多常见算法背后的具体细节的宝贵参考。使用 [Pandas](https://pandas.pydata.org/)，人们可以收集数据并将其分析为一种方便的表格格式。 [Numpy](https://numpy.org/) 为数学运算提供非常快速的工具，重点是向量和矩阵。 [Seaborn](https://seaborn.pydata.org/) 本身基于 [Matplotlib](https://matplotlib.org/) 包，是一种生成漂亮的数据可视化效果的快速方法，提供了许多开箱即用的良好默认值，以及一个展示如何生成许多常见数据可视化效果的图库。

当踏上成为数据科学家的旅程时，语言的选择并不是特别重要，Python 和 R 都有各自的优点和缺点。选择您喜欢的语言，然后查看我们下面列出的[免费课程](#free-courses) 之一！

### 初学者路线图
如果您刚刚开始，这里有一个简单的推荐路径：

1. **学习Python** – 从基础开始：变量、循环、函数
2. **学习核心库** – Pandas、NumPy、Matplotlib、Scikit-Learn
3. **练习初学者项目** – 在 Kaggle 上尝试泰坦尼克号生存或房价预测
4. **学习数学基础知识** – 统计学、线性代数、概率
5. **进入机器学习** – 监督学习 → 无监督 → 深度学习

## 代理商

本节包含对数据科学工作流程有用的代理框架和工具。

### 框架
- [ADK-Rust](https://github.com/zavora-ai/adk-rust) - 适用于 Rust 的生产就绪 AI 代理开发套件，具有与模型无关的设计（Gemini、OpenAI、Anthropic）、多种代理类型（LLM、Graph、Workflow）、MCP 支持和内置遥测。

### 工具
- [Frostbyte MCP](https://github.com/OzorOwn/frostbyte-mcp) - MCP 服务器为 AI 代理提供 13 种数据工具：实时加密价格、IP 地理位置、DNS 查找、网页抓取到 Markdown、代码执行和屏幕截图。一个 API 密钥可用于 40 多种服务。
- [Arch Tools](https://archtools.dev) - 61 个用于数据科学工作流程的生产就绪型 AI API 工具：代码分析、网页抓取、NLP、图像生成、加密数据和搜索。 REST API 和 MCP 协议支持。 [GitHub](https://github.com/Deesmo/Arch-AI-Tools)
- [Not Human Search](https://nothumansearch.ai) - AI 代理的搜索引擎，对 9,000 多个 AI 工具和 API 进行索引，根据代理准备情况对每个工具和 API 进行评分（llms.txt、OpenAPI、MCP、ai-plugin.json）。用于编程工具发现的 REST API 和 MCP 服务器。 [GitHub](https://github.com/unitedideas/not humansearch)
- [DeepAlpha](https://github.com/stefanoviana/deepalpha) - 使用 LightGBM + XGBoost 集成的 AI 加密交易框架，具有 72 个 ML 功能。样本外数据的前瞻验证准确度为 70.9%。支持Bybit和币安。 MIT 许可，可在 [PyPI](https://pypi.org/project/deepalpha-bot/) 上获取。
- [CAJAL](https://github.com/Agnuxo1/CAJAL) - 本地人工智能代理，用于生成具有真实 arXiv 引文、IMRaD 结构和法庭评分的可发表科学论文。 4B-9B 型号通过 Ollama 100% 离线运行。麻省理工学院许可。 [HuggingFace](https://huggingface.co/Agnuxo/CAJAL-9B-P2PCLAW)
- [ai-evaluation](https://github.com/future-agi/ai-evaluation) - 开源法学硕士和代理评估框架，具有 50 多个指标、法学硕士作为法官增强和护栏扫描仪（越狱、PII、提示注入）。对于对数据科学工作流程中的 RAG 输出、代理轨迹和函数调用行为进行评分非常有用。

### 研究与知识检索
- [BGPT MCP](https://bgpt.pro/mcp) - MCP 服务器使 AI 代理能够访问由全文研究中提取的原始实验数据构建的科学论文数据库。每篇论文返回 25 个以上的结构化字段，包括方法、结果、样本大小和质量分数。 [GitHub](https://github.com/connerlambden/bgpt-mcp)
- [Chunk Tuner](https://github.com/shantanu-deshmukh/chunktuner) - 开源 Python 库和 MCP 服务器，用于对 RAG 的文档分块策略进行基准测试、对检索质量进行评分并推荐语料库配置。
- [II-Commons](https://github.com/Intelligent-Internet/II-Commons-Skills) - 每日更新的技能和 CLI，用于跨 arXiv、PubMed/PMC 和支持的美国政策语料库的确定性检索。
- [Spraay x402 Gateway](https://docs.spraay.app/#cat-research) - x402 支付网关，具有 23 个 AI 代理研究和参考端点：维基百科、arXiv、PubMed、维基数据、学术引文查找、实体提取等。 Base 和 Solana 上的 USDC 按次付费 — 无需 API 密钥或订阅。还为 39 个类别的 150 多个端点提供服务，包括地理空间、AI 推理、DeFi 和计算。 [GitHub](https://github.com/plagtech)

- [Suppr](https://suppr.wilddata.cn/) - 人工智能文献检索、文档翻译和研究人员的深度研究工作区。

### 工作流程
**[`^ 回到顶部 ^`](#awesome-data-science)**
- [sim](https://sim.ai) - Sim Studio 的界面是一种轻量级、直观的方式，可以快速构建和部署与您喜爱的工具连接的 LLM。


## 培训资源
**[`^ 回到顶部 ^`](#awesome-data-science)**

你如何学习数据科学？当然是通过数据科学！好吧，好吧——当你刚开始的时候，这可能不是特别有帮助。在本节中，我们按照从最少到最大投入的粗略顺序列出了一些学习资源 - [教程](#tutorials)、[大规模开放在线课程 (MOOC)](#moocs)、[强化课程](#intense-programs) 和 [学院](#colleges)。


### 教程
**[`^ 回到顶部 ^`](#awesome-data-science)**

- [1000 个数据科学项目](https://cloud.blobcity.com/#/ps/explore) 您可以使用 IPython 在浏览器上运行。
- [#tidytuesday](https://github.com/rfordatascience/tidytuesday) - 针对 R 生态系统的每周数据项目。
- [数据科学你的方式](https://github.com/jadianes/data-science-your-way)
- [DataCamp Cheatsheets](https://www.datacamp.com/cheat-sheet) 数据科学备忘单。
- [PySpark 备忘单](https://github.com/kevinschaich/pyspark-cheatsheet)
- [使用 Python 进行机器学习、数据科学和深度学习 ](https://www.manning.com/livevideo/machine-learning-data-science-and-deep-learning-with-python)
- [TutorialSearch](https://tutorialsearch.io/) - 免费的跨平台搜索引擎，对来自 Udemy、Skillshare、Pluralsight 和其他主要学习平台的 45 多个类别的 50,000 多个教程进行索引。
- [潜在狄利克雷分配指南](https://medium.com/@lettier/how-does-lda-work-ill-explain-using-emoji-108abf40fa7d)
- [克林顿·谢泼德 (Clinton Sheppard) 所著的《Genetic Algorithms with Python》一书中的源代码教程](https://github.com/handcraftsman/GeneticAlgorithmsWithPython)
- [机器学习信号处理入门教程](https://github.com/jinglescode/python-signal-processing)
- [实时部署](https://www.microprediction.com/python-1) Python 时序模型部署教程。
- [Python 数据科学：初学者指南](https://learntocodewith.me/posts/python-for-data-science/)
- [机器学习面试的最低可行学习计划](https://github.com/khangich/machine-learning-interview)
- [通过构建可靠的项目来理解和了解机器学习工程](http://mlzoomcamp.com/)
- [12 个用于练习 Python 和 Pandas 的免费数据科学项目](https://www.datawars.io/articles/12-free-data-science-projects-to-practice-python-and-pandas)
- [数据科学新生的最佳简历](https://enhancv.com/resume-examples/data-scientist/)
- [了解 Java 数据科学课程](https://www.alter-solutions.com/articles/java-data-science)
- [数据分析面试问题（初级到高级）](https://www.appliedaicourse.com/blog/data-analytics-interview-questions/)
- [前 100 多个数据科学面试问题和答案](https://www.appliedaicourse.com/blog/data-science-interview-questions/)
- [DataDriven - SQL、Python 和数据建模面试问题](https://www.datadriven.io/)
- [StepByStepML](https://www.stepbystepml.com) - 交互式计算器，可可视化机器学习算法背后的逐步手动数学，以备考。
- [How to Build Optimal AI Agents That Actually Work](https://www.freecodecamp.org/news/how-to-build-optimal-ai-agents-that-actually-work-a-handbook-for-devs/) - 关于设计和构建有效的人工智能代理的开发人员手册。
- [Train LLM From Scratch](https://github.com/FareedKhan-dev/train-llm-from-scratch) - 培训法学硕士的简单方法，从下载数据到生成文本。

### 免费课程
**[`^ 回到顶部 ^`](#awesome-data-science)**

- [Data Science](https://github.com/ossu/data-science) - 开源协会大学
- [使用 R 的数据科学家](https://www.datacamp.com/tracks/data-scientist-with-r)
- [使用 Python 的数据科学家](https://www.datacamp.com/tracks/data-scientist-with-python)
- [遗传算法OCW课程](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-034-artificial-intelligence-fall-2010/lecture-videos/lecture-1-introduction-and-scope/)
- [AI Expert Roadmap](https://github.com/AMAI-GmbH/AI-Expert-Roadmap) - 成为人工智能专家的路线图
- [Convex Optimization](https://www.edx.org/course/convex-optimization) - 凸优化（凸分析的基础知识；最小二乘、线性和二次规划、半定规划、极小极大、极值体积和其他问题；最优条件、对偶理论...）
- [Learning from Data](https://home.work.caltech.edu/telecourse.html) - 机器学习简介，涵盖基础理论、算法和应用
- [Kaggle](https://www.kaggle.com/learn) - 了解数据科学、机器学习、Python 等
- [ML Observability Fundamentals](https://arize.com/ml-observability-fundamentals/) - 了解如何监控生产机器学习问题并找出根本原因。
- [Weights & Biases Effective MLOps: Model Development](https://www.wandb.courses/courses/effective-mlops-model-development) - 使用 W&B 构建端到端机器的免费课程和认证
- [Python for Data Science by Scaler](https://www.scaler.com/topics/course/python-for-data-science/) - 本课程旨在帮助初学者掌握在当今数据驱动的世界中脱颖而出的基本技能。全面的课程将为您在统计、编程、数据可视化和机器学习方面打下坚实的基础。
- [MLSys-NYU-2022](https://github.com/jacopotagliabue/MLSys-NYU-2022/tree/main) - 纽约大学 Tandon 2022 年金融机器学习课程的幻灯片、脚本和材料。
- [Hands-on Train and Deploy ML](https://github.com/Paulescu/hands-on-train-and-deploy-ml) - 培训和部署可预测加密货币价格的无服务器 API 的实践课程。
- [LLMOps: Building Real-World Applications With Large Language Models](https://www.comet.com/site/llm-course/) - 与法学硕士一起学习使用该领域最新的工具和技术构建现代软件。
- [Prompt Engineering for Vision Models](https://www.deeplearning.ai/short-courses/prompt-engineering-for-vision-models/) - 在 DeepLearning.AI 的这个免费课程中，学习如何使用自然语言、坐标点、边界框、分割掩模甚至其他图像来提示尖端计算机视觉模型。
- [Data Science Course By IBM](https://skillsbuild.org/students/course-catalog/data-science) - 免费资源并了解数据科学是什么以及它如何在不同行业中使用。
- [Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html) - Andrej Karpathy 的免费视频系列，涵盖从头开始的神经网络 - 反向传播、makemore、GPT 等。


  
### 慕课
**[`^ 回到顶部 ^`](#awesome-data-science)**

- [Coursera 数据科学简介](https://www.coursera.org/specializations/data-science)
- [数据科学 - 9 个步骤课程，Coursera 上的专业课程](https://www.coursera.org/specializations/jhu-data-science)
- [数据挖掘 - 5 个步骤课程，Coursera 上的专业课程](https://www.coursera.org/specializations/data-mining)
- [机器学习 – 5 步骤课程，Coursera 上的专业课程](https://www.coursera.org/specializations/machine-learning)
- [CS 109 数据科学](https://cs109.github.io/2015/)
- [OpenIntro](https://www.openintro.org/)
- [CS 171 可视化](https://www.cs171.org/#!index.md)
- [流程挖掘：数据科学的实践](https://www.coursera.org/learn/process-mining)
- [牛津深度学习](https://www.cs.ox.ac.uk/projects/DeepLearn/)
- [牛津深度学习 - 视频](https://www.youtube.com/playlist?list=PLE6Wd9FR--EfW8dtjAuPoTuPcqmOV53Fu)
- [牛津机器学习](https://www.cs.ox.ac.uk/research/ai_ml/index.html)
- [UBC 机器学习 - 视频](https://www.cs.ubc.ca/~nando/540-2013/lectures.html)
- [数据科学专业](https://github.com/DataScienceSpecialization/courses)
- [Coursera 大数据专业化](https://www.coursera.org/specializations/big-data)
- [Edx 的数据科学和分析统计思维](https://www.edx.org/course/statistical-thinking-for-data-science-and-analytic)
- [IBM 认知类 AI](https://cognitiveclass.ai/)
- [优达学城 - 深度学习](https://www.udacity.com/course/intro-to-tensorflow-for-deep-learning--ud187)
- [运动中的 Keras](https://www.manning.com/livevideo/keras-in-motion)
- [微软数据科学专业计划](https://academy.microsoft.com/en-us/professional-program/tracks/data-science/)
- [COMP3222/COMP6246 - 机器学习技术](https://tdgunes.com/COMP6246-2019Fall/)
- [CS 231 - 用于视觉识别的卷积神经网络](https://cs231n.github.io/)
- [Coursera Tensorflow 实践](https://www.coursera.org/professional-certificates/tensorflow-in-practice)
- [Coursera 深度学习专业化](https://www.coursera.org/specializations/deep-learning)
- [365 数据科学课程](https://365datascience.com/)
- [Coursera 自然语言处理专业课程](https://www.coursera.org/specializations/natural-language-processing)
- [Coursera GAN 专业化](https://www.coursera.org/specializations/generative-adversarial-networks-gans)
- [Codecademy 的数据科学](https://www.codecademy.com/learn/paths/data-science)
- [Linear Algebra](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/) - 吉尔伯特·斯特朗 (Gilbert Strang) 的线性代数课程
- [线性代数 2020 年愿景 (G. Strang)](https://ocw.mit.edu/resources/res-18-010-a-2020-vision-of-linear-algebra-spring-2020/)
- [Python 数据科学基础课程](https://intellipaat.com/academy/course/python-for-data-science-free-training/)
- [数据科学：统计与机器学习](https://www.coursera.org/specializations/data-science-statistics-machine-learning)
- [生产机器学习工程 (MLOps)](https://www.coursera.org/specializations/machine-learning-engineering-for-production-mlops)
- [明尼苏达大学推荐系统专业](https://www.coursera.org/specializations/recommender-systems) 是一个中级/高级专业，专注于 Coursera 平台上的推荐系统。
- [斯坦福人工智能专业项目](https://online.stanford.edu/programs/artificial-intelligence-professional-program)
- [使用 Python 的数据科学家](https://app.datacamp.com/learn/career-tracks/data-scientist-with-python)
- [与 Julia 一起编程](https://www.udemy.com/course/programming-with-julia/)
- [Scaler 数据科学与机器学习计划](https://www.scaler.com/data-science-course/)
- [数据科学技能树](https://labex.io/skilltrees/data-science)
- [数据科学初学者 - 与 AI 导师一起学习](https://codekidz.ai/lesson-intro/data-science-368dbf)
- [初学者机器学习 - 与 AI 导师一起学习](https://codekidz.ai/lesson-intro/machine-lear-36abfb)
- [数据科学导论](https://www.mygreatlearning.com/academy/learn-for-free/courses/introduction-to-data-science)
-[Python 数据科学入门](https://www.codecademy.com/learn/getting-started-with-python-for-data-science)
- [Google Advanced Data Analytics Certificate](https://grow.google/data-analytics/) - 数据分析、统计学和机器学习基础知识的专业课程。
- [Maschinelle Sprachgebrauchsanalyse - Grundlagen der Korpuslinguistik](https://www.twillo.de/edu-sharing/components/collections?id=e6ce03ae-4660-49b0-be10-dcc92e71e796) - 关于文本挖掘/语料库语言学的课程材料*德语*由北莱茵-威斯特法伦州资助
- [Programmieren für Germanist*innen](https://www.twillo.de/edu-sharing/components/collections?id=16bac749-f10e-483f-9020-5d6365b4e092) - 课程材料：用于数字人文的 Python *德语* 编程 - 由北莱茵-威斯特法伦州联邦资助

### 强化课程
**[`^ 回到顶部 ^`](#awesome-data-science)**

- [S2DS](https://www.s2ds.org/)
- [WorldQuant大学应用数据科学实验室](https://www.wqu.edu/adsl)


### 学院
**[`^ 回到顶部 ^`](#awesome-data-science)**

- [提供数据科学学位的学院和大学列表。](https://github.com/ryanswanstrom/awesome-datascience-colleges)
- [伯克利数据科学学位](https://ischoolonline.berkeley.edu/data-science/)
- [UVA 数据科学学位](https://datascience.virginia.edu/)
- [威斯康星州数据科学学位](https://datasciencedegree.wisconsin.edu/)
- [数据科学与应用学士学位](https://study.iitm.ac.in/ds/)
- [波士顿大学计算机信息系统硕士](https://www.bu.edu/online/programs/graduate-programs/computer-information-systems-masters-degree/)
- [亚利桑那州立大学在线商业分析硕士](https://asuonline.asu.edu/online-degree-programs/graduate/master-science-business-analytics/)
- [应用数据科学硕士@雪城大学](https://ischool.syr.edu/academics/applied-data-science-masters-degree/)
- [硕士管理与数据科学 @ Leuphana](https://www.leuphana.de/en/graduate-school/masters-programmes/management-data-science.html)
- [墨尔本大学数据科学硕士](https://study.unimelb.edu.au/find/courses/graduate/master-of-data-science/#overview)
- [爱丁堡大学数据科学硕士](https://www.ed.ac.uk/studying/postgraduate/degrees/index.php?r=site/view&id=902)
- [女王大学管理分析硕士](https://smith.queensu.ca/grad_studies/mma/index.php)
- [伊利诺伊理工学院数据科学硕士](https://www.iit.edu/academics/programs/data-science-mas)
- [密歇根大学应用数据科学硕士](https://www.si.umich.edu/programs/master-applied-data-science)
- [埃因霍温科技大学数据科学与人工智能硕士](https://www.tue.nl/en/education/graduate-school/master-data-science-and-artificial-intelligence/)
- [格拉纳达大学数据科学和计算机工程硕士学位](https://masteres.ugr.es/datcom/)

## 数据科学工具箱
**[`^ 回到顶部 ^`](#awesome-data-science)**

本节是数据科学领域中的包、工具、算法和其他有用项目的集合。

### 算法
**[`^ 回到顶部 ^`](#awesome-data-science)**

这些是一些机器学习和数据挖掘算法和模型，可帮助您理解数据并从中获取意义。

#### 三种机器学习系统

- 基于人工监督下的培训
- 基于动态增量学习
- 基于数据点比较和模式检测

### 比较
- [datacompy](https://github.com/capitalone/datacompy) - DataComPy 是一个用于比较两个 Pandas DataFrame 的包。

#### 监督学习

- [Regression](https://en.wikipedia.org/wiki/Regression)
- [线性回归](https://en.wikipedia.org/wiki/Linear_regression)
- [普通最小二乘法](https://en.wikipedia.org/wiki/Ordinary_least_squares)
- [逻辑回归](https://en.wikipedia.org/wiki/Logistic_regression)
- [逐步回归](https://en.wikipedia.org/wiki/Stepwise_regression)
- [多元自适应回归样条](https://en.wikipedia.org/wiki/Multivariate_adaptive_regression_spline)
- [Softmax回归](https://d2l.ai/chapter_linear-classification/softmax-regression.html)
- [局部估计散点图平滑](https://en.wikipedia.org/wiki/Local_regression)
- 分类
  - [k-最近邻](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm)
  - [支持向量机](https://en.wikipedia.org/wiki/Support_vector_machine)
  - [决策树](https://en.wikipedia.org/wiki/Decision_tree)
  - [ID3算法](https://en.wikipedia.org/wiki/ID3_algorithm)
  - [C4.5算法](https://en.wikipedia.org/wiki/C4.5_algorithm)
- [集成学习](https://scikit-learn.org/stable/modules/ensemble.html)
- [Boosting](https://en.wikipedia.org/wiki/Boosting_(machine_learning))
  - [Stacking](https://machinelearningmastery.com/stacking-ensemble-machine-learning-with-python)
  - [Bagging](https://en.wikipedia.org/wiki/Bootstrap_aggregating)
  - [随机森林](https://en.wikipedia.org/wiki/Random_forest)
  - [AdaBoost](https://en.wikipedia.org/wiki/AdaBoost)

#### 无监督学习
- [Clustering](https://scikit-learn.org/stable/modules/clustering.html#clustering)
  - [层次聚类](https://scikit-learn.org/stable/modules/clustering.html#hierarchical-clustering)
  - [k-means](https://scikit-learn.org/stable/modules/clustering.html#k-means)
  - [基于密度的聚类](https://scikit-learn.org/stable/modules/clustering.html#dbscan)
  - [模糊聚类](https://en.wikipedia.org/wiki/Fuzzy_clustering)
  - [混合模型](https://en.wikipedia.org/wiki/Mixture_model)
- [降维](https://en.wikipedia.org/wiki/Dimensionality_reduction)
  - [主成分分析（PCA）](https://scikit-learn.org/stable/modules/decomposition.html#principal-component-analysis-pca)
  - [t-SNE； t 分布随机邻域嵌入](https://scikit-learn.org/stable/modules/manifold.html#t-distributed-stochastic-neighbor-embedding-tsne)
  - [因素分析](https://scikit-learn.org/stable/modules/decomposition.html#factor-analysis)
  - [潜在狄利克雷分配 (LDA)](https://scikit-learn.org/stable/modules/decomposition.html#latent-dirichlet-allocation-lda)
- [神经网络](https://en.wikipedia.org/wiki/Neural_network)
- [自组织映射](https://en.wikipedia.org/wiki/Self-organizing_map)
- [自适应共振理论](https://en.wikipedia.org/wiki/Adaptive_resonance_theory)
- [隐马尔可夫模型 (HMM)](https://en.wikipedia.org/wiki/Hidden_Markov_model)

#### 半监督学习

- S3VM
- [Clustering](https://en.wikipedia.org/wiki/Weak_supervision#Cluster_assumption)
- [生成模型](https://en.wikipedia.org/wiki/Weak_supervision#Generative_models)
- [低密度分离](https://en.wikipedia.org/wiki/Weak_supervision#Low-density_separation)
- [拉普拉斯正则化](https://en.wikipedia.org/wiki/Weak_supervision#Laplacian_regularization)
- [启发式方法](https://en.wikipedia.org/wiki/Weak_supervision#Heuristic_approaches)

#### 强化学习

- [问学习](https://en.wikipedia.org/wiki/Q-learning)
- [SARSA（状态-行动-奖励-状态-行动）算法](https://en.wikipedia.org/wiki/State%E2%80%93action%E2%80%93reward%E2%80%93state%E2%80%93action)
- [时间差异学习](https://en.wikipedia.org/wiki/Temporal_difference_learning#:~:text=Temporal%20difference%20(TD)%20learning%20refers,estimate%20of%20the%20value%20function.)

#### 数据挖掘算法

- [C4.5](https://en.wikipedia.org/wiki/C4.5_algorithm)
- [k-Means](https://en.wikipedia.org/wiki/K-means_clustering)
- [SVM（支持向量机）](https://en.wikipedia.org/wiki/Support_vector_machine)
- [Apriori](https://en.wikipedia.org/wiki/Apriori_algorithm)
- [EM（期望最大化）](https://en.wikipedia.org/wiki/Expectation%E2%80%93maximization_algorithm)
- [PageRank](https://en.wikipedia.org/wiki/PageRank)
- [AdaBoost](https://en.wikipedia.org/wiki/AdaBoost)
- [KNN（K 最近邻）](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm)
- [朴素贝叶斯](https://en.wikipedia.org/wiki/Naive_Bayes_classifier)
- [CART（分类和回归树）](https://en.wikipedia.org/wiki/Decision_tree_learning)
#### 现代数据挖掘算法

- [XGBoost（极限梯度提升）](https://en.wikipedia.org/wiki/XGBoost)
- [LightGBM（光梯度增强机）](https://en.wikipedia.org/wiki/LightGBM)
- [CatBoost](https://catboost.ai/)
- [HDBSCAN（基于分层密度的噪声应用空间聚类）](https://en.wikipedia.org/wiki/DBSCAN#HDBSCAN)
- [FP-Growth（频繁模式增长算法）](https://en.wikipedia.org/wiki/Association_rule_learning#FP-growth_algorithm)
- [隔离森林](https://en.wikipedia.org/wiki/Isolation_forest)
- [深度嵌入式聚类 (DEC)](https://arxiv.org/abs/1511.06335)
- [TPU（Top-k 周期性和高实用性模式）](https://arxiv.org/abs/2509.15732)
- [上下文感知规则挖掘（基于转换器的框架）](https://arxiv.org/abs/2503.11125)


#### 深度学习架构

- [多层感知器](https://en.wikipedia.org/wiki/Multilayer_perceptron)
- [卷积神经网络（CNN）](https://en.wikipedia.org/wiki/Convolutional_neural_network)
- [循环神经网络 (RNN)](https://en.wikipedia.org/wiki/Recurrent_neural_network)
- [玻尔兹曼机](https://en.wikipedia.org/wiki/Boltzmann_machine)
- [Autoencoder](https://www.tensorflow.org/tutorials/generative/autoencoder)
- [生成对抗网络（GAN）](https://developers.google.com/machine-learning/gan/gan_structure)
- [自组织映射](https://en.wikipedia.org/wiki/Self-organizing_map)
- [Transformer](https://www.tensorflow.org/text/tutorials/transformer)
- [条件随机场 (CRF)](https://towardsdatascience.com/conditional-random-fields-explained-e5b8256da776)
- [机器学习系统设计）](https://www.evidentlyai.com/ml-system-design)

### 通用机器学习包
**[`^ 回到顶部 ^`](#awesome-data-science)**

* [scikit-learn](https://scikit-learn.org/)
* [scikit-multilearn](https://github.com/scikit-multilearn/scikit-multilearn)
* [sklearn-expertsys](https://github.com/tmadl/sklearn-expertsys)
* [scikit-feature](https://github.com/jundongl/scikit-feature)
* [scikit-rebate](https://github.com/EpistasisLab/scikit-rebate)
* [seqlearn](https://github.com/larsmans/seqlearn)
* [sklearn-bayes](https://github.com/AmazaspShumik/sklearn-bayes)
* [sklearn-crfsuite](https://github.com/TeamHG-Memex/sklearn-crfsuite)
* [sklearn-deap](https://github.com/rsteca/sklearn-deap)
* [sigopt_sklearn](https://github.com/sigopt/sigopt-sklearn)
* [sklearn-evaluation](https://github.com/edublancas/sklearn-evaluation)
* [scikit-image](https://github.com/scikit-image/scikit-image)
* [scikit-opt](https://github.com/guofei9987/scikit-opt)
* [scikit-posthocs](https://github.com/maximtrp/scikit-posthocs)
* [feature-engine](https://feature-engine.trainindata.com/)
* [pystruct](https://github.com/pystruct/pystruct)
* [Shogun](https://www.shogun-toolbox.org/)
* [xLearn](https://github.com/aksnzhy/xlearn)
* [cuML](https://github.com/rapidsai/cuml)
* [causalml](https://github.com/uber/causalml)
* [mlpack](https://github.com/mlpack/mlpack)
* [MLxtend](https://github.com/rasbt/mlxtend)
* [modAL](https://github.com/modAL-python/modAL)
* [Sparkit-learn](https://github.com/lensacom/sparkit-learn)
* [hyperlearn](https://github.com/danielhanchen/hyperlearn)
* [dlib](https://github.com/davisking/dlib)
* [imodels](https://github.com/csinva/imodels)
* [jSciPy](https://github.com/hissain/jscipy) - SciPy 信号处理模块的 Java 端口，提供过滤器、转换和其他科学计算实用程序。
* [RuleFit](https://github.com/christophM/rulefit)
* [pyGAM](https://github.com/dswah/pyGAM)
* [Deepchecks](https://github.com/deepchecks/deepchecks)
* [scikit-survival](https://scikit-survival.readthedocs.io/en/stable)
* [interpretable](https://pypi.org/project/interpretable)
* [XGBoost](https://github.com/dmlc/xgboost)
* [LightGBM](https://github.com/microsoft/LightGBM)
* [CatBoost](https://github.com/catboost/catboost)
* [PerpetualBooster](https://github.com/perpetual-ml/perpetual)
* [JAX](https://github.com/google/jax)



### 深度学习包

#### PyTorch 生态系统
* [PyTorch](https://github.com/pytorch/pytorch)
* [torchvision](https://github.com/pytorch/vision)
* [torchtext](https://github.com/pytorch/text)
* [torchaudio](https://github.com/pytorch/audio)
* [ignite](https://github.com/pytorch/ignite)
* [PyTorchNet](https://github.com/pytorch/tnt)
* [PyToune](https://github.com/GRAAL-Research/poutyne)
* [skorch](https://github.com/skorch-dev/skorch)
* [PyVarInf](https://github.com/ctallec/pyvarinf)
* [pytorch_geometric](https://github.com/pyg-team/pytorch_geometric)
* [GPyTorch](https://github.com/cornellius-gp/gpytorch)
* [pyro](https://github.com/pyro-ppl/pyro)
* [Catalyst](https://github.com/catalyst-team/catalyst)
* [pytorch_tabular](https://github.com/manujosephv/pytorch_tabular)
* [Yolov3](https://github.com/ultralytics/yolov3)
* [Yolov5](https://github.com/ultralytics/yolov5)
* [Yolov8](https://github.com/ultralytics/ultralytics)

#### TensorFlow 生态系统
* [TensorFlow](https://github.com/tensorflow/tensorflow)
* [TensorLayer](https://github.com/tensorlayer/TensorLayer)
* [TFLearn](https://github.com/tflearn/tflearn)
* [Sonnet](https://github.com/deepmind/sonnet)
* [tensorpack](https://github.com/tensorpack/tensorpack)
* [TRFL](https://github.com/deepmind/trfl)
* [Polyaxon](https://github.com/polyaxon/polyaxon)
* [NeuPy](https://github.com/itdxer/neupy)
* [tfdeploy](https://github.com/riga/tfdeploy)
* [tensorflow-upstream](https://github.com/ROCmSoftwarePlatform/tensorflow-upstream)
* [TensorFlow 折叠](https://github.com/tensorflow/fold)
* [tensorlm](https://github.com/batzner/tensorlm)
* [TensorLight](https://github.com/bsautermeister/tensorlight)
* [网格 TensorFlow](https://github.com/tensorflow/mesh)
* [Ludwig](https://github.com/ludwig-ai/ludwig)
* [TF-Agents](https://github.com/tensorflow/agents)
* [TensorForce](https://github.com/tensorforce/tensorforce)

#### Keras 生态系统

* [Keras](https://keras.io)
* [keras-contrib](https://github.com/keras-team/keras-contrib)
* [Hyperas](https://github.com/maxpumperla/hyperas)
* [Elephas](https://github.com/maxpumperla/elephas)
* [Hera](https://github.com/keplr-io/hera)
* [Spektral](https://github.com/danielegrattarola/spektral)
* [qkeras](https://github.com/google/qkeras)
* [keras-rl](https://github.com/keras-rl/keras-rl)
* [Talos](https://github.com/autonomio/talos)

#### 可视化工具
**[`^ 回到顶部 ^`](#awesome-data-science)**

- [altair](https://altair-viz.github.io/)
- [amcharts](https://www.amcharts.com/)
- [anychart](https://www.anychart.com/)
- [bokeh](https://bokeh.org/)
- [Comet](https://www.comet.com/site/products/ml-experiment-tracking/?utm_source=awesome-datascience)
- [slemma](https://slemma.com/)
- [cartodb](https://cartodb.github.io/odyssey.js/)
- [Cube](https://square.github.io/cube/)
- [d3plus](https://d3plus.org/)
- [数据驱动文档(D3js)](https://d3js.org/)
- [dygraphs](https://dygraphs.com/)
- [exhibit](https://www.simile-widgets.org/exhibit/)
- [gephi](https://gephi.org/)
- [ggplot2](https://ggplot2.tidyverse.org/)
- [Glue](http://docs.glueviz.org/en/latest/index.html)
- [谷歌图表库](https://developers.google.com/chart/interactive/docs/gallery)
- [Highcharts](https://www.highcharts.com/)
- [import.io](https://www.import.io/)
- [Matplotlib](https://matplotlib.org/)
- [nvd3](https://nvd3.org/)
- [Netron](https://github.com/lutzroeder/netron)
- [Openrefine](https://openrefine.org/)
- [plot.ly](https://plot.ly/)
- [raw](https://rawgraphs.io)
- [保留精简版](https://github.com/abistarun/resseract-lite)
- [Seaborn](https://seaborn.pydata.org/)
- [techanjs](https://techanjs.org/)
- [Timeline](https://timeline.knightlab.com/)
- [variancecharts](https://variancecharts.com/index.html)
- [vida](https://vida.io/)
- [vizzu](https://github.com/vizzuhq/vizzu-lib)
- [Wrangler](http://vis.stanford.edu/wrangler/)
- [r2d3](http://www.r2d3.us/visual-intro-to-machine-learning-part-1/)
- [NetworkX](https://networkx.org/)
- [Redash](https://redash.io/)
- [Metabase](https://www.metabase.com/)
- [C3](https://c3js.org/)
- [TensorWatch](https://github.com/microsoft/tensorwatch)
- [geomap](https://pypi.org/project/geomap/)
- [Dash](https://plotly.com/dash/)
- [MetaReview](https://metareview-8c1.pages.dev/) - 免费在线荟萃分析平台，具有 11 个交互式 D3.js 统计图表（森林图、漏斗图、Galbraith、L'Abbé、Baujat 等）、5 个效应量度量、AI 文献筛选和可出版的报告导出。 [github.com](https://github.com/TerryFYL/metareview)
- [torchvista](https://github.com/sachinhosmani/torchvista) - 基于交互式笔记本的工具，用于可视化任何 PyTorch 模型的前向传播。

### 杂项工具
**[`^ 回到顶部 ^`](#awesome-data-science)**

|链接 |描述 |
| --- | --- |
| [数据科学生命周期过程](https://github.com/dslp/dslp) |数据科学生命周期过程是一个反复、可持续地将数据科学团队从想法转变为价值的过程。该过程记录在此存储库中 |
| [数据科学生命周期模板存储库](https://github.com/dslp/dslp-repo-template) |数据科学生命周期项目的模板存储库 |
| [TabGAN](https://github.com/Diyago/Tabular-data- Generation) |使用 GAN、扩散模型和 LLM 以及对抗性过滤和隐私指标生成合成表格数据。 |
| [RexMex](https://github.com/AstraZeneca/rexmex) |用于公平评估的通用推荐指标库。  |
| [ChemicalX](https://github.com/AstraZeneca/chemicalx) |基于 PyTorch 的深度学习库，用于药物对评分。  |
| [FileShot.io](https://github.com/FileShot/FileShotZKE) |安全的零知识加密文件共享（浏览器内的 AES-256-GCM）。无需帐户，麻省理工学院许可，可自行托管，可选链接到期。 |
| [CorpusExplorer](http://corpusexplorer.de/) |面向语料库语言学家和文本/数据挖掘爱好者的软件。以 60 多种语言构建您自己的语料库。使用 50 多种工具/可视化。  |
| [PyTorch 几何时态](https://github.com/benedekrozemberczki/pytorch_geometric_temporal) |动态图的表示学习。  |
| [小毛球](https://github.com/benedekrozemberczki/littleballoffur) | NetworkX 的图形采样库，具有类似 Scikit-Learn 的 API。  |
| [空手道俱乐部](https://github.com/benedekrozemberczki/karateclub) | NetworkX 的无监督机器学习扩展库，具有类似 Scikit-Learn 的 API。 |
| [ML 工作区](https://github.com/ml-tooling/ml-workspace) |用于机器学习和数据科学的基于 Web 的一体化 IDE。该工作区部署为 Docker 容器，并预加载了各种流行的数据科学库（例如 Tensorflow、PyTorch）和开发工具（例如 Jupyter、VS Code）|
| [xonsh shell](https://github.com/xonsh/xonsh) |一个由 Python 驱动的 shell，可以集成、管理和编排主要用 Python 编写的数据科学库，让您可以构建管道、代码和基于命令的工作流程。它还可以用作 Jupyter Notebook 的内核。  |
| [Neptune.ai](https://neptune.ai) |社区友好型平台，支持数据科学家创建和共享机器学习模型。 Neptune 促进团队合作、基础设施管理、模型比较和再现性。 |
| [steppy](https://github.com/minerva-ml/steppy) |用于快速且可重复的机器学习实验的轻量级 Python 库。引入了非常简单的界面，可以实现干净的机器学习管道设计。 |
| [steppy-toolkit](https://github.com/minerva-ml/steppy-toolkit) |神经网络、变压器和模型的精选集合，使您的机器学习工作更快、更有效。 |
| [来自 Google 的 Datalab](https://cloud.google.com/datalab/docs/) |使用熟悉的语言（例如 Python 和 SQL）以交互方式轻松探索、可视化、分析和转换数据。 |
| [Hortonworks 沙箱](https://www.cloudera.com/downloads/hortonworks-sandbox.html) |是一个个人、便携式 Hadoop 环境，附带十几个交互式 Hadoop 教程。 |
| [R](https://www.r-project.org/) |是一个用于统计计算和图形的免费软件环境。 |
| [Tidyverse](https://www.tidyverse.org/) |是专为数据科学设计的 R 软件包的固执己见的集合。所有包都共享底层设计理念、语法和数据结构。 |
| [RStudio](https://www.rstudio.com) | IDE – 强大的 R 用户界面。它是免费且开源的，适用于 Windows、Mac 和 Linux。 |
| [Python - 熊猫 - Anaconda](https://www.anaconda.com) |完全免费的企业级 Python 发行版，用于大规模数据处理、预测分析和科学计算 |
| [Pandas GUI](https://github.com/adrotog/PandasGUI) |熊猫图形用户界面 |
| [极地](https://github.com/pola-rs/polars) |适用于 Rust 和 Python 的快速 DataFrame 库，旨在作为 Pandas 的更快替代方案 |
| [CiteMe](https://citeme.app) |人工智能驱动的学术引文生成器。搜索 11 多个学术数据库（OpenAlex、PubMed、Semantic Sc​​holar、CrossRef、SciELO）并以 40 多种引文样式格式化参考文献。可作为网络应用程序、浏览器扩展、Google 文档插件和公共 API 提供。 |
| [Scikit-Learn](https://scikit-learn.org/stable/) | Python 中的机器学习 |
| [NumPy](https://numpy.org/) | NumPy 是使用 Python 进行科学计算的基础。它支持大型多维数组和矩阵，并包含各种高级数学函数来对这些数组进行操作。 |
| [Vaex](https://vaex.io/) | Vaex 是一个 Python 库，可让您可视化大型数据集并高速计算统计数据。 |
| [SciPy](https://scipy.org/) | SciPy 与 NumPy 数组配合使用，并为数值积分和优化提供有效的例程。 |
| [数据科学工具箱](https://www.coursera.org/learn/data-scientists-tools) | Coursera 课程 |
| [数据科学工具箱](https://datasciencetoolbox.org/) |博客 |
| [Wolfram 数据科学平台](https://www.wolfram.com/data-science-platform/) |采用数值、文本、图像、GIS 或其他数据并对其进行 Wolfram 处理，进行全方位的数据科学分析和可视化，并自动生成丰富的交互式报告 - 所有这些都由革命性的基于知识的 Wolfram 语言提供支持。 |
| [Datadog](https://www.datadoghq.com/) |适用于大规模数据科学的解决方案、代码和开发运营。 |
| [方差](https://variancecharts.com/) |无需编写 JavaScript 即可构建强大的 Web 数据可视化 |
| [Kite 开发套件](http://kitesdk.org/docs/current/index.html) | Kite 软件开发工具包（Apache 许可证，版本 2.0）（简称 Kite）是一组库、工具、示例和文档，专注于让您更轻松地在 Hadoop 生态系统之上构建系统。 |
| [多米诺数据实验室](https://www.dominodatalab.com) |运行、扩展、共享和部署您的模型——无需任何基础设施或设置。 |
| [Apache Flink](https://flink.apache.org/) |高效、分布式、通用数据处理平台。 |
| [阿帕奇哈马](https://hama.apache.org/) | Apache Hama 是一个 Apache 顶级开源项目，允许您进行 MapReduce 之外的高级分析。 |
| [Weka](https://ml.cms.waikato.ac.nz/weka/index.html) | Weka 是用于数据挖掘任务的机器学习算法的集合。 |
| [八度](https://www.gnu.org/software/octave/) | GNU Octave 是一种高级解释语言，主要用于数值计算。（免费 Matlab） |
| [Apache Spark](https://spark.apache.org/) |快如闪电的集群计算 |
| [水圈薄雾](https://github.com/Hydrospheredata/mist) |用于将 Apache Spark 分析作业和机器学习模型公开为实时、批处理或反应式 Web 服务的服务。 |
| [数据力学](https://www.datamechanics.co) |一个数据科学和工程平台，使 Apache Spark 对开发人员更加友好且更具成本效益。 |
| [Caffe](https://caffe.berkeleyvision.org/) |深度学习框架|
| [火炬](http://torch.ch/) | LUAJIT 的科学计算框架 |
| [Nervana 基于 python 的深度学习框架](https://github.com/NervanaSystems/neon) |英特尔® Nervana™ 参考深度学习框架致力于在所有硬件上实现最佳性能。 |
| [Skale](https://github.com/skale-me/skale) | NodeJS 中的高性能分布式数据处理 |
| [Aerosolve](https://airbnb.io/aerosolve/) |为人类构建的机器学习包。 |
| [英特尔框架](https://github.com/intel/idlf) |英特尔® 深度学习框架 |
| [数据包装器](https://www.datawrapper.de/) |一个开源数据可视化平台，帮助每个人创建简单、正确和可嵌入的图表。也在 [github.com](https://github.com/datawrapper/datawrapper) |
| [张量流](https://www.tensorflow.org/) | TensorFlow 是一个用于机器智能的开源软件库 |
| [自然语言工具包](https://www.nltk.org/) |用于自然语言处理和分类的介绍性但功能强大的工具包 |
| [FunASR](https://github.com/modelscope/FunASR) |工业级语音识别工具包，支持 50 多种语言，内置 VAD、标点符号、说话人分类和情绪检测。包含与 OpenAI 兼容的 API 服务器。 |
| [注释实验室](https://www.johnsnowlabs.com/annotation-lab/) |用于文本注释和深度学习模型训练/调整的免费端到端无代码平台。对命名实体识别、分类、关系提取和断言状态 Spark NLP 模型的开箱即用支持。对用户、团队、项目、文档的无限支持。 |
| [node.js 的 nlp 工具包](https://www.npmjs.com/package/nlp-toolkit) |本模块涵盖一些基本的 nlp 原理和实现。主要关注点是性能。当我们在 nlp 中处理样本或训练数据时，我们很快就会耗尽内存。因此，该模块中的每个实现都被写入为流，以仅将当前在任何步骤处理的数据保存在内存中。 |
| [朱莉娅](https://julialang.org) |用于技术计算的高级、高性能动态编程语言 |
| [IJulia](https://github.com/JuliaLang/IJulia.jl) |与 Jupyter 交互环境相结合的 Julia 语言后端 |
| [阿帕奇齐柏林](https://zeppelin.apache.org/) |基于 Web 的笔记本，支持使用 SQL、Scala 等进行数据驱动、交互式数据分析和协作文档 |
| [Featuretools](https://github.com/alteryx/featuretools) |用 python 编写的自动化特征工程开源框架 |
| [擎天柱](https://github.com/hi-primus/optimus) |使用 PySpark 后端进行清理、预处理、特征工程、探索性数据分析和简单的机器学习。  |
| [Albumentations](https://github.com/albumentations-team/albumentations) |快速且与框架无关的图像增强库，实现了多种增强技术。支持开箱即用的分类、分割和检测。用于赢得 Kaggle、Topcoder 以及 CVPR 研讨会的多项深度学习竞赛。 |
| [DVC](https://github.com/iterative/dvc) |开源数据科学版本控制系统。它有助于跟踪、组织数据科学项目并使之可重复。在其非常基本的场景中，它有助于版本控制并共享大型数据和模型文件。 |
| [Lambdo](https://github.com/asavinov/lambdo) |是一种工作流引擎，通过将 (i) 特征工程和机器学习 (ii) 模型训练和预测 (iii) 表填充和列评估结合到一个分析管道中，显着简化了数据分析。 |
| [盛宴](https://github.com/feast-dev/feast) |用于管理、发现和访问机器学习功能的功能存储。 Feast 为模型训练和模型服务提供一致的特征数据视图。 |
| [多轴](https://github.com/polyaxon/polyaxon) |一个用于可重复和可扩展的机器学习和深度学习的平台。 |
| [UBIAI](https://ubiai.tools) |易于使用的文本注释工具，为团队提供最全面的自动注释功能。支持 NER、关系和文档分类以及发票标签的 OCR 注释 |
| [火车](https://github.com/allegroai/clearml) | Auto-Magical Experiment Manager、AI 版本控制和 DevOps |
| [Hopsworks](https://github.com/ologicalclocks/hopsworks) |具有特征存储的开源数据密集型机器学习平台。摄取和管理在线（MySQL Cluster）和离线（Apache Hive）访问、大规模训练和服务模型的功能。 |
| [MindsDB](https://github.com/mindsdb/mindsdb) | MindsDB 是一个为开发人员提供的可解释的 AutoML 框架。借助 MindsDB，您只需一行代码即可构建、训练和使用最先进的 ML 模型。 |
| [Lightwood](https://github.com/mindsdb/lightwood) |一种基于 Pytorch 的框架，可将机器学习问题分解为更小的块，这些块可以无缝地粘合在一起，目标是用一行代码构建预测模型。 |
| [AWS 数据牧马人](https://github.com/awslabs/aws-data-wrangler) |一个开源 Python 包，可将 Pandas 库的功能扩展到 AWS，连接 DataFrame 和 AWS 数据相关服务（Amazon Redshift、AWS Glue、Amazon Athena、Amazon EMR 等）。 |
| [Amazon Rekognition](https://aws.amazon.com/rekognition/) | AWS Rekognition 是一项服务，可让使用 Amazon Web Services 的开发人员将图像分析添加到其应用程序中。编目资产、自动化工作流程并从媒体和应用程序中提取意义。|
| [亚马逊 Textract](https://aws.amazon.com/texttract/) |自动从任何文档中提取打印文本、手写内容和数据。 |
| [亚马逊 Lookout for Vision](https://aws.amazon.com/lookout-for-vision/) |使用计算机视觉发现产品缺陷以实现自动化质量检查。识别缺失的产品组件、车辆和结构损坏以及违规行为，以进行全面的质量控制。
| [Amazon CodeGuru](https://aws.amazon.com/codeguru/) |通过 ML 支持的建议自动进行代码审查并优化应用程序性能。
| [CML](https://github.com/iterative/cml) |用于在数据科学项目中使用持续集成的开源工具包。使用 GitHub Actions 和 GitLab CI 在类似生产的环境中自动训练和测试模型，并自动生成有关拉取/合并请求的可视化报告。 |
| [Dask](https://dask.org/) |一个开源 Python 库，可轻松将您的分析代码转移到分布式计算系统（大数据）|
| [DuckDB](https://github.com/duckdb/duckdb) |进程内 SQL OLAP 数据库管理系统 |
| [Statsmodels](https://www.statsmodels.org/stable/index.html) |基于Python的推论统计、假设检验和回归框架|
| [Gensim](https://radimrehurek.com/gensim/) |用于自然语言文本主题建模的开源库 |
| [spaCy](https://spacy.io/) |高性能自然语言处理工具包 |
| [网格工作室](https://github.com/ricklamers/gridstudio) | Grid studio 是一个基于 Web 的电子表格应用程序，完全集成了 Python 编程语言。 |
|[Python 数据科学手册](https://github.com/jakevdp/PythonDataScienceHandbook)|Python 数据科学手册：Jupyter Notebooks 中的全文|
| [沙普利](https://github.com/benedekrozemberczki/shapley) |一个数据驱动的框架，用于量化机器学习集成中分类器的价值。  |
| [DAGsHub](https://dagshub.com) |一个基于开源工具构建的平台，用于数据、模型和管道管理。  |
| [Deepnote](https://deepnote.com) |一种新型数据科学笔记本。兼容 Jupyter，可实时协作并在云端运行。 |
| [Valohai](https://valohai.com) |一个处理机器编排、自动再现和部署的 MLOps 平台。 |
| [PyMC3](https://docs.pymc.io/) |用于概率编程（贝叶斯推理和机器学习）的 Python 库 |
| [PyStan](https://pypi.org/project/pystan/) | Stan 的 Python 接口（贝叶斯推理和建模）|
| [hmmlearn](https://pypi.org/project/hmmlearn/) |隐马尔可夫模型的无监督学习和推理 |
| [混沌天才](https://github.com/chaos-genius/chaos_genius/) |机器学习驱动的分析引擎，用于异常值/异常检测和根本原因分析 |
| [Nimblebox](https://nimblebox.ai/) |一个全栈 MLOps 平台，旨在帮助世界各地的数据科学家和机器学习从业者通过网络浏览器发现、创建和启动多云应用程序。 |
| [Towhee](https://github.com/towhee-io/towhee) |一个 Python 库，可帮助您将非结构化数据编码为嵌入。 |
| [LineaPy](https://github.com/LineaLabs/lineapy) |是否曾因清理又长又乱的 Jupyter 笔记本而感到沮丧？使用开源 Python 库 LineaPy，只需两行代码即可将混乱的开发代码转换为生产管道。 |
| [envd](https://github.com/tensorchord/envd) | 🏕️ 数据科学和 AI/ML 工程团队的机器学习开发环境 |
| [探索数据科学库](https://kandi.openweaver.com/explore/data-science) |一个搜索引擎🔎工具，用于发现和查找流行和新图书馆、顶级作者、趋势项目工具包、讨论、教程和学习资源的精选列表|
| [MLEM](https://github.com/iterative/mlem) | 🐶 按照 GitOps 原则版本和部署您的 ML 模型 |
| [MLflow](https://mlflow.org/) |用于在整个生命周期中管理 ML 模型的 MLOps 框架 |
| [cleanlab](https://github.com/cleanlab/cleanlab) |用于以数据为中心的 AI 并自动检测 ML 数据集中的各种问题的 Python 库 |
| [AutoGluon](https://github.com/awslabs/autogluon) | AutoML 可轻松对图像、文本、表格、时间序列和多模态数据进行准确预测 |
| [Arize AI](https://arize.com/) | Arize AI 社区层可观察性工具，用于监控生产中的机器学习模型以及数据质量和性能漂移等根本原因问题。 |
| [Aureo.io](https://aureo.io) | Aureo.io 是一个专注于构建人工智能的低代码平台。它为用户提供了创建管道、自动化并将其与人工智能模型集成的能力——所有这些都带有他们的基本数据。 |
| [ERD实验室](https://www.erdlab.io/) |为开发人员打造的免费基于云的实体关系图 (ERD) 工具。
| [Arize-Phoenix](https://docs.arize.com/phoenix) |笔记本中的 MLOps - 发现见解、揭示问题、监控和微调模型。 |
| [彗星](https://github.com/comet-ml/comet-examples) | MLOps 平台具有实验跟踪、模型生产管理、模型注册表和完整的数据沿袭，可支持从训练到生产的 ML 工作流程。 |
| [Opik](https://github.com/comet-ml/opik) |在您的开发和生产生命周期中评估、测试和交付 LLM 应用程序。 |
| [合成](https://synthical.com) |人工智能驱动的研究协作环境。查找相关论文、创建集合来管理参考书目并总结内容 - 全部集中在一个地方 |
| [teeplot](https://github.com/mmore500/teeplot) |自动组织数据可视化输出的工作流工具 |
| [Streamlit](https://github.com/streamlit/streamlit) |机器学习和数据科学项目的应用程序框架 |
| [Gradio](https://github.com/gradio-app/gradio) |围绕机器学习模型创建可定制的 UI 组件 |
| [权重和偏差](https://github.com/wandb/wandb) |实验跟踪、数据集版本控制和模型管理 |
| [DVC](https://github.com/iterative/dvc) |用于机器学习项目的开源版本控制系统 |
| [Optuna](https://github.com/optuna/optuna) |自动超参数优化软件框架|
| [Ray Tune](https://github.com/ray-project/ray) |可扩展的超参数调优库 |
| [Apache Airflow](https://github.com/apache/airflow) |以编程方式创作、安排和监控工作流程的平台 |
| [完美](https://github.com/PrefectHQ/prefect) |现代数据堆栈的工作流程管理系统|
| [Kedro](https://github.com/kedro-org/kedro) |用于创建可重复、可维护的数据科学代码的开源 Python 框架 |
| [汉密尔顿](https://github.com/dagworks-inc/hamilton) |用于创作和管理可靠数据转换的轻量级库 |
| [SHAP](https://github.com/slundberg/shap) |解释任何机器学习模型输出的博弈论方法 |
| [InterpretML](https://github.com/interpretml/interpret) | InterpretML 实现了可解释提升机 (EBM)，这是一种基于广义加性模型 (GAM) 的现代、完全可解释的机器学习模型。这个开源包还提供了 EBM、其他玻璃盒模型和黑盒解释的可视化工具 |
| [LIME](https://github.com/marcotcr/lime) |解释任何机器学习分类器的预测 |
| [flyte](https://github.com/flyteorg/flyte) |机器学习工作流程自动化平台 |
| [dbt](https://github.com/dbt-labs/dbt-core) |数据构建工具|
| [zasper](https://github.com/zasper-io/zasper) |数据科学的强大 IDE |
| [skrub](https://github.com/skrub-data/skrub/) |用于简化表格机器学习的预处理和特征工程的 Python 库 |
| [Codeflash](https://www.codeflash.ai/) |每次都交付速度极快的 Python 代码
| [拥抱脸](https://huggingface.co/) |用于共享 ML 模型、数据集以及在 NLP 和生成 AI 项目上进行协作的流行开放平台。 |
| [中文精英](https://github.com/anonym-g/Chinese-Elite) |一个开源项目，通过使用法学硕士解析公共数据来自动映射关系网络，并将其可视化为交互式图表。 |
| [Desbordante](https://github.com/desbordante/desbordante-core/) |一个开源数据分析器，专门专注于复杂模式的发现和验证，例如[数值关联规则](https://colab.research.google.com/github/Desbordante/desbordante-core/blob/main/examples/notebooks/Numerical_Association_Rules.ipynb)、[差分依赖项](https://colab.research.google.com/github/Desbordante/desbordante-core/blob/main/examples/notebooks/Differential_Dependency.ipynb)、[拒绝约束](https://colab.research.google.com/github/Desbordante/desbordante-core/blob/main/examples/notebooks/Denial_Constraints.ipynb)等等。 |
| [dna-claude-analysis](https://github.com/shmlkv/dna-claude-analysis) |带有 Python 脚本的个人基因组分析工具包可分析 17 个类别（健康风险、血统、药物基因组学、营养、心理学等）的原始 DNA 数据，并生成终端式单页 HTML 可视化。 |
| [RunMat](https://github.com/runmat-org/runmat) |具有自动 CPU/GPU 执行和融合数组内核的快速 MATLAB 语法运行时。 |
| [Turbostream](https://github.com/turboline-ai/turbostream) |用于试验自定义规则引擎和对实时数据流进行选择性 LLM 分析的终端 UI，无需担心流基础设施或背压。 |
| [WFGY 问题地图](https://github.com/onestardao/WFGY/blob/main/ProblemMap/README.md) | LLM 和 RAG 管道中 16 个重复出现问题的开源“故障图集”，其中包含可观察到的症状，并为数据科学团队提供了修复建议。 |
| [Deploybase](https://deploybase.ai/) |跟踪所有云和推理提供商的实时 GPU 和 LLM 定价。 |
| [DeepAnalyze](https://github.com/ruc-datalab/DeepAnalyze) |自主数据科学的代理法学硕士，可以在无需人工干预的情况下自主完成广泛的数据科学任务。 |
| [迪斯科](https://github.com/leap-laboratories/discovery-engine) |超人的探索性数据分析。通过 p 值、效应大小和文献引用，查找表格数据中法学硕士和手动探索遗漏的特征交互作用和子组效应。免费提供公共数据。 |
| [人工智能数据库](https://aifordatabase.com) |用自然语言与您的数据库聊天 — 无需 SQL。获取即时洞察、构建自刷新仪表板并根据数据库更改触发自动化工作流程。 |
| [加密泵扫描仪](https://github.com/stefanoviana/deepalpha) |具有 LSTM 神经网络的 AI 驱动的加密货币交易机器人（准确率 84.6%）。实时泵检测、前向验证模型、多交易所支持（Bybit、Binance、OKX、Gate.io）。开源。 |



## 文学与媒体
**[`^ 回到顶部 ^`](#awesome-data-science)**

本部分包括一些额外的阅读材料、可供观看的频道和可供收听的演讲。

### 书籍
**[`^ 回到顶部 ^`](#awesome-data-science)**

- [从头开始的数据科学：Python 的第一原理](https://www.amazon.com/Data-Science-Scratch-Principles-Python-dp-1492041130/dp/1492041130/ref=dp_ob_title_bk)
- [Python 人工智能 vue教程](https://www.tutorialspoint.com/artificial_intelligence_with_python/artificial_intelligence_with_python_tutorial.pdf)
- [从头开始机器学习](https://dafriedman97.github.io/mlbook/content/introduction.html)
- [概率机器学习：简介](https://probml.github.io/pml-book/book1.html)
- [How to Lead in Data Science](https://www.manning.com/books/how-to-lead-in-data-science) - 抢先体验
- [用数据对抗流失](https://www.manning.com/books/fighting-churn-with-data)
- [使用 Python 和 Dask 进行大规模数据科学](https://www.manning.com/books/data-science-with-python-and-dask)
- [Python 数据科学手册](https://jakevdp.github.io/PythonDataScienceHandbook/)
- [数据科学手册：25 位出色数据科学家的建议和见解](https://www.thedatasciencehandbook.com/)
- [像数据科学家一样思考](https://www.manning.com/books/think-like-a-data-scientist)
- [数据科学简介](https://www.manning.com/books/introducing-data-science)
- [R 实用数据科学](https://www.manning.com/books/practical-data-science-with-r)
- [日常数据科学](https://www.amazon.com/dp/B08TZ1MT3W/ref=cm_sw_r_cp_apa_fabc_a0ceGbWECF9A8) & [(更便宜的 PDF 版本)](https://gum.co/everydaydata)
- [Exploring Data Science](https://www.manning.com/books/exploring-data-science) - 免费电子书样本
- [Exploring the Data Jungle](https://www.manning.com/books/exploring-the-data-jungle) - 免费电子书样本
- [Python 中的经典计算机科学问题](https://www.manning.com/books/classic-computer-science-problems-in-python)
- [程序员数学](https://www.manning.com/books/math-for-programmers) 抢先体验
- [R in Action，第三版](https://www.manning.com/books/r-in-action-third-edition) 抢先体验
- [数据科学读书营](https://www.manning.com/books/data-science-bookcamp) 抢先体验
- [数据科学思维：下一次科学、技术和经济革命](https://www.springer.com/gp/book/9783319950914)
- [应用数据科学：数据驱动业务的经验教训](https://www.springer.com/gp/book/9783030118204)
- [数据科学手册](https://www.amazon.com/Data-Science-Handbook-Field-Cady/dp/1119092949)
- [Essential Natural Language Processing](https://www.manning.com/books/getting-started-with-natural-language-processing) - 抢先体验
- [Mining Massive Datasets](http://www.mmds.org/) - 通过在线课程理解的免费电子书
- [Pandas in Action](https://www.manning.com/books/pandas-in-action) - 抢先体验
- [遗传算法和遗传编程](https://www.taylorfrancis.com/books/9780429141973)
- [Advances in Evolutionary Algorithms](https://www.intechopen.com/books/advances_in_evolutionary_algorithms) - 免费下载
- [Genetic Programming: New Approaches and Successful Applications](https://www.intechopen.com/books/genetic-programming-new-approaches-and-successful-applications) - 免费下载
- [Evolutionary Algorithms](https://www.intechopen.com/books/evolutionary-algorithms) - 免费下载
- [Advances in Genetic Programming, Vol. 3](http://www0.cs.ucl.ac.uk/staff/W.Langdon/aigp3/) - 免费下载
- [Genetic Algorithms and Evolutionary Computation](https://www.talkorigins.org/faqs/genalg/genalg.html) - 免费下载
- [Convex Optimization](https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf) - Stephen Boyd 所著的凸优化书籍 - 免费下载
- [Data Analysis with Python and PySpark](https://www.manning.com/books/data-analysis-with-python-and-pyspark) - 抢先体验
- [R 数据科学](https://r4ds.had.co.nz/)
- [建立数据科学职业生涯](https://www.manning.com/books/build-a-career-in-data-science)
- [Machine Learning Bookcamp](https://mlbookcamp.com/) - 抢先体验
- [使用 Scikit-Learn、Keras 和 TensorFlow 进行机器学习实践，第二版](https://www.oreilly.com/library/view/hands-on-machine-learning/9781492032632/)
- [有效的数据科学基础设施](https://www.manning.com/books/effective-data-science-infrastructure)
- [实用 MLOps：如何为生产模型做好准备](https://valohai.com/mlops-ebook/)
- [使用 Python 和 PySpark 进行数据分析](https://www.manning.com/books/data-analysis-with-python-and-pyspark)
- [Regression, a Friendly guide](https://www.manning.com/books/regression-a-friendly-guide) - 抢先体验
- [流系统：大规模数据处理的内容、地点、时间和方式](https://www.oreilly.com/library/view/streaming-systems/9781491983867/)
- [命令行中的数据科学：用经过时间考验的工具面向未来](https://www.oreilly.com/library/view/data-science-at/9781491947845/)
- [使用 Python 进行机器学习 vue教程](https://www.tutorialspoint.com/machine_learning_with_python/machine_learning_with_python_tutorial.pdf)
- [深度学习](https://www.deeplearningbook.org/)
- [Designing Cloud Data Platforms](https://www.manning.com/books/designing-cloud-data-platforms) - 抢先体验
- [统计学习简介及其在 R 中的应用](https://www.statlearning.com/)
- [统计学习的要素：数据挖掘、推理和预测](https://hastie.su.domains/ElemStatLearn/)
- [使用 PyTorch 进行深度学习](https://www.simonandschuster.com/books/Deep-Learning-with-PyTorch/Eli-Stevens/9781617295263)
- [神经网络和深度学习](http://neuralnetworksanddeeplearning.com)
- [深度学习食谱](https://www.oreilly.com/library/view/deep-learning-cookbook/9781491995839/)
- [Python 机器学习简介](https://www.oreilly.com/library/view/introduction-to-machine/9781449369880/)
- [Artificial Intelligence: Foundations of Computational Agents, 2nd Edition](https://artint.info/index.html) - 免费 HTML 版本
- [The Quest for Artificial Intelligence: A History of Ideas and Achievements](https://ai.stanford.edu/~nilsson/QAI/qai.pdf) - 免费下载
- [Graph Algorithms for Data Science](https://www.manning.com/books/graph-algorithms-for-data-science) - 抢先体验
- [Data Mesh in Action](https://www.manning.com/books/data-mesh-in-action) - 抢先体验
- [Julia for Data Analysis](https://www.manning.com/books/julia-for-data-analysis) - 抢先体验
- [Casual Inference for Data Science](https://www.manning.com/books/julia-for-data-analysis) - 抢先体验
- [正则表达式谜题和 AI 编码助手](https://www.manning.com/books/regular-expression-puzzles-and-ai-coding-assistants) 作者：David Mertz
- [深入学习深度学习](https://d2l.ai/)
- [全民数据](https://www.manning.com/books/data-for-all)
- [Interpretable Machine Learning: A Guide for Making Black Box Models Explainable](https://christophm.github.io/interpretable-ml-book/) - 免费 GitHub 版本
- [数据科学基础](https://www.cs.cornell.edu/jeh/book.pdf) 免费下载
- [Comet for DataScience：增强您管理和优化数据科学项目生命周期的能力](https://www.amazon.com/Comet-Data-Science-Enhance-optimize/dp/1801814430)
- [Software Engineering for Data Scientists](https://www.manning.com/books/software-engineering-for-data-scientists) - 抢先体验
- [Julia for Data Science](https://www.manning.com/books/julia-for-data-science) - 抢先体验
- [An Introduction to Statistical Learning](https://www.statlearning.com/) - 下载页面
- [适合初学者的机器学习](https://www.amazon.in/Machine-Learning-Absolute-Beginners-Introduction-ebook/dp/B07335JNW1)
- [统一业务、数据和代码：使用 JSON 架构设计数据产品](https://learning.oreilly.com/library/view/unifying-business-data/9781098144999/)
- [格罗金贝叶斯](https://www.manning.com/books/grokking-bayes)
- [机器学习 Q 和 AI](https://sebastianraschka.com/books/ml-q-and-ai)
- [JavaScript for Data Science](https://third-bit.com/js4ds/) - 免费 html 页面
- [Angewandte Data Science](https://angewandtedatascience.de/) - 关于应用数据科学的德语书籍
- [人工智能背后的数学](https://www.freecodecamp.org/news/the-math-behind-artificial-intelligence-book)：一本免费的 FreeCodeCamp 书籍，从工程角度用简单的英语教授人工智能背后的数学。
- [执行数据科学](https://leanpub.com/eds)：管理数据科学团队和项目的高级指南。
- [现代统计学导论](https://leanpub.com/imstat)：一本现代、开放获取的统计学教科书，重点关注数据科学应用。
- [数据科学的艺术](https://bookdown.org/rdpeng/artofdatascience/)：专注于数据分析的“艺术”，如何提出正确的问题并完善它们。

#### 图书优惠（附属）

- [电子书促销 - 电子书最高可节省 45%！](https://www.manning.com/?utm_source=mikrobusiness&utm_medium=affiliate&utm_campaign=ebook_sale_8_8_22)

- [因果机器学习](https://www.manning.com/books/causal-machine-learning?utm_source=mikrobusiness&utm_medium=affiliate&utm_campaign=book_ness_causal_7_26_22&a_aid=mikrobusiness&a_bid=43a2198b
)
- [管理机器学习项目](https://www.manning.com/books/managing-machine-learning-projects?utm_source=mikrobusiness&utm_medium=affiliate&utm_campaign=book_thompson_managing_6_14_22)
- [数据科学的因果推理](https://www.manning.com/books/causal-inference-for-data-science?utm_source=mikrobusiness&utm_medium=affiliate&utm_campaign=book_ruizdevilla_causal_6_6_22)
- [全民数据](https://www.manning.com/books/data-for-all?utm_source=mikrobusiness&utm_medium=affiliate)

### 期刊、出版物和杂志
**[`^ 回到顶部 ^`](#awesome-data-science)**

- [ICML](https://icml.cc/2015/) - 国际机器学习会议
- [GECCO](https://gecco-2019.sigevo.org/index.html/HomePage) - 遗传与进化计算会议（GECCO）
- [epjdatascience](https://epjdatascience.springeropen.com/)
- [Journal of Data Science](https://jds-online.org/journal/JDS) - 致力于统计方法的广泛应用的国际期刊
- [大数据研究](https://www.journals.elsevier.com/big-data-research)
- [大数据杂志](https://journalofbigdata.springeropen.com/)
- [大数据与社会](https://journals.sagepub.com/home/bds)
- [数据科学杂志](https://www.jstage.jst.go.jp/browse/dsj)
- [datatau.com/news](https://www.datatau.com/news) - 与《黑客新闻》类似，但针对的是数据
- [数据科学 Trello 看板](https://trello.com/b/rbpEfMld/data-science)
- [Medium Data Science Topic](https://medium.com/tag/data-science) - 媒体上数据科学相关出版物
- [Towards Data Science Genetic Algorithm Topic](https://towardsdatascience.com/introduction-to-genetic-algorithms-including-example-code-e396e98d8bf3#:~:text=A%20genetic%20algorithm%20is%20a,offspring%20of%20the%20next%20generation.) - 数据科学的遗传算法相关出版物
- [Maxim AI](https://getmaxim.ai)。 AI 代理模拟、评估和可观察性工具。
- [8bitconcepts](https://8bitconcepts.com/) - 人工智能行业研究和分析，包含有关人工智能定价、企业采用和评估框架的论文。

### 时事通讯
**[`^ 回到顶部 ^`](#awesome-data-science)**

- [AI Weekly](https://aiweekly.co) - 来自行业领导者的精心策划的人工智能情报简报，涵盖模型、资金、政策和应用。自 2017 年以来每周 3 次，订阅者超过 4 万。
- [DataTalks.Club](https://datatalks.club)。关于数据相关事物的每周通讯。 [存档](https://us19.campaign-archive.com/home/?u=0d7822ab98152f5afc118c176&id=97178021aa)。
- [分析工程综述](https://roundup.getdbt.com/about)。关于数据科学的时事通讯。 [存档](https://roundup.getdbt.com/archive)。
- [Techpresso](https://dupple.com/techpresso)。免费每日时事通讯，涵盖人工智能、机器学习和技术领域最具影响力的发展。 [存档](https://dupple.com/techpresso)。
- [DiamantAI](https://diamantai.substack.com)。实用人工智能工程和生成式人工智能简单解释：RAG、代理和构建者的 LLM 应用模式。

### 邮件列表
**[`^ 回到顶部 ^`](#awesome-data-science)**
- [工作组 - 数字人文研究软件工程](https://www.listserv.dfn.de/sympa/info/ag-dhrse)。这是数字人文研究软件工程 (DH-RSE) 工作组的邮件列表。

### 博主
**[`^ 回到顶部 ^`](#awesome-data-science)**

- [Wes McKinney](https://wesmckinney.com/archives.html) - 韦斯·麦金尼档案馆。
- [Matthew Russell](https://miningthesocialweb.com/) - 挖掘社交网络。
- [Greg Reda](http://www.gregreda.com/) - 格雷格·雷达个人博客
- [Julia Evans](https://jvns.ca/) - 递归中心校友
- [Hakan Kardas](https://www.cse.unr.edu/~hkardes/) - 个人网页
- [Sean J. Taylor](https://seanjtaylor.com/) - 个人网页
- [Drew Conway](http://drewconway.com/) - 个人网页
- [Hilary Mason](https://hilarymason.com/) - 个人网页
- [Noah Iliinsky](http://complexdiagrams.com/) - 个人博客
- [Matt Harrison](https://hairysun.com/) - 个人博客
- [Vamshi Ambati](https://allthingsds.wordpress.com/) - 万物数据科学
- [Prash Chan](https://www.mdmgeek.com/) - 有关主数据管理及其相关话题的技术博客
- [Clare Corthell](http://datasciencemasters.org/) - 开源数据科学大师
- Peter Skomoroch 的 [Datawrangling](http://www.datawrangling.org)。机器学习、数据挖掘等
- [Quora Data Science](https://www.quora.com/topic/Data-Science) - 数据科学专家问答
- [Siah](https://openresearch.wordpress.com/) 伯克利分校博士生
- [Louis Dorard](https://www.ownml.co/blog/) 一位技术人员，对网络和大大小小的数据有着浓厚的兴趣
- [精通机器学习](https://machinelearningmastery.com/) 帮助专业程序员自信地应用机器学习算法来解决复杂问题。
- [Daniel Forsyth](https://www.danielforsyth.me/) - 个人博客
- [Data Science Weekly](https://www.datascienceweekly.org/) - 每周新闻博客
- [Revolution Analytics](https://blog.revolutionanalytics.com/) - 数据科学博客
- [R Bloggers](https://www.r-bloggers.com/) - R 博主
- [实用量化](https://practicalquant.blogspot.com/) 大数据
- [又一个数据博客](https://yet-another-data-blog.blogspot.com/)又一个数据博客
- [KD Nuggets](https://www.kdnuggets.com/) 数据挖掘、分析、大数据、数据、科学不是博客而是门户网站
- [Meta Brown](https://www.metabrown.com/blog/) - 个人博客
- [数据科学家](https://datascientists.com/) 正在构建数据科学家文化。
- [WhatSTheBigData](https://whatsthebigdata.com/) 是上述内容的部分、全部或更多内容，该博客探讨了它对信息技术、商业世界、政府机构和我们生活的影响。
- [Tevfik Kosar](https://magnus-notitia.blogspot.com/) - 马格努斯·诺蒂西亚
- [新数据科学家](https://newdatascientist.blogspot.com/) 社会科学家如何跳入大数据世界
- [Harvard Data Science](https://harvarddatascience.com/) - 统计计算与可视化的思考
- [Data Science 101](https://ryanswanstrom.com/datascience101/) - 学习成为一名数据科学家
- [Kaggle 过去的解决方案](https://www.chioka.in/kaggle-competition-solutions/)
- [DataScientistJourney](https://datascientistjourney.wordpress.com/category/data-science/)
- [纽约出租车可视化博客](https://chriswhong.github.io/nyctaxi/)
- [Data-Mania](https://www.data-mania.com/)
- [Data-Magnum](https://data-magnum.com/)
- [datascopeanalytics](https://datascopeanalytics.com/blog/)
- [数字化转型](https://tarrysingh.com/)
- [datascientistjourney](https://datascientistjourney.wordpress.com/category/data-science/)
- [Data Mania Blog](https://www.data-mania.com/blog/) - [文件抽屉](https://chris-said.io/) - Chris Said 的科学博客
- [埃米利奥·费拉拉的网页](http://www.emilio.ferrara.name/)
- [DataNews](https://datanews.tumblr.com/)
- [Reddit 文本挖掘](https://www.reddit.com/r/textdatamining/)
- [Periscopic](https://periscopic.com/#!/news)
- [希拉里帕克](https://hilaryparker.com/)
- [数据故事](https://datastori.es/)
- [数据科学实验室](https://datasciencelab.wordpress.com/)
- [的含义](https://www.kennybastani.com/)
- [数据王国的冒险](https://blog.smola.org)
- [Dataclysm](https://theblog.okcupid.com/)
- [FlowingData](https://flowingdata.com/) - 可视化和统计
- [计算风险](https://www.calculatedriskblog.com/)
- [奥莱利学习博客](https://www.oreilly.com/content/topics/oreilly-learning/)
- [Dominodatalab](https://blog.dominodatalab.com/)
- [i am trask](https://iamtrask.github.io/) - 机器学习工艺博客
- [Vademecum of Practical Data Science](https://datasciencevademecum.wordpress.com/) - 现实世界问题的数据驱动解决方案的手册和秘诀
- [Dataconomy](https://dataconomy.com/) - 关于新兴数据经济的博客
- [Springboard](https://www.springboard.com/blog/) - 为数据科学学习者提供资源的博客
- [Analytics Vidhya](https://www.analyticsvidhya.com/) - 一个关于数据科学和分析学习材料的成熟网站。
- [Occam's Razor](https://www.kaushik.net/avinash/) - 专注于网络分析。
- [Data School](https://www.dataschool.io/) - 适合初学者的数据科学教程！
- [Colah's Blog](https://colah.github.io) - 了解神经网络的博客！
- [Sebastian's Blog](https://ruder.io/#open) - NLP 和迁移学习博客！
- [Distill](https://distill.pub) - 致力于机器学习的清晰解释！
- [Chris Albon's Website](https://chrisalbon.com/) - 数据科学和人工智能笔记
- [Andrew Carr](https://andrewnc.github.io/blog/blog.html) - 使用深奥编程语言的数据科学
- [floydhub](https://blog.floydhub.com/introduction-to-genetic-algorithms/) - 进化算法博客
- [Jingles](https://jinglescode.github.io/) - 从学术论文中回顾并提取关键概念
- [nbshare](https://www.nbshare.io/notebooks/data-science/) - 数据科学笔记本
- [Loic Tetrel](https://ltetrel.github.io/) - 数据科学博客
- [Chip Huyen's Blog](https://huyenchip.com/blog/) - ML 工程、MLOps 以及 ML 在初创公司中的使用
- [Maria Khalusova](https://www.mariakhalusova.com/) - 数据科学博客
- [Aditi Rastogi](https://medium.com/@aditi2507rastogi) - ML、DL、数据科学博客
- [Santiago Basulto](https://medium.com/@santiagobasulto) - 使用 Python 进行数据科学
- [Akhil Soni](https://medium.com/@akhil0435) - 机器学习、深度学习和数据科学
- [Akhil Soni](https://akhilworld.hashnode.dev/) - 机器学习、深度学习和数据科学
- [Applied AI Blogs](https://www.appliedaicourse.com/blog/) - 关于人工智能、机器学习和数据科学概念及其实际应用的深入文章。
- [Scaler Blogs](https://www.scaler.com/blog/) - 有关软件开发、人工智能和技术职业发展的教育内容。
- [Mlu github](https://mlu-explain.github.io/) - Mlu 是亚马逊开发的，旨在帮助机器学习领域的人们，您可以通过实时图表从基础知识学习所有内容
- [Jan Oliver Rüdiger](https://notesjor.de/) - ML、DL 和数据科学 - 重点关注文本/数据挖掘

### 演讲
**[`^ 回到顶部 ^`](#awesome-data-science)**

- [如何成为一名数据科学家](https://www.slideshare.net/ryanorban/how-to-become-a-data-scientist)
- [数据科学导论](https://www.slideshare.net/NikoVuokko/introduction-to-data-science-25391618)
- [企业大数据的数据科学简介](https://www.slideshare.net/pacoid/intro-to-data-science-for-enterprise-big-data)
- [如何采访数据科学家](https://www.slideshare.net/dtunkelang/how-to-interview-a-data-scientist)
- [如何与统计学家共享数据](https://github.com/jtleek/datasharing)
- [数据科学伟大职业的科学](https://www.slideshare.net/katemats/the-science-of-a-great-career-in-data-science)
- [数据科学家做什么？](https://www.slideshare.net/datasciencelondon/big-data-sorry-data-science-what-does-a-data-scientist-do)
- [建立数据初创企业：快速、庞大且专注](https://www.slideshare.net/medriscoll/driscoll-strata-buildingdatastartups25may2011clean)
- [如何利用深度学习赢得数据科学竞赛](https://www.slideshare.net/0xdata/how-to-win-data-science-competitions-with-deep-learning)
- [全栈数据科学家](https://www.slideshare.net/AlexeyGrigorev/fullstack-data-scientist)

### 播客
**[`^ 回到顶部 ^`](#awesome-data-science)**

- [家庭人工智能](https://podcasts.apple.com/us/podcast/data-science-at-home/id1069871378)
- [今日人工智能](https://www.cognilytica.com/aitoday/)
- [对抗性学习](https://adversariallearning.com/)
- [Chai time 数据科学](https://www.youtube.com/playlist?list=PLLvvXm0q8zUbiNdoIazGzlENMXvZ9bd3x)
- [思想链](https://www.chainofthought.show/)
- [数据工程播客](https://www.dataengineeringpodcast.com/)
- [家庭数据科学](https://datascienceathome.com/)
- [数据科学混合器](https://community.alteryx.com/t5/Data-Science-Mixer/bg-p/mixer)
- [数据怀疑论者](https://dataskeptic.com/)
- [数据故事](https://datastori.es/)
- [Datacast](https://jameskle.com/writes/category/Datacast)
- [DataFramed](https://www.datacamp.com/community/podcast)
- [DataTalks.Club](https://anchor.fm/datatalksclub)
- [梯度下降](https://wandb.ai/fully-connected/gradient-descent)
- [学习机 101](https://www.learningmachines101.com/)
- [Let’s Data（巴西）](https://www.youtube.com/playlist?list=PLn_z5E4dh_Lj5eogejMxfOiNX3nOhmhmM)
- [线性离题](https://lineardigressions.com/)
- [不那么标准差](https://nssdeviations.com/)
- [奥莱利数据秀播客](https://www.oreilly.com/radar/topics/oreilly-data-show-podcast/)
- [偏导数](http://partiallyderivative.com/)
- [Superdatascience](https://www.superdatascience.com/podcast/)
- [数据工程展](https://www.dataengineeringshow.com/)
- [激进人工智能播客](https://www.radicalai.org/)
- [有什么意义](https://fivethirtyeight.com/tag/whats-the-point/)
- [分析工程播客](https://roundup.getdbt.com/s/the-analytics-engineering-podcast)

### YouTube 视频和频道
**[`^ 回到顶部 ^`](#awesome-data-science)**

- [什么是机器学习？](https://www.youtube.com/watch?v=WXHM_i-fgGo)
- [吴恩达：深度学习、自学学习和无监督特征学习](https://www.youtube.com/watch?v=n1ViNeWhC24)
- [Data36 - Tomi Mester 的初学者数据科学](https://www.youtube.com/c/TomiMesterData36comDataScienceForBeginners)
- [深度学习：来自大数据的智能](https://www.youtube.com/watch?v=czLI3oLDe8M)
- [专访谷歌人工智能和深度学习“教父”Geoffrey Hinton](https://www.youtube.com/watch?v=1Wp3IIpssEc)
- [Python 深度学习简介](https://www.youtube.com/watch?v=S75EdAcXHKk)
- [什么是机器学习，它是如何工作的？](https://www.youtube.com/watch?v=elojMnjn4kk)
- [CampusX](https://www.youtube.com/@campusx-official)
- [Data School](https://www.youtube.com/channel/UCnVzApLJE2ljPZSeQylSEyg) - 数据科学教育
- [适合新手的神经网络作者：Melanie Warrick（2015 年 5 月）](https://www.youtube.com/watch?v=Cu6A96TUy_o)
- [Hugo Larochelle 的神经网络视频系列](https://www.youtube.com/playlist?list=PL6Xpj9I5qXYEcOhn7TqghAJ6NAPrNmUBH)
- [谷歌 DeepMind 联合创始人 Shane Legg - 机器超级智能](https://www.youtube.com/watch?v=evNCyRL3DOU)
- [数据科学入门](https://www.youtube.com/watch?v=cHzvYxBN9Ls&list=PLPqVjP3T4RIRsjaW07zoGzH-Z4dBACpxY)
- [数据科学与遗传算法](https://www.youtube.com/watch?v=lpD38NxTOnk)
- [数据科学初学者](https://www.youtube.com/playlist?list=PL2zq7klxX5ATMsmyRazei7ZXkP1GHt-vs)
- [DataTalks.Club](https://www.youtube.com/channel/UCDvErgK0j5ur3aLgn6U-LqQ)
- [轻度过度拟合 - 有关中级 ML/DL 主题的教程](https://www.youtube.com/channel/UCYBSjwkGTK06NnDnFsOcR7g)
- [mlops.community - 关于生产 ML 的行业专家访谈](https://www.youtube.com/channel/UCYBSjwkGTK06NnDnFsOcR7g)
- [ML Street Talk - 毫不掩饰技术性和非商业性，因此您不会听到烦人的推销。](https://www.youtube.com/c/machinelearningstreettalk)
- [3Blue1Brown 的神经网络 ](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi)
- [Sentdex 从头开始的神经网络](https://www.youtube.com/playlist?list=PLQVvvaa0QuDcjD5BAw2DxE6OF2tius3V3)
- [曼宁出版社 YouTube 频道](https://www.youtube.com/c/ManningPublications/featured)
- [询问 Chong 博士：如何领导数据科学 - 第 1 部分](https://youtu.be/JYuQZii5o58)
- [询问 Chong 博士：如何领导数据科学 - 第 2 部分](https://youtu.be/SzqIXV-O-ko)
- [询问 Chong 博士：如何领导数据科学 - 第 3 部分](https://youtu.be/Ogwm7k_smTA)
- [询问 Chong 博士：如何领导数据科学 - 第 4 部分](https://youtu.be/a9usjdzTxTU)
- [询问 Chong 博士：如何领导数据科学 - 第 5 部分](https://youtu.be/MYdQq-F3Ws0)
- [询问 Chong 博士：如何领导数据科学 - 第 6 部分](https://youtu.be/LOOt4OVC3hY)
- [回归模型：应用简单的泊松回归](https://www.youtube.com/watch?v=9Hk8K8jhiOo)
- [深度学习架构](https://www.youtube.com/playlist?list=PLv8Cp2NvcY8DpVcsmOT71kymgMmcr59Mf)
- [时间序列建模与分析](https://www.youtube.com/playlist?list=PL3N9eeOlCrP5cK0QRQxeJd6GrQvhAtpBK)
- [Serrano.Academy](https://www.youtube.com/@SerranoAcademy)
- [端到端数据科学播放列表](https://www.youtube.com/watch?v=S_F_c9e2bz4&list=PLZoTAELRMXVPS-dOaVbAux22vzqdgoGhG)
- [数据科学简介 - Linkedin](https://www.linkedin.com/learning/introduction-to-data-science-22668235/beginning-your-data-science-exploration?u=42458916)

## 社交
**[`^ 回到顶部 ^`](#awesome-data-science)**

以下是一些社交媒体链接。与其他数据科学家联系！

- [脸书帐户](#facebook-accounts)
- [推特账户](#twitter-accounts)
- [电报频道](#telegram-channels)
- [松弛社区](#slack-communities)
- [GitHub 群组](#github-groups)
- [数据科学竞赛](#data-science-competitions)


### 脸书帐户
**[`^ 回到顶部 ^`](#awesome-data-science)**

- [Data](https://www.facebook.com/data)
- [大数据科学家](https://www.facebook.com/Bigdatascientist)
- [数据科学日](https://www.facebook.com/datascienceday/)
- [数据科学学院](https://www.facebook.com/nycdatascience)
- [Facebook 数据科学页面](https://www.facebook.com/pages/Data-science/431299473579193?ref=br_rs)
- [伦敦数据科学](https://www.facebook.com/pages/Data-Science-London/226174337471513)
- [数据科学技术与公司](https://www.facebook.com/DataScienceTechnologyCorporation?ref=br_rs)
- [数据科学 - 封闭组](https://www.facebook.com/groups/1394010454157077/?ref=br_rs)
- [数据科学中心](https://www.facebook.com/centerdatasciences?ref=br_rs)
- [大数据 hadoop NOSQL Hive Hbase](https://www.facebook.com/groups/bigdatahadoop/)
- [分析、数据挖掘、预测建模、人工智能](https://www.facebook.com/groups/data.analytics/)
- [使用 R 进行大数据分析](https://www.facebook.com/groups/434352233255448/)
- [使用 R 和 Hadoop 进行大数据分析](https://www.facebook.com/groups/rhadoop/)
- [大数据学习](https://www.facebook.com/groups/bigdatalearnings/)
- [大数据、数据科学、数据挖掘与统计](https://www.facebook.com/groups/bigdatastatistics/)
- [大数据/Hadoop 专家](https://www.facebook.com/groups/BigDataExpert/)
- [数据挖掘/机器学习/人工智能](https://www.facebook.com/groups/machinelearningforum/)
- [数据挖掘/大数据 - 社交网络分析](https://www.facebook.com/groups/dataminingsocialnetworks/)
- [实用数据科学学院](https://www.facebook.com/datasciencevademecum)
- [伊斯坦布尔 Veri Bilimi](https://www.facebook.com/groups/veribilimiistanbul/)
- [数据科学博客](https://www.facebook.com/theDataScienceBlog/)


### 推特账户
**[`^ 回到顶部 ^`](#awesome-data-science)**

|推特 |描述 |
| --- | --- |
| [大数据组合](https://twitter.com/BigDataCombine) |数据科学家寻求将其模型作为交易策略货币化的快速现场试用
|大数据狂热| Data Viz Wiz，数据记者、Growth Hacker、Data Science for Dummies (2015) 作者
| [大数据科学](https://twitter.com/analyticbridge) |大数据、数据科学、预测建模、业务分析、Hadoop、决策和运筹学。 |
|查理·格林巴克 | @ExploreAltamira 数据科学总监 |
| [克里斯·赛义德](https://twitter.com/Chris_Said) | Twitter 的数据科学家 |
| [克莱尔·科塞尔](https://twitter.com/clarecorthell) |开发、设计、数据科学@mattermark #hackerei |
| [DADI 查尔斯-阿布纳](https://twitter.com/DadiCharles) | #datascientist @Ekimetrics。 ，#machinelearning #dataviz #DynamicCharts #Hadoop #R #Python #NLP #Bitcoin #dataenthousiast |
| [数据科学中心](https://twitter.com/DataScienceCtrl) |数据科学中心是业界为大数据从业者提供的单一资源。 |
| [伦敦数据科学](https://twitter.com/ds_ldn) |数据科学。大数据。数据黑客。数据迷。数据初创公司。开放数据|
| [数据科学 Renee](https://twitter.com/BecomingDataSci) |记录我从攻读工程硕士学位的 SQL 数据分析师到数据科学家的历程 |
| [数据科学报告](https://twitter.com/TedOBrien93) |使命是帮助指导和推进数据科学与分析领域的职业生涯
| [数据科学技巧](https://twitter.com/datasciencetips) |为世界各地的数据科学家提供的提示和技巧！ #数据科学#bigdata |
| [数据维扎德](https://twitter.com/DataVisualizati) | DataViz、安全、军事 |
| [DataScienceX](https://twitter.com/DataScienceX) |  |
|深度学习4j | |
| [DJ 帕蒂尔](https://twitter.com/dpatil) |白宫数据主管、RelateIQ 副总裁。 |
| [Domino 数据实验室](https://twitter.com/DominoDataLab) | |
| [德鲁·康威](https://twitter.com/drewconway) |数据呆子、黑客、冲突学生。 |
|埃米利奥·费拉拉 | #网络、#机器学习和#数据科学。我在#社交媒体上工作。 @IndianaUniv 博士后 |
| [艾琳·巴托洛](https://twitter.com/erinbartolo) |与 #BigData 一起运行——对其炒作感到又爱又恨。 @iSchoolSU #DataScience 项目经理。 |
| [格雷格·雷达](https://twitter.com/gjreda) |在@_GrubHub_ 工作关于数据和pandas |
| [格雷戈里·皮亚特斯基](https://twitter.com/kdnuggets) |  KDnuggets 总裁，分析/大数据/数据挖掘/数据科学专家，KDD & SIGKDD 联合创始人，曾任 2 家初创公司首席科学家，兼职哲学家。 |
| [哈德利威克姆](https://twitter.com/hadleywickham) |  RStudio 首席科学家，奥克兰大学、斯坦福大学和莱斯大学统计学兼职教授。 |
| [哈坎·卡达斯](https://twitter.com/hakan_kardes) |数据科学家 |
| [希拉里·梅森](https://twitter.com/hmason) | @accel 的常驻数据科学家。 |
| [杰夫·哈默巴赫](https://twitter.com/hackingdata) |转发有关数据科学的推文 |
| [约翰·迈尔斯·怀特](https://twitter.com/johnmyleswhite) | Facebook 科学家和 Julia 开发人员。 《黑客机器学习》和《网站优化强盗算法》的作者。推文仅反映我的观点。 |
| [胡安·米格尔·拉维斯塔](https://twitter.com/BDataScientist) |微软数据科学团队首席数据科学家 |
| [朱莉娅·埃文斯](https://twitter.com/b0rk) |黑客 - Pandas - 数据分析 |
| [肯尼思·库基尔](https://twitter.com/kncukier) | 《经济学人》的数据编辑和《大数据》(http://www.big-data-book.com/) 的合著者。 |
|凯文·达文波特 | https://www.meetup.com/San-Diego-Data-Science-R-Users-Group/ 的组织者 |
| [凯文·马卡姆](https://twitter.com/justmarkham) |数据科学导师、【数据学院】(https://www.dataschool.io/)创始人 |
| [金·里斯](https://twitter.com/krees) |交互式数据可视化和工具。数据闲逛者。 |
| [柯克·博恩](https://twitter.com/KirkDBorne) |数据科学家、天体物理学博士、#BigData 顶级影响者。 |
|琳达·雷伯|数据讲故事，可视化。 |
| [路易斯·雷](https://twitter.com/lmrei) |博士生。编程、移动、网络。人工智能、智能机器人、机器学习、数据挖掘、自然语言处理、数据科学。 |
|马克·史蒂文森 | Salt (@SaltJobs) 数据分析招聘专家
| [马特·哈里森](https://twitter.com/__mharrison__) |全栈 Python 人、作者、讲师、目前担任数据科学家的观点。偶尔做父亲、做丈夫、做有机园艺。 |
| [马修·拉塞尔](https://twitter.com/ptwobrussell) |挖掘社交网络。 |
| [Mert Nuhoğlu](https://twitter.com/mertnuhoglu) | BizQualify 数据科学家、开发人员 |
| [莫妮卡·罗加蒂](https://twitter.com/mrogati) |数据@Jawbone。在 LinkedIn 将数据转化为故事和产品。文本挖掘、应用机器学习、推荐系统。前游戏玩家、前机器编码员；命名者。 |
| [诺亚·伊林斯基](https://twitter.com/noahi) |可视化和交互设计师。实用的自行车手。视觉书籍作者：https://www.oreilly.com/pub/au/4419 |
| [保罗·米勒](https://twitter.com/PaulMiller) |云计算/大数据/开放数据分析师和顾问。作家、演讲者和主持人。 Gigaom 研究分析师。 |
| [彼得·斯科莫罗奇](https://twitter.com/peteskomoroch) |创建智能系统来自动执行任务并改进决策。企业家、前首席数据科学家@LinkedIn。机器学习、ProductRei、网络 |
| [普拉什·陈](https://twitter.com/MDMGeek) | IBM 解决方案架构师、主数据管理、数据质量和数据治理博​​客。数据科学、Hadoop、大数据和云。 |
| [Quora 数据科学](https://twitter.com/q_datascience) | Quora 的数据科学主题 |
| [R-Bloggers](https://twitter.com/Rbloggers) |在 R 博客圈、数据科学会议和（！）数据科学家的空缺职位上发表推文。 |
| [兰德印地语](https://twitter.com/randhindi) |  |
| [兰迪·奥尔森](https://twitter.com/randal_olson) |研究人工智能的计算机科学家。数据修补匠。 @DataIsBeautiful 的社区领导者。 #开放科学倡导者。 |
| [雷杰普·埃罗尔](https://twitter.com/EROLRecep) |数据科学极客@UALR |
| [瑞安·欧尔班](https://twitter.com/ryanorban) |数据科学家、基因折纸师、硬件爱好者 |
| [肖恩·J·泰勒](https://twitter.com/seanjtaylor) |社会科学家。黑客。 Facebook 数据科学团队。关键词：实验、因果推理、统计学、机器学习、经济学。 |
| [西尔维娅·K·斯皮瓦](https://twitter.com/silviakspiva) |思科的#DataScience |
| [严厉 B. 古普塔](https://twitter.com/harshbg) | BBVA Compass 数据科学家 |
| [斯宾塞·尼尔森](https://twitter.com/spenczar_n) |数据迷 |
| [塔尔哈·奥兹](https://twitter.com/tozCSS) |喜欢 ABM、SNA、DM、ML、NLP、HI、Python、Java。 Kaggler/数据科学家 | 最高百分位
| [Tasos Skarlatidis](https://twitter.com/anskarl) |复杂事件处理、大数据、人工智能和机器学习。热衷于编程和开源。 |
| [特里·蒂姆科](https://twitter.com/Terry_Timko) |信息政府；大数据；数据即服务；数据科学；开放、社交和商业数据融合 |
| [托尼·贝尔](https://twitter.com/TonyBaer) | Ovum 的 IT 分析师涵盖大数据和数据管理以及一些系统工程。
| [托尼·奥赫达](https://twitter.com/tonyojeda3) |数据科学家、作家、企业家。联合创始人@DataCommunityDC。创始人@DistrictDataLab。 #DataScience #BigData #DataDC |
| [Vamshi Ambati](https://twitter.com/vambati) |数据科学@PayPal。 #NLP，#机器学习；卡内基梅隆大学校友博士（博客：https://allthingsds.wordpress.com）|
| [韦斯·麦金尼](https://twitter.com/wesmckinn) | Pandas（Python 数据分析库）。 |
| [WileyEd](https://twitter.com/WileyEd) |高级经理 - @Seagate 大数据分析 @McKinsey Alum #BigData + #Analytics Evangelist #Hadoop、#Cloud、#Digital 和 #R 爱好者 |
| [WNYC 数据新闻团队](https://twitter.com/datanews) | @WNYC 的数据新闻团队。实践数据驱动的新闻报道，使其可视化并展示我们的工作。 |
| [阿列克谢·格里戈列夫](https://twitter.com/Al_Grigor) |数据科学作者 |
| [伊尔克·阿尔斯兰](https://twitter.com/ilkerarslan_35) |数据科学作者。主要分享有关 Julia 编程的内容 |
| [不可避免](https://twitter.com/WeAreInevitable) |总部位于英国英格兰的人工智能和数据科学初创公司 |
| [Jan Oliver Rüdiger](https://x.com/notesJOR) | ML、DL 和数据科学 - 重点关注文本/数据挖掘 |

### 电报频道
**[`^ 回到顶部 ^`](#awesome-data-science)**

- [Open Data Science](https://t.me/opendatascience) - 第一个 Telegram 数据科学频道。涵盖与数据科学相关的所有技术和流行人员：人工智能、大数据、机器学习、统计学、普通数学及其应用。
- [Loss function porn](https://t.me/loss_function_porn) - 关于 DS/ML 主题的精彩帖子，带有视频或图形可视化。
- [Machinelearning](https://t.me/ai_machinelearning_big_data) - 每日机器学习新闻。


### 松弛社区
[顶部]（#awesome-data-science）

- [DataTalks.Club](https://datatalks.club)

### GitHub 群组
- [伯克利数据科学研究所](https://github.com/BIDS)

### 数据科学竞赛

一些数据挖掘竞赛平台

- [Kaggle](https://www.kaggle.com/)
- [DrivenData](https://www.drivendata.org/)
- [分析维迪亚](https://datahack.analyticsvidhya.com/)
- [InnoCentive](https://www.innocentive.com/)
- [Microprediction](https://www.microprediction.com/python-1)

## 乐趣

- [Infographic](#infographics)
- [Datasets](#datasets)
- [Comics](#comics)


### 信息图表
**[`^ 回到顶部 ^`](#awesome-data-science)**

|预览 |描述 |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [<img src="https://i.imgur.com/0OoLaa5.png" width="150" />](https://i.imgur.com/0OoLaa5.png) | [数据科学家与数据工程师的主要区别](https://searchbusinessanalytics.techtarget.com/feature/Key-differences-of-a-data-scientist-vs-data-engineer) |
| [<img src =“https://cloud.githubusercontent.com/assets/182906/19517857/604f88d8-960c-11e6-97d6-16c9738cb824.png”宽度=“150” />](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/DataScienceEightSteps_Full.png) | [DataCamp](https://www.datacamp.com) [(img)](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/DataScienceEightSteps_Full.png) 提供的《8 个步骤成为数据科学家》的视觉指南 |
| [<img src="https://i.imgur.com/W2t2Roz.png" width="150" />](https://i.imgur.com/FxsL3b8.png) |所需技能的思维导图 ([img](https://i.imgur.com/FxsL3b8.png)) |
| [<img src="https://i.imgur.com/rb9ruaa.png" width="150" />](https://nirvacana.com/thoughts/wp-content/uploads/2013/07/RoadToDataScientist1.png) | Swami Chandrasekaran 制作了一个[地铁地图课程](http://nirvacana.com/thoughts/2013/07/08/becoming-a-data-scientist/)。                                                                                                                                            |
| [<img src="https://i.imgur.com/XBgKF2l.png" width="150" />](https://i.imgur.com/4ZBBvb0.png) |通过 [@kzawadz](https://twitter.com/kzawadz) 通过 [twitter](https://twitter.com/MktngDistillery/status/538671811991715840) |
| [<img src="https://i.imgur.com/l9ZGtal.jpg" width="150" />](https://i.imgur.com/xLY3XZn.jpg) |作者：[数据科学中心](https://www.datasciencecentral.com/) |
| [<img src="https://i.imgur.com/TWkB4X6.png" width="150" />](https://i.imgur.com/0TydZ4M.png) |数据科学大战：R 与 Python |
| [<img src="https://i.imgur.com/gtTlW5I.png" width="150" />](https://i.imgur.com/HnRwlce.png) |如何选择统计或机器学习技术|
| [<img src =“https://scikit-learn.org/1.5/_downloads/b82bf6cd7438a351f19fac60fbc0d927/ml_map.svg”宽度=“150” />](https://scikit-learn.org/1.5/_downloads/b82bf6cd7438a351f19fac60fbc0d927/ml_map.svg) | [选择正确的估计器](https://scikit-learn.org/1.5/machine_learning_map.html#choosing-the-right-estimator) |
| [<img src="https://i.imgur.com/3JSyUq1.png" width="150" />](https://i.imgur.com/uEqMwZa.png) |数据科学行业：谁做什么？
| [<img src="https://i.imgur.com/DQqFwwy.png" width="150" />](https://i.imgur.com/RsHqY84.png) |数据科学~~维恩~~欧拉图|
| [<img src =“https://www.springboard.com/blog/wp-content/uploads/2016/03/20160324_springboard_vennDiagram.png”宽度=“150”高度=“150” />](https://www.springboard.com/blog/wp-content/uploads/2016/03/20160324_springboard_vennDiagram.png) | [Springboard](https://www.springboard.com) 的不同数据科学技能和角色 |
| [<img src="https://data-literacy.geckoboard.com/assets/img/data-fallacies-to-avoid-preview.jpg" width="150" alt="要避免的数据谬误" />](https://data-literacy.geckoboard.com/poster/) |一种简单而友好的方式来教授非数据科学家/非统计学家同事[如何避免数据错误](https://data-literacy.geckoboard.com/poster/)。来自 Geckoboard 的[数据素养课程](https://data-literacy.geckoboard.com/)。 |

### 数据集
**[`^ 回到顶部 ^`](#awesome-data-science)**

- [学术洪流](https://academictorrents.com/)
- [ADS-B Exchange](https://www.adsbexchange.com/data-samples/) - 飞机和广播自动相关监视 (ADS-B) 源的特定数据集。
- [AI Displacement Tracker](https://github.com/noahaust2/ai-displacement-tracker) - 结构化数据集跟踪 92 起由人工智能引发的劳动力减少事件，影响了 12 个国家和 11 个部门的 453,748 名工人。 JSON 和 CSV 格式。 CC-BY-4.0 许可。
- [Packrift Packaging Optimization Benchmark Corpus](https://packrift.github.io/packaging-optimization-benchmark-corpus/) - 公共包装产品数据集由 1,000 个精确规格的 SKU 记录生成，并提供可下载的 CSV 和 JSON 文件，用于电子商务履行和仓库分析。
- [hadoopilluminated.com](https://hadoopilluminated.com/hadoop_illuminated/Public_Bigdata_Sets.html)
- [data.gov](https://catalog.data.gov/dataset) - 美国政府开放数据之家
- [美国人口普查局](https://www.census.gov/)
- [enigma.com](https://enigma.com/) - 畅游公共数据世界 - 快速搜索和分析政府、公司和组织发布的数十亿条公共记录。
- [datahub.io](https://datahub.io/)
- [aws.amazon.com/datasets](https://aws.amazon.com/datasets/)
- [datacite.org](https://datacite.org/)
- [欧洲数据官方门户](https://data.europa.eu/en)
- [NASDAQ:DATA](https://data.nasdaq.com/) - 纳斯达克数据链接 金融、经济和另类数据集的主要来源。
- [Congressional Stock Brain](https://congressionalstockbrain.com) - 免费的人工智能工具，可根据重要性对美国国会股票法案的交易披露进行评分。来自 537 名立法者公开交易文件的机器评分信号。
- [figshare.com](https://figshare.com/)
- [GeoLite 旧版可下载数据库](https://dev.maxmind.com/geoip)
- [拥抱人脸数据集](https://huggingface.co/datasets)
- [Japan Neighborhoods](https://japanneighborhoods.com) - 东京 5,078 个社区 × 7 年犯罪统计数据的英文数据集（36,222 条记录，2018-2024 年），源自东京都警察公开数据。包括交互式犯罪地图、安全分级和生活成本指数。 CC BY 许可。
- [The Quiet-Broke Index](https://jeevesagency.github.io/quiet-broke-index/) - 30 地铁综合排名，显示 40 万美元的家庭收入中有多少用于住房、税收、儿童保育、医疗保健和交通。开放方法，免费，没有电子邮件门。
- [Crime Brasil](https://crimebrasil.com.br) - 巴西犯罪统计开放数据平台。南里奥格兰德州的社区级别（2022-2025 年，79,024 个社区发生 299 万起事件）、MG 和 RJ 的市政府级别，以及国家 PRF 高速公路和 DATASUS 人际暴力数据。免费 REST API、CSV/Parquet、每日更新、CC BY 4.0。
- [US Truck-Involved Fatal Crashes (FARS) 2018-2024](https://doi.org/10.5281/zenodo.20487070) - NHTSA 死亡分析报告系统的过滤子集，涵盖 2018 年至 2024 年美国所有 50 个州涉及中型和重型商用卡车的 33,898 起致命事故。包括比较 19 个城市的交互式 [Vision Zero 报告卡](https://accidentlawyerreview.com/research/vision-zero-report-card/)、[GitHub](https://github.com/MarvinBregiosa/vision-zero-fars) 上的可复制 Python 管道以及 HuggingFace 镜像。永久 DOI，CC BY 4.0。
- [Quora 的大数据集答案](https://www.quora.com/Where-can-I-find-large-datasets-open-to-the-public)
- [公共大数据集](https://hadoopilluminated.com/hadoop_illuminated/Public_Bigdata_Sets.html)
- [Kaggle 数据集](https://www.kaggle.com/datasets)
- [人类遗传变异的深度目录](https://www.internationalgenome.org/data)
- [由社区管理的知名人物、地点和事物的数据库](https://developers.google.com/freebase/)
- [谷歌公开数据](https://www.google.com/publicdata/directory)
- [世界银行数据](https://data.worldbank.org/)
- [纽约市出租车数据](https://chriswhong.github.io/nyctaxi/)
- [费城开放数据](https://www.opendataphilly.org/) 将费城的人们与数据联系起来
- [grouplens.org](https://grouplens.org/datasets/) 示例电影（带评级）、书籍和 wiki 数据集
- [UC Irvine Machine Learning Repository](https://archive.ics.uci.edu/ml/) - 包含有利于机器学习的数据集
- [研究质量数据集](https://web.archive.org/web/20150320022752/https://bitly.com/bundles/hmason/1) 作者：[Hilary Mason](https://web.archive.org/web/20150501033715/https://bitly.com/u/hmason/bundles)
- [国家环境信息中心](https://www.ncei.noaa.gov/)
- [ClimateData.us](https://www.climatedata.us/)（相关：[美国气候复原力工具包](https://toolkit.climate.gov/)）
- [r/datasets](https://www.reddit.com/r/datasets/)
- [MapLight](https://www.maplight.org/data-series) - 免费提供各种数据供公众免费使用。单击下面的数据集以了解更多信息
- [GHDx](https://ghdx.healthdata.org/) - 健康指标和评估研究所 - 来自世界各地的健康和人口数据集目录，包括 IHME 结果
- [圣路易斯联储经济数据 - FRED](https://fred.stlouisfed.org/)
- [新西兰经济研究所 – Data1850](https://data1850.nz/)
- [开放数据源](https://github.com/datasciencemasters/data)
- [联合国儿童基金会数据](https://data.unicef.org/)
- [undata](https://data.un.org/)
- [NASA 社会经济数据和应用中心 - SEDAC](https://earthdata.nasa.gov/centers/sedac-daac)
- [GDELT 项目](https://www.gdeltproject.org/)
- [瑞典，统计](https://www.scb.se/en/)
- [StackExchange Data Explorer](https://data.stackexchange.com) - 一个开源工具，用于对 Stack Exchange 网络中的公共数据运行任意查询。
- [旧金山政府开放数据](https://datasf.org/opendata/)
- [IBM 资产数据集](https://developer.ibm.com/exchanges/data/)
- [开放数据索引](http://index.okfn.org/)
- [公共 Git 档案](https://github.com/src-d/datasets/tree/master/PublicGitArchive)
- [GHTorrent](https://ghtorrent.org/)
- [微软研究院开放数据](https://msropendata.com/)
- [印度开放政府数据平台](https://data.gov.in/)
- [Google 数据集搜索（测试版）](https://datasetsearch.research.google.com/)
- [NAYN.CO 土耳其新闻类别](https://github.com/naynco/nayn.data)
- [Covid-19](https://github.com/datasets/covid-19)
- [Covid-19 谷歌](https://github.com/google-research/open-covid-19-data)
- [安然电子邮件数据集](https://www.cs.cmu.edu/~./enron/)
- [5000 张衣服图片](https://github.com/alexeygrigorev/clothing-dataset)
- [IBB 开放门户](https://data.ibb.gov.tr/en/)
- [人道主义数据交换](https://data.humdata.org/)
- [250k+ Job Postings](https://aws.amazon.com/marketplace/pp/prodview-p2554p3tczbes) - 卢森堡从 2020 年至今的历史招聘信息的不断扩展的数据集。免费提供 AWS Data Exchange 上托管的超过 25 万个职位发布。
- [FinancialData.Net](https://financialdata.net/documentation) - 财务数据集（股票市场数据、财务报表、可持续性数据等）。
- [Google Dataset Search](https://datasetsearch.research.google.com/) - 在网络上查找数据集。
- [notesjor corpus-collection](https://notes.jan-oliver-ruediger.de/korpora/) - 免费语料库（超过 60 亿个标记）主要是德语（历史上和当代德语）。
- [CLARIN-Repository](https://lindat.mff.cuni.cz/repository/home) - CLARIN 是欧洲科学数据集存储库。
- [GBIF](https://www.gbif.org/) - 全球生物多样性信息设施：2.4B+ 物种出现记录。用于生态建模和机器学习研究的免费开放 API。
- [FAOSTAT](https://www.fao.org/faostat/en/) - 联合国粮农组织有关 245 个以上国家的粮食生产、贸易、土地利用和排放的统计数据。免费API和批量下载。
- [FirstData](https://github.com/MLT-OSS/FirstData) - 全球最全面的权威数据源知识库。来自政府、国际组织和研究机构的 210 多个精选资源。 AI 代理的 MCP 集成。麻省理工学院许可。
- [latamdata-py](https://github.com/juanmoisesd/latamdata-py) - Python 包，用于单行访问来自拉丁美洲的 38 个开放研究数据集（健康、神经科学、心理健康、经济学）。 pip 安装 latamdata-py。
- [ZipCheckup](https://github.com/artakulov/us-water-quality-data) - 42,000 多个美国邮政编码的免费邮政级环境安全数据：水质、空气质量、PFAS 污染、氡气、铅、洪水风险以及其他 11 个垂直领域。公共 REST API、npm/PyPI 包、CC BY 4.0。
- [Helium](https://heliumtrades.com/mcp-page/) - 具有超过 15 个维度的结构化偏差特征的实时新闻语料库（320 万多篇文章、5,000 多个来源）、具有 AI 生成分析的实时金融市场数据（股票、ETF、加密货币）、具有概率指标和完整希腊语的 ML 期权定价、用于定量研究的历史期权链数据；可通过 MCP 服务器或 REST API 获取。


### 漫画
**[`^ 回到顶部 ^`](#awesome-data-science)**

- [漫画合集](https://medium.com/@nikhil_garg/a-compilation-of-comics-explaining-statistics-data-science-and-machine-learning-eeefbae91277)
- [Cartoons](https://www.kdnuggets.com/websites/cartoons.html)
- [数据科学卡通](https://www.cartoonstock.com/directory/d/data_science.asp)
- [数据科学：XKCD 版](https://davidlindelof.com/data-science-the-xkcd-edition/)

## 其他很棒的清单

- 其他令人惊叹的很棒的列表可以在[awesome-awesomeness](https://github.com/bayandin/awesome-awesomeness)中找到
- [很棒的机器学习](https://github.com/josephmisiti/awesome-machine-learning)
- [lists](https://github.com/jnv/lists)
- [awesome-dataviz](https://github.com/javierluraschi/awesome-dataviz)
- [awesome-python](https://github.com/vinta/awesome-python)
- [数据科学 IPython 笔记本。](https://github.com/donnemartin/data-science-ipython-notebooks)
- [awesome-r](https://github.com/qinwf/awesome-R)
- [awesome-datasets](https://github.com/awesomedata/awesome-public-datasets)
- [Awesome-机器学习和深度学习教程](https://github.com/ujjwalkarn/Machine-Learning-Tutorials/blob/master/README.md)
- [很棒的数据科学想法](https://github.com/JosPolfliet/awesome-ai-usecases)
- [软件工程师的机器学习](https://github.com/ZuzooVn/machine-learning-for-software-engineers)
- [社区精选的数据科学资源](https://hackr.io/tutorials/learn-data-science)
- [很棒的源代码机器学习](https://github.com/src-d/awesome-machine-learning-on-source-code)
- [很棒的社区检测](https://github.com/benedekrozemberczki/awesome-community-detection)
- [很棒的图分类](https://github.com/benedekrozemberczki/awesome-graph-classification)
- [很棒的决策树论文](https://github.com/benedekrozemberczki/awesome-decision-tree-papers)
- [很棒的欺诈检测论文](https://github.com/benedekrozemberczki/awesome-fraud-detection-papers)
- [很棒的梯度提升论文](https://github.com/benedekrozemberczki/awesome-gradient-boosting-papers)
- [很棒的计算机视觉模型](https://github.com/nerox8664/awesome-computer-vision-models)
- [很棒的蒙特卡罗树搜索](https://github.com/benedekrozemberczki/awesome-monte-carlo-tree-search-papers)
- [常见统计数据和机器学习术语词汇表](https://www.analyticsvidhya.com/glossary-of-common-statistics-and-machine-learning-terms/)
- [100 篇 NLP 论文](https://github.com/mhagiwara/100-nlp-papers)
- [很棒的游戏数据集](https://github.com/leomaurodesenv/game-datasets#readme)
- [ML/AI Interview Prep](https://github.com/aasimansari1/ml-interview-prep) - 500 多个带有可运行代码的 ML/AI 面试问答 — 涵盖 ML 基础知识、深度学习、NLP、PyTorch、scikit-learn 管道和系统设计
- [数据科学面试问题](https://github.com/alexeygrigorev/data-science-interviews)
- [很棒的可解释的图形推理](https://github.com/AstraZeneca/awesome-explainable-graph-reasoning)
- [热门数据科学面试问题](https://www.interviewbit.com/data-science-interview-questions/)
- [令人惊叹的药物协同作用、相互作用和复方用药预测](https://github.com/AstraZeneca/awesome-drug-pair-scoring)
- [深度学习面试问题](https://www.adaface.com/blog/deep-learning-interview-questions/)
- [2023 年数据科学的未来主要趋势](https://medium.com/the-modern-scientist/top-future-trends-in-data-science-in-2023-3e616c8998b8)
- [生成式人工智能如何改变创意工作](https://hbr.org/2022/11/how-generative-ai-is-changing-creative-work)
- [什么是生成式人工智能？](https://www.techtarget.com/searchenterpriseai/definition/generative-AI)
- [100 多个机器学习面试问题（初级到高级）](https://www.appliedaicourse.com/blog/machine-learning-interview-questions/)
- [数据科学项目](https://github.com/veb-101/Data-Science-Projects)
- [数据科学是一个好职业吗？](https://www.scaler.com/blog/is-data-science-a-good-career/)
- [数据科学的未来：预测和趋势](https://www.appliedaicourse.com/blog/future-of-data-science/)
- [数据科学和机器学习：有什么区别？](https://www.appliedaicourse.com/blog/data-science-and-machine-learning-whats-the-difference/)
- [数据科学中的人工智能：用途、角色和工具](https://www.scaler.com/blog/ai-in-data-science/)
- [前 13 种数据科学编程语言](https://www.appliedaicourse.com/blog/data-science-programming-languages/)
- [40 多个数据分析项目创意](https://www.appliedaicourse.com/blog/data-analytics-projects-ideas/)
- [最佳数据科学课程及证书](https://www.appliedaicourse.com/blog/best-data-science-courses/)
- [生成式人工智能模型](https://www.appliedaicourse.com/blog/generative-ai-models/)
- [Awesome Data Analysis](https://github.com/PavelGrigoryevDS/awesome-data-analysis) - 数据分析工具、库和资源的精选列表。
- [Awesome Evidence Synthesis](https://github.com/evidencesynthesis-tools/awesome-evidence-synthesis) - 用于系统评价、荟萃分析和证据综合的开源工具精选列表。
- [AI Dev Jobs](https://aidevboard.com/) - 求职板专注于 AI/ML 工程职位，拥有 5,400 多个列表和免费的 REST API。


### 爱好
- [很棒的音乐制作](https://github.com/ad-si/awesome-music-production)
