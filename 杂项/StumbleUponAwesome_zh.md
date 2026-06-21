# <img src="extension/images/icon_128.png" width="45"align="left"> StumbleUponAwesome
一个*很棒的*互联网发现按钮，适合开发人员、技术和科学爱好者。

<img src="https://img.shields.io/chrome-web-store/users/dhfmgppomdaagdcbpccdfjpopgikcdge?color=%236F82EB&label=chrome%20users&labelColor=464646&style=flat-square&logo=google-chrome&logoColor=white"/> <img src="https://flat.badgen.net/amo/users/stumbleuponawesome?color=6F82EB&label=firefox%20users&icon=firefox"/> <img src="https://img.shields.io/chrome-web-store/v/dhfmgppomdaagdcbpccdfjpopgikcdge?color=E87676&label=version&style=flat-square" /> <img src="https://flat.badgen.net/github/license/basharovV/stumbleuponawesome?color=green" />
[![Mentioned in Awesome](https://awesome.re/mentioned-badge-flat.svg)](https://github.com/sindresorhus/awesome)

<p align="center">
  <img style="width: 100%;padding:0;margin:0;" src="header.png"/>
</p>

> 一个浏览器扩展程序，可将您从 [很棒的精选列表](https://github.com/sindresorhus/awesome) 之一带到随机站点。就像好的 ol' StumbleUpon （现在已经死了）。
<p align="center">
  <a href="https://chrome.google.com/webstore/detail/stumbleuponawesome/dhfmgppomdaagdcbpccdfjpopgikcdge?authuser=3"><b>⚡️ Install Chrome Extension</b></a>
  <a href="https://addons.mozilla.org/en-GB/firefox/addon/stumbleuponawesome/"><b>⚡️ Install Firefox Add-on</b></a>
</p>

Github 上有来自善良贡献者的 554 个精彩列表，其中包含 45,787 个独特的站点。那里有一些隐藏的宝石等待着。

----

## 使用方法：
**绊倒：** 只需点击 ⚡️ 扩展按钮 → 转到一个新的很棒的网站！

<small>（或使用 <kbd>**`Alt`**</kbd> + <kbd>**`Shift`**</kbd> +<kbd>**`S`**</kbd>）</small>

---

<img align="right" width="150" src="./rabbit-hole-icon.gif"/>

### ꩜ Introducing: The Rabbit Hole 

_We have all been down internet rabbit holes_. <br/>
.<br/>
One minute you're casually reading the news, the next you've read so much about `random topic` you might as well do a TED talk. <br/>
.<br/>
_What just happened?_ The rabbit hole pulled you in and you lost track of time, but you also might have discovered something _awesome_. <br/>
.<br/>
So why not embrace it, by having a fancy button for it, _obviously_. 

**Stay stumblin' on the same topic,** or exit back to random mode.<br/>

<p align="center">
  <img style="width: 100%;padding:0;margin:0;" src="rabbit-hole.gif"/>
</p>

---

### 设置

1. 克隆或分叉此存储库
2. 打开 Chrome/Brave 或其他基于 Chromium 的浏览器
3. 通过 `chrome://extensions` 打开扩展页面
4.启用开发者模式
5. 单击“加载解压”并选择`/extension`文件夹。

### 发展

以下是我想为此扩展构建的一些内容。然而，现在的主要任务就是尽可能地管理链接，添加更多数据源，并确保页面是有趣、有用、有趣和令人兴奋的良好组合。

- [ ] 好/坏链接的反馈机制
- [ ] 最喜欢的“宝石”到书签文件夹
- [ ] 基本统计数据
- [ ] 类别
- [x] [很棒的精选列表](https://github.com/sindresorhus/awesome)
- [ ] 技术、科学、软件、初创公司等。
- [x] 兔子洞功能（保持同一主题）。
- [x] 火狐支持
- [ ] Safari 支持

**[→ 变更日志](CHANGELOG.md)**


### 关于权限的注释
此扩展程序需要“<all_urls>”权限，以便在您访问的每个临时页面上显示覆盖 UI。它不会访问这些站点上的数据。没有任何类型的跟踪或分析，状态仅存储在本地。

### 感谢策展人✔
这个扩展是由出色的互联网策划者实现的：
- [sindresorhus/awesome](https://github.com/sindresorhus/awesome) 和 [所有精彩列表作者](https://github.com/sindresorhus/awesome/graphs/contributors)

### 关于数据集的注释
它完全是本地的 - 您可以在 [/extension/data](./extension/data) 下找到它。它是用 [awesome_scraper.py](./scraper/awesome_scraper.py) 生成的。

##### 保持质量
为了确保每个链接都有效且相关，数据集已被清理。任何失效或损坏的链接以及 CI 管道的链接、递归链接、捐赠链接等都会被删除。这是通过 [utils.py](./scraper/utils.py) 中的清理函数完成的。如果连接速度较慢，运行此脚本可能需要几个小时。

##### 损坏的链接
从数据集中删除后，每次抓取后，死链接或损坏链接（带有 404、SSL、其他服务器错误的链接）的记录都会保存在[这些文本文件](./extension/data/broken-urls) 中。

❗️如果您是很棒的列表维护者之一，请找到 **[您的很棒列表的文本文件](./extension/data/broken-urls)** 来检查死链接并将其从列表中删除，或使用有效的 URL 进行更新。如果文件为空，那就一切顺利！

#### 贡献

[☝️提交问题](https://github.com/basharovV/StumbleUponAwesome/issues/new)
[🤘提交 PR](https://github.com/basharovV/StumbleUponAwesome/pulls)

✨ 保持好奇心！
