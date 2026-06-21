# 很棒的细胞数据 [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> 精彩细胞数据资源的精选列表。

![细胞数据徽标](cytodata-logo.png)

[Cytodata](https://cytodata.org/) 是指参与**生物表型**的**基于图像分析**的研究人员和资源社区。
这些**生物表型**通常是由遗传或化学扰动引起的，并且通常代表疾病状态。
**基于图像的分析**用于检查这些表型，以揭示生物学见解，包括发现遗传改变的影响和确定化合物的作用机制。

此页面展示了软件、数据集、里程碑出版物和基于图像的分析方法的精选列表。
我们的目标是为新老研究人员提供一个发现和记录出色的细胞数据资源的地方。

## 内容

- [Datasets](#datasets)
  - [原始图像](#raw-images)
  - [化学扰动](#chemical-perturbations)
  - [遗传扰动](#genetic-perturbations)
- [Software](#software)
- [Publications](#publications)
  - [Reviews](#reviews)
  - [Applications](#applications)
  - [Methods](#methods)

## 数据集

带注释的数据集，包括**原始图像**和**处理后的配置文件**，用于基于图像的化学和遗传扰动分析。

### 原始图像
- [The Cell Painting Gallery](https://broad.io/CellPaintingGallery) - 细胞绘画画廊是使用细胞绘画分析（或类似方法）创建的图像数据集的集合；它由布罗德研究所的卡彭特-辛格实验室维护。
- [Broad Bioimage Benchmark Collection](https://data.broadinstitute.org/bbbc/) - Broad Bioimage Benchmark Collection (BBBC) 是可免费下载的显微镜图像集的集合。除了图像本身之外，每组还包括生物应用的描述和某种类型的“基本事实”（预期结果）。
- [Image Data Resource](https://idr.openmicroscopy.org/) - 来自已发表科学研究的图像数据集的公共存储库。
- [RxRx1](https://www.rxrx.ai/rxrx1) - RxRx1 是一组 125,514 张高分辨率 512x512 6 通道荧光显微镜图像，这些图像是在 4 种细胞类型的 51 个实验批次中，在 1,108 种遗传扰动下的人类细胞的图像。  这些图像由 Recursion Pharmaceuticals 在犹他州盐湖城的实验室中制作。  研究人员将使用该数据集来研究和基准测试处理生物批次效应的方法，以及领域适应、迁移学习和 k-shot 学习等机器学习领域。
- [RxRx19](https://www.rxrx.ai/rxrx19) - RxRx19 是第一个展示了 COVID-19 形态学效应的拯救的形态学数据集。
- [Human Protein Atlas](https://www.proteinatlas.org/humanproteome/subcellular) - 在其他测定中，HPA 进行共聚焦成像，显示细胞系中超过 2/3 的人类蛋白质的位置。可以下载[原始图像](https://github.com/CellProfiling/HPA-competition#script-to-download-hpav18)或[推断的蛋白质亚细胞位置](https://www. Proteinatlas.org/about/download)。

### 化学扰动

- [Gustafsdottir et al. 2013](https://doi.org/10.1371/journal.pone.0080999) - U2OS 细胞中 1,600 种生物活性化合物的细胞绘制概况（从公共 S3 存储桶访问：`s3://cytodata/datasets/Bioactives-BBBC022-Gustafsdottir/profiles/Bioactives-BBBC022-Gustafsdottir/`）。
- [Wawer et al. 2014](https://doi.org/10.1073/pnas.1410933111) - U2OS 细胞中 31,770 种化合物的细胞绘制谱（[点击下载](http://www.broadinstitute.org/mlpcn/data/Broad.PNAS2014.ProfilingData.zip)）。
- [Bray et al. 2017](https://doi.org/10.1093/gigascience/giw014) - U2OS 细胞中 30,616 种化合物的细胞绘制概况（中心驱动研究项目 _CDRP_）（[从 GigaDB 下载](https://doi.org/10.5524/100351) | 从公共 S3 存储桶访问：`s3://cytodata/datasets/CDRPBIO-BBBC036-Bray/profiles_cp/CDRPBIO-BBBC036-Bray/`）。
- [Haghighi et al. 2021](https://doi.org/10.1038/s41592-022-01667-0) - 细胞绘制在 4 个实验中与 L1000 配置文件相匹配，包括化合物和遗传筛选（[GitHub 上的详细信息](https://github.com/carpenterlab/2021_Haghighi_subscribed)）。

### 遗传扰动

- [Singh et al. 2015](https://doi.org/10.1371/journal.pone.0131370) - U2OS 细胞中通过 RNA 干扰 (RNAi) 敲除的 41 个基因的 3,072 个细胞绘制图谱（[从 GitHub 访问](https://github.com/carpenterlab/2016_bray_natprot/blob/6dcdcf72cd90bb2dbf238b3ecf94691246d8f104/supplementary_files/profiles.csv.zip)）。
- [Rohban et al. 2017](https://doi.org/10.7554/eLife.24060.001) - 来自 U2OS 细胞中 220 个过表达基因的细胞绘制数据（从公共 S3 存储桶访问：`s3://cytodata/datasets/TA-ORF-BBBC037-Rohban/profiles_cp/TA-ORF-BBBC037-Rohban/`）。
- 未发表 - A549 细胞中 53 个基因的 596 个过表达等位基因的细胞绘制图谱（从公共 S3 存储桶访问：`s3://cytodata/datasets/LUAD-BBBC043-Caicedo/profiles_cp/LUAD-BBBC043-Caicedo/`）
- 未发表 - 来自 CRISPR 实验的 3,456 个细胞绘制图谱，敲除 A549、ES2 和 HCC44 细胞中的 59 个基因（[从 GitHub 访问](https://github.com/broadinstitute/cell-health/tree/master/0.generate-profiles/data/profiles)）。

## 软件

用于基于图像的生物表型分析的开源软件包。

- [Advanced Cell Classifier](https://www.cellclassifier.org/) - 一个使用机器学习对大型数据集中的细胞进行探索、注释和分类的软件包。
- [CellProfiler](http://cellprofiler.org/) - CellProfiler 是一款免费的开源软件，用于测量和分析细胞图像。
- [CellProfiler Analyst](http://cellprofiler.org/cp-analyst/) - 大型生物图像集的交互式数据探索、分析和分类。
- [Cytominer](https://github.com/cytomining/cytominer) - R 中基于图像的细胞分析方法。
- [EBImage](https://github.com/aoles/EBImage) - R 的图像处理工具箱。
- [HTSvis](http://htsvis.dkfz.de/HTSvis/) - 用于探索性数据分析和阵列高通量屏幕可视化的 Web 应用程序。
- [BioProfiling.jl](https://github.com/menchelab/BioProfiling.jl) - 用于在 Julia 中过滤和管理形态特征的工具包。
- [PyCytominer](https://github.com/cytomining/pycytominer) - Python 中基于图像的细胞分析方法。
- [ImJoy](https://imjoy.io) - 一个平台编译工具，用于使用 GUI 进行基于深度学习的图像分析。
- [histoCAT](https://github.com/BodenmillerGroup/histoCAT) - 用于提取组织学和多重成像的定量表型描述符和上下文信息的工具箱。

## 刊物

与基于图像的分析相关的出版物。

### 评论

- [Image-based profiling for drug discovery: due for a machine-learning upgrade?](https://www.nature.com/articles/s41573-020-00117-w) - 从 Carpenter 实验室/制药公司的角度回顾 2020 年基于图像的分析应用。
- [Data-analysis strategies for image-based cell profiling](https://doi.org/10.1038/nmeth.4397) - 介绍从显微镜图像集合创建基于图像的高质量（即形态）剖面所需的步骤。
- [High-content screening for quantitative cell biology](https://doi.org/10.1016/j.tcb.2016.03.008) - 描述 HCS 的一些最新应用，从识别特定生物过程所需的基因到表征遗传相互作用。
- [Microscopy-based high-content screening](https://doi.org/10.1016/j.cell.2015.11.007) - 描述基于图像的筛选实验的最新技术，描述实验方法和图像分析方法，并讨论挑战和未来方向，包括利用 CRISPR/Cas9 介导的基因组工程。
- [Applications in image-based profiling of perturbations](https://doi.org/10.1016/j.copbio.2016.04.003) - 描述基于图像的分析的应用，包括目标和 MOA 识别、先导跳跃、文库富集、基因注释和疾病特异性表型的识别
- [Large-scale image-based screening and profiling of cellular phenotypes](https://doi.org/10.1002/cyto.a.22909) - 基于图像的分析概述，包括其应用和挑战。
- [How cells explore shape space: A quantitative statistical perspective of cellular morphogenesis](https://dx.doi.org/10.1002%2Fbies.201400011) - 基于定量描述符的细胞形状变化生物学讨论。
- [Machine learning and image-based profiling in drug discovery](https://doi.org/10.1016/J.COISB.2018.05.004) - 形态分析简介以及机器学习功能的讨论。
- [Pooled genetic screens with image-based profiling](https://doi.org/10.15252/msb.202110768) - 回顾可用于遗传筛选的不同模式以及哪些模式适合形态学分析。

### 收藏

- [Deep learning in microscopy](https://www.nature.com/collections/cfcdjceech) - 《自然方法》上发表的一系列评论和研究文章，涉及深度学习的多个用例，包括降噪、分割、跟踪和表示学习。
- [High-Content Imaging and Informatics](https://journals.sagepub.com/toc/jbxb/25/7) - SLAS Discovery 发表的高内涵成像方法及应用文章合集。

### 应用领域

- [Expanding the antibacterial selectivity of polyether ionophore antibiotics through diversity-focused semisynthesis](https://rdcu.be/ccBFH) - Poulsen 2020 年的实验室论文，其中根据细胞绘画测定测试了抗生素使哺乳动物细胞尽可能完整的能力。
- [Image-based multivariate profiling of drug responses from single cells](https://doi.org/10.1038/nmeth1032) - 一种基于~300 个单细胞表型测量结果对未处理和已处理人类癌细胞进行分类的多变量方法。
- [Discovering metabolic disease gene interactions by correlated effects on cellular morphology](https://doi.org/10.1016/j.molmet.2019.03.001) - 分析脂肪细胞分化过程中疾病与基因的相互作用。
- [Phenotypic profiling of the human genome by time-lapse microscopy reveals cell division genes](https://doi.org/10.1038/nature08869) - 这项研究提供了对细胞分裂表型的深入分析，并将整个高内容数据集作为资源提供给社区。
- [Bioactivity screening of environmental chemicals using imaging-based high-throughput phenotypic profiling](https://doi.org/10.1016/j.taap.2019.114876) - 使用基于图像的分析来筛选环境化学品的生物活性
- [Repurposing High-Throughput Image Assays Enables Biological Activity Prediction for Drug Discovery](https://doi.org/10.1016/j.chembiol.2018.01.015) - 使用基于图像的图谱来预测其他不相关测定中小分子的生物活性。
- [Tales of 1,008 Small Molecules: Phenomic Profiling through Live-cell Imaging in a Panel of Reporter Cell Lines](https://doi.org/10.1038/s41598-020-69354-8) - 展示多药理学在 MOA 预测中的影响，同时提供在未来基于图像的分析研究中克服该影响的解决方案。
- [Mapping the perturbome network of cellular perturbations](https://doi.org/10.1038/s41467-019-13058-9) - 基于图像的药物组合分析和网络分析。
- [Morphological profiling of human T and NK lymphocytes by high-content cell imaging](https://doi.org/10.1016/j.celrep.2021.109318) - 基于图像的免疫突触肌动蛋白组织分析。
- [A subcellular map of the human proteome](https://doi.org/10.1126/science.aal3321) - 根据人类蛋白质图谱的共焦显微镜图像对蛋白质亚细胞位置进行分类。
- [A multi-scale map of cell structure fusing protein images and interactions](https://doi.org/10.1038/s41586-021-04115-9) - 结合蛋白质的共焦成像和质谱表征来预测物理接近度并表征细胞组织。
- [Predicting cell health phenotypes using image-based morphology profiling](https://doi.org/10.1091/mbc.E20-12-0784) - 基于图像的概况作为细胞凋亡、增殖和其他细胞健康描述符的预测因子。
- [Systematic genetics and single‐cell imaging reveal widespread morphological pleiotropy and cell‐to‐cell variability](https://doi.org/10.15252/msb.20199243) - 分析单细胞概况以表征变异性、多效性和不完全外显率。
- [Large‐scale image‐based profiling of single‐cell phenotypes in arrayed CRISPR‐Cas9 gene perturbation screens](https://doi.org/10.15252/msb.20178064) - 展示了成像阵列 CRISPR 筛选的可行性，并提供了一种表征单个细胞转染功效的方法。
- [Multiparametric phenotyping of compound effects on patient derived organoids](https://doi.org/10.1038/s41467-022-30722-9) - 分析对患者来源的类器官的化学影响。
- [A chemical-genetic interaction map of small molecules using high-throughput imaging in cancer cells](https://doi.org/10.15252/MSB.20156400) - 分析 12 种敲除细胞系中 1280 种化合物诱导的形态变化。
- [Time-resolved mapping of genetic interactions to model rewiring of signaling pathways](https://doi.org/10.7554/eLife.40174) - 基于多种形态描述符的遗传相互作用随时间的变化。
- [High-Content Imaging of Unbiased Chemical Perturbations Reveals that the Phenotypic Plasticity of the Actin Cytoskeleton Is Constrained](https://doi.org/10.1016/j.cels.2019.09.002) - 在大型复合屏幕中定义形态簇。
- [A map of directional genetic interactions in a metazoan cell](https://doi.org/10.7554/eLife.05464) - 通过整合 21 个表型描述符来表征遗传相互作用。
- [The phenotypic landscape of essential human genes](https://doi.org/10.1016/j.cell.2022.10.017) - 比较混合 CRISPR 筛选中的形态描述符与原位测序
- [Evaluation of Gene Expression and Phenotypic Profiling Data as Quantitative Descriptors for Predicting Drug Targets and Mechanisms of Action](https://doi.org/10.1101/580654) - 对分析模式（包括基于图像的分析）进行基准测试，以预测作用机制。
- [The molecular architecture of cell cycle arrest](https://doi.org/10.15252/msb.202211087) - 比较细胞周期不同阶段的细胞特征。
- [Integrated intracellular organization and its variations in human iPS cells](https://doi.org/10.1038/s41586-022-05563-7) - 在多个 iPSC 中以 3D 方式分解细胞和核形状并研究细胞结构之间的关联。
- [Single-cell metabolic profiling of human cytotoxic T cells](https://doi.org/10.1038/s41587-020-0651-8) - 结合代谢谱和空间信息来定义肿瘤微环境中的免疫子集。
- [The single-cell pathology landscape of breast cancer](https://doi.org/10.1038/s41586-019-1876-x) - 根据多重成像的形状、强度和背景信息定义乳腺癌中的细胞群及其相互作用。
- [Identification of phenotype-specific networks from paired gene expression–cell shape imaging data](https://doi.org/10.1101%2Fgr.276059.121) - 通过匹配表达和成像数据来寻找细胞形态学基础的基因网络。
- [Predicting drug polypharmacology from cell morphology readouts using variational autoencoder latent space arithmetic](https://doi.org/10.1371/journal.pcbi.1009888) - 使用自动编码器对细胞形态进行建模，以估计药物组合的效果。
- [Deep Morphology Learning Enhances Ex Vivo Drug Profiling-Based Precision Medicine](https://doi.org/10.1158/2643-3230.BCD-21-0219) - 具体描述如何从患者材料中提取形态信息并指导治疗。

### 方法

- [Cell Painting, a high-content image-based assay for morphological profiling using multiplexed fluorescent dyes](https://doi.org/10.1038/nprot.2016.105) - 描述使用细胞绘画设计和执行实验的协议。
- [Multiplex Cytological Profiling Assay to Measure Diverse Cellular States](https://doi.org/10.1371/journal.pone.0080999) - 细胞涂色测定。
- [CIDRE: an illumination-correction method for optical microscopy](https://doi.org/10.1038/nmeth.3323) - 基于能量最小化的光照校正回顾方法。
- [Retrospective shading correction based entropy minimization](https://doi.org/10.1046/j.1365-2818.2000.00669.x) - 基于熵最小化的回顾性阴影校正方法。
- [Capturing single-cell heterogeneity via data fusion improves image-based profiling](https://doi.org/10.1038/s41467-019-10154-8) - 将离散度和协方差添加到群体平均值中以捕获单细胞异质性。
- [Minimum redundancy feature selection from microarray gene expression data](https://doi.org/10.1142/S0219720005001004) - 最小冗余-最大相关性特征选择框架。
- [Learning unsupervised feature representations for single cell microscopy images with paired cell inpainting](https://doi.org/10.1371/journal.pcbi.1007348) - 在没有标记训练数据的情况下学习显微图像中单细胞特征表示的自监督方法。
- [Weakly supervised learning of single-cell feature embeddings](https://doi.org/10.1109/CVPR.2018.00970) - 使用弱监督特征学习方法训练 CNN。
- [Accurate Prediction of Biological Assays with High-Throughput Microscopy Images and Convolutional Networks](https://doi.org/10.1021/acs.jcim.8b00670) - 使用 CNN 进行端到端学习，使用基于图像的配置文件来预测不相关测定中小分子的生物活性。
- [Evaluation of Deep Learning Strategies for Nucleus Segmentation in Fluorescence Images](https://doi.org/10.1002/cyto.a.23863) - 比较几种用于核分割的深度学习方法。
- [Automating Morphological Profiling with Generic Deep Convolutional Networks](https://doi.org/10.1101/085118) - 传输通用 CNN 的激活特征以提取基于图像的分析的特征。
- [A BaSiC tool for background and shading correction of optical microscopy images](https://doi.org/10.1038/ncomms14836) - 考虑空间和时间依赖性偏差的照明校正方法。
- [Cellpose: a generalist algorithm for cellular segmentation](https://doi.org/10.1038/s41592-020-01018-x) - 具有预训练权重的细胞和细胞核分割的通用深度学习模型。
- [Deep Learning Automates the Quantitative Analysis of Individual Cells in Live-Cell Imaging Experiments](https://doi.org/10.1371/journal.pcbi.1005177) - DeepCell：深度学习分割模型的集合。
- [改善表型测量
高内涵成像屏幕](https://doi.org/10.1101/161422) - 使用迁移学习嵌入单细胞和复合配置文件，以作用预测机制为例。
- [The Multidimensional Perturbation Value](https://doi.org/10.1177/1087057112469257) - 提出一个分数来定义屏幕中的重要活动。
- [Label-Free Prediction of Cell Painting from Brightfield Images](https://doi.org/10.1038/s41598-022-12914-x) - 重建细胞绘画染料的图像并确保保留相应的形态测量结果。
- [ShapoGraphy: A User-Friendly Web Application for Creating Bespoke and Intuitive Visualisation of Biomedical Data](https://doi.org/10.3389/fbinf.2022.788607) - 可视化形态剖面的方法。
- [CytoGAN: Generative Modeling of Cell Images](https://doi.org/10.1101/227645) - 生成网络显示出从细胞图像中学习生物条件的潜在表示的潜力。
- [Self-supervised feature extraction from image time series in plant phenotyping using triplet networks](https://doi.org/https://doi.org/10.1093/bioinformatics/btaa905) - 从植物图像中直接提取表型特征。
- [Morphology and gene expression profiling provide complementary information for mapping cell state](https://doi.org/10.1016/j.cels.2022.10.001) - 对于相同扰动，比较 Cell Painting 和 L1000 测定中包含的信息。
- [Fully unsupervised deep mode of action learning for phenotyping high-content cellular images](https://doi.org/10.1093/bioinformatics/btab497) - 用与有意义的关系（例如作用机制）相对应的簇来表示细胞形态的无监督方法。概述用于形态分析和分类的深度学习方法。
- [Automated high-speed 3D imaging of organoid cultures with multi-scale phenotypic quantification](https://doi.org/10.1038/s41592-022-01508-0) - 使用光片显微镜提取类器官 3D 形态描述符的实验和计算工作流程。

## 贡献

欢迎投稿！首先阅读[贡献指南](contributing.md)。

## 执照

[![CC0](http://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](http://creativecommons.org/publicdomain/zero/1.0)
