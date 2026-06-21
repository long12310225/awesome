# 很棒的红豆杉 [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[<img src=“logo.svg”align=“right”width=“100”title=“Awesome Yew”>](https://github.com/yewstack/yew)

> 与紫杉相关的精彩事物的精选列表。

[Yew](https://github.com/yewstack/yew) 是一个受 Elm 和 React 启发的现代 Rust 框架，用于使用 WebAssembly 创建多线程前端应用程序。

欢迎投稿！首先阅读[贡献指南](CONTRIBUTING.md)。

## 内容

- [Official](#official)
- [Projects](#projects)
- [Templates](#templates)
- [Crates](#crates)
  - [组件库](#component-libraries)
  - [Components](#components)
  - [Hooks](#hooks)
  - [Utils](#utils)
  - [Wasm](#wasm)
- [Tooling](#tooling)
- [Articles](#articles)
- [Books](#books)
- [Alternatives](#alternatives)
- [相关列表](#related-lists)

## 官方

- [Yew](https://github.com/yewstack/yew) - 用于构建客户端 Web 应用程序的 Rust / WebAssembly 框架。
- [Live demo](https://yew-todomvc.netlify.com) - 一个 todomvc 演示。
- [Examples](https://github.com/yewstack/yew/tree/master/examples) - 官方仓库中包含较小的示例。
- [API Docs](https://docs.rs/yew) - docs.rs 上的文档。
- [Website](https://yew.rs/) - 官方网站。
- [Chatroom](https://discord.gg/VQck8X4) - 它非常活跃，是提问的好地方。
- [Reddit](https://www.reddit.com/r/yew_web/) - Reddit 专用子版块。
- [Financial Contribute](https://opencollective.com/yew) - 成为财务贡献者并帮助我们维持我们的社区。
- [Playground](https://play.yew.rs) - Yew 的在线游乐场。

## 项目

- [Realworld example](https://github.com/jetli/rust-yew-realworld-example-app) - 使用 Rust + Yew + WebAssembly 构建的示例性现实世界应用程序。它利用了Yew最新的“功能组件”和“钩子”。它还支持由 [Tauri](https://github.com/tauri-apps/tauri) 提供支持的桌面应用程序。
- [webapp.rs](https://github.com/saschagrunert/webapp.rs) - 一个完全用 Rust 编写的 Web 应用程序，前端是用 Yew 构建的。
- [Rust-Full-Stack](https://github.com/steadylearner/Rust-Full-Stack) - 通过博客文章来解释它们，可以轻松测试和使用 Rust 代码。
- [Bucket Questions](https://github.com/hgzimmerman/BucketQuestions) - 一个完全用 Rust 编写的网络应用程序，用于一个愚蠢的派对游戏。
- [web-view todomvc desktop app](https://github.com/Extrawurst/rust-webview-todomvc-yew) - 演示如何将 yew 用于编译为 WebAssembly 的 todomvc，并通过 [web-view](https://github.com/Boscop/web-view) 捆绑为轻量级（~2mb）桌面应用程序，作为 Electron 的替代品，[web-view](https://github.com/Boscop/web-view) 也有一个[演示](https://github.com/Boscop/web-view/tree/master/examples#todo-yew)。
- [yew-react-example](https://github.com/hobofan/yew-react-example) - 该项目展示了如何使用 Yew 组件内的 React 组件创建 Web 应用程序。
- [Kirk](https://github.com/stkevintan/Kirk) - 只是一个 Rust WebAssembly 博客。
- [rust-async-wasm-demo](https://github.com/extraymond/rust-async-wasm-demo) - 用于学习 Rust 和可部署到网络的异步的玩具项目。
- [karaoke-rs](https://github.com/tarkah/karaoke-rs) - Rust 中的一个简单的、支持网络的卡拉 OK 播放器。
- [I Love Hue! (rs)](https://github.com/noc7c9/i-love-hue-rs) - Yew (Rust) 中手机游戏“I Love Hue”的克隆。
- [yew-styles-page](https://github.com/spielrs/yew-styles-page) - 这是 yew 框架风格的初始项目。
- [caniuse.rs](https://github.com/jplatte/caniuse.rs) - Rust 特征搜索。
- [Rust electron yew demo](https://github.com/Extrawurst/rust-electron-demo) - 使用 Electron 将基于 Rust 的 Web 应用程序 (Yew) 构建到本机应用程序的示例。
- [covplot](https://github.com/jbowens/covplot) - 全球 CoVID-19 数据的实时图表。
- [Minesweeper](https://github.com/jgpaiva/minesweeper) - 使用 Rust、Yew 和 WebAssembly 构建的扫雷游戏。
- [Freecell](https://github.com/Stigjb/freecell) - 用 Rust 和 Yew 编写的耐心游戏。
- [Yew-WebRTC-Chat](https://github.com/codec-abc/Yew-WebRTC-Chat) - 使用 Yew 制作的简单 WebRTC 聊天。
- [Yew Fullstack Boilerplate](https://github.com/lukidoescode/yew-fullstack-boilerplate) - 使用 Rust 创建全栈应用程序的高度固执的样板。
- [Chord Quiz](https://github.com/Stigjb/chord-quiz) - 在此 Rust/Yew/WebAssembly 应用程序中练习识别和弦。
- [RustMart](https://github.com/sheshbabu/rustmart-yew-example) - 使用 Rust、Wasm 和 Yew 编写的单页应用程序 (SPA)。
- [DevAndDev](https://github.com/alepez/devand) - 开发人员可以找到结对编程合作伙伴的网站。用 Rust、Yew 前端编写。
- [yew-octicons](https://github.com/io12/yew-octicons) - 在 Yew 项目中使用 Octicons 的简单界面。
- [Pipe](https://github.com/pipe-fun/pipe) - 这是一个 Rust / Wasm 客户端 Web 应用程序，它是一个任务控制中心。
- [note-to-yew](https://github.com/oovm/note-to-yew) - 在线将您的标记转换为 Yew 宏，这也是由 Yew 制作的。
- [ASCII-Hangman](https://github.com/getreu/ascii-hangman) - 适合儿童的可配置绞刑吏游戏，具有 ASCII 艺术奖励。
- [dotdotyew](https://github.com/shaunbennett/dotdotyew) - [Dot-voting](https://en.wikipedia.org/wiki/Dot-voting) 使用 Yew，并使用 Rust 为后端 API 提供支持。
- [wasm-2048](https://github.com/dev-family/wasm-2048) - 2048 游戏使用 Rust 和 Yew 实现并编译为 Wasm。
- [website-wasm](https://github.com/kamiyaa/website-wasm) - 我的个人网站通过 Yew/Wasm 用 Rust 编写。
- [KeyPress](https://github.com/rayylee/keypress) - 一个用于练习中文英语的 Rust WebAssembly 网站示例。
- [yew-train-ticket](https://github.com/anthhub/yew-train-ticket) - 一个基于 Yew 最新钩子和函数式 API 的 Rust WebAssembly [Webapp](http://118.190.37.169:8002) 示例，代码风格非常像 React 函数组件。
- [yew-d3-example](https://github.com/ivanschuetz/yew-d3-example) - 显示 Yew 的 d3 图表。
- [Oxfeed](https://github.com/sanpii/oxfeed) - 用 Rust 编写的提要阅读器，带有 Yew 前端。
- [Flow.er](https://github.com/LighghtEeloo/flow.er) - 与待办事项列表实用程序集成的笔记本应用程序。使用 Rust、WebAssembly、Yew 和 Trunk 开发。
- [Fullstack-Rust](https://github.com/vascokk/fullstack-rust) - 带有 Actix-web、Yew、Bulma CSS 和 Diesel 的全栈 Rust 应用程序（Connect5 游戏）。
- [Sea_battle](https://github.com/MAE664128/sea_battle) - 海战游戏的简单示例。铁锈+红豆杉。
- [tide-async-graphql-mongodb](https://github.com/zzy/tide-async-graphql-mongodb) - graphql 服务的干净样板，带有 wasm/yew 前端。
- [surfer](https://github.com/zzy/surfer) - 一个基于 yew + graphql 构建的博客，带有[现场演示站点](https://niqin.com)。 graphql 服务的后端和 Web 应用程序的前端。
- [qubit](https://abhimanyu003.github.io/qubit) - 一个方便的计算器，基于 Rust 和 WebAssembly，[现场演示](https://abhimanyu003.github.io/qubit/)。
- [Paudle](https://github.com/pmsanford/paudle) - 由 Josh Wardle 重新实现的优秀文字游戏 Wordle。
- [Rust algorithms](https://github.com/Jondolf/rust-algorithms) - 具有各种算法的交互式实现的网站。
- [Marc Portfolio](https://gitlab.com/marcempunkt/maeurerdev) - 软件开发人员组合，[现场演示](https://maeurer.dev/)。
- [zzhack](https://github.com/zzhack-stack/zzhack) - 个人博客，基于Rust & Yew，[Live Demo](https://www.zzhack.fun/)。
- [Rquote](https://github.com/Altair-Bueno/rquote) - Rquote 是一个使用 Rust 和 WebAssembly 构建的 Web 应用程序。它从 Animechan API 获取动漫报价。 [现场演示](https://rquote.vercel.app/)。
- [yew-ssr-tide](https://github.com/zzy/yew-ssr-tide) - 该示例演示了 Yew 使用潮汐和冲浪进行服务器端渲染，它需要 Yew 的**开发版本**。
- [yew-ssr-actix-web](https://github.com/zzy/yew-ssr-actix-web) - 该示例演示了使用 actix-web 和 reqwest 进行 Yew 服务器端渲染，它需要 Yew 的**开发版本**。
- [PixelGuesser](https://github.com/tdooms/pixelguesser) - PixelGuesser 是一款现实生活中的派对游戏，玩家尝试尽快猜测图像的内容。
- [Crabtyper](https://github.com/brancobruyneel/crabtyper) - 用 Rust 编写的快速打字 Web 应用程序。
- [We-Come Monorepo](https://github.com/kabinetkmitb/wecome) - 这是 wecome KM ITB 的 monorepo，[现场演示](https://wecome-itb.com/)。
- [blog-rs](https://github.com/songday/blog-rs) - 一个前端和后端全部用 Rust 编写的博客系统。后端由 Warp 提供支持，前端基于 Yew (WASM) 构建。
- [mb2](https://devctm.com) - 带有 Yew 客户端的扑克服务器。单击“演示”按钮，然后单击“开始”以查看客户端。
- [Puzzle Cube](https://github.com/wainwrightmark/puzzle_cube) - 使用 Rust 和 Yew 的 Rubix Cube 求解器，[现场演示](https://wainwrightmark.github.io/puzzle_cube/)。
- [CubeShuffle](https://github.com/philipborg/CubeShuffle) - 用 Rust、Yew、Bulma 和 Tauri 构建的纸牌游戏洗牌实用程序。
- [Rust Audio](https://github.com/austintheriot/audio) - 在浏览器中使用 Rust/WASM 进行实时音频处理/合成，[现场演示](https://austintheriot.github.io/audio/)。
- [Kiomet](https://github.com/SoftbearStudios/kiomet) - 一款在线即时战略游戏，您可以通过占领塔楼来扩大领土。
- [Portfolio website](https://github.com/simbleau/website) - 由 Spencer Imbleau 设计的内置无障碍功能的 SPA 组合。
- [tchatche.rs](https://github.com/nag763/tchatchers) - 在 Yew 和 Axum 中构建的基于 Websocket 聊天的应用程序。
- [viz.rs](https://github.com/viz-rs/viz-rs.github.io) - 一个可视化 Web 框架网站，[Live Demo](https://viz.rs/)。
- [theiskaa.com](https://github.com/theiskaa/theiskaa.com) - Yew 框架的现实世界实现。 [住在 theiskaa.com](https://theiskaa.com)。
- [live-ask.com](https://github.com/liveask/liveask) - 实时活动/聚会问答平台。 [在 live-ask.com 直播](https://live-ask.com)。
- [Sumi](https://github.com/vgwidt/sumi) - 使用 Yew 和 Actix 构建的多用户问题跟踪和知识库应用程序。
- [hurlurl](https://github.com/lucasmerlin/hurlurl) - 随机链接缩短器，[现场演示](https://hurlurl.com/)。
- [Macige](https://github.com/tramlinehq/macige) - 用于移动应用程序开发的 CI 工作流程生成器，[现场演示](https://macige.tramline.app)。
- [Spaceman](https://github.com/eliaperantoni/spaceman) - Spaceman 是一个跨平台 gRPC 客户端，旨在使用起来令人愉悦且美观。
- [Crypto-helper](https://github.com/TheBestTvarynka/crypto-helper) - 可以在客户端对数据进行哈希、加密和签名的 Web 应用程序。还包括 JWT 调试器。 [网站](https://crypto.qkation.com)。
- [zoom-rs](https://github.com/security-union/zoom-rs) - 用于研究目的用 Rust 编写的 Zoom 克隆。
- [Ubiquity](https://github.com/opensourcecheemsburgers/ubiquity) - 开源、跨平台的 Markdown 编辑器；使用 Yew、Tauri、Tailwind 和 DaisyUI 构建。 [网络应用程序](https://ubiquity.rs)。
- [demo_web_zip_wasm](https://github.com/MAE664128/demo_web_zip_wasm) - 一个使用 WebAssembly 创建在浏览器中运行的 ZIP 存档的简单示例程序，[实时演示](https://mae664128.github.io/demo_web_zip_wasm/)。
- [RustedLessPass](https://github.com/RustedLessPass/RustedLessPass) - 无状态密码管理器。 [网络应用程序](https://rustedlesspass.github.io/)。
- [windows-terminal-theme-generator](https://github.com/LelouchFR/windows-terminal-theme-generator/) - 创建 Windows 终端主题，简化您的生活。 [现场演示](https://windows-terminal-theme-generator.netlify.app/)
- [SandCat](https://github.com/Xu-Mj/sandcat) - 该软件主要实现了IM应用的基本功能，包括基础好友系统、一对一聊天、群聊、一对一音视频通话等。它还支持 i18n，目前提供中英文切换。
- [PinePods](https://github.com/madeofpendletonwool/PinePods) - PinePods 是一个基于 Rust 的播客管理系统，它管理具有多用户支持的播客，并依赖于客户端连接到它的中央数据库。
- [0721](https://github.com/langyo/0721) - 用 Rust 编写的图像托管引擎。
- [Hikari](https://github.com/celestia-island/hikari) - 一切的前端。
- [simply-view-image-for-python-debugging](https://github.com/elazarcoh/simply-view-image-for-python-debugging?tab=readme-ov-file) - Visual Studio代码扩展在调试Python时只需查看图像变量的图像。
- [Mindsweeper](https://github.com/AlexBuz/mindsweeper) - 对扫雷的原则性看法，[现场演示](https://alexbuz.github.io/mindsweeper/)。
- [scap-rs](https://github.com/emo-crab/scap-rs) - Rust实现的国家漏洞数据库（NVD），[现场演示](https://scap.kali-team.cn/)。
- [Sentry Relay](https://github.com/getsentry/relay) - Sentry Relay 是一项将 Sentry SDK 和 Sentry 服务器的某些功能推送到代理进程的服务。
- [Syre](https://github.com/syre-data/syre) - 科学的数据管理和见解。
- [candle-wasm-examples](https://github.com/huggingface/candle) - Candle 是 Rust 的极简 ML 框架，重点关注性能（包括 GPU 支持）和易用性。尝试我们的在线演示：[whisper](https://huggingface.co/spaces/lmz/candle-whisper)、[LLaMA2](https://huggingface.co/spaces/lmz/candle-llama2)、[T5](https://huggingface.co/spaces/radames/Candle-T5-Generation-Wasm)、 [yolo](https://huggingface.co/spaces/lmz/candle-yolo)，[段
任何东西](https://huggingface.co/spaces/radames/candle-segment-anything-wasm)。
- [chipbox](https://github.com/chipnertkj/chipbox) - Chipbox 是一个用 Rust 编写的开源桌面 DAW。
- [Taxy](https://github.com/picoHz/taxy/tree/main) - 一个内置WebUI的反向代理服务器，支持TCP/HTTP/TLS/WebSocket，用Rust编写。
- [Proxelar](https://github.com/emanuele-em/proxelar) - 基于 Rust 的中间人代理，这是一个早期项目，旨在提供网络流量的可见性。
- [diff.rs](https://github.com/xfbs/diff.rs) - 用于呈现 Rust 板条箱版本之间差异的 Web 应用程序。在 Yew 中实现，作为 WebAssembly 在浏览器中完全运行，[现场演示](https://diff.rs)。
- [konnektoren.help](https://github.com/Konnektoren/konnektoren-web-game) - 用于学习德语语法的交互式网络应用程序，具有游戏化挑战和基于地图的界面。 [网络应用程序](https://konnektoren.help)
- [layout-viewer](https://prideout.net/layout-viewer) - 检查具有缩放和平移控制的集成电路布局。
- [Google Wasefire](https://github.com/google/wasefire) - 注重开发人员体验的安全固件框架。
- [Apache Iggy](https://github.com/apache/iggy) - Apache Iggy：以激光速度实现超高效消息流。

## 模板

- [Create Yew App](https://github.com/jetli/create-yew-app) - 通过运行一个命令“npx create-yew-app my-app”来设置现代 Yew Web 应用程序。
- [yew-wasm-pack-template](https://github.com/yewstack/yew-wasm-pack-template) - 用于启动与 wasm-pack 一起使用的 Yew 项目的模板。
- [yew-wasm-pack-minimal](https://github.com/yewstack/yew-wasm-pack-minimal) - 使用 wasm-bindgen 和 wasm-pack 启动 Yew 项目的最小模板。
- [yew-parcel-template](https://github.com/spielrs/yew-parcel-template) - 很棒的 Yew 与 Yew-Router 和 Parcel 应用程序。
- [yew-template-for-github-io](https://github.com/Ja-sonYun/yew-template-for-github-io) - github.io 的 yew 项目的可直接部署模板，使用 tailwind 和 webpack 进行 css，使用 trunk 进行构建和服务。
- [tailwindcss-yew-template](https://github.com/vvcaw/tailwindcss-yew-template) - 将 Tailwindcss 与 Yew 结合使用的简单布局。
- [axum-yew-setup](https://github.com/rksm/axum-yew-setup) - 一个入门项目，为全栈 Rust Web 应用程序设置 Axum 和 Yew。
- [rust-yew-axum-tauri-desktop](https://github.com/jetli/rust-yew-axum-tauri-desktop) - Rust + Yew + Axum + Tauri，桌面应用程序的全栈 Rust 开发。
- [Yew PWA Minimal](https://github.com/fkohlgrueber/yew-pwa-minimal) - 使用 Yew 的最小渐进式 Web 应用程序。
- [Yew HTTP Starter](https://github.com/LeTurt333/yew_http_starter) - Yew 模板带有简单的 HTTP 消息和有用的帮助注释。
- [Yew minimlistic template](https://github.com/averichev/yew-starter-template) - 用于快速启动红豆杉项目的简约模板。

## 板条箱

### 组件库

- [yew-mdc](https://github.com/dungeonfog/yew-mdc) - Yew 框架的材料设计组件。
- [muicss-yew](https://github.com/AlephAlpha/muicss-yew) - Yew 框架的 MUI-CSS 组件。
- [yew-bulma](https://github.com/kellpossible/yew-bulma) - 一个 Rust 库，为使用 Yew 的项目提供基于 bulma css 库的组件。
- [material-yew](https://github.com/hamza1311/material-yew) - Material Web 组件的 Yew 包装器。
- [Yewprint](https://github.com/yewprint/yewprint) - blueprintjs.com 到 Yew 的端口。
- [ybc](https://github.com/thedodd/ybc) - 基于 Bulma CSS 框架的 Yew 组件库。
- [patternfly-yew](https://github.com/ctron/patternfly-yew) - Yew 的 Patternfly 组件。
- [yew-feather](https://github.com/pedrodesu/yew-feather) - 红豆杉的羽毛图标组件。
- [tailwind-yew-builder](https://github.com/matiu2/tailwind-yew-builder) - 使用 docker-compose 为 Yew 构建 Tailwind CSS。还支持中继。
- [yew-components](https://github.com/angular-rust/yew-components) - Yew 框架的材料设计组件。
- [yew-chart](https://github.com/titanclass/yew-chart) - 一个基于 Yew 的图表库，提供基于 SVG 的组件来渲染图表。
- [tailyew](https://github.com/fuzzycloud/tailyew) - Yew 围绕 DaisyUI（基于 tailwindcss）组件进行包装。
- [yew-duskmoon-ui](https://github.com/gsmlg-dev/yew-duskmoon-ui) - Duskmoon UI 组件库。该包使用 `stylist` 将 CSS 嵌入到组件中，因此不需要额外的 CSS 文件。 [现场演示](https://gsmlg-dev.github.io/yew-duskmoon-ui/)。
- [yew-bootstrap](https://github.com/isosphere/yew-bootstrap) - Bootstrap 5 组件库的 Yew 包装器。
- [Zu](https://github.com/RustVis/zu) - Yew Web 组件，实现材料设计。
- [yew-nav-link](https://github.com/RAprogramm/yew-nav-link) - 导航链接根据应用程序中的当前路线了解其活动状态。
- [Rust Lucide](https://lucide.rustforweb.org) - Lucide 的 Yew 端口，一个由社区制作的漂亮且一致的图标工具包。
- [Rust Radix](https://radix.rustforweb.org) - Radix 的 Yew 端口，一个组件、图标、颜色和模板库，用于构建高质量、可访问的 UI。
- [Rust shadcn/ui](https://shadcn-ui.rustforweb.org) - shadcn/ui 的 Yew 端口，一个设计精美的组件库，您可以将其复制并粘贴到您的应用程序中。

### 组件

- [Yew Form](https://github.com/jfbilodeau/yew_form) - 使用 Yew 简化处理表单的组件。
- [yew-component-size](https://github.com/AircastDev/yew-component-size) - 当父组件更改宽度/高度时发出事件的 Yew 组件。
- [yew-virtual-scroller](https://github.com/AircastDev/yew-virtual-scroller) - 用于虚拟滚动/滚动窗口的 Yew 组件。
- [yew-oauth2](https://github.com/ctron/yew-oauth2/) - 一个普通的 Yew OAuth2/OpenIDConnect 组件，不依赖于任何 CSS 框架。
- [yew-scroll-area](https://github.com/MatchaChoco010/yew-scroll-area) - Yew 的自定义滚动区域。

### 挂钩

- [yew-hooks](https://github.com/jetli/yew-hooks) - Yew 的自定义 Hooks 库，灵感来自 [streamich/react-use](https://github.com/streamich/react-use) 和 [alibaba/hooks](https://github.com/alibaba/hooks)。
- [yew-side-effect](https://github.com/futursolo/yew-side-effect) - 受 [react-side-effect](https://github.com/gaearon/react-side-effect) 和 [react-helmet](https://github.com/nfl/react-helmet) 启发，协调 Yew 应用程序中的副作用。
- [Bounce](https://github.com/bounce-rs/bounce) - Yew 的简单状态管理库，受到 [Redux](https://github.com/reduxjs/redux) 和 [Recoil](https://github.com/facebookexperimental/Recoil) 的启发。
- [yewv](https://github.com/yewv/yewv) - Yew 的闪电般快速状态管理模块，以性能和简单性为首要任务。

### JavaScript 库端口

- [Plotly.rs](https://github.com/igiagkiozis/plotly) - 流行的 [Plotly](https://plotly.com/javascript/) 图表库的 Rust 绑定。
- [ag-grid-rs](https://github.com/mfreeborn/ag-grid-rs) - [AG Grid](https://www.ag-grid.com/javascript-data-grid/) 数据表库的 Rust 绑定。
- [popper-rs](https://github.com/ctron/popper-rs/) - [Popper JS](https://popper.js.org/) Rust 绑定。

### 实用工具

- [Yewdux](https://github.com/intendednull/yewdux) - Yew 应用程序的类似 Redux 的状态容器。
- [reacty_yew](https://github.com/hobofan/reacty_yew) - 通过 Typescript 类型定义从 React 组件生成 Yew 组件。
- [styled-yew](https://github.com/IcyDefiance/styled-yew) - Rust 中的 CSS，类似于样式组件，但适用于 Yew。
- [stylist-rs](https://github.com/futursolo/stylist-rs) - 适用于 WebAssembly 应用程序的 CSS-in-Rust 样式解决方案。
- [Yew Interop](https://github.com/Madoshakalaka/yew-interop) - 在 Yew 中异步加载 JavaScript 和 CSS。
- [Tailwind RS](https://github.com/oovm/tailwind-rs) - Rust 中的 Tailwind 风格跟踪器，JIT + AOT 解释器。
- [yew-style-in-rs](https://github.com/MatchaChoco010/yew-style-in-rs) - Rust for Yew 中的作用域 CSS。
- [yew_icons](https://github.com/finnbear/yew_icons) - 轻松将各种 svg 图标（Feather/Font Awesome/Octicons）包含到您的 Yew 应用程序中。
- [Yew-Template](https://github.com/INSAgenda/yew-template) - 使用 Yew 时用于分离 HTML 和 Rust 代码的 crate。
- [yew-nested-router](https://github.com/ctron/yew-nested-router) - 支持嵌套的路由器，Yew 0.20。
- [turf](https://github.com/myFavShrimp/turf) - 基于宏的编译时 SCSS 转译、CSS 缩小和受 CSS 模块启发的类名唯一化工具链。
- [browser-panic-hook](https://github.com/ctron/browser-panic-hook) - 浏览器环境的恐慌处理程序，允许以最终用户友好的方式失败。
- [Rust Floating UI](https://floating-ui.rustforweb.org/) - Floating UI 是一个库，可帮助您创建“浮动”元素，例如工具提示、弹出窗口、下拉菜单等。

### 瓦斯姆

- [wasm-bindgen](https://github.com/rustwasm/wasm-bindgen) - 促进 WebAssembly 模块和 JavaScript 之间的高级交互。
- [stdweb](https://github.com/koute/stdweb) - 提供 Rust 到 Web API 的绑定，并允许 Rust 和 JavaScript 之间的高度互操作性。
- [tauri-sys](https://github.com/JonasKruckenberg/tauri-sys) - 使用 wasm-bindgen 的项目对 Tauri API 的原始绑定。

### 框架

- [stackable](https://github.com/futursolo/stackable) - Yew 的框架体验。

## 工装

- [wasm-pack](https://github.com/rustwasm/wasm-pack) - 您最喜欢的 Rust -> WebAssembly 工作流程工具。
- [wasm-pack-action](https://github.com/jetli/wasm-pack-action) - Github 操作通过下载可执行文件来安装“wasm-pack”以加速 CI/CD。
- [wasm-bindgen-action](https://github.com/jetli/wasm-bindgen-action) - Github 操作通过下载可执行文件来安装“wasm-bindgen”以加速 CI/CD。
- [cargo-web](https://github.com/koute/cargo-web) - 用于客户端 Web 的 Cargo 子命令。
- [Trunk](https://github.com/thedodd/trunk) - 构建、捆绑您的 Rust Wasm 应用程序并将其发布到网络上。
- [trunk-action](https://github.com/jetli/trunk-action) - Github 操作通过下载可执行文件来安装“Trunk”以加速 CI/CD。
- [wabt](https://github.com/WebAssembly/wabt) - WebAssembly 二进制工具包，用于使用“wasm-strip”和“wasm-objdump”工具来减小 .wasm 文件大小。
- [binaryen](https://github.com/WebAssembly/binaryen) - WebAssembly 的编译器基础设施和工具链库，用于“wasm-opt”工具来减少 .wasm 文件大小。
- [Tauri](https://github.com/tauri-apps/tauri) - Tauri 是一个为所有主要桌面平台构建微小、速度极快的二进制文件的框架。开发人员可以集成任何可编译为 HTML、JS 和 CSS 的前端框架来构建用户界面。应用程序的后端是一个 Rust 源二进制文件，具有前端可以与之交互的 API。
- [yew-fmt](https://github.com/schvv31n/yew-fmt) - 用于格式化 Yew HTML 的“rustfmt”的可配置扩展。

## 文章

- [让我们用 Yew 构建 Rust 前端](https://dev.to/deciduously/lets-build-a-rust-frontend-with-yew---part-1-3k2o)
- [如何使用锈红豆杉](https://github.com/steadylearner/blog/tree/master/posts/Rust/How%20to%20use%20Rust%20Yew.md)
- [如何在 Rust 中使用模态](https://github.com/steadylearner/blog/tree/master/posts/Rust/How%20to%20use%20a%20modal%20in%20Rust.md)
- [如何在 Rust 前端使用路由器](https://github.com/steadylearner/blog/tree/master/posts/Rust/How%20to%20use%20routers%20in%20Rust%20Frontend.md)
- [如何模块化你的 Rust 前端](https://github.com/steadylearner/blog/tree/master/posts/Rust/How%20to%20modulize%20your%20Rust%20Frontend.md)
- [如何将 NPM 包与 Rust 前端结合使用](https://github.com/steadylearner/blog/tree/master/posts/Rust/How%20to%20use%20NPM%20packages%20with%20Rust%20Frontend.md)
- [如何在 Rust 前端中使用 Markdown](https://github.com/steadylearner/blog/blob/master/posts/Rust/How%20to%20use%20markdown%20with%20code%20snippets%20in%20Rust%20Frontend.md)
- [Fullstack Rust 与紫杉](https://github.com/steadylearner/blog/tree/master/posts/Rust/Fullstack%20Rust%20with%20Yew.md)
- [如何编写全栈 Rust 代码](https://github.com/steadylearner/blog/tree/master/posts/Rust/How%20to%20write%20Full%20Stack%20Rust%20code.md)
- [如何使用 Rust Yew fetch API 渲染 YouTube 视频博客](https://github.com/steadylearner/blog/blob/master/posts/Rust/How%20to%20render%20a%20YouTube%20vlog%20with%20%20Rust%20Yew%20fetch%20API.md)
- [如何使用 Rust Yew 安装的 API 渲染博客文章](https://github.com/steadylearner/blog/tree/master/posts/Rust/How%20to%20render%20blog%20posts%20with%20Rust%20Yew%20mounted%20API.md)
- [完全使用 Rust 编写的 Web 应用程序](https://medium.com/@saschagrunert/a-web-application-completely-in-rust-6f6bdb6c4471)
- [Yew - Rust 和 WebAse 前端框架](https://sudonull.com/post/11627-Yew-Rust-WebAsse-frontend-framework)
- [使用 Tauri 和 Yew 在 Rust 中创建桌面应用程序](https://dev.to/stevepryde/create-a-desktop-app-in-rust-using-tauri-and-yew-2bhe)
- [Yew 的代码演练视频以及 Christopher Hunt 和 Kiki Carter 的真实应用程序](https://www.youtube.com/watch?v=ilrGIJGdqRo)
- [为红豆杉添加顺风](https://mikekrisher.com/writings/yew_and_tailwind)

## 课程

- [full-stack-todo-rust-course](https://github.com/brooks-builds/full-stack-todo-rust-course) - 全栈 Rust 课程，包括红豆杉课程。

## 书籍

- [The WebAssembly Book](https://rustwasm.github.io/docs/book/) - 使用网络并生成 .wasm 文件。
- [The wasm-bindgen Guide](https://rustwasm.github.io/docs/wasm-bindgen/) - 如何绑定 Rust 和 JavaScript API。
- [The wasm-pack Guide](https://rustwasm.github.io/docs/wasm-pack/) - 如何构建和使用 Rust 生成的 WebAssembly。
- [Programming WebAssembly with Rust](https://pragprog.com/book/khrust/programming-webassembly-with-rust) - 包括关于使用 Yew 创建应用程序的“与 Yew 的高级 JavaScript 集成”一章。
- [Creative Projects for Rust Programmers](https://www.oreilly.com/library/view/creative-projects-for/9781789346220/) - 第 5 章，“使用 Yew 创建客户端 WebAssembly 应用程序”。
- [Server-Side WebAssembly](https://www.manning.com/books/server-side-webassembly) - 如何使用 WebAssembly 组件和 WebAssembly 系统接口 (WASI) 构建 Web 后端。

## 替代方案

Yew 团队喜欢与其他项目分享想法，并相信我们可以互相帮助，充分发挥这项令人兴奋的新技术的潜力。

- [Draco](https://github.com/utkarshkukreti/draco) - 用于使用 WebAssembly 构建客户端 Web 应用程序的 Rust 库。
- [Percy](https://github.com/chinedufn/percy) - 用于使用 Rust + WebAssembly 构建同构 Web 应用程序的模块化工具包。
- [Sauron](https://github.com/ivanceras/sauron) - Sauron 是一个用于构建 Web 应用程序的 HTML Web 框架。
- [Seed](https://github.com/seed-rs/seed) - 用于创建 Web 应用程序的 Rust 框架。
- [Smithy](https://github.com/rbalicki2/smithy) - 用于在 Rust 中构建 WebAssembly 应用程序的框架。
- [Dioxus](https://github.com/DioxusLabs/dioxus) - 优雅的类似 React 的库，用于构建桌面、Web、移动、SSR、实时查看等用户界面。
- [Sycamore](https://github.com/sycamore-rs/sycamore) - 用于在 Rust 和 WebAssembly 中创建 Web 应用程序的反应式库。
- [Leptos](https://github.com/leptos-rs/leptos) - 使用 Rust 构建快速的 Web 应用程序。

## 相关列表

- [Awesome Rust and WebAssembly](https://github.com/rustwasm/awesome-rust-and-webassembly) - 很棒的 Rust 和 WebAssembly 项目、库、工具和资源的列表。
- [Awesome WebAssembly](https://github.com/mbasso/awesome-wasm) - 有关 WebAssembly 生态系统的精彩内容的集合。
- [Awesome Rust](https://github.com/rust-unofficial/awesome-rust) - Rust 代码和资源的精选列表。
