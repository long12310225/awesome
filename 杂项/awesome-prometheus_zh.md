# 很棒的普罗米修斯  [![Awesome](https://awesome.re/badge-flat.svg)](https://github.com/sindresorhus/awesome)

> 精彩的 Prometheus 资源、项目和工具的精选列表。

<!--lint ignore double-link-->
[![Prometheus](media/prometheus.png)](https://prometheus.io/)

Prometheus 是一个开源系统监控和警报工具包。

## 内容
- [官方资源](#official-resources)
- [Tutorials](#tutorials)
- [Books](#books)
- [Videos](#videos)
- [播客和采访](#podcasts-and-interviews)
- [Presentations](#presentations)
- [博客文章和意见](#blog-posts-and-opinions)
- [部署工具](#deployment-tools)
- [Dashboards](#dashboards)
- [Exporters](#exporters)
    - [Databases](#databases)
    - [硬件相关](#hardware-related)
    - [HTTP](#http)
    - [其他监控系统](#other-monitoring-systems)
    - [Miscellaneous](#miscellaneous)
- [Alertmanager](#alertmanager)
- [Proxies](#proxies)
- [高可用性](#high-availability)
- [Uncategorized](#uncategorized)

## 官方资源
<!--lint ignore double-link-->
- [Website](https://prometheus.io/) - 普罗米修斯项目官方网站。
- [GitHub repository](https://github.com/prometheus/prometheus) - Prometheus 的源代码、问题讨论和协作。
- [Documentation](https://prometheus.io/docs/introduction/overview/) - 普罗米修斯官方文档。
- [Blog](https://prometheus.io/blog/) - 普罗米修斯官方博客。
- [Official Prometheus demo](https://demo.do.prometheus.io) - 由 Cloud Alchemy Ansible 角色管理的官方 Prometheus 演示站点使用 [Prometheus 存储库](https://github.com/prometheus/demo-site) 中的配置每日更新。

## 教程
- [Kubernetes monitoring with Prometheus, the ultimate guide](https://sysdig.com/blog/kubernetes-monitoring-prometheus/) - 使用 Prometheus 进行 Kubernetes 监控，Mateo Burillo 的终极指南。
- [How To Install Prometheus using Docker on CentOS 7](https://www.digitalocean.com/community/tutorials/how-to-install-prometheus-using-docker-on-centos-7) - 演练如何在 CentOS 7 上安装 Prometheus。
- [How to Use Prometheus to Monitor Your CentOS 7 Server](https://www.digitalocean.com/community/tutorials/how-to-use-prometheus-to-monitor-your-centos-7-server) - 演练如何使用 Prometheus 监控 CentOS 7 服务器。
- [How To Add a Prometheus Dashboard to Grafana](https://www.digitalocean.com/community/tutorials/how-to-add-a-prometheus-dashboard-to-grafana) - 演练如何将 Prometheus 仪表板添加到 Grafana。
- [Instructions and example code for a Prometheus workshop](https://github.com/juliusv/prometheus_workshop) - Julius Volz 的 Prometheus 研讨会的说明和示例代码。
- [Checking if SSH is responding with Prometheus](https://www.robustperception.io/checking-if-ssh-is-responding-with-prometheus/) - Brian Brazil 演练了如何使用 Blackbox Exporter 检查 SSH 是否响应。
- [Monitor your GitHub Repos with Docker and Prometheus](https://www.brianchristner.io/monitor-your-github-repos-with-docker/) - 使用 Docker 和 Prometheus 监控您的 GitHub 存储库。
- [Docker daemon metrics in Prometheus](https://medium.com/lucjuggery/docker-daemon-metrics-in-prometheus-7c359c7ff550) - Prometheus 中的 Docker 守护进程指标，作者：Luc Juggery。
- [Prometheus Monitoring Tutorial (10 minutes)](https://pagertree.com/blog/prometheus-monitoring-tutorial) - Austin Miller 编写的使用 Grafana、AlertManager 和 PagerTree 创建 Prometheus 监控堆栈的简单教程。
- [Prometheus-Basics](https://github.com/yolossn/Prometheus-Basics) - [yolossn](https://github.com/yolossn) 对 Prometheus 的初学者友好介绍。
- [Setting up Prometheus Monitoring On a Kubernetes Cluster](https://spacelift.io/blog/prometheus-kubernetes) - 在 Kubernetes 集群上设置 Prometheus 监控，作者：James Walker。

## 书籍
- [Monitoring with Prometheus](https://www.prometheusbook.com/) - James Turnbull 使用 Prometheus 进行监控。
- [Prometheus: Up & Running](http://shop.oreilly.com/product/0636920147343.do) - 普罗米修斯：布赖恩·巴西（Brian Brazil）的启动与运行。
- [Hands-On Infrastructure Monitoring with Prometheus](https://www.prombook.info/) - Joel Bastos 和 Pedro Araújo 的《使用 Prometheus 进行基础设施监控实践》，由 Brian Brazil 审阅。

## 视频
- [PromCon Online 2020](https://www.youtube.com/playlist?list=PLoz-W_CUquUm0r6nxziK9B9LnmNntzctE) - PromCon 在线 - 2020 年 7 月 14 日至 16 日。
- [PromCon 2019](https://www.youtube.com/playlist?list=PLoz-W_CUquUmIYKS97RBghcWumZIX2kvv) - PromCon 慕尼黑 - 2019 年 11 月 7-8 日，PromCon EU 2019。
- [An Introduction to Systems & Service Monitoring with Prometheus](https://www.youtube.com/watch?v=5O1djJ13gRU) - GOTO 2019：Prometheus 系统和服务监控简介 - Julius Volz。
- [Explain it Like I'm Five - What I Learned Teaching Observability to My Kids](https://vimeo.com/341142428) - Monitorama PDX，2019 - 戴夫·卡德沃拉德。
- [Prometheus Deep Dive](https://www.youtube.com/watch?v=Me-kZi4xkEs) - KubeCon - 2017 - GitLab：普罗米修斯深入研究 - Ben Kochie。
- [PromCon 2018](https://www.youtube.com/playlist?list=PLoz-W_CUquUlml1wBtQVBKErwoszt5B0h) - PromCon 慕尼黑 - 2018 年 8 月 9 日至 10 日 - 慕尼黑 PromCon 2018 的谈话录音。
- [Prometheus Monitoring for Java Web Applications w o Modifying Source Code](https://www.youtube.com/watch?v=BjyI93c8ltA) - Devoxx 比利时 - 2017 年 11 月 7 日 - Fabian Stäber。
- [PromCon 2017](https://www.youtube.com/playlist\?list\=PLoz-W_CUquUlnvoEBbqChb7A0ZEZsWSXt) - PromCon 慕尼黑 - 2017 年 8 月 17 日至 18 日 - 柏林 PromCon 2017 的谈话录音。
- [Best Practices and Beastly Pitfalls](https://www.youtube.com/watch?v=_MNYuTNfTb4) - PromCon 2017：最佳实践和可怕的陷阱 - Julius Volz。
- [Counting with Prometheus](https://www.youtube.com/watch?v=67Ulrq6DxwA) - 云原生 Con - 2017 - 用 Prometheus 计数 - Brian Brazil，稳健的感知。
- [Understanding and Extending Prometheus AlertManager](https://www.youtube.com/watch?v=jpb6fLQOgn4) - Cloud Native Con - 2017 - 了解和扩展 Prometheus AlertManager - Lee Calcote，SolarWinds。
- [Infrastructure and application monitoring using Prometheus](https://www.youtube.com/watch?v=5GYe_-qqP30) - Devoxx - 2017 年 5 月 17 日在 Devoxx UK - Marco Pas。
- [Prometheus Monitoring for Java Developers](https://www.youtube.com/watch?v=jb9j_IYv4cU) - Devoxx 比利时 - 2016 年 11 月 8 日 - Fabian Stäber。
- [Prometheus: Design and Philosophy - why it is the way it is](https://www.youtube.com/watch?v=QgJbxCWRZ1s) - Docker - 2016 年 10 月 14 日 - Julius Volz。
- [PromCon 2016](https://www.youtube.com/playlist?list=PLoz-W_CUquUlCq-Q0hy53TolAhaED9vmU) - PromCon Berlin - 2016 年 8 月 25 日至 26 日 - PromCon 2016 在柏林举行的谈话录音。
- [Prometheus: A Next Generation Monitoring System](https://www.youtube.com/watch?v=cwRmXqXKGtk) - FOSDEM 2016 - 2016 年 1 月 31 日 - 布莱恩·巴西。
- [The Prometheus Time Series Database](https://www.youtube.com/watch?v=HbnGSNEjhUc) - PromCon 2016：普罗米修斯时间序列数据库 - Björn Rabenstein。
- [PromCon 2016: So You Want to Write an Exporter](https://www.youtube.com/watch?v=KXq5ibSj2qA) - PromCon 2016 - 所以你想写一个导出器 - Brian Brazil。

## 播客和采访
- [Prometheus on FLOSS Weekly 357](https://twit.tv/shows/floss-weekly/episodes/357) - Julius Volz 在 FLOSS Weekly TWiT.tv 节目中。
- [Prometheus and Service Monitoring](https://changelog.com/podcast/168) - Julius Volz 在 Changelog 播客上。
- [Prometheus Monitoring with Brian Brazil](https://softwareengineeringdaily.com/2016/08/10/prometheus-monitoring-with-brian-brazil/) - Brian Brazil 在《软件工程日报》播客上。

## 演讲
- [Prometheus Overview](http://www.slideshare.net/brianbrazil/prometheus-overview) - Brian Brazil 的 Promethean 监控理想。
- [System Monitoring with Prometheus](http://www.slideshare.net/brianbrazil/devops-ireland-systems-monitoring-with-prometheus) - Brian Brazil 在都柏林 Devops Ireland 聚会上。
- [OMG! Prometheus](https://www.dropbox.com/s/0l7kxhjqjbabtb0/prometheus%20site-ops%20preso.pdf?dl=0) - Fitbit 站点运营人员 Benjamin Staffin 向他的团队解释了 Prometheus 的案例。
- [Deploying Prometheus](https://fosdem.org/2017/schedule/event/deploying_prometheus_at_wikimedia_foundation/attachments/slides/1773/export/events/attachments/deploying_prometheus_at_wikimedia_foundation/slides/1773/Prometheus_at_WMF_Fosdem_2017.pdf) - Filippo Giunchedi，维基媒体基金会，FOSDEM 2017。

## 博客文章和意见
- [Prometheus: Monitoring at SoundCloud](https://developers.soundcloud.com/blog/prometheus-monitoring-at-soundcloud) - Prometheus 概述和 Soundcloud 的第一手经验。
- [Monitor Docker Containers with Prometheus](http://5pi.de/2015/01/26/monitor-docker-containers-with-prometheus/) - 使用 Prometheus 监控 Docker 容器。
- [Prometheus and Kubernetes: A Perfect Match](https://www.weave.works/prometheus-kubernetes-perfect-match/) - _Prometheus 和 Kubernetes_ 系列中的第 1 部分（共 3 部分）。
- [Prometheus and Kubernetes: Deploying](https://www.weave.works/prometheus-kubernetes-deploying/) - _Prometheus 和 Kubernetes_ 系列中的第 2 部分（共 3 部分）。
- [Prometheus and Kubernetes: Monitoring Your Applications](https://www.weave.works/prometheus-and-kubernetes-monitoring-your-applications/) - 系列的第 3 部分_Prometheus 和 Kubernetes_。
- [Robust Perception](https://www.robustperception.io/tag/prometheus/) - Brian Bazil 撰写的多篇有关 Prometheus 的博客文章。
- [Initial experiences with the Prometheus monitoring system](https://medium.com/@griggheo/initial-experiences-with-the-prometheus-monitoring-system-167054ac439c#.q565suk4h) - Grig Gheorghiu 对普罗米修斯的初步体验。
- [Monitor your applications with Prometheus](http://blog.alexellis.io/prometheus-monitoring/) - 使用 Alex Ellis 的 Prometheus 监控您的应用程序。
- [Practical Services Monitoring with Prometheus and Docker](https://web.archive.org/web/20221206045124/https://airtame.engineering/practical-services-monitoring-with-prometheus-and-docker-30abd3cf9603?gi=b81b1156b4d9) - Simon KP 使用 Prometheus 和 Docker 进行实用服务监控。
- [Prometheus Blog Series (Part 1): Metrics and Labels](https://pierrevincent.github.io/2017/12/prometheus-blog-series-part-1-metrics-and-labels/) - 皮埃尔·文森特 (Pierre Vincent) 的_普罗米修斯博客系列_系列的第 1 部分。
- [Prometheus Blog Series (Part 2): Metric types](https://pierrevincent.github.io/2017/12/prometheus-blog-series-part-2-metric-types/) - 皮埃尔·文森特 (Pierre Vincent) 的_普罗米修斯博客系列_系列的第 2 部分。
- [Prometheus Blog Series (Part 3): Exposing and collecting metrics](https://pierrevincent.github.io/2017/12/prometheus-blog-series-part-3-exposing-and-collecting-metrics/) - 皮埃尔·文森特 (Pierre Vincent) 的_普罗米修斯博客系列_系列的第 3 部分。
- [Prometheus Blog Series (Part 4): Instrumenting code in Go and Java](https://pierrevincent.github.io/2017/12/prometheus-blog-series-part-4-instrumenting-code-in-go-and-java/) - 皮埃尔·文森特的_普罗米修斯博客系列_系列的第 4 部分。
- [Horizontal Pod Autoscaling in Kubernetes with Prometheus](https://livewyer.io/blog/2019/05/28/horizontal-pod-autoscaling/) - Louise 使用 Prometheus 在 Kubernetes 中进行水平 Pod 自动缩放。
- [PromQL tutorial for beginners](https://medium.com/@valyala/promql-tutorial-for-beginners-9ab455142085) - Aliaksandr Valialkin 为初学者编写的 PromQL 教程。
- [Prometheus storage: technical terms explained](https://medium.com/@valyala/prometheus-storage-technical-terms-for-humans-4ab4de6c3d48) - 普罗米修斯存储：Aliaksandr Valialkin 为人类提供的技术术语。
- [Alerting issues with Alertmanager](https://ali.sattari.me/posts/2020/alerting-issues-with-alertmanager/) - 由 [Ali Sattari](https://github.com/ali-sattari) 解决 Alertmanager 中的警报抖动和重复问题。
- [Contributing to Prometheus](https://atibhiagrawal.medium.com/contributing-to-prometheus-2bf35bd28256) - Atibhi Agrawal 为 Prometheus 做出的贡献。
- [Simple Prometheus queries for metrics inspection](https://mkaz.me/blog/2023/simple-prometheus-queries-for-metrics-inspection/) - Michal Kazmierczak 帮助识别高基数指标的 PromQL 查询概述。
- [Learn Prometheus](https://pagertree.com/learn/prometheus) - PagerTree LLC 的 Prometheus 速成课程。

## 部署工具
- [Ansitheus](https://github.com/ntk148v/ansitheus) - Ansible playbook，用于容器化、配置和部署 Prometheus 生态系统_by ntk148v_。
- [Cloud Alchemy Ansible roles](https://github.com/cloudalchemy) - Ansible 角色用于管理 Prometheus、Alertmanager、Grafana 和常见的 Prometheus 导出器。
- [Ansible-prometheus](https://github.com/ernestas-poskus/ansible-prometheus) - 用于安装 Prometheus 监控系统、导出器（例如：node、snmp、blackbox）的 Ansible playbook，以及警报管理器和推送网关_Ernestas Poskus_。
- [Click-to-deploy Prometheus](https://github.com/GoogleCloudPlatform/click-to-deploy/tree/master/k8s/prometheus) - Google Cloud Marketplace _by GoogleCloudPlatform_ 上列出的 Google Click to Deploy Prometheus 解决方案的来源。
- [Prometheus Operator](https://github.com/coreos/prometheus-operator) - Prometheus Operator 通过 CoreOS 在 Kubernetes 上创建/配置/管理 Prometheus 集群。

## 仪表板
- [Grafana](https://prometheus.io/docs/visualization/grafana/) - Grafana 是一个开源指标分析和可视化套件_Prometheus 的教程_。
- [Prometheus Monitoring with Grafana](http://logz.io/blog/prometheus-monitoring/) - 使用 Grafana _logz.io_ 提供的 Prometheus 监控_教程。

## 出口商
下面的列表包含由 [Prometheus GitHub 组织](https://github.com/prometheus) 维护的所有官方 Prometheus 导出器。有关包括任何非官方导出商在内的导出商的完整列表，请参阅 [prometheus.io](https://prometheus.io/docs/instrumenting/exporters/) 或 [exporterhub.io](https://exporterhub.io) 以获取 Prometheus 导出商的精选列表。

### 数据库
- [Consul exporter](https://github.com/prometheus/consul_exporter) - Consul 指标的导出器。
- [Memcached exporter](https://github.com/prometheus/memcached_exporter) - Memcached 导出器定期抓取 Memcached 统计信息。
- [MySQL server exporter](https://github.com/prometheus/mysqld_exporter) - MySQL 服务器导出器定期抓取 MySQL 统计信息。

### 硬件相关
- [Node/system metrics exporter](https://github.com/prometheus/node_exporter) - 节点导出器定期抓取系统统计信息。

### HTTP协议
- [HAProxy exporter](https://github.com/prometheus/haproxy_exporter) - HAProxy 导出器定期抓取 HAProxy 统计信息。

### 其他监控系统
- [AWS CloudWatch exporter](https://github.com/prometheus/cloudwatch_exporter) - Amazon AWS CloudWatch 指标的导出器。
- [Collectd exporter](https://github.com/prometheus/collectd_exporter) - Collectd 指标的导出器。
- [Graphite exporter](https://github.com/prometheus/graphite_exporter) - Graphite 指标的导出器。
- [InfluxDB](https://github.com/prometheus/influxdb_exporter) - InfluxDB 指标的导出器。
- [JMX exporter](https://github.com/prometheus/jmx_exporter) - JMX 指标的导出器。
- [SNMP exporter](https://github.com/prometheus/snmp_exporter) - SNMP 指标的导出器。
- [StatsD exporter](https://github.com/prometheus/statsd_exporter) - StatsD 指标的导出器。

### 杂项
- [Blackbox](https://github.com/prometheus/blackbox_exporter) - Blackbox 导出器允许通过 HTTP、HTTPS、DNS、TCP 和 ICMP 对端点进行黑盒探测。

## 警报管理器
- [Monitoring mixins](https://monitoring.mixins.dev) - 社区管理的警报、记录规则和 Grafana 仪表板包。
- [Awesome Prometheus Alerting Rules](https://github.com/samber/awesome-prometheus-alerts) - 很棒的 Prometheus 警报规则列表。
- [Karma](https://github.com/prymitive/karma) - Prometheus Alertmanager 的警报仪表板。

## 代理
- [Multi-prometheus proxy](https://github.com/matt-deboer/mpp) - 使用选择器策略将传入请求转发到部署为彼此 HA 副本的一组多个 Prometheus 实例之一。
- [Promxy](https://github.com/jacksontj/promxy) - 对 Prometheus HA 对中的数据进行重复数据删除。
- [Trickster](https://github.com/tricksterproxy/trickster) - 用于 HTTP 应用程序的 HTTP 反向代理/缓存以及用于时间序列数据库的仪表板查询加速器。
- [exporter_proxy](https://github.com/mrichar1/exporter_proxy) - 一个小型、简单的纯 python 反向代理，适用于 Prometheus 导出器，支持 TLS。
- [PromQL Guard](https://github.com/kfdm/promql-guard) - 在 Prometheus 之上提供瘦代理，允许检查和重写 PromQL 查询，以便租户只能看到允许的数据，即使在使用共享 Prometheus 服务器时也是如此。

## 高可用性
- [Cortex](https://github.com/cortexproject/cortex) - 水平可扩展、高可用、多租户、长期的 Prometheus。
- [Thanos](https://github.com/thanos-io/thanos) - 高度可用的 Prometheus 设置具有长期存储功能。
- [M3DB](https://github.com/m3db/m3) - Prometheus 的可扩展长期远程存储。
- [VictoriaMetrics](https://github.com/VictoriaMetrics/VictoriaMetrics) - 经济高效且易于操作的 Prometheus 远程存储。

## 未分类
- [Prometheus Monitoring subreddit](https://www.reddit.com/r/PrometheusMonitoring/) - Subreddit 收集互联网上所有与 Prometheus 相关的资源。
- [PromCon](https://promcon.io/) - 普罗米修斯会议。
