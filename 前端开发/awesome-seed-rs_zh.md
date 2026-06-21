<!--lint disable double-link-->

# 很棒的种子 RS [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

<p align="center">
    <img src="https://raw.githubusercontent.com/seed-rs/seed-rs.org/81ed1acc77062ede3295683f21f2d39611843192/seed_branding/seed_logo.min.svg" width="256" title="Seed logo">
</p>

> 与种子相关的精彩内容精选列表

Seed 是一个开源 Rust 框架，用于创建在 WebAssembly 中运行的快速可靠的 Web 应用程序。

欢迎贡献。通过拉取请求添加链接或创建问题以开始讨论。

## 内容

- [官方资源](#official-resources)
- [Books](#books)
- [Quickstarts](#quickstarts)
- [Bundlers](#bundlers)
- [Examples](#examples)
- [使用种子的项目](#projects-using-seed)
- [Libraries](#libraries)
- [Contribute](#contribute)

## 官方资源

- ~~首页~~
- [GitHub 仓库](https://github.com/seed-rs/seed)
- [Forum](https://seed.discourse.group)
- [Chat](https://discord.gg/JHHcHp5)

## 书籍
- [Engineering Rust Web Applications](https://erwabook.com/) - 柴油、火箭和种子。
- [Porting a JS app to Rust](https://slowtec.de/posts/2019-12-20-porting-javascript-to-rust-part-1.html) - 使用 Rust 将 JavaScript 应用程序移植到 WebAssembly（博客系列）。

## 快速入门

- [Default quickstart](https://github.com/seed-rs/seed-quickstart) - 仅包含 Rust 库。
- [Quickstart with Webpack](https://github.com/seed-rs/seed-quickstart-webpack) - 主要功能：自动重新加载、预渲染、缩小、[TailwindCSS](https://tailwindcss.com/)、Typescript。

## 捆绑者

- [Trunk](https://github.com/thedodd/trunk) - 适用于 Rust 的 WASM Web 应用程序捆绑器。
- [Web Bundler](https://github.com/panoptix-za/web-bundler) - 捆绑种子 SPA 以进行发布。
- [Seeder](https://github.com/MartinKavik/seeder) - 通过运行一个命令来设置种子应用程序并启动开发服务器。

## 示例

- [RealWorld example](https://github.com/seed-rs/seed-rs-realworld) - “所有演示应用程序之母”——示例性全栈 [Medium.com](https://medium.com/) 克隆。
- [Dark lang Realworld](https://github.com/MartinKavik/seed-realworld-darklang) - 在 _Quickstart with Webpack_ 上种子 Realworld 示例，集成了 [Dark lang](https://darklang.com/) Realworld。
- [Official examples](https://github.com/seed-rs/seed/tree/master/examples) - 官方仓库中包含较小的示例。
- [ERWA mytodo](https://github.com/seed-rs/erwa_mytodo) - Rust 全栈示例。柴油、火箭、种子。
- [Template for GUIs with seed+gotham](https://gitlab.com/liketechnik/local-gui-seed-gotham) - 用于本地/桌面 GUI 的 Electron 模板，包含 Gotham、rust-embed、web-view 和 Seed。
- [Seeded Game of Life](https://github.com/arn-the-long-beard/seeded_game_of_life) - 受 [wasm 教程](https://rustwasm.github.io/docs/book/) 启发，使用纯 Rust 语言的 [教程](https://dev.to/arnthelongbeard/how-to-only-rust-for-web-frontend-1026) 进行生命游戏。
- [Dota Underlord Perfect Build](https://github.com/warycat/dotawasm) - 一款帮助在 Dota Underlord 中构建最佳套牌的应用程序。
- [Play Seed](https://ide.play-seed.dev) - 有几个默认示例的游乐场。

## 使用种子的项目

- [AdEx Explorer](https://github.com/adexnetwork/adex-explorer) - 显示有关 AdEx 广告协议支付渠道网络的精选信息。
- [Kavik.cz](https://github.com/MartinKavik/kavik.cz) - 开源个人网站。
- [benxu.dev/blog](https://github.com/AlterionX/benxu-dev) - 一个比较简单的开源个人博客。基于 `Seed`、[`maud`](https://maud.lambda.xyz)、[`Rocket`](https://rocket.rs) 和 [`Diesel`](https://diesel.rs) 构建。
- ~~seed-rs.org~~ - Seed 的官方网站。
- [WeightRS](https://gitlab.com/mkroehnert/weightrs) - 简约且隐私友好的渐进式网络应用程序，用于跟踪您的体重。
- [Music composer](https://github.com/ethanboxx/planters-rdconf-hackathon-project) - 一个基本的音乐创作应用程序。
- [Play Seed](https://play-seed.dev) - 关于 Play Seed 的网站，演示种子应用程序的游乐场。
- [Typesync](https://typesync.rutrum.net) - 测试您的歌词打字速度。  使用 `Seed`、[`Rocket`](https://rocket.rs) 和 [`Diesel`](https://diesel.rs)。
- [CalcuPi](https://dvjn.github.io/CalcuPi) - 一个漂亮的蒙特卡罗模拟，用于近似 pi 的值。
- [Love Letter Tracker](https://www.fosskers.ca/en/tools/love-letter) - 卡牌游戏_情书_的知识追踪器。
- [Whatlang.org](https://whatlang.org/) - Whatlang（语言识别库）的交互式演示。
- [Pslink](https://pslink.teilgedanken.de) - 专注于在出版物中使用的 URL 缩短器页面（[演示](https://demo.pslink.teilgedanken.de/app/)（用户，密码：demo））。  使用 `Seed`、[`actix-web`](https://actix.rs/) 和 [`sqlx`](https://github.com/launchbadge/sqlx)。

## 图书馆

- [Savory](https://gitlab.com/MAlrusayni/savory) - 用于构建基于 Seed 的用户界面的库。
- [seed-icons](https://crates.io/crates/seed-icons) - 包含要包含在基于种子的应用程序中的图标集合的库。
- [Seed Bootstrap](https://github.com/panoptix-za/seed-bootstrap) - [Bootstrap](https://getbootstrap.com/) CSS 组件的集合。
- [seed_heroicons](https://github.com/mh84/seed_heroicons) - 库提供 [Heroicons](https://heroicons.com/) 以包含到基于种子的应用程序中。

## 贡献

欢迎投稿！首先阅读[贡献指南](contributing.md)。
