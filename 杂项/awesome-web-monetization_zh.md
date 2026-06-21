<img src="assets/wm_icon_animated.svg" alt="Logo Web Monetization" align="right" width="120px" />

# Awesome Web Monetization [![Awesome](https://awesome.re/badge-flat2.svg)](https://awesome.re)

> Awesome stuffs about Web Monetization. Learn more, check modules and others tools.

**Web Monetization** is a web service that allows you to send money directly in your browser.
This is a JavaScript browser API that allows the creation of a payment stream from the user agent to the website

## Contents

- [About Web Monetization](#about-web-monetization)
- [How to start monetize my website](#how-to-start-monetize-my-website)
- [Resources](#resources)
  - [Packages](#packages)
  - [Tutorials](#tutorials)
  - [Articles](#articles)
  - [Newsletters](#newsletters)
  - [Tools](#tools)
  - [Community](#community)
- [Contribute](#contribute)
- [Donate](#donate)

## About Web Monetization

- [Webmonetization.org](https://webmonetization.org/)
- [Documentation](https://webmonetization.org/docs/)
- [How Web Monetization work for paying payments](https://webmonetization.org/docs/intro/sending-payments/)
- [How Web Monetization work for receiving payments](https://webmonetization.org/docs/intro/receiving-payments/)
- [Specifications](https://webmonetization.org/specification/)
- [ILP Forum (read only)](https://forum.interledger.org/)
- [Grant For The Web](https://www.grantfortheweb.org/)

---

- [Interledger : Open protocol suite for sending payments across different ledgers](https://interledger.org/)

## How to start monetize my website

If you would like to monetize your content, you must have a Wallet and Provider account. See below the platforms that allow you to use them.

<details><summary>More details about Wallet and Provider account</summary>
<p>

---

| **Wallets** |                                                                                             |                                                                                                                                                                                                         |     |
|:-----------:|:-------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:---:|
|    Name     | [![GateHub](https://webmonetization.org/img/logo-wallet-gatehub.svg)](https://gatehub.net/) | [New Wallet ?<br>Create a issue !](https://github.com/thomasbnt/awesome-web-monetization/issues/new?assignees=thomasbnt&labels=Wallet%2C+%E2%86%94+WM+repository&template=new-wallet.md&title=%5BWa%5D) |
|    Fees     |                   SEPA: 1.00 EUR < 50,000 EUR<br>Wire: $15 min ($150 max)                   |                                                                                                                                                                                                         |

| **Payments** |        |
|--------------|--------|
| Name         | Empty. |

---

</p>
</详情>

在您的网页上，在元数据上集成您的“货币化”标签

```html
<link rel="monetization" href="https://ilp.example.com/alice">
```

并检测“货币化”是否可行，然后开始工作

```js
if (document.monetization) {
  document.monetization.addEventListener("monetizationstart", () => {
    console.log(
      "🎉 Awesome ! You use Web Monetization.\nMore information https://webmonetization.org",
    );
  });
}
```

## 资源

### 套餐

_任何包/模块和插件_

- [monetize.js](https://github.com/sunchayn/monetize.js) - 用于管理和模拟网络货币化的事件驱动库。 ![](assets/small_icons/javascript.png)
- [types-wm](https://github.com/dacioromero/types-wm) - Web Monetization 的 TypeScript 定义 ![](assets/small_icons/typescript.png)
- [ngx-monetization (archived)](https://github.com/CDDelta/ngx-monetization) - Angular 的 Web 货币化 API。 ![](assets/small_icons/angular.png)
- [react-hook-wm](https://github.com/dacioromero/react-hook-wm) - 用于与 Web Monetization 集成的 React hooks。 ![](assets/small_icons/react.png)
- [react-monetize](https://github.com/guidovizoso/react-monetize) - 用于加速与 Web Monetization API 集成的帮助程序和挂钩。 ![](assets/small_icons/react.png)
- [ep_monetization](https://github.com/ISNIT0/ep_monetization) - 用于将支付指针元标记应用到 Etherpad 站点的插件。 ![](assets/small_icons/javascript.png)
- [wp-connect-coil](https://wordpress.org/plugins/wp-connect-coil/) - 用于将 Coil 支付指针元标记应用于 WordPress 网站的插件。 ![](assets/small_icons/wordpress.png)
- [xrptipbot-wordpress-widget](https://wordpress.org/plugins/widget-xrptipbot/) - 基于 XRPTIPBOT 的 WordPress Widget 嵌入代码来捐赠内容创建者。 ![](assets/small_icons/wordpress.png)
- [eleventy-plugin-monetization](https://github.com/DanCanetti/eleventy-plugin-monetization) - 一个 Eleventy 插件，用于通过帖子和网站内容获利。 ![](assets/small_icons/11ty.png)
- [web-monetization-components](https://github.com/philnash/web-monetization-components) - 您可以在网络货币化网站上使用的网络组件的集合。 ![](assets/small_icons/javascript.png)
- [revshare](https://github.com/kewbish/revshare) - 一个用于收益共享的 JS 库。 ![](assets/small_icons/javascript.png)
- [web-monetization-proxy](https://github.com/tcdowney/web-monetization-proxy) - 用于注入 Web Monetization 元标记的简单 Go 代理。 ![](assets/small_icons/go.png)
- [gridsome-plugin-monetization](https://github.com/Sergix/gridsome-plugin-monetization) - Gridsome 的网络货币化。 ![](assets/small_icons/gridsome.png)
- [vuepress-plugin-web-monetization](https://github.com/spekulatius/vuepress-plugin-web-monetization) - 将网络货币化元标记添加到您的 VuePress 网站。 ![](assets/small_icons/vuejs.png)
- [jekyll-web_monetization](https://github.com/philnash/jekyll-web_monetization) - 一个 Jekyll 插件，用于将 Web MonetizationAPI 支付指针添加到您的网站。 ![](assets/small_icons/jekyll.png)
- [Monetization](https://github.com/KNawm/monetization) - 围绕 Web Monetization API 的包装器，用于通过应用程序获利。 ![](assets/small_icons/dart.png)
- [react-webmonetization-meta](https://github.com/uchibeke/react-webmonetization-meta) - React 的网络货币化元标签管理器。 ![](assets/small_icons/react.png)
- [web-monetization-electron-app](https://github.com/Jasmin2895/web-monetization-electron-app) - 项目演示了在 Electron App 中启用网络货币化的基本设置。 ![](assets/small_icons/electron.png)
- [web-monetized-video](https://github.com/Jasmin2895/web-monetized-video) - 具有播放和付费政策的 Web 组件会根据观看的视频量向您收费。 ![](assets/small_icons/javascript.png)
- [web-monetization-polyfill](https://github.com/immers-space/web-monetization-polyfill/) - 确保 JavaScript Web Monetization API 可用，即使在启用了内容安全策略的环境中也是如此。 ![](assets/small_icons/javascript.png)
- [web-monetization-video-ads](https://www.npmjs.com/package/web-monetization-video-ads) - 将网络货币化与视频广告联系起来，以实现网络货币化的免费增值商业模式。 ![](assets/small_icons/javascript.png)
- [web-monetization-revenue-share](https://www.npmjs.com/package/web-monetization-revenue-share) - 通过智能合约将资金自动重新分配给社区。 ![](assets/small_icons/javascript.png)
- [awesome-jsgames](https://github.com/proyecto26/awesome-jsgames) - 精彩 JavaScript 游戏精选列表！[](assets/small_icons/javascript.png)
- [mediadisclosures](https://github.com/oofdere/mediadisclosures) - 一个开源、不断发展的通用内容评级系统。 ![](assets/small_icons/javascript.png)
- [web-monetization-demo](https://github.com/peter279k/web-monetization-demo) - 这是一个网络货币化演示！[](assets/small_icons/javascript.png)
- [money-chat](https://github.com/dfoderick/money-chat) - 网络货币化聊天应用程序！[](assets/small_icons/javascript.png)

### 教程

- [Getting started](https://webmonetization.org/docs/guides/monetize-page/) - 来自 webmonetization.org 的官方文档。
- [Exclusive content](https://webmonetization.org/docs/guides/provide-exclusive-content/) - 在您的网站上放置独家内容。
- ['A Web Monetization Story'](https://esse-dev.github.io/a-web-monetization-story/) - 面向在线创作者的基于故事的交互式网络货币化教程。
- [Web Monetization like I'm 5](https://dev.to/hacksultan/web-monetization-like-i-m-5-1418) - 网络货币化！

### 文章

- [Monetizing Content in View](https://dev.to/godwinagedah/monetizing-content-in-view-paying-for-what-you-see-462a) - 为你所看到的付费。
- [Web Components](https://dev.to/philnash/web-components-for-the-web-monetization-api-4ed9) - 用于 Web Monetization API（系列）。

### 时事通讯

- [Newsletter of grantfortheweb.org](https://www.grantfortheweb.org/signup) - 注册电子邮件更新。

### 工具

- [Probabilistic Revshare Generator - Web Monetization](https://webmonetization.org/prob-revshare/) - 概率收入分享（revshare）是在多个支付指针之间分享部分网络货币化页面收入的一种方式。

> 使用此工具定义支付指针及其权重的列表。
> 然后，将生成的获利链接元素添加到您的网站。
> 该链接将包含托管在 https://webmonetization.org/api/revshare/pay/ 上的唯一 URL。
> 如果您不想使用托管 URL，您可以通过向您的网站添加脚本来设置收益分成。

- [Is web monetized](https://github.com/jkga/is-web-monetized) - 一个非常简单的工具，用于检查是否启用了网络货币化。

> ```bash
> npm install is-web-monetized -g
> 货币化 example.com
  > ```
  >
> 您还可以使用依赖项测试您的网站。

- [Paytrackr](https://github.com/thomasbnt/paytrackr) - （从 [wobsoriano/paytrackr](https://github.com/wobsoriano) 分叉） - 在一个地方跟踪和管理您的小额支付。

> PayTrackr 是跟踪和管理网络货币化网站小额支付的最简单、最安全的方式，拥有网络货币化提供商会员资格。

- [Akita](https://github.com/esse-dev/akita) - 浏览器扩展程序可让您深入了解您对网络货币化的参与情况。

> 秋田展示您最常访问的盈利网站、您在这些网站上花费的时间以及您为这些网站做出的贡献（或可能做出的贡献）。

- [Open Monetization Wallet](https://github.com/kristianfreeman/openmonetizationwallet) - 用于管理虚荣网络货币化钱包的工具。

> 开放货币化钱包 (OMW) 使大规模接受 Web 货币化 API 付款变得更加容易。一些特点：
  >
> - 自定义钱包 URL：拥有您自己的“支付指针”，例如$wallet.signalnerve.com，而不是 $pay.stronghold.co/abcdef123
> - 在钱包/提供商之间进行更改，无需停机
> - 传入付款请求的日志
> - 多个钱包之间的收入共享，例如对于多个团队成员
> - 通过无服务器技术无限扩展
> - 免费和开源

### 社区

- [网络货币化社区](https://community.interledger.org/)
- [Twitter 上的@GrantForTheWeb](https://twitter.com/GrantForTheWeb)
- [DEV 上的网络货币化标签](https://dev.to/t/webmonetization)

---

## 贡献

欢迎投稿！首先阅读[贡献指南](contributing.md)。
您还可以与您的朋友分享此存储库和网络货币化。 😄

如果要添加新的小图标，高度必须为**16px**。放入`assets/small_icons/NAME.png`。仅接受 PNG 格式。

> **由 Netlify 提供支持** ✨

Netlify 为[网站](https://awesomewebmonetization.netlify.app/) 提供支持。感谢他们！ 💚

[![Deploys by Netlify](https://img.shields.io/badge/Netlify-00C7B7?style=for-the-badge&logo=netlify&logoColor=white)](https://netlify.com)

## 捐赠

请随时帮助[我](https://github.com/thomasbnt)维护这个项目！
感谢所有 **GitHub 上的赞助商**！

![GitHub Sponsors](https://cdn.jsdelivr.net/gh/thomasbnt/sponsors/sponsors.svg)

[![GitHub Sponsors](https://img.shields.io/badge/Sponsor%20me-%23EA54AE.svg?&style=for-the-badge&logo=github-sponsors&logoColor=white)](https://github.com/sponsors/thomasbnt) [![Support me on Buy Me a Coffee](https://img.shields.io/badge/Support%20me-on%20Buy%20Me%20a%20Coffee-white?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black&labelColor=%23FFDD00)](https://www.buymeacoffee.com/thomasbnt?via=thomasbnt)
