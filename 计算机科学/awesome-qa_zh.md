# 很棒的问答 [![Awesome](https://awesome.re/badge.svg)](https://github.com/sindresorhus/awesome)

___[问答 (QA)](https://en.wikipedia.org/wiki/Question_answering)__ 主题的精选列表，该主题是信息检索和自然语言处理 (NLP) 领域内的计算机科学学科，旨在使用机器学习和深度学习_

_정보 검색 및 자연 언어 처리 분야의 질의응답에 관한 큐레션 - 머신러닝과 딥러닝 단계까지_<br/>
_问答系统主题的精选列表，是信息检索和自然语言处理领域的计算机科学学科 - 使用机器学习和深度学习_

## 内容

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [近期趋势](#recent-trends)
- [关于质量保证](#about-qa)
- [Events](#events)
- [Systems](#systems)
- [QA 竞赛](#competitions-in-qa)
- [Publications](#publications)
- [Codes](#codes)
- [Lectures](#lectures)
- [Slides](#slides)
- [数据集集合](#dataset-collections)
- [Datasets](#datasets)
- [Books](#books)
- [Links](#links)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## 近期趋势
### 最近的 QA 模型
- DilBert：延迟基于 Transformer 的编码器中的交互层以实现高效的开放域问答（2020）
- 论文：https://arxiv.org/pdf/2010.08422.pdf
- github：https://github.com/wissam-sib/dilbert
- UnifiedQA：使用单一 QA 系统跨越格式边界 (2020)
- 演示：https://unifiedqa.apps.allenai.org/
- ProQA：为开放域 QA 和 IR 预训练密集语料库索引的资源高效方法。 (2020)
- 论文：https://arxiv.org/pdf/2005.00038.pdf
- github：https://github.com/xwhan/ProQA
- TYDI QA：以类型多样的语言进行信息搜索问答的基准（2020）
- 论文：https://arxiv.org/ftp/arxiv/papers/2003/2003.05002.pdf
- 机器阅读理解回顾性阅读器
- 论文：https://arxiv.org/pdf/2001.09694v2.pdf
- TANDA：传输和调整预先训练的 Transformer 模型以选择答案句子（AAAI 2020）
- 论文：https://arxiv.org/pdf/1911.04118.pdf
### 最近的语言模型
- [ELECTRA：将文本编码器预训练为判别器而不是生成器](https://openreview.net/pdf?id=r1xMH1BtvB)，Kevin Clark 等人，ICLR，2020。
- [TinyBERT：蒸馏 BERT 以实现自然语言理解](https://openreview.net/pdf?id=rJx0Q6EFPB)，Xiaoqi Jiao 等人，ICLR，2020。
- [MINILM：用于预训练 Transformer 的任务无关压缩的深度自注意力蒸馏](https://arxiv.org/abs/2002.10957)，Wenhui Wang 等人，arXiv，2020。
- [T5：使用统一的文本到文本转换器探索迁移学习的局限性](https://arxiv.org/abs/1910.10683)，Colin Raffel 等人，arXiv 预印本，2019。
- [ERNIE：通过信息实体增强语言表示](https://arxiv.org/abs/1905.07129)，Zhengyan Zhang 等人，ACL，2019。
- [XLNet：语言理解的广义自回归预训练](https://arxiv.org/abs/1906.08237)，Zhilin Yang 等人，arXiv 预印本，2019。
- [ALBERT：用于语言表示自监督学习的 Lite BERT](https://arxiv.org/abs/1909.11942)，Zhenzhong Lan 等人，arXiv 预印本，2019。
- [RoBERTa：一种稳健优化的 BERT 预训练方法](https://arxiv.org/abs/1907.11692)，Yinhan Liu 等人，arXiv 预印本，2019。
- [DistilBERT，BERT 的精炼版本：更小、更快、更便宜、更轻](https://arxiv.org/pdf/1910.01108.pdf)，Victor sanh 等人，arXiv，2019。
- [SpanBERT：通过表示和预测跨度来改进预训练](https://arxiv.org/pdf/1907.10529v3.pdf)，Mandar Joshi 等人，TACL，2019。
- [BERT：用于语言理解的深度双向变压器的预训练](https://arxiv.org/abs/1810.04805)，Jacob Devlin 等人，NAACL 2019，2018。
### 2020年亚洲人工智能大会
- [TANDA：传输和调整用于答案句子选择的预训练 Transformer 模型](https://arxiv.org/pdf/1911.04118.pdf)，Siddhant Garg 等人，AAAI 2020，2019 年 11 月。
### 2019年亚冠
- [MEDIQA 2019 文本推理共享任务概述，
问题蕴含和问答](https://www.aclweb.org/anthology/W19-5039)，Asma Ben Abacha 等人，ACL-W 2019，2019 年 8 月。
- [面向具有挑战性的 NLP 应用的可扩展且可靠的胶囊网络](https://arxiv.org/pdf/1906.02829v1.pdf)，Wei Zhu 等人，ACL 2019，2019 年 6 月。
- [大规模多跳阅读理解的认知图](https://arxiv.org/pdf/1905.05460v2.pdf)，Ming Ding 等人，ACL 2019，2019 年 6 月。
- [使用密集-稀疏短语索引的实时开放域问答](https://arxiv.org/abs/1906.05807)，Minjoon Seo 等人，ACL 2019，2019 年 6 月。
- [完形填空翻译的无监督问答](https://arxiv.org/abs/1906.04980)，Patrick Lewis 等人，ACL 2019，2019 年 6 月。
- [SemEval-2019 任务 10：数学问答](https://www.aclweb.org/anthology/S19-2153)，Mark Hopkins 等人，ACL-W 2019，2019 年 6 月。
- [利用知识感知阅读器改进不完整知识库的问答](https://arxiv.org/abs/1905.07098)，Wenhan Xiong 等人，ACL 2019，2019 年 5 月。
- [通过图形分解和卷积匹配文章对](https://arxiv.org/pdf/1802.07459v2.pdf)，Bang Liu 等人，ACL 2019，2019 年 5 月。
- [情景记忆阅读器：从流数据中学习问答要记住什么](https://arxiv.org/abs/1903.06164)，Moonsu Han 等人，ACL 2019，2019 年 3 月。
- [自然问题：问答研究的基准](https://ai.google/research/pubs/pub47761)，Tom Kwiatkowski 等人，TACL 2019，2019 年 1 月。
- [利用多模态上下文图理解和自监督开放集理解进行教科书问答](https://arxiv.org/abs/1811.00232)，Daesik Kim 等人，ACL 2019，2018 年 11 月。
### EMNLP-IJCNLP 2019
- [语言模型作为知识库？](https://arxiv.org/pdf/1909.01066v2.pdf)，Fabio Petron 等人，EMNLP-IJCNLP 2019，2019 年 9 月。
- [LXMERT：从 Transformers 学习跨模态编码器表示](https://arxiv.org/pdf/1908.07490v3.pdf)，Hao Tan 等人，EMNLP-IJCNLP 2019，2019 年 12 月。
- [通过迭代查询生成回答复杂的开放域问题](https://arxiv.org/pdf/1910.07000v1.pdf)，Peng Qi 等人，EMNLP-IJCNLP 2019，2019 年 10 月。
- [KagNet：用于常识推理的知识感知图网络](https://arxiv.org/pdf/1909.02151v1.pdf)，Bill Yuchen Lin 等人，EMNLP-IJCNLP 2019，2019 年 9 月。
- [用于多样化序列生成的混合内容选择](https://arxiv.org/pdf/1909.01953v1.pdf)，Jaemin Cho 等人，EMNLP-IJCNLP 2019，2019 年 9 月。
- [用于弱监督问答的离散硬 EM 方法](https://arxiv.org/pdf/1909.04849v1.pdf)，Sewon Min 等人，EMNLP-IJCNLP，2019 年，2019 年 9 月。
### Arxiv
- [调查 BERT 用于段落重排序的成功与失败](https://arxiv.org/abs/1905.01758)，Harshith Padigela 等人，arXiv 预印本，2019 年 5 月。
- [BERT with History Answer Embedding for Conversational Question Answering](https://arxiv.org/abs/1905.05412)，Chen Qu 等人，arXiv 预印本，2019 年 5 月。
- [理解 BERT 在排名中的行为](https://arxiv.org/abs/1904.07531)，乔一帆等人，arXiv 预印本，2019 年 4 月。
- [BERT 复习阅读理解和基于方面的情感分析的后期培训](https://arxiv.org/abs/1904.02232)，Hu Xu 等人，arXiv 预印本，2019 年 4 月。
- [使用 BERTserini 进行端到端开放域问答](https://arxiv.org/abs/1902.01718)，Wei Yang 等人，arXiv 预印本，2019 年 2 月。
- [自然问题的 BERT 基线](https://arxiv.org/abs/1901.08634)，Chris Alberti 等人，arXiv 预印本，2019 年 1 月。
- [使用 BERT 进行段落重新排名](https://arxiv.org/abs/1901.04085)，Rodrigo Nogueira 等人，arXiv 预印本，2019 年 1 月。
- [SDNet：用于会话问答的基于上下文注意的深度网络](https://arxiv.org/abs/1812.03593)，Chenuang Zhu 等人，arXiv，2018 年 12 月。
### 数据集
- [ELI5：长格式问答](https://arxiv.org/abs/1907.09190)，Angela Fan 等人，ACL 2019，2019 年 7 月
- [CODAH：一个对抗性编写的问答数据集
常识](https://www.aclweb.org/anthology/W19-2008.pdf)，Michael Chen 等人，RepEval 2019，2019 年 6 月。
  
## 关于质量保证
### 质量保证的类型
- 单轮问答：不考虑任何上下文即可回答
- 对话式 QA：使用之前的对话轮流
#### QA 的子类型
- 基于知识的质量保证
- 基于表格/列表的质量检查
- 基于文本的质量检查
- 基于社区的质量检查
- 视觉质量检查

### QA 系统中预处理的分析和解析
语言分析
1. [形态分析](https://www.cs.bham.ac.uk/~pjh/sem1a5/pt2/pt2_intro_morphology.html)
2. [命名实体识别(NER)](mds/named-entity-recognition.md)
3. 同音异义词/一词多义分析
4.句法分析（依存分析）
5. 语义识别

### 大多数 QA 系统大约有 3 个部分
1.事实提取<br/>
1.实体提取<br/>
1. [命名实体识别(NER)](mds/named-entity-recognition.md)
2.【关系抽取】(mds/relation-extraction.md) <br/>
2. 理解问题
3. 生成答案

## 活动
- Wolfram Alpha 于 2009 年推出了答案引擎。
- IBM Watson 系统在 2011 年击败了*[Jeopardy!](https://www.jeopardy.com)* 顶级冠军。
- Apple 的 Siri 于 2011 年集成了 Wolfram Alpha 的应答引擎。
- Google 在 2012 年利用免费基础知识库推出了知识图谱，拥抱了 QA。
- 亚马逊回声| Alexa (2015)、Google Home | Google Assistant (2016)、INVOKE | MS Cortana (2017)、HomePod (2017)

## 系统
- [IBM Watson](https://www.ibm.com/watson/) - 具有最先进的性能。
- [Facebook DrQA](https://research.fb.com/downloads/drqa/) - 应用于SQuAD1.0数据集。 SQuAD2.0数据集已发布。但 DrQA 尚未测试。
- [MIT media lab's Knowledge graph](http://conceptnet.io/) - 是一个免费提供的语义网络，旨在帮助计算机理解人们使用的单词的含义。

## QA 竞赛

|   |数据集|语言 |主办方 |自从 |排名第一 |型号|状态 |超越人类表现|
|---|------------------|---------------|---------------------|-------|-------------------------|-------------------------|--------|------------------------|
| 0 | [故事完形填空测试](http://cs.rochester.edu/~nasrinm/files/Papers/lsdsem17-shared-task.pdf) |英语 |大学。罗彻斯特| 2016 | 2016米萨普|逻辑回归|关闭 | x|
| 1 |马可女士|英语 |微软 | 2016 | 2016猿夫道研究NLP |火星 |关闭 |哦|
| 2 | MS 马可 V2 |英语 |微软 | 2018 | NTT Media Intelli。实验室。 |面膜问答风格 |已开业 | x|
| 3 | [SQuAD](https://arxiv.org/abs/1606.05250) |英语 |大学。斯坦福大学| 2018 | XLNet（单一模型）|XLNet团队|关闭 |哦|
| 4 | [SQuAD 2.0](https://rajpurkar.github.io/SQuAD-explorer/) |英语 |大学。斯坦福大学| 2018 |平安全华 | ALBERT + DAAF + 验证者（整体）|已开业 |哦|
| 5 | [TriviaQA](http://nlp.cs.washington.edu/triviaqa/) |英语 |大学。华盛顿 | 2017 | 2017明彦| - |关闭 | - |
| 6 | [decaNLP](https://decanlp.com/) |英语 | Salesforce 研究 | 2018 | Salesforce 研究 | MQAN |关闭 | x|
| 7 | [DuReader Ver1.](https://ai.baidu.com/broad/introduction) |中文 |百度 | 2015 | 2015尝试者| T-Reader（单）|关闭 | x|
| 8 | [DuReader Ver2.](https://ai.baidu.com/broad/introduction) |中文 |百度 | 2017 | 2017文艺复兴 |阿里阅书 |已开业 | - |
| 9 | [KorQuAD](https://korquad.github.io/KorQuad%201.0/) |韩语 | LG CNS 人工智能研究 | 2018 | Clova AI LaRva 团队 | LaRva-Kor-Large+ + CLaF（单）|关闭 |哦|
| 10 | 10 [KorQuAD 2.0](https://korquad.github.io/) |韩语 | LG CNS 人工智能研究 | 2019 | 2019江原国立大学| KNU-基线（单模型） |已开业 | x|
| 11 | 11 [CoQA](https://stanfordnlp.github.io/coqa/) |英语 |大学。斯坦福大学| 2018 |追一科技| RoBERTa + AT + KD（合奏）|已开业 |哦|

## 刊物
- 论文
- [“学习浏览文本”](https://arxiv.org/pdf/1704.06877.pdf), Adams Wei Yu, Hongrae Lee, Quoc V. Le, 2017.
：仅在文本中显示您想要的内容
- [“利用局部神经注意进行深度联合实体消歧”](https://arxiv.org/pdf/1704.04920.pdf)，Octavian-Eugen Ganea 和 Thomas Hofmann，2017 年。
- [“机器理解的双向注意力流”](https://arxiv.org/pdf/1611.01603.pdf), Minjoon Seo, Aniruddha Kembhavi, Ali Farhadi, Hananneh Hajishirzi, ICLR, 2017。
- [“利用卷积神经网络捕获实体链接的语义相似性”](http://nlp.cs.berkeley.edu/pubs/FrancisLandau-Durrett-Klein_2016_EntityConvnets_paper.pdf)，Matthew Francis-Landau、Greg Durrett 和 Dan Klei，NAACL-HLT 2016。
- https://GitHub.com/matthewfl/nlp-entity-convnet
- [“实体与知识库的链接：问题、技术和解决方案”](https://ieeexplore.ieee.org/document/6823700/)，Wei Shen，Jianyong Wang，Jiawei Han，IEEE 知识与数据工程汇刊 (TKDE)，2014。
- [““这就是 Watson”简介](https://ieeexplore.ieee.org/document/6177724/)，IBM 研究与开发杂志，D. A. Ferrucci，2012 年。
- [“从信息检索角度对问答技术的调查”](https://www.sciencedirect.com/science/article/pii/S0020025511003860)，信息科学，2011。
- [“受限领域中的问答：概述”](https://www.mitpressjournals.org/doi/abs/10.1162/coli.2007.33.1.41)，Diego Mollá 和 José Luis Vicedo，计算语言学，2007 年
- [“自然语言问答：来自这里的观点”]()，L Hirschman，R Gaizauskas，自然语言工程，2001。
- 实体消歧/实体链接

## 代码
- [BiDAF](https://github.com/allenai/bi-att-flow) - 双向注意力流（BIDAF）网络是一个多阶段的分层过程，它以不同的粒度级别表示上下文，并使用双向注意力流机制来获得查询感知的上下文表示，而无需早期汇总。
- 官方的;张量流 v1.2
  - [Paper](https://arxiv.org/pdf/1611.01603.pdf)
- [QANet](https://github.com/NLPLearn/QANet) - 问答架构不需要循环网络：它的编码器仅由卷积和自注意力组成，其中卷积对局部交互进行建模，自注意力对全局交互进行建模。
- 谷歌;非官方;张量流 v1.5
  - [Paper](#qanet)
- [R-Net](https://github.com/HKUST-KnowComp/R-Net) - 用于阅读理解式问答的端到端神经网络模型，旨在回答给定段落中的问题。
- 多发性硬化症;香港科技大学非官方；张量流 v1.5
  - [Paper](https://www.microsoft.com/en-us/research/wp-content/uploads/2017/05/r-net.pdf)
- [R-Net-in-Keras](https://github.com/YerevaNN/R-NET-in-Keras) - Keras 中的 R-NET 重新实现。
- 多发性硬化症;非官方;喀拉斯 v2.0.6
  - [Paper](https://www.microsoft.com/en-us/research/wp-content/uploads/2017/05/r-net.pdf)
- [DrQA](https://github.com/hitvoice/DrQA) - DrQA 是一个应用于开放域问答的阅读理解系统。
- Facebook;官方的;火炬 v0.4
  - [Paper](#drqa)
- [BERT](https://github.com/google-research/bert) - 一种新的语言表示模型，代表 Transformers 的双向编码器表示。与最近的语言表示模型不同，BERT 旨在通过联合调节所有层中的左右上下文来预训练深度双向表示。
- 谷歌;正式实施；张量流 v1.11.0
  - [Paper](https://arxiv.org/abs/1810.04805)

## 讲座
- [Question Answering - Natural Language Processing](https://youtu.be/Kzi6tE4JaGo) - 作者：德拉戈米尔·拉德夫博士|密歇根大学| 2016年。

## 幻灯片
- [Question Answering with Knowledge Bases, Web and Beyond](https://github.com/scottyih/Slides/blob/master/QA%20Tutorial.pdf) - 叶文涛 & 马浩 | 作者：Scott Wen-tau Yih微软研究院 | 2016年。
- [Question Answering](https://hpi.de/fileadmin/user_upload/fachgebiete/plattner/teaching/NaturalLanguageProcessing/NLP2017/NLP8_QuestionAnswering.pdf) - 作者：Mariana Neves 博士 |哈索·普拉特纳研究所 | 2017年。

## 数据集集合
- [NLIWOD 的问答数据集](https://github.com/dice-group/NLIWOD/tree/master/qa.datasets)
- [karthinkncode 的自然语言处理数据集](https://github.com/karthikncode/nlp-datasets)

## 数据集
- [AI2 科学问题 v2.1(2017)](http://data.allenai.org/ai2-science-questions/)
- 它包含美国小学和初中年级学生评估中使用的问题。每个问题都是四向多项选择格式，可能包含也可能不包含图表元素。
- 论文：http://ai2-website.s3.amazonaws.com/publications/AI2ReasoningChallenge2018.pdf
- [儿童图书测试](https://uclmr.github.io/ai4exams/data.html)
- 它是 Facebook AI Research 的 bAbI 项目之一，旨在实现自动文本理解和推理的目标。 CBT 旨在直接衡量语言模型利用更广泛的语言环境的能力。
- [CODAH 数据集](https://github.com/Websail-NU/CODAH)
- [DeepMind 问答数据集；美国有线电视新闻网/每日邮报](https://github.com/deepmind/rc-data)
- 赫尔曼等人。 （2015）使用新闻文章创建了两个很棒的数据集用于问答研究。每个数据集包含许多文档（每个文档 90k 和 197k），每个文档平均包含大约 4 个问题。每个问题都是一个缺少一个单词/短语的句子，可以从随附的文档/上下文中找到。
- 论文：https://arxiv.org/abs/1506.03340
- [ELI5](https://github.com/facebookresearch/ELI5)
- 论文：https://arxiv.org/abs/1907.09190
- [GraphQuestions](https://github.com/ysu1989/GraphQuestions)
- 生成用于 QA 评估的特征丰富的问题集。
- [LC-QuAD](http://sda.cs.uni-bonn.de/projects/qa-dataset/)
- 它是黄金标准 KBQA（知识库问答）数据集，包含 5000 个问题和 SPARQL 查询。 LC-QuAD 使用 DBpedia v04.16 作为目标知识库。
- [马可女士](http://www.msmarco.org/dataset.aspx)
- 这是用于现实世界的问题回答。
- 论文：https://arxiv.org/abs/1611.09268
- [MultiRC](https://cogcomp.org/multirc/)
- 短段落和多句问题的数据集
- 论文：http://cogcomp.org/page/publication_view/833
- [NarrativeQA](https://github.com/deepmind/narrativeqa)
- 它包括带有维基百科摘要的文档列表、完整故事的链接以及问题和答案。
- 论文：https://arxiv.org/pdf/1712.07040v1.pdf
- [NewsQA](https://github.com/Maluuba/newsqa)
- 机器理解数据集
- 论文：https://arxiv.org/pdf/1611.09830.pdf
- [CMU 问答数据集](http://www.cs.cmu.edu/~ark/QA-data/)
- 这是维基百科文章的语料库、从中手动生成的事实问题以及这些问题的手动生成的答案，用于学术研究。这些数据是由 Noah Smith、Michael Heilman、Rebecca Hwa、Shay Cohen、Kevin Gimpel 以及卡内基梅隆大学和匹兹堡大学的许多学生在 2008 年至 2010 年间收集的。
- [SQuAD1.0](https://rajpurkar.github.io/SQuAD-explorer/)
- 斯坦福问答数据集（SQuAD）是一个阅读理解数据集，由众包者对一组维基百科文章提出的问题组成，其中每个问题的答案是相应阅读段落中的一段文本或跨度，否则问题可能无法回答。
- 论文：https://arxiv.org/abs/1606.05250
- [SQuAD2.0](https://rajpurkar.github.io/SQuAD-explorer/)
- SQuAD2.0 将 SQuAD1.1 中的 100,000 个问题与众包工作者对抗性编写的 50,000 多个新的、无法回答的问题结合起来，看起来与可回答的问题相似。为了在 SQuAD2.0 上表现出色，系统不仅必须在可能的情况下回答问题，而且还要确定何时该段落不支持答案并放弃回答。
- 论文：https://arxiv.org/abs/1806.03822
- [故事完形填空测试](http://cs.rochester.edu/nlp/rocstories/)
- “故事完形填空测试”是一种新的常识推理框架，用于评估故事理解、故事生成和剧本学习。该测试要求系统为一个四句故事选择正确的结局。
- 论文：https://arxiv.org/abs/1604.01696
- [TriviaQA](http://nlp.cs.washington.edu/triviaqa/)
- TriviaQA 是一个阅读理解数据集，包含超过 65 万个问答证据三元组。 TriviaQA 包括由琐事爱好者撰写的 95000 个问答对和独立收集的证据文档，平均每个问题 6 个，为回答问题提供高质量的远程监督。
- 论文：https://arxiv.org/abs/1705.03551
- [WikiQA](https://www.microsoft.com/en-us/download/details.aspx?id=52419&from=https%3A%2F%2Fresearch.microsoft.com%2Fen-US%2Fdownloads%2F4495da01-db8c-4041-a7f6-7984a4f6a905%2Fdefault.aspx)
- 用于开放域问答的公开可用的问题和句子对集。
  
### IBM Watson 5年内发表的DeepQA研究团队
- 2015
- “IBM Watson 中的电子病历自动生成问题列表”，Murthy Devarakonda、Ching-Huei Tsou，IAAI，2015 年。
- “IBM Watson 问答中的决策”，J. William Murdock，本体峰会，2015 年。
- [“IBM Watson 中的无监督实体关系分析”](http://www.cogsys.org/papers/ACS2015/article12.pdf)，Aditya Kalyanpur，J William Murdock，ACS，2015。
- “常识推理：基于事件微积分的方法”，E T Mueller，Morgan Kaufmann/Elsevier，2015 年。
- 2014
- “面向问题的患者记录摘要：关于 Watson 应用程序的早期报告”，M. Devarakonda、Dongyang 张、Ching-Huei Tsou、M. Bornea，Healthcom，2014 年。
- [“WatsonPaths：基于场景的问答和非结构化推理信息"](http://domino.watson.ibm.com/library/Cyberdig.nsf/1e4115aea78b6e7c85256b360066f0d4/088f74984a07645485257d5f006ace96!OpenDocument&Highlight=0,RC25489), Adam Lally, Sugato Bachi、Michael A. Barborak、David W. Buchanan、Jennifer Chu-Carroll、David A. Ferrucci*、Michael R. Glass、Aditya Kalyanpur、Erik T. Mueller、J. William Murdock、Siddharth Patwardhan、John M. Prager、Christopher A. Welty，IBM 研究报告 RC25489，2014 年。
- [“流形模型的医疗关系提取”](http://acl2014.org/acl2014/P14-1/pdf/P14-1078.pdf)，Chang Wang 和 James Fan，ACL，2014。

### MS Research 5年内发表的论文
- 2018
- “人际交流中问答的特征和支持”，Xiao Yang、Ahmed Hassan Awadallah、Madian Khabsa、Wei Wang、Miaosen Wang，ACM SIGIR，2018。
- [“FigureQA：用于视觉推理的注释图形数据集”](https://arxiv.org/abs/1710.07300)，Samira Ebrahimi Kahou、Vincent Michalski、Adam Atkinson、Akos Kadar、Adam Trischler、Yoshua Bengio、ICLR，2018
- 2017
- “视觉问答的多级注意力网络”，于东飞，付建龙，梅涛，睿勇，CVPR，2017。
- “问答和问题生成的联合模型”，Tong Wang、Xingdi (Eric) Yuan、Adam Trischler，ICML，2017。
- “机器理解中迁移学习的两阶段综合网络”，David Golub、Po-Sen Huang、Xiaodong He、Li Deng，EMNLP，2017。
- “用语法可解释的表示进行问答”，Hamid Palangi、Paul Smolensky、Xiaodong He、Li Deng，
- “基于搜索的神经结构化学习用于顺序问答”，Mohit Iyyer、Wen-tau Yih、Ming-Wei Chang，ACL，2017。
- 2016
- [“用于图像问答的堆叠注意力网络”](https://www.cv-foundation.org/openaccess/content_cvpr_2016/html/Yang_Stacked_Attention_Networks_CVPR_2016_paper.html)，Zichao Yang，Xiaodong He，Jianfeng Gau，Li Deng，Alex Smola，CVPR，2016。
- [“通过知识库、网络及其他方式进行问答”](https://www.microsoft.com/en-us/research/publication/question-answering-with-knowledge-base-web-and-beyond/)，Yih、Scott Wen-tau 和 Ma、Hao，ACM SIGIR，2016 年。
- [“NewsQA：机器理解数据集”](https://arxiv.org/abs/1611.09830)，Adam Trischler、Tong Wang、Xingdi Yuan、Justin Harris、Alessandro Sordoni、Philip Bachman、Kaheer Suleman、RepL4NLP，2016。
- [“问答的表格单元格搜索”](https://dl.acm.org/itation.cfm?id=2883080)，孙欢和马，郝和何，晓东和易，文涛和苏，余和严，Xifeng，WWW，2016。
- 2015
- [“WIKIQA：开放域问答挑战数据集”](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/YangYihMeek_EMNLP-15_WikiQA.pdf)，Yi Yang、Wen-tau Yih 和 Christopher Meek，EMNLP，2015。
- [“基于网络的问答：重访 AskMSR”](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/AskMSRPlusTR_082815.pdf)，Chen-Tse Tsai、Wen-tau Yih 和 Christopher J.C. Burges，MSR-TR，2015 年。
- [“通过语义丰富进行开放域问答”](https://dl.acm.org/itation.cfm?id=2741651)，Huan Sun、Hao Ma、Wen-tau Yih、Chen-Tse Tsai、Jingjing Liu 和 Ming-Wei Chang，WWW，2015。
- 2014
- [“斯坦福 WebQuestions 基准上的 Microsoft 深度 QA 系统概述”](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/Microsoft20Deep20QA.pdf)，Zhenghao Wang、Shengquan Yan、Huaming Wang 和 Xudong Huang，MSR-TR，2014 年。
- [“单关系问答的语义解析”]()，Wen-tau Yih，Xiaodong He，Christopher Meek，ACL，2014。
  
### Google AI 5年内发布
- 2018
- Google 质量检查<a name="qanet"></a>
- [“QANet：将局部卷积与全局自注意力相结合进行阅读理解”](https://openreview.net/pdf?id=B14TlG-RW)，Adams Wei Yu，David Dohan，Minh-Thang Luong，Rui Zhao，Kai Chen，Mohammad Norouzi，Quoc V. Le，ICLR，2018。
- [“提出正确的问题：强化学习的主动问题重构”](https://openreview.net/pdf?id=S1CChZ-CZ)，Christian Buck、Jannis Bulian、Massimiliano Ciaramita、Wojciech Paweł Gajewski、Andrea Gesmundo、Neil Houlsby 和 Wei Wang，ICLR，2018 年。
- [“使用段落向量构建大型机器阅读理解数据集”](https://arxiv.org/pdf/1612.04342.pdf)，Radu Soricut，Nan Ding，2018。
- 句子表示
- [“学习句子表示的有效框架”](https://arxiv.org/pdf/1803.02893.pdf)，Lajanugen Logeswaran，Honglak Lee，ICLR，2018。
- [“模型理解这个问题吗？”](https://arxiv.org/pdf/1805.05492.pdf)，Pramod K. Mudrakarta 和 Ankur Taly 以及 Mukund Sundararajan 和 Kedar Dhamdhere，ACL，2018。
- 2017
- [“分析主动问答代理学习的语言”](https://arxiv.org/pdf/1801.07537.pdf)，Christian Buck、Jannis Bulian、Massimiliano Ciaramita、Wojciech Gajewski、Andrea Gesmundo、Neil Houlsby 和 Wei Wang，NIPS，2017 年。
- [“学习提取问答的循环表示”](https://arxiv.org/pdf/1611.01436.pdf)，Kenton Lee、Shimi Salant、Tom Kwiatkowski、Ankur Parikh、Dipanjan Das 和 Jonathan Berant，ICLR，2017 年。
- 确定相同的问题
- [“噪声预训练问题的神经释义识别”](https://arxiv.org/pdf/1704.04565.pdf)，Gaurav Singh Tomar、Thyago Duque、Oscar Täckström、Jakob Uszkoreit 和 Dipanjan Das，SCLeM，2017 年。
- 2014
- “好问题！社区问答中的问题质量”，Sujith Ravi 和 Bo Pang、Vibhor Rastogi 和 Ravi Kumar，ICWSM，2014 年。

### Facebook人工智能研究5年内发表
- 2018
- [体现问答](https://research.fb.com/publications/embodied-question-answering/)，Abhishek Das、Samyak Datta、Georgia Gkioxari、Stefan Lee、Devi Parikh 和 Dhruv Batra，CVPR，2018 年
- [解释是否使 VQA 模型对人类更具可预测性？](https://research.fb.com/publications/do-explanations-make-vqa-models-more-predictable-to-a- human/)，Arjun Chandrasekaran、Viraj Prabhu、Deshraj Yadav、Prithvijit Chattopadhyay 和 Devi Parikh，EMNLP，2018
- [用于问答的神经组合指称语义](https://research.fb.com/publications/neural-compositional-denotational-semantics-for-question-answering/)，Nitish Gupta，Mike Lewis，EMNLP，2018
- 2017
- DrQA <a name="drqa"></a>
- [阅读维基百科回答开放域问题](https://cs.stanford.edu/people/danqi/papers/acl2017.pdf)，Danqi Chen、Adam Fisch、Jason Weston 和 Antoine Bordes，ACL，2017 年。

## 书籍
- 自然语言问答系统平装本 - Boris Galitsky (2003)
- 问答的新方向 - Mark T. Maybury (2004)
- 《牛津计算语言学手册》第 3.5 部分的问答 - Sanda Harabagiu 和 Dan Moldovan (2005)
- 第 28 章语音和语言处理中的问答 - Daniel Jurafsky 和 James H. Martin (2017)

## 友情链接
- [从头开始构建问答系统 — 第 1 部分](https://towardsdatascience.com/building-a-question-answering-system-part-1-9388aadff507)
- [使用 Tensorflow 回答问题 作者：Steven Hewitt，O'REILLY，2017](https://www.oreilly.com/ideas/question-answering-with-tensorflow)
- [为什么回答问题很难](http://nicklothian.com/blog/2014/09/25/why-question-answering-is-hard/)


## 贡献

欢迎投稿！首先阅读[贡献指南](contributing.md)。

## 许可证
[![CC0](http://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/share-your-work/public-domain/cc0/)

在法律允许的范围内，[seriousmac](https://github.com/seriousmac)（维护者）已放弃本作品的所有版权以及相关或邻接权。
