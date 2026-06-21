<p align="center">
  <br>
  <img width="200" src="./awesome-svelte.svg" alt="awesome-svelte logo">
  <br>
  <br>
</p>

# 很棒的苗条 [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

> ⚡ 精彩 Svelte 资源精选列表

[Svelte](https://svelte.dev/) 是一种构建 Web 应用程序的新方法。它是一个编译器，可以获取声明性组件并将它们转换为高效的 JavaScript

欢迎贡献。通过拉取请求添加链接或创建问题以开始讨论。

## 内容

- [很棒的苗条](#awesome-svelte-)
  - [Contents](#contents)
  - [Resources](#resources)
    - [官方资源](#official-resources)
    - [Community](#community)
    - [Conferences](#conferences)
    - [Podcasts](#podcasts)
    - [YouTube 频道](#youtube-channels)
    - [Tutorials](#tutorials)
    - [Studies](#studies)
  - [Integrations](#integrations)
    - [Preprocessing](#preprocessing)
    - [Mobile](#mobile)
  - [州立图书馆](#state-libraries)
  - [用户界面库](#ui-libraries)
  - [用户界面组件](#ui-components)
    - [Table](#table)
    - [Notification](#notification)
    - [Grid](#grid)
    - [Icons](#icons)
    - [Calendar](#calendar)
    - [Maps](#maps)
    - [Charts](#charts)
    - [Miscellaneous](#miscellaneous)
  - [Scaffold](#scaffold)
  - [Utilities](#utilities)
    - [Animations](#animations)
    - [拖放](#drag--drop)
    - [Forms](#forms)
      - [表单组件](#form-components)
    - [HTTP 请求](#http-requests)
    - [声音\&视频](#sound--video)
    - [WebGL](#webgl)
    - [PWA](#pwa)
    - [Portal](#portal)
    - [Fonts](#fonts)
    - [Internationalization](#internationalization)
  - [Routers](#routers)
  - [Frameworks](#frameworks)
  - [开发工具](#dev-tools)
    - [Lint](#lint)
    - [Test](#test)
    - [Editors](#editors)
      - [视觉工作室代码](#visual-studio-code)
      - [崇高的文字](#sublime-text)
      - [Vim](#vim)
      - [JetBrains](#jetbrains)
  - [应用实例](#application-examples)
    - [Desktop](#desktop)

## 资源

### 官方资源

- [官方指南](https://svelte.dev/tutorial)
- [API参考](https://svelte.dev/docs)
- [GitHub 存储库](https://github.com/sveltejs/svelte)
- [Changelog](https://github.com/sveltejs/svelte/blob/master/packages/svelte/CHANGELOG.md)

### 社区

- ~~[Twitter](https://twitter.com/sveltejs)~~
- [Bluesky](https://bsky.app/profile/svelte.dev)
- [Discord](https://svelte.dev/chat)
- [Reddit](https://www.reddit.com/r/sveltejs/)
- [Japan Discord](https://discord.com/invite/YTXq3ZtBbx) - Svelte 日本.

### 会议

- [苗条峰会](https://sveltesummit.com/)

### 播客

- [苗条电台](https://www.svelteradio.com/)

### YouTube 频道

- [苗条社会](https://www.youtube.com/channel/UCZSr5B0l07JXK2FIeWA0-jw)
- [精巧掌握](https://www.youtube.com/channel/UCg6SQd5jnWo5Y70rZD9SQFA)
- [代码的乐趣](https://www.youtube.com/@JoyofCodeDev)

### 教程

- [Getting Started with Svelte 5: A Guide for React Developers](https://www.edistys.dev/blog/getting-started-with-svelte-5-a-guide-for-react-developers) - 埃迪斯蒂斯
- [Svelte 5 Basics - Complete Svelte 5 Course for Beginners](https://www.youtube.com/watch?v=8DQailPy3q8) - 语法 (YouTube)
- [TutorialSearch](https://tutorialsearch.io/?q=svelte) - 免费的跨平台搜索引擎，对来自 Udemy、Skillshare、Pluralsight 和其他主要学习平台的 45 多个类别的 50,000 多个教程进行索引。

### 研究

_Svelte框架的学习和研究._

- [SvelteScaling](https://svelte-scaling.acmion.com/) - Svelte 可以扩展吗？ _（v5 之前）_
- [Will it Scale?](https://github.com/halfnelson/svelte-it-will-scale) - 寻找 Svelte 的拐点。 _（v5 之前）_

## 集成

### 预处理

- [svelte-preprocess](https://github.com/sveltejs/svelte-preprocess) - PostCSS、SCSS、Less、Stylus、Coffeescript、TypeScript、Pug 等的预处理器。
- [MDSveX](https://github.com/pngwn/MDsveX) - MDX markdown 的预处理器。
- [svelte-switch-case](https://github.com/l-portet/svelte-switch-case) - Svelte 的切换大小写语法。
- [svelte-preprocess-less](https://github.com/ls-age/svelte-preprocess-less) - 预处理器的成本更低。
- [modular-css](https://github.com/tivac/modular-css/tree/main/packages/svelte) - 对模块化 CSS 的预处理器支持。
- [svelte-preprocess-sass](https://github.com/ls-age/svelte-preprocess-sass) - sass 的预处理器。
- [svelte-preprocess-markdown](https://github.com/AlexxNB/svelte-preprocess-markdown) - 使用 Markdown 语法编写 Svelte 组件。
- [@nvl/sveltex](https://github.com/nvlang/sveltex) - Svelte + Markdown + LaTeX。

### 手机

_移动用户界面框架._

- [Svelte Native](https://svelte-native.technology/) - Svelte 通过 Nativescript 控制本机组件。
- [Framework7](https://framework7.io/svelte/) - 用于构建 iOS 和 Android 应用程序的全功能 HTML 框架。
- [Capacitor](https://capacitorjs.com/solution/svelte) - 使用 Web 技术和 Svelte 构建本机移动应用程序。

## 州立图书馆

- [svelte-asyncable](https://github.com/sveltetools/svelte-asyncable) - 支持异步值的 Svelte 存储合约。
- [exome](https://github.com/Marcisbee/exome) - 用于深度嵌套状态的基于简单代理的状态管理器。
- [tanstack-store](https://tanstack.com/store/latest/docs/framework/svelte/quick-start) - 具有反应式框架适配器的与框架无关的类型安全存储。
-

## 用户界面库

- [lomer-ui](https://ui.lomer.dev) - 一个非常简单的 CLI 工具，可以立即启动您的组件。
- [shadcn-svelte](https://www.shadcn-svelte.com/) - 设计精美的组件，您可以将其复制并粘贴到您的应用程序中。
- [SvelteUI](https://svelteui.dev/) - 全包 Svelte 库 - 组件、动作、实用程序、动画。
- [Flowbite Svelte](https://flowbite-svelte.com/) - 使用 Tailwind CSS 和 Flowbite 构建的开源 Svelte UI 组件。
- [Skeleton](https://www.skeleton.dev/docs/get-started) - Skeleton 使用 Tailwind 实用程序类和设计系统轻松创建可主题的用户界面。
- [Sveltestrap](https://github.com/sveltestrap/sveltestrap) - Bootstrap 4 和 5 组件。
- [carbon-components-svelte](https://github.com/IBM/carbon-components-svelte) - IBM Carbon Design System 的精简实现。
- [Svelte Material UI](https://github.com/hperrin/svelte-material-ui) - 材质 UI 组件。
- [Melt UI](https://github.com/melt-ui/melt-ui) - 可访问、可重用且可组合的无头组件构建器和实用程序的集合。
- [attractions](https://github.com/illright/attractions) - 一个非常酷且现代的 UI 套件。 _（v5 之前）_
- [ionic-svelte](https://github.com/Tommertom/svelte-ionic-app) - 与 Ionic 的 UI 集成，用于移动应用程序开发，包括许多初学者。
- [YeSvelte](https://www.yesvelte.com/) - YeSvelte 是构建在 Bootstrap css 之上的灵活的 Svelte UI 组件库。
- [Svelte UX](https://github.com/techniq/svelte-ux) - 大量组件、操作、存储和实用程序的集合，用于构建高度交互的应用程序
- [STDF](https://stdf.design) - 基于Svelte和Tailwind的移动Web组件库。
- [M3 Svelte](https://github.com/KTibow/m3-svelte) - 实现 Material Design 3 的强大组件库
- [AgnosUI](https://amadeusitgroup.github.io/AgnosUI/latest/) - 高度可配置的无头框架无关组件库
- [daisyUI](https://daisyui.com/) - Tailwind CSS 最受欢迎的组件库 - `daisyUI` 将组件类名称添加到 Tailwind CSS，以便您可以比以往更快地制作漂亮的网站。
- [Smelte](https://github.com/matyunya/smelte) - UI 框架，包含使用 Tailwind CSS 构建的材质组件。 _（v5 之前）_
- [SVAR Core for Svelte](https://github.com/svar-widgets/core) - 20 多个 Svelte UI 组件的集合，用于构建快速执行、交互式和响应式的 Web 应用程序。
- [AgnosticUI](https://github.com/agnosticui/agnosticui) - 可访问的 Svelte 组件原语（也适用于 React、Vue 3 和 Angular）。
- [Svelte Animations](https://animation-svelte.vercel.app) - 包含 Svelte Magic UI、Svelte Aceternity UI、Svelte Luxe 组件超过 200 个免费动画组件和 2 个模板
- [Svelte Marketing Blocks](https://sv-blocks.vercel.app) - 一个强大的库，包含 100 多个营销和 UI 块，使用 Shadcn Svelte、Tailwind CSS v4 和 Svelte 5 构建。
- [Quaff](https://quaff.dev) - 一个广泛的 UI 框架，具有遵循 Material Design 3 原则的现代而优雅的组件。
- [retroui-svelte](https://retroui-svelte.netlify.app) - 一个复古风格的 Svelte 组件库，构建在 shadcn-svelte 之上，提供 40 多个可定制的 UI 组件，打造时髦有趣的界面。
- [svelte-audio-ui](https://svelte-audio-ui.vercel.app) - 一组可访问且可组合的音频 UI 组件。它建立在 shadcn-svelte 之上，受到 audio-ui 的启发，专为您复制、粘贴和拥有而设计。
- [AgentsKit](https://github.com/AgentsKit-io/agentskit) - 无头聊天和代理组件以及用于在 Svelte 中构建 AI 应用程序的商店，具有支持流、工具、内存和 RAG 的框架无关核心。

## 用户界面组件

### 表

_表格和数据网格._

- [@vincjo/datatables](https://github.com/vincjo/datatables) - 用于使用 Svelte 创建数据表组件的工具包。
- [svelte-table](https://github.com/dasDaniel/svelte-table) - 允许排序和过滤的表实现。
- [svelte-generic-crud-table](https://github.com/ivosdc/svelte-generic-crud-table) - 具有 CRUD 功能的对象数组的不可知 Web 组件。对列进行排序和调整大小。每页多个表格。
- [svelte-generic-table-pager](https://github.com/ivosdc/svelte-generic-table-pager) - 带分页器的 Svelte-generic-crud-table。
- [powertable](https://github.com/muonw/powertable) - PowerTable 是一个 JavaScript 组件，可将 JSON 数据转换为交互式 HTML 表格。这有利于数据的手动检查、排序、过滤、搜索和编辑。
- [svelte-pivottable](https://github.com/jjagielka/svelte-pivottable) - 基于 Svelte 的数据透视表库，具有拖放功能。
- [SVAR DataGrid](https://github.com/svar-widgets/grid) - 一个 Svelte 数据网格，具有单元格内编辑、排序、上下文菜单、可折叠和冻结列、树数据视图、分页和虚拟滚动。
- [svelte-datagrid](https://github.com/revolist/svelte-datagrid) - 基于 [revogrid](https://rv-grid.com) 的强大数据网格库，具有 Excel 的最佳功能。
- [@wjfe/dataview](https://github.com/WJSoftware/wjfe-dataview) - 用于数据可视化目的的表，具有列固定等高级功能，并且是世界上唯一可以针对主子场景进行跨表列位置同步的组件。

### 通知

_Toaster / Snackbar - 使用无模式临时小弹出窗口通知用户。_

- [svelte-notifications](https://github.com/beyonk-adventures/svelte-notifications) - 可在任何 JS 应用程序中使用的 Toast 通知组件。
- [svelte-favicon-badge](https://github.com/kevmodrome/svelte-favicon-badge) - 一个自定义组件，添加一个图标和一个徽章，您可以使用它们来显示未读消息的数量等。
- [@zerodevx/svelte-toast](https://github.com/zerodevx/svelte-toast) - 简单优雅的吐司通知。
- [svelte-french-toast](https://github.com/kbrgl/svelte-french-toast) - Svelte 的黄油般光滑的吐司通知，灵感来自 React Hot Toast。默认情况下轻量、可定制且美观。
- [svelte-sonner](https://github.com/wobsoriano/svelte-sonner) - Svelte 的固执己见的 Toast 组件。

### 网格

- [svelte-grid-responsive](https://github.com/andrelmlins/svelte-grid-responsive) - 受 Bootstrap 启发的响应式网格系统。
- [svelte-flex](https://github.com/himynameisdave/svelte-flex) - 一个简单且可重用的 Svelte Flexbox 组件。

### 图标

- [unplugin-icons](https://github.com/unplugin/unplugin-icons) - 普遍按需访问数千个图标作为组件。
- [svelte-fa](https://github.com/Cweili/svelte-fa) - Tiny FontAwesome 5 和 6 组件。
- [svelte-awesome](https://github.com/RobBrazier/svelte-awesome) - Awesome SVG 图标组件，使用 Font Awesome 图标构建。
- [steeze-ui/icons](https://github.com/steeze-ui/icons) - 适用于 Svelte、React、Vue 等的轻松图标包和组件。
- [svelte-icons](https://github.com/AnxiousDarkly/svelte-icons) - 图标组件。
- [svelte-heroicons](https://github.com/krowten/svelte-heroicons) - 图标，由 Tailwind CSS 的创建者精心制作。
- [svelte-icomoon](https://github.com/aykutkardas/svelte-icomoon) - 它使得在 Svelte 项目中使用 SVG 图标变得非常简单。
- [svelte-unicons](https://github.com/devShamim/svelte-unicons) - Svelte 的 Unicons svg 图标基于 @iconscout/unicons。
- [@thesvg/svelte](https://github.com/glincker/thesvg) - Svelte 的 5,600 多个 SVG 品牌和云图标组件。 AWS、Azure、GCP 和 4,000 多个品牌徽标。
- [lucide-svelte](https://github.com/lucide-icons/lucide) - 为简洁的应用程序实现 lucide 图标库。
- [svelte-icons-pack](https://github.com/leshak/svelte-icons-pack) - 基于<https://github.com/react-icons/react-icons>。
- [svesome](https://github.com/pouchlabs/svesome) - 一个很棒的 v6 图标包装器，非常简洁。
- [hugeicons](https://github.com/hugeicons/svelte) - 漂亮的、可用于生产的 Svelte 图标包，具有完整的图标覆盖范围。
- [moving icons](https://github.com/jis3r/icons) - 一系列制作精美的动画 Lucide 图标。

### 日历

_在日历中显示不可编辑的事件。_

- [svelte-fullcalendar](https://github.com/YogliB/svelte-fullcalendar) - FullCalendar 的组件包装器。
- [svelte-calendar](https://github.com/6eDesign/svelte-calendar) - 一个轻量级的日期选择器，具有简洁的动画和独特的用户体验。
- [date-picker-svelte](https://github.com/probablykasper/date-picker-svelte) - 具有简洁用户体验的 Svelte 日期和时间选择器。
- [@schedule-x/svelte](https://github.com/schedule-x/schedule-x) - 材料设计事件日历库。

### 地图

- [svelte-googlemaps](https://github.com/beyonk-adventures/svelte-googlemaps) - 谷歌地图组件。
- [svelte-mapbox](https://github.com/beyonk-adventures/svelte-mapbox) - MapBox 地图和自动完成组件。
- [leaflet-svelte](https://github.com/anoram/leaflet-svelte) - 传单的细长包装。
- [esri-svelte](https://github.com/gavinr-maps/esri-svelte-example) - Web 应用程序展示了如何将 ArcGIS API for JavaScript 与 Svelte 结合使用。
- [svelte-maplibre](https://github.com/dimfeld/svelte-maplibre) - MapLibre 映射库的 Svelte 绑定。

### 图表

- [svelte-frappe-charts](https://github.com/himynameisdave/svelte-frappe-charts) - 用于冰沙图表的 Svelte 绑定。
- [Layer Cake](https://github.com/mhkeller/layercake) - 一个用于大多数可重用图形的框架，具有 svelte
- [LayerChart](https://github.com/techniq/layerchart) - 大量可组合的 Svelte 组件，用于构建广泛的可视化效果，基于 Layer Cake 构建
- [SVAR Gantt Chart](https://github.com/svar-widgets/gantt) - 用 Svelte 编写的交互式、可定制的甘特图组件

### 图表

- [svelte-flow](https://svelteflow.dev) - 一个可定制的 Svelte 组件，用于由 React Flow 的创建者构建基于节点的编辑器和交互式图表

### 杂项

- [number-flow](https://github.com/barvian/number-flow) - 用于转换、格式化和本地化数字的组件。
- [Svelte Tweakpane UI](https://kitschpatrol.com/svelte-tweakpane-ui) - [Tweakpane](https://tweakpane.github.io/docs/) 中的 UI 元素封装在惯用的 Svelte 组件集合中。
- [svelte-tree-viewer](https://github.com/kpulkit29/svelte-tree-viewer) - 用于渲染树视图的轻量级组件。
- [svelte-copyright](https://github.com/himynameisdave/svelte-copyright) - 用于格式化和显示版权声明的 Svelte 组件。
- [svelte-splitpanes](https://github.com/orefalo/svelte-splitpanes) - 全功能的可调整大小的视图面板。
- [mathjax-svelte](https://github.com/WoolDoughnut310/mathjax-svelte) - MathJax 的 Svelte 组件。
- [svelte-stepper](https://github.com/efstajas/svelte-stepper) - 用于构建动画步骤流的 Svelte 组件。
- [css-3d-progress](https://github.com/rofixro/css-3d-progress) - 3D 进度条组件
- [svelte-speedometer](https://github.com/palerdot/svelte-speedometer) - 使用 d3 显示速度计（如仪表）的 Svelte 组件。
- [embedz](https://github.com/embedz/embedz) - Svelte 和 Vue 的简单、无依赖性嵌入。
- [EmbedPDF](https://www.embedpdf.com/docs/svelte/introduction) - 专为 Svelte 构建的模块化高性能 PDF 查看器和编辑器，由 PDFium 提供支持。可通过注释、编辑、缩略图等插件完全扩展。
- [Edra](https://edra.tsuzat.com) - 最佳富文本编辑器，使用 Tiptap 为 Svelte 开发人员打造。
- [svelte-streamdown](https://github.com/beynar/svelte-streamdown) - [streamdown](https://streamdown.ai/) 端口。一款针对流媒体进行优化的一体化 Markdown 渲染器，具有内置样式、数学、美人鱼、代码突出显示支持等。
- [svelte-bash](https://github.com/YusufCeng1z/svelte-bash) - Svelte 5 的可定制终端样式组件。

## 脚手架

_模板/样板文件/入门套件/堆栈集合/Yeoman 生成器。_

- [create-vite](https://github.com/vitejs/vite/tree/main/packages/create-vite#readme) - 为 vite + svelte 应用程序生成脚手架。
- [create-svelte](https://github.com/sveltejs/kit/tree/master/packages/create-svelte#readme) - 用于创建新 SvelteKit 项目的 CLI。
- [saasstarter](https://github.com/CriticalMoments/CMSaasStarter) - 开源、快速且免费托管 Svelte SaaS 模板。
- [svelte-pwa-template](https://github.com/tretapey/svelte-pwa) - 基于官方模板的 PWA 入门模板。 _（v5 之前）_
- [vite-svelte-docker-template](https://github.com/bavragor/vite-svelte-docker-template) - Svelte + Docker + Vite + Vitest 的模板。
- [svelte-docs-starter](https://github.com/code-gio/svelte-docs-starter) - 使用 Svelte 5、MDSvex 和 Tailwind CSS 构建的现代文档模板。
- [template-svelte](https://github.com/phaserjs/template-svelte) - Phaser 的官方快速入门模板。
- [generic-app-template](https://github.com/GantonL/templates/tree/main/sveltekit-shadcn-v5) - 使用 SvelteKit + shadcn-svelte 构建的开源现代全栈 Web 应用程序模板。支持 i18n、主题、cookie 管理、SEO 管理、mdsvex 静态内容、shell 组件等。

## 公用事业

### 动画

- [AutoAnimate](https://auto-animate.formkit.com/) - 一个零配置的嵌入式动画实用程序，可为您的 Svelte 应用程序添加平滑的过渡。
- [svelte-typewriter](https://github.com/henriquehbr/svelte-typewriter) - 适用于 Svelte 应用程序的简单且可重复使用的打字机效果。
- [moving-icons](https://github.com/jis3r/icons) - 制作精美、移动的图标。为了苗条。 🧡
- [ssgoi](https://github.com/meursyphus/ssgoi) - 类似本机应用程序的页面转换具有弹簧物理特性、移动设备上的 60fps、SSR 就绪以及所有现代浏览器支持。

### 拖放

- [neodrag](https://github.com/PuruVJ/neodrag) - 一个 Draggable 即可统治一切💍。
- sveltednd(https://github.com/thisuxhq/sveltednd) - 用于 Svelte 5 应用程序的轻量级、灵活的拖放库。

### 表格

- [Superforms](https://superforms.rocks) - SvelteKit 库，用于处理服务器和客户端验证以及客户端表单显示。
- [Formsnap](https://www.formsnap.dev/) - 用于表单的高级 Svelte 组件，构建于 Superforms 和 Zod 之上。
- [felte](https://felte.dev/) - 可扩展的表单库，具有内置的 Yup、Zod、Vest 和 Superstruct 验证。
- [vest](https://github.com/ealush/vest) - 🦺 受单元测试启发的声明式表单验证框架。
- [svelte-formly](https://github.com/arabdevelop/svelte-formly) - 一个很好的解决方案，可以使用具有自定义样式的核心和自定义规则来生成和控制动态表单。 _（v5 之前）_
- [svelte-form-builder](https://github.com/pragmatic-engineering/svelte-form-builder-community) - 为 Svelte 构建的无代码拖放表单生成器。
- [Svelte Form Builder](https://svelte-form-builder.vercel.app) - 使用 Shadcn Svelte、Superforms 和 ZOD 创建表单 | Valibot 架构只需几分钟即可完成。
- [Formisch](https://formisch.dev/svelte/guides/introduction/) - Svelte 的表单库，重点关注性能、类型安全和包大小。

#### 表单组件

_单独的表单组件._

- [svelte-checkbox](https://github.com/HosseinShabani/svelte-checkbox) - 一个复选框组件（很酷的动画，可定制）。 _（v5 之前）_
- [svelte-toggle](https://github.com/beyonk-adventures/svelte-toggle) - 带样式的基本切换组件。 _（v5 之前）_

### HTTP 请求

- [sswr](https://github.com/ConsoleTVs/sswr) - Svelte stale while revalidate (SWR) 数据获取策略。
- [svelte-query](https://sveltequery.vercel.app/) - 在 Svelte 应用程序中获取、缓存和更新数据，而无需触及任何“全局状态”。
- [tanstack-svelte-query](https://tanstack.com/query/latest/docs/svelte/overview) - Svelte 的框架不可知类型安全查询和变异库。

### 声音和视频

- [svelte-sound](https://github.com/Rajaniraiyn/svelte-sound) - Svelte Actions 在目标 DOM 事件上播放交互声音。

### 网页GL

- [svelthree](https://github.com/vatro/svelthree) - 用于声明式构建反应式和可重用的 Three.js 场景图的组件库。
- [threlte](https://threlte.xyz) - Threlte 是一个渲染器和组件库，用于在 Svelte 应用程序中以声明性和状态驱动的方式使用 Three.js。

### 渐进式网页应用

- [SvelteKit-Adapter-Versioned-Worker](https://github.com/hedgehog125/SvelteKit-Adapter-Versioned-Worker) - 一个易于使用的服务工作线程构建插件，您无需担心缓存持续时间。

### 门户网站

- [svelte-portal](https://github.com/romkor/svelte-portal) - 用于在父组件的 DOM 之外渲染的组件。
- [svelte-teleport](https://github.com/nasso/svelte-teleport) - 跨 DOM 传送元素的组件。

### 字体

- [svelte-web-fonts/google](https://github.com/svelte-web-fonts/google) - 用于通过 Google Fonts API 轻松加载字体（包括自动完成）的微型组件。

### 国际化

- [svelte-fluent](https://github.com/nubolab-ffwd/svelte-fluent) - 用于轻松集成 [Fluent](https://projectfluent.org/) 本地化的组件。
- [svelte-i18n](https://github.com/kaisermann/svelte-i18n) - Svelte 的国际化库。
- [VoerkaI18n](https://zhangfisher.github.io/voerka-i18n/) - `Javascript/Typescript/Vue/React/Solidjs/SvelteJs/ReactNative` 的国际化解决方案
- [sveltekit-i18n](https://github.com/jarda-svoboda/sveltekit-i18n) - 用于在 SvelteKit 中集成 [i18n](https://www.npmjs.com/package/i18n) 风格的本地化。
- [@tolgee/svelte](https://github.com/tolgee/tolgee-js/tree/main/packages/svelte) - 基于网络的本地化工具，使用户能够直接在他们开发的 Svelte 应用程序中进行翻译。
- [@i18n-pro/svelte](https://github.com/i18n-pro/svelte) - Svelte 的轻量级、简单、灵活、自动翻译国际化工具。
- [ParaglideJS](https://inlang.com/m/dxnzrydw/library-inlang-paraglideJsAdapterSvelteKit) - 小型、类型安全的 i18n 库，带有开箱即用的翻译链接。
- [wuchale](https://github.com/K1DV5/wuchale) - 国际化库让您只需编写代码，无需函数调用或其他仪式。

## 路由器

_适用于单页应用程序 (SPA) 等。_

- [svelte-router-spa](https://github.com/jorgegorka/svelte-router) - 路由器将路由添加到您的单页应用程序 (SPA)。包括本地化、防护和嵌套布局。
- [svelte-routing](https://github.com/EmilTholin/svelte-routing) - 具有 SSR 支持的声明式 Svelte 路由库。
- [tinro](https://github.com/AlexxNB/tinro) - 一个小型、无依赖且高度声明的路由器。
- [svelte-spa-router](https://github.com/ItalyPaleAle/svelte-spa-router) - 针对单页应用程序 (SPA) 进行了优化，具有基于哈希的路由和参数支持。
- [svelte-client-router](https://github.com/arthurgermano/svelte-client-router) - Svelte Client Router 是您在路由 SPA 时所需和想到的一切。
- [@danielsharkov/svelte-router](https://github.com/DanielSharkov/svelte-router) - 一个简单易用的 SPA 路由器，在开发时考虑了页面转换。
- [@shaun/svelterouter](https://github.com/shaunlee/svelterouter) - 另一个受 vue-router 启发的 Svelte 路由器。
- [Elegua](https://github.com/howesteve/elegua) - 小型 (< 180LoC)、快速、简单、功能齐全的 SPA 路由器
- [svelte5-router](https://github.com/mateothegreat/svelte5-router) - 第一个带有嵌套、挂钩等功能的 Svelte 5 SPA 路由器。使用组件、片段或两者！
- [@wjfe/n-savant](https://github.com/WJSoftware/wjfe-n-savant) - 具有始终在线路径和哈希路由的快速反应式路由器，以及发明多哈希路由的路由器。
- [sv-router](https://github.com/colinlienard/sv-router) - 具有基于文件或基于代码的路由的类型安全 SPA 路由器。

## 框架

- [SvelteKit](https://svelte.dev/docs/kit/introduction) - 构建 Svelte 应用程序的最快方法。
- [Routify](https://routify.dev/) - Svelte 的路由，根据您的文件结构实现自动化。
- [Elder.js](https://github.com/elderjs/elderjs) - 针对 Svelte 的固执己见的静态站点生成器和 Web 框架，在构建时考虑了 SEO。 _（v5 之前）_
- [JungleJS](https://www.junglejs.org/) - 带有 GraphQL 的 Svelte Jamstack 框架。 _（v5 之前）_
- [svelte-document](https://github.com/mblouka/svelte-document) - 完全在 Svelte 中创建文档 (PDF)、简历或演示文稿。

## 开发工具

- [Frontman](https://github.com/frontman-ai/frontman) - 开源 AI 编码代理，位于您的浏览器中，可为 Svelte 应用程序提供点击编辑和热重载功能。

### 适配器

- [JesterKit EXE](https://github.com/Hugo-Dz/exe) - 一个适配器，用于将 SvelteKit Web 应用程序分发为具有零运行时依赖性的单个可执行二进制文件。与静态构建不同，它保留了所有 Kit 功能，如 SSR、API 端点、服务器挂钩等。

### 皮棉

_检查并格式化您的代码。_

- [prettier-plugin-svelte](https://github.com/sveltejs/prettier-plugin-svelte) - 使用 Prettyer 格式化您的组件。
- [svelte-check](https://www.npmjs.com/package/svelte-check) - 检查你的代码。
- [eslint-plugin-svelte](https://github.com/sveltejs/eslint-plugin-svelte) - 使用 AST 的 Svelte 的 ESLint 插件。

### 测试

- [svelte-jester](https://github.com/mihar-22/svelte-jester) - 一个 Jest 转换器，用于在将组件导入测试之前对其进行编译。
- [@testing-library/svelte](https://github.com/testing-library/svelte-testing-library) - 简单而完整的 Svelte DOM 测试实用程序，鼓励良好的测试实践。
- [jest-transform-svelte](https://github.com/rspieker/jest-transform-svelte) - 用于 Svelte 组件的 Jest Transformer。

### 编辑

_文本编辑器插件._

#### 视觉工作室代码

- [Svelte for VS Code](https://marketplace.visualstudio.com/items?itemName=svelte.svelte-vscode) - 为您的组件提供语法突出显示和丰富的智能感知。
- [Svelte 3 Snippets](https://marketplace.visualstudio.com/items?itemName=fivethree.vscode-svelte-snippets) - VS Code 的 Svelte 3 片段。

#### 崇高的文字

- [Svelte](https://packagecontrol.io/packages/Svelte) - 语法突出显示和对 Sublime Text 的支持。

#### 维姆

- [vim-svelte-plugin](https://github.com/leafOfTree/vim-svelte-plugin) - 语法突出显示和对 Vim 的支持。
- [coc-svelte](https://github.com/coc-extensions/coc-svelte) - 语法突出显示和对 (Neo)Vim 的支持。

#### 捷脑公司

- [Svelte](https://plugins.jetbrains.com/plugin/12375-svelte) - 语法突出显示和对 JetBrains 的支持。

## 应用实例

### 桌面

- [Oxide-Lab](https://github.com/FerrisMind/oxide-lab) - 以隐私为中心的本地 LLM 聊天应用程序，使用“candle”ML 框架使用 Svelte 5 前端和 Rust 后端构建。
- [Zephyr](https://github.com/Prismo-Studio/Zephyr) - 适用于 PC 游戏的开源模组管理器，内置 Archipelago 多世界随机发生器支持，使用 Svelte 5 和 Tauri 2 构建。
