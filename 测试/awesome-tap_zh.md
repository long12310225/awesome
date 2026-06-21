# 很棒的 TAP [<img src="https://testanything.org/images/tap.png" width="67"align="right">](https://testanything.org) [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> [Test Anything Protocol](https://testanything.org) 的有用资源

TAP 是测试工具中测试模块之间基于文本的简单接口。

*该列表目前非常关注 JavaScript。那只是因为我只熟悉 JS 世界中的 TAP 东西。欢迎任何语言的贡献。*

## 内容

- [Reporters](#reporters)
- [Producers](#producers)
- [Consumers](#consumers)
- [Tools](#tools)
- [Articles](#articles)
- [Tutorials](#tutorials)
- [Documentation](#documentation)
- [Community](#community)

## 记者

### JavaScript

- [tap-dot](https://github.com/scottcorgan/tap-dot) - 点输出。
- [tap-spec](https://github.com/scottcorgan/tap-spec) - 类似摩卡的规格记者。
- [tap-nyan](https://github.com/calvinmetcalf/tap-nyan) - 尼安猫.
- [tap-min](https://github.com/derhuerst/tap-min) - 最小输出。
- [tap-difflet](https://github.com/namuol/tap-difflet) - 具有差异的最小输出。
- [tap-diff](https://github.com/axross/tap-diff) - 具有差异的人性化输出。
- [tap-simple](https://github.com/joeybaker/tap-simple) - 简单的输出。
- [faucet](https://github.com/substack/faucet) - 人类可读的摘要器。
- [tap-mocha-reporter](https://github.com/isaacs/tap-mocha-reporter) - 使用任何 [Mocha reports](https://github.com/isaacs/tap-mocha-reporter/tree/master/lib/reporters)。
- [tap-summary](https://github.com/zoubin/tap-summary) - 总结输出。
- [tap-pessimist](https://github.com/clux/tap-pessimist) - 仅显示失败的测试。
- [tap-prettify](https://github.com/toolness/tap-prettify) - 具有差异的良好可读输出。
- [tap-colorize](https://github.com/substack/tap-colorize) - 对输出进行着色，同时保持机器可读性。
- [tap-bail](https://github.com/juliangruber/tap-bail) - 当第一次测试失败时退出。
- [tap-notify](https://github.com/axross/tap-notify) - 适用于 macOS、Linux 和 Windows 的通知程序。
- [tap-json](https://github.com/gummesson/tap-json) - JSON 输出。
- [ava-tap-json](https://github.com/yovasx2/ava-tap-json) - 具有 AVA 兼容性的 JSON 输出。
- [tap-xunit](https://github.com/aghassemi/tap-xunit) - xUnit 输出。
- [tap-teamcity](https://github.com/smockle/tap-teamcity) - TeamCity 的输出。

### 去

- [tapfmt](https://github.com/coreybutler/tapfmt) - 独立的跨平台格式化程序。

## 制片人

产生 TAP 输出的东西。

### JavaScript

- [AVA](https://github.com/sindresorhus/ava) - 未来测试运行程序（`$ ava --tap`）。
- [tap](https://github.com/isaacs/node-tap) - Node.js 的 TAP 测试框架。
- [tape](https://github.com/substack/tape) - 为 Node.js 和浏览器生成 TAP 测试工具。
- [ESLint](https://eslint.org/docs/user-guide/formatters/#tap) - 可插入的 JavaScript linter (`$ eslint --format=tap`)。
- [Mocha](https://mochajs.org) - 用于 Node.js 和浏览器的功能丰富的测试框架（`$ mocha reports=tap`）。
- [qunit-tap](https://github.com/twada/qunit-tap) - QUnit 的 TAP 输出。
- [jasmine-reporters](https://github.com/larrymyers/jasmine-reporters) - Jasmine 的 TAP 输出。
- [karma-tap-reporter](https://github.com/fumiakiy/karma-tap-reporter) - Karma 的 TAP 输出。
- [mos](https://github.com/zkochan/mos) - Markdown 文件生成器和测试器（`$ mos test --tap`）。
- [zora](https://github.com/lorenzofox3/zora) - TAP 生成测试运行程序，无需 Babel 即可与 ES2015 配合使用。
- [node:test](https://nodejs.org/api/test.html) - Node.js 附带的最小 TAP 测试运行程序。

### 斯威夫特

- [TAP](https://github.com/swiftdocorg/tap) - 用于 Test Anything Protocol (v13) 的 Swift 包。

### 鱼

- [Fishtape](https://github.com/fisherman/fishtape) - TAP 生产商和鱼类测试工具。

### 重击

- [bats](https://github.com/sstephenson/bats) - Bash 自动化测试系统。
- [ShellSpec](https://github.com/shellspec/shellspec) - 适用于 POSIX shell 的全功能 BDD 单元测试框架。

[更多...](https://testanything.org/ Producers.html)

## 消费者

消耗 TAP 输出的东西。

### JavaScript

- [tap-parser](https://github.com/substack/tap-parser) - TAP 解析器。
- [tap-out](https://github.com/scottcorgan/tap-out) - TAP 解析器。
- [yamlish](https://github.com/isaacs/yamlish) - YAML 块解析器。

[更多...](https://testanything.org/consumers.html)

## 工具

### JavaScript

- [tap-dev-tool](https://github.com/Jam3/tap-dev-tool) - 在浏览器控制台中美化 TAP。
- [tap-merge](https://github.com/anko/tap-merge) - 合并多个 TAP 流。
- [smokestack](https://github.com/hughsk/smokestack) - 在浏览器中运行 TAP 测试并将输出写入“stdout”。
- [chutney](https://github.com/derhuerst/chutney) - 在 Sauce Labs 运行 TAP 测试。轻量级 [smokestack](https://github.com/hughsk/smokestack) 替代方案。

### 蟒蛇

- [tappy](https://github.com/mblayman/tappy) - 使用 TAP 的工具。

## 文章

- [了解测试一切协议](https://www.effectiveperlprogramming.com/2011/05/understand-the-test-anything-protocol/)

## 教程

- [test-anything](https://github.com/finnp/test-anything) - 通过互动研讨会学习使用 TAP 测试任何内容。

## 文档

- [Specification](https://testanything.org/tap-version-13-specification.html)
- [Wikipedia](https://en.wikipedia.org/wiki/Test_Anything_Protocol)

## 社区

- [Discuss](https://github.com/TestAnything/Specification/issues)
- [Reddit](https://www.reddit.com/r/testanythingprotocol)
- [堆栈溢出](https://stackoverflow.com/questions/tagged/tap)
