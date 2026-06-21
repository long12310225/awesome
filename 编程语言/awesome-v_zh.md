<!--lint disable no-dead-urls-->

<palign="center"><img src="media/awesome-v-logo.svg"width="400"/></p>

# 太棒了V [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> 精选的精彩 V 框架、库、软件和资源列表。

[V](https://vlang.io/) 是一种简单、快速、安全的编译语言，用于开发可维护的软件。

## 内容

- [Applications](#applications)
	- [构建系统](#build-systems)
	- [Command-line](#command-line)
	- [Editors](#editors)
	- [Games](#games)
	- [Graphics](#graphics)
	- [Interpreters/Compilers](#interpreterscompilers)
	- [操作系统/内核](#operating-systemskernels)
	- [包管理器](#package-managers)
	- [项目管理](#project-management)
	- [Serialization](#serialization)
	- [Utilities](#utilities)
	- [Web](#web)
- [Libraries](#libraries)
	- [Audio](#audio)
	- [Automation](#automation)
	- [命令行界面 (CLI) / 终端 / Shell](#command-line-interface-cli--terminal--shell)
	- [数据库客户端](#database-clients)
	- [Discord](#discord)
	- [Eventing](#eventing)
	- [文件处理](#file-handling)
	- [游戏开发](#game-development)
	- [Graphics](#graphics-1)
	- [Interoperability](#interoperability)
	- [IRC](#irc)
	- [Networking](#networking)
	- [操作系统](#operating-system)
	- [科学计算](#scientific-computing)
	- [串行通讯](#serial-communications)
	- [Telecommunications](#telecommunications)
	- [Telegram](#telegram)
	- [文本处理](#text-processing)
	- [用户界面工具包](#user-interface-toolkits)
	- [Utility](#utility)
	- [Web](#web-1)
- [Other](#other)
	- [Articles](#articles)
	- [Books](#books)
	- [Communities](#communities)
	- [编辑器插件](#editor-plugins)
	- [Forums](#forums)
	- [GitHub 操作](#github-actions)
	- [GitHub 模板](#github-templates)
	- [带 V 的 IDE](#ides-with-v)
	- [带 V 的在线 IDE](#online-ides-with-v)
	- [操作系统和操作系统开发示例](#operating-systems--os-development-examples)
	- [Patterns](#patterns)
	- [编程竞赛](#programming-contests)
	- [语法高亮](#syntax-highlighting)
	- [Tutorials](#tutorials)
	- [Videos](#videos)

## 应用领域

### 构建系统

- [clockwork](https://github.com/emmathemartian/clockwork) - 用 V 编写的与语言无关的构建工具。
- [vab](https://github.com/vlang/vab) - 用于构建和打包 Android 应用程序的官方 V 工具。
- [vab-sdl](https://github.com/larpon/vab-sdl) - 用于构建和打包“vab”的独立命令和额外命令
基于 SDL2 和 SDL3 的应用程序导入“vlang/sdl”。

### 命令行

- [amdim](https://github.com/tailsmails/amdim) - 让你的屏幕亮度低于 0%。
- [crepl](https://github.com/l1mey112/crepl) - 在您键入 C 代码时即时编译并执行它。
- [dnshammer](https://github.com/tailsmails/dnshammer) - 将数据编码到 DNS 缓存定时差异中的隐蔽通信通道。
- [envelop](https://github.com/tailsmails/envelop) - 生成后台 HTTP HEAD 请求以混淆真实的 Web 流量。
- [fastgit](https://github.com/tailsmails/fastgit) - 用 V 编写的命令行工具，旨在自动化和简化上传、同步和修改 GitHub 存储库。
- [fdup](https://github.com/gechandesu/fdup) - 查找并删除重复的文件。
- [github-releases](https://github.com/Dracks/repo-download-asset) - Cli 工具用于跟踪作为 GitHub 版本发布的应用程序（或工作流程中的资产）并下载它们。
- [HN-top](https://github.com/BafS/hn-top) - 一个简单的命令，用于列出来自 hacker-news 的最新新闻。
- [httest](https://github.com/gechandesu/httest) - 支持 CGI 的 HTTP 测试服务器，用于模拟后端、检查请求以及模拟延迟和故障。
- [klonol](https://github.com/hungrybluedev/klonol) - CLI 工具可帮助您“克隆所有”属于您的 Git 存储库。可与 GitHub 和 Gitea 配合使用。
- [lagger](https://github.com/tailsmails/lagger) - 动态网络延迟和数据包丢失模拟代理，旨在模拟应用层的真实网络退化。
- [lsv](https://github.com/mike-ward/lsv) - `ls` 文件列表器本着 exa、eza、lsd、pls、natls、ls-go 等的精神。
- [minimax-v](https://github.com/whiter001/minimax-v) - 以V语言实现的本地AI Agent运行时。
- [mushroomtek](https://github.com/tailsmails/mushroomtek) - 不用担心网格，你只是一个半径（反IMSI捕手/反三角测量...）。
- [musicc](https://github.com/tailsmails/musicc) - 一个轻量级、高性能的命令行音乐编译器。
- [netprint](https://github.com/tailsmails/netprint) - 一种低级网络遥测和异常检测工具，旨在识别环境变化和流量拦截。
- [pfjson](https://github.com/fleximus/pfjson) - 一个 CLI 工具，用于将 OpenBSD 数据包过滤器配置文件 (`pf.conf`) 转换为 JSON，反之亦然。
- [PhoneSnatchProof](https://github.com/tailsmails/PhoneSnatchProof) - 一个 FS，用于加密您的应用程序数据并将其保存在 RAM 上（带有备份）。
- [portctl](https://github.com/apoprotsky/portctl) - 使用 Portainer API 管理 Docker Swarm 资源的 CLI 工具。
- [runner](https://github.com/Naheel-Azawy/runner) - 一种自动运行/编译用各种编程语言编写的代码的工具。
- [salty](https://github.com/tailsmails/salty) - 用 V 编写的轻量级命令行实用程序，用于安全数据加密、深度压缩和类似隐写的格式混淆。
- [sockslender](https://github.com/tailsmails/sockslender) - 一个用 V 编写的轻量级、速度极快的 SOCKS5 代理故障转移工具。
- [stripshot](https://github.com/tailsmails/stripshot) - 从屏幕截图中去除设备/操作系统指纹。
- [symlinker](https://github.com/serkonda7/symlinker) - 一个用于管理符号链接的小型 Linux 工具。
- [timingless](https://github.com/tailsmails/timingless) - 位于您的应用程序和 Tor 之间的 SOCKS5 代理，强制执行恒定带宽以击败流量计时分析。
- [v-terminal-apps](https://github.com/cogrow4/V-Terminal-Apps) - 用 V 编写的高质量终端应用程序的集合，包括工作计划器、计算器、笔记、文件浏览器、问答游戏、预算跟踪器、P2P 聊天 (WIP) 和番茄计时器。
- [v_llama_cpp](https://github.com/sakana-ctf/v_llama_cpp) - Llama.cpp 的轻量级 V 包装器，可实现高效的 LLM 执行。
- [vast](https://github.com/lydiandy/vast) - 一个简单的vlang工具，生成v源文件到AST json文件。
- [vcli](https://github.com/changhz/vcli) - 一个根据[指南](https://blog.vlang.io/the-complete-beginners-guide-to-cli-apps-in-v/)生成文件夹结构的CLI工具
- [verve](https://github.com/MohammadMD1383/verve) - 简单快速的静态文件服务器。
- [vfc](https://github.com/Ict00/vfc) - 一个简单的 TUI 文件管理器，用 V 制作。
- [vfetch](https://github.com/carlosqsilva/vfetch) - 用 V 编写的 macOS 系统信息获取。
- [vgoogle](https://github.com/changhz/vgoogle) - 在终端上进行谷歌搜索。
- [vin](https://github.com/DeoDorqnt387/vin) - V 的基本命令行界面。
- [vindex](https://github.com/wenxuanjun/vindex) - 一个简单的文件列表服务器生成json字符串，兼容nginx的autoindex模块。
- [vinit](https://github.com/pranavbaburaj/vinit) - 生成v项目的工具。
- [vLogQL](https://github.com/lmangani/vLogQL) - 一个用于查询 LogQL API 的小型命令行实用程序。
- [vlsh](https://github.com/vlshcc/vlsh) - *nix 用 V 编写的 Shell（管道、插件、多路复用模式等）。
- [vqrcode](https://github.com/carlosqsilva/vqrcode) - 用于创建 QR 码的 CLI。
- [vspect](https://github.com/zakuro9715/vspect) - 一个检查vlang源文件的工具。 （已存档）
- [vsqlite](https://github.com/quaesitor-scientiam/vsqlite) - SQLite CLI 和用纯 V 编写的模块替换。
- [vzcc](https://github.com/malisipi/vzcc) - 一个基于 Zig CC for V 的 CLI 交叉编译工具。
- [zilch](https://github.com/mike-ward/zilch) - 一个有趣的安装程序模拟。

### 编辑

- [lilly](https://github.com/tauraamui/lilly) - TUI 编辑器和 VIM/Neovim 替代品。
- [polygon-editor](https://github.com/ArtemkaKun/polygon-editor) - 一个使用 sprite 查找创建和编辑 2D 多边形的工具，在 V 中创建。
- [text_editor](https://github.com/vlang/v/blob/master/examples/term.ui/text_editor.v) - 来自官方 V 示例的小型文本编辑器。
- [ved](https://github.com/vlang/ved) - 用 V 编写的 1 MB 文本编辑器，具有硬件加速文本渲染功能。编译时间 <1 秒。
- [vee](https://github.com/Larpon/vee) - V 编辑器引擎。提供文本编辑器功能的 V 模块。附带一个 [TUI 编辑器示例](https://github.com/Larpon/vee/blob/master/examples/tuieditor/)。
- [volt](https://github.com/Volt-Editor-Team/volt) - 旨在成为一个完全用 Vlang 编写的功能齐全的文本编辑器。
- [vPDF](https://github.com/vlang/pdf) - 使用 V 编程语言简化 PDF 文件创建的模块。
- [vro](https://github.com/undivisible/vro) - <0.5MB 受微型启发的基本文本编辑器。与 Micro 的 YAML 语法高亮兼容。

### 游戏

- [2048](https://github.com/wenxuanjun/2048) - 一款融合了多种传统AI的2048游戏。
- [Boundstone](https://github.com/organization/boundstone) - 高性能/快速编译/轻量级 Minecraft：基岩版服务器。
- [flappylearning-v](https://github.com/vlang/v/tree/master/examples/flappylearning) - v 中的一个简单的 flappy 学习演示。
- [Kurarin](https://github.com/FireRedz/kurarin) - 奥苏！用 V 制作的beatmap可视化工具。[示例视频](https://p153.p0.n0.cdn.getcloudapp.com/items/6quvQjb5/ce3ea737-eb29-4b8c-a5f3-65a804a2f56f.mp4)。
- [minesweeper](https://github.com/ali-furkan/minesweeper-v) - 一个用 vlang 编写的简单扫雷游戏。
- [Puzzle Vibes](https://github.com/Larpon/puzzle_vibes) - 使用“shy”用 V 编写的类似拼图的益智游戏。
- [vchess](https://github.com/hedgeg0d/vchess) - 用V编程语言编写的国际象棋游戏。
- [v-pong](https://github.com/thebigsmileXD/v-pong) - 经典的桨游戏通过 V 的力量复活。

### 图形

- [mpv-v](https://github.com/xjunko/mpv-v) - 世界上最简单的视频播放器。
- [vpaint](https://github.com/pisaiah/vpaint) - 用 V 编写的 MS-Paint 替代方案。
- [vRayTracer](https://github.com/ali-raheem/vraytracer) - 用 V 编写的简单光线追踪器。

### 解释器/编译器

- [Aixt](https://github.com/fermarsan/aixt) - 基于 V 语言并用 V 编写的微控制器编程框架。
- [cotowali](https://github.com/cotowali/cotowali) - 一种静态类型脚本语言，可转换为 POSIX sh。
- [monkey_v](https://github.com/Delta456/monkey_v) - [Thorsten Ball 的 Monkey Language](https://interpreterbook.com/) 在 V 中的实现。
- [papyrus-compiler](https://github.com/russo-2025/papyrus-compiler) - Bethesda 的 Papyrus 脚本语言 (Skyrim SE/AE) 的开源编译器。
- [stas](https://github.com/l1mey112/stas/tree/0.1.0-v-compiler) - 基于堆栈的编译编程语言。引导编译器是用 V 编写的。
- [v](https://github.com/vlang/v) - 语言V本身。用于开发可维护软件的简单、快速、安全的编译语言。
- [vas](https://github.com/v420v/vas) - 用 V 编写的简单 x86-64 汇编器。
- [vbf](https://github.com/vpervenditti/vbf) - 一个脑残的解释器/编译器。
- [vfuck](https://github.com/ShayokhShorfuddin/VFuck) - 一个用 V 编写的脑残解释器。
- [vcc](https://github.com/lemoncmd/vcc) - 用 V 编写的 C 编译器。
- [Vork](https://github.com/Itay2805/Vork) - 用 Python 编写的替代 V 编译器/解释器。

### 操作系统/内核

- [Vinix](https://github.com/vlang/vinix) - V 中的小而简单的操作系统。运行 bash。
- [V-Unikernel](https://github.com/vlang/unikernel) - Unikernel 是与其所依赖的操作系统代码静态链接的计算机程序。

### 包管理器

- [vpm](https://github.com/vlang/vpm) - 用V编写的V语言包管理工具。

### 项目管理

- [Lenra template](https://github.com/lenra-io/template-v) - 用于为 Lenra 平台编写 V 应用程序的 Lenra 模板。
- [vset](https://github.com/mulh8377/vset) - V 项目的项目设置和配置工具。

### 序列化

- [ini-v](https://github.com/ldedev/ini-v) - 简单实用的ini/cfg文件操作模块。
- [maple](https://github.com/emmathemartian/maple) - 用 V 编写的一个非常简单的键值配置格式。
- [v-toxml](https://github.com/radare/v-toxml) - V 的 XML 序列化库
- [vgura](https://github.com/gura-conf/vgura) - V 的官方 Gura 解析器。
- [vlang-yaml](https://github.com/jdonnerstag/vlang-yaml) - V 原生 YAML 阅读器，包括。 YAML 到 JSON 转换器。
- [vproto](https://github.com/emily33901/vproto) - V 中的 Protobuf 编译器和运行时。

### 公用事业

- [boj-server](https://github.com/hyperpolymath/boj-server) - 使用V作为网络适配器层的统一开发者工具服务器。从单个 V 代码库公开 REST（端口 7700）、gRPC (7701) 和 GraphQL (7702)。通过具有 Idris2 验证接口的 Zig FFI 加载 18 个功能盒。
- [emoji-mart-desktop](https://github.com/ttytm/emoji-mart-desktop) - 使用 V、webview 和 SvelteKit 创建的表情符号选择器。
- [qptorrent](https://github.com/qptorrent/qptorrent) - 用 V + vlang/gui 编写的最小 GUI/CLI BitTorrent 客户端。
- [raur](https://github.com/Matejsdevelopment/raur) - 使用 Vlang 编码的简单 Arch 用户存储库 (AUR) 帮助程序。
- [unix-emulators-win](https://github.com/Ddiidev/unix-emulators-win) - 用 V for Windows 重写的 16 个 UNIX 实用程序的集合。
- [v-nodejs-addon](https://github.com/fanlia/v-nodejs-addon) - 演示如何使用 V 创建 Node.js 插件。

### 网络

- [Gitly](https://github.com/vlang/gitly) - 用 V 编写的 GitHub/GitLab 的轻量且快速的 SCM 替代品。
- [gitval](https://github.com/davlgd/gitval) - Git 存储库的静态站点生成器，用 V 编写。
- [Heroku Buildpack for V](https://github.com/zztkm/heroku-buildpack-v) - 在 Heroku 上部署 V 应用程序。
- [highlighter](https://codeberg.org/tamer/highlighter) - 在构建时或通过 CLI 工具将语法突出显示注入 HTML 文件。
- [Mantis](https://github.com/khalyomede/mantis) - 用 V 编写的 Web 框架。
- [Mustela](https://github.com/filipos800/mustela) - 超高性能静态站点生成器 (SSG) 专为速度（>9,000 页/秒）和总体数据主权而设计。
- [rr-dl](https://github.com/dy-tea/rr-dl) - 御道小说下载器。
- [Tiniest Veb Server](https://github.com/davlgd/tVeb) - 使用 V 编写的 < 1MB 静态托管 Web 服务器，基于“veb”。 🍃
- [v-admin-skeleton](https://github.com/xiusin/v-system-skeleton) - 用V编写的后端骨架。
- [v-vite starter](https://github.com/v-vite/starter) - Veb 应用程序的入门套件，使用 Vite.js 进行预配置。
- [vblog](https://github.com/scurty-labs/vblog) - 一个简单、快速且响应迅速的博客系统。
- [Vebview.JS](https://github.com/malisipi/Vebview.JS) - 用 V 编写的 Electron/Neutralino.JS 替代方案。
- [Verne](https://github.com/davlgd/Verne) - 另一个以法国著名作家命名的静态站点生成器。
- [vico_bot](https://github.com/KArjmand/vico_bot) - 具有持久内存和工具调用的轻量级自托管人工智能聊天机器人。
- [Vieter](https://github.com/ChewingBever/vieter) - Arch Linux 存储库服务器和包构建系统，用 V 编写。
- [Vlang Benchmarks Visualization](https://github.com/ArtemkaKun/VlangBenchmarksVisualization) - *[V 仍然很快吗？](https://fast.vlang.io/)* 的精美统计数据和图表。
- [vorum](https://github.com/vlang/vorum) - 用 V 编写的开源博客/论坛软件。
- [vss](https://github.com/vssio/vss) - 易于使用的静态站点生成器。
- [VTik](https://github.com/Sharqo78/VTik) - TikTok 和 Twitter 视频下载应用程序（CLI / Telegram Bot）。

## 图书馆

### 音频

- [miniaudio](https://github.com/larpon/miniaudio) - 优秀的 miniaudio C 音频库的绑定。
- [vave](https://github.com/thecodrr/vave) - 一个疯狂简单的库，用于在 V 中读取/写入 WAV 文件。🌊
- [vspeech](https://github.com/thecodrr/vspeech) - Mozilla 基于 DeepSpeech TensorFlow 的语音转文本库的完整 V 绑定。 📢📜

### 自动化

- [v-webdriver](https://github.com/quaesitor-scientiam/v-webdriver) - 用于浏览器自动化的 W3C WebDriver 协议的 V 语言实现。
- [vrobot](https://github.com/eioo/vrobot) - V 的桌面自动化。仅支持 Windows。

### 命令行界面 (CLI) / 终端 / Shell

- [bartender](https://github.com/tobealive/bartender) - V 终端应用程序的可定制进度指示器。
- [boxx](https://github.com/thecodrr/boxx) - 创建高度可定制的接线盒，而且看起来也很棒！ 📦
- [lol](https://github.com/0xLeif/lol) - lolcat（文本/角色彩虹化器）的 V 版本。
- [progressbar](https://github.com/Waqar144/progressbar) - 一个易于使用的 V 库，用于在 cli 中创建进度条。
- [spinners](https://github.com/rhygg/spinners) - 在您的终端中创建微调器！
- [termtable](https://github.com/serkonda7/termtable) - V 终端表：简单且高度可定制的库，用于在终端中显示表格。
- [vargs](https://github.com/nedpals/vargs) - 用于解析类似 argv 数组的参数的 V 库。 （已存档）
- [vesseract](https://github.com/barrack-obama/vesseract) - Tesseract-OCR（光学字符识别）的 V 包装器。

### 数据库客户端
<!-- lint disable awesome-spell-check -->
- [firebird](https://github.com/einar-hjortdal/firebird) - Firebird SQL 客户端。
- [mongodb](https://github.com/vlang/mongo) - V 的 MongoDB 驱动程序。
- [redict](https://github.com/einar-hjortdal/redict) - Redict 客户端，仅 LGPL-3.0 的 Redis 分支（与 Redis <=7.2.4 兼容）。
- [redis](https://github.com/patrickpissurno/vredis) - V 的 Redis 客户端，用 V 编写。
- [vduckdb](https://github.com/rodabt/vduckdb) - V 的 DuckDB 客户端包装器。
- [vmemcached](https://github.com/blacktrub/vmemcached) - V 的 Memcached 客户端，用 V 编写。
- [vredis](https://github.com/xiusin/vredis) - 一个简单、用户友好且全面的 Redis 客户端。
- [vsql](https://github.com/lydiandy/vsql) - V 的 sql 查询生成器。

### 不和谐

- [discord.v](https://github.com/Terisback/discord.v) - 用户友好的 Discord 机器人库。
- [discordwebhook](https://github.com/ysdragon/discordwebhook) - 通过 webhooks 发送不一致消息的超级简单界面。
- [kitten](https://github.com/geniushq/kitten) - 用于编写机器人的简单 Discord API 库。
- [viscord](https://github.com/vlang/viscord) - 用于连接到 Discord 网关的非常基本的库。
- [vord](https://github.com/9xN/vord) - 用于与用户帐户端点和网关（自助机器人、自定义客户端等）交互的库。

### 三项赛

- [eventbus](https://github.com/vlang/v/tree/master/vlib/eventbus) - V 的简单事件总线系统。

### 文件处理

- [v-mime](https://github.com/nedpals/v-mime) - V 的 MIME 检测库。
- [vmon](https://github.com/Larpon/vmon) - 异步监视目录中的文件更改。该模块本质上是“septag/dmon”的 V 包装器。它适用于 Windows、macOS 和 Linux。

### 游戏开发

- [chipmunk2d](https://github.com/larpon/chipmunk2d) - Chipmunk2D 物理库的 V 包装器。
- [engine](https://github.com/LouisSchmieder/engine) - V 中的 WIP Vulkan。
- [raylib.v](https://github.com/irishgreencitrus/raylib.v) - 更新了 [raylib](https://www.raylib.com) 的 V 绑定，并计划提供完整的跨平台支持。
- [sdl2test](https://github.com/nsauzede/sdl2test) - 针对带有 V 的 SDL2 的详尽测试和示例套件。
- [shy](https://github.com/Larpon/shy) - 帮助您在 V 中发挥创造力的基础。
- [V_ecs](https://github.com/mohamedLT/V_ecs) - ECS 库是在 V 中制作的，灵感来自 Bevy ECS。
- [vraylib](https://github.com/mohamedLT/vraylib) - 很棒的 raylib 库的 V 包装器。
- [vraylib](https://github.com/MajorHard/vraylib) - raylib 的 V 包装器（绑定），C 游戏开发框架。
- [wren](https://github.com/larpon/wren) - V 封装了优秀的 Wren 脚本语言。

### 图形

- [sdl](https://github.com/vlang/sdl) - V 的官方 SDL2 和 SDL3 绑定。
- [sgldraw](https://github.com/larpon/sgldraw) - 基于“sokol.sgl”的实验性实时矢量渲染 V 模块。
- [svgg](https://github.com/Avocadocs/svgg) - V 模块将 svg 文件加载并重新转换为 `gg.Image` 对象。
- [V Earcut](https://github.com/Larpon/earcut) - 基于 [mapbox/Earcut](https://github.com/mapbox/earcut) 的快速（实时）多边形三角剖分库，用于处理孔、扭曲多边形、简并和自相交。
- [V_sokol_gp](https://github.com/mohamedLT/V_sokol_gp) - sokol_gp 库的 V 包装器，可轻松快速地绘制 2d 图形。
- [vglyph](https://github.com/vlang/vglyph) - 适用于 V 编程语言的高性能文本渲染引擎，基于 Pango、FreeType 和 Sokol 构建。
- [viup](https://github.com/kjlaw89/viup) - 基于 C 的跨平台 UI 库 IUP 的 V 包装器。
- [vsdl](https://github.com/kjlaw89/vsdl) - 基于 C 的 SDL 库的 V 包装器。
- [vsdl2](https://github.com/nsauzede/vsdl2) - libSDL2 包装器。
- [vsl.vcl](https://github.com/vlang/vsl/tree/master/vcl#readme) - VCL 是使用 V 使用 OpenCL 编写程序的高级方法。这些是 V 的高度固定的 OpenCL 绑定。它试图通过一些糖抽象、V 的并发性和通道使 GPU 计算变得容易。
- [vbmp](https://github.com/dy-tea/vbmp) - 读取和写入位图文件。
- [voronoi](https://github.com/larpon/voronoi) - [JCash/voronoi](https://github.com/JCash/voronoi) 的 V 包装器。
- [vqoi](https://github.com/Le0Developer/vqoi) - V：QOI - “相当不错的图像”格式，用于快速、无损的图像压缩。

### 互操作性

- [jni](https://github.com/larpon/jni) - C Java 本机接口（桌面 + Android）的 V 包装器。
- [vjsx](https://github.com/guweigang/vjsx) - V 绑定到quickjs javascript 引擎。在V中运行JS。
- [vphp](https://github.com/guweigang/vphp) - Vlang 库，用于在 Vlang 中本地构建 PHP 扩展。

### IRC

- [vitric](https://github.com/m-242/vitric) - 透明的 IRC 库。

### 网络

- [netaddr](https://github.com/gechandesu/netaddr) - IPv4、IPv6 和 MAC（EUI-48、EUI-64）地址操作库。
- [netio](https://github.com/gechandesu/netio) - V 的低级网络库，提供对套接字的更多控制。
- [v-grpc](https://github.com/hyperpolymath/v-grpc) - gRPC 和 Protobuf 支持 V 以及 Idris2 ABI 证明和 Zig FFI。
- [vibe](https://github.com/tobealive/vibe) - 包装 libcurl 的请求库，可实现快速可靠的请求，同时提供更高级别的 API。
- [vmq](https://github.com/jordan-bonecutter/vmq) - [ZMQ](https://zeromq.org/) 的 V 包装器（又名 ZeroMQ、ØMQ、0MQ：高性能异步消息传递库）。

### 操作系统

- [clipboard](https://github.com/vlang/v/tree/master/vlib/clipboard) - 用于与操作系统剪贴板交互的 V 模块。完全跨平台。
- [mmap](https://github.com/jdonnerstag/vlang-mmap) - 为 Linux 和 Windows 上的内存映射提供本机 V-lang 支持。
- [vlipboard](https://github.com/asvvvad/vlipboard) - 易于使用的剪贴板包装器，支持 Wayland 和 Termux。
- [winreg](https://github.com/ldedev/WindowsRegistry) - MS Windows 注册表 API。 （开发中）

### 科学计算

- [vplot](https://github.com/erdetn/vplot) - GNU Plot 的 V 包装器 (`gnuplot_i`)。
- [vsl](https://github.com/vlang/vsl) - 具有多种不同模块的科学图书馆。尽管大多数模块提供纯 V 定义，但它还提供将已知 C 库包装在其他后端之间的模块，这些后端允许高性能计算作为替代方案。还为 OpenBLAS、LAPACKE、MPI、OpenCL 等库提供固定的包装器。
- [vstats](https://github.com/rodabt/vstats) - 一个用 V 从头开始编写的无依赖性线性代数、统计和机器学习库。
- [vtl](https://github.com/vlang/vtl) - V Tensor Library 是一个支持 n 维数据结构的数值计算库，由 VSL 支持。
- [NeuralNetworks-V-Module](https://github.com/Eliyaan/NeuralNetworks-V-Module) - 这是一个用于创建神经网络的 V 模块。

### 串行通讯

- [vi2c](https://github.com/erdetn/vi2c) - 一个用 V 编写的用于 Linux 的 I2C 串行通信的小型（包装）库。
- [vserialport](https://github.com/erdetn/vserialport) - [libserialport](https://sigrok.org/wiki/Libserialport) 的 V 包装器。
- [vserialx](https://github.com/erdetn/vserialx) - 一个用 V 编写的 Linux 小型（包装）串行通信库。

### 电信

- [vagi](https://github.com/Ouri028/vagi) - V 中的 Asterisk FastAGI 库。

### 电报

- [velegram](https://github.com/tailsmails/velegram) - TDLib（电报数据库库）的 V 语言包装器。
- [vgram](https://github.com/dariotarantini/vgram) - Telegram 机器人库。

### 文本处理


- [ascii_robot](https://github.com/Delta456/ascii_robot) - 用 V 编写的 ASCII 机器人生成器。
- [chalk](https://github.com/etienne-napoleone/chalk) - 对终端中的字符串进行着色。
- [cjson](https://github.com/lydiandy/cjson) - 为 vlang 封装 cJSON。
- [crayon](https://github.com/thecodrr/crayon) - 像毕加索一样绘制你的终端输出。 🖍️🎨
- [iconv](https://github.com/fanlia/iconv) - 将 iconv 换行为 vlang。
- [pcre2](https://github.com/srackham/pcre2) - 用于处理 PCRE 正则表达式的库。
- [read_xlsx_v](https://github.com/fanlia/read_xlsx_v) - 使用 vlang 读取 xlsx。
- [Rosie-RPL](https://github.com/jdonnerstag/vlang-rosie) - Rosie 模式语言 (RPL) 实现。
- [slugify](https://github.com/einar-hjortdal/slugify) - 将 Unicode 字符串转换为 url 友好、人类可读的 ASCII slugs。
- [text-processing](https://github.com/ArtemkaKun/text-processing) - V 文本处理库，包含操作文本数据的常用工具。
- [v-regex](https://github.com/spytheman/v-regex) - 一个简单的 V 正则表达式库。
- [vsoup](https://github.com/marcalc/vsoup) - 一个快速、受 JSoup 启发的 HTML5 解析器和 V DOM 操作库，由 Lexbor 提供支持。
- [vxml](https://github.com/i582/vxml) - 用于将 XML 解析为 DOM 的纯 V 库。
- [whisker](https://github.com/hungrybluedev/whisker) - 受胡子启发的 V 快速、强大的模板引擎。
- [xlsx](https://github.com/hungrybluedev/xlsx) - 用于读写 Microsoft Excel 文件的 V 库。
- [lexical_uuid](https://github.com/einar-hjortdal/lexical_uuid) - 按字典顺序排序的通用唯一标识符。

### 用户界面工具包

- [bobatea](https://github.com/tauraamui/bobatea) - TUI 框架的灵感来自于 Bubble Tea。
- [iUI](https://github.com/isaiahpatton/ui) - Isaiah 的 V 跨平台 GUI 库。受到 Java Swing 语法的启发。
- [mui](https://github.com/malisipi/mui) - 适用于 Windows、Linux、Android 和 Web 的跨平台 UI 库。
- [V UI](https://github.com/vlang/ui) - 适用于 Windows、macOS、Linux、Android、iOS 和 Web 的集成跨平台 UI 工具包。
- [vgtk3](https://github.com/vgtk/vgtk3) - V 中 GTK3 的包装器。
- [vig](https://github.com/nsauzede/vig) - [Dear ImGui](https://github.com/ocornut/imgui) GUI 工具包的绑定。
- [vnk](https://github.com/nsauzede/vnk) - [Nuklear](https://github.com/vurtun/nuklear) GUI 工具包的绑定。
- [V-WebUI](https://github.com/webui-dev/v-webui) - WebUI 的包装器。一个轻量级库，允许您使用任何 Web 浏览器作为 GUI，后端使用 V，前端使用 HTML5。
- [webview](https://github.com/ttytm/webview) - webview 的绑定。一个用于构建现代跨平台 GUI 应用程序的小型库。它允许将 V 与现代 Web 技术相结合来设计图形用户界面。

### 实用性

- [dialog](https://github.com/ttytm/dialog) - 用于打开系统对话框的跨平台实用程序库 - 打开文件、消息框、颜色选择器等。
- [dotenv](https://github.com/einar-hjortdal/dotenv) - 从 .env 文件加载环境变量以用于开发目的。
- [json2v](https://github.com/ldedev/Json2V) - 将 json 转换为 Vlang 中的结构体。
- [objc](https://github.com/magic003/objc) - V 绑定到 Objective-C 运行时。
- [range](https://github.com/Delta456/range) - V 中 Python range() 的功能。
- [ssh-config](https://github.com/walkingdevel/ssh-config) - 用于解析 SSH 配置文件的 V 库。
- [structlog](https://github.com/gechandesu/structlog) - V 的结构化日志库。
- [V-crypto](https://github.com/bstnbuck/V-crypto) - 附加加密算法的实现。
- [vaker](https://github.com/ChAoSUnItY/vaker) - 用 V 编写的轻量级编译时生成的数据伪造器。
- [vanadium](https://github.com/tailsmails/vanadium) - V 编程语言的 Ada 级运行时安全性。
- [vdotenv](https://github.com/zztkm/vdotenv) - 支持加载环境变量的 .env 文件。
- [vhs](https://github.com/KevinDaSilvaS/vhs) - Haskell prelude 列表函数（zip、zipwith、head 等）在 V 中实现。
- [VInstall](https://github.com/malisipi/VInstall) - 跨平台安装程序创建者。
- [votp](https://github.com/OdaiGH/votp) - v 中的 TOTP 和 HOTP 实现

### 网络

- [blobly](https://github.com/einar-hjortdal/blobly) - 中央文件服务器。
- [jsonrpcv](https://github.com/Te4nick/jsonrpcv) - 纯 V 中的 JSON-RPC 2.0 客户端+服务器实现。
- [pico.v](https://github.com/S-YOU/pico.v) - 基于 picoev 和 picohttpparser 的 V 中的 Web 服务器。
- [sessions](https://github.com/einar-hjortdal/sessions) - 与 Web 框架无关的会话库。
- [v-graphql](https://github.com/hyperpolymath/v-graphql) - 具有模式生成、Idris2 ABI 证明和 Zig FFI 的 GraphQL 服务器实现。
- [v-jsonrpc](https://github.com/nedpals/v-jsonrpc) - 在 V 上编写的基本 JSON-RPC 2.0 兼容服务器。
- [v-rest](https://github.com/hyperpolymath/v-rest) - 具有 Idris2 ABI 证明和 Zig FFI 的 REST API 服务器框架。
- [v-tiktok](https://github.com/walkingdevel/v-tiktok) - 用于下载 TikTok 视频的 V 库。
- [validate](https://github.com/endeveit/v-validate) - 一个简单的库，用于验证 V 中的字符串。
- [valval](https://github.com/taojy123/valval) - 用V编写的Web框架，由vweb改进。
- [vcurrency](https://github.com/mehtaarn000/vcurrency) - [https://api.exchangeratesapi.io](https://api.exchangeratesapi.io) 的 API 包装器（用 V 编写）。
- [veb](https://github.com/vlang/v/tree/master/vlib/veb) - V 的内置 Web 框架。
- [vest](https://github.com/alexferl/vest) - V 中的 REST 客户端。
- [vex](https://github.com/nedpals/vex) - 在 V 上编写的 Web 框架受到 Express 和 Sinatra 的启发。
- [vigest](https://github.com/withs/vigest) - 用于摘要身份验证的简单客户端（用 V 编写）。
- [vite.v](https://github.com/siguici/vite.v) - Veb 应用程序的无缝 [Vite.js](https://vite.dev) 集成。
- [vxbloauth](https://github.com/WolvesFortress/vxbl-oauth) - 适用于 vweb 的简约 Xbox Live 身份验证器。
- [west](https://github.com/Dracks/West) - vweb 的包装器以与 Nestjs 类似的方式工作，使用模块和依赖项注入。

## 其他

### 文章

- [V简介](https://simonknott.de/articles/VLang.html)

### 书籍

- [Getting Started with V Programming - Navule Pavan Kumar Rao - Packt 2021 Dec](https://www.amazon.com/Getting-Started-Programming-end-end-ebook/dp/B09FKK3JL7/ref=sr_1_1?keywords=Getting+started+with+V+programming&qid=1639480830&sr=8-1) - V 的入门书

### 社区

- [V社区](https://github.com/v-community)

### 编辑器插件

- [tree-sitter-v](https://github.com/undivisible/tree-sitter-v) - V 语言的树保护语法。使用现代 API、crates.io 包、244 个节点类型维护分支。

#### 原子

- [language-v](https://github.com/Cutlery-Drawer/language-v) - Atom 的 V 语言支持（vscode-vlang 的端口）。

#### Emacs

- [v-mode](https://github.com/damon-kwok/v-mode) - Emacs 主要模式为V 编程语言。
- [vlang-mode.el](https://github.com/Naheel-Azawy/vlang-mode.el) - Emacs 主要模式为V 编程语言。

#### 脉冲星

- [language-v](https://packages.pulsar-edit.dev/packages/language-v) - Atom 的 V 语言支持（vscode-vlang 的端口）（从atom.io 迁移）

#### 崇高文本3

- [sublime-v](https://github.com/onerbs/sublime-v) - 适用于 V 编程语言的全功能 Sublime Text 3 包。
- [vlang-sublime](https://github.com/oversoul/vlang-sublime) - Sublime Text 3 支持 Vlang 编程语言。

#### VS代码

- [vscode-vlang](https://github.com/vlang/vscode-vlang) - Visual Studio Code 的 V 语言扩展。
- [v-analyzer](https://github.com/vlang/v-analyzer) - 将 V 编程语言的 IDE 功能引入 VS Code。

#### 维姆

- [v-vim](https://github.com/ollykel/v-vim) - Vim 中支持 V 语法突出显示。
- [vim-v](https://github.com/cheap-glitch/vim-v) - V 编程语言的高质量语法突出显示。
- [vim-vtools](https://github.com/zakuro9715/vim-vtools) - Vim 的 V 工具，包括自动格式化。

### 论坛

- [r/vlang](https://www.reddit.com/r/vlang)
- [堆栈溢出](https://stackoverflow.com/questions/tagged/vlang)

### GitHub 操作

- [action-create-v-docs](https://github.com/marketplace/actions/create-documentation-for-v-modules) - 为 V 模块创建文档的 GitHub 操作。
- [setup-v](https://github.com/marketplace/actions/setup-vlang) - 在工作流程中安装和使用 V 的 GitHub 操作。

### GitHub 模板

- [v-project-basement](https://github.com/ArtemkaKun/v-project-basement) - 每个 V 项目的地下室，其中包含 V 项目的通用最小 GitHub CI 脚本和问题模板。

### 带 V 的 IDE

- [Vide](https://github.com/IsaiahPatton/Vide)

### 带 V 的在线 IDE

- [V游乐场](https://play.vlang.io)
- [V游乐场（旧）](https://v-wasm.now.sh/)
- [VOSCA V 游乐场](https://play.vosca.dev)

### 操作系统和操作系统开发示例

- [limine-v-template](https://github.com/plos-clan/limine-v-template) - 用于在 V 中构建符合 Limine 的内核的简单模板。
- [Simple Linux kernel module example](https://github.com/spytheman/simple_kernel_module_in_v) - 使用 V 编写一个非常简单的 Linux 内核模块的演示和测试。
- [v-limine](https://github.com/wenxuanjun/v-limine) - 用于处理 Limine 启动协议结构的 V 库。

### 图案

- [MVU.v](https://github.com/ArtemkaKun/MVU.v) - 用 V 编程语言实现的 MVU 模式（The Elm Architecture）。

### 编程竞赛

- [Advent of Code 2019](https://github.com/mvlootman/aoc2019) - V中Advent of Code 2019的解决方案。
- [Advent of Code 2022](https://github.com/vlang/adventofcode) - V 中 Code 2022 的出现的解决方案。
- [V 中的 Rosetta 代码](https://rosettacode.org/wiki/Category:V_(Vlang)) - V 中的 Rosetta 代码解决方案。
- [SoloLearn Coding Challenges](https://github.com/Serkonda/v-sololearn-coding-challenges) - 在 V 中实施 SoloLearn 编码挑战。

### 语法高亮

- [kate-syntax-highlight-v](https://github.com/Larpon/kate-syntax-highlight-v) - [Kate](https://kate-editor.org/) 的 V 语法高亮显示。
- [scite-v-support](https://github.com/sunnylcw/scite-v-support) - [SciTE](https://www.scintilla.org/SciTE.html) 的 V 语法突出显示。

### 教程

- [在 Y 分钟内学习 V](https://github.com/v-community/learn_v_in_y_minutes)
- [V by Example](https://github.com/v-community/v_by_example) - V 书作为 [GitBook](https://v-community.gitbook.io/v-by-example/)。
- [V for Node Devs](https://github.com/Thigidu/vlang-for-nodejs-developers) - 面向 Node js 开发人员的 Vlang。
- [V learning notes](https://github.com/lydiandy/vlang_note) - 个人中文学习笔记。
- [VOSCA Blog Tutorials](https://blog.vosca.dev/categories/tutorials/) - VOSCA 博客上的教程类别。

### 视频

- [V 编程语言](https://www.youtube.com/channel/UCLZIElNyubHOvbfudT7KS1A)
- [V 编程教程](https://www.youtube.com/watch?v=BVCuZ7z7GMY&list=PLEPMhdsq-gNpFr40A-ZnX-Hu9l-Sp5Oc_)
