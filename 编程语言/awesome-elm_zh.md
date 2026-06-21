
<div align="center">
    <img src="./assets/elm-logo.svg" height="180" width="180" />
    <h1>Awesome Elm</h1>
    <br />
</div>

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome) [![Build Status](https://app.travis-ci.com/sporto/awesome-elm.svg?branch=master)](https://app.travis-ci.com/sporto/awesome-elm)

社区驱动的有用 Elm 教程、库和软件列表。
受到 [awesome](#more-awesome) 列表的启发。请随意<a href="https://github.com/sporto/awesome-elm/blob/master/CONTRIBUTION.md" target="_blank">改进</a>此列表。


## 目录
- [学习指南](#learning-guides)
- [学习视频](#learning-videos)
- [Articles](#articles)
- [会议视频](#conference-videos)
- [News](#news)
- [Podcasts](#podcasts)
- [Testing](#testing)
- [代码生成器](#code-generators)
- [包管理器](#package-managers)
- [Libraries](#libraries)
- [Boilerplates](#boilerplates)
- [Frameworks](#frameworks)
- [静态分析](#static-analysis)
- [静态站点生成器](#static-site-generators)
- [展示发电机](#showcase-generators)
- [运行榆树](#run-elm)
- [编译并捆绑](#compile-and-bundle)
- [其他工具](#other-tools)
- [编辑器插件](#editor-plugins)
- [Examples](#examples)
- [社区和支持](#community-and-support)
- [Conferences](#conferences)
- [灵感来自榆树](#inspired-by-elm)
- [超越 DOM](#beyond-the-dom)
- [更多精彩](#more-awesome)
- <a href="https://github.com/sporto/awesome-elm/blob/master/CONTRIBUTION.md" target="_blank">贡献指南</a>

---

## 学习指南

*了解这个很棒的东西是什么。*

* [Official tutorial](http://elm-lang.org/docs) - 一般信息和带有示例的深入指南。
* [Elm in Action](https://www.manning.com/books/elm-in-action) - Manning Publications 为 Elm 初学者提供的深入书籍。
* [Architecture Tutorial](https://github.com/evancz/elm-architecture-tutorial) - 如何创建可与您的应用程序完美扩展的模块化 Elm 代码。
* [Exercism Elm Track](http://exercism.io/languages/elm) - 榆树练习集。
* [Learn you an Elm](http://learnyouanelm.github.io/) - Elm 教程包含详尽的示例和描述。
* [Beginning Elm](http://elmprogramming.com/) - 对 Elm 编程语言的简单介绍。
* [Elm patterns](http://sporto.github.io/elm-patterns/index.html) - Elm 中常见模式的集合。
* [Elm Koans](https://github.com/robertjlooby/elm-koans) - 练习 Elm 学习练习。
* [Learn Elm](https://github.com/dwyl/learn-elm) - 探索美丽的编程语言，它使前端 Web 应用程序的构建和维护变得充满乐趣！
* [Learn Elm in Y Minutes](https://learnxinyminutes.com/docs/elm/) - 语法和功能概述。 [learnxinyminutes.com](https://learnxinyminutes.com) 上的 Elm 页面
* [Elm Maybe - Dealing with null/Nothing](http://rundis.github.io/blog/2016/elm_maybe.html) - 使用 Maybe 类型，并提供注释良好的代码示例。
* [Programming Elm](https://pragprog.com/book/jfelm/programming-elm) - 《实用程序员》中的一本详尽的书，涵盖基础知识和高级概念。
* [Elm cheat sheet](https://github.com/izdi/elm-cheat-sheet) - 语法和功能概述。
* [Ninety-nine Problems, Solved in Elm](https://johncrane.gitbooks.io/ninety-nine-elm-problems/content/) - 对 Elm 的改编自九十九个 Haskell 问题。
* [Elm Tutorials on Codementor](https://www.codementor.io/elm/tutorial) - 关于使用 Elm 构建 Web 应用程序的两个教程。
* [Elm programming language](https://en.wikibooks.org/wiki/Elm_programming_language) - Elm 作为编程语言的简要概述。
* [Elm: A Beginners' Guide to Elm and Data](https://www.sitepoint.com/premium/courses/elm-a-beginners-guide-to-elm-and-data-2940) - Elm 和数据初学者课程
* [Practical Elm for a Busy Developer](https://korban.net/elm/book) - 一本关于开发 Elm 应用程序的实际方面的非初学者书籍。
* [Haskell to Elm](https://github.com/eeue56/haskell-to-elm) - Elm 与 Haskell 不同之处的示例集合，针对具有 Haskell 背景的 Elm 初学者。
* [A nice app on Elm street](https://madewithlove.com/blog/software-engineering/using-elm-with-react-a-nice-app-on-elm-street/) - 榆树简介
* [The Elmish Book](https://zaid-ajaj.github.io/the-elmish-book) 按照 Elm 架构的首要原则，使用 [F#](https://dotnet.microsoft.com/languages/fsharp) 构建 Web 应用程序。
* [Elm patterns](https://sporto.github.io/elm-patterns/) - 编码模式的集合。
* [Codings hints](https://github.com/elm/compiler/tree/master/hints) - Evan 的自述文件列表。
* [Ellies catalog](https://janiczek-ellies.builtwithdark.com/) - Ellie 中的小例子集合。
* [Elm Cookbook](https://orasund.gitbook.io/elm-cookbook/) - 一本关于 Elm 的数字书。
* [Awesome Elm PLTD](https://github.com/pd-andy/awesome-elm-pltd) - 有关 Elm 编程语言理论和开发的有用资源。

**[：顶部：回到顶部]（#目录）**

### 过时的教程和书籍（Elm 0.18 或更早版本）

* [Elm: Building Reactive Web Apps](https://pragmaticstudio.com/elm) - 了解如何使用 Elm 构建响应式 Web 应用程序。
* [Writing native](https://github.com/NoRedInk/take-home/wiki/Writing-Native) - 了解如何为 Elm 创建本机 JavaScript 模块。
* [Elm: Functional frontend development](https://dennisreimann.de/articles/elm.html) - 有关基础知识和高级主题的系列文章。
* [Elm Tutorial](https://sporto.gitbooks.io/elm-tutorial/content/) - 有关使用 Elm 开发单页 Web 应用程序的教程。
* [Elm Seeds](https://elmseeds.thaterikperson.com/) - Erik Person 教您 Elm 编程语言的简短截屏视频。
* [Elm For Beginners - Video Course](http://courses.knowthen.com/courses/elm-for-beginners) - 构建您的第一个 Elm Web 应用程序。
* [Single-Page Web Apps in Elm](https://www.linkedin.com/pulse/single-page-web-apps-elm-part-one-getting-started-new-kevin-greene) - Elm 教程由五部分组成。
* [Elm FAQ](http://faq.elm-community.org/) - 来自 [Elm 社区](http://elm-community.org/) 的 Elm 常见问题解答。
* [Elm Tutorial by Auth0](https://auth0.com/blog/creating-your-first-elm-app-part-1/) - 有关在 Elm 中构建应用程序（从身份验证到调用 API）的教程。

**[：顶部：回到顶部]（#目录）**

---

### 学习视频

* [Welcome to Elm](https://www.youtube.com/playlist?list=PLuGpJqnV9DXq_ItwwUoJOGk_uCr72Yvzb) - 有关学习所有 Elm 基础知识的视频播放列表。
* [Elm The Complete Guide](https://www.udemy.com/course/elm-the-complete-guide/) - 视频教程包括 Elm UI、Elm Review、响应式设计、测试等。
* [Egghead.io: Elm videos](https://egghead.io/q?q=elm) - Egghead 的 Elm 视频培训，很多都是免费的。
* [Elm Basics](https://www.youtube.com/watch?v=g48K6ABfRzA) - 浏览 Elm 作为通用编程语言的所有语法和基本思想。
* [Greg Ziegan: Elm live coding videos ](https://www.youtube.com/channel/UCJt-EkypIn-HoxNhoHqXmIA) - YouTube 上的实时编码视频。

**[：顶部：回到顶部]（#目录）**

---

## 文章

*阅读要点。查看 Elm 官方博客：[elm-lang.org/blog](http://elm-lang.org/blog)*

### 为什么是榆树？

* [Side-effects of Elm in production](http://nonullpointers.com/posts/2019-05-28-side-effects-of-elm-in-production.html?utm_campaign=Elm%20Weekly&utm_medium=email&utm_source=Revue%20newsletter) - Bellroy 的经验报告
* [How Elm Made Our Work Better](http://futurice.com/blog/elm-in-the-real-world) - 团队如何使用 Elm 为客户构建关键业务 Web 应用程序。
* [FP with games in Elm](https://github.com/Dobiasd/articles/blob/master/switching_from_imperative_to_functional_programming_with_games_in_Elm.md) - 在 Elm 中使用游戏从命令式编程切换到函数式编程。
* [Blazing Fast HTML](http://elm-lang.org/blog/blazing-fast-html) - Elm 中的虚拟 DOM。
* [Elm from a Business Perspective](http://www.gizra.com/content/elm-business-perspective/) - 本文从业务角度讨论有关 Elm 的主题
* [Move fast and don’t break things. Running a startup on Elm](https://medium.com/the-ahead-story/move-fast-and-dont-break-things-running-a-startup-on-elm-b5491082fe8b#.c534m1e1t) - 关于瑞典初创公司 Elm 开发的一些想法。
* [Elm: A frontend story that a backend dev can love](https://niteo.co/blog/elm-a-frontend-story-that-a-backend-dev-can-love/) - Elm 如何独一无二地适合后端开发人员大脑的故事

### 杂项文章

* [Learning FP the hard way](https://gist.github.com/ohanhi/0d3d83cf3f0d7bbea9db) - Elm 语言的经验。
* [Blog of Brian Hicks](https://www.brianthicks.com) - 包含有关 Elm 的各种主题的博客。
* [Introduction to The Elm Architecture and How to Build our First Application](https://css-tricks.com/introduction-elm-architecture-build-first-application/) - 一篇描述 Elm 架构以及如何构建简单应用程序的文章
* [Functional Programming for Web Frontend by Jan Luxemburk](https://drive.google.com/file/d/0BzfJvCA4sXjQNjJwd2twQUFOU0k/view) - 一篇关于前端开发函数式编程的学士论文，重点关注 Elm。

### 过时的文章（与当前的 Elm 架构无关）

* [Elm for Web Developers](https://github.com/eeue56/elm-for-web-developers) - 为考虑迁移到 Elm 的 Web 开发人员提供的笔记集合。
* [Elm & Components](https://medium.com/p/elm-components-3d9c00c6c612) - 一篇博客文章描述了减少 TEA 样板文件的可能方法。对于组件库和任何有兴趣了解函数类型可以做的令人惊奇的事情的人很有用。
* [Composing Features and Behaviours in the Elm Architecture](https://github.com/foxdonut/adventures-reactive-web-dev/tree/master/client-elm#composing-features-and-behaviours-in-the-elm-architecture) - 这篇文章描述了如何将遵循 Elm 架构的代码组织成独立的功能、如何在功能之间进行通信以及如何将其中一些功能组合在一起以组装更大的功能。
* [Getting Started with Elm](https://medium.com/@diamondgfx/getting-started-with-elm-11d7a53b1a78) - Elm 教育教程系列。
* [Elm & Guarantees](https://medium.com/@debois/elm-guarantees-92a66679f7bd) - 现实地了解 Elm 相对于其他选项的优劣。

**[：顶部：回到顶部]（#目录）**

---

## 会议视频

*观看有关 Elm 的精彩演讲*

这些大多是会议演讲，有关学习 Elm 的视频请参见 [学习视频](#learning-videos) 部分。

### 播放列表

* [Elm Conf 2019](https://www.youtube.com/playlist?list=PLglJM3BYAMPGsAM4QTka7FwJ0xLPS0mkN) - 2019 年 9 月
* [Elm Europe 2019](https://www.youtube.com/playlist?list=PL-cYi7I913S_oRLJEpsVbSTq_OOMSXlPD) - 2019年6月
* [Elm in the Spring 2019](https://www.youtube.com/channel/UC_wKoNegfKbmVIPg7YYKLWQ) - 2019年6月
* [Oslo Elm Day 2019](https://www.youtube.com/playlist?list=PLcAzxXzXQlPbalOfueVbHCRSo26ksIXiF) - 2019年2月
* [Elm Conf 2018](https://www.youtube.com/playlist?list=PLglJM3BYAMPHuB7zrYkH2Kin2vQOkr2xW) - 2018 年 elm-conf 的所有演讲
* [Elm Europe 2018](https://www.youtube.com/playlist?list=PL-cYi7I913S-VgTSUKWhrUkReM_vMNQxG) - 2018 年 Elm Europe 所有演讲的播放列表
* [Elm Conf 2017](https://www.youtube.com/playlist?list=PLglJM3BYAMPFTT61A0Axo_8n0s9n9CixA) - 2017 年 elm-conf 的所有演讲
* [Elm Europe 2017](https://www.youtube.com/playlist?list=PL-cYi7I913S8cGyZWdN6YVZ028iS9BfpM) - 2017 年 Elm Europe 所有演讲的播放列表
* [Oslo Elm Day 2017](https://www.youtube.com/playlist?list=PLcAzxXzXQlPZsNcYycHittqeF3UG4dGli) - 2017 年奥斯陆榆树日所有演讲的播放列表
* [Elm Conf 2016](https://www.youtube.com/playlist?list=PLglJM3BYAMPH2zuz1nbKHQyeawE4SN0Cd) - 2016 年 elm-conf 的所有演讲

### 杂项视频

* [Dillon Kearns: Types Without Borders | 2018](https://www.youtube.com/watch?v=memIRXFSNkU) - elm-conf 2018 讨论了使用 GraphQL 等外部模式的端到端类型安全性。
* [Jamison Dance: Rethinking All Practices - Building Applications in Elm | 2016](https://www.youtube.com/watch?v=txxKx_I39a8) - 在 React.js Conf 2016 上发表的演讲，内容涉及 Elm 必须向 JavaScript 世界传授什么以及为什么 JS 开发人员应该考虑尝试它。
* [Richard Feldman: Introduction to Elm | 2016](https://www.youtube.com/watch?v=3_M2G9U51GA) - 演讲对 Elm 进行了广泛、高层次的介绍。
* [Amitai Burstein: Frontend with Guarantees | 2016](https://www.youtube.com/watch?v=FgaoOgJ5CAU) - 《You Gotta Love Frontend 2016》的演讲
* [Jessica Kerr: Adventures in Elm | 2016](https://www.youtube.com/watch?v=cgXhMc8M4X4) - 在 GOTO Chicago 2016 上关于函数式编程与 Elm 结合的演讲。
* [Aaron VonderHaar：Codevember | 2016 ](https://www.youtube.com/playlist?list=PLDA4wlOlLJvXAEsJDje4hdLazsihZiQNf) + [ElmLive](https://www.youtube.com/playlist?list=PLDA4wlOlLJvWSYo3KiEa4q4ETkXpTaKlw) - Elm 直播视频示例。
* [Richard Feldman: Making impossible states impossible | 2016](https://www.youtube.com/watch?v=IcgmSRJHu_8) - 讨论如何在 Elm 中对数据结构进行建模，使无效状态无法表示
* [Richard Feldman: Effects as Data | 2015](https://www.youtube.com/watch?v=6EdXaWfoslc) - 关于 Elm 如何管理副作用的讨论。
* [Richard Feldman: Make the Back-End Team Jealous: Elm in Production | 2015](http://www.youtube.com/watch?v=FV0DXNB94NE) - 关于 Elm 以及在生产中使用它的初始步骤的讨论。
* [Evan Czaplicki: Let's be mainstream! User focused design in Elm | 2015](https://www.youtube.com/watch?v=oYk8CKH7OhE) - Elm 之父关于该语言背后的哲学的演讲。

---

## 新闻动态

* [Official Elm News](https://elm-lang.org/news) - Elm 官方博客
* [Elm Weekly](http://www.elmweekly.nl/) - 关于 Elm 的每周通讯
* [Elm Bits](https://elmbits.com/) - 关于 Elm 的免费每周时事通讯，其中包含精选的新闻、文章、书籍、活动、工具和库。
* [Elm News](https://elm-news.com/) - 所有 Elm 新闻都集中在一处
* [Elm Greenwood](https://releases.elm.dmy.fr/) - Elm 软件包发布
* [Elm Reddit](https://www.reddit.com/r/elm/) - Reddit 上的 Elm 新闻

---

## 播客

*收听有关 Elm 的播客*

* [Elm Radio](https://elm-radio.com) - 了解 Elm 生态系统中的工具和技术。
* [Elm Town](https://elmtown.github.io/) - 关于 Elm 社区人员的播客（已过时）。

### 个人播客剧集

* [Functional Geekery 33](https://www.functionalgeekery.com/functional-geekery-episode-33-richard-feldman-and-tessa-kelly/) - 理查德·费尔德曼和泰莎·凯利。
* [The Changelog 218](https://changelog.com/podcast/218) - Elm 与 Evan Czaplicki 和 Richard Feldman
* [The Changelog 191](https://changelog.com/podcast/191/) - Richard Feldman 的 Elm 和函数式编程。
* [Software Engineering Daily](http://softwareengineeringdaily.com/2015/11/03/elm-with-richard-feldman-and-srinivas-rao/) - Elm 与理查德·费尔德曼和斯里尼瓦斯·拉奥。
* [The Web Platform Podcast 15](http://thewebplatform.libsyn.com/functional-programming-with-elm-clojurescript-om-and-react) - 使用 Elm、ClojureScript、Om 和 React 进行函数式编程。
* [The Web Platform Podcast 76](http://thewebplatformpodcast.com/76-the-elm-programming-language) - Elm 编程语言。
* [The Web Platform Podcast 108](http://thewebplatformpodcast.com/108-elm-revisited) - 榆树重访。
* [Full Stack Radio 44](http://www.fullstackradio.com/44) - 榆树到底是什么？在本集中，Joel Clermont 谈论 Elm 和函数式编程。
* [InfoQ Podcast 2017-04-27](https://www.infoq.com/podcasts/richard-feldman) - Richard Feldman 讨论 Elm 与 React.js 的比较

**[：顶部：回到顶部]（#目录）**

---

## 测试

用于测试 Elm 应用程序的工具和库

* [Elm test](https://github.com/elm-explorations/test) - 单元测试和模糊测试
* [Elm Program test](https://github.com/avh4/elm-program-test/tree/3.0.0) - 测试完整的 Elm 程序
* [Elm Spec](https://github.com/brian-watkins/elm-spec) - 描述 Elm 程序的行为。

**[：顶部：回到顶部]（#目录）**

---

## 代码生成器

* [Elm Bridge](https://github.com/agrafix/elm-bridge) - 从 Haskell 生成 Elm 类型
* [Elm CodeGen](https://github.com/mdgriffith/elm-codegen) - 生成 Elm 代码
* [Elm TS Interop](https://github.com/dillonkearns/elm-ts-json) - 在 Elm 和 TypeScript 之间构建编码器/解码器。
* [Elm TypeScript Interop](https://github.com/dillonkearns/elm-typescript-interop) - 从 Elm 生成 TypeScript 定义（“Elm TS Interop”是其改进版本）。
* [elm-gql](https://github.com/vendrinc/elm-gql) - 从 GraphQL 查询生成 GraphQl 客户端代码
* [elm-graphql](https://github.com/dillonkearns/elm-graphql) - 从 GraphQL 模式生成 GraphQl 客户端代码
* [haskell-to-elm](https://github.com/folq/haskell-to-elm) - 从 Haskell 类型生成 Elm 类型、编码器和解码器
* [HTML to Elm](http://mbylstra.github.io/html-to-elm/) - 将 HTML 转换为 Elm Html。将应用程序移植到 Elm 时很有用。
* [JSON Schema to Elm](https://github.com/dragonwasrobot/json-schema-to-elm) - 根据 JSON 模式规范生成 Elm 类型、JSON 解码器、JSON 编码器和模糊测试
* [OpenApi Generator](https://github.com/OpenAPITools/openapi-generator) - 为 Elm 生成 OpenApi 类型。
* [PostCSS Elm Tailwind](https://github.com/monty5811/postcss-elm-tailwind) - 在你的榆树上放一些顺风
* [Protoc Gen Elm](https://github.com/andreasewering/protoc-gen-elm) - 从 .proto 文件生成 Protobuf En/Decoders
* [Quicktype](https://github.com/quicktype/quicktype) - 从 JSON 生成 JSON 解码器和编码器
* [Travelm Agency](https://github.com/andreasewering/travelm-agency) - 从翻译文件生成类型安全的 Elm 代码

**[：顶部：回到顶部]（#目录）**

---

## 包管理器

*共享 Elm 库的地方。*

* [elm-package](https://github.com/elm-lang/elm-package) - 用于共享 Elm 库的命令行工具。

**[：顶部：回到顶部]（#目录）**

---

## 图书馆

您可以在以下位置找到数百个高质量的软件包：

* [Elm packages](https://package.elm-lang.org/) - 官方注册表
* [Elm Catalog](https://korban.net/elm/catalog) - 在按类别组织的目录中查找包。
* [Elm Search](http://klaftertief.github.io/elm-search/) - 在 Elm 文档中搜索运算符、函数签名等。

**[：顶部：回到顶部]（#目录）**

---

## 样板文件

*新 Elm 项目的良好起点。*

* [create-elm-app](https://github.com/halfzebra/create-elm-app) - 创建无需构建配置的 Elm 应用程序。
* [elm-boil](https://github.com/GioPat/elm-boil) - 用于创建易于运行、构建和部署的 Elm 样板项目的命令行实用程序
* [elm-live](https://github.com/wking-io/elm-live) - Elm 的灵活开发服务器。包括实时重新加载。
* [elm-webpack-4-starter](https://github.com/romariolopezc/elm-webpack-4-starter) - Elm webpack 4 入门模板。
* [example-elm-hot-webpack](https://github.com/klazuka/example-elm-hot-webpack) - 显示 Elm 0.19 和 Webpack 热模块重新加载的示例
* [Elm Batteries](https://github.com/cedricss/elm-batteries) - 适用于 Elm、Parcel、Cypress 和 Netlify 的项目模板和生成器
* [IHP + Elm](https://www.youtube.com/watch?v=b9ULHutH6ag) - IHP Haskell 框架提供了一个内置的 Elm 样板，在前端使用 elm 并在后端使用 haskell 时非常有用

### 过时的样板

* [elm-webpack-starter](https://github.com/moarwick/elm-webpack-starter) - 用于编写 Elm 应用程序的简单 Webpack 设置。
* [elm-app-boilerplate](https://github.com/gkubisa/elm-app-boilerplate) - Elm 应用程序的功能齐全的基础项目：Webpack、HMR、ES6、JS 和 Elm 测试、语义 UI、示例代码等。
* [elmkit](https://github.com/khusnetdinov/elmkit) - 一个基于早午餐的轻量级网络应用程序设置。包括早午餐、热模块更换、Elm、Scss、Elm 测试。
* [elm-boilerplate](https://github.com/guillaumearm/elm-boilerplate) - 一个简单的 Makefile 能够创建 Elm 应用程序。
* [elm-init](https://github.com/JustusAdam/elm-init) - 新 Elm 项目的交互式设置。
* [elm-new](https://github.com/simonewebdesign/elm-new) - 基于模板生成初始项目脚手架。
* [elm-webpack-starter-kid](https://github.com/FranzSkuffka/elm-webpack-starter-kid) - 一个非常非常基本的 elm + webpack 4 模板。
* [generator-elm-mdl](https://github.com/ashellwig/generator-elm-mdl) - Yeoman 生成器，用于利用 Material Design 的简单 elm 应用程序。

**[：顶部：回到顶部]（#目录）**

---

## 框架

*将框架方法引入 Elm 的项目（脚手架、路线生成等）*

- [elm-spa](https://www.elm-spa.dev/) - 在 Elm 中制作单页应用程序的框架。
- [Elm Land](https://elm.land/) - 用于构建 Elm 应用程序的框架。
- [Spades](https://github.com/rogeriochaves/spades) - 启动 Elm SPA，为现实世界做好准备。

---

## 静态分析

* [Elm Analyse](https://github.com/stil4m/elm-analyse) - Elm 编程语言的 Linter。
* [Elm Review](https://github.com/jfmengels/elm-review) - Elm 编程语言的代码审查器。

**[：顶部：回到顶部]（#目录）**

---

## 静态站点生成器

* [Elm Pages](http://elm-pages.com) - 静态站点生成器，可预渲染 HTML 并合并到 Elm 客户端应用程序中（[这里是与 elmstatic 的简要比较](https://elm-pages.com/blog/introducing-elm-pages#comparing-elm-pages-and-elmstatic)）。
* [Elmstatic](https://korban.net/elm/elmstatic) - 基于 Elm 的静态站点生成器。
* [elm-starter](https://github.com/lucamug/elm-starter) - 一个基于 Elm 的实验性引导程序，也可以插入到现有的 Elm 应用程序中。

**[：顶部：回到顶部]（#目录）**

---

## 展示发电机

* [Elm Book](http://elm-book-in-elm-book.netlify.app) - 基于 Storybook 和 HexDocs 的丰富文档生成器。
* [Elm UI Explorer](https://github.com/kalutheo/elm-ui-explorer) - 展示您的观点和状态。

**[：顶部：回到顶部]（#目录）**

---

## 运行榆树

* [Ellie](https://ellie-app.com/) - Elm 实时编辑器
* [Elm Editor](https://elm-editor.com/) - 高级 Elm 实时编辑器
* [run-elm](https://github.com/jfairbank/run-elm) - 从命令行运行 Elm 代码
* [elm-instant](https://atom.io/packages/elm-instant) - atom 包来尝试编辑器中的 elm 代码。提供可视化 REPL 和预览窗格。
* [Glitch](https://glitch.com/search?q=elm&activeFilter=project) - 在浏览器中构建快速、全栈的 Web 应用程序。
* [Elm Live](https://elm-live.com/) - Elm 的灵活开发服务器。包括实时重新加载！
* [Elm Watch](https://github.com/lydell/elm-watch) - 观看模式下的“elm make”。快速可靠。

**[：顶部：回到顶部]（#目录）**

---

## 编译并捆绑

* [elm-compiler](https://github.com/elm/compiler) - 官方 Elm 编译器。
* [elm-webpack-loader](https://github.com/elm-community/elm-webpack-loader) - Webpack 加载器 Elm。
* [Parcel](https://parceljs.org/languages/elm/) - 使用包裹捆绑榆树。
* [vite-plugin-elm](https://github.com/hmsk/vite-plugin-elm) - Elm 的 Vite 插件。

### 无人维护

* [grunt-elm](https://github.com/rtfeldman/grunt-elm) - 将 Elm 文件编译为 JavaScript 的 Grunt 插件。

**[：顶部：回到顶部]（#目录）**

---

## 其他工具

*与 Elm 相关的有用工具。*

* [Elm Catalog](https://korban.net/elm/catalog) - Elm 工具目录。
* [Dependabot](https://dependabot.com) - 自动更新 elm.json 的 PR。
* [Elm Doc Preview](https://github.com/dmy/elm-doc-preview) - Elm 离线文档预览器。
* [Elm Format](https://github.com/avh4/elm-format) - 自动 Elm 代码格式化程序遵循 [Elm 风格指南](http://elm-lang.org/docs/style-guide)。
* [Elm JSON](https://github.com/zwilias/elm-json) - 安装、升级和卸载 Elm 依赖项
* [Elm Oracle](https://github.com/ElmCast/elm-oracle) - 查询有关 elm 源文件中的值的信息。被大多数编辑器插件使用。
* [type-o-rama](https://github.com/stereobooster/type-o-rama) - JS 类型系统的可移植性。
* [Html to Elm](https://html-to-elm.com/) - 将 HTML 转换为 Elm。
* [elm-posix](https://github.com/albertdahlin/elm-posix) - 使用 Elm 编写 CLI 程序
* [Litvis](https://github.com/gicentre/litvis) - 使用 Elm 进行文学可视化

**[：顶部：回到顶部]（#目录）**

---

## 编辑器插件

*代码编辑器中支持 Elm 的工具。*

### 原子

* [atom-linter-elm-make](https://atom.io/packages/linter-elm-make) - Atom 编辑器的 Elm 代码 linter。
* [atom-elm-snippets](https://github.com/chiefGui/atom-elm-snippets) - Atom 的 Elm 片段。
* [atom-language-elm](https://atom.io/packages/language-elm) - Atom 编辑器的语法突出显示和自动完成。
* [elmjutsu](https://atom.io/packages/elmjutsu) - Atom 编辑器的自动完成、转到定义、查找用法、重命名符号等。
* [atom-elm-navigator](https://atom.io/packages/elm-navigator) - 侧面板可帮助导航到项目中的任何函数、类型定义或端口。

### Emacs

* [emacs-elm-mode](https://github.com/jcollard/elm-mode) - Emacs 编辑器的语法突出显示、Elm REPL、Elm make 和 Elm 格式集成。

### 智能

* [elm-plugin](https://github.com/klazuka/intellij-elm) - IntelliJ IDEA 的 Elm 插件。

### 崇高的文字

* [LSP-elm](https://github.com/sublimelsp/LSP-elm) - Sublime 的 Elm 语言服务器（推荐）。
* [Elm Language Server](https://github.com/elm-tooling/elm-language-server#sublime) - Elm 的语言服务器实现
* [Elm Syntax Highlighting](https://packagecontrol.io/packages/Elm%20Syntax%20Highlighting) - Sublime Text 中 Elm 的语法突出显示。
* [Elm Format on Save](https://github.com/evancz/elm-format-on-save) - Sublime Text 插件可在保存时运行 elm 格式。

### Vim/Neovim

* [theJian/elm.vim](https://github.com/theJian/elm.vim) - Elm 语法高亮。与 [ale 或 Neoformat for Neovim](https://github.com/avh4/elm-format/issues/610) 一起使用，因为 ElmCast/elm-vim 不支持 Elm 0.19。
* [ElmCast/elm-vim](https://github.com/ElmCast/elm-vim) - Vim/Neovim 的 Elm 0.18 模式。
* [vim-elm-help](https://github.com/hoelzro/vim-elm-help) - 在编辑器中离线访问 Elm 文档。
* [emmet-vim](https://github.com/mattn/emmet-vim) - 具有 elm 支持的标记扩展。

### 视觉工作室代码

* [ElmLS](https://marketplace.visualstudio.com/items?itemName=Elmtooling.elm-ls-vscode) - Elm 语言服务器集成
* [Elmmet: Emmet for Elm (Visual Studio Code)](https://marketplace.visualstudio.com/items?itemName=necinc.elmmet) - Emmetio 缩写扩展为 Elm 函数的组合，内部有 elm-format'er。
* [HTML to Elm for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=Rubymaniac.vscode-html-to-elm) - 将 HTML 转换为 Elm 的 VSCode 插件


### 其他编辑

* [elm-light-table](https://github.com/rundis/elm-light) - 语法突出显示、REPL、自动完成、包管理以及 Light Table 的更多功能。

**[：顶部：回到顶部]（#目录）**

---

## 示例

*一些用 Elm 编写的优秀应用程序。*

* [Builtwithelm](http://builtwithelm.co/) - 使用 Elm 构建的网站，其中包含使用 Elm 构建的项目和应用程序列表。
* [Elm SPA Example](http://rtfeldman.github.io/elm-spa-example/) - 全栈 Elm 应用程序，具有 CRUD 操作、身份验证、路由、分页等。 [代码](https://github.com/rtfeldman/elm-spa-example) / [文章](https://dev.to/rtfeldman/tour-of-an-open-source-elm-spa) / [视频](https://youtu.be/RN2_NchjrJQ)
* [Elm Example App](https://github.com/sporto/elm-example-app) - Elm 中的一个小型 SPA 示例，用于学习基础知识
* [TodoMVC](https://github.com/evancz/elm-todomvc) - TodoMVC 应用程序的正确实现。
* [TodoMVC with JSON API](https://github.com/andrewsuzuki/elm-todo-rest-api) - 简单、模块化、文档丰富的待办事项应用程序，具有 JSON API 持久性。
* [TodoMVC/Firebase](https://github.com/ThomasWeiser/todomvc-elmfire) - TodoMVC 的分支演示了启动应用程序、[Elm 架构](https://github.com/evincz/elm-architecture-tutorial) 和 Firebase 作为后端。
* [TodoMVC in Electron](https://github.com/nirgn975/Elmctron) - 在 Electron 中记录并测试了 Elm TodoMVC 应用程序的实现。
* [Gipher](https://github.com/matthieu-beteille/gipher) - 使用 elm 和 firebase 构建的类似于 Tinder 的 gif 应用程序！
* [Collection of examples](https://github.com/halfzebra/elm-examples) - 一系列具有先进技术的示例，适用于现实世界的 Elm 应用程序。
* [\<elm-ement\>](https://github.com/ohanhi/elm-ement) - 自定义元素的最小示例。
* [Elm Playground](http://elm-playground.maciejsmolinski.com/) - Tiny Elm 项目的实施是为了通过示例进行学习。
* [Elm Architecture in Android](https://github.com/glung/elm-architecture-android) - 使用 Kotlin 编程语言和 Anko 库通过 Elm 架构实现的示例 Android 应用程序。
* [Elm + Phoenix + Webpack](https://github.com/ronanyeah/elm-phoenix-example) - 最小的 Elm + Phoenix 设置，使用 webpack 而不是 Brunch。
* [Spotify Mapper](https://github.com/FidelisClayton/elm-spotify-mapper) - Elm 应用程序与 Spotify Api 集成，用于搜索和探索新艺术家。
* [Pokelmon](https://github.com/brenopanzolini/pokelmon) - 使用 PokéAPI 的 Elm 项目。
* [JWT auth with Django + Elm](https://github.com/apirobot/django-elm-auth-with-jwt) - 使用 Django（后端）和 Elm（前端）进行 JSON Web Token (JWT) 身份验证。
* [Bitcoin BR Chrome Extension](https://github.com/jouderianjr/bitcoin-br-chrome-extension) - 在 Elm 中构建的 Chrome 扩展可显示所有巴西交易所的比特币价值。
* [Elmstagram](https://github.com/bkbooth/Elmstagram) - Instagram 的基本 UI 克隆 / 文章 - [第 1 部分](https://benbooth.dev/building-a-basic-ui-clone-of-instagram-using-elm-part-1/) [第 2 部分](https://benbooth.dev/building-a-basic-ui-clone-of-instagram-using-elm-part-2/) [部分3](https://benbooth.dev/building-a-basic-ui-clone-of-instagram-using-elm-part-3/)
* [Kanban Board in Elm](https://github.com/huytd/kanelm) - 使用 Elm 和 HTML5 Drag & Drop API 构建的看板（类似 trello）
* [Elm Playground](https://ccamel.github.io/playground-elm/index.html) - 纯 SPA（带路由）探索 Elm 的各个方面。
* [Elm Hacker News PWA](https://github.com/elmariofredo/elm-hn-pwa) - 使用 Elm 版本 0.18 构建的渐进式 Web 应用程序，使用官方 Hacker-News API
* [Elm Narrative Engine](https://github.com/jschomay/elm-narrative-engine) - 用于在 Elm 中构建交互式小说风格故事的框架。详细示例[elmnarrativeengine.com](http://elmnarrativeengine.com)展示了如何构建一个“选择你自己的冒险”游戏；非常适合初学者。 **榆树 v.0.19**
* [Ari's Garden](https://github.com/theiceshelf/arisgarden) - 一个作为 SPA 构建的配方 [站点](https://arisgarden.theiceshelf.com/)，也使用 Elm 解析器。
* [Bolster](https://github.com/tarbh-engineering/journal) - 端到端加密日记应用程序。
* [Conway's Game of Life](https://github.com/pecheneg2015/elm-conway-life) - 康威生命游戏的 Elm 实现。 **榆树 v.0.19**
* [Regex Nodes](https://github.com/johannesvollmer/regex-nodes) - 一个[基于节点的可视化编辑器，用于摆弄正则表达式](https://johannesvollmer.com/regex-nodes/)，用 Elm 构建。

### 游戏

* [elm-games](https://github.com/rofrol/elm-games) - 用 Elm 制作的优秀游戏列表
* [TheSpace App](https://github.com/thematters/thespace-app) - 像 DApp 这样的 Reddit 地方，在 Elm 中集成了区块链和画布（通过端口）。

**[：顶部：回到顶部]（#目录）**

---

## 社区和支持

* [Companies using Elm](https://github.com/jah2488/elm-companies) - 在生产中使用 Elm 的公司列表。

*哪里可以找到帮助。*

* [Discourse](https://discourse.elm-lang.org/) - Elm Discourse 实例（官方论坛）。
* [Reddit](https://www.reddit.com/r/elm) - Reddit 上的 Elm 板。
* [IRC](http://webchat.freenode.net/?channels=elm) - 在 elm freenode 上提问。
* [Slack](https://elm-lang.org/community/slack) - Elm 松弛社区。

**[：顶部：回到顶部]（#目录）**

---

## 会议

* [榆树会议](https://2019.elm-conf.com/)
* [欧洲榆树](https://2019.elmeurope.org/)
* [春天的榆树](https://www.elminthespring.org/)
* [奥斯陆榆树日](https://osloelmday.no/)
* [日本榆树](https://elmjapan.org/)
* [榆树营](https://elm.camp/)

**[：顶部：回到顶部]（#目录）**

---

## 灵感来自榆树

*一些受Elm影响的项目*

* [Bolero](https://fsbolero.io/) - 使用 Elmish 在 WebAssembly 中使用 F#
* [Bucklescript-TEA](https://github.com/OvermindDL1/bucklescript-tea) - 基于 OCaml / Reason 和 [Bucklescript](https://bucklescript.github.io/) 的 Elm 架构
* [Elchemy](https://github.com/wende/elchemy) - 使用静态类型的类似 Elm 的语法编写 Elixir 代码
* [Elmish](https://github.com/elmish/elmish) - F# 应用程序的类似 Elm 的抽象
* [Fabulous](https://github.com/fsprojects/Fabulous) - F# 功能应用程序开发，使用声明式动态 UI
* [Flame](https://github.com/easafe/purescript-flame) - 一个在 PureScript 中提供 Elm 架构的库。
* [Hyperapp](https://github.com/jorgebucaran/hyperapp) - 一个用 JavaScript 提供 Elm 架构的库。
* [Iced](https://github.com/hecrj/iced) - 受 Elm 启发的 Rust 跨平台 GUI 库
* [Indigo](https://indigoengine.io/) - Indigo 是一个受 Elm 启发的 Scala.js 游戏引擎。
* [Lustre](https://github.com/lustre-labs/lustre) - 一个在 Gleam 中提供 Elm 架构的库。
* [Miso](https://github.com/dmjio/miso) - 提供 Haskell 中的 Elm 架构的库。
* [Mobius](https://github.com/spotify/mobius) - Android 应用程序的 Elm 式抽象，由 Spotify 创建。
* [React-tea-cup](https://github.com/vankeisb/react-tea-cup) - IBM 使用的一个精简库，提供 React 中的 Elm 架构。
* [Redux](https://redux.js.org/introduction/prior-art) - JavaScript 应用程序的可预测状态容器。
* [Roc](https://github.com/roc-lang/roc) - 一种针对 WebAssembly 和受 Elm 启发的机器代码的语言。
* [Sauron](https://github.com/ivanceras/sauron) - 一个库，提供 Rust 中的 Elm 架构，面向 Web。
* [SwiftUI](https://developer.apple.com/xcode/swiftui/)
* [Tyrian](https://tyrian.indigoengine.io/) - Tyrian 是一个受 Elm 启发的 Scala.js 前端框架。
* [MAUI](https://devblogs.microsoft.com/dotnet/introducing-net-multi-platform-app-ui/) - .NET 多平台应用程序 UI
* [Oolong](https://oolong-kt.org/) - 受 Elm 启发的 Kotlin 多平台模型-视图-更新 (MVU) 实现。

**[：顶部：回到顶部]（#目录）**

---

## 超越 DOM

*目前 Elm 主要针对浏览器，以下是在 DOM 之外使用 Elm 的一些实验：*

* [iOS](https://github.com/pzp1997/elm-ios) 将 Elm 0.18 用于本机 iOS 应用程序的 POC
* [elmish-wasm](https://github.com/Chadtech/elmish-wasm) 用于将 elm 编译为 Web Assembly 的 POC
* [elm-serverless](https://github.com/ktonon/elm-serverless) 使用无服务器框架在 Cloud Functions 上运行 Elm 0.18
* [elm-posix](https://github.com/albertdahlin/elm-posix) - 使用 Elm 编写 CLI 程序

**[：顶部：回到顶部]（#目录）**

---

## 更多精彩

*发现其他令人惊叹的精彩列表。*

Awesome Elm 只是 Awesome thing 的一部分，在此处获取更多信息：

- <a href="https://github.com/sindresorhus/awesome" target="_blank">太棒了</a> 作者：[**@sindresorhus**](https://github.com/sindresorhus)
- <a href="https://github.com/bayandin/awesome-awesomeness" target="_blank">awesome-awesomeness</a> 作者：[**@bayandin**](https://github.com/bayandin)


**[：顶部：回到顶部]（#目录）**

---

## 许可证

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png)](http://creativecommons.org/publicdomain/zero/1.0/)
