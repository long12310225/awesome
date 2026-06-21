# 太棒了 <divalign="right">:steam_locomotive::train::train::train::train::train:</div> [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

> [choo](https://choo.io/) 是一个 `4kb` 框架，用于创建
> 强大的前端应用程序

## 内容

- [官方资源](#official-resources)
- [Dependencies](#dependencies)
- [Demos](#demos)
- [Community](#community)
- [插件和附加组件](#plugins-and-addons)
- [Elements](#elements)
- [CLI 模板](#cli-templates)
- [Resources](#resources)
- [使用 choo 的项目](#projects-using-choo)

### 官方资源

- [Docs](https://github.com/yoshuawuyts/choo/blob/master/README.md)
- [Handbook](https://github.com/yoshuawuyts/choo-handbook)
- [Repo](https://github.com/yoshuawuyts/choo)
- [Website](https://choo.io/)
- [推特话题](https://twitter.com/yoshuawuyts/status/730087077803528193)

### 依赖关系
`choo` 是一个模块化框架。这些是它粘合在一起的依赖项
在引擎盖下：

- [bel](https://github.com/shama/bel) - 使用以下命令创建可组合 DOM 元素
模板字符串。
- [hyperx](https://github.com/substack/hyperx) - 将模板字符串转换为
库后端。
- [nanomorph](https://github.com/choojs/nanomorph) - 真实 DOM 节点的超快速比较算法。
- [nanoraf](https://github.com/yoshuawuyts/nanoraf) - 仅在需要时致电英国皇家空军。
- [nanorouter](https://github.com/choojs/nanorouter) - Smol 前端路由器。
- [nanobus](https://github.com/choojs/nanobus) - 小型消息总线。
- [nanolocation](https://github.com/choojs/nanolocation) - 小 window.location 库。
- [nanohref](https://github.com/choojs/nanohref) - Tiny href 单击处理程序库。
- [nanoquery](https://github.com/choojs/nanoquery) - 小型查询字符串模块。
- [nanotiming](https://github.com/choojs/nanotiming) - 小型时序库。

### 演示

- [Input example](http://requirebin.com/?gist=e589473373b3100a6ace29f7bbee3186) - ([repo](https://github.com/yoshuawuyts/choo/tree/master/examples/title))
- [HTTP 效果](https://hyperdev.com/#!/project/fork-fang)
- [邮箱路由](https://github.com/yoshuawuyts/choo/tree/master/examples/mailbox)
- [TodoMVC](http://shuheikagawa.com/todomvc-choo) - ([repo](https://github.com/shuhei/todomvc-choo))
- [choo-firebase](https://choo-firebase-2ec21.firebaseapp.com) - ([repo](https://github.com/mw222rs/choo-firebase))
- [Grow](https://grow.static.land) - ([repo](https://github.com/sethvincent/grow))
- [Chatbot](http://chootbot.herokuapp.com) - ([repo](https://github.com/plaey/chatbot))
- [chat-random](https://github.com/akiva/chat-random)
- [choo-leaflet-demo](https://github.com/timwis/choo-leaflet-demo)
- [choo-scriber](https://zhouhansen.github.io/choo-scriber) - ([repo](https://github.com/ZhouHansen/choo-scriber))

### 社区

- [Freenode](https://webchat.freenode.net/?channels=choo)

### 插件和附加组件

- [choo-location-electron](https://github.com/bcomnes/choo-location-electron) - 修复 Electron 中 `choo` 的路由器。
- [choo-log](https://github.com/yoshuawuyts/choo-log) - choo 的开发记录器。
- [choo-test](https://github.com/mantoni/choo-test) - 简单的 choo 应用单元测试。
- [choo-persist](https://github.com/yoshuawuyts/choo-persist/) - 将 choo 状态与 LocalStorage 同步。
- [choo-promise](https://github.com/rahatarmanahmed/choo-promise) - 在效果和订阅中使用承诺。
- [choo-pull](https://github.com/yoshuawuyts/choo-pull) - 包装处理程序以在 choo 插件中使用拉流。
- [choo-redirect](https://github.com/yoshuawuyts/choo-redirect) - 将一个视图重定向到另一个视图。
- [choo-model](https://github.com/yoshuawuyts/choo-model) - choo 的实验性状态管理库。
- [choo-resume](https://github.com/bengourley/choo-resume) - choo-resume + hot-rld = choo 中的热门应用程序重新加载。
- [choo-detached](https://github.com/graforlock/choo-detached) - 使用 `choo` 作为可安装的、简单的独立组件（无路由）。
- [choo-service-worker](https://github.com/choojs/choo-service-worker) - `choo` 的 Service Worker 加载器。
- [choo-websocket](https://github.com/YerkoPalma/choo-websocket) - WebSocket 浏览器 API 的小包装，用于“choo”应用程序。
- [choo-store](https://github.com/ungoldman/choo-store) - choo 应用程序的轻量级状态结构。

### 元素

- [dom-notifications](https://github.com/finnp/dom-notifications) - 受 Atom 启发的通知组件。
- [choodown](https://github.com/trainyard/choodown) - 一个简单的 choo 降价组件。
- [choo-md-editor](https://github.com/dbtek/choo-md-editor) - 轻量级 Markdown 编辑器，可在 Choo 应用程序内使用或作为独立库使用。
- [choo-chartist](https://github.com/rexmortus/choo-chartist) - 用于将 [Chartist](https://gionkunz.github.io/chartist-js/) 与 choo 框架一起使用的小组件。

### CLI 模板

[choo-cli] 的模板(https://github.com/trainyard/choo-cli)

- [trainyard/template-basic](https://github.com/trainyard/template-basic)
- [haroenv/template-webpack](https://github.com/haroenv/template-webpack)
- [simonwjackson/atomic-choo](https://github.com/simonwjackson/atomic-choo) - 一个固执己见的项目种子，可以开始使用 electro、webpack 和 choo 进行开发。

其他 CLI 模板
- [graforlock/choo-bandwagon](https://github.com/graforlock/choo-bandwagon)

### 资源
> :movie_camera: : 视频
> :计算机: : 教程
> :书: :文章

- :computer: [你的第一个 choo 应用](https://yoshuawuyts.gitbooks.io/choo/content/02_your_first_app.html)
- :movie_camera: [TCBY 社区直播环聊](https://www.youtube.com/watch?v=a97Mw2z1SAI)
- :book: [更好的前端体验](https://medium.com/@yoshuawuyts/a-better-frontend-experience-7b0498c85658)
- :book: [CycleJS、choo、React 和 Angular2 中的组合](http://blog.krawaller.se/posts/composition-in-cyclejs-choo-react-and-angular2)
- :book: [choo 中愚蠢的智能组件](http://blog.krawaller.se/posts/stupidly-smart-components-in-choo)

### 使用 choo 的项目

- [boxcar](https://github.com/toddself/boxcar) - 基于 choo 的网格/电子表格编辑器。
- [choo-sortable](https://github.com/willkessler/choo-sortable) - 使用 choo 构建可排序的代码。
- [hacker-choo](https://github.com/mw222rs/hacker-choo) - 用 choo 编写的 Hacker Typer 克隆。
- [footprint-rechoo](https://github.com/npeihl/footprint-rechoo) - [footprint-review](http://github.com/sjcgis/footprint-review) 的 choo 重写。
- [minidocs](https://github.com/freeman-lab/minidocs) - 使用 choo 构建的文档站点生成器。
- [dataface](https://github.com/timwis/dataface) - 用于管理数据库的桌面应用程序。
- [BlankUp](https://github.com/HoverBaum/BlankUp-Electron) - 多平台 Markdown 编辑器。
- [hackernews-choo](https://github.com/kvnneff/hackernews-choo) - 使用 choo 构建的黑客新闻阅读器。
- [tic-tac-choo](https://github.com/YerkoPalma/tic-tac-toe) - 渐进式井字游戏，由 choo 制作。
- [enviar](https://github.com/timwis/enviar) - SMS/文本消息的聊天界面。
- [kaktus](https://github.com/kaktus/kaktus) - 一个新的简约 Web 浏览器，基于“choo”和 IndexedDB 构建。
- [civicdr.org](https://github.com/CiviCDR/civicdr.org) - [CiviCDR](https://civicdr.org/) 网站。
- [nekocafe](https://github.com/notenoughneon/nekocafe) - 网络聊天室 :cat: :speech_balloon:。
- [Robotopia](https://github.com/robotopia-x/robotopia) - 向孩子们介绍如何使用微型虚拟机器人进行编码！
- [busca](https://github.com/afk-mcz/busca) - 一个小型网络扩展，用于搜索 reddit 上的当前选项卡。
- [choo-ban](https://github.com/luizbaldi/choo-ban) - 用于管理董事会任务的简单看板，使用“choo”构建。
- [boowa](https://github.com/boowajs/boowa) - 一个有趣的博客生成器，用“choo”构建。
- [hyperamp](https://github.com/hypermodules/hyperamp) - 谦虚的音乐播放器。

### 许可证

[![CC0](http://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

在法律允许的范围内，[Yerko Palma](https://github.com/YerkoPalma) 已放弃本作品的所有版权以及相关或邻接权。
