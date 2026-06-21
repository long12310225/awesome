# 很棒的公鸡 [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[<img src="coq-logo.svg"align="right" width="100" alt="coq-community logo" title="Awesome Coq 是一个 coq-community 项目">](https://github.com/coq-community/manifesto)

> 很棒的 Coq 库、插件、工具和资源的精选列表。

[Coq 证明助手](https://coq.inria.fr) 提供了一种用于编写数学定义、可执行算法和定理的形式语言，以及用于机器检查证明的半交互式开发的环境。

欢迎投稿！首先阅读[贡献指南](https://github.com/coq-community/awesome-coq/blob/master/CONTRIBUTING.md)。

## 内容

- [Projects](#projects)
  - [Frameworks](#frameworks)
  - [用户界面](#user-interfaces)
  - [Libraries](#libraries)
  - [打包和构建管理](#package-and-build-management)
  - [Plugins](#plugins)
  - [谜题和游戏](#puzzles-and-games)
  - [Tools](#tools)
  - [类型理论和数学](#type-theory-and-mathematics)
  - [经过验证的软件](#verified-software)
- [Resources](#resources)
  - [Community](#community)
  - [Blogs](#blogs)
  - [Books](#books)
  - [课程资料](#course-material)
  - [教程和提示](#tutorials-and-hints)

---

## 项目

### 框架

- [ConCert](https://github.com/AU-COBRA/ConCert) - 智能合约测试和验证框架，具有多种智能合约语言的代码提取管道。
- [CoqEAL](https://github.com/CoqEAL/CoqEAL) - 用于简化证明中数据表示的更改的框架。
- [FCF](https://github.com/adampetcher/fcf) - 密码学证明框架。
- [Fiat](https://github.com/mit-plv/fiat) - 主要是构建正确程序的自动合成。
- [FreeSpec](https://github.com/lthms/FreeSpec) - 使用效果和效果处理程序模块化验证程序的框架。
- [Hoare Type Theory](https://github.com/imdea-software/htt/) - 顺序分离逻辑的浅嵌入被表述为类型理论。
- [Hybrid](https://www.site.uottawa.ca/~afelty/HybridCoq/) - 使用对象逻辑的高阶抽象语法表示进行推理的系统。
- [Iris](https://iris-project.org) - 高阶并发分离逻辑框架。
- [Q\*cert](https://github.com/querycert/qcert) - 用于实现和验证查询编译器的平台。
- [SSProve](https://github.com/SSProve/ssprove) - 基于数学组件库的模块化密码证明框架。
- [VCFloat](https://github.com/VeriNum/vcfloat) - 使用浮点计算验证 C 程序的框架。
- [Verdi](https://github.com/uwplse/verdi) - 用于正式验证分布式系统实现的框架。
- [VST](https://vst.cs.princeton.edu) - 用于在 Coq 内以高阶并发、命令式分离逻辑验证 C 代码的工具链，该逻辑是健全的。 CompCert 编译器的 Clight 语言。

### 用户界面

- [CoqIDE](https://coq.inria.fr/refman/practical-tools/coqide.html) - 用于与 Coq 交互的独立图形工具。
- [Coqtail](https://github.com/whonore/Coqtail) - 基于 Vim 文本编辑器的 Coq 界面。
- [Coq LSP](https://github.com/ejgallego/coq-lsp) - 用于 Visual Studio Code 和 VSCodium 编辑器的语言服务器和扩展，具有自定义文档检查引擎。
- [Proof General](https://proofgeneral.github.io) - 基于可扩展、可定制文本编辑器 Emacs 的校对助手通用界面。
- [Company-Coq](https://github.com/cpitclaudel/company-coq) - Proof General 的 Coq 模式的 IDE 扩展。
- [opam-switch-mode](https://github.com/ProofGeneral/opam-switch-mode) - Proof General 的 IDE 扩展可从菜单或使用命令在本地更改或重置 opam 开关。
- [jsCoq](https://github.com/jscoq/jscoq) - 将 Coq 移植到 JavaScript，从而可以在浏览器中运行 Coq 项目。
- [Jupyter kernel for Coq](https://github.com/EugeneLoy/coq_jupyter) - Coq 对 Jupyter Notebook Web 环境的支持。
- [VsCoq](https://github.com/coq-community/vscoq) - Visual Studio Code 和 VSCodium 编辑器的语言服务器和扩展。
- [VsCoq Legacy](https://github.com/coq-community/vscoq/tree/vscoq1) - 使用 Coq 旧版 XML 协议的 Visual Studio Code 和 VSCodium 编辑器的向后兼容扩展。
- [Waterproof editor](https://github.com/impermeable/waterproof) - 在交互式笔记本中编写数学证明的教育环境。
- [Tree Sitter Rocq](https://github.com/lamg/tree-sitter-rocq) - 部分 Rocq 树保护语法对于在文本编辑器（如 [Helix](https://github.com/helix-editor/helix)）中语法突出显示很有用，但不建议用于完全解析 Rocq 代码。

### 图书馆

- [ALEA](https://github.com/coq-community/alea) - 用于随机算法推理的库。
- [Algebra Tactics](https://github.com/math-comp/algebra-tactics) - 数学部分的环场战术。
- [Bignums](https://github.com/coq/bignums) - 任意大数的库。
- [Bedrock Bit Vectors](https://github.com/mit-plv/bbv) - 用于对固定精度机器字进行推理的库。
- [CertiGraph](https://github.com/Salamari/CertiGraph) - 用于推理有向图及其在分离逻辑中的嵌入的库。
- [CoLoR](https://github.com/fblanqui/color) - 有关重写理论、lambda 演算和终止的库，以及扩展 Coq 标准库的通用数据结构的子库。
- [coq-haskell](https://github.com/jwiegley/coq-haskell) - 库让 Haskell 用户顺利过渡到 Coq。
- [Coq-Kruskal](https://github.com/DmxLarchey/Coq-Kruskal) - 与玫瑰树和克鲁斯卡尔树定理相关的库集合。
- [CoqInterval](https://gitlab.inria.fr/coqinterval/interval/) - 对实数表达式进行不等式证明的策略。
- [Coq record update](https://github.com/tchajed/coq-record-update) - 库提供了更新 Coq 记录字段的通用方法。
- [Coq-std++](https://gitlab.mpi-sws.org/iris/stdpp) - Coq 的扩展替代标准库。
- [ExtLib](https://github.com/coq-community/coq-ext-lib) - 可能对其他 Coq 开发有用的理论和插件的集合。
- [FCSL-PCM](https://github.com/imdea-software/fcsl-pcm) - 用于验证指针操作程序的部分交换幺半群的形式化。
- [Flocq](https://gitlab.inria.fr/flocq/flocq) - 浮点数和计算的形式化。
- [Formalised Undecidable Problems](https://github.com/uds-psl/coq-library-undecidability) - 不可判定问题及其之间的约简库。
- [Hahn](https://github.com/vafeiadis/hahn) - 用于对列表和二元关系进行推理的库。
- [Interaction Trees](https://github.com/DeepSpec/InteractionTrees) - 用于表示递归和不纯程序的库。
- [LibHyps](https://github.com/Matafou/LibHyps) - Ltac 策略库用于管理和操纵证明中的假设。
- [MathComp Extra](https://github.com/thery/mathcomp-extra) - 数学组件库的额外材料，包括 AKS 素性测试和 RSA 加密和解密。
- [Mczify](https://github.com/math-comp/mczify) - 库使 Micromega 算术求解器能够在使用数学组件数字定义时工作。
- [Metalib](https://github.com/plclub/metalib) - 使用本地无名变量绑定表示的编程语言元理论库。
- [Paco](http://plv.mpi-sws.org/paco/) - 用于参数化共归纳的库。
- [Regular Language Representations](https://github.com/coq-community/reglang) - 正则语言不同定义之间的翻译，包括正则表达式和自动机。
- [Relation Algebra](https://github.com/damien-pous/relation-algebra) - 以异构二元关系作为模型的代数的模块化形式化。
- [Simple IO](https://github.com/Lysxia/coq-simple-io) - 具有用户可定义原语操作的输入/输出单子。
- [TLC](https://github.com/charguer/tlc) - Coq 标准库的非建设性替代方案。

### 打包和构建管理

- [coq_makefile](https://coq.inria.fr/refman/practical-tools/utilities.html) - 与 Coq 一起分发并基于生成 makefile 的构建工具。
- [Coq Nix Toolbox](https://github.com/coq-community/coq-nix-toolbox) - Nix 帮助程序脚本可自动执行 Coq 的本地构建和持续集成。
- [Coq Package Index](https://coq.inria.fr/opam/www/) - 基于 opam 的 Coq 包集合。
- [Coq Platform](https://github.com/coq/platform) - 精心策划的软件包集合，支持 Coq 在工业、教育和研究中的使用。
- [coq-community Templates](https://github.com/coq-community/templates) - 用于为 Coq 项目生成配置文件的模板。
- [Debian Coq packages](https://people.debian.org/~jpuydt/coq_platform.html) - Debian 测试发行版中提供了与 Coq 相关的软件包。
- [Docker-Coq](https://github.com/coq-community/docker-coq) - 许多版本的 Coq 的 Docker 镜像。
- [Docker-MathComp](https://github.com/math-comp/docker-mathcomp) - Coq 和数学组件库的多种版本组合的 Docker 镜像。
- [Docker-Coq GitHub Action](https://github.com/marketplace/actions/docker-coq-action) - 可与 Docker-Coq 或 Docker-MathComp 一起使用的 GitHub 容器操作。
- [Dune](https://dune.build) - 适用于 OCaml 和 Coq（以前的 jbuilder）的可组合且固定的构建系统。
- [Nix](https://nixos.org/nix/) - 适用于 Linux 和其他 Unix 系统的包管理器，支持原子升级和回滚。
- [Nix Coq packages](https://search.nixos.org/packages?channel=unstable&query=coqPackages) - Nix 的 Coq 相关包集合。
- [opam](https://opam.ocaml.org) - 适用于 OCaml 和 Coq 的灵活且 Git 友好的包管理器，具有多个编译器支持。

### 插件

- [AAC Tactics](https://github.com/coq-community/aac-tactics) - 重写通用量化方程、某些算子的模结合性和交换律的策略。
- [Coinduction](https://github.com/damien-pous/coinduction) - 用于通过增强共归纳进行证明的插件。
- [Coq-Elpi](https://github.com/LPCIC/coq-elpi) - 基于 λProlog 的扩展框架提供了广泛的 API 来实施命令和策略。
- [CoqHammer](https://github.com/lukaszcz/coqhammer) - 通用自动推理锤工具，将先前证明的学习与将问题转化为自动证明者以及重建找到的证明相结合。
- [Equations](https://github.com/mattam82/Coq-Equations) - Coq 的函数定义包。
- [Gappa](https://gitlab.inria.fr/gappa/coq) - 解决浮点运算和舍入误差目标的策略。
- [Hierarchy Builder](https://github.com/math-comp/hierarchy-builder) - 用于声明基于打包类的 Coq 层次结构的命令集合。
- [Itauto](https://gitlab.inria.fr/fbesson/itauto) - 类似于 SMT 的策略，用于对函数符号、构造函数和算术进行组合命题推理。
- [Ltac2](https://coq.inria.fr/refman/proof-engine/ltac2.html) - 实验性类型化策略语言，类似于 Coq 的经典 Ltac 语言。
- [MetaCoq](https://github.com/MetaCoq/metacoq) - 项目在 Coq 中正式化 Coq，并提供用于操作 Coq 术语和开发经过认证的插件的工具。
- [Mtac2](https://github.com/Mtac2/Mtac2) - 插件添加了向后推理的类型化策略。
- [Paramcoq](https://github.com/coq-community/paramcoq) - 用于生成 Coq 术语的参数化翻译的插件。
- [QuickChick](https://github.com/QuickChick/QuickChick) - 用于基于属性的随机测试的插件。
- [SMTCoq](https://github.com/smtcoq/smtcoq) - 用于检查来自外部 SAT 和 SMT 求解器的证据的工具。
- [Tactician](https://coq-tactician.github.io) - 交互式工具，它从所有已安装的 Coq 包中先前编写的策略脚本中学习，并建议下一个要执行的策略或尝试完全自动化证明合成。
- [Unicoq](https://github.com/unicoq/unicoq) - 用增强型算法替换现有统一算法的插件。
- [Waterproof proof language](https://github.com/impermeable/coq-waterproof) - 插件提供一种语言，用于以类似于非机械化数学证明的风格编写证明脚本。

### 谜题和游戏

- [Coqoban](https://github.com/coq-community/coqoban) - Coq 实现了 Sokoban（日本仓库管理员游戏）。
- [Hanoi](https://github.com/thery/hanoi) - Coq 中的汉诺塔谜题，包括有关配置的概括和定理。
- [Mini-Rubik](https://github.com/thery/minirubik) - 魔方拼图 2x2x2 版本的 Coq 形式化和求解器。
- [Name the Biggest Number](https://github.com/codyroux/name-the-biggest-number) - 用于提交 Coq 中最大数字头衔的经过验证的竞争者的存储库。
- [Natural Number Game](https://github.com/uncomputable/natural-number-game) - 为精益证明者开发的自然数游戏的 Coq 版本。
- [Sudoku](https://github.com/coq-community/sudoku) - Coq 中数独数字放置难题的形式化和求解器。
- [T2048](https://github.com/thery/T2048) - 2048 滑动瓷砖游戏的 Coq 版本。

### 工具

- [Alectryon](https://github.com/cpitclaudel/alectryon) - 用于编写混合 Coq 代码和散文的技术文档的工具集合。
- [Autosubst-ocaml](https://github.com/uds-psl/autosubst-ocaml) - 生成 Coq 代码的工具，用于处理语法中的绑定器，例如重命名和替换。
- [CFML](https://gitlab.inria.fr/charguer/cfml2) - 用于证明 OCaml 程序在分离逻辑中的属性的工具。
- [coq2html](https://github.com/xavierleroy/coq2html) - Coq 的替代 HTML 文档生成器。
- [coqdoc](https://coq.inria.fr/refman/using/tools/coqdoc.html) - 标准文档工具，可从 Coq 代码生成 LaTeX 或 HTML 文件。
- [CoqOfOCaml](https://github.com/clarus/coq-of-ocaml) - 用于从 OCaml 代码生成惯用 Coq 的工具。
- [coq-dpdgraph](https://github.com/coq-community/coq-dpdgraph) - 用于在 Coq 对象之间构建依赖关系图的工具。
- [coq-scripts](https://github.com/JasonGross/coq-scripts) - 用于处理 Coq 文件的脚本，包括将证明时间制成表格。
- [coq-tools](https://github.com/JasonGross/coq-tools) - 用于操纵 Coq 开发的脚本。
  - [`find-bug.py`](https://github.com/JasonGross/coq-tools/blob/master/find-bug.py) - 自动最小化产生错误的源文件，为 Coq 错误创建小型测试用例。
  - [`absolutize-imports.py`](https://github.com/JasonGross/coq-tools/blob/master/absolutize-imports.py) - 处理源文件以使依赖项的加载对文件名的阴影具有鲁棒性。
  - [`inline-imports.py`](https://github.com/JasonGross/coq-tools/blob/master/inline-imports.py) - 通过内联加载所有依赖项，从开发中创建独立的源文件。
  - [`minimize-requires.py`](https://github.com/JasonGross/coq-tools/blob/master/minimize-requires.py) - 删除未使用的依赖项的加载。
  - [`move-requires.py`](https://github.com/JasonGross/coq-tools/blob/master/move-requires.py) - 将所有依赖项加载语句移至源文件的顶部。
  - [`move-vernaculars.py`](https://github.com/JasonGross/coq-tools/blob/master/move-vernaculars.py) - 从证明脚本块中提出许多白话命令和内部引理。
  - [`proof-using-helper.py`](https://github.com/JasonGross/coq-tools/blob/master/proof-using-helper.py) - 修改源文件以包含证明注释，以加快并行证明速度。
- [Cosette](https://github.com/uwdb/Cosette) - 用于推理 SQL 查询等价性的自动求解器。
- [hs-to-coq](https://github.com/plclub/hs-to-coq) - 从 Haskell 代码到等效 Coq 代码的转换器。
- [lngen](https://github.com/plclub/lngen) - 用于生成本地无名 Coq 定义和证明的工具。
- [Menhir](http://gallium.inria.fr/~fpottier/menhir/) - 解析器生成器可以为经过验证的解析器输出 Coq 代码。
- [mCoq](https://github.com/EngineeringSoftware/mcoq) - Coq 项目的突变分析工具。
- [Ott](https://github.com/ott-lang/ott) - 用于编写可翻译为 Coq 的编程语言和演算定义的工具。
- [PyCoq](https://github.com/ejgallego/pycoq) - 用于从 Python 3 内部与 Coq 交互的一组绑定和库。
- [Rocqnavi](https://github.com/affeldt-aist/rocqnavi) - coq2html 的分支，添加了索引、可点击符号、注释中的 Markdown 和 LaTeX 格式等。
- [Roosterize](https://github.com/EngineeringSoftware/roosterize) - 用于在 Coq 项目中建议引理名称的工具。
- [Sail](https://github.com/rems-project/sail) - 用于指定处理器的指令集架构 (ISA) 语义并生成 Coq 定义的工具。
- [SerAPI](https://github.com/ejgallego/coq-serapi) - 用于 Coq 代码与 JSON 和 S 表达式之间的序列化（反序列化）的工具和 OCaml 库。
- [Trakt](https://github.com/ecranceMERCE/trakt) - 用于证明自动化策略的通用目标预处理工具。

### 类型理论和数学

- [Analysis](https://github.com/math-comp/analysis) - 与数学组件兼容的经典实分析库。
- [Category Theory in Coq](https://github.com/jwiegley/category-theory) - 范畴论的无公理形式化。
- [Completeness and Decidability of Modal Logic Calculi](https://github.com/coq-community/comp-dec-modal) - 逻辑 K、K*、CTL 和 PDL 的健全性、完整性和可判定性。
- [CoqPrime](https://github.com/thery/coqprime) - 使用 Pocklington 和椭圆曲线证书证明素数的库。
- [CoRN](https://github.com/coq-community/corn) - 建设性实分析和代数库。
- [Coqtail Math](https://github.com/coq-community/coqtail-math) - 数学结果库，范围从算术到实际分析和复杂分析。
- [Coquelicot](https://gitlab.inria.fr/coquelicot/coquelicot) - 经典实分析的形式化，与标准库兼容并注重可用性。
- [Finmap](https://github.com/math-comp/finmap) - 用有限映射、集合和多重集扩展数学组件。
- [Four Color Theorem](https://github.com/coq-community/fourcolor) - 四色定理的形式证明，图论的里程碑式成果。
- [Gaia](https://github.com/coq-community/gaia) - 布尔巴基《数学原理》书籍的实现，包括集合论和数论。
- [GeoCoq](https://github.com/GeoCoq/GeoCoq) - 基于塔斯基公理系统的几何形式化。
- [Graph Theory](https://github.com/coq-community/graph-theory) - 形式化的图论结果。
- [Homotopy Type Theory](https://github.com/HoTT/Coq-HoTT) - 同伦理论思想的发展。
- [Infotheo](https://github.com/affeldt-aist/infotheo) - 信息论和线性纠错码的形式化。
- [Mathematical Components](http://math-comp.github.io) - 数学理论的形式化，特别关注群论。
- [Math Classes](https://github.com/coq-community/math-classes) - 基于类型类的数学结构的抽象接口。
- [Monae](https://github.com/affeldt-aist/monae) - 一元效应和等式推理。
- [Odd Order Theorem](https://github.com/math-comp/odd-order) - 奇数阶定理的形式证明，是有限群论的里程碑式成果。
- [Puiseuxth](https://github.com/roglo/puiseuxth) - Puiseux 定理的证明和 Puiseux 级数多项式根的计算。
- [UniMath](https://github.com/UniMath/UniMath) - 旨在使用统一观点形式化大量数学的图书馆。

### 经过验证的软件

- [CompCert](http://compcert.inria.fr) - 适用于几乎所有 C 语言 (ISO C99) 的高保证编译器，为 PowerPC、ARM、RISC-V 和 x86 处理器生成高效代码。
- [Ceramist](https://github.com/certichain/ceramist) - 经过验证的基于哈希的近似成员资格结构，例如布隆过滤器。
- [CertiCoq](https://github.com/CertiCoq/certicoq) - 经过验证的编译器，从 Coq 的内部语言 Gallina 到 CompCert 的 Clight 语言。
- [Fiat-Crypto](https://github.com/mit-plv/fiat-crypto) - 密码原始代码生成。
- [Functional Algorithms Verified in SSReflect](https://github.com/clayrat/fav-ssr) - 用于搜索、排序和其他基本问题的算法的纯功能验证实现。
- [Incremental Cycles](https://gitlab.inria.fr/agueneau/incremental-cycles) - 已验证图形中增量循环检测算法的 OCaml 实现。
- [Jasmin](https://github.com/jasmin-lang/jasmin) - 用于高保证和高速加密的形式化语言和经过验证的编译器。
- [JSCert](https://github.com/jscert/jscert) - ECMAScript 5 (JavaScript) 的 Coq 规范以及经过验证的参考解释器。
- [lambda-rust](https://gitlab.mpi-sws.org/iris/lambda-rust) - Rust 核心语言和类型系统的形式模型、类型系统的逻辑关系以及一些 Rust 库的安全证明。
- [Prosa](https://gitlab.mpi-sws.org/RT-PROOFS/rt-proofs) - 实时系统可调度性分析的定义和证明。
- [RISC-V Specification in Coq](https://github.com/mit-plv/riscv-coq) - RISC-V 处理器指令集架构和扩展的定义。
- [Stable sort algorithms in Coq](https://github.com/pi8027/stablesort) - 合并排序函数的正确性（包括稳定性）的通用和模块化证明。
- [Tarjan and Kosaraju](https://github.com/math-comp/tarjan) - 拓扑排序和在有限图中查找强连通分量的算法的验证实现。
- [Vélus](http://velus.inria.fr) - 经过验证的类似 Lustre/Scade 数据流同步语言的编译器。
- [Verdi Raft](https://github.com/uwplse/verdi-raft) - Raft 分布式共识协议的实现，使用 Verdi 框架在 Coq 中进行验证。
- [WasmCert-Coq](https://github.com/WasmCert/WasmCert-Coq/) - WebAssembly（又名 Wasm）1.0 规范在 Coq 中的形式化。

## 资源

### 社区

- [Coq 官方网站](https://coq.inria.fr)
- [Coq 官方手册](https://coq.inria.fr/refman/)
- [Coq 官方标准库](https://coq.inria.fr/stdlib/)
- [官方 Coq Discourse 论坛](https://coq.discourse.group)
- [Coq Zulip 官方聊天](https://coq.zulipchat.com)
- [Coq-Club 官方邮件列表](https://sympa.inria.fr/sympa/arc/coq-club)
- [Coq 官方 wiki](https://github.com/coq/coq/wiki)
- [官方 Coq X/Twitter](https://x.com/CoqLang)
- [Coq Zulip 聊天档案](https://coq.gitlab.io/zulip-archive/)
- [Coq Reddit 子版块](https://www.reddit.com/r/Coq/)
- [Stack Overflow 上的 Coq 标签](https://stackoverflow.com/questions/tagged/coq)
- [理论计算机科学堆栈交换上的 Coq 标签](https://cstheory.stackexchange.com/questions/tagged/coq)
- [Proof Assistants Stack Exchange 上的 Coq 标签](https://proofassistants.stackexchange.com/questions/tagged/coq)
- [Zenodo 上的 Coq 关键字](https://zenodo.org/search?q=keywords%3A%22Coq%22)
- [Coq-社区包维护项目](https://github.com/coq-community/manifesto)
- [数学组件维基](https://github.com/math-comp/math-comp/wiki)
- [使用 Coq 证明的 100 个著名定理](https://github.com/coq-community/coq-100-theorems)
- [Planet Coq 链接聚合器](https://coq.pl-a.net)

### 博客

- [Coq Exchange：关于 Coq 的想法和实验报告](https://project.inria.fr/coqexchange/news/)
- [Gagallium](http://gallium.inria.fr/blog)
- [格雷戈里·马莱查的博客](https://gmalecha.github.io)
- [Joachim Breitner 在 Coq 上的博客文章](http://www.joachim-breitner.de/blog/tag/Coq)
- [吕夏的博客](https://blog.poisson.chat)
- [Coq 上的 MIT PLV 博客文章](http://plv.csail.mit.edu/blog/category/coq.html)
- [PLC俱乐部博客](https://www.seas.upenn.edu/~plclub/blog/)
- [Poleiro：Arthur Azevedo de Amorim 的 Coq 博客](http://poleiro.info)
- [Ralf Jung 在 Coq 上的博客文章](https://www.ralfj.de/blog/categories/coq.html)
- [Thomas Letan 在 Coq 上的博客文章](https://soap.coffee/~lthms/tags/coq.html)

### 书籍

- [Coq'Art](https://www.labri.fr/perso/casteran/CoqArt/) - 第一本专门介绍 Coq 的书。
- [Software Foundations](https://softwarefoundations.cis.upenn.edu) - 基于 Coq 的逻辑、函数式编程和编程语言基础的系列教科书，旨在供初学者使用。
  - [Volume 1: Logical Foundations](https://softwarefoundations.cis.upenn.edu/lf-current/index.html) - 函数式编程简介、逻辑基本概念和计算机辅助定理证明。
  - [Volume 2: Programming Language Foundations](https://softwarefoundations.cis.upenn.edu/plf-current/index.html) - 介绍编程语言的理论，包括操作语义、霍尔逻辑和静态类型系统。
  - [Volume 3: Verified Functional Algorithms](https://softwarefoundations.cis.upenn.edu/vfa-current/index.html) - 演示如何指定和验证各种基本数据结构。
  - [Volume 4: QuickChick](https://softwarefoundations.cis.upenn.edu/qc-current/index.html) - 介绍将基于属性的随机测试与正式规范和证明相结合的工具。
  - [Volume 5: Verifiable C](https://softwarefoundations.cis.upenn.edu/vc-current/index.html) - 有关使用已验证软件工具链指定和验证 C 程序的扩展教程。
  - [Volume 6: Separation Logic Foundations](https://softwarefoundations.cis.upenn.edu/slf-current/index.html) - 介绍分离逻辑以及如何在其之上构建程序验证工具。
- [Certified Programming with Dependent Types](http://adam.chlipala.net/cpdt/) - 关于 Coq 实际工程的教科书，教授高级实用技巧和非常具体的证明风格。
- [Program Logics for Certified Compilers](https://www.cs.princeton.edu/~appel/papers/plcc.pdf) - 本书解释了如何使用分离逻辑构建程序逻辑，并附有应用于 Clight 编程语言的 Coq 形式模型和其他示例。
- [Formal Reasoning About Programs](http://adam.chlipala.net/frap/) - 本书同时提供了关于程序正确性的形式逻辑推理以及为此目的使用 Coq 的一般介绍。
- [Programs and Proofs](https://ilyasergey.net/pnp/) - 本书对 Coq 中的交互式证明进行了简短且实用的介绍，强调通过 SSReflect 证明语言中的一小组原语对可判定命题进行归纳推理的计算性质。
- [Computer Arithmetic and Formal Proofs](https://www.sciencedirect.com/book/9781785481123/computer-arithmetic-and-formal-proofs) - 本书介绍了如何使用 Flocq 库在 Coq 中正式指定和验证浮点算法。
- [The Mathematical Components book](https://math-comp.github.io/mcb/) - 本书面向数学爱好者，重点关注数学组件库和 SSReflect 证明语言。
- [Modeling and Proving in Computational Type Theory](https://github.com/uds-psl/MPCTT) - 本书涵盖使用 Coq 的计算逻辑主题，包括基础知识、典型案例研究和实用编程。
- [Hydras & Co.](https://github.com/coq-community/hydra-battles) - 关于 Kirby 和 Paris 的九头蛇之战以及 Coq 中其他有趣的形式化数学的书籍和图书馆正在不断开发中，包括哥德尔-罗瑟第一不完备性定理的证明。

### 课程资料

- [An Introduction to MathComp-Analysis](https://staff.aist.go.jp/reynald.affeldt/documents/karate-coq.pdf) - 有关数学组件库入门并将其用于经典推理和实际分析的讲义。
- [Foundations of Separation Logic](https://chargueraud.org/teach/verif/) - 介绍如何在 Coq 中使用分离逻辑来推理顺序命令式程序。
- [Floating-Point Numbers and Formal Proof](https://github.com/thery/FlocqLecture) - Flocq 库中的 Coq 实数和浮点数入门课程。
- [Introduction to the Theory of Computation](https://gitlab.com/umb-svl/turing) - 形式化支持计算理论本科课程，包括语言和图灵机。
- [Lectures on Software Foundations](https://github.com/clarksmr/sf-lectures) - 有关软件基础系列教科书的材料，包括一系列 YouTube 视频。
- [MathComp School](https://github.com/gares/math-comp-school-2022) - Coq 提供课程和练习资源，介绍 SSReflect 证明语言和数学组件库。
- [Mechanized Semantics](https://github.com/xavierleroy/cdf-mech-sem) - Coq 的配套资源是法兰西学院编程语言语义课程的资源。
- [Program Logics](https://github.com/xavierleroy/cdf-program-logics) - Companion Coq 为法兰西学院的程序逻辑课程提供了资源。
- [Program verification with types and logic](https://gitlab.science.ru.nl/program-verification/course-2023-2024) - 奈梅亨内梅亨大学使用 Coq 编写的编程语言语义、类型系统和程序逻辑课程的讲座和练习材料。
- [Proofs and Reliable Programming using Coq](https://team.inria.fr/stamp/proofs-and-reliable-programming-using-coq-2022/) - 介绍使用 Coq 开发和验证程序。

### 教程和提示

- [Coq'Art Exercises and Tutorials](https://github.com/coq-community/coq-art) - Coq'Art 书中的 Coq 代码和练习，包括附加教程。
- [Coq in a Hurry](http://cel.archives-ouvertes.fr/inria-00001173) - 介绍如何使用 Coq 定义逻辑概念和函数并对其进行推理。
- [Coq requirements in Common Criteria evaluations](https://inria.hal.science/hal-04452421) - 有关如何在高保证应用程序中编写可读且可审查的 Coq 代码的指南。
- [Coq Tactics in Plain English](https://charlesaverill.github.io/ctpe/) - Coq 策略指南，附有解释和示例。
- [Learn X in Y minutes where X=Coq](https://learnxinyminutes.com/docs/coq/) - Coq 作为一种语言的旋风之旅。
- [Lemma Overloading](https://github.com/coq-community/lemma-overloading) - 演示使用规范结构进行编程和证明的设计模式。
- [MathComp Tutorial Materials](https://github.com/math-comp/tutorial_material) - 数学组件教程的源代码。
- [Mike Nahas's Coq Tutorial](https://mdnahas.github.io/doc/nahas_tutorial.html) - 使用 Coq 编写形式证明的基础知识。
- [Tricks in Coq](https://github.com/coq-community/coq-tricks) - Coq 中难以发现的提示、技巧和功能。
