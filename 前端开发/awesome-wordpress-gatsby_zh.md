<div align="center">
  <br /><br />
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat.svg" /></a>
  <br /><br /><br />
  <a href="https://wordpress.org/"><img width="150" height="150" align="center" src="media/wordpress-logo.svg" alt="WordPress"></a>
      <a href="https://www.gatsbyjs.org/"><img width="150" height="150" align="center" src="media/gatsby-logo.svg" alt="Gatsby"></a>
  <br /><br />
  <p>
    <b>
      A curated list of resources about WordPress as a headless CMS with Gatsby as a Static Site Generator (SSG).
    </b>
  </p>
  <br />
</div>

**无头 CMS** 是仅后端的内容管理系统 (CMS)。其目的是提供内容并使其可通过 API（例如 REST 或 GraphQL）进行访问。

**静态站点生成器 (SSG)** 是一个框架或设置，可帮助您生成静态网站 (HTML/CSS/JS)。数据源可以是从本地文件（例如文本文件或 Markdown）到 API（例如 REST、GraphQL）的任何内容。

<br />

**为什么选择 Gatsby 和 WordPress？**

WordPress 是**世界上最常用的 CMS 之一**，因此许多人已经知道如何使用它。在性能至关重要的环境中，使用基于 PHP 的模板的典型前端方法变得越来越有问题。使用 WordPress 作为无头 CMS 并通过 JavaScript 进行正常 API 调用的方法已经存在，但也有一个缺点，即必须向服务器发出请求并根据响应进行渲染。这会增加加载时间。 **Gatsby 相反，在编译时预渲染整个站点**，因此用户在第一次请求时会得到一个**完全准备好的静态站点**，使其成为**性能最佳方法**之一。另一个巨大的好处是**安全性**，因为您的 WordPress 实例可以位于任何地方，甚至是本地，并且您不需要向用户公开任何内容。 **因此，静态 Gatsby 站点是不可破解的。** 在下面的资源中查找有关优点和缺点的更多论点。

## 内容
<!-- TOC -->
- [Communities](#communities)
- [文章和演讲](#articles-and-talks)
- [Plugins](#plugins)
	- [WordPress](#wordpress)
	- [Gatsby](#gatsby)
- [免费教程/课程](#free-tutorials--courses)
	- [书面教程](#written-tutorials)
	- [视频教程](#video-tutorials)
- [付费教程/课程](#paid-tutorials--courses)
- [Starters](#starters)
- [Themes](#themes)
<!-- /TOC -->

## 社区
如果您需要任何帮助，这里有一些非常活跃的社区。

**WPGraphQL**
- [松弛聊天](https://wpgql-slack.herokuapp.com/)
- [频谱聊天](https://spectrum.chat/wpgraphql)
- [Twitter](https://twitter.com/wpgraphql)

**盖茨比**
- [不和谐聊天](https://gatsby.dev/discord)
- [Reddit](https://www.reddit.com/r/gatsbyjs/)
- [堆栈溢出](https://stackoverflow.com/questions/tagged/gatsby)


## 文章和演讲

详细阐述一般技术堆栈的文章和演讲列表。

- 2021.02：[宣布 Gatsby 的新 WordPress 集成](https://www.gatsbyjs.com/blog/wordpress-integration)
- 2021.02：[Jason Bahl 的 WPGraphQL 在网络操作系统中的作用](https://www.youtube.com/watch?v=Me_A0HBYXx8)
- 2021.02：[Torque 新闻发布：Jason Bahl 和 WPGraphQL](https://www.youtube.com/watch?v=8SAdtU8HAwM)
- 2021.02：[Gatsby 推出新的 WordPress 集成，扩展对 Headless 架构的支持](https://wptavern.com/gatsby-launches-new-wordpress-integration-expanding-support-for-headless-architecture)
- 2020.11：[宣布 WPGraphQL v1.0](https://www.wpgraphql.com/2020/11/16/announcing-wpgraphql-v1/)
- 2020.07：[我的解耦 WordPress Gatsby 网站的漫长旅程](https://css-tricks.com/my-long-journey-to-a-de Coupled-wordpress-gatsby-site/)
- 2019.06: [JAMstack 上的现代 Web 开发
](https://www.netlify.com/oreilly-jamstack/) - Netlify 关于 JAMStack 上的现代 Web 开发的报告，由 O'REILLY 发布。


## 插件

让 WordPress 和 Gatsby 协同工作的有用插件列表。按字母顺序排列。

### WordPress

#### 必备插件

- [WPGraphQL](https://github.com/wp-graphql/wp-graphql) - [文档](https://docs.wpgraphql.com/) - WPGraphQL 将 GraphQL 的强大功能带入您的 WordPress 网站。
- [WPGatsby](https://wordpress.org/plugins/wp-gatsby/) - 该插件将您的 WordPress 网站配置为 Gatsby 的优化源。

#### WPGraphQL 扩展

- [WPGraphQL Cors](https://github.com/funkhaus/wp-graphql-cors) - 这个来自 @kidunot89 和 @byfunkhaus 的免费插件声称可以通过允许您设置 GraphQL 接受的 CORS 标头来启用 WPGraphQL 身份验证“正常工作”，这意味着可以接受 WordPress 默认身份验证 cookie。
- [Total Counts for WPGraphQL](https://github.com/builtbycactus/total-counts-for-wp-graphql) - 来自 @builtbycactus 的这个免费插件公开了 WPGraphQL 架构中连接的总计数。
- [WPGraphQL Gutenberg](https://github.com/pristas-peter/wp-graphql-gutenberg) - 将 Gutenberg 块公开给 WPGraphQL API。
- [WPGraphQL JWT Authentication](https://github.com/wp-graphql/wp-graphql-jwt-authentication) - 扩展 WPGraphQL 插件以使用 JWT（JSON Web 令牌）提供身份验证。
- [WPGraphQL Lock](https://github.com/valu-digital/wp-graphql-lock) - 通过实现持久化 GraphQL 查询，为 WPGraphQL 启用查询锁定。
- [WPGraphQL Meta](https://github.com/roborourke/wp-graphql-meta) - 来自 @robertorourke 的这个免费插件将通过 WordPress register_meta API 注册的元公开到 WPGraphQL。
- [WPGraphQL Meta Query](https://github.com/wp-graphql/wp-graphql-meta-query) - 为 WPGraphQL 插件添加 Meta_Query 支持以用于 postObject 查询参数。
- [WPGraphQL Persisted Queries](https://github.com/Quartz/wp-graphql-persisted-queries) - 来自 @qz 的这个免费插件增加了通过 WPGraphQL 使用持久查询的能力。
- [WPGraphQL Offset Pagination](https://github.com/darylldoyle/wp-graphql-offset-pagination) - 来自 @enshrined 的这个免费插件添加了基本的偏移分页，而不是 WPGraphQL 附带的基于标准游标的分页。
- [WPGraphQL Send Email](https://github.com/ashhitch/wp-graphql-send-mail) - 这个来自 @Ash_Hitchcock 的免费插件允许您通过简单的突变发送电子邮件。包括限制发送到受信任来源的能力。

---
**使用 WPGraphQL 的其他插件的扩展**

- [QL Search](https://github.com/funkhaus/ql-search) - 将 SearchWP 集成到 WPGraphQL 中的扩展。
- [WPGraphQL Content Blocks](https://github.com/Quartz/wp-graphql-content-blocks) - 这个来自 QZ.com 人员的免费插件公开了一种从 WordPress 帖子和页面作为“块”（与古腾堡无关）查询 HTML 内容的方法，为您的查询内容带来更多结构。
- [WPGraphQL Enable All Post Types (DalkMania)](https://github.com/DalkMania/wp-graphql-cpt) - 来自 @DalkMania 的这个免费插件会自动将所有注册的帖子类型添加到 WPGraphQL 架构中。
- [WPGraphQL Enable All Post Types (TylerBarnes)](https://github.com/TylerBarnes/wp-graphql-enable-all-post-types) - 来自 @tylbar 的这个免费插件会自动将所有注册的帖子类型添加到 WPGraphQL 架构中。
- [WPGraphQL Google Schema](https://github.com/izzygld/wp-graphql-google-schema) - 来自 @izzygld261 的这个免费插件为 WPGraphQL 添加了 Google Schema 支持。
- [WPGraphQL Gutenberg ACF](https://github.com/pristas-peter/wp-graphql-gutenberg-acf) - 通过 GraphQL 公开 ACF 块
- [WPGraphQL MB (MetaBox)](https://github.com/DalkMania/wp-graphql-mb) - 来自 @DalkMania 的这个免费插件将所有使用 [metabox.io](https://metabox.io/) 注册的元框添加到 WPGraphQL 架构中。
- [WPGraphQL MetaBox Relationships](https://github.com/hsimah-services/wp-graphql-mb-relationships) - 来自 @hsimah 的这个免费插件为 WPGraphQL 添加了对 [metabox.io](https://metabox.io/) 关系字段的支持（当还使用他的 wp-graphql-metabox 插件时）。
- [WPGraphQL Polls](https://github.com/andrenoberto/wp-graphql-polls) - 这个来自 @andrenosouza 的免费插件允许您通过 GraphQL 查询和突变与 WP-Polls 插件中的数据进行交互。
- [WPGraphQL Polylang Extension](https://github.com/valu-digital/wp-graphql-polylang) - 使用 Polylang 插件中的语言数据扩展 WPGraphQL 架构。
- [WPGraphQL Tax Query](https://github.com/wp-graphql/wp-graphql-tax-query) - 为 postObject 查询参数 (WP_Query) 的 WPGraphQL 插件添加 Tax_Query 支持。
- [WPGraphQL WPML](https://github.com/rburgst/wp-graphql-wpml) - 来自 @rburgst 的这个免费插件使用 WPML 插件的语言数据扩展了 WPGraphQL 架构。此外，它还关闭 WPML 默认过滤器，以便能够迭代所有帖子，无论语言如何。
- [WPGraphQL for Advanced Custom Fields](https://github.com/wp-graphql/wp-graphql-acf) - 将高级自定义字段公开给 WPGraphQL 架构。
- [WPGraphQL for BuddyPress](https://github.com/wp-graphql/wp-graphql-buddypress) - 来自 @RenatoNascAlves 的这个免费插件将 BuddyPress 数据公开给 WPGraphQL。
- [WPGraphQL for Carbon Fields](https://github.com/matepaiva/wp-graphql-crb) - 来自 @matepaiva 的这个免费插件将使用 Carbon Fields 注册的字段公开到 WPGraphQL Schema。
- [WPGraphQL for Custom Post Type UI](https://github.com/wp-graphql/wp-graphql-custom-post-type-ui) - 这个免费插件向自定义帖子类型 UI 添加了设置，允许您设置 CPTUI 注册的帖子类型和分类法应显示在 WPGraphQL 架构中。
- [WPGraphQL for FacetWP](https://github.com/hsimah-services/wp-graphql-facetwp) - 来自 @hsimah 的这个免费插件公开了 WPGraphQL 查询上的过滤器，以允许使用 FacetWP 进行分面搜索。
- [WPGraphQL for Gravity Forms](https://github.com/harness-software/wp-graphql-gravity-forms) - 这个来自 @harness_up 的 @KellenMace 的免费插件将 @gravityforms 数据公开到 WPGraphQL，允许您查询表单、字段、条目等。
- [WPGraphQL for Metabox](https://github.com/hsimah-services/wp-graphql-metabox) - 来自 @hsimah 的这个免费插件将使用流行的 http://MetaBox.io 注册到 WPGraphQL 架构的字段公开。
- [WPGraphQL for Ninja Forms](https://github.com/toriphes/wp-graphql-ninja-forms) - 这个免费插件将 Ninja Forms 插件创建的表单公开给 WPGraphQL Schema，并允许通过 GraphQL Mutations 提交表单。
- [WPGraphQL for Posts 2 Posts](https://github.com/harness-software/wp-graphql-posts-to-posts) - 这个来自 @harness_up 的 @KellenMace 的免费插件会自动为您的所有 Posts 2 Posts 连接创建 GraphQL 连接。
- [WPGraphQL for SEOPress](https://github.com/ashhitch/wp-graphql-yoast-seo) - 来自 @moon_meister 的这个免费插件将 SEOPress 管理的数据公开到 WPGraphQL 架构，从而允许在无头应用程序中使用 SEO 数据。
- [WPGraphQL for WooCommerce](https://github.com/wp-graphql/wp-graphql-woocommerce) - 这个免费插件将 WooCommerce 数据公开给 WPGraphQL，允许您通过 GraphQL 查询和突变与商店的数据进行交互。
- [WPGraphQl Yoast SEO Plugin](https://github.com/ashhitch/wp-graphql-yoast-seo) - 将 Yoast SEO 数据公开给 WPGraphQL 插件。


#### 其他有用的插件

- [Advanced Custom Fields](https://wordpress.org/plugins/advanced-custom-fields/) - [ACF PRO](https://www.advancedcustomfields.com/pro/)
- [Headless Mode](https://wordpress.org/plugins/headless-mode/) - 无头模式为所有尝试访问该站点的用户设置重定向。唯一被授予许可的请求是尝试访问 REST API、WP GraphQL API 或任何希望访问无头安装以编辑或创建帖子的登录用户。
- [Polylang](https://wordpress.org/plugins/polylang/)
- [WP JAMstack Deployments](https://github.com/crgeary/wp-jamstack-deployments) - 用于在 Netlify（和其他平台）上部署 JAMstack 的 WordPress 插件。


### 盖茨比插件

- [gatsby-image](https://www.gatsbyjs.org/packages/gatsby-image)
- [gatsby-source-filesystem](https://www.gatsbyjs.org/packages/gatsby-source-filesystem)
- [gatsby-source-wordpress](https://www.gatsbyjs.org/packages/gatsby-source-wordpress)


## 免费教程/课程

**注意：** 自 gatsby-source-wordpress V4 发布以来，它比 gatsby-source-graphql 更受青睐，因此我只会列出与该方法相关的教程。


### 书面教程

- 2019.11：[Gatsby WordPress Starter Advanced with Previews、i18n 等指南](https://dev.to/nevernull/overview-guide-to-gatsby-wordpress-starter-advanced-with-previews-i18n-and-more-583l) - 一系列教程，从 WordPress 和 Gatsby 与 WPGraphQL 的基本设置开始，然后深入到更高级的主题，如部署、预览、i18n 和页面构建器（例如带有 ACF 灵活内容字段的设置）。
- 2019.08：[使用 WordPress 和 Gatsby 进行实时预览](https://justinwhall.com/live-previews-with-wordpress-gatsby/) - 教程展示如何使用主题的高阶组件来促进 WordPress 帖子和自定义帖子类型的预览。
- 2019.08：[Gatsby 与 WPGraphQL、ACF 和 Gatbsy-Image](https://dev.to/nevernull/gatsby-with-wpgraphql-acf-and-gatbsy-image-72m) - 指南，展示如何实现 gatsby-image，以便它可用于 WordPress 媒体文件。
- 2018.08：[Headless WordPress + Gatsby + Netlify 持续部署](https://justinwhall.com/headless-wordpress-gatsby-netlify-continous-deployment/) - 指南展示如何通过几个简单的步骤创建 WordPress + Gatsby + Netlify 设置。


### 视频教程

- 2019.11：[25+ 视频 - Gatsby + WordPress (2019) 完整课程](https://whatjackhasmade.co.uk/series/gatsby-wordpress-2019/) - 该系列重点介绍如何使用 WordPress 作为带有 GraphQL 架构的无头 CMS 进行交互。设置完 WordPress 站点和主题后，我们将转向 Gatsby，以及如何使用新模式为 Gatsby 站点生成内容、以编程方式生成页面、将 Gutenberg 块转换为 React 组件，并以 Gatsby 中的 SEO 为重点结束这一章。
- 2019.07：[Gatsby + WordPress 与 WPGraphQL（与 Jason Bahl） — 与 Jason 一起学习](https://www.youtube.com/watch?v=DH7I1xRrbxs) - 在本次直播中，Jason Bahl 教授如何使用带有高级自定义字段和 WPGraphQL 的 WordPress 创建强大、灵活的管理仪表板，然后在 Gatsby 站点中查询和显示该数据。
- 2019.07：[速成课程：使用 WPGraphQL、ACF 和 React 进行无头 WordPress](https://www.youtube.com/watch?v=9KGuI0UmpMw) - 在本视频中，Alex Young (WPCasts) 介绍了如何使用 WPGraphQL 和 React 进行简单的无头 WordPress 设置。
- 2019.06：[将 WordPress 与 WPGraphQL 结合使用](https://www.youtube.com/watch?v=aqEfEuVWqws) - 在本视频中，您将学习如何使用名为 WPGraphQL 的出色插件和一些额外酷的东西（例如 GraphQL + 高级自定义字段）将 GraphQL 与 WordPress 结合使用。
- 2019.04：[适用于 ACF 的 WPGraphQL](https://www.youtube.com/watch?v=rIg4MHc8elg) - Jason Bahl 展示了如何将 WPGraphQL 用于高级自定义字段。
- 2018.07：[GraphQL 与 WordPress 和 Gutenberg - Jason Bahl - 2018 JavaScript for WordPress 会议
](https://www.youtube.com/watch?v=6CuM1PY9ESQ) - 在 2018 年 WordPress JavaScript 会议的演讲中，WP GraphQL 插件的开发者 Jason Bahl 提供了如何将 GraphQL 与 WordPress 和 Gutenberg 结合使用的最新示例。


## 付费教程/课程
付费课程列表。

- 2021.01：[使用 Gatsby 构建无头 WordPress 网站](https://www.linkedin.com/learning/building-a-headless-wordpress-site-with-gatsby) - 本课程逐步介绍如何使用 gatsby-source-wordpress 插件创建功能齐全的无头 Gatsby WordPress 网站，其中包含帖子、页面、类别、标签、帖子导航和其他功能。


## 初学者
项目启动者列表，您可以克隆并开始构建。

- [Gatsby Starter - WordPress Twenty Twenty](https://github.com/henrikwirth/gatsby-starter-wordpress-twenty-twenty) - 使用新的 gatsby-source-wordpress@v4 将 WordPress Twenty Twenty 主题移植到 Gatsby。
- [Gatsby + WPGraphQL Blog Example](https://github.com/wp-graphql/gatsby-wpgraphql-blog-example) - 演示如何使用 WPGraphQL 作为 Gatsby 站点的源。
- [Gatsby + Headless WordPress + Netlify Starter](https://github.com/justinwhall/gatsby-wordpress-netlify-starter) - 用于持续部署到 Netlify 的 Gatsby + WordPress 入门程序。
- [Gatsby WordPress Starter Advanced](https://github.com/henrikwirth/gatsby-starter-wordpress-advanced) - 高级 Gatsby + WordPress 入门程序，根据教程系列构建，并与 ACF 灵活内容字段一起创建内容块/布局。
- [Gatsby Starter Blog](https://github.com/zeevo/gatsby-starter-wordpress-blog) - 博客入门者具有足够的功能，可以开箱即用地进行生产。

## 主题
以 WordPress 为源的 gatsby 主题列表，您可以在 Gatsby 设置中使用它们。

- [Twenty Nineteen Gatsby Theme](https://github.com/zgordon/twentynineteen-gatsby-theme) - 二十九 WordPress 主题移植到 Gatsby。
- [Gatsby WordPress 发布商主题
](https://github.com/staticfuse/gatsby-theme-publisher) - Gatsby Publisher 主题允许您创建无头（或解耦）的 WordPress 网站。该主题将在基于 React 和 Gatsby 构建的静态前端中显示您的所有页面和帖子。


## 贡献

欢迎投稿！首先阅读[贡献指南](contributing.md)。


## 许可证

[![CC0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0)

在法律允许的范围内，Henrik Wirth 放弃了所有版权和
本作品的相关或邻接权。

<!--- unicorn --->
