# 很棒的德诺 [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[<img src=“deno-logo.png”align=“right”宽度=“100”>](https://deno.land)

Deno 是一个简单、现代且安全的 JavaScript 和 TypeScript 运行时，它使用 V8 并用 Rust 构建。

该列表是最好的 Deno 模块和资源的集合。

## 内容

- [Docs](#docs)
  - [官方文档](#official-docs)
  - [外部文档](#external-docs)
- [Modules](#modules)
  - [Automation](#automation)
  - [CLI 实用程序](#cli-utils)
  - [云API](#cloud-apis)
  - [Database](#database)
  - [编辑器框架](#editor-framework)
  - [前端框架](#frontend-framework)
  - [游戏引擎](#game-engine)
  - [Logging](#logging)
  - [机器学习](#machine-learning)
  - [Mail](#mail)
  - [Markdown](#markdown)
  - [Math](#math)
  - [静态站点生成器](#static-site-generator)
  - [字符串实用程序](#string-utils)
  - [社交平台API](#social-platform-apis)
  - [模板引擎](#template-engine)
  - [Testing](#testing)
  - [Utils](#utils)
  - [网页框架](#web-framework)
  - [WebSocket](#websocket)
  - [网络工具](#web-utils)
  - [Webview](#webview)
  - [XML](#xml)
- [Registries](#registries)
- [Showcases](#showcases)
- [Tools](#tools)
- [Integrations](#integrations)
- [Articles](#articles)
- [Blogs/Newsletters](#blogsnewsletters)
- [Presentations](#presentations)
- [Resources](#resources)
  - [Books](#books)
- [其他语言的资源](#resources-in-other-languages)
  - [Chinese](#chinese)
  - [Hebrew](#hebrew)
  - [Indonesian](#indonesian)
  - [Italian](#italian)
  - [Japanese](#japanese)
  - [Korean](#korean)
  - [Russian](#russian)
  - [Spanish](#spanish)
  - [Darija（阿拉伯摩洛哥卡因）](#darija)
  - [库尔德语（中部）](#kurdish-central)

## 文档

### 官方文档

- [Deno API 参考](https://docs.deno.com/api)
- [德诺手册](https://docs.deno.com)
- [Deno 标准库](https://jsr.io/@std)
- [官方网站](https://deno.com)

### 外部文档

- [Deno 的 V8 文档](https://denolib.github.io/v8-docs/)

## 模块

### 自动化
- [swissknife](https://github.com/fakoua/SwissKnife) - SwissKnife - 适用于 Windows 的 Deno Swiss Knife 工具.

### CLI 实用程序
- [cac](https://github.com/cacjs/cac) - 用于构建命令行应用程序的简单而强大的框架。
- [charmd](https://github.com/littletof/charmd) - 适用于您的终端的简单、可扩展的 Markdown 渲染器。
- [cli-spinner](https://github.com/ameerthehacker/deno-cli-spinners) - 运行长时间任务时在终端中显示微调器。
- [cliffy](https://github.com/c4spar/cliffy) - 用于构建交互式命令行工具的完整解决方案。
- [clite](https://github.com/jersou/clite-parser) - 从类自动生成 CLI。
- [commit-sage-cli](https://github.com/AhmedOsman101/commit-sage-cli) - 根据 Git 存储库更改使用 AI 生成常规提交消息。
- [tui](https://github.com/Im-Beast/deno_tui) - 允许轻松创建终端用户界面的模块。
- [yargs](https://github.com/yargs/yargs) - 现代海盗主题的乐观主义者的继承者。

### 云API
- [aws-api](https://aws-api.deno.dev/) - 为 Deno 构建的从头开始 Typescript AWS API 客户端。
- [googleapis](https://googleapis.deno.dev/) - 为 Deno 自动生成的 Google API 客户端。

### 数据库
- [@iuioiua/redis](https://jsr.io/@iuioiua/redis) - 基于 Web Streams API 构建的快速、轻量级 Redis 客户端。
- [aloedb](https://github.com/Kirlovon/aloedb) - 用于 Deno 的轻量、可嵌入、NoSQL 数据库，无需依赖。
- [deno_mongo](https://github.com/denodrivers/mongo) - MongoDB 数据库驱动程序。
- [deno_mysql](https://github.com/denodrivers/mysql) - MySQL 数据库驱动程序。
- [denodb](https://github.com/eveningkid/denodb) - 适用于 Deno 的 MySQL、SQLite、MariaDB、PostgreSQL 和 MongoDB ORM。
- [dongoose](https://github.com/roonie007/dongoose) - 一个简单易用的 Deno KV ORM。
- [maxminddb](https://github.com/josh-hemphill/maxminddb-wasm) - 支持使用 MaxmindDB geoIP 数据库文件的库
- [nessie](https://github.com/halvardssm/deno-nessie) - 为 PostgreSQL、MySQL 和 SQLite 创建、迁移和回滚迁移。
- [postgres](https://github.com/denodrivers/postgres) - PostgreSQL 数据库的驱动程序。
- [redis](https://github.com/denodrivers/redis) - deno 的 redis 客户端的实验性实现。
- [yongo](https://github.com/yooneskh/yongo) - deno 中 Mongoose api 的子集（如 populate），但不会完全复制 mongoose

### 编辑器框架

- [Denops](https://github.com/vim-denops/denops.vim) - 🐜 使用 Deno 编写 Vim/Neovim 插件的生态系统。

### 前端框架
- [fresh](https://github.com/denoland/fresh) - 下一代网络框架。
- [packup](https://github.com/kt3k/packup) - 适用于 Deno 的零配置 Web 应用程序打包器。
- [ultra](https://github.com/exhibitionist-digital/ultra) - 💎 Deno 中的现代流式 React 框架。

### 游戏引擎
- [caviar](https://github.com/load1n9/caviar) - ⚡ 速度极快、现代的游戏引擎，由适用于 Deno 和浏览器的 WebGPU 提供支持
- [sdl2](https://github.com/littledivy/deno_sdl2) - Deno 的 SDL2 模块

### 图片
- [ImageScript](https://github.com/matmen/ImageScript) - JavaScript 中的图像处理，利用 WebAssembly 提高性能。
- [monke](https://github.com/retraigo/monke) - 带有额外图像过滤器（模糊、反转等）的颜色量化和抖动库。

### 记录
- [LogTape](https://github.com/dahlia/logtape) - Deno/Node.js/Bun/浏览器零依赖的简单日志库。

### 机器学习
- [appraisal](https://github.com/retraigo/appraisal) - 特征提取和转换。
- [classy-lala](https://github.com/retraigo/la-classy) - 用于监督学习任务的单层感知器。
- [netsaur](https://github.com/denosaurs/netsaur) - 由 WebGPU 加速的强大机器学习

### 邮件
- [deno-smtp](https://github.com/manyuanrong/deno-smtp) - deno 的 smtp 邮件发送器。

### 降价
- [LiteMarkup](https://github.com/tuures/LiteMarkup) - AST 优先解析器。 gzip 压缩后大小低于 3 KB，零依赖性。

### 数学
- [neo](https://github.com/denosaurs/neo/) - 矩阵和其他数学，由 WebGPU 加速

### 静态站点生成器
- [lume](https://github.com/lumeland/lume) - 类似于 Jekyll 或 Eleventy 的静态站点生成器，支持多种文件格式。
- [pagic](https://github.com/xcatliu/pagic) - 从 Markdown 生成静态 html 页面的最简单方法，使用 Deno 构建。

### 字符串实用程序
- [written](https://github.com/vixalien/written) - A 提供了一组用于操作文本的实用程序，重点是提供排版工具而不是纯粹的字符串操作。

### 社交平台API
- [discordeno](https://github.com/discordeno/discordeno) - Deno 的 Discord API 库
- [grammY](https://github.com/grammyjs/grammY) - Deno 的 Telegram Bot API 框架。
- [MTKruto](https://github.com/MTKruto/MTKruto) - 用于 Telegram MTProto API 的 Deno-first 跨运行时客户端库。


### 模板引擎
- [dejs](https://github.com/syumai/dejs) - deno 的 Ejs 模板引擎。
- [eta](https://github.com/bgub/eta) - 快速、轻量级且可配置的嵌入式模板引擎。
- [handlebars](https://github.com/alosaur/handlebars) - deno 的车把模板引擎

### 测试
- [deno-puppeteer](https://github.com/lucacasonato/deno-puppeteer) - 一个库，提供高级 API 以通过 DevTools 协议控制 Chromium 或 Chrome。
- [qunitx](https://github.com/izelnakri/qunitx) - 零依赖、完全可定制、成熟、通用的测试 API，可以使用默认运行时测试运行器在 Node.js、Deno 和浏览器中互换运行。
- [rhum](https://github.com/drashland/rhum) - Deno 的轻量级测试框架。
- [superdeno](https://github.com/cmorten/superdeno) - 用于测试 Deno HTTP 服务器的超级代理驱动库。
- [superoak](https://github.com/cmorten/superoak) - 通过 SuperDeno，Oak 的 HTTP 断言变得简单。
- [tepi](https://deno.land/x/tepi) - .http 测试运行程序
- [unexpected](https://github.com/unexpectedjs/unexpected) - 可扩展的 BDD 断言工具包。

### 实用工具
- [buckets](https://github.com/jacoborus/deno-buckets) - 将资源和脚本捆绑在一个可执行文件中。
- [colors](https://github.com/retraigo/colors) - TypeScript 中的颜色转换和操作。
- [computed_types](https://github.com/neuledge/computed-types) - Joi 类似于 Typescript 和 Deno 的验证器。
- [croner](https://github.com/Hexagon/croner) - Cron 库具有高级调度功能、文档齐全的 API 和零依赖性。
- [deno-config](https://github.com/yooneskh/deno-unified-config) - 通过 cli、.env 和 json 文件简化 deno 应用程序配置管理的实用程序
- [deno_kv_fs](https://github.com/hviana/deno_kv_fs) Deno KV 文件系统，与 Deno 部署兼容。使用 Web Streams API。
- [denon](https://github.com/denosaurs/denon/blob/master/mod.ts) - 带有等待生成器的文件观察器。
- [dinoenv](https://deno.land/x/dinoenv) - 使用 deno 管理环境变量的小型库。
- [durationjs](https://github.com/retraigo/duration.js) - 从时间戳或人类可读的字符串中获取格式化的持续时间。
- [envapt](https://github.com/materwelonDhruv/envapt) - 使用内置转换器、标准架构验证和零依赖性将环境变量读取为键入值。
- [esm-itter](https://github.com/tillsanders/esm-itter) - 流行的 EventEmitter3 的强类型分支，重点关注 EcmaScript 模块语法、TypeScript 和现代工具。
- [evt](https://github.com/garronej/evt) - 输入 EventEmitter 的安全替换。
- [fastest-validator](https://github.com/icebob/fastest-validator) - 适用于所有 JavaScript 平台的模式验证器
- [fortuna](https://github.com/retraigo/fortuna) - 加权扭蛋系统。
- [garn-validator](https://github.com/jupegarnica/garn-validator) - 轻松创建验证。
- [locale-kit](https://deno.land/x/localekit) ([GitHub](https://github.com/locale-kit/locale-kit)) - 一个国际化/本地化/翻译 (i18n/l10n/t9n) 库，带有 Fresh 包装器并支持复数和动态替换。
- [optionals](https://github.com/OliverBrotchie/optionals) - 类似 Rust 的错误处理和具有详尽模式匹配的选项。
- [PLS](https://github.com/xorgram/pls) - 使用 2 行将 localStorage 持久保存在任何数据库中，包括但不限于 MongoDB、PostgreSQL 和 Redis。
- [qrcode](https://github.com/denorg/qrcode) - Deno 的 QR 码图像生成器。
- [rubico](https://github.com/a-synchronous/rubico) - 🏞 [a]同步函数组合；它就是有效的。
- [solc](https://github.com/deno-web3/solc) - 💎 Deno 的 Solidity 绑定。
- [switcher4deno](https://github.com/switcherapi/switcher-client-deno) - 用于 Switcher-API 的功能标记 Deno SDK 客户端。
- [wu-diff-js](https://github.com/bokuweb/wu-diff-js) - 一个 diff 库，使用 wu(the O(NP)) 算法计算两个切片之间的差异。

### 验证

- [zod](https://github.com/colinhacks/zod) - 使用静态类型推断进行 TypeScript 优先模式验证。

### 网页框架
- [alosaur](https://github.com/alosaur/alosaur) - Alosaur - 具有许多 ES 装饰器的 Deno Web 框架。
- [aqua](https://github.com/predetermined/aqua) - 一个最小且快速的 Deno Web 框架。
- [danet](https://github.com/Savory/Danet) - Deno 的 Savory Web 框架深受 [Nest.js](https://nestjs.com) 的启发。
- [drash](https://github.com/drashland/drash) - 零依赖的 Deno HTTP 服务器的 REST 微框架。
- [faster](https://github.com/hviana/faster) - 一个快速且优化的中间件服务器，具有一组有用的中间件。
- [faster_react](https://github.com/hviana/faster_react) - 采用 React + Faster 的全栈 Web 框架。与 Deno Deploy 完全兼容。
- [hono](https://github.com/honojs/hono) - 适用于 Cloudflare Workers、Deno 和 Bun 的超快 Web 框架。快，但不仅仅是快。
- [oak](https://github.com/oakserver/oak) - Deno 网络服务器的中间件框架。
  - [oak-http-proxy](https://github.com/cmorten/oak-http-proxy) - Deno Oak HTTP 服务器的代理中间件。
  - [oak-routing-ctrl](https://github.com/Thesephi/oak-routing-ctrl) - TypeScript 装饰器可通过 Oak 框架轻松搭建 API 服务。
- [opine](https://github.com/cmorten/opine) - 从 ExpressJS 移植的快速、简约的 Web 框架。
  - [opine-http-proxy](https://github.com/cmorten/opine-http-proxy) - Deno Opine HTTP 服务器的代理中间件。

### WebSocket
- [dropper](https://github.com/denyncrawford/dropper-deno) - 用于在 Deno 上构建实时应用程序的自定义基于事件的 WebSockets 框架 🦕
- [wocket](https://github.com/drashland/wocket) - Deno 的 WebSocket 库。

### 网络工具
- [djwt](https://github.com/Zaubrik/djwt) - 根据 JWT 和 JWS 规范在 Deno 上制作 JSON Web Tokens (JWT)。
- [forwarded](https://github.com/deno-libs/forwarded) - `forwarded` 库的 Deno 端口。
- [fresh_chart](https://github.com/denoland/fresh_charts) - Fresh 的服务器端渲染图表库。
- [gentleRpc](https://github.com/timonson/gentle_rpc) - 用于 Deno 和浏览器的 JSON-RPC 2.0 TypeScript 库。
- [gql](https://github.com/deno-libs/gql) - 通用 GraphQL HTTP 中间件。
- [graphql-tag](https://github.com/deno-libs/graphql_tag) - 来自模板文字的 GraphQL 模式 AST。
- [nats](https://github.com/nats-io/nats.deno) - [NATS 消息系统](https://nats.io/) 的 Deno 客户端。
- [obsidian](https://github.com/open-source-labs/obsidian) - 原生 GraphQL 缓存客户端和服务器模块。
- [react-icons](https://react-icons.deno.dev/) - React 图标转换为 preact 以实现 deno fresh。
- [router](https://github.com/zhmushan/router) - 高性能基本路由器可以在任何地方工作。
- [rpc](https://github.com/deno-libs/rpc) - Deno 的 JSONRPC 服务器实现。
- [ts-prometheus](https://github.com/marcopacini/ts_prometheus) - 普罗米修斯客户端。

### 网页视图
- [webview](https://github.com/webview/webview_deno) - Deno 绑定 webview，一个用于创建基于 Web 的桌面 GUI 的小型库。

### XML
- [sax-ts](https://github.com/Maxim-Mazurok/sax-ts) - 从 [sax-js](https://github.com/isaacs/sax-js) 移植的 SAX 样式 XML 解析器。

## 登记处

- [crux.land](https://crux.land/) - 一个免费的注册表服务，用于托管小型（< 10kB）单 deno 脚本。
- [Deno PKG](https://denopkg.com/) - 在 Deno 项目中使用 GitHub 代码的更简单方法。
- [deno.land/x/](https://deno.land/x/) - 官方第 3 方模块注册表。
- [nest.land](https://nest.land) - 一个不可变的、由区块链驱动的 Deno 包注册表。 🥚

## 展示柜

- [Deno Rest](https://github.com/Prolifode/deno_rest) - deno RESTful api 的样板。
- [Edrys](https://github.com/edrys-org/edrys) - 远程教学软件
- [GitHub Profile Trophy](https://github.com/ryo-ma/github-profile-trophy) - 🏆 在自述文件中添加动态生成的 GitHub Trophy
- [ShopSavvy Deno Deploy](https://github.com/shopsavvy/deno-deploy-shopsavvy) - Deno 与 Hono 一起部署路由器，用于产品搜索、实时定价和价格历史记录。
- [The Official Showcase](https://deno.land/showcase) - Deno 的官方展示。
- [UsingDeno](https://usingdeno.com) - 使用 Deno 🦕 的 Web 应用程序和项目的精选列表。

## 工具

- [clone](https://github.com/ekaragodin/clone) - 一个用于方便克隆的简单实用程序。
- [denoflow](https://github.com/denoflow/denoflow) - 配置即代码，使用 YAML 编写在 Deno 上运行的自动化工作流程，以及任何 Deno 模块、Typescript/Javascript 代码
- [denoify](https://github.com/garronej/denoify) - 对于想要支持 Deno 但不想编写和维护端口的 NPM 模块作者。
- [denoliver](https://github.com/joakimunge/denoliver) - 一个简单、无依赖性的文件服务器，具有实时重新加载功能。
- [denomander](https://github.com/siokas/denomander) - Deno 命令行界面的灵感来自 Commander.js。
- [denon](https://github.com/denosaurs/denon) - 守护进程脚本运行程序，例如 nodemon。内置并适用于 Deno。
- [denopendabot](https://github.com/apps/denopendabot) - Deno 项目的 Dependabot。
- [denopkg](https://github.com/egoist-labs/denopkg.com) - 在 Deno 项目中使用 GitHub 代码的更简单方法。
- [Deno Dig](https://github.com/theGEBIRGE/DenoDig) - 用于从独立 Deno 可执行文件中提取应用程序代码和 npm 包的工具。
- [deno_docker](https://github.com/denoland/deno_docker) - Deno 的最新 dockerfiles 和镜像 - alpine、centos、debian、ubuntu。
- [dmm](https://github.com/drashland/dmm) - 轻量级 Deno 模块管理器
- [dnt](https://github.com/denoland/dnt) - Deno 到 npm 包构建工具。
- [dpm](https://github.com/dpmland/dpm) - Deno 包管理器，一个 NPM | Deno 的 Yarn 体验
- dvm
  - [asdf-community/asdf-deno](https://github.com/asdf-community/asdf-deno) - [asdf](https://asdf-vm.com/) 的 Deno 插件
  - [justjavac/dvm](https://github.com/justjavac/dvm) - Deno Version Manager：管理多个活动的 Deno 版本。
  - [axetroy/dvm](https://github.com/axetroy/dvm) - 没有运行时依赖的 Deno 版本管理器。
  - [ghosind/dvm](https://github.com/ghosind/dvm) - 适用于 Linux/MacOS 的轻量级 Deno 版本管理器。
- [entype](https://github.com/bcheidemann/entype) - 用于为序列化数据生成类型定义的 CLI 工具，目前支持 JSON 到 Rust 和 TypeScript。
- [kopo-cli](https://github.com/littletof/kopo-cli) - 终端中的 Deno 注册表浏览器。
- [make-deno-edition](https://github.com/bevry/make-deno-edition) - 自动使 package.json 项目（例如 npm 包和 node.js 模块）与 Deno 兼容。
- [pup](https://github.com/Hexagon/pup) - Deno 的高级流程管理器。具有自动重启、fs watch、cron 启动、进程遥测、ipc、集群、负载均衡器等功能。
- [studio-pack-generator](https://github.com/jersou/studio-pack-generator) - 将文件夹或 RSS URL 转换为 Lunii 设备的 Studio 包
- [trex](https://github.com/crewdevio/Trex) - 包管理类似于 deno 的 npm。
- [udd](https://github.com/hayd/deno-udd) - 更新 Deno 依赖项：将导入语句更新为最新发布的版本。
- [vscode-deno](https://github.com/denoland/vscode_deno) - VS Code 扩展，使用“TypeScript Deno 语言服务插件”提供 Deno 支持。

## 集成

- [Netlify Edge Functions](https://docs.netlify.com/edge-functions/overview/) - Edge Functions 连接 Netlify 平台和工作流程。
- [Slack Custom Functions](https://api.slack.com/future/functions/custom) - 使用 Deno 构建自定义 Run On Slack 函数。
- [Smallweb](https://www.smallweb.run/) - 包含在单个目录中的个人云。您可以使用 Deno 自定义服务器行为。
- [Supabase Edge Functions](https://supabase.com/docs/guides/functions) - 边缘函数是服务器端 TypeScript 函数，分布在边缘的全局范围内。
- [Astro](https://docs.astro.build/en/guides/deploy/deno/) - 将服务器端渲染的 Astro 站点部署到 Deno Deploy。

## 博客/时事通讯
- [Craig's Deno Diary](https://deno-blog.com) - 专注于 Deno 技术和 lib howtos 的博客。
- [Deno Blog](https://deno.com/blog) - Deno 公司的官方博客。
- [Deno News](https://deno.news) - Deno 文章、新闻和酷项目的时事通讯。

## 文章

- [使用 Deno 和 Visual Studio Code 进行开发](https://medium.com/@kitsonk/develop-with-deno-and-visual-studio-code-225ce7c5b1ba)
- [关于 JavaScript/TypeScript 运行时 Deno 的初步想法](https://43081j.com/2019/01/first-look-at-deno)
- [Deno 入门](https://dev.to/wuz/getting-started-with-deno-e1m)
- [什么是 Deno，它与 Node.js 有何不同？](https://dev.to/bnevilleoneill/what-s-deno-and-how-is-it-different-from-node-js-366g)
- [使用 Deno 编写一个小型 API](https://dev.to/kryz/write-a-small-api-using-deno-1cl0)
- [Cloud Run 上的 Deno](https://medium.com/google-cloud/deno-on-cloud-run-89ae64d1664d)
- [学习 Deno：聊天应用程序](https://aralroca.com/blog/learn-deno-chat-app)
- [从 Node 到 Deno](https://dev.to/aralroca/from-node-to-deno-5gpn)
- [使用 Deno 创建一个简单的笔记应用程序](https://dev.to/jeferson_sb/create-a-simple-note-taking-app-with-deno-3k7g)
- [使用 Deno、Oak 和 MYSQL 构建 API](https://codeforgeek.com/building-api-server-using-deno-and-mysql/)
- [使用 Deno 创建您的第一个 News CLI 应用](https://medium.com/javascript-in-plain-english/creating-your-first-news-cli-app-using-deno-e1470398c627)
- [与 Deno 持续集成](https://semaphoreci.com/blog/continuous-integration-with-deno)
- [Deno 隐藏的超能力：xeval](https://stefanbuck.com/blog/hidden-superpower-deno-xeval)
- Deno REST API 与 Oak 教程系列 [0](https://www.robinwieruch.de/deno-tutorial)、[1](https://www.robinwieruch.de/deno-oak)、[2](https://www.robinwieruch.de/deno-oak-rest-api)
- [Deno 入门](https://sabe.io/tutorials/getting-started-with-deno)
- [如何使用 Docker 部署 Deno 应用程序](https://sabe.io/tutorials/how-to-deploy-deno-app-docker)

## 演讲

- [关于 Node.js 我后悔的 10 件事 - Ryan Dahl - JSConf EU 2018](https://www.youtube.com/watch?v=M3BM9TB-8yA)
  - [Slides](https://tinyclouds.org/jsconf2018.pdf)
- [JSDC 2018#A01 - Deno，一个新的服务器端运行时 作者：Ryan Dahl](https://www.youtube.com/watch?v=FlTG0UXRAkE)
- [瑞恩·达尔. Deno，一种 JavaScript 的新方式。 JS节2019春季](https://www.youtube.com/watch?v=z6JRlx5NC9E)
  - [Slides](https://www.slideshare.net/JSFestUA/js-fest-2019-ryan-dahl-deno-a-new-way-to-javascript)
- [Rafał Pocztarski — 从 Node.js 到 Deno - 使用 V8 和 Rust 构建的 JavaScript/TypeScript 运行时 [EN]](https://www.youtube.com/watch?v=Aib1OZLy0_c)
- [Ryan Dahl：JavaScript 和 TypeScript 的安全运行时 | js.la 2019 年 4 月](https://www.youtube.com/watch?v=RAmqgbv247s)
  - [Slides](https://docs.google.com/presentation/d/1CSQVTeH5tFzE4AZVXIpx9Xwew5YS-gxJZ03eRFtNeIc/edit)
- [Ryan Dahl：Deno，JavaScript 的新方式 - HolyJS 2019 Piter](https://www.youtube.com/watch?v=HjdJzNoT_qg)
  - [Slides](https://docs.google.com/presentation/d/1BjvZx5S8noVfFINptH4jfKfqh9jB9nXlFC0I3oIDtg4/edit)
- [Rafał Pocztarski - 什么是 Deno？ 2020 年代现代 JavaScript 和 TypeScript 后端的新运行时 - Deno Warsaw](https://www.youtube.com/watch?v=aI5A9zvYSjk)
- [Michał Sabiniarz - 如何为 Deno 做出贡献？ - 德诺华沙](https://www.youtube.com/watch?v=LAtjnKLbPpw)
- [Bartek Iwańczuk - Deno 内部结构，如何构建现代运行时 - Deno Warsaw](https://www.youtube.com/watch?v=qt7fbmypAFk)
  - [Slides](https://docs.google.com/presentation/d/1LYNGpyjx9PemL-P__7hVC8mSqkX-jL8VQLMhCRehy00/edit?usp=sharing)
- [Ryan Dahl 和 Kitson Kelly：Deno 是 JavaScript 的新方式 - TSConf 2019](https://www.youtube.com/watch?v=1gIiZfSbEAE)
- [Bert Belder - Deno - dotJS 2019](https://www.youtube.com/watch?v=puXyo1jGQys)
- [Kitson P. Kelly - Deno 和 JavaScript 运行时的未来 - CityJS Conf 2020](https://www.youtube.com/watch?v=2eRyZpX4qvI)
- [Matías Insaurralde - Deno：V8 互操作性的实验方法 [EN 字幕] - NodeConf Argentina 2019](https://www.youtube.com/watch?v=N0BRE-0n2cU)
  - [Slides](https://speakerdeck.com/matiasinsaurralde/deno-an-experimental-approach-on-v8-interoperability)

## 资源

### 书籍
- [使用 Deno 进行现代 Web 开发](https://bpbonline.com/products/modern-web-development-with-deno)

## 其他语言的资源

### 中文

- [Deno 并不是下一代 Node.js](https://juejin.im/post/5b14a390e51d4506c1300bbc)
- [玩 Deno 遇到问题的解决方案](https://juejin.im/post/5b1245b3f265da6e4c6cf249)
- [让我们一起来学习别人学不动的 Deno](https://segmentfault.com/a/1190000015151287)
- [Node zh-CN 中的设计错误](https://zhuanlan.zhihu.com/p/37637923)
- [Node之父ry：Node中的设计错误](https://mp.weixin.qq.com/s/7XAiYw18c8YZc-fXk0-wrw)
- [Node之父 - Deno，一个新的JS运行时](https://www.bilibili.com/video/av52038617)

### 希伯来语

- [希伯来语 Deno 简介（英语幻灯片）](https://www.youtube.com/watch?v=9tJ_LkI6_qw)

### 印度尼西亚语

- [伯克纳兰·登甘·德诺](https://medium.com/@redhajuanda/berkenalan-dengan-dengan-deno-c48cdf3aa31e)
- [安装和安装的注意事项](https://youtu.be/V_kpUTJSd9c)
- [Deno Land 印度尼西亚电报群](https://t.me/deno_id)

### 意大利语

- [Deno - 节点字谜](https://www.slideshare.net/FrancescoSciuti/deno-lanagramma-di-node)

### 日语

- [deno-ja](https://deno-ja.deno.dev/) - Deno 日本用户组。
- [Node.js における設計ミス By Ryan Dahl](https://yosuke-furukawa.hatenablog.com/entry/2018/06/07/080335)
- [mizchi/deno_code_reading.md](https://gist.github.com/mizchi/31e5628751330b624a0e8ada9e739b1e)
- [Node 和 Deno 中的设计错误 #kng5 / deno](https://speakerdeck.com/masashi/deno)
- [Dive into Deno：プロセス起動からTypeScriptが実行されるまで](https://blog.leko.jp/post/code-reading-of-deno-boot-process/)

### 韩语

- [Deno Korea](https://deno.kr/) - Deno 韩国用户组。

### 俄语

- [电报频道](https://t.me/denoland_ru)
- [电报聊天](https://t.me/denoland)

### 西班牙语

- [你好，德诺！ 。 🦕](https://medium.com/javascript-espa%C3%B1ol/hola-deno-f31f9f6f2c84)
- [使用 Deno 来创建 API REST](https://medium.com/@mpampols/as%C3%AD-puedes-crear-tu-primera-api-rest-con-deno-a9094ee5c0b2)
- [NodeJS 与 Rust 和 TypeScript 的继承者](https://medium.com/@manurua/primeros-pasos-con-deno-el-nuevo-nodejs-desarrollado-con-rust-y-typescript-b9ac14f7d0c7)
- [底漆 vistazo con den](https://dev.to/buttercubz/first-look-with-deno-spanish-30dh)

### 达里贾

- [初看 Deno | BlaBlaConf 2021 🇲🇦](https://www.youtube.com/watch?v=Y_etUvzAa4s)

### 库尔德语（中部）

- [Deno 的简短介绍](https://devs.krd/about-deno)
