# 很棒的接力赛 [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
基于 [Awesome](https://github.com/sindresorhus/awesome/) 项目的 [Relay](https://github.com/facebook/relay) 很棒的资源

# 目录
- [学习资源](#learning-resources)
  - [Documentation](#documentation)
  - [FAQs](#faqs)
  - [Tutorials](#tutorials)
  - [Overviews](#overviews)
  - [示例实现](#example-implementations)
  - [列表列表](#lists-of-lists)
- [Ecosystem](#ecosystem)
  - [库和包](#libraries--packages)
  - [Tooling](#tooling)
  - [入门套件](#starter-kits)
- [中继特定服务器支持](#relay-specific-server-support)
  - [Go](#go)
  - [JavaScript](#javascript)
  - [Python](#python)
  - [Ruby](#ruby)
    - [Rails](#rails)
  - [Scala](#scala)
- [Testing](#testing)

# 学习资源
## 文档
- [Official Docs](https://facebook.github.io/relay/docs/getting-started.html#content) - 官方中继文档。

## 常见问题解答
- [Unofficial Relay FAQ](https://gist.github.com/wincent/598fa75e22bdfa44cf47) - 常见问题解答！目前中继资源稀缺，因此如果您遇到困难，这将非常有帮助。

## 教程
- [Getting Started with Relay](https://auth0.com/blog/2015/10/06/getting-started-with-relay/) - 为数不多的动手接力详细演练之一。
- [Relay 101: Building A Hacker News Client](https://medium.com/@clayallsopp/relay-101-building-a-hacker-news-client-bb8b2bdc76e6#.1i64q1pf9) - 一个完整的可行的例子。
  - [Relay 102: Mutations](https://medium.com/@clayallsopp/relay-102-mutations-d8b471a4730e#.i9vuv3vxl) - 《接力 101》的后续作品，重点关注突变。
- [Facebook Relay talk - Lunch and Learn session](https://www.youtube.com/watch?v=sP3n-nht0Xo) - 构建简单应用程序的演练以及 [GraphiQL](https://github.com/graphql/graphiql) 的演示。
- [A Beginner's Guide to Relay Mutations](http://blog.pathgather.com/blog/a-beginners-guide-to-relay-mutations) - 深度突变。
- [Learn Relay](https://learnrelay.org/) - 向您展示如何制作以 Pokemon 为主题的 CRUD 应用程序，提供基于云的个人 GraphQL 后端，以便您可以专注于客户端代码。

## 概述
- [React Data Fetching with Relay](http://www.sitepoint.com/react-data-fetching-with-relay/) - 对 Relay 的移动部件和魔法进行清晰的概念概述。
- [Joseph Savona - Relay: An Application Framework For React](https://www.youtube.com/watch?v=IrgHurBjQbg) - Facebook 团队对 Relay 的概念概述。
- [F8 2015 - React Native & Relay: Bringing Modern Web Techniques to Mobile](https://www.youtube.com/watch?v=X6YbAKiLCLU) - Relay 概述，一些关于原理的内容。
- [Relay - Daniel Dembach - Hamburg React.js Meetup](https://www.youtube.com/watch?v=dvWTxy1eY6s) - 对 Relay 的一个很好的总体概述，以及一些替代方案的讨论。最后的问答中涵盖了常见问题。
- [Facebook Relay talk - Lunch and Learn session](https://www.youtube.com/watch?v=sP3n-nht0Xo) - 构建简单应用程序的演练以及 [GraphiQL](https://github.com/graphql/graphiql) 的演示。
- [React with Relay and GraphQL with Andrew Smith](https://www.youtube.com/watch?v=Cfna8gwt9h8) - Relay 和 GraphQL 的高级概述，以及观众的一些有用的讨论。还有其他前端框架的一些讨论。
- [Relay for Visual Learners](http://sgwilym.github.io/relay-visual-learners/) - 一组非常清晰的图表，展示了 Relay 的不同部分如何相互关联。
- [Relay: Seamless Syncing For React](http://www.slideshare.net/BrooklynZelenka/relay-seamless-syncing-for-react-vanjs) - Relay 是什么的概述，以及在生产中使用它的经验的一些讨论。
- Facebook 的 Relay 的卡通介绍 - Relay 的工作原理概述，并附有插图。
  - [第 1 部分：使用 GraphQL 说明您需要哪些数据](https://code-cartoons.com/a-cartoon-intro-to-facebook-s-relay-part-1-3ec1a127bca5)
  - [第 2 部分：从服务器获取数据](https://code-cartoons.com/a-cartoon-intro-to-facebook-s-relay-part-2-d4a2435aee59)
  - [第 3 部分：将更改同步回服务器](https://code-cartoons.com/a-cartoon-intro-to-facebook-s-relay-part-3-9d8fcf8db670)
  - [第 4 部分：这一切如何结合在一起](https://code-cartoons.com/a-cartoon-intro-to-facebook-s-relay-part-4-aef7d819a8ed)
 
## 示例实现
- [Relay TODO MVC](https://github.com/taion/relay-todomvc) - 经典的 TODO 示例应用程序，使用 Relay 编写。
- [`relay-chat`](https://github.com/transedward/relay-chat) - 具有路由和分页功能的中继。
- [`koa-graphql-relay-example`](https://github.com/chentsulin/koa-graphql-relay-example) - 带有 [`koa-graphql`](https://github.com/chentsulin/koa-graphql) 和 `relay` 的“TODO”应用程序。
- [`todomvc-relay-go`](https://github.com/sogko/todomvc-relay-go) - Relay TodoMVC 应用程序，由 Golang GraphQL 后端驱动。

## 列表列表
- [Relay 和 GraphQL 介绍材料](https://quip.com/oLxzA1gTsJsE)

# 生态系统
## 库和包
- [`graphql-relay-js`](https://github.com/graphql/graphql-relay-js) - 简化了为“react-relay”创建 JS GraphQL 服务器的过程。
- [Babel Relay Plugin](https://www.npmjs.com/package/babel-relay-plugin) - 使用Relay最新的ES6+语法。
- [`react-router-relay`](https://github.com/relay-tools/react-router-relay) - 中继的“react-router”绑定。极大地简化了许多本地状态 UI 用例。
  - [Relay and Routing](https://medium.com/@cpojer/relay-and-routing-36b5439bad9#.h91614i65) - 清晰地介绍了“react-router-relay”及其解决的问题。
  - [`relay-nested-routes`](https://www.npmjs.com/package/relay-nested-routes) - 生成反映嵌套数据的嵌套路由。有助于管理深层数据。
  - [`isomorphic-relay-router`](https://github.com/denvned/isomorphic-relay-router) - 对“react-router-relay”的服务器端渲染支持。
- [`relay-decorator`](https://github.com/4Catalyzer/relay-decorators) - 具有 ES7 装饰器的 Relay 容器的简单语法（`@` 语法）
- [`recompose-relay`](https://www.npmjs.com/package/recompose-relay) - 通过柯里化并在容器之后提供组件来简化 Relay 容器的组合。
- [`relay-local-schema`](https://github.com/relay-tools/relay-local-schema) - 使用本地模式；不需要远程 GraphQL 服务器。
- [`react-native-relay`](https://github.com/lenaten/react-native-relay) - 将 Relay 与 React Native 结合使用。
- 将来可能会支持[开箱即用](https://github.com/facebook/relay/issues/26)。
- [`relay-sink`](https://github.com/acdlite/relay-sink) - 使用 Relay 在 React 组件外部获取和存储数据。
- [`babel-plugin-flow-relay-query`](https://github.com/guymers/babel-plugin-flow-relay-query) - 将 [Flow](http://flowtype.org) 类型转换为 Relay 片段。
- [`sequelize-relay`](https://github.com/MattMcFarland/sequelize-relay) - 使 Relay 与 [`sequelize`](https://github.com/sequelize/sequelize) 兼容。
- [`relay-mongodb-connection`](https://github.com/mikberg/relay-mongodb-connection) - 从 MongoDB 游标创建中继连接。
- [`relay-composite-network-layer`](https://github.com/eyston/relay-composite-network-layer) - 由许多不同的网络层组成您的中继网络层，每个网络层都有自己的架构。
- [`react-relay-network-layer`](https://github.com/nodkz/react-relay-network-layer) - 添加对查询批处理和中间件的支持的网络层。它还提供了一些有用的中间件，例如用于身份验证、日志记录等。

## 工装
- [GraphiQL](https://github.com/graphql/graphiql) - 一个用于内省 GraphQL、测试查询和突变的库。
  - [GraphiQL App](https://github.com/skevy/graphiql-app) - 一个独立的应用程序，用于查看 GraphQL、内省文档和测试查询/突变。对于调试 Relay 应用程序非常有用。
- [`relay-local-schema`](https://github.com/relay-tools/relay-local-schema) - 使用本地模式；不需要远程 GraphQL 服务器。
- [Babel Relay Plugin](https://www.npmjs.com/package/babel-relay-plugin) - 使用Relay最新的ES6+语法。

## 入门套件
- [Relay Skeleton](https://github.com/fortruce/relay-skeleton) - 中继项目骨架。
- [Relay Starter Kit](https://github.com/relayjs/relay-starter-kit) - 已经通过基本设置设置的应用程序。只需克隆和调整即可满足您的需求！
- [Node.js API Starter Kit](https://github.com/kriasoft/nodejs-api-starter) - 用于使用 Node.js、GraphQL 和 Relay 构建数据 API 的样板文件和工具
- [Simple Relay Starter](https://github.com/mhart/simple-relay-starter) - [Relay Starter Kit](https://github.com/relayjs/relay-starter-kit) 的 Browserify 版本。
- [UniversalRelayBoilerplate](https://github.com/codefoundries/UniversalRelayBoilerplate)
React Native（iOS、Android）、React（同构、Material-UI）、Relay、GraphQL、JWT、Node.js、Apache Cassandra 的样板 + 示例。
- [Relay on Rails Starter Kit](https://github.com/nethsix/relay-on-rails) - 用于 Rails 服务器上的 Relay 应用程序的准系统入门套件。只需克隆和调整即可！
- [Relay Fullstack](https://github.com/lvarayut/relay-fullstack) - Relay 入门套件与 Relay、Express、Webpack、Babel、Material Design Lite 和 PostCSS 集成。

# 中继特定服务器支持
## 去
- [Go Relay](https://github.com/graphql-go/relay) - 一个 Go/Golang 库，可帮助构建支持 React-relay 的 graphql-go 服务器。
- [`todomvc-relay-go`](https://github.com/sogko/todomvc-relay-go) - React/Relay TodoMVC 应用程序，由 Golang GraphQL 后端驱动。

## JavaScript
- [`graphql-relay-js`](https://github.com/graphql/graphql-relay-js) - 简化了为“react-relay”创建 JS GraphQL 服务器的过程。

## 蟒蛇
- [`graphql-relay-py`](https://github.com/graphql-python/graphql-relay-py) - 一个帮助构建支持“react-relay”的“graphql-py”服务器的库。
 
## 红宝石
- [`graphql-relay-ruby`](https://github.com/rmosolgo/graphql-relay-ruby) - GraphQL 和 Ruby 的中继助手。

### 导轨
- [GraphQL and Relay on Rails — First relay powered react component](https://medium.com/@gauravtiwari/graphql-and-relay-on-rails-first-relay-powered-react-component-cb3f9ee95eca#.c88zcoftn) - 完整演练简单的中继设置，包括可克隆代码。
- [Relay/GraphQL On Rails](https://medium.com/@khor/relay-facebook-on-rails-8b4af2057152#.5hjih9wms) - Relay with Rails 的简短示例，配有几个图表以帮助理解。
- [Relay on Rails Starter Kit](https://github.com/nethsix/relay-on-rails) - 用于 Rails 服务器上的 Relay 应用程序的准系统入门套件。只需克隆和调整即可！

## 斯卡拉
- [`sangria-relay`](https://github.com/sangria-graphql/sangria-relay) - 对 [Sangria](http://sangria-graphql.org) 的中继支持。

# 测试
- [Writing Simple Unit Tests with Relay](https://medium.com/@mikaelberg/writing-simple-unit-tests-with-relay-707f19e90129) - 早期对 Relay 测试的初步了解。
