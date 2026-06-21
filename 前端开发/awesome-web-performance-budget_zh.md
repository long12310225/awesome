# 出色的网络性能预算 [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
> Web 性能预算是对影响站点性能的某些值的一组限制，在任何 Web 项目的设计和开发中都不应超出这些值。通过设置性能预算，我们可以更加关注性能，从而提高网站的速度和整体用户体验。该列表帮助我们提供各种文章、项目、工具和技术的链接，以维持性能预算。


## 内容

- [Articles](#articles)
- [衡量绩效预算的工具](#tools-to-measure-performance-budget)
- [开源工具](#open-source-tools)
- [构建工具来设置性能预算](#build-tools-to-set-up-performance-budget)
- [捆绑分析仪](#bundle-analyzers)
- [网站分析器](#website-analyzers)
- [Blogs](#blogs)
- [Podcasts](#podcasts)
- [Videos](#videos)
- [Books](#books)
- [案例研究](#case-studies)

## 文章
- [JavaScript Start-up Performance](https://medium.com/reloading/javascript-start-up-performance-69200f43b201) - Addyosmani 的绩效预算。
- [Performance Budget](https://addyosmani.com/blog/performance-budgets/) - Addyosmani 的绩效预算。
- [Your first performance budget](https://web.dev/your-first-performance-budget/) - 解释了如何通过几个简单的步骤定义您的第一个绩效预算。
- [Designing for Performance](http://designingforperformance.com/index.html#table-of-contents) - 性能对于设计师来说有多重要。
- [Web Performance for Designers and developers](https://csswizardry.com/2013/01/front-end-performance-for-web-designers-and-front-end-developers/) - 网页设计师和前端开发人员的前端性能。
- [Performance as design](http://bradfrost.com/blog/post/performance-as-design/) - 将性能视为基本设计特征的最佳实践。
- [Inside Design - Setting a web performance budget](https://www.invisionapp.com/inside-design/setting-a-web-performance-budget/) - 通过 Invision 设置绩效预算。
- [Real-world Web Performance Budgets By Alex Russel](https://infrequently.org/2017/10/can-you-afford-it-real-world-web-performance-budgets/) - 你能负担得起吗？：现实世界的网络性能预算。
- [Performance Budget using Angular CLI](https://medium.com/dailyjs/how-did-angular-cli-budgets-save-my-day-and-how-they-can-save-yours-300d534aae7a) - 在 Angular 项目中实施绩效预算。
- [Performance budgets 101](https://web.dev/performance-budgets-101/) - 如何通过设置绩效预算来开始旅程。
- [Incorporate performance budgets into your build process](https://web.dev/incorporate-performance-budgets-into-your-build-tools) - 在构建过程中设置性能预算。
- [How to make Performance Budget](http://v3.danielmall.com/articles/how-to-make-a-performance-budget/) - 制定绩效预算的说明。
- [Impact of Page Weight on Load Time](https://paulcalvano.com/2018-07-02-impact-of-page-weight-on-load-time/) - 页面重量对加载时间的影响。

## 衡量绩效预算的工具

- [Performance Budget Calculator](http://www.performancebudget.io/) - 计算您网站的性能预算。
- [Web Page Test](https://www.webpagetest.org/easy) - 测试你的表现。
- [lightest app](https://www.lightest.app/) - 可视化与竞争对手相比的网络性能。
- [Speed Curve](https://speedcurve.com) - 测量网络性能，获取今天的性能指标。
- [Yellow Lab Tools](https://yellowlab.tools/) - 在线测试有助于加快繁重网页的速度。
- [Sitespeed.io](https://www.sitespeed.io/) - 轻松监控和衡量网站的性能。
- [Perf Track](https://perf-track.web.app/) - 大规模跟踪框架性能。

## 开源工具

- [Perfume.js](https://zizzamia.github.io/perfume/) - 小型 Web 性能监控库，可将现场数据报告回您最喜欢的分析工具。
- [Falco](https://github.com/theodo/falco) - 帮助您监控、分析和优化您的网站。

## 构建工具来设置性能预算

- [Bundle Size](https://github.com/siddharthkp/bundlesize) - 控制好你的捆绑包大小。
- [Webpack Perf Budget](https://webpack.js.org/configuration/performance/) - 如果您在项目中使用 Webpack，那么您可以更喜欢这个。
- [Lighthouse](https://web.dev/use-lighthouse-for-performance-budgets/) - 如何使用 [lighthouse](https://developers.google.com/web/tools/lighthouse) 设置性能预算并使用 [Lighthouse bot](https://web.dev/using-lighthouse-bot-to-set-a-performance-budget/) 实现自动化。
- [Grunt-perfbudget](https://github.com/tkadlec/grunt-perfbudget) - 绩效预算的 Grunt 任务。
- [Size Limit](https://github.com/ai/size-limit) - 计算运行 JS 应用程序或库以保持良好性能的实际成本。如果成本超出限制，则在拉取请求中显示错误。
- [Size Plugin](https://github.com/GoogleChromeLabs/size-plugin) - 随着时间的推移跟踪压缩的 Webpack 资产大小。
- [Performance Budget Builder](https://github.com/GoogleChromeLabs/pr-bot) - 布置模板类型，为每个模板类型设置尺寸预算，然后插入将在模板中加载的每个资产类别的尺寸。
- [Progressive Web Metrics](https://github.com/paulirish/pwmetrics) - 布置模板类型，为每个模板类型设置尺寸预算，然后插入将在模板中加载的每个资产类别的尺寸。
- [rollup-plugin-size-snapshot](https://github.com/TrySound/rollup-plugin-size-snapshot) - CLI 工具和库用于通过 Lighthouse 收集性能指标。
- [ImportCost - VS Extension](https://marketplace.visualstudio.com/items?itemName=wix.vscode-import-cost) - 用于在 VS 代码编辑器中内联显示导入包的大小的扩展。

## 捆绑分析仪

- [Bundlephobia](https://bundlephobia.com/) - 查找将 npm 包添加到捆绑包中的成本。
- [bundle-buddy](https://bundle-buddy.firebaseapp.com/) - 该工具可帮助您查找 JavaScript 块/拆分中的源代码重复。
- [webpack-bundle-analyzer](https://github.com/webpack-contrib/webpack-bundle-analyzer) - Webpack 插件和 CLI 实用程序将捆绑包内容表示为方便的交互式可缩放树形图。
- [Disc](http://hughsk.io/disc/) - 可视化 browserify 项目包的模块树并追踪膨胀情况。
- [lasso-analyzer](https://github.com/ajay2507/lasso-analyzer) - 分析和可视化 Lasso 创建的项目包。
- [Rollup Visualizer](https://github.com/btd/rollup-plugin-visualizer) - 可视化并分析您的 Rollup 包，看看哪些模块占用了空间。
- [Parcel plugin Visualizer](https://github.com/gregtillbrook/parcel-plugin-bundle-visualiser) - 包裹捆绑器的插件，用于可视化包裹内容。
- [CSS Analyzer](https://github.com/macbre/analyze-css) - CSS 选择器复杂性和性能分析器。

## 网站分析器
- [Lighthouse Metrics](https://lighthouse-metrics.com/) - Lighthouse Metrics 可以轻松洞察您网站的性能。通过从多个位置运行测试来获得您所需的宝贵见解，从而节省您的时间。
- [UITest.com Site Check](https://uitest.com/check/) - 使用 80 多种工具（基于网络且免费）测试您的网站。
- [PageGuard](https://pageguard.org) - 免费网站健康扫描仪。衡量核心 Web 生命体（LCP、FCP、CLS、TTFB）、性能分数并提供人工智能驱动的行动计划。无需注册。

## 博客
- [Web Performance Calender](https://calendar.perfplanet.com/2020/) - 速度极客一年中最喜欢的时间。
- [Web Performance Budget: How to Set up, Calculate, And Apply](https://uxify.com/blog/post/web-performance-budget-guide) - 如何设置、计算和应用预算

## 播客
- [Chasing Waterfalls](https://chasingwaterfalls.io/) - 与人们对话以提高网络速度 作者：[Tim kadlec](https://timkadlec.com/)
- [Shoptalk Show](https://shoptalkshow.com/) - 关于构建网站的播客。

## 视频

- [Concept of Performance Budget](https://www.youtube.com/watch?list=PLYo5nh8xQFpkwsu9QNlCpPGkmCCuTTWDJ&v=yqejmZrtmNg) - 蒂姆·卡德莱克的绩效预算。
- [Implementing Performance Budgets](https://youtu.be/vVlpCmK1l5k) - 如何实施性能预算以避免回归 - Google Chrome 开发人员。
- [Design Decisions Through The Lens Of A Performance Budget](https://vimeo.com/108328247) - 我们如何从项目一开始就做出更明智的设计决策，以确保我们的网站表现良好。
- [Revisiting Performance Budgets](https://www.youtube.com/watch?v=cnr3CJwpaps) - 重新审视绩效预算

## 书籍

- [网络性能战士](https://www.oreilly.com/library/view/web-performance-warrior/9781492048114/)
- [性能设计](http://designingforperformance.com/)

## 案例研究

- [Web Performance Optimization case studies](https://wpostats.com/) - 案例研究和实验展示了 Web 性能优化 (WPO) 对用户体验和业务指标的影响。
- [BBC - Cutting the mustard](http://responsivenews.co.uk/post/18948466399/cutting-the-mustard) - 构建响应式网站时进行优化。
- [Casper.com Self-hosting Optimization](https://medium.com/caspertechteam/we-shaved-1-7-seconds-off-casper-com-by-self-hosting-optimizely-2704bcbff8ec) - 我们如何通过自托管 Optimizely 将 casper.com 的时间缩短了 1.7 秒。
- [Netflix Performance Improvement by shipping less JS](https://medium.com/dev-channel/a-netflix-web-performance-case-study-c0bcde26a9d9) - Netflix Web 性能案例研究。
- [Pinterest Web App Optimization](https://medium.com/dev-channel/a-pinterest-progressive-web-app-performance-case-study-3bd6ed2e6154/) - Pinterest 渐进式 Web 应用程序性能案例研究。
- [Smashing Magazine's Web Performance](https://www.smashingmagazine.com/2014/09/improving-smashing-magazine-performance-case-study/) - 改进 Smashing Magazine 的 Web 性能案例研究。
- [Tinder Web App Performance](https://medium.com/@addyosmani/a-tinder-progressive-web-app-performance-case-study-78919d98ece0/) - Tinder 渐进式 Web 应用程序性能案例研究。
- [Treebo PWA Case Study](https://medium.com/dev-channel/treebo-a-react-and-preact-progressive-web-app-performance-case-study-5e4f450d5299/) - Treebo - React 和 Preact PWA 性能案例研究。
- [Twitter Lite](https://medium.com/@paularmstrong/twitter-lite-and-high-performance-react-progressive-web-apps-at-scale-d28a00e780a3/) - 大规模 Twitter Lite Web 应用程序。
- [Telegraph - Creating a web performance culture](https://medium.com/the-telegraph-engineering/improving-third-party-web-performance-at-the-telegraph-a0a1000be5) - 提高《电讯报》的第三方网络性能。
- [Zillow's Performance Budget](https://www.zillow.com/engineering/bigger-faster-more-engaging-budget/) - 关于 Zillow 如何使用绩效预算的真实故事。

## 执照

[![CC0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0)
