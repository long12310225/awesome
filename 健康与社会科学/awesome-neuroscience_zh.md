<!-- ![Awesome Neuroscience](./AWESOME2.png) -->
<img src="./AWESOME2.png" width="50%">

> 精彩的神经科学库、软件和与该领域相关的任何内容的精选列表。

[神经科学](https://en.wikipedia.org/wiki/Neuroscience) 是对神经系统如何发育、其结构及其作用的研究。神经科学家关注大脑及其对行为和认知功能的影响。传统上，神经科学被视为生物学的一个分支，但它已经发展到涵盖广泛的跨学科领域，这些领域共同努力在多个研究层面上阐明大脑功能。

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)


## 内容

- [Programming](#programming)
  - [Python](#python)
  - [Matlab](#matlab)
  - [C++](#c)
  - [JavaScript](#javascript)
  - [R](#r)
- [Resources](#resources)
  - [Ebooks](#ebooks)
  - [Blogs](#blogs)
  - [MOOCs](#moocs)
  - [Communities](#communities)
  - [Newsletters](#newsletters)
  - [Miscellaneous](#miscellaneous)


## 编程
用于开发目的的软件、库和框架。

### 蟒蛇

- [Nengo](https://github.com/nengo/nengo) - 用于创建和模拟大规模大脑模型的库。
- [Nitime](https://github.com/nipy/nitime) - 神经科学数据的时间序列分析。
- [Nilearn](https://github.com/nilearn/nilearn) - 用于对神经影像数据执行统计学习/机器学习的模块。
- [DIPY](https://github.com/nipy/dipy) - 用于分析 MR 扩散成像的工具箱。
- [MNE-Python](https://github.com/mne-tools/mne-python) - 社区驱动的软件，用于处理时间分辨神经信号，包括脑电图 (EEG) 和脑磁图 (MEG)。
- [NiBabel](https://github.com/nipy/nibabel) - 提供对一些常见医学和神经影像文件格式的读写访问。
- [PsychoPy](https://github.com/psychopy/psychopy) - 用于运行心理学和神经科学实验的软件包。它允许在 Python 中创建心理刺激。
- [Brian2](https://github.com/brian-team/brian2) - 用于尖峰神经网络的免费开源模拟器。
- [expyriment](https://github.com/expyriment/expyriment) - 独立于平台的轻量级 Python 库，用于设计和进行时间关键的行为和神经影像实验。
 - [BindsNET](https://github.com/Hananel-Hazan/bindsnet) - 用于模拟强化和机器学习的尖峰神经网络的软件包。
 - [SpikeInterface](https://github.com/SpikeInterface/spikeinterface) - 旨在统一尖峰分选技术的框架
 - [NiMARE](https://nimare.readthedocs.io/en/latest/) - NiMARE 是一个用于神经影像荟萃分析的 Python 包
- [DeepLabCut](https://github.com/DeepLabCut/DeepLabCut) - 使用深度神经网络的迁移学习进行动物行为分析的无标记姿势估计工具包。
- [CaImAn](https://github.com/flatironinstitute/CaImAn) - 用于大规模钙成像数据分析的计算工具箱，包括运动校正、源提取和反卷积。
- [Elephant](https://github.com/NeuralEnsemble/elephant) - 用于分析电生理学数据的库，提供尖峰序列统计、信号处理和连接分析工具。
- [NEURON](https://github.com/neuronsimulator/nrn) - 用于对单个神经元和神经元网络进行建模的仿真环境，广泛应用于计算和系统神经科学。
- [Nipype](https://github.com/nipy/nipype) - 工作流引擎为现有神经影像包（FSL、FreeSurfer、AFNI、SPM、ANT）提供统一的 Python 接口和灵活的管道组合。
- [PyNWB](https://github.com/NeurodataWithoutBorders/pynwb) - 用于读取和写入 Neurodata Without Borders (NWB) 文件的 Python API，这是基于细胞的神经生理学数据的社区标准数据格式。
- [fMRIPrep](https://github.com/nipreps/fmriprep) - 强大的 fMRI 数据预处理管道，几乎适用于任何数据集，并以最少的手动干预生成可供分析的输出。
- [AllenSDK](https://github.com/AllenInstitute/AllenSDK) - 用于访问和处理艾伦脑科学研究所（包括艾伦脑图谱和艾伦脑天文台）数据的工具包。
- [Suite2p](https://github.com/MouseLand/suite2p) - 用于细胞检测和从大规模双光子钙成像记录中提取信号的管道。
- [Neo](https://github.com/NeuralEnsemble/python-neo) - 用于用 Python 表示电生理学数据的包，具有多种神经生理学文件格式的阅读器。
 
### MATLAB

- [Brain Dynamics Toolbox](https://bdtoolbox.org/) - 用于模拟神经科学动力系统的开放软件。
- [BrainStorm](https://neuroimage.usc.edu/brainstorm/) - 致力于分析大脑记录（MEG、EEG、fNIRS、ECoG、深度电极和多单元电生理学）的开源应用程序。
- [EEGLAB](https://sccn.ucsd.edu/eeglab/) - 用于处理连续和事件相关的 EEG、MEG 和其他电生理数据的交互式 Matlab 工具箱。
- [FieldTrip](https://github.com/fieldtrip/fieldtrip) - 用于 MEG 和 EEG 分析的工具箱。
- [Psychtoolbox-3](http://psychtoolbox.org/) - 用于视觉和神经科学研究的免费 Matlab 和 GNU Octave 函数集。
- [SPM](https://www.fil.ion.ucl.ac.uk/spm/) - 用于分析脑成像数据序列（fMRI、PET、SPECT、EEG、MEG）的免费开源软件。

### C++

- [Brayns](https://github.com/BlueBrain/Brayns) - 可以执行神经元光线追踪渲染的简约可视化工具。光线追踪可以帮助突出显示神经回路中细胞相互接触以及突触产生的区域，从而更好地了解单个细胞以及随后的大脑如何运作。

### JavaScript
- [Brainbrowser](https://github.com/aces/brainbrowser) - 库公开了一组基于网络的 3D 可视化工具，主要针对神经影像。
- [jsPsych](https://www.jspsych.org/) - 用于在网络浏览器中创建和运行行为实验的库。

### R
- [nat: NeuroAnatomy Toolbox](https://github.com/jefferis/nat) - 用于生物图像数据的 (3D) 可视化和分析的软件包，特别是单个神经元的追踪。
- [brainGraph](https://github.com/cwatson/brainGraph) - 用于对大脑 MRI 数据进行图论分析的软件包。

## 资源
与神经科学相关的有趣资源。

### 电子书
- [Neuroscience Online](http://nba.uth.tmc.edu/neuroscience/m/index.htm) - 深度涵盖神经科学的开放获取电子教科书和交互式课件。由休斯顿德克萨斯大学医学院神经生物学和解剖学系提供。
- [Computational Cognitive Neuroscience](https://compcogneuro.org/book) - 文本深入介绍了计算认知神经科学的主要思想，该领域旨在通过使用基于生物学的计算模型来理解大脑。
- [Neuronal Dynamics](https://neuronaldynamics.epfl.ch) - 涵盖计算和理论神经科学的开放获取电子教科书。由洛桑联邦理工学院 (EPFL) 提供。
- [Andy's Brain Book](https://andysbrainbook.readthedocs.io/en/latest/) - [安迪的大脑博客](https://www.andysbrainblog.com/) 的书籍伴侣。介绍在 Unix 环境中工作、fMRI 分析以及常见的神经影像工具和主题。
- [NiPraxis](https://textbook.nipraxis.org/intro.html) - [NiPraxis 课程](https://nipraxis.org/) 的教科书涵盖了神经影像分析的基本概念以及它们与更广泛的统计学、工程和计算机科学领域的关系。了解如何使用数据和代码，以更深入地了解功能磁共振成像方法的工作原理、它们如何失败、如何修复它们以及如何开发新方法。

### 博客

- [Neuroskeptic](https://www.discovermagazine.com/author/neuroskeptic) - [Discover magazine](http://discovermagazine.com/) 的神经科学博客，通过批判性的视角介绍神经科学、精神病学和心理学的最新发展。
- [Andy's Brain Blog](https://www.andysbrainblog.com/) - 大量文章、教程和视频，涵盖许多流行的神经影像工具和方法。

### 慕课

[大规模开放在线课程 (MOOC)](https://en.wikipedia.org/wiki/Massive_open_online_course) 是免费的基于网络的远程学习计划，专为大量分散在各地的学生的参与而设计。
MOOC 可能以学院或大学课程为模式，也可能结构较少。

- [Introduction to Neuroscience | MIT OCW](https://ocw.mit.edu/courses/brain-and-cognitive-sciences/9-01-introduction-to-neuroscience-fall-2007/) - 介绍哺乳动物神经系统，重点是人脑的结构和功能。
- [Computational Neuroscience | Coursera](https://www.coursera.org/learn/computational-neuroscience) - 介绍基本计算方法，以了解神经系统的作用并确定它们的功能。
- [Medical Neuroscience](https://www.coursera.org/learn/medical-neuroscience) - 探索人类中枢神经系统的功能组织和神经生理学，同时为理解人类行为提供神经生物学框架。
- [Neuromatch Academy](https://github.com/NeuromatchAcademy/course-content) - 为期三周的计算神经科学强化暑期学校的 Jupyter 笔记本。

### 社区
- [Quora](https://www.quora.com/topic/Neuroscience-1) - Quora 上的神经科学主题包含通常由专家提供的从基础到高级问题的答案。
- [r/neuroscience](https://www.reddit.com/r/neuroscience/) - Reddit 子版块，用于讨论神经科学新闻、研究和问题。
- [StackExchange](https://psychology.stackexchange.com) - 心理学和神经科学 StackExchange 网站。
- [neuroimaging@python.org](https://mail.python.org/mailman/listinfo/neuroimaging) - Python 神经影像分析讨论列表。除其他事项外，此列表是有关 [NiPy](https://nipy.org/) 项目（包括 NiBabel、Nilearn、dipy、MNE-Python 等）的讨论的所在地。

### 时事通讯
- [On The Brain](http://neuro.hms.harvard.edu/harvard-mahoney-neuroscience-institute/hmni-newsletter) - 哈佛马奥尼神经科学研究所的电子季刊。
- [BrainPost](https://www.brainpost.co/) - 一个邮件列表，每周提供最新神经科学出版物的易于阅读的摘要。

### 杂项
- [Awesome Public Datasets - Neuroscience](https://github.com/awesomedata/awesome-public-datasets#neuroscience) - 高质量的开放神经科学数据集。
- [McCulloch & Pitts Neural Net Simulator](https://justinmeiners.github.io/neural-nets-sim/) - 基于神经元的历史计算模型的模拟器。
- [ModelDB](https://modeldb.science/) - 计算神经科学模型的可搜索数据库。
- [NeuroElectro](https://neuroelectro.org/) - 可搜索的神经元及其电生理特性数据库（摘自文献）
- [Neuroscience Mindmap](https://learn-anything.xyz/neuroscience) - 交互式思维导图包含为任何有兴趣学习神经科学的人精心策划的资源。
- [neuroSummerSchools](https://github.com/PhABC/neuroSummerSchools) - 神经科学及相关领域的夏季（和季节性）暑期学校列表。
- [Brain Matters](https://brainpodcast.com/) - 神经科学播客，真正的神经科学家坐下来谈论大脑。
- [NeuroHackademy](https://neurohackademy.org/) - 神经影像和数据科学暑期学校在华盛顿大学电子科学研究所举办。讲座可通过该研究所的 [YouTube 频道](https://www.youtube.com/@UWeScienceInstitute) 获取。
- [SORTED](https://github.com/PTDZ/SORTED) - 已排序：有趣的科学想法和链接列表（认知/神经和数据科学）
- [BIDS](https://bids.neuroimaging.io/) - 脑成像数据结构：组织神经成像和行为数据的社区标准，由大多数现代神经成像工具支持。
- [OpenNeuro](https://openneuro.org/) - 用于共享和分析神经影像数据（MRI、MEG、EEG、iEEG、ECoG、ASL、PET）的免费开放平台。

## 贡献

欢迎投稿！首先阅读[贡献指南](contributing.md)。


## 许可证

[![CC0](http://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](http://creativecommons.org/publicdomain/zero/1.0)

在法律允许的范围内，[Akash Tandon](https://github.com/analyticalmonk) 已放弃所有版权和
本作品的相关或邻接权。
