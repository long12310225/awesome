# Nginx 资源 [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

涵盖 Nginx、Nginx + Lua、OpenResty 和 Tengine 的资源集合。

该列表由 [Frederic Cambus](https://www.cambus.net) 维护。如需更新，请在 Twitter 上关注我：[@fcambus](https://twitter.com/fcambus)

## 了解 Nginx

- [Nginx 的历史](https://www.nginx.com/wp-content/uploads/2014/11/Infographic_History-of-Nginx_FulI_20141101.png)
- [了解 Nginx 版本控制](https://www.f5.com/company/blog/nginx/nginx-1-18-1-19-released)
- [Nginx 创建者专访](https://web.archive.org/web/20180614224054/http://mindend.com/interview-with-the-creator-of-nginx/)
- [专访 Apache 竞争对手 NGINX 的作者 Igor Sysoev](https://freesoftwaremagazine.com/articles/interview_igor_sysoev_author_apaches_competitor_nginx/)
- [Nginx 在应用程序服务器前端的案例](https://www.cambus.net/the-case-for-nginx-in-front-of-application-servers/)
- [Nginx优化：了解sendfile、tcp_nodelay和tcp_nopush](https://fv.gs/nginx-optimization-understanding-sendfile-tcp-nodelay-and-tcp-nopush-c55cdd276765)

## 建筑

- [开源应用架构（第二卷）：nginx](https://aosabook.org/en/nginx.html)
- [Nginx Guts - 揭示 Nginx 内部结构](http://www.nginxguts.com/category/nginx/)
- [Nginx 发现之旅](https://www.nginx-discovery.com/)
- [Nginx 内部结构](https://www.slideshare.net/slideshow/nginx-internals/2028238)
- [NGINX 内部：我们如何设计性能和规模](https://blog.nginx.org/blog/inside-nginx-how-we-designed-for-performance-scale)
- [NGINX 中的线程池](https://www.f5.com/company/blog/nginx/thread-pools-boost-performance-9x)

## 配置

- [初学者指南](https://nginx.org/en/docs/beginners_guide.html)
- [按字母顺序排列的变量索引](https://nginx.org/en/docs/varindex.html)
- [Nginx 陷阱](https://www.nginx.com/resources/wiki/start/topics/tutorials/config_pitfalls/)
- [对 Nginx 有用的重写](https://www.engineyard.com/blog/useful-rewrites-for-nginx/)
- [Nginx 配置入门](https://blog.martinfjordvald.com/nginx-primer/)
- [Nginx 入门 2：从 Apache 到 Nginx](https://blog.martinfjordvald.com/nginx-primer-2-from-apache-to-nginx/)
- [了解 Nginx 配置继承模型](https://blog.martinfjordvald.com/understanding-the-nginx-configuration-inheritance-model/)
- [Nginx HTTP 服务器样板配置](https://github.com/h5bp/server-configs-nginx)
- [Nginx Boilerplate - 配置模板和一组方便的必备片段](https://github.com/nginx-boilerplate/nginx-boilerplate)
- [如何在 Apache 和 Nginx 中配置 OCSP 装订](https://sslmate.com/blog/post/ocsp_stapling_in_apache_and_nginx)
- [NGINX Config - 在线 nginx 配置生成器](https://www.digitalocean.com/community/tools/nginx)
- [适合开发者的 nginx 功能](https://alex.dzyoba.com/blog/nginx-features-for-developers/)
- [适合运营商的 nginx 功能](https://alex.dzyoba.com/blog/nginx-features-for-operators/)
- [避免十大 NGINX 配置错误](https://www.f5.com/company/blog/nginx/avoiding-top-10-nginx-configuration-mistakes)
- [Gixy - Nginx configuration static analyzer](https://github.com/yandex/gixy) - 维护的分叉：[gixy-ng](https://github.com/dvershinin/gixy)、[gixy-next](https://github.com/MegaManSec/Gixy-Next)
- [Nginx 通用配置 - 通用配置和片段](https://github.com/tldr-devops/nginx-common-configuration)

## 安全性

- [BunkerWeb - 基于 Nginx 的下一代开源 Web 应用程序防火墙 (WAF)](https://www.bunkerweb.io)

## 教程

- [NGINX 和 NGINX Plus 管理指南](https://docs.nginx.com/nginx/admin-guide/)
- [agentzh 的 Nginx 教程](https://openresty.org/download/agentzh-nginx-tutorials-en.html) ([来源](https://github.com/openresty/nginx-tutorials))
- [nginx.conf 脚本简介](https://agentzh.org/misc/slides/nginx-conf-scripting/nginx-conf-scripting.html)
- [使用 NGINX 和 NGINX Plus 进行负载平衡](https://www.f5.com/company/blog/nginx/load-balancing-with-nginx-plus) ([第 2 部分])https://www.f5.com/company/blog/nginx/load-balancing-with-nginx-plus-part-2))
- [优化 Nginx 以应对高流量负载](https://blog.martinfjordvald.com/optimizing-nginx-for-high-traffic-loads/)
- [NGINX 作为 WebSockets 代理](https://www.f5.com/company/blog/nginx/websocket-nginx)
- [HTTP Keepalive 连接和 Web 性能 ](https://www.f5.com/company/blog/nginx/http-keepalives-and-web-performance)
- [Nginx 上的 CORS](https://enable-cors.org/server_nginx.html)
- [使用 Nginx 和 Zopfli 提供预压缩内容](https://www.cambus.net/serving-precompressed-content-with-nginx-and-zopfli/)
- [FreeBSD 上的 Nginx](https://www.cambus.net/nginx-on-freebsd/)
- [使用新的调试功能来探测 NGINX 内部](https://www.nginx.com/blog/new-debugging-features-probe-nginx-internals/)
- [使用 NGINX 和 NGINX Plus 执行 A/B 测试](https://www.f5.com/company/blog/nginx/performing-a-b-testing-nginx-plus)
- [使用内核 TLS 和 SSL_sendfile() 提高 NGINX 性能](https://www.f5.com/company/blog/nginx/improving-nginx-performance-with-kernel-tls)

## 模块开发

- [官方开发指南](https://nginx.org/en/docs/dev/development_guide.html)
- [Nginx 模块开发指南](https://www.evanmiller.org/nginx-modules-guide.html)
- [Nginx 模块开发的高级主题](https://www.evanmiller.org/nginx-modules-guide-advanced.html)

## API

- [Telize - 基于 Nginx 和 Lua 构建的 JSON IP 和 GeoIP REST API（IP 地理定位）](https://www.telize.com)
- [GIN - JSON-API 框架](https://gin.io/)
- [Kong - 微服务和 API 的管理层](https://github.com/kong/kong)

## 黑客

- [Nginx JSON 黑客](https://web.archive.org/web/20140921162448/http://www.gabrielweinberg.com/blog/2011/07/nginx-json-hacks.html)
- [在 Nginx.conf 中使用环境变量](https://web.archive.org/web/20170712003702/https://docs.apitools.com/blog/2014/07/02/using-environment-variables-in-nginx-conf.html)
- [直接在 Nginx 配置文件中记录轮换](https://www.cambus.net/log-rotation-directly-within-nginx-configuration-file/)
- [使用 Nginx、syslog-ng 和 Redis 进行实时像素跟踪](https://benwilber.github.io/nginx/redis/syslog/pixel-tracking/2013/09/13/realtime-pixel-tracking-with-nginx-syslog-ng-and-redis.html)
- [Nginx 中的动态日志格式](https://benwilber.github.io/nginx/syslog/logging/2015/08/26/dynamic-log-formats-in-nginx.html)
- [捕获并延迟不需要的请求](https://github.com/p0pr0ck5/lua-resty-tarpit)
- [Nginx：缓存、缩略图、反向代理图像服务器？](https://charlesleifer.com/blog/nginx-a-caching-thumbnailing-reverse-proxying-image-server-/)

## 温馨提示

- [你不知道 Nginx 可以做的事情](https://www.slideshare.net/slideshow/5-things-you-didnt-know-nginx-could-do/35181267)
- [找到 nginx gzip_comp_level 的最佳位置](https://mjanja.ch/2015/03/finding-the-nginx-gzip_comp_level-sweet-spot/)
- [nginx 镜像提示和技巧](https://alex.dzyoba.com/blog/nginx-mirror/)

## Nginx+Lua

- [Nginx、Lua 及其他](https://agentzh.org/misc/slides/nginx-lua-and-beyond.pdf)
- [用 Lua 将 Nginx 推向极限](https://blog.cloudflare.com/pushing-nginx-to-its-limit-with-lua/)
- [通过 Lua 向 Nginx 添加 OAuth 支持](https://chairnerd.seatgeek.com/oauth-support-for-nginx-with-lua/)
- [在 Nginx 中使用 Lua 编写 libdrizzle 脚本](https://agentzh.org/misc/slides/libdrizzle-lua-nginx.pdf)
- [Nginx 和 Lua](https://web.archive.org/web/20141223070856/http://devblog.mixlr.com/2012/09/01/nginx-lua/)
- [用Lua编写Nginx认证模块](https://www.stavros.io/posts/writing-an-nginx-authentication-module-in-lua/)
- [使用 Nginx 和 Lua 在云中扩展 TextRazor](https://www.textrazor.com/blog/2013/03/scaling-textrazor-in-the-cloud-with-nginx-and-lua.html)
- [LSSO - 具有 OAuth 后端的 Lua + Nginx SSO 系统](https://github.com/pirogoeth/lsso)
- [使用 Lua 和 Redis 测量 Nginx 缓存性能](https://charlesleifer.com/blog/measuring-nginx-cache-performance-using-lua-and-redis/)
- [nginx-lua - 基于 Alpine Linux、Amazon Linux、CentOS、Debian、Fedora 和 Ubuntu 的 Nginx 1.19+，支持 LUA。](https://github.com/fabiocicerchia/nginx-lua)

## Nginx+njs
- [njs 脚本语言参考和示例](https://nginx.org/en/docs/njs/)
- [njs用例集合](https://github.com/f5devcentral/nginx-njs-usecases)
- [NGINX 上嵌入的 JavaScript - njs 入门](https://www.bluedoa.com/javascript-embedded-on-nginx-getting-started-with-njs/)
- [在 JavaScript 中创建 Nginx 扩展](https://dev.to/metal3d/create-nginx-extensions-in-javascript-3310)
- [使用 njs 0.7.7 让您的 nginx 配置更加模块化和可重用](https://www.f5.com/company/blog/nginx/make-nginx-config-even-more-modular-reusable-njs-0-7-7)
- [使用 NGINX JavaScript 模块进行诊断日志记录](https://www.f5.com/company/blog/nginx/diagnostic-logging-nginx-javascript-module)
- [如何使用 NGINX 和 njs 记录请求标头](https://wildwolf.name/how-to-log-request-headers-with-nginx-and-njs/)
- [通过 njs 使用 NGINX 作为对象存储网关](https://blog.nginx.org/blog/using-nginx-as-object-storage-gateway/)
- [通过 njs 使用 NGINX 和 ACME 轻松实现 HTTPS](https://steinkamp.us/posts/2023-08-10_easy-https-with-nginx)

## OpenResty

- [OpenResty - 通过扩展 Nginx 实现快速 Web 应用程序服务器](https://openresty.org/en/)
- [Lapis - 由 OpenResty 提供支持的 Lua 或 MoonScript Web 框架](https://leafo.net/lapis/)
- [使用 OpenResty 和 Lua 的 Nginx 图像处理服务器](https://leafo.net/posts/creating_an_image_server.html)
- [构建 OpenResty 事件服务器](https://github.com/cagerton/dropthat/)
- [SysAdvent 2014 - OpenResty、Nginx 和 Lua](https://sysadvent.blogspot.com/2014/12/day-22-largely-unappreciated.html) ([来源](https://github.com/lusis/sysadvent-2014))
- [Ceryx - 动态反向代理](https://www.sourcelair.com/blog/articles/75/ceryx-dynamic-nginx)
- [OpenResty 简介](https://www.openmymind.net/An-Introduction-To-OpenResty-Nginx-Lua/)
- [OpenResty 编程（由 OpenResty 创建者编写）](https://openresty.gitbooks.io/programming-openresty/content/)
- [VeryNginx - Nginx 发行版，提供 WAF、控制面板和仪表板](https://github.com/alexazhou/VeryNginx)

## 特引擎

- [Tengine网络服务器](https://tengine.taobao.org)
- [OpenResty 和 Tengine 的区别](https://github.com/openresty/openresty/issues/54)

## 会谈

- [NGINX 会议 2019 视频](https://www.youtube.com/playlist?list=PLGz_X9w9raXflDvBv642YFqT0UTqQGFsH)
- [NGINX 会议 2018 视频](https://www.youtube.com/playlist?list=PLGz_X9w9raXe_Vc708VKvr5KJ4gnf1WxS)
- [NGINX 会议 2017 视频](https://www.youtube.com/playlist?list=PLGz_X9w9raXeT-z_rcZ9yF0kV5SENZ-yt)
- [NGINX 会议 2016 视频](https://www.youtube.com/playlist?list=PLGz_X9w9raXcOsB_dT26iu0BvbSxWYG1g)
- [NGINX 会议 2015 视频](https://www.youtube.com/playlist?list=PLGz_X9w9raXdED9BR6GQ61A6d3fBzjpbn)
- [NGINX 会议 2014 视频](https://www.youtube.com/playlist?list=PLGz_X9w9raXewvc6tjIGGFZ6DBKHEld3k)
- [2014 年 NGINX 用户峰会 - 闪电演讲](https://www.youtube.com/playlist?list=PLGz_X9w9raXfTnRnI6Xl0LMhAKoTVVZv8)

## 许可证

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

在法律允许的范围内，[Frederic Cambus](https://www.cambus.net) 已放弃本作品的所有版权以及相关或邻接权。
