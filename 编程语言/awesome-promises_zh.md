<a href="https://promisesaplus.com/">
    <img src="https://promisesaplus.com/assets/logo-small.png" alt="Promises/A+ logo" align="right" />
</a>

# 令人敬畏的承诺 [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

> JavaScript Promises 有用资源的精选列表

受到 [awesome](https://github.com/sindresorhus/awesome) 列表的启发。不要与其他令人敬畏的承诺相混淆，例如“我向你保证一百万美元”或“我保证你会保持健康并且永远不必再去健身房”。

**目录**

- [资源、博客和书籍](#resources-blogs-and-books)
- [Promises/A+ 实现（兼容 ES6/ES2015）](#promisesa-implementations-es6es2015-compatible)
  - [严格执行](#strict-implementations)
  - [带有额外功能的实现](#implementations-with-extras)
  - [Fallbacks](#fallbacks)
- [便利设施](#convenience-utilities)

## 资源、博客和书籍

### 对于初学者
* [Promise Cookbook](https://github.com/mattdesl/promise-cookbook) - 为什么、什么以及如何。 “简要介绍[...]主要针对前端开发人员”。
* [Promises for Asynchronous Programming](http://exploringjs.com/es6/ch_promises.html) - 摘自[探索 ES6](http://exploringjs.com/) 的章节
* [You Don't Know JS: Promises](https://github.com/getify/You-Dont-Know-JS/blob/master/async%20&%20performance/ch3.md) - 《你不懂 JS：异步与性能》的章节(https://github.com/getify/You-Dont-Know-JS/tree/master/async%20%26%20performance)
* [JavaScript Promises: an Introduction](https://developers.google.com/web/fundamentals/getting-started/primers/promises) - JavaScript 原生 Promise 实现的基础知识。
* [JavaScript with Promises](http://shop.oreilly.com/product/0636920032151.do) - 来自奥莱利。简短而切题。使用本地和蓝鸟。
* [Promise it won't hurt](https://github.com/stevekane/promise-it-wont-hurt) - 互动式 [nodeschool](https://nodeschool.io/) 研讨会
* [ES6 Kata Promises](http://es6katas.org/) - Promises Katas ：[基础知识](http://tddbin.com/#?kata=es6/language/promise/basics)
* [ES6 的深度承诺](https://ponyfoo.com/articles/es6-promises-in-depth)
* [An Incremental Tutorial on Promises](http://www.sohamkamani.com/blog/2016/08/28/incremenal-tutorial-to-promises/) - 面向初学者的常见问题解答风格教程。

### 深入探讨
* [Promise Fun](https://github.com/sindresorhus/promise-fun) - @sindresorhus 的注释、模式和常见 Promise 问题的解决方案
* [You're Missing the Point of Promises](https://blog.domenic.me/youre-missing-the-point-of-promises/) - Promise 不仅仅是回调聚合，而且 jQuery 的实现（3.0 之前）还不够。
* [We have a problem with promises](https://pouchdb.com/2015/05/18/we-have-a-problem-with-promises.html) - “我们中的许多人在没有真正理解承诺的情况下使用它们。”
* [Promise anti-patterns](https://github.com/petkaantonov/bluebird/wiki/Promise-anti-patterns) - 常见的误用以及如何避免它们。
* [Promise anti-patterns (2)](http://taoofcode.net/promise-anti-patterns/) - 另一组承诺反模式
* [Promise Ponderings, (Anti-)Patterns, and Apologies](https://sdgluck.github.io/2015/08/24/promise-ponderings-patterns-apologies/) - 通过常见问题及其答案来展示和解释承诺行为。
* [Javascript Promises...In Wicked Detail](http://www.mattgreer.org/articles/promises-in-wicked-detail/) - 重新创建承诺实施
* [Writing Promise-Using Specifications](https://www.w3.org/2001/tag/doc/promises-guide) - “本文档提供了有关如何编写创建、接受或操纵承诺的规范的指导”
* [异步函数 - 使 Promise 变得友好](https://developers.google.com/web/fundamentals/getting-started/primers/async-functions)

### 参考文献
* [承诺/A+规范](https://promisesaplus.com/)
* [卡尼乌斯承诺](http://caniuse.com/#feat=promises)
* [Fates and States](https://github.com/domenic/promises-unwrapping/blob/master/docs/states-and-fates.md) - 可能状态的快速定义。
* [Promisees](https://bevacqua.github.io/promisees/) - 为敢于冒险的人提供可视化游乐场。

## Promises/A+ 实现（兼容 ES6/ES2015）

### 严格执行
这些实现不高于或低于 es6 规范。它们可以制作出很棒的 Polyfill，并且与原生的 Promise 非常兼容。

* [pinkie](https://github.com/floatdrop/pinkie) - 小马填充。面向节点，但[可浏览](https://github.com/substack/node-browserify)。 *极其*小的实现。
* [native-promise-only](https://github.com/getify/native-promise-only) - 聚酯填料。浏览器和节点兼容。
* [es6-promise](https://github.com/stefanpenner/es6-promise) - 选择加入 Polyfill。 rsvp.js 的严格规范子集。
* [lie](https://github.com/calvinmetcalf/lie) - 体积小，可通过浏览器进行选择，并带有可选的polyfill。

### 带有额外功能的实现
所有这些都提供了比该语言更多的功能，但仍然兼容。适合所有人的节点+浏览器。

* [bluebird](https://github.com/petkaantonov/bluebird) - 功能齐全，性能卓越。长堆栈跟踪和生成器/协程支持。
* [creed](https://github.com/briancavalier/creed) - 与 Bluebird 类似，性能超强且功能齐全，但以 FP 为导向。协程、生成器、promise、ES2015 迭代和幻想世界规范。
* [rsvp.js](https://github.com/tildeio/rsvp.js/) - 重量轻，带有一些附加功能。兼容低至IE6！
* [Q](https://github.com/kriskowal/q) - 最初的实现之一。长堆栈跟踪和其他好东西。
* [then/promise](https://github.com/then/promise) - 小型，添加了“nodeify”、“denodify”和“done()”。
* [when.js](https://github.com/cujojs/when) - 充满了控制流、功能和实用方法。


### 后备措施
* [native-or-bluebird](https://www.npmjs.com/package/native-or-bluebird) - 帮助过渡到完全原生。
* [pinkie-promise](https://github.com/floatdrop/pinkie-promise) - 使用本机，或回退到“pinkie”。非常适合节点库作者。
* [any-promise](https://github.com/kevinbeaty/any-promise) - 加载第一个可用的实现。对于 browserify 来说是安全的。

## 便利设施
本机且严格符合规范的承诺对于兼容性、面向未来、库作者和浏览器来说都是非常棒的。然而，像 bluebird 这样的库将好东西修补到“Promise”构造函数和原型上。解决方案？当然是小模块！

### sindresorhus 的许多 Promise 实用程序（参见注释）
* [delay](https://github.com/sindresorhus/delay) - 将承诺延迟指定的时间。
* [pify](https://github.com/sindresorhus/pify) - Promisify（“denodify”）回调风格的函数。
* [loud-rejection](https://github.com/sindresorhus/loud-rejection) - 使未处理的承诺拒绝大声失败，而不是默认的无声失败。
* [hard-rejection](https://github.com/sindresorhus/hard-rejection) - 使未处理的承诺拒绝立即失败，而不是默认的静默失败
* [p-queue](https://github.com/sindresorhus/p-queue) - 具有并发控制的 Promise 队列
* [p-break](https://github.com/sindresorhus/p-break) - 打破承诺链
* [p-lazy](https://github.com/sindresorhus/p-lazy) - 创建一个延迟执行的延迟承诺，直到调用`.then()`或`.catch()`
* [p-defer](https://github.com/sindresorhus/p-defer) - 创建延期承诺
* [p-if](https://github.com/sindresorhus/p-if) - 条件承诺链
* [p-tap](https://github.com/sindresorhus/p-tap) - 利用承诺链而不影响其价值或状态
* [p-map](https://github.com/sindresorhus/p-map) - 同时映射 Promise
* [p-all](https://github.com/sindresorhus/p-all) - 同时运行承诺返回和异步函数以及可选的有限并发
* [p-limit](https://github.com/sindresorhus/p-limit) - 以有限的并发性运行多个承诺返回和异步函数
* [p-times](https://github.com/sindresorhus/p-times) - 同时运行承诺返回和异步函数特定次数
* [p-catch-if](https://github.com/sindresorhus/p-catch-if) - 条件承诺捕获处理程序
* [p-time](https://github.com/sindresorhus/p-time) - 衡量解决承诺所需的时间
* [p-log](https://github.com/sindresorhus/p-log) - 记录承诺的值/错误
* [p-filter](https://github.com/sindresorhus/p-filter) - 同时过滤承诺
* [p-settle](https://github.com/sindresorhus/p-settle) - 同时结算承诺并获取其履行价值或拒绝原因
* [p-memoize](https://github.com/sindresorhus/p-memoize) - Memoize 承诺返回和异步函数
* [p-whilst](https://github.com/sindresorhus/p-whilst) - 当条件返回 true 时重复调用函数，然后解决承诺
* [p-throttle](https://github.com/sindresorhus/p-throttle) - 限制承诺返回和异步函数
* [p-debounce](https://github.com/sindresorhus/p-debounce) - 反跳承诺返回和异步函数
* [p-retry](https://github.com/sindresorhus/p-retry) - 重试承诺返回或异步函数
* [p-wait-for](https://github.com/sindresorhus/p-wait-for) - 等待条件成立
* [p-timeout](https://github.com/sindresorhus/p-timeout) - 在指定时间后使承诺超时
* [p-race](https://github.com/sindresorhus/p-race) - 更好的 `Promise.race()`
* [p-try](https://github.com/sindresorhus/p-try) - `Promise#try()` ponyfill - 启动一个承诺链
* [p-finally](https://github.com/sindresorhus/p-finally) - `Promise#finally()` ponyfill - 无论结果如何，当 Promise 解决时调用
* [p-any](https://github.com/sindresorhus/p-any) - 等待任何承诺的兑现
* [p-some](https://github.com/sindresorhus/p-some) - 等待指定数量的承诺履行
* [p-pipe](https://github.com/sindresorhus/p-pipe) - 将承诺返回和异步函数组合成可重用的管道
* [p-each-series](https://github.com/sindresorhus/p-each-series) - 连续迭代 Promise
* [p-map-series](https://github.com/sindresorhus/p-map-series) - 依次映射 Promise
* [p-reduce](https://github.com/sindresorhus/p-reduce) - 使用 Promise 将值列表缩减为值的 Promise
* [p-props](https://github.com/sindresorhus/p-props) - 类似于“Promise.all()”，但适用于“Map”和“Object”

### 其他
* [promise-method](https://github.com/wbinnssmith/promise-method) - 独立的“bluebird.method”。将同步返回方法转变为承诺返回方法。
* [is-promise](https://github.com/then/is-promise) - 确定某件事是否看起来像 Promise。
* [sprom](https://github.com/then/sprom) - 流结束时解决。可选缓冲（小心这一点！）
* [task.js](https://github.com/mozilla/task.js) - 使用 Promise 和生成器以阻塞方式编写异步函数。就像“bluebird.coroutine”一样。
* [co](https://github.com/tj/co) - 类似于“task.js”和“bluebird.coroutine”，但也支持 thunk。
* [lie-fs](https://www.npmjs.com/package/lie-fs) - Node 的 FS API 的 Promise 包装器。
* [promise-do-until](https://github.com/busterc/promise-do-until) - 重复调用函数，直到条件返回 true，然后解决 Promise。
* [promise-do-whilst](https://github.com/busterc/promise-do-whilst) - 当条件返回 true 时重复调用函数，然后解决承诺。
* [promise-semaphore](https://github.com/samccone/promise-semaphore) - 以可配置的串行方式推送一组要完成的工作
* [promise-nodeify](https://github.com/kevinoid/promise-nodeify) - 独立的“nodeify”方法，它在解决或拒绝时调用节点样式的回调。

## 许可证
根据 [知识共享 CC0 许可证](https://creativecommons.org/publicdomain/zero/1.0/) 获得许可。
