# 很棒的预反应 [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

[<img src="https://rawgit.com/ooade/awesome-preact/master/preact-logo.svg"align="right" width="100">](https://preactjs.com)

> 关于 [Preact](https://github.com/developit/preact) 生态系统的令人惊叹的精彩事物的精选列表：star2：

[Preact](https://github.com/developit/preact) 是一个快速的 3kb React 替代品，具有相同的 ES6 API。组件和虚拟 DOM。

## 内容
- [Community](#community)
- [Toolkits](#toolkits)
- [Boilerplates](#boilerplates)
- [Routing](#routing)
- [Components](#components)
- [Libraries](#libraries)
- [测试工具](#testing-utils)
- [Articles](#articles)
- [示例应用程序](#example-apps)
- [真实应用程序](https://preactjs.com/about/we-are-using)
- [相关库](#related-libraries)
- [Tips](#tips)

### 社区
- [Slack](https://chat.preactjs.com/)（讨论论坛）
- [堆栈溢出](https://stackoverflow.com/questions/tagged/preact)
- [Github](https://github.com/developit/preact)
- [Twitter](https://twitter.com/preactjs)

### 工具包
- [Preact CLI](https://github.com/developit/preact-cli) - 在几秒钟内构建一个 Preact 渐进式 Web 应用程序。
- [Vite](https://github.com/vitejs/vite) - 适用于 Preact、Vue 或 React 的快速本机 ESM 支持的 Web 开发构建工具。
- [PreactPress](https://github.com/kamod-ch/preactpress) - Vite 和 Preact 支持的文档、博客和营销网站静态网站生成器 *([demo](https://kamod-ch.github.io/preactpress/))*。
- [nwb](https://github.com/insin/nwb) - 使用 React、Inferno 或 Preact 进行快速开发。
- [React App Rewire Preact](https://github.com/timarney/react-app-rewired) - 将 Preact 与 create-react-app 一起使用，无需弹出。
- [Preact CLI PostCSS](https://github.com/SaraVieira/preact-cli-postcss) - 它删除了 Preact CLI 上的默认 postcss 配置，因此您可以使用 postcss.config.js。
- [Create Preact App](https://github.com/just-boris/create-preact-app) - 创建无需构建配置的 Preact 应用程序。
- [Storybook Preact](https://github.com/storybooks/storybook/tree/next/app/preact) - Storybook for Preact 是 Preact 组件的 UI 开发环境。

### 样板文件
- [Official Boilerplate](https://github.com/developit/preact-boilerplate) - 准备就绪的 Preact 入门项目，由 Webpack 提供支持。
- [Preact Simple Starter](https://github.com/ooade/PreactSimpleStarter) - 使用 Preact、Preact-mdl 和 Webpack2 的 PWA 简单入门程序。
- [Preact Offline Starter](https://github.com/lukeed/preact-starter) - Webpack2 样板，用于使用 Preact 构建 SPA/PWA/离线前端应用程序。
- [TypeScript Preact Starter](https://github.com/nickytonline/ts-preact-starter) - 使用 TypeScript 进行 Preact 的 Barebones 入门项目。
- [TypeScript PWA Preact Starter](https://github.com/bmitchinson/preact-typescript-pwa-starter) - 使用 TypeScript 和 SASS 的 PWA 入门程序 (131kb)
- [Electron TypeScript Preact Boilerplate](https://github.com/yoctopuce-examples/electron-typescript-preact-boilerplate) - Electron 入门项目，支持 TypeScript 和 Preact，由 esbuild 提供支持。
- [Preact Modern Startupper](https://github.com/kolodziejczakM/preact-modern-startupper) - 支持 TypeScript、Goober、Unistore 和 Plop 的 PWA 样板。
- [Preact Redux SSR Example](https://github.com/csbun/preact-redux-ssr-example) - 使用 Redux 示例进行服务器端渲染。
- [Preact PWA](https://github.com/ezekielchentnik/preact-pwa) - PWA 专注于原始性能、服务器端渲染、预渲染、redux、express、rollup。
- [Preact Chrome Extension](https://github.com/debdut/preact-chrome-extension) - 全功能 Preact Chrome 扩展入门套件。
- [Preact Web Extension](https://github.com/PiyushSuthar/preact-webext) - ⚡️ WebExtension Vite 入门模板与 Preact。
- [Preact Neutralino TypeScript Starter](https://github.com/ernest-rudnicki/preact-neutralino-typescript-starter) - 使用 Preact 和 neutralino.js 构建轻量级桌面应用程序的入门项目。
- [Simple Deno Starter](https://github.com/nesterow/minizavr) - 使用 Preact 和 Deno 构建单页应用程序的小型入门模板。

### 路由
- [Preact Router](https://github.com/developit/preact-router) - Preact 的 URL 路由器。
- [Preact Route Async](https://github.com/mjanssen/preact-route-async) - 一个 (440b gzip) 路由组件，支持页面组件的异步加载。
- [Wouter](https://github.com/molefrog/wouter) - 一个用于 Preact/React 的小型 (1KB gzip) 路由器，具有类似 React Router 的 API。
- [Ufbr](https://github.com/zakarialaoui10/ufbr) - 一个小型客户端基于文件的通用路由器，支持“Preact”。

### 组件
- [Preact Material Components](https://github.com/prateekbh/preact-material-components) - “Web 材料组件”的 Preact 包装器。
- [Preact Scroll Header](https://github.com/lukeed/preact-scroll-header) - 滚动 Preact 时将显示/隐藏的 (800b gzip) 标头。
- [Preact Progress](https://github.com/lukeed/preact-progress) - Preact 的简单轻量级（~590 字节 gzip）进度条组件。
- [Preact Compat](https://github.com/preactjs/preact-compat) - 将任何 React 库与 Preact *([完整示例](https://github.com/developit/preact-compat-example))* 结合使用。
- [Preact Render To String](https://github.com/preactjs/preact-render-to-string) - 通用渲染。
- [Preact Markup](https://github.com/developit/preact-markup) - 将 HTML 和自定义元素渲染为 JSX 和组件。
- [Preact Portal](https://github.com/developit/preact-portal) - 将 Preact 组件渲染到 (a) 空间中。
- [Preact Richtextarea](https://github.com/developit/preact-richtextarea) - 简单的 HTML 编辑器组件。
- [Preact Token Input](https://github.com/developit/preact-token-input) - 用于标记输入的文本字段，例如标签之类的内容。
- [Preact Virtual List](https://github.com/developit/preact-virtual-list) - 轻松渲染包含数百万行的列表（[演示](https://jsfiddle.net/developit/qqan9pdo/)）。
- [Preact Cycle](https://github.com/developit/preact-cycle) - Preact 的功能反应式范例。
- [Preact Layout](https://download.github.io/preact-layout/) - 小而简单的布局库。
- [Preact Socrates](https://github.com/matthewmueller/preact-socrates) - [Socrates](http://github.com/matthewmueller/socrates) 的 Preact 插件。
- [Preact Flyd](https://github.com/xialvjun/preact-flyd) - 在 Preact + JSX 中使用 [flyd](https://github.com/paldepind/flyd) FRP 流。
- [Preact I18nline](https://github.com/download/preact-i18nline) - 通过 [i18nline](https://github.com/download/i18nline) 将 [i18n-js](https://github.com/everydayhero/i18n-js) 周围的生态系统与 Preact 集成。
- [Preact MUI](https://github.com/luisvinicius167/preact-mui) - MUI CSS Preact 库。
- [Preact MDL](https://github.com/developit/preact-mdl) - 使用 [MDL](https://getmdl.io) 作为 Preact 组件。
- [Preact Photon](https://github.com/developit/preact-photon) - 使用 [photon](http://photonkit.com) 构建漂亮的桌面 UI。
- [Preact Classless Component](https://github.com/ld0rman/preact-classless-component) - 创建不带 class 关键字的 preact 组件。
- [Preact Hyperscript](https://github.com/queckezz/preact-hyperscript) - 用于创建元素的类似超脚本的语法。
- [Shallow Compare](https://github.com/tkh44/shallow-compare) - 简化的“shouldComponentUpdate”帮助器。
- [Preact Codemod](https://github.com/vutran/preact-codemod) - 将 React 代码转换为 Preact。
- [Preact Helmet](https://github.com/download/preact-helmet) - Preact 的文档主管经理。
- [Preact Delegate](https://github.com/NekR/preact-delegate) - 委托 DOM 事件。
- [Preact No SSR](https://github.com/gufsky/preact-no-ssr) - 跳过组件的服务器端渲染。
- [Preact Head](https://github.com/matthewmueller/preact-head) - Preact 的独立声明式 \<Head />。
- [Preact Side Effect](https://github.com/ooade/preact-side-effect) - 创建其嵌套 prop 更改映射到全局副作用的组件。
- [Preact Tiny Atom](https://github.com/KwanMan/preact-tiny-atom) - 与 [Tiny Atom](https://github.com/qubitproducts/tiny-atom) 进行 Preact 集成。
- [Preact Level List](https://github.com/juliangruber/preact-level-list) - Preact 的实时更新 leveldb 列表组件。
- [Preact Country Picker](https://github.com/bboydflo/flagstrap-preact) - 基于 Bootstrap 3 的国家/地区选择器，专为 Preact 制作。
- [Preact Fluid](https://github.com/ajainvivek/preact-fluid) - Preact 的最小 UI 套件。
- [Preact Feather Icons](https://github.com/ForsakenHarmony/preact-feather) - Preact 的羽毛图标。
- [Preact Animate On Change](https://github.com/Sobesednik/preact-animate-on-change) - 属性更改时添加 CSS3 动画。
- [Preact Async Route](https://github.com/prateekbh/preact-async-route) - preact-router 的异步路由组件。
- [MU Forms](https://github.com/mobiushorizons/mu-forms) - (P)React 的简单表单库。
- [Pimg](https://github.com/ooade/pimg) - 渐进式图像组件；用于延迟加载图像。
- [Preact Component Console](https://github.com/haensl/preact-component-console) - 控制台模拟器。通过动态延迟模拟打字。
- [Preact Translate](https://github.com/DenysVuika/preact-translate) - Preact 的简约翻译 (i18n) 库。
- [Preact Dock](https://github.com/TimDaub/preact-touchable-dock) - 适用于 Preact 应用程序的简单 DnD 和支持触摸的 Dock。
- [Preact Particles](https://github.com/matteobruni/tsparticles#preact) - 轻量级组件，可轻松向网站添加炫酷的粒子动画。
- [Pant](https://github.com/webyom/pant) - 基于 Preact 构建的移动 UI 组件 *([文档和演示](https://webyom.github.io/pant))*。移植自 [Vant](https://github.com/youzan/vant) 的出色 Vue 组件。
- [Preact Transitioning](https://github.com/fakundo/preact-transitioning) - 公开 Preact 组件以轻松实现基本 CSS 动画和过渡。
- [Preact Nominal Allocator](https://github.com/TimDaub/preact-nominal-allocator) - 也可以通过两个按钮 (-/+) 进行操作的数字输入元素。
- [Tailored Components](https://github.com/nesterow/tailored) - Preact 和 Deno 的无样式组件和挂钩。
- [Plotery](https://shelacek.bitbucket.io/plotery) - 快速且轻量级的图表库。
- [Formica](https://shelacek.bitbucket.io/formica) - Preact 的简单声明形式。
- [HelloCSV](https://hellocsv.github.io/HelloCSV/) - 现代、优雅、嵌入式 CSV 导入器，内置于 Preact 中。平面文件替代方案。
- [Vski Table](https://table.vski.ai) - 使用 Preact 构建的 Datagrid 组件。
- [Kamod UI](https://github.com/kamod-ch/kamod-ui) - 轻量级 Preact 和 Tailwind UI 组件（shadcn 风格的方法）*([demo](https://kamod-ch.github.io/kamod-ui/))*。
- [Preact Filter Builder](https://github.com/dimidd/preact-filter-builder) - 一个可重用的基于 Preact 的过滤器构建器 UI 组件，带有 AND/OR 布尔连接器 *([demo](https://cute-empanada-425012.netlify.app/))*。

### 图书馆
- [Redux Zero](https://github.com/concretesolutions/redux-zero) - 基于 Redux 的轻量级状态容器，具有单个存储且无减速器。
- [Unistore](https://github.com/developit/unistore) - 350b / 650b 状态容器，包含 Preact 和 React 的组件操作。
- [FPreact](https://github.com/UnwrittenFun/fpreact) - 提供了一个用于创建 preact 组件的替代 api，很大程度上受到 elm 的启发。
- [ProppyJS - 一个用于功能性道具组合的小型库](https://proppyjs.com)
- [ClearX](https://github.com/Autodesk/clearx) - React、Preact 和 Inferno 的快速、轻松的状态管理，学习曲线为零。
- [Preact-urql](https://github.com/FormidableLabs/urql/tree/master/packages/preact-urql) - 将 [urql](https://github.com/FormidableLabs/urql) 与 Preact core + hooks 结合使用。
- [hooked-head](https://github.com/JoviDeCroock/hooked-head) - 用于操作 DOM 的 `<head>` 部分的钩子。它有一个带有核心 preact 支持的子包（使用 `preact/hooks`）。
- [Kamod Hooks](https://github.com/kamod-ch/kamod-hooks) - Preact hooks 库移植自 [ahooks](https://github.com/alibaba/hooks)。
- [Teaful](https://github.com/teafuljs/teaful) - 小巧（800B）、简单而强大的（P）React 状态管理。
- [Nano Stores](https://github.com/nanostores/nanostores) - 一个小型（199 字节）状态管理器，具有许多原子树可抖动存储。
- [Modular Forms](https://github.com/fabian-hiller/modular-forms) - Preact 的模块化、类型安全和基于信号的表单库。
- [exome](https://github.com/Marcisbee/exome) - 用于深度嵌套状态的基于简单代理的状态管理器。
- [Fastro](https://fastro.deno.dev) - 适用于 Deno、TypeScript、Preact 和 Tailwind 的快速模块化 SSR Web 框架。
- [Jotai](https://github.com/pmndrs/jotai) - React 和 Preact 的原始而灵活的状态管理。
- [Pretch](https://github.com/EGAMAGZ/pretch) - 一个轻量级且灵活的获取增强库，可与普通 JavaScript、React 和 Preact 配合使用
- [Formisch](https://formisch.dev/preact/guides/introduction/) - Preact 的表单库，重点关注性能、类型安全和包大小。
- [zikofy](https://github.com/zakarialaoui10/zikofy) - 将 Preact 组件转换为 Zikojs `UIElement`。
- [Preact In Motion](https://github.com/alloc/preact-in-motion) - Preact 的轻量、优雅的动画插件（由 Motion.dev 和 WAAPI 提供支持）。

### 测试工具
- [Preact JSX Chai](https://github.com/developit/preact-jsx-chai) - JSX 断言测试_（无 DOM，就在 Node 中）_。
- [Preact Render Spy](https://github.com/mzgoddard/preact-render-spy) - 渲染 Preact 组件，可以访问生成的虚拟 dom 进行测试。
- [Preact Test Utils](https://github.com/windyGex/preact-test-utils) - preact 中的模拟 react-test-utils 酶。
- [Preact Testing Library](https://github.com/antoaravinth/preact-testing-library) - 简单而完整的 Preact DOM 测试实用程序鼓励良好的测试实践。
- [Preact Island](https://github.com/mwood23/preact-island) - 轻松将您的 Preact 组件呈现为任何网页上的小部件。

### 文章
- [WTF 是 JSX](https://jasonformat.com/wtf-is-jsx/)
- [虚拟 DOM 的内部工作原理](https://medium.com/@rajaraodv/the-inner-workings-of-virtual-dom-666ee7ad47cf)
- [使用 Preact 代替 React](https://medium.com/@rajaraodv/using-preact-instead-of-react-70f40f53107c)
- [Preact 内部结构 #1：简单的零件](https://medium.com/@asolove/preact-internals-1-the-easy-parts-3a081fa36205#.twnc3doig)
- [Preact 内部结构 #2：组件模型](https://medium.com/@asolove/preact-internals-2-the-component-model-36a05e32957b#.8zyec2y9v)
- [使用 Preact 和 Firebase 构建小型 PWA](https://dandenney.com/posts/front-end-dev/building-a-small-pwa-with-preact-and-firebase)
- [使用 Auth0 进行身份验证](https://auth0.com/blog/preact-authentication-tutorial)

### 示例应用程序
- [Preact HN](https://github.com/kristoferbaxter/preact-hn) - 用于将 Hacker News 构建为 PWA 的 Preact 演示。
- [TodoMVC](https://github.com/developit/preact-todomvc) - TodoMVC 在 Preact 中完成。不到 6kb 并且速度很快。
- [Colors App](https://github.com/lukeed/colors-app) - 用于从流行调色板复制值的 PWA。支持 HEX、RGB 和 HSL 格式。
- [Tracks](https://github.com/jordic/tracks_preact/) - PWA 用于一般跟踪事物。 Gdrive 同步。
- [Hueify](https://github.com/kvartborg/hueify) - 适用于您的飞利浦 Hue 灯的简单控制器。
- [Golazon](https://github.com/sobstel/golazon) - 足球数据mnmlist方式。
- [Shopping List](https://github.com/ibm-watson-data-lab/shopping-list-preact-pouchdb) - 使用 Preact 和 PouchDB 构建的渐进式 Web 应用程序。
- [Code and Comment](https://github.com/code-and-comment/code-and-comment) - 用于将注释添加到 Github 中的文件的应用程序（[演示](https://code-and-comment.github.io/code-and-comment/)）。
- [Play.cash](https://play.cash) :注释: _([GitHub 项目](https://github.com/feross/play.cash))_
- [Songsterr](https://www.songsterr.com) 🎼 自 10.0 alpha 起在生产中使用 Preact X
- [BitMidi](https://bitmidi.com/) 🎹 免费 MIDI 文件的 Wayback 机器 _([GitHub 项目](https://github.com/feross/bitmidi.com))_
- [Ultimate Guitar](https://www.ultimate-guitar.com) 🎸Preact 提高了速度。
- [ESBench](http://esbench.com) 使用 Preact 构建。
- [BigWebQuiz](https://bigwebquiz.com) _([GitHub 项目](https://github.com/jakearchibald/big-web-quiz))_
- [Nectarine.rocks](http://nectarine.rocks) _([GitHub 项目](https://github.com/developit/nectarine))_ :peach:
- [OSS.Ninja](https://oss.ninja)_([GitHub 项目](https://github.com/developit/oss.ninja))_
- [GuriVR](https://gurivr.com) _([GitHub 项目](https://github.com/opennewslabs/guri-vr))_
- [离线图库](https://use-the-platform.com/offline-gallery/) _([GitHub 项目](https://github.com/vaneenige/offline-gallery/))_ :balloon:
- [周期性天气](https://use-the-platform.com/periodic-weather/) _([GitHub 项目](https://github.com/vaneenige/periodic-weather/))_ :sunny:
- [橄榄球新闻板](http://nbrugby.com)_[(GitHub 项目)](https://github.com/rugby-board/rugby-board-node)_
- [Preact Gallery](https://preact.gallery/) 一个使用 Preact 构建的 8KB 照片库 PWA。
- [Rainbow Explorer](https://use-the-platform.com/rainbow-explorer/) Preact 应用程序将现实生活中的颜色转换为数字颜色_([Github 项目](https://github.com/vaneenige/rainbow-explorer))_。
- [YASCC](https://carlosqsilva.github.io/YASCC/#/) 另一个 SoundCloud 客户端 _([Github 项目](https://github.com/carlosqsilva/YASCC))_。
- [Journalize](https://preact-journal.herokuapp.com/) 使用 preact 的 14k 离线日志 PWA。 _([Github 项目](https://github.com/jpodwys/preact-journal))_。
- [Proxx](https://proxx.app) GoogleChromeLabs 使用 preact 开发的接近游戏。 _([Github 项目](https://github.com/GoogleChromeLabs/proxx))_。
- [Web Maker](https://webmaker.app) 使用 Preact 构建的离线且快速的前端游乐场。 _([Github 项目](https://github.com/chinchang/web-maker))_。
- [Intergram](https://www.intergram.xyz) 一个链接到使用 Preact 构建的 Telegram Messenger 的实时聊天小部件。 _([Github 项目](https://github.com/idoco/intergram))_。
- [ES6 中的 Preact 应用程序，无需 Babel 或 JSX](https://vanilla-preact.surge.sh) _([GitHub 项目](https://github.com/safdarjamal/vanilla-preact/))_。
- [GHFresh](https://code2k.github.io/ghfresh/) 监控 GitHub 存储库版本 – 使用 Preact 进行预渲染。使用 Preact Compat、TypeScript、Material-UI 和 Redux Toolkit 构建。 _([GitHub 项目](https://github.com/code2k/ghfresh))_。
- [Passwords Fountain](https://passwords-fountain.com/) - 现代且高性能的密码管理器界面，可在任何地方使用_([Github项目](https://github.com/kolodziejczakM/passwords-fountain))_。
- [macOS Web](https://macos-preact.now.sh) - macOS Big Sur Web 桌面体验，使用 Preact 和 Vite 构建_([Github 项目](https://github.com/PuruVJ/macos-preact))_。
- [Cinemate](https://cinemate.me) - 使用 Preact 和 TypeScript 构建的电影推荐系统。用 Rust 编写的后端。
- [Windows 11 Web](https://win11.vercel.app) - 令人惊叹的 Windows 11 网络克隆！ ⚡ _([Github 项目](https://github.com/PiyushSuthar/Windows-11-Web))_。
- [Idea Keeper](https://miftikcz.github.io/idea-keeper-2) :brain: 高度可扩展且简约的创意保存应用程序 _([GitHub 项目](https://github.com/MiftikCZ/idea-keeper-2))_。
- [Trellith](https://trellith.sakih.net/) - 微型 Trello 克隆 PWA（[GitHub 项目](https://github.com/sakihet/trellith)）。
- [Gladys Assistant](https://gladysassistant.com/) - 隐私第一的开源家庭助理 _([GitHub 项目](https://github.com/GladysAssistant/Gladys))_。

### 相关库
- [React](https://github.com/facebook/react) - 用于构建用户界面的声明式、高效且灵活的 JavaScript 库。
- [Inferno](https://github.com/infernojs/inferno) - 一个极其快速、类似 React 的 JavaScript 库，用于构建现代用户界面。
- [Rax](https://github.com/alibaba/rax) - 通用的 React 兼容渲染引擎。
- [Zikojs](https://github.com/zakarialaoui10/zikojs) - 一个可组合的基于超脚本的 UI 库，具有与 Preact 组件的双向互操作性。

### 温馨提示
贡献一些；）

---
### 贡献
随时欢迎您的贡献和建议。使用 Preact 构建出色的东西，与我们分享;) <br/>
确保遵循[指南](/contributing.md)。谢谢你！

---
### 执照
[![CC0](http://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](http://creativecommons.org/publicdomain/zero/1.0/)
