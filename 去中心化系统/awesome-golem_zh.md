# 很棒的傀儡 [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[<img src=“golem-logo.svg”align=“right”width=“150”>](https://golem.network/)

> 欢迎来到 **Awesome Golem**，这是社区策划的 Golem 资源、链接、项目、工具和应用程序列表！

Golem 的用户以 Rust 实现 Yagna 的形式运行参考实现。用户共同组成了 Golem 网络，这是一个计算资源的 P2P 市场，个人可以充当两个非排他性角色之一：提供者出售闲置资源，或者请求者购买资源来运行任务。

## 内容

- [Golem](#golem)
- [网络统计](#network-statistics)
- [魔像项目](#Golem-Projects)
  - [GPU提供商](#GPU-Provider)
  - [雷对傀儡](#Ray-on-Golem)
  - [golem-js - Golem 的 JS SDK](#golem-js---the-JS-SDK-from-Golem)
  - [Golem 上的 Jupyter](#Jupyter-on-Golem)
  - [在 Golem 上渲染](#Rendering-on-Golem)
  - [信誉系统](#Reputation-System)
- [Ecosystem](#Ecosystem)
- [区块链自动化（又名 Emeth.xyz）]（#Blockchain-automations-（又名-Emeth.xyz））
- [开发者和请求者资源](#developer-and-requestor-resources)
- [提供商资源](#provider-resources)
  - [Monitoring](#monitoring)
  - [Provisioning](#provisioning)
- [学习资源](#learning-resources)
  - [演示和研讨会材料](#presentations-and-workshop-material)
  - [揭开 Golem 的下一个里程碑博客系列的面纱](#unraveling-golems-the-next-milestone-blog-series)
  - [GitHub 摘要博客系列](#github-digest-blog-series)
- [Archive](#Archive)
  - [Apps](#apps)


## 魔像

- [Golem Network Platform](https://www.golem.network/platform) - 在 Golem Network 官方网站上了解 Golem 平台。
- [Golem Network Discord](https://chat.golem.network/) - 加入 Discord 上的 Golem Network 社区并直接与团队聊天。
- [Reddit](https://reddit.com/r/GolemProject) - Reddit 平台上的 Golem Network 讨论。
- [Twitter](https://twitter.com/golemproject) - Golem 项目推特。
- [Blog](http://blog.golemproject.net/) - 官方博客，您可以在其中找到有关公告、摘要和更新的最可靠信息。

## 网络统计

- [Golem Network Stats](https://stats.golem.network) - Golem 网络中的统计跟踪任务和提供者资源利用率。
- [Golem Stats backend](https://github.com/cryptobench/golem-stats-backend) - Golem 网络统计页面的后端，包括 API 端点 URL。
- [Stats API Documentation](https://docs.stats.golem.network/) - Golem 网络统计页面用于显示其数据的 API 端点。

## 魔像项目

### GPU提供商

我们希望扩展 Golem 网络针对 GPU 工作负载的功能。项目状态可在我们的 [Discord](https://chat.golem.network/) 上专用 GPU 提供商频道的固定消息中找到。您可以在#golem-projects 下找到它。

### 雷对傀儡

[Ray on Golem](https://github.com/golemfactory/ray-on-golem) 是与分布式计算框架 Ray 的令人兴奋的集成，为 Python 开发人员提供更简单的访问 Golem 网络的方法。

### golem-js - Golem 的 JS SDK

[golem-js](https://github.com/golemfactory/golem-js) 是一个库以及一组开发人员工具和文档，旨在使开发人员能够创建在 Node.js 或浏览器上下文中运行的 Golem 应用程序。

### Golem 上的 Jupyter

[Jupyter on Golem](https://github.com/golemfactory/golem-kernel-python) 是一个 JupyterLab Python 内核，使您能够使用 Golem 网络上可用的去中心化资源来运行 Python 笔记本。

### 在 Golem 上渲染

通过与 Reality Games 密切合作，我们开发了一项服务，可以激活 Golem 的提供者来渲染个性化建筑动画，作为 ERC-1155 代币的 (web2) 所有权证明。了解更多信息[此处](https://reality.golem.network/)


### 信誉系统

声誉系统的目标是解决网络中信任和可靠性的挑战，任何人都可以作为提供者或请求者参与，而无需任何身份验证。该系统旨在建立一个信任框架，确保网络参与者之间安全可靠的交互。

## 生态系统

### 区块链自动化（又名 Emeth.xyz）

Emeth 专注于 DeFi（去中心化金融）投资组合管理和区块链自动化。它利用 Golem 的技术提供自动化和简化 DeFi 投资管理的工具。该平台专注于提高 DeFi 领域运营的便利性和效率。它将用户友好的界面与复杂的分析相结合，满足新手和经验丰富的 DeFi 用户的需求。

## 开发者和请求者资源

- [Golem Docs](https://docs.golem.network/) - Golem 手册（适用于请求者和提供者）。
- [Python API Reference](https://yapapi.readthedocs.io/) - Yapapi API 参考。
- [Releases List](https://github.com/golemfactory/yagna/releases) - Yagna 的 GitHub 版本。
- [JS Requestor Quickstart](https://docs.golem.network/docs/quickstarts/js-quickstart) - 快速开始并在 Golem 上创建您的第一个任务/请求。
- [Yagna tag on Stack Overflow](https://stackoverflow.com/questions/tagged/yagna) - 如果您有一个有趣的问题想要得到解答，请使用 Yagna 标签。


## 提供商资源

- [Provider Tutorial](https://docs.golem.network/docs/providers/provider-installation) - 使用手册开始作为 Golem 网络的提供商。
- [Yagna-binaries for aarch64](https://github.com/MarijnStevens/yagna-binaries) - 针对 64 位 Arm 架构进行构建，以便能够作为提供程序在 Raspberry Pi 等系统上运行。
- [Automatically update provider node prices](https://gist.github.com/sv3t0sl4v/28f896752edc9e20347ffc6d8cefe74c) - 检查 stats.golem.network 上价格中位数并更新提供者节点上与价格相关的所有 3 个值的脚本。
- [Golem Price Updater](https://github.com/jedbrooke/golem-price-updater) - 根据 GLM 的当前价格自动调整 Golem 节点的价格。

### 监控

- [Golem Provider dashboard](https://github.com/vciancio/golem-dashboard) - ReactJS 仪表板用于快速从提供商节点收集状态，而无需通过 SSH 连接到它们。
- [Golem Provider dashboard backend / GolemBar](https://github.com/vciancio/golem-node-server) - Flask 后端从提供程序收集数据，然后与上面的仪表板项目一起使用。

### 配置

- [Ansible ya_provider](https://galaxy.ansible.com/golemfactory/ya_provider) - Ansible 角色，只需最少的配置即可自动部署 Golem 提供程序。
- [Golem Provider Terraform](https://github.com/nemani/golem-provider-terraform) - Terraform 脚本，用于在云提供商上自动部署 Golem Provider 并使用 prometheus 设置监控。
- [Automatic Golem](https://github.com/r34x/Automatic-Golem) - 使用简单的说明和日志设置 Golem 提供程序，指导您完成整个过程。
- [Golem Provider Node](https://github.com/alexandre-abrioux/golem-node) - 节点的 Docker 版本可帮助您快速开始在 Docker 容器中作为提供者运行。
- [Golem Provider node](https://github.com/blue-notes-robot/golem-node) - 上面的 Alxexandre-abrioux 项目的分支，允许从 ENV 变量动态生成配置文件并指定您想要生成的副本数量。

## 学习资源

### 演示和研讨会材料

- [Golem: Distributed parallel computing with JavaScript](https://www.youtube.com/watch?v=2iUhqOJUsoI) - Grzegorz Godlewski 关于基于 Golem 网络的 JavaScript 分布式并行计算的演示（meet.js 峰会 2023）。
- [Golem: Architecture, SDKs and tips with Jakub Mazurek at 0xHack](https://youtu.be/1UoZWC9XI2g) - 现场研讨会深入探讨具有 Python 或 JS 编码经验的开发人员如何开始构建在 Golem 上运行的应用程序。
  

### 揭开 Golem 的下一个里程碑博客系列的面纱

- [Unraveling Golem's The Next Milestone](https://blog.golemproject.net/next-milestone) - Golem 的 Yagna 实现简介。
- [Unraveling Golem's The Next Milestone, Part II](https://blog.golemproject.net/next-milestone-part-ii/) - 基本的建筑概念构成了 Golem Yagna 新实施的基础。
- [Unraveling Golem's The Next Milestone, Part III](https://blog.golemproject.net/next-milestone-part-iii/) - Golem 参考架构的元素，并说明了它们如何相互作用以形成一个工作生态系统，即 Golem 网络。

### GitHub 摘要博客系列

- [Golem GitHub Digest #1](https://blog.golemproject.net/golem-github-digest-1/) - 了解 Golem 存储库。
- [Golem GitHub Digest #2](https://blog.golemproject.net/golem-github-digest-2/) - 深入了解 Golem 存储库。
- [Golem GitHub Digest #3](https://blog.golemproject.net/golem-github-digest-3/) - 深入研究 Golem 存储库的 Pull 请求。
- [Golem GitHub Digest #4](https://blog.golemproject.net/golem-github-digest-4/) - 深入了解 Golem 存储库中的最新版本。
- [Golem GitHub Digest #5](https://blog.golemproject.net/golem-github-digest-5/) - 深入 Golem alpha 测试网。
- [Golem GitHub Digest #6](https://blog.golemproject.net/golem-github-digest-6/) - Golem 的 SGX 概念验证。
- [Golem GitHub Digest #7](https://blog.golemproject.net/golem-github-digest-7/) - Golem 市场的去中心化。
- [Golem GitHub Digest #8](https://blog.golemproject.net/golem-github-digest-8/) - 很棒的 Golem 和 Alpha 3 的后续步骤。
- [Golem GitHub Digest #9](https://blog.golemproject.net/golem-github-digest-9/) - AMD 提供商支持、网络指标和改进的提案处理。
- [Golem GitHub Digest #10](https://blog.golemproject.net/golem-github-digest-10/) - 社区反馈的改进。
- [Golem GitHub Digest #11](https://blog.golemproject.net/golem-github-digest-11/) - 轻松收集日志。
- [Golem GitHub Digest #12](https://blog.golemproject.net/golem-github-digest-12/) - 我们在主网上线并收集反馈。
- [Golem GitHub Digest #13](https://blog.golemproject.net/golem-github-digest-13/) - 在 Golem 社区的帮助下进步更快。
- [Golem GitHub Digest #14](https://blog.golemproject.net/golem-github-digest-14/) - 迈向下一个主要版本。
- [Golem GitHub Digest #15](https://blog.golemproject.net/golem-github-digest-15/) - 太棒了，哥特式改进，面向 Beta 3。
- [Golem GitHub Digest #16](https://blog.golemproject.net/golem-github-digest-16/) - VPN、请求者的 ARM 二进制文件以及自定义使用计数器。


## 贡献

欢迎向 Awesome Golem 提出拉取请求和问题建议！请在提交 PR 之前阅读 [contributing](contributing.md) 指南。

## 存档

### 应用程序

- [Chess On Golem](https://chessongolem.app/) - 托管国际象棋应用程序，利用 Stockfish 开源国际象棋引擎与网络提供商对弈。
- [Go le' Machin](https://github.com/DEUTSCHKLUB/go-le-m) - 基于 Web 的批量图像编辑器，允许用户上传多个图像并对它们应用批量操作。

#### 码头工人

- [Golem Requestor Node](https://github.com/DerekJarvis/general-golem) - Docker 化的请求者环境。传入 py 脚本，它会设置守护进程并运行它。

#### 测试

- [Golem Test Harness (Goth)](https://github.com/golemfactory/goth) - 该工具旨在加快您的开发过程并让应用程序创建者更享受其中。
- [Golem-afl](https://github.com/sladecek/golem-afl) - 一个实验性测试模糊框架。协助发现安全漏洞。
- [Golem Cargo Test](https://github.com/sladecek/golem_cargo_test) - Rust 项目的自适应分布式测试执行器。
- [Golem CI](https://github.com/hhio618/golem-ci) - 分散的任务管道。
- [Golem SLATE](https://github.com/deutschklub/golem-slate) - 上述“应用程序”部分中描述的 Golem SLATE 开源存储库。
- [ThorgPress](https://github.com/figurestudios/thorgpress) - 一种对提供商进行基准测试并揭示其真实能力的工具，其能力超出了市场所能看到的范围。

#### VPN

- [Yagna httpx client](https://github.com/golemfactory/ya-httpx-client/tree/johny-b/vpn) - Yagna 上的 VPN 使用演示了与基于提供商的 HTTP 服务器的通信方式，就像与任何其他 HTTP 服务器通信一样。
- [Golem Provider with network access](https://github.com/jedbrooke/golem-network-requestor) - 请求者充当运行提供者的 http 代理，允许他们访问更广泛的互联网。

#### 游戏

- [Golem Sudoku](https://github.com/Dodecane/golem-sudoku) - 具有不同尺寸的数独游戏。
- [HSOG-requester](https://github.com/ChrisHelmsC/hsog-requestor) - 通过运行大量模拟游戏，帮助《炉石传说》社区设计和构建套牌。
- [ChessOnGolem](https://github.com/broadcastmonkey/ChessOnGolem) - 第一个应用程序部分中描述了国际象棋的开源存储库。包括用于 2 个 AI 通过 Golem 后端相互对抗的 React 前端。
- [Golem Fleet Battle Simulator](https://github.com/UnfortuN8/Golem-Fleet-Battle-Simulator) - 用于计算两个敌对星舰舰队之间战斗结果的系统。在 iOS 游戏《岩纸护卫舰》中用于确定 PvP 舰队战斗的结果。

#### CLI工具

- [Golem Completion Engine](https://github.com/krunch3r76/gc__enhanced_completion) - 增强的 bash 补全引擎，通过为 golemsp 和 yagna 提供上下文帮助来扩展内置补全。
- [Golocity](https://github.com/davidstyers/golocity) - 只需两个命令即可在 Golem 网络上构建和部署 Docker 化应用程序。
- [gc__push_image](https://github.com/figurestudios/gc__push_image) - 一个 CLI 工具，可将 GVMI 映像发布到 Skynet，使用户能够更改 image_url，而无需自托管/放弃控制权。

#### 视频转码和编辑

- [Golem Network Video Transcoder](https://github.com/Doc-Saintly/golem-video) - 用于对视频进行转码的示例应用程序。选择您的转码配置文件，然后上传您的视频。
- [Golem Transcoding requestor](https://github.com/Edhendil/golem-transcoding) - 基于 React + Spring 的 Web 应用程序接受视频文件作为输入并将这些文件转码为不同的格式。
- [Golem Auto Editor](https://github.com/jedbrooke/golem-auto-editor) - 运行自动编辑器自动执行一些视频编辑功能，将视频处理卸载到 Golem。

#### 数据分析
- [Coacervate](https://github.com/pryce-turner/coacervate/) - Coacervate 是一种免费的开源公共产品，可让您在成本极低的全球超级计算机上轻松运行基因组分析；实现开展突破性研究所需知识和基础设施的民主化。
- [Flan](https://github.com/nestorbonilla/flan) - 为企业家提供对数百万条全球贸易价值记录进行定制分析的工具，为他们提供有关需要更多关注哪些行业的大胆指导。
- [Golem Lorenz-attractor](https://github.com/hhio618/golem-lorenz-attractor) - 三个耦合的一阶非线性微分方程组，描述粒子随时间的轨迹。
- [Golem Geomandel](https://github.com/Edhendil/golem-geomandel) - 用于生成以单个点为中心且每个图像的缩放比例增加的 Mandelbrot 图像序列的 Python 脚本。
- [Golem COVID](https://github.com/iRhonin/golem-covid) - 创建每百万人与新冠病毒相关的新死亡病例的图像。生成所有图像后，它将收集它们并创建一个 gif。
- [Golem Parallel Matplotlib](https://github.com/CoeJoder/golem-parallel-matplotlib) - 对人类测试对象的昼夜节律测量进行了各种统计分析。
- [Full-Text Search Engine](https://github.com/niklr/golem-fulltext-search) - 一种遍历文本文件的搜索引擎服务。

#### 数据模拟

- [cadCAD Golem](https://github.com/rogervs/cadcadgolem) - cadCAD 的软件包包装器可将模拟工作负载分派到多个 Golem 节点。支持 Jupyter 笔记本。
- [Golem Array](https://github.com/johngrantuk/golem-array) - 天线阵列设计与仿真。
- [Limit visualization](https://github.com/vporton/limit-visualization) - 绘制具有各种限制的图表。支持不连续图。
- [GolemGraphWavePair](https://github.com/smiley1983/golemGraphWavePair) - 生成图形框架，然后将它们组合成动画。
- [Golemized strong-gravitational-lense](https://github.com/rezahsnz/golemized-strong-gravitational-lense) - 简单的分布式计算黑客，模拟称为引力透镜的物理现象。

#### 数据优化

- [Golem or-tools](https://github.com/Doc-Saintly/golem-ortools) - 使用 or-tools 约束编程库来解决问题。
- [No more COFUD](https://github.com/DEUTSCHKLUB/no-more-COFUD) - 计算如何在一个空间内容纳最多的人，同时保持彼此之间 2 米的距离。
- [Mutta Puffs](https://github.com/DeveloperInProgress/Mutta-Puffs) - 体育联盟调度程序，使用基于群体的模拟退火来解决给定一组球队的旅行锦标赛问题。

#### 机器学习
- [DeML-Golem](https://github.com/anshuman73/DeML-Golem) - 去中心化机器学习使用联邦学习来组合子步骤模型，它在不同的提供者节点上训练成一个完整的模型。
- [Golem Image Classifier](https://github.com/ControlCplusControlV/Golem-Image-Classifier) - 通过主动服务对图像进行训练和分类。

#### 深度学习
- [Mlg](https://github.com/rezahsnz/mlg) - CNN 预测服务，一种深度学习应用程序，可分发使用 ImageNet 数据集预训练的流行 CNN。
- [Deepart Golem](https://github.com/echinocacti/deepart_golem) - 通过运行张量流应用程序、上传您的内容和风格图片，使用分布式计算进行艺术创作。

#### RNG
- [Gandom](https://github.com/rezahsnz/gandom) - 从提供商处提取随机流。支持两种 PRNG，一种基于 Chaos 机器，另一种使用 Sodium。
- [Entropythief](https://github.com/krunch3r76/entropythief) - 使用 Linux 熵源或 Intel 的 RDRAND CPU 指令（受 Gandom 启发）从多个提供商处以较低的价格获取随机熵。

#### 密码恢复
- [Golem-JTR](https://github.com/hhio618/golem-jtr) - 运行 John The Ripper 来恢复密码。
- [Yacat](https://docs.golem.network/docs/creators/python/tutorials/task-example-2-hashcat) - Hashcat 密码恢复步骤。

#### 去中心化金融

- [Golem Staking Pool incentivize system for GLM holders](https://github.com/masaun/GLM-stake-pool) - 智能合约旨在为 GLM 代币持有者提供流动性挖矿的机会。
- [Magic-doll](https://github.com/bakaoh/magic-doll) - Sumer 是一款 DeFi 应用程序，人们可以委托他们的 Splinterland 卡来赚取被动收入。它的核心是“Kyle”，一个 Golem 应用程序，它会进行所有计算来选择每场比赛的最佳球队。

#### 用户界面

- [Golem UI](https://github.com/shri4net/golem-hackathon-2020) - Yagna 的电子用户界面。

#### 杂项

- [Gc__ListOffers](https://github.com/krunch3r76/gc__listoffers) - 使用 GUI 列出 Golem 网络上提供商的报价。
- [gvm-vim](https://github.com/canokaue/gvm-vim) - 用于编译 VIM 编辑器的 Golemized docker 镜像。
- [Golem Image Sharpening](https://github.com/visualNext/golem) - 锐化图像的工具。
- [Filterms](https://github.com/krunch3r76/filterms) - 作为 Golem 请求者 (yapapi) 列入白名单或黑名单的市场策略。
- [golem-bulk-image-handler](https://github.com/figurestudios/golem-bulk-image-handler) - 获取输入图像并使用 Pillow 库以多种不同的方式对其进行处理。

