# 很棒的化学信息学 [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> 化学信息学（也称为化学信息学、化学信息学和化学信息学）是利用计算机和信息技术解决化学领域的一系列问题。— [维基百科](https://en.wikipedia.org/wiki/Cheminformatics)

精彩的化学信息学软件、资源和库的精选列表。主要基于命令行，并且免费或开源。请随时[贡献](CONTRIBUTING.md)！

## 内容

* [Applications](#applications)
  * [Visualization](#app-visualization)
  * [命令行工具](#app-cmd)
  * [Docking](#app-docking)
  * [虚拟机](#app-virtual)
* [Libraries](#libraries)
  * [通用型](#lib-general)
  * [Visualization](#lib-visualization)
  * [命令行工具](#lib-format)
  * [Docking](#lib-dock)
  * [分子描述符](#lib-des)
  * [机器学习](#lib-ml)
  * [网络 API](#lib-web)
  * [Databases](#lib-db)
  * [Others](#lib-others)
* [Journals](#journals)
* [Resources](#resources)
  * [Courses](#courses)
  * [Blogs](#blogs)
  * [Books](#books)
* [另请参阅](#see-also)

## 应用领域

<a id="app-visualization"></a>
### 可视化

* [PyMOL](https://sourceforge.net/projects/pymol/) - Python 增强的分子图形工具。
* [Jmol](http://jmol.sourceforge.net/) - 基于浏览器的 HTML5 查看器和独立 Java 查看器，用于 3D 化学结构。
* [VMD](http://www.ks.uiuc.edu/Research/vmd/) - 分子可视化程序，用于使用 3D 图形和内置脚本来显示、动画和分析大型生物分子系统。
* [Chimera](https://www.cgl.ucsf.edu/chimera/) - 用于交互式分子可视化和分析的高度可扩展程序。 [来源](https://www.cgl.ucsf.edu/chimera/docs/sourcecode.html) 可用。
* [ChimeraX](https://www.cgl.ucsf.edu/chimerax/) - 继 UCSF Chimera 之后的下一代分子可视化程序。来源可在[此处](https://www.cgl.ucsf.edu/chimerax/docs/devel/conventions.html)获得。
* [DataWarrior](http://www.openmolecules.org/datawarrior/index.html) - 数据可视化和分析程序，将动态图形视图和交互式行过滤与化学智能相结合。

<a id="app-cmd"></a>
### 命令行工具

* [Open Babel](http://openbabel.org/wiki/Main_Page) - 化学工具箱旨在支持多种化学数据语言。
* [MayaChemTools](http://www.mayachemtools.org/index.html) - 支持日常计算发现需求的 Perl 和 Python 脚本、模块和类的集合。
* [Packmol](http://m3g.iqm.unicamp.br/packmol/home.shtml) - 通过包装优化进行分子动力学模拟的初始配置。
* [BCL::Commons](http://meilerlab.org/index.php/bclcommons/show/b_apps_id/1)

<a id="app-docking"></a>
### 对接

* [AutoDock Vina](http://vina.scripps.edu/) - 分子对接和虚拟筛选。
* [smina](https://sourceforge.net/projects/smina/) - 定制[AutoDock Vina](http://vina.scripps.edu/)，更好支持评分功能开发和高性能能耗最小化。

<a id="app-virtual"></a>
### 虚拟机

* [myChEMBL](http://chembl.blogspot.com/2015/07/mychembl-20-has-landed.html) - 使用开源软件（Ubuntu、PostgreSQL、RDKit）构建的 ChEMBL 版本
* [3D e-Chem Virtual Machine](https://github.com/3D-e-Chem/3D-e-Chem-VM) - 具有运行 3D-e-Chem Knime 工作流程的所有软件和示例数据的虚拟机

## 图书馆

<a id="lib-general"></a>
### 通用型

* [RDKit](http://www.rdkit.org/) - 用 C++ 和 Python 编写的化学信息学和机器学习软件集合。
* [Indigo](https://github.com/epam/Indigo) - 通用分子工具包，可用于用 C++ 包编写的分子指纹识别、子结构搜索和分子可视化，并带有 Java、C# 和 Python 包装器。
* [CDK (Chemistry Development Kit)](https://sourceforge.net/projects/cdk/) - 结构化学和生物信息学算法，用 Java 实现。
* [ChemmineR](https://www.bioconductor.org/packages/release/bioc/vignettes/ChemmineR/inst/doc/ChemmineR.html) - 用于分析 R 中类药物小分子数据的化学信息学包。
* [ChemPy](https://github.com/bjodah/chempy) - 对化学有用的 Python 包（主要是物理/无机/分析化学）
* [MolecularGraph.jl](https://github.com/mojaie/MolecularGraph.jl) - 完全在 Julia 中实现的基于图形的分子建模和化学信息学分析工具包
* [datamol](https://github.com/datamol-org/datamol): - 分子操作变得简单。构建在 RDKit 之上的轻量级包装器。
* [CGRtools](https://github.com/cimm-kzn/CGRtools) - 用于处理分子、反应和反应浓缩图的工具包。可用于化学标准化、MCS 搜索、互变异构体生成，并向后兼容 RDKit 和 NetworkX。

<a id="lib-format"></a>
### 格式检查

* [ChEMBL_Structure_Pipeline (formerly standardiser)](https://github.com/chembl/ChEMBL_Structure_Pipeline) - 旨在提供一种简单的分子标准化方法的工具，作为例如分子标准化的前奏。分子建模练习。
* [MolVS](https://github.com/mcs07/MolVS) - 基于[RDKit](http://www.rdkit.org/)的分子验证和标准化。
* [rd_filters](https://github.com/PatWalters/rd_filters) - 使用 RDKit 和 ChEMBL 运行结构警报的脚本
* [pdb-tools](https://github.com/haddocking/pdb-tools) - 用于操作和编辑 PDB 文件的瑞士军刀。

<a id="lib-visualization"></a>
### 可视化

* [Kekule.js](http://partridgejiang.github.io/Kekule.js/) - 前端 JavaScript 库，提供在 Web 浏览器上表示、绘制、编辑、比较和搜索分子结构的能力。
* [3Dmol.js](https://github.com/3dmol/3Dmol.js) - 一个面向对象、基于 webGL 的 JavaScript 库，用于在线分子可视化。
* [JChemPaint](https://github.com/JChemPaint/jchempaint) - 基于[化学开发套件](https://sourceforge.net/projects/cdk/)的化学二维结构编辑器应用程序/小程序。
* [rdeditor](https://github.com/EBjerrum/rdeditor) - 使用 PySide 的简单 RDKit 分子编辑器 GUI。
* [nglviewer](http://nglviewer.org/nglview/latest/) - Jupyter 笔记本的交互式分子图形。
* [RDKit.js](https://www.npmjs.com/package/@rdkit/rdkit) - RDKit 化学信息学功能的官方 JavaScript 发行版 - 化学信息学的 C++ 库。

<a id="lib-des"></a>
### 分子描述符

* [mordred](https://github.com/mordred-descriptor/mordred) - 基于[RDKit](http://www.rdkit.org/)的分子描述符计算器。
* [DescriptaStorus](https://github.com/bp-kelley/descriptastorus) - 用于机器学习的描述符计算（化学）和（可选）存储。
* [mol2vec](https://github.com/samoturk/mol2vec) - 分子子结构的矢量表示。
* [Align-it](http://silicos-it.be.s3-website-eu-west-1.amazonaws.com/software/align-it/1.0.4/align-it.html#alignit-generating-pharmacophore-points) - 根据分子的药效团排列分子。
* [Rcpi](https://nanx.me/Rcpi/index.html) - R/Bioconductor 包可生成蛋白质、化合物及其相互作用的各种描述符。

<a id="lib-ml"></a>
### 机器学习

* [DeepChem](https://github.com/deepchem/deepchem) - 基于Tensorflow的化学深度学习库
* [Chemprop](https://github.com/chemprop/chemprop) - 定向消息传递神经网络用于具有不确定性和解释的分子和反应的性质预测。
* [ChemML](https://github.com/hachmannlab/chemml) - ChemML 是一个机器学习和信息学程序套件，用于化学和材料数据的分析、挖掘和建模。 （基于张量流）
* [olorenchemengine](https://github.com/Oloren-AI/olorenchemengine) - 使用针对不同模型和表示的统一 API 进行分子特性预测，
具有集成的不确定性量化、可解释性和超参数/架构调整。
* [OpenChem](https://github.com/Mariewelt/OpenChem) - OpenChem 是一个具有 PyTorch 后端的计算化学深度学习工具包。
* [DGL-LifeSci](https://github.com/awslabs/dgl-lifesci) - DGL-LifeSci 是一个基于 [DGL](https://www.dgl.ai/) 的软件包，适用于生命科学中的图形神经网络的各种应用。
* [chainer-chemistry](https://github.com/pfnet-research/chainer-chemistry) - 生物学和化学深度学习图书馆。
* [pytorch-geometric](https://pytorch-geometric.readthedocs.io/en/latest/) - PyTorch 库提供了许多图卷积算法的实现。
* [chemmodlab](https://github.com/jrash/ChemModLab) - 用于拟合和评估 R 机器学习模型的化学信息学建模实验室。
* [Summit](https://github.com/sustainable-processes/summit) - 一个使用机器学习优化化学反应的 python 包（包含 10 个算法 + 几个基准）。

<a id="lib-web"></a>
### 网络 API

* [webchem](https://github.com/ropensci/webchem) - 来自网络的化学信息。
* [PubChemPy](http://pubchempy.readthedocs.io) - PubChem PUG REST API 的 Python 包装器。
* [ChemSpiPy](http://chemspipy.readthedocs.org) - ChemSpider API 的 Python 包装器。
* [CIRpy](http://cirpy.readthedocs.org/) - [NCI 化学标识符解析器 (CIR)](https://cactus.nci.nih.gov/chemical/struct) 的 Python 包装器。
* [Beaker](https://github.com/chembl/chembl_beaker) - [RDKit](http://www.rdkit.org/) 和 [OSRA](https://cactus.nci.nih.gov/osra/) 在 [Tornado](http://www.tornadoweb.org/en/stable/) 上的 [Bottle](http://bottlepy.org/docs/dev/) 中。
* [chemminetools](https://github.com/girke-lab/chemminetools) - 基于 Django 的用于小分子分析的开源 Web 框架。
* [ambit](http://ambit.sourceforge.net/) - 通过 REST Web 服务提供化学信息学功能。

<a id="lib-db"></a>
### 数据库

* [razi](https://github.com/rvianello/razi) - SQLAlchemy 数据库的化学信息扩展。
* [Chemical Translation Service](https://bitbucket.org/fiehnlab/fiehnlab-cts/src/master/) - [化学翻译服务](https://cts.fiehnlab.ucdavis.edu/) Web 服务的源代码。

<a id="lib-dock"></a>
### 对接
* [Rosetta](https://www.rosettacommons.org/docs/latest/Home) - 用于模拟大分子结构的综合软件套件。很少用于蛋白质-蛋白质对接。
* [DOCKSTRING](https://github.com/dockstring/dockstring) - 自动化和标准化 AutoDock Vina 的配体制备。

<a id="lib-md"></a>
### 分子动力学

* [Gromacs](http://www.gromacs.org/) - 分子动力学软件包主要用于模拟蛋白质、脂质和核酸。
* [OpenMM](http://openmm.org/) - 用于分子模拟的高性能工具包，包括针对 Python、C、C++ 甚至 Fortran 的广泛语言绑定。
* [NAMD](https://www.ks.uiuc.edu/Research/namd/) - 专为大型生物分子系统的高性能模拟而设计的并行分子动力学代码。
* [MDTraj](https://github.com/mdtraj/mdtraj) - 分子动力学轨迹分析。
* [cclib](https://github.com/cclib/cclib) - 计算化学日志文件的解析器和算法。
* [ProDy](https://github.com/prody/ProDy) - 用于蛋白质动力学分析的 Python 包

<a id="lib-others"></a>
### 其他

* [eiR](https://github.com/girke-lab/eiR) - 小分子的加速相似性搜索
* [OPSIN](https://github.com/dan2097/opsin) - 用于系统 IUPAC 命名法的开放解析器
* [Cookiecutter for Computational Molecular Sciences](https://github.com/MolSSI/cookiecutter-cms) - 用于分子计算化学包的以 Python 为中心的 Cookiecutter，作者：[MolSSL](https://molssi.org/)
* [Auto-QChem](https://github.com/PrincetonUniversity/auto-qchem) - 用于生成和存储有机分子 DFT 计算的自动化工作流程。
* [Gypsum-DL](https://git.durrantlab.pitt.edu/jdurrant/gypsum_dl) - 用于将 2D SMILES 字符串转换为 3D 模型的程序。
* [RDchiral](https://github.com/connorcoley/rdchiral) - RDKit RunReactants 的包装，以改善立体化学处理
* [confgen](https://github.com/Et9797/confgen-webapp) - 用于生成构象异构体的 Web 应用程序
 
 
## 期刊

* [化学信息学杂志](https://jcheminf.biomedcentral.com/)
* [化学信息与建模杂志（ACS 出版物）](https://pubs.acs.org/journal/jcisd8)

## 资源

### 课程

* [Learncheminformatics.com](http://learncheminformatics.com/) - 印第安纳大学的“化学信息学：化学数据世界导航”课程。
* [用于化学信息学的 Python](https://github.com/Mishima-syk/py4chemoinformatics)
* [TeachOpenCADD](https://github.com/volkamerlab/TeachOpenCADD) - 使用开源包和数据的计算机辅助药物设计 (CADD) 教学平台。
* [化学信息学 OLCC](https://chem.libretexts.org/Courses/Intercollegiate_Courses/Cheminformatics_OLCC_(2019)) - 阿肯色大学小石城分校合作校际在线化学课程 (OLCC) 的化学信息学课程，作者：Robert Belford
* [BigChem](http://bigchem.eu/alllectures) - [BigChem](http://bigchem.eu/) 的所有讲座（Horizon 2020 MSC ITN EID 项目，提供大化学数据分析方面的创新教育。）
* [Molecular modeling course](https://dasher.wustl.edu/chem478/) - 由华盛顿大学圣路易斯分校教授 [Jay Ponder](https://dasher.wustl.edu/) 博士撰写。
* [Simulation in Chemistry and Biochemistry](https://dasher.wustl.edu/chem430/) - 由华盛顿大学圣路易斯分校教授 [Jay Ponder](https://dasher.wustl.edu/) 博士撰写。

### 博客

* [Open Source Molecular Modeling](https://opensourcemolecularmodeling.github.io/README.html) - 开源分子建模软件的可更新目录。
* [PubChem Blog](https://pubchemblog.ncbi.nlm.nih.gov/) - 有关 [PubChem](https://pubchem.ncbi.nlm.nih.gov/) 的新闻、更新和教程。
* [The ChEMBL-og blog](http://chembl.blogspot.tw/) - 来自 [EMBL-EBI](https://www.ebi.ac.uk/) 计算化学生物学小组的故事和新闻。
* [ChEMBL blog](http://chembl.github.io/) - GitHub 上的 ChEMBL。
* [SteinBlog](http://www.steinbeck-molecular.de/steinblog/) - [Christoph Steinbeck](http://www.steinbeck-molecular.de/steinblog/index.php/about/) 的博客，他是 EMBL-EBI 化学信息学和新陈代谢的负责人。
* [Practical Cheminformatics](http://practicalcheminformatics.blogspot.com/) - 包含化学信息学实际应用的深入示例的博客。
* [So much to do, so little time - Trying to squeeze sense out of chemical data](http://blog.rguha.net/) - [Rajarshi Guha](http://blog.rguha.net/?page_id=8) 的 Bolg 是 NIH 转化科学促进中心的研究科学家。
* 一些旧博客 [1](https://rguha.wordpress.com/) [2](http://www.rguha.net/index.html)。
* [Noel O'Blog](http://baoilleach.blogspot.tw/) - [Noel O'Boyle](https://www.redbrick.dcu.ie/~noel/) 的博客，他是 NextMove Software 的高级软件工程师。
* [chem-bla-ics](http://chem-bla-ics.blogspot.tw/) - 马斯特里赫特大学助理教授 [Egon Willighagen](http://egonw.github.io/) 的博客。
<!---
* [Asad's Blog](https://chembioinfo.com/) - Syed Asad Rahman 的 Bolg 是 EMBL-EBI [Thornton 小组](http://www.ebi.ac.uk/research/thornton) 的研究科学家。
-->
* [steeveslab-blog](http://asteeves.github.io/) - 使用 [RDKit](http://www.rdkit.org/) 的一些示例。
* [Macs in Chemistry](http://www.macinchem.org/) - 为使用 Apple Macintosh 计算机的化学家提供资源。
* [DrugDiscovery.NET](http://www.drugdiscovery.net/) - 剑桥大学分子信息学读者 [Andreas Bender](http://www.andreasbender.de/) 的博客。
* [Is life worth living?](https://iwatobipen.wordpress.com/) - 化学信息学库的一些示例。
* [Cheminformatics 2.0](https://cheminf20.org/) - Collaborative Drug Discovery 的研究科学家 [Alex M. Clark](https://twitter.com/aclarkxyz) 的博客。
* [Depth-First](https://depth-first.com/) - [Richard L. Apodaca](https://depth-first.com/about/) 的博客，他是一位居住在加利福尼亚州拉霍亚的化学家。
* [Cheminformania](https://www.cheminformania.com) - [博士 Esben Jannik Bjerrum](https://www.cheminformania.com/about/esben-jannik-bjerrum/) 的博客，他是阿斯利康的首席科学家、机器学习和人工智能专家。

### 书籍

* [Computational Approaches in Cheminformatics and Bioinformatics](https://books.google.com/books/about/Computational_Approaches_in_Cheminformat.html?id=bLqV4rYQoYsC) - 同时包括来自公众 (NIH)、学术界和工业界的见解。
* [Chemoinformatics for Drug Discovery](https://onlinelibrary.wiley.com/doi/book/10.1002/9781118742785) - 有关如何使用化学信息学策略来改善药物发现结果的材料。
* [Molecular Descriptors for Chemoinformatics](https://onlinelibrary.wiley.com/doi/book/10.1002/9783527628766) - 超过 3300 个描述符和相关术语，用于化合物特性的化学信息学分析。

<a id="see-also"></a>
## 另请参阅

* [deeplearning-biology](https://github.com/hussius/deeplearning-biology#chemoinformatics-and-drug-discovery-) - 深度学习生物学回购中的化学信息学和药物发现部分。
* [awesome-python-chemistry](https://github.com/lmmentel/awesome-python-chemistry) - 另一个列表重点关注与化学相关的 Python 内容。
* [awesome-small-molecule-ml](https://github.com/benb111/awesome-small-molecule-ml) - 用于小分子药物发现的机器学习的论文、数据集和其他资源列表。
* [awesome-molecular-docking](https://github.com/yangnianzu0515/awesome-molecular-docking) - 分子对接软件、数据集和其他密切相关资源的精选列表。
* [MolSSI 分子软件数据库](https://molssi.org/software-search/)
＊[Tobias Kind博士创建的页面](https://fiehnlab.ucdavis.edu/staff/kind/metabolomics)

## 许可证

[![CC0](http://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)
