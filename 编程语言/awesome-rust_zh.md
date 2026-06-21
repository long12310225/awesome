# 很棒的铁锈 [![lint badge](https://github.com/rust-unofficial/awesome-rust/actions/workflows/lint.yml/badge.svg)](https://github.com/rust-unofficial/awesome-rust/actions/workflows/lint.yml)

Rust 代码和资源的精选列表。

如果您想做出贡献，请阅读[此](CONTRIBUTING.md)。

## 目录

<!-- toc -->

- [Applications](#applications)
  * [音频和音乐](#audio-and-music)
  * [Blockchain](#blockchain)
  * [Database](#database)
  * [Embedded](#embedded)
  * [Emulators](#emulators)
  * [文件管理器](#file-manager)
  * [Finance](#finance)
  * [Games](#games)
  * [Graphics](#graphics)
  * [图像处理](#image-processing)
  * [工业自动化](#industrial-automation)
  * [消息队列](#message-queue)
  * [MLOps](#mlops)
  * [Observability](#observability)
  * [操作系统](#operating-systems)
  * [包管理器](#package-managers)
  * [Payments](#payments)
  * [Productivity](#productivity)
  * [路由协议](#routing-protocols)
  * [安全工具](#security-tools)
  * [社交网络](#social-networks)
  * [系统工具](#system-tools)
  * [任务调度](#task-scheduling)
  * [文本编辑器](#text-editors)
  * [文本处理](#text-processing)
  * [Utilities](#utilities)
  * [Video](#video)
  * [Virtualization](#virtualization)
  * [Web](#web)
  * [网络服务器](#web-servers)
  * [工作流程自动化](#workflow-automation)
- [开发工具](#development-tools)
  * [构建系统](#build-system)
  * [Debugging](#debugging)
  * [Deployment](#deployment)
  * [Embedded](#embedded-1)
  * [FFI](#ffi)
  * [Formatters](#formatters)
  * [IDEs](#ides)
  * [Profiling](#profiling)
  * [Services](#services)
  * [静态分析](#static-analysis)
  * [Testing](#testing)
  * [Transpiling](#transpiling)
  * [Tunnel](#tunnel)
- [Libraries](#libraries)
  * [人工智能](#artificial-intelligence)
+ [遗传算法](#遗传算法)
+ [谷歌双子座](#google-gemini)
+ [机器学习](#machine-learning)
+ [OpenAI](#openai)
+ [工具](#工具)
  * [Astronomy](#astronomy)
  * [Asynchronous](#asynchronous)
  * [音频和音乐](#audio-and-music-1)
  * [Authentication](#authentication)
  * [Automotive](#automotive)
  * [Bioinformatics](#bioinformatics)
  * [Caching](#caching)
  * [Cloud](#cloud)
  * [Command-line](#command-line)
  * [Compression](#compression)
  * [Computation](#computation)
  * [Concurrency](#concurrency)
  * [Configuration](#configuration)
  * [Cryptography](#cryptography)
  * [数据处理](#data-processing)
  * [数据流](#data-streaming)
  * [数据结构](#data-structures)
  * [数据可视化](#data-visualization)
  * [Database](#database-1)
  * [日期和时间](#date-and-time)
  * [分布式系统](#distributed-systems)
  * [领域驱动设计](#domain-driven-design)
  * [eBPF](#ebpf)
  * [Email](#email)
  * [Encoding](#encoding)
  * [Filesystem](#filesystem)
  * [Finance](#finance-1)
  * [函数式编程](#functional-programming)
  * [游戏开发](#game-development)
  * [Geospatial](#geospatial)
  * [图算法](#graph-algorithms)
  * [Graphics](#graphics-1)
  * [GUI](#gui)
  * [图像处理](#image-processing-1)
  * [语言规范](#language-specification)
  * [Licensing](#licensing)
  * [Logging](#logging)
  * [Macro](#macro)
  * [标记语言](#markup-language)
  * [Mobile](#mobile)
  * [网络编程](#network-programming)
  * [Parsing](#parsing)
  * [Peripherals](#peripherals)
  * [平台特定](#platform-specific)
  * [逆向工程](#reverse-engineering)
  * [Scripting](#scripting)
  * [Simulation](#simulation)
  * [社交网络](#social-networks-1)
  * [System](#system)
  * [任务调度](#task-scheduling-1)
  * [模板引擎](#template-engine)
  * [文本处理](#text-processing-1)
  * [文字搜索](#text-search)
  * [Unsafe](#unsafe)
  * [Video](#video-1)
  * [Virtualization](#virtualization-1)
  * [网页编程](#web-programming)
- [Registries](#registries)
- [Resources](#resources)
- [License](#license)

<!-- tocstop -->

## 应用领域

* [ad-si/Woxi](https://github.com/ad-si/Woxi) [[woxi](https://crates.io/crates/woxi)] - 由 Rust 支持的 Wolfram 语言解释器。
* [alacritty](https://github.com/alacritty/alacritty) - 跨平台、GPU 增强的终端模拟器
* [Andromeda](https://github.com/tryandromeda/andromeda) - JavaScript 和 TypeScript 运行时是用 Rust 🦀 从头开始构建的，并由 Nova 引擎提供支持。
* [arimxyer/models](https://github.com/arimxyer/models) [[modelsdev](https://crates.io/crates/modelsdev)] - 用于浏览 AI 模型、基准测试和编码代理的 TUI [![CI](https://github.com/arimxyer/models/actions/workflows/ci.yml/badge.svg)](https://github.com/arimxyer/models/actions/workflows/ci.yml)
* [Arti](https://gitlab.torproject.org/tpo/core/arti) - Tor 的实现。 （到目前为止，这是一个不是很完整的客户端。但是请注意这个空间！） [![Crates.io](https://img.shields.io/crates/v/arti.svg)](https://crates.io/crates/arti)
* [asm-cli-rust](https://github.com/cch123/asm-cli-rust) - 交互式装配外壳。
* [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) - 基于 tauri 和 rust 的跨平台现代 Clash GUI，支持 Windows、macOS 和 Linux。
* [cloudflare/boringtun](https://github.com/cloudflare/boringtun) - 用户空间 WireGuard VPN 实现 [![构建徽章](https://img.shields.io/crates/v/boringtun.svg)](https://crates.io/crates/boringtun)
* [DBX](https://github.com/t8y2/dbx) - 一款使用 Tauri 构建的轻量级开源数据库管理工具，支持 MySQL、PostgreSQL、SQLite、Redis、MongoDB、DuckDB 等。 [![CI](https://github.com/t8y2/dbx/actions/workflows/ci.yml/badge.svg)](https://github.com/t8y2/dbx/actions/workflows/ci.yml)
* [defguard](https://github.com/defguard/defguard) - 具有真正 2FA/MFA 的企业开源 SSO 和 WireGuard VPN
* [denoland/deno](https://github.com/denoland/deno) - 使用 V8 和 Tokio 构建的安全 JavaScript/TypeScript 运行时 [![构建状态](https://github.com/denoland/deno/actions/workflows/ci.yml/badge.svg)](https://github.com/denoland/deno/actions)
* [doprz/dipc](https://github.com/doprz/dipc) - 使用您最喜欢的调色板/主题转换您最喜欢的图像和壁纸 [![crates.io](https://img.shields.io/crates/v/dipc)](https://crates.io/crates/dipc)
* [EasyTier](https://github.com/EasyTier/EasyTier) - 一个简单、功能齐全、分散的网状 VPN，支持 WireGuard。 [![crates.io](https://img.shields.io/crates/v/easytier)](https://crates.io/crates/easytier) [![GitHub 操作](https://github.com/EasyTier/EasyTier/actions/workflows/core.yml/badge.svg)](https://github.com/EasyTier/EasyTier/actions/)[![GitHub操作](https://github.com/EasyTier/EasyTier/actions/workflows/gui.yml/badge.svg)](https://github.com/EasyTier/EasyTier/actions/)
* [Edit](https://github.com/microsoft/edit) - 满足简单需求的简单编辑器。 [![CI](https://github.com/microsoft/edit/actions/workflows/ci.yml/badge.svg)](https://github.com/microsoft/edit/actions/workflows/ci.yml)
* [fcsonline/drill](https://github.com/fcsonline/drill) - 受 Ansible 语法启发的 HTTP 负载测试应用程序
* [fend](https://github.com/printfn/fend) - 任意精度单位感知计算器 [![build](https://github.com/printfn/fend/workflows/build/badge.svg)](https://github.com/printfn/fend/actions/workflows/actions.yml)
* [Fractalide](https://github.com/fractalide/fractalide) - 简单的微服务
* [glzr-io/glazewm](https://github.com/glzr-io/glazewm) - 受 i3wm 启发的 Windows 平铺窗口管理器，具有 YAML 配置、多显示器支持和键盘驱动命令
* [google/mdbook-i18n-helpers](https://github.com/google/mdbook-i18n-helpers) [[mdbook-i18n-helpers](https://crates.io/crates/mdbook-i18n-helpers)] - mdbook 的国际化和渲染扩展。
* [habitat](https://github.com/habitat-sh/habitat) - 由 Chef 创建的用于构建、部署和管理应用程序的工具。
* [Herd](https://github.com/imjacobclark/Herd) - 实验性 HTTP 负载测试应用程序
* [hickory-dns](https://crates.io/crates/hickory-dns) - DNS 服务器 [![构建状态](https://github.com/hickory-dns/hickory-dns/actions/workflows/test.yml/badge.svg)](https://github.com/hickory-dns/hickory-dns/actions?query=workflow%3Atest)
* [innernet](https://github.com/tonarino/innernet) - 在底层使用 Wireguard 的覆盖网络或专用网状网络
* [jedisct1/flowgger](https://github.com/awslabs/flowgger) - 快速、简单、轻量级的数据收集器
* [kalker](https://github.com/PaddiM8/kalker) - 一种科学计算器，支持类似数学的语法，包括用户定义的变量、函数、推导、积分和复数。跨平台 + WASM 支持 [![构建状态](https://github.com/PaddiM8/kalker/workflows/Release/badge.svg)](https://github.com/PaddiM8/kalker/actions)
* [kftray](https://github.com/hcavarsan/kftray) - 一个跨平台系统托盘应用程序，用于管理和共享多个 kubectl 端口转发配置。 [![构建状态](https://github.com/hcavarsan/kftray/workflows/Release/badge.svg)](https://github.com/hcavarsan/kftray/actions)
* [kytan](https://github.com/changlan/kytan) - 高性能点对点 VPN
* [linkerd/linkerd2-proxy](https://github.com/linkerd/linkerd2-proxy) - 适用于 Kubernetes 的超轻服务网格。
* [LWE](https://github.com/YangYuS8/lwe) - 用于浏览、管理和应用 Wallpaper Engine 内容的 Linux 桌面应用程序，使用 Rust 和 Tauri 构建。
* [lzanini/mdbook-katex](https://github.com/lzanini/mdbook-katex) [[mdbook-katex](https://crates.io/crates/mdbook-katex)] - [mdBook](https://github.com/rust-lang/mdBook) 的预处理器，使用 KaTeX 渲染 LaTeX 数学表达式。
* [MaidSafe](https://github.com/maidsafe) - 一个去中心化的平台。
* [mayocream/koharu](https://github.com/mayocream/koharu) - 一款基于 ML 的漫画翻译器，具有自动语音气泡检测、OCR、修复和 LLM 翻译功能，使用 Candle 和 Tauri 构建
* [mdBook](https://github.com/rust-lang/mdBook) - 用于从 markdown 文件创建书籍的命令行实用程序 [![Build Status](https://github.com/rust-lang/mdBook/actions/workflows/main.yml/badge.svg)](https://github.com/rust-lang/mdBook/actions)
* [Mega](https://github.com/web3infra-foundation/mega) - 支持 Git 的 monorepo 和整体代码库管理系统，也是 Google Piper 的非官方开源实现。
* [Michael-F-Bryan/mdbook-linkcheck](https://github.com/Michael-F-Bryan/mdbook-linkcheck) [[mdbook-linkcheck](https://crates.io/crates/mdbook-linkcheck)] - mdbook 的后端，它将为您检查链接。
* [mirrord](https://github.com/metalbear-co/mirrord) - 连接本地流程和云环境，并在云环境中运行本地代码
* [mmalmi/nostr-vpn](https://github.com/mmalmi/nostr-vpn) [[nvpn](https://crates.io/crates/nvpn)] - 基于 Nostr 身份和 FIPS 支持的数据平面构建的 Tailscale 风格的私有网状 VPN。具有本机跨平台应用程序（macOS、Linux、Windows、Mobile）和 CLI/守护程序。
* [nicohman/eidolon](https://github.com/nicohman/eidolon) - 适用于 Linux 和 Macosx 的无 Steam 和 DRM 的游戏注册表和启动器
* [OxideTerm](https://github.com/AnalyseDeCircuit/oxideterm) - 使用 Tauri 2.0 和纯 Rust SSH (russh) 构建的跨平台 SSH 终端客户端和本地终端模拟器。具有多路连接、SFTP 文件管理器、内置 IDE (CodeMirror 6)、端口转发 (-L/-R/-D)、宽限期自动重新连接、插件系统、AI 助手、加密导出 (.oxy) 和 11 种语言。 [![CI](https://github.com/AnalyseDeCircuit/oxyterm/actions/workflows/ci.yml/badge.svg)](https://github.com/AnalyseDeCircuit/oxyterm/actions/workflows/ci.yml)
* [Pijul](https://pijul.org) - 基于补丁的分布式版本控制系统
* [provrb/OBDium](https://github.com/provrb/obdium) - 一款基于 Tauri 的跨平台应用程序，适用于所有车辆诊断。通过 ELM327 适配器​​连接您的车辆并读取故障代码、实时 OBD-II 数据、I/M 准备测试等等！
* [qiluo-admin](https://github.com/chelunfu/qiluo_admin) - 企业级快速开发平台（Axum + SeaORM + JWT + VUE3，支持MySQL/Postgres/SQLite）
* [Rauthy](https://github.com/sebadob/rauthy) - OpenID Connect 单点登录身份和访问管理
* [Rio](https://github.com/raphamorim/rio) - 由 WebGPU 提供支持的硬件加速 GPU 终端模拟器，专注于在桌面和浏览器中运行。
* [rkik](https://github.com/aguacero7/rkik) - CLI 工具专为无状态和被动 NTP 检查而设计，就像 dig 或 ping 用于 DNS 和 ICMP 一样。它支持异步请求和持续监控。 [![crates.io](https://img.shields.io/crates/v/rkik?logo=rust)](https://crates.io/crates/rkik)
* [run](https://github.com/Esubaalew/run) [[run-kit](https://crates.io/crates/run-kit)] - 通用多语言运行器和智能 REPL（25 种以上语言：Python、JS、Go、C 等）。
* [Rust Iot Platform](https://github.com/iot-ecology/rust-iot-platform) - 使用 Rust 构建的高性能物联网开发平台，专为多协议支持和实时数据处理而设计。该平台支持 MQTT、WebSockets (WS)、TCP 和 CoAP 协议，使其高度灵活地适用于各种物联网应用。
* [rx](https://github.com/cloudhead/rx) - Vi 启发的现代像素艺术编辑器
* [Ryot](https://github.com/ignisda/ryot) - 一个自托管应用程序，用于跟踪媒体消费、健身等。
* [s00d/switchshuttle](https://github.com/s00d/switchshuttle) - 跨平台系统托盘应用程序，用于使用全局热键、嵌套菜单和 JSON 支持的配置（Tauri + Vue）组织和运行预定义的终端命令。
* [Saga Reader](https://github.com/sopaco/saga-reader) - 一款由人工智能驱动的极速极轻量互联网阅读器。支持获取搜索引擎信息和RSS。
* [Servo](https://github.com/servo/servo) - 原型网络浏览器引擎
* [shoes](https://github.com/cfal/shoes) - 多协议代理服务器
* [shuttle](https://github.com/shuttle-hq/shuttle) - 无服务器平台。
* [Sniffnet](https://github.com/GyulyVGC/sniffnet) - 跨平台应用程序，可轻松监控网络流量 [![构建徽章](https://img.shields.io/github/actions/workflow/status/gyulyvgc/sniffnet/rust.yml?logo=github)](https://github.com/GyulyVGC/sniffnet/blob/main/.github/workflows/rust.yml) [![crate](https://img.shields.io/crates/v/sniffnet?logo=rust)](https://crates.io/crates/sniffnet)
* [SWC](https://github.com/swc-project/swc) - 超快速 TypeScript / JavaScript 编译器
* [TabbyML/tabby](https://github.com/TabbyML/tabby) - 自托管 AI 编码助手，是 GitHub Copilot 的开源替代方案，具有 GPU 支持和 OpenAPI 接口 [![最新版本](https://shields.io/github/v/release/TabbyML/tabby)](https://github.com/TabbyML/tabby/releases/latest)
* [temps](https://github.com/gotempsh/temps) - 一种自托管 PaaS，使用单个 Rust 二进制文件取代 Vercel、分析、错误跟踪和正常运行时间监控
* [tiny](https://github.com/osa1/tiny) - 终端 IRC 客户端
* [topjohnwu/Magisk](https://github.com/topjohnwu/Magisk) - 一套开源工具，用于定制 Android、提供 root 访问、启动映像操作和无系统修改
* [Typst](https://github.com/typst/typst) - 基于标记的排版系统 [![crates.io](https://img.shields.io/crates/v/typst.svg)](https://crates.io/crates/typst)
* [UpVPN](https://github.com/upvpn/upvpn-app) - 基于 Tauri 构建的适用于 macOS、Linux 和 Windows 的 WireGuard VPN 客户端。
* [vortix](https://github.com/Harry-kp/vortix) - 用于 WireGuard 和 OpenVPN 的终端 UI，具有实时遥测、泄漏检测和终止开关
* [vproxy](https://github.com/0x676e67/vproxy) - 高性能 HTTP/HTTPS/SOCKS5 代理服务器 [![crates.io](https://img.shields.io/crates/v/vproxy.svg)](https://crates.io/crates/vproxy)
* [wasmer](https://github.com/wasmerio/wasmer) - 支持 WASI 和 Emscripten 的安全快速的 WebAssembly 运行时 [![构建状态](https://github.com/wasmerio/wasmer/actions/workflows/build.yml/badge.svg)](https://github.com/wasmerio/wasmer/actions)
* [Weld](https://github.com/serayuzgur/weld) - 完全伪造的 REST API 生成器
* [wezterm](https://github.com/wezterm/wezterm) - GPU 加速的跨平台终端仿真器和多路复用器
* [WinterJS](https://github.com/wasmerio/winterjs) - 使用 SpiderMonkey 和 Axum 构建的安全 JavaScript 运行时
* [zellij](https://github.com/zellij-org/zellij) - 包含电池的终端多路复用器（工作区）
* [Zephyr](https://github.com/Juwan-Hwang/Zephyr) - 使用 Tauri 构建的现代、轻量级且安全的 Mihomo (Clash Meta) GUI 客户端。 [![安全审核](https://github.com/Juwan-Hwang/Zephyr/actions/workflows/security.yml/badge.svg)](https://github.com/Juwan-Hwang/Zephyr/actions/workflows/security.yml)

### 音频和音乐

* [dano](https://github.com/kimono-koans/dano) - 用于媒体文件的 hashdeep/md5tree （但更多）
* [enginesound](https://github.com/DasEtwas/enginesound) - 用于按程序生成半真实引擎声音的 GUI 和命令行应用程序。具有深度配置、可变采样率和频率分析窗口。
* [Festival](https://github.com/hinto-janai/festival) - 本地音乐播放器/服务器/客户端 [![build-badge](https://github.com/hinto-janai/festival/actions/workflows/ci.yml/badge.svg)](https://github.com/hinto-janai/festival/actions/workflows/ci.yml)
* [figsoda/mmtc](https://github.com/figsoda/mmtc) [[mmtc](https://crates.io/crates/mmtc)] - 最小的 mpd 终端客户端，目标是简单但高度可配置[![build-badge](https://github.com/figsoda/mmtc/actions/workflows/ci.yml/badge.svg)](https://github.com/figsoda/mmtc/actions/workflows/ci.yml)
* [Glicol](https://github.com/chaosprint/glicol) - 面向图形的实时编码语言，用于在浏览器中协作音乐。
* [LargeModGames/spotatui](https://github.com/LargeModGames/spotatui) [[spotatui](https://crates.io/crates/spotatui)] - 具有本机流媒体、同步歌词和实时音频可视化功能的 Spotify 终端客户端 [![连续部署](https://github.com/LargeModGames/spotatui/actions/workflows/cd.yml/badge.svg)](https://github.com/LargeModGames/spotatui/actions/workflows/cd.yml)
* [mierak/rmpc](https://github.com/mierak/rmpc) [[rmpc](https://crates.io/crates/rmpc)] - 一个现代且可配置、基于终端的 MPD 客户端，支持专辑封面
* [ncspot](https://github.com/hrkfdn/ncspot) - 跨平台 ncurses Spotify 客户端，灵感来自 ncmpc 等。 [![构建徽章](https://github.com/hrkfdn/ncspot/actions/workflows/ci.yml/badge.svg)](https://github.com/hrkfdn/ncspot/actions?query=workflow%3ABuild)
* [OpenMeters](https://github.com/httpsworldview/openmeters) - 用 Rust 编写的适用于 Linux 的快速、简单且专业的音频计量/可视化。
* [Pinepods](https://github.com/madeofpendletonwool/PinePods) - 一个基于 Rust 的播客管理系统，具有多用户支持。 Pinepods 利用中央数据库，因此收听时间和主题等方面在不同设备上都遵循。通过使用 Tauri 构建的客户端，它是一个完整的跨平台聆听解决方案！ [![Docker 容器构建](https://github.com/madeofpendletonwool/PinePods/actions/workflows/docker-publish.yml/badge.svg)](https://github.com/madeofpendletonwool/PinePods/actions/workflows/docker-publish.yml)
* [Polaris](https://github.com/agersant/polaris) - 音乐流媒体应用程序。
* [Spotify Player](https://github.com/aome510/spotify-player) - 终端中的 Spotify 播放器具有全功能平价。
* [Spotifyd](https://github.com/Spotifyd/spotifyd) - 作为 UNIX 守护进程运行的开源 Spotify 客户端。 [![持续集成](https://github.com/Spotifyd/spotifyd/actions/workflows/ci.yml/badge.svg)](https://github.com/Spotifyd/spotifyd/actions/workflows/ci.yml)
* [termusic](https://github.com/tramhao/termusic) - 音乐播放器 TUI 编写
* [tunein-cli](https://github.com/tsirysndr/tunein-cli) - 直接从您的终端浏览和收听全球数千个广播电台 [![CI](https://github.com/tsirysndr/tunein-cli/actions/workflows/ci.yml/badge.svg)](https://github.com/tsirysndr/tunein-cli/actions/workflows/ci.yml)
* [WhatBPM](https://github.com/sergree/whatbpm) - 为电子舞曲制作人提供的每日静态生成的信息资源。使用 Beatport 和 Spotify 等公开数据，提供每种 EDM 流派最常用值的日常分析：节奏、调、根音等。

### 区块链

* [Anchor](https://github.com/solana-foundation/anchor) - Anchor 是用于构建安全 Solana 程序（智能合约）的领先开发框架。
* [artemis](https://github.com/paradigmxyz/artemis) - 用于编写 MEV 机器人的简单、模块化且快速的框架。
* [比特币中本聪的愿景](https://github.com/brentongunning/rust-sv) [[sv](https://crates.io/crates/sv)] - 用于使用比特币 SV 的库。
* [cairo](https://github.com/starkware-libs/cairo) - Cairo 是第一个图灵完备的语言，用于创建可证明的通用计算程序。这也是 [StarkNet](https://www.starknet.io) 的母语，这是一个使用 STARK 证明的 ZK-Rollup！[GitHub 工作流程状态](https://img.shields.io/github/workflow/status/starkware-libs/cairo/CI?style=flat-square&logo=github)
* [ChainX](https://github.com/chainx-org/ChainX) - Polkadot 上完全去中心化的链间加密资产管理。
* [CITA](https://github.com/citahub/cita) - 面向企业用户的高性能区块链内核。
* [coinbase-pro-rs](https://github.com/inv2004/coinbase-pro-rs) - Coinbase pro客户端，支持同步/异步/websocket
* [datahaven-xyz/datahaven](https://github.com/datahaven-xyz/datahaven) - 由 EigenLayer 保护的 AI-First 去中心化存储。
* [Diem](https://github.com/diem/diem) - 吴庭艳的使命是建立一个简单的全球货币和金融基础设施，为数十亿人提供帮助。
* [dusk-network/rusk](https://github.com/dusk-network/rusk) - Dusk 的参考实现，这是一个注重隐私、可扩展的 FMI，适用于现实世界资产 (RWA) 和合规的金融应用程序。 [![构建状态](https://github.com/dusk-network/rusk/actions/workflows/rusk_ci.yml/badge.svg)](https://github.com/dusk-network/rusk/actions/workflows/rusk_ci.yml)
* [electrumrs](https://github.com/romanz/electrs) - Electrum Server 的高效重新实现。
* [equilibriumco/beerus](https://github.com/equilibriumco/beerus) - Beerus 是一个无需信任的 StarkNet 轻客户端，⚡速度极快 ⚡ [![GitHub 工作流程状态](https://github.com/equilibriumco/beerus/actions/workflows/check.yml/badge.svg)](https://github.com/equilibriumco/beerus/actions/workflows/check.yml)
* [ethabi](https://github.com/rust-ethereum/ethabi) - 对智能合约调用进行编码和解码。
* [ethaddrgen](https://github.com/Limeth/ethaddrgen) - 自定义以太坊虚荣地址生成器
* [etk](https://github.com/quilt/etk) - etk 是用于编写、读取和分析 EVM 字节码的工具集合。
* [Forest](https://github.com/ChainSafe/forest) - Filecoin 实现 [![构建状态](https://img.shields.io/circleci/build/gh/ChainSafe/forest/main?branch=master)](https://app.circleci.com/pipelines/github/ChainSafe/forest?branch=main)
* [Foundry](https://github.com/foundry-rs/foundry) - Foundry 是一个用于以太坊应用程序开发的快速、便携和模块化工具包。 ![构建状态](https://img.shields.io/github/workflow/status/foundry-rs/foundry/test?style=flat-square)
* [Grin](https://github.com/mimblewimble/grin/) - MimbleWimble 协议的演变
* [hdwallet](https://github.com/jjyr/hdwallet) [[hdwallet](https://crates.io/crates/hdwallet)] - BIP-32 HD 钱包相关的密钥派生实用程序。
* [Holochain](https://github.com/holochain/holochain) - 适用于您一直想要构建的所有分布式应用程序的区块链的可扩展 P2P 替代方案。 [![检测关键检查失败](https://github.com/holochain/holochain/actions/workflows/autorebase.yml/badge.svg)](https://github.com/holochain/holochain/actions/)
* [Hyperlane](https://github.com/hyperlane-xyz/hyperlane-monorepo) - 无需许可的模块化互操作性框架。链下客户端以及 Solana VM 和 CosmWasm 的智能合约都是用 Rust 编写的。
* [ibc-rs](https://github.com/informalsystems/hermes) - [区块链间通信](https://docs.cosmos.network/ibc)协议的实现
* [infincia/bip39-rs](https://github.com/infincia/bip39-rs) [[bip39](https://crates.io/crates/bip39)] - BIP39 的实现。
* [interBTC](https://github.com/interlay/interbtc) - 无需信任且完全去中心化的比特币桥接 Polkadot 和 Kusama。
* [Joystream](https://github.com/Joystream/joystream) - 用户管理的视频平台
* [Kaspa](https://github.com/kaspanet/rusty-kaspa) - 世界上最快、开源、去中心化且完全可扩展的 Layer-1。
* [Lighthouse](https://github.com/sigp/lighthouse) - 以太坊共识层 (CL) 客户端 [![构建状态](https://github.com/sigp/lighthouse/actions/workflows/test-suite.yml/badge.svg)](https://github.com/sigp/lighthouse/actions)
* [linera-io/linera-protocol](https://github.com/linera-io/linera-protocol) - 专为高度可扩展、低延迟的 Web3 应用程序设计的去中心化区块链基础设施 [![构建状态](https://github.com/linera-io/linera-protocol/actions/workflows/rust.yml/badge.svg)](https://github.com/linera-io/linera-protocol/actions/workflows/rust.yml)
* [near/nearcore](https://github.com/near/nearcore) - 适用于低端移动设备的去中心化智能合约平台。
* [Nervos CKB](https://github.com/nervosnetwork/ckb) - Nervos CKB 是一个公共的无需许可的区块链，是 Nervos 网络的公共知识层。
* [opensea-rs](https://github.com/gakonst/opensea-rs) - Opensea API 和合约的绑定和 CLI。
* [Parity-Bitcoin](https://github.com/paritytech/parity-bitcoin) - Parity 比特币客户端
* [Phala-Network/phala-blockchain](https://github.com/Phala-Network/phala-blockchain) - 基于Intel SGX和Substrate的保密智能合约区块链
* [polkadot-sdk](https://github.com/paritytech/polkadot-sdk) - Parity Polkadot 区块链 SDK
* [pragma-org/amaru](https://github.com/pragma-org/amaru) - 用 Rust 编写的卡尔达诺节点客户端。
* [reth](https://github.com/paradigmxyz/reth) - 以太坊协议的模块化、贡献者友好且极快的实施。
* [revm](https://github.com/bluealloy/revm) - Revolutionary Machine (revm) 是一个快速的以太坊虚拟机。
* [rust-bitcoin](https://github.com/rust-bitcoin/rust-bitcoin) - 支持反序列化、解析和执行与比特币相关的数据结构和网络消息的库。
* [rust-lightning](https://github.com/lightningdevkit/rust-lightning) [![Crate](https://img.shields.io/crates/v/lightning.svg?logo=rust)](https://crates.io/crates/lightning) - 比特币闪电库。主包“lightning”不处理网络、持久性或任何其他 I/O。因此，它与运行时无关，但用户必须在链接箱上实现基本的网络逻辑、链交互和磁盘存储。
* [sigma-rust](https://github.com/ergoplatform/sigma-rust) - ErgoTree 解释器和钱包相关功能。
* [starkware-libs/cairo-vm](https://github.com/starkware-libs/cairo-vm) - Cairo VM 的实现 [![rust](https://github.com/starkware-libs/cairo-vm/actions/workflows/rust.yml/badge.svg)](https://github.com/starkware-libs/cairo-vm/actions/workflows/rust.yml)
* [Subspace](https://github.com/autonomys/subspace) - 第一个能够同时实现可扩展性、安全性和去中心化，彻底解决区块链三难困境的第一层区块链。
* [Sui](https://github.com/MystenLabs/sui) - 下一代智能合约平台，具有高吞吐量、低延迟和由 Move 编程语言支持的面向资产的编程模型。
* [svm-rs](https://github.com/alloy-rs/svm-rs) - Solidity-编译器版本管理器。
* [tempoxyz/tempo](https://github.com/tempoxyz/tempo) - 专为大规模稳定币支付而构建的区块链，具有 EVM 兼容性、亚秒级最终确定性和本机智能账户功能，基于 Reth SDK 构建
* [tendermint-rs](https://github.com/cometbft/tendermint-rs) - Tendermint 区块链数据结构和客户端
* [wagyu](https://github.com/howardwu/wagyu) [[wagyu](https://crates.io/crates/wagyu)] - 用于生成加密货币钱包的库
* [zcash](https://github.com/zcash/zcash) - Zcash 是“Zerocash”协议的实现。

### 数据库

* [apecloud/ape-dts](https://github.com/apecloud/ape-dts) - 数据传输套件。提供 MySQL、PostgreSQL、Redis、MongoDB、Kafka、ClickHouse 等之间的数据复制。
* [Atomic-Server](https://github.com/ontola/atomic-server/) [[atomic-server](https://crates.io/crates/atomic_server)] - NoSQL 图形数据库，具有实时更新、动态索引和易于使用的 GUI，用于 CMS 目的。 [![发布](https://github.com/ontola/atomic-server/actions/workflows/release_please.yml/badge.svg)](https://github.com/ontola/atomic-server/actions)
* [ayarotsky/redis-shield](https://github.com/ayarotsky/redis-shield) - Redis 模块，将令牌桶算法实现为高性能速率限制的本机命令
* [CozoDB](https://github.com/cozodb/cozo) - 一种使用 Datalog 并专注于图数据和算法的事务型关系数据库。能够进行时间旅行，而且速度很快！ [![GitHub 工作流程状态](https://img.shields.io/github/actions/workflow/status/cozodb/cozo/build.yml?branch=main)](https://github.com/cozodb/cozo/actions/workflows/build.yml)
* [Curvine](https://github.com/CurvineIO/curvine) - Curvine 是一个用 Rust 编写的高性能、并发分布式缓存系统，专为人工智能、大数据等领域的低延迟和高吞吐量工作负载而设计。
* [darkbird](https://github.com/Rustixir/darkbird) [[darkbird](https://crates.io/crates/darkbird)] - 受 erlang mnesia 启发的高并发、实时、内存存储
* [Databend](https://github.com/databendlabs/databend) - 具有云原生架构的现代实时数据处理和分析 DBMS [![发布](https://github.com/databendlabs/databend/actions/workflows/release.yml/badge.svg)](https://github.com/databendlabs/databend/actions)
* [DB3 Network](https://github.com/dbpunk-labs/db3) - DB3 是一个社区驱动的区块链 Layer2 去中心化数据库网络 [![GitHub 工作流状态（带事件）](https://github.com/dbpunk-labs/db3/actions/workflows/ci.yml/badge.svg)](https://github.com/dbpunk-labs/db3/actions/workflows/ci.yml)
* [dsplce-co/supabase-plus](https://github.com/dsplce-co/supabase-plus) [[supabase-plus](https://crates.io/crates/supabase-plus)] - 一个包含电池的命令行实用程序，扩展了官方 Supabase CLI [![GitHub Actions 工作流程]状态](https://img.shields.io/github/actions/workflow/status/dsplce-co/supabase-plus/publish.yml)
](https://github.com/dsplce-co/supabase-plus/actions/workflows/publish.yml)
* [erikgrinaker/toydb](https://github.com/erikgrinaker/toydb) - 分布式 SQL 数据库，作为学习项目编写。
* [Garage](https://github.com/deuxfleurs-org/garage) [[garage](https://crates.io/crates/garage)] - 兼容 S3 的分布式对象存储服务，专为中小型规模的自托管而设计。 [![状态徽章](https://woodpecker.deuxfleurs.fr/api/badges/1/status.svg)](https://woodpecker.deuxfleurs.fr/repos/1)
* [GlueSQL](https://github.com/gluesql/gluesql) - 用于 SQL 数据库的 Rust 库，包括解析器 (sqlparser-rs)、执行层和各种存储选项（持久和非持久），全部位于一个包中。 [![crates.io](https://img.shields.io/crates/v/gluesql.svg)](https://crates.io/crates/gluesql)
* [GreptimeDB](https://github.com/grepTimeTeam/greptimedb/) - 支持 PromQL/SQL/Python 的开源、云原生、分布式时间序列数据库。[![CI](https://github.com/greptimeTeam/greptimedb/actions/workflows/develop.yml/badge.svg)](https://github.com/greptimeTeam/greptimedb/actions/workflows/develop.yml)
* [HelixDB](https://github.com/HelixDB/helix-db) - 强大的图形矢量数据库，用于 RAG 和 AI 的智能数据存储
* [Hiqlite](https://github.com/sebadob/hiqlite) - 高可用、可嵌入、基于 raft 的 SQLite + 缓存
* [indradb](https://crates.io/crates/indradb) - 图数据库
* [KiteSQL](https://github.com/KipData/KiteSQL) - SQL 作为 Rust 的函数
* [lancedb](https://github.com/lancedb/lancedb) [[vectordb](https://crates.io/crates/vectordb)] - 用于人工智能应用程序的无服务器、低延迟矢量数据库
* [Lucid](https://github.com/lucid-kv/lucid) - 可通过 HTTP API 访问的高性能分布式 KV 存储。 [![构建状态](https://github.com/lucid-kv/lucid/workflows/Lucid/badge.svg?branch=master)](https://github.com/lucid-kv/lucid/actions?workflow=Lucid)
* [Materialize](https://github.com/MaterializeInc/materialize) - 由 Timely Dataflow 提供支持的流式 SQL 数据库：heavy_dollar_sign：
* [microsoft/pg_durable](https://github.com/microsoft/pg_durable) - PostgreSQL 内的持久执行。具有自动检查点、崩溃恢复和并行执行功能的长时间运行、容错 SQL 函数。零基础设施 - 作为使用 pgrx 和 Rust 构建的 PostgreSQL 扩展运行。 [![许可证](https://img.shields.io/badge/license-PostgreSQL%20License-3d86c6.svg)](LICENSE.txt)
* [native_db](https://github.com/vincent-herlemont/native_db) [[native_db](https://crates.io/crates/native_db)] - 用于多平台应用程序（服务器、桌面、移动）的嵌入式嵌入式数据库。轻松同步 Rust 类型
* [Neon](https://github.com/neondatabase/neon) - 无服务器 Postgres。我们将存储和计算分开，以提供自动扩展、分支和无底存储。
* [noria](https://github.com/mit-pdos/noria) [[noria](https://crates.io/crates/noria)] - 用于 Web 应用程序后端的动态变化、部分状态数据流
* [oxigraph/oxigraph](https://github.com/oxigraph/oxigraph) [[oxigraph](https://crates.io/crates/oxigraph)] - 实现 [SPARQL](https://www.w3.org/TR/sparql11-overview/) 标准的图形数据库！[Crates.io 版本](https://img.shields.io/crates/v/oxigraph?logo=Rust)
* [ParadeDB](https://github.com/paradedb/paradedb/) - ParadeDB 是基于 Postgres 构建的 Elasticsearch 替代方案，专为实时搜索和分析而设计。
* [ParityDB](https://github.com/paritytech/parity-db) - 快速可靠的数据库，针对读取操作进行了优化
* [pgdogdev/pgdog](https://github.com/pgdogdev/pgdog) - 通过连接池、负载平衡和分片来扩展 PostgreSQL 的快速代理。
* [PumpkinDB](https://github.com/PumpkinDB/PumpkinDB) - 事件源数据库引擎
* [Qdrant](https://github.com/qdrant/qdrant) - 具有扩展过滤支持的开源矢量相似性搜索引擎 [![测试](https://github.com/qdrant/qdrant/actions/workflows/rust.yml/badge.svg)](https://github.com/qdrant/qdrant/actions)
* [Qrlew/qrlew](https://github.com/Qrlew/qrlew) [[qrlew](https://crates.io/crates/qrlew)] - SQL 到 SQL 差异隐私层[![Qrlew](https://github.com/Qrlew/qrlew/actions/workflows/ci.yml/badge.svg)](https://github.com/Qrlew/qrlew/actions) ![Crates.io 版本](https://img.shields.io/crates/v/qrlew?logo=Rust)
* [QuillSQL](https://github.com/feichai0017/QuillSQL) - 受 CMU 15445 启发的教育 Rust 关系数据库 (RDBMS)
* [RisingWaveLabs/RisingWave](https://github.com/RisingWaveLabs/risingwave) - 云端的下一代流数据库 [![CI](https://github.com/risingwavelabs/risingwave/actions/workflows/labeler.yml/badge.svg)](https://github.com/risingwavelabs/risingwave/actions)
* [RustFS](https://github.com/rustfs/rustfs) [[RustFS](https://crates.io/crates/rustfs)] - 🚀 RustFS 是一个开源的、S3 兼容的高性能对象存储系统，支持迁移并与其他 S3 兼容平台（如 MinIO 和 Ceph）共存。  [![status-badge](https://github.com/rustfs/rustfs/actions/workflows/ci.yml/badge.svg)](https://github.com/rustfs/rustfs)
* [ruvnet/ruvector](https://github.com/ruvnet/ruvector) [[ruvector-core](https://crates.io/crates/ruvector-core)] - 一个自学习向量数据库和认知容器，可在本地运行 LLM 并水平扩展。
* [sabiql](https://github.com/riii111/sabiql) [[sabiql](https://crates.io/crates/sabiql)] - 一个快速、无驱动程序的 TUI，用于浏览、查询和编辑 PostgreSQL 数据库。 [![CI](https://github.com/riii111/sabiql/actions/workflows/ci.yml/badge.svg)](https://github.com/riii111/sabiql/actions/workflows/ci.yml)
* [seppo0010/rsedis](https://github.com/seppo0010/rsedis) - Redis 重新实现。
* [Skytable](https://github.com/skytable/skytable) - 多模型 NoSQL 数据库！[GitHub 工作流程状态](https://img.shields.io/github/workflow/status/skytable/skytable/Tests?style=flat-square)
* [sled](https://crates.io/crates/sled) - 一个（测试版）现代嵌入式数据库 [![构建状态](https://github.com/spacejam/sled/actions/workflows/test.yml/badge.svg)](https://github.com/spacejam/sled/actions?workflow=Rust)
* [SQLSync](https://github.com/orbitinghail/sqlsync) - 多人离线优先 SQLite [![GitHub 工作流状态](https://github.com/orbitinghail/sqlsync/actions/workflows/actions.yaml/badge.svg?branch=main)](https://github.com/orbitinghail/sqlsync/actions?query=branch%3Amain)
* [SurrealDB](https://github.com/surrealdb/surrealdb) - 可扩展的分布式文档图数据库 [![构建状态](https://img.shields.io/github/workflow/status/surrealdb/surrealdb/Continously%20integration/main)](https://github.com/surrealdb/surrealdb/actions)
* [tabularis](https://github.com/TabularisDB/tabularis) - 一个轻量级、以开发人员为中心的数据库管理工具，使用 Tauri 和 React 构建。
* [TerminusDB](https://github.com/terminusdb/terminusdb-store) - 开源图形数据库和文档存储 [![构建状态](https://github.com/terminusdb/terminusdb-store/actions/workflows/test.yml/badge.svg)](https://github.com/terminusdb/terminusdb-store/actions)
* [tikv](https://github.com/tikv/tikv) - Rust 中的分布式 KV 数据库
* [tokio-rs/toasty](https://github.com/tokio-rs/toasty) [[toasty](https://crates.io/crates/toasty)] - 一个舒适、简单的 Rust ORM，支持 SQL（SQLite、PostgreSQL、MySQL）和 DynamoDB，具有派生宏、类型安全查询和特定于数据库的功能公开。 [![Crates.io](https://img.shields.io/crates/v/toasty.svg)](https://crates.io/crates/toasty)
* [Tonbo](https://github.com/tonbo-io/tonbo) - Tonbo 是一个基于 Apache Arrow 和 Parquet 构建的嵌入式持久数据库 [![crates.io](https://img.shields.io/crates/v/tonbo.svg)](https://crates.io/crates/tonbo)
* [TrailBase](https://github.com/trailbaseio/trailbase) - 快速、轻量级、单文件 FireBase 替代品，具有类型安全的 API、内置 V8 JS/ES6/TS 引擎、身份验证和管理仪表板 [![GitHub 工作流程状态](https://github.com/trailbaseio/trailbase/workflows/test/badge.svg)](https://github.com/trailbaseio/trailbase/actions?workflow=test)
* [tsink](https://github.com/h2337/tsink) - Rust 的嵌入式时间序列数据库 [![crates.io](https://img.shields.io/crates/v/tsink.svg)](https://crates.io/crates/tsink)
* [Turso](https://github.com/tursodatabase/turso) - Turso Database 是一个进程内 SQL 数据库，与 SQLite 兼容。
* [USearch](https://github.com/unum-cloud/usearch) - 向量和字符串的相似性搜索引擎 [![crates.io](https://img.shields.io/crates/v/usearch.svg)](https://crates.io/crates/usearch)
* [valentinus](https://github.com/kn0sys/valentinus) - 使用 LMDB 绑定构建的下一代矢量数据库 [![Crates.io 版本](https://img.shields.io/crates/v/valentinus)](https://crates.io/crates/valentinus)
* [vorot93/libmdbx-rs](https://github.com/vorot93/libmdbx-rs) [[mdbx-sys](https://crates.io/crates/mdbx-sys)] - MDBX 的绑定，“快速、紧凑、强大、嵌入式、事务性键值数据库，具有宽松的许可证”。这是 mozilla/lmdb-rs 的一个分支，带有补丁以使其能够与 libmdbx 一起使用。
* [WooriDB](https://github.com/naomijub/wooridb) - 受 Crux 和 Datomic 启发的通用时间序列数据库。

### 嵌入式

* [embassy-rs/embassy](https://github.com/embassy-rs/embassy) [[embassy](https://crates.io/crates/embassy)] - 用于嵌入式 Rust 的下一代异步/等待框架，具有适用于 STM32、nRF、RP、ESP32 等的 HAL。具有 embassy-time、embassy-net、embassy-usb 和低功耗支持。 [![构建状态](https://github.com/embassy-rs/embassy/actions/workflows/ci.yml/badge.svg)](https://github.com/embassy-rs/embassy/actions)
* [infinition/waveshare-watch-rs](https://github.com/infinition/waveshare-watch-rs) - 适用于 Waveshare ESP32-S3-Touch-AMOLED-2.06 的 100% Rust `no_std` 智能手表固件。具有 QSPI 80 MHz DMA 显示、Embassy 异步运行时、事件驱动电源管理和始终开启显示功能。
* [rmk](https://github.com/haobogu/rmk) - 功能丰富的键盘固件。
* [rtic-rs/rtic](https://github.com/rtic-rs/rtic) [[rtic](https://crates.io/crates/rtic)] - 用于构建嵌入式实时系统的实时中断驱动的并发框架。
* [uefi-rs](https://github.com/rust-osdev/uefi-rs) - 统一可扩展固件接口的 Rusty 包装器。该箱可以轻松开发 Rust 软件，该软件利用安全、方便且高性能的 UEFI 功能抽象。

### 模拟器

另请参阅[匹配关键字“模拟器”的板条箱](https://crates.io/keywords/emulator)。

* 芯片-8
  * [ColinEberhardt/wasm-rust-chip8](https://github.com/ColinEberhardt/wasm-rust-chip8) - WebAssembly CHIP-8 模拟器。
  * [starrhorne/chip8-rust](https://github.com/starrhorne/chip8-rust) - 芯片8模拟器
*准将64
  * [kondrak/rust64](https://github.com/kondrak/rust64) - Commodore 64 模拟器
* 闪存播放器
  * [Ruffle](https://github.com/ruffle-rs/ruffle) - Ruffle 是一个 Adob​​e Flash Player 模拟器。 Ruffle 使用 WebAssembly 面向桌面和 Web。 [![CI](https://github.com/ruffle-rs/ruffle/actions/workflows/test_rust.yml/badge.svg)](https://github.com/ruffle-rs/ruffle/actions/workflows/test_rust.yml )[![CI](https://github.com/ruffle-rs/ruffle/actions/workflows/test_web.yml/badge.svg)](https://github.com/ruffle-rs/ruffle/actions/workflows/test_web.yml)
* 游戏男孩
  * [Gekkio/mooneye-gb](https://github.com/Gekkio/mooneye-gb) - Game Boy 研究项目和模拟器
  * [joamag/boytacean](https://github.com/joamag/boytacean) - 使用 WebAssembly 在 Web 上运行的 GameBoy Color 模拟器。
  * [mohanson/gameboy](https://github.com/mohanson/gameboy) - 全功能跨平台 GameBoy 模拟器。永远的男孩！
  * [mvdnes/rboy](https://github.com/mvdnes/rboy) - Gameboy 模拟器
* 游戏男孩前进
  * [michelhe/rustboyadvance-ng](https://github.com/michelhe/rustboyadvance-ng) - RustboyAdvance-ng 是一款 Gameboy Advance 模拟器，支持桌面、Android 和 [WebAssembly](https://michelhe.github.io/rustboyadvance-ng/)。 [![构建徽章](https://github.com/michelhe/rustboyadvance-ng/actions/workflows/deploy.yml/badge.svg)](https://github.com/michelhe/rustboyadvance-ng/actions?query=workflow%3ADeploy)
* 游戏制作者
  * [OpenGMK](https://github.com/OpenGMK/OpenGMK) - OpenGMK 是对专有 GameMaker Classic 引擎的现代重写，提供了运行程序的完整源端口、反编译器、TASing 框架以及用于您自己处理游戏数据的库。
* IBM 个人电脑
  * [MartyPC](https://github.com/dbalsom/martypc) - 用 Rust 编写的 IBM PC/XT 模拟器。
* 英特尔8080CPU
  * [mohanson/i8080](https://github.com/mohanson/i8080) - Intel 8080 CPU 模拟器
* iOS
  * [touchHLE](https://github.com/touchHLE/touchHLE) - iPhone OS 应用程序的高级模拟器
* iPod
  * [clicky](https://github.com/daniel5151/clicky) - 点击轮 iPod 模拟器 (WIP)
* 红白机
  * [koute/pinky](https://github.com/koute/pinky) - NES模拟器
  * [pcwalton/sprocketnes](https://github.com/pcwalton/sprocketnes) - NES模拟器
* 任天堂 64
  * [gopher64](https://github.com/gopher64/gopher64) - 用 Rust 编写的 N64 模拟器
* 任天堂 DS
  * [dust](https://github.com/kelpsyberry/dust) - 任天堂 DS 模拟器
* 游戏机 4
  * [Obliteration](https://github.com/obhq/obliteration) - 适用于 Windows、macOS 和 Linux 的实验性 PS4 模拟器 [![CI](https://github.com/obhq/obliteration/actions/workflows/main.yml/badge.svg)](https://github.com/obhq/obliteration/actions/workflows/main.yml)
* 冲击波播放器
  * [DirPlayer](https://github.com/igorlira/dirplayer-rs) - 用 Rust 编写的网络兼容的 Shockwave Player 模拟器
* ZX光谱
  * [rustzx/rustzx](https://github.com/rustzx/rustzx) - [![RustZX CI](https://github.com/rustzx/rustzx/actions/workflows/ci.yml/badge.svg)](https://github.com/rustzx/rustzx/actions/workflows/ci.yml)

### 文件管理器

* [broot](https://github.com/Canop/broot) - 一种查看和导航目录树的新方法（获得目录的概述，即使是大目录；找到一个目录，然后“cd”到它；搜索时永远不会丢失文件层次结构；操作文件，...），进一步阅读 [dystroy.org/broot](https://dystroy.org/broot/) [![最新版本](https://img.shields.io/crates/v/broot.svg)](https://crates.io/crates/broot)
* [elio-fm/elio](https://github.com/elio-fm/elio) [[elio](https://crates.io/crates/elio)] - 包含电池的终端文件管理器，具有丰富的预览、批量操作和垃圾支持。
* [FileSSH](https://github.com/JayanAXHF/FileSSH) - 一个快速且易于使用的 TUI，用于管理远程服务器上的文件，包括快速 SSH 会话创建、就地文件编辑等等！ ![crates.io](https://img.shields.io/crates/v/filessh)
* [joshuto](https://github.com/kamiyaa/joshuto) - 类似游侠的终端文件管理器
* [moyangzhan/mango-finder](https://github.com/moyangzhan/mango-finder) - 使用自然语言搜索您的文件
* [pikeru](https://github.com/dvhar/pikeru) - 适用于 Linux 的文件选择器，具有良好的缩略图和搜索功能
* [spacedriveapp/spacedrive](https://github.com/spacedriveapp/spacedrive) - 构建在虚拟分布式文件系统上的文件管理器。
* [xplr](https://github.com/sayanarijit/xplr) - 一个可破解的、最小的、快速的 TUI 文件浏览器
* [yazi](https://github.com/sxyazi/yazi) - 基于异步 I/O 的极快终端文件管理器。

### 金融

另请参阅[付款](# payments) 应用程序。

* [Ashutosh0x/rust-finance](https://github.com/Ashutosh0x/rust-finance) - 具有多交易所摄取、执行、风险模型和 TUI 仪表板的人工智能交易终端。
* [klirr](https://github.com/Sajjon/klirr) [[klirr](https://crates.io/crates/klirr)] - 零维护和智能 FOSS 生成漂亮的服务和费用发票。
* [longbridge/longbridge-terminal](https://github.com/longbridge/longbridge-terminal) - 长桥证券AI原生CLI：港股/美股/A股/新加坡实时报价、投资组合、交易。
* [nautechsystems/nautilus_trader](https://github.com/nautechsystems/nautilus_trader) - 用 Rust 和 Python 编写的高性能、生产级算法交易平台。
* [tackler](https://github.com/tackler-ng/tackler) [[tackler](https://crates.io/crates/tackler)] - 快速、可靠的簿记引擎，具有原生 GIT SCM 支持纯文本会计 [![CI徽章](https://github.com/tackler-ng/tackler/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/tackler-ng/tackler/blob/main/.github/workflows/ci.yml)
* [tarkah/tickrs](https://github.com/tarkah/tickrs) - 终端中的实时股票行情数据

### 游戏

另请参阅[用活塞制作的游戏](https://github.com/PistonDevelopers/piston/wiki/Games-Made-With-Piston)。

* [buxx/OpenCombat](https://github.com/buxx/OpenCombat) - 一款实时第二次世界大战战术游戏
* [chess-tui](https://github.com/thomas-mauran/chess-tui) - 国际象棋 TUI 实现 ♟️
* [citybound](https://github.com/citybound/citybound) - 你值得拥有的城市模拟游戏
* [cristicbz/rust-doom](https://github.com/cristicbz/rust-doom) - 《毁灭战士》的渲染器可能会发展成为一款可玩的游戏
* [doukutsu-rs](https://github.com/doukutsu-rs/doukutsu-rs) - 重新实现了洞穴故事引擎并进行了一些增强。
* [garkimasera/gaia-maker](https://github.com/garkimasera/gaia-maker) - 行星和环境改造模拟游戏
* [garkimasera/rusted-ruins](https://github.com/garkimasera/rusted-ruins) - 具有像素艺术的可扩展开放世界 Rogue 游戏
* [GitType](https://github.com/unhappychoice/gittype) - 一款 CLI 代码输入游戏，可将您的源代码变成输入挑战
* [gorilla-devs/ferium](https://github.com/gorilla-devs/ferium) - Ferium 是一个快速且功能丰富的 CLI 程序，用于从 Modrinth、CurseForge 和 GitHub 版本下载和更新 Minecraft mods，以及来自 Modrinth 和 CurseForge 的 modpack！[ferium build](https://github.com/gorilla-devs/ferium/actions/workflows/build.yml/badge.svg?branch=main)
* [HactarCE/Hyperspeedcube](https://github.com/HactarCE/Hyperspeedcube) - 现代、适合初学者的 3D 和 4D 魔方模拟器，具有可定制的鼠标和键盘控制以及用于快速求解的高级功能
* [lifthrasiir/angolmois-rust](https://github.com/lifthrasiir/angolmois-rust) - 一款支持BMS格式的简约音乐视频游戏
* [louis-e/arnis](https://github.com/louis-e/arnis) - 使用 OpenStreetMap 和海拔数据从真实地理生成 Minecraft Java/基岩世界 [![CI](https://github.com/louis-e/arnis/actions/workflows/ci-build.yml/badge.svg)](https://github.com/louis-e/arnis/actions)
* [maras-archive/rsnake](https://github.com/maras-archive/rsnake) - 蛇。
* [mcthesw/game-save-manager](https://github.com/mcthesw/game-save-manager) - 用于管理游戏保存的用户友好工具 [![构建徽章](https://github.com/mcthesw/game-save-manager/actions/workflows/tauri.yml/badge.svg)](https://github.com/mcthesw/game-save-manager/actions/workflows/tauri.yml)
* [mtkennerly/ludusavi](https://github.com/mtkennerly/ludusavi) - PC游戏备份工具保存[![构建徽章](https://img.shields.io/github/actions/workflow/status/mtkennerly/ludusavi/main.yaml?logo=github)](https://github.com/mtkennerly/ludusavi/actions/workflows/main.yaml) [![crate](https://img.shields.io/crates/v/ludusavi?logo=rust)](https://crates.io/crates/ludusavi)
* [ozkriff/zemeroth](https://github.com/ozkriff/zemeroth) - 一款小型2D回合制六边形策略游戏
* [rhex](https://github.com/dpc/rhex) - 六边形 ASCII Roguelike
* [rsaarelm/magog](https://github.com/rsaarelm/magog) - 一款roguelike游戏。
* [SoftbearStudios/mk48](https://github.com/SoftbearStudios/mk48) - Mk48.io 是一款在线多人海战游戏
* [Stropox/tetro-tui](https://github.com/Stropox/tetro-tui) [[tetro-tui](https://crates.io/crates/tetro-tui)] - 一款跨平台终端游戏，tetromino 会掉落并堆叠。
* [swatteau/sokoban-rs](https://github.com/swatteau/sokoban-rs) - 推箱子的实现
* [thetawavegame/thetawave-legacy](https://github.com/thetawavegame/thetawave-legacy) - 一款太空射击游戏，致力于成为新游戏开发者做出首次贡献的切入点。 ![构建徽章](https://github.com/thetawavegame/thetawave-legacy/actions/workflows/ci.yml/badge.svg?branch=master)
* [Thinkofname/rust-quake](https://github.com/Thinkofname/rust-quake) - 地震地图渲染器。
* [topheman/snake-pipe-rust](https://github.com/topheman/snake-pipe-rust) - 终端中基于 stdin/stdout（+tcp 和 unix 域套接字）的贪吃蛇游戏 [![crates.io](https://img.shields.io/crates/v/snakepipe.svg)](https://crates.io/crates/snakepipe)
* [ttyperacer/terminal-typeracer](https://gitlab.com/ttyperacer/terminal-typeracer) - 为终端编写的单人打字测试游戏
* [Veloren](https://gitlab.com/veloren/veloren) - 一款开放世界、开源多人体素 RPG 游戏，目前处于 alpha 开发阶段 [![构建徽章](https://gitlab.com/veloren/veloren/badges/master/pipeline.svg)](https://gitlab.com/veloren/veloren/-/pipelines)
* [zipxing/rust_pixel](https://github.com/zipxing/rust_pixel) [[rust_pixel](https://crates.io/crates/rust_pixel)] - 2D 像素艺术游戏引擎和快速原型制作工具，支持文本和图形渲染模式。
* [Zone of Control](https://github.com/ozkriff/zoc) - 一款回合制六边形策略游戏

### 图形

* [dps/rust-raytracer](https://github.com/dps/rust-raytracer) - Peter Shirley 的《One Weekend》中基于光线追踪的一种非常简单的光线追踪器的实现。
* [flxzt/rnote](https://github.com/flxzt/rnote) - 画草图并做手写笔记。
* [ivanceras/svgbob](https://github.com/ivanceras/svgbob) - 将 ASCII 图表转换为 SVG 图形
* [KaminariOS/rustracer](https://github.com/KaminariOS/rustracer) - 基于 Vulkan 光线追踪的 PBR glTF 2.0 渲染器。
* [Limeth/euclider](https://github.com/Limeth/euclider) - 实时 4D CPU 光线追踪器
* [linebender/resvg](https://github.com/linebender/resvg) - 一个 SVG 渲染库。
* [museslabs/phonto](https://github.com/museslabs/phonto) - 适用于 Wayland 和 macOS 的 GPU 加速视频壁纸程序，用 Rust 编写。
* [rodrigorc/papercraft](https://github.com/rodrigorc/papercraft) - 一种打开 3D 模型并用剪刀和胶水在纸上创建它们的工具。
* [rustq/vue-skia](https://github.com/rustq/vue-skia) - 基于 Skia 的 2d 图形 vue 渲染库。它基于 Rust 来实现软件光栅化来执行渲染。
* [storytold/artcraft](https://github.com/storytold/artcraft) - 人工智能驱动的 IDE 和有形计算表面，用于像粘土一样塑造场景、视频和图像。
* [turnage/valora](https://crates.io/crates/valora) - 生成美术的图书馆
* [Twinklebear/tray_rust](https://github.com/Twinklebear/tray_rust) - 光线追踪器
* [wahn/rs_pbrt](https://github.com/wahn/rs_pbrt) - 实现 PBRT 书（第 3 版）C++ 代码的对应部分。

### 图像处理

* [Darkly](https://github.com/darkly-art/darkly) - 适用于数字艺术家和画家的熵编辑器。
* [Graphite](https://github.com/GraphiteEditor/Graphite) - 基于矢量的图形编辑器。
* [Imager](https://github.com/imager-io/imager) - 自动图像优化。
* [oxipng](https://github.com/oxipng/oxipng) [[oxipng](https://crates.io/crates/oxipng)] - 用 Rust 编写的多线程 PNG 优化器。 [![构建状态](https://github.com/oxipng/oxipng/workflows/oxipng/badge.svg)](https://github.com/oxipng/oxipng/actions?query=branch%3Amaster) [![版本](https://img.shields.io/crates/v/oxipng.svg)](https://crates.io/crates/oxipng)
* [visioncortex/vtracer](https://github.com/visioncortex/vtracer) [[vtracer](https://crates.io/crates/vtracer)] - 光栅到矢量图形转换器（jpg/png 到 svg）。

### 工业自动化

* [dora-rs/dora](https://github.com/dora-rs/dora) [[dora-cli](https://crates.io/crates/dora-cli)] - 一个快速、简单的面向数据流的框架，用于使用 Python、Rust 和 C/C++ API 构建机器人和多 AI 应用程序[![CI](https://github.com/dora-rs/dora/workflows/CI/badge.svg)](https://github.com/dora-rs/dora/actions)
* [locka99/opcua](https://github.com/locka99/opcua) - [OPC UA](https://opcfoundation.org/about/opc-technologies/opc-ua/) 库。
* [slowtec/tokio-modbus](https://github.com/slowtec/tokio-modbus) - 一个基于 [tokio](https://tokio.rs) 的 [modbus](https://www.modbus.org) 库。

### 消息队列

* [lonewolf-io/Narwhal](https://github.com/lonewolf-io/narwhal) - 用于边缘应用程序的可扩展的发布/订阅消息服务器。
* [Rmqtt](https://github.com/rmqtt/rmqtt) - MQTT 服务器/MQTT 代理 — 适用于 5G 时代物联网的可扩展分布式 MQTT 消息代理。
* [RobustMQ](https://github.com/robustmq/robustmq) - 下一代云原生融合消息队列。
* [Rocketmq-Rust](https://github.com/mxsm/rocketmq-rust) - 🚀Apache RocketMQ 使用 Rust 构建。更快、更安全、内存使用率更低。

### MLOps

* [TensorZero](https://github.com/tensorzero/tensorzero) - 法学硕士的数据和学习飞轮，统一了推理、可观察性、优化和实验！[TensorZero 构建状态](https://img.shields.io/github/check-runs/tensorzero/tensorzero/main)

### 可观察性

* [avito-tech/bioyino](https://github.com/avito-tech/bioyino) - 高性能可扩展的 StatsD 兼容服务器。
* [esrlabs/chipmunk](https://github.com/esrlabs/chipmunk) - 用于分析大量日志文件和流的本机 egui 桌面应用程序。具有 WebAssembly 插件系统和汽车格式支持。 [![Chipmunk CI](https://github.com/esrlabs/chipmunk/actions/workflows/lint_master.yml/badge.svg)](https://github.com/esrlabs/chipmunk/actions/workflows/lint_master.yml)
* [MegaAntiCheat/client-backend](https://github.com/MegaAntiCheat/client-backend) - [MAC](https://github.com/MegaAntiCheat) 的客户端应用程序。
* [openobserve](https://github.com/openobserve/openobserve) - 方便 10 倍、存储成本降低 140 倍、高性能、PB 级 - Elasticsearch/Splunk/Datadog 替代方案。
* [OpenTelemetry](https://crates.io/crates/opentelemetry) - OpenTelemetry 提供一组 API、库、代理和收集器服务，用于从应用程序捕获分布式跟踪和指标。您可以使用 Prometheus、Jaeger 和其他可观察性工具来分析它们。 [![GitHub Actions CI](https://github.com/open-telemetry/opentelemetry-rust/actions/workflows/ci.yml/badge.svg)](https://github.com/open-telemetry/opentelemetry-rust/actions/workflows/ci.yml)
* [Quickwit-oss/quickwit](https://github.com/quickwit-oss/quickwit) - 用于日志管理的云原生且高性价比的搜索引擎。 [![CI](https://github.com/quickwit-oss/quickwit/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/quickwit-oss/quickwit/actions?query=workflow%3ACI)
* [Scaphandre](https://github.com/hubblo-org/scaphandre) - 功耗监控代理，用于跟踪主机和每个服务的功耗，并支持设计系统和应用程序以实现更高的可持续性。设计适合任何监控工具链（已经支持 prometheus、warp10、riemann...）。
* [vectordotdev/vector](https://github.com/vectordotdev/vector) - 高性能日志、指标和事件路由器。

### 操作系统

另请参阅[用 Rust 编写的操作系统的比较](https://github.com/flosse/rust-os-comparison)。

* [0x59616e/SteinsOS](https://github.com/0x59616e/SteinsOS) - 适用于armv8-a架构的操作系统。
* [Andy-Python-Programmer/aero](https://github.com/Andy-Python-Programmer/aero) - 遵循整体内核设计的现代类 UNIX 操作系统。
* [asterinas/asterinas](https://github.com/asterinas/asterinas) - 安全、快速且通用的操作系统内核，提供与 Linux 兼容的 ABI。
* [DragonOS-Community/DragonOS](https://github.com/DragonOS-Community/DragonOS) - 一个从头开始自主开发内核、兼容Linux的操作系统。
* [hexagonal-sun/moss-kernel](https://github.com/hexagonal-sun/moss-kernel) - 用 Rust 和 Aarch64 程序集编写的类 Unix、Linux 兼容内核。
* [koibtw/highlightos](https://github.com/koibtw/highlightos) - x86_64 操作系统内核用 Rust 和 Assembly 编写。
* [redox-os/redox](https://gitlab.redox-os.org/redox-os/redox) - 一个类Unix通用的基于微内核的操作系统，注重安全性、稳定性、性能、正确性、简单性和实用性，旨在成为Linux和BSD的完整替代品。
* [thepowersgang/rust_os](https://github.com/thepowersgang/rust_os) - 用 Rust 编写的操作系统内核。非 POSIX
* [theseus-os/Theseus](https://github.com/theseus-os/Theseus) - 从头开始编写的安全语言、单一地址空间和单一特权级别操作系统 - [![构建徽章](https://img.shields.io/github/workflow/status/theseus-os/Theseus/Documentation?label=docs%20build)](https://www.theseus-os.com/Theseus/book/index.html)
* [tock/tock](https://github.com/tock/tock) - 适用于基于 Cortex-M 的微控制器的安全嵌入式操作系统
* [vinc/moros](https://github.com/vinc/moros) - 一种基于文本的业余爱好操作系统，针对具有 x86-64 架构和 BIOS 的计算机。

### 包管理器

* [helsing-ai/buffrs](https://github.com/helsing-ai/buffrs) [[buffrs](https://crates.io/crates/buffrs)] - 用于协议缓冲区和 gRPC 架构的现代包管理器。
* [rebos](https://crates.io/crates/rebos) - 在任何 Linux 发行版上自动化包管理的声明式方法 [![crate](https://img.shields.io/crates/v/rebos?logo=rust)](https://crates.io/crates/rebos)

### 付款方式

* [hyperswitch](https://github.com/juspay/hyperswitch) - 一个开源支付协调器，可让您轻松连接多个支付处理器并路由支付流量，所有这些都通过单个 API 集成！[GitHub 最后提交](https://img.shields.io/github/last-commit/juspay/hyperswitch?style=flat-square)

### 生产力

* [0xdea/jiggy](https://github.com/0xdea/jiggy) [[jiggy](https://crates.io/crates/jiggy)] - 用 Rust 编写的简约跨平台鼠标抖动器[![构建](https://github.com/0xdea/jiggy/actions/workflows/build.yml/badge.svg)](https://github.com/0xdea/oneiromancer/jiggy/workflows/build.yml)
* [aannoo/hcom](https://github.com/aannoo/hcom) - 让 AI 代理通过终端（Claude Code、Gemini CLI、Codex、OpenCode）相互发送消息、监视和生成。 Rust PTY 包装器，具有屏幕跟踪、TUI (ratatui) 和守护程序客户端二进制文件； Python 挂钩和 API [![CI](https://github.com/aannoo/hcom/actions/workflows/ci.yml/badge.svg)](https://github.com/aannoo/hcom/actions/workflows/ci.yml)
* [agent-of-empires](https://github.com/njbrake/agent-of-empires) - 用于使用 tmux、git worktrees 和 Docker 沙箱管理多个 AI 编码代理会话的 TUI/CLI
* [aichat](https://github.com/sigoden/aichat) - 一体化 LLM CLI 工具，具有 Shell Assistant、Chat-REPL、RAG、AI 工具和代理，可访问 OpenAI、Claude、Gemini、Ollama、Groq 等。
* [AlexsJones/llmfit](https://github.com/AlexsJones/llmfit) [[llmfit](https://crates.io/crates/llmfit)] - 终端工具，可根据系统的 RAM、CPU 和 GPU 调整 LLM 模型的大小。交互式 TUI，具有硬件检测、多维评分（质量/速度/适合/上下文）、社区排行榜，并支持 Ollama、llama.cpp、MLX、vLLM 等。 [![CI](https://github.com/AlexsJones/llmfit/actions/workflows/ci.yml/badge.svg)](https://github.com/AlexsJones/llmfit/actions/workflows/ci.yml)
* [AlexsJones/llmserve](https://github.com/AlexsJones/llmserve) [[llmserve](https://crates.io/crates/llmserve)] - 交互式 TUI，通过自动检测后端（llama-server、KoboldCpp、LocalAI、MLX、Ollama、vLLM、LM Studio）为本地 LLM 模型提供服务。具有源树导航、每个后端预设、实时日志和视觉模型支持。 [![CI](https://github.com/AlexsJones/llmserve/actions/workflows/ci.yml/badge.svg)](https://github.com/AlexsJones/llmserve/actions/workflows/ci.yml)
* [ast-grep](https://github.com/ast-grep/ast-grep) - 用于代码结构搜索、lint 和重写的 CLI 工具。
* [Bartib](https://github.com/nikolassv/bartib) [[Bartib](https://crates.io/crates/bartib)] - 一个简单的命令行时间跟踪器[![测试](https://github.com/nikolassv/bartib/actions/workflows/test.yml/badge.svg?branch=master)](https://github.com/nikolassv/bartib/actions/workflows/test.yml)
* [bitrouter/bitrouter](https://github.com/bitrouter/bitrouter) [[bitrouter](https://crates.io/crates/bitrouter)] - 代理原生 LLM 路由器，可在每次运行时优化您的代理，零线束更改，使每个模型调用可靠、可追踪、安全且经济高效。通过单个本地端点跨 OpenAI、Anthropic、Google、OpenRouter、Bedrock、GitHub Copilot 等进行路由，并具有 MCP 网关、ACP 集成、护栏、可观察性和多账户故障转移。
* [CookCLI](https://github.com/cooklang/CookCLI) - 具有网络服务器、购物清单和膳食计划功能的命令行食谱管理器。
* [espanso](https://github.com/espanso/espanso) - 跨平台文本扩展器。 [![CI](https://github.com/espanso/espanso/actions/workflows/ci.yml/badge.svg?branch=dev&event=push)](https://github.com/espanso/espanso/actions/workflows/ci.yml)
* [eureka](https://crates.io/crates/eureka) - 无需离开终端即可输入和存储您的想法的 CLI 工具
* [farion1231/cc-switch](https://github.com/farion1231/cc-switch) - 适用于 Claude Code、Codex 和 Gemini CLI 的一体化 GUI 助手和配置文件管理器。
* [fkiene/llmtrim](https://github.com/fkiene/llmtrim) [[llmtrim](https://crates.io/crates/llmtrim)] - 压缩 LLM API 请求以剪切输入和输出标记而不更改答案的本地代理。通过 HTTPS_PROXY 位于 AI 工具和提供商之间；与 Claude Code、Codex 等兼容。 [![CI](https://github.com/fkiene/llmtrim/actions/workflows/ci.yml/badge.svg)](https://github.com/fkiene/llmtrim/actions/workflows/ci.yml)
* [flusterIO/fluster](https://github.com/flusterIO/fluster) - 一款专为 STEM 学生和专业人士打造的一体化笔记应用程序。 [![发布](https://github.com/flusterIO/fluster/actions/workflows/release_rust.yml/badge.svg)](https://github.com/flusterIO/fluster/actions/workflows/release_rust.yml)
* [fulsomenko/kanban](https://github.com/fulsomenko/kanban) [[kanban-tui](https://crates.io/crates/kanban-tui)] - 受lazygit启发的基于终端的项目管理工具[![CI](https://github.com/fulsomenko/kanban/actions/workflows/ci.yml/badge.svg)](https://github.com/fulsomenko/kanban/actions/workflows/ci.yml)
* [Furtherance](https://github.com/unobserved-io/Furtherance) - 使用 GTK4 构建的时间跟踪应用程序
* [graves/awful_aj](https://github.com/graves/awful_aj) [[awful_aj](https://crates.io/crates/awful_aj)] - 用于使用 OpenAI 兼容 API 的 CLI、用于即时工程的 YAML 模板以及用于持久内存的内置矢量数据库。
* [graykode/abtop](https://github.com/graykode/abtop) [[abtop](https://crates.io/crates/abtop)] - 用于监控 AI 编码代理会话的终端 TUI（Claude Code、Codex CLI、OpenCode）。跟踪令牌使用情况、上下文窗口百分比、速率限制、子进程和孤立端口。具有 tmux 集成、12 个主题（包括色盲友好选项）和跨平台支持。 [![CI](https://github.com/graykode/abtop/actions/workflows/ci.yml/badge.svg)](https://github.com/graykode/abtop/actions/workflows/ci.yml)
* [Hmbown/DeepSeek-TUI](https://github.com/Hmbown/DeepSeek-TUI) [[deepseek-tui-cli](https://crates.io/crates/deepseek-tui-cli)] - DeepSeek V4 的终端编码代理，具有流推理块、本地工作区编辑、自动模型选择、MCP 支持和基于ratatui 的 TUI。 [![CI](https://github.com/Hmbown/DeepSeek-TUI/actions/workflows/ci.yml/badge.svg)](https://github.com/Hmbown/DeepSeek-TUI/actions/workflows/ci.yml)
* [iBz-04/gloamy](https://github.com/iBz-04/gloamy) [[gloamy](https://crates.io/crates/gloamy)] - 用于 CLI、通道、网关和硬件工作流程的 Rust 优先自主代理运行时。
* [illacloud/illa](https://github.com/illacloud/illa) - 低代码内部工具构建器。
* [iwe-org/iwe](https://github.com/iwe-org/iwe) [[iwe](https://crates.io/crates/iwe)] - 一个基于 Markdown 的知识管理工具，带有 LSP 服务器和 CLI [![Build状态](https://github.com/iwe-org/iwe/actions/workflows/rust.yml/badge.svg)](https://github.com/iwe-org/iwe/actions/workflows/rust.yml)
* [kruseio/hygg](https://github.com/kruseio/hygg) [[hygg](https://crates.io/crates/hygg)] - 📚 简化您的阅读方式。类似 Vim 的简约 TUI 文档阅读器。
* [LLDAP](https://github.com/lldap/lldap) - 用于身份验证的简化 LDAP 界面。
* [mag123c/toktrack](https://github.com/mag123c/toktrack) - 快速 TUI/CLI，可跟踪 AI 编码 CLI（Claude Code、Codex、Gemini CLI 等）中的令牌使用情况和成本，并具有可在 CLI 数据删除后继续存在的持久缓存。 [![CI](https://github.com/mag123c/toktrack/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/mag123c/toktrack/actions/workflows/ci.yml)
* [max-sixty/worktrunk](https://github.com/max-sixty/worktrunk) [[worktrunk](https://crates.io/crates/worktrunk)] - 用于 git 工作树管理的 CLI，设计用于并行运行 AI 代理，具有钩子、LLM 提交消息和合并工作流程[![CI](https://img.shields.io/github/actions/workflow/status/max-sixty/worktrunk/ci.yaml?branch=main&logo=github)](https://github.com/max-sixty/worktrunk/actions?query=branch%3Amain+workflow%3Aci)
* [muvon/octomind](https://github.com/muvon/octomind) - 开源 AI 代理运行时 CLI，具有超过 48 个专业代理、具有动态服务器注册功能的 MCP 主机、多提供商支持（超过 13 个法学硕士）以及适用于 4 小时以上会话的自适应上下文压缩。
* [pier-cli/pier](https://github.com/pier-cli/pier) - 用于管理（添加、搜索元数据等）所有单行代码、脚本、工具和 CLI 的中央存储库
* [rtk-ai/rtk](https://github.com/rtk-ai/rtk) - 高性能 CLI 代理，可将 AI 编码助手的 LLM 令牌消耗减少 60-90%。过滤和压缩 Claude Code、Copilot、Cursor、Gemini CLI、Codex 等的命令输出。 [![CI](https://github.com/rtk-ai/rtk/workflows/Security%20Check/badge.svg)](https://github.com/rtk-ai/rtk/actions)
* [screenpipe](https://github.com/screenpipe/screenpipe) - 24/7 本地人工智能屏幕和麦克风录音。构建具有完整上下文的人工智能应用程序。与奥拉玛合作。
* [ShadoySV/work-break](https://github.com/ShadoySV/work-break) [[work-break](https://crates.io/crates/work-break)] - 工作和休息时间平衡器考虑到您当前和今天的压力[![构建](https://github.com/ShadoySV/work-break/actions/workflows/release.yml/badge.svg)](https://github.com/ShadoySV/work-break/actions/workflows/release.yml)
* [tambourine-voice](https://github.com/kstonekuan/tambourine-voice) - 适用于任何应用程序的个人 AI 语音界面 - 可定制的听写，让您选择自己的模型和提示，使用 Rust 构建。
* [tassiovirginio/try-rs](https://github.com/tassiovirginio/try-rs) [[try-rs](https://crates.io/crates/try-rs)] - 带有 TUI 的工作区管理器 CLI，用于组织和导航临时实验。
* [thClaws/thClaws](https://github.com/thClaws/thClaws) - 原生 Rust AI 代理工作区，具有多提供商 LLM 支持、技能系统、MCP 服务器、知识库和代理编排。具有桌面 GUI、CLI REPL 和非交互模式。 [![许可证](https://img.shields.io/badge/license-MIT%20OR%20Apache--2.0-blue.svg)](https://github.com/thClaws/thClaws)
* [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) - 开源代理助手，具有桌面 UI、118+ OAuth 集成、本地优先内存树、与 Obsidian 兼容的 wiki、本机语音和 TokenJuice 压缩。使用 Tauri 和 Rust 构建，用于注重隐私的个人 AI。
* [tw93/Pake](https://github.com/tw93/Pake) - 使用 Rust 和 Tauri，通过一个命令将任何网页变成桌面应用程序。轻量、快速且支持 macOS、Windows 和 Linux。
* [xingkongliang/skills-manager](https://github.com/xingkongliang/skills-manager) - 轻量级桌面应用程序，可跨 15 种以上编码工具（Cursor、Claude Code、Codex、Copilot 等）管理、同步和组织 AI 代理技能，并支持 Tauri 2、Rust 后端和 Git 备份。
* [yashs662/rust_kanban](https://github.com/yashs662/rust_kanban) [[rust-kanban](https://crates.io/crates/rust-kanban)] [![Build](https://github.com/yashs662/rust_kanban/actions/workflows/build.yml/badge.svg)](https://github.com/yashs662/rust_kanban/releases) - 终端的看板应用程序

### 路由协议

* [Holo](https://github.com/holo-routing/holo) - Holo 是一套路由协议，旨在支持大规模和自动化驱动的网络
* [RustyBGP](https://github.com/osrg/rustybgp) - 边界网关协议

### 安全工具

* [0xdea/augur](https://github.com/0xdea/augur) [[augur](https://crates.io/crates/augur)] - 逆向工程助手，从二进制文件中提取字符串和相关伪代码[![构建](https://github.com/0xdea/augur/actions/workflows/build.yml/badge.svg)](https://github.com/0xdea/augur/actions/workflows/build.yml)
* [0xdea/haruspex](https://github.com/0xdea/haruspex) [[haruspex](https://crates.io/crates/haruspex)] - 从 IDA Hex-Rays 反编译器中提取伪代码的漏洞研究助手[![构建](https://github.com/0xdea/haruspex/actions/workflows/build.yml/badge.svg)](https://github.com/0xdea/haruspex/actions/workflows/build.yml)
* [0xdea/oneiromancer](https://github.com/0xdea/oneiromancer) [[oneiromancer](https://crates.io/crates/oneiromancer)] - 逆向工程助手，使用本地运行的 LLM 来帮助源代码分析[![构建](https://github.com/0xdea/oneiromancer/actions/workflows/build.yml/badge.svg)](https://github.com/0xdea/oneiromancer/actions/workflows/build.yml)
* [0xdea/rhabdomancer](https://github.com/0xdea/rhabdomancer) [[rhabdomancer](https://crates.io/crates/rhabdomancer)] - 漏洞研究助手，可在二进制文件中找到对潜在不安全 API 函数的所有调用[![构建](https://github.com/0xdea/rhabdomancer/actions/workflows/build.yml/badge.svg)](https://github.com/0xdea/rhabdomancer/actions/workflows/build.yml)
* [AdGuardian-Term](https://github.com/Lissy93/AdGuardian-Term) [[adguardian](https://crates.io/crates/adguardian)] - 基于终端的 AdGuard Home 实例的实时流量监控和统计
* [AFLplusplus/LibAFL](https://github.com/AFLplusplus/LibAFL) - 高级模糊测试库 - 将您的模糊测试器放在 Rust 中！跨核心和机器扩展。适用于 Windows、Android、MacOS、Linux、no_std 等。 [![构建和测试](https://github.com/AFLplusplus/LibAFL/actions/workflows/build_and_test.yml/badge.svg)](https://github.com/AFLplusplus/LibAFL/actions/workflows/build_and_test.yml)
* [arp-scan-rs](https://github.com/kongbytes/arp-scan-rs) - 一款简约的 ARP 扫描工具，可快速扫描本地网络
* [biandratti/huginn-net](https://github.com/biandratti/huginn-net) - 多协议被动网络指纹识别结合 p0f TCP 和 JA4 TLS 分析，用于操作系统和应用程序检测 [![CI](https://github.com/biandratti/huginn-net/actions/workflows/ci.yml/badge.svg)](https://github.com/biandratti/huginn-net/actions/workflows/ci.yml)
* [bountyyfi/lonkero](https://github.com/bountyyfi/lonkero) - 企业级 Web 漏洞扫描器，具有 60 多个攻击模块，用于渗透测试和安全评估
* [cargo-audit](https://crates.io/crates/cargo-audit) - 审核 Cargo.lock 是否存在安全漏洞
* [cargo-auditable](https://crates.io/crates/cargo-auditable) - 使生产 Rust 二进制文件可审计
* [cargo-crev](https://crates.io/crates/cargo-crev) - 用于货物包管理器的可加密验证的代码审查系统。
* [cargo-deny](https://crates.io/crates/cargo-deny) - Cargo 插件可帮助您管理大型依赖图
* [Cherrybomb](https://github.com/blst-security/cherrybomb) - 使用 CLI 工具停止半成品 API 规范，该工具可帮助您通过验证 API 规范来避免未定义的用户行为。
* [cotp](https://github.com/replydev/cotp) - 值得信赖的加密命令行 TOTP/HOTP 身份验证器应用程序，具有导入功能。
* [domcyrus/rustnet](https://github.com/domcyrus/rustnet) - 跨平台网络监控 TUI，通过 eBPF/PKTAP 进行进程识别和深度数据包检查 [![构建徽章](https://img.shields.io/github/actions/workflow/status/domcyrus/rustnet/rust.yml?logo=github)](https://github.com/domcyrus/rustnet/actions/workflows/rust.yml) [![crate](https://img.shields.io/crates/v/rustnet-monitor?logo=rust)](https://crates.io/crates/rustnet-monitor)
* [EFForg/rayhunter](https://github.com/EFForg/rayhunter) - IMSI 捕获器检测工具设计用于在移动热点硬件上运行，帮助用户识别潜在的蜂窝监视（Stingray/蜂窝站点模拟器）[![测试](https://github.com/EFForg/rayhunter/actions/workflows/main.yml/badge.svg)](https://github.com/EFForg/rayhunter/actions/workflows/main.yml)
* [entropic-security/xgadget](https://github.com/entropic-security/xgadget) [[xgadget](https://crates.io/crates/xgadget)] - 快速、并行、跨变体 ROP/JOP 小工具搜索 [![GitHub Actions](https://github.com/entropic-security/xgadget/workflows/test/badge.svg)](https://github.com/entropic-security/xgadget/actions)
* [epi052/feroxbuster](https://github.com/epi052/feroxbuster) - 一个简单、快速、递归的内容发现工具。
* [InnerWarden/innerwarden](https://github.com/InnerWarden/innerwarden) - 适用于 Linux 和 macOS 的自卫安全代理，具有 22 个 eBPF 内核挂钩、39 个检测器和 AI 驱动的事件响应 [![CI](https://github.com/InnerWarden/innerwarden/actions/workflows/ci.yml/badge.svg)](https://github.com/InnerWarden/innerwarden/actions/workflows/ci.yml)
* [Inspektor](https://github.com/inspektor-dev/inspektor) - 用于执行访问策略的数据库协议感知代理👮
* [kpcyrd/authoscope](https://github.com/kpcyrd/authoscope) - 可编写脚本的网络身份验证破解程序
* [kpcyrd/rshijack](https://github.com/kpcyrd/rshijack) - TCP 连接劫持者；重写shijack
* [kpcyrd/sn0int](https://github.com/kpcyrd/sn0int) - 半自动 OSINT 框架和包管理器
* [kpcyrd/sniffglue](https://github.com/kpcyrd/sniffglue) - 安全的多线程数据包嗅探器
* [LeChatP/RootAsRole](https://github.com/LeChatP/RootAsRole) - sudo(-rs)/su 的更好替代品 • ⚡ 速度极快 • 🛡️ 内存安全 • 🔐 面向安全 ![Build](https://img.shields.io/github/actions/workflow/status/LeChatP/RootAsRole/build.yml?logo=githubactions&label=Build&logoColor=white) ![覆盖范围](https://img.shields.io/codecov/c/github/lechatp/rootasrole?color=green&link=https%3A%2F%2Fapp.codecov.io%2Fgh%2FLeChatP%2FRootAsRole&label=Test%20Coverage) ![crates.io](https://img.shields.io/crates/v/rootasrole.svg?label=Version&color=e37602&logo=rust)
* [microsoft/mxc](https://github.com/microsoft/mxc) - 沙盒代码执行系统，用于在 Windows、Linux 和 macOS 上运行不受信任的代码（模型输出、插件、工具）。具有多个遏制后端（ProcessContainer、Windows Sandbox、LXC、Bubblewrap、Seatbelt、MicroVM、Hyperlight、IsolationSession、WSLC）以及基于 JSON 的策略驱动沙箱和 TypeScript SDK。 [![CI](https://github.com/microsoft/mxc/actions/workflows/ci.yml/badge.svg)](https://github.com/microsoft/mxc/actions)
* [mongodb/kingfisher](https://github.com/mongodb/kingfisher) - 一个极快的工具，用于跨文件、Git 存储库、S3、Jira 和 Confluence 进行秘密检测和实时验证
* [mullvad/mullvadvpn-app](https://github.com/mullvad/mullvadvpn-app) - 适用于 Mulvad VPN 服务的跨平台 VPN 客户端应用程序，具有 WireGuard 支持、抗量子隧道和注重隐私的功能。 [![CI](https://github.com/mullvad/mullvadvpn-app/actions/workflows/verify.yml/badge.svg)](https://github.com/mulvad/mullvadvpn-app/actions)
* [observer_ward](https://github.com/emo-crab/observer_ward) - Web应用和服务指纹识别工具
* [Raspirus](https://github.com/Raspirus/Raspirus) - 用户和资源友好的基于规则的恶意软件扫描程序 [![status](https://github.com/Raspirus/Raspirus/actions/workflows/testproject.yml/badge.svg)](https://github.com/Raspirus/Raspirus/actions/workflows/testproject.yml)
* [reaction](https://framagit.org/ppom/reaction) - 扫描日志并采取行动：fail2ban 的替代方案
* [ripasso](https://github.com/cortex/ripasso/) - 一个密码管理器，与pass兼容的文件系统
* [rustscan](https://github.com/bee-san/RustScan) - 使用此端口扫描工具使 Nmap 更快 [![构建徽章](https://github.com/bee-san/RustScan/actions/workflows/test.yml/badge.svg)](https://github.com/bee-san/RustScan/actions)
* [secluso](https://github.com/secluso/core) - 使用端到端加密的私有 Raspberry Pi 家庭安全摄像头
* [sherlock](https://github.com/jonaylor89/sherlock-rs) [[sherlock](https://crates.io/crates/sherlock)] - 通过社交网络上的用户名搜索社交媒体帐户[![状态](https://github.com/jonaylor89/sherlock-rs/actions/workflows/rust.yml/badge.svg)](https://github.com/jonaylor89/sherlock-rs/actions/workflows/rust.yml)
* [ssh-vault](https://github.com/ssh-vault/ssh-vault) - 一个使用 ssh 密钥进行加密和解密来管理机密的简单工具。
* [SystemVll/TAuth](https://github.com/SystemVll/TAuth) - 适用于您的 PC 的简单且用户友好的 2FA 和凭据管理器。

### 社交网络

* 不和谐
  * [concord](https://github.com/chojs23/concord) - 功能丰富的 Discord TUI 客户端。
* 乳齿象
  * [Rustodon](https://github.com/rustodon/rustodon) - 与 Mastodon 兼容、使用 ActivityPub 的服务器。
* 电报
  * [tgt](https://github.com/FedericoBruzzone/tgt) - Telegram 的跨平台 TUI [![ci-linux](https://github.com/FedericoBruzzone/tgt/actions/workflows/ci-linux.yml/badge.svg)](https://github.com/FedericoBruzzone/tgt/actions/workflows/ci-linux.yml) [![ci-macos](https://github.com/FedericoBruzzone/tgt/actions/workflows/ci-macos.yml/badge.svg)](https://github.com/FedericoBruzzone/tgt/actions/workflows/ci-macos.yml) [![ci-windows](https://github.com/FedericoBruzzone/tgt/actions/workflows/ci-windows.yml/badge.svg)](https://github.com/FedericoBruzzone/tgt/actions/workflows/ci-windows.yml)

### 系统工具

* [ajeetdsouza/zoxide](https://github.com/ajeetdsouza/zoxide/) - “cd”的快速替代品，可以了解您的习惯 [![release](https://github.com/ajeetdsouza/zicide/actions/workflows/release.yml/badge.svg)](https://github.com/ajeetdsouza/zicide/actions)
* [anylinuxfs](https://github.com/nohajc/anylinuxfs) - 用于在 Mac 上安装任何 Linux 支持的文件系统的 CLI 工具 - 使用带有 microVM 的 NFS
* [anylinuxfs-gui](https://github.com/fenio/anylinuxfs-gui) - Anylinuxfs 的 GUI 应用程序
* [ataraxy-labs/sem](https://github.com/ataraxy-labs/sem) - 实体级语义版本控制 CLI。通过 Tree-sitter 在 26 种语言的函数/类级别进行差异、责任、图表和影响分析。 [![发布](https://github.com/ataraxy-labs/sem/actions/workflows/release.yml/badge.svg)](https://github.com/ataraxy-labs/sem/actions/workflows/release.yml)
* [ataraxy-labs/weave](https://github.com/ataraxy-labs/weave) - Git 的实体级合并驱动程序。通过树守护者了解代码结构来解决合并冲突。通过 .gitattributes 作为自定义合并驱动程序放入 git 中。 [![发布](https://github.com/ataraxy-labs/weave/actions/workflows/release.yml/badge.svg)](https://github.com/ataraxy-labs/weave/actions/workflows/release.yml)
* [atuin](https://github.com/atuinsh/atuin) [[atuin](https://crates.io/crates/atuin)] - Atuin 用 SQLite 数据库替换现有的 shell 历史记录，并记录命令的附加上下文。此外，它还通过 Atuin 服务器提供机器之间可选且完全加密的历史记录同步。
* [bandwhich](https://github.com/imsnif/bandwhich) - 终端带宽利用工具
* [bolivian-peru/os-moda](https://github.com/bolivian-peru/os-moda) - NixOS 发行版中的 AI 代理通过 91 种类型的 MCP 工具获得 root 权限。 9 个 Rust 守护进程（系统桥、原子 SafeSwitch 部署自动回滚、哈希链式审计账本、AES-256-GCM 加密钱包、Noise_XX + ML-KEM-768 P2P 网格、本地 STT/TTS、MCP 服务器生命周期、系统学习、域允许的出口代理）通过 Unix 套接字进行通信。
* [bottom](https://github.com/ClementTsang/bottom) - 另一种跨平台图形进程/系统监视器。 [![GitHub 工作流程状态（分支）](https://img.shields.io/github/workflow/status/ClementTsang/bottom/ci/master)](https://github.com/ClementTsang/bottom/actions?query=branch%3Amaster)
* [brocode/fblog](https://github.com/brocode/fblog) - 小型命令行 JSON 日志查看器
* [brush-shell](https://github.com/reubeno/brush) - bash/POSIX 兼容 shell [![CICD](https://github.com/reubeno/brush/actions/workflows/ci.yaml/badge.svg)](https://github.com/reubeno/brush/actions/wo rkflows/ci.yaml)[![板条箱](https://img.shields.io/crates/v/brush-shell.svg?logo=rust)](https://crates.io/crates/brush-shell)
* [bustd](https://github.com/vrmiguel/bustd) - 用于处理 Linux 上内存不足情况的轻量级进程杀手守护进程。 [![GitHub 工作流状态（分支）](https://img.shields.io/github/workflow/status/vrmiguel/bustd/build-and-test)](https://github.com/vrmiguel/bustd/actions?query=branch%3Amaster)
* [buster/rrun](https://github.com/buster/rrun) - Linux 的命令启动器，类似于 gmrun
* [cantino/mcfly](https://github.com/cantino/mcfly) - 浏览您的 shell 历史记录。伟大的斯科特！
* [ChurchTao/clipboard-rs](https://github.com/ChurchTao/clipboard-rs) [[clipboard-rs](https://crates.io/crates/clipboard-rs)] - 用 Rust 编写的跨平台库，用于获取、设置和监视系统级剪贴板内容的更改。
* [Cocoa-Way](https://github.com/J-x-Z/cocoa-way) [[homebrew](https://github.com/J-x-Z/homebrew-tap)] - 本机 macOS Wayland 合成器，用于运行 Linux GUI 应用程序，无需 VM 开销。与史密斯一起建造。 [![构建徽章](https://github.com/J-x-Z/cocoa-way/actions/workflows/release.yml/badge.svg)](https://github.com/J-x-Z/cocoa-way/actions)
* [crabz](https://github.com/sstadick/crabz) - 多线程压缩和解压CLI工具 [![构建状态](https://github.com/sstadick/crabz/workflows/Check/badge.svg)](https://github.com/sstadick/crabz/actions?query=workflow%3ACheck)
* [cristianoliveira/funzzy](https://github.com/cristianoliveira/funzzy) - 受 [entr](http://eradman.com/entrproject/) 启发的可配置文件系统观察器
* [dalance/procs](https://github.com/dalance/procs) - 'ps' 的现代替代品 [![Regression](https://github.com/dalance/procs/actions/workflows/regression.yml/badge.svg)](https://github.com/dalance/procs/actions/workflows/regression.yml)
* [ddh](https://github.com/darakian/ddh) - 快速重复文件查找器
* [deshaw/procfd](https://github.com/deshaw/procfd) [[procfd](https://crates.io/crates/procfd)] - Linux lsof 替换以列出进程的打开文件描述符
* [diskonaut](https://github.com/imsnif/diskonaut) - 终端可视磁盘空间导航器
* [dust](https://github.com/bootandy/dust) - du 的更直观版本
* [erickochen/purple](https://github.com/erickochen/purple) [[purple-ssh](https://crates.io/crates/purple-ssh)] - Ratatui 支持的 SSH 客户端，具有云同步、容器管理、文件传输、隧道、片段和密码管理功能[![CI](https://github.com/erickochen/purple/actions/workflows/ci.yml/badge.svg)](https://github.com/erickochen/purple/actions/workflows/ci.yml)
* [eza-community/eza](https://github.com/eza-community/eza) - 'ls' 的替代品
* [fish-shell/fish-shell](https://github.com/fish-shell/fish-shell) - 用户友好的命令行 shell
* [fork](https://github.com/immortal/fork) - 用于创建与控制终端分离的新进程的库（守护进程）
* [fselect](https://crates.io/crates/fselect) - 使用类似 SQL 的查询查找文件
* [git-ai-project/git-ai](https://github.com/git-ai-project/git-ai) - 一个 git 扩展，用于跟踪存储库中 AI 生成的代码，将行链接到代理、模型和转录本。
* [gitbutlerapp/gitbutler](https://github.com/gitbutlerapp/gitbutler) - 基于 Git 的现代版本控制界面，具有 GUI 和 CLI，专为 AI 驱动的工作流程而全新构建。
* [gitui](https://github.com/gitui-org/gitui) - 极速的 git 终端客户端。 [![build](https://github.com/gitui-org/gitui/actions/workflows/ci.yml/badge.svg)](https://github.com/gitui-org/gitui/actions)
* [GQL](https://github.com/amrdeveloper/gql) - 类似 SQL 的查询语言，可在 .git 文件上运行。
* [httm](https://github.com/kimono-koans/httm) - 适用于 ZFS/btrfs/nilfs2 的交互式文件级类似时间机器的工具（甚至是实际的时间机器备份！）
* [hyperb1iss/unifly](https://github.com/hyperb1iss/unifly) [[unifly](https://crates.io/crates/unifly)] - 用于管理具有双 API 覆盖和 10 屏幕 Ratatui 仪表板的 Ubiquiti UniFi 网络控制器的 CLI 和 TUI [![CI](https://github.com/hyperb1iss/unifly/actions/workflows/cicd.yml/badge.svg)](https://github.com/hyperb1iss/unifly/actions/workflows/cicd.yml)
* [j0ru/kickoff](https://github.com/j0ru/kickoff) - 快速、敏捷的 Wayland 程序启动器 [![build](https://github.com/j0ru/kickoff/actions/workflows/ci.yml/badge.svg)](https://github.com/j0ru/kickoff/actions)
* [jacek-kurlit/pik](https://github.com/jacek-kurlit/pik) [[pik](https://crates.io/crates/pik)] - 一个 TUI 命令行工具，有助于查找和终止进程
* [Kondo](https://github.com/tbillington/kondo) - 用于删除软件项目工件和回收磁盘空间的 CLI 和 GUI 工具
* [LACT](https://github.com/ilya-zlobintsev/LACT) - Linux AMDGPU 控制器
* [lodosgroup/lpm](https://github.com/lodosgroup/lpm) - 实验性系统包管理器
* [lotabout/rargs](https://github.com/lotabout/rargs) [[rargs](https://crates.io/crates/rargs)] - xargs + awk，支持模式匹配
* [lsd](https://github.com/lsd-rs/lsd) - 一个有很多漂亮颜色和很棒图标的 ls [![build](https://github.com/lsd-rs/lsd/actions/workflows/CICD.yml/badge.svg)](https://github.com/lsd-rs/lsd/actions)
* [Luminarys/synapse](https://github.com/Luminarys/synapse) - 灵活且快速的 BitTorrent 守护程序。
* [m4b/bingrep](https://github.com/m4b/bingrep) - 对来自各种操作系统和架构的二进制文件进行 Greps，并为它们着色。
* [macpow](https://github.com/k06a/macpow) - 适用于 Apple Silicon Mac (M1–M5+) 的实时功耗监控 TUI。读取 IOReport、SMC、IORegistry — 无需 sudo。 [![CI](https://github.com/k06a/macpow/actions/workflows/ci.yml/badge.svg)](https://github.com/k06a/macpow/actions/wo rkflows/ci.yml)[![crates.io](https://img.shields.io/crates/v/macpow.svg?logo=rust)](https://crates.io/crates/macpow)
* [matheus-git/systemd-manager-tui](https://github.com/matheus-git/systemd-manager-tui) [[systemd-manager-tui](https://crates.io/crates/systemd-manager-tui)] - 通过 TUI（终端用户界面）管理 systemd 服务的程序。
* [matthart1983/diskwatch](https://github.com/matthart1983/diskwatch) - 单主机磁盘诊断 TUI：跨设备、卷、文件系统、IO、SMART、热文件和见解的八个选项卡。
* [mattart1983/netwatch](https://github.com/matthart1983/netwatch) [[netwatch-tui](https://crates.io/crates/netwatch-tui)] - 实时网络诊断 TUI：跨 13 种协议（TLS、QUIC、HTTP、DNS、SSH、MQTT、SNMP 等）的深度数据包检测，通过 eBPF / PKTAP、TCP 进行每个进程归因重传分析、JA4 指纹识别、可选的 Landlock 沙箱和飞行记录器事件包。
* [mattart1983/syswatch](https://github.com/mattart1983/syswatch) [[syswatch](https://crates.io/crates/syswatch)] - 单主机系统诊断 TUI：跨 CPU、内存、磁盘、进程、GPU、电源、服务和网络的 12 个选项卡，以及时间轴清理器和 Insights 异常引擎。
* [mdgaziur/findex](https://github.com/mdgaziur/findex) - Findex 是一个使用 GTK3 的高度可定制的应用程序查找器
* [mitnk/cicada](https://github.com/mitnk/cicada) - 类似 bash 的 Unix shell
* [mmstick/concurr](https://github.com/mmstick/concurr) - 具有客户端-服务器架构的 GNU Parallel 的替代方案
* [mmstick/fontfinder](https://github.com/mmstick/fontfinder) - 用于预览和安装 Google 字体的 GTK3 应用程序
* [mmstick/tv-renamer](https://github.com/mmstick/tv-renamer) - 带有可选 GTK3 前端的电视剧重命名应用程序。
* [mxseev/logram](https://github.com/mxseev/logram) - 将日志文件的更新推送到 Telegram
* [netscanner](https://github.com/Chleba/netscanner) - TUI 网络扫描仪
* [nickgerace/gfold](https://github.com/nickgerace/gfold) [[gfold](https://crates.io/crates/gfold)] - CLI 工具帮助跟踪多个 Git 存储库[![build](https://img.shields.io/github/workflow/status/nickgerace/gfold/merge/main)](https://github.com/nickgerace/gfold/actions?query=workflow%3Amerge+branch%3Amain)
* [nivekuil/rip](https://github.com/nivekuil/rip) - “rm”的安全且符合人体工程学的替代品
* [nushell/nushell](https://github.com/nushell/nushell) - 一种新型外壳
* [nwiizo/tfmcp](https://github.com/nwiizo/tfmcp) - Terraform MCP Tool - 用于 AI 助手的 CLI，可通过模型上下文协议管理 Terraform 环境。
* [nwiizo/tfocus](https://github.com/nwiizo/tfocus) - 用于选择和执行 Terraform 计划/应用操作的交互式工具
* [orhun/kmon](https://github.com/orhun/kmon) - Linux 内核管理器和活动监视器！[https://github.com/orhun/kmon/actions](https://img.shields.io/github/actions/workflow/status/orhun/kmon/ci.yml?branch=master&label=build)
* [orhun/systeroid](https://github.com/orhun/systeroid) - 具有终端用户界面的 sysctl(8) 的更强大替代品！[https://github.com/orhun/systeroid/actions](https://img.shields.io/github/actions/workflow/status/orhun/systeroid/ci.yml?branch=main&label=build)
* [ouch](https://github.com/ouch-org/ouch) - 在命令行上进行无痛压缩和解压 [![GitHub Workflow Status (branch)](https://img.shields.io/github/workflow/status/ouch-org/ouch/build-and-test)](https://github.com/ouch-org/ouch/actions?query=branch%3Amaster)
* [pkolaczk/fclones](https://github.com/pkolaczk/fclones) - 高效的重复文件查找器和删除器
* [pop-os/popsicle](https://github.com/pop-os/popsicle) - GTK3 和 CLI 实用程序用于并行刷新多个 USB 设备
* [pop-os/system76-power](https://github.com/pop-os/system76-power/) - 带有 CLI 工具的 Linux 电源管理守护进程（DBus 接口）。
* [pueue](https://github.com/nukesor/pueue) - 管理长时间运行的 shell 命令。 [![GitHub Actions 工作流程](https://github.com/Nukesor/pueue/actions/workflows/test.yml/badge.svg)](https://github.com/nukesor/pueue/actions)
* [qarmin/czkawka](https://github.com/qarmin/czkawka) - 用于查找重复项、空文件夹、相似图像等的多功能应用程序。 [![GitHub Actions Workflow](https://github.com/qarmin/czkawka/actions/workflows/pages/pages-build-deployment/badge.svg?branch=master)](https://github.com/qarmin/czkawka/actions)
* [redox-os/ion](https://github.com/redox-os/ion) - 下一代系统外壳
* [sharkdp/bat](https://github.com/sharkdp/bat) - 一只带翅膀的猫（1）克隆体。 [![CICD](https://github.com/sharkdp/bat/actions/workflows/CICD.yml/badge.svg?branch=master)](https://github.com/sharkdp/bat/actions/workflows/CICD.yml)
* [sharkdp/fd](https://github.com/sharkdp/fd) - 一个简单、快速且用户友好的替代方案。 [![CICD](https://github.com/sharkdp/fd/actions/workflows/CICD.yml/badge.svg)](https://github.com/sharkdp/fd/actions/workflows/CICD.yml)
* [sharkdp/hexyl](https://github.com/sharkdp/hexyl) [[hexyl](https://crates.io/crates/hexyl)] - 命令行十六进制查看器，针对不同字节类别提供彩色输出[![CICD](https://github.com/sharkdp/hexyl/actions/workflows/CICD.yml/badge.svg)](https://github.com/sharkdp/hexyl/actions/workflows/CICD.yml)
* [sitkevij/hex](https://github.com/sitkevij/hex) - 彩色十六进制转储终端实用程序。
* [skim](https://github.com/skim-rs/skim) - 模糊查找器
* [supercilex/fuc](https://github.com/supercilex/fuc) - 快速“cp”和“rm”命令
* [topheman/webassembly-component-model-experiments](https://github.com/topheman/webassembly-component-model-experiments) - 基于 WebAssembly 组件模型的 REPL，具有沙盒多语言插件系统 [![Crates.io](https://img.shields.io/crates/v/pluginlab.svg)](https://crates.io/crates/pluginlab)
* [trippy](https://github.com/fujiapple852/trippy) - 网络诊断工具 [![构建徽章](https://github.com/fujiapple852/trippy/workflows/CI/badge.svg)](https://github.com/fujiapple852/trippy/actions/workflows/ci.yml)
* [tw93/Kaku](https://github.com/tw93/Kaku) - 专为 AI 编码而构建的快速、开箱即用的终端模拟器，具有零配置默认值、AI 助手集成和 WezTerm 兼容的 Lua 配置。仅限 macOS。
* [uutils/coreutils](https://github.com/uutils/coreutils) - GNU coreutils 的跨平台重写 [![CICD](https://github.com/uutils/coreutils/actions/workflows/CICD.yml/badge.svg)](https://github.com/uutils/coreutils/actions/workflows/CICD.yml)
* [watchexec](https://github.com/watchexec/watchexec) - 执行命令以响应文件修改
* [XAMPPRocky/tokei](https://github.com/XAMPPRocky/tokei) - 计算代码行数
* [ynqa/jnv](https://github.com/ynqa/jnv) - 使用 jq 的交互式 JSON 过滤器 [![ci](https://github.com/ynqa/jnv/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/ynqa/jnv/actions/workflows/ci.yml)
* [ynqa/logu](https://github.com/ynqa/logu) - 从（流式传输）非结构化日志消息中提取模式 [![ci](https://github.com/ynqa/logu/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/ynqa/logu/actions/workflows/ci.yml)
* [ynqa/sig](https://github.com/ynqa/sig) - 交互式 grep （用于流式传输） [![ci](https://github.com/ynqa/sig/actions/workflows/ci.yml/badge.svg)](https://github.com/ynqa/sig/actions/workflows/ci.yml)

### 任务调度

* [tasklet](https://github.com/stav121/tasklet) [[tasklet](https://crates.io/crates/tasklet)] - 用 Rust 编写的任务调度库！[构建状态](https://img.shields.io/github/actions/workflow/status/stav121/tasklet/rust.yml)

### 文本编辑器

* [amp](https://amp.rs) - 受到 Vi/Vim 的启发。
* [Ferrite](https://github.com/OlaProeis/Ferrite) - 使用 egui 构建的跨平台 Markdown 编辑器，具有实时预览、语法突出显示和美人鱼图等功能。
* [Fresh](https://github.com/sinelaw/fresh) - 易于使用、功能强大且快速的终端文本编辑器和 IDE，支持 TypeScript 插件。
* [gchp/iota](https://github.com/gchp/iota) - 一个简单的文本编辑器
* [helix](https://github.com/helix-editor/helix) - 受 Neovim/Kakoune 启发的后现代模态文本编辑器。 [![构建徽章](https://github.com/helix-editor/helix/actions/workflows/build.yml/badge.svg)](https://github.com/helix-editor/helix/actions)
* [ilai-deutel/kibi](https://github.com/ilai-deutel/kibi) - 一个小型（≤1024 LOC）文本编辑器，具有语法突出显示、增量搜索等功能。 [![构建徽章](https://github.com/ilai-deutel/kibi/actions/workflows/ci.yml/badge.svg)](https://github.com/ilai-deutel/kibi/actions?query=branch%3Amaster)
* [Inkwell](https://github.com/4worlds4w-svg/inkwell) - 使用 Tauri v2 构建的便携式、离线优先的 Markdown 编辑器。单一可执行文件，零遥测。
* [ki-editor/ki-editor](https://github.com/ki-editor/ki-editor) - 多光标组合模态编辑器
* [Lapce](https://github.com/lapce/lapce) - 具有后端的现代编辑器。从已停产的 [xi-editor](https://github.com/xi-editor/xi-editor) 中汲取灵感。
* [manyougz/velotype](https://github.com/manyougz/velotype) - 基于块的本机 Markdown 编辑器，具有所见即所得渲染和源编辑模式，基于 GPUI 构建，无需 WebView shell。
* [mathall/rim](https://github.com/mathall/rim) - 类似 Vim 的文本编辑器。
* [ox](https://github.com/curlpipe/ox) - 在您的终端中运行的独立 Rust 文本编辑器！
* [SoloMD](https://github.com/zhitongblog/solomd) - 具有实时预览功能的轻量级跨平台 Markdown 编辑器，使用 Tauri 2 构建。
* [vamolessa/pepper](https://git.sr.ht/~lessa/pepper) [[pepper](https://crates.io/crates/pepper)] - 一个固执己见的模式编辑器，用于简化终端的代码编辑
* [zed](https://github.com/zed-industries/zed) - 来自 Atom 和 Tree-sitter 的创建者的高性能多人代码编辑器。

### 文本处理

* [ashvardanian/stringzilla](https://github.com/ashvardanian/StringZilla) - 适用于 x86 AVX2 和 AVX-512 以及 Arm NEON 的 SIMD 加速字符串搜索、排序、编辑距离、对齐和生成器 [![crates.io](https://img.shields.io/crates/v/stringzilla.svg)](https://crates.io/crates/stringzilla)
* [brevity1swos/rgx](https://github.com/brevity1swos/rgx) [[rgx-cli](https://crates.io/crates/rgx-cli)] - 终端正则表达式调试器，具有实时匹配、逐步调试器、3 个引擎、代码生成和实时流过滤功能。 [![CI](https://github.com/brevity1swos/rgx/actions/workflows/ci.yml/badge.svg)](https://github.com/brevity1swos/rgx/actions/workflows/ci.yml)
* [cchexcode/complate](https://github.com/cchexcode/complate) - 一种终端内文本模板工具，旨在标准化消息（例如 GIT 提交）。 [![crates.io](https://img.shields.io/crates/v/complate.svg)](https://crates.io/crates/complate) [![crates.io](https://img.shields.io/crates/d/complate?label=crates.io%20downloads)](https://crates.io/crates/complate) [![build徽章](https://github.com/cchexcode/complate/actions/workflows/release.yml/badge.svg)](https://github.com/cchexcode/complate/actions)
* [dathere/qsv](https://github.com/dathere/qsv) [[qsv](https://crates.io/crates/qsv)] - 高性能 CSV 数据整理工具包。从 xsv 分叉，具有 34 多个附加命令及更多。 [![Linux 构建状态](https://github.com/dathere/qsv/actions/workflows/rust.yml/badge.svg)](https://github.com/dathere/qsv/actions/workflows/rust.yml) [![Windows 构建状态](https://github.com/dathere/qsv/actions/workflows/rust-windows.yml/badge.svg)](https://github.com/dathere/qsv/actions/workflows/rust-windows.yml) [![macOS 构建状态](https://github.com/dathere/qsv/actions/workflows/rust-macos.yml/badge.svg)](https://github.com/dathere/qsv/actions/workflows/rust-macos.yml)
* [dominikwilkowski/cfonts](https://github.com/dominikwilkowski/cfonts) [[cfonts](https://crates.io/crates/cfonts)] - 控制台的性感 ANSI 字体！[构建徽章](https://github.com/dominikwilkowski/cfonts/actions/workflows/testing.yml/badge.svg)
* [grex](https://github.com/pemistahl/grex) - 用于从用户提供的测试用例生成正则表达式的命令行工具和库
* [harehare/mq](https://github.com/harehare/mq) - 使用类似 jq 的语法处理 Markdown 的命令行工具和库 [![build badged](https://github.com/harehare/mq/actions/workflows/ci.yml/badge.svg)](https://github.com/harehare/mq/actions/workflows/ci.yml)
* [Lisprez/so_stupid_search](https://github.com/Lisprez/so_stupid_search) - 一个简单快速的人类字符串搜索工具
* [loki_text](https://github.com/roquess/loki_text) [[loki_text](https://crates.io/crates/loki_text)] - 具有模式搜索、文本转换和多种字符串搜索算法的字符串操作库（KMP、Boyer-Moore、Aho-Corasick 等）
* [Melody](https://github.com/yoav-lavi/melody) - 一种编译为正则表达式的语言，旨在更易于阅读和维护 [![构建徽章](https://github.com/yoav-lavi/melody/actions/workflows/rust.yml/badge.svg)](https://github.com/yoav-lavi/melody/actions/workflows/rust.yml) [![crates.io](https://img.shields.io/crates/v/melody_compiler?label=compiler)](https://crates.io/crates/melody_compiler)
* [micahkepe/jsongrep](https://github.com/micahkepe/jsongrep) [[jsongrep](https://crates.io/crates/jsongrep)] - 一个快速搜索 JSON、YAML、TOML 和其他序列化格式的工具，具有直观的路径查询语法。
* [phiresky/ripgrep-all](https://github.com/phiresky/ripgrep-all) - ripgrep，还可以搜索 PDF、电子书、Office 文档、zip、tar.gz 等。
* [ripgrep](https://crates.io/crates/ripgrep) - 结合了 The Silver Searcher 的可用性和 grep 的原始速度
* [ruplacer](https://github.com/your-tools/ruplacer) - 查找并替换源文件中的文本 [![运行测试](https://github.com/your-tools/ruplacer/actions/workflows/test.yml/badge.svg?branch=master)](https://github.com/your-tools/ruplacer/actions/workflows/test.yml)
* [scooter](https://github.com/thomasschafer/scooter) - 在终端中进行交互式查找和替换。
* [sd](https://crates.io/crates/sd) - 直观的查找和替换 CLI
* [sstadick/hck](https://github.com/sstadick/hck) - 更快、更有功能的替代 `cut` [![构建徽章](https://github.com/sstadick/hck/workflows/Check/badge.svg?branch=master)](https://github.com/sstadick/hck)
* [vishaltelangre/ff](https://github.com/vishaltelangre/ff) - 按名称查找文件 (ff)！
* [whitfin/bytelines](https://github.com/whitfin/bytelines) [[bytelines](https://crates.io/crates/bytelines)] - 将输入行读取为字节切片以提高效率。
* [whitfin/runiq](https://github.com/whitfin/runiq) - 从未排序的输入中过滤重复行的有效方法。
* [xsv](https://crates.io/crates/xsv) - 快速 CSV 命令行工具（切片、索引、选择、搜索、采样等）

### 公用事业

* [1History](https://github.com/localfirstapp/1History) - 用于将 Firefox/Chrome/Safari 历史记录备份到一个 SQLite 文件的命令行界面 [![Build Status](https://github.com/localfirstapp/1History/actions/workflows/CI.yml/badge.svg)](https://github.com/localfirstapp/1History/actions/workflows/CI.yml)
* [bloznelis/kbt](https://github.com/bloznelis/kbt) [[kbt](https://crates.io/crates/kbt)] - 用于键盘测试的简单 TUI 工具。
* [brycx/checkpwn](https://github.com/brycx/checkpwn) - Have I Been Pwned (HIBP) 命令行实用工具，可让您轻松检查受损的帐户和密码。
* [cartesiancs/vessel](https://github.com/cartesiancs/vessel) - 用于编排物理设备的 C2（命令与控制）软件。
* [dcapal](https://github.com/dcapal/dcapal) - DcaPal 是一款免费、无需注册的在线工具，可帮助您保持投资组合与平均成本投资的平衡。
* [Eoin-McMahon/Blindfold](https://github.com/Eoin-McMahon/Blindfold) [[Blindfold](https://crates.io/crates/blindfold)] - 一个简单的 CLI 工具，用于快速轻松地生成 `.gitignore` 文件。 [![build-badge](https://github.com/Eoin-McMahon/blindfold/actions/workflows/rust.yml/badge.svg)]([https://github.com/nix-community/nurl/actions/workflows/ci.yml](https://github.com/Eoin-McMahon/blindfold/actions/workflows/rust.yml))
* [Epic Asset Manager](https://github.com/AchetaGames/Epic-Asset-Manager) - 一个非官方客户端，用于安装虚幻引擎，下载和管理从 Epic Games Store 购买的资产、项目、插件和游戏。
* [evansmurithi/cloak](https://github.com/evansmurithi/cloak) - 命令行 OTP（一次性密码）身份验证器应用程序。 ![CI](https://github.com/evansmurithi/cloak/workflows/CI/badge.svg) [![构建徽章](https://ci.appveyor.com/api/projects/status/9mlfpfru3ng4c689/branch/master?svg=true)](https://ci.appveyor.com/project/evansmurithi/cloak)
* [fcsonline/tmux-thumbs](https://github.com/fcsonline/tmux-thumbs) - tmux-fingers 的闪电版本，像 vimium/vimperator 一样复制/粘贴 tmux。
* [gitlogue](https://github.com/unhappychoice/gitlogue) - 一个 TUI 屏幕保护程序，可在终端中可视化 Git 提交历史记录
* [guoxbin/dtool](https://github.com/guoxbin/dtool) - 一个有用的命令行工具集合，可协助开发，包括转换、编解码器、散列、加密等。
* [IvanWng97/pixtuoid](https://github.com/IvanWng97/pixtuoid) [[pixtuoid](https://crates.io/crates/pixtuoid)] - 终端像素艺术办公室，将克劳德代码会话实时可视化为动画同事。 [![CI](https://img.shields.io/github/actions/workflow/status/IvanWng97/pixtuoid/ci.yml?branch=main)](https://github.com/IvanWng97/pixtuoid/actions/workflows/ci.yml)
* [Linus-Mussmaecher/rucola](https://github.com/Linus-Mussmaecher/rucola) - 基于终端的 Markdown 笔记管理器。 [![Crate](https://img.shields.io/crates/v/rucola-notes.svg?logo=rust)](https://crates.io/crates/rucola-notes) [![构建状态](https://github.com/Linus-Mussmaecher/rucola/actions/workflows/continuous-testing.yml/badge.svg)](https://github.com/Linus-Mussmaecher/rucola/actions/workflows/continuous-testing.yml)
* [Mobslide](https://github.com/thewh1teagle/mobslide) - 桌面应用程序可将您的智能手机变成演示遥控器。
* [mprocs](https://github.com/pvolok/mprocs) - 用于运行多个进程的 TUI
* [mrjackwills/oxker](https://github.com/mrjackwills/oxker) [[oxker](https://crates.io/crates/oxker)] - 一个简单的 tui 来查看和控制 docker 容器。
* [nix-community/nix-init](https://github.com/nix-community/nix-init) - 通过哈希预取、依赖推断、许可证检测等功能从 URL 生成 Nix 包
* [nix-community/nix-melt](https://github.com/nix-community/nix-melt) - 类似 Ranger 的 flake.lock 查看器 [![build-badge](https://github.com/nix-community/nix-melt/actions/workflows/ci.yml/badge.svg)](https://github.com/nix-community/nix-melt/actions/workflows/ci.yml)
* [nix-community/nurl](https://github.com/nix-community/nurl) [[nurl](https://crates.io/crates/nurl)] - 从存储库 URL 生成 Nix fetcher 调用[![build-badge](https://github.com/nix-community/nurl/actions/workflows/ci.yml/badge.svg)](https://github.com/nix-community/nurl/actions/workflows/ci.yml)
* [nomino](https://github.com/yaa110/nomino) - 为开发人员提供的批量重命名实用程序
* [raftario/licensor](https://github.com/raftario/licensor) - 将许可证写入标准输出 [![GitHub Actions](https://github.com/raftario/licensor/actions/workflows/build.yml/badge.svg?branch=master)](https://github.com/raftario/licensor/actions/workflows/build.yml)
* [restsend/rustpbx](https://github.com/restsend/rustpbx) - 软件定义的 SIP 代理，包括注册、存在、b2bua。 Freeswitch/FreePBX 的替代品。
* [rust-parallel](https://github.com/aaronriekenberg/rust-parallel) - 使用 Tokio 并行执行命令的快速命令行应用程序。  与 GNU Parallel 或 xargs 类似的接口。 [![Crate](https://img.shields.io/crates/v/rust-parallel.svg?logo=rust)](https://crates.io/crates/rust-parallel) [![构建状态](https://github.com/aaronriekenberg/rust-parallel/actions/workflows/CI.yml/badge.svg)](https://github.com/aaronriekenberg/rust-parallel/actions/workflows/CI.yml)
* [rustdesk/rustdesk](https://github.com/rustdesk/rustdesk) - 远程桌面软件，TeamViewer 和 AnyDesk 的绝佳替代品。
* [rustic-rs/rustic](https://github.com/rustic-rs/rustic) [[rustic-rs](https://crates.io/crates/rustic-rs)] - 由 Rust 支持的快速、加密、重复数据删除备份。 [![版本](https://img.shields.io/crates/v/rustic-rs.svg)](https://crates.io/crates/rustic-rs)
* [ruvnet/RuView](https://github.com/ruvnet/RuView) - 使用 WiFi 信道状态信息 (CSI) 和机器学习的隐私保护人体姿势估计系统。
* [sorairolake/qrtool](https://github.com/sorairolake/qrtool) [[qrtool](https://crates.io/crates/qrtool)] - 用于编码和解码 QR 码图像的实用程序。 [![CI](https://github.com/sorairolake/qrtool/workflows/CI/badge.svg?branch=develop)](https://github.com/sorairolake/qrtool/actions?query=workflow%3ACI)
* [splashboard](https://github.com/unhappychoice/splashboard) [[splashboard](https://crates.io/crates/splashboard)] - 在 shell 启动和目录更改时呈现的可自定义终端启动画面，以及每个目录的仪表板[![CI](https://github.com/unhappychoice/splashboard/actions/workflows/ci.yml/badge.svg)](https://github.com/unhappychoice/splashboard/actions/workflows/ci.yml)
* [str4d/rage](https://github.com/str4d/rage) [[rage](https://crates.io/crates/rage)] - [age](https://github.com/FiloSottile/age) 的 Rust 实现。
* [suckit](https://github.com/Skallwar/suckit) - 递归访问网站内容并将其下载到您的磁盘上。 [![Crate](https://img.shields.io/crates/v/suckit.svg?logo=rust)](https://crates.io/crates/suckit) [![构建状态](https://github.com/Skallwar/suckit/workflows/Build%20and%20test/badge.svg)](https://github.com/Skallwar/suckit/blob/master/.github/workflows/build_and_test.yml)
* [Tabiew](https://github.com/shshemi/tabiew) - 用于查看和查询 CSV 文件的轻量级 TUI 应用程序。
* [Tail Tales](https://github.com/davidmoreno/tailtales) - 具有 logfmt 支持的 TUI 日志查看器。 [![板条箱](https://img.shields.io/crates/v/tailtales.svg?logo=rust)](https://crates.io/crates/tailtales)
* [television](https://github.com/alexpasmantier/television) - 一个超快的通用模糊查找器 TUI！[GitHub 分支检查运行](https://img.shields.io/github/check-runs/alexpasmantier/television/main)
* [Thoth](https://github.com/anitnilay20/thoth) - 高性能、功能丰富的桌面应用程序，用于查看和探索 JSON 和 NDJSON 文件，并具有基于 WASM 的插件支持。 [![CI](https://github.com/anilay20/thoth/workflows/CI/badge.svg)](https://github.com/anilay20/thoth/actions/workflows/ci.yml)
* [tversteeg/emplace](https://github.com/tversteeg/emplace) - 同步多台机器上安装的包
* [vamolessa/verco](https://github.com/vamolessa/verco) [[verco](https://crates.io/crates/verco)] - 一个简单的 Git/Hg tui 客户端，专注于键盘快捷键
* [vaultwarden](https://github.com/dani-garcia/vaultwarden#readme) [![Build](https://github.com/dani-garcia/vaultwarden/actions/workflows/build.yml/badge.svg)](https://github.com/dani-garcia/vaultwarden/actions/workflows/build.yml) - 用 Rust 编写的 Bitwarden 服务器 API 的替代实现
* [veirt/weathr](https://github.com/Veirt/weathr) [[weathr](https://crates.io/crates/weathr)] - 带有 ASCII 动画的终端天气应用程序。 [![发布](https://github.com/Veirt/weathr/actions/workflows/release.yml/badge.svg)](https://github.com/Veirt/weathr/actions/workflows/release.yml)
* [Vibe](https://github.com/thewh1teagle/vibe) - 在每个平台上以每种语言转录音频或视频。
* [warpdotdev/Warp](https://github.com/warpdotdev/Warp) - :heavy_dollar_sign: Warp 是一款速度极快的现代 GPU 加速终端，旨在提高您和您的团队的工作效率。
* [Water-Run/treepp](https://github.com/Water-Run/treepp) - 基于 Rust 的本机 Windows“树”替换，在成功运行时具有不同级别的输入/输出兼容性，还有更多功能，包括基本排除和“.gitignore”支持，以及数倍更快的性能。
* [wrestic](https://github.com/alvaro17f/wrestic) - Restic 的包装。
* [wthrr](https://github.com/ttytm/wthrr-the-weathercrab) - 航站楼的天气伴侣。 [![crates.io](https://img.shields.io/crates/v/wthrr?logo=rust)](https://crates.io/crates/wthrr)
* [YueMiyuki/Risuko](https://github.com/YueMiyuki/Risuko) - 功能齐全的下载管理器。 [![发布徽章](https://github.com/YueMiyuki/Risuko/actions/workflows/release.yml/badge.svg)](https://github.com/YueMiyuki/Risuko/actions/workflows/release.yml)

### 视频

* [dertuxmalwieder/yaydl](https://github.com/dertuxmalwieder/yaydl) [[yaydl](https://crates.io/crates/yaydl)] - 一个简单的视频下载器
* [gyroflow/gyroflow](https://github.com/gyroflow/gyroflow) - 使用陀螺仪数据的视频稳定应用
* [harlanc/xiu](https://github.com/harlanc/xiu) - 一个强大且安全的实时服务器（rtmp/httpflv/hls/relay）。 [![crates.io](https://img.shields.io/crates/v/xiu.svg)](https://crates.io/crates/xiu)
* [vidmerger](https://github.com/TGotwig/vidmerger) - 通过 CLI 合并视频和音频文件
* [xiph/rav1e](https://github.com/xiph/rav1e) - 最快、最安全的 AV1 编码器。

### 虚拟化

* [firecracker-microvm/firecracker](https://github.com/firecracker-microvm/firecracker) - 用于容器工作负载的轻量级虚拟机 [Firecracker Microvm](https://firecracker-microvm.github.io/)
* [kata-containers/kata-containers](https://github.com/kata-containers/kata-containers) - 轻量级虚拟机 (VM) 的实现，其感觉和执行方式类似于容器，但提供了 VM 的工作负载隔离和安全优势。
* [superradcompany/microsandbox](https://github.com/superradcompany/microsandbox) - 轻量级 microVM 沙盒库，用于在几毫秒内运行隔离的代码执行。支持 Rust、Python 和 TypeScript SDK 以及 OCI 兼容的容器映像。 [![GitHub 发布](https://img.shields.io/github/v/release/superradcompany/microsandbox?include_prereleases)](https://github.com/superradcompany/microsandbox/releases)
* [tailhook/vagga](https://github.com/tailhook/vagga) - 没有守护进程的容器化工具
* [youki-dev/youki](https://github.com/youki-dev/youki) - 容器运行时 [![构建徽章](https://github.com/youki-dev/youki/actions/workflows/basic.yml/badge.svg)](https://github.com/youki-dev/youki/actions)

### 网络

* [0xMassi/webclaw](https://github.com/0xMassi/webclaw) - 使用 TLS 指纹识别、MCP 服务器和无需浏览器的 LLM 进行 Web 内容提取 [![CI](https://github.com/0xMassi/webclaw/actions/workflows/ci.yml/badge.svg)](https://github.com/0xMassi/webclaw/actions)
* [agrinman/tunnelto](https://github.com/agrinman/tunnelto) [[tunnelto](https://crates.io/crates/tunnelto)] - 允许您通过公共 URL 公开本地运行的 Web 服务器。
* [cfal/tobaru](https://github.com/cfal/tobaru) - 具有白名单、IP 和 TLS SNI/ALPN 基于规则的路由、iptables 支持、循环转发（负载平衡）和热重载的端口转发器。
* [hook0/hook0](https://github.com/hook0/hook0) - 开源 Webhooks 即服务平台，使 SaaS 开发人员可以轻松发送 Webhooks
* [importantimport/hatsu](https://github.com/importantimport/hatsu) - 🩵 用于静态站点的自托管和全自动 ActivityPub 桥。 [![发布](https://github.com/importantimport/hatsu/actions/workflows/release.yml/badge.svg)](https://github.com/importantimport/hatsu/actions/workflows/release.yml)
* [janreges/siteone-crawler](https://github.com/janreges/siteone-crawler) [[siteone-crawler](https://crates.io/crates/siteone-crawler)] - 多合一
网站爬虫、审核器、离线存档器和具有 CI/CD 质量门控的 AI 就绪 Markdown 导出器
  [![CI](https://github.com/janreges/siteone-crawler/workflows/CI/badge.svg)](https://github.com/janreges/siteone-crawler/actions)
* [konippi/servo-fetch](https://github.com/konippi/servo-fetch) - 一个独立的浏览器引擎，可以以 Markdown、JSON 或屏幕截图的形式获取、渲染和提取 Web 内容 - 无需 Chromium，无需 API 密钥。 CLI、Python、MCP 服务器。 [![CI](https://github.com/konippi/servo-fetch/actions/workflows/ci.yml/badge.svg)](https://github.com/konippi/servo-fetch/actions/workflows/ci.yml)
* [LemmyNet/lemmy](https://github.com/LemmyNet/lemmy) - fediverse 的链接聚合器/reddit 克隆 [![Build Status](https://cloud.drone.io/api/badges/LemmyNet/lemmy/status.svg)](https://cloud.drone.io/LemmyNet/lemmy)
* [MASQ-Project/Node](https://github.com/MASQ-Project/Node) - MASQ Node 软件为全球用户提供了一个去中心化的网状节点网络，以访问正常的互联网内容 - Tor 和 VPN 之外的技术的下一步发展 [![构建徽章](https://github.com/MASQ-Project/Node/actions/workflows/ci-matrix.yml/badge.svg)](https://github.com/MASQ-Project/Node/actions)
* [Plume-org/Plume](https://github.com/Plume-org/Plume) - ActivityPub 联合博客应用程序
* [Redlib](https://github.com/redlib-org/redlib) - Reddit 的替代私有前端，起源于 [Libreddit](https://github.com/libreddit/libreddit)
* [shouya/rss-funnel](https://github.com/shouya/rss-funnel) - 模块化 RSS 处理管道系统。
* [SinTan1729/Chhoto URL](https://github.com/SinTan1729/chhoto-url) - 一个简单、快速、自托管的 URL 缩短器，没有不必要的功能。[![release](https://github.com/SinTan1729/chhoto-url/actions/workflows/docker-release.yml/badge.svg)](https://github.com/SinTan1729/chhoto-url/actions/workflows/docker-release.yml)
* [Stoatchat](https://github.com/stoatchat/stoatchat) - 采用现代网络技术构建的用户至上的聊天平台。
* [zhom/donutbrowser](https://github.com/zhom/donutbrowser) - 开源反检测浏览器，具有无限的隔离配置文件、Chromium/Firefox 引擎、指纹欺骗、代理/VPN 支持、本地 API 和 MCP 服务器以及 E2E 加密云同步。 [![GitHub 发布](https://img.shields.io/github/v/release/zhom/donutbrowser)](https://github.com/zhom/donutbrowser/releases)

### 网络服务器

* [cloudflare/pingora](https://github.com/cloudflare/pingora) - 用于构建快速、可靠和可发展的网络服务的库。
* [emanuele-em/proxelar](https://github.com/emanuele-em/proxelar) - MITM 代理🦀！具有 SSL/TLS 功能的 HTTP/1、HTTP/2 和 WebSocket 工具包 [![Rust](https://github.com/emanuele-em/proxelar/actions/workflows/autofix.yml/badge.svg)](https://github.com/emanuele-em/proxelar/actions)
* [g3proxy](https://github.com/bytedance/g3) - 正向代理服务器，支持代理链、协议检查、MITM拦截、ICAP适配、透明代理 [![CodeCoverage](https://github.com/bytedance/g3/actions/workflows/codecov.yml/badge.svg)](https://github.com/bytedance/g3/actions)
* [Mini RPS](https://github.com/marcodpt/minirps) - 迷你反向代理服务器、HTTPS、CORS、静态文件托管和模板引擎 (minijinja) [crates.io](https://crates.io/crates/minirps)
* [mu-arch/skyfolder](https://github.com/mu-arch/skyfolder) - 🪂 漂亮的 HTTP/Bittorrent 服务器，没有任何麻烦。安全 - GUI - 漂亮 - 快速
* [mufeedvh/binserve](https://github.com/mufeedvh/binserve) - 一个极快的静态 Web 服务器，在单个二进制文件中提供路由、模板和安全性，您可以使用零代码进行设置 [![构建徽章](https://github.com/mufeedvh/binserve/actions/workflows/build.yml/badge.svg)](https://github.com/mufeedvh/binserve/actions)
* [orhun/rustypaste](https://github.com/orhun/rustypaste) - 一个最小的文件上传/pastebin服务！[https://github.com/orhun/rustypaste/actions](https://img.shields.io/github/actions/workflow/status/orhun/rustypaste/ci.yml?branch=master&label=build)
* [plabayo/rama](https://github.com/plabayo/rama) - 用于移动和转换网络数据包的模块化服务框架，用于构建 Web 客户端、服务器，以及最重要的代理
* [ronanyeah/rust-hasura](https://github.com/ronanyeah/rust-hasura) - 演示如何使用 [Hasura](https://hasura.io/) ![Rust](https://github.com/ronanyeah/rust-hasura/workflows/Rust/badge.svg?branch=master) 将 GraphQL 服务器用作远程模式
* [static-web-server](https://github.com/static-web-server/static-web-server) - 用于静态文件服务的超快异步 Web 服务器。 ⚡ [![CI](https://github.com/static-web-server/static-web-server/actions/workflows/devel.yml/badge.svg)](https://github.com/static-web-server/static-web-server/actions/workflows/devel.yml?query=branch%3Amaster)
* [svenstaro/miniserve](https://github.com/svenstaro/miniserve) - 一个小型、独立的跨平台 CLI 工具，允许您获取二进制文件并通过 HTTP 提供一些文件 [![构建徽章](https://github.com/svenstaro/miniserve/workflows/CI/badge.svg?branch=master)](https://github.com/svenstaro/miniserve/actions)
* [thecoshman/http](https://github.com/thecoshman/http) - 请托管这些东西 - 一个基本的 http 服务器，用于快速、简单地托管文件夹
* [TheWaWaR/simple-http-server](https://github.com/TheWaWaR/simple-http-server) - 简单的静态http服务器
* [vetis-server/vetis](https://github.com/vetis-server/vetis) - 专为现代 Rust 应用程序构建的速度极快、简约的 HTTP 服务器。提供虚拟主机、SNI、静态内容、反向代理、HTTP 1/2/3 和 Tokio 或 Smol 作为异步运行时！
* [vproxy/0x676e67](https://github.com/0x676e67/vproxy) - 快速异步 Rust HTTP/Socks5 代理

### 工作流程自动化

* [cowork-forge](https://github.com/sopaco/cowork-forge) - AI 原生多代理平台，通过 7 阶段管道协调专业代理，将想法转化为可生产的软件。 [![发布](https://img.shields.io/github/actions/workflow/status/sopaco/cowork-forge/rust.yml?label=Build)](https://github.com/sopaco/cowork-forge/actions/workflows/release.yml)
* [dali-benothmen/cronflow](https://github.com/dali-benothmen/cronflow) - Cronflow 是一个高性能、以开发人员为中心的工作流自动化库，可让您完全用代码构建和编排复杂的、可扩展的自动化工作流。 [![发布](https://github.com/dali-benothmen/cronflow/actions/workflows/release.yml/badge.svg)](https://github.com/dali-benothmen/cronflow/actions/workflows/release.yml)
* [SouravRoy-ETL/duckle](https://github.com/SouravRoy-ETL/duckle) - 完全在 DuckDB 上运行的视觉优先的开源数据工作室 (ETL/ELT)。将源、转换和接收器拖到画布上，然后将其编译为纯 DuckDB SQL； 300 多个连接器和内置 MCP 服务器。 [![发布](https://github.com/SouravRoy-ETL/duckle/actions/workflows/release.yml/badge.svg)](https://github.com/SouravRoy-ETL/duckle/actions/workflows/release.yml)

## 开发工具

* [7df-lab/devo](https://github.com/7df-lab/devo) - 一种轻量级、模型中立的编码代理，作为单个二进制文件运行。快速、代币高效且高度可定制。 [![CI](https://github.com/7df-lab/devo/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/7df-lab/devo/actions/workflows/ci.yml)
* [aaif-goose/goose](https://github.com/aaif-goose/goose) - 一个开源的本地人工智能代理，可自动执行工程任务。
* [armgabrielyan/deadbranch](https://github.com/armgabrielyan/deadbranch) [[deadbranch](https://crates.io/crates/deadbranch)] - 安全清理过时的 git 分支[![CI](https://github.com/armgabrielyan/deadbranch/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/armgabrielyan/deadbranch/actions/workflows/ci.yml)
* [ATAC](https://github.com/Julien-cpsn/ATAC) - 用 Rust 制作的功能齐全的 TUI API 客户端。 ATAC 是免费、开源、离线且无账户的。
* [bacon](https://github.com/Canop/bacon) - 后台 Rust 代码检查器，类似于 Cargo-Watch
* [biome](https://github.com/biomejs/biome) - 用于网络项目的工具链，旨在提供维护它们的功能。 Biome 提供格式化程序和 linter，可通过 CLI 和 LSP 使用
* [cachix/devenv](https://github.com/cachix/devenv) - 使用 Nix 的快速、声明性、可重现和可组合的开发环境 [![CI](https://github.com/cachix/devenv/actions/workflows/release.yml/badge.svg)](https://github.com/cachix/devenv/actions/workflows/release.yml)
* [claudectl](https://github.com/mercurialsolo/claudectl) [[claudectl](https://crates.io/crates/claudectl)] - 使用本地 LLM 大脑 (ollama/llama.cpp/vLLM) 自动驾驶 Claude 代码，学习自动批准/拒绝工具调用。多会话编排、健康监控、支出控制。 [![CI](https://github.com/mercurialsolo/claudectl/actions/workflows/ci.yml/badge.svg)](https://github.com/mercurialsolo/claudectl/actions/workflows/ci.yml)
* [clippy](https://crates.io/crates/clippy) - 锈屑
* [clog-tool/clog-cli](https://github.com/clog-tool/clog-cli) - 从 git 元数据生成变更日志（[传统变更日志](https://blog.thoughtram.io/announcements/tools/2014/09/18/announcing-clog-a-conventional-changelog-generator-for-the-rest-of-us.html)）
* [cloudflare/foundations](https://github.com/cloudflare/foundations) - Foundations 是一个模块化 Rust 库，旨在帮助扩展分布式生产级系统的程序。
* [comtrya](https://github.com/comtrya/comtrya) - 用于 localhost / dotfiles 的配置管理工具 [![构建徽章](https://github.com/comtrya/comtrya/actions/workflows/main.yaml/badge.svg)](https://github.com/comtrya/comtrya/actions)
* [create-rust-app](https://github.com/Wulf/create-rust-app) - 通过运行一个命令来设置现代 rust+react Web 应用程序。 [![crate](https://img.shields.io/crates/v/create-rust-app.svg)](https://crates.io/crates/create-rust-app)
* [dan-t/rusty-tags](https://github.com/dan-t/rusty-tags) - 为货物项目及其所有依赖项创建 ctags/etags
* [datanymizer/datanymizer](https://github.com/datanymizer/datanymizer) - 具有灵活规则的强大数据库匿名器 [![构建徽章](https://github.com/datanymizer/datanymizer/workflows/CI/badge.svg?branch=main)](https://github.com/datanymizer/datanymizer/actions?query=workflow%3ACI+branch%3Amain)
* [delta](https://crates.io/crates/git-delta) - 用于 git 和 diff 输出的语法荧光笔[![构建徽章](https://github.com/dandavison/delta/actions/workflows/ci.yml/badge.svg)](https://github.com/dandavison/delta//actions)
* [dotenv-linter](https://github.com/dotenv-linter/dotenv-linter) - `.env` 文件的 Linter [![构建徽章](https://github.com/dotenv-linter/dotenv-linter/actions/workflows/ci.yml/badge.svg)](https://github.com/dotenv-linter/dotenv-linter/actions?query=workflow%3ACI+branch%3Amaster)
* [envio](https://github.com/humblepenguinn/envio) - 用于管理环境变量的现代且安全的 CLI 工具 [![构建徽章](https://github.com/humblepenguinn/envio/actions/workflows/CICD.yml/badge.svg?branch=main)](https://github.com/humblepenguinn/envio/actions/workflows/CICD.yml)
* [Feel-ix-343/markdown-oxide](https://github.com/Feel-ix-343/markdown-oxide) - PKM Markdown 语言服务器，支持 Neovim、VSCode、Zed、Helix 和 Kakoune 的黑曜石风格 wiki 链接、反向链接和每日笔记
* [Flox](https://github.com/flox/flox) - Flox 是一个集虚拟环境和包管理器于一体的产品。
* [forgecode](https://github.com/tailcallhq/forgecode) - 基于终端的 AI 对编程器，用于代码生成和编辑。 [![网站](https://img.shields.io/badge/website-forgecode.dev-blue)](https://forgecode.dev/)
* [frolic](https://github.com/frolicflow/Frolic) - API 层可将构建面向客户的仪表板速度提高 10 倍
* [fw](https://github.com/brocode/fw) - 工作区生产力助推器 [![Rust](https://github.com/brocode/fw/actions/workflows/rust.yml/badge.svg)](https://github.com/brocode/fw/actions/workflows/rust.yml)
* [fzf-make](https://github.com/kyu08/fzf-make) [[fzf-make](https://crates.io/crates/fzf-make)] - 一个命令行工具，使用带预览窗口的模糊查找器执行 make 目标。 [![crates.io](https://img.shields.io/crates/v/fzf-make?style=flatflat-square)](https://crates.io/crates/fzf-make)
* [geiger](https://github.com/geiger-rs/cargo-geiger) - 一个程序，列出与板条箱中不安全代码的使用相关的统计信息及其所有依赖项 [![Build状态](https://dev.azure.com/cargo-geiger/cargo-geiger/_apis/build/status/geiger-rs.cargo-geiger?branchName=master)](https://dev.azure.com/cargo-geiger/cargo-geiger/_build/latest?definitionId=1&branchName=master)
* [git-cliff](https://github.com/orhun/git-cliff) - 高度可定制的变更日志生成器，遵循常规提交规范！[https://github.com/orhun/git-cliff/actions](https://img.shields.io/github/actions/workflow/status/orhun/git-cliff/ci.yml?branch=main&label=build)
* [git-journal](https://github.com/saschagrunert/git-journal/) - Git 提交消息和变更日志生成框架
* [git-time-machine](https://github.com/dinakars777/git-time-machine) - 用于撤销 git 错误的可视化 git reflog TUI [![crate](https://img.shields.io/crates/v/git-time-machine.svg)](https://crates.io/crates/git-time-machine) [![build徽章](https://github.com/dinakars777/git-time-machine/actions/workflows/rust.yml/badge.svg)](https://github.com/dinakars777/git-time-machine/actions/workflows/rust.yml)
* [GiticideLabs/giticide](https://github.com/GiticideLabs/gitride) [[gix](https://crates.io/crates/gix)] - Pure-Rust Git 实现，具有高性能管道箱和 CLI 工具，用于克隆、获取、状态、差异、提交、配置、引用等。 [![CI](https://github.com/GiticideLabs/giticide/workflows/ci/badge.svg)](https://github.com/GiticideLabs/giticide/actions)
* [hot-lib-reloader](https://github.com/rksm/hot-lib-reloader-rs) - 热重载 Rust 代码 [![构建徽章](https://github.com/rksm/hot-lib-reloader-rs/actions/workflows/ci.yml/badge.svg)](https://github.com/rksm/hot-lib-reloader-rs/actions/workflows/ci.yml)
* [intelli-shell](https://github.com/lasantosr/intelli-shell) - 使用占位符为命令添加书签，并随时搜索或自动完成 [![crate](https://img.shields.io/crates/v/intelli-shell.svg)](https://crates.io/crates/intelli-shell) [![build徽章](https://github.com/lasantosr/intelli-shell/actions/workflows/release.yml/badge.svg)](https://github.com/lasantosr/intelli-shell/actions/workflows/release.yml)
* [j178/prek](https://github.com/j178/prek) - 一种更快、无依赖、直接替代预提交的方法，用 Rust 编写。
* [jj-vcs/jj](https://github.com/jj-vcs/jj) - 与 Git 兼容的版本控制系统，具有干净的 CLI、一流的冲突处理和自动变基 [![Release](https://img.shields.io/github/v/release/martinvonz/jj)](https://github.com/jj-vcs/jj/releases)
* [just](https://github.com/casey/just) - 用于特定于项目的任务的便捷命令运行程序
* [mask](https://github.com/jacobdeichert/mask) - 由简单的 markdown 文件定义的 CLI 任务运行器 [![build badged](https://github.com/jacobdeichert/mask/workflows/CI/badge.svg?branch=master)](https://github.com/jacobdeichert/mask/actions?query=workflow%3ACI)
* [mise](https://github.com/jdx/mise) [[mise](https://crates.io/crates/mise)] - 多语言工具版本管理器和任务运行器； asdf 的直接替代品，具有更快的性能。 [![构建徽章](https://github.com/jdx/mise/actions/workflows/test.yml/badge.svg)](https://github.com/jdx/mise/actions/workflows/test.yml)
* [Module Linker](https://github.com/fiatjaf/module-linker) - 添加“<a>”链接到 GitHub 上“mod”、“use”和“extern crate”语句中引用的扩展。
* [Muvon/octocode](https://github.com/Muvon/octocode) [[octocode](https://crates.io/crates/octocode)] - 带有 GraphRAG 知识图和 MCP 服务器的语义代码索引器。 Tree-sitter AST 解析、ast-grep 结构搜索、LanceDB 向量存储、代码签名视图。 CLI + MCP 服务器模式，适用于 Claude/Cursor/Windsurf 等 AI 助手。 [![CI](https://github.com/Muvon/octocode/actions/workflows/ci.yml/badge.svg)](https://github.com/Muvon/octocode/actions/workflows/ci.yml)
* [ptags](https://github.com/dalance/ptags) - git 存储库的并行通用 ctags 包装器
* [Racer](https://github.com/racer-rust/racer) - Rust 的代码完成
* [reflex-search/reflex](https://github.com/reflex-search/reflex) [[reflex-search](https://crates.io/crates/reflex-search)] - 用于 AI 编码代理的本地优先全文代码搜索引擎。 Trigram 索引、低于 100 毫秒的查询、MCP 服务器模式、通过树管理员支持 18 种语言。
* [Rust Search Extension](https://github.com/huhu/rust-search-extension) - 一个方便的浏览器扩展，用于在地址栏（多功能框）中搜索包和文档。 [![构建状态](https://github.com/huhu/rust-search-extension/workflows/build/badge.svg?branch=master)](https://github.com/huhu/rust-search-extension/actions)
* [Rustup](https://github.com/rust-lang/rustup) - Rust 工具链安装程序 [![构建徽章](https://github.com/rust-lang/rustup/actions/workflows/ci.yaml/badge.svg)](https://github.com/rust-lang/rustup/actions)
* [scriptisto](https://github.com/igor-petruk/scriptisto) - 一种与语言无关的“shebang 解释器”，使您能够用编译语言编写一个文件脚本。 [![构建状态](https://cloud.drone.io/api/badges/igor-petruk/scriptisto/status.svg)](https://cloud.drone.io/igor-petruk/scriptisto)
* [typos](https://github.com/crate-ci/typos) [[typos-cli](https://crates.io/crates/typos-cli)] - 源代码拼写检查器
* [voidzero-dev/vite-plus](https://github.com/voidzero-dev/vite-plus) - 一个统一的 Web 开发工具链，将 Vite、Vitest、Oxlint、Rolldown 等组合到单个 Rust 支持的 CLI (`vp`) 中
* [VT Code](https://crates.io/crates/vtcode) - 终端编码代理将现代 TUI 与由 tree-sitter 和 ast-grep 提供支持的深度语义代码理解相结合。
* [Wilfred/difftastic](https://github.com/Wilfred/difftastic) [[difftastic](https://crates.io/crates/difftastic)] - 一个理解语法的结构 diff 工具，支持 30 多种编程语言
* [yvgude/lean-ctx](https://github.com/yvgude/lean-ctx) [[lean-ctx](https://crates.io/crates/lean-ctx)] - AI编码代理的上下文运行时：MCP服务器和shell钩子，用于压缩工具和终端输出以减少LLM令牌的使用；树守护者解析、会话缓存。 [![CI](https://github.com/yvgude/lean-ctx/actions/workflows/ci.yml/badge.svg)](https://github.com/yvgude/lean-ctx/actions/workflows/ci.yml)

### 构建系统

* [better-fullstack](https://github.com/Marve10s/Better-Fullstack) - 支持 Rust（Axum、Actix Web、Leptos、Dioxus、SeaORM、SQLx、tonic、async-graphql）以及 TypeScript、Go 和 Python 的端到端全栈脚手架工具 — 为您或您的 AI 代理准备好代码。
* [Cargo](https://crates.io/) - Rust 包管理器
  * [cargo-all-features](https://github.com/frewsxcv/cargo-all-features) - 一个可配置的子命令，用于简化所有功能组合的测试、构建等等
  * [cargo-benchcmp](https://crates.io/crates/cargo-benchcmp) - 比较微基准的实用程序
* [cargo-bins/cargo-binstall](https://github.com/cargo-bins/cargo-binstall) [[cargo-binstall](https://crates.io/crates/cargo-binstall)] - Rust 箱子的快速二进制安装程序，获取预构建的工件而不是从源代码编译[![CI](https://github.com/cargo-bins/cargo-binstall/actions/workflows/ci.yml/badge.svg)](https://github.com/cargo-bins/cargo-binstall/actions)
  * [cargo-bitbake](https://crates.io/crates/cargo-bitbake) - 一个可以利用 meta-rust 中的类生成 BitBake 配方的货物扩展
  * [cargo-cache](https://crates.io/crates/cargo-cache) - 检查/管理/清理你的货物缓存（`~/.cargo/`/`${CARGO_HOME}`），打印尺寸等[！[构建状态]（https://github.com/matthiaskrgr/cargo-cache/workflows/ci/badge.svg?branch=master）]（https://github.com/matthiaskrgr/cargo-cache/actions）
  * [cargo-check](https://crates.io/crates/cargo-check) - “cargo rustc -- -Zno-trans”的包装器，如果您只需要正确性检查，则有助于运行更快的编译
  * [cargo-commander](https://crates.io/crates/cargo-commander) - `cargo` 运行 CLI 命令的子命令类似于 `package.json` 中脚本部分的工作方式 [![构建和测试](https://github.com/simonhyll/cargo-commander/actions/workflows/build.yml/badge.svg)](https://github.com/simonhyll/cargo-commander/actions/workflows/build.yml)
  * [cargo-count](https://crates.io/crates/cargo-count) - 列出有关货运项目的源代码计数和详细信息，包括不安全的统计数据
  * [cargo-deb](https://crates.io/crates/cargo-deb) - 生成二进制 Debian 软件包
  * [cargo-depgraph](https://crates.io/crates/cargo-depgraph) - 使用货物元数据和 graphviz 为货物项目创建依赖关系图
  * [cargo-do](https://crates.io/crates/cargo-do) - 连续运行多个货物命令
  * [cargo-ebuild](https://crates.io/crates/cargo-ebuild) - 可以使用树内 eclass 生成 ebuild 的货物扩展
  * [cargo-edit](https://crates.io/crates/cargo-edit) - 允许您通过从命令行读取/写入 Cargo.toml 文件来添加和列出依赖项
  * [cargo-generate](https://github.com/cargo-generate/cargo-generate) - 利用预先存在的 git 存储库作为模板来生成 Rust 项目。
  * [cargo-info](https://crates.io/crates/cargo-info) - 从命令行查询 crates.io 以获取 crate 详细信息
  * [cargo-license](https://crates.io/crates/cargo-license) - 一个 Cargo 子命令，用于快速查看所有依赖项的许可证。
  * [cargo-limit](https://crates.io/crates/cargo-limit) - 噪音较小的货物：跳过警告，直到修复错误、Neovim 集成等。
  * [cargo-make](https://crates.io/crates/cargo-make) - 任务运行器和构建工具。 [![构建徽章](https://github.com/sagiegurari/cargo-make/workflows/CI/badge.svg?branch=master)](https://github.com/sagiegurari/cargo-make/actions)
  * [cargo-modules](https://crates.io/crates/cargo-modules) - 一个货物插件，用于显示板条箱模块的树状概述。
  * [cargo-multi](https://crates.io/crates/cargo-multi) - 在多个箱子上运行指定的货物命令
  * [cargo-outdated](https://crates.io/crates/cargo-outdated) - 当较新版本的 Rust 依赖项可用或过时时显示
* [cargo-rdme](https://github.com/orium/cargo-rdme) [[cargo-rdme](https://crates.io/crates/cargo-rdme)] - Cargo 子命令，用于根据 crate 的文档创建 README。 [![构建徽章](https://github.com/orium/cargo-rdme/workflows/CI/badge.svg)](https://github.com/orium/cargo-rdme/actions?query=workflow%3ACI)
  * [cargo-release](https://crates.io/crates/cargo-release) - 用于发布 git 管理的货物项目、构建、标记、发布、文档和推送的工具 [![Rust](https://github.com/crate-ci/cargo-release/actions/workflows/ci.yml/badge.svg)](https://github.com/crate-ci/cargo-release/actions/workflows/rust.yml)
  * [cargo-script](https://crates.io/crates/cargo-script) - 让人们快速轻松地运行 Rust“脚本”，从而利用 Cargo 的包生态系统
* [cargo-udeps](https://github.com/est31/cargo-udeps) [[cargo-udeps](https://crates.io/crates/cargo-udeps)] - 查找未使用的依赖项
  * [cargo-update](https://crates.io/crates/cargo-update) - 货物子命令，用于检查和应用已安装的可执行文件的更新
  * [cargo-watch](https://crates.io/crates/cargo-watch) - 当源发生变化时，cargo 编译项目的实用程序
  * [dtolnay/cargo-expand](https://github.com/dtolnay/cargo-expand) - 扩展源代码中的宏
* CMake
  * [Devolutions/CMakeRust](https://github.com/Devolutions/CMakeRust) - 对于将 Rust 库集成到 CMake 项目中非常有用
  * [SiegeLord/RustCMake](https://github.com/SiegeLord/RustCMake) - 一个示例项目，展示了 CMake 与 Rust 的用法
* [facebook/buck2](https://github.com/facebook/buck2) - [Buck2](https://buck2.build/) 是一个用 Rust 构建的大型构建工具
* [Fleet](https://github.com/suptejas/fleet) [[fleet-rs](https://crates.io/crates/fleet-rs)] - Rust 的快速构建工具。
* GitHub 操作
  * [icepuma/rust-action](https://github.com/icepuma/rust-action) - Rust github 操作
* [Nix](https://nixos.org/)
  * [nix-community/fenix](https://github.com/nix-community/fenix) - 适用于 nix 的 Rust 工具链和 rust 分析器每晚 [![build-badge](https://github.com/nix-community/fenix/actions/workflows/ci.yml/badge.svg)](https://github.com/nix-community/fenix/actions/workflows/ci.yml)
* [pantsbuild/pants](https://github.com/pantsbuild/pants) - [Pants](https://www.pantsbuild.org/) 是一个快速、可扩展、用户友好的构建系统，适用于用 Rust 构建的各种规模的代码库。
* [rolldown/rolldown](https://github.com/rolldown/rolldown) - 用 Rust 编写的 JavaScript/TypeScript 捆绑器旨在充当 Vite 中未来的捆绑器。
* [tracemachina/nativelink](https://github.com/TraceMachina/nativelink) - [NativeLink](https://www.nativelink.com) 是一个用 Rust 编写的后端远程执行平台，适用于客户端构建系统，例如 [Buck2](https://buck2.build/)、[Bazel](https://bazel.build/)、[Pants](https://www.pantsbuild.org/) 等。 [![OpenSSF记分卡](https://api.securityscorecards.dev/projects/github.com/TraceMachina/nativelink/badge)](https://securityscorecards.dev/viewer/?uri=github.com/TraceMachina/nativelink) [![OpenSSF 最佳实践](https://www.bestpractices.dev/projects/8050/badge)](https://www.bestpractices.dev/projects/8050)
* [vercel/turborepo](https://github.com/vercel/turborepo) - 用于 JavaScript 和 TypeScript monorepos 的高性能构建系统，用 Rust 编写。具有增量计算、远程缓存和并行任务执行的特点。

### 调试

* 广东发展局
  * [gdbgui](https://github.com/cs01/gdbgui) - 基于浏览器的 gdb 前端，用于调试 C、C++、Rust 和 go。
* [godzie44/BugStalker](https://github.com/godzie44/BugStalker) - 适用于 Linux x86-64 的现代调试器。用 Rust 编写，用于 Rust 程序。
* [kxxt/tracexec](https://github.com/kxxt/tracexec) [[tracexec](https://crates.io/crates/tracexec)] - execve{,at} 和预执行行为的跟踪器，调试器的启动器。
* LLDB
  * [CodeLLDB](https://marketplace.visualstudio.com/items?itemName=vadimcn.vscode-lldb) - [Visual Studio Code](https://code.visualstudio.com/) 的 LLDB 扩展。

### 部署

* 码头工人
  * [emk/rust-musl-builder](https://github.com/emk/rust-musl-builder) - 用于使用 musl-libc 和 musl-gcc 编译静态 Rust 二进制文件的 Docker 映像，以及有用的 C 库的静态版本
  * [kpcyrd/mini-docker-rust](https://github.com/kpcyrd/mini-docker-rust) - 非常小的 Rust docker 镜像的示例项目
  * [liuchong/docker-rustup](https://github.com/liuchong/docker-rustup) - 多版本（带有 musl 工具）Rust Docker 镜像
  * [LukeMathWalker/cargo-chef](https://github.com/LukeMathWalker/cargo-chef) - 用于缓存 Docker 构建之间的编译远程依赖关系的工具和预构建映像。
  * [moghtech/komodo](https://github.com/moghtech/komodo) - 一种跨多个服务器构建和部署软件的工具，具有 Web UI、API，并且没有服务器限制
  * [rust-cross/rust-musl-cross](https://github.com/rust-cross/rust-musl-cross) - 用于使用 musl-cross 编译静态 Rust 二进制文件的 Docker 映像 [![Build](https://github.com/rust-cross/rust-musl-cross/workflows/Build/badge.svg)](https://github.com/rust-cross/rust-musl-cross/actions?query=workflow%3ABuild)
  * [rust-lang/docker-rust](https://github.com/rust-lang/docker-rust) - 官方 Rust Docker 镜像
  * [Stavrospanakakis/is_ready](https://github.com/Stavrospanakakis/is_ready) - 等待多个服务可用！[构建](https://github.com/Stavrospanakakis/is_ready/actions/workflows/release.yml/badge.svg)
*赫罗库
  * [emk/heroku-buildpack-rust](https://github.com/emk/heroku-buildpack-rust) - Heroku 上 Rust 应用程序的构建包
* [release-plz](https://github.com/release-plz/release-plz) [[release-plz](https://crates.io/crates/release-plz)] - 从 CI 中发布 crate，并生成变更日志和 semver 检查。 [![构建徽章](https://github.com/release-plz/release-plz/workflows/CI/badge.svg)](https://github.com/release-plz/release-plz/actions)

### 嵌入式

[Rust Embedded](https://rust-embedded.org/) 专注于改善在资源受限环境和非传统平台中使用 Rust 的端到端体验。请参阅 [awesome-embedded-rust](https://github.com/rust-embedded/awesome-embedded-rust) 以获取精选的、更扩展的嵌入式 Rust 资源列表。

* 阿杜伊诺
  * [avr-rust/ruduino](https://github.com/avr-rust/ruduino) - Arduino Uno 的可重复使用组件。
* 交叉编译
  * [japaric/rust-cross](https://github.com/japaric/rust-cross) - 关于交叉编译 Rust 程序您需要了解的一切
  * [japaric/xargo](https://github.com/japaric/xargo) - 将 Rust 程序轻松交叉编译为自定义裸机目标，例如 ARM Cortex-M
* 开发工具
* [probe-rs/probe-rs](https://github.com/probe-rs/probe-rs) [[probe-rs-tools](https://crates.io/crates/probe-rs-tools)] - 用于刷新和调试 ARM 和 RISC-V 微控制器的嵌入式调试工具包。
  * [Vaishnav-Sabari-Girish/ComChan](https://github.com/Vaishnav-Sabari-Girish/ComChan) - 带有绘图仪 TUI 的最小串行监视器。
* 乐鑫
  * [esp-rs](https://github.com/esp-rs) - 是许多社区项目的所在地，支持在 Espressif Systems 生产的各种 SoC 和模块上使用 Rust 编程语言。
* 固件
  * [oreboot/oreboot](https://github.com/oreboot/oreboot) - oreboot 是 coreboot 的一个分支，删除了 C，用 Rust 编写
* 射频
  * [nrf-rs/nrf-hal](https://github.com/nrf-rs/nrf-hal) - 适用于 nRF 系列设备的 Rust HAL

### 外国金融机构

另请参阅[外部函数接口](https://doc.rust-lang.org/book/first-edition/ffi.html)、[The Rust FFI Omnibus](http://jakegoulding.com/rust-ffi-omnibus/)（使用其他语言的 Rust 编写的代码的示例集合）和[用 Rust 编写的 FFI 示例](https://github.com/alexcrichton/rust-ffi-examples)。

* C
  * [gtk-rs/gir](https://github.com/gtk-rs/gir) - 用于从基于 GObject 的 C 库创建安全 Rust 绑定的代码生成器。
  * [mozilla/cbindgen](https://github.com/mozilla/cbindgen) - 从 Rust 源文件生成 C 头文件。在 Gecko 中用于 WebRender
  * [Sean1708/rusty-cheddar](https://github.com/Sean1708/rusty-cheddar) - 从 Rust 源文件生成 C 头文件
* C#
  * [csbindgen](https://github.com/Cysharp/csbindgen) - 为 Rust 源文件生成 C# 绑定
* C++
  * [dtolnay/cxx](https://github.com/dtolnay/cxx) - Rust 和 C++ 之间的安全互操作 [![构建徽章](https://img.shields.io/badge/github-dtolnay/cxx-8da0cb?style=for-the-badge&labelColor=555555&logo=github)](https://github.com/dtolnay/cxx)
  * [rust-cpp](https://crates.io/crates/cpp) - 将 C++ 代码直接嵌入 Rust 中。 [![构建状态](https://ci.appveyor.com/api/projects/status/uu76vmcrwnjqra0u/branch/master?svg=true)](https://ci.appveyor.com/project/mystor/rust-cpp/branch/master)
  * [rust-lang/rust-bindgen](https://github.com/rust-lang/rust-bindgen) - Rust 绑定生成器
* 埃尔兰
  * [rusterlium/rustler](https://github.com/rusterlium/rustler) - 用于创建 Erlang NIF 函数的安全 Rust 桥
* 爪哇
  * [bennettanderson/rjni](https://github.com/benanders/rjni) - 从 Rust 使用 Java
  * [drrb/java-rust-example](https://github.com/drrb/java-rust-example) - 从 Java 使用 Rust
  * [j4rs](https://crates.io/crates/j4rs) - 从 Rust 使用 Java
  * [jni](https://crates.io/crates/jni) - 从 Java 使用 Rust
  * [jni-sys](https://crates.io/crates/jni-sys) - 对应于 jni.h 的 Rust 定义
  * [rucaja](https://crates.io/crates/rucaja) - 从 Rust 使用 Java
* 卢阿
  * [jcmoyer/rust-lua53](https://github.com/jcmoyer/rust-lua53) - Rust 的 Lua 5.3 绑定
  * [lilyball/rust-lua](https://github.com/lilyball/rust-lua) - 与 Lua 5.1 的安全 Rust 绑定
  * [mlua-rs/mlua](https://github.com/mlua-rs/mlua) - 高级 Lua 5.4/5.3/5.2/5.1（包括 LuaJIT）和 Roblox Luau 绑定到 Rust，支持异步/等待 [![构建徽章](https://github.com/mlua-rs/mlua/workflows/CI/badge.svg)](https://github.com/mlua-rs/mlua/actions)
* [tickbh/td_rlua](https://github.com/tickbh/td_rlua) [[td_rlua](https://crates.io/crates/td_rlua)] - Rust 的零成本高级 lua 5.3 包装器
  * [tomaka/hlua](https://github.com/tomaka/hlua) - Rust 库与 Lua 交互
* 姆鲁比
  * [anima-engine/mrusty](https://github.com/anima-engine/mrusty) - Rust 的 mruby 安全绑定
* 节点.js
  * [infinyon/node-bindgen](https://github.com/infinyon/node-bindgen) - 使用 Rust 生成 Nodejs 模块的简单方法
  * [neon-bindings/neon](https://github.com/neon-bindings/neon) - 用于编写安全快速的原生 Node.js 模块的 Rust 绑定
  * [zhangyuang/node-ffi-rs](https://github.com/zhangyuang/node-ffi-rs) - 用 Rust 和 N-API 编写的模块为 Node.js 提供接口 (FFI) 功能
* 目标C
  * [SSheldon/rust-objc](https://github.com/SSheldon/rust-objc) - Rust 的 Objective-C 运行时绑定和包装器
* PHP
  * [phper-framework/phper](https://github.com/phper-framework/phper) - 该框架允许我们尽可能使用纯粹且安全的 Rust 编写 PHP 扩展
* 序言
  * [mthom/scryer-prolog](https://github.com/mthom/scryer-prolog/) - Scryer Prolog 是一个用 Rust 编写的免费软件 ISO Prolog 系统
* Python
  * [dgrunwald/rust-cpython](https://github.com/dgrunwald/rust-cpython) - Python 绑定
  * [getsentry/milksnake](https://github.com/getsentry/milksnake) - python setuptools 的扩展，允许您以可想象的最便携的方式在 Python 轮子中分发动态链接库。
  * [PyO3/PyO3](https://github.com/PyO3/PyO3) - Python 解释器的 Rust 绑定
  * [RustPython](https://github.com/RustPython/RustPython) - 用 Rust 编写的 Python 解释器 [![构建状态](https://github.com/RustPython/RustPython/workflows/CI/badge.svg)](https://github.com/RustPython/RustPython/actions?query=workflow%3ACI)
* 红宝石
  * [d-unsed/ruru](https://github.com/d-unsed/ruru) - 用 Rust 编写的本机 Ruby 扩展
  * [danielpclark/rutie](https://github.com/danielpclark/rutie) - 用 Rust 编写的本机 Ruby 扩展，反之亦然
* 网络组装
  * [rhysd/wain](https://github.com/rhysd/wain) - wain：WebAssembly INterpreter 从零依赖安全 Rust 开始 [![构建徽章](https://github.com/rhysd/wain/workflows/CI/badge.svg?branch=master&event=push)](https://github.com/rhysd/wain/actions?query=workflow%3ACI+branch%3Amaster+event%3Apush)
  * [wasm-bindgen](https://github.com/wasm-bindgen/wasm-bindgen) - 一个促进 wasm 模块和 JS 之间高级交互的项目。
  * [wasm-pack](https://github.com/wasm-bindgen/wasm-pack) - :package: :sparkles: 打包 wasm 并将其发布到 npm！

### 格式化程序

* [astral-sh/ruff](https://github.com/astral-sh/ruff) - 极快的 Python linter 和代码格式化程序 [![Actions status](https://github.com/astral-sh/ruff/workflows/CI/badge.svg)](https://github.com/astral-sh/ruff/actions)
* [dprint](https://github.com/dprint/dprint) - 可插入且可配置的代码格式化平台 [![构建徽章](https://github.com/dprint/dprint/workflows/CI/badge.svg)](https://github.com/dprint/dprint/actions?query=workflow%3ACI)
* [Prettier Rust](https://github.com/jinxdash/prettier-plugin-rust) - 一个固执己见的 Rust 代码格式化程序，可以自动修复错误的语法（[Prettier](https://prettier.io/) 社区插件）
* [rustfmt](https://github.com/rust-lang/rustfmt) - Rust 代码格式化程序由 Rust 团队维护并包含在 Cargo 中

### IDE

另请参阅 [Rust 工具](https://rust-lang.org/tools/)。

  * [Eclipse](https://www.eclipse.org/)
    * [Eclipse Corrosion](https://github.com/eclipse-corrosion/corrosion) - 用于 Eclipse IDE 的 Rust 开发插件，通过与 Rust Analyzer 语言服务器、Cargo 运行器和 gdb 调试器集成提供丰富的版本体验
  * [Emacs](https://www.gnu.org/software/emacs/)
    * [emacs-racer](https://github.com/racer-rust/emacs-racer) - 自动完成（另请参阅 [company](https://company-mode.github.io) 和 [auto-complete](https://github.com/auto-complete/auto-complete)）
    * [flycheck-rust](https://github.com/flycheck/flycheck-rust) - Rust 对 [Flycheck](https://github.com/flycheck/flycheck) 的支持
    * [rust-mode](https://github.com/rust-lang/rust-mode) - Rust 主要模式
    * [rustic](https://github.com/emacs-rustic/rustic) - Emacs 的 Rust 开发环境 [![构建徽章](https://github.com/emacs-rustic/rustic/workflows/CI/badge.svg)](https://github.com/emacs-rustic/rustic/actions?query=workflow%3ACI)
  * [gitpod.io](https://gitpod.io) - 基于 Rust 语言服务器的完全支持 Rust 的在线 IDE
  * [gnome-builder](https://wiki.gnome.org/Apps/Builder) - 自版本 3.22.2 起对 Rust 和 Cargo 的本机支持
  * [IntelliJ](https://www.jetbrains.com/idea/)
    * [intellij-rust/intellij-rust](https://github.com/intellij-rust/intellij-rust) - IntelliJ 平台的 Rust 插件
  * [Kakoune](http://kakoune.org/)
    * [kakoune-lsp](https://github.com/kakoune-lsp/kakoune-lsp/) - [LSP](https://microsoft.github.io/language-server-protocol/) 客户端。用 Rust 实现并支持开箱即用的 rls。
  * [lapce](https://github.com/lapce/lapce) - 用 Rust 编写的闪电般快速且强大的代码编辑器。 [![构建徽章](https://github.com/lapce/lapce/actions/workflows/release.yml/badge.svg)](https://github.com/lapce/lapce/actions/workflows/release.yml)
  * [Ride](https://github.com/madeso/ride) - Rust IDE
  * [RustRover](https://www.jetbrains.com/rust/) - JetBrains 推出的功能强大的 Rust IDE，免费供个人非商业用途
  * [崇高的文字](https://www.sublimetext.com/)
    * [rust-lang/rust-enhanced](https://github.com/rust-lang/rust-enhanced) - 官方 Rust 包
  * [Vim](https://vim.sourceforge.io/) - 无处不在的文本编辑器
    * [autozimu/LanguageClient-neovim](https://github.com/autozimu/LanguageClient-neovim) - [LSP](https://microsoft.github.io/language-server-protocol/) 客户端。用 Rust 实现并支持开箱即用的 rls。
    * [cargo.nvim](https://github.com/nwiizo/cargo.nvim) - 用于与 Cargo 命令无缝集成的 Neovim 插件。
    * [crates.nvim](https://github.com/Saecki/crates.nvim) - 有助于管理 crates.io 依赖项的插件。
    * [rust.vim](https://github.com/rust-lang/rust.vim) - 提供文件检测、语法突出显示、格式化、Syntastic 集成等。
    * [vim-racer](https://github.com/racer-rust/vim-racer) - 允许 vim 使用 [Racer](https://github.com/racer-rust/racer) 进行 Rust 代码补全和导航。
* 视觉工作室
    * [PistonDevelopers/VisualRust](https://github.com/PistonDevelopers/VisualRust) - Rust 的 Visual Studio 扩展 [![构建状态](https://ci.appveyor.com/api/projects/status/5nw5no10jj0y4p3f?svg=true)](https://ci.appveyor.com/project/vosen/visualrust)
  * [视觉工作室代码](https://code.visualstudio.com/)
    * [CodeLLDB](https://marketplace.visualstudio.com/items?itemName=vadimcn.vscode-lldb) - LLDB 扩展
    * [Dependi](https://marketplace.visualstudio.com/items?itemName=fill-labs.dependi) - 轻松管理您的依赖项
    * [Even Better TOML](https://marketplace.visualstudio.com/items?itemName=tamasfe.even-better-toml) - vscode 中的 TOML 支持
    * [Prettier - Code formatter (Rust)](https://marketplace.visualstudio.com/items?itemName=jinxdash.prettier-rust) - 固执己见的 Rust 代码格式化程序，可自动修复错误语法（[Prettier](https://prettier.io/) 社区插件）
    * [rust-analyzer](https://marketplace.visualstudio.com/items?itemName=rust-lang.rust-analyzer) - RLS 的替代 Rust 语言服务器

### 分析

* [Bencher](https://github.com/bencherdev/bencher) - 一套连续基准测试工具，旨在捕获 CI 中的性能回归
* [bheisler/criterion.rs](https://github.com/bheisler/criterion.rs) - 统计驱动的基准测试库
* [Bytehound](https://github.com/koute/bytehound) - 适用于 Linux 的内存分析器
* [cong-or/hud](https://github.com/cong-or/hud) - 找出阻碍您的 Tokio 运行时的因素。零仪器 eBPF 分析器。
* [Divan](https://github.com/nvzqz/divan) - 简单而强大的基准测试库，具有分配分析功能
* [ellisonch/rust-stopwatch](https://github.com/ellisonch/rust-stopwatch) - 秒表库
* 火焰图
  * [llogiq/flame](https://github.com/llogiq/flame) - 用于锈蚀的侵入式火焰图分析工具
* [g3bench](https://github.com/bytedance/g3) - 支持 HTTP 1.x、HTTP 2、HTTP 3、TLS Handshake、DNS 和 Cloudflare Keyless 的基准测试工具
* [pawurb/hotpath](https://github.com/pawurb/hotpath-rs) - 一个简单的分析器，准确显示代码在何处花费时间并分配 [![GH Actions](https://github.com/pawurb/hotpath-rs/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/pawurb/hotpath-rs/actions)
* [sharkdp/hyperfine](https://github.com/sharkdp/hyperfine) - 命令行基准测试工具

### 服务

* [deepwiki-rs](https://github.com/sopaco/deepwiki-rs) - 将您的代码库转换为专业的架构文档。 [![crates.io](https://img.shields.io/crates/v/deepwiki-rs?logo=rust)](https://crates.io/crates/deepwiki-rs)
* [deps.rs](https://github.com/deps-rs/deps.rs) - 检测过时或不安全的依赖项
* [docs.rs](https://docs.rs) - 自动生成 crate 文档

### 静态分析

[[断言](https://crates.io/keywords/assert)，[静态](https://crates.io/keywords/static)]

* [cargo-coupling](https://github.com/nwiizo/cargo-coupling) - 使用 Vlad Khononov 的“软件设计中的平衡耦合”框架的 Rust 耦合分析工具
* [creusot-rs/creusot](https://github.com/creusot-rs/creusot) - Rust 的演绎验证器，通过将代码翻译到 Why3 验证平台来证明不存在恐慌、溢出和断言失败
* [dupehound](https://github.com/Rafaelpta/dupehound) [[dupehound](https://crates.io/crates/dupehound)] - 重复代码检测器，对功能体进行指纹识别（筛选），因此副本在重命名后仍然存在。 Repo slop 分数、重复历史图表以及指向要重用的原始函数的 CI 门。支持 Rust 和其他 11 种语言。 [![CI](https://github.com/Rafaelpta/dupehound/actions/workflows/ci.yml/badge.svg)](https://github.com/Rafaelpta/dupehound/actions/workflows/ci.yml)
* [MIRAI](https://github.com/endorlabs/mirai) - 在 Rust 的中级中间表示（MIR）上运行的抽象解释器 [![持续集成](https://github.com/endorlabs/mirai/actions/workflows/rust.yml/badge.svg)](https://github.com/endorlabs/mirai/actions/workflows/rust.yml)
* [RAPx](https://github.com/safer-rust/RAPx) - 一个帮助 Rust 程序员开发和使用 rustc 编译器提供的高级静态分析工具的平台。
* [static_assertions](https://crates.io/crates/static_assertions) - 编译时断言以确保满足不变量
* [verus-lang/verus](https://github.com/verus-lang/verus) - 已验证 Rust 的低级系统代码
* [zizmorcore/zizmor](https://github.com/zizmorcore/zizmor) [[zizmor](https://crates.io/crates/zizmor)] - GitHub Actions 的静态分析工具，可发现安全问题，包括模板注入、凭证泄漏、权限过多和冒充者提交。 [![CI](https://github.com/zizmorcore/zizmor/actions/workflows/ci.yml/badge.svg)](https://github.com/zizmorcore/zizmor/actions/workflows/ci.yml)

### 测试

[[测试](https://crates.io/keywords/test)，[测试](https://crates.io/keywords/testing)]
* 断言和匹配器
* [googletest-json-serde](https://crates.io/crates/googletest-json-serde) [![最新版本](https://img.shields.io/crates/v/googletest-json-serde.svg)](https://crates.io/crates/googletest-json-serde) - googletest-rust 的 JSON 匹配器集合，支持路径、数组和对象。 [![构建状态](https://github.com/chege/googletest-json-serde/actions/workflows/ci.yaml/badge.svg)](https://github.com/chege/googletest-json-serde/actions)
* 代码覆盖率
  * [tarpaulin](https://crates.io/crates/cargo-tarpaulin) - 一个代码覆盖率工具
* 持续集成
  * [trust](https://github.com/japaric/trust) - Travis CI 和 AppVeyor 模板，用于在 5 种架构上测试 Rust 箱并发布适用于 Linux、macOS 和 Windows 的二进制版本
* 框架和运行程序
  * [AlKass/polish](https://github.com/AlKass/polish) - 迷你测试/测试驱动框架 [![Crates 包状态](https://img.shields.io/crates/v/polish.svg)](https://crates.io/crates/polish)
* [bitfield/cargo-testdox](https://github.com/bitfield/cargo-testdox) [[cargo-testdox](https://crates.io/crates/cargo-testdox)] - 将 Rust 测试转换为文档[![CI](https://github.com/bitfield/cargo-testdox/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/bitfield/cargo-testdox/actions/workflows/ci.yml)
  * [cargo-dinghy](https://crates.io/crates/cargo-dinghy/) - 一个货物扩展，用于简化在智能手机和其他小型处理器设备上运行库测试和工作台。
* [cucumber](https://crates.io/crates/cucumber) [![最新版本](https://img.shields.io/crates/v/cucumber.svg)](https://crates.io/crates/cucumber) - Rust 的 Cucumber 测试框架的实现。完全原生，没有外部测试运行程序或依赖项。 [![构建状态](https://github.com/cucumber-rs/cucumber/actions/workflows/ci.yml/badge.svg)](https://github.com/cucumber-rs/cucumber/actions)
* [d-e-s-o/test-log](https://github.com/d-e-s-o/test-log) [[test-log](https://crates.io/crates/test-log)] - 替换 `#[test]` 属性，用于在运行测试之前初始化日志记录和/或跟踪基础设施。 [![GitHub 工作流状态](https://github.com/d-e-s-o/test-log/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/d-e-s-o/test-log/actions/workflows/test.yml)
  * [demonstrate](https://crates.io/crates/demonstrate) - 声明式测试框架
  * [GoogleTest Rust](https://crates.io/crates/googletest) - 基于 C++ 测试库 GoogleTest 的强大测试断言框架 [![构建状态](https://github.com/google/googletest-rust/workflows/CI/badge.svg)](https://github.com/google/googletest-rust/actions?query=workflow%3ACI+branch%3Amain)
* [nextest-rs/nextest](https://github.com/nextest-rs/nextest) [[cargo-nextest](https://crates.io/crates/cargo-nextest)] - Rust 的下一代测试运行程序，具有并行测试执行、更快的测试运行、高级过滤和丰富的输出。 [![crates.io 上的 cargo-nextest](https://img.shields.io/crates/v/cargo-nextest)](https://crates.io/crates/cargo-nextest)
  * [rlt](https://github.com/wfxr/rlt) - 通用负载测试框架，具有实时 tui 支持。
  * [rstest](https://crates.io/crates/rstest) - 基于夹具的测试框架 [![构建状态](https://github.com/la10736/rstest/workflows/Test/badge.svg?branch=master)](https://github.com/la10736/rstest/actions)
  * [speculate](https://crates.io/crates/speculate) - 受 RSpec 启发的最小测试框架
* 模拟和测试数据
* [asomers/mockall](https://github.com/asomers/mockall) [[mockall](https://crates.io/crates/mockall)] - 一个强大的模拟对象库。 [![CI](https://github.com/asomers/mockall/actions/workflows/ci.yml/badge.svg)](https://github.com/asomers/mockall/actions/workflows/ci.yml)
* [bcheidemann/fixtures-rs](https://github.com/bcheidemann/fixtures-rs/tree/main/fixtures) [[fixtures](https://crates.io/crates/fixtures)] - 用于使用 glob 模式从固定装置生成测试的 proc 宏
  * [fake-rs](https://github.com/cksac/fake-rs) - 用于生成假数据的库
* [goldenfile](https://github.com/calder/rust-goldenfile) [[goldenfile](https://crates.io/crates/goldenfile)] - 一个为goldenfile测试提供简单API的库。
  * [httpmock](https://github.com/httpmock/httpmock) - HTTP 模拟 [![Build](https://github.com/httpmock/httpmock/actions/workflows/build.yml/badge.svg)](https://github.com/httpmock/httpmock/actions/workflows/build.yml)
  * [mockiato](https://crates.io/crates/mockiato) - 一个严格但友好的模拟库，适用于不稳定的 Rust 2018
  * [mockito](https://crates.io/crates/mockito) - HTTP 模拟
* [mocktail](https://github.com/IBM/mocktail) [![mocktail](https://img.shields.io/crates/v/mocktail)](https://crates.io/crates/mocktail) - Rust 的 HTTP 和 gRPC 服务器模拟！[build](https://github.com/IBM/mocktail/actions/workflows/build.yml/badge.svg)
* [nrxus/faux](https://github.com/nrxus/faux/) [![最新版本](https://img.shields.io/crates/v/faux.svg)](https://crates.io/crates/faux) - 一个用结构创建模拟的库。 ![构建](https://github.com/nrxus/faux/workflows/test/badge.svg?branch=master)
  * [synth](https://github.com/shuttle-hq/synth/) - 以声明方式生成数据库数据。 [![build](https://github.com/shuttle-hq/synth/actions/workflows/synth-test.yml/badge.svg)](https://github.com/shuttle-hq/synth)
* 突变测试
* [cargo-mutants](https://github.com/sourcefrog/cargo-mutants) [[cargo-mutants](https://crates.io/crates/cargo-mutants)] - 通过注入突变查找未经充分测试的代码，无需更改源代码。 [![构建徽章](https://github.com/sourcefrog/cargo-mutants/actions/workflows/tests.yml/badge.svg?branch=main&event=push)](https://github.com/sourcefrog/cargo-mutants/actions/workflows/tests.yml?query=branch%3Amain)
* [mutagen](https://github.com/llogiq/mutagen) [[mutagen](https://crates.io/crates/mutagen)] - 源代码级突变测试框架（仅限夜间）
* 属性测试和模糊测试
  * [Ackee-Blockchain/trident](https://github.com/Ackee-Blockchain/trident) - Solana 智能合约的模糊测试框架，具有手动引导测试、基于流程的序列和基于属性的验证
  * [proptest](https://crates.io/crates/proptest) - 属性测试框架的灵感来自于 Python 的 [Hypothesis](https://hypothesis.works/) 框架
  * [quickcheck](https://crates.io/crates/quickcheck) - [QuickCheck](https://wiki.haskell.org/Introduction_to_QuickCheck1) 的 Rust 实现
  * [rust-fuzz/afl.rs](https://github.com/rust-fuzz/afl.rs) - 一个 Rust 模糊器，使用 [AFL](https://lcamtuf.coredump.cx/afl/)

### 转译

* [aleph-lang/aleph_ollama](https://github.com/aleph-lang/aleph_ollama) [[aleph_ollama](https://crates.io/crates/aleph_ollama)] - 使用本地 Ollama API 的人工智能源代码翻译工具。
* [BayesWitnesses/m2cgen](https://github.com/BayesWitnesses/m2cgen) - 一个 CLI 工具，用于将经过训练的经典机器学习模型转换为零依赖的本机 Rust 代码。 [![GitHub 操作状态](https://github.com/BayesWitnesses/m2cgen/workflows/GitHub%20Actions/badge.svg?branch=master)](https://github.com/BayesWitnesses/m2cgen/actions)
* [immunant/c2rust](https://github.com/immunant/c2rust) - C 到 Rust 的翻译器和交叉检查器构建在 Clang/LLVM 之上。
* [jameysharp/corrode](https://github.com/jameysharp/corrode) - 用 Haskell 编写的 C 到 Rust 翻译器。

### 隧道

* [ekzhang/bore](https://github.com/ekzhang/bore) [[bore-cli](https://crates.io/crates/bore-cli)] - 一个简单的 TCP 隧道，将本地端口暴露给远程服务器，绕过 NAT 防火墙 [![构建状态](https://img.shields.io/github/actions/workflow/status/ekzhang/bore/ci.yml)](https://github.com/ekzhang/bore/actions)
* [joaoh82/rustunnel](https://github.com/joaoh82/rustunnel) - 自托管安全隧道服务器。通过 yamux 多路复用的 TLS 加密 WebSocket 公开本地 HTTP/HTTPS/TCP/UDP 服务；多区域、Prometheus 指标、AI 代理的 MCP 服务器。
* [ngrok/ngrok-rust](https://github.com/ngrok/ngrok-rust) [[ngrok-rust](https://crates.io/crates/ngrok)] - ngrok 是一个开发人员工具，可以安全地将本地应用程序公开到互联网。
* [rathole-org/rathole](https://github.com/rathole-org/rathole) - 用于 NAT 穿越的安全、高性能反向代理，具有噪声协议/TLS 加密和热重载配置支持！[CI](https://img.shields.io/github/actions/workflow/status/rathole-org/rathole/rust.yml?branch=main)

## 图书馆

* [perf-monitor-rs](https://github.com/larksuite/perf-monitor-rs) - 一个工具包，旨在成为应用程序监控其性能的基础。 [![crates.io](https://img.shields.io/crates/v/perf_monitor.svg)](https://crates.io/crates/perf_monitor)

### 人工智能

#### 遗传算法

* [innoave/genevo](https://github.com/innoave/genevo) - 以可定制和可扩展的方式执行遗传算法 (GA) 模拟。
* [m-decoster/RsGenetic](https://github.com/m-decoster/RsGenetic) - 遗传算法库。处于维护模式。
* [Martin1887/oxigen](https://github.com/Martin1887/oxigen) - 快速、并行、可扩展且适应性强的遗传算法库。使用此库的示例只需几秒钟即可解决 N = 255 的 N Queens 问题，并且使用的 RAM 不到 1 MB。
* [pkalivas/radiate](https://github.com/pkalivas/radiate) - 一个可定制的并行遗传编程引擎，能够为监督、无监督和强化学习问题提供解决方案。附带完整且可定制的 NEAT 和 Evtree 实现。！[Crates.io](https://img.shields.io/crates/v/radiate)
* [willi-kappler/darwin-rs](https://github.com/willi-kappler/darwin-rs) - 进化算法

#### 谷歌双子座

* [gemini-client-api](https://crates.io/crates/gemini-client-api) - 使用 Google Gemini API 的库。自动上下文管理、模式生成、函数调用等等。

#### 机器学习

请参阅[[机器学习](https://crates.io/keywords/machine-learning)]

另请参阅[关于 Rust 的机器学习社区](https://medium.com/@autumn_eng/about-rust-s-machine-learning-community-4cda5ec8a790#.hvkp56j3f) 和[我们在学习吗？](https://www.arewelearningyet.com)。

* [autumnai/leaf](https://github.com/autumnai/leaf) - 开放机器智能框架。废弃的项目。最新的分支是[juice](https://github.com/fff-rs/juice)。
* [ave-sergeev/tictonix](https://github.com/Ave-Sergeev/Tictonix) [[tictonix](https://crates.io/crates/tictonix)] - 一个库，提供将令牌转换为嵌入以及对其位置进行编码的能力。
* [blackportal-ai/delta](https://github.com/blackportal-ai/delta) - Δ Rust 中的开源机器学习框架。 ![crates.io](https://img.shields.io/crates/v/deltaml.svg) ![build](https://img.shields.io/github/actions/workflow/status/blackportal-ai/delta/core.yml?branch=master)
* [blackportal-ai/nebula](https://github.com/blackportal-ai/nebula) - 机器学习数据集和模型的包管理器。 ![构建](https://img.shields.io/github/actions/workflow/status/blackportal-ai/nebula/core.yml?branch=master)
* [burn](https://github.com/tracel-ai/burn) - 灵活且全面的深度学习框架。
* [chelsea0x3b/dfdx](https://github.com/chelsea0x3b/dfdx) - CUDA 加速机器学习框架，利用 Rust 的许多独特功能。 ![Crates.io](https://img.shields.io/crates/v/dfdx)
* [EricLBuehler/mistral.rs](https://github.com/EricLBuehler/mistral.rs) [[mistralrs](https://crates.io/crates/mistralrs)] - 快速、灵活的 LLM 推理引擎，支持多模态模型、量化 (GGUF/GPTQ/ISQ) 和 OpenAI 兼容 API
* [guillaume-be/rust-bert](https://github.com/guillaume-be/rust-bert) [[rust_bert](https://crates.io/crates/rust_bert)] - 即用型 NLP 管道和语言模型
* [huggingface/candle](https://github.com/huggingface/candle) [[candle-core](https://crates.io/crates/candle-core)] - 一个简约的机器学习框架，重点关注易用性和性能（包括 GPU 支持）
* [huggingface/tokenizers](https://github.com/huggingface/tokenizers) - Hugging Face 的现代 NLP 管道的分词器（原始实现）与 Python 的绑定。 [![构建状态](https://github.com/huggingface/tokenizers/workflows/Rust/badge.svg?branch=master)](https://github.com/huggingface/tokenizers/actions)
* [katanemo/plano](https://github.com/katanemo/plano) - 用于代理应用程序的 AI 原生代理服务器和数据平面。
* [LaurentMazare/tch-rs](https://github.com/LaurentMazare/tch-rs) - PyTorch 的绑定。
* [luminal-ai/luminal](https://github.com/luminal-ai/luminal) [[luminal](https://crates.io/crates/luminal)] - 高性能通用推理编译器，具有 RISC 风格架构、基于搜索的优化和本机 CUDA/Metal 后端。支持变压器、卷积网络和自动分级。 [![CI 状态](https://img.shields.io/github/actions/workflow/status/luminal-ai/luminal/test-core.yml?style=for-the-badge&logo=github-actions&logoColor=white&branch=main)](https://github.com/luminal-ai/luminal/actions)
* [maciejkula/rustlearn](https://github.com/maciejkula/rustlearn) - 机器学习库。 [![Circle CI](https://circleci.com/gh/maciejkula/rustlearn.svg?style=svg)](https://app.circleci.com/pipelines/github/maciejkula/rustlearn)
* [Mottl/lightgb3-rs](https://github.com/Mottl/lightgbm3-rs) - LightGBM 的绑定 [![Crates.io](https://img.shields.io/crates/v/lightgbm3.svg)](https://crates.io/crates/lightgbm3) [![build](https://github.com/Mottl/lightgbm3-rs/actions/workflows/ci.yml/badge.svg)](https://github.com/Mottl/lightgbm3-rs/actions)
* [perpetual-ml/perpetual](https://github.com/perpetual-ml/perpetual) [[perpetual](https://crates.io/crates/perpetual)] - 一种不需要超参数优化的自泛化梯度增强机器。
* [ramsyana/RustTensor](https://github.com/ramsyana/RustTensor) - 一个以学习为中心的高性能张量计算库，用 Rust 从头开始​​构建，具有自动微分和 CPU/CUDA 后端。
* [raphaelmansuy/edgequake](https://github.com/raphaelmansuy/edgequake) - 一个高性能的Graph-RAG框架，可将文档转换为智能知识图谱。
* [rust-ml/linfa](https://github.com/rust-ml/linfa) - 机器学习框架。
* [sipemu/anofox-regression](https://github.com/sipemu/anofox-regression) [[anofox-regression](https://crates.io/crates/anofox-regression)] - 统计回归模型（OLS、弹性网络、GLM、分位数和等渗），具有类似 R 的推理（p 值、置信度和预测区间）和 Wasm 支持。
* [smartcorelib/smartcore](https://github.com/smartcorelib/smartcore) - 机器学习库 [![构建状态](https://img.shields.io/circleci/build/github/smartcorelib/smartcore)]
* [tag1consulting/feste](https://github.com/tag1consulting/feste) - 出于教育目的，在 Rust 中从头开始实现的 GPT-2 样式转换器语言模型。
* [tensorflow/rust](https://github.com/tensorflow/rust) - TensorFlow 的绑定。

#### 开放人工智能

* [0xplaygrounds/rig](https://github.com/0xplaygrounds/rig) - 用于创建代理和模块化、可扩展的 LLM 应用程序的库
* [64bit/async-openai](https://github.com/64bit/async-openai) [[async-openai](https://crates.io/crates/async-openai)] - 基于 OpenAPI 规范的 OpenAI API 的符合人体工程学的 Rust 绑定。
* [awakenworks/awaken](https://github.com/awakenworks/awaken) [[awaken](https://crates.io/crates/awaken)] - Rust 的 AI 代理运行时 — 类型安全状态、多协议服务、插件可扩展性。
* [liquidos-ai/AutoAgents](https://github.com/liquidos-ai/AutoAgents) [[AutoAgents](https://crates.io/crates/autoagents)] - 用于构建具有本机边缘支持的 AI 代理的多代理框架。
* [openai/codex](https://github.com/openai/codex) - Codex CLI 是来自 OpenAI 的在本地运行的编码代理。
* [openai/harmony](https://github.com/openai/harmony) [[openai-harmony](https://crates.io/crates/openai-harmony/0.0.3)] - 与 gpt-oss 一起使用的和声响应格式的渲染器。
* [zurawiki/tiktoken-rs](https://github.com/zurawiki/tiktoken-rs) [[tiktoken-rs](https://crates.io/crates/tiktoken-rs)] - 使用 tiktoken 通过 OpenAI 模型对文本进行标记化的库。 [![CI](https://github.com/zurawiki/tiktoken-rs/actions/workflows/ci.yml/badge.svg)](https://github.com/zurawiki/tiktoken-rs/actions/workflows/ci.yml)

#### 工装

* [BAML](https://github.com/BoundaryML/baml) - 一种简单的提示语言，用于构建可靠的人工智能工作流程和代理。 BAML 的编译器是用 Rust 编写的！
* [Cortex Memory](https://github.com/sopaco/cortex-mem) - 代理内存的完整解决方案，从提取和矢量搜索到自动优化，以及开箱即用的见解仪表板。
* [juyterman1000/entroly](https://github.com/juyterman1000/entroly) - 信息论上下文工程引擎，使用强化学习来智能修剪和选择最佳 RAG 片段。
* [memvid/memvid](https://github.com/memvid/memvid) [[memvid-core](https://crates.io/crates/memvid-core)] - 用于 AI 代理的单文件便携式内存层，将矢量搜索、全文搜索和长期召回打包到一个“.mv2”文件中
* [pydantic/monty](https://github.com/pydantic/monty) - 一个最小的、安全的Python解释器，用于在AI代理中运行LLM生成的代码，具有微秒启动、严格的沙箱和快照支持[![CI](https://github.com/pydantic/monty/actions/workflows/ci.yml/badge.svg)](https://github.com/pydantic/monty/actions/workflows/ci.yml)

### 天文学

[[天文学](https://crates.io/keywords/astronomy)]

* [cds-astro/aladin-lite](https://github.com/cds-astro/aladin-lite) - 用于在不同投影中可视化空间和行星图像调查的 Web 应用程序
* [fitsio](https://crates.io/crates/fitsio) - 适合包装 cfitsio 的接口库
* [flosse/rust-sun](https://github.com/flosse/rust-sun) [[sun](https://crates.io/crates/sun)] - JS 库 suncalc 的 Rust 端口
* [saurvs/astro-rust](https://github.com/saurvs/astro-rust) - 天文学

### 异步

* [async-std](https://async.rs/) [[async-std](https://crates.io/crates/async-std)] - Rust 标准库的异步版本[![CI](https://github.com/async-rs/async-std/actions/workflows/ci.yml/badge.svg?branch=master)](https://github.com/async-rs/async-std/actions/workflows/ci.yml)
* [dagrs](https://github.com/dagrs-dev/dagrs) - 一个高性能的异步任务编程框架，遵循基于流程的编程概念。
* [dpc/mioco](https://github.com/dpc/mioco) - 可扩展、基于协程的异步 IO 处理库
* [igumnoff/gabriel2](https://github.com/igumnoff/gabriel2) [[gabriel2](https://crates.io/crates/gabriel2)] - Gabriel2：基于 Tokio 的演员模型库
* [iii-hq/iii](https://github.com/iii-hq/iii) [[iii-sdk](https://crates.io/crates/iii-sdk)] - 用于通过 Worker-Function-Trigger 原语组合服务的分布式运行时。实时目录、可追踪的函数调用和多语言 SDK（Rust、Node.js、Python）。用 Rust (ELv2) 编写的引擎，Apache 2.0 下的 SDK。
* [mio](https://github.com/tokio-rs/mio) - MIO 是一个轻量级 IO 库，重点是在操作系统抽象上添加尽可能少的开销
* [nextest-rs/future-queue](https://github.com/nextest-rs/future-queue) [[future-queue](https://crates.io/crates/future-queue)] - 用于同时运行 future 的流适配器，具有加权并发限制和可选的每组限制。
* [rust-lang/futures-rs](https://github.com/rust-lang/futures-rs) - 零成本期货
* [t3hmrman/async-dropper](https://github.com/t3hmrman/async-dropper) [[async-dropper](https://crates.io/crates/async-dropper)] - `AsyncDrop` 的实现
* [TeaEntityLab/fpRust](https://github.com/TeaEntityLab/fpRust) - Monad/MonadIO、Handler、Coroutine/doNotation、Rust 函数式编程功能
* [tokio-rs/tokio](https://github.com/tokio-rs/tokio) - 用于使用 Rust 编程语言编写可靠、异步且精简的应用程序的运行时。
* [tqwewe/kameo](https://github.com/tqwewe/kameo) - 基于 Tokio 的容错异步 Actor
* [Xudong-Huang/may](https://github.com/Xudong-Huang/may) - Stackful协程库
* [zonyitoo/coio-rs](https://github.com/zonyitoo/coio-rs) - 具有工作窃取调度程序的协程 I/O 库

### 音频和音乐

[[音频](https://crates.io/keywords/audio)]

* [aschey/stream-download-rs](https://github.com/aschey/stream-download-rs) [[stream-download](https://crates.io/crates/stream-download)] - 用于流式传输音频、视频和其他媒体内容的库 [![build徽章](https://github.com/aschey/stream-download-rs/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/aschey/stream-download-rs/actions)
* [hound](https://crates.io/crates/hound) - 一个WAV编码和解码库
* [insomnimus/nodi](https://github.com/insomnimus/nodi) [[nodi](https://crates.io/crates/nodi)] - 用于播放和抽象 MIDI 文件的库。 [![构建徽章](https://github.com/insomnimus/nodi/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/insomnimus/nodi/actions)
* [jhasse/ears](https://github.com/jhasse/ears) - 一个简单的库，用于在 OpenAL 和 libsndfile 之上播放声音和音乐
* [musitdev/portmidi-rs](https://github.com/musitdev/portmidi-rs) - [PortMidi](https://portmedia.sourceforge.net/portmidi/) 绑定
* [ozankasikci/rust-music-theory](https://github.com/ozankasikci/rust-music-theory) - 音乐理论图书馆
* [pdeljanov/Symphonia](https://github.com/pdeljanov/Symphonia) - 支持 AAC、FLAC、MP3、MP4、OGG、Vorbis 和 WAV 的音频解码和媒体解复用库。
* [RustAudio](https://github.com/RustAudio)
  * [RustAudio/cpal](https://github.com/RustAudio/cpal) - 低级跨平台音频 I/O 库。 [![操作状态](https://github.com/RustAudio/cpal/workflows/cpal/badge.svg?branch=master)](https://github.com/RustAudio/cpal/actions)
  * [RustAudio/rodio](https://github.com/RustAudio/rodio) - 音频播放库
  * [RustAudio/rust-portaudio](https://github.com/RustAudio/rust-portaudio) - PortAudio 绑定
* [Serial-ATA/lofty-rs](https://github.com/Serial-ATA/lofty-rs) [[lofty](https://crates.io/crates/lofty)] - 用于读取和编辑各种音频格式元数据的库 [![build徽章](https://github.com/Serial-ATA/lofty-rs/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/Serial-ATA/lofty-rs/actions)

### 认证

* [constantoine/totp-rs](https://github.com/constantoine/totp-rs) [[totp-rs](https://crates.io/crates/totp-rs)] - 2fa 库，用于生成和验证基于 TOTP 的令牌！[构建状态](https://github.com/constantoine/totp-rs/workflows/Rust/badge.svg)
* [Keats/jsonwebtoken](https://github.com/Keats/jsonwebtoken) - [JSON Web 令牌](https://en.wikipedia.org/wiki/JSON_Web_Token) 库
* [oauth2](https://github.com/ramosbugs/oauth2-rs) - 可扩展的强类型 OAuth2 客户端库
* [oxide-auth](https://github.com/197g/oxide-auth) - 一个 OAuth2 服务器库，与 actix 或其他前端结合使用，具有一组可配置和可插入的后端 [![CI](https://github.com/HeroicKatora/oxy-auth/actions/workflows/ci.yml/badge.svg)](https://github.com/HeroicKatora/oxy-auth/actions/workflows/ci.yml)
* [sgrust01/jwtvault](https://github.com/sgrust01/jwtvault) - 用于管理和编排 JWT 工作流程的异步库
* [yup-oauth2](https://github.com/dermesser/yup-oauth2) - 提供设备、已安装和服务帐户流的 oauth2 客户端实现

### 汽车

* [idletea/tokio-socketcan](https://github.com/idletea/tokio-socketcan) [[tokio-socketcan](https://crates.io/crates/tokio-socketcan)] - 基于socketcan crate对tokio的Linux SocketCAN支持
* [marcelbuesing/tokio-socketcan-bcm](https://github.com/marcelbuesing/tokio-socketcan-bcm) [[tokio-socketcan-bcm](https://crates.io/crates/tokio-socketcan-bcm)] - Linux SocketCAN BCM 对 tokio 的支持
* [mbr/socketcan](https://github.com/socketcan-rs/socketcan-rs) [[socketcan](https://crates.io/crates/socketcan)] - Linux SocketCAN 库
* [oxibus/can-dbc](https://github.com/oxibus/can-dbc) [[can-dbc](https://crates.io/crates/can-dbc)] - DBC 格式的解析器
* [Sensirion/lin-bus](https://github.com/Sensirion/lin-bus-rs) [[lin-bus](https://crates.io/crates/lin-bus)] - LIN 总线驱动程序特征和协议实现 [![build徽章](https://circleci.com/gh/Sensirion/lin-bus-rs.svg?style=svg)](https://app.circleci.com/pipelines/github/Sensirion/lin-bus-rs)

### 生物信息学

* [polars-bio](https://github.com/biodatageeks/polars-bio) - Python DataFrame 上的极速生物信息操作！[PyPI - 版本](https://img.shields.io/pypi/v/polars-bio)
* [Rust-Bio](https://github.com/rust-bio) - 生物信息学图书馆。

### 缓存

* [06chaynes/http-cache](https://github.com/06chaynes/http-cache) [[http-cache](https://crates.io/crates/http-cache)] - 遵循 HTTP 缓存规则的缓存中间件 [![build徽章](https://github.com/06chaynes/http-cache/workflows/http-cache/badge.svg)](https://github.com/06chaynes/http-cache/actions/workflows/http-cache.yml)
* [aisk/rust-memcache](https://github.com/aisk/rust-memcache) - Memcached 客户端库
* [al8n/stretto](https://github.com/al8n/stretto) - 高性能线程安全内存绑定缓存 [![构建徽章](https://github.com/al8n/stretto/actions/workflows/ci.yml/badge.svg)](https://github.com/al8n/stretto/actions/workflows/ci.yml)
* [hit-box/hitbox](https://github.com/hit-box/hitbox) - 具有 HTTP 中间件和多层后端的声明式缓存编排框架 [![CI](https://github.com/hit-box/hitbox/actions/workflows/CI.yml/badge.svg)](https://github.com/hit-box/hitbox/actions/workflows/CI.yml)
* [jaemk/cached](https://github.com/jaemk/cached) - 简单的函数缓存/记忆
* [moka-rs/moka](https://github.com/moka-rs/moka) - 受 Java Caffeine 库启发的高性能并发缓存库 [![构建徽章](https://github.com/moka-rs/moka/workflows/CI/badge.svg)](https://github.com/moka-rs/moka/actions/workflows/CI.yml)
* [mozilla/sccache](https://github.com/mozilla/sccache/) - 共享编译缓存，很棒的编译
* [salsa-rs/salsa](https://github.com/salsa-rs/salsa) [[salsa](https://crates.io/crates/salsa)] - 受 rustc 查询系统启发，使用记忆查询进行按需增量计算的通用框架。 [![测试](https://github.com/salsa-rs/salsa/workflows/Test/badge.svg)](https://github.com/salsa-rs/salsa/actions?query=workflow%3ATest)
* [zkat/cacache-rs](https://github.com/zkat/cacache-rs) - 高性能、并发、内容可寻址的磁盘缓存，针对异步 API 进行了优化 [![构建徽章](https://github.com/zkat/cacache-rs/workflows/CI/badge.svg)](https://github.com/zkat/cacache-rs/actions/workflows/ci.yml)

### 云

* AWS [[aws](https://crates.io/keywords/aws)]
* [aws/aws-lambda-rust-runtime](https://github.com/aws/aws-lambda-rust-runtime) [[lambda_runtime](https://crates.io/crates/lambda_runtime)] - AWS Lambda 的运行时 [![build徽章](https://github.com/aws/aws-lambda-rust-runtime/workflows/Rust/badge.svg)](https://github.com/aws/aws-lambda-rust-runtime/actions)
  * [awslabs/aws-sdk-rust](https://github.com/awslabs/aws-sdk-rust) - 新的 AWS 开发工具包
* [faiscadev/fakecloud](https://github.com/faiscadev/fakecloud) [[fakecloud](https://crates.io/crates/fakecloud)] - 用于开发和测试的本地 AWS 云模拟器。 [![CI](https://github.com/faiscadev/fakecloud/workflows/CI/badge.svg?branch=main)](https://github.com/faiscadev/fakecloud/actions)
  * [rusoto/rusoto](https://github.com/rusoto/rusoto) - 适用于 Rust 的 AWS 开发工具包
* 天蓝色
  * [Azure/azure-sdk-for-rust](https://github.com/Azure/azure-sdk-for-rust) - Rust 官方 Azure SDK
* 负载均衡器
  * [Convey](https://github.com/bparli/convey) - 具有动态配置加载的第 4 层负载均衡器。
* 多云
  * [Qovery/engine](https://github.com/Qovery/engine) - 抽象层库只需几分钟即可在云提供商上轻松部署应用程序

### 命令行

* 参数解析
* [clap-rs](https://github.com/clap-rs/clap) [[clap](https://crates.io/crates/clap)] - 一个简单易用、功能齐全的命令行参数解析器
  * [cliparser](https://crates.io/crates/cliparser) - 简单的命令行解析器。 [![构建徽章](https://github.com/sagiegurari/cliparser/actions/workflows/ci.yml/badge.svg)](https://github.com/sagiegurari/cliparser/actions)
* [docopt/docopt.rs](https://github.com/docopt/docopt.rs) [[docopt](https://crates.io/crates/docopt)] - DocOpt 的实现
* [google/argh](https://github.com/google/argh) [[argh](https://crates.io/crates/argh)] - 针对代码大小进行优化的基于 Derive 的参数解析器
* [killercup/quicli](https://github.com/killercup/quicli) [[quicli](https://crates.io/crates/quicli)] - 快速构建酷炫的 CLI 应用程序
* [ksk001100/seahorse](https://github.com/ksk001100/seahorse) [[seahorse](https://crates.io/crates/seahorse)] - 一个最小的 CLI 框架 [![构建状态](https://github.com/ksk001100/seahorse/workflows/CI/badge.svg?branch=master)](https://github.com/ksk001100/seahorse/actions)
* [TeXitoi/structopt](https://github.com/TeXitoi/structopt) [[structopt](https://crates.io/crates/structopt)] - 通过定义结构来解析命令行参数
* 数据可视化
* [nukesor/comfy-table](https://github.com/nukesor/comfy-table) [[comfy-table](https://crates.io/crates/comfy-table)] - 用于 cli 工具的漂亮动态表。 [![构建状态](https://github.com/Nukesor/comfy-table/workflows/Tests/badge.svg?branch=master)](https://github.com/nukesor/comfy-table/actions)
* [zhiburt/tabled](https://github.com/zhiburt/tabled) [[tabled](https://crates.io/crates/tabled)] - 一个易于使用的库，用于漂亮地打印结构和枚举表。 [![构建状态](https://github.com/zhiburt/tabled/actions/workflows/ci.yml/badge.svg)](https://github.com/zhiburt/tabled/actions)
* 以人为本的设计
* [rust-cli/ human-panic](https://github.com/rust-cli/ human-panic) [[ human-panic](https://crates.io/crates/ human-panic)] - 人类的恐慌消息
* 行编辑器
* [kkawakam/rustyline](https://github.com/kkawakam/rustyline) [[rustyline](https://crates.io/crates/rustyline)] - readline 实现
* [MovingtoMars/liner](https://github.com/MovingtoMars/liner) [[liner](https://crates.io/crates/liner)] - 提供类似 readline 功能的库
* [murarth/linefeed](https://github.com/murarth/linefeed) [[linefeed](https://crates.io/crates/linefeed)] - 可配置、可扩展、交互式行阅读器
* [srijs/rust-copperline](https://github.com/srijs/rust-copperline) [[copperline](https://crates.io/crates/copperline)] - 命令行编辑库
* 其他
* [mgrachev/update-informer](https://github.com/mgrachev/update-informer) [[update-informer](https://crates.io/crates/update-informer)] - 更新 CLI 应用程序的通知程序。它会检查 Crates.io 和 GitHub 上的新版本 [![构建徽章](https://github.com/mgrachev/update-informer/workflows/CI/badge.svg)](https://github.com/mgrachev/update-informer/actions)
* 管道
* [hniksic/rust-subprocess](https://github.com/hniksic/rust-subprocess) [[subprocess](https://crates.io/crates/subprocess)] - 与外部管道交互的设施
* [imp/pager-rs](https://gitlab.com/imp/pager-rs) [[pager](https://crates.io/crates/pager)] - 通过外部寻呼机传输输出
* [oconnor663/duct.rs](https://github.com/oconnor663/duct.rs) [[duct](https://crates.io/crates/duct)] - 子进程管道和 IO 重定向的构建器
* [rust-cli/rexpect](https://github.com/rust-cli/rexpect) [[rexpect](https://crates.io/crates/rexpect)] - 自动化交互式应用程序，例如 ssh、ftp、passwd 等[![CI](https://github.com/rust-cli/rexpect/actions/workflows/ci.yml/badge.svg)](https://github.com/rust-cli/rexpect/actions/workflows/ci.yml)
* [zhiburt/expectrl](https://github.com/zhiburt/expectrl) [[expectrl](https://crates.io/crates/expectrl)] - 用于控制伪终端中的交互式程序的库 [![build徽章](https://github.com/zhiburt/expectrl/actions/workflows/ci.yml/badge.svg)](https://github.com/zhiburt/expectrl/actions/workflows/ci.yml)
* 进展
* [a8m/pb](https://github.com/a8m/pb) [[pbr](https://crates.io/crates/pbr)] - 控制台进度条
* [clitic/kdam](https://github.com/clitic/kdam) [[kdam](https://crates.io/crates/kdam)] - 受 tqdm 和 rich.progress 启发的控制台进度条库[![CI](https://github.com/clitic/kdam/actions/workflows/tests.yml/badge.svg)](https://github.com/clitic/kdam/actions/workflows/tests.yml)
* [console-rs/indicatif](https://github.com/console-rs/indicatif) [[indicatif](https://crates.io/crates/indicatif)] - 向用户指示进度
* [etienne-napoleone/spinach](https://github.com/etienne-napoleone/spinach) [[spinach](https://crates.io/crates/spinach)] - 实用旋转器。 [![CI](https://github.com/etienne-napoleone/spinach/actions/workflows/ci.yml/badge.svg)](https://github.com/etienne-napoleone/spinach/actions/workflows/ci.yml)
* [FGRibreau/spinners](https://github.com/FGRibreau/spinners) [[spinners](https://crates.io/crates/spinners)] - 60 多个优雅的终端微调器
* [vyfor/rattles](https://github.com/vyfor/rattles) [[rattles](https://crates.io/crates/rattles)] - 一个最小的、无依赖的终端旋转器库。
* 提示
* [hashmismatch/terminal_cli.rs](https://github.com/hashmismatch/terminal_cli.rs) [[terminal_cli](https://crates.io/crates/terminal_cli)] - 构建交互式命令提示符
* [mikaelmello/inquire](https://github.com/mikaelmello/inquire) [[inquire](https://crates.io/crates/inquire)] - 用于在终端上构建交互式提示的库。 [![构建状态](https://github.com/mikaelmello/inquire/actions/workflows/build.yml/badge.svg?branch=main)](https://github.com/mikaelmello/inquire/actions)
* [starship/starship](https://starship.rs/) [[starship](https://crates.io/crates/starship)] - 适用于任何 shell 的最小、极快且高度可定制的提示 [![构建状态](https://github.com/starship/starship/actions/workflows/workflow.yml/badge.svg)](https://github.com/starship/starship/actions)
* [ynqa/promkit](https://github.com/ynqa/promkit) [[promkit](https://crates.io/crates/promkit)] - 用于构建交互式命令行工具的工具包[![ci](https://github.com/ynqa/promkit/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/ynqa/promkit/actions/workflows/ci.yml)
* 风格
* [colored](https://github.com/colored-rs/colored) [[colored](https://crates.io/crates/colored)] - 着色终端如此简单，您已经知道如何做了！
* [console-rs/dialoguer](https://github.com/console-rs/dialoguer) [[dialoguer](https://crates.io/crates/dialoguer)] - 用于命令行提示和类似内容的库。
* [LukasKalbertodt/bunt](https://github.com/LukasKalbertodt/bunt) [[bunt](https://crates.io/crates/bunt)] - 跨平台终端颜色和宏样式 [![Build状态](https://github.com/LukasKalbertodt/bunt/actions/workflows/ci.yml/badge.svg)](https://github.com/LukasKalbertodt/bunt/actions?query=workflow%3ACI+branch%3Amaster)
* [LukasKalbertodt/term-painter](https://github.com/LukasKalbertodt/term-painter) [[term-painter](https://crates.io/crates/term-painter)] - 跨平台风格的终端输出
* [ogham/rust-ansi-term](https://github.com/ogham/rust-ansi-term) [[ansi_term](https://crates.io/crates/ansi_term)] - 控制 ANSI 终端上的颜色和格式
* [SergioBenitez/yansi](https://github.com/SergioBenitez/yansi) [[yansi](https://crates.io/crates/yansi)] - 一个简单的 ANSI 终端彩色绘画库
*途易
* [AppCUI](https://github.com/gdt050579/AppCUI-rs) [[appcui](https://crates.io/crates/appcui)] - Rust 中功能齐全的跨平台 TUI/CUI 框架，具有内置小部件、布局控制、动画、Unicode 和主题支持。
* BearLib 终端
* [cfyzium/bearlibterminal](https://github.com/nabijaczleweli/BearLibTerminal.rs) [[bear-lib-terminal](https://crates.io/crates/bear-lib-terminal)] - [BearLibTerminal](https://github.com/tommyettinger/BearLibTerminal) 绑定
* [ccbrown/iocraft](https://github.com/ccbrown/iocraft) [[iocraft](https://crates.io/crates/iocraft)] - 一个漂亮的、手工制作的 CLI、TUI 和基于文本的 IO 的箱子。 [![构建状态](https://github.com/ccbrown/iocraft/actions/workflows/commit.yaml/badge.svg?branch=main)](https://github.com/ccbrown/iocraft/actions) [![docs.rs](https://img.shields.io/docsrs/iocraft)](https://docs.rs/iocraft/)
* [gyscos/Cursive](https://github.com/gyscos/Cursive) [[cursive](https://crates.io/crates/cursive)] - 构建丰富的 TUI 应用程序
  * [ivanceras/titik](https://github.com/ivanceras/titik) - 跨平台 TUI 小部件库，旨在提供交互式小部件
* ncurses
* [ihalila/pancurses](https://github.com/ihalila/pancurses) [[pancurses](https://crates.io/crates/pancurses)] -curses 库，支持 linux 和 windows
* [jeaye/ncurses-rs](https://github.com/jeaye/ncurses-rs) [[ncurses](https://crates.io/crates/ncurses)] - [ncurses](https://invisible-island.net/ncurses/ncurses.html) 绑定
* [ogham/rust-term-grid](https://github.com/ogham/rust-term-grid) [[term_grid](https://crates.io/crates/term_grid)] - 用于将事物放入网格中的库
* [ratatui-org/ratatui](https://github.com/ratatui/ratatui) [[ratatui](https://crates.io/crates/ratatui)] - 所有关于烹饪终端用户界面 (TUI) 的库
* [redox-os/termion](https://github.com/redox-os/termion) [[termion](https://crates.io/crates/termion)] - 用于控制终端/TTY 的无绑定库
  * [ruterm](https://crates.io/crates/ruterm) - 用于 TTY 的小型且简单的库
* [subinium/SuperLightTUI](https://github.com/subinium/SuperLightTUI) [[superlighttui](https://crates.io/crates/superlighttui)] - 具有 50 多个小部件、Flexbox 布局和动画系统的即时模式 TUI 库[![CI](https://github.com/subinium/SuperLightTUI/actions/workflows/ci.yml/badge.svg)](https://github.com/subinium/SuperLightTUI/actions/workflows/ci.yml)
* 术语箱
* [gchp/rustbox](https://github.com/gchp/rustbox) [[rustbox](https://crates.io/crates/rustbox)] - 绑定到 [Termbox](https://github.com/nsf/termbox)
* [TimonPost/crossterm](https://github.com/crossterm-rs/crossterm) [[crossterm](https://crates.io/crates/crossterm)] - 跨平台终端库

### 压缩

* [7z](https://7-zip.org/7z.html)
* [[sevenz-rust](https://crates.io/crates/sevenz-rust)] - 用纯 Rust 编写的 7z 解压器/压缩器。
* [Brotli](https://opensource.googleblog.com/2015/09/introducing-brotli-new-compression.html)
  * [dropbox/rust-brotli](https://github.com/dropbox/rust-brotli) - Brotli 解压缩器可以选择性地避免 stdlib
  * [ende76/brotli-rs](https://github.com/ende76/brotli-rs) - Brotli压缩的实现
* bzip2
  * [trifectatechfoundation/bzip2-rs](https://github.com/trifectatechfoundation/bzip2-rs) - [libbz2](https://www.sourceware.org/bzip2/) 绑定
* 压缩包
* [zopfli](https://github.com/zopfli-rs/zopfli) [[zopfli](https://crates.io/crates/zopfli)] - 实现更高质量的 deflate 或 zlib 压缩的 Zopfli 压缩算法
* gzp
  * [sstadick/gzp](https://github.com/sstadick/gzp/) - deflate 格式和 snappy 的多线程编解码
* 迷你
  * [rust-lang/flate2-rs](https://github.com/rust-lang/flate2-rs) - [miniz](https://code.google.com/archive/p/miniz) 绑定 [![构建徽章](https://github.com/rust-lang/flate2-rs/workflows/CI/badge.svg?branch=master)](https://github.com/rust-lang/flate2-rs/actions)
* [paxit](https://github.com/roquess/paxit) [[paxit](https://crates.io/crates/paxit)] - 使用各种算法（zip、tar、gzip、xz、zst 等）压缩和解压缩文件的灵活库，采用模块化设计，易于扩展
* 焦油
  * [alexcrichton/tar-rs](https://github.com/alexcrichton/tar-rs) - tar 存档读/写
* 邮编
* [zip-rs/zip2](https://github.com/zip-rs/zip2) [[zip](https://crates.io/crates/zip)] - 读取和写入 ZIP 档案
* zstd
  * [gyscos/zstd-rs](https://github.com/gyscos/zstd-rs) - zstd 压缩库的 Rust 绑定

### 计算

* [alphaville/optimization-engine](https://github.com/alphaville/optimization-engine) [[optimization-engine](https://crates.io/crates/optimization_engine)] - 优化引擎 (OpEn) 是用于约束非凸优化问题的求解器 [![连续集成](https://github.com/alphaville/optimization-engine/actions/workflows/ci.yml/badge.svg?branch=master)](https://github.com/alphaville/optimization-engine/actions/workflows/ci.yml)
* [argmin-rs/argmin](https://github.com/argmin-rs/argmin) [[argmin](https://crates.io/crates/argmin)] - 优化库
* [BLAS](https://en.wikipedia.org/wiki/Basic_Linear_Algebra_Subprograms) [[blas](https://crates.io/keywords/blas)]
  * [mikkyang/rust-blas](https://github.com/mikkyang/rust-blas) - BLAS 结合
* [calebwin/emu](https://github.com/calebwin/emu) - GPGPU数值计算语言
* [dimforge/nalgebra](https://github.com/dimforge/nalgebra) - 低维线性代数库
* [faer-rs](https://github.com/sarah-quinones/faer-rs) [[faer](https://crates.io/crates/faer)] - Rust 的线性代数基础
* [fastnum](https://github.com/neogenie/fastnum) [fastnum](https://crates.io/crates/fastnum) - 在纯 Rust 中实现的快速精确十进制数。适用于金融、加密货币和任何其他固定精度计算。
* [GSL](http://www.gnu.org/software/gsl/)
  * [GuillaumeGomez/rust-GSL](https://github.com/GuillaumeGomez/rust-GSL) - GSL 绑定
* [LAPACK](https://en.wikipedia.org/wiki/LAPACK)
  * [stainless-steel/lapack](https://github.com/blas-lapack-rs/lapack) - LAPACK 绑定
* 并行
  * [arrayfire/arrayfire-rust](https://github.com/arrayfire/arrayfire-rust) - [Arrayfire](https://github.com/arrayfire) 绑定
  * [autumnai/collenchyma](https://github.com/autumnai/collenchyma) - 一个可扩展、可插拔、与后端无关的框架，用于在 CUDA、OpenCL 和通用主机 CPU 上进行并行高性能计算。
  * [luqmana/rust-opencl](https://github.com/luqmana/rust-opencl) - [OpenCL](https://www.khronos.org/opencl/) 绑定
* 科学
  * [Axect/Peroxide](https://github.com/Axect/Peroxide) - Rust 数值库，包含纯 Rust 中的线性代数、数值分析、统计和机器学习工具
  * [cool-japan/scirs](https://github.com/cool-japan/scirs) - 生产就绪的纯 Rust 科学计算，包括线性代数、优化、统计、神经网络等。 API 的灵感来自于 Python 的 SciPy。
  * [cpmech/russell](https://github.com/cpmech/russell) - Rust 科学库，用于数值数学、常微分方程、特殊数学函数、高性能（稀疏）线性代数
  * [Nonanti/mathcore](https://github.com/Nonanti/mathcore) - 具有 CAS 功能的符号数学库。支持微分、积分、方程求解和任意精度算术 [![crates.io](https://img.shields.io/crates/v/mathcore.svg)](https://crates.io/crates/mathcore)
  * [Ryan-D-Gast/differential-equations](https://github.com/Ryan-D-Gast/differential-equations) - 用于数值求解微分方程的高性能库
* 统计数据
  * [statrs-dev/statrs](https://github.com/statrs-dev/statrs) - 强大的统计计算库

### 并发性

* [crossbeam-rs/crossbeam](https://github.com/crossbeam-rs/crossbeam) - 支持并行性和低级并发
* [NikitaSmithTheOne/rate-limiters-rs](https://github.com/NikitaSmithTheOne/rate-limiters-rs) [[rate-limiters](https://crates.io/crates/rate_limiters)] - 用于速率限制的 Rust 库（漏桶、令牌桶、固定/滑动窗口）
* [orium/archery](https://github.com/orium/archery) [[archery](https://crates.io/crates/archery)] - 从 `Rc`/`Arc` 指针类型抽象的库。 [![构建徽章](https://github.com/orium/archery/workflows/CI/badge.svg)](https://github.com/orium/archery/actions?query=workflow%3ACI)
* [orx-parallel](https://crates.io/crates/orx-parallel) - 高性能、可配置且富有表现力的并行计算库。
* [Rayon](https://github.com/rayon-rs/rayon) - 数据并行库
* [rustcc/coroutine-rs](https://github.com/rustcc/coroutine-rs) - 协程库
* [zonyitoo/coio-rs](https://github.com/zonyitoo/coio-rs) - 协程I/O

### 配置

* [andoriyu/uclicious](https://github.com/andoriyu/uclicious) [[uclicious](https://crates.io/crates/uclicious)] - [libUCL](https://github.com/vstakhov/libucl) 基于功能丰富的配置库。 [![CircleCI](https://circleci.com/gh/vstakhov/libucl.svg?style=svg)](https://app.circleci.com/pipelines/github/vstakhov/libucl)
* [Kixunil/configure_me](https://github.com/Kixunil/configure_me) [[configure_me](https://crates.io/crates/configure_me)] - 用于轻松处理应用程序配置的库
* [leptonyu/cfg-rs](https://github.com/leptonyu/cfg-rs) [[cfg-rs](https://crates.io/crates/cfg-rs)] - Rust 应用程序的配置库。
* [rust-cli/config-rs](https://github.com/rust-cli/config-rs) [[config](https://crates.io/crates/config)] - 分层配置系统（对 12 因素应用程序提供强大支持）。
* [SergioBenitez/Figment](https://github.com/SergioBenitez/Figment) [[figment](https://crates.io/crates/figment)] - 一个如此自由的配置库，它是不真实的。
* [softprops/envy](https://github.com/softprops/envy) - 将环境变量反序列化为类型安全结构 [![Main](https://github.com/softprops/envy/actions/workflows/main.yml/badge.svg)](https://github.com/softprops/envy/actions/workflows/main.yml)

### 密码学

[[加密](https://crates.io/keywords/crypto)，[加密](https://crates.io/keywords/cryptography)]

* [arkworks-rs/circom-compat](https://github.com/arkworks-rs/circom-compat) - Arkworks 与 Circcom 的 R1CS 绑定，用于 Groth16 证明和见证生成。
* [briansmith/ring](https://github.com/briansmith/ring) - 使用 Rust 和 BoringSSL 的加密原语进行安全、快速、小型加密。
* [briansmith/webpki](https://github.com/briansmith/webpki) - Web PKI TLS X.509 证书验证。
* [conradkleinespel/rooster](https://github.com/conradkleinespel/rooster) [[rooster](https://crates.io/crates/rooster)] - 在终端中使用的简单密码管理器
* [cossacklabs/themis](https://github.com/cossacklabs/themis) [[themis](https://crates.io/crates/themis)] - 用于解决典型数据安全任务的高级加密库，最适合多平台应用程序。 [![构建徽章](https://circleci.com/gh/cossacklabs/themis/tree/master.svg?style=shield)](https://app.circleci.com/pipelines/github/cossacklabs/themis)
* [DaGenix/rust-crypto](https://github.com/DaGenix/rust-crypto) - 密码算法
* [dalek-cryptography/curve25519-dalek](https://github.com/dalek-cryptography/curve25519-dalek) - Curve25519操作
* [debris/tiny-keccak](https://github.com/debris/tiny-keccak) - Keccak 家族 (SHA3)
* [dusk-network/bls12-381](https://github.com/dusk-network/bls12_381) - Rust 原生 BLS12-381 增强了 zk 性能：优化的多标量乘法、自定义哈希和 serde 支持 - 非常适合注重隐私的协议和零知识应用程序。 ![构建状态](https://github.com/dusk-network/bls12_381/workflows/Continously%20integration/badge.svg) [[dusk-bls12_381](https://crates.io/crates/dusk-bls12_381)]
* [dusk-network/plonk](https://github.com/dusk-network/plonk/) - PLONK zk-SNARK 在 BLS12-381 上的高性能 Rust 原生实现，通过自定义门和 KZG10 多项式承诺进行优化，以实现高效的零知识证明。 ![构建状态](https://github.com/dusk-network/plonk/workflows/Continously%20integration/badge.svg) [[PLONK](https://crates.io/crates/dusk-plonk)]
* [dusk-network/poseidon252](https://github.com/dusk-network/Poseidon252) - Poseidon252 是基于 BLS12-381 的 Rust 原生 Poseidon 哈希，专为 zk-SNARK 效率而构建，非常适合注重隐私的协议和零知识应用程序。 ![构建状态](https://github.com/dusk-network/Poseidon252/workflows/Continously%20integration/badge.svg) [[Poseidon](https://crates.io/crates/dusk-poseidon)]
* [exonum/exonum](https://github.com/exonum/exonum) [[exonum](https://crates.io/crates/exonum)] - 区块链项目的可扩展框架
* [facebook/opaque-ke](https://github.com/facebook/opaque-ke) - 实施最近的 [OPAQUE](https://datatracker.ietf.org/doc/draft-krawczyk-cfrg-opaque/) 密码验证密钥交换。 [![构建徽章](https://github.com/facebook/opaque-ke/workflows/Rust%20CI/badge.svg?branch=master)](https://github.com/facebook/opaque-ke)
* [iddm/randomorg](https://github.com/iddm/randomorg) - random.org 客户端库。 [![板条箱徽章](https://img.shields.io/crates/v/randomorg.svg)](https://crates.io/crates/randomorg)
* [klutzy/suruga](https://github.com/klutzy/suruga) - [TLS 1.2] 的实施(https://datatracker.ietf.org/doc/html/rfc5246)
* [kn0sys/ecc-rs](https://github.com/kn0sys/ecc-rs) - 椭圆曲线加密教程的直观库 [![Crates.io 版本](https://img.shields.io/crates/v/kn0syseccrs)](https://crates.io/crates/kn0syseccrs)
* [kornelski/rust-security-framework](https://github.com/kornelski/rust-security-framework) - 安全框架的绑定（OSX 本机）
* [libOctavo/octavo](https://github.com/libOctavo/octavo) - 模块化哈希和加密库
* [orion-rs/orion](https://github.com/orion-rs/orion) - 该库旨在提供简单易用的加密货币。 “可用”意味着公开易于使用且难以误用的高级 API。 [![测试](https://github.com/orion-rs/orion/actions/workflows/test.yml/badge.svg?branch=master)](https://github.com/orion-rs/orion/actions/workflows/test.yml)
* [racum/rust-djangohashers](https://github.com/racum/rust-djangohashers) [[djangohashers](https://crates.io/crates/djangohashers)] - Django 项目中使用的密码原语的端口。它不需要 Django，仅根据其样式对密码进行哈希处理和验证。
* [rust-native-tls/rust-native-tls](https://github.com/rust-native-tls/rust-native-tls) - 本机 TLS 库的绑定
* [rust-openssl](https://github.com/rust-openssl/rust-openssl) - [OpenSSL](https://www.openssl.org/) 绑定
* [rust-random/rand](https://github.com/rust-random/rand) [[rand](https://crates.io/crates/rand)] - 综合随机数生成库，支持强和小 PRNG、随机值采样、分布和随机过程。 [![测试状态](https://github.com/rust-random/rand/actions/workflows/test.yml/badge.svg?event=push)](https://github.com/rust-random/rand/actions)
* [RustCrypto/hashes](https://github.com/RustCrypto/hashes) - 加密哈希函数的集合
* [rustls/rustls](https://github.com/rustls/rustls) - 实施传输层安全协议
* [schnorrkel](https://github.com/paritytech/schnorrkel) - Schnorr VRF 和 Ristretto 集团的签名
* [sorairolake/abcrypt](https://github.com/sorairolake/abcrypt) [[abcrypt](https://crates.io/crates/abcrypt)] - 一个简单、现代且安全的文件加密库。 [![CI](https://github.com/sorairolake/abcrypt/workflows/CI/badge.svg?branch=develop)](https://github.com/sorairolake/abcrypt/actions?query=workflow%3ACI)
* [sorairolake/scryptenc-rs](https://github.com/sorairolake/scryptenc-rs) [[scryptenc](https://crates.io/crates/scryptenc)] - scrypt 加密数据格式的实现。 [![CI](https://github.com/sorairolake/scryptenc-rs/workflows/CI/badge.svg?branch=develop)](https://github.com/sorairolake/scryptenc-rs/actions?query=workflow%3ACI)
* [verifyfetch](https://github.com/hamzaydia/verifyfetch) - 使用 Rust/WASM SHA-256 散列和恒定内存进行流文件完整性验证。浏览器中大文件的可断点续传下载。

### 数据处理

* [amv-dev/yata](https://github.com/amv-dev/yata) - 高性能技术分析库 [![构建状态](https://img.shields.io/github/workflow/status/amv-dev/yata/Rust?branch=master)](https://github.com/amv-dev/yata/actions?query=workflow%3ARust)
* [bluss/ndarray](https://github.com/rust-ndarray/ndarray) - 具有数组视图、多维切片和高效运算的 N 维数组
* [cocoindex](https://github.com/cocoindex-io/cocoindex) - ETL框架构建新鲜索引
* [DataBora/elusion](https://github.com/DataBora/elusion) [[elusion](https://crates.io/crates/elusion)] - 基于 DataFusion 构建的端到端数据工程 DataFrame 库，具有适用于 Microsoft Fabric、Azure、SharePoint、FTP、Postgres、MySQL 和 REST API 的连接器
* [datafusion](https://github.com/apache/datafusion) - DataFusion 是一个非常快速、可扩展的查询引擎，用于使用 Apache Arrow 内存格式在 Rust 中构建高质量的以数据为中心的系统。
* [GoPlasmatic/datalogic-rs](https://github.com/GoPlasmatic/datalogic-rs) [[datalogic-rs](https://crates.io/crates/datalogic-rs)] - Rust 中的高性能、类型安全的 JSONLogic 评估引擎，非常适合业务规则和动态过滤。
* [ironcalc/IronCalc](https://github.com/ironcalc/IronCalc) [[ironcalc](https://crates.io/crates/ironcalc)] - 一个新的、现代的、正在进行中的电子表格引擎。
* [kernelmachine/utah](https://github.com/kernelmachine/utah) - 数据帧结构和操作
* [lakehq/sail](https://github.com/lakehq/sail) - Sail 是用 Rust 编写的 Apache Spark 替代品，统一了批处理、流处理和计算密集型 AI 工作负载。
* [pathwaycom/pathway](https://github.com/pathwaycom/pathway) - 具有 Rust 运行时的高性能开源 Python ETL 框架，支持 300 多个数据源。
* [pg_analytics](https://github.com/paradedb/paradedb/tree/dev/pg_analytics) - PostgreSQL 扩展可将 Postgres 内的分析查询处理加速到与专用 OLAP 数据库相当的性能水平。
* [pg_lakehouse](https://github.com/paradedb/paradedb/tree/dev/pg_lakehouse) - PostgreSQL 扩展，可将 Postgres 转换为基于 AWS S3/GCS 等对象存储和 Delta Lake/Iceberg 等表格式的分析查询引擎。
* [pola-rs/polars](https://github.com/pola-rs/polars) - 快速功能完整的 DataFrame 库 [![Lint Rust](https://github.com/pola-rs/polars/actions/workflows/lint-rust.yml/badge.svg)](https://github.com/pola-rs/polars/actions)
* [weld-project/weld](https://github.com/weld-project/weld) - 数据分析应用程序的高性能运行时

### 数据流

* [arkflow-rs/arkflow](https://github.com/arkflow-rs/arkflow) - 高性能 Rust 流处理引擎 [![CI](https://github.com/arkflow-rs/arkflow/actions/workflows/rust.yml/badge.svg?branch=main)](https://github.com/arkflow-rs/arkflow/actions)
* [ArroyoSystems/arroyo](https://github.com/ArroyoSystems/arroyo) - Rust 和 SQL 中的高性能实时分析 [![CI](https://github.com/ArroyoSystems/arroyo/actions/workflows/ci.yml/badge.svg?branch=master)](https://github.com/ArroyoSystems/arroyo/actions)
* [beava-dev/beava](https://github.com/beava-dev/beava) - 单二进制特征服务器。通过 HTTP 或 TCP 推送事件，查询新的每个实体计数器并内联聚合，中间没有代理。对于欺诈、推荐、LLM 护栏和产品内分析 [![CI](https://github.com/beava-dev/beava/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/beava-dev/beava/actions)
* [fluvio](https://github.com/fluvio-community/fluvio) - 可编程数据流平台 [![CI](https://github.com/fluvio-community/fluvio/actions/workflows/ci.yml/badge.svg)](https://github.com/fluvio-community/fluvio/actions)
* [iggy](https://github.com/apache/iggy) [[iggy](https://crates.io/crates/iggy)] - 持久消息流平台，支持 QUIC、TCP 和 HTTP 传输协议 [![CI](https://github.com/apache/iggy/actions/workflows/test.yml/badge.svg)](https://github.com/apache/iggy/actions/workflows/test.yml)
* [wingfoil](https://github.com/wingfoil-io/wingfoil) - 基于图的流处理框架 [![CI](https://github.com/wingfoil-io/wingfoil/actions/workflows/rust.yml/badge.svg)](https://github.com/wingfoil-io/wingfoil/actions/workflows/rust.yml)

### 数据结构

* [alrevuelta/rs-merkle-tree](https://github.com/alrevuelta/rs-merkle-tree) - Rust 中的 Merkle 树实现，具有可配置的存储后端和哈希函数。仅固定深度和增量。针对快速证明生成进行了优化。
* [ashvardanian/NumKong](https://github.com/ashvardanian/NumKong) - 适用于 x86 AVX2 和 AVX-512 以及 Arm NEON 的 SIMD 加速矢量距离和相似度函数 [![crates.io](https://img.shields.io/crates/v/simsimd.svg)](https://crates.io/crates/simsimd)
* [becheran/grid](https://github.com/becheran/grid) [[grid](https://crates.io/crates/grid)] - 提供易于使用且快速的二维数据结构。 [![构建状态](https://github.com/becheran/grid/actions/workflows/rust.yml/badge.svg)](https://github.com/becheran/grid/actions)
* [billyevans/tst](https://github.com/billyevans/tst) [[tst](https://crates.io/crates/tst)] - 三元搜索树集合
* [contain-rs](https://github.com/contain-rs) - Rust 的 std::collections 的扩展
* [danielpclark/array_tool](https://github.com/danielpclark/array_tool) - 数组助手。您在数组上使用的一些最常见的方法在向量上可用。用于处理大多数用例的多态实现。
* [enum-map](https://codeberg.org/sugar700/enum-map) [[enum-map](https://crates.io/crates/enum-map)] - 使用数组存储值的枚举的优化映射实现。
* [fizyk20/generic-array](https://github.com/fizyk20/generic-array) - 允许使用 typenums 大小的数组的 hack
* [garro95/priority-queue](https://github.com/garro95/priority-queue)[[priority-queue](https://crates.io/crates/priority-queue)] - 实现优先级更改的优先级队列。
* [greyblake/nutype](https://github.com/greyblake/nutype) [[nutype](https://crates.io/crates/nutype)] - 定义具有验证约束的新类型结构。 [![构建状态](https://github.com/greyblake/nutype/actions/workflows/ci.yml/badge.svg)](https://github.com/greyblake/nutype/actions)
* [mrhooray/kdtree-rs](https://github.com/mrhooray/kdtree-rs) - 用于快速地理空间索引和最近邻居查找的 K 维树
* [orium/rpds](https://github.com/orium/rpds) [[rpds](https://crates.io/crates/rpds)] - 持久数据结构。 [![构建徽章](https://github.com/orium/rpds/workflows/CI/badge.svg)](https://github.com/orium/rpds/actions?query=workflow%3ACI)
* [RoaringBitmap/roaring-rs](https://github.com/RoaringBitmap/roaring-rs) - 咆哮位图
* [rust-itertools/itertools](https://github.com/rust-itertools/itertools) - 额外的迭代器适配器、函数和宏
* [tnballo/scapegoat](https://github.com/tnballo/scapegoat) [[scapegoat](https://crates.io/crates/scapegoat)] - “BTreeSet”和“BTreeMap”的安全、易错、仅堆栈替代品。 [![GitHub Actions](https://github.com/tnballo/scapegoat/workflows/test/badge.svg?branch=master)](https://github.com/tnballo/scapegoat/actions)
* [yamafaktory/hypergraph](https://github.com/yamafaktory/hypergraph) [[hypergraph](https://crates.io/crates/hypergraph)] - Hypergraph 是一个用于生成有向超图的数据结构库。 [![ci](https://github.com/yamafaktory/hypergraph/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/yamafaktory/hypergraph/actions/workflows/ci.yml)

### 数据可视化

* [blitzarx1/egui_graphs](https://github.com/blitzarx1/egui_graphs) [[egui_graphs](https://crates.io/crates/egui_graphs)] - 由 egui 和 petgraph 提供支持的交互式图形可视化小部件。 [![Crates.io](https://img.shields.io/crates/v/egui_graphs)](https://crates.io/crates/egui_graphs) [![docs.rs](https://img.shields.io/docsrs/egui_graphs)](https://docs.rs/egui_graphs)
* [djduque/pgfplots](https://github.com/djduque/pgfplots) [[pgfplots](https://crates.io/crates/pgfplots)] - 用于生成出版质量图形的库。 [![build](https://github.com/DJDuque/pgfplots/actions/workflows/rust.yml/badge.svg)](https://github.com/DJDuque/pgfplots/actions/workflows/rust.yml)
* [mazznoer/colorgrad-rs](https://github.com/mazznoer/colorgrad-rs) [[colorgrad](https://crates.io/crates/colorgrad)] - 用于数据可视化、图表、游戏、地图、生成艺术等的色阶库。
* [milliams/plotlib](https://github.com/milliams/plotlib) - Rust 数据绘图库
* [plotly](https://github.com/plotly/plotly.rs) - 密谋 Rust
* [plotpy](https://github.com/cpmech/plotpy) [[plotpy](https://crates.io/crates/plotpy)] - 使用 Python 的 Rust 绘图库 (Matplotlib)
* [plotters](https://github.com/plotters-rs/plotters) - [![构建徽章](https://github.com/plotters-rs/plotters/workflows/CI/badge.svg)](https://github.com/plotters-rs/plotters/actions)
* [rerun](https://github.com/rerun-io/rerun) - [[rerun](https://crates.io/crates/rerun)] - 用于记录计算机视觉和机器人数据（张量、点云等）的 SDK，与可视化工具配合使用，用于随着时间的推移探索该数据。
* [saresend/gust](https://github.com/saresend/Gust) - 一个小型图表/可视化工具和部分 vega 实现
* [wangjiawen2013/charton](https://github.com/wangjiawen2013/charton) - Rust 图形库的分层语法。 [![文档](https://img.shields.io/docsrs/charton/latest)](https://docs.rs/charton) [![构建状态](https://github.com/wangjiawen2013/charton/actions/workflows/ci.yml/badge.svg)](https://github.com/wangjiawen2013/charton/actions)

### 数据库

[[数据库](https://crates.io/keywords/database)]

* NoSQL [[nosql](https://crates.io/keywords/nosql)]

  * [ArangoDB](https://arangodb.com)
* [Aragog](https://gitlab.com/qonfucius/aragog) [[aragog](https://crates.io/crates/aragog)] - 轻量级 ArangoDB 对象文档、关系和图形映射器 [![pipeline状态](https://gitlab.com/qonfucius/aragog/badges/master/pipeline.svg)](https://gitlab.com/qonfucius/aragog/-/commits/master)
* [Arangors](https://github.com/fMeow/arangors) [[arangors](https://crates.io/crates/arangors)] - ArangoDB 驱动程序
* [Cassandra](https://cassandra.apache.org/_/index.html) [[cassandra](https://crates.io/keywords/cassandra), [cql](https://crates.io/keywords/cql)]
* [AlexPikalov/cdrs](https://github.com/AlexPikalov/cdrs) [[cdrs](https://crates.io/crates/cdrs)] - 本机客户端
    * [cassandra-rs](https://github.com/cassandra-rs/cassandra-rs) - 绑定到 DataStax C/C++
    * [krojew/cdrs-tokio](https://github.com/krojew/cdrs-tokio) - 用 100% Rust 编写的高级异步 Cassandra 客户端。 [![构建徽章](https://github.com/krojew/cdrs-tokio/actions/workflows/rust.yml/badge.svg)](https://github.com/krojew/cdrs-tokio/actions)
* [[cassandra-protocol](https://crates.io/crates/cassandra-protocol)] - Cassandra 协议实现。
* [[cdrs-tokio](https://crates.io/crates/cdrs-tokio)] - 生产就绪的异步 Apache Cassandra 驱动程序客户端
* CouchDB [[couchdb](https://crates.io/keywords/couchdb)]
* [chill-rs/chill](https://github.com/chill-rs/chill) [[couchdb](https://crates.io/crates/chill)] - CouchDB REST API 的客户端
* [DynamoDB](https://aws.amazon.com/dynamodb/) [[dynamodb](https://crates.io/keywords/dynamodb)]
    * [softprops/dynomite](https://github.com/softprops/dynomite) - 一个与 rusoto_dynamodb 进行强类型且方便交互的库 [![构建徽章](https://github.com/softprops/dynomite/workflows/Main/badge.svg?branch=master)](https://github.com/softprops/dynomite/actions)
* Elasticsearch [[elasticsearch](https://crates.io/keywords/elasticsearch)]
* [benashford/rs-es](https://github.com/benashford/rs-es) [[rs-es](https://crates.io/crates/rs-es)] - [Elastic](https://www.elastic.co/) REST API 客户端
* [elastic-rs/elastic](https://github.com/elastic-rs/elastic) [[elastic](https://crates.io/crates/elastic)] - elastic 是一个用 Rust 编写的高效、模块化的 Elasticsearch API 客户端 [![build徽章](https://ci.appveyor.com/api/projects/status/csa78tcumdpnbur2?svg=true)](https://ci.appveyor.com/project/KodrAus/elastic)
* 等
* [jimmycuadra/rust-etcd](https://github.com/jimmycuadra/rust-etcd) [[etcd](https://crates.io/crates/etcd)] - CoreOS 的 etcd 客户端库。
  * [InfluxDB](https://www.influxdata.com/)
    * [driftluo/InfluxDBClient-rs](https://github.com/driftluo/InfluxDBClient-rs) - 同步接口
* 等级数据库
    * [skade/leveldb](https://github.com/skade/leveldb) - [LevelDB](https://github.com/google/leveldb) 绑定
* LMDB [[lmdb](https://crates.io/keywords/lmdb)]
* [meilisearch/heed](https://github.com/meilisearch/heed) [[heed](https://crates.io/crates/heed)] - 另一个 [LMDB](https://www.symas.com/symas-embedded-database-lmdb) 绑定
* [vhbit/lmdb-rs](https://github.com/vhbit/lmdb-rs) [[lmdb-rs](https://crates.io/crates/lmdb-rs)] - [LMDB](https://www.symas.com/symas-embedded-database-lmdb) 绑定
* MongoDB [[mongodb](https://crates.io/keywords/mongodb)]
* [mongodb/mongo-rust-driver](https://github.com/mongodb/mongo-rust-driver) [[mongodb](https://crates.io/crates/mongodb)] - [MongoDB](https://www.mongodb.com/) 绑定
  * [PickleDB](https://pythonhosted.org/pickleDB/)
    * [seladb/pickledb-rs](https://github.com/seladb/pickledb-rs) - 一个轻量级且简单的键值存储，很大程度上受到 Python 的 PickleDB 的启发。
  * [PoloDB](https://www.polodb.org/)
    * [PoloDB](https://github.com/PoloDB/PoloDB) - 基于 JSON 的嵌入式数据库具有类似于 MongoDB 的 API。 ![GitHub 工作流程状态](https://img.shields.io/github/actions/workflow/status/PoloDB/PoloDB/rust.yml)
  * [Redb](https://www.redb.org/)
    * [Redb](https://github.com/cberner/redb) - 嵌入式键值数据库。它提供了与其他嵌入式键值存储（例如rocksdb和lmdb）类似的接口。 ![GitHub 工作流程状态](https://github.com/cberner/redb/actions/workflows/ci.yml/badge.svg)
* Redis [[redis](https://crates.io/keywords/redis)]
* [aembke/fred](https://github.com/aembke/fred.rs) [[fred](https://crates.io/crates/fred)] - 用于 Rust 和 Tokio 的高级异步 [Redis](https://redis.io/) 客户端。 [![CircleCI](https://circleci.com/gh/aembke/fred.rs/tree/main.svg?style=svg)]([https://circleci.com/gh/aembke/fred.rs/tree/main](https://app.circleci.com/pipelines/github/aembke/fred.rs?branch=main))
    * [redis-rs](https://github.com/redis-rs/redis-rs) - [Redis](https://redis.io/) 库 [![Rust](https://github.com/redis-rs/redis-rs/actions/workflows/rust.yml/badge.svg)](https://github.com/redis-rs/redis-rs/actions/workflows/rust.yml)
  * [RocksDB](https://rocksdb.org/)
    * [rust-rocksdb/rust-rocksdb](https://github.com/rust-rocksdb/rust-rocksdb) - RocksDB 绑定 [![RocksDB CI](https://github.com/rust-rocksdb/rust-rocksdb/actions/workflows/rust.yml/badge.svg?branch=master)](https://github.com/rust-rocksdb/rust-rocksdb/actions/workflows/rust.yml)
  * [SurrealDB](https://surrealdb.com/)
    * [surrealdb/surrealdb](https://github.com/surrealdb/surrealdb) - SurrealDB 嵌入式文档图形数据库
  * [UnQLite](https://github.com/symisc/unqlite)
    * [zitsen/unqlite.rs](https://github.com/zitsen/unqlite.rs) - UnQLite 绑定
  * [ZooKeeper](https://zookeeper.apache.org/)
* [bonifaido/rust-zookeeper](https://github.com/bonifaido/rust-zookeeper) [[zookeeper](https://crates.io/crates/zookeeper)] - Apache ZooKeeper 的客户端库。
* [krojew/rust-zookeeper](https://github.com/krojew/rust-zookeeper) [[zookeeper-async](https://crates.io/crates/zookeeper-async)] - 异步 Zookeeper 客户端，基于 tokio。  ![构建状态](https://github.com/krojew/rust-zookeeper/actions/workflows/rust.yml/badge.svg)
* OGM [[ogm](https://crates.io/keywords/ogm)]
* [Aragog](https://gitlab.com/qonfucius/aragog) [[aragog](https://crates.io/crates/aragog)] - 轻量级 ArangoDB 对象文档、关系和图形映射器 [![pipeline状态](https://gitlab.com/qonfucius/aragog/badges/master/pipeline.svg)](https://gitlab.com/qonfucius/aragog/-/commits/master)
* ORM [[orm](https://crates.io/keywords/orm)]
  * [ayarotsky/diesel-guard](https://github.com/ayarotsky/diesel-guard) - 用于 Diesel 和 SQLx 的 linter，可捕获危险的 PostgreSQL 迁移（表锁、重写、阻塞操作）并建议安全替代方案 [![crate](https://img.shields.io/crates/v/diesel-guard.svg)](https://crates.io/crates/diesel-guard)
  * [diesel-rs/diesel](https://github.com/diesel-rs/diesel) - ORM 和查询构建器
  * [ivanceras/rustorm](https://github.com/ivanceras/rustorm) - 一个 ORM
  * [njord](https://github.com/njord-rs/njord) - ⛵ 多功能、功能丰富的 Rust ORM [![构建状态](https://github.com/njord-rs/njord/actions/workflows/core.yml/badge.svg)](https://github.com/njord-rs/njord/actions/workflows/core.yml) ![crates.io](https://img.shields.io/crates/v/njord.svg)
  * [rbatis/rbatis](https://github.com/rbatis/rbatis) - 高性能ORM框架（基于JSON）
  * [SeaQL/sea-orm](https://github.com/SeaQL/sea-orm) - 🐚 异步和动态 ORM [![crate](https://img.shields.io/crates/v/sea-orm.svg)](https://crates.io/crates/sea-orm) [![docs](https://img.shields.io/docsrs/sea-orm/latest)](https://docs.rs/sea-orm) [![build状态](https://github.com/SeaQL/sea-orm/actions/workflows/rust.yml/badge.svg)](https://github.com/SeaQL/sea-orm/actions/workflows/rust.yml)
  * [SeaQL/seaography](https://github.com/SeaQL/seaography) - 🧭 SeaORM 的 GraphQL 框架 [![crate](https://img.shields.io/crates/v/seaography.svg)](https://crates.io/crates/seaography) [![docs](https://img.shields.io/docsrs/seaography/latest)](https://docs.rs/seaography) [![build状态](https://github.com/SeaQL/seaography/actions/workflows/tests.yaml/badge.svg)](https://github.com/SeaQL/seaography/actions/workflows/tests.yaml)
  * [thegenius/taitan-orm](https://github.com/thegenius/taitan-orm) - 用于 Rust、异步和编译时生成的最先进的 ORM。
* [sfackler/r2d2](https://github.com/sfackler/r2d2) - 通用连接池
* SQL [[sql](https://crates.io/keywords/sql)]
* 通用
    * [launchbadge/sqlx](https://github.com/launchbadge/sqlx) - 具有强类型支持的异步 PostgreSQL/MySQL/SQLite 连接池 [![构建徽章](https://img.shields.io/github/workflow/status/launchbadge/sqlx/Rust/master?style=flat-square)](https://github.com/launchbadge/sqlx)
    * [SeaQL/sea-query](https://github.com/SeaQL/sea-query) - 🔱 适用于 MySQL、Postgres 和 SQLite 的动态 SQL 查询生成器 [![crate](https://img.shields.io/crates/v/sea-query.svg)](https://crates.io/crates/sea-query) [![docs](https://img.shields.io/docsrs/sea-query/latest)](https://docs.rs/sea-query) [![build状态](https://github.com/SeaQL/sea-query/actions/workflows/rust.yml/badge.svg)](https://github.com/SeaQL/sea-query/actions/workflows/rust.yml)
    * [SeaQL/sea-schema](https://github.com/SeaQL/sea-schema) - 🌿 SQL 模式定义和发现 [![crate](https://img.shields.io/crates/v/sea-schema.svg)](https://crates.io/crates/sea-schema) [![docs](https://img.shields.io/docsrs/sea-schema/latest)](https://docs.rs/sea-schema) [![build状态](https://github.com/SeaQL/sea-schema/actions/workflows/rust.yml/badge.svg)](https://github.com/SeaQL/sea-schema/actions/workflows/rust.yml)
* 微软SQL
    * [prisma/tiberius](https://github.com/prisma/tiberius) - [![货物测试](https://github.com/prisma/tiberius/actions/workflows/test.yml/badge.svg?branch=master)](https://github.com/prisma/tiberius/actions/workflows/test.yml)
* MySql [[mysql](https://crates.io/keywords/mysql)]
    * [AgilData/mysql-proxy-rs](https://github.com/AgilData/mysql-proxy-rs) - MySQL 代理 [![CircleCI](https://circleci.com/gh/AgilData/mysql-proxy-rs/tree/master.svg?style=svg)](https://app.circleci.com/pipelines/github/AgilData/mysql-proxy-rs?branch=master)
* [blackbeam/mysql_async](https://github.com/blackbeam/mysql_async) [[mysql_async](https://crates.io/crates/mysql_async)] - 基于 Tokio 的异步 Mysql 驱动程序。 [![CircleCI](https://circleci.com/gh/blackbeam/mysql_async/tree/master.svg?style=shield)](https://app.circleci.com/pipelines/github/blackbeam/mysql_async?branch=master)
* [blackbeam/rust-mysql-simple](https://github.com/blackbeam/rust-mysql-simple) [[mysql](https://crates.io/crates/mysql)] - 原生 MySql 客户端
* 甲骨文
* [kubo/rust-oracle](https://github.com/kubo/rust-oracle) [[oracle](https://crates.io/crates/oracle)] - Oracle 驱动程序 [![build徽章](https://github.com/kubo/rust-oracle/actions/workflows/run-tests.yml/badge.svg?branch=master)](https://github.com/kubo/rust-oracle/actions/workflows/run-tests.yml)
* PostgreSql [[postgres](https://crates.io/keywords/postgres), [postgresql](https://crates.io/keywords/postgresql)]
    * [c410-f3r/wtx](https://github.com/c410-f3r/wtx) - 快速实施，外部依赖较少。
* [rust-postgres](https://github.com/rust-postgres/rust-postgres) [[postgres](https://crates.io/crates/postgres)] - 原生 [PostgreSQL](https://www.postgresql.org/) 客户端
* Sqlite [[sqlite](https://crates.io/keywords/sqlite)]
    * [rusqlite](https://github.com/rusqlite/rusqlite) - [Sqlite3](https://sqlite.org/index.html) 绑定
* [VennDB](https://venndb.plabayo.tech/) [[venndb](https://github.com/plabayo/venndb)] - Rust 中的仅附加内存数据库，用于使用位（标志）列查询的行。

### 日期和时间

[[日期](https://crates.io/keywords/date)，[时间](https://crates.io/keywords/time)]

* [arthurhenrique/rusti-cal](https://github.com/arthurhenrique/rusti-cal) [[rusti-cal](https://crates.io/crates/rusti-cal)] - cal(1) 克隆快如闪电 ~ 超过 9999 年 ~ 用 Rust 编写。
* [burntSushi/jiff](https://github.com/BurntSushi/jiff) - Rust 的日期时间库，鼓励您跳入成功的深渊。 [![构建状态](https://github.com/BurntSushi/jiff/workflows/ci/badge.svg)](https://github.com/BurntSushi/jiff/actions)
* [chronotope/chrono](https://github.com/chronotope/chrono) - 日期和时间库
* [Mnwa/ms](https://github.com/Mnwa/ms) [[ms-converter](https://crates.io/crates/ms-converter)] - 这是一个将人类时间转换为毫秒的库 [![build徽章](https://github.com/Mnwa/ms/workflows/build/badge.svg?branch=master)](https://github.com/Mnwa/ms/actions?query=workflow%3Abuild)
* [sorairolake/nt-time](https://github.com/sorairolake/nt-time) [[nt-time](https://crates.io/crates/nt-time)] - Windows 文件时间库。 [![CI](https://github.com/sorairolake/nt-time/workflows/CI/badge.svg?branch=develop)](https://github.com/sorairolake/nt-time/actions?query=workflow%3ACI)
* [time-rs/time](https://github.com/time-rs/time) - [![构建徽章](https://github.com/time-rs/time/workflows/Build/badge.svg)](https://github.com/time-rs/time/actions)

### 分布式系统

* 锑
* [antimonyproject/antimony](https://github.com/antemonyproject/antimony) [[antimony](https://crates.io/crates/antmony)] - 流处理/分布式计算平台
* 阿帕奇卡夫卡
* [fede1024/rust-rdkafka](https://github.com/fede1024/rust-rdkafka) [[rdkafka](https://crates.io/crates/rdkafka)] - [librdkafka](https://github.com/confluenceinc/librdkafka) 绑定
* [gklijs/schema_registry_converter](https://github.com/gklijs/schema_registry_converter) [[schema_registry_converter](https://crates.io/crates/schema_registry_converter)] - 与 [confluence schema 注册表](https://www.confluence.io/product/confluence-platform/data-compatibility/) 集成
  * [kafka-rust/kafka-rust](https://github.com/kafka-rust/kafka-rust) - Apache Kafka 的 Rust 客户端
* HDFS
* [hyunsik/hdfs-rs](https://github.com/hyunsik/hdfs-rs) [[hdfs](https://crates.io/crates/hdfs)] - libhdfs 绑定
* 其他
* [build-trust/ockam](https://github.com/build-trust/ockam) [[ockam](https://crates.io/crates/ockam)] - 分布式应用程序的端到端加密、相互身份验证和 ABAC [![构建徽章](https://github.com/build-trust/ockam/workflows/Rust/badge.svg)](https://github.com/build-trust/ockam)

### 领域驱动设计

* [serverlesstechnology/cqrs](https://github.com/serverlesstechnology/cqrs) [[cqrs-es](https://crates.io/crates/cqrs-es)] - CQRS 和事件溯源框架以及 [用户指南](https://doc.rust-cqrs.org/)

### 电子BPF

* [aya/aya-rs](https://github.com/aya-rs/aya) - 注重开发人员体验和可操作性。
* [libbpf/libbpf-rs](https://github.com/libbpf/libbpf-rs) - 一个最小且固执己见的 eBPF 工具。

### 电子邮件

[[电子邮件](https://crates.io/keywords/email)、[imap](https://crates.io/keywords/imap)、[smtp](https://crates.io/keywords/smtp)]

* [duesee/imap-codec](https://github.com/duesee/imap-codec) [[imap-codec](https://crates.io/crates/imap-codec)] - 坚如磐石且完整的 IMAP 编解码器 [![构建 &测试](https://github.com/duesee/imap-codec/actions/workflows/build_and_test.yml/badge.svg)](https://github.com/duesee/imap-codec/actions/workflows/build_and_test.yml)
* [gsquire/sendgrid-rs](https://github.com/gsquire/sendgrid-rs) - SendGrid API 库
* [jdrouet/catapulte](https://github.com/jdrouet/catapulte) - 使用 [MRML](https://github.com/jdrouet/mrml) 模板发送电子邮件的微服务。
* [jdrouet/jolimail](https://github.com/jdrouet/jolimail) - 用于构建 [MRML](https://github.com/jdrouet/mrml) 模板的 Web 应用程序。
* [jdrouet/mrml](https://github.com/jdrouet/mrml) - 一个可以生成适用于任何邮件客户端的漂亮电子邮件模板的库。
* [lettre/lettre](https://github.com/lettre/lettre) - SMTP 库 [![CI](https://github.com/lettre/lettre/actions/workflows/test.yml/badge.svg?branch=master)](https://github.com/lettre/lettre/actions/workflows/test.yml)
* [mailtutan/mailtutan](https://github.com/mailtutan/mailtutan) - 用于测试和开发环境的 SMTP 服务器。
* [meli/meli](https://github.com/meli/meli) - 🐝 终端邮件客户端
* [reacherhq/check-if-email-exists](https://github.com/reacherhq/check-if-email-exists) [[check-if-email-exists](https://crates.io/crates/check-if-email-exists)] - 在不发送任何电子邮件的情况下检查电子邮件地址是否存在，使用 SMTP 验证、一次性地址检测和全面检查 [![操作状态](https://github.com/reacherhq/check-if-email-exists/workflows/pr/badge.svg)](https://github.com/reacherhq/check-if-email-exists/actions)
* [rustmailer/bichon](https://github.com/rustmailer/bichon) - 具有全文搜索和 WebUI 的轻量级高性能电子邮件存档器。
* [staktrace/mailparse](https://github.com/staktrace/mailparse) [[mailparse](https://crates.io/crates/mailparse)] - 用于解析真实电子邮件文件的库
* [stalwartlabs/mail-auth](https://github.com/stalwartlabs/mail-auth) [[mail-auth](https://crates.io/crates/mail-auth)] - DKIM、ARC、SPF 和 DMARC 消息身份验证库 [![build徽章](https://github.com/stalwartlabs/mail-auth/actions/workflows/rust.yml/badge.svg)](https://github.com/stalwartlabs/mail-auth/actions/workflows/rust.yml)
* [stalwartlabs/mail-parser](https://github.com/stalwartlabs/mail-parser) [[mail-parser](https://crates.io/crates/mail-parser)] - 一个快速、强大的电子邮件解析库，具有完整的 MIME 支持 [![build徽章](https://github.com/stalwartlabs/mail-parser/actions/workflows/rust.yml/badge.svg)](https://github.com/stalwartlabs/mail-parser/actions/workflows/rust.yml)
* [stalwartlabs/mail-send](https://github.com/stalwartlabs/mail-send) [[mail-send](https://crates.io/crates/mail-send)] - 支持 DKIM 的电子邮件生成器和 SMTP 客户端库 [![build徽章](https://github.com/stalwartlabs/mail-send/actions/workflows/rust.yml/badge.svg)](https://github.com/stalwartlabs/mail-send/actions/workflows/rust.yml)
* [tweedegolf/mailcrab](https://github.com/tweedegolf/mailcrab) - 用于开发的电子邮件测试服务器。

### 编码

[[编码](https://crates.io/keywords/encoding)]

* ASN.1
  * [alex/rust-asn1](https://github.com/alex/rust-asn1) - ASN.1 (DER) 串行器
* 二进制
  * [bincode](https://crates.io/crates/bincode) - 二进制编码器/解码器
  * [bincode-next](https://crates.io/crates/bincode-next) - 二进制编码器/解码器，现在无人维护的二进制代码的后继者
* [jamesmunns/postcard](https://github.com/jamesmunns/postcard) [[postcard](https://crates.io/crates/postcard)] - Postcard 是 Serde 的 #![no_std] 重点序列化器和反序列化器。
* [m4b/goblin](https://github.com/m4b/goblin) [[goblin](https://crates.io/crates/goblin)] - 跨平台、零拷贝和字节序感知二进制解析
* BSON
  * [mongodb/bson-rust](https://github.com/mongodb/bson-rust) - BSON 编码和解码支持
* 字节交换
  * [BurntSushi/byteorder](https://github.com/BurntSushi/byteorder) - 支持大端、小端和本机字节顺序
* 船长原型
  * [capnproto/capnproto-rust](https://github.com/capnproto/capnproto-rust) - Cap'n Proto 是分布式系统的类型系统
* CBOR
  * [serde_cbor](https://crates.io/crates/serde_cbor) - CBOR 对 serde 的支持
* 字符编码
* [hsivonen/encoding_rs](https://github.com/hsivonen/encoding_rs) [[encoding_rs](https://crates.io/crates/encoding_rs)] - 编码标准的面向 Gecko 的实现
  * [lifthrasiir/rust-encoding](https://github.com/lifthrasiir/rust-encoding) - Rust 的字符编码支持。 （也称为 rust-encoding）它基于 WHATWG 编码标准，还提供了用于错误检测和恢复的高级接口。
* CRC
  * [mrhooray/crc-rs](https://github.com/mrhooray/crc-rs) - Rust 实现 CRC(16,32,64)，支持各种标准
* CSV
  * [BurntSushi/rust-csv](https://github.com/BurntSushi/rust-csv) - 快速灵活的 CSV 读取器和写入器，支持 Serde
* 电子数据网络
* [edn-rs](https://github.com/naomijub/edn-rs) [[edn-rs](https://crates.io/crates/edn-rs)] - 用于解析 EDN 格式并将其生成 Rust 类型的包。
* [FlatBuffers](https://flatbuffers.dev/)
  * [frol/flatc-rust](https://github.com/frol/flatc-rust) - 用于 Cargo 构建脚本的 FlatBuffers 编译器 (flatc) 集成
* 哈尔
* [mandrean/har-rs](https://github.com/mandrean/har-rs) [[har](https://crates.io/crates/har)] - HTTP 存档格式 (HAR) 序列化和反序列化库
* HTML
  * [servo/html5ever](https://github.com/servo/html5ever) - 高性能浏览器级 HTML5 解析器
* JSON
* [cloudwego/sonic-rs](https://github.com/cloudwego/sonic-rs) [[sonic-rs](https://crates.io/crates/sonic-rs)] - 基于 SIMD 的快速 Rust JSON 库。
* [importcjj/rust-ajson](https://github.com/importcjj/rust-ajson) [[ajson](https://crates.io/crates/ajson)] - 快速获取 JSON 值
* [rustadopt/jzon-rs](https://github.com/rustadopt/jzon-rs/) [[jzon](https://crates.io/crates/jzon)] - JSON 实现
* [serde-rs/json](https://github.com/serde-rs/json) [[serde\_json](https://crates.io/crates/serde_json)] - 对 [Serde](https://github.com/serde-rs/serde) 框架的 JSON 支持
* [simd-lite/simd-json](https://github.com/simd-lite/simd-json) [[simd-json](https://crates.io/crates/simd-json)] - 基于 simdjson 端口的高性能 JSON 解析器
* [vcschapp/bufjson](https://github.com/vcschapp/bufjson) [[bufjson](https://crates.io/crates/bufjson)] - 流式 JSON 解析器和词法分析器，无复制/无分配，可选流式 JSON 指针计算器
* 消息包
  * [3Hren/msgpack-rust](https://github.com/3Hren/msgpack-rust) - 低/高级 MessagePack 实现
* 网络CDF
* [georust/netcdf](https://github.com/georust/netcdf) [[netcdf](https://crates.io/crates/netcdf)] - 中级 netCDF 绑定，允许轻松读取和写入类似数组的结构到文件。
* 质子交换膜
* [jcreekmore/pem-rs](https://github.com/jcreekmore/pem-rs) [[pem](https://crates.io/crates/pem)] - 解析和编码 PEM 编码数据
* 协议缓冲区
  * [stepancheg/rust-protobuf](https://github.com/stepancheg/rust-protobuf) - Google 协议缓冲区的 Rust 实现
  * [tokio-rs/prost](https://github.com/tokio-rs/prost) - [![持续集成](https://github.com/tokio-rs/prost/workflows/continuous%20integration/badge.svg?branch=master)](https://github.com/tokio-rs/prost/actions)
* rkyv
* [rkyv/rkyv](https://github.com/rkyv/rkyv) [[rkyv](https://crates.io/crates/rkyv)] - rkyv（存档）是一个零拷贝反序列化框架
* RON（生锈的对象表示法）
  * [https://github.com/ron-rs/ron](https://github.com/ron-rs/ron) - 生锈的对象表示法
*塞尔德
  * [iddm/serde-aux](https://github.com/iddm/serde-aux/) - 与 serde 库一起使用的其他工具。 [![CI](https://github.com/iddm/serde-aux/actions/workflows/ci.yml/badge.svg)](https://github.com/iddm/serde-aux/actions/workflows/ci.yml) [![箱子徽章](https://img.shields.io/crates/v/serde-aux.svg)](https://crates.io/crates/serde-aux)
* TOML
* [tamasfe/taplo](https://github.com/tamasfe/taplo) [[taplo](https://crates.io/crates/taplo)] - TOML 工具包[![CI](https://github.com/tamasfe/taplo/workflows/Continously%20integration/badge.svg)](https://github.com/tamasfe/taplo/actions?query=workflow%3A%22Continously+integration%22)
  * [toml-rs/toml](https://github.com/toml-rs/toml) - [![CI](https://github.com/toml-rs/toml/actions/workflows/ci.yml/badge.svg)](https://github.com/toml-rs/toml/actions/workflows/ci.yml)
* [vitiral/stfu8](https://github.com/vitiral/stfu8) [[stfu8](https://crates.io/crates/stfu8)] - UTF-8 的某种文本格式
* XML
  * [Florob/RustyXML](https://github.com/Florob/RustyXML) - XML 解析器
  * [netvl/xml-rs](https://github.com/netvl/xml-rs) - 流式 XML 库
  * [shepmaster/sxd-document](https://github.com/shepmaster/sxd-document) - XML 库
  * [shepmaster/sxd-xpath](https://github.com/shepmaster/sxd-xpath) - XPath 库
  * [tafia/quick-xml](https://github.com/tafia/quick-xml) - 高性能 XML Pull 读取器/写入器
  * [yaserde](https://github.com/luminvent/yaserde) - 另一种专门用于 XML 的序列化器/反序列化器
* yaml
  * [chyh1990/yaml-rust](https://github.com/chyh1990/yaml-rust) - 缺少 YAML 1.2 实现。
  * [saphyr](https://github.com/saphyr-rs/saphyr) - 一组专用于解析 YAML 的 crate。
  * [serde-saphyr](https://github.com/bourumir-wyngs/serde-saphyr) - Serde 的 YAML（反）序列化器，强调无恐慌解析和良好的错误报告 [![crates.io](https://img.shields.io/crates/d/serde-saphyr.svg)](https://crates.io/crates/serde-saphyr)

### 文件系统

[[文件系统](https://crates.io/keywords/filesystem)]
* 运营
* [Camino](https://github.com/camino-rs/camino) [[camino](https://crates.io/crates/camino)] - 像 Rust 的 std::path::Path 一样，但是是 UTF-8。
* [dmtrKovalenko/fff](https://github.com/dmtrKovalenko/fff) [[fff-search](https://crates.io/crates/fff-search)] - 防打字错误的文件和内容搜索库，具有频率排名、git 感知注释、后台观察程序和轻量级内存内容索引。提供MCP服务器、Node/Bun SDK、C库和Neovim插件。
* [dnbln/dir-struct](https://github.com/dnbln/dir-struct) [[dir-struct](https://crates.io/crates/dir-struct)] - 使用普通 Rust 结构对文件系统树进行建模。 [![测试](https://github.com/dnbln/dir-struct/actions/workflows/test-dir-struct.yml/badge.svg?branch=trunk)](https://github.com/dnbln/dir-struct/actions/workflows/test-dir-struct.yml)
* [OpenDAL](https://github.com/apache/opendal) [[opendal](https://crates.io/crates/opendal)] - 统一的数据访问层，使用户能够无缝、高效地从不同的存储服务中检索数据。 [![build](https://img.shields.io/github/actions/workflow/status/apache/opendal/ci_core.yml?branch=main)](https://github.com/apache/opendal/actions?query=branch%3Amain)
* [ParthJadhav/Rust_Search](https://github.com/ParthJadhav/Rust_Search) [[rust_search](https://crates.io/crates/rust_search)] - 速度极快的文件搜索库。
* [pop-os/dbus-udisks2](https://github.com/pop-os/dbus-udisks2) [[dbus-udisks2](https://crates.io/crates/dbus-udisks2)] - UDisks2 DBus API
* [pop-os/sys-mount](https://github.com/pop-os/sys-mount) [[sys-mount](https://crates.io/crates/sys-mount)] - `mount` / `umount2` 系统调用的高级抽象。
* [vitiral/path_abs](https://github.com/vitiral/path_abs) [[path_abs](https://crates.io/crates/path_abs)] - 绝对可序列化路径类型和关联方法。
  * [webdesus/fs_extra](https://github.com/webdesus/fs_extra) - 扩展标准库 std::fs 和 std::io 的机会
* 临时文件
  * [Stebalien/tempfile](https://github.com/Stebalien/tempfile) - 临时文件库
* [Stebalien/xattr](https://github.com/Stebalien/xattr) [[xattr](https://crates.io/crates/xattr)] - 列出和操作 unix 扩展文件属性
* [zboxfs/zbox](https://github.com/zboxfs/zbox) [[zbox](https://crates.io/crates/zbox)] - 零细节、注重隐私的嵌入式文件系统。

### 金融

* [avhz/RustQuant](https://github.com/avhz/RustQuant) [[RustQuant](https://crates.io/crates/RustQuant)] - 定量金融库。 ![GitHub 工作流程状态（带事件）](https://img.shields.io/github/actions/workflow/status/avhz/RustQuant/build.yml)
* [d-e-s-o/apca](https://github.com/d-e-s-o/apca) [[apca](https://crates.io/crates/apca)] - 与 [Alpaca API](https://alpaca.markets/) 进行股票交易等的固执且全面的绑定。 ![GitHub 工作流程状态](https://github.com/d-e-s-o/apca/actions/workflows/test.yml/badge.svg?branch=main)
* [kand-ta/kand](https://github.com/kand-ta/kand) [[kand](https://crates.io/crates/kand)] - Rust、Python 和 JS/TS(WASM) 中的现代高性能技术分析库。 [![图片](https://img.shields.io/crates/v/kand.svg)](https://crates.io/crates/kand)
* [stochastic-rs](https://github.com/rust-dd/stochastic-rs) [[stochastic-rs](https://crates.io/crates/stochastic-rs)] - 使用量化金融工具进行随机过程的高性能数据生成库。 ![GitHub 工作流程状态](https://github.com/rust-dd/stochastic-rs/actions/workflows/rust.yml/badge.svg)

### 函数式编程

[[函数式编程](https://crates.io/keywords/fp)]
* 前奏
  * [JasonShin/fp-core.rs](https://github.com/JasonShin/fp-core.rs) - 函数式编程库
  * [myrrlyn/tap](https://github.com/myrrlyn/tap) - 后缀位置管道行为

### 游戏开发

另请参阅[我们开始玩了吗？](https://arewegameyet.rs)
* 快板
  * [SiegeLord/RustAllegro](https://github.com/SiegeLord/RustAllegro) - [Allegro 5](https://liballeg.org/) 绑定
* [Awesome Quads](https://github.com/ozkriff/awesome-quads) - 与 miniquad/macroquad 相关的代码和资源的链接的精选列表
* [Awesome wgpu](https://github.com/rofrol/awesome-wgpu) - wgpu 代码和资源的精选列表
* 括号-lib（以前为 RLTK）
* [bracket-lib](https://github.com/amethyst/bracket-lib) [[bracket-lib](https://crates.io/crates/bracket-lib)] - Roguelike 工具包 (RLTK)。 [![Rust](https://github.com/amethyst/bracket-lib/actions/workflows/rust.yml/badge.svg)](https://github.com/amethyst/bracket-lib/actions/workflows/rust.yml)
* 查隆格
* [iddm/challonge-rs](https://github.com/iddm/challonge-rs) [[challonge](https://crates.io/crates/challonge)] - Challonge REST API 的客户端库。帮助组织比赛。 [![CI](https://github.com/iddm/challonge-rs/actions/workflows/ci.yml/badge.svg)](https://github.com/iddm/challonge-rs/actions/workflows/ci.yml)
* 实体组件系统 (ECS)
  * [amethyst/specs](https://github.com/amethyst/specs) - 规格 并行 ECS
  * [legion](https://github.com/amethyst/legion) - 功能丰富的高性能 ECS 库，具有最少的样板 [![构建徽章](https://github.com/amethyst/legion/workflows/CI/badge.svg?branch=master)](https://github.com/amethyst/legion/actions)
* 游戏引擎
  * [AscendingCreations/AscendingGraphics](https://github.com/AscendingCreations/AscendingGraphics) - 使用 WGPU 和 Winit 的 2D 渲染框架。 - [![Crates.io](https://img.shields.io/crates/v/ascending_graphics.svg)](https://crates.io/crates/ascending_graphics) [![许可证](https://img.shields.io/crates/l/ascending_graphics.svg)](https://github.com/AscendingCreations/AscendingGraphics/blob/main/LICENSE.MIT) [![Crates.io](https://img.shields.io/crates/d/ascending_graphics.svg)](https://crates.io/crates/ascending_graphics)
  * [Bevy](https://github.com/bevyengine/bevy) - 是一个令人耳目一新的简单数据驱动游戏引擎。 - [![Crates.io](https://img.shields.io/crates/v/bevy.svg)](https://crates.io/crates/bevy) [![Crates.io](https://img.shields.io/crates/d/bevy.svg)](https://crates.io/crates/bevy)
  * [Fyrox](https://fyrox.rs/) - 游戏引擎 3D [![Crates.io](https://img.shields.io/crates/v/fyrox.svg)](https://crates.io/crates/fyrox) [![许可证](https://img.shields.io/crates/l/fyrox.svg)](https://github.com/FyroxEngine/Fyrox/blob/master/LICENSE.md) [![Crates.io](https://img.shields.io/crates/d/fyrox.svg)](https://crates.io/crates/fyrox)
  * [ggez](https://github.com/ggez/ggez) - 一个轻量级的游戏框架，用于以最小的摩擦制作 2D 游戏 - [![Crates.io](https://img.shields.io/crates/v/ggez.svg)](https://crates.io/crates/ggez) [![license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/ggez/ggez/blob/master/LICENSE) [![Crates.io](https://img.shields.io/crates/d/ggez.svg)](https://crates.io/crates/ggez)
  * [Kiss3d](https://github.com/dimforge/kiss3d) - 一个简单、愚蠢的 3d 图形引擎 [![Crates.io](https://img.shields.io/crates/d/kiss3d.svg)](https://crates.io/crates/kiss3d)
  * [oxidator](https://github.com/Ruddle/oxidator) - 支持WebGPU的实时策略游戏/引擎
  * [Piston](https://www.piston.rs/) - [![Crates.io](https://img.shields.io/crates/v/piston.svg?style=flat-square)](https://crates.io/crates/piston) [![Crates.io](https://img.shields.io/crates/l/piston.svg)](https://github.com/PistonDevelopers/piston/blob/master/LICENSE) [![Crates.io](https://img.shields.io/crates/d/piston.svg)](https://crates.io/crates/piston)
  * [Unrust](https://github.com/unrust/unrust) - Webgl 2.0 / 原生游戏引擎
* 游戏服务器
* [gamedig/rust-gamedig](https://github.com/gamedig/rust-gamedig) [[gamedig](https://crates.io/crates/gamedig)] - 查询游戏服务器的信息，例如名称、在线玩家、最大玩家数等。 [![Crates.io](https://img.shields.io/crates/v/gamedig.svg)](https://crates.io/crates/gamedig) [![Crates.io](https://img.shields.io/crates/d/gamedig.svg)](https://crates.io/crates/gamedig)
* [Godot](https://godotengine.org/)
  * [adalinesimonian/gdvm](https://github.com/adalinesimonian/gdvm) - CLI 的 Godot 版本管理器 [![CI](https://github.com/adalinesimonian/gdvm/actions/workflows/build-and-test.yml/badge.svg)](https://github.com/adalinesimonian/gdvm/actions/workflows/build-and-test.yml)
* [godot-rust/gdext](https://github.com/godot-rust/gdext) [[gdext](https://crates.io/crates/gdext)] - 绑定到 Godot 4+ 游戏引擎[![CI](https://github.com/godot-rust/gdext/actions/workflows/full-ci.yml/badge.svg)](https://github.com/godot-rust/gdext/actions/workflows/full-ci.yml)
* [godot-rust/gdnative](https://github.com/godot-rust/gdnative) [[gdnative](https://crates.io/crates/gdnative)] - 绑定到 Godot 3+ 游戏引擎[![CI](https://github.com/godot-rust/gdnative/actions/workflows/full-ci.yml/badge.svg)](https://github.com/godot-rust/gdnative/actions/workflows/full-ci.yml)
* 我的世界
  * [bedrock-crustaceans/bedrock-rs](https://github.com/bedrock-crustaceans/bedrock-rs) - 用于 Rust 中的 Minecraft 基岩版开发的通用工具包。 [![GitHub 星星](https://img.shields.io/github/stars/bedrock-crustaceans/bedrock-rs)](https://github.com/bedrock-crustaceans/bedrock-rs) [![CI](https://github.com/bedrock-crustaceans/bedrock-rs/actions/workflows/ci.yml/badge.svg)](https://github.com/bedrock-crustaceans/bedrock-rs/actions/workflows/ci.yml)
  * [FerrumC](https://github.com/ferrumc-rs/ferrumc) - Rust 中原始 Minecraft 服务器的升级 [![构建徽章](https://github.com/ferrumc-rs/ferrumc/actions/workflows/rust.yml/badge.svg)]
  * [Pumpkin](https://github.com/pumpkin-mc/pumpkin) - 完全用 Rust 编写的高性能 Minecraft 服务器软件
* [Raylib](https://www.raylib.com/)
* [deltaphc/raylib-rs](https://github.com/deltaphc/raylib-rs) [[raylib](https://crates.io/crates/raylib)] - raylib 的绑定
* [SDL](https://www.libsdl.org/) [[sdl](https://crates.io/keywords/sdl)]
  * [brson/rust-sdl](https://github.com/brson/rust-sdl) - SDL1 结合
  * [Rust-SDL2/rust-sdl2](https://github.com/Rust-SDL2/rust-sdl2) - SDL2 结合
* SFML
  * [jeremyletang/rust-sfml](https://github.com/jeremyletang/rust-sfml) - [SFML](https://www.sfml-dev.org/) 绑定
* 技能等级
* [atomflunder/skill空间](https://github.com/atomflunder/skill空间) [[skill空间](https://crates.io/crates/skill空间)] - 多人游戏的技能等级算法集合，如 Elo、Glicko-2、TrueSkill 等。 [![crates.io]徽章](https://img.shields.io/crates/v/skill ratings)](https://crates.io/crates/skill ratings) [![CI](https://github.com/atomflunder/skill ratings/actions/workflows/ci.yml/badge.svg)](https://github.com/atomflunder/skill ratings/actions/workflows/ci.yml)
* 榻榻米
* [giraffekey/tatami](https://github.com/giraffekey/tatami) [[tatami](https://crates.io/crates/tatami-dungeon)] - 一种 Roguelike 地下城生成算法。
* 锦标赛-rs
  * [iddm/toornament-rs](https://github.com/iddm/toornament-rs) - Toornament.com API 绑定。 [![CI](https://github.com/iddm/toornament-rs/actions/workflows/ci.yml/badge.svg)](https://github.com/iddm/toornament-rs/actions/workflows/ci.yml) [![箱子徽章](https://img.shields.io/crates/v/toornament.svg)](https://crates.io/crates/toornament)
* 维克托雷姆
* [VictoremWinbringer/Victorem](https://github.com/VictoremWinbringer/Victorem) [[Victorem](https://crates.io/crates/Victorem)] - Easy UDP 游戏服务器和 UDP 客户端框架，用于创建简单的 2D 和 3D 在线游戏原型

### 地理空间

[[geo](https://crates.io/keywords/geo)，[gis](https://crates.io/keywords/gis)]

* [apache/sedona-db](https://github.com/apache/sedona-db) - SedonaDB 是一个用 Rust 编写的地理空间 DataFrame 库。
* [DaveKram/coord_transforms](https://github.com/DaveKram/coord_transforms) [[coord_transforms](https://crates.io/crates/coord_transforms)] - 坐标变换（2-d、3-d 和地理空间）
* [Georust](https://github.com/georust) - 编写的地理空间工具和库
* [georust/geojson](https://github.com/georust/geojson) [[geojson](https://crates.io/crates/geojson)] - 用于序列化和反序列化 GeoJSON 矢量 GIS 文件格式的库。
* [MapLibre/Martin](https://github.com/maplibre/martin) - 具有 PostGIS、MBTiles、PMTiles 和 sprite 支持的地图切片服务器。 [![CI 构建](https://github.com/maplibre/martin/actions/workflows/ci.yml/badge.svg)](https://github.com/maplibre/martin/actions)[![crates.io版本](https://img.shields.io/crates/v/martin.svg)](https://crates.io/crates/martin)[![书籍](https://img.shields.io/badge/docs-Book-informational)](https://maplibre.org/martin/)
* [rust-reverse-geocoder](https://github.com/gx0r/rrgeo) - 一个快速的离线反向地理编码器，灵感来自 [thampiman/reverse-geocoder](https://github.com/thampiman/reverse-geocoder)
* [vlopes11/geomorph](https://github.com/vlopes11/geomorph) [[geomorph](https://crates.io/crates/geomorph)] - UTM、LatLon 和 MGRS 坐标之间的转换

### 图算法

* [neo4j-labs/graph](https://github.com/neo4j-labs/graph) - 高性能图算法库 [![graph CI status](https://img.shields.io/github/workflow/status/neo4j-labs/graph/CI/main?label=CI)](https://github.com/neo4j-labs/graph/actions/workflows/rust.yml)
* [petgraph/petgraph](https://github.com/petgraph/petgraph) - 图数据结构库。 [![图 CI 状态](https://github.com/petgraph/petgraph/workflows/Continously%20integration/badge.svg?branch=master)](https://github.com/petgraph/petgraph/actions/workflows/ci.yml)

### 图形

[[图形](https://crates.io/keywords/graphics)]

* 字体
  * [redox-os/rusttype](https://github.com/redox-os/rusttype) - FreeType 等库的替代品
  * [rustybuzz](https://github.com/harfbuzz/rustybuzz) - 增量 harfbuzz 端口
* [gfx-rs/gfx](https://github.com/gfx-rs/gfx) - 高性能、无绑定图形 API。
* [gfx-rs/wgpu](https://github.com/gfx-rs/wgpu) - 基于 gfx-hal 的原生 WebGPU 实现。 [![构建徽章](https://github.com/gfx-rs/wgpu/workflows/CI/badge.svg?branch=master)](https://github.com/gfx-rs/wgpu/actions)
* OpenGL [[opengl](https://crates.io/keywords/opengl)]
  * [gl-rs](https://github.com/rust-windowing/gl-rs) - OpenGL函数指针加载器
  * [glium/glium](https://github.com/glium/glium) - 安全的 OpenGL 包装器。
  * [glutin](https://crates.io/crates/glutin) - [GLFW](https://www.glfw.org/) 的替代方案
  * [PistonDevelopers/glfw-rs](https://github.com/PistonDevelopers/glfw-rs) - GLFW3 绑定和惯用包装器
* PDF
* [bastibense/libharu_ng](https://github.com/bastibense/libharu_ng) [[libharu_ng](https://crates.io/crates/libharu_ng)] - 从 Rust 应用程序轻松生成 PDF。
  * [fschutt/printpdf](https://github.com/fschutt/printpdf) - PDF书写库
  * [J-F-Liu/lopdf](https://github.com/J-F-Liu/lopdf) - PDF文档操作
  * [kaj/rust-pdf](https://github.com/kaj/rust-pdf) - 用纯 Rust 生成 PDF 文件
* [yfedoseev/pdf_oxy](https://github.com/yfedoseev/pdf_oxy) [[pdf_oxy](https://crates.io/crates/pdf_oxy)] - 使用 Python 绑定快速提取、创建和编辑 PDF 文本
* [Vulkan](https://www.vulkan.org/) [[vulkan](https://crates.io/keywords/vulkan)]
* [爆发](https://gitlab.com/Friz64/erupt) [[爆发](https://crates.io/crates/erupt)] - [![构建徽章](https://gitlab.com/Friz64/erupt/badges/main/pipeline.svg)](https://gitlab.com/Friz64/erupt/-/pipelines)
* [vulkano](https://github.com/vulkano-rs/vulkano) [[vulkano](https://crates.io/crates/vulkano)] - Vulkan API 周围安全且丰富的 Rust 包装器

### 图形用户界面

[[gui](https://crates.io/keywords/gui)]

* [autopilot-rs/autopilot-rs](https://github.com/autopilot-rs/autopilot-rs) - 一个简单的跨平台 GUI 自动化库。
* 可可
  * [servo/core-foundation-rs](https://github.com/servo/core-foundation-rs) - Rust 绑定到 Core Foundation 以及 Mac OS X 和 iOS 上的其他低级库
* [DioxusLabs/dioxus](https://github.com/dioxuslabs/dioxus) - 一个可移植、高性能且符合人体工程学的框架，用于在 Rust 中构建跨平台用户界面。 ![rust ci](https://github.com/dioxuslabs/dioxus/actions/workflows/main.yml/badge.svg)
* [emilk/egui](https://github.com/emilk/egui) - 简单、快速且高度可移植的即时模式 GUI 库。 egui 在网络上、本机以及您最喜欢的游戏引擎中运行。 [![构建状态](https://github.com/emilk/egui/workflows/CI/badge.svg)](https://github.com/emilk/egui/actions?workflow=CI)
* [emoon/rust_minifb](https://github.com/emoon/rust_minifb) - minifb 是一个跨平台窗口设置，具有可选的位图渲染。它还配备了简单的鼠标和键盘输入。主要为原型设计而设计
* [FerrisMind/shadcn-rs](https://github.com/FerrisMind/shadcn-rs) [[iced-shadcn](https://crates.io/crates/iced-shadcn)] - 具有 shadcn/ui 美学的iced 和 egui 组件集；包括 [egui-shadcn](https://crates.io/crates/egui-shadcn)。
* [FLTK](https://www.fltk.org/)
  * [fltk-rs](https://github.com/fltk-rs/fltk-rs) - FLTK 绑定 [![Build](https://github.com/fltk-rs/fltk-rs/workflows/Build/badge.svg?branch=master)](https://github.com/fltk-rs/fltk-rs/actions)
* [Flutter](https://flutter.dev/)
  * [cunarist/rinf](https://github.com/cunarist/rinf) - Rust 作为您的 Flutter 后端，Flutter 作为您的 Rust 前端 [![构建测试](https://github.com/cunarist/rinf/actions/workflows/build_test.yaml/badge.svg)](https://github.com/cunarist/rinf/actions/workflows/build_test.yaml?query=branch%3Amain)
  * [flutter-rs](https://github.com/flutter-rs/flutter-rs) - 使用 dart 和 Rust 构建 flutter 桌面应用程序。
  * [fzyzcjy/flutter_rust_bridge](https://github.com/fzyzcjy/flutter_rust_bridge) - 适用于 Flutter/Dart <-> Rust 的高级内存安全绑定生成器
* [fschutt/azul](https://github.com/fschutt/azul) - 一个免费的、实用的、面向 IMGUI 的 GUI 框架，用于快速开发用 Rust 编写的桌面应用程序，并由 Mozilla WebRender 渲染引擎支持。
* [GTK+](https://www.gtk.org/) [[gtk](https://crates.io/keywords/gtk)]
  * [gtk-rs/gtk4-rs](https://github.com/gtk-rs/gtk4-rs) - GTK4 绑定 ![CI](https://github.com/gtk-rs/gtk4-rs/workflows/CI/badge.svg)
  * [relm](https://github.com/antoyo/relm) - 异步、基于 GTK+ 的 GUI 库，灵感来自 Elm
* [iced-rs/iced](https://github.com/iced-rs/iced) [[iced](https://crates.io/crates/iced)] - 一个跨平台 GUI 库，专注于简单性和类型安全。灵感来自榆树。
* [ImGui](https://github.com/ocornut/imgui)
  * [imgui-rs](https://github.com/imgui-rs/imgui-rs) - ImGui 的绑定 [![构建状态](https://github.com/imgui-rs/imgui-rs/workflows/ci/badge.svg?branch=master)](https://github.com/imgui-rs/imgui-rs/actions)
* [IUP](http://webserver2.tecgraf.puc-rio.br/iup/)
  * [Kiss-ui](https://github.com/KISS-UI/kiss-ui) - 基于IUP构建的简单UI框架
* [ivanceras/sauron-native](https://github.com/ivanceras/sauron-native) - 一个真正的本机跨平台 GUI 库。一种统一的代码可以作为本机 GUI、Html Web 和 TUI 运行。
* [libui](https://github.com/andlabs/libui)
  * [rust-native-ui/libui-rs](https://github.com/rust-native-ui/libui-rs) - 力比绑定。
* [longbridge/gpui-component](https://github.com/longbridge/gpui-component) [[gpui-component](https://crates.io/crates/gpui-component)] - 用于使用 GPUI 构建出色的桌面应用程序的 UI 组件。
* [makepad/makepad](https://github.com/makepad/makepad) [[makepad-widgets](https://crates.io/crates/makepad-widgets)] - Makepad 是一个创意软件开发平台，可编译为 wasm/webGL、osx/metal、windows/dx11 linux/opengl。
* [Nuklear](https://github.com/Immediate-Mode-UI/Nuklear)
  * [nuklear-rust](https://github.com/snuk182/nuklear-rust) - 核绑定
* [OrbTk](https://github.com/redox-os/orbtk) - Orbital Widget Toolkit 是一个使用 SDL2 的多平台 (G)UI 工具包 [![构建和测试](https://github.com/redox-os/orbtk/workflows/build/badge.svg?branch=develop)](https://github.com/redox-os/orbtk/actions)
* [PistonDevelopers/conrod](https://github.com/PistonDevelopers/conrod/) - 易于使用的即时模式 2D GUI 库
* [project-blinc/Blinc](https://github.com/project-blinc/Blinc) [[blinc_app](https://crates.io/crates/blinc_app)] - 一个 GPU 加速的跨平台 UI 框架，具有受 GPUI 启发的构建器 API、玻璃形态效果、弹簧物理动画以及桌面、Android 和 iOS 上的本机渲染。
* [Qt](https://doc.qt.io)
  * [cyndis/qmlrs](https://github.com/cyndis/qmlrs) - QtQuick 绑定
  * [rust-qt](https://github.com/rust-qt) - Rust 的 Qt 绑定
  * [woboq/qmetaobject-rs](https://github.com/woboq/qmetaobject-rs) - 通过在编译时构建 QMetaObject 来集成 Qml 和 Rust。
* [Ribir](https://github.com/RibirX/Ribir) - Ribir 是一个 Rust GUI 框架，可帮助您从单个代码库构建美观的本机多平台应用程序。
* [rise-ui](https://github.com/rise-ui/rise) - 简单的基于组件的跨平台 GUI 工具包，用于开发美观且用户友好的界面。
* [saurvs/nfd-rs](https://github.com/saurvs/nfd-rs) - [nativefiledialog](https://github.com/mlabbe/nativefiledialog) 绑定
* [Sciter](https://sciter.com/)
  * [sciter-sdk/rust-sciter](https://github.com/sciter-sdk/rust-sciter) - Sciter 绑定 [![构建徽章](https://ci.appveyor.com/api/projects/status/github/sciter-sdk/rust-sciter?svg=true)](https://ci.appveyor.com/project/sciter-sdk/rust-sciter)
* [slint-ui/slint](https://github.com/slint-ui/slint) [slint](https://crates.io/crates/slint) - [Slint](https://slint.dev/) 是一个为嵌入式设备和桌面应用程序高效开发流畅图形用户界面的工具包。 [![构建状态](https://github.com/slint-ui/slint/workflows/CI/badge.svg?branch=master)](https://github.com/slint-ui/slint/actions?query=workflow%3ACI)
* [tauri-apps/tauri](https://github.com/tauri-apps/tauri) - 使用由 [WRY](https://github.com/tauri-apps/wry) 提供支持的 Web 前端构建更小、更快、更安全的桌面应用程序。 [![测试库](https://img.shields.io/github/workflow/status/tauri-apps/tauri/test%20library?label=test%20library)](https://github.com/tauri-apps/tauri/actions?query=workflow%3A%22test+library%22)
* [tauri-apps/wry](https://github.com/tauri-apps/wry) - Webview 渲染库。
* [xilem](https://github.com/linebender/xilem) - 数据优先 UI 设计工具包 [druid](https://github.com/linebender/druid) 的后继者。

### 图像处理

* [abonander/img_hash](https://github.com/abonander/img_hash) - 感知图像散列以及相等性和相似性的比较。
* [Enet4/dicom-rs](https://github.com/Enet4/dicom-rs) - DICOM 标准的纯 Rust 实现，允许用户使用 DICOM 对象并与 DICOM 应用程序交互，同时旨在快速、安全和直观地使用。
* [image-rs/image](https://github.com/image-rs/image) - 基本图像处理功能以及图像格式转换的方法
* [image-rs/imageproc](https://github.com/image-rs/imageproc) - 一个图像处理库，基于“image”库。
* [marekm4/dominant_color](https://github.com/marekm4/dominant_color) [[dominant_color](https://crates.io/crates/dominant_color)] - 主色提取器！[构建徽章](https://github.com/marekm4/dominant_color/actions/workflows/rust.yml/badge.svg?branch=master)
* [rust-cv/cv](https://github.com/rust-cv/cv) - 实施计算机视觉算法、抽象和系统。尽可能支持 `#[no_std]`。 ![构建徽章](https://github.com/rust-cv/cv/workflows/tests/badge.svg)
* [teovoinea/steganography](https://github.com/teovoinea/steganography) [[steganography](https://crates.io/crates/steganography)] - 一个简单的隐写库
* [twistedfall/opencv-rust](https://github.com/twistedfall/opencv-rust) - OpenCV 的绑定

### 语言规范

* [shnewto/bnf](https://github.com/shnewto/bnf) - 用于解析巴科斯-诺尔形式上下文无关语法的库。

### 许可

* [WyvernIXTL/license-fetcher](https://github.com/WyvernIXTL/license-fetcher) [[license-fetcher](https://crates.io/crates/license-fetcher)] - 在构建时获取依赖项的许可证并将其嵌入到您的程序中。

### 记录

[[日志](https://crates.io/keywords/log)]

* [donnie4w/tklog](https://github.com/donnie4w/tklog "donnie4w/tklog") - 轻量级且高效的 Rust 结构化日志库，支持日志级别、文件分段、压缩归档。
* [estk/log4rs](https://github.com/estk/log4rs) - 以 Java 的 Logback 和 log4j 库为模型的高度可配置的日志框架 [![CircleCI](https://circleci.com/gh/estk/log4rs.svg?style=shield)](https://app.circleci.com/pipelines/github/estk/log4rs)
* [fast/logforth](https://github.com/fast/logforth) - 适用于 Rust 应用程序的多功能、可扩展且易于使用的日志记录框架。它允许您配置多个调度、过滤器和附加程序，以根据您的需要自定义日志记录设置。
* [rbatis/fast_log](https://github.com/rbatis/fast_log) - 异步日志 高性能异步日志记录
* [rust-lang/log](https://github.com/rust-lang/log) - 日志记录实现
* [seanmonstar/pretty-env-logger](https://github.com/seanmonstar/pretty-env-logger) - 一个漂亮、易于使用的记录器。
* [slog-rs/slog](https://github.com/slog-rs/slog) - 结构化、可组合的日志记录
* [tokio-rs/tracing](https://github.com/tokio-rs/tracing) - 用于异步感知结构化日志记录、错误处理、指标等的应用程序级跟踪框架 [![构建状态](https://github.com/tokio-rs/tracing/workflows/CI/badge.svg?branch=master)](https://github.com/tokio-rs/tracing/actions?query=workflow%3ACI)

### 宏

* 可爱
  * [mattgathu/cute](https://github.com/mattgathu/cute) - Python 式列表推导式的宏。
* [elastio/bon](https://github.com/elastio/bon) [[bon](https://crates.io/crates/bon)] - 为结构和函数生成编译时检查的构建器，为函数和方法提供部分应用程序、可选和命名参数。 [![构建状态](https://github.com/elastio/bon/actions/workflows/ci.yml/badge.svg)](https://github.com/elastio/bon/actions)
* [Linq-in-Rust](https://github.com/StardustDL/Linq-in-Rust) - 类似 C#-LINQ 表达式的宏和方法。 [![CI](https://github.com/StardustDL/Linq-in-Rust/workflows/CI/badge.svg?branch=master)](https://github.com/StardustDL/Linq-in-Rust/actions?query=workflow%3ACI)

### 标记语言

* 通用标记
  * [pulldown-cmark/pulldown-cmark](https://github.com/pulldown-cmark/pulldown-cmark) - [CommonMark](https://commonmark.org/) 解析器
* [insomnimus/tidier](https://github.com/insomnimus/tidier) [[tidier](https://crates.io/crates/tidier)] - 用于格式化 HTML、XHTML 和 XML 文档的库。 [![构建徽章](https://github.com/insomnimus/tidier/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/insomnimus/tidier/actions)

### 手机

* 安卓/iOS
  * [ivnsch/rust_android_ios](https://github.com/ivnsch/rust_android_ios) - 分别使用 rust-swig 和 cbindgen 为 Android 和 iOS 使用共享库的示例。
* 通用
  * [Geal/rust_on_mobile](https://github.com/Geal/rust_on_mobile) - iOS CocoaPods / Android JNI
* [redbadger/crux](https://github.com/redbadger/crux) [[crux_core](https://crates.io/crates/crux_core)] - 跨平台应用程序开发。 Crux 可帮助您在移动设备 (iOS/Android) 和 Web 上共享应用程序的业务逻辑和行为 - 作为单个可重用核心。 [![构建状态](https://img.shields.io/github/actions/workflow/status/redbadger/crux/build.yaml)](https://github.com/redbadger/crux/actions)
* iOS
  * [TimNN/cargo-lipo](https://github.com/TimNN/cargo-lipo) - 一个 Cargo lipo 子命令，可自动创建与您的 iOS 应用程序一起使用的通用库。

### 网络编程

* 蓝牙
* [bluez/bluer](https://github.com/bluez/bluer) [[bluer](https://crates.io/crates/bluer)] - 官方 BlueZ 绑定。 [![构建徽章](https://github.com/bluez/bluer/actions/workflows/rust.yml/badge.svg?branch=master)](https://github.com/bluez/bluer/actions/workflows/rust.yml)
* 合作协议
  * [Covertness/coap-rs](https://github.com/Covertness/coap-rs) - [约束应用协议 (CoAP)](https://datatracker.ietf.org/doc/html/rfc7252) 库。
* DNS
* [kweonminsung/bind9_rndc_rust](https://github.com/kweonminsung/bind9_rndc_rust) [[rndc](https://crates.io/crates/rndc)] - Rust 的 BIND9 RNDC 协议实现[![CI](https://github.com/kweonminsung/bind9_rndc_rust/actions/workflows/ci.yml/badge.svg)](https://github.com/kweonminsung/bind9_rndc_rust/actions/workflows/ci.yml)
* 码头工人
  * [fussybeaver/bollard](https://github.com/fussybeaver/bollard) - Docker 守护进程 API
* FTP
  * [mattnenterprise/rust-ftp](https://github.com/mattnenterprise/rust-ftp) - 一个 [FTP](https://en.wikipedia.org/wiki/File_Transfer_Protocol) 客户端
* gRPC
  * [hyperium/tonic](https://github.com/hyperium/tonic) - 具有 async/await 支持的本机 gRPC 客户端和服务器实现 [![Crates.io](https://img.shields.io/crates/v/tonic)](https://crates.io/crates/tonic)
  * [tikv/grpc-rs](https://github.com/tikv/grpc-rs) - 基于 C Core 库和 future 构建的 gRPC 库
* HTTP
  * [deboa](https://crates.io/crates/deboa) - 一个基于 hyper 的友好 http 客户端，带有多个插件、序列化格式和宏。 [![Crates.io](https://img.shields.io/crates/v/deboa)]
  * [Hurl](https://github.com/Orange-OpenSource/hurl) - 使用纯文本和 libcurl 运行和测试 HTTP 请求 [![CI](https://github.com/Orange-OpenSource/hurl/workflows/CI/badge.svg)](https://github.com/Orange-OpenSource/hurl/actions)
* IP网络
  * [achanda/ipnetwork](https://github.com/achanda/ipnetwork) - 用于 IP 网络的库
  * [candrew/netsim](https://github.com/canndrew/netsim) - 用于网络模拟和测试的库
* 低电平
  * [actix/actix](https://github.com/actix/actix) - 演员库
  * [dylanmckay/protocol](https://github.com/dylanmckay/protocol) - 自定义 TCP/UDP 协议定义
  * [libpnet/libpnet](https://github.com/libpnet/libpnet) - 跨平台、低层网络
  * [smoltcp-rs/smoltcp](https://github.com/smoltcp-rs/smoltcp) - 专为裸机实时系统设计的独立、事件驱动的 TCP/IP 堆栈
* 消息io
  * [lemunozm/message-io](https://github.com/lemunozm/message-io) - 事件驱动的消息库可轻松快速地构建网络应用程序。支持 TCP、UDP 和 WebSocket。 [![构建徽章](https://img.shields.io/github/workflow/status/lemunozm/message-io/message-io%20ci)](https://github.com/lemunozm/message-io/actions?query=workflow%3A%22message-io+ci%22)
* MQTT
  * [bytebeamio/rumqtt](https://github.com/bytebeamio/rumqtt) - 一个库，供开发人员构建通过 TCP 和 WebSocket 与 [MQTT 协议](https://mqtt.org) 进行通信的应用程序，无论是否使用 TLS。 [![构建和测试](https://github.com/bytebeamio/rumqtt/actions/workflows/build.yml/badge.svg)](https://github.com/bytebeamio/rumqtt/actions/workflows/build.yml)
  * [rmqtt/rmqtt](https://github.com/rmqtt/rmqtt) - MQTT Server/MQTT Broker - 适用于 5G 时代物联网的可扩展分布式 MQTT 消息代理
* 纳米信息
  * [thehydroimpulse/nanomsg.rs](https://github.com/thehydroimpulse/nanomsg.rs) - [nanomsg](https://nanomsg.org/) 绑定
* NATS
  * [nats-io/nats.rs](https://github.com/nats-io/nats.rs) - NATS（云原生消息传递系统）的客户端。 [![构建状态](https://github.com/nats-io/nats.rs/workflows/Rust/badge.svg?branch=master)](https://github.com/nats-io/nats.rs/actions)
* 宁格
* [neachdainn/nng-rs](https://gitlab.com/neachdainn/nng-rs) [[Nng](https://crates.io/crates/nng)] - [Nng (nanomsg v2)](https://nng.nanomsg.org/index.html) 绑定 [![build徽章](https://gitlab.com/neachdainn/nng-rs/badges/master/pipeline.svg)](https://gitlab.com/neachdainn/nng-rs/-/pipelines)
* NNTP
* [mattnenterprise/rust-nntp](https://github.com/mattnenterprise/rust-nntp) [[nntp](https://crates.io/crates/nntp)] - 一个 [NNTP](https://en.wikipedia.org/wiki/Network_News_Transfer_Protocol) 客户端
* P2P
  * [libp2p/rust-libp2p](https://github.com/libp2p/rust-libp2p) - libp2p 网络堆栈的实现。 [![Circle CI](https://circleci.com/gh/libp2p/rust-libp2p.svg?style=svg)](https://app.circleci.com/pipelines/github/libp2p/rust-libp2p)
* [n0-computer/iroh](https://github.com/n0-computer/iroh) [[iroh](https://crates.io/crates/iroh)] - 用于在设备之间建立直接连接的板条箱[![CI](https://github.com/n0-computer/iroh/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/n0-computer/iroh/actions/workflows/ci.yml)
* POP3
* [mattnenterprise/rust-pop3](https://github.com/mattnenterprise/rust-pop3) [[pop3](https://crates.io/crates/pop3)] - 一个 [POP3](https://en.wikipedia.org/wiki/Post_Office_Protocol) 客户端
* 快速
  * [aws/s2n-quic](https://github.com/aws/s2n-quic) - IETF QUIC 协议的实现！[ci](https://img.shields.io/github/actions/workflow/status/aws/s2n-quic/ci.yml?branch=main)
  * [cloudflare/quiche](https://github.com/cloudflare/quiche) - QUIC 传输协议和 HTTP/3 的 cloudflare 实现！[build](https://img.shields.io/github/actions/workflow/status/cloudflare/quiche/stable.yml?branch=master)
  * [mozilla/neqo](https://github.com/mozilla/neqo) - QUIC 的实现
  * [quinn-rs/quinn](https://github.com/quinn-rs/quinn) - 基于 Futures 的 QUIC 实现 [![构建徽章](https://dev.azure.com/dochtman/Projects/_apis/build/status/Quinn?branchName=master)](https://dev.azure.com/dochtman/Projects/_build)
  * [tencent/tquic](https://github.com/Tencent/tquic) - 高性能、轻量级、跨平台的 QUIC 库 [![构建状态](https://img.shields.io/github/actions/workflow/status/tencent/tquic/rust.yml)](https://github.com/Tencent/tquic/actions/workflows/rust.yml)
* 拉克网
  * [b23r0/rust-raknet](https://github.com/b23r0/rust-raknet) - RakNet 协议实现 [![构建状态](https://img.shields.io/github/workflow/status/b23r0/rust-raknet/Rust)](https://github.com/b23r0/rust-raknet/actions/workflows/rust.yml)
* 远程过程调用
* [remoc-rs/remoc](https://github.com/remoc-rs/remoc) [[remoc](https://crates.io/crates/remoc)] - Remoc 提供类似于 Tokio 的通道（广播、mpsc、oneshot、watch）以及通过任何远程传输进行特征调用。 [![构建徽章](https://github.com/remoc-rs/remoc/actions/workflows/rust.yml/badge.svg?branch=master)](https://github.com/remoc-rs/remoc/actions/workflows/rust.yml)
  * [smallnest/rpcx-rs](https://github.com/smallnest/rpcx-rs) - 一个用于以简单的方式开发微服务的 RPC 库。
* 会话协议
  * [restsend/rsipstack](https://github.com/restsend/rsipstack) - 符合 RFC 3261 的 SIP 堆栈
* 套接字.io
* [1c3t3a/rust-socketio](https://github.com/1c3t3a/rust-socketio) [[rust_socketio](https://crates.io/crates/rust_socketio)] - 用 Rust 编写的 [socket.io](https://socket.io) 客户端的实现。 [![构建徽章](https://github.com/1c3t3a/rust-socketio/actions/workflows/build.yml/badge.svg)](https://github.com/1c3t3a/rust-socketio/actions/workflows/build.yml)
* SSH
  * [alexcrichton/ssh2-rs](https://github.com/alexcrichton/ssh2-rs) - [libssh2](https://libssh2.org/) 绑定
* [Thrussh](https://pijul.org/thrussh) [[thrussh](https://crates.io/crates/thrussh)] - 一个 SSH 库，由 [libsodium](https://doc.libsodium.org/) 支持
* 跺脚
  * [zslayton/stomp-rs](https://github.com/zslayton/stomp-rs) - [STOMP 1.2](http://stomp.github.io/stomp-specification-1.2.html) 客户端实现
* VPN
  * [defguard/wireguard-rs](https://github.com/DefGuard/wireguard-rs) - 多平台库提供统一的高级 API，用于使用本机操作系统内核和用户空间 WireGuard 协议实现来管理 WireGuard 接口
* 泽诺
  * [eclipse-zenoh-flow/zenoh-flow](https://github.com/eclipse-zenoh-flow/zenoh-flow) - 用于从*云*到*事物*的计算的声明性框架
  * [eclipse-zenoh/zenoh](https://github.com/eclipse-zenoh/zenoh) - 零开销网络协议
* 零MQ
  * [erickt/rust-zmq](https://github.com/erickt/rust-zmq) - [ZeroMQ](https://zeromq.org/) 绑定

### 解析

* [0xlane/pe-sign](https://github.com/0xlane/pe-sign) [[pe-sign]](https://crates.io/crates/pe-sign) - 一个跨平台的 Rust no-std 库，用于从 PE 文件中验证和提取签名信息。 [![crates.io](https://img.shields.io/crates/v/pe-sign)](https://crates.io/crates/pe-sign) [![build](https://github.com/0xlane/pe-sign/actions/workflows/rust.yml/badge.svg)](https://github.com/0xlane/pe-sign/actions/workflows/rust.yml)
  * [cchexcode/wavefront_rs](https://github.com/cchexcode/wavefront_rs) - Wavefront OBJ 格式的解析器。 [![crates.io](https://img.shields.io/crates/v/wavefront_rs.svg)](https://crates.io/crates/wavefront_rs) [![crates.io](https://img.shields.io/crates/d/wavefront_rs?label=crates.io%20downloads)](https://crates.io/crates/wavefront_rs) [![build徽章](https://github.com/cchexcode/wavefront_rs/workflows/pipeline/badge.svg?branch=master)](https://github.com/cchexcode/wavefront_rs/actions)
* [comex/rust-shlex](https://github.com/comex/rust-shlex) [[shlex](https://crates.io/crates/shlex)] - 将字符串拆分为 shell 单词，就像 Python 的 shlex 一样。 [![构建徽章](https://github.com/comex/rust-shlex/actions/workflows/test.yml/badge.svg?branch=master)](https://github.com/comex/rust-shlex/actions/workflows/test.yml)
  * [Eliah-Lakhin/lady-deirdre](https://github.com/Eliah-Lakhin/lady-deirdre) - 新编程语言和 LSP 服务器的框架。
  * [firecrawl/pdf-inspector](https://github.com/firecrawl/pdf-inspector) - 用于 PDF 分类和文本提取的快速 Rust 库。
  * [Folyd/robotstxt](https://github.com/Folyd/robotstxt) - Google 的 robots.txt 解析器和匹配器 C++ 库的端口
  * [freestrings/jsonpath](https://github.com/freestrings/jsonpath) - [JsonPath](https://goessner.net/articles/JsonPath/) 引擎。也支持 WebAssembly 和 Javascript
  * [hmeyer/stl_io](https://crates.io/crates/stl_io) - STL（STereoLithography）文件的解析器
  * [igumnoff/shiva](https://github.com/igumnoff/shiva) - Shiva 库：用 Rust 实现任何类型文档（纯文本、Markdown、HTML、PDF 等）的解析器和生成器
  * [kevinmehall/rust-peg](https://github.com/kevinmehall/rust-peg) - 解析表达式语法 (PEG) 解析器生成器
  * [lalrpop/lalrpop](https://github.com/lalrpop/lalrpop) - LR(1) 解析器生成器
  * [m4rw3r/chomp](https://github.com/m4rw3r/chomp) - 快速单子式解析器组合器
  * [Marwes/combine](https://github.com/Marwes/combine) - 解析器组合器库
* [nrc/zero](https://github.com/nrc/zero) [[zero](https://crates.io/crates/zero/)] - 二进制数据的零分配解析
* [oxc-project/oxc](https://github.com/oxc-project/oxc) [[oxc](https://crates.io/crates/oxc)] - 用 Rust 编写的高性能 JavaScript/TypeScript 解析器、转换器、压缩器和解析器。支持 Rolldown、Nuxt、Nova 等。 [![构建状态](https://github.com/oxc-project/oxc/actions/workflows/ci.yml/badge.svg?event=push&branch=main)](https://github.com/oxc-project/oxc/actions/workflows/ci.yml)
  * [pest-parser/pest](https://github.com/pest-parser/pest) - 优雅的解析器
  * [ptal/oak](https://github.com/ptal/oak) - 类型化 PEG 解析器生成器（编译器插件）
* [run-llama/liteparse](https://github.com/run-llama/liteparse) [[liteparse](https://crates.io/crates/liteparse)] - 快速、轻型 PDF 解析库，具有空间文本提取、边界框、灵活的 OCR（Tesseract/HTTP 服务器）和多语言绑定（Rust、Node.js、Python、WASM）。使用 CLI 工具“lit”基于 PDFium 构建。 [![CI](https://github.com/run-llama/liteparse/actions/workflows/ci.yml/badge.svg)](https://github.com/run-llama/liteparse/actions/workflows/ci.yml)
  * [rust-bakery/nom](https://github.com/rust-bakery/nom) - 解析器组合器库
  * [s-panferov/queryst](https://github.com/s-panferov/queryst) - 受 [gs] 启发的查询字符串解析库(https://github.com/ljharb/qs#readme)
* [slimreaper35/dockerfile-parser-rs](https://github.com/slimreaper35/dockerfile-parser-rs) [[dockerfile-parser-rs](https://crates.io/crates/dockerfile-parser-rs)] - Dockerfile 解析库和 CLI 工具
  * [softdevteam/grmtools](https://github.com/softdevteam/grmtools/) - 具有更好纠错能力的LR解析器
  * [tree-sitter/tree-sitter](https://github.com/tree-sitter/tree-sitter) - 解析器生成器工具和面向编程工具的增量解析库

### 周边设备

* [esp-rs/esp-hal](https://github.com/esp-rs/esp-hal) [[esp-hal](https://crates.io/crates/esp-hal)] - Espressif ESP32 设备的裸机 `no_std` 硬件抽象层（ESP32、ESP32-C2/C3/C5/C6/C61、ESP32-H2、 ESP32-P4、ESP32-S2/S3）。为 GPIO、I2C、SPI、UART、定时器、DMA 等提供安全的 Rust API。 [![GitHub Actions 工作流程状态](https://img.shields.io/github/actions/workflow/status/esp-rs/esp-hal/ci.yml?labelColor=1C2C2E&label=CI&logo=github&style=flat-square)](https://github.com/esp-rs/esp-hal/actions/workflows/ci.yml)
* 指纹识别器
* [alvaroparker/libfprint-rs](https://github.com/alvaroparker/libfprint-rs) [[libfprint-rs](https://crates.io/crates/libfprint-rs)] - Libfprint-rs 提供了 Linux libfprint 库的包装器。
* 串口
* [serialport/serialport-rs](https://github.com/serialport/serialport-rs) [[serialport](https://crates.io/crates/serialport)] - 提供对串行端口的访问的跨平台库

### 平台特定

* 跨平台
  * [iddm/thread-priority](https://github.com/iddm/thread-priority/) - 简单、跨平台的线程优先级管理。 [![CI](https://github.com/iddm/thread-priority/actions/workflows/ci.yml/badge.svg)](https://github.com/iddm/thread-priority/actions/workflows/ci.yml) [![箱子徽章](https://img.shields.io/crates/v/thread-priority.svg)](https://crates.io/crates/thread-priority)
  * [svartalf/rust-battery](https://crates.io/crates/battery) - 有关笔记本电池的跨平台信息
* 自由BSD
* [fubarnetes/libjail-rs](https://github.com/fubarnetes/libjail-rs/) [[jail](https://crates.io/crates/jail)] - FreeBSD 监狱库
* Linux
  * [hannobraun/inotify-rs](https://github.com/hannobraun/inotify-rs) - [inotify](https://en.wikipedia.org/wiki/Inotify) 绑定 [![Rust](https://github.com/hannobraun/inotify-rs/actions/workflows/rust.yml/badge.svg)](https://github.com/hannobraun/inotify-rs/actions/workflows/rust.yml)
  * [pop-os/distinst](https://github.com/pop-os/distinst/) - Linux 发行版安装程序
* [yaa110/rust-iptables](https://github.com/yaa110/rust-iptables) [[iptables](https://crates.io/crates/iptables)] - [iptables](https://www.netfilter.org/projects/iptables/index.html) 绑定
* 类Unix
  * [nix-rust/nix](https://github.com/nix-rust/nix) - 类 Unix API 绑定 [![CI](https://github.com/nix-rust/nix/actions/workflows/ci.yml/badge.svg)](https://github.com/nix-rust/nix/actions/workflows/ci.yml)
  * [rustix](https://github.com/bytecodealliance/rustix) - 安全绑定到 POSIX/Unix/Linux/Winsock2 系统调用 [![操作状态](https://github.com/bytecodealliance/rustix/workflows/CI/badge.svg)](https://github.com/bytecodealliance/rustix/actions?query=workflow%3ACI)
  * [zargony/fuse-rs](https://github.com/zargony/fuse-rs) - [FUSE](https://github.com/libfuse/libfuse) 绑定
* 窗户
  * [microsoft/windows-rs](https://github.com/microsoft/windows-rs) - Rust for Windows [![操作状态](https://github.com/microsoft/windows-rs/workflows/CI/badge.svg)](https://github.com/microsoft/windows-rs/actions)
  * [retep998/winapi-rs](https://github.com/retep998/winapi-rs) - Windows API 绑定 [![Rust](https://github.com/retep998/winapi-rs/actions/workflows/rust.yml/badge.svg?branch=dev)](https://github.com/retep998/winapi-rs/actions/workflows/rust.yml)

### 逆向工程

* [idalib](https://github.com/idalib-rs/idalib) [[idalib](https://crates.io/crates/idalib)] - IDA SDK 的 Rust 绑定，支持使用 IDA v9.0 的 idalib 开发独立分析工具
* [objdiff](https://github.com/encounter/objdiff) - 用于反编译项目的本地差异工具

### 脚本编写

[[脚本](https://crates.io/keywords/scripting)]

* [3body-lang](https://github.com/rustq/3body-lang) - 三种肢体语言
* [boa-dev/boa](https://github.com/boa-dev/boa) [[boa_engine](https://crates.io/crates/boa_engine)] - 用 Rust 编写的实验性 JavaScript 词法分析器、解析器和解释器。
* [cel-rust](https://github.com/cel-rust/cel-rust) [[cel-interpreter](https://crates.io/crates/cel-interpreter)] - 通用表达式语言解析器和解释器
* [duckscript](https://crates.io/crates/duckscript) - [简单、可扩展且可嵌入的脚本语言。](https://github.com/sagiegurari/duckscript) [![构建徽章](https://github.com/sagiegurari/duckscript/workflows/CI/badge.svg?branch=master)](https://github.com/sagiegurari/duckscript/actions)
* [facebook/starlark-rust](https://github.com/facebook/starlark-rust) - 一种小型、确定性、线程安全的语言，采用 Python 语法
* [fleabitdev/gamelisp](https://github.com/fleabitdev/glsp) - 用于游戏开发的类似 Lisp 的脚本语言
* [giraffekey/xylo](https://github.com/giraffekey/xylo) [[xylo-lang](https://crates.io/crates/xylo-lang)] - 一种用于程序艺术的函数式编程语言。 [![构建徽章](https://github.com/giraffekey/xylo/actions/workflows/rust.yml/badge.svg)](https://github.com/giraffekey/xylo/actions)
* [gluon-lang/gluon](https://github.com/gluon-lang/gluon) - 一种小型、静态类型、函数式编程语言
* [kcl](https://github.com/kcl-lang/kcl) - 一种基于约束的记录和功能语言，主要用于配置和策略场景。
* [kyren/piccolo](https://github.com/kyren/piccolo) [[piccolo](https://crates.io/crates/piccolo)] - 用纯 Rust 实现的实验性无堆栈 Lua 虚拟机，具有循环检测增量 GC、沙箱功能和安全的 Rust <-> Lua 绑定。 [![crates.io](https://img.shields.io/crates/v/piccolo)](https://crates.io/crates/piccolo)
* [metacall/core](https://github.com/metacall/core) [[metacall](https://crates.io/crates/metacall)] - 跨平台多语言运行时，支持 NodeJS、JavaScript、TypeScript、Python、Ruby、C#、Wasm、Java、Cobol 等。 [![构建徽章](https://gitlab.com/metacall/core/badges/master/pipeline.svg)](https://gitlab.com/metacall/core)
* [mun](https://github.com/mun-lang/mun) - 一种编译的静态类型脚本语言，具有一流的热重载支持
* [murarth/ketos](https://github.com/murarth/ketos) - 一种 Lisp 方言函数式编程语言，用作 Rust 的脚本和扩展语言
* [PistonDevelopers/dyon](https://github.com/PistonDevelopers/dyon) - 生锈的动态类型脚本语言
* [rhaiscript/rhai](https://github.com/rhaiscript/rhai) - 一种小型且快速的嵌入式脚本语言，类似于 JavaScript 和 Rust 的组合 [![构建徽章](https://github.com/rhaiscript/rhai/workflows/Build/badge.svg)](https://github.com/rhaiscript/rhai/actions)
* [rune-rs/rune](https://github.com/rune-rs/rune) - 一种嵌入式动态编程语言
* [trynova/nova](https://github.com/trynova/nova) - JavaScript 引擎完全用 Rust 编写

### 模拟

[[模拟](https://crates.io/keywords/simulation)]

* [nyx-space](https://crates.io/crates/nyx-space) - 高保真、快速、可靠且经过验证的天体动力学工具包库，用于航天器任务设计和轨道确定 [![构建状态](https://gitlab.com/nyx-space/nyx/badges/master/pipeline.svg)](https://gitlab.com/nyx-space/nyx/-/pipelines)

### 社交网络

* 电报
* [tdilb-rs](https://github.com/FedericoBruzzone/tdlib-rs) [[tdilb-rs](https://crates.io/crates/tdlib-rs)] - Telegram 数据库库 (TDLib) 的跨平台 Rust 包装器 [![CI Linux](https://github.com/FedericoBruzzone/tdlib-rs/actions/workflows/ci-linux.yml/badge.svg)](https://github.com/FedericoBruzzone/tdlib-rs/actions/workflows/ci-linux.yml) [![CI macOS](https://github.com/FedericoBruzzone/tdlib-rs/actions/workflows/ci-macos.yml/badge.svg)](https://github.com/FedericoBruzzone/tdlib-rs/actions/workflows/ci-macos.yml) [![CI Windows](https://github.com/FedericoBruzzone/tdlib-rs/actions/workflows/ci-windows.yml/badge.svg)](https://github.com/FedericoBruzzone/tdlib-rs/actions/workflows/ci-windows.yml)

### 系统

* [ardaku/whoami](https://github.com/ardaku/whoami) [[whoami](https://crates.io/crates/whoami)] - 获取当前用户和环境的箱子。 [![构建徽章](https://github.com/ardaku/whoami/actions/workflows/ci.yml/badge.svg?branch=stable)](https://github.com/ardaku/whoami/actions/workflows/ci.yml)
* [GuillaumeGomez/sysinfo](https://github.com/GuillaumeGomez/sysinfo) [[sysinfo](https://crates.io/crates/sysinfo)] - 用于获取系统信息的跨平台库 [![build徽章](https://github.com/GuillaumeGomez/sysinfo/actions/workflows/CI.yml/badge.svg?branch=master)](https://github.com/GuillaumeGomez/sysinfo/actions/workflows/CI.yml)
* [navidys/procsys](https://github.com/navidys/procsys) [[procsys](https://crates.io/crates/procsys)] - 用于从伪文件系统 /proc 和 /sys 检索系统、内核和进程指标的库。
* [Phate6660/nixinfo](https://github.com/Phate6660/nixinfo) [[nixinfo](https://crates.io/crates/nixinfo)] - 用于收集系统信息（如 cpu、发行版、环境、内核等）的 lib crate。
* [sorairolake/sysexits-rs](https://github.com/sorairolake/sysexits-rs) [[sysexits](https://crates.io/crates/sysexits)] - 由 [`<sysexits.h>`](https://man.openbsd.org/sysexits) 定义的系统退出代码。 [![CI](https://github.com/sorairolake/sysexits-rs/workflows/CI/badge.svg?branch=develop)](https://github.com/sorairolake/sysexits-rs/actions?query=workflow%3ACI)

### 任务调度

* [delay-timer](https://github.com/BinChengZhao/delay-timer) - 延迟任务的时间管理者。与 crontab 类似，但可以执行异步任务。 [![构建](https://github.com/BinChengZhao/delay-timer/actions/workflows/rust.yml/badge.svg)]( https://github.com/BinChengZhao/delay-timer/actions)
* [persistent-scheduler](https://github.com/rustmailer/persistent-scheduler) [[persistent-scheduler](https://crates.io/crates/persistent-scheduler)] - 使用 Tokio 构建的高性能任务调度系统，提供任务持久性、可重复任务和基于 Cron 的调度，以实现可靠的基于时间的操作。

### 模板引擎

* 车把
  * [sunng87/handlebars-rust](https://github.com/sunng87/handlebars-rust) - 具有继承、自定义帮助器支持的车把模板引擎。
  * [zzau13/yarte](https://github.com/zzau13/yarte) - Yarte 代表 **Y**et **A**nother **R**ust **T**emplate **E**ngine，是最快的模板引擎。
* HTML
  * [askama](https://github.com/askama-rs/askama) - 基于Jinja的模板渲染引擎
  * [kaj/ructe](https://github.com/kaj/ructe) - HTML模板系统
  * [Keats/tera](https://github.com/Keats/tera) - 基于 Jinja2 和 Django 模板语言的模板引擎。 [![操作状态](https://github.com/Keats/tera/workflows/ci/badge.svg?branch=master)](https://github.com/Keats/tera/actions)
  * [lambda-fairy/maud](https://github.com/lambda-fairy/maud) - 编译时 HTML 模板
  * [Stebalien/horrorshow-rs](https://github.com/Stebalien/horrorshow-rs) - 编译时 HTML 模板
* 小胡子
  * [rustache/rustache](https://github.com/rustache/rustache) - Mustache 规范的 Rust 实现

### 文本处理

* [becheran/wildmatch](https://github.com/becheran/wildmatch) [[wildmatch](https://crates.io/crates/wildmatch)] - 使用问号和星号通配符进行简单字符串匹配 [![操作状态](https://github.com/becheran/wildmatch/workflows/Build/badge.svg?branch=master)](https://github.com/becheran/wildmatch/actions)
* [BurntSushi/suffix](https://github.com/BurntSushi/suffix) - 线性时间后缀数组构造（支持Unicode）
* [BurntSushi/tabwriter](https://github.com/BurntSushi/tabwriter) - 弹性制表位（即文本列对齐）
* [cpc](https://github.com/probablykasper/cpc) - 解析和计算数学字符串，支持单位和单位转换，从“1+2”到“1% 的圆形（1 光年/14！s 到公里/小时）”。
* [Daniel-Liu-c0deb0t/triple_accel](https://github.com/Daniel-Liu-c0deb0t/triple_accel) [[triple_accel](https://crates.io/crates/triple_accel)] - 使用 SIMD 加速 Rust 编辑距离例程；支持快速 Hamming、Levenshtein、受限 Damerau-Levenshtein 等距离计算和字符串搜索 [![构建徽章](https://github.com/Daniel-Liu-c0deb0t/triple_accel/workflows/Test/badge.svg?branch=master)](https://github.com/Daniel-Liu-c0deb0t/triple_accel/actions)
* [fancy-regex/fancy-regex](https://github.com/fancy-regex/fancy-regex) [[fancy-regex](https://crates.io/crates/fancy-regex)] - 正则表达式实现，旨在支持相对丰富的功能集，例如环视和回溯。 [![板条箱](https://img.shields.io/crates/v/fancy-regex.svg)](https://crates.io/crates/fancy-regex) [![构建徽章](https://github.com/fancy-regex/fancy-regex/workflows/ci/badge.svg)](https://github.com/fancy-regex/fancy-regex/actions/workflows/ci.yml)
* [greyblake/whatlang-rs](https://github.com/greyblake/whatlang-rs) - 基于三元组的自然语言检测库
* [kreuzberg-dev/kreuzberg](https://github.com/kreuzberg-dev/kreuzberg) [[kreuzberg](https://crates.io/crates/kreuzberg)] - 文档智能库，可从 62 多种格式（PDF、Office、OCR 图像、HTML、电子邮件、档案）中提取文本、表格和元数据
* [Lucretiel/joinery](https://github.com/Lucretiel/joinery) [[joinery](https://crates.io/crates/joinery)] - 通用字符串+可迭代连接
* [mgeisler/textwrap](https://github.com/mgeisler/textwrap) [[textwrap](https://crates.io/crates/textwrap)] - 自动换行文本（支持连字符）
* [null8626/decancer](https://github.com/null8626/decancer) [[decancer](https://crates.io/crates/decancer)] - 一个小包，从字符串中删除常见的unicode易混淆/同形文字。 [![板条箱](https://img.shields.io/crates/v/decancer.svg)](https://crates.io/crates/decancer) [![构建徽章](https://github.com/null8626/decancer/workflows/CI/badge.svg)](https://github.com/null8626/decancer/actions/workflows/CI.yml)
* [ps1dr3x/easy_reader](https://github.com/ps1dr3x/easy_reader) - 允许在大文件行中向前、向后和随机导航而不消耗迭代器的阅读器
* [pwoolcoc/ngrams](https://github.com/pwoolcoc/ngrams) [[ngrams](https://crates.io/crates/ngrams)] - 从任意迭代器构造 [n-grams](https://en.wikipedia.org/wiki/N-gram)
* [rust-lang/regex](https://github.com/rust-lang/regex) - 正则表达式（RE2 风格）
* [strsim-rs](https://crates.io/crates/strsim) - 字符串相似度度量
* [yaa110/rake-rs](https://github.com/yaa110/rake-rs) [[rake](https://crates.io/crates/rake)] - Rust 的 RAKE 算法的多语言实现

### 文字搜索

* [andylokandy/simsearch](https://github.com/andylokandy/simsearch) [[simsearch](https://crates.io/crates/simsearch)] - 一个简单且轻量级的模糊搜索引擎，在内存中工作，搜索相似的字符串
* [BurntSushi/fst](https://github.com/BurntSushi/fst) [[fst](https://crates.io/crates/fst)] - 使用有限状态机快速实现有序集和映射
* [CurrySoftware/perlin](https://github.com/CurrySoftware/perlin) [[perlin](https://crates.io/crates/perlin)] - 一个惰性、零分配和数据不可知的信息检索库
* [meilisearch/MeiliSearch](https://github.com/meilisearch/MeiliSearch) - 超相关、即时且容错的全文搜索 API。 [![构建状态](https://github.com/meilisearch/MeiliSearch/workflows/Cargo%20test/badge.svg?branch=master)](https://github.com/meilisearch/MeiliSearch/actions)
* [pg_search](https://github.com/paradedb/paradedb/tree/dev/pg_search) - PostgreSQL 扩展，支持使用 BM25 算法对 SQL 表进行全文搜索，BM25 算法是最先进的全文搜索排名函数。
* [SeekStorm](https://github.com/SeekStorm/SeekStorm) [[SeekStorm](https://crates.io/crates/seekstorm)] - Rust 中的亚毫秒级全文搜索库和多租户服务器
* [tantivy](https://github.com/quickwit-oss/tantivy) [[tantivy](https://crates.io/crates/tantivy)] - 用 Rust 编写的高速全文搜索引擎库。 [![构建状态](https://github.com/quickwit-oss/tantivy/actions/workflows/test.yml/badge.svg)](https://github.com/quickwit-oss/tantivy/actions/workflows/test.yml)

### 不安全

* [zerocopy](https://crates.io/crates/zerocopy) - “零复制使零成本的内存操作变得毫不费力。我们编写‘不安全’，所以你不必这样做。”

### 视频

* [ffmpeg-sidecar](https://github.com/nathanbabcock/ffmpeg-sidecar) - 将独立的 FFmpeg 二进制文件包装在直观的迭代器界面中。 [![构建状态](https://github.com/nathanbabcock/ffmpeg-sidecar/actions/workflows/ci.yml/badge.svg)](https://github.com/nathanbabcock/ffmpeg-sidecar/actions)
* [screencapturekit-rs](https://github.com/doom-fish/screencapturekit-rs) [[screencapturekit](https://crates.io/crates/screencapturekit)] - 用于 macOS 屏幕/音频捕获的 Apple ScreenCaptureKit 框架的安全 Rust 绑定 [![Build状态](https://github.com/doom-fish/screencapturekit-rs/actions/workflows/ci.yml/badge.svg)](https://github.com/doom-fish/screencapturekit-rs/actions)

### 虚拟化

* [beneills/quantum](https://github.com/beneills/quantum) - 先进的量子计算机模拟器
* [bytecodealliance/wasmtime](https://github.com/bytecodealliance/wasmtime) - WebAssembly 的独立运行时 [![构建状态](https://github.com/bytecodealliance/wasmtime/workflows/CI/badge.svg)](https://github.com/bytecodealliance/wasmtime/actions?query=workflow%3ACI)
* [capsule](https://github.com/capsulerun/capsule) - 用于执行不受信任代码的 WebAssembly 沙箱运行时
* [chromium/chromiumos/platform/crosvm](https://chromium.googlesource.com/chromiumos/platform/crosvm/) - CrOSVM 使 Chrome 操作系统能够在快速、安全的虚拟化环境中运行 Linux 应用程序
* [oxidecomputer/propolis](https://github.com/oxidecomputer/propolis) - illumos bhyve 内核模块的用户空间程序
* [saurvs/hypervisor-rs](https://github.com/saurvs/hypervisor-rs) - OS X 上的硬件加速虚拟化
* [wasmi-labs/wasmi](https://github.com/wasmi-labs/wasmi) - WebAssembly 的轻量级运行时

### 网页编程

另请参阅 [我们已经联网了吗？](https://www.arewewebyet.org) 和 [Rust Web 框架比较](https://github.com/flosse/rust-web-framework-comparison)。
* 后端
  * [actix/actix-web](https://github.com/actix/actix-web) - 具有 websocket 支持的轻量级异步 Web 框架
  * [Anansi](https://github.com/saru-tora/anansi) - 一个简单的全栈Web框架
  * [Rocket](https://github.com/rwf2/Rocket) - Rocket 是一个注重易用性、可表达性和速度的 Web 框架
  * [summer-rs](https://github.com/summer-rs/summer-rs) - Summer-rs 是一个用 Rust 编写的应用程序框架，其灵感来自于 java 的 spring-boot。
  * [tako](https://github.com/rust-dd/tako) - Tako 是 Hyper 和 Tokio 上 Rust 的异步 Web 框架。 [GitHub 工作流程状态](https://github.com/rust-dd/tako/actions/workflows/ci.yml/badge.svg)
  * [tokio/axum](https://github.com/tokio-rs/axum) - 使用 Tokio、Tower 和 Hyper 构建的符合人体工程学的模块化 Web 框架 [![构建徽章](https://github.com/tokio-rs/axum/actions/workflows/CI.yml/badge.svg?branch=main)](https://github.com/tokio-rs/axum/actions/workflows/CI.yml)
* 客户端/WASM
  * [cargo-web](https://crates.io/crates/cargo-web) - 用于客户端 Web 的 Cargo 子命令
  * [leptos](https://github.com/leptos-rs/leptos) - Leptos 是一个全栈同构 Web 框架，利用细粒度反应性来构建声明式用户界面。[![crate](https://img.shields.io/crates/v/create-rust-app.svg)](https://crates.io/crates/leptos)
  * [sauron](https://github.com/ivanceras/sauron) - 客户端 Web 框架紧密遵循 Elm 架构。
  * [seed](https://github.com/seed-rs/seed) - 用于创建 Web 应用程序的框架
  * [stdweb](https://crates.io/crates/stdweb) - 客户端 Web 的标准库
* [synphonyte/leptos-use](https://github.com/synphonyte/leptos-use) [[leptos-use](https://crates.io/crates/leptos-use)] - 受 React-Use 和 VueUse 启发的基本乐浦实用程序集合，具有 SSR 支持 [![Build状态](https://github.com/synphonyte/leptos-use/actions/workflows/cd.yml/badge.svg)](https://github.com/synphonyte/leptos-use/actions/workflows/cd.yml)
* [thaw-ui/thaw](https://github.com/thaw-ui/thaw) [[thaw](https://crates.io/crates/thaw)] - 一个易于使用的基于 Fluent Design 的乐浦组件库
  * [tinyweb](https://github.com/LiveDuo/tinyweb) - 800 行代码的 wasm 最小 Rust Web 框架
  * [yew](https://crates.io/crates/yew) - 用于制作客户端 Web 应用程序的框架
* HTTP 客户端
  * [0x676e67/wreq](https://github.com/0x676e67/wreq) - 具有 TLS 指纹的符合人体工程学的 Rust HTTP 客户端。 [![CI](https://github.com/0x676e67/wreq/actions/workflows/ci.yml/badge.svg)](https://github.com/0x676e67/wreq/actions/workflows/ci.yml) [![crates.io](https://img.shields.io/crates/v/wreq.svg?logo=rust)](https://crates.io/crates/wreq)
  * [alexcrichton/curl-rust](https://github.com/alexcrichton/curl-rust) - [libcurl](https://curl.se/libcurl/) 绑定
  * [async-graphql](https://github.com/async-graphql/async-graphql) - GraphQL 服务器库 [![构建状态](https://dev.azure.com/graphql-rust/GraphQL%20Rust/_apis/build/status/graphql-rust.juniper)](https://dev.azure.com/graphql-rust/GraphQL%20Rust/_build/latest?definitionId=1)
  * [c410-f3r/wtx](https://github.com/c410-f3r/wtx) - HTTP/2 客户端框架
* [DoumanAsh/yukikaze](https://gitlab.com/Douman/yukikaze) [[yukikaze](https://crates.io/crates/yukikaze)] - 美丽而优雅的 Yukikaze 是基于 hyper 的小型 HTTP 客户端库。 [![构建徽章](https://gitlab.com/Douman/yukikaze/badges/master/pipeline.svg)](https://gitlab.com/Douman/yukikaze)
  * [ducaale/xh](https://github.com/ducaale/xh) - 用于发送 HTTP 请求的友好且快速的工具 [![crate](https://img.shields.io/crates/v/create-rust-app.svg)](https://crates.io/crates/xh) [![GitHub actions Status](https://github.com/ducaale/xh/workflows/CI/badge.svg?branch=master)](https://github.com/ducaale/xh/actions)
  * [graphql-client](https://github.com/graphql-rust/graphql-client) - 输入的、正确的 GraphQL 请求和响应。 [![GitHub 操作状态](https://github.com/graphql-rust/graphql-client/workflows/CI/badge.svg?branch=master)](https://github.com/graphql-rust/graphql-client/actions)
  * [hyperium/hyper](https://github.com/hyperium/hyper) - HTTP 实现 [![CI](https://github.com/hyperium/hyper/workflows/CI/badge.svg?branch=master)](https://github.com/hyperium/hyper/actions?query=workflow%3ACI)
  * [plabayo/rama](https://github.com/plabayo/rama) - 用于移动和转换网络数据包的模块化服务框架，可用于构建具有 TLS、JA3/JA4、H2 和 QUIC/H3 指纹模拟的客户端
  * [seanmonstar/reqwest](https://github.com/seanmonstar/reqwest) - 符合人体工程学的 HTTP 客户端。
* HTTP 服务器
  * [branca](https://crates.io/crates/branca) - 为经过身份验证和加密的 API 令牌实施 Branca。
  * [c410-f3r/wtx](https://github.com/c410-f3r/wtx) - 低级和高级 HTTP/2 服务器
* [carllerche/tower-web](https://github.com/carllerche/tower-web) [[tower-web](https://crates.io/crates/tower-web)] - 一个快速、无样板的 Web 框架
  * [Cot](https://github.com/cot-rs/cot) - 适合懒惰开发人员的 Rust Web 框架。
  * [GildedHonour/frank_jwt](https://github.com/GildedHonour/frank_jwt) - JSON Web 令牌实施。
  * [Gotham](https://github.com/gotham-rs/gotham) - 一个灵活的 Web 框架，不会牺牲安全性、保密性或速度。
  * [Graphul](https://github.com/graphul-rs/graphul) - 受 Express 启发的 Web 框架。 [![crate](https://img.shields.io/crates/v/create-rust-app.svg)](https://crates.io/crates/graphul)
  * [handlebars-rust](https://github.com/sunng87/handlebars-rust) - Iron Web 框架中间件。
  * [hyperium/hyper](https://github.com/hyperium/hyper) - HTTP 实现 [![CI](https://github.com/hyperium/hyper/workflows/CI/badge.svg?branch=master)](https://github.com/hyperium/hyper/actions?query=workflow%3ACI)
  * [Iron](https://github.com/iron/iron) - 基于中间件的服务器框架
  * [Juniper](https://github.com/graphql-rust/juniper) - GraphQL 服务器库
  * [miketang84/sapper](https://github.com/miketang84/sapper) - 一个基于 async hyper 构建的轻量级 Web 框架。
  * [Nickel](https://github.com/nickel-org/nickel.rs/) - 灵感来自 [Express](https://expressjs.com/)
  * [plabayo/rama](https://github.com/plabayo/rama) - 用于移动和转换网络数据包的模块化服务框架，还可用于对传入客户端进行指纹识别
  * [poem-web/poem](https://github.com/poem-web/poem) - 一个功能齐全且易于使用的 Web 框架。 [![CI](https://github.com/poem-web/poem/actions/workflows/ci.yml/badge.svg)](https://github.com/poem-web/poem/actions/workflows/ci.yml)
  * [Rustless](https://github.com/rustless/rustless) - 受 [Grape](https://github.com/ruby-grape/grape) 和 [Hyper](https://github.com/hyperium/hyper) 启发的类似 REST 的 API 微框架
  * [Salvo](https://github.com/salvo-rs/salvo) - 一个基于 hyper 和 tokio 的易于使用的网络框架。 [![构建构建](https://github.com/salvo-rs/salvo/actions/workflows/release.yml/badge.svg)](https://github.com/salvo-rs/salvo/actions)
  * [Saphir](https://github.com/richerarc/saphir) - 具有低级控制的渐进式 Web 框架，没有任何痛苦。
  * [seanmonstar/warp](https://github.com/seanmonstar/warp) - 一个超级简单、可组合的网络服务器框架，可提高速度。 [![crate](https://img.shields.io/crates/v/create-rust-app.svg)](https://crates.io/crates/warp)
  * [tiny-http](https://github.com/tiny-http/tiny-http) - 低级 HTTP 服务器库
  * [tomaka/rouille](https://github.com/tomaka/rouille) - 网页框架
  * [Zino](https://github.com/zino-rs/zino) - 可组合应用程序的下一代框架
* 杂项
  * [cargonauts](https://github.com/cargonauts-rs/cargonauts) - 一个旨在构建可维护、精心设计的 Web 应用程序的 Web 框架。
* [edezhic/prest](https://github.com/edezhic/prest) [[prest](https://crates.io/crates/prest)] - 旨在简化全栈开发的渐进式 RESTful 框架
* [hominee/dyer](https://github.com/hominee/dyer) [[dyer](https://crates.io/crates/dyer)] - Dyer 是为可靠、灵活、快速的基于请求响应的服务而设计的，包括数据处理、网络爬虫等，在不影响速度的情况下提供一些友好、灵活、全面的功能。
* [osohq/oso](https://github.com/osohq/oso) [[oso](https://crates.io/crates/oso)] - 嵌入在应用程序中的授权策略引擎。 [![构建状态](https://github.com/osohq/oso/workflows/Development/badge.svg?branch=main)](https://github.com/osohq/oso/actions?query=branch%3Amain+workflow%3ADevelopment)
* [pwoolcoc/soup](https://gitlab.com/pwoolcoc/soup) [[soup](https://crates.io/crates/soup)] - 类似于 Python 的 BeautifulSoup 的库，旨在实现快速轻松地操作和查询 HTML 文档。 [![构建状态](https://gitlab.com/pwoolcoc/soup/badges/master/pipeline.svg)](https://gitlab.com/pwoolcoc/soup/badges/master/pipeline.svg)
* [pyrossh/rust-embed](https://git.sr.ht/~pyrossh/rust-embed) [[rust-embed](https://crates.io/crates/rust-embed)] - 将静态资源嵌入到 rust 二进制文件中的宏
  * [rookie](https://github.com/thewh1teagle/rookie) - 从任何平台上的任何浏览器加载 cookie。 ![crates.io](https://img.shields.io/crates/v/rookie.svg)
* [rust-scraper/scraper](https://github.com/rust-scraper/scraper) [[scraper](https://crates.io/crates/scraper)] - 使用 CSS 选择器进行 HTML 解析和查询。 [![构建状态](https://github.com/rust-scraper/scraper/actions/workflows/test.yml/badge.svg?branch=master)](https://github.com/rust-scraper/scraper/actions)
* [serenity-rs/serenity](https://github.com/serenity-rs/serenity) [[serenity](https://crates.io/crates/serenity)] - Discord API 的库
  * [softprops/openapi](https://github.com/softprops/openapi) - 用于处理 openapi 规范文件的库
* [svix/svix-webhooks](https://github.com/svix/svix-webhooks) [[svix](https://crates.io/crates/svix)] - 用于发送 webhooks 和验证签名的库。
* [tbot](https://gitlab.com/SnejUgal/tbot) [[tbot](https://crates.io/crates/tbot)] - 轻松制作炫酷的 Telegram 机器人 [![管道状态](https://gitlab.com/SnejUgal/tbot/badges/master/pipeline.svg)](https://gitlab.com/SnejUgal/tbot/-/commits/master)
  * [teloxide/teloxide](https://github.com/teloxide/teloxide/) - 一个优雅的 Telegram 机器人框架 [![构建状态](https://github.com/telacet/teloxy/actions/workflows/ci.yml/badge.svg)](https://github.com/telacet/teloxy/actions)
* [tu6ge/valitron](https://github.com/tu6ge/valitron) [[valitron](https://crates.io/crates/valitron)] - 符合人体工程学、实用且可配置的验证器
* [utkarshkukreti/select.rs](https://github.com/utkarshkukreti/select.rs) [[select](https://crates.io/crates/select)] - 一个从 HTML 文档中提取有用数据的库，适合网络抓取。
  * [Utoipa](https://github.com/juhaku/utoipa) - 简单、快速、代码优先、编译时生成 OpenAPI 文档 [![crates.io](https://img.shields.io/crates/v/utoipa.svg?label=crates.io&color=orange&logo=rust)](https://crates.io/crates/utoipa) [![Utoipa构建](https://github.com/juhaku/utoipa/actions/workflows/build.yaml/badge.svg)](https://github.com/juhaku/utoipa/actions/workflows/build.yaml)
  * [Utoipauto](https://github.com/ProbablyClem/utoipauto) - Rust 宏自动将路径/模式添加到 Utoipa [![crates.io](https://img.shields.io/crates/v/utoipauto.svg?label=crates.io&color=orange&logo=rust)](https://crates.io/crates/utoipauto)
* 反向代理
* [sozu-proxy/sozu](https://github.com/sozu-proxy/sozu) [[sozu](https://crates.io/crates/sozu)] - HTTP 反向代理。 [![CI](https://github.com/sozu-proxy/sozu/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/sozu-proxy/sozu/actions/workflows/ci.yml)
* 静态站点生成器
  * [cobalt-org/cobalt.rs](https://github.com/cobalt-org/cobalt.rs) - 静态站点生成器 [![构建状态](https://dev.azure.com/cobalt-org/cobalt-org/_apis/build/status/cobalt.rs?branchName=master)](https://dev.azure.com/cobalt-org/cobalt-org/_build?definitionId=2)
* [FuGangqiang/mdblog.rs](https://github.com/FuGangqiang/mdblog.rs) [[mdblog](https://crates.io/crates/mdblog)] - 来自 Markdown 文件的静态站点生成器。
* [getzola/zola](https://github.com/getzola/zola) [[zola](https://www.getzola.org/)] - 一个内置所有内容的固执己见的静态站点生成器。 [![构建状态](https://dev.azure.com/getzola/zola/_apis/build/status/getzola.zola?branchName=master)](https://dev.azure.com/getzola/zola/_build)
* [grego/blades](https://github.com/grego/blades) [[blades](https://www.getblades.org/)] - 快速简单的静态站点生成器。
* [leven-the-blog/leven](https://github.com/leven-the-blog/leven) [[leven](https://crates.io/crates/leven)] - 一个简单的并行博客生成器。
* [rochacbruno/marmite](https://github.com/rochacbruno/marmite/) [[Marmite](https://marmite.blog/)] - 零配置博客生成器
* [WebSocket](https://datatracker.ietf.org/doc/rfc6455/)
  * [c410-f3r/wtx](https://github.com/c410-f3r/wtx) - 具有加密支持的客户端和服务器。
  * [housleyjk/ws-rs](https://github.com/housleyjk/ws-rs) - 轻量级、事件驱动的 WebSocket
  * [iddm/urlshortener-rs](https://github.com/iddm/urlshortener-rs) - 一个非常简单的 urlshortener 库。 [![CI](https://github.com/iddm/urlshortener-rs/actions/workflows/ci.yml/badge.svg)](https://github.com/iddm/urlshortener-rs/actions/workflows/ci.yml) [![箱子徽章](https://img.shields.io/crates/v/urlshortener.svg)](https://crates.io/crates/urlshortener)
* [ratchet](https://github.com/graphform/ratchet) [[ratchet_rs](https://crates.io/crates/ratchet_rs)] - Ratchet 是 WebSocket 协议的快速、轻量级且完全异步的实现，支持扩展和 Deflate。
* [rerun-io/ewebsock](https://github.com/rerun-io/ewebsock) [[ewebsock](https://crates.io/crates/ewebsock)] - 用于 Rust 的简单 WebSocket 库，可编译为本机和 Web (WASM)。支持使用异步友好的 API 发送和接收文本/二进制消息。 [![不安全禁止](https://img.shields.io/badge/unsafe-forbidden-success.svg)](https://github.com/rust-secure-code/safety-dance/)
  * [rust-websocket](https://github.com/websockets-rs/rust-websocket) - 处理 WebSocket 连接（客户端和服务器）的框架
  * [snapview/tungstenite-rs](https://github.com/snapview/tungstenite-rs) - 基于流的轻量级 WebSocket 实现。
  * [vi/websocat](https://github.com/vi/websocat) - 用于与 WebSocket 交互的 CLI，具有 Netcat、Curl 和 Socat 的功能。

## 登记处

注册表允许您将 Rust 库发布为 crate 包，以便公开和私下与其他人共享它们。

* [cenotelie/cratery](https://github.com/cenotelie/cratery) - 一个包含电池的轻量级私人货物登记处，专为组织构建，包括类似于 [docs.rs](https://docs.rs) 和 [deps.rs](https://deps.rs) 的功能。 [![CI](https://github.com/cenotelie/cratery/actions/workflows/ci.yml/badge.svg)](https://github.com/cenotelie/cratery/actions/workflows/ci.yml)
* [Cloudsmith :heavy_dollar_sign:](https://cloudsmith.com/product/formats/cargo-registry) - 完全托管的包管理 SaaS，为公共和私人 Cargo/Rust 注册中心（以及许多其他注册中心）提供一流的支持。对于开源项目免费。
* [Crates](https://crates.io) - Rust/Cargo 的官方公共注册表。
* [getnora-io/nora](https://github.com/getnora-io/nora) - 一个轻量级的单二进制工件注册表，支持 Docker、Maven、npm、PyPI、Cargo、Go 和原始格式。具有缓存和气隙模式的上游代理。
* [RepoFlow :heavy_dollar_sign:](https://www.repoflow.io) - 一个简单而现代的存储库平台，可以托管 Rust crate 存储库和代理 crates.io。还支持其他包类型，例如 Docker、PyPI、Maven、npm 和 RubyGems。可作为云服务或自托管。
* [w4/chartered](https://github.com/w4/chartered) - 私有的、经过身份验证的、经过许可的 Cargo 注册表 [![CI](https://github.com/w4/chartered/actions/workflows/ci.yml/badge.svg)](https://github.com/w4/chartered/actions/workflows/ci.yml)

## 资源

* [A Brief History of Rust. Part 1](https://medium.com/rustaceans/make-it-mandatory-a-brief-history-of-rust-part-1-805459c60c6b) - 从开发人员对软件稳定性的追求到几乎破坏其创建者稳定性的项目。 [第 2 部分](https://medium.com/rustaceans/make-it-mandatory-a-brief-history-of-rust-part-2-981d61451aa5)。 [第 3 部分](https://medium.com/rustaceans/make-it-mandatory-a-brief-history-of-rust-part-2-b8c0f7a7e781?sk=c0e7fe5fde11a62edc23f284f125aa18)。
* 艺术
  * [🦀 Free Ferris Pack 🦀](https://github.com/MariaLetta/free-ferris-pack) - 包含 50 多个免费 Ferris 插图，具有不同的情感、姿势和情况，采用 CC0 许可的 PNG 和 SVG 格式
* 基准
  * [c410-f3r/wtx-bench](https://github.com/c410-f3r/wtx-bench) - 网络基准测试
  * [TeXitoi/benchmarksgame-rs](https://github.com/TeXitoi/benchmarksgame-rs) - [计算机语言基准测试游戏](https://benchmarksgame-team.pages.debian.net/benchmarksgame/) 的实现
* 演讲稿和演示文稿
  * [Learning systems programming with Rust](https://speakerdeck.com/jvns/learning-systems-programming-with-rust) - 由 [Julia Evans](https://x.com/@b0rk) @ Rustconf 2016 提出。
  * [Rust: Hack Without Fear!](https://www.youtube.com/watch?v=lO1z-7cuRYI) - 由[Nicholas Matsakis](https://github.com/nikomatsakis)@C++Now 2018 提出
  * [Shipping a Solid Rust Crate](https://www.youtube.com/watch?v=t4CyEKb-ywA) - 由 [Michael Gattozzi](https://github.com/mgattozzi) @ RustConf 2017 提出
* 学习
  * [100 Exercises To Learn Rust](https://rust-exercises.com) - 通过 100 个实践练习学习 Rust，涵盖语法、类型等
  * [An Introduction to Programming using entity-component-systems and existence-based processing in Rust](https://root-11.github.io/intro-book/) - 比约恩·马德森所著的书
  * [Aquascope](https://github.com/cognitive-engineering-lab/aquascope) - Rust 在编译时和运行时的交互式可视化
  * [Awesome Rust Streaming](https://github.com/jamesmunns/awesome-rust-streaming) - 社区精选的直播列表。
  * [awesome-rust-mentors](https://rustbeginners.github.io/awesome-rust-mentors/) - 一份乐于助人的导师名单，他们愿意接受学员并教育他们有关 Rust 和编程的知识。
  * [CIS 198: Rust Programming](http://cis198-2016s.github.io/schedule/) - 宾夕法尼亚大学的 Comp Sci Rust 编程课程
  * [CodeCrafters.io](https://app.codecrafters.io/tracks/rust) - 构建您自己的 Redis、Git、Docker 或 SQLite
  * [Comprehensive Rust 🦀](https://google.github.io/comprehensive-rust/) - 为期 3 天的 Rust 基础知识课程以及为期 1 天的 Android、裸机 Rust 和并发课程。提供英语、[巴西葡萄牙语](https://google.github.io/compressive-rust/pt-BR/) 和[韩语](https://google.github.io/compressive-rust/ko/) 版本。
  * [Easy Rust](https://github.com/Dhghomon/easy_rust) - 用简单的英语学习 Rust。
  * [Embedded Software with Rust](https://www.manning.com/books/embedded-software-with-rust) - 实用介绍如何构建比用 C 或 C++ 编写的传统嵌入式软件快速、高效且安全得多的固件。
  * [exercism.org](https://exercism.org/tracks/rust) - 编程练习可帮助您学习 Rust 中的新概念。
  * [Hands-on Rust](https://pragprog.com/titles/hwrust/hands-on-rust/) - 通过制作游戏来学习 Rust 的实践指南 - 作者：[Herbert Wolverson](https://github.com/thebracket/)（付费）
  * [How to Avoid Fighting Rust Borrow Checker](https://qouteall.fun/qouteall-blog/2025/How%20to%20Avoid%20Fighting%20Rust%20Borrow%20Checker) - 关于 Rust 中的借用工作原理以及如何防止借用错误的指南，作者：[Qouteall](https://github.com/qouteall)
  * [Idiomatic Rust](https://github.com/mre/idiomatic-rust) - 经过同行评审的文章/演讲/存储库集合，教授惯用的 Rust。
  * [LabEx Rust Skill Tree](https://labex.io/skilltrees/rust) - 带有动手实验室的结构化 Rust 学习路径，专为初学者逐步掌握 Rust 而设计。
  * [Learn Rust 101](https://rust-lang.guide/) - 帮助您成为 Rustacean（Rust 开发人员）的指南
  * [Learn Rust by 500 lines code](https://github.com/cuppar/rtd) - 通过 500 行代码学习 Rust，从头开始构建一个 Todo Cli 应用程序。
  * [Learning Rust With Entirely Too Many Linked Lists](https://rust-unofficial.github.io/too-many-lists/) - 通过实现几种不同类型的列表结构，深入探索 Rust 的内存管理规则。
  * [Little Book of Rust Books](https://lborb.github.io/book/) - Rust 书籍和操作方法的精选列表。
  * [Programming Community Curated Resources for Learning Rust](https://hackr.io/tutorials/learn-rust) - 由编程社区投票选出的推荐资源列表。
  * [Refactoring to Rust](https://www.manning.com/books/refactoring-to-rust) - 一本介绍 Rust 语言的书。
  * [Rust by Example](https://doc.rust-lang.org/rust-by-example/) - 一组可运行的示例，说明了各种 Rust 概念和标准库。
  * [Rust Cookbook](https://rust-lang-nursery.github.io/rust-cookbook/) - 一组简单的示例，展示了使用 Rust 生态系统的板条箱完成常见编程任务的良好实践。
  * [Rust Flashcards](https://github.com/ad-si/Rust-Flashcards) - 超过 550 张抽认卡，帮助您从基本原理开始学习 Rust。
  * [Rust for professionals](https://overexact.com/rust-for-professionals/) - 为经验丰富的软件开发人员快速介绍 Rust。
  * [Rust Gym](https://github.com/warycat/rustgym) - 用 Rust 解决的编码面试问题的大集合。
  * [Rust in Action](https://www.manning.com/books/rust-in-action) - Rust 系统编程实践指南，作者：[Tim McNamara](https://github.com/timClicks)（付费）
  * [Rust in Motion](https://www.manning.com/livevideo/rust-in-motion?a_aid=cnichols&a_bid=6a993c2e) - [Carol Nichols](https://github.com/carols10cents) 和 [Jake Goulding](https://github.com/shepmaster) 的视频系列（付费）
  * [Rust Language Cheat Sheet](https://cheats.rs/) - Rust 语言备忘单
  * [Rust Tiếng Việt](https://rust-tieng-viet.github.io/) - 用越南语学习 Rust。
  * [rust-how-do-i-start](https://github.com/jondot/rust-how-do-i-start) - 一个致力于回答以下问题的存储库：“那么，Rust。我如何*开始*？”。初学者只能手工挑选资源和学习轨迹。
  * [rust-learning](https://github.com/ctjhoa/rust-learning) - 学习 Rust 的有用资源集合
  * [Rustfinity](https://www.rustfinity.com) - 通过实践练习和挑战练习 Rust 的互动平台
  * [Rustlings](https://github.com/rust-lang/rustlings) - 让您习惯阅读和编写 Rust 代码的小练习
  * [Rusty CS](https://github.com/AbdesamedBendjeddou/Rusty-CS) - 计算机科学课程，有助于实践 Rust 中获得的学术知识
  * [stdx](https://github.com/brson/stdx) - 首先学习这些板条箱作为 std 的扩展
  * [Tour of Rust](https://tourofrust.com) - 这是一个交互式逐步指南，介绍 Rust 编程语言的功能。
* 性能
  * [How to avoid bounds checks in Rust (without unsafe!)](https://shnatsel.medium.com/how-to-avoid-bounds-checks-in-rust-without-unsafe-f65e618b4c1e) - 关于优化边界检查您需要了解的所有信息
  * [Performance of Rust language](https://raw.githubusercontent.com/yugr/rust-slides/main/EN.pdf) - Rust 面向性能的语言特性概述
  * [The Rust Performance Book](https://nnethercote.github.io/perf-book/) - 优化 Rust 程序的技巧
* 播客
  * [New Rustacean](https://newrustacean.com) - 关于学习 Rust 的播客
  * [Rustacean Station](https://rustacean-station.org/) - 用于为 Rust 创建播客内容的社区项目
* [Rust Design Patterns](https://github.com/rust-unofficial/patterns) - Rust 设计模式、反模式和习语的目录
* [Rust Guidelines](http://aturon.github.io/) - Aaron Turon 关于 Rust 的博客文章
* [Rust Security Handbook](https://github.com/yevh/rust-security-handbook) - 一本 10 章的手册，用于编写真正安全的 Rust：类型安全、防恐慌等等。
* [Rust Servers, Services and Apps - MEAP](https://www.manning.com/books/rust-servers-services-and-apps) - 使用 Rust 构建后端服务器、服务和前端，以获得快速、可靠且可维护的应用程序。
* [Rust Subreddit](https://www.reddit.com/r/rust/) - 一个 Reddit 子版块（论坛），其中发布和讨论与 Rust 相关的问题、文章和资源
* [RustBooks](https://github.com/sger/RustBooks) - RustBooks 列表
* [RustCamp 2015 Talks](https://www.youtube.com/playlist?list=PLE7tQUdRKcybdIw61JpCoo89i4pWU5f_t) - RustCamp 2015 的演讲录音
* [RustViz](https://github.com/rustviz/rustviz) - 从简单的 Rust 程序生成可视化，以帮助用户更好地理解 Rust 生命周期和借用机制。
* [Watch Jon Gjengset Implement BitTorrent in Rust](https://www.youtube.com/watch?v=jf_ddGnum_4) - 用 Rust 实现（部分）BitTorrent 客户端

## 许可证

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)
