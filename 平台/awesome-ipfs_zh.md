# 很棒的IPFS [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

这是与 IPFS 相关的精彩项目、应用程序、工具和服务的社区列表。

要提交您的项目，请阅读[内容政策](https://github.com/ipfs/awesome-ipfs/blob/main/CONTRIBUTING.md#content-policy)，并[**提交 PR**](https://github.com/ipfs/awesome-ipfs/edit/main/README.md)

## 目录

- [Implementations](#implementations)
- [Apps](#apps)
- [Browsers](#browsers)
- [Tools](#tools)
- [调试工具和学习](#debugging-tools--learning)
- [服务与平台](#services--platforms)
- [固定服务](#pinning-services)
- [过时的项目](#stale-projects)
- [Contribute](#contribute)
- [License](#license)

## 实施
IPFS 是一个开源项目，鼓励开发该协议的多种实现，每种实现都旨在针对各种用例进行优化。

查看 IPFS 文档中的 [IPFS 实现](https://docs.ipfs.tech/concepts/ipfs-implementations/#popular-or-actively-maintained) 列表。

## 应用程序

- [Agregore](https://github.com/AgregoreWeb/agregore-browser) - 用于分布式网络的最小网络浏览器。支持使用浏览器的“fetch()” API 从 IPFS 下载/上传数据
- [Anytype](https://github.com/anyproto) - Anytype 是一个无代码、模块化的 Web 构建器，旨在将所有权归还给创建者。它建立在我们私有、本地优先、p2p 同步和开放的 Anysync 协议之上。
- [archiveweb.page](https://github.com/webrecorder/archiveweb.page) - 适用于 Chrome 和 Chromium 浏览器的高保真 Web 归档扩展，支持 IPFS。
- [Autonomica "IPFS Social Proof"](https://github.com/IBM/ipfs-social-proof) - Autonomica 是一个类似 Keybase 的 Dapp，用于创建身份并通过发布的社交媒体和网络证明来证明该身份。
- [brig](https://github.com/sahib/brig) - 与 git 类似的界面和 FUSE 文件系统进行文件同步。
- [Diffuse](https://github.com/icidasset/diffuse) - 从您的 IPFS 节点或您使用的任何其他云/分布式存储服务播放音乐。
- [Durin](https://durin.site/) - 用于访问和上传 IPFS 网络上的内容的移动应用程序。
- [Hardbin](https://github.com/jes/hardbin) - Hardbin是一个加密的pastebin，解密密钥在URL片段中传递
- [hyprspace](https://github.com/hyprspace/hyprspace) - 建立在 IPFS + Libp2p 之上的轻量级 VPN，用于真正的分布式网络。
- [InterPlanetary Wayback](https://github.com/oduwsdl/ipwb) - 使用 IPFS 进行网络档案 (WARC) 索引和重放。
- [Interplanetary Wiki](https://github.com/jamescarlyle/ipfs-wiki) - Wiki 建立在 IPFS 之上
- [IPFessay](https://gitlab.com/stavros/IPFessay) - 一种在 IPFS 上发布未经审查的论文的简单方法。
- [IPFS Desktop](https://github.com/ipfs-shipyard/ipfs-desktop) - IPFS Desktop 在一个方便的桌面应用程序中为您提供 IPFS 的所有功能：完整的 IPFS 节点，加上方便的操作系统菜单栏/任务栏快捷方式以及一体化文件管理器、对等地图和内容资源管理器。
- [IPFS Share](https://github.com/ipfs-shipyard/ipfs-share-files) - 使用 IPFS 直接从浏览器共享文件。
- [ipfs-chat](https://github.com/SomajitDey/ipfs-chat) - 基于终端的加密聊天室。允许私人消息传递和安全的聊天内文件/目录共享。无服务器/代理（不需要信令/集合服务器）。通过 LAN/互联网工作（带 NAT 穿越）。
- [IPFS-FPS](https://github.com/underscoredLabs/webgl-ipfs-fps) - 完全去中心化的第一人称射击游戏。使用 Unity、Fleek、Unstoppable Domans 和 Pinata 构建。
- [killcord](https://github.com/nomasters/killcord) - 抗审查制度的死亡开关
- [Mintter](https://github.com/MintterHypermedia/mintter) - Mintter 超媒体是一个基于 IPFS 构建的开放系统，允许社区就结构化且深度链接的内容进行协作。系统中的所有内容均经过 IPFS 加密签名、版本控制并永久保存。
- [orbitchat.dev](https://github.com/cppshane/orbit-chat) - 网络上超简单的聊天室。
- [Peer Web Site](https://github.com/Weedshaker/PeerWebSite) - 点对点网站托管触手可及！从您的浏览器发送全功能 HTML（包括 CSS、JS）站点并附加文件，例如。视频、图像等
- [Peergos](https://github.com/Peergos/Peergos) - 端到端加密、点对点文件存储和共享。
- [Planet](https://github.com/Planetable/Planet) - 在 Mac 上使用 IPFS 构建和托管去中心化博客和网站
- [Plebbit](https://github.com/plebbit) - Plebbit 是一个无服务器、无管理、去中心化和无限可扩展的点对点和开源社交媒体平台。它构建在 IPFS、Gossipsub 和区块链名称系统（ENS、SNS）之上。
- [PushToTalk](http://timothy.hobbs.cz/push-to-talk/index.html) - Push to Talk 可让您编辑音频文章并使用 IPFS 发布它们。
- [Quiet](https://tryquiet.org/) - 注重隐私的端到端加密聊天应用程序，通过 Tor 连接运行私有 IPFS 网络。提供桌面和移动 iOS 和 Android 应用程序。
- [TeaTime](https://github.com/bjesus/teatime) - 由 IPFS、SQLite 和 GitHub 提供支持的完全静态分布式图书馆系统。

## 浏览器
具有 IPFS 集成的 Web 浏览器列表
- [Agregore](https://github.com/AgregoreWeb/agregore-browser) - 用于分布式网络的最小网络浏览器。支持使用浏览器的“fetch()” API 从 IPFS 下载/上传数据
- [Brave](https://brave.com/ipfs-support/) - 一款注重隐私的浏览器，具有许多未来的前瞻性功能。
- [galacteek](https://github.com/pinnaculum/galacteek) - 用于分布式 Web 的基于 Qt5 的多平台浏览器。
- [Opera](https://blogs.opera.com/tips-and-tricks/2021/02/opera-crypto-files-for-keeps-ipfs-unstoppable-domains/) - Opera 浏览器于 2021 年添加了对“ipfs://”的支持


## 工具

- [create-ipfs-app](https://github.com/alexbakers/create-ipfs-app) - 通过运行一个命令来设置一个去中心化的 web3 应用程序。
- [dScan](https://github.com/p2plabsxyz/dscan) - 一个浏览器扩展，可将内容上传到 Web3.Storage 并为 CID 生成 QR 代码。
- [dump-ipfs](https://github.com/quasarch/dump-ipfs) - 一个用于 IPFS 和 Filecoin 支持的流行数据库的去中心化加密备份代理。
- [gatsby-plugin-ipfs](https://github.com/moxystudio/gatsby-plugin-ipfs) - 通过确保资产是相对的，添加了对将 Gatsby 网站部署到 IPFS 的支持。
- [git-ipfs-rehost](https://github.com/whyrusleeping/git-ipfs-rehost) - 在 ipfs 中重新托管 git 存储库的脚本。
- [git-remote-ipfs](https://github.com/cryptix/git-remote-ipfs) - 从 IPFS 推送/拉取存储库。
- [Git IPFS Remote Bridge](https://github.com/ElettraSciComp/Git-IPFS-Remote-Bridge) - 一组用 Python 3 编写的程序，允许 Git 用户通过 IPFS 去中心化数据存储系统克隆、推送、获取、自托管或发布 Git 存储库。
- [go-orbit-db](https://github.com/berty/go-orbit-db) - 这是 OrbitDB 的 Golang 端口，旨在与原始 JavaScript 版本完全兼容。 OrbitDB 是一个无服务器、分布式、点对点数据库。
- [gomobile-ipfs](https://github.com/ipfs-shipyard/gomobile-ipfs) - 移动设备上的 IPFS 和 libp2p，以及 Gomobile。
- [http2ipfs](https://github.com/jbenet/http2ipfs-web) - 这是一个简单的 Web 工具，用于将 URL 添加到 IPFS 节点。
- [IPDR](https://github.com/miguelmota/ipdr) - IPFS 支持的 Docker 注册表。
- [IPFS Setup Action](https://github.com/ibnesayeed/setup-ipfs) - 用于安装和初始化 go-ipfs 的 GitHub Action，以在 GitHub 的 CI 平台上配置跨平台测试环境。
- [ipfs-action](https://github.com/aquiladev/ipfs-action) - 用于交付静态网站的 GitHub Action。
- [ipfs-add-from-encrypted](https://github.com/TroyWilson1/ipfs-add-from-encrypted) - 使用 AES256 加密文件或目录，然后添加到 IPFS。
- [IPFS-boot](https://github.com/rhodey/IPFS-boot) - 发布需要用户同意才能更新的 IPFS Web 应用程序。
- [ipfs-companion](https://github.com/ipfs/ipfs-companion) - 简化对 IPFS 资源访问的浏览器扩展。
- [ipfs-deploy](https://github.com/agentofuser/ipfs-deploy) - 用于部署静态网站的零配置 CLI：cd my-static-website && npx @agentofuser/ipfs-deploy
- [ipfs-mount](https://github.com/richardschneider/net-ipfs-mount) - 在 Windows 上将 IPFS 安装为映射驱动器。
- [ipfs-paste](https://github.com/jbenet/ipfs-paste) - 将 stdin 和剪贴板粘贴到 IPFS。
- [ipfs-pinner](https://github.com/wabarc/ipfs-pinner) - 工具包可帮助将文件上传到 IPFS 固定服务。
- [ipfs-publish](https://github.com/auhau/ipfs-publish/) - 持续交付工具，用于将静态网站从 Git 提供商交付到 IPFS。
- [ipfs-screencap](https://github.com/jbenet/ipfs-screencap) - 捕获屏幕截图，将其发布到 IPFS，并将链接复制到剪贴板。
- [ipfs-video-gateway](https://github.com/bneijt/ipfs-video-gateway) - 在云提供商上对您自己的 IPFS 网关进行云初始化，并通过简单的 Web 界面轻松固定内容。
- [ipfsecret](https://github.com/shlemph/ipfsecret) - 使用秘密密码加密和解密 IPFS 文件。
- [ipget](https://github.com/ipfs/ipget) - :satellite: wget for IPFS：通过 IPFS 检索文件并将其保存在本地。
- [IPLD Explorer](https://github.com/ipfs-shipyard/ipld-explorer) - 从舒适的浏览器中探索默克尔森林。
- [ipns-pin](https://github.com/justicenode/node-ipns-pin) - 一个通过 ipns 固定内容的命令行工具。
- [IPRedirect](https://github.com/JayBrown/IPRedirect) - 用于将 IPFS/IPNS 地址重定向到本地网关的浏览器用户脚本。这应该适用于任何尚未为其编写扩展且支持用户脚本的浏览器。
- [iprfc](https://github.com/RTradeLtd/iprfc) - IETF RFC 下载器将 RFC 存储在 IPFS 上并使用 RTradeLtd/Lens 对其进行索引。
- [mahuta](https://github.com/ConsenSys/Mahuta) - Mahuta 是一种适用于微服务架构的即插即用服务，允许在 IPFS 上收集、存储和索引数据，并提供搜索功能（全文、查询）。
- [Multiverse](https://github.com/multiverse-vcs/go-multiverse) - Multiverse 是一个分散的版本控制系统，支持点对点软件开发。
- [Omnipin](https://github.com/omnipin/omnipin) - 终极去中心化网站部署工具包。
- [orbit-db](https://github.com/orbitdb/orbit-db) - OrbitDB 是一个无服务器、分布式、点对点数据库，它使用 IPFS 作为数据存储，并使用 IPFS Pubsub 自动与对等点同步数据库。
- [Pin Tweet to IPFS](https://github.com/meandavejustice/pin-tweet-to-ipfs) - Web 扩展创建推文的 WebArchiveZip 并添加到 IPFS 网络。
- [Public Gateway Checker](https://github.com/ipfs/public-gateway-checker) - 检查哪些公共网关是否在线。
- [rivet](https://github.com/wabarc/rivet) - 工具包可以更轻松地将网页存档到 IPFS。
- [sourcify](https://github.com/ethereum/sourcify) - 去中心化Solidity合约源代码验证服务
- [SimpleAsWater Bot](https://github.com/simpleaswater/twitter-pinbot) - 一个 Twitter 机器人，可使用 IPFS 集群将您的推文添加、固定或取消固定到公共 IPFS 网络。
- [solid-ipfs](https://github.com/Eximua/solid-ipfs) - 使用 Solid 私下或公开存储 IPFS 哈希。
- [Tellit](https://gitlab.com/terceranexus6/tellit) - 在上传文件之前使用密钥对或密码对其进行加密。
- [VIPFS](https://github.com/Ideea-inc/vipfs) - 将您的 Vue 应用程序轻松发布到 IPFS。
- [wbipfs](https://github.com/wabarc/wbipfs) - 用于返回 IPFS 网页的命令行工具和 Go 包接口。
- [youtube2ipfs](https://github.com/dokterbob/youtube2ipfs) - 从 YouTube（和类似的视频平台）下载视频并将其添加到 IPFS。

## 调试工具和学习

- [IPFS检查](https://check.ipfs.network/)
- [海莉亚识别](https://ipfs.fyi/identify)
- [刑事调查督察](https://cid.ipfs.tech/)
- [文件到 UnixFS DAG](https://dag.ipfs.tech/)
- [IPLD浏览器](https://explore.ipld.io)
- [公共网关检查器](https://github.com/ipfs/public-gateway-checker)
- [IPNS检查员](https://github.com/ipfs/ipns-inspector)

## 服务与平台

- [Apillon](http://apillon.io/) - 一个 Web3 开发平台，提供 IPFS 网关、通过 Crust 网络的 IPFS 文件固定以及 IPFS 支持的网站和应用程序托管服务。
- [Ceramic](https://ceramic.network/) - Ceramic 将 IPFS 内容寻址与先进的密码学和区块链时间戳相结合，以保证数据的安全性和可验证性。
- [dAppling](https://www.dappling.network/) - 具有从 GitHub 到 IPFS 自动部署的托管平台
- [Fileverse](https://fileverse.io/) - 基于IPFS的加密文件共享。使用或不使用钱包共享任何文件
- [Fleek](http://fleek.co/) - 开放式 Web 开发平台，用于在 IPFS、Filecoin 和互联网计算机上构建、托管和存储网站和应用程序。
- [Fission](https://fission.codes) - Fission 构建开源协议和托管解决方案，使开发人员能够构建可扩展且安全的软件应用程序。
- [Matters.town](https://matters.town/) - 去中心化的内容发布生态系统。
- [Peergos](https://peergos.org) - 您的私人但社交的在线空间。存储和编辑文档和媒体。与朋友共享文件或文件夹。


## 固定服务
- [4EVERLAND](https://www.4everland.org/) - 4EVERLAND 是一项固定服务，提供 IPFS 基础设施和工具，使托管前端、存储数据/NFT/文件以及使用 IPFS 获取数据变得更容易、更快捷。
- [Filebase](https://filebase.com/) - 将数据固定到 IPFS 可能很困难。文件库消除了这种复杂性。
- [lighthouse.storage](https://lighthouse.storage/) - 具有隐私和加密功能的去中心化 IPFS 固定服务
- [NFT.Storage](https://nft.storage/) - IPFS 和 Filecoin 上的 NFT 的免费去中心化存储和带宽。
- [Pinata](https://pinata.cloud) - 通过 Pinata 的 REST API 和 IPFS 工具包构建和管理您的 dapp。
- [QuickNode](https://www.quicknode.com/ipfs) - IPFS 网关和固定
- [Storacha](https://storacha.network) - 超热门的大规模去中心化数据。

## 过时的项目
我们保留了一份不再维护的项目列表以供参考。如果您发现此列表中的某些内容不再维护，请提交一个 PR，将该条目移至 [stale.md](./stale.md)，并可选择添加其被标记为过时的原因并带有缩进注释。

[在此处查看过时项目列表](./stale.md)

## 贡献

欢迎贡献！

请参阅[**贡献指南**](./CONTRIBUTING.md)。

## 执照

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)
