# 很棒的堆栈[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[![Awesome Stacks](img/awesome-stacks.png 'Awesome Stacks')](https://www.stacks.co)

[Stacks](https://www.stacks.co/what-is-stacks) 是一个以比特币为基础的区块链，支持应用程序、智能合约和数字资产。 Stacks是一个连接比特币的第一层区块链，通过[Clarity语言](https://clarity-lang.org/)实现智能合约和去中心化应用。通过[传输证明（PoX）共识机制](https://docs.stacks.co/stacks-101/proof-of-transfer)，Stacks区块链的状态锚定在比特币区块链上，从而为Stacks提供了比特币的安全性和最终性。 Stacks为比特币带来了其他区块链技术的可编程性，而无需修改比特币本身的核心共识机制。

## 内容

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
<!--lint ignore awesome-list-item-->

- [Apps](#apps)
  - [Wallets](#wallets)
  - [堆栈 Web 应用程序](#stacks-web-applications)
  - [区块链名称系统](#blockchain-name-system)
  - [DeFi](#defi)
  - [Games](#games)
  - [堆叠应用程序](#stacking-apps)
- [清晰度资源](#clarity-resources)
  - [开发者工具](#developer-tools)
  - [合同示例](#example-contracts)
  - [库和协议](#libraries--protocols)
  - [Contracts](#contracts)
  - [不可替代的代币](#non-fungible-tokens)
  - [可替代代币](#fungible-tokens)
  - [Stacking](#stacking)
- [应用程序开发](#app-development)
  - [客户端库](#client-libraries)
  - [CLI](#cli)
  - [索引和查询 API](#indexing-and-querying-apis)
- [学习资源](#learning-resources)
  - [Documentation](#documentation)
  - [Videos](#videos)
  - [书面教程](#written-tutorials)
  - [Books](#books)
  - [Courses](#courses)
- [Community](#community)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## 应用程序

### 钱包

- [Asigna](https://asigna.io) - 适用于比特币、Ordinals、BRC20 和 Stacks 的多重签名钱包。
- [Leather Wallet](https://leather.io/) - 用于连接比特币和 Stacks Web 应用程序的开源钱包。也适用于移动设备。
- [OKX Web3 Wallet](https://web3.okx.com/download) - 也支持 Stacks 的多链钱包。
- [Xverse Wallet](https://www.xverse.app) - 用于管理比特币、STX 和堆栈的移动钱包应用程序和浏览器扩展（部分开源）。
- [WalletConnect](https://docs.reown.com/advanced/multichain/rpc-reference/stacks-rpc) - 如何将 Wallet Connect (Reown) 与 Stacks 结合使用的文档。

### 堆栈 Web 应用程序

- [Hiro Explorer](https://explorer.hiro.so/?chain=mainnet) - 用于审查 Stacks 区块链上交易的应用程序。
- [STXER](https://stxer.xyz/) - Stacks 事务的浏览器、调试器和模拟器。
- [Send Many](https://sendstx.com) - 一种在一笔交易中向多个接收者发送 STX 和其他代币的应用程序。
- [Speed Spend](https://speed-spend.org) - 测试网上的一套有效的 Clarity 实验（[来源](https://github.com/friedger/speed-spend)）。
- [Blocksurvey](https://blocksurvey.io) - 人工智能驱动的调查平台，重点关注数据所有权和隐私。
- [AIBTC](https://aibtc.com/) - 致力于可衡量任务的人工智能代理协调网络。
- [FatStx](https://fatstx.github.io/) - 年度交易查看器，例如纳税申报。

### 区块链名称系统

- [BNS V2](https://www.bnsv2.com/) - Stacks 上所有区块链名称空间的中心，包含交易历史记录和分析。
- [btc.us](https://btc.us) - .btc 名称的申请。
- [Owl.link](https://owl.link) - 为 BNS 名称创建链接页面的应用程序。

### 去中心化金融

- [Bitflow](https://www.bitflow.finance/) - 去中心化交易所。
- [Velar](https://www.velar.co/) - 在顶级比特币 L2 上交换、交易、启动资产。
- [Zest Protocol](https://www.zestprotocol.com/) - 比特币和 Stacks 上的去中心化借贷。
- [FakFun](https://fak.fun) - 基于比特币构建的 memecoin 交换、发布、包装平台。
- [Alex Lab](https://app.alexlab.co) - DeFi 服务平台。
- [Arkadiko Protocol](https://arkadiko.finance) - 基于自还贷款的稳定币（USDA）。
- [Granite](https://granite.world/) - 一种比特币流动性协议，提供非托管、安全和去中心化的比特币借款方式。
- [BSD](https://www.bsd.money/) - 一种由比特币支持的合成数字美元，采用超额抵押借贷模式。
- [USDh](https://app.hermetica.fi) - 一种由比特币衍生的、具有收益的合成美元，使用空头永续期货头寸和机构级托管人。
- [STXTools](https://stxtools.io/) - Stacks 上 DeFi 的图表、交易、价格提醒。
- [Stacks Pulse](https://www.stackspulse.com/) - Stacks DeFi 的实时链上统计数据。
- [Signal21](https://signal21.io/) - 比特币 L1、L2 和 Dapp 的链上分析。
- [Lydian](https://app.lydian.xyz) - 去中心化财务管理协议（已停产）。
- [CityCoins](https://minecitycoins.com) - 城市代币（逐步结束）。

### 游戏

- [Stacks Degens](https://stacksdegens.com) - 一款通过 NFT 启用的具有复古图形的赛车游戏。
- [Project Indigo](https://www.projectindigonft.com) - 互动故事和角色扮演游戏体验。

### 堆叠应用程序

- [Stacking on Leather](https://app.leather.io/stacking) - 用于直接或通过池堆叠 Stacks 令牌的应用程序。
- [Fast pool](https://fastpool.org/) - 信任最小化堆叠池。
- [PlanBetter pool](https://planbetter.com/) - 带有比特币奖励的堆叠池。
- [Xverse pool](https://pool.xverse.app/) - Xverse 移动应用程序中内置的堆叠池。
- [Stacking DAO](https://www.stackingdao.com/) - 液体堆叠在堆栈上。
- [Lisa](https://app.lisalab.io) - 使用变基在堆栈上进行液体堆叠。
- [Stacking Tracker](https://stacking-tracker.com) - Stacking和历史数据概述[源代码](https://github.com/StackingDAO/stacking-tracker)。

## 清晰度资源

### 开发者工具

- [Clarinet](https://github.com/hirosystems/clarinet) - Clarity 运行时打包为 CLI，有助于 Clarity 智能合约的开发和测试。
- [Clarigen](https://github.com/obylabs/clarigen) - 用于编写与 Clarity 智能合约交互的 TypeScript 代码的工具。
- [clarity.tools](https://clarity.tools) - 浏览器内 Clarity REPL。
- [ClarityGPT Prompt](https://claritygpt.com/) - 使用聊天机器人编写智能合约。
- [Hiro Platform](https://platform.hiro.so/) - 浏览器内 IDE。
- [secondlayer](https://github.com/ryanwaits/secondlayer) - 使用 React 挂钩和测试实用程序为 Clarity 合约生成 TypeScript 代码。灵感来自克拉瑞根。

### 合同示例

- [Source of Clarity](https://source-of-clarity.com) - 主网上所有部署的 Clarity 合约的列表以及一些评论。
- [Example Contracts](https://github.com/hirosystems/clarity-examples) - 示例智能合约的集合，可作为编写您自己的智能合约的起点。
- [Audited Example Smart Contracts](https://github.com/clarity-lang/book/tree/main/projects) - 另一个智能合约示例集合，这些示例已经过安全审核。

### 库和协议

- [blaze](https://gist.github.com/r0zar/414e91d3e6769644981b4918141a1708) - 基于签名的授权协议。
- [uint256](https://github.com/KStasi/clarity-uint256-lib) - 用于将值转换为 256 位的库。
- [clarity-bitcoin](https://github.com/friedger/clarity-bitcoin) - 验证比特币交易的库。
- [STX20](https://github.com/fess-v/stx20-standard) - 在 Stacks 上创建和共享数字工件的协议。

### 合约

- [CityCoin](https://github.com/citycoins/citycoin) - PoX lite 的实现，使用 STX 传输以比例概率铸造新币。
- [SWAPR](https://github.com/psq/swapr) - Stacks 2.0 和 Clarity 上类似 Uniswap 的实现。
- [FLEXR](https://github.com/psq/flexr) - Ampleforth 对 Stacks 的解释。
- [ClarityDAO](https://github.com/friedger/clarity-dao) - Moloch DAO 的清晰转换。
- [NFT Marketplace](https://github.com/friedger/clarity-marketplace/blob/master/contracts/market.clar) - 可交易资产市场的清晰智能合约。
- [StackStarter](https://github.com/MarvinJanssen/stackstarter/blob/master/contracts/stackstarter.clar) - 清晰的众筹智能合约。
- [Lightning Swaps](https://github.com/radicleart/clarity-rstack/blob/master/contracts/lightning-swaps-v1.clar) - 使用闪电网络进行防欺诈交换。
- [Election Voting](https://github.com/elbaruni/clarity-election/blob/master/contracts/election.clar) - 使用 Clarity 对候选人进行基本投票。
- [DualX](https://github.com/westridgeblockchain/dualX) - 为交易所实施 DeFi 生态系统的 Clarity 合约集合。
- [ExecutorDAO](https://github.com/MarvinJanssen/executor-dao) - 用于将 DAO 功能构建到智能合约中的 Clarity 框架。
- [Digital Will](https://github.com/LoRdSoban/Cryptonomers) - 有条件的资金转移。
- [MultiSafe](https://github.com/Trust-Machines/multisafe) - 用于管理 Stacks (STX) 和比特币 (BTC) 的共享加密库。
- [Charisma](https://github.com/pointblankdev/dungeon-master) - Stacks 区块链上社区运行的 memecoin DAO。

### 不可替代的代币

- [This is #1](https://www.thisisnumberone.com) - 第一个基于比特币和 Stacks 区块链的专业 NFT（[合约](https://explorer.hiro.so/txid/SP3QSAJQ4EA8WXEDSRRKMZZ29NH91VZ6C5X88FGZQ.thisisnumberone-v2?chain=mainnet)）。
- [Smart Contract GPT](https://github.com/Markeljan/stxgpt) - 聊天机器人经过训练可以创建 SIP-009 合同。

### 可替代代币

- [Nothing](https://nothingtoken.xyz/) - 一种不执行任何操作的可替代代币（[合约](https://explorer.hiro.so/txid/SP32AEEF6WW5Y0NMJ1S8SBSZDAY8R5J32NBZFPKKZ.nope?chain=mainnet)）。

### 堆叠

- [Stacking Pools](https://github.com/friedger/clarity-stacking-pools) - 用于堆叠池的 PoX 包装合约。
- [Stacks Pools](https://github.com/degen-lab/stacks-pools) - 去中心化的堆叠池。

## 应用程序开发

### 客户端库

- [Stacks.js](https://github.com/stx-labs/stacks.js) - Monorepo 用于与 Stacks 区块链交互的 JavaScript 库。
- [stacks.rs](https://github.com/52/stacks.rs) - 用于与 Stacks 区块链交互的 Rust 工具包。
- [stacks.py](https://github.com/rohitverma007/stackspy) - 用于与 Stacks 区块链交互的 Python 库。
- [go-stacks](https://github.com/cbadawi/go-stacks) - 用于与堆栈区块链交互的 Golang SDK。
- [x402 Stacks](https://www.x402stacks.xyz) - 用于在 Stacks 区块链上构建支付门控 API 的协议和 SDK。
- [Stacks Connect](https://github.com/stx-labs/connect) - 用于将应用程序与 Stacks 帐户连接的库。
- [Sign-In With Stacks](https://github.com/pradel/sign-in-with-stacks/) - 用于创建和验证 Sign-In with Stacks 消息的库。

### 命令行界面

- [@stacks/cli](https://github.com/stx-labs/stacks.js/tree/main/packages/cli) - 用于与身份验证、存储和事务交互的命令行界面。

### 索引和查询 API

- [Stacks API](https://www.hiro.so/stacks-api) - 托管 API 可直接与区块链交互，以查询信息、广播交易并扩展 Stacks 上的项目。
- [Quicknode](https://www.quicknode.com/chains/stx) - 托管 ednpoint，可使用 Quicknode 快速轻松地连接到 Stack。
- [Self-Hosted Render](https://github.com/stacksfoundation/render-stacks) - 一键部署工具可在 Render 上自行托管 Stacks 节点。
- [Self-Hosted Digital Ocean](https://marketplace.digitalocean.com/apps/stacks-blockchain) - 用于运行 Stacks 节点的 Digital Ocean Droplet。
- [Self-Hosted Docker](https://github.com/stacks-network/stacks-blockchain-docker) - 使用 Docker 运行自托管 Stacks 节点的工具。
- [Stacks Monitoring](https://github.com/alexlmiller/stacks-monitoring) - 堆栈节点的 Grafana 仪表板。

## 学习资源

### 文档

- [Official Stacks documentation](https://docs.stacks.co/) - 用于学习的文档和开发者教程
清晰度和开发 Stacks 应用程序。
- [Hiro documentation](https://docs.hiro.so/) - 文档主要针对开发人员。
- [Stacks 101](https://stacks101.com) - 社区策划的 STX 知识。

### 视频

- [Clarity 101](https://youtu.be/lXJutQqDq3w) - 了解 Clarity 设计原则的基础知识。
- [Developer Registry 101](https://www.crowdcast.io/e/clarity-program) - 了解如何从头开始构建 Clarity 智能合约。
- [How Clarity Prevents Common Smart Contract Vulnerabilities](https://www.youtube.com/watch?v=VYXhrwPsBws) - Clarity 安全原则的解释。
- [Proof of Transfer Whitepaper Reading with Muneeb Ali](https://www.youtube.com/watch?v=NY_eUrIcWOY&t=3s) - 作者的转移证明 (PoX) 白皮书概述。
- [Web3 for Bitcoin](https://www.crowdcast.io/e/web3-for-bitcoin/) - Stacks 概述、它解决的问题、它如何为比特币带来智能合约功能以及如何开始构建它。
- [Why Build on Stacks](https://www.youtube.com/watch?v=WaTMCremGwE) - 概述为什么 Web3 开发人员可能希望在 Stacks 上构建而不是其他区块链协议。

### 书面教程
- [Bitcoin Primer](https://docs.stacks.co/tutorials/bitcoin-primer/introduction) - 在比特币上构建全栈 Dapp 的介绍。
- [Understanding Stacks Post Conditions](https://dev.to/stacks/understanding-stacks-post-conditions-e65) - 了解和使用堆栈中的后置条件的指南。
- [Test-Driven Stacks Development with Clarinet](https://dev.to/stacks/test-driven-stacks-development-with-clarinet-2e4i) - 展示如何利用 Clarinet 进行测试和 TDD 的教程。
- [Build a DEX with Stacks](https://www.pointer.gg/tutorials/build-a-dex-with-stacks/56abb3a4-05c1-4608-b096-f82189e9f759) - 广泛介绍如何通过构建全栈去中心化交易所来使用 Stacks。
- [Build a Stacks app with Remix](https://micro-stacks.dev/guides/with-remix) - 如何使用 Remix JS 框架和 Micro-Stacks 创建服务器端渲染的 Stacks 应用程序。
- [Build a Stacks app with Next.js](https://micro-stacks.dev/guides/with-nextjs) - 与上面的 Remix 教程类似，本教程利用 Next.js 和 Micro-Stacks。
- [Creating a Voting Contract](https://www.clearness.dev/01-voting-clarity-smart-contract/01-getting-started) - 该系列由多部分组成，展示了如何使用 Clarity 创建简单的投票智能合约。
- [Building an NFT with Stacks and Clarity](https://blog.developerdao.com/building-an-nft-with-stacks-and-clarity) - 利用 SIP-009 标准使用 Clarity 创建 NFT。
- [Order Book Contract Walkthrough](https://byzantion.hiro.so/) - 使用 Clarity 构建的订单簿智能合约的演练。
- [NFT Tutorial](https://docs.hiro.so/tutorials/clarity-nft) - 创建清晰的 NFT。

### 书籍

- [Clarity of Mind](https://book.clarity-lang.org/) - 编写可预测的高效智能合约。 [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)

### 课程

- [Clarity Universe](https://clarity-lang.org/universe) - 全面的清晰度发展课程，既可以作为自定进度的课程，也可以作为为期 6 周的指导课程。

## 社区

- [Discord](https://discord.gg/zrvWsQC) - Stacks 生态系统不和谐。
- [Twitter](https://twitter.com/stacks) - Stacks 生态系统 Twitter。
- [YouTube](https://www.youtube.com/c/Blockstack) - Stacks 生态系统 YouTube。
- [Official Stacks Forum](https://forum.stacks.org/) - Stacks 社区论坛。
- [r/stacks](https://www.reddit.com/r/stacks) - 堆栈 subreddit。

## 贡献

我们欢迎社区对此列表做出贡献。请在贡献之前阅读[贡献指南](contributing.md)。
