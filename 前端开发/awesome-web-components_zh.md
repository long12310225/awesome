# 很棒的 Web 组件 [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

精彩 Web 组件资源的精选列表。

> **注意**
> 该项目以前被命名为“Web Components the Right Way”

[Web 组件](https://developer.mozilla.org/en-US/docs/Web/Web_Components) — 一套不同的技术，允许您创建可重用的自定义元素 — 将其功能封装在其余代码之外 — 并在您的 Web 应用程序中使用它们。

## 内容

- [Introduction](#introduction)
- [Standards](#standards)
  - [自定义元素](#custom-elements)
  - [影子 DOM](#shadow-dom)
  - [HTML 模板](#html-templates)
  - [CSS 阴影部分](#css-shadow-parts)
- [Guides](#guides)
  - [Accessibility](#accessibility)
  - [最佳实践](#best-practices)
  - [Codelabs](#codelabs)
  - [Examples](#examples)
- [Articles](#articles)
  - [Architecture](#architecture)
  - [Interoperability](#interoperability)
  - [Limitations](#limitations)
  - [Styling](#styling)
- [现实世界](#real-world)
  - [案例研究](#case-studies)
  - [Components](#components)
  - [组件库](#component-libraries)
  - [设计系统](#design-systems)
  - [使用案例](#use-cases)
- [Libraries](#libraries)
  - [基于类别](#class-based)
  - [Functional](#functional)
  - [Integrations](#integrations)
  - [Benchmarks](#benchmarks)
- [Frameworks](#frameworks)
  - [Angular](#angular)
  - [React](#react)
  - [Vue](#vue)
  - [Svelte](#svelte)
- [Ecosystem](#ecosystem)
  - [元框架](#meta-frameworks)
  - [入门套件](#starter-kits)
  - [测试解决方案](#testing-solutions)
  - [Tools](#tools)
- [Books](#books)
- [Tutorials](#tutorials)
- [Insights](#insights)
  - [Podcasts](#podcasts)
  - [Presentations](#presentations)
  - [Talks](#talks)
- [使用指标](#usage-metrics)
- [Proposals](#proposals)
  - [表单关联的自定义元素](#form-associated-custom-elements)
  - [可构造的样式表对象](#constructable-stylesheet-objects)
  - [自定义状态伪类](#custom-state-pseudo-class)
- [Miscellaneous](#miscellaneous)
- [Archive](#archive)
  - [Polyfills](#polyfills)
  - [History](#history)
- [关注谁](#who-to-follow)
- [Maintainers](#maintainers)

## 简介

- [Web 组件简介](https://css-tricks.com/an-introduction-to-web-components/)
- [Web 组件简介](https://developer.salesforce.com/blogs/2020/01/intro-to-web-components.html)
- [可重用组件的圣杯：自定义元素、Shadow DOM 和 NPM](https://www.smashingmagazine.com/2018/07/reusable-components-custom-elements-shadow-dom-npm/)
- [使用 Web 组件的动机，简介](https://www.thinktecture.com/web-components/introduction-and-motivation/)
- [Web 组件的力量](https://hacks.mozilla.org/2018/11/the-power-of-web-components/)
- [网络组件 101](https://nhswd.com/blog/web-components-101-what-are-web-components/)
- [网络组件：从轨道高度](https://javascript.info/webcomponents-intro)
- [什么是浏览器本机 Web 组件？](https://gomakethings.com/what-are-browser-native-web-components/)
- [为什么选择 Web 组件？](https://www.fast.design/docs/resources/why-web-components/)

## 标准

### 自定义元素

自定义元素为作者提供了一种构建自己的全功能 DOM 元素的方法。

- [React 开发人员自定义元素指南](https://css-tricks.com/a-guide-to-custom-elements-for-react-developers/)
- [关于 HTML 自定义元素的所有信息](https://github.com/shawnbot/custom-elements)
- [自定义元素](https://javascript.info/custom-elements)
- [自定义元素 v1：可重用 Web 组件](https://web.dev/custom-elements-v1/)
- [处理自定义元素升级中的属性](https://nolanlawson.com/2021/08/03/handling-properties-in-custom-element-upgrades/)
- [方便的自定义元素模式](https://gist.github.com/WebReflection/ec9f6687842aa385477c4afca625bbf4)
- [HTML 生活标准：自定义元素](https://html.spec.whatwg.org/multipage/custom-elements.html)
- [MDN - 使用自定义元素](https://developer.mozilla.org/en-US/docs/Web/Web_Components/Using_custom_elements)
- [web-platform-tests](https://github.com/web-platform-tests/wpt/tree/master/custom-elements)

### 影子 DOM

Shadow DOM 描述了一种将多个 DOM 树组合成一个层次结构的方法，以及这些树如何在文档中相互交互，从而更好地组合 DOM。

- [Shadow DOM 和事件传播的完整指南](https://pm.dartus.fr/blog/a-complete-guide-on-shadow-dom-and-event-propagation/)
- [DOM 生活标准：影子树](https://dom.spec.whatwg.org/#shadow-trees)
- [MDN - 使用 Shadow DOM](https://developer.mozilla.org/en-US/docs/Web/Web_Components/Using_shadow_DOM)
- [注意 document.activeElement！](https://dev.to/open-wc/mind-the-document-activeelement-2o9a)
- [开放与封闭 Shadow DOM](https://blog.revillweb.com/open-vs-closed-shadow-dom-9f3d7427d1af)
- [影子 DOM](https://javascript.info/shadow-dom)
- [Shadow DOM 和事件](https://javascript.info/shadow-dom-events)
- [深入了解 Shadow DOM](https://github.com/praveenpuglia/shadow-dom-in-depth)
- [Shadow DOM 插槽、组合](https://javascript.info/slots-composition)
- [Shadow DOM 样式](https://javascript.info/shadow-dom-style)
- [Shadow DOM v1：独立的 Web 组件](https://web.dev/shadowdom-v1/)
- [Shadow DOM 的兴起](https://medium.com/front-end-hacking/the-rise-of-shadow-dom-84aa1f731e82)
- [了解 Web 组件的插槽更新](https://coryrylan.com/blog/understanding-slot-updates-with-web-components)
- [什么是 Shadow DOM？](https://bitsofco.de/what-is-the-shadow-dom/)
- [谁不喜欢老虎机？](https://dev.to/westbrook/who-doesnt-love-some-s-3de0)
- [Shadow DOM 门户中的内容](https://dev.to/westbrook/your-content-in-shadow-dom-portals-3cdb)
- [web-platform-tests](https://github.com/web-platform-tests/wpt/tree/master/shadow-dom)

### HTML 模板

`<template>` 元素用于声明可以通过脚本克隆并插入到文档中的 HTML 片段。

- [制作可重复使用的 HTML 模板](https://css-tricks.com/crafting-reusable-html-templates/)
- [HTML 生活标准：“模板”元素](https://html.spec.whatwg.org/multipage/scripting.html#the-template-element)
- [使用普通 JavaScript 的 HTML 模板](https://gomakethings.com/html-templates-with-vanilla-javascript/)
- [MDN - <template>：内容模板元素](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/template)
- [MDN - 使用模板和槽](https://developer.mozilla.org/en-US/docs/Web/Web_Components/Using_templates_and_slots)
- [模板元素](https://javascript.info/template-element)
- [HTML 中的模板](https://kittygiraudel.com/2022/09/30/templating-in-html/)
- [HTML5 模板元素](https://dev.to/ahferroin7/the-html5-template-element-26b6)
- [了解 HTML 中的模板元素](https://blog.openreplay.com/understanding-the-template-element-in-html/)
- [web-platform-tests](https://github.com/web-platform-tests/wpt/tree/master/html/semantics/scripting-1/the-template-element)

### CSS 阴影部分

CSS Shadow Parts 允许开发人员公开 Shadow DOM 中的某些元素以用于样式设计。

- [W3C 第一个公开工作草案](https://www.w3.org/TR/css-shadow-parts-1/)
- [CSS 阴影部分来了！](https://dev.to/webpadawan/css-shadow-parts-are-coming-mi5)
- [MDN - `::part()` CSS 伪元素](https://developer.mozilla.org/en-US/docs/Web/CSS/::part)
- [MDN - `part` 全局属性](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/part)
- [::部分和::主题，::解释者](https://meowni.ca/posts/part-theme-explainer/)
- [web-platform-tests](https://github.com/web-platform-tests/wpt/tree/master/css/css-shadow-parts)

## 指南

### 无障碍

- [Web 组件的可访问性](https://developer.salesforce.com/blogs/2020/01/accessibility-for-web-components.html)
- [ID 引用和 Shadow DOM 的可访问性](https://coryrylan.com/blog/accessibility-with-id-referencing-and-shadow-dom)
- [对话框和影子 DOM：我们可以使其可访问吗？](https://nolanlawson.com/2022/06/14/dialogs-and-shadow-dom-can-we-make-it-accessible/)
- [如何制作可访问的 Web 组件 - 简要指南](https://www.sitepoint.com/accessible-web-components/)
- [管理 Shadow DOM 中的焦点](https://nolanlawson.com/2021/02/13/managing-focus-in-the-shadow-dom/)
- [自定义元素可访问性的未来](https://robdodson.me/the-future-of-accessibility-for-custom-elements/)
- [可访问 Web 组件指南](https://www.erikkroes.nl/blog/accessibility/the-guide-to-accessible-web-components-draft/)
- [Web 组件和可访问性对象模型 (AOM)](https://www.24a11y.com/2019/web-components-and-the-aom/)
- [Web 组件打孔清单](https://www.tpgi.com/web-components-punch-list/)
- [Web 组件仍然需要可访问](https://www.24a11y.com/2018/web-components-still-need-to-be-accessible/)

### 最佳实践

- [自定义元素最佳实践](https://web.dev/custom-elements-best-practices/)
- [开发组件：发布](https://open-wc.org/guides/developing-components/publishing/)
- [Web 组件的黄金标准清单](https://github.com/webcomponents/gold-standard/wiki)
- [创建 Web 平台兼容组件的指南](https://w3ctag.github.io/webcomponents-design-guidelines/)
- [如何将 Web 组件发布到 NPM](https://justinfagnani.com/2019/11/01/how-to-publish-web-components-to-npm/)
- [开放式 Web 组件建议](https://open-wc.org)

### 代码实验室

- [使用 LitElement 构建故事 Web 组件](https://dev.to/straversi/build-a-story-web-component-with-litelement-e59)
- [使用 Web 组件为 2020 年选举构建自定义元素](https://medium.com/stories-from-upstatement/building-custom-elements-with-web-components-for-the-2020-elections-f767ff9e9c6a)
- [使用 ElementInternals 创建自定义表单控件](https://css-tricks.com/creating-custom-form-controls-with-elementinternals/)
- [从 Web 组件到 Lit 元素](https://codelabs.developers.google.com/codelabs/the-lit-path)
- [HowTo 组件 –`<howto-checkbox>`](https://web.dev/components-howto-checkbox/)
- [HowTo 组件 –`<howto-tabs>`](https://web.dev/components-howto-tabs/)
- [HowTo 组件 – `<howto-tooltip>`](https://web.dev/components-howto-tooltip/)
- [点燃：基础知识](https://open-wc.org/codelabs/basics/lit-html.html#0)
- [亮：中级](https://open-wc.org/codelabs/intermediate/lit-html.html#0)
- [为 React 开发者点亮](https://codelabs.developers.google.com/codelabs/lit-2-for-react-devs#0)
- [Web 组件：基础知识](https://open-wc.org/codelabs/basics/web-components.html#0)

### 示例

- [generic-components](https://github.com/thepassle/generic-components) - 通用 Web 组件的集合，重点关注可访问性和易用性。
- [howto-components](https://github.com/GoogleChromeLabs/howto-components) - 实现常见 Web UI 模式的 Web 组件的集合。
- [Nude UI](https://github.com/LeaVerou/nudeui) - 可访问、可定制、超轻量 Web 组件的集合。
- [open-wc code examples](https://open-wc.org/guides/developing-components/code-examples/) - 开发 Web 组件的最佳实践和设计模式的集合。
- [vanilla-retro-js](https://github.com/martine-dowden/vanilla-retro-js) - Vanilla JS UI 组件库，包含已弃用的 HTML 标签。
- [web-components-examples](https://github.com/mdn/web-components-examples) - 系列 Web 组件示例，与 MDN Web 组件文档相关。

## 文章

### 建筑

- [深入分析同构、自主跨框架使用#MicroFrontends](https://itnext.io/a-deep-analysis-into-isomorphic-autonomous-cross-framework-usage-microfrontends-364271dc5fa9)
- [《弗兰肯斯坦迁移》：与框架无关的方法（第 1 部分）](https://www.smashingmagazine.com/2019/09/frankenstein-migration-framework-agnostic-approach-part-1/)
- [《弗兰肯斯坦迁移》：与框架无关的方法（第 2 部分）](https://www.smashingmagazine.com/2019/09/frankenstein-migration-framework-agnostic-approach-part-2/)
- [使用 Web 组件生成配置驱动的动态表单](https://codeburst.io/generating-config-driven-dynamic-forms-using-web-components-7c8d400f7f2e)
- [从 Web 组件 API 中隐藏内部框架方法和属性](https://component.kitchen/blog/posts/hiding-internal-framework-methods-and-properties-from-web-component-apis)
- [如何交付自定义元素](https://medium.com/@WebReflection/how-to-deliver-custom-elements-702fae32d25c)
- [为不同的上下文制作 Web 组件](https://css-tricks.com/making-web-components-for-different-contexts/)
- [支持自动和手动注册自定义元素](https://component.kitchen/blog/posts/supporting-both-automatic-and-manual-registration-of-custom-elements)
- [Web 组件 — 正确的方法](https://equinusocio.dev/blog/web-components-the-right-way/)

### 互操作性

- [Web 组件的高级工具](https://css-tricks.com/advanced-tooling-for-web-components/)
- [定制元素无处不在](https://custom-elements-everywhere.com)
- [随处可用的自定义元素](https://robdodson.me/interoperable-custom-elements/)
- [JavaScript 框架，遇见 Web 组件](https://www.voorhoede.nl/nl/blog/javascript-frameworks-meet-web-components/)
- [Web 组件不是框架的替代品 - 它们比框架更好](https://lamplightdev.com/blog/2020/01/18/web-components-arent-a-framework-replacement-theyre-better-than-that/)
- [Web 组件：无缝互操作](https://medium.com/@sergicontre/web-components-seamlessly-interoperable-82efd6989ca4)

### 局限性

- [除了 Polyfill：Web 组件如何影响当今的我们？](https://dev.to/webpadawan/beyond-the-polyfills-how-web-components-affect-us-today-3j0a)
- [自定义元素、影子 DOM 和隐式表单提交](https://www.hjorthhansen.dev/shadow-dom-and-forms/)
- [表单关联的自定义元素](https://www.hjorthhansen.dev/shadow-dom-form-participation/)
- [你可能不需要 Shadow DOM](https://www.hjorthhansen.dev/you-might-not-need-shadow-dom/)

### 造型

- [Shadow DOM 会提高样式性能吗？](https://nolanlawson.com/2021/08/15/does-shadow-dom-improve-style-performance/)
- [避开 Shadow DOM](https://every-layout.dev/blog/eschewing-shadow-dom/)
- [Nordhealth 如何在 Web 组件中使用自定义属性](https://web.dev/custom-properties-web-components/)
- [Web 组件样式选项](https://nolanlawson.com/2021/01/03/options-for-styling-web-components/)
- [样式范围与 Shadow DOM：哪个最快？](https://nolanlawson.com/2022/06/22/style-scoping-versus-shadow-dom-which-is-fastest/)
- [设置 Web 组件的样式](https://css-tricks.com/styling-a-web-component/)
- [使用 CSS 阴影部分在 Shadow DOM 中设置样式](https://css-tricks.com/styling-in-the-shadow-dom-with-css-shadow-parts/)
- [思考 Web 组件的样式选项](https://css-tricks.com/thinking-through-styling-options-for-web-components/)
- [Web 组件伪类和伪元素比您想象的要容易](https://css-tricks.com/web-component-pseudo-classes-and-pseudo-elements/)
- [Web 标准满足用户层面：使用 CSS-in-JS 来设置自定义元素的样式](https://css-tricks.com/web-standards-meet-user-land-using-css-in-js-to-style-custom-elements/)

## 现实世界

### 案例研究

- [Apple 刚刚将 Web 组件投入生产，您可能错过了](https://dev.to/ionic/apple-just-shipped-web-components-to-production-and-you-probably-missed-it-57pf)
- [让网页设计混乱变得有序（使用 Web 组件）](https://dev.to/thatjoemoore/bringing-order-to-web-design-chaos--3fhb)
- [使用 Microsoft 的 FAST Web 组件开始行动](https://www.infoworld.com/article/3618410/get-moving-with-microsofts-fast-web-components.html)
- [如何在 GitHub 和 Salesforce 中使用 Web 组件](https://thenewstack.io/how-web-components-are-used-at-github-and-salesforce/)
- [我们如何在 GitHub 上使用 Web Components](https://github.blog/2021-05-04-how-we-use-web-components-at-github/)
- [使用 Stencil.js 实现设计语言系统](https://medium.com/@Danetag/implementing-a-design-language-system-with-stencil-js-515432918eb5)
- [ING ❤ Web 组件](https://dev.to/thepassle/ing--web-components-aef)
- [ING Open-Sources Lion，其白标 Web 组件库 – Thomas Allmer 的问答](https://www.infoq.com/articles/ing-open-sources-lion-web-component/)
- [经验教训，使用 Web 组件制作我们的应用程序](https://medium.com/samsung-internet-dev/lessons-learned-making-our-app-with-web-components-bf55379cfcda)
- [回顾 Web 组件的五年](https://bitworking.org/news/2019/07/looking-back-on-five-years-of-web-components)
- [2020 年发布 Web 组件](https://dev.to/joe8bit/shipping-web-components-in-2020-2h54)
- [Firefox UI 现在是使用 Web 组件构建的](https://briangrinstead.com/blog/firefox-webcomponents/)
- [使用Web组件封装CSS并解决设计系统冲突](https://about.gitlab.com/blog/2021/05/03/using-web-components-to-encapsulate-css-and-resolve-design-system-conflicts/)
- [GitHub 上的 Web Components - Web Components SF Meetup](https://www.infoq.com/news/2020/08/web-components-sf-meetup-2020/)
- [Salesforce 的大规模 Web 组件：遇到的挑战、吸取的经验教训](https://www.infoq.com/news/2020/03/web-components-salesforce-lwc/)
- [大规模 Web 开发：使用 Web 组件的可组合应用程序](https://medium.com/@jarrodek/composable-applications-with-web-components-ebe5158387be)
- [web.dev 工程博客 #1：我们如何构建网站并使用 Web 组件](https://web.dev/how-we-build-webdev-and-use-web-components/)

### 组件

- [`<active-table>`](https://github.com/OvidijusParsiunas/active-table) - 可编辑的表格 Web 组件。
- [`<api-viewer>`](https://github.com/web-padawan/api-viewer-element) - API 文档和 Web 组件的实时游乐场。
- [`<chess-board>`](https://github.com/justinfagnani/chessboard-element) - 独立的棋盘 Web 组件。
- [`<css-doodle>`](https://github.com/css-doodle/css-doodle) - 用于使用 CSS 绘制图案的 Web 组件。
- [`<dark-mode-toggle>`](https://github.com/GoogleChromeLabs/dark-mode-toggle) - 允许创建暗模式切换或开关的自定义元素。
- [`<deep-chat>`](https://github.com/OvidijusParsiunas/deep-chat) - 用于与 AI 功能聊天的 Web 组件。
- [`<emoji-picker>`](https://github.com/nolanlawson/emoji-picker-element) - 轻量级表情符号选择器，作为 Web 组件分发。
- [`<fg-modal>`](https://github.com/filamentgroup/fg-modal) - 可访问的模式对话框 Web 组件。
- [`<file-viewer>`](https://github.com/avipunes/file-viewer) - 使用 Svelte 构建的 Web 组件用于查看文件。
- [`<json-viewer>`](https://github.com/alenaksu/json-viewer) - 用于在树视图中可视化 JSON 数据的 Web 组件。
- [`<lite-youtube>`](https://github.com/paulirish/lite-youtube-embed) - Lite YouTube 嵌入，注重视觉表现。
- [`<midi-player>`](https://github.com/cifkao/html-midi-player) - MIDI 文件播放器和可视化 Web 组件。
- [`<model-viewer>`](https://github.com/google/model-viewer) - 用于渲染交互式 3D 模型的 Web 组件。
- [`<notectl-editor>`](https://github.com/Samyssmile/notectl) - 现代富文本编辑器，具有插件架构、不可变状态和零配置与框架无关的部署。
- [`<pdfjs-viewer-element>`](https://github.com/alekswebnet/pdfjs-viewer-element) - 嵌入 PDF.js 默认查看器的自定义元素。
- [`<phantom-ui>`](https://github.com/Aejkatappaja/phantom-ui) - 骨架加载器，测量真实 DOM 以渲染匹配的闪光占位符。
- [`<player-x>`](https://github.com/playerxo/playerx) - 媒体播放器 Web 组件。
- [`<progressive-image>`](https://github.com/andreruffert/progressive-image-element) - 自定义元素可逐步增强图像占位符。
- [`<qr-code>`](https://github.com/bitjson/qr-code) - 用于渲染可定制、可动画、基于 SVG 的 QR 代码的 Web 组件。
- [`<range-slider>`](https://github.com/andreruffert/range-slider-element) - 具有键盘支持的可访问范围滑块自定义元素。
- [`<rapi-doc>`](https://github.com/mrin9/RapiDoc) - 用于根据 OpenAPI 规范创建文档的 Web 组件。
- [`<shader-doodle>`](https://github.com/halvves/shader-doodle) - 用于编写和渲染着色器的 Web 组件。
- [`<theme-switch>`](https://github.com/mahozad/theme-switch) - 动画切换按钮可在浅色、深色和系统主题之间切换。
- [`<trix-editor>`](https://github.com/basecamp/trix) - 用于日常写作的富文本编辑器自定义元素。
- [`<vime-player>`](https://github.com/vime-js/vime) - 可定制、可扩展、可访问且与框架无关的媒体播放器。
- [`<web-vitals>`](https://github.com/stefanjudis/web-vitals-element) - 使用自定义元素将 [webvitals](https://github.com/GoogleChrome/web-vitals) 快速引入您的页面。

### 组件库

- [AgnosticUI](https://github.com/AgnosticUI/agnosticui) - 基于 CLI 的 UI 组件库，可将 Lit Web 组件直接复制到您的项目中。用于本机框架体验的完整 React 和 Vue 包装器。
- [AMP](https://github.com/ampproject/amphtml) - Web 组件框架，用于轻松创建用户至上的网站、故事、广告、电子邮件等。
- [AnywhereUI](https://github.com/adaleks/anywhere-ui) - 包含框架绑定的丰富 Web 组件的集合。使用 StencilJS 创建。
- [Apollo Elements](https://github.com/apollo-elements/apollo-elements) - 用于将 Apollo GraphQL 与各种 Web 组件库结合使用的自定义元素。
- [AXA Pattern Library](https://github.com/axa-ch-webhub-cloud/pattern-library) - 使用 Web 组件构建的 AXA CH UI 组件库。
- [Blackstone UI](https://github.com/kjantzer/bui) - Blackstone Publishing 用于创建界面的 Web 组件。
- [Blaze UI Atoms](https://github.com/BlazeSoftware/atoms) - 由 Blaze CSS 提供支持的 Web 组件集。
- [Brightspace UI core](https://github.com/BrightspaceUI/core) - 用于构建 Brightspace 应用程序的 Web 组件集合。
- [Burnish Components](https://github.com/danfking/burnish/tree/main/packages/components) - 用于将 MCP 工具调用输出呈现为 UI 的 Web 组件。
- [Clever components](https://github.com/CleverCloud/clever-components) - 由 Clever Cloud 制作的 Web 组件集合。
- [Curvenote](https://github.com/curvenote/article) - 用于创建交互式科学文章的 Web 组件。
- [DataFormsJS](https://github.com/dataformsjs/dataformsjs) - 用于 SPA 路由、显示来自 Web 服务的数据等的独立组件。
- [Dile Components](https://github.com/Polydile/dile-components) - 一般用于网站和应用程序的 Web 组件。
- [elements-sk](https://github.com/google/elements-sk) - 用于“点菜”Web 开发的自定义元素集合。
- [github-elements](https://github.com/github/github-elements) - GitHub 的 Web 组件集合。
- [Elix](https://github.com/elix/elix) - 适用于常见用户界面模式的高质量、可定制的 Web 组件。
- [Furo Webcomponents](https://github.com/eclipse/eclipsefuro-web) - 企业级 Web 组件集，最适合与 Eclipse Furo 配合使用。
- [Fusion Web Components](https://github.com/equinor/fusion-web-components) - Equinor Fusion 使用的 Web 组件系列。
- [Ignite UI Web Components](https://github.com/IgniteUI/igniteui-webcomponents) - Infragistics 的完整 UI 组件库。
- [Immersive Custom Elements](https://github.com/MozillaReality/immersive-custom-elements) - 用于嵌入沉浸式（VR 和 AR）内容的 Web 组件集。
- [Joomla UI custom elements](https://github.com/joomla-projects/custom-elements) - Joomla 4 自定义元素的编译。
- [Ketch.UP](https://github.com/smeup/ketchup) - Sme.UP 的 Web 组件库。
- [LDRS](https://github.com/GriffinJohnston/ldrs) - 轻量级、可定制的加载动画/旋转器。
- [Lion Web Components](https://github.com/ing-bank/lion) - 一组高性能、可访问且灵活的 Web 组件。
- [LRNWebComponents](https://github.com/elmsln/lrnwebcomponents/) - ELMS:LN 为任何项目生产 Web 组件。
- [Lume](https://github.com/lume/lume) - 3D 图形的自定义元素。使用 Three.js 构建用于 WebGL/WebGPU 渲染，并使用 Solid.js 构建反应性和模板。
- [Medblocks UI](https://github.com/medblocks/medblocks-ui) - 用于快速开发 openEHR 和 FHIR 系统的 Web 组件。
- [Microsoft Graph Toolkit](https://github.com/microsoftgraph/microsoft-graph-toolkit) - Microsoft Graph 的 Web 组件集合。
- [Mutation testing elements](https://github.com/stryker-mutator/mutation-testing-elements) - 突变测试结果的架构，并通过 Web 组件对其进行可视化。
- [Nightingale](https://github.com/ebi-webcomponents/nightingale) - 适用于生命科学的数据可视化 Web 组件。
- [Nuxeo Elements](https://github.com/nuxeo/nuxeo-elements) - 用于使用 Web 组件通过 Nuxeo 构建 Web 应用程序的组件。
- [One Platform Components](https://github.com/1-Platform/op-components) - Red Hat One Platform 的一组 Web 组件。
- [Open Business Application Platform Web Components](https://github.com/openbap/obap-elements) - 为业务应用程序设计的 Web 组件的集合。
- [Pixano Elements](https://github.com/pixano/pixano-elements) - 专用于数据注释任务的可重用 Web 组件。
- [Playground Elements](https://github.com/PolymerLabs/playground-elements) - 使用 Web 组件的无服务器代码体验。
- [Shoelace](https://github.com/shoelace-style/shoelace) - 具有前瞻性的 Web 组件库。
- [Smart Web Components](https://github.com/HTMLElements/smart-webcomponents) - 用于业务应用程序的 Web 组件。
- [Stripe Elements](https://github.com/bennypowers/stripe-elements) - Stripe.js v3 元素的自定义元素包装器。
- [TEI Publisher Components](https://github.com/eeditiones/tei-publisher-components) - TEI Publisher 使用的 Web 组件及其生成的应用程序的集合。
- [Titanium Elements](https://github.com/LeavittSoftware/titanium-elements) - Leavitt Group Enterprises 使用的轻量级 Web 组件集合。
- [Tradeshift Elements](https://github.com/Tradeshift/elements) - 可重复使用 Tradeshift UI 组件作为 Web 组件。
- [TrendChart Elements](https://github.com/WebLogin/trendchart-elements) - 用于生成简单、轻便且响应灵敏的图表的组件。
- [Umbraco UI Components](https://github.com/umbraco/Umbraco.UI) - Umbraco CMS 的用户界面 Web 组件集合。
- [Vaadin components](https://github.com/vaadin/web-components) - 用于构建业务 Web 应用程序的一组不断发展的高质量 Web 组件。
- [VSCode Webview Elements](https://github.com/bendera/vscode-webview-elements) - 用于创建使用 Webview API 的 VSCode 扩展的组件。
- [Warp View](https://github.com/senx/warpview) - Warp 10 的图表 Web 组件集合。
- [Webmarkets web components](https://github.com/Webmarkets/wm-web-components) - Webmarkets 的公共 Web 组件集。
- [Wired Elements](https://github.com/wiredjs/wired-elements) - 一组常见的 UI 元素，具有手绘、粗略的外观。
- [Wokwi Elements](https://github.com/wokwi/wokwi-elements) - 用于 Arduino 和各种电子零件的 Web 组件。
- [XWeather](https://github.com/kherrick/x-weather) - 实现 OpenWeatherMap API 部分的 Web 组件集合。

### 设计系统

- [Astro Space UX Design System](https://github.com/RocketCommunicationsInc/astro) - 一组组件，用于通过既定的交互模式构建丰富的空间应用程序体验。
- [Auro Design System](https://auro.alaskaair.com) - 阿拉斯加航空的设计系统致力于理念创新和未来合作。
- [Blueprint UI](https://blueprintui.dev) - 基于 Web 组件的设计系统，具有灵活且轻量级的组件。
- [Bolt Design System](https://github.com/boltdesignsystem/bolt) - Twig 和 Web Component 支持的 UI 组件、可重用的视觉样式和工具。
- [Calcite Components](https://github.com/Esri/calcite-components) - Esri 的 Calcite 设计框架的共享 Web 组件。
- [Carbon Web Components](https://github.com/carbon-design-system/carbon-web-components) - 基于 Web 组件的 Carbon 设计系统变体。
- [Clarity Core Web Components](https://github.com/vmware-clarity/core/tree/main/projects/core) - 来自 Clarity Design System 的 Web 组件套件。
- [Crayons](https://github.com/freshdesk/crayons) - 遵循 Freshworks 设计系统的 Web 组件集合。
- [FAST Components](https://github.com/microsoft/fast/tree/master/packages/web-components) - 基于FAST设计语言的Web组件库。
- [Fluent UI Web Components](https://github.com/microsoft/fluentui/tree/master/packages/web-components) - 支持 Microsoft Fluent 设计语言的 Web 组件库。
- [Forge Components](https://github.com/tyler-technologies-oss/forge) - 遵循 Forge 设计系统的 Web 组件库。
- [GOV.UK Web Components](https://github.com/tgreyuk/govuk-webcomponents) - 使用 GOV.UK 设计系统的一组封装 Web 组件。
- [Helix UI](https://github.com/HelixDesignSystem/helix-ui) - Helix 设计系统的 Web 组件库。
- [Liquid](https://github.com/emdgroup-liquid/liquid) - 基于Liquid Design System的UI组件库。
- [Lyne Components](https://github.com/lyne-design-system/lyne-components) - Lyne 设计系统的构建块基于 Web 组件。
- [Material Web Components](https://github.com/material-components/material-web) - Material Design 作为 Web 组件实现。
- [Momentum UI Web Components](https://github.com/momentum-design/momentum-ui/tree/master/web-components) - 基于 Momentum Design 的 UI 组件集。
- [Nord](https://nordhealth.design) - Nordhealth 的产品、数字体验和品牌设计系统。
- [NuML | NUDE Elements](https://github.com/tenphi/numl) - 基于 Web 组件和运行时 CSS 生成的 HTML 框架和设计系统。
- [NVIDIA Elements](https://github.com/nvidia/elements) - 适用于 AI/ML 工厂、机器人和自动驾驶车辆的设计语言和 UI 代理工具。
- [OutlineJS](https://github.com/phase2/outline) - 基于 Web 组件的设计系统入门套件。
- [PatternFly Elements](https://github.com/patternfly/patternfly-elements) - 基于统一设计套件的灵活且轻量级的 Web 组件集合。
- [Pharos Design System](https://github.com/ithaka/pharos) - JSTOR 的设计系统可创造有凝聚力、支持性且优美的体验。
- [Red Hat Design System](https://github.com/RedHat-UX/red-hat-design-system) - 用于构建红帽品牌统一体验的 Web 组件。
- [Siemens iX Web Components](https://github.com/siemens/ix/tree/main/packages/core) - 实施西门子 iX 设计系统的 Web 组件。
- [Spectrum Web Components](https://github.com/adobe/spectrum-web-components) - 使用 Web 组件构建的 Adob​​e Spectrum 设计语言实现。
- [UI5 Web Components](https://github.com/SAP/ui5-webcomponents) - 一组实施 SAP Fiori 设计指南的可重用 UI 元素。
- [U-M Library Design System](https://design-system.lib.umich.edu) - 密歇根大学图书馆设计系统。
- [Zooplus web components](https://github.com/zooplus/zoo-web-components) - 一组实现 Z+ 商店风格指南的 Web 组件。

### 使用案例

- [我们如何选择使用 StencilJS Web 组件构建我们的设计系统](https://medium.com/8451/how-we-chose-to-build-our-design-system-using-stenciljs-web-components-4878c36743c5)
- [寻找无捆绑包的 React 如何让我找到了 Web 组件](https://www.bryanbraun.com/2020/08/31/how-searching-for-a-bundle-free-react-led-me-to-web-components/)
- [Web 组件非常适合大公司的原因](https://medium.com/@sergicontre/reasons-web-components-are-perfect-for-a-big-company-28790d712ad5)
- [Web 组件非常适合设计系统的 5 个原因](https://ionicframework.com/blog/5-reasons-web-components-are-perfect-for-design-systems/)
- [Web 组件：帮助推动 Web 的秘密成分](https://web.dev/web-components-io-2019/)
- [企业 Web 组件。第 1 部分：Salesforce、Oracle、SAP](https://dev.to/webpadawan/web-components-for-enterprise-part-1-salesforce-oracle-sap-e70)
- [企业 Web 组件。第 2 部分：Nuxeo、Ionic、Vaadin](https://dev.to/webpadawan/web-components-for-enterprise-part-2-nuxeo-ionic-vaadin-22l7)
- [为什么我使用 Web 组件 - 我的用例](https://dev.to/shihn/why-i-use-web-components-my-use-cases-1nip)
- [我们为什么使用 Web 组件](https://viljamis.com/2019/why-we-use-web-components/) 作者：[@viljamis](https://twitter.com/viljamis)
- [我们为什么使用 Web 组件](https://dev.to/ionic/why-we-use-web-components-2c1i) 作者：[@maxlynch](https://twitter.com/maxlynch)

## 图书馆

### 基于类别

- [DNA](https://github.com/chialab/dna) - 渐进式 Web 组件库。
- [element-js](https://github.com/webtides/element-js) - 简单、轻量级的 Web 组件基类，具有漂亮的 API。
- [FAST Element](https://github.com/microsoft/fast/tree/master/packages/web-components/fast-element) - 用于构建高性能、内存高效、符合标准的 Web 组件的轻量级库。
- [Forge Core](https://github.com/tyler-technologies-oss/forge-core) - 构建 Forge Web 组件时使用的构建块和实用程序。
- [Joist](https://github.com/joist-framework/joist) - 一组小型库，旨在向 Web 组件添加最少的内容，以提高您的工作效率。
- [Lit](https://lit.dev) - 用于构建快速、轻量级 Web 组件的简单库。
- [Lightning Web Components](https://github.com/salesforce/lwc) - 速度极快的企业级 Web 组件基础。
- [Lume Element](https://github.com/lume/element) - 编写具有由 Solid.js 信号和效果支持的反应性和模板的自定义元素。
- [Omi](https://github.com/Tencent/omi) - 4kb JavaScript 的下一代 Web 框架（Web 组件 + JSX + 代理 + 存储 + 路径更新）。
- [Panel](https://github.com/mixpanel/panel) - Web 组件 + 虚拟 DOM：强大 UI 的 Web 标准。
- [ReadyMade](https://github.com/readymade-ui/readymade/tree/main/src/modules/core) - 使用装饰器编写自定义元素类。没有依赖性。
- [slim.js](https://github.com/slimjs/slim.js) - 基于现代标准的快速、稳健的前端微框架。
- [Stencil](https://github.com/ionic-team/stencil) - 用于生成 Web 组件的编译器。
- [Tonic](https://github.com/optoolco/tonic) - 极简、稳定、审计友好的组件框架。
- [WebCell](https://github.com/EasyWebApp/WebCell) - 基于 VDOM、JSX、MobX 和 TypeScript 的 Web 组件引擎。

### 功能性

- [atomico](https://github.com/atomicojs/atomico) - 用于使用函数和挂钩创建基于 Web 组件的界面的小型库。
- [Elemento](https://github.com/dsolimando/elemento) - 一个轻量级库，用于使用信号和 Lit 构建功能性 Web 组件。
- [haunted](https://github.com/matthewp/haunted) - React 的 Hooks API 为 Web 组件实现。
- [hybrids](https://github.com/hybridsjs/hybrids) - 用于使用简单且功能强大的 API 创建 Web 组件的 UI 库。
- [Solid Element](https://github.com/solidjs/solid/tree/main/packages/solid-element) - 扩展 Solid 添加自定义 Web 组件和扩展的库。

### 集成

- [ember-custom-elements](https://github.com/Ravenstine/ember-custom-elements) - 使用自定义元素渲染 Ember 和 Glimmer 组件。
- [preact-custom-element](https://github.com/preactjs/preact-custom-element) - 从 preact 组件生成/注册自定义元素。
- [@adobe/react-webcomponent](https://github.com/adobe/react-webcomponent) - 自动将 React 组件包装在自定义元素中。
- [nuxt-custom-elements](https://github.com/GrabarzUndPartner/nuxt-custom-elements) - 将项目组件导出为自定义元素，以便集成到外部页面中。
- [react-shadow](https://github.com/Wildhoney/ReactShadow) - 在 React 中利用 Shadow DOM 并享受样式封装的所有好处。
- [reactify-wc](https://github.com/BBKolton/reactify-wc) - 使用具有 React 属性和功能的 Web 组件。
- [remount](https://github.com/rstacruz/remount) - 使用自定义元素将 React 组件安装到 DOM。
- [@riotjs/custom-elements](https://github.com/riot/custom-elements) - 使用 Riot.js 创建普通自定义元素的简单 API。

### 基准测试

- [制作 Web 组件的所有方法](https://webcomponents.dev/blog/all-the-ways-to-make-a-web-component/)
- [web-components-benchmark](https://vogloblinsky.github.io/web-components-benchmark/) - 通过各种示例对 Web 组件技术进行基准测试。
- [web-components-todo](https://wc-todo.firebaseapp.com/) - 出于基准目的，在不同的 Web 组件库中构建了相同的待办事项应用程序。

## 框架

### 角

- [角度元素概述](https://angular.io/guide/elements)
- [将 Angular Elements 作为 Web 组件构建和使用](https://indepth.dev/building-and-bundling-web-components/)
- [如何将 Angular ngModel 和 ngForms 与 WebComponents 结合使用](https://itnext.io/how-to-use-angular-ngmodel-and-ngforms-with-webcomponents-802bd9e1d3d7)
- [在 Angular 中使用 Web 组件](https://coryrylan.com/blog/using-web-components-in-angular)
- [6 步即可使用 Angular Ivy 构建 Web 组件](https://www.softwarearchitekt.at/post/2019/05/18/web-components-custom-elements-with-angular-ivy-in-6-steps.aspx)

### 反应

- [将 React 与自定义元素集成的 3 种方法](https://css-tricks.com/3-approaches-to-integrate-react-with-custom-elements/)
- [构建甚至可以与 React 一起使用的可互操作的 Web 组件](https://css-tricks.com/building-interoperable-web-components-react/)
- [使用自定义元素渲染 React 组件](https://guillaumebriday.fr/rendering-react-components-with-custom-elements)
- [如何在 React 中使用 Web 组件](https://www.robinwieruch.de/react-web-components)
- [将 Web 组件与 Next（或任何 SSR 框架）一起使用](https://css-tricks.com/using-web-components-with-next-or-any-ssr-framework/)

### 维埃

- [在 Vue 中使用 Web 组件](https://coryrylan.com/blog/using-web-components-in-vue)

### 斯韦尔特

- [Svelte 自定义元素 API](https://svelte.dev/docs#Custom_element_API)
- [如何在 Svelte 中创建 Web 组件](https://dev.to/silvio/how-to-create-a-web-components-in-svelte-2g4j)
- [Svelte Web 组件 — 5.4KB](https://itnext.io/svelte-web-component-5-4kb-4afe46590d99)

## 生态系统

## 元框架

- [AMP](https://github.com/ampproject/amphtml) - Web 组件框架可轻松创建用户优先的 Web 体验。
- [Enhance](https://enhance.dev/docs/) - 基于 Web 标准的 HTML 框架，用于构建轻量级 Web 应用程序。
- [luna-js](https://github.com/webtides/luna-js) - SSR 框架使使用 WebComponents 标准变得轻而易举。
- [Rocket](https://rocket.modern-web.dev) - 带有少量 JavaScript 的静态网站的现代 Web 设置。
- [Web Components Compiler](https://github.com/ProjectEvergreen/wcc) - 编译器使本机 Web 组件的服务器端渲染更加容易。
- [WebC](https://github.com/11ty/webc) - 独立于框架的独立 HTML 序列化器，用于生成 Web 组件的标记。

### 入门套件

- [Create Open Web Components](https://open-wc.org/docs/development/generator/) - Web 组件项目脚手架。
- [custom-element-boilerplate](https://github.com/github/custom-element-boilerplate) - 用于创建自定义元素的样板。
- [hello-web-components](https://github.com/fernandopasik/hello-web-components) - 用 TypeScript 编写的简单入门 hello world Web 组件。
- [nutmeg](https://github.com/abraham/nutmeg) - 构建、测试和发布带有一点趣味的普通 Web 组件。

### 测试解决方案

- [capybara-shadowdom](https://github.com/yuki24/capybara-shadowdom) - Ruby gem 为 Capybara 添加了对 Shadow DOM 的基本支持。
- [Cypress component tests for Lit](https://dev.to/simonireilly/cypress-component-tests-for-lit-elements-web-components-45oj) - 如何使用 Cypress 运行 Lit Web 组件的组件测试。
- [cypress-lit](https://github.com/simonireilly/cypress-lit) - 使用所有现代浏览器在 Cypress 中测试您的 Lit 元素和本机 Web 组件。
- [Developing Components: Testing](https://open-wc.org/guides/developing-components/testing/) - 使用 @web/test-runner 在真实浏览器中测试 Web 组件。
- [How To Automate Shadow DOM In Selenium WebDriver](https://www.lambdatest.com/blog/shadow-dom-in-selenium/) - 在 Maven 项目中使用 Selenium WebDriver 定位 Shadow DOM 元素。
- [Native Automation support for Shadow DOM](https://staleelement.medium.com/native-automation-support-for-shadow-dom-with-webdriverio-and-cypress-chapter-3-26249a589f5e) - Shadow DOM 和开源测试框架。
- [Open Web Components: Testing](https://open-wc.org/docs/testing/testing-package/) - 组合和配置测试库的固定包。
- [query-selector-shadow-dom](https://github.com/webdriverio/query-selector-shadow-dom) - querySelector 可以穿透 Shadow DOM 根，对于自动化测试很有用。
- [shadow-automation-selenium](https://github.com/sukgu/shadow-automation-selenium) - 使用 Selenium 实现 Shadow DOM 自动化。
- [Testing Shadow DOM elements in Selenium](https://reflect.run/articles/testing-shadow-dom-elements-in-selenium/) - 在 Selenium 4 中，现在有一种访问 Shadow DOM 节点的方法。
- [Test web components with Playwright](https://alexbilson.dev/plants/technology/test-web-components-with-playwright/) - 现在您已经创建了一两个本机 Web 组件。如何在流行的浏览器中测试它们？
- [W3C Webdriver conquering automation of Shadow DOM](https://staleelement.medium.com/w3c-webdriver-conquering-automation-of-shadow-dom-chapter-2-d92c7fe9e74c) - Shadow DOM 树及其与 W3C Webdriver 的交互。

### 工具

- [Backlight](https://backlight.dev/) - Backlight 注重开发人员和设计人员之间的协作，是一个非常完整的编码平台，团队可以在其中构建、记录、发布、扩展和维护设计系统。
- [Custom Elements Locator](https://github.com/open-wc/locator) - 用于查找页面上的自定义元素的 Chrome 扩展。
- [@storybook/web-components](https://www.npmjs.com/package/@storybook/web-components) - 用于普通 Web 组件片段的 UI 开发环境。
- [webcomponents.dev](https://webcomponents.dev) - 面向 Web 平台开发人员的组件 IDE。
- [web-component-analyzer](https://github.com/runem/web-component-analyzer) - CLI 用于分析 Web 组件并发出文档/诊断信息。
- [Web Components Codemods](https://github.com/kcmr/web-components-codemods) - Web 组件的 Codemods。

## 书籍

- [Web Components in Action](https://www.manning.com/books/web-components-in-action) - 本·法雷尔 (Ben Farrell) 所著的书，可在曼宁早期发行计划中购买。
- [Web Component Development with Modern Libraries and Tooling](https://www.manning.com/books/web-component-development-with-modern-libraries-and-tooling) - 马克·沃尔克曼 (Mark Volkmann) 所著书籍，可在曼宁早期访问计划中获取。
- [Web Component Essentials](https://leanpub.com/web-component-essentials) - Cory Rylan 所著的书，早期预览版可在 Leanpub 购买。

## 教程

- [使用 Vanilla JavaScript 构建 Web 组件](https://dev.to/aspittel/building-web-components-with-vanilla-javascript--jho)
- [从头开始创建自定义元素](https://css-tricks.com/creating-a-custom-element-from-scratch/)
- [创建可重用的 Avatar Web 组件](https://marcoslooten.com/blog/creating-a-reusable-avatar-web-component/)
- [使用 Stencil 创建 Web 组件](https://auth0.com/blog/creating-web-components-with-stencil/)
- [使用 Shadow DOM 封装样式和结构](https://css-tricks.com/encapsulating-style-and-structure-with-shadow-dom/)
- [LitElement 和 TypeScript 入门](https://labs.thisdot.co/blog/getting-started-with-litelement-and-typescript)
- [Web 组件：从零到英雄](https://dev.to/thepassle/web-components-from-zero-to-hero-4n4m)
- [深入探讨：Web 组件和依赖注入 – 实验](https://www.thinktecture.com/web-components/dependency-injection/)
- [使用 Web 组件处理数据](https://itnext.io/handling-data-with-web-components-9e7e4a452e6e)
- [如何将 D3js 与 WebComponent 结合使用](https://towardsdatascience.com/how-to-use-d3js-with-webcomponents-a75ae4f980de)
- [使用 Vaadin Router、LitElement 和 TypeScript 的导航生命周期](https://labs.thisdot.co/blog/navigation-lifecycle-using-vaadin-router-litelement-and-typescript)
- [使用 SVG 和 `<lit-element>` 重新创建 Arduino 按钮](https://www.smashingmagazine.com/2020/01/recreating-arduino-pushbutton-svg/)
- [使用 LitElement 和 TypeScript 进行路由管理](https://labs.thisdot.co/blog/routing-management-with-litelement)
- [使用 Omi 的 Web 组件和 MVP 架构制作吃蛇游戏](https://dev.to/dntzhang/snake-eating-game-making-with-web-components-of-omi-and-mvp-architecture-206)
- [Stencil – 类固醇上的 Web 组件](https://www.thinktecture.com/web-components/stenciljs-web-components-on-steroids/)
- [使用现代 Web 组件](https://coryrylan.com/blog/using-modern-web-components)
- [在 WordPress 中使用 Web 组件比您想象的要容易](https://css-tricks.com/using-web-components-in-wordpress-is-easier-than-you-think/)
- [Web 组件 101：框架比较](https://coderpad.io/blog/development/web-components-101-framework-comparison/)
- [Web 组件 101：Lit 框架](https://coderpad.io/blog/development/web-components-101-lit-framework/)
- [Web 组件工具：比较](https://www.nexmo.com/blog/2020/05/20/web-components-tools-a-comparison)
- [从哪里开始构建 Web 组件？ - 基础知识](https://dev.to/alangdm/where-to-begin-building-web-components-the-basics-3b78)
- [从哪里开始构建 Web 组件？ - 基于类的库](https://dev.to/alangdm/where-to-begin-building-web-components-class-based-libraries-18m6)

## 见解

### 播客

- [Code[ish]，第 38 集：使用 Web 组件构建](https://www.heroku.com/podcasts/codeish/38-building-with-web-components)
- [前端欢乐时光，第 62 集：Web 组件 - 影子 DOM 的镜头](https://frontendhappyhour.com/episodes/web-components-shots-of-shadow-dom/)
- [实验室讲座 - Peter Muessig 的 Web 组件](https://labstalk.buzzsprout.com/993481/3932975-web-components-with-peter-muessig)
- [Real Talk JavaScript，第 7 集：Rob Wormald 的自定义 Web 组件](https://realtalkjavascript.simplecast.fm/eaf3db9e)
- [Real Talk JavaScript，第 101 集：使用本机 HTML 和 LitElement 回归基础](https://realtalkjavascript.simplecast.com/episodes/episode-101-back-to-basics-with-native-html-and-litelement)

### 演讲

- [Web 组件是 Web 开发的 Betamax 吗？](https://noti.st/lostinbrittany/EjUZyd/are-web-components-the-betamax-of-web-development) 作者：[@lostinbrittany](https://twitter.com/lostinbrittany)
- [设计标准系统](https://drive.google.com/file/d/1ALFiWOFU0UAGUpaZPMIVnoADs9_REtL5/view) 作者：[@stefsull](https://twitter.com/stefsull) 和 [@bferrua](https://twitter.com/bferrua)
- [可扩展设计系统的前端架构](https://events.drupal.org/seattle2019/sessions/design-system-architecture-pattern-lab-twig-and-web-components) 作者：[@salem_cobalt](https://twitter.com/salem_cobalt)
- [lit-apollo：使用该平台的数据驱动组件](https://apolloelements.dev/using-lit-apollo/) 作者：[@PowersBenny](https://twitter.com/PowersBenny)
- [掌握 Shadow DOM](https://martine-dowden.github.io/portfolio/presentation/mastering-shadow-dom) 作者：[@Martine_Dowden](https://twitter.com/Martine_Dowden)
- [使用 Web 组件现代化大型前端](https://speakerdeck.com/samjulien/modernizing-large-frontends-with-web-components) 作者：[@samjulien](https://twitter.com/samjulien)
- [Shadow DOM：人迹罕至的地方](https://docs.google.com/presentation/d/1wi74YiTLtLSfgjyccKm5LxYp9k8aeJda0AekWV5mqJI/edit?usp=sharing) 作者：[@serhiikulykov](https://twitter.com/serhiikulykov)
- [使用 Web 组件构建与框架无关的 UI 库](https://gotochgo.com/2019/sessions/866/using-web-components-to-build-a-framework-agnostic-ui-library) 作者：[@brianbouril](https://twitter.com/brianbouril) 和 [@danciupuliga](https://twitter.com/danciupuliga)
- [Web 组件和 AOM](https://decks.tink.uk/2019/jsconf/index.html) 作者：[@LeonieWatson](https://twitter.com/LeonieWatson)
- [Web 组件和样式范围](https://www.dropbox.com/s/wdh9uufjui5htll/Web-Components-and-Styles-Scoping-by-bashmish-FrontMania-2018.pdf) 作者：[@bashmish](https://twitter.com/bashmish)
- [Web Components 可以做到这一点？！](https://slides.com/vogloblinsky/web-components-can-do-that) 作者：[@vogloblinsky](https://twitter.com/vogloblinsky)
- [Web 组件：介绍和最新技术](https://webcomponents.dev/blog/web-components-slides/) 作者：[@webcomp_dev](https://twitter.com/webcomp_dev)

### 会谈

- [更好的应用程序：以 Web 组件的形式提供通用 UI 模式](https://youtu.be/mtHf7crZZIQ) 作者：[@janmiksovsky](https://twitter.com/janmiksovsky)
- [自定义 Web 阴影元素，或其他......](https://vimeo.com/364370506) 作者：[@aerotwist](https://twitter.com/aerotwist)
- [样式和主题 Web 组件](https://youtu.be/FM7ROEVPA4k) 作者：[@justinfagnani](https://twitter.com/justinfagnani)
- [企业规模的 Web 组件](https://youtu.be/iFp-P2UJT_Y) 作者：[@diervo](https://twitter.com/diervo)

## 使用指标

- [Chrome 平台状态：“CustomElementRegistryDefine”](https://chromestatus.com/metrics/feature/timeline/popularity/1689)
- [Chrome 平台状态：“ElementAttachShadow”](https://chromestatus.com/metrics/feature/timeline/popularity/804)
- [Chrome 平台状态：“HTMLTemplateElement”](https://chromestatus.com/metrics/feature/timeline/popularity/2769)

## 提案

### 表单关联的自定义元素

- [Form Participation API Explained](https://docs.google.com/document/d/1JO8puctCSpW-ZYGU8lF-h4FWRIDQNDVexzHoOQ2iQmY/edit?usp=sharing) - Google Chrome 团队的文档。
- [Form-associated custom elements](https://www.chromestatus.com/features/4708990554472448) - Chrome 平台状态中的功能。
- [web-platform-tests](https://github.com/web-platform-tests/wpt/tree/master/custom-elements/form-associated)

### 可构造的样式表对象

- [规范草案](https://wicg.github.io/construct-stylesheets/)
- [web-platform-tests](https://github.com/web-platform-tests/wpt/blob/master/css/cssom/CSSStyleSheet-constructable.html)
- [Explainer](https://github.com/WICG/construct-stylesheets/blob/gh-pages/explainer.md)
- [Constructable Stylesheets](https://www.chromestatus.com/feature/5394843094220800) - Chrome 平台状态中的功能。

### 自定义状态伪类

- [闪烁：意图实施](https://groups.google.com/a/chromium.org/forum/#!topic/blink-dev/CApU9QIu3TM)
- [`ElementInternals` 的 `states` 属性和 `:state()` 伪类](https://github.com/w3c/webcomponents/blob/gh-pages/proposals/custom-states-and-state-pseudo-class.md)

## 杂项

- [bruck](https://github.com/Heydon/bruck) - 使用 Web 组件和 Houdini Paint API 构建的原型系统。
- [Vaadin Directory](https://vaadin.com/directory) - 发布、讨论和评价 Web 组件
- [webcomponents.org](http://webcomponents.org/) - 讨论&amp;共享网络组件。

## 存档

### 聚合物填料

现代浏览器支持 Web 组件标准，而无需使用下面列出的任何 Polyfill。
唯一值得注意的例外是自定义的内置元素被 WebKit (Safari) 拒绝。

#### 自定义元素polyfill

- [@webcomponents/custom-elements](https://github.com/webcomponents/polyfills/tree/master/packages/custom-elements) - Polymer 团队的自定义元素 polyfill。
- [document-register-element](https://github.com/WebReflection/document-register-element) - Andrea Giammarchi 的自定义元素 polyfill。

#### 定制的内置元素polyfill

- [@corpuscule/custom-builtin-elements](https://github.com/corpusculejs/custom-builtin-elements) - 由[CorpusculeJS](https://github.com/corpusculejs)定制的内置元素polyfill。
- [@ungap/custom-elements-builtin](https://github.com/ungap/custom-elements-builtin) - 由[ungap项目](https://ungap.github.io)定制的内置元素polyfill。

#### Shadow DOM 垫片

- [@webcomponents/shadydom](https://github.com/webcomponents/polyfills/tree/master/packages/shadydom) - ShadowDOM v1 垫片。
- [@webcomponents/shadycss](https://github.com/webcomponents/polyfills/tree/master/packages/shadycss) - ShadowDOM 风格的封装垫片。
- [@lwc/synthetic-shadow](https://github.com/salesforce/lwc/blob/master/packages/@lwc/synthetic-shadow) - Shadow DOM polyfill 由 [LWC](https://lwc.dev) 提供。

#### HTML 模板 polyfill

- [@webcomponents/template](https://github.com/webcomponents/polyfills/tree/master/packages/template) - `<template>` 的最小填充。
- [@ungap/import-node](https://github.com/ungap/import-node) - [ungap 项目](https://ungap.github.io) 的 IE11 的“importNode”polyfill。

### 历史

下面的文章讲述了 Web 组件规范走向标准化的漫长故事。
其中一些引用了早期所谓的“v0”Shadow DOM 和自定义元素规范，并放弃了 HTML 导入规范。
这些材料仅出于历史原因放在这里，它们按年份分组并按时间顺序列出。

#### 2019

- [HTML slot 元素的历史](https://component.kitchen/blog/posts/a-history-of-the-html-slot-element)
- [跨框架组件库的 Web 组件](https://codeburst.io/web-components-for-cross-framework-component-libraries-2647741f9470)
- [2019 年 Web 组件：第 1 部分](https://codeburst.io/web-components-in-2019-part-1-6bd7251edce5)
- [2019 年 Web 组件：第 2 部分](https://codeburst.io/web-components-in-2019-part-2-a7de8c770c5a)
- [2019 年 Web 组件：第 3 部分](https://codeburst.io/web-components-in-2019-part-3-e725b781a414)
- [2019 年 Web 组件：第 4 部分](https://codeburst.io/web-components-in-2019-part-4-7fe8e63a4dee)
- [2019 年令我兴奋的 Web 组件发展](https://medium.com/angular-in-depth/developments-in-web-components-im-excited-about-in-2019-3ae7751c2f64)

#### 2018

- [设计可访问性：Web 组件方法](https://medium.com/@cfscorreia/styling-accessibility-a-web-components-approach-dc2aa8123eb2)
- [Web 组件 101：Web 组件简介](https://www.telerik.com/blogs/web-components-101-an-introduction-to-web-components)
- [Vue Web 组件入门](https://medium.com/@royprins/get-started-with-vue-web-components-593b3d5b3200)
- [您应该使用本机 Web 组件的 6 个原因](https://codeburst.io/6-reasons-you-should-use-native-web-components-b45e18e069c2)
- [2018 年 Web 组件](https://www.sitepen.com/blog/web-components-in-2018)
- [Web 组件简介：2018 年创建自定义 HTML 元素](https://www.grapecity.com/en/blogs/web-components-introduction-creating-custom-html-elements-2018)
- [使用 Vue CLI 3 创建和发布 Web 组件](https://vuejsdevelopers.com/2018/05/21/vue-js-web-component/)
- [使用 Web 组件扩展原生 DOM 元素](https://medium.com/revillweb/extending-native-dom-elements-with-web-components-233350c8e86a)

#### 2017

- [样式对于 Web 组件重用至关重要，但在实践中可能会很困难](https://component.kitchen/blog/posts/styling-is-critical-to-web-component-reuse-but-may-prove-difficult-in-practice)
- [Web 组件：漫长的游戏](https://infrequently.org/2017/10/web-components-the-long-game/)
- [Web 组件：恰逢其时（聚合物峰会 2017）](https://youtu.be/y-8Lmg5Gobw)
- [在 Ionic 中使用 Web 组件（聚合物峰会 2017）](https://youtu.be/UfD-k7aHkQE)
- [VR 网络组件（聚合物峰会 2017）](https://youtu.be/8GmTu2JF4-0)
- [使用 Web 组件构建企业规模的 UI（Polymer Summit 2017）](https://youtu.be/FJ2KEvzlyo4)
- [定制元素无处不在（聚合物峰会 2017）](https://youtu.be/sK1ODp0nDbM)
- [发展下一代聚合物元件（聚合物峰会 2017）](https://youtu.be/rvpJ5O0W_6A)
- [聚合物 @ YouTube（聚合物峰会 2017）](https://youtu.be/tNulrEbTQf8)
- [CMS 的 Web 组件（聚合物峰会 2017）](https://youtu.be/c-WDHG6rrdU)
- [水獭 Web 组件简介](https://meowni.ca/posts/web-components-with-otters/)
- [Web 组件兑现的承诺](https://dmitriid.com/blog/2017/03/the-broken-promise-of-web-components/)
- [关于 Web 组件的失信](http://robdodson.me/regarding-the-broken-promise-of-web-components/)
- [Web Components v1 - 下一代](https://web.dev/webcomponents-org/)

#### 2016

- [引入自定义元素](https://webkit.org/blog/7027/introducing-custom-elements/)
- [自定义元素案例：第 1 部分](https://medium.com/dev-channel/the-case-for-custom-elements-part-1-65d807b4b439)
- [自定义元素案例：第 2 部分](https://medium.com/dev-channel/the-case-for-custom-elements-part-2-2efe42ce9133)
- [揭秘 Web 组件](http://www.backalleycoder.com/2016/08/26/demythstifying-web-components/)
- [可扩展的网络组件](https://adactio.com/journal/11052)
- [Web 组件的挑战](https://blog.revillweb.com/web-component-challenges-a09ebc598d65)
- [Web 组件和渐进增强](https://onishi.ltd/articles/2016/08/web-components-and-progressive-enhancement/)
- [Shadow DOM 和自定义元素标准化更新](https://annevankesteren.nl/2015/07/shadow-dom-custom-elements-update)
- [Shadow DOM v1 的新增功能（通过示例）](https://hayatoito.github.io/2016/shadowdomv1/)
- [为什么 Web 组件如此重要](https://blog.revillweb.com/why-web-components-are-so-important-66ad0bd4807a)
- [了解 Web 组件](https://medium.com/the-ui-files/understanding-web-components-d051baa66019)

#### 2015

- [引入基于槽的 Shadow DOM API](https://webkit.org/blog/4096/introducing-shadow-dom-api/)
- [有一个元素可以做到这一点](https://medium.com/synsugar/there-is-an-element-for-that-a9fcdafe4a25)
- [Web 组件发生了什么？](https://2ality.com/2015/08/web-component-status.html)
- [Web 组件及其在未来 Web 开发中的作用](http://kaytcat.github.io/web-components/)
- [Microsoft Edge 和 Web 组件](https://blogs.windows.com/msedgedev/2015/07/15/microsoft-edge-and-web-components/)
- [将组件化引入 Web：Web 组件概述](https://blogs.windows.com/msedgedev/2015/07/14/bringing-componentization-to-the-web-an-overview-of-web-components/)
- [为什么 Web Components 将使网络成为我们用户更美好的地方](https://medium.com/@kaelig/why-web-components-will-make-the-web-a-better-place-for-our-users-38dc3154fc1d)
- [围绕 Web 组件的实际问题](https://www.ianfeather.co.uk/practical-questions-around-web-components/)
- [Web 组件的状态](https://hacks.mozilla.org/2015/06/the-state-of-web-components/)

#### 2014

- [Web 组件简明指南，第 1 部分：规格](http://cbateman.com/blog/a-no-nonsense-guide-to-web-components-part-1-the-specs/)
- [Web 组件简明指南，第 2 部分：实际使用](http://cbateman.com/blog/a-no-nonsense-guide-to-web-components-part-2-practical-use/)
- [Web 组件 + 主干：改变游戏规则的组合](https://youtu.be/dztuKgjk0Bg)
- [Mozilla 和 Web 组件：更新](https://hacks.mozilla.org/2014/12/mozilla-and-web-components/)
- [由 Web 组件提供支持的无服务器应用程序](https://youtu.be/MdcD1rNkNLE)
- [Web 组件和 CSS 的未来](https://youtu.be/QHxrr6Q82yI)
- [使用 Web 组件轻松组合和重用](https://youtu.be/6vcQlD-jadk)
- [让我们用 Polymer 构建一些应用程序！](https://youtu.be/kV0hgdMpH28)
- [聚合物：国情咨文](https://youtu.be/0LT6W5QVCJI)
- [Web Components 101：HTML 基本变化简介](https://youtu.be/hEzmy93zr0Y?t=540)
- [Web 组件 201：设计可重用的 Web 组件](https://youtu.be/dwxaG-eoxdU)
- [为什么使用 Web 组件——Web 真的需要另一个组件吗？](https://medium.com/@shaunwalla/why-web-components-does-the-web-really-need-another-component-4af010b6446)
- [“不要停止思考明天”——AngularJS 和 Web 组件](https://youtu.be/gSTNTXtQwaY)
- [具有 Web 组件的多设备应用程序](https://youtu.be/kn0y7uugO0Y)
- [当我走过 DOM 阴影之谷时](https://youtu.be/nbsWP2cPhhU)
- [为什么 Web 组件已准备好投入生产](https://www.telerik.com/blogs/web-components-ready-production)
- [组件化网络的现状](https://www.leggetter.co.uk/2014/08/06/state-componentised-web.html)
- [为什么 Web 组件尚未做好生产准备的附录](https://www.tjvantoll.com/2014/07/18/an-addendum-to-why-web-components-arent-ready-for-production-yet/)
- [为什么 Web 组件还没有做好生产准备](https://www.telerik.com/blogs/web-components-arent-ready-production-yet)
- [与 React 和自定义元素的组件互操作](https://addyosmani.com/blog/component-interop-with-react-and-custom-elements/)
- [Web 组件的可访问性](https://youtu.be/BgvDZZ8Ms8c)
- [组件化 Web：回到浏览器！](https://youtu.be/GOPXVLxp9Nc)
- [Google I/O 2014 - Polymer 和 Web 组件革命](https://youtu.be/yRbOSdAe_JU)
- [Google I/O 2014 - Polymer 和 Web Components 改变了您对 Web 开发的了解](https://youtu.be/8OJ7ih8EE7s)
- [Google I/O 2014 - 使用 Polymer 开启 UI 开发的下一个时代](https://youtu.be/HKrYfrAzqFA)
- [让聚合物元素触手可及](https://youtu.be/_IBiXfxhF-A)
- [使用 Web 组件构建可访问的披露按钮](https://developer.paciellogroup.com/blog/2014/06/accessible-disclosure-button-using-web-components/)
- [Web 组件之路](https://youtu.be/yLyyXHhSl8w)
- [Web 组件革命已经到来](https://youtu.be/3QLmAm9xtnU)
- [Web 组件：创造未来的机会](https://youtu.be/JUzjr1bIRUg)
- [凌晨 3 点 Web 组件混搭](https://youtu.be/75EuHl6CSTo)
- [Web 组件工具和库](https://youtu.be/iPmN4CvLGJc)
- [Web 组件可以做到这一点吗？！](https://addyosmani.com/fitc-wccdt/)
- [Web Components 和你——要避免的危险](https://christianheilmann.com/2014/04/18/web-components-and-you-dangers-to-avoid/)
- [HTML 作为自定义元素](https://github.com/domenic/html-as-custom-elements)
- [Web 的声明式、可组合的未来](https://addyosmani.com/blog/the-webs-declarative-composable-future/)
- [使用 Polymer 创建 Web 组件](https://code.tutsplus.com/tutorials/using-polymer-to-create-web-components--cms-20475)
- [Shadow DOM 日记](https://gist.github.com/dglazkov/efd2deec54f65aa86f2e)
- [自定义元素详细介绍](https://www.smashingmagazine.com/2014/03/introduction-to-custom-elements/)

#### 2013

- [称为 Web 组件的未来](https://speakerdeck.com/zenorocha/a-future-called-web-components)
- [使用 Brick 构建移动 Web 应用程序](https://youtu.be/dW2ib0bkxGQ)
- [Polymer：声明式、封装式和可重用的 Web 组件](https://youtu.be/DH1vTVkqCDQ)
- [Web 组件：为什么您已经是专家](https://youtu.be/s1PTPZwzQA4)
- [Yo Polymer：构建网络应用程序的新方法](https://youtu.be/booRxAJblwM)
- [性能和自定义元素](https://www.stevesouders.com/blog/2013/11/26/performance-and-custom-elements/)
- [Web 组件革命](https://robdodson.github.io/webcomponents-revolution/)
- [Web 组件指南](https://css-tricks.com/modular-future-web-components/)
- [Inspector Web 回归：一年后的 Web 组件](https://vimeo.com/78899868)
- [使用自定义元素](https://web.dev/customelements/)
- [使用 HTML 模板元素创建可重用标记](https://blog.teamtreehouse.com/creating-reusable-markup-with-the-html-template-element)
- [使用 Shadow DOM](https://blog.teamtreehouse.com/working-with-shadow-dom)
- [突破性开发：Web 组件](https://www.lukew.com/ff/entry.asp?1752)
- [Web 组件：Web 开发的结构性转变 - Google I/O 2013](https://youtu.be/fqULJBBEVQE)
- [Web 组件：入门](https://vimeo.com/68212204)
- [影子 DOM 101](https://web.dev/shadowdom/)
- [影子 DOM 201](https://web.dev/shadowdom-201/)
- [影子 DOM 301](https://web.dev/shadowdom-301/)
- [可视化影子 DOM 概念](https://developer.chrome.com/blog/visualizing-shadow-dom-concepts/)
- [Web 组件和 Web 开发的未来](https://youtu.be/pb6DsPNdoXk)
- [HTML 的新模板标签](https://web.dev/webcomponents-template/)

#### 2012

- [Shadow DOM 的基础知识](https://www.sitepoint.com/the-basics-of-the-shadow-dom/)
- [Web 组件 + ARIA 的注释](https://developer.paciellogroup.com/blog/2012/07/notes-on-web-components-aria/)
- [Google I/O 2012 - Web 平台的前沿](https://youtu.be/2txPYQOWBtg)
- [Web 组件简介](https://www.w3.org/TR/2012/WD-components-intro-20120522/)

#### 2011

- [Web 组件和模型驱动视图，作者：Alex Russell](https://fronteers.nl/congres/2011/sessions/web-components-and-model-driven-views-alex-russell)
- [Shadow DOM 到底是什么？](https://glazkov.com/2011/01/14/what-the-heck-is-shadow-dom/)

## 关注谁

<table>
  <tbody>
    <tr>
      <td align="center">
        <a href="https://twitter.com/polymer">
          <img width="80" height="80" src="https://pbs.twimg.com/profile_images/1063502058337136640/RmlG_bbW_80x80.jpg">
          <div>Polymer</div>
        </a>
</td>
<td对齐=“中心”>
        <a href="https://twitter.com/stenciljs">
          <img width="80" height="80" src="https://pbs.twimg.com/profile_images/1135534552137510914/5ZzvOFFp_80x80.png">
          <div>Stencil</div>
        </a>
</td>
<td对齐=“中心”>
        <a href="https://twitter.com/openwc">
          <img width="80" height="80" src="https://pbs.twimg.com/profile_images/1101188623930662912/YKlBD7n6_80x80.png">
          <div>open-wc.org</div>
        </a>
</td>
<td对齐=“中心”>
        <a href="https://twitter.com/webcomp_dev">
          <img width="80" height="80" src="https://pbs.twimg.com/profile_images/1169270943371407360/U-90Bxn0_80x80.jpg">
          <div>webcomponents.dev</div>
        </a>
</td>
</tr>
<tr>
<td对齐=“中心”>
        <a href="https://twitter.com/justinfagnani">
          <img width="80" height="80" src="https://pbs.twimg.com/profile_images/378800000808710206/2dbdaa1cb7b0db02f997aea5b40f29b8_80x80.jpeg">
          <div>Justin Fagnani</div>
        </a>
</td>
<td对齐=“中心”>
        <a href="https://twitter.com/viljamis">
          <img width="80" height="80" src="https://pbs.twimg.com/profile_images/671595827740086273/wCUWq-1S_80x80.png">
          <div>Viljami Salminen</div>
        </a>
</td>
<td对齐=“中心”>
        <a href="https://twitter.com/JanMiksovsky">
          <img width="80" height="80" src="https://pbs.twimg.com/profile_images/675000078055051264/u1ZEQfeE_80x80.jpg">
          <div>Jan Miksovsky</div>
        </a>
</td>
<td对齐=“中心”>
        <a href="https://twitter.com/serhiikulykov">
          <img width="80" height="80" src="https://pbs.twimg.com/profile_images/1028197887329685504/cM6nOHlp_80x80.jpg">
          <div>Serhii Kulykov</div>
        </a>
</td>
</tr>
<正文>
</table>

## 维护者

- 由 [@mateusortiz](https://github.com/mateusortiz) 于 2014 年创建。
- 自 2018 年起由 [@web-padawan](https://github.com/web-padawan) 维护。
