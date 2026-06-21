![Awesome Sass](https://raw.githubusercontent.com/Famolus/awesome-sass/master/awesome-sass-logo-github.png)

# 很棒的萨斯 [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

> 精彩的 [Sass](http://sass-lang.com/) 和 [SCSS](http://sass-lang.com/) 框架、库、风格指南、文章和资源的精选列表。

- 使用<kbd>command</kbd> + <kbd>F</kbd>或<kbd>ctrl</kbd> + <kbd>F</kbd>搜索关键字。
- 欢迎贡献，请参阅[贡献指南](contributing.md)。

## 内容
- [About](#about)
- [开始使用](#getting-started)
- [Sass 与 SCSS](#sass-vs-scss)
- [Frameworks](#frameworks)
- [库和混入](#libraries-and-mixins)
  - [Grid](#grid)
  - [媒体查询](#media-queries)
  - [Color](#color)
  - [Typography](#typography)
  - [Animation](#animation)
  - [Miscellaneous](#miscellaneous)
- [风格指南](#style-guides)
- [Articles](#articles)
- [Tools](#tools)
- [Books](#books)
- [Videos](#videos)
- [Community](#community)

## 关于
[Sass](http://sass-lang.com/) 是 CSS 的扩展，为基本语言增添了力量和优雅。它允许您使用变量、嵌套规则、混合、内联导入等，所有这些都具有完全 CSS 兼容的语法。 Sass 有助于保持大型样式表组织良好，并快速启动和运行小型样式表。

Sass 有两种语法。新的主要语法（从 Sass 3 开始）称为“SCSS”（“Sassy CSS”），是 CSS 语法的超集。这意味着每个有效的 CSS 样式表也是有效的 SCSS。 SCSS 文件使用扩展名“.scss”。

第二种较旧的语法称为缩进语法（或简称“Sass”）。受到 Haml 简洁性的启发，它面向那些喜欢简洁性而不是 CSS 相似性的人。它不使用括号和分号，而是使用行缩进来指定块。尽管不再是主要语法，但缩进语法将继续受到支持。缩进语法中的文件使用扩展名“.sass”。

## 开始使用
- [Official Sass and SCSS Guide](http://sass-lang.com/guide) - 官方 Sass 和 SCSS 指南。
- [Tutorialzine](http://tutorialzine.com/2016/01/learn-sass-in-15-minutes/) - 15 分钟教程学习 SASS。
- [Codecademy](https://www.codecademy.com/learn/learn-sass) - 通过 Codecademy 学习 Sass。
- [Lynda](https://www.lynda.com/SASS-training-tutorials/1435-0.html) - 通过行业专家教授的在线视频教程，了解如何使用 Sass，从初学者基础知识到高级技术。
- [Official Sass and SCSS Reference](http://sass-lang.com/documentation/file.SASS_REFERENCE.html) - 官方 Sass 和 SCSS 文档参考。
- [SitePoint Sass and SCSS Reference](https://www.sitepoint.com/sass-reference/) - SitePoint Sass 和 SCSS 参考。

## Sass 与 SCSS
- [SitePoint](https://www.sitepoint.com/whats-difference-sass-scss/) - Sass 和 SCSS 有什么区别？
- [The Sass Way](http://thesassway.com/editorial/sass-vs-scss-which-syntax-is-better) - 哪种语法更好？
- [Stack Overflow](http://stackoverflow.com/questions/5654447/whats-the-difference-between-scss-and-sass) - SCSS 和 Sass 有什么区别？

## 框架
- [avalanche](https://avalanche.oberlehner.net) - 用于构建基于包的 CSS 工作流程基础的框架。
- [Bootstrap 4](https://github.com/twbs/bootstrap) - Bootstrap 版本 4，最流行的 HTML、CSS 和 JS 框架，用于在 Web 上开发响应式、移动优先的项目。
- [Bootstrap-sass](https://github.com/twbs/bootstrap-sass) - Bootstrap 2 和 3 的官方 Sass 移植。
- [Bulma](https://github.com/jgthms/bulma) - 基于 Flexbox 的现代 CSS 框架。
- [Cirrus](https://github.com/Spiderpig86/Cirrus) - 一个以组件和实用程序为中心的 SCSS 框架，专为快速原型设计而设计。
- [Foundation for Sites](https://github.com/zurb/foundation-sites) - 世界上最先进的响应式前端框架。为在任何类型的设备上运行的网站快速创建原型和生产代码。
- [Hocus-Pocus](https://bkzl.github.io/hocus-pocus/) - 通用且轻量级的样式表入门套件，专注于基本 html 元素和版式。
- [iotaCSS](https://www.iotacss.com) - 专为扩展而构建的基于 Sass 的开源 OOCSS 框架。
- [Kickoff](http://trykickoff.com) - Kickoff 是一个轻量级前端框架，用于创建可扩展、高性能和响应灵敏的站点。
- [Materialize](http://materializecss.com) - 基于材料设计的现代响应式前端框架。
- [mini.css](http://minicss.org/) - 最小的、响应式的、与样式无关的 CSS 框架。
- [Scooter](http://dropbox.github.io/scooter/) - SCSS 框架旨在为 Dropbox 提供基本样式、CSS 组件和快速静态原型。
- [Sierra](http://sierra-library.github.io/) - Micro SCSS 库可帮助您构建网站，而无需所有任意选择器。

## 库和混入

### 网格
- [Avalanche](http://colourgarden.net/avalanche) - 轻量级、响应式、基于 Sass、BEM 语法的网格系统。
- [csswizardry-grids](http://csswizardry.com/csswizardry-grids/) - 简单、流畅、可嵌套、灵活、基于 Sass 的响应式网格系统。
- [Griddle](http://necolas.github.io/griddle/) - 极其灵活的 CSS 网格构造函数。
- [Gridlex](http://gridlex.devlint.fr/) - Flexbox 网格系统。
- [Jeet](https://github.com/mojotech/jeet) - Sass 和 Stylus 的简单分数网格系统。
- [Neat](http://neat.bourbon.io/) - 使用 Sass 构建的轻量级语义网格框架。
- [Sass Flexible Grid System](https://dnomak.com/flexiblegs/install/sass/) - Sass 灵活的网格系统。
- [SCSS Flexible Grid System](https://dnomak.com/flexiblegs/install/scss/) - SCSS灵活的网格系统。
- [Susy](https://github.com/oddbird/susy) - Sass 的响应式布局工具包。
- [Toast](http://daneden.github.io/Toast/) - 来自 [animate.css](https://daneden.github.io/animate.css/) 创建者的灵活且轻量级的网格框架。
- [Waffle Grid](https://lucasgruwez.github.io/waffle-grid/) - 易于使用的 Flexbox 网格系统。

### 媒体查询
- [Breakpoint](https://github.com/at-import/breakpoint) - 断点使得在 Sass 中编写媒体查询变得非常简单。
- [include-media](https://eduardoboucas.github.io/include-media/) - 简单、优雅且可维护的媒体查询。
- [mq-scss](https://github.com/Dan503/mq-scss) - 一个极其强大但易于使用的 Sass 媒体查询 mixin。
- [Sass MediaQueries](http://rafalbromirski.github.io/sass-mediaqueries/) - 适用于 Sass 的有用媒体查询混合集合（包括 iOS 设备、电视等）。
- [Sass MQ](https://github.com/sass-mq/sass-mq) - Sass mixin 可帮助您以优雅的方式编写媒体查询。

### 颜色
- [brand-colors](http://brand-colors.com/) - 1100 多种流行品牌颜色可供选择，包括 Sass、Less、Stylus 和 CSS。
- [Open color](https://github.com/yeun/open-color) - 开放色是一种UI设计的配色方案。可用于 CSS、SCSS、LESS、Stylus、Adobe 库、Photoshop/Illustrator 色板和 Sketch 调色板。
- [sass-planifolia](https://github.com/xi/sass-planifolia) - vanilla Sass 中的高级颜色操作和对比度计算。
- [scss-blend-modes](https://github.com/heygrady/scss-blend-modes) - 使用 Sass 中的标准颜色混合函数。

### 版式
- [Sassline](https://sassline.com/) - 使用响应式模块化比例，使用 Sass 和 rems 将 Web 上的文本设置为基线网格。
- [Sassy-Gridlover](https://github.com/hiulit/Sassy-Gridlover) - 超级容易使用 Sass mixins 来建立具有模块化比例和垂直节奏的排版系统。基于 Gridlover 应用程序。
- [Shevy](http://kyleshevlin.github.io/shevy/) - 排版变得简单。垂直节奏库。
- [Typi](https://github.com/zellwk/typi) - Sass mixin 使响应式排版变得简单。

### 动画
- [Animate.scss](https://github.com/geoffgraham/animate.scss) - Dan Eden 的 SASS 的 [Animate.css](https://daneden.github.io/animate.css/) 端口。
- [Hover](http://ianlunn.github.io/Hover/) - CSS3 驱动的悬停动画效果集合，可应用于链接、按钮、徽标、SVG、特色图像等。可用于 CSS、Sass 和 LESS。
- [Kf](https://kf-sass.com) - Sass mixin 库，用于从地图创建基于关键帧的动画。
- [Sass Burger](https://github.com/jorenvanhee/sass-burger) - 用于创建动画汉堡图标的 Sass mixin。
- [SpinThatShit](https://matejkustec.github.io/SpinThatShit/) - 用于单元素加载器和旋转器的 SCSS mixin 集。

### 杂项
- [Angled Edges](https://github.com/josephfusco/angled-edges) - Sass mixin 用于通过动态编码 SVG 在部分上创建有角度的边缘。
- [Bourbon](http://bourbon.io/) - Sass 的简单轻量级 mixin 库。
- [Buttono](https://github.com/hsnaydd/buttono) - 一个灵活的 Sass mixin，用于创建 BEM 风格的按钮。
- [Buttons](https://github.com/alexwolfe/Buttons) - 使用 Sass 和 Compass 构建的 CSS 按钮库。
- [csstyle](https://csstyle.io) - 一个 SCSS 库，可帮助您构建模块化 CSS，为您生成选择器并自动处理特殊性。
- [Family.scss](http://lukyvj.github.io/family.scss/) - 26 个智能 Sass mixin 集，将帮助您以简单而优雅的方式管理 :nth-child'ified 元素的样式。
- [Gerillass](https://gerillass.com/) - 一个 Sass mixin 库，可帮助您创建现代网站。
- [Juice](http://kylebrumm.com/juice/) - Sass mixin 和函数的集合。
- [Modular Scale](https://github.com/modularscale/modularscale-sass) - Sass 中内置的模块化比例计算器。
- [normalize-scss](https://github.com/JohnAlbin/normalize-scss) - Normalize.css 的 Sass/Compass 版本，是 HTML 元素和属性规则集的集合，用于规范所有浏览器中的样式。
- [Pretty checkbox](https://github.com/lokesh-coder/pretty-checkbox) - 用于美化复选框和单选按钮的 SCSS/CSS 库。
- [retina.js](https://github.com/imulus/retinajs) - 用于渲染高分辨率图像变体的 JavaScript、SCSS、Sass、Less 和 Stylus 助手。
- [Sass Accoutrement](http://oddbird.net/open-source/accoutrement/) - Accoutrement 模块是 Sass 工具包，它们协同工作以形成项目的中心配置。这些工具可以单独使用，也可以集成使用以获得额外的功能。
- [Sass Deprecate](https://github.com/salesforce-ux/sass-deprecate) - Sass mixin 有助于管理代码弃用。
- [Sass flexbox mixin](https://github.com/mastastealth/sass-flex-mixin) - 为那些想要使用当前浏览器的本机支持来摆弄 Flexbox 的人提供的 Mixin 集。
- [Sassdash](https://github.com/davidkpiano/sassdash) - lodash 的 Sass 实现（[API 文档](http://davidkpiano.github.io/sassdash)）。
- [Scut](https://github.com/davidtheclark/scut) - Sass 实用程序的集合，用于简化和改进常见样式代码模式的实现。

## 风格指南
- [Hugo Giraudel's Sass Guidelines](https://sass-guidelin.es/) - 编写健全、可维护和可扩展的 Sass 的指南。
- [BigCommerce Sass Coding Guidelines](https://github.com/bigcommerce/sass-style-guide) - BigCommerce 使用指南。
- [Airbnb Sass and CSS Style Guide](https://github.com/airbnb/css) - Airbnb 的 Sass 和 CSS 风格指南。
- [Dropbox (S)CSS Style Guide](https://github.com/dropbox/css-style-guide) - Dropbox 的 (S)CSS 创作风格指南。

## 文章
- [Hugo Giraudel Personal Awesome Sass List](https://github.com/HugoGiraudel/awesome-sass) - Hugo Giraudel 在 Sass 上的作品记录。
- [Sass 中的三次贝塞尔曲线表示](http://thesassway.com/advanced/cubic-bezier-representation-in-sass)
- [使用 Webpack 构建更快的 Sass](http://eng.localytics.com/faster-sass-builds-with-webpack/)
- [大规模过渡到 SCSS](https://codeascraft.com/2015/02/02/transitioning-to-scss-at-scale/)
- [Sass 映射到 UI 组件](https://blog.prototypr.io/sass-maps-to-ui-components-f14e1f34412e#.9zt0s0rxt)
- [Sass 的反三角函数](http://thesassway.com/advanced/inverse-trigonometric-functions-with-sass)
- [别再与你的 Mixin 争论太多了](http://sassbreak.com/stop-arguing-with-your-mixins)
- [在 Sass 中设置 React 组件的样式](http://hugogiraudel.com/2015/06/18/styling-react-components-in-sass/)
- [Sass !default 用例](https://robots.thoughtbot.com/sass-default)
- [美学 Sass 3：版式和垂直节奏](https://scotch.io/tutorials/aesthetic-sass-3-typography-and-vertical-rhythm)
- [CSS 和 Sass 精度的故事](https://www.sitepoint.com/a-tale-of-css-and-sass-precision/)
- [直接从 Sass 构建风格指南](https://css-tricks.com/build-style-guide-straight-sass/)
- [高级 SCSS，或者您可能不知道样式表可以做的 16 件很酷的事情](https://gist.github.com/jareware/4738651)
- [可持续 SCSS 的 80-20 方法](https://zendev.com/2018/05/30/the-80-20-approach-to-sustainable-scss.html)
- [Sass 映射的高级使用](https://itnext.io/advanced-use-of-sass-maps-bd5a47ca0d1a)

## 工具
- [dart-sass](https://github.com/sass/dart-sass) - Sass 的 Dart 实现。
- [diamond](https://diamond.js.org) - 为 Sass、Less 和 CSS 构建的依赖管理。
- [libsass-python](https://github.com/dahlia/libsass-python) - Python 的 libsass 绑定。
- [libsass](https://github.com/sass/libsass) - Sass 编译器的 C/C++ 实现。
- [node-sass-magic-importer](https://github.com/maoberlehner/node-sass-magic-importer) - 自定义 node-sass 导入器，用于选择器特定导入、节点导入、模块导入、全局支持和仅导入文件一次。
- [node-sass](https://github.com/sass/node-sass) - Node.js 与 libsass 的绑定。
- [OctoLinker](https://github.com/OctoLinker/browser-extension) - 使用 GitHub 的 OctoLinker 浏览器扩展有效地浏览 *.scss 和 *.sass 文件。
- [sass-extract](https://github.com/jgranstrom/sass-extract) - 从 scss 文件中提取变量。通过将计算样式提取到 js 对象中，使用 scss 来描述在 javascript 中使用的样式。支持导入和高级语言功能。
- [sass-loader](https://github.com/jtangelder/sass-loader) - Webpack 的 Sass 加载器。
- [sass-rails](https://github.com/rails/sass-rails) - Sass 的 Ruby on Rails 样式表引擎。
- [SassDoc](http://sassdoc.com/) - 文档系统（如 JavaScript 的 JSDoc）可在眨眼间构建漂亮且功能强大的文档。
- [Scout-App](http://scout-app.io/) - 将 Sass 和 SCSS 文件处理为 CSS，无需任何命令行知识。
- [scss-lint](https://github.com/brigade/scss-lint) - 用于编写干净且一致的 SCSS 的可配置工具。 [（已弃用）](https://github.com/brigade/scss-lint#notice-consider-other-tools-before-adopting-scss-lint)
- [SharpScss](https://github.com/xoofx/SharpScss) - P/Invoke libsass 周围的 .NET 包装器，将 SCSS 转换为支持 NET2.0/NET3.5/NET4.x+ 和 CoreCLR 平台的 CSS。
- [stylelint](https://stylelint.io/) - 一个强大的、现代的 CSS linter，可以帮助您强制执行一致的约定并避免样式表中的错误。支持类似 CSS 的语法，包括 SCSS。

## 书籍
- [现实世界中的 Sass：第一卷第四卷](https://anotheruiguy.gitbooks.io/sassintherealworld_book-i/content/)
- [现实世界中的 Sass：第二卷第四卷](https://anotheruiguy.gitbooks.io/sass-in-the-real-world-book-2-of-4/content/)
- [快速入门 Sass：在周末快速掌握 Sass](https://www.amazon.com/Jump-Start-Sass-Speed-Weekend/dp/0994182678)
- [面向设计师的 Sass 和 Compass](https://www.amazon.com/Sass-Compass-Designers-Ben-Frain/dp/1849694540)

## 视频
- [Sass 教程](https://www.youtube.com/watch?v=wz3kElLbEHE)
- [系列 Sass 教程展示了安装、基础知识和使用关键功能](https://www.youtube.com/playlist?list=PL2CB1F80266E986EA)
- [Sass 还是 LESS？你应该使用什么？](https://www.youtube.com/watch?v=lJclQekSfSM)
- [在此免费速成课程中学习 Sass - 赋予您的 CSS 超能力！](https://www.youtube.com/watch?v=roywYSEPSvc)
- [Net Ninja Sass 播放列表](https://www.youtube.com/watch?v=St5B7hnMLjg&list=PL4cUxeGkcC9iEwigam3gTjU_7IA3W2WZA)

## 社区
- [Reddit](https://www.reddit.com/r/Sass/)
- [堆栈溢出](http://stackoverflow.com/questions/tagged/sass)
- [Twitter 上的@SassCSS](https://twitter.com/SassCSS)

## 许可证
[![CC0](http://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)
