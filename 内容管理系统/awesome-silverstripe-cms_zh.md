# 很棒的 Silverstripe CMS [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
<!--lint ignore double-link-->
[<img src=“images/logo-silverstripe-cms.png”align=“right”width=“200”>](https://www.silverstripe.org/)

> Silverstripe 框架和 CMS 的有用资源
<!--lint ignore double-link-->
[Silverstripe CMS](https://www.silverstripe.org) 是一个用于构建 Web 应用程序的开源 PHP 框架。它是一个快速开发的 MVC 框架，可用作经典的成熟 CMS 或无头 CMS，可以通过 GraphQL 或自定义 API 进行查询。
遵循“Active Record”设计模式，您可以使用项目特定的数据模型轻松扩展内置功能。

[欢迎贡献](CONTRIBUTING.md)，请发送拉取请求或打开问题以开始讨论。

过时的项目可以在[存档](ARCHIVE.md)中找到。

## 内容
<!-- PLEASE USE `doctoc --maxlevel 3 README.md` TO KEEP THE TOC TO AN APPROPRIATE SIZE -->
<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->


- [Resources](#resources)
  - [官方网站](#official-websites)
  - [文档和教程](#documentation--tutorials)
  - [Blogs](#blogs)
  - [视频频道](#video-channels)
  - [Community](#community)
  - [会议和聚会](#conferences--meetups)
- [非常有用的模块](#very-useful-modules)
  - [模块列表](#module-listings)
  - [通用模块](#general-modules)
  - [I18N（国际化）](#i18n-internationalisation)
  - [站内搜索](#site-search)
  - [开发助手](#development-helpers)
  - [花式表单字段](#fancy-form-fields)
- [Tools](#tools)
  - [Management](#management)
  - [IDE插件](#ide-plugins)
  - [Virtualisation](#virtualisation)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## 资源
### 官方网站
<!--lint ignore double-link-->
- [www.silverstripe.org](https://www.silverstripe.org) - 框架和CMS。
- [www.silverstripe.com](https://www.silverstripe.com) - Silverstripe Ltd.，CMS 背后的公司。
- [www.s2-hub.com](https://www.s2-hub.com) - S2Hub - 欧洲银条协会。

### 文档和教程
- [API Docs](http://api.silverstripe.org/) - 自动生成的 API 文档。
- [Technical Documentation](http://doc.silverstripe.org/framework/en/) - 对于开发商来说。解释所有核心概念。
- [Using the CMS](http://userhelp.silverstripe.org/) - 为最终用户提供如何使用核心功能的文档。
- [Silverstripe Lessons](https://www.silverstripe.org/learn/lessons/) - 了解如何通过实际项目逐步构建 Silverstripe 网站。
- [Font reference](https://silverstripe-fonts.dorset-digital.net/) - 内置图标字体供后端使用。
- [TinyMCE Configuration Examples For SS3](https://github.com/jonom/silverstripe-tinytidy) - HTMLEditorField 的配置示例。


### 博客
- [Official Silverstripe Blog](https://www.silverstripe.org/blog/) - 有关 Silverstripe CMS 的新闻。
- [SilverStrip.es](http://www.silverstrip.es) - Silverstripe 开发人员的有用发现。

### 视频频道
- [Official StripeCon YouTube Channel](https://www.youtube.com/channel/UC38vU3H_UrdGFnc3vTJiORA) - 各种 StripeCon 会议的演讲。
- [Official Silverstripe Vimeo Channel](https://vimeo.com/silverstripe) - 来自聚会和会议的各种视频。

### 社区
- [Stack Overflow](https://stackoverflow.com/questions/tagged/silverstripe) - Stack Overflow 上与 Silverstripe 相关的问题。
- [Silverstripe User Slack](https://silverstripe-users.slack.com/) - 社区 Slack 频道，提供即时帮助或与其他开发人员交流。
  - [邀请 Silverstripe 用户 Slack](https://www.silverstripe.org/community/slack-signup)
- [Forum](https://forum.silverstripe.org/) - 用于提问或讨论的官方论坛。

### 会议和聚会
- [European Silverstripe Conference](https://www.stripecon.eu) - 每年都会去另一个国家。
- [Meetups](https://www.meetup.com/topics/silverstripe/all/) - Silverstripe 相关聚会的列表。

## 非常有用的模块
### 模块列表
- [SSMods: Detailed Module Search](http://ssmods.com) - 替代模块搜索。
- [Most Used Modules](https://addons.silverstripe.org/add-ons?sort=relative) - 显示下载最多的模块。
- [Silverstripe Recipes on Packagist](https://packagist.org/packages/silverstripe/recipe-plugin/dependents) - 为不同类型的项目预先配置的模块集。

### 通用模块
- [Multiuser editing alert](https://github.com/silverstripe/silverstripe-multiuser-editing-alert) - 当多人编辑同一页面时，向 Silverstripe CMS 中的用户发出警报。

### I18N（国际化）
- [Fluent](https://github.com/tractorcow-farm/silverstripe-fluent) - Silverstripe 的多语言翻译模块，无需管理单独的站点树。
- [Autotranslate](https://github.com/bratiask/silverstripe-autotranslate) - 使用 Google Translate API 创建字段的自动翻译。

### 站内搜索
- [Silverstripe Searchable](https://github.com/i-lateral/silverstripe-searchable) - 使用 Silverstripe ORM 添加更复杂的站点搜索。具有跨多个搜索对象的搜索结果的专用模板。
- [Searchable DataObjects](https://github.com/g4b0/silverstripe-searchable-dataobjects) - 基于 MySQL 的快速而简单的搜索。对于单一语言网站很有用。
- [Fulltext Search](https://github.com/silverstripe/silverstripe-fulltextsearch) - Solr4 的完整搜索界面（EOL）。
- [Fulltext Search Local Solr](https://addons.silverstripe.org/add-ons/silverstripe/fulltextsearch-localsolr) - 易于安装 Solr4 (EOL) 实例以进行本地开发。
- [Solr search](https://github.com/firesphere/silverstripe-solr-search) - Solr 搜索接口，支持最新的 Solr (9) 版本。带有子模块，例如从“全文搜索”模块过渡，以及子站点、流利等。

### 开发助手
- [Debugbar](https://github.com/lekoala/silverstripe-debugbar/) - 显示浏览器中的调试统计信息。
- [IdeAnnotator](https://github.com/silverleague/silverstripe-ideannotator) - 在开发/构建上自动生成类注释。
- [Populate](https://github.com/dnadesign/silverstripe-populate) - 通过 YAML 文件填充您的数据库。
- [Mock DataObjects](https://github.com/unclecheese/silverstripe-mock-dataobjects) - 允许 DataObjects 使用虚假数据智能地自行填充。
- [Version Truncator](https://github.com/axllent/silverstripe-version-truncator) - 自动删除旧的 SiteTree 页面版本。
- [UserSwitcher](https://github.com/sheadawson/silverstripe-userswitcher) - 在前端和后端添加一个小表单，以便以任何用户身份快速登录。
- [Masquerade](https://github.com/dhensby/silverstripe-masquerade) - 允许管理员以另一个“成员”的身份“登录”。这对于调试和远程支持很有用。

### 花式表单字段
- [Markdown Field](https://github.com/Silverstripers/markdownfield) - 可以替换您的 HTMLEditorFields（使用 TinyMCE），以便您可以使用 Markdown 语法。
- [Code Editor Field](https://github.com/nathancox/silverstripe-codeeditorfield) - 为您提供语法突出显示的文本区域字段 - 非常适合基于 CMS 的 YAML 或 HTML。

## 工具
### 管理
- [SSPak](https://github.com/silverstripe/sspak) - 用于管理 Silverstripe 环境中的数据库/资产包的工具。
- [SSPy](https://github.com/Firesphere/silverstripe-sspy) - Python版本的SSPak，可以处理超过2GB的资产。

### IDE插件
- [VSCode Silverstripe](https://marketplace.visualstudio.com/items?itemName=adrian.silverstripe) - VSCode 中 Silverstripe 模板文件的语法突出显示。
- [Jetbrains / PHPStorm Silverstripe Template Language Support](https://plugins.jetbrains.com/plugin/17014-silverstripe-template-language-support) - Silverstripe 模板文件的语法突出显示。
- [PHPStorm / Webstorm Live Templates](https://github.com/northcreation-agency/silverstripe-php-web-storm-live-templates) - 添加各种 Silverstripe 特定代码片段的快捷方式。

### 虚拟化

#### 码头工人
- [ddev setup](https://firesphere.dev/articles/ddevelopment-environment/) - 如何设置 ddev 以与 Silverstripe CMS 一起使用。
- [brettt89/silverstripe-web](https://hub.docker.com/r/brettt89/silverstripe-web) - Apache + PHP Docker 映像，带有预装的 PHP 模块以支持 Silverstripe。
- [brettt89/sspak](https://hub.docker.com/r/brettt89/sspak) - SSPak Docker 镜像。
- [brettt89/silverstripe-solr-cwp](https://hub.docker.com/r/brettt89/silverstripe-solr-cwp) - CWP Solr Docker 镜像。

#### 流浪者
没有像 Laravel 有它的 homestead 盒子那样的官方盒子。然而，有一些不错的 Vagrant 盒子可供您使用：
- [Twisted Bytes](https://www.twistedbytes.nl/en/blog/php-vagrant-box/) - 有用的 vagrant box，具有多个 PHP 版本、MariaDB 或 PostgreSQL、邮件捕获器等等。
- [Twisted Bytes Box Templates](https://derkbox.com) - 使用 Twisted Bytes vagrant box 的不同开发场景的有用模板。
- [Laravel Homestead](https://github.com/laravel/homestead) - 用于本地开发的预包装盒。
- [Scotchbox](https://box.scotch.io) - 用于本地开发的流行 LAMP/LEMP 堆栈。
- [Zauberfisch Vagrant Boxes](https://github.com/Zauberfisch/vagrant-boxes) - 用于 SS3 和 SS4 的预配置 Vagrant 盒。


