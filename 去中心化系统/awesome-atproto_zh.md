<div align="center">
<img src="https://raw.githubusercontent.com/atblueprints/awesome-atproto/main/assets/logo.png" width="300px">

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
</div>

# 很棒的 ATProto

> [AT Protocol](https://atproto.com/) 是一个联盟协议，用于在开放、去中心化的网络上构建社交应用程序

## 内容

* [AT协议](#at-protocol)
    * [References](#references)
    * [Articles](#articles)
* [Browsers](#browsers)
* [Platforms](#platforms)
    * [Bluesky](#bluesky)
* [Tools](#tools)
* [Lexicons](#lexicons)

## AT协议

### 参考文献

* [Glossary](https://atproto.com/guides/glossary) - AT 协议术语快速参考。
* [Lexicons, Pinned Posts, and Interoperability](https://docs.bsky.app/blog/pinned-posts) - 关于词典演变和经验教训的事后剖析。
* [Quick start guide to building applications on AT Protocol](https://atproto.com/guides/applications) - 创建基本 ATProto 应用程序的指南。

### 文章

* [First impressions of Bluesky's AT Protocol](https://educatedguesswork.org/posts/atproto-firstlook/) - 深入分析 Bluesky 的 ATProto，强调其创建去中心化社交媒体架构的目标。
* [Nostr and ATProto](https://shreyanjain.net/2024/07/05/nostr-and-atproto.html) - 比较 Nostr 和 ATProto 这两种去中心化社交媒体协议，探讨它们的起源、异同。
* [How decentralized is Bluesky really?](https://dustycloud.org/blog/how-decentralized-is-bluesky/) - 对 Bluesky 的去中心化主张及其与既定协议相比的架构挑战进行严格审查。
* [Reply on Bluesky and Decentralization](https://whtwnd.com/bnewbold.net/3lbvbtqrg5t2t) - 回复 Christine Lemmer-Webber 深思熟虑（且被广泛阅读）的“Bluesky 到底有多去中心化？”博客文章。
* [What is atproto.com good for?](https://bnewbold.net/2022/atproto_thoughts/) - 对 ATProto 的设计原则、架构挑战以及作为去中心化社交媒体协议的潜在局限性进行技术探索。
* [The AT Protocol Architecture](https://hackernoon.com/the-at-protocol-architecture) - ATProto 架构分析。
* [运行全网络 atproto 中继的注意事项（2024 年 7 月）](https://whtwnd.com/bnewbold.net/entries/Notes%20on%20Running%20a%20Full-Network%20atproto%20Relay%20(July%202024)) - 有关运行 ATProto 中继的经验。

## 浏览器

* [PDSls](https://pdsls.dev/) - ATProto 存储库浏览器。
* [ATProto Browser](https://atproto-browser.vercel.app/) - ATProto URI 浏览器。

## 平台

* [Bluesky](https://bsky.social) - 深受喜爱的社交网络和主要 ATProto 平台。
* [Blue Place](https://place.blue/) - 大量实时协作画布。
* [Bookhive](https://bookhive.buzz/) - 好读的替代品。
* [Frontpage](https://frontpage.fyi/) - 联合链接聚合器。
* [GrayHaze](https://grayhaze.live/about) - 实时流媒体服务（alpha）。
* [Linkat](https://linkat.blue/) - Bluesky 简介中的链接。
* [Pastesphere](https://pastesphere.link/) - 巴斯德宾替代品。
* [Picosky](https://psky.social/) - ATProto 聊天应用程序视图。
* [PinkSea](https://pinksea.art/) - 大卡基论坛。
* [recipe.exchange](https://recipe.exchange/) - 烹饪食谱分享。
* [Skylights](https://skylights.my/) - 书评。
* [Smoke Signal](https://smokesignal.events/) - 活动创建和管理。
* [Sparta Social](https://github.com/dblock/sparta-social) - 锻炼活动追踪器（wip）。
* [Whitewind](https://whtwnd.com/) - 使用 ATProto 的 Markdown 博客服务，无需注册。

### 蓝天

* [ClearSky](https://clearsky.app/) - 探索 Bluesky 帐户的工具。
* [cleanfollow](https://cleanfollow-bsky.pages.dev/) - 选择不活动或被阻止的帐户以取消关注。
* [Handles directory](https://blue.mackuba.eu/directory/) - 处理 TLD 排名。
* [Labellers](https://blue.mackuba.eu/labellers/) - 已知贴标商列表。
* [蓝滑雪账户历史](https://mocku.me/nt/#%23+BluSki+account+history//%23%23+Whose+history%3F//Let's+pick+a+rando+hot+poster+from+Discovery+feed+--//%60 %60%60JavaScript/%2F%2F+下载+Discovery+feed+posts/let+discoveryFeedPosts+=+(await+fetch(/++'https:%2F%2Fapi.bsky.app%2Fxrpc%2Fapp.bsk y.feed.getFeed%3Ffeed=at:%2F%2Fdid:plc:z72i7hdynmk6r22z27h6tvur%2Fapp.bsky.feed.generator%2Fwhats-hot%26limit=100',/++%7B+标头:+%7B+'acce pt-语言':+'en'+%7D+%7D).then(x+=%3E+x.json())).feed;//%2F%2F+sort+by+likes/let+topTextPost+=+discoveryFeedPosts/++.filter(p+=%3E+p.post. record.text+%26%26+!p.post.record.embed)/++.sort((p1,+p2)+=%3E+p2.post.likeCount+-+p1.post.likeCount)%5B0%5D;//%2F%2F+let's+see+all+the+info +now/let+hotAuthor+=+%7B/++...topTextPost.post.author,/++post:+%7B+...topTextPost.post,+...topTextPost.post.record,+post:+未定义,+记录: +undefined,+author:+undefined+%7D/%7D;/%60%60%60//如果+you're+after+specifc+handle,+specify+it+now.//%60%60%60JavaScript/let+bskyHandle+=+%2F% 2F+'oyin.bo';+++++++%2F%2F++%3C--+like+this/++hotAuthor.handle;+//let+resolvedAccount+=++await+fetch(/++'https:%2F%2Fpublic.api.bsky.app%2Fx rpc%2Fapp.bsky.actor.getProfile%3Factor='+%2B+bskyHandle).then(x=%3Ex.json())/%60%60%60//%23%23+Finding+PDS+for+that+account//PDS,+个人+数据+服务器+物理+存储+帐户的+数据。+通常+它的+一个+一个+几个+几十个+BluSki+服务器+在+云中。//通过+传统+他们+得到+拉丁+蘑菇+名称。//帐户+有时+shift+从+一个+蘑菇+到+另一个，+所以+我们+找到+the+latest+most+actual+PDS。//%60%60%60JavaScript/let+plcE ntries+=+await+fetch(%60https:%2F%2Fplc.directory%2F$%7BresolvedAccount.did%7D%2Flog%2Faudit%60).then(x+=%3E+x.json());+%2F%2F+full+account+注册表/let+lastKnownPds+=+plcEntries.slice().reverse().map(x=%3Ex.operation%3F.services%3F.atproto_pds%3F.endpoint).filter(Boolean)%5B0%5D ;+%2F%2F+last+PDS+操作+记录/%60%60%60//%23%23+下载+the+history+in+CAR%2FCBOR+format//账户+历史+is+a+public+service,+beca use+it's+used+in+distributing+BluSki+data+across+the+network。+The+file+can+be+anything+ Between+1-50Mb+depending+on+shitposting+power。//The+b inary+CAR%2FCBOR+format+saves+storage+and+bandwith,+and+has+extra+funky+cryptographic+signatures+(of+which+no+normal+person+cares).//%60%60%6 0JavaScript/let+binarySnapshot+=+await+fetch(lastKnownPds+%2B+'%2Fxrpc%2Fcom.atproto.sync.getRepo%3Fdid='+%2B+resolvedAccount.did).then(x+=% 3E+x.arrayBuffer());/binarySnapshot.byteLength.toLocaleString()/%60%60%60//%23%23+Extracting+useful+data+from+CAR%2FCBOR//有+are+库s+for+that+in+every+programming+language.+Just+invoke+and+it'll+come.//%60%60%60JavaScript/import+%7B+readCAR+%7D+from+'https:%2F%2Funpkg.co m%2Fcoldsky';/let+parsedRecords+=+await+readCAR(resolvedAccount.did,+binarySnapshot,+%7B+sleep:+600+%7D)/%60%60%60//%23+最后,+有用+信息!//拥有+这个+丰富的+历史+的+垃圾帖子、+回复、+喜欢+和+更多，+我们+准备好+查看+实际+统计数据。//%23%23+什么+种类+的+活动+统治ates%3F//%60%60%60SQL/SELECT+%5B$type%5D,+COUNT(*)/FROM+$4+GROUP+BY+%5B$type%5D/ORDER+BY+COUNT(*)+DESC/%60%60%60//%23%23+5+天+最重+ shitpost//%60%60%60SQL/SELECT+TOP+5+createdAt-%3Esplit('T')-%3E%5B0%5D+as+date,+COUNT(*)/FROM+$4/++WHERE+%5B$type%5D+=+%22app.bsky.feed.post %22/++GROUP+BY+createdAt-%3Esplit('T')-%3E%5B0%5D/ORDER+BY+COUNT(*)+DESC/%60%60%60//%23%23+5+days+of+love:+更多+喜欢+有天赋+给+其他人//%60% 60%60SQL/SELECT+TOP+5+createdAt-%3Esplit('T')-%3E%5B0%5D+as+date,+COUNT(*)/FROM+$4/++WHERE+%5B$type%5D+=+%22app.bsky.feed.like%22/++GROUP+BY +createdAt-%3Esplit('T')-%3E%5B0%5D/ORDER+BY+COUNT(*)+DESC/%60%60%60//%23%23+10+收藏+帐户//%60%60%60SQL/SELECT+TOP+10+主题-%3Eur i-%3Esplit('at:%2F%2F')-%3E%5B1%5D-%3Esplit('%2F')-%3E%5B0%5D+as+did,+COUNT(*)+AS+likes/FROM+$4/++WHERE+%5B$type%5D+=+%22app.bsky.feed.like% 22/++GROUP+BY+主题-%3Euri-%3Esplit('at:%2F%2F')-%3E%5B1%5D-%3Esplit('%2F')-%3E%5B0%5D/ORDER+BY+COUNT(*)+DESC/%60%60%60//%23%23+谁+是+th ese+people%3F//帐户+历史记录+文件+引用+to+其他+帐户+with+十六进制+DID,+which+as+you+see+above+isn't+that+可读。//No+sweat,+Bl uSki+has+a+service+to+resolve+DID+to+account+name%2Fhandle%2Finfo.+Here+you+go.//%60%60%60JavaScript/Promise.all($8.map(async+entry+=%3E+%7B /++const+profile+=+await+fetch('https:%2F%2Fpublic.api.bsky.app%2Fxrpc%2Fapp.bsky.actor.getProfile%3Factor='+%2B+entry.did).then(x+=%3E+x.js on());/++return+%7B/++++did:+profile.did,+handle:+profile.handle,+displayName:+profile.displayName,/++++likesCount:+entry.likes,/++++postsCou
* [Starter Packs](https://www.starterpacks.net/) - 搜索 Bluesky 入门包和配置文件。
* [PDS self-hosting](https://atproto.com/guides/self-hosting) - 自托管 Bluesky PDS 意味着运行您自己的个人数据服务器，该服务器能够与更广泛的 ATProto 网络联合。
* [Bluesky-powered comments for any website](https://github.com/czue/bluesky-comments) - 轻松在您的网站上嵌入 Bluesky 评论（[公告](https://www.coryzue.com/writing/bluesky-comments/)）。

有关更多 Bluesky 工具，请查看 [Awesome Bluesky](https://github.com/notjuliet/awesome-bluesky)，这是适用于 Bluesky 的更详尽的工具和客户端列表。

## 工具

* [ATFile](https://github.com/ziodotsh/atfile) - 在 ATmosphere 上存储和检索文件。
* [ShopSavvy for Bluesky](https://github.com/shopsavvy/bluesky-shopsavvy) - AT 协议套件：用于实时价格查找的反应式提及机器人、自定义交易源生成器和每日交易海报。

## 词典

Lexicon 是一种模式定义语言，用于描述 atproto 记录、HTTP 端点 (XRPC) 和事件流消息。

在下面找到每个平台的词典：

* [ATFile](https://github.com/ziodotsh/lexicons/tree/main/blue/zio/atfile)
* [Bluemoji](https://github.com/aendra-rininsland/bluemoji/tree/main/schema/blue.moji)
* [Bluesky](https://github.com/bluesky-social/atproto/tree/main/lexicons/app/bsky)
* [Bookhive](https://github.com/nperez0111/bookhive/tree/main/lexicons)
* [Frontage](https://github.com/likeandscribe/frontpage/tree/main/lexicons/fyi/unravel/frontpage)
* [GrayHaze](https://github.com/hugeblank/grayhaze.live/tree/main/lexicons/live/grayhaze)
* [Linkat](https://github.com/mkizka/linkat/tree/main/lexicons/blue/linkat)
* [Pastesphere](https://github.com/echo8/pastesphere/tree/main/lexicons)
* [Picosky](https://github.com/psky-atp/appview/tree/main/lexicons/social/psky)
* [PinkSea](https://github.com/shinolabs/PinkSea/tree/master/PinkSea.Lexicons/com/shinolabs/pinksea)
* [place.blue](https://github.com/QuietImCoding/place.blue/tree/main/atproto/lexicons)
* [recipe.exchange](https://recipe.exchange/lexicons/)
* [Skylights](https://github.com/Gregoor/skylights/tree/main/web/lexicons)
* [Skymdb](https://github.com/safwanyp/skymdb/tree/main/domain/lexicons)
* [烟雾信号](https://github.com/SmokeSignal-Events/lexicon)
* [斯巴达社交](https://github.com/dblock/sparta-social/tree/main/lexicons)
* [Whitewind](https://github.com/whtwnd/whitewind-blog/tree/main/lexicons/com/whtwnd/blog) 

## 贡献

欢迎投稿！首先阅读[贡献指南](contributing.md)。
