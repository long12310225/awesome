<divalign="center"><img src="browserify.png" alt="Browserify!"></div>

# 很棒的浏览器 [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

> :crystal_ball：精选的 [Browserify](https://github.com/substack/node-browserify) 资源、库和工具列表。

请通过 [contributing](contributing.md) 帮助改进此列表！

## 内容

- [About](#about)
- [官方资源](#official-resources)
- [社区资源](#community-resources)
- [Tutorials](#tutorials)
- [Articles](#articles)
- [Demos](#demos)
- [Videos](#videos)
- [Tools](#tools)
  - [开发服务器](#development-servers)
  - [Plugins](#plugins)
  - [Watchers](#watchers)
  - [CSS 捆绑器](#css-bundlers)
  - [Transforms](#transforms)
  - [浏览器中的节点](#node-in-the-browser)
  - [生产工具](#production-tools)

## 关于

Browserify 允许您通过捆绑所有依赖项在浏览器中“require('modules')”。

您可以使用节点样式的“require()”来组织浏览器代码并加载 npm 安装的模块。 Browserify 将递归地分析应用程序中的所有“require()”调用，以便构建一个可以在单个“<script>”标记中提供给浏览器的包。

## 官方资源

- [Docs](https://github.com/substack/node-browserify#usage)
- [Handbook](https://github.com/substack/browserify-handbook)
- [Repo](https://github.com/substack/node-browserify)
- [Website](http://browserify.org/)

## 社区资源

- [IRC](http://webchat.freenode.net/?channels=browserify)
- [Twitter](http://twitter.com/browserify)
- [StackOverflow](http://stackoverflow.com/questions/tagged/browserify)

## 教程

- [你好世界与 Browserify](http://browserify.org/#middle-section)
- [浏览器冒险](https://github.com/workshopper/browserify-adventure)
- [温和的 Browserify 演练](https://ponyfoo.com/articles/a-gentle-browserify-walkthrough)
- [浏览器指南](http://zhaoda.net/2015/10/16/browserify-guide/)（中文）

## 文章

- [浏览器化简介](https://writingjavascript.org/posts/introduction-to-browserify)
- [在客户端使用 npm](http://dontkry.com/posts/code/using-npm-on-the-client-side.html)
- [Browserify 的工作原理](http://benclinkinbeard.com/posts/how-browserify-works/)
- [Gulp + Browserify：一切帖子](https://www.viget.com/articles/gulp-browserify-starter-faq)
- [浏览器化与组件化](http://www.forbeslindesay.co.uk/post/44144487088/browserify-vs-component)
- [为 Webpack 用户提供 Browserify](https://gist.github.com/substack/68f8d502be42d5cd4942)
- [Browserify 与 Webpack](https://mattdesl.svbtle.com/browserify-vs-webpack)

## 演示

- [画布分割器](http://requirebin.com/?gist=maxogden/9576799) 作者：[hughsk](http://github.com/hughsk)
- [无限 2D 洞穴生成器](http://requirebin.com/?gist=maxogden/9557700) by [hughsk](http://github.com/hughsk)
- [2D 速度控制](http://requirebin.com/?gist=maxogden/9557776) 作者：[sethvincent](http://github.com/sethvincent)

## 视频

- [James Halliday (子堆栈) - LXJS 2013 - Modularidade para todos](https://www.youtube.com/watch?v=DCQNm6yiZh0)
- [Browserify 入门](https://www.youtube.com/watch?v=CTAa8IcQh1U) 作者：[shama](https://github.com/shama/)
- [shama](https://github.com/shama/) [使用 Browserify 转换您的捆绑包](https://www.youtube.com/watch?v=Uk2bgp8OLT8)

## 工具

### 开发服务器

- [budo](https://github.com/mattdesl/budo) - 用于快速原型设计的开发服务器。
- [beefy](https://github.com/chrisdickinson/beefy) - 本地开发服务器，旨在使 browserify 的使用变得快速而有趣。
- [wzrd](https://github.com/maxogden/wzrd) - 超小型 browserify 开发服务器。

### 插件

- [browserify-hmr](https://github.com/AgentME/browserify-hmr) - Browserify 的热模块替换插件。

### 观察者

- [watchify](https://github.com/substack/watchify) - browserify 构建的监视模式。
- [persistify](https://github.com/royriojas/persistify) - 包装“browserify”以进行增量构建。

### CSS 捆绑器

- [sheetify](https://github.com/stackcss/sheetify) - 用于 browserify 的模块化 CSS 捆绑器。
- [parcelify](https://github.com/rotundasoftware/parcelify) - 将 css 添加到 browserify 使用的 npm 模块中。
- [css-modulesify](https://github.com/css-modules/css-modulesify) - 用于加载 CSS 模块的 Browserify 插件。

### 变换

- [babelify](https://github.com/babel/babelify) - babel 的 browserify 转换。
- [aliasify](https://github.com/benbria/aliasify) - 重新映射需要在构建时调用。
- [brfs](https://github.com/substack/brfs) - `fs.readFileSync()` 和 `fs.readFile()` 静态资源 browserify 转换。

### 浏览器中的节点

- [crypto-browserify](https://github.com/crypto-browserify/crypto-browserify) - 节点的“加密”模块到浏览器的端口。
- [stream-browserify](https://github.com/substack/stream-browserify) - 来自节点核心的“stream”模块，适用于浏览器！
- [buffer](https://github.com/feross/buffer) - Node.js 中用于浏览器的“buffer”模块。
- [requirebin](http://requirebin.com/) - 使用 NPM 中的模块编写浏览器 JavaScript 程序。

### 生产工具

- [wzrd.in](https://wzrd.in/) - 浏览器 CDN。浏览器即服务！
- [bankai](https://github.com/yoshuawuyts/bankai) - DIY 资产服务器。以流的形式提供 HTML、CSS 和 JS。

## 贡献

欢迎投稿！请在开始之前阅读[贡献指南](contributing.md)。

## 许可证

[browserify 徽标](browserify.png) 由 [substack](https://github.com/substack) 提供。

所有其他内容均根据 [CC0-1.0](https://spdx.org/licenses/CC0-1.0.html) 发布到公共领域。

[![CC0](http://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)
