# 很棒的硒 [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

> 令人愉快的 [Selenium](http://www.seleniumhq.org/) [资源](#resources) 的精选列表。

受到 [awesome](https://github.com/sindresorhus/awesome) 列表的启发。

## 资源

- [Tools](#tools)
- [CSS 回归测试](#css-regression-testing)
- [Containers](#containers)
- [Driver](#driver)
- [桌面工具](#desktop-tools)
- [硒网格](#selenium-grid)
- [云服务](#cloud-services)
- [设备农场](#device-farms)
- [网页抓取/挖掘](#web-scraping--mining)
- [Specifications](#specifications)
- [Blogs](#blogs)

### 工具

#### JavaScript

- [selenium-webdriver](https://github.com/SeleniumHQ/selenium/wiki/WebDriverJs) - 来自 Selenium 项目的官方 WebDriver JavaScript 绑定。
- [WD](https://github.com/admc/wd) - WebDriver/Selenium 2 node.js 客户端。
- [WebdriverIO](http://webdriver.io) - 通过预定义的 50 多个操作更好地实现 WebDriver 绑定。
- [Zombie.js](http://zombie.js.org/) - 极其快速的无头全栈测试。
- [SlimerJS](http://slimerjs.org/) - 适合 Web 开发人员的可编写脚本的浏览器。
- [Nightwatch](http://nightwatchjs.org/) - 高效且简单的 Javascript 端到端测试。
- [Karma](http://karma-runner.github.io/0.12/index.html) - 为开发人员提供高效的测试环境以进行单元测试（主要是 AngularJS）。
- [Protractor](https://angular.github.io/protractor/) - Protractor 是 AngularJS 应用程序的端到端测试框架。
- [CodeceptJS](http://codecept.io/) - NodeJS 的现代验收测试框架。

#### 红宝石

- [Selenium with Ruby](http://seleniumhq.github.io/selenium/docs/api/rb/index.html) - 硒红宝石绑定
- [Watir](http://watir.github.io) - 无害的自动化测试
- [Anemone](https://github.com/chriskite/anemone) - 海葵网络蜘蛛框架。
- [Mechanize](http://docs.seattlerb.org/mechanize/) - 与网站的自动化交互。
- [Spidr](https://github.com/postmodern/spidr) - 网络蜘蛛库，可以蜘蛛一个网站、多个域、某些链接或无限。
- [cobweb](https://rubygems.org/gems/cobweb) - 网络爬虫，可以使用resque进行集群爬取，快速爬取超大网站。
- [Capybara](https://rubygems.org/gems/capybara) - 用于基于机架的 Web 应用程序的集成测试工具。它模拟用户如何与网站交互。

#### PHP
- [Facebook WebDriver](https://github.com/facebook/php-webdriver) - Webdriver 的 PHP 客户端。
- [Selenium Setup](https://github.com/bogdananton/Selenium-Setup) - PHP 开发人员启动自己的 Selenium 服务器的工具。
- [Steward](https://github.com/lmc-eu/steward) - 将 php-webdriver 与 PHPUnit 集成的测试运行程序。

#### 蟒蛇

- [Selenium with Python](http://selenium-python.readthedocs.io/) - Selenium Python 绑定
- [Helium](https://github.com/mherrmann/selenium-python-helium) - Helium 使 Selenium 的使用更容易、更快捷
- [Selene](https://github.com/yashaka/selene) - 受Selenide启发的简洁易读的自动化测试框架，像Selenide一样很好地支持Ajax。
- [mechanize](http://wwwsearch.sourceforge.net/mechanize/) - 有状态的程序化网页浏览。
- [Robot](http://robotframework.org/) - Robot Framework 是用于验收测试和 ATDD 的通用测试自动化框架。
- [behave-webdriver](https://github.com/spyoungtech/behave-webdriver) 使用 Selenium 和 Python 进行行为驱动测试。

#### 爪哇

- [Selenium with Java](http://seleniumhq.github.io/selenium/docs/api/java/index.html) - Selenium Java 绑定
- [Conductor](http://conductor.ddavison.io) - 涡轮增强的 Selenium 框架使测试编写变得轻而易举。
- [darcy](https://github.com/darcy-framework/darcy-webdriver) - 用于结构化、可维护自动化的页面对象框架。
- [Selenide](https://github.com/codeborne/selenide) - 一个使用 Fluent API 编写易于阅读和易于维护的自动化测试的框架。 Selenide 有一个神奇的技巧，可以解决大多数 Ajax 和超时问题。
- [Galen Framework](http://galenframework.com/) - 自动测试响应式网站的外观。
- [Serenity](http://www.thucydides.info/) - 它是一个开源库，用于更快地编写质量更好的自动化验收测试。 （以前的修昔底德）。
- [seleniumQuery](https://github.com/seleniumQuery/seleniumQuery) - Java 中用于 WebDriver 的类似 jQuery 的跨驱动程序接口。它被设计为薄层，可以单独使用，也可以在您最喜欢的框架之上使用，只是为了在需要时简化某些情况（例如断言/等待）。
- [WebDriverManager](https://github.com/bonigarcia/webdrivermanager) - Selenium WebDriver 二进制文件的自动管理。
- [Lightning](https://github.com/aerokube/lightning-java) - 轻量且快如闪电的 WebDriver 客户端。

#### C#

- [Selenium with C#](http://seleniumhq.github.io/selenium/docs/api/dotnet/index.html) - Selenium C# 绑定
- [Atata](https://github.com/atata-framework/atata) - 基于 Selenium WebDriver 的自动化 Web 测试全功能框架。
- [Strontium](https://github.com/jimevans/strontium) - Selenium/WebDriver（远程）服务器的 .NET 实现（但已过时）

#### 格罗维

- [Geb](http://www.gebish.org/) - 它可用于脚本编写、抓取和一般自动化，或者通过与 Spock、JUnit 和 TestNG 等测试框架集成，同样作为功能/网络/验收测试解决方案。

#### 飞镖

- [dart.webdriver](https://github.com/google/webdriver.dart) - 为 Dart 提供 WebDriver 绑定。它们使用 WebDriver JSON 接口，因此需要使用 WebDriver 远程服务器。

### CSS 回归测试

- [WebdriverCSS](https://github.com/webdriverio/webdrivercss) - [WebdriverIO](http://webdriver.io) 回归测试工具（目前已弃用，请暂时使用 [wdio-screenshot](https://www.npmjs.com/package/wdio-screenshot)）。

- [Website-Diff](https://github.com/GeiserX/Website-Diff) - 智能网页比较工具，支持 Wayback Machine 和通过 Selenium 进行视觉回归测试。

- [Wopee.io](https://wopee.io) - 具有人工智能驱动的测试代理的自主视觉回归测试平台。与 Playwright、Cypress 和 Robot Framework 集成。

### 集装箱

#### 码头工人

- [elgalu/docker-selenium](https://github.com/elgalu/docker-selenium) - Docker 中的 Selenium 与 Chrome 和 Firefox 以及视频录制支持。
- [Ggr](https://github.com/aerokube/ggr) - 用于创建大型 Selenium 集群的轻量级负载均衡器。
- [SeleniumHQ/docker-selenium](https://github.com/SeleniumHQ/docker-selenium) - 适用于 Chrome 和 Firefox 的 Selenium 独立服务器、集线器和节点配置的 Docker 映像。
- [Selenoid](https://github.com/aerokube/selenoid) - 一个轻量级的 Selenium hub 实现，在 Docker 容器中启动浏览器。
- [zalando/zalenium](https://github.com/zalando/zalenium) - 允许任何人拥有一次性且灵活的 Selenium Grid 基础设施
- [bravostudiodev/bravo-grid](https://github.com/bravostudiodev/bravo-grid) - Selenium Grid Extras 的 Docker 镜像/设置（参见 Selenium Grid 部分），用于提供远程 Sikuli 测试/自动化执行和网格节点文件上传/下载支持。

#### 库伯内斯
- [kubernetes/examples](https://github.com/kubernetes/examples/tree/master/staging/selenium) - Kubernetes 集群上 Selenium Hub 和节点的示例部署
- [Moon](https://github.com/aerokube/moon) - 使用 Kubernetes 启动浏览器的商业闭源企业 Selenium 实现
- [Callisto](https://github.com/wrike/callisto) - 用于在 Kubernetes 中启动浏览器的开源工具。为每个 selenium 会话创建单独的会话。
- [WebGrid](https://github.com/TilBlechschmidt/WebGrid) - 开源、去中心化、可扩展且强大的 Selenium-grid 等价物。

### 司机

#### 桌面（浏览器）

- [Firefox](https://github.com/SeleniumHQ/selenium/wiki/FirefoxDriver) - Firefox 驱动程序（适用于 FF < v48）包含在可下载的 selenium-server-standalone.jar 中。
- [Geckodriver](https://github.com/mozilla/geckodriver) - Firefox 驱动程序（适用于 FF > v48），受 Selenium >= v3 支持
- [Chrome](https://sites.google.com/a/chromium.org/chromedriver/home) - ChromeDriver 是一个独立的服务器，它为 Chromium 实现 WebDriver 的有线协议。
- [Internet Explorer](https://github.com/SeleniumHQ/selenium/wiki/InternetExplorerDriver) - InternetExplorerDriver 是一个独立的服务器，它实现了WebDriver 的有线协议。
- [Edgedriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) - 适用于 Edge 的 Microsoft Webdriver 服务器
- [Safari](https://github.com/SeleniumHQ/selenium/wiki/SafariDriver) - SafariDriver 是作为 Safari 浏览器扩展实现的。该驱动程序反转了传统的客户端/服务器关系，并使用 WebSocket 与 WebDriver 客户端进行通信（仅支持 Safari <= v9，与 macOS Sierra 一起提供的所有新 Safari 版本都附带 Apple 闭源的集成 SafariDriver）。
- [Opera](https://github.com/operasoftware/operachromiumdriver/blob/master/README.md) - OperaDriver 是由 Opera Software 和志愿者开发的供应商支持的 WebDriver 实现，为 Opera 实现了 WebDriver API。

#### 移动设备（浏览器和应用程序）

- [Appium](http://appium.io/) - Appium 是一个开源测试自动化框架，可与本机和混合移动应用程序一起使用。它使用 WebDriver 协议驱动 iOS、Android 应用程序。
- [Selendroid](http://selendroid.io/mobileWeb.html) - Selendroid 基于 Android 仪器框架。
- [ios-driver](http://ios-driver.github.io/ios-driver/) - 使用 Selenium / WebDriver 测试任何 IOS 本机、混合或移动 Web 应用程序。
- [WebDriverAgent](https://github.com/manishPatwari/WebDriverAgent) - 用于 iOS 的 WebDriver 服务器，可通过 WebDriver API 远程控制设备。

#### 桌面 GUI 自动化（非以浏览器为中心）

- [WinAppDriver](https://github.com/Microsoft/WinAppDriver) - Microsoft 用于 Windows 应用程序自动化的 WebDriver 实现。
- [Winium](https://github.com/2gis/Winium) - Windows 平台的自动化框架。它是免费的。它是开源的。它是基于硒的。支持：Windows 桌面（WPF、WinForms）；适用于 Windows Phone 的 Windows 应用商店或通用应用程序； Windows Phone Silverlight 应用程序。
- [QtWebDriver](https://github.com/cisco-open-source/qtwebdriver) - 用于使用 WebDriver 自动化基于 Qt 的 GUI 应用程序。
- [AutoItDriverServer](https://github.com/daluu/AutoItDriverServer) - Selenium 服务器通过（远程）WebDriver API 控制/驱动 AutoIt。
- [AutoPyDriverServer](https://github.com/daluu/AutoPyDriverServer) - Selenium 服务器通过（远程）WebDriver API 控制/驱动 AutoPy。
- [Appium for Mac]([https://appium.io/docs/en/drivers/mac/](https://github.com/appium/appium-mac2-driver)) - 用于自动化 Mac OS X 桌面的 Appium/WebDriver 实现。
- [SilkAppDriver](https://github.com/MicroFocus/SilkAppDriver) - Selenium 服务器通过（远程）WebDriver API 控制/驱动商业 SilkTest 平台。

### 桌面工具

- [SWET](https://github.com/sergueik/SWET) - SWD 页面记录器的后继者，具有相同的功能。
- [Looking Glass](https://github.com/dmolchanenko/LookingGlass) - 提供跨浏览器元素检查器和 Selenium 代码生成器的 Java 应用程序。
- [Silk WebDriver](https://www.microfocus.com/products/silk-portfolio/silk-webdriver/) - SilkTest 创建者提供的用于记录、回放和脚本导出的 Selenium IDE 替代方案。
- [Fire IE Selenium](https://code.google.com/archive/p/fire-ie-selenium/) - 基于 Microsoft Excel 的工具，为 Internet Explorer 浏览器提供元素检查。

### 硒网格

- [Selenium Grid Extras](https://github.com/groupon/Selenium-Grid-Extras) - 一个框架，提供除基本 Selenium Grid 之外的附加功能，如视频录制。
- [SeLion](https://github.com/paypal/SeLion) - 一个（Java）框架，用于运行 Selenium 测试，具有超出基本 Selenium Grid 功能的附加功能，特别是稳定性改进等。
- [Selenium Grid Extensions](https://github.com/sterodium/selenium-grid-extensions) - 一组 Selenium Grid 扩展，提供附加功能，例如远程运行 Sikuli 测试/自动化、在网格节点上上传/下载文件。

### 云服务

- [Sauce Labs](https://saucelabs.com) - 跨浏览器测试非常棒。在 300 多个操作系统/浏览器平台上进行 Selenium 测试、移动测试、JS 单元测试。免费开始使用。
- [HeadSpin](https://www.headspin.io/) - 在运行真实浏览器的数千台真实设备上测试您的网站的跨浏览器兼容性。即时访问云上的多个桌面和移动浏览器。获取免费试用。
- [Browserstack](https://www.browserstack.com/) - 在真实浏览器上测试您的网站的跨浏览器兼容性。即时访问多个桌面和移动浏览器。获取免费试用。
- [TestGrid](https://www.testgrid.io/) - 在 1000 多个真实浏览器和操作系统上对移动应用程序和网站进行端到端测试。请求免费试用。
- [LambdaTest](https://www.lambdatest.com/selenium-automation) - 测试您的网站在 2000 多个真实浏览器和操作系统上的跨浏览器兼容性。获取免费试用。
- [TestingBot](https://testingbot.com) - TestBot 在云中使用 Selenium 提供简单的跨浏览器测试。
- [Moon Cloud](https://aerokube.com/moon-cloud/) - 公共云平台中的专用 Selenium 集群按分钟计费且浏览器数量不受限制。
- [Mail7](https://www.mail7.io/) - 用于自动化电子邮件工作流程测试的一次性电子邮件服务，[本文档](https://docs.mail7.io/tutorials/registration-and-login-automation-using-selenium-with-disposable-email)解释了如何使用 Selenium 实现 Mail7
- [Thundra Foresight](https://www.thundra.io/foresight) - 通过立即发现测试失败来了解测试套件的可见性工具。
- [Hyperbrowser](https://hyperbrowser.ai/) - 浏览器基础设施和自动化，用于使用无头 Chrome 运行和扩展 Selenium 自动化，并具有代理、验证码解决和会话记录等高级功能。

### 设备农场

- [OpenSTF](https://github.com/DeviceFarmer/stf) - 用于运行您自己的设备场的框架，适用于 Android，也适用于 iOS。

### 网页抓取/挖掘

- [Scrapy](http://scrapy.org) - **Python**，主要是一个 scraper/miner - 快速，有据可查，并且可以与 [Django Dynamic Scraper](http://django-dynamic-scraper.readthedocs.org/en/latest/) 链接以进行良好的挖掘部署，或与 [Scrapy Cloud](http://scrapinghub.com/scrapy-cloud.html) 链接以进行 PaaS（无服务器）部署，在终端或服务器独立进程中工作，可以与 **Celery** 一起使用，建立在 **Twisted** 之上。
- [Node-Crawler](https://github.com/sylvinus/node-crawler) - **Node.js** 用于 NodeJS + 服务器端 jQuery 的 Web Crawler/Spider。

### 规格

- [The WebDriver Wire Protocol](https://www.selenium.dev/documentation/legacy/json_wire_protocol/) - 与浏览器或 RemoteWebDriver 服务器通信的所有 WebDriver 实现都应使用通用有线协议。
- [WebDriver](http://www.w3.org/TR/webdriver/) - 该规范定义了 WebDriver API，这是一个与平台和语言无关的接口以及相关的有线协议，允许程序或脚本内省并控制 Web 浏览器的行为。

### 博客

- [Official Selenium Blog](https://www.selenium.dev/blog/) - SeleniumHQ 的官方博客。
- [Elemental Selenium](http://elementalselenium.com/) - 每周一次的免费电子邮件，介绍如何像专业人士一样使用 Selenium。
- [SauceLabs Blog](https://saucelabs.com/blog) - 由 SauceLabs 策划的博客。

## 许可证

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](http://creativecommons.org/publicdomain/zero/1.0/)

在法律允许的范围内，[Christian Bromann](http://www.christian-bromann.com/) 已放弃本作品的所有版权以及相关或邻接权。
