# 很棒的 IRC [![Awesome](https://awesome.re/badge-flat.svg)](https://awesome.re)

> 精选的精彩 [IRC](https://en.wikipedia.org/wiki/Internet_Relay_Chat) 资源列表。

与 Internet 中继聊天 (IRC) 协议相关的工具、软件和其他资源列表。

IRC（Internet Relay Chat）是一种开源协议，可用于通过通道进行基于文本的多用户通信。

## 内容

<!--lint disable awesome-list-item-->
<!--lint ignore awesome-toc double-link-->
- [Clients](#clients)
- [Bouncers](#bouncers)
  - [Hosted](#hosted)
  - [Self-hosted](#self-hosted)
- [Daemons](#daemons)
- [Services](#services)
- [Bots](#bots)
- [Encryption](#encryption)
- [Frameworks](#frameworks)
  - [Bridges](#bridges)
- [Channels](#channels)
  - [Discovery](#discovery)
  - [Platforms](#platforms)
- [Networks](#networks)
- [Articles](#articles)
- [Guides](#guides)
- [Protocol](#protocol)
- [Miscellaneous](#miscellaneous)

## 客户

*您使用它们连接到 IRC。*

- [![Textual-icon](https://user-images.githubusercontent.com/15098724/56874954-680a0500-69f2-11e9-87ec-d4015ce54af5.png) Textual](https://www.codeux.com/textual/) - 非常可定制，ZNC 集成，iCloud 同步（4.99 美元）。 ([来源](https://github.com/Codeux-Software/Textual)) `macOS`
- [![LimeChat-icon](https://user-images.githubusercontent.com/15098724/56875043-04cca280-69f3-11e9-8e1f-285e54784fe4.png) LimeChat](http://limechat.net/mac/) - 一个窗口用于多个服务器，键盘快捷键，快速稳定。 ([来源](https://github.com/psychs/limechat)) `macOS` `iOS`
- [![HexChat-icon](https://user-images.githubusercontent.com/15098724/56874706-b28a8200-69f0-11e9-9ca7-27c8779134e0.png) HexChat](https://hexchat.github.io) - 基于 XChat，易于使用、拼写检查和多种语言。 ([来源](https://github.com/hexchat/hexchat)) `Windows` `macOS` `Linux`
- [gamja](https://sr.ht/~emersion/gamja/) - 一个简单的 IRC Web 客户端。 ([来源](https://git.sr.ht/~emersion/gamja)) `Web`
- [![KiwiIRC-icon](https://user-images.githubusercontent.com/15098724/56875143-a7852100-69f3-11e9-8b33-2035c156c016.png) Kiwi IRC](https://kiwiirc.com) - 强大的现代 IRC 网络信使。 ([来源](https://github.com/kiwiirc/kiwiirc), [演示](https://kiwiirc.com/nextclient/)) `Web`
- [![CIRC-icon](https://user-images.githubusercontent.com/15098724/56875201-1498b680-69f4-11e9-91ff-ae3b674c82be.png) CIRC](https://flackr.github.io/circ/) - 使用 chrome.sockets API 直接连接到 IRC 服务器，无需代理。 ([来源](https://github.com/flackr/circ)) `Chrome`
- [![Quassel-icon](https://user-images.githubusercontent.com/15098724/56875264-84a73c80-69f4-11e9-807c-75db09db0ec5.png) Quassel](https://quassel-irc.org) - 分布式（客户端可以连接到永久在线的中央核心或从中分离。 ([来源](https://github.com/quassel/quassel)) `Linux` `macOS` `Windows`
- [![Circe-icon](https://user-images.githubusercontent.com/15098724/56875558-a3a6ce00-69f6-11e9-92da-2e4d8c7b4a53.png) Circe](https://github.com/emacs-circe/circe) - 用于 Emacs，默认值正常。 `Emacs`
- [![Smuxi-icon](https://user-images.githubusercontent.com/15098724/56875672-2f205f00-69f7-11e9-8cac-5721602234bb.png) Smuxi](https://smuxi.im) - 用户友好，基于 GNOME / GTK+。 ([来源](https://github.com/meebey/smuxi)) `Linux` `Windows` `macOS`
- [![KvIRC-icon](https://user-images.githubusercontent.com/15098724/56874636-1d878900-69f0-11e9-856e-719c4c822e25.png) KvIRC](https://www.kvirc.net) - 免费、可移植、基于 Qt GUI 工具包。 ([来源](https://github.com/kvirc/KVIrc)) `Linux` `macOS` `Windows`
- [![Konversation-icon](https://user-images.githubusercontent.com/15098724/56876024-609a2a00-69f9-11e9-91dd-196f310776d7.png) Konversation](https://konversation.kde.org) - 基于 KDE 平台构建的用户友好客户端。 ([来源](https://github.com/KDE/konversation)) `Linux`
- [![sic-icon](https://user-images.githubusercontent.com/15098724/56876157-457bea00-69fa-11e9-94f5-11dcd0bfb00c.png) sic](https://tools.suckless.org/sic/) - **S**imple **I**RC **c**lient - 终端客户端不到 250 行 C 语言。 `Linux` `macOS`
- [![irssi-icon](https://user-images.githubusercontent.com/15098724/56876266-0c904500-69fb-11e9-85a9-00796373cf88.png) irssi](https://irssi.org) - 终端客户端，对模块作者来说多协议友好，GPLv2。 `Linux` `macOS` `Cygwin` `BSD`
- [![RevolutionIRC-icon](https://user-images.githubusercontent.com/15098724/56876444-4f065180-69fc-11e9-8200-b244b6a86e94.png) Revolution IRC](https://github.com/MCMrARM/revolution-irc) - 功能齐全、积极维护的 Android IRC 客户端。 `安卓`
- [![AdiIRC-icon](https://user-images.githubusercontent.com/15098724/56632956-0e2fc680-6611-11e9-949e-c79c21f465a0.png) AdiIRC](https://adiirc.com) - 从来没有客户端为 IRC 体验的各个方面提供如此精细的设置。 ([功能](https://dev.adiirc.com/projects/adiirc/wiki/Features), [屏幕截图](https://dev.adiirc.com/projects/adiirc/wiki/Screenshots)) `Windows` `WINE`
- [![IRCforAndroid-icon](https://user-images.githubusercontent.com/15098724/56655816-b3b25c80-6648-11e9-92e1-12ca4587d9eb.png) IRC for Android™](https://www.countercultured.net/android/) - 适用于高级用户的 Android/Chrome 操作系统客户端，带有 ZNC内置、通知逻辑、可靠的 DCC、硬件键盘的按键绑定等。`Android``ChromeOS`
- [Iridium](https://appcenter.elementary.io/com.github.avojak.iridium/) - 友好的 IRC 客户端内置于 Vala 和 GTK，专为基本操作系统设计。 ([来源](https://github.com/avojak/iridium)) `Linux`
- [MERK](https://github.com/nutjob-laboratories/merk) - 开源、多文档界面 GUI 客户端，具有丰富的插件框架，支持 40 多个事件；直接在应用程序内创建的插件。 ([来源](https://github.com/nutjob-laboratories/merk)) `Windows` `macOS` `Linux` `Python`
- [mIRC](https://www.mirc.co.uk) - 最流行的 Windows IRC 客户端之一，具有内置脚本语言。 `Windows`
- [ObsidianIRC](https://hello.obby.world/) - 现代 WebSocket IRC 客户端，具有类似 Discord 的 UI。 ([来源](https://github.com/ObsidianIRC/ObsidianIRC)) `Linux` `Windows` `macOS` `Android` `iOS` `Web`
- [XChat](https://xchat.org) - HexChat 的前身，多平台图形 IRC 客户端。 `Windows``Linux`
- [ircII](http://www.eterna23.net/ircii/) - 最古老的 IRC 客户端之一，最初发布于 1989 年。 `Linux` `macOS`
- [BitchX](https://bitchx.sourceforge.net/) - 基于终端的客户端在类 Unix 系统上很流行。 ([屏幕截图](https://bitchx.sourceforge.net/category/screenshots.html)) `Linux` `macOS` `Windows`
- [Goguma](https://sr.ht/~emersion/goguma/) - 用于移动设备的 IRC 客户端，来自 soju 的创建者。 `安卓``Linux`

<!--lint ignore double-link-->
*更多？包含保镖的客户可在[下方](#bouncers)找到。*

## 保镖

*对于断开连接和重新连接而不丢失聊天会话很有用。*

### 主办

- [![IRCCloud-icon](https://user-images.githubusercontent.com/15098724/56879253-ba581f80-6a0c-11e9-8f6b-8461c10ed149.png) IRCCloud](https://www.irccloud.com) - 团队、朋友和社区的群聊。保持联系，随时随地聊天，不错过任何消息（+客户端）（0-3.50 英镑/月）。
  - [iOS App](https://github.com/irccloud/ios) - 官方的。 `Objective-C`
  - [Android App](https://github.com/irccloud/android) - 官方。 `Java`
  - [Nimbus](https://github.com/jnordberg/irccloudapp) - 独立客户端。 `macOS` `Objective-C`

### 自托管

- [![Convos-icon](https://user-images.githubusercontent.com/15098724/56879497-d8724f80-6a0d-11e9-844d-7a5380b4524b.png) Convos](https://convos.chat) - 始终在线的 Web IRC 客户端。 ([来源](https://github.com/convos-chat/convos)) `Perl` `JavaScript` `Web`
- [![ZNC-icon](https://user-images.githubusercontent.com/15098724/56879721-d8268400-6a0e-11e9-8b74-c2c748d15c4a.png) ZNC](https://wiki.znc.in/ZNC) - 最受欢迎。许多不同的插件。 ([来源](https://github.com/znc/znc)) `C++`
- [![BIP-icon](https://user-images.githubusercontent.com/15098724/56899123-89491080-6a47-11e9-8513-4c8d09be32d9.png) BIP IRC 代理](https://bip.milkypond.org) - 始终在线、轻量级且安全的开源 IRC 代理，具有积压功能。 ([来源](https://projects.duckcorp.org/projects/bip/repository)) `C`
- [![TheLounge-icon](https://user-images.githubusercontent.com/15098724/56899491-6b2fe000-6a48-11e9-9f01-1ed2cfb86b09.png) TheLounge](https://thelounge.chat) - 响应式、自托管并支持多个用户。 ([来源](https://github.com/thelounge/thelounge), [演示](https://demo.thelounge.chat/)) `JavaScript` `Node.js` `Web`
- [![WeeChat-icon](https://user-images.githubusercontent.com/15098724/56876389-e028f880-69fb-11e9-82d6-8084e17f2f04.png) WeeChat](https://weechat.org) - 一款快速、轻便且可扩展的聊天客户端。 ([来源](https://github.com/weechat/weechat)) `Linux` `macOS`
- [soju](https://codeberg.org/emersion/soju) - 用户友好的 IRC 保镖。 ‘走’
- [sms-webhook](https://github.com/terminaldweller/sms-webhook) - 一个简单的 Webhook，用于在 IRC 上接收 SMS 消息。 ‘走’
- [psyBNC](https://psybnc.org/) - 具有加密支持的多用户、永久 IRC 保镖。 `Linux`

## 守护进程

*用于运行您自己的 IRC 服务器或网络。*

- [ircd.js](https://github.com/alexyoung/ircd.js) - 服务器将允许客户端连接、加入频道、更改主题；基本的东西。
- [InspIRCd](https://www.inspircd.org) - 模块化、稳定、从头开始编写。 ([来源](https://github.com/inspircd/inspircd))
- [miniircd](https://github.com/jrosdahl/miniircd) - 非常简单且有限。
- [ngIRCd](https://ngircd.barton.de) - 便携且轻便，适用于小型或专用网络。 ([来源](https://github.com/ngircd/ngircd))
- [Ergo](https://ergo.chat/) - 便携式现代服务器，围绕规范设计（前沿的 IRCv3 支持）。 ([来源](https://github.com/ergochat/ergo))
- [UnrealIRCd](https://www.unrealircd.org) - 自 1999 年以来，模块化、先进的 IRCd 为数千个网络提供服务。（[来源](https://github.com/unrealircd/unrealircd)）
- [RobustIRC](https://robustirc.net) - 没有网络分割的 IRC 服务器。 ([来源](https://github.com/robustirc/robustirc/))

## 服务

*用于向您的网络提供用户帐户和机器人（例如 NickServ/ChanServ）。*

- [Atheme](https://atheme.github.io) - 专为具有高可扩展性要求的大型网络而设计。 ([来源](https://github.com/atheme/atheme))
- [anope](https://www.anope.org) - 专为灵活性和易用性而设计。 ([来源](https://github.com/anope/anope))

## 机器人

*为人类提供服务的IRC用户，例如集成或信息。*

- [Eggdrop](https://www.eggheads.org) - 最古老的 IRC 机器人仍在积极开发中。功能丰富，使用Tcl脚本。 ([来源](https://github.com/eggheads/eggdrop)) `C`
- [Sopel](https://sopel.chat) - 大量现成的功能、教程、完整的文档。 ([来源](https://github.com/sopel-irc/sopel)) `Python`
- [Limnoria](https://github.com/ProgVal/Limnoria) - 健壮、用户友好、开发人员友好。 `Python`
- [Twitch Plays](https://github.com/aidanrwt/twitch-plays ) - 从聊天中获取输入并按相应的键。 `Python`
- [Skybot](https://github.com/rmmh/skybot) - 主要目标是简单和强大。 `Python`
- [lazybot](https://github.com/Raynes/lazybot) - 用户友好且功能强大。 `Clojure`
- [IRC-BF](https://gitlab.com/ddevault/bf-irc-bot) - ‘脑残’
- [geordi](https://github.com/Eelis/geordi) - 编译并运行 C++ 代码片段。 `C++`
- [CloudBot](https://github.com/TotallyNotRobots/CloudBot) - 简单、快速、可扩展。 `Python`
- [yossarian-bot](https://github.com/woodruffw/yossarian-bot) - 大型默认插件集，基于 Cinch。 「红宝石」
- [helga](https://github.com/shaunduncan/helga) - 支持多种协议的可插拔聊天机器人。 `Python`
- [EveIRC](https://github.com/Inspyre-Technologies/EveIRC) - 可扩展的聊天/频道/服务器管理服务提供机器人。使用[Cinch框架](https://github.com/cinchrb/cinch)。 「红宝石」
- [BitBot](https://github.com/bitbot-irc/bitbot) - 模块化、事件驱动的机器人，具有 REST API、个人用户设置等。 ([bitbot.dev](https://bitbot.dev)) `Python`
- [Cardinal](https://github.com/JohnMaguire/Cardinal) - Python Twisted IRC 机器人，专注于插件开发的简易性。 `Python`
- [pyHoneybot](https://pyhoneybot.github.io/honeybot-store/) - Python Twisted IRC 机器人，专注于插件开发的简易性。 ([来源](https://github.com/pyhoneybot/honeybot)) `Python`
- [wayback](https://github.com/wabarc/wayback) - 具有 IRC 界面的归档工具，集成了各种归档服务。
- [milla](https://github.com/terminaldweller/milla) - 新一代 LLM 支持的机器人，支持 lua 脚本。 ‘走’
- [MansionNET Bot Suite](https://github.com/MansionNET) - 自托管 IRC 机器人的集合：人工智能聊天助手、实时天气、注重隐私的搜索、YouTube 元数据和人工智能驱动的琐事。 ([来源](https://github.com/MansionNET)) `Python`

## 加密

*用于加密 IRC 消息的插件和工具。*

- [irssi-otr](https://github.com/cryptodotis/irssi-otr) - irssi 的非记录 (OTR) 消息传递插件。 `C`
- [weechat-otr](https://github.com/mmb/weechat-otr) - WeeChat 的非记录 (OTR) 消息传递插件。 `Python`
- [FiSH-irssi](https://github.com/falsovsky/FiSH-irssi) - ECB/CBC 模式下的 Blowfish 加密与 irssi 的 Diffie-Hellman 密钥交换。 `C`

## 框架

*有助于编写机器人或将 IRC 与应用程序集成。*

- [node-irc](https://github.com/Throne3d/node-irc)`JavaScript`
- [goirc](https://github.com/fluffle/goirc) - 基于事件、有状态、缺乏文档。 ‘走’
- [Hubot IRC Adapter](https://github.com/nandub/hubot-irc) - hubot 的 IRC 适配器。 `JavaScript`
- [go-ircevent](https://github.com/thoj/go-ircevent) - 基于事件。 ‘走’
- [slate-irc](https://github.com/slate/slate-irc) - 插件系统，简单的API，任意输入流，调试支持。 `JavaScript`
- [PircBotX](https://github.com/pircbotx/pircbotx) - 基于事件的 IRC 库，具有简单的 API（[PircBot](https://www.jibble.org/pircbot.php) 的更新分支）。 `Java`
- [IRC::Client](https://github.com/lizmat/IRC-Client) - 基于“Perl6”的可扩展 IRC 客户端框架。
- [irccd](https://projects.malikania.fr/irccd/index.html) - 可使用 JavaScript 进行自定义的灵活 IRC 机器人。 `C++`。

### 桥梁

*来回发送消息。*

- [discord-irc](https://github.com/reactiflux/discord-irc) - 不和谐 ↔ IRC。 `JavaScript`
- [dibridge](https://github.com/OpenTTD/dibridge) - Discord ↔ IRC（带木偶）`Python`
- [Dis4IRC](https://github.com/zachbr/Dis4IRC) - 不和谐 ↔ IRC。 `科特林`
- [slack-irc](https://github.com/ekmartin/slack-irc) - Slack ↔ IRC。 `JavaScript`
- [irc-slack](https://github.com/insomniacslk/irc-slack) - Slack ↔ IRC。 ‘走’
- [BitlBee](https://www.bitlbee.org/main.php/news.r.html) - XMPP、Jabber、Google Talk、MSN Messenger、雅虎！ Messenger、AIM、ICQ、Twitter API、HipChat ↔ IRC。 `C`
- [teleirc](https://github.com/RITlug/teleirc) - 电报 ↔ IRC。 `JavaScript`
- [toxirc](https://github.com/e0ff/toxirc) - 毒物 ↔ IRC。 `C`
- [skyweb2irc](https://github.com/ProgVal/skyweb2irc) - Skype（网络客户端 API）↔ IRC。 `Javascript`
- [matterbridge](https://github.com/42wim/matterbridge) - IRC ↔ Mattermost ↔ Discord ↔ XMPP ↔ Gitter ↔ Slack ↔ Discord ↔ Telegram ↔ 等等 `Go`
- [Heisenbridge](https://github.com/hifi/heisenbridge) - Bouncer 风格的 Matrix IRC 桥“Python”
- [Appservice-IRC](https://github.com/matrix-org/matrix-appservice-irc) - 网关和网桥 Matrix ↔ IRC `Javascript`
- [matterircd](https://github.com/42wim/matterircd) - Matterbridge ↔ IRC、Slack ↔ IRC、Mastodon ↔ IRC。 ‘走’

## 渠道

*IRC 频道。*

### 发现

- [netsplit.de Search](https://netsplit.de/channels/ ) - 搜索 563 个不同的网络。
- [KiwiIRC Search](https://kiwiirc.com/search) - 搜索 318 个不同的网络。

### 平台

- [#Ubuntu](https://wiki.ubuntu.com/IRC/ChannelList)@Libera.Chat - Ubuntu 官方支持频道。 （[规则](https://wiki.ubuntu.com/IRC/Guidelines)）

## 网络

*IRC 服务器的集合称为网络。*

- [Libera.Chat](https://libera.chat) - Network 主要专注于免费和开源项目，由前 freenode 员工运营。
- [MansionNET](https://inthemansion.com) - 注重隐私的社区网络，运行 UnrealIRCd 和 Anope 服务；向所有人开放，无跟踪，无广告。 （`irc.inthemansion.com:6697`，网络聊天位于`webirc.inthemansion.com`）
- [Snoonet](https://snoonet.org) - reddit 和 subreddits 社区。 ([规则](https://snoonet.org/rules/))
- [OFTC](https://oftc.net) - 免费和开源软件社区的社区。
- [LibertaCasa](https://liberta.casa) - 隐私认可社区是讨论各种主题的安全和开放的空间。

## 文章

*有关 IRC 的文章和博客文章。*

- [Please don't use Slack for FOSS projects](https://drewdevault.com/2015/11/01/Please-stop-using-slack.html) - 德鲁·德瓦特的博客。
- [IRC is dead, long live IRC](https://www.pingdom.com/blog/irc-is-dead-long-live-irc/) - 平多姆。
- [IRC Has Lost 60% Of Its Users Since 2003, But Life As A Robot Is Just Beginning](https://techcrunch.com/2013/01/06/irc-has-lost-60-of-its-users-since-2003-but-life-as-a-robot-is-just-beginning/) - 亚历克斯·威廉姆斯（TechCrunch）。

## 指南

*操作方法、文档和书籍。*

- [#irchelp](https://www.irchelp.org) - 大量合理的最新信息。

## 协议

*有关 IRC 协议本身的信息和资源。*

- [IRCv3 Working Group](https://ircv3.net) - 一群 IRC 软件作者致力于增强、改进、维护和标准化 IRC 协议。 ([来源](https://github.com/ircv3/ircv3.github.io))
- [Modern IRC Documents](https://modern.ircdocs.horse) - 尝试写入原始 IRC 协议的更新。文档（[来源](https://github.com/ircdocs/modern-irc)）
- [IRC Definition Files](https://defs.ircdocs.horse) - 数字、模式、ISUPPORT 令牌和其他协议详细信息的列表。 ([来源](https://github.com/ircdocs/irc-defs))
- [grawity's IRC docs](https://github.com/grawity/irc-docs) - 其他 IRC 协议文档的集合。
- [Protocol Statistics](https://stats.ircdocs.horse) - 有关当今网络上使用的服务器软件的统计数据。 ([来源](https://github.com/ircdocs/irc-stats))
- [IRC Parser Tests](https://github.com/ircdocs/parser-tests) - 一组 CC0 测试套件，用于确保 IRC 消息解析器的一致性。

## 杂项

*属于列表中但无法分类的项目。*

- [superseriousstats](https://github.com/tommyrot/superseriousstats) - 快速高效的程序可以根据各种类型的聊天日志创建统计数据。 `PHP``网络`
- [img2src](https://github.com/waveplate/img2irc) - 使用一系列后处理滤镜将图像转换为半块 ANSI 或 IRC。 `铁锈`

## 使用

使用此列表的最佳方法是：

- 通过浏览[内容](#contents)
- 使用<kbd>command</kbd> + <kbd>F</kbd>搜索内容

此列表还使用标签来帮助搜索内容：
- **语言** - `Python`、`Java`、`C++`、`Go`、`JavaScript`、`Ruby`、`C` 等。
- **平台** - `Web`、`macOS`、`Windows`、`Linux`、`Chrome` 等。

## 制作人员

作者：[Craig Davison](https://davison.io) 和贡献者。
