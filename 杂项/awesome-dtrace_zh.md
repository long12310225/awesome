# 很棒的 DTrace [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

精彩的 DTrace 书籍、文章、视频、工具和资源的精选列表。

## 内容

- [Learn](#learn)
- [Articles](#articles)
- [Videos](#videos)
- [Software](#software)
- [Tools](#tools)
- [Community](#community)
- [Contributing](#contributing)

- - -

## 学习

学习 DTrace 的推荐阅读材料。

### 书籍

- [Dynamic Tracing Guide](http://dtrace.org/guide/preface.html) - Illumos.org DTrace 指南。
- [DTrace: Dynamic Tracing in Oracle Solaris, Mac OS X, and FreeBSD](http://www.dtracebook.com/index.php/Main_Page) - DTrace 官方书籍。
- [Dynamic Tracing with DTrace & SystemTap](http://myaut.github.io/dtrace-stap-book/) - 一本书介绍了 DTrace 和 SystemTap。

### 其他

- [dtrace(1m) man page](https://illumos.org/man/1m/dtrace) - DTrace 手册页。
- [DTrace cheatsheet](http://www.brendangregg.com/DTrace/DTrace-cheatsheet.pdf) - Brendan Gregg 的 DTrace 备忘单。
- [DTrace one-liners](http://www.brendangregg.com/DTrace/dtrace_oneliners.txt) - DTrace 1 衬垫。方便的命令。
- [DTrace one-liners (FreeBSD)](https://wiki.freebsd.org/DTrace/One-Liners) - 来自 FreeBSD 的 DTrace oneliners。
- [DTrace QuickStart](http://www.tablespace.net/quicksheet/dtrace-quickstart.html) - DTrace 快速入门指南。
- [Using DTrace stories](https://github.com/NanXiao/using-dtrace-stories) - 使用 DTrace 调试系统故事的集合。
- [Advanced DTrace Tips, Tricks and Gotchas](http://dtrace.org/resources/bmc/dtrace_tips.pdf) - 使用 DTrace 的高级技巧集合。

## 文章

有关 DTrace 和实际用例的有趣文章。

### PID提供者

- [pid provider: entry probe](http://dtrace.org/blogs/brendan/2011/02/09/dtrace-pid-provider/) - DTrace PID 提供程序。
- [pid provider: entry arguments](http://dtrace.org/blogs/brendan/2011/02/11/dtrace-pid-provider-arguments/) - DTrace PID 提供程序参数。
- [pid provider: return](http://dtrace.org/blogs/brendan/2011/02/14/dtrace-pid-provider-return/) - DTrace PID 提供程序返回。
- [pid provider: instructions](http://dtrace.org/blogs/brendan/2011/02/16/dtrace-pid-provider-instructions/) - DTrace PID 提供程序说明。
- [pid provider: overhead](http://dtrace.org/blogs/brendan/2011/02/18/dtrace-pid-provider-overhead/) - DTrace PID 提供程序开销。
- [pid provider exposed](http://dtrace.org/blogs/ahl/2005/03/01/pid-provider-exposed/) - Adam Leventhal 的 PID 提供程序内部结构。
- [When magic collides](http://dtrace.org/blogs/bmc/2011/03/09/when-magic-collides/) - Bryan Cantrill 对 PID 提供程序错误进行了深入探讨。

### USDT提供商

- [Understanding DTrace ustack helpers](http://dtrace.org/blogs/dap/2013/11/20/understanding-dtrace-ustack-helpers/) - DTrace ustack 助手。
- [USDT Providers Redux](http://dtrace.org/blogs/dap/2011/12/13/usdt-providers-redux/) - 在自定义应用程序中构建 USDT 提供商的参考。

### 系统事件提供商

- [DTrace sysevent provider](https://blogs.oracle.com/eschrock/entry/dtrace_sysevent_provider) - DTrace 的 Solaris/illumos sysevent 提供程序。

### Ruby 和 DTrace

- [Using DTrace to measure mutex contention in Ruby](https://vaneyckt.io/posts/using_dtrace_to_measure_mutex_contention_in_ruby/) - Ruby 中的互斥锁争用测量。

### 可视化方法

- [Flamegraphs](http://www.brendangregg.com/flamegraphs.html) - 分析软件的可视化，可以快速准确地识别最常见的代码路径。
- [Heat Maps](http://brendangregg.com/heatmaps.html) - 热图允许可视化三个维度的数据，类似于使用颜色作为维度的天气雷达图。

## 视频

有关 DTrace 的有趣视频。

- [DTrace review](https://www.youtube.com/watch?v=TgmA48fILq8) - Bryan Cantrill 解释了如何使用 DTrace 显着改进开发系统和实时系统的调试。

### dtrace.conf

- [dtrace.conf 2008](https://youtu.be/RvyP61WeFdM?list=PL8516982CBF9FADCC)
    - [NFSv3 和 iSCSI 提供商](https://www.youtube.com/watch?v=sgBCz7bXkSo&index=4&list=PL8516982CBF9FADCC)
    - [硬件 DTrace](https://www.youtube.com/watch?v=1Bc2Dz8aS6s&list=PL8516982CBF9FADCC&index=5)
    - [区域和 DTrace](https://www.youtube.com/watch?v=D8_onK0pSvA&index=8&list=PL8516982CBF9FADCC)
    - [DTrace Solaris 构建](https://www.youtube.com/watch?v=e55iXXYj-74&index=10&list=PL8516982CBF9FADCC)
    - [战争故事](https://www.youtube.com/watch?v=yR39YqVXQOM&index=11&list=PL8516982CBF9FADCC)
    - [太阳基准](https://www.youtube.com/watch?v=uK0DjEXo99w&list=PL8516982CBF9FADCC&index=12)
    - [Erlang](https://www.youtube.com/watch?v=PXIGE5GFAkE&index=13&list=PL8516982CBF9FADCC)
    - [Erlang（续）](https://www.youtube.com/watch?v=YTNiCv9Za2Y&index=14&list=PL8516982CBF9FADCC)
    - [检测 Adobe AIR](https://www.youtube.com/watch?v=4astU1_X5xM&index=15&list=PL8516982CBF9FADCC)
    - [HotSpot 运行时和 Java](https://www.youtube.com/watch?v=8kdJDHqiByI&list=PL8516982CBF9FADCC&index=16)
    - [PostgreSQL：深入了解 Solaris](https://www.youtube.com/watch?v=p5NKcxDny_4&list=PL8516982CBF9FADCC&index=17)
    - [PostgreSQL 提供商](https://www.youtube.com/watch?v=SJykRURWgeU&list=PL8516982CBF9FADCC&index=18)
    - [分布式DTrace](https://www.youtube.com/watch?v=oYK1kgFwxk4&index=19&list=PL8516982CBF9FADCC)
    - [DTrace 的 Apple 端口](https://www.youtube.com/watch?v=OKSuox4eFrk&list=PL8516982CBF9FADCC&index=21)

- [dtrace.conf 2012](https://www.youtube.com/watch?v=l_7v7Fn7uMQ&list=PL973D48F273EB0360)
    - [DTrace 国情咨文](https://www.youtube.com/watch?v=l_7v7Fn7uMQ&list=PL973D48F273EB0360)
    - [用户级CTF](https://www.youtube.com/watch?v=0QF04ivO_WE&list=PL973D48F273EB0360&index=3)
    - [动态翻译器](https://www.youtube.com/watch?v=CqLcj0lVnp4&index=4&list=PL973D48F273EB0360)
    - [DTrace 的 Clang 解析器](https://www.youtube.com/watch?v=6NqV_Uj8Ba4&index=7&list=PL973D48F273EB0360)
    - [Visualizations](https://www.youtube.com/watch?v=XD5hdaWnQM4&index=8&list=PL973D48F273EB0360)
    - [可视化，为无缝 USDT 启用工具链](https://www.youtube.com/watch?v=3Sqa8mmtnMM&index=9&list=PL973D48F273EB0360)
    - [更多可视化](https://www.youtube.com/watch?v=-B6u6wY3Iro&index=10&list=PL973D48F273EB0360)
    - [Node.js 中的 DTrace](https://www.youtube.com/watch?v=0ZMvSh7lUdM&list=PL973D48F273EB0360&index=11)
    - [DTrace 和 Erlang](https://www.youtube.com/watch?v=4Si-7nAic2c&list=PL973D48F273EB0360&index=12)
    - [Linux 上的 DTrace](https://www.youtube.com/watch?v=NElog3MvUC8&list=PL973D48F273EB0360&index=13)
    - [ZFS 提供商](https://www.youtube.com/watch?v=m_V7yrrn49Y&index=14&list=PL973D48F273EB0360)
    - [FreeBSD 上的 DTrace](https://www.youtube.com/watch?v=s5PpSiPfSNI&index=15&list=PL973D48F273EB0360)
    - [采用 DTrace 的障碍](https://www.youtube.com/watch?v=P95LHZ-WOWw&index=16&list=PL973D48F273EB0360)

- [dtrace.conf 2016](https://www.joyent.com/about/events/2016/dtrace-conf)
    - [Introduction](https://player.vimeo.com/video/173346406)
    - [（有用！）DTrace 简介](https://player.vimeo.com/video/173346405)
    - [CTF无处不在！](https://player.vimeo.com/video/173346404)
    - [分布式DTrace](https://player.vimeo.com/video/173346403)
    - [DTraign 应用程序](https://player.vimeo.com/video/173346402)
    - [DTrace 和 JSON：终于在一起了！](https://player.vimeo.com/video/173346401)
    - [ASSERT() 作为 DTrace 探针（以及为什么我需要一些帮助）](https://player.vimeo.com/video/173346400)
- [在 FreeBSD 中实现（或不实现）fds[]](https://player.vimeo.com/video/173346399)
    - [OpenDTrace](https://player.vimeo.com/video/173346398)
    - [通过始终在线的仪器提高 DTrace 性能](https://player.vimeo.com/video/173300658)
    - [D 语言改进](https://player.vimeo.com/video/173300657)
    - [D 语法糖](https://player.vimeo.com/video/173300656)
    - [DTrace 和 Go](https://player.vimeo.com/video/173300655)
    - [DTrace 和 Postgres](https://player.vimeo.com/video/173300654)
    - [区域中的 DTrace](https://player.vimeo.com/video/173300653)
    - [DTrace ustack() 性能改进](https://player.vimeo.com/video/173300651)
    - [DTrace 漏洞利用](https://player.vimeo.com/video/173300650)

## 软件

支持 DTrace 的软件列表。

### 编程语言

#### 埃尔兰

- [Erlang](http://erlang.org/doc/apps/runtime_tools/DTRACE.html) - DTrace 和 Erlang/OTP。

#### 卢阿

- [lua-usdt](https://github.com/chrisa/lua-usdt) - Lua 的 Libusdt 绑定。

#### Node.js

- [node-dtrace-provider](https://github.com/chrisa/node-dtrace-provider) - Node.js 应用程序的本机 DTrace 探针。

#### 珀尔

- [perl-Devel-DTrace-Provider](https://github.com/chrisa/perl-Devel-DTrace-Provider) - libusdt 的 Perl 包装器。

#### PHP

- [PHP](https://secure.php.net/manual/en/features.dtrace.dtrace.php) - 使用 PHP 和 DTrace。

#### 蟒蛇

- [Python](https://www.jcea.es/artic/python_dtrace.htm) - 适用于 Python 2.7.x 和 3.x 的 DTrace 补丁。
- [python-usdt](https://github.com/nshalman/python-usdt) - Python 的 Libusdt 绑定。

#### 红宝石

- [Ruby](http://ruby-doc.org/core-2.3.1/doc/dtrace_probes_rdoc.html) - Ruby DTrace 探针。
- [ruby-usdt](https://github.com/kevinykchan/ruby-usdt) - 用于 ruby​​ 应用程序的本机 DTrace 探针。

### 数据库

- [MySQL](https://dev.mysql.com/doc/refman/5.7/en/dba-dtrace-mysqld-ref.html) - MySQL DTrace 探针。
- [PostgreSQL](https://www.postgresql.org/docs/current/static/dynamic-trace.html) - PostgreSQL DTrace 探针。

### 网络服务器

- [mod_usdt](https://github.com/davepacheco/mod_usdt) - “httpd”DTrace 提供程序。

### 可视化

- [FlameGraph](https://github.com/brendangregg/FlameGraph) - 堆栈跟踪可视化工具。
- [node-stackvis](https://github.com/joyent/node-stackvis) - 堆栈跟踪可视化工具。

## 工具

- [DTraceToolkit](http://www.brendangregg.com/dtracetoolkit.html) - 有用的记录 DTrace 脚本的集合。
- [dtrace-cloud-tools](https://github.com/brendangregg/dtrace-cloud-tools) - 为 SmartOS/SmartDataCenter 云（基于 illumos）编写的 DTrace 工具。
- [pgsql tools](https://github.com/joyent/pgsqlstat) - 报告顶级 PostgreSQL 统计信息。
- [portsnoop](https://github.com/davepacheco/portsnoop) - 跟踪事件端口活动。
- [storage tools](https://github.com/richardelling/tools) - 报告 NFS、CIFS 和 iSCSI 统计信息。

## 社区

- [Community site](http://dtrace.org) - DTrace 社区网站。
- [Mailing list](http://dtrace.org/blogs/mailing-list/) - DTrace 社区邮件列表。
- [FreeBSD DTrace mailing list](https://lists.freebsd.org/mailman/listinfo/freebsd-dtrace) - FreeBSD DTrace 社区邮件列表。
- [China DTrace](http://chinadtrace.org/) - 一个中文 DTrace 网站。

## 贡献

非常欢迎您的贡献！请先参阅[贡献指南](https://github.com/xen0l/awesome-dtrace/blob/master/CONTRIBUTING.md)。
