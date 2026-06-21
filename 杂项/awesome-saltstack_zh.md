# 很棒的 SaltStack [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> 协作策划的精彩 SaltStack 资源、教程和其他咸味东西的列表。

<!--lint ignore double-link-->
[<img src="https://user-images.githubusercontent.com/519955/35341388-d8c0cf0e-0125-11e8-9831-51f13fab58c7.jpg" width="100%">](https://saltproject.io/)

Salt（通常称为 SaltStack）是另一个用 Python 构建的配置管理系统。\
它采用了一种新的基础设施管理方法，开发的软件足够简单，可以在几秒钟内运行，可扩展性足以管理数万台服务器，并且足够快，可以在几毫秒内控制它们并与之通信。
SaltStack 软件管理系统基础架构和在其上运行的应用程序堆栈，供 Web 规模应用程序开发人员、DevOps 团队和系统管理员使用。\
VMware 于 2020 年 10 月收购了 SaltStack。

## 内容

- [官方资源](#official-resources)
- [Tutorials](#tutorials)
- [Code](#code)
- [Integrations](#integrations)
- [Books](#books)
- [Videos](#videos)
- [Tools](#tools)
- [Presentations](#presentations)
- [博客文章和意见](#blogposts-and-opinions)
- [Discussions](#discussions)
- [Community](#community)
- [Formulas](#formulas)
- [备忘单](#cheat-sheets)
- [Uncategorized](#uncategorized)
- [Attic](#attic)

## 官方资源

<!--lint ignore double-link-->
- [Salt Project site](https://saltproject.io/) - Salt 项目（Salt 开源）网站。
- [vRealize Automation SaltStack Config](https://www.vmware.com/products/vrealize-automation/saltstack-config.html) - VMware 的 vRealize Automation SaltStack Config 网站（商业 SaltStack 产品的新名称）。
- [GitHub repo](https://github.com/saltstack/salt) - Salt 的源代码、问题讨论和协作。
- [GitLab repo](https://gitlab.com/saltstack/open) - 盐项目最终的新家。
- [SaltStack Documentation](https://docs.saltproject.io/en/latest/) - 官方文档。
- [Salt in 10 minutes](https://docs.saltproject.io/en/latest/topics/tutorials/walkthrough.html) - 官方攻略。
<!--lint ignore awesome-list-item-->
- [SaltStack Get Started](https://docs.saltproject.io/en/getstarted/) - 这些教程将引导您了解 SaltStack 的启动和运行的基础知识。
- [Training and certification](https://www.saltstack.com/products/saltstack-training/) - 正式培训。
- [Jinja2 documentation](http://jinja.pocoo.org/docs/latest/) - 该官方文档涵盖了 Salt 中使用的模板语言。
- [Salt Module Contributions](https://github.com/saltstack/salt-contrib) - 由社区开发的 Salt 模块。

## 教程

<!--lint ignore awesome-list-item-->
- [About SaltStack](http://www.yet.org/2016/09/salt/) - 内容丰富的博文，包含大量深入信息。
- [A dive into SaltStack](https://opencredo.com/a-dive-into-salt-stack/) - SaltStack 揭秘——配置管理对于系统工程师来说是一个巨大的飞跃。
- [How To Use Salt Cloud Map Files to Deploy App Servers and an Nginx Reverse Proxy](https://www.digitalocean.com/community/tutorials/how-to-use-salt-cloud-map-files-to-deploy-app-servers-and-an-nginx-reverse-proxy) - 演练如何使用 Salt Cloud 映射文件部署应用程序服务器和 Nginx 反向代理。
- [An Introduction to SaltStack Terminology and Concepts](https://www.digitalocean.com/community/tutorials/an-introduction-to-saltstack-terminology-and-concepts) - _使用 SaltStack 管理开发环境_系列中的第 1 部分（共 6 部分）。
- [SaltStack Infrastructure: Installing the Salt Master](https://www.digitalocean.com/community/tutorials/saltstack-infrastructure-installing-the-salt-master) - 系列_使用 SaltStack 管理开发环境_中的第 2 部分（共 6 部分）。
- [SaltStack Infrastructure: Configuring Salt-Cloud to Spin Up DigitalOcean Resources](https://www.digitalocean.com/community/tutorials/saltstack-infrastructure-configuring-salt-cloud-to-spin-up-digitalocean-resources) - 系列_使用 SaltStack 管理开发环境_中的第 3 部分（共 6 部分）。
- [SaltStack Infrastructure: Creating Salt States for Nginx Web Servers](https://www.digitalocean.com/community/tutorials/saltstack-infrastructure-creating-salt-states-for-nginx-web-servers) - 系列_使用 SaltStack 管理开发环境_中的第 4 部分（共 6 部分）。
- [SaltStack Infrastructure: Creating Salt States for HAProxy Load Balancers](https://www.digitalocean.com/community/tutorials/saltstack-infrastructure-creating-salt-states-for-haproxy-load-balancers) - 系列_使用 SaltStack 管理开发环境_中的第 5 部分（共 6 部分）。
- [SaltStack Infrastructure: Creating Salt States for MySQL Database Servers](https://www.digitalocean.com/community/tutorials/saltstack-infrastructure-creating-salt-states-for-mysql-database-servers) - 系列的第 6 部分_使用 SaltStack 管理开发环境_。
- [Getting Started with SaltStack - the Other Configuration Management System Built with Python](https://www.linuxjournal.com/content/getting-started-salt-stack-other-configuration-management-system-built-python) - 2013 年的 Linux 期刊“入门”。
- [Create an army of Salt minions on DigitalOcean](http://www.aaronbell.com/lets-make-salt-minions-on-digitalocean/) - 将 Salt 的简单性与 DigitalOcean 的快照和图像功能相结合。
- [Vagrant & SaltStack Quickstart Tutorial](https://hittaruki.info/post/vagrant-saltstack-tutorial/) - SaltStack 和 Vagrant 入门。
- [Salt-API, A Crash Course](https://thereluctanttecchie.blogspot.com/2014/01/salt-api-crash-course.html) - 启动并运行准系统的 salt-api 概念验证。
- [Revised Getting Started with SaltStack - Part 1](https://www.infracloud.io/blog/revised-getting-started-with-saltstack-part-1/) - 简单的设置并在命令行上进行操作。
- [SaltStack Examples](https://www.unixmen.com/saltstack-examples/) - 将快速教您一些默认功能。
- [Getting Started with Saltstack and salt-workspace](https://blog.badgerops.net/getting-started-with-salt-workspace/) - 通过设置 salt-workspace 来学习 SaltStack。
- [Getting started with Salt Structure](https://blog.badgerops.net/getting-started-with-salt-structure-2/) - 了解如何设置结构化的 SaltStack 工作区。
- [Introduction to SaltStack](https://github.com/redmage123/Introduction-to-Saltstack) - 为期两天的课程，旨在快速向系统管理员和应用程序开发人员介绍如何开始使用 Saltstack。
- [The Simplest Way to Learn SaltStack](https://medium.com/@timlwhite/the-simplest-way-to-learn-saltstack-cd9f5edbc967) - 通过在 Docker 中进行设置来开始学习 SaltStack 的基础知识。
- [SaltStack - Quick Guide](https://www.tutorialspoint.com/saltstack/saltstack_quick_guide.htm) - 教程点上较大的“学习 SaltStack”教程的一部分。
- [Upgrading Salt to Python 3](https://salt.tips/upgrading-salt-to-python-3/) - 如何将 SaltStack 从 Python2 切换到 Python3。
- [Salt Guides and Tutorials, by Linode](https://www.linode.com/docs/guides/applications/configuration-management/salt/) - 由 Linode 创建和管理的 Salt 指南和教程的优秀集合。

## 代码

- [valentin2105/Kubernetes-Saltstack](https://github.com/valentin2105/Kubernetes-Saltstack) - 从头开始部署 Kubernetes 集群的 Saltstack 配方。
- [madflojo/masterless-salt-base](https://github.com/madflojo/masterless-salt-base) - 快速引导一个通用的 Ubuntu 服务器。一种已准备好托管 Docker 容器的容器。

## 集成

- [Jenkins Salt API Plugin](https://plugins.jenkins.io/saltstack/) - 该插件发送 SaltStack API 消息作为构建步骤。
- [Rundeck](https://github.com/amendlik/salt-gen-resource) - 从盐矿生成 Rundeck 节点资源。

## 书籍

- [O'Reilly - Salt Essentials](http://shop.oreilly.com/product/0636920033240.do) - 作者：克雷格·塞贝尼克、托马斯·哈奇。
- [O'Reilly - Network Automation at Scale](https://www.cloudflare.com/network-automation-at-scale-ebook/) - 作者：Mircea Ulinic 和 Seth House（由 Cloudflare 赞助的电子书）。
- [Leanpub - SaltStack For DevOps](https://leanpub.com/saltstackfordevops) - 作者：艾门·艾尔·阿姆里。
- [Leanpub - Getting Started with SaltStack](https://leanpub.com/gettingstartedwithsaltstack) - 本·霍斯默着。
- [Packt - Learning SaltStack, 2nd ed.](https://www.packtpub.com/networking-and-servers/learning-saltstack-second-edition) - 作者：科尔顿·迈尔斯。
- [Packt - Mastering SaltStack, 2nd ed.](https://www.packtpub.com/networking-and-servers/mastering-saltstack-second-edition) - 约瑟夫·霍尔着。
- [Packt - Extending SaltStack](https://www.packtpub.com/networking-and-servers/extending-saltstack) - 约瑟夫·霍尔着。
- [Packt - Salt Cookbook](https://www.packtpub.com/networking-and-servers/salt-cookbook) - 作者：阿尼班·萨哈。

## 视频

<!--lint ignore awesome-list-item-->
- [SaltStack](https://www.youtube.com/user/saltstack) - SaltStack 的官方 YouTube 频道。
- [Salt Project on Twitch](https://www.twitch.tv/saltprojectoss) - Salt Project 的官方 Twitch 频道。
- [Managing Your Infrastructure with SaltStack](https://www.youtube.com/watch?v=y-zQUqMHRX4&t=35s) - PyCon 2015 - 2015 年 4 月 11 日 - 科尔顿·迈尔斯。
- [Testing Salt States with Docker](https://www.youtube.com/watch?v=_xO7wj19OzI) - SaltStack PDX - 2015 年 6 月 23 日 - Jason Denning。
- [Beyond Configuration Management with SaltStack for Event-Driven Infrastructure](https://www.youtube.com/watch?v=cMCH6EizVVc) - 南加州 Linux 博览会 - 2016 年 1 月 23 日 - David Boucha。
- [Automation and Orchestration with SaltStack and Twilio](https://vimeo.com/162183524) - Devops 芝加哥 - 2016 年 3 月 2 日 - Nathan Brooks。
- [SaltStack for FreeBSD](https://www.youtube.com/watch?v=HijG0hWebZk&list=PL5yV8umka8YQOr1wm719In5LITdGzQMOF) - 有关 SaltStack for FreeBSD 的 7 部分视频速成课程。
- [SaltConf15 - YouTube](https://www.youtube.com/playlist?list=PL9svBjLDUl_8BqpIDKlCTqHZI2mkysTvZ) - SaltConf15 上发表了 60 多场演讲，我们将其全部记录下来。
- [SaltConf16 - YouTube](https://www.youtube.com/playlist?list=PL9svBjLDUl_-sVwcRliUQ-VGDb2qvwpx_) - SaltConf16 演示的视频录制。
- [SaltConf17 - YouTube](https://www.youtube.com/playlist?list=PL9svBjLDUl_-8yJxp-nSlmM9KYEQH4fgj) - SaltStack 客户和合作伙伴提供的 SaltConf17 演示视频录制。
- [SaltConf18 - YouTube](https://www.youtube.com/playlist?list=PL9svBjLDUl_-wsL5HZqtTuvV80Y6dqmQE) - SaltConf18 演示的视频记录。
- [SaltConf19 - YouTube](https://www.youtube.com/playlist?list=PL9svBjLDUl_8E03aA45ZncgwTrI96ky2m) - SaltConf19 演示的视频记录。
- [SaltConf20 - YouTube](https://www.youtube.com/playlist?list=PL9svBjLDUl__frIm2HOGPm1GrcVQkOZTe) - SaltConf20 演示的视频记录。

## 工具

- [SaltGUI](https://github.com/erwindon/SaltGUI) - 用于管理基于 SaltStack 的基础设施的 Web 界面。
- [Silica](https://gitlab.com/perfecto25/silica) - 基于 Flask 的轻量级 Salt Web 控制台。
- [Molten](https://github.com/martinhoefling/molten) - Molten 是 Saltstack 公开的 REST API 的 WebUI。
- [salt-pepper](https://pypi.org/project/salt-pepper/) - salt-api 系统的 CLI 前端。
- [salt-sproxy](https://github.com/mirceaulinic/salt-sproxy) - Salt 插件可自动管理和配置设备和应用程序，而无需运行（代理）Minions。
- [salt-lint](https://github.com/warpnet/salt-lint/) - 检查 Salt 状态文件 (SLS) 中是否有可能改进的实践和行为。
- [Alcali](https://alcali.dev/) - 一个基于 Web 的工具，用于监视和管理 Saltstack Salt。
- [ISalt](https://github.com/mirceaulinic/isalt) - 基于 IPython 的命令 shell，用于交互式 Salt 编程。

## 演讲

- [Getting Started with SaltStack](https://speakerdeck.com/pycon2014/getting-started-with-saltstack-by-peter-baumgartner) - 作者：彼得·鲍姆加特纳。
- [An introduction to infrastructure management with SaltStack](https://www.slideshare.net/saltstack/an-overvisaltstack-presentation-clean) - 作者：奥雷利安·杰隆。
- [Saltpad: A SaltStack Web GUI](https://speakerdeck.com/lothiraldan/saltpad-a-saltstack-web-gui) - 作者：鲍里斯·费尔德。
- [Intro to SaltStack](http://www.justincarmony.com/slides/salt-tutorial/) - 作者：贾斯汀·卡莫尼。
- [salt-deconstructed](http://salt-decon.carson-anderson.com/) - 卡森·安德森 (Carson Anderson) 的视频和演示文稿（幻灯片和 PDF）。

## 博客文章和意见

- [Docker with SaltStack](https://opsnotice.xyz/docker-with-saltstack/) - 如何在基于 Debian 或 Ubuntu 的虚拟云服务器上使用 SaltStack。
- [One week of Salt: frustrations and reflections](https://stevebennett.me/2014/02/17/one-week-of-salt-frustrations-and-reflections/) - Chef 用户的第一手经验。
- [Getting started with SaltStack by example: Automatically Installing nginx](http://bencane.com/2013/09/03/getting-started-with-saltstack-by-example-automatically-installing-nginx/) - 对于 Salt Master 和 Minions 来说都是一个很好的入门指南。
- [SaltStack: Manage entries in unmanaged files with File Blockreplace](https://makina-corpus.com/blog/metier/2014/saltstack-manage-entries-in-unmanaged-files-with-file-blockreplace) - 如何使用 SaltStack 的核心 `file.blockreplace`。
- [SaltStack: Keeping Salt Pillar data encrypted using GPG](http://fabianlee.org/2016/10/18/saltstack-keeping-salt-pillar-data-encrypted-using-gpg/) - 关于支柱数据的安全加密/解密。
- [Secure Pillar in SaltStack with GPG](https://gijs.io/2017/02/28/secure-pillar-data-in-saltstack-with-gpg/) - 可以使用 GPG 来加密您的支柱数据。
- [Network-Automation with Salt, NAPALM and Kubernetes](http://blog.simonmetzger.de/2018/02/salt-napalm-k8s-network-automation/) - 如何管理无法自行安装软件的旧设备。
- [Using Salt like Ansible](https://duncan.codes/2016/05/18/using-salt-like-ansible.html) - 如何以类似于 Ansible 的方式使用 Salt。
- [Using Salt with reclass](http://www.yet.org/2016/10/reclass/) - 使用类继承来定义节点角色并避免重复。
- [Text editor plugins for Salt states and YAML/Jinja](https://salt.tips/text-editor-plugins-for-salt-states-and-yaml-jinja/) - 涵盖编写 Salt 状态时不同编辑器的插件。
- [Writing a custom Salt Grain](https://blog.badgerops.net/writing-a-custom-salt-grain/) - 编写自定义 Salt Grain，以及您可能想要这样做的原因。
- [Building Self-Healing Applications](http://bencane.com/2014/12/30/building-self-healing-applications-with-salt-api/) - 自动执行检测并采取第一个行动来纠正基础设施中的错误。
- [Testing your salt states with kitchen-salt](https://blog.gtmanfred.com/kitchen-salt.html) - 可以轻松地独立于生产环境测试盐态或配方。
- [Salt Sudo](https://medium.com/@mike.reider/using-saltstack-for-emergency-sudoers-access-tempsudo-d5417e528e4d) - 使用 Salt 自定义模块来管理用户的 sudo 访问。
- [Complex User management with Saltstack (using Py! renderer)](https://medium.com/@mike.reider/complex-user-management-with-saltstack-using-py-renderer-a4caa5cf229a) - 使用包含所有用户数据的集中式用户 YAML 文件。
- [Vagrant Provisioning with SaltStack](https://medium.com/@Joachim8675309/vagrant-provisioning-with-saltstack-50dab12ce6c7) - 使用无主 Salt Stack 配置虚拟系统。
- [Salt DevKit with External Formulas](https://medium.com/@Joachim8675309/salt-devkit-with-external-formulas-9e38d8b90cd7) - 使用外部 Salt 公式使用 Vagrant 进行本地开发。
<!--lint ignore awesome-list-item-->
- [Prometheus - Auto-deploying Consul and Exporters using Saltstack](https://yetiops.net/posts/prometheus-consul-saltstack-part-1-linux/) - 如何在 Linux 上部署 SaltStack、Consul 和 Prometheus Node Exporter。
- [Network Automation at Scale](https://mirceaulinic.net/2017-02-14-network-automation-tutorial/) - 60 分钟内即可启动并运行。
- [SaltStack Overview](https://saidvandeklundert.net/2020-03-20-saltstack-overview/) - 对 Salt 的精彩概述和介绍。
- [Parsing Command Output in Saltstack with JC](https://blog.kellybrazil.com/2020/09/15/parsing-command-output-in-saltstack-with-jc/) - 如何使用“jc”轻松解析 SaltStack 中的远程命令输出。

## 讨论

<!--lint ignore no-repeat-punctuation-->
- [Reddit: Vagrat, SaltStack, Ansible, Docker, Chef, Puppet, Packer.. Something](https://www.reddit.com/r/sysadmin/comments/2fmkvq/vagrat_saltstack_ansible_docker_chef_puppet/) - Reddit 上的讨论于 2014 年 9 月在 `/r/sysadmin` 中开始。

## 社区

- [Salt IRC chat](https://web.libera.chat/?channels=#salt) - Libera Chat 上有关 Salt 的 IRC。
- [SaltStack Community Slack](https://saltstackcommunity.slack.com/) - 官方 SaltStack Slack 社区（[注册链接](https://saltstackcommunity.herokuapp.com)）。
- [SaltStack on Reddit](https://www.reddit.com/r/saltstack/) - SaltStack Reddit 子版块。
- [#saltstack on Network to Code Slack](https://networktocode.slack.com/archives/C0NL8RRMX) - Network To Code Slack 上的#saltstack 频道（[注册链接](https://networktocode.herokuapp.com/)）。
- [#saltstack on VMware {code} Community Slack](https://vmwarecode.slack.com/archives/C01CASFRWG0) - VMware {code} Community Slack 上的#saltstack 频道（[注册链接](https://code.vmware.com/web/code/join)）。
- [Twitter feed](https://twitter.com/Salt_Project_OS) - 盐计划官方 Twitter 帐户。
- [Mailing list](https://groups.google.com/forum/#!forum/salt-users) - Google 网上论坛上的 Salt 用户邮件列表。
- [SaltStack Meetups](https://www.meetup.com/pro/saltstack/) - 全球聚会团体。
- [SaltConf](https://saltconf.com/) - 为 SaltStack 客户、用户、合作伙伴、开发人员和社区成员举办的年度用户会议。
- [Facebook](https://www.facebook.com/SaltProjectOSS/) - 盐计划官方 Facebook 帐户。

## 公式

- [SaltStack Formulas](https://github.com/saltstack-formulas/) - SaltStack 公式存储库的中央集合。
- [Salt Formulas](https://github.com/salt-formulas) - 社区开发了 SaltStack 公式生态系统。
- [Writing SaltStack formulas](http://ryepup.unwashedmeme.com/blog/2015/03/16/writing-saltstack-formulas/) - 有关编写 SaltStack 公式的概述。
<!--lint ignore awesome-list-item-->
- [盐配方](http://www.yet.org/2016/09/salt-formulas/) 关于盐配方的深入博文。

## 备忘单

- [SaltStack Cheat Sheet Plus](https://github.com/fmdlc/saltstack-cheatsheet) - 作者：法库·德拉·克鲁斯。
- [Salt Commands cheat sheet](https://sites.google.com/site/mrxpalmeiras/saltstack/salt-cheat-sheet) - 常见 Salt 命令列表。
- [SaltStack Wiki](https://github.com/saltstack/salt/wiki/Cheat-Sheet) - SaltStack GitHub Wiki 中的备忘单。

## 未分类

- [Salt（软件）](https://en.wikipedia.org/wiki/Salt_(软件)) - 维基百科（英语）。

## 阁楼

- [How To Install Salt on Ubuntu 12.04](https://www.digitalocean.com/community/tutorials/how-to-install-salt-on-ubuntu-12-04) - 《盐简介》系列第 1 部分（共 2 部分）。
- [How To Create Your First Salt Formula](https://www.digitalocean.com/community/tutorials/how-to-create-your-first-salt-formula) - 系列的第 2 部分_盐简介_。
- [Automated Provisioning of DigitalOcean Cloud Servers with Salt Cloud on Ubuntu 12.04](https://www.digitalocean.com/community/tutorials/automated-provisioning-of-digitalocean-cloud-servers-with-salt-cloud-on-ubuntu-12-04) - 在 Ubuntu 12.04 上使用 Salt Cloud 自动配置 DigitalOcean 云服务器的演练。
- [How To Install and Configure Salt Master and Minion Servers on Ubuntu 14.04](https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-salt-master-and-minion-servers-on-ubuntu-14-04) - Ubuntu 14.04 的 SaltStack 安装演练。
- [Docker Swarm 1.12 Cluster Orchestration with SaltStack](https://btmiller.com/2016/11/27/docker-swarm-1.12-cluster-orchestration-with-saltstack.html) - 让我们看看如何使用 SaltStack 自动启动集群。
