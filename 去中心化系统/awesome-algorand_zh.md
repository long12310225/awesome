# 很棒的 Algorand [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

<div align="center">
<a href="https://github.com/awesome-algorand/awesome-algorand"><img src="https://dweb.link/ipfs/QmfTGB4EFu1FypcZEWWgs3jCmFw75MrqezVV7oQbnbQPyQ" /></a>
</div>
<br/>
<div align="center">
⚡ A curated list of awesome resources related to the <a href='https://www.algorand.co/'>Algorand</a> Blockchain.
<br />
<br />
Algorand is an open-source, proof of stake Blockchain and smart contract computing platform.
</div>

<p align="center">
    <img  src="https://api.visitorbadge.io/api/visitors?path=aorumbayev%2Fawesome-algorand&countColor=%23000000&style=flat" />
    <a target="_blank" href="https://awesomealgo.com"><img src="https://img.shields.io/badge/url-website-black.svg" /></a>
    <a target="_blank" href="https://github.com/awesome-algorand/awesome-algorand"><img src="https://img.shields.io/badge/url-repository-black.svg" /></a>
    <br />
    <a target="_blank" href="https://rss.com/podcasts/the-awesomealgo-podcast"><img src="https://img.shields.io/badge/podcast-rss-black.svg?color=gold" /></a>
    <a target="_blank" href="https://coinmarketcap.com/currencies/algorand/"><img src="https://img.shields.io/badge/coinmarketcap-price-black.svg?color=teal" /></a>
    <a target="_blank" href="https://github.com/awesome-algorand/awesome-algorand"><img src="https://img.shields.io/github/stars/awesome-algorand/awesome-algorand?color=teal" /></a>
    <a target="_blank" href="https://github.com/awesome-algorand/awesome-algorand/network/members"><img src="https://img.shields.io/github/forks/awesome-algorand/awesome-algorand?color=gold" /></a>
</p>

## 内容

- [核心资源](#core-resources)
  - [官方资源](#official-resources)
  - [AlgoKit](#algokit)
  - [AlgoKit 模板](#algokit-templates)
- [学习资源](#learning-resources)
  - [速成班](#crash-courses)
  - [普通课程](#general-courses)
  - [Tutorials](#tutorials)
  - [社区资源](#community-resources)
  - [Projects](#projects)
  - [AlgoKit 社区模板](#algokit-community-templates)
- [开发与工具](#development--tools)
  - [语言 SDK 和工具](#language-sdks--tools)
  - [智能合约开发](#smart-contract-development)
  - [CLI](#cli)
  - [IDEs](#ides)
  - [测试与调试](#testing--debugging)
  - [部署与环境](#deployment--environment)
- [钱包与资产交互](#wallets--asset-interaction)
  - [钱包提供商](#wallet-providers)
  - [钱包开发](#wallet-development)
  - [区块链探索者](#blockchain-explorers)
  - [投资组合追踪器](#portfolio-trackers)
  - [名称服务](#name-services)
- [基础设施和生态系统服务](#infrastructure--ecosystem-services)
  - [节点&共识参与](#nodes--consensus-participation)
  - [区块链桥梁](#blockchain-bridges)
  - [Oracles](#oracles)
  - [安全审计服务](#security-auditing-services)
  - [指标和分析服务](#metrics-and-analytics-services)
- [SSI、DID 和可验证凭证](#ssi-did-and-verifiable-credentials)
- [人工智能和机器学习](#ai-and-machine-learning)
- [应用平台和示例](#application-platforms--examples)
  - [去中心化金融平台](#defi-platforms)
  - [NFT 市场](#nft-marketplaces)
  - [预测市场](#prediction-markets)
  - [订阅管理](#subscription-management)
  - [去中心化投票](#decentralized-voting)
- [Standards](#standards)
  - [Algorand 征求意见](#algorand-request-for-comments)

## 核心资源

### 官方资源

> Algorand 的官方资源。

- [Algorand](https://algorandtechnologies.com/) - 官方网站。
- [Algorand Foundation](https://algorand.foundation/) - 基金会官方网站。
- [Algorand FAQ](https://algorand.foundation/faq) - 由 Algorand 基金会维护的常见问题解答。
- [Algorand Governance](https://governance.algorand.foundation/) - Algorand 治理计划的官方网站。
- [Algorand Developer Portal](https://dev.algorand.co/) - 官方 Algorand 开发者门户。
- [Algorand Protocol Specs](https://github.com/algorandfoundation/specs) - Algorand 平台的协议级规范文档。
- [Algorand Discord](https://discord.com/invite/YgPTCVk) - 官方 Algorand Discord 服务器。

### 算法套件

> AlgoKit 是为在 Algorand 网络上构建的开发人员提供的官方一站式工具。由 Algorand 基金会维护。

- [algokit-cli](https://github.com/algorandfoundation/algokit-cli) - Algorand AlgoKit CLI 是为在 Algorand 网络上构建的开发人员提供的一站式工具。
- [algokit-lora](https://lora.algokit.io/mainnet) - 可视化本地网络浏览器和应用程序构建器，用于测试 Algorand 应用程序（部署合约、检查状态、工艺交易）。
- [AlgoKit Docs](https://dev.algorand.co/algokit/algokit-intro/) - Algorand AlgoKit 官方文档。
- [algokit-utils-py](https://github.com/algorandfoundation/algokit-utils-py) - 用于 Python 的 Algorand AlgoKit Utils。
- [algokit-core](https://github.com/algorandfoundation/algokit-core) - 多语言核心原语（Rust + FFI 绑定）为更高级别的 AlgoKit 工具（加密、编码、协议逻辑）提供支持。
- [algokit-utils-ts](https://github.com/algorandfoundation/algokit-utils-ts) - 用于 TypeScript 的 Algorand AlgoKit Utils。
- [algokit-client-generator-py](https://github.com/algorandfoundation/algokit-client-generator-py) - 适用于 Python 的 Algorand AlgoKit 类型客户端生成器。
- [algokit-client-generator-ts](https://github.com/algorandfoundation/algokit-client-generator-ts) - 适用于 TypeScript 的 Algorand AlgoKit 类型化客户端生成器。
- [puya](https://github.com/algorandfoundation/puya) - 官方的 Python 到 TEAL 编译器，允许您使用 Python 语法编写在 Algorand 虚拟机 (AVM) 上执行的代码。
- [puya-ts](https://github.com/algorandfoundation/puya-ts) - 官方 TypeScript 到 TEAL 编译器前端利用核心 puya 编译器，允许您使用 TypeScript 语法编写在 Algorand 虚拟机 (AVM) 上执行的代码。
- [algorand-python-testing](https://github.com/algorandfoundation/algorand-python-testing) - 用于单元测试 Algorand Python 智能合约的 Python 库，无需与 Algorand 区块链交互。
- [algorand-TypeScript-testing](https://github.com/algorandfoundation/algorand-TypeScript-testing) - 用于单元测试 Algorand 智能合约的 TypeScript 库，无需与 Algorand 区块链交互。
- [algokit-avm-vscode-debugger](https://github.com/algorandfoundation/algokit-avm-vscode-debugger) - VSCode 扩展，用于通过 AVM 跟踪对 Algorand Python、TypeScript、TealScript 和原始 TEAL 智能合约进行逐行调试。

### AlgoKit 模板
> AlgoKit 模板是一组入门级和生产就绪的基线模板，用于开发和部署 Algorand 应用程序。它们旨在用作开发人员快速引导其项目并专注于应用程序的业务逻辑的起点。有关如何创建自己的 AlgoKit 模板的一般指南，请参阅[创建 AlgoKit 模板](https://github.com/algorandfoundation/algokit-cli/blob/main/docs/tutorials/algokit-template.md)。

- [algokit-python-template](https://github.com/algorandfoundation/algokit-python-template) - 官方 AlgoKit 的 Algorand Python 模板为在 Python 中开发和部署智能合约提供了生产就绪的基线。
- [algokit-TypeScript-template](https://github.com/algorandfoundation/algokit-TypeScript-template) - 官方 AlgoKit 的 Algorand TypeScript 模板为在 TypeScript 中开发和部署智能合约提供了生产就绪的基线。
- [algokit-react-frontend-template](https://github.com/algorandfoundation/algokit-react-frontend-template) - 官方 AlgoKit React 前端模板提供了一个生产就绪的基线，用于开发和部署集成了 Algorand 依赖项的 React 前端应用程序。还可以作为模板构建者实现独立 algokit 前端模板的参考。
- [algokit-fullstack-template](https://github.com/algorandfoundation/algokit-fullstack-template) - 官方 AlgoKit 全栈模板为开发和部署集成了 Algorand 依赖项的全栈应用程序提供了生产就绪基线。还可以为模板构建者提供有关如何在一个完整堆栈模板项目下组合独立 algokit 模板的参考。

## 学习资源

> Algorand 学习资源列表。包括课程、教程和其他资源。

### 速成班

- [Algorand School](https://github.com/cusma/algorand-school) - 速成课程幻灯片。
- [Zero to Hero PyTeal](https://www.youtube.com/playlist?list=PLwRyHoehE435ttTjvFZA-DyqHYIYc26K_) - PyTeal 速成课程视频讲座。
- [Algorand, efficient self-sustaining Blockchain](https://prismic-io.s3.amazonaws.com/algorandfoundationv2/d5407f96-8e7d-4465-9656-2abb558850a9_Proof+of+Stake+Blockchain+Efficiency+Framework.pdf) - 权益证明区块链效率框架。
- [Algorand Efficiency](https://www.youtube.com/watch?v=e8s8Ui8vDaY) - 了解 Algorand 的工作原理及其效率。
- [Introduction to AVM and Applications](https://www.youtube.com/watch?v=fTAPLiPcj28) - Algorand 虚拟机架构和 Algorand 智能合约（又名应用程序）简介。
- [Introduction to PyTeal](https://www.youtube.com/watch?v=zXDqJHK_Bqs) - PyTeal 演练，用于开发 Algorand 智能合约的 Python 框架（使用 [@matteojug](https://twitter.com/matteojug)）。
- [PyTeal ABI Smart Contracts](https://www.youtube.com/watch?v=USLcyfVD_ws) - 使用 PyTeal 在 Algorand 上开发_ABI 兼容_智能合约。最后的实时编码部分（与 [@deanste](https://twitter.com/_deanste)）。
- [Beaker](https://www.youtube.com/watch?v=031VvOxvuxY) - 基于 PyTeal 的 Algorand 智能合约开发、客户端和测试框架。实时编码会议（与 [@HGKimChris](https://twitter.com/HGKimChris)）。
- [Dissecting Algorand](https://medium.com/coinmonks/dissecting-algorand-e962f48f8c72) - Algorand 简介以及 Algorand 内部工作原理分析。
- [Zero to Hero Blockchain Algorand](https://github.com/VKappaKV/Zero-To-Hero-blockchain-Algorand) - 为 Algorand 开发者精心策划的学习路径。


### 普通课程

> 请注意，这些内容适用于对与所有区块链系统相关的基础知识感兴趣的绝对初学者。对区块链协议领域的理论理解是一个重要的先决条件，可以显着增强您对 Algorand 技术的学习。

- [Foundations of Blockchains](https://www.youtube.com/watch?v=KNJGPI0fuFA&list=PLEGCF-WLh2RLOHv_xUGLqRts_9JxrckiA) - 哥伦比亚大学计算机科学教授 Tim Roughgarden 的视频课程强调了区块链协议的基本原理、概念和属性。

### 教程

- [Lending pool using Reach](https://developer.algorand.org/tutorials/building-a-lending-pool-using-reach/) - 有关如何使用 Reach 语言构建借贷池的教程。
- [Creating a License Manager Contract](https://developer.algorand.org/tutorials/creating-a-license-manager-contract-utilizing-pyteal-and-inner-transactions/) - 有关使用 PyTEAL 和内部事务的教程。
- [Stateless session management with the Pera wallet](https://developer.algorand.org/tutorials/stateless-session-management-with-the-pera-wallet/) - Pera Wallet 与 Next.js 和 Redux 的连接示例。
- [AlgoMinter](https://developer.algorand.org/tutorials/algominter-a-web-app-for-minting-assets-using-python-algosigner-and-anvil-platform/) - 使用 Python、AlgoSigner 和 Anvil Platform 构建用于铸造资产的 Web 应用程序。
- [Getting Started with Django, Python, and Algorand](https://developer.algorand.org/solutions/getting-started-with-python-algorand-sdk-and-django/) - 来自 algorand 开发者门户的教程。
- [MultiSig with Algorand for Co-operative Groups](https://developer.algorand.org/tutorials/decentralised-co-operative-unions-algorand-multisignature-account/) - 具有 Algorand 多重签名账户的去中心化合作联盟。
- [Adding Notes to Transactions](https://developer.algorand.org/tutorials/v2-read-and-write-transaction-note-field-python/) - 使用 Python 读取和写入交易备注字段。
- [Create Assets with a Stateful Smart Contract](https://developer.algorand.org/solutions/using-stateful-smart-contract-to-create-algorand-standard-asset/) - 使用有状态智能合约创建 Algorand 标准资产。
- [Artificial Intelligence on Algorand](https://developer.algorand.org/solutions/artificial-intelligence-on-algorand/) - 有关使用机器学习预测 Algorand 区块链上 USDC 稳定币交易量的教程。

### 社区资源

> 以下包含与开源项目、实用程序和新闻资源相关的部分。

### 项目

> 基于 Algorand 构建的开源项目、博客、网站的列表。

- [arc3.xyz](https://github.com/barnjamin/arc3.xyz) - 可用于铸造符合 ARC3 标准的 NFT 的 Dapp。
- [Auction Demo](https://github.com/algorand/auction-demo) - 使用智能合约的链上 NFT 拍卖。
- [Algorand Session Wallet](https://github.com/barnjamin/algorand-session-wallet) - 会话钱包允许跨多个钱包的持久钱包连接。
- [AlgoWorld-Contracts](https://github.com/algoworldNFT/algoworld-contracts) - AlgoWorld 使用的所有智能合约的集合，用 PyTeal 编写。
- [AlgoWorld-Swapper](https://github.com/algoworldNFT/algoworld-swapper) - 免费且无需信任的 ASA 交换器，由 Algorand 智能签名提供支持。
- [WalletConnect Example DApp](https://github.com/algorand/walletconnect-example-dapp) - Algorand WalletConnect 演示。
- [TinyBar App](https://github.com/aorumbayev/tinybar) - 一款小型 macOS 菜单栏应用程序，用于跟踪 TinyMan 的 ASA 价格。
- [algonim](https://github.com/cusma/algonim) - 第一款 Algorand 迷你益智游戏。由 [@cusma](https://twitter.com/cusma_b) 用 Python+PyTEAL 编写。
- [algorealm](https://github.com/algorealm/algorealm) - 夺取 Algorand 领域的王冠和权杖！由 [@cusma](https://github.com/cusma) 用 Python+PyTEAL 编写。
- [algorealm-ui](https://github.com/algorealm/algorealm-ui) - @aorumbayev 的 algorealm cli 游戏的 Web CLI 模拟器版本。
- [minter](https://github.com/algofishexe/minter) - 遵循 ARC-69 社区标准批量铸造 Algorand NFT。由 [@fish.exe](https://twitter.com/AlgofishExe) 用 Node.js 编写。
- [algovanity](https://algovanity.com/) - 来自 [Ripe](https://github.com/Ripe/algovanity) 的 Algorand Vanity 地址生成器。
- [galvanity](https://github.com/shmutalov/galvanity) - 基于 Go 的 Algorand 虚荣地址生成器。
- [genpyteal](https://github.com/runvnc/genpyteal) - 从（大部分）普通 Python 生成 PyTeal。
- [AgorHash](https://github.com/bafio89/agorhash) - 公开的、无需许可的、去中心化的、不可审查的自由言论协议。
- [QRCode Generator](https://github.com/emg110/algorand-qrcode) - 适用于 Algorand ARC-26 URI 的通用 QRCode 生成器模块。
- [algofractals](https://github.com/aorumbayev/algofractals) - Mint 随机生成带有嵌入 ARC69 标签的曼德尔布罗分形。 （存档于2023年12月31日）
- [algorewards](https://algorewards.github.io/) - 免费且非官方的 Algorand 治理奖励计算器。托管在 GitHub 页面上。
- [Pipeline-UI](https://github.com/headline-design/pipeline-ui) - 一个基于 React.js 的组件库，用于快速部署 Algorand Dapps。
- [STOI](https://stoi.org/) - 歌曲所有权通过 microDAO 实现去中心化。
- [AlgoTables](https://algotables.github.io/) - 一套工具，旨在帮助参与 Algorand 生态系统的日常 ALGO 持有者。
- [AlgoPing](https://github.com/aorumbayev/algoping) - 如果公共 Algorand 节点（AlgoExplorer、AlgoNode 等）不健康，它会发出 [tweet](https://twitter.com/algoping) 的小型 cron 作业。
- [staketaxcsv](https://github.com/hodgerpodger/staketaxcsv) - [stake.tax](https://stake.tax) 的 Python 后端，为 Algorand 和其他区块链生成应税交易 CSV。
- [Automated Prediction Market Maker on Algorand](https://github.com/dspytdao/Algo_AMM) - 项目托管在 [algoAMM.com](https://algoamm.com) 的后端存储库。
- [AlgoDepo](https://github.com/dspytdao/AlgoDepo) - 单次存款应用程序 Algorand。
- [AlgoDeposit](https://github.com/dspytdao/AlgoDeposit) - AMM 矿池应用程序 Algorand。
- [txnDuck](https://github.com/No-Cash-7970/txnDuck) - Algorand 区块链的交易构建工具。
- [lazylora](https://github.com/aorumbayev/lazylora) - 用于探索 Algorand 区块链的终端 UI。
- [wen-tools](https://github.com/LoafPickleWW/wen-tools) - Algorand 的批量操作工具。
- [algonoderewards](https://github.com/cryptomalgo/algonoderewards) - 使用 Nodely API 跟踪和可视化 Algorand 节点奖励。
- [xGov-Guru](https://github.com/SilentRhetoric/xGov-Guru) - 用于浏览 xGov 投票数据和提案的工具。

### AlgoKit 社区模板

> AlgoKit 社区模板是一组入门级和生产就绪的基线模板，用于开发和部署由 Algorand 社区中的项目和个人创建的 Algorand 应用程序。

- [algokit-tealish-template](https://github.com/aorumbayev/algokit-tealish-template) - AlgoKit 社区模板，用于使用 Tealish 和 algojig 快速启动智能合约项目。
- [algokit-goracle-template](https://github.com/GoracleNetwork/algokit_default_template) - Algokit 社区模板，用于快速启动与 goracle 交互的智能合约项目。
- [algokit-subtopia-template](https://github.com/subtopia-algo/algokit-subtopia-template) - Algokit 社区模板，用于快速启动与 Subtopia 平台交互的 dapp 前端项目。

## 开发与工具

> 很棒的用于开发的客户端库、工具和社区实用程序。

### 语言 SDK 和工具

> 很棒的客户端库、工具和社区实用程序，按实现语言排序。

#### C/C++

- [vertices-algorand-sdk](https://github.com/vertices-network/c-vertices-sdk) - Vertices SDK 为开发人员提供了轻松的设备访问来与区块链交互。
- [unreal-algorand-sdk](https://github.com/Wisdom-Labs/Algorand-Unreal-Engine-SDK) - Algorand 区块链平台的官方虚幻引擎插件。
- [cplusplus-algorand-sdk](https://github.com/Wisdom-Labs/Algorand-CPlusPlus-SDK) - Algorand C++ SDK：该仓库在 algorand 链上提供 C++ sdk。

#### 飞镖

- [dart-algorand-sdk](https://pub.dev/packages/algorand_dart) - Dart 算法和 SDK。

#### 去

- [go-algorand](https://github.com/algorand/go-algorand) - Algorand 在 Go 中的正式实现。
- [go-algorand-sdk](https://github.com/algorand/go-algorand-sdk) - Algorand Golang SDK。
- [conduit](https://github.com/algorand/conduit) - Algorand 的数据管道框架。

#### PHP

- [php-algorand-sdk](https://github.com/ffsolutions/php-algorand-sdk) - Algorand PHP SDK 由 [@ffsolutions](https://github.com/ffsolutions) 创建。
- [algorand-php](https://github.com/RootSoft/algorand-php) - Algorand PHP SDK 由 [@RootSoft](https://github.com/RootSoft) 创建。

#### 蟒蛇

- [py-algorand-sdk](https://github.com/algorand/py-algorand-sdk) - Algorand Python SDK。
- [tinyman-py-sdk](https://github.com/tinymanorg/tinyman-py-sdk) - Tinyman Python SDK。
- [smart-asa](https://github.com/algorandlabs/smart-asa) - 基于 ARC-20 的智能 ASA PyTeal 参考实施。

#### JavaScript 和 TypeScript

- [js-algorand-sdk](https://github.com/algorand/js-algorand-sdk) - Algorand JavaScript SDK 和示例。
- [algo-builder](https://github.com/scale-it/algo-builder) - 自动开发 Algorand 资产和智能合约的框架。
- [algo-builder-templates](https://github.com/scale-it/algo-builder-templates) - Algo Builder 的 Dapps 模板。
- [algonaut.js](https://github.com/thencc/algonautjs) - 用于前端 dapp 的更简单的 Algo sdk (TypeScript)。
- [perawallet-connect](https://github.com/perawallet/connect) - 用于将 Pera Wallet 集成到 Web 应用程序的 JavaScript SDK。
- [defly-connect](https://github.com/blockshake-io/defly-connect) - 用于将 Defly Wallet 集成到 Web 应用程序的 JavaScript SDK。
- [subtopia-js](https://github.com/subtopia-algo/subtopia-js) - Subtopia JavaScript SDK 提供与 Subtopia 平台交互的便捷接口。
- [solid-algo-wallets](https://github.com/SilentRhetoric/solid-algo-wallets) - Algorand 的 SolidJS 钱包集成库。

#### 爪哇

- [java-algorand-sdk](https://github.com/algorand/java-algorand-sdk) - Algorand Java SDK。

#### .NET

- [dotnet-algorand-sdk](https://github.com/RileyGe/dotnet-algorand-sdk) - Algorand .NET SDK 由 [@RileyGe](https://github.com/RileyGe) 创建。
- [unity-algorand-sdk](https://github.com/CareBoo/unity-algorand-sdk) - 适用于 Unity 的 Algorand SDK。在您的视频游戏中使用 Algorand 区块链。
- [unity-algorand-sdk-based-on-net-sdk](https://github.com/Vytek/AlgorandUnitySDK) - RileyGe 基于 .NET Algorand SDK 的快速而肮脏的 Unity SDK。
- [dotnet-alogrand-sdk (2)](https://github.com/FrankSzendzielarz/dotnet-algorand-sdk) - Algorand .NET SDK 由 [@FrankSzendzielarz](https://github.com/FrankSzendzielarz) 维护。
- [dotnet-tinyman-sdk](https://github.com/geoffodonnell/dotnet-tinyman-sdk) - Tinyman .NET SDK。
- [dotnet-yieldly-sdk](https://github.com/geoffodonnell/dotnet-yieldly-sdk) - .NET SDK。
- [powershell-algorand-module](https://github.com/geoffodonnell/powershell-algorand-module) - Algorand PowerShell 模块。

#### 铁锈

- [rust-algorand-sdk](https://github.com/manuelmauro/algonaut) - Rust 算法和 SDK。

#### 斯威夫特

- [algorand-wallet](https://github.com/algorand/algorand-wallet) - Algorand 钱包在 Swift 中的官方实现。
- [swift-algorand](https://github.com/CorvidLabs/swift-algorand) - 适用于 Algorand 区块链的现代 Swift SDK，具有异步/等待和 Swift 并发支持。
- [swift-algorand-sdk](https://github.com/Jesulonimi21/Swift-Algorand-Sdk) - 用于与 Algorand 区块链交互的 Swift SDK。
- [swift-algokit](https://github.com/CorvidLabs/swift-algokit) - 面向 Swift 开发人员的 AlgoKit 实用程序。
- [swift-arc](https://github.com/CorvidLabs/swift-arc) - 用于使用 NFT 的 Algorand ARC 元数据标准的 Swift 库。
- [swift-mint](https://github.com/CorvidLabs/swift-mint) - 用于在 Algorand 区块链上铸造 NFT 的 Swift 库。
- [swift-algochat](https://github.com/CorvidLabs/swift-algochat) - Algorand 上的端到端加密消息传递，以及 Swift 中的混合 ECDH 和 PSK 棘轮。

#### 红宝石

- [TEALrb](https://github.com/joe-p/TEALrb) - 用于编写 Algorand 智能合约的 Ruby DSL。 （存档于2023年1月22日）


### 智能合约开发

#### 语言和编译器
- [pyteal](https://github.com/algorand/pyteal) - Python 中的 Algorand 智能合约。
- [reach](https://docs.reach.sh) - 用于构建跨链去中心化应用程序（DApp）的特定领域语言。
- [aqua-compiler](https://github.com/optio-labs/aqua-compiler) - 一种用于 Algorand 区块链的富有表现力的高级语言，可编译为 TEAL 代码。
- [algoml](https://github.com/petitnau/algoml) - 一种用于指定 Algorand 智能合约的领域特定语言，可编译为 TEAL 脚本。
- [tealang](https://github.com/pzbitskiy/tealang) - Algorand ASC1 和 TEAL 的高级语言。
- [tealish](https://tealish.tinyman.org) - 可读的 Algorand VM 语言支持注重清晰度的程序式 TEAL。
- [TEALScript](https://github.com/algorand-devrel/TEALScript) - 通过原生 TypeScript 语法、工具和 IDE 支持实现 Algorand 智能合约开发。

#### 框架和实用程序
- [beaker](https://github.com/algorandfoundation/beaker) - Pythonic 智能合约框架（PyTEAL DSL 包装器、客户端 + 测试实用程序）。 （规范回购）
- [pyteal-utils](https://github.com/algorand/pyteal-utils) - PyTEAL 实用程序库。
- [avm-semantics](https://github.com/runtimeverification/avm-semantics) - K 框架中的 Algorand 虚拟机和 TEAL 语义。帮助智能合约的测试和形式验证。
- [d-asa](https://github.com/cusma/d-asa) - 债务算法和标准应用程序为符合 ACTUS 标准的债务工具（债券、贷款、商业票据）代币化提供参考实现和接口。


### 命令行界面

- [AlgoRun](https://github.com/algorandfoundation/algorun) - 用于设置和启动 Algorand 主网参与节点的简单 CLI 实用程序。


### IDE

> 很棒的客户端库、工具、社区插件和 IDE 集成。

#### 维姆

- [vim-algorand-teal](https://github.com/aldur/vim-algorand-teal) - Algorand 的 TEAL 智能合约语言的简约语法突出显示到 vim。

#### 智能

- [algoDEA](https://algodea-docs.bloxbean.com/) - Algorand IntelliJ 插件。

#### VS代码

- [Obsidian Labs/vscode-algorand](https://github.com/ObsidianLabs/vscode-algorand) - Algorand VS 代码扩展。
- [optio-labs/teal-debugger-extension](https://github.com/optio-labs/teal-debugger-extension) - 在 VSCode 内使用最少的 AVM 配置调试青色。

#### 视觉工作室

- [Algorand Visual Studio Extension](https://github.com/FrankSzendzielarz/AlgorandVisualStudio) - 用于 C# TEAL 编译和 Algorand 智能合约开发的 Visual Studio 扩展。


### 测试与调试

- [graviton](https://github.com/algorand/graviton) - Algorand 的 TEAL 黑盒测试工具包。
- [algokit-avm-debugger](https://github.com/algorandfoundation/algokit-avm-debugger) - 独立 AVM 调试适配器协议实现为高级合同调试工具提供支持。
- [tealer](https://github.com/crytic/tealer) - 带有一组漏洞检测器的静态 TEAL 分析器，用于快速合同审查。
- [irulan](https://irulan.dev/) - 用于部署和测试智能合约的 Web 应用程序（[开源！+ 欢迎 PR](https://github.com/thencc/irulan)）。
- [algojig](https://github.com/Hipo/algojig) - 用于测试 Algorand 智能合约的工具。
- [tealinspector](https://github.com/Hipo/tealinspector) - Hipo 实验室快速轻松地进行 TEAL 代码调试。
- [swift-algotest](https://github.com/CorvidLabs/swift-algotest) - 用于 Algorand 智能合约的 Swift 测试框架，支持模拟链。


### 部署与环境

- [Algorand Sandbox](https://github.com/algorand/sandbox) - 创建和配置 Algorand 开发环境的快速方法。
- [Algorand Sandbox Dev](https://github.com/MakerXStudio/algorand-sandbox-dev) - Docker Hub 映像可加快本地开发和 CI/CD 使用速度。 （存档于2024年1月2日）
- [Official Algod Container](https://hub.docker.com/r/algorand/algod) - Algod Docker Hub 镜像来自 Algorand Inc.
- [Official Conduit Container](https://hub.docker.com/r/algorand/conduit) - 来自 Algorand Inc. 的 Conduit Docker Hub 镜像


## 钱包与资产交互

### 钱包提供商

> Algorand 钱包提供商列表。请注意，此列表并不详尽，也不代表任何钱包提供商的认可。
> ⚠️鉴于MyAlgo钱包用户受到[攻击](https://twitter.com/myalgo_/status/1632862464244162560)，相关sdk已被排除在列表之外。

- [Pera Wallet](https://github.com/perawallet) - 适用于移动和桌面设备的安全、开源和社区驱动的钱包。由官方 Algorand 钱包背后的团队维护。
- [Method Wallet](https://methodwallet.app/) - 您一定会喜欢的 Algorand 钱包。
- [Defly Wallet](https://defly.app/) - Defly 是一款 Algorand 钱包，具有出色的集成 DeFi 功能。
- [Exodus](https://www.exodus.com/) - 支持 Algorand 的多加密货币钱包。
- [A-Wallet](https://a-wallet.net/) - AWallet 是一款开源、仅 HTML、企业友好且安全的 Algorand 钱包。
- [Liquid Auth](https://github.com/algorandfoundation/liquid-auth) - 自托管服务，用于将密钥绑定到加密密钥对以及用于安全对等连接的 P2P 信令。
- [Kibisis](https://github.com/kibis-is/web-extension) - 使用 React 和 TypeScript 构建的开源 Algorand 钱包 Web 扩展。


### 钱包开发

- [use-wallet](https://github.com/txnlab/use-wallet) - React hooks 用于在 Web 应用程序中使用 Algorand 兼容钱包。由[txnlab](https://www.txnlab.dev/)开发。
- [use-wallet-js](https://github.com/TxnLab/use-wallet-js) - 用于将 Algorand 钱包集成到去中心化应用程序中的 TypeScript 库。
- [rsagg](https://github.com/dragmz/rsagg) - 用于 GPU 加速 Algorand“虚荣”地址生成的 Rust 库。


### 区块链探索者

> Algorand 的区块链浏览器列表。用于查看交易、账户、资产等。

- [Allo](https://allo.info) - Nodely 覆盖所有网络的统一 Algorand 浏览器。
- [Pera Explorer](https://explorer.perawallet.app/) - Algorand Accounts，由 [Pera Wallet](https://perawallet.app/) 构建的标准资产 (ASA) 浏览器
- [Algorand Ballet](https://akaalias.github.io/algorand-ballet/) - Algorand 账户的二维图表。
- [Algorand Multiverse](https://algo3d.live/) - Algorand 账户的 3D 图表。
- [AlgoSurf](https://algo.surf/) - Algorand Network Explorer（支持 `localhost` 中的 LocalNet）。
- [Algo Explorer](https://github.com/corvid-agent/algo-explorer) - 现代 Algorand 区块链浏览器，具有实时交易监控功能。


### 投资组合追踪器

> Algorand 的投资组合跟踪器列表。帮助跟踪您的资产价值。

- [CompX](https://app.compx.io/dashboard) - 随时随地跟踪或搜索 Algorand 区块链上的资产、奖励、流动性挖矿、交易和 NFT。以前称为 Algogator.Finance。
- [ASA Stats](https://www.asastats.com/) - 一站式投资组合跟踪器，用于总结最多五个钱包地址的 Algorand 资产估值。


### 名称服务

> 允许人类可读地址的名称服务列表。

- [NFDomains](https://nf.domains/) - Algorand 名称服务和不可替代域名 (NFD) 市场 — 钱包地址的唯一、可读别名。


## 基础设施和生态系统服务

### 节点&共识参与

- [Algorand - The Undocumented Docs](https://github.com/AlgoChads/algorand-undoc-docs) - 存档节点、索引器设置（等等）的开发说明。
- [Nodely](https://nodely.io) - 免费的节点/索引器 API、节点运行常见问题解答、节点/索引器每日快照。
- [Algorand Node UI](https://github.com/algorand/node-ui) - 用于远程 Algorand 节点管理的终端 UI。
- [nodekit](https://github.com/algorandfoundation/nodekit) - 用于在本地运行和管理 Algorand 节点的终端用户界面。
- [SubQuery](https://subquery.network) - Algorand 的开放、快速、灵活且去中心化的跨链数据索引器（[入门指南](https://academy.subquery.network/quickstart/quickstart_chains/algorand.html)）。
- [AlloCTRL](https://github.com/AlgoNode/alloctrl) - 一个简单的开源仪表板，可帮助从本地计算机安全地管理节点和参与密钥。
- [reti](https://github.com/algorandfoundation/reti) - Algorand“The Reti”共识激励的合约、节点守护进程和 UI，使去中心化的质押池能够扩大参与范围并增强网络安全性。


### 区块链桥梁

> 这提供了允许在 Algorand 和其他区块链之间进行资产跨链转移的桥梁列表。

- [Algomint](https://algomint.io/) - 中心化 BTC 和 ETH 桥接到 Algorand。
- [Messina](https://messina.one/) - ALGO — ETH 双向 Messina.one 桥将为以太坊和 ERC-20 代币与 Algorand 之间的互操作性打开大门。


### 神谕者

> 允许智能合约与现实世界交互的预言机解决方案列表。

- [Gora](https://www.gora.io/) - 连接 Algorand 区块链与现实世界的去中心化预言机网络。


### 安全审计服务

> 本节无意宣传以下任何公司，请在研究可用于审计的选项时尽职调查。相反，以下内容只是为了强调为 Algorand 生态系统提供智能合约审计的公司种类不断增多。

- [Certik](https://www.certik.com/ecosystems/algorand) - Web3 安全套件：针对 Algorand 项目的智能合约审计和分析（Skynet、SkyTrace）。
- [UlamLabs](https://www.ulam.io/software-services/smart-contract-audits) - 位于波兰的区块链实验室，为 Algorand 智能合约提供审计服务。
- [Runtime Verification](https://runtimeverification.com/smartcontract) - 由审核 Algofi、FolksFinance、Yieldly 以及生态系统中其他知名 DeFi 平台等平台的团队进行智能合约分析和验证。
- [Immunebytes](https://www.immunebytes.com) - 使用可靠的安全审计解决方案保护您的 Algorand 智能合约。
- [KudelskiSecurity](https://kudelskisecurity.com) - 将您的区块链项目安全、成功地转移到生产环境或主网上。公司可以帮助您评估、设计、定制、部署和管理区块链和数字账本技术系统，以便您可以自信地利用安全性作为这个动态市场中的强大差异化因素。
- [algorand-ecosystem-audits](https://github.com/blockshake-io/algorand-ecosystem-audits) - 由 [blockshake-io](https://blockshake.io) 维护的 Algorand 生态系统中越来越多的审计报告。
- [Vantage Point Blockchain](https://www.vantagepoint.sg/contact-us) - Algorand 生态系统中的智能合约审计、加密钱包审计和其他渗透测试服务，客户包括 Folks.Finance、Pera、Algorand Foundation、Deflex (Defly/Alammex)、GARD、Venue.One 等。报告由velocity.vantagepoint.algo 签名并发布在https://github.com/vantagepointreports/releases。
- [Tenset Security](https://github.com/tenset-security/audits) - Tenset Security 由 Web3 安全研究人员团队组成，致力于不遗余力地追求卓越的安全性。他们在发现 Algorand 项目中特别是高严重性漏洞方面拥有[经过验证的成功记录](https://twitter.com/algoworld_nft/status/1691891473166279042)，强调了他们的专业知识和对 Algorand 生态系统的承诺。


### 指标和分析服务

> Algorand 的指标和分析服务。

- [Algorand MainNet metrics](https://metrics.algorand.org/) - 衡量开源 Algorand 协议当前规模、安全性、去中心化和采用情况的仪表板。
- [Metrika](https://app.metrika.co/dashboard/algorand/) - Algorand 网络性能和账户监控。
- [Allo Metrics](https://metrics.allo.info/) - Algorand 主网的数字。

## SSI、DID 和可验证凭证

> W3C 去中心化标识符、可验证凭证和自我主权身份服务项目列表。

- [GoPlausible](https://goplausible.com) - 提供 [PLAUSIBLE 协议](https://github.com/GoPlausible)、基于 Algorand 构建的 W3C DID、可验证凭证和实用 NFT 协议，以及 [ThisDID](https://thisdid.com) 通用 W3C DID/URI 解析器。


## 人工智能和机器学习

> 利用 Algorand 的人工智能、机器学习和数据科学项目列表。

- [Algorand-GPT](https://chatgpt.com/g/g-izA6hnC93-algorand-gpt) - Algorand 助理专家，可以访问由 GoPlausible 在 OpenAI 的 ChatGPT 平台上构建的所有 Algorand 文档和链数据。
- [DID-GPT](https://chatgpt.com/g/g-rOCQculZQ-did-gpt) - 由 GoPlausible 在 OpenAI 的 ChatGPT 平台上构建的 W3C DID 解析器助手。
- [algorand-mcp](https://github.com/GoPlausible/algorand-mcp) - GoPlausible 的 Algorand 模型上下文协议（服务器和客户端）。
- [algorand-remote-mcp](https://github.com/GoPlausible/algorand-remote-mcp) - Algorand 远程 SSE MCP 服务器 Cloudflare Worker。
- [arcontextify](https://github.com/aorumbayev/arcontextify) - Algorand ARC-56 到 MCP 服务器转换器。
- [VibeKit](https://github.com/gabrielkuettel/vibekit) - CLI + MCP 服务器为 AI 编码助理提供在 Algorand 上构建的技能和工具。
- [corvid-agent](https://github.com/corvid-agent/corvid-agent) - 一个基于 Algorand 构建的自主人工智能代理平台，具有加密的链上消息传递。
- [AlgoChat](https://github.com/corvid-agent/corvid-agent-chat) - 使用 Algorand 交易和 PSK 棘轮的加密点对点聊天客户端。
- [algorand-agent-skills](https://github.com/algorand-devrel/algorand-agent-skills) - Algorand DevRel 在 Algorand 上进行人工智能辅助开发的代理技能规范集合。


## 应用平台和示例

### 去中心化金融平台

> Algorand 上很棒的 DeFi 平台和协议。请注意，此列表并非旨在推广任何特定项目，而是提供生态系统的全面概述。在投资或使用此处列出的任何项目之前，请先进行自己的研究。

- [Tinyman](https://tinyman.org/) - 去中心化交易协议、AMM 和平台。
- [Pact](https://www.pact.fi/) - 基于 Algorand 协议构建的去中心化自动做市商 (AMM)。
- [Lofty.ai](https://www.lofty.ai/) - 代币化的房地产投资平台。
- [Folks.finance](https://folks.finance/) - 去中心化资本市场协议。
- [Cometa.farm](https://cometa.farm/) - 去中心化的流动性即服务。
- [aramid.finance](https://www.aramid.finance/) - 支持 Algorand、Polygon、Ethereum 和其他 EVM 链的去中心化跨链协议。
- [stabilitas.finance](https://stabilitas.finance/) - 稳定、安全的数字资产，用于购买、汇款和作为价值储存等多种用途。
- [vestige.fi](https://vestige.fi/) - 去中心化的工具生态系统，主要用作跟踪和趋势整个生态系统中的 Algorand 标准资产和流动性池的工具。该平台还提供去中心化交换和启动板平台。
- [folks-router](https://github.com/Folks-Finance/folks-router) - Folks Finance 在 Algorand 上的高效交换路由 SDK。
- [Folks-Finance/algorand-js-sdk](https://github.com/Folks-Finance/folks-finance-js-sdk) - 官方民间金融 Algorand 协议 SDK。
- [DorkFi](https://dork.fi/) - Algorand 和 Voi 网络上的跨链借/贷协议。具有超额抵押贷款、WAD 稳定币铸造和 UNIT 治理代币。


### NFT 市场

> Algorand 上精彩的 NFT 市场和画廊。

- [Rand Gallery](https://www.randgallery.com/) - Algorand 标准资产 (ASA) 浏览器和市场由 [Chris Antaki](https://github.com/ChrisAntaki) 开发。
- [AlgoGems](https://algogems.io/) - Algorand Standard Asset (ASA) 为 NFT 收藏者提供的市场和交易平台。
- [AlgoMart](https://github.com/deptagency/algomart) - 开源 NFT 市场白标解决方案。
- [Flatter](https://www.flatternft.com/) - NFT 艺术品和收藏品市场。
- [NFT Gallery](https://github.com/corvid-agent/nft-gallery) - 支持 ARC 标准的 Algorand NFT 图库浏览器。

### 预测市场

> Algorand 上很棒的预测市场和交易平台。

- [Alpha Arcade](https://www.alphaarcade.com/) - Algorand 上的预测市场平台。

### 订阅管理

> Algorand 上很棒的订阅管理平台。请注意，此列表并非旨在推广任何特定项目，而是提供生态系统的全面概述。在投资或使用此处列出的任何项目之前，请先进行自己的研究。

- [Subtopia](https://subtopia.io/) - 面向 dApp 创建者的去中心化订阅管理平台和 Algorand 平台。管理和拥有您的订阅基础设施、设置灵活的计划、折扣并通过 Algo 或任何 ASA 代币获得付款。由@aorumbayev 创建。


### 去中心化投票

> 由 Algorand 支持的链上投票工具

- [nft_voting_tool](https://github.com/algorandfoundation/nft_voting_tool) - Algorand 基金会的官方投票工具。该存储库包含一个投票工具，允许使用 Algorand 区块链创建和促进不可变、防篡改的投票。


## 标准

### Algorand 征求意见

> _最终_ ARC 中定义的标准和规范。
> 所有 ARC 的列表可以在[此处](https://arc.algorand.foundation)找到。

- [ARC3](https://github.com/algorandfoundation/ARCs/blob/main/ARCs/arc-0003.md) - 可替代和不可替代代币的官方 Algorand 标准资产参数约定。
- [ARC4](https://github.com/algorandfoundation/ARCs/blob/main/ARCs/arc-0004.md) - 应用程序二进制接口。
- [ARC32](https://github.com/algorandfoundation/ARCs/blob/main/ARCs/arc-0032.md) - 应用规范。
- [ARC56](https://github.com/algorandfoundation/ARCs/blob/main/ARCs/arc-0056.md) - 扩展和改进的应用规范。
- [ARC69](https://github.com/algorandfoundation/ARCs/blob/main/ARCs/arc-0069.md) - Algorand 标准资产参数约定之一。


## 贡献

欢迎投稿！首先阅读[贡献指南](https://github.com/awesome-algorand/awesome-algorand/blob/main/contributing.md)。

特别感谢所有分叉或加星标的存储库❤️
