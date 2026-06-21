# 真棒influxdb [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

与 [InfluxDB](https://www.influxdata.com/) 相关的精彩项目、库、工具等的精选列表。
此列表重点关注支持 InfluxDB 1.0 及更高版本的库、工具等。

想让这个列表变得更好吗？
查看我们的 [contributing](CONTRIBUTING.md) 页面，然后打开拉取请求！

## 参考资料

如果您知道此列表中任何特别有用的博客文章、演讲、幻灯片等，请打开拉取请求！

* [官方文档](https://docs.influxdata.com/influxdb/latest/)
* IoT 世界中的 InfluxDB。 [第1部分：简介](https://www.easyitblog.info/2017/11/10/influxdb-and-grafana-fighting-together-with-iot-data-attack/) | [第 2 部分：在 AWS 上托管和扩展](https://www.easyitblog.info/2017/11/14/influxdb-in-iot-world-aws-part-2/) | [第3部分：使用Grafana绘制图表](https://www.easyitblog.info/2017/11/26/influxdb-in-iot-world-making-it-production-ready-part-3/)

## 客户端库

### 官方

* [C#](https://github.com/influxdata/influxdb-csharp) - 用于高效地将点发送到 InfluxDB 的 .NET 库
* [Go](https://github.com/influxdata/influxdb1-client) - InfluxDB 1.x 的 Go 客户端
* [Java](https://github.com/influxdata/influxdb-java) - InfluxDB 的 Java 客户端
* [PHP](https://github.com/influxdata/influxdb-php) - InfluxDB 的 PHP 客户端
* [Python](https://github.com/influxdata/influxdb-python) - InfluxDB 的 Python 客户端
* [Rails](https://github.com/influxdata/influxdb-rails) - Ruby on Rails 绑定自动将指标写入 InfluxDB
* [Ruby](https://github.com/influxdata/influxdb-ruby) - InfluxDB 的 Ruby 客户端

### 非官方

* [capacitor](https://github.com/olauzon/capacitor) - InfluxDB 的 Clojure 客户端
* [cl-influxdb](https://github.com/mmaul/cl-influxdb) - 时间序列数据库 InfluxDB 的 Common Lisp 接口
* [erflux](https://github.com/gossiperl/erflux) - Erlang 的 InfluxDB 客户端
* [fluxter](https://github.com/lexmag/fluxter) - Elixir 的 InfluxDB 编写器
* [influent](https://github.com/gobwas/influent) - InfluxDB Javascript 驱动程序
* [influent.rs](https://github.com/gobwas/influent.rs) - InfluxDB Rust 驱动程序
* [InfluxDB-Client-for-Arduino](https://github.com/tobiasschuerg/InfluxDB-Client-for-Arduino) - InfluxDB 的 Arduino 客户端
* [InfluxDB-Client-LabVIEW](https://github.com/johanvandenbroek/InfluxDB-Client-LabVIEW) - InfluxDB 的 LabVIEW 客户端
* [influxdb-cpp-rest](https://github.com/d-led/influxdb-cpp-rest) - 具有批处理异步接口的 C++ InfluxDB 客户端
* [influxdb-haskell](https://github.com/maoe/influxdb-haskell) - InfluxDB 的 Haskell 客户端库
* [InfluxDB.NET](https://github.com/ziyasal/InfluxDB.Net) - InfluxDB 的 .NET 客户端
* [InfluxDB PHP SDK](https://github.com/corley/influxdb-php-sdk) - 用于读写数据的 UDP/IP 或 HTTP 适配器
* [influxdbr](https://github.com/dleutnant/influxdbr) - InfluxDB 的 R 库
* [instream](https://github.com/mneudert/instream) - Elixir 的 InfluxDB 驱动程序
* [node-influx](https://github.com/node-influx/node-influx) - InfluxDB Node.js 客户端
* [node-influx-udp](https://github.com/mediocre/node-influx-udp) - 使用 UDP 接口写入 InfluxDB
* [scala-influxdb-client](https://github.com/paulgoldbaum/scala-influxdb-client) - Scala 异步 InfluxDB 客户端

## 将数据收集到 InfluxDB 中

### 项目

#### 专用

主要或唯一目的是将数据输入 InfluxDB 的工具。

* [accelerometer2influx](https://github.com/CorpGlory/accelerometer2influx) - Android 应用程序从手机加速度计获取 x-y-z 轴指标并将数据发送到 InfluxDB。
* [agento](https://github.com/abrander/agento) - 客户端/服务器从 Linux 主机收集近乎实时的指标
* [aggregateD](https://github.com/ccpgames/aggregateD) - 受 [dogstatsD](https://docs.datadoghq.com/guides/dogstatsd/) 启发的 InfluxDB 指标和事件聚合守护进程
* [aprs2influxdb](https://github.com/FaradayRF/aprs2influxdb) - 连接业余无线电 APRS-IS 服务器并将数据包数据保存到 influxdb 数据库中
* [Charmander](https://github.com/att-innovate/charmander) - Charmander 是一个用于测量和分析资源调度算法的实验室环境
* [gopherwx](https://github.com/chrissnell/gopherwx) - 一项从 Davis Instruments Vantage Pro2 站提取实时天气数据并将其存储在 InfluxDB 中的服务
* [grade](https://github.com/influxdata/grade) - 通过将结果存储在 InfluxDB 中来跟踪 Go 基准性能随时间的变化
* [Influx-Capacitor](https://github.com/poxet/Influx-Capacitor) - Influx-Capacitor 使用性能计数器从 Windows 计算机收集指标。数据发送到 influxDB 以供 grafana 查看
* [Influxdb-Powershell](https://github.com/vsavornin/Influxdb-Powershell) - 用于将 Windows 性能计数器发送到 InfluxDB 服务器的 Powershell 脚本
* [influxdb-logger](https://github.com/codersaur/SmartThings/tree/master/smartapps/influxdb-logger) - SmartApp 将 [SmartThings](https://www.smartthings.com/) 设备属性记录到 InfluxDB 数据库
* [influxdb-sqlserver](https://github.com/zensqlmonitor/influxdb-sqlserver) - 收集 Microsoft SQL Server 指标以向 InfluxDB 报告并使用 Grafana 进行可视化
* [k6](https://github.com/loadimpact/k6) - 使用 Go 和 JavaScript 的现代负载测试工具
* [marathon-event-metrics](https://github.com/Wikia/marathon-event-metrics) - 用于向 InfluxDB 报告 [Marathon](https://mesosphere.github.io/marathon/) 事件的工具
* [mesos-influxdb-collector](https://github.com/kpacha/mesos-influxdb-collector) - InfluxDB 的轻量级 [mesos](https://mesos.apache.org/) 统计收集器
* [mqforward](https://github.com/shirou/mqforward) - [MQTT](http://mqtt.org/) 到 influxdb 转发器
* [node-opcua-logger](https://github.com/coussej/node-opcua-logger) - 从 OPC UA 服务器收集工业数据
* [ntp_checker](https://github.com/fss1/ntp_checker) - 比较内部 NTP 源，如果服务器之间的偏移量超过可定义的（分数）秒，则发出警告
* [proc_to_influxdb](https://github.com/d-led/proc_to_influxdb) - 通过 InfluxDB 观察 Windows 进程启动和停止的控制台应用程序
* [pysysinfo_influxdb](https://github.com/nagylzs/pysysinfo_influxdb) - 定期发送系统信息到influxdb（使用python3 + psutil，所以在Windows下也可以工作）
* [sysinfo_influxdb](https://github.com/novaquark/sysinfo_influxdb) - 收集系统（linux）信息并将其发送到 InfluxDB
* [snmpcollector](https://github.com/toni-moreno/snmpcollector) - 功能齐全的通用 SNMP 数据收集器，带有 InfluxDB 的 Web 管理界面
* [Telegraf](https://github.com/influxdata/telegraf) - （官方）插件驱动的服务器代理，用于将指标报告到 InfluxDB 中
* [tesla-streamer](https://github.com/timdorr/tesla-trip/blob/master/lib/tesla_stream_reader.rb) - 将数据从 Tesla Model S 流式传输到 InfluxDB（[rake 任务](https://github.com/timdorr/tesla-trip/blob/master/lib/tasks/tesla.rake#L12-L16)）
* [traffic_stats](https://traffic-control-cdn.readthedocs.io/en/latest/overview/traffic_stats.html) - 获取并存储有关 [Apache Traffic Control](https://trafficcontrol.apache.org/) 控制的 CDN 的统计信息
* [vsphere-influxdb-go](https://github.com/Oxalide/vsphere-influxdb-go) - 收集 VMware vSphere、vCenter 和 ESXi 性能指标并将其发送到 InfluxDB

#### 非专用

生成输入多个后端的数据的工具，包括 InfluxDB。

* [cAdvisor](https://github.com/google/cadvisor) - 分析运行容器的资源使用情况和性能特征
* [Centreon](https://github.com/centreon/centreon) - 网络、系统、应用的监管和监控工具
* [cernan](https://github.com/postmates/cernan) - 遥测和日志聚合服务器
* [cloudwatch-sender](https://github.com/BBC-News/cloudwatch-sender) - 从 [Amazon Cloudwatch](https://aws.amazon.com/cloudwatch/) 将指标发送到 InfluxDB/Graphite
* [crankshaftd](https://github.com/fullcontact/crankshaftd) - 简单的 Go 代理，通过 SSE 从 [Turbine](https://github.com/Netflix/Turbine) 获取流数据，并将其作为仪表推送到 StatsD 或 InfluxDB
* [Domoticz](https://www.domoticz.com) - 开源家庭自动化系统
* [gatling](https://github.com/gatling/gatling) - 基于异步 Scala-Akka-Netty 的压力工具
* [Glances](https://github.com/nicolargo/glances) - 监视您的系统
* [Graphios](https://github.com/shawn-sterling/graphios) - 将 nagios perf 数据发送到 Graphite (carbon) / statsd / librato / influxDB 的程序
* [heapster](https://github.com/kubernetes-retired/heapster) - 监控 [Kubernetes](https://kubernetes.io/) 集群的容器资源使用情况
* [heka](https://github.com/mozilla-services/heka) - 通用数据收集和处理工具
* [internet_data_usage](https://github.com/precurse/internet_data_usage) - 基于 Python 的应用程序可提取 Telus 和 Koodo 等不同运营商的数据计划使用情况
* [ioBroker](http://www.iobroker.net/) - 家庭自动化/物联网平台使用 Influxdb 存储[历史数据](https://github.com/ioBroker/ioBroker.influxdb/blob/master/README.md)
* [jmxtrans](https://github.com/jmxtrans/jmxtrans) - 实际上，一端通过 JMX 与 JVM 通信，另一端是您可以想象的任何日志记录/监视/图形包之间缺少连接器。
* [Apache JMeter](https://jmeter.apache.org/usermanual/realtime-results.html) - 流行的负载测试工具，您可以通过 InfluxDBBackendListenerClient 获取发送到后端的实时结果，它允许您使用 UDP 或 HTTP 协议将指标（活动线程、响应时间...）发送到 InfluxDB 后端
* [logary](https://github.com/logary/logary) - 适用于 mono 和 .Net 的高性能、多目标日志记录、指标和运行状况检查库
* [metrics.sh](https://github.com/pstadler/metrics.sh) - 使用可移植 shell 脚本收集和转发指标
* [OpenHAB](https://www.openhab.org/) - 适用于家庭自动化所有事物的通用集成平台
* [Riemann](https://github.com/riemann/riemann) - Clojure 中的网络事件流处理系统
* [statsd-jvm-profiler](https://github.com/etsy/statsd-jvm-profiler) - 使用 StatsD 的简单 JVM 分析器
* [statsite](https://github.com/statsite/statsite) - statsd的C实现
* [Sematext Agent](https://github.com/sematext/sematext-agent-integrations) - [开源监控代理](https://sematext.com/blog/now-open-source-sematext-monitoring-agent/) 通过可插入集成从 Solr、Elasticsearch、Cassandra、JVM、JMX、ClickHouse、MySQL、Hadoop 等收集指标。通过 Influx Line 协议输出到 InfluxDB 或 [Sematext Cloud](https://sematext.com/cloud/)
* [logagent](https://github.com/sematext/logagent-js) - 是一个现代的、开源的、轻量级的日志运输工具。 Logagent 包括 [influxdb 输入插件](https://sematext.com/docs/logagent/input-plugin-influxdb-http/) 和 [influxdb 输出插件](https://sematext.com/docs/logagent/output-plugin-influxdb/) 以及许多其他[集成](https://sematext.com/docs/logagent/plugins/)

### 图书馆

用于收集数据并输入 InfluxDB 的库。

* [crow-metrics](https://github.com/robey/crow-metrics) - 节点服务器的小型指标收集器
* [django-influxdb-metrics](https://github.com/bitlabstudio/django-influxdb-metrics) - 一个可重用的 Django 应用程序，它将有关您的项目的指标发送到 InfluxDB
* [go-runtime-metrics](https://github.com/tevjef/go-runtime-metrics) - 收集golang运行时Metrics，输出到InfluxDB或通过Telegraf
* [lua-resty-influx](https://github.com/p0pr0ck5/lua-resty-influx) - [OpenResty](https://openresty.org/en/) InfluxDB 客户端
* [metrics](https://github.com/beberlei/metrics) - (PHP) 抽象不同指标收集器的简单库。 “我发现有必要拥有一个一致且简单的指标（功能）API，并且不会导致供应商锁定”
* [pyVsphereInflux](https://github.com/fennm/pyVsphereInflux) - 用于从 [vSphere](https://www.vmware.com/products/vsphere.html) 提取数据并将其插入 InfluxDB 的库和支持脚本
* [telemetry](https://github.com/arussellsaw/telemetry) - Go 应用程序的指标报告

#### 挂钩

其他日志库输出到 InfluxDB 的挂钩。

* [go-metrics-influxdb](https://github.com/vrischmann/go-metrics-influxdb) - [go-metrics 库](https://github.com/rcrowley/go-metrics) 的记者，将把指标发布到 InfluxDB
* [logrus_influxdb](https://github.com/Abramovic/logrus_influxdb) - [Logrus] 的 InfluxDB 挂钩(https://github.com/Sirupsen/logrus)

### 插件

允许其他独立工具将数据发送到 InfluxDB 的插件。

* [embulk-output-influxdb](https://github.com/joker1007/embulk-output-influxdb) - [Embulk]的 InfluxDB 输出插件(https://github.com/embulk/embulk)
* [exometer_influxdb](https://github.com/travelping/exometer_influxdb) - [Exometer](https://github.com/Feuerlabs/exometer) InfluxDB 记者
* [fluent-plugin-influxdb](https://github.com/fangli/fluent-plugin-influxdb) - [fluxd](https://www.fluxd.org/) 和 InfluxDB 的缓冲输出插件
* [influx-nagios-plugin](https://github.com/shaharke/influx-nagios-plugin) - [Nagios](https://www.nagios.org/) 插件，用于从 InfluxDB 查询监控统计信息
* [jenkinsci/influxdb-plugin](https://github.com/jenkinsci/influxdb-plugin) - [Jenkins](https://jenkins.io/index.html) 插件，用于将构建指标发送到 InfluxDB
* [kafka-influxdb](https://github.com/mre/kafka-influxdb) - 用 Python 编写的 InfluxDB 的 [Kafka](https://kafka.apache.org/) 消费者
* [logstash-output-influxdb](https://github.com/logstash-plugins/logstash-output-influxdb) - 社区维护的 [Logstash](https://www.elastic.co/products/logstash) 插件，用于将指标输出到 InfluxDB
* [metrics-influxdb](https://github.com/davidB/metrics-influxdb) - [dropwizard](https://www.dropwizard.io/0.9.1/docs/) 指标的记者，向 InfluxDB 服务器公布测量结果
* [mod-influxdb](https://github.com/savoirfairelinux/mod-influxdb) - [Shinken](http://www.shinken-monitoring.org/) 用于将数据导出到 InfluxDB 的模块
* [sensu-plugins-influxdb](https://github.com/sensu-plugins/sensu-plugins-influxdb) - [Sensu](https://sensu.io/) InfluxDB 插件
* [sidekiq-influxdb](https://github.com/vassilevsky/sidekiq-influxdb) - 用于将作业执行指标发送到 InfluxDB 的 [Sidekiq](https://sidekiq.org/) 中间件
* [snap-plugin-publisher-influxdb](https://github.com/intelsdi-x/snap-plugin-publisher-influxdb) - 将 [snap](https://github.com/intelsdi-x/snap) 指标发布到 InfluxDB
* [statsd-influxdb-backend](https://github.com/bernd/statsd-influxdb-backend) - StatsD 的原生 InfluxDB 后端
* [logagent influx input plugin](https://sematext.com/docs/logagent/input-plugin-influxdb-http/) - Logagent 插件通过 Influx Line 协议接收数据
* [logagent InfluxDB output plugin](https://sematext.com/docs/logagent/input-plugin-influxdb-http/) - 通过 Influx Line 协议发送数据的插件


### 导入工具

将一组固定数据导入 InfluxDB 的工具。
* [JMeter2InfluxDB](https://github.com/soprasteria/jmeter2influxdb) - 在负载测试后读取 csv 文件中的 JMeter 结果并将结果放入 InfluxDB
* [LoadRunner Raw Results Exporter](https://admhelp.microfocus.com/lr/en/12.60-12.62/help/WebHelp/Content/Controller/raw_results_exporter.htm) - 将场景结果（负载测试结果）导出到 InfluxDB
* [nmon2influxdb](https://github.com/adejoux/nmon2influxdb) - 将 [nmon](http://nmon.sourceforge.net/pmwiki.php) 文件导入 InfluxDB

## 使用 InfluxDB 中的数据

### 仪表板和可视化

* [Chronograf](https://github.com/influxdata/chronograf) - InfluxDB官方数据可视化工具
* [DBeaver](https://dbeaver.com/databases/influxdb/) - DBeaver 通用数据库工具，DBeaver Enterprise 对 InfluxDB 有特殊扩展
* [facette](https://github.com/facette/facette) - 时间序列数据可视化和绘图软件
* [FluxDash](https://github.com/vrecan/FluxDash) - 基于终端的 InfluxDB 仪表板
* [grafana](https://github.com/grafana/grafana) - 适用于 Graphite、InfluxDB 和 OpenTSDB 的华丽指标可视化、仪表板和编辑器
* [InfluxDB Studio](https://github.com/CymaticLabs/InfluxDBStudio) - InfluxDB Studio是一个UI管理工具，其灵感来自于其他类似的SQL数据库管理工具（使用在MS Windows上运行的InfluxData.Net）
* [InfluxGraph](https://github.com/InfluxGraph/influxgraph) - 适用于 Graphite-API 的 Graphite InfluxDB 存储查找器
* [ostent](https://github.com/ostrost/ostent) - 收集并显示系统指标并可选择中继到 Graphite 和/或 InfluxDB

### 其他工具

* [hubot-influxdb-alerts](https://github.com/amwelch/hubot-influxdb-alerts) - 使用 [hubot](https://hubot.github.com/) 和 influxdb 在聊天室中创建和管理警报
* [influx-alert](https://github.com/joshrendek/influx-alert) - 查询 InfluxDB 并根据 YAML 配置发送警报的工具
* [influxdb_google_sheets](https://github.com/HormyAJP/influxdb_google_sheets) - 用于获取和格式化 InfluxDB 数据的 Google Sheets 脚本
* [Morgoth](https://github.com/nathanielc/morgoth) - 指标异常检测

## 配置 InfluxDB

帮助您运行 InfluxDB 的工具、库等，无需手动安装。

* [chef-influxdb](https://github.com/bdangit/chef-influxdb) - InfluxDB 的厨师食谱
* [golja-influxdb](https://github.com/dgolja/golja-influxdb) - InfluxDB 的 Puppet 模块
* [influxdb-formula](https://github.com/saltstack-formulas/influxdb-formula) - 安装并配置 InfluxDB 时间序列数据库
* [influxdb-release](https://github.com/pivotal-cf-experimental/influxdb-release) - InfluxDB 的实验性 BOSH 版本
* [puppet-telegraf](https://forge.puppet.com/datacentred/telegraf/readme) - Telegraf 的 Puppet 模块
* [rossmcdonald/influxdb](https://github.com/rossmcdonald/influxdb) - 用于安装、配置和维护 InfluxDB 的 Ansible 角色
* [tutum-docker-influxdb](https://github.com/tutumcloud/influxdb) - 用于运行开箱即用的 InfluxDB 服务器的 Docker 映像

## 查询

* [dbal-influxdb](https://github.com/corley/dbal-influxdb) - InfluxDB 的 Doctrine DBAL
* [Influxdb::Arel](https://github.com/undr/influxdb-arel) - Influxdb::Arel 是 InfluxDB 方言的 SQL AST 管理器。它简化了复杂 SQL 查询的生成
* [influxer](https://github.com/palkan/influxer) - InfluxDB ActiveRecord 风格
* [Time Series Admin](https://github.com/timeseriesadmin/timeseriesadmin) - InfluxDB 数据库的管理面板和查询界面

## InfluxDB / SaaS 托管

* [InfluxCloud](https://cloud.influxdata.com/plan-picker) - 来自 InfluxDB 的创建者
* [Aiven](https://aiven.io/influxdb) - 提供主机（AWS、Google、DigitalOcean 等）、地理位置和服务器规格的选择
* [Scalingo](https://scalingo.com/databases/influxdb) - 提供服务器规格选择
* [HostedMetrics](https://hostedmetrics.com/product/influxdb/) - 通过托管 InfluxDB、Grafana 和 StatsD 的组合来实现自定义应用程序监控


## 杂项

似乎不适合任何其他类别的项目。

* [influx-protector](https://github.com/ve-global/influx-protector) - 代理以防止危险查询进入 influxdb
* [influxdb-schema-updater](https://github.com/open-ch/influxdb-schema-updater) - 一个小型 DevOps 工具，用于使用一组配置文件管理 InfluxDB 实例的架构
* [influx-prompt](https://github.com/RPing/influx-prompt) - 具有自动完成功能的交互式命令行 InfluxDB cli
* [cleanflux](https://github.com/Transatel/cleanflux) - 围绕 /query 端点的代理，具有自动保留策略选择和在线错误修正功能

## 其他很棒的列表

### 很棒的列表，其中包含 InfluxDB 的链接

* [awesome-bigdata](https://github.com/onurakpolat/awesome-bigdata)
* [awesome-dashboard](https://github.com/obazoud/awesome-dashboard)
* [awesome-data-engineering](https://github.com/igorbarinov/awesome-data-engineering)
* [awesome-db](https://github.com/numetriclabz/awesome-db)
* [awesome-go](https://github.com/avelino/awesome-go)
* [awesome-home-assistant](https://github.com/frenck/awesome-home-assistant)
* [awesome-microservices](https://github.com/mfornos/awesome-microservices)
* [awesome-sysadmin](https://github.com/kahun/awesome-sysadmin)

### 包含 Awesome-influxdb 的很棒列表的列表

* [awesome](https://github.com/sindresorhus/awesome)
* [lists](https://github.com/jnv/lists)

## 许可证

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

在法律允许的范围内，作者和贡献者已放弃 Awesome-influxdb 的所有版权和相关或邻接权。
