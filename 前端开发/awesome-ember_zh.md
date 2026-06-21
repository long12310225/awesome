# 很棒的 Ember.js [![Awesome](https://awesome.re/badge.svg)](https://github.com/sindresorhus/awesome)

<div align="center">
  <a href="https://emberjs.com"><img width="300" src="media/ember-logo.svg" alt="Ember.js"></a>
  <br>
</div>

<p align="center">A curated list of delightful Ember.js <a href="#packages">packages</a> and <a href="#resources">resources</a>.</p>

<br>
  
<p align="center">
  <a href="ember-myths.md">Ember.js Myths</a>&nbsp;&nbsp;&nbsp;
  <a href="ember-questions.md">Readers Questions</a>&nbsp;&nbsp;&nbsp;
  <a href="https://help-wanted.emberjs.com/core">Contribute to Ember.js</a>
</p>

<br>

<p align="center">
  <sub>Just type <a href="https://ember.cool"><code>ember.cool</code></a> OR <a href="https://ember-community-russia.github.io/awesome-ember/"><code>https://ember-community-russia.github.io/awesome-ember/</code></a> to go here.</sub>
</p>

---

[Ember.js](https://emberjs.com) 是一个 JavaScript 框架，可以大大减少所需的时间、精力和资源
构建任何网络应用程序。它的重点是通过完成大多数 Web 开发项目中涉及的所有常见、重复性但重要的任务，使开发人员尽可能提高工作效率。

[Ember.js](https://emberjs.com) 还提供对 JavaScript、HTML 和浏览器最高级功能的访问，为您提供创建下一个杀手级 Web 应用程序所需的一切。

---

*您可能也喜欢[awesome-javascript](https://github.com/sorrycc/awesome-javascript)。*
*贡献前请阅读[贡献指南](contributing.md)。*

---

## 内容
- 很棒的 Ember.js [![很棒](https://awesome.re/badge.svg)](https://github.com/sindresorhus/awesome)
  - [Contents](#contents)
  - [Packages](#packages)
    - [AST](#ast)
    - [a11y](#a11y)
    - [Adapters](#adapters)
    - [Animations](#animations)
    - [Authentication](#authentication)
    - [Automation](#automation)
    - [Benchmarking](#benchmarking)
    - [Blogging](#blogging)
    - [Babel](#babel)
    - [Boilerplating](#boilerplating)
    - [Broccoli](#broccoli)
    - [西兰花读](#broccoli-read)
    - [构建工具](#build-tools)
    - [Charts](#charts)
    - [CI/CD](#cicd)
    - [代码分割](#code-splitting)
    - [Codestyle](#codestyle)
    - [命令行应用程序](#command-line-apps)
    - [命令行实用程序](#command-line-utilities)
    - [组件插件](#component-addons)
    - [Compression](#compression)
    - [内容管理系统](#content-management-systems)
    - [控制流程](#control-flow)
    - [CSS等](#css--etc)
    - [Fonts](#fonts)
    - [状态管理](#state-management)
    - [造型套件](#styling-kits)
    - [数据管理](#data-management)
    - [数据处理和计算](#data-manipulation--computed)
    - [数据验证](#data-validation)
    - [Database](#database)
    - [Date](#date)
    - [调试/分析](#debugging--profiling)
    - [Decorators](#decorators)
    - [Documentation](#documentation)
    - [Ember-inspector 路线图和概述](#ember-inspector-roadmaps--overview)
    - [最终用户定制](#end-user-customization)
    - [ES6](#es6)
    - [外部元件集成](#external-components-integration)
    - [Forms](#forms)
    - [函数式编程](#functional-programming)
    - [HTTP](#http)
    - [Helpers](#helpers)
    - [Image](#image)
    - [包含外部 JS 代码](#include-external-js-code)
    - [无限滚动](#infinite-scroll)
    - [国际化与本地化](#internalization--localization)
    - [Inputs](#inputs)
    - [作业队列](#job-queues)
    - [Logging](#logging)
    - [疯狂的科学](#mad-science)
    - [Math](#math)
    - [Metrics](#metrics)
    - [Minifiers](#minifiers)
    - [Miscellaneous](#miscellaneous)
    - [Mobile](#mobile)
    - [Modifiers](#modifiers)
    - [Parcel](#parcel)
    - [Payments](#payments)
    - [Polyfills](#polyfills)
    - [PWA](#pwa)
    - [查询参数](#query-params)
    - [Real-time](#real-time)
    - [路由插件](#routing-addons)
    - [旋转变压器定制](#resolver-customization)
    - [Security](#security)
    - [服务人员](#service-workers)
    - [SSR/服务器端渲染](#ssr--server-side-rendering)
    - [静态网站生成器和 SEO](#static-site-generators--seo)
    - [Styling](#styling)
    - [Templating](#templating)
    - [Testing](#testing)
    - [Text](#text)
    - [摇树](#tree-shaking)
    - [TypeScript](#typescript)
    - [用户界面库](#ui-libs)
    - [用户界面组件](#ui-components)
    - [UX](#ux)
    - [VR](#vr)
    - [VS 代码插件](#vs-code-addons)
    - [原子插件](#atom-addons)
    - [VIM](#vim)
    - [网络组件](#web-components)
    - [Webpack](#webpack)
    - [Weird](#weird)
    - [Resources](#resources)
    - [Articles](#articles)
    - [Ember-Cli 文章](#ember-cli-articles)
    - [为什么文章](#why-articles)
    - [快速入门文章](#jump-start-articles)
    - [文章 微光](#articles-glimmer)
    - [文章 引擎](#articles-engines)
    - [文章 Ember-并发](#articles-ember-concurrency)
    - [文章 ES6](#articles-es6)
    - [文章 TypeScript](#articles-typescript)
    - [文章 现代测试](#articles-modern-testing)
    - [文章 快速启动](#articles-fastboot)
    - [有关数据的文章](#articles-about-data)
    - [有关路由的文章](#articles-about-routing)
    - [Ember 文章中的纱线](#yarn-in-ember-articles)
    - [Best-practices](#best-practices)
    - [很高兴知道](#nice-to-know)
    - [Blogs](#blogs)
    - [Books](#books)
    - [Cheatsheets](#cheatsheets)
    - [Codemods](#codemods)
    - [Community](#community)
    - [贡献指南](#contribution-guides)
    - [Courses](#courses)
    - [Discovery](#discovery)
    - [余烬发布](#ember-releases)
    - [Examples](#examples)
    - [例子 微光](#examples-glimmer)
    - [Gists](#gists)
    - [要点 Ember 数据](#gists-ember-data)
    - [Miscellaneous](#miscellaneous-1)
    - [Newsletters](#newsletters)
    - [Podcasts](#podcasts)
    - [Sandboxes](#sandboxes)
    - [Screencasts](#screencasts)
    - [Slides](#slides)
    - [Styleguides](#styleguides)
    - [Tools](#tools)
    - [Tutorials](#tutorials)
    - [Twitter](#twitter)
    - [Videos](#videos)
    - [YouTube 频道](#youtube-channels)
    - [YouTube 播放列表](#youtube-playlists)
  - [License](#license)


## 套餐
### 谷草转氨酶

- [ember-ast-helpers](https://github.com/cibernox/ember-ast-helpers) - 该库是一个实用程序带，用于进行 AST 转换并尽可能让用户免受 AST 的细微差别的影响，因为它仍然是私有 API。
- [ember-template-recast](https://github.com/ember-template-lint/ember-template-recast) - 无损模板变压器。
- [jscodeshift](https://github.com/facebook/jscodeshift) - JavaScript codemod 工具包。
- [dyfactor](https://github.com/dyfactor/dyfactor) - 一个基于运行时信息运行代码模块的平台。

### a11y

- [ember-accessibility](https://github.com/coyote-labs/ember-accessibility) - 插件可帮助识别开发过程中的可访问性违规行为。
- [e-a11y-modal](https://github.com/MelSumner/e-a11y-modal) - 用于可访问的 Ember.js 应用程序的简单模式。
- [ember-a11y-landmarks](https://github.com/ember-a11y/ember-a11y-landmarks) - Ember.js 插件可帮助实现里程碑式的角色，以实现更好的可访问性。
- [ember-a11y](https://github.com/ember-a11y/ember-a11y) - 用于构建可访问的 Ember.js 应用程序的工具集合。
- [ember-component-focus](https://github.com/ember-a11y/ember-component-focus) - 一个 mixin，用于向 Ember.js 组件添加方法，帮助您管理当前聚焦的元素。
- [ember-gestures](https://github.com/html-next/ember-gestures) - Ember.js 手势提供了一种简单的手势使用方法，让您可以在整个应用程序中轻松定义和使用 HammerJS 管理器和识别器。
- [ember-steps](https://github.com/rwjblue/ember-steps) - 声明式创建向导、选项卡式 UI 等。
- [ember-page-title](https://github.com/tim-evans/ember-page-title) - Ember.js 应用程序的页面标题管理。
- [ember-self-focused](https://github.com/linkedin/self-focused/tree/master/packages/ember-self-focused) - 专注于过渡路线。
- [ember-keyboard](https://github.com/patience-tema-baron/ember-keyboard) - 一个 Ember.js 插件，用于轻松支持键盘事件。
- [ember-a11y-testing](https://github.com/ember-a11y/ember-a11y-testing) - 一套可在 Ember.js 测试框架内运行的可访问性测试。
- [a11y-announcer](https://github.com/ember-a11y/a11y-announcer) - 一个易于访问的 ember 路线变更播音员。
- [ember-a11y-refocus](https://github.com/MelSumner/ember-a11y-refocus) - 为 Ember 应用程序提供不显眼的导航叙述元素。

### 适配器

- [ember-cli-markdown-resolver](https://github.com/willviles/ember-cli-markdown-resolver) - Ember CLI 插件，用于解析自定义文件夹中的 Markdown 文件并通过服务检索内容。
- [ember-cloud-firestore-adapter](https://github.com/rmmmp/ember-cloud-firestore-adapter) - 适用于 Cloud Firestore 的非官方 Ember 数据适配器和序列化器。
- [ember-data-hal-9000](https://github.com/201-created/ember-data-hal-9000) - 与 ember-data 兼容的 ember-cli 插件，提供 HAL 适配器 (HATEOAS)。
- [ember-django-adapter](https://github.com/dustinfarris/ember-django-adapter) - 适用于 Django REST Framework 的 Ember CLI 插件适配器。
- [ember-graphql-adapter](https://github.com/alphasights/ember-graphql-adapter) - Ember 数据的 GraphQL 适配器。
- [ember-indexeddb](https://github.com/mydea/ember-indexeddb) - 用于与 ember 和 ember-data 中的 IndexedDB 配合使用的实用程序和适配器。
- [ember-localforage-adapter](https://github.com/genkgo/ember-localforage-adapter) - Ember 数据的离线使用。
- [ember-local-storage](https://github.com/funkensturm/ember-local-storage) - 该插件为计算属性提供存储，该属性返回代理并将更改保存到 localStorage 或 sessionStorage。
- [ember-pouch](https://github.com/pouchdb-community/ember-pouch) - 用于 Ember 数据的 PouchDB/CouchDB 适配器。
- [ember-wordpress](https://github.com/oskarrough/ember-wordpress) - Ember.js 和 WordPress 之间的桥梁。
- [emberfire](https://github.com/firebase/emberfire) - Firebase 的官方 Ember 数据适配器。
- [ninjafire](https://github.com/lineupninja/ninjafire) - 用 Typescript 编写的 Firebase ORM。

### 动画

- [ember-animated](https://github.com/ember-animation/ember-animated) - [使用 Ember js 制作网页动画](https://www.youtube.com/watch?v=TSvnutA9PUE)
- [liquid-fire](https://github.com/ember-animation/liquid-fire) - 雄心勃勃的 Ember.js 应用程序的动画和过渡。

### 认证

- [ember-cli-simple-auth-extensions](https://emberobserver.com/categories/ember-cli-simple-auth-extensions)
- [ember-simple-auth](https://github.com/simplabs/ember-simple-auth) - 用于在 Ember.js 应用程序中实现身份验证/授权的库。
- [tori](https://github.com/Vestorly/torii) - Ember.js 中用于身份验证的一组干净的抽象。

### 自动化

- [ember-cli-deploy](https://github.com/ember-cli-deploy/ember-cli-deploy) - Ember CLI 应用程序的部署管道。
- [ember-cli-deploy-webhooks](https://github.com/simplabs/ember-cli-deploy-webhooks) - Ember CLI 部署插件，用于在部署期间调用 Webhook。
- [ember-cli-release](https://github.com/shipshapecode/ember-cli-release) - 用于版本化发布管理的 Ember CLI 插件。
- [ember-cli-sri](https://github.com/jonathanKingston/ember-cli-sri) - 该插件用于为 ember 应用程序生成子资源完整性 (SRI) 哈希值。
- [ember-cli-dependency-lint](https://github.com/salsify/ember-cli-dependency-lint) - 检查应用程序的插件依赖项，确保每个插件只有一个版本。

### 标杆管理

- [ember-macro-benchmark](https://github.com/krisselden/ember-macro-benchmark) - 使用 2 个版本的 Ember.js 运行的 Ember 应用程序的基准测试记录。
- [ember-performance](https://github.com/eviltrout/ember-performance) - 一套 Ember.js 测试套件，可帮助提高性能。
- [emberperf](http://emberperf.eviltrout.com) - Ember.js 性能（版本之间）。

### 写博客

- [empress-blog](https://github.com/empress/empress-blog) - 基于 Ember.js 构建的博客系统的功能齐全、SEO 友好的静态站点实现。
- [ember-cli-blog](https://github.com/broerse/ember-cli-blog) - Tom Dale 的博客示例已针对 Ember CLI 进行了更新。
- [ember-tumblr](https://github.com/elwayman02/ember-tumblr) - 用于集成 Tumblr 博客的 Ember.js 插件。

### 巴别塔

- [ember-cli-babel-plugin-helpers](https://github.com/dfreeman/ember-cli-babel-plugin-helpers) - 用于在 Ember CLI 应用程序和插件中管理 Babel 插件的实用程序。

### 锅炉电镀

- [ember-boilerplate](https://github.com/mirego/ember-boilerplate) - 我们在 Mirego 构建 Ember.js 项目的稳定基础。


### 西兰花

- [broccoli-concat-analyser](https://github.com/stefanpenner/broccoli-concat-analyser) - 资产概况。
- [broccoli-debug](https://github.com/broccolijs/broccoli-debug) - 构建管道作者的实用程序，允许对他们编写的 Broccoli 管道进行简单的调试。
- [broccoli-stew](https://github.com/stefanpenner/broccoli-stew) - 提供用于开发基于 broccoli 的构建管道的常用便利函数。
- [broccolijs-tutorial](https://github.com/oligriffiths/broccolijs-tutorial) - Broccoli.js 教程存储库。
- [broccoli-rollup](https://github.com/chadhietala/broccoli-rollup) - 用于“Rollup”的西兰花插件。
- [broccoli-manifest](https://github.com/racido/broccoli-manifest) - 西兰花的 HTML5 缓存清单编译。
- [broccoli-glow](https://github.com/locks/broccoli-glow) - 从单个文件动态创建组件等

### 西兰花读

- [调试西兰花树](https://dockyard.com/blog/2015/02/02/debugging-a-broccoli-tree)
- [调试 Broccoli 和 Ember-CLI](https://mfeckie.github.io/Debugging-Broccoli-And-Ember/)
- [调试 Ember-cli 构建时间](https://medium.com/@Dhaulagiri/debugging-ember-cli-build-times-38bd1b0f55f9)
- [吃你的蔬菜 - Broccoli.js 教程](http://www.oligriffiths.com/broccolijs/)
- [Ember.js 惰性资产：指纹识别和按需加载静态/动态资产](https://codeburst.io/ember-js-lazy-assets-fingerprinting-loading-static-dynamic-assets-on-demand-f09cd7568155)
- [关于如何编写更快的西兰花插件的思考](https://gist.github.com/Gaurav0/c1eb3a00670eed28e57c2cf92d3f7668)

### 构建工具

- [Broccoli](https://github.com/broccolijs/broccoli) - 快速、可靠的资产管道，支持恒定时间重建和紧凑的构建定义。

### 图表

- [ember-charts](https://github.com/Addepar/ember-charts) - 使用 Ember.js 和 d3.js 框架构建的图表库。
- [ember-sparkles](https://github.com/LocusEnergy/ember-sparkles) - 使用 ember-d3-helpers 构建的可组合 D3 组件的集合。
- [ember-highcharts](https://github.com/ahmadsoe/ember-highcharts) - ember-cli 的 Highcharts、HighStock 和 HighMaps 组件。
- [ember-c3](https://github.com/Glavin001/ember-c3) - C3 的插件库，基于 D3 的可重用图表库，兼容性更强。

### 持续集成/持续交付

- [ember-cli-server-variables](https://github.com/blimmer/ember-cli-server-variables) - 一个 Ember CLI 插件，支持将变量添加到生成的 index.html 文件的 head 标签中。
- [ember-ci](https://github.com/mike-north/ember-ci) - ember.js 应用程序的持续集成好东西。
- [CI with GitHub Actions for Ember Apps](https://crunchingnumbers.live/2020/03/17/ci-with-github-actions-for-ember-apps/) - 使用 GitHub Actions 减少 CI 运行时间
- [CI with GitHub Actions for Ember Apps: Part 2](https://crunchingnumbers.live/2020/08/31/ci-with-github-actions-for-ember-apps-part-2/) - 迁移到 v2 操作，降低运行时成本并持续部署

### 代码分割

- [ember-engines](https://github.com/ember-engines/ember-engines) - 此 Ember.js 插件实现了 Ember.js 引擎 RFC 中描述的功能。从用户的角度来看，引擎允许将多个逻辑应用程序组合成一个应用程序。
- [ember-lazy-mount](https://github.com/buschtoens/ember-lazy-mount) - 允许 {{mount}} 延迟加载无路由引擎。
- [ember-cli-bundle-loader](https://github.com/MiguelMadero/ember-cli-bundle-loader) - 允许多个捆绑包并进行延迟加载的插件。
- [ember-cli-lazy-load](https://github.com/duizendnegen/ember-cli-lazy-load) - 支持通过将 Ember.js 应用程序拆分为捆绑包来延迟加载它。

### 代码风格

- [ember-cli-template-lint](https://github.com/ember-template-lint/ember-cli-template-lint) - “ember-template-lint”的 Ember CLI 集成。
- [ember-cli-alex](https://github.com/yohanmishkin/ember-cli-alex) - Alex 负责 Ember.js 应用程序。
- [ember-prop-types](https://github.com/ciena-blueplanet/ember-prop-types) - 改进了 Ember.js 应用程序和插件的属性管理。

### 命令行应用程序

- [ember-cli-create](https://github.com/gossi/ember-cli-create) - 用于创建新 ember 项目的 CLI 向导。
- [@ember/optional-features](https://github.com/emberjs/ember-optional-features) - 该插件允许您轻松启用/禁用 ember-source 中的可选功能。为了澄清我们所说的可选的含义，这些是在可预见的将来选择加入/选择退出和可选的功能，而不是默认启用的功能。它仅适用于应用程序，不适用于插件。
- [ember-cli-rename](https://github.com/trabus/ember-cli-rename) - ember-cli 的插件提供了“ember rename”命令。

### 命令行实用程序

- [ember-cli-update](https://github.com/ember-cli/ember-cli-update) - 更新 Ember CLI Ember.js 应用程序、插件和 Glimmer.js 应用程序。
- [ember-cli-deprecation-workflow](https://github.com/mixonic/ember-cli-deprecation-workflow) - 一个旨在使 Ember.js 升级更容易的插件，允许您在没有大量控制台噪音的情况下处理弃用。

### 组件插件

- [ember-diff-attrs](https://github.com/workmanw/ember-diff-attrs)
- [ember-compatibility-helpers](https://github.com/pzuraq/ember-compatibility-helpers) - 允许您编写向后兼容的 Ember.js 插件的帮助程序。

### 压缩

- [ember-cli-deploy-brotli](https://github.com/mfeckie/ember-cli-deploy-brotli) - Ember.js 部署插件来支持 brotli 压缩。


### 内容管理系统

- [ember-admin](https://github.com/DockYard/ember-admin) - 自动发现您的模型并在简单的 CRUD 界面中与所有模型数据进行交互。
- [https://authmaker.com/](https://authmaker.com/) - 在 3 天内从零到功能齐全并成为 MVP。

### 控制流程

- 承诺
	- [ember-computed-promise-monitor](https://github.com/NullVoxPopuli/ember-computed-promise-monitor) - 使计算属性具有异步感知能力。
- 可观察到的
	- [ember-rx](https://github.com/alexlafroscia/ember-rx) - Ember.js 的 RxJS 6 集成。
- 发电机
	- [ember-concurrency](https://github.com/machty/ember-concurrency) - Ember.js 插件使您能够编写简洁、无忧、可取消、可重新启动的异步任务。
  - [ember-master-tab](https://github.com/rhyek/ember-master-tab) - 一种提供服务的库，可帮助仅在 Ember 应用程序的一个选项卡上运行功能。

### CSS等

- [ember-cli-stylelint](https://github.com/billybonks/ember-cli-stylelint) - 将 styleint 添加到您的 ember 应用程序中，以检查各种 css。
- [ember-cli-autoprefixer](https://github.com/kimroen/ember-cli-autoprefixer) - 通过 autoprefixer 自动运行您的样式。
- [ember-cli-sass](https://github.com/aexmachina/ember-cli-sass) - 使用 node-sass 预处理 ember-cli 应用程序的文件，并支持 sourceMaps 和包含路径。
- [ember-cli-sass-pods](https://github.com/justtal/ember-cli-sass-pods) - 享受使用 pod 目录中的 sass 样式文件来设计 pod 的样式。
- [ember-component-css](https://github.com/ebryn/ember-component-css) - 一个 Ember CLI 插件，允许您为各个组件指定样式。
- [ember-cli-postcss](https://github.com/jeffjewiss/ember-cli-postcss) - ember-cli 的 PostCSS 集成。
- [ember-css-modules](https://github.com/salsify/ember-css-modules) - 用于雄心勃勃的应用程序的 CSS 模块。
- [ember-cli-tailwind](https://github.com/embermap/ember-cli-tailwind) - Tailwind 是一个实用程序优先的 CSS 框架，用于快速构建自定义用户界面。
- [ember-emotion](https://github.com/alexlafroscia/ember-emotion) - 在 Ember.js 中使用情感样式。
- [css-blocks](https://github.com/linkedin/css-blocks) - 高性能、可维护的样式表。
- [ember-cli-eyeglass](https://github.com/linkedin/eyeglass/tree/master/packages/ember-cli-eyeglass) - 这个 Ember CLI 插件使得通过 node-sass 编译具有 Eyeglass 支持的 sass 文件变得很简单。

### 字体
- [ember-cli-webfont](https://github.com/vitch/ember-cli-webfont) - 作为 ember-cli 构建过程的一部分，轻松从 svg 文件生成 webfonts。

### 状态管理

- [ember-buffered-proxy](https://github.com/yapplabs/ember-buffered-proxy)
- [ember-changeset](https://github.com/poteto/ember-changeset)
- [ember-cerebraljs](https://github.com/lifeart/ember-cerebraljs) - 使用 Cerebral 增强复杂 Ember.js 应用程序的状态管理。
- [ember-redux](http://www.ember-redux.com/) - Ember 应用程序的可预测状态管理。
- [ember-state-services](https://github.com/stefanpenner/ember-state-services)
- [ember-time-machine](https://github.com/offirgolan/ember-time-machine)


### 造型套件

- [ember-cli-tailwind](https://github.com/embermap/ember-cli-tailwind) - 将 Tailwind CSS 添加到您的应用程序或插件中。

### 数据管理

- [ember-apollo-client](https://github.com/bgentry/ember-apollo-client) - Apollo 客户端和 GraphQL 的 ember-cli 插件。
- [ember-cli-sofa](https://github.com/ampatspell/ember-cli-sofa) - Ember.js 的 CouchDB 持久性库。
- [ember-orbit](https://github.com/orbitjs/ember-orbit) - 使用 Orbit.js 构建的 Ember.js 数据层。
- [ember-data-storefront](https://github.com/embermap/ember-data-storefront) - 解决常见数据加载问题的 API 集合。
- [ember-m3](https://github.com/hjdivad/ember-m3) - 该插件提供了 DS.Model 的替代模型实现。
- [ember-cli-zuglet](https://www.ember-cli-zuglet.com/) - Ember.js 插件可轻松集成 Firebase。

### 数据处理和计算

- [ember-awesome-macros](https://github.com/kellyselden/ember-awesome-macros) - Ember.js 计算宏的集合。
- [ember-cpm](https://github.com/cibernox/ember-cpm) - Ember.js 的计算属性宏。
- [ember-macaroni](https://github.com/poteto/ember-macaroni) - 使用计算属性通心粉（宏）使您的应用程序代码保持干燥和免费。

### 数据验证

- [ember-cp-validations](https://github.com/offirgolan/ember-cp-validations) - Ember.js 基于计算属性的验证。
- [ember-changeset-validations](https://github.com/poteto/ember-changeset-validations/) - 对 ember-changeset 的验证。
- [ember-model-validator](https://github.com/esbanarango/ember-model-validator) - 以明确且简单的方式向 Ember 数据模型添加验证，无需一堆验证文件或复杂的结构。
- [ember-validated-form](https://github.com/adfinis-sygroup/ember-validated-form) - 通过客户端验证轻松创建表单。
- [ember-line-graph](https://astronomersiva.github.io/ember-line-graph/) - 用于绘制折线图的零依赖 ember-addon。

### 数据库

- [ember-indexeddb](https://github.com/mydea/ember-indexeddb) - 用于与 ember 和 ember-data 中的 IndexedDB 配合使用的实用程序和适配器。

### 日期

- [ember-moment](https://github.com/stefanpenner/ember-moment) - moment.js 和 Ember.js 的模板助手和计算属性宏。


### 调试/分析

- [ember-debug-logger](https://github.com/salsify/ember-debug-logger) - 公开 Visionmedia/debug 库以在 Ember.js 应用程序中使用。
- [ember-devtools](https://github.com/aexmachina/ember-devtools) - 有用的 Ember.js 调试功能的集合。
- [ember-chrome-devtools](https://github.com/dwickern/ember-chrome-devtools) - Ember.js 的 Chrome DevTools 插件。
- [ember-cli-bundle-analyzer](https://github.com/kaliber5/ember-cli-bundle-analyzer) - 一个 Ember CLI 插件，用于使用交互式可缩放树形图来分析应用程序捆绑输出的大小和内容。
- [ember-perf-timeline](https://github.com/ember-best-practices/ember-perf-timeline) - 将性能信息添加到 Ember.js 应用程序的 Chrome 时间线中。
- [ember-cli-route-map](https://github.com/BBVAEngineering/ember-cli-route-map) - 用于生成 Ember.js 应用程序的路由图的命令。
- [heimdalljs-visualizer](https://github.com/rwjblue/heimdalljs-visualizer) - heimdalljs 数据的可视化工具。
- [source-map-explorer](https://github.com/danvk/source-map-explorer) - 通过源映射分析和调试空间使用情况。
- [ember-dead-code](https://github.com/buschtoens/ember-dead-code) - 通过真实的用户监控，自信地检测死代码。

### 装饰器

- [Macro Decorators](https://pzuraq.github.io/macro-decorators/) - 通过创建复制 getter/setter 功能的装饰器来干燥代码

### 文档

- [ember-cli-addon-docs](https://github.com/ember-learn/ember-cli-addon-docs) - 简单、漂亮的 Ember.js 插件文档。
- [ember-cli-jsdoc](https://github.com/softlayer/ember-cli-jsdoc) - 一个 Ember.js CLI 插件，用于根据源代码中的 JSDoc 注释生成 HTML 文档。
- [ember-freestyle](https://github.com/chrislopresto/ember-freestyle) - Ember-freestyle 是一个 Ember.js 插件，可让您快速为 Ember.js 应用程序创建组件资源管理器。

### Ember-inspector 路线图和概述

- [Ember 检查员配对](https://www.youtube.com/watch?v=rFNR_Fj1G84)
- [Ember 检查器同步](https://www.youtube.com/watch?v=PvsfQrKxl_8)

### 最终用户定制
- [ember-asset-loader](https://github.com/ember-engines/ember-asset-loader) - Ember.js 应用程序的资产加载支持。
- [ember-experiments](https://github.com/outdoorsy/ember-experiments) - 实验，Ember.js 的 A/B 对比测试插件。
- [ember-cli-hot-loader](https://github.com/toranb/ember-cli-hot-loader) - 初步了解 Ember 生态系统中的热重载是什么样子。
- [ember-ast-hot-load](https://github.com/lifeart/ember-ast-hot-load) - 通用热加载插件。
- [ember-cli-build-notifications](https://github.com/pdud/ember-cli-build-notifications) - ember-cli 出现构建错误时的通知。
- [ember-feature-flags](https://github.com/kategengler/ember-feature-flags) - 提供功能标志的 ember-cli 插件。
- [ember-named-yields](https://github.com/knownasilya/ember-named-yields) - Ember.js 组件的命名 Yields。
- [ember-islands](https://github.com/mitchlloyd/ember-islands) - 在服务器渲染页面上的任何位置渲染 Ember.js 组件以创建“丰富的岛屿”。
- [ember-wormhole](https://github.com/yapplabs/ember-wormhole) - 在 DOM 中的其他位置渲染子视图。
- [ember-stargate](https://github.com/kaliber5/ember-stargate) - 现代的做法是使用所谓的“门户”将事物呈现在 DOM 树的不同位置，而不是应用程序中逻辑定义的位置。

### ES6

- [ember-concurrency-decorators](https://github.com/machty/ember-concurrency-decorators) - 用于声明/配置 ember 并发任务的装饰器语法。
- [ember-decorators](https://github.com/ember-decorators/ember-decorators) - 适用于 Ember.js 应用程序的有用装饰器。
- [@ember-decorators/argument](https://github.com/ember-decorators/argument) - Ember.js 中组件和对象参数的装饰器。
- [sparkles-decorators](https://github.com/gossi/sparkles-decorators) - Sparkles/Glimmer.js 组件的装饰器。

### 外部元件集成

- [ember-glimmer-component](https://github.com/smfoote/ember-glimmer-component) - Ember.js 中类似 Glimmer.js 的组件。
- [sparkles-component](https://github.com/rwjblue/sparkles-component) - Addon 曾经通过现有的公共 API 在 Ember.js 应用程序中试验 @glimmer.js/component 风格的 API。
- [hooked-components](https://github.com/lifeart/hooked-components) - Ember.js 的自定义组件，受到 React Hooks 方法的启发。
- [ember-functional-component](https://github.com/rwjblue/ember-functional-component) - 尝试使用“纯函数”作为组件。
- [ember-lifecycle-component](https://github.com/NullVoxPopuli/ember-lifecycle-component) - 当您可能需要模板时，组件具有额外的生命周期。
- [ember-vue-components](https://github.com/lifeart/ember-vue-components) - Ember 的 Vue.JS 组件 API。
- [@alexlafroscia/ember-cli-react](https://github.com/alexlafroscia/ember-cli-react) - 在 Ember.js 中渲染 React 组件。
- [@AltSchool/ember-cli-react](https://github.com/AltSchool/ember-cli-react) - 在 Ember.js 应用程序中使用 React 组件层次结构。

### 表格

- [ember-cli-crudities](https://ember-cli-crudities.readthedocs.io) - 表单和可编辑列表生成器，从 json 配置工作，可以静态或动态加载。
- [ember-form-for](https://github.com/martndemus/ember-form-for) - 这个 Ember.js 插件将为您提供一种构建良好表单的简单方法。

### 函数式编程

- [Bacon.js](http://baconjs.github.io) - 函数式反应式编程。
- [Folktale](http://folktale.origamitower.com) - 用于 JavaScript 中通用函数式编程的库套件，使您能够编写优雅的模块化应用程序，同时减少错误并提高重用率。
- [immutable](https://github.com/facebook/immutable-js) - 不可变的数据集合。
- [Kefir.js](https://github.com/rpominov/kefir) - 反应式库专注于高性能和低内存使用。
- [Lazy.js](https://github.com/dtao/lazy.js) - 实用程序库类似于 lodash/Underscore，但具有惰性求值，在许多情况下可以转化为卓越的性能。
- [lodash](https://lodash.com) - 实用程序库提供一致性、定制、性能和附加功能。更好更快的 Underscore.js。
- [mori](http://swannodette.github.io/mori/) - 用于使用 ClojureScript 的持久数据结构并通过普通 JavaScript 支持 API 的库。
- [Mout](http://moutjs.com) - 实用程序库与其他现有解决方案的最大区别在于您可以选择仅加载您需要的模块/功能，无需额外的开销。
- [Ramda](http://ramdajs.com) - 实用程序库重点关注通过自动柯里化和反向参数顺序实现的灵活功能组合。避免改变数据。
- [RxJS](http://reactivex.io) - 用于转换、组合和查询各种数据的函数反应库。
- [underscore-contrib](http://documentcloud.github.io/underscore-contrib/) - Underscore 实用腰带上的黄铜扣。

### HTTP协议

- [ember-ajax](https://github.com/ember-cli/ember-ajax) - 用于在 Ember.js 1.13+ 应用程序中发出 AJAX 请求的服务。
- [ember-socket-guru](https://github.com/netguru/ember-socket-guru) - 用于轻松与 Pusher.js、Action Cable、Socket.io 和 Phoenix Channels 集成的插件。

### 帮手

- [ember-event-helpers](https://github.com/buschtoens/ember-event-helpers) - `{{on}}` 修饰符的免费事件模板助手。
- [ember-render-helpers](https://github.com/buschtoens/ember-render-helpers) - `@ember/render-modifiers` 作为模板助手。
- [ember-element-helper](https://github.com/tildeio/ember-element-helper) - Glimmer 模板的动态元素助手。
- [ember-composable-helpers](https://github.com/DockYard/ember-composable-helpers) - Ember.js 中声明性模板的可组合助手。
- [ember-helpers](https://github.com/abcum/ember-helpers) - Ember.js 的车把助手集合。
- [ember-d3-helpers](https://github.com/LocusEnergy/ember-d3-helpers) - 用于构建可组合 D3 图表的 Ember.js 帮助器集合。
- [ember-math-helpers](https://github.com/shipshapecode/ember-math-helpers) - Ember.js HTMLBars 用于基本算术的帮助程序。
- [ember-promise-helpers](https://github.com/fivetanley/ember-promise-helpers) - 为您的 Ember.js 模板提供 Promise-y 糖分。
- [ember-route-action-helper](https://github.com/DockYard/ember-route-action-helper) - 路线中的气泡闭合动作。
- [ember-root-url](https://github.com/ef4/ember-root-url) - 一个模板助手，用于保持 URL 相对于应用程序的 rootURL。
- [ember-store-helpers](https://github.com/ember-sapporo/ember-store-helpers) - 该附加组件提供与 ember-data 相关的帮助程序。
- [ember-truth-helpers](https://github.com/jmurphyau/ember-truth-helpers) - Ember.js HTMLBars 用于 `{{if}}` 和 `{{unless}}` 的帮助器：not、and、or、eq 和 is-array。
- [ember-awesome-macros](https://github.com/kellyselden/ember-awesome-macros) - Ember.js 计算宏的集合。
- [ember-macro-helpers](https://github.com/kellyselden/ember-macro-helpers) - Ember.js 宏助手，用于制作您自己的精美宏！
- [ember-cli-string-helpers](https://github.com/romulomachado/ember-cli-string-helpers) - 从 DockYard 的 ember-composable-helpers 中提取的字符串助手集。

### 图片

- [ember-svg-jar](https://github.com/ivanvotti/ember-svg-jar) - 将 SVG 图像嵌入到 Ember.js 应用程序中的最佳方式。

### 包含外部 JS 代码

- [ember-auto-import](https://github.com/ef4/ember-auto-import) - 从 npm 包中零配置导入。
- [ember-cli-cjs-transform](https://github.com/rwjblue/ember-cli-cjs-transform) - CommonJS 导入。
- [ember-cli-es6-transform](https://github.com/sandydoo/ember-cli-es6-transform) - 从 npm、bower 或应用程序中的其他任何位置导入 ES6 模块。
- [ember-browserify](https://github.com/ef4/ember-browserify) - 用于通过 browserify 从 npm 轻松加载 CommonJS 包的插件。

### 无限滚动

- [ember-infinity](https://github.com/ember-infinity/ember-infinity) - Ember CLI 应用程序的简单、灵活的无限滚动。
- [vertical-collection](https://github.com/html-next/vertical-collection) - > 60 FPS 时无限滚动和遮挡。
- [smoke-and-mirrors](https://github.com/html-next/smoke-and-mirrors) - 为雄心勃勃的应用程序提供雄心勃勃的无限滚动和纤薄渲染。

### 国际化与本地化

- [ember-intl](https://github.com/ember-intl/ember-intl) - 翻译复杂的消息字符串。日期/时间、数字和相对时间的本地化格式。
- [ember-intl-analyzer](https://github.com/simplabs/ember-intl-analyzer) - 查找 Ember.js 项目中未使用的翻译。

### 输入

- [ember-autoresize](https://github.com/tim-evans/ember-autoresize) - 自动调整 Ember.js 组件的大小。


### 作业队列

- [ember-data-tasks](https://github.com/knownasilya/ember-data-tasks)
- [ember-concurrency](http://ember-concurrency.com)
- [ember-custom-actions](https://github.com/Exelord/ember-custom-actions) - Ember.js 应用程序的自定义 API 操作。
- [ember-pipeline](https://github.com/poteto/ember-pipeline)
- [ember-lifeline](https://github.com/ember-lifeline/ember-lifeline) - 一个 ember 插件，用于管理对象中异步行为的生命周期。

### 记录

- [console.re](https://console.re/)
- [ember-debug-logger](https://emberobserver.com/addons/ember-debug-logger) - 用于公开 Visionmedia 调试记录器的 Ember.js 插件。
- [ember-logging-service](https://github.com/acquia/ember-logging-service/) - 该插件提供了可在整个应用程序中使用的通用且可扩展的日志记录服务。
- [raygun](https://raygun.com/)

### 疯狂的科学

- [ember-elm](https://github.com/nucleartide/ember-elm) - 在您的 Ember.js 应用程序中编写 Elm。
- [javascript-algorithms](https://github.com/trekhleb/javascript-algorithms) - 用 JavaScript 实现的算法和数据结构，并附有解释和进一步阅读的链接。

### 数学

- [ember-katex](https://github.com/firecracker/ember-katex) - 使用 KaTeX 渲染您的 LaTeX 公式。
- [ember-math-helpers](https://github.com/shipshapecode/ember-math-helpers) - Ember.js HTMLBars 用于基本算术的帮助程序。

### 指标

- [ember-user-activity](https://github.com/elwayman02/ember-user-activity) - 用于跟踪用户活动和闲置的 Ember.js 插件。
- [ember-metrics](https://github.com/poteto/ember-metrics) - 将数据发送到多个分析服务，无需重新实现新的 API。

### 缩小器
- [ember-hbs-minifier](https://github.com/simplabs/ember-hbs-minifier) - 从 Handlebars 模板中去除空白。
- [ember-cli-template-trimmer](https://github.com/lifeart/ember-cli-template-trimmer) - 该插件在编译阶段删除换行符。

### 杂项

- [diagonal routes](https://alexspeller.com/ember-diagonal/) - 查看给定 ember 路由定义的路由结构、模板和路由挂钩。
- [ember data model maker](https://github.com/andycrum/ember-data-model-maker/) - Ember 数据模型制作器 (EDMM)。

### 手机

- [corber](https://github.com/isleofcode/corber) - 使用 Ember.js 构建的 cordova 和人行横道混合应用程序的工具。
- [glimmer-native](https://github.com/bakerac4/glimmer-native) - 您是否曾经想过使用 Ember.js/Glimmer.js 创建原生移动应用程序？好吧，现在你可以了！
- [ember-mobile-bar](https://github.com/nickschot/ember-mobile-bar) - 具有类似移动应用程序行为的托管固定（工具）栏。
- [ember-mobile-core](https://github.com/nickschot/ember-mobile-core) - 为 ember-mobile-* 插件提供平移识别器和一些实用程序。
- [ember-mobile-menu](https://github.com/nickschot/ember-mobile-menu) - 专为移动设备定制的可拖动侧边栏。
- [ember-mobile-pane](https://github.com/nickschot/ember-mobile-pane) - 移动布局 ember-mobile-pane。
- [ember-responsive](https://github.com/freshbooks/ember-responsive) - 使用 Ember.js 轻松实现响应式布局。

### 修饰符
- [ember-css-vars](https://github.com/luxferresum/ember-css-vars) - 应用 css 变量的 ember 修饰符。这提供了一种将数据从 JavaScript 公开到 css 的保存方法。
- [ember-on-modifier](https://github.com/buschtoens/ember-on-modifier) - Modifiers RFC #353 中显示的“{{on}}”元素修饰符的实现。
- [ember-ref-modifier](https://github.com/lifeart/ember-ref-modifier) - `{{ref}}` 元素修饰符的实现。
- [ember-render-modifiers](https://github.com/emberjs/ember-render-modifiers) - 实现 RFC #415 的 did-insert / did-update / will-destroy 修饰符。
- [ember-functional-modifiers](https://github.com/spencer516/ember-functional-modifiers) - Ember.js 的功能修饰符。
- [ember-style-modifier](https://github.com/jelhan/ember-style-modifier) - 该插件提供了一个 {{style}} 元素修饰符来设置元素的样式。
- [ember-simple-animate](https://github.com/abhilashlr/ember-simple-animate) - 简单的 ember animate 插件，用于基于 CSS 的动画。

### 包裹

- [ember-parcel-example](https://github.com/rtablada/ember-parcel-example) - Ember.js + Parcel.js 示例。
- [todomvc-demo](https://github.com/devongovett/todomvc-demo) - Glimmer.js + Parcel.js 示例。

### 付款方式

- [ember-credit-card](https://github.com/esbanarango/ember-credit-card) - “用一行代码让你的信用卡变得梦幻”。

### 聚合物填料

- [ember-modifier-manager-polyfill](https://github.com/rwjblue/ember-modifier-manager-polyfill) - Ember.js 2.12 到 3.7 的 Polyfill 元素修饰符。
- [ember-angle-bracket-invocation-polyfill](https://github.com/rwjblue/ember-angle-bracket-invocation-polyfill) - 该插件为尖括号调用语法提供了一个填充，如 RFC 311 中所述。
- [ember-named-arguments-polyfill](https://github.com/rwjblue/ember-named-arguments-polyfill) - Polyfills 支持 Ember.js 2.10 到 3.0 的命名参数。
- [ember-native-class-polyfill](https://github.com/pzuraq/ember-native-class-polyfill) - 该插件为 Ember.js RFC #240 和 #337 中提出的本机类行为提供了一个填充。
- [ember-router-service-polyfill](https://github.com/rwjblue/ember-router-service-polyfill) - 该插件为 Ember.js 2.15 中添加的 ember-routing-router-service 功能提供了尽力而为的 polyfill。
- [ember-fn-helper-polyfill](https://github.com/rwjblue/ember-fn-helper-polyfill) - 该插件为 {{fn}} 帮助器提供了一个填充，如 RFC #470 中所述。
- [ember-named-blocks-polyfill](https://github.com/ember-polyfills/ember-named-blocks-polyfill) - 该插件为可生成的命名块功能提供了一个填充。

### 渐进式网页应用

- [ember-service-worker-asset-cache](https://github.com/DockYard/ember-service-worker-asset-cache)
- [ember-service-worker-cache-fallback](https://github.com/DockYard/ember-service-worker-cache-fallback)
- [ember-service-worker-cache-first](https://github.com/DockYard/ember-service-worker-cache-first)
- [ember-service-worker-index](https://github.com/DockYard/ember-service-worker-index)
- [ember-service-worker-prember](https://github.com/shipshapecode/ember-service-worker-prember)
- [ember-service-worker](https://github.com/DockYard/ember-service-worker) - Ember.js 的 Service Workers 的可插入方法。
- [ember-web-app](https://github.com/san650/ember-web-app) - 此 Ember.js 插件可帮助您配置和管理创建渐进式 Web 应用程序所需的 manifest.json 和元标记。

### 查询参数

- [ember-query-params-service](https://github.com/NullVoxPopuli/ember-query-params-service) - 您是否有*仅*解析查询参数的控制器？
- [ember-parachute](https://github.com/offirgolan/ember-parachute) - 改进了 Ember.js 的查询参数。
- [ember-href-to](https://github.com/intercom/ember-href-to) - {{link-to}} 的轻量级替代品。

### 实时

- [ember-cli-flash](https://github.com/poteto/ember-cli-flash) - ember-cli 的简单且高度可配置的 Flash 消息。

### 路由插件
- [ember-component-routes](https://github.com/wongpeiyi/ember-component-routes) - 直接从 Ember.js 中的路由渲染组件。
- [ember-redirect](https://github.com/thoov/ember-redirect) - 该插件旨在成为一种简单易用的方法，以最少的努力执行基于路由的重定向。
- [ember-router-scroll](https://github.com/dollarshaveclub/ember-router-scroll) - 滚动到顶部并保留浏览器历史记录滚动位置。

### 旋转变压器定制
- [ember-cli-extended-resolver](https://www.npmjs.com/package/ember-cli-extended-resolver) - 该插件允许修改默认文件结构以进行更多功能分组。

### 安全性

- [ember-can](https://github.com/minutebase/ember-can) - 适用于 Ember.js 应用程序的简单 [授权插件](http://ember-can.com)。
- [ember-permissions](https://github.com/Bagaar/ember-permissions) - Ember 应用程序的权限管理。

### 服务人员

- [ember-cli-workbox](https://github.com/BBVAEngineering/ember-cli-workbox/) - 离线缓存作为使用 Service Worker 的渐进增强。
- [ember-service-worker](https://github.com/DockYard/ember-service-worker) - Ember.js 的 Service Workers 的可插入方法。
- [ember-service-worker-index](https://github.com/DockYard/ember-service-worker-index) - 一个 Ember.js Service Worker 插件，用于缓存 index.html 文件。
- [ember-service-worker-asset-cache](https://github.com/DockYard/ember-service-worker-asset-cache) - 一个 Ember.js Service Worker 插件，用于缓存 Ember.js 应用程序的资源文件。
- [ember-service-worker-cache-first](https://github.com/DockYard/ember-service-worker-cache-first) - 一个缓存第一个 Ember.js Service Worker 插件。
- [ember-service-worker-cache-fallback](https://github.com/DockYard/ember-service-worker-cache-fallback) - 一个 Ember.js Service Worker 插件，当网络请求失败时，它会求助于缓存的后备版本。
- [ember-service-worker-emberfire-messaging](https://github.com/Matt-Jensen/ember-service-worker-emberfire-messaging) - Firebase Cloud Messaging Service Worker 对 Emberfire 应用程序的支持。
- [ember-service-worker-unregistration](https://github.com/GreatWizard/ember-service-worker-unregistration) - 一个 Ember.js 插件，可在禁用 ember-service-worker 时取消注册服务工作者。
- [ember-service-worker-request-chaos](https://github.com/maxfierke/ember-service-worker-request-chaos) - 类似于 Netflix 的 Chaos Monkey，但适用于 Ember.js SPA 的 API 请求。
- [ember-service-worker-project-entagled-registration](https://github.com/rwjblue/ember-service-worker-project-entagled-registration) - 该插件将与 ember-service-worker 一起使用，以确保所使用的 Service Worker 与项目正确配对。
- [ember-service-worker-cache-rendered](https://github.com/PrinceCornNM/ember-service-worker-cache-rendered) - Ember.js 服务工作者插件，用于将渲染的 html 存储在缓存中，对于 fastboot 非常有用。
- [ember-service-worker-update-notify](https://github.com/topaxi/ember-service-worker-update-notify) - 更新服务人员的通知。
- [ember-service-worker-enqueue](https://github.com/The-Don-Himself/ember-service-worker-enqueue) - 一个 Ember.js Service Worker 插件，用于捕获失败的突变请求，例如 POST、PUT、DELETE 并将它们排队以进行后台处理。
- [ember-service-worker-prember](https://github.com/shipshapecode/ember-service-worker-prember) - 一个 Ember.js Service Worker 插件，用于缓存每个 prember 路由的 index.html 文件。

### SSR/服务器端渲染

- [ember-fastboot](https://github.com/ember-fastboot/ember-cli-fastboot) - Ember.js 应用程序的服务器端渲染。
- [glimmer-ssr-test](https://github.com/josemarluedke/glimmer-ssr-test) - 使 Glimmer.js 应用程序在服务器中呈现。

### 静态网站生成器和 SEO

- [ember-meta](https://github.com/shipshapecode/ember-meta) - 为您的 Prember/Ember.js 博客设置元以支持 opengraph、微数据、Facebook、Twitter、Slack 等。
- [prember-rss-feed](https://github.com/shipshapecode/prember-rss-feed) - 为您的 Prember 站点发送 RSS 源。
- [prember](https://github.com/ef4/prember) - 在构建时使用 Fastboot 预渲染 Ember.js 应用程序。

### 造型

- [ember-cli-sass](https://github.com/aexmachina/ember-cli-sass) - 使用 node-sass 预处理 ember-cli 应用程序的文件，并支持 sourceMaps 和包含路径。

### 模板化

- [ember-template-component-import](https://github.com/crashco/ember-template-component-import) - 该插件允许您使用导入样式语法在模板文件中创建到组件的本地绑定。
- [ember-cli-jsx-templates](https://github.com/lifeart/ember-cli-jsx-templates) - TSX/JSX 支持 ember 模板。
- [Emblem.js](https://github.com/machty/emblem.js/) - Ember.js 友好，Handlebars.js 的缩进语法替代方案。

### 测试

- [ember-qunit-decorators](https://github.com/mike-north/ember-qunit-decorators) - 在 Ember.js 应用程序中使用 ES6 或 TypeScript 装饰器进行 QUnit 测试。
- [ember-cli-addon-tests](https://github.com/tomdale/ember-cli-addon-tests) - 用于在真实 Ember.js 应用程序上下文中测试 Ember CLI 插件的测试助手。
- [ember-cli-code-coverage](https://github.com/kategengler/ember-cli-code-coverage) - 使用 Istanbul 的 Ember 应用程序的代码覆盖率。
- [ember-cli-mirage](http://www.ember-cli-mirage.com/) - 使用符合 [JSON API](http://jsonapi.org/) 的客户端服务器构建、测试和演示您的应用程序。
- [ember-cli-mocha](https://github.com/ember-cli/ember-cli-mocha) - Mocha 和 Chai 测试 ember-cli 应用程序。
- [ember-cli-page-object](https://github.com/san650/ember-cli-page-object) - 这个 ember-cli 插件简化了验收和集成测试中页面对象的构建。
- [ember-cli-yadda](https://github.com/albertjan/ember-cli-yadda) - 为 ember-cli 应用程序编写 Cucumber 规范。
- [ember-concurrency-test-waiter](https://github.com/bendemboski/ember-concurrency-test-waiter) - 轻松启用测试服务员来执行 ember 并发任务。
- [ember-exam](https://github.com/trentmwillis/ember-exam) - 通过随机化、分割和并行化来运行测试，以获得漂亮的测试。
- [ember-percy](https://github.com/percy/ember-percy) - Ember.js 插件，用于使用 Percy 进行视觉回归测试。
- [ember-qunit](https://github.com/emberjs/ember-qunit) - Ember.js 的 QUnit 测试助手。
- [ember-test-friendly-error-handler](https://github.com/rwjblue/ember-test-friendly-error-handler) - 构建不会投入生产的可测试错误处理程序...
- [ember-test-selectors](https://github.com/simplabs/ember-test-selectors) - 在 Ember.js 测试中启用更好的元素选择器。
- [ember-test-setup](https://github.com/kellyselden/ember-test-setup) - 测试简写以减少重复。
- [ember-window-mock](https://github.com/kaliber5/ember-window-mock) - 使用 window global 作为可以在测试中模拟的 Ember.js 服务。
- [mirage-glue](https://github.com/izelnakri/mirage-glue) - 该程序读取您的 API 端点并创建响应或将响应附加到相关的 Mirage 固定文件。
- [ember-sinon](https://github.com/csantero/ember-sinon) - Ember CLI 插件添加了对 sinon.js 的支持。

### 文字

- [ember-text-measurer](https://github.com/cibernox/ember-text-measurer) - 简单的 Ember.js 服务，以高性能的方式测量字符串的宽度。


### 摇树
- [ember-cli-tree-shaker](https://github.com/kellyselden/ember-cli-tree-shaker) - 这是 Kelly Selden 和 Alex Navasardyan 的新的 tree-shaking 和代码分割工作的测试平台。

### 打字稿

- [ember-cli-typescript](https://github.com/typed-ember/ember-cli-typescript) - 在您的 Ember.js 应用程序中使用 TypeScript！
- [ember-typings](https://github.com/typed-ember/ember-typings) - ember.js 的 Typescript 类型定义。
- [ember-typescript-utils](https://github.com/happycollision/ember-typescript-utils) - 围绕 Typescript 和 Ember.js 构建的实用函数。


### 用户界面库

- [ember-bootstrap](http://www.ember-bootstrap.com/) - 提供原生 Ember.js 组件的集合，以 ember 友好的方式模仿原始 Bootstrap 插件和组件。
- [Frontile](https://github.com/josemarluedke/frontile) - Frontile 旨在提供构建一致且强大的 Ember.js 应用程序所需的乐高积木（组件、帮助器、修饰符和样式）。
- [ember-cli-uniq](https://github.com/uniplaces/ember-cli-uniq/) - 实现 Uniplaces 设计系统的 Ember.js 的默认组件。
- [ember-element-ui](https://github.com/aalasolutions/ember-element-ui) - 为 ember 提供 element-ui。
- [ember-elements](https://github.com/dunkinbase/ember-elements) - [Ember 中的 UI 工具包](https://dunkinbase.github.io/ember-elements/)
- [ember-ghost-casper-template](https://github.com/stonecircle/ember-ghost-casper-template) - Ghost 默认个人博客主题的静态站点版本。
- [ember-paper](https://github.com/miguelcobain/ember-paper) - Ember.js 的材料设计方法。
- [ember-radical](https://github.com/healthsparq/ember-radical) - 适用于您的 Ember.js 应用程序的轻量级、完全可访问的 DDAU 组件库。
- [游牧用户界面](https://github.com/hashicorp/nomad/tree/master/ui)
- [Semantic-UI-Ember](https://github.com/Semantic-Org/Semantic-UI-Ember) - 这是 Semantic-UI 模块的官方 Ember.js 库。
- [Flexi](https://github.com/html-next/flexi)

### 用户界面组件

- [ember-attacher](https://kybishop.github.io/ember-attacher/) - 工具提示和弹出窗口变得简单。
- [ember-burger-menu](https://github.com/offirgolan/ember-burger-menu) - 一个画布外侧边栏组件，包含使用 CSS 过渡的动画和样式集合。
- [ember-flatpickr](https://github.com/shipshapecode/ember-flatpickr) - 包装 Flatpickr 日期选择器的 Ember.js 插件。
- [ember-power-select](https://github.com/cibernox/ember-power-select) - 为 ember 构建的可扩展选择组件。
- [ember-basic-dropdown](https://github.com/cibernox/ember-basic-dropdown) - ember 应用程序所需的基本下拉菜单。
- [ember-drag-sort](https://github.com/kaliber5/ember-drag-sort) - 一个可排序的列表组件，支持多个和嵌套列表。
- [ember-perfect-scroll](https://github.com/imanhodjaev/ember-perfect-scroll) - 作为 Ember cli 插件的完美滚动组件。

### 用户体验

- [ember-onbeforeunload](https://github.com/jasonmit/ember-onbeforeunload) - 在路线之间转换或关闭窗口时调用逻辑。

### 虚拟现实

- [ember-vr](https://github.com/ember-vr)

### VS 代码插件

- [Ember Syntax](https://marketplace.visualstudio.com/items?itemName=dhedgecock.ember-syntax) - Ember.js 模板文件的语法突出显示以及带有标记模板的内联模板定义的语法突出显示！
- [Glimmer Templates Syntax for VS Code](https://marketplace.visualstudio.com/items?itemName=lifeart.vscode-glimmer-syntax) - Ember.js 的 Glimmer 语法高亮显示。
- [ember-language-server](https://github.com/emberwatch/ember-language-server) - Ember.js 项目的语言服务器协议实现。
- [unstable-ember-language-server](https://marketplace.visualstudio.com/items?itemName=lifeart.vscode-ember-unstable) - Ember.js 项目的语言服务器协议实现（不稳定，包括实验性功能）。
- [vscode-ember-colorizer](https://github.com/ciena-blueplanet/vscode-ember-colorizer) - VSCode 扩展，可对 Ember.js .hbs、控制器和路由文件进行着色/标记。
- [ember-module-snippets](https://github.com/candidmetrics/ember-module-snippets) - 使在 VSCode 中导入 Ember.js 模块变得轻而易举的片段。

### 原子插件

- [原子余烬片段](https://github.com/mattmcmanus/atom-ember-snippets)
 
### 维姆

- [neovim 的语言服务器不稳定](https://gist.github.com/meirish/639e6def0f352f63fef662dce3ca2f98)

### 网络组件

- [ember-cli-web-components](https://github.com/BBVAEngineering/ember-cli-web-components) - 在其他框架中使用您的 Ember.js 组件作为 Web 组件！
- [shadow-dom](https://github.com/knownasilya/ember-shadow-dom) - 为 Shadow DOM 根内部的组件编写模板。

### 网页包

- [glimmer-compiler-webpack-plugin](https://github.com/tomdale/glimmer-compiler-webpack-plugin)

### 奇怪的

- [ember-dynamic-render-template](https://github.com/miguelcobain/ember-dynamic-render-template) - 从模板字符串渲染 DOM。

### 资源

- [前端性能检查表](https://github.com/thedaviddias/Front-End-Performance-Checklist)
- [Ember.js 批准要求](https://gist.github.com/PoslinskiNet/2d7a05944ca3c468440a0faea153062b)

### 文章

- [Ember.js 构建性能基本指南](http://hangaroundtheweb.com/2018/02/an-elementary-guide-to-ember-build-performance/)
- [Ember.js 2019 路线图帖子](https://github.com/abhilashlr/emberjs2019-posts)
- [如何真正免费构建卓越的 Web 应用程序](https://medium.com/@devotox/zero-cost-web-apps-part-1-b2d6b46916f1)
- [开始使用 Glimmer-Native](https://codingitwrong.com/2019/06/26/glimmer-native-tutorial.html)
- [可嵌入 Ember.js 的案例](https://dev.to/dustinsoftware/the-case-for-embeddable-ember-4120)
- [2019 年 Ember.js 插件生态系统的状况](https://0xadada.pub/2019/06/17/essential-ember-addons/)
- [Ember.js 中的静态类型？](https://dev.to/jamesbyrne/static-types-in-emberjs-26b7)
- [Ember 如何启动？](https://hackernoon.com/how-does-ember-boot-5e1f9e7a1117)
- [我为自己制作的 Ember.js 测试指南](https://medium.com/@sarbbottam/the-ember-js-testing-guide-i-made-for-myself-c9a073a0c718)
- [使用 Lerna 管理多个 Ember.js 应用程序](https://cenchat.com/blog/2019/05/25/using-lerna-to-manage-multiple-ember-apps.html)
- [如何使用 ember-intl 翻译您的 Ember.js 应用程序](https://www.codeandweb.com/babeledit/tutorials/how-to-translate-your-ember-app-with-ember-intl)
- [使用 ember-animated 对列表重新排序](https://devjournal.balinterdi.com/using-ember-animated-to-resort-a-list/)
- [使用 Ember 并发限制 Ember 数据](https://medium.com/@mudflye/throttling-ember-data-with-ember-concurrency-ff30d804a1b)
- [Ember.js 中的动画和可预测数据加载](https://crunchingnumbers.live/2019/04/02/animation-and-predictable-data-loading-in-ember/)
- [让您已弃用的 CSS 脱颖而出](https://ondrejsevcik.com/deprecate-css/)
- [Ember.js ❤ 尖括号。迁移指南和备忘单](https://medium.com/@AveryBloom/ff309d6effdf)
- [Ember Octane 即将推出 - 第 1 部分：Native 类](https://www.pzuraq.com/coming-soon-in-ember-octane-part-1-native-classes/)
- [Ember Octane 即将推出 - 第 2 部分：尖括号语法和命名参数](https://www.pzuraq.com/coming-soon-in-ember-octane-part-2-angle-brackets-and-named-arguments/)
- [Ember Octane 即将推出 - 第 3 部分：跟踪属性](https://www.pzuraq.com/coming-soon-in-ember-octane-part-3-tracked-properties/)
- [Ember Octane 即将推出 - 第 4 部分：修饰符](https://www.pzuraq.com/coming-soon-in-ember-octane-part-4-modifiers/)
- [即将推出 Ember Octane - 第 5 部分：Glimmer 组件](https://www.pzuraq.com/coming-soon-in-ember-octane-part-5-glimmer-components/)
- [Ember Octane 更新：“@action”怎么了？](https://www.pzuraq.com/ember-octane-update-action/)
- [Ember Octane 更新：登陆装饰器](https://www.pzuraq.com/ember-octane-update-landing-decorators/)
- [Ember Octane 更新：异步观察者](https://www.pzuraq.com/ember-octane-update-async-observers/)
- [确认 Ember.js 中的操作](https://medium.com/@chrsmllr/confirming-actions-in-ember-362b19a0c01f)
- [Ember.js 中的异步计算属性](https://www.barelyknown.com/posts/async-computed-properties-in-ember)
- [Ember.js 原生类更新：2019 版](https://www.pzuraq.com/emberjs-native-class-update-2019-edition/)
- [Ember.js 路由钩子 — 完整外观](https://alexdiliberto.com/posts/ember-route-hooks-a-complete-look/)
- [理解 Ember.js 中的unknownProperty](https://wyeworks.com/blog/2015/11/24/understanding-unknownproperty-in-ember)
- [面向 Angular 开发人员的 Ember.js 简介](https://davidtang.io/2016/02/10/introduction-to-ember-for-angular-developers.html)
- [使用 VScode 调试 Ember.js](https://dev.to/michalbryxi/debugging-emberjs-with-vscode-2p5g)
- [使用 ember-cli-deploy 暂存环境](http://blog.firstiwaslike.com/staging-environments-with-ember-cli-deploy/)
- [Ember.js 中的高阶组件](https://www.chriskrycho.com/2018/higher-order-components-in-emberjs.html)
- [如何处理 Ember.js 中的异步属性](https://medium.com/macsour/how-to-handle-async-abilities-with-ember-can-22d90df056ed)
- [2018 年 8 个最热门的 Ember.js 面试问题](http://blog.honeypot.io/emberjs-interview-questions-2018/)
- [Ember.js 社区，认识 CodeSandbox！](https://medium.com/@mikenorth/ember-community-meet-codesandbox-10a43076b3fa)
- [使用 Octane 为您的 Ember.js 加油](https://clark.engineering/fuel-up-your-ember-with-octane-171c8dd13fd6)
- [Ember Octane – 下一个 Ember.js 版本中可以期待的一切](http://hangaroundtheweb.com/2018/08/ember-octane-everything-one-can-expect-in-the-next-ember-edition/)
- [Ember.js 中的延迟加载模块](https://medium.com/zonky-developers/lazy-loading-modules-in-emberjs-e4f880b15aa0)
- [Ember.js 中的组件模式](https://medium.com/macsour/components-patterns-in-ember-js-5e6fc6eea28f)
- [优化 Ember.js 模板](https://medium.com/square-corner-blog/optimizing-ember-templates-c479d26fe58e)
- [如何保持 ember.js 项目干净且结构良好](https://geeks.uniplaces.com/how-to-keep-your-ember-js-project-clean-and-well-structured-fbff040274de)
- [PWA 您的 Ember.js 应用程序](https://blog.201-created.com/pwa-your-ember-app-7ee8242f306e)
- [向 Ember.js 应用程序添加新的构建通知](https://medium.com/@jonpitch/adding-a-new-build-notification-to-an-ember-application-c657211289f6)
- [使 Ember.js 应用程序的 UI 转换对屏幕阅读器友好](https://engineering.linkedin.com/blog/2018/10/making-ember-applications--ui-transitions-screen-reader-friendly)
- [在应用程序之间共享 Ember.js 通用代码](https://dev.to/michalbryxi/share-emberjs-common-code-between-apps-1a7k)
- [未来的 Ember.js...今天！](https://dev.to/nullvoxpopuli/the-emberjs-of-the-future-today-12c)
- [使用 Ember.js 构建渐进式 Web 应用程序](https://madhatted.com/2017/6/16/building-a-progressive-web-app-with-ember)
- [Ember.js 中的动态组件布局](https://medium.com/freshworks-engineering-blog/dynamic-component-layout-in-ember-c9375c49126a)
- [将 PurgeCSS 与 Ember.js 结合使用](http://www.jurecuhalev.com/blog/2018/09/07/using-purgecss-with-ember-js/)
- [现代 Ember.js (2018)](https://codingitwrong.com/2018/08/16/modern-ember.html)
- [在 AWS 上自动化 Ember.js 应用程序部署](https://medium.com/@piotr.steininger/automating-ember-js-app-deployment-on-aws-feccc6d94828)
- [Django 和 Ember.js 全栈基础知识：连接前端和后端 — 第 1 部分](https://medium.com/@sunskyearthwind/django-emberjs-full-stack-basics-connecting-frontend-and-backend-part-1-beed8c386b08)
- [Ember Octane 提供您所期待的一切](http://hangaroundtheweb.com/2018/08/ember-octane-everything-one-can-expect-in-the-next-ember-edition)
- [根据用户的浏览器传送 Ember.js 捆绑包](https://sivasubramanyam.me/emberjs-shipping-different-bundles/)
- [到“attrs”或不到“attrs”](https://locks.svbtle.com/to-attrs-or-not-to-attrs)
- [嵌套组件和尖括号，一个偷偷摸摸的解决方案](https://locks.svbtle.com/nested-components-and-angle-brackets)
- [我如何向我的 Ember.js 应用程序添加白标主题](https://medium.com/@simeonberns/how-i-added-whitelabel-theming-to-my-ember-app-97bfca9e263a)
- [装饰指南：常用的 Ember.js 装饰器](https://codingitwrong.com/2018/08/21/decorating-guide.html)
- [了解 Ember 的解析器](https://dockyard.com/blog/2016/09/14/understanding-ember-s-resolver)
- [创建连接感知的 Ember.js 媒体组件](http://hangaroundtheweb.com/2018/08/creating-connection-aware-ember-media-components/)
- [雄心勃勃的 Chrome 扩展框架](https://envoy.engineering/a-framework-for-ambitious-chrome-extensions-b08d1f4b944d)
- [Ember.js 组件游乐场的自动发现](https://simplabs.com/blog/2018/06/05/ember-component-playground.html)

- [为 GDPR 配置 Ember.js Analytics](https://fullstackstanley.com/read/configuring-ember-js-analytics-for-gdpr)
- [使用 Ember.js 在 iOS 上拖放](https://dockyard.com/blog/2018/07/20/drag-and-drop-on-ios-with-ember)
- [缩短大型应用程序构建时间的技巧](https://discuss.emberjs.com/t/tips-for-improving-build-time-of-large-apps/15008)
- [错误处理](https://github.com/pixelhandler/ember-jsonapi-resources/wiki/Error-Handling)
- [构建并验证 Ember.js 3 应用程序](https://auth0.com/blog/build-and-authenticate-an-emberjs-3-application)
- [升级 Ember.js 应用程序所需了解的所有信息](https://medium.com/front-end-hacking/everything-you-need-to-know-to-upgrade-your-ember-js-app-including-ember-3-9de5e808dde0)
- [16 个值得学习的开源 Ember.js 项目](https://www.icicletech.com/blog/16-opensource-emberjs-projects-to-learn-from)
- [您必须了解的 5 个 Ember.js 基本概念](https://emberigniter.com/5-essential-ember-concepts/)
- [将 AWS Amplify 添加到 Ember.js 应用程序](https://itnext.io/adding-aws-amplify-to-an-ember-js-application-72683167c476)

- [对 Ember.js 的 Tom Dale 的采访](https://javascriptreport.com/interview-with-tom-dale/)
- [Ember.js 中使用液体火的动画](https://www.airpair.com/ember.js/posts/animations-in-emberjs-with-liquidfire)

- [很棒的 Ember.js 插件](https://www.codementor.io/gowiem/awesome-ember-addons-bwhiofit9)
- [使用 Ember Fastboot 和 Phoenix 构建高性能的实时 Web 应用程序](https://medium.com/peep-stack/building-a-performant-web-app-with-ember-fastboot-and-phoenix-part-1-fa1241654308)
- [使用 VSCode 调试 Ember.js 应用](https://medium.com/@minhdn/debug-ember-app-with-vscode-5f4fde511f9f)
- [在 Visual Studio Code 中调试 Ember.js 应用程序](http://blog.firstiwaslike.com/debugging-ember-js-application-in-visual-studio-code/)
- [使用 Ember.JS 进行部署：一个故事](https://blogs.library.ucsf.edu/ckm/2017/09/06/deploying-with-ember-js-a-story/)
- [不要混淆部署目标的环境](https://lolma.us/en/blog/class-and-attribute-bindings)
- [Ember.js 最佳实践：使用动态从属键计算属性](https://dockyard.com/blog/2015/10/23/ember-best-practices-dynamic-dependent-keys-for-computed-properties)
- [Ember.js 最佳实践：避免将状态泄漏到工厂中](https://dockyard.com/blog/2015/09/18/ember-best-practices-avoid-leaking-state-into-factories)
- [Ember CLI 插件文档：Ember.js 生态系统的共享文档](https://medium.com/build-addepar/ember-cli-addon-docs-shared-documentation-for-the-ember-ecosystem-6f29aa0cee87)
- [Ember 检查员 - 迄今为止的旅程](https://shipshape.io/blog/ember-inspector-the-journey-so-far/)
- [Medium 上的 Ember.js](https://medium.com/front-end-hacking/tagged/ember)
- [EmberCamp 模块统一更新](https://madhatted.com/2017/7/12/embercamp-module-unification-update)
- [Ember.js 中的骨架屏幕加载](https://emberway.io/skeleton-screen-loading-in-ember-js-2f7ac2384d63)
- [使用 Prember 和 Markdown 的静态博客](https://shipshape.io/blog/static-blogs-with-prember-and-markdown/)
- [Tom Dale on Ember.js and JavaScript Frameworks](https://www.infoq.com/interviews/tom-dale-ember) - 2013 年。
- [使用 ember-freestyle 作为组件游乐场](https://simplabs.com/blog/2018/01/24/ember-freestyle.html)
- [在 Ember CLI 中使用 npm 库](https://simplabs.com/blog/2017/02/13/npm-libs-in-ember-cli.html)
- [我们有一个新的 Ember.js 前端！](https://medium.com/@appaloosastore/we-have-a-new-emberjs-front-end-c7246e76cdbd)
- [关于从父模板传递动态类名和属性投标，您不知道的事情](https://lolma.us/en/blog/class-and-attribute-bindings)
- [你只能改变你能衡量的东西](https://blog.201-created.com/you-can-only-change-what-you-can-measure-6be8826503a7)

- [我如何向我的 Ember.js 应用程序添加白标主题](https://medium.com/@simeonberns/how-i-added-whitelabel-theming-to-my-ember-app-97bfca9e263a)
- [自定义 Ember Power Select](https://medium.com/life-at-kayako/customising-ember-power-select-3d570c7c4c0c)
- [深入了解 Ember.js 事件](https://medium.com/square-corner-blog/deep-dive-on-ember-events-cf684fd3b808)

- [总结 EmberConf 2021 的笔记集](https://alexdiliberto.com/posts/emberconf-2021-notes/)
- [总结 EmberConf 2020 的笔记集](https://alexdiliberto.com/posts/emberconf-2020-notes/)
- [总结 EmberConf 2019 的笔记集](https://alexdiliberto.com/posts/emberconf-2019-notes/)
- [EmberConf 2019 链接和注释](https://github.com/dknutsen/emberconf-2019)
- [总结 EmberConf 2018 的链接集合](https://github.com/nucleartide/emberconf-2018)
- [总结 EmberConf 2017 的链接集合](https://github.com/poteto/emberconf-2017)
- [总结 EmberConf 2016 的链接集合](https://github.com/poteto/emberconf-2016)
- [总结 EmberConf 2015 的链接集合](https://github.com/poteto/emberconf-2015)
- [EmberJS2018 博客文章和想法列表](https://github.com/zinyando/emberjs2018-posts)
- [雄心勃勃的框架的博客文章](https://blog.201-created.com/blog-post-for-an-ambitious-framework-d7e9248893fa)
- [基本 Ember 插件：2019 年 Ember 插件生态系统状况](https://0xadada.pub/2019/06/17/essential-ember-addons/)
- [将 Ember.js 应用程序部署到 Netlify](https://derricksdocs.com/deploying-an-emberjs-app-to-netlify/)
- [Ember 性能调整：优化构建时间线和捆绑包大小](https://abhilashlr.in/ember-performance-tweaks-part-1)
- [Ember 性能调整：优化资产](https://abhilashlr.in/ember-performance-tweaks-part-2)
- [Ember 性能调整：搜索引擎优化](https://abhilashlr.in/ember-performance-tweaks-part-3)

### Ember-Cli 文章
- [Ember-cli 指纹识别和动态资产](https://medium.com/@ruslanzavacky/ember-cli-fingerprinting-and-dynamic-assets-797a298d8dc6)
- [Ember-CLI 服务器的秘密：使用 Ember-CLI 的 Express 中间件](https://blog.201-created.com/secrets-of-the-ember-cli-server-bde80bb546dd)


### 为什么文章
- [纽约市规划实验室：为什么选择 Ember.js？](https://medium.com/nycplanninglabs/nyc-planning-labs-why-choose-ember-js-fe9ff75f4373)
- [为什么 DockYard 使用 Ember.js 构建](https://dockyard.com/blog/2017/10/04/why-dockyard-uses-ember)
- [Ember.js。你最好的选择。](https://medium.com/@alvincrespo/ember-your-best-bet-b5cd7275dc84)
- [为什么选择 Ember.js？](http://www.melsumner.com/blog/ember/why-ember/)
- [2019 年使用 Ember.js 的 6 个理由](https://selleo.com/blog/6-reasons-why-to-use-ember-in-2019)
- [Ember.js：我们的秘密武器](https://www.prototypal.io/blog/)
- [Ember.js 如何让我们专注于运输功能](http://blog.nightwatch.io/ember-js-shipping-features)
- [当你不应该选择 Ember.js 作为你的下一个前端工具时](https://medium.com/selleo/when-you-should-not-pick-emberjs-as-your-next-front-end-tool-203697c2e0f0)
- [2020 年从 React 迁移到 Ember](http://medium.com/@nowims/moving-from-react-to-ember-2020-86e082477d45)
- [基本 Ember 插件：2019 年 Ember 插件生态系统状况](https://0xadada.pub/2019/06/17/essential-ember-addons/)

### 快速入门文章
- [最简单的 Ember 数据 CRUD 教程](https://medium.com/ember-ish/the-simplest-possible-ember-data-crud-16eacee33ae6)
- [我在使用 Ember.js 时面临的挑战(d)](https://medium.com/@sarbbottam/challenges-i-face-with-ember-js-59bfba30416e)
- [在 Ember.js 中更容易。大概。](http://www.melsumner.com/blog/development/its-easier-in-ember-probably/)

### 文章 微光
- [Elm 应用程序的替代视图层](https://robots.thoughtbot.com/elm-glimmer)
- [使用 Glimmer 创建 Web 组件](https://simplabs.com/blog/2017/08/28/creating-web-components-with-glimmer.html)
- [使用 Glimmer.js 构建 PWA](https://simplabs.com/blog/2018/07/03/building-a-pwa-with-glimmer-js.html)
- [Glimmer VM：快速启动并保持快速](https://yehudakatz.com/2017/04/05/the-glimmer-vm-boots-fast-and-stays-fast/)
- [微光二元体验](https://engineering.linkedin.com/blog/2017/12/the-glimmer-binary-experience)
- [Glimmer.js：TypeScript 是怎么回事？](https://medium.com/@tomdale/glimmer-js-whats-the-deal-with-typescript-f666d1a3aad0)
- [Glimmer.js Application proposal](https://gist.github.com/tomdale/10fe9feeb84f2e4325f042839799bd9d) - 编译、渲染、SSR、补水。
- [Git 指南](https://github.com/glimmerjs/glimmer-vm/blob/master/guides/01-introduction.md)
- [像编程语言一样设计和实现 Glimmer](https://thefeedbackloop.xyz/designing-and-implementing-glimmer-like-a-programming-language/)
- [Glimmer：Ember.js 的极速渲染，第 1 部分](https://engineering.linkedin.com/blog/2017/03/glimmer--blazing-fast-rendering-for-ember-js--part-1)
- [Glimmer：Ember.js 的极速渲染，第 2 部分](https://engineering.linkedin.com/blog/2017/06/glimmer--blazing-fast-rendering-for-ember-js--part-2)
- [为什么我对 Glimmer.js 感到兴奋](https://hackernoon.com/why-im-excited-about-glimmerjs-3631bd0c95c4)
- [开始使用 Glimmer-Native](https://codingitwrong.com/2019/06/26/glimmer-native-tutorial.html)
- [更先进的 Glimmer VM 功能的当前状态如何？](https://discuss.emberjs.com/t/what-is-the-current-state-of-more-advanced-glimmer-vm-features/18114/4)
- [对 Glimmer 组件进行单元测试](https://timgthomas.com/2019/11/unit-testing-glimmer-components/)

### 文章 引擎
- [Ember 引擎中的 CSS](https://medium.com/@ynotdraw/css-in-ember-engines-230ef8d4cef8)
- [Enginification](https://simplabs.com/blog/2017/12/04/enginification.html)

### 文章 Ember-并发
- [采用 ember-concurrency 或：我如何学会停止担忧并热爱这项任务](https://engineering.linkedin.com/blog/2016/12/ember-concurrency--or--how-i-learned-to-stop-worrying-and-love-t)
- [异步或游泳：用 Ember 并发任务替换您的路线模型](https://medium.com/@AveryBloom/async-or-swim-replacing-your-route-models-with-ember-concurrency-tasks-5a230252893a)
- [ember-concurrency：解决许多你不知道的问题](https://emberway.io/ember-concurrency-the-solution-to-so-many-problems-you-never-knew-you-had-cce6d7731ba9)
- [PromiseProxyMixin：ember-concurrency 的纯 Ember 替代品](https://lolma.us/en/blog/promise-proxy-mixin/)
- [Ember.js 中的双任务路由](https://tritarget.org/#Two-Tasks%20Routes%20in%20Ember)

### 文章 ES6
- [Ember.js 中的 ES 类](https://medium.com/build-addepar/es-classes-in-ember-js-63e948e9d78e)

### 文章 TypeScript
- [ember-cli-typescript v2 测试版](https://www.chriskrycho.com/2018/ember-cli-typescript-v2-beta.html)
- [Ember Typescript 代码覆盖率 - 如何要点](https://gist.github.com/lifeart/5f75981d5f6262d1bfc4525aebfcf7d5)
- [类型知情设计](https://www.chriskrycho.com/2018/type-informed-design.html)
- [Typing Your Ember.js](https://www.chriskrycho.com/typing-your-ember.html) - 将 TypeScript 与 Ember.js 结合使用。
- [Ember.js、TypeScript 和类属性](https://www.chriskrycho.com/2018/ember-ts-class-properties.html)
- [将您的 Ember.js 项目设置为使用 TypeScript](http://www.chriskrycho.com/2017/typing-your-ember-part-1.html)
- [类属性 — 关于事物与 Ember.Object 世界有何不同的一些注释](https://www.chriskrycho.com/2018/typing-your-ember-update-part-2.html)
- [计算属性、操作、mixin 和类方法](https://www.chriskrycho.com/2018/typing-your-ember-update-part-3.html)
- [使用 Ember 数据以及服务和控制器注入改进](https://www.chriskrycho.com/2018/typing-your-ember-update-part-4.html)

### 文章 现代测试
- [使用来自 Ember-Sinon-QUnit 的赝品](https://medium.com/@mudflye/using-fakes-from-ember-sinon-qunit-c9fb7d4d9b1d)
- [使用 Docker 在 GitLab 中进行 Headless Ember.js 测试](https://medium.com/devopslinks/headless-ember-tests-in-gitlab-with-docker-fd5f05eef436)
- [让我的 Ember.js 测试套件速度提高 3 倍。关于海市蜃楼的故事](https://mlange.io/blog/making-tests-faster-mirage/making-tests-faster-mirage/)
- [在 Ember.js 中学习 TDD](https://learntdd.in/ember/)
- [基于故事的 BDD - 使用 Ember 进行测试的替代方法](https://www.kaliber5.de/en/blog/story-based-bdd-an-alternative-approach-to-testing-with-ember/)
- [Ember.js 计时器泄漏：测试基础设施中的坏苹果](https://engineering.linkedin.com/blog/2018/01/ember-timer-leaks)
- [测试助手：下一代](https://dockyard.com/blog/2018/01/18/test-helpers-the-next-generation)
- [我们如何在 10 分钟内测试 20 万行 Ember.js 应用程序。再次！](https://hackernoon.com/how-we-got-tests-for-200k-lines-ember-application-running-10-minutes-again-1fa7a4c5af2f)
- [Ember.js 测试中的弯曲时间](https://dockyard.com/blog/2018/04/18/bending-time-in-ember-tests)
- [Ember.js QUnit 简化](https://www.rwjblue.com/2017/10/23/ember-qunit-simplication/)
- [2018 年测试您的 Ember.js 应用程序](https://dockyard.com/blog/2018/03/29/testing-your-ember-application-in-2018)
- [现代 Ember.js 测试](https://dockyard.com/blog/2018/01/11/modern-ember-testing)
- [2018 年测试 Ember.js 应用程序](https://blog.201-created.com/testing-ember-applications-in-2018-4635ac241f00)
- [使用容器测试 Ember.js Mixins（和 Helpers）](https://www.chriskrycho.com/2016/testing-emberjs-mixins-with-a-container.html)
- [像数学家一样编写测试：第 1 部分](https://crunchingnumbers.live/2019/08/04/write-tests-like-a-mathematician-part-1/)
- [像数学家一样编写测试：第 2 部分](https://crunchingnumbers.live/2019/08/06/write-tests-like-a-mathematician-part-2/)
- [像数学家一样编写测试：第 3 部分](https://crunchingnumbers.live/2019/10/11/write-tests-like-a-mathematician-part-3/)
- [为您的 Ember 插件设置工作服](http://hangaroundtheweb.com/2020/05/setting-up-coveralls-for-your-ember-addons/)

### 文章 快速启动
- [如何将 Ember FastBoot 集成到 Firebase 的 Cloud Functions 中](https://cenchat.com/blog/2019/06/06/how-to-setup-ember-fastboot-in-cloud-functions-for-firebase.html)
- [Ember FastBoot + Google 应用引擎](https://pulletsforever.com/ember-fastboot-google-app-engine-1d38e1e3ffc2)
- [使用 ember-cli-deploy 部署 FastBoot 应用程序](https://www.effective-ember.com/blog/deploying-fastboot-apps-with-ember-cli-deploy)

### 有关数据的文章
- [使用 JSON API 管理 Ember 数据中的关系](https://www.mediasuite.co.nz/blog/managing-relations-ember-data-json-api/)
- [当belongsTo请求错误时创建默认记录](https://shipshape.io/blog/ember-data-belongs-to-find-or-create/)
- [Ember Data 中反对异步关系的案例](https://embermap.com/notes/83-the-case-against-async-relationships)
- [无需图论：Ember.js 和 GraphQL 实践](https://medium.com/kloeckner-i/ember-and-graphql-8aa15f7a2554)
- [离线数据并与 Ember-Orbit 同步](https://codingitwrong.com/2018/05/10/ember-orbit.html)
- [在 Ember.js 中内联存储数据](https://balinterdi.com/blog/inlining-store-data-in-ember-js/)
- [使用 Ember 数据从自定义 API 中提取元数据](https://thejsguy.com/2018/04/06/extracting-metadata-from-a-custom-api-with-ember-data.html)
- [与 Ember 数据的临时关系](https://shipshape.io/blog/ad-hoc-relationships-with-ember-data/)
- [Ember 数据记录数组反模式](https://gist.github.com/runspired/d86a76158050c4f573f5f26df1dab143)
- [有用的 Ember 数据助手](https://gist.github.com/runspired/96618af26fb1c687a74eb30bf15e58b6)
- [级联删除 Ember 数据中的关系](https://davidtang.io/2017/02/10/cascade-deleting-relationships-in-ember-data.html)
- [使用自定义适配器和序列化器将任何后端安装到 Ember 中](https://emberigniter.com/fit-any-backend-into-ember-custom-adapters-serializers/)

### 有关路由的文章
- [如何使用 this.route() 重置 Ember.js 路由器命名空间](http://toddsmithsalter.com/how-to-reset-the-route-namespace-with-this-route/)
- [Ember.js-路由器通配符/通配符路由](https://www.tutorialspoint.com/emberjs/route_glbng_rut.htm)
- [Ember.js.Route 将“/”重定向到“/my-own”](https://medium.com/ember-titbits/quest-4-ember-route-defaulting-to-my-own-f22b0dcb336f)

### Ember 文章中的纱线
- [Ember.js 和 Yarn 工作区](https://medium.com/square-corner-blog/ember-and-yarn-workspaces-fca69dc5d44a)

### 最佳实践

- [ember-best-practices](https://github.com/ember-best-practices)
- [Ember.js 调试流程图](https://www.mutuallyhuman.com/blog/2016/08/12/an-ember-debugging-flowchart)
- [Ember.js 中的内置输入助手：什么时候应该使用它们？](https://balinterdi.com/blog/built-in-input-helpers-in-ember-js-when-and-whether-they-should-be-used/)

### 很高兴知道

- [Codemods](https://caseywatts.com/2018/08/23/codemods.html)
- [使用遥测助手创建运行时辅助的 Codemod](http://hangaroundtheweb.com/2019/10/creating-runtime-assisted-codemods-using-telemetry-helpers/)

### 博客

- [lost-in-technology.com](https://www.lost-in-technology.com/blog/)
- [今天我学到了 / Ember.js](https://til.hashrocket.com/emberjs)
- [Ember.js 每日提示](http://www.emberdaily.com)
- [emberway.io](https://emberway.io/)
- [yehudakatz](https://yehudakatz.com/)
- [201-created.com](https://blog.201-created.com/)
- [airpair.com](https://www.airpair.com/ember.js)
- [alexdiliberto.com](https://alexdiliberto.com/)
- [balinterdi.com](https://balinterdi.com/blog/) - 巴林特·埃尔迪博客。
- [codeburst.io](https://codeburst.io/tagged/emberjs)
- [codementor.io](https://www.codementor.io/community/topic/emberjs)
- [dockyard.com](https://dockyard.com/blog/categories/ember)
- [emberigniter.com](https://emberigniter.com/articles/)
- [blog.embermap.com](https://blog.embermap.com)
- [engineering.linkedin.com](https://engineering.linkedin.com/blog/topic/ember)
- [hackernoon.com](https://hackernoon.com/tagged/ember)
- [lolma.us](https://lolma.us/en/blog)
- [madhatted.com](https://madhatted.com/)
- [medium.com/ember-ish](https://medium.com/ember-ish) - 适合初学者和中级开发人员的 Ember.js 基础知识。
- [netguru.co](https://www.netguru.co/blog/topic/ember-js)
- [programwitherik.com](https://www.programwitherik.com) - Ember.js 啧啧。
- [rwjblue.com](http://rwjblue.com/)
- [shipshape.io](https://shipshape.io/blog/)
- [simplabs.com](https://simplabs.com/blog/)
- [thejsguy.com](https://thejsguy.com/)

### 书籍

- [最短的 Ember.js 书](https://github.com/ember-learn/the-shortest-ember-book)
- [深入研究 Ember.js 运行循环](https://github.com/eoinkelly/ember-runloop-handbook)
- [开发 Ember.js Edge](https://gumroad.com/l/xlsx)
- [野外的 Ember 数据](https://leanpub.com/emberdatainthewild)
- [ember-cli 101](https://leanpub.com/ember-cli-101) - 作者：阿道夫·布伊斯。
- [Ember.js for Artisans](https://leanpub.com/emberforartisans) - 创建由 Laravel 支持的单页应用程序。
- [Ember.js in Action](http://manning.com/skeie/) - 作者：约阿希姆·哈根·斯基。
- [Frisby 教授的函数式编程基本足够指南](https://drboolean.gitbooks.io/mostly-adequate-guide-old/)
- [使用 Ember.js 进行摇滚乐](http://rockandrollwithemberjs.com/)
- [Ember.js 书（俄语）](https://leanpub.com/ember-book)
- [JavaScript 中实用、平衡的 FP](https://github.com/getify/Functional-Light-JS)

### 备忘单

- [API](https://emberjs.com/api/)
- [Glimmer.js](https://glimmerjs.com/)
- [guides](https://guides.emberjs.com/)
- [Ember Component Cheat Sheet](https://codingitwrong.com/2019/07/23/ember-component-cheat-sheet.html) - 前辛烷值

### 代码模组
- [ember-es6-class-codemod](https://github.com/scalvert/ember-es6-class-codemod) - 用于将 Ember.js 对象转换为 es6 原生类的 codemod-cli 项目。
- [ember-native-class-codemod](https://github.com/ember-codemods/ember-native-class-codemod) - 一个 codemod，用于使用装饰器将您的 ember 应用程序代码转换为原生 JavaScript 类语法！
- [ember-cli-mirage-faker-codemod](https://github.com/caseywatts/ember-cli-mirage-faker-codemod) - 此 codemod 旨在帮助从通过 ember-cli-mirage 导入 faker 过渡到直接从 faker 导入。
- [ember-mocha-codemods](https://github.com/Turbo87/ember-mocha-codemods) - ember-mocha 的 Codemod 脚本。
- [ember-module-migrator](https://github.com/rwjblue/ember-module-migrator) - 自动迁移新的 Ember.js 应用程序布局。
- [ember-qunit-codemod](https://github.com/rwjblue/ember-qunit-codemod) - 此 codemod 旨在自动将您的项目从 ember-qunit@2 的旧 moduleFor* 语法转换为新语法。
- [ember-test-helpers-codemod](https://github.com/simonihmig/ember-test-helpers-codemod) - Codemod 将您的 Ember.js 测试转换为使用 @ember/test-helpers。
- [es5-getter-ember-codemod](https://github.com/rondale-sc/es5-getter-ember-codemod) - 此 codemod 旨在自动将 get 和 getProperties 的用法转换为使用传统的对象点表示法。
- [qunit-dom-codemod](https://github.com/simplabs/qunit-dom-codemod) - 基本 codemod 自动将您的断言转换为 qunit-dom 断言。
- [test-selectors-codemod](https://github.com/lorcan/test-selectors-codemod) - 用于修复 ember-test-selectors testSelector 帮助程序弃用的代码模式。
- [ember-on-codemod](https://github.com/craigbilner/ember-on-codemod) - 替换使用 Ember.on。
- [ember-memory-leaks-codemod](https://github.com/rajasegar/ember-memory-leaks-codemod) - 用于修复 Ember.js 应用程序中内存泄漏的 codemod 集合。
- [ember-3x-codemods](https://github.com/rajasegar/ember-3x-codemods) - 一个包含一系列转换的 Codemod，用于解决 Ember.js 3.x 弃用问题。
- [ember-computed-getter-codemod](https://github.com/Alonski/ember-computed-getter-codemod) - Ember.js 计算的 Getter Codemod。

### 社区

- [Forum](http://discuss.emberjs.com/)
- [GitHub 问题](https://github.com/emberjs/ember.js/issues)
- [Reddit](https://www.reddit.com/r/emberjs/)
- [Slack](https://embercommunity.slack.com)
- [堆栈溢出](http://stackoverflow.com/questions/tagged/ember.js)
- [Telegram](https://t.me/ember_js)

### 贡献指南

- [如何为余烬时代做出贡献 - 第 1 部分](https://www.kennethlarsen.org/how-to-contribute-to-the-ember-times)
- [如何贡献 Ember 发布后 - 第 2 部分](https://www.kennethlarsen.org/how-to-contribute-ember-release-post)

### 课程

- [embermap.com](https://embermap.com)
- [Emberschool.com](https://www.emberschool.com)
- [embercasts.com](https://www.embercasts.com)
- [前端大师：高级 Ember.js 2.x - Mike North](https://frontendmasters.com/courses/advanced-ember-2/)
- [前端大师：Ember.js 2.x - Mike North](https://frontendmasters.com/courses/ember-2/)

### 发现

- [emberobserver](https://emberobserver.com/) - 余烬观察者.
- [emberjs.GitHub.io/rfcs/](https://emberjs.github.io/rfcs/) - Ember.js RFC。

### 余烬发布

- [Ember 3.10 Released](https://blog.emberjs.com/2019/05/21/ember-3-10-released.html) - 2019 年 5 月 21 日
- [Ember 3.11](https://blog.emberjs.com/2019/07/15/ember-3-11-released.html) - 2019 年 7 月 15 日
- [Ember 3.12](https://blog.emberjs.com/2019/08/16/ember-3-12-released.html) - 2019 年 8 月 16 日
- [Ember 3.13 (Octane Preview)](https://blog.emberjs.com/2019/09/25/ember-3-13-released.html) - 2019 年 9 月 25 日
- [Ember 3.14 (Octane Preview Cont.)](https://blog.emberjs.com/2019/11/18/ember-3-14-released.html) - 2019 年 11 月 18 日
- [Ember 3.15 "Octane" Released](https://blog.emberjs.com/2019/12/20/ember-3-15-released.html) - 2019 年 12 月 20 日
- [Ember 3.16](https://blog.emberjs.com/2020/02/12/ember-3-16-released.html) - 2020 年 2 月 12 日
- [Ember 3.17](https://blog.emberjs.com/2020/03/16/ember-3-17-released.html) - 2020 年 3 月 16 日
- [Ember 3.18](https://blog.emberjs.com/2020/05/05/ember-3-18-released.html) - 2020 年 5 月 5 日
- [Ember 3.19](https://blog.emberjs.com/2020/06/26/ember-3-19-released.html) - 2020 年 6 月 26 日
- [Ember 3.20](https://blog.emberjs.com/2020/07/29/ember-3-20-released.html) - 2020 年 7 月 29 日
- [Ember 3.21](https://blog.emberjs.com/2020/09/02/ember-3-21-released.html) - 2020 年 9 月 2 日
- [Ember 3.22](https://blog.emberjs.com/2020/10/20/ember-3-22-released.html) - 2020 年 10 月 20 日

### 示例
- [开源 Ember.js 应用程序列表](https://github.com/EmberSherpa/open-source-ember-apps)
- [ember-orbit 的简单联系人管理器演示应用程序](https://github.com/cerebris/peeps-ember-orbit)
- [API Docs](https://github.com/ember-learn/ember-api-docs) - 该应用程序旨在显示我们的版本化 API 文档。
- [guides-app](https://github.com/ember-learn/guides-app) - 替换 emberjs/guides 和 Ember.js 指南。
- [Builds](https://github.com/ember-learn/builds) - 这是 Ember.js 团队构建的应用程序，用于显示我们的各种发布渠道。
- [HospitalRun](https://github.com/HospitalRun/hospitalrun-frontend) - HospitalRun 的 Ember.js 前端 [hospitalrun.io](http://hospitalrun.io/)。
- [Rancher](https://github.com/rancher/ui) - [Rancher](http://rancher.com) 是 Kubernetes 的企业管理。
- [Super Rentals](https://github.com/ember-learn/super-rentals) - Super Rentals 是一个很好的入门项目，可以帮助您适应 Ember.js 的工作方式。
- [Travis CI](https://github.com/travis-ci/travis-web) - [Travis CI](https://travis-ci.org/) 的 Ember.js Web 客户端。
- [Vault](https://github.com/hashicorp/vault/tree/master/ui/app) - 管理秘密的工具（Hashicorp）。
- [ember-osf-web](https://github.com/CenterForOpenScience/ember-osf-web) - 开放科学框架的 Ember.js 前端。
- [ember-graphql-examples](https://github.com/chadian/ember-graphql-examples) - 在 Ember.js 中使用 GraphQL 的示例。
- [ember-rolodex](https://github.com/rtablada/ember-rolodex) - 快速入门和超级租金之间的 Ember.js 教程的示例。
- [ember-styleguide](https://github.com/ember-learn/ember-styleguide)
- [Ghost 管理客户端](https://github.com/TryGhost/Ghost-Admin)
- [emberclear](https://github.com/NullVoxPopuli/emberclear) - 加密聊天。没有历史。没有日志。  + MU 和 TS。
- [Ember.js 嵌套引擎示例应用程序 + Fastboot。](https://github.com/catz/eng-test)
- [Percy 的前端 Web 应用程序，使用 Ember.js 构建。](https://github.com/percy/percy-web)
- [Fire Tracker](https://github.com/SCPR/fire-tracker) - KPCC 用于跟踪和研究加州野火的工具。
- [skylines-project](https://github.com/skylines-project/skylines/tree/master/ember) - 实时跟踪、航班数据库和竞赛框架。
- [PIX](https://github.com/1024pix/pix-editor) - PIX。
- [ember-monorepo-demo](https://github.com/lennyburdette/ember-monorepo-demo)
- [documize.com](https://github.com/documize/community)
- [纽约市人口普查报告工具](https://github.com/NYCPlanning/labs-factfinder)
- [Medicine Inventory](https://github.com/aalasolutions/ember-medical-inventory) - 使用 Ember CLI、Corber.io、ember-element-ui 开发的示例应用程序。
- [octane-ecommerce](https://github.com/betocantu93/octane-ecommerce) - Ember Octane + FastBoot + Algolia + PayPal + Formspree ([s](https://docs.google.com/presentation/d/1YaG26Fj-tVjyFV8LvQJkfIH89-HYdkfHfhdRz3bC2-k/edit#slide=id.g56ccd9a7f0_0_33), [v](https://www.youtube.com/watch?v=KnkWs18V9dA&feature=youtu.be)、[d](https://octane-ecommerce.herokuapp.com/))。
- [Rust Package Registry](https://github.com/rust-lang/crates.io) - [crates.io](https://crates.io)
- [Ember.js RealWorld Implementation](https://github.com/gothinkster/ember-realworld) - Ember.js 代码库包含符合 RealWorld 规范和 API 的真实世界示例（CRUD、身份验证、高级模式等）。
- [野生汤姆斯特出现](https://github.com/scudco/tomsweeper)
- [用于使用 blockly 构建可视化编程编辑器的 ember 集成。](https://github.com/Program-AR/ember-blockly)
- [https://www.submarinecablemap.com/](https://www.submarinecablemap.com/)
- [https://music.apple.com/](https://music.apple.com/)
- [https://creator.emojible.store/](https://creator.emojible.store/)


### 例子 微光
- [breethe-client](https://github.com/simplabs/breethe-client) - 世界各地的空气质量数据。
- [Glimmeroids](https://github.com/t-sauer/Glimmeroids) - 使用 Glimmer.js 实现小行星。
- [glimmer-hn-pwa](https://github.com/mhadaily/glimmer-hn-pwa) - 由 Glimmer.js 提供支持的黑客新闻渐进式 Web 应用程序演示。
- [the-chosen](https://github.com/FLarra/the-chosen) - Glimmer.js 项目的创建是为了在我们的 scrum 每日会议期间更轻松地学习和决定谁是下一个分享状态的人。
- [glimmer_eats](https://github.com/James-Byrne/glimmer_eats) - 使用 Glimmer.js 构建的演示 PWA。
- [built-with-spaghetti](https://github.com/gordonbisnor/built-with-spaghetti) - 用 Spaghetti 构建的目的是作为网络艺术的门户。
- [glimmer-live-chat](https://github.com/rajasegar/glimmer-live-chat) - 使用 Glimmer.js 制作的实时聊天应用程序。
- [glimmer-synth](https://github.com/jimenglish81/glimmer-synth) - 使用 WebAudio 和 Glimmer.js 构建的合成器。
- [glimmer-js-online-offline-demo](https://github.com/thomasbrus/glimmer-js-online-offline-demo) - 示例 Glimmer.js 应用程序：在线/离线浏览器事件。
- [glimmer-qrious](https://github.com/c0urg3tt3/glimmer-qrious) - Glimmer.js 组件使用 QRious 库在网页中生成二维码。
- [glimmerjs-address-book-demo](https://github.com/ttdonovan/glimmerjs-address-book-demo) - 示例 Glimmer.js 应用程序 - AddressBook 演示。
- [glimmer-dashboard](https://github.com/JustInToCoding/glimmer-dashboard) - Glimmer.js 仪表板示例。
- [glimmer-redux-todo](https://github.com/bashmach/glimmer-redux-todo) - 使用 Glimmer.js 和 Redux 编写的 Todo 应用程序。
- [glimmer-pong](https://github.com/knownasilya/glimmer-pong) - 使用 Glimmer.js 和 SVG 编写的 Pong 游戏。
- [glimmer-material](https://github.com/cyk/glimmer-material) - 用于 Web 的 Material 组件的 Glimmer.js 包装器。
- [glimmer-of-life](https://github.com/trentmwillis/glimmer-of-life) - 使用 Glimmer.js 实现 Conway 的生命游戏。
- [vorfreude](https://github.com/chadian/vorfreude) - 当你不能等待但又不得不等待的时候。
- [endless-hoops](https://github.com/mtmckenna/endless-hoops) - 这是一款用 JavaScript/Canvas/Glimmer.js 编写的篮球游戏。
- [glimmer-hangman](https://github.com/BenSchoenmakers94/glimmer-hangman) - 著名游戏“Hangman”在 Glimmer.js 中的实现。


### 要点
- [在 Glimmer 中转发命名块](https://gist.github.com/tomdale/bedb77662b19529f59154ec55e2f4a21)
- [多命名块](https://gist.github.com/pzuraq/0c16d7baef7237b62dfd7529d1969344)
- [访问 Ember CLI 应用程序中的全局应用程序对象](https://gist.github.com/lifeart/fcdc59e2aa6a3c78457fecd57e578aa9)
- [表单的原则模型](https://gist.github.com/chriskrycho/48fa641eeb55217d4063592b411b1192)
- [ember-cli-advanced-proxy](https://github.com/bryanaka/ember-cli-advanced-proxy/blob/594e13cf2de386d8ea65dac88f643241f7a28363/index.js)
- [Ember.js VSCode 扩展列表](https://github.com/Alonski/ember-vscode-extensions)
- [Ember.js 包大小](https://gist.github.com/CodingItWrong/074d20c5468a9c340e15aa46e19a8221)
- [将库转换为 Ember CLI 插件](https://gist.github.com/kristianmandrup/ae3174217f68a6a51ed5)
- [开发插件和蓝图](https://gist.github.com/kristianmandrup/ae3174217f68a6a51ed5)
- [Ember.js + ESLint + Prettier + Ember Suave](https://gist.github.com/sarupbanskota/2394fc439e538239a073c39514a5aa55)
- [@listochkin/Ember.js 视频集（俄语/英语）](https://gist.github.com/listochkin/87e47cdbf986fb2e9905)
- [@rwjblue/ember_examples](https://gist.github.com/rwjblue/8816372)
- [@wycats/最初为 Ember.js 使用而构建的外部项目的一小部分样本，但设计为独立使用](https://gist.github.com/wycats/b58d56e5a47db4128a0a)
- [Ember.js 发布工具](https://gist.github.com/anulman/1e1da1d38178e7242d4701638bb29391)
- [Ember CLI es6 导入](https://gist.github.com/lifeart/949d867ba5f5455f8d955d9c9dc3610d)
- [Ember CLI Windows 加速](https://gist.github.com/lifeart/f436306a92f62610d65caaa699c17065)
- [如何使用 VS Code 调试 ember 应用程序](https://gist.github.com/nightire/38ad30167df55175853b20f025f46596)
- [组件到底是什么。](https://gist.github.com/begedin/98045c9b4df900bb4695)
- [“为什么选择 Ember.js”的想法](https://gist.github.com/MelSumner/971ba6b7a3c0b01a4cb3a43d3b962dac)
- [Ember.js 批准要求](https://gist.github.com/PoslinskiNet/2d7a05944ca3c468440a0faea153062b)

### 要点 Ember 数据
- [Mirage GraphQL 示例](https://gist.github.com/samselikoff/0e176a76e5be53cbb94e85020fc2b115)
- [余烬数据|有用的助手：推送删除、推送有效负载](https://gist.github.com/runspired/96618af26fb1c687a74eb30bf15e58b6)
- [余烬数据|复杂属性](https://gist.github.com/runspired/a4b56f7eefe9f8e04f7f0c83e4dfeaf0)
- [余烬数据|高级查询缓存](https://gist.github.com/runspired/dba8d8b4b0cde8d272ec368739460eba)
- [余烬数据|我们可以卸载已删除的记录吗？](https://gist.github.com/runspired/c92c8d066511083f8c171a33ae27dedf)
- [余烬数据|保留本地关系变化](https://gist.github.com/runspired/15387de0130478aae377d22b16021982)
- [余烬数据|推多态](https://gist.github.com/runspired/c5e86b006841fdab62bcddbc200f14e2)
- [余烬数据|有很多批量创建](https://gist.github.com/runspired/ad9a9bab3ee2dac11c2af8ee9e31b81d)
- [余烬数据|本地删除](https://gist.github.com/runspired/68ad36b99367946a32c470fe1504d0ee)
- [余烬数据|保存交易](https://gist.github.com/runspired/a607f4debabde043efd284a04b244974)
- [余烬数据|在适配器 Twiddle 中合并 findHasMany](https://gist.github.com/runspired/597ff8ccc4e9a06ff26c1754ba108fb3)
- [余烬数据|嵌套保存](https://gist.github.com/runspired/bc93f1c525837420f7b14d8cdcb2d36a)
- [余烬数据|级联删除](https://gist.github.com/runspired/e9ee98ccc89fad2a07d9c86f2541a763)

### 杂项

- [builtwithember](http://builtwithember.io/) - 由 Ember.js 提供支持的应用程序。
- [emberwatch](https://github.com/emberwatch) - Ember.js 内容的社区中心。

### 时事通讯

- [Ember Weekly](http://www.emberweekly.com/) - 最新的 Ember.js 新闻、提示和代码直接发送到您的收件箱。
- [Official Ember Blog](https://emberjs.com/blog/) - 重大公告，例如新的 Ember.js 版本发行说明或国情咨文信息。
- [statusboard](https://emberjs.com/statusboard/) - 状态板。
- [The Ember Times](https://the-emberjs-times.ongoodbits.com/) - 来自 Ember.js 学习团队的更新。

### 播客

- [embermap](https://embermap.com/topics/the-embermap-podcast)
- [emberweekend](https://emberweekend.com/episodes)

### 沙箱
- [Ember Twiddle](https://ember-twiddle.com/) - 用于多个文件的 Ember.js Twiddle，可让您将工作保存在 GitHub 中。
- [Ember @ Glitch](https://ember.glitch.me/) - Glitch.me 与 Ember.js。
- [Ember @ CodeSandbox](https://codesandbox.io/s/github/mike-north/ember-new-output) - CodeSandbox 与 Ember.js。
- [Ember Octane @ CodeSandbox](https://codesandbox.io/s/octane-starter-li841) - Ember Octane CodeSandbox 模板。

### 截屏视频

- [BuildLab：Ember.js 已确定的截屏视频。](https://www.youtube.com/channel/UC1ssGKlQh87Ubyuv1lEiY0g)
- [Ember Screencasts](https://www.emberscreencasts.com/) - 为忙碌的开发人员提供的每周截屏视频。
- [EmberCasts](http://www.embercasts.com/) - 目前处于中断状态，而作者正在开发 Handlebars 的下一版本。
- [EmberWatch - Screencasts](http://emberwatch.com/screencasts.html) - Ember.js 截屏视频的集合。
- [社区组应用程序 - 在 Ember CLI Mirage 中创建记录（第 2a 部分）](https://www.youtube.com/watch?v=4iqNcTUXurY)
- [社区组应用程序 - 在 Ember CLI Mirage 中创建记录（第 2b 部分）](https://www.youtube.com/watch?v=eAI1LxgSOqw)
- [社区组应用程序 - 在 Ember CLI Mirage 中调试关系（第 3 部分）](https://www.youtube.com/watch?time_continue=1&v=DRzPJ4RMT0w)

### 幻灯片

- [30 Days Of Ember](https://slides.com/poslinski_net/30-days-of-ember) - 大卫·波斯林斯基。
- [NaNoWriMo: How can Ember help you write a novel](https://slides.com/emma_be/nanowrimo-ember#/) - @艾玛德莱科勒。
- [Slides from Ember JS Berlin talk, Design Patterns in Ember](https://github.com/chadian/ember-js-berlin-design-patterns) - 作者：@chadian。
- [Rainy Day Ember Data](https://speakerdeck.com/tonywok/rainy-day-ember-data) - 托尼·施奈德（@tonywok）。
- [Building Realtime Apps with Ember.js and WebSockets](https://www.slideshare.net/BenLimmer/building-realtime-apps-with-emberjs-and-websockets) - 本·利默。
- [Deploying a Location-Aware Ember Application](https://www.slideshare.net/BenLimmer/deploying-a-locationaware-ember-application) - 本·利默。
- [Developing Desktop Apps with Electron & Ember.js - FITC WebU2017](https://www.slideshare.net/anulman/developing-desktop-apps-with-electron-emberjs-fitc-webu2017) - 艾丹·努尔曼。
- [使用 Electron 和 Ember.js 开发桌面应用程序](https://www.slideshare.net/fitc_slideshare/developing-desktop-apps-with-electron-emberjs)
- [Ember addons, served three ways](https://www.slideshare.net/mikelnorth/ember-addons-served-three-ways) - 迈克·诺斯.
- [Ember At Scale](https://www.slideshare.net/chadhietala/ember-at-scale) - 查德·希塔拉，LinkedIn。
- [EmberConf 2015 – Ambitious UX for Ambitious Apps](https://www.slideshare.net/sugarpirate/emberconf-2015-ambitious-ux-for-ambitious-apps) - 劳伦·伊丽莎白·谭。
- [EmberConf 2016 – Idiomatic Ember: Finding the Sweet Spot of Performance & Productivity](https://www.slideshare.net/sugarpirate/emberconf-2016-idiomatic-ember-finding-the-sweet-spot-of-performance-productivity) - 劳伦·伊丽莎白·谭。
- [Fun with Ember 2.x Features](https://www.slideshare.net/BenLimmer/fun-with-ember-2x-features) - 本·利默。
- [How do I Even Web App](https://www.slideshare.net/lydiaguarino/how-do-i-even-web-app) - Lydia Guarino 介绍使用 Ember CLI 进行 Web 编程。
- [Rapid prototyping and easy testing with ember cli mirage](https://www.slideshare.net/KrzysztofBiaek1/rapid-prototyping-and-easy-testing-with-ember-cli-mirage) - 克日什托夫·比亚莱克。
- [Start Me Up - Building an MVP with EmberJS, Firebase and Material Design](https://www.slideshare.net/PickNBook/start-me-up-building-an-mvp-with-emberjs-firebase-and-material-design) - 布伦丹·奥哈拉.
- [Upgrading Ember.js Apps](https://www.slideshare.net/BenLimmer/upgrading-emberjs-apps) - 本·利默。

### 风格指南

- [ember-styleguide](https://github.com/ember-learn/ember-styleguide)
- [软件层 Ember.js](https://github.com/softlayer/ember-style-guide)
- [Netguru Ember.js](https://github.com/netguru/ember-styleguide)
- [DockYard Ember.js](https://github.com/DockYard/styleguides/blob/master/engineering/ember.md)
- [JavaScript 风格指南](https://github.com/DockYard/styleguides/blob/master/engineering/javascript.md)

### 工具

- [Ember Data Sails Adapter](https://github.com/bmac/ember-data-sails-adapter) - 用于 Sails.js 套接字的 Ember 数据适配器。
- [Ember Data WordPress Adapter](https://github.com/HeyHumanAgency/Ember-Data-WordPress) - 用于 WordPress JSON API 的 Ember 数据适配器。
- [Ember Gist](http://ember-gist.joostdvrs.com/) - 使用 GitHub Gist 演示 Ember CLI'eque 应用程序。
- [Ember Inspector](https://github.com/emberjs/ember-inspector) - 向 Chrome 或 Firefox 开发者工具添加 Ember.js 选项卡，允许您检查应用程序中的 Ember.js 对象。 - 官方维护。
- [Ember Perf](https://github.com/mike-north/ember-perf) - 在 ember.js 应用程序中测量用户感知的性能数据。
- [ember-cli-diff](http://www.ember-cli-diff.org/) - 一个简单的工具，可以查看新的 Ember 应用程序之间的差异。
- [ember-cli](https://ember-cli.com/) - 用于雄心勃勃的 Web 应用程序的命令行界面。
- [ember-data-model-maker](https://andycrum.github.io/ember-data-model-maker/) - 用于制作 ember 数据模型和有效负载示例的 UI。
- [Glimmer Playground](https://try.glimmerjs.com/) - 一个 Glimmer.js 游乐场。
- [mber](https://github.com/izelnakri/mber) - Ember CLI 替换。目前是阿尔法。
- [remote-inspector](https://github.com/joostdevries/ember-cli-remote-inspector) - 允许您使用 websocket 检查通过网络在不同设备/浏览器上运行的应用程序。
- [Ember Unused Components](https://github.com/vastec/ember-unused-components) - 该脚本搜索 Ember 项目中未使用的组件

### 教程

- [如何快速学习EmberJS](https://medium.com/ember-ish/how-to-learn-emberjs-in-a-hurry-c6fdeae256a0)
- [Discover Ember 2](https://www.ludu.co/course/ember) - 了解如何从头开始构建 Twitter 克隆。
- [Ember Components: A Deep Dive](http://code.tutsplus.com/tutorials/ember-components-a-deep-dive--net-35551) - 详细了解 Ember.js 组件的使用。
- [Ember runloop handbook](https://github.com/eoinkelly/ember-runloop-handbook) - 深入研究 Ember.js 运行循环。
- [Ember with Phoenix (AKA The PEEP Stack)](https://medium.com/peep-stack) - 开发 Ember.js 前端以及兼容 [JSON API](http://jsonapi.org/) 的 [Phoenix](http://www.phoenixframework.org/) 后端。
- [Getting into Ember.js](http://code.tutsplus.com/tutorials/getting-into-emberjs--net-30709) - 由五部分组成的 Ember 入门课程。
- [Getting Started with Ember.js using Ember CLI](https://thetechcofounder.com/getting-started-with-ember/) - 使用 Ember CLI 构建 Todo 应用程序。
- [yoember.com/](http://yoember.com/) - Ember.js 教程 - 从初学者到高级。
- [build-pacman](http://www.jeffreybiles.com/build-pacman)

### 推特

- [EmberJS](https://twitter.com/emberjs)
- [余烬时报](https://twitter.com/embertimes)
- [余烬观察](https://twitter.com/EmberWatch)
- [余烬周刊](https://twitter.com/EmberWeekly)

- [汤姆·戴尔](https://twitter.com/tomdale)
- [耶胡达·卡茨](https://twitter.com/wycats)
- [梅兰妮·萨姆纳](https://twitter.com/melaniersumner)
- [珍·韦伯](https://twitter.com/jwwweber)
- [罗伯特·杰克逊](https://twitter.com/rwjblue)
- [斯特凡·彭纳](https://twitter.com/stefanpenner)
- [马修·比尔](https://twitter.com/mixonic)
- [克里斯·索伯恩](https://twitter.com/Runspired)
- [克里斯·加勒特](https://twitter.com/pzuraq)
- [亚历克斯·纳瓦萨迪安](https://twitter.com/twokul)
- [伊戈尔·泰尔齐奇](https://twitter.com/terzicigor)
- [丹·格布哈特](https://twitter.com/dgeb)

- [亚历克斯·斯佩勒](https://twitter.com/alexspeller)
- [萨姆·塞利科夫](https://twitter.com/samselikoff)
- [埃里克·布林](https://twitter.com/ebryn)
- [加文·乔伊斯](https://twitter.com/gavinjoyce)
- [瑞安·多伦多](https://twitter.com/ryantotweets)
- [巴林特·埃尔迪](https://twitter.com/baaz)
- [卢克·梅利亚](https://twitter.com/lukemelia)

### 视频

- [使用 Ember 动画和插件内部：Ember 并发 – Ember 纽约，2019 年 5 月](https://www.youtube.com/watch?v=JbxaVHQFou0)
- [Ember.js 教程：20 分钟内构建一个绘画游戏](https://www.youtube.com/watch?v=N4KrBuO0RRE)
- [Jacob Bixby 的 Ember-cli In-Repo 插件](https://www.youtube.com/watch?v=VYrMs1Zzpqs)
- [与 Chris Ng 一起大规模维护 Ember 应用程序](https://www.youtube.com/watch?v=gyGZHydh0Hw&feature=em-uploademail)
- [Jackie Luo：从 React 到 Ember：现代比较](https://www.youtube.com/watch?v=7yxr4iBrZsw)
- [Ember 旧金山 Square 聚会，2018 年 10 月](https://www.youtube.com/watch?v=ulWhjL0Aj5s)
- [The Future of Ember js](https://www.youtube.com/watch?v=4b9VbB2bnfw) - 基于 EmberConf 2018 演示文稿的 Ember.js 即将发生的更改摘要。
- [Ember：未来十年 |汤姆·戴尔 | 2018 年芝加哥 EmberCamp](https://www.youtube.com/watch?v=9cseB2xoT-0)
- [停止编码：您存在产品差距 |萨姆·塞利科夫 | 2018 年芝加哥 EmberCamp](https://www.youtube.com/watch?v=fYHgyIlGttk)
- [默认商店的注意事项 - Ember London - 2018 年 9 月](https://www.youtube.com/watch?v=EcKaDu0xo_A)
- [2019 年余烬节](https://www.youtube.com/playlist?list=PLN4SpDLOSVkT0e094BZhGkUnf2WBF09xx)
- [2018 年余烬节](https://www.youtube.com/watch?v=oRzmDobMZ_Q&list=PLN4SpDLOSVkSB9034lDNdP1JoNBGssax9)
- [2014 年余烬节](https://www.youtube.com/watch?v=z4oxa-UR7oA&list=PLN4SpDLOSVkSbGTLohVaYGDB8hxWxGPBA)
- [全球 Ember 聚会](https://vimeo.com/globalembermeetup)
- [余烬@Netflix](https://pusher.com/sessions/meetup/emberfest/ember-netflix)
- [大规模的 Ember 引擎](https://pusher.com/sessions/meetup/ember-london/ember-engines-at-scale)
- [Ember 测试记录仪](https://pusher.com/sessions/meetup/ember-london/ember-test-recorder)
- [Jacob Bixby 的 Ember-cli In-Repo 插件](https://www.youtube.com/watch?v=VYrMs1Zzpqs)
- [ember-content-placeholders](https://pusher.com/sessions/meetup/emberfest/ember-content-placeholders)
- [2020 年 Ember.JS](https://pusher.com/sessions/meetup/emberfest/emberjs-in-the-year-2020)
- [EmberConf 2014](https://www.youtube.com/playlist?list=PLE7tQUdRKcyaOyfBnAndJxQ9PNVmKva0d) - EmberConf 2014 的会议视频。
- [EmberConf 2015](https://www.youtube.com/playlist?list=PLE7tQUdRKcyacwiUPs0CjPYt6tJub4xXU) - EmberConf 2015 的会议视频。
- [EmberConf 2016](https://www.youtube.com/playlist?list=PL4eq2DPpyBblc8aQAd516-jGMdAhEeUiW) - EmberConf 2016 的会议视频。
- [EmberConf 2017](https://www.youtube.com/playlist?list=PL4eq2DPpyBbna_5fLPqOqensqSZpGf-hT) - EmberConf 2017 的会议视频。
- [EmberConf 2018](https://www.youtube.com/watch?v=NhtpXs0ZtUc&list=PL4eq2DPpyBbnjD5iLp55as9OvIdEDI_Kt) - EmberConf 2018 的会议视频。
- [EmberConf 2019](https://www.youtube.com/playlist?list=PLE7tQUdRKcyYWLWrHgmWsvzsQBSWCLHYL) - EmberConf 2019 的会议视频。
- [EmberConf 2020](https://www.youtube.com/playlist?list=PL4eq2DPpyBbkC03mdzlyej6tcbEqrZK8N) - EmberConf 2020 的会议视频。
- [ReactiveConf 2017 - Tom Dale：Glimmer VM 的秘密](https://www.youtube.com/watch?v=nXCSloXZ-wc)
- [反应会议 2017](https://youtu.be/62xd25kEZ3o?t=27618)
- [Tim Thomas - 使用 Ember.js 构建 Electron 应用程序](https://www.youtube.com/watch?v=ER1V_u0N7u4)
- [Tom Dale 于 2018 年谈静态分析、Upstreaming Glimmer 和 Ember](https://embermap.com/topics/the-embermap-podcast/tom-dale-on-static-analysis-upstreaming-glimmer-and-ember-in-2018)
- [Tom Dale 谈论 EmberJS](https://www.slideshare.net/LinkedInPulse/tom-dale-ember-javascript-emberjs-linkedin)
- [在 Ember 中使用 TypeScript](https://pusher.com/sessions/meetup/ember-london/using-typescript-in-ember)
- [Web App Performance & Ember.js](https://www.youtube.com/watch?v=BelKk7dvA1A) - Web 应用程序性能和 Ember.js。
- [为什么 Ember CLI 使用西兰花](https://embermap.com/topics/intro-to-broccoli/why-ember-uses-broccoli)
- [在 glitch.com 上开发 ember 应用程序](https://www.youtube.com/watch?v=uhXA6ECaknw)
- [Chris Krycho：TypeScript 和 Ember js - 为什么以及如何？](https://www.youtube.com/watch?v=fFzxbBrvytU)
- [Isaac Lee：将 D3 与 Ember 结合使用](https://www.youtube.com/watch?v=vD7H9O--tu4)
- [开源直播 - 罗伯特·杰克逊 (Robert Jackson) 和克里斯·曼森 (Chris Manson) 在 ember-cli 上结对](https://www.youtube.com/watch?v=rsftBMGOfyo)
- [EmberJS 中必须有附加组件 - Dawid Pośliński](https://www.youtube.com/watch?v=IprfNT0xbrI)
- [使用 API 服务构建现代应用程序 - Ember 聚会 2018 年 8 月 21 日](https://www.youtube.com/watch?v=VMnzGJ4PN0s)
- [如何改进你的测试？ ——帕韦乌·库维克](https://www.youtube.com/watch?v=rs71sx5IZ-U&t=0s&list=PLxt6MasYELQ5W3y8rwGa98GsyMBdhr_cp)
- [可选和即将推出的功能 - Michał Staśkiewicz](https://www.youtube.com/watch?v=4XokzPT4rgg&t=0s&list=PLxt6MasYELQ5W3y8rwGa98GsyMBdhr_cp)
- [与 Ember/Glimmer 的混合应用程序](https://pusher.com/sessions/meetup/emberfest/hybrid-apps-with-emberglimmer)
- [实际有效的高效前端测试驱动开发](https://www.youtube.com/watch?v=63Ya91f8W-8)
- [EmberCamp 2018](https://www.youtube.com/watch?v=0ziETDm1QTI&list=PL4eq2DPpyBbm-vTgHMdBjUi1Qd5GiRIfW) - 2018 年 EmberCamp 会议视频
- [EmberCamp 2019](https://www.youtube.com/watch?v=a1HALof3r5M&list=PL4eq2DPpyBbmSKZLCqzMqdtpedlGrDQuc) - 2019 年 EmberCamp 会议视频
- [Ember.js：纪录片](https://www.youtube.com/watch?v=Cvz-9ccflKQ&vl=en)
- [Ember.js: The Documentary (Русская версия)](https://www.youtube.com/watch?v=7Ym2ADCn77Q) - 俄语版本
- [GraphQL：纪录片](https://www.youtube.com/watch?v=783ccP__No8&vl=en)
- [GraphQL: The Documentary (Русская версия)](https://www.youtube.com/watch?v=i_rsfHMF3x4) - 俄语版本
- [Ember 和 GraphQL：一个简单示例](https://www.youtube.com/watch?v=YxRvXgDIHW8)
- [Ember Octane 直播：构建鼓机](https://www.youtube.com/watch?v=5znpEiwHpL4)
- [Tracking in the Glimmer VM](https://www.youtube.com/watch?v=BjKERSRpPeI) - Chris Garrett 讨论 Ember 中的跟踪工作原理
- [Commit Porto '19：通过炒作周期蓬勃发展：Ember.js 故事 (Ricardo Mendes)](https://www.youtube.com/watch?v=ECkbVa0iC4k)
- [Animating Across Routes with Ember Animated](https://www.youtube.com/watch?v=O4Mt-dDqkk0) - EmberMap 视频添加跨路线过渡动画
- [Creating an Ember Application](https://www.youtube.com/watch?v=R2JdP4lb5Xw) - Ember 即将推出的系列中的第一个
- [Ember 和 GraphQL：一个简单示例](https://www.youtube.com/watch?v=YxRvXgDIHW8)
- [Stef & Rob：我们还需要内置输入组件吗？](https://www.youtube.com/watch?v=c0Rl6o9wLX0) Stefan Penner 和 Robert Jackson 争论内置输入组件
- [Ember Octane - Great For Beginners](https://www.youtube.com/watch?v=iTPFsXcTAaY&feature=youtu.be) - 您只需编写 HTML 和 CSS 即可轻松使用 Ember Octane
- [另一个测试运行者 作者：Kelly Sheldon @ Ember London](https://www.youtube.com/watch?v=HYwXL3f854Y&list=PL4eq2DPpyBbmvEzhyW9fhMzlctxwrn8JM&index=1)


### YouTube 频道

- [阿姆斯特丹 Ember.js](https://www.youtube.com/channel/UCx9sVlEZLOKxw8OGCtoqULw)
- [波士顿余烬](https://www.youtube.com/channel/UCp_L_YjmXTKR4Q2fg1XahsA)
- [丹佛余烬](https://www.youtube.com/channel/UCsy4OVL_kNXsxr0a5LNKWpw)
- [余烬视频](https://www.youtube.com/channel/UCMmzJ82sCmooDdtzVY8FxEA)
- [EmberJS 钦奈](https://www.youtube.com/channel/UC-PzS1OA64zFD2kt3hwfGTA)
- [Ember.js 都柏林](https://www.youtube.com/channel/UCQeD0i9ltSV1aOfX6FGeiOA)
- [EmberATX](https://www.youtube.com/channel/UCl7qY85b7KLJV3xnn1Xh_Cw)
- [EmberJSSeattleMeetup](https://www.youtube.com/channel/UC_EzRy1fCQPRPOD-uqk-E5w)
- [EmberSchool](https://www.youtube.com/channel/UCntNIA2acwPDIY77bX2uLmw)
- [EmberSherpa](https://www.youtube.com/user/EmberSherpa/videos)
- [见面会：伦敦](https://www.youtube.com/playlist?list=PL4eq2DPpyBbmvEzhyW9fhMzlctxwrn8JM)
- [硅谷 Ember.js 聚会](https://www.youtube.com/channel/UCi12gVD9jIDwJLVTNnKvhlw)
- [所以余烬 2017](https://www.youtube.com/watch?v=UpUtVGW43hY&list=PLXOJZupxSq204IxtG80UfIW-gU0IxAScY)
- [邪恶的好余烬 2016](https://www.youtube.com/playlist?list=PLXOJZupxSq22zfW2KVnXFgLbu--DA7q0G)
- [我可以问一个问题吗](https://www.youtube.com/channel/UCyErLHzPqLAkL1F-SivFDcA)

### YouTube 播放列表
- [2018 年伦敦 Ember 展会](https://www.youtube.com/watch?v=EcKaDu0xo_A&list=PL8xuokhAnn4rUlol6aspg-VYetu9BLsWV)
- [对讲机截屏视频](https://www.youtube.com/playlist?list=PLpAr6J-75N27wctNT70O0lubaGTPjwi1L)
- [Ember.js tutorial for beginners in 2020](https://www.youtube.com/watch?v=eQUvN9Ujs1s&list=PLk51HrKSBQ88wDXgPF-QLMfPFlLwcjTlo) - Shawn Chen 的 10 部分系列

## 许可证

[CC0](./许可证)
