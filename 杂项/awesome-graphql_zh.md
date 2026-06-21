# Awesome-graphql ![GitHub Actions 工作流程状态](https://img.shields.io/github/actions/workflow/status/chentsulin/awesome-graphql/awesome_bot.yml?logo=githubactions&label=Awesome%20Bot) [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

> 很棒的 GraphQL 列表

如果您想对此列表做出贡献（请这样做），请向我发送拉取请求。

## 目录

<!-- MarkdownTOC depth=4 -->

- [awesome-graphql  ](#awesome-graphql--)
  - [目录](#table-of-contents)
  - [Specifications](#specifications)
  - [Foundations](#foundations)
  - [Communities](#communities)
  - [Meetups](#meetups)
  - [Implementations](#implementations)
    - [JavaScript/TypeScript](#javascripttypescript)
      - [Clients](#clients)
        - [前端框架集成](#frontend-framework-integrations)
          - [React](#react)
      - [Servers](#servers)
        - [数据库\& ORM](#databases--orms)
        - [PubSub](#pubsub)
      - [自定义标量](#custom-scalars)
      - [Type](#type)
      - [Miscellaneous](#miscellaneous)
      - [JavaScript 示例](#javascript-examples)
      - [TypeScript 示例](#typescript-examples)
    - [Ruby](#ruby)
      - [红宝石示例](#ruby-examples)
    - [PHP](#php)
      - [PHP 示例](#php-examples)
    - [Python](#python)
      - [Python 示例](#python-examples)
    - [Java](#java)
      - [自定义标量](#custom-scalars-1)
      - [Java 示例](#java-examples)
    - [Kotlin](#kotlin)
      - [Kotlin 示例](#kotlin-examples)
    - [C/C++](#cc)
    - [Go](#go)
      - [围棋示例](#go-examples)
    - [Scala](#scala)
      - [斯卡拉示例](#scala-examples)
    - [.NET](#net)
      - [.NET 示例](#net-examples)
    - [Elixir](#elixir)
      - [长生不老药的例子](#elixir-examples)
    - [Haskell](#haskell)
    - [SQL](#sql)
    - [Lua](#lua)
    - [Elm](#elm)
    - [Clojure](#clojure)
      - [Clojure 示例](#clojure-examples)
    - [Swift](#swift)
    - [OCaml](#ocaml)
    - [Android](#android)
      - [Android 示例](#android-examples)
    - [iOS](#ios)
      - [iOS 示例](#ios-examples)
    - [ClojureScript](#clojurescript)
    - [ReasonML](#reasonml)
    - [Dart](#dart)
    - [Rust](#rust)
      - [生锈的例子](#rust-examples)
    - [D (dlang)](#d-dlang)
    - [R（R统计）](#r-rstat)
    - [Julia](#julia)
    - [Crystal](#crystal)
    - [Ballerina](#ballerina)
      - [芭蕾舞演员样品](#ballerina-samples)
  - [Tools](#tools)
    - [工具 - 编辑器\& IDE \& 浏览器](#tools---editors--ides--explorers)
    - [工具 - 测试、原型设计和模拟](#tools---testing-prototyping--mocking)
    - [工具 - 安全](#tools---security)
    - [工具 - 浏览器扩展](#tools---browser-extensions)
    - [工具 - 文档](#tools---docs)
    - [工具 - 编辑器插件](#tools---editor-plugins)
    - [工具 - 杂项](#tools---miscellaneous)
  - [Databases](#databases)
  - [Services](#services)
    - [CDN](#cdn)
    - [CMS](#cms)
  - [Books](#books)
  - [Videos](#videos)
  - [Podcasts](#podcasts)
  - [风格指南](#style-guides)
  - [Blogs](#blogs)
    - [博客 - 安全](#blogs---security)
  - [Posts](#posts)
  - [Tutorials](#tutorials)
  - [License](#license)

<!-- /MarkdownTOC -->

<a name="spec" />

## 规格

- [GraphQL](https://github.com/graphql/graphql-spec) - GraphQL 规范的工作草案。
- [GraphQL over HTTP](https://github.com/graphql/graphql-over-http) - “GraphQL over HTTP”规范的工作草案。
- [GraphQL Relay](https://relay.dev/docs/guides/graphql-server-specification/) - 符合 Relay 的 GraphQL 服务器规范。
- [OpenCRUD](https://github.com/opencrud/opencrud) - OpenCRUD 是数据库的 GraphQL CRUD API 规范。
- [Apollo Federation](https://www.apollographql.com/docs/federation/federation-spec/) - 阿波罗联盟规范
- [GraphQXL](https://gabotechs.github.io/graphqxl/) - GraphQXL 是 GraphQL 语言的扩展，具有一些附加功能，有助于创建大型且可扩展的服务器端模式。
- [GraphQL Scalars](https://www.graphql-scalars.com/) - 主机社区定义了与 @specifiedBy 一起使用的自定义标量规范。

<a name="foundation" />

## 基础

- [GraphQL Foundation](https://graphql.org/foundation/) - Linux基金会下的GraphQL基金会

<a name="community" />

## 社区

- [Discord - GraphQL](https://discord.graphql.org/) - 官方 GraphQL.org 不和谐频道。
- [GraphQL Weekly](https://www.graphqlweekly.com/) - 每周简讯，重点介绍 GraphQL 社区的资源和新闻。
- [Apollo GraphQL Community](https://community.apollographql.com/) - 与其他开发人员联系并分享有关 Apollo GraphQL 平台各个部分的知识。
- [Discord - Reactiflux](http://join.reactiflux.com/) - 加入 Reactiflux Discord 服务器上的“#help-graphql”。
- [Facebook](https://www.facebook.com/groups/795330550572866/) - 讨论、文章和知识共享的小组。
- [X](https://x.com/search?q=%23GraphQL) - 使用主题标签“#graphql”。
- [StackOverflow](https://stackoverflow.com/questions/tagged/graphql) - 问答。使用标签“graphql”。
- [GraphQL APIs](https://github.com/APIs-guru/graphql-apis) - 公共 GraphQL API 的集体列表。
- [/r/GraphQL](https://www.reddit.com/r/graphql/) - 一个包含有趣且信息丰富的 GraphQL 内容和讨论的 Reddit 子版块。

<a name="meetup" />

## 聚会

- [Relay Meetup](https://relaymeetup.com/) - Relay（GraphQL 客户端）上的全球在线聚会。
- [Amsterdam](https://www.meetup.com/Amsterdam-GraphQL-Meetup/)
- [Bangalore](https://www.meetup.com/graphql-bangalore/)
- [Berlin](https://www.meetup.com/graphql-berlin/)
- [布宜诺斯艾利斯](https://www.meetup.com/es-ES/GraphQL-BA/)
- [Copenhagen](https://www.meetup.com/Copenhagen-GraphQL-Meetup-Group/)
- [达拉斯-沃斯堡](https://www.meetup.com/DFW-GraphQL-Meetup/)
- [Hamburg](https://www.meetup.com/GraphQL-Hamburg/)
- [London](https://www.meetup.com/GraphQL-London/)
- [Melbourne](https://www.meetup.com/GraphQL-Melbourne/)
- [Munich](https://www.meetup.com/GraphQL-Munich/)
- [纽约市](https://www.meetup.com/GraphQL-NYC/)
- [旧金山](https://www.meetup.com/GraphQL-SF/)
- [Seattle](https://www.meetup.com/Seattle-GraphQL/)
- [Sydney](https://www.meetup.com/GraphQL-Sydney/)
- [特拉维夫](https://www.meetup.com/GraphQL-TLV/)
- [Wrocław](https://www.meetup.com/GraphQL-Wroclaw/)
- [Singapore](https://www.meetup.com/GraphQL-SG/)
- [Zurich](https://www.meetup.com/GraphQL-Zurich/)

<a name="impl" />

## 实施

<a name="js" />

### JavaScript/TypeScript

- [graphql-js](https://github.com/graphql/graphql-js) - JavaScript 的 GraphQL 参考实现。
- [graphql-jit](https://github.com/zalando-incubator/graphql-jit) - 使用 JIT 编译器执行 GraphQL。
- [Gra*fast*](https://grafast.org) - GraphQL 的尖端规划和执行引擎。

#### 客户

- [apollo-client](https://github.com/apollographql/apollo-client) - 适用于每个 UI 框架和 GraphQL 服务器的功能齐全、生产就绪的缓存 GraphQL 客户端。
- [graphql-request](https://github.com/prisma-labs/graphql-request) - 适用于 Node 和浏览器的最小 GraphQL 客户端。
- [typescript-graphql-request](https://graphql-code-generator.com/docs/plugins/typescript-graphql-request) - 使用 GraphQL Request 作为完全类型化的 SDK。
- [graphql-zeus](https://github.com/graphql-editor/graphql-zeus) - GraphQL Zeus 为“JavaScript”或“TypeScript”创建自动完成客户端库，为强类型查询提供自动完成功能。
- [graphqurl](https://github.com/hasura/graphqurl) - 用于 GraphQL 的curl，具有自动完成、订阅和 GraphiQL 功能。也是一个极其简单的通用 JavaScript GraphQL 客户端。
- [aws-amplify](https://github.com/aws-amplify/amplify-js) - 由 Amazon 开发的用于缓存、分析等的客户端库，其中包括一种获取 GraphQL 查询的方法。
- [gqty](https://github.com/gqty-dev/gqty) - TypeScript 的无 GraphQL 客户端
- [genql](https://github.com/remorses/genql) - 适用于任何 GraphQL API 的类型安全 TypeScript 客户端。

##### 前端框架集成

- [vue-apollo](https://github.com/vuejs/vue-apollo) - VueJS 的 Apollo/GraphQL 集成。
- [apollo-angular](https://github.com/kamilkisiela/apollo-angular) - 适用于 Angular 和每个 GraphQL 服务器的功能齐全、可用于生产的缓存 GraphQL 客户端。
- [svelte-apollo](https://github.com/timhall/svelte-apollo) - Apollo GraphQL 的 Svelte 集成。
- [ember-apollo-client](https://github.com/ember-graphql/ember-apollo-client) - Apollo 客户端和 GraphQL 的 ember-cli 插件。
- [apollo-elements](https://github.com/apollo-elements/apollo-elements) - 适用于任何前端框架的 GraphQL Web 组件。
- [sveltekit-kitql](https://github.com/jycouet/kitql) - 一组工具，可帮助您使用 SvelteKit 和 GraphQL 快速构建高效的应用程序。

###### 反应

- [react-apollo](https://www.apollographql.com/docs/react/) - 核心 @apollo/client 库提供与 React 的内置集成。
- [relay](https://github.com/facebook/relay) - Relay 是一个用于构建数据驱动的 React 应用程序的 JavaScript 框架。
- [urql](https://github.com/FormidableLabs/urql) - 一个简单的 React 缓存 GraphQL 客户端。
- [graphql-hooks](https://github.com/nearform/graphql-hooks) - 最小钩子优先的 GraphQL 客户端，具有缓存和服务器端渲染支持。
- [mst-gql](https://github.com/mobxjs/mst-gql) - mobx-state-tree 和 GraphQL 的绑定。
- [micro-graphql-react](https://github.com/arackaf/micro-graphql-react) - 用于将 GraphQL 添加到 React 的轻量级实用程序。成分。包括简单的缓存并使用 GET 请求，这些请求还可以通过服务工作线程进行缓存。
- [@gqty/react](https://github.com/gqty-dev/gqty) - TypeScript 的无 GraphQL 客户端

#### 服务器

- [apollo-server](https://github.com/apollographql/apollo-server) - 符合规范且可投入生产的 JavaScript GraphQL 服务器，可让您以架构优先的方式进行开发。专为 Express、Connect、Hapi、Koa 等而构建。
- [hapi-graphql](https://github.com/SimonDegraeve/hapi-graphql) - 使用 Hapi 创建 GraphQL HTTP 服务器。
- [hapi-plugin-graphiql](https://github.com/rse/hapi-plugin-graphiql) - 用于 GraphiQL 集成的 HAPI 插件。
- [graphql-api-koa](https://github.com/jaydenseric/graphql-api-koa) - GraphQL Koa 中间件，从头开始实现 GraphQL.js，并支持原生 ESM。
- [koa-graphql](https://github.com/chentsulin/koa-graphql) - GraphQL Koa 中间件。
- [graphql-koa-scripts](https://github.com/ryanhs/graphql-koa-scripts) - GraphQL Koa 1 文件已简化。对于快速测试很有用
- [gql](https://github.com/deno-libs/gql) - 适用于 Deno 的通用 GraphQL HTTP 中间件。
- [mercurius](https://github.com/mercurius-js/mercurius) - Fastify 的 GraphQL 插件。
- [graphql-yoga](https://github.com/prisma-labs/graphql-yoga) - 功能齐全的 GraphQL Server，专注于轻松设置、性能和出色的开发人员体验。
- [graphitejs](https://github.com/graphitejs/server) - GraphQL 的 NodeJS 框架。
- [graphql-helix](https://github.com/contrawork/graphql-helix) - 高度发展的 GraphQL HTTP 服务器。
- [pylon](https://github.com/getcronit/pylon) - 仅使用函数编写功能齐全的 API。不再需要样板代码，不再需要设置。只需编写函数并部署即可。
- [modus](https://github.com/hypermodeinc/modus) - 基于 WebAssembly 的无服务器运行时，可提供自动生成的 GraphQL API。

##### 数据库和 ORM

- [graphql-sequelize](https://github.com/mickhansen/graphql-sequelize) - GraphQL 的 Sequelize 助手。
- [graphql-bookshelf](https://github.com/brysgo/graphql-bookshelf) - 有些帮助围绕 BookshelfJS 模型定义 GraphQL 架构。
- [join-monster](https://github.com/acarl005/join-monster) - 用于批量数据获取的 GraphQL 到 SQL 查询执行层。

##### 发布订阅

- [graphql-ably-pubsub](https://github.com/ably-labs/graphql-ably-pubsub) - GraphQL 的 Ably PubSub 实现用于发布突变更新并通过订阅查询订阅结果。

#### 自定义标量

- [graphql-scalars](https://github.com/Urigo/graphql-scalars) - 自定义 GraphQL 标量库，用于创建精确的类型安全 GraphQL 模式。

#### 类型

- [type-graphql](https://github.com/19majkel94/type-graphql) - 使用 TypeScript、使用类和装饰器创建 GraphQL 模式和解析器！
- [graphql-nexus](https://github.com/graphql-nexus/nexus) - 代码优先、类型安全、GraphQL 架构构建。
- [graphql-code-generator](https://github.com/dotansimha/graphql-code-generator)：GraphQL 代码生成器，灵活支持自定义插件和模板，如 TypeScript（前端和后端）、React Hooks、解析器签名等。
- [pothos](https://github.com/hayes/pothos) - Pothos 是一个基于插件的 Typescript GraphQL 模式构建器。它使得在 TypeScript 中构建 graphql 模式变得简单、快速和愉快。
- [garph](https://github.com/stepci/garph) - Garph 是用于在 TypeScript 中构建类型安全的 GraphQL API 的全栈框架。
- [gqloom](https://github.com/modevol-com/gqloom) - GQLoom 是一个用于 TypeScript/JavaScript 的 GraphQL 编织器，它使用 [Valibot](https://github.com/fabian-hiller/valibot)、[Zod](https://github.com/colinhacks/zod) 或 [Yup](https://github.com/jquense/yup) 编织 GraphQL 架构和解析器。
- [fast-graphql](https://github.com/idurar/fast-graphql) - 用于为 Node.js、Next.Js 和 Graphql Apollo 服务器构建、组合解析器和合并架构定义的 Graphql 工具
- [graphql-to-type](https://github.com/lkster/graphql-to-type) - GraphQL 查询解析器完全用 TypeScript 的类型系统编写，用于根据提供的查询创建接口
- [gql.tada](https://github.com/0no-co/gql.tada) - GraphQL 文档创作库，推断 TypeScript 类型系统中 GraphQL 查询和片段的结果和变量类型。

#### 杂项

- [graphql-tools](https://github.com/apollographql/graphql-tools) - 用于构建和维护 GraphQL-JS 服务器的工具库。
- [graphql-tag](https://github.com/apollographql/graphql-tag) - 解析 GraphQL 查询的 JavaScript 模板文字标记。
- [load-gql](https://github.com/KunalSin9h/load-gql) - 来自文件和文件夹的小型、零依赖 GraphQL 模式加载器。
- [graphql-compose](https://github.com/graphql-compose/graphql-compose) - 该工具允许您通过插件从不同的数据源构建灵活的 graphql 模式。
- [graphql-modules](https://github.com/Urigo/graphql-modules) - 按模块或功能将 GraphQL 服务器分成更小的、可重用的部分。
- [graphql-shield](https://github.com/maticzav/graphql-shield) - 一个帮助为 graphql api 创建权限层的库。
- [graphql-shield-generator](https://github.com/omar-dulaimi/graphql-shield-generator) - 从 GraphQL 架构中发出 GraphQL Shield。
- [graphqlgate](https://github.com/oslabs-beta/GraphQL-Gate) - 具有 Node.js 查询复杂性分析功能的 GraphQL 速率限制库
- [graphql-let](https://github.com/piglovesyou/graphql-let) - 一个 webpack 加载器，用于直接从 GraphQL 文档导入受类型保护的代码生成结果
- [graphql-config](https://github.com/kamilkisiela/graphql-config) - 适用于所有 GraphQL 工具的一种配置（大多数工具、编辑器和 IDE 支持）。
- [graphql-cli](https://github.com/urigo/graphql-cli) - 用于常见 GraphQL 开发工作流程的命令行工具。
- [graphql-toolkit](https://github.com/ardatan/graphql-toolkit) - 一组用于更快开发 GraphQL 工具的实用程序（架构和文档加载、架构合并等）。
- [graphql-mesh](https://github.com/urigo/graphql-mesh) - 使用 GraphQL 查询语言访问不运行 GraphQL 的远程 API（以及运行 GraphQL 的远程 API）中的数据。
- [sofa](https://github.com/Urigo/sofa) - 从 GraphQL API 生成 REST API。
- [graphback](https://github.com/aerogear/graphback) - 使用数据模型将 GraphQLCRUD API 层添加到 GraphQL 服务器的框架和 CLI。
- [graphql-middleware](https://github.com/maticzav/graphql-middleware) - 将 GraphQL 解析器拆分为中间件函数。
- [graphql-relay-js](https://github.com/graphql/graphql-relay-js) - 一个帮助构建支持react-relay的graphql-js服务器的库。
- [graphql-normalizr](https://github.com/monojack/graphql-normalizr) - 标准化 GraphQL 响应以持久保存在客户端缓存/状态中。
- [babel-plugin-graphql](https://github.com/ooflorent/babel-plugin-graphql) - Babel 插件，编译 GraphQL 标记模板字符串。
- [eslint-plugin-graphql](https://github.com/apollographql/eslint-plugin-graphql) - 一个 ESLint 插件，用于根据架构检查 GraphQL 字符串。
- [graphql-ws](https://github.com/enisdenjo/graphql-ws) - 连贯、零依赖、惰性、简单、基于 WebSocket 协议的 GraphQL 兼容服务器和客户端。
- [graphql-live-query](https://github.com/n1ru4l/graphql-live-query) - 使用 JavaScript 进行实时 GraphQL 实时查询。
- [GraphVinci](https://github.com/Comcast/graphvinci) - GraphQL API 的交互式模式可视化工具。
- [supertest-graphql](https://github.com/alexstrat/supertest-graphql) - 扩展 [supertest](https://github.com/visionmedia/supertest) 以轻松测试 GraphQL 端点
- [schemathesis](https://github.com/schemathesis/schemathesis) - 运行与 GraphQL 架构匹配的任意查询以查找服务器错误。
- [microfiber](https://github.com/anvilco/graphql-introspection-tools) - 以有用的方式查询和操作 GraphQL 自省查询结果。
- [graphql-armor](https://github.com/Escape-Technologies/graphql-armor) - 用于生产 GraphQL 端点的即时安全层。
- [goctopus](https://github.com/Escape-Technologies/goctopus) - 一个极其快速的 GraphQL 发现和指纹识别工具箱。
- [GraphQL Constraint Directive](https://github.com/confuser/graphql-constraint-directive) - 允许使用@constraint作为指令来验证输入数据。受到约束指令 RFC 和 OpenAPI 的启发
- [Validator.js Wrapper Directive](https://github.com/ktutnik/graphql-directive/tree/master/packages/validator) - 验证器指令的完整列表包含 Validator.js 功能
- [WunderGraph Cosmo](https://github.com/wundergraph/cosmo) - 开源 GraphQL 联合解决方案，具有（联合）GraphQL 的完整生命周期 API 管理。模式注册表、组成检查、分析、指标、跟踪和路由。
- [graphql-go-tools](https://github.com/wundergraph/graphql-go-tools) - 用 Golang 编写的 graphQL Router / API Gateway 框架，专注于正确性、可扩展性和高性能。支持联合 v1 和 v2、订阅等。
- [graphql-sunset](https://github.com/sophiabits/graphql-sunset) - 快速轻松地向 GraphQL 服务器添加对“Sunset”标头的支持，以更好地传达即将发生的重大更改。
- [Schemato](https://www.schemato.top/graphql-to-typescript) - 仅浏览器的 GraphQL SDL 转换器，用于生成 TypeScript、Zod、Pydantic、Go、Rust 和其他类型模型。

<a name="js-example" />

#### JavaScript 示例

- [React Starter Kit](https://github.com/kriasoft/react-starter-kit) - 使用 React、Relay、GraphQL 和 JAM 堆栈架构的前端入门套件。
- [SWAPI GraphQL Wrapper](https://github.com/graphql/swapi-graphql) - GraphQL 模式和服务器包装 SWAPI。
- [Relay TodoMVC](https://github.com/taion/relay-todomvc) - 使用路由中继 TodoMVC。
- [Apollo Client documentation](https://www.apollographql.com/docs/react) - 使用 apollo 客户端构建 GraphQL 应用程序的文档和示例。
- [Apollo Server tools documentation](https://www.apollographql.com/docs/apollo-server/) - 有关构建 GraphQL 服务器以及连接到 SQL、MongoDB 和 REST 端点的文档、教程和示例。
- [F8 App 2017](https://github.com/fbsamples/f8app) - 2016 年官方 F8 应用程序的源代码，由 React Native 和其他 Facebook 开源项目提供支持。
- [Apollo React example for Github GraphQL API](https://github.com/katopz/react-apollo-graphql-github-example) - 使用示例 Apollo React for Github GraphQL API 和 create-react-app。
- [Next.js TypeScript and GraphQL Example](https://github.com/zeit/next.js/tree/canary/examples/with-typescript-graphql) - Next.js 上受类型保护的 GraphQL 示例，在后台运行 [graphql-codegen](https://graphql-code-generator.com/)
- [GraphQL StackBlitz Starter](https://stackblitz.com/fork/graphql) - 一个实时的、可编辑的演示在大约 2 秒内启动并在浏览器中运行。
- [NAPERG](https://github.com/alan345/naperg) - 全栈样板 GraphQL。使用 React 和 Prisma + 身份验证和角色制成。
- [VulcanJS](http://vulcanjs.org) - 全栈React+GraphQL框架
- [RAN Toolkit](https://github.com/sly777/ran) - 生产就绪的工具包/样板，支持 GraphQL、SSR、热重载、CSS-in-JS、缓存等。

<a name="ts-example" />

#### TypeScript 示例

- [Node.js API Starter](https://github.com/kriasoft/nodejs-api-starter) - 基于 Yarn v2 的 monorepo 模板（代码优先 GraphQL API、PostgreSQL、PnP、零安装、无服务器）。
- [Next.js Apollo TypeScript Starter](https://github.com/borisowsky/nextjs-apollo-ts-starter) - Next.js 入门项目专注于开发人员体验。
- [GraphQL Starter](https://github.com/cerino-ligutom/GraphQL-Starter) - TypeScript + Node Express + Apollo GraphQL API 的样板。
- [Mocked Managed Federation - Apollo Server 3](https://github.com/setchy/apollo-server-3-mocked-federation) - 如何使用 Apollo Server 3.x 模拟托管联合 Supgraph 的示例
- [Mocked Managed Federation - Apollo Server 4](https://github.com/setchy/apollo-server-4-mocked-federation) - 如何使用 Apollo Server 4.x 模拟托管联合 Supgraph 的示例
- [Next.js Advanced Graphql Crud MongoDB Starter](https://github.com/idurar/starter-advanced-graphql-crud-next-js-mongodb) - 使用带有 Next.js 和 Mongodb (TypeScript) 的高级 Apollo Graphql 服务器启动通用 CRUD

<a name="rb" />

### 红宝石

- [graphql-ruby](https://github.com/rmosolgo/graphql-ruby) - Facebook GraphQL 的 Ruby 实现。
- [graphql-batch](https://github.com/Shopify/graphql-batch) - graphql gem 的查询批处理执行器。
- [graphql-auth](https://github.com/o2web/graphql-auth) - 与设备一起使用的 JWT 身份验证包装器。
- [agoo](https://github.com/ohler55/agoo) - 实现 Facebook GraphQL 的 Ruby Web 服务器。
- [GQLi](https://github.com/contentful-labs/gqli.rb) - GraphQL 客户端和 DSL。允许用本机 Ruby 编写查询。

<a name="rb-example" />

#### 红宝石示例

- [graphql-ruby-demo](https://github.com/rmosolgo/graphql-ruby-demo) - 使用 graphql-ruby 公开 Rails 应用程序。
- [github-graphql-rails-example](https://github.com/github/github-graphql-rails-example) - 使用 GitHub 的 GraphQL API 的示例 Rails 应用程序。
- [relay-on-rails](https://github.com/nethsix/relay-on-rails) - 用于带有 Rails GraphQL 服务器的 Relay 应用程序的 Barebones 入门套件。
- [relay-rails-blog](https://github.com/gauravtiwari/relay-rails-blog) - 一个由 graphql、继电器和标准 Rails 应用程序支持的演示博客。
- [to_eat_app](https://github.com/jcdavison/to_eat_app) - 示例 graphql/rails/relay 应用程序以及相关的 3 部分文章系列。
- [agoo-demo](https://github.com/ohler55/agoo/tree/develop/example/graphql) - 使用 Agoo 服务器演示简单的 GraphQL 应用程序。
- [rails-devise-graphql](https://github.com/zauberware/rails-devise-graphql) - 带有设计、graphql 和 JWT auth 的 Rails 6 样板。

<a name="php" />

### PHP

- [graphql-php](https://github.com/webonyx/graphql-php) - GraphQL 参考实现的 PHP 端口。
- [graphql-relay-php](https://github.com/ivome/graphql-relay-php) - 用于 GraphQL 的 webonyx/graphql-php 实现的中继助手。
- [lighthouse](https://github.com/nuwave/lighthouse) - 一个 PHP 包，允许从 Laravel 应用程序提供 GraphQL 端点服务。
- [graphql-laravel](https://github.com/rebing/graphql-laravel) - Facebook GraphQL 的 Laravel 包装器。
- [overblog/graphql-bundle](https://github.com/overblog/GraphQLBundle) - 该捆绑包提供了在 Symfony 应用程序中构建完整 GraphQL 服务器的工具。支持反应中继。
- [wp-graphql](https://github.com/wp-graphql/wp-graphql) - 适用于 WordPress 的 GraphQL API。
- [graphqlite](https://github.com/thecodingmachine/graphqlite) - 与框架无关的库，允许您通过注释 PHP 类来编写 GraphQL 服务器。
- [siler](https://github.com/leocavalcante/siler) - 普通的旧函数为具有订阅支持的 GraphQL 服务器提供声明性 API。
- [graphql-request-builder](https://github.com/dpauli/php-graphql-request-builder) - 在 GraphQL 结构中构建请求负载。
- [drupal/graphql](https://www.drupal.org/project/graphql) - 为 Drupal 9 和 10 制作并公开 GraphQL 架构。
- [jerowork/graphql-schema-builder](https://github.com/jerowork/graphql-attribute-schema) - 使用 PHP 属性而不是大型配置数组轻松构建 webonyx/graphql-php 的 GraphQL 架构。

<a name="php-example" />

#### PHP 示例

- [siler-graphgl](https://github.com/leocavalcante/siler/tree/main/examples/graphql) - 使用 Siler 编写的 GraphQL 服务器示例。

<a name="py" />

### 蟒蛇

- [graphql-parser](https://github.com/tryolabs/graphql-parser) - Python 的 GraphQL 解析器。
- [graphql-core](https://github.com/graphql-python/graphql-core) - 基于 GraphQL.js v16.3.0 参考实现的 Python GraphQL 实现
- [graphql-relay-py](https://github.com/graphql-python/graphql-relay-py) - 一个帮助构建支持react-relay的graphql-py服务器的库。
- [graphql-parser-python](https://github.com/tallstreet/graphql-parser-python) - libgraphqlparser 的 python 包装器。
- [graphene](https://github.com/graphql-python/graphene) - 用于以 Python 风格的简单方式创建 GraphQL 模式/类型的包。
- [graphene-gae](https://github.com/graphql-python/graphene-gae) - 向 Google AppEngine (GAE) 添加 GraphQL 支持。
- [django-graphiql](https://github.com/GraphQL-python-archive/django-graphiql) - 将 GraphiQL 轻松集成到您的 Django 项目中。
- [flask-graphql](https://github.com/graphql-python/flask-graphql) - 向您的 Flask 应用程序添加 GraphQL 支持。
- [python-graphql-client](https://github.com/prisma/python-graphql-client) - 适用于 Python 2.7+ 的简单 GraphQL 客户端
- [python-graphjoiner](https://github.com/healx/python-graphjoiner) - 使用联接、SQL 或其他方式创建 GraphQL API。
- [graphene-django](https://github.com/graphql-python/graphene-django) - 石墨烯的 Django 集成。
- [Flask-GraphQL-Auth](https://github.com/callsign-viper/Flask-GraphQL-Auth) - Flask 的身份验证库，灵感来自于 Flask-jwt-extended。
- [tartiflette](https://github.com/dailymotion/tartiflette) - GraphQL 实现，SDL First，适用于 python 3.6+ / asyncio。
- [tartiflette-aiohttp](https://github.com/dailymotion/tartiflette-aiohttp) - Tartiflette 的包装器，基于 aiohttp / 3.6+ / asyncio 通过 HTTP 公开 GraphQL API，[tartiflette.io 上提供官方教程](https://tartiflette.io/docs/tutorial/getting-started)。
- [Ariadne](https://github.com/mirumee/ariadne) - 使用模式优先方法实现 GraphQL 服务器的库。异步查询执行，包括 ASGI、WSGI 和流行的 Web 框架的电池，[完整记录](https://ariadnegraphql.org)。
- [django-graphql-auth](https://github.com/PedroBern/django-graphql-auth) - 使用 GraphQL 进行 Django 注册和身份验证。
- [strawberry](https://github.com/strawberry-graphql/strawberry) - 一个新的 Python GraphQL 库。
- [turms](https://github.com/jhnnsrs/turms) - 围绕 graphql-core 和 pydantic 构建的 pythonic graphql 代码生成器
- [rath](https://github.com/jhnnsrs/rath) - 类似 apollo 的 graphql 客户端，具有异步和同步接口
- [sgqlc](https://github.com/profusion/sgqlc) - 简单的 GraphQL 客户端使得在 Python 中使用 GraphQL API 响应变得更加容易。

<a name="py-example" />

#### Python 示例

- [swapi-graphene](https://github.com/graphql-python/swapi-graphene) - 使用 [Graphene](https://graphene-python.org) 的 GraphQL 模式和服务器。
- [Python Backend Tutorial](https://hasura.io/learn/graphql/backend-stack/languages/python/) - 有关使用 [Strawberry](https://strawberry.rocks/) 创建 GraphQL 服务器和使用 [Qlient](https://qlient-org.github.io/python-qlient/site/) 创建客户端的教程。

<a name="java" />

### 爪哇

- [graphql-java](https://github.com/graphql-java/graphql-java) - GraphQL Java 实现。
- [DGS Framework](https://github.com/Netflix/dgs-framework) - 由 Netflix 开发的 Spring Boot GraphQL 服务器框架。
- [graphql-java-generator](https://github.com/graphql-java-generator) - 一个 [Maven 插件](https://github.com/graphql-java-generator/graphql-maven-plugin-project) 和一个 [Gradle 插件](https://github.com/graphql-java-generator/graphql-gradle-plugin-project)，可以生成 **Client** 和 **Server** （POJO 和实用程序类）。服务器部分基于graphql-java，并隐藏其所有样板代码。
- [gaphql-java-type-generator](https://github.com/graphql-java/graphql-java-type-generator) - 自动生成与 GraphQL Java 一起使用的类型
- [schemagen-graphql](https://github.com/bpatters/schemagen-graphql) - 模式生成和执行包，将 POJO 转换为 GraphQL Java 可查询对象集。允许使用注释将任何服务公开为 GraphQL 服务。
- [graphql-java-annotations](https://github.com/Enigmatis/graphql-java-annotations) - 使用 GraphQL Java 为模式定义提供基于注释的语法。
- [graphql-java-tools](https://github.com/graphql-java-kickstart/graphql-java-tools) - 模式优先的 graphql-java 便利库，可以轻松地将您自己的实现作为数据解析器。受到 JS 的 [graphql-tools](https://github.com/apollographql/graphql-tools) 的启发。
- [graphql-java-codegen-maven-plugin](https://github.com/kobylynskyi/graphql-java-codegen-maven-plugin) - 用于生成 Java 类型和 Resolver 接口的模式优先 Maven 插件。与 graphql-java-tools 完美结合。受到 [swagger-codegen-maven-plugin](https://github.com/swagger-api/swagger-codegen/tree/master/modules/swagger-codegen-maven-plugin) 的启发。
- [graphql-java-codegen-gradle-plugin](https://github.com/kobylynskyi/graphql-java-codegen-gradle-plugin) - 用于生成 Java 类型和 Resolver 接口的模式优先 gradle 插件。与 graphql-java-tools 完美结合。受到 [gradle-swagger-generator-plugin](https://github.com/int128/gradle-swagger-generator-plugin) 的启发。
- [graphql-java-servlet](https://github.com/graphql-java-kickstart/graphql-java-servlet) - 一个与框架无关的 java servlet，用于通过 GET、POST 和分段上传公开 graphql-java 查询端点。
- [manifold-graphql](https://github.com/manifold-systems/manifold/tree/master/manifold-deps-parent/manifold-graphql) - 全面的 GraphQL 客户端使用。模式优先。类型安全的 GraphQL 类型、查询和结果，没有代码生成器、没有 POJO、没有注释。 IntelliJ IDEA 和 Android Studio 提供出色的 [IDE 支持](http://manifold.systems/images/graphql.mp4)。请参阅下面的 [Java 示例](#example-java)。
- [spring-graphql-common](https://github.com/oembedler/spring-graphql-common) - Spring 框架 GraphQL 库。
- [graphql-spring-boot](https://github.com/graphql-java-kickstart/graphql-spring-boot) - GraphQL 和 GraphiQL Spring 框架引导启动器。
- [vertx-graphql-service-discovery](https://github.com/engagingspaces/vertx-graphql-service-discovery) - 异步 GraphQL 服务发现和查询微服务。
- [vertx-dataloader](https://github.com/engagingspaces/vertx-dataloader) - Facebook DataLoader 的端口，用于在集群 GraphQL 环境中进行高效、异步批处理和缓存。
- [graphql-spqr](https://github.com/leangen/GraphQL-SPQR) - 用于快速开发 GraphQL 服务的 Java 8+ API。
- [Light Java GraphQL](https://github.com/networknt/light-graphql-4j)：一个轻量级、快速的微服务框架，解决了所有横切问题并准备插入 GraphQL 模式。
- [Elide](https://elide.io)：一个 Java 库，可以将 JPA 带注释的数据模型公开为任何关系数据库上的 GraphQL 服务。
- [federation-jvm](https://github.com/apollographql/federation-jvm) - JVM 上的 Apollo Federation。
- [graphql-orchestrator-java](https://github.com/graph-quilt/graphql-orchestrator-java) GraphQL Orchestrator/Gateway 库，支持架构缝合和 Apollo Federation 指令，将多个 GraphQL 微服务的架构组合成一个统一的架构。
- [graphql-java-extended-validation](https://github.com/graphql-java/graphql-java-extended-validation) - 为 graphql-java 提供字段和字段参数的扩展验证。
- [dgs-extended-formatters](https://github.com/setchy/dgs-extended-formatters) - 用于常见格式化用例的一组实验性 DGS 指令。

#### 自定义标量

- [graphql-java-datetime](https://github.com/donbeave/graphql-java-datetime) - GraphQL ISO Date 是一组与 graphql-java 一起使用的符合 RFC 3339 的日期/时间标量类型。
- [graphql-java-extended-scalars](https://github.com/graphql-java/graphql-java-extended-scalars) - graphql-java 的扩展标量。

<a name="java-example" />

#### Java 示例

- [light-java-graphql examples](https://github.com/networknt/light-example-4j/tree/master/graphql) - Light Java GraphQL 示例和教程。
- [graphql-spqr-samples](https://github.com/leangen/graphql-spqr-samples) - 使用 Spring MVC 和 GraphQL-SPQR 编写的示例 GraphQL 服务器。
- [manifold-graphql sample](https://github.com/manifold-systems/manifold-sample-graphql-app) - 一个简单的应用程序，包括客户端和服务器，演示了 Manifold GraphQL 库。
- [graphql-java-kickstart_samples](https://github.com/graphql-java-kickstart/samples) - 使用 GraphQL Java Kickstart 项目的示例。
- [graphql-java-kickstart-federation-example](https://github.com/setchy/graphql-java-kickstart-federation-example) - GraphQL Java Kickstart 联合示例。
- [dgs-federation-example](https://github.com/Netflix/dgs-federation-example) - Netflix DGS 联合示例。
- [Spring Boot backend tutorial](https://hasura.io/learn/graphql/backend-stack/languages/java/) - 使用 Spring Boot 和 Netflix DGS 创建 GraphQL 服务器和客户端的教程。

<a name="kotlin" />

### 科特林

- [graphql-kotlin](https://github.com/ExpediaGroup/graphql-kotlin) - GraphQL Kotlin 实现。
- [manifold-graphql](https://github.com/manifold-systems/manifold/tree/master/manifold-deps-parent/manifold-graphql) - 全面的 GraphQL 客户端使用。模式优先。类型安全的 GraphQL 类型、查询和结果，没有代码生成器、没有 POJO、没有注释。 IntelliJ IDEA 和 Android Studio 提供出色的 [IDE 支持](http://manifold.systems/images/graphql.mp4)。请参阅下面的 [Kotlin 示例](#example-kotlin)。
- [KGraphQL](https://github.com/aPureBase/KGraphQL)：用于设置 GraphQL 服务器的纯 Kotlin 实现。
- [Kobby](https://github.com/ermadmi78/kobby) - 采用 GraphQL 模式的 Kotlin DSL 客户端的 Codegen 插件。生成的 DSL 支持在 Kotlin 中执行复杂的 GraphQL 查询、突变和订阅，其语法类似于原生 GraphQL 语法。
- [Graphkt](https://github.com/cufyorg/graphkt) - 一个基于 DSL 的 kotlin graphql 服务器库，由 graphql-java 支持。

<a name="kotlin-example" />

#### Kotlin 示例

- [manifold-graphql sample](https://github.com/manifold-systems/manifold-sample-kotlin-app) - 一个简单的 GraphQL 应用程序（客户端和服务器），使用 Kotlin 演示 Manifold GraphQL 库。

<a name="c" />

### C/C++

- [libgraphqlparser](https://github.com/graphql/libgraphqlparser) - 具有 C 和 C++ API 的 C++ GraphQL 查询解析器。
- [agoo-c](https://github.com/ohler55/agoo-c) - 用 C 编写的高性能 GraphQL 服务器。 [基准测试](https://github.com/the-benchmarker/graphql-benchmarks)
- [cppgraphqlgen](https://github.com/Microsoft/cppgraphqlgen) - C++ GraphQL 模式服务生成器。
- [CaffQL](https://github.com/caffeinetv/CaffQL) - 从 GraphQL 内省查询生成 C++ 客户端类型和请求/响应序列化。

<a name="go" />

### 去

- [graphql](https://github.com/graphql-go/graphql) - GraphQL for Go 的实现遵循 graphql-js
- [graphql-go](https://github.com/graph-gophers/graphql-go) - 注重易用性的 GraphQL 服务器。
- [gql](https://github.com/kadirpekel/gql) - 首先编写 graphql (graphql-go/graphql) 模式构建器。
- [gqlgen](https://github.com/99designs/gqlgen) - Go 生成基于 graphql 服务器库。
- [graphql-relay-go](https://github.com/graphql-go/relay) - 一个 Go/Golang 库，可帮助构建支持 React-relay 的服务器。
- [graphjin](https://github.com/dosco/graphjin)：使用 GraphQL 在 5 分钟内构建 API。即时 GraphQL 到 SQL 编译器。
- [graphql-go-tools](https://github.com/wundergraph/graphql-go-tools) - 用 Golang 编写的 graphQL Router / API Gateway 框架，专注于正确性、可扩展性和高性能。支持联合 v1 和 v2、订阅等。
- [Thunder](https://github.com/Raezil/Thunder) - 由 Go、gRPC-Gateway、Prisma 和 Kubernetes 支持的可扩展微服务框架。它公开了 REST、gRPC 和 Graphql
- [grpc-graphql-gateway](https://github.com/ysugimoto/grpc-graphql-gateway) - 一个 protoc 插件，可从 Protocol Buffers 生成 graphql 执行代码。
<a name="go-example" />

#### 围棋示例

- [golang-relay-starter-kit](https://github.com/sogko/golang-relay-starter-kit) - 使用 Golang GraphQL 服务器的 Relay 应用程序的准系统起点。
- [todomvc-relay-go](https://github.com/sogko/todomvc-relay-go) - React/Relay TodoMVC 应用程序的端口，由 Golang GraphQL 后端驱动。
- [go-graphql-subscription-example](https://github.com/ccamel/go-graphql-subscription-example) - 一个 GraphQL 架构和服务器，演示 GraphQL [订阅](https://github.com/apollographql/subscriptions-transport-ws/blob/v0.9.4/PROTOCOL.md)（通过 Websocket）使用 [Apache Kafka](https://kafka.apache.org/) 消息。
- [Go Backend Tutorial](https://hasura.io/learn/graphql/backend-stack/languages/go/) - 本教程展示了如何使用代码生成来制作 Go GraphQL 服务器和客户端。

<a name="scala" />

### 斯卡拉

- [sangria](https://github.com/sangria-graphql/sangria) - Scala GraphQL 服务器实现。
- [sangria-relay](https://github.com/sangria-graphql/sangria-relay) - 桑格利亚汽酒中继支持。
- [caliban](https://github.com/ghostdogpr/caliban) - Caliban 是一个纯函数库，用于在 Scala 中创建 GraphQL 后端。

<a name="scala-example" />

#### 斯卡拉示例

- [sangria-akka-http-example](https://github.com/sangria-graphql/sangria-akka-http-example) - 使用 akka-http 和 [sangria](https://sangria-graphql.github.io/) 编写的示例 GraphQL 服务器
- [sangria-playground](https://github.com/sangria-graphql/sangria-playground) - 使用 Play 和 sangria 编写的 GraphQL 服务器示例。

<a name="dotnet" />

### .NET

- [graphql-dotnet](https://github.com/graphql-dotnet/graphql-dotnet) - 适用于 .NET 的 GraphQL。
- [graphql-net](https://github.com/ckimes89/graphql-net) - GraphQL 到 IQueryable for .NET。
- [Hot Chocolate](https://github.com/ChilliCream/hotchocolate) - 适用于 .Net Core 和 .NET Framework 的 GraphQL 服务器。
- [Snowflaqe](https://github.com/Zaid-Ajaj/Snowflaqe) - 适用于 F# 和 [Fable](https://github.com/fable-compiler/Fable) 的类型安全 GraphQL 代码生成器
- [EntityGraphQL](https://github.com/EntityGraphQL/EntityGraphQL) - 用于在数据模型之上构建 GraphQL API 的库，具有可扩展性，可将多个数据源整合到单个 GraphQL 架构中。
- [ZeroQL](https://github.com/byme8/ZeroQL) - 类型安全的 GraphQL 客户端，具有类似 Linq 的 C# 接口

<a name="net-example" />

#### .NET 示例

- [.NET backend tutorial](https://hasura.io/learn/graphql/backend-stack/languages/dotnet/) - 使用 .NET 创建 GraphQL 服务器和客户端的教程。

<a name="elixir" />

### 灵丹妙药

- [absinthe-graphql](https://github.com/absinthe-graphql/absinthe) - 功能齐全的 Elixir GraphQL 库。
- [graphql-elixir](https://github.com/graphql-elixir/graphql) - GraphQL Elixir。 （不再维护）
- [plug_graphql](https://github.com/graphql-elixir/plug_graphql) - GraphQL Elixir 的插件集成。
- [graphql_relay](https://github.com/graphql-elixir/graphql_relay) - GraphQL Elixir 的中继助手。
- [graphql_parser](https://github.com/graphql-elixir/graphql_parser) - [libgraphqlparser] 的 Elixir 绑定(https://github.com/graphql/libgraphqlparser)
- [graphql](https://github.com/asonge/graphql) - Elixir GraphQL 解析器。
- [plot](https://github.com/peburrows/plot) - Elixir 的 GraphQL 解析器和解析器。

<a name="elixir-example" />

#### 长生不老药的例子

- [hello_graphql_phoenix](https://github.com/graphql-elixir/hello_graphql_phoenix) - Phoenix 中安装的 GraphQL Elixir Plug 端点示例

<a name="haskell" />

### 哈斯克尔

- [graphql-haskell](https://github.com/jdnavarro/graphql-haskell) - Haskell 的 GraphQL AST 和解析器。
- [morpheus-graphql](https://github.com/morpheusgraphql/morpheus-graphql) - Haskell GraphQL Api、客户端和工具。

<a name="sql" />

### SQL

- [GraphpostgresQL](https://github.com/solidsnack/GraphpostgresQL) - 用于 Postgres 的 GraphQL。
- [sql-to-graphql](https://github.com/rexxars/sql-to-graphql) - 根据您的 SQL 数据库结构生成 GraphQL API。
- [PostGraphile](https://github.com/graphile/postgraphile) - 适用于 PostgreSQL 的闪电般的 GraphQL API：高度可定制；可通过插件扩展；即时的。
- [Hasura](https://github.com/hasura/graphql-engine) - Hasura 通过 PostgreSQL 提供即时实时 GraphQL API。也适用于现有数据库。
- [subZero](https://subzero.cloud/) - 适用于您的数据库的 GraphQL 和 REST API

<a name="lua" />

### 卢阿

- [graphql-lua](https://github.com/bjornbytes/graphql-lua) - Lua 的 GraphQL。

<a name="elm" />

### 榆树

- [elm-graphql](https://github.com/dillonkearns/elm-graphql) - Elm 的 GraphQL。

<a name="clojure" />

### 克洛尤尔

- [graphql-clj](https://github.com/tendant/graphql-clj) - 旨在提供 GraphQL 实现的 Clojure 库。
- [Lacinia](https://github.com/walmartlabs/lacinia) - 纯 Clojure 中的 GraphQL 实现。
- [graphql-query](https://github.com/district0x/graphql-query) - Clojure（脚本）GraphQL 查询生成。

<a name="clojure-example" />

#### Clojure 示例

- [Clojure Game Geek](https://github.com/walmartlabs/clojure-game-geek) - Lacinia GraphQL 框架教程的示例代码。

<a name="swift" />

### 斯威夫特

- [GraphQL](https://github.com/GraphQLSwift/GraphQL) - GraphQL 的 Swift 实现。

<a name="ocaml" />

### 奥卡米尔

- [ocaml-graphql-server](https://github.com/andreas/ocaml-graphql-server) - OCaml 中的 GraphQL 服务器。

<a name="android" />

### 安卓

- [apollo-android](https://github.com/apollographql/apollo-android) - 📟 适用于 Android 的强类型缓存 GraphQL 客户端，用 Java 编写。
- [manifold-graphql](https://github.com/manifold-systems/manifold/tree/master/manifold-deps-parent/manifold-graphql) - 全面的 GraphQL 客户端使用。模式优先。类型安全的 GraphQL 类型、查询和结果，没有代码生成器、没有 POJO、没有注释。 IntelliJ IDEA 和 Android Studio 提供出色的 [IDE 支持](http://manifold.systems/images/graphql.mp4)。请参阅下面的 [Java 示例](#example-java)。

<a name="android-example" />

#### Android 示例

- [apollo-frontpage-android-app](https://github.com/rnitame/apollo-frontpage-android-app) - 📄 Apollo“hello world”应用程序，适用于 Android。

<a name="ios" />

### iOS系统

- [apollo-ios](https://github.com/apollographql/apollo-ios) - 📱 用于 iOS 的强类型缓存 GraphQL 客户端，用 Swift 编写。
- [ApolloDeveloperKit](https://github.com/manicmaniac/ApolloDeveloperKit) - 适用于 [Apollo iOS] 的 Apollo 客户端 Devtools 桥接器。
- [Graphaello](https://github.com/nerdsupremacist/Graphaello) - 直接从 SwiftUI 输入 Safe GraphQL。

<a name="ios-example" />

#### iOS 示例

- [frontpage-ios-app](https://github.com/apollographql/frontpage-ios-app) - 📄 Apollo“hello world”应用程序，适用于 iOS。

<a name="clojurescript" />

### Clojure脚本

- [re-graph](https://github.com/oliyh/re-graph) - ClojureScript 的 GraphQL 客户端，具有用于重新构建应用程序的绑定。
- [graphql-query](https://github.com/district0x/graphql-query) - Clojure（脚本）GraphQL 查询生成。

<a name="reasonml" />

### ReasonML

- [reason-apollo](https://github.com/apollographql/reason-apollo) - Apollo 客户端的 ReasonML 绑定。
- [ReasonQL](https://github.com/sainthkh/reasonql) - 面向 ReasonML 开发人员的类型安全且简单的 GraphQL 客户端。
- [reason-urql](https://github.com/FormidableLabs/reason-urql) - urql 客户端的 ReasonML 绑定。

<a name="dart" />

### 飞镖

- [graphql-flutter](https://github.com/zino-app/graphql-flutter) - Flutter 的 GraphQL 客户端。
- [Artemis](https://github.com/comigor/artemis) - 用于 Dart/Flutter 的 GraphQL 类型和查询生成器。

<a name="rust" />

### 铁锈

- [async-graphql](https://github.com/async-graphql/async-graphql) - 支持所有 GraphQL 规范的高性能服务器端库。
- [juniper](https://github.com/graphql-rust/juniper) - Rust 的 GraphQL 服务器库。
- [graphql-client](https://github.com/tomhoule/graphql-client) - 用于 Rust 的 GraphQL 客户端库，支持 WebAssembly (wasm)。
- [graphql-parser](https://github.com/graphql-rust/graphql-parser) - 用于 Rust 的 GraphQL 查询和模式定义语言的解析器、格式化程序和 AST。
- [tailcall](https://github.com/tailcallhq/tailcall) - 用于构建高性能 GraphQL 后端的平台。

<a name="rust-example" />

#### 生锈的例子

- [Warp GraphQL 瞻博网络](https://graphql-rust.github.io/)
- [Tailcall](https://tailcall.run/docs/)

<a name="d" />

### D (dlang)

- [graphqld](https://github.com/burner/graphqld) - D 的 GraphQL 服务器库

<a name="r" />

### R（R统计）

- [ghql](https://github.com/ropensci/ghql) - 通用 GraphQL R 客户端。
- [graphql](https://github.com/ropensci/graphql) - 绑定到“libgraphqlparser”C++ 库。解析 GraphQL 语法并以 JSON 格式导出 AST。
- [gqlr](https://github.com/schloerke/gqlr) - R GraphQL 实现。

<a name="julia" />

### 朱莉娅

- [Diana.jl](https://github.com/codeneomatrix/Diana.jl) - Julia GraphQL 客户端/服务器实现。
- [GraphQLClient.jl](https://github.com/DeloitteDigitalAPAC/GraphQLClient.jl) - 用于与服务器无缝集成的 Julia GraphQL 客户端。

<a name="crystal" />

### 水晶

- [graphql](https://github.com/graphql-crystal/graphql) - GraphQL 服务器库。
- [graphql-crystal](https://github.com/ziprandom/graphql-crystal) - 库的灵感来自 [graphql-ruby](https://github.com/rmosolgo/graphql-ruby) & [go-graphql](https://github.com/playlyfe/go-graphql) & [graphql-parser](https://github.com/graphql-dotnet/parser)。
- [crystal-gql](https://github.com/itsezc/crystal-gql) - GraphQL 客户端分片受到 Apollo 客户端的启发。
- [graphql.cr](https://github.com/garymardell/graphql.cr) - GraphQL 分片。

### 芭蕾舞女演员

- [graphql](https://github.com/ballerina-platform/module-ballerina-graphql) - GraphQL 的 Ballerina 标准库。该库提供了 GraphQL 客户端和服务器实现，包括对 GraphQL 订阅的内置支持。
- [graphql CLI](https://github.com/ballerina-platform/graphql-tools) - 一个 CLI 工具，用于从 GraphQL 架构生成 Ballerina 代码，并从 Ballerina 代码生成 GraphQL 架构。它还提供使用 GraphQL 模式和文档生成特定于使用情况的 GraphQL 客户端的功能。

#### 芭蕾舞演员样品

- [芭蕾舞女演员 GraphQL 示例](https://github.com/ballerina-platform/module-ballerina-graphql/tree/master/examples)
- [将天气 REST API 转换为 GraphQL API](https://github.com/ThisaruGuruge/weather-rest-api-to-graphql)

<a name="tools" />

## 工具

### 工具 - 编辑器、IDE 和浏览器

- [GraphiQL](https://github.com/graphql/graphiql) - 用于探索 GraphQL 的浏览器内 IDE。
- [GraphQL Editor](https://github.com/graphql-editor/graphql-editor) - 可视化编辑器和 GraphQL IDE。
- [GraphQL Voyager](https://github.com/APIs-guru/graphql-voyager) - 将任何 GraphQL API 表示为交互式图表。
- [Altair GraphQL Client](https://github.com/altair-graphql/altair) - 适用于所有平台、功能丰富、美观的 GraphQL 客户端。
- [Brangr](https://github.com/networkimprov/brangr) - 适用于任何 GraphQL 服务的独特、用户友好的数据浏览器/查看器，具有有吸引力的结果布局。
- [Insomnia](https://insomnia.rest/) - 带有第一方 GraphQL 查询编辑器的全功能 API 客户端。
- [Postman](https://learning.postman.com/docs/sending-requests/supported-api-frameworks/graphql/) - 支持编辑 GraphQL 查询的 HTTP 客户端。
- [Bruno](https://github.com/usebruno/bruno) - 快速的开源 API 客户端，仅以 Git 友好的纯文本标记语言离线存储集合。
- [Escape GraphMan](https://github.com/Escape-Technologies/graphman) - 从 GraphQL 端点生成完整的 Postman 集合。
- [Apollo Sandbox](https://sandbox.apollo.dev/) - 导航和测试 GraphQL 端点的最快方法。
- [GraphQL Birdseye](https://github.com/Novvum/graphql-birdseye) - 将任何 GraphQL 架构视为动态交互式图表。
- [AST Explorer](https://astexplorer.net/) - 选择顶部的“GraphQL”，探索 GraphQL AST 并通过单击查询突出显示不同的部分。
- [Firecamp - GraphQL Playground](https://firecamp.io/graphql) - 最快的协作 GraphQL 游乐场。
- [CraftQL](https://github.com/yamafaktory/craftql) - 一个 CLI 工具，用于可视化 GraphQL 模式并将图形数据结构输出为 graphviz .dot 格式。
- [gqt](https://github.com/eerimoq/gqt) - 在终端中构建并执行 GraphQL 查询。
- [Hackolade](https://studio.hackolade.com/) - 可视化 GraphQL 架构编辑器，无需了解 GraphQL 语法即可生成架构定义语言文件。还可以通过内省来可视化和记录现有端点。  其他信息和说明[此处](https://hackolade.com/help/GraphQL.html)
- [Smart Formatter - GraphQL Query Formatter](https://smartformatter.com/tools/graphql-query-formatter) - 一个仅限浏览器的客户端工具，用于立即格式化、美化和验证 GraphQL 查询和模式。


<a name="tool-testing" />

### 工具 - 测试、原型设计和模拟

- [Beeceptor](https://beeceptor.com/graphql-mock-server/) - 一个无代码平台，用于从您的模式 (SDL) 创建人工智能驱动的 **GraphQL 模拟服务器**，具有规则、状态模拟、突变/订阅，以加快开发和集成测试。
- [graphql-to-karate](https://github.com/wbaldoumas/graphql-to-karate) - **从 GraphQL 架构生成空手道 API 测试**
- [GraphQL Faker](https://github.com/APIs-guru/graphql-faker) - 🎲 使用伪造的数据模拟或扩展您的 GraphQL API。无需编码。
- [GraphQL Inspector](https://the-guild.dev/graphql/inspector) - 用于**验证架构**、比较架构更改、查找重大更改以及根据架构检查文档覆盖率的工具。
- [Microcks](https://microcks.io/) - 开源（[CNCF](https://www.cncf.io/projects/microcks/) 项目）、用于 **API Mocking** 的云原生工具以及使用 [GraphQL 支持](https://microcks.io/blog/graphql-features-what-to-expect/) 进行测试 🎥 [GraphQL conf 2023](https://youtu.be/UjDnrrTp7uI?si=M6S4l_Bukp9CEYl4)
- [mockd](https://github.com/getmockd/mockd) - 具有 GraphQL 模式模拟、解析器配置和查询验证的多协议模拟服务器。还支持 HTTP、gRPC、WebSocket、MQTT 和 SOAP。
- [Keploy](https://keploy.io/) - 开源 AI 支持的 API 测试工具，可通过记录真实 API 流量自动生成测试用例和**数据模拟。支持 GraphQL、REST 和 gRPC。
- [Step CI](https://stepci.com) - 具有 GraphQL 支持的开源 API **测试和监控**

<a name="tool-security" />

### 工具 - 安全

- [GraphCrawler - The all-in-one GraphQL Security toolkit](https://github.com/gsmith257-cyber/GraphCrawler) - 用 Python 编写的 GraphQL 一体化自动化渗透测试工具包
- [Escape - The GraphQL Security Scanner](https://graphql.security/) - 对 GraphQL 端点进行一键安全扫描。免费，无需登录。
- [Escape Graphinder - GraphQL Subdomain Enumeration](https://github.com/Escape-Technologies/graphinder) - 使用子域枚举、脚本分析和暴力破解的超快 GraphQL 端点查找器。
- [StackHawk - GraphQL Vulnerability Scanner](https://www.stackhawk.com/blog/automated-graphql-security-testing) - [StackHawk](https://www.stackhawk.com)
- [InQL Scanner](https://github.com/doyensec/inql) - 用于 GraphQL 安全测试的 Burp 扩展
- [GraphQL攻略](https://portswigger.net/bappstore/4841f0d78a554ca381c65b26d48207e6) [BurpSuite](https://portswigger.net/burp)
- [WAF for graphQL](https://lab.wallarm.com/api-security-solution/) - graphQL API 的 Web 应用程序防火墙
- [GraphQL Intruder](https://github.com/davinerd/gql_intruder) - 基于插件的 python 脚本来执行 GraphQL 漏洞评估。
- [GraphQL Cop](https://github.com/dolevf/graphql-cop) - GraphQL 的安全审计实用程序
- [GraphQLer](https://github.com/omar2535/GraphQLer) - 依赖关系感知的动态 GraphQL 测试工具
- [Vulert](https://vulert.com) - Vulert 通过检测开源依赖项中的漏洞来保护软件，而无需访问您的代码。它支持 Js、PHP、Java、Python 等

### 工具 - 浏览器扩展

- [Apollo Client Developer Tools](https://github.com/apollographql/apollo-client-devtools) - Chrome 开发者控制台中 Apollo Client 的 GraphQL 调试工具
- [GraphQL Network Inspector](https://chrome.google.com/webstore/detail/graphql-network-inspector/ndlbedplllcgconngcnfmkadhokfaaln) - 一个简单干净的 chrome 开发工具扩展，用于 GraphQL 网络检查。

### 工具 - 文档

- [graphdoc](https://github.com/2fd/graphdoc) - 用于记录 GraphQL 架构的静态页面生成器。
- [gqldoc](https://github.com/Code-Hex/gqldoc) - 为 GraphQL 制作 API 文档的最简单方法。
- [spectaql](https://github.com/anvilco/spectaql) - 自动生成静态 GraphQL API 文档。
- [graphql-markdown](https://graphql-markdown.github.io/) - 由 Docusaurus 提供支持的 GraphQL 的灵活文档。
- [xyd](https://xyd.dev) - 生成 GraphQL API 文档。

### 工具 - 编辑器插件

- [Apollo GraphQL VSCode Extension](https://marketplace.visualstudio.com/items?itemName=apollographql.vscode-apollo) - 丰富的编辑器支持 GraphQL 客户端和服务器开发，与 Apollo 平台无缝集成
- [js-graphql-intellij-plugin](https://github.com/jimkyndemeyer/js-graphql-intellij-plugin/) - 对 IntelliJ IDEA 和 WebStorm 的 GraphQL 语言支持，包括 JavaScript 和 TypeScript 中的 Relay.QL 标记模板。
- [vim-graphql](https://github.com/jparise/vim-graphql) - 一个 Vim 插件，提供 GraphQL 文件检测和语法突出显示。
- [graphql-autocomplete](https://github.com/orionsoft/atom-graphql-autocomplete) - 从 Atom 中的 GraphQL 端点自动完成和 lint。

### 工具 - 杂项

- [graphql-code-generator](https://github.com/dotansimha/graphql-code-generator) - 基于模式和文档的 GraphQL 代码生成器。
- [swagger-to-graphql](https://github.com/yarax/swagger-to-graphql) - 基于 Swagger 中描述的 REST API 的 GraphQL 类型构建器。允许从 REST 迁移到 GraphQL 5 分钟
- [ts-graphql-plugin](https://github.com/Quramy/ts-graphql-plugin) - 语言服务插件完成并验证 TypeScript 模板字符串中的 GraphQL 查询。
- [apollo-tracing](https://github.com/apollographql/apollo-tracing) - GraphQL 扩展使您能够轻松获取解析器级别的性能信息作为 GraphQL 响应的一部分。
- [json-graphql-server](https://github.com/marmelab/json-graphql-server) - 基于 JSON 数据文件，在 30 秒内获得零编码的完整假 GraphQL API。
- [Prisma](https://github.com/prisma/prisma) - 将您的数据库转变为 GraphQL API。 Prisma 可让您设计数据模型，并在几分钟内在线获得生产就绪的 GraphQL API。
- [Typetta](https://github.com/twinlogix/typetta) - 用 TypeScript 为类型爱好者编写的 Node.js ORM。 Typetta 是 GraphQL + NodeJS + Typescript 堆栈的完美 ORM。
- [tuql](https://github.com/bradleyboy/tuql) - 从任何 sqlite 数据库自动创建 GraphQL 服务器。
- [Bit](https://github.com/teambit/bit) - 将 GraphQL API 组织为组件，供 NPM 使用或从任何项目进行修改，[example-explanation](https://hackernoon.com/make-your-graphql-api-easier-to-adopt-through-components-74b022f195c1))。
- [openapi-to-graphql](https://github.com/ibm/openapi-to-graphql) - 采用任何 OpenAPI 规范 (OAS) 或 swagger 并创建 GraphQL 界面 - 两分钟视频和资源 [此处](https://developer.ibm.com/open/projects/openapi-to-graphql/)
- [Retool](https://retool.com/) - GraphQL API + GraphQL IDE 之上的内部工具构建器，带有模式浏览器。
- [dataloader-codegen](https://github.com/Yelp/dataloader-codegen) - 一个固执己见的 JavaScript 库，用于通过一组资源（例如 HTTP 端点）自动生成可预测的、类型安全的 DataLoader。
- [raphql-inspector](https://github.com/kamilkisiela/graphql-inspector)：验证模式、获取模式更改通知、验证操作、查找重大更改、查找相似类型、模式覆盖率。
- [amplication](https://github.com/amplication/amplication)：Amplication 是一个开源低代码开发工具。它使用 REST API 和 GraphQL 构建具有关系、排序、过滤、分页功能的 CRUD 数据库应用程序。
- [Blendbase](https://github.com/blendbase/blendbase)：单个开源 GraphQL API，用于将 CRM 连接到 SaaS。使用 SaaS 应用程序中的单个 API 查询来查询任何客户 CRM 系统（Salesforce、Hubspot 等）。
- [microfiber](https://github.com/anvilco/graphql-introspection-tools) - 以有用的方式查询和操作 GraphQL 自省查询结果。
- [DronaHQ](https://www.dronahq.com/) - 在几分钟内基于 GraphQL 数据构建内部工具、仪表板、管理面板
- [Dynaboard](https://dynaboard.com) - 使用 AI 从任何 GraphQL API 生成低代码 Web 应用程序。
- [gqlhash](https://github.com/romshark/gqlhash) - 闪电般的快速查询哈希器，忽略格式差异和注释，并支持多种哈希函数。
- [Apollo APQ Debugger](https://github.com/rookieInTraining/apq-debugger) - 揭示 Apollo APQ 哈希背后的完整 GraphQL 查询。在 DevTools 中检查回退流程并调试自动持久查询。
  <a name="databases" />


## 数据库

- [Cube](https://cube.dev) - [Headless BI](https://cube.dev/blog/headless-bi)，用于使用 SQL、REST 和 [GraphQL API](https://cube.dev/docs/backend/graphql) 构建数据应用程序。连接任何数据库或数据仓库，立即获得具有亚秒级延迟的 GraphQL API。 - [源代码](https://github.com/cube-js/cube.js)
- [Dgraph](https://dgraph.io/) - 可扩展、分布式、低延迟、高吞吐量以 GraphQL 作为查询语言的图数据库
- [EdgeDB](https://edgedb.com/) - 具有原生 GraphQL 支持的下一代对象关系数据库。
- [ArangoDB](https://arangodb.com/) - 通过内置的 [Foxx 微服务框架](https://www.arangodb.com/docs/stable/foxx.html) 实现具有 [GraphQL 集成](https://www.arangodb.com/docs/3.4/foxx-reference-modules-graph-ql.html) 的本机多模型数据库。
- [Weaviate](https://github.com/semi-technologies/weaviate) - Weaviate 是一个云原生、模块化、实时矢量搜索引擎，具有 [GraphQL 接口](https://weaviate.io/developers/weaviate/api/graphql)，旨在扩展您的机器学习模型。

<a name="services" />

## 服务

- [AWS AppSync](https://aws.amazon.com/appsync/) - 可扩展的托管 GraphQL 服务，具有用于构建实时和离线优先应用程序的订阅

- [Moesif API Analytics](https://www.moesif.com/features/graphql-analytics) - 用于查找功能和性能问题的 GraphQL 分析和监控服务。
- [Booster framework](https://booster.cloud/) - 一个开源框架，让您_完全_忘记基础设施，并允许您专注于您的业务逻辑。它会为您的模型自动生成 GraphQL API，支持突变、查询和订阅。
- [Nhost](https://nhost.io/) - 使用 GraphQL 的开源 Firebase 替代品
- [Saleor](https://github.com/mirumee/saleor/) - GraphQL-第一个无头电子商务平台。
- [Stargate](https://stargate.io/docs/latest/quickstart/qs-graphql-cql-first.html) - 目前支持 Apache Cassandra® 的开源数据网关和 DataStax Enterprise。
- [Vedika](https://vedika.io) - 吠陀占星学 AI API，具有 GraphQL 支持星座、出生图、kundali 匹配和 108 个以上端点。
- [Grafbase](https://grafbase.com) - 适用于任何数据源的即时 GraphQL API。

### CDN

- [GraphCDN](https://graphcdn.io/) - 用于缓存 GraphQL API 的 GraphQL CDN。

### 内容管理系统

- [DatoCMS](https://www.datocms.com/) - 基于 CDN GraphQL 的无头内容管理系统。
- [Apito](https://apito.io/) - 基于云的 Headless CMS，具有 CDN、Webhooks、团队协作、内容修订、云功能。
- [Hygraph](https://hygraph.com/) - 构建可扩展的内容体验。
- [Cosmic](https://www.cosmicjs.com/) - GraphQL 支持的 Headless CMS 和 API 工具包。
- [Graphweaver](https://graphweaver.com/) - 将多个数据源转换为单个 GraphQL API。

<a name="book" />

## 书籍

- [GraphQL 指南](https://graphql.guide) 作者：John Resig 和 Loren Sands-Ramshaw
- [使用苦艾酒在 Elixir 中制作 GraphQL API](https://pragprog.com/book/wwgraphql/craft-graphql-apis-in-elixir-with-absinthe) 作者：Bruce Williams 和 Ben Wilson
- [GraphQL 之路](https://www.roadtographql.com/)
- [实用 GraphQL](https://leanpub.com/book-graphql) 作者：Daniel Schmitz
- [生产就绪 GraphQL](https://book.productionreadygraphql.com) 作者：Marc-André Giroux
- [全栈 GraphQL 应用程序](https://www.manning.com/books/fullstack-graphql-applications) 作者：William Lyon

<a name="video" />

## 视频

- [GraphQL：纪录片](https://www.youtube.com/watch?v=783ccP__No8)
- [30 分钟内从零到 GraphQL](https://www.youtube.com/embed/UBGzsb2UkeY)
- [Facebook 的 React 应用程序的数据获取](https://www.youtube.com/watch?v=9sc8Pyc51uU)
- [React Native 和 Relay：将现代 Web 技术引入移动设备](https://www.youtube.com/watch?v=X6YbAKiLCLU)
- [探索 GraphQL](https://www.youtube.com/watch?v=WQLzZf34FJ8)
- [创建 GraphQL 服务器](https://www.youtube.com/watch?v=gY48GW87Feo)
- [《金融时报》中的 GraphQL](https://www.youtube.com/watch?v=S0s935RKKB4)
- [Relay：React 应用程序框架](https://www.youtube.com/watch?v=IrgHurBjQbg)
- [使用 Facebook 构建和部署 Relay](https://www.youtube.com/watch?t=643&v=Pxdgu2XIAAg)
- [GraphQL 简介](https://vimeo.com/144817545)
- [探索 GraphQL@Scale](https://www.youtube.com/watch?v=_9RgHXqH8J0)
- [克里斯·麦考德《凤凰城的下一步是什么》](https://www.youtube.com/watch?v=IMUpYOc9z3c&feature=youtu.be)
- [GraphQL 与 Nick Schrock](https://www.youtube.com/watch?v=Ed6oJXKt3-M)
- [使用 PostgreSQL/MySQL 为 Node.js 构建 GraphQL 服务器](https://www.youtube.com/watch?v=DNPVqK_woRQ)
- [Node.js 与 SQL、MongoDB 和 REST 的 GraphQL 服务器教程](https://www.youtube.com/watch?v=PHabPhgRUuU)
- [JavaScript Air 第 023 集：从 REST 过渡到 GraphQL](https://www.youtube.com/watch?v=ENqDNIp1Nd8)
- [2016 年 React-europe 上的 GraphQL 未来](https://www.youtube.com/watch?v=ViXL0YQnioU)
- [Facebook 在 React-europe 2016 上的 GraphQL](https://www.youtube.com/watch?v=etax3aEe2dA)
- [在 React-europe 2016 上使用 GraphQL 构建原生移动应用程序](https://www.youtube.com/watch?v=z5rz3saDPJ8)
- [构建 GraphQL 服务器](https://www.youtube.com/watch?v=PEcJxkylcRM&list=PLillGF-RfqbYZty73_PHBqKRDnv7ikh68)
- [GraphQL 教程](https://www.youtube.com/watch?v=Y0lDGjwRYKw&list=PL4cUxeGkcC9iK6Qhn-QLcXCXPQUov1U7f)
- [GraphQL 五年](https://www.youtube.com/watch?v=s8meG38iZAM)
- [GraphQL 适合 Moon Highway 上的所有人](https://moonhighway.teachable.com/p/graphql-is-for-everyone)

<a name="podcast" />

## 播客

- [GraphQL.FM](https://podcasts.google.com/feed/aHR0cHM6Ly9hbmNob3IuZm0vcy8zNjE5NmViMC9wb2RjYXN0L3Jzcw==) 作者：Marc-Andre Giroux 和 Tony Ghita。

<a name="style-guide" />

## 风格指南

- [Shopify GraphQL Design Tutorial](https://github.com/Shopify/graphql-design-tutorial) - 本教程最初是由 Shopify 出于内部目的而创建的。它基于 Shopify 近 3 年创建和发展生产模式的经验教训。
- [GitLab GraphQL API Style Guide](https://docs.gitlab.com/ee/development/api_graphql_styleguide.html) - 本文档概述了 GitLab GraphQL API 的样式指南。
- [Yelp GraphQL Guidelines](https://yelp.github.io/graphql-guidelines/) - 该存储库包含标准化且最合理的 GraphQL 方法的文档和指南（在 Yelp 上）。
- [Principled GraphQL](https://principledgraphql.com/) - Apollo 的 10 条 GraphQL 原则分为三类，其格式受到十二因素应用程序的启发。

<a name="blogs" />

## 博客

- [官方 GraphQL 博客](https://graphql.org/blog/)
- [建造阿波罗](https://blog.apollographql.com/)
- [公会博客](https://medium.com/the-guild)
- [生产就绪 GraphQL 博客](https://productionreadygraphql.com)

<a name="security-blog" />

### 博客 - 安全

- [Escape - The GraphQL Security Blog](https://escape.tech/blog) - 了解 GraphQL 安全性、性能、测试以及使用 GraphQL 生态系统的最新工具和最佳实践构建生产就绪的 API。
- [9 个 GraphQL 安全最佳实践](https://escape.tech/blog/9-graphql-security-best-practices/)
- [发现 GraphQL 端点和 SQLi 漏洞](https://medium.com/@localh0t/discovering-graphql-endpoints-and-sqli-vulnerabilities-5d39f26cea2e)
- [保护 GraphQL API 的安全](https://lab.wallarm.com/securing-graphql-api/)
- [实施 GraphQL 之前要考虑的安全点](https://nordicapis.com/security-points-to-consider-before-implementing-graphql/)
- [GraphQL 中的授权模式](https://www.osohq.com/post/graphql-authorization)

<a name="post" />

## 帖子

- [使用 Apollo Federation 和 Apollo GraphOS 的 GraphQL 联合示例](https://cube.dev/blog/graphql-federation-example-with-apollo-federation-and-apollo-graphos)
- [GraphQL 与 Hasura GraphQL Engine 和 Cube 的联合](https://cube.dev/blog/graphql-federation-with-hasura-graphql-engine)
- [使用 DataLoader 批量处理 GraphQL 请求](https://medium.com/@gajus/using-dataloader-to-batch-requests-c345f4b23433)
- [介绍 Relay 和 GraphQL](https://reactjs.org/blog/2015/02/20/introducing-relay-and-graphql.html)
- [GraphQL 简介](https://reactjs.org/blog/2015/05/01/graphql-introduction.html)
- [非官方中继常见问题解答](https://gist.github.com/wincent/598fa75e22bdfa44cf47)
- [您的第一个 GraphQL 服务器](https://medium.com/the-graphqlhub/your-first-graphql-server-3c766ab4f0a2)
- [GraphQL 概述 - GraphQL 和 Node.js 入门](https://blog.risingstack.com/graphql-overview-getting-started-with-graphql-and-nodejs/)
- [您应该尝试 GraphQL 的 4 个理由](https://medium.freecodecamp.org/introduction-to-graphql-1d8011b80159)
- [从 REST 迁移到 GraphQL](https://medium.com/@frikille/moving-from-rest-to-graphql-e3650b6f5247)
- [使用 GraphQL 编写基本 API](http://davidandsuzi.com/writing-a-basic-api-with-graphql/)
- [使用 Node.js 和 SQL 构建 GraphQL 服务器](https://www.reindex.io/blog/building-a-graphql-server-with-node-js-and-sql/)
- [《金融时报》中的 GraphQL](https://www.slideshare.net/LondonReact/graph-ql)
- [实施 GraphQL RBAC 授权：实用指南](https://www.permit.io/blog/implementing-graphql-authorization)
- [从 REST 到 GraphQL](https://jacobwgillespie.com/2015-10-09-from-rest-to-graphql)
- [GraphQL：一种数据查询语言](https://graphql.org/blog/graphql-a-query-language/)
- [GraphQL 和 Relay 中的订阅](https://graphql.org/blog/subscriptions-in-graphql-and-relay/)
- [Relay 101：构建黑客新闻客户端](https://medium.com/@clayallsopp/relay-101-building-a-hacker-news-client-bb8b2bdc76e6)
- [GraphQL Schema Reference](https://graphql.org/learn/schema/) - 解释 GraphQL 模式定义语言和速记符号的官方文档。
- [GitHub GraphQL API](https://githubengineering.com/the-github-graphql-api/)
- [Github GraphQL API React 示例](https://medium.com/@katopz/github-graphql-api-react-example-eace824d7b61)
- [使用 Jest 测试 GraphQL Server](https://medium.com/entria/testing-a-graphql-server-using-jest-4e00d0e4980e)
- [如何在 GraphQL 中实现viewerCanSee](https://medium.com/entria/how-to-implement-viewercansee-in-graphql-78cc48de7464)
- [防止对 GraphQL API 的遍历攻击](https://blog.morethancode.dev/preventing-traversal-attacks-in-your-graphql-api/)
- [使用 faker.js 真实模拟您的 GraphQL 服务器](https://dev.to/yvonnickfrin/mock-your-graphql-server-realistically-with-faker-js-25oo)
- [使用 React 和 GraphQL 创建无限加载列表](https://dev.to/yvonnickfrin/create-an-infinite-loading-list-with-react-and-graphql-19hh)
- [REST 与 GraphQL](https://www.moesif.com/blog/technical/graphql/REST-vs-GraphQL-APIs-the-good-the-bad-the-ugly/)
- [GraphQL API 的身份验证和授权](https://www.moesif.com/blog/technical/api-design/Steps-to-Building-Authentication-and-Authorization-For-GraphQL-APIs/)
- [在 Swoole 之上使用 Siler 构建 GraphQL API](https://www.swoole.co.uk/article/Build-a-GraphQL-API-on-top-of-Swoole)
- [Fluent GraphQL 客户端：如何像老板一样编写查询](https://hasura.io/blog/fluent-graphql-clients-how-to-write-queries-like-a-boss/)
- [使用 GraphQL 数据即服务层升级您的无服务器游戏](https://hasura.io/blog/level-up-your-serverless-game-with-a-graphql-data-as-a-service-layer/)
- [深入研究 Relay，这是一个友好且固执己见的 GraphQL 客户端](https://hasura.io/blog/deep-dive-into-relay-graphql-client/)
- [通过组件让你的 graphql api 更容易被采用](https://hackernoon.com/make-your-graphql-api-easier-to-adopt-through-components-74b022f195c1)
- [未记录：将 GraphQL 模式的部分内容隐藏起来以防止内省](https://www.useanvil.com/blog/engineering/undocumented-directive/)
- [Ballerina 中使用 Apache Kafka 进行 GraphQL 订阅](https://medium.com/ballerina-techblog/graphql-subscriptions-with-apache-kafka-in-ballerina-b3c296d333cd)
- [如何测试您的 GraphQL 端点](https://escape.tech/blog/8-most-common-graphql-vulnerabilities/)
- [为什么自动持久查询无法扩展](https://blog.tailcall.run/the-truth-about-scaling-automatic-persisted-queries/)

<a name="tutorials" />

## 教程

- [How to GraphQL](https://www.howtographql.com) - Fullstack 教程网站，包含所有主要框架和语言的跟踪，包括 React、Apollo、Relay、JavaScript、Ruby、Java、Elixir 等等。
- [Apollo Odyssey](https://odyssey.apollographql.com/) - Apollo 的免费互动学习平台。
- [learning-graphql](https://github.com/mugli/learning-graphql) - 尝试学习 GraphQL。
- [GraphQL Roadmap](https://roadmap.sh/graphql) - 学习 GraphQL 的分步指南。
- [OWASP GraphQL Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/GraphQL_Security_Cheat_Sheet.html) - 用于保护 GraphQL 端点和防止漏洞的综合指南。

## 许可证

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

在法律允许的范围内，[Chen-Tsu Lin](https://github.com/chentsulin) 已放弃本作品的所有版权以及相关或邻接权。
