很棒的比特币
===============
为软件开发人员精心挑选的比特币服务和工具列表
[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

## 内容清单

- [Utilities](#utilities)
- [区块链 API 和 Web 服务](#blockchain-api-and-web-services)
- [钱包API](#wallets-api)
- [开源钱包](#open-source-wallets)
- [区块链探索者](#blockchain-explorers)
- [C 语言库](#c-libraries)
- [C++ 库](#c-libraries-1)
- [JavaScript 库](#javascript-libraries)
- [PHP 库](#php-libraries)
- [红宝石库](#ruby-libraries)
- [Python 库](#python-libraries)
- [Java 库](#java-libraries)
- [斯卡拉库](#scala-libraries)
- [斯威夫特库](#swift-libraries)
- [.Net 库](#net-libraries)
- [哈斯克尔图书馆](#haskell-libraries)
- [Playgrounds](#playgrounds)
- [区块链转储](#blockchain-dump)
- [全节点](#full-nodes)
- [Read](#read)
- [Course](#course)
- [其他资源](#additional-resources)


## 公用事业
* [Nigiri](https://github.com/vulpemventures/nigiri/) - CLI 可与 Electrs 和 Esplora 一起快速启动比特币注册测试框。包括水龙头和推送命令。
* [hal](https://github.com/stevenroose/hal) - 比特币 CLI 瑞士军刀（基于 rust-bitcoin）。
* [BitKey](https://bitkey.io) - 用于气隙交易的实时 USB 和比特币瑞士军刀。
* [PaperVault](https://github.com/boazeb/papervault) - 使用 AES-256-GCM 和 Shamir 的秘密共享进行离线纸质秘密存储。使用阈值密钥分割创建种子短语的可打印加密备份。
* [Pycoin](https://github.com/richardkiss/pycoin) - 基于 Python 的比特币和替代币实用程序库。
* [bx](https://github.com/libbitcoin/libbitcoin-explorer) - 比特币命令行工具。
* [Deadhand Protocol](https://deadhandprotocol.com) - Dead man 使用 Shamir 的秘密共享来保护种子短语并确保继承，转而使用加密货币。
* [txwatcher](https://github.com/tsileo/txwatcher) - 一个 Python 实用程序，可让您通过 Blockchain Websocket API 监控比特币地址并执行自定义回调。
* [hellobitcoin](https://github.com/prettymuchbryce/hellobitcoin) - 一组简单的程序，可以生成比特币钱包、创建和签署交易以及通过比特币网络发送交易。
* [采矿可视化](https://yogh.io/landing/)
* [HD Wallet Scanner](https://github.com/alexk111/HD-Wallet-Scanner) - 查找您的 Bitcoin HD 钱包中所有已使用的地址，绕过间隙限制。
* [`<qr-code>`](https://github.com/bitjson/qr-code) - 一个无框架、无依赖项、可定制、可动画、基于 SVG 的“<qr-code>” Web 组件。
* [Bitcoin Serverless Donations](https://github.com/tombennet/bitcoin-serverless-donations) - 自我托管的无服务器捐赠小部件，具有源自 XPUB 的地址轮换。
* [BTC Tooling](https://github.com/douvy/btc-tooling) - 比特币仪表板包含实时价格数据、图表、订单簿、市场摘要、Twitter/X 见解和减半倒计时数据。 [现场演示](https://www.btctooling.com/)
* [Chartscout](https://chartscout.io) - 跨多个交易所的实时 BTC 图表模式检测和交易警报。
* [Bitcoin Bottom Score](https://bitcoinbottom.app) - 实时比特币周期底部概率跟踪器。将 25 个链上和宏观信号（MVRV Z-Score、Puell Multiple、Hash Ribbon、ETF 流）聚合为每日 P（底部）分数。免费，每日更新两次。
* [BTC Airgap Bridge](https://github.com/paranoid-qrypto/btc-airgap-bridge) - 100% 客户端工具，用于广播来自气隙钱包的签名比特币交易。
* [SuperScalar MCP](https://github.com/8144225309/superscalar-mcp) - 用于 SuperScalar 比特币闪电通道工厂的 MCP 服务器 — 在一个共享 UTXO 中装载 N 个用户，无需软分叉。
* [Lightning Memory](https://github.com/singularityjason/lightning-memory) - 比特币/闪电经济中人工智能代理的开源内存层。 L402支付网关、供应商信誉、支出异常检测。
* [CryptoCalk](https://cryptocalk.com) - 比特币盈利能力和链上计算器：ASIC/GPU 挖矿投资回报率、哈希率转换器、减半倒计时、Mayer 倍数、库存流量 (S2F)、彩虹图、利润/亏损、DCA 模拟器、税收估算器、清算价格。客户端，无需注册，提供 6 种语言版本。
* [dont-trust-verify](https://dont-trust-verify.com) - 仅限比特币的客户端工具和自我托管教育：22 个计算器、验证器和解码器（BIP-39 验证器、tx-stuck 检查器、费用估算器、钱包安装程序 SHA-256 验证器、自我托管分数测验），以及主要来源指南和硬件钱包评论。无需注册，无需跟踪，EN + TH。

## 区块链 API 和 Web 服务
* [3xpl.com](https://3xpl.com/) - 最快的无广告通用区块浏览器。
* [Bitquery.io](https://bitquery.io/) - Bitquery 提供区块链数据，为 40 多个链提供实时流 API、NFT API 和资金流调查工具。
* [block.io](https://block.io)
* [blockchair.com](https://blockchair.com/) - 通用区块链浏览器和搜索引擎。
* [BlockCypher](https://www.blockcypher.com)
* [Esplora](https://github.com/Blockstream/esplora) - 自托管区块链浏览器。
* [Insight](https://insight.is)
* [Chain.com](https://chain.com)
* [Coinbase 钱包](https://wallet.coinbase.com/)
* [Chainradar API](https://github.com/yasaricli/chainradar-api) - Chainradar 的区块链浏览器 API。
* [一次性地址](https://github.com/alexk111/One-Time-Address) 一种更好的方式来分享您的比特币地址。
* [Cryptocurrency Alerting](https://cryptocurrencyalerting.com/blockchain-alerts.html) - 比特币钱包监控和区块链警报。
* [BTC Connect](https://developers.particle.network/reference/introduction-to-btc-connect) - 统一的比特币第一层和第二层钱包连接和账户抽象。
* [Tatum](https://tatum.io/blockchain-api) - 用于构建Web3应用程序的区块链开发平台。 Web3 开发人员首选的区块链数据 API。
* [mempool.space](https://mempool.space/docs/api/rest) - 开源和自托管 REST、WebSocket 和 Electrum RPC API
* [Bitview](https://bitview.space/) - 开源比特币核心数据提取器和可视化工具（又名 FOSS Glassnode）
* [Maestro](https://www.gomaestro.org/) - 高性能比特币 RPC 和 UTXO 索引器 API，为具有实时区块链数据、内存池监控和事件通知的应用程序提供支持。

## 市场数据API
* [CoinGapRadar](https://coingapradar.com) - 跨 9 个国家/地区的实时加密货币溢价跟踪器。监控泡菜溢价和区域价格差距。免费，无需注册。
* [CoinMetrics.io](https://docs.coinmetrics.io/) JSON REST API（免费和付费）可访问市场数据。还提供 CSV 数据文件下载。
* [CoinPaprika](https://api.coinpaprika.com) 免费的加密货币市场数据API。 12,000 多个代币、350 多个交易所、股票行情、OHLCV、历史价格。免费套餐没有 API 密钥。
* [Messari.io](https://messari.io/api) JSON REST API（免费和付费），可访问市场数据、新闻、指标、概况等。
* [PreReason](https://www.prereason.com) - 通过 REST API 预先分析比特币市场简报。涵盖 BTC 价格、算力、难度、挖矿生产成本、持有的国债（30 家上市公司）以及影响比特币走势的宏观信号（美联储资产负债表、M2、国债收益率）。返回趋势方向、置信度分数和状态分类，而不是原始数字。提供免费套餐。

## 钱包API
* [BitGo](https://developers.bitgo.com)
* [Coinbase](https://developers.coinbase.com)
* [Blockchain.com](https://www.blockchain.com/api)
* [BIP32](http://bip32.org)
* [walletOS](https://www.pinestreetlabs.com/walletos/)

## 开源钱包
* [蓝色钱包](https://bluewallet.io/)
* [BitPay 共同支付](https://copay.io/)
* [Coinb.in](https://coinb.in)
* [零钱包](https://coin.space/)
* [Electrum](https://electrum.org/)
* [Green](https://blockstream.com/green/)
* [Sparrow](https://sparrowwallet.com/)
* [芥末钱包](https://wasabiwallet.io/)

## 隐私项目
* [Joinmarket](https://github.com/JoinMarket-Org/joinmarket-clientserver) - 去中心化 CoinJoin 实施
* [Jam](https://jamapp.org/) - Joinmarket 的用户友好前端

## 区块链探索者
* [3xpl.com](https://3xpl.com/bitcoin) - 最快的无广告通用区块浏览器。
* [Chain.so](http://chain.so)
* [Blockchain.com](https://blockchain.com)
* [Blockchair.com](https://blockchair.com/bitcoin) - 通用区块链浏览器和搜索引擎。
* [Blockstream.info](https://blockstream.info) - 具有 API（主网、测试网和 Liquid）的区块链浏览器。
* [比特币交易浏览器](https://github.com/JornC/bitcoin-transaction-explorer)
* [Blockexplorer.com](https://blockexplorer.com)
* [Smartbit](https://www.smartbit.com.au)
* [mempool.space](https://mempool.space/) - 开源、自托管区块链、内存池和闪电网络浏览器

## C 语言库
* [libsecp256k1](https://github.com/bitcoin-core/secp256k1)
* [UltrafastSecp256k1](https://github.com/shrec/UltrafastSecp256k1) - 高性能“secp256k1”引擎，具有稳定的 C ABI、CPU、CUDA、OpenCL、嵌入式和 WebAssembly 目标。

## C++ 库
* [Libbitcoin](https://libbitcoin.org/)
* [Libbitcoin](https://libbitcoin.info/) - 一组用于构建比特币应用程序的跨平台 C++ 库
* [libwally-core](https://github.com/ElementsProject/libwally-core)

## JavaScript 库
* [很棒的 CryptoCoinJS](https://github.com/cryptocoinjs/awesome-cryptocoinjs)
* [比特核心库](https://github.com/bitpay/bitcore/tree/v8.0.0/packages/bitcore-lib)
* [Bitcoinjs-lib](https://github.com/bitcoinjs/bitcoinjs-lib)
* [Cryptocoin](http://cryptocoinjs.com/#modules)
* [BlockTrail SDK NodeJS](https://github.com/blocktrail/blocktrail-sdk-nodejs)
* [bcoin](https://github.com/bcoin-org/bcoin) - 适用于 Node.js 和浏览器的 Javascript 比特币库。
* [Libauth](https://libauth.org/) - 一个轻量级、零依赖的 JavaScript/TypeScript 比特币库。
* [noble-curves](https://github.com/paulmillr/noble-curves) - 纯打字稿中 secp256k1 + schnorr 的审计实现
* [noble-secp256k1](https://github.com/paulmillr/noble-secp256k1) - secp256k1 的替代实现：gzip 后大小仅为 4KB；很多评论，对于学习算法如何工作非常有价值
* [scure-btc-signer](https://github.com/paulmillr/scure-btc-signer) - 用于创建、签名和解码比特币交易的经过审计的最小库。使用 Schnorr、Taproot、UTXO 和 PSBT。
* [bitcoin-sdk-js](https://github.com/ChrisCho-H/bitcoin-sdk-js) - 适用于 NodeJS、浏览器和移动设备的比特币 TypeScript/JavaScript 库。 Segwit 和 Taproot 支持。
* [toll-booth](https://github.com/forgesworn/toll-booth) - Node.js 的 HTTP 402 支付中间件；通过五个后端选项来控制闪电网络、Cashu 或稳定币支付背后的任何 API。
## PHP 库
* [PHP-OP_RETURN](https://github.com/coinspark/php-OP_RETURN)
* [BlockTrail PHP SDK](https://github.com/blocktrail/blocktrail-sdk-php)

## 红宝石库
* [Bitcoin-ruby](https://github.com/lian/bitcoin-ruby)
* [bitcoinrb](https://github.com/chaintope/bitcoinrb) - Ruby 比特币库，包括脚本解释器。
* [bech32rb](https://github.com/azuchi/bech32rb) - Bech32 和 Bech32m 编码/解码库。
* [bip-schnorrrb](https://github.com/chaintope/bip-schnorrrb) - 比特币的 Schnorr 签名库。

## Rust 库
* [Bitcoin Dev Kit (BDK)](https://bitcoindevkit.org/) - 使用BDK，您可以无缝构建跨平台移动钱包
* [Rust Bitcoin](https://github.com/rust-bitcoin/rust-bitcoin) - 支持数据结构和网络消息的反序列化、解析和执行。
* [Lightning Dev Kit (LDK)](https://lightningdevkit.org/) - 完整的 Lightning 实施打包为 SDK
* [Bithoven](https://github.com/ChrisCho-H/bithoven) - 比特币智能合约的高级命令式语言，具有 LR(1) 解析器，具有静态分析功能，可确保编译时安全。

## Python 库
* [BlockTrail SDK Python](https://github.com/blocktrail/blocktrail-sdk-python)
* [btctxstore](https://github.com/F483/btctxstore) - 使用 OP_RETURN 存储/检索比特币交易信息的简单库。
* [pybitcointools](https://github.com/vbuterin/pybitcointools) - 来自 Vitalik Buterin 的用于比特币签名和交易的 Python 库。项目停止。
* [pycoin](https://github.com/richardkiss/pycoin) - 用于比特币密钥、签名、交易的 Python 库。包括完整的虚拟机实现以及用于操作密钥 (ku) 和事务 (tx) 的工具。
* [bitcoin_tools](https://github.com/sr-gi/bitcoin_tools) - 用于构建和分析交易和脚本（标准和自定义）的 Python 库。附带 UTXO 集分析工具。包括几个示例和详尽的文档。
* [pybtc](https://github.com/mohanson/pybtc) - Python BTC是一个实验项目，旨在为常见的BTC操作提供人性化的界面。

## Java 库
> 请注意，您还可以在 Java 中使用 [Scala 库](#scala-libraries)。
* [BitcoinJ](https://bitcoinj.github.io)
* [XChange](https://github.com/knowm/XChange) - 库提供了一个简单且一致的 API，用于与 50 多个比特币货币交易所进行交互。
* [Bitcoin Spring Boot Starter](https://github.com/theborakompanioni/bitcoin-spring-boot-starter) - Spring Boot 应用程序的比特币集成。
* [bech32](https://github.com/NostrGameEngine/bech32) - Bech32 和 Bech32m 编码/解码库。

## Scala 库
> 请注意，您还可以在 Scala 中使用 [Java 库](#java-libraries)。
* [Bitcoin-S](https://bitcoin-s.org) - 用于比特币应用程序的 Scala/JVM 工具包，包括比特币数据结构、交易签名、强类型“bitcoind”/Eclair RPC 客户端等。

## 斯威夫特库
* [secp256k1.swift](https://github.com/GigaBitcoin/secp256k1.swift) - 适用于 secp256k1 应用程序的 Swift 软件包，包括椭圆曲线操作、Schnorr、ZKP 等适用于比特币的操作。

## .Net 库
* [NBitcoin](https://github.com/MetacoSA/NBitcoin) - 适用于 .NET 框架的综合比特币库。
* [BitcoinLib](https://github.com/cryptean/bitcoinlib) - 最完整、最新、经过实战考验的 .net 库和 C# 中比特币和山寨币的 RPC 包装器。

## 哈斯克尔图书馆
* [Haskoin-core](https://github.com/haskoin/haskoin-core) - Haskoin Core 是一个用 Haskell 编写的比特币和比特币现金函数库。

## 游乐场
* [脚本游乐场](https://www.crmarsh.com/script-playground/)
* [Bitcoin IDE](https://github.com/siminchen/bitcoinIDE) - 傻瓜比特币脚本。
* [脚本调试器](https://github.com/kallewoof/btcdeb)
* [比特核游乐场](https://bitcore.io/playground/)
* [助记码生成器](https://iancoleman.io/bip39/)
* [blockchain-demo](https://github.com/anders94/blockchain-demo/) - 基于网络的区块链概念演示。
* [Bitcoin Script Debugger](https://github.com/liuhongchao/bitcoin4s) - 可视化真实交易的比特币脚本执行。
* [Bitauth IDE](https://ide.bitauth.com/) - 比特币合约的交互式开发环境。
* [ChainQuery Bitcoin RPC](https://chainquery.com) - 运行选择的比特币 RPC API 调用并在浏览器中阅读完整的 RPC 文档。
* [Bithoven IDE](https://bithoven-lang.github.io/bithoven/ide/) - Bithoven 的 Web IDE，比特币智能合约的高级命令式语言。

## 区块链转储
* [BitcoinDatabaseGenerator](https://github.com/ladimolnar/BitcoinDatabaseGenerator) - 一种高性能数据传输工具，可用于将数据从 Bitcoin Core 区块链文件复制到 SQL Server 数据库。
* [Blockparser+SQL](https://github.com/mcdee/blockparser) - 快速、快速和肮脏的比特币区块链解析器。
* [BitcoinABE](https://github.com/bitcoin-abe/bitcoin-abe) - Abe：比特币和类似货币的区块浏览器。
* [Chaingraph](https://github.com/bitauth/chaingraph/) - 多节点区块链索引器和 GraphQL API。

## 全节点
* [btcd](https://github.com/btcsuite/btcd/) - 自 2013 年起基于 Go 的全节点。
* [Bitcoin-ruby-node](https://github.com/mhanne/bitcoin-ruby-node) - 基于比特币-红宝石-区块链的比特币节点。
* [Fullnode](https://github.com/moneybutton/yours-bitcoin) - 比特币的 JavaScript 实现。
* [Bitcore Node](https://github.com/bitpay/bitcore-node) - bitcoind 通过 BitPay 链接到 node.js。
* [Bitcore](https://github.com/bitpay/bitcore) - 以前只是一个 Nodejs 库，现在是一个完整的节点。
* [Bitcoin Core](https://bitcoincore.org/) - C++ 中原始比特币实现的直接后代

## 阅读
* [比特币核心开发简介](https://medium.com/bitcoin-tech-talk/a-gentle-introduction-to-bitcoin-core-development-fdc95eaee6b8)
* [掌握比特币](https://github.com/bitcoinbook/bitcoinbook)
* [Grokking Bitcoin](https://www.manning.com/books/grokking-bitcoin) - 一本深入的技术书籍，插图丰富。
* [比特币堆栈交换](https://bitcoin.stackexchange.com)
* [椭圆曲线密码学简介](https://andrea.corbellini.name/2015/05/17/elliptic-curve-cryptography-a-gentle-introduction/)。
* [使用 BitcoinJS 和 Bitcoin Core CLI 进行比特币编程](https://github.com/bitcoin-studio/Bitcoin-Programming-with-BitcoinJS)。
* [比特币协议开发课程 - Chaincode Labs](https://github.com/chaincodelabs/bitcoin-curriculum)。
* [闪电网络协议开发课程 - Chaincode Labs](https://github.com/chaincodelabs/lightning-curriculum)。
* [btcinformation.org / Developer Documentation](https://btcinformation.org/en/developer-documentation) - 为开发人员查找有用的资源、指南和参考材料。

## 课程
* [比特币和加密货币](http://bitcoinbook.cs.princeton.edu/)。

## 其他资源
* [@lopp / Bitcoin Developers](https://twitter.com/lopp/lists/bitcoin-developers) - 具有比特币实施或应用程序经验的软件开发人员。
* [@lopp / Lightning Developers](https://twitter.com/i/lists/981976067551490048) - 具有 LN 实施/应用程序经验的软件开发人员。
* [实用比特币信息 - Google 表格](https://docs.google.com/spreadsheets/d/1Z3Ofa4P8097VWV70Z_bMqIMladngvm-Ck24ot9TDNmw/)。
* [比特币发展简史...](https://www.youtube.com/watch?v=ZfFNce6CVsE)
* [bitcoin-resources.com](https://bitcoin-resources.com/) 比特币资源元列表，从书籍、文章到播客。
* [Jameson Lopp 比特币资源列表](https://www.lopp.net/bitcoin-information.html) 由 J. Lopp 精心策划的非常详细的比特币资源列表和元列表
* [Svrgnty.com：一切比特币](https://svrgnty.com/) 最佳比特币资源的精选列表。
* [River Learn](https://river.com/learn) 一系列教育资源，可帮助您了解比特币基础知识、投资、技术等。
* [BitcoinCompanies](https://bitcoincompanies.co/) - 企业比特币金库地图和排行榜，其中包含已声明与已验证的持有量。
* [Learn me a Bitcoin - Greg Walker](https://learnmeabitcoin.com/) - 为比特币开发者提供丰富的学习资源
* [Bennet.org](https://bennet.org/) - 比特币爱好者的交互式技术指南。
* [Knowing Bitcoin](https://knowingbitcoin.com/) - 全面的比特币教育，包含 214 多个有关闪电网络、钱包、安全、隐私和节点的深入指南。
* [Bitcoin.diy](https://bitcoin.diy) - 仅限比特币的教育和硬件钱包评论，专注于初学者和中级用户的自我托管。
* [Bitcoin Institute](https://bitcoin-institute.pages.dev) - 中本聪主要来源的双语（EN/JP）档案：论坛帖子、电子邮件和邮件列表消息，每个都链接到其原始来源。
---

受到 [awesome](https://github.com/sindresorhus/awesome) 列表的启发。
由 BlockchainU 研究员创建。

---

### 许可证

[![CC0](https://i.creativecommons.org/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

在法律允许的范围内，[Igor Barinov](https://github.com/igorbarinov/) 已放弃本作品的所有版权以及相关或邻接权。
