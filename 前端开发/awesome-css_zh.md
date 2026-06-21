[很棒的链接]：https://github.com/sindresorhus/awesome
[真棒徽章]：https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg
[travis-link]：https://travis-ci.org/awesome-css-group/awesome-css
[travis-badge]：https://travis-ci.org/awesome-css-group/awesome-css.svg?branch=master

# 很棒的 CSS [![很棒][很棒的徽章]][很棒的链接] [![Travis 构建状态][travis-badge]][travis-link]

> /* 很棒的框架、样式指南和其他用于编写令人惊叹的 CSS 的酷块的精选列表。 */

## 简介

### 动机

本文档是一个精选的框架列表、样式指南以及用于编写出色 CSS 的精彩信息。它不包含学习 CSS 的资源。

### 补充资源

如果您遇到与 CSS 相关的问题，请在以下资源中寻找答案：

- [CSS - MDN - Mozilla](https://developer.mozilla.org/en-US/docs/Web/CSS)
- [红迪网 (CSS)](https://www.reddit.com/r/css/)
- [堆栈溢出 (CSS)](https://stackoverflow.com/questions/tagged/css)

<!-- Used for the "back to top" links within the document -->
<div id="内容"></div>

## 目录

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->


- [CSS 工作组](#css-working-group)
  - [编辑草稿：black_nib：](#editors-draft-black_nib)
- [解析器：mag：](#parsers-mag)
- [预处理器：丸：](#preprocessors-pill)
- [框架：艺术：](#frameworks-art)
- [工具包：扳手：](#toolkits-wrench)
- [重置和正常化](#reset-and-normalize)
- [大型网站的 CSS 开发](#css-development-at-large-scale-websites)
- [代码风格指南：书：](#code-style-guidelines-book)
- [风格指南](#style-guide)
- [风格指南生成器：slot_machine：](#style-guide-generators-slot_machine)
- [命名约定和方法：bulb：](#naming-conventions--methodologies-bulb)
- [JS 中的 CSS](#css-in-js)
- [CSS Polyfill](#css-polyfills)
- [Miscellaneous](#miscellaneous)
- [播客：广播：](#podcasts-radio)
- [推特：卫星：](#twitter-satellite)
- [视频：电视：](#videos-tv)
  - [2019](#2019)
  - [2016](#2016)
  - [2015](#2015)
- [书籍：书籍：](#books-books)
- [教程：拍手：](#tutorials-clapper)
- [Maintainers](#maintainers)
- [Contribute](#contribute)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## CSS 工作组

CSS 工作组创建并定义 CSS 规范。这些规范在设计过程中被分配[成熟度级别](https://www.w3.org/2005/10/Process-20051014/tr#maturity-levels)。如果您想了解更多信息，请访问 [CSS 工作组页面](https://www.w3.org/Style/CSS/)。

### 编辑草稿：black_nib：

*CSS规范的编辑草稿*

- [W3c/csswg-drafts](https://github.com/w3c/csswg-drafts) - CSS WG 编辑器草案存储库的镜像。
- [W3c/css-houdini-drafts](https://github.com/w3c/css-houdini-drafts) - Houdini WG 编辑器存储库的镜像。

## 解析器：mag：

* [CSSOM](https://github.com/NV/CSSOM) - 用纯 JavaScript 实现的 CSS 对象模型。
* [CSSTree](https://github.com/csstree/csstree) - 带有语法验证器的详细 CSS 解析器。
* [Gonzales PE](https://github.com/tonyganch/gonzales-pe) - 支持预处理器的 CSS 解析器。
* [Mensch](https://github.com/brettstimmerman/mensch) - 一个不错的 CSS 解析器。
* [ParserLib](https://github.com/CSSLint/parser-lib) - CSSLint/解析器库。
* [PostCSS](https://github.com/postcss/postcss) - 使用 JS 插件转换样式。
* [Rework](https://github.com/reworkcss/rework) - Node.js 中 CSS 预处理的插件框架。
* [Stylecow](https://github.com/stylecow/stylecow) - 适用于所有浏览器的现代 CSS。

<sub>[⇧ back to top](#contents)</sub>

## 预处理器：丸：

*更快地编写 CSS*

* [LESS](https://github.com/less/less.js) - 向后兼容 CSS，并且它添加的额外功能使用现有的 CSS 语法。
* [PostCSS](https://github.com/postcss/postcss) - 使用 JS 插件转换 CSS。
* [Sass](https://github.com/sass/sass) - 成熟、稳定、强大的专业级CSS扩展语言。
* [STYLIS](https://github.com/thysultan/stylis.js) - 轻量级 CSS 预处理器。
* [Stylus](http://learnboost.github.io/stylus/) - 专为 NodeJs 构建的富有表现力、强大且功能丰富的 CSS 语言。
* [Vanilla Extract](https://vanilla-extract.style/) - 使用 Typescript 生成静态 CSS。编写类型安全、本地范围的类、变量和主题。

<sub>[⇧ back to top](#contents)</sub>

## 框架：艺术：

* [AgnosticUI](https://www.agnosticui.com/) - 可访问的 CSS 组件原语也适用于 React、Vue 3、Svelte 和 Angular。
* [Bonsai](https://www.bonsaicss.com/) - 小于 50kb 的完整实用程序优先 CSS 框架。
* [Bootstrap](https://getbootstrap.com/) - 最流行的 HTML、CSS 和 JS 框架。
* [Bulma](http://bulma.io/) - 基于 Flexbox 的现代 CSS 框架。还可以导入 Sass 进行修改。
* [Butter Cake](http://getbuttercake.com/) - 现代轻量级前端 CSS 框架，可实现更快、更轻松的 Web 开发。
* [Charts.css](https://chartscss.org/) - CSS数据可视化框架。
* [Chota](https://jenil.github.io/chota/) - 一个响应式、可定制的微框架（3kb），带有有用的实用程序和网格系统。
* [Cirrus](https://spiderpig86.github.io/Cirrus/) - 一个完全响应式且全面的 CSS 框架，具有漂亮的控件和简单的结构。
* [Foundation](http://foundation.zurb.com/) - 先进的响应式前端框架。
* [Gralig](http://gralig.com/) - 一个朴素的、浅灰色的 CSS 库。
* [Halfmoon](https://www.gethalfmoon.com/) - 一个内置深色模式的响应式前端框架。
* [Hasser CSS](https://github.com/HeavenMercy/HasserCSS) - 一个轻量级（12k，未缩小）但有用的 CSS 框架，具有灵活的 Grid、Hero 等。
* [Inuit.css](http://inuitcss.com/) - 功能强大、可扩展、基于 Sass、BEM、OOCSS 框架。
* [Material-components-web](https://github.com/material-components/material-components-web) - 适用于 Web 的模块化和可定制的 Material Design UI 组件。
* [Materialize](http://materializecss.com/) - 基于材料设计的现代响应式前端框架。
* [Milligram](http://milligram.io) - 一个简约的 CSS 框架。
* [Numl](https://numl.design) - 基于 HTML 的语言和设计系统，可让您创建响应灵敏且可访问的具有任何外观的高质量 Web 界面。
* [Pure.css](http://purecss.io/) - 一组小型、响应式 CSS 模块，可在每个 Web 项目中使用。
* [Semantic UI](http://semantic-ui.com/) - 强大的框架，使用人性化的 HTML。
* [Shorthand Framework](https://github.com/shorthandcss/shorthand) - 新十年功能丰富的 CSS 框架。
* [Spectre.css](https://picturepan2.github.io/spectre/index.html) - 一个轻量级、响应式、现代的 CSS 框架。
* [Strawberry](https://github.com/jfet97/strawberry) - 一组常见的 Flexbox 实用程序，专注于通过嵌套 Flexbox 让您的生活变得更轻松、更快捷。
* [Tachyons](http://tachyons.io/) - 人类的函数式 CSS。
* [Tacit](https://yegor256.github.io/tacit/) - CSS 框架，适合图形设计零技能的傻瓜。
* [Tailwindcss](https://github.com/tailwindcss/tailwindcss) - 用于快速 UI 开发的实用程序优先 CSS 框架。
* [Tronic247 Material](https://material.pages.dev/) - 一个基于 CSS 和一些 JS 的响应式框架，同时遵循 Material Design 指南。
* [UIkit](http://getuikit.com/) - 一个轻量级、模块化的前端框架。
* [Unsemantic](http://unsemantic.com/) - 适用于移动设备、平板电脑和桌面设备的流体网格。
* [Wing](https://kbrsh.github.io/wing/) - 一个最小的、轻量级的、响应式的框架。

_[您可以在“awesome-css-frameworks”找到更多框架](https://github.com/troxler/awesome-css-frameworks)_

<sub>[⇧ back to top](#contents)</sub>

## 工具包：扳手：

* [Bourbon](http://bourbon.io/) - 一个简单且轻量级的 Sass mixin 库。

<sub>[⇧ back to top](#contents)</sub>

## 重置和正常化

- [CSS Checker](https://github.com/ruilisi/css-checker) - 查找并减少相似和重复的 CSS 脚本。
- [MiniReset.css](https://github.com/jgthms/minireset.css) - 一个微小的现代 CSS 重置。
- [Normalize-OpenType](https://github.com/kennethormandy/normalize-opentype.css) - 将 OpenType 功能（连字、字距调整等）添加到 Normalize.css。
- [Normalize](https://github.com/necolas/normalize.css) - 一组 CSS 规则，可在 HTML 元素的默认样式中提供更好的跨浏览器一致性。
- [Reset.css](https://meyerweb.com/eric/tools/css/reset/) - CSS 工具：重置 CSS。
- [Reseter.css](https://github.com/krishdevdb/reseter.css) - 未来派 CSS 重置/标准化器。这是重新定义而不是保留。
- [Sanitize.css](https://github.com/jonathantneal/sanitize.css/) - 一组 CSS 规则，其样式符合当今开箱即用的最佳实践。
- [Unstyle.css](https://github.com/Martin-Pitt/css-unstyle) - 用于删除用户代理样式的专用样式表，根据您的基线设计网页。

<sub>[⇧ back to top](#contents)</sub>

## 大型网站的 CSS 开发

* [Bugsnag 的 CSS 架构](http://blog.bugsnag.com/bugsnags-css-architecture) 作者：[Max Lustre](https://twitter.com/maxluster)
* [BBC Sport 的 CSS](https://medium.com/@shaunbent/css-at-bbc-sport-part-1-bab546184e66) 作者：Shaun Bent
* [CSS AT HOOTSUITE](http://code.hootsuite.com/css-at-hootsuite/) 作者：Steve Mynett
* [GitHub 的 CSS](http://markdotto.com/2014/07/23/githubs-css/) 作者：[Mark Otto](https://twitter.com/mdo)
* [我们如何在 Ghost 中使用 CSS](https://dev.ghost.org/css-at-ghost/) 作者：Paul Davis
* [孤独星球](http://ianfeather.co.uk/css-at-lonely-planet/) 作者：[Ian Feather](https://twitter.com/ianfeather)
* [Medium 的 CSS 实际上相当不错。](https://medium.com/@fat/mediums-css-is-actually-pretty-fucking-good-b8e2a6c78b06) 作者：[Jacob Thornton](https://twitter.com/fat)
* [改进我们在 Trello 构建 CSS 的方式](http://blog.trello.com/refining-the-way-we-struct-our-css-at-trello/) 作者：[Bobby Grace](https://twitter.com/bobbygrace)
* [Scalable-css-reading-list](https://github.com/davidtheclark/scalable-css-reading-list)

<sub>[⇧ back to top](#contents)</sub>

## 代码风格指南：书：

* [代码指南](http://codeguide.co/) 作者：[Mark Otto](https://twitter.com/mdo)
* [CSS 指南](http://cssguidelin.es/) 作者：[Harry Roberts](https://twitter.com/csswizardry)
* [CSS 样式指南](https://github.com/grvcoelho/css) 作者：[Guilherme Rv Coelho](https://github.com/grvcoelho)
* Dropbox 的 [Dropbox (S)CSS 样式指南](https://github.com/dropbox/css-style-guide)
* [Google HTML/CSS 样式指南](https://google.github.io/styleguide/htmlcssguide.html) 由 Google
* [惯用 CSS](https://github.com/necolas/idiomatic-css) 作者：[Nicolas Gallagher](https://twitter.com/necolas)
* [官方 Trello CSS 指南](https://gist.github.com/bobbygrace/9e961e8982f42eb91b80) 作者：Bobby Grace
* [Sass 指南](https://sass-guidelin.es/) 作者：[Kitty Giraudel](https://twitter.com/KittyGiraudel)
* Sass 团队的 [SASS 风格指南](http://sass-lang.com/styleguide)
* [ThinkUp CSS 样式指南](https://github.com/ThinkUpLLC/ThinkUp/wiki/Code-Style-Guide:-CSS) 作者：ThinkUp
* [WordPress CSS 编码标准](https://make.wordpress.org/core/handbook/best-practices/coding-standards/css/) 由 WorldPress

<sub>[⇧ back to top](#contents)</sub>

## 风格指南

* [AUI](http://docs.atlassian.com/aui/latest/docs) 由 Atlassian Design 设计
* [设计元素](http://rizzo.lonelyplanet.com/styleguide/design-elements/colours) 作者：孤独星球
* [Fluent UI](https://github.com/microsoft/fluentui) 由 Microsoft
* [GitHub CSS 样式指南](https://primer.github.io/) by Github
* [照明设计系统](https://www.lightningdesignsystem.com/) by Salesforce
* [模式](https://ux.mailchimp.com/patterns) 由 MailChimp 提供
* [Solid](http://solid.buzzfeed.com/) by BuzzFeed
*星巴克的[风格指南](https://www.starbucks.com/static/reference/styleguide/)
* [网站风格指南资源](http://styleguides.io/examples.html) 作者：Awesome people

查看更多风格指南，请访问[网站风格指南资源](http://styleguides.io/)

<sub>[⇧ back to top](#contents)</sub>


## 风格指南生成器：slot_machine：

- [Hologram](https://github.com/trulia/hologram)
- [mdcss](https://github.com/jonathantneal/mdcss)
- [Source](https://github.com/sourcejs/Source)
- [Styledoc](https://github.com/Joony/styledoc/)
- [Styledocco](https://github.com/jacobrask/styledocco)
- [Styledown](https://github.com/styledown/styledown)
- [Sc5-styleguide](https://github.com/SC5/sc5-styleguide)

<sub>[⇧ back to top](#contents)</sub>


## 命名约定和方法：bulb：

* [原子设计](http://patternlab.io/resources.html)
* [原子 OOBEMITSCSS](https://www.sitepoint.com/atomic-oobemitscss/)
* [BEM](https://en.bem.info/)
* [ITCSS](http://itcss.io/)
* [启动CSS](http://trykickoff.com/learn/css.html#namingscheme)
* [MaintainableCSS](http://maintainablecss.com)
* [NCSS](https://ncss.io)
* [OOCSS](https://www.smashingmagazine.com/2011/12/an-introduction-to-object-oriented-css-oocss/)
* [北角](http://pointnorth.io/#base-browser-styling)
* [RSCSS](https://rscss.io/)
* [套装CSS](https://github.com/suitcss/suit/blob/master/doc/naming-conventions.md#u-utilityname)
* [标题 CSS](https://www.sitepoint.com/title-css-simple-approach-css-class-naming/)

<sub>[⇧ back to top](#contents)</sub>


## JS 中的 CSS

* [Aphrodite](https://github.com/Khan/aphrodite)
* [Babel-plugin-css-in-js](https://github.com/martinandert/babel-plugin-css-in-js)
* [Classy](https://github.com/inturn/classy)
* [Csjs](https://github.com/rtsao/csjs)
* [Css-loader](https://github.com/webpack/css-loader)
* [JSS](https://github.com/cssinjs/jss)
* [React-styled](https://github.com/bloodyowl/react-styled)
* [React-with-styles](https://github.com/airbnb/react-with-styles)
* [Styled-jsx](https://github.com/zeit/styled-jsx)
* [Styled-components](https://github.com/styled-components/styled-components)
* [Stylin](https://github.com/sultan99/stylin)


这是一个[CSS in JS技术比较](https://github.com/MicheleBertoli/css-in-js)

<sub>[⇧ back to top](#contents)</sub>


## CSS Polyfill

* [Polyfill.js](https://github.com/philipwalton/polyfill/) - 一个使创建 CSS polyfill 变得更加容易的库。
* [Prefixfree](https://github.com/LeaVerou/prefixfree) - 摆脱 CSS 前缀地狱。
* [Fixed-sticky](https://github.com/filamentgroup/fixed-sticky) - CSS 位置：粘性填充。
* [Selectivizr](https://github.com/keithclark/selectivizr) - 一个 JavaScript 实用程序，可在 Internet Explorer 6-8 中模拟 CSS3 伪类和属性选择器。
* [PIE](https://github.com/lojjic/PIE) - 允许 Internet Explorer 识别并呈现各种 CSS3 框装饰属性。


<sub>[⇧ back to top](#contents)</sub>


## 各种各样的

* [Beautiful CSS box-shadow examples](https://getcssscan.com/css-box-shadow-examples) - 精选了 93 个漂亮的 CSS box-shadow 集合。点击复制。
* [Can I use](https://caniuse.com/) - 浏览器支持 CSS、HTML5 和其他前端 Web 技术。
* [Flexbox 模式](https://flexboxpatterns.com/) 作者：cjcenizal
* [Glassmorphism CSS Generator](https://ui.glass/generator/) - 为 glassmorphism 生成 CSS。
* [GradientArt](https://gra.dient.art/) - 先进的 CSS 渐变编辑器，具有分层、设计工具和免费云存储。
* [Live editor for CSS and LESS](https://github.com/webextensions/live-css-editor) - 适用于 Chrome、Firefox 和 Edge 的 Magic CSS 扩展。
* [RevengeCSS](https://github.com/Heydon/REVENGE.CSS) - 一个 CSS 书签，它使用选择器来查找不良标记，在您编写不良 HTML 的地方以漫画无衬线显示丑陋的粉红色错误消息
* [Single Div Project](https://github.com/ManrajGrover/SingleDivProject) - One `<div>`. Many possibilities.
* [You Might Not Need JS](http://youmightnotneedjs.com/) - CSS alternatives for common JS UI components.
* [Xpath-to-selector](https://github.com/steambap/xpath-to-selector) - Convert xpath to css selector.

<sub>[⇧ back to top](#contents)</sub>

## Podcasts :radio:

*Something to listen to while programming.*

* [CSS Podcast](https://thecsspodcast.libsyn.com/) - Una Kravets and Adam Argyle,and development.
* [Non Breaking Space Show](http://goodstuff.fm/nbsp) - Seeking out the best,and smartest creative people on digital art,and the accompanying blog,and UX.
* [Shop Talk Show](http://shoptalkshow.com/) - A live podcast with Chris Coyier and Dave Rupert about front-end web design,hosted by Anna Debenham and Brad Frost.
* [Style Guide Podcast](http://styleguides.io/podcast/index.html) - A small batch series of interviews on style guides,art direction,brightest,content strategy,design,Developer Advocates from Google,development,gleefully breakdown complex aspects of CSS into digestible episodes covering everything from accessibility to z-index.
* [Syntax](https://syntax.fm/) - A Tasty Treats Podcast for Web Developers.,typography,web technology
* [The Big Web Show](http://5by5.tv/bigwebshow/) - Topics like web publishing,is all about keeping you updated with the latest in Open Source Technology.
* [The Changelog](https://changelog.com/) - The tagline for the Changelog says it all: “Open Source moves fast. Keep up.” This podcast,and more. It's everything web that matters.
* [The Web Ahead](http://5by5.tv/webahead/) - Conversations with world experts on changing technologies and future of the web.

<sub>[⇧ back to top](#contents)</sub>


## Twitter :satellite:

*Active accounts to follow.*

* [Adam Morse](https://twitter.com/mrmrs_) - Advocate for users and open-source.
* [Andrey Sitnik](https://twitter.com/andreysitnik) - Author of @Autoprefixer, http://easings.net  and @PostCSS.
* [Ben Briggs](https://twitter.com/ben_eb) - Final year web technologies student. node.js, javascript, open source modules, client side optimisation, web performance.
* [Brad Frost](https://twitter.com/brad_frost) - Web designer, speaker, writer, consultant, musician.
* [Chris Coyier](https://twitter.com/chriscoyier) - Designer @CodePen. Writer @Real_CSS_Tricks.
* [Connor Sears](https://twitter.com/connors) - Designer at GitHub.
* [CSS Animation](https://twitter.com/cssanimation)
* [CSS Commits](https://twitter.com/CSScommits) - Latest commits to @CSSWG’s public Mercurial repository.
* [Daniel Glazman](https://twitter.com/glazou) - W3C CSS Working Group Co-chairman, entrepreneur, software engineer, geek, father of two, polyglot, duck lover. Nah. Tweets are strictly mine.
* [Dave McFarland](https://twitter.com/davemcfarland) - Web developer, author of CSS: The Missing Manual, JavaScript & jQuery.
* [Donovan Hutchinson](https://twitter.com/donovanh) - Designer, developer, writer. Occasionally blogs at http://Hop.ie, and currently building @cssanimation.
* [Dudley Storey](https://twitter.com/dudleystorey) - Web development writer, teacher, and speaker.
* [Eric Bidelman](https://twitter.com/ebidel) - Engineer at Google working on Chrome, web components, and Polymer.
* [Evangelina Ferreira](https://twitter.com/evaferreira92) - Web Designer. Professor at @multimedial_utn HTML5 & CSS Freak. Ocassional Translator.
* [Guy Routledge](https://twitter.com/guyroutledge) - Front-end dev, Teacher @GA_London, Screencaster at http://www.atozcss.com, property snob, Foodie.
* [Harry Roberts](https://twitter.com/csswizardry)- Consultant Front-end Architect: @google, @Etsy, @kickstarter, @BBC, @Deloitte, @FT, more.
* [Heydon Pickering](https://twitter.com/heydonworks) - Moderate consumer of rice. Also a UX designer, author, @smashingmag editor and programmer.
* [Jonathan Snook](https://twitter.com/snookca) - Designer, Developer, Writer, Speaker. I make stuff on the web. I wrote SMACSS.
* [Kitty Giraudel](https://twitter.com/KittyGiraudel) - Non-binary accessibility & diversity advocate, frontend developer, author.
* [L. David Baron](https://twitter.com/davidbaron) - Mozilla developer, CSS and W3C standards diplomat.
* [Lea Verou](https://twitter.com/LeaVerou) - Research Assistant @MIT_CSAIL, @CSSWG IE, @OReillyMedia author, Ex @W3C staff.
* [Manoela Ilic](https://twitter.com/crnacura) - ...aka Mary Lou @codrops ༶ CSS & HTML are my crayons ༶ Interested in Cognitive Science, AI, HCI, UI Design & Astrophysics ༶ Digital nomad.
* [Mark Otto](https://twitter.com/mdo) - GitHub and Bootstrap. Formerly at Twitter. Huge nerd.
* [Maxime Thirouin](https://twitter.com/MoOx) - Freelance front-end vigilante, UI/UX developer.
* [Natalie Weizenbaum](https://twitter.com/nex3) - Trans coder lady. Lead designer/developer of @SassCSS, working for @google on @dart_lang.
* [Nicolas Gallagher](https://twitter.com/necolas) - Software Engineer at @twitter.
* [Nicole Sullivan](https://twitter.com/stubbornella) - GEEK.
* [Patrick Hamann](https://twitter.com/patrickhamann) - Lover of mountains, craft beers and discovering new food.
* [Paul Lewis](https://twitter.com/aerotwist) - Googler who noodles with code and design.
* [Phil Walton](https://twitter.com/philwalton) - Engineer at Google • Open Source Advocate • Developer • Designer • Writer.
* [Rachel Andrew](https://twitter.com/rachelandrew) - Web Developer, half of @grabaperch CMS, CSS Working Group Invited Expert.
* [Remy Sharp](https://twitter.com/rem) - All about CSS sizing units.
* [Sara Soueidan](https://twitter.com/SaraSoueidan) - Author of the @Codrops CSS Reference & Co-author of the Smashing Book #5.
* [Scott Jehl](https://twitter.com/scottjehl) - Author of @responsiblerwd, now on sale from @abookapart.
* [Simon](https://twitter.com/simurai) - UI designer, CSS doodler.
* [The Chris Eppstein](https://twitter.com/chriseppstein) - Loves love. Hates hate. Has a kick-ass family. Writes code. Leads stylesheet tech @LinkedIn.
* [Una Kravets](https://twitter.com/Una) - Front-end @IBMDesign. Sassvocate, community builder, & handcrafter. STEMinist :) Open source all the things.
* [Zoe M. Gillenwater](https://twitter.com/zomigi) - Web designer/developer specializing in CSS, RWD, UX, & accessibility.
* [Zoltán Szőgyényi](https://twitter.com/zoltanszogyenyi) - Web developer, Co-founder at Themesberg. I'm building Glass UI.
* [앗킨스 탭](https://twitter.com/tabatkins) - Literally Jenn Schiffer's Mom.

<sub>[⇧ back to top](#contents)</sub>


## Videos :tv:

*Good study videos from CSS Must Watch Videos. Some items are quoted from [AllThingsSmitty/must-watch-css](https://github.com/AllThingsSmitty/must-watch-css).

[I told him on Twitter](https://twitter.com/sota0805/status/527635856031375360). I appreciate his valuable efforts.*

### 2019

1. [Next-Generation Web Styling](https://www.youtube.com/watch?v=-oyeaIirVC0) - Una Kravets & Adam Argyle @ Chrome Dev Summit 2019.

### 2016

1. [Component-Based Style Reuse](https://www.youtube.com/watch?v=_70Yp8KPXH8) :page_facing_up: [transcript](https://2016.cssconf.com/) :watch: `37:24` - Pete Hunt @ CSS conf 2016.
1. [CSS4 Grid: True Layout Finally Arrives](https://www.youtube.com/watch?v=jl164y-Vb5E) :page_facing_up: [transcript](https://2016.cssconf.com/) :watch: `29:27` - Jen Kramer @ CSS conf 2016.
1. [Houdini: Demystifying the Future of CSS](https://www.youtube.com/watch?v=sE3ttkP15f8) :watch: `36:58` @ Google I/O 2016.

### 2015

1. [Mdo-ular CSS](http://jqueryuk.com/2015/videos.php?s=mdo-ular-css) :watch: `30:06` - Mark Otto @ jQuery UK.
1. [CSS Architecture with SMACSS](https://www.youtube.com/watch?v=6co781JgoqQ) :watch: `30:15` - Caleb Meredith @ DevTips channel.
1. [CSS Workflow from the Ground Up](https://www.youtube.com/watch?v=ZVk3GQHfkbU) :watch: `46:06` - Jonathan Snook @ Generate conf 2015.

<sub>[⇧ back to top](#contents)</sub>

## Books :books:

* [CSS: The Definitive Guide, 4th Edition](http://shop.oreilly.com/product/0636920012726.do)  - Visual Presentation for the Web
* [CSS: The Missing Manual](http://shop.oreilly.com/product/0636920036357.do) – Really Helpful in Advancing your Design Skills to a whole new Level
* [CSS Secrets](http://shop.oreilly.com/product/0636920031123.do) – Better Solutions to Everyday Web Design Problems
* [Every Layout: Relearn CSS Layout](https://every-layout.dev/) – Solving responsive layout problems using algorithmic design.
* [Tiny CSS Projects](https://www.manning.com/books/tiny-css-projects) – Improve the way you write CSS as you build 12 tiny projects.

<sub>[⇧ back to top](#contents)</sub>

## Tutorials :clapper:

* [30 Seconds of CSS](https://www.30secondsofcode.org/css/p/1) -  A curated collection of useful CSS snippets you can understand in 30 seconds or less.
* [All selectors in CSS](https://medium.com/@ymzEmre/css-cascade-specificity-basic-selectors-c5adc01dd861) - All selectors in CSS.
* [Community Curated CSS Resources](https://hackr.io/tutorials/learn-css) - Top Recommended Resources.
* [CSS Diner](https://flukeout.github.io/) – Interactive gamified tutorial for learning selection with CSS.
* [CSS Grid PlayGround](https://mozilladevelopers.github.io/playground/) - Simple tutorial to learn CSS Grid from Mozilla.
* [CSS Grids videos tutorial](https://cssgrid.io/) - Free video course by Wes Bos to learn CSS Grids.
* [CSS Hands-on Tutorial](https://labex.io/tutorials/quick-start-with-css-free-tutorials-413795) - Free CSS hands-on tutorial by LabEx.
* [CSS Math Functions](https://stackdiary.com/css-math-functions/) - Using CSS Math for responsive design.
* [Flexbox video tutorial](https://flexbox.io/) - Free video course by Wes Bos to learn flexbox.
* [Organize CSS with a Modular Architecture: OOCSS, BEM, SMACSS](https://snipcart.com/blog/organize-css-modular-architecture) - In-depth intro to OOCSS, BEM, SMACSS, with examples.
* [Work With Animations](https://developer.mozilla.org/en-US/docs/Tools/Page_Inspector/How_to/Work_with_animations) - Inspecting animations.

<sub>[⇧ back to top](#contents)</sub>

## Maintainers

[sotayamashita]: https://github.com/sotayamashita
[Rishabh04-02]:  https://github.com/Rishabh04-02

[@sotayamashita][sotayamashita], [@Rishabh04-02][Rishabh04-02] and You!


## Contribute

[contributor-covenant]: https://www.contributor-covenant.org/version/1/3/0/code-of-conduct/

Feel free to dive in! Open an issue or submit PRs.

Awesome CSS follows the [Contributor Covenant][contributor-covenant] Code of Conduct.
