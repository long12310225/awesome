# 离线优先 [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

> 用于创建离线优先 Web 应用程序的有用资源

> “网络”和“在线”是两个密切相关的术语，对许多人来说完全是同义词。那么我们到底为什么要谈论“离线”网络技术，这个术语究竟意味着什么？

受到 [awesome](https://github.com/sindresorhus/awesome) 列表的启发。

## 目录
- [W3C 规范](#w3c-specification)
- [Newsletter](#newsletter)
- [Posts](#posts)
- [Presentations](#presentations)
  - [Videos](#videos)
  - [Slides](#slides)
- [Tools](#tools)
- [Books](#books)
- [Showcase](#showcase)
- [关注谁](#who-to-follow)
- [Contributing](#contributing)

## W3C 规范

[离线网络应用程序](http://www.w3.org/TR/offline-webapps/)
> 本规范重点介绍了 HTML5 的功能（SQL、离线应用程序缓存 API 以及在线/离线事件、状态和 localStorage API），并提供了有关如何使用这些功能创建离线工作的 Web 应用程序的简要教程。

[服务工作者](http://www.w3.org/TR/service-workers/)
> 本规范描述了一种使应用程序能够利用持久后台处理的方法，包括在离线时启用 Web 应用程序引导的挂钩。

[IndexedDB](http://www.w3.org/TR/IndexedDB/)
> 该规范定义了保存简单值和分层对象的记录数据库的 API。每条记录都由一个键和一些值组成。此外，数据库还维护其存储的记录的索引。应用程序开发人员直接使用 API 通过键或索引来定位记录。查询语言可以在此 API 上分层。索引数据库可以使用持久 B 树数据结构来实现。


## 时事通讯
[离线第一读者](http://offlinefirst.us4.list-manage1.com/subscribe?u=12d36bbe9418ed6a43127cd62&id=7fc00bfaef)。每月一次的读者，以离线优先为主题，涵盖新离线用例的理论、技术和用户体验。

## 帖子

[离线优先 Web 应用程序的设计模式](https://blog.bitsrc.io/design-patterns-for-offline-first-web-apps-5891a4b06f3a)
（拉维杜·佩雷拉 - 2022 年 9 月 20 日）

[让 PWA 与 Service Worker 一起离线工作](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Offline_Service_workers)
（MDN - 2022 年 9 月 9 日）

[为什么 Web 应用程序需要静态加密？](https://levelup.gitconnected.com/why-would-a-web-app-need-encryption-at-rest-3efd10c145e1)
（埃里克·赫尔曼森 - 2022 年 5 月 31 日）

[离线用户体验设计指南](https://web.dev/offline-ux-design-guidelines/)
（穆斯塔法·库尔图杜、托马斯·施泰纳 - 2022 年 6 月 13 日）

[如何针对慢速网络和离线进行设计](https://uxplanet.org/youre-not-connected-to-internet-50a46ee016a7)
（尼克·巴比奇 - 2022 年 2 月 17 日）

[离线优先的缺点](https://rxdb.info/downsides-of-offline-first.html)
（丹尼尔·迈耶 - 2021 年 10 月 3 日）

[关于离线优先](https://rxdb.info/offline-first.html)
（丹尼尔·迈耶 - 2021 年 10 月 1 日）

[创建离线后备页面](https://web.dev/offline-fallback-page/)
（托马斯·斯坦纳、皮特·勒佩奇 - 2020 年 9 月 24 日）

[构建离线优先应用程序的设计指南](https://hasura.io/blog/design-guide-to-offline-first-apps)
（高塔姆英国电信 - 2020 年 2 月 13 日）

[制作真正的离线优先应用程序的挑战](https://medium.com/idea-growr/rebuilding-idea-growr-offline-first-using-react-native-graphql-docker-during-our-hackaton-576b6f7a8b90)
（朱利叶斯·惠因克 - 2019 年 6 月 4 日）

[离线优先应用程序的可访问性测试](https://medium.com/ibm-watson-data-lab/accessibility-testing-for-offline-first-applications-d8d2bfd24a6e)
（莫琳·麦克伊莱尼 - 2017 年 11 月 6 日）

[如何向您的 PWA 添加“离线”通知](https://medium.com/@argo49/how-to-add-an-offline-notification-to-your-pwa-c11ee640822b)
（泰勒·阿尔戈 - 2017 年 10 月 28 日）

[使用 MVVM、RxJava、Room 和优先级作业队列构建离线优先应用程序](https://proandroiddev.com/offline-apps-its-easier-than-you-think-9ff97701a73f)
（詹姆斯·什瓦茨 - 2017 年 10 月 8 日）

[支持离线用户 — 中断时会发生什么？](https://medium.com/offline-camp/supporting-offline-users-what-happens-when-it-breaks-562f7dcea0a9)
（约翰·克莱因施密特 - 2017 年 9 月 27 日）

[使用 React 和 Preact 构建我的第一个离线应用程序](https://medium.com/offline-camp/using-react-and-preact-to-build-my-first-offline-first-apps-8df4a1e5471b)
（尼克·卡斯滕 - 2017 年 9 月 5 日）

[离线友好表单](https://mxb.at/blog/offline-forms/)
（马克斯·博克 - 2017 年 8 月 23 日）

[Service Worker：任意宽高比的一张备用离线图像](https://hackernoon.com/service-worker-one-fallback-offline-image-for-any-aspect-ratio-b427c0f897fb)
（塞巴斯蒂安·埃伯莱因 - 2017 年 8 月 14 日）

[您已离线](https://mxb.at/blog/youre-offline/)
（马克斯·博克 - 2017 年 7 月 12 日）

[[第 2 部分] 使用 Service Worker 在 Angular 应用程序中获得快速离线功能](https://medium.com/onehourcode/part-2-get-rapid-offline-capability-in-your-angular-app-with-service-worker-954f17109dd0)
（雨果·多兰 - 2017 年 6 月 28 日）

[持久存储 API：为离线网络构建](https://deanhume.com/Home/BlogPost/persistent-storage-api--building-for-the-offline-web/10161)
（迪恩·休姆 - 2017 年 6 月 26 日）

[[第 1 部分] 使用 Service Worker 在 Angular 应用程序中获得快速离线功能](https://medium.com/onehourcode/part-1-get-rapid-offline-capability-in-your-angular-app-with-service-worker-762a889a503d)
（雨果·多兰 - 2017 年 6 月 21 日）

[使用 ServiceWorkers 构建可在极低网络条件下工作的离线 Web 应用程序](https://medium.com/progressive-web-apps/building-offline-webapp-using-serviceworkers-8939a694cc5)
（哈里克里希纳 - 2017 年 6 月 16 日）

[渐进式 Web 应用程序中的离线 POST](https://medium.com/@nitish404/offline-post-in-progressive-web-apps-3d02f893b223)
（尼蒂什·塔库尔 - 2017 年 6 月 23 日）

[离线优先设计模式：工程](https://medium.com/offline-camp/offline-first-design-patterns-engineering-1c66821137d3)
（阿尼鲁达·贝德尔 - 2017 年 3 月 28 日）

[Redux Offline 简介：渐进式 Web 应用程序和 React Native 的离线优先架构](https://hackernoon.com/introducing-redux-offline-offline-first-architecture-for-progressive-web-applications-and-react-68c5167ecfe0)
（贾尼·埃瓦卡利奥 - 2017 年 3 月 28 日）

[重新思考 Service Workers 的离线首次同步](https://medium.com/offline-camp/rethinking-offline-first-sync-for-service-workers-da4727b6dee)
（诺兰·劳森 - 2017 年 3 月 16 日）

[离线支持：“稍后再试”，不再。](https://medium.com/@yonatanvlevin/offline-support-try-again-later-no-more-afc33eba79dc)
（约纳坦诉莱文 - 2017 年 3 月 2 日）

[使用 HTTP/2 服务器推送和 Service Workers 进行优化！](https://blog.yld.io/2017/03/01/optimize-with-http-2-server-push-and-service-workers)
（丹妮拉·马托斯·德卡瓦略 - 2017 年 3 月 1 日）

[了解Android中的离线优先和离线最后](https://medium.com/@coreflodev/understand-offline-first-and-offline-last-in-android-71191e92b426)
（弗洛伦特·吉勒莫 - 2017 年 2 月 27 日）

[为什么首先离线？](https://medium.com/buildit/why-offline-first-20470604ee36)
（扎卡里·史密斯 - 2017 年 2 月 22 日）

[当您重新上线时使用 Service Workers 和后台同步发送消息](https://www.twilio.com/blog/2017/02/send-messages-when-youre-back-online-with-service-workers-and-background-sync.html)
（菲尔·纳什 - 2017 年 2 月 17 日）

[使用 Webpack 离线插件轻松离线第一个应用程序](https://dev.to/kayis/easy-offline-first-apps-with-webpacks-offline-plugin)
（凯·普洛瑟 - 2017 年 2 月 12 日）

[离线首个 React Native + Meteor 应用](https://hackernoon.com/offline-first-react-native-meteor-apps-2bee8e976ec7)
（斯宾塞·卡利 - 2017 年 2 月 8 日）

[使用 Redux 和 PouchDB 的离线优先 Web 应用程序](https://stories.jotform.com/offline-first-web-applications-d2d321444510)
（贝尔凯·艾登 - 2017 年 1 月 30 日）

[与 Service Workers 一起实施“离线保存”。](https://una.im/save-offline)
（尤娜·克拉维茨 - 2017 年 1 月 26 日）

[超越本地存储](https://journal.standardnotes.org/moving-beyond-localstorage-991e3695be15#.wqzo3mpuz)
（莫比塔尔 - 2017 年 1 月 17 日）

[我的 Service Worker 应该在离线缓存中预先放入多少数据？](https://nicolas-hoizey.com/2017/01/how-much-data-should-my-service-worker-put-upfront-in-the-offline-cache.html)
（尼古拉斯·霍伊泽 - 2017 年 1 月 12 日）

[使弹性网页设计离线工作](https://medium.com/@adactio/making-resilient-web-design-work-offline-a5854781b75b#.8khh8bnio)
（杰里米·基思 - 2017 年 1 月 11 日）

[使用 Service Workers 和缓存将 Web 性能提升到新水平](https://calendar.perfplanet.com/2016/service-workers-cache-web-performance-new-level/)
（克里斯·乐福 - 2016 年 12 月 23 日）

[伪造进度（Service Worker版）](https://medium.com/remys-blog/faking-progress-service-worker-edition-4c3fa16e5b32#.coya1w3ki)
（雷米·夏普 - 2016 年 12 月 22 日）

[渐进式 Web 应用程序简介（离线优先）](https://auth0.com/blog/introduction-to-progressive-apps-part-one/)
（Prosper Otemuyiwa - 2016 年 12 月 19 日）

[不会再被愚弄：Lie-Fi 的教训](https://medium.com/outsystems-engineering/wont-get-fooled-again-lessons-in-lie-fi-9097052ea66e#.texx2j9pd)
（里卡多·费雷拉 - 2016 年 12 月 15 日）

[针对意外断开进行设计：我们首次尝试离线方法](http://blog.gethop.io/2016/12/14/designing-for-accidental-disconnects-our-first-attempt-at-an-offline-approach/)
（维维安·克伦威尔 - 2016 年 12 月 14 日）

[离线模式：还有很多工作要做](https://medium.com/offline-camp/offline-patterns-there-are-many-jobs-to-be-done-9f97f7e89304#.54tbekzbf)
（史蒂夫·特雷瓦森 - 2016 年 12 月 13 日）

[编写离线网络应用程序很容易](https://medium.com/@aliafshar/writing-offline-web-apps-is-easy-bc5ece2ed16e#.26kewn4dd)
（阿里·阿夫沙尔 - 2016 年 12 月 9 日）

[构建一个能够“离线工作”的 Web 应用程序](https://blog.super human.com/architecting-a-web-app-to-just-work-offline-part-1-8697f316c0eb#.i6y75or3v)
（伊斯兰沙拉巴什 - 2016 年 12 月 6 日）

[离线应用架构：如何构建下一个十亿](https://hackernoon.com/so-you-want-to-develop-for-the-next-billion-9eb072c26bc8#.30ev0831v)
（阿伦·萨西达兰 - 2016 年 12 月 4 日）

[跨域 Service Worker：尝试外部获取](https://developers.google.com/web/updates/2016/09/foreign-fetch)
（杰夫·波斯尼克 - 2016 年 12 月）

[Service Worker，你是什么？](https://medium.com/@kosamari/service-worker-what-are-you-ca0f8df92b65#.wc6eggecd)
（小坂真理子 - 2016 年 12 月 1 日）

[设计为离线优先](https://medium.com/hypertrack/Design-to-be-offline-first-def41a3668b8#.a0u11gp4j)
（阿琼·阿塔姆 - 2016 年 11 月 29 日）

[黑客时间：Service Workers、后台同步和 PouchDB](https://medium.com/offline-camp/hack-time-service-workers-background-sync-and-pouchdb-3c8b71535823#.qlqbjm6dw)
（约翰·克莱因施密特 - 2016 年 11 月 29 日）

[离线用户体验注意事项](https://developers.google.com/web/fundamentals/instant-and-offline/offline-ux)
（穆斯塔法·库尔图杜 - 2016）

[离线存储敏感数据](https://medium.com/offline-camp/storing-sensitive-data-offline-cec851df95e3#.g78qucejz)
（保罗·弗雷泽 - 2016 年 11 月 17 日）

[构建离线第一个 React Native 应用程序](https://medium.com/ Differential/building-offline-first-react-native-apps-b958acac0009#.94hfszbig)
（斯宾塞·卡利 - 2016 年 11 月 16 日）

[使用 ServiceWorker 构建简单的具有离线功能的记事本应用程序](https://hackernoon.com/building-a-simple-offline-capable-notepad-app-using-serviceworker-97b9b50767a5#.k9zhvs3ep)
（阿米特·麦钱特 - 2016 年 11 月 15 日）

[使用 Google 的应用程序 Shell 架构即时加载 Web 应用程序](https://developers.google.com/web/updates/2015/11/app-shell)
（阿迪·奥斯马尼和马特·冈特 - 2016）

[我在加利福尼亚州圣玛格丽塔的第二个线下营中最大的收获 — 加上吐司！](https://medium.com/@jessebeach/my-biggest-takeaway-from-the-second-offline-camp-in-santa-margarita-ca-d0dd930cd02b#.di93bftj9)
（J. Renée Beach - 2016 年 11 月 8 日）

【2016年线下体验】(https://medium.com/@leofle/the-offline-experience-in-2016-83b1f00d7bfa#.nk8910brf)
（里奥·弗莱什曼 - 2016 年 10 月 27 日）

[关于离线我错了](https://medium.com/outsystems-engineering/i-was-wrong-about-offline-fe5426894740#.yb9hhitn0)
（蒂亚戈·西蒙斯 - 2016 年 10 月 20 日）

[离线策略出现在 Service Worker Cookbook 中](https://hacks.mozilla.org/2016/10/offline-strategies-come-to-the-service-worker-cookbook/)
（萨尔瓦 - 2016 年 10 月 19 日）

[使用 IndexedDB 进行“即时加载”（构建 PWA，第 2 部分）](https://bitsofco.de/bitsofcode-pwa-part-2-instant-loading-with-indexeddb/)
（艾尔·阿德里诺昆 - 2016 年 10 月 18 日）

[Service Worker 生命周期](https://developers.google.com/web/fundamentals/instant-and-offline/service-worker/lifecycle)
（杰克·阿奇博尔德 - 2016 年 10 月 13 日）

[使用 Service Worker 实现“离线优先”（构建 PWA，第 1 部分）](https://bitsofco.de/bitsofcode-pwa-part-1-offline-first-with-service-worker/)
（艾尔·阿德里诺昆 - 2016 年 10 月 11 日）

[您的网络应用程序中需要 Service Worker 吗？](https://codingbox.io/do-you-need-service-worker-in-your-web-app-d68131d65e2c?gi=666f4385e803)
（瓦莱里·亚茨科 - 2016 年 10 月 9 日）

[使用 React.js 的渐进式 Web 应用程序：第 3 部分 — 离线支持和网络弹性]（https://medium.com/@addyosmani/progressive-web-apps-with-react-js-part-3-offline-support-and-network-resilience-c84db889162c?source=userActivityShare-136a881c591e-1475748613）
（阿迪·奥斯马尼 - 2016 年 10 月 5 日）

[离线阅读列表](https://chrisruppel.com/blog/service-worker-offline-content-list/)
（克里斯·鲁佩尔 - 2016 年 10 月 5 日）

[几乎任何网页都可以离线工作](https://github.com/homam/service-workers-example)
（霍曼·胡赛尼 - 2016 年 9 月 24 日）

[通过 Service Worker 在 Web 上实现离线首次体验](https://medium.com/offline-camp/enabling-offline-first-experiences-on-the-web-with-service-workers-e4bc8c773dae#.c6ui0i9cs)
（丹·扎伊德班德 - 2016 年 9 月 12 日）

[离线构建更可靠的 Web 应用程序](http://thenewstack.io/build-better-customer-experience-applications-using-offline-first-principles/)
（佩德罗·特谢拉 - 2016 年 9 月 7 日）

[Songsearch – 使用 ServiceWorker 使 4 MB CSV 在浏览器中轻松搜索](https://www.christianheilmann.com/2016/08/26/songsearch-using-serviceworker-to-make-a-4-mb-csv-easily-searchable-in-a-browser/)
（克里斯蒂安·海尔曼 - 2016 年 8 月 26 日）

[渐进式 Web 应用程序的离线存储](https://medium.com/dev-channel/offline-storage-for-progressive-web-apps-70d52695513c#.ryrpvq43r)
（阿迪·奥斯马尼 - 2016 年 8 月 15 日）

[向任何网络应用程序添加离线支持](https://medium.com/google-developer-experts/add-offline-support-to-any-web-app-c20edc4bea0e#.jeseb4ovf)
（瓦西姆·切格姆 - 2016 年 7 月 23 日）

[ServiceWorker：BackgroundSync 基本指南](https://ponyfoo.com/articles/backgroundsync)
（迪恩·休谟 - 2016 年 7 月 19 日）

[离线优先、去中心化网络和点对点技术](https://medium.com/offline-camp/offline-first-the-decentralized-web-and-peer-to-peer-technologies-b05b7fb3bcdd#.6xdfvy6on)
（佩德罗·特谢拉 - 2016 年 7 月 15 日）

[离线 Google Analytics 变得简单](https://developers.google.com/web/updates/2016/07/offline-google-analytics)
（杰夫·波斯尼克 - 2016 年 7 月）

[离线优先应用程序的安全性](https://medium.com/offline-camp/offline-first-security-59bf4800e82a)
（卡尔文·梅特卡夫 - 2016 年 7 月 8 日）

[我的博客的Service Worker和缓存策略](https://paul.kinlan.me/my-blogs-service-worker-and-caching-strategy/)
（保罗·金兰 - 2016 年 6 月 15 日）

[离线/低带宽用户体验设计模式](https://medium.com/offline-camp/offline-low-bandwidth-ux-design-patterns-51391230a79e#.sctlcxk4e)
（史蒂夫·特雷瓦森 - 2016 年 7 月 8 日）

[Service Worker 的离线内容](https://chrisruppel.com/blog/service-worker-offline-content/)
（克里斯·鲁佩尔 - 2016 年 6 月 6 日）

[将在线图书离线](https://adactio.com/journal/10754)
（杰里米·基思 - 2016 年 6 月 3 日）

[Service Workers — 陷阱](https://medium.com/@boopathi/service-workers-gotchas-44bec65eab3f#.4q0ncllos)
（布帕蒂·拉贾 - 2016 年 5 月 9 日）

[离线优先 QR 码徽章扫描器](https://developer.ibm.com/clouddataservices/2016/05/05/offline-first-qr-code-badge-scanner/)
（格林·伯德 - 2016 年 5 月 5 日）

[Service Workers 和 PWA：重要的是可靠的性能，而不是“离线”](https://infrequently.org/2016/05/service-workers-and-pwas-its-about-reliable-performance-not-offline/)
（亚历克斯·拉塞尔 - 2016 年 5 月 4 日）

[渐进式网络应用程序：吃你的蛋糕](https://medium.com/@torgo/progressive-web-apps-eating-your-cake-c0a79797220f#.jp6qup8xg)
（丹尼尔·阿佩尔奎斯特 - 2016 年 4 月 27 日）

[带有 Service Workers 的渐进式 Web 应用程序](http://blog.booking.com/progressive-web-apps-with-service-workers.html)
（杰西·杨 - 2016 年 4 月 21 日）

[如何在 Ionic 2 中使用 PouchDB + SQLite 进行本地存储](http://gonehybrid.com/how-to-use-pouchdb-sqlite-for-local-storage-in-ionic-2/)
（Ashteya Biharisingh - 2016 年 4 月 18 日）

[离线优先、文档共享、模板：Monod 回来了（不是黑色）](https://tailordev.fr/blog/2016/04/15/le-lab-2-offline-first-document-sharing-templates-monod-is-back/)
（2016 年 4 月 15 日）

[问题 4：离线标记、DevTools、测试、Travis、Web 存储、Service Worker 范围、数据驱动开发、计算引擎](https://medium.com/totally-tooling-tears/issue-4-offline-badging-testing-travis-devtools-issues-web-storage-data-driven-development-8dd1cfbc410a#.mgur8g8n3)
（阿迪·奥斯马尼 - 2016 年 4 月 15 日）

[新建设者EP。 1：精酿啤酒和渐进式 Web 应用程序](https://developer.ibm.com/tv/untappd-web-apps/)
（道格拉斯·弗洛拉 - 2016 年 4 月 14 日）

[Service Workers 取代 AppCache：一把大锤破解坚果](https://medium.com/@firt/service-workers-replacing-appcache-a-sledgehammer-to-crack-a-nut-5db6f473cc9b#.sdp7iqxc3)
（马克西米利亚诺·菲尔特曼 - 2016 年 4 月 11 日）

[渐进式 Web 应用程序 — 离线并添加到主屏幕](https://medium.com/@greenido/progressive-web-apps-offline-and-add-to-home-screen-2187a2487a5c#.7m52kq892)
（伊多·格林 - 2016 年 3 月 28 日）

[手机上的网络](https://adactio.com/journal/10410)
（杰里米·基思 - 2016 年 3 月 23 日）

[第一个 Service Worker 的复制和粘贴指南](https://remysharp.com/2016/03/22/the-copy--paste-guide-to-your-first-service-worker)
（雷米·夏普 - 2016 年 3 月 22 日）

[Service Workers：使用 Save-Data 标头保存用户数据](http://www.deanhume.com/Home/BlogPost/service-workers--save-your-users-data-using-the-save-data-header/10139)
（迪恩·休谟 - 2016 年 3 月 8 日）

[Service Worker 笔记](https://adactio.com/journal/10186)
（杰里米·基思 - 2016 年 2 月 4 日）

[打造 Service Worker：案例研究](https://www.smashingmagazine.com/2016/02/making-a-service-worker/)
（莱扎·危险·加德纳 - 2016 年 2 月 1 日）

[使用 Service Workers 创建一个非常非常简单的离线页面](http://deanhume.com/home/blogpost/create-a-really--really-simple-offline-page-using-service-workers/10135)
（迪恩·休谟 - 2016 年 1 月 25 日）

[离线Web应用程序：使用IndexedDB和Service Worker](https://www.udacity.com/course/offline-web-applications--ud899)
（迈克尔·威尔士 - 2016 年 1 月 20 日）

[使用 ServiceWorkers 和 UpUp 构建离线站点](https://dev.opera.com/articles/offline-with-upup-service-workers/)
（塔尔阿特 - 2016 年 1 月 19 日）

[即时网络应用程序](https://glebbahmutov.com/blog/instant-web-application/)
（格列布·巴穆托夫 - 2015 年 12 月 24 日）

[后台同步简介](https://developers.google.com/web/updates/2015/12/background-sync)
（杰克·阿奇博尔德 - 2015）

[超越离线](https://hacks.mozilla.org/2015/12/beyond-offline/)
（萨尔瓦多·德拉普恩特·冈萨雷斯 - 2015 年 12 月 21 日）

[Service Worker 工具箱入门](http://deanhume.com/Home/BlogPost/getting-started-with-the-service-worker-toolbox/10134)
（迪恩·休谟 - 2015 年 12 月 17 日）

[ServiceWorker 食谱](https://serviceworke.rs/)
（由 Mozilla 提供）

[使用 CouchDB、PouchDB 和 Ember CLI 的离线 Web 应用程序](https://teamgaslight.com/blog/offline-web-applications-with-couchdb-pouchdb-and-ember-cli)
（克里斯·摩尔 - 2015 年 12 月 10 日）

[连帽衫案例研究：mines.io 如何离线](http://hood.ie/blog/minutes-offline-case-study)
（亚历克斯·费耶克 - 2015 年 12 月 1 日）

[使用 Service Worker 减少单点故障](http://calendar.perfplanet.com/2015/reducing-single-point-of-failure-using-service-workers/)
（迪恩·休谟 - 2015 年 12 月 1 日）

[使用 React、Redux、PouchDB 和 WebSockets 构建实时协作离线优先应用程序](https://blog.yld.io/2015/11/30/building-realtime-collaborative-offline-first-apps-with-react-redux-pouchdb-and-web-sockets/)
（佩德罗·特谢拉 - 2015 年 11 月 30 日）

[Service Workers 中的缓存限制……再次](https://adactio.com/journal/9888)
（杰里米·基思 - 2015 年 11 月 29 日）

[Pokedex.org 简介：一款面向 Pokémon 粉丝的渐进式网络应用程序](http://www.pocketjavascript.com/blog/2015/11/23/introducing-pokedex-org)
（诺兰·劳森 - 2015 年 11 月 23 日）

[Service Workers 中的缓存限制](https://adactio.com/journal/9844)
（杰里米·基思 - 2015 年 11 月 19 日）

[Service Workers 的离线秘诀](https://hacks.mozilla.org/2015/11/offline-service-workers/)
（大卫·沃尔什 - 2015 年 11 月 19 日）

[使用应用程序 Shell 架构即时加载 Web 应用程序](https://medium.com/google-developers/instant-loading-web-apps-with-an-application-shell-architecture-7c0c2f10c73)
（阿迪·奥斯马尼 - 2015 年 11 月 17 日）

【Service Workers 的线下体验】(http://brandonrozek.tumblr.com/post/135657690564/service-workers)
（布兰登·罗泽克 - 2015 年 11 月 14 日）

[构建 Flipkart Lite：渐进式 Web 应用程序](https://medium.com/@AdityaPunjani/building-flipkart-lite-a-progressive-web-app-2c211e641883)
（阿迪亚·旁贾尼 - 2015 年 11 月 11 日）

[您的第一个离线网络应用程序](https://developers.google.com/web/fundamentals/getting-started/codelabs/offline/)
（Chrome 开发团队 - 2015 年）

[使用 ServiceWorker 使简单站点离线工作](https://css-tricks.com/serviceworker-for-offline/)
（尼古拉斯·贝瓦夸 - 2015 年 11 月 10 日）

[我的第一个 Service Worker](https://medium.com/@adactio/my-first-service-worker-5e5af0b1bdbb#.tsjcjzk2n)
（杰里米·基思 - 2015 年 11 月 7 日）

[为 theguardian.com 构建离线页面](https://www.theguardian.com/info/developer-blog/2015/nov/04/building-an-offline-page-for-theguardiancom)
（奥利弗·约瑟夫·阿什 - 2015 年 11 月 4 日）

[使用 Service Workers 创建离线优先的 Web 应用程序](https://auth0.com/blog/2015/10/30/creating-offline-first-web-apps-with-service-workers/)
（瑞安·陈基 - 2015 年 10 月 30 日）

[使用 Service Worker 缓存沙盒 HTTP 请求](https://medium.com/@roman01la/cache-sandboxed-http-requests-with-service-worker-6bb3801237d1#.3jjklzohz)
（罗曼·刘季科夫 - 2015 年 10 月 26 日）

[离线体验（或者，告别命令式数据获取）](https://medium.com/@d.gieselaar/the-offline-experience-or-saying-goodbye-to-imperative-data-fetching-9b2fa487eea7)
（达里奥·吉斯拉尔 - 2015 年 10 月 25 日）

[ServiceWorker：Web 平台的革命](https://ponyfoo.com/articles/serviceworker-revolution)
（尼古拉斯·贝瓦夸 - 2015 年 10 月 21 日）

[通过 Service Worker 让网络离线](https://mobiforge.com/design-development/take-web-offline-service-workers)
（鲁丹·奥多诺霍 - 2015 年 10 月 21 日）

[使用 Service Worker](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API/Using_Service_Workers)
（MDN - 2015 年 10 月 18 日）

[不要等待 ServiceWorker：使用 One-Line 添加离线支持](https://davidwalsh.name/dont-wait-serviceworker-adding-offline-support-oneline)
（肯尼思·奥曼迪 - 2015 年 10 月 14 日）

[生产中的 Service Worker](https://developers.google.com/web/showcase/2015/service-workers-iowa)
（杰夫·波斯尼克 - 2015 年 10 月 1 日）

[我们现在如何完成它？](http://alistapart.com/column/how-do-we-get-it-done-now)
（莱扎·危险·加德纳 - 2015 年 9 月 30 日）

[Workers 的角色和离线缓存](https://unoyunodiez.wordpress.com/2015/08/23/modern-mobile-web-development-01/)
（2015 年 9 月 7 日）

[让离线 Web 应用程序变得安全！](http://sakurity.com/blog/2015/07/28/appcache.html)
（叶戈尔·霍马科夫 - 2015 年 7 月 28 日）

[Service Worker 会议亮点](https://blog.wanderview.com/blog/2015/07/28/service-worker-meeting-highlights/)
（本·凯利 - 2015 年 7 月 28 日）

[问答：Couchbase 表示，线下优先，而不仅仅是移动优先](http://www.cbronline.com/news/mobility/apps/qa-offline-first-not-just-mobile-first-says-couchbase-4609613)
（詹姆斯·纳恩斯 - 2015 年 6 月 26 日）

[为什么离线优先很重要，以及开发人员应该了解什么](https://logbook.hanno.co/offline-first-matters-developers-know/)
（马塞尔·卡尔维拉姆 - 2015 年 6 月 2 日）

[让 Appcache 的 Fallback 正常工作，跨浏览器](https://www.iandevlin.com/blog/2015/06/html5/getting-appcaches-fallback-to-work-crossbrowser)
（伊恩·德夫林 - 2015 年 6 月 1 日）

[移动应用离线支持](https://www.infoq.com/articles/mobile-apps-offline-support)
（古斯塔沃·马查多 - 2015 年 5 月 29 日）

[使react-europe.org与Service Workers一起离线工作并从Cloudflare获得免费SSL](https://medium.com/@patcito/making-react-europe-org-work-offline-with-service-workers-f54fb0457048)
（帕特里克·阿尔乔德 - 2015 年 5 月 14 日）

[Ionic 中的离线数据同步](https://frontmag.no/artikler/utvikling/offline-data-synchronization-ionic)
（马可·费尔南德斯 - 2015 年 4 月 29 日）

[浏览器中的离线数据](http://www.levvel.io/blog-post/offline-data-in-the-browser/)
（阿萨夫·温伯格 - 2015 年 3 月）

[离线：当您的应用程序无法连接到互联网时](https://uxdesign.cc/offline-93c2f8396124)
（丹尼尔·索伯 - 2015 年 3 月 29 日）

[离线不仅仅是另一个移动功能](http://betanews.com/2015/03/04/offline-is-not-just-another-mobile-feature/)
（查克·加纳帕蒂 - 2015 年 3 月 4 日）

[离线优先，快速，使用 sw-precache 模块](https://developers.google.com/web/updates/2015/02/offline-first-with-sw-precache)
（杰夫·波斯尼克 - 2015 年 2 月 23 日）

[离线不是一个功能](http://www.formotus.com/17221/blog-mobility/offline-is-not-a-feature)
（2015 年 2 月 16 日）

[让应用程序离线时的正确和错误策略](http://appdevelopermagazine.com/2356/2015/2/9/The-Right-and-Wrong-Strategies-When-Taking-Your-App-Offline/)
（马丁·海勒 - 2015 年 2 月 9 日）

[网络开发人员在经历了两周极其缓慢的互联网之后的三个要点](https://byrslf.co/third-takeaways-for-web-developers-after-two-weeks-of-painously-slow-internet-9e7f6d47726e)
（加博·莱纳德 - 2015 年 1 月 25 日）

[离线优先：就像拔掉并播放一样简单？](http://www.ae.be/blog-en/offline-first-simple-unplug-play/)
（托马斯·安西奥 - 2015 年 1 月 15 日）

[一个简单的ServiceWorker应用程序](http://blog.lamplightdev.com/2015/01/06/A-Simple-ServiceWorker-App/)
（克里斯·海恩斯 - 2015 年 1 月 6 日）

[ServiceWorker 在 Chrome 40 beta 中可用](https://plus.google.com/+IlyaGrigorik/posts/WPZsWr4QGqR)
（伊利亚·格里戈里克 - 2014 年 12 月 11 日）

[PSA：服务工作者来了](http://infrequently.org/2014/12/psa-service-workers-are-coming/)
（亚历克斯·拉塞尔 - 2014 年 12 月 11 日）

[离线食谱](https://jakearchibald.com/2014/offline-cookbook/)
（杰克·阿奇博尔德 - 2014 年 12 月 9 日）

[网络上的下一个用户体验挑战：获得离线信任](https://www.christianheilmann.com/2014/12/08/the-next-ux-challenge-on-the-web-gaining-offline-trust/)
（克里斯蒂安·海尔曼 - 2014 年 12 月 8 日）

[Service Worker 食谱](https://github.com/GoogleChrome/samples/tree/gh-pages/service-worker)
（塞萨尔·威廉·阿尔瓦伦加 - 2014 年 12 月 8 日）

[Service Worker 简介](https://developers.google.com/web/fundamentals/getting-started/primers/service-workers)
（马特·冈特 - 2014 年 12 月 1 日）

[浏览器中离线去中心化单点登录](http://substack.net/offline_decentralized_single_sign_on_in_the_browser)
（詹姆斯“substack”哈利迪 - 2014 年 11 月 27 日）

[带有 Meteor 的离线网络应用程序](https://subvisual.co/blog/posts/45-offline-web-apps-with-meteor)
（加布里埃尔·波卡，2014 年 11 月 26 日）

[如何使用 PouchDB 构建可以离线工作的 Web 应用程序？](http://www.theodo.fr/blog/2014/11/how-to-build-web-applications-work-offline-pouchdb/)
（扬·雅克 - 2014 年 11 月 25 日）

[让您的应用程序离线工作：提示和警示故事](https://quickleft.com/blog/making-your-app-work-offline-tips-and-cautionary-tales/)
（大卫·阿拉贡 - 2014 年 11 月 11 日）

[Google 和 Mozilla 的目标是如何让网络应用程序在离线状态下大放异彩](http://www.techrepublic.com/article/how-google-and-mozilla-are-aiming-to-make-web-apps-work-as-well-offline-as-on/)
（尼克·希思 - 2014 年 10 月 30 日）

[线下优先就是以人为本](https://nolanlawson.com/2014/10/03/offline-first-is-people-first/)
（诺兰·劳森 - 2014 年 10 月 3 日）

[Hoodie 简介：面向前端开发人员的全栈应用程序开发](https://www.toptal.com/front-end/introducing-hoodie-full-stack-app-development-for-front-end-developers)
（阿尔瓦罗·奥利维拉 - 2014 年 9 月 24 日）

[离线优先：网络开发的新范例](ttps://translate.google.com/translate?hl=en&sl=nl&tl=en&u=http%3A%2F%2Fwww.e-sites.nl%2Fblog%2F400-offline-first-een-nieuw-paradigma-in-web-development.html)
（博耶·奥门斯 - 2014 年 9 月 16 日）

[使用 IndexedDB 和 WebSQL 构建简单的跨浏览器离线待办事项列表](https://www.smashingmagazine.com/2014/09/building-simple-cross-browser-offline-todo-list-indexeddb-websql/)
（马特·安德鲁斯 - 2014 年 9 月 2 日）

[MakeDrive简介](http://blog.humphd.org/introducing-makedrive/)
（大卫·汉弗莱 - 2014 年 8 月 25 日）

[使用 AngularJs 正确完成 Worklight 身份验证](https://medium.com/@papasimons/worklight-authentication-done-right-with-angularjs-768aa933329c)
（吉迪恩·西蒙斯 - 2014 年 8 月 22 日）

[使您的 Worklight 应用程序脱机](https://medium.com/@papasimons/take-your-worklight-apps-offline-e8c2c2d8533a)
（吉迪恩·西蒙斯 - 2014 年 8 月 19 日）

[离线工作](https://developer.mozilla.org/en-US/Apps/Fundamentals/Offline)
（2014 年 8 月 12 日）

[离线优先 - 海王星风格的 Web 开发新范例](http://scn.sap.com/community/developer-center/front-end/blog/2014/08/05/offline-first--the-new-paradigm-in-web-development-done-neptune-style) (Njål Stabell - 2014 年 8 月 5 日)

[突破性发展：离线优先是新的移动优先](http://www.lukew.com/ff/entry.asp?1902)
（卢克·弗罗布莱夫斯基 - 2014 年 7 月 29 日）

[离线模式](https://www.ibm.com/developerworks/community/blogs/worklight/entry/offline_patterns?lang=en)
（卡洛斯·安德鲁 - 2014 年 7 月 3 日）

[离线 Web 应用、Web 存储、IndexedDB、AppCache、文件 API 期货](https://www.youtube.com/watch?v=pklpK55uQmE&feature=youtu.be)
（阿里·阿拉巴斯 - 2014 年 5 月 21 日）

[Service Workers：现在离线（ish）！](https://www.youtube.com/watch?v=BKD7ZLRi9HI)
（亚历克斯·拉塞尔 - 2014 年 5 月 21 日）

[Service Worker - 初稿已发布](https://jakearchibald.com/2014/service-worker-first-draft/)
（杰克·阿奇博尔德 - 2014 年 5 月 8 日）

[BMEAN 堆栈和离线优先设计](http://dailyjs.com/2014/04/10/bmean/)
（加藤大师 - 2014 年 4 月 11 日）

[HTML5应用程序必须一直在线吗？](https://www.christianheilmann.com/2014/03/23/do-html5-apps-have-to-be-online-all-the-time/)
（克里斯蒂安·海尔曼 - 2014 年 3 月 23 日）

[使用 PouchDB 构建离线优先应用程序](https://www.sitepoint.com/building-offline-first-app-pouchdb/)
（蒂芙尼·布朗 - 2014 年 3 月 10 日）

[Kindle Fire 上的离线 Web 应用程序简介](https://developer.amazon.com/public/community/post/Tx21KG2QC7O71S9/Introduction-to-Offline-Web-Apps-on-the-Kindle-Fire.html)
（拉塞尔·贝蒂 - 2014 年 1 月 30 日）

[设计离线优先的 Web 应用程序](http://alistapart.com/article/offline-first)
（亚历克斯·费耶克 - 2013 年 12 月 4 日）

[线下优先：从原生经验中学习](https://medium.com/@dalmaer/offline-first-learning-from-native-experiences-4a778ce8a445)
（迪翁·阿尔玛尔 - 2013 年 12 月 4 日）

[离线优先](http://www.kryogenix.org/days/2013/11/06/offline-first/)
（斯图尔特·兰格里奇 - 2013 年 11 月 6 日）

[首先让网络离线工作](http://marcelkalveram.com/2013/11/developing-for-offline-first/)
（马塞尔·卡尔维拉姆 - 2013 年 11 月 20 日）

[先向离线打个招呼](http://hood.ie/blog/say-hello-to-offline-first.html)
（丹·拉什 - 2013 年 11 月 5 日）

[离线优先：您的下一个渐进增强技术？](https://www.sitepoint.com/offline-first-next-progressive-enhancement-technique/)
（克雷格·巴克勒 - 2013 年 10 月 30 日）

[Appcache，与其说是一个混蛋，不如说是 #$%^ 中的一个彻底的痛苦](http://www.webdirections.org/blog/appcache-not-so-much-a-douchebag-as-a-complete-pain-in-the/)
（约翰·奥尔索普 - 2013 年 7 月 19 日）

[在单页应用程序中使用 HTML5 AppCache](https://techblog.dorogin.com/2013/03/using-html5-appcache-with-single-page-apps.html)
（谢尔盖·多罗金 - 2013 年 3 月 29 日）

[应用程序缓存是个混蛋](http://alistapart.com/article/application-cache-is-a-douchebag)
（杰克·阿奇博尔德 - 2012 年 5 月 8 日）

[Appcache 事实](http://mmariani.github.io/appcachefacts/)

[Chrome 离线应用程序](https://developer.chrome.com/apps/offline_apps)

[离线支持很有价值，而且以后无法添加](http://aanandprasad.com/articles/offline/)
（阿南德·普拉萨德 - 2011 年 8 月 13 日）

[离线优先网络应用程序设计](https://unhosted.org/practice/29/Offline-first-web-app-design.html)
（米契尔·B·德容 - 2011）

[没有杀手级离线 Web 应用程序的 5 个原因](https://www.sitepoint.com/killer-offline-web-applications/)
（克雷格·巴克勒 - 2010 年 2 月 16 日

[离线网络应用程序](https://hacks.mozilla.org/2010/01/offline-web-applications/)
（保罗·鲁热 - 2010 年 1 月 7 日）

[让我们离线](http://diveintohtml5.info/offline.html)
（马克·朝圣者）


## 演讲

### 视频

[Offline First Web 应用程序简介](https://www.youtube.com/watch?v=2zyAX9J8Diw)
（马克斯·格费勒 - 2022 年 5 月 30 日）

[设计 24/7 使用：离线优先移动应用程序开发](https://www.mendix.com/videos/designing-for-24-7-use-offline-first-mobile-app-development/)
（丹尼·罗斯特 - 2020 年 10 月 1 日）

[静态网站离线优先](https://www.youtube.com/watch?v=_kJMjJ1tm6o)
（杰夫·波斯尼克 - 2017 年 1 月 30 日）

[Service Worker 和 Web 应用](http://www.thedotpost.com/2016/12/nolan-lawson-service-worker-and-the-appification-of-the-web)
（诺兰·劳森 - 2016 年 12 月 5 日）

[未来应用模型：高级 Service Worker](https://www.youtube.com/watch?v=J2dOTKBoTL4)
（杰克·阿奇博尔德 - 2016 年 11 月 11 日）

[离线是新的黑色](https://vimeo.com/171317290)
（马克斯·斯托伊伯 - 2016 年 6 月 19 日）

[Facebook 和 Flipkart 大规模服务人员](https://www.youtube.com/watch?v=fGTUIlEM0m8&feature=youtu.be&t=2200)
（欧文·坎贝尔-摩尔、Aditya Punjani 和 Nate Schloss - 2016 年 5 月 20 日）

[即时加载：构建离线优先的渐进式 Web 应用程序](https://www.youtube.com/watch?v=cmGr0RszHc8)
（杰克·阿奇博尔德 - 2016 年 5 月 20 日）

[离线优先 – 好的部分](https://www.youtube.com/watch?v=NEferkZOGV4&feature=youtu.be)
（格雷戈尔·马丁努斯 - 2016 年 5 月 12 日）

[离线Web应用程序：使用IndexedDB和Service Worker](https://www.udacity.com/course/offline-web-applications--ud899)

[完全工具提示：离线支持](https://www.youtube.com/watch?v=OBfLvqA_E4A)
（阿迪·奥斯马尼和马特·冈特 - 2016 年 4 月 27 日）

[在 Ember 中使用 Service Workers](http://confreaks.tv/videos/emberconf2016-using-service-workers-in-ember)
（约翰·克莱因施密特 - 2016 年 3 月 29 日）

[使用 PouchDB 的离线优先应用程序](https://www.youtube.com/watch?v=7L7esHWAjSU)
（布拉德利·霍尔特 - 2015 年 12 月 11 日）

[工作人员即服务](https://www.youtube.com/watch?v=5LAMbIlwilc)
（奥拉·加西德洛 - 2015 年 11 月 19 日）

[使您的 Web 应用程序离线](https://www.youtube.com/watch?v=EZF1EfjQlbo)
（迈克·尼奇 - 2015 年 11 月 16 日）

[您的浏览器中有一个客户端代理（ServiceWorker）！](https://www.youtube.com/watch?v=etACK2qbHfc)
（伊利亚·格里戈里克 - 2015 年 11 月 16 日）

[OnConnectionLost：离线 Web 应用程序的生命周期](https://www.youtube.com/watch?v=rw8Q9ZLDkEs)
（斯蒂芬妮·格雷维尼格 - 2015 年 10 月 12 日）

[离线优先和服务工作者](https://www.youtube.com/watch?v=TGwjgmAqNRo)
（马克西米利安·斯托伊伯 - 2015 年 10 月 5 日）

[离线第一播客](https://www.youtube.com/watch?v=tilH8jgLrXQ)
（网络平台播客 - 2015 年 9 月 8 日）

[曾经与未来的网络](https://www.youtube.com/watch?v=RQQNNP8tFro)
（杰克·阿奇博尔德 - 2015 年 7 月 28 日）

[离线](https://www.youtube.com/watch?v=BucGrYACJdQ)
（罗布·多德森 - 2015 年 6 月 29 日）

[让 Ember 离线](https://www.youtube.com/watch?t=20&v=VhZS4n2DMyU)
（约翰·克莱因施密特 - 2015 年 6 月 16 日）

[神圣同步](https://www.youtube.com/watch?v=Yp1h3cd8dsg)
（尤金尼奥·马莱蒂 - 2015 年 5 月 5 日）

[通过 Service Workers 减少线下的麻烦](https://www.youtube.com/watch?v=nqecpa6MtZ0)
（布雷特·利特尔 - 2015 年 3 月 28 日）

【先向离线打个招呼】(https://www.youtube.com/watch?v=ZsMS_sviJs0)
（奥拉·加西德洛 - 2015 年 3 月 26 日）

[离线优先的用户体验](https://vimeo.com/125479288)
（杰克·阿奇博尔德 - 2015 年 3 月 18 日）

[网络的未来是离线的](https://vimeo.com/120474703)
（约翰·奥尔索普 - 2015 年 2 月 24 日）

[使用 Backbone 构建离线优先应用程序](https://www.youtube.com/watch?v=Zb01eNS6-no)
（格雷戈尔·马丁努斯 - 2014 年 12 月 17 日）

[连接工作以离线创建](https://www.youtube.com/watch?v=fj49cSQ986k)
（克里斯蒂安·海尔曼 - 2014 年 11 月 24 日）

[ServiceWorker 来了，看起来很忙！](https://www.youtube.com/watch?v=Rr2vXDIVerI)
（杰克·阿奇博尔德 - 2014 年 9 月 21 日）

[网络的下一个挑战是我们](https://www.youtube.com/watch?v=QPRqQH_30hU&t=22m53s)
（克里斯蒂安·海尔曼 - 2014 年 8 月 1 日）

[离线优先](https://www.youtube.com/watch?v=dPz_5-MEvcg)
（亚历克斯·费耶克 - 2014 年 7 月 17 日）

[ServiceWorker：网络层是你的](https://www.youtube.com/watch?v=4uQMl7mFB6g)
（杰克·阿奇博尔德 - 2014 年 6 月 25 日）

[离线网络应用程序](https://www.youtube.com/watch?v=AbixY3W8ayo)
（简·钟布姆 - 2014 年 5 月 23 日）

[离线网站](https://www.youtube.com/watch?v=nnLBdFLo2fc)
（戴尔·哈维 - 2014 年 6 月 20 日）

[将 NoSQL 带入您的手机](https://www.youtube.com/watch?v=qfC90DQEoeY)
（帕特里克·赫内斯 - 2013 年 12 月 16 日）

[网络连接：可选](https://www.youtube.com/watch?v=Z7sRMg0f5Hk)
（杰克·阿奇博尔德 - 2013 年 12 月 4 日）

[离线末日生存](https://www.youtube.com/watch?v=Qg75x08Mtcs)
（约翰·克莱因施密特 - 2014 年 11 月 29 日）

[离线优先](https://www.youtube.com/watch?v=7mdG-iAizVc)
（扬·莱纳德 - 2013 年 5 月 27 日）

[线下规则：《金融时报》的前沿网络标准](https://vimeo.com/64201695)
（安德鲁·贝茨 - 2013 年 4 月）

[将离线构建到 Web 应用程序中的正确方法是什么？](https://www.youtube.com/watch?v=Oic22dQMRXQ)
（杰克·阿奇博尔德、马克·克里斯蒂安、亚历克斯·拉塞尔和乔纳斯·希金 - 2013 年 2 月 9 日）

[AppCache：Douchebag](https://www.youtube.com/watch?v=cR-TP6jOSQM)
（杰克·阿奇博尔德 - 2013 年 1 月 20 日）

[应用程序缓存和本地存储](https://www.youtube.com/watch?v=ceODU6z4-yc)
（斯科特·戴维斯 - 2012 年 12 月 7 日）

[离线规则](https://www.youtube.com/watch?v=RrGo1Sz4IgQ)
（安德鲁·贝茨 - 2012 年 12 月 4 日）

[构建未来的网络应用程序。明天、今天和昨天。](https://www.youtube.com/watch?v=O3AukCYymEU)
（保罗·金兰 - 2012 年 11 月 12 日）

[使 Web 应用程序离线](https://www.youtube.com/watch?v=ejcJmeewtd4)
（凯文·马克曼 - 2012 年 11 月 5 日）

[使用 HTML5 构建离线 Web 应用程序](https://www.youtube.com/watch?v=W41mvarupH0)
（乔纳森·斯塔克 - 2012 年 7 月 25 日）

[下线（线路）：离线工作的 HTML5 应用程序的 appcache、localStorage](https://www.youtube.com/watch?v=dN8e-QdYyCk)
（约翰·奥尔索普 - 2012 年 7 月 3 日）

### 幻灯片

[离线、渐进式、多线程](https://nolanlawson.github.io/fronteers-2016/#/)
（诺兰·劳森 - 2016 年 10 月 10 日）

[网络工作者的崛起](http://blog.nparashuram.com/2016/09/rise-of-web-workers-nationjs.html)
（Parashuram N - 2016 年 9 月 16 日）

[为 theguardian.com 构建离线页面](https://speakerdeck.com/oliverjash/building-an-offline-page-for-theguardian-dot-com-jsconf-budapest-may-2016)
（奥利弗·约瑟夫·阿什 - 2016 年 5 月 14 日）

[与 Service Worker 一起离线](https://docs.google.com/presentation/d/1crh5m2aDdZPAL07Zo1FtuAliwwghW6FMOEtXviA_BZo/edit#slide=id.p)
（伊曼纽尔·克鲁格 - 2016）

[为 theguardian.com 构建离线页面](https://speakerdeck.com/oliverjash/building-an-offline-page-for-theguardian-dot-com-london-web-perf-march-2016)
（奥利弗·约瑟夫·阿什 - 2016 年 3 月）

[使用 Service Workers 和早期刷新实现超快渲染](https://speakerdeck.com/mstuart/service-workers-and-early-flushing)
（马克·斯图尔特 - 2015 年 12 月 14 日）

[Node.js Interactive 上使用 PouchDB 的离线优先应用程序](https://speakerdeck.com/bradleyholt/offline-first-apps-with-pouchdb-at-node-dot-js-interactive)
（布拉德利·霍尔特 - 2015 年 12 月 9 日）

[开发离线优先移动体验](http://www.slideshare.net/NicRaboy/developing-for-offline-first-mobile-experiences)
（尼克·拉博伊 - 2015 年 12 月 2 日）

【竭诚为您服务！ - 不仅仅是应用程序缓存用于 Service Workers](http://delapuente.github.io/presentations/at-your-service/index.html)
（萨尔瓦多·德拉普恩特·冈萨雷斯 - 2015 年 10 月 21 日）

[离线优先（Web）应用程序](https://speakerdeck.com/espylaub/offline-first-web-apps-beuth-hochschule-berlin)
（亚历克斯·费耶克 - 2015 年 10 月 20 日）

[离线优先 Web 应用程序](https://docs.google.com/presentation/d/1gDGIyGtXMSmtT8WsyXj7ADyUjNV679T1BF5QGEKqooc/mobilepresent)
（彼得·穆勒 - 2015）

[客户端中的服务器 - Service Workers 的崛起](http://slides.com/flaki/server-in-the-client#/)
（Szmozsánszky István - 2015 年 10 月 7 日）

[离线优先 Web 应用程序](https://docs.google.com/presentation/d/1gDGIyGtXMSmtT8WsyXj7ADyUjNV679T1BF5QGEKqooc/mobilepresent?slide=id.gb7f243163_0_53)
（彼得·穆勒 - 2015 年 6 月 27 日）

[使用 PouchDB、IBM Cloudant 和 IBM Bluemix 的离线优先移动 Web 应用程序](http://www.slideshare.net/IBMBluemix/offlinefirst-mobile-web-apps-with-pouchdb-ibm-cloudant-and-ibm-bluemix)
（布拉德利·霍尔特 - 2015 年 6 月 22 日）

[使用 PouchDB 构建支持离线的应用程序](https://speakerdeck.com/bradleyholt/building-offline-enabled-apps-with-pouchdb-at-php-tek-2015)
（布拉德利·霍尔特 - 2015 年 5 月 20 日）

[赤裸害怕离线移动](http://www.slideshare.net/ColdFusionConference/naked-and-afraid-48288396)
（马特·伍德沃德 - 2015 年 5 月 18 日）

[离线优先，无痛方式](http://de.slideshare.net/MarcelKalveram/offline-first-the-painless-way)
（马塞尔·卡尔维拉姆 - 2015 年 5 月 17 日）

[noBackend e 离线优先：专注于创造体验 (pt-br)](https://speakerdeck.com/joselitojunior1/nobackend-e-offline-first-foque-em-criar-experiencias-number-frontinfortaleza)
（小何塞 - 2015 年 5 月 16 日）

[HOLY SYNC：离线优先跨平台数据同步的明智方法](https://speakerdeck.com/takhion/holy-sync-a-sane-approach-to-offline-first-cross-platform-data-syncing)
（尤金尼奥·马莱蒂 - 2015 年 4 月 10 日）

[Service Worker 和离线 Web](https://slidr.io/lewiscowper/service-worker-and-the-offline-web-lightning-talk)
（刘易斯·考珀 - 2015 年 3 月 7 日）

[服务人员休假...](https://docs.google.com/presentation/d/1LUuMYDi1ssmslQKnnX3cwrdLVy2YCqyww3PBtqEP0q8/edit)
（娜塔莎·鲁尼 - 2015 年 3 月 6 日）

[TGIF - 离线优先](http://codekult.github.io/tgif-offline-first/)
（迭戈·卡尔德龙 - 2015 年 1 月 30 日）

[ServiceWorkers 和高性能离线应用程序](https://huffduffer.com/AlanDalton/202718)
（艾伦道尔顿 - 2015 年 1 月 13 日）

[利用 hood.ie 构建离线状态](http://de.slideshare.net/MarcelKalveram/codemotion-talk-41932602)
（马塞尔·卡尔维拉姆 - 2014 年 11 月 24 日）

[让 Drupal 离线！](http://www.slideshare.net/dickolsson/lets-take-drupal-offline-41650712)
（迪克·奥尔森 - 2014 年 11 月 17 日）

[离线优先网络应用程序 - Velocity EU 2014](http://www.slideshare.net/andrewsmatt/velocity-eu-2014)
（马特·安德鲁斯 - 2014 年 11 月 17 日）

[发现 ServiceWorker](http://www.slideshare.net/sandropaganotti/discover-serviceworker)
（桑德罗·帕加诺蒂 - 2014 年 11 月 16 日）

[先离线<3](https://speakerdeck.com/zoepage/ayb14-offline-first-1)
（奥拉·加西德洛 - 2014 年 10 月 17 日）

[缩小：离线第一个故事](https://speakerdeck.com/wohali/scaling-down-the-offline-first-story)
（琼·图泽 - 2014 年 9 月 16 日）

[网络离线状态](https://www.infoq.com/presentations/status-web-offline)
（草兰·麦克马洪 - 2014 年 8 月 21 日）

[看马，没有联系！使用 HTML5 构建支持离线的 Web 应用程序](https://www.infoq.com/presentations/html5-offline-storage)
（Bijan Vaez - 2014 年 8 月 1 日）

[先向离线打个招呼！](https://speakerdeck.com/zoepage/say-hello-to-offline-first)
（奥拉·加西德洛 - 2014 年 5 月 19 日）

[离线优先（Web）应用程序](https://speakerdeck.com/espylaub/offline-first-web-apps)
（亚历克斯·费耶克 - 2014 年 5 月 2 日）

[离线优先 – 变得简单！](https://speakerdeck.com/gr2m/offline-first-made-simple)
（格雷戈尔·马丁努斯 - 2014 年 4 月 24 日）

[离线首次重新想象现实世界的 Web 开发](https://qconlondon.com/london-2014/dl/qcon-london-2014/slides/CaolanMcMahon_OfflineFirstReImaginingWebDevelopmentForTheRealWorld.pdf)
（曹兰·麦克马洪 - 2014 年 3 月）

## 工具

[offline-plugin](https://github.com/NekR/offline-plugin/)：webpack 的离线插件（ServiceWorker、AppCache）。

[Pinterest Service Workers](https://github.com/pinterest/service-workers)：用于创建/测试/实验 Service Workers 的实用程序集合。

[Kinto](http://www.kinto-storage.org/)：在几秒钟内为您的 Web 应用程序添加同步和共享功能。

[bottle-service](https://github.com/bahmutov/bottle-service)：从 ServiceWorker 缓存恢复的即时 Web 应用程序。

[react-boilerplate](https://github.com/mxstbr/react-boilerplate)：快速设置面向性能、离线优先的 React.js 应用程序。

[Haywire](https://github.com/omnia-salud/haywire)：用于网络问题检测的最小 JavaScript 库。

[sw-toolbox](https://github.com/GoogleChrome/sw-toolbox)：服务工作者工具的集合。

[UpUp](https://www.talater.com/upup/)：离线优先库，旨在成为向站点添加离线功能的最简单方法。

[simple-serviceworker-tutorial](https://github.com/jakearchibald/simple-serviceworker-tutorial)：一个非常简单的 ServiceWorker 示例，旨在以交互式方式介绍 ServiceWorker。

[Hyperboot](https://github.com/substack/hyperboot)：离线 web 应用引导加载程序。

[MakeDrive](https://github.com/mozilla/makedrive)：相当于浏览器文件系统的基于云的 Dropbox®。设计用于与 Mozilla Webmaker 工具和服务配合使用。
请参阅 [Mozilla MakeDrive Wiki 页面](https://wiki.mozilla.org/Webmaker/MakeDrive) 了解背景信息。

[ApplicationCache](https://developer.mozilla.org/en-US/docs/Web/HTML/Using_the_application_cache)：HTML5 提供了一种应用程序缓存机制，允许基于 Web 的应用程序离线运行。

[IndexedDB](https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API)：IndexedDB 是一个 API，用于在客户端存储大量结构化数据，并使用索引对这些数据进行高性能搜索。

[ServiceWorkers](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API)：Service Worker 的作用类似于客户端上的代理。对于页面请求和页面发出的请求，您会收到一个 fetch 事件，您可以自己响应该事件，从而创建离线体验。

[localForage](https://github.com/localForage/localForage)：离线存储，改进。使用简单但功能强大的 API 包装 IndexedDB、WebSQL 或 localStorage。

[remoteStorage](https://remotestorage.io/)：支持 RemoteStorage 的应用程序会自动在所有设备（从台式机到平板电脑到智能手机，甚至电视）上同步您的数据。

[pouchdb](https://pouchdb.com/)：PouchDB 是一个受 Apache CouchDB 启发的开源 JavaScript 数据库，旨在在浏览器中良好运行。

[Offline.js](http://github.hubspot.com/offline/docs/welcome/)：一个很棒的 JavaScript 库，可以在用户失去连接时改善应用程序的体验。

[Hoodie](http://hood.ie/)：Hoodie 是一种离线优先且无后端的架构，适用于 Web 和 iOS 上的仅前端 Web 应用程序。

[离线状态](http://offlinestat.es/)：当我们没有互联网连接时显示应用程序。

[appCache Nanny](https://github.com/gr2m/appcache-nanny)：appCache 的 JavaScript API

[bro-fs](https://github.com/vitalets/bro-fs)：基于 [HTML5 Filesystem API](https://www.w3.org/TR/file-system-api/) 的基于 Promise 的包装器，允许在 Chrome 中使用沙盒文件系统。

[Orbit.js](http://orbitjs.com/)：用于编排数据源之间的访问、转换和同步的框架。

[workbox](https://github.com/GoogleChrome/workbox)：用于离线缓存的 JavaScript 库

[rxdb](https://github.com/pubkey/rxdb)


## 书籍

[离线第一本书](https://neighbourhood.ie/offline-first/book/)
（来自邻居）

[离线优先 Web 开发](https://www.packtpub.com/web-development/offline-first-web-development)
（丹尼尔·索伯）

[构建渐进式 Web 应用程序](http://shop.oreilly.com/product/0636920052067.do)
（塔尔·阿特摄）

[客户端数据存储](http://shop.oreilly.com/product/0636920043676.do)
（雷蒙德·卡姆登）

[离线第一：本书（草稿）](http://www.webdirections.org/offlineworkshop/ibooksDraft.pdf)
（约翰·奥尔索普）

[专业 HTML5 编程 - 第 12 章：创建 HTML5 离线 Web 应用程序](http://apress.jensimmons.com/v5/pro-html5-programming/ch12.html)
（彼得·吕伯斯、布莱恩·阿尔伯斯和弗兰克·萨利姆）

## 展示柜
[Minutes.io](https://minutes.io)：使用 [Hoodie](http://hood.ie/) 构建的很棒的离线第一分钟记录应用程序。

[2048](https://gabrielecirulli.github.io/2048/)：原版 2048 是一款适合固定在主屏幕上的精彩游戏。

[hospitalrun.io](http://hospitalrun.io/)：面向发展中国家医院的开源软件。

[pokedex.org](https://www.pokedex.org/)：神奇宝贝的索引，构建为客户端 JavaScript Web 应用程序。由 ServiceWorker、PouchDB、virtual-dom 和 Web Worker 提供支持。

[Soundslice](https://www.soundslice.com/)：使用[离线模式](https://www.soundslice.com/blog/29/introducing-soundslice-offline-mode/)通过交互式记谱更好地学习和教授音乐。

## 关注谁
- [Matthew Riley](https://github.com/tofumatt)：在 mozilla 工作，localForage（localstroage、IndexedDb 和 WebSQL Wrapper）的创建者
- [Jake Archibald](https://github.com/jakearchibald)：自称服务工作者狂热者，在谷歌工作，帮助离线网络应用程序成为现实。

## 贡献
随时欢迎分享、建议和贡献！如果您想做出贡献，我们强烈鼓励您这样做。请阅读[贡献指南](CONTRIBUTING.md)。

感谢所有[贡献者](https://github.com/pazguille/offline-first/graphs/contributors)。

## 维护者
- Guille Paz（前端 Web 开发人员和 Web 标准爱好者）
- 电子邮件：[guille87paz@gmail.com](mailto:guille87paz@gmail.com)
- Twitter：[@pazguille](https://twitter.com/pazguille)
- 网址：[https://pazguille.me/](https://pazguille.me/)


## 许可证
[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)
