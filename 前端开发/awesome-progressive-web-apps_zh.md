# 很棒的渐进式网络应用程序 [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

渐进式 Web 应用程序资源的精选集合。

<a href="https://pwabook.com/oreillyapwa"><img align="right" src="images/mpwa.png" alt="Building Progressive Web Apps"></a>
> 渐进式网络应用程序是一种新型网络应用程序。它们将本机应用程序的优点与网络的低摩擦特性结合起来。渐进式网络应用程序一开始是简单的网站，但随着用户与它们交互，它们逐渐获得新的能力。它们从网站转变为更像传统本机应用程序的东西。
>
> -- <cite>[构建渐进式 Web 应用程序 - O'Reilly](https://pwabook.com/oreillyapwa)</cite>

如果您想贡献，请阅读[贡献指南](contributing.md)。

## 内容

- [必读](#must-reads)
- [学习资源](#learning-resources)
- [浏览器支持](#browser-support)
- [Videos](#videos)
- [案例研究](#case-studies)
- [渐进式 Web 应用程序示例](#sample-progressive-web-apps)
- [具体技术](#specific-technologies)
  - [服务人员](#service-workers)
  - [缓存存储API](#cachestorage-api)
  - [后台同步](#background-sync)
  - [推送通知](#push-notifications)
  - [IndexedDB](#indexeddb)
  - [可安装的网络应用程序](#installable-web-apps)
    - [应用程序图标](#app-icons)
  - [网络共享 API](#web-share-apis)
- [出色的表现](#awesome-performance)

## 必读

- [Building Progressive Web Apps - O'Reilly Media](https://pwabook.com/oreillyapwa) - 深入探讨渐进式 Web 应用程序、服务工作者、推送通知、后台同步、IndexedDB、离线优先等等。
- [Offline Web Applications Using IndexedDB & Service Worker](https://www.udacity.com/course/offline-web-applications--ud899) - 免费的 Udacity 课程，介绍构建渐进式 Web 应用程序的基本概念。

## 学习资源

- [Google Developers - Your First Progressive Web App](https://developers.google.com/web/fundamentals/getting-started/your-first-progressive-web-app/?hl=en) - 使用应用程序 shell 模式构建渐进式 Web 应用程序的分步指南。
- [Awesome Service Workers](https://github.com/TalAter/awesome-service-workers) - 供学习服务人员使用的精彩资源的集合。
- [Service Workers W3C Specification](https://www.w3.org/TR/service-workers/) - 官方服务人员规范。

## 浏览器支持

- [Can I Use - Service Workers](http://caniuse.com/#feat=serviceworkers) - ServiceWorker API 最新浏览器支持表。
- [Is Service Worker ready?](https://jakearchibald.github.io/isserviceworkerready/) - ServiceWorker 在不同浏览器中的支持现状。

## 视频

- [Instant Loading: Building offline-first Progressive Web Apps - Google I/O 2016](https://youtu.be/cmGr0RszHc8) - 快速深入了解构建渐进式 Web 应用程序的最常见技术和技巧。
- [Intro To Progressive Web Apps](https://www.udacity.com/course/intro-to-progressive-web-apps--ud811) - 这门由 Google 提供的免费 Udacity 课程涵盖了 PWA、服务工作人员和网络应用清单的介绍。
- [Offline Web Applications Using IndexedDB & Service Worker](https://www.udacity.com/course/offline-web-applications--ud899) - 如果您打算深入了解服务工作者，那么这个免费的 Udacity 课程是必须的。
- [Progressive Web Apps (Chrome Dev Summit 2015)](https://www.youtube.com/watch?v=MyQ8mtR9WxI) - Alex Russell 和 Andreas Bovens 介绍了渐进式 Web 应用程序。
- [Polymer and Progressive Web Apps: Building on the modern web - Google I/O 2016](https://www.youtube.com/watch?v=fFF2Yup2dMM) - 使用 Polymer 构建渐进式 Web 应用程序。

## 案例研究

- [Building the Google I/O 2016 Progressive Web App](https://developers.google.com/web/showcase/2016/iowa2016) - 使用 Web 组件、Polymer 和材料设计构建和启动渐进式 Web 应用程序。
- [AliExpress Case Study](https://developers.google.com/web/showcase/2016/aliexpress) - AliExpress 通过新的渐进式网络应用程序将新用户的转化率提高了 104%。
- [eXtra Electronics Case Study](https://developers.google.com/web/showcase/2016/extra) - United eXtra Electronics 通过网络推送通知将电子商务销售额增长了 100%。
- [Jumia Case Study](https://developers.google.com/web/showcase/2016/jumia) - 推送通知帮助 Jumia 扭转购物车放弃现象，并将转化率提高 9 倍。
- [Konga Case Study](https://developers.google.com/web/showcase/2016/konga) - Konga 通过新的渐进式网络应用程序将数据使用量减少了 92%。
- [Suumo Case Study](https://developers.google.com/web/showcase/2016/suumo) - 日本顶级房地产网站通过网络推送通知增强新列表的吸引力，通知打开率高达 31%。

## 渐进式 Web 应用程序示例

- [PWA.rocks](https://pwa.rocks/) - 几个渐进式 Web 应用程序的展示，由 [Opera Dev 关系团队](https://twitter.com/ODevRel) 收集。
- [SVGOMG](https://jakearchibald.github.io/svgomg/)
- [吉他调音器](https://aerotwist.com/blog/guitar-tuner/)
- [语音备忘录](https://voice-memos.appspot.com/)
- [黑客新闻](https://react-hn.appspot.com/)

## 具体技术

### 服务人员

- [Awesome Service Workers](https://github.com/TalAter/awesome-service-workers/) - 最好的服务工作者资源的精选集合。

### 缓存存储API

- [Offline Storage for Progressive Web Apps](https://medium.com/@addyosmani/offline-storage-for-progressive-web-apps-70d52695513c) - 浏览器中离线存储的当前状态
- [CacheStorage API](https://developer.mozilla.org/en-US/docs/Web/API/Cache) - API 文档和来自 Mozilla 的示例代码。

### 后台同步

- [Introducing Background Sync](https://developers.google.com/web/updates/2015/12/background-sync) - 对后台同步的简单介绍，以及一些精彩的视频和代码示例。
- [Background Sync Explained](https://github.com/WICG/BackgroundSync/blob/master/explainer.md) - 后台同步的官方“解释器”文档，包括一次性同步和周期性同步。
- [Background Sync Spec](https://wicg.github.io/BackgroundSync/spec/) - 后台同步的 WIP 规范。

### 推送通知

- [Can I Use - Push API](http://caniuse.com/#feat=push-api) - Push API 的最新浏览器支持表。
- [Chrome Platform Status - Web Notifications](https://www.chromestatus.com/feature/5480344312610816) - Chrome 和其他浏览器的实施状态。
- [2016 年 PWA 开发峰会代码实验室 - 推送通知](https://developers.google.com/web/fundamentals/getting-started/push-notifications/?hl=en) 有关渐进式 Web 应用程序、推送通知和 Service Worker 基础知识的最新入门教程。
- [Using the Push API](https://developer.mozilla.org/en-US/docs/Web/API/Push_API/Using_the_Push_API) - 一篇介绍 Push API 的文章。
- [web-push-libs](https://github.com/web-push-libs) - 不同技术（Node.js、PHP、Python 等）中用于 Web 推送的有用库的集合

### 索引数据库

- [IndexedDB API](https://developer.mozilla.org/en/docs/Web/API/IndexedDB_API) - 来自 Mozilla 的 API 文档、关键概念和示例代码。

### 可安装的网络应用程序

- [Increasing Engagement with Web App Install Banners](https://developers.google.com/web/updates/2015/03/increasing-engagement-with-app-install-banners-in-chrome-for-android?hl=en) - 应用安装横幅简介以及确保 Chrome 向用户提供您的网络应用。
- [Installable Web Apps with the Web App Manifest in Chrome for Android](https://developers.google.com/web/updates/2014/11/Support-for-installable-web-apps-with-webapp-manifest-in-chrome-38-for-Android) - 介绍 Android 版 Chrome 中可安装的 Web 应用程序。

#### 应用程序图标

- [RealFaviconGenerator](http://realfavicongenerator.net/) - 这是生成在不同浏览器上显示应用程序图标所需的所有图像、网站图标和关联文件的好方法。
- [Android Asset Studio - Launcher Icon Generator](https://romannurik.github.io/AndroidAssetStudio/icons-launcher.html) - 生成Android风格的图标。

### 网络共享 API

- [Introducing the Web Share API](https://developers.google.com/web/updates/2016/10/navigator-share) - Web Share API 的高级介绍。
- [Web Share API explainer](https://github.com/WICG/web-share/blob/master/docs/explainer.md) - API 的解释以及一些示例。提案文档的一部分。
- [Web Share Target API](https://github.com/WICG/web-share-target) - Web Share Target API 的提案以及高级[解释器](https://github.com/WICG/web-share-target/blob/master/docs/explainer.md)。

## 出色的表现

- [Web Fundamentals - Performance](https://developers.google.com/web/fundamentals/performance/) - Google 的性能学习门户，包含有关优化网络应用程序性能的丰富知识。
- [Introducing RAIL: A User-Centric Model For Performance](https://www.smashingmagazine.com/2015/10/rail-user-centric-model-performance/) - Gang of Pauls 对 RAIL 的开创性介绍。
- [Website Performance Optimization](https://udacity.com/ud884) - 关于优化网站速度的免费 Udacity 课程。
- [Browser Rendering Optimization](https://udacity.com/ud860) - 免费的 Udacity 课程可帮助您创建保持无卡顿 60fps 性能的 Web 应用程序。
- [The PRPL Pattern](https://developers.google.com/web/fundamentals/performance/prpl-pattern/) - 构建和服务渐进式 Web 应用程序的新模式，重点关注性能。
- [Browser Rendering Performance](https://developers.google.com/web/fundamentals/performance/rendering/) - 了解浏览器如何处理 HTML、JavaScript 和 CSS，以及如何相应地优化您的页面。

