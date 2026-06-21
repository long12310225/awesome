# 很棒的 SSH [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

> *SSH* [应用程序](#apps)、[库](#libraries) 和[资源](#resources) 的精选列表。

<h2align="center"><img src="https://raw.githubusercontent.com/moul/awesome-ssh/master/logo.jpg" width="400" /></h2>

受到 [awesome](https://github.com/sindresorhus/awesome) 列表的启发。

如果您想贡献，请阅读[贡献指南](CONTRIBUTING.md)。

**查看我的[博客](https://manfred.life/)🦄或在[Twitter](https://twitter.com/moul)上打个招呼*。**

## 目录

- [Apps](#apps)
  - [`.ssh/config`](#sshconfig)
  - [使用 *SSH* 协议的工具](#tools-using-the-ssh-protocol)
  - [Servers](#servers)
  - [Network](#network)
  - [Multiplexers](#multiplexers)
  - [SSH 密钥/身份验证](#ssh-keys--authentication)
  - [SSH代理](#ssh-agent)
  - [Tools](#tools)
  - [Automation](#automation)
  - [Web](#web)
  - [测试/蜜罐](#testing--honeypots)
  - [SSH 的替代方案](#alternatives-to-ssh)
- [Libraries](#libraries)
- [Resources](#resources)
  - [Tutorials](#tutorials)
  - [Security](#security)
  - [Documentation](#documentation)
  - [Community](#community)

## 应用程序

### `.ssh/config`

* [`assh`](https://github.com/moul/assh) [![stars](https://img.shields.io/github/stars/moul/advanced-ssh-config.svg?style=social&label=stars)](https://github.com/moul/advanced-ssh-config) - 透明包装器 (ProxyCommand)，将正则表达式、别名、网关、包含、动态主机名添加到 *SSH*和 `ssh-config`。 _以前：`高级 ssh 配置`_
* [storm](https://github.com/emre/storm) [![stars](https://img.shields.io/github/stars/emre/storm.svg?style=social&label=stars)](https://github.com/emre/storm) - 像老板一样管理您的 *SSH*。
* [ansible-ssh-config](https://github.com/gaqzi/ansible-ssh-config) [![stars](https://img.shields.io/github/stars/gaqzi/ansible-ssh-config.svg?style=social&label=stars)](https://github.com/gaqzi/ansible-ssh-config) - 让 *Ansible* 管理 `ssh_config`。
* [ec2ssh](https://github.com/mirakui/ec2ssh) [![stars](https://img.shields.io/github/stars/mirakui/ec2ssh.svg?style=social&label=stars)](https://github.com/mirakui/ec2ssh) - *AWS EC2* 的 `ssh_config` 管理器。
* [ssh-config](https://github.com/dbrady/ssh-config) [![stars](https://img.shields.io/github/stars/dbrady/ssh-config.svg?style=social&label=stars)](https://github.com/dbrady/ssh-config) - 帮助管理 `.ssh/config` 文件的工具。

### 使用 *SSH* 协议的工具

* [scp](http://linux.die.net/man/1/scp) - 通过 *SSH* 保护远程文件复制实用程序。
* [rsync](https://rsync.samba.org) - 支持 *SSH* 的快速增量传输实用程序。
* [sftp](https://en.wikipedia.org/wiki/SSH_File_Transfer_Protocol) - 通过 *SSH* 的文件传输协议。
* [curl](http://curl.haxx.se) - 用于传输数据的命令行工具和库（支持“sftp”）。

### 服务器

* [sshportal](https://github.com/moul/sshportal) [![stars](https://img.shields.io/github/stars/moul/sshportal.svg?style=social&label=stars)](https://github.com/moul/sshportal) - 简单、有趣、透明的 SSH（和 Telnet）堡垒服务器
* [ssh2docker](https://github.com/moul/ssh2docker) [![stars](https://img.shields.io/github/stars/moul/ssh2docker.svg?style=social&label=stars)](https://github.com/moul/ssh2docker) - *SSH* 服务器到 Docker 容器。
* [ssh-proxy](https://github.com/ml-tooling/ssh-proxy) [![stars](https://img.shields.io/github/stars/ml-tooling/ssh-proxy.svg?style=social&label=stars)](https://github.com/ml-tooling/ssh-proxy) - Dockerized SSH 堡垒，用于将 SSH 连接代理到任意容器。
* [whosthere](https://github.com/FiloSottile/whosthere) [![stars](https://img.shields.io/github/stars/FiloSottile/whosthere.svg?style=social&label=stars)](https://github.com/FiloSottile/whosthere) - 一个知道你是谁的 *SSH* 服务器。 `$ ssh whoami.filippo.io`。
* [sshfront](https://github.com/gliderlabs/sshfront) [![stars](https://img.shields.io/github/stars/gliderlabs/sshfront.svg?style=social&label=stars)](https://github.com/gliderlabs/sshfront) - 可编程 *SSH* 前端。
* [ssh-chat](https://github.com/shazow/ssh-chat) [![stars](https://img.shields.io/github/stars/shazow/ssh-chat.svg?style=social&label=stars)](https://github.com/shazow/ssh-chat) - 通过 *SSH* 聊天。
* [sshcommand](https://github.com/dokku/sshcommand) [![stars](https://img.shields.io/github/stars/dokku/sshcommand.svg?style=social&label=stars)](https://github.com/dokku/sshcommand) - 将 *SSH* 变成专门针对您的应用程序的瘦客户端。
* [sshmuxd](https://github.com/joushou/sshmuxd) [![stars](https://img.shields.io/github/stars/joushou/sshmuxd.svg?style=social&label=stars)](https://github.com/joushou/sshmuxd) - `sshmux` 前端。
* [x84](https://github.com/jquast/x84) [![stars](https://img.shields.io/github/stars/jquast/x84.svg?style=social&label=stars)](https://github.com/jquast/x84) - 用于现代 *UTF-8* 和经典 *cp437* 网络虚拟终端的 *python* `telnet`/`ssh` 服务器。本着 *ami/x*、*teleguard*、*renegade*、*inquity* 等经典软件的精神。
* [teleport](https://github.com/gravitational/teleport) [![stars](https://img.shields.io/github/stars/gravitational/teleport.svg?style=social&label=stars)](https://github.com/gravitational/teleport) - 适用于集群和团队的现代 *SSH* 服务器。
* [ShellHub](https://github.com/shellhub-io/shellhub) [![stars](https://img.shields.io/github/stars/shellhub-io/shellhub.svg?style=social&label=stars)](https://github.com/shellhub-io/shellhub) - 用于远程访问防火墙和 NAT 后面的任何 Linux 设备的 *SSH* 网关。

### 网络

* [Mosh](https://mosh.mit.edu) - 手机外壳。
* [sshfs](https://github.com/libfuse/sshfs) [![stars](https://img.shields.io/github/stars/libfuse/sshfs.svg?style=social&label=stars)](https://github.com/libfuse/sshfs) - 基于 *SSH* 文件传输协议的文件系统客户端。
* [ngrok](https://github.com/inconshreveable/ngrok) [![stars](https://img.shields.io/github/stars/inconshreveable/ngrok.svg?style=social&label=stars)](https://github.com/inconshreveable/ngrok) - 内省到本地主机的隧道。
* [localtunnel](https://github.com/progrium/localtunnel) [![stars](https://img.shields.io/github/stars/progrium/localtunnel.svg?style=social&label=stars)](https://github.com/progrium/localtunnel) - 将本地主机服务器公开到互联网。
* [sshuttle](https://github.com/sshuttle/sshuttle) [![stars](https://img.shields.io/github/stars/sshuttle/sshuttle.svg?style=social&label=stars)](https://github.com/sshuttle/sshuttle) - 透明代理服务器，充当穷人的*VPN*。通过“ssh”转发。不需要管理员。适用于 *Linux* 和 *MacOS*。支持*DNS 隧道*。
* [sshttp](https://github.com/stealth/sshttp) [![stars](https://img.shields.io/github/stars/stealth/sshttp.svg?style=social&label=stars)](https://github.com/stealth/sshttp) - *SSH*/*HTTP(S)* 多路复用器。在同一端口上运行网络服务器和“sshd”，无需更改。
* [switcher](https://github.com/jamescun/switcher) [![stars](https://img.shields.io/github/stars/jamescun/switcher.svg?style=social&label=stars)](https://github.com/jamescun/switcher) - 在同一端口上运行 *SSH* 和 *HTTP(S)*。
* [sslh](https://github.com/yrutschle/sslh) [![stars](https://img.shields.io/github/stars/yrutschle/sslh.svg?style=social&label=stars)](https://github.com/yrutschle/sslh) - 应用协议多路复用器（即：*SSH* + *HTTPS*）。
* [tund](https://github.com/aphyr/tund) [![stars](https://img.shields.io/github/stars/aphyr/tund.svg?style=social&label=stars)](https://github.com/aphyr/tund) - *SSH* 反向隧道守护进程。
* [autossh](http://www.harding.motd.ca/autossh/) - 网络中断后自动重新生成 *SSH* 会话。
* [wssh](https://github.com/aluzzardi/wssh) [![stars](https://img.shields.io/github/stars/aluzzardi/wssh.svg?style=social&label=stars)](https://github.com/aluzzardi/wssh) - *SSH* 到 WebSockets 桥。
* [docker-volume-sshfs](https://github.com/vieux/docker-volume-sshfs) [![stars](https://img.shields.io/github/stars/vieux/docker-volume-sshfs.svg?style=social&label=stars)](https://github.com/vieux/docker-volume-sshfs) - `sshfs` docker 卷插件。
* [quicssh](https://github.com/moul/quicssh) [![stars](https://img.shields.io/github/stars/moul/quicssh.svg?style=social&label=stars)](https://github.com/moul/quicssh) - SSH 的 QUIC 代理
* [sshpiper](https://github.com/tg123/sshpiper) [![stars](https://img.shields.io/github/stars/tg123/sshpiper.svg?style=social&label=stars)](https://github.com/tg123/sshpiper) - ssh scp 缺少的反向代理。
* [sshhub](https://sshhub.de) - Web 服务：访问防火墙后面的 SSH 服务器 (ssh-teamviewer)。

### 多路复用器

* [tmux](https://tmux.github.io) - 终端多路复用器。
* [clusterssh](https://github.com/duncs/clusterssh) [![stars](https://img.shields.io/github/stars/duncs/clusterssh.svg?style=social&label=stars)](https://github.com/duncs/clusterssh) - 通过 *SSH* 进行集群管理。
* [tmux-cssh](https://github.com/dennishafemann/tmux-cssh) [![stars](https://img.shields.io/github/stars/dennishafemann/tmux-cssh.svg?style=social&label=stars)](https://github.com/dennishafemann/tmux-cssh) - `tmux` 具有类似 *ClusterSSH* 的行为。
* [tm](https://github.com/Ganneff/tm) [![stars](https://img.shields.io/github/stars/Ganneff/tm.svg?style=social&label=stars)](https://github.com/Ganneff/tm) - `tmux` 管理器/助手。
* [i2cssh](https://github.com/wouterdebie/i2cssh) [![stars](https://img.shields.io/github/stars/wouterdebie/i2cssh.svg?style=social&label=stars)](https://github.com/wouterdebie/i2cssh) - `csshX` 就像 *iTerm2* 的 *SSH* 工具。
* [ClusterSSH](http://sourceforge.net/projects/clusterssh/) - 通过单个图形控制台控制多个“xterm”窗口。

### *SSH* 密钥/身份验证

* [authy-ssh](https://github.com/authy/authy-ssh) [![stars](https://img.shields.io/github/stars/authy/authy-ssh.svg?style=social&label=stars)](https://github.com/authy/authy-ssh) - 针对 *SSH* 服务器的简单“双因素”身份验证。
* [github-auth](https://github.com/chrishunt/github-auth) [![stars](https://img.shields.io/github/stars/chrishunt/github-auth.svg?style=social&label=stars)](https://github.com/chrishunt/github-auth) - GitHub 用户的 *SSH* 密钥管理。
* [cipherhub](https://github.com/substack/cipherhub) [![stars](https://img.shields.io/github/stars/substack/cipherhub.svg?style=social&label=stars)](https://github.com/substack/cipherhub) - 基于 *SSH* 公钥加密消息，可轻松从 GitHub 导入。
* [Slack 通知](http://www.ryanbrink.com/slack-ssh-session-notifications/) ([存档版本](https://web.archive.org/web/20160505202303/http://www.ryanbrink.com/slack-ssh-session-notifications/)) - 设置 Slack 通知的指南（可以针对其他服务进行修改）。
* [totp-ssh-fluxer](https://github.com/benjojo/totp-ssh-fluxer) [![stars](https://img.shields.io/github/stars/benjojo/totp-ssh-fluxer.svg?style=social&label=stars)](https://github.com/benjojo/totp-ssh-fluxer) - 一种确保您的`sshd` 端口每 30 秒更改一次。
* [github-keygen](https://github.com/dolmen/github-keygen) [![stars](https://img.shields.io/github/stars/dolmen/github-keygen.svg?style=social&label=stars)](https://github.com/dolmen/github-keygen) - 为您的 GitHub 帐户轻松创建安全的 *SSH* 配置。
* [kr](https://github.com/KryptCo/kr) [![stars](https://img.shields.io/github/stars/dolmen/github-keygen.svg?style=social&label=stars)](https://github.com/KryptCo/kr) - Kr 代理，将访问请求路由到安装 Kryptonite 的配对手机。
* [ServerAuth](https://serverauth.com) - 跨服务器自动同步 SSH 访问
* [HIBA](https://github.com/google/hiba) [![stars](https://img.shields.io/github/stars/google/hiba.svg?style=social&label=stars)](https://github.com/google/hiba) - 集中管理对一组机器的访问，无需推送authorized_users 文件。

### *SSH*代理

* [ssh-ident](https://github.com/ccontavalli/ssh-ident) [![stars](https://img.shields.io/github/stars/ccontavalli/ssh-ident.svg?style=social&label=stars)](https://github.com/ccontavalli/ssh-ident) - 不同项目的不同代理和不同密钥，使用 `ssh`。
* [oh-my-zsh/plugins/ssh-agent](https://github.com/robbyrussell/oh-my-zsh) [![stars](https://img.shields.io/github/stars/robbyrussell/oh-my-zsh.svg?style=social&label=stars)](https://github.com/robbyrussell/oh-my-zsh) - `ssh-agent` 插件`zsh`。
* [sshecret](https://github.com/thcipriani/sshecret) - 自动创建和管理多个密钥的多个代理。

### 工具

* [xxh](https://github.com/xxh/xxh) [![stars](https://img.shields.io/github/stars/xxh/xxh.svg?style=social&label=stars)](https://github.com/xxh/xxh) - 无论您在何处通过 ssh，都带上您最喜欢的 shell。
* [sshrc](https://github.com/danrabinowitz/sshrc) [![stars](https://img.shields.io/github/stars/danrabinowitz/sshrc.svg?style=social&label=stars)](https://github.com/danrabinowitz/sshrc) - 当你`ssh`时带上你的`.bashrc`，`.vimrc`等。
* [kyrat](https://github.com/fsquillace/kyrat) [![stars](https://img.shields.io/github/stars/fsquillace/kyrat.svg?style=social&label=stars)](https://github.com/fsquillace/kyrat) - SSH 包装脚本，让您在 Linux 和 OSX 上始终随身携带点文件。
* [ssh-vault](https://github.com/ssh-vault/ssh-vault) [![stars](https://img.shields.io/github/stars/ssh-vault/ssh-vault.svg?style=social&label=stars)](https://github.com/ssh-vault/ssh-vault) - 使用 ssh 密钥加密/解密文件
* [ssh-ping](https://github.com/vaporup/ssh-tools) [![stars](https://img.shields.io/github/stars/vaporup/ssh-tools.svg?style=social&label=stars)](https://github.com/vaporup/ssh-tools) - 使用 ssh_config 检查主机是否可访问
* [SSHPry v2](https://github.com/nopernik/SSHPry2.0) [![stars](https://img.shields.io/github/stars/nopernik/SSHPry2.0.svg?style=social&label=stars)](https://github.com/nopernik/SSHPry2.0) - 监视和控制 SSH 连接客户端的 TTY
* [redial](https://github.com/taypo/redial) [![stars](https://img.shields.io/github/stars/taypo/redial?style=social)](https://github.com/taypo/redial) - 适用于 Unix 系统的基于终端的 SSH 会话管理器

### 自动化

* [Ansible](https://github.com/ansible/ansible) [![stars](https://img.shields.io/github/stars/ansible/ansible.svg?style=social&label=stars)](https://github.com/ansible/ansible) - 通过 *SSH* 进行应用程序部署、配置管理和编排。
* [rtop](https://github.com/rapidloop/rtop) [![stars](https://img.shields.io/github/stars/rapidloop/rtop.svg?style=social&label=stars)](https://github.com/rapidloop/rtop) - 基于 *SSH* 的交互式远程系统监控工具。
* [DSH - Dancer's shell / distributed shell](https://www.netfort.gr.jp/~dancer/software/dsh.html.en) - 用于从一个命令行执行多个远程 shell 命令的包装器。
* [parallel-ssh](https://github.com/ParallelSSH/parallel-ssh) [![stars](https://img.shields.io/github/stars/ParallelSSH/parallel-ssh.svg?style=social&label=stars)](https://github.com/ParallelSSH/parallel-ssh) - 提供并行版本的 OpenSSH 及相关工具。
* [SSH Power Tool](https://code.google.com/p/sshpt/) - 无需使用预共享密钥即可同时执行命令并将文件上传到许多服务器。

### 网络

* [安全外壳 Chrome 扩展](https://chrome.google.com/webstore/detail/secure-shell/pnhechapfaindjhompbnflcldabbghjo?hl=en)
* [GateOne](https://github.com/liftoff/GateOne) [![stars](https://img.shields.io/github/stars/liftoff/GateOne.svg?style=social&label=stars)](https://github.com/liftoff/GateOne) - HTML5 支持的终端模拟器和 *SSH* 客户端。
* [KeyBox](https://github.com/skavanagh/KeyBox) [![stars](https://img.shields.io/github/stars/skavanagh/KeyBox.svg?style=social&label=stars)](https://github.com/skavanagh/KeyBox) - 基于 Web 的 *SSH* 控制台，集中管理对系统的管理访问。
* [Apache Guacamole](https://guacamole.incubator.apache.org/) - Apache Guacamole 是一个基于 HTML5 的无客户端远程桌面网关。它支持 VNC、RDP 和 SSH 等标准协议。
* [SSHmon](https://github.com/hpello/sshmon) [![stars](https://img.shields.io/github/stars/hpello/sshmon.svg?style=social&label=stars)](https://github.com/hpello/sshmon) - 用于监控 SSH 连接并建立端口转发的实时 GUI。

### 测试/蜜罐

* [ssh-hammer](https://github.com/shazow/ssh-hammer) [![stars](https://img.shields.io/github/stars/shazow/ssh-hammer.svg?style=social&label=stars)](https://github.com/shazow/ssh-hammer) - *SSH* 负载测试工具。
* [kippo](https://github.com/desaster/kippo) [![stars](https://img.shields.io/github/stars/desaster/kippo.svg?style=social&label=stars)](https://github.com/desaster/kippo) - *SSH* 蜜罐。
* [cowrie](https://github.com/micheloosterhof/cowrie) [![stars](https://img.shields.io/github/stars/micheloosterhof/cowrie.svg?style=social&label=stars)](https://github.com/micheloosterhof/cowrie) - *SSH* 蜜罐（基于 kippo）。
* [sshmitm](http://linux.die.net/man/8/sshmitm) - *SSH* 中间的猴子。
* [ssh-audit](https://github.com/arthepsy/ssh-audit) [![stars](https://img.shields.io/github/stars/arthepsy/ssh-audit.svg?style=social&label=stars)](https://github.com/arthepsy/ssh-audit) - 用于 *SSH* 服务器审核的工具。
* [sshesame](https://github.com/jaksi/sshesame) [![stars](https://img.shields.io/github/stars/jaksi/sshesame.svg?style=social&label=stars)](https://github.com/jaksi/sshesame) - 一个假的 SSH 服务器，允许每个人登录并记录他们的活动。


### *SSH* 的替代方案

* [GoTTY](https://github.com/yudai/gotty) [![stars](https://img.shields.io/github/stars/yudai/gotty.svg?style=social&label=stars)](https://github.com/yudai/gotty) - 将您的终端共享为 Web 应用程序。
* [telnet](http://www.telnet.org/htm/faq.htm) - 一种未加密的网络协议和用于连接到远程计算机并发出命令的应用程序。
* [ttyd](https://github.com/tsl0922/ttyd) [![stars](https://img.shields.io/github/stars/tsl0922/ttyd.svg?style=social&label=stars)](https://github.com/tsl0922/ttyd) - 通过网络共享您的终端。
* [rsh](https://en.wikipedia.org/wiki/Remote_Shell) - 一种未加密的网络协议和应用程序，用于连接到远程计算机并发出命令。

## 图书馆

* C/C++
  * [libssh](https://www.libssh.org) - *SSH* 库。
* 戈兰
  * [crypto/ssh](https://godoc.org/golang.org/x/crypto/ssh) - 内置 *SSH* 客户端和服务器库。
* [sftp](https://github.com/pkg/sftp) [![stars](https://img.shields.io/github/stars/pkg/sftp.svg?style=social&label=stars)](https://github.com/pkg/sftp) - *SFTP* 支持 go.crypto/ssh 包。
* [go-sshkit](https://github.com/shazow/go-sshkit) [![stars](https://img.shields.io/github/stars/shazow/go-sshkit.svg?style=social&label=stars)](https://github.com/shazow/go-sshkit) - 用于在 Go 中构建 *SSH* 服务器和客户端的工具包。
* [Socker](https://github.com/cosiner/socker) [![stars](https://img.shields.io/github/stars/cosiner/socker.svg?style=social&label=stars)](https://github.com/cosiner/socker) - 用于简化 *SSH* 使用的 Go 库。
  * [go-sshkeys](https://github.com/moul/go-sshkeys) - Golang SSH 密钥操作库
* 爪哇
  * [jsch](http://www.jcraft.com/jsch/) - 纯 *java*、*BSD* 许可、*SSH2* 客户端库。
* JavaScript/Node.js
* [ssh2](https://github.com/mscdex/ssh2) [![stars](https://img.shields.io/github/stars/mscdex/ssh2.svg?style=social&label=stars)](https://github.com/mscdex/ssh2) - *SSH2* 客户端和服务器模块以纯 *JavaScript* 为 *node.js* 编写。
* Python
* [paramiko](https://github.com/paramiko/paramiko) [![stars](https://img.shields.io/github/stars/paramiko/paramiko.svg?style=social&label=stars)](https://github.com/paramiko/paramiko) - 原生 *Python* *SSHv2* 协议库。
* 红宝石
* [net-ssh](https://github.com/net-ssh/net-ssh) [![stars](https://img.shields.io/github/stars/net-ssh/net-ssh.svg?style=social&label=stars)](https://github.com/net-ssh/net-ssh) - *SSH*（协议 2）客户端的纯 *Ruby* 实现。

## 资源

### 教程

* [如何使用 *SSH* 连接到远程服务器](https://www.digitalocean.com/community/tutorials/how-to-use-ssh-to-connect-to-a-remote-server-in-ubuntu)
* [最佳实践](https://blog.0xbadc0de.be/archives/300)
* [授予对服务器的临时访问权限（使用签名的 *SSH* 密钥）](http://linux-audit.com/granting-temporary-access-to-servers-using-signed-ssh-keys/)
* [如何SSH无密码登录](https://www.rosehosting.com/blog/ssh-login-without-password-using-ssh-keys/)
* [Gist: SSH Recipes](https://gist.github.com/mjalajel/beaa91a5f8d04ebb464c2c28da01406a) - 编写出色的 ssh 配置文件的秘诀集合。

### 安全性

* [01/14/2016](https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2016-0777) - 整数溢出“CVE 2016 077[7-8]”。
* [Security/Guidelines/OpenSSH - MozillaWiki](https://wiki.mozilla.org/Security/Guidelines/OpenSSH) - `sshd\_config` 适用于 `6.7+`、`5.3`。
* [应用加密强化](https://github.com/BetterCrypto/Applied-Crypto-Hardening) [![stars](https://img.shields.io/github/stars/BetterCrypto/Applied-Crypto-Hardening.svg?style=social&label=stars)](https://github.com/BetterCrypto/Applied-Crypto-Hardening) - `6.X` 的 `sshd\_config`

### 文档

* [手册页](http://linux.die.net/man/1/ssh)
* [规格 (OpenSSH)](http://www.openssh.com/specs.html)
* [维基百科文章](https://en.wikipedia.org/wiki/Secure_Shell)

### 社区

* [StackOverflow](http://stackoverflow.com/questions/tagged/ssh)
* [ServerFault](http://serverfault.com/questions/tagged/ssh)

## 许可证

[![CC0](https://i.creativecommons.org/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

在法律允许的范围内，[Manfred Touron](https://github.com/moul) 已放弃本作品的所有版权以及相关或邻接权。
