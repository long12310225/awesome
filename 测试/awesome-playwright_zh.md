# 很棒的剧作家 [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> 使用 Playwright 的精彩工具、实用程序和项目的精选列表

[Playwright](https://github.com/microsoft/playwright) 是一个用于 Web 测试和自动化的框架。它允许使用单个 API 测试 Chromium、Firefox 和 WebKit。适用于 Node.js、Python、.NET 和 Java。

## 内容

- [Integrations](#integrations)
- [语言支持](#language-support)
- [Utils](#utils)
- [抓取和自动化](#scraping--automation)
- [人工智能与代理](#ai--agents)
- [Reporters](#reporters)
- [Showcases](#showcases)
- [Guides](#guides)
- [Contribute](#contribute)

## 集成

- [@appetize/Playwright](https://docs.appetize.io/testing) - 使用 Playwright Test Runner 在 [Appetize](https://www.appetize.io) 的虚拟设备上对 Web 或本机应用程序进行移动测试。
- [appwright](https://www.npmjs.com/package/appwright) - 使用 Appium 和 Playwright Test Runner 进行移动测试。
- [artillery-engine-playwright](https://github.com/artilleryio/artillery/tree/main/packages/artillery-engine-playwright) - 使用 Playwright 进行负载测试。
- [@axe-core/Playwright](https://github.com/dequelabs/axe-core-npm/blob/develop/packages/playwright/README.md) - Axe 与 Playwright 的官方集成。
- [axe-playwright](https://github.com/abhinaba-ghosh/axe-playwright) - Axe 与 Playwright 的非官方整合。
- [Chromium for Serverless platforms](https://github.com/Sparticuz/chromium?tab=readme-ov-file#usage-with-playwright) - 在无服务器平台上为 Playwright 预构建 Chromium 二进制文件。
- [CodeceptJS](https://github.com/Codeception/CodeceptJS) - Node.js 的增压 End 2 End 测试框架。
- [cucumber-playwright](https://github.com/Tallyb/cucumber-playwright) - 用于使用 TypeScript 和 Playwright 编写基于 Cucumber 的 E2E 测试的入门存储库。
- [@guidepup/Playwright](https://github.com/guidepup/guidepup-playwright) - Playwright 的 VoiceOver 和 NVDA 屏幕阅读器驱动程序集成。
- [Happo](https://docs.happo.io/docs/playwright) - 捕捉意外的视觉和可访问性变化以及 UI 错误。
- [Playwright Angular Schematic](https://github.com/playwright-community/playwright-ng-schematics) - 将 Playwright Test 添加到您的 Angular 项目中。
- [playwright-bdd](https://github.com/vitalets/playwright-bdd) - 使用 Playwright runner 和 CucumberJS 进行 BDD 测试。
- [Playwright CRX](https://github.com/ruifigueira/playwright-crx) - Playwright codegen 作为 Chrome 扩展。可在 [Chrome 网上应用店](https://chromewebstore.google.com/detail/playwright-crx/jambeljnbnfbkcpnoiaedcabbgmnnlcd) 购买。
- [playwright-graphql](https://www.npmjs.com/package/playwright-graphql?activeTab=readme) - 生成类型安全的 GraphQL 客户端和用于 Playwright API 测试的装置，以及用于模式/操作生成和可选覆盖率报告的 CLI。
- [playwright-pytest](https://github.com/microsoft/playwright-pytest/) - 官方 Pytest 插件，用于将 Playwright 页面与固定装置一起使用。
- [Serenity/JS](https://serenity-js.org) - Playwright 的验收测试、报告和测试集成框架，实现[剧本模式](https://serenity-js.org/handbook/design/screenplay-pattern/)。

## 语言支持

- [Playwright](https://git.io/JT2bj) - Node.js（JavaScript 和 TypeScript）的官方剧作家。
- [playwright-dotnet](https://github.com/microsoft/playwright-dotnet) - 官方 Playwright 移植到 .NET。
- [playwright-java](https://github.com/microsoft/playwright-java) - 官方 Playwright 移植到 Java。
- [playwright-python](https://github.com/microsoft/playwright-python) - 官方 Playwright 移植到 Python。
- [playwright-go](https://github.com/playwright-community/playwright-go) - Golang 的剧作家端口。
- [playwright-perl](https://github.com/teodesian/playwright-perl) - Perl 的剧作家移植。
- [playwright-php](https://github.com/playwright-php/playwright) - PHP 的剧作家端口。
- [playwright-ruby-client](https://github.com/YusukeIwaki/playwright-ruby-client) - Ruby 的剧作家移植。
- [playwright-rust](https://github.com/padamson/playwright-rust) - Rust 的剧作家移植。

## 实用工具

- [@bgotink/playwright-coverage](https://github.com/bgotink/playwright-coverage) - 使用 v8 覆盖率报告 Playwright 测试的覆盖率，无需任何仪器。
- [BrowserClaw](https://github.com/idan-rubin/browserclaw) - 基于 Playwright 构建的 AI 浏览器自动化，通过可访问性快照和参考定位实现。
- [eslint-plugin-playwright](https://github.com/playwright-community/eslint-plugin-playwright) - ESLint 插件可满足您的 Playwright 测试需求。
- [@global-cache/Playwright](https://github.com/vitalets/global-cache) - 用于在并行工作程序和测试运行之间共享数据的键值缓存。
- [Heroshot](https://github.com/omachala/heroshot) - 文档截图自动化。用于定义屏幕截图的视觉选择器，一个命令即可重新生成所有屏幕截图。
- [Libretto](https://github.com/saffron-health/libretto) - 基于 Playwright 的开源工具包和 CLI，用于编码代理检查页面、捕获网络流量并生成自动化脚本。
- [Moon](https://github.com/aerokube/moon) - 用于在 Kubernetes 集群中并行执行 Playwright 测试的工具。
- [nextcov](https://github.com/stevez/nextcov) - 使用 Playwright 测试的 Next.js 应用程序的 V8 代码覆盖率收集和合并，将单元、组件和集成覆盖率统一到单个报告中。
- [octomind.dev](https://octomind.dev) - 通过人工智能辅助的测试用例发现自动生成、运行和维护。
- [playwright-best-practices-skill](https://github.com/currents-dev/playwright-best-practices-skill) - AI 技能使代理成为编写、调试和维护 Playwright 测试的专家。
- [Playwright-cleanup](https://www.npmjs.com/package/playwright-cleanup) - Playwright 清理工具，通过撤消对测试环境的任何更改来简化测试清理。
- [playwright-elements](https://danteukraine.github.io/playwright-elements) - Playwright 测试扩展，用于创建可重用、可链接的组件元素，以减少页面对象样板。
- [playwright-magic-steps](https://github.com/vitalets/playwright-magic-steps) - 自动将 JavaScript 注释转换为剧作家步骤。
- [playwright-network-cache](https://github.com/vitalets/playwright-network-cache) - 通过在文件系统上缓存网络请求来加速 Playwright 测试。
- [Playwright-performance](https://www.npmjs.com/package/playwright-performance) - 用于使用 Playwright 测量和分析测试流性能的插件。
- [playwright-python-language-injection](https://github.com/Mattwmaster58/playwright-python-language-injection) - 在 PyCharm 中使用“python-playwright”时 CSS/JS 语法突出显示的语言注入定义。
- [playwright-skill](https://github.com/testdino-hq/playwright-skill) - 70 多种经过生产测试的 Playwright 技能，适用于编码代理，涵盖最佳实践、POM 模式、CI/CD 和迁移路径。
- [playwright-test-coverage](https://github.com/anishkny/playwright-test-coverage) - 用于从运行 Playwright 测试中收集代码覆盖率的插件。
- [Playwright Test for VSCode](https://marketplace.visualstudio.com/items?itemName=ms-playwright.playwright) - VS Code 的官方 Playwright 测试扩展。
- [playwright-ui5](https://github.com/detachhead/playwright-ui5) - sapui5 的自定义选择器引擎。
- [playwright-xpath](https://github.com/detachhead/playwright-xpath) - xpath 2 和 3 的自定义选择器引擎。
- [POMWright](https://github.com/DyHex/POMWright) - 基于 TypeScript 的页面对象模型框架，具有自动嵌套/链接定位器生成功能。
- [TestingBot](https://testingbot.com) - 将您的 Playwright 测试与云中的浏览器连接。
- [Try Playwright](https://try.playwright.tech) - 用于运行剧作家测试的交互式游乐场。

## 抓取和自动化

- [browsers-benchmark](https://github.com/techinz/browsers-benchmark) - 用于针对机器人检测系统测试浏览器自动化引擎的基准工具（Cloudflare、DataDome、reCAPTCHA、Akamai、PerimeterX、Kasada...）。
- [camofox-browser](https://github.com/jo-inc/camofox-browser) - 隐形无头浏览器服务器可用作与 Playwright 兼容的自动化后端，内置反检测功能。
- [CloakBrowser](https://github.com/CloakHQ/CloakBrowser) - Stealth Chromium 具有源代码级指纹补丁以及与 Playwright 兼容的 Python 和 JavaScript 包装器。
- [Human Browser](https://humanbrowser.cloud) - Playwright 插件，可使用住宅 IP 和设备指纹以及 A2A + MCP 端点在托管云浏览器上运行脚本。
- [invisible_playwright](https://github.com/feder-cr/invisible_playwright) - 使用带有源级指纹和反检测补丁的已修补 Firefox 进行即插即用的 Playwright 替换。
- [playwright-captcha](https://github.com/techinz/playwright-captcha) - Playwright、Patchright 和 Camoufox 的自动验证码解决。支持 Cloudflare Turnstile、reCAPTCHA V2 和 V3。

## 人工智能与代理

- [Playwright Agent CLI](https://playwright.dev/agent-cli/introduction) - 专为编码代理设计的浏览器自动化官方命令行界面，具有令牌有效的命令和可安装的技能。
- [Playwright MCP](https://github.com/microsoft/playwright-mcp) - 官方模型上下文协议服务器，通过 Playwright 可访问性快照为法学硕士提供浏览器自动化。

## 记者

- [allure-playwright](https://github.com/allure-framework/allure-js/tree/master/packages/allure-playwright) - Allure 与 Playwright Test 框架集成。
- [Checkly](https://www.checklyhq.com/docs/detect/testing/playwright-reporter/) - 将 Playwright 测试结果、屏幕截图、视频和跟踪上传到 Checkly 平台，以便在全球区域进行监控和调试。
- [currents-dev](https://currents.dev/) - 用于调试、排除故障和分析并行 Playwright CI 测试的云仪表板。
- [echoed](https://github.com/mrasu/echoed) - 通过在 HTML 中可视化 OpenTelemetry 数据，使测试变得可观察。
- [monocart-reporter](https://github.com/cenfun/monocart-reporter) - 剧作家测试记者，在 html 网格中显示套件/案例/步骤。
- [playwright-ctrf-json-reporter](https://github.com/ctrf-io/playwright-ctrf-json-reporter) - 遵循 CTRF 架构的 Playwright JSON 测试结果报告器。
- [playwright-slack-report](https://github.com/ryanrosello-og/playwright-slack-report) - 将您的 Playwright 测试结果发布到您最喜欢的 Slack 频道。
- [playwright-smart-reporter](https://www.npmjs.com/package/playwright-smart-reporter) - 功能丰富的 HTML 报告器，具有稳定性等级、趋势分析、重试分析、性能跟踪和可选的人工智能驱动的故障分析。
- [playwright-tesults-reporter](https://github.com/tesults/playwright-tesults-reporter) - 用于将测试结果从 Playwright 上传到 Tesults 的库。
- [playwright-xray](https://github.com/inluxc/playwright-xray) - Playwright Xray Reporter，将测试执行发送到 Jira / Xray。
- [qase](https://github.com/qase-tms/qase-javascript/tree/main/qase-playwright) - 剧作家 Qase Reporter，将测试执行发送至 [qase](https://qase.io)。
- [TestDino](https://testdino.com) - 用于 Playwright 测试分析的 AI 云平台，具有即时故障调试、片状测试检测和 ML 分类功能。
- [testomatio-reporter](https://github.com/testomatio/reporter) - 运行测试执行并将其发送到 TCMS testomatio、Jira / Linear / Azure DevOps 任务管理。
- [playwright-timeline-reporter](https://github.com/vitalets/playwright-timeline-reporter) - 交互式时间线报告器，可优化您的测试运行性能和工作人员利用率。

## 展示柜

- [Elastic APM JS agent](https://github.com/elastic/apm-agent-rum-js) - Playwright 用于跨浏览器运行基准测试。
- [playwright-examples](https://github.com/microsoft/playwright-examples) - Playwright 的各种测试场景。
- [TypeScript](https://github.com/microsoft/TypeScript) - Playwright 用于跨浏览器测试 TypeScript.js。
- [VS Code](https://github.com/microsoft/vscode) - Playwright 用于在其 Web 构建上运行跨浏览器测试。
- [xterm.js](https://github.com/xtermjs/xterm.js) - Playwright 用于运行跨浏览器集成测试。

## 指南

- [Currents Blog](https://currents.dev/blog/playwright) - 由 QA 专业人员撰写的剧作家文章。
- [Playwright Tips (videos)](https://www.youtube.com/playlist?list=PLMZDRUOi3a8NtMq3PUS5iJc2pee38rurc) - 使用 Playwright 测试和监控常见挑战的视频演练。
- [Playwright Weekly](https://playwrightweekly.com) - 来自互联网的剧作家文章和新闻的精选聚合器。
- [playwrightsolutions.com](https://playwrightsolutions.com) - 剧作家自动化测试问题和解决方案的精选。
- [serenity-js.org](https://serenity-js.org/handbook/web-testing/your-first-web-scenario/) - 了解如何使用 Playwright 和 Serenity/JS 剧本模式以业务语言编写验收测试。
- [Testing 3D applications with Playwright on GPU](https://blog.promaton.com/testing-3d-applications-with-playwright-on-gpu-1e9cfc8b54a9) - 为 CI 上的 Playwright 测试启用硬件加速的配方。

## 贡献

欢迎投稿！首先阅读[贡献指南](https://github.com/mxschmitt/awesome-playwright/blob/main/CONTRIBUTING.md)。
