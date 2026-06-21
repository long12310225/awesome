<!--lint disable double-link-->
# 很棒的举动 [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> 来自 [Move](https://github.com/move-language/move) 编程语言社区的精选代码和内容列表。

Move 是一种用于编写安全智能合约的编程语言，最初由 Facebook 开发，为 Libra 区块链提供支持。 Move 被设计为一种与平台无关的语言，可在具有截然不同的数据和执行模型的不同区块链上启用通用库、工具和开发人员社区。 Move 的野心是成为无处不在的“web3 的 JavaScript”——当开发人员想要快速编写涉及资产的安全代码时，就应该用 Move 编写。

## 内容

- [Overview](#overview)
- [移动驱动的区块链](#move-powered-blockchains)
- [Books](#books)
- [Tutorials](#tutorials)
- [Community](#community)
- [Code](#code)
  - [可替代代币](#fungible-tokens)
  - [不可替代的代币](#non-fungible-tokens)
  - [去中心化身份](#decentralized-identity)
  - [DeFi](#defi)
  - [SocialFi](#socialfi)
  - [链上治理](#on-chain-governance)
  - [跨链桥](#cross-chain-bridge)
  - [Accounts](#accounts)
  - [Frameworks](#frameworks)
  - [Libraries](#libraries)
  - [Miscellaneous](#miscellaneous)
- [Tools](#tools)
- [IDEs](#ides)
- [包管理器](#package-managers)
- [Wallets](#wallets)
- [SDKs](#sdks)
- [Papers](#papers)
  - [语言设计](#language-design)
  - [静态分析与验证](#static-analysis-and-verification)
- [Videos](#videos)
- [Slides](#slides)
- [Podcasts](#podcasts)
- [博客文章](#blog-posts)
- [Security](#security)

## 概述

- [Installation](https://github.com/move-language/move/tree/main/language/tools/move-cli#installation)
- [问题陈述](https://github.com/mystenlabs/awesome-move/blob/main/docs/problem_statement.md#problem-statement)

## 移动驱动的区块链

- [Sui](https://github.com/MystenLabs/sui) - 下一代智能合约平台，具有高吞吐量、低延迟和由 Move 编程语言支持的面向资产的编程模型（在 [devnet](https://medium.com/mysten-labs/sui-devnet-public-release-a2be304ff36b)）。
- [0L](https://github.com/OLSF/libra) - 中性复制状态机的参考实现。从 Libra/Diem 技术分叉（在 [mainnet](https://0l.network/) 中）。
- [Starcoin](https://github.com/starcoinorg/starcoin) - 通过分层扩展的智能合约区块链网络（在 [mainnet](https://stcscan.io/) 中）。
- [Aptos](https://github.com/aptos-labs/aptos-core) - Aptos-core 致力于成为最安全、最具可扩展性的第一层区块链解决方案（在 [mainnet](https://explorer.aptoslabs.com/?network=mainnet) 中）。
- [Pontem](https://github.com/pontem-network/pontem) - 基于 Substrate 的平行链，内置 MoveVM（在 [testnet](https://polkadot.js.org/apps/?rpc=wss://testnet.pontem.network/ws#/explorer)）。
- [Celo](https://github.com/celo-org/celo-blockchain) - 具有 EVM 和 MoveVM 的区块链（[即将推出](https://www.businesswire.com/news/home/20210921006104/en/Celo-Sets-Sights-On-Becoming-Fastest-EVM-Chain-Through-Collaboration-With-Mysten-Labs)）。
- [Diem](https://github.com/diem/diem) - 来自 Meta 的原始基于 Move 的区块链（Facebook 的 Libra）（已停产）。
- [ChainX](https://github.com/chainx-org/ChainX) - 比特币的 Layer2 智能合约网络已经支持 WASM 和 EVM，并且正在支持 MoveVM（在 [mainnet](https://scan.chainx.org) 中）。

## 书籍

- [Move Book](https://move-language.github.io/move/) - Move book maintained by the Move core team ([中文](https://github.com/move-language/move/tree/main/language/documentation/book/translations/move-book-zh)).
- [Move Book](https://move-book.com/) - Move book maintained by [@damirka](https://github.com/damirka) ([中文](https://move-book.com/cn/)).
- [Move Patterns](https://www.move-patterns.com/) - 由 [@villesundell](https://github.com/villesundell) 维护的一本关于 Move 软件设计模式的书。
- [Sui Move by Example](https://examples.sui.io/) - 由 [@MystenLabs](https://github.com/MystenLabs) 维护的关于 Sui Move 变体的书。

## 教程

- [Implementing, testing, and verifying a fungible token](https://github.com/move-language/move/tree/main/language/documentation/tutorial) - 由 Move 核心团队维护。
- [Programming with objects](https://docs.sui.io/build/programming-with-objects) - 由 Sui 团队维护。
- [Move and SmartContract Development](https://starcoinorg.github.io/starcoin-cookbook/docs/move/) - 由星币团队维护。
- [Move Language](https://imcoding.online/courses/move-language) - Interactive Move language course, free for everyone, maintained by [imcoding.online](https://imcoding.online) ([中文](https://imcoding.online/courses/move-language?lng=zh)).

## 社区

- [移动语言不和谐](https://discord.gg/cPUmhe24Mz)
- [Move @ Sui by Mysten Labs Discord](https://discord.gg/sui)
- [移动@0L 不和谐](https://discord.gg/0lnetwork)
- [移动@Starcoin Discord](https://discord.gg/starcoin)
- [移动@Aptos Discord](https://discord.gg/aptoslabs)
- [MoveChina](https://move-china.com) - 最大的Move编程语言中文社区。

## 代码

用 Move 编写的代码。

### 可替代代币

- [Fungible token examples](https://github.com/MystenLabs/sui/tree/main/sui_programmability/examples/fungible_tokens) - Sui 的多个示例令牌实现。
- [BasicCoin](https://github.com/move-language/move/tree/main/language/documentation/examples/experimental/basic-coin) - 类似 [ERC20](https://ethereum.org/en/developers/docs/standards/tokens/erc-20/) 的可替代代币的玩具实现。
- [Diem](https://github.com/OLSF/libra/blob/main/language/diem-framework/modules/Diem.move) - 具有许可铸造/燃烧的类似 ERC20 的代币，另请参阅此[规范](https://github.com/diem/dip/blob/main/dips/dip-20.md)。部署在 0L 上。
- [Token](https://github.com/starcoinorg/starcoin-framework/blob/main/sources/Token.move) - 另一个类似 ERC20 的代币。部署在星币上。
- [GAS](https://github.com/OLSF/libra/blob/main/language/diem-framework/modules/0L/GAS.move) - 实例化上述 Diem 标准的令牌。部署在 0L 上。
- [STC](https://github.com/starcoinorg/starcoin-framework/blob/main/sources/STC.move) - 实例化上述星币标准的代币。部署在星币上。
- [STAR](https://github.com/Elements-Studio/starswap-core/blob/master/sources/gov/STAR.move) - Starswap dApp 的治理代币，为 AMM+DEX 生态系统提供动力。部署在星币上。
- [XUSDT](https://github.com/Elements-Studio/poly-stc-contracts/blob/master/sources/asset/erc20/XUSDT.move) - USDT 在 Starcoin 上的映射资产。
- [XETH](https://github.com/Elements-Studio/poly-stc-contracts/blob/master/sources/asset/erc20/XETH.move) - Starcoin 上 ETH 的映射资产。
- [WEN stablecoin](https://github.com/wenwenprotocol/wen-protocol) - 部署在星币上。
- [FAI stablecoin](https://github.com/BFlyFinance/FAI) - 部署在星币上的超额抵押稳定币。
- [FLY stablecoin](https://github.com/BFlyFinance/FLY) - 部署在 Starcoin 上的分叉 OHM 的实现。
- [Synthetic token backed by a basket containing a reserve of other tokens](https://github.com/OLSF/libra/blob/main/language/diem-framework/modules/XDX.move) - 来自迪姆。
- [XBTC](https://github.com/OmniBTC/OmniBridge/blob/main/aptos/bridge/sources/xbtc.move) - Aptos 上的 BTC 镜像资产。
- [XBTC](https://github.com/OmniBTC/OmniBridge/blob/main/sui/bridge/sources/xbtc.move) - Sui上的BTC镜像资产。

### 不可替代的代币

- [NFT examples](https://github.com/MystenLabs/sui/tree/main/sui_programmability/examples/nfts) - Sui 的多个 NFT 示例实现。
- [NFT](https://github.com/starcoinorg/starcoin-framework/blob/main/sources/NFT.move) - 类似 ERC721 的代币。部署在星币上。
- [Merkle Airdrop](https://github.com/starcoinorg/starcoin-framework/blob/main/sources/MerkleNFT.move) - 用于空投大量 NFT 的实用程序。部署在星币上。
- [NFT](https://github.com/diem/diem/blob/main/diem-move/diem-framework/experimental/sources/NFT.move) - 混合 ERC721/ERC1155 类代币的实现。来自迪姆。
- [BARS](https://github.com/diem/diem/blob/main/diem-move/diem-framework/experimental/sources/BARS.move) - 体现这种混合标准的 NFT。来自迪姆。
- [MultiToken](https://github.com/diem/diem/blob/main/diem-move/diem-framework/experimental/sources/MultiToken.move) - 类似 ERC1155 的代币。来自迪姆。
- [NFTGallery](https://github.com/diem/diem/blob/main/diem-move/diem-framework/experimental/sources/NFTGallery.move) - 用于保存多个相同类型的 NFT 的实用程序。来自迪姆。
- [NFT Protocol](https://github.com/Origin-Byte/nft-protocol) - NFT 协议和集合框架。来自 OriginByte。
- [Suia](https://github.com/Mynft/suia) - Sui 上的第一个 POAP 应用程序。

### 去中心化身份
- [aptos-cid](https://github.com/coming-chat/aptos-cid) - Aptos 上的去中心化身份，是 ComeChat 的底层账户系统。
- [MoveDID](https://github.com/NonceGeek/MoveDID) - MoveDID是一种DID协议，与基于Move的区块链网络兼容，包括Aptos、Sui和Starcoin。由 [NonceGeek](https://github.com/NonceGeek) 维护。


### 去中心化金融

- [DeFi examples](https://github.com/MystenLabs/sui/tree/main/sui_programmability/examples/defi) - Sui 的多个 DeFi 示例实现。
- [CoinSwap](https://github.com/move-language/move/tree/main/language/documentation/examples/experimental/coin-swap) - 类似 Uniswap 的流动性池的玩具实现，包含两个代币。
- [Starswap](https://github.com/Elements-Studio/starswap-core) - Uniswap 风格的 DEX。部署在星币上。
- [Offer](https://github.com/move-language/move/blob/main/language/move-stdlib/nursery/sources/offer.move) - 任何资产对的原子交换的通用实现。
- [AptosRedPacket](https://github.com/coming-chat/aptos-red-packet) - Aptos上一款集私密聊天和加密钱包于一体的红包社交应用。
- [SuiRedPacket](https://github.com/coming-chat/sui-red-packet) - Sui上一款集私密聊天和加密钱包于一体的红包社交应用。
- [AptosAMMswap](https://github.com/OmniBTC/Aptos-AMM-swap) - Aptos AMM Swap 由 OmniBTC 团队实施。
- [SuiAMMswap](https://github.com/OmniBTC/Sui-AMM-swap) - Sui AMM Swap 由 OmniBTC 团队实施。
- [AptosOmniSwap](https://github.com/OmniBTC/OmniSwap/tree/main/aptos) - 基于跨链互操作协议虫洞，aptos与EVM链（如ETH/BSC/AVAX等）之间一键互换。
- [DolaProtocol](https://github.com/OmniBTC/DolaProtocol) - 以各公链单一币池为核心，Wormhole、Layerzero等跨链消息协议为桥梁，以穗公链为结算中心的去中心化全链流动性聚合协议。
- [ObjectMarket](https://github.com/coming-chat/object-market) - Sui网络中独特的物品交易市场。

### 社交网络
- [Dmens](https://github.com/coming-chat/Dmens) - Decentralized Moments 是建立在 Sui 网络上的区块链 Twitter 协议。

### 链上治理

- [ValidatorUniverse](https://github.com/OLSF/libra/blob/main/language/diem-framework/modules/0L/ValidatorUniverse.move) - 验证器集管理。部署在 0L 上。
- [Oracle](https://github.com/OLSF/libra/blob/main/language/diem-framework/modules/0L/Oracle.move) - 用于链上社区投票。部署在 0L 上。
- [DAO](https://github.com/starcoinorg/starcoin-framework/blob/main/sources/Dao.move) - 用于链上提案和投票。部署在星币上。
- [DiemSystem](https://github.com/diem/diem/blob/main/diem-move/diem-framework/DPN/sources/DiemSystem.move) - 验证器集管理。来自迪姆。
- [Vote](https://github.com/diem/diem/blob/main/diem-move/diem-framework/experimental/sources/Vote.move) - 链上投票。来自迪姆。

### 跨链桥

- [Poly Bridge](https://github.com/Elements-Studio/poly-stc-contracts) - Move 和 EVM 之间的第一个跨链桥。部署在星币上。
- [OmniBTC Bridge](https://github.com/OmniBTC/OmniBridge) - 基于超轻节点的比特币与Move语言公链（如Aptos、Sui）之间的桥梁。

### 账户

- [Account](https://github.com/diem/diem/blob/main/diem-move/diem-framework/core/sources/Account.move) - Diem 支持的连锁店的通用账户。来自迪姆。
- [DiemAccount](https://github.com/OLSF/libra/blob/main/language/diem-framework/modules/DiemAccount.move) - 上面的叉子。从0L开始。
- [Account](https://github.com/starcoinorg/starcoin-framework/blob/main/sources/Account.move) - 上面的叉子。来自星币。

### 框架

Move **框架**是包含在链的创世状态中的一组 Move 模块。
这些模块通常实现账户、货币等关键概念。
将区块链特定框架逻辑与 Move 语言的通用功能分开的能力是 Move 平台无关设计的关键部分。

- [隋框架](https://github.com/MystenLabs/sui/tree/main/crates/sui-framework)
- [阿普托斯框架](https://github.com/aptos-labs/aptos-core/tree/main/aptos-move/framework)
- [0L框架](https://github.com/OLSF/libra/tree/main/language/diem-framework/modules/0L)
- [星币框架](https://github.com/starcoinorg/starcoin-framework)
- [迪姆框架](https://github.com/diem/diem/tree/main/diem-move/diem-framework/DPN)

### 图书馆

- [Move standard library](https://github.com/move-language/move/tree/main/language/move-stdlib) - 旨在（但不是必需）在运行 Move 的每个平台中使用的实用程序。来自 Move 存储库。
- [Move nursery](https://github.com/move-language/move/tree/main/language/move-stdlib/nursery) - 最终可能被提升到标准库中的实验模块。来自 Move 存储库。
- [Decimal](https://github.com/OLSF/libra/blob/main/language/diem-framework/modules/0L/Decimal.move) - 十进制值的有效实现。从0L开始。
- [Math](https://github.com/starcoinorg/starcoin-framework/blob/main/sources/Math.move) - 数学实用函数。来自星币。
- [Compare](https://github.com/move-language/move/blob/main/language/move-stdlib/nursery/sources/compare.move) - 多态比较（即比较相同类型的任意两个 Move 值）。来自托儿所。
- [Vault](https://github.com/move-language/move/blob/main/language/move-stdlib/nursery/sources/vault.move) - 能力库。来自托儿所。
- [ACL](https://github.com/move-language/move/blob/main/language/move-stdlib/nursery/sources/acl.move) - 用于基于列表的访问控制的库。来自托儿所。
- [TaoHe](https://github.com/taoheorg/taohe) - 可嵌套的 Move 资源的集合。
- [Starcoin Framework Commons](https://github.com/starcoinorg/starcoin-framework-commons) - starcoin 框架上的 Move commons 实用程序库。来自星币。
- [Movemate](https://github.com/pentagonxyz/movemate) - Aptos 和 Sui 的智能合约构建块（数学实用程序、治理合约、托管等）。由五角大楼团队维护。
- [Move cron parser](https://github.com/snowflake-so/move-cron-parser#readme) - 库是为了解析 cron 表达式而构建的。由雪花网络团队维护。

### 杂项

- [Move-on-EVM](https://github.com/move-language/move/tree/main/language/evm) - 将源代码编译为 EVM 字节码的实验项目。
- [aoc-move](https://github.com/whonore/aoc-move) - Move 中代码解决方案的出现，经过一些形式验证。

## 工具

- [Move Package Manager](https://github.com/move-language/move/tree/main/language/tools/move-cli) - 就像 Move 的 `cargo` 或 `npm` 一样：单个 CLI（以及用于其他工具挂钩的相应 Rust API）用于构建、运行、测试、调试和验证 Move [packages](https://move-language.github.io/move/)。由 Move 核心团队维护。
- [Move Prover](https://github.com/move-language/move/tree/main/language/move-prover) - 对用 Move 源代码编写的用户定义规范进行形式验证。由 Move 核心团队维护。
- [Move Read/Write Set Analyzer](https://github.com/move-language/move/tree/main/language/tools/read-write-set) - 静态分析工具，用于计算 Move 程序所触及的全局内存的过近似值。由 Move 核心团队维护。
- [Move Playground JS Library](https://github.com/imcoding-online/js-move-playground) - 将 [Move Playground by Pontem](https://playground.pontem.network/) 包装为浏览器的 JavaScript 库。您可以使用它来构建您自己的 Move Playground。
- [go-sui-indexer](https://github.com/coming-chat/go-sui-indexer) - 一个非全节点服务，用于从 Sui Node 提供数据。

## IDE

- [Move VS Code plugin](https://marketplace.visualstudio.com/items?itemName=move.move-analyzer) - 由 Move 核心团队维护（[源代码](https://github.com/move-language/move/tree/main/language/move-analyzer)）。
- [Move IntelliJ plugin](https://plugins.jetbrains.com/plugin/14721-move-language) - 由 Pontem 团队维护（[源代码](https://github.com/pontem-network/intellij-move)）。
- [Move Playground](https://playground.pontem.network/) - 就像 Move 的 [Remix](https://remix.ethereum.org/) 一样。 Web IDE 的 Alpha 版本。请参阅[说明](https://gist.github.com/borispovod/64b6d23741d8c1f4b0b958a3a74aa68d)。由 Pontem 团队维护。
- [Starcoin IDE](https://marketplace.visualstudio.com/items?itemName=starcoinorg.starcoin-ide) - 由 Starcoin 团队维护（[源代码](https://github.com/starcoinorg/starcoin-ide)）。
- [Move Vim](https://github.com/rvmelkonian/move.vim) - 由 [@rvmelkonian](https://github.com/rvmelkonian/) 维护。
- [move-mode](https://github.com/amnn/move-mode) - Emacs 的主要模式由 [@amnn](https://github.com/amnn/) 维护。

## 包管理器
- [Movey](https://www.movey.net/) - 一个 crates.io 风格的 Move 包存储库。

## 钱包

- [StarMask](https://github.com/starcoinorg/starmask-extension) - Starcoin 区块链的钱包。由 Starcoin 团队维护（[Chrome 网上应用店](https://chrome.google.com/webstore/detail/starmask/mfhbebgoclkghebffdldpobeajmbecfk?hl=en)）。
- [Sui Wallet](https://github.com/MystenLabs/sui/tree/main/apps/wallet) - 适用于 Sui 的 chrome (v88+) 扩展钱包（[Chrome Webstore](https://chrome.google.com/webstore/detail/sui-wallet/opcgpfmipidbgpenhmajoajpbobppdil)）。
- [Pontem Wallet](https://github.com/pontem-network/pontem-wallet) - Pontem 团队针对 Aptos 网络的钱包扩展（[Chrome 网上应用店](https://chrome.google.com/webstore/detail/pontem-wallet/phkbamefinggmakgklpkljjmgibohnba)）。
- [Fewcha Aptos Wallet](https://github.com/fewcha-wallet/fewcha.app) - 第 1 层区块链 Aptos 的钱包（[Chrome Webstore](https://chrome.google.com/webstore/detail/fewcha-aptos-wallet/ebfidpplhabeedpnhjnobghokpiioolj)）。
- [bcs-js](https://github.com/pontem-network/lcs-js) - Move 使用的 [BCS](https://github.com/diem/bcs) 序列化方案的 JavaScript 实现可能对于实现钱包很有用。
- [ComingChat](https://coming.chat/) - 去中心化的社会金融/web3 门户。  支持公链钱包，如Sui、Aptos钱包。
- [Suiet Wallet](https://github.com/suiet/suiet) - Sui 的开源钱包。 （[Chrome 网上应用店](https://chrome.google.com/webstore/detail/suiet/khpkpbbcccdmmclmpigdgddabeilkdpd)、[网站](https://suiet.app))
- [Ethos Wallet](https://github.com/EthosWallet/chrome-extension) - 适用于 Sui 的开源 chrome 扩展钱包（[Chrome 网上应用店](https://chrome.google.com/webstore/detail/ethos-sui-wallet/mcbigmjiafegjnnogedioegffbooigli)、[网站](https://ethoswallet.xyz/)）。

### 钱包适配器

- [Sui Wallet](https://github.com/MystenLabs/sui/tree/main/sdk/wallet-adapter) - Sui 钱包适配器。
- [Suiet Wallet](https://github.com/suiet/wallet-adapter) - Suiet 钱包适配器。

### 钱包套件

- [Suiet Wallet Kit](https://github.com/suiet/wallet-kit) - 软件包支持所有 Sui 钱包，具有可定制的 UI。
- [Ethos Connect](https://github.com/EthosWallet/ethos-connect) - 具有内置钱包适配器和电子邮件选项的 UI，用于支持 Sui 上的所有钱包和无钱包用户。

## 软件开发工具包

### 隋 SDK
- [Rust SDK](https://docs.sui.io/devnet/build/rust-sdk)（官方）
- [TS/JS SDK](https://github.com/MystenLabs/sui/tree/main/sdk/typescript)（官方）
- [Golang SDK 1](https://github.com/coming-chat/go-sui-sdk)（社区）
- [Golang SDK 2](https://github.com/block-vision/sui-go-sdk)（社区）
- [Python SDK](https://github.com/FrankC01/pysui)（社区）
- [Java SDK](https://github.com/GrapeBaBa/sui4j)（社区）
- [Kotlin SDK](https://github.com/cosmostation/suikotlin)（社区）
- [C# SDK](https://github.com/naami-finance/SuiNet)（社区）

### Sui Dapps SDK
- [OmniSwap-Sui-SDK](https://github.com/OmniBTC/OmniSwap-Sui-SDK)（社区）

### 其他网络SDK
- [Aptos Golang SDK](https://github.com/coming-chat/go-aptos-sdk)（社区）

## 论文

### 语言设计

- [Move: A Language With Programmable Resources](https://developers.diem.com/papers/diem-move-a-language-with-programmable-resources/2019-06-18.pdf) - 这是 2018 年发布的原始 Move 白皮书。其中的许多方面现在都已经过时了（例如，字节码指令的语法和描述），但前两部分值得一读，因为它解释了使用资产进行编程的困难以及 Move 如何解决这些困难。
- [强大的移动安全性](https://arxiv.org/abs/2110.05043)
- [移动借用检查器](https://arxiv.org/abs/2205.05181)
- [资源：金钱的安全语言抽象](https://arxiv.org/abs/2004.05106)

### 静态分析与验证

- [使用 Move Prover 对智能合约进行快速可靠的形式验证](https://arxiv.org/abs/2110.08362)
- [移动证明者](https://research.facebook.com/publications/the-move-prover/)
- [Libra Move语言编写的程序验证](https://ethz.ch/content/dam/ethz/special-interest/infk/chair-program-method/pm/documents/Education/Theses/Constantin_M%C3%BCller_MS_Report.pdf)
- [精确且线性时间的 Gas 成本分析](https://research.facebook.com/publications/exact-and-linear-time-gas-cost-analysis/)

## 视频

- [移动编程语言](https://youtu.be/J1U_0exNFu0)
- [继续隋](https://www.youtube.com/watch?v=xMsE1X4wio4)
- [继续阿普托斯](https://www.youtube.com/watch?v=gvRJdJTQd8U)
- [Move: A Safe Language for Programming with Money](https://www.youtube.com/watch?v=EG2-7bQNPv4&ab_channel=FieldsInstitute) - [@sblackshear](https://github.com/sblackshear) 在 [Fields Institute Blockchain](http://www.fields.utoronto.ca/activities/seminar_series/blockchain-research-seminar-series) 研究研讨会系列中的演讲。
- [Formal Verification of Move Programs for the Libra Blockchain](http://www.fields.utoronto.ca/talks/Formal-verification-Move-programs-Libra-blockchain) - [@DavidLDill](https://github.com/DavidLDill) 在 [Fields Institute Blockchain](http://www.fields.utoronto.ca/activities/seminar_series/blockchain-research-seminar-series) 研究研讨会系列中的演讲。
- [Move for the Masses](https://www.youtube.com/watch?v=b_2jZ4YEfWc) - 在 [Converge '22](https://converge.circle.com/event/4ea0d06f-3900-4b6d-a9cd-aeaedda9ef2e/summary) 上进行演讲。

## 幻灯片
- [移动深潜](https://docs.google.com/presentation/d/1Tb2iZD0xrQSlwXIJNL1djNYc0_p0szfB2STgURgHgls/edit?usp=sharing)
- [Move overview](https://docs.google.com/presentation/d/1gU-M42Juz7ARc61unPXphJ_BX1OlQrBwR1VdaPT4M5w/edit?usp=sharing) - 来自 [SBC '22](https://cbr.stanford.edu/sbc22/) 的 [关于金融系统的推理](https://reasoningaboutfinancialsystems.org/) 研讨会的幻灯片。

## 播客

- [与来自 Mysten Labs 的 Sam Blackshear 一起 Move and Sui](https://zeroknowledge.fm/228-2/)
- [Move AMA 涵盖 Move 起源故事](https://twitter.com/i/spaces/1jMKgepNOleJL)

## 博客文章
- [比较 Move 和 Rust 智能合约开发](https://medium.com/@kklas/smart-contract-development-move-vs-rust-4d8f84754a8f)
- [帝姆式走法与隋式走法的比较](https://sui.io/resources-move/why-we-created-sui-move)

## 安全性
- [Aptos-movevm 拒绝服务漏洞](https://medium.com/numen-cyber-labs/analysis-of-the-first-critical-0-day-vulnerability-of-aptos-move-vm-8c1fd6c2b98e)

## 贡献

欢迎投稿！首先阅读[贡献指南](CONTRIBUTING.md)。
