# 很棒的 Wagtail [<img src="https://cdn.jsdelivr.net/gh/wagtail/awesome-wagtail@ac912cc661a7099813f90545adffa6bb3e75216c/logo.svg" width="104"align="right" alt="Wagtail">](https://wagtail.org/) [![Awesome](https://cdn.jsdelivr.net/gh/sindresorhus/awesome@d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

> 来自 Wagtail 社区的精彩软件包、文章和其他酷资源的精选列表。
> [Wagtail](https://wagtail.org/) 是一个由 Django 提供支持的 Python CMS，专注于灵活性和用户体验。

_您可能还喜欢 [Awesome Django](https://github.com/wsvincent/awesome-django) 和 [Awesome Python](https://github.com/vinta/awesome-python)。 :蛇:_

## 内容

- [一般资源](#general-resources)
- [Apps](#apps)
  - [Blogging/news](#bloggingnews)
  - [富文本编辑器扩展](#rich-text-editor-extensions)
  - [Widgets](#widgets)
  - [StreamField](#streamfield)
  - [静态站点生成](#static-site-generation)
  - [设置管理](#settings-management)
  - [E-commerce](#e-commerce)
  - [搜索引擎优化和SMO](#seo-and-smo)
  - [客户体验](#customer-experience)
  - [Security](#security)
  - [Media](#media)
  - [Translations](#translations)
  - [Forms](#forms)
  - [Testing](#testing)
  - [Modeladmin](#modeladmin)
  - [内容管理](#content-management)
  - [Misc](#misc)
- [Tools](#tools)
  - [模板和入门套件](#templates--starter-kits)
- [Resources](#resources)
  - [开始使用](#getting-started)
  - [Articles](#articles)
  - [Presentations](#presentations)
  - [Podcasts](#podcasts)
  - [Videos](#videos)
  - [Showcases](#showcases)
  - [包装清单](#package-lists)
- [对于编辑](#for-editors)
- [Community](#community)
- [开源网站](#open-source-sites)

## 一般资源

- [官方网站](https://wagtail.org/)
- [GitHub 存储库](https://github.com/wagtail/wagtail)
- [项目路线图](https://wagtail.org/roadmap/)

## 应用程序

### 博客/新闻

- [Wagtail CRX (CodeRed Extensions)](https://github.com/coderedcorp/coderedcms) - Wagtail + CodeRed 扩展支持快速开发以营销为中心的网站。
- [Puput](https://github.com/APSL/puput) - 在 Wagtail 中实现的 Django 博客应用程序。

### 富文本编辑器扩展

- [Wagtail EditorJS](https://github.com/Nigel2392/wagtail_editorjs) - 一个 [EditorJS](https://editorjs.io/) 小部件，对 Wagtail 的页面、图像和文档选择器提供大力支持。
- [Wagtail Terms](https://github.com/smark-1/wagtailterms) - 用于将术语表术语实体添加到 Draftail 编辑器的插件。
- [wagtailmdx](https://github.com/julinodev/wagtailmdx) - Wagtail 的 [MDXEditor](https://github.com/mdx-editor/editor) 集成作为文本字段小部件。

### 小部件

- [wagtailgmaps](https://github.com/springload/wagtailgmaps) - Wagtail 字段的简单 Google 地图地址格式化程序。
- [Wagtail-Geo-Widget](https://github.com/Frojd/wagtail-geo-widget) - Wagtail 中 GeoDjango PointField 字段的 Google 地图小部件。
- [wagtail-markdown](https://github.com/torchbox/wagtail-markdown) - 对 Wagtail 的 Markdown 支持。
- [wagtail-autocomplete](https://github.com/wagtail/wagtail-autocomplete) - 自动完成“ForeignKey”、“ParentalKey”和“ManyToMany”字段的选择器。
- [wagtail-instance-selector](https://github.com/ixc/wagtail-instance-selector) - 用于创建和选择相关项目的“ForeignKey”小部件。类似于 Django 的 `raw_id_fields`。
- [wagtail-generic-chooser](https://github.com/wagtail/wagtail-generic-chooser) - 提供用于为 Wagtail 管理员构建选择器弹出窗口和表单小部件的基类，与 Wagtail 页面、文档、片段和图像的内置选择器的外观和感觉相匹配。
- [Wagtail-Color-Panel](https://github.com/marteinn/wagtail-color-panel) - 添加用于选择颜色的新面板的包，适用于常规页面字段和流字段。
- [Wagtail Ace Editor](https://github.com/Nigel2392/wagtail_ace_editor) - Ace Editor 就在您的 Wagtail 管理员中。
- [wagtail-html-editor](https://github.com/kkm-horikawa/wagtail-html-editor) - 增强了 Wagtail CMS 的 HTML 编辑器块，具有 CodeMirror 6、语法突出显示、Emmet 支持和全屏模式。

### 流场

- [wagtail-inventory](https://github.com/cfpb/wagtail-inventory) - 按 Wagtail 页面包含的 StreamField 块搜索它们。
- [Wagtail Code Block](https://github.com/wagtail-nest/wagtailcodeblock) - Wagtail CMS 的 StreamField 代码块，具有实时 PrismJS 语法突出显示功能。

### 静态站点生成

- [Wagtail-bakery](https://github.com/wagtail-nest/wagtail-bakery) - 一组帮助程序，用于将 Django Wagtail 站点烘焙为平面文件。

### 设置管理

- [Wagtail-Flags](https://github.com/cfpb/wagtail-flags) - Wagtail 网站的功能标志。

### 电子商务

- [django-salesman](https://github.com/dinoperovic/django-salesman) - 用于 Django 的无头电子商务框架，与 Wagtail modeladmin 集成。

### 搜索引擎优化和SMO

- [wagtail-meta-preview](https://github.com/Frojd/wagtail-meta-preview) - Wagtail Meta Preview 提供了用于在 Wagtail 管理员中预览 Facebook 共享、Twitter 共享和 Google 搜索结果的面板。
- [Wagtail Yoast](https://github.com/Aleksi44/wagtailyoast) - 一种通过 SEO 建议提高文本可读性的工具。
- [Wagtail SEO](https://github.com/coderedcorp/wagtail-seo) - Wagtail 的搜索引擎和社交媒体优化。

### 客户体验

- [Wagtail Experiments](https://github.com/torchbox/wagtail-experiments) - Wagtail 的 A/B 测试。
- [Wagtail Personalisation](https://github.com/wagtail-nest/wagtail-personalisation) - 个性化模块，使编辑者能够根据其规则直接在管理界面中配置的片段创建自定义页面或页面的一部分。

### 安全性

- [wagtail-2fa](https://github.com/labd/wagtail-2fa) - 通过与 django-otp 集成，向 Wagtail 添加双因素身份验证。

### 媒体

- [wagtailmedia](https://github.com/torchbox/wagtailmedia) - 用于在管理员内管理视频和音频文件的 Wagtail 模块。
- [Wagtail Transcription](https://github.com/j-bodek/wagtail-transcription) - 提供一个字段来自动从 YouTube 视频创建转录。

### 翻译

- [Wagtail Localize](https://github.com/wagtail/wagtail-localize) - Wagtail CMS 的翻译插件。
- [Wagtail Modeltranslation](https://github.com/infoportugal/wagtail-modeltranslation) - 包含 mixin 模型的简单应用程序，该模型将 [django-modeltranslation](https://github.com/deschler/django-modeltranslation) 集成到 Wagtail 面板系统中。

### 表格

- [Wagtail 内置的表单生成器](https://docs.wagtail.org/en/stable/reference/contrib/forms/) 适用于一般用例。
- [Wagtail ReCaptcha](https://github.com/wagtail-nest/wagtail-django-recaptcha) - wagtail-django-captcha 提供了一种在使用 Wagtail formbuilder 时集成 [django-recaptcha](https://github.com/django-recaptcha/django-recaptcha) 字段的简单方法。
- [Wagtail Jotform](https://github.com/torchbox/wagtail-jotform) - 在 wagtail 中使用 jotforms 的插件。
- [Wagtail Model Forms](https://github.com/vicktornl/wagtail-model-forms) - Wagtail Form Builder 功能可用于您的模型/片段。
- [Wagtail Formation](https://github.com/mwesterhof/wagtail_formation) - 完全动态且易于使用的 CMS 表单，适用于 wagtail

### 测试

- [wagtail-linkchecker](https://github.com/neon-jungle/wagtail-linkchecker) - 一种帮助查找 Wagtail 网站上损坏链接的工具。
- [Wagtail Accessibility](https://github.com/wagtail-nest/wagtail-accessibility) - ✅ Wagtail 网站的可访问性内容检查。
- [Wagtail Factories](https://github.com/wagtail/wagtail-factories) - 工厂男孩为鹡鸰上课。

### 模型管理员

- [wagtail-admin-list-controls](https://github.com/ixc/wagtail-admin-list-controls) - 向 Wagtail 的 modeladmin 列表视图添加高级搜索、排序和布局控件。
- [Wagtail Rangefilter](https://github.com/wunderweiss/wagtail-rangefilter) - 将 django-admin-rangefilter 集成到 Wagtail 的 ModelAdmin 中。
- [Wagtail-TreeModelAdmin](https://github.com/cfpb/wagtail-treemodeladmin) - Wagtail 的 ModelAdmin 的扩展，用于 Django 模型关系的类似页面浏览器的导航。

### 内容管理

- [Wagtail Sharing](https://github.com/cfpb/wagtail-sharing) - 更轻松地共享 Wagtail 草稿。
- [Wagtail Transfer](https://github.com/wagtail/wagtail-transfer) - Wagtail 的官方扩展，允许在 Wagtail 项目的多个实例之间传输内容
- [Wagtail Content Import](https://github.com/torchbox/wagtail-content-import) - 使用可自定义的映射系统将内容从 Google Docs 或 Docx 导入 StreamFields。
- [Wagtail Headless Preview](https://github.com/torchbox/wagtail-headless-preview) - 无头 Wagtail 设置预览
- [Wagtail-FEdit](https://github.com/Nigel2392/wagtail_fedit) - 将前端编辑添加到您的 Wagtail 网站。

### 杂项

- [wagtailmenus](https://github.com/jazzband/wagtailmenus) - 一款可帮助您更有效地管理和渲染 Wagtail 项目中的菜单的应用程序。
- [Wagtail Gridder](https://github.com/wharton/wagtailgridder) - 网格卡布局类似于 Google 图像搜索结果，具有扩展的卡片详细信息区域。
- [Wagtail App Pages](https://github.com/mwesterhof/wagtail_app_pages) - 使用实际的 URL 配置和 django 视图扩展 Wagtail 页面。
- [Wagtail Cache](https://github.com/coderedcorp/wagtail-cache) - 使用 Django 缓存中间件的 Wagtail 的简单页面缓存。
- [Wagtail Orderable](https://github.com/elton2048/wagtail-orderable) - Mixin 支持管理面板中的拖放排序。
- [Wagtail Resume](https://github.com/adinhodovic/wagtail-resume) - Wagtail 项目旨在简化开发人员简历的创建。
- [Wagtail Trash](https://github.com/Frojd/wagtail-trash) - 按删除键时，页面不会被删除，而是会被扔进“垃圾桶”。
- [wagtail-pdf-view](https://github.com/donhauser/wagtail-pdf) - Wagtail CMS 的 PDF 渲染视图。
- [Wagtail Grapple](https://github.com/torchbox/wagtail-grapple) - 一款 Wagtail 应用程序，让构建 GraphQL 端点变得轻而易举。
- [Wagtail Cache Invalidator](https://github.com/vicktornl/wagtail-cache-invalidator) - 通过 Wagtail CMS 中的用户友好界面使缓存失效并清除（前端）缓存。

## 工具

### 模板和入门套件

- [Pipit](https://github.com/Frojd/Wagtail-Pipit) - Pipit 是一个 Wagtail CMS 样板，旨在通过 React 渲染的前端提供简单而现代的开发人员工作流程。
- [cookiecutter-wagtail-package](https://github.com/wagtail/cookiecutter-wagtail-package) - 用于构建 Wagtail 附加包的 cookiecutter 模板。
- [Wagtail for Platform.sh](https://github.com/platformsh-templates/wagtail) - Platform.sh 的 Wagtail 模板。
- [cookiecutter-wagtail-vix](https://github.com/engineervix/cookiecutter-wagtail-vix) - 一个最小的、包含电池的、可重复使用的项目框架，作为 Wagtail 项目的起点。
- [Sites Conformes](https://github.com/numerique-gouv/sites-conformes) - 国家设计系统的永久内容和安全管理基于互联网。 Wagtail CMS 基地。

### 模板（启动命令）

- [Wagtail template: Your first Wagtail site](https://github.com/thibaudcolas/wagtail-tutorial-template) - Wagtail 项目入门模板 – 包含 Wagtail 官方“您的第一个 Wagtail 站点”教程的解决方案。
- [Wagtail News Template](https://github.com/wagtail/news-template) - 新闻网站的 Wagtail 模板。

## 资源

### 开始使用

- [Getting started in Wagtail, a newcomer's perspective](https://wagtail.org/blog/getting-started-wagtail-newcomers-perspective/) - 一段时间以来，我几乎完全使用 Drupal 作为我选择的主要工具，我被要求使用 Wagtail 构建一个版本。
- [Présentation de Wagtail, le dernier CMS Django](https://makina-corpus.com/django/presentation-de-wagtail-le-dernier-cms-django) - Wagtail 是最近与 Django 生态系统相关的 CMS。无论如何，我的儿子年轻时就拥有了这些文章中的功能。
- [Getting Started With Wagtail](https://vix.digital/insights/getting-started-wagtail/) - 我们与 Wagtail 及周边社区广泛合作，发现了开发人员在开始使用 Wagtail 交付时遇到的一系列常见陷阱。

### 文章

- [Wagtail Tutorials: Build Blog Step by Step](https://saashammer.com/blog/wagtail-tutorials/) - 这些教程将教您如何从头开始一步步创建标准博客。
- [Multi-tenancy with Wagtail](https://cynthiakiser.com/blog/2023/11/01/multitenancy-with-wagtail.html) - 有关 Wagtail 中强大的多租户支持的多部分指南。
- [如何防止用户按类型创建页面](https://timonweb.com/wagtail/how-to-prevent-users-from-creating-certain-page-types-in-wagtail-cms/)
- [如何创建和管理 Wagtail 应用程序的菜单](https://saashammer.com/blog/how-to-create-and-manage-menus-in-wagtail/)

### 演讲

- [Wagtail 简介](https://www.youtube.com/watch?v=glIIF-kBXf0)，作者：Eloise "Ducky" Macdonald-Meyer - 本演讲介绍 Wagtail，这是一个基于 Python Web 框架 Django 构建的内容管理系统。
- Tom Dyson 的 [DjangoCon US 2015 - Wagtail - Yet Another Django CMS](https://www.youtube.com/watch?v=6j0NVq6g4FE) - Tom 将解释为什么他的机构决定构建一个新的 CMS，分享在运行不断发展的开源项目中学到的一些经验教训，并概述 Wagtail 的版本 2 及更高版本的路线图。 [幻灯片](https://speakerdeck.com/tomdyson/wagtail-yet-another-cms-djangocon-us-2015)。
- Springload 开发团队的 Josh、Jordi 和 Rich 举办的 [惠灵顿 Wagtail CMS 聚会 - 认识 Wagtail](https://docs.google.com/presentation/d/19EGWFtfHovHSAvyHCnLbxK50IAR2o7WwKd709cqi9p4/edit) - Wagtail 的介绍性会议，展示其提供的主要功能。
- [DjangoCon US 2016 - Atomic Wagtail](https://www.youtube.com/watch?v=kqAKiouk1lY) 作者：Kurt Wall – Brad Frost 的原子设计原则正在席卷我们设计 Web 的方式。我将解释什么是 Wagtail、如何根据原子设计原则使用它、以及在此过程中可能遇到的一些障碍以及如何提供帮助的建议。
- [PyCon Australia – 比较 Wagtail、Django CMS 和 Mezzanine](https://www.youtube.com/watch?v=3UC1MNFOjEI)，作者：Adam Brenecki – 本演讲探讨了每种 CMS 的不同方法、优点和缺点，以及它们对开发人员和内容编辑者的意义。
- [Wagtail — еще одна CMS на Django](https://www.youtube.com/watch?v=yRmZ6WUfoOc) 作者：Mikalai Radchuk - 本演讲用俄语介绍 Wagtail。
- [Wagtail 与敏捷 – Wagtail Space 2017](https://www.youtube.com/watch?t=2m21s&v=-Qii_AyQsxE) 作者：Edd Baldry。
- [将 Wagtail 部署到 Divio 云 – Wagtail Space 2017](https://www.youtube.com/watch?t=38m13s&v=-Qii_AyQsxE)，作者：Daniele Procida。
- [关于 Wagtail 的一切 – Wagtail Space 2017](https://www.youtube.com/watch?v=OedQi5W3Zho) 作者：Robin van der Rijst。
- [推出 Wagtail Clear StreamField，一款模块化 StreamField 应用程序 – Wagtail Space 2017](https://www.youtube.com/watch?t=19m1s&v=OedQi5W3Zho)，作者：Edd Baldry。
- [Wagtail 实验，为您的 Wagtail 网站进行简单的 A/B 测试 – Wagtail Space 2017](https://www.youtube.com/watch?t=34m37s&v=OedQi5W3Zho)，作者：Tom Dyson。
- [Wagtail 预览，新希望 – Wagtail Space 2017](https://www.youtube.com/watch?v=ObM2pUgY-bs) 作者：Bertrand Bordage。
- [鹡鸰之禅 –鹡鸰空间 2017](https://www.youtube.com/watch?t=16m38s&v=ObM2pUgY-bs) 作者：Matt Westcott。
- [Plone to Wagtail – Wagtail Space 2017](https://www.youtube.com/watch?t=2m57s&v=hZcuq8WJVew)，作者：Coen van der Kamp。
- [数百只鹡鸰飞行 – Wagtail Space 2017](https://www.youtube.com/watch?t=24m9s&v=hZcuq8WJVew) 作者：Simon de Haan。
- [Google 如何使用 Wagtail – Wagtail Space 2018](https://www.youtube.com/watch?v=lh9nmN1mzwQ&t=1937s) 作者：Kevin Chung。
- [在 Wagtail 中引入 Draft.js – Wagtail Space 2018](https://www.youtube.com/watch?v=lh9nmN1mzwQ&t=2690s)，作者：Thibaud Colas。 [演示](https://thib.me/introducing-draft-js-in-wagtail)。
- [Let It Go – Wagtail Space 2018](https://www.youtube.com/watch?v=lh9nmN1mzwQ&t=3938s) 作者：Matt Wescott。
- [为女孩开发解决方案，男性 – Wagtail Space 2018](https://www.youtube.com/watch?v=lh9nmN1mzwQ&t=5184s)，作者：Lisa Adams。
- [Wagtail 的第一次孵化 – Wagtail Space 2018](https://www.youtube.com/watch?v=P8RUQE7Djdg&t=265s)，作者：Bertrand Bordage。
- [单词问题 – Wagtail Space 2018](https://www.youtube.com/watch?v=P8RUQE7Djdg&t=2841s)，作者：Tom Dyson。
- [Divio Cloud 上的 Wagtail – Wagtail Space 2018](https://www.youtube.com/watch?v=P8RUQE7Djdg&t=3856s)，作者：Daniele Procida。
- [将鹡鸰的头砍下来然后粘回去 – Wagtail Space 2018](https://www.youtube.com/watch?v=u0CPaXRSOzI&t=152s)，作者：托尼·耶茨 (Tony Yates)。
- [UWKM 的 StreamField 编辑 – Wagtail Space 2018](https://www.youtube.com/watch?v=u0CPaXRSOzI&t=400s)，作者：Geert jan Hoogeslag。
- [我在 Wagtail Space 学到的东西 – Wagtail Space 2018](https://www.youtube.com/watch?v=u0CPaXRSOzI&t=719s) 作者：Codie Roelf。
- [将 Wagtail 飞向 PyCon – Wagtail Space 2018](https://www.youtube.com/watch?v=u0CPaXRSOzI&t=912s)，作者：Daniele Procida。
- [Wagtail 表演 – Wagtail 空间 2018](https://www.youtube.com/watch?v=u0CPaXRSOzI&t=1345s)，作者：Michael van Tellingen。 [代码](https://gist.github.com/mvantellingen/daebda6abbaa9a5ed0888f886a77fcf0)。
- [多图片上传器 – Wagtail Space 2018](https://www.youtube.com/watch?v=u0CPaXRSOzI&t=1661s) 作者：Rajeev J Sebastian。
- [Wagtail Space 复活节彩蛋团队演示 – Wagtail Space 2018](https://www.youtube.com/watch?v=u0CPaXRSOzI&t=2057s)，作者：Lars。 [代码](https://github.com/specialunderwear/haunted-wagtail)。
- [Wagtail 空间 2019 – Wagtail 空间 2018](https://www.youtube.com/watch?v=u0CPaXRSOzI&t=2278s) 作者：Maarten Kling。
- [Wagtail 2018 – Wagtail Space US 2018](https://www.youtube.com/watch?v=ICKYMO0YoFI&index=2&list=PLEyaio0l1qoGGbXg3XH0205FIF32oO1wV) 作者：Tom Dyson。
- [Wagtail 文档没有告诉您的内容 – Wagtail Space US 2018](https://www.youtube.com/watch?v=PCkxBNXWM64&index=3&list=PLEyaio0l1qoGGbXg3XH0205FIF32oO1wV)，作者：Lacey Williams Henschel。
- [Wagtail 的 Django 日志记录 – Wagtail Space US 2018](https://www.youtube.com/watch?v=kkztl9ORUKQ&list=PLEyaio0l1qoGGbXg3XH0205FIF32oO1wV&index=4)，作者：Ryan Sullivan。
- [为 1 亿女孩扩展 Wagtail – Wagtail Space US 2018](https://www.youtube.com/watch?v=AiOJAKE0M0I&index=5&list=PLEyaio0l1qoGGbXg3XH0205FIF32oO1wV)，作者：Lisa Adams 和 Codie Roelf。
- [使用 Wagtail 争取新闻自由 – Wagtail Space US 2018](https://www.youtube.com/watch?v=FYqbqsa04T8&list=PLEyaio0l1qoGGbXg3XH0205FIF32oO1wV&index=6) 作者：Harris Lapiroff。
- [为哥伦比亚大学选择 Wagtail – Wagtail Space US 2018](https://www.youtube.com/watch?v=OiZScRcluCo&list=PLEyaio0l1qoGGbXg3XH0205FIF32oO1wV&index=7)，作者：Zarina Mustapha。
- [在 Wagtail 中运行多站点新闻编辑室 – Wagtail Space US 2018](https://www.youtube.com/watch?v=lMCjInjAz-M&list=PLEyaio0l1qoGGbXg3XH0205FIF32oO1wV&index=8)，作者：Ryan Verner。
- [云中的 Wagtail – Wagtail Space US 2018](https://www.youtube.com/watch?v=N1MeTEPRmJA&index=9&list=PLEyaio0l1qoGGbXg3XH0205FIF32oO1wV)，作者：Daniele Procida。
- [斩首 Wagtail：Wagtail 作为无头 CMS – Wagtail Space US 2018](https://www.youtube.com/watch?v=HZT14u6WwdY&index=10&list=PLEyaio0l1qoGGbXg3XH0205FIF32oO1wV)，作者：Michael Harrison。
- [学习 Wagtail – Wagtail Space US 2018](https://www.youtube.com/watch?v=C-tXt5fLj_s&index=11&list=PLEyaio0l1qoGGbXg3XH0205FIF32oO1wV)，作者：Dawn Wages。
- [分享即关怀 – Wagtail Space US 2018](https://www.youtube.com/watch?v=6AXyg6vvMTE&index=12&list=PLEyaio0l1qoGGbXg3XH0205FIF32oO1wV)，作者：Andy Chosak。
- [闪电演讲 – Wagtail Space US 2018](https://www.youtube.com/watch?v=uoxyBIpaXTU&index=13&list=PLEyaio0l1qoGGbXg3XH0205FIF32oO1wV)
- [Wagtail: когда хочется чего-то приятнее, чем просто Django – 莫斯科 Python Conf++ 2018](https://www.youtube.com/watch?v=xPPfTvLS7oQ) 作者：Игорь Мосягин
- [鹡鸰的状态 – Wagtail Space 2019](https://www.youtube.com/watch?t=592&v=MAzZ2lhMhzM) 作者：Tom Dyson。
- [图像旋转功能 – Wagtail Space 2019](https://www.youtube.com/watch?t=2057&v=MAzZ2lhMhzM) 作者：Chris Adams。代码。
- [调试模板 – Wagtail Space 2019](https://www.youtube.com/watch?t=2264&v=MAzZ2lhMhzM)，作者：Coen van der Kamp。
- [Wagtail Headless with HATEOAS – Wagtail Space 2019](https://www.youtube.com/watch?t=2567&v=MAzZ2lhMhzM)，作者：Duco Dokter。
- [构建地球友好网络（与 Wagtail）– Wagtail Space 2019](https://www.youtube.com/watch?t=2926&v=MAzZ2lhMhzM) 作者：Chris Adams。
- [\[WIP\] Wagtail 中（富文本）创作体验的未来 – Wagtail Space 2019](https://www.youtube.com/watch?t=4067&v=MAzZ2lhMhzM)，作者：Thibaud Colas。
- [Wagtail 和 Whatsapp – Wagtail 空间 2019](https://www.youtube.com/watch?t=47&v=CSwpj-jyjP4)，丽莎·亚当斯 (Lisa Adams) 和科迪·罗尔夫 (Codie Roelf)。
- [Slack2Wagtail – Wagtail Space 2019](https://www.youtube.com/watch?t=785&v=CSwpj-jyjP4)，作者：Coen van der Kamp 和 Lucas Moeskops。
- [Wagtail 和 Oscar – Wagtail Space 2019](https://www.youtube.com/watch?t=1634&v=CSwpj-jyjP4) 作者：Lars van de Kerkhof。
- [wagtail-textract – Wagtail Space 2019](https://www.youtube.com/watch?t=3313&v=CSwpj-jyjP4)，作者：Kees Hink。 [代码](https://github.com/fourdigits/wagtail_texttract)。
- [Django 2.2 兼容性 – Wagtail Space 2019](https://www.youtube.com/watch?t=3468&v=CSwpj-jyjP4) 作者：Matt Wescott。
- [SEO 仪表板 – Wagtail Space 2019](https://www.youtube.com/watch?t=3937&v=CSwpj-jyjP4) 作者：Janneke Janssen。 [代码](https://github.com/LUKKIEN/wagtail-marketing-addons)。
- [我的第一个 Wagtail 贡献 – RichText 编辑器中的更多格式 – Wagtail Space 2019](https://www.youtube.com/watch?t=4126&v=CSwpj-jyjP4)，作者：Arifin Ibne Matin。
——【飞吧，鹡鸰，飞吧！ – Wagtail Space 2019](https://www.youtube.com/watch?t=4404&v=CSwpj-jyjP4) 作者：Daniele Procida。
- [Wagtail 和 GraphQL – Wagtail Space 2019](https://www.youtube.com/watch?t=24&v=YydSbL8gMS4) 作者：Arthur Bayr。
- [作者写作（代码） - Wagtail Space US 2019](https://www.youtube.com/watch?v=Ihsrki0d1G8&list=PLEyaio0l1qoEIUFM9bnRKoN6VKEUOdxAn&index=1) 作者：Brian Smith 和 Eric Sherman。 [幻灯片](https://docs.google.com/presentation/d/1z61u0uKwJxmYS4Zawbu4Zgg-kCtInd1VgsEg-rnwzBE/edit)。
- [用 Wagtail 拯救生命：世界各地的恢复会议 – Wagtail Space US 2019](https://www.youtube.com/watch?v=QlLWvNT5Wrk&list=PLEyaio0l1qoEIUFM9bnRKoN6VKEUOdxAn&index=2) 作者：Timothy Allen。
- [为什么我们为 CodeRed CMS 选择 Wagtail – Wagtail Space US 2019](https://www.youtube.com/watch?v=1JUOAmLQFA&list=PLEyaio0l1qoEIUFM9bnRKoN6VKEUOdxAn&index=3) 作者：Vince Salvino。
- [构建基于 Wagtail 的网站和创作环境并考虑到可访问性 – Wagtail Space US 2019](https://www.youtube.com/watch?v=CxjlAI6R7iY&list=PLEyaio0l1qoEIUFM9bnRKoN6VKEUOdxAn&index=4)，作者：Zarina Mustapha。
- [让 Wagtail 无障碍 – Wagtail Space US 2019](https://www.youtube.com/watch?v=tdB1I_gSCeY&list=PLEyaio0l1qoEIUFM9bnRKoN6VKEUOdxAn&index=5) 作者：Thibaud Colas。 [幻灯片](https://docs.google.com/presentation/d/15y8XIe7SL-RYEO9tEE8n9chx80_X4j4PbczGGM-cEGE/edit)。
- [每个人都可以悬挂旗帜 – Wagtail Space US 2019](https://www.youtube.com/watch?v=ZqwmgsqMTEs&list=PLEyaio0l1qoEIUFM9bnRKoN6VKEUOdxAn&index=6)，作者：Will Barton。 [幻灯片](https://docs.google.com/presentation/d/1-A1doke2ylcqG72oIP-MLiX8SKXKkKNxQeKxddYUGBw/edit)。
- [多域网站架构 – Wagtail Space US 2019](https://www.youtube.com/watch?v=xMbJmHF7kCw&list=PLEyaio0l1qoEIUFM9bnRKoN6VKEUOdxAn&index=7) 作者：Ben Beecher。 [幻灯片](https://slides.com/benbeecher/mds/)。
- [贡献不仅仅是代码 – Wagtail Space US 2019](https://www.youtube.com/watch?v=tK-3kEBbblg&list=PLEyaio0l1qoEIUFM9bnRKoN6VKEUOdxAn&index=8)，作者：Kalob Taulien。
- [深思熟虑的代码审查 – Wagtail Space US 2019](https://www.youtube.com/watch?v=RY0K1BEV-_U&list=PLEyaio0l1qoEIUFM9bnRKoN6VKEUOdxAn&index=9)，作者：Naomi Morduch Toubman。 [幻灯片](https://docs.google.com/presentation/d/1b_Hda8381G6mMc7uzYDc2EYjocfwSi2TYiRMI7d4e3I/edit)。
- [通过探索 Wagtail 代码来解决您的问题 – Wagtail Space US 2019](https://www.youtube.com/watch?v=BMoOhjgirFM&list=PLEyaio0l1qoEIUFM9bnRKoN6VKEUOdxAn&index=10) 作者：Harris Lapiroff。 [幻灯片](https://harrislapiroff.github.io/wagtail-space-us-2019/)
- [Wagtail 状态：2019 – Wagtail Space US 2019](https://www.youtube.com/watch?v=s29vaGnFcq8&list=PLEyaio0l1qoEIUFM9bnRKoN6VKEUOdxAn&index=11)，作者：Tom Dyson。
- [Wagtail 指南 - 入门 - Wagtail Space US 2022](https://www.youtube.com/watch?v=E3-kFY6jPPY)，作者：Coen van der Kamp。
- [多租户 Wagtail 的新方法 - Wagtail Space US 2022](https://www.youtube.com/watch?v=WN0L4YNrWes)，作者：Stephanie C. Smith 和 Addison Hardy。
- [基于游戏的课程的 Wagtail 市场 - Wagtail Space 2022](https://www.youtube.com/watch?v=ueou6CxiR3Y)，作者：Sarah Toms。
- [Wagtail 生态系统 - Wagtail Space US 2022](https://www.youtube.com/watch?v=4Qd43nsxmoc) 作者：Vince Salvino。
- [Wagtail 图表和图表 - Wagtail Space US 2022](https://www.youtube.com/watch?v=QK-Vhlpos3Q)，作者：Sævar Öfjörð Magnússon 和 Arnar Tumi Þorsteinsson。
- [Wagtail 作为 JavaScript 前端的无头 CMS - Wagtail Space US 2022](https://www.youtube.com/watch?v=bYRQ492BED0)，作者：Tommaso Amici。
- [向 Wagtail 添加 GraphQL API - Wagtail Space US 2022](https://www.youtube.com/watch?v=_O5isU354vg)，作者：Patrick Arminio。
- [将 JSONField 引入 Wagtail 核心 - Wagtail Space US 2022](https://www.youtube.com/watch?v=XtazMDNdlK8)，作者：Sage Abdullah。
- [Wagtail 与 WordPress - Wagtail Space US 2022](https://www.youtube.com/watch?v=Vl2g7H3aodw)，作者：Kalob Taulien。
- [设计新页面编辑器 - Wagtail Space US 2022](https://www.youtube.com/watch?v=t2xiPJ91UCE)，作者：Phil Dexter 和 Ben Enright。
- [我从艰难的方式中学到的有关 Wagtail 的 5 件事 - Wagtail Space US 2022](https://www.youtube.com/watch?v=LNqVzLkZkig) 作者：Meagen Voss。
- [维护 Wagtail 软件包的技巧 - Wagtail Space US 2022](https://www.youtube.com/watch?v=Zh608nVBrEw) 作者：Tim Allen。
- [Wagtail 指南 - Wagtail Space US 2022](https://www.youtube.com/watch?v=W0tL-5V5BWA)，作者：Coen van der Kamp。
- [Wagtail 2022 年状态 - Wagtail Space NL 2022](https://www.youtube.com/watch?v=4D49RENHfoM) 作者：Tom Dyson。
- [选择者 - Wagtail Space NL 2022](https://www.youtube.com/watch?v=nSjVAISLr4M)，作者：Matthew Westcott。
- [使用图像滤镜 - Wagtail Space NL 2022](https://www.youtube.com/watch?v=gCGT51BcTdM)，作者：Arnar Tumi Þorsteinsson。
- [我学到的东西 - Wagtail Space NL 2022](https://www.youtube.com/watch?v=xG5-s48TZt8) 作者：Dan Braghis。
- [Wagtail Roadrunner Beep Beep - Wagtail Space NL 2022](https://www.youtube.com/watch?v=ynlFUcutSWQ)，作者：Lars van de Kerkhof。
- [5 分钟内 Docker 化 wagtail 项目 - Wagtail Space NL 2022](https://www.youtube.com/watch?v=PgkpBMoN4UY)，作者：Sævar Öfjörð Magnússon。
- [新闻室中的 Wagtail - Wagtail Space NL 2022](https://www.youtube.com/watch?v=B85HwmX5uaw)，作者：Sævar Öfjörð Magnússon 和 Arnar Tumi Þorsteinsson。
- [数字游牧者 - Wagtail Space NL 2022](https://www.youtube.com/watch?v=9Evrwzpg-dw)，作者：Maikel Martens。
- [低调的国际化 - Wagtail Space NL 2022](https://www.youtube.com/watch?v=_dhScxTdtjA)，作者：Lars van de Kerkhof。
- [移动 Wagtail 页面 - Wagtail Space NL 2022](https://www.youtube.com/watch?v=OFqPKffSVWI)，作者：Viggo de Vries。
- [Wagtail 架构选项，或者我应该无头 - Wagtail Space NL 2022](https://www.youtube.com/watch?v=JMULuz6RzjQ)，作者：Dan Braghis。
- [Wagtail 无头和 NextJS 前端 - Wagtail Space NL 2022](https://www.youtube.com/watch?v=s8cJhFtjqZA)，作者：Lucas Moeskops。
- [Wagtail 状态 - Wagtail Space US 2024](https://www.youtube.com/watch?v=TKLYeKpFbno&list=PLfwZ-fob20cMduvPwjstgycu-Z_1QwJQB) 作者：Tom Dyson。
- [愉快的发布模式 - Wagtail Space US 2024](https://www.youtube.com/watch?v=ZXGcqY-OeYk&list=PLfwZ-fob20cMduvPwjstgycu-Z_1QwJQB)，作者：Michael Trythall。
- [复杂组件和接口的可访问性 - Wagtail Space US 2024](https://www.youtube.com/watch?v=AC1gy9R2Z6c&list=PLfwZ-fob20cMduvPwjstgycu-Z_1QwJQ)，作者：Kara Gaulrapp。
- [一千零一个鹡鸰遗址 - Wagtail Space US 2024](https://www.youtube.com/watch?v=yciVqzSGWTw&list=PLfwZ-fob20cMduvPwjstgycu-Z_1QwJQB) 作者：Vince Salvino。
- [Wagtail 3D 文件 - Wagtail Space US 2024](https://www.youtube.com/watch?v=ccBrb50xRCM&list=PLfwZ-fob20cMduvPwjstgycu-Z_1QwJQ)，作者：Dawn Wages 和 Mira Gibson。
- [Wagtail，重新激活 - Headless Without the Headache - Wagtail Space US 2024](https://www.youtube.com/watch?v=mQsI8Ji3_LY&list=PLfwZ-fob20cMduvPwjstgycu-Z_1QwJQB)，作者：Josh Marantz。
- [Lightning Talks June 20 - Wagtail Space US 2024](https://www.youtube.com/watch?v=UuE3Y15To8Q&list=PLfwZ-fob20cMduvPwjstgycu-Z_1QwJQ) - 闪电般的谈话。
- [LLM 和 Wagtail - Wagtail Space US 2024](https://www.youtube.com/watch?v=b-luIDn80bc&list=PLfwZ-fob20cMduvPwjstgycu-Z_1QwJQB) 作者：Emily Topp-Mugglestone。
- [PudlStack - 建立提供机器人助手的 Wagtail 亲和小组社区 - Wagtail Space US 2024](https://www.youtube.com/watch?v=SNEeo_ABQ7g&list=PLfwZ-fob20cMduvPwjstgycu-Z_1QwJQB)，作者：Anthony Garcia。
- [审核 Wagtail 内容 - Wagtail Space US 2024](https://www.youtube.com/watch?v=a1O3hKib8Ns&list=PLfwZ-fob20cMduvPwjstgycu-Z_1QwJQB&index=2&pp=i)，作者：Will Barton 和 Chuck Sebian-Lander。
- [编辑真正想要的 - Wagtail Space US 2024](https://www.youtube.com/watch?v=1qF5wC4rCY4&list=PLfwZ-fob20cMduvPwjstgycu-Z_1QwJQ) 作者：Meagen Voss。
- [通过验证改善编辑体验 - Wagtail Space US 2024](https://www.youtube.com/watch?v=UVBHciwpgKM&list=PLfwZ-fob20cMduvPwjstgycu-Z_1QwJQ)，作者：Scott Cranfill。
- [sditail：将 Wagtail CMS 扩展为空间数据基础设施 - Wagtail Space US 2024](https://www.youtube.com/watch?v=XxdJpYNT4EM&list=PLfwZ-fob20cMduvPwjstgycu-Z_1QwJQ)，作者：César Benjamin。
- [Packages! Packages! Packages! - Wagtail Space US 2024](https://www.youtube.com/watch?v=r5ovJPWvxL4&list=PLfwZ-fob20cMduvPwjstgycu-Z_1QwJQ) - 控制板。
- [Lightning Talks June 21 - Wagtail Space US 2024](https://www.youtube.com/watch?v=vazMp9jTlEU&list=PLfwZ-fob20cMduvPwjstgycu-Z_1QwJQ) - 闪电般的谈话。
- [Wagtail 状态 - Wagtail Space NL 2024](https://www.youtube.com/watch?v=P9Ftbu5NVUI&list=PLEyaio0l1qoGj7XTEuNXT2o3tYpuSmlbP&index=1) 作者：Tom Dyson。
- [无头鹡鸰策略 - Wagtail Space NL 2024](https://www.youtube.com/watch?v=nweVHX5DgWU&list=PLEyaio0l1qoGj7XTEuNXT2o3tYpuSmlbP&index=2)，作者：Rémy Sanchez。
- [Wagging HubSpot 的尾巴 - Wagtail Space NL 2024](https://www.youtube.com/watch?v=VUoOoRxlWrU&list=PLEyaio0l1qoGj7XTEuNXT2o3tYpuSmlbP&index=3) 作者：Simon Blanchard 和 Joost Meijerink。
- [Wagtail 和缓存 - Wagtail Space NL 2024](https://www.youtube.com/watch?v=vBdG2GfAZAo&list=PLEyaio0l1qoGj7XTEuNXT2o3tYpuSmlbP&index=4)，作者：Jake Howard。
- [更快的缩略图，更快的网络 - Wagtail Space NL 2024](https://www.youtube.com/watch?v=0kHhGBxwzeM&list=PLEyaio0l1qoGj7XTEuNXT2o3tYpuSmlbP&index=5)，作者：Alex Tomkins。
- [让每个人都快乐的不可能艺术 - Wagtail Space NL 2024](https://www.youtube.com/watch?v=v3KEaMTfKg0&list=PLEyaio0l1qoGj7XTEuNXT2o3tYpuSmlbP&index=6) 作者：Matthew Westcott。
- [将现代身份验证引入 Wagtail：WebAuthn 和密码 - Wagtail Space NL 2024](https://www.youtube.com/watch?v=qJwg2kFtFW4&list=PLEyaio0l1qoGj7XTEuNXT2o3tYpuSmlbP&index=7)，作者：Storm Heg。
- [如何随心所欲地滥用 Wagtail 的 StreamFields - Wagtail Space NL 2024](https://www.youtube.com/watch?v=tOBGJ0riDRw&list=PLEyaio0l1qoGj7XTEuNXT2o3tYpuSmlbP&index=8)，作者：Rémy Sanchez。
- [Wagtail AI 和 Wagtail 矢量索引 - Wagtail Space NL 2024](https://www.youtube.com/watch?v=jHuhX_SNF1s&list=PLEyaio0l1qoGj7XTEuNXT2o3tYpuSmlbP&index=9)，作者：Dan Braghiş。
- [Wagtail 翻译 - Wagtail Space NL 2024](https://www.youtube.com/watch?v=QxnC70Bwj0k&list=PLEyaio0l1qoGj7XTEuNXT2o3tYpuSmlbP&index=10)，作者：Coen van der Kamp。
- [您的内容网站缓存错误 - Wagtail Space NL 2024](https://www.youtube.com/watch?v=bWF06aCjbUM&list=PLEyaio0l1qoGj7XTEuNXT2o3tYpuSmlbP&index=11)，作者：Rémy Sanchez。
- [通用列表 - Wagtail Space NL 2024](https://www.youtube.com/watch?v=aNto27_lfJ4&list=PLEyaio0l1qoGj7XTEuNXT2o3tYpuSmlbP&index=12)，作者：Sage Abdullah。
- [恢复已删除的 Django 模型 - Wagtail Space NL 2024](https://www.youtube.com/watch?v=TB64DtQZeB0&list=PLEyaio0l1qoGj7XTEUNXT2o3tYpuSmlbP&index=13)，作者：Jake Howard。
- [Wagtail 仪表板 - Wagtail Space NL 2024](https://www.youtube.com/watch?v=0msxKe0RoNw&list=PLEyaio0l1qoGj7XTEuNXT2o3tYpuSmlbP&index=14) 作者：Judith van Leersum 和 Emmelien Schiet。
- [Wagtail 多语言网站 - Wagtail Space NL 2024](https://www.youtube.com/watch?v=5rPvOsVeRhA&list=PLEyaio0l1qoGj7XTEuNXT2o3tYpuSmlbP&index=15)，作者：Paul Stevens。
- [Wagtail 2025 年状态 - Wagtail 空间 2025](https://www.youtube.com/watch?v=9Kduqs6NH7Q&list=PLfwZ-fob20cPI9_fnG_ULYIdOS5TKP1IZ&index=2) 作者：Thibaud Colas。
- [工业中的鹡鸰：从农业到金融 - Wagtail Space 2025](https://www.youtube.com/watch?v=DH87OzXzj28&list=PLfwZ-fob20cPI9_fnG_ULYIdOS5TKP1IZ&index=3) 作者：Vince Salvino。
- [重新设计和重构 Wagtail 组件 - Wagtail Space 2025](https://www.youtube.com/watch?v=8h0fxe7b8s8&list=PLfwZ-fob20cPI9_fnG_ULYIdOS5TKP1IZ&index=4)，作者：Mariana。
- [构建更好的 Wagtail 网站：优秀 CMS 的特征 - Wagtail Space 2025](https://www.youtube.com/watch?v=n5KHTLS22YE&list=PLfwZ-fob20cPI9_fnG_ULYIdOS5TKP1IZ&index=5)，作者：Michael Trythall。
- [REX：从 Wagtail 构建 SaaS - Wagtail Space 2025](https://www.youtube.com/watch?v=3T-ITKTByH4&list=PLfwZ-fob20cPI9_fnG_ULYIdOS5TKP1IZ&index=6)，作者：Sébastien Corbin。
- [在 Wagtail 中实施法国政府设计系统 - Wagtail Space 2025](https://www.youtube.com/watch?v=8_CBltGuv0g&list=PLfwZ-fob20cPI9_fnG_ULYIdOS5TKP1IZ&index=7)，作者：Sylvain Boissel 和 Lucie Laporte。
- [Wagtail Nest：共同维护社区包 - Wagtail Space 2025](https://www.youtube.com/watch?v=h0kKy4R5kNY&list=PLfwZ-fob20cPI9_fnG_ULYIdOS5TKP1IZ&index=8)，作者：Coen van der Kamp。
- [自动数据加载器：用于天气数据集成的 Wagtail - Wagtail Space 2025](https://www.youtube.com/watch?v=iTxcq__Gcr4&list=PLfwZ-fob20cPI9_fnG_ULYIdOS5TKP1IZ&index=9)，作者：Erick Otenyo 和 Grace Amondi。
- [为编辑者构建灵活的 Wagtail CMS 体验 - Wagtail Space 2025](https://www.youtube.com/watch?v=-azqKJdEivk&list=PLfwZ-fob20cPI9_fnG_ULYIdOS5TKP1IZ&index=10)，作者：Annette Lewis 和 Eric Sherman。
- [在 Wagtail 上构建一个小型 YouTube - Wagtail Space 2025](https://www.youtube.com/watch?v=hLw3FWb2LfQ&list=PLfwZ-fob20cPI9_fnG_ULYIdOS5TKP1IZ&index=11)，作者：Tom Dyson。
- [使用 AI 创建故事和对象之间的联系 - Wagtail Space 2025](https://www.youtube.com/watch?v=Wkjm8xdV_6c&list=PLfwZ-fob20cPI9_fnG_ULYIdOS5TKP1IZ&index=12) 作者：Trish Thomas。
- [Wagtail 中的人工智能：内容编辑者的负责任创新 - Wagtail Space 2025](https://www.youtube.com/watch?v=n2fIFJLSH5E&list=PLfwZ-fob20cPI9_fnG_ULYIdOS5TKP1IZ&index=16)，作者：Sage Abdullah 和 Tom Usher。
- [波哥大数字图书馆：Wagtail 成功故事 - Wagtail Space 2025](https://www.youtube.com/watch?v=cbANVWkDIs0&list=PLfwZ-fob20cPI9_fnG_ULYIdOS5TKP1IZ&index=17)，作者：Juan Aguayo。
- [Wagtail 和 AI 代理编码 - Wagtail Space 2025](https://www.youtube.com/watch?v=pukU8F3ciEM&list=PLfwZ-fob20cPI9_fnG_ULYIdOS5TKP1IZ&index=18)，作者：Maciej Baron。
- [对 Wagtail 贡献的影响 - Wagtail Space 2025](https://www.youtube.com/watch?v=sW8k4F1DY18&list=PLfwZ-fob20cPI9_fnG_ULYIdOS5TKP1IZ&index=19)，作者：Chiemezuo Akujobi。
- [一个 URL 统治一切：Wagtail 中的动态登陆页面 - Wagtail Space 2025](https://www.youtube.com/watch?v=UOEvu4Lyj8w&list=PLfwZ-fob20cPI9_fnG_ULYIdOS5TKP1IZ&index=20) 作者：Chrissy Wainwright 和 Doug Harris。
- [使用 Wagtail 进行事实核查 - Wagtail Space 2025](https://www.youtube.com/watch?v=Spdt-W5XotM&list=PLfwZ-fob20cPI9_fnG_ULYIdOS5TKP1IZ&index=21)，作者：Jon Chittenden 和 Craig Dawson。
- [Sympa 与 Wagtail 的时事通讯 - Wagtail Space 2025](https://www.youtube.com/watch?v=n7bM54MAc24&list=PLfwZ-fob20cPI9_fnG_ULYIdOS5TKP1IZ&index=22)，作者：Agnès Haasser。
- [创建内容的代码 - Wagtail Space 2025](https://www.youtube.com/watch?v=XkSX195ssjY&list=PLfwZ-fob20cPI9_fnG_ULYIdOS5TKP1IZ&index=23)，作者：Alex Morega。
- [那个代码片段是谁？屏幕阅读器猜谜游戏 - Wagtail Space 2025](https://www.youtube.com/watch?v=VkPOe_JixTI&list=PLfwZ-fob20cPI9_fnG_ULYIdOS5TKP1IZ&index=24)，作者：Laura Wissiak 和 Pawel Masarczyk。
- [Bird Meets Bot：使用 AI 工具让 Wagtail 更智能 - Wagtail Space 2025](https://www.youtube.com/watch?v=SsjXnpuLnL0&list=PLfwZ-fob20cPI9_fnG_ULYIdOS5TKP1IZ&index=25)，作者：Alex Tomkins。
- [鹡鸰搜索的下一步在哪里？ - Wagtail Space 2025](https://www.youtube.com/watch?v=LglWFsqIu3E&list=PLfwZ-fob20cPI9_fnG_ULYIdOS5TKP1IZ&index=26) 作者：Matt Westcott。

### 播客

- [Podcast.\_\_init\_\_ Episode 58 - Wagtail with Tom Dyson](https://www.pythonpodcast.com/episodepage/episode-58-wagtail-with-tom-dyson) - 在本集中，汤姆·戴森 (Tom Dyson) 解释了 Wagtail 是如何创建的、它与其他选项的区别以及何时应该在项目中实施它。
- [Django Chat E9: Wagtail CMS - Tom Dyson](https://djangochat.com/episodes/wagtail-cms-tom-dyson) - Tom Dyson 在 Wagtail 上的采访，Wagtail 是基于 Django 的领先 CMS，被数以万计的组织使用，包括 Google、NASA 和英国 NHS。
- [Django Chat E84: Dawn Wages](https://djangochat.com/episodes/wagtail-react-gatsby-dawn-wages-RaD8k37m) - 对 Wagtail 团队核心成员 Dawn Wages 的采访。关于 Wagtail、React 和 Gatsby 的讨论。
- [Django Chat E168: Thibaud Colas](https://djangochat.com/episodes/thibaud-colas-2025-dsf-board-nominations) - 采访 Wagtail 核心团队成员，讨论 Django 的现状、即将举行的 DSF 董事会选举、Wagtail 路线图和社区机会。

### 视频

- [Learn Wagtail](https://learnwagtail.com/) - 关于 Wagtail 各个方面的定期视频教程。
- [Wagtail Wednesdays #01 - Adding Help Text to Improve Wagtail Editor Experience](https://www.youtube.com/watch?v=ciYNMcv3lE0) - Catherine 将向您介绍向 Wagtail 管理添加一些有用的补充文本字段可以采取的步骤。
- [Wagtail Wednesdays #02 - Customising Rich Text Features in Wagtail](https://www.youtube.com/watch?v=ei7ot_Wry3o) - Catherine 将向您介绍自定义富文本编辑器的步骤，以控制内容编辑器可以使用哪些功能。
- [Wagtail Wednesdays #03 - Using tabs to create a cleaner admin interface](https://www.youtube.com/watch?v=uZc0aZrHtQw) - Chris 向您介绍如何使用选项卡来组织字段。
- [Wagtail Wednesdays #04 - Organising Images and Documents using Wagtail Collections](https://www.youtube.com/watch?v=HGXHtFpLDCA) - Kieran 将向您介绍将图像和文档组织到集合中的过程。
- [Wagtail Wednesdays #05 - How to organise your fields and streamline the editor experience](https://www.youtube.com/watch?v=CedcZmQ9KHs) - Chelsea 将向您介绍组织字段的过程，以便更轻松地管理它们并简化编辑体验。
- [Wagtail Wednesdays #06 - Creating & using custom settings in your wagtail site](https://www.youtube.com/watch?v=KJWCGq3IRNc) - Chris 将向您介绍如何设置和使用自定义站点设置。
- [Wagtail Wednesdays #07 - How to Enable the Wagtail Styleguide](https://www.youtube.com/watch?v=_CfU9UivYPI) - 这是一个非常有用的资源，不需要任何时间即可启用，它允许您根据指南检查组件并显示所有可用的 Wagtail 图标。
- [How to Deploy Wagtail to Google App Engine](https://www.youtube.com/watch?v=uD9PTag2-PQ) - 重点是 Google Cloud Platform，但很好地介绍了如何在其 PAAS 中启动和运行 Wagtail。

### 展示柜

- [Offiical showcase - Projects made with Wagtail](https://wagtail.org/showcase/) - 精选的网站和应用程序列表，让您体验使用 Wagtail 构建的最佳项目。
- [Made with Wagtail](https://madewithwagtail.org/) - 使用 Wagtail CMS 制作的网站和应用程序的展示。

### 包装清单

- [Wagtail third-party packages](https://wagtail.org/packages/) - 基于 PyPI 数据的官方列表。
- [Framework: Wagtail on PyPI](https://pypi.org/search/?c=Framework+%3A%3A+Wagtail) - 标记为“框架：Wagtail”的软件包。
- [Wagtail grid - Django Packages](https://djangopackages.org/grids/g/wagtail-cms/) - Django Packages 上的 Wagtail 项目和包。

## 对于编辑

- [Wagtail user guide](https://guide.wagtail.org/) - 为在 Wagtail 中创建内容或管理内容制作的任何人提供的官方用户指南
- [How Do I Wagtail?](https://www.mozillafoundation.org/en/docs/how-do-i-wagtail/) - Mozilla 面向编辑器的指南，介绍如何使用 Wagtail 的管理界面。
- [CCA Wagtail Editor Portal](https://portal.cca.edu/help/wagtail-documentation/) - 加州艺术学院为 Wagtail 提供的面向用户的文档
- [Caltech Wagtail Editor Portal](https://sites.caltech.edu/) - Caltech 的 Wagtail 面向用户的文档

## 社区

- [Wagtail Space](https://www.wagtail.space/) - Wagtail 培训课程、Wagtail（闪电）演讲和 Wagtail 冲刺。 2019 年 3 月 13 日至 15 日，Wagtail Space 在荷兰阿纳姆举行。
- [Wagtail updates on Telegram](https://telegram.me/wagtail) - 用于一般 Wagtail 更新的非官方 Telegram 频道。
- [Wagtail support on Telegram](https://telegram.me/wagtailcms) - 用于支持问题和讨论的非官方 Telegram 频道。

## 开源网站

- [Wagtail demo project](https://github.com/wagtail/bakerydemo) - 下一代 Wagtail 演示，诞生于雷克雅未克。
- [Torchbox.com on Wagtail](https://github.com/torchbox/torchbox.com) - Torchbox 网站 2024 年版本。
- [Made with Wagtail](https://github.com/springload/madewithwagtail) - 展示使用 Wagtail CMS（易于使用的开源 Django 内容管理系统）制作的网站和应用程序。
- [Federal Election Commission](https://github.com/fecgov/fec-cms) - 新联邦选举委员会网站的内容管理系统 (CMS)。
- [Bow Valley SPCA Website](https://github.com/nfletton/bvspca) - Bow Valley SPCA 基于 Wagtail/Django 的网站。
- [SecureDrop](https://github.com/freedomofpress/securedrop.org) - SecureDrop 举报人文件提交系统由 Wagtail 提供支持的网站。
- [consumerfinance.gov](https://github.com/cfpb/consumerfinance.gov) - Django 项目保护美国消费者。
- [Western Friend website](https://github.com/WesternFriend/westernfriend.org) - 贵格会出版物 Western Friend (westernfriend.org) 的网站，为寻求在世界上实现信仰的贵格会社区和个人提供资源和支持。西方之友是宗教之友协会的一部分。
- [Outreachy website](https://github.com/outreachy/website) - Outreachy 网站的代码，基于 Python、Django 和 Bootstrap。
- [Wagtail user guide](https://github.com/wagtail/guide) - 一个向内容编辑、版主和管理员教授 Wagtail 的网站。
- [Penticon Public Library](https://github.com/danlerche/public-library-wagtailCMS) - 这是一个使用 wagtail CMS 的公共图书馆网站示例。

## 贡献

随时欢迎您的贡献！请先阅读[贡献指南](docs/CONTRIBUTING.md)。

## 许可证

[Springload](https://www.springload.co.nz/) 和其他贡献者的这项工作被标记为 [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/)。
