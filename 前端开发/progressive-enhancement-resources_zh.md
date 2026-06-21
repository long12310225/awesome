# 渐进增强资源 [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

有关渐进增强的全面资源集合。从概念和策略到特征检测和测试方法。包含（代码）示例列表。


## 内容

* [概念](#the-concept)
* [Strategies](#strategies)
* [特征检测](#feature-detection)
* [支持表](#support-tables)
* [测试方法](#testing-methods)
* [Examples](#examples)
* [相关文章](#related-articles)


## 概念

[渐进增强](https://en.wikipedia.org/wiki/Progressive_enhancement)是指在验证目标环境（例如浏览器）有能力后逐步改善用户体验。从内容开始，确保保持功能性和可访问性。

* [Progressive Enhancement: It's about the content](http://cognition.happycog.com/article/progressive-enhancement-its-about-the-content) - 共享内容是网络的核心。渐进增强确保对内容的访问。
* [The Role of Enhancement in Web Design](https://www.nngroup.com/articles/enhancement/) - 从增强的概念到丰富用户界面的标准和规则。
* [Understanding Progressive Enhancement](http://alistapart.com/article/understandingprogressiveenhancement) - 以智能方式层层应用技术，打造令人惊叹的体验。
* [Designing with Progressive Enhancement](https://www.filamentgroup.com/dwpe/) - *关于渐进增强的书*（400 多页）。
* [Adaptive Web Design](http://adaptivewebdesign.info/2nd-edition/) - 关于从内容到设计和交互的渐进增强的书籍。
* [Detecting (HTML5) features](http://diveinto.html5doctor.com/detect.html) - 通过示例和演示介绍不同的特征检测技术。
* [Progressive Web Apps](https://infrequently.org/2015/06/progressive-apps-escaping-tabs-without-losing-our-soul/) - 将网站增强为类似本机的应用程序（渐进式，而不是混合式）。


## 策略

您可以通过不同的方式应用渐进增强：

* [The Content-out Approach](https://articles.uie.com/progressive_enhancement/) - 提供对内容的广泛访问，不受技术限制。
* [Make the page usable with only HTML](https://www.gov.uk/service-manual/technology/using-progressive-enhancement#make-the-page-usable-with-only-html) - 这为每个设备和浏览器设定了基线。
* [Test Driven Progressive Enhancement](http://alistapart.com/article/testdriven) - 核心功能体验经过测试能力增强。
* [Cut the mustard](http://responsivenews.co.uk/post/18948466399/cutting-the-mustard) - 设置收集增强功能的阈值。
* [对组件进行评分，而不是对浏览器进行评分](https://www.filamentgroup.com/lab/grade-the-components.html
) - 组件级功能测试和增强。
* [Feature vs Browser vs Form factor detection](http://www.html5rocks.com/en/tutorials/detection/) - 作为调整您的应用程序以适应其环境的不同策略。
* [Server-side device detection](https://www.smashingmagazine.com/2014/07/server-side-device-detection-with-javascript/) - 使用用户代理和其他 HTTP 标头信息与设备数据库相结合来有条件地提供文件。
* [Writing polyfills](https://addyosmani.com/blog/writing-polyfills/) - 如果您的基线对于某些浏览器来说仍然太高，请考虑 [polyfills](https://remysharp.com/2010/10/08/what-is-a-polyfill)（又名 [回归增强](https://twitter.com/SlexAxton/status/25600963629)）。
* [Application Shell Architecture](https://medium.com/google-developers/instant-loading-web-apps-with-an-application-shell-architecture-7c0c2f10c73) - 设置即时加载网络应用程序。


## 特征检测

在尝试增强体验之前，您需要确保环境能够增强体验。您可以通过执行特征检测来测试这一点：

* [CSS 功能查询](https://www.sitepoint.com/an-introduction-to-css-supports-rule-feature-queries/) ([`CSS.supports()`](https://developer.mozilla.org/en/docs/Web/API/CSS/supports) & [`@supports()`](https://developer.mozilla.org/en-US/docs/Web/CSS/@supports)) - 本地测试是否特定 CSS使用 JS 方法或 CSS 声明来支持该功能。
* [Feature Detect ES6](https://www.npmjs.com/package/feature-detect-es6) - 检测哪些 ES2015 功能可用。
* [SVG requiredFeatures](https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/requiredFeatures) - 仅当 SVG 元素的“[requiredFeatures]”计算结果为 true 时才渲染它们。
* [Modernizr](https://modernizr.com/) - 广泛的功能检测套件（支持自定义构建）。
* [Feature.js](http://featurejs.com/) - 轻量级特征检测套件。
* [Conditioner.js](http://conditionerjs.com/) - 根据 HTML 属性中的指令有条件地加载 JS 模块。
* [EnhanceJS](https://www.filamentgroup.com/lab/introducing-enhancejs-smarter-safer-apply-progressive-enhancement.html) - 允许您在一组预定义的功能测试后异步加载 CSS 和 JS。


## 支持表

不同的环境（平台、浏览器、版本）具有不同的功能。支持表告诉您每个环境具有哪些功能。了解支持级别可以帮助您权衡增强功能与其实施的工作量和影响。

* [The Web Platform](https://platform.html5.org/) - 浏览器技术概述以及文档和测试套件的链接。
* [Can I use ...?](http://caniuse.com/) - 比较桌面和移动浏览器的功能实现和限制。
* [I want to use ...](http://www.iwanttouse.com/) - 找出浏览器对功能组合的支持。
* [HTML5 Test](http://html5test.com/) - 测试并比较跨浏览器的 HTML5 功能支持。
* [CSS3 Test](http://css3test.com/) - 对当前浏览器的 CSS3 功能支持进行细粒度测试。
* [Accessibility Support](https://a11ysupport.io/) - 比较跨浏览器和辅助技术对 HTML 元素和 ARIA 角色的可访问性支持。
* [State of Web Type](https://github.com/bramstein/stateofwebtype) - 支持网络上的类型和排版功能表。
* [Font Family Reunion](http://fontfamily.io/) - 默认本地（系统）字体的兼容性表。
* [HTML5 Accessibility](http://html5accessibility.com/) - 比较主要浏览器对 HTML5 标签、输入类型和属性的功能支持。
* [WAI-ARIA Screen reader compatibility](https://www.powermapper.com/tests/screen-readers/aria/) - ARIA 角色和属性支持不同的屏幕阅读器和浏览器组合。
* [What web can do today](https://whatwebcando.today/) - 列出并检查现代 Web API，例如对设备系统、传感器和执行器的访问。
* [HTML5 Worker test](https://nolanlawson.github.io/html5workertest/) - 比较跨浏览器的 Web Workers 和 Service Workers 支持哪些 API。
* [HTML5 Please](http://html5please.com/) - 通过建议和 Polyfill 链接探索功能。
* [API Catalog](https://developer.microsoft.com/en-us/microsoft-edge/platform/catalog/) - 让您可以比较主要桌面浏览器中 API 规范的实现。
* [Kangax's ECMAScript compatibility table](http://kangax.github.io/compat-table/) - 跨浏览器和其他运行时的 JavaScript 功能支持概述。
* [Node compatibility table](http://node.green/) - 跨 NodeJS 版本的 JavaScript 功能支持概述。
* [Is service worker ready?](https://jakearchibald.github.io/isserviceworkerready/) - 概述对渐进式 Web 应用程序背后的核心技术所涉及的所有功能的支持。
* [Is PWA ready?](https://ispwaready.toxicjohann.com/) - 概述对全球流行浏览器和许多中国浏览器的渐进式 Web 应用程序背后的核心和相关技术的支持。
* [Is WebRTC ready yet?](http://iswebrtcreadyyet.com/) - 实时通信背后对不同浏览器功能的支持概述。
* [Is WebVR ready?](https://iswebvrready.org/) - WebVR 背后对不同浏览器功能的支持概述，包括显示、游戏手柄、音频和语音 API。
* [Is Houdini ready yet?](https://ishoudinireadyyet.com/) - 跨浏览器对 Houdini（暴露部分 CSS 渲染引擎的低级 API）的支持概述。
* [Chrome 平台状态](https://www.chromestatus.com/features)
* [边缘平台状态](https://developer.microsoft.com/en-us/microsoft-edge/platform/status/)
* [火狐平台状态](https://platform-status.mozilla.org/)
* [Webkit 平台状态](https://webkit.org/status/) (Safari)
* [MDN Compatibility tables](https://developer.mozilla.org/en-US/docs/MDN/Contribute/Structures/Compatibility_tables) - MDN 的 Web 技术文档在每篇文章的末尾都有一个浏览器兼容性表。
* [MDN Browser Compat Data](https://github.com/mdn/browser-compat-data) - npm 模块为 MDN 兼容性表提供支持。
* [Device Bugs & Quirks](https://github.com/scottjehl/Device-Bugs) - 众包移动设备中奇怪的 HTML、CSS 和 JS 怪癖，您在其他支持表中找不到这些怪癖。
* [Can I Email?](https://www.caniemail.com/) - 支持电子邮件中的 HTML 和 CSS 表格。灵感来自[我可以使用吗](http://caniuse.com/)。
* [Project Fugu API tracker](https://fugu-tracker.web.app/) - 浏览器支持 Web API 填补“应用程序空白”的状态概述。
* [iOS PWA Compatibility](https://firt.dev/notes/pwa-ios/) - PWA 功能的支持表，包括服务工作人员、清单、后台同步和推送通知（非官方，由 Maximiliano Firtman 维护）。


## 测试方法

通过渐进增强，您可以支持不同环境中的不同体验。以下是测试所有这些变化的一些方法：

* [Open Device Lab](https://opendevicelab.com/) - 让您*在实际设备上手动测试*（免费）。
* [Text browsers](https://en.wikipedia.org/wiki/Text-based_web_browser) - 测试您的内容是否可以在基线上访问的好方法。例如尝试 [Lynx](http://lynx.browser.org/)。
* [Testing in Opera Mini](https://dev.opera.com/articles/making-sites-work-opera-mini/#testing-in-opera-mini) - 下载应用程序，在桌面上模拟，设置以测试本地网站。 （Opera Mini 占全球浏览器使用率的 5% 以上）
* [cURL](https://curl.haxx.se/docs/manual.html) - 用于查看页面预渲染源代码的网页。
* [Browserling](https://www.browserling.com/) - 允许您在 Windows 和 Android 平台上的不同版本浏览器中手动测试网页。
* [Run Internet Explorer using Virtual Machines](https://developer.microsoft.com/en-us/microsoft-edge/tools/vms/mac/) - 在其他平台上测试IE浏览器。
* [设备仿真器和模拟器](https://developers.google.com/web/tools/chrome-devtools/iterate/device-mode/testing-other-browsers?hl=en#device-emulators-and-simulators)
* [Configure *Desired Capabilities* in Selenium](https://github.com/SeleniumHQ/selenium/wiki/DesiredCapabilities) - 在不同场景中运行自动化浏览器测试。
* 使用 [BrowserStack](https://www.browserstack.com/)、[Saucelabs](https://saucelabs.com/) 或其他替代方案在不同浏览器中持续运行自动化测试。
* [Lighthouse](https://github.com/GoogleChrome/lighthouse) - 审核和测量渐进式 Web 应用程序的性能（通过 cli 或 [Chrome 扩展](https://chrome.google.com/webstore/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk)）。
* [渐进式增强清单（第 1 版，HTML）](http://adaptivewebdesign.info/1st-edition/read/chapter-6.html#the-progressive-enhancement-checklist)、[第 2 版清单 (PDF)](http://adaptivewebdesign.info/2nd-edition/checklist.pdf) - 可操作的列表，用于检查您是否已应用渐进式增强最佳实践。 [自适应网页设计书](http://adaptivewebdesign.info/) 的一部分。
* [CSS Feature Toggles](https://chrome.google.com/webstore/detail/css-feature-toggles/aeinmfddnniiloadoappmdnffcbffnjg) - Chrome DevTools 扩展可切换对选定 CSS 功能的支持，以测试渐进增强回退。


## 示例

### 自定义表单元素

* [Fancy radio buttons](https://www.sitepoint.com/replacing-radio-buttons-without-replacing-radio-buttons/) - 基于 HTML 单选按钮，使用 CSS 伪类和元素增强视觉效果。
* [Checkboxes & radio buttons](https://www.filamentgroup.com/dwpe/checkbox-radiobutton/) - 具有自定义焦点、悬停和选中状态。异步增强。
* [Toggle switch](https://ghinda.net/css-toggle-switch/) - 复选框或单选按钮，仅使用 CSS 在视觉上增强为滑动切换开关。
* [5-star rating](http://lea.verou.me/2011/08/accessible-star-rating-widget-with-pure-css/) - 基于 HTML 单选按钮，使用 CSS 伪类和元素增强视觉效果。
* [jQuery slider](https://github.com/filamentgroup/jQuery-Slider) - 基于标准 HTML 选择的可访问自定义滑块小部件。
* [jQuery custom file input](https://www.filamentgroup.com/lab/jquery-custom-file-input-book-designing-with-progressive-enhancement.html) - 文章和图书馆。
* [React isomorphic form](https://github.com/ghengeveld/react-isomorphic-form/) - 一组可以在服务器端预渲染和处理的 React 表单组件。它们在客户端得到增强而不会丢失状态。

### 数据可视化

* [Timeline](https://css-tricks.com/progressive-enhancement-data-visualizations/) - 从定义列表到 SVG 插图（带演示的文章）。
* [Charts](https://www.filamentgroup.com/lab/update-to-jquery-visualize-accessible-charts-with-html5-from-designing-with.html) - 使用 HTML5 画布（文章和库）从数据表到主题图表。

### 图片

* [Responsive Carousel](http://filamentgroup.github.io/responsive-carousel/test/functional/fade-auto.html) - 图像列表增强为响应式轮播，具有各种行为选项。
* [Lazy Progressive Enhancement](https://github.com/tvler/lazy-progressive-enhancement) - 在“<noscript>”标签内延迟加载图像。 （注意：仅限 Evergreen 浏览器）

### 菜单

* [Progressive hamburger menu](http://heydonworks.com/practical_aria_examples/#hamburger) - 页脚中的链接列表增强为画布外菜单。

### 页面导航

使用 ajax 和 `history.pushState` 在静态页面之间异步获取和转换：

* [Barba.js](http://barbajs.org/) - 添加带有事件挂钩、缓存和预取支持的页面转换。
* [SmoothState.js](https://github.com/miguel-perez/smoothState.js) - 添加带有事件挂钩、缓存和预取支持的页面转换。 （需要 jQuery）。
* [jquery-pjax](https://github.com/defunkt/jquery-pjax) - 添加页面转换并支持多个容器/内容槽（需要 jQuery）。
* [MoOx/pjax](https://github.com/MoOx/pjax) - 与 jquery-pjax 类似，但没有 jQuery 依赖。
* [Turbolinks](https://github.com/turbolinks/turbolinks) - 添加带有事件挂钩和缓存支持的页面转换。具有绑定到 iOS 和 Android 上的本机导航控件的适配器。


## 相关文章

* [Make the web work for everyone](https://hacks.mozilla.org/2016/07/make-the-web-work-for-everyone/) - 请开发人员考虑浏览器差异并构建一个有弹性的网络。
* [How many people are missing out on JavaScript enhancement?](https://gds.blog.gov.uk/2013/10/21/how-many-people-are-missing-out-on-javascript-enhancement/) - 研究为什么 1.1% 的页面访问中 JavaScript 未加载。

---

## 许可证

[![CC0](http://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

[Jasper Moelker](https://twitter.com/jbmoelker) 在法律允许的范围内放弃本作品在全球范围内根据版权法享有的所有权利，包括所有相关和邻接权。

您可以复制、修改、分发和执行该作品，甚至可以用于商业目的，而无需征求许可。
