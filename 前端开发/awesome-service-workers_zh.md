# 很棒的服务人员 [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

Service Worker 资源的精选集合。

<a href="https://pwabook.com/oreillyasw"><img align="right" src="https://github.com/TalAter/awesome-progressive-web-apps/raw/master/images/mpwa.png" alt="Building Progressive Web Apps"></a>
>Service Workers 是每个渐进式 Web 应用程序的核心。它们的持久性使渐进式网络应用程序能够满足我们对应用程序应该做什么的期望。它们是只有本机应用程序才能执行的操作与现代渐进式 Web 应用程序可以执行的操作之间缺少的链接。
>
> -- <cite>[构建渐进式 Web 应用程序 - O'Reilly](https://pwabook.com/oreillyasw)</cite>

如果您想贡献，请阅读[贡献指南](contributing.md)。

## 内容

- [必读](#must-reads)
- [学习资源](#learning-resources)
- [Reference](#reference)
- [浏览器支持](#browser-support)
- [库和工具](#libraries-and-tools)
- [Videos](#videos)
- [案例研究](#case-studies)
- [相关技术](#related-technologies)

## 必读

- [Building Progressive Web Apps - O'Reilly](https://pwabook.com/oreillyasw) - 服务工作者、缓存策略、推送通知等的实践指南和参考。构建现代渐进式 Web 应用程序所需的一切。
- [Introduction to Service Worker](http://www.html5rocks.com/en/tutorials/service-worker/introduction/) - 对服务人员的温和介绍。
- [Offline Web Applications Using IndexedDB & Service Worker](https://www.udacity.com/course/offline-web-applications--ud899) - 一个很棒的 Udacity 课程，介绍了 Service Worker 和 IndexedDB。
- [Service Workers Explained](https://github.com/slightlyoff/ServiceWorker/blob/master/explainer.md) - 服务人员由 [Alex Russell](https://github.com/slightlyoff) 解释。

## 学习资源

- [Building Offline Sites with ServiceWorkers and UpUp](https://dev.opera.com/articles/offline-with-upup-service-workers/) - 对 Service Worker 以及使用 UpUp 在几分钟内提供离线功能的一般介绍。
- [Service Worker 简介](http://www.html5rocks.com/en/tutorials/service-worker/introduction/)
- [Service Workers 101](https://github.com/delapuente/service-workers-101) - 信息图总结了 Service Worker API 最重要的部分。
- [ServiceWorker Cookbook by Mozilla](https://serviceworke.rs/) - 针对不同用例的食谱集合。
- [The copy & paste guide to your first Service Worker](https://remysharp.com/2016/03/22/the-copy--paste-guide-to-your-first-service-worker) - 最短的可用介绍，作者：[Remy Sharp](https://github.com/remy)。
- [The offline cookbook](https://jakearchibald.com/2014/offline-cookbook/) - 杰克·阿奇博尔德 (Jake Archibald) 的《服务工作者模式圣经》。
- [Designing Offline-First Web Apps](http://alistapart.com/article/offline-first) - 对处理各种连接状态的设计和用户体验考虑因素进行了有趣的审视。

## 参考

- [Background Sync Spec](https://wicg.github.io/BackgroundSync/spec/) - 后台同步的 WIP 规范。
- [Service Workers - W3C Specification](https://www.w3.org/TR/service-workers/) - 官方服务人员规范。

## 浏览器支持

- [Can I Use - Service Workers](http://caniuse.com/#feat=serviceworkers) - ServiceWorker API 最新浏览器支持表。
- [Jake Archibald - Is Service Worker ready?](https://jakearchibald.github.io/isserviceworkerready/) - ServiceWorker 在不同浏览器中的支持现状。

## 库和工具

- [UpUp](http://upup.rocks/) - 一个流行的 Service Worker 库，只需一行代码即可为您的站点提供完整的离线功能。
- [sw-toolbox](https://github.com/GoogleChrome/sw-toolbox/) - 一组简单的帮助程序，用于简化常见运行时缓存模式的实现。
- [Manifest Generator](https://brucelawson.github.io/manifest/) - 生成推送通知和可安装 Web 应用程序所需的 Web 应用程序清单。
- [sw-precache](https://github.com/GoogleChrome/sw-precache/) - 生成一个 Service Worker 来缓存您的本地 App Shell 资源。
- [sw-offline-google-analytics](https://developers.google.com/web/updates/2016/07/offline-google-analytics) - 服务工作人员帮助程序库，用于在连接可用时重试离线 Google Analytics 请求。
- [Workbox](https://developers.google.com/web/tools/workbox/) - 一组库和 Node 模块，可以轻松缓存资源并充分利用用于构建渐进式 Web 应用程序的功能。

## 视频

- [Instant Loading: Building offline-first Progressive Web Apps - Google I/O 2016](https://youtu.be/cmGr0RszHc8) - 快速深入了解构建渐进式 Web 应用程序的最常见技术和技巧。
- [Offline Web Applications Using IndexedDB & Service Worker](https://www.udacity.com/course/offline-web-applications--ud899) - 如果您打算深入了解服务工作者，那么这个免费的 Udacity 课程是必须的。
- [Instant Loading with Service Workers (Chrome Dev Summit 2015)](https://www.youtube.com/watch?v=jCKZDTtUA2A) - 解释如何构建您的 Web 应用程序以优化初始访问者和回访者的加载时间，并介绍有用的 Service Worker 库，以最大程度地减少您必须编写的样板代码量。

## 案例研究

- [Service Workers in Production](https://developers.google.com/web/showcase/case-study/service-workers-iowa) - 有关如何构建 Google I/O 2015 网络应用程序的案例研究。
- [Measuring the Real-world Performance Impact of Service Workers](https://developers.google.com/web/showcase/2016/service-worker-perf) - Service Worker 最显着的好处之一（至少从性能角度来看）是他们主动控制资产缓存的能力。一个可以缓存所有必要资源的 Web 应用程序对于回访者来说加载速度应该会更快。但对于真实用户来说，这些收益实际上是什么样的呢？你如何衡量这一点？

## 相关技术

- [应用程序安装横幅](https://github.com/TalAter/awesome-progressive-web-apps#installable-web-apps)
- [后台同步](https://github.com/TalAter/awesome-progressive-web-apps#background-sync)
- [缓存存储API](https://github.com/TalAter/awesome-progressive-web-apps#cachestorage-api)
- [IndexedDB](https://github.com/TalAter/awesome-progressive-web-apps#indexeddb)
- [推送通知](https://github.com/TalAter/awesome-progressive-web-apps#push-notifications)
