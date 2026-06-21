# 很棒的 FOSS 应用程序 [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

> 按类别组织的精彩生产级免费和开源软件的精选列表。

此列表适用于那些正在寻找可分析和学习的高品质应用程序的开发人员。

*灵感来自 Sindre Sorhus 的 [awesome](https://github.com/sindresorhus/awesome)。*

## 总有机碳

- [Web 应用程序（仅限前端）](#web-apps-frontend-only)
- [Web 应用程序（全栈）](#web-apps-fullstack)
- [桌面应用程序](#desktop-apps)
- [移动应用程序](#mobile-apps)
- [Games](#games)


## Web 应用程序（仅限前端）
----

### 代码沙箱

* 反应、nginx、凤凰
* GNU 通用公共许可证

> Codesandbox 是一个在线 IDE，供 Web 开发人员使用 Vue、Preact、React 等现代 javascript 框架甚至普通 javascript 快速原型化和实现前端应用程序。

### 循环CI

* clojurescript、om、反应
* Eclipse 公共许可证

> CircleCI 提供持续集成和部署平台。前端是使用 clojurescript 的不可变数据结构构建的大型应用程序的一个令人印象深刻的示例。前端与 Pusher、Intercom、d3 和 google Analytics 集成，并且有一个通过实时事件、Websockets 和后端 API 服务器进行导航路由和通信的绝佳示例。它的测试套件不是那么广泛，但确实提供了如何使用 karma 测试 clojurescript/om 应用程序的一个很好的示例。

### 前体应用程序

* clojurescript、om、反应
* Eclipse 公共许可证

> Precursor 是一款高度交互的原型制作网络应用程序。它的前端是用 clojurescript 从头开始​​构建的。该项目有一个足够简单的路由和事件传递系统，以便新的 clojurescript 开发人员可以轻松了解 clojurescript 应用程序中的路由如何工作。它还充满了许多示例，说明如何构建基于组件的前端架构，该架构是交互式图形应用程序的一部分，即许多组件操纵 HTML5 画布或使用 HTML5 API。

### 卫报

* play2、scala、节点
* Apache 2.0 许可证

> Guardian 是一个新闻网站，具有订阅、登录、搜索、管理界面和一系列中间人 scala 应用程序，用于处理静态前端和后端 API 之间的通信。它非常快，并且有一个全面的测试套件以及如何优化大型传统网站速度的很好的例子。

### Web 应用程序（全栈）
----

### 幽灵

* 节点、快递、余烬
* 麻省理工学院许可证

> Ghost 为博主提供了一个简单的发布平台。该代码包含一个 emberjs 客户端和节点服务器后端，用于处理授权、角色管理、标记、博客发布、数据持久性以及您期望从优质博客平台获得的大多数功能。 Ghost 唯一不处理的是 i18n。它还包含一个全面的测试套件，其中包含针对整个 ember/node 堆栈的集成和单元测试。

### 亚特实验室

* 红宝石、Rails、coffescript、redis、sidekiq、
* 麻省理工学院许可证

> Gitlab 是一个代码协作工具。它被超过 100,000 个组织使用。它几乎拥有您在 Web 应用程序中所能想象到的一切：用户管理、用户角色、OAuth、i18n、许多专为与第三方集成而设计的模块、深度 git 集成以及使用 Sidekiq 的广泛异步任务系统。它有一个使用 cucumber 和 rspec 的示例测试套件。

### 话语

* 红宝石、Rails、Ember
* GPLv2 许可证

> Discourse 是一个讨论平台或网络论坛的现代版本。它有一个构建在 Rails 之上的非常模块化的系统，并包含如何在 Rails 应用程序中使用 Ember 构建交互式前端的很好的示例。它有一个管理界面，可以通过 Oauth 注册/登录 Google、Facebook、Twitter、Yahoo 和 Github。它具有广泛的国际化、实时通知、插件生态系统，经过 SEO 优化，专为平板电脑和移动设备设计。

### 红迪网

* python、pylons、node、react、rabbitmq、postgresql
* 通用公共归属许可版本 1.0

> Reddit 是一个发布网络上的新鲜和流行内容的新闻平台。它是用 python 构建的，并与许多第三方服务集成：rabbitmq、memcached、cassandra、solr 和 postgresql 等。该代码提供了大型 pylons 项目的一个很好的示例，并且在与许多其他服务集成的代码方面表现出色。

### 大河

* python3、django、coffeescript、角度
* GNU Affero 许可证

> Taiga 是一个项目管理工具。这是模块化架构的一个令人难以置信的例子。它的界面干净、设计精良、响应灵敏、速度快，用 python3 编写的现代后端代码是编写良好的 django 应用程序的一个很好的例子。它还具有广泛的测试套件，其中使用 pytest 进行集成和单元测试。


### 特拉维斯·西尔

* 红宝石、Rails、西纳特拉、RabbitMQ、Ember
* 麻省理工学院许可证

> Travis CI 是一个持续集成和部署系统。 Travis 的伟大之处在于它的模块化架构，这个大型分布式系统的每个组件都根据其主要功能进行划分。从工作人员管理、rails 后端、emberjs 前端到 yaml 配置解析器，每个都分为自己的存储库。

### 文件存储

* golang，反应
* AGPLv3 许可证

> Filestash 是一个基于 Web 的文件管理器，支持一系列协议和平台：FTP、SFTP、S3、Minio、Git、WebDAV、Backblaze、Dropbox、Google Drive、LDAP、CalDAV、CardDAV。

### 笔记

* golang、反应、打字稿
* GPLv3 许可证、AGPLv3 许可证

> Dnote 是一款免费开源命令行笔记软件，支持无限数量设备之间的可扩展数据同步，以及移动优先 Web 界面，也可以作为渐进式 Web 应用程序安装在移动设备上。

### 健康检查

* python、django、postgresql
* BSD 许可证

> Healthchecks 是一项 cron 作业监控服务。它侦听来自 cron 作业和计划任务（“检查”）的 HTTP 请求和电子邮件消息（“ping”）。当 ping 未按时到达时，Healthchecks 会发出警报。

## 桌面应用程序
----

### 搅拌机

* C、C++、Python
* GPLv2 许可证

> Blender 是一款可以在视觉上与 Maya 和 3DS Max 竞争的 3D 图形软件。最终产品是跨平台 3D Tooling 软件的一个令人惊叹的例子。这是一个非常成熟的项目，自 1994 年以来一直在开发。它有一个嵌入式 Python 脚本引擎、一个游戏逻辑引擎，并加载了 3D 操作、渲染和合成算法的实现。


### 原子

* 咖啡脚本、电子、节点
* 麻省理工学院许可证

> Atom 是一个可破解的文本编辑器。它构建在 Electron 之上，是将 libchromium、nodejs 和 Web 技术集成到跨平台可运行二进制文件中的一个很好的示例。它还包含电子应用程序的示例测试套件。

### 代托纳

* 去
* Apache 2.0 许可证

> Daytona 是一个极其简单的开源开发环境管理器。它自动化了设置开发环境的整个过程；配置实例、解释和应用配置、设置预构建、建立安全 VPN 连接、安全连接本地或 Web IDE，以及为开发环境分配完全限定的域名以方便共享和协作。

### 移动应用程序
----

*仍在寻找*

### 游戏
----

### 0广告

* C++、Python
* GPLv2 许可证

> 0 A.D是一款跨平台的古代战争即时战略游戏。游戏实施的各个方面都是现代且令人印象深刻的——从人工智能到图形。它还具有嵌入式 SpiderMonkey 脚本引擎，这是向现有 cpp 项目添加 js 脚本能力的一个很好的例子。

### 对冲战争

* C、C++、帕斯卡、哈斯克尔
* GPLv2 许可证

> Hedgewars 是一款 2D 回合制策略游戏，类似于蠕虫，但有刺猬。它的图形、动画和游戏玩法可以在各个层面上与蠕虫竞争。游戏服务器是一个令人印象深刻的 Haskell 现实世界示例，前端在 QT 和后端游戏之间提供了一个干净的接口。

### 韦诺之战

* c、c++、lua
* GPLv2 许可证

> 韦诺之战是一款回合制战术策略游戏，具有高度奇幻主题。它具有单人游戏和在线多人战斗功能。它的 GUI 和游戏图形以及多平台支持（甚至基于 NaCL 构建）令人印象深刻。它提供了干净、编码良好的示例，几乎涵盖了游戏开发人员想要了解的所有内容，从嵌入式 lua 脚本引擎，到对话框和 GUI 系统，再到 C++ 测试套件和跨平台构建。


## 许可证

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png)](http://creativecommons.org/publicdomain/zero/1.0/)

在法律允许的范围内，John Faucett 放弃了本作品的所有版权以及相关或邻接权。
