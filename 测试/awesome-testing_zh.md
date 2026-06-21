![](https://github.com/TheJambo/awesome-testing/blob/master/AwesomeTesting.jpg?raw=true)

# 很棒的测试 [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
> 测试软件、扩展和资源的精选列表

## 前言
这旨在为软件测试社区中的新人提供资源。它不是针对特定领域（可用性/性能）或角色（自动化/管理）量身定制的。我们的想法是，您可以将此列表交给计算机科学毕业生，这将极大地提高他们的测试技能、效率和整体知识广度。请注意，这适用于编写相关代码后软件测试的所有领域（无单元测试/静态分析！）。

最后，我确信每个阅读此列表的人都有他们想要添加的一件事。请阅读[如何贡献](https://github.com/TheJambo/awesome-testing/blob/master/CONTRIBUTING.md)页面并添加到列表中。 :)

## 内容

- [Software](#software)
- [Books](#books)
- [Training](#training-includes-developer-training-for-automation-testers)
- [Blogs](#blogs)
- [Newsletters](#newsletters)
- [推荐精彩清单](#suggested-awesome-lists)
- [质量保证和测试路线图](#qa-and-testing-road-map)
- [Others](#others)
- [Contributing](#contributing)
- [行为准则](#code-of-conduct)
- [License](#license)


## 软件

### API测试
- [Bruno](https://github.com/usebruno/bruno) - 用于探索和测试 API 的开源 API 客户端。
- [API Status Check](https://apistatuscheck.com) - 适用于 188 多个第三方 API（OpenAI、Stripe、AWS、GitHub 等）的实时状态监控仪表板，具有响应时间跟踪和免费警报级别。
- [Polarity](https://www.polarity.so) - 第一位进行完整E2E、API、UI测试的AI QA工程师。了解您的整个代码库并确保所有相关测试都是使用我们长期运行的代理设置进行的。
- [BitDive](https://bitdive.io/) - Java/Kotlin 的零代码 API 测试平台。捕获深层运行时上下文（HTTP、SQL、方法），根据真实流量自动生成模拟，并启用实时上下文重放以进行 E2E 测试和调试。
- [CORS Tester](https://cors-error.dev/cors-tester/) - 开发人员和 API 测试人员可以使用该工具检查 API 是否针对给定域启用了 CORS 并识别差距。
- [HttpMaster](https://www.httpmaster.net) - 用于 HTTP 测试和调试的专业软件工具。
- [Keploy](https://github.com/keploy/keploy) - API 测试平台可自动生成单元测试用例以及依赖项模拟。
- [RestQA](https://github.com/restqa/restqa) - 基于Gherkin的REST API测试框架。
- [SpecTest](https://github.com/justiceo/spectest) - Js 或纯 JSON 中真正的声明式 API 测试框架。
- [Tests Coverage Tool](https://github.com/Nikita-Filonov/tests-coverage-tool) - 通过测试衡量 gRPC 服务覆盖率的终极工具。
- [Swagger Coverage Tool](https://github.com/Nikita-Filonov/swagger-coverage-tool) - Swagger 覆盖率工具旨在根据 Swagger 文档测量 API 测试覆盖率。它提供 API 测试覆盖率的自动跟踪和报告，有助于确保您的端点和服务经过良好的测试。
- [Webhook Debugger & Logger](https://apify.com/ar27111994/webhook-debugger-logger) - 用于实时测试、调试和记录传入 Webhook 的企业级工具。
- [Webhook Debugger](https://github.com/brancogao/webhook-debugger) - 开源、自托管的 Webhook 检查器，支持签名验证。
- [Spiderhash](https://spiderhash.io/) - Webhook 调试和请求检查工具，用于测试回调有效负载、标头和传递行为。
- [KushoAI](https://kusho.ai/) - 用于 API 合约测试、端到端测试、UI 测试和持续安全扫描的 AI 原生平台，具有自动适应 CI/CD 中代码更改的自我修复测试。
- [postman2pytest](https://github.com/golikovichev/postman2pytest) - 将 Postman Collection v2.1 JSON 文件转换为可立即运行的 pytest 测试套件。

### 安全测试
- [BeEF](http://beefproject.com/) - 通过利用您发现的任何 XSS 漏洞来操纵浏览器。
- [OWASP ZAP](https://github.com/zaproxy/zaproxy) - 用于 HTTP 流量操纵、安全扫描和利用的拦截代理。
- [BurpSuite](https://portswigger.net/burp/communitydownload) - 拦截 API 并根据 API 操作实时回复更改。
- [Nuclei Scanner](https://github.com/projectdiscovery/nuclei) - nuclee 是用于现场常见漏洞查找的自动扫描仪。

### 人工智能和法学硕士测试
- [promptfoo](https://github.com/promptfoo/promptfoo) - 用于测试和红队 LLM 应用程序的开源框架。比较提示、测试 RAG 架构、运行多轮对抗攻击并通过 CI/CD 集成捕获安全漏洞。
- [Tenro](https://github.com/tenro-ai/tenro-python) - AI 代理的开源测试框架。模拟 LLM 和工具调用以测试边缘情况、故障路径和代理逻辑，而无需实时 API 调用。
- [voicetest](https://github.com/voicetestdev/voicetest) - 用于语音 AI 代理的开源测试工具，支持 Retell、VAPI、LiveKit 和 Bland，具有自主模拟和基于 LLM 的评估。
- [AgentSkeptic](https://github.com/jwekavanagh/agentskeptic) - 通过检查执行后的数据库状态、使用只读 SQL 比较预期结果与观察到的结果来验证 AI/代理工作流程。
- [Evaliphy](https://github.com/evaliphy/evaliphy) - 使用 Evaliphy 端到端测试您的 AI 系统。它使用剧作家风格的测试方法并生成 HTML 报告。

### 服务虚拟化
- [Beeceptor](https://beeceptor.com/) - 易于使用无代码模拟服务器进行服务虚拟化。支持 Rest、SOAP、GraphQL。从 OpenAPI 规范或 Postman 集合创建 API 模拟服务器。
- [DeepfakeHTTP](https://github.com/xnbox/DeepfakeHTTP) - 使用 HTTP 转储作为 API 模拟的响应源的 Web 服务器。
- [fakecloud](https://github.com/faiscadev/fakecloud) - 用于集成测试的免费开源本地 AWS 云模拟器，具有 100% 一致性的 23 项服务以及 6 种语言的第一方测试断言 SDK。
- [mockd](https://github.com/getmockd/mockd) - 开源多协议模拟服务器，支持 HTTP、gRPC、GraphQL、WebSocket、MQTT 和 SOAP，具有混沌工程和代理记录。
- [MockServer](https://github.com/mock-server/mockserver-monorepo) - 适用于多种协议（HTTP、gRPC、GraphQL、LLM、MCP、Kafka、TCP 等）的模拟、调试代理和混沌工程工具；模拟任何依赖关系、记录/重播和检查流量、验证请求并注入故障。 Docker、JAR、Helm、多语言客户端。
- [WireMock](https://github.com/wiremock/wiremock) - 用 Java 编写的开源 HTTP 模拟引擎。嵌入您的测试代码、作为独立进程运行或通过 Docker 部署。
- [ApiNotes](https://apinotes.io/mock-server) - 放下您的 OpenAPI 规范，立即获得功能齐全的模拟 API 服务器。导出到Bruno API客户端或直接测试。

### 视觉测试
- [Frostbyte Screenshot Action](https://github.com/OzorOwn/frostbyte-screenshot-action) - GitHub Action，用于 CI/CD 管道中的自动网站屏幕截图。支持多个视口、全页捕获和暗模式模拟。
- [Fluxguard](https://fluxguard.com) - 屏幕截图像​​素和 DOM 变化比较。
- [GoodLooks](https://github.com/dashcamio/goodlooks) - 用于剧作家测试的人工智能视觉验证。
- [Happo](https://happo.io) - 跨浏览器屏幕截图和视觉回归测试服务，与 Storybook、Playwright 和 Cypress 等工具集成。
- [Lastest](https://lastest.cloud) - 通过 AI 碎片分类和基线审查对 Playwright 进行视觉回归测试。
- [TestingBot](https://testingbot.com) - 支持自动、手动和可视化测试。
- [recheck-web](https://github.com/retest/recheck-web) - 更改与 Golden Masters 和“牢不可破的 Selenium”测试的比较工具。
- [Sherlo](https://github.com/sherlo-io/sherlo) - React Native Storybook 的可视化测试平台。在云端的 iOS 和 Android 模拟器上捕获屏幕截图并自动检测视觉变化。
- [wopee.io](https://wopee.io/) - 自主视觉回归测试平台。
- [SmartUI by TestMu AI (formerly LambdaTest)](https://www.testmuai.com/visual-testing-tool/) - AI 原生视觉测试工具，可实现跨浏览器、应用程序、网站和 PDF 的完美 UI。

### UI 和端到端测试
- [Polarity](https://www.polarity.so) - 完整的视觉和桌面环境展示了所有 UI/UX 功能的完整 E2E 测试。在测试运行时为您生成 Playwrite、Cypress 和其他代码。
- [BugBug](https://bugbug.io) - 用于 Web 应用程序的无代码测试自动化工具。
- [Courgette](https://courgette-testing.com) - 使用 Gherkin 进行声明性 BDD UI 测试。
- [DevAssure](https://app.devassure.io) - 在真实浏览器上进行 E2E Web UI 代理测试。可以将代理添加到 Github Actions 以仅测试 PR 中已更改的流。
- [DeviceLab](https://devicelab.dev) - 用于移动测试的私人设备实验室基础设施。连接您自己的 iOS/Android 设备并通过 WebRTC 远程运行 Appium、Maestro 或 XCUITest。零信任架构将测试数据保留在您的网络上。
- [Ferrum](https://github.com/rubycdp/ferrum) - 通过 CDP 和高级 Ruby API 实现 Chrome 自动化。
- [flutter-skill](https://github.com/ai-dashboad/flutter-skill) - 通过 MCP 对 Flutter、React Native、iOS、Android、Electron、Tauri、KMP 和 .NET MAUI 进行 AI 支持的 E2E 测试。零测试代码。
- [Hyperbrowser](https://hyperbrowser.ai) - 具有内置会话记录的可扩展无头浏览器测试。
- [Hercules](https://github.com/test-zeus-ai/testzeus-hercules) - 开源端到端测试代理。
- [Keploy](https://keploy.io) - 开源 AI 支持的 API 和微服务端到端测试工具，可根据实际流量自动生成测试用例和模拟。
- [TestMu AI (formerly LambdaTest)](https://www.testmuai.com) - 全栈代理人工智能质量工程平台，使团队能够智能测试并更快地交付。
- [Mocky Balboa](https://docs.mockybalboa.com/) - 在运行时以声明方式模拟全栈应用程序中的服务器端网络请求
- [Octomind](https://github.com/OctoMind-dev) - 人工智能驱动的测试用例发现和维护。
- [playwright-bdd](https://github.com/vitalets/playwright-bdd) - BDD 风格的剧作家测试。
- [QA Wolf](https://github.com/qawolf/qawolf) - Node.js 库用于更快地创建浏览器测试。
- [tapflow](https://github.com/jo-duchan/tapflow) - 自托管移动 QA 工具，可将 iOS 模拟器和 Android 模拟器流式传输到浏览器，以进行团队范围的测试，无需本地设置。
- [UI Coverage Tool](https://github.com/Nikita-Filonov/ui-coverage-scenario-tool) - UI 覆盖率工具是一种创新的无开销解决方案，用于直接在实际应用程序上跟踪和可视化 UI 测试覆盖率，而不是静态快照。
- [agent-qa](https://github.com/vostride/agent-qa) - 带内存的开源代理 QA 工具。用自然语言编写测试。 agent-qa 使用执行内存在网络和移动设备上运行它们，在发布之前捕获回归。
  
  
### 测试管理
- [Kiwi TCMS](https://github.com/kiwitcms/Kiwi) - 开源测试用例管理。
- [skipper](https://github.com/get-skipper/skipper) - 通过 Google Spreadsheet 进行实时测试执行控制，无需更改代码即可实现即时切换。
- [TestLink](https://github.com/TestLinkOpenSourceTRMS/testlink-code) - 开源测试用例管理系统。
- [Testomatio](https://testomat.io/) - 现代 TCMS 允许同步手动和自动测试。

### 测试数据管理
- [MockHero](https://mockhero.dev) - 用于生成综合测试数据的 REST API。 156 种字段类型、22 个区域设置、关系数据，不到 50 毫秒。提供免费套餐。
- [Synth](https://github.com/getsynth/synth) - 开源测试数据生成器。
- [Touca](https://github.com/trytouca/trytouca) - 用于行为和性能比较的连续回归测试。
- [test-each](https://github.com/ehmicky/test-each) - 数据驱动的测试框架。

### 浏览器扩展和实用程序
- [Anchor Browser](https://anchorbrowser.io) - 具有内置隐形和代理轮换功能的云浏览器基础设施，可用于大规模自动化测试
- [Bug Magnet](https://chrome.google.com/webstore/detail/bug-magnet/efhedldbjahpgjcneebmbolkalbhckfi) - 用于表单测试的基于字段的值建议。
- [Check All](https://chrispederick.com/work/web-developer/) - 提供缺少的“全选”功能。
- [Full Page Screenshot](https://chrome.google.com/webstore/detail/full-page-screen-capture/fdpohaocaechififmbbbbbknoalclacl) - 捕获全页屏幕截图。
- [Form Filler](https://chrome.google.com/webstore/detail/form-filler/bnjjngeaknajbdcgpfkgnonkmififhfo) - 使用虚拟数据自动填写大型表格。
- [ProxySwitcher](https://chrome.google.com/webstore/detail/proxy-switcher-manager/onnfghpihccifgojkpnnncpagjcdbjod) - 测试/生产环境的轻松代理切换。
- [Requestly](https://requestly.io/) - 用于拦截和修改网络请求的轻量级代理。

### 辅助功能和可用性测试
- [Colour Blindness Simulator](https://altreus.github.io/colourblind/) - 模拟不同类型的色盲。
- [RatedWithAI](https://ratedwithai.com) - 由 AI 驱动的网站可访问性扫描仪，可通过即时可操作审核来检查 ADA 和 WCAG 2.2 合规性。
- [VertaaUX CLI](https://github.com/VertaaUX/cli) - 来自终端和 CI 的用户体验、可访问性和转换审核，以及基于分数的质量门和 PR 回归检测。
- [WAVE](https://wave.webaim.org/) - 一套评估工具，可帮助作者让残障人士更容易访问他们的网络内容。

### 性能和负载测试
- [Yslow](http://yslow.org/) - 根据 Yahoo! 的规则分析网页性能。
- [Load Testing Hub Panel](https://github.com/Nikita-Filonov/load-testing-hub-panel) - 用于可视化负载测试结果的终极 Web UI

### Web3 和区块链测试
- [Cannon](https://usecannon.com/) - 以太坊的持续配置自动化。
- [Dapp.tools](https://dapp.tools/) - 以太坊的命令行工具和智能合约库。
- [Ganache](https://trufflesuite.com/ganache/) - 用于运行测试的个人以太坊区块链。
- [Foundry](https://github.com/foundry-rs/foundry) - 用于以太坊开发的快速、模块化工具包。
- [Hardhat](https://hardhat.org/) - 以太坊开发和测试环境。
- [Truffle Suite](https://trufflesuite.com/) - 全面的智能合约开发套件。
- [Robot Framework Solidity Testing Toolkit](https://github.com/jg8481/Robot-Framework-Solidity-Testing-Toolkit) - 用于 Solidity 测试的机器人框架集成。

### 测试自动化框架
- [Jumpstarter](https://github.com/jumpstarter-dev/jumpstarter) - 开源硬件在环测试框架，用于通过 CI/CD 集成对真实和虚拟硬件进行自动化测试。
- [Robot Framework](https://robotframework.org/) - 用于测试和 RPA 的通用开源自动化框架。
- [ai-natural-language-tests](https://github.com/aiqualitylab/ai-natural-language-tests) - 使用 LangGraph、ChromaDB 和多提供商 LLM 支持根据自然语言要求生成 Cypress 和 Playwright E2E 测试。
- [OpenTester](https://github.com/kznr02/OpenTester) - MCP-First 测试框架：AI 代理现在可以像人类一样进行测试

### 屏幕录制和会话重播
- [Captura](https://github.com/MathewSachin/Captura) - 开源视频录制工具。

### 思维导图和文档
- [Xmind](http://www.xmind.net/) - 用于记录测试用例和策略的思维导图工具。

### A/B 测试
- [Kirro](https://kirro.io) - 具有可视化编辑器、贝叶斯统计和 GA4 转化跟踪的 A/B 测试工具。


## 书籍
- [The Scrum Field Guide, Agile advice for your first year and beyond](https://amzn.to/2OERKEm) - 为什么您可能希望将您的公司转向敏捷，以及关于如何做到这一点的实用建议。
- [Fifty quick ideas to improve your Tests](https://amzn.to/2AzMUF7) - 关于如何改进测试以及为什么应该进行测试的精彩示例。非常适合作为赢得争论的证据！
- [Agile Testing: A Practical Guide](https://amzn.to/2n1K2aG) - 为那些希望作为测试人员过渡到敏捷的人提供指南，以及作者如何在他们的敏捷团队中工作。
- [Explore It!: Reduce Risk and Increase Confidence with Exploratory Testing](https://amzn.to/2n8axLn) - 一本关于构建探索性测试和设计测试的非常好的书。
- [The Domain Testing Workbook](https://amzn.to/2Az4l90) - 深入了解当今使用的最常见的测试技术——域测试（也称为边界分析和等价类划分），并提供大量示例以使其变得更好。
- [Don't Make Me Think: A Common Sense Approach to Web Usability](https://amzn.to/2naYmhf) - 一本对于可用性测试非常有用的书。
- [Lessons Learned in Software Testing](https://amzn.to/2LTjM01) - 关于软件测试的最好的书籍之一，分为小节课程，现在和出版时一样适用。
- [UI is Communication](https://amzn.to/2vbiALY) - 如何制作直观的用户界面（UI 和可用性测试）。
- [Thinking, Fast and Slow](https://amzn.to/2vcjasX) - 关于我们如何做出决策以及如何进行实验（实验==测试）。
- [Chaos Engineering: Crash test your applications](https://www.manning.com/books/chaos-engineering) - 一本关于如何设计和执行受控软件故障实验的书。
- [Testing JavaScript Applications](https://www.manning.com/books/testing-javascript-applications) - 一本关于面向开发人员的 JavaScript 测试工具和技术的书。
- [Chaos Engineering](https://www.manning.com/books/chaos-engineering) - 这本书教你设计和执行受控实验来发现隐藏的问题。
- [The Art of Unit Testing, Third Edition](https://www.manning.com/books/the-art-of-unit-testing-third-edition) - 这本书逐步指导您从最初的简单单元测试到构建可维护、可读且值得信赖的完整测试集。
- [Testing Web APIs](https://www.manning.com/books/testing-web-apis) - 通过实施自动化测试流程来保证 Web API 的质量和一致性。
- [Effective Software Testing](https://www.manning.com/books/effective-software-testing) - 为开发人员提供的实践指南，介绍如何以系统且有效的方式创建高质量的测试。

## 培训（包括针对自动化测试人员的开发人员培训）
- [Learn to Code](https://github.com/karlhorky/learn-to-program) - 另一个很棒的开发人员培训列表
- [The Dojo](https://dojo.ministryoftesting.com/) - 直接来自测试社区的课程和讲座。
- [Coursera](https://www.coursera.org/) - 来自顶尖大学的在线课程。
- [Cybrary](https://www.cybrary.it/) - 在线免费安全培训。
- [BBST Testing Courses](https://bbst.courses/bbst-testingeducation-materials/) - 著名的黑盒软件测试（BBST）课程是关于软件测试基础、错误报告和测试设计的大学水平课程。这些材料已获得知识共享许可，可供任何人使用。包括文章、幻灯片和视频讲座。
- [FrontRow](https://github.com/majdukovic/frontrow) - 开源 React Native 移动应用程序构建为 QA 自动化的实践培训界面。跨平台 testID 可在 Maestro、Appium、Espresso 和 XCUITest 上工作，深度 QA 调试菜单可让学员强制执行生产中实际出现的故障模式（4xx、5xx、超时、离线、拒绝权限、拒绝 IAP、过期令牌），而无需后端。

## 博客
- [詹姆斯·巴赫](http://www.satisfice.com/blog/)
- [迈克尔·博尔顿](http://www.developsense.com/blog/)
- [珍妮特·格雷戈里](http://janetgregory.ca/blog/)
- [尼基塔·索博列夫](https://sobolevn.me/)
- [软件测试人员博客](https://www.softwaretester.blog/)
- [自动化熊猫](https://automationpanda.com/)
- [还有其他人](https://github.com/ChristoWolf/awesome-testing-blogs)

## 时事通讯
- [Coding Jag](https://www.testmuai.com/newsletter) - 每周了解 AI、测试、开发、CI/CD 和自动化方面的最新知识，让您保持领先地位。
- [Software Testing Weekly](https://softwaretestingweekly.com/) - 每周五发布的最佳软件测试新闻和工具的精选综述。

## 推荐精彩清单

### 必读
- [Falsehoods](https://github.com/kdeldycke/awesome-falsehood) - 一个有趣且有教育意义的清单，说明了为什么软件开发中没有什么是容易的。您认为可以将婚姻存储在数据库中吗？
- [Naughty Strings](https://github.com/minimaxir/big-list-of-naughty-strings) - 这是著名的 Naughty Strings 列表。如果您正在进行一些现场验证，请不要再寻找灵感。
- [Unicode](https://github.com/jagracey/Awesome-Unicode) - 这是学习 unicode 如何工作及其可能导致的问题的绝佳资源。

### 有用的参考资料
- [The Original](https://github.com/sindresorhus/awesome) - 很棒的清单中的很棒的清单。
- [Learn to Code](https://github.com/karlhorky/learn-to-program) - 学习编码，适合那些希望转向自动化的人
- [Application Security](https://github.com/paragonie/awesome-appsec) - 范围广泛得令人难以置信，但您一定会找到符合要求的东西。
- [Selenium](https://github.com/christian-bromann/awesome-selenium) - 如果你知道自己想要什么，比搜索谷歌更好。
- [Security](https://github.com/sbilly/awesome-security) - 这主要集中在基础设施上，但如果您正在测试一系列系统，这非常有用。
- [Awesome Software Quality](https://github.com/ligurio/awesome-software-quality) - 免费软件测试和验证资源列表。
- [Awesome Cucumber](https://github.com/virajkulkarni14/awesome-cucumber) - 一个（相对较新的）精选的与黄瓜和小黄瓜相关的资源列表。
- [Awesome JMeter](https://github.com/aliesbelik/awesome-jmeter) - 有关 Apache JMeter 的精选资源集合。
- [Awesome Performance Engineering](https://github.com/be-next/awesome-performance-engineering) - 性能工程工具和资源的精选集合，涵盖可观察性和性能测试。
- [How They Test](https://github.com/abhivaikar/howtheytest) - 来自科技公司的精选公共资源，介绍他们如何测试软件和建立质量文化

## 质量保证和测试路线图
- [How to start QA and Testing career](https://github.com/fityanos/Quality-Assurance-Road-Map) - 开始软件测试和自动化职业生涯所需的一系列广泛而丰富的策略、主题和技能。

## 其他
- [Testers Rage Playlist](https://play.spotify.com/user/sanchezni/playlist/5yzT0HrymwEeO8ckqgkPiW) - 测试人员在红雾降临时的协作播放列表。
- [Software Testing Conferences](http://testingconferences.org/) - 软件测试会议和研讨会的列表。
- [Software Testing Interview Tool](https://github.com/TheJambo/ToDoInterviewTest) - 一个非常有问题的待办事项列表，以方便面对面采访。

## 贡献
有关如何贡献的详细信息，请参阅*很棒的测试* [贡献指南](CONTRIBUTING.md)。

## 行为准则
详情请参阅【行为准则】(CODE-OF-CONDUCT.md)。基本上可以归结为：
>为了营造开放和热情的环境，我们
贡献者和维护者承诺参与我们的项目并
我们的社区为每个人提供无骚扰的体验，无论年龄、身体状况如何
身材、残疾、种族、性别认同和表达、经验水平、
国籍、外表、种族、宗教或性认同和取向。


## 许可证
[![CC0](http://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

在法律允许的范围内，[
贡献者](https://github.com/TheJambo/awesome-testing/graphs/contributors)
已放弃本作品的所有版权以及相关或邻接权。请参阅
[许可证文件](LICENSE) 了解详细信息。
