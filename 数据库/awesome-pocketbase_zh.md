# 很棒的 PocketBase [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

![GitHub forks](https://img.shields.io/github/stars/benallfree/awesome-pocketbase?style=flat) ![GitHub forks](https://img.shields.io/github/forks/benallfree/awesome-pocketbase?style=flat) ![GitHub forks](https://img.shields.io/github/contributors/benallfree/awesome-pocketbase?style=flat)

> 精选的 [PocketBase](https://pocketbase.io) 资源列表。

PocketBase 是一个开源后端，由具有实时订阅功能的嵌入式数据库 (SQLite)、内置身份验证管理、方便的仪表板 UI 和简单的 REST-ish API 组成。

## 内容

- [官方套餐](#official-packages)
- [顶级 PocketBase 特定项目（\>100 颗星）](#top-pocketbase-specific-projects-100-stars)
- [主要社区项目](#major-community-projects)
- [JSVM 插件](#jsvm-plugins)
- [去插件](#go-plugins)
- [React](#react)
- [Svelte](#svelte)
- [Vue](#vue)
- [Solid](#solid)
- [Dart/Flutter](#dartflutter)
- [C#](#c)
- [D](#d)
- [Node.js](#nodejs)
- [非官方 PocketBase 客户端 (SDK)](#unofficial-pocketbase-clients-sdks)
- [自托管](#self-hosting)
- [TypeScript 工具](#typescript-tools)
- [SQLite工具](#sqlite-tools)
- [其他工具](#other-tools)
- [Showcases](#showcases)
- [PocketPorts 套餐](#pocketports-packages)

## 官方套餐

- [Golang Server](https://github.com/pocketbase/pocketbase/releases/) - 主要的 PocketBase 服务器。 ![GitHub Repo 星星](https://img.shields.io/github/stars/pocketbase/pocketbase)

- [JavaScript SDK](https://github.com/pocketbase/js-sdk) - 用于与 PocketBase API 交互的浏览器和 Node.js。 ![GitHub Repo 星星](https://img.shields.io/github/stars/pocketbase/js-sdk)
- [Dart SDK](https://github.com/pocketbase/dart-sdk) - 用于与 PocketBase Web API 交互的多平台 SDK。 ![GitHub Repo 星星](https://img.shields.io/github/stars/pocketbase/dart-sdk)

## 顶级 PocketBase 特定项目（>100 星）

- [pockethost.io](https://pockethost.io) - 专业 PocketBase 托管。 ![GitHub Repo 星星](https://img.shields.io/github/stars/pockethost/pockethost)
- [PocketBase Typegen](https://github.com/patmood/pocketbase-typegen) - 从 SQLite db 文件生成 TypeScript 类型。 ![GitHub Repo 星星](https://img.shields.io/github/stars/patmood/pocketbase-typegen)
- [PocketBase Docker](https://github.com/muchobien/pocketbase-docker) - Docker 设置支持多种架构，并随 PocketBase 版本自动更新。 ![GitHub Repo 星星](https://img.shields.io/github/stars/muchobien/pocketbase-docker)
- [PocketBase+Stripe](https://github.com/mrwyndham/pocketbase-stripe) - 扩展 PocketBase 以进行 Stripe 订阅集成。 ![GitHub Repo 星星](https://img.shields.io/github/stars/mrwyndham/pocketbase-stripe)
- [PocketBase+Lemonsqueezy](https://github.com/mrwyndham/pocketbase-lemonsqueezy) - 扩展 PocketBase 以实现 Lemonsqueezy 订阅集成。 ![GitHub Repo 星星](https://img.shields.io/github/stars/mrwyndham/pocketbase-lemonsqueezy)
- [SvelteKit Starter](https://github.com/spinspire/pocketbase-sveltekit-starter) - 入门套件展示了如何使用定制的 PocketBase 作为 SvelteKit 前端的后端。 ![GitHub Repo 星星](https://img.shields.io/github/stars/spinspire/pocketbase-sveltekit-starter)
- [SvelteKit Auth](https://github.com/danawoodman/sveltekit-auth-example) - 该项目被设计为使用 SvelteKit 获取身份验证设置的示例实现参考。 ![GitHub Repo 星星](https://img.shields.io/github/stars/danawoodman/sveltekit-auth-example)
- [SvelteKit PocketBase Auth](https://github.com/jianyuan/pocketbase-sveltekit-auth) - 带有示例的演示登录和注册页面。 ![GitHub Repo star](https://img.shields.io/github/stars/jianyuan/pocketbase-sveltekit-auth)

## 主要社区项目

- [pocketpages.dev](https://pocketpages.dev) - 服务器端 JS 页面和 PocketBase 托管。 ![GitHub Repo 星星](https://img.shields.io/github/stars/benallfree/pocketpages)
- [pocodex.dev](https://pocodex.dev) - 非官方的 PocketBase 插件存储库和代码交换。 ![GitHub Repo 星星](https://img.shields.io/github/stars/benallfree/pocodex)
- PocketPorts - NPM/Node.js 包移植到 PocketBase JSVM。官方列表托管在 Awesome-pocketbase 中。

## JSVM 插件

- [pocketbase-otp](https://github.com/benallfree/pocketbase-otp) - <=v0.22.\* 的一次性密码！[GitHub 存储库 star](https://img.shields.io/github/stars/benallfree/pocketbase-otp)
- [pocketpages](https://github.com/benallfree/pocketpages) - PocketBase 的服务器端 EJS 页面。 ![GitHub Repo 星星](https://img.shields.io/github/stars/benallfree/pocketpages)
- [pocketbase-presigned-urls](https://github.com/benallfree/pocketbase-presigned-urls) - 从预先签名的 S3 URL 提供文件上传服务。 ![GitHub Repo 星星](https://img.shields.io/github/stars/benallfree/pocketbase-presigned-urls)

## 去插件

- [Telegram auth](https://github.com/iamelevich/pocketbase-plugin-telegram-auth) - 添加 Telegram 身份验证（小组件按钮和 WebApp）。 ![GitHub Repo 星星](https://img.shields.io/github/stars/iamelevich/pocketbase-plugin-telegram-auth)
- [Ngrok](https://github.com/iamelevich/pocketbase-plugin-ngrok) - 使用 ngrok 将本地 PocketBase 公开到互联网。 ![GitHub Repo 星星](https://img.shields.io/github/stars/iamelevich/pocketbase-plugin-ngrok)
- [Proxy](https://github.com/iamelevich/pocketbase-plugin-proxy) - 将请求转发到另一台主机。当您想使用单独的服务器作为前端（如 Next.js），但使用相同的端口提供所有服务时，这可能很有用。 ![GitHub Repo 星星](https://img.shields.io/github/stars/iamelevich/pocketbase-plugin-proxy)
- [Webhooks](https://gist.github.com/cugu/9e74f75dcad3df74370c71ff3c02085a) - 在管理 UI 中添加 Webhook 支持，以通过 POST 请求向其他系统发送所选集合上的“创建”、“更新”和“删除”事件。
- [TypeScript Generator](https://github.com/Vogeslu/pocketbase-ts-generator) - 生成 TypeScript 类型的独立工具或库，具有自动生成挂钩或命令。 ![GitHub Repo 星星](https://img.shields.io/github/stars/Vogeslu/pocketbase-ts-generator)
- [pocketbase-gogen](https://github.com/Snonky/pocketbase-gogen) - 从 PocketBase 模式生成数据模型结构。 ![GitHub Repo 星星](https://img.shields.io/github/stars/Snonky/pocketbase-gogen)
- [pb-ext](https://github.com/magooney-loon/pb-ext) - 增强的 PocketBase 服务器，具有监控、日志记录和 API 文档。 ![GitHub Repo 星星](https://img.shields.io/github/stars/magooney-loon/pb-ext)

## 反应

- [PocketBase React](https://github.com/tobicrain/pocketbase-react) - 用于与 PocketBase JavaScript SDK 交互的非官方 React SDK（React、React Native、Expo）。 ![GitHub Repo 星星](https://img.shields.io/github/stars/tobicrain/pocketbase-react)
- [PocketBase Next.js App Template](https://github.com/tsensei/nextjs-pocketbase-starter-template) - PocketBase Next.js 模板，带有使用 cookie 的服务器和浏览器客户端。 ![GitHub Repo 星星](https://img.shields.io/github/stars/tsensei/nextjs-pocketbase-starter-template)
- [Next.js PocketBase Auth](https://github.com/jianyuan/pocketbase-nextjs-auth) - 示例 Next.js 15 应用程序与 PocketBase 集成、类型化客户端、服务器端和客户端渲染技术以及服务器操作。 ![GitHub Repo star](https://img.shields.io/github/stars/jianyuan/pocketbase-nextjs-auth)
- [next-pocketbase-auth](https://github.com/g12i/next-pocketbase-auth) - Next.js 应用程序的轻量级身份验证包装器，提供易于使用的实用程序来处理客户端和服务器组件中的用户会话。 ![GitHub Repo 星星](https://img.shields.io/github/stars/g12i/next-pocketbase-auth)
- [pbtsdb](https://github.com/nathanstitt/pbtsdb) - 类型安全的 TanStack DB 适配器，可轻松创建具有实时订阅的 LiveQueries。 ![GitHub Repo 星星](https://img.shields.io/github/stars/nathanstitt/pbtsdb)

## 斯韦尔特

- [svelte-query-pocketbase](https://github.com/goknsh/svelte-query-pocketbase) - TanStack 查询包装器围绕 PocketBase for Svelte 和 SvelteKit，实时更新查询缓存。 ![GitHub Repo 星星](https://img.shields.io/github/stars/goknsh/svelte-query-pocketbase)
- [pocketbase-sveltekit-starter](https://github.com/spinspire/pocketbase-sveltekit-starter) - 入门套件展示了如何使用定制的 (Go/JS) PocketBase 作为 SvelteKit 前端的后端。 ![GitHub Repo 星星](https://img.shields.io/github/stars/spinspire/pocketbase-sveltekit-starter)
- [pocketbase-sveltekit-static](https://github.com/Egor-S/pocketbase-sveltekit-static) - 具有配置授权的简约模板，具有用于部署的单个 Docker 映像（55 MB 起）。 ![GitHub Repo 星星](https://img.shields.io/github/stars/Egor-S/pocketbase-sveltekit-static)

## 维埃

- [Vue 3 + Vite starter kit](https://github.com/StefanVDWeide/pocketbase-vue) - Vue 3 + Vite + PocketBase 的入门套件。 ![GitHub Repo 星星](https://img.shields.io/github/stars/StefanVDWeide/pocketbase-vue)
- [Tutorial](https://studioterabyte.nl/en/blog/pocketbase-vue-3) - Vue 3 教程。
- [Quasar starter kit](https://github.com/aaronblondeau/pocketbase_quasar_starter) - 带有类星体的 Pocketbase。 ![GitHub Repo 星星](https://img.shields.io/github/stars/aaronblondeau/pocketbase_quasar_starter)
- [PocketNuxt](https://github.com/j-wil/pocket-nuxt) - 构建为单个二进制文件的 Nuxt3 PocketBase 启动器。 ![GitHub Repo 星星](https://img.shields.io/github/stars/j-wil/pocket-nuxt)

## 固体

- [Solid-pocketbase-hooks](https://github.com/kirill-dev-pro/solid-pocketbase-hooks) - Solid.js 的 Pocketbase 挂钩！[GitHub 存储库星星](https://img.shields.io/github/stars/kirill-dev-pro/solid-pocketbase-hooks)

## 飞镖/颤动

- [PocketBase Drift](https://github.com/rodydavis/pocketbase_drift) - 使用 Drift 缓存的 PocketBase 客户端。 ![GitHub Repo 星星](https://img.shields.io/github/stars/rodydavis/pocketbase_drift)
- [Dart Generator](https://github.com/rodydavis/pocketbase_dart_generator) - 生成类型安全的客户端 SDK 以在本地 SQLite、JSON 或 GraphQL 解析器中使用。 ![GitHub Repo 星星](https://img.shields.io/github/stars/rodydavis/pocketbase_dart_generator)
- [PocketBase Server Flutter](https://github.com/rohitsangwan01/pocketbase_server_flutter) - 一个 Flutter 插件，可直接从 Android/iOS 运行 PocketBase 服务器。 ![GitHub Repo 星星](https://img.shields.io/github/stars/rohitsangwan01/pocketbase_server_flutter)

## C#

- [ORM and code generator](https://github.com/iluvadev/PocketBaseClient-csharp) - 用于管理 PocketBase 应用程序的 ORM。 ![GitHub Repo 星星](https://img.shields.io/github/stars/iluvadev/PocketBaseClient-csharp)
- [PocketBaseSharp](https://github.com/PSCourtney/PocketBaseSharp) - 适用于 PocketBase 的 C# SDK 和演示 Blazor WebAssembly web 应用程序。 ![GitHub Repo 星星](https://img.shields.io/github/stars/PSCourtney/PocketBaseSharp)

## D

- [libpb](https://github.com/Hax-io/libpb) - D 的 PocketBase 客户端包装器，具有与 JSON 之间的自动序列化和反序列化功能。 ![GitHub Repo 星星](https://img.shields.io/github/stars/Hax-io/libpb)

## Node.js

- [gobot](https://github.com/benallfree/gobot) - PocketBase 作为 npm 包。 CLI 和 API。 ![GitHub Repo 星星](https://img.shields.io/github/stars/benallfree/gobot)

## 非官方 PocketBase 客户端 (SDK)

- [Go](https://github.com/pluja/pocketbase) - Golang 中的 PocketBase 客户端。 ![GitHub Repo 星星](https://img.shields.io/github/stars/pluja/pocketbase)
- [Kotlin](https://github.com/agrevster/pocketbase-kotlin) - Kotlin 中的 PocketBase 客户端。 ![GitHub Repo 星星](https://img.shields.io/github/stars/agrevster/pocketbase-kotlin)
- [Kotlin (Multiplatform)](https://github.com/IdanAizikNissim/pocketbase-kt) - Kotlin 中的 PocketBase 客户端。 ![GitHub Repo 星星](https://img.shields.io/github/stars/IdanAizikNissim/pocketbase-kt)
- [Python (Sync)](https://github.com/vaphes/pocketbase) - Python 中的 PocketBase 客户端。 ![GitHub Repo 星星](https://img.shields.io/github/stars/vaphes/pocketbase)
- [Python (Async)](https://github.com/thijsmie/pocketbase) - Python 中的 PocketBase 客户端。 ![GitHub Repo 星星](https://img.shields.io/github/stars/thijsmie/pocketbase)
- [C#](https://github.com/PRCV1/pocketbase-csharp-sdk) - C# 中的 PocketBase 客户端。 ![GitHub Repo 星星](https://img.shields.io/github/stars/PRCV1/pocketbase-csharp-sdk)
- [Rust](https://github.com/sreedevk/pocketbase-sdk-rust) - Rust 中的 PocketBase 客户端。 ![GitHub Repo 星星](https://img.shields.io/github/stars/sreedevk/pocketbase-sdk-rust)
- [Unity (Multiplatform)](https://github.com/Sov3rain/pocketbase-unity) - Unity 3D 游戏引擎的 PocketBase 客户端。 ![GitHub Repo 星星](https://img.shields.io/github/stars/Sov3rain/pocketbase-unity)

## 自托管

- [DigitalOcean](https://github.com/pocketbase/pocketbase/discussions/512) - 在 Droplet 中部署的指南。
- [Fly.io](https://github.com/pocketbase/pocketbase/discussions/537) - Fly.io 中免费部署指南。
- [Railway](https://github.com/metruzanca/pocketbase_railway) - 铁路部署指南。
- [AWS Lightsail](https://github.com/boustanihani/pocketbase-lightsail-hosting) - 部署到 AWS Lightsail 的指南。
- [LocalXpose](https://localxpose.io/docs/tutorials/expose-pocketbase-backend) - 允许公共访问本地主机实例。
- [PocketBase Docker](https://github.com/kdpuvvadi/pocketbase) - Docker 镜像支持多种架构，并使用最新的 PocketBase 版本进行了更新。 ![GitHub Repo 星星](https://img.shields.io/github/stars/kdpuvvadi/pocketbase)
- [PocketBase on Dokku](https://github.com/blockshiftnetwork/dokku-pocketbase) - 轻松在 Dokku 上部署 PocketBase 实例。 ![GitHub Repo 星星](https://img.shields.io/github/stars/blockshiftnetwork/dokku-pocketbase)
- [PBLauncher](https://github.com/user0608/pb_launcher) - 管理 PocketBase 实例 — 快速、轻量级、开源。 ![GitHub Repo 星星](https://img.shields.io/github/stars/user0608/pb_launcher)
- [pb-deployer](https://github.com/magooney-loon/pb-deployer) - 自动化将 PocketBase 应用程序部署到生产环境的生命周期！[GitHub Repo star](https://img.shields.io/github/stars/magooney-loon/pb-deployer)

## TypeScript 工具

- [pocketbase-jsvm](https://github.com/benallfree/pocketbase-jsvm) - JSVM 类型。 ![GitHub Repo 星星](https://img.shields.io/github/stars/benallfree/pocketbase-jsvm)
- [pb_hooks starter kit](https://github.com/benallfree/ts-pb-hooks-starter) - 使用 TypeScript 构建 PocketBase JavaScript 挂钩。 ![GitHub Repo 星星](https://img.shields.io/github/stars/benallfree/ts-pb-hooks-starter)
- [typed-pocketbase](https://github.com/david-plugge/typed-pocketbase) - 从 PocketBase 实例生成类型并享受完全类型安全的查询。 ![GitHub Repo 星星](https://img.shields.io/github/stars/david-plugge/typed-pocketbase)
- [pocketbase-ts](https://github.com/satohshi/pocketbase-ts) - SDK 包装器具有更可读的“选项”语法和完整的类型安全性。 ![GitHub Repo 星星](https://img.shields.io/github/stars/satohshi/pocketbase-ts)
- [pocketbase-query](https://github.com/emresandikci/pocketbase-query) - 基于 TypeScript 的查询生成器，旨在为 PocketBase 生成复杂的过滤器查询。它允许使用各种运算符轻松构建查询，同时保持流畅且可链接的 API。 ![GitHub Repo 星星](https://img.shields.io/github/stars/emresandikci/pocketbase-query)
- [pocketbase-schema-generator](https://github.com/satohshi/pocketbase-schema-generator) - 用于自动生成模式文件的 JS 钩子。 （Zod/TS 接口）！[GitHub Repo star](https://img.shields.io/github/stars/satohshi/pocketbase-schema-generator)
- [pb-query](https://github.com/sergio9929/pb-query) - 灵活的强类型查询生成器，具有有用的帮助程序，可简化查询过程，具有示例、文档和基于您的架构的完全自动完成功能，直接在 IDE 中进行。 ![GitHub Repo 星星](https://img.shields.io/github/stars/sergio9929/pb-query)
- [pbkit](https://github.com/Karnak19/pbkit) - PocketBase 代码生成工具包。内省您的集合并生成完全类型化的 TypeScript SDK，以及 TanStack 查询、Zod 和实时插件。 ![GitHub Repo 星星](https://img.shields.io/github/stars/Karnak19/pbkit)

## SQLite工具

- [Marmot](https://github.com/maxpert/marmot) - 分布式 SQLite 复制器 [带有 PocketBase 教程](https://www.youtube.com/watch?v=Zapupe_FREc)。 ![GitHub Repo 星星](https://img.shields.io/github/stars/maxpert/marmot)
- [Litestream](https://litestream.io/) - 流式 SQLite 复制。 ![GitHub Repo 星星](https://img.shields.io/github/stars/benbjohnson/litestream)
- [PocketBase+Litestream example](https://github.com/TylerSustare/pocketbase-framework-litestream) - 显示与 PocketBase 一起运行的 Litestream 的模板。 ![GitHub Repo 星星](https://img.shields.io/github/stars/TylerSustare/pocketbase-framework-litestream)
- [PocketBase with Litestream](https://github.com/bscott/pocketbase-litestream/) - 从 Litestream 保存/恢复 PocketBase 的 Docker 示例。 ![GitHub Repo 星星](https://img.shields.io/github/stars/bscott/pocketbase-litestream)
- [pb-import](https://github.com/burggraf/pb-import) - 从 SQLite 数据库以及 CSV 和 TSV 文件导入数据。 ![GitHub Repo 星星](https://img.shields.io/github/stars/burggraf/pb-import)

## 其他工具

- [PocketBaseUML](https://pocketbase-uml.github.io/) - 一个免费的开源 Web 应用程序，可基于 PocketBase 数据库生成 UML 图。 ![GitHub Repo 星星](https://img.shields.io/github/stars/bscott/pocketbase-litestream)
- [PocketBaseMobile](https://github.com/rohitsangwan01/pocketbase_mobile) - 用于从移动设备运行 PocketBase 的 Android 和 iOS 框架。 ![GitHub Repo 星星](https://img.shields.io/github/stars/rohitsangwan01/pocketbase_mobile)
- [pbf](https://github.com/nedpals/pbf) - 用于序列化和反序列化 PocketBase 过滤器语法的库。 ![GitHub Repo 星星](https://img.shields.io/github/stars/nedpals/pbf)
- [PocketBase Templates](https://github.com/Pocket-Space/pocketbase-templates) - PocketBase 模式的开源集合，可帮助您快速入门。 ![GitHub Repo 星星](https://img.shields.io/github/stars/Pocket-Space/pocketbase-templates)
- [pocketbase-queue](https://github.com/joseferben/pocketbase-queue) - 使用 PocketBase 的后台任务的类型安全队列。 ![GitHub Repo 星星](https://img.shields.io/github/stars/joseferben/pocketbase-queue)
- [PocketBase GPT](https://chat.openai.com/g/g-Owo2FBp4K-pocketbase-gpt) - 一个 GPT，其中上传了 PocketBase 的所有文档，以提供更准确和最新的答案。
- [PocketBase API Rule Builder](https://pocketbase-api-rule-builder.vercel.app) - 一个免费的开源 Web 应用程序，可以轻松直观地为 PocketBase 集合生成 API 规则。 ![GitHub Repo 星星](https://img.shields.io/github/stars/kerimovok/pocketbase-api-rule-builder)
- [pb-llm](https://github.com/magooney-loon/pb-llm) - Pocketbase LLM 文档抓取工具！[GitHub Repo star](https://img.shields.io/github/stars/magooney-loon/pb-llm)
- [pocketbase-security-skill](https://github.com/Perufitlife/pocketbase-security-skill) - 开源 MIT 审计程序，以匿名方式进行探测，以确认允许的默认规则通配符、匿名记录列表暴露和管理 API 错误配置。输出带有复制粘贴修复片段的 HTML 报告。 ![GitHub Repo 星星](https://img.shields.io/github/stars/Perufitlife/pocketbase-security-skill)

## 展示柜

- [Vimsnake](https://github.com/patmood/vim_snake) - 实时 WebAssembly 游戏，其中 Vim 命令用作控制器输入。 ![GitHub Repo 星星](https://img.shields.io/github/stars/patmood/vim_snake)
- [ToDo](https://github.com/rajesh6161/pocketbaseTodo) - 基于 React 的待办事项演示应用程序。 ![GitHub Repo 星星](https://img.shields.io/github/stars/rajesh6161/pocketbaseTodo)
- [Realtime Blog](https://github.com/rajesh6161/pbRealtimeBlog) - 基于 React 的实时博客演示。 ![GitHub Repo 星星](https://img.shields.io/github/stars/rajesh6161/pbRealtimeBlog)
- [oAuth](https://github.com/rajesh6161/pocketbase-oauth-demo) - 基于 React 的 oAuth 演示。 ![GitHub Repo 星星](https://img.shields.io/github/stars/rajesh6161/pocketbase-oauth-demo)
- [Flutter Chat App](https://github.com/rohitsangwan01/flutter_pocketbase_chat) - Flutter 中使用 PocketBase 的聊天应用程序。 ![GitHub Repo 星星](https://img.shields.io/github/stars/rohitsangwan01/flutter_pocketbase_chat)
- [JustJot](https://justjot.app) - 一个键盘优先的全功能渐进式网络应用程序。 [前端仓库](https://github.com/JunoNgx/justjot-frontend) / [后端仓库](https://github.com/JunoNgx/justjot-backend) ![GitHub 仓库星星](https://img.shields.io/github/stars/JunoNgx/justjot-backend)
- [Cookie auth demo](https://github.com/davidbarton/pocketbase-cookie-auth-demo) - PocketBase 基于 cookie 的身份验证流程演示。 ![GitHub Repo 星星](https://img.shields.io/github/stars/davidbarton/pocketbase-cookie-auth-demo)
- [Adnexos](https://github.com/tametsi/adnexos) - 网络上可自行托管的费用分配器。 ![GitHub Repo 星星](https://img.shields.io/github/stars/tametsi/adnexos)
- [pocketbase-libsql](https://github.com/cobeo2004/pocketbase-libsql) - 使用 LibSQL 和 sqld 扩展 Pocketbase - 概念验证！[GitHub 存储库星星](https://img.shields.io/github/stars/cobeo2004/pocketbase-libsql)
- [PocketChat](https://github.com/PocketTogether/pocket-chat) - 使用 PocketBase 和 Vue3 构建的实时聊天平台，支持 OAuth、通知、PWA、文件/图像共享、权限等。 ![GitHub Repo 星星](https://img.shields.io/github/stars/PocketTogether/pocket-chat)
- [TinyCld](https://github.com/tinycld) - 带有邮件/日历/驱动器/文本/计算包的全功能工作区，使用 Pocketbase 和 React Native 进行实时数据库和文件存储。  使用 imap/smtp/caldav/webdav 的 golang 服务扩展 Pocketbase 服务器。

## PocketPorts 套餐

将 NPM/Node.js 包移植到 PocketBase JSVM。

| OG 套餐 |移植包 |描述 |                                                                                      |
| ---------------------------------------------- | ---------------------------------------------------------------- | -------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| [Node.js](https://nodejs.org/docs/latest/api/) | [pocketbase-node](https://github.com/benallfree/pocketbase-node) | Node.js 核心包（`fs`、`process` 等）| ![GitHub Repo 星星](https://img.shields.io/github/stars/benallfree/pocketbase-node) |
| [ejs](https://github.com/mde/ejs) | [pocketbase-ejs](https://github.com/benallfree/pocketbase-ejs) |嵌入式 JavaScript 模板 - [http://ejs.co](http://ejs.co) | ![GitHub Repo 星星](https://img.shields.io/github/stars/benallfree/pocketbase-ejs) |
| [标记](https://github.com/markedjs/marked) |无需更改即可工作 | Markdown 解析器和编译器。专为速度而打造。               | ![GitHub 仓库星星](https://img.shields.io/github/stars/markedjs/marked) |
