<!--lint disable double-link-->
# 令人敬畏的宇宙 [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> 社区精选的与 Cosmos 生态系统相关的精彩项目列表

Cosmos SDK 是一个用于在 Go 中构建区块链应用程序的模块化框架。
Gaia 是 Cosmos Hub 的实现，是使用 Cosmos SDK 构建的。

**贡献：**
请阅读[贡献指南](./CONTRIBUTING.md)。感谢我们所有的[贡献者](https://github.com/cosmos/awesome/graphs/contributors)。

**免责声明：这个社区维护的存储库并不反映任何官方实体的观点。**

## 内容

* [核心组件](#core-components)
* [Documentation](#documentation)
* [客户端库](#client-libraries)
    * [Go](#go)
    * [JavaScript](#javascript)
    * [Python](#python)
    * [Rust](#rust)
* [区块浏览器](#block-explorers)
    * [视觉块浏览器](#visual-block-explorers)
    * [接线端子探索者](#terminal-block-explorers)
* [连锁登记处](#chain-registry)
* [Validators](#validators)
* [Cosmos SDK 模块](#cosmos-sdk-modules)
* [Monitoring](#monitoring)
* [Indexers](#indexers)
* [Frameworks](#frameworks)
* [虚拟机](#virtual-machines)
* [IBC](#ibc)
* [Testing](#testing)
* [Templates](#templates)
* [Tools](#tools)
    * [CLI](#cli)
    * [GUI](#gui)
    * [Bots](#bots)
* [节点操作](#node-operations)
    * [Utilities](#utilities)
* [Ecosystem](#ecosystem)
* [Wallets](#wallets)
* [Blogs](#blogs)
    * [Articles](#articles)
* [Related](#related)

## 核心组件

* [宇宙中心](https://github.com/cosmos/gaia)
<!-- -->
* [宇宙SDK](https://github.com/cosmos/cosmos-sdk/)
* [IBC 围棋](https://github.com/cosmos/ibc-go)
* [CometBFT](https://github.com/cometbft/cometbft)
* [CosmWasm](https://github.com/CosmWasm/cosmwasm)
* [CosmJS](https://github.com/cosmos/cosmjs)
<!-- -->
* [Protobuf](https://buf.build/cosmos)
* [IAVL](https://github.com/cosmos/iavl)
* [ICS23](https://github.com/cosmos/ics23)

## 文档

* [Cosmos 开发者门户](https://tutorials.cosmos.network)
* [跨链开发者学院](https://ida.interchain.io/)
* [宇宙SDK](https://docs.cosmos.network/)
* [IBC](https://ibc.cosmos.com/)
* [CometBFT](https://docs.cometbft.com/)
* [宇宙中心](https://hub.cosmos.network/)
* [CosmWasm](https://docs.cosmwasm.com/docs/1.0/)
* [Cosmology](https://cosmology.tech/learn)

## 客户端库

### 去

* [Ignite CLI](https://github.com/ignite/cli) - 用于在主权且安全的区块链上构建、启动和维护任何加密应用程序的一体化平台。通过 UI 快速引导新的 Cosmos SDK 区块链并支持创建新模块并方便地与现有 Cosmos SDK 模块配合使用。

### JavaScript

* [cosmos/cosmjs](https://github.com/cosmos/cosmjs) - Cosmos JavaScript 库。
* [telescope](https://github.com/osmosis-labs/telescope) - Typescript 库生成器构建在 CosmJS 之上。
* [chainapsis/cosmosjs](https://github.com/chainapsis/cosmosjs) - Chainapsis 签名和 API 库。
* [cosmos-client/cosmos-client-ts](https://github.com/cosmos-client/cosmos-client-ts) - Cosmos SDK 区块链的 JavaScript / TypeScript 客户端。
* [cosmology-tech/chain-registry](https://github.com/cosmology-tech/chain-registry) - 官方 Cosmos 链注册表的 npm 包。
* [strangelove-ventures/graz](https://github.com/strangelove-ventures/graz) - 用于与钱包、签名者、签名客户端等交互的 React hook 集合。
* [cosmology-tech/create-cosmos-app](https://github.com/cosmology-tech/create-cosmos-app) - 用于引导 Cosmos Web UI 的 npm 包。
* [cosmology-tech/cosmos-kit](https://github.com/cosmology-tech/cosmos-kit) - Cosmos 的钱包连接器。
* [nabla-studio/quirks](https://github.com/nabla-studio/quirks) - 适用于 Cosmos dApp 的通用钱包适配器，可在移动设备和浏览器上运行。
* [toschdev/bip44](https://github.com/toschdev/cosmos-bip44) - JavaScript 中的 Cosmos BIP44 实现用于开发和教育学习。

### 蟒蛇

* [cosmpy](https://github.com/fetchai/cosmpy) - 一个基于 Cosmos SDK 与区块链交互的 Python 客户端库。
* [pyCosmicWrap](https://github.com/ChihuahuaChain/pyCosmicWrap/) - 围绕 Cosmos API/RPC 的 python3 包装器。
* [mospy](https://github.com/ctrl-Felix/mospy) - 一个 Python 库，用于为基于 Cosmos SDK 的硬币创建和签署交易。
* [cosmospy-protobuf](https://github.com/ctrl-Felix/cosmospy-protobuf) - 包含所有已编译的 protobuf 文件的 Python 库（对于 grpc 非常有用）。
* [fx-py-sdk](https://github.com/functionx/fx-py-sdk) - Cosmos Python 客户端库。

### 铁锈

* [CosmWasm/cosmwasm](https://github.com/CosmWasm/cosmwasm) - Cosmos SDK 的 WebAssembly 智能合约。
* [iqlusioninc/stdtx](https://github.com/iqlusioninc/crates) - 来自 iqlusion 的开源 Rust 箱的集合。
* [peggyjv/ocular](https://github.com/peggyjv/ocular) - Cosmos SDK 链的客户端库，专注于愉悦的用户体验。

## 区块浏览器

* [ATOMScan](https://atomscan.com)
* [Big Dipper](https://bigdipper.live) - [来源](https://github.com/forbole/big-dipper-2.0-cosmos)
* [IOBScan](https://ibc.iobscan.io/)
* [Mintscan](https://www.mintscan.io)
    * [Mintscan for Cosmos Hub 测试网](https://cosmoshub-testnet.mintscan.io/cosmoshub-testnet)
* [NG探索者](https://explorers.guru/)
* [Ping.pub](https://ping.pub) - [来源](https://github.com/ping-pub/explorer)
* [股份编号](https://stake.id)

### 视觉块浏览器

查看区块链间通信 (IBC) 传输活动。该地图追踪不同区块链（在 Cosmos Hub 中称为区域）之间的 IBC 交易，以显示有关整个 Cosmos 生态系统脉搏的准确聚合信息。

* [Map of Zones](https://mapofzones.com/?period=24) - [来源](https://github.com/mapofzones)
* [Mintscan](https://hub.mintscan.io) - Cosmostation 的跨链浏览器。

### 接线端子探索者

通过终端探索 Cosmos SDK 区块链。

* [gex](https://github.com/cosmos/gex) - GEX 终端内浏览器。
* [cshtop](https://github.com/gsk967/cshtop) - Cosmos htop ，在终端上阻止可视化工具。
* [pvtop](https://github.com/blockpane/pvtop) - 终端上的共识可视化工具。
* [tmtop](https://github.com/quokkastake/tmtop) - 受 pvtop 启发的类似 Htop 的共识可视化工具，允许显示升级信息，与消费者链和非 Cosmos 链合作等等。

## 连锁登记处

包含来自大多数 Cosmos 链的标准化元数据的注册表。

* [cosmos/chain-registry](https://github.com/cosmos/chain-registry/)
* [Cosmos directory](https://cosmos.directory) - [来源](https://github.com/eco-stake/cosmos-directory)
* [cosmology-tech/chain-registry](https://github.com/cosmology-tech/chain-registry) - 官方 Cosmos 链注册表的 npm 包。

## 验证者

流行的区块浏览器提供了活跃验证者的列表。查看验证器配置文件的最简单入口点是来自区块浏览器：

* [Mintscan 上的列表](https://www.mintscan.io/cosmos/validators)
* [ATOMScan 上的列表](https://atomscan.com/validators)
* [北斗星列表](https://cosmos.bigdipper.live/validators)
* [Kujira POD 上的列表](https://pod.kujira.app/cosmoshub-4)

选择验证器时的 DYOR。考虑将您的代币委托给前 20 名之外的验证者，以提高网络的去中心化程度。
这也是避免 0% 佣金验证器和交易所验证器的好做法。

## Cosmos SDK 模块

查找 Cosmos SDK 模块的准确列表的最佳位置是项目存储库：

* 有关生产级模块的列表，请参阅[模块列表](https://docs.cosmos.network/main/modules/)。
* 知名第三方模块列表请参见[Cosmod.xyz](https://cosmod.xyz)

## 监控
* [PANIC Monitoring and Alerting For Blockchains](https://github.com/SimplyVC/panic) - 适用于 Cosmos SDK、Substrate 和 Chainlink 节点的开源监控和警报解决方案。
* [Prometheus Exporter](https://github.com/node-a-team/Cosmos-IE) - Cosmos SDK 的集成 Prometheus 导出器。
* [Cosmos Chains Dashboard](https://github.com/zhangyelong/cosmos-dashboard) - 用于监控 Cosmos SDK 和基于 Tendermint 的区块链节点的 Grafana 仪表板。
* [Chain Pulse](https://github.com/informalsystems/chainpulse) - 使用 Prometheus 导出器监控中继 IBC 数据包。
* [missed-blocks-checker](https://github.com/QuokkaStake/missed-blocks-checker) - 监控多个 Cosmos 链上验证者丢失的区块，并将其通知发送到 Telegram。
* [Nodes Checker](https://t.me/NodesGuru_bot) - 在线检查您的节点状态，如果您的验证器节点出现问题，您会收到即时通知。
* [Cosmon](https://github.com/iqlusioninc/cosmon) - 适用于 Cosmos 和其他 Tendermint 应用程序的可观察性工具。
* [Tenderduty](https://github.com/blockpane/tenderduty) - Tendermint 链的综合监控工具。它的主要功能是在验证者丢失区块等情况时向验证者发出警报。
* [UpgradesWatchdog](https://github.com/ChihuahuaChain/UpgradesWatchdog) - SoftwareUpgradeProposal & GitHub 发布电报监控工具。
* [cosmos-node-exporter](https://github.com/QuokkaStake/cosmos-node-exporter.git) - Prometheus 导出器，用于抓取有关节点同步状态、Cosmovisor 升级和 GitHub 版本不匹配的数据，对于节点操作员和验证器非常有用。
* [cosmos-wallets-exporter](https://github.com/QuokkaStake/cosmos-wallets-exporter.git) - 一个 Prometheus 导出器，用于抓取钱包余额数据，如果您的钱包余额太低，可以收到通知。
* [cosmos-validators-exporter](https://github.com/QuokkaStake/cosmos-validators-exporter.git) - 一个 Prometheus 导出器，用于抓取有关验证器的数据（错过的区块、委托人数量、总质押金额、排名等）
* [cosmos-validator-monitoring-service(CVMS)](https://github.com/cosmostation/cvms) - Cosmos 应用链生态系统中验证者的集成监控系统。
* [cosmos-proposals-checker](https://github.com/QuokkaStake/cosmos-proposals-checker.git) - 如果您的钱包尚未对任何提案进行投票，则机器人会向您发送有关多个 Cosmos 链的通知。
* [cosmos-transactions-bot](https://github.com/QuokkaStake/cosmos-transactions-bot.git) - 一个机器人，可以向您发送有关您想要在多个 Cosmos 链上订阅的任何交易的通知。

## 索引器

* [Cosmscan](https://github.com/cosmscan/cosmscan-go) - Cosmos 链的索引器引擎。
* [interchain-indexer](https://github.com/Reecepbcups/interchain-indexer) - Python 中的 Cosmos 区块链索引器。
* [Cosmos Indexer](https://github.com/DefiantLabs/cosmos-indexer) - Go 中具有关联性和直接数据库索引的通用数据库模式索引器。
* [BDJuno](https://github.com/forbole/bdjuno) - 从 RPC 和 gRPC 端点查询的所有链数据都存储在 PostgreSQL 数据库中，然后可以在该数据库上使用 Hasura 创建 GraphQL API。

## 框架

* [Cosmos SDK](https://github.com/cosmos/cosmos-sdk/) - 用 Go 构建高价值公共区块链的框架。
* [Orga](https://github.com/nomic-io/orga) - Rust 中状态机转换的 ABCI 框架。
* [CosmosSwift](https://github.com/CosmosSwift) - 基于 Tendermint 共识，在 Swift 中构建区块链应用程序。
* [ABCI-RS](https://github.com/devashishdxt/abci-rs) - 用于创建 ABCI 应用程序的 Rust 箱。
* [CosmRS](https://github.com/cosmos/cosmos-rust/tree/main/cosmrs) - 在 Rust 中构建 Cosmos 区块链应用程序的框架。

## 虚拟机

在 Cosmos SDK 中运行的虚拟机的模块或框架

* [Agoric SDK](https://github.com/Agoric/agoric-sdk) - Agoric JavaScript 智能合约平台。
* [CosmWasm](https://github.com/CosmWasm/cosmwasm) - WASM 虚拟机和 Rust 智能合约。
* [Ethermint](https://github.com/evmos/ethermint) - 以太坊虚拟机。
* [Polaris](https://github.com/berachain/polaris) - 模块化以太坊虚拟机。

## 中型散装容器

* [IBCprotocol.dev](https://ibcprotocol.dev/) - IBC 协议网站。
* [Interchain Standards](https://github.com/cosmos/ibc/) - Cosmos 网络和链间生态系统的链间标准 (ICS)。
* [cosmos/ibc-go](https://github.com/cosmos/ibc-go) - Go 中的区块链间通信协议（IBC）实现。
* [cosmos/ibc-rs](https://github.com/cosmos/ibc-rs) - Rust 实现了区块链间通信 (IBC) 协议。
* [interchaintest](https://github.com/strangelove-ventures/interchaintest) - IBC 链的端到端测试框架。
* [cosmos/relayer](https://github.com/cosmos/relayer) - Go 中的 IBC 中继器。
* [informalsystems/hermes](https://github.com/informalsystems/hermes) - Rust 中的 IBC 中继器。
* [confio/ts-relayer](https://github.com/confio/ts-relayer) - TypeScript 中的 IBC 中继器。
* [local-interchain](https://github.com/Reecepbcups/local-interchain) - 在任何操作系统上快速启动本地 IBC 开发环境。
* [IBC-escrow-auditor](https://github.com/Cordtus/ibc-escrow) - 用于根据交易对手链上的 IBC 锁定账户检查和报告链上代币金额的独立工具。

## 测试

* [interchaintest](https://github.com/strangelove-ventures/interchaintest) - IBC 链的端到端测试框架。
* [atomkraft](https://github.com/informalsystems/atomkraft-cosmos) - Cosmos SDK 区块链端到端测试框架。
* [python-iavl](https://github.com/crypto-com/python-iavl) - 用Python实现的IAVL检查工具。
* [cosmos-sdk-codeql](https://github.com/crypto-com/cosmos-sdk-codeql) - CodeQL 查询常见 Cosmos SDK 错误。
* [tm-load-test](https://github.com/informalsystems/tm-load-test) - CometBFT 负载测试应用程序。
* [cosmosloadtester](https://github.com/orijtech/cosmosloadtester) - Cosmos SDK 区块链的负载测试器。
* [CometMock](https://github.com/informalsystems/CometMock) - 在端到端测试中替代 CometBFT。
* [quint](https://github.com/informalsystems/quint) - 具有令人愉快的工具的可执行规范语言。
* [apalache](https://github.com/informalsystems/apalache) - APALACHE：TLA+ 和 Quint 的符号模型检查器。

## 模板

可帮助您开始构建 Cosmos SDK 区块链的模板。

* [ignite](https://github.com/cli) - 通过 UI 快速引导新的 Cosmos SDK 区块链并支持创建新模块并方便地与现有 Cosmos SDK 模块配合使用。
* [cosmosregistry/example](https://github.com/cosmosregistry/example) - Cosmos SDK 模块的模板和示例存储库。
* [cosmosregistry/chain-minimal](https://github.com/cosmosregistry/chain-minimal) - 最小 Cosmos SDK 区块链的模板和示例。
* [spawn](https://github.com/rollchains/spawn) - 通过测试、GitHub 集成和简单的即时测试网生成新的 Cosmos SDK 区块链。

## 工具

### 命令行界面

* [tmkms](https://github.com/iqlusioninc/tmkms) - Tendermint 验证者的密钥管理系统。
* [cosmosvisor](https://github.com/cosmos/cosmos-sdk/tree/main/cosmovisor#readme) - 自动执行 Cosmos SDK 应用程序二进制升级。
* [cosmosvanity](https://github.com/hukkinj1/cosmosvanity) - 用于生成 Cosmos 虚荣地址的 CLI 工具。
* [findaccount](https://github.com/blockpane/findaccount) - 帮助识别具有相同地址的多个 Cosmos 链上是否存在帐户。
* [lens](https://github.com/strangelove-ventures/lens) - CLI 工具可与任何支持核心 Cosmos-SDK 模块的 Cosmos 链进行交互。
* [cosmology](https://github.com/cosmology-tech/cosmology) - 用于进行加密货币交易、加入流动性池以及在 Osmosis 上进行权益奖励的 CLI 工具。
* [multisig](https://github.com/informalsystems/multisig) - 用于管理 Cosmos SDK 链上多重签名帐户的 CLI 工具。
* [cosmos-genesis-tinkerer](https://github.com/hyphacoop/cosmos-genesis-tinkerer) - 用于修改 Cosmos 创世文件的 CLI 工具。
* [airdrop-tools](https://github.com/Reecepbcups/airdrop-tools) - CLI 脚本可帮助分发多种格式的各种令牌。
* [cosmos.nix](https://github.com/informalsystems/cosmos.nix) - [Nix](https://nixos.org/) 支持 Cosmos 和 CosmWasm。

### 图形用户界面

* [REStake](https://restake.app) - 使用 Authz 的 Cosmos 区块链自动复合应用程序（[来源](https://github.com/eco-stake/restake)）。
* [Cosmfaucet](https://github.com/scalalang2/cosmfaucet) - 基于 Cosmos 的区块链的自托管水龙头服务。
* [Cosmos Notifier](https://cosmos-notifier.decrypto.online) - Telegram 和 Discord 的治理通知工具（[来源](https://github.com/shifty11/cosmos-notifier)）。
* [Skip:Go](https://go.skip.build) - IBC 代币传输、自动交换和多跳路由（[来源](https://github.com/skip-mev/skip-go-app)）。

### 机器人

* [Cosmos Discord Faucet](https://github.com/0x4139/cosmos-discord-faucet) - 用于 Cosmos SDK 区块链的可配置 Discord 水龙头。
* [Cosmos Discord Bot](https://github.com/okp4/discord-bot) - 适用于 Cosmos SDK 区块链的通用 Discord 机器人。
* [cosmos-proposals-checker](https://github.com/QuokkaStake/cosmos-proposals-checker.git) - 如果您的钱包没有对多个 Cosmos SDK 链上的提案进行投票，机器人会通知您。
* [cosmos-transactions-bot](https://github.com/QuokkaStake/cosmos-transactions-bot.git) - 获取有关在多个 Cosmos SDK 链上与您想要的过滤器匹配的交易的通知。
* [cosmos-balance-bot](https://github.com/Reecepbcups/cosmos-balance-bot) - 按设定的时间间隔获取有关多个 Cosmos SDK 链上的钱包余额的通知。
* [validator-stats-notifications](https://github.com/Reecepbcups/validator-stats-notifs) - Discord 公告，包括排名、一段时间内的授权以及独特的授权人。
* [Secret Stashh NFT Bot](https://github.com/Reecepbcups/stashh-bot) - 一个 Discord 机器人，用于获取 Secret Network NFT 系列的销售、拍卖和购买通知。
* [DAODAO Treasury Bot](https://github.com/Reecepbcups/dao-treasury-bot) - 一个不和谐的机器人，可以跟上 DAO 的国库法币价值。
* [Cosmos Price Bot](https://github.com/Reecepbcups/cosmos-price-bot) - 一个不和谐的机器人，通过 DEX 为任何 Cosmos 代币的美元价格起昵称。

## 节点操作

### 公用事业

* [Cosmos Cache](https://github.com/Reecepbcups/cosmos-endpoint-cache) - 通过在预定义的时间集（正则表达式）内缓存响应来优化 Cosmos 查询。
* [cosmos-operator](https://github.com/strangelove-ventures/cosmos-operator) - Cosmos Operator 是一个用于管理 Cosmos 节点的 Kubernetes Operator。
* [Wallet-generator](https://github.com/Cordtus/wallet_generator) - 根据助记词手动生成密钥对 + 钱包地址，根据 privkey 手动生成 pubkey + 钱包地址，或者根据 pubkey 生成钱包地址。接受任意 HDpath（包括 cointype）

## 生态系统

使用 Cosmos SDK 构建的最新项目列表可以在 [Cosmos 目录](https://cosmos.directory) 上找到。

## 钱包

支持 Cosmos 链的钱包列表是 <https://cosmos.network/ecosystem/wallets>。

## 博客

随着生态系统的发展，内容也在不断发展。 DYOR 并关注您感兴趣的项目。

**免责声明：这个社区维护的存储库并不反映任何官方实体的观点。**

* [什么是宇宙？](https://cosmos.network/intro/)
* [宇宙博客](https://blog.cosmos.network/)
* [跨链基金会博客](https://interchain-io.medium.com)

### 文章

* [Cosmos 开发系列：Cosmos 区块链升级](https://zerofruit.medium.com/cosmos-dev-series-cosmos-sdk-based-blockchain-upgrade-b5e99181554c)
* [硬化导轨](https://cyber.orijtech.com/scsec/cosmos-hardening)
* [如何将您的前端连接到 Cosmos 区块链](https://dev.to/kikiding/how-to-connect-your-frontend-to-cosmos-blockchain-5fcn)
* [（并非如此）Smart Cosmos，常见 Cosmos 应用程序漏洞的示例](https://github.com/crytic/building-secure-contracts/tree/master/not-so-smart-contracts/cosmos)
* [Go 编码指南](https://cyber.orijtech.com/scsec/cosmos-go-coding-guide)
* [Cosmos 安全手册 - 第 1 部分](https://www.faulttolerant.xyz/2024-01-16-cosmos-security-1)

## 相关

* [很棒的 CosmWasm](https://github.com/InterWasm/cw-awesome)
