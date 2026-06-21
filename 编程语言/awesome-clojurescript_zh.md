
<img src="https://avatars2.githubusercontent.com/u/12118456?v=3&s=75"
对齐=“右”/>

# 很棒的 ClojureScript

##### 社区驱动的 ClojureScript 书籍、框架、库和包装器列表。

* * *

  - [Resources](#resources)
      - [Books](#books)
  - [很棒的 ClojureScript](#awesome-clojurescript-1)
      - [Canvas](#canvas)
      - [客户端/服务器通信](#clientserver-communication)
      - [代码分析](#code-analysis)
      - [数据序列化](#data-serialization)
      - [数据可视化](#data-visualization)
      - [Database](#database)
      - [Development](#development)
      - [文档对象模型](#document-object-model)
      - [Documentation](#documentation)
      - [Graphics](#graphics)
      - [HTTP处理程序](#http-handler)
      - [Internationalization](#internationalization)
      - [JavaScript 互操作性](#javascript-interoperability)
      - [Miscellaneous](#miscellaneous)
      - [React.js 接口](#reactjs-interface)
      - [反应式编程](#reactive-programming)
      - [Routing](#routing)
      - [状态管理](#state-management)
      - [Testing](#testing)
      - [Validation](#validation)
      - [网页框架和模板](#web-framework--template)
      - [WebSockets](#websockets)
  - [Contributing](#contributing)
  - [License](#license)


* * *


## 资源


### 书籍
- [ClojureScript Unraveled](https://leanpub.com/clojurescript-unraveled) - 一本关于 ClojureScript 语言的开源书籍，涵盖了所有语言功能、如何使用编译器以及构建应用程序和库的工具。
- [ClojureScript Unraveled (2nd edition)](https://funcool.github.io/clojurescript-unraveled/) - 一本关于 ClojureScript 语言的开源书籍，涵盖了所有语言功能、如何使用编译器以及构建应用程序和库的工具。
- [ClojureScript: Up and Running](https://shop.oreilly.com/product/0636920025139.do) - 由 Clojure Stuart Sierra 和 Luke VanderHart 等大佬编写的 ClojureScript 简介。
- [Clojure, The Essential Reference](https://www.manning.com/books/clojure-the-essential-reference) - 关于 Clojure 语言和标准库的参考书。
- [Etudes for ClojureScript](https://shop.oreilly.com/product/0636920043584.do) - 一本实用手册，包含 30 个介绍 ClojureScript 的配套练习或练习曲。
- [Learning ClojureScript](https://www.packtpub.com/web-development/learning-clojurescript) - 掌握使用 ClojureScript 进行敏捷单页 Web 应用程序开发的艺术。
- [Transforming Data with ClojureScript](https://langintro.com/cljsbook) - ClojureScript 初学者指南，包含交互式示例和练习，“重点关注编程的主要任务——转换数据”。



### 课程
- [ClojureScript Koans](http://clojurescriptkoans.com/) - 这是通过交互式挑战开始在网络上学习 Clojure 和 ClojureScript 的好方法。
- [Lambda Island](https://lambdaisland.com/) - 全栈 Web 开发课程，包括使用 ClojureScript 的前端、使用 Clojure 的后端、语言基础知识、安全性、互联网标准和系统管理。
- [Learn Reagent](https://www.learnreagent.com/) - 为开发人员介绍 ClojureScript with Reagent。提供 1 小时免费内容。 [learn re-frame](https://www.learnreframe.com/) 是它的后续。
- [Learning ClojureScript](https://purelyfunctional.tv/) - O'Really Online Learning 提供的长达 2 小时 11 分钟的 Clojurescript 简介。也可在 [Udemy](https://www.udemy.com/course/learning-clojurescript/) 上找到。


### 视频
- [ClojureScript for Skeptics](https://www.youtube.com/watch?v=gsffg5xxFQI) - Derek Slager 在 Clojure Conj 2015 的演讲中讨论了为什么 ClojureScript 实际上是一种非常实用的 Web 开发语言。
- [Interactive programming Flappy Bird in ClojureScript](https://www.youtube.com/watch?v=KZjFVdU8VLI) - 2014 年的 5 分钟视频，展示了 ClojureScript 开发人员体验的强大功能。


## 很棒的 ClojureScript


### 帆布
- [Monet](https://github.com/rm-hull/monet) - 一个小型 ClojureScript 库，可以更轻松地使用画布和视觉效果。
- [Quamolit](https://github.com/Quamolit/quamolit) - 一个小型的声明性动画库，受到 React 的启发。


### 客户端/服务器通信
- [cljs-ajax](https://github.com/JulianBirch/cljs-ajax) - 用于 ClojureScript 和 Clojure 的简单 Ajax 客户端。
- [Fetch](https://github.com/LightTable/fetch) - 一个 ClojureScript 库，使客户端/服务器交互变得轻松。


### 代码分析
- [kibit](https://github.com/jonase/kibit) - 静态代码分析器用于查找可以使用更惯用的函数或宏重写的代码模式。


### 数据序列化
- [Cljson](https://github.com/tailrecursion/cljson) - 用于加速浏览器数据反序列化的 Clojure/ClojureScript 库。
- [Transit](https://github.com/cognitect/transit-cljs) - 一种数据交换格式和一组库，用于在用不同编程语言编写的应用程序之间传递值。


### 数据可视化
- [C2](https://keminglabs.com/c2) - 它允许您基于数据以声明方式创建 HTML 和 SVG 标记。


### 数据库
- [Datascript](https://github.com/tonsky/datascript) - ClojureScript 中的不可变内存数据库和 Datalog 查询引擎。
- [Jaki](https://github.com/pandeiro/jaki) - 一个简单的 ClojureScript CouchDB 客户端。
- [Konserve](https://github.com/replikativ/konserve) - 带有 core.async 的 clojuresque 键值/文档存储协议。
- [specql](https://github.com/tatut/specql) - 使用命名空间键进行简单 PostgreSQL 查询的库。


### 发展
- [Ambly](https://github.com/omcljs/ambly) - iOS JavaScriptCore 中的 ClojureScript REPL。
- [cljs-devtools](https://github.com/binaryage/cljs-devtools) - 在 Chrome Devtools 中更好地呈现 ClojureScript 值。
- [Devcards](https://github.com/bhauman/devcards) - Devcards 旨在为 ClojureScript 提供可视化 REPL 体验。
- [Instaparse](https://github.com/lbradstreet/instaparse-cljs) - 它的目标是成为在 ClojureScript 中构建解析器的最简单方法。
- [lein-cljsbuild](https://github.com/emezeske/lein-cljsbuild) - 一个 Leiningen 插件，使 ClojureScript 开发变得容易。
- [lein-figwheel](https://github.com/bhauman/lein-figwheel) - Leiningen 插件，将 ClojureScript 代码更改推送到客户端。
- [Lumo](https://github.com/anmonteiro/lumo) - 快速、跨平台、独立的 ClojureScript 环境。
- [Planck](https://github.com/mfikes/planck) - 基于 JavaScriptCore 的适用于 macOS 和 Linux 的独立 ClojureScript REPL。
- [Ribol](http://docs.caudate.me/ribol/) - clojure/clojurescript 有条件重新启动。
- [shadow-cljs](https://github.com/thheller/shadow-cljs) - ClojureScript 编译变得简单
- [Truss](https://github.com/ptaoussanis/truss) - Clojure/ClojureScript 的固执己见的断言 API。


### 文档对象模型
- [cljs-binding](https://github.com/fluentsoftware/cljs-binding) - 它将 html 元素绑定到 ClojureScript 函数。
- [Crate](https://github.com/ibdknox/crate) - Hiccup 的 ClojureScript 实现。
- [Dominator](https://github.com/dubiousdavid/dominator) - ClojureScript 中的 Virtual-Dom。
- [Dommy](https://github.com/plumatic/dommy) - 一个严肃的 ClojureScript 模板和 DOM 操作库。
- [Enfocus](http://ckirkendall.github.io/enfocus-site/) - 受 Enlive 启发的 ClojureScript DOM 操作和模板库。
- [Freactive](https://github.com/aaronc/freactive) - 一个高性能、纯 Clojurescript、声明性 DOM 库，灵感来自reagent、om、reflex 和 hiccup。
- [Hiccups](https://github.com/teropa/hiccups) - Hiccup 的 ClojureScript 端口。
- [Hickory](https://github.com/davidsantiago/hickory) - 它将 HTML 解析为 Clojure 数据结构，因此您可以分析、转换并输出回 HTML。
- [json-html](https://github.com/yogthos/json-html) - 提供 JSON 并获取具有该 JSON 的人类表示形式的 DOM 节点。
- [Kioo](https://github.com/ckirkendall/kioo) - ClojureScript 中 Facebook 的 React 和 Om 的 DOM 操作和模板库。
- [Respo](https://github.com/mvc-works/respo) - 一个响应式 DOM 库，受 React 启发。
- [Sablono](https://github.com/r0man/sablono) - ClojureScript 中 Facebook React 的 Lisp/Hiccup 风格模板。


### 文档
- [codox](https://github.com/weavejester/codox) - 用于从 Clojure 或 ClojureScript 源代码生成 API 文档的工具。


### 图形
- [geom](https://github.com/thi-ng/geom) - 用于 Clojure/Clojurescript 的 2D/3D 几何工具包。
- [Quil](https://github.com/quil/quil) - 处理和图形编程库。


### HTTP处理程序
- [Castra](https://github.com/hoplon/castra) - Clojure 的 HTTP 远程过程调用处理程序。


### 国际化
- [Tempura](https://github.com/ptaoussanis/tempura) - 继 Tower 后的 Clojure(Script) i18n 库
- [Tower](https://github.com/ptaoussanis/tower) - Clojure（脚本）i18n 和 L10n 库。


### JavaScript 互操作性
- [CLJSJS](http://cljsjs.github.io/) - Clojurescript 开发人员依赖 Javascript 库的一种简单方法。
- [Jayq](https://github.com/ibdknox/jayq) - jQuery 的 ClojureScript 包装器。
- [Purnam](https://github.com/zcaudate/purnam) - ClojureScript 库，旨在提供更好的 clojurescript/javascript 互操作、测试和文档工具。
- [Pylon](https://github.com/bodil/pylon) - 100% Clojurescript 中的 Javascript 类系统。


### CSS工具
- [Garden](https://github.com/noprompt/garden) - 用于在 Clojure 和 ClojureScript 中渲染 CSS 的库。
- [stylefy](https://github.com/jarzka/stylefy) - stylefy 可以将 UI 组件样式定义为 Clojure 数据，并将它们轻松附加到组件中，而无需编写 CSS 选择器


### 杂项
- [Automat](https://github.com/ztellman/automat) - 受 Ragel 启发，用于定义和使用有限状态自动机的 Clojure(Script) 库。
- [Bardo](https://github.com/pleasetrythisathome/bardo) - 用于函数插值和转换的 Clojure(Script) 库。
- [core.async](https://github.com/clojure/core.async/) - 一个 Clojure(Script) 库，旨在提供异步编程和通信设施。
- [Entanglement](https://github.com/Frozenlock/entanglement) - 它从其他原子创建原子并将数据链接在一起。
- [inflections-clj](https://github.com/r0man/inflections-clj) - Clojure 和 ClojureScript 的类似 Rails 的变形库。
- [Keybind](https://github.com/piranha/keybind) - 用于处理浏览器中的键绑定（快捷方式）的库。
- [markdown-clj](https://github.com/yogthos/markdown-clj) - Clojure/ClojureScript 中的 Markdown 解析器。
- [namespacefy](https://github.com/Jarzka/namespacefy) - 一个简单的 Clojure(Script) 库，旨在轻松保持映射键命名空间，无论您的数据来自何处。
- [om-tools](https://github.com/plumatic/om-tools) - 它旨在提供在使用 Om 的 API 构建组件时经常有用的高阶抽象和实用程序。
- [reforms](https://github.com/bilus/reforms) - 适用于 Om 和 Reagent 的漂亮 Bootstrap 3 表单。
- [reagent-forms](https://github.com/reagent-project/reagent-forms/) - 试剂的引导表单组件。
- [Sepal.clj](https://github.com/Cirru/sepal.clj) - 一个用宏系统从字符串向量和向量生成 Clojure 代码的库。

### React.js 接口
- [Brutha](https://github.com/weavejester/brutha) - 一个简单而实用的 React ClojureScript 接口。
- [cljsx](https://github.com/peterhudec/cljsx) - [JSX](https://reactjs.org/docs/introducing-jsx.html) 适用于 Clojure 和 ClojureScript，也适用于 [Inferno](https://infernojs.org)、[Nerv](https://nerv.aotu.io/)、[Preact](https://preactjs.com/)、[Snabbdome](https://github.com/snabbdom/snabbdom) 等。
- [Helix](https://github.com/lilactown/helix) - 一个简单、易于使用的库，用于 ClojureScript 中的 React 开发，在 React 之上几乎没有语义。
- [hx](https://github.com/Lokeh/hx) - 另一个简单易用的 ClojureScript 中 React 开发库。
- [Om](https://github.com/omcljs/om) - React 的强大接口利用了其面向对象的结构。
- [Quiescent](https://github.com/levand/quiescent) - 它偏向于函数式风格，完全无状态。
- [re-com](https://github.com/Day8/re-com) - Reagent 的可重用组件的 ClojureScript 库。
- [Reagent](http://reagent-project.github.io/) - 简约，功能齐全。
- [Rum](https://github.com/tonsky/rum) - 分解、可扩展、简单。


### 反应式编程
- [Javelin](https://github.com/hoplon/javelin) - ClojureScript 的函数反应式编程库。
- [Manifold-cljs](https://github.com/dm3/manifold-cljs) - [Manifold](https://github.com/ztellman/manifold) 到 ClojureScript 的端口。
- [Reagi](https://github.com/weavejester/reagi) - 用于 Clojure 和 ClojureScript 的 FRP 库，构建于 core.async 之上。
- [rx-cljs](https://github.com/leonardoborges/rx-cljs) - Javascript 反应式扩展 (Rx) 的 ClojureScript 包装器。
- [Yolk](https://github.com/Cicayda/yolk) - bacon.js 的一个瘦 ClojureScript 包装器。


### 路由
- [Bidi](https://github.com/juxt/bidi) - Clojure（脚本）数据驱动的路由库。
- [Router](https://github.com/darkleaf/router) - Clojure/Script 的双向环形路由器。以休息为导向。
- [Secretary](https://github.com/gf3/secretary) - ClojureScript 的客户端路由器。
- [Silk](https://github.com/DomKM/silk) - Clojure 和 ClojureScript 的同构路由库。


### 状态管理
- [component](https://github.com/stuartsierra/component) - Clojure(Script) 中有状态对象的托管生命周期。
- [hodgepodge](http://funcool.github.io/hodgepodge/) - HTML5 存储的惯用 ClojureScript 接口。
- [mount](https://github.com/tolitius/mount) - 一个漂亮且惯用的状态管理库。
- [plato](https://github.com/eneroth/plato) - 增量地将原子状态保存到 ClojureScript 中的本地存储中。
- [storage-atom](https://github.com/alandipert/storage-atom) - 由 HTML5 Web 存储支持的 ClojureScript 原子。
- [Tuck](https://github.com/tatut/tuck) - 一个用于构建 Reagent 应用程序的微框架，该应用程序将视图代码和事件处理代码完全分离。
- [Waltz](https://github.com/ibdknox/waltz) - 一个 ClojureScript 库，可帮助使用非确定性有限状态机管理客户端应用程序中的状态。


### 测试
- [cljs.test](https://github.com/clojure/clojurescript/wiki/Testing) - ClojureScript 的集成测试框架（合并自 [clojurescript.test](https://github.com/cemerick/clojurescript.test)）
- [Expectations](http://jayfields.com/expectations/) - 极简主义的单元测试框架。
- [Speclj](https://github.com/slagyr/speclj) - Clojure 和 ClojureScript 的 TDD/BDD 框架。
- [test.check](https://github.com/clojure/test.check) - 受 QuickCheck 启发的基于属性的生成测试工具。


### 验证
- [Bouncer](https://github.com/leonardoborges/bouncer) - Clojure 和 Clojurescript 应用程序的验证 DSL。
- [form-validator-cljs](https://github.com/kwladyka/form-validator-cljs) - 使用spec和fn验证表单。
- [Validateur](http://clojurevalidations.info/) - 受 Ruby ActiveModel 启发的 Clojure 验证库。


### 网页框架和模板
- [atw-om](https://github.com/zaiste/atw-om) - 使用 Clojure/Compojure、ClojureScript/Om 和 core.async 的 Web 应用程序模板。
- [Chestnut](https://github.com/plexus/chestnut) - 具有实时重新加载功能的 ClojureScript/Om 应用程序模板。
- [Clops](https://github.com/sveri/closp) - 一个固执己见、完整堆栈且易于使用的 Web 框架。
- [descjop](https://github.com/karad/lein_template_descjop) - 使用 Electron 的基于 Web 的桌面应用程序的模板。
- [electron-template](https://github.com/ducky427/electron-template) - 用于使用 Electron、ClojureScript 和 Reagent 创建基于 Web 的桌面应用程序的模板。
- [Fulcro](http://fulcrologic.github.io/fulcro) - 用于在 clj/cljs 中开发单页全栈 Web 应用程序的库。
- [Hoplon](http://hoplon.io) - 使用 Clojure 和 ClojureScript、客户端和服务器端编写所有内容。
- [Keechma](http://keechma.com) - ClojureScript 和 Reagent 的微前端框架。
- [Luminus](http://www.luminusweb.net/) - 它旨在提供一个强大、可扩展且易于使用的平台。
- [Macchiato](https://github.com/macchiato-framework/macchiato-core) - 它旨在为 Node.js 提供一个易于使用的平台。
- [Mies](https://github.com/swannodette/mies) - 最小的 ClojureScript 项目模板。
- [Mr-Clean](https://bitbucket.org/sonwh98/mr-clean) - 一个试剂兼容库，不依赖于react.js。
- [Precept](https://github.com/CoNarrative/precept) - 声明式编程框架。
- [re-frame](https://github.com/Day8/re-frame) - 用 Clojurescript 编写 SPA 的试剂框架。
- [Tenzing](http://martinklepsch.github.io/tenzing/) - 没有使用 Boot 的后端的 ClojureScript 模板。
- [WebFUI](https://github.com/drcode/webfui) - ClojureScript 的客户端 Web 框架。


### WebSockets
- [Chord](https://github.com/jarohen/chord) - 旨在弥合 CLJ/CLJS、Web-sockets 和 core.async 三者之间的差距。
- [Sente](https://github.com/ptaoussanis/sente) - Clojure（脚本）+ core.async + WebSockets/Ajax。


* * *


## 贡献
欢迎所有贡献。在打开拉取请求之前，请阅读 [Contributing](CONTRIBUTING.md)。 tl;dr `-` 用于项目符号，`–` 用于链接和描述之间的分隔符，列表应按字母顺序排列。


## 许可证
[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png)](http://creativecommons.org/publicdomain/zero/1.0/)

[Han Tuzun](http://hantuzun.com) 在法律允许的范围内，放弃了其在全球范围内根据版权法对该作品享有的所有权利，包括所有相关和邻接权，并将该作品奉献给公共领域。

您可以复制、修改、分发和执行该作品，甚至可以用于商业目的，而无需征求许可。
