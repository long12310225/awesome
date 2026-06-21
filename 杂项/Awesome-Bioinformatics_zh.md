# 很棒的生物信息学 [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

> 生物信息学是一个跨学科领域，开发用于理解生物数据的方法和软件工具。 - [维基百科](https://en.wikipedia.org/wiki/Bioinformatics)

精彩的生物信息学软件、资源和库的精选列表。主要基于命令行，并且免费或开源。请随时[贡献](CONTRIBUTING.md)！

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
## 目录

- [套餐套房](#package-suites)
- [数据工具](#data-tools)
  - [Downloading](#downloading)
  - [Compressing](#compressing)
- [数据处理](#data-processing)
  - [命令行实用程序](#command-line-utilities)
- [下一代测序](#next-generation-sequencing)
  - [工作流程管理器](#workflow-managers)
  - [Pipelines](#pipelines)
  - [序列处理](#sequence-processing)
  - [数据分析](#data-analysis)
  - [序列比对](#sequence-alignment)
    - [Pairwise](#pairwise)
    - [多序列比对](#multiple-sequence-alignment)
    - [Clustering](#clustering)
  - [Quantification](#quantification)
  - [变体调用](#variant-calling)
    - [结构变异调用者](#structural-variant-callers)
  - [BAM 文件实用程序](#bam-file-utilities)
  - [VCF 文件实用程序](#vcf-file-utilities)
  - [GFF BED 文件实用程序](#gff-bed-file-utilities)
  - [变体模拟](#variant-simulation)
  - [变体预测/注释](#variant-predictionannotation)
  - [Python 模块](#python-modules)
    - [Data](#data)
    - [Tools](#tools)
  - [Assembly](#assembly)
  - [Annotation](#annotation)
- [长读长测序](#long-read-sequencing)
  - [长读汇编](#long-read-assembly)
- [Visualization](#visualization)
  - [基因组浏览器/基因图](#genome-browsers--gene-diagrams)
  - [马戏团相关](#circos-related)
- [数据库访问](#database-access)
- [Resources](#resources)
  - [成为一名生物信息学家](#becoming-a-bioinformatician)
  - [GitHub 上的生物信息学](#bioinformatics-on-github)
  - [Sequencing](#sequencing)
  - [RNA-Seq](#rna-seq)
  - [ChIP-Seq](#chip-seq)
  - [YouTube 频道和播放列表](#youtube-channels-and-playlists)
  - [Blogs](#blogs)
  - [Miscellaneous](#miscellaneous)
- [在线网络团体](#online-networking-groups)
- [License](#license)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

---

## 套餐套房

软件包套件收集了特定语言或平台的软件包和安装工具。我们有一些生物信息学软件。

- **[Bioperl](https://github.com/bioperl/bioperl-live)** - 生物信息学、基因组学和生命科学开源 Perl 工具用户和开发人员的国际协会。 [ [paper-2002](https://doi.org/10.1101%2Fgr.361602) | [网络](https://bioperl.org)]

- **[Bioconductor](https://github.com/Bioconductor)** - 用于分析和理解高通量基因组数据的大量工具，包括 1500 多个软件包。 [ [paper-2004](https://link.springer.com/article/10.1186/gb-2004-5-10-r80) | [网络](https://www.bioconductor.org)]

- **[Biopython](https://github.com/biopython/biopython)** - 免费提供的 Python 生物计算工具，包括说明书、打包和完整的文档。 [开放生物信息学基金会](http://open-bio.org/) 的一部分。包含非常有用的 [Entrez](https://biopython.org/DIST/docs/api/Bio.Entrez-module.html) 包，用于通过 API 访问 NCBI 数据库。 [ [论文-2009](https://pubmed.ncbi.nlm.nih.gov/19304878) | [网络](https://biopython.org)]

- **[Bioconda](https://github.com/bioconda)** - 专门从事生物信息学软件的 [conda 包管理器](http://conda.pydata.org/docs/intro.html) 的频道。包括一个包含 3000 多个可立即安装（使用“conda install”）生物信息学软件包的存储库。 [ [论文-2018](https://pubmed.ncbi.nlm.nih.gov/29967506) | [网络](https://bioconda.github.io)]

- **[BioJulia](https://github.com/BioJulia)** - Julia 编程语言的生物信息学和计算生物学基础设施。 [ [网络](https://biojulia.net) ]
- **[Rust-Bio](https://github.com/rust-bio/rust-bio)** - 对生物信息学有用的算法和数据结构的 Rust 实现。 [ [paper-2016](http://bioinformatics.oxfordjournals.org/content/early/2015/10/06/bioinformatics.btv573.short?rss=1) ]
- **[SeqAn](https://github.com/seqan/seqan3)** - 用于序列分析的现代 C++ 库。
- **[(Poly)merase](https://github.com/TimothyStiles/poly)** - 用于工程生物体的 Go 库和命令行实用程序。
- **[Biocaml](https://github.com/biocaml/biocaml)** - Biocaml 旨在成为一个高性能、用户友好的生物信息学库。
- **[Biojava](https://github.com/biojava/biojava)** - 用于处理生物数据的 Java 框架。

## 数据工具

### 正在下载
- **[GGD](https://github.com/gogetdata/ggd-cli)** - 获取数据；用于获取基因组数据的命令行界面。 [ [网络](https://gogetdata.github.io) ]
- **[SRA-Explorer](https://github.com/ewels/sra-explorer)** - 轻松获取SRA下载链接和其他信息。 [ [web](https://sra-explorer.info) ]

### 压缩
- **[Genozip](https://github.com/divonlan/genozip)** - 常见基因组文件格式（BAM、CRAM、FASTQ、VCF 等）的压缩器。 [ [web](https://genozip.com/?utm_source=Awesome-Bioinformatics) | [paper-2021](https://www.researchgate.net/publication/349347156_Genozip_-_A_Universal_Extensible_Genomic_Data_Compressor)]

## 数据处理

### 命令行实用程序

- **[生物信息学 One Liners](https://github.com/stephenturner/oneliners)** - 有用的单行命令的 Git 存储库。
- **[BioNode](https://github.com/bionode/bionode)** - 模块化和通用生物信息学，Bionode 为生物信息学分析工作流程提供可管道的 UNIX 命令行工具和 JavaScript API。 [ [网络](http://bionode.io) ]
- **[bioSyntax](https://github.com/bioSyntax/bioSyntax)** - vim/less/gedit/sublime 中计算生物学文件格式（SAM、VCF、GTF、FASTA、PDB 等）的语法突出显示。 [ [论文-2018](https://pubmed.ncbi.nlm.nih.gov/30134911) | [网络](http://www.bioSyntax.org)]
- **[CSVKit](https://github.com/wireservice/csvkit)** - 用于处理 CSV/制表符分隔文件的实用程序。 [ [网络](https://csvkit.readthedocs.io/en/latest) ]
- **[csvtk](https://github.com/shenwei356/csvtk)** - 另一个跨平台、高效、实用且漂亮的 CSV/TSV 工具包。 [ [网页](https://bioinf.shenwei.me/csvtk) ]
- **[datamash](https://git.savannah.gnu.org/gitweb/?p=datamash.git)** - 数据转换和统计。 [ [网络](http://www.gnu.org/software/datamash) ]
- **[easy_qsub](https://github.com/shenwei356/easy_qsub)** - 使用脚本模板轻松提交 PBS 作业。支持多个输入文件。
- **GNU Parallel** - 在单个多核机器上并行运行作业的通用并行器。 [此处](https://www.biostars.org/p/63816/) 是一些使用 GNU Parallel 的示例脚本。 [ [网络](http://www.gnu.org/software/parallel) ]
- **[grabix](https://github.com/arq5x/grabix)** - 一个用于随机访问 BGZF 文件的小工具。
- **[grepq](https://github.com/Rbfinch/grepq)** - 通过将读取与一个或多个正则表达式模式匹配来快速进行 FASTQ 过滤。
- **[gsort](https://github.com/brentp/gsort)** - 根据指定的顺序对基因组文件进行排序。
- **[tabix](https://github.com/samtools/tabix)** - 表文件索引。 [ [论文-2011](https://pubmed.ncbi.nlm.nih.gov/21208982) ]
- **[wormtable](https://github.com/wormtable/wormtable)** - 用于大型数据集的一次写入多次读取表。
- **[zindex](https://github.com/mattgodbolt/zindex)** - 在压缩文本文件上创建索引。

## 下一代测序

### 工作流程管理器

- **[BigDataScript](https://github.com/pcingola/BigDataScript)** - 一种跨系统脚本语言，用于在不同规模和功能的计算机系统中处理大数据管道。 [ [论文-2014](https://pubmed.ncbi.nlm.nih.gov/25189778) | [网络](https://pcingola.github.io/BigDataScript)]
- **[Bpipe](https://github.com/ssadedin/bpipe)** - 一种用于定义管道阶段并将它们链接在一起以形成管道的小语言。 [ [网络](http://docs.bpipe.org) ]
- **[通用工作流语言](https://github.com/common-workflow-language/common-workflow-language)** - 用于描述分析工作流和工具的规范，这些工作流和工具在各种软件和硬件环境（从工作站到集群、云和高性能计算 (HPC) 环境）中可移植和可扩展。 [ [网络](http://www.commonwl.org) ]
- **[Cromwell](https://github.com/broadinstitute/cromwell)** - 面向科学工作流程的工作流程管理系统。 [ [网络](https://cromwell.readthedocs.io) ]
- **[Galaxy](https://github.com/galaxyproject)** - 一个流行的开源、基于网络的平台，用于数据密集型生物医学研究。具有多种功能，从数据分析到工作流程管理再到可视化工具。 [ [论文-2018](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6030816) | [网络](https://galaxyproject.org)]
- **[Nextflow](https://github.com/nextflow-io/nextflow)（推荐）** - 围绕 UNIX 管道概念建模的流畅 DSL，以可移植的方式简化了并行和可扩展管道的编写。 [ [论文-2018](https://pubmed.ncbi.nlm.nih.gov/29412134) | [网络](http://nextflow.io)]
- **[redun](https://github.com/insitro/redun)** - 基于 python 的工作流程管理器。
- **[Ruffus](https://github.com/cgat-developers/ruffus)** -广泛应用于科学和生物信息学的Python计算管道库。 [ [论文-2010](https://pubmed.ncbi.nlm.nih.gov/20847218) | [网络](http://www.ruffus.org.uk) ]
- **[SciPipe](https://github.com/scipipe/scipipe)** - 嵌入 Go 编程语言中的工作流库，专注于支持复杂的工作流构造、编译为单个二进制文件、为每个输出提供强大的文件命名和全面的审计报告 [[paper-2019](https://pubmed.ncbi.nlm.nih.gov/31029061/) | [网络](https://scipipe.org/)]
- **[SeqWare](https://github.com/SeqWare/seqware)** - 基于 Hadoop Oozie 的工作流程系统，专注于云环境中的基因组数据分析。 [ [论文-2010](https://pubmed.ncbi.nlm.nih.gov/21210981) | [网络](https://seqware.github.io)]
- **[Snakemake](https://bitbucket.org/snakemake)** - Python 中的工作流管理系统，旨在通过提供快速舒适的执行环境来降低创建工作流的复杂性。 [ [论文-2018](https://pubmed.ncbi.nlm.nih.gov/29788404) | [网络](https://snakemake.readthedocs.io)]
- **[工作流描述符语言](https://github.com/broadinstitute/wdl)** - 由 Broad 开发的工作流标准。 [ [网络](https://software.broadinstitute.org/wdl) ]

### 管道

- **[Awesome-Pipeline](https://github.com/pditommaso/awesome-pipeline)** - 管道资源列表。
- **[Bactopia](https://github.com/bactopia/bactopia/)** - 使用 Nextflow 构建的灵活管道，用于对细菌基因组进行完整分析。 [ [网络](https://bactopia.github.io/) ]
- **[Bacannot](https://github.com/fmalmeida/bacannot)** - 通用但全面的细菌注释管道，使用 Nextflow 构建，具有用于调查结果的良好图形选项。 [ [web](https://bacannot.readthedocs.io/en/latest/?badge=latest) ]
- **[bcbio-nextgen](https://github.com/chapmanb/bcbio-nextgen)** - 电池包括用于变异和 RNA-Seq 分析、结构变异调用、注释和预测的基因组分析管道。 [ [网络](https://bcbio-nextgen.readthedocs.io) ]
- **[R-Peridot](https://github.com/pentalpha/r-peridot)** - 通过直观的 GUI 进行差异表达分析的可定制管道。 [ [网络](http://www.bioinformatics-brazil.org/r-peridot) ]
- **[ngs-preprocess](https://github.com/fmalmeida/ngs-preprocess)** - 使用 Nextflow 构建的用于预处理短和长测序读取的管道。 [ [web](https://ngs-preprocess.readthedocs.io/en/latest/?badge=latest) ]

### 序列处理

序列处理包括诸如多路分解原始读取数据和修剪低质量碱基等任务。

- **[AfterQC](https://github.com/OpenGene/AfterQC)** - fastq 数据的自动过滤、修剪、错误消除和质量控制。 [ [论文-2017](https://pubmed.ncbi.nlm.nih.gov/28361673) ]
- **[FastQC](https://github.com/s-andrews/FastQC)** - 高通量序列数据的质量控制工具。 [ [网络](http://www.bioinformatics.babraham.ac.uk/projects/fastqc) ]
- **[Fastqp](https://github.com/mdshw5/fastqp)** - 使用 Python 进行 FASTQ 和 SAM 质量控制。
- **[Fastx Tookit](https://github.com/agordon/fastx_toolkit)** - FASTQ/A 短读预处理工具：解复用、修剪、裁剪、质量过滤和屏蔽实用程序。 [ [网络](http://hannonlab.cshl.edu/fastx_toolkit) ]
- **[MultiQC](https://github.com/ewels/MultiQC)** - 将多个样本的生物信息学分析结果汇总到一份报告中。 [ [论文-2016](https://pubmed.ncbi.nlm.nih.gov/27312411) | [网络](http://multiqc.info)]
- **[SeqFu](https://github.com/telatin/seqfu2)** - 用 Nim 编写的 FASTA/FASTQ 文件的序列操作工具包。 [ [paper-2021](https://www.mdpi.com/2306-5354/8/5/59) | [网络](https://telatin.github.io/seqfu2/)]
- **[SeqKit](https://github.com/shenwei356/seqkit)** - 用于 Golang 中 FASTA/Q 文件操作的跨平台超快工具包。 [ [论文-2016](https://pubmed.ncbi.nlm.nih.gov/27706213) | [网页](https://bioinf.shenwei.me/seqkit) ]
- **[seqmagick](https://github.com/fhcrc/seqmagick)** - 以方便的方式在 Biopython 中进行文件格式转换。 [ [网络](http://seqmagick.readthedocs.io) ]
- **[Seqtk](https://github.com/lh3/seqtk)** - 用于处理 FASTA/Q 格式序列的工具包。
- **[smof](https://github.com/incertae-sedis/smof)** - UNIX 风格的 FASTA 操作工具。

### 数据分析

以下项目允许通过引入专门的数据库来进行可扩展的基因组分析。

- **[Hail](https://github.com/hail-is/hail)** - 可扩展的基因组分析。
- **[GLNexus](https://github.com/dnanexus-rnd/GLnexus)** - 用于群体测序项目的可扩展 gVCF 合并和联合变体调用。 [ [论文-2018](https://www.biorxiv.org/content/10.1101/343970v1.abstract) ]

### 序列比对

#### 成对

- **[Bowtie 2](https://github.com/BenLangmead/bowtie2)** - 一种超快且内存高效的工具，用于将测序读数与长参考序列对齐。 [ [论文-2012](https://pubmed.ncbi.nlm.nih.gov/22388286) | [网络](http://bowtie-bio.sourceforge.net/bowtie2)]
- **[BWA](https://github.com/lh3/bwa)** - Burrow-Wheeler Aligner 用于 DNA 序列之间的成对比对。
- **[BWA-FastAlign](https://github.com/zzhofict/BWA-FastAlign)** - BWA-MEM 直接替代品：速度提高 2-3 倍，成本降低 2-5 倍，在标准 CPU 上输出 100% 相同。 [[论文2026](https://dl.acm.org/doi/10.1145/3774934.3786421)]
- **[WFA](https://github.com/smarco/WFA)** - 波前对齐算法 (WFA)，利用序列相似性来加速对齐 [[paper-2020](https://academic.oup.com/bioinformatics/advance-article/doi/10.1093/bioinformatics/btaa777/5904262) ]
- **[Parasail](https://github.com/jeffdaily/parasail)** - 用于全局、半全局和局部成对序列比对的 SIMD C 库 [[paper-2016](https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-016-0930-z) ]
- **[MUMmer](https://github.com/mummer4/mummer)** - 一个用于快速比对整个基因组的系统，无论是完整的还是草稿的形式。 [ [paper-1999](http://mummer.sourceforge.net/MUMmer.pdf) | [论文-2002](http://mummer.sourceforge.net/MUMmer2.pdf) | [论文-2004](http://mummer.sourceforge.net/MUMmer3.pdf) | [网络](http://mummer.sourceforge.net) ]
- **[DIAMOND](https://github.com/bbuchfink/diamond)** - 用于“blastp”和“blastx”等搜索的超快蛋白质对准器。 [[论文-2021](https://www.nature.com/articles/s41592-021-01101-x)]

#### 多序列比对

- **[POA](https://github.com/ljdursi/poapy)** - 偏序比对，用于多个同源序列的快速比对和共识。 [ [论文-2002](https://academic.oup.com/bioinformatics/article/18/3/452/236691) ]

#### 聚类

- **[MMseqs2](https://github.com/soedinglab/MMseqs2)** - 用于蛋白质和核苷酸序列集的超快速、灵敏的搜索和聚类套件。 [ [论文-2017](https://www.nature.com/articles/nbt.3988) | [论文-2018](https://www.nature.com/articles/s41467-018-04964-5)]

### 量化

- **[Cufflinks](https://github.com/cole-trapnell-lab/cufflinks)** - Cufflinks 组装转录本，估计其丰度，并测试 RNA-Seq 样本中的差异表达和调控。 [ [论文-2010](https://www.nature.com/articles/nbt.1621) ]
- **[RSEM](https://github.com/deweylab/RSEM)** - 用于根据 RNA-Seq 数据估计基因和亚型表达水平的软件包。 [ [论文-2011](https://bmcbioinformatics.biomedcentral.com/articles/10.1186/1471-2105-12-323) | [网络](http://deweylab.github.io/RSEM/)]

### 变体调用

- **[DeepVariant](https://github.com/google/deepvariant)** - 基于深度学习的变体调用程序 [[paper-2018](https://rdcu.be/7Dhl) ]
- **[freebayes](https://github.com/ekg/freebayes)** - 基于贝叶斯单倍型的多态性发现和基因分型。 [ [网络](http://arxiv.org/abs/1207.3907) ]
- **[GATK](https://github.com/broadgsa/gatk)** - 高通量测序数据中的变体发现。 [ [网络](https://software.broadinstitute.org/gatk) ]
- **[Octopus](https://github.com/luntergroup/octopus)** - 具有广泛适用性的多态贝叶斯基因分型模型。 [[论文2021](https://www.nature.com/articles/s41587-021-00861-3)]
- **[bcftools](https://github.com/samtools/bcftools)** - samtools/bcftools 是一套用于操作 NGS 数据的工具，可用于调用变体。 [ [论文-2009](https://pubmed.ncbi.nlm.nih.gov/19505943) | [网络](http://htslib.org)]
#### 结构变异调用者

- **[Delly](https://github.com/dellytools/delly)** - 通过集成配对末端和分割读取分析发现结构变异。 [ [论文-2012](https://pubmed.ncbi.nlm.nih.gov/22962449) ]
- **[lumpy](https://github.com/arq5x/lumpy-sv)** -lumpy：用于结构变体发现的通用概率框架。 [ [论文-2014](https://link.springer.com/article/10.1186/gb-2014-15-6-r84) ]
- **[manta](https://github.com/Illumina/manta)** - 用于映射测序数据的结构变体和插入缺失调用程序。 [ [论文-2015](https://pubmed.ncbi.nlm.nih.gov/26647377) ]
- **[gridss](https://github.com/PapenfussLab/gridss)** - GRIDSS：基因组重排识别软件套件。 [ [论文-2017](https://pubmed.ncbi.nlm.nih.gov/29097403) ]
- **[smoove](https://github.com/brentp/smoove)** - 使用现有工具进行结构变异调用和基因分型，但是，顺利。

### BAM 文件实用程序

- **[Bamtools](https://github.com/pezmaster31/bamtools)** - 用于处理 BAM 文件的工具集合。 [ [论文-2011](https://academic.oup.com/bioinformatics/article/27/12/1691/255399) ]
- **[bam 工具箱](https://github.com/AndersenLab/bam-toolbox)** MtDNA：核覆盖； BAM Toolbox 可以输出 MtDNA:核覆盖率的比率，这是线粒体含量的代表。
- **[mergesam](https://github.com/DarwinAwardWinner/mergesam)** - 自动执行常见的 SAM 和 BAM 转换。
- **[mosdepth](https://github.com/brentp/mosdepth)** - 用于 WGS、外显子组或靶向测序的快速 BAM/CRAM 深度计算。 [ [论文-2017](https://pubmed.ncbi.nlm.nih.gov/29096012/) ]
- **[SAMstat](https://github.com/TimoLassmann/samstat)** - 显示下一代测序的序列统计数据。 [ [论文-2010](https://academic.oup.com/bioinformatics/article/27/1/130/201972) | [网络](http://samstat.sourceforge.net)]
- **[Somalier](https://github.com/brentp/somalier)** - 对 BAM/CRAM/VCF/GVCF 进行快速样本交换和相关性检查。 [[论文-2020](https://pubmed.ncbi.nlm.nih.gov/32664994)]
- **[Telseq](https://github.com/zd1/telseq)** - Telseq 是一种根据全基因组序列数据估计端粒长度的工具。 [ [论文-2014](https://academic.oup.com/nar/article/42/9/e75/1249448) ]

### VCF 文件实用程序

- **[bcftools](https://github.com/samtools/bcftools)** - 用于操作 VCF 文件的工具集。 [ [论文-2016](https://pubmed.ncbi.nlm.nih.gov/26826718) | [论文 2017](https://pubmed.ncbi.nlm.nih.gov/28205675) | [网络](http://samtools.github.io/bcftools)]
- **[vcfanno](https://github.com/brentp/vcfanno)** - 使用其他 VCF/BED/tabixed 文件注释 VCF。 [ [论文-2016](https://pubmed.ncbi.nlm.nih.gov/27250555) ]
- **[vcflib](https://github.com/vcflib/vcflib)** - 用于解析和操作 VCF 文件的 C++ 库。
- **[vcftools](https://github.com/vcftools/vcftools)** - VCF 操作和统计（例如连锁不平衡、等位基因频率、Fst）。 [ [论文-2011](https://pubmed.ncbi.nlm.nih.gov/21653522) ]

### GFF BED 文件实用程序

- **[AGAT](https://github.com/NBISweden/AGAT)** - 用于处理任何 GTF/GFF 格式的基因注释的工具套件。 [ [web](https://agat.readthedocs.io/en/latest/?badge=latest) ]
- **[gffutils](https://github.com/daler/gffutils)** - GFF 和 GTF 文件操作和相互转换。 [ [网络](http://daler.github.io/gffutils) ]
- **[BEDOPS](https://bedops.readthedocs.io/en/latest/index.html)** - 快速、高度可扩展且易于并行的基因组分析工具包。 [ [论文-2012](https://academic.oup.com/bioinformatics/article/28/14/1919/218826) ]
- **[Bedtools2](https://github.com/arq5x/bedtools2)** - 用于基因组算术的瑞士军刀。 [ [论文-2010](https://pubmed.ncbi.nlm.nih.gov/20110278) | [论文 2014](https://pubmed.ncbi.nlm.nih.gov/25199790) | [网络](https://bedtools.readthedocs.io)]

### 变体模拟

- **[Bam Surgeon](https://github.com/adamewing/bamsurgeon)** - 用于向现有 `.bam` 文件添加突变的工具，用于测试突变调用者。 [ [网络](https://popmodels.cancercontrol.cancer.gov/gsr/packages/bamsurgeon) ]
- **[wgsim](https://github.com/lh3/wgsim)** - **附带 samtools！** - 读取模拟器。 [ [网络](https://popmodels.cancercontrol.cancer.gov/gsr/packages/wgsim) ]

### 变体预测/注释

- **[SIFT](https://github.com/teamdfir/sift)** - 预测氨基酸替换是否影响蛋白质功能。 [ [paper-2003](https://pubmed.ncbi.nlm.nih.gov/12824425) | [网络](http://sift.jcvi.org) ]
- **[SnpEff](https://github.com/pcingola/SnpEff)** - 遗传变异注释和效果预测工具箱。 [ [论文-2012](https://www.tandfonline.com/doi/full/10.4161/fly.19695) | [网络](https://pcingola.github.io/SnpEff)]
- **[Ensembl VEP](https://anaconda.org/bioconda/ensembl-vep)** - VEP 确定变体（SNP、插入、缺失、CNV 或结构变体）对基因、转录本和蛋白质序列以及调控区域的影响。 [ [论文-2016](https://doi.org/10.1186/s13059-016-0974-4) | [网络](http://www.ensembl.org/info/docs/tools/vep/index.html)]
- **[ANNOVAR](https://annovar.openbioinformatics.org/en/latest/)** - 用于遗传变异的注释工具，预测对基因、转录本和调控元件的影响，允许自定义数据库集成。 [ [论文-2010](https://doi.org/10.1093/nar/gkq603) | [网络](https://annovar.openbioinformatics.org/en/latest/)]


### Python 模块

#### 数据

- **[cruzdb](https://github.com/brentp/cruzdb)** - 对 UCSC 基因组数据库的 Python 访问。 [ [论文-2013](https://academic.oup.com/bioinformatics/article/29/23/3003/248468) ]
- **[pyensembl](https://github.com/openvax/pyensembl)** - 对 Ensembl 数据库的 Pythonic 访问。 [ [网络](https://pyensembl.readthedocs.io/en/latest/pyensembl.html) ]
- **[bioservices](https://github.com/coelaer/bioservices)** - 从 Python 访问生物 Web 服务。 [ [paper-2013](https://academic.oup.com/bioinformatics/article/29/24/3241/194040) [web](http://bioservices.readthedocs.io) ]

#### 工具

- **[cyvcf](https://github.com/arq5x/cyvcf)** - 使用 Cython 提高速度的 [pyVCF](https://github.com/jamescasbon/PyVCF) 端口。
- **[cyvcf2](https://github.com/brentp/cyvcf2)** - Cython + HTSlib == 快速 VCF 解析；解析速度甚至比 pyVCF 还要快。 [ [论文-2017](https://pubmed.ncbi.nlm.nih.gov/28165109) | [网络](https://brentp.github.io/cyvcf2)]
- **[polars-bio](https://github.com/biodatageeks/polars-bio)** - 用于在 Polars DataFrames 上进行超快速基因组间隔操作和基因组文件格式 I/O 的 Python 库 [[paper-2025](https://doi.org/10.1093/bioinformatics/btaf640) | [ [网络](https://biodatageeks.org/polars-bio/) ] ]
- **[pyBedTools](https://github.com/daler/pybedtools)** - [bedtools](https://github.com/arq5x/bedtools) 的 Python 包装器。 [ [论文-2011](https://pubmed.ncbi.nlm.nih.gov/21949271) | [网络](http://daler.github.io/pybedtools)]
- **[pyfaidx](https://github.com/mdshw5/pyfaidx)** - 对 FASTA 文件的 Python 访问。
- **[pysam](https://github.com/pysam-developers/pysam)** - [samtools](https://github.com/samtools/samtools) 的 Python 包装器。 [ [web](https://pysam.readthedocs.io/en/latest/api.html) ]
- **[pyVCF](https://github.com/jamescasbon/PyVCF)** - 用于 Python 的 VCF 解析器。 [ [web](http://pyvcf.readthedocs.org/en/latest/index.html) ]
- **[Scanpy](https://github.com/scverse/scanpy)** - 用于分析单细胞基因表达数据的可扩展工具包，包括预处理、可视化、聚类和轨迹推断。 [ [论文-2018](https://doi.org/10.1186/s13059-017-1382-0) | [网络](https://scanpy.readthedocs.io)]

### 组装
- **[SPAdes](https://github.com/ablab/spades)** - SPAdes（圣彼得堡基因组组装程序）是一个组装工具包，包含各种组装管道和原核基因组组装的事实上的标准。
- **[SKESA](https://github.com/ncbi/SKESA)** - SKESA 是微生物基因组的从头序列读取组装程序。它使用保守启发法，旨在在基因组的重复区域创建断裂。这会带来优异的序列质量，而不会显着影响连续性。
- **[Minimap2](https://github.com/lh3/minimap2)** - Minimap2 是基因组和剪接核苷酸序列的成对比对器。它可以执行程序集到程序集的对齐，并适用于 gzip 的 FASTQ、FASTA 格式。它还发现长读之间的重叠。
- **[D-GENIES](https://dgenies.toulouse.inra.fr/)** - **D**不会以**I**互动、**E**高效且**S**简单的方式绘制大型**基因组。它是一个在线工具，旨在支持大型基因组、比较两个基因组，并且您可以与点图交互以改善可视化效果。它还可以通过将 PAF（Pairwise mApping Format）或 MAF（Multiple Alignment File）对齐文件生成的输出上传到 D-GENIES 来扩展 minimap2

### 注释
- **[Prokka](https://github.com/tseemann/prokka)** - Prokka：快速原核基因组注释。 Prokka 是最常被引用的微生物基因组注释命令行工具之一。
- **[Bakta](https://github.com/oschwengers/bakta)** - Bakta 是一种快速、标准化注释细菌基因组和质粒的工具。它以机器可读的 JSON 和生物信息学标准文件格式提供丰富的 dbxref 和包含 sORF 的注释，用于自动下游分析。

## 长读长测序

### 长读汇编

- **[canu](https://github.com/marbl/canu)** - 适用于大大小小的基因组的单分子序列组装器。
- **[flye](https://github.com/fenderglass/Flye)** - 使用重复图进行单分子测序读取的从头组装器。
- **[hifiasm](https://github.com/chhylp123/hifiasm)** - 用于准确 Hifi 读取的单倍型解析汇编程序。
- **[wtdbg2](https://github.com/ruanjue/wtdbg2)** - 用于长噪声读取组装的模糊 Bruijn 图方法

## 可视化

### 基因组浏览器/基因图

以下工具可用于可视化基因组数据或构建基因组数据的定制可视化，包括来自 DNA-Seq、RNA-Seq 和 ChIP-Seq、变体等的序列数据。

- **[Squiggle](https://github.com/Lab41/squiggle)** - 易于使用的 DNA 序列可视化工具，可将 FASTA 文件转换为基于浏览器的可视化。 [ [论文-2018](https://pubmed.ncbi.nlm.nih.gov/30247632) | [网络](https://squiggle.readthedocs.io/en/latest/)]
- **[biodalliance](https://github.com/dasmoth/dalliance)** - 可嵌入的基因组查看器。集成来自各种来源的数据，并且可以直接从流行的基因组学文件格式（包括 bigWig、BAM 和 VCF）加载数据。
[ [论文-2011](https://pubmed.ncbi.nlm.nih.gov/21252075) | [网络](http://www.biodalliance.org) ]
- **[BioJS](https://github.com/biojs/biojs)** - BioJS 是一个包含一百多个 JavaScript 组件的库，使您能够使用当前的 Web 技术可视化和处理数据。 [ [论文-2014](https://pubmed.ncbi.nlm.nih.gov/25075290/) | [网络](http://biojs.net/)]
- **[Circleator](https://github.com/jonathancrabtree/Circleator)** - 使用 BioPerl 和 SVG 对基因组相关数据进行灵活的循环可视化。 [ [论文-2014](https://pubmed.ncbi.nlm.nih.gov/25075113) ]
- **[DNAism](https://github.com/drio/dnaism)** - 用于 DNA 数据的基于 Horizon Chart D3 的 JavaScript 库。 [ [论文-2016](https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-016-0891-2) | [网络](http://drio.github.io/dnaism/)]
- **[IGV js](https://github.com/igvteam/igv)** - 基于 Java 的浏览器。快速、高效、可扩展的基因组数据和注释可视化工具。处理多种格式。 [ [论文-2019](https://pubmed.ncbi.nlm.nih.gov/31099383) | [网络](https://software.broadinstitute.org/software/igv)]
- **[Island Plot](https://github.com/lairdm/islandplot)** - 基于 D3 JavaScript 的基因组查看器。构造 SVG。 [ [论文-2015](https://pubmed.ncbi.nlm.nih.gov/25916842/) ]
- **[JBrowse](https://github.com/GMOD/jbrowse)** - JavaScript 基因组浏览器，可通过插件和跟踪自定义进行高度定制。 [ [论文-2016](https://pubmed.ncbi.nlm.nih.gov/27072794) | [网络](http://jbrowse.org/)]
- **[PHAT](https://github.com/chgibb/PHAT)** - 用于分析和可视化下一代测序数据集的点击式跨平台套件。 [ [论文-2018](https://pubmed.ncbi.nlm.nih.gov/30561651) | [网络](https://chgibb.github.io/PHATDocs)]
- **[pileup.js](https://github.com/hammerlab/pileup.js)** - JavaScript 库，可用于生成交互式且高度可定制的基于 Web 的基因组浏览器。 [ [论文-2016](https://pubmed.ncbi.nlm.nih.gov/27153605) ]
- **[scribl](https://github.com/chmille4/Scribl)** - 用于绘制基于画布的基因图的 JavaScript 库。 [ [论文-2012](https://pubmed.ncbi.nlm.nih.gov/23172864) | [网络](http://chmille4.github.io/Scribl)]
- **Lucid Align** - 现代序列比对查看器。 [ [网络](https://lucidalign.com) ]

### 马戏团相关

- **[Circos](https://github.com/vigsterkr/circos)** - 用于圆形图的 Perl 软件包，非常适合基因组重排。 [ [论文-2009](https://pubmed.ncbi.nlm.nih.gov/19541911) | [网络](http://circos.ca) ]
- **ClicO FS** - Circos 的基于网络的交互式服务。 [ [论文-2015](https://pubmed.ncbi.nlm.nih.gov/26227146) ]
- **OmicCircos** - 用于组学数据圆形图的 R 包。 [ [论文-2014](https://pubmed.ncbi.nlm.nih.gov/24526832) | [网络](http://www.bioconductor.org/packages/release/bioc/html/OmicCircos.html)]
- **J-Circos** - 用于与 Circos 绘图进行交互工作的 Java 应用程序。 [ [论文-2014](https://pubmed.ncbi.nlm.nih.gov/25540184) | [网络](http://www.australianprostatecentre.org/research/software/jcircos) ]
- **[rCircos](https://bitbucket.org/henryhzhang/rcircos/src/master/)** - 用于圆形图的 R 包。 [ [论文-2013](https://pubmed.ncbi.nlm.nih.gov/23937229) | [网络](http://watson.nci.nih.gov/cran_mirror/web/packages/RCircos/index.html)]
- **[fujiplot](https://github.com/mkanai/fujiplot)** - 多个 GWAS 结果的 circos 表示。 [ [论文-2018](https://www.nature.com/articles/s41588-018-0047-6) ]

## 数据库访问

- [Entrez Direct: E-utilities on the UNIX command line](http://www.ncbi.nlm.nih.gov/books/NBK179288/) - 用于以编程方式访问 NCBI 数据库的 UNIX 命令行工具。安装说明和示例可在链接中找到。

## 资源

### 成为一名生物信息学家

- [什么是生物信息学家](http://blog.fejes.ca/?p=2418)
- [生物信息学课程指南：核心能力的定义](http://www.ploscompbiol.org/article/info:doi%2F10.1371%2Fjournal.pcbi.1003496)
- [攻读博士学位的 N 大理由或生物信息学/计算生物学博士后](http://caseybergman.wordpress.com/2012/07/31/top-n-reasons-to-do-a-ph-d-or-post-doc-in-bioinformaticscomputational-biology/)
- [A 10-Step Guide to Party Conversation For Bioinformaticians](https://genomebiology.biomedcentral.com/articles/10.1186/gb-2013-14-1-104) - 以下是关于如何向未参与该领域的人传达概念的分步指南，当被问到“那么，你会做什么？”
- [A History Of Bioinformatics (In The Year 2039)](https://www.youtube.com/watch?v=uwsjwMO-TEA) - C. Titus Brown 的演讲，讲述了他对 2039 年生物信息学的回顾。他的演讲笔记可以在[此处](http://ivory.idyll.org/blog/2014-bosc-keynote.html) 找到。
- [A farewell to bioinformatics](https://madhadron.com/science/farewell_to_bioinformatics.html) - 对生物信息学现状的批判性观点。
- [A Series of Interviews with Notable Bioinformaticians](http://www.acgt.me/blog/2014/3/25/101-questions-a-new-series-of-interviews-with-notable-bioinformaticians) - Keith Bradnam 博士“认为向一群著名的生物信息学家提出一系列简单的问题来评估他们对生物信息学研究现状的感受可能会很有启发性，并且可能会得到一些对他们的生物信息学职业有用的建议。”
- [Open Source Society University on Bioinformatics](https://github.com/ossu/bioinformatics) - 对于那些想要在自己的时间免费完成世界上最好的大学的生物信息学课程的人来说，这是一条坚实的道路。
- [Rosalind](http://rosalind.info/) - Rosalind 是一个通过解决问题来学习生物信息学的平台。
- [A guide for the lonely bioinformatician](http://www.opiniomics.org/a-guide-for-the-lonely-bioinformatician/) - 本指南针对生物信息学家，旨在指导他们更好的职业发展。
- [生物信息学简史](https://doi.org/10.1093/bib/bby063)

### GitHub 上的生物信息学

- [Awesome-alternative-splicing](https://github.com/HussainAther/awesome-alternative-splicing) - 有关选择性剪接的资源列表，包括软件、数据库和其他工具。
- [Awesome AI-based Protein Design](https://github.com/opendilab/awesome-AI-based-protein-design) - 基于人工智能的蛋白质设计的研究论文集。

### 测序

- [下一代测序技术 - Elaine Mardis (2014)](https://youtu.be/6Is3W7JkFp8) [1:34:35] - 下一代和第三代测序技术的出色（技术）概述，以及癌症研究中的一些应用。
- [Annotated bibliography of \*Seq assays](https://liorpachter.wordpress.com/seq/) - 约 100 篇关于各种测序技术和分析（从转录到转座元件发现）的论文列表。
- [For all you seq... (PDF)](http://www.Illumina.com/content/dam/Illumina-marketing/documents/applications/ngs-library-prep/ForAllYouSeqMethods.pdf) (3456x5471) - Illumina 提供的海量信息图，说明了多种测序技术的工作原理。技术涵盖蛋白质-蛋白质相互作用、RNA转录、RNA-蛋白质相互作用、RNA低水平检测、RNA修饰、RNA结构、DNA重排和标记、DNA低水平检测、表观遗传学和DNA-蛋白质相互作用。包括参考文献。

### RNA测序

- [Review papers on RNA-seq (Biostars)](https://www.biostars.org/p/52152/) - 包括许多有关 RNA-seq 和分析方法的开创性论文。
- [Informatics for RNA-seq: A web resource for analysis on the cloud](https://github.com/griffithlab/rnaseq_tutorial) - 有关使用 Amazon AWS 云服务在云中执行 RNA-seq 分析的教育资源。主题包括准备数据、预处理、差异表达、异构体发现、数据可视化和解释。
- [RNA-seqlopedia](http://rnaseq.uoregon.edu/) - RNA-seqlopedia 提供了 RNA-seq 的精彩概述以及成功进行 RNA-seq 实验所需的选择。
- [A survey of best practices for RNA-seq data analysis](http://genomebiology.biomedcentral.com/articles/10.1186/s13059-016-0881-8) - 为 RNA-seq 计算分析提供了很棒的路线图，包括挑战/障碍和需要注意的事项，以及如何将 RNA-seq 数据与其他数据类型集成。
- [增刊中的故事](https://www.youtube.com/watch?v=5NiFibnbE8o) [46:39] - Lior Pachter 博士分享了他在著名 RNA-seq 分析软件 CuffDiff 和 [Cufflinks](http://cole-trapnell-lab.github.io/cufflinks/) 增刊中的故事，并解释了它们的一些方法。
- [List of RNA-seq Bioinformatics Tools](https://en.wikipedia.org/wiki/List_of_RNA-Seq_bioinformatics_tools) - 维基百科上有分析所需的 RNA-seq 生物信息学工具的详细列表，范围涵盖分析流程的所有部分，包括质量控制、比对、剪接分析和可视化。
- [RNA-seq Analysis](https://github.com/crazyhottommy/RNA-seq-analysis) - [@crazyhottommy](https://github.com/crazyhottommy) 关于进行 RNA-seq 分析时的各种步骤和注意事项的注释。

### 芯片测序

- [ChIP-seq analysis notes from Tommy Tang](https://github.com/crazyhottommy/ChIP-seq-analysis) - 有关 ChIP-seq 数据的资源，包括论文、方法、软件链接和分析。

### YouTube 频道和播放列表

- [Current Topics in Genome Analysis 2016](https://www.genome.gov/12514288/current-topics-in-genome-analysis-2016-course-syllabus-handouts-and-videos/) - NIH 举办了 14 场精彩系列讲座，内容涉及基因组学的当前主题，从序列分析到测序技术，甚至还有基因组医学等更多转化主题。
- [GenomeTV](https://www.youtube.com/user/GenomeTV) - “GenomeTV 是 NHGRI 的官方视频资源集合，从讲座、新闻纪录片到解决基因组研究的研究、问题和临床应用的完整会议视频集。”
- [Leading Strand](https://www.youtube.com/user/LeadingStrand) - 冷泉港实验室 (CSHL) 会议的主题演讲。更多关于[领导链](http://theleadingstrand.cshl.edu/)。
- [Genomics, Big Data and Medicine Seminar Series](https://www.youtube.com/playlist?list=PLqLDR0CTP9_pboZCk6gR9Zn4kW7h9XWJI) - “我们的研讨会致力于 GBM 的关键交叉点，深入研究将深刻塑造未来的‘前沿’技术和方法。”
- [Rafael Irizarry's Channel](https://www.youtube.com/user/RafalabChannel/videos) - Rafael Irizarry 博士关于基因组学统计的讲座和学术讲座。
- [NIH VideoCasting and Podcasting](https://www.youtube.com/user/nihvcast) - “NIH VideoCast 通过互联网以实时流媒体视频形式向全世界观众直播研讨会、会议和会议。”不仅是基因组学和生物信息学视频，还有许多关于生物信息学和基因组学领域特定用途的精彩演讲。

### 博客

- [ACGT](http://www.acgt.me/) - 基思·布拉德南 (Keith Bradnam) 博士撰写了“关于生物学、基因组学以及生物信息学缩略词的虚假使用对人类持续威胁的思考”。
- [Opiniomics](http://www.opiniomics.org/) - 米克·沃森 (Mick Watson) 博士撰写有关生物信息学、基因组和生物学的文章。
- [Bits of DNA](https://liorpachter.wordpress.com/) - Lior Pachter 博士撰写计算生物学评论和评论。
- [it is NOT junk](http://www.michaeleisen.org/blog/) - Michael Eisen 博士撰写“关于基因组、DNA、进化、开放科学、棒球和其他重要事物的博客”
- [#!/perl/bioinfo](https://bioinfoperl.blogspot.com) - EEAD-CSIC 的计算和结构生物学小组用西班牙语和英语撰写有关植物基因组学、计算和结构生物学问题的想法和代码。

### 杂项

- [The Leek group guide to genomics papers](https://github.com/jtleek/genomicspapers/) - 专业策划的基因组学论文，可帮助您快速了解基因组学、RNA-seq、统计学（用于基因组学）、软件开发等领域。
- [A New Online Computational Biology Curriculum](https://doi.org/10.1371/journal.pcbi.1003662) - “本文介绍了数百个免费视频课程的目录，这些课程对于那些希望扩展生物信息学和计算生物学知识的人来说可能会感兴趣。这些课程以大学院系为模型分为 11 个学科领域，并附有评论和职业建议。”
- [How Perl Saved the Human Genome Project](http://www.foo.be/docs/tpj/issues/vol1_2/tpj0102-0001.html) - Lincoln D. Stein 讲述了 Perl 编程语言在人类基因组计划中的重要性。
- [Educational Papers from Nature Biotechnology and PLoS Computational Biology](https://liacs.leidenuniv.nl/~hoogeboomhj/mcb/nature_primer.html) - 有关计算生物学和生物信息学中使用的各种方法的入门书和简短教育文章的链接页面。
- [The PeerJ Bioinformatics Software Tools Collection](https://peerj.com/collections/45-bioinformatics-software/) - 由 Keith Crandall 和 Claus White 策划的工具集，旨在整理 PeerJ 中最有趣、创新和相关的生物信息学工具文章。

## 在线网络团体

- [Bioinformatics (on Discord)](https://discord.com/invite/3uxbPns) - 用于一般生物信息学的 Discord 服务器
- [r-bioinformatics](https://www.reddit.com/r/bioinformatics/comments/7ndwm1/rbioinformatics_slack_channel_and_an_open_call/) - r/bioinformatics 的官方 Slack 工作区（[直接向 apfejes 发送消息reddit](https://www.reddit.com/message/compose/?to=apfejes&subject=Request%20to%20join%20the%20r/bioinformatics %20Slack%20group&message=I%20would%20like%20to%20request%20to%20join%20the%20r/生物信息学%20Slack%20group))
- [BioinformaticsGRX](https://bioinformaticsgrx.es/) - 位于西班牙格拉纳达的生物信息学家社区
- [Comunidad de Desarolladores de Software en Bioinformática](https://comunidadbioinfo.github.io/) - 以拉丁美洲为中心的生物信息学家社区
- [COMBINE](https://combine.org.au/) - 奥地利生物信息学学生小组

## 许可证

[![CC0](http://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)
