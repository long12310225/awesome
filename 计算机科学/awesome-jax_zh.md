<!--lint ignore double-link-->
# 很棒的 JAX[<img src="https://raw.githubusercontent.com/google/jax/master/images/jax_logo_250px.png" alt="JAX 徽标"align="right" height="100">](https://github.com/google/jax) [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

<!--lint ignore double-link-->
[JAX](https://github.com/google/jax) 通过类似 [NumPy](https://numpy.org/) 的 API 将自动微分和 [XLA 编译器](https://www.tensorflow.org/xla) 结合在一起，用于 GPU 和 TPU 等加速器上的高性能机器学习研究。
<!--lint enable double-link-->

这是很棒的 JAX 库、项目和其他资源的精选列表。欢迎贡献！

## 内容

- [Libraries](#libraries)
- [模型和项目](#models-and-projects)
- [Videos](#videos)
- [论文](#papers)https://github.com/jax-ml/jax
- [教程和博客文章](#tutorials-and-blog-posts)
- [Books](#books)
- [Community](#community)

<a name="libraries" />

## 图书馆

- 神经网络库
    - [Flax](https://github.com/google/flax) - 以灵活性和清晰度为中心。 <img src =“https://img.shields.io/github/stars/google/flax?style=social”align =“center”>
    - [Flax NNX](https://github.com/google/flax/tree/main/flax/nnx) - 由同一团队对 Flax 进行的演变 <img src="https://img.shields.io/github/stars/google/flax?style=social"align="center">
    - [Haiku](https://github.com/deepmind/dm-haiku) - 注重简单性，由 DeepMind 的 Sonnet 作者创建。 <img src =“https://img.shields.io/github/stars/deepmind/dm-haiku?style=social”align =“center”>
    - [Objax](https://github.com/google/objax) - 具有类似于 PyTorch 的面向对象设计。 <img src =“https://img.shields.io/github/stars/google/objax?style=social”align =“center”>
    - [Elegy](https://poets-ai.github.io/elegy/) - JAX 中深度学习的高级 API。支持 Flax、Haiku 和 Optax。 <img src =“https://img.shields.io/github/stars/poets-ai/elegy?style=social”align =“center”>
    - [Trax](https://github.com/google/trax) - “包含电池”深度学习库专注于为常见工作负载提供解决方案。 <img src =“https://img.shields.io/github/stars/google/trax?style=social”align =“center”>
    - [Jraph](https://github.com/deepmind/jraph) - 轻量级图神经网络库。 <img src =“https://img.shields.io/github/stars/deepmind/jraph?style=social”align =“center”>
    - [Neural Tangents](https://github.com/google/neural-tangents) - 用于指定有限和无限宽度神经网络的高级 API。 <img src =“https://img.shields.io/github/stars/google/neural-tangents?style=social”align =“center”>
    - [HuggingFace Transformers](https://github.com/huggingface/transformers) - 用于各种自然语言任务的预训练 Transformer 生态系统 (Flax)。 <img src =“https://img.shields.io/github/stars/huggingface/transformers?style=social”align =“center”>
    - [Equinox](https://github.com/patrick-kidger/equinox) - 可调用的 PyTree 和过滤的 JIT/grad 转换 => JAX 中的神经网络。 <img src =“https://img.shields.io/github/stars/patrick-kidger/equinox?style=social”align =“center”>
    - [Scenic](https://github.com/google-research/scenic) - 用于计算机视觉研究及其他领域的 Jax 库。  <img src =“https://img.shields.io/github/stars/google-research/scenic?style=social”align =“center”>
    - [Penzai](https://github.com/google-deepmind/penzai) - 使用可组合工具和简单的心理模型优先考虑神经网络模型的易读性、可视化和轻松编辑。  <img src =“https://img.shields.io/github/stars/google-deepmind/penzai?style=social”align =“center”>
- [Levanter](https://github.com/stanford-crfm/levanter) - 具有命名张量和 JAX 的清晰、可扩展、可重复的基础模型。  <img src =“https://img.shields.io/github/stars/stanford-crfm/levanter?style=social”align =“center”>
- [EasyLM](https://github.com/young-geng/EasyLM) - 法学硕士变得简单：在 JAX/Flax 中预训练、微调、评估和服务法学硕士。  <img src="https://img.shields.io/github/stars/young-geng/EasyLM?style=social"align="center">
- [NumPyro](https://github.com/pyro-ppl/numpyro) - 基于 Pyro 库的概率编程。 <img src =“https://img.shields.io/github/stars/pyro-ppl/numpyro?style=social”align =“center”>
- [Chex](https://github.com/deepmind/chex) - 用于编写和测试可靠的 JAX 代码的实用程序。 <img src =“https://img.shields.io/github/stars/deepmind/chex?style=social”align =“center”>
- [Optax](https://github.com/deepmind/optax) - 梯度处理和优化库。 <img src =“https://img.shields.io/github/stars/deepmind/optax?style=social”align =“center”>
- [RLax](https://github.com/deepmind/rlax) - 用于实施强化学习代理的库。 <img src =“https://img.shields.io/github/stars/deepmind/rlax?style=social”align =“center”>
- [JAX, M.D.](https://github.com/google/jax-md) - 加速、微分分子动力学。 <img src =“https://img.shields.io/github/stars/google/jax-md?style=social”align =“center”>
- [Coax](https://github.com/coax-dev/coax) - 将强化学习论文转化为代码，这是一种简单的方法。 <img src =“https://img.shields.io/github/stars/coax-dev/coax?style=social”align =“center”>
- [Distrax](https://github.com/deepmind/distrax) - TensorFlow Probability 的重新实现，包含概率分布和双射器。 <img src =“https://img.shields.io/github/stars/deepmind/distrax?style=social”align =“center”>
- [cvxpylayers](https://github.com/cvxgrp/cvxpylayers) - 构建可微凸优化层。 <img src="https://img.shields.io/github/stars/cvxgrp/cvxpylayers?style=social"align="center">
- [TensorLy](https://github.com/tensorly/tensorly) - 张量学习变得简单。 <img src =“https://img.shields.io/github/stars/tensorly/tensorly?style=social”align =“center”>
- [NetKet](https://github.com/netket/netket) - 量子物理学的机器学习工具箱。 <img src =“https://img.shields.io/github/stars/netket/netket?style=social”align =“center”>
- [Fortuna](https://github.com/awslabs/fortuna) - 用于深度学习中不确定性量化的 AWS 库。 <img src =“https://img.shields.io/github/stars/awslabs/fortuna?style=social”align =“center”>
- [BlackJAX](https://github.com/blackjax-devs/blackjax) - JAX 采样器库。 <img src =“https://img.shields.io/github/stars/blackjax-devs/blackjax?style=social”align =“center”>
- [Dynamax](https://github.com/probml/dynamax) - 概率状态空间模型。 <img src =“https://img.shields.io/github/stars/probml/dynamax?style=social”align =“center”>

<a name="new-libraries" />

### 新图书馆

本节包含制作精良且有用的库，但尚未经过大量用户群的实际测试。

- 神经网络库
    - [FedJAX](https://github.com/google/fedjax) - JAX 中的联邦学习，基于 Optax 和 Haiku 构建。 <img src =“https://img.shields.io/github/stars/google/fedjax?style=social”align =“center”>
    - [Equivariant MLP](https://github.com/mfinzi/equivariant-MLP) - 构建等变神经网络层。 <img src="https://img.shields.io/github/stars/mfinzi/equivariant-MLP?style=social"align="center">
    - [jax-resnet](https://github.com/n2cholas/jax-resnet/) - Flax 中 ResNet 变体的实现和检查点。 <img src =“https://img.shields.io/github/stars/n2cholas/jax-resnet?style=social”align =“center”>
    - [jax-raft](https://github.com/alebeck/jax-raft/) - RAFT 光流估计器的 JAX/Flax 端口。 <img src =“https://img.shields.io/github/stars/alebeck/jax-raft?style=social”align =“center”>
    - [Parallax](https://github.com/srush/parallax) - JAX 的不可变 Torch 模块。 <img src =“https://img.shields.io/github/stars/srush/parallax?style=social”align =“center”>
- 非线性优化
    - [Optimistix](https://github.com/patrick-kidger/optimistix) - 求根、最小化、不动点和最小二乘。 <img src =“https://img.shields.io/github/stars/patrick-kidger/optimistix?style=social”align =“center”>
    - [JAXopt](https://github.com/google/jaxopt) - JAX 中的硬件加速 (GPU/TPU)、可批处理和可微分优化器。 <img src =“https://img.shields.io/github/stars/google/jaxopt?style=social”align =“center”>
- [jax-unirep](https://github.com/ElArkk/jax-unirep) - 为蛋白质机器学习应用实现 [UniRep 模型](https://www.nature.com/articles/s41592-019-0598-1) 的库。 <img src =“https://img.shields.io/github/stars/ElArkk/jax-unirep?style=social”align =“center”>
- [flowjax](https://github.com/danielward27/flowjax) - 作为春分点模块构建的分布和标准化流量。 <img src =“https://img.shields.io/github/stars/danielward27/flowjax?style=social”align =“center”>
- [flaxdiff](https://github.com/AshishKumar4/FlaxDiff) - 用于在多节点多设备分布式设置 (TPU) 中构建和训练扩散模型的框架和库 <img src="https://img.shields.io/github/stars/AshishKumar4/FlaxDiff?style=social"align="center">
- [jax-flows](https://github.com/ChrisWaites/jax-flows) - 标准化 JAX 中的流。 <img src =“https://img.shields.io/github/stars/ChrisWaites/jax-flows?style=social”align =“center”>
- [sklearn-jax-kernels](https://github.com/ExpectationMax/sklearn-jax-kernels) - 使用 JAX 的“scikit-learn”内核矩阵。 <img src =“https://img.shields.io/github/stars/ExpectationMax/sklearn-jax-kernels?style=social”align =“center”>
- [jax-cosmo](https://github.com/DifferentiableUniverseInitiative/jax_cosmo) - 可微宇宙学库。 <img src="https://img.shields.io/github/stars/DifferentiableUniverseInitiative/jax_cosmo?style=social"align="center">
- [efax](https://github.com/NeilGirdhar/efax) - JAX 中的指数族。 <img src =“https://img.shields.io/github/stars/NeilGirdhar/efax?style=social”align =“center”>
- [mpi4jax](https://github.com/PhilipVinc/mpi4jax) - 将 MPI 操作与 CPU 和 GPU 上的 Jax 代码结合起来。 <img src="https://img.shields.io/github/stars/PhilipVinc/mpi4jax?style=social"align="center">
- [imax](https://github.com/4rtemi5/imax) - 图像增强和变换。 <img src =“https://img.shields.io/github/stars/4rtemi5/imax?style=social”align =“center”>
- [FlaxVision](https://github.com/rolandgvc/flaxvision) - TorchVision 的 Flax 版本。 <img src =“https://img.shields.io/github/stars/rolandgvc/flaxvision?style=social”align =“center”>
- [Oryx](https://github.com/tensorflow/probability/tree/master/spinoffs/oryx) - 基于程序转换的概率编程语言。
- [Optimal Transport Tools](https://github.com/google-research/ott) - 捆绑实用程序以解决最佳运输问题的工具箱。
- [delta PV](https://github.com/romanodev/deltapv) - 具有自动微分功能的光伏模拟器。 <img src =“https://img.shields.io/github/stars/romanodev/deltapv?style=social”align =“center”>
- [jaxlie](https://github.com/brentyi/jaxlie) - 用于刚体变换和优化的李理论库。 <img src =“https://img.shields.io/github/stars/brentyi/jaxlie?style=social”align =“center”>
- [BRAX](https://github.com/google/brax) - 用于模拟环境的可微分物理引擎以及用于针对这些环境训练代理的学习算法。 <img src =“https://img.shields.io/github/stars/google/brax?style=social”align =“center”>
- [flaxmodels](https://github.com/matthias-wright/flaxmodels) - Jax/Flax 的预训练模型。 <img src =“https://img.shields.io/github/stars/matthias-wright/flaxmodels?style=social”align =“center”>
- [CR.Sparse](https://github.com/carnotresearch/cr-sparse) - 用于稀疏表示和压缩感知的 XLA 加速算法。 <img src =“https://img.shields.io/github/stars/carnotresearch/cr-sparse?style=social”align =“center”>
- [exojax](https://github.com/HajimeKawahara/exojax) - 与 JAX 兼容的系外行星/棕矮星的自动可微分谱建模。 <img src="https://img.shields.io/github/stars/HajimeKawahara/exojax?style=social"align="center">
- [PIX](https://github.com/deepmind/dm_pix) - PIX是JAX中的图像处理库，用于JAX。 <img src =“https://img.shields.io/github/stars/deepmind/dm_pix?style=social”align =“center”>
- [bayex](https://github.com/alonfnt/bayex) - 由 JAX 提供支持的贝叶斯优化。 <img src =“https://img.shields.io/github/stars/alonfnt/bayex?style=social”align =“center”>
- [JaxDF](https://github.com/ucl-bug/jaxdf) - 具有任意离散化的可微模拟器框架。 <img src =“https://img.shields.io/github/stars/ucl-bug/jaxdf?style=social”align =“center”>
- [tree-math](https://github.com/google/tree-math) - 将对数组进行操作的函数转换为对 PyTree 进行操作的函数。 <img src =“https://img.shields.io/github/stars/google/tree-math?style=social”align =“center”>
- [jax-models](https://github.com/DarshanDeshpande/jax-models) - 最初没有代码或使用 JAX 以外的框架编写的代码的研究论文的实现。 <img src="https://img.shields.io/github/stars/DarshanDeshpande/jax-modelsa?style=social"align="center">
- [PGMax](https://github.com/vicariousinc/PGMax) - 用于构建离散概率图形模型 (PGM) 并通过 JAX 对它们运行推理的框架。 <img src =“https://img.shields.io/github/stars/vicariousinc/pgmax?style=social”align =“center”>
- [EvoJAX](https://github.com/google/evojax) - 硬件加速神经进化 <img src="https://img.shields.io/github/stars/google/evojax?style=social"align="center">
- [evosax](https://github.com/RobertTLange/evosax) - 基于 JAX 的进化策略 <img src="https://img.shields.io/github/stars/RobertTLange/evosax?style=social"align="center">
- [SymJAX](https://github.com/SymJAX/SymJAX) - 符号 CPU/GPU/TPU 编程。 <img src =“https://img.shields.io/github/stars/SymJAX/SymJAX？style=social”align =“center”>
- [mcx](https://github.com/rlouf/mcx) - 表达和编译概率程序以进行高性能推理。 <img src =“https://img.shields.io/github/stars/rlouf/mcx?style=social”align =“center”>
- [Einshape](https://github.com/deepmind/einshape) - 用于 JAX 和其他框架的基于 DSL 的重塑库。 <img src =“https://img.shields.io/github/stars/deepmind/einshape?style=social”align =“center”>
- [ALX](https://github.com/google-research/google-research/tree/master/alx) - 使用交替最小二乘进行分布式矩阵分解的开源库，更多信息请参见[_ALX：TPU 上的大规模矩阵分解_](https://arxiv.org/abs/2112.02194)。
- [Diffrax](https://github.com/patrick-kidger/diffrax) - JAX 中的数值微分方程求解器。 <img src =“https://img.shields.io/github/stars/patrick-kidger/diffrax?style=social”align =“center”>
- [tinygp](https://github.com/dfm/tinygp) - JAX 中最小的高斯过程库。 <img src="https://img.shields.io/github/stars/dfm/tinygp?style=social"align="center">
- [gymnax](https://github.com/RobertTLange/gymnax) - 具有著名的gym API 的强化学习环境。 <img src =“https://img.shields.io/github/stars/RobertTLange/gymnax?style=social”align =“center”>
- [Mctx](https://github.com/deepmind/mctx) - 本机 JAX 中的蒙特卡洛树搜索算法。 <img src =“https://img.shields.io/github/stars/deepmind/mctx?style=social”align =“center”>
- [KFAC-JAX](https://github.com/deepmind/kfac-jax) - 神经网络近似曲率的二阶优化。 <img src =“https://img.shields.io/github/stars/deepmind/kfac-jax?style=social”align =“center”>
- [TF2JAX](https://github.com/deepmind/tf2jax) - 将函数/图形转换为 JAX 函数。 <img src =“https://img.shields.io/github/stars/deepmind/tf2jax?style=social”align =“center”>
- [jwave](https://github.com/ucl-bug/jwave) - 用于可微分声学模拟的库 <img src="https://img.shields.io/github/stars/ucl-bug/jwave?style=social"align="center">
- [GPJax](https://github.com/thomaspinder/GPJax) - JAX 中的高斯过程。
- [Jumanji](https://github.com/instadeepai/jumanji) - 用 JAX 编写的一套行业驱动的硬件加速 RL 环境。 <img src =“https://img.shields.io/github/stars/instadeepai/jumanji?style=social”align =“center”>
- [Eqxvision](https://github.com/paganpasta/eqxvision) - Torchvision 的 Equinox 版本。 <img src="https://img.shields.io/github/stars/paganpasta/eqxvision?style=social"align="center">
- [JAXFit](https://github.com/dipolar-quantum-gases/jaxfit) - 用于非线性最小二乘问题的加速曲线拟合库（参见 [arXiv 论文](https://arxiv.org/abs/2208.12187)）。 <img src =“https://img.shields.io/github/stars/dipolar-quantum-gases/jaxfit?style=social”align =“center”>
- [econpizza](https://github.com/gboehl/econpizza) - 使用 JAX 求解具有异质主体的宏观经济模型。 <img src =“https://img.shields.io/github/stars/gboehl/econpizza?style=social”align =“center”>
- [SPU](https://github.com/secretflow/spu) - 特定于域的编译器和运行时套件，用于使用 MPC（安全多方计算）运行 JAX 代码。 <img src =“https://img.shields.io/github/stars/secretflow/spu?style=social”align =“center”>
- [jax-tqdm](https://github.com/jeremiecoullon/jax-tqdm) - 向 JAX 扫描和循环添加 tqdm 进度条。 <img src="https://img.shields.io/github/stars/jeremiecoullon/jax-tqdm?style=social"align="center">
- [safejax](https://github.com/alvarobartt/safejax) - 使用 🤗`safetensors` 序列化 JAX、Flax、Haiku 或 Objax 模型参数。 <img src =“https://img.shields.io/github/stars/alvarobartt/safejax?style=social”align =“center”>
- [Kernex](https://github.com/ASEM000/kernex) - JAX 中的可微分模板装饰器。 <img src =“https://img.shields.io/github/stars/ASEM000/kernex?style=social”align =“center”>
- [MaxText](https://github.com/google/maxtext) - 一个简单、高性能且可扩展的 Jax LLM，用纯 Python/Jax 编写，针对 Google Cloud TPU。 <img src =“https://img.shields.io/github/stars/google/maxtext?style=social”align =“center”>
- [Pax](https://github.com/google/paxml) - 用于训练大型模型的基于 Jax 的机器学习框架。 <img src =“https://img.shields.io/github/stars/google/paxml?style=social”align =“center”>
- [Praxis](https://github.com/google/praxis) - Pax 的层库，目标是可供其他基于 JAX 的 ML 项目使用。 <img src =“https://img.shields.io/github/stars/google/praxis?style=social”align =“center”>
- [purejaxrl](https://github.com/luchris429/purejaxrl) - JAX 中的可矢量化端到端 RL 算法。 <img src="https://img.shields.io/github/stars/luchris429/purejaxrl?style=social"align="center">
- [Lorax](https://github.com/davisyoshida/lorax) - 自动将 LoRA 应用于 JAX 模型（Flax、Haiku 等）
- [SCICO](https://github.com/lanl/scico) - JAX 中的科学计算成像。 <img src =“https://img.shields.io/github/stars/lanl/scico?style=social”align =“center”>
- [Spyx](https://github.com/kmheckel/spyx) - JAX 中的尖峰神经网络用于神经形态硬件上的机器学习。 <img src =“https://img.shields.io/github/stars/kmheckel/spyx?style=social”align =“center”>
- 大脑动力学编程生态系统
    - [BrainPy](https://github.com/brainpy/BrainPy) - Python 中的大脑动力学编程。 <img src =“https://img.shields.io/github/stars/brainpy/BrainPy?style=social”align =“center”>
    - [brainunit](https://github.com/chaobrain/brainunit) - JAX 中的物理单位和单位感知数学系统。 <img src =“https://img.shields.io/github/stars/chaobrain/brainunit?style=social”align =“center”>
    - [dendritex](https://github.com/chaobrain/dendritex) - JAX 中的树突建模。 <img src =“https://img.shields.io/github/stars/chaobrain/dendritex?style=social”align =“center”>
    - [brainstate](https://github.com/chaobrain/brainstate) - 用于程序编译和增强的基于状态的转换系统。 <img src =“https://img.shields.io/github/stars/chaobrain/brainstate?style=social”align =“center”>
    - [braintaichi](https://github.com/chaobrain/braintaichi) - 利用太极郎定制大脑动力学算子。 <img src =“https://img.shields.io/github/stars/chaobrain/braintaichi?style=social”align =“center”>
- [OTT-JAX](https://github.com/ott-jax/ott) - JAX 中的最佳运输工具。 <img src =“https://img.shields.io/github/stars/ott-jax/ott?style=social”align =“center”>
- [QDax](https://github.com/adaptive-intelligent-robotics/QDax) - Jax 中的质量多样性优化。 <img src =“https://img.shields.io/github/stars/adaptive-intelligent-robotics/QDax?style=social”align =“center”>
- [JAX Toolbox](https://github.com/NVIDIA/JAX-Toolbox) - 使用 T5x、Paxml 和 Transformer Engine 等库的 NVIDIA GPU 上的夜间 CI 和 JAX 优化示例。 <img src="https://img.shields.io/github/stars/NVIDIA/JAX-Toolbox?style=social"align="center">
- [Pgx](http://github.com/sotetsuk/pgx) - 强化学习的矢量化棋盘游戏环境以及 AlphaZero 示例。 <img src =“https://img.shields.io/github/stars/sotetsuk/pgx?style=social”align =“center”>
- [EasyDeL](https://github.com/erfanzar/EasyDeL) - EasyDeL 🔮 是一个开源库，可让您的训练更快、更优化，在 JAX 中提供很酷的训练和服务选项（Llama、MPT、Mixtral、Falcon 等）<img src="https://img.shields.io/github/stars/erfanzar/EasyDeL?style=social"align="center">
- [XLB](https://github.com/Autodesk/XLB) - Python 中用于基于物理的机器学习的可微分大规模并行格子玻尔兹曼库。 <img src =“https://img.shields.io/github/stars/Autodesk/XLB?style=social”align =“center”>
- [dynamiqs](https://github.com/dynamiqs/dynamiqs) - 使用 JAX 对量子系统进行高性能和可微分模拟。 <img src="https://img.shields.io/github/stars/dynamiqs/dynamiqs?style=social"align="center">
- [foragax](https://github.com/i-m-iron-man/Foragax) - JAX 中基于代理的建模框架。  <img src =“https://img.shields.io/github/stars/i-m-iron-man/Foragax?style=social”align =“center”>
- [tmmax](https://github.com/bahremsd/tmmax) - 使用 JAX 对薄膜结构中的光学特性进行矢量化计算。用于薄膜光学研究的瑞士军刀工具<img src =“https://img.shields.io/github/stars/bahremsd/tmmax”align =“center”>
- [Coreax](https://github.com/gchq/coreax) - 用于查找核心集以压缩大型数据集同时保留其统计属性的算法。 <img src =“https://img.shields.io/github/stars/gchq/coreax?style=social”align =“center”>
- [NAVIX](https://github.com/epignatelli/navix) - 在 JAX 中重新实现强化学习环境 MiniGrid <img src="https://img.shields.io/github/stars/epignatelli/navix?style=social"align="center">
- [FDTDX](https://github.com/ymahlau/fdtdx) - JAX 中的有限差分时域电磁仿真 <img src="https://img.shields.io/github/stars/ymahlau/fdtdx?style=social"align="center">
- [DiffeRT](https://github.com/jeertmans/DiffeRT) - 由 JAX 生态系统提供支持的用于无线电传播的可微光线追踪工具箱。 <img src="https://img.shields.io/github/stars/jeertmans/DiffeRT?style=social"align="center">
- [JAX-in-Cell](https://github.com/uwplasma/JAX-in-Cell) - 使用 PIC（粒子在细胞）方法自洽求解电磁场中的电子和离子动力学的等离子体物理模拟<img src="https://img.shields.io/github/stars/uwplasma/JAX-in-Cell?style=social"align="center">
- [kvax](https://github.com/nebius/kvax) - JAX 的 FlashAttention 实现，支持高效的文档掩码计算和上下文并行性。 <img src =“https://img.shields.io/github/stars/nebius/kvax?style=social”align =“center”>
- [astronomix](https://github.com/leo1200/astronomix) - JAX 中天体物理学的可微（磁）流体动力学 <img src="https://img.shields.io/github/stars/leo1200/astronomix?style=social"align="center">
- [vivsim](https://github.com/haimingz/vivsim) - 使用浸入边界格子玻尔兹曼方法进行流固耦合模拟。 <img src =“https://img.shields.io/github/stars/haimingz/vivsim?style=social”align =“center”>
- [MBIRJAX](https://github.com/cabouman/mbirjax) - 高性能断层扫描重建。 <img src =“https://img.shields.io/github/stars/cabouman/mbirjax？style-social”align =“center”>
- [torchax](https://github.com/google/torchax/) - torchax 是 Jax 的一个库，用于与 PyTorch 编写的模型代码进行互操作。<img src="https://img.shields.io/github/stars/google/torchax?style=social"align="center">

<a name="models-and-projects" />

## 模型和项目

### 贾克斯

- [Fourier Feature Networks](https://github.com/tancik/fourier-feature-networks) - [_傅立叶特征让网络学习低维域中的高频函数_](https://people.eecs.berkeley.edu/~bmild/fourfeat) 的正式实施。
- [kalman-jax](https://github.com/AaltoML/kalman-jax) - 使用迭代卡尔曼滤波和平滑对马尔可夫（即时间）高斯过程进行近似推理。
- [jaxns](https://github.com/Joshuaalbert/jaxns) - JAX 中的嵌套采样。
- [Amortized Bayesian Optimization](https://github.com/google-research/google-research/tree/master/amortized_bo) - 与[_离散空间上的摊销贝叶斯优化_](http://www.auai.org/uai2020/proceedings/329_main_paper.pdf)相关的代码。
- [Accurate Quantized Training](https://github.com/google-research/google-research/tree/master/aqt) - 用于在 JAX 和 Flax 中运行和分析神经网络量化实验的工具和库。
- [BNN-HMC](https://github.com/google-research/google-research/tree/master/bnn_hmc) - 论文的实现 [_贝叶斯神经网络后验到底是什么样的？_](https://arxiv.org/abs/2104.14421)。
- [JAX-DFT](https://github.com/google-research/google-research/tree/master/jax_dft) - JAX 中的一维密度泛函理论 (DFT)，并实施 [_Kohn-Sham 方程作为正则化器：将先验知识构建到机器学习物理学中_](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.126.036401)。
- [Robust Loss](https://github.com/google-research/google-research/tree/master/robust_loss_jax) - 论文参考代码[_A General and Adaptive Robust Loss Function_](https://arxiv.org/abs/1701.03077)。
- [Symbolic Functionals](https://github.com/google-research/google-research/tree/master/symbolic_functionals) - 来自[_演化符号密度泛函_](https://arxiv.org/abs/2203.02540)的演示。
- [TriMap](https://github.com/google-research/google-research/tree/master/trimap) - [_TriMap：使用 Triplets 进行大规模降维_](https://arxiv.org/abs/1910.00204) 的官方 JAX 实现。

### 亚麻

- [awesome-jax-flax-llms](https://github.com/your-username/awesome-jax-flax-llms) - 在 **JAX** 和 **Flax** 中实现的法学硕士集合
- [DeepSeek-R1-Flax-1.5B-Distill](https://github.com/J-Rosser-UK/Torch2Jax-DeepSeek-R1-Distill-Qwen-1.5B) - DeepSeek-R1 1.5B 蒸馏推理 LLM 的 Flax 实现。
- [Performer](https://github.com/google-research/google-research/tree/master/performer/fast_attention/jax) - Performer（通过 FAVOR+ 的线性变压器）架构的 Flax 实现。
- [JaxNeRF](https://github.com/google-research/google-research/tree/master/jaxnerf) - 实现[_NeRF：将场景表示为用于视图合成的神经辐射场_](http://www.matthewtancik.com/nerf)，并支持多设备 GPU/TPU。
- [mip-NeRF](https://github.com/google/mipnerf) - [_Mip-NeRF：抗锯齿神经辐射场的多尺度表示_](https://jonbarron.info/mipnerf) 的正式实现。
- [RegNeRF](https://github.com/google-research/google-research/tree/master/regnerf) - [_RegNeRF：正则化神经辐射场以从稀疏输入进行视图合成_](https://m-niemeyer.github.io/regnerf/) 的正式实现。
- [JaxNeuS](https://github.com/huangjuite/jaxneus) - [_NeuS：通过体渲染学习神经隐式曲面进行多视图重建_](https://lingjie0206.github.io/papers/NeuS/)的实现
- [Big Transfer (BiT)](https://github.com/google-research/big_transfer) - [_大迁移（BiT）：通用视觉表示学习_]（https://arxiv.org/abs/1912.11370）的实现。
- [JAX RL](https://github.com/ikostrikov/jax-rl) - 强化学习算法的实现。
- [gMLP](https://github.com/SauravMaheshkar/gMLP) - [_关注 MLP_](https://arxiv.org/abs/2105.08050) 的实施。
- [MLP Mixer](https://github.com/SauravMaheshkar/MLP-Mixer) - [_MLP-Mixer：视觉的全 MLP 架构_](https://arxiv.org/abs/2105.01601) 的最小实现。
- [Distributed Shampoo](https://github.com/google-research/google-research/tree/master/scalable_shampoo) - 实施[_二阶优化变得实用_](https://arxiv.org/abs/2002.09018)。
- [NesT](https://github.com/google-research/nested-transformer) - [_聚合嵌套变压器_](https://arxiv.org/abs/2105.12723)的正式实现。
- [XMC-GAN](https://github.com/google-research/xmcgan_image_generation) - [_文本到图像生成的跨模态对比学习_](https://arxiv.org/abs/2101.04702)的正式实施。
- [FNet](https://github.com/google-research/google-research/tree/master/f_net) - [_FNet：混合令牌与傅里叶变换_](https://arxiv.org/abs/2105.03824)的正式实现。
- [GFSA](https://github.com/google-research/google-research/tree/master/gfsa) - [_使用有限状态自动机层学习图结构_](https://arxiv.org/abs/2007.04929) 的正式实现。
- [IPA-GNN](https://github.com/google-research/google-research/tree/master/ipagnn) - [_学习使用指令指针注意力图神经网络执行程序_](https://arxiv.org/abs/2010.12621)的正式实现。
- [Flax Models](https://github.com/google-research/google-research/tree/master/flax_models) - 在 Flax 中实现的模型和方法的集合。
- [Protein LM](https://github.com/google-research/google-research/tree/master/protein_lm) - 实现蛋白质的 BERT 和自回归模型，如 [_Biological Structure and Function Emerge from Scaling Unsupervised Learning to 2.50 Million Protein Sequences_](https://www.biorxiv.org/content/10.1101/622803v1.full) 和 [_ProGen：蛋白质语言建模一代_](https://www.biorxiv.org/content/10.1101/2020.03.07.982272v2)。
- [Slot Attention](https://github.com/google-research/google-research/tree/master/ptopk_patch_selection) - [_图像识别的可微分片选择_](https://arxiv.org/abs/2104.03059)的参考实现。
- [Vision Transformer](https://github.com/google-research/vision_transformer) - [_一张图像值得 16x16 个单词：用于大规模图像识别的 Transformers_](https://arxiv.org/abs/2010.11929) 的正式实现。
- [FID computation](https://github.com/matthias-wright/jax-fid) - [mseitzer/pytorch-fid](https://github.com/mseitzer/pytorch-fid) 到 Flax 的端口。
- [ARDM](https://github.com/google-research/google-research/tree/master/autoregressive_diffusion) - [_自回归扩散模型_](https://arxiv.org/abs/2110.02037)的正式实施。
- [D3PM](https://github.com/google-research/google-research/tree/master/d3pm) - [_离散状态空间中的结构化去噪扩散模型_](https://arxiv.org/abs/2107.03006) 的正式实现。
- [Gumbel-max Causal Mechanisms](https://github.com/google-research/google-research/tree/master/gumbel_max_causal_gadgets) - [_学习广义 Gumbel-max 因果机制_](https://arxiv.org/abs/2111.06888) 的代码，[GuyLor/gumbel_max_causal_gadgets_part2](https://github.com/GuyLor/gumbel_max_causal_gadgets_part2) 中有额外代码。
- [Latent Programmer](https://github.com/google-research/google-research/tree/master/latent_programmer) - ICML 2021 论文的代码 [_Latent Programmer: Discrete Latent Codes for Program Synthesis_](https://arxiv.org/abs/2012.00377)。
- [SNeRG](https://github.com/google-research/google-research/tree/master/snerg) - [_烘焙神经辐射场以进行实时视图合成_](https://phog.github.io/snerg) 的正式实现。
- [Spin-weighted Spherical CNNs](https://github.com/google-research/google-research/tree/master/spin_spherical_cnns) - [_自旋加权球形 CNN_](https://arxiv.org/abs/2006.10731) 的改编。
- [VDVAE](https://github.com/google-research/google-research/tree/master/vdvae_flax) - [_非常深的 VAE 推广自回归模型并在图像上优于它们_](https://arxiv.org/abs/2011.10650)，原始代码位于 [openai/vdvae](https://github.com/openai/vdvae)。
- [MUSIQ](https://github.com/google-research/google-research/tree/master/musiq) - ICCV 2021论文的检查点和模型推理代码[_MUSIQ: Multi-scale Image Quality Transformer_](https://arxiv.org/abs/2108.05997)
- [AQuaDem](https://github.com/google-research/google-research/tree/master/aquadem) - [_通过演示进行动作量化的连续控制_](https://arxiv.org/abs/2110.10149) 的正式实施。
- [Combiner](https://github.com/google-research/google-research/tree/master/combiner) - [_Combiner：具有稀疏计算成本的全注意力变压器_](https://arxiv.org/abs/2107.05768)的正式实现。
- [Dreamfields](https://github.com/google-research/google-research/tree/master/dreamfields) - ICLR 2022 论文 [_Progressive Distillation for Fast Sampling of Diffusion Models_](https://ajayj.com/dreamfields) 的正式实现。
- [GIFT](https://github.com/google-research/google-research/tree/master/gift) - [_野外渐进域适应：当中间分布不存在时_](https://arxiv.org/abs/2106.06080)的正式实施。
- [Light Field Neural Rendering](https://github.com/google-research/google-research/tree/master/light_field_neural_rendering) - [_光场神经渲染_](https://arxiv.org/abs/2112.09687)的正式实现。
- [Sharpened Cosine Similarity in JAX by Raphael Pisoni](https://colab.research.google.com/drive/1KUKFEMneQMS3OzPYnWZGkEnry3PdzCfn?usp=sharing) - 锐化余弦相似度层的 JAX/Flax 实现。
- [GNNs for Solving Combinatorial Optimization Problems](https://github.com/IvanIsCoding/GNN-for-Combinatorial-Optimization) - [物理启发图神经网络的组合优化](https://arxiv.org/abs/2107.01188) 的 JAX + Flax 实现。
- [DETR](https://github.com/MasterSkepticista/detr) - 使用 Sinkhorn 求解器和并行二分匹配来实现 [_DETR：使用 Transformers 进行端到端对象检测_](https://github.com/facebookresearch/detr)。

### 俳句

- [AlphaFold](https://github.com/deepmind/alphafold) - AlphaFold v2.0 推理流程的实现，在 [_使用 AlphaFold 进行高精度蛋白质结构预测_](https://www.nature.com/articles/s41586-021-03819-2) 中介绍。
- [Adversarial Robustness](https://github.com/deepmind/deepmind-research/tree/master/adversarial_robustness) - [_Uncovering the Limits of Adversarial Training against Norm-Bounded Adversarial Examples_](https://arxiv.org/abs/2010.03593) 和 [_Fishing Data Augmentation to Improve Adversarial Robustness_](https://arxiv.org/abs/2103.01946) 的参考代码。
- [Bootstrap Your Own Latent](https://github.com/deepmind/deepmind-research/tree/master/byol) - 论文的实现 [_Bootstrap your own Latent: A new method to self-supervised Learning_](https://arxiv.org/abs/2006.07733)。
- [Gated Linear Networks](https://github.com/deepmind/deepmind-research/tree/master/gated_linear_networks) - GLN 是一类无反向传播的神经网络。
- [Glassy Dynamics](https://github.com/deepmind/deepmind-research/tree/master/glassy_dynamics) - 该论文的开源实现[_揭开玻璃系统中静态结构的预测能力_](https://www.nature.com/articles/s41567-020-0842-8)。
- [MMV](https://github.com/deepmind/deepmind-research/tree/master/mmv) - [_自监督多模式多功能网络_](https://arxiv.org/abs/2006.16228)中的模型代码。
- [Normalizer-Free Networks](https://github.com/deepmind/deepmind-research/tree/master/nfnets) - [_NFNets_](https://arxiv.org/abs/2102.06171) 的官方俳句实现。
- [NuX](https://github.com/Information-Fusion-Lab-Umass/NuX) - 使用 JAX 标准化流程。
- [OGB-LSC](https://github.com/deepmind/deepmind-research/tree/master/ogb_lsc) - 该存储库包含 DeepMind 对 [PCQM4M-LSC](https://ogb.stanford.edu/kddcup2021/pcqm4m/)（量子化学）和 [MAG240M-LSC](https://ogb.stanford.edu/kddcup2021/mag240m/)（学术图）的条目
[OGB 大规模挑战赛](https://ogb.stanford.edu/kddcup2021/) (OGB-LSC) 的曲目。
- [Persistent Evolution Strategies](https://github.com/google-research/google-research/tree/master/persistent_es) - 用于论文 [_使用持久进化策略的展开计算图中的无偏梯度估计_](http://proceedings.mlr.press/v139/vicol21a.html) 的代码。
- [Two Player Auction Learning](https://github.com/degregat/two-player-auctions) - 论文 [_拍卖学习作为两人游戏_](https://arxiv.org/abs/2006.05684) 的 JAX 实现。
- [WikiGraphs](https://github.com/deepmind/deepmind-research/tree/master/wikigraphs) - 用于重现 [_WikiGraphs：维基百科文本 - 知识图配对数据集_](https://aclanthology.org/2021.textgraphs-1.7) 中的结果的基线代码。

### 特拉克斯

- [Reformer](https://github.com/google/trax/tree/master/trax/models/reformer) - 实施 Reformer（高效变压器）架构。

### 数字火力

- [lqg](https://github.com/RothkopfLab/lqg) - 线性二次高斯问题的贝叶斯逆最优控制的正式实现来自论文 [_通过连续心理物理学的逆最优控制将感知付诸行动_](https://elifesciences.org/articles/76635)


### 春分

- [Sampling Path Candidates with Machine Learning](https://differt.eertmans.be/icmlcn2025/notebooks/sampling_paths.html) - 官方教程和实现来自论文 [_Towards Generative Ray Path Sampling for Faster Point-to-Point Ray Tracing_](https://arxiv.org/abs/2410.23773)。

<a name="videos" />

## 视频

- [NeurIPS 2020: JAX Ecosystem Meetup](https://www.youtube.com/watch?v=iDxJxIyzSiM) - JAX、它在 DeepMind 的使用，以及工程师、科学家和 JAX 核心团队之间的讨论。
- [Introduction to JAX](https://youtu.be/0mVmRHMaOJ4) - 在 JAX 中从头开始简单的神经网络。
- [JAX: Accelerated Machine Learning Research | SciPy 2020 | VanderPlas](https://youtu.be/z-WSrQDXkuM) - JAX 的核心设计、它如何推动新研究以及如何开始使用它。
- [Bayesian Programming with JAX + NumPyro — Andy Kitchen](https://youtu.be/CecuWGpoztw) - 使用 NumPyro 进行贝叶斯建模简介。
- [JAX: Accelerated machine-learning research via composable function transformations in Python | NeurIPS 2019 | Skye Wanderman-Milne](https://slideslive.com/38923687/jax-accelerated-machinelearning-research-via-composable-function-transformations-in-python) - [_机器学习的程序转换_](https://program-transformations.github.io) 研讨会上的 JAX 介绍演示。
- [JAX on Cloud TPUs | NeurIPS 2020 | Skye Wanderman-Milne and James Bradbury](https://drive.google.com/file/d/1jKxefZT1xJDUxMman6qrQVed7vWI0MIn/edit) - 通过演示演示 TPU 主机访问。
- [Deep Implicit Layers - Neural ODEs, Deep Equilibirum Models, and Beyond | NeurIPS 2020](https://slideslive.com/38935810/deep-implicit-layers-neural-odes-equilibrium-models-and-beyond) - 教程由 Zico Kolter、David Duvenaud 和 Matt Johnson 创建，Colab 笔记本可在 [_Deep Implicit Layers_](http://implicit-layers-tutorial.org) 中找到。
- [Solving y=mx+b with Jax on a TPU Pod slice - Mat Kelcey](http://matpalm.com/blog/ymxb_pod_slice/) - 包含 Colab 笔记本的四部分 YouTube 教程系列，从 Jax 基础知识开始，逐步过渡到在 v3-32 TPU Pod 切片上使用数据并行方法进行训练。
- [JAX, Flax & Transformers 🤗](https://github.com/huggingface/transformers/blob/9160d81c98854df44b1d543ce5d65a6aa28444a2/examples/research_projects/jax-projects/README.md#talks) - 为期 3 天的演讲围绕 JAX / Flax、Transformers、大规模语言建模和其他重要主题。

<a name="papers" />

## 论文

本节包含专注于 JAX 的论文（例如基于 JAX 的库白皮书、JAX 研究等）。在 JAX 中实现的论文列在 [模型/项目](#projects) 部分中。

<!--lint disable-->
- [__Compiling machine learning programs via high-level tracing__. Roy Frostig, Matthew James Johnson, Chris Leary. _MLSys 2018_.](https://mlsys.org/Conferences/doc/2018/146.pdf) - 白皮书描述了 JAX 的早期版本，详细说明了如何跟踪和编译计算。
- [__JAX, M.D.: A Framework for Differentiable Physics__. Samuel S. Schoenholz, Ekin D. Cubuk. _NeurIPS 2020_.](https://arxiv.org/abs/1912.04232) - 介绍 JAX, M.D.，这是一个可微分物理库，其中包括模拟环境、交互势、神经网络等。
- [__Enabling Fast Differentially Private SGD via Just-in-Time Compilation and Vectorization__. Pranav Subramani, Nicholas Vadivelu, Gautam Kamath. _arXiv 2020_.](https://arxiv.org/abs/2010.09063) - 使用 JAX 的 JIT 和 VMAP 实现比现有库更快的差分私有。
- [__XLB: A Differentiable Massively Parallel Lattice Boltzmann Library in Python__. Mohammadmehdi Ataei, Hesam Salehipour. _arXiv 2023_.](https://arxiv.org/abs/2311.16080) - 描述 XLB 库的白皮书：基准、验证以及有关该库的更多详细信息。
<!--lint enable-->


<a name="tutorials-and-blog-posts" />

## 教程和博客文章

- [Using JAX to accelerate our research by David Budden and Matteo Hessel](https://deepmind.com/blog/article/using-jax-to-accelerate-our-research) - 描述 DeepMind 的 JAX 和 JAX 生态系统的状态。
- [Getting started with JAX (MLPs, CNNs & RNNs) by Robert Lange](https://roberttlange.github.io/posts/2020/03/blog-post-10/) - 使用基本 JAX 运算符从头开始构建神经网络块。
- [Learn JAX: From Linear Regression to Neural Networks by Rito Ghosh](https://www.kaggle.com/code/truthr/jax-0) - 简要介绍 JAX 并使用它来实现线性和逻辑回归以及神经网络模型并使用它们来解决现实世界的问题。
- [Tutorial: image classification with JAX and Flax Linen by 8bitmp3](https://github.com/8bitmp3/JAX-Flax-Tutorial-Image-Classification-with-Linen) - 了解如何使用 Flax 的 Linen API 创建简单的卷积网络并训练它识别手写数字。
- [Plugging Into JAX by Nick Doiron](https://medium.com/swlh/plugging-into-jax-16c120ec3302) - 在 Kaggle 花卉分类挑战中比较 Flax、Haiku 和 Objax。
- [Meta-Learning in 50 Lines of JAX by Eric Jang](https://blog.evjang.com/2019/02/maml-jax.html) - JAX 和元学习简介。
- [Normalizing Flows in 100 Lines of JAX by Eric Jang](https://blog.evjang.com/2019/07/nf-jax.html) - [RealNVP](https://arxiv.org/abs/1605.08803)的简洁实现。
- [Differentiable Path Tracing on the GPU/TPU by Eric Jang](https://blog.evjang.com/2019/11/jaxpt.html) - 实现路径跟踪的教程。
- [Ensemble networks by Mat Kelcey](http://matpalm.com/blog/ensemble_nets) - 集成网络是一种将模型集成表示为单个逻辑模型的方法。
- [Out of distribution (OOD) detection by Mat Kelcey](http://matpalm.com/blog/ood_using_focal_loss) - 实现 OOD 检测的不同方法。
- [Understanding Autodiff with JAX by Srihari Radhakrishna](https://www.radx.in/jax.html) - 了解自动差异如何使用 JAX 工作。
- [From PyTorch to JAX: towards neural net frameworks that purify stateful code by Sabrina J. Mielke](https://sjmielke.com/jax-purify.htm) - 展示如何从类似 PyTorch 的编码风格转变为更函数式的编码风格。
- [Extending JAX with custom C++ and CUDA code by Dan Foreman-Mackey](https://github.com/dfm/extending-jax) - 教程演示了在 JAX 中提供自定义操作所需的基础设施。
- [Evolving Neural Networks in JAX by Robert Tjarko Lange](https://roberttlange.github.io/posts/2021/02/cma-es-jax/) - 探索 JAX 如何为下一代可扩展神经进化算法提供支持。
- [Exploring hyperparameter meta-loss landscapes with JAX by Luke Metz](http://lukemetz.com/exploring-hyperparameter-meta-loss-landscapes-with-jax/) - 演示如何使用 JAX 通过 SGD 和 Momentum 执行内部损失优化、使用梯度的外部损失优化以及使用进化策略的外部损失优化。
- [Deterministic ADVI in JAX by Martin Ingram](https://martiningram.github.io/deterministic-advi/) - 演练如何使用 JAX 轻松、干净地实现自动微分变分推理 (ADVI)。
- [Evolved channel selection by Mat Kelcey](http://matpalm.com/blog/evolved_channel_selection/) - 训练对不同分辨率下的输入通道的不同组合具有鲁棒性的分类模型，然后使用遗传算法来确定特定损失的最佳组合。
- [Introduction to JAX by Kevin Murphy](https://colab.research.google.com/github/probml/probml-notebooks/blob/main/notebooks/jax_intro.ipynb) - Colab 介绍了该语言的各个方面并将其应用于简单的 ML 问题。
- [Writing an MCMC sampler in JAX by Jeremie Coullon](https://www.jeremiecoullon.com/2020/11/10/mcmcjax3ways/) - 有关在 JAX 中编写 MCMC 采样器的不同方法以及速度基准的教程。
- [How to add a progress bar to JAX scans and loops by Jeremie Coullon](https://www.jeremiecoullon.com/2021/01/29/jax_progress_bar/) - 有关如何使用“host_callback”模块向 JAX 中已编译循环添加进度条的教程。
- [Get started with JAX by Aleksa Gordić](https://github.com/gordicaleksa/get-started-with-JAX) - 从零 JAX 知识到用俳句构建神经网络的一系列笔记本和视频。
- [Writing a Training Loop in JAX + FLAX by Saurav Maheshkar and Soumik Rakshit](https://wandb.ai/jax-series/simple-training-loop/reports/Writing-a-Training-Loop-in-JAX-FLAX--VmlldzoyMzA4ODEy) - 有关使用 JAX、Flax 和 Optax 编写简单的端到端训练和评估管道的教程。
- [Implementing NeRF in JAX by Soumik Rakshit and Saurav Maheshkar](https://wandb.ai/wandb/nerf-jax/reports/Implementing-NeRF-in-JAX--VmlldzoxODA2NDk2?galleryTag=jax) - 有关 JAX 中神经辐射场表示的场景 3D 体积渲染的教程。
- [Deep Learning tutorials with JAX+Flax by Phillip Lippe](https://uvadlc-notebooks.readthedocs.io/en/latest/tutorial_notebooks/JAX/tutorial2/Introduction_to_JAX.html) - 一系列笔记本解释了各种深度学习概念，从基础知识（例如 JAX/Flax 简介、激活函数）到最新进展（例如 Vision Transformers、SimCLR），并翻译为 PyTorch。
- [Achieving 4000x Speedups with PureJaxRL](https://chrislu.page/blog/meta-disco/) - 关于 JAX 如何通过矢量化大幅加速 RL 训练的博客文章。
- [Simple PDE solver + Constrained Optimization with JAX by Philip Mocz](https://levelup.gitconnected.com/create-your-own-automatically-differentiable-simulation-with-python-jax-46951e120fbb?sk=e8b9213dd2c6a5895926b2695d28e4aa) - 使用 JAX 求解平流扩散方程并将其用于约束优化问题以找到产生所需结果的初始条件的简单示例。

<a name="books" />

## 书籍

- [Jax in Action](https://www.manning.com/books/jax-in-action) - 使用 JAX 进行深度学习和其他数学密集型应用程序的实践指南。

<a name="community" />

## 社区

- [JaxLLM（非官方）Discord](https://discord.com/channels/1107832795377713302/1107832795688083561)
- [JAX GitHub 讨论](https://github.com/google/jax/discussions)
- [Reddit](https://www.reddit.com/r/JAX/)

## 贡献

欢迎投稿！首先阅读[贡献指南](contributing.md)。
