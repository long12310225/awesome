# 出色的机器学习软件工程 [![Awesome](https://awesome.re/badge-flat2.svg)](https://awesome.re)

机器学习软件工程是用于构建不涉及核心 ML 问题的 ML 应用程序的技术和指南，例如：新算法的开发——而是周围的活动，如数据摄取、编码、测试、版本控制、部署、质量控制和团队协作。
良好的软件工程实践可以使用机器学习组件增强生产级应用程序的开发、部署和维护。

⭐ 必读

🎓 科学出版物


<br>
根据这些文献，我们编制了一项有关机器学习组件应用程序软件工程实践采用情况的调查。


请随意[参与并分享调查](https://se-ml.github.io/survey)并[阅读更多](https://se-ml.github.io/practices)！



## 内容

- [总体概述](#broad-overviews)
- [数据管理](#data-management)
- [模型训练](#model-training)
- [部署与运营](#deployment-and-operation)
- [社会方面](#social-aspects)
- [Governance](#governance)
- [Tooling](#tooling)

## 总体概述

这些资源涵盖了各个方面。
- [人工智能工程：11个基础实践](https://resources.sei.cmu.edu/asset_files/WhitePaper/2019_019_001_634648.pdf) ⭐
- [机器学习应用的最佳实践](https://pdfs.semanticscholar.org/2869/6212a4a204783e9dd3953f06e103c02c6972.pdf)
- [机器学习工程最佳实践](https://se-ml.github.io/practices/) ⭐
- [机器学习系统中隐藏的技术债务](https://papers.nips.cc/paper/5656-hidden-technical-debt-in-machine-learning-systems.pdf) 🎓⭐
- [机器学习规则：机器学习工程最佳实践](https://developers.google.com/machine-learning/guides/rules-of-ml) ⭐
- [机器学习软件工程：案例研究](https://www.microsoft.com/en-us/research/publication/software-engineering-for-machine-learning-a-case-study/) 🎓⭐


## 数据管理

如何管理机器学习中使用的数据集。

- [机器学习大数据数据收集调查 - AI Integration Perspective_2019](https://deepai.org/publication/a-survey-on-data-collection-for-machine-learning-a-big-data-ai-integration-perspective) 🎓
- [自动化大规模数据质量验证](http://www.vldb.org/pvldb/vol11/p1781-schelter.pdf) 🎓
- [生产机器学习中的数据管理挑战](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/46178.pdf)
- [机器学习的数据验证](https://mlsys.org/Conferences/2019/doc/2019/167.pdf) 🎓
- [如何组织 ML 的数据标签](https://www.altexsoft.com/blognp/datascience/how-to-organize-data-labeling-for-machine-learning-approaches-and-tools/)
- [大数据标签的诅咒以及解决它的三种方法](https://aws.amazon.com/blogs/apn/the-curse-of-big-data-labeling-and-three-ways-to-solve-it/)
- [Data Linter：ML 数据集的轻量级自动完整性检查](http://learningsys.org/nips17/assets/papers/paper_19.pdf) 🎓
- [机器学习数据标签终极指南](https://www.cloudfactory.com/data-labeling-guide)


## 模型训练

如何组织模型训练实验。

- [深度学习的 10 个最佳实践](https://nanonets.com/blog/10-best-practices-deep-learning/#track-model-experiments)
- [交叉验证研究中的苹果对苹果：分类器性能测量的陷阱](https://dl.acm.org/doi/abs/10.1145/1882471.1882479) 🎓
- [地面公平：将算法公平方法应用于生产系统](https://scontent-amt2-1.xx.fbcdn.net/v/t39.8562-6/159714417_1180893265647073_4215201353052552221_n.pdf?_nc_cat=111&c cb=1-3&_nc_sid=ae5e01&_nc_ohc=6WFnNMmyp68AX95bRHk&_nc_ht=scontent-amt2-1.xx&oh=7a548f822e659b7bb2f58a511c30ee19&oe=606F33AD)🎓
- [您如何管理机器学习实验？](https://medium.com/@hadyelsahar/how-do-you-manage-your-machine-learning-experiments-ab87508348ac)
- [机器学习测试：调查、景观和视野](https://arxiv.org/pdf/1906.10742.pdf) 🎓
- [吹毛求疵的机器学习技术债务](https://matthewmcateer.me/blog/machine-learning-technical-debt/)
- [关于比较分类器：要避免的陷阱和推荐的方法](https://link.springer.com/article/10.1023/A:1009752403260) 🎓⭐
- [关于人类智力和机器故障：综合机器学习系统故障排除](https://arxiv.org/pdf/1611.08309.pdf) 🎓
- [算法配置的陷阱和最佳实践](https://www.jair.org/index.php/jair/article/download/11420/26488/) 🎓
- [监督特征选择的陷阱](https://academic.oup.com/bioinformatics/article/26/3/440/213774) 🎓
- [机器学习的准备和架构](https://www.gartner.com/en/documents/3889770/preparing-and-architecting-for-machine-learning-2018-upd)
- 【机器学习系统开发流程初步系统文献综述】(https://arxiv.org/abs/1910.05528) 🎓
- [深度学习环境中的软件开发最佳实践](https://towardsdatascience.com/software-development-best-practices-in-a-deep-learning-environment-a1769e9859b1)
- [机器学习中的测试和调试](https://developers.google.com/machine-learning/testing-debugging)
- [出了什么问题以及为什么？在野外诊断情境交互失败](https://www.microsoft.com/en-us/research/publication/what-went-wrong-and-why-diagnosing-situated-interaction-failures-in-the-wild/) 🎓


## 部署与运营

如何在生产环境中部署和操作模型。

- [机器学习基础设施的最佳实践](https://algorithmia.com/blog/best-practices-in-machine-learning-infrastructure)
- [构建机器学习持续集成服务](http://pages.cs.wisc.edu/~wentaowu/papers/kdd20-ci-for-ml.pdf) 🎓
- [机器学习的持续交付](https://martinfowler.com/articles/cd4ml.html) ⭐
- [TensorFlow Extended (TFX) 平台中的生产 ML 持续训练](https://www.usenix.org/system/files/opml19papers-baylor.pdf) 🎓
- [公平指标：公平机器学习系统的可扩展基础设施](https://ai.googleblog.com/2019/12/fairness-indicators-scalable.html) 🎓
- [机器学习物流](https://mapr.com/ebook/machine-learning-logistics/)
- [机器学习：从实验到生产](https://blog.codecentric.de/en/2019/03/machine-learning-experiments-production/)
- [ML Ops：机器学习作为一门工程学科](https://towardsdatascience.com/ml-ops-machine-learning-as-an-engineering-discipline-b86ca4874a3f)
- [减少生产无政府状态的模型治理](https://www.usenix.org/conference/atc18/presentation/sridhar) 🎓
- [ModelOps：基于云的生命周期管理，实现可靠且值得信赖的 AI](http://hummer.io/docs/2019-ic2e-modelops.pdf)
- [操作机器学习](https://www.kdnuggets.com/2018/04/operational-machine-learning-successful-mlops.html)
- [扩展机器学习即服务](http://proceedings.mlr.press/v67/li17a/li17a.pdf)🎓
- [TFX：基于张量流的生产规模机器学习平台](https://dl.acm.org/doi/pdf/10.1145/3097983.3098021?download=true) 🎓
- [ML 测试分数：ML 生产准备情况和技术债务减少的评分标准](https://research.google/pubs/pub46555/) 🎓
- [规格不足对现代机器学习的可信度提出了挑战](https://arxiv.org/abs/2011.03395) 🎓
- [端到端机器学习管道的版本控制](https://doi.org/10.1145/3076246.3076248) 🎓



## 社会方面

如何组织团队和项目以确保有效的协作和问责制。

- [软件团队中的数据科学家：最先进的技术和挑战](http://web.cs.ucla.edu/~miryung/Publications/tse2017-datascientists.pdf) 🎓
- [机器学习访谈](https://github.com/chiphuyen/machine-learning-systems-design/blob/master/build/build1/consolidated.pdf)
- [管理机器学习项目](https://d1.awsstatic.com/whitepapers/aws-managing-ml-projects.pdf)
- [有原则的机器学习：高效协作的实践和工具](https://dev.to/robogeek/principled-machine-learning-4eho)


## 治理
- [基于证据权重的以人为中心的可解释性框架](https://arxiv.org/pdf/2104.13299.pdf) 🎓
- [机器学习系统的架构风险分析](https://berryvilleiml.com/docs/ara.pdf)
- [超越除偏](https://complexdiscovery.com/wp-content/uploads/2021/09/EDRi-Beyond-Debiasing-Report.pdf)
- [缩小人工智能问责差距：定义内部算法审计的端到端框架](https://dl.acm.org/doi/pdf/10.1145/3351095.3372873) 🎓
- [公平确定风险评分的固有权衡](https://arxiv.org/abs/1609.05807) 🎓
- [负责任的人工智能实践](https://ai.google/responsible-ai-practices/) ⭐
- [迈向可信赖的人工智能发展：支持可验证声明的机制](https://arxiv.org/abs/2004.07213)
- [理解软件-2.0](https://dl.acm.org/doi/abs/10.1145/3453478) 🎓

## 工装

工具可以让您的生活更轻松。

我们只共享开源工具或提供大量免费研究包的商业平台。

- [Aim](https://aimstack.io) - Aim 是一个开源实验跟踪工具。
- [Airflow](https://airflow.apache.org/) - 以编程方式创作、安排和监控工作流程。
- [Alibi Detect](https://github.com/SeldonIO/alibi-detect) - Python 库专注于异常值、对抗性和漂移检测。
- [Archai](https://github.com/microsoft/archai) - 神经架构搜索。
- [Data Version Control (DVC)](https://dvc.org/) - DVC 是一种数据和 ML 实验管理工具。
- [Facets Overview / Facets Dive](https://pair-code.github.io/facets/) - 强大的可视化有助于理解机器学习数据集。
- [FairLearn](https://fairlearn.github.io/) - 用于评估和提高机器学习模型公平性的工具包。
- [Git Large File System (LFS)](https://git-lfs.github.com/) - 使用 Git 内的文本指针替换大型文件（例如数据集）。
- [Great Expectations](https://github.com/great-expectations/great_expectations) - 通过管道集成进行数据验证和测试。
- [HParams](https://github.com/PetrochukM/HParams) - 一种深思熟虑的机器学习项目配置管理方法。
- [Kubeflow](https://www.kubeflow.org/) - 为想要构建和试验 ML 管道的数据科学家提供的平台。
- [Label Studio](https://github.com/heartexlabs/label-studio) - 具有标准化输出格式的多类型数据标注和注释工具。
- [LiFT](https://github.com/linkedin/LiFT) - Linkedin 公平工具包。
- [MLFlow](https://mlflow.org/) - 管理机器学习生命周期，包括实验、部署和中央模型注册表。
- [Model Card Toolkit](https://github.com/tensorflow/model-card-toolkit) - 简化并自动化模型卡的生成；用于模型文档。
- [Neptune.ai](https://neptune.ai/) - 实验跟踪工具为数据科学项目带来组织和协作。
- [Neuraxle](https://github.com/Neuraxio/Neuraxle) - 类似 Sklearn 的框架，用于深度学习项目中的超参数调整和 AutoML。
- [OpenML](https://www.openml.org) - 一项包容性运动，旨在建立一个开放、有组织的在线机器学习生态系统。
- [PyTorch Lightning](https://github.com/PyTorchLightning/pytorch-lightning) - 用于高性能人工智能研究的轻量级 PyTorch 包装器。缩放您的模型，而不是样板。
- [REVISE: REvealing VIsual biaSEs](https://github.com/princetonvisualai/revise-tool) - 自动检测视觉数据集中的偏差。
- [Robustness Metrics](https://github.com/google-research/robustness_metrics) - 用于评估分类模型稳健性的轻量级模块。
- [Seldon Core](https://github.com/SeldonIO/seldon-core) - 一个 MLOps 框架，用于在 Kubernetes 上打包、部署、监控和管理数千个生产机器学习模型。
- [Spark Machine Learning](https://spark.apache.org/mllib/) - Spark 的 ML 库由常见的学习算法和实用程序组成。
- [TensorBoard](https://www.tensorflow.org/tensorboard/) - TensorFlow 的可视化工具包。
- [Tensorflow Extended (TFX)](https://www.tensorflow.org/tfx/) - 用于部署生产机器学习管道的端到端平台。
- [Tensorflow Data Validation (TFDV)](https://github.com/tensorflow/data-validation) - 用于探索和验证机器学习数据的库。与远大前程类似，但针对的是 Tensorflow 数据。
- [Weights & Biases](https://www.wandb.com/) - 实验跟踪、模型优化和数据集版本控制。


## 贡献

欢迎贡献！首先阅读[贡献指南](contributing.md)
