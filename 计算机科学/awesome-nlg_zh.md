# 令人惊叹的自然语言生成 [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

![来自 BL Harley 647 的 Piscis Magnus](logo.png)

自然语言生成是一个广泛的领域，在聊天机器人、故事生成和数据描述中都有应用。有多种不同的技术可解决部分或整个 NLG 流程。该列表旨在通过提供各种项目、工具、研究论文和学习材料的链接来展示 NLG 应用和技术的多样性。

## 内容

- [Datasets](#datasets)
- [Dialog](#dialog)
- [Evaluation](#evaluation)
- [Grammar](#grammar)
- [Libraries](#libraries)
- [叙事生成](#narrative-generation)
- [神经自然语言生成](#neural-natural-language-generation)
- [论文和文章](#papers-and-articles)
- [Products](#products)
- [Realizers](#realizers)
- [模板语言](#templating-languages)
- [Videos](#videos)

## 数据集

- [Alex Context NLG Dataset](https://github.com/UFAL-DSG/alex_context_nlg_dataset) - 公共交通信息领域对话系统中的 NLG 数据集。
- [Box-score data](https://github.com/harvardnlp/boxscore-data/) - 该数据集由（人工编写的）NBA 篮球比赛摘要组成，与其相应的得分和得分相符。
- [E2E](http://www.macs.hw.ac.uk/InteractionLab/E2E) - 这项共享任务重点关注最近的端到端（E2E）、数据驱动的 NLG 方法，该方法从非对齐数据中共同学习句子规划和表面实现。
- [Neural-Wikipedian](https://github.com/pvougiou/Neural-Wikipedian) - 该存储库包含代码以及所需的语料库，用于构建一个“学习”如何为语义网三元组生成英语传记的系统。
- [WeatherGov](https://cs.stanford.edu/~pliang/data/weather-data.zip) - 来自weather.gov（美国公共预报）的计算机生成的天气预报以及相应的天气数据。
- [WebNLG](https://github.com/ThiagoCF05/webnlg) - WebNLG 的丰富版本 - 用于评估常见 NLG 任务的资源，包括话语排序、词汇化和引用表达式生成。
- [WikiBio - wikipedia biography dataset](https://rlebret.github.io/wikipedia-biography-dataset/) - 该数据集从维基百科收集了 728,321 份传记。它旨在评估文本生成算法。
- [The Schema-Guided Dialogue Dataset](https://github.com/google-research-datasets/dstc8-schema-guided-dialogue) - 模式引导对话 (SGD) 数据集由人类和虚拟助手之间超过 20k 个带注释的多域、面向任务的对话组成。
- [The Wikipedia company corpus](https://gricad-gitlab.univ-grenoble-alpes.fr/getalp/wikipediacompanycorpus) - 从维基百科收集的公司描述。该数据集包含 51K 公司的英语语义表示、简短和详细描述。
- [YelpNLG](https://nlds.soe.ucsc.edu/yelpnlg) - YelpNLG 提供用于自然语言生成餐厅评论的资源。

## 对话

- [Chatito](https://github.com/rodrigopivi/Chatito) - 使用简单的 DSL 为 AI 聊天机器人、NLP 任务、命名实体识别或文本分类模型生成数据集！
- [NNDIAL](https://github.com/shawnwun/NNDIAL) - NNDial 是一个开源工具包，用于构建端到端可训练的面向任务的对话模型。
- [Plato](https://github.com/uber-research/plato-research-dialogue-system) - 这就是柏拉图研究对话系统，一个用于开发对话式人工智能代理的灵活平台。
- [RNNLG](https://github.com/shawnwun/RNNLG) - RNNLG 是口语对话系统应用领域中自然语言生成（NLG）的开源基准工具包。
- [TGen](https://github.com/UFAL-DSG/tgen) - 用于口语对话系统的统计 NLG。

## 评价

- [BLEURT：基于迁移学习的自然语言生成指标](https://github.com/google-research/bleurt)
- [compare-mt](https://github.com/neulab/compare-mt) - 语言生成系统整体分析的工具。
- [GEM](https://gem-benchmark.com/) - NLG 的基准环境，重点是通过人工注释和自动化指标进行评估。
- [NLG-eval](https://github.com/Maluuba/nlg-eval) - 用于自然语言生成的各种无监督自动化指标的评估代码。
- [VizSeq](https://github.com/facebookresearch/vizseq) - 用于文本生成任务的可视化分析工具包。

## 语法

- [OpenCCG](https://github.com/OpenCCG/openccg) - OpenCCG库，用于用CCG解析和实现。
- [GrammaticalFramework](http://www.grammaticalframework.org/) - 用于多语言语法应用程序的编程语言。
- [EasyCCG](https://github.com/mikelewis0/easyccg) - CCG：所有组合器、通用语法格式、解析为逻辑形式、概率 CCG 的参数估计。
- [CCG Lab](https://github.com/bozsahin/ccglab) - 所有组合器、通用语法格式、解析为逻辑形式、概率 CCG 的参数估计。
- [CCGweb](https://github.com/texttheater/ccgweb) - 用于解析和注释的 Web 平台。

## 图书馆

- [Cron Expression Descriptor](https://github.com/bradymholt/cron-expression-descriptor) - 一个 .NET 库，可将 cron 表达式转换为人类可读的描述。
- [Number Words](https://github.com/tokenmill/numberwords) - 将数字转换为近似文本表达式：从“0.23”到“小于四分之一”。
- [Writebot](https://docs.writebot.app) - 一个 NodeJS 库，通过使用预设可以更轻松地使用 GPT-3。

## 叙事生成

- [Random Story Generator](https://github.com/aherriot/story-generator) - 使用自然语言生成 (NLG) 创建随机短篇故事。
- [Tracery](https://github.com/galaxykate/tracery) - JavaScript 的故事语法生成库。

## 神经自然语言生成

- [aitextgen](https://github.com/minimaxir/aitextgen) - 一个强大的 Python 工具，用于使用 GPT-2 进行基于文本的 AI 训练和生成。
- [graph-2-text](https://github.com/diegma/graph-2-text) - 在 Pytorch 中结合图卷积网络和 opennmt-py 实现的图到序列。
- [Image Caption Generator](https://github.com/neural-nuts/image-caption-generator) - 基于神经网络的生成模型，用于使用 Tensorflow 为图像添加字幕。
- [lightnlg](https://github.com/kasnerz/lightnlg) - 一个简约的代码库，用于使用 PyTorch Lightning 微调 NLG 模型并与之交互。
- [PaperRobot: Incremental Draft Generation of Scientific Ideas](https://github.com/EagleW/PaperRobot) - 我们展示了一个 PaperRobot，它充当自动研究助理。
- [PPLM](https://github.com/uber-research/PPLM) - 即插即用语言模型实现。允许控制 GPT-2 模型的主题和属性。
- [Question Generation using hugstransformers](https://github.com/patil-suraj/question_generation) - 问题生成是从文本段落自动生成问题的任务。
- [Texar](https://github.com/asyml/texar) - Texar 是一个旨在支持广泛的机器学习的工具包，特别是自然语言处理和文本生成任务。
- [textgenrnn](https://github.com/minimaxir/textgenrnn) - 只需几行代码，即可在任何文本数据集上轻松训练您自己的任何大小和复杂程度的文本生成神经网络。
- [This Word Does Not Exist](https://github.com/turtlesoupy/this-word-does-not-exist) - 这个项目允许人们训练 GPT-2 的变体，从头开始组成单词、定义和示例。
- [Transformers](https://github.com/huggingface/transformers) - 适用于 TensorFlow 2.0 和 PyTorch 的最先进的自然语言处理。
- [Summary Generation From Structured Data](https://github.com/akanimax/natural-language-summary-generation-from-structured-data) - 用于将以结构化数据形式存在的信息转换为自然语言文本。

## 论文和文章
- [2022：修复破裂的基础：生成文本评估实践障碍调查](https://arxiv.org/abs/2202.06935)
- [2021 年：愿景：NLG 可以帮助数据和人工智能人性化](https://ehudreiter.com/2021/03/17/vision-nlg-can-help-humanise-data-and-ai/)
- [2020：神经文本退化的奇怪案例](https://openreview.net/forum?id=rygGQyrFvH)
- [2020：评估数据到文本系统准确性的黄金标准方法](https://arxiv.org/abs/2011.03992)
- [2020 年：评估端到端自然语言生成的最新技术：E2E NLG 挑战](https://www.sciencedirect.com/science/article/pii/S0885230819300919)
- [2020：如何生成文本：使用不同的解码方法通过 Transformers 生成语言](https://huggingface.co/blog/how-to-generate)
- [2020 年：自然语言生成：2020 年的商业最先进水平](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/BA2417D73AF29F8073FF5B611CDEB97F/S135132492000025Xa.pdf/natural_language_generation_the_commercial_state_of_the_art_in_2020.pdf)
- [2020 年：Turing-NLG：微软的 170 亿参数语言模型](https://www.microsoft.com/en-us/research/blog/turing-nlg-a-17-billion-parameter-language-model-by-microsoft/)
- [2019：仔细研究数据到文本 NLG 动词选择的最新结果](https://www.inlg2019.com/assets/papers/178_Paper.pdf)
- [2019：针对癌症患者的个性化数据到文本支持工具](https://www.inlg2019.com/assets/papers/28_Paper.pdf)
- [2019：通过人为设计的主题标签控制数据到文档生成的内容](https://www.inlg2019.com/assets/papers/79_Paper.pdf)
- [2019：生成的文本必须准确！](https://ehudreiter.com/2019/09/26/generated-texts-must-be-accurate/)
- [2019：Hotel Scribe：产生高度变化的酒店描述](https://www.inlg2019.com/assets/papers/44_Paper.pdf)
- [2019 年：以事实为依据重新审视数据到文本生成的挑战](https://www.inlg2019.com/assets/papers/32_Paper.pdf)
- [2017 年：自然语言生成技术现状调查：核心任务、应用和评估](https://arxiv.org/pdf/1703.09902.pdf)
- [2016：自然语言生成利用不确定信息增强人类决策](https://arxiv.org/pdf/1606.03254.pdf)


## 产品展示

- [Accelerated Text](https://github.com/tokenmill/accelerated-text) - 自动生成措辞和结构各异的数据的多种自然语言描述。
- [RosaeNLG](https://rosaenlg.org) - 一个用于 Node.js 或客户端（浏览器）执行的开源库，基于 Pug 模板引擎，用于生成英语、法语、德语和意大利语文本。
- [Twine](http://twinery.org/) - 一种用于讲述交互式非线性故事的开源工具。

## 实现者

- [Genl](https://github.com/kowey/GenI) - 使用树邻接语法的表面实现器（自然语言生成系统的一部分）。
- [JSrealB](https://github.com/rali-udem/JSrealB) - 用于 Web 开发的 JavaScript 双语文本实现器。
- [SimpleNLG](https://github.com/simplenlg/simplenlg) - 用于自然语言生成的 Java API。
- [SimpleNLG DE](https://github.com/sebischair/SimpleNLG-DE) - SimpleNLG 4 的德语版本。
- [SimpleNLG-EnFr](https://github.com/rali-udem/SimpleNLG-EnFr) - SimpleNLG-EnFr 1.1 是 SimpleNLG v4.2 的英语/法语双语版本。

## 模板语言

- [calyx](https://github.com/maetl/calyx) - 用于使用递归模板语法生成文本的 Ruby 库。
- [nalgene](https://github.com/spro/nalgene) - 自然语言生成语言。
- [StringTemplate](https://www.stringtemplate.org/) - Java 模板引擎（带有 C##、Objective-C、JavaScript、Scala 端口），用于生成源代码、网页、电子邮件或任何其他格式化文本输出。

## 视频

- [数据到文本：生成复杂数据的文本摘要 - Ehud Reiter](https://www.youtube.com/watch?v=kFRw-wk5YOA)
- [模仿学习及其在自然语言生成中的应用](https://slideslive.com/38922816/imitation-learning-and-its-application-to-natural-language-generation)
- [自然语言生成（简介）](https://www.youtube.com/watch?v=4fjM72lbJaw)
- [地层数据会议|自然语言生成的未来：2017-2027](https://www.youtube.com/watch?v=Ls7elVbN8bI)
- [对自动故事生成的探索 - Mark Riedl](https://www.youtube.com/watch?v=wgcDUX_BPpk)

## 许可证

[![CC0](http://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](http://creativecommons.org/publicdomain/zero/1.0)

在法律允许的范围内，[TokenMill](https://www.tokenmill.ai) 已放弃本作品的所有版权以及相关或邻接权。
