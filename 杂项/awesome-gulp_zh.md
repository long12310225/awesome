# 令人敬畏的咕噜声 [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

> 精选的 [gulp](https://github.com/gulpjs/gulp) 资源、插件和样板列表，以实现更好的开发工作流程自动化。

_还在寻找其他东西吗？看看其他[很棒的列表](https://github.com/sindresorhus/awesome)._

## 贡献

:octocat：欢迎所有贡献。请随意贡献（[指南](contributing.md)）。

## 内容

- [Legend](#legend)
- [Resources](#resources)
  - [一般资源](#general-resources)
  - [官方文档](#official-documentation)
  - [Community](#community)
  - [Tutorials](#tutorials)
    - [吞咽教程](#gulp-tutorials)
    - [Gulp 4 教程](#gulp-4-tutorials)
    - [使用 Browserify 吞咽](#gulp-with-browserify)
    - [Gulp 与 Angular](#gulp-with-browserify)
    - [Gulp 与 Angular 和 Browserify](#gulp-with-angular-and-browserify)
    - [Gulp 与 Angular 和 Webpack](#gulp-with-angular-and-webpack)
    - [Gulp 与 React 和 Browserify](#gulp-with-react-and-browserify)
    - [吞下 Ember](#gulp-with-ember)
  - [杂项资源](#miscellaneous-resources)
- [Plugins](#plugins)
  - [Compilation](#compilation)
  - [Transpilation](#transpilation)
  - [Concatenation](#concatenation)
  - [Minification](#minification)
  - [Optimization](#optimization)
  - [注入资产](#injecting-assets)
  - [Templating](#templating)
  - [Linting](#linting)
  - [实时重新加载](#live-reload)
  - [Caching](#caching)
  - [流量控制](#flow-control)
  - [Logging](#logging)
  - [Testing](#testing)
  - [杂项插件](#miscellaneous-plugins)
- [Scaffolding](#scaffolding)
  - [Boilerplates](#boilerplates)
  - [自耕农发电机](#yeoman-generators)
- [Miscellaneous](#miscellaneous)

## 传奇

[:no_entry:] - 弃用通知；

## 资源

### 一般资源

- [官方网站](http://gulpjs.com/)
- [Github 存储库](https://github.com/gulpjs/gulp)
- [插件注册表](http://gulpjs.com/plugins/)
- [NPM模块](https://www.npmjs.com/package/gulp)
- [列入黑名单的插件](https://github.com/gulpjs/plugins/blob/master/src/blackList.json)

### 官方文档

- [开始使用](https://github.com/gulpjs/gulp/blob/master/docs/getting-started.md)
- [API文档](https://github.com/gulpjs/gulp/blob/master/docs/API.md)
- [CLI 文档](https://github.com/gulpjs/gulp/tree/master/docs#articles)
- [编写插件](https://github.com/gulpjs/gulp/blob/master/docs/writing-a-plugin/README.md)
- [Recipes](https://github.com/gulpjs/gulp/tree/master/docs/recipes)

### 社区

- [StackOverflow](http://stackoverflow.com/questions/tagged/gulp)
- [Twitter](https://twitter.com/gulpjs)

### 教程

#### 吞咽教程

- [用 Gulp 构建](https://www.smashingmagazine.com/2014/06/building-with-gulp/)
- [使用 Gulp.js 轻松自动化您的任务](https://scotch.io/tutorials/automate-your-tasks-easily-with-gulp-js)
- [Gulp - 项目的愿景、历史和未来](https://medium.com/@contrahacks/gulp-3828e8126466)
- [Gulp.js 简介](http://stefanimhoff.de/tag/gulp/)
- [视频：学习 Gulp](http://leveluptuts.com/tutorials/learning-gulp)
- [使用 Gulp 将脚本和样式标签直接注入 HTML](http://blog.johnnyreilly.com/2015/02/using-gulp-in-asp-net-instead-of-web-optimization.html)
- [使用 Gulp.js 的 5 个经验教训](http://denbuzze.com/post/5-lessons-learned-using-gulpjs/)
- [自动化链接：我如何学会停止担忧并热爱构建](http://conan.is/bower/gulp/wiredep/javascript/2014/08/18/automating_linkage-or-how-i-learned-to-stop-worrying-and-love-the-build.html)
- [首次设置 Gulp 任务](https://www.codementor.io/development-process/tutorial/how-to-set-up-gulp-beginner-guide#/)
- [为什么你不应该创建 Gulp 插件（或者，如何停止担忧并学会喜欢现有的 Node 包）](http://blog.overzealous.com/post/74121048393/why-you-shouldnt-create-a-gulp-plugin-or-how-to)
- [您现在可以使用 6 个 Gulp 最佳实践来从根本上改善您的开发体验](http://blog.rangle.io/angular-gulp-bestpractices/)
- [适合初学者的 Gulp](https://css-tricks.com/gulp-for-beginners/)

#### Gulp 4 教程

- [通过示例迁移到 Gulp 4](https://blog.wearewizards.io/migrating-to-gulp-4-by-example)
- [Gulp 4：新的任务执行系统 - gulp.parallel 和 gulp.series](http://fettblog.eu/gulp-4-parallel-and-series/)

#### 使用 Browserify 吞咽

- [Gulp + Browserify，Gulp-y 方式](https://medium.com/@sogko/gulp-browserify-the-gulp-y-way-bb359b3f9623)
- [Gulp + 浏览器化](https://viget.com/extend/gulp-browserify-starter-faq)
- [使用 Watchify 快速构建 Browserify](https://github.com/gulpjs/gulp/blob/master/docs/recipes/fast-browserify-builds-with-watchify.md)

#### Gulp 与 Angular

- [每个 Angular 项目可能需要什么 - 以及 Gulp 构建来提供它](http://blog.jhades.org/what-every-angular-project-likely-needs-and-a-gulp-build-to-provide-it/)

#### Gulp 与 Angular 和 Browserify

- [带有 Gulp、Node 和 Browserify 的高级 AngularJS 结构](http://omarfouad.com/blog/2015/03/21/advanced-angularjs-structure-with-gulp-node-and-browserify/)

#### Gulp 与 Angular 和 Webpack

- [用于 SPA 的 Angular、Webpack 和 Gulp：第一部分](https://luwenhuang.wordpress.com/2015/01/18/refactoring-an-angular-app-to-use-webpack-and-gulp/)
- [用于 SPA 的 Angular、Webpack 和 Gulp：第二部分](https://luwenhuang.wordpress.com/2015/01/19/angular-webpack-and-gulp-for-an-spa-part-ii/)
- [用于 SPA 的 Angular、Webpack 和 Gulp：第三部分](https://luwenhuang.wordpress.com/2015/01/28/angular-webpack-and-gulp-for-an-spa-part-iii/)

#### Gulp 与 React 和 Browserify

- [使用 React 进行 Browserify 和 Gulp](https://hacks.mozilla.org/2014/08/browserify-and-gulp-with-react/)
- [将 React 提升到新的水平：Mixin、Gulp 和 Browserify](http://pomax.github.io/1420592591221/taking-react-to-the-next-level-mixins-gulp-and-browserify)

#### 吞下 Ember

- [使用 Gulp.js 改进 Ember.js 工作流程](http://www.sitepoint.com/improving-ember-js-workflow-using-gulp-js/)

#### 使用 WordPress 进行吞咽

- [使用 Gulp 进行高级 WordPress 开发](https://premium.wpmudev.org/blog/advanced-wordpress-development-using-gulp/)

### 杂项资源

- [Gulp 备忘单](https://github.com/osscafe/gulp-cheatsheet)
- [Gulp 食谱游乐场](https://github.com/johnpapa/gulp-patterns)

## 插件

### 编译

- [gulp-sass](https://github.com/dlmanning/gulp-sass) - Sass → CSS 与 [libsass](https://github.com/sass/libsass)。
- [gulp-ruby-sass](https://github.com/sindresorhus/gulp-ruby-sass) - Sass → CSS 与 Ruby Sass。
- [gulp-compass](https://github.com/appleboy/gulp-compass) - Sass → CSS 与 Ruby Sass 和 Compass。
- [gulp-less](https://github.com/plus3network/gulp-less) - [更少](https://github.com/less/less.js) → CSS。
- [gulp-stylus](https://github.com/stevelacy/gulp-stylus) - [手写笔](https://github.com/stylus/stylus) → CSS。
- [gulp-postcss](https://github.com/postcss/gulp-postcss) - 通过一次解析将 CSS 通过 [PostCSS](https://github.com/postcss/postcss) 处理器进行管道传输。
- [gulp-coffee](https://github.com/contra/gulp-coffee) - [Coffeescript](https://github.com/jashkenas/coffeescript) → JavaScript。
- [gulp-typescript](https://github.com/ivogabe/gulp-typescript) - [TypeScript](https://github.com/Microsoft/TypeScript) → JavaScript。
- [gulp-react](https://github.com/sindresorhus/gulp-react) - Facebook [React](https://github.com/facebook/react) JSX 模板 → JavaScript。
- [webpack-stream](https://github.com/shama/webpack-stream) - 以流的形式运行 [webpack](https://github.com/webpack/webpack) 以方便地与 gulp 集成。

### 转译

- [gulp-babel](https://github.com/babel/gulp-babel) - ES6 → ES5 与 [babel](https://github.com/babel/babel)。
- [gulp-traceur](https://github.com/sindresorhus/gulp-traceur) - ES6 → ES5 使用 [Traceur](https://github.com/google/traceur-compiler)。
- [gulp-regenerator](https://github.com/sindresorhus/gulp-regenerator) - ES6 → ES5 与 [Regenerator](https://github.com/facebook/regenerator)。
- [gulp-es6-transpiler](https://github.com/sindresorhus/gulp-es6-transpiler) - [:no_entry:] ES6 → ES5 与 [es6-transpiler](https://github.com/termi/es6-transpiler)。
- [gulp-myth](https://github.com/sindresorhus/gulp-myth) - [Myth](https://github.com/segmentio/myth) - CSS 规范未来版本的填充。
- [gulp-cssnext](https://github.com/MoOx/gulp-cssnext) - [:no_entry:] 使用明天的 CSS 语法，今天使用 [cssnext](https://github.com/MoOx/postcss-cssnext)。

### 连接

- [gulp-concat](https://github.com/contra/gulp-concat) - 连接文件。

### 缩小化

- [gulp-clean-css](https://github.com/scniro/gulp-clean-css) - 使用 [clean-css](https://github.com/jakubpawlowicz/clean-css) 缩小 CSS。
- [gulp-csso](https://github.com/ben-eb/gulp-csso) - 使用 [CSSO](https://github.com/css/csso) 缩小 CSS。
- [gulp-uglify](https://github.com/terinjokes/gulp-uglify) - 使用 [UglifyJS2](https://github.com/mishoo/UglifyJS2) 缩小 JavaScript。
- [gulp-htmlmin](https://github.com/jonschlinkert/gulp-htmlmin) - 使用 [html-minifier](https://github.com/kangax/html-minifier) 缩小 HTML。
- [gulp-imagemin](https://github.com/sindresorhus/gulp-imagemin) - 使用 [imagemin](https://github.com/imagemin/imagemin) 缩小 PNG、JPEG、GIF 和 SVG 图像。
- [gulp-svgmin](https://github.com/ben-eb/gulp-svgmin) - 使用 gulp 缩小 SVG 文件。

### 优化

- [gulp-uncss](https://github.com/ben-eb/gulp-uncss) - 使用 [UnCSS](https://github.com/giakki/uncss) 删除未使用的 CSS 选择器。
- [gulp-css-base64](https://github.com/zckrs/gulp-css-base64) - 将 CSS 文件中找到的所有资源（url() 声明中的资源）转换为 base64 编码的数据 URI 字符串。
- [gulp-svg2png](https://github.com/akoenig/gulp-svg2png) - 将 SVG 转换为 PNG。
- [gulp-responsive](https://github.com/mahnunchik/gulp-responsive) - 生成不同尺寸的图像。
- [gulp-svgstore](https://github.com/w0rm/gulp-svgstore) - 将 svg 文件与“<symbol>”元素合并为一个。
- [gulp-iconfont](https://github.com/nfroidure/gulp-iconfont) - 从多个 SVG 图标创建图标字体。

### 注入资产

- [gulp-useref](https://github.com/jonkemp/gulp-useref) - 解析 HTML 文件中的构建块以替换对非优化脚本或样式表的引用。
- [gulp-inject](https://github.com/klei/gulp-inject) - 将每个文件转换为字符串，并将每个转换后的字符串注入目标流文件中的占位符中。
- [wiredep](https://github.com/taptapship/wiredep) - 将 Bower 依赖项连接到您的源代码。

### 模板化

- [gulp-angular-templatecache](https://github.com/miickel/gulp-angular-templatecache) - 在 $templateCache 中连接并注册 AngularJS 模板。
- [gulp-jade](https://github.com/phated/gulp-jade) - [Jade](https://github.com/pugjs/jade) → HTML。
- [gulp-handlebars](https://github.com/lazd/gulp-handlebars) - [Handlebars](https://github.com/wycats/handlebars.js) 模板 → JavaScript。
- [gulp-hb](https://github.com/shannonmoeller/gulp-hb) - [Handlebars](https://github.com/wycats/handlebars.js) 模板 → HTML。
- [gulp-nunjucks](https://github.com/sindresorhus/gulp-nunjucks) - [Nunjucks](https://github.com/mozilla/nunjucks) 模板 → JavaScript。
- [gulp-dustjs](https://github.com/sindresorhus/gulp-dust) - [Dust](https://github.com/linkedin/dustjs) 模板 → JavaScript。
- [gulp-riot](https://github.com/e-jigsaw/gulp-riot) - [Riot](https://github.com/riot/riot) 模板 → JavaScript。
- [gulp-markdown](https://github.com/sindresorhus/gulp-markdown) - 标记 → HTML。
- [gulp-template](https://github.com/sindresorhus/gulp-template) - [Lodash](https://github.com/lodash/lodash) 模板 → JavaScript。
- [gulp-swig](https://github.com/colynb/gulp-swig) - [Swig](https://github.com/paularmstrong/swig) 模板 → HTML。
- [gulp-remark](https://github.com/denysdovhan/gulp-remark) - [remark](https://github.com/wooorm/remark) 的 Gulp 插件 - 由插件提供支持的 Markdown 处理器

### 棉绒

- [gulp-csslint](https://www.npmjs.com/package/gulp-csslint) - 使用 [CSSLint](https://github.com/CSSLint/csslint) 自动检查 CSS。
- [gulp-htmlhint](https://github.com/bezoerb/gulp-htmlhint) - [HTMLHint](https://github.com/yaniswang/HTMLHint) 包装器来验证您的 HTML。
- [gulp-jshint](https://github.com/spalger/gulp-jshint) - 使用 [JSHint](https://github.com/jshint/jshint) 检测 JavaScript 中的错误和潜在问题。
- [gulp-jscs](https://github.com/jscs-dev/gulp-jscs) - 使用 [jscs](https://github.com/jscs-dev/node-jscs) 检查 JavaScript 代码风格。
- [gulp-coffeelint](https://github.com/janraasch/gulp-coffeelint) - 一个风格检查器，有助于保持 [CoffeeScript](https://github.com/jashkenas/coffeescript) 代码干净。
- [gulp-tslint](https://github.com/panuhorsmalahti/gulp-tslint) - [TypeScript](https://github.com/Microsoft/TypeScript) gulp 的 linter 插件。
- [gulp-eslint](https://github.com/adametry/gulp-eslint) - 识别并报告 ECMAScript/JavaScript 代码中发现的模式。
- [gulp-w3cjs](https://github.com/callumacrae/gulp-w3cjs) - 使用 [w3cjs](https://github.com/thomasdavis/w3cjs) 验证 HTML。
- [gulp-lesshint](https://github.com/lesshint/gulp-lesshint) - 使用 [lesshint](https://github.com/lesshint/lesshint) 检查较少的文件。
- [gulp-check-unused-css](https://github.com/zalando/gulp-check-unused-css) - 检查 HTML 模板中是否有未使用的 CSS 类。

### 实时重新加载

- [browser-sync](https://github.com/BrowserSync/browser-sync) - 构建网站时保持多个浏览器和设备同步（[食谱](https://github.com/BrowserSync/gulp-browser-sync)）。
- [gulp-livereload](https://github.com/vohof/gulp-livereload) - 用于 livereload 的 Gulp 插件。

### 缓存

- [gulp-changed](https://github.com/sindresorhus/gulp-changed) - 只传递已更改的文件。
- [gulp-cached](https://github.com/contra/gulp-cached) - 一个简单的内存文件缓存。
- [gulp-remember](https://github.com/ahaurw01/gulp-remember) - 记住并调用通过它的文件。
- [gulp-newer](https://github.com/tschaub/gulp-newer) - 仅传递较新的源文件。

### 流量控制

- [merge-stream](https://github.com/grncdr/merge-stream) - 将多个流合并为一个交错流。
- [streamqueue](https://github.com/nfroidure/StreamQueue) - 逐步对排队的流进行管道传输。
- [run-sequence](https://github.com/OverZealous/run-sequence) - 按顺序运行一系列依赖的 gulp 任务。
- [gulp-if](https://github.com/robrich/gulp-if) - 有条件地运行任务。

### 记录

- [gulp-notify](https://github.com/mikaelbr/gulp-notify) - gulp 的通知插件。
- [gulp-size](https://github.com/sindresorhus/gulp-size) - 显示您的项目的大小。
- [gulp-debug](https://github.com/sindresorhus/gulp-debug) - 调试乙烯基文件流以查看哪些文件通过 gulp 管道运行。
- [gulp-beer](https://github.com/lordgiotto/gulp-beer) - 更好的错误报告，具有交互式系统通知和用于错误显示的自定义服务器。

### 测试

- [gulp-mocha](https://github.com/sindresorhus/gulp-mocha) - 运行 [Mocha](https://github.com/mochajs/mocha) 测试。
- [gulp-jasmine](https://github.com/sindresorhus/gulp-jasmine) - 在 Node.js 中运行 [Jasmine 2](https://github.com/jasmine/jasmine) 测试。
- [gulp-protractor](https://github.com/mllrsohn/gulp-protractor) - 用于 [Protractor](https://github.com/angular/protractor) 测试的 Gulp 包装器。
- [gulp-coverage](https://github.com/dylanb/gulp-coverage) - Node.js 的覆盖率报告独立于测试运行程序。
- [gulp-karma](https://github.com/karma-runner/gulp-karma) - gulp 的 Karma 测试运行程序。
- [gulp-ava](https://github.com/sindresorhus/gulp-ava) - 使用 gulp 运行 [AVA](https://github.com/sindresorhus/ava) 测试。

### 杂项插件

- [gulp-util](https://github.com/gulpjs/gulp-util) - 一组有用的实用程序。
- [gulp-plumber](https://github.com/floatdrop/gulp-plumber) - 防止因错误而导致管道破裂。
- [gulp-load-plugins](https://github.com/jackfranklin/gulp-load-plugins) - 自动加载 gulp 插件。
- [main-bower-files](https://github.com/ck86/main-bower-files) - 通过动态获取库文件来简化构建过程设置。
- [autoprefixer](https://github.com/postcss/autoprefixer) - 通过 Can I Use 解析 CSS 并将供应商前缀添加到规则中。
- [gulp-sourcemaps](https://github.com/floridoo/gulp-sourcemaps) - 提供源地图支持。
- [gulp-replace](https://github.com/lazd/gulp-replace) - gulp 的字符串替换插件。
- [gulp-rename](https://github.com/hparra/gulp-rename) - 轻松重命名文件。
- [gulp-rev](https://github.com/sindresorhus/gulp-rev) - 通过将内容哈希附加到文件名来进行静态资产修订：unicorn.css → unicorn-d41d8cd98f.css。
- [del](https://github.com/sindresorhus/del) - 使用 glob 删除文件/文件夹。
- [gulp-exec](https://github.com/robrich/gulp-exec) - 运行外壳命令。
- [gulp-strip-debug](https://github.com/sindresorhus/gulp-strip-debug) - 从 JavaScript 代码中删除控制台、警报和调试器语句。
- [gulp-cssimport](https://github.com/unlight/gulp-cssimport) - 解析 CSS 文件，查找导入，获取链接文件的内容并用它替换导入语句。
- [gulp-inline-css](https://github.com/jonkemp/gulp-inline-css) - 将 CSS 属性内联到 HTML 文件的 style 属性中。
- [gulp-gh-pages](https://github.com/shinnn/gulp-gh-pages) - 将内容发布到 Github 页面。
- [gulp-ng-annotate](https://github.com/Kagami/gulp-ng-annotate) - 使用 [ng-annotate](https://github.com/olov/ng-annotate) 添加 AngularJS 依赖注入注释。
- [gulp-bump](https://github.com/stevelacy/gulp-bump) - 碰撞任何 semver JSON 版本。
- [gulp-file-include](https://github.com/coderhaoxin/gulp-file-include) - 使用 gulp 包含文件。
- [gulp-zip](https://github.com/sindresorhus/gulp-zip) - ZIP 压缩文件。
- [gulp-git](https://github.com/stevelacy/gulp-git) - 使用 gulp 运行 Git 命令。
- [gulp-filter](https://github.com/sindresorhus/gulp-filter) - 使用通配符过滤黑胶流中的文件。
- [gulp-preprocess](https://github.com/jas/gulp-preprocess) - 根据自定义上下文或环境配置预处理文件。
- [gulp-eval](https://github.com/gulp-bem/gulp-eval) - 评估 JS 表达式或需要 CommonJS 模块和 JSON 文件。

## 脚手架

### 样板文件

- [web-starter-kit](https://github.com/google/web-starter-kit) - Google 网络入门套件。
- [gulp-plugin-boilerplate](https://github.com/sindresorhus/gulp-plugin-boilerplate) - 用于启动创建 gulp 插件的样板。
- [polymer-starter-kit](https://github.com/polymerelements/polymer-starter-kit) - Polymer 1.0 应用程序的起点。
- [este](https://github.com/este/este) - 适用于同构功能 Web 应用程序的最完整的 React/Flux 开发堆栈和入门套件。
- [mnml](https://github.com/mrmrs/mnml) - 用于启动响应式 HTML5/Sass 项目的最小样板。
- [kraken](https://github.com/cferdinandi/kraken) - 面向前端 Web 开发人员的轻量级、移动优先的样板。
- [angularjs-gulp-browserify-boilerplate](https://github.com/jakemmarsh/angularjs-gulp-browserify-boilerplate) - 使用 AngularJS、Sass、gulp 和 Browserify 的样板。
- [hapi-ninja](https://github.com/poeticninja/hapi-ninja) - Node.js、Hapi 和 Swig 样板。
- [laravel-5-boilerplate](https://github.com/rappasoft/laravel-5-boilerplate) - Laravel 5 样板项目。
- [react-starterkit](https://github.com/wbkd/react-starterkit) - React 入门套件包含 React-router、Reflux、jest、webpack、gulp 和 Stylus。
- [gulp-front](https://github.com/zoxon/gulp-front) - 基于 gulp、pug、stylus、postcss、webpack 和 babel 的前端样板和模块化 BEM css 框架。
- [Front End Starter](https://github.com/Puritanic/Frontend-Starter-Kit) - 由 Gulp、HTML5 bolierplate、Sass、PostCss 和 Webpack（用于 Babel 转译）支持的前端项目的样板。

### 自耕农发电机

- [generator-gulp-webapp](https://github.com/yeoman/generator-gulp-webapp) - 现代网络应用程序的 gulp 生成器。
- [generator-gulp-angular](https://github.com/Swiip/generator-gulp-angular) - 带有 gulp 的 AngularJS Yeoman 生成器。
- [generator-react-gulp-browserify](https://github.com/randylien/generator-react-gulp-browserify) - React 库的 Yeoman 生成器。它包括 gulp、Browserify、Browsersync 和 Bootstrap。
- [generator-node-gulp](https://github.com/youngmountain/generator-node-gulp) - 一个 Node.js 模块生成器，包括 gulp 和 Mocha。
- [generator-gulp-bootstrap](https://github.com/niallobrien/generator-gulp-bootstrap) - Bootstrap、gulp 和 libsass 的 Yeoman 生成器。
- [generator-angulpify](https://github.com/jgoux/generator-angulpify) - Yeoman 生成器涉及 AngularJS、gulp 和 Browserify。
- [generator-ionic-gulp](https://github.com/tmaximini/generator-ionic-gulp) - 用于 Ionic 项目的 Yeoman 生成器，带有 gulp。
- [generator-gulp-plugin-boilerplate](https://github.com/sindresorhus/generator-gulp-plugin-boilerplate) - 搭建一个 [gulp 插件样板](https://github.com/sindresorhus/gulp-plugin-boilerplate)。
- [generator-jekyllized](https://github.com/sondr3/generator-jekyllized) - Jekyll 工作流程，包括 gulp、Sass、AutoPrefixer、资产优化和缓存清除等等。

## 杂项

- [elixir](https://github.com/laravel/elixir) - 一个干净、流畅的 API，用于为 Laravel 应用程序定义基本的 gulp 任务。
- [gulp-app](https://github.com/sindresorhus/gulp-app) - Gulp 作为应用程序 (OS X)。
- [lmn-gulp-tasks](https://github.com/Lostmyname/lmn-gulp-tasks) - gulp 任务单元测试示例。
- [gulp-chef](http://gulp-cookery.github.io/gulp-chef/) - 一种优雅、直观的重用 gulp 任务的方法。

## 许可证

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png)](http://creativecommons.org/publicdomain/zero/1.0/)

在法律允许的范围内，[Philipp Alferov](https://github.com/alferov) 已放弃本作品的所有版权以及相关或邻接权。
