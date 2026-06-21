# 很棒的流浪者
[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome) [![Gitter](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/iJackUA/awesome-vagrant?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge) [![Build Status](https://api.travis-ci.org/iJackUA/awesome-vagrant.svg?branch=master)](https://travis-ci.org/iJackUA/awesome-vagrant)

很棒的 Vagrant 资源、插件、教程和其他好东西的精选列表。


## 官方资源

* [Vagrant site](https://www.vagrantup.com/) - 安装说明、官方手册和文档。
* [GitHub repo](https://github.com/hashicorp/vagrant) - 源代码、问题讨论和协作。


## 盒子

*在哪里可以找到操作系统盒？*

* [Vagrantbox.es](http://www.vagrantbox.es/) - 所有可用框的最大列表，由社区通过 GitHub Pull Request 维护。
* [Vagrant Cloud](https://app.vagrantup.com/boxes/search) - 配置共享、盒子分发和发现（也是私人协作和共享的高级功能）。
* [Cloud Images Ubuntu.com](https://cloud-images.ubuntu.com/vagrant/) - “干净的”官方 Ubuntu 云镜像。
* [Baseboxes from Opscode](https://github.com/chef/bento#current-baseboxes) - CentOS、Fedora、Debian、FreeBSD、Ubuntu。
* [Puppet Labs Vagrant Boxes](http://puppet-vagrant-boxes.puppetlabs.com/) - 这些盒子可供各种 Puppet 项目使用。
* [Cloudsmith](https://cloudsmith.io) - 完全托管的包管理 SaaS，支持 Vagrant 存储库（以及许多其他存储库）。

## 配置

* [All available build in provisioning providers](https://www.vagrantup.com/docs/provisioning) - 官方文档。
* [Vaprobash](http://fideloper.github.io/Vaprobash/index.html) - Vagrant 配置 Bash 脚本。


## 值得注意的插件

*您可以通过此命令`vagrant plugin install MODULE-NAME`安装这些模块*

* [来自 GitHub wiki 的可用 Vagrant 插件列表](https://github.com/hashicorp/vagrant/wiki/Available-Vagrant-Plugins)。
* [vagrant-vbguest](https://github.com/dotless-de/vagrant-vbguest) - 自动更新 VirtualBox 来宾添加（根据 VB 版本）。
* [vagrant-hostsupdater](https://github.com/cogitatio/vagrant-hostsupdater) - 在主机系统上的 /etc/hosts 文件中添加一个条目。
* [vagrant-cachier](http://fgrehm.viewdocs.io/vagrant-cachier/) - 在相似的 VM 实例之间共享公共包（apt-get、npm 等）缓存。
* [vagrant-host-shell](https://github.com/phinze/vagrant-host-shell) - vagrant 配置程序，用于在虚拟机启动时在主机上运行命令。
* [vagrant-ansible-local](https://github.com/jaugustin/vagrant-ansible-local) 允许直接从来宾虚拟机为您的虚拟机配置 ansible playbook。
* [sahara](https://github.com/jedi4ever/sahara) - 轻松管理虚拟机状态（在尝试软件堆栈时提交/回滚）。
* [vagrant-registration](https://github.com/projectatomic/adb-vagrant-registration) - 向 Vagrant 来宾添加“注册”和“取消注册”功能，以便在具有订阅模型的系统（例如 Red Hat Enterprise Linux）上进行更新。
* [vagrant-service-manager](https://github.com/projectatomic/vagrant-service-manager) - 使您能够更轻松地访问 [Atomic Developer Bundle (ADB)](https://github.com/projectatomic/adb-atomic-developer-bundle) 提供的功能和服务。
* [vagrant-scp](https://github.com/invernizzi/vagrant-scp) - 通过 SCP 将文件复制到 Vagrant VM。

## 助手/工具

* [Packer](https://www.packer.io/) - 一种从单一源配置为多个平台创建相同机器映像的工具。用于具有多提供商可移植性的快速基础设施部署。
* [T.A.D.S. boilerplate](https://github.com/Thomvaill/tads-boilerplate) - 用于创建、开发和部署 Docker Swarm 环境的样板文件，使用 Vagrant 在本地重现生产环境。
* [Veewee](https://github.com/jedi4ever/veewee) - 一个用于轻松（且重复）构建自定义 Vagrant 基础盒、KVM 和虚拟机映像的工具。
* [Vagrant plugin for ZSH shell](https://github.com/robbyrussell/oh-my-zsh/wiki/Plugins#vagrant) - 自动完成命令、任务名称、框名称和内置文档。
* [CLI Vagrant Manager](https://github.com/MunGell/vgm) - 管理多个流浪盒的简单命令行工具

## 桌面工具

* [Vagrant Manager](http://vagrantmanager.com/) 适用于 OS X。

## 网络服务

*使用自动配置脚本生成 Vagrantfile。*

* [Phansible](http://phansible.com/) - 提供了一个易于使用的界面，可帮助您为基于 PHP 的项目生成 Ansible Playbook。
* [PuPHPet](https://puphpet.com/) - 一个简单的 GUI，用于为 <s>PHP</s> Web 开发设置虚拟机。
* [Protobox](http://getprotobox.com/) - PuPHPet 类似，但使用自己的带有 YAML 配置格式的安装程序来控制虚拟机上安装的所有内容。
* [Rove](http://rove.io/) - 允许您预先生成典型 Vagrant 构建的服务。

## 代理服务

*代理您的本地网络服务器并使其通过互联网公开可用。*

* [Vagrant share](https://www.vagrantup.com/docs/share/) - 允许您与世界上的任何人共享您的 Vagrant 环境。
* [nip.io](http://nip.io) - 提供通配符 DNS 的神奇域名
对于任何 IP 地址。
* [ngrok](https://ngrok.com/) - 创建安全隧道以将 NAT 或防火墙后面的本地服务器暴露给互联网的工具。
* [serveo](https://serveo.net/) - 将本地服务器暴露在互联网上，无需安装任何客户端！
* [proxylocal.com](http://proxylocal.com) - 代理您的本地网络服务器并使其通过互联网公开可用。
* [localtunnel.me](https://localtunnel.github.io/www/) - 为您分配一个唯一的可公开访问的 URL，它将所有请求代理到您本地运行的网络服务器。
* [portmap.io](https://portmap.io/) - 基于OpenVPN的免费端口转发解决方案。

## 教程

* [Vagrant 入门](http://www.thisprogrammingthing.com/2013/getting-started-with-vagrant/)，作者：This Programming Thing。
* [Vagrant 入门 - 自动化开发服务器部署和配置。](http://stdout.in/en/post/getting_started_with_vagrant_automated_dev_servers_deploy_and_provisioning)
* [使用 PhpStorm 中的高级 Vagrant 功能。](http://confluence.jetbrains.com/display/PhpStorm/Working+with+Advanced+Vagrant+features+in+PhpStorm)
* [通过 Vagrant Share 在网络上共享您的虚拟机](https://scotch.io/tutorials/sharing-your-virtual-machine-on-the-web-with-vagrant-share)。
* [编程社区精选资源用于学习 Vagrant](https://hackr.io/tutorials/learn-vagrant)
* [Classpert Vagrant 在线课程](https://classpert.com/vagrant) Vagrant 在线课程列表（免费和付费）

## 书籍

* [Vagrant：启动并运行](https://www.amazon.com/Vagrant-Running-Virtualized-Development-Environments/dp/1449335837)，作者：Mitchell Hashimoto。
* [Vagrant CookBook](https://leanpub.com/vagrantcookbook) 作者：Erika Heidi。
* [Pro Vagrant](https://www.amazon.com/Pro-Vagrant-Wlodzimierz-Gajda/dp/1484200748/) 作者：Wlodzimierz Gajda。
* [使用 Vagrant 创建开发环境](http://shop.oreilly.com/product/9781849519182.do) / [第二版](http://shop.oreilly.com/product/9781784397029.do) 作者：Michael Peacock
* [Vagrant 虚拟开发环境手册](http://shop.oreilly.com/product/9781784393748.do)，作者：Chad Thompson

## 流行的现成环境

* [Vagrantpress](https://github.com/vagrantpress/vagrantpress) - 用于创建和修改 WordPress 网站的开发环境。
* [Varying Vagrant Vagrants](https://github.com/Varying-Vagrant-Vagrants/VVV) - 专注于 WordPress 开发的开源 Vagrant 配置。
* [Joomla-Vagrant](https://github.com/joomlatools/joomlatools-vagrant)。
* [VDD](https://www.drupal.org/project/vdd) - Vagrant Drupal 开发。
* [Drupal VM](https://www.drupalvm.com/) - 用于本地 Drupal 开发的 VM，使用 Vagrant + Ansible 构建
* [Try Yii2](https://github.com/iJackUA/try-yii2) - 尝试使用 Vagrant VM + Ansible 配置的 Yii2 = 完整的现成虚拟服务器游乐场。
* [Laravel4-Vagrant](https://github.com/bryannielsen/Laravel4-Vagrant) - 在带有 PHP 5.5 的 Ubuntu 12.04 Vagrant 虚拟机中运行 Laravel 4。
* [OpenStack on Ansible with Vagrant](https://github.com/openstack-ansible/openstack-ansible)。
* [Laravel Homestead](https://laravel.com/docs/master/homestead) - 用于 Laravel 开发的官方 Vagrant Box，基于 Ubuntu 16.04 LTS、PHP 7、Nginx 和多个数据库平台。
* [Scotch Box](https://scotch.io/bar-talk/announcing-scotch-box-2-0-our-dead-simple-vagrant-lamp-stack-improved) - 带有 [LAMP](https://en.m.wikipedia.org/wiki/LAMP_%28software_bundle%29) 堆栈的简单 Vagrant Box，以及一些有用的附加功能，基于 Ubuntu 14.04 LTS。


## 许可证

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

在法律允许的范围内，[Ievgen Kuzminov](http://stdout.in/) 已放弃本作品的所有版权以及相关或邻接权。
