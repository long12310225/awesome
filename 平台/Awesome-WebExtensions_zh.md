# 很棒的网络扩展 [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> 用于 WebExtensions 开发的精选资源列表。

WebExtensions 是一个用于开发浏览器插件的跨浏览器系统。该系统在很大程度上兼容Google Chrome支持的扩展API。大多数情况下，为此浏览器编写的扩展程序只需进行一些更改即可在 Firefox 中运行（https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Porting_a_Google_Chrome_extension）。

关注 [@fregante](https://fregante.com) 了解更多与 webext 相关的新闻。

## 内容

- [开始使用](#getting-started)
- [Community](#community)
- [库和框架](#libraries-and-frameworks)
- [Tools](#tools)
- [Testing](#testing)
- [Boilerplates](#boilerplates)
- [示例扩展](#sample-extensions)

## 开始使用

- [Chrome Extensions documentation](https://developer.chrome.com/docs/extensions/reference) - 原始 Chrome 扩展模型的文档。
- [Mozilla's WebExtensions documentation](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions) - WebExtensions API 的 MDN wiki。
- [Browser support for WebExtensions](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Browser_support_for_JavaScript_APIs) - Chrome、Edge、Firefox 和 Opera 的兼容性表。
- [Safari Extensions documentation](https://developer.apple.com/safari/extensions/) - 有关构建 Safari 扩展的开发人员文档。从技术上讲不是WebExtensions，API 完全不同。
- [Opera API support](https://dev.opera.com/extensions/apis/) - Opera 的详细 WebExtensions 支持。
- [Browser Extension Standard](https://browserext.github.io/browserext/) - API 标准，受 Mozilla、Opera 和 Microsoft 支持。

## 社区

- [Google Groups](https://groups.google.com/a/chromium.org/forum/#!forum/chromium-extensions) - 讨论。
- [Mozilla Discourse](https://discourse.mozilla.org/c/add-ons) - 讨论。
- [`#addons:mozilla.org`](https://matrix.to/#/#addons:mozilla.org) - Mozilla 的矩阵通道。
- [`google-chrome-extension` tag on Stack Overflow](https://stackoverflow.com/questions/tagged/google-chrome-extension) - 相关问题。
- [`firefox-addon-webextensions` tag on Stack Overflow](https://stackoverflow.com/questions/tagged/firefox-addon-webextensions) - 相关问题。
- [`microsoft-edge-extension` tag on Stack Overflow](https://stackoverflow.com/questions/tagged/microsoft-edge-extension) - 相关问题。

## 库和框架

代码意味着成为扩展的一部分。

- [webext-options-sync](https://github.com/fregante/webext-options-sync) - 帮助您管理和自动保存扩展程序的选项。
- [webext-storage-cache](https://github.com/fregante/webext-storage-cache) - 类似地图的承诺缓存存储会过期。
- [webext-dynamic-content-scripts](https://github.com/fregante/webext-dynamic-content-scripts) - 自动将您的“content_scripts”注入自定义域。
- [mozilla/webextension-polyfill](https://github.com/mozilla/webextension-polyfill) - Polyfill 支持“浏览器”命名空间中基于标准化 API 的承诺。
- [@types/firefox-webext-browser](https://www.npmjs.com/package/@types/firefox-webext-browser) - 为“浏览器”命名空间提供 TypeScript 类型。
- [redux-webext](https://github.com/ivantsov/redux-webext) - 使用 Redux 来管理 WebExtension 的状态。
- [ExtPay](https://github.com/Glench/ExtPay) - 在扩展中进行安全支付，无需运行服务器后端。
- [inject-react-anywhere](https://github.com/OlegWock/inject-react-anywhere) - 通过方便的 API 和样式隔离将 React 组件注入第三方站点。
- [More…](https://github.com/fregante/webext-fun)

## 工具

帮助您管理扩展的应用程序。

- [Chrome Webstore Upload](https://github.com/fregante/chrome-webstore-upload-cli) - 通过 cli（或在 Travis 上自动）将扩展程序上传到 Chrome Web Store。
- [mozilla/web-ext](https://github.com/mozilla/web-ext) - 命令行工具可帮助构建、运行和测试 WebExtensions。
- [chromepet](https://github.com/ZenHubIO/chromepet) - 当您的新版本发布时收到通知。
- [chrome-ext-downloader](https://github.com/jiripospisil/chrome-ext-downloader) - 下载 Chrome 网上应用店中的任意扩展程序，看看它们是如何实现的。
- [chrome-store-api](https://github.com/acvetkov/chrome-store-api) - Chrome 网上应用店 API 包装器。
- [Chrome extension source viewer](https://github.com/Rob--W/crxviewer) - WebExtension 可直接在商店中查看扩展的源代码。
- [@wext/shipit](https://github.com/LinusU/wext-shipit) - 自动发布到 Chrome Web Store、Mozilla Addons 和 Opera Addons 的工具。
- [wext-manifest-loader](https://github.com/abhijithvijayan/wext-manifest-loader) - Webpack 加载器可让您指定“manifest.json”属性仅出现在特定浏览器中。
- [webextension-manifest-loader](https://github.com/jsmnbom/webextension-manifest-loader) - Webpack 加载器加载浏览器定制的manifest.json。它还导入所有可导入的属性，允许您将“manifest.json”作为唯一的 webpack 入口点。
- [webpack-extension-reloader](https://github.com/rubenspgcavalcante/webpack-extension-reloader) - 一个 Webpack 插件，用于在开发过程中自动重新加载浏览器扩展。
- [webpack-target-webextension](https://github.com/awesome-webextension/webpack-target-webextension) - 为使用 Webpack 构建的 WebExtensions 添加代码分割支持。
- [Extension.js](https://github.com/cezaraugusto/extension.js) - 即插即用、零配置、跨浏览器扩展开发工具。

## 测试

- [sinon-chrome](https://github.com/acvetkov/sinon-chrome) - 模拟 Chrome 扩展 API 进行测试。
- [addons-linter](https://github.com/mozilla/addons-linter) - 根据 Mozilla 指南验证扩展。
- [webextensions-jsdom](https://github.com/stoically/webextensions-jsdom) - 根据manifest.json 使用 JSDOM 加载弹出窗口、侧边栏和背景。
- [webextensions-api-fake](https://github.com/stoically/webextensions-api-fake) - 内存中 WebExtensions API 假实现（包括 TypeScript 类型）。
- [webextensions-api-mock](https://github.com/stoically/webextensions-api-mock) - WebExtensions API 作为 sinon 存根（包括 TypeScript 类型）。
- [webextensions-schema](https://github.com/stoically/webextensions-schema) - 以编程方式使用 WebExtensions 架构 JSON 文件。

## 样板文件

- [browser-extension-template](https://github.com/fregante/browser-extension-template) - 带有包裹、选项处理程序和自动发布的准系统样板。
- [create-webextension](https://github.com/rpl/create-webextension) - Yarn WebExtension 生成器。
- [generator-web-extension](https://github.com/webextension-toolbox/generator-web-extension) - WebExtension 生成器可创建开始跨浏览器 Web 扩展开发所需的一切。
- [WXT](https://github.com/wxt-dev/wxt) - 用于开发 Web 扩展的下一代框架

## 示例扩展

这些是简单而现代的 WebExtensions 存储库，可以帮助您确定各个部分的去向，包括通过 Travis CI 自动部署。

- [npmhub](https://github.com/npmhub/npmhub)
- [隐藏 GitHub 上的文件](https://github.com/sindresorhus/hide-files-on-github)
- [mdn/webextension-examples](https://github.com/mdn/webextensions-examples) - 为 MDN 文档策划的各种示例扩展。
