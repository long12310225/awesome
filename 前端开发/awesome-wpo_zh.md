# 很棒的 WPO [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[![GitHub contributors](https://img.shields.io/github/contributors/davidsonfellipe/awesome-wpo.svg)](https://github.com/davidsonfellipe/awesome-wpo/graphs/contributors)
[![MIT license](https://img.shields.io/github/license/mashape/apistatus.svg?style=flat)](https://davidsonfellipe.mit-license.org/)

欢迎来到 Web 性能优化资源精选列表。该存储库旨在收集与优化网站性能相关的最佳工具、文章、博客、书籍和讲座。无论您是开发人员、设计师还是性能爱好者，您都可以在这里找到有价值的内容来增强您的 Web 项目。

> :globe_with_meridians: **在线浏览：** 此列表也可通过网站 **[awesome-wpo.dev](https://awesome-wpo.dev/)** 获取。

## 类别

:globe_with_meridians: [很棒的 WPO / 网站](https://awesome-wpo.dev/)

:memo: [很棒的 WPO / 文章](#articles)

：书籍：[很棒的 WPO / 书籍](#books)

:book: [很棒的 WPO / 文档](#documentation)

:calendar: [很棒的 WPO / 活动](#events)

:movie_camera: [很棒的 WPO / 演讲](#talks)

## 目录

以下是此集合中涵盖的类别的快速概述：

- [代理技巧](#agent-skills)
- [Analyzers](README.md#analyzers)
- [分析器API](README.md#analyzers---api)
- [应用程序性能监控](#application-performance-monitoring)
- [捆绑分析仪](#bundle-analyzer)
- [Benchmarks](#benchmarks)
- [Bookmarklets](#bookmarklets)
- [CDN](#cdn)
- [核心网络生命力](#core-web-vitals)
- [Extensions](#extensions)
- [图像优化器](#image-optimizers)
- [Generators](#generators)
- [Lazyloaders](#lazyloaders)
- [Loaders](#loaders)
- [指标监控器](#metrics-monitor)
- [Minifiers](#minifiers)
- [Miscellaneous](#miscellaneous)
- [真实用户监控](#real-user-monitoring)
- [SVG](#svg)
- [网络组件](#web-components)
- [Web 服务器基准测试](#web-server-benchmarks)
- [网络服务器模块](#web-server-modules)
- [Specs](#specs)
- [Stats](#stats)
- [其他很棒的清单](#other-awesome-lists)
- [Contributing](#contributing)

## 代理技巧

> 网络质量审核和优化工作流程的代理技能。

- [web-quality-audit](https://github.com/addyosmani/web-quality-skills#web-quality-audit) - 所有类别的全面质量审查。
- [core-web-vitals](https://github.com/addyosmani/web-quality-skills#core-web-vitals) - LCP、INP 和 CLS 特定优化。
- [accessibility](https://github.com/addyosmani/web-quality-skills#accessibility) - WCAG 合规性、屏幕阅读器支持和键盘导航。
- [performance](https://github.com/addyosmani/web-quality-skills#performance) - 加载速度、运行效率和资源优化。
- [best-practices](https://github.com/addyosmani/web-quality-skills#best-practices) - 安全性、现代 API 和代码质量模式。

## 文章

> 浏览 [awesome-wpo.dev](https://awesome-wpo.dev/) 或查看 [ARTICLES.md](ARTICLES.md)。

## 书籍

> 关于 WPO 的最佳书籍

- [HTTP/2 in Action by Barry Pollard](https://www.manning.com/books/http2-in-action) - 巴里·波拉德.
- [Web Performance in Action by Jeremy Wagner](https://www.manning.com/books/web-performance-in-action) - 杰里米·L·瓦格纳。
- [Book of Speed](https://www.bookofspeed.com/) - 斯托扬·斯特凡诺夫。
- [Designing for Performance: Weighing Aesthetics and Speed](https://designingforperformance.com/) - 拉拉·霍根。
- [Even Faster Web Sites: Performance Best Practices for Web Developers](https://www.oreilly.com/library/view/even-faster-web/9780596803773/) - 史蒂夫·苏德斯。
- [High Performance Browser Networking: What every web developer should know about networking and web performance](https://www.oreilly.com/library/view/high-performance-browser/9781449344757/) - 伊利亚·格里戈里克。
- [High Performance JavaScript](https://www.oreilly.com/library/view/high-performance-javascript/9781449382308/) - 尼古拉斯·扎卡斯 (Nicholas C. Zakas)
- [High Performance Web Sites: Essential Knowledge for frontend Engineers](https://www.oreilly.com/library/view/high-performance-web/9780596529307/) - 史蒂夫·苏德斯。
- [High Performance Responsive Design: Building Faster Sites Across Devices](https://www.oreilly.com/library/view/high-performance-responsive/9781491949979/) - 汤姆·巴克.
- [Lean sites](https://www.sitepoint.com/premium/books/lean-websites/) - 芭芭拉·贝尔梅斯.
- [Time Is Money: The Business Value of Web Performance](https://www.oreilly.com/library/view/time-is-money/9781491928783/) - 塔米·埃弗茨。
- [Using WebPagetest](https://www.oreilly.com/library/view/using-webpagetest/9781491902783/) - 里克·维斯科米、安迪·戴维斯、马塞尔·杜兰。
- [Web Performance Daybook Volume 2](https://www.amazon.com/Web-Performance-Daybook-Stoyan-Stefanov-ebook/dp/B008CQA8BA/) - 斯托扬·斯特凡诺夫。
- [Web Performance Tuning](https://www.oreilly.com/library/view/web-performance-tuning/059600172X/) - 帕特里克·基勒利亚.
- [You Don't Know JS: Async & Performance](https://www.oreilly.com/library/view/you-dont-know/9781491905197/) - 凯尔·辛普森。
- [Linux, Apache, MySQL, PHP Performance end-to-end](https://play.google.com/store/books/details/Colin_McKinnon_Linux_Apache_MySQL_PHP_Performance?id=Z3ciBgAAQBAJ) - 科林·麦金农。
- [Web Components in Action](https://www.manning.com/books/web-components-in-action) - 本·法雷尔.
- [Image Optimization](https://www.smashingmagazine.com/printed-books/image-optimization/) - 阿迪·奥斯马尼.
- [Performance Engineering in Practice](https://www.manning.com/books/performance-engineering-in-practice) - 丹·奥德尔.
- [Web Performance Engineering in the Age of AI](https://www.oreilly.com/library/view/web-performance-engineering/9798341660182/) - 阿迪·奥斯马尼.

## 案例研究

- [WPOStats](https://wpostats.com/) - 案例研究和实验展示了 Web 性能优化 (WPO) 对用户体验和业务指标的影响。
- [Google Developers Case Studies](https://web.dev/case-studies) - 了解其他开发人员为何以及如何使用网络为其用户创造令人惊叹的网络体验。

## 文档

- [PageSpeed Insights Rules](https://developers.google.com/speed/docs/insights/v5/get-started) - 由 PageSpeed 团队创建的指南。
已弃用。该版本已弃用，并将于 2019 年 5 月关闭。版本 5 是最新版本，提供来自 Chrome 用户体验报告的真实数据和来自 Lighthouse 的实验室数据。
- [Best Practices for Speeding Up Your site](https://developer.yahoo.com/performance/rules.html) - 该列表包括 35 个最佳实践，分为 7 个类别，由 Yahoo! 创建。卓越的绩效团队。
- [Chrome Developers: Performance](https://developer.chrome.com/docs/performance/) - 有关渲染、加载和运行时性能的深入指南。
- [Lighthouse Docs](https://developer.chrome.com/docs/lighthouse/) - 审核方法、评分详细信息和使用指南。
- [Code Splitting (Webpack)](https://webpack.js.org/guides/code-splitting/) - 分割 JavaScript 包以加快初始加载和按需加载的官方指南。
- [Navigation Timing API (MDN)](https://developer.mozilla.org/en-US/docs/Web/API/Navigation_timing_API) - 页面导航和加载里程碑指标。
- [Navigation Timing Level 2 (W3C)](https://www.w3.org/TR/navigation-timing-2/) - 使用“responseStart”和“requestStart”导出第一个字节的时间 (TTFB)。
- [Resource Timing API (MDN)](https://developer.mozilla.org/en-US/docs/Web/API/Resource_Timing_API) - 资产的详细网络时序。
- [Long Tasks API (MDN)](https://developer.mozilla.org/en-US/docs/Web/API/Long_Tasks_API) - 检测主线程阻塞工作。
- [Paint Timing API (MDN)](https://developer.mozilla.org/en-US/docs/Web/API/Paint_Timing_API) - 第一个油漆和第一个内容丰富的油漆信号。
- [Largest Contentful Paint API (MDN)](https://developer.mozilla.org/en-US/docs/Web/API/LargestContentfulPaint) - 对 LCP 条目的编程访问。
- [Layout Instability API (MDN)](https://developer.mozilla.org/en-US/docs/Web/API/LayoutShift) - 测量和检查布局偏移 (CLS)。

## 活动

> 因为社区很重要！

### 会议

- [We Love Speed](https://www.welovespeed.com/2024/) - 源于尽可能广泛地分享网络性能知识和经验的愿望。
- [PWA Summit](https://pwasummit.org/) - 一个免费的在线单轨会议，专注于帮助每个人通过渐进式 Web 应用程序取得成功。
- [performance.now()](https://perfnow.nl/) - Performance.now() 会议将返回阿姆斯特丹！我们是一个由 14 位世界级演讲者组成的单轨会议，涵盖当今最重要的网络性能见解。
- [PerfMatters](https://perfmattersconf.com/) - Conference是由国际知名性能开发者举办的在线网络性能会议。

### 聚会

> 浏览 [awesome-wpo.dev](https://awesome-wpo.dev/) 或查看 [MEETUPS.md](MEETUPS.md)。

## 会谈

> 浏览 [awesome-wpo.dev](https://awesome-wpo.dev/) 或查看 [TALKS.md](TALKS.md)。

## 工具

- [Speculation Rules Generator](https://www.corewebvitals.io/tools/speculation-rules-generator) - 为预取和预渲染配置构建推测规则 JSON。
- [Critical CSS Generator](https://www.corewebvitals.io/tools/critical-css-generator) - 生成用于首屏渲染的关键路径 CSS。
- [Core Web Vitals Report](https://www.corewebvitals.io/core-web-vitals-report) - 使用 CrUX 历史数据生成 Core Web Vitals 报告。

## 分析仪

- [Request Map](https://requestmap.webperf.tools/) - 将第一方和第三方请求依赖关系可视化为交互式地图。
- [Web.dev](https://web.dev/) - 借助 web.dev 的有用指导和分析，在您自己的网站和应用程序上获取网络的现代功能。
- [PageSpeed Insights](https://pagespeed.web.dev/) - 适用于任何 URL 的实验室和现场 CWV 诊断。
- [PageGym](https://pagegym.com) - 适合经验丰富的用户和技术 SEO 专业人员的高级页面速度分析和优化工具。
- [DebugBear](https://www.debugbear.com/) - 基于Lighthouse的站点监控。查看您的分数和指标如何随时间变化，重点了解导致每次变化的原因。付费产品可免费试用 30 天。
- [Page Speed](https://developers.google.com/speed) - PageSpeed 系列工具旨在帮助您优化网站的性能。 PageSpeed Insights 产品将帮助您确定可应用于您网站的性能最佳实践，而 PageSpeed 优化工具可以帮助您自动化该过程。
- [Dareboost](https://www.dareboost.com/) - [多重审核] 跨性能、可访问性、SEO 和安全最佳实践的网站质量测试。
- [Screpy](https://screpy.com) - [多重审核] 基于人工智能的性能、SEO、正常运行时间和质量监控。
- [YSlow](https://github.com/marcelduran/yslow) - 分析网页并根据一组高性能网页规则提出提高其性能的方法。
- [Grunt-WebPageTest](https://github.com/sideroad/grunt-wpt) - 用于连续测量 WebPageTest 的 Grunt 插件。 ([演示](http://sideroad.github.io/sample-wpt-page/))
- [Grunt-perfbudget](https://github.com/tkadlec/grunt-perfbudget) - 用于执行性能预算的 Grunt.js 任务（[有关性能预算的更多信息](https://timkadlec.com/2013/01/setting-a-performance-budget/)）。
- [Web Tracing Framework](https://github.com/google/tracing-framework) - 用于跟踪和调查复杂 Web 应用程序的库、工具和可视化工具。
- [Yandex.Tank](https://github.com/yandex/yandex-tank) - 面向高级 Linux 用户的可扩展开源负载测试工具，作为自动化负载测试套件的一部分特别有用。
- [Yellow Lab Tools](https://yellowlab.tools/) - 在线快速简单的工具，可审核前端不良实践、揭示性能问题并分析 JavaScript。
- [Pagelocity](https://pagelocity.com/) - 一款Web性能优化和分析工具。
- [Speed Racer](https://github.com/speedracer/speedracer) - 使用 Chrome headless 收集您的库/应用程序的性能指标。
- [Lightest App](https://lightest.app/) - 网页加载时间对于转化和收入极其重要。可视化与竞争对手相比的网络性能。
- [Redirect Checker](https://github.com/brancogao/redirect-checker) - 分析 HTTP 重定向链、检测循环并测量对页面加载时间的性能影响。
- [Third Party Analysis Tool](https://tools.paulcalvano.com/wpt-third-party-analysis/) - 分析 WebPageTest 运行中的第三方请求风险、渲染阻塞影响以及潜在的单点故障。
- [Web Font Analyzer](https://tools.paulcalvano.com/wpt-font-analysis/) - 使用 WebPageTest 数据检查字体加载时间、有效负载和字形使用情况。
- [Webfont Usage Analyzer](https://github.com/paulcalvano/webfont-usage-analyzer) - Bookmarklet 脚本可将加载的 Web 字体映射到可见 DOM 使用情况并帮助发现字体优化机会。
- [Waterfall Tools](https://waterfall-tools.com/) - 用于 HAR、WPT JSON、Chrome 跟踪/网络日志和 tcpdump 捕获的高级客户端网络请求瀑布查看器。

## 分析器 - API

- [PSI](https://github.com/GoogleChromeLabs/psi) - Node.js 的 PageSpeed Insights - 带有报告。

## 应用程序性能监控

- [Datadog APM](https://www.datadoghq.com/product/apm/) - 大规模的端到端分布式跟踪和 APM，与所有遥测相关。
- [BetterUptime](https://betteruptime.com) - 一个很好的网站监控工具（捆绑状态页面、事件通知）。
- [Pingdom](https://www.pingdom.com/) - 一种获取网站正常运行时间的工具（使用来自不同位置的探测器）。
- [UptimeRobot](https://uptimerobot.com) - 另一个正常运行时间监控工具（具有慷慨的免费计划）。
- [StatusList](https://statuslist.app) - 正常运行时间、带有调试详细信息的性能监控以及在一个简单的仪表板中托管的状态页面。

## 真实用户监控

- [Catchpoint Real User Monitoring](https://www.catchpoint.com/real-user-monitoring) - 适用于 Web 和本机移动应用程序的 RUM，具有核心 Web Vitals、第三方影响以及与综合监控的相关性（基于 OpenTelemetry）。
- [Atatus](https://www.atatus.com/) - 全栈可观察性，包括 RUM、APM、综合正常运行时间、会话重播和 OpenTelemetry。
- [Datadog Real User Monitoring](https://www.datadoghq.com/product/real-user-monitoring/) - 具有会话重播、核心 Web Vitals 以及与跟踪和日志关联的浏览器和移动 RUM。
- [New Relic Browser Monitoring](https://newrelic.com/platform/browser-monitoring) - 使用 Core Web Vitals 进行真实用户浏览器监控、后端分布式跟踪以及部署标记。
- [SpeedCurve](https://www.speedcurve.com/features/performance-monitoring/) - Web 性能监控结合了综合测试、RUM、Lighthouse、Core Web Vitals、性​​能预算和竞争基准测试。
- [Boomerang (Open Source)](https://akamai.github.io/boomerang/oss/) - Boomerang 开源版本的文档，由 Akamai 员工在 OSS 社区的贡献下维护。
- [Akamai mPulse Boomerang](https://techdocs.akamai.com/mpulse-boomerang/docs/welcome-to-mpulse-boomerang) - Boomerang 的 Akamai mPulse 版本的文档，其中包括特定于与 mPulse 交互的附加内容。

## 捆绑分析仪

- [Bundlesize](https://github.com/siddharthkp/bundlesize) - 控制好你的捆绑包大小。
- [source-map-explorer](https://github.com/danvk/source-map-explorer) - 通过源映射分析和调试包空间使用情况。
- [Bundlephobia](https://bundlephobia.com/) - 帮助您了解将 npm 包添加到前端包对性能的影响。
- [Webpack bundle analyzer](https://github.com/webpack/webpack-bundle-analyzer) - Webpack 插件和 CLI 实用程序将包内容表示为方便的交互式可缩放树形图。
- [Disc](http://hughsk.io/disc/) - 可视化 browserify 项目包的模块树并追踪膨胀情况。
- [Lasso-analyzer](https://github.com/pajaydev/lasso-analyzer) - 分析和可视化 Lasso 创建的项目包。
- [Compression Webpack plugin](https://github.com/webpack/compression-webpack-plugin) - 准备资产的压缩版本以通过内容编码为其提供服务。
- [BundleStats](https://github.com/relative-ci/bundle-stats) - 生成捆绑包报告（捆绑包大小、资产、模块、包）并比较不同构建之间的结果。

## 基准测试

> 一组用于创建测试用例并比较 CSS、JavaScript 和 PHP 中不同实现的工具。

- [CSS-perf](https://github.com/mdo/css-perf) - 测试 CSS 性能的完全不科学的方法。大多数这些测试将围绕确定有效 CSS 架构的方法和技术。换句话说，我想知道在特定的 CSS 策略比较中哪种方法最有效。
- [JSBench](https://jsbench.me/) - 一个基于浏览器的现代 JavaScript 基准测试工具，用于快速创建和共享性能测试。
- [Benchmark.js](https://benchmarkjs.com/) - 一个强大的基准测试库，几乎适用于所有 JavaScript 平台，支持高分辨率计时器，并返回具有统计意义的结果。
- [JSlitmus](https://github.com/broofa/jslitmus) - 用于创建临时 JavaScript 基准测试的轻量级工具。
- [Matcha](https://github.com/logicalparadox/matcha) - 允许您设计测量代码性能的实验。每个工作台都应关注应用程序中的特定影响点。
- [Timing.js](https://github.com/addyosmani/timing.js) - 用于使用导航计时 API 来确定应用程序将时间花在哪里的小助手。可用作独立脚本、DevTools 代码片段或小书签。
- [Stats.js](https://github.com/mrdoob/stats.js) - 此类提供了一个简单的信息框，可帮助您监控代码性能。
- [PerfTests](https://github.com/kogarashisan/PerfTests) - JavaScript 继承模型的性能测试。
- [Memory-stats.js](https://github.com/paulirish/memory-stats.js) - 通过性能内存最小监控 JS 堆大小。
- [JSPerf](https://github.com/jsperf/jsperf.com) - 创建并共享通过基准测试比较 JavaScript 代码片段性能的测试用例。 `请关注此问题以获取更新：https://github.com/jsperf/jsperf.com/issues/537`。
- [PHPench](https://github.com/mre/PHPench) - PHP 基准测试的图形输出：使用 GnuPlot 实时绘制任何函数的运行时间并导出结果的图像。
- [php-bench](https://github.com/jacobbednarz/php-bench) - 对 PHP 代码块进行基准测试和分析，同时测量性能足迹。

## 小书签

- [Yahoo YSlow for Mobile/Bookmarklet](https://developer.yahoo.com/yslow/) - YSlow 分析网页并根据一组高性能网页规则提出提高其性能的方法。
- [PerfMap](https://github.com/zeman/perfmap) - 一个书签，用于使用资源计时 API 创建浏览器中加载的资源的前端性能热图。
- [DOM Monster](https://github.com/madrobby/dom-monster) - 一个跨平台、跨浏览器的书签，它将分析您所在页面的 DOM 和其他功能，并为您提供其运行状况。
- [CSS Stress](https://andy.edinborough.org/CSS-Stress-Testing-and-Performance-Profiling) - CSS 的压力测试和性能分析。
- [Performance-Bookmarklet](https://github.com/micmro/performance-bookmarklet) - 通过资源计时 API、导航计时 API 和用户计时分析当前页面 - 类似于轻量级实时 WebPageTest。作为 [Firefox 插件](https://addons.mozilla.org/en-US/firefox/addon/performance-analysisr/?src=cb-dl-created)，名称为 Performance-Analyser。

## CDN

> 内容交付网络或内容分发网络 (CDN) 是部署在互联网上多个数据中心的大型分布式服务器系统。 CDN 的目标是以高可用性和高性能向最终用户提供内容。请参阅 [Wikipedia](http://en.wikipedia.org/wiki/Content_delivery_network#Notable_content_delivery_service_providers) 中的大量 CDN 列表。

- [Cloudflare CDN](https://www.cloudflare.com/application-services/products/cdn/) - 使用下一代技术提供快速、可靠的 CDN 服务的内容交付网络。
- [PageCDN](https://pagecdn.com/lib) - 最先进的开源 CDN，使用 brotli-11 压缩、HTTP/2 服务器推送、更好的 HTTP/2 多路复用等进行积极的内容优化。已支持 100 个库和 2000 多个 WordPress 主题。易于使用，易于链接，而且速度非常快。
- [jsDelivr](https://github.com/jsdelivr/jsdelivr) - 与 Google 托管库类似，jsDelivr 是一个开源 CDN，允许开发人员托管自己的项目，并允许任何人链接到他们网站上的我们托管的文件。
- [Google Hosted Libraries](https://developers.google.com/speed/libraries/) - Google 为最流行的开源 JavaScript 库运行的 CDN。
- [CDNjs](https://cdnjs.com/) - 由 Cloudflare 赞助的 JavaScript 和 CSS 开源 CDN，托管从 jQuery 和 Modernizr 到 Bootstrap 的所有内容。
- [Amazon CloudFront](https://aws.amazon.com/cloudfront/) - 亚马逊的内容交付网络，可以与其他亚马逊服务很好地集成，也可以单独使用。
- [jQuery](https://releases.jquery.com/) - 由 MaxCDN 提供支持的最新稳定版本的官方 CDN。
- :cn: [UpYun CDN](http://jscdn.upai.com/) - 由upyun提供的CDN。
- :cn: [Bootstrap 中文网开放 CDN 服务](http://www.bootcdn.cn/) - Bootstrap Chinese net open CDN service (only HTTP).
- :ru: [Yandex CDN](https://yandex.ru/dev/jslibs/) - Yandex 内容交付网络托管流行的第三方 JavaScript 和 CSS 库（最适合在俄罗斯使用）。
- [CDNperf](https://www.cdnperf.com/) - 为您找到快速、可靠的 JavaScript CDN，让您的网站变得活泼、愉快。
- [Gulp-google-cdn](https://github.com/sindresorhus/gulp-google-cdn) - 将脚本引用替换为 Google CDN 脚本引用。

> 要查找更多有用信息以帮助您在付费 CDN 之间做出正确选择，请访问 [CDNPlanet](http://www.cdnplanet.com/)。

## 核心网络生命力

- [web-vitals](https://github.com/GoogleChrome/web-vitals) - 用于在浏览器中准确测量核心 Web 生命体（LCP、FID、CLS、INP、TTFB）的小型库。
- [Lighthouse](https://github.com/GoogleChrome/lighthouse) - 在实验室条件下审核核心 Web Vitals（请参阅 [Analyzers](#analyzers)）。
- [Lighthouse CI](https://github.com/GoogleChrome/lighthouse-ci) - 在 CI 中运行 Lighthouse，以在每次提交时强制执行 Core Web Vitals 预算。

## 扩展

- [Browser Calories](https://github.com/zenorocha/browser-calories) - 衡量绩效预算的最简单方法。

## 发电机

- [AtBuild](https://github.com/jarred-sumner/atbuild) - JavaScript 代码生成工具，可让您编写输出 JavaScript 的 JavaScript。非常适合展开循环和编写编译运行时的库。
- [Glue](https://github.com/jorgebastida/glue) - 一个简单的命令行工具，用于生成 CSS 精灵。
- [Pitomba-spriter](https://github.com/pitomba/spriter) - Spriter 是一个简单而灵活的 CSS 动态精灵生成器，使用 Python。它可以同步和异步处理 CSS，因为它提供了在 Python 代码中使用的类，并且还提供了一个监听器，可以侦听文件系统并在静态更改后立即更改 CSS 和 sprite。
- [Grunt-spritesmith](https://github.com/twolfson/grunt-spritesmith) - 用于将一组图像转换为精灵表和相应 CSS 变量的 Grunt 任务。
- [Grunt-sprite-css-replace](https://www.npmjs.com/package/grunt-sprite-css-replace) - Grunt 任务，从样式表中引用的图像生成精灵，然后使用新的精灵图像和位置更新引用。
- [Grunt-svg-sprite](https://www.npmjs.com/package/grunt-svg-sprite) - SVG sprites & stacks galore - 围绕 svg-sprite 的 Grunt 插件读取一堆 SVG 文件，优化它们并创建各种风格的 SVG sprites 和 CSS 资源。
- [Gulp-sprite](https://github.com/aslansky/gulp-sprite) - Gulp 任务，用于创建图像精灵和 Gulp 相应的样式表。
- [Gulp-svg-sprites](https://github.com/shakyShane/gulp-svg-sprites) - 用于创建 SVG 精灵的 Gulp 任务。
- [SvgToCSS](https://github.com/kajyr/SvgToCSS) - 优化并渲染 CSS / Sass 精灵中的 SVG 文件。
- [Assetgraph-sprite](https://github.com/assetgraph/assetgraph-sprite) - 基于 CSS 依赖图自动生成精灵的 Assetgraph 转换。
- [Sprite Cow](http://www.spritecow.com/) - 以可复制 CSS 的形式获取 spritesheet 中 sprite 的背景位置、宽度和高度。
- [CSS Sprite Generator](https://css.spritegen.com/) - CSS 精灵允许您将多个图像合并到一个文件中。
- [Sprity](https://github.com/sprity/sprity) - 具有很多功能的模块化图像精灵生成器：支持视网膜精灵，支持不同的输出格式，从图像目录生成精灵和适当的样式文件等......
- [Sprite Factory](https://github.com/jakesgordon/sprite-factory) - sprite 工厂是一个 ruby 库，可用于生成 CSS 精灵。它将目录中的各个图像文件组合成单个统一的 sprite 图像，并创建适当的 CSS 样式表以在您的 Web 应用程序中使用。

## 图像优化器

> 如何删除所有这些不必要的数据并在不降低质量的情况下为您提供文件。

- [Shortpixel](https://shortpixel.com/online-image-compression) - 通过删除图像中不必要的字节来压缩图像并将其转换为 WebP/AVIF。
- [Grunt-smushit](https://github.com/heldr/grunt-smushit) - Grunt 插件使用 Yahoo Smushit 删除不必要的 PNG 和 JPG 字节。
- [Gulp-smushit](https://github.com/heldr/gulp-smushit) - Gulp 插件使用 Yahoo Smushit 优化 PNG 和 JPG。在smosh上面做的。
- [Smush it](https://www.imgopt.com/) - 使用特定于格式的优化从图像文件中删除不必要的字节。无损：优化图像而不改变其外观或视觉质量。
- [Imagemin](https://github.com/imagemin/imagemin) - 使用 Node.js 无缝缩小图像。
- [Sharp](https://github.com/lovell/sharp) - 此高速 Node.js 模块的典型用例是将多种格式的大图像转换为较小的、适合 Web 的不同尺寸的 JPEG、PNG 和 WebP 图像。
- [Gm](https://github.com/aheckmann/gm) - 适用于 Node.js 的 GraphicsMagick 和 ImageMagick。
- [ExifCleaner](https://exifcleaner.com) - GUI 应用程序可通过拖放从图像和视频文件中删除 EXIF 元数据。免费且开源。
- [OptiPNG](https://optipng.sourceforge.net/) - PNG 优化器可将图像文件重新压缩为较小的尺寸，而不会丢失信息。
- [Grunt-contrib-imagemin](https://github.com/gruntjs/grunt-contrib-imagemin) - 为 Grunt 缩小 PNG 和 JPEG 图像。
- [Gulp-imagemin](https://github.com/sindresorhus/gulp-imagemin) - 使用 Gulp 的 imagemin 缩小 PNG、JPEG、GIF 和 SVG 图像。
- [Grunt-WebP](https://github.com/somerandomdude/grunt-webp) - 将您的图像转换为 WebP 格式。
- [Gulp-WebP](https://github.com/sindresorhus/gulp-webp) - 将图像转换为 Gulp 的 WebP。
- [Imageoptim](https://imageoptim.com/mac) - 免费应用程序，使图像占用更少的磁盘空间并加载更快，而不牺牲质量。它优化压缩参数，并删除垃圾元数据和不必要的颜色配置文件。
- [Imager](http://github.com/imager-io/imager) - 自动图像压缩可在网络上高效分发图像。
- [Grunt-imageoptim](https://github.com/JamieMason/grunt-imageoptim) - 让 ImageOptim、ImageAlpha 和 JPEGmini 成为您自动化构建过程的一部分。
- [ImageOptim-CLI](https://github.com/JamieMason/ImageOptim-CLI) - 自动化 Mac 版 ImageOptim、ImageAlpha 和 JPEGmini，使图像批量优化成为自动化构建过程的一部分。
- [Tapnesh-CLI](https://github.com/JafarAkhondali/Tapnesh) - Tapnesh 是一个 CLI 工具，可以轻松高效地并行优化所有图像！
- [Tinypng](https://tinypng.com/) - 对 PNG 图像进行高级有损压缩，保留完整的 Alpha 透明度。
- [Kraken Web-interface](https://kraken.io/web-interface) - 优化您的图像，可供下载 12 小时。
- [Compressor](https://compressor.io/) - JPG、PNG、SVG 和 GIF 的在线图像压缩器。
- [mozjpeg](https://github.com/mozilla/mozjpeg) - 改进的 JPEG 编码器。
- [Jpegoptim](https://github.com/tjko/jpegoptim) - 用于优化/压缩 JPEG 文件的实用程序。
- [AdvPNG](http://www.advancemame.it/doc-advpng.html) - 重新压缩 PNG 文件以获得尽可能小的大小。
- [Leanify](https://github.com/JayXon/Leanify) - 轻量级无损文件压缩器/优化器。
- [Trimage](https://trimage.org/) - 用于无损优化 PNG 和 JPG 文件的跨平台工具。
- [ImageEngine](https://imageengine.io) - 用于动态优化、调整大小和缓存图像的云服务，具有出色的移动支持。
- [ImageKit.io](https://imagekit.io) - 通过全球交付网络和存储进行智能实时图像优化、图像转换。
- [Optimizt](https://github.com/343dev/optimizt) - CLI 图像优化工具。它可以有损和无损压缩 PNG、JPEG、GIF 和 SVG，还可以为光栅图像创建 AVIF 和 WebP 版本。
- [ResponsiveImage](https://responsive-image.dev/) - 使用 Vite 或 Webpack 插件生成优化的图像（WebP、AVIF）和 LQIP 占位符，并使用适用于多个框架的图像组件渲染响应式图像标记。
- [Adaptive Images](https://adaptive-images.com/) - 服务器端 PHP 工具，可检测屏幕尺寸并根据现有的“<img>”标记自动创建、缓存和提供适合设备大小的调整后的图像。

## 惰性加载器

- [lazyload](https://github.com/vvo/lazyload) - 使用独立的 JavaScript 延迟加载程序 (~1kb) 延迟图像、iframe 和小部件。
- [lozad.js](https://github.com/ApoorvSaxena/lozad.js) - 纯 JS 中的高性能、轻量约 0.9kb 且可配置的延迟加载程序，不依赖于响应式图像、iframe 等。
- [quicklink](https://github.com/GoogleChromeLabs/quicklink) - 在视口中预取链接（通过 Intersection Observer）以使将来的导航更快。

## 装载机

- [HeadJS](https://github.com/headjs/headjs) - 你头脑中唯一的脚本。用于响应式设计、特征检测和资源加载。
- [RequireJS](https://requirejs.org/) - JavaScript 文件和模块加载器。它针对浏览器内使用进行了优化，但也可以在其他 JavaScript 环境中使用，例如 Rhino 和 Node.js。
- [Labjs](https://github.com/getify/LABjs) - Getify Solutions 支持的开源（MIT 许可证）项目。 LABjs 的核心目的是成为一个通用的、按需的 JavaScript 加载器，能够随时从任何位置将任何 JavaScript 资源加载到任何页面中。
- [Defer.js](https://github.com/wessman/defer.js) - 异步一切：使用这个 JS 部分使页面的主要内容加载得更快。
- [InstantClick](https://github.com/dieulot/instantclick) - 悬停时预加载页面，因此站点内链接感觉即时。
- [prerender.js](https://github.com/genderev/prerender.js) - 在导航之前预加载页面和资源，以实现更快的页面转换。
- [JIT](https://github.com/shootaroo/jit-grunt) - Grunt 的 JIT（Just In Time）插件加载器。即使有很多插件，Grunt 的加载时间也不会减慢。
- [Guess.js](https://github.com/guess-js/guess) - 使用分析和机器学习进行预测预取和性能优化。

## 指标监控器

- [Phantomas](https://github.com/macbre/phantomas) - 基于 PhantomJS 的 Web 性能指标收集器和监控工具。
- [Bench](https://github.com/jmervine/bench) - 使用 Phantomas（PhantomJS 支持的客户端性能指标抓取器）。对页面进行基准测试，将结果存储在 MongoDB 中，并通过内置服务器显示结果。
- [Keepfast](https://github.com/keepfast/keepfast) - 用于监控与网页性能相关的指标的工具。
- [GTmetrix](https://gtmetrix.com/) - 用于测试和监控页面性能的免费工具。使用 Lighthouse 对您的页面进行评分，并提供有关如何优化页面的可行建议。
- [Pingbreak.com](https://pingbreak.com/) - 免费站点和 SSL 监控，具有响应时间警报（在 Slack、Twitter、Mattermost、Discord 或自定义 Webhook 上）。
- [Pingdom site Speed Test](https://tools.pingdom.com/) - 测试该页面的加载时间，对其进行分析并找到瓶颈。
- [Dotcom-tools](https://www.dotcom-tools.com/website-speed-test) - 在全球 20 个地点的真实浏览器中分析您的网站速度。
- [WebPageTest](https://www.catchpoint.com/webpagetest) - 使用真实的浏览器（IE 和 Chrome）以真实的消费者连接速度从全球多个位置运行免费的网站速度测试。您可以运行简单的测试或执行高级测试，包括多步骤事务、视频捕获、内容阻止等等。您的结果将提供丰富的诊断信息，包括资源加载瀑布图、页面速度优化检查和改进建议。
- [Sitespeed.io](https://www.sitespeed.io/) - 开源工具，可根据 Web 性能最佳实践检查您的网站，并使用导航计时 API 收集指标。输出 XML 和 HTML 报告。
- [Grunt-phantomas](https://github.com/stefanjudis/grunt-phantomas) - Grunt 插件包装幻象来测量前端性能。
- [Perfjankie](https://www.npmjs.com/package/perfjankie) - 运行时浏览器性能回归套件（[演示](https://github.com/asciidisco/perfjankie-test)）。
- [BrowserView Monitoring](https://www.dotcom-monitor.com/products/web-page-monitoring/) - 从世界各地的多个点持续检查 Internet Explorer、Chrome 和 Firefox 中的网页加载时间。
- [DareBoost](https://www.dareboost.com/en) - 真正的浏览器监控。使用 YSlow、Page Speed 和众多自定义提示提供有关 Web 性能和质量的完整报告。
- [Perfume.js](https://github.com/Zizzamia/perfume.js) - 用于从真实用户收集 Core Web Vitals 和其他性能指标的小型库。
- [puppeteer-webperf](https://github.com/addyosmani/puppeteer-webperf) - 在 Puppeteer 脚本中收集 Web 性能指标。
- [WebPageTest API Wrapper for Node.js](https://github.com/catchpoint/WebPageTest.api-nodejs) - WebPageTest API Wrapper 是一个 npm 包，它将 Node.js 的 WebPageTest API 包装为模块和命令行工具。
- [WebPerformance Report](https://webperformancereport.com/) - 每周在您的收件箱中发送网络性能报告。获取有关您想要监控的电子商务或网站的 Web 性能和 Web 优化状态的个性化报告，其中包括核心 Web Vitals。

## 缩小器

- [HTMLCompressor](https://code.google.com/archive/p/htmlcompressor/) - 小型、快速的 Java 库，通过删除额外的空格、注释和不需要的字符来缩小 HTML 或 XML，而不破坏结构。包括命令行构建。
- [Django-htmlmin](https://github.com/cobrateam/django-htmlmin) - 适用于 Python 的 HTML 压缩器，完全支持 HTML 5。支持 Django、Flask 和任何其他 Python Web 框架，以及用于静态站点或部署脚本的命令行工具。
- [HTMLMinifier](https://github.com/kangax/html-minifier) - 高度可配置、经过充分测试、基于 JavaScript 的 HTML 压缩器，具有类似 lint 的功能。
- [Grunt-contrib-htmlmin](https://github.com/gruntjs/grunt-contrib-htmlmin) - 一个使用 HTMLMinifier 来缩小 HTML 的 grunt 插件。
- [Gulp-htmlmin](https://github.com/jonschlinkert/gulp-htmlmin) - 一个使用 HTMLMinifier 来缩小 HTML 的 gulp 插件。
- [Grunt-htmlcompressor](https://github.com/jney/grunt-htmlcompressor) - 用于 HTML 压缩的 Grunt 插件，使用 htmlcompressor。
- [HTML_minifier](https://github.com/stereobooster/html_minifier) - kangax html 压缩器的 Ruby 包装器。
- [HTML_press](https://github.com/stereobooster/html_press) - 用于压缩 html 的 Ruby gem，可删除所有空白垃圾，只留下 HTML。
- [Koa HTML Minifier](https://github.com/koajs/html-minifier) - 使用 html-minifier 缩小 HTML 响应的中间件。它使用 html-minifier 的默认选项，默认情况下这些选项都是关闭的，因此您必须设置这些选项，否则它不会执行任何操作。
- [HTML Minifier Online](http://kangax.github.io/html-minifier/) - kangax (HTMLMinifier Creator) 的 HTML min 工具。
- [Minimize](https://github.com/Swaagie/minimize) - 基于node-htmlparser的HTML压缩器；目前仅限服务器端。客户端缩小已计划。
- [Html-minifier](https://github.com/deanhume/html-minifier) - 一个简单的 Windows 命令行工具，用于缩小 HTML、Razor 视图和 Web 表单视图。
- [UglifyJS2](https://github.com/mishoo/UglifyJS) - UglifyJS 是一个用 JavaScript 编写的 JavaScript 解析器、压缩器、压缩器或美化器工具包。
- [CSSO](https://github.com/css/csso) - CSS 最小化器与其他最小化器不同。除了通常的缩小技术之外，它还可以对 CSS 文件进行结构优化，从而与其他缩小器相比，文件大小更小。
- [Grunt-contrib-concat](https://github.com/gruntjs/grunt-contrib-concat) - 用于连接文件的 Grunt 插件。
- [Grunt-contrib-uglify](https://github.com/gruntjs/grunt-contrib-uglify) - 用于连接和缩小 JavaScript 文件的 Grunt 插件。
- [Clean-css](https://github.com/clean-css/clean-css) - 一个快速、高效且经过充分测试的 Node.js CSS 压缩器。
- [Django-compressor](https://github.com/django-compressor/django-compressor) - 将链接和内联 JavaScript 或 CSS 压缩到单个缓存文件中。
- [Django-pipeline](https://github.com/jazzband/django-pipeline) - Pipeline 是 Django 的资产打包库，提供 CSS 和 JavaScript 连接和压缩、内置 JavaScript 模板支持以及可选的 data-URI 图像和字体嵌入。
- [JShrink](https://github.com/tedious/JShrink) - PHP 类可缩小 JavaScript 以更快地交付给客户端。
- [JSCompress](http://jscompress.com/) - 最简约的在线JS压缩工具。
- [CSSshrink](https://github.com/stoyan/cssshrink) - 因为CSS是渲染页面的关键路径。一定很小！否则！
- [Grunt-cssshrink](https://github.com/JohnCashmore/grunt-cssshrink) - 这只是 CSS Shrink 的一个 grunt 包装器。
- [Gulp-cssshrink](https://github.com/torrottum/gulp-cssshrink) - 使用 Gulp 的 cssshrink 缩小 CSS 文件。
- [Prettyugly](https://github.com/stoyan/prettyugly) - Uglify（去除空格）或 prettify（添加一致的空格）CSS 代码。
- [Grunt-contrib-cssmin](https://github.com/gruntjs/grunt-contrib-cssmin) - Grunt 的 CSS 缩小器。
- [Grunt-uncss](https://github.com/uncss/grunt-uncss) - 从项目中删除未使用的 CSS 的繁重任务。
- [Gulp-uncss](https://github.com/ben-eb/gulp-uncss) - 用于从项目中删除未使用的 CSS 的 gulp 任务。

## 杂项

- [Fontaine](https://github.com/unjs/fontaine) - 基于字体规格的自动字体回退，以减少由 Web 字体加载引起的累积布局偏移 (CLS)。
- [Socialite.js](http://socialitejs.com/) - Socialite 提供了一种非常简单的方法来实施和激活大量的社交共享按钮 - 任何时候你愿意。文档加载时、文章悬停时、任何事件时。
- [uCSS](https://github.com/oyvindeh/ucss) - 抓取大型网站以查找未使用的 CSS 选择器（不会删​​除未使用的 CSS）。
- [HTTPinvoke](https://github.com/jakutis/httpinvoke) - 适用于浏览器和 Node.js 的无依赖 HTTP 客户端库，具有基于 Promise 或 Node.js 风格的基于回调的 API，用于处理事件、文本和二进制文件上传和下载、部分响应正文、请求和响应标头、状态代码。
- [Critical](https://github.com/addyosmani/critical) - HTML 页面中提取和内联关键路径 CSS (alpha)。
- [Csscolormin](https://github.com/stoyan/csscolormin) - 缩小 CSS 颜色的实用程序，例如：min("white"); // 缩小为“#fff”。
- [Lazysizes](https://github.com/aFarkas/lazysizes) - 适用于图像（响应式和普通）、iframe 和脚本的高性能延迟加载程序，无需配置即可检测通过用户交互、CSS 或 JavaScript 触发的任何可见性更改。
- [react-virtualized](https://github.com/bvaughn/react-virtualized) - React 组件通过虚拟化可见行来高效渲染大型列表和表格数据。
- [TMI](https://github.com/addyosmani/tmi) - 太多图像：在网络上发现您的图像权重。

## 静止无功发生器

- [SVGO](https://github.com/svg/svgo) - 基于 Node.js 的 SVG 矢量图形优化器。
- [SVG OMG](https://jakearchibald.github.io/svgomg/) - SVGOMG 是 SVGO 缺失的 GUI，旨在公开 SVGO 的大多数（如果不是全部）配置选项。
- [Grunt-svgmin](https://github.com/sindresorhus/grunt-svgmin) - 使用 SVGO for Grunt 缩小 SVG。
- [Gulp-svgmin](https://www.npmjs.com/package/gulp-svgmin) - 使用 SVGO for Gulp 缩小 SVG。
- [Scour](http://www.codedread.com/scour/) - 开源 Python 脚本，可积极清理 SVG 文件，去除工具或作者嵌入文档中的垃圾。
- [SVG Cleaner](https://github.com/RazrFalcon/SVGCleaner) - 使用批处理模式、许多清理选项以及多核 CPU 上的线程处理来清理 SVG 文件中不必要的数据。

## 网络组件

- [Polymer Bundler](https://github.com/Polymer/tools/tree/master/packages/bundler) - Polymer-bundler 是一个用于打包项目资产以进行生产的库，以最大程度地减少网络往返。
- [Gulp-vulcanize](https://github.com/sindresorhus/gulp-vulcanize) - 使用 Vulcanize 将一组 Web 组件连接到一个文件中。

## Web 服务器基准测试

- [HTTPerf](https://github.com/httperf/httperf) - 通过灵活生成 HTTP 工作负载和服务器指标来衡量 Web 服务器性能。
- [Apache JMeter](https://jmeter.apache.org/download_jmeter.cgi) - 开源负载测试工具：它是一个Java平台应用程序。
- [Locust](https://locust.io/) - 一个开源负载测试工具。使用 Python 代码定义用户行为，并让数百万并发用户涌入您的系统。
- [Autoperf](https://github.com/igrigorik/autoperf) - httperf 的 Ruby 驱动程序可自动对单个端点或通过日志重放进行负载和性能测试。
- [HTTPerf.rb](https://github.com/jmervine/httperfrb) - httperf 的简单 Ruby 接口，用 Ruby 编写。
- [PHP-httperf](https://github.com/jmervine/php-httperf) - HTTPerf.rb 的 PHP 端口。
- [HTTPerf.js](https://github.com/jmervine/httperfjs) - HTTPerf.rb 的 JS 端口。
- [HTTPerf.py](https://github.com/jmervine/httperfpy) - HTTPerf.rb 的 Python 端口。
- [Gohttperf](https://github.com/jmervine/gohttperf) - 转到 HTTPerf.rb 的端口。
- [wrk](https://github.com/wg/wrk) - HTTP 基准测试工具（带有可选的 Lua 脚本，用于请求生成、响应处理和自定义报告）。
- [beeswithmachineguns](https://github.com/newsapps/beeswithmachineguns) - 用于武装（创建）许多蜜蜂（微型 EC2 实例）以攻击（负载测试）目标（Web 应用程序）的实用程序。
- [k6](https://k6.io/) - 为开发人员构建的开源负载测试工具。易于集成到 CI 管道中。测试是用 ES6 JS 编写的，您可以使用 HTTP/1.1、HTTP/2 和 WebSocket 测试 API、微服务和站点。

## 网络服务器模块

- [PageSpeed Module](https://modpagespeed.com/docs/getting-started/) - PageSpeed 可加快您的网站速度并减少页面加载时间。此开源 Web 服务器模块会自动将 Web 性能最佳实践应用于页面和相关资产（CSS、JavaScript、图像），而无需您修改现有内容或工作流程。 PageSpeed 可作为 Apache 2.x 和 Nginx 1.x 的模块。
- [WebP-detect](https://github.com/igrigorik/webp-detect) - WebP 与 Accept 协商。

## 规格

- [Web Performance Working Group](https://www.w3.org/webperf/) - Web 性能工作组是富 Web 客户端活动的一部分，其任务是提供测量用户代理功能和 API 的应用程序性能方面的方法。
- [Page Visibility](https://html.spec.whatwg.org/multipage/interaction.html#page-visibility) - 该规范为站点开发人员定义了一种方法，可以通过编程方式确定页面当前的可见性状态，以便开发节能和 CPU 高效的 Web 应用程序。
- [Navigation Timing](https://w3c.github.io/navigation-timing/) - 该规范定义了一个统一的接口来存储和检索与文档导航相关的高分辨率性能指标数据。
- [Resource Timing](https://www.w3.org/TR/resource-timing/) - 该规范定义了 Web 应用程序访问文档中资源的完整计时信息的接口。
- [User Timing](https://www.w3.org/TR/user-timing/) - 该规范定义了一个接口，通过允许 Web 开发人员访问高精度时间戳来帮助他们测量应用程序的性能。
- [Performance Timeline](https://www.w3.org/TR/performance-timeline/) - 该规范定义了一个统一的接口来存储和检索性能指标数据。本规范不涵盖单独的性能指标接口。
- [CSS will-change](https://drafts.csswg.org/css-will-change/) - 该规范定义了“will-change” CSS 属性，它允许作者提前声明哪些属性将来可能会更改，以便 UA 可以在需要之前设置适当的优化。这样，当实际更改发生时，页面会快速更新。
- [Resource Hints](http://www.w3.org/TR/resource-hints/) - 该规范定义了 HTML 链接元素 (<link>) 的 dns-prefetch、preconnect、prefetch 和 prerender 关系。这些原语使开发人员以及生成或交付资源的服务器能够协助用户代理决定应连接到哪些源，以及应获取和预处理哪些资源以提高页面性能。
- [RFC 9218: HTTP Prioritization](https://www.rfc-editor.org/rfc/rfc9218.html) - HTTP 的协议级优先级机制。

## 统计数据

- [HTTP Archive](https://httparchive.org/) - 它是 Web 性能信息（例如页面大小、失败的请求和所使用的技术）的永久存储库。这些性能信息使我们能够了解 Web 构建方式的趋势，并提供用于进行 Web 性能研究的通用数据集。
- [Chrome User Experience Report (CrUX)](https://developer.chrome.com/docs/crux/) - 来自 Chrome 用户的原始级别真实用户性能数据。

## 其他很棒的清单

- [iamakulov/awesome-webpack-perf](https://github.com/iamakulov/awesome-webpack-perf) - 用于提高 Web 性能的 Webpack 工具的精选列表。
- [imteekay/web-performance-research](https://github.com/imteekay/web-performance-research) - Web 性能研究。

## 贡献

如需贡献，请检查 [contributing.md](contributing.md)，然后 [打开问题](https://github.com/davidsonfellipe/awesome-wpo/issues) 和/或 [拉取请求](https://github.com/davidsonfellipe/awesome-wpo/pulls)。
