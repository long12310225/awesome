## 很棒的 Cycle.js

一系列很棒的 Cycle.js 工具、资源、视频和闪亮的东西。

- [Learn](#learn)
  - [Documentation](#documentation)
  - [Tutorials](#tutorials)
  - [Videos](#videos)
  - [Slides](#slides)
  - [应用示例](#example-applications)
- [Tools](#tools)
  - [CLI](#cli)
- [Libraries](#libraries)
  - [Drivers](#drivers)
  - [Boilerplates](#boilerplates)
  - [Testing](#testing)
  - [Debugging](#debugging)
  - [Components](#components)
- [Community](#community)

---
## 学习

### 文档

* [cycle.js.org](http://cycle.js.org/) - Cycle.js 官方教程和文档。

### 教程

* [What Developers Need to Know about MVI (Model-View-Intent)](http://thenewstack.io/developers-need-know-mvi-model-view-intent/) - 关于 MVI 架构的帖子。
* [Cycle.js: a reactive framework](https://lucamezzalira.com/2016/05/23/cycle-js-a-reactive-framework/) - 通过实时数据示例介绍 Cycle.js。
* [Building realtime applications with CycleJS and RxJS](https://blog.pusher.com/building-realtime-applications-with-cyclejs-and-rxjs/) - 了解如何使用 CycleJS 和 RxJS 构建实时应用程序
* [Working with HTTP Streams with Cycle.js](http://ivanjov.com/working-with-http-streams-with-cycle-js/) - 了解如何使用 Cycle.js 处理 HTTP 请求和响应

### 视频

* [What if the user was a function?](https://www.youtube.com/watch?v=1zj7M1LnJV4) - [Andre Staltz] 在 JSConf BP2015 上的演讲(https://twitter.com/andrestaltz)
* [Unidirectional data flow architectures](https://vimeo.com/168652278) - [Andre Staltz] 在前端会议上的演讲(https://twitter.com/andrestaltz)
* [Cycle.js and functional reactive user interfaces](https://www.youtube.com/watch?v=uNZnftSksYg) - [Andre Staltz] 在 ReactiveConf 2015 上的演讲(http://twitter.com/andrestaltz)
* [Intro to Functional Reactive Programming with Cycle.js](https://www.youtube.com/watch?v=6_ETUyh0tns) - [尼克·约翰斯通](https://twitter.com/widdnz) 的演讲
* [Cycle.js Fundamentals](https://egghead.io/series/cycle-js-fundamentals) - 播放列表位于 [egghead.io](https://egghead.io)
* [Cycle.js was built to solve problems](https://www.youtube.com/watch?v=Rj8ZTRVka4E) - 作者：Andre Staltz，作者：[Frontend.fi](http://frontend.fi/)
* [Brains as Building Blocks](https://www.youtube.com/watch?v=1ToJ7cxb1R8) - 作者：Andre Staltz 在 [CycleConf 2016](http://cycleconf.com/)
* [Back to the Future, Hot reloading with Cycle.js](https://www.youtube.com/watch?v=rbrnyC5fXMM) - 作者：Nick Johnstone 在 [CycleConf 2016](http://cycleconf.com/)
* [From MVC to FRP](https://www.youtube.com/watch?v=-PCq4pXaDZw) - 作者：Gleb Bahmutov 在 [CycleConf 2016](http://cycleconf.com/)
* [Cycle.js on the bash side](https://www.youtube.com/watch?v=Rx5N99TQ52g) - 作者：Hadrien de Cuzey，作者：[CycleConf 2016](http://cycleconf.com/)
* [Reactive Programming with Cycle.js](https://vimeo.com/175121069) - 作者：Luca Mezzalira，作者：[JSDay 2016](http://2016.jsday.it/)
* [Learning how to ride: an introduction to Cycle.js](https://youtu.be/31URmaeNHSs) - 作者：Fernando Macias Pereznieto，来自 [JS 伦敦月刊](http://www.meetup.com/js-monthly-london/)
* [User Interfaces as Pure Functions of Time](https://www.youtube.com/watch?v=9BG0Y3C6WqM) - [Thomas Belin](http://twitter.com/atomrc) 在 [dotjs 2016](http://dotjs.io/) 的闪电演讲

### 幻灯片

* [Cycle.js an honestly reactive framework for web user interfaces](http://slides.com/erykpiast/cycle) - 作者：埃里克·纳皮拉拉
* [Intro to Cycle.js](http://www.slideshare.net/aryelukashevski/cyclejs-introduction) - 作者：阿耶·卢卡舍夫斯基
* [Reactive Programming with Cycle.js](http://www.slideshare.net/flashplatform/reactive-programming-with-cyclejs) - 通过卢卡·梅扎里拉
* [Cycle.js - building apps with streams only](http://lmatteis.github.io/cyclejs-slides/keynote/index.html) - 卢卡·马蒂斯
* [Functional Reactive Programming with Cycle.js](https://slides.com/artfuldev/frp-with-cycle-js) - 作者：苏达桑·巴拉吉
* [Beyond flux: going full cycle with FRP](https://clementd-files.cellar.services.clever-cloud.com/blog/frp-full-cycle-ncrafts.html) - 作者：[克莱门特·德拉法格](http://clementd.cleverapps.io/)

### 应用示例

* [**cyclejs/cycle-examples**](https://github.com/cyclejs/cyclejs/tree/master/examples) - Cycle.js 小例子官方合集
* [Widdershin/tricycle ★23](https://github.com/Widdershin/tricycle) - 用于尝试 Cycle.js 的 Scratchpad 依赖于带有 Cycle 的 Ace Editor
* [cgeorg/todomvp ★21](https://github.com/cgeorg/todomvp) - Minimum Viable Pizza，用 Cycle.js 编写的示例 Web 应用程序
* [erykpiast/cyclejs-examples ★9](https://github.com/erykpiast/cyclejs-examples) - 使用 Cycle.js 构建的示例 Web 应用程序。
* [grozen/trends-cycle ★3](https://github.com/grozen/trends-cycle) - 用 Cycle.js 编写的 Slack 趋势搜索
* [ivan-kleshnin/cyclejs-examples ★120](https://github.com/ivan-kleshnin/cyclejs-examples) - CycleJS 示例集合，ES6。
* [ivan-kleshnin/tetris-cyclejs ★12](https://github.com/ivan-kleshnin/tetris-game) - 用 CycleJS、ES6 实现的俄罗斯方块游戏
* [phadej/graafi ★20](https://github.com/phadej/graafi) - Cycle.js 使用 SVG 和全局撤消/重做进行实验
http://oleg.fi/graafi/
* [**staltz/matrixmultiplication.xyz ★548**](https://github.com/staltz/matrixmultiplication.xyz) - 交互式矩阵乘法 [webapp](http://matrixmultiplication.xyz/)
* [**staltz/rxmarbles ★2,577**](https://github.com/staltz/rxmarbles) - Rx Observables 的交互图 http://rxmarbles.com/
* [MarcCloud/magic-cart ★6](https://github.com/MarcCloud/magic-cart) - 魔法生物商店的简单购物车。
* [foxdonut/cycle-todolist ★11](https://github.com/foxdonut/cycle-todolist) - 演示了一个带有 CRUD 的简单 Cycle.js TODO 列表应用程序。
* [**Mercateo/component-check ★468**](https://github.com/Mercateo/component-check) - 构建 Cycle.js 组件的常见模式
* [edge/electron-cycle-media ★27](https://github.com/edge/electron-cycle-media) - 用 Cycle.js 和 Electron 编写的媒体播放器。
* [kibin/cycle-example-who-to-follow ★16](https://github.com/kibin/cycle-example-who-to-follow) - 小示例使用 github api 部分实现了 Twitter 的“谁关注”框。
* [SkaterDad/cycle-snabbdom-examples ★12](https://github.com/SkaterDad/cycle-snabbdom-examples) - 嵌套组件的示例，使用 snabbdom 特定的动画。
* [bahmutov/draw-cycle ★112](https://github.com/bahmutov/draw-cycle) - 计数器应用程序的交互式可视化显示 MVI 组件内的数据流 [glebbahmutov.com/draw-cycle](https://glebbahmutov.com/draw-cycle/)
* [andreloureiro/pomocycle ★21](https://github.com/andreloureiro/pomocycle) - 一个简单的番茄钟计时器。
* [laszlokorte/tams-tools ★24](https://github.com/laszlokorte/tams-tools) - 一套使用 Cycle.js 构建的用于教授和学习计算机科学的工具。
* [lucamezzalira/jsday-cycle-js ★16](https://github.com/lucamezzalira/jsday-cycle-js) - 使用 Cycle.js 构建的反应式实时伦敦地铁列车状态示例。
* [cyclejs-community/built-with-cycle ★9](https://github.com/cyclejs-community/built-with-cycle) - [一个网站](http://cyclejs-community.github.io/built-with-cycle) 展示使用 Cycle.js 构建的酷项目
* [class-ideas/cyclejs-hangman ★10](https://github.com/class-ideas/cyclejs-hangman) - 使用 Cycle.js 构建的刽子手游戏
* [wmaurer/cyclejs-fractals ★15](https://github.com/wmaurer/cyclejs-fractals) - 跳舞毕达哥拉斯树分形 - 对 2048 个 SVG 节点进行动画处理。
* [fabiothiroki/cyclejs-starwars ★2](https://github.com/fabiothiroki/cyclejs-starwars) - 使用 Cycle.js、RxJS 和虚拟 DOM 测试的星球大战角色搜索应用程序。
* [staltz/mmmmm-mobile ★124](https://github.com/staltz/mmmmm-mobile/) - 一个 React Native + Cycle.js 应用程序，用于在安全 Scuttlebutt 网络上实现社交网络
* [cyclejs/todomvc-cycle ★214](https://github.com/cyclejs/todomvc-cycle/) - TodoMVC [示例](https://cyclejs.github.io/todomvc-cycle/) 在 Cycle.js 中实现
* [jefersondaniel/cyclejs-notes](https://github.com/jefersondaniel/cyclejs-notes/) - 使用 Cycle.js 和 Orbit.js 的 Notes 应用程序 https://jefersondaniel.com/cyclejs-notes
* [staltz/dat-installer ★77](https://github.com/staltz/dat-installer) - 通过 Dat 下载、安装和更新 Android 应用
* [usm4n/cycle-hn ★25](https://github.com/usm4n/cycle-hn) - Hackernews 使用 CycleJS 克隆
* [lizraeli/cycle-github-emojis](https://github.com/lizraeli/cycle-github-emojis) - 使用 Cycle.JS 制作的 github 表情符号查看器 [webapp](https://github-emoji.levizraelit.com/)
* [perjerz3434/meetup.com ★1](https://github.com/perjerz3434/meetup.com) - Meetup.com 使用 CycleJS 在世界各地实现 RSVP 可视化

## 工具

### 命令行界面

* [cyclejs-community/create-cycle-app ★160](https://github.com/cyclejs-community/create-cycle-app) - 创建无需构建配置的 Cycle.js 应用程序。

## 图书馆

### 司机

* [@cycle/http](https://github.com/cyclejs/cyclejs/tree/master/http) - 用于发出 HTTP 请求的 Cycle.js 驱动程序，基于 superagent。
* [**@cycle/dom**](https://github.com/cyclejs/cyclejs/tree/master/dom) - 用于启用与 DOM 交互的 Cycle.js 驱动程序。该驱动程序基于 snabbdom 作为虚拟 DOM 库。
* [@cycle/storage](https://github.com/cyclejs/storage) - 用于使用 localStorage 和 sessionStorage 的 Cycle.js 驱动程序。
* [@cycle/history](https://github.com/cyclejs/cyclejs/tree/master/history) - 这是用于处理 [History API](https://developer.mozilla.org/en-US/docs/Web/API/History_API) 的标准 Cycle.js 驱动程序
* [@cycle/isolate](https://github.com/cyclejs/cyclejs/tree/master/isolate) - 用于在 Cycle.js 中创建作用域数据流组件的实用程序函数。
* [@cycle/time](https://github.com/cyclejs/cyclejs/tree/master/time) - Cycle.js 快速、美观的测试和时间管理
* [cyclejs/cycle-notification-driver ★20](https://github.com/cyclejs/cycle-notification-driver) - 用于显示和响应 HTML5 通知的 Cycle.js 驱动程序。
* [axefrog/cycle-router5 ★30](https://github.com/axefrog/cycle-router5) - 使用 Router5 的路由器驱动程序
* [cgeorg/cycle-socket.io ★27](https://github.com/cgeorg/cycle-socket.io) - Socket.IO 客户端的 Cycle 驱动程序
* [secobarbital/cycle-fetch-driver ★2](https://github.com/secobarbital/cycle-fetch-driver) - Cycle.js 驱动程序，用于使用 Fetch API 发出 HTTP 请求。
* [r7kamura/cycle-fetcher-driver ★14](https://github.com/r7kamura/cycle-fetcher-driver) - Cycle.js 驱动程序，用于使用 [stackable-fetcher](https://github.com/r7kamura/stackable-fetcher) 发出 HTTP 请求。
* [benji6/cycle-audio-graph ★12](https://github.com/benji6/cycle-audio-graph) - 用于使用 [virtual-audio-graph](https://github.com/benji6/virtual-audio-graph) 操作 Web 音频 API 的 Cycle.js 驱动程序
* [CyclicMaterials/cycle-hammer-driver ★11](https://github.com/CyclicMaterials/cycle-hammer-driver) - 用于包装 Hammer.js 并检测触摸手势的 Cycle.js 驱动程序
* [jessaustin/cycle-sse-driver ★6](https://github.com/jessaustin/cycle-sse-driver) - 服务器发送事件/EventSource 的源驱动程序。
* [tylors/cycle-snabbdom ★41](https://github.com/TylorS/cycle-snabbdom) - 使用 Snabbdom 的 DOM 驱动程序
* [cyclejs-community/cyclic-router ★90](https://github.com/cyclejs-community/cyclic-router) - 为 Cycle.js 构建的路由器驱动程序
* [Widdershin/cycle-animation-driver ★33](https://github.com/Widdershin/cycle-animation-driver) - requestAnimationFrame 的循环驱动程序
* [dralletje/cycle-firebase ★21](https://github.com/dralletje/cycle-firebase) - 适用于 Firebase 的 Cycle.js 驱动程序
* [edge/cycle-blessed ★46](https://github.com/edge/cycle-blessed) - 用于终端应用程序的 Cycle.js 驱动程序
* [10clouds/cyclejs-cookie ★2](https://github.com/10clouds/cyclejs-cookie) - Cycle.js 的 Cookie 驱动程序
* [whitecolor/cycle-async-driver ★25](https://github.com/whitecolor/cycle-async-driver) - 用于创建异步请求/响应 Cycle.js 驱动程序的工厂
* [raquelxmoss/cycle-keys ★35](https://github.com/raquelxmoss/cycle-keys) - 键盘事件驱动程序
* [rektide/recyclec ★0](https://github.com/rektide/recyclec) - 读取线驱动程序
* [goodmind/cycle-telegram ★15](https://github.com/goodmind/cycle-telegram) - Telegram Bot API 的 Cycle.js 驱动程序
* [apoco/cycle-electron-driver ★22](https://github.com/apoco/cycle-electron-driver) - 驱动程序与 Cycle.js 应用程序中的 Electron 接口进行交互
* [rkrupinski/cyclejs-animated-localstorage ★12](https://github.com/rkrupinski/cyclejs-animated-localstorage) - 用于动画 (srsly) localStorage 的 Cycle.js 驱动程序。
* [cyclejs-community/cycle-keyboard ★9](https://github.com/cyclejs-community/cycle-keyboard) - Cycle.js 的键盘驱动程序
* [garrydzeng/cycle-page ★3](https://github.com/garrydzeng/cycle-page) - Cycle.js 的小型客户端路由器
* [jbowden1982/cycle-socketcluster ★5](https://github.com/jbowden1982/cycle-socketcluster) - Cycle.js 的套接字集群驱动程序
* [cyclejs-community/redux-cycles ★599](https://github.com/cyclejs-community/redux-cycles) - 一个 Redux 中间件，允许您使用 Cycle.js 处理操作生命周期
* [JuniperChicago/cycle-gun ★18](https://github.com/JuniperChicago/cycle-gun) - 包装 Gun.js 实例的基本 Cycle.js 驱动程序，允许图形存储和 p2p 同步
* [EnigmaCurry/cycle-deepstream ★8](https://github.com/EnigmaCurry/cycle-deepstream) - [deepstream.io](https://deepstream.io) 的 Cycle.js 驱动程序
* [Alex0007/cycle-express-driver ★1](https://github.com/Alex0007/cycle-express-driver) - Express.js 服务器的 Cycle.js 驱动程序
* [mrpierrot/cycle-node-http-server ★4](https://github.com/mrpierrot/cycle-node-http-server) - Node.js HTTP(S) 服务器的 Cycle.js 驱动程序
* [mrpierrot/cycle-net ★0](https://github.com/mrpierrot/cycle-net) - Node.js HTTP(S)/WS(S)/Socket.io 服务器的 Cycle.js 驱动程序
* [Avalander/cycle-idb ★4](https://github.com/Avalander/cycle-idb) - 包装 IndexedDB 的 Cycle.js 驱动程序
* [unhappychoice/cycle-pusher ★1](https://github.com/unhappychoice/cycle-pusher) - [Pusher](https://pusher.com/) 的 Cycle.js 驱动程序
* [helmoski/cycle-selection-driver](https://github.com/helmoski/cycle-selection-driver) - 用于与 [Selection API] 交互的 Cycle.js 驱动程序(https://developer.mozilla.org/en-US/docs/Web/API/Selection)
* [mjyc/cycle-posenet-driver ★1](https://github.com/mjyc/cycle-robot-drivers/tree/master/3rdparty/cycle-posenet-driver) - 使用 [TensorFlow.js](https://js.tensorflow.org/) 驱动的 [PoseNet](https://github.com/tensorflow/tfjs-models/tree/master/posenet) 进行姿势检测的 Cycle.js 驱动程序
* [@cycle-robot-drivers/speech ★1](https://github.com/mjyc/cycle-robot-drivers/tree/master/speech) - 使用 [Web Speech API] 进行语音合成和识别的 Cycle.js 驱动程序(https://developer.mozilla.org/en-US/docs/Web/API/Web_Speech_API)
* [@cycle-robot-drivers/sound ★1](https://github.com/mjyc/cycle-robot-drivers/tree/master/sound) - 使用 [HTMLAudioElement](https://developer.mozilla.org/en-US/docs/Web/API/HTMLAudioElement) 播放声音的 Cycle.js 驱动程序

### 公用事业

* [staltz/chai-virtual-dom ★24](https://github.com/staltz/chai-virtual-dom) - 用于测试 virtual-dom VTree 的 Chai 断言助手
* [cgeorg/sinject ★10](https://github.com/cgeorg/sinject) - 一个支持 Cycle 循环依赖的依赖注入工具
* [erykpiast/cyclejs-group ★20](https://github.com/erykpiast/cyclejs-group) - CycleJS 框架的实用程序，用于在创建流组时减少样板文件。
* [erykpiast/cyclejs-wc ★2](https://github.com/erykpiast/cyclejs-wc) - 用于创建基于 Cycle.js 的 Web 组件的实用程序
* [**ohanhi/hyperscript-helpers ★390**](https://github.com/ohanhi/hyperscript-helpers) - elm-html 启发了编写超脚本或虚拟超脚本的助手。
* [**pH200/cycle-react ★342**](https://github.com/pH200/cycle-react) - 使用 React 而不是 virtual-dom 以及类似 Cycle 的 API
* [madcapjake/earlhyperscript ★2](https://github.com/MadcapJake/earl-hyperscript) - 用于将 Earl Grey 的[文档构建语法](https://breuleux.github.io/earl-grey/doc.html#documentbuildingsyntax) 与 Cycle.js 结合使用的辅助函数和宏。
* [WorldMaker/cycle-gear ★4](https://github.com/WorldMaker/cycle-gear) - 基于 Cycle 的 MVI 模式形式化的 Cycle 的主函数工厂
* [SuperManitu/cyclejs-sortable ★15](https://github.com/cyclejs-community/cyclejs-sortable) - 只需一行代码即可通过拖放对所有内容进行排序！
* [atomrc/cyclejs-auth0 ★22](https://github.com/atomrc/cyclejs-auth0) - 在 Cyclejs 应用程序上开始使用 Auth0 所需的一切（驱动程序 + 组件）
* [**staltz/cycle-onionify ★244**](https://github.com/staltz/cycle-onionify) - Cycle.js 应用程序的分形状态管理
* [maiermic/cycle-storageify ★5](https://github.com/maiermic/cycle-storageify) - 通过将其洋葱形状态存储在本地存储中来增强 Cycle.js 组件（主函数）
* [shfrmn/cycle-lot](https://github.com/shfrmn/cycle-lot) - 轻松处理 Cycle.js 组件的动态列表（完整的打字支持）
* [sarimarton/powercycle](https://powercycle.js.org) - 基于 Cycle.js 的静态 VDOM 组合和类似 React 的开发

### 样板文件

* [andreloureiro/cyclejs-starter ★50](https://github.com/andreloureiro/cyclejs-starter) - 使用 ES6 和 Livereload 的 Cycle.js 入门模板。
* [Frikki/generator-cyclejs ★2](https://github.com/Frikki/generator-cyclejs) - 使用 Yeoman 构建 Cycle.js 嵌套对话模块。
* [**edge/cyc ★194**](https://github.com/edge/cyc) - 在几秒钟内搭建一个同构的 Cycle.js 应用程序。
* [cmdv/cycle-webpack-boilerplate ★101](https://github.com/Cmdv/cycle-webpack-boilerplate) - 具有路由、状态处理和测试的循环应用程序。
* [Widdershin/cycle-hot-reloading-example ★27](https://github.com/Widdershin/cycle-hot-reloading-example) - 使用 browserify-hmr 进行热重载的 Cycle.js 入门项目
* [mciparelli/cycle-hmr-example ★0](https://github.com/mciparelli/cycle-hmr-example) - 使用 browserify 和 Cycle-hmr 的 Cycle.js 入门项目
* [cycle-community/typescript-starter-cycle ★22](https://github.com/cyclejs-community/typescript-starter-cycle) - 一个使用 Webpack 在 Cycle.js 中开始使用 TypeScript 的简单项目。将 Visual Studio Code 设置为糖果。
* [wyqydsyq/unicycle ★6](https://github.com/wyqydsyq/unicycle) - 通过 Webpack 使用 HMR 和 ServiceWorkers 在 Koa.js 服务器上运行的样板通用 Cycle 应用程序
* [syarul/cycle-iso ★4](https://github.com/syarul/cycle-iso) - 一个准系统样板 Cycle 应用程序，其数据流基于 Promise 并使用 Falcor.js 获取
* [snowpack-cycle](https://github.com/rajasegar/snowpack-cycle) - Snowpack 应用程序模板，用于使用 create-snowpack-app 创建 Cycle.js 项目

### 测试

* [erykpiast/cyclejs-mock ★22](https://github.com/erykpiast/cyclejs-mock) - 用于测试基于 CycleJS 框架的应用程序的实用程序。
* [jeysal/pretty-format-snabbdom ★0](https://github.com/jeysal/pretty-format-snabbdom) - 一个 [pretty-format](https://github.com/facebook/jest/tree/master/packages/pretty-format) ([Jest](https://facebook.github.io/jest/) snapshot) 插件，用于渲染 snabbdom VNode 的快照和 React 元素的快照一样好

### 调试

* [**cyclejs/cycle-time-travel ★213**](https://github.com/cyclejs/cycle-time-travel) - Cycle.js 应用程序的时间旅行调试器。显示一个流可视化工具，您可以拖动它来及时返回。

### 组件

* [erykpiast/autocompleted-select ★10](https://github.com/erykpiast/autocompleted-select) - 选择具有自动完成功能的 Web 组件。基于 RxJS 和 VirtualDOM。
* [enten/cyclejs-calendar ★11](https://github.com/enten/cyclejs-calendar) - Cycle.js 的日历组件。在线尝试[此处](http://enten.github.io/cyclejs-calendar/example)。
* [mciparelli/cyclejs-gravatar ★0](https://github.com/mciparelli/cyclejs-gravatar) - Cycle.js 组件用于渲染头像个人资料图像。
* [tommy-the-runner/cyclejs-ace-editor ★0](https://github.com/tommy-the-runner/cyclejs-ace-editor) - 使用 [brace](https://github.com/thlorenz/brace) 将 Cycle.js 与 Ace Editor 集成。查看示例[此处](https://tommy-the-runner.github.io/cyclejs-ace-editor/)。
* [raquelxmoss/cycle-color-picker ★44](https://github.com/raquelxmoss/cycle-color-picker) - Cycle.js 的颜色选择器组件。 [查看示例](https://raquelxmoss.github.io/cycle-color-picker)。
* [cyclejs-community/cycle-svg-pan-and-zoom ★4](https://github.com/cyclejs-community/cycle-svg-pan-and-zoom) - Cycle.js 的 Google 地图风格 SVG 平移和缩放组件

## 社区

* [Gitter chat](https://gitter.im/cyclejs/cycle-core) - 问“我该如何……？”


## 执照

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png)](http://creativecommons.org/publicdomain/zero/1.0/)
