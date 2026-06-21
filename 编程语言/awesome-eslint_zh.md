# 很棒的 ESLint [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[<img src="https://eslint.org/icon.svg" width="160"align="right" alt="eslint">](http://eslint.org)

> 很棒的 ESLint 配置、插件等列表。

如果您想贡献，请阅读[贡献指南](contributing.md)。

## 内容

- [Configs](#configs)
  - [知名公司/组织的配置](#configs-by-well-known-companiesorganizations)
  - [其他突出的配置（100星左右）](#other-prominent-configs-100-stars-or-so)
  - [其他配置](#other-configs)
- [使用 ESLint 设置进行预配置](#preconfigured-configs-with-eslint-set-up)
- [Plugins](#plugins)
  - [代码质量](#code-quality)
  - [Compatibility](#compatibility)
  - [JS 中的 CSS](#css-in-js)
  - [Deprecation](#deprecation)
  - [Embedded](#embedded)
  - [Frameworks](#frameworks)
  - [语言和环境](#languages-and-environments)
  - [Libraries](#libraries)
  - [Misc](#misc)
  - [实践和具体 ES 功能](#practices-and-specific-es-features)
  - [Performance](#performance)
  - [Security](#security)
  - [Style](#style)
  - [测试工具](#testing-tools)
- [Parsers](#parsers)
- [Formatters](#formatters)
- [Globals](#globals)
- [Tools](#tools)
- [为 ESLint 开发](#developing-for-eslint)
- [Tutorials](#tutorials)
- [安装和设置](#installation-and-setup)

## 配置

### 知名公司/组织的配置

- [Airbnb](https://github.com/airbnb/javascript/tree/master/packages/eslint-config-airbnb) - [Airbnb 风格指南](https://github.com/airbnb/javascript) 的可共享配置。
- [Airbnb-babel](https://github.com/davidjbradshaw/eslint-config-airbnb-babel) - Airbnb 的 ESLint 配置和 Babel 支持。
- [Alloy](https://github.com/AlloyTeam/eslint-config-alloy) - 适用于 React/Vue/TypeScript 项目的渐进式 ESLint 配置。
- [ESLint](https://github.com/eslint/eslint/tree/master/packages/eslint-config-eslint) - 包含用于 ESLint 团队维护的项目的 ESLint 配置。
- [Facebook](https://www.npmjs.com/package/eslint-config-fbjs) - Facebook 风格指南的可共享配置。
- [Feedzai](https://github.com/feedzai/eslint-config-feedzai) - Feedzai 用于 JavaScript/React 项目的可共享配置。
- [Shopify](https://github.com/Shopify/web-foundation/blob/main/packages/eslint-plugin/README.md) - [Shopify 风格指南](https://github.com/Shopify/javascript) 的可共享配置。
- [Wikimedia](https://github.com/wikimedia/eslint-config-wikimedia) - [Wikimedia 风格指南](https://www.mediawiki.org/wiki/Manual:Coding_conventions/JavaScript) 的可共享配置，由 [MediaWiki](https://www.mediawiki.org/) 使用。

### 其他突出的配置（100星左右）

- [Auto](https://github.com/davidjbradshaw/eslint-config-auto) - 根据项目的依赖关系自动配置 ESLint。
- [Canonical](https://github.com/gajus/eslint-config-canonical) - [规范风格指南](https://github.com/gajus/canonical)的可共享配置。
<!-- lint disable double-link -->
- [Standard](https://github.com/feross/eslint-config-standard) - JavaScript 的可共享配置[标准样式](https://github.com/feross/standard)。
- [XO](https://github.com/xojs/eslint-config-xo) - [XO](https://github.com/xojs/xo) 的可共享配置。
- [Antfu Eslint Config](https://github.com/antfu/eslint-config) - Anthony 的 ESLint 配置预设。

### 其他配置

- [Adjunct](https://github.com/davidjbradshaw/eslint-config-adjunct) - 与主要 ESLint 配置一起使用的合理插件集合。
- [Ash-Nazg](https://github.com/brettz9/eslint-config-ash-nazg) - 一种配置即可统治所有！
- [Cecilia](https://github.com/SandroMiguel/eslint-config-cecilia) - 很棒的项目的 ESLint 配置。
- [clean-typescript](https://github.com/cunarist/eslint-config-clean-typescript) - 通过禁止过多的关键字，在 TypeScript 代码库中强制执行经典 JavaScript 功能。
- [Hardcore](https://github.com/EvgenyOrekhov/eslint-config-hardcore) - 最严格（但实用）的 ESLint 配置。
- [Problems](https://github.com/RyanZim/eslint-config-problems) - 可共享的配置仅捕获实际问题，并且不强制执行风格首选项。
- [Supermind](https://github.com/supermind/eslint-config-supermind) - Supermind 风格的可共享配置。
- [Sheriff](https://github.com/AndreaPontrandolfo/sheriff) - 全面且高度固执的 Eslint 配置。面向打字稿。

## 使用 ESLint 设置进行预配置

- [Node.js Standard Style](https://github.com/geek/node-style) - Node.js 核心配置。
- [eslint-config-airbnb-extended](https://github.com/eslint-config/airbnb-extended) - 强大的 ESLint 配置扩展了流行的 Airbnb 风格指南，并增加了对 TypeScript 的支持。
- [eslint-config-prettier](https://github.com/prettier/eslint-config-prettier) - Prettier 团队维护的 ESlint Prettier 配置。
- [Standard](https://github.com/feross/standard) - JavaScript 标准样式。
- [Superlint](https://github.com/supermind/superlint) - JavaScript Supermind 风格。
- [XO](https://github.com/sindresorhus/xo) - JavaScript 幸福风格 linter ❤️。

## 插件

### 代码质量

- [depend](https://github.com/es-tooling/eslint-plugin-depend) - 帮助检测依赖树膨胀和冗余填充。
- [GitHub](https://github.com/github/eslint-plugin-github) - 杂项。来自 GitHub 的规则。
- [SonarJS](https://github.com/SonarSource/SonarJS/blob/master/packages/jsts/src/rules/README.md) - 检测错误和可疑模式的规则。
- [Unicorn](https://github.com/sindresorhus/eslint-plugin-unicorn) - 各种很棒的 ESLint 规则。
- [@mysticatea/eslint-plugin](https://github.com/mysticatea/eslint-plugin) - 杂项。规则。
- [@brettz9/eslint-plugin](https://github.com/brettz9/eslint-plugin) - 杂项。规则。没有个人配置的“@mysticatea”。
- [De Morgan](https://github.com/azat-io/eslint-plugin-de-morgan) - 转换代码中的逻辑表达式以使它们更易于理解。
- [Deslint](https://github.com/jaydrao215/deslint) - AI 生成的前端代码的设计质量门。 20 条规则，涵盖任意颜色/间距/排版、设计系统漂移、响应式覆盖范围以及跨 React、Vue、Svelte、Angular 和纯 HTML 的 WCAG 2.2 / 2.1 AA 可访问性。
- [eslint-plugin-code-complete](https://github.com/aryelu/eslint-plugin-code-complete) - 一个自定义的 ESLint 插件，它强制执行干净、可维护的软件设计原则——受到 Code Complete 的启发。
- [eslint-plugin-ai-guard](https://github.com/YashJadhav21/eslint-plugin-ai-guard) - 检测 AI 生成的代码通常引入的错误和安全问题（异步误用、空捕获、身份验证间隙、SQL 连接、机密）。

### 兼容性

- [Compat](https://github.com/amilajack/eslint-plugin-compat) - 使用的 API 的 Lint 浏览器兼容性（[caniuse](http://caniuse.com/#search=fetch) 作为 ESLint 插件）。
- [ecmascript-compat](https://github.com/robatwilliams/es-compat) - 禁用您的浏览器列表目标不支持的 ECMAScript 语言功能。
- [es-x](https://github.com/eslint-community/eslint-plugin-es-x) - 禁用特定 ECMAScript 语言版本或个别功能。正确维护不再维护“eslint-plugin-es”的分支。
- [es5](https://github.com/nkt/eslint-plugin-es5) - 适用于 ES5 用户的 ESLint 插件（禁止 ES2015+ 使用）。
- [ie11](https://github.com/Volox/eslint-plugin-ie11) - 检测 IE11 中不支持的 ES6 功能。

### JS 中的 CSS

- [CSS-modules](https://github.com/atfzl/eslint-plugin-css-modules) - Lint css 模块的未定义或未使用的规则。
- [Emotion](https://github.com/emotion-js/emotion/tree/master/packages/eslint-plugin) - ESLint 情感规则。
- 样式组件
  - [Better Styled Components](https://github.com/tinloof/eslint-plugin-better-styled-components) - 自动修复 ESlint 的样式组件规则。
  - [styled-components-a11y](https://github.com/brendanmorrell/eslint-plugin-styled-components-a11y) - A11y 用于样式组件。
- [vanilla-extract](https://github.com/antebudimir/eslint-plugin-vanilla-extract) - 一个 ESLint 插件，用于在 [vanilla-extract CSS](https://github.com/vanilla-extract-css/vanilla-extract) 样式中强制执行 CSS 属性排序。

### 弃用

- [deprecate](https://github.com/AlexMost/eslint-plugin-deprecate) - 将函数或模块标记为已弃用，并在使用它们时获取 lint 消息。
- [disable](https://github.com/mradionov/eslint-plugin-disable) - 使用文件路径模式和内联注释禁用指定的插件。

### 嵌入式

- [HTML](https://github.com/BenoitZugmeyer/eslint-plugin-html) - HTML `<script>` 标签内 JavaScript 的 Linting。
- [Markdown](https://github.com/eslint/eslint-plugin-markdown) - Markdown 内部 JavaScript 的 Linting。

### 框架

- [Angular](https://github.com/angular-eslint/angular-eslint) - Angular (v2+) 的 Linting 规则。
- [AngularJS](https://github.com/Gillespie59/eslint-plugin-angular) - 遵守 [John Papa 的 AngularJS 样式指南](https://github.com/johnpapa/angular-styleguide) 的 Linting 规则。
- [Astro](https://github.com/ota-meshi/eslint-plugin-astro) - [Astro 组件](https://docs.astro.build/en/core-concepts/astro-components/) 插件。
- [Backbone](https://github.com/ilyavolodin/eslint-plugin-backbone) - Backbone 的 Linting 规则。
- [Ember](https://github.com/ember-cli/eslint-plugin-ember) - Ember 的 Linting 规则。
- [Hapi](https://github.com/continuationlabs/eslint-plugin-hapi) - hapi 的 Linting 规则。
- [Meteor](https://github.com/meteor/meteor/tree/devel/npm-packages/eslint-plugin-meteor) - ESLint 的 Meteor 特定 linting 规则。
- 反应
  - [JSX a11y](https://github.com/jsx-eslint/eslint-plugin-jsx-a11y) - JSX 元素的可访问性规则。
  - [React](https://github.com/yannickcr/eslint-plugin-react) - React 和 JSX 的 Linting 规则。
  - [React Hooks](https://github.com/facebook/react/tree/master/packages/eslint-plugin-react-hooks) - React Hooks 的 Linting 规则。
  - [React Native](https://github.com/Intellicode/eslint-plugin-react-native) - React Native 特定的 linting 规则。
  - [React-Redux](https://github.com/DianaSuvorova/eslint-plugin-react-redux) - React-Redux 特定的 linting 规则。
  - [React Refresh](https://github.com/ArnaudBarre/eslint-plugin-react-refresh) - 提升Vite使用时的HMR体验。
- [Solid](https://github.com/joshwilsonvu/eslint-plugin-solid) - Solid 和 JSX 的 Linting 规则。
- [Svelte](https://github.com/sveltejs/eslint-plugin-svelte) - Svelte v3 组件的 Linting 规则。
- 维尤
  - [VueJS](https://github.com/vuejs/eslint-plugin-vue) - VueJS 的插件。
  - [VueJS Scoped CSS](https://github.com/future-architect/eslint-plugin-vue-scoped-css) - VueJS 中作用域 CSS 的插件。

### 语言和环境

- [Babel](https://github.com/babel/babel/tree/main/eslint/babel-eslint-plugin) - 添加内置规则的替换以包含 Babel 功能。
- [eslint-plugin-eslint-plugin](https://github.com/not-an-aardvark/eslint-plugin-eslint-plugin) - 用于检查 ESLint 插件的 ESLint 插件。
- 流量
  - [Flow](https://github.com/gajus/eslint-plugin-flowtype) - 流类型 linting 规则。
  - [Flow Errors](https://github.com/amilajack/eslint-plugin-flowtype-errors) - 将 Flow 作为 ESLint 插件运行。
- [HTML](https://github.com/yeonjuan/html-eslint) - HTML 的 ESLint 插件。
- JSON
  - [JSON](https://github.com/azeemba/eslint-plugin-json) - 检查您的 JSON 文件。
  - [JSON, package.json](https://github.com/Bkucera/eslint-plugin-json-format) - 对 JSON 文件进行 Lint、格式化和自动修复。对你的“package.json”进行排序。
  - [JSON with Comments](https://github.com/ota-meshi/eslint-plugin-jsonc) - 适用于 JSON、JSONC 和 JSON5 的 ESLint 插件。
  - [JSON Schema](https://github.com/ota-meshi/eslint-plugin-json-schema-validator) - 使用 JSON Schema Validator 验证 JavaScript、JSON、YAML 和 TOML 中定义的数据。
  - [eslint-plugin-package-json](https://github.com/JoshuaKGoldberg/eslint-plugin-package-json) - 一致、可读且有效的 package.json 文件的规则。
- [MDX](https://github.com/mdx-js/eslint-mdx/tree/master/packages/eslint-plugin-mdx) - MDX 的 ESLint 解析器/插件。
- [N](https://github.com/eslint-community/eslint-plugin-n) - Node.js 的附加 ESLint 规则。正确维护不再维护“eslint-plugin-node”的分支。
- [SQL](https://github.com/gajus/eslint-plugin-sql) - ESLint 的 SQL linting 规则。
- [TOML](https://github.com/ota-meshi/eslint-plugin-toml) - TOML 的 ESLint 插件。
- [TypeScript](https://typescript-eslint.io) - TypeScript 的 Linting 规则。
  - [eslint-plugin-erasable-syntax-only](https://github.com/JoshuaKGoldberg/eslint-plugin-erasable-syntax-only) - 精细地强制执行 TypeScript 的erasableSyntaxOnly 标志。
  - [eslint-plugin-expect-type](https://github.com/JoshuaKGoldberg/eslint-plugin-expect-type) - 提供 Twoslash、$ExpectError 和 $ExpectType 类型断言。
- [YAML](https://github.com/ota-meshi/eslint-plugin-yml) - YAML 的 ESLint 插件。

### 图书馆

- GraphQL
  - [dotansimha/graphql-eslint](https://github.com/dotansimha/graphql-eslint) - 验证、美化和检查您的 GraphQL 操作和 GraphQL 架构以获得最佳实践。
  - [apollostack/eslint-plugin-graphql](https://github.com/apollostack/eslint-plugin-graphql) - 根据架构检查 GraphQL 查询字符串。
- [TypeGraphQL](https://github.com/borremosch/eslint-plugin-type-graphql) - TypeGraphQL 的 Linting 规则，旨在发现常见错误。
- [jQuery](https://github.com/wikimedia/eslint-plugin-no-jquery) - jQuery 的 Linting 规则，包括已弃用功能的版本化配置。
- [JSDoc](https://github.com/gajus/eslint-plugin-jsdoc) - JSDoc 注释的 Linting 规则（包括 `@example` 中的 JavaScript）。
- 洛达什
  - [Lodash](https://github.com/wix/eslint-plugin-lodash) - Lodash 特定的 linting 规则。
  - [Lodash/fp](https://github.com/jfmengels/eslint-plugin-lodash-fp) - Lodash/fp 特定的 linting 规则。
  - [Lodash template](https://github.com/ota-meshi/eslint-plugin-lodash-template) - Lodash 模板/下划线模板的插件。
- [微模板](https://github.com/platinumazure/eslint-plugin-microtemplates)（用于Lodash和Underscore.js）
- [Mongodb](https://github.com/nfroidure/eslint-plugin-mongodb) - Mongodb 原生 Node.js 驱动程序 linting 规则。
- [Ramda](https://github.com/ramda/eslint-plugin-ramda) - Ramda 特定的 linting 规则。
- [RequireJS](https://github.com/cvisco/eslint-plugin-requirejs) - RequireJS 的 Linting 规则。
- [Tailwind CSS](https://github.com/francoismassart/eslint-plugin-tailwindcss) - Tailwind CSS 类名的 Linting 规则。
- [Tailwind CSS v4](https://github.com/schoero/eslint-plugin-better-tailwindcss) - ESLint 插件可通过格式化规则提高可读性并使用 linting 规则强制执行最佳实践，帮助您编写更好的 tailwindcss。

### 杂项

- [Diff](https://github.com/paleite/eslint-plugin-diff) - 仅在更改的行上运行 ESLint。还支持CI！
- [Misc](https://github.com/ilyub/eslint-plugin-misc) - 各种规则，包括创建自定义检查和包装（修改）第三方规则的规则。
- [Notice](https://github.com/nickdeis/eslint-plugin-notice) - 一个 eslint 规则，可以检查文件顶部并修复它们！
- [Only-Error](https://github.com/davidjbradshaw/eslint-plugin-only-error) - 将所有规则转换为错误。
- [Only-Warn](https://github.com/bfanger/eslint-plugin-only-warn) - 将所有规则转换为警告。
- [PutOut](https://github.com/coderaiser/putout/tree/master/packages/eslint-plugin-putout) - ESLint 插件将 [putout](https://github.com/coderaiser/putout) linter 集成到 ESLint 中。
- [TypeLint](https://github.com/yarax/eslint-plugin-typelint) - 引入基于现有模式（Swagger、Redux）的类型和对对象属性的 linting 访问，防止“未定义”错误。
- [Woke](https://github.com/amwmedia/eslint-plugin-woke) - 帮助捕获不敏感的单词，促进包容性代码库。

### 实践和具体 ES 功能

- [array-func](https://github.com/freaktechnik/eslint-plugin-array-func) - 使用 es2015 数组方法和函数时避免冗余。
- [arrow functions](https://github.com/getify/eslint-plugin-proper-arrows) - ESLint 规则确保正确的箭头函数定义。
- [boundaries](https://github.com/javierbrea/eslint-plugin-boundaries) - 确保项目中检查文件结构和依赖关系的元素尊重您的架构边界。
- [@eslint-community/eslint-plugin-eslint-comments](https://github.com/eslint-community/eslint-plugin-eslint-comments) - 有关 ESLint 指令注释的最佳实践（`/*eslint-disable*/` 等）。正确维护的分支不再维护“eslint-plugin-eslint-comments”。
- [eslint-plugin-error-cause](https://github.com/Amnish04/eslint-plugin-error-cause) - 重新抛出异常时保留原始错误上下文的插件。
- [eslint-plugin-hexagonal-architecture](https://github.com/CodelyTV/eslint-plugin-hexagonal-architecture) - 一个可以帮助您实施六边形架构最佳实践的插件。
- [eslint-plugin-hex-under](https://github.com/2nd-Labs/eslint-plugin-hex-under) - 一个证明十六进制数小于指定值的插件。
- [eslint-plugin-signature-design](https://github.com/Vladyslav-Soldatenko/eslint-plugin-signature-design) - 禁止具有太多相同类型参数的函数，鼓励基于对象的签名并防止原始痴迷。
- [eslint-plugin-write-good-comments](https://github.com/kantord/eslint-plugin-write-good-comments) - 在评论中强化良好的写作风格。
- [eslint-plugin-exception-handling](https://github.com/Akronae/eslint-plugin-exception-handling) - Lints 可能引发错误的未处理函数。
- [fp](https://github.com/jfmengels/eslint-plugin-fp) - 函数式编程的 ESLint 规则。
- [functional](https://github.com/jonaskello/eslint-plugin-functional) - ESLint 规则在 JavaScript 和 TypeScript 中禁用突变并提升 fp。
- [mutate](https://github.com/gchumillas/eslint-plugin-mutate) - 通过强制执行显式的 `mut` 前缀 (JavaScript) 或 `Mut<T>` 类型注释 (TypeScript) 来防止意外的参数突变。
- [ime-safe-form](https://github.com/hiroya-uga/eslint-plugin-ime-safe-form) - 通过要求“e.isCompositing”防护或表单“submit”事件来防止 IME 组合期间意外提交表单。
- [Immutable](https://github.com/jhusain/eslint-plugin-immutable) - 禁用 JavaScript 中的所有突变。
- [import](https://github.com/benmosher/eslint-plugin-import) - ES2015+ 导入/导出语法的 Linting，并防止文件路径和导入名称拼写错误的问题。
- [import-x](https://github.com/un-ts/eslint-plugin-import-x) - ES2015+ 导入/导出语法的 Linting，并防止文件路径和导入名称拼写错误的问题。 “eslint-plugin-import”的轻量级分支，但这破坏了向后兼容性。
- [logical-imports](https://gitlab.com/philbooth/eslint-plugin-logical-imports) - 按本地名称对导入进行逻辑排序。
- [Math](https://github.com/ota-meshi/eslint-plugin-math) - 与数学对象和数字相关的 ESLint 插件。
- [new-with-error](https://github.com/Trott/eslint-plugin-new-with-error) - 要求使用“new”抛出错误。
<!-- lint ignore awesome-spell-check -->
- [no-argument-spread](https://github.com/causalhq/eslint-plugin-no-argument-spread) - 针对“Math.max(...args)”等可能导致大型数组堆栈溢出的表达式进行 lints。
- [no-comments](https://github.com/wisniewski94/eslint-plugin-no-comments) - 如果不使用捆绑器，则可以防止将注释泄漏到生产中，并阻止开发人员注释掉旧代码行。
- [no-constructor-bind](https://github.com/markalfred/eslint-plugin-no-constructor-bind) - 通过报告“this”与“bind”的使用或在构造函数中设置状态来鼓励使用类属性。
- [no-inferred-method-name](https://github.com/johnstonbl01/eslint-no-inferred-method-name) - ESLint 的自定义规则，用于检查对象文字中推断的方法名称。
- [no-loops](https://github.com/buildo/eslint-plugin-no-loops) - 都2019年了，你还在用循环吗？
- [no-restricted-syntax](https://github.com/brettz9/eslint-plugin-query) - 在消息中显示查询语法的内容。
- [no-use-extend-native](https://github.com/dustinspecker/eslint-plugin-no-use-extend-native) - 防止使用扩展的本机对象。
- [Promise](https://github.com/xjamundx/eslint-plugin-promise) - 使用 Promise 时的最佳实践。
- [pure](https://github.com/purely-functional/eslint-plugin-pure) - 强制执行纯函数（无副作用）。
- [ReDoS](https://makenowjust-labs.github.io/recheck/docs/usage/as-eslint-plugin/) - ESLint 插件，用于查找可能的 ReDoS 漏洞。
- [ReDoSDetector](https://github.com/tjenkinson/eslint-plugin-redos-detector) - ESLint 插件，用于查找可能的 ReDoS 漏洞。
- [RegExp](https://github.com/ota-meshi/eslint-plugin-regexp) - ESLint 插件，用于查找正则表达式错误和样式指南违规。
- [sort-keys-fix](https://github.com/leo-buneev/eslint-plugin-sort-keys-fix) - 添加 ESLint `sort-keys` 规则的修复程序。
- [this](https://github.com/matijs/eslint-plugin-this) - 编写纯函数，不允许使用“this”。
- [toplevel](https://github.com/HKalbasi/eslint-plugin-toplevel) - 一个 eslint 插件，用于在模块顶层禁止副作用。

### 性能

- [DOM](https://github.com/amilajack/eslint-plugin-dom)
- [Optimize Regex](https://github.com/BrainMaestro/eslint-plugin-optimize-regex) - 优化正则表达式文字。
- Perf-Standard [插件](https://github.com/Raynos/eslint-plugin-perf-standard) 和 [配置](https://github.com/Raynos/eslint-config-perf-standard)

### 安全性

- [no-secrets](https://github.com/nickdeis/eslint-plugin-no-secrets) - 一个 eslint 插件，用于检测潜在的秘密/凭证。
- [no-unsanitized](https://github.com/mozilla/eslint-plugin-no-unsanitized) - 检查“innerHTML”、“outerHTML”等。
- [pii](https://github.com/shiva-hack/eslint-plugin-pii) - 检查并强制执行代码的 PII 合规性。即注释或字符串中没有电子邮件地址、出生日期、IP 地址或电话号码。
- [pg](https://github.com/interlace-collie/eslint/tree/main/packages/eslint-plugin-pg) - PostgreSQL/node-postgres 安全性：SQL 注入预防 (CWE-89)、连接池泄漏检测 (CWE-772)、事务安全。 13 条规则与 CWE 映射。
- [Security](https://github.com/nodesecurity/eslint-plugin-security) - 节点安全性的 ESLint 规则。
- [xss](https://github.com/Rantanen/eslint-plugin-xss) - 尝试在代码库最终投入生产之前检测代码库中的 XSS 问题。

### 风格

- [ESLint Stylistic](https://eslint.style/) - [格式和风格 ESLint 核心规则已移至此项目并由社区维护。](https://eslint.org/blog/2023/10/deprecating-formatting-rules/)
- [const case](https://www.npmjs.com/package/eslint-plugin-const-case) - 强制常量原始文字大写。
- [editorconfig](https://github.com/platinumazure/eslint-plugin-editorconfig) - 从 [`.editorconfig`](https://editorconfig.org/) 派生规则。
- [filenames](https://github.com/selaux/eslint-plugin-filenames) - 确保 JavaScript 文件的文件名一致。不再维护并且根本不能与 ESlint 9 一起使用。
- [Simple import sort](https://github.com/lydell/eslint-plugin-simple-import-sort) - 轻松自动修复导入排序。
- [perfectionist sorting](https://github.com/azat-io/eslint-plugin-perfectionist) - 对对象、导入、TypeScript 类型、枚举、JSX 属性等进行排序。
- [split-and-sort-imports](https://github.com/sngn/eslint-plugin-split-and-sort-imports) - 对导入进行排序并将“多个”导入拆分为单行导入。
- [Switch case](https://github.com/lukeapage/eslint-plugin-switch-case) - ESLint 的特定于 switch-case 的 linting 规则。
- [padding](https://github.com/mu-io/eslint-plugin-padding) - 允许/禁止语句之间的填充。
- [paths](https://github.com/vitonsky/eslint-plugin-paths) - 使用 tsconfig/jsconfig 中的路径并自动修复别名的相对路径。
- [@gitbutler/no-relative-imports](https://www.npmjs.com/package/@gitbutler/no-relative-imports) - 使用 tsconfig 中的路径并自动修复别名的相对路径。观察 tsconfig 继承。

### 测试工具

- [AVA](https://github.com/avajs/eslint-plugin-ava) - AVA 的 Linting 规则。
- 柴
  - [期待实践](https://github.com/turbo87/eslint-plugin-chai-expect)
  - [带有未使用的表达式](https://github.com/ihordiachenko/eslint-plugin-chai-friendly)
  - [允许的关键字](https://github.com/gavinaiken/eslint-plugin-chai-expect-keywords)
  - [使用 chai-as-promised 插件](https://github.com/fintechstudios/eslint-plugin-chai-as-promised)
  <!-- lint disable double-link -->
  - [globals](https://github.com/t-huth/eslint-plugin-chai-assert-bdd)
- [Cucumber](https://github.com/darrinholst/eslint-plugin-cucumber) - Cucumber 的 Linting 规则。
- [Cypress](https://github.com/cypress-io/eslint-plugin-cypress) - Cypress 的 Linting 规则。
- [Jasmine](https://github.com/tlvince/eslint-plugin-jasmine) - Jasmine 的 Linting 规则。
- 开玩笑
  - [Enforcing practices](https://github.com/jest-community/eslint-plugin-jest) - Jest 的 Linting 规则。
  - [Enforcing consistent formatting](https://github.com/dangreenisrael/eslint-plugin-jest-formatting) - Jest 的格式规则。
  - [Jest-async](https://www.npmjs.com/package/eslint-plugin-jest-async) - Jest 的异步 linting 规则。
  - [Jest-DOM](https://github.com/testing-library/eslint-plugin-jest-dom) - Jest-DOM 的 Linting 规则。
- 维泰斯特
  - [ESLint Plugin Vitest](https://github.com/vitest-dev/eslint-plugin-vitest) - Vitest 的 ESLint 插件。
- 摩卡
  - [Enforcing practices](https://github.com/lo1tuma/eslint-plugin-mocha) - Mocha 的 Linting 规则。
  - [加强可管理性](https://github.com/onechiporenko/eslint-plugin-mocha-cleanup/)
- [Playwright](https://github.com/playwright-community/eslint-plugin-playwright) - Playwright 的 Linting 规则。
- [QUnit](https://github.com/platinumazure/eslint-plugin-qunit) - QUnit 的 Linting 规则。
- [TestCafe-Community](https://github.com/testcafe-community/eslint-plugin-testcafe-community) - TestCafe linting 规则与 env 全局变量（来自 [TestCafe 全局变量](https://github.com/miherlosev/eslint-plugin-testcafe) 的分支）。
- [Testing Library](https://github.com/testing-library/eslint-plugin-testing-library) - 测试库的 Linting 规则。

## 解析器

- [babel-eslint-parser](https://github.com/babel/babel/tree/main/eslint/babel-eslint-parser) - 允许您使用出色的 ESLint 来检查所有有效的 Babel 代码。
- [TypeScript](https://typescript-eslint.io/packages/parser) - 生成与 ESLint 兼容的输出的 TypeScript 解析器。
- [BrightScript](https://github.com/RokuRoad/eslint-plugin-roku) - 用于 Roku 开发的 BrightScript 插件。包括解析器和规则。
- [GraphQL](https://github.com/dotansimha/graphql-eslint) - GraphQL AST 的解析器。包括解析器、插件、处理器（对于非 graphql 文件）和规则。

## 格式化程序

<!-- ignore is to keep "github" lower-case -->
<!--lint ignore awesome-spell-check-->

- [html](https://github.com/shuoshubao/eslint-formatter-html) - 增强的 ESLint 格式化程序。
- [badger](https://github.com/brettz9/eslint-formatter-badger) - 制作基于 SVG 的徽章来总结 ESLint 结果（例如，用于自述文件）。
- [git-log](https://github.com/JamieMason/eslint-formatter-git-log) - ESLint 格式化程序具有 Git 作者、日期和哈希功能。
- [github](https://github.com/hipstersmoothie/eslint-formatter-github) - 直接在拉取请求中查看 ESLint 错误和警告。
- [gitlab](https://gitlab.com/remcohaszing/eslint-formatter-gitlab) - 在 GitLab 代码质量结果中输出 ESLint 结果。
- [mo](https://github.com/fengzilong/eslint-formatter-mo) - 好看的 ESLint 格式化程序，也带来愉快的阅读体验。
- [SARIF](https://www.npmjs.com/package/@microsoft/eslint-formatter-sarif) - 生成 SARIF 格式的结果，以便可以将其导入到 GitHub Advanced Security 等工具中。
- [summary-chart](https://github.com/davidjbradshaw/eslint-formatter-summary-chart) - 将 ESLint 输出格式化为条形图。

## 全局变量

- [confusing-browser-globals](https://github.com/facebook/create-react-app/tree/main/packages/confusing-browser-globals) - 浏览器全局变量的精选列表，通常会引起混乱，并且不建议在没有显式窗口的情况下使用。预选赛。
- [ES 和浏览器全局变量](https://github.com/sindresorhus/globals)（最初来自 ESLint）
- [柴全球](https://github.com/t-huth/eslint-plugin-chai-assert-bdd)
- [TestCafe globals](https://github.com/miherlosev/eslint-plugin-testcafe) - TestCafe 的 `fixture` 和 `test` 全局变量。

## 工具

- [es-file-traverse](https://github.com/brettz9/es-file-traverse) - 根据输入文件或多个文件中的导入和/或需求，仅获取正在使用的文件的列表；可传递给 ESLint 的列表。预期的特别是。用于检查 3rd 方依赖项。
- [eslint-find-rules](https://github.com/sarbbottam/eslint-find-rules) - 查找自定义配置中没有的内置 ESLint 规则。
- [eslint-index](https://github.com/wagerfield/eslint-index) - 用于查找和管理 ESLint 配置文件中的规则的 CLI。
- [eslint-interactive](https://github.com/mizdra/eslint-interactive) - 用于修复大量 ESLint 错误的 CLI 工具。
- [eslint-multiplexer](https://github.com/pimlie/eslint-multiplexer) - 复用 eslint 结果并合并常见文件的结果。
- [eslint-nibble](https://github.com/IanVS/eslint-nibble) - 通过一次修复一个规则来轻松使用 ESLint。
- [eslint-plugin-rule-adoption](https://github.com/Jugbot/eslint-plugin-rule-adoption) - 一个 eslint 插件，用于增量规则采用，当 `--fix` 和 codemods 不能削减它时。
- [eslint-rule-documentation](https://github.com/jfmengels/eslint-rule-documentation) - 查找 ESLint 规则文档的 URL。
- [ESlint Rules Index](https://eslint-rules-index.vercel.app/) - ESlint 规则大表可帮助开发人员轻松找到它们。
- [eslint-watch](https://github.com/rizowski/eslint-watch) - 使用监视模式运行 ESLint。
- [codacy-eslint](https://github.com/codacy/codacy-eslint) - [Codacy](https://www.codacy.com) 使用 Docker 来运行 ESLint。
- [esprint](https://github.com/pinterest/esprint) - 跨多个线程运行 ESLint。
- [generator-eslint](https://github.com/eslint/generator-eslint) - 生成 ESLint
[Yeoman](http://yeoman.io/) 的插件和规则。
- [editor-info](https://github.com/fisker/editor-info) - 检测是否在编辑器/IDE 中以及哪种类型，从而允许相应地调整 ESLint 配置。
- [eslint-dashboard](https://github.com/fengzilong/eslint-dashboard) - 位于您终端中的交互式 ESLint 工作流程。
- [eslint-remote-tester](https://github.com/AriPerkkio/eslint-remote-tester) - CLI 工具，用于同时针对多个存储库测试给定的 ESlint 规则。
- [eslint-disable-autofix](https://github.com/MorevM/eslint-disable-autofix/) - 用于禁用特定 ESLint 规则的自动修复的实用程序。

## 为 ESLint 开发

- [eslint-doc-generator](https://github.com/bmish/eslint-doc-generator) - 为您的 ESLint 插件生成文档，包括自述文件的规则表和规则文档的标头。
- [eslint-docgen](https://github.com/wikimedia/eslint-docgen) - 从规则元数据和测试用例自动生成 ESLint 插件文档。

## 教程

- [Creating an ESLint Plugin](https://medium.com/tumblbug-engineering/creating-an-eslint-plugin-87f1cb42767f) - 文章介绍了 ESLint 规则和插件的创建。
- [Lint Like It's 2015](https://medium.com/@dan_abramov/lint-like-it-s-2015-6987d44c5b48#.5p3yk0b03) - 文章介绍了使用 ESLint 的好处。
- [Writing a rule to spot undeclared props hiding in plain sight](http://blog.cowchimp.com/writing-a-custom-eslint-rule-to-spot-undeclared-props/) - 有关创建需要范围分析的规则的文章。
- [Dear Old ESLint](https://adropincalm.com/blog/dear-old-eslint/) - 关于 ESLint 的快速介绍文章。

## 安装和设置

- [Lintier](https://github.com/josh-stillman/lintier) - CLI 可在 TypeScript 项目中快速构建 ESLint 和 Prettier 设置。
