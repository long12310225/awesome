关键路径（首屏）CSS 工具 [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
==========================================

> 帮助确定首屏 CSS 优先级的工具

### 首先优先考虑首屏内容。

为了获得最佳性能，PageSpeed Insights [建议](https://developers.google.com/speed/docs/insights/PrioritizeVisibleContent)将页面的关键（首屏）CSS 直接内联到 HTML 中。这消除了额外的往返，并允许浏览器更快地将上折体验绘制到用户的屏幕上。主要思想是：

* 确定页面的首屏样式并将它们写在头部的`<style>`标签之间。
* 在页脚中加载所有其他样式表，最好是异步加载。

以下是帮助生成、内联和报告关键路径 CSS 的工具列表。

## 节点模块


* [Penthouse](https://github.com/pocketjoso/penthouse) - 作者：Jonas Ohlsson 生成关键路径 CSS
* [Critical](https://github.com/addyosmani/critical) - 作者：Addy Osmani 生成并内联关键路径 CSS（使用 Penthouse、[Oust](https://github.com/addyosmani/oust) 和内联样式）
* [CriticalCSS](https://github.com/filamentgroup/criticalcss) - 由 FilamentGroup 发现并输出关键 CSS


## 服务器端模块

* [mod_pagespeed](https://github.com/pagespeed/mod_pagespeed) - 用于自动 PageSpeed 优化的 Apache 模块
* [ngx_pagespeed](https://github.com/pagespeed/ngx_pagespeed) - 用于自动 PageSpeed 优化的 Nginx 模块

## Grunt 任务

* [grunt-penthouse](https://github.com/fatso83/grunt-penthouse)
* [grunt-critical-css](https://github.com/filamentgroup/grunt-criticalcss)
* [grunt-critical](https://github.com/bezoerb/grunt-critical)

## 卡斯珀JS

* [critical-css-casperjs](https://github.com/ibrennan/critical-css-casperjs) - CasperJS 脚本从页面中提取关键 CSS 信息

## PhantomJS

* [dr-css-inliner](https://github.com/drdk/dr-css-inliner) - PhantomJS 脚本用于在页面上内联首屏 CSS。

## 内联源（样式、脚本）

* [inline-styles](https://github.com/maxogden/inline-styles) - 作者：Max Ogden，用内联“<style>”标签替换“<link>”标签+使用数据 URI 的内联 CSS url() 调用
* [gulp-inline-source](https://github.com/fmal/gulp-inline-source) - 作者：Filip Malinowski，将“<link>”标签替换为内联“<style>”标签，并将“<script src="">”标签替换为其内联内容
* [inline-critical](https://github.com/bezoerb/inline-critical) - 作者：Ben Zörb，内联关键路径 CSS 并使用“loadCSS”加载现有样式表
* [isomorphic-style-loader](https://github.com/kriasoft/isomorphic-style-loader/) for Webpack - 允许在 React 应用程序中提取任何给定页面/屏幕的关键 CSS，并在服务器端渲染 (SSR) 期间将其内联到 HTML 中。请参阅 [React Starter Kit](https://github.com/kriasoft/react-starter-kit) 作为示例。

## 异步加载 CSS

内联关键路径 CSS 后，应使用异步加载来获取站点范围内的其余样式。

* [loadCSS](https://github.com/filamentgroup/loadCSS) - 使用 JS 异步加载 CSS。导致此问题的[研究](https://gist.github.com/scottjehl/87176715419617ae6994)也是可用的。
* [async & conditional loading](https://gist.github.com/matt-bailey/602b40c77a5d3381ff26) - 用于根据 body 标签类有条件地异步加载 CSS 文件的 POC 脚本
* [asyncLoader](https://github.com/n0mad01/asyncLoader) - 异步脚本/样式表加载器
* [basket.js](http://addyosmani.github.io/basket.js/) - 支持本地存储缓存的异步脚本/资源加载器。可以[扩展](https://github.com/andrewwakeling/basket-css-example)来加载样式表。

注意：卫报目前还将其全局样式缓存到 localStorage 中以供后续页面加载。更多信息在此[评论](https://gist.github.com/scottjehl/87176715419617ae6994)。

## 在线工具

* [顶层公寓在线](https://jonassebastianohlsson.com/criticalpathcssgenerator/)

## 小书签/扩展

* [片段](https://gist.github.com/PaulKinlan/6284142) 作者：Paul Kinlan。 Patrick Hamann 有一个使用您可以尝试的代码片段的[练习](http://patrickhamann.com/workshops/performance/tasks/2_Critical_Path/2_2.html)。
* [片段](https://gist.github.com/scottjehl/b6129da04733e4e0f9a4) 作者：Scott Jehl
* [CSSVacuum](https://github.com/ndreckshage/CSSVacuum) 作者：ndreckshage

## 渲染阻塞问题检测

* [PageSpeed Insights](https://developers.google.com/speed/pagespeed/insights/) - 用于测量移动设备和桌面设备页面性能的在线工具。它会两次获取 URL，一次使用移动用户代理，一次使用桌面用户代理。
* [PSI](https://github.com/addyosmani/psi) - 作为构建过程一部分的 PageSpeed Insights 报告的节点模块。直接与 Gulp 一起使用，或者如果是 Grunt 用户，则使用 [grunt-pagespeed](https://github.com/jrcryer/grunt-pagespeed)。对于本地测试，可以使用此任务和 [ngrok](http://www.jamescryer.com/2014/06/12/grunt-pagespeed-and-ngrok-locally-testing/) 进行编写。
* [PageSpeed Insights DevTools extension](https://chrome.google.com/webstore/detail/pagespeed-insights-by-goo/gplegfbjlmmehdoakndmohflojccocli?hl=en) - 用于从浏览器内部运行 PageSpeed 测试的 Chrome 扩展。
* [PageSpeed Insights Checker for mobile extension](https://chrome.google.com/webstore/detail/pagespeed-insights-checke/mkjmodmicmpjedhoekkmafdgpocdkbna?hl=en) - 检查每个页面的移动 PageSpeed 分数并为您提供方便的预览。

## 补充工具

* [UnCSS](https://github.com/giakki/uncss) 从页面中删除未使用的 CSS，从而允许您减少站点可能需要加载的全局 CSS。任务可用于 [Grunt](https://github.com/addyosmani/grunt-uncss)、[Gulp](https://github.com/ben-eb/gulp-uncss) 和 [其他](https://addyosmani.com/blog/removing-unused-css/) 构建工具。

