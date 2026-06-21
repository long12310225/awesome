# 很棒的审计算法 [![Awesome](https://awesome.re/badge-flat.svg)](https://awesome.re)

用于审核黑盒算法的精选算法列表。
如今，许多算法（推荐、评分、分类）都是由第三方提供商运行的，用户或机构对如何操作数据没有任何了解。因此，此列表中的审核算法适用于此设置，创造了“黑匣子”设置，其中一名审核员希望深入了解这些远程算法。

<img src="https://github.com/erwanlemerrer/awesome-audit-algorithms/blob/main/resources/audit.png" width="600" alt="banner" class="center">

> 用户查询远程算法（例如，通过可用的API），以推断有关该算法的信息。

## 更新
缓慢/无更新：被当前技术取代......

## 内容
- [Papers](#papers)
- [相关活动（会议/研讨会）](#related-events)

## 论文

### 2026 
- [The Fair Game: Auditing & debiasing AI algorithms over time](https://www.cambridge.org/core/journals/cambridge-forum-on-ai-law-and-governance/article/fair-game-auditing-debiasing-ai-algorithms-over-time/9E8408C67F7CE30505122DD1586D9FA2) - 剑桥人工智能论坛杂志：法律与治理
- [Exposing the Illusion of Fairness: Auditing Vulnerabilities to Distributional Manipulation Attacks](https://arxiv.org/pdf/2507.20708) - (arXiv)

### 2025
- [Auditing Pay-Per-Token in Large Language Models](https://arxiv.org/pdf/2510.05181) - (arXiv) *开发一个基于鞅理论的审计框架，使受信任的第三方审计员能够顺序查询提供商
检测令牌误报。*
- [P2NIA: Privacy-Preserving Non-Iterative Auditing](https://arxiv.org/abs/2504.00874) - (ECAI) *建议审核员和平台进行互利合作：一种保护隐私和非迭代的审核方案，使用合成或本地数据增强公平性评估，避免与传统基于 API 的审核相关的挑战。*
- [The Fair Game: Auditing & debiasing AI algorithms overtime](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/9E8408C67F7CE30505122DD1586D9FA2/S3033373325000080a.pdf/the-fair-game-auditing-and-debiasing-ai-algorithms-over-time.pdf) - （剑桥人工智能论坛：法律与治理）*旨在通过创建一个审计员来模拟社会中道德和法律框架的演变，该审计员向围绕机器学习系统部署的去偏算法发送反馈。*
- [Robust ML Auditing using Prior Knowledge](https://arxiv.org/pdf/2505.04796) - (ICML) *正式规定审核员可以利用有关基本事实的先验知识来防止审核操纵的条件。*
- [CALM: Curiosity-Driven Auditing for Large Language Models](https://arxiv.org/abs/2501.02997) - (AAAI) *作为黑盒优化问题进行审计，其目标是自动发现目标 LLM 中表现出非法、不道德或不安全行为的输入-输出对。*
- [Queries, Representation & Detection: The Next 100 Model Fingerprinting Schemes](https://arxiv.org/abs/2412.13021) - (AAAI) *将模型指纹识别分为三个核心组件，以识别 ∼100 个以前未探索过的组合，并深入了解它们的性能。*

### 2024
- [Hardware and software platform inference](https://arxiv.org/pdf/2411.05197) - (arXiv) *一种仅根据黑盒机器学习模型的输入输出行为来识别其底层 GPU 架构和软件堆栈的方法。*
- [Auditing Local Explanations is Hard](https://arxiv.org/abs/2407.13281) - (NeurIPS) *给出审计解释的（令人望而却步的）查询复杂性。*
- [LLMs hallucinate graphs too: a structural perspective](https://arxiv.org/abs/2409.00159) - （复杂网络）*向法学硕士查询已知图并研究拓扑幻觉。提出结构性幻觉等级。*
- [Fairness Auditing with Multi-Agent Collaboration](https://arxiv.org/pdf/2402.08522) - (ECAI) *考虑多个
代理一起工作，每个代理审核同一平台的不同任务。*
- [绘制算法审计领域：系统文献综述
识别研究趋势、语言和地理差异](https://arxiv.org/pdf/2401.11194) - (Arxiv) *算法的系统审查
审计研究并确定其方法论的趋势。*
- [FairProof: Confidential and Certifiable Fairness for Neural Networks](https://arxiv.org/pdf/2402.12572v1.pdf) - (Arxiv) *使用零知识证明等加密工具提出传统审计的替代范例；给出了一个名为 FairProof 的系统，用于验证小型神经网络的公平性。*
- [Under manipulations, are some AI models harder to audit?](https://grodino.github.io/projects/manipulated-audits/preprint.pdf) - (SATML) *涉及黑盒审计的难度
使用 Rademacher 复杂度来评估目标模型的容量。*
- [Improved Membership Inference Attacks Against Language Classification Models](https://arxiv.org/pdf/2310.07219.pdf) - (ICLR) *提出了一个在审核模式下对分类器运行成员推理攻击的框架。*
- [Auditing Fairness by Betting](https://arxiv.org/pdf/2305.17570.pdf) - (Neurips) [[代码]](https://github.com/bchugg/auditing-fairness) *允许连续监控来自黑盒分类器或回归器的传入数据的顺序方法。*
### 2023
- [Privacy Auditing with One (1) Training Run](https://neurips.cc/virtual/2023/poster/70925) - （NeurIPS - 最佳论文）*通过单次训练来审核差分隐私机器学习系统的方案。*
- [Auditing fairness under unawareness through counterfactual reasoning](https://www.sciencedirect.com/science/article/pii/S0306457322003259) - （信息处理与管理）*展示如何揭示符合规定的黑盒模型是否仍然存在偏见。*
- [XAudit : A Theoretical Look at Auditing with Explanations](https://arxiv.org/pdf/2206.04740.pdf) - (Arxiv) *正式化解释在审计中的作用并调查是否以及如何模型解释
可以帮助审核。*
- [Keeping Up with the Language Models: Robustness-Bias Interplay in NLI Data and Models](https://arxiv.org/pdf/2305.12620.pdf) - (Arxiv) *提出了一种通过使用语言模型本身来延长审计数据集保质期的方法；还发现当前偏差审计指标的问题并提出替代方案——这些替代方案强调模型的脆弱性表面上增加了之前的偏差分数。*
- [Online Fairness Auditing through Iterative Refinement](https://dl.acm.org/doi/pdf/10.1145/3580305.3599454) - (KDD) *提供自适应过程，自动推断与估计公平性指标相关的概率保证。*
- [Stealing the Decoding Algorithms of Language Models](https://people.cs.umass.edu/~amir/papers/CCS23-LM-stealing.pdf) - (CCS) *窃取 LLM 解码算法的类型和超参数。*
- [Modeling rabbit‑holes on YouTube](https://link.springer.com/epdf/10.1007/s13278-023-01105-9?sharing_token=h-O-asHI49VUWS9FxN1Gsve4RwlQNchNByi7wbcMAY6I98PKW1PqhFQJ_JqQyk3TrB05qDb3LUzMDmKOgrupccQliViDle-rwKEi2MZ8xBViaAQhyN41oZBKLLeXchoeIW2kklVHC094I5KD8pxja4-if6-iB0uAI1FnqnYoxjU%3D) - (SNAM) *对 YouTube 中兔子洞中用户的诱捕动态进行建模，并提供对该封闭空间的测量。*
- [Auditing YouTube’s Recommendation Algorithm for Misinformation Filter Bubbles](https://dl.acm.org/doi/full/10.1145/3568392) - （推荐系统上的交易）*如何“打破泡沫”，即从推荐中恢复泡沫外壳。*
- [Auditing Yelp’s Business Ranking and Review Recommendation Through the Lens of Fairness](https://arxiv.org/pdf/2308.02129.pdf) - (Arxiv) *审计 Yelp 业务的公平性
排名和评论推荐系统，具有人口统计平等、曝光度和统计测试，例如分位数线性和逻辑回归。*
- [Confidential-PROFITT: Confidential PROof of FaIr Training of Trees](https://openreview.net/pdf?id=iIfDQVyuFD) - (ICLR) *提出公平的决策树学习算法以及零知识证明协议，以获得审核服务器上的公平性证明。*
- [SCALE-UP: An Efficient Black-box Input-level Backdoor Detection via Analyzing Scaled Prediction Consistency](https://arxiv.org/pdf/2302.03251.pdf) - (ICLR) *考虑机器学习即服务 (MLaaS) 应用程序中黑盒设置下的后门检测。*
### 2022
- [Two-Face: Adversarial Audit of Commercial Face Recognition Systems](https://ojs.aaai.org/index.php/ICWSM/article/view/19300/19072) - (ICWSM) *对多个系统 API 和数据集进行对抗性审计，提出一些令人担忧的观察结果。*
- [Scaling up search engine audits: Practical insights for algorithm auditing](https://journals.sagepub.com/doi/10.1177/01655515221093029) - （信息科学杂志）[（代码）]（https://github.com/gesiscss/WebBot）*使用虚拟代理的模拟浏览行为审核多个搜索引擎。*
- [A zest of lime: towards architecture-independent model distances](https://openreview.net/pdf?id=OUz_9TiTv9j) - (ICLR) *使用 LIME 测量两个远程模型之间的距离。*
- [Active Fairness Auditing](https://proceedings.mlr.press/v162/yan22c/yan22c.pdf) - (ICML) *基于查询的审核算法的研究，可以以查询有效的方式估计 ML 模型的人口统计奇偶性。*
- [Look at the Variance! Efficient Black-box Explanations with Sobol-based Sensitivity Analysis](https://proceedings.neurips.cc/paper/2021/file/da94cbeff56cfda50785df477941308b-Paper.pdf) - (NeurIPS) *Sobol 指数提供了一种有效的方法来捕获图像区域之间的高阶交互及其通过方差镜头对（黑匣子）神经网络预测的贡献。*
- [Your Echos are Heard: Tracking, Profiling, and Ad Targeting in the Amazon Smart Speaker Ecosystem](https://arxiv.org/pdf/2204.10920.pdf) - (arxiv) *推断 Amazon Echo 系统和广告定位算法之间的联系。*
### 2021
- [When the Umpire is also a Player: Bias in Private Label Product Recommendations on E-commerce Marketplaces](https://arxiv.org/pdf/2102.00141.pdf) - (FAccT) *亚马逊自有品牌产品是否获得了不公平的推荐份额，因此与第三方产品相比具有优势？*
- [Everyday Algorithm Auditing: Understanding the Power of Everyday Users in Surfacing Harmful Algorithmic Behaviors](https://arxiv.org/pdf/2105.02980.pdf) - (CHI) *为用户提供“日常算法审计”的理由。*
- [Auditing Black-Box Prediction Models for Data Minimization Compliance](https://www.cs.bu.edu/faculty/crovella/paper-archive/minimization-audit-Neurips21.pdf) - (NeurIPS) *使用有限数量的查询来衡量预测模型满足的数据最小化水平。*
- [Setting the Record Straighter on Shadow Banning](https://arxiv.org/abs/2012.05101) - (INFOCOM) [(Code)](https://gitlab.enseeiht.fr/bmorgan/infocom-2021) *考虑 Twitter 中影子禁令的可能性（即审核黑盒算法），并测量几个假设的概率。*
- [Extracting Training Data from Large Language Models](https://arxiv.org/pdf/2012.07805.pdf) - （USENIX Security）*从 GPT-2 模型的训练数据中提取逐字文本序列。*
- [FairLens: Auditing black-box clinical decision support systems](https://www.sciencedirect.com/science/article/pii/S030645732100145X?casa_token=oyjFKij269MAAAAA:w_ohScpMPNMnkDdzBqAIod5QfBgQlq5Ht9mMRSOydZpOgNG-i1yuqEmBjWN__38gOGmjNL7dVT0) - （信息处理和管理）*通过比较不同的多标签分类差异度量，提出一个检测和解释临床 DSS 中潜在公平性问题的管道。*
- [Auditing Algorithmic Bias on Twitter](https://dl.acm.org/doi/abs/10.1145/3447535.3462491) - （网络科学）。
- [Bayesian Algorithm Execution: Estimating Computable Properties of Black-box Functions Using Mutual Information](https://proceedings.mlr.press/v139/neiswanger21a.html) - (ICML) *预算约束和贝叶斯优化程序，用于从黑盒算法中提取属性。*
### 2020
- [Black-Box Ripper: Copying black-box models using generative evolutionary algorithms](https://proceedings.neurips.cc/paper/2020/file/e8d66338fab3727e34a9179ed8804f64-Paper.pdf) - (NeurIPS) *复制黑盒神经模型的功能，但查询数量没有限制（通过教师/学生方案和进化搜索）。*
- [Auditing radicalization pathways on ](https://dl.acm.org/doi/pdf/10.1145/3351095.3372879) - (FAT*) *使用静态信道推荐上的随机游走来研究激进信道彼此之间的可达性。*
- [Adversarial Model Extraction on Graph Neural Networks](https://arxiv.org/abs/1912.07721) - （AAAI 图深度学习研讨会：方法论和应用）*介绍了 GNN 模型提取并提出了初步方法。*
- [Remote Explainability faces the bouncer problem](https://rdcu.be/b6qB4) - （《自然机器智能》第 2 卷，第 529-539 页）[（代码）](https://github.com/erwanlemerrer/bouncer_problem) *显示了远程人工智能决策的解释中的不可能性（通过一个请求）或难以发现。*
- [GeoDA: a geometric framework for black-box adversarial attacks](https://openaccess.thecvf.com/content_CVPR_2020/papers/Rahmati_GeoDA_A_Geometric_Framework_for_Black-Box_Adversarial_Attacks_CVPR_2020_paper.pdf) - （CVPR）[（代码）]（https://github.com/thisisalirah/GeoDA）*在纯黑盒设置中制作对抗性示例来愚弄模型（无梯度，仅推断类）。*
- [The Imitation Game: Algorithm Selectionby Exploiting Black-Box Recommender](https://github.com/erwanlemerrer/erwanlemerrer.github.io/raw/master/files/imitation_blackbox_recommenders_netys-2020.pdf) - (Netys) [(Code)](https://github.com/gdamaskinos/RecRank) *通过模仿远程且训练有素的决策来参数化本地推荐算法。*
- [Auditing News Curation Systems:A Case Study Examining Algorithmic and Editorial Logic in Apple News](https://ojs.aaai.org/index.php/ICWSM/article/view/7277) - (ICWSM) *对 Apple News 作为社会技术新闻管理系统的审计研究（热门故事部分）。*
- [Auditing Algorithms:  On Lessons Learned and the Risks of DataMinimization](https://dl.acm.org/doi/pdf/10.1145/3375627.3375852) - (AIES) *对 Telefónica 开发的健康推荐应用程序进行实际审核（主要是关于偏见）。*
- [Extracting Training Data from Large Language Models](https://arxiv.org/pdf/2012.07805) - (arxiv) *执行训练数据提取攻击，通过查询语言模型来恢复单个训练示例。*
### 2019
- [Adversarial Frontier Stitching for Remote Neural Network Watermarking](https://arxiv.org/abs/1711.01894) - （神经计算和应用）[（替代实现）]（https://github.com/dunky11/adversarial-frontier-stitching）*检查远程机器学习模型是否是“泄漏”模型：通过对远程模型的标准 API 请求，提取（或不提取）零位水印，该水印被插入到水印有价值的模型（例如大型深度神经网络）中。*
- [Knockoff Nets: Stealing Functionality of Black-Box Models](https://arxiv.org/abs/1812.02766.pdf) - （CVPR）*询问对手可以在多大程度上窃取此类仅基于黑盒交互的“受害者”模型的功能：图像输入，预测输出。*
- [Opening Up the Black Box:Auditing Google's Top Stories Algorithm](https://par.nsf.gov/servlets/purl/10101277) - (Flairs-32) *对 Google 热门故事面板的审计，提供对其用于选择和排名新闻发布商的算法选择的见解*
- [Making targeted black-box evasion attacks effective andefficient](https://arxiv.org/pdf/1906.03397.pdf) - (arXiv) *研究对手如何最佳地使用其查询预算来针对深度神经网络进行有针对性的规避攻击。*
- [Online Learning for Measuring Incentive Compatibility in Ad Auctions](https://research.fb.com/wp-content/uploads/2019/05/Online-Learning-for-Measuring-Incentive-Compatibility-in-Ad-Auctions.pdf) - （WWW）*衡量黑盒拍卖平台的激励兼容（IC）机制（遗憾）。*
- [TamperNN: Efficient Tampering Detection of Deployed Neural Nets](https://arxiv.org/abs/1903.00317) - (ISSRE) *制作输入的算法可以检测远程执行的分类器模型的篡改。*
- [Neural Network Model Extraction Attacks in Edge Devicesby Hearing Architectural Hints](https://arxiv.org/pdf/1903.03916.pdf) - (arxiv) *通过总线监听获取内存访问事件，通过LSTM-CTC模型识别层序列，根据内存访问模式进行层拓扑连接，以及数据量限制下的层维数估计，证明可以准确地恢复出类似的网络架构作为攻击起点*
- [Stealing Knowledge from Protected Deep Neural Networks Using Composite Unlabeled Data](https://ieeexplore.ieee.org/abstract/document/8851798) - (ICNN) *复合方法可用于攻击和提取黑盒模型的知识，即使它完全隐藏其 softmax 输出。*
- [Neural Network Inversion in Adversarial Setting via Background Knowledge Alignment](https://dl.acm.org/citation.cfm?id=3354261) - (CCS) *对手环境中的模型反转方法基于训练充当原始模型的逆模型的反转模型。在不完全了解原始训练数据的情况下，通过从更通用的数据分布中提取的辅助样本训练反演模型，仍然可以实现准确的反演。*
### 2018
- [Counterfactual Explanations without Opening the Black Box: Automated Decisions and the GDPR](https://arxiv.org/abs/1711.00399) - （哈佛法律与技术杂志）*为了解释关于 x 的决定，请找到一个对事实：最接近 x 的点会改变决定。*
- [Distill-and-Compare: Auditing Black-Box Models Using Transparent Model Distillation](https://arxiv.org/abs/1710.06169) - (AIES) *将黑盒模型视为老师，训练透明的学生模型来模仿黑盒模型分配的风险评分。*
- [Towards Reverse-Engineering Black-Box Neural Networks](https://arxiv.org/abs/1711.01768) - (ICLR) [(代码)](https://github.com/coallaoh/WhitenBlackBox) *通过分析远程神经网络模型对某些输入的响应模式来推断其内部超参数（例如层数、非线性激活类型）。*
- [Data driven exploratory attacks on black box classifiers in adversarial domains](https://www.sciencedirect.com/science/article/pii/S092523121830136X) - （神经计算）*对远程分类器模型进行逆向工程（例如，用于逃避验证码测试）。*
- [xGEMs: Generating Examplars to Explain Black-Box Models](https://arxiv.org/pdf/1806.08867.pdf) - (arXiv) *通过训练无监督的隐式生成模型来搜索黑盒模型中的偏差。然后通过沿着数据流形扰动数据样本来定量总结黑盒模型的行为。*
- [Learning Networks from Random Walk-Based Node Similarities](https://arxiv.org/pdf/1801.07386) - (NIPS) *通过观察一些随机游走通勤时间来反转图表。*
- [Identifying the Machine Learning Family from Black-Box Models](https://rd.springer.com/chapter/10.1007/978-3-030-00374-6_6) - (CAEPIA) *确定返回的预测背后是哪种机器学习模型。*
- [Stealing Neural Networks via Timing Side Channels](https://arxiv.org/pdf/1812.11720.pdf) - (arXiv) *通过使用查询的计时攻击窃取/近似模型。*
- [Copycat CNN: Stealing Knowledge by Persuading Confession with Random Non-Labeled Data](https://arxiv.org/abs/1806.05476) - （IJCNN）[（代码）]（https://github.com/jeiks/Stealing_DL_Models）*通过使用随机自然图像（ImageNet 和 Microsoft-COCO）查询黑盒模型（CNN）知识来窃取它们。*
- [Auditing the Personalization and Composition of Politically-Related Search Engine Results Pages](https://dl.acm.org/doi/10.1145/3178876.3186143) - (WWW) *Chrome 扩展程序，用于调查参与者并收集搜索引擎结果页面 (SERP) 和自动完成建议，用于研究个性化和组合。*
### 2017
- [Uncovering Influence Cookbooks : Reverse Engineering the Topological Impact in Peer Ranking Services](https://dl.acm.org/authorize.cfm?key=N21772) - (CSCW) *旨在确定同行排名服务中使用哪些中心性指标。*
- [The topological face of recommendation: models and application to bias detection](https://arxiv.org/abs/1704.08991) - （复杂网络）*为向用户推荐的项目提出了偏差检测框架。*
- [Membership Inference Attacks Against Machine Learning Models](http://ieeexplore.ieee.org/document/7958568/) - （安全与隐私研讨会）*给定一个机器学习模型和一条记录，确定该记录是否用作模型训练数据集的一部分。*
- [Practical Black-Box Attacks against Machine Learning](https://dl.acm.org/citation.cfm?id=3053009) - （亚洲 CCS）*了解远程服务如何容易受到对抗性分类攻击。*
### 2016
- [Algorithmic Transparency via Quantitative Input Influence: Theory and Experiments with Learning Systems](https://www.andrew.cmu.edu/user/danupam/datta-sen-zick-oakland16.pdf) - (IEEE S&P) *使用 shapley 值评估特征对模型的个体、联合和边际影响。*
- [Auditing Black-Box Models for Indirect Influence](https://arxiv.org/abs/1602.07043) - (ICDM) *通过“巧妙地”从数据集中删除变量并查看准确度差距来评估变量对黑盒模型的影响*
- [Iterative Orthogonal Feature Projection for Diagnosing Bias in Black-Box Models](https://arxiv.org/abs/1611.04967) - （FATML 研讨会）*执行特征排名来分析黑盒模型*
- [Bias in Online Freelance Marketplaces: Evidence from TaskRabbit](http://datworkshop.org/papers/dat16-final22.pdf) - （dat 研讨会）*测量 TaskRabbit 的搜索算法排名。*
- [Stealing Machine Learning Models via Prediction APIs](https://www.usenix.org/conference/usenixsecurity16/technical-sessions/presentation/tramer) - (Usenix Security) [(Code)](https://github.com/ftramer/Steal-ML) *旨在提取远程服务使用的机器学习模型。*
- [“Why Should I Trust You?”Explaining the Predictions of Any Classifier](https://arxiv.org/pdf/1602.04938v3.pdf) - (arXiv) [(代码)](https://github.com/marcotcr/lime-experiments) *通过对数据实例进行采样来解释黑盒分类器模型。*
- [Back in Black: Towards Formal, Black Box Analysis of Sanitizers and Filters](http://ieeexplore.ieee.org/document/7546497/) - （安全和隐私）*消毒剂和过滤器的黑盒分析。*
- [Algorithmic Transparency via Quantitative Input Influence: Theory and Experiments with Learning Systems](http://ieeexplore.ieee.org/document/7546525/) - （安全和隐私）*引入了捕获输入对观察系统输出的影响程度的措施。*
- [An Empirical Analysis of Algorithmic Pricing on Amazon Marketplace](https://mislove.org/publications/Amazon-WWW.pdf) - (WWW) [(Code)](http://personalization.ccs.neu.edu) *开发一种检测算法定价的方法，并根据经验使用它来分析其在亚马逊市场上的流行程度和行为。*
### 2015
- [Certifying and Removing Disparate Impact](https://arxiv.org/abs/1412.3756) - (SIGKDD) *提出基于 SVM 的方法来证明不存在偏差以及从数据集中消除偏差的方法。*
- [Peeking Beneath the Hood of Uber](https://dl.acm.org/citation.cfm?id=2815681) - (IMC) *推断 Uber 激增价格算法的实施细节。*
### 2014
- [窥探黑匣子：通过随机化探索分类器]() - （数据挖掘和知识发现期刊）（[代码](https://github.com/tsabsch/goldeneye)) *查找可以在不更改预测样本的输出标签的情况下进行排列的特征组*
- [XRay: Enhancing the Web's Transparency with Differential Correlation](https://www.usenix.org/node/184394) - （USENIX 安全）*审核哪些用户配置文件数据用于定位特定广告、推荐或价格。*
### 2013
- [Measuring Personalization of Web Search](https://dl.acm.org/citation.cfm?id=2488435) - (WWW) *开发一种衡量网络搜索结果个性化的方法。*
- [Auditing: Active Learning with Outcome-Dependent Query Costs](https://www.cs.bgu.ac.il/~sabatos/papers/SabatoSarwate13.pdf) - (NIPS) *从二元分类器中学习，只需为负标签付费。*

### 2012
- [Query Strategies for Evading Convex-Inducing Classifiers](http://www.jmlr.org/papers/v13/nelson12a.html) - (JMLR) *凸分类器的规避方法。考虑规避复杂性。*
### 2008
- [Privacy Oracle: a System for Finding Application Leakswith Black Box Differential Testing](https://dl.acm.org/citation.cfm?id=1455806) - (CCS) *Privacy Oracle：一种发现应用程序在传输到远程服务器时泄露个人信息的系统。*
### 2005
- [Adversarial Learning](https://dl.acm.org/citation.cfm?id=1081950) - (KDD) *使用成员资格查询对远程线性分类器进行逆向工程。*

## 相关活动

### 2025
* [AIMLAI 参加 ECML/PKDD 2025](https://project.inria.fr/aimlai/)
* [AAAI 人工智能治理研讨会：联盟、道德和法律](https://aaai.org/conference/aaai/aaai-25/workshop-list/#ws06)

### 2024
* [第一届审计与人工智能国际会议](https://www.ircg.msm.uni-due.de/ai/)
* [可调节机器学习研讨会 (RegML'24)](https://regulatableml.github.io/)

### 2023
* [支持用户参与测试、审核和竞争 AI（CSCW 用户 AI 审核）](https://cscw-user-ai-auditing.github.io/)
* [算法的算法审计研讨会（WAAA）](https://algorithmic-audits.github.io)
* [可调节机器学习研讨会 (RegML'23)](https://regulatableml.github.io/)
