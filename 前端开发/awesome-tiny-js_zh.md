# 很棒的小 JS [![Awesome](https://awesome.re/badge-flat.svg)](https://awesome.re)

<div align="center">
  <a href="https://github.com/thoughtspile/awesome-tiny-js#readme">
    <img src="./awesome-logo.png" width="300" height="207">
  </a>
</div>

小型前端库可以让你的包节食。规则：

- 大小低于 2 kB 左右，最小 + gzip，包含所有依赖项，除非另有说明。
- 对于多用途库，有用子集的大小必须低于 2 kB 左右。
- 有用的客户端。我还没有弄清楚仅节点库的参与规则，而且我不太担心它们。
- 二级库仅允许 React、Vue、Angular、svelte。
- 100 多个 GitHub star _或 500 多个每周 npm 安装，专注于经过一些社区审查的工具。
- 没有零 JS（CSS 或仅类型）库。这不是awesome-css之类的。

## 内容

- [用户界面框架](#ui-frameworks)
- [事件发射器](#event-emitters)
- [状态管理者](#state-managers)
  - [Signals](#signals)
  - [反应式编程](#reactive-programming)
- [路由器和 URL 实用程序](#routers-and-url-utils)
- [API层](#api-layer)
- [I18N](#i18n)
- [日期和时间](#dates-and-time)
- [通用实用程序](#generic-utilities)
- [Validation](#validation)
- [唯一ID生成](#unique-id-generation)
- [Colors](#colors)
- [触摸手势](#touch-gestures)
- [文本搜索](#text-search)

## 用户界面框架

UI 框架（库？）提供声明性模板、事件绑定和可观察状态来更新视图。我很慷慨地将这个类别的大小限制扩大到 4.5 kB（如果你很无聊，将它们算作 2 个库），但也将星级限制增加到 2K。

- [preact](https://github.com/preactjs/preact) - 类似 React 的 API（预钩子）。由类似的微型工具和组件组成的酷生态系统。强烈推荐。 <imgalign=“顶部”高度=“24”src=“./img/preact.svg”>

以下库虽小但很酷，但请注意，它们的受欢迎程度大约是 preact 的 500 倍。](https://npmtrends.com/preact-vs-hyperapp-vs-redom) 感谢您解构“框架”的本质：

- [hyperapp](https://github.com/jorgebucaran/hyperapp) - 具有纯 JS 语法和不可变状态的 vDOM 框架， <imgalign="top" height="24" src="./img/hyperapp.svg">
- [redom](https://github.com/redom/redom) - 具有 _imperative_ 事件侦听器和更新的 Hyperapp 样式模板，<imgalign="top"height="24"src="./img/redom.svg">

现在，对于[公开实验](https://npmtrends.com/@arrow-js/core-vs-fre-vs-hyperapp-vs-redom-vs-superfine-vs-vanjs-core) UI 库：

- [fre](https://github.com/frejs/fre) - 类似 React 的库，具有钩子和并发性，<imgalign="top"height="24"src="./img/fre.svg">
- [van](https://github.com/vanjs-org/van) - 基于 vDOM 的框架针对无构建设置进行了优化，<imgalign="top"height="24"src="./img/vanjs-core.svg">
- [superfine](https://github.com/jorgebucaran/superfine) - 删除了状态和效果挂钩的 Hyperapp，<imgalign="top"height="24"src="./img/superfine.svg">
- [arrowjs](https://github.com/justin-schroeder/arrow-js) - 标记模板 + 反应数据，<imgalign="top"height="24"src="./img/arrow-jscore.svg">

如果你不喜欢声明式：

- [umbrella](https://github.com/franciscop/umbrella) - jQuery 风格的 DOM 操作库，<imgalign="top"height="24"src="./img/umbrellajs.svg">

## 事件发射器

事件发射器模式很容易自己实现，但是当您拥有这些很酷的工具时为什么还要麻烦呢？通过一场军备竞赛来构建最小的，限制是 0.5 kB。

- [mitt](https://github.com/developit/mitt) - 我在大多数项目中使用的普通事件发射器，<imgalign="top"height="24"src="./img/mitt.svg">
- [nanoevents](https://github.com/ai/nanoevents) - 更好的取消订阅 API，但没有 `*` 事件，<imgalign="top"height="24"src="./img/nanoevents.svg">
- [onfire.js](https://github.com/hustcc/onfire.js) - 还有 `.once` 方法， <imgalign="top" height="24" src="./img/onfirejs.svg">

## 状态管理者

状态管理器将可观察状态与操作和框架绑定结合起来，用于应用程序范围的状态。

- [zustand](https://github.com/pmndrs/zustand) - 简单的商店，具有令人愉悦的操作和选择器。香草<imgalign=“top”height=“24”src=“./img/zustandvanilla.svg”>，React<imgalign=“top”height=“24”src=“./img/zustand.svg”>
- [nanostores](https://github.com/nanostores/nanostores) - 模块化商店，具有良好的 tree-shaking 支持，<imgalign="top"height="24"src="./img/nanostores.svg">vanilla，+React<imgalign="top"height="24"src="./img/nanostoresreact.svg">额外。支持所有顶级框架。
- [exome](https://github.com/marcisbee/exome) - 带有大量框架连接器的原子存储，<imgalign="top"height="24"src="./img/exome.svg">+React<imgalign="top"height="24"src="./img/exomereact.svg">额外。支持所有顶级框架。
- [storeon](https://github.com/storeon/storeon) - 带有大量框架连接器的最小 redux 风格商店，<imgalign="top"height="24"src="./img/storeon.svg">。 React 额外的 <imgalign="top"height="24"src="./img/storeonreact.svg">+Vue、Svelte、Angular。
- [unistore](https://github.com/developit/unistore) - 带有操作的集中存储，<imgalign="top"height="24"src="./img/unistore.svg">+React<imgalign="top"height="24"src="./img/unistorereact.svg">
- [teaful](https://github.com/teafuljs/teaful) - 使用类似 useState 的 API 进行存储，<imgalign="top"height="24"src="./img/teaful.svg">，包括 React / preact 连接器。

### 信号

信号风格的状态管理器提供可观察值（又名_信号_）、派生值和效果。

- [@preact/signals](https://github.com/preactjs/signals) - 来自 preact <imgalign="top" height="24" src="./img/preactsignals-core.svg"> 核心的 OG 信号，<imgalign="top" height="24" src="./img/preactsignals-react.svg"> 与 React 集成。
- [usignal](https://github.com/WebReflection/usignal) - 较小的信号实现，<imgalign="top"height="24"src="./img/usignal.svg">
- [hyperactiv](https://github.com/elbywan/hyperactiv) - 4 个使对象可观察并监听变化的函数，<imgalign="top"height="24"src="./img/hyperactiv.svg">
- [flimsy](https://github.com/fabiospampinato/flimsy) - 来自 Solid 的信号（它_几乎_适合 UI 框架类别本身）。作者警告：_这可能有问题。_ <imgalign="top"height="24"src="./img/flimsy.svg">

荣誉奖：[oby](https://github.com/vobyjs/oby)_可以_如果_它有tree-shaking，但否则大约 7 kB。

### 反应式编程

另一种众所周知的状态管理方法是反应式编程——对事件流进行操作，应用过滤器和转换以最终获得可观察的值。想想 RxJS，但很小：

- [flyd](https://github.com/paldepind/flyd) - Rx 风格的事件流，<imgalign="top"height="24"src="./img/flyd.svg">
- [callbag-basics](https://github.com/staltz/callbag-basics) - Rx 风格事件流，<imgalign="top"height="24"src="./img/callbag-basics.svg">

## 路由器和 URL 实用程序

通过路径匹配和解析来处理 URL/历史更改：

- [wouter](https://github.com/molefrog/wouter) - 用于 React / preact 的声明式路由器， <imgalign="top" height="24" src="./img/wouter.svg">，也可用作独立挂钩： <imgalign="top" height="24" src="./img/wouteruse-browser-location.svg">
- [@nanostores/router](https://github.com/nanostores/router) - 作为 nanostores 存储的路由（与框架无关），<imgalign="top"height="24"src="./img/nanostoresrouter.svg">
- [navaid](https://github.com/lukeed/navaid) - 基于历史的可观察路由器，<imgalign="top"height="24"src="./img/navaid.svg">

只想解析或匹配 URL 路径而不观察它们？给你：

- [matchit](https://github.com/lukeed/matchit) - <img align="top" height="24" src="./img/matchit.svg"> 中的路由解析器和匹配器
- [regexparam](https://github.com/lukeed/regexparam) - 将 <imgalign="top" height="24" src="./img/regexparam.svg"> 中的路径转换为正则表达式
- [qss](https://github.com/lukeed/qss) - 解析 <imgalign="top" height="24" src="./img/qss.svg"> 中的查询字符串。不确定您是否需要它，[URL API](https://developer.mozilla.org/en-US/docs/Web/API/URL) 支持很好。

## API层

`fetch` API 有一些与之相关的样板：序列化和解析数据、拒绝非 200 响应等。这些小包会为您处理它：

- [redaxios](https://github.com/developit/redaxios) - 现代浏览器的直接 axios 替代品，<imgalign="top"height="24"src="./img/redaxios.svg">
- [wretch](https://github.com/elbywan/wretch) - 可链接的 API，具有错误处理和大量额外插件，<imgalign="top"height="24"src="./img/wretch.svg">
- [gretchen](https://github.com/truework/gretchen) - 具有类型安全错误的可链接 API，<imgalign="top"height="24"src="./img/gretchen.svg">

如果由于某种原因你仍然需要 fetch polyfill，请尝试这个：

- [unfetch](https://github.com/developit/unfetch) - 松散获取填充，<imgalign="top"height="24"src="./img/unfetch.svg">

## 国际化

字符串映射似乎足以翻译应用程序，但这些工具还可以处理插值和一些额外的好处：

- [@nanostores/i18n](https://github.com/nanostores/i18n) - 检测语言环境、加载字典、格式化日期/数字、<imgalign="top"height="24"src="./img/nanostoresin.svg">包括 nanostore。
- [eo-locale](https://github.com/ibitcy/eo-locale) - 插值和日期/数字，<imgalign="top"height="24"src="./img/eo-localecore.svg">或<imgalign="top"height="24"src="./img/eo-localereact.svg">与反应绑定。
- [rosetta](https://github.com/lukeed/rosetta) - 简单的模板字符串（`{{hello}}，{{username}}`）和用于其他所有内容的自定义函数， <imgalign="top" height="24" src="./img/rosetta.svg">
- [lingui](https://github.com/lingui/js-lingui) - 带模板字符串的小核心，<imgalign="top"height="24"src="./img/linguicore.svg">

## 日期和时间

纯 JS 中的日期和时间操作非常冗长。幸运的是，两个顶级日期库都有合理的大小：

- [date-fns](https://github.com/date-fns/date-fns/) - 整体来说并不小，但[大多数函数](https://bundlephobia.com/package/date-fns) 每个函数都在 1 kB 以下（格式和解析相当繁重）。
- [dayjs](https://github.com/iamkun/dayjs) - _几乎_ moment.js 兼容 API，涵盖大多数用例，<imgalign="top"height="24"src="./img/dayjsesm.svg">

还有一些仅进行格式化的包：

- [tinytime](https://github.com/aweary/tinytime) - 简单的日期/时间格式化程序： `{h}:{mm} -> 9:33`, <img align="top" height="24" src="./img/tinytime.svg">
- [tinydate](https://github.com/lukeed/tinydate) - 日期/时间格式化程序，仅支持填充数字输出（`September -> 09`），<img align="top" height="24" src="./img/tinydate.svg">
- [time-stamp](https://github.com/jonschlinkert/time-stamp) - 更多相同的是 <imgalign="top"height="24"src="./img/time-stamp.svg">
- [ms](https://github.com/vercel/ms) - 解析和格式化毫秒持续时间，例如`"1m" <-> 60000`, <imgalign="top"height="24"src="./img/ms.svg">
- [timeago.js](https://github.com/hustcc/timeago.js) - 将日期格式化为 _X 分钟前_ 或 _X 小时后_ <imgalign="top" height="24" src="./img/timeagojs.svg">
- [fromnow](https://github.com/lukeed/fromnow) - 更多相同的是 <imgalign="top"height="24"src="./img/fromnow.svg">

请注意，内置的 [`Intl.DateTimeFormat`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat) 具有良好的支持。

## 通用实用程序

你可以在 lodash 或 ramda 中找到的东西，但更小。大多数非常相似并且非常小，在包结构（单个/每个帮助程序包）和树摇动与直接帮助程序导入方面存在细微差别。

- [remeda](https://github.com/remeda/remeda) - 90 个可摇树的助手 [(list).](https://bundlephobia.com/package/remeda)
- [rambda](https://github.com/selfrefactor/rambda) - 187 个可摇树的助手 [(list).](https://bundlephobia.com/package/rambda)
- [just](https://github.com/angus-c/just) - 82 个助手在单独的包中 [(list).](https://anguscroll.com/just/)
- [@fxts/core](https://github.com/marpple/FxTS) - 96 个可摇树的助手。惰性评估支持。

荣誉奖：[下划线](https://github.com/jashkenas/underscore) 包含许多小于 1 kB 的帮助程序。由于代码库结构，它不像上面的库那样进行树摇动。

注意：lodash 本身不是可树摇动的，但在模块化方面做了很多尝试，包括“lodash.method”包、从“lodash/method”导入和“lodash-es”，但在实践中都没有很好的效果。

另请注意，许多原始 lodash 功能都内置于现代 ES 中。在您的浏览器目标允许的情况下，优先选择本机版本而不是库。

## 验证

要检查对象是否与预期模式匹配，您通常会使用 zod、yup、joi 或 ajv。但 90% 的情况下，您可以在 2 kB 以内获得所需的内容。 _注意：_ 我在树摇动下比较基本验证子集（核心+对象/数组+字符串/数字/布尔值），以避免惩罚具有更多功能的库。

- [v8n](https://github.com/imbrn/v8n) - 具有细粒度检查的 zod 风格 API：`v8n().string().minLength(5).first("H").last("o")`。没有树摇动，<imgalign="top"height="24"src="./img/vn.svg">
- [banditypes](https://github.com/thoughtspile/banditypes) - 最小的验证库：<imgalign="top"height="24"src="./img/banditypes.svg">
- [superstruct](https://github.com/ianstormtaylor/superstruct) - 最流行的模块化验证库，具有良好的tree-shaking功能，<imgalign="top"height="24"src="./img/superstruct.svg">
- [valibot](https://github.com/fabian-hiller/valibot) - 另一个模块化验证库，<imgalign="top"height="24"src="./img/valibot.svg">
- [deep-waters](https://github.com/antonioru/deep-waters) - 可组合功能验证器，<imgalign="top"height="24"src="./img/deep-waterscompose-deep-watershasShape-deep-watersarrayOf-deep-watersisString-deep-watersisNumber-deep-watersisBoolean.svg">。

## 唯一ID生成

唯一 ID 生成不需要大量代码，但我不想自己编写。限制为 500 字节。另请注意，[本机`crypto.randomUUID`](https://developer.mozilla.org/en-US/docs/Web/API/Crypto/randomUUID)具有[OK支持。](https://caniuse.com/mdn-api_crypto_randomuuid)

- [@lukeed/uuid](https://github.com/lukeed/uuid) - 真实 UUID，<imgalign="top"height="24"src="./img/lukeeduuid.svg">
- [nanoid](https://github.com/ai/nanoid) - 具有较大字母的随机 ID，<imgalign="top"height="24"src="./img/nanoid.svg">
- [uid](https://github.com/lukeed/uid) - 更多相同的是 <imgalign="top"height="24"src="./img/uid.svg">
- [hexoid](https://github.com/lukeed/hexoid) - 十六进制 ID，<imgalign="top"height="24"src="./img/hexoid.svg">

## 颜色

颜色操作在纯 UI 开发中很少见，但对于数据可视化非常有帮助，并且使用了[怪异的数学]。

- [colord](https://github.com/omgovich/colord) - 操作颜色并在空格之间进行转换，<imgalign="top"height="24"src="./img/colord.svg">。额外的功能以插件的形式提供，每个插件 150b 到 1.5 kB。
- [colr](https://github.com/stayradiated/colr) - 更多相同的是 <imgalign="top"height="24"src="./img/colr.svg">
- [polychrome](https://github.com/cdonohue/polychrome) - 更多相同的是 <imgalign="top"height="24"src="./img/polychrome.svg">
- [randomcolor](https://github.com/davidmerfield/randomColor) - 有吸引力的随机颜色与配置。 <imgalign=“顶部”高度=“24”src=“./img/randomcolor.svg”>

## 触摸手势

滑动、拖动、捏合或双击等触摸手势是移动用户体验的主要内容，但将一系列触摸移动/指针事件识别为手势非常棘手，而且测试也很痛苦。这里有两个库可以为您完成繁重的工作：

- [alloyfinger](https://github.com/AlloyTeam/AlloyFinger) - 平移、滑动、点击、双击、长按以及捏/旋转。我个人最喜欢的。 <imgalign=“顶部”高度=“24”src=“./img/alloyfinger.svg”>。
- [tinygesture](https://github.com/sciactive/tinygesture) - 可配置的平移、滑动、点击、双击、长按。 <imgalign=“顶部”高度=“24”src=“./img/tinygesture.svg”>。

即使您想自己检测手势，处理鼠标、触摸和指针事件也足够困难，而且浏览器的不一致也无济于事。这里还有两个库可以帮助实现这一点：

- [pointer-tracker](https://github.com/GoogleChromeLabs/pointer-tracker) - 鼠标、触摸和指针事件的统一接口，<imgalign="top"height="24"src="./img/pointer-tracker.svg">
- [detect-it](https://github.com/rafgraph/detect-it) - 检测当前和主要输入法（触摸/鼠标）和支持的事件，<imgalign="top"height="24"src="./img/detect-it.svg">

荣誉奖：[any-touch](https://github.com/any86/any-touch)尝试采用模块化方法进行手势检测，但核心大小约为 2 kB，没有任何手势识别器。 ant design 系统中使用的 [rc-gesture](https://github.com/react-component/gesture) 可能是列表中唯一的 React 组件，但 babel-runtime / corejs 硬连接到构建中的填充将 ~2.5 kB 大小推至超过 10 kB。

## 文本搜索

文本搜索对于客户端过滤和自动建议非常重要。天真的 `option.includes(search)` 对结果没有合理的顺序，并且忽略单词边界会产生意外的匹配，例如 _spa -> newSPAper._ 首先，这里有一些优先考虑单词匹配的库：

- [js-search](https://github.com/bvaughn/js-search) - 功能丰富且可定制：多字段索引、停用词、自定义词干分析器和分词器。 <imgalign=“顶部”高度=“24”src=“./img/js-search.svg”>
- [ndx](https://github.com/localvoid/ndx) - 与js-search类似，不同之处在于[排名](https://kmwllc.com/index.php/2020/03/20/understanding-tf-idf-and-bm-25/)，并且对多词查询不太严格[（比较）]（https://leoniya.github.io/uFuzzy/demos/compare.html?libs=js-search,ndx,Wade&search=twilight%20sag）。支持字段权重。 <imgalign=“顶部”高度=“24”src=“./img/ndx-ndxquery.svg”>
- [wade](https://github.com/kbrsh/wade) - 同样类似，[(compare)](https://leeoniya.github.io/uFuzzy/demos/compare.html?libs=js-search,Wade,ndx&search=twilight%20sag) <imgalign="top"height="24"src="./img/wade.svg">
- [libsearch](https://github.com/thesephist/libsearch) - 无索引搜索（速度较慢，但更易于使用），排序合理 <imgalign="top"height="24"src="./img/libsearch.svg">

找到合理的不精确匹配的一种方法是_stemming_——将单词转换为词根形式。 _Walked_ 将匹配 _walking、_ 等。以下是一些针对英语的 [Porter 词干分析器](https://vijinimallawaarachchi.com/2017/05/09/porter-stemming-algorithm/)：

- [stemmer](https://github.com/words/stemmer) - <imgalign=“顶部”高度=“24”src=“./img/stemmer.svg”>
- [porter-stemmer](https://github.com/jedp/porter-stemmer) - <imgalign=“顶部”高度=“24”src=“./img/porter-stemmer.svg”>

对于非英语单词，我只有荣誉奖：[snowball-js](https://github.com/fortnightlabs/snowball-js) 为 17 kB，支持 15 种语言，[lunr-languages](https://github.com/MihaiValentin/lunr-languages) 支持 30 种语言，但仅适用于 [lunr，](https://github.com/olivernn/lunr.js) 最有前途的是[natural](https://github.com/NaturalNode/natural/tree/master/lib/natural/stemmers)，但它取决于 Node.js。

### 模糊搜索

__模糊搜索__是不精确匹配的另一种方式——单词可以修改。首先，我们有只允许插入的库：spacecat -> SPACECrAfT。不太适合通用文本搜索，但非常适合文件名、命令或 URL 查找。

- [fuzzy](https://github.com/mattyork/fuzzy) - 无索引，可以突出显示匹配项。 <imgalign=“顶部”高度=“24”src=“./img/fuzzy.svg”>
- [fuzzy-search](https://github.com/wouterrutgers/fuzzy-search) - 具有状态索引。 <imgalign=“顶部”高度=“24”src=“./img/fuzzy-search.svg”>
- [fzy.js](https://github.com/jhawthorn/fzy.js) - 一次匹配一个字符串、可摇动树的分数和匹配突出显示。 <imgalign="top"height="24"src="./img/fzyjs.svg">总计，或仅“hasMatch”约 150 字节。
- [fuzzysearch](https://github.com/bevacqua/fuzzysearch) - 一次一个字符串，不计算分数/排名。 <imgalign=“顶部”高度=“24”src=“./img/fuzzysearch.svg”>
- [liquidmetal](https://github.com/rmm5t/liquidmetal) - Quicksilver 算法，优先考虑命令缩写词开头的匹配（例如 `gp` -> `git push`）。一次一根弦。 <imgalign=“顶部”高度=“24”src=“./img/liquidmetal.svg”>
- [quick-score](https://github.com/fwextensions/quick-score) - 另一个基于水银的库，针对长字符串进行了调整。内置列表过滤和排序，<imgalign="top"height="24"src="./img/quick-score.svg">或1.2kB用于单字符串评分。

最后，有一个专门用于拼写检查的库：

- [fuzzyset](https://github.com/Glench/fuzzyset.js) - 查找拼写错误，例如密西比西 -> 密西西比，<imgalign="top"height="24"src="./img/fuzzyset.svg">商业使用费用为 42 美元。


## 贡献

欢迎提出建议！请参阅 [contributing.md](contributing.md)，或删除 [issue](https://github.com/thoughtspile/awesome-tiny-js/issues)。

## 脚注

请参阅 [WIP](wip.md) 了解我发现但尚未深入分析的可能很棒的库，以及 [incubate](incubate.md) 了解尚未满足流行标准的很棒的库。

由 [Vladimir Klepov](https://blog.thoughtspile.tech) 于 2023 年收集和审阅。
