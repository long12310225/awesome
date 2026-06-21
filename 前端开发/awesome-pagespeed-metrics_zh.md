# 令人敬畏的页面速度指标 [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> 帮助了解页面速度和用户体验的指标。

如果您刚刚开始，请先查看 [web.dev/metrics](https://web.dev/metrics/)。

## 内容

<!-- toc -->

- [Concepts](#concepts)
  - [实验室数据（综合测量）](#lab-data-synthetic-measurements)
  - [现场数据（真实用户监控 - RUM）](#field-data-real-user-monitoring---rum)
  - [关键渲染路径](#critical-rendering-path)
  - [长任务](#long-tasks)
  - [以用户为中心的指标](#user-centric-metrics)
- [渲染指标](#rendering-metrics)
  - [首次内容绘制 (FCP)](#first-contentful-paint-fcp)
  - [最大内容涂料 (LCP)](#largest-contentful-paint-lcp)
  - [累积布局偏移 (CLS)](#cumulative-layout-shift-cls)
  - [视觉上完整](#visually-complete)
  - [速度指数](#speed-index)
  - [（英雄）元素时机](#hero-element-timing)
- [交互性指标](#interactivity-metrics)
  - [互动时间 (TTI)](#time-to-interactive-tti)
  - [总阻塞时间 (TBT)](#total-blocking-time-tbt)
  - [首次输入延迟 (FID)](#first-input-delay-fid)
  - [最大潜在第一输入延迟](#max-potential-first-input-delay)
- [网络指标](#network-metrics)
  - [DNS 延迟](#dns-latency)
  - [TCP 和 SSL/TLS 延迟](#tcp-and-ssltls-latency)
  - [第一个字节的时间 (TTFB)](#time-to-first-byte-ttfb)
  - [传输的字节数](#transferred-bytes)
- [其他指标](#other-metrics)
  - [Google PageSpeed Insights 得分](#google-pagespeed-insights-score)
  - [用户计时](#user-timing)
  - [服务器计时](#server-timing)
  - [帧率](#frame-rate)
  - [DOMContentLoaded](#domcontentloaded)
  - [window.load](#windowload)

<!-- tocstop -->

## 概念

### 实验室数据（综合测量）

使用工具向您的页面发出请求并评估性能。确保使其切合实际（例如通过限制网络和 CPU）并减少噪音（例如通过多次运行）。

- [Lighthouse](https://developers.google.com/web/tools/lighthouse/) - 一款基于 Google Chrome 构建的用于审核网页的工具。您可以从 Chrome DevTools、Chrome 扩展程序或命令行（甚至使用无头 Chrome）运行它。
- [Google PageSpeed Insights](https://developers.google.com/speed/pagespeed/insights/) - 由 Google 提供的免费托管 Lighthouse 报告（及更多内容）。
- [WebpageTest](https://www.webpagetest.org/) - 免费和托管的 Web 性能测试（也是一个开源项目）。
- [Sitespeed.io](https://www.sitespeed.io/) - 一组开源性能监控工具。
- [Calibre](https://calibreapp.com) - Web 性能监控 SaaS。
- [treo.sh](https://treo.sh/) - Web 性能监控 SaaS。
- [SpeedCurve](https://speedcurve.com/) - Web 性能监控 SaaS。
- [AwesomeTechStack](https://awesometechstack.com/) - 网站精彩程度监控工具。

---

### 现场数据（真实用户监控 - RUM）

收集访问您页面的真实用户的性能数据。请注意实际开销，因为它在用户的浏览器中运行，并注意浏览器对最新指标的支持（例如与您的用户群相比）。

- [使用 Google Analytics (GA) 进行绩效跟踪](https://philipwalton.com/articles/the-google-analytics-setup-i-use-on-every-site-i-build/#performance-tracking)
- [Chrome 用户体验报告 (CrUX)](https://developers.google.com/web/tools/chrome-user-experience-report/)
- [Load abandonment](https://developers.google.com/web/updates/2017/06/user-centric-performance-metrics#load_abandonment) - 跟踪“可见性变化”以解释幸存者偏差。
- [SpeedCurve LUX](https://speedcurve.com/features/lux/) - 真实用户监控 SaaS。
- [Akamai mPulse](https://www.akamai.com/uk/en/products/performance/mpulse-real-user-monitoring.jsp) - 真实用户监控 SaaS。
- [Sematext Experience](https://sematext.com/experience/) - 真实用户监控 SaaS。
- [Perfume.js](https://zizzamia.github.io/perfume/) - 用于收集现场数据的开源库。
- [Web Vitals](https://github.com/GoogleChrome/web-vitals) - 用于收集现场数据的开源库。
- [Vercel Analytics](https://vercel.com/docs/analytics) - 基于 Web Vitals 的真实用户监控。

### 关键渲染路径

关键渲染路径是**接收网络字节和在屏幕上渲染某些内容之间发生的所有事情**。要优化任何渲染指标，例如 [First Contentful Paint (FCP)](#first-contentful-paint-fcp) 或 [Speed Index](#speed-index)，您必须了解关键渲染路径的工作原理。

- [关键渲染路径](https://developers.google.com/web/fundamentals/performance/critical-rendering-path/)

### 长任务

处理用户输入的浏览器主线程也是执行 JavaScript（以及许多其他事情）的线程。阻塞主线程太长时间可能会使您的页面无响应。

用户将 100 毫秒内的任何视觉变化视为即时。任何耗时超过 50 毫秒而阻塞主线程的任务都被视为长任务（因为它可能会使浏览器对用户输入无响应）。

要优化 [总阻塞时间 (TBT)](#total-blocking-time-tbt) 和 [首次输入延迟 (FID)](#first-input-delay-fid) 等交互指标，您必须了解长任务以及如何尽可能避免它们。

- [规格 - 长任务](https://w3c.github.io/longtasks/)
- [博客文章 - 使用长任务 API 跟踪 CPU](https://calendar.perfplanet.com/2017/tracking-cpu-with-long-tasks-api/)

### 以用户为中心的指标

跟踪与用户及其体验相关的指标非常重要。为了衡量感知的绩效，我们可以通过围绕几个关键问题来选择指标。

- [文档 - 以用户为中心的性能指标 - web.dev](https://web.dev/user-centric-performance-metrics/)
- 它发生了吗？ - 导航启动成功了吗？服务器有响应吗？ （例如 [FCP](https://github.com/csabapalfi/awesome-web-performance-metrics/#first-contentful-paint-fcp))
- 它有用/有意义吗？ - 是否呈现了足够的内容供用户参与？ （例如 [LCP](https://github.com/csabapalfi/awesome-web-performance-metrics/#largest-contentful-paint-lcp)）
- 是否可用 - 用户可以与页面交互，还是页面仍在忙于加载？ （例如 [TBT](https://github.com/csabapalfi/awesome-web-performance-metrics/#total-blocking-time-tbt))
- 令人愉快/顺利吗？ - 交互是否流畅自然，没有滞后和卡顿？

---

## 渲染指标

### 首次内容绘制 (FCP)

首次内容绘制 (FCP) 指标衡量从页面开始加载到页面内容的任何部分呈现在屏幕上的时间。对于此指标，“内容”是指文本、图像（包括背景图像）、“<svg>”元素或非白色“<canvas>”元素。

- 实验室：灯塔
- 领域：Chrome 60+、CrUX
- [文档 - FCP - web.dev](https://web.dev/fcp/)
- [规范 - 绘制计时 - W3C](https://w3c.github.io/paint-timing/)

### 最大内容涂料 (LCP)

最大内容绘制 (LCP) 指标报告视口中可见的最大内容元素的渲染时间。

- 实验室：灯塔/WPT
- 领域：Chrome 77+
- [文档 - LCP - web.dev](https://web.dev/largest-contentful-paint/)
- [规格 - LCP - W3C](https://github.com/WICG/largest-contentful-paint#readme)

### 累积布局偏移 (CLS)

每当可见元素将其位置从一帧更改为下一帧时，都会发生布局转换。 CLS 测量页面整个生命周期内发生的每个意外布局变化的所有单独布局变化得分的总和。

- 实验室：灯塔/WPT
- 领域：Chrome 77+
- [文档 - CLS - web.dev](https://web.dev/cls/)
- [规范 - 布局不稳定 API - W3C](https://github.com/WICG/layout-instability)

### 视觉上完整

视觉完整度是指从初始导航开始到页面的**可见（首屏）部分不再发生变化**的时间。 （例如，WPT 使用基于视频/屏幕截图记录的页面颜色直方图来测量这一点）。

- 实验室：WPT
- 字段：不适用
- [文档 - 视觉上完整 - WPT](https://sites.google.com/a/webpagetest.org/docs/using-webpagetest/metrics/speed-index)

### 速度指数

速度指数显示**页面内容可见填充的速度**（数字越低越好）。这是通过在加载过程中频繁测量视觉完整性来完成的。页面越快在视觉上完成得越完整，该值就越低。

- 实验室：Lighthouse、WPT（但规格略有不同）
- 字段：不适用
- [文档 - 速度指数 - web.dev](https://web.dev/speed-index/)
- [文档 - 速度指数 - WPT](https://sites.google.com/a/webpagetest.org/docs/using-webpagetest/metrics/speed-index)
- [讲座 - 速度感知与灯塔](https://ldnwebperf.org/sessions/speed-perception-and-lighthouse/)

### （英雄）元素时机

元素计时捕获浏览器**何时绘制特定元素**。英雄元素可以定义为最大的 h1、img 或背景图像（或使用 Element Timing API 自定义）

- 实验室：WPT
- 领域：Chrome 77+
- [文档 - 最后绘制的英雄 - WPT](https://github.com/WPO-Foundation/webpagetest/blob/master/docs/Metrics/HeroElements.md)
- [规范 - 元素计时 API](https://wicg.github.io/element-timing/)
- [博客文章 - 英雄元素计时 - SpeedCurve](https://speedcurve.com/blog/web-performance-monitoring-hero-times/)

---

## 交互性指标

### 互动时间 (TTI)

交互时间是**页面完全交互所需的时间**（如主线程安静 5 秒）。有时称为一致交互，不要与首次交互或首次 CPU 空闲混淆。 （警告：最令人困惑和误解的指标之一）。

- 实验室：灯塔、WPT
- 字段：不推荐，因为与页面交互的用户可能会扭曲 TTI 的字段测量
- [文档 - TTI - web.dev](https://web.dev/tti/)
- [规格 - TTI - 灯塔](https://docs.google.com/document/d/1GGiI9-7KeY3TPqS3YT271upUVimo-XiL5mwWorDUD4c/edit)
- [博客文章 - TTI](https://blog.dareboost.com/en/2019/05/measuring-interactivity-time-to-interactive/)

### 总阻塞时间 (TBT)

总阻塞时间 (TBT) 指标测量首次内容绘制 (FCP) 和交互时间 (TTI) 之间的总时间量，其中主线程被阻塞足够长的时间以防止输入响应。

- 实验室：灯塔
- 字段：不适用
- [文档 - TBT - web.dev](https://web.dev/tbt/)

### 首次输入延迟 (FID)

首次输入延迟 (FID) 测量**从用户首次与您的网站交互到浏览器实际能够响应**该交互的时间。交互可以是用户单击链接、点击按钮或使用由 JavaScript 驱动的自定义控件。

- 实验室：不适用（因为它需要用户与页面交互）
- 字段：IE9+（以及 Safari、Chrome、Firefox）（带有 polyfill - 0.4KB）
- [文档 - FID - web.dev](https://web.dev/fid/)
- [聚合物填料 - FID](https://github.com/GoogleChromeLabs/first-input-delay)

### 最大潜在第一输入延迟

用户可能体验到的最大潜在[首次输入延迟](#first-input-delay-fid)。基本上等于浏览器主线程上最长的[长任务](#long-tasks)的持续时间。

- 实验室：灯塔
- 字段：不适用
- [文档 - 最大潜力 FID - web.dev](https://web.dev/lighthouse-max-potential-fid/)

---

## 网络指标

网络计时字段数据可以发现未优化的 TLS 设置、缓慢的 DNS 查找或服务器端处理以及 CDN 配置问题。另请参阅有关测量[已传输字节](#transferred-bytes) 的单独部分。

- [博客文章 - 导航和资源计时](https://developers.google.com/web/fundamentals/performance/navigation-and-resource-timing/)
- [规格 - 导航计时](https://www.w3.org/TR/navigation-timing-2/)
- [规范 - 资源计时](https://www.w3.org/TR/resource-timing-2/)

### DNS 延迟

- 实验室：DNS 性能测试工具
- 领域：IE9+、Safari 9+

```js
// Measuring DNS lookup time
var pageNav = performance.getEntriesByType("navigation")[0];
var dnsTime = pageNav.domainLookupEnd - pageNav.domainLookupStart;
```

### TCP 和 SSL/TLS 延迟

- 实验室：请参阅 [Qualys SSL 实验室](https://www.ssllabs.com/ssltest/index.html) 进行审核
- 领域：IE9+、Safari 9+

```js
// Quantifying total connection time
var pageNav = performance.getEntriesByType("navigation")[0];
var connectionTime = pageNav.connectEnd - pageNav.connectStart;
var tlsTime = 0; // <-- Assume 0 by default

// Did any TLS stuff happen?
if (pageNav.secureConnectionStart > 0) {
  // Awesome! Calculate it!
  tlsTime = pageNav.connectEnd - pageNav.secureConnectionStart;
}
```

### 第一个字节的时间 (TTFB)

- 实验室：大多数服务器负载测试工具都会报告这一点
- 领域：IE9+、Safari 9+

```js
var ttfb = pageNav.responseStart - pageNav.requestStart;
```

### 传输的字节数

您可以使用多种工具来测量资产的字节重量。您通常只会跟踪这些实验室，因为现场的数字通常相同（但请注意设备类型或地理位置特定页面）。

测量自己（和第三方）的 JavaScript 字节至关重要，因为 JavaScript 是 [TTI](#time-to-interactive-tti) 或 [FID](#first-input-delay-fid) 值较高的主要原因。

- 实验室：Lighthouse（预算）、Sitespeed.io、自定义工具
- 字段：N/A - 但数字通常与实验室中的相同
- [Sitespeed.io PageXray](https://www.sitespeed.io/documentation/pagexray/)
- [灯塔绩效预算](https://developers.google.com/web/tools/lighthouse/audits/budgets)
- [你能负担得起吗？：现实世界的网络性能预算](https://infrequently.org/2017/10/can-you-afford-it-real-world-web-performance-budgets/)
- [哪些第三方脚本最过分](https://github.com/patrickhulce/third-party-web)

---

## 其他指标

### Google PageSpeed Insights 得分

- [关于 PageSpeed Insights](https://developers.google.com/speed/docs/insights/v5/about)
- [Google PageSpeed 得分包含哪些内容](https://medium.com/expedia-group-tech/whats-in-the-google-pagespeed-score-a5fc93f91e91)
- [Google Pagespeed 的工作原理](https://calibreapp.com/blog/how-pagespeed-works/)

### 用户计时

用户计时 API 允许开发人员创建应用程序特定的时间戳，这些时间戳是浏览器性能时间线的一部分。例如您可以创建一个用户计时标记来测量页面上特定组件的 JS 加载时间。

- 实验室：灯塔、WPT
- 领域：IE 10+、Safari 11+（当然还有 Chrome、Firefox）
- [规格 - 用户计时](https://www.w3.org/TR/user-timing/)

### 服务器计时

在用户浏览器的开发人员工具或 PerformanceServerTiming 界面中显示任何后端服务器计时指标（例如数据库延迟等）。

- [文档 - 服务器计时](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Server-Timing)

### 帧率

帧速率是**浏览器可以显示帧的频率**。一帧表示浏览器在一次事件循环迭代中完成的工作量，例如处理 DOM 事件、调整大小、滚动、渲染、CSS 动画等。60 fps（每秒帧数）的帧速率是良好响应式用户体验的常见目标。这意味着浏览器应在大约 16.7 毫秒内处理一帧。

- 实验室：Chrome 和 FF 开发工具
- 字段：尚无浏览器实现帧计时 API，但您可以使用“requestAnimationFrame”滚动自己的 fps 计
- [文档 - 帧计时 API](https://developer.mozilla.org/en-US/docs/Web/API/Frame_Timing_API)
- [文档 - Chrome 开发工具 - FPS](https://developers.google.com/web/tools/chrome-devtools/evaluate-performance/#analyze_frames_per_second)
- [文档 - Firefox 开发者工具 - 帧速率](https://developer.mozilla.org/en-US/docs/Tools/Performance/Frame_rate)

### DOM内容已加载

- [文档 - `DOMContentLoaded`](https://developer.mozilla.org/en-US/docs/Web/Events/DOMContentLoaded)

### 窗口加载

- [文档 - `window.load`](https://developer.mozilla.org/en-US/docs/Web/Events/load)

## 许可证

[![CC0](http://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

在法律允许的范围内，Csaba Palfi 放弃了本作品的所有版权以及相关或邻接权。
