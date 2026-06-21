# 很棒的信用模型 [![Awesome](https://awesome.re/badge-flat.svg)](https://github.com/sindresorhus/awesome)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

> 关于信用评分和信用风险建模的精彩论文、文章和各种资源不断增多。

信用评分是用于描述用于将信用申请人分类为风险类别的正式统计方法的术语。贷款人使用此类分类来评估申请人的信用度和违约概率。

## 内容

- [Introduction](#introduction)
- [信用评分](#credit-scoring)
- [机构信用风险](#institutional-credit-risk)
- [点对点借贷](#peer-to-peer-lending)
- [样本选择](#sample-selection)
- [特征选择](#feature-selection)
- [模型可解释性](#model-explainability)

## 简介

- [Statistical Classification Methods in Consumer Credit Scoring: A Review](https://www.jstor.org/stable/2983268) - 信用评分主题的经典介绍和回顾。

- [Consumer Finance: Challenges for Operational Research](https://www.jstor.org/stable/40540227) - 回顾信用评分（评估消费金融风险的方式）的发展以及信用评分的含义。概述了运筹学支持消费金融建模的 10 项挑战。

- [Machine Learning in Credit Risk Modeling](https://www.slideshare.net/YvanDeMunck/machine-learning-in-credit-risk-modeling-a-james-white-paper) - James（原 CrowdProcess）是一家现已解散的在线信用风险管理初创公司，为金融机构提供风险管理工具。本白皮书概述了信用风险建模领域的机器学习应用。

- ['Lending by numbers': credit scoring and the constitution of risk within American consumer credit](https://www.tandfonline.com/doi/abs/10.1080/03085140601089846) - 研究贷方如何应用统计信用评分技术来控制美国消费信贷中的违约水平。探讨他们感知到的方法、程序和时间风险。

- [Machine Learning in Financial Crisis Prediction: A Survey](https://ieeexplore.ieee.org/document/6069610) - 回顾 1995 年至 2010 年间的 130 篇期刊论文，重点关注用于破产预测和信用评分建模的最先进机器学习技术的开发。还介绍了他们当前的成就和局限性。

- [Fintech and big tech credit: a new database](https://www.bis.org/publ/work887.pdf) - 国际清算银行的这份工作文件虽然没有重点关注信用风险，但描绘了替代信贷的条件和所占据的利基市场，无论是金融科技公司还是大型科技公司提供的替代信贷。

## 信用评分

- [Benchmarking state-of-the-art classification algorithms for credit scoring: An update of research](https://www.sciencedirect.com/science/article/abs/pii/S0377221715004208) - 记分卡的开发已经取得了一些进展，包括新颖的学习方法、绩效衡量方法和可靠比较不同分类器的技术，而信用评分文献并未反映出这些进展。本文将几种新颖的分类算法与最先进的信用评分算法进行了比较。此外，还检查了替代记分卡的评估在已建立的和新的预测准确性指标之间的差异程度。

- [Classification methods applied to credit scoring: Systematic review and overall comparison](https://www.sciencedirect.com/science/article/abs/pii/S1876735416300101) - 控制和有效管理信用风险的需要促使金融机构在改进为此目的而设计的技术方面表现出色，从而导致金融机构和咨询公司开发了各种定量模型。因此，越来越多的关于信用评分的学术研究表明，有多种分类方法可以用来区分好借款人和坏借款人。本文旨在对信用评分财务分析的二​​元分类技术的理论和应用进行系统的文献综述。总体结果显示了信用评级主要技术的使用和重要性，以及多年来一些科学范式的变化。

- [Classifier Technology and the Illusion of Progress](https://projecteuclid.org/euclid.ss/1149600839) - 已经开发了许多用于监督分类的工具，从线性判别分析等早期方法到神经网络和支持向量机等现代发展。为了确定这些方法的相对优越性，已经进行了大量的比较研究。本文认为，这些比较往往未能考虑到实际问题的重要方面，因此更复杂的方法的明显优越性可能只是一种幻觉。特别是，简单方法通常产生的性能几乎与更复杂的方法一样好，以至于性能差异可能会被经典监督分类范式中通常不考虑的其他不确定性来源所淹没。

- [Financial credit risk assessment: a recent review](https://dl.acm.org/doi/10.1007/s10462-015-9434-x) - 总结了财务困境预测的传统统计模型和最先进的智能方法，重点介绍了最新成果。

- [Good practice in retail credit scorecard assessment](https://www.tandfonline.com/doi/abs/10.1057/palgrave.jors.2601932) - 在零售银行业务中，称为“记分卡”的预测统计模型用于将客户分配到类别，从而分配适当的行动或干预措施。此类分配是根据客户的预测分数高于还是低于给定阈值进行的。此类记分卡的预测能力会随着时间的推移而逐渐下降，因此需要对绩效进行监控。零售银行业常用的绩效衡量标准包括基尼系数、柯尔莫哥洛夫-斯米尔诺夫统计、均差和信息价值。然而，所有这些措施都使用了与分数大小无关的信息，并且未能使用与错误分类的数字相关的关键信息。结果是，这些措施有时可能会产生严重误导，导致做出质量低劣的决策，并采取错误的行动。

- [A literature review on the application of evolutionary computing to credit scoring](https://link.springer.com/article/10.1057/jors.2012.145) - 本文的目的是通过对 2000 年至 2012 年期间发表的科学文章的全面回顾，总结进化算法在信用评分中应用的最新进展。

- [Machine learning predictivity applied to consumer creditworthiness](https://fbj.springeropen.com/articles/10.1186/s43093-020-00041-w) - 使用巴西银行的贷款数据库分析借款人分类模型的充分性，探索机器学习技术，并将其预测准确性与基于逻辑回归模型的基准进行比较。比较基于通常的分类性能指标。

- [Consumer credit-risk models via machine-learning algorithms](https://alo.mit.edu/wp-content/uploads/2015/06/Household-behaviorConsumer-credit-riskCredit-card-borrowingMachine-learningNonparametric-estimation.pdf) - 作者应用机器学习技术构建消费者信用风险的非线性非参数预测模型。他们能够构建样本外预测，从而显着提高信用卡持卡人拖欠和违约的分类率。

- [Example-Dependent Cost-Sensitive Logistic Regression for Credit Scoring](https://ieeexplore.ieee.org/document/7033125) - 一些现实世界的分类问题本质上是依赖于示例的成本敏感的，其中由于错误分类而导致的成本因示例而异。信用评分是成本敏感分类的典型例子。然而，通常使用不考虑与贷款业务相关的实际财务成本的方法来处理它。

- [Credit scoring using the clustered support vector machine](https://www.sciencedirect.com/science/article/abs/pii/S0957417414005119) - 介绍使用集群支持向量机 (CSVM) 进行信用记分卡开发。这种最近设计的算法解决了与基于传统非线性支持向量机 (SVM) 的分类方法相关的一些限制。具体来说，众所周知，随着历史信用评分数据集变得越来越大，这些非线性方法虽然非常准确，但计算成本却很高。 CSVM 可以实现相当水平的分类性能，同时保持相对便宜的计算成本。

- [A comparative study on base classifiers in ensemble methods for credit scoring](https://www.sciencedirect.com/science/article/abs/pii/S0957417416306947) - 近年来，人工智能方法在信用风险评估中的应用意味着对传统方法的改进。最近的工作表明，分类器集成在此类任务中取得了更好的结果。

- [Multiple classifier application to credit risk assessment](https://www.sciencedirect.com/science/article/abs/pii/S0957417409008847) - ([勘误](https://www.sciencedirect.com/science/article/pii/S0957417410012364)) - 本文探讨了五种分类器对于不同类型噪声在信用风险预测准确性方面的预测行为，以及如何通过使用分类器集成来提高这种准确性。

- [Recent developments in consumer credit risk assessment](https://www.sciencedirect.com/science/article/abs/pii/S0377221706011866) - 尽管研究人员考虑了许多其他类型的分类器，但通常使用逻辑回归模型来估计向信贷申请人提供贷款的风险，但数据质量问题可能会阻止这些基于实验室的结果在实践中实现。对已接受申请人的样本而不是申请人群体的样本代表进行分类器的训练似乎不会导致偏差，尽管它确实会导致设置截止值的困难。

- [A survey of credit and behavioural scoring: forecasting financial risk of lending to consumers](https://www.sciencedirect.com/science/article/abs/pii/S0169207000000340) - 调查所使用的技术（基于统计和运营研究）以帮助组织决定是否向消费者提供信贷。它还讨论了将经济状况纳入评分系统的必要性，以及系统如何从估计消费者违约概率转变为估计消费者将为贷款组织带来的利润。

- [The comparisons of data mining techniques for the predictive accuracy of probability of default of credit card clients](https://www.sciencedirect.com/science/article/abs/pii/S0957417407006719) - 本研究比较了六种数据挖掘方法的违约概率预测准确性。从风险管理的角度来看，违约概率估计的预测准确性的结果将比分类的二元结果更有价值。

- [Super-App Behavioral Patterns in Credit Risk Models: Financial, Statistical and Regulatory Implications](https://arxiv.org/abs/2005.14658) - 与传统的局数据相比，呈现源自基于应用程序的市场的替代数据对信用评分模型的影响。这些替代数据源已证明在预测传统上银行和金融机构服务不足的领域中的借款人行为方面具有巨大的威力。与此同时，替代数据必须经过仔细验证，以克服不同司法管辖区的监管障碍。

- [Credit scoring methods: Latest trends and points to consider](https://www.sciencedirect.com/science/article/pii/S2405918822000095) - “（...）本文旨在对最新（2016-2021）的文章进行系统回顾，使用一组固定的问题来识别信用评分的趋势。调查方法和调查问卷与之前分析 1991-2015 年发表的信用评分文章的类似研究一致。我们力求将我们的结果与之前的时期进行比较，并强调该领域的一些最新最佳实践，这些可能对未来的研究人员有用。”

## 机构信用风险

- [Availability of Credit to Small Businesses](https://www.federalreserve.gov/publications/2017-september-availability-of-credit-to-small-businesses.htm) - 1996 年《经济增长和监管文书减少法案》第 2227 条要求，联邦储备系统理事会每五年向国会提交一份报告，详细说明所有债权人向小企业提供贷款的程度。最近的日期为 2017 年 9 月。

- [Credit Scoring and the Availability, Price, and Risk of Small Business Credit](https://muse.jhu.edu/article/181124) - 研究发现，在控制银行规模和银行之间的其他差异后，小企业信用评分与 10 万美元以下小企业信贷的数量扩大、平均价格较高和平均风险水平较高相关。

- [Credit Risk Assessment Using Statistical and Machine Learning: Basic Methodology and Risk Modeling Applications](https://link.springer.com/article/10.1023/A:1008699112516) - 通过风险建模实现更有效地利用资源的目标的一个重要因素是找到机构信贷组合中个体风险的准确预测因子。在这种背景下，作者对抵押贷款数据集的不同统计和机器学习建模方法进行了比较分析，目的是了解它们的局限性和潜力。

- [Random Survival Forests Models for SME Credit Risk Measurement](https://link.springer.com/article/10.1007/s11009-008-9078-2) - 扩展了中小企业（SME）信用风险违约领域的现有实证研究文献，提出了一种基于随机生存森林（RSF）的非参数方法，并将其性能与标准logit模型进行了比较。

- [Modeling Institutional Credit Risk with Financial News](https://arxiv.org/abs/2004.08204) - 当前降级风险建模工作依赖于第三方评级机构和风险管理咨询公司提供的多种量化指标。人们广泛推动使用替代数据源，例如财经新闻、财报电话会议记录或社交媒体内容，以可能在行业中获得竞争优势。本文提出了一种仅使用神经网络嵌入表示的新闻数据的预测降级模型。

- [Bankruptcy prediction for credit risk using neural networks: A survey and new results](https://ieeexplore.ieee.org/document/935101) - 企业破产的预测是一个重要且广泛研究的课题，因为它可以对银行贷款决策和盈利能力产生重大影响。这项工作回顾了破产预测的主题，重点是神经网络（NN）模型，并开发了神经网络破产预测模型，为神经网络系统提出了新的指标。

## 点对点借贷

- [Network based credit risk models](https://www.tandfonline.com/doi/abs/10.1080/08982112.2019.1655159) - 点对点借贷平台可能会降低成本并改善用户体验。这些改进可能是以信用风险测量不准确为代价的。作者建议用“替代数据”来增强传统的信用评分方法，这些数据包括从借款人之间的相似性网络中得出的中心性度量，并根据其财务比率推导出来。

## 样本选择

- [Reject inference in application scorecards: evidence from France](https://econpapers.repec.org/paper/drmwpaper/2016-10.htm) - 关于该主题的良好介绍和讨论。

- [Reject inference, augmentation, and sample selection](https://www.sciencedirect.com/science/article/abs/pii/S0377221706011969) - 深入讨论。

- [信用评分中的实例抽样：样本量和平衡的实证研究](http://www.research.lancs.ac.uk/portal/en/publications/instance-sampling-in-credit-scoring-an-empirical-study-of-sample-size-and-balancing(89b83914-c7f2-499a-8fa1-844d6cb6004d).html) -讨论信用建模中的传统采样约定，并认为使用更大的样本可以显着提高算法的准确性。

## 特征选择

- [A multi-objective approach for profit-driven feature selection in credit scoring](https://www.sciencedirect.com/science/article/pii/S0167923619300570) - 在信用评分中，特征选择的目的是去除不相关的数据，以提高记分卡的性能和可解释性。标准技术将特征选择视为单目标任务，并依赖于相关性等统计标准。最近的研究表明，使用基于利润的指标可以提高企业评分模型的质量。

- [Data mining feature selection for credit scoring models](https://link.springer.com/article/10.1057/palgrave.jors.2601976) - 使用的特征可能对信用评分模型的性能产生重要影响。为信用评分模型选择最佳特征集的过程通常是非系统性的，并且以某种任意的试验为主。本文对四种机器学习特征选择方法进行了实证研究。

- [Combination of feature selection approaches with SVM in credit scoring](https://www.sciencedirect.com/science/article/abs/pii/S0957417409010719) - 信用评分中有效的分类模型将客观地帮助依赖直觉经验的管理者。本研究提出了四种使用 SVM（支持向量机）分类器进行特征选择的方法，这些方法保留了足够的信息用于分类目的。

## 模型可解释性

- [Explainable Machine learning in Credit Risk Management](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3506274) - 提出了一种可解释的人工智能模型，可用于信用风险管理，特别是衡量使用信用评分平台借贷时产生的风险。

- [Machine learning explainability in finance: an application to default risk analysis](https://www.bankofengland.co.uk/working-paper/2019/machine-learning-explainability-in-finance-an-application-to-default-risk-analysis) - 英格兰银行的这篇工作论文提出了一个框架，用于解决某些机器学习 (ML) 应用中存在的“黑匣子”问题。

- [Regulatory learning: How to supervise machine learning models? An application to credit scoring](https://www.sciencedirect.com/science/article/pii/S2405918817300648) - 大数据策略的到来正在威胁金融监管的最新趋势，即简化模型和增强金融机构选择的方法的可比性。事实上，大数据战略的内在动态理念几乎与本文所述的当前法律和监管框架不相容。此外，模型选择也可能动态发展，迫使从业者和监管机构开发模型库、允许从一种模型切换到另一种模型的策略以及允许金融机构在降低风险的环境中进行创新的监管方法。
