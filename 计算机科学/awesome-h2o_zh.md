# 很棒的水 [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

[<img src =“https://rawgit.com/h2oai/awesome-h2o/master/h2o_logo.png”align =“right”width =“100”>]（https://github.com/h2oai/h2o-3）

以下是使用 [H2O](https://github.com/h2oai/h2o-3)（一个开源分布式机器学习平台）的所有精彩项目、应用程序、研究、教程、课程和书籍的精选列表。  H2O 提供许多监督和无监督机器学习算法的并行实现，例如广义线性模型、梯度提升机（包括 XGBoost）、随机森林、深度神经网络（深度学习）、堆叠集成、朴素贝叶斯、Cox 比例风险、K 均值、PCA、Word2Vec 以及全自动机器学习算法 (AutoML)。

[H2O.ai](http://www.h2o.ai/about/) 制作了许多关于 H2O 的[教程](https://github.com/h2oai/h2o-tutorials)、[博客文章](http://blog.h2o.ai/)、[演示文稿](https://github.com/h2oai/h2o-meetups) 和[视频](https://www.youtube.com/user/0xdata)，但是下面的列表由更大的 H2O 用户社区制作的精彩内容组成。

我们刚刚开始使用此列表，因此非常感谢拉取请求！  🙏 请在提出拉取请求之前查看[贡献指南](contributing.md)。  如果您不是 GitHub 用户并想做出贡献，请发送电子邮件至community@h2o.ai。

如果你也觉得 H2O 很棒，请 ⭐ [H2O GitHub 存储库](https://github.com/h2oai/h2o-3/)。

## 内容

- [博客文章和教程](#blog-posts--tutorials)
- [Books](#books)
- [研究论文](#research-papers)
- [Benchmarks](#benchmarks)
- [Presentations](#presentations)
- [Courses](#courses)
- [软件（使用 H2O 构建）](#software)
- [License](#license)

## 博客文章和教程

- [使用 H2O AutoML 简化训练过程（并预测葡萄酒质量）](https://enjoymachinelearning.com/posts/h2o-auto-machine-learning/) 2020 年 8 月 4 日
- [使用 LIME 可视化 ML 模型](https://uc-r.github.io/lime)
- [H2O 中的并行网格搜索](https://www.pavel.cool/h2o-3/h2o-parallel-grid-search/) 2020 年 1 月 17 日
- [在 H2O 中使用 MOJO 模型导入、检查和评分](https://www.pavel.cool/h2o-3/h2o-mojo-import/) 2019 年 12 月 10 日
- [H2O.ai 让人工智能变得简单：在 Python 中使用 H2O.ai 和 AutoML 进行建模的综合指南](https://towardsdatascience.com/artificial-intelligence-made-easy-187ecb90c299) 2019 年 6 月 12 日
- [使用 H2O 的隔离森林进行异常检测](https://dzone.com/articles/anomaly-detection-with-isolation-forests-using-h2o-1) 2018 年 12 月 3 日
- [使用食谱预测布拉迪斯拉发的住宅物业价格 - H2O 机器学习](https://www.michal-kapusta.com/post/2018-11-02-predicting-residential-property-prices-in-bratislava-using-recipes-h2o-machine-learning-part-ii/) 2018 年 11 月 25 日
- [在 H2O 中检查决策树](https://dzone.com/articles/inspecting-decision-trees-in-h2o) 2018 年 11 月 7 日
- [H2O.ai 对 AutoML 的简单介绍](https://medium.com/analytics-vidhya/gentle-introduction-to-automl-from-h2o-ai-a42b393b4ba2) 2018 年 9 月 13 日
- [H2O 机器学习 — 数据科学家实践指南](https://dzone.com/articles/machine-learning-with-h2o-hands-on-guide-for-data) 2018 年 6 月 27 日
- [使用 LIME 机器学习来了解员工流失情况](http://www.business-science.io/business/2018/06/25/lime-local-feature-interpretation.html) 2018 年 6 月 25 日
- [大规模分析：AWS EMR 上的 h2o、Apache Spark 和 R](https://redoakstrategic.com/h2oaws/) 2018 年 6 月 21 日
- [癌症检测中自动化且不神秘的机器学习](https://kkulma.github.io/2017-11-07-automated_machine_learning_in_cancer_detection/) 2017 年 11 月 7 日
- [使用 h2o+timetk 进行时间序列机器学习](http://www.business-science.io/code-tools/2017/10/28/demo_week_h2o.html) 2017 年 10 月 28 日
- [销售分析：如何使用机器学习来预测和优化产品缺货](http://www.business-science.io/business/2017/10/16/sales_backorder_prediction.html) 2017 年 10 月 16 日
- [人力资源分析：利用机器学习预测员工流动率](http://www.business-science.io/business/2017/09/18/hr_employee_attrition.html) 2017 年 9 月 18 日
- [欺诈分析中机器学习的自动编码器和异常检测](https://shiring.github.io/machine_learning/2017/05/01/fraud) 2017 年 5 月 1 日
- [使用 h2o 和 rsparkling 构建预测心律失常的深度神经网络](https://shiring.github.io/machine_learning/2017/02/27/h2o) 2017 年 2 月 27 日
- [使用 Sparklyr（机器学习）预测食物偏好](https://shiring.github.io/machine_learning/2017/02/19/food_spark) 2017 年 2 月 19 日
- [将大量数据从 R 移动到 H2O - 使用安然电子邮件进行垃圾邮件检测](https://ellisp.github.io/blog/2017/02/18/svmlite) 2016 年 2 月 18 日
- [使用 R 中的 mxnet、h2o 包进行深度学习和参数调整](http://blog.hackerearth.com/understand-deep-learning-parameter-tuning-with-mxnet-h2o-package-in-r) 2017 年 1 月 30 日

## 书籍

- [精神病学和神经病学中的大数据，第 11 章：可扩展的药物摄入监测系统](https://www.elsevier.com/books/big-data-in-psychiatry-and-neurology/moustafa/978-0-12-822884-5) Diane Myung-Kyung Woodbridge 和 Kevin Bengtson Wong。 (2021)
- [R 时间序列实践](https://www2.packtpub.com/big-data-and-business-intelligence/hands-time-series-analysis-r) Rami Krispin。 (2019)
- [使用 Spark 2.x 掌握机器学习](https://www.packtpub.com/product/mastering-machine-learning-with-spark-2-x/9781785283451) Alex Tellez、Max Pumperla、Michal Malohlava。 (2017)
- [使用 R 进行机器学习](https://www.amazon.com/Machine-Learning-Using-Karthik-Ramasubramanian/dp/1484223330) Karthik Ramasubramanian、Abhishek Singh。 (2016)
- [H2O 实用机器学习：强大、可扩展的深度学习和人工智能技术](https://www.amazon.com/Practical-Machine-Learning-H2O-Techniques/dp/149196460X) Darren Cook。 (2016)
- [颠覆性分析](http://link.springer.com/book/10.1007/978-1-4842-1311-7) Thomas Dinsmore。 (2016)
- [计算机时代统计推断：算法、证据和数据科学](https://web.stanford.edu/~hastie/CASI/) Bradley Efron、Trevor Hastie。 (2016)
- [R 深度学习基础](https://www.packtpub.com/big-data-and-business-intelligence/r-deep-learning-essentials) Joshua F. Wiley。 (2016)
- [Spark 行动](https://www.manning.com/books/spark-in-action) Petar Zečević、Marko Bonaći。 (2016)
- [大数据手册](https://www.crcpress.com/Handbook-of-Big-Data/Buhlmann-Drineas-Kane-van-der-Laan/p/book/9781482249071) Peter Bühlmann、Petros Drineas、Michael Kane、Mark J. van der Laan (2015)

## 研究论文

- [自动化机器学习：商业分析中人工智能驱动的决策](https://www.sciencedirect.com/science/article/pii/S2667305323000133) Marc Schmitt。 (2023)
- [基于 H2O AutoML 和可解释的 AI 技术的水质预测](https://www.mdpi.com/2073-4441/15/3/475) Hamza Ahmad Madni、Muhammad Umer、Abid Ishaq、Nihal Abuzinadah、Oumaima Saidani、Shtwai Alsubai、Monia Hamdi、Imran Ashraf。 (2023)
- [选择哪个型号？从高分辨率卫星气溶胶光学深度预测 PM2.5 的统计模型和机器学习模型的性能比较](https://www.sciencedirect.com/science/article/abs/pii/S1352231022002291?dgcid=coauthor) Padmavati Kulkarnia、V.Sreekantha、Adithi R.Upadhyab、Hrishikesh ChandraGautama。  (2022)
- [对急诊科疑似急性感染和脓毒症患者的转录组严重程度分类器进行前瞻性验证](https://pubmed.ncbi.nlm.nih.gov/35467566/) Noa Galtung、Eva Diehl-Wiesenecker、Dana Lehmann、Natallia Markmann、Wilma H Bergström、James Wacker、Oliver Liesenfeld、Michael Mayhew、Ljubomir Buturovic，罗兰·鲁西、蒂莫西·E·斯威尼、鲁道夫·陶伯、凯·卡珀特、拉詹·索马孙达拉姆、沃尔夫冈·鲍尔。 (2022)
- [COVID-19 大流行期间帕金森病患者的抑郁水平预测](https://embc.embs.org/2021/)) Hashneet Kaur、Patrick Ka-Cheong Poon、Sophie Yuefei Wang、Diane Myung-kyung Woodbridge。 (2021)
- [对健康参与者使用连续血糖监测进行基于机器学习的膳食检测：参与者遵守协议的客观衡量标准](https://embc.embs.org/2021/) Victor Palacios、Diane Myung-kyung Woodbridge、Jean L. Fry。 (2021)
- [灰质结构和白质连接体的成熟度及其与青少年精神症状的关系](https://onlinelibrary.wiley.com/doi/full/10.1002/hbm.25565) Alex Luna, Joel Bernanke, Kakyeong Kim, Natalie Aw, Jordan D. Dworkin, Jiook Cha, Jonathan Posner (2021)。
- [意大利 COVID-19 大流行期间的阑尾切除术：意大利内窥镜外科和新技术协会开展的多中心双向队列研究（CRAC 研究）](https://pubmed.ncbi.nlm.nih.gov/34219197/) Alberto Sartori、Mauro Podda、Emanuele Botteri、Roberto Passera、Ferdinando Agresta、Alberto Arezzo。 (2021)
- [通过机器学习预测加拿大 GDP 增长](https://carleton.ca/economics/wp-content/uploads/cewp21-05.pdf) Shafiullah Qureshi、Ba Chu、Fanny S. Demers。 (2021)
- [珊瑚礁的形态特征可预测灭绝风险，但不能预测保护状态](https://onlinelibrary.wiley.com/doi/10.1111/geb.13321) Nussaïbah B. Raja、Andreas Lauchstedt、John M. Pandolfi、Sun W. Kim、Ann F. Budd、Wolfgang Kiessling。 (2021)
- [机器学习作为改进房价预测的工具](https://openaccess.nhh.no/nhh-xmlui/bitstream/handle/11250/2739783/masterthesis.pdf?sequence=1) Henrik I W. Wolstad 和 Didrik Dewan。 (2020)
- [公民科学数据显示河流前哨无脊椎动物因温度而下降](https://pubs.acs.org/doi/10.1021/acs.estlett.0c00206) Timothy J. Maguire、Scott O. C. Mundle。 (2020)
- [利用神经网络和梯度增强机预测邮政投递延误风险](https://www.diva-portal.org/smash/get/diva2:1467609/FULLTEXT01.pdf) Matilda Söderholm。 (2020)
- [使用堆叠集成学习方法进行股票市场分析](https://github.com/malhartakle/MastersDissertation/blob/master/Research%20Project%20Report.pdf) Malkar Takle。 (2020)
- [H2O AutoML：可扩展的自动机器学习](https://www.automl.org/wp-content/uploads/2020/07/AutoML_2020_paper_61.pdf)。艾琳·勒德尔，塞巴斯蒂安·普瓦里尔。  (2020)
- [外周血单细胞质谱流式细胞仪识别与原发性胆汁性胆管炎相关的免疫细胞亚群](https://www.nature.com/articles/s41598-020-69358-4) Jin Sung Jang, Brian D. Juran, Kevin Y. Cunningham, Vinod K. Gupta, Young Min Son, Ju Dong Yang, Ahmad H. Ali, Elizabeth Ann L. Enninga, Jaeyun宋和康斯坦丁诺斯·N·拉扎里迪斯。 (2020)
- [使用 BRCA-ML 预测 BRCA1 和 BRCA2 中错义变异的功能影响](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7190647/) Steven N. Hart、Eric C. Polley、Hermella Shimelis、Siddhartha Yadav、Fergus J. Couch。 (2020)
- [用于预测个体树高和胸径之间关系的创新深度学习人工智能应用](https://doi.org/10.1186/s40663-020-00226-3) ilker Ercanlı。 (2020)
- [开源 AutoML 基准](https://www.automl.org/wp-content/uploads/2019/06/automlws2019_Paper45.pdf)Peter Gijsbers、Erin LeDell、Sebastien Poirier、Janek Thomas、Berndt Bischl、Joaquin Vanschoren。 (2019)
- [Python 中的机器学习：数据科学、机器学习和人工智能的主要发展和技术趋势](https://arxiv.org/abs/2002.04803) Sebastian Raschka、Joshua Patterson、Corey Nolet。 (2019)
- [多摄像机视点视频场景中的人体动作识别](https://www.sciencedirect.com/science/article/pii/S1389041718308970) Fernando Itano, Ricardo Pires, Miguel Angelo de Abreu de Sousa, Emilio Del-Moral-Hernandeza。 (2019)
- [使用遗传算法扩展 MLP ANN 超参数优化](https://ieeexplore.ieee.org/document/8489520/authors#authors) Fernando Itano, Miguel Angelo de Abreu de Sousa, Emilio Del-Moral-Hernandez。 (2018)
- [askMUSIC：利用临床登记系统开发新的机器学习模型，告知患者类似男性选择的前列腺癌治疗方法](https://doi.org/10.1016/j.eururo.2018.09.050) Gregory B. Auffenberg、Khurshid R. Ghani、Shreyas Ramani、Etiowo Usoro、Brian Denton、Craig Rogers、Benjamin斯托克顿、大卫·C·米勒、卡兰迪普·辛格。 (2018)
- [执行定价优化的机器学习方法。  与标准 GLM 的比较](http://www.variancejournal.org/articlespress/articles/Machine-Spedicato.pdf) Giorgio Alfredo Spedicato、Christophe Dutang 和 Leonardo Petrini。 (2018)
- [H2O 平台上各种激活函数的神经网络架构的性能比较分析](https://arxiv.org/abs/1707.04940) Yuriy Kochura、Sergii Stirenko、Yuri Gordienko。 (2017)
- [在高频数据上使用深度神经网络的算法交易](https://link.springer.com/chapter/10.1007/978-3-319-66963-2_14) Andrés Arévalo、Jaime Niño、German Hernandez、Javier Sandoval、Diego León、Arbey Aragón。 (2017)
- [项圈标签上的通用在线动物活动识别](https://dl.acm.org/itation.cfm?id=3124407) Jacob W. Kamminga、Helena C. Bisby、Duc V. Le、Nirvana Meratnia、Paul J. M.havinga。 (2017)
- [撒哈拉以南非洲土壤养分图：利用机器学习评估 250 m 空间分辨率的土壤养分含量](https://link.springer.com/content/pdf/10.1007%2Fs10705-017-9870-x.pdf) Tomislav Hengl, Johan G. B. Leenaars, Keith D. Shepherd, Markus G. Walsh, Gerard B. M. Heuvelink、Tekalign Mamo、Helina Tilahun、Ezra Berkhout、Matthew Cooper、Eric Fegraus、Ichsani Wheeler、Nketia A. Kwabena。 (2017)
- [数据依赖性随机中介效应的稳健和灵活估计：随机试验环境中提出的方法和示例](https://arxiv.org/pdf/1707.09021.pdf) Kara E. Rudolph、Oleg Sofrygin、Wenjing Cheng 和 Mark J. van der Laan。 (2017)
- [因果推理的自动化方法与自己动手方法：从数据分析竞赛中吸取的教训](https://arxiv.org/abs/1707.02641) Vincent Dorie、Jennifer Hill、Uri Shalit、Marc Scott、Dan Cervone。 (2017)
- [利用深度学习预测白血病患者死亡率](https://qspace.library.queensu.ca/bitstream/handle/1974/15929/Muthalaly_Reena%20S_201707_MSC.pdf) Reena Shaw Muthalaly。 (2017)
- [使用机器学习框架预测药物滥用障碍治疗的成功](http://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0175383&type=printable) Laura Acion、Diana Kelmansky、Mark van der Laan、Ethan Sahker、DeShauna Jones、Stephan Arnd。 (2017)
- [使用深度学习对信道响应数据进行超宽带天线引起的误差预测](https://www.kn.e-technik.tu-dortmund.de/.cni-bibliography/publications/cni-publications/Tiemann2017a.pdf)Janis Tiemann、Johannes Pillmann、Christian Wietfeld。 (2017)
- [从通勤特征旅行矩阵推断乘客类型](http://www.tandfonline.com/doi/abs/10.1080/21680566.2017.1291377?journalCode=ttrb20) Erika Fille T. Legara，Christopher P. Monterola。 (2017)
- [深度神经网络、梯度增强树、随机森林：标准普尔 500 指数的统计套利](http://www.sciencedirect.com/science/article/pii/S0377221716308657) Christopher Krauss、Xuan Anh Doa、Nicolas Huckb。 (2016)
- [利用深度学习识别巴西政府采购系统中的 IT 采购异常](http://ieeexplore.ieee.org/document/7838233/?reload=true) Silvio L. Domingos、Rommel N. Carvalho、Ricardo S. Carvalho、Guilherme N. Ramos。 (2016)
- [预测巴西银行信贷业务的恢复](http://ieeexplore.ieee.org/abstract/document/7838243/) Rogério G. Lopes、Rommel N. Carvalho、Marcelo Ladeira、Ricardo S. Carvalho。 (2016)
- [深度学习异常检测支持巴西出口和反洗钱欺诈调查](http://ieeexplore.ieee.org/abstract/document/7838276/) Ebberth L. Paula、Marcelo Ladeira、Rommel N. Carvalho、Thiago Marzagão。 (2016)
- [用于预测癌症药物反应的深度学习和关联规则挖掘](https://doi.org/10.1101/070490) Konstantinos N. Vougas、Thomas Jackson、Alexander Polyzos、Michael Liontos、Elizabeth O. Johnson、Vassilis Georgoulias、Paul Townsend、Jiri Bartek、Vassilis G. Gorgoulis。 (2016)
- [兴趣点信息在预测具有成本效益的充电基础设施位置方面的价值](http://www.rsm.nl/fileadmin/Images_NEW/ECFEB/The_value_of_points_of_interest_information.pdf) Stéphanie Florence Visser。 (2016)
- [土壤分类单元空间多样化的自适应建模。水土开发杂志](https://www.degruyter.com/downloadpdf/j/jwld.2016.30.issue-1/jwld-2016-0029/jwld-2016-0029.xml) Krzysztof Urbański、Stanisław Gruszczyńsk。 (2016)
- [可扩展的集成学习和计算高效的方差估计](http://www.stat.berkeley.edu/~ledell/papers/ledell-phd-thesis.pdf) Erin LeDell。 (2015)
- [Superchords：解码毫秒范围内的脑电图信号](https://doi.org/10.7287/peerj.preprints.1265v1) Rogerio Normand，Hugo Alexandre Ferreira。 (2015)
- [理解随机森林：从理论到实践](https://github.com/glouppe/phd-thesis) Gilles Louppe。 (2014)

## 基准测试

- [Are categorical variables getting lost in your random forests?](http://roamanalytics.com/2016/10/28/are-categorical-variables-getting-lost-in-your-random-forests/) - 分类编码方案的基准以及对基于树的模型的影响（Scikit-learn 与 H2O）。 2016 年 10 月 28 日
- [Deep learning in R](http://www.rblog.uni-freiburg.de/2017/02/07/deep-learning-in-r/) - R 中开源深度学习包的基准测试。2016 年 3 月 7 日
- [Szilard's machine learning benchmark](https://github.com/szilard/benchm-ml) - 常见开源 ML 框架中随机森林、GBM、深度学习和 GLM 实现的基准。 2015 年 7 月 3 日

## 演讲

- [模型部署管道](https://www.slideshare.net/rocalabern/digital-origin-pipelines-for-model-deployment) 2017 年 4 月 25 日
- [使用 H2O.ai 进行机器学习](https://speakerdeck.com/szilard/machine-learning-with-h2o-dot-ai-la-h2o-meetup-at-at-and-t-jan-2017) 2017 年 1 月 23 日

## 课程

- [University of San Francisco (USF) Distributed Data System Class (MSDS 697)](https://github.com/dianewoodbridge/2020-msds697-example) - 数据科学项目理学硕士。
- [University of Oslo: Introduction to Automatic and Scalable Machine Learning with H2O and R](https://www.ub.uio.no/english/courses-events/events/all-libraries/2019/research-bazaar-2019.html) - 2019年研究义卖会
- [UCLA: Tools in Data Science (STATS 418)](https://github.com/szilard/teach-data-science-UCLA-master-appl-stats) - 应用统计学硕士课程。
- [GWU: Data Mining (Decision Sciences 6279)](https://github.com/jphall663/GWU_data_mining) - 商业分析理学硕士。
- [University of Cape Town: Analytics Module](http://www.stats.uct.ac.za/stats/study/postgrad/honours) - 统计科学研究生荣誉课程。
- [Coursera: How to Win a Data Science Competition: Learn from Top Kagglers](https://www.coursera.org/learn/competitive-data-science) - 高级机器学习专业。

## 软件

- [modeltime.h2o R 包](https://business-science.github.io/modeltime.h2o/)：使用 H2O AutoML 进行预测
- [Evaporate](https://github.com/ML4LHS/Evaporate)：通过 Javascript 在浏览器中运行 H2O 模型。  更多信息[此处](https://twitter.com/kdpsinghlab/status/1367992786239242248)。
- [splash R package](https://github.com/ML4LHS/splash)：将用户界面添加到 H2O MOJO 文件上。  更多信息[此处](https://twitter.com/kdpsinghlab/status/1367809740705792008)。
- [h2oparsnip R 包](https://github.com/stevenpawley/h2oparsnip)：一组包装器，用于将 h2o 算法与 [parsnip](https://parsnip.tidymodels.org/) 包绑定。
- [在 AWS 上启动 PySpark 和 PySparkling](https://github.com/kcrandall/EMR_Spark_Automation)
- [预测美国电力需求](https://github.com/RamiKrispin/USelectricity)：美国电力需求的实时[仪表板](https://ramikrispin.github.io/USelectricity/)（使用H2O GLM预测）
- [h2o3-pam](https://github.com/navdeep-G/h2o3-pam)：H2O-3 中的围绕 Mediods 分区 (PAM) 聚类算法
- [h2o3-gapstat](https://github.com/navdeep-G/h2o3-gapstat): H2O-3 中的间隙统计算法

## 许可证

[![CC0](https://upload.wikimedia.org/wikipedia/commons/6/69/CC0_button.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

在法律允许的范围内，[H2O.ai](http://h2o.ai) 已放弃本作品的所有版权以及相关或邻接权。
