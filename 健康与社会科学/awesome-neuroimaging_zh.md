# 很棒的神经影像学 [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> 探索、组织和分析大脑图像和记录。先生专注。

## 内容

- [Viewers](#viewers)
- [Acquisition](#acquisition)
  - [MR](#mr)
- [质量保证和检查](#quality-assurance-and-checking)
- [Pipelines](#pipelines)
  - [Suites](#suites)
  - [BOLD](#bold)
  - [DSI](#dsi)
  - [Structural](#structural)
- [原始数据](#raw-data)
- [来源和自动化](#provenance-and-automation)
- [成像工具](#imaging-tools)
  - [Skullstripping](#skullstripping)
  - [Warping](#warping)
  - [Manipulation](#manipulation)
  - [Modeling](#modeling)
- [Libraries](#libraries)
- [Resources](#resources)
  - [博客、书籍和文档](#blogs-books-and-docs)
  - [讨论区和聊天室](#boards-and-chats)
  - [数据集存储库](#datasets-repositories)


## 观众
- [AFNI](https://afni.nimh.nih.gov/pub/dist/doc/htmldoc/afniandafni/gui_guide/main_toc.html) - AFNI 套装的体积观察器。 GUI 的美学由 90 年代 Motif 工具包定义。
- [freeview](https://surfer.nmr.mgh.harvard.edu/fswiki/FreeviewGuide/FreeviewIntroduction) - Freesurfer 套装中的表面和体积图像查看器。使用QT工具包。
- [fsleyes](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FSLeyes) - FSL 的体积查看器。
- [mricron](https://www.nitrc.org/projects/mricron) - 适用于 Windows 的体积查看器。
- [dsistudio](https://dsi-studio.labsolver.org/doc/gui_t1.html) - 来自 dsi-studio 工具套件的 DSI 查看器。
- [osirix](https://www.osirix-viewer.com/) - DICOM 数据库组织者和查看器。
- [Mango](https://mangoviewer.com/) - 多图像分析 GUI 是用于 dcm、nii、surface 等医学研究图像的查看器； 2019 年发布 4.1 版本。
- [`wb_view`](https://www.humanconnectome.org/software/connectome-workbench) - Connectome 工作台表面文件查看器。

## 收购
### 先生
#### 组织机构
- [reproIn](https://dbic-handbook.readthedocs.io/en/latest/mri/reproin.html) - 命名考试卡序列。
- [BIDS](https://bids-specification.readthedocs.io/en/stable/) - 脑成像数据结构 - 目录层次结构和文件命名规范。
#### 管理
- [PACS](https://en.wikipedia.org/wiki/Picture_archiving_and_communication_system) - 图片存档和通信系统标准，用于存储和传输来自医疗设备的 DICOM 图像，可能由扫描仪制造商实施。请参阅 [Siemens Healthineers Syngo Carbon](https://www.siemens-healthineers.com/en-us/digital-health-solutions/syngo-carbon)、[Phillips Vue PACS](https://www.documents.philips.com/assets/20240227/5a788a79bbdd4e1986f1b12300b0e534.pdf)、 [GE HealthCare True PACS](https://www.gehealthcare.com/products/healthcare-it/true-pacs)。
- [XNAT](https://www.xnat.org/) - 一个可扩展的开源成像信息学软件平台，致力于基于成像的研究。
  - [DAX](https://github.com/VUIIS/dax) - XNAT 的分布式自动化：使用带有 YAML 定义的输入/输出的容器化。
- [LORIS](https://mcin.ca/technology/loris/) - LORIS（纵向在线研究和成像系统）是用于神经影像研究的基于网络的数据和项目管理软件。
- [brainlife.io](https://brainlife.io) - 开源、免费且安全的可重复神经科学分析平台。
- [cbrain](https://mcin.ca/technology/cbrain/) - CBRAIN 是基于网络的软件，允许神经影像研究人员通过将数据连接到高性能计算 (HPC) 来对数据进行计算密集型分析。
- 💲[Flywheel](https://flywheel.io) - 一个基于云的成像研究数据平台，用于数据捕获、管理、自动化和机器学习。
- 💲[QMENTA](https://qmenta.com) - 用于临床试验的多合一成像平台。

#### 运动
- [FIRMM](https://firmm.readthedocs.io) - 用于 fMRI、扩散和导航 T1/T2 图像采集的实时运动监测。
- [`Dimon`](https://afni.nimh.nih.gov/pub/dist/doc/program_help/Dimon.html) - 使用 AFNI 监控 DICOM 图像文件的实时采集。


## 质量保证和检查

扫描仪图像的质量保证和质量控制。

- [MRIQC](https://mriqc.readthedocs.io/) - 从结构（T1w 和 T2w）和功能 MRI（磁共振成像）数据中提取无参考 IQM（图像质量指标）。
- [mrQA](https://github.com/Open-Minds-Lab/mrQA) - 用于医学成像数据集质量保证的工具，包括协议合规性。
- [bids-validator](https://github.com/bids-standard/bids-validator/) - 脑成像数据结构的验证器。

## 管道

预处理工作流程。

### 套房
适用于多种模式的软件包，通常提供图形用户界面。

<!--lint ignore double-link-->
- [AFNI](https://afni.nimh.nih.gov/) - Analysis of Function NeuroImages 是一款由 C、Python、R 程序和 shell 脚本组成的领先软件套件，主要用于分析和显示多种 MRI 模式。
- [FSL](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki) - 用于 FMRI、MRI 和扩散脑成像数据的综合分析工具库。
- [SPM](https://www.fil.ion.ucl.ac.uk/spm/) - 统计参数映射是指用于测试功能成像数据假设的空间扩展统计过程的构建和评估。
- [Qu|Nex](https://qunex.yale.edu/) - 定量神经影像环境和工具箱 (QuNex) 是一个开源软件套件，共同支持跨神经影像模式的数据组织、预处理、质量保证和分析的可扩展框架。
<!-- - [MINC](https://mcin.ca/technology/minc/) -- more of a format than suit? -->


### 大胆

- [fmriprep](https://fmriprep.org/) - 可访问的预处理管道对扫描采集协议的变化具有鲁棒性，并具有全面的错误和输出报告。输入是 BIDS 数据集。
- [`afni_proc.py`](https://afni.nimh.nih.gov/pub/dist/doc/program_help/afni_proc.py.html) - 使用 AFNI 预配置块的最佳实践管道。
- [HALFpipe](https://github.com/HALFpipe/HALFpipe) - 用户友好的软件，有助于功能磁共振成像数据的可重复分析。
- [XCP-D](https://xcp-d.readthedocs.io/en/latest/) - 后处理和噪声回归流程从 fMRIprep 结束的地方开始。
- [clpipe](https://clpipe.readthedocs.io/en/latest/) - 使用 fmriprep 预处理 fMRI 数据，并实现对功能连接分析（例如滋扰回归和过滤）非常重要的各种附加处理步骤。
- [fmri_processing_scripts](https://github.com/LabNeuroCogDevel/fmri_processing_scripts) - 用于最大程度预处理的传统管道。
- [HCP Pipeline](https://www.humanconnectome.org/software/hcp-mr-pipelines) - 管道脚本实现了 [Glasser et al. 2017] 中描述的最小预处理管道 (MPP)。 2013](http://www.ncbi.nlm.nih.gov/pubmed/23668970)。

### 数字SI

- [dsi-studio](https://dsi-studio.labsolver.org/) - 一种纤维束成像软件工具，可绘制大脑连接图并将结果与神经心理疾病相关联。
- [qsiprep](https://qsiprep.readthedocs.io/) - 配置用于处理扩散加权 MRI (dMRI) 数据的管道。

### 结构性
<!--lint ignore double-link-->
- [Freesurfer](https://freesurfer.net/) - 一个开源神经影像工具包，用于处理、分析和可视化人脑 MR 图像。
- [CIVET](https://mcin.ca/technology/civet/) - 用于对人脑成像数据进行全自动体积、皮层测量和形态测量分析的图像处理管道。


## 原始数据

处理 DICOM 和 k 空间图像

- [dcm2niix](https://github.com/rordenlab/dcm2niix) - DICOM 到 NIfTI 转换器。
- [heudiconv](https://github.com/nipy/heudiconv/) - 灵活的 DICOM 转换器，用于将脑成像数据组织到结构化目录布局中。
- [gdcm](https://sourceforge.net/projects/gdcm/) - Grassroots DICOM 是一个用于 DICOM 医疗文件的 C++ 库和 CLI 工具。
- [`pydicom`](https://pydicom.github.io/) - 用于检查、修改和创建 DICOM 文件的 Python 包和 cli 工具。
- [`dicom_hinfo`](https://afni.nimh.nih.gov/pub/dist/doc/program_help/dicom_hinfo.html), `dicom_hdr` - 打印 DICOM 文件中选定的信息。
<!--lint ignore double-link-->
- [`dcmdirtab`, `dcmtab_bids`](https://lncd.github.io/lncdtools/BIDS/) - 来自 [lncdtools](https://github.com/lncd/lncdtools/) 的以 CLI 为中心、基于正则表达式且迭代友好的 BIDS 转换管道。
- [pymapVBVD](https://git.fmrib.ox.ac.uk/wclarke/pymapvbvd) - 读取西门子 .dat 'twix' 原始数据文件。 Philipp Ehses 的 Matlab 工具图VBVD 的 Python 端口。
- [med2image](https://github.com/FNNDSC/med2image/pulls) - 用于从 DICOM 或 nifti 文件生成 jpg 或 png 图像的 Python CLI 工具。

## 来源和自动化

- [make](https://www.frontiersin.org/articles/10.3389/fninf.2016.00002/full) - 遵循“Makefile”中定义的脚本配方。
- [datalad](https://github.com/datalad/datalad) - 使用 git 和 git-annex 控制代码、数据、容器。特别是 `datalad run --input=... --output=...`。
- [`3dNotes`](https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dNotes.html) - 用于添加、删除和显示 AFNI 数据集注释的程序。
<!--lint ignore double-link-->
- [`niinote`](https://github.com/lncd/lncdtools/blob/master/niinote) - 将 AFNI nifti XML 历史记录添加到标头以运行和记录任何命令。 [lncdtools](https://github.com/lncd/lncdtools/) 的一部分。

## 成像工具
用于读取、写入和操作体积和/或表面数据的软件。

### 剥颅
- [optibet](https://montilab.psych.ucla.edu/fmri-wiki/optibet/) - 结合 afni 和 fsl 工具的 Shell 脚本，可在患者群体中实现更稳健的颅骨剥离。
<!--lint ignore double-link-->
- [`3dSkullStrip`](https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dSkullStrip.html) - [AFNI](https://afni.nimh.nih.gov/) 的头骨剥离实用程序具有许多参数。
<!--lint ignore double-link-->
- [`bet`](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/BET/UserGuide) - [FSL](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki) 的大脑提取工具。
<!--lint ignore double-link-->
- [`antsBrainExtraction.sh`](https://dpaniukov.github.io/2016/06/06/brain-extraction-with-ants.html) - [ANTs](http://stnava.github.io/ANTs/) 版本。
<!--lint ignore double-link-->
- [`mri-watershed`](https://surfer.nmr.mgh.harvard.edu/fswiki/mri_watershed) - [Freesurfer](https://freesurfer.net/) 管道的一部分。
- [ROBEX](https://www.nitrc.org/projects/robex) - 无需调整参数的鲁棒大脑提取。

### 翘曲
空间归一化

<!--lint ignore double-link-->
- [ANTs](http://stnava.github.io/ANTs/) - 高级归一化工具包括基于专家标记数据的概率组织分割和机器学习方法，以最大限度地提高多模态图像分割的可靠性和一致性。
<!--lint ignore double-link-->
- [3dQwarp](https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dQwarp.html) - OpenMP 并行 [AFNI](https://afni.nimh.nih.gov/) 工具，用于计算源数据集的非线性扭曲版本以匹配基础数据集。
<!--lint ignore double-link-->
- [flirt, fnirt](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FNIRT/UserGuide) - 由[FSL](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki)工具提供的变形软件。

#### 模板
- [templateflow](https://www.templateflow.org/) - 模块化、版本控制的资源，允许研究人员使用“现成的”模板并共享新模板。
- [MNI152](https://www.bic.mni.mcgill.ca/ServicesAtlases/ICBM152NLin2009) - 正常人群的无偏标准磁共振成像模板脑容量。

### 操纵
对矩阵值进行数学运算的工具

- [3dcalc](https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dcalc.html) - 1D 到 4D 数据集上的逐体素算术。来自AFNI。
- [fslmaths](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/Fslutils#:~:text=a%20combined%20image.-,fslmaths,--%20simple%20but%20powerful) - 简单但功能强大的程序可以对图像进行数学处理。来自 FSL。
- [fscalc](https://www.freesurfer.net/pub/dist/freesurfer/dev_binaries/centos6_x86_64/fscalc.fsl) - Freesurfer 的 fslmaths 包装。
<!--- Also see [#Libraries](#libraries) for development interfaces to be used within programming language.-->


### 造型

#### 热辐射

<!--lint ignore double-link-->
- [3dDeconvolve](https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dDeconvolve.html) - [AFNI](https://afni.nimh.nih.gov/) - 用于计算具有指定输入刺激时间序列的测量 3D+时间数据集的反卷积的程序。  该程序还可以使用多个输入刺激时间序列执行多元线性回归。
<!--lint ignore double-link-->
- [FEAT](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FEAT) - 基于一般线性建模的 GUI 引导简单实验分析。 [FSL](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki) 的一部分。

#### 磁共振成像

- [lcmodel](https://github.com/schorschinho/LCModel) - 实现磁共振波谱数据的线性组合建模。
- [FSL-MRS](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FSL-MRS) - 一套磁共振波谱工具，包括单体素 (SVS)、MRS 成像 (MRSI)、功能 MRS (fMRS)、扩散 MRS (dwMRS)、编辑波谱等。
- [Osprey](https://github.com/schorschinho/osprey) - 一款一体化软件套件，用于对体内磁共振波谱 (MRS) 数据进行最先进的处理和定量分析。

#### 脑电图
- [`fooof`](https://fooof-tools.github.io/fooof/index.html) - 快速、高效且具有生理信息的工具，用于参数化神经功率谱。

#### 杂项
- [hurst](https://github.com/elifesciences-publications/ei_hurst/) - 评估 MR 内在兴奋抑制失衡的算法（[Trakoshis et al, eLife, 2020](http://doi.org/10.7554/eLife.55684)）。
<!--lint ignore double-link-->
- [tat2](https://lncd.github.io/lncdtools/tat2/) - 使用 [lncdtools](https://github.com/lncd/lncdtools/) 中的 AFNI 二进制文件的时间平均 T2* 包装器脚本。

## 图书馆

### 蟒蛇

- [nipy](https://nipy.org/) - 包括“nibabel”、“nipype”和“nilearn”。

### R
- [oro.nifti](https://github.com/bjw34032/oro.nifti) - 用于遵循 ANALYZE、NIfTI 或 AFNI 格式的医学成像数据的输入/输出和可视化的功能。

### MATLAB

<!--lint ignore double-link-->
- [SPM](https://www.fil.ion.ucl.ac.uk/spm/) - 统计参数映射是指用于测试功能成像数据假设的空间扩展统计过程的构建和评估。
- [`imtool3D_td`](https://github.com/tanguyduval/imtool3D_td) - 带有用于 Matlab 的 ROI 工具的 3D 图像查看器（NIFTI 查看器，手动分割）。

## 资源

### 博客、书籍和文档

- [Andy's brain blog](https://andysbrainblog.com/) - 所有主要软件包（AFNI、SPM 和 FSL）中有关神经影像分析从头到尾的教程和视频。
- [DataLad handbook](https://handbook.datalad.org/) - 使用来源跟踪软件“datalad”的神经影像学特定应用的从头到尾的用例。
- [Hitchhacker's guide to the brain](https://learn-neuroimaging.github.io/hitchhackers_guide_brain/) - 从研究计划到通过采集、处理、分析和质量控制进行报告和数据共享的注释。
- [Online Neuroimaging Resources](https://github.com/Remi-Gau/online_neuroimaging_resources) - MRI、fMRI、EEG、MEG 在线资源清单。
- [U of A: Neuroimaging Core Documentation](https://neuroimaging-core-docs.readthedocs.io/) - 亚利桑那大学神经影像核心使用和/或开发的方法的文档。

### 讨论区和聊天室
- [neurostars](https://neurostars.org/) - 一般神经影像“讨论”形式。 `fmriprep` 建议的问答网站。
- [afni discuss](https://discuss.afni.nimh.nih.gov) - AFNI 的“讨论”实例。
- [brainhack](https://mattermost.brainhack.org/) - 神经影像学家的重要社区。

### 数据集存储库

- [openneuro](https://openneuro.org/) - 一个免费开放的平台，用于验证和共享符合 BIDS 的 MRI、PET、MEG、EEG 和 iEEG 数据。
- [NDA](https://nda.nih.gov/) - 国家心理健康研究所数据档案 (NDA) 提供从多个科学领域的数百个研究项目收集的人类受试者数据。
- [NITRC](https://www.nitrc.org/) - NeuroImaging 工具和资源 神经信息学软件和数据合作图书馆。

#### 大数据集

- [ABCD](https://abcdstudy.org/) - 长期青少年大脑认知发展研究，包括数千次纵向 MRI 扫描。
- [UK Biobank](https://www.ukbiobank.ac.uk/) - 拥有 500,000 名研究参与者的大型生物医学数据库和研究资源。
- [NCANDA](http://www.ncanda.org/) - 国家青少年酒精与神经发育联盟（4000+ MR 访问）。
- [PNC](https://www.med.upenn.edu/bbl/philadelphianeurodevelopmentalcohort.html) - 基于人口的样本，包括来自大费城地区的 9500 多名年龄在 8 至 21 岁之间、在 CHOP 网络接受过医疗护理的个体。
- [ENIGMA](https://enigma.ini.usc.edu/) - 通过荟萃分析增强神经影像遗传学联盟包含 50 个工作组的影像和基因组学数据。

## 贡献

欢迎投稿！首先阅读[贡献指南](contributing.md)。
