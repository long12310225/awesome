
![](图片/banner.png)

<p align="center">
  <a href="https://github.com/sindresorhus/awesome">
    <img src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg" />
  </a>
</p>

有用的 Heroku 资源的精选列表。

- [Analytics](#-analytics)
- [Architecture](#-architecture)
- [Blogs](#-blogs)
- [Deployment](#-deployment)
- [Development](#-development)
- [Domains](#-domains)
- [Meta](#-meta)
- [Postgres](#-postgres)
- [Scaling](#-scaling)
- [Security](#-security)
- [Toolbelt](#-toolbelt)
- [Goodbye...](#-goodbye)


## <img width="21" height="21" src="images/analytics.png" /> 分析

Heroku 分析...

- `tool` [Metabase](http://www.metabase.com/docs/v0.13.3/operations-guide/running-metabase-on-heroku.html) — Metadata 的测试版，作为可以直接部署到 Heroku 的应用程序。


## <img width="21" height="21" src="images/architecture.png" /> 架构

如何构建您的 Heroku 项目......

- `文章` [探索 Heroku 上的微服务架构](http://blog.codeship.com/exploring-microservices-architecture-on-heroku/) — 探讨了为什么 Heroku 消除了您在使用微服务时需要担心的许多工具。
- `文章` [Heroku 和 SOA](https://www.rdegges.com/2014/heroku-and-soa/) — 讨论了为什么 Heroku 非常适合为您的项目构建面向服务的架构。
- `文章` [使用 npm 和 NodeJS 在 Heroku 上将前端与后端分离](https://medium.com/@spygi/scalable-cost-efficient-web-architectures-for-heroku-eb8f1f55a4b6) - 使用 npm 和 NodeJS 在 Heroku 中部署微服务 Web 应用程序的实践指南。


## <img width="21" height="21" src="images/blogs.png" /> 博客

互联网上经常（或专门）撰写有关 Heroku 的博客......

- `blog` [Heroku 博客](https://blog.heroku.com) — Heroku 官方博客。


## <img width="21" height="21" src="images/deployment.png" /> 部署

有助于在 Heroku 上部署的资源...

- `official` [Preboot](https://devcenter.heroku.com/articles/preboot) — 解释了如何使用“Preboot”功能来实现零停机部署，这可能很难做到正确。
- `文章` [从 Jenkins 自动化 Heroku 部署](https://www.paulfurley.com/automating-heroku-deployments-from-jenkins/) — 解释了如何自动化部署的某些部分，例如启用维护模式、将数据库从生产复制到暂存、针对暂存运行迁移等。
- `question` [部署到 Heroku 时如何忽略文件？](http://stackoverflow.com/questions/12523435/how-do-i-ignore-folders-and-files-when-pushing-to-heroku-with-a-rails-app) — 有关 `.gitignore` 等功能的常见问题的答案。
- `文章` [掌握 Procfile 的六个技巧](https://medium.com/@adam_41691/six-tips-for-mastering-your-procfile-64ea1207b779) — 改进运行 Heroku 进程的方式。
- `文章` [使用 Docker 将 Django 部署到 Heroku](https://testdriven.io/blog/deploying-django-to-heroku-with-docker/) — 着眼于如何通过 Heroku 容器运行时使用 Docker 将 Django 应用程序部署到 Heroku


## <img width="21" height="21" src="images/development.png" /> 开发

- `official` [管理应用程序的多个环境](https://devcenter.heroku.com/articles/multiple-environments) — 关于如何考虑管理每个环境的不同部分的一个很好的入门知识。


## <img width="21" height="21" src="images/domains.png" /> 域名

在 Heroku 上使用自定义域名的提示...

- `文章` [为 Heroku 应用程序配置 CloudFlare DNS](http://www.higherorderheroku.com/articles/cloudflare-dns-heroku/) — 演练如何使用 CloudFlare 作为 DNS 提供商。
- `文章` [在单个域上托管多个 Heroku 应用程序](https://pilot.co/blog/hosting-multiple-heroku-apps-on-a-single-domain/) — 一篇有关如何在多个 Heroku 应用程序之间共享同一域的文章。
- `question` [如何在单个域上托管多个 Heroku 应用程序？](http://stackoverflow.com/questions/19119164/multiple-heroku-apps-on-a-single-domain) — 一个 StackOverflow 问题，其中包含对如何从不同路径而不是子域提供多个 Heroku 应用程序的常见问题的一些回答。


## <img width="21" height="21" src="images/general.png" /> 一般

涵盖 Heroku 的许多不同内容的通用资源......

- `book` [Heroku 黑客指南](http://www.theherokuhackersguide.com/) — 一本电子书，涵盖了在 Heroku 上维护和扩展项目的许多基础知识。
- `book` [Heroku Cookbook](http://www.amazon.com/Heroku-Cookbook-Mike-Coutermarsh/dp/1782177949) — 逐步解决在 Heroku 上管理和扩展实际生产 Web 应用程序的挑战的方法。


## <img width="21" height="21" src="images/meta.png" /> 元数据

有关公司本身的信息...

- `official` [大启动](https://blog.heroku.com/archives/2007/10/30/the_big_kickoff) — 第一篇 Heroku 博客文章。
- `文章` [Heroku 不适合白痴](https://www.rdegges.com/2012/heroku-isnt-for-idiots/) — 解释了 Heroku 的优势以及为什么它不仅仅适用于副项目。
- `文章` [我的 Heroku 价值观](https://brandur.org/heroku-values) — [Brandur Leach](https://twitter.com/brandur) 离开 Heroku 时的一系列精彩收获。
- `talk` [Buildpack Adventure](http://buildpack-adventure.herokuapp.com/) — 一个关于 Heroku 的 buildpack 的很酷的幻灯片，以及开源社区正在与它们一起进行的黑客攻击。


## <img width="21" height="21" src="images/postgres.png" /> Postgres

任何与 [Heroku Postgres](https://www.heroku.com/postgres) 相关的事情......

- `official` [Heroku Postgres](https://www.heroku.com/postgres) — 登陆页面解释它是。
- `plugin` [heroku-buildpack-pgbouncer](https://github.com/heroku/heroku-buildpack-pgbouncer) — 一个构建包，允许使用 [`stunnel`](https://www.stunnel.org/index.html) 和 [`pgbouncer`](https://wiki.postgresql.org/wiki/PgBouncer) 进行事务池以避免达到连接限制。


## <img width="21" height="21" src="images/redis.png" /> Redis

任何与 [Heroku Redis](https://elements.heroku.com/addons/heroku-redis) 相关的事情......


## <img width="21" height="21" src="images/scaling.png" /> 缩放

帮助您扩展 Heroku 项目的资源...

- `tool` [HireFire](https://www.hirefire.io/) — 一种 SaaS 工具，可根据负载需要自动缩放 Heroku dyno。


## <img width="21" height="21" src="images/security.png" /> 安全

如何保护您的 Heroku 应用程序......

- `文章` [在 Heroku 上设置 CloudFlare 的免费 SSL](https://robots.thoughtbot.com/set-up-cloudflare-free-ssl-on-heroku) — 引导您完成通过 Cloudflare 设置免费 SSL 的确切步骤。


## <img width="21" height="21" src="images/toolbelt.png" /> 工具带

[Heroku Toolbelt](https://toolbelt.heroku.com/) 的有用资源...

- `official` [工具带下载](https://toolbelt.heroku.com/) — 下载 Heroku 工具带的位置。
- `plugin` [heroku-accounts](https://github.com/ddollar/heroku-accounts) — 可以轻松地从命令行同时使用多个帐户。
- `plugin` [heroku-pg-extras](https://github.com/heroku/heroku-pg-extras) — 一个工具带插件，为使用 Postgres 添加了额外有用的插件。诸如分析缓存命中率、异常查询、未使用的索引、表大小等。


## <img width="21" height="21" src="images/goodbye.png" /> 再见...

如果您出于某种原因决定从 Heroku 迁移，需要检查的事项......

- `tool` [dokku](http://dokku.viewdocs.io/dokku/) — 一个自托管、基于 docker、兼容 Heroku 的平台。


## <img width="21" height="21" src="images/license.png" /> 许可证

[![CC0](http://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

在法律允许的范围内，[Ian Storm Taylor](http://ianstormtaylor.com) 已放弃本作品的所有版权以及相关或邻接权。
