# 很棒的角度 [![Awesome](https://awesome.re/badge.svg)](https://github.com/sindresorhus/awesome)

<p align="center">
  <a href="https://patrickjs.com" target="_blank">
    <img src="/media/new/awesome-angular.png" alt="Awesome Angular" />
  </a>
</p>

> 标志由[SAWARATSUKI]设计(https://github.com/SAWARATSUKI/KawaiiLogos)

这是 Angular 框架的精彩列表，它包含 Angular 生态系统中适合所有开发人员的有趣的库。缺少什么吗？ [欢迎 PR！](https://github.com/PatrickJS/awesome-angular/edit/gh-pages/README.md)

> 由 [@jdegand](https://github.com/jdegand) 和 [@patrickjs](https://github.com/patrickjs) 维护的存储库

当前 Angular 版本：[![npm 版本](https://badge.fury.io/js/%40angular%2Fcore.svg)](https://www.npmjs.com/~angular)

## 内容

* [Angular](#angular)
  * [官方资源](#official-resources)
  * [Builders](#builders)
  * [CLI工具](#cli-tools)
  * [Deployment](#deployment)
  * [桌面应用程序](#desktop-applications)
  * [更新角度](#updating-angular)
* [角脉冲](#angular-pulse)
  * [Community](#community)
  * [Newsletters](#newsletters)
  * [Podcasts](#podcasts)
  * [Bluesky](#bluesky)
  * [X 上的 Angular 团队](#angular-team-on-x)
  * [X 上的 Angular 专家](#angular-experts-on-x)
  * [X 方面的 Google 开发者专家](#google-developer-experts-on-x)
* [学习资源](#learning-resources)
  * [Blogs](#blogs)
  * [Books](#books)
  * [认证计划](#certification-programs)
  * [备忘单](#cheat-sheets)
  * [Exercises](#exercises)
  * [Training](#training)
  * [风格指南](#style-guides)
  * [YouTube 频道](#youtube-channels)
* [架构和高级主题](#architecture-and-advanced-topics)
  * [功能标志](#feature-flags)
  * [GraphQL](#graphql)
  * [HTTP](#http)
  * [Micro-Frontends](#micro-frontends)
  * [模块联盟](#module-federation)
  * [Monorepos](#monorepos)
  * [服务器端渲染](#server-side-rendering)
* [开发实用程序](#development-utilities)
  * [Accessibility](#accessibility)
  * [AI](#ai)
  * [Analytics](#analytics)
  * [代码分析](#code-analysis)
  * [Debugging](#debugging)
  * [文档工具](#documentation-tools)
  * [IDE 扩展](#ide-extensions)
  * [发电机和脚手架](#generators-and-scaffolding)
  * [Internationalization](#internationalization)
  * [Linting](#linting)
  * [Networking](#networking)
  * [Performance](#performance)
  * [Runtime](#runtime)
  * [SEO](#seo)
  * [Styling](#styling)
* [安全与认证](#security-and-authentication)
  * [Authentication](#authentication)
  * [Payments](#payments)
  * [基于角色的访问控制](#role-based-access-control)
  * [安全最佳实践](#security-best-practices)
* [状态管理](#state-management)
  * [NgRx](#ngrx)
  * [NGXS](#ngxs)
  * [其他州立图书馆](#other-state-libraries)
* [Testing](#testing)
  * [E2E](#e2e)
  * [Component](#component)
  * [Helpers](#helpers)
* [网站模板](#site-templates)
  * [免费模板](#free-templates)
  * [付费模板](#paid-templates)
* [第三方组件](#third-party-components)
  * [Animations](#animations)
  * [Calendars](#calendars)
  * [Captcha](#captcha)
  * [Carousels](#carousels)
  * [Charts](#charts)
  * [Cookies](#cookies)
  * [CSV](#csv)
  * [数据网格](#data-grids)
  * [Dates](#dates)
  * [Directives](#directives)
  * [DOM](#dom)
  * [拖放](#drag-and-drop)
  * [Editors](#editors)
  * [文件上传](#file-upload)
  * [Forms](#forms)
  * [表单控件](#form-controls)
  * [JSON 表单](#json-forms)
  * [表单验证](#form-validation)
  * [Icons](#icons)
  * [Images](#images)
  * [键盘鼠标](#keyboard-mouse)
  * [Layout](#layout)
  * [Loaders](#loaders)
  * [Loggers](#loggers)
  * [Maps](#maps)
  * [Markdown](#markdown)
  * [Media](#media)
  * [混合公用事业](#mixed-utilities)
  * [Modals](#modals)
  * [Notifications](#notifications)
  * [入职和产品参观](#onboarding-and-product-tours)
  * [PDF](#pdf)
  * [Pipes](#pipes)
  * [Printing](#printing)
  * [二维码](#qr-codes)
  * [Router](#router)
  * [Scroll](#scroll)
  * [Storage](#storage)
  * [Tooltips](#tooltips)
  * [用户界面库](#ui-libraries)
  * [基于 Bootstrap 构建的 UI 库](#ui-libraries-built-on-bootstrap)
  * [基于 Material 的 UI 库](#ui-libraries-built-on-material)
  * [基于 Tailwind CSS 构建的 UI 库](#ui-libraries-built-on-tailwind-css)
  * [UI 库和 Ionic 框架](#ui-library-and-framework-ionic)
  * [用户界面基元](#ui-primitives)
  * [Viewers](#viewers)
  * [视觉效果](#visual-effects)
* [底层技术](#underlying-technologies)
  * [RxJS](#rxjs)
  * [TypeScript](#typescript)
* [框架互操作性](#framework-interoperability)
  * [跨框架集成](#cross-framework-integration)
  * [外部整合](#external-integration)
  * [Wrappers](#wrappers)
* [Angular 启发的解决方案](#angular-inspired-solutions)
* [外部列表](#external-lists)

## 角

> Angular 是一个 Web 框架，使开发人员能够构建用户喜爱的快速、可靠的应用程序。

### 官方资源

* [Site](https://angular.dev)
* [Blog](https://blog.angular.dev/)
* [Documentation](https://angular.dev/overview)
* [入门教程](https://angular.dev/tutorials/learn-angular)
* [GitHub 存储库](https://github.com/angular/angular)
* [过去的文档站点](https://v17.angular.io/docs)

### 建设者

* [Webpack](https://webpack.js.org)
* [esbuild](https://esbuild.github.io/)
* [Angular Builders](https://github.com/just-jeb/angular-builders) - 该存储库整合了 Angular 构建外观的所有社区构建器（ES Build、Webpack、Jest、Bazel 和 Timestamp）。
* [玩笑生成器](https://github.com/just-jeb/angular-builders/tree/master/packages/jest)
* [自定义网页包](https://github.com/just-jeb/angular-builders/tree/master/packages/custom-webpack)
* [自定义 esbuild](https://github.com/just-jeb/angular-builders/tree/master/packages/custom-esbuild)
* [Bazel](https://github.com/just-jeb/angular-builders/tree/master/packages/bazel) - 提供 Angular CLI Builder，当 ng build、ng test 等触发时可以执行 Bazel。
* [Timestamp](https://github.com/just-jeb/angular-builders/tree/master/packages/timestamp) - 这篇[文章](https://medium.com/angular-in-deep)对此进行了解释。
* [ngx-build-plus](https://github.com/manfredsteyer/ngx-build-plus) - 扩展 Angular CLI 的默认构建行为而不弹出，例如。 g。对于角度元素。
* [ngx-electronify](https://github.com/bampakoa/ngx-electronify) - Angular CLI 构建器，使用 Electron 在桌面上运行您的应用程序。
* [dotenv-run](https://github.com/chihab/dotenv-run) - 无缝加载环境变量。支持 cli、esbuild、Rollup、Vite、Webpack、Angular、ESM 和 Monorepos。
* [ng-packagr](https://github.com/ng-packagr/ng-packagr) - 以 Angular 包格式 (APF) 编译和打包 Angular 库。
* [angular-env-builder](https://github.com/igorissen/angular-env-builder) - 生成器根据您的环境变量生成“src/environments/environment.ts”文件。
* [angular-rspack](https://github.com/nrwl/nx/tree/HEAD/packages/angular-rspack) - [Rspack](https://github.com/web-infra-dev/rspack) 用于 Angular 应用程序的插件和工具。
* [ngx-devkit-builders](https://github.com/Celtian/ngx-devkit-builders) - 该软件包包含用于构建和测试 Angular 应用程序和库的 Architect 构建器。
* [angular-static-assets-hash](https://github.com/sitelint/angular-static-assets-hash) - 创建 Angular 静态资源列表和每个文件的哈希值。
* [ngx-schematic-builder](https://github.com/kstepien3/ngx-schematic-builder) - 用于构建 Angular 原理图项目的工具。编译并打包您的自定义原理图，为发布和使用做好准备。
* [ng-builder-typescript](https://github.com/da-mkay/ng-builder-typescript) - Angular CLI 的构建器，用于使用 TypeScript 编译器“tsc”构建 Node.js 应用程序（不使用 Webpack 或任何其他捆绑器）。

### CLI工具

* [官方网站](https://angular.dev/tools/cli)
* [官方 GitHub 存储库](https://github.com/angular/angular-cli)
* [alterforge](https://github.com/themodulardev/alterforge) - 一个 CLI 工具，可通过可选的 React 或 Angular 前端搭建和管理模块化微服务架构。
* [@MohamedBouattour/angular-clean-architecture](https://github.com/MohamedBouattour/angular-clean-architecture) - 一个 CLI 工具，可生成基于干净架构、可用于生产的 Angular 功能，并具有清晰、可维护的层。
* [angular-cli-diff](https://github.com/cexbrayat/angular-cli-diff) - 轻松将 Angular CLI 应用程序从一个版本升级到另一个版本 🚀。
* [angular-cli-ssr-diff](https://github.com/cexbrayat/angular-cli-ssr-diff) - 轻松将 Angular CLI SSR 应用程序从一个版本升级到另一个版本。
* [angular-parallel-test-runner](https://github.com/mahdi-hajian/angular-parallel-test-runner) - CLI 可跨项目并行运行 Angular 测试；使用可用的 CPU 内核。
* [angular-web-cli](https://github.com/qodalis-solutions/angular-web-cli) - 灵活的 CLI 工具，旨在简化工作流程、自动化任务并为开发人员提供可定制的实用程序。
* [Better-Fullstack](https://github.com/Marve10s/Better-Fullstack) - 几秒钟内即可构建可投入生产的全栈应用程序。从 425 个选项中选择您的堆栈 — CLI 将所有内容连接在一起。
* [dotairc](https://github.com/elecash/dotairc) - 该工具有助于为人工智能助手使用您的代码库创建一致的指令。
* [firebase-framework-tools](https://github.com/FirebaseExtended/firebase-framework-tools) - [Firebase CLI](https://github.com/firebase/firebase-tools/) 的实验性插件，用于添加 Web 框架支持。
* [i18n-fixer](https://github.com/zfurkandurum/i18n-fixer) - 与框架无关的 CLI 工具，可查找硬编码字符串、丢失的 i18n 键和未使用的翻译。
* [js-stack](https://github.com/vipinyadav01/js-stack) - 现代 CLI，用于搭建生产就绪的 JavaScript 全栈项目，具有自定义和最佳实践预设。
* [kqgen](https://github.com/KilloconQ/kqgen) - 用于生成 Angular 组件和服务的快速灵活的 CLI。包括表、过滤器和 REST/GraphQL 服务的预设。
* [lin](https://github.com/yuo-app/lin) - Lazy I18N 是一种使用 LLM 转换语言环境 JSON 的 CLI 工具。
* [mcp-angular-cli](https://github.com/talzach/mcp-angular-cli) - 提供 Angular CLI 和工作区自动化的服务器，使 LLM 和代理能够生成组件、添加包、创建工作区以及运行自定义架构师目标。
* [nest-schematics](https://github.com/lcasass3/nest-schematics) - 用于在 NestJS 中生成具有六边形架构的 CQRS（命令查询职责分离）模块的 Angular CLI 示意图。
* [ng-chrome-extension](https://github.com/larscom/ng-chrome-extension) - 轻松创建 Angular Chrome 扩展（清单 v3）。
* [ns-gc](https://github.com/th3n00bc0d3r/ns-gc) - 一个轻量级的命令行工具，用于生成具有干净结构和零配置的独立 NativeScript Angular 组件和 Angular 服务。
* [ngx-i18n-scan](https://github.com/pratiksonone/ngx-i18n-scan) - 一个 CLI 工具，可扫描 Angular 代码以提取和更新 i18n 翻译密钥，从而保持翻译文件干净。
* [ngx-stats](https://github.com/tomer953/ngx-stats) - CLI 工具，用于分析 Angular 项目、量化模块、组件、指令、管道和服务，以提供清晰的结构概览，从而获得更好的架构洞察力。
* [ngx-ws](https://github.com/art-ws/ngx-ws) - 使用 [JSON 参考](https://www.npmjs.com/package/@apidevtools/json-schema-ref-parser) 的强大功能，以及 [YAML](https://yaml.org/) 和 [JSON5](https://json5.org/) 格式的便利，轻松将大型“angular.json”拆分为模块化的项目本地文件。
* [prepare-angular-json](https://github.com/ackheron/prepare-angular-json) - 一个轻量级 CLI 工具，可从带注释的“angular.jsonc”生成干净的“angular.json”文件。
* [rafacli](https://github.com/rafa00716/rafacli) - CLI 工具，可为 NestJS 和 Angular 生成身份验证和 CRUD 模块，自动执行样板以简化开发并确保一致性。
* [ngx-crafter](https://github.com/ErwanHeschung/ngx-crafter) - 一个强大的 CLI 工具，可帮助您使用预配置的文件夹结构和基本包来制作 Angular 项目。
* [ng new command generator](https://ng.gridatek.com/) - 生成优化的“ng new”命令。
* [svger-cli](https://github.com/faezemohades/svger-cli) - 一个轻量级 CLI，可将 SVG 转换为零依赖的优化 Angular 组件。
* [tailwind-init-cli](https://github.com/ImLeoNova/tailwind-init-cli) - Angular、React 或 Next.js 项目中 Tailwind CSS 的单命令设置工具！

### 部署

* [AWS 放大](https://docs.amplify.aws/angular/)
* [Vercel](https://vercel.com/solutions/angular)
* [Firebase 托管](https://firebase.google.com/docs/app-hosting/get-started)
* [Netlify](https://docs.netlify.com/frameworks/angular/) - Netlify 上的 Angular 应用程序通过 [Angular Runtime](https://github.com/netlify/angular-runtime) 插件获得自动框架检测和重定向。
* [angular-cli-ghpages](https://github.com/angular-schule/angular-cli-ghpages) - SSR 不起作用，并且可能有一些警告，但您可以在 GitHub Pages 上托管 Angular 项目。
* [analog-publish-gh-pages](https://github.com/k9n-dev/analog-publish-gh-pages) - 用于在 GitHub Pages 上部署“Analog.js”应用程序的 GitHub 操作。
* [Genezio](https://github.com/Genez-io/genezio) - 编写和托管无服务器应用程序的最简单方法。
* [Cloudflare 页面](https://developers.cloudflare.com/pages/framework-guides/deploy-an-angular-site/#create-a-new-project-using-the-create-cloudflare-cli-c3)
* [Zerops](https://zerops.io/) - 它使得部署和运行模拟应用程序，无论是[服务器端渲染](https://github.com/zeropsio/recipe-analog-nodejs)还是[静态](https://github.com/zeropsio/recipe-analog-static)，都变得轻而易举。
* [SST](https://sst.dev/) - 一个可以轻松构建和自动化现代全栈应用程序的框架。
* [ngx-config-orchestrator](https://github.com/xhani-manolis-trungu/ngx-config-orchestrator) - 通过外部 JSON 进行运行时配置的 Angular 库，实现“一次构建，随处部署”。
* [deploy-with-git](https://github.com/RunOnFlux/deploy-with-git/tree/master/deploy-angular) - 允许您将 Angular 应用程序从 Git 存储库直接部署到 [Flux Network](https://runonflux.com/)。
* [@railwayapp-templates/angular-starter](https://github.com/railwayapp-templates/angular-starter) - 一键默认Angular TS启动器，利用Caddy服务！
* [angular-deploy-bunny](https://github.com/lostium/angular-deploy-bunny) - Angular Architect 构建器（`ng deploy`）使用 SHA256 增量比较将您的构建同步到 Bunny.net CDN 存储区域，然后清除相应的 Pull 区域。
* [ngx-ssh-deploy](https://bitbucket.org/dkhang97/ngx-ssh-deploy/src/master/) - 使用 SSH 部署 Angular 项目。

### 桌面应用程序

* [electron](https://github.com/electron/electron) - 使用 JavaScript、HTML 和 CSS 构建跨平台桌面应用程序。
* [angular-electron](https://github.com/maximegris/angular-electron) - 使用 Angular 和 Electron 进行超快速引导。
* [neutralinojs](https://github.com/neutralinojs/neutralinojs) - 一个轻量级、可移植的框架，用于使用 JavaScript、HTML 和 CSS 构建跨平台桌面应用程序，在 Linux、macOS、Windows、Web 和 Chrome 上运行。
* [nw.js](https://github.com/nwjs/nw.js) - 使用 HTML、JavaScript 和直接 Node 集成的本机应用程序的 Chromium + Node.js 运行时。
* [nw-angular-example](https://github.com/nwutils/nw-angular-example) - 将 Angular 与 NW.js 集成的示例。
* [tauri](https://v2.tauri.app/) - 创建小型、快速、安全、跨平台的应用程序。
* [angular-tauri](https://github.com/maximegris/angular-tauri) - 使用 Angular 和 Tauri 进行超快速引导。
* [create-tauri-app](https://github.com/tauri-apps/create-tauri-app) - 快速搭建一个新的 Tauri 应用程序项目。
* [wails](https://github.com/wailsapp/wails) - 使用 Go 和 Web 技术（包括 [Angular](https://wails.io/docs/guides/angular/)）构建桌面应用程序。
* [MōBrowser](https://teamdev.com/mobrowser) - 一个使用 TypeScript、HTML 和 CSS 构建桌面应用程序的框架，内置源代码保护。

### 更新角度

* [Official website](https://angular.dev/update-guide) - 交互式指南可帮助您从一个版本的 Angular 迁移到另一个版本。
* [Official update reference](https://angular.dev/cli/update) - 使用 CLI 更新您的项目或通过添加“--next”标志来尝试新的 Angular 功能。
* [Official migrations reference](https://angular.dev/reference/migrations) - Angular 原理图通过转换为独立组件、新的控制流语法等来帮助更新项目。
* [ng-morph](https://github.com/taiga-family/ng-morph) - 项目或原理图中的代码更改从未比现在更容易。
* [ngx-libs](https://github.com/eneajaho/ngx-libs) - Angular 库支持列出了每个 Angular 版本的社区库支持。
* [@fast-facts/ng-update](https://github.com/fast-facts/ng-update) - 一个 GitHub Action，可通过基于“ng update”的自动 PR 使基于 Angular CLI 的项目保持最新状态。
* [npx-app-updater](https://github.com/DSI-HUG/ngx-app-updater) - 部署新版本时提醒用户可用的更新。
* [ngx-update-app](https://github.com/Celtian/ngx-update-app) - 通过服务人员更新应用程序的角度指令。
* [Angular Caniuse](https://www.angular.courses/caniuse/features) - 跟踪 Angular 功能从预览到稳定阶段的过程。
* [Depfixer](https://depfixer.com/sample-report/angular) - JS/TS项目的智能依赖分析；检测兼容性冲突并提供逐步修复。
* [migration-planificator](https://github.com/silvestv/migration-planificator-documentation) - 通过精确的 AST 分析来规划 Angular 迁移、计算工作负载估算并生成交互式 HTML 仪表板。
* [NgReady](https://www.ngready.dev/) - 停止在 Angular 升级上浪费时间。

## 角脉冲

### 社区

* [角度不和谐通道](https://discord.com/invite/angular)
* [Angular Hashtag](https://x.com/hashtag/angular) - 在 X 上使用“#angular”主题标签。
* [吉特频道](https://gitter.im/angular/angular)
* [角度堆栈溢出](https://stackoverflow.com/questions/tagged/angular)
* [@Angular 在 X 上](https://x.com/angular)
* [/r/Angular 子版块](https://www.reddit.com/r/Angular/)
* [Angular Buddies Slack 频道](https://angularbuddies.slack.com/)
* [angular-logos](https://github.com/maartentibau/angular-logos) - Repo 致力于收集所有不同类型的 Angular 徽章和徽标。
* [Made with Angular](https://github.com/madewithangular/madewithangular.github.io) - 使用 Angular 构建的 Web 应用程序的展示。
* [Angular Hub](https://github.com/angular-sanctuary/angular-hub) - Angular 事件和社区的精选列表。
* [Angular Space](https://www.angularspace.com/) - 作为 Angular 开发人员学习和成长的中心。
* [builtwith trends](https://trends.builtwith.com/framework/Angular) - 角度使用统计。
* [Angular：纪录片 |一个起源故事](https://www.youtube.com/watch?v=cRC9DlH45lA)
* [Angular Talents](https://www.angulartalents.com/) - 独立开发人员可以突出显示他们对即将进行的项目的可用性，从而无需无休止地滚动工作板。
* [Map of GitHub](https://anvaka.github.io/map-of-github/#9.14/-21.9624/9.8143) - 探索 NgSphere 以发现具有重叠观星者的存储库。
* [Good First Issues](https://www.dolmen.tools/en/angular/good-first-issues/explorer) - 查找适合初学者的问题并开始为 Angular 开源项目做出贡献。

### 时事通讯

* [角度瘾君子](https://www.angularaddicts.com/)
* [角度摘要](https://geromegrignon.substack.com/)
* [终极课程](https://ultimatecourses.com/newsletter)
* [每周角度](https://prodigious-knitter-4508.kit.com/subscribe)

### 播客

* [角空气](https://angularair.com/)
* [角度大师播客](https://www.youtube.com/playlist?list=PLYJFRoKhU5SNcu5GBjIn4X3oVpy4fP1wV)
* [角加显示](https://open.spotify.com/show/1PrLErQHBqBhZsRV1KHhGM)
* [Angularidades](https://podcasts.apple.com/us/podcast/angularidades/id1702444448) - 用西班牙语。

### 蓝天

* [Angular 入门包，作者：@brandonroberts.dev](https://bsky.app/starter-pack/brandonroberts.dev/3l7lzgkwkqu2n)

### X 上的 Angular 团队

* [明科·格切夫](https://x.com/mgechev)
* [艾伦·阿吉乌斯](https://x.com/AlanAgius4)
* [马蒂厄·里格勒](https://x.com/jean__meche)
* [亚历克斯·里卡博](https://x.com/synalx)
* [克里斯蒂安·科斯塔迪诺夫](https://x.com/_crisbeto)
* [保罗·格施文特纳](https://x.com/devversion)
* [乔斯特·科霍恩](https://x.com/devjoost)
* [西蒙娜·科廷](https://x.com/simona_cotin)
* [杰西卡·贾纽克](https://mastodon.social/@jessicajaniuk)
* [道格·帕克](https://mastodon.social/@develwithoutacause@techhub.social)
* [艾玛·特沃斯基](https://x.com/twerske)
* [马克·汤普森](https://x.com/marktechson)
* [帕维尔·科兹洛斯基](https://x.com/pkozlowski_os)
* [迪伦·洪](https://x.com/dylhunn)

### X 上的 Angular 专家

* [@PatrickJS](https://x.com/PatrickJS)
* [@eggheadio](https://x.com/eggheadio)
* [@hirez_io](https://x.com/hirez_io)
* [@cedric_exbrayat](https://x.com/cedric_exbrayat)
* [@victorsavkin](https://x.com/victorsavkin)
* [@jeffbcross](https://x.com/jeffbcross)
* [@marsibarsi](https://x.com/marsibarsi)
* [@maciejtreder](https://x.com/maciejtreder)
* [@maartentibau](https://x.com/maartentibau)

### X 方面的 Google 开发者专家

* [杰克·富兰克林](https://x.com/jack_franklin)
* [蒂埃里·查特尔](https://x.com/ThierryChatel)
* [尤里·沙克德](https://x.com/urishaked)
* [贡萨洛·鲁伊斯·德维拉·苏亚雷斯](https://x.com/gruizdevilla)
* [莎朗·迪奥里奥](https://x.com/sharondio)
* [约翰·帕帕](https://x.com/John_Papa)
* [丹·华林](https://x.com/danwahlin)
* [克里斯蒂安·维尔](https://x.com/christianweyer)
* [托德座右铭](https://x.com/toddmotto)
* [蒂姆·鲁弗斯](https://x.com/timruffles)
* [瓦西姆·切格姆](https://x.com/manekinekko)
* [亚伦·弗罗斯特](https://x.com/js_dev)
* [威尔逊·门德斯](https://x.com/willmendesneto)
* [贾里德·威廉姆斯](https://x.com/jaredwilli)
* [杰拉德·桑斯](https://x.com/gerardsans)
* [帕斯卡·普雷希特](https://x.com/PascalPrecht)
* [杰夫·维尔普利](https://x.com/jeffwhelpley/)
* [劳尔·希门尼斯](https://x.com/elecash/)
* [马克西姆·萨尔尼科夫](https://x.com/webmaxru)
* [黛博拉·仓田](https://x.com/deborahkurata)
* [谢·雷兹尼克](https://x.com/shai_reznik)
* [曼弗雷德·斯泰尔](https://x.com/manfredsteyer)
* [尤里·斯特朗普弗洛纳](https://x.com/juristr)
* [威廉·格拉塞尔](https://x.com/willgmbr)
* [艾莉莎·尼科尔](https://x.com/AlyssaNicoll)
* [尼尔·考夫曼](https://x.com/nirkaufman)
* [德米特里·谢霍夫佐夫](https://x.com/valorkin)
* [杰夫·德莱尼](https://x.com/jeffdelaney23)
* [尼舒·戈尔](https://x.com/TheNishuGoel)
* [亚历克斯·英金](https://x.com/waterplea)
* [桑托什·亚达夫](https://x.com/SantoshYadavDev)
* [Ankit](https://x.com/ankitsharma_007)
* [悉达多·阿吉梅拉](https://x.com/SiddAjmera)
* [穆罕默德·阿赫桑·阿亚兹](https://x.com/codewith_ahsan)
* [德米特罗·梅真斯基](https://x.com/DecodedFrontend)
* [迈克尔·赫拉德基](https://x.com/Michael_Hladky)
* [法比奥·比昂迪](https://x.com/biondifabio)
* [托马斯·拉福奇](https://x.com/laforge_toma)

## 学习资源

### 博客

* [Angular Experts](https://angularexperts.io/blog) - 了解有关 Angular、NgRx、RxJS 和 NX 的所有信息，并通过指南、深入内容和可操作的提示和技巧来提高您的技能！
* [angular-university](https://blog.angular-university.io/) - 学习并跟上 Angular 生态系统的步伐。
* [simplified courses](https://blog.simplified.courses/) - 用爱写的博客文章，只为您！
* [Just Angular](https://justangular.com/) - 分享有关 Angular 的最新、最重要的更新，以及有用的提示和技巧。
* [Angular Love](https://angular.love/) - （波兰语）优秀的 Angular 最新资源。
* [角度思维](https://www.angularminds.com/blog)
* [角度建筑师](https://www.angulararchitects.io/en/blog/)
* [角屋](https://houseofangular.io/blog/)
* [这个点实验室](https://www.thisdot.co/blog?tags=angular)
* [halodoc](https://blogs.halodoc.io/tag/angular-2-2/)
* [ninja-squad](https://blog.ninja-squad.com/)
* [marmicode](https://marmicode.io/learn/everything)
* [内塔内尔基础](https://medium.com/@netbasal)
* [蒂姆·德施莱弗](https://timdeschryver.dev/)
* [周陈](https://nartc.me/)
* [明科·格切夫](https://blog.mgechev.com/)
* [马蒂厄·里格勒](https://riegler.fr/)
* [托马斯·拉福奇](https://medium.com/@thomas.laforge)
* [莱纳·哈内坎普](https://medium.com/@rainer-hahnekamp)
* [叶夫根尼·奥兹](https://medium.com/@eugeniyoz)
* [托马斯·图拉真](https://tomastrajan.medium.com/)
* [托马斯·杜辛](https://ducin.dev/blog)
* [这是有角的](https://dev.to/this-is-angular)
* [daily.dev](https://app.daily.dev/tags/angular)
* [角度哲学](https://github.com/tomavic/angular-philosophies)
* [Angular Material Dev](https://angular-material.dev/home) - 与 Angular 中的材料设计相关的所有内容都集中在一处。
* [Angular Tips](https://ngtips.com/) - 使用 Angular 构建复杂、大型且可维护的应用程序的最佳实践和建议。
* [Practical Angular Guide](https://practical-angular.donaldmurillo.com/) - [Donald Murillo](https://github.com/DonaldMurillo) 为 Angular 开发人员提供的现实世界解决方案。

### 书籍

* [Packt Publishing](https://www.packtpub.com/en-us/search?query=angular&sort=best-selling) - 查找种类最多的最新编程书籍的最佳选择。
* [GumRoad](https://gumroad.com/software-development/web-development/javascript?tags=angular) - 各种免费和付费的 Angular 电子书。
* [LeanPub](https://leanpub.com/bookstore?type=all&search=angular) - 利用 LeanPub 灵活的定价模式，按照您自己的条件支持作者，让您可以自由选择支付费用。
* [Manning](https://www.manning.com/) - 随处购买曼宁电子书，即可免费获得电子书。
* [Become a ninja with Angular](https://books.ninja-squad.com/angular) - 《忍者小队》。
* [Angular-Buch (German)](https://angular-buch.com/) - `dpunkt.verlag`。
* [与 Ahsan 一起编码](https://www.codewithahsan.dev/books)
* [Angular University Ebooks](https://angular-university.io/my-ebooks) - 单独提供或包含在订阅中。
* [Angular Enterprise Architecture](https://angularexperts.io/products/ebook-angular-enterprise-architecture) - “托马斯·图拉真”。
* [Testing Angular](https://testing-angular.com) - 强大的 Angular 应用程序指南 **免费**。
* [Modern Angular](https://www.angulararchitects.io/en/ebooks/modern-angular/?book) - “曼弗雷德·斯泰尔”**免费**。
* [TutorialSearch](https://tutorialsearch.io/browse/programming-languages/angular-interview) - 免费的跨平台搜索引擎，对来自 Udemy、Skillshare、Pluralsight 和其他主要学习平台的 45 多个类别的 50,000 多个教程进行索引。
* [Ultimate Guide to Angular Evolution](https://houseofangular.io/the-ultimate-guide-to-angular-evolution/) - “Angular 之家”**免费**。
* [Micro Frontends and Moduliths with Angular](https://www.angulararchitects.io/en/ebooks/micro-frontends-and-moduliths-with-angular/) - “曼弗雷德·斯泰尔”**免费**。
* [Angular Mastery](https://christianlydemann.com/angular-mastery-book/) - “克里斯蒂安·吕德曼”**免费**。
* [Enterprise Monorepo Angular Patterns](https://go.nx.dev/angular-patterns-ebook) - `Nx 核心团队` **免费**。

### 认证计划

* [Certificates.dev](https://certificates.dev/angular) - 获得 Angular 开发人员的能力认证。
* [Angular Academy CA](https://www.angularacademy.ca/angular-certification) - 在加拿大进行由讲师指导的实践 Angular 培训。
* [Hackerrank](https://www.hackerrank.com/skills-verification/angular_basic) - Angular（基本）技能认证测试。
* [Koenig](https://www.koenig-solutions.com/angularjs-training-certification-courses) - 各种课程分别或全面介绍 Angular。
* [Simplilearn](https://www.simplilearn.com/angular-certification-training-course) - Angular 认证培训课程。

### 备忘单

* [官方 Angular 版本 17 备忘单](https://v17.angular.io/guide/cheatsheet)
* [100 个 Angular 面试问题及答案列表](https://github.com/sudheerj/angular-interview-questions)
* [Angular 开发者路线图](https://roadmap.sh/angular)
* [Framework Field Guide](https://playfulprogramming.com/collections/framework-field-guide) - 一种一次性学习 Angular、React 和 Vue 的免费且实用的方法。
* [Marmicode Cookbook](https://cookbook.marmicode.io/) - 烹饪美味应用程序的配料和食谱。
* [angular-interview-questions](https://github.com/Devinterview-io/angular-interview-questions) - Angular 面试问题和答案可帮助您为下一次技术面试做好准备。
* [dotnet_angular_cli_cheatsheet](https://github.com/shashinvision/dotnet_angular_cli_cheatsheet) - 面向使用 .NET 和 Angular 的全栈开发人员的综合指南。

### 练习

* [angular-fundamental-lessons](https://github.com/MarkTechson/angular-fundamentals-lessons)
* [Angular Challenges](https://angular-challenges.vercel.app/) - 包含 60 多个 Angular、Nx、RxJS、NgRx 和 TypeScript 挑战的存储库，旨在提高实际技能。
* [Codelabs](https://codelabs.developers.google.com/?text=angular) - Google Developers Codelabs 提供指导性实践教程来构建应用程序或添加新功能。
* [rxjs-fruits](https://www.rxjs-fruits.com/subscribe) - 互动课程涵盖 RxJS 中的一系列运算符。
* [modern-angular-exercises](https://github.com/kobi-hari-courses/modern-angular-exercises) - 有关各种 Angular 主题的练习，包括解决方案和解决方案视频。

### 培训

* [Angular Academy](https://www.angularacademy.ca/) - 世界一流的讲师指导的实时在线 Angular 课程！
* [角度训练营](https://angularbootcamp.com)
* [Angular Start](https://angularstart.com/) - 学习使用新功能和现代最佳实践来构建专业级 Angular 应用程序。
* [Angular Training](https://www.angulartraining.com/) - 您需要的 Angular 教练。
* [Angular UI](https://angular-ui.com/) - 准备好使用 Angular 以及交互式课程和练习构建您的下一个 Web 应用程序。
* [Angular University](https://angular-university.io/) - 学习并跟上 Angular 生态系统的步伐。
* [Angular.Schule（德国）](https://angular.schule/)
* [Angular.DE（德国）](https://angular.de/schulungen/angular-intensiv/)
* [learnbydo.ing](https://www.learnbydo.ing/) - 通过 [Fabio Biondi](https://www.fabiobiondi.dev/) 提供的课程、书籍和练习来学习 {Web} 编程。内容为意大利语或英语。
* [liveloveapp](https://liveloveapp.com/) - 研讨会可针对 Cypress、NgRx、RxJS、AG Grid 和 Web 性能。
* [Marmicode](https://www.eventbrite.fr/o/younes-jaaidi-marmicode-29329031085)
* [ng.guide](https://ng.guide/) - 通过构建真实世界的应用程序来学习 Angular。
* [Tech OS](https://tech-os.org/) - 提供专为要求严格的开发人员和雄心勃勃的团队设计的高水平 Angular 培训。
* [Udemy：Angular - 完整指南](https://www.udemy.com/course/the-complete-guide-to-angular-2)
* [Ultimate Courses](https://ultimatecourses.com/courses/angular) - 成为 Angular 专家所需的一切。
* [Workshops.DE（德国）](https://workshops.de/seminare-schulungen-kurse/angular-typescript/)

### 风格指南

* [官方 Angular 风格指南](https://angular.dev/style-guide)
* [Infinum](https://infinum.com/handbook/frontend/angular/introduction)
* [TypeScript 风格指南](https://mkosir.github.io/typescript-style-guide/)

### YouTube 频道

* [Angular](https://www.youtube.com/@Angular)
* [NG会议](https://www.youtube.com/@ngconfonline)
* [Procademy](https://www.youtube.com/@procademy)
* [怪物课程学院](https://www.youtube.com/@MonsterlessonsAcademy)
* [约书亚·莫罗尼](https://www.youtube.com/@JoshuaMorony)
* [Nihira 技术人员](https://www.youtube.com/@NihiraTechiees)
* [角大学](https://www.youtube.com/@AngularUniversity)
* [莱纳·哈内坎普](https://www.youtube.com/@RainerHahnekamp)
* [使用 Profanis 进行代码拍摄](https://www.youtube.com/@CodeShotsWithProfanis)
* [黛博拉·仓田](https://www.youtube.com/@deborah_kurata)
* [BrandonRobertsDev](https://www.youtube.com/@BrandonRobertsDev)
* [解码前端](https://www.youtube.com/@DecodedFrontend)
* [佐阿布·汗](https://www.youtube.com/@ZoaibKhan)
* [NivekDev](https://www.youtube.com/@nivekDev)
* [WebTechTalk](https://www.youtube.com/@WebTechTalk)
* [巴巴通德·拉米迪](https://www.youtube.com/@babatundelmd)
* [TechStackNation](https://www.youtube.com/@techstacknation)
* [角爱](https://www.youtube.com/@angularlove)
* [异常新闻](https://www.youtube.com/@ng-news)
* [学习伙伴](https://www.youtube.com/@LearningPartnerDigital)
* [伊戈尔·谢多夫](https://www.youtube.com/@theigorsedov)
* [布赖恩·特里斯](https://www.youtube.com/@briantreese)
* [科比·哈里](https://www.youtube.com/@kobihari)
* [编程实践](https://www.youtube.com/@programmingpracticals)
* [丹尼尔·拉比佐](https://www.youtube.com/@daniilrabizo)
* [StartupAngular](https://www.youtube.com/@StartupAngular) - 日语。
* [Code with Keys](https://www.youtube.com/@codewithkeys) - 波斯语。

## 架构和高级主题

### 功能标志

* [OpenFeature Angular SDK](https://openfeature.dev/docs/reference/technologies/client/web/angular) - 与供应商无关、社区驱动的 API 规范，用于功能标记。
* [@devcycle/openfeature-angular-provider](https://www.npmjs.com/package/@devcycle/openfeature-angular-provider) - [DevCycle](https://docs.devcycle.com/sdk/client-side-sdks/angular/) 支持 OpenFeature Angular SDK。
* [@openfeature/go-feature-flag-web-provider](https://www.npmjs.com/package/@openfeature/go-feature-flag-web-provider) - [GO 功能标志](https://gofeatureflag.org/) 提供程序允许您使用“@openfeature/web-sdk”[连接](https://gofeatureflag.org/docs/sdk/client_providers/openfeature_angular) 到您的 GO 功能标志实例。
* [Flagsmith](https://www.flagsmith.com/) - 通过功能标志管理加快交付速度并控制版本。
* [@statsig/angular-bindings](https://www.npmjs.com/package/@statsig/angular-bindings) - [Statsig](https://www.statsig.com/) Angular 绑定包提供了一个可以注入到您的组件中的 `StatsigService`。有关更多详细信息，请参阅 [Statsig 文档](https://docs.statsig.com/client/javascript-sdk/Angular/)。
* [@configcat/js-sdk](https://github.com/configcat/js-sdk) - ConfigCat SDK for JavaScript 为您的应用程序提供了与 [ConfigCat](https://configcat.com/) 的轻松集成。
* [@configcat-labs/feature-flags-in-angular-sample-app](https://github.com/configcat-labs/feature-flags-in-angular-sample-app) - 使用 ConfigCat 的示例应用程序。
* [featurit-sdk-angular](https://github.com/featurit/featurit-sdk-angular) - [FeaturIT](https://featurit.com/) 功能标志管理平台的 JavaScript 客户端的 Angular 包装器。
* [ngx-feature-proxy](https://github.com/zenkiet/ngx-feature-proxy) - 带有 Unleash 的 Angular 特征标志库；只需最少的设置即可实现反应式和类型安全的标志管理。
* [ngx-feature-flags](https://github.com/pavan-98/ngx-feature-flags) - Angular 优先、企业就绪的功能标志层，可标准化 Angular 应用程序中标志的解析、保护和呈现方式。
* [ngx-feature-flags-toggly](https://www.npmjs.com/package/@ops-ai/ngx-feature-flags-toggly) - 用于 [Toggly](https://toggly.io/) 功能标志的 Angular SDK。
* [ngx-circuit](https://github.com/pjlamb12/ngx-circuit) - 通过布尔标志和百分比推出等灵活选项简化功能切换管理。
* [ngx-feature-toggle](https://github.com/willmendesneto/ngx-feature-toggle) - 使用此 Angular 指令简化管理功能切换。
* [@rollgate/sdk-angular](https://github.com/rollgate/sdks/tree/main/packages/sdk-angular) - 适用于 [Rollgate](https://rollgate.io) 的 Angular SDK，这是一个具有预定发布和逐步推出功能的平台。

### GraphQL

* [apollo-angular](https://github.com/kamilkisiela/apollo-angular) - 适用于 Angular 和每个 GraphQL 服务器的功能齐全、可用于生产的缓存 GraphQL 客户端。
* [apollo-dynamic-angular](https://github.com/giuliano-marinelli/apollo-dynamic-angular) - Apollo Angular 的变体，允许通过修饰模式动态选择查询、突变和订阅集。
* [apollo-orbit](https://github.com/wassim-k/apollo-orbit) - 用于 Angular 的功能齐全的 GraphQL 客户端，具有模块化状态管理。
* [buoy](https://github.com/buoy-graphql/buoy) - 构建在 Apollo 之上的 Angular GraphQL 客户端。
* [graphql-code-generator](https://github.com/dotansimha/graphql-code-generator) - 用于 GraphQL 模式和操作的代码生成器，具有灵活的插件支持。
* [ngx-graphql-client](https://github.com/Alevettih/ngx-graphql-client) - 用于 Angular 应用程序的类型化 GraphQL 客户端，具有完整的 TypeScript 支持。
* [takeshape](https://www.takeshape.io/) - 使用 TakeShape 构建 GraphQL API 很容易。请按照此[指南](https://app.takeshape.io/docs/get-started/client/angular) 与 Angular 集成。

### HTTP协议

* [ng-http-caching](https://github.com/nigrosimone/ng-http-caching) - Angular 应用程序中 HTTP 请求的缓存。
* [@ngify/http](https://github.com/ngify/ngify/tree/main/packages/http) - 反应式 Angular HTTP 客户端，具有类型化响应、简化的错误和请求/响应拦截。
* [ng-http-loader](https://github.com/mpalourdio/ng-http-loader) - 智能 Angular HTTP 拦截器 - 自动拦截 HTTP 请求并显示 spinkit 旋转器/加载器/进度条。
* [angular-odata](https://github.com/diegomvh/angular-odata) - 用于在 Angular 中查询、创建、更新和删除 OData 资源的流畅 API。
* [ng-memento](https://github.com/terzurumluoglu/ng-memento) - 通过防止在 Angular 项目中再次调用相同的 HTTP 请求，使您的应用程序更快。
* [ngx-suspense-of](https://github.com/Celtian/ngx-suspense-of) - 为您的应用程序增添悬念的 Angular 指令。
* [ngx-pwa](https://github.com/Service-Soft/ngx-pwa) - 提供围绕 Angular PWA 的附加功能。最值得注意的是能够缓存和同步 POST/PATCH/DELETE 请求。
* [ngx-repository](https://github.com/paddls/ngx-repository) - 在 Angular 项目中轻松创建强类型数据客户端（HTTP REST 或 Firestore）。
* [ng-rest-client](https://github.com/gizm0bill/gzm/tree/master/libs/ng-rest-client) - 该库允许开发人员使用方法装饰器定义 RESTful API 客户端，从而简化了 HTTP 请求。
* [ngx-sse-client](https://github.com/marcospds/ngx-sse-client) - 一个简单的**SSE**（服务器发送事件）客户端，用于 Angular 应用程序来替换“EventSource”的使用。
* [@connectrpc/connect-web](https://github.com/connectrpc/connect-es/tree/main/packages/connect-web) - [Connect](https://connectrpc.com/)提供跨平台的API库。 [@connectrpc/connect](https://www.npmjs.com/package/@connectrpc/connect) 在 TypeScript 中提供类型安全的 Protobuf API，并且 [@connectrpc/connect-web](https://www.npmjs.com/package/@connectrpc/connect-web) 添加了浏览器支持。请参阅[Angular 示例](https://github.com/connectrpc/examples-es/tree/main/angular)。
* [ng-httpclient-easy-network-stub](https://github.com/NGneers/ng-httpclient-easy-network-stub) - 一个简单的类，用于模拟来自 Angular HttpClient 的大量网络请求。
* [simply-direct](https://github.com/fvilli/simply-direct) - 一个全栈通信库，通过由 WebSockets 提供支持的实时双向通信来桥接 Angular 和 NestJS。
* [ng-error-handling](https://github.com/ressurectit/ng-error-handling) - 专为管理 HTTP API 错误响应而设计的 Angular 模块。
* [active-connect](https://github.com/HiptJo/active-connect) - Node.js、Angular 和 WebSockets 的连接框架，可简化与装饰器和实用程序的实时客户端-服务器通信。
* [ngx-signal-pagination](https://github.com/JPtenBerge/ngx-signal-pagination) - Angular 的分页，由信号驱动。
* [ngx-http](https://github.com/OGS-GmbH/ngx-http) - 一个轻量级 Angular 库，通过提供类型、静态值和实用函数来增强 HTTP 功能。
* [ng-speed-test](https://github.com/jrquick17/ng-speed-test) - 用于检查互联网速度的轻量级 Angular 库。
* [ngx-interceptors](https://github.com/SebaRenner/ngx-interceptors) - 具有适用于 Angular 应用程序的常见 HTTP 拦截器的库。
* [ngx-hal](https://github.com/infinum/ngx-hal) - 支持处理 [HAL 格式](http://stateless.co/hal_specation.html) HTTP 请求的数据存储库。
* [trpc-angular](https://github.com/heddendorp/trpc-angular) - 该存储库提供了两个基于 tRPC 的 Angular 包：用于 HttpClient 的“@heddendorp/trpc-link-angular”，以及用于反应式数据获取的“@heddendorp/tanstack-angular-query”。
* [my-http-resource](https://github.com/consoleLogMyAss/my-http-resource/tree/main/projects/my-http-resource) - 反应式 Angular HttpClient 包装器，通过管理状态、URL 参数和配置来简化请求。
* [luminara](https://github.com/miller-28/luminara) - 一个基于本机获取构建的现代通用 HTTP 客户端，专为可靠、可扩展且清晰的架构而设计。
* [ngx-cachr](https://github.com/nulzo/ngx-cachr) - 一个精简的、基于信号的 Angular 缓存库。
* [ngx-data-polling](https://github.com/antonio-spinelli/ngx-data-polling) - Angular 库，具有以声明性和类型安全的方式处理数据轮询的实用程序。
* [ngx-soap](https://github.com/seyfer/ngx-soap) - 基于 [node-soap](https://github.com/vpulim/node-soap) 构建的轻量级 SOAP 客户端，与 Angular 的信号、独立组件和现代功能完全兼容。
* [ngx-http-fetch-tracking](https://github.com/pegasusheavy/ngx-http-fetch-tracking) - Angular 库为 Fetch API 后端提供上传进度跟踪。
* [fetchquack](https://github.com/adrian-bueno/fetchquack) - Angular 就绪的 HTTP 客户端，具有 RxJS Observable 包装器和注入上下文支持，提供基于 Fetch 的轻量级流、SSE 和上传/下载进度处理。
* [ziflux](https://github.com/neogenz/ziflux) - 适用于 Angular 21+ 的零依赖、信号原生缓存层，具有资源 () 的 stale-while-revalidate - 即时导航、后台刷新、无旋转器。
* [ng-signal-query](https://github.com/Ali7040/ng-signal-query) - 一个基于信号构建的类型安全的 Angular 查询库，可简化服务器状态、无限查询、突变和高性能缓存。
* [api-caller](https://forge.deejayy.hu/angular-packages/api-caller) - Angular 的简单 API 调用程序库。
* [ngx-lite-cache](https://github.com/Suleeyman/ngx-lite-cache) - 一个 Angular 库，通过 HttpClient 拦截器缓存 HTTP 响应，以减少冗余请求并提高性能。
* [ng-qubee](https://github.com/AndreaAlhena/ng-qubee) - Angular 查询生成器，具有反应式 URI（RxJS + 信号）、类型化分页、495 多个测试和多驱动程序支持。

### 微前端

* [angular-microfrontend-demo](https://github.com/gioboa/angular-microfrontend-demo) - 模块联盟 Vite + Angular 现已成为可能。
* [backbase-micro-frontends](https://github.com/Backbase/backbase-micro-frontends) - 概念证明展示了旧版应用程序（小部件）如何通过模块联合与新应用程序（旅程）协同工作。
* [micro-frontends-mindmaps](https://github.com/santoshshinde2012/micro-frontends-mindmaps) - 总结微前端概念的思维导图。
* [ngx-mfe](https://github.com/dkhrunov/ngx-mfe) - 用于在 Webpack 5 和插件 ModuleFederation 中使用微前端的 Angular 库。

### 模块联盟

* [@module-federation/core](https://github.com/module-federation/core) - 模块联合是一个允许开发人员在多个 JavaScript 应用程序之间共享代码和资源的概念。
* [ng-dynamic-mf](https://github.com/LoaderB0T/ng-dynamic-mf) - 通过模块联合在运行时实现真正的动态模块。
* [module-federation-plugin](https://github.com/angular-architects/module-federation-plugin) - 将 Module Federation 与 Angular CLI 集成的插件，用于加载微前端或插件。
* [webpack-module-federation-with-angular](https://github.com/edumserrano/webpack-module-federation-with-angular) - 通过多个 Angular 代码演示了解 Webpack 模块联合的指南。
* [Vite-module-federation-angular-test](https://github.com/Seifenn/vite-module-federation-angular-test) - 使用 Angular 和 AnalogJS 测试 [Module Federation Vite](https://github.com/module-federation/vite)（通过 [@brandonroberts/angular-vite](https://github.com/brandonroberts/angular-vite)）；使用 AnalogJS 主机探索 SSR（插件 SSR 支持可能有所不同）。
* [mfe-crossframework](https://github.com/igorhms/mfe-crossframework) - 具有 Angular Host、跨框架远程且无 Nx 的模块联合项目。
* [npm-mfe-live-reload](https://www.npmjs.com/package/npm-mfe-live-reload) - 当远程微前端发生变化时，该工具会在开发模式下自动重新加载 shell。

### 莫诺回购

* [Moon](https://moonrepo.dev/docs/guides/examples/angular) - 一个基于 Rust 的网络构建和 monorepo 管理工具。
* [Nx](https://github.com/nrwl/nx) - 具有集成工具和高级 CI 功能的构建系统，用于在本地和 CI 中维护和扩展 monorepos。
* [Turbo](https://github.com/vercel/turbo) - 用于 JavaScript 和 TypeScript 的 Turbopack（Rust 捆绑程序）和 Turborepo（构建系统/monorepo 工具）。

### 服务器端渲染

* [Official website](https://angular.dev/guide/ssr#enable-server-side-rendering) - 框架中内置的新 SSR 包的文档。
* [angular-prerender](https://github.com/chrisguttandin/angular-prerender) - 用于预渲染 Angular 应用程序的命令行工具。
* [analogjs](https://analogjs.org/) - Fullstack Angular 元框架支持 Angular 应用程序的服务器端渲染 (SSR) 和静态站点生成 (SSG)。
* [bot-ssr](https://github.com/patrikx3/bot-ssr) - 适用于机器人的 SSR，适用于用户的即时 CSR — 适用于主要爬虫的快速加载和干净的预渲染 HTML，由 [isbot](https://github.com/omrilotan/isbot) 提供支持。
* [ngx-sitemaps](https://github.com/json-derulo/ngx-sitemaps) - 从 Angular 预渲染的路线生成站点地图。
* [ngx-bun](https://github.com/pegasusheavy/ngx-bun) - 使用 Bun 内置服务器的适用于 Angular 19+ 的高性能 SSR/SSG 适配器。

## 开发实用程序

### 无障碍

* [Official Angular ARIA](https://angular.dev/guide/aria/overview) - 实现常见 WAI-ARIA 模式的无头、可访问指令的集合。
* [digital.gov](https://digital.gov/guides/accessibility-for-teams/) - 美国政府的团队无障碍指南。
* [WAI](https://www.w3.org/WAI/) - W3C Web 可访问性倡议 (WAI) 开发标准和支持材料来帮助您了解和实施可访问性。
* [webaim](https://webaim.org/) - 牢记网络可访问性。
* [WAVE](https://wave.webaim.org/) - 网络可访问性评估工具。
* [axe Accessibility Linter](https://marketplace.visualstudio.com/items?itemName=deque-systems.vscode-axe-linter) - HTML、Angular、React、Markdown、Vue 和 React Native 的辅助功能 linting。
* [Angular Material CDK - a11y](https://material.angular.io/cdk/a11y/overview) - a11y 软件包提供了许多工具来提高可访问性。
* [PrimeNG](https://primeng.org/guides/accessibility) - PrimeNG 的辅助功能指南。
* [astral-accessibility](https://github.com/verto-health/astral-accessibility) - 用 Angular 编写的开源辅助功能小部件。
* [angular-vlibras](https://github.com/angular-a11y/angular-vlibras) - 一个 Angular 库，集成了 VLibras，可自动将内容翻译为巴西手语 (Libra)。
* [a11y-libraries](https://github.com/LDV2k3/a11y-libraries) - 一系列适用于 Angular 的辅助功能解决方案。
* [a11yguard](https://github.com/shamaz332/a11yguard) - 提供零依赖辅助功能工具包，其中包含跨框架原语、惯用适配器以及映射到 EAA/EN301549 的运行时审核。
* [ulam](https://github.com/mikeyil/ulam) - 现代网络的辅助功能实用程序。 Vanilla-first，带有可选的 React、Remix、Vue 和 Angular 适配器。

### 人工智能

* [官方人工智能文档](https://angular.dev/ai)
* [官方 Angular CLI MCP 服务器设置](https://angular.dev/ai/mcp)
* [Official Angular Examples Repo](https://github.com/angular/examples) - 使用 [GenKit](https://firebase.google.com/docs/genkit) 和 AI 的 Angular 示例。
* [官方角度技能](https://github.com/angular/skills)
* [官方llms.txt文件](https://angular.dev/llms.txt)
* [官方 llms-full.txt 文件](https://angular.dev/assets/context/llms-full.txt)
* [abbi-ng-ai-image-descriptor](https://github.com/slsfi/abbi-ng-ai-image-descriptor) - 用于 AI 生成图像描述的 Angular Web 应用程序。您需要 OpenAI API 密钥才能使用该工具。
* [AGENT.md](https://ampcode.com/AGENT.md#tool-integration) - 通用代理配置文件。
* [agentbridge](https://github.com/ayoubachak/agentbridge) - 一个标准化人工智能代理如何发现、交互和控制应用程序组件的框架。
* [agent-rules-kit](https://github.com/tecnomanu/agent-rules-kit) - 用于 AI 的 CLI 工具，用于安装和配置规则以指导代理采用技术堆栈最佳实践。
* [agentskit](https://github.com/AgentsKit-io/agentskit) - 用于在 Angular 中构建 AI 代理的可组合工具包和无头聊天组件，具有流、工具、内存和 RAG。
* [aitools.fyi](https://aitools.fyi/technology/angular) - 使用 Angular 构建的 AI 工具。
* [angular-agent-framework](https://github.com/cacheplane/angular-agent-framework) - 用于构建代理应用程序 + 生成式 UI 的 Angular SDK。
* [Angular code editor rules](https://promptgenius.net/cursorrules/frameworks/frontend/angular) - 使用 Angular 代码时有效的 AI 交互模式指南。
* [@Kobolden/angular-skills](https://github.com/Kobolden/angular-skills) - 利用 AI 辅助编码技能增强您的 Angular 开发，其中包括最新模式、最佳实践和版本 20+ 的示例。
* [augment code](https://www.augmentcode.com/) - 第一个为专业软件工程师和大型代码库构建的人工智能编码助手。
* [CodingFleet](https://codingfleet.com/code-generator/angular/) - 一种创新的人工智能工具，可将您的指令转换为高效的 Angular 代码。
* [context7](https://github.com/upstash/context7) - MCP 服务器为 LLM 和 AI 代码编辑器提供最新的代码文档。
* [cursor.directory](https://cursor.directory/?q=angular) - 光标爱好者的家。
* [deep-chat](https://github.com/OvidijusParsiunas/deep-chat) - 适合您网站的完全可定制的人工智能聊天机器人组件。
* [Feature Search Agent - Angular PR Scout](https://github.com/dnlrbz/feature_search_agent) - 使用 Google 代理开发套件 (ADK) 构建的人工智能驱动代理，可自动搜索和分析 Angular 的 GitHub 拉取请求以获取新功能。
* [gitingest](https://gitingest.com/) - 将任何 Git 存储库转换为其代码库的简单文本摘要。这对于将代码库输入到任何 LLM 中非常有用。
* [glama](https://glama.ai/mcp/servers?query=angular) - 过滤 Angular 相关条目的 MCP 服务器目录。
* [hashbrown](https://github.com/liveloveapp/hashbrown) - [Hashbrown](https://hashbrown.dev/) 框架用于构建愉悦的、人工智能驱动的用户体验。
* [ngAutoPilot](https://github.com/janpereira-dev/ngAutoPilot) - 与代理无关的 Angular、TypeScript、JavaScript、RxJS、测试、代码质量、架构、版本控制和质量治理工作流程的微技能目录。
* [ng-mocks-testing-skill](https://github.com/mintarasss/ng-mocks-testing-skill) - 一系列 Claude 代码技能，用于使用 Jest 和“ng-mocks”编写高质量的 Angular 单元测试。
* [ngx-agents-md](https://github.com/pr4san/ngx-agents-md) - 将 Angular 文档添加到您的 AI 编码代理项目（Claude Code、Cursor 等）。
* [ngx-ai-devtools](https://github.com/ahmedkhan1/ngx-ai-devtools) - 无需离开浏览器选项卡即可查看应用程序花费的每个提示、响应、令牌和美元。
* [ngx-bob](https://github.com/scottstraughan/ngx-bob) - Angular 聊天小部件，具有消息传递、本地历史记录、错误处理、命令和搜索功能。
* [ngx-gen-ui](https://github.com/alessiopelliccione/ngx-gen-ui) - 用于通过 Firebase AI 流式传输生成 UI 内容的轻量级 Angular 指令和服务。
* [ngx-prompt-kit](https://github.com/PianoNic/ngx-prompt-kit) - 用于 AI 聊天界面的 Angular 组件，基于 Spartan UI 构建。
* [PureCode AI](https://purecode.ai/components/angular/application-ui) - 使用 PureCode AI 构建 Angular 应用程序 UI 的速度提高 50%。
* [reangular](https://github.com/AleksanderBodurri/reangular) - 一种编码代理技能，可将 React 库转换为具有完整功能奇偶校验、自动浏览器验证和并行奇偶校验的现代 Angular 库。
* [repomix](https://github.com/yamadashy/repomix) - 该工具可将整个存储库打包到单个 AI 友好的文件中。
* [rxjs-mcp-server](https://github.com/shuji-bonji/rxjs-mcp-server) - 直接从 Claude 等 AI 助手执行、调试和可视化 RxJS 流。
* [superconnect](https://github.com/bitovi/superconnect) - 一个人工智能驱动的工具，可以扫描您的 Figma 文件，探索您的 React 或 Angular 存储库，生成“.figma.tsx”或“.figma.ts”映射，并通过 Figma 的 CLI 将它们发布回来。
* [UI2CODE](https://ui2code.ai/) - 使用 AI 在几秒钟内完成 UI 到代码转换器。
* [web-codegen-scorer](https://github.com/angular/web-codegen-scorer) - 用于评估大型语言模型 (LLM) 生成的 Web 代码质量的工具。
* [Workik](https://workik.com/angular-code-generator) - 免费的人工智能驱动的 Angular 代码生成器 |您的情境驱动人工智能合作伙伴！
* [Yes Chat AI](https://www.yeschat.ai/gpts-ZxX35UdX-Angular-Ninja-%F0%9F%A5%B7) - Angular Ninja - Angular 开发助手。
* [Zipy](https://www.zipy.ai/online-tools/ai-angular-code-generator) - AI 角度代码生成器。

### 分析

* [@blue-cardinal/ngx-google-analytics](https://github.com/blue-cardinal/ngx-google-analytics) - 用于注入 Google Analytics 脚本的 Angular 模块，具有防止在开发环境中使用的保护措施。
* [clickstream-analytics-on-aws-web-sdk](https://github.com/aws-solutions/clickstream-analytics-on-aws-web-sdk) - 允许通过提供的数据管道将浏览器点击流数据收集到 AWS。
* [Heap](https://help.heap.io/hc/en-us/articles/37271957075345-Using-Heap-With-Popular-Web-Frameworks-Libraries) - 用于跟踪客户旅程、转化和保留的产品分析。
* [kitbase](https://docs.kitbase.dev/sdks/angular) - 用于产品分析和功能管理的开发人员平台。
* [litlyx](https://github.com/Litlyx/litlyx) - 一种开源分析工具——用一行代码即可设置。
* [@luzmo/ngx-embed](https://www.npmjs.com/package/@luzmo/ngx-embed) - 用于在 Angular 应用程序中嵌入 [Luzmo](https://www.luzmo.com/) 仪表板的库。
* [ngx-gtm](https://github.com/jerkovicl/ngx-gtm) - Angular 库，可自动注入使用 Google 跟踪代码管理器 (GTM) 所需的脚本标记。
* [ngx-material-tracking](https://github.com/Service-Soft/ngx-material-tracking) - 通过内置 Google Analytics、Meta Pixel 和自定义选项，为 Angular 网站提供符合 GDPR 的跟踪。
* [ngx-matomo-client](https://github.com/EmmanuelRoux/ngx-matomo-client) - 适用于 Angular 应用程序的 Matomo 分析客户端。
* [ngx-meta-pixel](https://github.com/Szymonexis/ngx-meta-pixel) - 该软件包使您能够为 Angular 应用程序设置 [Meta Pixel](https://www.facebook.com/business/tools/meta-pixel)。
* [ngx-piwik-pro](https://github.com/PiwikPRO/ngx-piwik-pro) - 用于实现标签管理器和跟踪的专用 [Piwik PRO](https://piwik.pro/) Angular 库。
* [oculr-ngx](https://github.com/Progressive-Insurance/oculr-ngx) - 一个分析库，使在 Angular 应用程序中收集数据变得简单。
* [plausible](https://github.com/plausible/analytics) - 具有 SPA 支持的轻量级、开源、隐私友好的分析 - 请参阅 [SPA 支持](https://plausible.io/docs/spa-support)。
* [rybbit](https://github.com/rybbit-io/rybbit) - Google Analytics 的隐私友好替代方案；有关 Angular 集成，请参阅此[指南](https://www.rybbit.io/docs/guides/angular)。
* [gizmo](https://gizmoanalytics.io/) - 谷歌分析的人工智能原生替代品，比竞争对手提供更慷慨的免费套餐。
* [ngx-segment-community](https://github.com/behdi/ngx-segment-community) - 社区维护的 [ngx-segment-analytics](https://github.com/opendecide/ngx-segment-analytics) 的后继者。
* [swetrix](https://github.com/Swetrix/swetrix) - [将 Swetrix 与您的 Angular 应用程序集成](https://swetrix.com/docs/angular-integration) 来跟踪页面视图、监控错误并捕获自定义事件 - 同时保持隐私友好和 GDPR 合规性。
* [@grandgular/logrocket-angular](https://github.com/Grandgular/logrocket) - LogRocket Web SDK 的包装器，具有 DI 友好的初始化、延迟加载、类型化选项、隐私帮助程序以及用于数据私有/数据公共的 DOM 指令。
* [ngx-umami](https://github.com/mitsuru17/ngx-umami) - [Umami Analytics](https://umami.is/) 的 Angular 集成 — 专为 Angular 应用程序量身定制的轻量级、隐私优先的跟踪解决方案。

### 代码分析

* [angular-compiler-output](https://github.com/JeanMeche/angular-compiler-output) - 查看给定 Angular 模板的 Angular 编译器的 JS 输出。
* [angular-doctor](https://github.com/antonygiomarxdev/angular-doctor) - 扫描您的项目是否存在 Angular 特定的 lint 问题和死代码，然后生成 0-100 的运行状况评分以及可操作的诊断。
* [angular-mermaider](https://github.com/earthdmitriy/angular-mermaider) - 生成 Mermaid 数据流图的静态代码分析器。
* [compuse](https://github.com/jakub-hajduk/compuse) - 用于分析代码库中 Angular 组件使用情况的统一 API。
* [modulens](https://github.com/sinanyilmaz0/modulens) - 一套用于前端工作区的体系结构、结构和质量分析工具。
* [ngcompass](https://github.com/RoadmapDevelop/ngcompass) - 针对架构、性能、SSR、安全性和代码质量的 Angular 感知静态分析。
* [ng-di-graph](https://github.com/m-yoshiro/ng-di-graph) - 一个命令行工具，用于分析 Angular TypeScript 代码库以提取依赖注入关系。
* [ng-lens](https://github.com/MerrittMelker/ng-lens) - 一个 Node.js 工具，使用“ts-morph”来分析 Angular 组件并检测任何 API 库中的服务使用模式。
* [ng-parsel](https://github.com/angular-experts-io/ng-parsel) - 将 Angular 代码库解析为 JSON 抽象 - 非常适合显示 API 和分析。
* [ngx-genie](https://github.com/SparrowVic/ngx-genie) - 一种可视化依赖注入树、分析服务状态、跟踪组件关系以及识别内存或架构问题的工具。
* [ngx-html-bridge](https://github.com/nagashimam/ngx-html-bridge) - 将 Angular 模板转换为静态 HTML 变体，从而使用任何标准 HTML 工具实现可靠的验证和 linting。
* [ngx-locator](https://github.com/Ea-st-ring/ngx-locator) - Angular 开发实用程序，用于从浏览器打开组件和模板，例如 [LocatorJS](https://www.locatorjs.com/)。
* [oxc-angular-compiler](https://github.com/voidzero-dev/oxc-angular-compiler) - 用 Rust 编写的高性能 Angular 模板编译器，利用 [Oxc](https://github.com/oxc-project/oxc) 基础设施实现超快编译。
* [ts-analyzer](https://github.com/amir-valizadeh/ts-analyzer) - 全面的 TypeScript 代码库分析器，提供有关类型安全性、代码复杂性和质量的详细指标。

### 调试

* [Bugfender](https://bugfender.com/platforms/angular-logging/) - 用于实时收集日志和 Angular 错误的云服务。
* [ngx-debug-console](https://github.com/andrerds/ngx-debug-console) - 适用于 Angular 14+ 应用程序的浮动调试控制台覆盖层。
* [ngrx-devtool](https://github.com/AmadeusITGroup/ngrx-devtool) - 用于可视化和调试 NgRx 状态管理的开发工具。
* [ngx-dev-toolbar](https://github.com/alfredoperez/ngx-dev-toolbar) - 用于 Angular 应用程序的强大开发工具栏，可直接在浏览器中提高开发人员的工作效率。
* [omelet-angular-debug-panel](https://github.com/maycuatroi1/omelet-angular-debug-panel) - Angular 调试仪表板提供 SQL 活动、服务器计时和身份验证调试的可见性。
* [angular-scan](https://github.com/husseinAbdElaziz/angular-scan) - 自动检测并突出显示正在重新渲染的 Angular 组件。
* [angular-render-scan](https://github.com/edisonaugusthy/angular-render-scan) - 用于 Angular 变化检测的可视化调试覆盖层。
* [rxjs-leak-finder](https://github.com/FlorinCiocirlan/rxjs-leak-finder) - 一种开发模式工具，可在 Angular 应用程序中查找泄露的 RxJS 订阅。
* [form-lens-angular](https://github.com/hebertdelima13/form-lens-angular) - 在开发过程中，直接在应用程序内部检查表单结构、控件状态、验证错误和嵌套表单树。

### 文档工具

* [Storybook](https://github.com/storybooks/storybook) - 您会喜欢使用的 UI 开发环境。
* [Compodoc](https://github.com/compodoc/compodoc) - 您的 Angular 应用程序缺少文档工具。
* [ng-doc](https://github.com/ng-doc/ng-doc) - Angular 项目的文档引擎。
* [docgeni](https://github.com/docgeni/docgeni) - 一个现代的、强大的、开箱即用的文档生成器，用于 Angular 组件库和 markdown 文档。
* [ng-component-hierarchy-visualizer](https://github.com/timonkrebs/ng-component-hierarchy-visualizer) - 一个不显眼的工具，可以根据路由配置生成 Angular 组件层次结构的 Mermaid 图。
* [easy-template-x-angular-expressions](https://github.com/alonrbar/easy-template-x-angular-expressions) - 角度表达式支持 [easy-template-x](https://github.com/alonrbar/easy-template-x)。
* [story-ui](https://github.com/southleft/story-ui) - 通过人工智能驱动的对话生成 Storybook 故事，从而自动化组件文档，与许多 LLM 提供商兼容。
* [envguards](https://github.com/princeofv/envguards) - 与框架无关的环境变量验证、文档生成器和“.env.example”创建器。

### IDE 扩展

* [AngularCliPlus](https://github.com/danisss9/AngularCliPlus) - Angular CLI 命令、原理图生成器和 VS Code 项目工具。
* [angular-code-quality-toolkit](https://github.com/Arul1998/angular-code-quality-toolkit) - [VS Code 扩展](https://marketplace.visualstudio.com/items?itemName=arul1998.angular-code-quality-toolkit) 用于运行 Angular 代码质量工具（depcheck、ts-prune、ESLint）并帮助清理未使用的代码和依赖项。
* [Angular Dev Tools](https://angular.dev/tools/devtools) - 用于调试和分析 Angular 应用程序的浏览器扩展。
* [Angular Extension Pack](https://marketplace.visualstudio.com/items?itemName=loiane.angular-extension-pack) - 该扩展包打包了一些最流行的 VS Code Angular 扩展。
* [Angular File Generator](https://marketplace.visualstudio.com/items?itemName=imgildev.vscode-angular-generator) - 通过直观、快速的文件生成来增强您的 Angular 开发。
* [Angular Schematics Pro](https://cyrilletuzi.gumroad.com/l/schematicspro) - Visual Studio Code 中的终极 Angular 代码生成。
* [Angular Schematics](https://marketplace.visualstudio.com/items?itemName=cyrilletuzi.angular-schematics) - Visual Studio Code 中的终极代码生成。
* [GraphLens](https://github.com/GraphLens/graphlens) - Angular 项目的交互式架构可视化工具。
* [Ionic VS Code Extension](https://ionicframework.com/docs/intro/vscode-extension) - 执行开发 Ionic 应用程序时常见的各种功能，所有这些都无需离开 VS Code 窗口。
* [mini-typescript-hero](https://github.com/angular-schule/mini-typescript-hero) - 轻量级、现代的 VSCode 扩展，可自动管理您的导入语句。
* [ngx-html-syntax](https://github.com/princemaple/ngx-html-syntax) - [Sublime Text](https://www.sublimetext.com/) 的 Angular HTML 语法。
* [Nx Console](https://marketplace.visualstudio.com/items?itemName=nrwl.angular-console) - 花更少的时间查找命令行参数，花更多的时间交付令人难以置信的产品。
* [Redux DevTools](https://github.com/reduxjs/redux-devtools/) - 可以与“@ngrx/store-devtools”结合使用来检查 NgRx 应用程序的状态。
* [vscode-angulartools](https://github.com/CoderAllan/vscode-angulartools) - 您可以探索 Angular 项目、增强文档、逆向工程代码以及使用 [AngularTools](https://marketplace.visualstudio.com/items?itemName=coderAllan.vscode-angulartools) 进行重构。
* [VS Code Angular HTML](https://marketplace.visualstudio.com/items?itemName=ghaschel.vscode-angular-html) - Angular HTML 模板文件的语法突出显示。
* [vscode-angular-auto-import](https://github.com/ngx-rock/vscode-angular-auto-import) - 根据模板中使用的选择器自动建议并插入缺少的 Angular 组件导入。
* [zed-angular](https://github.com/nathansbradshaw/zed-angular) - 此扩展将 Angular 语言服务集成到 [Zed](https://zed.dev/) 中。

### 发电机和脚手架

* [angular-scaffold](https://github.com/EPAM-JS-Competency-center/angular-scaffold) - 使用生产项目所需的所有工具搭建 Angular 项目。
* [ngx-schematics-utilities](https://github.com/DSI-HUG/ngx-schematics-utilities) - Angular Schematics 的有用实用程序。
* [abp](https://github.com/abpframework/abp) - 适用于具有固定架构的企业应用程序的开源 ASP.NET Core 框架。
* [LymeStack](https://www.lymestack.com/) - 全栈 Web 应用程序模板和工具集，可帮助小型团队快速构建和增强应用程序。
* [spiderly](https://github.com/filiptrivan/spiderly) - 一个“.NET”(C#) 生成器，可将 EF Core 模型转换为可自定义的“.NET”和 Angular 应用程序。
* [generator-jhipster-ionic](https://github.com/jhipster/generator-jhipster-ionic) - 您可以使用它生成与 JHipster 后端对话的 Ionic 应用程序。
* [Node Initializr](https://start.nodeinit.dev/) - 快速收集应用程序的依赖项并为您处理大部分初始设置。
* [nx](https://nx.dev/nx-api/angular) - 该插件提供了用于管理应用程序和库的执行器、生成器和实用程序。
* [skulljs](https://skulljs.github.io/) - 提供标准化文件结构，用于使用流行的 JavaScript 和 TypeScript 框架构建 Web 应用程序。
* [teleport-code-generators](https://github.com/teleporthq/teleport-code-generators) - 现代 JavaScript 应用程序的代码生成器集合。
* [Bootify.io](https://bootify.io) - 使用自定义数据库、Angular 前端和 CRUD 功能生成 Spring Boot 应用程序。
* [jangular-cli](https://github.com/nathangtg/jangular-cli) - Spring Boot + Angular 入门套件，具有 JWT 身份验证、Flyway 迁移、路由保护和 CLI 设置。
* [enterprise-java-saas-starter-kit](https://github.com/zukovlabs/enterprise-java-saas-starter-kit) - 生产就绪的 SaaS 入门工具，包含 Java 21、Spring Boot 3.4、Angular 21（独立 + 信号）、MSSQL、JWT auth 和 Docker Compose。
* [SaaS Starter](https://github.com/sayahweb2-png/saas-starter-lite) - 生产就绪的 NestJS + Angular 21 SaaS 样板，具有 JWT/OAuth/2FA 身份验证、Stripe 支付、多租户、RBAC、BullMQ、Docker、Terraform 和 55 多个测试。
* [JHipster](https://www.jhipster.tech) - 适用于 Spring Boot 和 Angular 的开源应用程序生成器。
* [ng-openapi](https://github.com/ng-openapi/ng-openapi) - Angular OpenAPI 客户端生成器。
* [tmf](https://github.com/tripsnek/tmf) - Eclipse 建模框架 (EMF) 的轻量级 TypeScript 端口，用于跨 Node.js、Java 和 Angular/React 的模型驱动、类型安全的数据模型。
* [polyfront-scaffold](https://github.com/NirmalSamaranayaka/polyfront-scaffold) - 一个生成器，提供广泛的配置选项来构建灵活、可扩展的 Angular 应用程序。
* [orval](https://github.com/orval-labs/orval) - 根据您的 OpenAPI 规范在前端应用程序中生成、验证、缓存和模拟。
* [angular-sitemap-generator](https://github.com/borisonekenobi/angular-sitemap-generator) - 为 Angular 项目生成“sitemap.xml”文件。
* [AutoFormsBuilderFilesGenerator](https://github.com/XHAlawa/AutoFormsBuilderFilesGenerator) - 使用“ng-openapi-gen”从 OpenAPI/Swagger 生成 Angular 表单，具有强大的类型、验证和 UI 帮助器。
* [ngx-autogen](https://github.com/barcidev/ngx-autogen) - 一组示意图，通过生成最佳实践代码并减少重复的设置任务来简化 Angular 工作流程。
* [angular-momentum](https://github.com/TheGameKnave/angular-momentum) - 以最少的配置在单一存储库中快速启动 Angular 项目。
* [swaggular](https://github.com/AlexMA2/swaggular) - 一种根据 Swagger/OpenAPI 规范生成 Angular 服务和模型的工具。
* [prism](https://github.com/arclight-digital/prism) - 从 Lit Web 组件自动生成框架包装器（React、Vue、Svelte、Angular、Solid、Preact）和 HTML/CSS 示例。
* [momentum-cms](https://github.com/DonaldMurillo/momentum-cms) - 基于 Angular 的无头 CMS。在 TypeScript 中定义集合，自动生成管理 UI、REST API 和数据库架构。

### 国际化

* [angular-ecmascript-intl](https://github.com/json-derulo/angular-ecmascript-intl) - 包含使用 Intl.* 浏览器 API 转换国际化数据的管道。
* [angular-i18next](https://github.com/Romanchuk/angular-i18next) - [i18next](https://www.i18next.com/) 的角度集成。
* [angular-intlayer](https://www.npmjs.com/package/angular-intlayer) - 这个 [intlayer](https://github.com/aymericzip/intlayer) 包允许您国际化您的 Angular 应用程序。它为 Angular 国际化提供上下文提供者和挂钩。
* [angular-locale-chain](https://github.com/i18n-agent/angular-locale-chain) - Angular 和 Transloco 的智能区域设置后备链。
* [angular-translation-checker](https://github.com/ricardoferreirades/angular-translation-checker) - 一个“ngx-translate”工具，可以检测未使用或丢失的键以保持 i18n 文件干净。
* [Crowdin](https://crowdin.com/) - 由人工智能驱动的本地化软件，通过 600 多个应用程序和[集成](https://store.crowdin.com/search?query=angular) 实现内容翻译自动化。
* [doloc](https://doloc.io/) - [Angular](https://doloc.io/getting-started/frameworks/angular/) 工作流程中的即时翻译。
* [I18N](https://github.com/soluling/I18N) - Soluling 为“.NET”、Angular 和 Delphi 实现了一系列国际化 (I18N) API。
* [i18n-keygen](https://github.com/gagle/i18n-keygen) - 适用于每个构建工具的类型安全 i18n 密钥。一包，零锁定。
* [i18n-scanner-toolkit](https://github.com/58bcbedf47bd91439c/i18n-scanner-toolkit) - 通过 CSV 导出/导入提取、检测缺失的翻译并管理多语言内容。
* [intl-tel-input-ng](https://github.com/mpalourdio/intl-tel-input-ng) - 一个 Angular 组件，可轻松集成 [intl-tel-input](https://github.com/jackocnr/intl-tel-input)。
* [langsync](https://github.com/mariokreitz/langsync) - 用于 TypeScript 项目中本地化工作流程的 CLI 工具。
* [localess](https://github.com/Lessify/localess) - 使用 Angular 和 Firebase 构建的强大翻译管理工具和内容管理系统。
* [ng-extract-i18n-merge](https://github.com/daniel-sc/ng-extract-i18n-merge) - 提取并合并 Angular 项目的 i18n xliff 翻译文件。
* [ng-linguo](https://github.com/jmwierzbicki/linguo) - 现代 Angular 18+ i18n 工具包构建在 SignalStore 上 - 一个响应式、从头开始的替代方案，可替代 `@ngx-translate/core` 和 Transloco，组件中的 RxJS 为零。
* [ngx-atomic-i18n](https://github.com/viacharles/ngx-atomic-i18n) - 具有延迟加载功能的 Angular 翻译库。
* [ngx-bidi](https://github.com/ystolyarchuk/ngx-bidi) - 用于自动或手动 LTR/RTL 文本方向的 Angular 库，具有指令、“NgxBidiService”、SCSS mixins 和模块/独立支持。
* [ngx-directo](https://github.com/ahmaed0hakam/ngx-directo) - 基于 Angular 18+ Signals 的库，用于 RTL/LTR 方向性、阿拉伯语本地化和 Google Font 编排。
* [ngx-easy-i18n-js](https://github.com/gabrie-allaigre/ngx-easy-i18n-js) - Angular 的简单国际化 (i18n) 库。
* [ngx-g11n](https://github.com/DSI-HUG/ngx-g11n) - 用于国际化和本地化应用程序的 Angular 助手。
* [ngx-i18n-extract-regex-cli](https://github.com/Celtian/ngx-i18n-extract-regex-cli) - 使用正则表达式从 Angular 应用程序中提取翻译的工具。
* [ngx-i18n-tools](https://github.com/Ascor8522/ngx-i18n-tools) - 用于翻译 Angular 应用程序的工具，包括 Excel/XLIFF 转换器 - [ngx-xlf-xlsx](https://github.com/Ascor8522/ngx-i18n-tools/tree/master/ngx-xlf-xlsx)。
* [ngx-localized-router](https://github.com/odomanskyi/ngx-localized-router) - 一个轻量级 Angular 库，可通过向 URL 添加语言段来帮助您本地化应用程序路由。
* [ngx-runtime-i18n](https://github.com/AshwinSathian/ngx-runtime-i18n) - Angular 的运行时国际化 — 信号优先、SSR 安全和框架无关的核心。
* [ngx-signal-translate](https://github.com/adamcsk1/ngx-signal-translate) - 信号驱动的翻译服务。
* [ngx-tolgee](https://github.com/tolgee/tolgee-js/tree/main/packages/ngx/projects/ngx-tolgee) - 基于 Web 的本地化工具，使用户能够直接在他们开发的 Angular 应用程序中进行翻译。
* [ngx-translate](https://github.com/ngx-translate/core) - Angular 的国际化 (i18n) 库。
* [@OGS-GmbH/ngx-translate](https://github.com/OGS-GmbH/ngx-translate) - 一个轻量级的 Angular i18n 库，具有基于 REST 的设置、动态语言切换和灵活的翻译管理。
* [ngx-translate-cut](https://github.com/bartholomej/ngx-translate-cut) - 用于切割翻译的角管 ✂️ 🌍（`@ngx-translate` 的插件）。
* [ngx-translate-lint](https://github.com/romanrostislavovich/ngx-translate-lint) - 用于检查“ngx-translate”键的简单 CLI 工具。
* [ngx-translate-messageformat-compiler](https://github.com/lephyrus/ngx-translate-messageformat-compiler) - `ngx-translate` 的编译器使用 [messageformat.js](https://github.com/messageformat/messageformat) 使用 ICU 语法编译翻译来处理复数和性别。
* [ngx-translate-module-loader](https://github.com/larscom/ngx-translate-module-loader) - 用于“@ngx-translate/core”的高度可配置且灵活的翻译加载器。
* [ngx-translate-multi-http-loader](https://github.com/rbalet/ngx-translate-multi-http-loader) - ngx-translate 的加载器，通过 http 调用加载翻译。
* [ngx-translate-phraseapp](https://github.com/phrase/ngx-translate-phraseapp) - 用于将 [短语字符串上下文编辑器](https://support.phrase.com/hc/articles/5784095916188-In-Context-Editor-Strings) 与 Angular 应用程序中的“ngx-translate”集成的官方库。
* [ngx-translate-routes](https://github.com/darioegb/ngx-translate-routes) - 该服务翻译标题和路线路径。
* [ngx-translate-toolkit](https://github.com/robmanganelly/ngx-translate-toolkit) - 一个 Angular 库，旨在扩展“@ngx-translate/core”并简化大型项目中管理翻译的过程。
* [ngx-translate-version](https://github.com/Celtian/ngx-translate-version) - 为语言文件提供版本的 Angular 模块。
* [ruci](https://github.com/njirolu/ruci) - 一个 CLI 工具，通过“ngx-translate”简化 Angular 项目中的 i18n 验证，确保准确、高质量的翻译。
* [runtime-localizer](https://forge.deejayy.hu/angular-packages/runtime-localizer) - Angular 的运行时本地化程序。
* [rust-ngx-translate-lint](https://github.com/hafnerpw/rust-ngx-translate-lint) - 用于提高性能的“ngx-translate-lint”的 Rust 端口。
* [signal-translate](https://github.com/NGneers/signal-translate) - 以信号为核心的翻译服务。
* [Transifex](https://github.com/transifex/transifex-javascript/tree/master/packages/angular/projects/tx-native-angular-sdk) - 您可以使用 [Transifex 库扩展](https://www.npmjs.com/package/@transifex/angular) 轻松本地化 Angular 组件。该库扩展了 [Transifex Native JavaScript SDK](https://developers.transifex.com/docs/javascript-sdk) 的功能。
* [TransLatte](https://github.com/Marbulinek/TransLatte) - 一个使用 Lingva API 生成翻译 JSON 文件的 CLI 工具。
* [transloco](https://github.com/jsverse/transloco) - Angular 的国际化 (i18n) 库。
* [transloco-keys-manager](https://github.com/jsverse/transloco-keys-manager) - 帮助减少单调工作的工具。
* [xlf-sync](https://github.com/atheodosiou/xlf-sync) - 用于同步 Angular XLIFF（1.2 和 2.0）区域设置文件的 CLI 工具。

### 棉绒

* [@ni/javascript-styleguide](https://github.com/ni/javascript-styleguide) - NI 针对 ESLint 的 JavaScript 和 TypeScript linter 规则。
* [@yoo-digital/eslint-plugin-angular](https://github.com/yoo-digital/eslint-plugin-angular) - Angular 的自定义 lint 规则。
* [angular-eslint](https://github.com/angular-eslint/angular-eslint) - Monorepo 提供所有使 ESLint 能够检查 Angular 项目的工具。
* [angular-eslint-injection-context](https://github.com/cyrilletuzi/angular-eslint-injection-context) - Angular 注入上下文的 ESLint 规则有助于防止 [NG0203](https://angular.dev/errors/NG0203) 错误。
* [angular-eslint-zoneless](https://github.com/cyrilletuzi/angular-eslint-zoneless) - 检查无区域应用程序是否不使用基于 Zone.js 的功能以及是否使用信号/资源模式。
* [eslint-config-angular-strict](https://github.com/Jbz797/eslint-config-angular-strict) - 现代 ESLint 配置，具有严格的 Angular 开发规则。
* [eslint-config-spartan](https://github.com/glitch452/eslint-config-spartan) - 一个固执己见的 ESLint 配置，为各种 eslint 插件提供单独的配置（称为 mixins）。
* [eslint-plugin-ng-module-sort](https://github.com/ducktordanny/eslint-plugin-ng-module-sort) - 自动排序 Angular 和 NestJS 模块数组，以保持模块整洁有序。
* [ngx-html-bridge-markuplint](https://github.com/nagashimam/ngx-html-bridge-markuplint) - 该库通过将 Markuplint 反向编译为 HTML，将 Markuplint 链接到 Angular 模板，从而通过正确的源映射报告实现准确的 linting。
* [eslint-config-neon](https://github.com/iCrawl/eslint-config-neon) - 全面的可共享 ESLint 配置。
* [eslint-config-angular](https://github.com/noneforge/eslint-config-angular) - 全面的 Angular ESLint 配置，具有 TypeScript 支持、组件/模板规则、可访问性和 CSS linting。
* [linters](https://github.com/developer239/linters) - ESLint / StyleLint 和其他代码质量工具的超严格配置集合。
* [eslint-plugin-angular-class-ordering](https://github.com/Leritas/eslint-plugin-angular-class-ordering) - ESLint 插件，通过自动修复功能使 Angular 类成员（字段和方法）保持一致的顺序。
* [lint-a-lot](https://github.com/JanKru/lint-a-lot) - 使用现代扁平配置的 Angular 项目的固执己见的 ESLint 和 Stylelint 配置。
* [neighbor](https://github.com/a11yfred/neighbor) - 在发布之前捕获标记、CSS 和副本中的辅助功能问题。

### 网络

* [angular-http-server](https://github.com/simonh1000/angular-http-server) - 用于单页应用程序 (SPA) 的简单 http 服务器。
* [ngx-device-detector](https://github.com/AhsanAyaz/ngx-device-detector) - 用于检测设备、操作系统和浏览器详细信息的 Angular v7+ 库。
* [ngx-offline-indicator](https://github.com/thdang1009/ngx-offline-indicator) - 一种简单且可定制的方式来通知用户其 Angular 应用程序中的互联网连接状态。

### 性能

* [angular-rust-compiler](https://github.com/truonglvos/angular-rust-compiler) - 用 Rust 编写的高性能 Angular AOT 编译器，提供 Angular 组件和指令的完全静态编译。
* [detective](https://github.com/angular-architects/detective) - 在架构级别使用取证代码分析来揭示代码库中隐藏的模式。
* [esbuild Bundle Size Analyzer](https://esbuild.github.io/analyze/) - 可视化 esbuild 包的内容。
* [hawkeye](https://github.com/angular-experts-io/hawkeye) - 一种可视化和优化 JavaScript 捆绑包、揭示影响性能的模块、依赖项和资产的工具。
* [microwave](https://github.com/jscutlery/devkit/tree/main/packages/microwave) - 轻松优化 Angular 变化检测。
* [ng-event-plugins](https://github.com/taiga-family/ng-event-plugins) - 一个小型库，用于优化性能敏感事件的变更检测周期。
* [ng-queuex](https://github.com/dagnygus/ng-queuex) - 实验性 Angular 生态系统，具有类似 React 的调度程序和用于细粒度变化检测的信号驱动指令。
* [ng-reactive-lint](https://github.com/Shrinivassab/ng-reactive-lint) - 特定于 Angular 的 linter，通过 Signals 和 RxJS 强制执行最佳反应模式。
* [ngx-idle-monitor](https://github.com/giorgi1441/ngx-idle-monitor) - 一种轻量级 Angular 服务，用于跟踪用户活动、管理会话超时以及跨选项卡同步空闲状态。
* [ngx-network-monitor](https://github.com/MadeByRaymond/ngx-network-monitor) - 用于监控网络状态的轻量级 Angular 服务：在线/离线、连接质量 (2G/3G/4G/5G) 和 ping 延迟。
* [ngx-performance-diagnostics](https://github.com/maciekv/ngx-performance-diagnostics) - 零设置即可发现 Angular 应用程序中的性能瓶颈、过多的变更检测周期和内存泄漏。
* [ngx-script-optimizer](https://github.com/Mohid123/ngx-script-optimizer) - 一个轻量级的 Angular 库，旨在增强您的第三方脚本处理能力。
* [ngx-unused](https://github.com/wgrabowski/ngx-unused) - 在代码库中查找已声明但未使用的 Angular 类。
* [ngx-worker-bridge](https://github.com/yashwantyashu/worker-bridge) - 用于 Angular 和 React 的轻量级、零样板反应桥，使 Web Workers（专用和共享）像调用常规方法一样简单。
* [sonda](https://github.com/filipsobol/sonda) - JavaScript 和 CSS 的通用可视化工具和分析器。

### 运行时

* [angular-compile](https://github.com/patrikx3/angular-compile) - 角度动态编译。将字符串转换为 Angular 组件。
* [deepequalspure](https://github.com/puckowski/deepequalspure) - JavaScript 对象深度等于为 Angular 项目提供服务。
* [lbx-change-sets](https://github.com/Service-Soft/lbx-change-sets) - 使用可扩展的基础存储库自动跟踪实体更改。
* [ng-noop](https://github.com/joeskeen/ng-noop) - 一个最小的、无 DOM 的 Angular 平台，用于自定义运行时、CLI、服务器和实验渲染器。
* [ngx-api-mimic](https://github.com/mateuszbilicz/ngx-api-mimic) - 该库允许您使用 Angular 的 HTTP 拦截器来模拟数据并模拟虚假 API。
* [ngx-compare-object](https://github.com/RzoDev/ngx-compare-object) - 用于将原始对象与其修改版本进行比较的 Angular 实用程序。
* [ngx-json-reader](https://github.com/Verbalman/ngx-json-reader) - Angular 17+ JSON 阅读器/编辑器，具有多 URL 比较和差异功能。
* [runtime-config-loader](https://github.com/pjlamb12/runtime-config-loader) - Angular 库提供了一种简单的方法来加载配置 JSON 文件以进行运行时配置。

### 搜索引擎优化

* [@davidlj95/ngx-meta](https://ngx-meta.dev) - 通过 SSR 支持快速设置 Angular 站点元数据（元标签、Open Graph、X Cards、JSON-LD）。
* [ngx-seo](https://github.com/samvloeberghs/kwerri-oss/tree/main) - Kwerri OSS：samvloeberghs.be + ngx-seo。
* [Angular React SEO](https://github.com/ganatan/angular-react-seo) - Angular 和 React 示例 SEO（搜索引擎优化）。
* [unhead](https://www.npmjs.com/package/@unhead/angular) - Angular 应用程序的全栈“<head>”管理。

### 造型

* [Angular-Material-Tailwind-Integration](https://github.com/adandedjanstephane-git/Angular-Material-Tailwind-Integration) - 一组稳定的、可主题化的 CSS 自定义属性，将 Material Design System 标记映射到 Tailwind CSS 实用程序类。
* [element-identifier](https://github.com/jooherrera/element-identifier) - 创建可靠、独特的 CSS 选择器来定位 DOM 元素，并利用 Web 组件进行视觉检查和选择。
* [Material Theme Builder](https://www.materialthemebuilder.com/) - 为您的应用程序提供实时 Angular Material 主题。
* [ngx-angora-css](https://github.com/LynxPardelle/ngx-angora-css) - 一个基于 JavaScript 的 CSS 框架，可在页面加载时动态生成样式。
* [ngx-classed](https://github.com/lukonik/ngx-classed) - 库允许您根据状态动态添加或删除类。
* [ngx-css](https://github.com/squidit/ngx-css) - [Squid CSS](https://github.com/squidit/css) 的 Angular 抽象。
* [ngx-mq](https://github.com/martsinlabs/ngx-mq) - 一个声明性库，使用信号和本机 [matchMedia API](https://developer.mozilla.org/en-US/docs/Web/API/Window/matchMedia) 来管理媒体查询，并为 Tailwind、Bootstrap 和 Angular Material 提供内置断点预设。
* [ngx-responsive-signals](https://github.com/irvrodflo/ngx-responsive-signals) - Angular 基于信号的响应断点。
* [ngx-theme-stack](https://github.com/WanderleeDev/ngx-theme-stack) - 现代、SSR 安全的 Angular 库，用于通过 Angular Signals 管理暗模式、亮模式和自定义主题。
* [panda](https://github.com/chakra-ui/panda) - 轻松使用 Panda、CSS-in-JS 框架以及 Angular 及其专用的[集成](https://panda-css.com/docs/docs/installation/angular)。
* [prime-ng-theme-fe](https://github.com/mkccl/prime-ng-theme-fe) - PrimeNG 的视觉主题设计师。
* [Super JSS](https://github.com/rsantoyo-dev/super-jss-workspace) - Super JavaScript Stylesheets 是一个小型 Angular 运行时库，可生成带有断点和主题的原子 CSS。
* [Theme-Kit](https://github.com/M1tsumi/Theme-Kit) - 统一的设计令牌 SDK，可集中您的颜色、版式和间距，以便在 React、Vue、Angular 或任何 JavaScript 项目中无缝使用。
* [tokiforge](https://github.com/TokiForge/tokiforge) - 适用于 React、Vue、Angular、Svelte 和 vanilla JS 的与框架无关的设计令牌引擎。
* [ukit-css](https://github.com/vcalderondev/ukit-css) - JIT 实用程序优先的 CSS 引擎 - 适用于任何前端堆栈（React、Vue、Angular、Svelte、Next.js、Astro、纯 HTML）的 Tailwind 式按需类生成。

## 安全与认证

### 认证

* [angular-auth-oidc-client](https://github.com/damienbod/angular-auth-oidc-client) - 用于 OpenID Connect、带有 PKCE 的 OAuth 代码流、刷新令牌和隐式流的 NPM 包。
* [angular-oauth2-oidc](https://github.com/manfredsteyer/angular-oauth2-oidc) - 支持 Angular 中的 OAuth 2 和 OpenId Connect (OIDC)。
* [angular-authentication](https://github.com/nikosanif/angular-authentication) - 一个 Angular 应用程序，演示用户身份验证和授权流程的最佳实践。
* [angularfire](https://github.com/angular/angularfire) - 角度 + Firebase。
* [angularx-social-login](https://github.com/abacritt/angularx-social-login) - Angular 17 的社交登录和身份验证模块。
* [angular2-jwt](https://github.com/auth0/angular2-jwt) - 用于在 Angular 应用程序中处理 JWT 的帮助程序库。
* [appwrite](https://github.com/appwrite/appwrite) - 将您的 [Angular 应用](https://appwrite.io/docs/quick-starts/angular) 与 [Appwrite](https://appwrite.io/) 集成，以实现身份验证、数据库、存储、功能等。
* [auth0-angular](https://github.com/auth0/auth0-angular) - 用于 Angular 单页应用程序的 Auth0 SDK。
* [authon-sdk](https://github.com/mikusnuz/authon-sdk/tree/main/packages/angular) - Angular SDK for [Authon](https://authon.dev/) — 服务、防护和拦截器。
* [authress-angular](https://github.com/mikepattyn/authress-angular) - 该软件包仅包含一个用于轻松设置和注册 [Authress](https://authress.io/) LoginClient 的模块。
* [@badisi/ngx-auth](https://github.com/Badisi/auth-js/tree/main/libs/ngx-auth) - 基于 Angular 的桌面和移动应用程序的身份验证和授权支持。
* [corbado](https://www.corbado.com/#signup-init) - [集成](https://docs.corbado.com/corbado-complete/frontend-integration/angular) Corbado 与 Angular 使用密钥进行身份验证。
* [fingerprint](https://dev.fingerprint.com/docs/angular) - Fingerprint Angular SDK 是将 Fingerprint 集成到 Angular 应用程序中的一种简单方法。
* [frontegg-angular](https://github.com/frontegg/frontegg-angular) - Angular 的托管登录 SDK；请参阅[快速入门](https://developers.frontegg.com/ciam/sdks/frontend/angular/hosted-login)。
* [FusionAuth Angular SDK](https://fusionauth.io/docs/sdks/angular-sdk) - 用于登录/注册、注销和刷新令牌处理的 Angular SDK。
* [hanko](https://github.com/teamhanko/hanko) - 按照此 [快速入门](https://docs.hanko.io/quickstarts/frontend/angular) 将开源身份验证和用户管理解决方案 [Hanko](https://www.hanko.io/) 集成到您的 Angular 应用程序中。
* [keycloak-angular](https://github.com/mauriciovigolo/keycloak-angular) - Angular 应用程序的简单 Keycloak 设置。
* [lbx-jwt](https://github.com/Service-Soft/lbx-jwt) - 为环回应用程序提供 JWT 身份验证。包括在令牌内存储角色和处理刷新。内置重用检测。
* [Logto](https://logto.io/) - 开源 Auth0 替代方案 (OIDC/OAuth2/SAML)。 Angular [快速入门](https://docs.logto.io/quick-starts/angular#preventions)。
* [Melody Auth](https://github.com/ValueMelody/melody-auth) - 它的 [SDK](https://www.npmjs.com/package/@melody-auth/angular) 可实现 Angular-melody 身份验证与自动状态、重定向和令牌处理的无缝集成。
* [MojoAuth](https://mojoauth.com/) - [集成](https://docs.mojoauth.com/guides/angular) 密钥的最简单方法。
* [msal-angular](https://github.com/AzureAD/microsoft-authentication-library-for-js/tree/dev/lib/msal-angular) - MSAL for Angular 允许 Angular 应用通过 [Azure AD](https://docs.microsoft.com/azure/active-directory/develop/v2-overview)、Microsoft 帐户以及通过 [Azure AD B2C](https://docs.microsoft.com/azure/active-directory-b2c/active-directory-b2c-overview#identity-providers) 的社交提供商对用户进行身份验证，并获取 Microsoft 服务的令牌，例如[图](https://graph.microsoft.io)。
* [ng-awesome-node-auth](https://github.com/nik2208/ng-awesome-node-auth) - [awesome-node-auth](https://github.com/nik2208/awesome-node-auth) 的角度拦截器和守卫。
* [ngx-better-auth](https://github.com/thomasorgeval/ngx-better-auth) - [Better Auth](https://github.com/better-auth/better-auth) 的 Angular 20+ 包装器。提供带有信号的反应式会话处理、带有可观察值的干净 DI 提供程序设置以及现代防护。
* [ngx-cognito-auth](https://github.com/SamsonGross/ngx-cognito-auth) - 使用 OAuth 2.0 授权代码流程和 PKCE 进行 AWS Cognito 身份验证的 Angular 21+ 库。
* [ngxfire](https://github.com/teve-no/ngxfire) - 无区域 AngularFire 替代品。
* [ngx-webauthn](https://github.com/JonnyHeavey/ngx-webauthn) - 一个 Angular 库，提供类型安全、简化的原生 WebAuthn API 抽象，并内置对标准类型的支持和常见用例的可选预设。
* [omni-auth](https://github.com/ngx-addons/omni-auth) - Angular 身份验证库提供身份验证流程、防护和错误处理的核心功能。
* [otp-angular](https://github.com/subha-patra/otp-angular) - 一款轻量级、高度可定制且无依赖性的 OTP（一次性密码）输入组件，专为 Angular 20+ 应用程序构建。
* [passlock](https://github.com/passlock-dev/passlock) - 适用于 Angular 和其他框架的无摩擦密钥身份验证。
* [@serhiisol/ngx-auth](https://github.com/serhiisol/ngx-auth) - Angular 20+ 身份验证模块。
* [Supabase](https://supabase.com/docs/guides/getting-started/tutorials/with-angular) - 使用 Angular 构建用户管理应用程序。
* [SuperTokens](https://supertokens.com) - 配置您的 [Angular](https://supertokens.com/docs/quickstart/frontend-setup) 应用程序以使用 SuperToken 进行身份验证。
* [witspry-auth-ng-client](https://github.com/satya-jugran/witspry-auth-ng-client) - 用于 OAuth2 身份验证的综合 Angular 库，支持 PKCE（代码交换证明密钥）。
* [zenuxs-oauth](https://github.com/developer-rs5/zenuxs-oauth) - 适用于现代应用程序的通用 OAuth 2.0 + PKCE 客户端。
* [zitadel](https://zitadel.com/docs/examples/login/angular) - 为您的应用程序提供安全的身份验证管理。通过简单的 API 和可编程工作流程，随着您的成长进行定制。专注于成长，您的登录名将得到妥善保管。

### 付款方式

* [adyen-angular-online-payments](https://github.com/adyen-examples/adyen-angular-online-payments) - 使用卡、钱包和主要本地支付方式在基于 Angular/Express 的网站上接受付款。
* [angular-spotflow-checkout](https://github.com/Spotflow-One/angular-spotflow-checkout) - [Spotflow](https://www.spotflow.one/) Angular SDK 使用户能够通过简化的结账体验进行付款。
* [google-pay-button](https://github.com/google-pay/google-pay-button) - Google Pay 按钮 - React、Angular 和自定义元素。
* [ngx-hyperpay](https://github.com/MagdyAbouelnasr/ngx-hyperpay) - 一个 Angular 库，可轻松集成 [HyperPay](https://www.hyperpay.com/) 支付网关。
* [ngx-mp-payments](https://github.com/JosemaCeballos/ngx-mp-payments) - 用于与 [Mercado Pago](https://www.mercadopago.com.ar/) 集成的 Angular 库。
* [ngx-stripe](https://github.com/richnologies/ngx-stripe) - StripeJS 和 [Stripe Elements](https://stripe.com/docs/stripe-js) 的 Angular 绑定。
* [ngx-supabase-stripe](https://github.com/dotted-labs/ngx-supabase-stripe) - 用于 Supabase + Stripe 支付/订阅的现成 Angular 组件。
* [solidgate](https://github.com/solidgate-tech/angular-sdk) - 借助其 Angular SDK，您可以添加 Solidgate 付款表格。

### 基于角色的访问控制

* [casl-angular](https://github.com/stalniy/casl/tree/master/packages/casl-angular) - 将同构权限管理库 [CASL](https://github.com/stalniy/casl) 与 Angular 集成的模块。
* [nblocks](https://www.nblocks.dev/) - 用于无缝管理身份验证、付款、订阅、功能和角色管理的控制中心。
* [ngx-can-i](https://github.com/kopy011/ngx-can-i) - 为 Angular 开发人员提供的一个包，可帮助他们处理权限。
* [ngx-permissions](https://github.com/AlexKhymenko/ngx-permissions) - Angular 应用程序基于权限和角色的访问控制（AOT，兼容惰性模块）。
* [ngx-role-accessor](https://github.com/IroshanRathnayake/ngx-role-accessor) - 企业级 Angular 基于角色的访问控制 (RBAC) 库。
* [ngx-signal-permissions](https://github.com/levart/ngx-signal-permissions) - 一个现代的、基于信号的 Angular 库，用于管理权限和角色，并具有完整的 TypeScript 支持。
* [ngx-smart-permissions](https://github.com/rami-sheikha-dev/ngx-smart-permissions) - 一个轻量级的 Angular 库，用于基于角色和权限的访问控制，支持独立组件和 NgModule。
* [ngxsmk-gatekeeper](https://github.com/NGXSMK/ngxsmk-gatekeeper) - 一种轻量级、开发人员友好的 Angular 中间件引擎，可通过一个可组合的设置来保护路由和 HTTP 请求。
* [permit](https://www.permit.io/) - 可以与 [Angular](https://www.permit.io/blog/how-to-implement-role-based-access-control-rbac-in-angular) 一起使用的授权即服务解决方案。
* [ng-ability](https://github.com/topaxi/ng-ability) - 在 Angular 中定义访问控制列表。

### 安全最佳实践

* [Official Angular Security](https://angular.dev/best-practices/security) - 最佳实践。
* [Aikido](https://www.aikido.dev/) - 在一个中央系统中保护您的代码、云和运行时。自动查找并修复漏洞。
* [GitHub Code Scanning](https://docs.github.com/en/code-security/concepts/code-scanning) - 了解 GitHub 代码扫描功能的核心概念。
* [GitHub Skills](https://skills.github.com/) - 提供了代码安全和分析的交互式指导教程。
* [HackTricks](https://book.hacktricks.xyz/network-services-pentesting/pentesting-web/angular) - 角度安全检查表。
* [SafeDep](https://safedep.io/) - 它持续扫描开源代码中的漏洞和恶意软件，帮助安全工程团队主动减轻继承的 OSS 风险。
* [Snyk](https://snyk.io/) - 直接集成到开发工具、工作流程和自动化管道中的开发人员安全平台。
* [Socket](https://socket.dev/) - 开发人员优先的安全平台，可保护您的代码免受易受攻击和恶意依赖的影响。
* [supply-chain-inspector](https://github.com/DenysVuika/supply-chain-inspector) - 一个独立的、零依赖的 Node.js 脚本，用于 npm 依赖项的供应链安全分析。
* [Vulert](https://vulert.com) - 通过检测开源依赖项中的漏洞来保护软件，而无需访问您的代码。它支持 JS、PHP、Java、Python 等。

## 状态管理

### NGRx

* [官方网站](https://ngrx.io/)
* [Official GitHub repository](https://github.com/ngrx/platform) - Angular 的反应状态。
* [ngrx-course](https://github.com/angular-university/ngrx-course) - Angular 大学完整指南。
* [ngrx-store-localstorage](https://github.com/btroncone/ngrx-store-localstorage) - `@ngrx/store` 和本地存储之间的简单同步。
* [ngrx-toolkit](https://github.com/angular-architects/ngrx-toolkit) - NgRx 信号存储的各种扩展。
* [ngrx-traits](https://github.com/gabrielguerrero/ngrx-traits) - NgRx Traits 是一个库，可帮助您在应用程序中编写和重用一组 NGRX 操作、选择器、效果和化简器。
* [ngrx-addons](https://github.com/Michsior14/ngrx-addons) - NgRx 插件的集合，包括状态持久性。
* [ngrx-store-storagesync](https://github.com/larscom/ngrx-store-storagesync) - localStorage/sessionStorage 和 @ngrx/store 之间高度可配置的状态同步库。
* [ngrx-wieder](https://github.com/nilsmehlhorn/ngrx-wieder) - 使用 NgRx 和 Immer.js 进行 Angular 的轻量级撤消重做。
* [ngrx-immer](https://github.com/timdeschryver/ngrx-immer) - 围绕 NgRx 方法 createReducer、on 和 ComponentStore 进行沉浸式包装。
* [ngrx-rtk-query](https://github.com/SaulMoro/ngrx-rtk-query) - 使用 Hooks 进行 RTK 查询可在 Angular 应用程序中使用。
* [angular-ngrx-nx-realworld-example-app](https://github.com/stefanoslig/angular-ngrx-nx-realworld-example-app) - 使用 Angular 21、NgRx 21 和 Nx 22 构建的真实世界应用程序。
* [ngx-view-state](https://github.com/yurakhomitsky/ngx-view-state) - 用于处理 NgRx 中的加载/成功/错误的库。
* [store-service](https://github.com/ngxp/store-service) - 在 Angular 组件和 NgRx 存储之间添加抽象层/外观。
* [ngx-signal-store-query](https://github.com/k3nsei/ngx-signal-store-query) - 与 [Angular Query](https://tanstack.com/query/latest/docs/framework/angular/overview) 桥接的信号存储功能。
* [SmartNgRX](https://github.com/DaveMBush/SmartNgRX) - 该库通过抽象 NgRx 来简化 CRUD 操作，同时仍然利用和支持现有的 NgRx 代码。
* [ngrx-hateoas](https://github.com/angular-architects/ngrx-hateoas) - 一个按照 HATEOAS 方法将超媒体 json 引入 NgRx Signal Store 的库。
* [ngrx-http-tracking](https://github.com/acandylevey/ngrx-http-tracking) - 该 NgRx 库与现有商店集成，以减少样板文件并简化处理 HTTP 请求状态（例如加载、成功和错误）。
* [ngrx-set](https://github.com/parloti/ngrx-set) - 这简化了为可能成功、失败或中止的异步请求操作的创建。
* [easy-ngrx-distinct-selector](https://github.com/NGneers/easy-ngrx-distinct-selector) - 提供函数来轻松创建具有相同函数的参数和结果值的“@ngrx/store”选择器。
* [ngrx-store-wrapper](https://github.com/himanshuarora111/ngrx-store-wrapper) - 用于 NgRx 状态管理的 Angular 库，具有内置会话和本地存储，无需手动操作或减速器。
* [ngx-rehydrate](https://github.com/solidexpert-ltd/ngx-rehydrate) - 用于 Angular SSR 应用程序的 NgRx 状态补水库。

### NGXS

* [官方网站](https://www.ngxs.io/)
* [Official GitHub repository](https://github.com/ngxs/store) - NGXS 旨在以最少的样板和维护来简化状态管理。
* [action-lifecycle-hooks](https://github.com/ngxs-labs/action-lifecycle-hooks) - 可以轻松地根据操作结果（例如成功或错误）触发代码，而无需手动操作连接。
* [actions-executing](https://github.com/ngxs-labs/actions-executing) - 该插件可让您轻松了解某个操作是否正在执行，并控制 UI 元素或控制要执行的代码流。
* [emitter](https://github.com/ngxs-labs/emitter) - 新模式提供了摆脱行动的机会。
* [firestore-plugin](https://github.com/ngxs-labs/firestore-plugin) - NGXS 的 Firestore 插件。
* [ngxs-postmessage-plugin](https://github.com/nelsongraa8/ngxs-postmessage-plugin) - NGXS 插件，使用“postMessage”跨窗口或微前端进行状态同步。
* [ngxs-synchronizers](https://github.com/lVlyke/ngxs-synchronizers) - 简化基于 NGXS 的应用程序状态与外部数据源的同步。

### 其他州立图书馆

* [ng-simple-state](https://github.com/nigrosimone/ng-simple-state) - Angular 中仅使用服务和 RxJS 进行简单的状态管理。
* [exome](https://github.com/Marcisbee/exome) - 用于深度嵌套状态的基于简单代理的状态管理器，可与 Angular Signals 和 RxJS 配合使用。
* [TanStack Query](https://github.com/TanStack/query) - 强大的异步状态管理、服务器状态实用程序和网络数据获取。
* [state-adapt](https://github.com/state-adapt/state-adapt) - 声明式增量状态管理库。
* [mini-rx-store](https://github.com/spierala/mini-rx-store) - 反应式状态管理平台。
* [ngx-collection](https://github.com/e-oz/ngx-collection) - Angular 的集合状态管理服务。
* [xstate](https://github.com/statelyai/xstate) - 针对复杂应用程序逻辑的基于参与者的状态管理和编排。
* [signalstory](https://github.com/zuriscript/signalstory) - 基于 Angular 信号构建的状态管理库，支持简单的存储库、解耦命令、副作用以及通过事件驱动架构进行的商店间通信。
* [ngx-sherlock](https://github.com/politie/ngx-sherlock) - 与 [@politie/sherlock](https://github.com/politie/sherlock) 分布式反应式状态管理库一起使用的 Angular 工具库。
* [tansu](https://github.com/AmadeusITGroup/tansu) - 一个轻量级的、基于推送的状态管理库。它与 [Angular 生态系统](https://amadeusitgroup.github.io/tansu/#md:tansu-works-well-with-the-angular-ecosystem) 配合良好。
* [@tethys/store](https://github.com/worktile/store) - 一个迷你但功能强大的 Angular 状态管理库。
* [ngx-crud](https://github.com/henryruhs/ngx-crud) - Angular 中的 CRUD 服务可轻松中止、缓存和观察。
* [@ng-state/store](https://github.com/ng-state/store) - RxJS 和 Immer（或 ImmutableJs）为受 NgRx 启发的 Angular 应用程序提供嵌套状态管理。
* [ng-simple-state-management](https://github.com/LionMarc/ng-simple-state-management) - Angular 应用程序的简单状态管理实现。
* [ngx-statewise](https://github.com/Pierre-MarieMarchio/ngx-statewise) - NgRx 或 NGXS 的简化状态管理替代方案。
* [signaltree](https://github.com/JBorgia/signaltree) - 适用于 Angular 应用程序的强大、类型安全、模块化、基于信号的状态管理解决方案。
* [ngx-simple-signal-store](https://github.com/adamcsk1/ngx-simple-signal-store) - 一种使用只读接口创建信号存储的简单方法。
* [angulator](https://github.com/angulator-dev/angulator) - 一个轻量级的 Angular [mediator](https://refactoring.guru/design-patterns/mediator) 库，旨在使用请求/响应和通知/处理程序模式简化应用程序不同部分之间的通信。
* [ngx-query](https://github.com/CoreSyncHub/ngx-query) - 一个轻量级、基于可观察的查询库，可帮助您管理服务器状态、缓存以及后端和 UI 之间的同步。
* [@tanstack/angular-db](https://github.com/TanStack/db/tree/main/packages/angular-db) - TanStack DB 的 Angular 挂钩是一种反应式客户端存储，可让您使用与后端无关的实时数据层构建快速、同步驱动的应用程序。
* [usm](https://github.com/unadlib/usm) - 与 Angular 兼容的模块化状态管理库。
* [ngx-mxstore](https://github.com/MaxxtonGroup/ngx-mxstore) - 通过将逻辑转移到纯粹的、可测试的方法中并通过装饰器将组件连接到存储来简化状态管理。
* [ngx-stashr](https://github.com/nulzo/ngx-stashr) - Angular21 的轻量级信号驱动状态管理库，受到 React 的 [Zusstand](https://github.com/pmndrs/zustand) 的启发。
* [ngx-event-bus-lib](https://github.com/orelnatan/ngx-event-bus-lib) - 在应用程序中的任何位置广播强类型事件并以声明方式对其做出反应 - 无需服务、DI、提供程序、RxJS、信号或紧密耦合。
* [rs-x](https://github.com/robert-sanders-software-ontwikkeling/rs-x) - 一种反应式引擎，将同步和异步数据统一到一个透明模型中，为 Angular 提供细粒度的自动更改检测，无需手动异步处理。
* [stateloom](https://github.com/sujeet-pro/stateloom) - 通用状态管理 SDK，具有信号驱动的反应式核心，以及适用于 React、Angular 等的范例适配器（Store、Atom、Proxy）和框架适配器。
* [ngx-state-crafter](https://github.com/irvrodflo/ngx-state-crafter) - 一个轻量级、信号驱动的 Angular 状态库，具有干净、无样板的 API。
* [coaction](https://github.com/unadlib/coaction) - 一个高效、灵活的状态管理库，用于构建高性能、多线程 Web 应用程序。
* [flurryx](https://github.com/fmflurry/flurryx) - 用于 Angular 的信号优先反应式状态工具包，可将 RxJS 流桥接到结构化的、缓存感知的存储中。
* [ngStato](https://github.com/becher/ngStato) - 使用 async/await 而不是 RxJS 的 Angular 状态管理。
* [ng-eagleeye.js](https://github.com/webKrafters/ng-eagleeye.js) - 与框架无关的原生 JavaScript 不可变状态管理器，具有变更流，可部署在任何地方。
* [ngx-deep-signals](https://github.com/simplesoftsoul/ngx-deep-signals) - Angular 的深度反应式、零仪式嵌套状态 - 将任何对象转换为信号图，无需调用、setter 或样板文件。
* [editate](https://github.com/inokawa/editate) - 一个实验性的、类型安全的、与框架无关的小型（5kB+）内容可编辑状态管理器。
* [sdux-vault](https://github.com/sdux-vault/vault) - 与框架无关的确定性状态管理系统。

## 测试

### 端到端

* [Cypress](https://www.cypress.io/) - Angular 的端到端和组件测试。
* [cypress-harness](https://github.com/jscutlery/devkit/tree/main/packages/cypress-harness) - 该库为组件测试工具提供赛普拉斯支持。
* [cypress-angular-commands](https://github.com/MohamedSci/cypress-angular-commands) - 适用于现代 Angular 企业和 ERP 应用程序的可重用 Cypress 自定义命令的生产就绪集合。
* [lib-e2e-cypress-for-dummys](https://github.com/GonzaloCarmenado/lib-e2e-cypress-for-dummys) - 一个 Angular 库，可在您浏览和使用界面时自动记录测试应用程序所需的 Cypress 命令。
* [testcafe](https://testcafe.io/) - 用户友好的端到端测试解决方案。
* [webdriverio](https://github.com/webdriverio/webdriverio) - Node.js 的下一代浏览器和移动自动化测试框架。
* [Puppeteer Angular Schematic](https://pptr.dev/guides/ng-schematics) - 将 [基于 Puppeteer](https://github.com/puppeteer/puppeteer) e2e 测试添加到您的 Angular 项目中。
* [ngx-playwright](https://github.com/bgotink/ngx-playwright) - 在 Angular 工作区中运行 Playwright e2e 测试的工具。
* [playwright-ng-schematics](https://github.com/jfgreffier/playwright-ng-schematics) - 将 Playwright Test 添加到您的 Angular 项目中。
* [playwright-coverage](https://github.com/bgotink/playwright-coverage) - 使用 v8 覆盖率报告 Playwright 测试的覆盖率，无需任何仪器。
* [Cypress to Playwright](https://www.cy2pw.com/) - 精选的资源集合，可帮助您将测试套件从 Cypress 迁移到 Playwright。
* [Playwright Chrome Recorder](https://chromewebstore.google.com/detail/playwright-chrome-recorde/bfnbgoehgplaehdceponclakmhlgjlpd) - 将 Chromium 录音机选项卡数据导出到 Playwright 测试。这为您提供了一个很好的起点，您可以将其完善为现代剧作家。
* [playwright-mcp](https://github.com/microsoft/playwright-mcp) - 模型上下文协议 (MCP) 服务器，使用 Playwright 提供浏览器自动化功能。
* [twd](https://github.com/BRIKEV/twd) - 浏览器内测试运行器具有即时反馈、测试库支持、Vite 发现和内置 API 模拟 - 与框架无关且易于在 Angular 中使用。

### 组件

* [Angular Testing Library](https://testing-library.com/docs/angular-testing-library/intro/) - 通过引入为测试 Angular 组件量身定制的 API 来扩展 DOM 测试库。
* [@jscutlery/playwright-ct-angular](https://github.com/jscutlery/devkit/tree/main/packages/playwright-ct-angular) - 剧作家 Angular 组件测试。
* [ngx-speculoos](https://github.com/Ninja-Squad/ngx-speculoos) - 更简单、更清晰的 Angular 单元测试。
* [Meticulous AI](https://www.meticulous.ai/) - 覆盖应用程序的数千种边缘情况 - 无需编写或维护单个测试。
* [Jasmine](https://jasmine.github.io/) - 简单的 JavaScript 测试。
* [docker-ng-cli-karma](https://github.com/trion-development/docker-ng-cli-karma) - Angular Docker 镜像能够通过 Chrome 运行 Karma。
* [Jest](https://jestjs.io/) - 一个令人愉快的 JavaScript 测试框架，注重简单性。
* [jest-preset-angular](https://github.com/thymikee/jest-preset-angular) - Angular 项目的 Jest 配置预设。
* [jest-preview](https://github.com/nvh95/jest-preview) - 调试您的 Jest 测试。毫不费力。
* [jest-marbles](https://github.com/just-jeb/jest-marbles) - 使用 Jest 进行弹珠测试的助手库。
* [jest-codemods](https://github.com/skovhus/jest-codemods) - 用于迁移到 Jest 的 Codemods。
* [ts-jest](https://github.com/kulshekhar/ts-jest) - 具有源映射支持的 Jest 转换器，可让您使用 Jest 测试用 TypeScript 编写的项目。
* [Vitest](https://vitest.dev/) - 一个Vite原生的测试框架。
* [Early AI](https://www.startearly.ai/) - 通过 Early 自动生成、验证和确认的单元测试，节省时间、增强代码覆盖率并确保质量。与 Jest 和 Vitest 配合使用。
* [swc-angular](https://github.com/jscutlery/devkit/tree/main/packages/swc-angular) - 这是一组 Angular 预设，使您能够将 SWC（快速 Web 编译器）与 Jest 或 Vitest 结合使用。
* [swc-angular-plugin](https://github.com/jscutlery/devkit/tree/main/packages/swc-angular-plugin) - SWC（Speedy Web Compiler）是一个快如闪电的 JavaScript/TypeScript 编译器，但它不支持 Angular，所以你需要这个插件。
* [wdio-harness](https://github.com/badisi/wdio-harness) - WebdriverIO 支持 Angular 组件测试工具。
* [testronaut](https://github.com/testronaut/testronaut) - 通过消除模拟和猜测，[Testronaut](https://testronaut.github.io/testronaut/) 使开发人员能够直观地检查输出并使用 Playwright 强大的 API 编写精确的测试。

### 帮手

* [Official Angular Material CDK Testing](https://material.angular.dev/cdk/testing/overview) - `@angular/cdk/testing` 提供了帮助测试 Angular 组件的基础设施。
* [ng-mocks](https://github.com/help-me-mom/ng-mocks) - 用于模拟组件、指令、管道、服务并促进 TestBed 设置的 Angular 测试库。
* [ng-mocks-sandbox](https://github.com/help-me-mom/ng-mocks-sandbox) - 一个包含使用 ng-mocks 在 Angular 应用程序中进行单元测试的指南和示例的存储库。
* [spectacular](https://github.com/ngworker/ngworker/tree/main/packages/spectacular) - 为 Angular 应用程序和库提供测试工具。
* [ngx-page-object-model](https://github.com/FrancescoBorzi/ngx-page-object-model) - 该库使用页面对象模型 (POM) 简化了 Angular UI 组件测试，将测试逻辑与 DOM 操作分开以实现更好的抽象。
* [ngtx](https://github.com/Centigrade/ngtx) - A**ng**ular **T**esting E**x**tensions 是一小组函数，可让您在测试 Angular 组件时变得更轻松。
* [ngx-testing-tools](https://github.com/remscodes/ngx-testing-tools) - 提供高级实用程序并减少用于测试 Angular 应用程序的样板文件。
* [stryker-js](https://github.com/stryker-mutator/stryker-js) - JavaScript 和朋友的突变测试。
* [msw](https://github.com/mswjs/msw) - 适用于浏览器和 Node.js 的无缝 REST/GraphQL API 模拟库。
* [msw-lens](https://github.com/hypertheory-labs/msw-lens) - 一种生成 AI 可读的项目状态快照的工具，因此任何模型都可以理解您的模拟 API、活动场景和上下文，而无需手动解释。
* [shallow-render](https://github.com/getsaf/shallow-render) - 通过浅层渲染和简单的模拟，角度测试变得容易。
* [ngx-testbox](https://github.com/kirill-kolomin/ngx-testbox) - 用于 Angular 应用程序的综合测试实用程序库，可简化测试编写并提高测试可靠性。您会发现该库对于单元、集成和 e2e 测试非常有用。
* [ng-automocks](https://github.com/MillerSvt/ng-automocks) - 它通过使用 Jest 自动生成组件、指令、管道、模块和服务的模拟来简化 Angular 测试，从而消除手动存根。
* [jest-angular-test-verifier](https://github.com/Neizan93/jest-angular-test-verifier) - Jest 报告器可验证 Angular 组件、服务、指令和其他文件类型是否具有匹配的测试文件。
* [ngx-api-mocks-interceptor](https://github.com/MaloPolese/ngx-api-mocks-interceptor) - 一个强大的 Angular HTTP 拦截器，用于模拟 API 响应，支持动态数据生成、路径匹配、响应延迟和模拟文件操作。
* [testing-library-queries](https://github.com/thomasmikava/testing-library-queries) - 通过可组合、可链接的 API、TypeScript 支持、CSS 选择器帮助器、简洁的语法、可重用的查询逻辑和与框架无关的兼容性来简化 DOM 查询。
* [ArchUnitTS](https://github.com/LukasNiessen/ArchUnitTS) - 通过简单的设置和无缝测试框架集成，在 JS/TS 项目中执行架构规则、检测循环依赖关系并验证代码标准。
* [qc-auto-package](https://github.com/KareemMostafa77/qc-auto-package) - 轻松、可靠的 Angular 测试 ID — 由测试人员管理，独立于代码。
* [ng-magic-test-bed](https://github.com/peejay-solutions/ng-magic-test-bed) - Angular 测试床包装器允许您从规范文件中删除大量臃肿代码。
* [schmock](https://github.com/khalic-lab/schmock) - 使用插件管道和框架适配器根据 OpenAPI 规范或手工制作的路由创建可调用的模拟 API。

## 网站模板

### 免费模板

* [ng-matero](https://github.com/ng-matero/ng-matero) - Angular Material 管理仪表板模板。
* [coreui-free-angular-admin-template](https://github.com/coreui/coreui-free-angular-admin-template) - CoreUI Angular 是基于 Bootstrap 5 的免费 Angular 管理模板。
* [sakai-ng](https://github.com/primefaces/sakai-ng) - PrimeNG 提供的免费 Angular 管理模板。
* [devextreme-angular-template](https://github.com/DevExpress/devextreme-angular-template) - 基于 DevExtreme Angular 组件的响应式应用程序布局模板。
* [QuickApp](https://github.com/emonney/QuickApp) - ASP.NET Core / Angular 启动项目模板，具有完整的登录、用户和角色管理。加上其他用于快速应用程序开发的有用服务。
* [material-pro-angular-lite](https://github.com/wrappixel/material-pro-angular-lite) - MaterialPro Angular Lite 是来自 WrapPixel 的高品质免费 Angular Material 模板/主题。您可以下载并用于个人和商业项目。
* [spike-angular-free](https://github.com/wrappixel/spike-angular-free) - Spike 是基于 Material Angular 的最强大、最全面的免费 Angular 管理模板。
* [Flexy-admin-angular-lite](https://github.com/wrappixel/Flexy-admin-angular-lite) - Flexy 是基于 Material Angular 的最强大、最全面的免费 Angular 管理模板。
* [angular-quickstart](https://github.com/netlify-templates/angular-quickstart) - 一个简单的 Angular 模板，可让您快速部署到 Netlify！
* [template-angular](https://github.com/phaserjs/template-angular) - Phaser 3 TypeScript 项目模板，使用 Angular 框架和 Vite 进行捆绑。
* [angular-ngrx-frontend](https://github.com/tarlepp/angular-ngrx-frontend) - 用于 Symfony（或类似）后端的 Angular NgRx 支持的前端模板。
* [zen](https://github.com/ZenSoftware/zen) - Nest + Prisma + Apollo + Angular 全栈 GraphQL 入门套件。
* [Colorlib](https://colorlib.com/wp/free-angular-templates/)
* [HTMLrev](https://htmlrev.com/free-angular-templates.html)
* [tailkit-starter-kit-angular](https://github.com/pixelcave/tailkit-starter-kit-angular) - Angular Starter Kit，用于在项目中使用开箱即用的“Tailkit UI”组件。
* [angular-tailwind](https://github.com/lannodev/angular-tailwind) - Angular 和 Tailwind CSS 管理仪表板入门套件。
* [angular-starter-kit](https://github.com/svierk/angular-starter-kit) - 具有 Prettier、Linter、Git-Hooks 和 VS Code 设置的 Angular 项目模板。
* [fractal-boilerplate-lua-angular](https://github.com/FRACTAL-GAME-STUDIOS/fractal_boilerplate_lua_angular) - Basic Angular & Lua - FiveM Boilerplate：用于 Web 和游戏内开发的简化入门套件，具有热构建和实用脚本。
* [angular-sample-app](https://github.com/descope-sample-apps/angular-sample-app) - 一个示例 Angular 应用程序，将 [Descope](https://www.descope.com) 与登录、用户仪表板和动态导航集成。
* [berry-free-angular-admin-template](https://github.com/codedthemes/berry-free-angular-admin-template) - Berry 是一个免费的 Angular + Bootstrap 5 管理仪表板，具有可定制、功能丰富的页面，可实现最佳用户体验。
* [gradient-able-free-admin-template](https://github.com/codedthemes/gradient-able-free-admin-template) - 可渐变的免费 Bootstrap、Angular、React 管理模板。
* [mantis-free-angular-admin-template](https://github.com/codedthemes/mantis-free-angular-admin-template)
* [datta-able-free-angular-admin-template](https://github.com/codedthemes/datta-able-free-angular-admin-template)
* [sanity-template-angular-clean](https://github.com/sanity-io/sanity-template-angular-clean) - 一个干净的 Angular SPA，从 [Sanity](https://www.sanity.io/) 获取内容。
* [angular-templates](https://github.com/hawkgs/angular-templates) - 一组适用于常见 Web 应用程序的 Angular 模板。
* [LightNap](https://github.com/SharpLogic/LightNap) - 具有“ASP.NET”核心身份、JWT 管理和管理员身份功能的全栈 SPA 入门套件。
* [Angspire](https://github.com/tbarracha/Angspire) - Angular + `.NET` monorepo 模板具有内置身份验证、主题和可扩展的基础，可实现更快的开发。
* [keycloakify-starter-angular-vite](https://github.com/keycloakify/keycloakify-starter-angular-vite) - [Keycloakify 11](https://www.keycloakify.dev/) 的 Angular 和 Vite Starter。
* [extreme-angular](https://github.com/joematthews/extreme-angular) - 带有预配置开发工具的入门模板，可强制执行创建干净、可维护且可访问的 Web 应用程序的最佳实践。
* [@wlucha/angular-starter](https://github.com/wlucha/angular-starter) - Angular 19 Starter 包含 Storybook、Transloco、Jest、Cypress、Docker、ESLint、Material 和 Prettier。
* [dataclouder-template-angular](https://github.com/dataclouder-dev/dataclouder-template-angular) - 具有 Firebase 身份验证集成的即用型 Angular/Ionic 模板。
* [signal-admin](https://github.com/codebangla/signal-admin) - Angular 20 管理面板（Material + Tailwind）具有响应式布局、侧边栏、用户管理和 UI 组件。
* [ngXpress](https://github.com/angularcafe/ngXpress) - 全栈 Angular 入门套件（SSR、Zoneless、Express 5、Prisma、better-auth、Tailwind CSS 4）。
* [spartan-stack-starter](https://github.com/thatsamsonkid/spartan-stack-starter) - 使用 Spartan Stack 的固执己见的模板项目启动器。
* [jet](https://github.com/karmasakshi/jet) - 用于快速构建高质量 Web 应用程序的 Angular 入门套件。
* [free-angular-tailwind-dashboard](https://github.com/TailAdmin/free-angular-tailwind-dashboard) - 免费、开源的 Angular + Tailwind CSS 管理仪表板，具有基本的 UI 组件和预构建页面，可实现时尚、现代的界面。
* [hanko-angular-express-starter](https://github.com/teamhanko/hanko-angular-express-starter) - 开始将 Hanko 身份验证与 Angular 和 Express 集成。
* [ng-ultimate-base](https://github.com/Beszt/ng-ultimate-base) - Angular 20 模板，包含 Angular Material UI、Tailwind CSS、i18n、ESLint、Prettier、Husky 和 ​​CI/CD。
* [angular-dev-enhanced](https://github.com/nelsongraa8/angular-dev-enhanced) - 一个即用型 Angular 入门工具，包含 Vite、Vitest、ESLint 和 Prettier，非常适合干净、现代的开发。
* [angular-realworld-example-app](https://github.com/gothinkster/angular-realworld-example-app) - Angular 代码库包含遵循 [RealWorld](https://github.com/gothinkster/realworld) 规范和 API 的真实世界示例（CRUD、身份验证、高级模式等）。
* [angular.ng](https://github.com/desoga10/angular.ng) - 使用 Angular 和 Supabase 构建的开源生产力仪表板。
* [angluar-crm](https://github.com/minhpham-mew/angluar-crm) - Angular CRM 模板，具有联系人管理、交易跟踪和分析功能。
* [ngx-admin-v20](https://github.com/sebbegamer2222/ngx-admin-v20) - 借助此管理仪表板，您将享受带有 SASS 自定义、可重用组件和时尚材质主题的现代 Bootstrap5 UI。
* [nestjs-angular-starter](https://github.com/tivanov/nestjs-angular-starter) - 一个全栈入门模板，具有 NestJS 后端和 Angular 前端，配有身份验证、用户管理和通用基础设施模式。
* [AngularTemplate](https://github.com/EmmanuelLefevre/AngularTemplate) - 该 Angular 模板提供了一个可用于生产的项目设置，包括结构化架构、工具、测试、CI/CD、样式、原理图和清晰的规则文档。
* [free-tailwind-admin-dashboard-template](https://github.com/Tailwind-Admin/free-tailwind-admin-dashboard-template) - 专为现代 Web 开发人员构建的免费开源 Tailwind CSS 管理仪表板模板。
* [ngx-blog](https://github.com/pegasusheavy/ngx-blog) - 一个基于 Angular 的现代博客 CMS，具有主题支持和 SEO 优化。
* [radixweb](https://radixweb.com/starter-kits/enterprise-microservices-boilerplate) - 完整的生产就绪型微服务样板。
* [base-angular-monorepo](https://github.com/myvictorlife/base-angular-monorepo) - 用于开发可扩展的 Angular 应用程序（Nx、NgRx、Tailwind CSS、Jest、ESLint、Prettier）的生产就绪基础项目。
* [nx-ng-starter](https://github.com/rfprod/nx-ng-starter) - 具有工作流程自动化功能的 Monorepo 启动器：Nx、Angular、Angular Elements、Electron、Node、Nest、Firebase。
* [elements-template](https://github.com/giacomo/elements-template) - 一个现代的、固执己见的入门套件，用于构建由 Angular 21、Tailwind CSS v4 和 Vitest 提供支持的自定义 Web 组件。
* [realworld-angular](https://github.com/realworld-angular/realworld-angular) - RealWorld Angular 示例应用程序展示了实际使用的 Angular 库。

### 付费模板

* [管理市场](https://adminmart.com/templates/angular-dashboard/)
* [CozyDevKit](https://cozydevkit.com/) - Angular 21 的交互式工具、架构模式、备忘单和 DevOps 服务。
* [devkitly](https://www.devkitly.io/) - 可投入生产的 Angular 21 入门套件，包含身份验证、计费、审核日志记录、功能标志和 SSR。
* [Nzoni](https://nzoni.app/) - 使用 Angular 在几天内启动您的 SAAS。
* [主题森林](https://themeforest.net/search/angular)
* [Vortex](https://template.giacomobellazzi.com/) - 使用 Angular 和 Java 构建的高性能 Web 应用程序模板，旨在提供无缝的用户体验和强大的后端解决方案。
* [环绕像素](https://www.wrappixel.com/templates/category/angular-templates/)

## 第三方组件

### 动画

* [ngx-confetti-explosion](https://github.com/ChellappanRajan/ngx-confetti-explosion) - Angular 中的五彩纸屑。
* [ngx-lottie](https://github.com/ngx-lottie/ngx-lottie) - 用于渲染 After Effects 动画的完全可定制的 Angular 组件。与 Angular 9+ 兼容。
* [angular-animations-explorer](https://github.com/williamjuan027/angular-animations-explorer) - 展示可以使用 Angular 制作的不同动画的资源。
* [ngx-count-animation](https://github.com/hm21/ngx-count-animation) - 一个可以优雅地动画数字变化的软件包，创建从一个值到另一个值的视觉上引人入胜的过渡，非常适合计数或显示实时数据更新。
* [ng-auto-animate](https://github.com/ajitzero/ng-auto-animate) - FormKit 的 [自动动画](https://auto-animate.formkit.com) 的 Angular 指令（库）。
* [layout-projection](https://github.com/Char2sGu/layout-projection) - 用精彩的布局动画美化网页。
* [ngx-easy-view-transitions](https://github.com/DerStimmler/ngx-easy-view-transitions) - Angular 库可以更轻松地使用视图转换 API。
* [ngx-typed-writer](https://github.com/SkyZeroZx/ngx-typed-writer) - 原生 Angular 2+ 打字动画库（Angular SSR 和 Angular 通用友好）。
* [ngx-number-ticker](https://github.com/omnedia/ngx-number-ticker) - 一个简单的数字滚动效果来动画计数。
* [ngx-word-rotation](https://github.com/omnedia/ngx-word-rotation) - 一个 Angular 库，旨在促进 Angular 应用程序中的单词旋转动画。
* [ngx-word-morph](https://github.com/omnedia/ngx-word-morph) - 一个 Angular 库，旨在促进 Angular 应用程序中的单词变形动画。
* [ngx-cryptic-text](https://github.com/omnedia/ngx-cryptic-text) - 一个 Angular 库，提供神秘的文本动画效果。该组件通过随机切换字母来动画文本，直到出现正确的字符。
* [ngx-word-pullup](https://github.com/omnedia/ngx-word-pullup) - 一个 Angular 库，为单词提供平滑的上拉动画效果。该组件旨在以可定制的延迟顺序提取和显示单词。
* [ngx-typewriter](https://github.com/omnedia/ngx-typewriter) - 一个轻量级且易于使用的库，用于创建打字机效果。它使用 RxJS 来管理打字效果，确保流畅且可定制的动画。
* [ngx-gradient-text](https://github.com/omnedia/ngx-gradient-text) - 一个 Angular 库，可实现平滑的动画文本渐变和可自定义的颜色过渡。
* [ngx-shiny-text](https://github.com/omnedia/ngx-shiny-text) - 一个 Angular 库，提供闪烁的文本动画效果。
* [ngx-ripple](https://github.com/omnedia/ngx-ripple) - 用于交互式、引人入胜的背景或容器的可定制波纹效果组件。
* [ngx-shine-border](https://github.com/omnedia/ngx-shine-border) - 一个 Angular 库，为 Angular 组件提供动态且可定制的动画边框效果。
* [ngx-border-beam](https://github.com/omnedia/ngx-border-beam) - 该组件允许您创建发光的动画边框，可以在颜色、边框半径和动画持续时间方面进行自定义。
* [ngx-dotpattern](https://github.com/omnedia/ngx-dotpattern) - 一个 Angular 库，为 Angular 组件提供可定制的点图案背景效果。
* [ngx-meteors](https://github.com/omnedia/ngx-meteors) - 一个 Angular 库，可为您的组件添加迷人的流星雨动画效果。
* [ngx-background-beams](https://github.com/omnedia/ngx-background-beams) - 一个 Angular 组件，可生成具有可自定义渐变和运动路径的动态动画背景光束。
* [ngx-aurora](https://github.com/omnedia/ngx-aurora) - 一个 Angular 库，用于可定制的动画极光背景，具有渐变效果和两种动画风格。
* [ngx-particles](https://github.com/omnedia/ngx-particles) - 一个用于交互式粒子动画的 Angular 库，可响应鼠标移动，创建可自定义的背景。
* [ngx-spotlight](https://github.com/omnedia/ngx-spotlight) - 用于 SVG 聚光灯效果的 Angular 库，可使用可自定义的颜色和动画突出显示页面部分。
* [ngx-starry-sky](https://github.com/omnedia/ngx-starry-sky) - 一个 Angular 库，可以创建美丽的星空背景，并具有可选的流星效果。
* [ngx-connection-beam](https://github.com/omnedia/ngx-connection-beam) - 动态渲染两个元素之间的动画连接线的 Angular 组件。
* [ngx-countUp](https://github.com/inorganik/ngx-countUp) - 通过计数来动画显示数值。
* [ngx-gsap](https://github.com/marcos-velasquez/ngx-gsap) - 由 GSAP 提供支持的轻量级、可定制的 Angular 动画库，具有声明性且易于使用。
* [ngx-animations](https://github.com/bananalasmari/ngx-animations) - Angular 动画库受 GSAP 启发，提供高性能指令、组件和时间轴服务，并具有完整的 RTL 支持。
* [ngx-spring](https://github.com/angular-threejs/ngx-spring) - 使用弹簧物理而不是持续时间和缓动曲线创建流畅、自然的动画。
* [ngx-unicode-spinners](https://github.com/neogenz/ngx-unicode-spinners) - 18 个基于盲文的 Angular Unicode 旋转动画。零运行时依赖性。
* [ng-motion](https://github.com/ScriptType/ng-motion) - 基于 [motion-dom](https://github.com/motiondivision/motion) 构建的 Angular 动画库。
* [ngx-digit-flow](https://github.com/ayangabryl/ngx-digit-flow) - Angular 的单独数字动画。每个数字都有一个垂直卷轴 (0-9)，当数字发生变化时，卷轴会滚动到新值 - 老虎机/里程表风格。
* [angular-movement](https://github.com/Andersseen/angular-movement) - 一种 Angular 运动生态系统，将可重用的动画指令库与演示和文档站点结合在一个存储库中。

### 日历

* [angular-calendar](https://github.com/mattlewis92/angular-calendar) - 适用于 Angular 15+ 的灵活日历组件，可以在月、周或日视图上显示事件。
* [@pyas/connect-angular](https://www.npmjs.com/package/@pyas/connect-angular) - 围绕 [Pyas Connect](https://github.com/brutforce-tech/pyas-connect) Web 组件的插件包装器，将 PyasConnect 公开为一流的 Angular 组件。
* [cyrus-calendar](https://github.com/mhmfofa/cyrus-calendar) - 一个轻量级的多日历 Angular 日期选择器，支持公历、Shamsi（贾拉里/波斯）和帝国日历。
* [daypilot-lite-angular](https://www.npmjs.com/package/@daypilot/daypilot-lite-angular) - JavaScript/HTML5 事件日历/调度程序组件的 Angular 版本，可以显示日/周/月日历视图。
* [fullcalendar-angular](https://github.com/fullcalendar/fullcalendar-angular) - FullCalendar 的官方 Angular 组件。
* [ngx-calendario](https://github.com/roquemacia/ngx-calendario) - 一个 Angular 库，用于显示具有事件支持的可自定义日历。
* [ngx-calendar-view](https://github.com/charlesschaefer/ngx-calendar-view/tree/main/projects/ngx-calendar-view) - 响应式 Angular 日历组件库，具有日/周/月视图、拖放事件、移动滑动支持和内置暗模式。
* [ngx-calendar-widget](https://github.com/giacomo/ngx-calendar-widget) - 一个轻量级、可定制且功能丰富的日历小部件，旨在简化 Angular 应用程序中的事件管理和日程安排。
* [ngx-datepicker-calendar](https://github.com/mumair4462/ngx-datepicker-calendar) - 一个快速、可访问的 Angular 日期选择器库，由信号和独立组件构建。
* [ngx-resource-scheduler](https://github.com/rmpt/ngx-resource-scheduler) - Angular 的轻量级、灵活的资源调度程序。
* [ngx-strip-calendar](https://github.com/codingchefss/ngx-strip-calendar) - Angular 17+ 的条形日历组件。
* [schedule-x](https://github.com/schedule-x/schedule-x) - 材料设计活动日历。
* [timegrid-angular](https://www.npmjs.com/package/@hexaflexa/timegrid-angular) - [HexaFlexa](https://hexaflexa.com/) Timegrid Web 组件的 Angular 包装器。
* [CalendarJS](https://github.com/componade/calendarjs) - 开源 JavaScript 日历和日程安排组件，可以集成到 Angular 项目中。
* [hss-calendar](https://github.com/HawkerSoftwares/hss-calendar) - 适用于 Angular 19+ 的优质、轻量级且完全可定制的日历库。

### 验证码

* [altcha](https://github.com/altcha-org/altcha) - 符合 GDPR、WCAG 2.2 AA 和 EAA 标准的自托管验证码替代方案，具有 PoW 机制和高级反垃圾邮件过滤器。
* [go-captcha-angular](https://github.com/wenlng/go-captcha-angular) - 简单易用、交互安全的行为验证码，实现文本/图形点击、滑动/拖拽、旋转等验证方式。
* [ng-cloudflare-turnstile](https://github.com/pangz-lab/ng-cloudflare-turnstile) - 适用于 Angular 的直观、轻量级且易于集成的 [Cloudflare Turnstile](https://developers.cloudflare.com/turnstile/) 组件。
* [ng-hcaptcha](https://github.com/leNicDev/ng-hcaptcha) - 为 [hCaptcha](https://hcaptcha.com/) 提供易于使用的组件。
* [ng-recaptcha-2](https://github.com/LakhveerChahal/ng-recaptcha-2) - [ng-recaptcha](https://github.com/DethAriel/ng-recaptcha) 的 Angular 18 分支。或者，您可以借助本文[文章](https://ben-5.azurewebsites.net/2024/9/5/google-recaptcha-v3-with-angular/#google_vignette) 创建自己的服务来实现 Google 的 reCAPTCHA。
* [ngx-captcha-kit](https://github.com/edward124689/ngx-captcha-kit) - 该套件通过单个组件和服务简化了 CAPTCHA 实施，确保与信号和无区域变更检测等 Angular 20+ 功能兼容。
* [ngx-dice-captcha](https://github.com/Easy-Cloud-in/ngx-dice-captcha) - 动态 3D CAPTCHA 库，具有基于骰子的交互和由 Three.js 和 Cannon-es 提供支持的逼真物理特性。
* [ngx-easy-captcha](https://github.com/angx-libs/ngx-easy-captcha) - 轻松实现 Google Recaptcha 和 Cloudflare Turnstile 的验证码。
* [ngx-numeric-captcha](https://github.com/ShreyashThorat-17/ngx-numeric-captcha) - 一个现代、轻量级的 Angular CAPTCHA 库，具有多种验证挑战。
* [ngx-turnstile](https://github.com/verto-health/ngx-turnstile) - 适用于 Angular 的 Cloudflare Turnstile。
* [trustcaptcha-angular](https://www.npmjs.com/package/@trustcomponent/trustcaptcha-angular) - 该库可帮助您将 [Trustcaptcha](https://www.trustcaptcha.com/en) [集成](https://docs.trustcaptcha.com/en/frontend/integration?frontend=angular) 集成到 Angular 前端应用程序中。
* [yandex-smart-captcha](https://github.com/ngx-rock/yandex-smart-captcha) - 一个 Angular 库，用于集成 [Yandex SmartCaptcha](https://yandex.cloud/en/services/smartcaptcha)，支持标准/不可见验证码、反应式表单和现代信号/效果。

### 旋转木马

* [@daelmaak/ngx-gallery](https://github.com/daelmaak/ngx-gallery) - 小型、高性能、响应灵敏、无依赖、易于使用的 Angular 8+ 库。
* [@MurhafSousli/ngx-gallery](https://github.com/MurhafSousli/ngx-gallery/tree/release/13.0.0) - 简化为网络和移动设备创建精美图片库的过程。
* [@vinlos/ngx-gallery](https://github.com/vinlos/ngx-gallery) - 一个简单的 Angular 原生画廊组件。
* [ngu-carousel](https://github.com/uiuniversal/ngu-carousel) - 角度通用轮播。
* [ngx-slider](https://github.com/angular-slider/ngx-slider) - 基于 [angularjs-slider](https://github.com/angular-slider/angularjs-slider) 的 Angular 独立、移动友好的滑块组件。
* [ngx-slick-carousel](https://github.com/leo6104/ngx-slick-carousel) - Angular 17+ 光滑插件的包装器。
* [ngx-owl-carousel-o](https://github.com/vitalii-andriiovskyi/ngx-owl-carousel-o) - Angular >=6 的“owl-carousel”。
* [angular2-image-gallery](https://github.com/BenjaminBrandmeier/angular2-image-gallery) - 使用 Angular 17+、Node.js 和 GraphicsMagick 构建的图片库。
* [egjs-flicking](https://naver.github.io/egjs-flicking/docs/quick-start) - 轻弹角度快速启动。
* [ngx-drag-scroll](https://github.com/bfwg/ngx-drag-scroll) - 一个轻量级响应式 Angular 轮播库。
* [ngx-darkbox-gallery-library](https://github.com/failed-successfully/ngx-darkbox-gallery-library) - 一个高度可配置的灯箱主题画廊库，适用于使用 Ivy 引擎 (Angular 15+) 的 Angular 应用程序。
* [ngx-stories](https://github.com/Gauravdarkslayer/ngx-stories) - 一个 Angular 组件，用于渲染 Instagram 的故事。
* [carousel-library](https://github.com/GreenFlag31/carousel-library) - 一个多功能的 Angular 库，提供功能丰富、简单且高性能的轮播组件。
* [ngx-simple-gallery](https://github.com/zolcsi/ngx-simple-gallery) - Angular 18 的轻量级图库库，将所有图像显示为缩略图，单击或点击时将其扩展为完整尺寸。
* [embla-carousel-angular](https://github.com/donaldxdonald/embla-carousel-angular) - [Embla Carousel](https://github.com/davidjerleke/embla-carousel) 的角度包装器。
* [ngx-cdk-lightbox](https://github.com/miskith/ngx-cdk-lightbox/tree/master/projects/ngx-cdk-lightbox) - 基于 CDK 的定制解决方案，用于在 Angular 中渲染具有灯箱功能的图像库。
* [rm-image-slider](https://github.com/malikrajat/rm-image-slider) - 独立的 Angular 图像滑块，具有灯箱、延迟加载和视频支持 (YouTube/MP4)。
* [ngx-carousel-modern](https://github.com/Aizaz-ul-haq/ngx-carousel-modern) - 适用于 Angular 16+ 的现代可定制轮播组件，支持独立应用程序和基于 NgModule 的应用程序。
* [fslightbox-angular](https://github.com/banthagroup/fslightbox-angular) - [全屏灯箱](https://fslightbox.com/) 的 Angular 版本。
* [whirli-ng](https://github.com/babbage42/whirli-ng) - 具有拖动、循环、虚拟幻灯片、投影内容、拇指、SSR 友好的响应式布局、外部控件和丰富的事件 API 的角度轮播。

### 图表

* [@cubejs-client/ngx](https://www.npmjs.com/package/@cubejs-client/ngx) - 与 [@cubejs-client/core](https://www.npmjs.com/package/@cubejs-client/core) 一起，您可以在 Angular 中[集成](https://cube.dev/docs/product/apis-integrations/javascript-sdk/angular) Cube.js。
* [ngx-charts](https://github.com/swimlane/ngx-charts) - 适用于 Angular2 及更高版本的声明式图表框架！
* [ag-charts](https://github.com/ag-grid/ag-charts/tree/latest/packages/ag-charts-angular) - 功能齐全且高度可定制的 JavaScript 图表库。
* [amcharts5](https://github.com/amcharts/amcharts5) - JavaScript 和 TypeScript 应用程序的图表库。查看 [Angular 集成指南](https://www.amcharts.com/docs/v5/getting-started/integrations/angular/)。
* [angular-chrts](https://github.com/dennisadriaans/angular-chrts) - 适用于现代 Angular 应用程序的高性能、开发人员友好的数据可视化库。
* [angular-google-charts](https://github.com/FERNman/angular-google-charts) - 用 Angular 编写的 Google Charts 库的包装器。
* [carbon-charts](https://github.com/carbon-design-system/carbon-charts/tree/master/packages/angular) - Carbon Charts Angular 是一个围绕普通 JavaScript @carbon/charts 组件库的薄 Angular 包装器。
* [Foblex](https://flow.foblex.com/) - Angular 驱动的流程图库。
* [highcharts-angular](https://github.com/highcharts/highcharts-angular) - Angular 的官方最小 [Highcharts](https://www.highcharts.com/) 集成。
* [ng-apexcharts](https://github.com/apexcharts/ng-apexcharts) - ApexCharts 的 Angular 包装器用于构建交互式可视化。
* [ng-chartist](https://github.com/willsoto/ng-chartist) - [Chartist.js](https://github.com/chartist-js/chartist) 的 Angular 组件。
* [ng-diagram](https://github.com/synergycodes/ng-diagram) - 用于构建交互式、可定制图表、基于节点的编辑器和可视化工作流程的 Angular 库。
* [ng-draw-flow](https://github.com/taiga-family/ng-draw-flow) - 用于创建基于将数据显示为节点的界面的库。
* [ngx-echarts](https://github.com/xieziyu/ngx-echarts) - [Apache ECharts](https://github.com/apache/incubator-echarts) 的 Angular 指令。
* [ngx-flexmonster](https://github.com/flexmonster/ngx-flexmonster) - 一个强大且完全可定制的 JavaScript 组件，用于 Web 报告和数据可视化。
* [ngx-gantt](https://github.com/worktile/ngx-gantt) - Angular 的现代且强大的甘特图组件。
* [ngx-graph](https://github.com/swimlane/ngx-graph) - Angular 的图形可视化库。
* [ngx-interactive-org-chart](https://github.com/zeyadelshaf3y/ngx-interactive-org-chart) - 现代 Angular 组织结构图组件，具有交互式平移和缩放功能。
* [ngx-recharts](https://github.com/wook95/ngx-recharts) - 使用与 [Recharts](https://recharts.github.io/) 相同的 API，使用 Angular 组件构建可组合图表。
* [ngx-simple-charts](https://github.com/Angular2Guy/ngx-simple-charts) - Angular 17+ 库，用于基于 D3 的折线图、条形图、圆环图和日期/时间线图表，具有多个入口点。提供了用于令牌处理的可配置服务。
* [org-chart](https://github.com/bumbeishvili/org-chart) - 高度可定制的组织结构图。可用于 Angular、React 和 Vue 的集成。
* [pioneer-charts](https://github.com/PioneerCode/pioneer-charts) - 用于使用 D3.js 创建响应式、可自定义图表的 Angular 库，支持条形图、折线图、饼图等。
* [sequential-workflow-designer](https://github.com/nocode-js/sequential-workflow-designer) - 可定制的无代码组件，用于构建基于流程的编程应用程序或工作流程自动化。零外部依赖。
* [systelab-charts](https://github.com/systelab/systelab-charts) - Systelab 角度图表服务。
* [unovis](https://github.com/f5/unovis) - 适用于 React、Angular、Svelte、Vue 和 vanilla TypeScript 或 JavaScript 的模块化数据可视化框架。

### 饼干

* [ngx-cookie-service](https://github.com/stevermeister/ngx-cookie-service) - cookie 的角度服务。最初基于 [ng2-cookies](https://github.com/BCJTI/ng2-cookies) 库。
* [cookieconsent](https://github.com/orestbida/cookieconsent) - 用 vanilla js 编写的简单跨浏览器 cookie-consent 插件，可以添加到 [Angular](https://cookieconsent.orestbida.com/essential/getting-started.html#angular)。
* [ngx-cookie-ssr](https://github.com/Ask-786/ngx-cookie-ssr) - 受 ngx-cookie-service 启发，适用于 Angular 19 应用程序的简单 cookie 服务。
* [ngx-gdpr-cookie-consent](https://github.com/KoblerS/ngx-gdpr-cookie-consent) - 一个漂亮的Cookie同意库，易于使用。
* [smallest-cookie-banner](https://github.com/DreadfulCode/smallest-cookie-banner) - 最小的与框架无关的 cookie 同意横幅。
* [ngrithms-cookie-consent](https://github.com/aboudbadra/ngrithms-cookie-consent) - 现代 Angular cookie 同意 — 独立组件、基于信号的状态、“provideCookieConsent()”功能设置、SSR 安全和零运行时依赖。

### CSV

* [impler](https://github.com/implerhq/impler.io) - 使用 [Angular 包](https://www.npmjs.com/package/@impler/angular) 将 CSV Excel 导入器嵌入到您的应用程序中。
* [ng2csv](https://github.com/rars/ng2csv) - 用于将数据保存到 CSV 文件的 Angular 服务。
* [ngx-export-as](https://github.com/wnabil/ngx-export-as) - Angular 2+ / Ionic 2+ HTML/表格元素可将其导出为 JSON、XML、PNG、CSV、TXT、MS-Word、Ms-Excel 和 PDF。
* [rm-ng-export-to-csv](https://github.com/malikrajat/rm-ng-export-to-csv) - 一个轻量级且可定制的 Angular 库，用于将 JSON 数据导出到 CSV 文件，并支持自动下载。非常适合图表、表格、报告和仪表板。

### 数据网格

* [ag-grid](https://www.ag-grid.com/) - 用于构建企业应用程序的最佳 JavaScript 数据表。支持 React、Angular、Vue 和纯 JavaScript。
* [ignite-ui-angular's grid](https://www.infragistics.com/products/ignite-ui-angular/angular/components/grid/grid) - “Ignite UI”中的数据网格、树形网格、分层网格提供了 Excel 风格的过滤、实时数据、排序、可拖动行和其他工具栏。
* [sheetjs](https://docs.sheetjs.com/docs/demos/frontend/angular) - 用于从电子表格读取和写入数据的 JavaScript 库。
* [active-table](https://github.com/OvidijusParsiunas/active-table) - 与框架无关的表组件，可提供可编辑的数据体验。
* [jsgrids](https://github.com/statico/jsgrids) - 用于比较 JavaScript 数据网格和电子表格库的比较工具。  从此存储库中找到更多库。
* [handsontable](https://handsontable.com/docs/javascript-data-grid/angular-installation/) - 一种流行的 JavaScript 数据网格组件，可为您的应用程序带来众所周知的电子表格外观和感觉。
* [slickgrid-universal](https://github.com/ghiscoding/slickgrid-universal) - 一个 monorepo，其中包括与框架无关的 [SlickGrid](https://github.com/6pac/SlickGrid) 使用相关的所有编辑器、过滤器、扩展和服务。
* [revogrid](https://github.com/revolist/revogrid) - 具有高级定制功能的强大虚拟数据网格智能表。 Excel 的最佳功能加上令人难以置信的性能。
* [ZingGrid](https://github.com/ZingGrid/zinggrid) - JavaScript Web 组件库，允许开发人员在其 Web 应用程序中包含交互式数据表。该库可用于 [Angular](https://www.zinggrid.com/docs/integrations/js-frameworks-&-libs/angular) 和更多框架。
* [ngx-panemu-table](https://github.com/panemu/ngx-panemu-table) - 一个 Angular 表格组件。它被设计为易于使用。大多数工作将在 TypeScript 文件中进行，而 HTML 文件只需要有一个非常简单的“panemu-table”标签。
* [@guiexpert/angular-table](https://github.com/guiexperttable/angular-19-table) - 与框架无关的表库，旨在与主要框架无缝集成，包括 [Angular](https://gui.expert/getstarted/angular/)。
* [ngx-tabulator-tables](https://github.com/knackstedt/ngx-tabulator-tables) - [Tabulator](https://tabulator.info/) 表库的 Angular 包装器。
* [activereportsjs/angular-reporting-tool](https://developer.mescius.com/activereportsjs/angular-reporting-tool) - 用于数据可视化和报告的角度组件。使用 [ActiveReportsJS](https://developer.mescius.com/activereportsjs) 嵌入报告。
* [mat-datatable](https://github.com/BePo65/mat-datatable) - 使用 Angular Material 进行虚拟滚动的简单数据表。
* [@Trixwell/data-grid](https://github.com/Trixwell/data-grid) - 具有过滤、排序、分页、CSV 导出、子网格和材质集成功能的 Angular 数据表组件。
* [ngx-multi-sort-table](https://github.com/Maxl94/ngx-multi-sort-table) - 该库具有基于 Angular Material Design 的多个可排序表，重点关注服务器端加载和排序的数据。
* [angular2-smart-table](https://github.com/dj-fiorex/angular2-smart-table) - Angular 智能数据表组件。
* [ngx-editable-material-table](https://github.com/valentinstn/ngx-editable-material-table) - 一个可编辑的表格，构建在 Angular Material 之上，原生适用于 Angular。
* [ngx-flamegraph](https://github.com/mgechev/ngx-flamegraph) - 用 Angular 编写的堆栈跟踪可视化火焰图。
* [ng-virtual-grid](https://github.com/DjonnyX/ng-virtual-grid) - 超大型网格的最佳性能。
* [ngx-simple-datatables](https://github.com/rinturaj/ngx-simple-datatables) - 一个轻量级、高性能的 Angular 数据表组件，具有虚拟滚动、列冻结和可自定义模板等功能。
* [ngx-list-manager](https://github.com/RzoDev/ngx-list-manager) - 一个用于高效管理列表的 Angular 服务工具。
* [cerious-grid](https://github.com/ryoucerious/cerious-widgets) - 一个非常强大的 Angular 网格，适合需要控制、灵活性和性能的开发人员。
* [ngxsmk-datatable](https://github.com/toozuuu/ngxsmk-datatable) - 现代 Angular 17+ 数据表专注于性能、定制和开发人员体验。
* [ngx-column-filter](https://github.com/kakarotx10/ngx-column-filter) - 一个强大的、可重用的 Angular 列过滤器组件，支持多种字段类型、高级过滤规则和可自定义的匹配模式。
* [@witqq/spreadsheet](https://github.com/witqq/spreadsheet) - 基于 Canvas 的电子表格/数据网格引擎，具有零依赖性、60fps 100K+ 行、完整编辑和实时协作。检查他们的[网站](https://spreadsheet.witqq.dev/)。
* [Jspreadsheet CE](https://github.com/jspreadsheet/ce) - 开源 JavaScript 电子表格和数据网格组件，当通过 Angular 元素包装或使用时，可以在 Angular 应用程序中使用。
* [TabularJS](https://github.com/jspreadsheet/tabularjs) - 轻量级 JavaScript 表格和数据网格库，用于 Angular 中的高级表格功能。
* [uni-table](https://github.com/Unify-India/uni-table) - 基于信号构建的 Angular 数据网格可实现零延迟性能，将先进的服务器端功能与简化的配置 API 相结合。
* [ogrid](https://github.com/alaarab/ogrid) - 具有企业特性、零企业成本的轻量级、多框架数据网格。
* [angular-datatables.net](https://github.com/Vinccool96/angular-datatables.net) - Angular 加上 [DataTables](https://datatables.net/)。
* [uiGrid](https://github.com/orneryd/uiGrid) - 开源、多平台数据网格从原始的 [ui-grid](https://github.com/angular-ui/ui-grid) 重建，具有相同的 API 和现代 Angular 信号，支持 Angular、Web Components、React 和 Rust。
* [ngx-datawindow](https://github.com/sugitter/ngx-datawindow) - 表组件通过零配置 CRUD、计算列、多缓冲区状态、离线同步和粒度更改跟踪对经典 DataWindow 进行了现代化改造。
* [simple-table](https://github.com/petera2c/simple-table) - 与框架无关的数据网格和表组件，用于构建现代、可扩展的应用程序。
* [toolbox](https://github.com/OysteinAmundsen/toolbox) - 适用于数据密集型应用程序的高性能、与框架无关的 Web 组件。
* [gp-grid](https://github.com/GioPat/gp-grid) - 采用模块化架构构建的数据网格库，将核心逻辑与框架集成完全分离，以有效处理具有数百万行的海量数据集。
* [ngx-powerful-tree](https://github.com/raknjarasoa/ngx-powerful-tree) - 具有 HTML5 拖放、快速搜索、锁定子树和文件选择器模式的虚拟树，基于“@angular/cdk/scrolling”构建，可在 100k+ 行上实现流畅的性能。

### 枣子

* [ngx-date-fns](https://github.com/joanllenas/ngx-date-fns) - [Date-fns](https://date-fns.org/) Angular 管道。
* [ngx-mat-timepicker](https://github.com/tonysamperi/ngx-mat-timepicker) - 真正的材料时间选择器。
* [mat-datetimepicker](https://github.com/kuhnroyal/mat-datetimepicker) - `@angular/material` 的材质日期时间选择器。
* [ngx-multiple-dates](https://github.com/lekhmanrus/ngx-multiple-dates) - 基于 Angular Material 的多个日期选择器。
* [ng-datetime](https://github.com/ressurectit/ng-datetime) - 包含用于处理日期时间的组件的 Angular 库。
* [time2blocks-ngx](https://github.com/antonioconselheiro/time2blocks-ngx) - Angular lib 用于识别过去与区块链块关联的时间（并对其进行格式化）。
* [@dhutaryan/ngx-mat-timepicker](https://github.com/dhutaryan/ngx-mat-timepicker) - 基于材料设计的材料时间选择器。
* [ngx-timeline](https://github.com/omnedia/ngx-timeline) - 一个简单的组件库，用于添加动画时间轴视图。
* [frxjs-Ngx-Timeline](https://github.com/emanuelefricano93/frxjs-Ngx-Timeline) - 该库允许您将时间线集成到 Angular 应用程序中。
* [ngx-daterangepicker-pro](https://github.com/Abhinavgaur01/ngx-daterangepicker-pro-demo) - 一个强大的、可定制的 Angular 日期范围选择器，使用 Angular 17+ 和 [Day.js](https://github.com/iamkun/dayjs) 构建。
* [ngx-custom-daterangepicker](https://github.com/nedpuganti/ngx-custom-daterangepicker) - 具有可配置选项的 Angular Material 日期范围选择器，支持高级功能和直接集成。
* [angular-material-jalali-datepicker-adapter](https://github.com/aliqb/angular-material-jalali-datepicker-adapter) - 一个综合性的 Angular 库，为 Angular Material 日期选择器组件提供 Jalali（波斯语/阳历回历/Shamsi）日期适配器。
* [date-interceptors](https://github.com/AdaskoTheBeAsT/date-interceptors) - 该库提供了一个强大的解决方案，用于将日期和持续时间字符串从 JSON 有效负载分别转换为本机日期对象和持续时间对象。
* [ngx-vertical-timeline](https://github.com/callyafiune/ngx-vertical-timeline) - 用于创建响应式垂直时间线的 Angular 组件。
* [ngx-timeago](https://github.com/ihym/ngx-timeago) - Angular 中的动态时间戳渲染。
* [ngx-chronica](https://github.com/klajdm/ngx-chronica) - 一个全面的 Angular 库，提供六个专门的日期和时间选择器组件，填补了 Angular 生态系统中的关键空白。
* [ngx-mat-multi-date-picker](https://github.com/ali79heidari/ngx-mat-multi-date-picker) - 一个全面、独立的 Angular 库，提供高质量的公历、贾拉里（波斯）和回历（伊斯兰）日期选择器。
* [date-time-picker](https://github.com/danielmoncada/date-time-picker) - 角度日期时间选择器。
* [date-time-picker-moment-adapter](https://github.com/danielmoncada/date-time-picker-moment-adapter) - Moment.js `@danielmoncada/date-time-picker` 适配器。
* [hijri-date-time-picker](https://github.com/hanygamal72/hijri-date-time-picker) - 使用 Umm Al-Qura 日历的 Angular 独立双公历/回历日期时间选择器。
* [ng-laydate](https://github.com/lanxuexing/ng-laydate) - 适用于 Angular 18+ 的简单而强大的日期和时间选择器。
* [lifecycle-timeline](https://github.com/ericreboisson/lifecycle-timeline) - 一个交互式 Vanilla JS 组件，用于可视化产品生命周期阶段，并附有 Angular 集成指南。
* [weekly-availability-picker](https://github.com/squareetlabs/weekly-availability-picker) - 独立的 Angular 每周可用性选择器，支持拖动和调整大小。
* [ng-date-hour-range-selector](https://github.com/deciosfernandes/ng-date-hour-range-selector) - 基于 Angular CDK Overlay 构建的灵活的 Angular 日期/日期时间范围选择器。

### 指令

* [ng-click-outside](https://github.com/Kr0san89/ng-click-outside) - 用于处理元素外部的单击事件的 Angular 指令。
* [ng-for-track-by-property](https://github.com/nigrosimone/ng-for-track-by-property) - 具有严格类型检查的 Angular 全局 `trackBy` 属性指令。
* [ng-let](https://github.com/nigrosimone/ng-let) - 用于将数据作为局部变量共享到 HTML 组件模板中的结构指令。
* [ngx-app-version](https://github.com/Celtian/ngx-app-version) - 用于将版本写入 DOM 的 Angular 指令。
* [ngx-clamp](https://github.com/Chitova263/ngx-clamp) - 用于多行或基于高度的文本夹紧的角度指令，具有旧版浏览器支持。
* [ngx-copypaste](https://github.com/JsDaddy/ngx-copypaste) - 一个纯粹且很棒的 Angular 复制粘贴指令。
* [ngx-copy-to-clipboard](https://github.com/andreasnicolaou/ngx-copy-to-clipboard) - 一个 Angular 指令，只需单击一下即可轻松将文本复制到剪贴板。它支持可自定义的成功/错误消息并触发复制操作事件。
* [ngx-cut](https://github.com/Celtian/ngx-cut) - 用于使用响应选项剪切文本的角度指令。
* [ngx-fixed-footer](https://github.com/Celtian/ngx-fixed-footer) - 添加固定页脚而不重叠的角度指令。
* [ngx-if-platform](https://github.com/Celtian/ngx-if-platform) - 基于平台的条件显示指令。
* [ngx-memoize](https://github.com/ali79heidari/ngx-memoize) - 一个轻量级、零依赖的装饰器，可记忆 Angular 类方法，以消除重复的模板调用开销并提高性能。
* [ngx-nullable](https://github.com/Celtian/ngx-nullable) - 该库提供了一种在 Angular 模板中使属性可为空的方法。
* [ngx-overflow-reveal](https://github.com/hosembafer/ngx-overflow-reveal) - 一个 Angular 指令，可以在悬停时优雅地显示截断的文本。
* [ngx-repeat](https://github.com/Celtian/ngx-repeat) - 用于按计数重复 HTML 元素的 Angular 指令。
* [ngx-speech-button](https://github.com/JayChase/ngx-speech-button) - 一个 Angular 指令，为 Web 语音 API 提供易于使用的包装器，只需最少的设置即可实现语音输入功能。
* [ngxsmk-button-spinner](https://github.com/toozuuu/ngxsmk-button-spinner) - Angular 17+ 指令用于显示加载微调器内联或居中于任何按钮。
* [ngxture](https://github.com/gianpierreVelasquez/ngxture) - 一个轻量级、模块化的 Angular 库，提供即用型动画和手势指令。
* [@maxime1jacquet/npm-directives](https://github.com/maxime1jacquet/npm-directives) - Angular 指令包括 [ngx-cursor](https://www.npmjs.com/package/ngx-cursor) 和 [ngx-simple-countdown](https://www.npmjs.com/package/ngx-simple-countdown)。
* [ngx-mat-menu-hover](https://github.com/Gamekohl/ngx-mat-menu-hover) - 此 Angular 指令提供了处理悬停菜单行为的功能，允许菜单在悬停时打开，在鼠标离开时关闭。

### DOM

* [ngx-resize-observer](https://github.com/fidian/ngx-resize-observer) - Angular 8+ 模块用于检测元素何时调整大小。
* [ngx-mutation-observer](https://github.com/fidian/ngx-mutation-observer) - 当 DOM 中的元素发生变化时触发 Angular 8+ 事件。
* [ngx-visibility](https://github.com/fidian/ngx-visibility) - 检测元素何时可见的 Angular 模块。使用 IntersectionObserver。
* [ngx-fade](https://github.com/omnedia/ngx-fade) - 使用 Intersection Observer API 实现平滑淡入淡出和滑动视口过渡的 Angular 组件。
* [ngx-dynamic-hooks](https://github.com/MTobisch/ngx-dynamic-hooks) - 自动将实时 Angular 组件插入动态字符串（基于其选择器或您选择的任何模式）并在 DOM 中渲染结果。
* [ngx-highlightjs](https://github.com/MurhafSousli/ngx-highlightjs) - 即时代码高亮，自动检测语言，超级好用！
* [ngx-sharebuttons](https://github.com/MurhafSousli/ngx-sharebuttons) - 有角度的分享按钮。
* [ng-helpers](https://github.com/Jaspero/ng-helpers) - Angular 有用的组件、指令和管道的集合。
* [ngx-ellipsis](https://github.com/lentschi/ngx-ellipsis) - Angular 9+ 带有省略号的多行文本。
* [ng-gd](https://github.com/luisalejandrofigueredo/ng-gd) - 管理画布元素的简单方法，支持鼠标或平板电脑事件。
* [ngx-annotate-text](https://github.com/philenius/ngx-annotate-text) - 用于可视化和注释文本的 Angular 库，非常适合命名实体识别和词性标记等任务。
* [ng-dynamic-component](https://github.com/gund/ng-dynamic-component) - 动态组件，为 Angular 的输入和输出提供全生命周期支持。
* [ngx-optimus](https://github.com/Bilal-Abubakari/ngx-optimus) - Angular 库提供自定义管道来简化数据格式化并保持组件逻辑清晰。
* [ng-lock](https://github.com/nigrosimone/ng-lock) - Angular 装饰器用于在任务运行时锁定功能和用户界面。
* [angular-paginator](https://github.com/sibiraj-s/angular-paginator) - Angular 应用程序的分页组件。
* [ngx-signal-combinators](https://github.com/alessiopelliccione/ngx-signal-combinators) - 用于 Angular 信号的可组合布尔助手，可实现更清晰的反应式模板逻辑。
* [viewport-truth](https://github.com/AntonVoronezh/viewport-truth) - 一个小型的 VisualViewport-first 存储，用于精确的 CSS 像素视口大小，可检测虚拟键盘，减少调整大小/滚动抖动，并跨框架与 SSR 配合使用。
* [angular-inport](https://github.com/ajaysinghj8/angular-inport) - 角度视口内检测器。

### 拖放

* [官方 Angular 文档](https://angular.dev/guide/drag-drop)
* [ngx-drag-drop](https://github.com/reppners/ngx-drag-drop) - 使用原生 HTML 拖放 API 的 Angular 指令。
* [@hackingharold/ngx-dropzone](https://github.com/hackingharold/ngx-dropzone) - Angular Material 缺少文件输入组件。
* [ng-dnd](https://github.com/ng-dnd/ng-dnd) - Angular 的拖放操作。
* [angular-drag-drop-layout](https://github.com/skutam/angular-drag-drop-layout) - 一个轻量级、无依赖性的 Angular 库，用于创建具有拖放功能的高度可定制、响应式网格布局。
* [ngx-swapy](https://github.com/omnedia/ngx-swapy) - 一个简单的组件库，通过 [Swapy](https://github.com/TahaSh/swapy) 的帮助来获取拖放 DOM。
* [ngx-draggable-dom](https://github.com/bmartinson/ngx-draggable-dom) - 使任何元素成为可拖动元素的角度属性指令。
* [ngx-drag-resize](https://github.com/dmytro-parfenov/ngx-drag-resize) - 这个 Angular 库提供了向 HTML 元素添加拖动和调整大小功能的指令。
* [ng-keyboard-sort](https://github.com/johnhwhite/ng-keyboard-sort) - 为也使用 CDK 拖放排序的元素添加键盘命令的库。
* [angular-mixed-cdk-drag-drop](https://github.com/rosejoe47/angular-mixed-cdk-drag-drop) - 使用 Angular CDK 支持混合方向拖放的 Angular 指令。
* [cdk-drag-snap-to-point](https://github.com/shhdharmen/cdk-drag-snap-to-point) - 展示 cdkDrag 功能的演示，仅在某些点上实现拖放。
* [ngx-puzzle](https://github.com/zhongmiao-org/ngx-puzzle) - 适用于 Angular 应用程序的拖放式仪表板构建器。
* [ngx-drag-drop-kit](https://github.com/mr-samani/ngx-drag-drop-kit) - 高性能 Angular 拖放工具包，具有网格布局、排序、调整大小、嵌套等功能。
* [ngx-dashboard](https://github.com/TobyBackstrom/ngx-dashboard) - 现代 Angular 工作区，用于构建具有可调整大小的单元格和可自定义小部件的拖放网格仪表板。
* [ngx-dropzone-next](https://github.com/arturovt/ngx-dropzone-next) - 维护的“@peterfreeman/ngx-dropzone”分支，提供错误修复并与较新的 Angular 版本兼容。

### 编辑

* [Angular-JSON-Tree-Editor-Component](https://github.com/stefonalfaro/Angular-JSON-Tree-Editor-Component) - 真正有效的 Angular JSON 树编辑器组件。
* [@acrodata/code-editor](https://github.com/acrodata/code-editor) - Angular 的 CodeMirror 6 包装器。
* [angular2-froala-wysiwyg](https://github.com/froala/angular-froala-wysiwyg) - Froala WYSIWYG HTML 编辑器的 Angular 包装器。
* [ckeditor](https://ckeditor.com/docs/ckeditor5/latest/installation/getting-started/frameworks/angular.html) - Angular 的插件。
* [domternal](https://github.com/domternal/domternal) - 轻量级、可扩展的富文本编辑器工具包，具有原生 Angular 组件（Signals、OnPush、独立）、内置工具栏和主题以及完整表格支持。
* [ngx-aztreya-editor](https://github.com/aztreya/ngx-aztreya-editor) - 一个轻量级、可定制的 Angular 富文本编辑器组件，具有内置工具栏、标题、文本格式和对齐选项。
* [ngx-simple-text-editor](https://github.com/Raiper34/ngx-simple-text-editor) - Ngx 简单文本编辑器或 ST 编辑器是 Angular 9+ 的简单本机文本编辑器组件。
* [ngx-quill](https://github.com/KillerCodeMonkey/ngx-quill) - Quill 富文本编辑器的 Angular 组件。
* [@sibiraj-s/ngx-editor](https://github.com/sibiraj-s/ngx-editor) - 使用 ProseMirror 的 Angular 富文本编辑器。
* [@bobbyquantum/ngx-editor](https://github.com/bobbyquantum/ngx-editor) - `sibiraj-s/ngx-editor` 的 Angular 21+ 分支。
* [ngx-wig](https://github.com/stevermeister/ngx-wig) - Angular 所见即所得 HTML 富文本编辑器。
* [ngx-property-editor](https://github.com/heinerwalter/ngx-property-editor) - Angular 库包含简单的输入组件和属性编辑器组件，该组件会自动构建用于编辑任何对象的所有属性的表单。
* [ngx-tiptap](https://github.com/sibiraj-s/ngx-tiptap) - [tiptap v2](https://tiptap.dev/) 的角度绑定。
* [tinymce-angular](https://github.com/tinymce/tinymce-angular) - 官方 [TinyMCE](https://www.tiny.cloud/) Angular 组件。
* [slate-angular](https://github.com/worktile/slate-angular) - [Slate](https://github.com/ianstormtaylor/slate) 的角度视图层。
* [ngx-jodit](https://github.com/julianpoemp/ngx-jodit/) - [Jodit](https://github.com/xdan/jodit) WYSIWYG 编辑器的 Angular 包装器。
* [ngx-tinymce](https://github.com/cipchk/ngx-tinymce) - 使用 Angular 构建的“TinyMCE”组件。
* [MagnetarQuill](https://github.com/scherenhaenden/MagnetarQuill) - 可扩展的 Angular WYSIWYG 编辑器，用于具有插件架构的富文本、媒体和表格。
* [ngx-editorjs2](https://github.com/Ba5ik7/ngx-editorjs2) - 可扩展的块编辑器受到 [Editor.js](https://editorjs.io/) 的启发，具有可定制的块和 Angular 反应功能。 [ngx-editor-js2-blocks](https://github.com/Ba5ik7/ngx-editor-js2-blocks) 添加了对自定义内容类型的支持。
* [ngx-traak](https://github.com/mouhamadalmounayar/ngx-traak) - 构建在 ProseMirror 之上的所见即所得 Angular 编辑器库，专为独立组件而构建，并可通过插件进行高度自定义。
* [ngx-summernote](https://github.com/lula/ngx-summernote) - [Summernote](https://github.com/summernote/summernote) Angular 编辑器。
* [angular-rich-text-editor](https://github.com/manishpatidar028/angular-rich-text-editor) - [RichTextEditor](https://richtexteditor.com/) 的 Angular 包装器，具有许可证密钥支持和“ControlValueAccessor”。
* [armor-editor](https://github.com/technicults/armor-editor) - 具有高级功能的安全、轻量级富文本编辑器，旨在无缝集成到 Angular 应用程序中。
* [ngx-workflow](https://github.com/abdulkyume/ngx-workflow) - 一个功能强大、高度可定制的 Angular 库，用于构建基于节点的交互式编辑器、流程图和图表。
* [contentful-rich-text-angular-renderer](https://github.com/flowup/contentful-rich-text-angular-renderer) - 用于内容丰富的富文本的 Angular 渲染器，使用 Angular 模板提供可自定义的节点和标记渲染。
* [Monaco Pattern Editor](https://github.com/KhlifiIsmail/Editor) - 一个优质的 Angular 库，为 Monaco Editor 提供了精美的主题和编码面试准备功能。
* [angular-editor](https://github.com/kolkov/angular-editor) - Angular 的简单原生 WYSIWYG 编辑器组件。
* [ngx-json-editor](https://github.com/RonnyValdivieso/ngx-json-editor) - 一个最小的、可主题化的 Angular JSON 编辑器。
* [ngx-ace-signal](https://github.com/WebArtWork/ngx-ace-signal) - Ace 编辑器的现代基于 Angular 信号的包装器。
* [ngx-rwriter](https://github.com/ReiAg/ngx-rwriter) - 适用于 Angular 21+ 的现代富文本编辑器组件，原生支持图像、对齐、列表、颜色选择器和翻译。
* [ngx-pro-editor](https://github.com/ChauhanShubham8758/ngx-pro-editor) - 功能丰富的 Angular 所见即所得编辑器，具有自动保存、特殊字符和高级格式设置功能。
* [dragble-angular-editor](https://github.com/Dragble/dragble-angular-editor) - 双模式 Angular 组件将设计人员友好的可视化编辑器与人工智能驱动的对话界面融为一体。

### 文件上传

* [ng2-file-upload](https://github.com/valor-software/ng2-file-upload) - 易于使用的文件上传指令。
* [ngx-flow](https://github.com/flowjs/ngx-flow) - 用于文件上传的 [flow.js](https://github.com/flowjs/flow.js) 的 Angular7+ 包装器。
* [ngx-uploadx](https://github.com/kukhariev/ngx-uploadx) - Angular 可续传上传模块。
* [file-upload](https://github.com/pIvan/file-upload) - 用于文件上传的 Angular 模块。
* [ngx-file-drop](https://github.com/georgipeltekov/ngx-file-drop) - 用于简单桌面文件和文件夹拖放的 Angular 模块。该库不需要 rxjs-compat。
* [Uppy](https://github.com/transloadit/uppy) - 一个时尚、模块化的 JavaScript 文件上传器，[与 Angular 无缝集成](https://uppy.io/docs/angular/)。
* [ngx-custom-material-file-input](https://github.com/daemons88/ngx-custom-material-file-input) - Angular Material 的文件输入管理。
* [ngx-file-preview](https://github.com/wh131462/ngx-file-preview) - 适用于多种文件类型的强大预览工具。
* [ngx-file-helpers](https://github.com/fvilers/ngx-file-helpers) - Angular 文件助手包括文件选择器和拖放区。
* [ngx-file-uploader](https://github.com/uniprank/ngx-file-uploader) - 带有内置文件预览的 Angular 上传组件和指令。
* [file-uploader](https://github.com/uploadcare/file-uploader) - 基于 Web 组件的文件上传小部件，与任何 JavaScript 框架（React、Next.js、Vue、Angular 和 Svelte）兼容，无需适配器。
* [ngx-accessible-dropzone](https://github.com/mahmoudQq2023/ngx-accessible-dropzone) - 一个小型、零依赖、完全可访问的 Angular 拖放文件上传组件，支持键盘和屏幕阅读器。

### 表格

* [ngx-mask](https://github.com/JsDaddy/ngx-mask) - 用于在表单字段和 html 元素上制作遮罩的 Angular 插件。
* [maskito](https://github.com/taiga-family/maskito) - 用于创建输入掩码的库集合，确保用户根据预定义格式键入值。
* [ng-signal-forms](https://github.com/timdeschryver/ng-signal-forms) - 信号供电的角度形式。
* [ngx-sub-form](https://github.com/cloudnc/ngx-sub-form) - 用于将 Angular 形式分解为多个组件的实用程序库。
* [ngx-currency-v2](https://github.com/gabriel-hawerroth/ngx-currency-v2) - [ngx-currency](https://github.com/nbfontana/ngx-currency) 的一个分支已更新为最新的 Angular 版本。
* [ngx-enhancy-forms](https://github.com/klippa-app/ngx-enhancy-forms) - 花哨的增强型 Angular 形式。
* [ngx-focus-entities](https://github.com/klee-contrib/ngx-focus-entities) - 用于从使用 [TopModel](https://github.com/klee-contrib/topmodel) 生成的 Focus4 表示生成反应式 Angular 表单的库。
* [@TanStack/form](https://github.com/TanStack/form) - 凭借 TypeScript 支持、无头 UI 和与框架无关的设计，它简化了跨框架表单处理。
* [@luistabotelho/angular-signal-forms](https://github.com/luistabotelho/angular-signal-forms) - 使用信号实现表单的简单 Angular 库。
* [ngx-form-object](https://github.com/infinum/ngx-form-object) - 对 Angular 反应形式的抽象，可从模型生成形式并管理嵌套关系。
* [pro-form](https://github.com/ProAngular/pro-form) - 一组基于 Angular Material 的预定义反应式且可重用的表单输入组件。
* [ngx-forms](https://github.com/nncl/ngx-forms) - Angular 表单函数的集合，将帮助您构建应用程序。
* [ngxAccessor](https://github.com/Zarlex/ngxAccessor) - 该库为 Angular 形式添加了第三种方法，将信号与现有方法一起集成并具有适应性。
* [angular-template-signal-forms](https://github.com/chocosd/angular-template-signal-forms) - 使用 Signals 从头开始​​构建的现代 Angular 表单库 — 灵活、类型安全且完全主题化。
* [ngx-formidable](https://github.com/Cynthion/ngx-formidable) - 强大的 Angular 组件库，用于构建丰富的、经过验证的表单。
* [piying-view](https://github.com/piying-org/piying-view) - 强类型前端表单解决方案； “ngx-formly”和 Angular 官方表单框架的替代方案。
* [ngx-form-m3](https://github.com/webilix/ngx-form-m3) - Angular 和 Material 3 的波斯语表单库。
* [lite-form](https://github.com/liangk/lite-form) - 一个轻量级的 Angular 库，提供具有验证、样式和动画功能的可定制表单组件。
* [cc-form-engine](https://github.com/ChristianCruzArango/cc-form-engine) - 高级 Angular 库，用于反应式表单生成和管理，具有动态验证、更改跟踪和可定制的错误消息。
* [ngx-vest-forms](https://github.com/ngx-vest-forms/ngx-vest-forms) - 一个轻量级、类型安全的适配器，将 Angular 模板驱动的表单与 [Vest.js](https://vestjs.dev/) 链接起来，以进行复杂的异步验证。
* [ngx-autosave-forms](https://github.com/zinetnorf/ngx-autosave-forms) - 使用 Angular 中的模板表单或反应式表单将表单值自动保存在 localStorage 中。
* [ngx-better-forms](https://github.com/Bioroxx/ngx-better-forms) - 简化、可维护的反应式表单实用程序。
* [ngx-query-builder](https://github.com/solidexpert-ltd/ngx-query-builder) - Angular 查询构建器具有独立组件、合理的默认值、模板挂钩以及对特定于域的编辑器的完整形式支持。
* [ngx-mat-form](https://github.com/Salromag/ngx-mat-form) - Angular 库，使用 Reactive Forms 和 Angular Material 从模式动态生成可配置的表单。
* [ng-forge](https://github.com/ng-forge/ng-forge) - 为 Angular 基于信号的表单构建的类型安全的动态表单库。
* [zignal](https://github.com/biyonik/zignal) - 使用信号和 Zod 验证的类型安全 Angular 表单库，具有土耳其特定的验证器和多语言支持。
* [ngx-form-stepper](https://github.com/rayaneriahi/ngx-form-stepper) - 强类型 Angular 库，用于构建强大的多步骤表单，以最少的配置防止开发过程中出现无效状态。
* [ngx-form-rules](https://github.com/bulbul5391/ngx-form-rules) - 一个轻量级的 Angular 库，可以使用简单的声明性规则轻松启用、禁用和控制反应式表单字段。
* [ngx-reactive-forms-utils](https://github.com/pjlamb12/ngx-reactive-forms-utils) - 协助使用反应式 Angular 形式的实用程序。
* [ngx-entity-forms](https://github.com/irvrodflo/ngx-entity-form) - 从实体界面生成完全类型化的 Angular FormGroup，并包含自动完成、验证和错误消息。
* [ngx-form-draft](https://github.com/neokyuubi/ngx-form-draft) - 零依赖 Angular 表单草稿自动保存和恢复。
* [ngx-signal-forms](https://github.com/lorenzomusche/ngx-signal-forms) - 信号驱动、类型安全的 Angular 表单库，基于实验性 Signal Forms API 构建，具有现代 M3 样式。
* [formsync](https://github.com/sudhucodes/formsync) - 开发人员友好的 Angular 就绪表单后端，让您无需服务器端代码即可收集和管理提交内容。
* [@neutro-web/form](https://github.com/neutro-web/form) - 高性能、零依赖、与框架无关的反应式表单引擎。

### 表单控件

* [ngx-color-picker](https://github.com/zefoy/ngx-color-picker) - 颜色选择器小部件。
* [angular-colorful](https://github.com/ngx-eco/angular-colorful) - 适用于现代 Angular 应用程序的小型颜色选择器组件。
* [ng-select](https://github.com/ng-select/ng-select) - 全部在一个 UI 选择、多选和自动完成中。
* [file-input-accessor](https://github.com/jwelker110/file-input-accessor) - Angular 指令以 Angular 形式提供文件输入功能。
* [ngx-filesaver](https://github.com/cipchk/ngx-filesaver) - 使用 [FileSaver.js](https://github.com/eligrey/FileSaver.js) 简单保存文件。
* [ngx-bar-rating](https://github.com/MurhafSousli/ngx-bar-rating) - 角棒评级。
* [angular-code-input](https://github.com/AlexMiniApps/angular-code-input) - 适用于 Angular 7-16+ 的强大 Angular 输入组件（数字/字符），支持 Ionic 4-7、移动设备和剪贴板。
* [angular-iban](https://github.com/fundsaccess/angular-iban) - Angular 的 IBAN 指令和管道。
* [ngx-autosize-input](https://github.com/joshuawwright/ngx-autosize-input) - 自动调整输入元素宽度的 Angular 指令。它会收缩并增加宽度。
* [angular-cc-library](https://github.com/timofei-iatsenko/angular-cc-library) - 支持信用卡输入屏蔽和验证的库。
* [ngx-ui-switch](https://github.com/webcat12345/ngx-ui-switch) - 一个简单的 iOS 7 风格的 Angular 开关组件。
* [ngx-otp-input](https://github.com/pkovzz/ngx-otp-input) - Angular 的一次性密码输入库。
* [ngx-show-hide-password](https://github.com/osahner/ngx-show-hide-password) - 添加分割输入按钮以进行密码或文本输入。在“文本”和“密码”之间切换输入类型。
* [ngx-phone-field](https://github.com/alex-mirankov/ngx-phone-field) - 用于国际电话输入的 Angular 指令，带有标志下拉菜单，支持反应式和模板驱动表单。
* [ngx-mat-birthday-input](https://github.com/rbalet/ngx-mat-birthday-input) - 用于输入生日的 Angular Material 库。
* [ngx-countries-dropdown](https://github.com/kapilkumar0037/ngx-countries-dropdown) - Angular 库具有可定制的国家/地区下拉组件，其中包含标志、拨号代码、语言和货币详细信息。
* [ngx-mat-split-button](https://github.com/feature23/ngx-mat-split-button) - Angular Material 拆分按钮，具有主要操作和次要选项的下拉菜单。
* [ng-select2](https://github.com/Harvest-Dev/ng-select2) - [select2-component](https://github.com/plantain-00/select2-component) 的更新分支。
* [ngx-super-select](https://github.com/HesamKashefi/ngx-super-select) - Angular 的多选输入组件。
* [ngx-super-select-tree](https://github.com/HesamKashefi/ngx-super-select-tree) - Angular 的单选/多选下拉树！
* [ngx-mat-table-multi-sort](https://github.com/pgerke/ngx-mat-table-multi-sort) - 向 Angular Material 表添加多重排序功能。
* [ng-country-select](https://github.com/wlucha/ng-country-select) - 带有国旗和代码的智能多语言国家/地区搜索。
* [ngx-cron](https://github.com/swimlane/ngx-cron) - 用户友好的 cron 输入。
* [@amirsavand/ngx-input](https://www.npmjs.com/package/@amirsavand/ngx-input) - 很棒的一体化 Angular 包，用于输入和表单处理。
* [ng-otp-input](https://github.com/code-farmz/ng-otp-input) - 一款完全可定制的一次性密码 (OTP) 输入组件，适用于使用 Angular 构建的 Web。
* [rm-ng-star-rating](https://github.com/malikrajat/rm-ng-star-rating) - 完全可定制且功能丰富的 Angular 独立组件，可通过精确且响应式的设计实现高级星级评定。
* [ngx-animated-paginator](https://github.com/eladbh-stanley/ngx-animated-paginator) - [animated-paginator-web-component](https://www.npmjs.com/package/animated-paginator-web-component) 的角度包装器，通过“ControlValueAccessor”无缝插入模板驱动和反应式表单。
* [ngx-input-color](https://github.com/mr-samani/ngx-input-color) - `ngx-input-gradient` 和 `ngx-input-color` 是可定制的 Angular 组件，用于通过预览和表单集成来选择颜色/渐变。
* [ngx-morse](https://github.com/monkeyscript/ngx-morse) - Angular 的简单莫尔斯电码编码器和解码器。
* [ngxsmk-tel-input](https://github.com/toozuuu/ngxsmk-tel-input) - 一个 Angular 电话输入组件，具有国家/地区下拉列表、标志和强大的验证/格式设置。
* [gradient-picker](https://github.com/acrodata/gradient-picker) - 一个强大而美丽的渐变选择器。
* [ngxsmk-datepicker](https://github.com/toozuuu/ngxsmk-datepicker) - 一个现代的、高度可定制的 Angular 日期范围选择器组件。
* [ngx-country-selector](https://github.com/evicio1/ngx-country-selector) - 时尚、可定制的 Angular Material 国家/地区选择器，提供可访问的下拉菜单，其中包含国旗、代码、本地名称等。
* [@nsnayp1/angular-datepicker2](https://github.com/nsnayp13/angular-datepicker2) - 轻量级 Angular 16+ 日期选择器，具有独立支持、范围和多日期选择以及可自定义模板 - 无外部依赖项。
* [ngx-phone](https://github.com/manishpatidar028/ngx-phone) - Angular 手机输入具有自动国家/地区检测、实时格式化、验证和完整表单支持。
* [ngx-phone-country-input](https://github.com/mostafaM212/ngx-phone-country-input) - 用于电话输入和国家/地区选择的综合 Angular 库，支持反应式表单。
* [ngx-mat-period-picker](https://github.com/felixdulfer/ngx-mat-period-picker) - 使用独立组件构建的现代 Angular Material 周期选择器组件。
* [touchspin-angular](https://github.com/istvan-ujjmeszaros/touchspin-angular) - 用于 [TouchSpin](https://github.com/istvan-ujjmeszaros/touchspin) 数字输入组件的角度适配器，支持每个渲染器。
* [ngx-cron-editor](https://github.com/haavardj/ngx-cron-editor) - 图形化 Angular 15+ cron 构建器，具有反应式表单集成和 Material Design 样式。
* [ngx-otp-code-input](https://github.com/Swaraj55/otp-input) - Angular OTP 输入组件，具有广泛的自定义选项，包括屏蔽、纯数字输入和自动对焦。
* [smart-date-input](https://github.com/ngxpert/smart-date-input) - 智能日期输入指令，使用 Writer API 解析自然语言日期。
* [color-picker](https://github.com/acrodata/color-picker) - 另一个漂亮的颜色选择器。
* [ngx-pattern-lock](https://github.com/nicotole/ngx-pattern-lock) - 适用于 Angular 的轻量级、完全响应式且可定制的 Android 风格模式锁定组件。
* [smt-select](https://github.com/sametacar/smt-select) - 高性能、轻量级、可定制的 Angular 选择组件，具有内置虚拟滚动和搜索功能。
* [ngx-mat-searchable-select](https://github.com/khalilElmouedene/ngx-mat-searchable-select) - 一个可重复使用的 Angular Material 选择组件，具有无限滚动、去抖动搜索、“未找到项目”反馈以及静态/模拟数据支持。
* [mat-password-meter](https://github.com/ngx-zen/mat-password-meter) - Angular 密码强度计（[zxcvbn](https://github.com/dropbox/zxcvbn)，符合 NIST，可定制）。
* [nicematic-emoji-picker](https://github.com/myposty/nicematic-emoji-picker) - 适用于 Angular 17+ 的高性能、零依赖表情符号选择器，具有 929 个表情符号、自动主题、i18n 和响应式设计。
* [ngx-starflow](https://github.com/ahmadfakher/ngx-starflow) - 一个轻量级的 Angular 组件，用于高精度地显示分数星级。
* [combobox](https://github.com/ng-matero/combobox) - 具有内置多项选择和自动完成功能的一体化 Angular Select 解决方案。
* [BlossomColorPicker](https://github.com/dayflow-js/BlossomColorPicker) - 一个精美的、绚丽的 Web 颜色选择器，作为独立的 JS 库提供，带有 Angular、React、Vue 和 Svelte 的轻量级包装器。
* [ngx-intl-phone-input](https://github.com/JoaoHenriqueAlmeida/ngx-intl-phone-input) - 可访问的无头 Angular 国际电话输入，带有 CDK 驱动的国家/地区选择器。
* [ngx-colors2](https://github.com/DominicWrege/ngx-colors) - 针对 Angular 20+ 更新的材质风格 Angular 颜色选择器，使用信号且无动画依赖性。
* [ngx-signal-datetimepicker](https://github.com/dominikmodrzejewski99/ngx-signal-datetimepicker) - 基于 Signal Forms 构建的 Angular 日期时间选择器 — 日期 + 时间在一个控件中，零依赖，开箱即用的 WCAG 2.2 AAA。
* [ngx-multi-field-dropdown](https://github.com/luismtapiab/ngx-multi-field-dropdown) - 具有多字段搜索支持的可定制 Angular 可搜索下拉组件。
* [angular-multiselect-dropdown](https://github.com/alexandroit/angular-multiselect-dropdown) - 为模板驱动和反应式表单构建的维护的 Angular 多选下拉列表。
* [@koenz/angular-datepicker](https://github.com/koenz/angular-datepicker) - 适用于 Angular 21+ 的动画日期选择器。
* [ngx-dual-rangepicker](https://github.com/olivierpetitjean/ngx-dual-rangepicker) - 适用于 Angular 20+ 和 Angular Material M3 的双日历日期范围选择器。

### JSON 表单

* [ngx-formly](https://github.com/ngx-formly/ngx-formly) - JSON 驱动/Angular 的动态表单。
* [formio](https://github.com/formio/angular) - Angular 的 JSON 支持表单。
* [fluent-form](https://github.com/fluent-form/fluent-form) - 使用 Fluent API 或 JSON 在 Angular 中构建动态表单。
* [jsonforms](https://github.com/eclipsesource/jsonforms) - 可定制的基于 JSON Schema 的表单，具有开箱即用的 React、Angular 和 Vue 支持。
* [jsonforms-angular-seed](https://github.com/eclipsesource/jsonforms-angular-seed) - 基于 Angular 的 JSON Forms 种子应用程序。
* [ng-formworks](https://github.com/zahmo/ng-formworks) - 一个 Angular [JSON 模式](https://json-schema.org/) 表单构建器，与 [Angular 模式表单](http://schemaform.io/examples/bootstrap-example.html)、[React JSON 模式表单](https://rjsf-team.github.io/react-jsonschema-form/) 和 [JSON 表单](https://ulion.github.io/jsonform/playground/) 类似，并且大部分 API 兼容。
* [DynamicAngularForm](https://github.com/Brrake/DynamicAngularForm) - 通过传递带有关联值的 JSON 创建动态表单。
* [dynamic-forms](https://github.com/dynamic-forms/dynamic-forms) - 基于 JSON 的动态表单的 Angular 项目。
* [json-forms-zorro-wrapper](https://github.com/wojtek1150/json-forms-zorro-wrapper) - Ng Zorro json 表单库的包装器。
* [ngx-formwork](https://github.com/TheNordicOne/ngx-formwork) - 根据 JSON 或 TypeScript 配置构建的 Angular Reactive Forms 框架。
* [ngx-formbar](https://github.com/TheNordicOne/ngx-formbar) - 用于生成声明性反应形式的高度灵活的框架。
* [formitiva](https://github.com/formitiva/formitiva-monorepo) - 与框架无关的运行时表单引擎，用于从 JSON 模式构建表单。

### 表单验证

* [ngx-valdemort](https://github.com/Ninja-Squad/ngx-valdemort) - 更简单、更清晰的 Angular 验证错误消息。
* [validointi](https://github.com/validointi/validointi) - 这是一个帮助您验证模板驱动表单的库。
* [angular-reactive-validation](https://github.com/davidwalschots/angular-reactive-validation) - 该库消除了对大量 HTML 的需求，从而简化了反应式表单验证。
* [ngx-formcontrol-errors](https://github.com/dgonzalez870/ngx-formcontrol-errors) - 用于显示 Angular 表单控件中的错误的指令。
* [ngx-validator-pack](https://github.com/dynimorius/ngx-validator-pack) - 旨在简化使用并允许快速定制的验证器集合。
* [ngx-reactive-form-class-validator](https://github.com/abarghoud/ngx-reactive-form-class-validator) - 一个轻量级库，用于使用 [class-validator](https://github.com/typestack/class-validator) 库动态验证 Angular 反应式表单。
* [ng-error-tooltips](https://github.com/mkeller1992/ng-error-tooltips) - Angular 反应式表单库，显示错误工具提示，以提供用户友好的验证消息。
* [ng-reactive-form-validate](https://github.com/vbnr/ng-reactive-form-validate) - 用于简化表单验证的 Angular 库，具有可自定义消息、Transloco 集成和样式错误标签。
* [angular-password-checker](https://github.com/akehir/angular-password-checker) - 通过这个简单的 Angular 指令，防止您的用户重复使用已知被黑客攻击的密码。
* [translation-validation](https://github.com/RiskChallenger/translation-validation) - 任何语言的 Angular 表单的自动验证消息。
* [polish-validators](https://github.com/joker876/polish-validators) - 专为波兰语特定格式设计的验证库，也可通过 [ngx-polish-validators](https://www.npmjs.com/package/ngx-polish-validators) 作为 Angular 包装器使用。
* [ngx-mat-errors](https://github.com/Totati/ngx-mat-errors) - 提供了一种简单且适应性强的方法来在“MatFormField”中呈现错误消息。
* [oop-validator](https://github.com/visaruruqi/oop-validator) - 适用于任何 UI 框架（Vue、React、Angular 等）的强大、灵活的验证库，可实现完整的前端验证。
* [ngx-cross-field-validation](https://github.com/soc221b/ngx-cross-field-validation) - Angular 库提供对表单控件的条件、相等、不等和基于序列的验证。
* [validauth](https://github.com/adiksuu/validauth) - 适用于 JavaScript 应用程序的轻量级、强大的身份验证验证器。
* [ngx-validation-messages](https://github.com/lagoshny/ngx-validation-messages) - 该模块通过使用单个组件简化了表单验证器消息的显示。

### 图标

* [angular-fontawesome](https://github.com/FortAwesome/angular-fontawesome) - Font Awesome 5+ 的官方 Angular 组件。
* [ng-icons](https://github.com/ng-icons/ng-icons) - Angular 的终极图标库。
* [angular-svg-icon](https://github.com/czeckd/angular-svg-icon) - 用于内联 SVG 的 Angular 组件和服务，允许使用 CSS 轻松设置它们的样式。
* [ng-hero-icons](https://github.com/dimaslz/ng-heroicons) - 在 Angular 应用程序中使用 [Heroicons](https://heroicons.com)。
* [ngx-fluent-ui](https://github.com/bennymeg/ngx-fluent-ui) - Microsoft Fluent UI 图标的 Angular 和在线库。
* [angular-line-awesome](https://github.com/marco-martins/angular-line-awesome) - Angular Line Awesome 是一个用于管理 [Line Awesome](https://icons8.com/line-awesome) 图标的 Angular 组件。
* [angular-techs-logos](https://github.com/criar-art/angular-techs-logos) - 技术相关图标库。
* [ngx-x-browser-svg-mask](https://github.com/bmartinson/ngx-x-browser-svg-mask) - 在创建 SVG 蒙版时轻松实现跨浏览器合规性的指令。
* [Semantic Icons](https://github.com/khalilou88/semantic-icons) - 通过组件选择器和 SVG 标签为 Angular 项目提供免费的开源图标集合。
* [coolshapes](https://github.com/ngxpert/coolshapes) - 一个 Angular 库，旨在允许开发人员使用来自 [coolshapes](https://coolshap.es/) 的带有小颗粒渐变的酷炫抽象形状。
* [lucide](https://github.com/lucide-icons/lucide) - 具有 1000 多个 SVG 的开源图标库，具有[官方 Angular 包](https://lucide.dev/guide/packages/lucide-angular)，可轻松集成。
* [@ngverse/icons](https://github.com/ngverse/icons) - Angular 库允许您使用流行的开源图标作为常规组件。
* [ngxi](https://github.com/adrian-ub/ngxi) - 适用于 Angular 的全面 SVG 图标集，无缝集成数千个流行图标。
* [animated-icons](https://github.com/ajitzero/animated-icons) - 基于[移动图标](https://www.movi​​ngicons.dev/)的 Angular 动画图标。
* [hugeicons-angular](https://github.com/hugeicons/angular) - 超过 5,100 个 MIT 许可的免费 Angular 圆角图标。
* [@quikturn-sdk/logos-angular](https://github.com/quikturn-sdk/Company-Logos) - 适用于 [Quikturn Logos API](https://getquikturn.io/) 的 TypeScript SDK - 通过域名获取任何公司的徽标。

### 图片

* [cloudinary](https://cloudinary.com/documentation/angular_integration) - 来自 Cloudinary 的 Angular SDK。
* [ng-cropper](https://github.com/DanielGabbay/ng-cropper) - 基于“CropperJS”构建的角度图像裁剪器，具有可定制的界面和可选的工具栏，可实现无缝裁剪。
* [ngx-advanced-img](https://github.com/bmartinson/ngx-advanced-img) - Angular 属性指令套件提供各种 HTML img 功能扩展。
* [ngx-avatars](https://github.com/Heatmanofurioso/ngx-avatars) - [ngx-avatar](https://github.com/HaithemMosbahi/ngx-avatar)的精神继承者。
* [ngx-broken-img](https://github.com/andreagrossetti/ngx-broken-img) - 用于修复 img 中损坏的 url 的 Angular 指令。如果图像url返回404，则使用占位符来填充img的src。
* [ngx-image-compression](https://github.com/ShreyashThorat-17/ngx-image-compression) - Angular 的轻量级图像压缩和转换库。
* [ngx-image-cropper](https://github.com/Mawi137/ngx-image-cropper) - Angular 的图像裁剪器。
* [ngx-image-magnifier](https://github.com/SeriousSez/ngx-image-magnifier) - 角度图像放大镜指令，具有键盘修改器支持、智能定位、移动优化和流畅的 GPU 加速动画。
* [ngx-img-cropper](https://github.com/web-dave/ngx-img-cropper) - Angular 的图像裁剪工具。
* [@jjmhalew/ngx-lightbox](https://github.com/jjmhalew/ngx-lightbox) - 与 Angular >= 18（无区域）一起使用的 [lightbox2](https://github.com/lokesh/lightbox2) 实现端口。
* [@necraidan/ngx-lightbox](https://github.com/necraidan/ngx-lightbox) - 一个轻量级、易于访问的 Angular 21+ 灯箱，具有缩放、平移、捏合缩放和键盘导航功能，所有这些都具有零依赖性。
* [ngx-pinch-zoom](https://github.com/medDV-GmbH/ngx-pinch-zoom) - 该模块可以通过触摸屏手势实现图像缩放和定位。
* [ngx-smart-cropper](https://github.com/kurti-vdb/ngx-smart-cropper) - Angular 独立图像上传器，具有裁剪、调整大小、拖动和调整大小、网格覆盖和纵横比支持。
* [unpic](https://unpic.pics/img/angular/) - 用于响应式高性能图像的 Angular 指令，具有自动 srcset、大小调整和 CDN/CMS URL 检测功能。
* [ngx-image-fallback](https://github.com/joyblanks/ngx-image-fallback) - Angular 的图像后备指令。
* [ng-image-optimizer](https://github.com/Hasan-Kakeh/ng-image-optimizer) - 高性能 Angular SSR 图像优化器，使用 [Sharp](https://sharp.pixelplumbing.com/) 提供 Next.js 风格的体验。
* [ngx-ratio-image](https://github.com/gerd-siebert/ngx-ratio-image) - Angular 库，用于在具有固定宽高比的容器内显示具有可变宽高比的图像。

### 键盘鼠标

* [angular-touch-keyboard](https://github.com/mohsen77sk/angular-touch-keyboard) - 用于 Angular 应用程序的虚拟键盘。
* [ngx-contextmenu](https://github.com/PerfectMemory/ngx-contextmenu) - Angular 的上下文菜单组件。
* [ngx-keys](https://github.com/mrivasperez/ngx-keys) - 反应式 Angular 库，用于通过基于信号的 UI 集成来管理键盘快捷键。
* [focusly](https://github.com/mad-vx/focusly) - 一个轻量级的 Angular 库，为 Web 应用程序带来直观的、键盘驱动的导航。
* [ngx-arrow-state](https://github.com/jaychase/ngx-arrow-state) - 一个 Angular 库，使用箭头键提供类似终端/shell 的输入历史导航，以及文本区域的 Ctrl+Enter 表单提交。
* [angular-onscreen-material-keyboard](https://github.com/eFaps/angular-onscreen-material-keyboard) - 使用 Angular Material 的 Angular 屏幕虚拟键盘。
* [@TanStack/hotkeys](https://github.com/TanStack/hotkeys) - 类型安全的键盘快捷键库，具有出色的开发工具。
* [ngx-keyboard-shortcuts](https://github.com/phalgunv/ngx-keyboard-shortcuts) - 已归档 [ngx-keyboard-shortcuts](https://github.com/milestechnologies/ngx-keyboard-shortcuts) 包的一个积极维护的分支，添加了 Angular 16+ 支持和现代工具。
* [ngx-command-palette](https://github.com/theryansmee/ngx-command-palette) - 零设置、键盘驱动的 Angular 命令面板，具有自动注册路线、自定义命令、异步搜索和上下文可见性。

### 布局

* [angular-split](https://github.com/bertrandg/angular-split) - 角分割组件。
* [ngx-layout](https://github.com/ngbracket/ngx-layout) - Angular FlexLayout 的克隆。
* [ng-sortgrid](https://github.com/kreuzerk/ng-sortgrid) - 网格允许您通过拖放对所有项目进行排序。
* [angular-gridster2](https://github.com/tiberiuzuld/angular-gridster2) - 角网格2.
* [angular-grid-layout](https://github.com/katoid/angular-grid-layout) - 响应式网格，具有适用于 Angular 应用程序的可拖动和可调整大小的项目。
* [gridstack](https://github.com/gridstack/gridstack.js/tree/master/angular/) - 适合移动设备的 TypeScript 库，用于支持 Angular 的拖放、多列响应式仪表板。
* [ngx-flickering-grid](https://github.com/omnedia/ngx-flickering-grid) - 一个简单的组件库，用于创建具有动画网格图案背景的容器。
* [ngx-gridpattern](https://github.com/omnedia/ngx-gridpattern) - 一个简单的组件库，用于创建具有图案背景的容器。
* [ngx-retro-grid](https://github.com/omnedia/ngx-retro-grid) - 3D 透视网格组件，具有可定制的颜色、旋转和流畅的动画，可实现怀旧或未来效果。
* [ngx-bottom-sheet](https://github.com/ArslanAmeer/ngx-bottom-sheet) - 高度可定制的轻量级 Angular 服务，提供适合移动设备的底部表单组件。
* [ngx-swipe-menu](https://github.com/charlesschaefer/ngx-swipe-menu) - 用于创建“向左滑动以执行‘操作’”体验的组件。
* [berg-layout](https://github.com/blidblid/berg-layout) - 此 monorepo 包含 [Berg Layout for Angular](https://www.npmjs.com/package/@berg-layout/angular)、React 和 Web Components 的版本。
* [static-columns](https://github.com/darekf77/static-columns) - 使用 Angular 和 FlexBox 定义具有静态宽度的列。
* [ngx-flex-layout](https://github.com/jtc10005/ngx-flex-layout) - [Angular Flex Layout](https://github.com/angular/flex-layout) 的端口在 EOL 后提供支持。
* [ng-polymorpheus](https://github.com/taiga-family/ng-polymorpheus) - Angular 中多态模板的小型库。
* [gui](https://github.com/acrodata/gui) - 用于可配置面板的 JSON 支持的 GUI。
* [ngx-zoomable](https://github.com/json-k/ngx-zoomable) - 用于 Angular 应用程序的可缩放、可平移的容器组件。
* [ngx-material-drawer](https://github.com/ansarisufiyan777/ngx-material-drawer) - 可配置的角度材料抽屉和工具栏。
* [@marxlnfcs/ngx-grid](https://github.com/marxlnfcs/ngx-grid) - 用于现代网格布局的简单角度网格模块。
* [lightweight-grid-layout](https://github.com/liketiger/lightweight-grid-layout) - 一个用于 JavaScript/TypeScript 的无头、无依赖的网格布局库，可以与任何框架一起使用，也可以不与任何框架一起使用，将渲染和样式留给用户。
* [ng-flex-layout](https://github.com/alessiobianchini/ng-flex-layout) - Angular 库，提供基于 Flexbox 和 mediaQuery 可观察量构建的响应式、灵活的布局 API。
* [dockview-angular](https://www.npmjs.com/package/dockview-angular) - 零依赖布局管理器支持选项卡、组、网格和分割视图。
* [ngx-compactable-row](https://github.com/MikeVensel/ngx-compactable-row) - 提供响应式按钮行，在空间有限时将多余的按钮移至菜单中。

### 装载机

* [angular-busy](https://github.com/tiberiuzuld/angular-busy) - 在 Promise/Observable 期间在任何元素上显示繁忙/加载指示器。
* [angular-svg-round-progressbar](https://github.com/crisbeto/angular-svg-round-progressbar) - 使用 SVG 创建圆形进度条的 Angular 模块。
* [boneyard](https://github.com/0xGF/boneyard) - 自动生成的骨架加载框架，可与 React、Preact、Vue、Svelte、Angular 和 React Native 配合使用。
* [groupix-spinner-library](https://github.com/ArshdeepGrover/groupix-spinner-library) - 用于无缝加载动画的轻量级 Angular 微调器库！
* [loaderx-arun](https://github.com/Arun44764/loaderx-arun) - 500 多个下一代动画 UI 加载器。
* [loadingTrace](https://github.com/lucapiciollo/loadingTrace) - 具有零样板、76 个动画、自动跟踪、命名叠加、确定进度、运行时配置和信号的角度加载叠加。
* [ng-overlay-skeleton-loader](https://github.com/ebrahim-salehipanah/ng-overlay-skeleton-loader) - 一个轻量级的 Angular 指令，用于向组件添加可自定义的骨架加载状态。
* [ngx-fastboot](https://github.com/KernelPanic92/ngx-fastboot) - 动态 Angular 配置加载器通过在单独的块中编译配置来提高启动性能。
* [ngx-loader](https://github.com/nisicadmir/ngx-loader) - 基本加载程序与状态管理服务配对。
* [ngx-loader-indicator](https://github.com/jsdaddy/ngx-loader-indicator) - 适用于 Angular 应用程序的出色加载程序。没有包装，只有你的元素。
* [ngx-loading-bar](https://github.com/aitboudad/ngx-loading-bar) - Angular 的自动页面加载/进度条。
* [ngx-loading-buttons](https://github.com/dkreider/ngx-loading-buttons) - 一个轻量级的 Angular 库，用于向 Angular Material 按钮添加加载微调器。
* [ngx-loading-overlay](https://github.com/shaman-apprentice/ngx-loading-overlay) - 一个 Angular 指令将加载覆盖层添加到 HTML。
* [ngx-progressbar](https://github.com/MurhafSousli/ngx-progressbar) - 纳米级进度条，具有逼真的滴流动画。
* [ngx-promise-buttons](https://github.com/meysamsahragard/ngx-promise-buttons) - Angular 的冷加载按钮。
* [ngx-signal-loading-bar](https://github.com/KennySchl/ngx-signal-loading-bar) - 用于 Angular 的轻量级、基于信号、无区域的加载栏。
* [ngx-skeleton-loader](https://github.com/willmendesneto/ngx-skeleton-loader) - 制作漂亮的动画加载骨架，自动适应您的 Angular 应用程序。
* [ngx-source](https://github.com/mehrabisajad/ngx-source) - 在应用程序执行期间动态加载 JavaScript 和 CSS。
* [ngx-spinner](https://github.com/napster2210/ngx-spinner) - 用于加载 Angular 微调器的库。
* [ngx-spinner-loading](https://github.com/thalsi/ngx-spinner-loading) - 轻量级、可定制的 Angular 微调器，具有全局、部分、内联加载器、HTTP 拦截器和基于信号的状态。
* [ngxsmk-skeleton-loader](https://github.com/Cholki2025/ngxsmk-skeleton-loader) - 一个轻量级的骨架加载器，具有 SCSS 动画和简单的主题。
* [ngx-ui-loader](https://github.com/t-ho/ngx-ui-loader) - 多功能 Angular 加载器/旋转器，具有前台/后台模式、进度条和多加载器支持。
* [shimmer-from-structure](https://github.com/darula-hpp/shimmer-from-structure) - 一个 React、Vue、Svelte 和 Angular 闪光/骨架库，可自动适应组件的运行时结构。
* [skedapt](https://github.com/z4k7/skedapt) - 用于 Angular 的零配置自适应骨架加载器，用于装饰主机元素，以便骨架自动匹配容器的自然布局。
* [skeletonizer](https://github.com/lukaVarga/skeletonizer) - 轻量级、可定制的包，用于使用 Vue 和 Angular 适配器创建骨架视图。
* [skeleton-styler](https://github.com/HoaiNam071001/skeleton-styler) - 一个轻量级的、与框架无关的库，用于生成具有可定制样式和动画的骨架加载 UI。

### 伐木工

* [lumberjack](https://github.com/ngworker/lumberjack) - 多功能 Angular 日志记录库，具有内置驱动程序和自定义日志驱动程序的轻松自定义功能。
* [log4ngx](https://github.com/secondbounce/log4ngx) - 用于 Angular 项目的 TypeScript 日志记录框架，基于 Log4j、Log4net 等中使用的概念。
* [candy-logger](https://github.com/shehari007/candy-logger) - 用于 JavaScript/TypeScript 的轻量级日志库，在浏览器中具有弹出式 UI，并在 Node.js 中提供增强的终端输出。
* [@pubfunc/ngx-common-log](https://github.com/pubfunc/ngx-libs/tree/master/packages/common/log) - 适用于 Angular 应用程序的灵活日志库，支持多种传输、日志级别、命名空间和依赖项注入。

### 地图

* [cesium-angular-example](https://github.com/Developer-Plexscape/cesium-angular-example) - 一个简单的 Web 应用程序，演示了 [Cesium](https://cesium.com) 与最新版本 Angular 的集成。
* [ngx-mapbox-gl](https://github.com/Wykks/ngx-mapbox-gl) - `mapbox-gl-js` 的角度绑定。
* [ngx-leaflet](https://github.com/bluehalo/ngx-leaflet) - Angular 的核心 Leaflet 包。
* [ngx-leaflet-markercluster](https://github.com/bluehalo/ngx-leaflet-markercluster) - 提供与 Angular 项目的 [leaflet.markercluster](https://github.com/Leaflet/Leaflet.markercluster) 集成。
* [ngx-maplibre-gl](https://github.com/maplibre/ngx-maplibre-gl) - maplibre-gl 的角度绑定。
* [ng-azure-maps](https://github.com/arnaudleclerc/ng-azure-maps) - 用于 azure-maps-controls 的 Angular HTML 驱动包装器，可轻松集成到 Angular 应用程序中。
* [ngx-gaia-gis](https://github.com/Olympus-Analytics/ngx-gaia-gis) - 一种 Angular 服务，可使用强大的 [OpenLayers](https://openlayers.org/) 库简化地图创建和交互。
* [ngx-google-maps-places](https://github.com/lekhmanrus/ngx-google-maps-places) - Google Maps Places API 的 Angular 包装器，简化了 Google Places 集成。
* [angular-yandex-maps](https://github.com/ddubrava/angular-yandex-maps) - Yandex.Maps 实现 Yandex.Maps JavaScript API 的 Angular 组件。
* [workletjs](https://github.com/workletjs/workletjs) - Angular 地图组件库，提供与 OpenLayers 的无缝集成，使开发人员能够创建交互式和可定制的地图。
* [ng-simple-maps](https://github.com/hanafnafs/ng-simple-maps) - 适用于 Angular 应用程序的漂亮、轻量级 SVG 世界地图。

### 降价

* [angular-markdown-editor](https://github.com/ghiscoding/angular-markdown-editor) - Angular Markdown 编辑器。一体化 Markdown 编辑器和预览。
* [markular](https://github.com/larswaechter/markular) - Angular 的轻量级 Markdown 编辑器。
* [mdbook-angular](https://github.com/bgotink/mdbook-angular) - [mdbook](https://rust-lang.github.io/mdBook/index.html) 的渲染器，可将 Angular 代码示例转换为运行的 Angular 应用程序。
* [md-juice](https://github.com/aruidev/md-juice) - 用于 Markdown HTML 输出的轻量级、标记化 CSS 主题。
* [ngx-markdown](https://github.com/jfcere/ngx-markdown) - 结合了 Marked、Prism.js、Emoji-Toolkit、KaTeX、Mermaid 和 Clipboard.js 的 Angular 库。
* [ngx-markdown-pages](https://github.com/jamesmandrews/ngx-markdown-pages) - 用于将 Markdown 文件渲染为可路由页面的 Angular 库。
* [ngx-md-editable](https://codeberg.org/tomaszatoo/ngx-md-editable) - 一个轻量级的 Angular 组件，可编辑 Markdown 并呈现富有表现力的 HTML 内容。
* [ngx-remark](https://github.com/ericleib/ngx-remark) - 使用自定义 Angular 模板渲染 Markdown。
* [ngx-streamdown](https://github.com/dina-kar/ngx-streamdown) - [Streamdown](https://streamdown.ai/) 的 Angular 端口是针对 AI 驱动的应用程序优化的流式 Markdown 渲染器。
* [mark-down](https://github.com/mzebley/mark-down) - 一个与框架无关的代码片段引擎，带有 Angular 适配器，可在构建时对 Markdown 进行索引，并在运行时通过可选的清理功能呈现 HTML。
* [m-render](https://github.com/Foblex/m-render) - 用于渲染 Markdown 的库，具有对 Angular 组件和代码片段的扩展支持。
* [markstream](https://github.com/Simon-He95/markstream-vue) - 在 Markdown 仍在流式传输时渲染它。

### 媒体

* [angular-audio-context](https://github.com/chrisguttandin/angular-audio-context) - Web Audio API 的 AudioContext 的 Angular 包装器。
* [silicon-audio-wave](https://github.com/joldibaev/silicon-audio-wave) - 来自硅的非常简单的音频波系统。
* [Vidstack](https://github.com/vidstack/player) - 具有用于自定义 Web 媒体播放器的 UI 组件的框架，以及可自定义的默认布局。请参阅[安装指南](https://www.vidstack.io/docs/player/getting-started/installation/angular?styling=default-layout&provider=video)。
* [@dytesdk/web-core](https://www.npmjs.com/package/@dytesdk/web-core) - 本[快速入门](https://docs.dyte.io/guides/livestream/client-setup/angular)展示了如何将 Dyte 的 Livestream SDK 添加到 Angular 应用程序中。
* [voicecapture-angular](https://github.com/angular-a11y/voicecapture-angular) - 该库提供了用于处理语音输入和转录的可定制选项，使其成为增强用户界面的灵活解决方案。
* [ngx-cam-shoot](https://github.com/RzoDev/ngx-cam-shoot) - 简化的 Angular 组件，可简化设备相机的使用并加速图像捕获和保存。
* [cometchat-uikit-angular](https://github.com/cometchat/cometchat-uikit-angular) - [CometChat](https://www.cometchat.com/) Angular UI Kit 提供预构建的 UI，可实现快速、可靠、功能齐全的聊天集成。
* [ngx-user-camera](https://codeberg.org/tomaszatoo/ngx-user-camera) - 现代 Angular 20+ 相机组件，具有前/后切换、可选画布渲染和无区域反应信号。
* [ngx-rumbletalk](https://github.com/RumbleTalk/ngx-rumbletalk) - 用于 [Rumbletalk](https://rumbletalk.com/) 群聊的 Angular 库。
* [ng-three-model-cropper](https://github.com/AlexRynas/ng-three-model-cropper) - Angular `Three.js` 库，用于可配置 3D 模型裁剪，支持 GLB/FBX 和三角形修剪导出。
* [@ngx-core/media-optimizer](https://github.com/barbozaa/media-optimizer-workspace) - 用于图像优化、转换和压缩的专业框架无关库。
* [ngx-streaming-player](https://github.com/jhonsferg/ngx-streaming-player) - 一个统一的即插即用视频播放器组件，可通过单个 API 处理 HLS、DASH、MP4 和 YouTube。
* [ngx-pro-media-player](https://github.com/kamal-dev1/ngx-pro-media-player) - Angular 媒体播放器，具有音频、视频、队列、交叉淡入淡出、歌词和 RTL 支持。
* [MediaSFU-Angular](https://github.com/MediaSFU/MediaSFU-Angular) - 用于 WebRTC 视频会议、网络研讨会、直播、聊天、屏幕共享、录音、分组讨论室、白板、投票、实时字幕和翻译的 Angular SDK。

### 混合公用事业

* [Official Angular Components repository](https://github.com/angular/components) - Angular 的组件基础设施和 Material Design 组件。
* [rx-angular](https://github.com/rx-angular/rx-angular) - RxAngular 工具包适用于完全响应式应用程序，专注于性能、模板渲染和开发人员体验。
* [ng-web-apis](https://github.com/taiga-family/ng-web-apis) - 一组用于通过 Angular 使用 Web API 的常用实用程序。
* [daffodil](https://github.com/graycoreio/daffodil) - Angular 电子商务 PWA 框架。
* [ngworker](https://github.com/ngworker/ngworker) - @ngworker NPM 组织的 Monorepo。用于 Angular 应用程序和测试的包。
* [jscutlery devkit](https://github.com/jscutlery/devkit) - 让 Angular 开发人员的生活变得更轻松的工具。
* [lithium-angular](https://github.com/lVlyke/lithium-angular) - Lithium 通过无缝反应状态和事件交互的实用程序简化了 Angular。
* [rxweb](https://github.com/rxweb/rxweb) - 大量适用于 Angular、Vue 和 React 项目的功能丰富的软件包。
* [ngspot](https://github.com/DmitryEfimenko/ngspot) - 很棒的 Angular 库的集合。
* [ts-cacheable](https://github.com/angelnikolov/ts-cacheable) - 一个流行的与平台无关的缓存库。
* [ngxtension-platform](https://github.com/ngxtension/ngxtension-platform) - Angular 的实用程序。
* [spartan](https://github.com/goetzrobin/spartan) - 支持 Angular 全栈开发的尖端工具。
* [ngify](https://github.com/ngify/ngify) - 在 Angular 之外使用 Angular 功能。
* [angular-ru-sdk](https://github.com/Angular-RU/angular-ru-sdk) - 用于常见交互模式的工具链集，抽象 Angular 核心功能而没有呈现偏差。
* [dfts-common](https://github.com/Dafnik/dfts-common) - TypeScript 库的集合（图标和其他实用程序）。
* [dfx-common](https://github.com/Dafnik/dfx-common) - Angular 库的集合，包括“dfx-qrcode”等。
* [sba-angular](https://github.com/sinequa/sba-angular) - [Sinequa 的](https://www.sinequa.com/) 基于 Angular 的搜索应用程序 (SBA) 框架。
* [ng-as](https://github.com/nigrosimone/ng-as) - 用于类型转换模板变量的角度管道和指令。
* [angular-toolbox](https://github.com/pechemann/angular-toolbox) - 一个为 Angular 应用程序开发提供有用工具的库。
* [ngx-lift](https://github.com/wghglory/ngx-lift) - “clr-lift”和“ngx-lift”通过实用程序、操作符和组件增强了 Angular，以简化开发。
* [firestitch](https://github.com/orgs/Firestitch/repositories) - [Firestitch](https://firestitch.com/) 提供了各种开源 Angular 解决方案。
* [@studiohyperdrive/ngx-tools](https://github.com/studiohyperdrive/hyperdrive-opensource) - 一个单一存储库，提供由 [Studio Hyperdrive](https://studiohyperdrive.be/) 团队创建和维护的多个基于 Angular 的包。
* [ngx-utility](https://github.com/OPI-PIB/ngx-utility) - 用于表单、区域、DOM 操作、HTTP 请求等的各种帮助器。
* [ssv.ngx](https://github.com/sketch7/ssv.ngx) - 来自 [sketch7](https://github.com/sketch7) 的 Mono-repo 库。 [ngx.command](https://github.com/sketch7/ssv.ngx/tree/master/libs/ngx.command#readme) 是 Angular 的命令模式实现。 [ngx.ux](https://github.com/sketch7/ssv.ngx/blob/master/libs/ngx.ux/README.md) 提供用于构建应用程序的 UX 基础知识和实用程序。
* [ng-kit](https://github.com/js-smart/ng-kit) - 使用 Angular Material 和 Bootstrap 5.x 构建的可重用 Angular 组件，用于日期、表单和字符串操作的实用程序类/函数。
* [nxt-components](https://github.com/Liquid-JS/nxt-components) - 各种 Angular 组件的集合。
* [ngx-signal-plus](https://github.com/milad-hub/ngx-signal-plus) - Angular Signals 的综合实用程序库，提供增强的功能、运算符和实用程序。
* [ngx-nuts-and-bolts](https://github.com/infinum/ngx-nuts-and-bolts) - [Infinum](https://infinum.com/) 使用的常用 Angular 相关代码片段的集合。
* [ngx-signals-plus](https://github.com/dszendrei/ngx-signals-plus) - 用于改善开发人员体验的附加信号。
* [ng-tool-collection](https://github.com/domideimel/ng-tool-collection) - 用 Angular 编写的有用工具。
* [yaagoub](https://yaagoub.org/) - 使用装饰器、指令、图标、服务和 OAuth 2.0 加速您的开发。
* [@everllence/ngx-tools](https://github.com/everllence/ngx-tools) - 该存储库包含一系列旨在提升您的 Angular 开发体验的库。
* [ngx-oneforall](https://github.com/love1024/ngx-oneforall) - 一个 Angular 库，包含可重用的管道、指令、服务、装饰器、常量、枚举等。
* [angular-signal-generators](https://github.com/DDtMM/angular-signal-generators) - Angular 信号生成器通过信号和实用程序简化开发，从而实现更快、更清晰的代码。
* [mmstack](https://github.com/mihajm/mmstack) - mmstack 库的 monorepo。
* [@shanieMoonlight/moonlight-repo](https://github.com/shanieMoonlight/moonlight-repo) - SpiderBaby 的开源 Angular 库、实用程序和演示应用程序的 Monorepo。
* [@jchpro/ng](https://github.com/jchpro/ng) - Angular 的各种库的 Monorepo。  访问[示例页面](https://ng.jchpro.pl/)了解更多信息。
* [rxap](https://gitlab.com/rxap/packages) - 一系列模块和工具，可减少 Web 和云应用程序的开发工作。
* [ng-util](https://github.com/ng-util/ng-util) - 一组 Angular 实用程序。
* [reactive-kit](https://github.com/max-scopp/reactive-kit) - 用于反应式 Angular 应用程序的轻量级实用程序，减少了样板文件并与“ngxtension”很好地配对。
* [fireng](https://github.com/BhanukaDev/fireng) - Angular 库的集合，用于使用信号简化响应式开发。
* [xprng](https://github.com/ziv/xprng) - Angular 的简单智能组件的微型包。
* [ngx-primeng-toolkit](https://github.com/saiful-70/ngx-primeng-toolkit) - 用于 Angular 状态管理的综合 TypeScript 实用程序，具有 PrimeNG 帮助程序、“ng-select”、存储和 NgRx 缓存。
* [@ibenvandeveire opensource](https://github.com/IbenTesara/opensource) - 托管多个包（包括 Angular 和非 Angular）的 monorepo，由 [Iben Van de Veire](https://github.com/IbenTesara) 开发和维护。
* [@farfadev/ngx-lib](https://github.com/farfadev/ngx-lib) - 来自 [Farfadev](https://github.com/farfadev) 的 Angular 库存储库，可在任何应用程序中使用。
* [ngx-security](https://github.com/xbranch/ngx-security) - 用于身份验证、角色和权限管理的模块化 Angular 库。
* [ng-catbee](https://github.com/catbee-technologies/ng-catbee) - 由 [Catbee](https://catbee.in/docs/@ng-catbee/) 团队开发和维护的 Angular 库集合。
* [ngx-persian](https://github.com/alihoseiny/ngx-persian) - 用于波斯语应用程序的全功能工具集。
* [acontplus-libs](https://github.com/acontplus/acontplus-libs) - Nx monorepo 包含 Angular 库，为企业应用程序提供领域驱动设计 (DDD) 架构、核心实用程序和 Angular Material UI 组件。
* [Angular Directive Workspace](https://github.com/sergeydus/ng-tailwind-workspace) - 一个 Angular monorepo，托管多个独立指令和实用程序库，包括 [ng-signals-utils](https://www.npmjs.com/package/@sergeydus/ng-signals-utils)。
* [angular-cool](https://github.com/Hacklone/angular-cool) - monorepo 包含开发人员友好的 Angular 实用程序，可通过轻松的 UI、存储、网络和性能功能增强应用程序。
* [dasch-ng](https://github.com/DaSchTour/dasch-ng) - 用于现代 Web 开发的可重用 Angular 库和 TypeScript 实用程序的集合。
* [ngx-schema-tools](https://github.com/Expeed-Software/ngx-schema-tools) - 包含用于 JSON 模式编辑、可视数据映射和动态表单渲染的 Angular 库的 monorepo。
* [angular-3d](https://github.com/Hive-Academy/angular-3d) - 现代 Angular 库，用于构建令人惊叹的 3D 图形和滚动动画。
* [npm-ntk-cms-angular](https://github.com/akaravi/npm-ntk-cms-angular) - 该 monorepo 包含 9 个可重用的 Angular 库的集合，专为构建现代 CMS 应用程序而设计。
* [ngx-vertex](https://github.com/pjlamb12/ngx-vertex) - 旨在帮助在 Angular 应用程序中创建和管理有向无环图模型。
* [telperion](https://github.com/telperiontech/telperion) - 用于现代 Web 开发的高质量、独立于框架的实用程序和工具的集合，包括 [ng-pack](https://github.com/telperiontech/telperion/tree/main/libs/ng-pack)。
* [signality](https://github.com/signalityjs/signality) - 用于在 Angular 中构建反应性组合的原子实用程序的集合。
* [@alvaromarinho/libs](https://github.com/alvaromarinho/libs) - 满足常见 UI 需求的 Angular 库集合，与 Angular 14+ 兼容。
* [angular-helpers](https://github.com/Gaspar1992/angular-helpers) - 一套 Angular 库，可帮助您构建安全的、浏览器集成的应用程序，并提供干净的开发人员体验。
* [ngneat-archive](https://github.com/ngneat-archive) - [ngneat](https://github.com/ngneat) 存储库的只读保存存档。

### 莫代尔

* [ngx-dialog](https://github.com/soc221b/ngx-dialog) - 适用于 Angular 16+ 的类型安全 Angular 对话框指令。
* [ng-modal-service](https://github.com/nhusby/ng-modal-service) - 一个简单的 Angular 模态服务。
* [strictly-typed-mat-dialog](https://github.com/JustSolve-self-serve/strictly-typed-mat-dialog) - 角度材质库可提高垫对话框的类型安全性。
* [angular-confirmation-capture](https://github.com/lazycuh/angular-confirmation-capture) - 一个单例的全局 Angular 服务，以编程方式显示确认框以获取用户的同意。
* [angular-anchored-floating-box](https://github.com/lazycuh/angular-anchored-floating-box) - Singleton Angular 服务，用于渲染锚定到具有“TemplateRef”或组件内容的元素的浮动框。
* [ngx-side-page](https://github.com/strikerh/ngx-side-page) - 多功能 Angular 库，用于滑出式侧面板，具有平滑的、基于服务的动画，例如侧页的材质对话框。
* [async-modal-ngx](https://github.com/antonioconselheiro/async-modal-ngx) - 该库使用灵活的数据流呈现 Angular 组件，而所有样式和模式宿主设计仍然由您负责。
* [rnd-dialog](https://github.com/acrodata/rnd-dialog) - 基于 CDK 对话框的可调整大小和可拖动的对话框。
* [prettier-modals](https://github.com/antuuanyf/prettier-modals) - Angular 指令和 Prettier Modals 的可注入服务 - 由 GSAP Flip 提供支持的原生“<dialog>”元素的精美打开/关闭动画。

### 通知

* [alert-bar-library](https://github.com/npm-lahsiv/alert-bar-library) - 使用干净、可访问的样式显示上下文消息（成功、信息、警告、错误），这些样式与现代 Web 应用程序与此库相匹配。
* [angular-bootstrap-toast-service](https://github.com/svierk/angular-bootstrap-toast-service) - 用于发送基于 Bootstrap 的 toast 通知（包括 Vercel 部署）的 Angular 项目。
* [angular-notification](https://github.com/lazycuh/angular-notification) - 一个单例的全局 Angular 服务，用于以编程方式显示通知。
* [angular-toaster](https://github.com/damingerdai/angular-toaster) - 更新了 [Angular2-Toaster](https://github.com/Stabzs/Angular2-Toaster) 的分支。
* [grand-notifications](https://github.com/rishi-rj-s/grand-notifications) - 带有艺术动画的漂亮、可定制的 Toast 通知。
* [hot-toast](https://github.com/ngxpert/hot-toast) - Angular 的冒烟热吐司通知。
* [makki-toast-package](https://github.com/DanielJimenezC/makki-toast-package) - 一个可定制的 Toast 组件，旨在简化定制警报的创建和管理。
* [mk-magic-messages-library](https://github.com/mkeller1992/mk-magic-messages-library) - 在 Angular 20+ 应用程序中轻松显示动画成功、信息、警告和错误警报。
* [ngx-advanced-toast](https://github.com/Hamed-kshiem/ngx-advanced-toast) - 基于原生 `<dialog>` 元素构建的高级 Angular toast 通知 — 信号优先、零 RxJS、纯 CSS 动画、完全可访问。
* [ngx-alertifying](https://github.com/Salromag/ngx-alertifying) - 可定制、响应灵敏的 Angular 警报组件可跨设备和环境提供时尚、可访问的反馈。
* [ngx-french-toast](https://github.com/thiagopg84/ngx-french-toast) - 轻量级、可定制的 Angular 14+ toast 库，提供信息性消息、反馈和动态组件支持。
* [ngx-modern-alerts](https://github.com/jonaaix/ngx-modern-alerts) - 灵活的 Angular 系统，用于横幅和浮动警报，具有集线器、超时、自定义操作等。
* [@klausbrandner/ngx-notifications](https://github.com/klausbrandner/ngx-notifications) - 适用于 Angular 的简单、轻量级的 Toast 通知。
* [@pascaliske/ngx-notifications](https://github.com/pascaliske/ngx-notifications) - Angular 的简单通知模块。
* [ngx-notifier](https://github.com/sibiraj-s/ngx-notifier) - 用于 Angular 应用程序的简单通知服务。
* [ngx-popify](https://github.com/fgilmet/ngx-popify) - Angular 16+ 的 Toast 通知使用反应信号构建，并通过视图组件轻松集成。
* [ngx-signal-toast](https://github.com/white-devil1/ngx-signal-toast-workspace) - 适用于 Angular 21+ 的信号优先 Toast 通知库，具有无区域支持、零依赖性、SSR 安全性和强大的主题。
* [ngx-snotifire](https://github.com/ccpatrut/ngx-snotifire) - 灵活的 Toast 库，提供多种通知类型、同步位置、丰富的配置、完全自定义样式、内置主题、回调和自定义 HTML 支持。
* [ngx-sonner](https://github.com/tutkli/ngx-sonner) - Angular 的固执己见的 Toast 组件。 @emilkowalski 儿子的端口。
* [ngx-sweetalert2](https://github.com/sweetalert2/ngx-sweetalert2) - 用于 Angular 的声明式、反应式和模板驱动的 SweetAlert2 集成。
* [ngx-toast](https://github.com/aminekun90/ngx-toast) - 适用于 Angular 21+ 和 React 18+ 的轻量级、高性能、Zoneless-ready toast 通知库。
* [@IQXLimited/ngx-toastr](https://github.com/IQXLimited/ngx-toastr) - “ngx-toastr”的一个分支，添加了额外的功能、改进和自定义。
* [ngx-toastr-notifier](https://github.com/Mazen-Embaby/ngx-toastr-notifier) - 轻量级、可定制的 Angular 20 多个 Toast 通知，采用 Material Design 和灵活的 API，取代了“toastr”。
* [notifyx](https://github.com/awalhadi/notifyx) - 一个简单的、可定制的 JavaScript/TypeScript 零依赖 toast 库。
* [OneSignal](https://documentation.onesignal.com/docs/angular-setup) - 使用 [onesignal-ngx](https://github.com/OneSignal/onesignal-ngx) 将 OneSignal 集成到 Angular 应用中，以进行推送和应用内消息传递。
* [toastify](https://github.com/andreasnicolaou/toastify) - 适用于 Web 应用程序的轻量级且可自定义的 Toast 通知。
* [web-notifier](https://github.com/andreasnicolaou/web-notifier) - 轻量级、灵活的 Web 通知库，具有用于浏览器通知的简单的基于 RxJS 的 API。
* [ngx-dynamic-toast](https://github.com/ederjavs/ngx-dynamic-toast) - 一个优雅、流畅的 Angular Toast 通知库，深受美丽的 [Sileo](https://github.com/hiaaryan/sileo) 项目的启发。
* [flexi-toast](https://github.com/FlexiUI-labs/flexi-toast) - Angular Toast 通知组件，具有标题、消息、图标类型、自动关闭、手动关闭、动画、主题和定位支持。
* [ngx-notitia](https://github.com/klajdm/ngx-notitia) - 更新了“ngx-toastr”的分支，为 Angular 21+ 提供了附加功能、修复和现代化。
* [ngx-herald](https://github.com/HoplaGeiss/ngx-herald) - 一个轻量级、现代的 Angular toast 通知库。信号优先、无区域兼容、零运行时依赖性以及易于使用的 ngx-toastr 替代品。

### 入职和产品参观

* [angular-shepherd](https://github.com/shepherd-pro/angular-shepherd) - Angular Service 封装了站点浏览库 [Shepherd](https://github.com/shepherd-pro/shepherd)。
* [skyux](https://github.com/blackbaud/skyux) - 适用于 Angular 的 SKY UX 组件。
* [ngx-ui-tour](https://github.com/hakimio/ngx-ui-tour) - 受 [angular-ui-tour](https://github.com/benmarch/angular-ui-tour) 启发的 UI 游览库。
* [ngx-onboarding](https://github.com/rosen-group/ngx-onboarding) - 用于无缝 Angular 教程的入门库，帮助用户快速学习和导航您的应用程序。
* [ngx-web-tour](https://github.com/abbas-mgz/ngx-web-tour) - 适用于 Angular 应用程序的可定制产品浏览库，支持通过动画和专业 UI 进行用户引导。
* [ngx-intro](https://github.com/andresciceri/ngx-intro) - 一个 Angular 库，提供 [Intro.js](https://introjs.com/) 的简单集成，以创建交互式指南和分步教程。
* [ngx-custom-tour](https://github.com/miraxes/ngx-custom-tour) - 轻松自定义 Angular 15+ 的分步教程/入门。
* [ng-beacon](https://github.com/HomelessCoder/ng-beacon) - 适用于 Angular 19+ 的轻量级导游库，具有信号和无区域兼容渲染。
* [ngx-guided-tour-lite](https://github.com/pantarey-io/ngx-guided-tour-lite) - 一个轻量级、无依赖的 Angular 导游库。

### PDF

* [Angular Image & PDF Viewer](https://github.com/NiranjanKushwaha/imgPdfViewer_library_Angular) - 一个可自定义的库，用于使用 Mozilla 的 [pdf.js](https://github.com/mozilla/pdf.js) 引擎查看 PDF 和图像，以实现流畅的预览。
* [ng-pdf-renderer](https://github.com/askinjohn/ng-pdf-renderer) - 适用于 Angular 应用程序的现代零配置 PDF 查看器，具有智能自动调整、文本选择和响应式设计。
* [ng2-pdfjs-viewer](https://github.com/intbot/ng2-pdfjs-viewer) - PDFJS 和 ViewerJS 的 Angular 组件（支持所有版本的 Angular）。
* [ngx-document-signer](https://github.com/YaseenAlMufti/ngx-document-signer) - 一个可重复使用的包，提供 PDF 表单创建者和 PDF 签名者。
* [ngx-extended-pdf-viewer](https://github.com/stephanrauh/ngx-extended-pdf-viewer) - 适用于 Angular 16+ 的成熟 PDF 查看器。
* [ngx-pdf-viewer](https://github.com/subedigaurav/ngx-pdf-viewer) - 用于 Angular 应用程序的轻量级 PDF 查看器库。
* [pdf-viewer-kit](https://github.com/AmanKrr/pdf-viewer-kit) - 一个现代的、高性能的、与框架无关的、轻量级的 PDF 查看器和注释库，构建在“pdf.js”之上。

### 管道

* [ng-generic-pipe](https://github.com/nigrosimone/ng-generic-pipe) - 用于角度应用的通用管道。
* [ng-dompurify](https://github.com/taiga-family/ng-dompurify) - 使用 [DOMPurify](https://github.com/cure53/DOMPurify) 的 Angular Sanitizer/Pipe 具有完整的配置支持。
* [ngx-signal-pipes](https://github.com/wassim-k/ngx-signal-pipes) - 使用功能管道转换 Angular 信号。
* [ngx-pipe-lib](https://github.com/mofirojean/ngx-pipe-lib) - 适用于日常任务的常见 Angular 管道示例。
* [memoize-pipe](https://github.com/ngx-rock/memoize-pipe) - 用于记忆 Angular 模板中的计算的通用管道。
* [ngx-highlight-text](https://github.com/ultrasonicsoft/ngx-highlight-text) - 突出显示 HTML 标记中选定单词的角度管道。
* [ngx-smart-pipes](https://github.com/Kavshree/-bjkavyashree-ngx-smart-pipes) - 一个轻量级的、可摇树摇动的独立 Angular 管道集合，专为现实世界的用例而设计。
* [ngx-dynamic-search](https://github.com/mustafaer/ngx-dynamic-search) - 角度管道设计用于跨复杂嵌套对象和数组进行动态、深度搜索过滤。
* [ngx-name-capitalize](https://github.com/gabo2151/ngx-name-capitalize) - 用于名称大写的角管道，用于格式化复合姓氏、语言助词、连字符名称、撇号和 Unicode 字符。
* [ngx-transforms](https://github.com/mofirojean/ngx-transforms) - 90 多个独立的、tree-shakable 管道，用于字符串、数字、日期、数组、对象等。

### 印刷

* [ngx-pos-print](https://github.com/gmetenou7/NGX-POS-PRINT) - 从 Angular 应用程序在 POS 热敏打印机上打印收据。
* [ngx-print](https://github.com/selemxmn/ngx-print) - 一个即插即用的 Angulae 库来打印您的东西。
* [ngx-printer-demo](https://github.com/plaetzchen79/ngx-printer-demo) - 一个简单的 Angular 服务，用于打印窗口、窗口的一部分 (div)、图像、HTMLElements 或 Angular 对象。

### 二维码

* [ng-qrcode](https://github.com/mnahkies/ng-qrcode) - 易于使用的 AOT 兼容 QR 代码生成器，适用于 Angular 项目。
* [angularx-qrcode](https://github.com/cordobo/angularx-qrcode) - 快速且易于使用的 Ivy 兼容 Ionic 和 Angular QR 代码生成器库。
* [dfts-qrcode](https://github.com/Dafnik/dfts-common/tree/main/libs/dfts-qrcode) - 一个小型且易于使用的 JavaScript / TypeScript QR 代码生成器库。完全类型安全且兼容 ES 模块。
* [ngx-scanner](https://github.com/zxing-js/ngx-scanner) - Angular QR 码、条形码、DataMatrix、使用 ZXing 的扫描仪组件。
* [ng-qrcode-svg](https://github.com/larscom/ng-qrcode-svg) - 适用于 Angular 的简单 QR 代码生成器（仅限 SVG）。
* [Angular-html5qrcode](https://github.com/mohamedfakhreldin/Angular-html5qrcode) - 该库为 [html5-qrcode](https://github.com/mebjas/html5-qrcode) 库提供了 Angular 包装器，使开发人员可以轻松地将 QR 码和条形码扫描功能集成到他们的应用程序中。
* [ngx-kjua](https://github.com/werthdavid/ngx-kjua) - 使用 [kjua](https://github.com/lrsjng/kjua) 的 Angular QR 代码生成器组件。
* [ngx-qrcode](https://github.com/GNURub/ngx-qrcode) - 一个简单的 Angular 18+ 组件，用于生成 QR 码。基于 [react-native-qrcode-skia](https://github.com/enzomanuelmangano/react-native-qrcode-skia) 库。
* [qrcode-angular](https://github.com/selfxyz/self/tree/main/sdk/qrcode-angular) - 一个简化的 Angular 库，可为 [Self.xyz](https://self.xyz/) 创建验证二维码。
* [qr-code-layout-generate-tool](https://github.com/shashi089/qr-code-layout-generate-tool) - 适用于 React、Angular、Vue、Svelte 和 Node.js 的与框架无关的 QR 代码标签和徽章设计器。

### 路由器

* [ngx-route-breadcrumbs](https://github.com/alevettih/ngx-route-breadcrumbs) - Angular 库，可简化基于路由 URL 和参数创建面包屑的过程。
* [xng-breadcrumb](https://github.com/udayvunnam/xng-breadcrumb) - 适用于 Angular 6+ 的零配置、轻量级、可配置、反应式面包屑。
* [angular-router-menus](https://github.com/muuvmuuv/angular-router-menus) - 类型化、可定制的基于 Angular 路线的菜单，具有多重导航、嵌套下拉菜单和注入令牌访问。
* [ngx-back-button](https://github.com/rbalet/ngx-back-button) - 用于处理适当的 Angular 后退按钮功能的库。
* [ngx-foresight](https://github.com/akshykhade/ngx-foresight) - [ForesightJS](https://foresightjs.com/) 的 Angular 集成，用于根据用户意图进行智能路由器预加载。
* [ngx-href](https://github.com/rbalet/ngx-href) - 该指令允许 href 理解 Angular 的路由器，同时保留其默认功能。
* [ngx-multi-level-push-menu](https://github.com/ramiz4/ngx-multi-level-push-menu) - 一个现代、可访问的 Angular 组件，用于响应式多级推送菜单，具有广泛的自定义选项。
* [ngx-quicklink](https://github.com/mgechev/ngx-quicklink) - Angular 路由器的 Quicklink 预取策略。
* [ngx-route-manager](https://github.com/perez247/ngx-route-manager) - 一个简单的库，用于存储应用程序中使用的所有路由 URL。
* [ngx-speculation-rules](https://github.com/SkyZeroZx/ngx-speculation-rules) - [推测规则 API](https://developer.mozilla.org/en-US/docs/Web/API/Speculation_Rules_API) 的 Angular 库支持预取和预渲染，以实现更快、SSR 和 Zoneless 兼容的导航。
* [ui-router](https://github.com/ui-router/angular) - Angular 中基于状态的路由是通过 [Angular 的 UI-Router](https://ui-router.github.io) 启用的。
* [ngx-url-params](https://github.com/shlomog12/ngx-url-params) - 轻量级 Angular 服务，用于通过简洁的反应式 API 管理和同步 URL 查询参数。
* [ngx-history](https://github.com/lumentut/ngx-history) - 现代 Angular 导航历史服务，具有反应式编程支持。

### 滚动

* [ngx-ui-scroll](https://github.com/dhilt/ngx-ui-scroll) - Angular 的虚拟/无限滚动。
* [ngx-page-scroll](https://github.com/Nolanus/ngx-page-scroll) - 用纯 TypeScript 编写的 Angular 动画滚动功能。
* [lithium-ngx-virtual-scroll](https://github.com/lVlyke/lithium-ngx-virtual-scroll) - Angular 的快速、轻量级虚拟滚动解决方案，支持单列列表、网格列表和视图缓存。
* [angular-fullpage](https://github.com/alvarotrigo/angular-fullpage) - fullPage.js 的官方组件，全屏滚动库。
* [ngx-scrolltop](https://github.com/bartholomej/ngx-scrolltop) - 轻量级、受材料设计启发的按钮，用于滚动到页面顶部。没有依赖性。
* [OverlayScrollbars](https://github.com/KingSora/OverlayScrollbars) - 用于自定义样式的覆盖滚动条的 JavaScript 插件，可隐藏本机，同时保留功能。
* [ngx-scrollbar](https://github.com/MurhafSousli/ngx-scrollbar) - 具有本机滚动机制的自定义覆盖滚动条。
* [ngx-tracing-beam](https://github.com/omnedia/ngx-tracing-beam) - 一个简单的组件库，可将动画跟踪光束添加到垂直滚动中。
* [ngx-marquee](https://github.com/omnedia/ngx-marquee) - 一个简单的组件库，可使用您的内容创建无限滚动选取框。
* [@omnedia/ngx-scrollbar](https://github.com/omnedia/ngx-scrollbar) - 具有平滑滚动和完整样式控制的自定义滚动条。
* [ngx-virtual-dnd-list](https://github.com/mfuu/ngx-virtual-dnd-list) - 一个可以通过拖动排序的虚拟滚动列表组件。
* [ngx-scroll-top](https://github.com/ProAngular/ngx-scroll-top) - 适用于 Angular 项目的可配置、轻量级返回顶部按钮。
* [ng-mat-select-infinite-scroll](https://github.com/HaidarZ/ng-mat-select-infinite-scroll) - 用于角度材质选择组件的无限滚动指令。
* [simplebar](https://github.com/Grsmto/simplebar) - 自定义滚动条原生 JavaScript 库，具有原生滚动功能，简单、轻量级、易于使用且跨浏览器。
* [ngx-responsive-virtual-scroll](https://github.com/dcbeck/ngx-responsive-virtual-scroll) - 用于单列列表、响应式网格和视图缓存的快速、轻量级 Angular 虚拟滚动。
* [ngx-virtual-scroller-flexible](https://github.com/onexip/ngx-virtual-scroller-flexible) - 超快速、灵活的虚拟滚动条可无缝渲染具有不同高度的无限项目。
* [ngx-perfect-scrollbar-portable](https://github.com/brakmic/ngx-perfect-scrollbar-portable) - 完美滚动条的角度包装库。
* [ng-virtual-list](https://github.com/djonnyx/ng-virtual-list) - 超大列表的最佳性能。
* [ngx-horizontal-menu-scroll](https://github.com/isahohieku/ngx-horizontal-menu-scroll) - 一个轻量级、可定制的 Angular 库，用于创建具有流畅导航控件的漂亮水平滚动菜单。
* [usal](https://github.com/italoalmeida0/usal) - 与框架无关的终极滚动动画库。
* [ar-virtual-scroll](https://github.com/artomenwork/ar-virtual-scroll) - 具有自动动态高度的轻量级 Angular 虚拟滚动，非常适合聊天、提要和变量列表。
* [angular-infinity-scroller](https://github.com/Jayant061/angular-infinity-scroller) - 轻量级、高性能的无限滚动指令，旨在与现代 Angular 和 SSR 设置无缝协作。
* [cerious-scroll](https://github.com/ceriousdevtech/cerious-scroll) - Web 应用程序的高性能虚拟滚动。
* [ngx-zoneless-scrollbar](https://github.com/Legalfina/ngx-zoneless-scrollbar) - 专为无区域模式构建的轻量级 Angular 滚动条，使用带有 CSS 样式的本机滚动。
* [ngx-scrollbar-ultimate](https://github.com/andrew-dev283/ngx-scrollbar-ultimate) - 用于垂直滚动的轻量级库。
* [ngx-scrollspy](https://github.com/uniprank/ngx-scrollspy) - 带有事件的 Angular Scroll Spy 服务。
* [ngx-virtual-grid](https://github.com/theryansmee/ngx-virtual-grid) - 响应式虚拟滚动 Angular 网格，支持无限加载，使用 CSS 网格，自动测量项目大小，并仅渲染可见元素。

### 存储

* [rxdb](https://rxdb.info/) - [IndexedDB](https://rxdb.info/articles/angular-indexeddb.html) 的抽象层。
* [ngx-reactive-storage](https://github.com/e-oz/ngx-reactive-storage) - IndexedDB/localStorage 的包装器，具有基于承诺的 API，支持 Angular Signals 和 RxJS Observables。
* [ng2-webstorage](https://github.com/PillowPillow/ng2-webstorage) - LocalStorage 和 SessionStorage 管理器。
* [ngx-indexed-db](https://github.com/assuncaocharles/ngx-indexed-db) - 将 IndexedDB 包装在 Angular 服务中。
* [angular-async-local-storage](https://github.com/cyrilletuzi/angular-async-local-storage) - Angular 的高效客户端存储：简单的 API + 性能 + Observables + 验证。
* [signaldb](https://github.com/maxnowack/signaldb) - 本地 JavaScript DB 具有类似 MongoDB 的界面、TypeScript、基于信号的反应性、无模式设计和快速查询。
* [dexie](https://github.com/dexie/Dexie.js) - IndexedDB 的简约包装器。
* [angular-web-storage](https://github.com/cipchk/angular-web-storage) - 用于保存和恢复 HTML5 本地和会话存储的 Angular 装饰器。
* [ng-storage](https://github.com/edisonaugusthy/ng-storage) - 一种现代的反应式 Angular 服务，用于浏览器存储管理，具有 AES-GCM 加密、TTL、更改通知和 Apollo 风格的提供程序。
* [convex-angular](https://github.com/azhukau-dev/convex-angular) - Convex 的 Angular 客户端。
* [secure-client-store](https://github.com/msaadart/secure-client-store) - 用于 AES-256-GCM 客户端加密的通用 TypeScript 库（适用于浏览器和 Node.js）。
* [ngx-persist](https://github.com/khvedela/ngx-persist) - 用于 Angular 的类型安全、基于信号的持久状态实用程序，与 localStorage、sessionStorage、IndexedDB 或自定义后端同步。
* [ngx-webstore](https://github.com/saurabh-vaish/ngx-webstore) - 用于浏览器存储管理的综合 Angular 库，具有 TypeScript 支持、反应式 API、加密、TTL 等。
* [@moltendb-web/angular](https://github.com/maximilian27/moltendb-web) - Rust/WebAssembly 本地优先的 Angular 数据库，带有信号、OPFS、GraphQL 式查询和 Web Workers。
* [ngx-secure-storage](https://github.com/MadeByRaymond/ngx-secure-storage) - 与 SSR 兼容的 Angular 服务，使用 AES 加密安全地存储、检索和管理 localStorage 和 sessionStorage 中的加密数据。

### 工具提示

* [popover](https://github.com/ncstate-sat/popover) - 角度弹出组件。
* [ngx-tooltip-directives](https://github.com/mkeller1992/ngx-tooltip-directives) - 具有三个工具提示指令（字符串、HTML、模板）的库，灵感来自 [ng2-tooltip-directive](https://github.com/drozhzhin-n-e/ng2-tooltip-directive)。
* [angular-tooltip](https://github.com/babybeet/angular-tooltip) - 在 Angular 中以编程方式和/或声明方式轻松显示工具提示。
* [ngx-tippy-wrapper](https://github.com/farengeyt451/ngx-tippy-wrapper) - [Tippy.js](https://github.com/atomiks/tippyjs) 的角度包装器。
* [angular-tooltip](https://github.com/lazycuh/angular-tooltip) - 在 Angular 中以编程方式和/或声明方式轻松显示工具提示。
* [ngx-overlay](https://github.com/bastienmoulia/ngx-overlay) - 用于现代 CSS/HTML 叠加层（模式、工具提示和弹出窗口）的轻量级 Angular 库，与浏览器兼容且优雅。
* [ngx-smart-tooltip](https://github.com/techasif/ngx-smart-tooltip) - Angular 18 的轻量级、可定制的工具提示库，使用信号、Web 动画 API 和 OnPush 更改检测。

### 用户界面库

* [Dev Extreme](https://js.devexpress.com/Overview/Angular/) - 功能齐全的 65+ Angular 组件套件。
* [Zyra UI](https://zyraui.dev/) - 现代 Angular 组件库，具有设计令牌、信号、暗模式优先主题和 WCAG 2.1 AA 可访问性。
* [Syncfusion](https://www.syncfusion.com/angular-components) - 其 [Angular 的基本 UI 套件](https://github.com/syncfusion/essential-ui-kit-for-angular) 与 Tailwind CSS 和 Bootstrap 兼容。
* [ej2-angular-ui-components](https://github.com/syncfusion/ej2-angular-ui-components) - Syncfusion Angular UI 库包含 70 多个轻量级、响应式、模块化、触摸友好的组件。
* [Nebular](https://github.com/akveo/nebular) - 基于 Eva 设计系统的可定制 Angular UI 库。
* [NG-ZORRO](https://github.com/NG-ZORRO/ng-zorro-antd) - 基于Ant Design和Angular的企业级UI组件。
* [NG-ALAIN](https://github.com/ng-alain/ng-alain/) - NG-ZORRO 管理面板前端框架。
* [zardui](https://github.com/zard-ui/zardui) - 基于 [shadcn-ui](https://github.com/shadcn-ui/ui) 和 NG‑ZORRO 的漂亮、易于访问的 Angular 组件集合，完全开源且免费。
* [ngx-ui](https://github.com/swimlane/ngx-ui) - 适用于 Angular2 及更高版本的样式和组件库！
* [prime-ng](https://github.com/primefaces/primeng) - 最完整的 Angular UI 组件库。
* [Wijmo 5](http://wijmo.com/products/wijmo-5/) - Angular2 的 UI 组件集。
* [Taiga UI](https://taiga-ui.dev/) - 强大的 Angular 开源组件集！
* [AgnosUI](https://amadeusitgroup.github.io/AgnosUI/latest/) - 高度可配置的无头框架无关组件库。
* [ng-aquila](https://github.com/allianz/ng-aquila) - Aquila 是一个开源 Allianz GDF 组件库，在此作为白标变体提供。
* [oblique](https://github.com/oblique-bit/oblique) - 采用瑞士企业设计的 Angular 框架和适用于品牌业务应用程序的即用型组件。
* [fundamental-ngx](https://github.com/SAP/fundamental-ngx) - Angular 的基础库是 SAP Design System Angular 组件库。
* [designsystem](https://github.com/kirbydesign/designsystem) - Kirby Design System 是一个实现 Kirby 设计理念的 UX 组件库。
* [sbb-angular](https://github.com/sbb-design-systems/sbb-angular) - SBB 的 Angular 库。
* [ui](https://github.com/alauda/ui) - 来自 Alauda 前端团队的企业级 Angular UI 框架。
* [ngx-tethys](https://github.com/atinc/ngx-tethys) - 适用于 Angular 的快速可靠的 Tethys Design 组件。
* [antwerp-ui_angular](https://github.com/digipolisantwerp/antwerp-ui_angular) - Antwerp UI 是一个组件界面库，用于构建用户界面和响应式 Web 应用程序。
* [ng-clarity](https://github.com/vmware-clarity/ng-clarity) - Clarity Angular 是一个专为 Angular 构建的可扩展、可访问、可定制的开源设计系统。
* [ngx-float-ui](https://github.com/tonysamperi/ngx-float-ui) - [Floating UI](https://floating-ui.com/) 库的 Angular 包装器。
* [carbon-components-angular](https://github.com/carbon-design-system/carbon-components-angular) - IBM Carbon 设计系统的 Angular 实现。
* [dyte-io/ui-kit](https://github.com/dyte-io/ui-kit/tree/staging/packages/angular-library) - Dyte UI Kit：预构建组件，用于将视频和语音通话快速集成到任何应用程序或网站中。
* [ng-zen](https://github.com/kstepien3/ng-zen) - 在项目中无缝创建可定制、可用于生产的 Angular UI 组件。
* [ngwr](https://github.com/thekhegay/ngwr) - Angular UI 套件可用于制作时尚的 Angular 应用程序。
* [Windmillcode-Angular-CDK](https://github.com/WindMillCode/Windmillcode-Angular-CDK) - 提供一系列可重用的 UI 组件，每个组件都经过精心设计，注重细节和性能。
* [ng-vcl](https://github.com/vcl/ng-vcl) - 基于VCL CSS生态系统的Angular组件库。
* [ngx-ui](https://ngxui.com/docs) - 来自 [OMnedia](https://github.com/omnedia) 的 NGXUI：独立的 Angular 组件、块以及用于登陆页面和营销材料的模板。
* [po-angular](https://github.com/po-ui/po-angular) - 基于Angular的组件库。葡萄牙语文档。
* [ngx-nighthawk](https://github.com/evenuxjs/ngx-nighthawk) - 使用 Bootstrap 开发的生产就绪型企业级项目，提供广泛的自定义功能。
* [@ng-verse/ui](https://github.com/ngverse/ui) - 您可以复制/粘贴的生产就绪角度组件。
* [bryntum](https://bryntum.com/) - 用于日历、甘特图、看板和日程安排的世界级 Web 组件。
* [flexi-ui](https://github.com/TanerSaydam/flexi-ui) - [Flexi UI](https://flexi-ui.ecnorow.com/)：可重用、可定制、开源 UI 组件，适用于现代、具有视觉吸引力的前端应用程序。
* [@koobiq/angular-components](https://github.com/koobiq/angular-components) - 适用于以安全为中心的产品的开源设计系统，提供 UI 模式、组件、工具、资源和指南。
* [Vega](https://vega.hlprd.com/) - 通过利用根据您的首选框架定制的可重用组件和样式来加快功能开发。
* [Blueprint UI](https://blueprintui.dev/) - 使用随处可用的灵活 UI 组件和工具加速您的开发。
* [mantic-ui](https://github.com/KY-Programming/mantic-ui) - [Semantic UI](https://semantic-ui.com/) 和 [Semantic UI](https://fomantic-ui.com/) 的 Angular 组件。
* [kage-ui](https://github.com/sanjib-kumar-mandal/kage-ui) - 轻量级、灵活的 Angular 库，具有可重复使用的组件，其灵感源自边界优先设计系统，可实现可扩展、一致的 UI。
* [quix-quang](https://github.com/quix-it/quix-quang) - 由 [Quix Srl](https://www.quixconsulting.com/) 开发的 Angular 组件和实用程序库。
* [ngx-vflow](https://github.com/artem-mangilev/ngx-vflow) - 一个开源库，用于使用 Angular 构建基于节点的 UI。
* [ship-ui](https://github.com/shipuicom/core) - 适用于 Angular 的现代、基于信号、无区域兼容的 UI 库。在其[官方网站](https://www.shipui.com) 上探索其功能和文档。
* [slateui](https://github.com/angularcafe/slateui) - 一个现代、可访问的 UI 组件库，提供使用 Angular 原语、Tailwind CSS 和信号构建的基于指令的组件。
* [@nexcraft/forge](https://github.com/dev-ignis/forge) - 与框架无关的 Web 组件 UI 库。通过自定义元素在 Angular 中工作。
* [ngx-nova-ui](https://github.com/lebocow/ngx-nova-ui) - 现代 Angular 20 UI 组件库，使用信号、独立组件和 CSS 优先的主题方法构建。
* [MaxterDev NGX Components](https://github.com/MatoMakuch/maxterdev/tree/main/projects/ngx-components) - 高度灵活且可通过 SCSS 定制的 Angular 组件库。
* [gcds-components](https://github.com/cds-snc/gcds-components/tree/main/packages/angular) - `gcds-components-angular` 包可以轻松地将 [GC 设计系统](https://design-system.alpha.canada.ca/) Web 组件集成到 Angular 中。
* [particle-ng](https://github.com/entake-org/particle-ng) - 一个轻量级、可主题化的组件库，为 Angular Material 和 PrimeNG 提供灵活、高控制的替代方案。
* [ngx-kit-ui](https://github.com/OpenKit-Labs/ngx-kit-ui) - 适用于移动和 Web 的现代 Angular UI 库。
* [TecnualNG](https://github.com/tecnual/tecnualng) - 现代 Angular UI 库，提供可重用、可定制且可访问的组件，用于构建专业的 Web 应用程序。
* [takeoff-ui](https://github.com/turkishtechnology/takeoff-ui) - 一个全面的设计系统，提供使用 Stencil.js 开发的与框架无关的 Web 组件。
* [mozek](https://github.com/thecodemeor/mozek-package) - 轻量级 SCSS 工具包和 UI 库，专为干净、简单、非过度设计的样式而设计，具有一致的间距、颜色和版式。
* [Magma](https://github.com/ikilote/Magma) - 支持其生态系统并可供任何人使用或扩展的广泛组件、服务、管道、指令和实用程序。
* [ngx-aespartal-ui](https://github.com/Aespartal/ngx-aespartal-ui) - 一个专业、轻量级、可定制的 Angular 组件库，采用原子设计原则构建。
* [JSuites](https://github.com/jsuites/jsuites) - UI 组件和实用程序（表单、模态、输入）的集合，可以使用自定义包装器或指令集成到 Angular 中。
* [ngx-support-chat](https://github.com/avs2001/ngx-support-chat) - 用于客户支持聊天界面的纯演示性 Angular 组件库。
* [luma-ui](https://github.com/lumaui/luma-ui) - 适用于 Angular 应用程序的 Neo-Minimal 设计系统。
* [Mundane UI](https://github.com/waga97/Mundane-UI) - 与框架无关、零依赖、轻量级 UI 组件库。
* [eagami-design-system](https://github.com/mwiraszka/eagami-design-system) - 基于 CSS 自定义属性构建的轻量级、可访问的 Angular UI 组件库。
* [angular-liquid-glass](https://github.com/thiagopac/angular-liquid-glass) - 用于液态玻璃和玻璃形态界面的独立 Angular 组件库。
* [ngx-pk-ui](https://github.com/superpck/ngx-pk-ui) - Angular 21 组件库提供 UI 组件和 CSS 实用程序。
* [magary](https://github.com/JhoanGon/magary) - 一个现代的、独立的第一 Angular UI 库 monorepo。
* [ngx-core-components](https://github.com/prajaktadube/ngx-core-components) - Angular 19+ 组件库 — 使用信号、OnPush 更改检测和零运行时依赖性构建的生产就绪 UI 组件。
* [ngx-cupertino](https://github.com/gacc94/ngx-cupertino) - Angular 组件实现了 Apple 的 iOS 26 / macOS Tahoe 26 设计系统。

### 基于 Bootstrap 构建的 UI 库

* [angular-bootstrap-md](https://mdbootstrap.com/docs/angular/) - Bootstrap 5 和 Angular 17 的材料设计。
* [ng-bootstrap](https://ng-bootstrap.github.io) - 使用 Bootstrap5 CSS 和专为 Angular 生态系统定制的 API 构建的 Angular 小部件。
* [ng-bootstrap-addons](https://github.com/mikaelbotassi/ng-bootstrap-addons) - 添加 `ng-bootstrap` 中不可用的 UI 组件（例如，输入/表单控件）。
* [ngx-bootstrap](https://github.com/valor-software/ngx-bootstrap) - Angular 中快速可靠的 Bootstrap 小部件（支持 Ivy 引擎）。
* [design-angular-kit](https://github.com/italia/design-angular-kit) - 基于 Bootstrap Italia 的工具包
用于创建使用 Angular 开发的 Web 应用程序。
* [yoozsoft](https://www.yoozsoft.com/ys-ng/home) - 使用 Bootstrap 5、CSS 和 NG Bootstrap 17 构建的小部件以及专为 Angular 生态系统设计的 API。
* [ngx-gccb](https://www.npmjs.com/package/ngx-gccb) - Angular19+ 库具有易于使用的共享组件、指令、管道和服务。请参阅 [showcase](https://ngx-gccb.netlify.app/) 了解代码片段。
* [cute-widgets](https://github.com/cute-widgets/base) - 一个开源 Angular UI 库，提供使用 Bootstrap 5+ 实用程序和设计类设计的基于本机指令的组件。

### 基于 Material 的 UI 库

* [angular-ui-plusify](https://github.com/RockyCott/angular-ui-plusify) - 包括日期时间选择器和 Markdown 编辑器，并计划扩展到完整的 Angular UI 工具包。
* [MDBootstrap](https://github.com/mdbootstrap/mdb-angular-ui-kit) - Bootstrap 5 和 Angular 17 UI KIT - 700 多个组件，MIT 许可证，安装简单。
* [Angular Material](https://material.angular.dev/) - Angular 的材料设计组件。
* [Covalent](https://github.com/Teradata/covalent/) - 基于 Angular Material 构建的 Teradata UI 平台。
* [IgniteUI Angular](https://github.com/IgniteUI/igniteui-angular) - Ignite UI for Angular 是一个完整的 Angular 原生、基于 Material 的 Angular UI 组件库，具有最快的网格、图表等。
* [angular-jqwidgets](https://www.jqwidgets.com/angular/) - 采用材料设计的高级角度组件。
* [@ng-matero/extensions](https://github.com/ng-matero/extensions) - 角度材质扩展库。
* [angular-material-css-vars](https://github.com/johannesjo/angular-material-css-vars) - 将 CSS 变量与 Angular Material 结合使用的小库。
* [ngx-components](https://github.com/DSI-HUG/ngx-components) - Angular 的有用组件和实用函数。
* [ngx-material-auth](https://github.com/Service-Soft/ngx-material-auth) - Angular 的库，提供有关身份验证和授权的前端部分的功能。
* [ngx-material-navigation](https://github.com/Service-Soft/ngx-material-navigation) - 创建材料导航元素，例如组合导航栏和侧边导航或页脚，根据断点自动移动项目。
* [ngx-material-entity](https://github.com/Service-Soft/ngx-material-entity) - 使用“NgxMaterialEntity”，您可以创建实体并定义如何直接在其属性上显示它们。它甚至可以生成完整且高度可定制的 CRUD 表。
* [c3-components](https://github.com/c3ulnta0rk/c3-components) - 一个扩展了“@angular/material”库的开源组件库。
* [simplematcomponents](https://github.com/wobkenh/simplematcomponents) - 适合或使用 Angular Material Design 的 Angular 组件集。
* [Angular Material Dev UI](https://ui.angular-material.dev/home) - 开发人员探索基于 Angular Material 和 Tailwind CSS 的应用程序的组件和块的一站。
* [nmce](https://github.com/zijianhuang/nmce) - Angular Material 扩展套件，具有可重用代码和 UI 增强功能，适用于复杂、数据丰富的业务应用程序。
* [NgxMatFacetToolkit](https://github.com/drsutphin/NgxMatFacetToolkit) - 带有 Material UI 的 Angular 独立构面过滤工具包。
* [ngx-dynamic-stepper](https://github.com/yingyu-projects/ngx-dynamic-stepper) - 一个强大、灵活的 Angular 库，用于创建基于 Angular Material Stepper 的动态向导式步进器。
* [BuilderKit](https://builderkit.dev/) - 基于 Angular Material 构建的完整 UI 工具包和现代设计系统，包含块、模板，为构建 Angular 应用程序奠定了坚实的基础。

### 基于 Tailwind CSS 构建的 UI 库

* [angular-superui](https://github.com/bhaimicrosoft/angular-superui) - 全面的 Angular UI 库，包含 50 多个可立即投入生产的组件，基于 TailwindCSSv4、TypeScript 和 Angular17+ Signals 构建。
* [angular-tailwind-ui](https://github.com/quedicesebas/angular-tailwind-ui) - 易于使用且简单的组件、指令和服务。使用 Angular 19 和 Tailwind CSS 3。
* [elbe-ui](https://github.com/marcjulian/elbe-ui) - 使用 Tailwind CSS 和 Spartan UI 构建的 Angular UI 组件。
* [Flowbite](https://flowbite.com/docs/getting-started/angular/) - 使用 Tailwind CSS 构建的开源 UI 组件，支持 Angular。
* [FlyonUI](https://github.com/themeselection/flyonui) - [集成](https://flyonui.com/framework-integrations/angular/) FlyonUI 与 Angular 和 Tailwind CSS 相结合，创建现代化的响应式 UI，从而高效简化您的开发流程。
* [Galaxy UI](https://github.com/buikevin/galaxy-design) - 通用组件库为 Angular 带来了美观且易于访问的组件。
* [koala-ui](https://github.com/igordrangel/koala-ui) - 一个现代且可访问的组件库，旨在加速界面开发。
* [ng-brutalism](https://github.com/khangtrannn/ng-brutalism) - 新野蛮主义 Angular UI 库，带有信号、zoneless 和 Tailwind CSS v4。大胆的边框、偏移的阴影、端到端的固执己见的美学。
* [Metronic](https://keenthemes.com/metronic/tailwind/docs/getting-started/integration/angular) - 全面的 Tailwind CSS UI 工具包，用于高效构建现代、可扩展的 Web 应用程序。
* [ngx-lite-suite](https://github.com/michaelsch72/ngx-lite-suite) - Angular UI 库，具有玻璃态、渐变和流体动画的“Lite Suite”设计系统。
* [ngx-tailwindcss](https://github.com/pegasusheavy/ngx-tailwindcss) - 适用于 Tailwind CSS 4+ 的可定制 Angular UI 库，提供可访问、设计精美的组件以及完整的样式控制。
* [ngx-tw](https://github.com/bugMaker-237/ngx-tw) - 使用 Tailwind CSS 构建的综合组件库，为 Angular 应用程序提供一组现代且可定制的 UI 组件。
* [nicacoder-ng](https://ng.nicacoder.com/) - 可定制组件的集中式 Angular 库可加速开发并确保项目一致性。
* [Preline UI](https://preline.co/docs/frameworks-angular.html#docs-on-this-page-sidebar) - [Preline](https://github.com/htmlstreamofficial/preline) 是一组基于实用程序优先的 Tailwind CSS 框架的开源预构建 UI 组件集。
* [PrimeBlocks](https://primeblocks.org/) - 专业设计的 UI 块专为快速应用程序开发而定制。
* [seacotools](https://github.com/Seacotec/seacotools) - 专为现代 Angular 应用程序设计的库，提供一套与 Tailwind CSS 兼容的可重用 UI 组件和服务。
* [semantic-components](https://github.com/gridatek/semantic-components) - 模块化 Angular CDK + Tailwind UI 元素，具有语义 HTML、完全可访问性和轻量级灵活性。
* [simui](https://github.com/dofu-lab/simui) - 使用 Tailwind CSS 和 Spartan 构建的漂亮 Angular UI 组件。
* [starting-point-ui](https://github.com/gufodotdev/starting-point-ui) - 与框架无关的 Tailwind CSS 组件受 shadcn/ui 启发，与 Angular 完全兼容。
* [synerity-ui](https://github.com/synerity-ai/synerity-ui) - 企业级 Angular20+ 库，包含 90 多个可访问、高性能的 Tailwind 风格组件，适用于现代应用程序。
* [Tailkit UI](https://tailkit.com/) - 为您的项目精心打造、可定制、完全响应式的 Tailwind CSS 组件、模板和工具。
* [tailng](https://github.com/tociva/tailng) - 使用 Tailwind 设计的角度组件可实现类似 Material 的外观。
* [zapui](https://github.com/zapuilib/zapui) - 使用来自 [zap:ui](https://zapui.togethercreative.co.uk/) 的 Tailwind 支持的设计系统构建可扩展的 Angular 应用程序。

### UI 库和 Ionic 框架

* [官方网站](https://ionicframework.com)
* [官方 GitHub 存储库](https://github.com/ionic-team/ionic-framework)
* [Ionic Academy](https://ionicacademy.com/) - 学习 Ionic 的最快方法。
* [Elite Ionic](https://eliteionic.com/) - 为想要创建下一个级别的本机 Web 应用程序的 Angular 开发人员提供的高级培训。
* [Ionic Start](https://ionicstart.com/) - 使用 Ionic 构建 Web 和本机移动应用程序，同时使用 Angular 学习现代反应式开发。
* [awesome-cordova-plugins](https://github.com/danielsogl/awesome-cordova-plugins) - 使用 Cordova/PhoneGap 和开放 Web 技术构建的移动应用程序的本机功能。完成 TypeScript 支持。
* [ionic-angular-library](https://github.com/rdlabo-team/ionic-angular-library) - 可用于开发 Ionic Angular 应用程序的组件和服务的集合。
* [ionic-angular-collect-icons](https://github.com/rdlabo-team/ionic-angular-collect-icons) - 用于对 ionIcons 进行分组并自动生成导出文件的库，简化小型项目中的 addIcons() 管理。
* [IDEA-Ionic8-extra](https://github.com/iter-idea/IDEA-Ionic8-extra) - [IDEA's](https://www.iter-idea.com/) 基于 Ionic 8 构建的额外组件和服务，并与不同的 NPM 包一起分发。
* [ionic-component-snippets](https://github.com/LennonReid/ionic-component-snippets) - 非官方 Ionic 演示和库的存储库，仍然可以使开发人员及其应用程序受益。
* [ionic-header-parallax](https://github.com/RaschidJFR/ionic-header-parallax) - 该指令可以在“ion-header”元素上启用视差效果，以在页面顶部显示封面照片，并在向下滚动时过渡到普通工具栏。
* [ionic-state](https://github.com/godenji/ionic-state) - 提供用于在 Ionic 应用程序中处理状态的实用程序。
* [ionx-search-select](https://github.com/kisimediaDE/ionx-search-select) - 现代 Angular/Ionic 搜索和选择，具有独立组件、信号和完整的“ControlValueAccessor”支持。
* [ionic-insta-api-wrapper](https://github.com/appit-online/ionic-insta-api-wrapper) - 轻量级 Ionic/Cordova 库，用于通过登录和 cookie 支持获取 Instagram 内容（故事、卷轴、帖子、个人资料）。
* [ionic-adv-tooltip](https://github.com/PhaZRic/ionic-adv-tooltip) - Ionic Angular 的媒体丰富工具提示和弹出窗口可在任何主机上渲染模板、图像、视频或实时预览。
* [PushApp-Capacitor](https://github.com/mehery-soccom/PushApp-Capacitor) - 一个 Capacitor 插件，用于 Ionic/Angular/Capacitor 应用程序中的推送通知、应用内消息传递、事件跟踪和会话处理。

### 用户界面基元

* [ng-primitives](https://github.com/ng-primitives/ng-primitives) - 一个低级 UI 组件库，重点关注可访问性、自定义和开发人员体验。
* [primitives](https://github.com/radix-ng/primitives) - [Radix UI](https://www.radix-ui.com/) 原语的 Angular 端口。无障碍。可定制。
* [vacui-ui](https://github.com/DanielAlcaraz/vacui-ui) - 一个无头 Angular 库，以实用程序优先、原语、低级指令作为基本元素。
* [ngx-headless](https://github.com/fawadtariq/ngx-headless) - 受 [Headless UI](https://headlessui.com) 和 [FormKit](https://formkit.com) 启发的独立、可访问的 Angular 原语集合。
* [Clean Architecture Frontend](https://github.com/ialiaslani/caf) - 用于使用干净架构构建前端应用程序的与领域无关的原语。可与 React、Vue、Angular 或任何未来的框架配合使用。
* [@luminacn/ui](https://github.com/luminacn/ui) - Angular 的信号优先、无头 UI 原语。
* [Bloc UI](https://github.com/debasish1996/BLOC-UI) - 轻量级、可访问的 Angular 组件，设计意见为零。使用您自己的样式或可选的主题包。
* [angular-primitives](https://github.com/snatuva/angular-primitives) - 信号优先的 Angular 原语，用于构建可扩展、可访问的 UI 系统。
* [frame-ui](https://github.com/Gamekohl/frame-ui) - 围绕现代基元构建的可定制 Angular 组件库。

### 观众

* [file-viewer](https://github.com/ameyb88/file-viewer) - 适用于 Angular 应用程序的强大通用文件预览器库，支持 PDF、图像、文档、电子表格等。
* [json-diff](https://github.com/mufasa-dev/Json-diff) - 一个基于 Angular 的工具，可快速比较两个 JSON 对象并突出显示它们的差异！
* [ngx-diff](https://github.com/rars/ngx-diff) - 用于显示文本差异的 Angular 组件库。
* [ngx-gist](https://github.com/ProAngular/ngx-gist) - Angular Material 和highlightjs 风格的显示框，用于显示 GitHub 要点和本地代码片段。
* [ngx-json-diff-viewer](https://www.npmjs.com/package/ngx-json-diff-viewer) - 用于直观地显示两个 JSON 对象之间差异的 Angular 组件。
* [ngx-json-schema-viewer](https://github.com/jy95/ngx-json-schema-viewer) - Angular 中的 JSON 模式查看器。
* [ngx-json-treeview](https://github.com/MichaelDoyle/ngx-json-treeview) - Angular 的可折叠 JSON 树视图。
* [ngx-omniview](https://github.com/binapani-edu/ngx-omniview) - Angular 的一体化内容查看器，仅使用单个组件即可将原始字符串输入无缝显示为纯文本、HTML、Markdown、LaTeX、MathJax、JSON 等。
* [ngx-profile-comparison](https://github.com/singharsh0/ngx-profile-comparison) - 一个高质量、可用于生产的 Angular 组件库，通过突出显示两个用户配置文件的相似点和差异来直观地比较它们。
* [ngx-serial-console](https://github.com/binuud/ngx-serial-console) - 用于监视串行设备输出的 Angular 组件和服务。
* [ngx-universal-viewer](https://github.com/Imishu29/ngx-universal-viewer) - 一个 Angular 组件，用于以连续滚动或逐页模式查看 PDF、Word、Excel 和 PowerPoint 文件。
* [ngx-voyage](https://github.com/mschn/ngx-voyage) - 适用于 Angular 和 PrimeNG 的文件资源管理器。
* [ngx-file-peek](https://github.com/valtonngara/ngx-file-peek) - 一个 Angular 独立组件库，可将来自任何 URL 或存储源的真实文件内容呈现为缩略图。

### 视觉效果

* [angular-tag-cloud-module](https://github.com/d-koppenhagen/angular-tag-cloud-module) - 通过该模块，您可以生成词云/标签云。
* [levita](https://github.com/Jeromearsene/levita) - 具有加速度计支持的轻量级 3D 倾斜和视差。
* [ng-snowfall](https://github.com/Leksip/ng-snowfall) - 交互式角度降雪组件，其中雪花响应鼠标移动以创建逼真的风效果。
* [ng-whiteboard](https://github.com/mostafazke/ng-whiteboard) - 轻量级 Angular 白板组件。
* [@craftedcode-dev/ngx-analog-clock](https://github.com/craftedcode-dev/ngx-analog-clock) - 适用于 Angular 应用程序的模拟时钟组件，具有时区支持、自定义主题和广泛的样式选项。
* [@DerStimmler/ngx-analog-clock](https://github.com/DerStimmler/ngx-analog-clock) - 为您的 Angular 应用程序定制模拟时钟。
* [ngx-color-scheme](https://github.com/rbalet/ngx-color-scheme) - 轻松将暗模式添加到您的 Angular 应用程序中。
* [ngx-countdown](https://github.com/cipchk/ngx-countdown) - 简单、轻松且高性能的倒计时。
* [ngx-font-picker](https://github.com/zefoy/ngx-font-picker) - 适用于 Angular 的 Google 字体字体选择器小部件。
* [ngx-gauge](https://github.com/ashish-chopra/ngx-gauge) - 用于 Angular 应用程序和仪表板的高度可定制的仪表组件。
* [ngx-glassy-effect](https://github.com/anassmdi/ngx-glassy-effect) - 向 HTML 元素应用玻璃效果的 Angular 指令。
* [ngx-globe](https://github.com/omnedia/ngx-globe) - 一个简单的组件库，用于创建带有动画地球仪的容器。
* [ngx-gooey](https://github.com/wadie/ngx-gooey) - Angular 的粘稠效果，用于形状斑点/元球。
* [ngx-lamp](https://github.com/omnedia/ngx-lamp) - 用于创建灯的简单组件库。
* [ngx-neon-underline](https://github.com/omnedia/ngx-neon-underline) - 一个 Angular 库，可为您的组件提供发光的霓虹灯下划线效果。
* [ngx-parallax-stars](https://github.com/DerStimmler/ngx-parallax-stars) - Angular 库可创建具有视差效果的美丽星星。
* [ngx-waterbox](https://github.com/vwochnik/ngx-waterbox) - 等距水箱组件。

## 底层技术

### 接收JS

* [Official website](https://rxjs.dev/) - JavaScript 的反应式扩展库。
* [eslint-plugin-rxjs-x](https://github.com/JasonWeinzierl/eslint-plugin-rxjs-x) - [eslint-plugin-rxjs](https://github.com/cartant/eslint-plugin-rxjs) 的分支添加了 ESLint 平面配置支持，并进行了重大更改和改进。
* [learn-rxjs](https://github.com/btroncone/learn-rxjs) - RxJS 的清晰示例、解释和资源。
* [ng-event-bus](https://github.com/cristiammercado/ng-event-bus) - 用于 Angular 的基于 RxJS 的消息总线服务。
* [ngx-device-permission](https://github.com/PhilipSh/ngx-device-permission) - Angular 库，用于使用 RxJS 以反应方式处理设备权限（相机、麦克风、地理位置等）。
* [ngx-operators](https://github.com/nilsmehlhorn/ngx-operators) - Angular 的 RxJS 运算符。
* [ngx-safe-subscribe](https://github.com/Badisi/ngx-safe-subscribe) - 自动取消订阅 Angular 组件中的 RxJS 可观察量的简单方法。
* [operators](https://github.com/jscutlery/devkit/tree/main/packages/operators) - 该包重新组合了几个 RxJS 运算符，旨在简化一些常见模式。
* [reactive-event-source](https://github.com/andreasnicolaou/reactive-event-source) - 基于 RxJS 的轻量级 EventSource 包装器，具有自动重新连接、泄漏预防和反应式状态管理功能。
* [redux-observable](https://github.com/redux-observable/redux-observable) - RxJS 中间件使用“Epics”在 Redux 中实现操作副作用。
* [rx-computed](https://github.com/jscutlery/devkit/tree/main/packages/rx-computed) - 基于 RxJS 的异步版本的信号“compulated()”。
* [@mrOranger/RxJs](https://github.com/mrOranger/RxJs) - 使用 RxJS 库的反应式编程范例的理论和示例。
* [rxjs-broker](https://github.com/chrisguttandin/rxjs-broker) - 用于 WebRTC 数据通道和 WebSocket 的 RxJS 消息代理。
* [rxjs-challenge](https://github.com/AngularWave/rxjs-challenge) - 一组 RxJS 小谜题，用于练习您的 Observable 技能。
* [rxjs-collection](https://github.com/henryruhs/rxjs-collection) - RxJS 增强了 Array、Map、WeakMap、Set 和 WeakSet。
* [rxjs-common](https://github.com/paddls/rxjs-common) - 有用的 RxJS 运算符的集合。
* [rxjs-conduit](https://github.com/Fasteroid/rxjs-conduit) - RxJS ReplaySubjects 具有附加功能，使反应式编程变得更容易。
* [rxjs-course](https://github.com/angular-university/rxjs-course) - Angular 大学的 RxJS 课程。
* [subscribable-things](https://github.com/chrisguttandin/subscribable-things) - 各种浏览器 API 的反应式包装器的集合。
* [subsiphon](https://github.com/shobeiry/subsiphon) - 用于使用索引/命名键和简单清理方法管理多个 RxJS 订阅的轻量级实用程序。
* [web-serial-rxjs](https://github.com/gurezo/web-serial-rxjs) - 一个 TypeScript 库，为 Web 串行 API 提供基于 RxJS 的反应式包装器，从而在 Web 应用程序中实现轻松的串行端口通信。

### 打字稿

* [官方网站](https://www.typescriptlang.org/)
* [官方 TypeScript REPL](https://www.typescriptlang.org/play/)
* [官方 GitHub 存储库](https://github.com/Microsoft/TypeScript)
* [DefinitelyTyped GitHub repository](https://github.com/DefinitelyTyped/DefinitelyTyped) - 高质量 TypeScript 类型定义的存储库。
* [guardz](https://github.com/thiennp/guardz) - 轻量级、零依赖的 TypeScript 类型防护，用于运行时验证和结构化错误处理。
* [mutates](https://github.com/IKatsuba/mutates) - 强大的 TypeScript AST 突变工具集，从“ng-morph”分叉，可实现 Angular 之外的广泛项目范围转换。
* [quicktype](https://github.com/glideapps/quicktype) - 从 JSON、Schema 和 GraphQL 生成类型和转换器。
* [Sheriff](https://github.com/softarc-consulting/sheriff) - TypeScript 项目的轻量级模块化。
* [Total TypeScript Book](https://github.com/total-typescript/total-typescript-book) - 即将出版的 Total TypeScript 书籍的配套存储库。
* [transform.tools](https://transform.tools/json-to-typescript) - 使用此 JSON 到 TypeScript 转换器可以节省大量输入 API 响应的时间。
* [trpc](https://github.com/trpc/trpc) - 快速行动，不破坏任何东西。端到端类型安全 API 变得简单。
* [ts-essentials](https://github.com/ts-essentials/ts-essentials) - 所有基本的 TypeScript 类型都集中在一处。
* [ts-pattern](https://github.com/gvergnaud/ts-pattern) - 适用于 TypeScript 的详尽模式匹配库，具有智能类型推断功能。
* [ts-serializer](https://github.com/paddls/ts-serializer) - 将模型序列化为强类型 TypeScript 类。
* [tsconfig](https://github.com/smartrecruiters/tsconfig) - SmartRecruiters 的 tsconfig 包含所有严格的规则并提高您的项目类型安全性。
* [typebox](https://github.com/sinclairzx81/typebox) - 具有 TypeScript 静态类型解析的 JSON 模式类型生成器。
* [type-challenges](https://github.com/type-challenges/type-challenges) - 带有在线评判的 TypeScript 类型挑战集合。
* [type-fest](https://github.com/sindresorhus/type-fest) - 基本 TypeScript 类型的集合。将包添加为依赖项或复制粘贴所需的类型。
* [typehero](https://github.com/typehero/typehero) - 与 TypeScript 开发人员社区联系、协作和成长。
* [typescript-book](https://github.com/gibbok/typescript-book) - TypeScript 有效开发的简明指南。
* [valibot](https://github.com/fabian-hiller/valibot) - 用于验证结构数据的模块化和类型安全模式库。
* [zod](https://github.com/colinhacks/zod) - 使用静态类型推断进行 TypeScript 优先模式验证。

## 框架互操作性

### 跨框架集成

* [detector](https://github.com/kitium-ai/detector) - 一个零依赖、TypeScript 优先的库，用于快速、通用地检测平台、框架、浏览器和功能。
* [@oguimbal/ngx-react](https://github.com/oguimbal/ngx-react) - 实现 React 和 Angular 组件的平滑集成，或两者之间的轻松迁移。
* [ngx-reactify](https://github.com/knackstedt/ngx-reactify) - 使 Angular 和 React 应用程序一起运行变得容易的库。
* [ng-react-bridge](https://github.com/john310897/ng-react-bridge) - 一个轻量级的 Angular 包，使开发人员能够使用指令在 Angular 组件内无缝渲染 React 组件。
* [gong](https://github.com/fullstack-lang/gong) - 具有 Go（Gin、Gorm、纯 SQLite）后端和 Angular Material 前端的全栈框架。
* [@retejs/angular-plugin](https://github.com/retejs/angular-plugin) - Angular 插件，具有节点、连接、套接字和控制组件的经典预设，基于 [Rete.js](https://retejs.org/) 构建。
* [Stencil](https://stenciljs.com/docs/angular) - 为您的 Web 组件生成 Angular 组件包装器。
* [AnQst](https://github.com/DusteDdk/AnQst) - 从共享 DSL 生成 Angular 服务和本机 Qt 小部件，让 Angular 应用程序通过 AnQst CLI 和主机库编译成基于 QWidget 的 C++ UI。

### 外部整合

* [Sentry](https://docs.sentry.io/platforms/javascript/guides/angular/configuration/integrations/) - 开发人员优先的错误跟踪和性能监控平台。
* [DataDog](https://docs.datadoghq.com/integrations/rum_angular/) - 通过 Datadog Angular 集成，您可以快速解决性能问题。
* [Elastic](https://www.elastic.co/guide/en/apm/agent/rum-js/current/angular-integration.html) - 使用 Angular 应用程序监控真实用户 JavaScript 代理。
* [@elastic/apm-rum-angular](https://www.npmjs.com/package/@elastic/apm-rum-angular) - 针对 Angular 应用程序的 Elastic APM 真实用户监控。
* [Partytown](https://partytown.qwik.dev/angular/) - 将资源密集型第三方脚本从主线程重新定位到 Web Worker 中。
* [Pega](https://community.pega.com/marketplace/component/angular-sdk) - Angular SDK 包括一个桥接器和 DX 组件，用于将 ConstellationJS 引擎连接到基于 Angular 的设计系统。
* [Postcat](https://github.com/Postcatlab/postcat) - 一个基于 Angular 和 Electron 的轻量级、可扩展的 API 工具。
* [NativeScript](https://docs.nativescript.org) - 直接向 JavaScript 运行时（具有强类型）提供平台 API，以获得丰富的 TypeScript 开发体验。
* [Strich](https://docs.strich.io/angular-integration-guide.html) - 一个 JavaScript 库，用于直接在 Web 浏览器中进行实时、多格式条形码扫描。
* [stream-chat-angular](https://github.com/GetStream/stream-chat-angular) - Angular 聊天 SDK ➜ 流聊天。轻松构建聊天应用程序。
* [foblex2D](https://github.com/siarheihuzarevich/foblex2D) - 用于 2D 几何的 Angular 库，具有点、线、向量、形状和变换的实用程序，用于“Folex Flow”。
* [Bloomreach Angular SDK](https://github.com/bloomreach/spa-sdk/blob/main/packages/ng-sdk/README.md) - 为基于 Angular 的应用程序提供与 [Bloomreach Content](https://www.bloomreach.com/en/products/content) 的简化无头集成。
* [ngx-notion-cms](https://github.com/borjamrd/ngx-notion-cms) - 通过 Angular 应用程序作为 CMS 渲染您的 Notion 内容。
* [Otter](https://github.com/AmadeusITGroup/otter) - 高度模块化的 Angular 框架，具有用于本地化、测试、定制和 CMS 驱动的动态配置的单元。
* [HyperFormula](https://hyperformula.handsontable.com/guide/integration-with-angular.html#demo) - TypeScript 中的无头电子表格引擎，用于公式解析/评估，带有 Angular 集成演示。
* [fusio-sdk-javascript-angular](https://github.com/apioo/fusio-sdk-javascript-angular) - 此 SDK 使 Angular 应用程序能够与 [Fusio](https://www.fusio-project.org/) 集成，由 [backend](https://github.com/apioo/fusio-apps-backend) 和 [developer](https://github.com/apioo/fusio-apps-developer) 等项目使用。
* [limitless-angular](https://github.com/limitless-angular/limitless-angular) - 一系列强大的 Angular 库，旨在增强 Angular 生态系统，并帮助开发人员构建更好的应用程序，重点关注“Sanity.io”集成。
* [Bit](https://bit.dev/docs/angular-introduction/) - 利用 Bit 构建可组合软件。
* [angular-twitter-timeline](https://github.com/mustafaer/angular-twitter-timeline) - Angular 公共 Twitter 时间轴小部件。
* [ngx-signalr-websocket](https://github.com/yurivoronin/ngx-signalr-websocket) - 适用于 Angular 的轻量级 ASP.NET SignalR 客户端。
* [Keploy](https://keploy.io/docs/quickstart/openhospital/) - 通过与 Angular UI 交互来记录测试用例和模拟，然后使用 Keploy 对其进行测试。
* [alterior](https://github.com/alterior-mvc/alterior) - 同构 TypeScript 框架，用于构建具有无缝 Angular 集成的模块化服务。
* [23blocks SDK](https://github.com/23blocks-OS/frontend-sdk) - 使用模块化后端块构建全栈应用程序的速度提高了 10 倍。

### 包装纸

* [angular-calendly](https://github.com/tolutronics/angular-calendly) - 一个现代 Angular 库，提供用于嵌入 [Calendly](https://calendly.com/) 调度小部件的独立组件。
* [angular-email-editor](https://github.com/unlayer/angular-email-editor) - [Unlayer](https://unlayer.com/embed) 的拖放式电子邮件编辑器作为 Angular 包装组件。
* [angular-three](https://github.com/angular-threejs/angular-three) - [THREE.js](https://github.com/mrdoob/third.js) 的角度渲染器。
* [atlas-editor](https://github.com/sumanthnagireddi/atlas-editor) - 动态加载基于 React 的 Atlaskit 编辑器和侧面导航 Web 组件的 Angular 包装器。
* [chat-widget-adapters](https://github.com/livechat/chat-widget-adapters) - [LiveChat](https://developers.livechat.com/) 聊天小部件 (JavaScript API) 的 Angular 包装器。
* [ckeditor5-angular](https://github.com/ckeditor/ckeditor5-angular) - 适用于 Angular 2+ 的官方 CKEditor 5 富文本编辑器组件。
* [cytoscape-angular](https://github.com/michaelbushe/cytoscape-angular) - 一个生产就绪的 Angular 库，使用 [Cytoscape.js](https://js.cytoscape.org/) 提供复杂的图形可视化功能。
* [d3-cloud-angular](https://github.com/maitrungduc1410/d3-cloud-angular) - 基于 [d3-cloud](https://github.com/jasondavies/d3-cloud) 构建的 Angular 的 D3 Cloud 组件。
* [flowchart-sequence-designer-angular](https://github.com/ag-gr-hub/flowchart-sequence-designer-angular) - [flowchart-sequence-designer](https://github.com/ag-gr-hub/flowchart-sequence-designer)的角度包装器。
* [gojs-angular](https://github.com/NorthwoodsSoftware/gojs-angular) - 一组用于管理 [GoJS](https://gojs.net/latest/index.html) 图表、调色板和概述的 Angular 组件。
* [@foisit/angular-wrapper](https://github.com/boluwatifee4/foisit/tree/main/libs/angular-wrapper) - 用于 Angular 应用程序的人工智能对话助手。
* [lyne-angular](https://github.com/sbb-design-systems/lyne-angular) - [Lyne Web 组件](https://github.com/sbb-design-systems/lyne-components) 的角度包装器。
* [@interopio/ng](https://www.npmjs.com/package/@interopio/ng) - [IO Connect](https://interop.io/) Angular 包装器，用于简化项目中 IO Connect 库的初始化和使用。
* [ng-elementum](https://github.com/MillerSvt/ng-elementum) - “@angular/elements”的现代分支，增强了 Angular 组件与 Web 组件标准的集成。
* [ngfire](https://github.com/qarapace/ngfire) - Firebase JS SDK 的最小 Angular 包装器。
* [ngx-apexgantt](https://github.com/apexcharts/ngx-apexgantt) - [ApexGantt](https://github.com/apexcharts/apexgantt) 的 Angular 包装器，这是一个用于创建基于 SVG 的甘特图的 JavaScript 库。
* [ngx-apexsankey](https://github.com/apexcharts/ngx-apexsankey) - [ApexSankey](https://github.com/apexcharts/apexsankey) 的 Angular 包装器 - 用于创建 Sankey 图的 JavaScript 库。
* [ngx-apextree](https://github.com/apexcharts/ngx-apextree) - [ApexTree](https://github.com/apexcharts/apextree) 的 Angular 包装器 - 用于创建组织和分层图表的 JavaScript 库。
* [ngx-barcode6](https://github.com/efgiese/ngx-barcode6) - Angular 9+ 的 Angular 组件，用于基于 [JsBarcode](https://github.com/lindell/JsBarcode) 创建一维条形码。
* [ngx-chessground](https://github.com/topce/ngx-chessground) - [chessground](https://github.com/ornicar/chessground) 的角度包装器。
* [ngx-d3](https://github.com/simonegosetto/ngx-d3) - 受 [d3-ng2-service](https://github.com/tomwanzek/d3-ng2-service) 启发的 Angular 应用程序的 [D3](https://d3js.org/) 包装服务。
* [ngx-fabric-wrapper](https://github.com/zefoy/ngx-fabric-wrapper) - [Fabric](http://fabricjs.com/) 的角度包装库。
* [ngx-filesize](https://github.com/amitdahan/ngx-filesize) - [filesize.js](https://filesizejs.com/) 的角度包装器。
* [ngx-grapesjs](https://github.com/Developer-Plexscape/ngx-grapesjs) - [GrapesJS](https://grapesjs.com) 的 Angular 包装库。
* [ngx-highlight-js](https://github.com/cipchk/ngx-highlight-js) - [highlight.js](https://highlightjs.org/) 的 Angular 包装器用于语法突出显示。
* [ngx-kel-agent](https://github.com/k0swe/ngx-kel-agent) - 用于与 [kel-agent](https://github.com/k0swe/kel-agent) 集成的 Angular 应用程序的客户端库。
* [ngx-linkifyjs](https://github.com/code-name-jack/ngx-linkifyjs) - Angular [Linkify](https://github.com/nfrasser/linkifyjs) 包装器，用于自动检测 URL、电子邮件、主题标签和提及，并将它们转换为 HTML 链接。
* [ngx-neoline](https://github.com/smartargs/ngx-neoline) - [NeoLine](https://tutorial.neoline.io/) N3 dAPI 的 Angular 包装器，检测提供程序、等待 READY 并公开类型化方法。
* [ngx-open-web-ui-chat](https://github.com/JealousyM/ngx-open-web-ui-chat) - 用于嵌入 [Open WebUI](https://openwebui.com/) 聊天与 Socket.IO 流、对话历史记录和 Markdown 支持的 Angular 组件库。
* [ngx-pendo](https://github.com/yociduo/ngx-pendo) - 在 Angular 中加载 Pendo 的简单包装器。
* [ngx-sentry](https://github.com/DSI-HUG/ngx-sentry) - [Sentry JavaScript SDK](https://github.com/getsentry/sentry-javascript) 的角度包装器。
* [ngx-serializer](https://github.com/paddls/ngx-serializer) - `@paddls/ts-serializer` 库的角度包装器。
* [ngx-simple-text-diff](https://github.com/jjtortosa/ngx-simple-text-diff) - 使用 [diff](https://www.npmjs.com/package/diff) 库显示文本差异的 Angular 库。
* [ngx-socket-io](https://github.com/rodgc/ngx-socket-io) - 用于 Angular 的 [Socket.IO](https://socket.io/) 模块。
* [ngx-tagify](https://github.com/Brakebein/ngx-tagify) - 包装 [Tagify](https://github.com/yaireo/tagify/) 的 Angular 库。
* [ngx-three](https://github.com/demike/ngx-three) - 以声明方式将 [Three.js](https://thirdjs.org) 与您的 Angular 项目结合使用。
* [ngx-three-globe](https://github.com/omnedia/ngx-three-globe) - 一个 Angular 库，提供使用“Three.js”构建的交互式 3D 地球可视化。
* [ngx-virtual-select](https://github.com/zinetnorf/ngx-virtual-select) - 在 Angular 中集成 [Virtual Select](https://github.com/sa-si-dev/virtual-select) 的组件。
* [ngx-vis](https://github.com/visjs/ngx-vis) - [vis.js](https://visjs.org/) 的角度包装器。
* [ngx-viz](https://github.com/vedph/ngx-viz) - 用于渲染 [DOT 图表](https://graphviz.org/doc/info/lang.html) 的简单 Angular [viz.js](https://viz-js.com/) 包装器。
* [ngx-webdatarocks](https://github.com/WebDataRocks/ngx-webdatarocks) - [WebDataRocks](https://www.webdatarocks.com/) 的角度包装器。按照此[示例](https://github.com/WebDataRocks/pivot-angular) 集成 WebDataRocks Web 报告工具。
* [ngx-xyflow](https://github.com/knackstedt/ngx-xyflow) - [xyflow](https://github.com/xyflow/xyflow) 的角度包装器。
* [rive-angular](https://github.com/Grandgular/rive) - 用于 [Rive](https://rive.app/) 动画的现代 Angular 包装器，具有反应式状态管理，采用 Angular 信号和无区域架构构建。
* [seatsio-angular](https://github.com/seatsio/seatsio-angular) - 用于渲染 [Seats.io](https://www.seats.io/) 座位表的角度包装器。
* [simplyfire](https://github.com/coturiv/simplyfire) - 用于 Firebase 云功能和 Angular 的轻量级 Firestore API。
* [zag-angular](https://github.com/makuko/zag-angular) - [zag](https://github.com/chakra-ui/zag) 的角度包装器。

## Angular 启发的解决方案

* [angular-style-injector](https://github.com/emmat-york/angular-style-injector) - 受 Angular 注入器启发的轻量级依赖注入容器。
* [di](https://github.com/kaokei/di) - 该库是一个轻量级依赖注入库，类似于[InversifyJS](https://github.com/inversify/InversifyJS)和[typedi](https://github.com/typestack/typedi)。
* [flexdi](https://github.com/AndreyShashlovDev/flexdi) - 适用于 React、React Native 和 Vue3 的灵​​活、轻量级 DI 库，受到 NestJS 和 Angular 的启发。
* [gapi](https://github.com/Stradivario/gapi) - 受到 Angular 的启发，旨在以最小的努力提供复杂的 Node.js GraphQL 后端应用程序。
* [GTPL](https://github.com/garag-lib/GTPL) - 使用 Direct DOM 和 Proxy 的反应式模板的 TypeScript 库，受到 Vue、Angular AOT 和 JSX 的启发，采用紧凑的 9KB 包。
* [illuma](https://github.com/git-illuma/core) - TypeScript 的 Angular 风格依赖注入。
* [indulgent](https://github.com/frodi-karlsson/indulgent) - 一组轻量级的 TypeScript 实用程序，专为 Web 开发而设计，没有外部依赖项，并针对稳定的运行时性能进行了优化。
* [injection-js](https://github.com/mgechev/injection-js) - 一个快速、经过充分测试的 JavaScript/TypeScript 依赖注入库，从 Angular 的“ReflectiveInjector”中提取。
* [ioc](https://github.com/Isqanderm/ioc) - 适用于 TypeScript 应用程序的强大且灵活的控制反转 (IoC) 容器。受到 Angular 和 NestJS 的启发。
* [knifecycle](https://github.com/nfroidure/knifecycle) - 通过不显眼的依赖注入实现自动管理 Node.js 进程的生命周期。
* [Lua-Generate](https://github.com/Gabriel-c0Nsp/Lua-Generate) - 受 Angular 的 ng 工具启发，用于生成样板代码的 CLI 工具。
* [named-slots](https://github.com/maybebot/named-slots) - React 组件的声明性“漏洞”，受到 Vue、Svelte、Angular 和 WebComponents 中插槽的启发。
* [needle-di](https://github.com/needle-di/needle-di) - 用于 JavaScript 和 TypeScript 项目的轻量级、类型安全的依赖注入 (DI) 库。
* [npm-clang-format-node](https://github.com/lumirlumir/npm-clang-format-node) - LLVM Clang 的 clang-format 和 git-clang-format 本机二进制文件的节点包装器，受 [clang-format](https://github.com/angular/clang-format) 启发。
* [ozean](https://github.com/ozeanjs/ozean) - 一个基于 Bun 运行时构建的现代、简单且高性能的 Web 框架。它提供了 Angular 用户应该熟悉的开发体验和架构。
* [react-di-lite](https://github.com/zobla-kv/react-di-lite) - 受 Angular 服务启发，React 的轻量级、分层依赖注入。
* [@joanpablo/reactive_forms](https://github.com/joanpablo/reactive_forms) - 受 Angular 反应式表单启发，使用模型驱动方法进行表单和验证的 Dart 库。
* [reaktiv](https://github.com/buiapp/reaktiv) - Python 的反应信号具有一流的异步支持，受到 Angular 反应模型的启发。
* [rgenex](https://github.com/asengar14/rgenex) - 用于 React 的 Angular-CLI 风格生成器，可立即搭建组件、挂钩和页面。
* [rxor](https://github.com/nsevendev/rxor) - 受到 Angular Signals、Vue 3 的“ref/compulated”和 SolidJS 的启发，为 React 带来反应式信号。
* [Signals](https://github.com/dmytrodemchenko/Signals) - 使用优化的 Angular 推/拉架构，为 TypeScript 和 JavaScript 提供零依赖性、无故障反应信号。
* [sio](https://github.com/silicia-apps/sio) - Silicia Framework：一种基于 Ionic 的全新方法，旨在简化混合应用程序和网站的开发。
* [UnReact.js](https://github.com/arnvjshi/unreactpjs) - 一个现代框架，结合了 Angular 和 React 的优点，以增强组件通信。
* [use-vue-service](https://github.com/kaokei/use-vue-service) - 受 Angular 服务启发，具有依赖注入的轻量级 Vue 3 状态管理。

## 外部列表

* [awesome-utils-dev](https://github.com/pegaltier/awesome-utils-dev/blob/master/utils-coding/utils-angular-list.md) - 详尽的 Angular 资源——如果您仍然需要更多资源，可以作为后备资源。
* [awesome-angular](https://github.com/DaanDeSmedt/awesome-angular)
* [角企业](https://angular-enterprise.com/en/ngcategory/resources/)
* [framework.dev](https://angular.framework.dev/)
