# 很棒的视觉回归测试 [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

> 精选的精彩视觉回归测试资源列表。

回归测试是一种软件测试，它验证先前开发和测试的软件在更改或与其他软件交互后仍然以相同的方式运行。回归测试的目的是确保对软件的更改没有引入新的故障。

## 前言

这是关于视觉回归测试的“不完整”资源列表。它不是针对特定领域或角色（开发人员/QA/UX 设计师）量身定制的。请注意，这适用于编写相关代码*之后*进行回归软件测试的所有领域。有关一般软件测试的精彩列表，请参阅例如[真棒测试](https://github.com/TheJambo/awesome-testing)。

最后，我确信每个阅读此列表的人都有他们想要添加的一件事。请阅读[如何贡献](.github/CONTRIBUTING.md) 页面并**随意添加到列表中!!**。如果您认为这有帮助**请给一个星星⭐️**。

## 内容

- [一般信息](#general-information)
- [浏览器自动化](#browser-automation)
- [工具和框架](#tools-and-frameworks)
- [在线服务](#online-services)
- [博客文章](#blog-posts)
- [幻灯片、讲座和视频](#slideshows-talks-and-videos)
- [Deprecated](#deprecated)
- [Miscellaneous](#Miscellaneous)
  - [Contributing](#contributing)
  - [行为准则](#code-of-conduct)
  - [License](#license)

## 一般信息

- [基于屏幕截图的 CSS 测试工具调查](https://gist.github.com/cvrebert/adf91e429906a4d746cd)
- [维基百科：回归测试](https://en.wikipedia.org/wiki/Regression_testing)

## 浏览器自动化

- [Cypress.io](https://www.cypress.io/) - 在浏览器中运行的自动化框架。
- [Selenium](https://github.com/SeleniumHQ/selenium) - 浏览器自动化框架和生态系统。
- [SlimerJS](https://github.com/laurentj/slimerjs) - 可编写脚本的浏览器，例如基于 Firefox 的 PhantomJS。
- [Webdriver.io](https://github.com/webdriverio/webdriverio/) - W3C WebDriver 协议的 Node.js 绑定实现。

## 工具和框架 (a-z↓)

- [AET](https://github.com/Cognifide/aet) - 可扩展的测试工具，提供视觉回归测试、可访问性和性能验证、标记分析等。
- [AyeSpy](https://github.com/newsuk/ayespy) - 90 秒内比较 44 幅图像。
- [BackstopJS](https://github.com/garris/BackstopJS) - 配置驱动的自动化屏幕截图测试框架。
- [basset](https://basset.io) - 用于生成和审查视觉差异的开源平台。支持多种浏览器、github 和 Slack 集成。
- [BitDive](https://bitdive.io/) - BitDive 是一个针对 Java/Kotlin 应用程序的零代码回归测试工具。它捕获真实的运行时行为（方法、SQL、HTTP），并通过自动模拟启用实时上下文重放，以检测版本之间的语义偏差。
- [BFFless](https://bffless.app) - 自托管平台，用于通过 GitHub Actions 集成托管和查看来自 CI/CD 管道的视觉回归屏幕截图。
- [Chimp](https://github.com/xolvio/chimp) - 通过实时反馈开发验收测试和端到端测试。
- [CodeceptJS](https://github.com/codeception/codeceptjs/) - NodeJS 的现代验收测试框架。
- [Creevey](https://github.com/wKich/creevey) - 神奇的跨浏览器视觉测试。功能丰富的工具，具有 UI Runner、测试热重载、Docker 和 Storybook 集成。
- [CSSCritic](https://github.com/cburgmer/csscritic) - 轻量级 CSS 回归测试。
- [Differencify](https://github.com/NimaSoroush/differencify) - 使用 [Puppeteer](https://github.com/GoogleChrome/puppeteer) 进行视觉回归测试的库。
- [DiffGoblin Action](https://github.com/neg-0/diffgoblin-action) - GitHub Action，截取两个 URL 并将视觉差异作为 PR 评论发布。零配置，无需外部服务。
- [ember-visual-test](https://github.com/Cropster/ember-visual-test) - [Ember](https://emberjs.com/) 的简单视觉回归测试。
- [FuncUnit](https://github.com/bitovi/funcunit) - 基于 jQuery 的功能测试套件
- [Frostbyte Screenshot Action](https://github.com/OzorOwn/frostbyte-screenshot-action) - GitHub Action 用于 CI/CD 中的自动网站屏幕截图。基于API（无本地浏览器），支持5个视口、全页捕获、深色模式。
- [Galen](https://github.com/galenframework/galen) - 基于[Selenium](https://github.com/SeleniumHQ/selenium)的Java框架。
- [gatling](https://github.com/gabrielrotbart/gatling) - 集成的视觉 RSpec 匹配器使真正的视觉测试变得容易（Ruby）。
- [grunt-photobox](https://github.com/stefanjudis/grunt-photobox) - 该插件可通过站点的屏幕截图照片会话来防止您的项目布局损坏。
- [Happo](https://github.com/happo/happo.io) - CI 中用户界面的视觉差异。
- [Hardy](https://github.com/thingsinjars/Hardy) - Selenium 驱动、Cucumber 驱动的 CSS 测试。
- [jest-image-snapshot](https://github.com/americanexpress/jest-image-snapshot) - 使用 [pixelmatch](https://www.npmjs.com/package/pixelmatch) 执行图像比较的玩笑匹配器
- [jest-puppeteer-react](https://github.com/Hapag-Lloyd/jest-puppeteer-react) - 使用 Jest 和 puppeteer 对 React 组件进行视觉回归测试
- [Karma](http://karma-runner.github.io/latest/index.html) - AngularJS 团队的测试运行程序可以满足我们的所有需求。
- [Lastest](https://github.com/las-team/lastest) - 基于 Playwright 构建的视觉回归测试平台，具有屏幕截图比较、基线审查和 AI 碎片分类功能。通过 docker-compose 或 k8s 自托管。
- [Loki](https://github.com/oblador/loki) - 在 docker 等中使用 Chrome 对 Storybook 进行视觉回归测试。
- [Look-alike](https://github.com/kdzwinel/Look-alike) - 用于拍摄和比较屏幕截图的 Chrome 扩展。
- [Lost Pixel](https://github.com/lost-pixel/lost-pixel) - 对整页、组件（通过 Storybook 和 Ladle 集成）和自定义镜头（例如通过 Cypress）进行整体视觉回归测试。
- [Muppeteer](https://github.com/HuddleEng/Muppeteer) - 使用 [Mocha](https://mochajs.org/) 和 [Puppeteer](https://github.com/GoogleChrome/puppeteer) 的 Chrome 视觉回归测试框架。
- [Needle](https://github.com/python-needle/needle) - Needle 是一个使用 Selenium 和 Noose (Python) 测试视觉效果的工具。
- [Nightmare](https://github.com/segmentio/nightmare) - 基于 Electron 的高级浏览器自动化库。
- [Nightwatch](https://github.com/nightwatchjs/nightwatch) - 基于Node.js并使用Webdriver协议的自动化测试和持续集成框架。
- [OSnap](https://github.com/eWert-Online/osnap) - 适用于您的项目的快速且易于使用的快照测试工具（1200 个快照将在 3 分钟内运行）。
- [Playwright](https://github.com/microsoft/playwright) - Node 库可通过单个 API 实现 Chromium、Firefox 和 WebKit 的自动化。
- [Protractor](https://github.com/angular/protractor) - Angular 应用程序的 E2E 测试框架。
- [Puppeteer](https://github.com/GoogleChrome/puppeteer) - 无头 Google Chrome 节点 API。
- [qd_screenshottests](https://www.drupal.org/project/qd_screenshottests) - 基于 CasperJS 的 UI 回归和功能测试主要针对 Drupal 8 站点。
- [reg-cli](https://github.com/bokuweb/reg-cli) - 可视化回归测试工具，输出易于阅读的单文件 html 报告。
- [reg-suit](https://github.com/reg-viz/reg-suit) - 视觉回归测试套件可比较图像、存储快照并将差异通知给您的 GitHub 存储库。
- [ResembleJS](https://github.com/Huddle/Resemble.js) - 使用 Javascript 和 HTML5 分析和比较图像。
- [Selenide](https://github.com/selenide/selenide) - 由 Selenium WebDriver 支持的框架，用于用 Java 编写易于阅读和易于维护的自动化测试。
- [Shoov](https://github.com/shoov/shoov) - UI 回归和功能测试主要针对 Drupal 7 站点。
- [Spectre](https://github.com/wearefriday/spectre) - 提供图像比较功能和用于管理屏幕截图的管理界面。
- [test-crawler](https://github.com/apiel/test-crawler) - 视觉回归测试，通过抓取网站并提供快照比较报告。
- [TestCafe](https://github.com/DevExpress/testcafe) - 现代 Web 开发堆栈的自动化浏览器测试。
- [Touca](https://github.com/trytouca/trytouca) - 开源连续回归测试，无需管理快照文件的麻烦。
- [vrtest](https://github.com/nathanmarks/vrtest) - JavaScript 库，用于通过 selenium 在跨浏览器的组件上运行视觉回归测试。
- [wdio-visual-regression](https://github.com/ennjin/wdio-visual-regression) - webdriver.io 的视觉回归工具
- [Wendigo](https://github.com/angrykoala/wendigo) - 基于 Puppeteer 的面向测试的浏览器自动化库。
- [Wraith](https://github.com/BBC-News/wraith) - 易于使用的 ruby​​ 工具，支持 docker。
- [Zombie.js](http://zombie.js.org/) - 使用 Node.js 进行极其快速的无头全栈测试。

## 在线服务（a-z↓）

- [applitools](https://applitools.com) - 云基础视觉测试。
- [Argos](https://argos-ci.com) - 适用于现代工程团队的开源视觉测试平台。
- [Axcept](https://axcept.io) - 对整个团队进行测试。最多可并行进行 100 个测试。端点模拟。代码覆盖率。
- [Browser Shots](http://browsershots.org) - 仅截图。
- [browserling](https://www.browserling.com) - 实时交互式跨浏览器测试。
- [BrowserStack](https://www.browserstack.com) - 免费开源。支持[Selenium Webdriver](https://github.com/SeleniumHQ/selenium/tree/master/javascript/node/selenium-webdriver)。
- [BugBug.io](https://bugbug.io/) - 用于 Web 应用程序的轻量级测试自动化工具。易于学习，不需要编码。它是免费的，并且有无限的测试。只需支付额外的月费，您还可以获得云监控和 CI/CD 集成。
- [Chromatic](https://www.chromatic.com/) - 组件库的可视化测试和 UI 审查。基于云。 [视频](https://youtu.be/6KDLJBcutQE)
- [CrossBrowserTesting](https://crossbrowsertesting.com) - 在 1500 多个真实浏览器和移动设备上进行手动和探索性测试。
- [Diffy](https://diffy.website) - 基于云的视觉回归工具，专注于 Drupal 和 WordPress。全页屏幕截图和最少的误报。只需提供您网站的 URL 即可开始。无需编码。
- [Fluxguard](https://fluxguard.com) - 屏幕截图像​​素和 DOM 变化比较和回归。
- [Ghost Inspector](https://ghostinspector.com) - 请参阅[介绍视频](https://vimeo.com/ghostinspector/intro)。
- [Happo](https://happo.io/) - 基于云的屏幕截图测试服务，支持多种浏览器。
- [HeadSpin](https://www.headspin.io/) - HeadSpin 的回归测试为您提供了一个强大的比较工具，用于分析新应用程序构建、操作系统版本、功能添加、位置等方面的退化情况。
- [Keploy](https://keploy.io) - 开源回归测试工具，可根据真实的 API 调用自动生成测试用例和模拟。

- [LambdaTest](https://www.lambdatest.com/) - 在 2000 多个真实浏览器和操作系统上在线执行自动化和实时交互式跨浏览器测试。
- [Meticulous.ai](https://meticulous.ai) - 无需编写代码即可轻松创建前端测试。使用 Meticulous 记录 Web 应用程序上的工作流程。然后，您可以在新的前端代码上重播这些流程，并通过比较两个重播来创建测试。
- [Micoo](https://github.com/Mikuu/Micoo) - 所有UI应用视觉回归解决方案的开源服务
- [MyVisReg](https://myvisreg.com) - 直接在浏览器中运行视觉回归测试，无需安装或设置。
- [PageBolt](https://pagebolt.dev) - 屏幕截图、视频录制、PDF 和页面检查 API，具有设备模拟、广告拦截和 cookie 横幅删除功能。
- [percy.io](https://percy.io) - 对网络应用程序进行持续的视觉审查。
- [Pixeleye](https://pixeleye.io/home) - 开源、多浏览器视觉审查和测试平台，可选择自行托管。它对 Storybook、Cypress、Playwright 和 Puppeteer 提供一流的支持。
- [Preflight: Cypress Recorder](https://cypress.preflight.com) - 在浏览器中创建人工智能驱动的赛普拉斯测试/POM 模型，并自动化赛普拉斯的电子邮件和视觉测试。
- [Preflight](https://preflight.com) - 最简单的视觉回归测试和自动化 Web 测试工具。 （有限）免费使用。
- [Reflect](https://reflect.run) - 可视化回归测试和测试自动化工具。
- [screener.io](https://screener.io) - 对于 React，看起来是开源的。
- [screenster.io](http://screenster.io) - 适用于 Web 和移动 UI 的基于云的自动化测试平台。
- [Sherlo](https://github.com/sherlo-io/sherlo) - React Native Storybook 的可视化测试平台。在云端的 iOS 和 Android 模拟器上捕获屏幕截图并自动检测视觉变化。
- [TestGrid](https://www.testgrid.io/) - 执行端到端测试自动化，无论是跨浏览器测试、移动应用程序测试、性能测试还是云端或本地的 API 测试。
- [TestingBot](https://testingbot.com) - 提供超过 3600 个浏览器来运行自动化视觉测试。免费开源。
- [Testomat.io Reporter](https://github.com/testomatio/reporter) - 允许将测试收集到 testomat.io 等测试用例管理系统 (TCMS)，并将手动和自动测试同步到一处。
- [testRigor](https://testrigor.com) - 适用于 Web、移动和桌面测试的端到端功能测试自动化工具。
- [Vidiff](https://vidiff.com) - 基于云的跨阶段视觉回归测试。
- [Visual Knight](https://visual-knight.io/) - 基于云的可视化测试平台，为测试工具提供实时结果。
- [Visual Regression Tracker](https://github.com/Visual-Regression-Tracker/Visual-Regression-Tracker) - 用于视觉回归测试的开源自托管服务
- [VisWiz.io](https://www.viswiz.io) - 灵活的视觉回归测试服务。
- [VRTs - Visual Regression Tests](https://bleech.de/en/products/visual-regression-tests/) - WordPress 插件会在内容更新时自动更新屏幕截图，防止误报。
- [Wopee.io](https://wopee.io) - 具有人工智能驱动的测试代理的自主视觉回归测试平台。与 Playwright、Cypress 和 Robot Framework 集成。

## 博客文章 (a-z↓)

- [Angela Riggs: Visual Regression Testing with BackstopJS](https://www.metaltoad.com/blog/visual-regression-testing-backstopjs) - 使用 BackstopJS 的教程。
- [在 Bitbucket 管道中使用无头 Chrome、Puppeteer 和 Pixelmatch 进行自动屏幕截图比较测试](https://jakobzanker.de/blog/automated-screenshot-comparison-test-with-headless-chrome-in-bitbucket-pipeline/)
- [使用 Puppeteer 自动进行视觉比较](https://meowni.ca/posts/2017-puppeteer-tests/)
- [Chromeless, Chrominator, Chromy, Navalia, Lambdium, GhostJS, AutoGCD](https://medium.com/@kensoh/chromeless-chrominator-chromy-navalia-lambdium-ghostjs-autogcd-ef34bcd26907) - Headless Chrome 正在改变传统的自动化测试方法。
- [CodeLift: Introduction to Diffy for Visual Regression Testing](https://codelift.ai/resources/tech-articles/introduction-diffy-visual-regression-testing) - 在投入生产之前发现视觉和功能问题。
- [Everything you need to know about Visual Regression Testing in 2022](https://david-x.medium.com/the-state-of-visual-regression-testing-in-2022-5de10ffe8f6f) - 使用截至 2022 年更新的工具介绍视觉回归测试。
- [Garris Shipon: Automating CSS Regression Testing](https://css-tricks.com/automating-css-regression-testing/) - 使用 BackstopJS 的教程。
- [Garris Shipon: Visual Regression Testing For Angular Applications](https://davidwalsh.name/visual-regression-testing-angular-applications) - 使用 BackstopJS 的教程。
- [Keeping a React Design System consistent: using visual regression testing to save time and headaches](https://techblog.commercetools.com/keeping-a-react-design-system-consistent-f055160d5166) - 使用 percy 和 jest puppeteer 直观地测试 React 组件库。
- [Kevin Lamping: The 5 best visual regression testing tools](http://www.creativebloq.com/features/the-5-best-visual-regression-testing-tools) - 比较：Wraith、PhantomCSS、Gemini、WebdriverCSS 和 Spectre。
- [Make visual regression testing easier](https://medium.com/@nima.soroush.h/make-visual-regression-testing-easier-4a3dc7073737) - [Differencify](https://github.com/NimaSoroush/differencify) 简介以及如何使用它。
- [Pavels Jelisejevs: Visual Regression Testing with PhantomCSS](https://www.sitepoint.com/visual-regression-testing-with-phantomcss) - PhantomCSS 简介。
- [Phillip Gourley: Making visual regression useful](https://medium.com/@philgourley/making-visual-regression-useful-acfae27e5031) - 为什么你应该使用 BackstopJS。
- [Poor man's visual regression testing](https://idkshite.com/posts/compare-visual-changes) - 使用 PerfectPixel chrome 插件改进了手动视觉回归测试。
- [theheadless.dev](https://theheadless.dev) - 包含有关 Playwright 和 Puppeteer 的实用指南和可运行示例的博客。
- [UI Visual Regression Testing with Micoo](https://mikuu.medium.com/ui-visual-regression-testing-with-micoo-12c7a4a036b9) - 介绍如何使用Micoo服务进行视觉回归测试
- [Visual Regression Test with WebdriverIO & WebdriverCSS](https://medium.com/@dalenguyen/visual-regression-test-with-webdriverio-webdrivercss-d7675a1812b2) - 使用 WebdriverIO 和 WebdriverCSS 与 Spec Reporter 的教程
- [Visual regression testing for Hugo with Github-CI and BackstopJS](https://jameskiefer.com/posts/visual-regression-testing-for-hugo-with-github-ci-and-backstopjs/) - 如何使用 BackstopJS 对 Hugo 进行自动化回归测试
- [Visual regression testing using Jest, Chromeless and AWS Lambda](https://github.com/novemberfiveco/visual-regression-testing-jest-chromeless) - 使用 Chromeless 和 jest-image-snapshot 的教程。
- [Visual Regression Testing with Puppeteer & Jest](https://www.viswiz.io/help/tutorials/puppeteer) - 使用 Puppeteer、Jest 和 VisWiz.io 设置可视化测试的教程。

## 幻灯片、讲座和视频 (a-z↓)

- [CSS Regression Testing with Wraith](https://youtu.be/gE_19L0l2q0) - 截屏视频：屏幕截图比较工具 Wraith 的基本介绍。
- [Cypress in 100 Seconds](https://www.youtube.com/watch?v=BQqzfHQkREo&ab_channel=Fireship) - Fireship 的介绍视频。
- [Look-alike - visual regression testing tool](https://youtu.be/vTyoQuC0To8) - 演示 Look-alike Chrome 扩展是什么、它是如何工作的以及它是如何构建的以及为何构建。
- [Screencast on CSS critic - a lightweight testing framework for CSS](https://youtu.be/AqQ2bNPtF60) - 如何使用 CSS Critic 编写你的第一个 CSS 测试，使其通过、破坏它，然后使其再次通过。
- [Screenster Tutorial](https://youtu.be/Zy8y_dGzZXI) - 有关如何使用 Screenster 创建可视化自动化测试的教程。
- Nikhil Verma 的[视觉回归测试 - 从工具到流程](https://speakerdeck.com/nikhilverma/visual-regression-testing-from-a-tool-to-a-process) - Badoo 中的移动 Web 团队如何将 PhantomCSS 转换并集成到他们的工作流程中，并将其连接到他们的 CI 流程。
- [Visual Regression Testing with PhantomCSS](https://youtu.be/Vp8vnXMjIfw) - Jon Bellah 讲述如何在 WordPress 开发过程中使用 PhantomCSS。
- [Visual Regression Testing with Shoov](https://youtu.be/CBBiJ6YlXLc) - 如何设置 shov 并编写第一个测试。
- [Visual Regression Testing: Sanity Checks With BackstopJS](https://youtu.be/l8lGj8Zh0k4) - 包含代码演示和最佳实践的截屏视频。
- [Scaling up your Screenshot Testing, without the Friction](https://www.youtube.com/watch?v=9sarjgIHF2g) - 来自 Droidcon/Fluttercon India 的针对移动设备的演讲。解释了扩大屏幕截图测试的瓶颈以及如何解决这些瓶颈。

## 已弃用 (a-z↓)

以下项目不再积极维护，但由于其用户基础仍然值得一提。

- [CasperJS](https://github.com/casperjs/casperjs) - PhantomJS 和 SlimerJS 的导航脚本和测试实用程序。 （2018 年存档）
- [Chromeless](https://github.com/graphcool/chromeless) - Chrome 自动化变得简单。在 AWS Lambda 上本地运行或无头运行。 （2018 年存档）
- [DalekJS](https://github.com/dalekjs/dalek) - 使用 JavaScript 进行自动化跨浏览器测试。自 2017 年 6 月 4 日起不再维护。
- [dpxdt](https://github.com/bslatkin/dpxdt) - 使用 Python 进行端到端测试。
- [Gemini](https://github.com/gemini-testing/gemini) - 功能丰富的框架，支持 [Selenium](https://github.com/SeleniumHQ/selenium) 和 [CasperJS](https://github.com/casperjs/casperjs)。双子座已被弃用，请使用赫敏代替。
- [Huxley](https://github.com/facebookarchive/huxley) - 基于[Selenium Webdriver](https://github.com/SeleniumHQ/selenium/tree/master/javascript/node/selenium-webdriver)的Python框架。
- [Navalia](https://github.com/joelgriffith/navalia) - 基于无头 Chrome 和 GraphQL 的浏览器自动化。 （2018 年存档）
- [OcularJS](https://github.com/mmacartney10/ocularjs) - 使用 [PhantomJS](https://github.com/ariya/phantomjs)。
- [PhantomCSS](https://github.com/Huddle/PhantomCSS) - 使用 PhantomJS 或 SlimerJS 进行视觉/CSS 回归测试。自 2017 年 12 月 22 日起不再维护。
- [PhantomFlow](https://github.com/Huddle/PhantomFlow) - 基于决策树的 UI 测试实验方法。
- [PhantomJS](https://github.com/ariya/phantomjs) - 可编写脚本的无头 WebKit。自 2018 年 6 月 2 日起不再维护。
- [trifleJS](https://github.com/sdesalas/trifleJS) - Internet Explorer 的无头自动化。 （最后更新2016年）
- [Visual Review](https://github.com/xebia/VisualReview) - 用于测试和审查视觉回归的人性化工具。
- [WebdriverCSS](https://github.com/webdriverio/webdrivercss) - WebdriverCSS 位于 [Webdriver.io](https://github.com/webdriverio/webdriverio/) 之上，并挂钩到 [Selenium](https://github.com/SeleniumHQ/selenium)。

## 杂项

### 贡献

有关如何贡献的详细信息，请参阅[贡献指南](.github/CONTRIBUTING.md)。

### 行为准则

详情请参阅【行为准则】(.github/CODE-OF-CONDUCT.md)。基本上可以归结为：
> 为了营造开放和热情的环境，我们
贡献者和维护者承诺参与我们的项目并
我们的社区为每个人提供无骚扰的体验，无论年龄、身体状况如何
身材、残疾、种族、性别认同和表达、经验水平、
国籍、外表、种族、宗教或性认同和取向。

### 许可证

[![CC-BY-SA](http://mirrors.creativecommons.org/presskit/buttons/88x31/svg/by-sa.svg)](http://creativecommons.org/licenses/by-sa/4.0/)

本作品根据 [知识共享署名-相同方式共享 4.0 国际许可证](http://creativecommons.org/licenses/by-sa/4.0/) 获得许可。
许可证持有者是[所有贡献者](https://github.com/mojoaxel/awesome-regression-testing/graphs/contributors)。
