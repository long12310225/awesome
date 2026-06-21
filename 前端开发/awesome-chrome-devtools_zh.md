# 很棒的 Chrome 开发工具 [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> Chrome DevTools 生态系统中很棒的工具和资源

## 内容

- [Learning](#learning)
- [DevTools 工具和生态系统](#devtools-tooling-and-ecosystem)
- [Chrome 开发者工具协议](#chrome-devtools-protocol)
- [将 DevTools 前端与其他平台结合使用](#using-devtools-frontend-with-other-platforms)
- [Applications](#applications)
- [开发工具扩展](#devtools-extensions)
- [Alumni](#alumni)

---

## 学习
- [Dev Tips](https://umaar.com/dev-tips/) - 以 GIF 动画形式提供的大量提示。
- [DevTools Tips](https://devtoolstips.org/) - 作为迷你教程的插图提示集合。
- [Can I DevTools?](https://www.canidev.tools/) - 各种工作流程，已记录。还有每周提示和技巧[时事通讯](https://canidevtools.substack.com/)。
- [Web cheatcodes](https://codepo8.github.io/web-cheatcodes/) - 面向非开发人员的浏览器开发人员工具。
- [Dear Console](https://codepo8.github.io/dearconsole) - 在浏览器控制台中使用的代码片段的集合。
- [Chrome Secret Menus](https://github.com/sparkyrider/chrome-secret-menus) - Chrome 中的内部页面和诊断工具的综合指南。
- [Front-end Debugging Tools Handbook](https://github.com/lala-hakobyan/front-end-debugging-handbook) - 掌握前端调试工具的实用指南，从 Chrome DevTools 和框架扩展到 AI 增强型 IDE 调试。

---

## DevTools 工具和生态系统

### 对象格式化
- [immutable-devtools](https://github.com/andrewdavey/immutable-devtools) - Immutable-js 值的自定义格式化程序。

### 网络巡检
- [betwixt](https://github.com/kdzwinel/betwixt) - 系统级网络代理，通过网络面板提供检查。

### CPU配置文件
- [call-trace](https://github.com/brendankenny/call-trace) - 可以使用钩子检测您的 JS，然后生成完整（非采样）执行的“.cpuprofile”。查看时间或呼叫计数。
- [cpuprofilify](https://github.com/thlorenz/cpuprofilify) - 将各种分析/采样工具的输出转换为“.cpuprofile”格式。
- [Wishbone Python framework](https://wishbone.readthedocs.io/en/latest/misc/profiling.html) - 分析数据可以导出为“.cpuprofile”。

### 多媒体
- [snapline](https://github.com/pmdartus/snapline) - 将时间线屏幕截图转换为 gif。

### 时间线、追踪和分析
- [DevTools Timeline Viewer](https://chromedevtools.github.io/timeline-viewer/) - 分享您的时间线录音的 URL。

### Chrome 调试器与编辑器集成
- [VS Code - Debugger for Chrome](https://github.com/Microsoft/vscode-chrome-debug/) - VS Code 中的断点调试。
- [VS Code - Elements for Microsoft Edge](https://github.com/microsoft/vscode-edge-devtools) - VS Code 内的元素面板。
- [ChromeREPL](https://github.com/acarabott/ChromeREPL) - 在 Sublime Text 中，使用 Chrome 控制台。
- [Sublime Web Inspector](http://sokolovstas.github.io/SublimeWebInspector/) - 直接在 Sublime Text 中进行 JavaScript 断点调试。
- [WebStorm/JetBrains Chrome Extension](https://www.jetbrains.com/help/webstorm/2017.1/configuring-javascript-debugger-and-jetbrains-chrome-extension.html) - WebStorm IDE 可以调试 JavaScript、查看 DOM 树以及实时编辑 HTML、CSS 和 JS。

---

## Chrome 开发者工具协议
- [ChromeDevTools/devtools-protocol](https://github.com/chromedevtools/devtools-protocol) - **协议 JSON 的规范位置**。协议错误的问题跟踪器。 TypeScript 类型。
- [DevTools Protocol API Docs](https://chromedevtools.github.io/devtools-protocol/) - 易于浏览的 UI，用于探索协议的域、方法和事件。

### 使用协议进行开发
- [chrome-remote-interface Wiki](https://github.com/cyrus-and/chrome-remote-interface/wiki) - 许多有用的食谱。
- [Chrome Protocol Proxy](https://github.com/wendigo/chrome-protocol-proxy) - 使用 devtools 协议调试客户端的工具。

### 两大自动化库
- [Puppeteer](https://github.com/GoogleChrome/puppeteer/) - Node.js 提供高级 API，通过 DevTools 协议控制无头 Chrome。另请参阅 [awesome-puppeteer](https://github.com/transitive-bullshit/awesome-puppeteer)。
- [Playwright](https://github.com/microsoft/playwright) - 使用单个 API 实现 Chromium、Firefox 和 WebKit 自动化的库。适用于 Node.js、Python、.Net、Java。另请参阅 [awesome-playwright](https://github.com/mxschmitt/awesome-playwright)。

### 用于驱动协议（或之上一层）的库

- JavaScript/Node.js：[chrome-remote-interface](https://github.com/cyrus-and/chrome-remote-interface)
- TypeScript/Node.js：[chrome-debugging-client](https://github.com/TracerBench/chrome-debugging-client)
- TypeScript/Node.js：[noice-json-rpc](https://www.npmjs.com/package/noice-json-rpc) - 基于代理的实现，将 CDP 公开为其 API。
- TypeScript/Node.js：[Taiko](https://github.com/getgauge/taiko/)
- TypeScript/Node.js：[Lumen](https://github.com/omxyz/lumen) - 视觉优先的浏览器代理，具有通过 CDP 进行自我修复的确定性重播。
- Rust：[Rust Headless Chrome](https://github.com/atroche/rust-headless-chrome/)
- Java：[chrome-devtools-java-client](https://github.com/kklisura/chrome-devtools-java-client)
- Java: [jvppeteer](https://github.com/fanyong920/jvppeteer) - Java 版无头 Chrome
- Python：[PyCDP](https://github.com/hyperiongray/python-chrome-devtools-protocol) - 纯 Python，无 IO 包装器。另请参阅 [Trio CDP 驱动程序](https://github.com/hyperiongray/trio-chrome-devtools-protocol)
- Python：[chromewhip](https://github.com/chuckus/chromewhip) - `splash` 服务的直接替代品
- Python: [pyppeteer](https://github.com/pyppeteer/pyppeteer) - Puppeteer 端口
- Python：[ChromeController](https://github.com/fake-name/ChromeController) - 高级浏览器管理
- Go：[chromedp](https://github.com/chromedp/chromedp) - 用于驱动浏览器的高级操作和任务
- 转到：[cdp](https://github.com/mafredri/cdp)
- 转到：[gcd](https://github.com/wirepair/gcd)
- 转到：[godet](https://github.com/raff/godet)
- 去：[Rod](https://github.com/go-rod/rod)
- C#/.NET: [Puppeteer Sharp](https://github.com/hardkoded/puppeteer-sharp) - Puppeteer 端口
- C#/dotnet: [chrome-dev-tools](https://github.com/BaristaLabs/chrome-dev-tools) - 协议包装生成器，可以通过编辑车把模板进行自定义。包括.Net Core 模板。
- C#/.NET：[dotnet-chrome-protocol](https://github.com/seclerp/dotnet-chrome-protocol) - C#/.NET 中用于 Chrome DevTools 协议支持的运行时库和架构代码生成工具。
- Ruby: [Ferrum](https://github.com/route/ferrum) - 在 Ruby 中控制 Chrome 的高级 API
- Ruby：[Cuprite](https://github.com/machinio/cuprite) - 水豚驱动程序
- Kotlin：[chrome-reactive-kotlin](https://github.com/wendigo/chrome-reactive-kotlin) - 反应式 (rxjava 2.x)，Kotlin 中的低级客户端库
- Kotlin：[chrome-devtools-kotlin](https://github.com/joffrey-bion/chrome-devtools-kotlin) - 基于协程的客户端库，提供低级 CDP 原语和高级扩展。
- Clojure：[clj-chrome-devtools](https://github.com/tatut/clj-chrome-devtools) - CDP 包装器 API 是自动生成的，并将在 CDP 协议更改时更新。
- Clojure：[cuic](https://github.com/milankinen/cuic) - 通过 DevTools 协议为 UI 测试自动化提供高级 API。
- PHP: [chrome-devtools-protocol](https://github.com/jakubkulhan/chrome-devtools-protocol) - 该协议的 PHP 客户端库。
- PHP: [PuPHPeteer](https://github.com/rialto-php/puphpeteer) - PHP 桥接节点 Puppeteer


### 浏览器适配器
- [devtools-remote-debugger](https://github.com/Nice-PLQ/devtools-remote-debugger) - 对网页使用开发工具；在客户端 JS 中实现的 CDP 代理。
- [Inspect](https://inspect.dev/) - 轻松使用针对 iOS 和 Android 的开发工具。浏览器和网络视图。 **（闭源）**


## 将 DevTools 前端与其他平台结合使用

#### 安卓
- [Facebook Stetho](https://github.com/facebook/stetho) - 使用 Chrome DevTools 进行本机 Android 调试。
- [j2v8-debugger](https://github.com/AlexTrotsenko/j2v8-debugger) - 使用 Chrome DevTools 调试在 [J2V8](https://github.com/eclipsesource/J2V8) 中运行的 JavaScript。

#### Clojure脚本
- [Dirac](https://github.com/binaryage/dirac) - ClojsureScript 的调试。

#### iOS系统
- [PonyDebugger](https://github.com/square/PonyDebugger) - 使用 Chrome DevTools 远程网络和数据调试 iOS 应用程序。

#### Node.js
- [ndb](https://github.com/GoogleChromeLabs/ndb) - 通过 DevTools 前端改进 Node.js 调试体验。
- [Debugging Node.js with Chrome DevTools](https://medium.com/@paul_irish/debugging-node-js-nightlies-with-chrome-devtools-7c4a1b95ae27) - 有关使用 Node v6.3+ 中完整调试和分析支持的指南。
- [thetool](https://github.com/sfninja/thetool) - 使用 Node.js 进行 CPU、内存、覆盖率、类型分析。
- [chrome-devtools-frontend](https://www.npmjs.com/package/chrome-devtools-frontend) - Chrome 中提供的前端镜像。

#### 红宝石
- [ruby/debug](https://github.com/ruby/debug) - Ruby 的调试功能。

---

## 应用领域

### 浏览器
- [BrowserBox](https://github.com/BrowserBox/BrowserBox) - 将 Chrome 嵌入网页，主要由 DevTools 提供支持，并支持多用户浏览、远程 DevTools、音频以及“.docx”、“.pdf”等文档。
- [Puppetromium](https://github.com/dosyago/puppetromium) - 使用 Puppeteer 构建的概念验证 Web 浏览器，使用 Node.js、HTML 和 CSS 编写，客户端 JavaScript 占比为 0%。

### 网络归档器和索引器
- [dn](https://github.com/dosyago/dn) - 您浏览的存档和索引页面用于离线查看和搜索，使用“Fetch”域的拦截实现，并可与任何基于 Chromium 的浏览器配合使用。
  
---

## 开发工具扩展

### 工作流程
- [Clockwork](https://chromewebstore.google.com/detail/clockwork/dmggabnehkmmfmdffgajcflpdjlnoemp?hl=en) - 查看 PHP 应用程序分析数据。
- [RailsPanel](https://chromewebstore.google.com/detail/railspanel/gjpfobpafnhjhbajcjgccbbdofdckggg?hl=en-US) - 查看 Ruby on Rails 应用程序分析数据。
- [React Developer Tools](https://chromewebstore.google.com/detail/react-developer-tools/fmkadmapgofadopljbjfkapdkoienihi) - 检查 React 组件层次结构。
- [Ember.js Inspector](https://chromewebstore.google.com/detail/ember-inspector/bmdblncegkenkacieihfhpjfppoconhi) - 允许您检查应用程序中的 Ember.js 对象。
- [Vue.js Developer Tools](https://github.com/vuejs/vue-devtools) - 检查 Vue.js 组件并操作它们的数据。
- [Angular DevTools](https://chromewebstore.google.com/detail/angular-devtools/ienfalfjdbdpebioblfackkekamfmbnh) - Angular 应用程序的调试和分析。
- [Backbone Debugger](https://chromewebstore.google.com/detail/backbone-debugger/bhljhndlimiafopmmhjlgfpnnchjjbhd) - 检查 Backbone 应用程序的视图、模型、事件和路由。
- [Redux Devtools](https://chromewebstore.google.com/detail/redux-devtools/lmhkpmbekcpmknklioeibfkpmmfibljd) - 通过操作历史记录、撤消和重播检查 Redux。
- [Insight](https://github.com/3Dparallax/insight/) - 一个 WebGL 调试工具包，可实现更高效的 WebGL 开发和更高效的 WebGL 应用程序。
- [BEM devtools](https://github.com/escaton/bem-chrome-devtools) - 检查“i-bem”框架中表达的 BEM 实体。
- [Web Component DevTools](https://chromewebstore.google.com/detail/web-component-devtools/gdniinfdlmmmjpnhgnkmfpffipenjljo) - 检查、修改和观察页面上的 Web 组件。

### 主题
- [Material UI Theme](https://chromewebstore.google.com/detail/material-devtools-theme-c/jmefikbdhgocdjeejjnnepgnfkkbpgjo) - 提供各种受材料设计启发的主题。

### 性能
- [sloth](https://github.com/denar90/sloth) - Chrome 扩展允许启用并保存所选选项卡的 CPU 和网络限制。
- [TracerBench](https://github.com/TracerBench/tracerbench) - 用于 Web 应用程序的受控性能基准测试工具，提供有关性能增量的清晰、可操作且可用的见解。

### 自动化
- [Puppeteer IDE](https://github.com/gajananpp/puppeteer-ide-extension) - 浏览器开发者工具中的独立 Puppeteer 游乐场。
- [k6 browser](https://github.com/grafana/xk6-browser) - 浏览器自动化和端到端 Web 测试工具，可与浏览器交互并收集前端性能指标。

## 校友
老项目，可能不再维护了……但仍然很酷。

- [Remote Debug Gateway](https://github.com/RemoteDebug/remotedebug-gateway) - 允许您一次将客户端连接到多个浏览器。
- 多用户开发工具：[DevTools Remote](https://github.com/auchenberg/devtools-remote) - 远程调试其他人的浏览器。
- [DevTools Backend](https://github.com/christian-bromann/devtools-backend) - 用于调试任意 Web 环境的 Chrome DevTools 后端的独立实现。
- Python CDP 驱动程序：[pychrome](https://github.com/fate0/pychrome) - 低级 CDP 传输处理程序
- [ios-webkit-debug-proxy](https://github.com/google/ios-webkit-debug-proxy) - 通过 CDP 公开 Mobile Safari 和 UIWebView 实例。
  - [Remote Debug iOS WebKit adapter](https://github.com/RemoteDebug/remotedebug-ios-webkit-adapter) - 基于 ios-webkit-debug-proxy 构建，并将 WebKit 的远程调试协议 API 转换为 CDP。
- [IE Diagnostics Adapter](https://github.com/Microsoft/IEDiagnosticsAdapter) - Microsoft IE 11 到 CDP 的协议适配器。
- [go-debugger-devtools](https://github.com/allada/go-debugger-devtools)
