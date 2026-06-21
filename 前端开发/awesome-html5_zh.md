真棒 HTML5 [![真棒](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome) [![构建状态](https://api.travis-ci.org/diegocard/awesome-html5.svg?branch=master)](https://travis-ci.org/diegocard/awesome-html5)
=============

精彩 HTML5 资源的精选列表。受到 [awesome-php](https://github.com/ziadoz/awesome-php) 和 [awesome-python](https://github.com/vinta/awesome-python) 的启发

## 目录
- [文章和标准](#articles-and-standards)
- [多媒体功能](#multimedia-capabilities)
  - [Audio](#audio)
  - [媒体捕捉](#media-capture)
  - [画中画](#picture-in-picture)
  - [语音合成](#speech-synthesis)
  - [语音识别](#voice-recognition)
  - [虚拟现实（VR）](#virtual-reality)
  - [网页动画](#web-animations)
- [Elements](#elements)
  - [Canvas](#canvas)
  - [Head](#head)
  - [Sectioning](#sectioning)
  - [媒体元素](#media-elements)
  - [Forms](#forms)
  - [Time](#time)
  - [WebVTT](#webtt)
  - [HTML 导入](#html-imports)
- [开发API](#development-apis)
  - [Permissions](#permissions)
  - [Geolocation](#geolocation)
  - [Cryptography](#cryptography)
  - [File](#file)
  - [帧时序](#frame-timing)
  - [requestIdleCallback](#requestidlecallback)
  - [requestAnimationFrame](#requestanimationframe)
  - [网络支付](#web-payments)
- [Semantics](#semantics)
- [Accessibility](#accessibility)
- [DOM管理](#dom-management)
  - [影子 DOM](#shadow-dom)
  - [数据绑定](#data-binding)
  - [网络组件](#web-components)
- [渐进式网络应用程序](#progressive-web-apps)
  - [服务人员](#service-workers)
  - [离线缓存](#offline-caching)
  - [推送通知](#push-notifications)
- [客户端存储](#client-side-storage)
- [Performance](#performance)
- [Mobile](#mobile)
- [通信和互操作性](#communications-and-interoperability)
  - [网络套接字](#web-sockets)
  - [WebRTC](#webrtc)
- [网络工作者](#web-workers)
- [WebGL](#webgl)
- [浏览器兼容性](#browser-compatibility)
- [Books](#books)
- [游戏开发](#game-development)
- [Bootcamp](#bootcamp)
- [视频和主题演讲](#videos-and-keynotes)
- [网站和资源](#websites-and-resources)
  - [Websites](#websites)
  - [每周新闻](#weekly-news)
  - [Twitter](#twitter)
- [Contributing](#contributing)

## 文章和标准

* [HTML 5.3](https://w3c.github.io/html/) - 当前 HTML5 规范
* [渐进增强](https://www.smashingmagazine.com/2009/04/progressive-enhancement-what-it-is-and-how-to-use-it/)
* [可扩展网络宣言](https://extensiblewebmanifesto.org/)
* [W3C 中 HTML5 和 HTML4 之间的差异](https://www.w3.org/TR/html5-diff/)

## 多媒体功能

### 音频

* [网络音频 API 入门](https://www.html5rocks.com/en/tutorials/webaudio/intro/?redirect_from_locale=es)
* [MDN 上的 Web 音频 API](https://developer.mozilla.org/es/docs/Web_Audio_API)
* [使用 HTML5 制作吉他调音器](https://jonathan.bergknoff.com/journal/making-a-guitar-tuner-html5)
* [使用 Web Audio API 和 React 进行音频可视化](https://www.twilio.com/blog/audio-visualisation-web-audio-api--react)

### 媒体捕捉

* [在 HTML5 中捕获音频和视频](https://www.html5rocks.com/es/tutorials/getusermedia/intro/)
* [使用媒体捕获 API](https://www.sitepoint.com/using-the-media-capture-api/)

### 画中画

* [Chrome 的新画中画 API](https://developers.google.com/web/updates/2018/10/watch-video-using-picture-in-picture)

### 语音合成

* [HTML5 语音合成 API 简介](http://creative-punch.net/2014/10/intro-html5-speech-synthesis-api/)
* [另一个有用的介绍](https://shapeshed.com/html5-speech-recognition-api/)

### 语音识别

* [网络语音 API 演示](https://www.google.com/intl/en/chrome/demos/speech.html)
* [使用网络语音 API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Speech_API/Using_the_Web_Speech_API)
* [试验 Web Speech API](https://www.sitepoint.com/experimenting-web-speech-api/)
* [免费语音识别库（annyang）](https://www.talater.com/annyang/)

### 虚拟现实

* [Firefox Reality 现已推出](https://blog.mozilla.org/blog/2018/09/18/firefox-reality-now-available/)

### 网页动画

* [网页动画简介](http://danielcwilson.com/blog/2015/07/animations-intro/)
* [何时使用 Web 动画 API](http://danielcwilson.com/blog/2016/08/why-waapi/)

## 元素

### 帆布

* [W3 学校的简要说明](https://www.w3schools.com/tags/tag_canvas.asp)
* [来自 MDN 的教程](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Tutorial)
* [各种教程](https://www.html5canvastutorials.com/)
* [备忘单](https://simon.html5.org/dump/html5-canvas-cheat-sheet.html)

### 头

* [页面 HEAD 元素中的内容列表](https://gethead.info/)

### 切片

* [如何使用 HTML5 分段元素](https://blog.teamtreehouse.com/use-html5-sectioning-elements)

### 媒体元素

* 音频和视频
  - [来自 W3Schools 的音频标签](https://www.w3schools.com/tags/tag_audio.asp)
  - [来自 W3 学校的视频标签](https://www.w3schools.com/tags/tag_video.asp)
  - [来自 MDN 的教程](https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Video_and_audio_content)
  - [在 HTML5 中捕获音频和视频](https://www.html5rocks.com/en/tutorials/getusermedia/intro/)
* 嵌入标签
  - [W3 学校的简要说明](https://www.w3schools.com/tags/tag_embed.asp)
* 源标签
  - [W3 学校的简要说明](https://www.w3schools.com/tags/tag_source.asp)
* 轨道标签
  - [W3 学校的简要说明](https://www.w3schools.com/tags/tag_track.asp)

### 表格

* [MDN 对 HTML5 中表单的更改](https://developer.mozilla.org/en-US/docs/Learn/HTML/Forms)
* [HTML 表单](https://www.w3schools.com/html/html_forms.asp)

### 详情

* [如何使用详细信息和摘要元素](https://blog.teamtreehouse.com/use-details-summary-elements)
* [详细信息元素polyfill](https://www.smashingmagazine.com/2014/11/complete-polyfill-html5-details-element/)

### 时间

* [时间元素指南](https://www.sitepoint.com/html5-time-element-guide/)

### 网络VTT

* [W3C 的初稿](http://www.w3.org/TR/2014/WD-webvtt1-20141113/)

### HTML 导入

* [HTML 导入简介](https://www.webcomponents.org/community/articles/introduction-to-html-imports)

## 开发API

### 权限

* [Google 的 Web 权限 API](https://developers.google.com/web/updates/2015/04/permissions-api-for-the-web)

### 地理定位

* [使用地理定位](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation_API)
* [HTML5 应用程序：通过地理定位进行定位](https://code.tutsplus.com/tutorials/html5-apps-positioning-with-geolocation--mobile-456)

### 密码学

* [Web 加密 API 草案](http://www.w3.org/TR/WebCryptoAPI/)
* [Web 加密支持表](http://diafygi.github.io/webcrypto-examples/)
* [Window.crypto](https://developer.mozilla.org/en-US/docs/Web/API/Window/crypto)
* [W3C 密码学的下一步](http://www.w3.org/2012/webcrypto/webcrypto-next-workshop/report.html)

### 文件

* [使用 Web 应用程序 (MDN) 中的文件](https://developer.mozilla.org/en-US/docs/Web/API/File/Using_files_from_web_applications)
* [在JavaScript中读取本地文件](https://www.html5rocks.com/en/tutorials/file/dndfiles/)
* [文件 API 草案](https://w3c.github.io/FileAPI/)
* [文件系统API](http://www.w3.org/TR/file-system-api/)

### 帧时序

* [来自谷歌开发者的视频](https://www.youtube.com/watch?v=4zoC3eaa9z0)
* [W3C 草案](https://w3c.github.io/frame-timing/)

### 请求空闲回调

* [关于谷歌开发者](https://developers.google.com/web/updates/2015/08/using-requestidlecallback)

### 请求动画帧

* [使用 requestAnimationFrame（CSS 技巧）](https://css-tricks.com/using-requestanimationframe/)
* [保罗·爱尔兰写的很棒的文章](https://medium.com/@paul_irish/requestanimationframe-scheduling-for-nerds-9c57f7438ef4#.9gev5fdub)

### 网络支付

* [网络支付 API 概述](https://developers.google.com/web/fundamentals/payments/)

## 语义学

* [来自 W3Schools 的语义元素](https://www.w3schools.com/html/html5_semantic_elements.asp)
* [MDN 文档中 HTML5 的章节和大纲](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/Using_HTML_sections_and_outlines)
* [Smashing 杂志的 HTML5 语义](https://www.smashingmagazine.com/2011/11/html5-semantics/)
* [W3C 和 Opera 中鲜为人知的语义元素](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Advanced_text_formatting)

## 无障碍

* [从 Google 基础知识出发对可访问性进行了精彩介绍](https://developers.google.com/web/fundamentals/accessibility/)
* [Web 开发人员的辅助功能清单](https://webaim.org/standards/wcag/checklist)
* [来自 MDN 的 ARIA](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA)
* [出色的可访问性风格指南](https://a11y-style-guide.com/style-guide/)
* [针对认知差异进行设计](https://alistapart.com/article/designing-for-cognitive-differences)
* [有关屏幕阅读器如何支持 HTML 元素的指南](https://thepaciellogroup.github.io/AT-browser-tests/)
* [排名前 25 的网站可访问性测试工具](https://dynomapper.com/blog/27-accessibility-testing/246-top-25-awesome-accessibility-testing-tools-for-websites)
* [W3 的网页可访问性评估工具列表](http://www.w3.org/WAI/ER/tools/)
* [Pa11y - 自动可访问性测试](http://pa11y.org/)
* [HTML 中的咏叹调](https://developer.paciellogroup.com/blog/2014/10/aria-in-html-there-goes-the-neighborhood/)
* [易于访问且响应迅速的 HTML5 视频播放器](https://2017.ind.ie/blog/accessible-video-player/)

## DOM管理

### 影子 DOM

* [Shadow DOM v1：独立的 Web 组件](https://developers.google.com/web/fundamentals/web-components/shadowdom)
* [Shadow DOM v1 的新增功能（通过示例）](https://hayato.io/2016/shadowdomv1/)

### 数据绑定

* [使用 Object.observe() 进行数据绑定革命](https://www.html5rocks.com/en/tutorials/es7/observe/)

### 网络组件

* [自定义元素 v1：可重用的 Web 组件](https://developers.google.com/web/fundamentals/web-components/customelements)
* [Web 组件的力量](https://hacks.mozilla.org/2018/11/the-power-of-web-components/)
* [高分子项目](https://github.com/polymer)
* [聚合物快速介绍](https://www.webcomponents.org/community/articles/a-quick-polymer-introduction)
* [使用 Polymer 和 ES6 类构建 Web 组件](https://www.polymer-project.org/blog/es6)
* [揭秘 Web 组件](http://www.backalleycoder.com/2016/08/26/demythstifying-web-components/)
* [HTML 导入](https://www.html5rocks.com/en/tutorials/webcomponents/imports/)
* [使用 Yeoman 和 Polymer 构建 Web 应用程序](https://www.html5rocks.com/en/tutorials/webcomponents/yeoman/)

## 渐进式网络应用程序

* [PWA 简介](https://developers.google.com/web/progressive-web-apps/)
* [渐进式 Web 应用程序的详尽指南](https://www.smashingmagazine.com/2018/11/guide-pwa-progressive-web-applications/)
* [渐进式 Web 应用程序的商业案例](https://cloudfour.com/thinks/the-business-case-for-progressive-web-apps/)

### 服务人员

* [Service Worker 基础知识](https://developers.google.com/web/fundamentals/primers/service-workers/)
* [ServiceWorkies - 学习软件工程师玩游戏](https://serviceworkies.com/)
* [Service Worker 食谱](https://serviceworke.rs/)
* [与服务人员的离线内容](https://www.madebymike.com.au/writing/service-workers/)
* [培养服务工作者：案例研究（Smashing 杂志）](https://www.smashingmagazine.com/2016/02/making-a-service-worker/)
* [服务人员解释](https://github.com/w3c/ServiceWorker/blob/master/explainer.md)
* [Service Worker 库，完全工具提示](https://www.youtube.com/watch?v=IIRj8DftkqE)
* [ServiceWorker：Web 平台的革命](https://ponyfoo.com/articles/serviceworker-revolution)

### 离线缓存

* [离线食谱](https://developers.google.com/web/fundamentals/instant-and-offline/offline-cookbook/)
* [离线即时加载（Progressive Web App Summit 2016）](https://www.youtube.com/watch?v=qDJAz3IIq18)
* [渐进式 Web 应用程序的离线存储（作者：Addy Osmani）](https://medium.com/dev-channel/offline-storage-for-progressive-web-apps-70d52695513c#.jsbxgywzz)
* [使用应用程序缓存的初学者指南](https://www.html5rocks.com/en/tutorials/appcache/beginner/)

### 推送通知

* [网络推送通知（Google 的网络基础知识）](https://developers.google.com/web/fundamentals/push-notifications/)
* [推送 API W3C 草案](http://w3c.github.io/push-api/)
* [通知 API 规范](https://notifications.spec.whatwg.org/)

## 客户端存储

* [客户端存储](https://www.html5rocks.com/en/tutorials/offline/storage/)
* [离线食谱](https://jakearchibald.com/2014/offline-cookbook/)
* [IndexedDB简介](https://www.codemag.com/Article/1411041)
* [现实世界的离线数据存储](https://code.tutsplus.com/tutorials/real-world-off-line-data-storage--net-34063)
* [本地存储教程](https://developer.mozilla.org/en-US/docs/Archive/Add-ons/Overlay_Extensions/XUL_School/Local_Storage)

## 性能

* [加速移动页面 (AMP)](https://www.ampproject.org/learn/overview/)
* [谷歌开发者最佳实践](https://developers.google.com/speed/docs/insights/rules)
* [从 Google Web 基础知识优化性能](https://developers.google.com/web/fundamentals/performance/why-performance-matters/)
* [资源提示草案（预连接和预加载）](http://www.w3.org/TR/2014/WD-resource-hints-20141021/)
* [预取和预呈现](https://medium.com/@luisvieira_gmr/html5-prefetch-1e54f6dda15d)
* [图像压缩](https://www.html5rocks.com/en/tutorials/speed/img-compression/)
* [文本压缩](https://www.html5rocks.com/en/tutorials/speed/txt-compression/)
* [资源计时规范](http://www.w3.org/TR/resource-timing/)

## 手机

* [Web App Manifest（Google 的基础知识）](https://developers.google.com/web/fundamentals/web-app-manifest/)
* [Web 应用程序现场指南](https://www.html5rocks.com/webappfieldguide/toc/index/)
* [Apache Cordova 教程](http://ccoenraets.github.io/cordova-tutorial/)
* [从头开始的 PhoneGap](https://code.tutsplus.com/tutorials/phonegap-from-scratch-introduction--mobile-9171)
* [移动网络应用程序的最佳实践](https://www.html5rocks.com/en/tutorials/speed/quick/)
* [使用 Kendo UI 构建移动应用程序](https://docs.telerik.com/kendo-ui/controls/hybrid/introduction)
* [HTML5 振动 API](https://code.tutsplus.com/tutorials/html5-vibration-api--mobile-22585)
* [HTML5 电池状态 API](https://code.tutsplus.com/tutorials/html5-battery-status-api--mobile-22795)
* [HTML5电池状态API的隐私分析](https://eprint.iacr.org/2015/616.pdf)
* [HTML5 网络信息 API](https://code.tutsplus.com/tutorials/html5-network-information-api--cms-21598)
* [Sencha Touch 教程](https://docs.sencha.com/)

## 通信和互操作性

### 网络套接字

* [Websocket 简介](https://www.html5rocks.com/en/tutorials/websockets/basics/)
* [关于 HTML5 WebSocket](https://www.websocket.org/aboutwebsocket.html)
* [HTML5 Web 套接字 API](http://www.tutorialspark.com/html5/HTML5_WebSockets.php)

### 网络RTC

* [什么是 WebRTC 及其工作原理](https://www.innoarchitech.com/what-is-webrtc-and-how-does-it-work/)
* [WebRTC 变得简单](https://blog.carbonfive.com/2014/10/16/webrtc-made-simple/)
* [WebRTC数据通道教程](https://www.html5rocks.com/en/tutorials/webrtc/datachannels/)
* [来自 MDN 的 WebRTC 数据通道](https://developer.mozilla.org/en-US/docs/Games/Techniques/WebRTC_data_channels)

## 网络工作者

* [Web Worker 基础知识](https://www.html5rocks.com/en/tutorials/workers/basics/)
* [网络工作者的速度有多快？](https://hacks.mozilla.org/2015/07/how-fast-are-web-workers/)
* [MDN 中的 Web Worker](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Using_web_workers)
* [Web Worker 入门](https://code.tutsplus.com/tutorials/getting-started-with-web-workers--net-27667)

## 网页GL

* [WebGL 基础知识](https://www.html5rocks.com/en/tutorials/webgl/webgl_fundamentals/)

## 浏览器兼容性

* [我想用](http://www.iwanttouse.com/)
* [我可以用...](https://caniuse.com/)
* [W3C 质量工具](http://w3c.github.io/developers/tools/)
* [HTML5测试](http://beta.html5test.com/)
* [HTML5 演示](https://bestvpn.org/html5demos/)

## 书籍

* [深入研究 HTML5](http://diveinto.html5doctor.com/)
* [HTML5：启动并运行](https://www.amazon.com/HTML5-Running-Dive-Future-Development/dp/0596806027)
* [使用 HTML5 文件系统 API](http://shop.oreilly.com/product/0636920021360.do)
* [HTML5 游戏开发见解](https://www.apress.com/us/book/9781430266976)
* [网页设计游乐场：HTML 和 CSS 交互方式](https://www.manning.com/books/web-design-playground)

## 游戏开发

* [Mozilla Hacks 的 HTML5 游戏开发入门](https://hacks.mozilla.org/2013/09/getting-started-with-html5-game-development/)
* [Mozilla 的 HTML 5 游戏开发视频系列](https://hacks.mozilla.org/2016/02/html-5-game-development-video-series/)
* [信息、新闻和教程](http://html5gamedevelopment.com/)
* [超过 380 个有关 HTML5 游戏开发的资源](https://html5-game-development.zeef.com/andre.antonio.schmitz)
* 开源 JavaScript 游戏引擎
  - [Pixi.js](https://github.com/pixijs/pixi.js)
  - [Phaser](https://github.com/photonstorm/phaser)
  - [MelonJS](https://github.com/melonjs/melonJS)
  - [Kiwi.js](https://github.com/gamelab/kiwi.js)
  - [Crafty](https://github.com/craftyjs/Crafty)
  - [PhysicsJS](https://github.com/wellcaffeinated/PhysicsJS)
  - [Stage.js](https://github.com/shakiba/stage.js)
  - [Cocos2d](https://github.com/cocos2d/cocos2d-html5)

## 训练营
*[在线免费学习编码](https://www.freecodecamp.org/)
*[免费在线课程](https://www.khanacademy.org/)

## 视频和主题演讲

* [HTML5开发者大会](https://html5devconf.com/videos.html)
* [Polymer：声明式、封装式、可重用组件](https://www.youtube.com/watch?v=DH1vTVkqCDQ)
* [使移动网络变得快速、功能丰富且美观](https://www.youtube.com/watch?v=EXjPsvwIDwU)
* [Dart：未来的 HTML，就在今天！](https://www.youtube.com/watch?v=euCNWhs7ivQ)

## 网站和资源

### 网站

* [HTML官方参考](https://webplatform.github.io/docs/Main_Page/index.html)（允许像wiki一样协作修改内容）
* [HTML5 Rocks](https://www.html5rocks.com/en/)（新闻、教程和更新）
* [HTML5 Gallery](http://html5gallery.com/)（使用 HTML5 标记和 API 的网站展示）
* [MDN 的 HTML5 开发指南](https://developer.mozilla.org/en-US/docs/Learn/HTML)
* [2014 年 6 月 W3C 亮点](http://www.w3.org/2014/06/w3c-highlights/)
* [HTML5 Please](https://html5please.com/)（了解 HTML5 功能何时可以使用）
* [Keen HTML](https://keenhtml.com)（学习 HTML 的免费互动课程）
* [表元素的完整指南 ](https://css-tricks.com/complete-guide-table-element/)

### 每周新闻

* [HTML5周刊](https://frontendfoc.us/)
* [Mozilla 黑客每周文章](https://hacks.mozilla.org/category/mozilla-hacks-weekly/)
* [响应式设计通讯](http://responsivedesignweekly.com/)

### 推特

* [@html5](https://twitter.com/html5)
* [@html5rock](https://twitter.com/html5rock)
* [@html5gallery](https://twitter.com/html5gallery)
* [@html5doctor](https://twitter.com/html5doctor)
* [@GameDevHTML5](https://twitter.com/GameDevHTML5)
* [@mozhacks](https://twitter.com/mozhacks)
* [@googlechrome](https://twitter.com/googlechrome)

## 其他很棒的列表

* [awesome-awesomeness](https://github.com/bayandin/awesome-awesomeness)
* [lists](https://github.com/jnv/lists)
* [社区精选资源](https://hackr.io/tutorials/learn-html-5)

## 贡献

随时欢迎您的贡献！
