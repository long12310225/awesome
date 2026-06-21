# 很棒的 AVA [<img src="https://github.com/avajs/ava/raw/main/media/header.png" width="280"align="right" alt="AVA">](https://avajs.dev) [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> [AVA](https://avajs.dev) 是一个最小且未来派的 JavaScript 测试运行器

## 内容

- [Articles](#articles)
- [Videos](#videos)
- [Packages](#packages)
- [与 AVA 合作](#works-with-ava)
- [Tutorials](#tutorials)
- [Miscellaneous](#miscellaneous)
- [Support](#support)

## 文章

- [Recipes](https://github.com/avajs/ava/tree/main/docs/recipes)
- [使用 AVA 测试 React Native 应用程序](https://shift.infinite.red/testing-the-bejeezus-out-of-react-native-apps-with-ava-330f51f8f6c3)
- [开始使用 Create React App 和 AVA](https://semaphoreci.com/community/tutorials/getting-started-with-create-react-app-and-ava)
- [使用 AVA 轻松进行单元测试](https://wecodetheweb.com/2016/04/19/effortless-unit-testing-with-ava/)

## 视频

- [AVA 团队的 JavaScript Air 剧集](http://jsair.io/ava)
- [使用 AVA 测试 React 组件](https://www.youtube.com/watch?v=RxLW6-3dk5A)

## 套餐

- [eslint-plugin-ava](https://github.com/avajs/eslint-plugin-ava) - ESLint 规则。
- [ava-codemods](https://github.com/jamestalmage/ava-codemods) - Codemods 简化了升级到新版本的过程。
- [sublime-ava](https://github.com/avajs/sublime-ava) - Sublime 的片段。
- [atom-ava](https://github.com/avajs/atom-ava) - Atom 的片段。
- [vscode-ava](https://github.com/samverschueren/vscode-ava) - Visual Studio 代码的片段。
- [vim-ava-snippets](https://github.com/ahmedelgabri/vim-ava-snippets) - Vim 的片段。
- [redux-ava](https://github.com/sotojuan/redux-ava) - Redux 的测试助手。
- [redux-test-recorder](https://github.com/conorhastings/redux-test-recorder) - 在 React 应用程序中为 Redux 减速器生成 AVA 测试。
- [gulp-ava](https://github.com/avajs/gulp-ava) - 使用 Gulp 运行测试。
- [grunt-ava](https://github.com/avajs/grunt-ava) - 使用 Grunt 运行测试。
- [fly-ava](https://github.com/pine/fly-ava) - 使用 Fly 运行测试。
- [start-ava](https://github.com/start-runner/ava) - 使用“开始”运行测试。
- [sigh-ava](https://github.com/unlight/sigh-ava) - 使用 Sigh 运行测试。
- [eslint-ava-rule-tester](https://github.com/jfmengels/eslint-ava-rule-tester) - 使用 AVA 测试 [ESLint](https://github.com/eslint/eslint) 插件。
- [jscodeshift-ava-tester](https://github.com/jfmengels/jscodeshift-ava-tester) - 使用 AVA 测试 [jscodeshift](https://github.com/facebook/jscodeshift) codemod。
- [ava-preact-init](https://github.com/avajs/ava-preact-init) - 为 Preact 设置 AVA。
- [ava-fixture](https://github.com/unional/ava-fixture) - 运行夹具/基线测试。
- [ava-fast-check](https://github.com/dubzzz/ava-fast-check) - 基于属性的测试。
- [ava-fixture-docker-db](https://github.com/cdaringe/ava-fixture-docker-db) - 将 docker 数据库添加到您的测试上下文中。
- [ava-webcomponents](https://github.com/Wildhoney/ava-webcomponents) - 通过 Puppeteer 测试 Web 组件。
- [ava-tap-json](https://github.com/yovasx2/ava-tap-json) - 具有 AVA 兼容性的 JSON 输出。
- [ava-typescript-worker](https://github.com/seamapi/ava-typescript-worker) - 在共享工作线程中使用 TypeScript
- [ava-postgres](https://github.com/seamapi/ava-postgres) - 为每个测试获取一个新的 Postgres 数据库
- [pava](https://github.com/TomerAberbach/pava) - 参数化测试。

## 与 AVA 合作

- [Spectron](https://github.com/electron/spectron#with-ava) - 使用 AVA 和 ChromeDriver 测试 Electron 应用程序。
- [Chūhai](https://github.com/Hypercubed/chuhai) - 使用 AVA 和 benchmark.js 运行并验证基准测试。
- [Leakage](https://github.com/andywer/leakage#usage-with-ava--tape) - 内存泄漏测试。
- [pify](https://github.com/sindresorhus/pify) - Promisify 回调式函数可以更好地进行测试。 [（示例）](https://github.com/sindresorhus/registry-url/blob/eb1f0e01722208366c9199b96235fd043ec162ae/test.js#L6)
- [p-event](https://github.com/sindresorhus/p-event) - 承诺一个事件。 [（示例）](https://github.com/sindresorhus/gulp-debug/blob/4db5871594742a346d17aa9b34f43c87d4e54934/test.js#L42-L44)
- [execa](https://github.com/sindresorhus/execa) - 测试您的 CLI 工具。 [（示例）](https://github.com/sindresorhus/active-win-cli/blob/d01813762b304102d1fee147855481e9f38c8517/test.js#L5-L6)
- [delay](https://github.com/sindresorhus/delay) - 给你的测试增加延迟。 [（示例）](https://github.com/sindresorhus/p-queue/blob/a3a5cadefc2b54269f4939bb34e8dc180c3bd800/test.js#L39)
- [get-stream](https://github.com/sindresorhus/get-stream) - 测试流的输出。 [（示例）](https://github.com/sindresorhus/ora/blob/4ceeedd51795bb88a8033229d198e70cd8a2aff7/test.js#L33-L35)
- [create-test-server](https://github.com/lukechilds/create-test-server) - 创建一个最小的 Express 服务器用于测试。 [（示例）]（https://github.com/lukechilds/clone-response/blob/11f5870e4e1b039e2d9a8f1f72d45fd1b9706bf3/test/clone-response.js）

## 教程

- [Testing a React & Redux Codebase](http://silvenon.com/testing-react-and-redux/) - 关于使用 AVA 测试 React 和 Redux 项目的综合教程系列。

## 杂项

- [Stickers, t-shirts, etc](https://www.redbubble.com/people/sindresorhus/works/30330590-ava-logo) - 产品按生产价销售，不加价。
- [Slides from AVA talk at London Node User Group](https://speakerdeck.com/novemberborn/ava-at-lnug) - 由核心团队成员 [Mark Wubben](https://github.com/novemberborn) 撰写。

## 支持

- [Github 讨论](https://github.com/avajs/ava/discussions)
- [堆栈溢出](https://stackoverflow.com/questions/tagged/ava)
- [Twitter](https://twitter.com/ava__js)
