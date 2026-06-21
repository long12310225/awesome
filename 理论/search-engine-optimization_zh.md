# 搜索引擎优化（SEO） [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

有用的清单/搜索引擎优化 (SEO) 技巧和技术的集合。

## 内容

- [URL](#url)
- [Accessibility](#accessibility)
- [元信息](#meta-information)
- [Keywords](#keywords)
- [Content](#content)
- [Images](#images)
- [Videos](#videos)
- [Links](#links)
- [Mobile](#mobile)
- [Sitemap](#sitemap)
- [社交媒体](#social-media)
- [工具与服务](#tools--services)
  - [Webmasters](#webmasters)
  - [Analytics](#analytics)
  - [Optimization](#optimization)
  - [Keywords](#keywords-1)
  - [Links](#links-1)
  - [结构化数据](#structured-data)
  - [Bookmarklets](#bookmarklets)
  - [浏览器扩展](#browser-extensions)
  - [Jekyll 插件](#jekyll-plugins)
  - [TYPO3 扩展](#typo3-extensions)
  - [WordPress 插件](#wordpress-plugins)
- [Books](#books)
- [Courses](#courses)

## 网址

- 描述性 URL：使用描述性页面 URL，该 URL 应反映您的目标关键字。
- [File extension](https://www.youtube.com/watch?v=dSG6C33GwsE) - 不要删除 URL 上的文件扩展名。
- [HTTPS](https://webmasters.googleblog.com/2014/08/https-as-ranking-signal.html) - 安全是 Google 的首要任务。
- [Hyphens](https://www.youtube.com/watch?v=AQcSFsQyct8) - 使用连字符分割单词。
- [Localisation](https://support.google.com/webmasters/answer/62399) - 选择特定于国家/地区的域名，以获得更好的本地搜索结果。
- [Subdomain or subfolder](https://www.youtube.com/watch?v=_MswMYk05tk) - 子域被视为单独的域。
- [URL builder](https://support.google.com/analytics/answer/1033867) - 使用此工具将自定义营销活动参数添加到您的 URL。

## 无障碍

- 403：提供 403 - 访问被拒绝页面。
- 404：提供 404 - 页面未找到页面。
- [Custom Search](https://developers.google.com/structured-data/slsb-overview) - 通过 Google Sitelink 搜索框，人们可以更快地找到您的内容。
- 未找到文件：避免“404 FILE_NOT_FOUND”错误。
- 布局：使用“divs”而不是“tables”进行布局。使用“tables”在语义上是不正确的。
- 移动网站：通过“.htaccess”将所有链接重定向到新位置。
- [Pagination](https://support.google.com/webmasters/answer/1663744) - 为链接实现 `rel="next"` 和 `rel="prev"` 属性。
- [Performance](https://developers.google.com/webmasters/mobile-sites/mobile-seo/common-mistakes/slow-mobile-pages) - 性能和加载时间很重要。
- 重定向：如果可能，避免重定向。使用 301 重定向而不是 302。
- [RichSnippets](https://schema.org/) - 使用丰富的代码片段标记您的代码，它们会显示在搜索结果页面上。
- [Robots](https://en.wikipedia.org/wiki/Robots_exclusion_standard) - 阻止不应通过“robots.txt”文件编制索引的页面或
`<meta name="robots" content="">`。
- 验证：编写有效代码（[HTML 验证器](https://validator.w3.org/) [CSS 验证器](https://jigsaw.w3.org/css-validator/)）。
- [WAI-Aria](https://www.w3.org/TR/wai-aria/) - 使用 WAI-Aria 标签帮助机器理解您的代码。

## 元信息

- [Description](https://www.youtube.com/watch?v=W4gr88oHb-k) - 每个页面都应有唯一的描述（最多 160 个字符）
`<meta name="description" content="">`。
- 标题：每个页面都应该有一个唯一的标题（60 - 100 个字符）“<title>网站标题</title>”。

## 关键词

- 内容：关键字应出现在文章长度的 3% 左右。
- 标题：关键字应出现在标题中。
- [Meta Tag](https://www.youtube.com/watch?v=jK7IPbnmvVU) - 您可以省略 `<meta name="keywords" content="">`，
搜索引擎不使用此元标记。
- 研究：对流量高、竞争少的关键词进行排名。
- 单一：每个页面都应该有一个唯一的目标关键字。
- 标题：关键字应出现在页面标题中。
- [URL](https://www.youtube.com/watch?v=rAWFv43qubI) - 关键字应出现在 URL 名称中。

## 内容

- 内容：内容在 SEO 中最重要。
- Flash：避免使用 Flash 内容和 Flash 页面。它们无法通过手机访问，并且排名较低。
- 新鲜度：新内容很重要。建议定期更新页面或发布。
- 标题：结构清晰“H1”-“H6”最多。 70 个字符长。
- 长度：文章应至少 300 字。
- 强：使用“强”标签来突出显示您的目标关键字。
- [Uniqueness](https://www.youtube.com/watch?v=mQZY7EmjbMA) - 不要提供重复的内容，使用独特的内容类型。

## 图片

- [Alt tag](https://support.google.com/webmasters/answer/114016) - 添加 alt 标签作为图像的描述（60 - 70 个字符）。
- 尺寸：向图像添加 `width=""` 和 `height=""` 属性。
- [File name](https://www.youtube.com/watch?v=h2SWuUobbr0) - 使用简短的描述性名称。
- [Optimization](https://imageoptim.com/) - 通过删除一些元信息来优化图像。
- [Responsive Images](https://www.w3.org/TR/html-picture-element/) - 提供与窗口大小相对应的最优化图像。
- 大小：保持文件大小尽可能小。

## 视频

- 控件：添加控件以播放并控制您的视频。
- 嵌入：允许其他人嵌入您的视频。
- 转录：使用转录进行索引、可用性和内容。
- [Unplayable content](https://developers.google.com/webmasters/mobile-sites/mobile-seo/common-mistakes/unplayable-content) - 避免无法播放的视频内容。使用 HTML5 `<video>` 标签代替 Flash。

## 友情链接

- 反向链接：仅当您的网站有反向链接时才添加外部链接。
- 内部链接：向您的内容添加 ~3 个内部链接。
- [Languages](https://moz.com/learn/seo/hreflang-tag) - hreflang 标签告诉 Google 您在特定页面上使用哪种语言，因此搜索引擎可以将该结果提供给使用该语言搜索的用户
`<link rel="alternate" href="example.com/fr/" hreflang="fr-fr" />`。
- 命名：使用描述性链接名称：“单击此处”或“阅读更多”是错误的链接文本。更好的“阅读有关 SEO 和 Web 可访问性的更多信息”。
- [nofollow](https://support.google.com/webmasters/answer/96569) - 向外部链接添加 `rel="nofollow"` 属性只是为了防止垃圾邮件和不良链接。
- 标题：为链接添加标题属性。

## 手机

- [AppLinks](http://applinks.org/documentation/) - 然后，链接到您的内容的应用程序可以使用此元数据深层链接到您的应用程序。
- [mobile friendly](https://googlewebmastercentral.blogspot.be/2014/11/helping-users-find-mobile-friendly-pages.html) - 移动优化网站会在搜索结果中标记。测试[移动设备友好网站](https://www.google.com/webmasters/tools/mobile-Friendly/)。
- [Smart App Banner](https://developer.apple.com/library/ios/documentation/AppleApplications/Reference/SafariWebContent/PromotingAppswithAppBanners/PromotingAppswithAppBanners.html) - Safari 具有智能应用横幅功能，可提供从网站在 App Store 上推广应用的标准化方法。
- [Tap targets](https://developers.google.com/speed/docs/insights/SizeTapTargetsAppropriately) - 可点击的链接不应太小。
- 视口：告诉浏览器如何调整页面的尺寸和缩放比例以适应设备
`<meta name =“viewport”content =“width = device-width，initial-scale = 1”>`

## 网站地图

- [HTML sitemap](https://www.youtube.com/watch?v=hi5DGOu1uA0) - HTML 站点地图允许站点访问者轻松浏览网站。
- [Image sitemap](https://support.google.com/webmasters/answer/178636) - 增加您的图像可以在图像搜索结果中找到的程度。
- [Mobile sitemap](https://support.google.com/webmasters/answer/6082207) - 对于功能手机，您可以创建移动站点地图。
- [Video sitemap](https://support.google.com/webmasters/answer/80471) - 确保搜索引擎了解您网站上的所有视频内容。
- [XML sitemap](https://support.google.com/webmasters/answer/183668) - 帮助搜索引擎索引您的页面。

## 社交媒体

- 作者信息。
- [Facebook](https://developers.facebook.com/docs/sharing/best-practices) - 分享网站和移动应用程序的最佳实践。
- [OpenGraph](http://ogp.me/) - 开放图谱协议使任何网页都可以成为社交图谱中的丰富对象。
- [Social Profiles](https://developers.google.com/webmasters/structured-data/customize/social-profiles) - 将社交资料添加到您的 Google 搜索结果中。
- 社交共享：为您的网站提供共享选项。
- [Twitter](https://dev.twitter.com/cards/getting-started) - 使用 Twitter 卡，您可以将照片、视频和媒体体验附加到您的推文中。

## 工具与服务

### 网站管理员

- [Bing Webmasters](http://www.bing.com/toolbox/webmaster) - 允许网站管理员将其网站添加到 Bing 索引爬虫。
- [Google Search Console (GWT)](https://www.google.com/webmasters/) - 允许网站管理员检查索引状态并优化其网站的可见性。
- [Google Tag Manager](https://www.google.com/analytics/tag-manager/) - 了解 Google Analytics（分析）跟踪代码管理器以及它如何帮助简化您的生活和 IT 请求需求。只需点击几下即可启动新标签。

### 分析

- [Ahrefs](https://ahrefs.com/) - 分析网站、跟踪社交媒体、建立反向链接 - Ahrefs 都能满足您的需求。立即尝试我们的营销和 SEO 工具网站浏览器和内容浏览器！
- [BuzzSumo](https://app.buzzsumo.com/research/most-shared) - 查找任何主题或领域最共享的内容。
- [Followerwonk](https://moz.com/followerwonk) - Twitter 分析、生物搜索等工具。
- [Google Analytics](https://www.google.com/analytics/) - 生成有关网站流量的详细统计数据。
- [Open Site Explorer](https://moz.com/researchtools/ose/) - 使用 Open Site Explorer 来识别链接构建机会。研究反向链接、识别热门页面、查看社交活动并分析锚文本。
- [Matomo](https://matomo.org/) - 开放的分析平台。
- [SEMrush](https://www.semrush.com/) - SEMrush 是一款功能强大且多功能的竞争情报套件，适用于在线营销，从 SEO 和 PPC 到社交媒体和视频广告研究。
- [Seomator](https://seomator.com/) - SEO 审核工具和网站爬虫可通过如何修复提示提高 SEO 性能。
- [SEOstats](https://github.com/eyecatchup/SEOstats) - SEOstats 是一个功能强大的开源 PHP 库，用于请求一堆 SEO 相关指标。
- [SimilarWeb](https://www.similarweb.com/) - 使用SimilarWeb.com 的高级流量估算器工具比较网站流量。查看任何网站的流量来源并发现他们的在线营销策略。
- [SpyFu](https://www.spyfu.com/) - 无限搜索任何竞争对手的 SEO 或 Google Ads 关键字。研究关键词，找到任何领域最强大的内容及其最主要的广告文案。
- [Twitter Analytics](https://analytics.twitter.com/) - 衡量并提升您在 Twitter 上的影响力。
- [Plausible](https://plausible.io/) - Google Analytics 的简单且保护隐私的替代方案。

### 优化

- [Web.dev](https://web.dev/) - 借助 Web.dev 的有用指导和分析，在您自己的网站和应用程序上获取网络的现代功能。无论您已经拥有网站还是刚刚开始，都可以在 Web.dev 上学习如何构建现代网络。
- [PageSpeed Insights](https://developers.google.com/speed/pagespeed/insights/) - Page Speed Insights 衡量移动设备和桌面设备的页面性能。
- [Varvy Seo tool](https://varvy.com/) - 显示：域名强度、链接、图像搜索引擎优化、社交计数和提及、页面/技术搜索引擎优化、页面速度等。
- [Webpagetest.org](https://www.webpagetest.org/) - 网页测试为您提供整体性能瀑布以及网站的渲染时间表。它还提供了对第一个字节的时间以及可能阻碍网页性能的因素的重要见解。
- [WooRank](https://www.woorank.com/) - WooRank 将帮助您解决网站上的问题并寻找机会，让您在竞争中领先。
- [Awesometechstack.com](https://awesometechstack.com/) - AwesomeTechStack 提供有关任何网站技术堆栈的安全性、现代性和性能的见解，以及改进 Web 生命体和技术堆栈的指导。
- [OptimalUX](https://optimalux.com/seo-patching) - 通过无缝 SEO 修补和基于 Cloudflare 构建的 A/B 测试工具来优化您的网站，以便轻松集成。

### 关键词

- [Google Trends](https://www.google.com/trends/) - 使用 Google 趋势探索 Google 热门搜索主题。
- [Keyword Planner](https://adwords.google.com/KeywordPlanner) - 规划您的搜索网络广告系列并了解您的客户正在寻找什么。
- [Keyword Tool](http://keywordtool.io/) - 用于 SEO 和 PPC 关键字研究的 Google 关键字工具的最佳免费替代品！在几秒钟内从 Google Suggest 获取 750 多个相关长尾关键词！
- [Moz Keyword Explorer](https://moz.com/explorer) - 付费关键词工具提供精确的搜索量、关键词难度、SERP 功能和有机点击率数据。
- [Keyword Clarity](https://keywordclarity.io) - 免费的关键字分析工具，可让您使用树形图对关键字指标进行可视化和分组。该工具可处理来自 Google Search Console API 和 CSV 的数据。
- [SEOwl](https://www.seowl.co) - 跟踪您的关键字排名并监控您的反向链接

### 友情链接

- [OpenLinkProfiler](http://www.openlinkprofiler.org/) - 深入分析最新的实时反向链接。
- [Search Engine Spider Simulator](http://tools.seochat.com/tools/search-spider-simulator) - 该工具通过显示网页内容来模拟搜索引擎，其方式与搜索引擎机器人抓取页面时看到的内容完全相同：查看最突出或无法访问的页面元素。
- [Screaming Frog SEO Spider Tool & Crawler Software](https://www.screamingfrog.co.uk/seo-spider/) - Screaming Frog SEO Spider 是一个小型桌面程序（PC 或 Mac），它从 SEO 角度抓取网站链接、图像、CSS、脚本和应用程序。
- [Linkbuilding Spider](https://github.com/fulldecent/linkbuilding-spider) - 一个 PHP 项目，用于检查网站是否链接到您的网站。
- [linkok.com](https://linkok.com) - 在线损坏链接检查应用程序。

### 结构化数据

- [Facebook Debugger](https://developers.facebook.com/tools/debug) - 输入您要抓取的 URL，以查看页面标记在 Facebook 中的显示方式。
- [Pinterest](https://developers.pinterest.com/rich_pins/validator/) - 验证您的 Rich Pin 图并申请将其发布到 Pinterest 上。
- [Structured Data Testing Tool](https://developers.google.com/structured-data/testing-tool/) - 粘贴您的丰富摘要或网址进行测试。
- [Twitter card validator](https://cards-dev.twitter.com/validator) - 输入带有要验证的元标记的页面 URL。

### 小书签

- [OuiSEO](https://github.com/carlsednaoui/seo-bookmarklet) - 一个开源书签，可向您显示页面搜索引擎优化和社交元数据信息。
- [SEO Bookmarklet](https://twkm.ca/projects/seo-bookmarklet) - 一站式 SEO 书签，可快速查看现场 SEO。

### 浏览器扩展

- [MozBar](https://moz.com/tools/seo-toolbar) - Moz 的 SEO 工具栏可让您快速访问许多页面 SEO 因素、域名和页面权限以及快速 nofollow 切换。立即下载免费工具栏！

### Jekyll 插件

- [Jekyll SEO Tag](https://github.com/jekyll/jekyll-seo-tag) - 一个 Jekyll 插件，可为搜索引擎和社交网络添加元数据标签，以更好地索引和显示网站内容。

### TYPO3 扩展

- [Basic SEO Features](https://typo3.org/extensions/repository/view/seo_basics) - 为每页标题标签添加一个单独的字段，在新模块中添加简单且 SEO 友好的关键字和描述编辑以及灵活的 Google 站点地图。
- [Google sitemap](https://typo3.org/extensions/repository/view/dd_googlesitemap) - 高性能 Google 站点地图实现，可避免其他类似扩展的典型错误。

### WordPress 插件

- [All in One SEO Pack](https://wordpress.org/plugins/all-in-one-seo-pack/) - 下载次数最多的 WordPress 插件（近 3000 万次下载）。使用多合一 SEO 包自动针对搜索引擎优化您的网站。
- [Yoast SEO](https://wordpress.org/plugins/wordpress-seo/) - 改善您的 WordPress SEO：使用 Yoast SEO 插件编写更好的内容并拥有完全优化的 WordPress 网站。
- [Slim SEO](https://wordpress.org/plugins/slim-seo/) - 使用轻量级 WordPress SEO 插件为您自动执行 SEO 任务。

## 书籍

- [Search engine optimization 2016: Learn SEO with smart internet marketing strategies](https://www.amazon.com/Search-Optimization-Internet-Marketing-Strategies/dp/151534567X) - 通过 SEO 2016 学习 SEO 策略，在 Google 中排名靠前。
- [Search Engine Optimization All-in-One For Dummies](https://www.amazon.com/Search-Engine-Optimization-All-Dummies/dp/1118921755) - Bruce Clay 是 SEO 社区中最受尊敬的人物之一，在所有主要会议上教授课程和研讨会。就像《SEO 艺术》一样，这本书实际上非常技术性，可能不是您最好的简单入门指南，尽管它是“傻瓜”系列的一部分。
- [SEO 2016: Learn Search Engine Optimization](https://www.amazon.com/SEO-2016-Search-Engine-Optimization/dp/1512275069) - 在当今竞争激烈的搜索环境中，全面的 SEO 必备指南。
- [SEO Fitness Workbook](https://www.amazon.com/SEO-Fitness-Workbook-2016-Optimization/dp/1518748880) - 关于 SEO 的分步书籍，从目标开始，进行页面 SEO（例如页面标签），最后进行页外 SEO（例如链接构建和社交提及）。
- [SEO For Dummies, 6th Edition](http://shop.oreilly.com/product/9781119129554.do) - 您完全更新的搜索引擎优化指南。
- [SEO Step-by-Step - The Complete Beginner's Guide to Getting Traffic from Google](https://www.amazon.com/SEO-Step-Step-Complete-Beginners/dp/1497415020) - 还从关键字开始，涵盖页面搜索引擎优化和页面外搜索引擎优化。强调速度的重要性，并有一个很好的附录，其中包含 SEO 资源、术语表和链接。
- [SEO Warrior](http://shop.oreilly.com/product/9780596157081.do) - 提高网络可见性的基本技术。
- [SEO: Marketing Strategies to Dominate the First Page](https://www.amazon.com/SEO-Marketing-Strategies-analytics-optimization-ebook/dp/B01ACB7LQM) - 介绍 Google Analytics、网站管理员、网站流量、AdWords、按点击付费、网站推广和搜索引擎优化。
- [The Art of SEO, 3rd Edition](http://shop.oreilly.com/product/0636920032908.do) - 掌握搜索引擎优化。
- [The Beginner's Guide to SEO](https://moz.com/beginners-guide-to-seo) - SEO 新手？需要完善你的知识吗？ SEO 初学者指南已被阅读超过 300 万次，提供了您迈向专业品质 SEO 之路所需的信息。
- [The SEO Battlefield](http://shop.oreilly.com/product/0636920050964.do) - 如果您想建立一个持续的 SEO 计划，以增加流量和搜索显着性，本实用的分步指南将帮助您了解 SEO 方法，然后向您展示如何将这些理论付诸实践。

## 课程

- [Analyzing Your Website to Improve SEO](https://www.lynda.com/Marketing-Small-Business-Marketing-tutorials/Analyzing-Your-Website-Improve-SEO/82409-2.html) - 逐步完成审查网站内容和标记的过程，以提高其在搜索引擎结果中的排名。 Lynda.com 与 Peter Kent 合作。
- [ClickMinded](https://www.clickminded.com/) - ClickMinded 是一门 SEO 培训课程，适合希望尽快增加自然流量和销售额的初创公司。
- [Ecommerce SEO 101 Video Series](https://www.shopify.com/videos/ecommerce-seo-101) - Shopify 与 Helen Overland 合作的电子商务 SEO 101 视频系列。
- [Improving SEO Using Accessibility Techniques](https://www.lynda.com/HTML-5-tutorials/Improving-SEO-Using-Accessibility-Techniques/89051-6.html) - 通过适当的标记和网络标准合规性，使网站更易于访问和搜索引擎友好。与 Morten Rand-Hendriksen 合作，作者：Lynda.com。
- [International SEO Fundamentals](https://www.lynda.com/Analytics-tutorials/International-SEO-Fundamentals/377449-6.html) - 利用这些 SEO 技巧吸引国际访问者访问您的网站。了解如何确定目标市场并针对世界各地的国家/地区和语言优化网站的技术方面和内容。 Lynda.com 与 David Booth 合作。
- [Learning Search Engine Optimization (SEO) - A Video Introduction](https://www.video2brain.com/en/courses/learning-search-engine-optimization-seo-a-video-introduction) - 学习搜索引擎优化 (SEO) - video2brain 的 Matt Bailey 视频介绍。
- [Learning Web Analytics](https://www.video2brain.com/en/courses/learning-web-analytics) - 通过 video2brain 与 Matt Bailey 一起学习网络分析。
- [SEO for Beginners](http://seoforbeginners.com/) - SEO 初学者：视频指南介绍。
- [SEO for Ecommerce](https://www.lynda.com/Google-Analytics-tutorials/SEO-Ecommerce/386884-2.html) - 电子商务的 SEO 是不同的。获取专门优化在线商店的策略，以提高页面排名并增加流量。 Lynda.com 与史蒂文·哈里斯 (Steven Harris) 合作。
- [SEO for Local Visibility](https://www.lynda.com/Google-Maps-tutorials/SEO-Local-Visibility/178132-2.html) - 通过这些本地 SEO 策略实现搜索排名的最大可见度。 Lynda.com 的 Brad Batesole。
- [SEO for Web Designers](https://webdesign.tutsplus.com/courses/seo-for-web-designers) - TutsPlus 的 Craig Campbell 为网页设计师提供 SEO。
- [SEO Fundamentals](https://www.lynda.com/Analytics-tutorials/SEO-Fundamentals/187858-2.html) - Lynda.com 的 David Booth 的 SEO 基础知识。
- [SEO Fundamentals](https://www.pluralsight.com/courses/seo-fundamentals) - Pluralsight 的 Paul Wilson 的 SEO 基础知识。
- [SEO Tools Fundamentals](https://www.lynda.com/Buzzstream-tutorials/SEO-Tools-Fundamentals/368917-2.html) - 了解当今用于技术优化、内容优化、站外优化和竞争研究的顶级 SEO 工具。 Lynda.com 的 Brad Batesole。
- [SEO Training Course by Moz](https://www.udemy.com/whiteboard-seo/) - udemy 的 Moz SEO 培训课程。
- [SEO: Keyword Strategy in Depth](https://www.lynda.com/Business-Online-Marketing-tutorials/SEO-Keyword-Strategy-Depth/147030-6.html) - 了解如何研究关键字、将其应用到您的网站以及围绕关键字创建广告活动。通过关键字增加您的网站流量并更好地了解用户的意图。 Lynda.com 与马特·贝利 (Matt Bailey) 合作。
- [SEO: Link Building in Depth](https://www.lynda.com/Business-Online-Marketing-tutorials/SEO-Link-Building-Depth/95253-6.html) - 研究链接的结构、链接如何影响页面排名以及构成优秀入站链接的属性。 Lynda.com 与 Peter Kent 合作。
- [Spying with SEO Tools](https://www.lynda.com/Marketing-PPC-tutorials/Spying-SEO-Tools/371730-6.html) - 了解如何使用 SEO 工具和技术在线研究竞争对手。找出您的竞争对手正在优化哪些关键字，然后在搜索引擎结果页面上超越他们。 Lynda.com 与安森·亚历山大 (Anson Alexander) 合作。
- [WordPress Plugins: SEO](https://www.lynda.com/WordPress-tutorials/WordPress-Plugins-SEO/140779-2.html) - 借助两个强大的插件进行搜索引擎优化 (SEO)，吸引更多访问者访问您的 WordPress 网站。与 Morten Rand-Hendriksen 合作，作者：Lynda.com。

## 执照

[![CC0](https://i.creativecommons.org/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)
