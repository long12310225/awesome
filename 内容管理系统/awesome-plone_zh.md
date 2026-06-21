# 很棒的克隆人 [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

<!--lint ignore double-link-->
[<img align="right" src="logo.png" height="64">](https://plone.org)

> 社区精选的 _awesome_ Plone 附加组件列表。

<!--lint ignore double-link-->
[Plone](https://plone.org) 是一个用 Python 编写的开源 CMS，重点关注开箱即用的功能、可定制性和安全性。

<!--lint ignore double-link-->
[Plone on PyPi](https://pypi.org/search/?q=&o=&c=Framework+%3A%3A+Plone) 有超过 3000 个附加组件，GitHub 上的 [Collective](https://github.com/collective) 组织中有超过 1500 个存储库。如果您想知道是否已有适合您需求的 Plone 插件，在 GitHub 或 PyPi 上搜索它可能会很困难。很难理解哪一个可能是一个好的解决方案，或者不是一个好的解决方案。

该列表旨在填补这一空白，并创建有关常见产品和技术的共享知识。

有关从 PyPi 聚合所有 Plone 相关软件包的可过滤插件列表，请参阅 https://pag.derico.tech。

此列表仅涵盖适用于 Plone 最新主要版本（当前为 5.2 和 6）的附加组件以及支持 Python 3 的附加组件。

Plone 6 附带了一个名为 Volto 的新默认前端，它是用 React 编写的，并使用“plone.restapi”与 Plone 进行通信。 Volto 本身具有很强的可扩展性。查看 [awesome-volto 列表](https://github.com/collective/awesome-volto) 了​​解 Volto 的附加组件。


## 内容

* [内容和内容的实用程序](#content-and-utilities-for-content)
* [Editing](#editing)
* [搜索和分类](#searching-and-categorizing)
* [Layout](#layout)
* [Tiles](#tiles)
* [Events](#events)
* [Forms](#forms)
* [Multilingual](#multilingual)
* [Media](#media)
* [Security](#security)
* [SEO](#seo)
* [Authentication](#authentication)
* [Shop](#shop)
* [出口、进口和迁移](#export-import-and-migrations)
* [Themes](#themes)
* [Develop](#develop)
* [Sysadmin](#sysadmin)
* [寻找更多附加组件](#finding-more-add-ons)
* [官方资源](#official-resources)

---

## 内容和内容的实用程序

_提供内容类型或附加内容功能的附加组件_

* [collective.consent](https://github.com/collective/collective.consent) - 在继续之前，请用户同意不同的主题。
* [collective.dexteritytextindexer](https://github.com/collective/collective.dexteritytextindexer) - 灵活内容类型的动态 SearchableText 索引。对于 Plone 6，这已合并到 Plone 核心中。
* [collective.documentgenerator](https://github.com/collective/collective.documentgenerator) - 基于 appy 框架 (https://appyframe.work/) 和 OpenOffice/LibreOffice 从内容生成文档（.odt、.pdf、.doc）。
* [collective.documentviewer](https://github.com/collective/collective.documentviewer) - 非常好的文档查看器，将 DocumentCloud 查看器和 PDF 处理集成到 Plone 中。
* [collective.easyformplugin.createdx](https://github.com/collective/collective.easyformplugin.createdx) - 从 EasyForm 提交创建 Plone 内容对象。
* [collective.embeddedpage](https://github.com/collective/collective.embeddedpage) - 在 Plone Classic 和 Volto 中嵌入远程 HTML 页面的内容类型。
* [collective.folderishtraverse](https://github.com/collective/collective.folderishtraverse) - 遍历到文件夹中的第一项。
* [collective.folderishtypes](https://github.com/collective/collective.folderishtypes) - 提供“Folderish Event”、“Folderish News Item”和“Folderish Document”类型作为默认类型的替换。这些类型能够保存任何其他内容，例如文件夹。
* [collective.geolocationbehavior](https://github.com/collective/collective.geolocationbehavior) - 使用 LeafletJS 对 Plone 内容进行地理标记。
* [collective.glossary](https://github.com/collective/collective.glossary) - 用于定义术语表及其术语的内容类型。
* [collective.immediatecreate](https://github.com/collective/collective.immediatecreate) - 立即创建内容并跳过添加表单。
* [collective.lineage](https://github.com/collective/collective.lineage) - 子站点：将 Plone 站点的子文件夹显示为自主 Plone 站点。还有一个针对子网站的插件的完整生态系统。
* [collective.mailchimp](https://github.com/collective/collective.mailchimp) - Plone 的 MailChimp 时事通讯集成。
* [collective.mirror](https://github.com/collective/collective.mirror) - 镜像任何其他容器内容的内容类型。
* [collective.mustread](https://github.com/collective/collective.mustread) - 跟踪用户对标记为必读内容的查看。
* [collective.person](https://github.com/collective/collective.person) - 代表一个人的内容类型，具有将其连接到 Plone 用户的可选行为。
* [collective.pdfjs](https://github.com/collective/collective.pdfjs) - Mozilla JavaScript PDF 阅读器的 Plone 集成。
* [collective.remoteproxy](https://github.com/collective/collective.remoteproxy) - 远程内容的代理。为其创建本地代理的所有远程 URL 将在结果内容中替换。
* [collective.restrictportlets](https://github.com/collective/collective.restrictportlets) - 允许您限制非管理员可以添加的可用 portlet。
* [collective.workspace](https://github.com/collective/collective.workspace) - 轻松管理克隆站点特定区域的“会员资格”。它允许使用成员资格组而不是每个用户的本地角色来授予人们对内容区域的访问权限，并将对该组的控制权委托给无权访问站点范围的用户/组控制面板的人员。
* [dexterity.membrane](https://github.com/collective/dexterity.membrane) - 使内容能够用作 Plone 站点中的用户和组。
* [plone.pdfexport](https://github.com/plone/plone.pdfexport) - Plone 内容的通用 PDF 导出功能。
* [Products.EasyNewsletter](https://github.com/collective/Products.EasyNewsletter) - 适用于 Plone 的强大新闻通讯/邮件产品。
* [zopyx.ipsumplone](https://github.com/zopyx/zopyx.ipsumplone) - 为 Plone 创建演示内容和演示图像。
* [collective.folderorder](https://github.com/collective/collective.folderorder) - 允许对克隆文件夹进行替代排序。


## 编辑

* [collective.a11ycheck](https://github.com/collective/collective.a11ycheck) - 保存页面时向网站编辑报告可访问性问题。
* [collective.collabora](https://github.com/collective/collective.collabora) - Collabora Online 与 Plone 集成，提供协作文档编辑。
* [collective.bbcodesnippets](https://github.com/collective/collective.bbcodesnippets) - 为 Plone 提供通用且可扩展的 BBCode 标记集成。
* [collective.richdescription](https://github.com/collective/collective.richdescription) - Plone 的可格式化描述字段。


## 搜索和分类

* [cioppino.twothumbs](https://github.com/collective/cioppino.twothumbs) - 使用向上和向下拇指对内容进行评分。
* [collective.bookmarks](https://github.com/collective/collective.bookmarks) - Plone 的书签/收藏夹/愿望清单。
* [collective.collectionfilter](https://github.com/collective/collective.collectionfilter) - 用于集合或内容列表图块的多面导航过滤器。
* [collective.elasticsearch](https://github.com/collective/collective.elasticsearch) - 使用 Elasticsearch 作为 Plone 的搜索后端。
* [collective.elastic.plone](https://github.com/collective/collective.elastic.plone) - Plone 内容的 Elasticsearch 集成。
* [collective.searchandreplace](https://github.com/collective/collective.searchandreplace) - 查找并替换 Plone 内容对象中的文本。
* [collective.solr](https://github.com/collective/collective.solr) - Plone 的 Solr 搜索引擎集成。
* [collective.taxonomy](https://github.com/collective/collective.taxonomy) - 创建、编辑和使用分层分类法对内容进行分类。
* [eea.facetednavigation](https://github.com/collective/eea.facetednavigation) - 非常强大的界面，无需编程技能即可改善搜索。配置是通过网络完成的，让您逐渐选择和探索内容的不同方面（元数据/属性），并快速动态地缩小搜索范围。
* [Products.PloneKeywordManager](https://github.com/collective/Products.PloneKeywordManager) - 更改、合并和删除关键字/标签/主题）。
* [zopyx.typesense](https://github.com/zopyx/zopyx.typesense) - Plon 与外部 Typesense 搜索服务器（开源）集成。这是 Collective.solr 或 Elasticsearch 的替代品。


## 布局

_帮助开发人员和用户创建和管理网站布局的产品和资源。_

* [plone.app.mosaic](https://github.com/plone/plone.app.mosaic) - 强大且可扩展的编辑器，允许用户用不同的图块组成页面内容。
* [collective.cover](https://github.com/collective/collective.cover) - 封面允许围绕拖放界面创建精美的封面。使用与 plone.app.mosaic 相同的块/图块生态系统，但使用不同的编辑方法。
* [collective.contentsections](https://github.com/collective/collective.contentsections) - 为 Plone 6 Classic 提供完全基于 Dexterity 内容类型的块方法。
* [collective.gridlisting](https://github.com/collective/collective.gridlisting) - 通过添加 Bootstrap 5 CSS 类和patternslib 中的“pat-masonry”，添加灵巧行为和浏览器模板来操作文件夹和集合列表。


## 瓷砖

_扩展布局编辑器 plone.app.mosaic._ 的附加组件

* [plone.app.standardtiles](https://github.com/plone/plone.app.standardtiles) - Mosaic 使用的一组标准图块，但可以从任何其他图块管理器中使用。
* [collective.tiles.carousel](https://github.com/collective/collective.tiles.carousel) - 基于 Bootstrap 5 的轮播组件的 plone.app.mosaic 滑块图块。
* [collective.tiles.advancedstatic](https://github.com/collective/collective.tiles.advancedstatic) - 显示 html 文本的图块（类似于静态文本 portlet），具有一些附加配置，例如添加自定义 css 类的可能性。
* [collective.tiles.collection](https://github.com/collective/collective.tiles.collection) - 显示一组集合结果的图块，可以选择（和开发）自定义布局。


## 活动

_处理事件和日历的附加组件._

* [collective.easyformplugin.registration](https://github.com/collective/collective.easyformplugin.registration) - 向 Collective.easyform 添加一个行为来管理活动注册表单。
* [collective.fullcalendar](https://github.com/collective/collective.fullcalendar) - 使用 https://fullcalendar.io 在漂亮的日历 UI 中显示事件。
* [collective.venue](https://github.com/collective/collective.venue) - 具有地理位置支持的场地类型，可与活动或任何其他特定于位置的内容一起使用。


## 表格

_允许生成和使用表单的附加组件._

* [collective.easyform](https://github.com/collective/collective.easyform) - EasyForm 使用字段、小部件、操作和验证器通过网络提供 Plone 表单构建器。表单输入可以保存或通过电子邮件发送。简单且用户友好的界面允许非程序员创建自定义表单。
* [collective.fieldedit](https://github.com/collective/collective.fieldedit) - 用于编辑内容类型的选定字段的灵活表单。
* [collective.honeypot](https://github.com/collective/collective.honeypot) - 表单的蜜罐保护。
* [collective.z3cform.datagridfield](https://github.com/collective/collective.z3cform.datagridfield) - 具有数据网格（表）的字段，其中每一行都是一个子表单。
* [collective.z3cform.norobots](https://github.com/collective/collective.z3cform.norobots) - 基于问题/答案列表的“人类”验证码小部件。
* [plone.formwidgets.hcaptcha](https://github.com/plone/plone.formwidget.hcaptcha) - HCaptcha 小部件可保护 Plone 免受机器人、垃圾邮件和其他形式的自动滥用的侵害。
* [yafowil.plone](https://github.com/bluedynamics/yafowil.plone) - Yafowil 是一个 Python 表单库。这是它的克隆集成包。


## 多语言

_帮助管理多语言网站的附加组件。_

* [collective.linguatags](https://github.com/collective/collective.linguatags) - Plone 的多语言标签。
* [plone.app.multilingualindexes](https://github.com/plone/plone.app.multilingualindexes) - 优化索引以查询使用 plone.app.multilingual 制作的多语言内容。
* [cs.adminlanguage](https://github.com/codesyntax/cs.adminlanguage) - 配置编辑 Plone 站点时使用的语言，独立于站点语言。
* [collective.multilingual](https://github.com/collective/collective.multilingual/tree/fix-tests) - 此附加组件提供对多种语言（多语言）内容的支持。


## 媒体

_处理图像、视频和音频内容的附加组件。_

* [collective.autoscaling](https://github.com/collective/collective.autoscaling) - 大图像自动缩放。当编辑者上传太大的图像时，有助于减小数据库大小。
* [collective.behavior.banner](https://github.com/collective/collective.behavior.banner) - 从横幅创建横幅和滑块的行为。
* [collective.behavior.relatedmedia](https://github.com/collective/collective.behavior.relatedmedia) - 为内容类型创建/上传/管理媒体关系（图像、文件）的行为。
* [collective.lazysizes](https://github.com/collective/collective.lazysizes) - 将lazysizes（一个轻量级惰性加载器）集成到Plone中。
* [collective.wavesurfer](https://github.com/collective/collective.wavesurfer) - 为 Plone 实现 https://wavesurfer-js.org 音频播放器。
* [plone.app.imagecropping](https://github.com/collective/plone.app.imagecropping) - 使用cropper JS 库手动在Plone 中裁剪图像。
* [plone.gallery](https://github.com/plone/plone.gallery) - Plone 的照片库视图。
* [redturtle.gallery](https://github.com/RedTurtle/redturtle.gallery) - 添加带有用光滑制成的轮播的画廊视图。
* [wildcard.media](https://github.com/collective/wildcard.media) - 提供音频和视频内容类型和行为。
* [cs_flickrgallery](https://github.com/codesyntax/cs_flickrgallery) - Flickr 照片库支持 Plone。


## 安全性

* [collective.explicitacquisition](https://github.com/collective/collective.explicitacquisition) - 禁止访问当前路径之外获取的内容。
* [collective.geotransform](https://github.com/collective/collective.geotransform) - Plone 的优雅电子邮件混淆。
* [collective.contactformprotection](https://github.com/collective/collective.contactformprotection) - 禁用默认的“contact-info”表单或使用“plone.formwidget.[h|re]captcha”保护它。
* [collective.lockdown](https://github.com/collective/collective.lockdown) - 保护 Plone 站点，防止站点管理员重新配置站点或更改布局。


## 搜索引擎优化

_用于搜索引擎优化的附加组件。_

* [bda.plone.gtm](https://github.com/bluedynamics/bda.plone.gtm) - 谷歌标签管理器集成。
* [collective.behavior.seo](https://github.com/collective/collective.behavior.seo) - 添加用于 SEO 优化的额外字段。
* [collective.splitsitemap](https://github.com/collective/collective.splitsitemap) - 在大型公共站点上提供缓存的分割站点地图。
* [kitconcept.seo](https://github.com/kitconcept/kitconcept.seo) - 添加用于使用 Volto 的网站进行 SEO 优化的额外字段。


## 认证

_身份验证插件列表，用于将 Plone 与外部用户、Importsources 和 Migrations.import 集成_

* [pas.plugins.ldap](https://github.com/collective/pas.plugins.ldap) - 提供 LDAP 目录中的用户和组。
* [pas.plugins.authomatic](https://github.com/collective/pas.plugins.authomatic) - 自动 OAuth1/OAuth2/OpenID 登录与 Plone 集成。
* [pas.plugins.eea](https://github.com/collective/pas.plugins.eea) - 在 pas.plugins.authomatic 之上提供用户和组枚举，并支持 Microsoft Entra ID。包括用户和组同步。
* [iw.rejectanonymous](https://github.com/collective/iw.rejectanonymous) - 无条件拒绝来自 Plone 站点的匿名用户，无需对安全策略矩阵或工作流程进行任何更改。基本用例是外联网，所有访问者都必须经过身份验证。
* [pas.plugins.headers](https://github.com/collective/pas.plugins.headers) - 读取请求标头并使用它们进行身份验证。想想由 Apache 或 nginx 等前端 Web 服务器设置的 SAML 标头。
* [dm.zope.saml2](https://pypi.org/project/dm.zope.saml2/) - 支持基于 SAML2 的单点登录。
* [collective.impersonate](https://github.com/collective/collective.impersonate) - 允许管理员冒充其他用户。对于验证真实内容上设置的工作流程/权限很有用。
* [collective.pwexpiry](https://github.com/collective/collective.pwexpiry) - 提供了Plone中更强的用户密码和密码攻击防护的方法。
* [pas.plugins.oidc](https://github.com/collective/pas.plugins.oidc) - 使用 OIDC 提供商登录。
* [wcs.samlauth](https://github.com/collective/wcs.samlauth) - 使用 SAML 提供商登录。


## 商店

* [bda.plone.productshop](https://github.com/bluedynamics/bda.plone.productshop) - 适用于 Plone 的灵活且模块化的电子商务解决方案。


## 出口、进口和迁移

* [collective.exportimport](https://github.com/collective/collective.exportimport) - 从 Plone 导出和导入内容以及大量其他数据。基于plone.restapi的各类迁移的主要解决方案。
* [collective.migrationhelpers](https://github.com/collective/collective.migrationhelpers) - 迁移期间使用的帮助程序和示例。
* [collective.jsonify](https://github.com/collective/collective.jsonify) - 将 Plone 内容导出为 JSON。
* [collective.transmogrifier](https://github.com/collective/collective.transmogrifier) - 一个可配置的管道，旨在转换内容以进行导入和导出。


## 主题

* [plonetheme.tokyo](https://github.com/collective/plonetheme.tokyo) - 使用 Bootstrap 5 的 Plone 替代主题。
* [plonetheme.grueezibuesi](https://github.com/collective/plonetheme.grueezibuesi) - Plone 6 的小猫主题。
* [collective.sidebar](https://github.com/collective/collective.sidebar) - 整合工具栏和导航的侧边栏。
* [collective.editablemenu](https://github.com/RedTurtle/collective.editablemenu) - Plone 的可定制导航菜单。
* [collective.localstyles](https://github.com/collective/collective.localstyles) - 通过添加 css 文件在 Plone 站点的任何子部分中添加本地样式。


## 开发

_帮助开发 Plone 的附加组件_

* [Products.PDBDebugMode](https://github.com/collective/Products.PDBDebugMode) - 事后调试：每当发生异常时打开 pdb 会话，以便您可以找出问题所在。另外：通过将 /pdb 添加到 url，您最终会进入当前上下文的 pdb 会话。开发人员的杀手级工具。
* [plone.app.debugtoolbar](https://github.com/plone/plone.app.debugtoolbar) - 一个工具栏，显示有关正在运行的 Plone 站点以及您正在检查的内容的大量调试信息。还包括一个交互式 python-shell、一个 TALES 表达式求值器和代码重新加载。
* [plone.reload](https://github.com/plone/plone.reload) - 无需重新启动服务器即可重新加载代码和配置。
* [Products.PrintingMailHost](https://github.com/collective/Products.PrintingMailHost) - 记录邮件消息而不是发送邮件。
* [experimental.gracefulblobmissing](https://github.com/collective/experimental.gracefulblobmissing/) - 优雅地处理 Plone 中丢失的二进制文件。
* [collective.debugtools](https://github.com/collective/collective.debugtools) - 通过 debugpy 为 VSCode 或 PyCharm 等兼容 debugpy 的客户端添加远程调试。
* [collective.icecream](https://github.com/collective/collective.icecream) - 使用icecream 包调试和检查Plone。
* [collective.patchwatcher](https://github.com/collective/collective.patchwatcher) - 用于跟踪修补或覆盖文件的伴侣。
* [collective.pdbpp](https://github.com/collective/collective.pdbpp) - 允许您使用 pdbpp 包。
* [collective.relationhelpers](https://github.com/collective/collective.relationhelpers) - 在 Plone 5.x 中管理、创建、导出和重建关系的助手。对于 Plone 6，这已合并到 Plone 核心中。


## 系统管理员

_帮助管理员部署和维护 Plone 的附加组件_

* [collective.catalogcleanup](https://github.com/collective/collective.catalogcleanup) - 从目录中删除不再属于实际对象的数据。
* [collective.fingerpointing](https://github.com/collective/collective.fingerpointing) - 跟踪不同的事件并将其写入审核日志。
* [collective.ftw.upgrade](https://github.com/collective/collective.ftw.upgrade) - 简化 Plone 附加组件和项目的编写和运行升级步骤。
* [collective.ifttt](https://github.com/collective/collective.ifttt) - 使任何 Plone 站点都能在 IFTTT 生态系统中发挥作用。例如，当发布新闻时，请发布有关该新闻的推文或将其发布在 Facebook 上。
* [collective.purgebyid](https://github.com/collective/collective.purgebyid) - 在 Plone 中使用基于标签的缓存失效（例如使用 Varnish 的 xkey 模块）。
* [collective.recipe.backup](https://github.com/collective/collective.recipe.backup) - 适用于 Plone 的强大且灵活的备份/恢复解决方案。
* [collective.regenv](https://github.com/collective/collective.regenv) - 使用存储在文件中的环境变量覆盖注册表设置。
* [plone-registryfromenviron](https://github.com/bluedynamics/plone-registryfromenviron) - 覆盖环境变量中的 plone.registry 设置。
* [collective.revisionmanager](https://github.com/collective/collective.revisionmanager) - 管理会使数据库膨胀的 Products.CMFEditions 历史记录。
* [collective.sentry](https://github.com/collective/collective.sentry) - Sentry 集成可聚合错误并帮助查找其原因。
* [dm.historical](https://pypi.org/project/dm.historical) - 访问数据库的任何历史状态。对于查明对象过去发生的情况以及恢复意外删除或修改的对象非常有用。
* [haufe.requestmonitoring](https://github.com/collective/haufe.requestmonitoring) - 发布事件之上的详细请求日志记录功能。有助于找出什么花费的时间比应有的时间长。
* [Cloudbrine](https://bluedynamics.github.io/zodb-pgjsonb/ecosystem.html) - 一组附加组件，用 PostgreSQL 替换 ZODB 和目录，并将对象存储为可查询的 JSONB，并且可以将图像缩放委托给 Thumbor。


## 寻找更多附加组件

找到适合您需求的附加组件有时可能具有挑战性。
以下是一些可以帮助您的提示：

<!--lint ignore double-link-->
* 首先列出您需要的功能。
* 首先检查此列表，看看现有的附加组件是否满足您的需求。
* 在 [PyPi](https://pypi.org/search/?c=Framework+%3A%3A+Plone) 上搜索 Plone 插件。
* 浏览 GitHub 上的 [Collective](https://github.com/collective) 组织。
* 浏览 GitHub 上的 [Plone](https://github.com/plone) 组织。
* 或者直接通过 Google 搜索您的需求。

一旦你有了候选名单，就可以测试这些附加组件。以下是在生产站点上安装附加组件之前需要测试的主要问题：

* 测试所有必需的功能。阅读但不信任文档
* 检查插件是否在您所需的版本上运行
* 检查是否维护
* 它是否支持 i18n，即用户界面是否已翻译成您的语言？
* 是否卸载干净？
* 检查是否存在不需要的依赖项

一旦找到您喜欢的附加组件，您可以询问社区您是否做出了正确的选择或者是否错过了某些内容：

<!--lint ignore double-link-->
* 留言板：[community.plone.org](https://community.plone.org)

如果您找不到 100% 符合您要求的东西，您可以：

* 根据现有情况调整您的要求。
* 投入时间和金钱来定制现有的附加组件，以更好地满足您的需求。
* 创建一个完全满足您需要的新附加组件。

## 官方资源

_因为Plone也有很多好的官方信息资源_

<!--lint ignore double-link-->
* [plone.org](https://plone.org) - 开发者和社区的官方网站。
* [community.plone.org](https://community.plone.org) - 官方社区论坛，获得帮助的最佳场所。
* [Discord chat](https://discord.gg/zFY3EBbjaj) - Discord 是与 Plone 社区成员聊天的最佳方式。
* [Plone support](https://plone.org/support) - 到哪里寻求帮助。
* [docs.plone.org](https://docs.plone.org) - 开发人员/集成商的官方文档。
* [Plone 6 Documentation](https://6.dev-docs.plone.org) - 即将推出的 Plone 6 的官方文档（正在进行中）。
* [training.plone.org](https://training.plone.org) - 面向开发人员/集成商/用户/设计师的培训课程。
* [plone.api](https://6.dev-docs.plone.org/plone.api/index.html) - plone.api 的文档。


## 贡献

欢迎贡献！阅读[贡献指南](contributing.md)。
