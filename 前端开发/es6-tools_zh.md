# <img src="http://i.imgur.com/yy1sACZ.png" width="100px"/> ECMAScript 6 工具 [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

## 转译器

* [Babel](https://github.com/babel/babel) - 将 ES6+ 代码转换为普通 ES5，无需运行时
* [Traceur compiler](https://github.com/google/traceur-compiler) - ES6 功能 > ES5。包括类、生成器、承诺、解构模式、默认参数等。
* [es6ify](https://github.com/thlorenz/es6ify) - Traceur 编译器包装为 [Browserify](http://browserify.org/) v2 转换
* [babelify](https://github.com/babel/babelify) - Babel 转译器包装为 [Browserify](http://browserify.org/) 转换
* [es6-transpiler](https://github.com/termi/es6-transpiler) - ES6 > ES5。包括类、解构、默认参数、传播
* Square 的 [es6-module-transpiler](https://github.com/esnext/es6-module-transpiler) - AMD 或 CJS 的 ES6 模块
* Facebook 的 [regenerator](https://github.com/facebook/regenerator) - 将 ES6 Yield/generator 函数转换为 ES5
* Facebook 的 [jstransform](https://github.com/facebookarchive/jstransform) - 一个用于可插入 JS 语法转换的简单实用程序。附带一小组 ES6 -> ES5 转换
* [defs](https://github.com/olov/defs) - ES6 块作用域 const 和 let 变量到 ES3 vars
* [es6_module_transpiler-rails](https://github.com/DavyJonesLocker/es6_module_transpiler-rails) - Rails 资产管道中的 ES6 模块
* [一些 Sweet.js 宏](https://github.com/jlongster/es6-macros) 从 ES6 编译到 ES5
* Bitovi 的 [transpile](https://github.com/stealjs/transpile) - 将 ES6 转换为 AMD、CJS 和 StealJS。
* [regexpu](https://github.com/mathiasbynens/regexpu) - 将支持 Unicode 的 ES6 正则表达式转换为 ES5
* [Lebab](https://github.com/mohebifar/lebab) - ES5 代码到 ES6 的转换（近似值）

## 构建时转译

### 吞咽插件
* 巴别塔：[gulp-babel](https://github.com/babel/gulp-babel)
* Traceur：[gulp-traceur](https://github.com/sindresorhus/gulp-traceur)
* 再生器：[gulp-regenerator](https://github.com/sindresorhus/gulp-regenerator)
* ES6 模块转译器：[gulp-es6-module-transpiler](https://github.com/ryanseddon/gulp-es6-module-transpiler)
* es6-transpiler: [gulp-es6-transpiler](https://github.com/sindresorhus/gulp-es6-transpiler) - ES6 → ES5
* es6-jstransform: [gulp-jstransform](https://github.com/hemanth/gulp-jstransform) - ES6 → ES5 使用 FB 的 [jstransform](https://github.com/facebook/jstransform)
* 正则表达式：[gulp-regexpu](https://github.com/mathiasbynens/gulp-regexpu)
* TypeScript：[gulp-typescript](https://github.com/ivogabe/gulp-typescript)

### 繁重任务
* Babel: [grunt-babel](https://github.com/babel/grunt-babel) - 将 ES6+ 代码转换为普通 ES5，无需运行时
* Traceur：[grunt-traceur](https://github.com/aaronfrost/grunt-traceur) ES6 > ES5 转译，[grunt-traceur-build](https://github.com/tarruda/grunt-traceur-build)
* ES6 模块转译器：[grunt-es6-module-transpiler](https://github.com/joefiorini/grunt-es6-module-transpiler)
* Regenerator: [grunt-regenerator](https://github.com/sindresorhus/grunt-regenerator) - ES6 生成器函数到 ES5
* [grunt-microlib](https://github.com/thomasboyt/grunt-microlib) - 使用 ES6 模块转译器的库工具（示例 [Gruntfile](https://github.com/jakearchibald/es6-promise/blob/c3336087fffc52e66cf5398e5b56b23a291080fc/Gruntfile.js)）
* [grunt-defs](https://github.com/EE/grunt-defs) - ES6 块作用域 const 和 let 变量，到 ES3
* es6-transpiler: [grunt-es6-transpiler](https://github.com/sindresorhus/grunt-es6-transpiler) - ES6 → ES5
* TypeScript: [grunt-ts](https://github.com/TypeStrong/grunt-ts) - ES6+ > ES5/ES3 转译

### 西兰花插件
* Babel：[broccoli-babel-transpiler](https://github.com/babel/broccoli-babel-transpiler)
* Traceur：[broccoli-traceur](https://github.com/sindresorhus/broccoli-traceur)
* 再生器：[broccoli-regenerator](https://github.com/sindresorhus/broccoli-regenerator)
* ES6 转译器：[broccoli-transpiler](https://github.com/sindresorhus/broccoli-es6-transpiler)
* ES6 模块转译器：[broccoli-es6-module-transpiler](https://github.com/mmun/broccoli-es6-module-transpiler)
* ES6 fat arrow 转译器：[broccoli-es6-arrow](https://github.com/hemanth/broccoli-es6-arrow.git)
* TypeScript：[broccoli-tsc](https://github.com/ngParty/broccoli-tsc)

### 早午餐插件
* Babel：[babel-brunch](https://github.com/babel/babel-brunch)
* ES6 模块转译器：[es6-module-transpiler-brunch](https://github.com/gcollazo/es6-module-transpiler-brunch)
* TypeScript：[typescript-brunch](https://github.com/josheyse/typescript-brunch)

## Webpack 插件
* 巴别塔：[babel-loader](https://github.com/babel/babel-loader)
* Traceur：[traceur-compiler-loader](https://github.com/gdi2290/traceur-compiler-loader)
* TypeScript：[awesome-typescript-loader](https://github.com/s-panferov/awesome-typescript-loader)

## 双核插件
* 巴别塔：[duo-babel](https://github.com/babel/duo-babel)
* TypeScript：[duo-typescript](https://github.com/frankwallis/duo-typescript)

## 连接插件
* 巴别塔：[babel-connect](https://github.com/babel/babel-connect)
* TypeScript：[typescript-middleware](https://github.com/brn/typescript-middleware)

## 吞噬插件
* 巴别塔：[gobble-babel](https://github.com/babel/gobble-babel)
* Traceur：[gobble-es6-transpiler](https://github.com/gobblejs/gobble-es6-transpiler)

## 玉石插件
* 通天塔：[jade-babel](https://github.com/babel/jade-babel)
* Traceur：[jade-traceur](https://www.npmjs.com/package/jade-traceur)

## 笑话插件
* 巴别塔：[babel-jest](https://github.com/babel/babel-jest)

## 业力插件
* Babel：[karma-babel-preprocessor](https://github.com/babel/karma-babel-preprocessor)
* Traceur：[karma-traceur-preprocessor](https://github.com/karma-runner/karma-traceur-preprocessor)
* TypeScript：[karma-typescript-preprocessor](https://github.com/sergeyt/karma-typescript-preprocessor)

## 链轮插件
* Babel：[sprockets-es6](https://github.com/josh/sprockets-es6)
* Traceur：[sprockets-traceur](https://github.com/gunpowderlabs/sprockets-traceur)
* TypeScript：[typescript-rails](https://github.com/typescript-ruby/typescript-rails)

## 浏览器插件
* [Scratch JS](https://github.com/richgilbank/Scratch-JS) - Chrome/Opera DevTools 扩展，用于在带有 Babel 或 Traceur 的页面上运行 ES6
* [generator-typescript](https://github.com/mrkev/generator-typescript) - TypeScript 应用程序的 Yeoman 生成器

## 摩卡插件
* [Mocha Traceur](https://github.com/domenic/mocha-traceur) - Mocha 的一个简单插件，用于通过 Traceur 编译器传递 JS 文件

## 模块加载器

* ES6 [Module Loader polyfill](https://github.com/ModuleLoader/es6-module-loader)（与最新规范和 Traceur 兼容）
* [js-loaders](https://github.com/jorendorff/js-loaders) - Mozilla 的符合规范的加载器原型
* [JSPM](http://jspm.io/) - ES6、AMD、CJS 模块加载/包管理
* [Babel 模块加载器](https://github.com/babel/babel-loader)
* [beck.js](https://github.com/unscriptable/beck) - 用于 ES6 模块加载器管道的工具包、用于遗留环境的垫片

## 样板文件
* [es6-boilerplate](https://github.com/davidjnelson/es6-boilerplate) - 允许社区现在通过 Traceur 与 amd 和浏览器全局模块结合使用 es6 的工具，并在真实浏览器中进行源映射、串联、缩小、压缩和单元测试。
* [es6-jspm-gulp-boilerplate](https://github.com/alexweber/es6-jspm-gulp-boilerplate) - 现在允许社区通过 babel 结合 jspm 使用 es6 的工具，并使用 es6 在真实浏览器中进行源映射、串联、缩小、压缩和单元测试。

## 代码生成

* [generator-node-esnext](https://github.com/briandipalma/generator-node-esnext) - Traceur 应用程序的 Yeoman 生成器
* [generator-es6-babel](https://github.com/HenriqueLimas/generator-es6-babel) - Babel 应用程序的 Yeoman 生成器
* [generator-gulp-babelify](https://github.com/HenriqueLimas/generator-gulp-babelify) - [Babel](https://babeljs.io/)、[Browserify](http://browserify.org/) 和 [Gulp](http://gulpjs.com/) 的 Yeoman 生成器
* [grunt-init-es6](https://www.npmjs.com/package/grunt-init-es6) - 带有单元测试的脚手架节点模块，用 ES6 编写
* [带有 ES6 ember 模块的 Loom 发电机](https://github.com/ryanflorence/loom-generators-ember)
* 用于 ES6 模块转译的 Brunch [插件](https://www.npmjs.com/package/es6-module-transpiler-brunch)

## 聚合物填料

* [core-js](https://github.com/zloirock/core-js) - ES6的模块化和紧凑的polyfills，包括Symbols、Map、Set、Iterators、Promises、setImmediate、Array generics等。[Babel](https://github.com/babel/babel)使用的标准库。
* [es6-shim](https://github.com/paulmillr/es6-shim) - 几乎所有新的 ES6 方法——来自 Map、Set、String、Array、Object、Object.is 等。
* [WeakMap、Map、Set、HashMap - ES6 集合](https://github.com/Benvie/harmony-collections)
* Polymer 的 [WeakMap 垫片](https://github.com/Polymer/WeakMap)
* [`String.prototype.startsWith`](https://github.com/mathiasbynens/String.prototype.startsWith)
* [`String.prototype.endsWith`](https://github.com/mathiasbynens/String.prototype.endsWith)
* [`String.prototype.at`](https://github.com/mathiasbynens/String.prototype.at)
* [`String.prototype.repeat`](https://github.com/mathiasbynens/String.prototype.repeat)
* [`String.prototype.includes`](https://github.com/mathiasbynens/String.prototype.includes)
* [`String.prototype.codePointAt`](https://github.com/mathiasbynens/String.prototype.codePointAt)
* [`String.fromCodePoint`](https://github.com/mathiasbynens/String.fromCodePoint)
* [`Array.prototype.find`](https://github.com/paulmillr/Array.prototype.find)
* [`Array.prototype.findIndex`](https://github.com/paulmillr/Array.prototype.findIndex)
* [`Array.from`](https://github.com/mathiasbynens/Array.from)
* [`Array.of`](https://github.com/mathiasbynens/Array.of)
* [`Object.assign`](https://github.com/sindresorhus/object-assign)
* [`Number.isFinite`](https://github.com/sindresorhus/is-finite)
* [`Math.sign`](https://github.com/sindresorhus/math-sign)
* [`RegExp.prototype.match`](https://github.com/mathiasbynens/RegExp.prototype.match)
* [`RegExp.prototype.search`](https://github.com/mathiasbynens/RegExp.prototype.search)
* [es6-promise](https://github.com/jakearchibald/es6-promise) - 用于与 ES6 API 匹配的 Promise 的 polyfill
* [ES6 Map Shim](https://github.com/eriwen/es6-map-shim) - 尽可能遵循最新规范的破坏性垫片。
* [`Function.create`](https://github.com/walling/Function.create.js)
* [ES6 垫片](https://github.com/inexorabletash/polyfill/blob/master/es6.md)
* [ES6 符号填充](https://github.com/medikoo/es6-symbol)
* [ES6 映射、集合、WeakMap](https://github.com/EliSnow/Blitz-Collections)
* [harmony-reflect](https://github.com/tvcutsem/harmony-reflect) - ES6 [反射模块](http://wiki.ecmascript.org/doku.php?id=harmony:reflect_api)（包含[代理 API](http://soft.vub.ac.be/~tvcutsem/proxies/)）
* [ES5 based shims in pure CJS style](https://gist.github.com/medikoo/102b7d0e697627133788#list-of-ecmascript-6-shims) - 数组、对象、数字、数学和字符串函数/方法，以及 Map、Set、Symbol 和 WeakMap 对象

## 编辑

* [Sublime Text 和 TextMate] 的 ES6 语法高亮显示(https://github.com/Benvie/JavaScriptNext.tmLanguage)
* [WebStorm](https://www.jetbrains.com/webstorm/) 和 [PhpStorm](https://www.jetbrains.com/phpstorm/) 中的 ES6 语法支持，使用 [文件观察器或任务运行器](http://blog.jetbrains.com/webstorm/2015/05/ecmascript-6-in-webstorm-transpiling/) 编译为 ES5
* 用于 Traceur 的 DocPad [插件](https://github.com/pflannery/docpad-plugin-traceur)
* [Atom](https://atom.io/) 的语法和转译 [包](https://github.com/gandm/language-babel)
* 了解 Webstorm 中的 ES6 转译选项 [阅读博客文章](http://blog.jetbrains.com/webstorm/2015/05/ecmascript-6-in-webstorm-transpiling/)

## 解析器

* [Esprima](http://esprima.org) - 支持ES6的JavaScript解析器，解析为[ESTree AST格式](https://github.com/estree/estree)
* [Acorn](https://github.com/ternjs/acorn) - 一个小型、快速、基于 JavaScript 的 JavaScript 解析器，支持 ES6，解析为 [SpiderMonkey AST](https://developer.mozilla.org/en-US/docs/Mozilla/Projects/SpiderMonkey/Parser_API) 格式。
* [esparse](https://github.com/zenparsing/esparse) - 用 ES6 编写的 ES6 解析器。
* [Traceur 编译器](https://github.com/google/traceur-compiler) 还具有 `traceur.syntax.Parser` 下可用的内置解析器。

## 其他

* [ES.next showcase](https://github.com/sindresorhus/esnext-showcase) - ES6 功能的实际使用示例
* [looper](https://github.com/wycats/looper) - ES6 的静态分析工具
* [es6-module-packager](https://www.npmjs.com/package/es6-module-packager)
* [es-dependency-graph](https://github.com/yahoo/es-dependency-graph) 和 [grunt-es-dependency-graph](https://github.com/yahoo/grunt-es-dependency-graph) - 从 ES6 模块文件生成导入和导出列表，对于预加载、捆绑等很有用。
* [es6-import-validate](https://github.com/sproutsocial/es6-import-validate) 和 [grunt-es6-import-validate](https://github.com/sproutsocial/grunt-es6-import-validate) - 验证 ES6 模块中匹配的命名/默认导入语句。
* [let-er](https://github.com/getify/let-er) - 将 [let-block block-scoping](http://wiki.ecmascript.org/doku.php?id=proposals:block_expressions#let_statement) （ES6 不接受）转换为 ES3 或 ES6
* [Recast](https://github.com/benjamn/recast) - 基于 Esprima 的 JavaScript 语法树转换器、保守的漂亮打印机和自动源映射生成器。由上面列出的几个转译器使用，包括 [regenerator](https://github.com/facebook/regenerator) 和 [es6-arrow-function](https://github.com/esnext/es6-arrow-function)。
* [Paws on ES6](https://github.com/hemanth/paws-on-es6) - ES6 功能的极简示例。
* [ES6 on node](http://h3manth.com/new/blog/2013/es6-on-nodejs/) - 如何在 Node.js 中使用 ES6 功能。
* [es6-translate](https://github.com/calvinmetcalf/es6-translate) - 使用 ES6 加载器钩子加载 ES6 中的（节点风格的）commonjs 包。
* [Isparta](https://github.com/douglasduteil/isparta)
* [babel-node](https://babeljs.io/docs/usage/cli/#babel-node) - 使用 Babel 运行带有 ES6 转译的 Node cli。
* [ES6 Lab setup](https://github.com/hemanth/es6-lab-setup) - 使用支持“gulp”和“jasmine”的“Babel”或“traceur”将 ES6 转换为 ES5 的简单设置。
* [TypeScript](http://www.typescriptlang.org/) - ECMAScript 的超集，具有严格的类型，旨在与 ES6 保持一致
* [Rollup](http://rollupjs.org/) - Rollup 是下一代 JavaScript 模块捆绑器。使用 ES2015 模块编写您的应用程序或库，然后将它们有效地捆绑到单个文件中以在浏览器和 Node.js 中使用
