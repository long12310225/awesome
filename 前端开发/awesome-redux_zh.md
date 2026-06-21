# Redux 库和学习材料 [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

[<img src="https://rawgit.com/brillout/awesome-redux/master/redux-logo.svg"align="right" width="110">](http://redux.js.org/)

> Redux 是 JavaScript 应用程序的状态容器。

- 官方网站：[`devarchy.com/redux`](https://devarchy.com/redux)
- 使用 devarchy 将库添加到目录中
 
 <br/>

#### 内容
- [代码架构](#code-architecture)
- [Utilities](#utilities)
- [代码风格](#code-style)
- [开发工具/检查工具](#dev-tools--inspection-tools)
- [反应集成](#react-integration)
- [其他集成](#other-integrations)
- [Boilerplate](#boilerplate)
- [Miscellaneous](#miscellaneous)
- [学习资料](#learning-material)
- [Community](#community)

<br/>

## 代码架构

*旨在完善源代码的整体结构。使代码推理变得更容易。*

 - [redux-schema](https://github.com/ddsol/redux-schema) - Redux 的自动操作、reducers 和验证。
 - [redux-tcomb](https://github.com/gcanti/redux-tcomb) - Redux 的不可变和类型检查状态和操作。
 - [redux-action-tree](https://github.com/cerebral/redux-action-tree) - Cerebral 信号与 Redux 一起运行。
 - [redux-elm](https://github.com/salsita/redux-elm) - JavaScript 中的 Elm 架构。


## 公用事业

 - [redux-orm](https://github.com/tommikaikkonen/redux-orm) - 小型、简单且不可变的 ORM，用于管理 Redux 存储中的关系数据。
 - [redux-api-middleware](https://github.com/agraboso/redux-api-middleware) - 用于调用 API 的 Redux 中间件。
 - [redux-ignore](https://github.com/omnidan/redux-ignore) - 高阶减速器忽略 Redux 操作。
 - [redux-modifiers](https://github.com/calvinfroedge/redux-modifiers) - 用于编写 Redux 减速器以操作各种数据结构的通用函数的集合。
 - [rereduce](https://github.com/slorber/rereduce) - Redux 的减速器库。
 - [redux-search](https://github.com/treasure-data/redux-search) - 用于客户端搜索的 Redux 绑定。
 - [redux-logger](https://github.com/evgenyrodionov/redux-logger) - Redux 的记录器中间件。
 - [redux-immutable](https://github.com/gajus/redux-immutable) - Redux-immutable 用于创建与 Immutable.js 状态一起使用的 Redux mixReducers 的等效函数。
 - [reselect](https://github.com/reactjs/reselect) - Redux 的选择器库。
 - [redux-requests](https://github.com/idolize/redux-requests) - 使用 Redux 减速器管理正在进行的请求，以避免发出重复的请求。
 - [redux-undo](https://github.com/omnidan/redux-undo) - 高阶减速器向 Redux 状态容器添加撤消/重做功能。
 - [redux-bug-reporter](https://github.com/dtschust/redux-bug-reporter) - Redux 的错误报告器和错误回放工具。
 - [redux-transducers](https://github.com/acdlite/redux-transducers) - Redux 的传感器实用程序。


### 存储持久性

 - [redux-storage](https://github.com/michaelcontento/redux-storage) - 具有灵活后端的 Redux 持久层。
 - [redux-persist](https://github.com/rt2zz/redux-persist) - 坚持并补充 Redux 存储。


### 副作用

*副作用/异步操作*

 - [redux-saga](https://github.com/yelouafi/redux-saga) - Redux 应用程序的替代副作用模型。
 - [redux-promise-middleware](https://github.com/pburtchaell/redux-promise-middleware) - Redux 中间件，用于通过有条件的乐观更新来解决和拒绝承诺。
 - [redux-effects](https://github.com/redux-effects/redux-effects) - 您编写纯函数，redux-effects 处理其余的事情。
 - [redux-thunk](https://github.com/gaearon/redux-thunk) - Redux 的 Thunk 中间件。
 - [redux-connect](https://github.com/makeomatic/redux-connect) - 提供装饰器来解析react-router中的异步props，对于处理React中的服务器端渲染非常有用。
 - [redux-loop](https://github.com/redux-loop/redux-loop) - 将 elm-effects 和 Elm Architecture 移植到 Redux，允许您通过从减速器返回效果来自然而纯粹地对效果进行排序。
 - [redux-side-effects](https://github.com/salsita/redux-side-effects) - Redux 工具集用于将所有副作用保留在您的减速器中，同时保持其纯度。
 - [redux-logic](https://github.com/jeffbski/redux-logic) - 用于组织业务逻辑和操作副作用的 Redux 中间件。
 - [redux-observable](https://github.com/redux-observable/redux-observable) - RxJS 中间件使用“Epics”来处理 Redux 中的操作副作用。
 - [redux-ship](https://github.com/clarus/redux-ship) - 可组合、可测试和可输入的副作用。


## 代码风格

*旨在使部分源代码更易于阅读/编写。*

 - [redux-act](https://github.com/pauldijou/redux-act) - 用于为 Redux 创建操作和化简器的自以为是的库。
 - [redux-crud](https://github.com/Versent/redux-crud) - Redux CRUD 应用程序的一组标准操作和减速器。


## 开发工具/检查工具

 - [redux-devtools-inspector](https://github.com/alexkuz/redux-devtools-inspector) - 另一个 Redux DevTools 监视器。
 - [redux-diff-logger](https://github.com/fcomb/redux-diff-logger) - Redux 状态之间的差异记录器。
 - [redux-devtools-chart-monitor](https://github.com/romseguy/redux-devtools-chart-monitor) - Redux DevTools 的图表监视器。
 - [redux-devtools](https://github.com/gaearon/redux-devtools) - Redux 的 DevTools 具有热重载、动作重放和可定制的 UI。
 - [redux-devtools-dispatch](https://github.com/YoruNoHikage/redux-devtools-dispatch) - 手动调度您的操作以测试您的应用程序是否反应良好。
 - [redux-devtools-dock-monitor](https://github.com/gaearon/redux-devtools-dock-monitor) - 用于 Redux DevTools 监视器的可调整大小且可移动的底座。
 - [redux-devtools-filterable-log-monitor](https://github.com/bvaughn/redux-devtools-filterable-log-monitor) - Redux DevTools 的可过滤树视图监视器。
 - [redux-devtools-log-monitor](https://github.com/gaearon/redux-devtools-log-monitor) - Redux DevTools 的默认监视器，具有树视图。
 - [remote-redux-devtools](https://github.com/zalmoxisus/remote-redux-devtools) - 远程 Redux DevTools。


## 反应集成

 - [redux-test-recorder](https://github.com/conorhastings/redux-test-recorder) - Redux 中间件通过 ui 交互自动生成减速器的测试。
 - [react-redux](https://github.com/reactjs/react-redux) - Redux 的官方 React 绑定。
 - [react-easy-universal](https://github.com/keystonejs/react-easy-universal) - 通用路由和使用 React 和 React 进行渲染Redux 太难了。现在很容易了。
 - [redux-form-material-ui](https://github.com/erikras/redux-form-material-ui) - 一组包装器组件，以方便将 Material UI 与 Redux Form 一起使用。


### 路由

 - [redux-async-connect](https://github.com/Rezonans/redux-async-connect) - 它允许您请求异步数据，将它们存储在 Redux 状态并将它们连接到您的 React 组件。
 - [redux-tiny-router](https://github.com/Agamennon/redux-tiny-router) - 专为 Redux 打造的路由器，专为通用应用程序打造。停止使用路由器作为控制器，它只是状态。
 - [redux-router](https://github.com/acdlite/redux-router) - React Router 的 Redux 绑定 –将路由器状态保存在 Redux 存储中。
 - [react-router-redux](https://github.com/reactjs/react-router-redux) - 非常简单的绑定，以保持反应路由器和 Redux 同步。
 - [ground-control](https://github.com/raisemarketplace/ground-control) - 可扩展的减速机管理和React Router 和 React Router 强大的数据获取功能终极版。


### 表格

 - [redux-form](https://github.com/erikras/redux-form) - 高阶组件使用react-redux将表单状态保存在Redux存储中。
 - [react-redux-form](https://github.com/davidkpiano/react-redux-form) - 使用 Redux 在 React 中轻松创建表单。


### 组件状态

 - [redux-react-local](https://github.com/threepointone/redux-react-local) - 通过 Redux 进行本地组件状态。
 - [redux-ui](https://github.com/tonyhb/redux-ui) - React Redux 的简单 UI 状态管理。


## 其他集成


### 通量

 - [redux-actions](https://github.com/acdlite/redux-actions) - Redux 的 Flux 标准操作实用程序。
 - [redux-promise](https://github.com/acdlite/redux-promise) - 适用于 Redux 的符合 FSA 的 Promise 中间件。


### 骨干网

 - [backbone-redux](https://github.com/redbooth/backbone-redux) - 保持主干集合和 Redux 存储同步的简单方法。


### 法尔科

 - [redux-falcor](https://github.com/ekosz/redux-falcor) - 将 Redux 前端连接到 falcor 后端。


### 接收JS

 - [redux-observable](https://github.com/redux-observable/redux-observable) - RxJS 中间件使用“Epics”来处理 Redux 中的操作副作用。
 - [rx-redux](https://github.com/jas-chen/rx-redux) - 使用 RxJS 重新实现 Redux。
 - [redux-rx](https://github.com/acdlite/redux-rx) - 用于 Redux 的 RxJS 实用程序。
 - [redurx](https://github.com/shiftyp/redurx) - 使用 RxJS 进行 Redux 风格的功能状态管理。


### 电子

 - [redux-electron-store](https://github.com/samiskin/redux-electron-store) - Redux 存储增强器允许电子进程之间自动同步。


### 出库

 - [deku-redux](https://github.com/troch/deku-redux) - deku < 中 Redux 的绑定v2。


### 其他

 - [redux-rollbar-middleware](https://github.com/netguru/redux-rollbar-middleware) - Redux 中间件将异常包装在操作中并将其以当前状态发送到 Rollbar。
 - [kasia](https://github.com/outlandishideas/kasia) - 适用于 WordPress API 的 React Redux 工具集。


## 样板文件

*样板/脚手架/入门套件/生成器/堆栈组合*

 - [redux-cli](https://github.com/SpencerCDixon/redux-cli) - 用于更快构建 Redux/React 应用程序的固定 CLI。
 - [reactuate](https://github.com/reactuate/reactuate) - React/Redux 堆栈（不是样板套件）。
 - [react-chrome-extension-boilerplate](https://github.com/jhen0409/react-chrome-extension-boilerplate) - Chrome 扩展 React.js 项目的样板。
 - [universal-redux](https://github.com/bdefore/universal-redux) - Npm 包可让您直接使用通用（同构）渲染进行 React 和 Redux 编码。仅在需要时管理 Express 设置或 Webpack 配置。
 - [generator-react-aspnet-boilerplate](https://github.com/pauldotknopf/react-aspnet-boilerplate) - 使用 ASP.NET Core 1 构建同构 React 应用程序的起点，利用现有技术。
 - [generator-redux](https://github.com/banderson/generator-redux) - Redux 的 CLI 工具：带有 devtools 的下一代功能 Flux/React。
 - [generator-react-webpack-redux](https://github.com/stylesuxx/generator-react-webpack-redux) - React Webpack 生成器包括 Redux 支持。
 - [socrates](https://github.com/matthewmueller/socrates) - 小型 (8kb)、包含电池的 Redux 存储，可减少样板文件并促进良好习惯。


## 杂项

 - [redux-core](https://github.com/jas-chen/redux-core) - 最小化 Redux。


## 学习资料

- **Redux 的概念**

[Redux官方文档](http://redux.js.org/)很好地解释了Redux的核心原理。

- **为什么是不可变的数据结构**

React官方文档的[性能指南](https://facebook.github.io/react/docs/advanced-performance.html)很好地解释了什么是不可变数据结构以及它们为何发挥重要作用。

- **副作用**

[Redux Loop 的自述文件](https://github.com/redux-loop/redux-loop) 很好地洞察了 Redux 背景下的副作用。

阅读上述材料将为您使用 Redux 编写应用程序提供良好的开端。
如果您想了解更多信息，请查看以下资源。

- **函数式编程 - 基础知识**

这篇[帖子](http://jaysoo.ca/2016/01/13/function-programming-little-ideas/)在构建 YouTube 即时搜索演示应用程序时介绍了函数式编程的基本概念。

- **反应式编程**

[反应式编程简介](https://gist.github.com/staltz/868e7e9bc2a7b8c1f754) 清晰地解释了反应式编程。

- **函数式编程 - 超越**

写得很好的[文章](https://medium.com/@chetcorcos/function-programming-for-javascript-people-1915d8775504)，讨论了用函数式语言实现的有趣的计算机科学概念以及这些概念如何应用于 JavaScript。

- **单子**

对 monad 感到好奇吗？维基百科提供了很好的[monads概述](https://en.wikipedia.org/wiki/Monad_(functioning_programming))和[本文](http://adit.io/posts/2013-04-17-functors,_applicatives,_and_monads_in_pictures.html)用图形和简单的例子更详细地解释了monads。


## 社区

- [Reddit](https://www.reddit.com/r/reduxjs/)
- [堆栈溢出](http://stackoverflow.com/questions/tagged/redux)
- [Discord](https://discord.gg/0ZcbPKXt5bZ6au5t)
- [Slack](http://slack.redux.io/)
- [Gitter](https://gitter.im/reactjs/redux)
- [freenode 上的“#rackt”](https://webchat.freenode.net/)

