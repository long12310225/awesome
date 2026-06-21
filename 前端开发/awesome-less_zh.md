# 真棒少 [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

[<img src="https://cdn.rawgit.com/LucasBassetti/awesome-less/14437854/less-logo.svg"align="right"height="80">](http://lesscss.org/)

> 精彩的 Less 框架、库、风格指南、文章和资源的精选列表。主要的想法是每个人都可以在这里做出贡献，这样我们就可以集中所有关于Less的信息并保持最新。

## 内容
- [About](#about)
- [开始使用](#getting-started)
- [UI/主题框架和组件](#uitheme-frameworks-and-components)
- [库和混入](#libraries-and-mixins)
  - [Grid](#grid)
  - [媒体查询](#media-queries)
  - [Color](#color)
  - [Animation](#animation)
  - [Miscellaneous](#miscellaneous)
- [风格指南](#style-guides)
- [更少的端口](#ports-of-less)
  - [Java](#java)
  - [.Net](#net)
  - [PHP](#php)
  - [Python](#python)
  - [Ruby](#ruby)
  - [Go](#go)
- [GUI、编辑器和插件](#guis-editors-and-plugins)
- [在线Less编译器](#online-less-compilers)
- [支持较少的在线 Web IDE/游乐场](#online-web-idesplaygrounds-with-less-support)
- [Translations](#translations)
- [Articles](#articles)
- [Books](#books)
- [Videos](#videos)
- [Experiments](#experiments)
- [Community](#community)
- [Contributing](#contributing)
- [License](#license)

## 关于

Less是一种开源的动态样式表语言，可以编译成级联样式表（CSS）并在客户端或服务器端运行。 Less 由 Alexis Sellier 设计，受到 Sass 的影响，并影响了 Sass 较新的“SCSS”语法，该语法采用了类似 CSS 的块格式语法。 Less 提供了以下机制：变量、嵌套、mixin、运算符和函数； Less 和其他 CSS 预编译器之间的主要区别在于，Less 允许浏览器通过 Less 进行实时编译。字体：[维基百科](https://en.wikipedia.org/wiki/Less_(stylesheet_language))

**[返回顶部](#contents)**

## 开始使用

- [初学者指南](http://www.hongkiat.com/blog/less-basic/)
- [从更少开始](https://scotch.io/tutorials/getting-started-with-less)
- [10 分钟即可学会](http://tutorialzine.com/2015/07/learn-less-in-10-minutes-or-less/)
- [官方指南](http://lesscss.org/)
- [官方存储库](https://github.com/less/less.js)

**[返回顶部](#contents)**

## UI/主题框架和组件

- [1pxdeep](http://rriepe.github.io/1pxdeep/) - 将按相对视觉权重进行设计或使用配色方案进行设计引入 Bootstrap。
- [Ant Design](https://github.com/ant-design/ant-design/) - 企业级 UI 设计语言和基于 React 的实现。
- [Bootstrap a11y theme](https://github.com/bassjobsen/bootstrap-a11y-theme) - 使 Bootstrap 开发人员更容易访问 Web。
- [Bootstrap 3](http://getbootstrap.com/) - Bootstrap 是最流行的 HTML、CSS 和 JS 框架，用于在 Web 上开发响应式、移动优先的项目。
- [Bootswatch](http://bootswatch.com/) - Bootstrap 免费主题集合。
- [Cardinal](http://cardinalcss.com/) - 小型“移动优先”CSS 框架，适合构建响应式 Web 应用程序的前端开发人员。
- [CSSHórus](https://github.com/firminoweb/csshorus) - 用于开发响应式和移动网站的库。
- [Flat UI Free](http://designmodo.github.io/Flat-UI/) - Bootstrap 的主题和框架。
- [JBST](http://jbst.eu/) - 主题框架可用作独立的网站构建器或创建 WordPress 主题。
- [Less Rails](https://github.com/metaskills/less-rails) - Rails 则较少。
- [Material Design for Bootstrap](https://github.com/FezVrasta/bootstrap-material-design) - Material Design for Bootstrap 是 Bootstrap V3 兼容主题；这是在基于 Bootstrap 3 的应用程序中使用 Google 新材料设计指南的简单方法。
- [Metro UI CSS](http://metroui.org.ua/) - 用于创建界面类似于 Windows 8 的网站的一组样式。
- [Schema](http://danmalarkey.github.io/schema/) - 轻量级、响应式、精益的前端 UI 框架。
- [Semantic UI](http://semantic-ui.com/) - UI 组件框架基于自然语言的有用原理。
- [UIkit](https://getuikit.com/) - 用于开发 Web 界面的轻量级模块化前端框架。
- [Wee](https://www.weepower.com/) - 用于逻辑构建复杂、响应式 Web 项目的轻量级前端框架。

**[返回顶部](#contents)**

## 库和混入

### 网格

- [Bootstrap Grid Only](https://github.com/zirafa/bootstrap-grid-only) - 仅 Bootstrap 的响应式网格和响应式实用程序类，没有任何额外功能。轻巧但仍然强大。风格品味。
- [Framework](https://github.com/jonikorpi/Less-Framework) - Less Framework 是一个用于设计自适应网站的 CSS 网格系统。它包含 4 种布局和 3 组版式预设，全部基于单个网格。
- [Flexible Grid System](http://flexible.gs/) - 该框架将让您以前所未有的灵活方式创建 Web 应用程序。
- [Fluidable](http://fluidable.com/) - Fluidable 是一个移动优先、响应式网格系统。它是独立的、轻量级的并且使用 Less 构建。
- [Grid System](https://github.com/goodpixels/less-grid-system) - 超级易于使用、独立于标记的网格系统。
- [Less Zen Grid](https://github.com/bassjobsen/LESS-Zen-Grid) - 以更少的方式实现 [Zen Grids](https://github.com/JohnAlbin/zen-grids)。
- [Order.Less](https://github.com/chromice/order.less) - 基线对齐、列网格和模块化比例。

**[返回顶部](#contents)**

### 媒体查询

- [CSS and Media Query Strategies](https://github.com/buymeasoda/less-media-queries) - 使用 Less CSS 为现代和传统浏览器开发媒体查询驱动的解决方案。
- [Media Queries Library](https://github.com/mrmlnc/less-mq) - Less 中非常简单的媒体查询。
- [Media Query to Type](https://github.com/himedlooff/media-query-to-type) - 一种用于创建 IE 特定样式表的方法，该样式表允许 Internet Explorer 8 及更低版本访问媒体查询的内容。

**[返回顶部](#contents)**

### 颜色

- [Brand Colors](http://brand-colors.com/) - 1100 多种流行品牌颜色可供选择，包括 Sass、Less、Stylus 和 CSS。
- [More-Colors](http://jasonrobb.github.io/More-Colors.less/) - 当您在浏览器中进行设计时，可以使用变量更轻松地进行颜色操作。
- [Open Color](https://github.com/yeun/open-color) - 开放色是一种UI设计的配色方案。可用于 CSS、SCSS、Less、Stylus、Adobe 库、Photoshop/Illustrator 色板和 Sketch 调色板。

**[返回顶部](#contents)**

### 动画

- [Animate](https://github.com/joshuapekera/animate) - 使用 Less 创作的 CSS3 关键帧动画库。
- [Animate Less](https://github.com/machito/animate.less) - 将 Dan Eden 的 [Animate.css](https://daneden.github.io/animate.css/) 移植到 Less。
- [Cube Less](https://github.com/sparanoid/cube.less) - 仅使用 CSS（Less）的 3D（动画）立方体，最初由 LeanCloud（又名 AVOS Cloud）使用。
- [Hover](http://ianlunn.github.io/Hover/) - CSS3 驱动的悬停动画效果集合，可应用于链接、按钮、徽标、SVG、特色图像等。
- [Less Burguer](https://github.com/MarkRabey/less-burger) - [Sass Burger](http://joren.co/sass-burger/) 港口至 Less。

**[返回顶部](#contents)**

### 杂项

- [3L](http://mateuszkocz.github.io/3l/) - 混合库。
- [Bidi](https://github.com/danielkatz/less-bidi) - 用于创建双向样式的 mixin 集。
- [Clearless](http://clearleft.github.io/clearless/) - mixin 的集合。
- [Css3LessPlease](http://chrsr.com/css3lessplease/) - 将 css3please.com 转换为 Less mixins。
- [CssEffects](http://adodson.com/css-effects/) - CSS 样式效果的集合。
- [Cssowl](http://cssowl.owl-stars.com/) - 混合库。
- [Dynamic Stylesheet](https://github.com/mrkrupski/LESS-Dynamic-Stylesheet) - 一组有用的 mixin。
- [Est](https://github.com/ecomfe/est/) - 混合库。
- [Hexagon](http://db0company.github.io/css-hexagon/) - 生成具有自定义尺寸和颜色的 CSS 六边形。
- [Homeless](https://github.com/pixelass/homeless) - 有用的功能。
- [Less Elements](http://lesselements.com/) - 一组基本 mixin。
- [Lesshat](https://github.com/madebysource/lesshat) - 智能 mixins 库。
- [Lessley](https://github.com/pixelass/lessley) - 用纯 Less 编写的类似茉莉花的测试套件。
- [Lessmore](https://github.com/belyan/lessmore) - 混合库。对 CSS3 功能等的跨浏览器支持。
- [Normalize](https://github.com/segundofdez/normalize.less) - 使用 Less 模块化著名的 [normalize.css](https://github.com/necolas/normalize.css/)。
- [Oban](http://oban.io/) - mixin 的集合。
- [Preboot](https://github.com/mdo/preboot) - 用于编写更好 CSS 的 mixin 和变量的集合。
- [Retina.js](https://github.com/imulus/retinajs) - 用于渲染高分辨率图像变体的 JavaScript、SCSS、Sass、Less 和 Stylus 助手。
- [Shape](https://github.com/fahad19/shape.less) - 各种形状的 mixin 集合。
- [TRRtoolbelt](https://github.com/therebelrobot/tRRtoolbelt.less) - 常见操作的混入和函数。

**[返回顶部](#contents)**

## 风格指南

- [Handshake Style Guide](https://github.com/handshake/less-style-guide) - 本指南介绍了一系列最佳实践和编码约定。
- [WebMD Health Services Style Guide](https://github.com/bitmap/less-styleguide) - 本文档概述了 WebMD Health Services 的 CSS/Less 最佳实践。

**[返回顶部](#contents)**

## 更少的端口

### 爪哇

- [JLessC](https://github.com/i-net-software/jlessc) - Less编译器完全用Java编写。
- [Less Engine](https://github.com/Asual/lesscss-engine) - 在基于 Rhino JVM 的 JavaScript 解释器中运行较少。
- [Less CSS Compiler for Java](https://github.com/marceloverdijk/lesscss-java) - 在基于 Rhino JVM 的 JavaScript 解释器中运行较少。
- [Less4j](https://github.com/SomMeri/less4j) - 本机 Java 实现。
- [Lesscss](https://github.com/houbie/lesscss) - 使用Rhino、Nasshorn 或node.js 引擎运行较少；符合 1.7.0。
- [Lesscss Gradle Plugin](https://github.com/houbie/lesscss-gradle-plugin) - 基于Less的Gradle插件。

**[返回顶部](#contents)**

### .Net

- [BundleTransformer.Less](http://www.nuget.org/packages/BundleTransformer.Less/) - 用.Net编写的编译器。
- [Less CSS for .Net](http://www.dotlesscss.org/) - 用.Net编写的编译器。

**[返回顶部](#contents)**

### PHP

- [ILess](https://github.com/mishal/iless) - 用 Javascript 编写的 PHP 端口。
- [Lessphp](http://leafo.net/lessphp/) - 用 PHP 编写的编译器。
- [Less.php](http://lessphp.gpeasy.com/) - PHP 端口。

**[返回顶部](#contents)**

### 蟒蛇

- [Pyhton Compiler](https://github.com/lesscpy/lesscpy) - 用Python编写的编译器。

**[返回顶部](#contents)**

### 红宝石

- [Ruby Compiler](https://github.com/cowboyd/less.rb) - Ruby 的 V8 引擎中较少。

**[返回顶部](#contents)**

### 去

- [Go Compiler](https://github.com/kib357/less-go) - 在嵌入式 Javascript 引擎内运行较少。

**[返回顶部](#contents)**

## GUI、编辑器和插件

- [Atom Linter](https://github.com/josa42/atom-linter-less) - Atom 文本编辑器中的 Linter 插件。
- [CSS 2 Convert](http://css2less.co/) - 自动将 CSS 转换为 Less 的快速方法，就像复制和粘贴一样简单。
- [CSS Less(ish)](https://github.com/kizza/CSS-Less-ish) - Sublime Text 2 和 3 插件实现了 css 预处理器（例如 Less）中功能的精简版本。
- [Crunch 2!](http://getcrunch.co/) - Crunch 2 是一款具有集成编译功能的跨平台（Windows、Mac 和 Linux）编辑器。如果您处理大型 Less 项目，您绝对应该尝试一下，因为您只需要 Less 文件的免费版本。
- [Diamond](https://diamond.js.org) - 为 Sass、Less 和 CSS 构建的依赖管理。
- [Eclipse Less Plugin](http://www.normalesup.org/~simonet/soft/ow/eclipse-less.html) - 该插件通过提供方便的功能来编辑和编译 Less 样式表，从而扩展了 Eclipse IDE。
- [Eclipse Transpiler Plugin](https://github.com/gossi/eclipse-transpiler-plugin) - Eclipse 插件自动转译您的文件（Less、SASS、CoffeeScript 等）。
- [Emacs](https://github.com/purcell/less-css-mode) - 支持保存时编译的 Emacs 模式。
- [Grunt Contrib](https://github.com/gruntjs/grunt-contrib-less) - 使用 Grunt 将 Less 文件编译为 CSS。
- [Grunt Lint](https://github.com/jgable/grunt-lesslint) - 使用 Grunt 的 CSS Lint 对 Less 文件进行 Lint 处理。
- [Gulp Less](https://github.com/plus3network/gulp-less) - Gulp 插件。
- [Hayaky](https://github.com/hayaku/hayaku) - Hayaku 是一组有用的脚本，旨在快速前端 Web 开发。
- [Hyra Helper](https://github.com/Hyra/less) - CakePHP 插件，仅使用 PHP 将 Less 文件转换为 CSS。
- [Koala](http://koala-app.com/) - Koala 是一个跨平台 GUI 应用程序，用于编译 Less、sass 和 Coffeescript。
- [Less for Notepad++](https://github.com/azrafe7/LESS-for-Notepad-plusplus) - Notepad++ 的语法突出显示。
- [Less Sublime](https://github.com/danro/Less-sublime) - Sublime Text 的语法突出显示。
- [Lesshint](https://github.com/lesshint/lesshint) - 帮助您编写干净一致的 Less 的工具。
- [LiveReload](http://livereload.com/) - CSS 编辑和图像更改实时生效。 CoffeeScript、SASS、Less 等都可以正常工作。
- [SimpleLess](https://wearekiss.com/simpless) - SimpleLess 是一个简约的 Less 编译器。只需拖放并编译即可。
- [Sublime Less2CSS](https://github.com/timdouglas/sublime-less2css) - Sublime Text 2 插件，用于在保存时将 Less 文件编译为 css。
- [SublimeOnSaveBuild](https://github.com/alexnj/SublimeOnSaveBuild) - 在 Sublime Text 2 中保存文件时触发构建。最适合使用 Less、Compass 和任何其他预处理器或 makefile 的 Web 项目。
- [Vim Less](https://github.com/groenewege/vim-less) - 这个 vim 包添加了语法突出显示、缩进和自动完成功能。
- [Visual Studio Web Essentials](http://vswebessentials.com/) - 如果您曾经编写过 CSS、HTML、JavaScript、TypeScript、CoffeeScript 或 Less，那么您会发现许多有用的功能，使您作为开发人员的生活更加轻松。
- [Winless](http://lesscss.org/usage/#editors-and-plugins) - WinLess 最初是 Less.app 的克隆，它采用了功能更完整的方法并具有多种设置。它还支持以命令行参数启动。

**[返回顶部](#contents)**

## 在线Less编译器

- [BeautifyTools Less Compiler](http://beautifytools.com/less-compiler.php) - [BeautifyTools](http://beautifytools.com/) 上具有可选格式和缩小功能的在线 Less 编译器。
- [EstFiddle](http://ecomfe.github.io/est/fiddle/) - 在线Less编译器为Less和est提供现场演示。允许用户在1.4.0之后的所有Less版本之间切换，并具有可选的est/Autoprefixer功能。
- [ILess](http://demo-iless.rhcloud.com/) - [ILess](https://github.com/mishal/iless) PHP 编译器的现场演示。
- [Leafo](http://leafo.net/lessphp/editor.html) - [Lessphp](http://leafo.net/lessphp/) 现场演示。
- [Less2CSS](http://less2css.org/) - 托管在浏览器中的在线集成开发环境 (IDE)，允许用户实时编辑和编译 Less 为 CSS。
- [LessPHP](http://lessphp.gpeasy.com/demo) - [Less.php](http://lessphp.gpeasy.com/) 现场演示。
- [Lesstester](http://lesstester.com/) - Less CSS 的在线编译器。
- [Precess](http://precess.co/) - 实时预处理器编译器。
- [Winless](http://winless.org/online-less-compiler) - 这个在线Less编译器可以帮助你学习Less。您可以查看下面的示例或尝试您自己的 Less 代码。

**[返回顶部](#contents)**

## 支持较少的在线 Web IDE/游乐场

- [CodePen](http://codepen.io/) - CodePen 是网络前端的游乐场。
- [CSSDeck Labs](http://cssdeck.com/labs) - CSSDeck Labs 是一个可以快速创建一些涉及 HTML、CSS、JS 代码的实验（或测试用例）的地方。
- [Fiddle Salad](http://fiddlesalad.com/less/) - 具有即时就绪编码环境的在线游乐场。
- [JS Bin](http://jsbin.com/) - JS Bin 是一款专门设计用于帮助 JavaScript 和 CSS 测试代码片段的 Web 应用程序。
- [JsFiddle](http://jsfiddle.net/hb2rsm2x/) - 在线网页编辑器。

**[返回顶部](#contents)**

## 翻译

- [Chinese (中文)](http://lesscss.cn/)
- [Danish](http://lesscss.dk/)
- [German](http://www.lesscss.de)
- [Indonesian](http://bertzzie.com/post/7/dokumentasi-less-bahasa-indonesia)
- [Iranian](http://less-css.ir)
- [Japanese](http://less-ja.studiomohawk.com/)
- [Polish](http://ciembor.github.com/lesscss.org/)
- [Spanish](http://amatellanes.github.io/lesscss.org/)
- [Vietnamese](http://less.eten.vn/)

**[返回顶部](#contents)**

## 文章

- [Less 简介以及与 Sass 的比较](https://www.smashingmagazine.com/2011/09/an-introduction-to-less-and-comparison-to-sass/)
- [最佳 Less 教程：Less 综合指南](http://www.cssauthor.com/less-tutorials/)
- [用更少的钱做更多的事](https://medium.com/social-tables-tech/doing-more-with-less-256054d19f7d#.a41deg3dx)
- [如何用更少的 CSS 创建循环](https://medium.com/@omererkan/how-to-make-a-loops-in-less-css-d74062debef1#.snv6jqw5x)
- [让我们用更少的资源来创建更少的 CSS，而不仅仅是 CSS](https://medium.com/@zamamohammed/lets-use-lessjs-to-create-less-css-not-just-css-2d45d92a62e8#.jsocohrne)
- [少回访](https://medium.com/@ddprrt/revisiting-less-50b741bd884#.oyion811m)

**[返回顶部](#contents)**

### 书籍

- [Instant Less CSS 预处理器操作方法](https://www.packtpub.com/web-development/instant-less-css-preprocessor-how-instant)
- [更少的 Web 开发要点](http://pdf.th7.cn/down/files/1508/Less%20Web%20Development%20Essentials,%202nd%20Edition.pdf)
- [少学点](https://www.packtpub.com/web-development/learning-lessjs)

**[返回顶部](#contents)**

## 视频

- [少学点](https://www.packtpub.com/web-development/learning-less-video)
- [Less（CSS 预处理器）教程](https://www.youtube.com/watch?v=oh7_iZWvIyU&list=PLE42615v2IxlxVyGZd0rKnOzbqUtUiekE)
- [适合初学者的 CSS 教程较少](https://www.youtube.com/watch?v=YQYJUeokqOY&list=PL6gx4Cwl9DGCshbAx1JpBtNoKh8iKAAiy)
- [Less CSS - 初学者教程](https://www.youtube.com/watch?v=-D5mWO9_vLI&list=PLLa1ZAmCB2zjEZ4QNLDi4173_xIGeV6nC)

**[返回顶部](#contents)**

## 实验

- [3D按钮](https://codepen.io/MamayAlexander/pen/aAsiq)
- [边界半径混合](https://codepen.io/eky/pen/dCmnp)
- [CSS3 色轮](https://codepen.io/bitmap/pen/eBbHt)
- [演示：变量](https://codepen.io/ericrasch/pen/uGlvA)
- [简单的按钮](https://codepen.io/octavioamu/pen/zJexw)
- [线性梯度混合](https://codepen.io/eky/pen/eAnCI)
- [Navbar](https://codepen.io/lukasdietrich/pen/mkeAJ)
- [响应式网格](https://codepen.io/mecarter/pen/idKqg)
- [仅限 CSS 的大型图标](https://codepen.io/ericrasch/pen/rndaF)
- [三角形/箭头混合](https://codepen.io/eky/pen/AaCwF)
- [More...](https://codepen.io/tag/less/)

**[返回顶部](#contents)**

## 社区

- [贡献更少](https://github.com/less/less.js/blob/master/CONTRIBUTING.md)
- [Freenode](http://webchat.freenode.net/?randomnick=1&channels=%23%23lesscss)
- [Medium](https://medium.com/search?q=less%20css)
- [Quora](https://www.quora.com/topic/LESS-stylesheet-language)
- [堆栈溢出](http://stackoverflow.com/questions/tagged/less)
- [Twitter](https://twitter.com/hashtag/lesscss)

**[返回顶部](#contents)**

## 贡献

随时欢迎您的贡献！ [点击此处阅读指南](https://github.com/LucasBassetti/awesome-less/blob/master/CONTRIBUTING.md)。

**[返回顶部](#contents)**

## 许可证

[![CC0](http://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

在法律允许的范围内，[Lucas Bassetti](http://lucasbassetti.com.br) 已放弃本作品的所有版权以及相关或邻接权。

**[返回顶部](#contents)**
