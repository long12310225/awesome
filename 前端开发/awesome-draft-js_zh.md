# 很棒的 Draft.js [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

[Draft.js](https://draftjs.org/) 是一个在 React 中构建富文本编辑器的框架。

**目录**

- [Community](https://github.com/nikgraf/awesome-draft-js#community)
- [Presentations](https://github.com/nikgraf/awesome-draft-js#presentations)
- [基于 Draft.js 的项目](https://github.com/nikgraf/awesome-draft-js#standalone-editors-built-on-draftjs)
- [常用工具](https://github.com/nikgraf/awesome-draft-js#common-utilities)
- [博客文章和文章](https://github.com/nikgraf/awesome-draft-js#blog-posts--articles)
- [现场演示](https://github.com/nikgraf/awesome-draft-js#live-demos)
- [生产中的使用](https://github.com/nikgraf/awesome-draft-js#usage-in-production)
- [License](https://github.com/nikgraf/awesome-draft-js#license)

## 社区

* [松弛通道](https://draftjs.herokuapp.com/)

## 演讲
* [使用 React 进行富文本编辑 @ React.js Conf 2016 作者：Isaac Salier-Hellendag ](https://www.youtube.com/watch?v=feUYwoLhE_4)
* [使用 Nik Graf 的 Draft.js 和 DraftJS 插件进行富文本编辑](https://www.youtube.com/watch?v=gxNuHZXZMgs)
* [反应EP。 37：我今天学到的Draftjs – Atomic Jolt](https://www.youtube.com/watch?v=0k9suXgCtTA)
* [008 - Draft.js 插件 @ React30](https://www.youtube.com/watch?v=w-PqnpMizcQ)
* [HubSpot 上的 Draft.js 作者：Ben Briggs](https://product.hubspot.com/blog/tech-talk-at-night-react-meetup)
* [Draft.js 底层 - React 墨尔本聚会](https://www.youtube.com/watch?feature=player_embedded&v=vOZAO3jFSHI)

## 基于 Draft.js 构建的独立编辑器

* [Draft WYSIWYG](https://github.com/bkniffler/draft-wysiwyg) - 所见即所得编辑器，具有拖放、调整大小和工具提示功能。
* [Draft.js Editor](https://github.com/AlastairTaft/draft-js-editor/) - 受 Medium 和 Facebook Notes 启发的富文本编辑器。
* [React-RTE](https://github.com/sstur/react-rte/) - 类似于 CKEditor 或 TinyMCE 的全功能文本区域替代品。
* [Facebook Notes Clone(ish)](https://github.com/andrewcoelho/react-text-editor) - 类似于 Facebook 笔记的富文本编辑器。
* [Megadraft](https://github.com/globocom/megadraft) - 一个富文本编辑器，具有良好的默认插件基础和可扩展性。
* [Medium Draft](https://github.com/brijeshb42/medium-draft) - 类似于 Medium 的富文本编辑器，专注于键盘快捷键。
* [React-Draft-Wyiswyg](https://github.com/jpuri/react-draft-wysiwyg) - 所见即所得编辑器，具有各种文本编辑选项和相应的 HTML 生成。
* [Dante 2](https://github.com/michelson/dante2) - 只是另一个建立在 DraftJs 之上的 Medium 克隆。
* [Last Draft](https://github.com/vacenz/last-draft) - 使用 Draft.js 插件构建的草稿编辑器。
* [Z-Editor](https://github.com/Z-Editor/Z-Editor) - 在线 Z 符号编辑器。
* [Draftail](https://github.com/springload/draftail/) - 基于 Draft.js 的可配置富文本编辑器，专为 Wagtail 构建。
* [Braft](https://github.com/margox/braft-editor) - 可扩展的 JS 草稿编辑器

## 为 Draft.js 构建的插件和装饰器

* [Draft.js Plugins](https://github.com/draft-js-plugins/draft-js-plugins) - 基于 Draft.js 的插件架构
  - [Alignment](https://www.draft-js-plugins.com/plugin/alignment)
  - [Block Breakout](https://github.com/icelab/draft-js-block-breakout-plugin) - 键入时打破块类型。
  - [Buttons](https://github.com/vacenz/last-draft-js-plugins)
  - [颜色选择器](https://github.com/vacenz/last-draft-js-plugins)
  - [Counter](https://www.draft-js-plugins.com/plugin/counter) - 字符、字数和行数计数。
  - [Divider](https://github.com/simsim0709/draft-js-plugins/tree/master/draft-js-divider-plugin)
  - [拖放](https://www.draft-js-plugins.com/plugin/drag-n-drop)
  - [Embed](https://github.com/vacenz/last-draft-js-plugins)
  - [Emoji](https://www.draft-js-plugins.com/plugin/emoji) - Slack 式的表情符号支持
  - [EmojiPicker](https://github.com/vacenz/last-draft-js-plugins)
  - [Focus](https://www.draft-js-plugins.com/plugin/focus)
  - [GifPicker](https://github.com/vacenz/last-draft-js-plugins)
  - [Hashtags](https://www.draft-js-plugins.com/plugin/hashtag) - 类似 Twitter 的主题标签支持
  - [Image](https://www.draft-js-plugins.com/plugin/image)
  - [内联工具栏](https://www.draft-js-plugins.com/plugin/inline-toolbar)
  - [Katex](https://github.com/letranloc/draft-js-katex-plugin) - 使用 Katex 插入并渲染 LaTeX。
  - [Link](https://github.com/vacenz/last-draft-js-plugins)
  - [Linkify](https://www.draft-js-plugins.com/plugin/linkify) - 自动将链接变成锚标签。
  - [List](https://github.com/samuelmeuli/draft-js-list-plugin) - 自动列表创建、嵌套列表
  - [Markdown Shortcuts](https://github.com/ngs/draft-js-markdown-shortcuts-plugin/) - Markdown 语法快捷方式。
  - [Mathjax](https://github.com/tarjei/draft-js-mathjax-plugin) - 使用 Mathjax 渲染的 (La)TeX 编辑数学。
  - [Mention](https://www.draft-js-plugins.com/plugin/mention) - 类似 Twitter 的提及支持
  - [Modal](https://github.com/vacenz/last-draft-js-plugins)
  - [Prism](https://github.com/withspectrum/draft-js-prism-plugin) - 使用 Prism 语法突出显示代码块。
  - [Resizeable](https://www.draft-js-plugins.com/plugin/resizeable)
  - [RichButtons](https://github.com/jasonphillips/draft-js-richbuttons-plugin) - 添加和自定义丰富的格式按钮。
  - [侧边工具栏](https://www.draft-js-plugins.com/plugin/side-toolbar)
  - [Sidebar](https://github.com/vacenz/last-draft-js-plugins)
  - [Single Line](https://github.com/icelab/draft-js-single-line-plugin) - 限制为单行输入。
  - [Sticker](https://www.draft-js-plugins.com/plugin/sticker) - 类似 Facebook 的贴纸支持
  - [Toolbar](https://github.com/vacenz/last-draft-js-plugins)
  - [Undo](https://www.draft-js-plugins.com/plugin/undo) - 撤消和重做按钮。
  - [Video](https://www.draft-js-plugins.com/plugin/video)
* [Draft.js Gutter](https://github.com/seejamescode/draft-js-gutter) - 赞美行号排水沟。
* [Draft.js Basic HTML Editor](https://github.com/dburrows/draft-js-basic-html-editor) - 接受 html 作为其输入格式，并将 html 返回到 onChange。
* [Draft.js Prism](https://github.com/SamyPesse/draft-js-prism) - 使用 Prism 突出显示代码块。
* [Draft.js Typeahead](https://github.com/dooly-ai/draft-js-typeahead) - 支持预输入功能。
* [Draft Extend](https://github.com/HubSpot/draft-extend) - 使用可配置插件和集成序列化构建可扩展的 Draft.js 编辑器。
* [Draft.js Code](https://github.com/SamyPesse/draft-js-code) - 用于更好的代码编辑的低级实用程序的集合
* [Draft.js Annotatable](https://github.com/cltk/annotations) - 开箱即用的 Draft.js 注释系统，支持用户创建的注释。
* [Draft.js Regex](https://github.com/YozhikM/draft-regex) - 一组灵活的帮助器，如正则表达式、防止空行和粘贴 HTML 清除。

## 常用工具

* [BackDraft.js](https://github.com/evanc/backdraft-js) - 将 rawContentBlock 转换为标记字符串的函数。
* [Draft.js Exporter](https://github.com/rkpasia/draft-js-exporter) - 从 Draft.js 导出内容并设置其格式。
* [Draft.js: Export ContentState to HTML](https://github.com/sstur/draft-js-utils/tree/master/packages/draft-js-export-html) - 将 ContentState 导出为 HTML。
* [Draft.js: Export ContentState to PDFMake](https://github.com/datagenno/draft-js-export-pdfmake) - 将 ContentState 导出到 PDFMake。
* [Redraft](https://github.com/lokiuz/redraft) - 使用提供的回调渲染 Draft.js ConvertToRaw 的结果，与 React 配合良好
* [Draft.js exporter (Ruby)](https://github.com/ignitionworks/draftjs_exporter) - 将 Draft.js 内容状态导出为 HTML。
* [Draft.js exporter (Python)](https://github.com/springload/draftjs_exporter) - 将 Draft.js 原始 ContentState 转换为 HTML 的库
* [Draft.js AST Exporter](https://github.com/icelab/draft-js-ast-exporter) - 将内容导出到抽象语法树 (AST)。
* [Draft.js AST Importer](https://github.com/icelab/draft-js-ast-importer) - 从配套的 Draft-js-ast-exporter 导入抽象语法树 (AST) 输出。
* [Draft.js Multidecorators](https://github.com/SamyPesse/draft-js-multidecorators) - 组合多个装饰器。
* [Draft.js SimpleDecorator](https://github.com/Soreine/draft-js-simpledecorator) - 轻松创建灵活的装饰器。
* [DraftJS Utils](https://github.com/jpuri/draftjs-utils) - DraftJS 的实用函数集。
* [DraftJs to HTML](https://github.com/jpuri/draftjs-to-html) - 用于为 DraftJS 编辑器内容生成 HTML 的库。
* [Draft Convert](https://github.com/HubSpot/draft-convert) - 使用 HTML 可扩展地序列化和反序列化 Draft.js ContentState。
* [HTML to DraftJS](https://github.com/jpuri/html-to-draftjs) - 将纯 HTML 转换为 DraftJS 编辑器内容。
* [Draft.js Exporter (Go)](https://github.com/ejilay/draftjs) - 将 Draft.js 内容状态导出为 HTML。
* [React Native Draft.js Render](https://github.com/globocom/react-native-draftjs-render) - Draft.js 模型的 React Native 渲染。
* [Draft.js filters](https://github.com/thibaudcolas/draftjs-filters) - 过滤 Draft.js 内容以仅保留您允许的格式。
* [Sticky](https://github.com/nadunindunil/sticky) - 一个简单的笔记和剪贴板管理桌面应用程序

## 博客文章和文章

* [Facebook 开源富文本编辑器框架 Draft.js](https://code.facebook.com/posts/1684092755205505/facebook-open-sources-rich-text-editor-framework-draft-js/)
* [这篇博文是使用 Draft.js 编写的](https://dev.to/ben/this-blog-post-was-written-using-draftjs)
* [Draft.js 如何表示富文本数据](https://medium.com/@rajaraodv/how-draft-js-represents-rich-text-data-eeabb5f25cf2#.7gd8psdvi)
* [Draft.js 初学者指南](https://medium.com/@adrianli/a-beginner-s-guide-to-draft-js-d1823f58d8cc#.uufeulpl5)
* [在 Draft.js 中实现待办事项列表](http://bitwiser.in/2016/08/31/implementing-todo-list-in-draft-js.html)
* [Draft.js 片段](https://cannibalcoder.com/2016/12/02/draft-js-pieces/)
* [Learning Draft.js](https://reactrocket.com/series/learning-draft-js/) - 有关如何使用 Draft.js 进行开发的系列博客文章
* [为什么 Wagtail 的新编辑器是使用 Draft.js 构建的](https://wagtail.io/blog/why-wagtail-new-editor-is-built-with-draft-js/)
* [使用 Draft.js 重新思考富文本管道](https://wagtail.io/blog/rethinking-rich-text-pipelines-with-draft-js/)

## 现场演示
* [Draft-js Samples - 带有示例和代码说明的应用程序](https://github.com/Mair/react-meetup-draftjs)
* [Draftail Playground](https://draftail-playground.herokuapp.com/) - Wagtail 的 Draft.js 依赖项作为独立演示。
* [适用于移动浏览器的草稿拖放演示](https://github.com/jan4984/draft-dnd-example)

## 官方存储库中的示例游乐场 (v.0.10.0)
* [富文本编辑器](https://codepen.io/Kiwka/pen/YNYvyG)
* [颜色编辑器](https://codepen.io/Kiwka/pen/oBpVve)
* [从 HTML 编辑器转换](https://codepen.io/Kiwka/pen/YNYgWa)
* [实体编辑器](https://codepen.io/Kiwka/pen/wgpOoZ)
* [链接编辑器](https://codepen.io/Kiwka/pen/ZLvPeO)
* [媒体编辑](https://codepen.io/Kiwka/pen/rjpRzj)
* [纯文本编辑器](https://codepen.io/Kiwka/pen/jyYJzb)
* [装饰器编辑器 - 推文示例](https://codepen.io/Kiwka/pen/KaZERV)

## 生产中的使用
* [StoryChief](https://www.storychief.io/)
* [HKW科技圈杂志](https://technosphere-magazine.hkw.de/)
* [豆瓣阅读](https://read.douban.com/editor_ng)
* [Dooly](https://www.dooly.ai)
* [Wagtail](https://wagtail.io/)
* [Patreon](https://www.patreon.com/)

## 许可证

[![CC0](http://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

在法律允许的范围内，[Nikolaus Graf](https://github.com/nikgraf/) 已放弃本作品的所有版权以及相关或邻接权。
