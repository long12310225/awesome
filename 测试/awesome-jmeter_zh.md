# 很棒的 JMeter [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

<!--lint ignore double-link-->
精选的资源集合，涵盖 [Apache JMeter](https://jmeter.apache.org/) 以及相关内容和亮点：插件、集成、测试技术、DevOps 实践等。

<!--lint ignore double-link match-punctuation -->
[<img src=“assets/images/jmeter-logo.svg”align=“right”width=“260”alt=“Apache JMeter”>](https://jmeter.apache.org/)

<!--lint ignore double-link-->
> [Apache JMeter](https://jmeter.apache.org/) 是开源的纯 Java 应用程序，旨在加载测试功能行为和测量性能。

<!--lint ignore double-link-->
该列表源自 Stack Exchange 上的[偶尔的答案](https://sqa.stackexchange.com/a/2552/1842) 和个人 JMeter 相关链接集合，从 [awesome](https://github.com/sindresorhus/awesome) 项目中获得了进一步的灵感，并由这些[令人惊叹的贡献者](CONTRIBUTORS.md) 进行了改进。

## 内容

<!--lint ignore double-link-->
- [官方资源](#official-resources)
- [Distributions](#distributions)
- [开始使用](#getting-started)
- [Tutorials](#tutorials)
- [最佳实践](#best-practices)
- [Scripting](#scripting)
- [Automation](#automation)
  - [DSL](#dsl)
  - [Packages](#packages)
  - [Frameworks](#frameworks)
  - [Conversion](#conversion)
- [CI](#ci)
  - [工具和插件](#tools--plugins)
  - [教程和演示](#tutorials--demo)
- [分布式测试](#distributed-testing)
- [云服务/SaaS](#cloud-services--saas)
- [结果处理](#results-processing)
  - [结果分析](#results-analysis)
  - [报告和可视化](#reporting--visualization)
- [性能测试](#performance-testing)
  - [流媒体协议](#streaming-protocols)
  - [移动应用程序](#mobile-apps)
  - [大型机环境](#mainframe-environments)
  - [RPC 框架](#rpc-frameworks)
  - [RESTful API](#restful-api)
- [Tools](#tools)
  - [Plugins](#plugins)
  - [Correlation](#correlation)
  - [扩展 JMeter](#extending-jmeter)
  - [IDE集成](#ide-integration)
  - [Editors](#editors)
  - [Utilities](#utilities)
  - [AI](#ai)
- [应用性能管理集成](#apm-integration)
- [JMeter 性能](#jmeter-performance)
- [提示与技巧](#tips--tricks)
- [Books](#books)
- [培训和课程](#trainings--courses)
- [Videos](#videos)
- [Community](#community)
  - [Blogs](#blogs)
  - [Forums](#forums)
  - [Twitter](#twitter)
  - [Q&A](#qa)
- [Related](#related)
  - [很棒的清单](#awesome-lists)
  - [Other](#other)

## 官方资源

<!--lint ignore double-link-->
- [Apache JMeter Project](https://jmeter.apache.org/) - Apache JMeter 官方网站。
- [GitHub Repository](https://github.com/apache/jmeter) - Apache JMeter 源代码存储库。
- [JMeter Wiki](https://cwiki.apache.org/confluence/display/jmeter) - Apache JMeter 官方文档。
- [Issue Tracking](https://jmeter.apache.org/issues.html) - Apache JMeter 问题跟踪系统。
- [Mailing Lists](https://jmeter.apache.org/mail2.html) - Apache JMeter 邮件列表。

## 发行版

- [Download Apache JMeter](https://jmeter.apache.org/download_jmeter.cgi) - Apache JMeter：官方下载。
- [JMeter for Windows](https://sourceforge.net/projects/jmeterforwindows/) - 带插件的 JMeter 安装包。
- [JMeter Bootstrap](https://github.com/cfpb/jmeter-bootstrap) - 设置 JMeter 和 JMeter 插件的解决方案，适合用作子模块。

## 开始使用

- [Apache JMeter 入门](https://dzone.com/refcardz/getting-started-with-apache-jmeter)
- [Apache JMeter 性能测试初学者指南](https://medium.com/better-programming/the-beginners-guide-to-performance-testing-with-apache-jmeter-5cc52c327ff6)
- JMeter — 性能和负载测试：初学者指南：[第 1 部分](https://ekremkurt1907.medium.com/jmeter-performance-and-load-testing-beginners-guide-part-i-5121604bf97a)，[部分2](https://ekremkurt1907.medium.com/jmeter-performance-and-load-testing-beginners-guide-part-ii-7edb98b0d2c3)

## 教程

- [JMeter Tutorial](https://artoftesting.com/jmeter-tutorial) - 作者：测试艺术。
- 使用 JMeter 进行负载测试：[第 1 部分](https://lincolnloop.com/blog/load-testing-jmeter-part-1-getting-started/)、[第 2 部分](https://lincolnloop.com/blog/load-testing-jmeter-part-2-headless-testing-and-je/)、[部分3](https://lincolnloop.com/blog/load-testing-jmeter-part-3-replaying-apache-logs/) - 作者：Brandon Konkle。
- [JMeter Tutorial](https://www.tutorialspoint.com/jmeter/) - 通过教程点。
- [JMeter Tutorial for Load Testing: The Ultimate Guide](https://www.javacodegeeks.com/2014/11/jmeter-tutorial-load-testing.html) - 作者：丹尼尔·古铁雷斯·迪兹。
- [JMeter: Load Development Lifecycle](https://datacadamia.com/jmeter/lifecycle) - 由 DataCadamia 提供。
- [Load Testing with Apache JMeter](https://www.digitalocean.com/community/tutorial-series/load-testing-with-apache-jmeter) - 作者：Mitchell Anicas @ DigitalOcean。
- [JMeter Tutorial for Beginners](https://www.guru99.com/jmeter-tutorials.html) - 作者：Guru99。
- [JMeter Tutorials](https://qaautomation.expert/2023/12/07/jmeter-tutorials/) - 由 QA 自动化专家撰写。
- [Web App Load Testing Using Maven Plugins for Apache JMeter, and Analyzing the Results](https://dzone.com/articles/running-load-test-web-app-using-maven-plugins) - 作者：文森特·达布伦

## 最佳实践

- [JMeter官方最佳实践](https://jmeter.apache.org/usermanual/best-practices.html)
- [优化 JMeter 以进行大规模测试](https://blog.octoperf.com/optimize-jmeter-for-large-scale-tests/)
- [使用 JMeter 进行并发、高吞吐量性能测试](https://howtojboss.wordpress.com/2012/07/31/concurrent-high-throughput-performance-testing-with-jmeter/)

## 脚本编写

- [Beanshell vs JSR223 vs Java JMeter Scripting](https://www.blazemeter.com/blog/beanshell-vs-jsr223-vs-jmeter) - 最流行的脚本机制性能比较。
- [Testing with Groovy](https://static.packt-cdn.com/downloads/Testingwithgroovy.pdf) - 使用 JMeter 和 Groovy 进行负载测试。

## 自动化

### DSL

- [jmeter-java-dsl](https://abstracta.github.io/jmeter-java-dsl/) - 简单的 Java API，以 VCS 和程序员友好的方式运行 JMeter 性能测试。
- [jmeter-dotnet-dsl](https://abstracta.github.io/jmeter-dotnet-dsl/) - 简单的 .Net API 以 VCS 和程序员友好的方式运行 JMeter 性能测试。
- [jmeter-groovy-dsl](https://github.com/smicyk/groovy-jmeter) - Groovy-JMeter 项目是用于编写 JMeter 测试计划的简单 DSL。
- [jmeter-as-code](https://github.com/anasoid/jmeter-as-code) - JMeter 的简单包装器，用于使用 Java 编写和执行 JMeter 测试。
- [pymeter](https://github.com/eldaduzman/pymeter) - 适用于 Python 的简单 JMeter 性能测试 API。

### 套餐

- [loadtest](https://github.com/tmobile/loadtest) - 使用 JMeter 进行负载测试的 R 包。

### 框架

- [Taurus](https://gettaurus.org/) - 用于持续测试的自动化友好框架。
- [Performance testing framework](https://github.com/serputko/performance-testing-framework) - 用于使用 Apache JMeter 进行后端负载测试和使用 sitespeed.io +pagetest 私有实例进行前端负载测试的框架。
- [JMeter Load Testing Center](https://github.com/innogames/ltc) - 在线 Web 应用程序/仪表板，用于使用 JMeter 运行、监控和分析负载测试的结果。
- [MeterSphere](https://github.com/metersphere/metersphere) - 一站式开源企业级持续测试平台，兼容JMeter:cn:等开源标准。
- [Carrier](https://github.com/carrier-io) - 持续测试执行平台能够使用定制的 JMeter 和 Gadling 容器执行负载测试。

### 转换

- [swaggerjmx](https://github.com/Pactortester/swaggerjmx) - 将 Swagger UI 规范转换为 JMeter 测试计划的工具。
- [postman2jmx](https://github.com/Loadium/postman2jmx) - Postman 集合到 JMeter jmx 文件转换器。
- [convert-postman-jmeter](https://github.com/sercheo87/convert-postman-jmeter) - 将 Postman 项目转换为 JMeter。
- [fiddler2jmeter](https://github.com/dperfly/fiddler2jmeter) - Fiddler 或 Charles 到 JMeter 脚本转换器。
- [har-convertor-jmeter-tool](https://github.com/vdaburon/har-convertor-jmeter-plugin) - Apache JMeter 插件，用于将 HAR 文件转换为 JMeter 脚本和记录 XML 文件。
- [JMeter HAR Importer Plugin](https://github.com/Qytera-Gmbh/JMeterHARImporterPlugin) - 用于将 HTTP Archive (HAR) 文件导入 Apache JMeter 的 JMeter 插件。

## CI

### 工具和插件

- [JMeter Ant Task](https://github.com/jfifield/ant-jmeter) - Ant 任务自动运行 JMeter 测试计划。
- [JMeter Maven Plugin](https://github.com/jmeter-maven-plugin/jmeter-maven-plugin) - Maven 插件，提供在构建过程中运行 JMeter 测试的能力。
- [JMeter Gradle Plugin](https://github.com/jmeter-gradle-plugin/jmeter-gradle-plugin) - 用于执行 JMeter 测试的 Gradle 插件。
- [Jenkins Performance Plugin](https://plugins.jenkins.io/performance/) - Jenkins 插件用于从 JMeter 捕获报告并生成带有性能和稳健性趋势报告的图形图表。
- [TeamCity Performance Tests Analysis Plugin](https://github.com/jtorgan/jmeter_plugin) - TeamCity 插件，用于在 CI 中组织最简单的性能测试。
- [Bamboo JMeter Aggregator Plugin](https://marketplace.atlassian.com/apps/5902/jmeter-aggregator-for-bamboo) - 用于收集、断言和绘制 JMeter 测试结果图表的 Bamboo 插件。
- [Sonar JMeter Plugin](https://github.com/SonarQubeCommunity/sonar-jmeter) - 用于收集 JMeter 性能测试结果并显示在 Sonar 仪表板💀 中的插件。
- [Lightning](https://deliverymind.github.io/lightning/) - 将 JMeter 非功能测试与 CI/CD 服务器集成的框架。
- [Taurus JMeter Executor](https://gettaurus.org/docs/JMeter/) - Taurus 自动化框架中的 JMeter Executor。
- [PerfAction for JMeter](https://github.com/marketplace/actions/perfaction-for-jmeter) - GitHub Action 使用 Apache JMeter 及其插件运行性能测试。
- [Apache JMeter GitHub Action](https://github.com/marketplace/actions/apache-jmeter) - 用于执行 Apache JMeter 性能测试的 GitHub Action。

### 教程和演示

- 詹金斯
  - [使用 JMeter、Maven 和 Hudson 进行性能测试](https://medium.com/the-server-labs/performance-tests-with-jmeter-maven-and-hudson-d1cbdb3ffad8)
  - [CI 与 Jenkins、Git、Maven、Grunt 和 JMeter](https://github.com/dzuluagaapigee/apigee-ci-jenkins-git-maven-jmeter)
  - [使用 Jenkins 和 JMeter 进行持续自动化 Web 测试](https://www.linkedin.com/pulse/continuous-automated-web-tests-using-jenkins-jmeter-mahanta)
  - [使用 Maven 和 Jenkins 自动化 JMeter 测试](https://www.codecentric.de/en/knowledge-hub/blog/automating-jmeter-tests-maven-jenkins)
- 如何使用 Maven 和 Jenkins 自动化 JMeter 测试：[第 1 部分](https://ribblescode.wordpress.com/2012/04/16/how-to-run-jmeter-tests-with-maven/)，[部分2](https://ribblescode.wordpress.com/2012/04/16/how-to-automate-jmeter-tests-with-maven-and-jenkins-hudson-8/)
- JMeter 连续性能测试（JMeter + Ant + Jenkins）：[第 1 部分](https://www.testautomationguru.com/jmeter-continuous-performance-testing-part1/)，[第 2 部分](https://www.testautomationguru.com/jmeter-continuous-performance-testing-part2/)
  - [持续集成 101：如何使用 Jenkins 运行 JMeter](https://dzone.com/articles/continuous-integration-101-how-to-run-jmeter-with)
- 竹子
  - [如何使用 Bamboo 在持续集成环境中运行 JMeter](https://dzone.com/articles/how-to-run-jmeter-in-a-continuous-integration-envi)
- 团队城市
  - [如何使用 TeamCity 运行 JMeter 测试以实现持续集成](https://web.archive.org/web/20211204112944/https://www.blazemeter.com/blog/how-run-jmeter-tests-teamcity-continuous-integration/)
-CircleCI
  - [如何将 JMeter 集成到 CircleCI 中](https://www.blazemeter.com/blog/circleci-jmeter)
- 声纳Qube
  - [JMeter 与声纳](https://testersinaction.blogspot.com/2013/05/v-behaviorurldefaultvmlo_24.html)

## 分布式测试

- [JMeter 分布式测试分步](https://jmeter.apache.org/usermanual/jmeter_distributed_testing_step_by_step.pdf)
- [JMeter远程测试](https://jmeter.apache.org/usermanual/remote-test.html)
- [设置 JMeter 集群进行 Web 服务器负载测试](https://www.howtoforge.com/setting-up-jmeter-cluster-for-load-testing/)
- Docker化
  - [Dockerized JMeter](https://gist.github.com/hhcordero/abd1dcaf6654cfe51d0b) - 使用 Docker 和 JMeter 进行分布式负载测试工作流程。
  - [JMeter Docker 镜像](https://hub.docker.com/search/?isAutomated=0&isOfficial=0&page=1&pullCount=0&q=jmeter&starCount=0)
  - [使用 Docker 进行分布式 JMeter 测试](https://srivaths.blogspot.com/2014/08/distrubuted-jmeter-testing-using-docker.html)
  - [JMeter + InfluxDB + Grafana 性能测试的 Docker 解决方案](https://medium.com/@ellenhuang523/a-docker-solution-to-jmeter-influxdb-grafana-performance-testing-568848de7a0f)
  - [AutoMeter](https://github.com/intuit/autometer) - 一种基于 JMeter 主从架构的自动化工具，用于使用分布式从站扩展负载测试。
  - [JMeter Docker Extension](https://hub.docker.com/extensions/qainsights/jmeter-docker-extension) - 用于从 Docker 桌面运行 JMeter 测试的 Docker 扩展。
- 云测试
- 库伯内特斯
    - [jmeter-kubernetes](https://github.com/kubernauts/jmeter-kubernetes) - JMeter 集群支持 Kubernetes 和 OpenShift。
    - [jmeter-k8s-starterkit](https://github.com/Rbillon59/jmeter-k8s-starterkit) - JMeter Kubernetes 入门套件，包含实时测试报告、JMeter 监控、Kubernetes 监控和模拟即服务。
    - [kangal](https://github.com/hellofresh/kangal) - Kubernetes 和 Go 自动加载器解决方案使用多个负载生成器在 Kubernetes 集群中运行性能测试。
    - [aks_testing_fwk](https://github.com/petegrimsdale/aks_testing_fwk) - 基于 AKS 的可扩展 JMeter 测试框架，具有 Grafana 报告。
- 亚马逊网络服务
    - [jmeter-ec2](https://github.com/oliverlloyd/jmeter-ec2/) - 在 Amazon EC2 上自动运行 Apache JMeter。
    - [gee](https://github.com/kowalcj0/gee) - JMeter-EC2项目的修改版本。
    - [os-jmeter-aws](https://github.com/Aptimyze/os-jmeter-aws) - 在多个 Amazon EC2 实例上运行 JMeter，在 ELK 中查看结果。
    - [使用 JMeter 和 Amazon EC2 进行负载测试](https://medium.com/@alttaf/load-testing-with-jmeter-and-amazon-ec2-e143a7350596)
    - [使用 JMeter 和 AWS 在云中进行性能测试](https://web.archive.org/web/20190526033436/http://www.artofsoftwaredevelopment.com/performance/performance-testing-in-the-cloud-with-jmeter-aws)
    - [使用 Amazon EC2 进行 JMeter 分布式测试](https://vedovini.net/2009/08/17/jmeter-distributed-testing-with-amazon-ec2/)
    - [jmeter-ecs](https://github.com/smithmicro/jmeter-ecs) - 用于 EC2 容器服务 (ECS) 上的分布式测试的 JMeter Docker 映像。
- 数字海洋
    - [Lightweight JMeter Cloud](https://docs.google.com/presentation/d/1Yi5C27C3Q0AnT-uw9SRnMeEqXSKLQ8h9O9Jqo1gQiyI/) - 使用 DigitalOcean、JMeter 和 Docker 构建您自己的 JMeter 云。
- 微软Azure
    - [Load Testing Pipeline with JMeter, ACI and Terraform](https://github.com/Azure-Samples/jmeter-aci-terraform) - 使用 Apache JMeter 和 Terraform 的可扩展云负载/压力测试管道解决方案，可动态配置和销毁 Azure 上所需的基础设施。

## 云服务/SaaS

*支持 JMeter 测试计划执行的基于云的负载测试服务列表。*

- [Perforce BlazeMeter](https://www.blazemeter.com/) - 支持 JMeter 和 Selenium 的性能工程平台。
- [OctoPerf](https://octoperf.com/) - 支持 JMeter 和 Selenium 的 SaaS 和本地负载测试工具。
- [RedLine13](https://redline13.com/) - 基于 AWS 的负载测试服务，支持 JMeter、Gatting 和 Selenium 场景。
- [OpenText Core Performance Engineering](https://www.opentext.com/products/saas/core-performance-engineering) - 基于 OpenText 云的解决方案，用于 Web 和移动性能测试，支持 JMeter 和 Gadling（以前称为 Micro Focus LoadRunner Cloud，以前称为 HP StormRunner Load）。
- [Loadium](https://loadium.com/) - 基于 AWS 的负载测试服务，支持 JMeter 和 Selenium。
- [Azure Microsoft](https://azure.microsoft.com/en-us/products/app-testing/) - Azure 负载测试服务使用 Apache JMeter。

## 结果处理

- [JMeter Report Dashboard](https://jmeter.apache.org/usermanual/generating-dashboard.html) - JMeter 支持仪表板报告生成，以从测试计划中获取图表和统计数据。
- [Latency Lingo](https://latencylingo.com) - 发布测试结果以生成包含见解的托管交互式仪表板。

### 结果分析

<!--lint ignore double-link-->
- [JMeter Log Analysis](https://cwiki.apache.org/confluence/display/jmeter/LogAnalysis) - JMeter 日志分析的建议和秘诀。
- [分析 JMeter 结果](https://www.datazoo.de/articles/158/performance-testing-analyzing-jmeter-results)
- [JMeter 结果分析：终极指南](https://blog.octoperf.com/jmeter-result-analysis-the-ultimate-guide/)
- [JtlReporter](https://github.com/ludeknovy/jtl-reporter) - 在线报告应用程序通过上传 JTL 文件生成报告。
- [JMeter Result Analysis Plugin](https://github.com/afranken/jmeter-analysis-maven-plugin) - Maven 插件，用于解析 JMeter 测试结果并生成带有图表的详细报告。
- [JMeter Results Analyser](https://sourceforge.net/projects/jmstats/) - 用于整理、分析和报告 JMeter 测试结果的基于 Web 的应用程序。
- [JMeter Graph Tool Maven Plugin](https://github.com/vdaburon/jmeter-graph-tool-maven-plugin) - Maven 插件，用于使用 [JMeter 插件](#plugins) 中的 CMDRunner 和过滤结果工具创建图表和过滤结果；通常与 [JMeter Maven 插件](#tools--plugins) 和一组 [配套插件](https://github.com/vdaburon/jmeter-graph-tool-maven-plugin#compagnion-tools) 一起使用。
- 数据库结果收集器
  - [JMeter DBCollector Plugin](https://sourceforge.net/projects/jmeterdbcollect/) - 插件可将结果记录到数据库中以实现更有效的报告。
  - [JMeter MySQLCollector Plugin](https://cwiki.apache.org/confluence/display/jmeter/MysqlCollectorPlugin) - 用于配置侦听器以登录 MySQL 数据库的补丁。
- SLA 和 KPI
  - [JMeter SLA Report](https://github.com/sgoeschl/jmeter-sla-report) - 基于 JAMon 的 JMeter HTML 报告生成器。
  - [JMeter JUnit Reporter](https://github.com/tilln/jmeter-junit-reporter) - Apache JMeter 插件，用于根据自定义 KPI（关键绩效指标）生成 XML 格式的 JUnit 报告。
- 验证 KPI 结果的工具：
    - [JUnit KPI Reporter from JMeter CSV Report](https://github.com/vdaburon/JUnitReportKpiJMeterReportCsv) - 用于根据应用于 JMeter 报告 CSV 文件的自定义 KPI 生成 JUnit 报告的工具。
    - [JUnit KPI Reporter from JMeter Dashboard Statistics JSON File](https://github.com/vdaburon/JUnitReportKpiJMeterDashboardStats) - 用于根据应用于 JMeter 仪表板统计 JSON 文件的自定义 KPI 生成 JUnit 报告的工具。
    - [JUnit Report Compare 2 JMeter Report CSV Files](https://github.com/vdaburon/JUnitReportKpiCompareJMeterReportCsv) - 使用 JMeter 报告 CSV 文件比较 2 个负载测试并根据自定义 KPI 创建 JUnit 报告的工具。

### 报告和可视化

<!--lint ignore double-link-->
- InfluxDB 和 Grafana
  - [Using JMeter with InfluxDB & Grafana](https://blog.vinsguru.com/category/influxdb/) - 使用 InfluxDB 和 Grafana 收集和可视化实时测试结果和服务器监控统计数据的指南集合。
  - [如何使用 Grafana 监控 JMeter 非 GUI 结果](https://dzone.com/articles/how-to-use-grafana-to-monitor-jmeter-non-gui-resul)
  - [jmeterReports](https://github.com/kirillyu/jmeterReports) - 使用 Grafana 自定义仪表板自动生成的 JMeter 测试运行结果报告到 Confluence 中：ru:。
  - [InfluxDB Community Template for JMeter](https://github.com/influxdata/community-templates/tree/master/apache_jmeter) - 预打包的 InfluxDB 配置包含从仪表板和 Telegraf 配置到单个清单文件中的通知和警报的所有内容。
- Grafana 仪表板
    - [JMeter Load Test Dashboard](https://grafana.com/grafana/dashboards/1152-jmeter-load-test/) - Grafana 仪表板显示 JMeter（由 NovaTec-APM）提供的实时负载测试指标。
    - [JMeter Dashboard using Core InfluxdbBackendListenerClient](https://grafana.com/grafana/dashboards/5496-apache-jmeter-dashboard-by-ubikloadpack/) - 使用 InfluxDB 和 Grafana（由 Philippe M）实时监控 Apache JMeter 负载测试。
    - [JMeter Dashboard (3.2 and up)](https://grafana.com/grafana/dashboards/3351-jmeter-3-3/) - 使用 InfluxDB 和 Grafana（由 adrianbanu）实时监控 JMeter 负载测试。
    - [JMeter (via prometheus exporter)](https://grafana.com/grafana/dashboards/2492-jmeter/) - Grafana 仪表板，用于通过 Prometheus 导出器检查 JMeter 指标（由 chiabre 提供）。
  - [JMeter-InfluxBD-Writer Plugin](https://github.com/NovatecConsulting/JMeter-InfluxDB-Writer) - JMeter 插件可将负载测试数据即时写入 InfluxDB。
  - [JMeter Results to InfluxDB](https://github.com/soprasteria/jmeter2influxdb) - 从 csv 文件读取 JMeter 结果并放入 InfluxDB 数据库中。
- ELK堆栈
  - [Using ELK](https://ecmarchitect.com/archives/2014/09/09/3932) - 使用 Elasticsearch、Logstash 和 Kibana 可视化 JMeter 测试结果。
  - [JMeter + Elasticsearch Live Monitoring](https://medium.com/@anthony.gauthier325/jmeter-elasticsearch-live-monitoring-c895c843c51e) - 使用Elasticsearch后端监听器和Grafana/Kibana实时监控结果。
  - [jmeter-logstash](https://github.com/anasoid/jmeter-logstash) - 实时或测试结束后使用 Docker 和 Logstash 解析 JTL 结果，并将数据发送到 Elasticsearch 或 InfluxDB，以获得漂亮的仪表板并比较不同的测试。
- 普罗米修斯
  - [jmeter-prometheus-plugin](https://github.com/johrstrom/jmeter-prometheus-plugin) - Apache JMeter 的 Prometheus 监听器，在 HTTP API 中公开结果。
  - [jmeter-prometheus-listener](https://github.com/kolesnikovm/jmeter-prometheus-listener) - 用于 Prometheus 指标导出的 Apache JMeter 后端侦听器实现。
  - [ulp-observability-plugin](https://github.com/ubikingenierie/ulp-observability-plugin) - 允许您从您喜欢的浏览器监控 JMeter CLI 性能测试，而无需在 GUI 模式下启动 JMeter。
- ClickHouse
  - [JMeter Results from ClickHouse](https://grafana.com/grafana/dashboards/9561-jmeter-results-from-clickhouse-eng/) - 使用 [JMeter Listener pack](https://gitlab.com/testload/jmeter-listener/-/wikis/3.3-ClickHouse-usage)、ClickHouse 和 Grafana 收集和监控测试结果。
  - [jmeter-clickhouse-listener](https://gitlab.com/testload-group/jmeter-clickhouse-listener) - JMeter 插件允许将负载测试数据即时写入 ClickHouse。
- 后端监听器实现
  - [jmeter-elasticsearch-backend-listener](https://github.com/anthonygauthier/jmeter-elasticsearch-backend-listener) - JMeter 插件用于将测试结果发送到 Elasticsearch 引擎。
  - [jmeter-backend-azure](https://github.com/adrianmo/jmeter-backend-azure) - 用于将测试结果发送到 Azure Application Insights 的 JMeter 插件。
  - [jmeter-backend-listener-kafka](https://github.com/veeranalyticsltd/jmeter-backend-listener-kafka) - JMeter 插件用于将测试结果发送到 Kafka 服务器。
  - [jmeter-listener](https://gitlab.com/testload/jmeter-listener) - JMeter 插件可将负载测试数据即时写入 ClickHouse、InfluxDB、Elasticsearch。
  - [jmeter-influxdb2-listener-plugin](https://github.com/mderevyankoaqa/jmeter-influxdb2-listener-plugin) - 适用于 Apache JMeter 的 InfluxDB v2.0 监听器插件。
  - [jmeter-datadog-backend-listener](https://github.com/DataDog/jmeter-datadog-backend-listener) - 将 JMeter 测试结果发送到 Datadog。
  - [jmeter-dynatrace-plugin](https://github.com/dynatrace-oss/jmeter-dynatrace-plugin) - JMeter 后端侦听器实现，用于通过 Dynatrace MINT 指标摄取将记录的负载测试指标发送到配置的 Dynatrace 监控环境。
  - [jmeter-backend-newrelic](https://github.com/darrensmithwtc/jmeter-backend-newrelic) - 一个 JMeter 插件，用于将测试结果发送到 New Relic Metrics API。
- AWS 云观察
  - [jmeter-cw-logs](https://github.com/concurrencylabs/jmeter-cw-logs) - 用于将 JMeter 测试结果发布到 AWS CloudWatch Logs 的 CloudFormation 模板。
- 自定义和弃用
  - [Using Matplotlib & Python](https://www.metaltoad.com/blog/plotting-your-load-test-jmeter) - 使用 Matplotlib 绘图工具和 Python 绘制 JMeter 负载测试结果。
  - [Statistical Aggregate Report](https://rubenlaguna.com/post/2007-01-02-better-jmeter-graphs/) - 自定义统计聚合报告侦听器，用于增强结果可视化。
  - [JChav](https://github.com/d6y/jchav) - JMeter 图表历史和可视化库。
- JMeter Dashboard：[howto](https://seangkuan.blogspot.com/2015/06/jmeter-dashboard-realtime-monitoring-of.html)，[来源](https://github.com/vincentskooi/JMeterDashboard) - JMeter负载测试的实时监控。
  - [Using CMDRunner & Powershell](https://performancewebautoamtionother.blogspot.com/2015/12/jmeter-create-graphs-with-cmdrunner.html) - 使用 CMDRunner 和 powershell 并行执行创建 JMeter 图表。

## 性能测试

### 流媒体协议

- [使用 Apache JMeter 对 HTTP 直播流 (HLS) 进行简单、真实的负载测试](https://ubik-ingenierie.com/blog/easy-and-realistic-load-testing-of-http-live-streaming-hls-with-apache-jmeter/)
- [使用JMeter负载测试Wowza Streaming Engine的Live HLS并发](https://web.archive.org/web/20210918113142/https://www.realeyes.com/blog/wowza-streaming/)
- [如何使用 JMeter 测试视频流](https://www.blazemeter.com/blog/video-streaming-testing)
- [HLS JMeter 插件](https://github.com/Blazemeter/HLSPlugin)

### 移动应用程序

- [记录iOS应用程序HTTP请求](https://www.testautomationguru.com/jmeter-record-ios-application-http-requests/)
- [移动应用程序的负载测试变得简单](https://www.blazemeter.com/blog/mobile-app-load-testing)

### 大型机环境

- [JMeter RTE Plugin](https://github.com/Blazemeter/RTEPlugin) - JMeter RTE（远程终端仿真器协议）插件用于测试大型机应用程序。

### RPC 框架

- [JMeter gRPC Plugin](https://github.com/zalopay-oss/jmeter-grpc-plugin) - JMeter插件支持负载测试gRPC。
- [JMeter gRPC Request](https://github.com/zalopay-oss/jmeter-grpc-request) - JMeter 采样器将 gRPC 请求发送到服务器。
- [JMeter Dubbo Plugin](https://github.com/thubbo/jmeter-plugins-for-apache-dubbo) - Apache Dubbo 的 JMeter 插件。

### RESTful API

- [使用 JMeter 进行 REST API 测试。分步指南](https://blog.octoperf.com/rest-api-testing-with-jmeter-step-by-step-guide/)

## 工具

### 插件

- [JMeter Plugins](https://jmeter-plugins.org/) - Apache JMeter 的独立插件集，插件管理器引用了许多插件并简化了安装。
- [Ubik Load Pack](https://ubikloadpack.com/) - Apache JMeter 的生产力扩展。
- GitHub 主题：[jmeter-plugin](https://github.com/topics/jmeter-plugin)、[jmeter-plugins](https://github.com/topics/jmeter-plugins) - 探索标有“jmeter-plugin”或“jmeter-plugins”标签的 JMeter 插件。

### 相关性

<!--lint ignore double-link-->
- [Correlation Recorder Plugin](https://github.com/Blazemeter/CorrelationRecorder) - JMeter 插件通过在记录时提供变量的自动关联来简化具有动态变量的应用程序的记录过程。
- [Siebel CRM Plugin](https://github.com/Blazemeter/SiebelPlugin) - JMeter 插件通过在记录时提供变量的自动关联来简化 Siebel CRM 应用程序的脚本编写❄️。
- [ULP Auto-correlator Plugin](https://ubik-ingenierie.com/blog/ubikloadpack-autocorrelator-plugin-help/) - 来自 [Ubik Load Pack](#plugins) 的 Oracle 和基于 Vaadin 的应用程序的商业插件。

### 扩展 JMeter

- [JMeter开发手册](https://cwiki.apache.org/confluence/display/jmeter/DeveloperManual)
- [如何为 JMeter 编写插件](https://jmeter.apache.org/usermanual/jmeter_tutorial.html)
- [如何利用 Groovy 构建 JMeter 插件](https://web.archive.org/web/20180225144718/http://artur.ejsmont.org/blog/content/how-to-build-a-jmeter-plugin-utilising-groovy)
- [如何在 JMeter 中创建插件](https://stackoverflow.com/questions/20422640/how-to-create-a-plugin-in-jmeter)
- [自定义 JMeter 采样器和配置元素](https://codyaray.com/2014/07/custom-jmeter-samplers-and-config-elements)
- [实施自定义 JMeter 采样器](https://dzone.com/articles/implement-custom-jmeter-samplers)
- [Hello JMeter plugin](https://github.com/Bugazelle/hello-jmeter-plugin) - 创建您的第一个 JMeter 插件的简短、清晰和快速的指南。

### IDE集成

- [IntelliJ IDEA IDE Plugin](https://plugins.jetbrains.com/plugin/7013-jmeter-plugin) - 从 IntelliJ IDEA 创建运行配置并运行 JMeter 测试。
- [JMeter Viewer](https://github.com/anboralabs/intellij-jmeter) - 在 IntelliJ IDE 中打开 JMeter 测试计划。
- [JMeter + Eclipse HOWTO](https://cwiki.apache.org/confluence/display/jmeter/JMeterAndEclipseHowTo) - 使用 Eclipse IDE 开发 JMeter 项目。
- [在 NetBeans IDE 中使用负载生成器](https://netbeans.apache.org/tutorial/main/kb/docs/java/profile-loadgenerator/)

### 编辑

*除了标准 JMeter GUI 和 XML 编辑器之外，JMX 文件的替代编辑器。*

<!--lint ignore double-link-->
- [BlocklyJMX Editor](https://jmeter-plugins.org/editor/) - 基于 Web 的 JMeter 测试计划文件查看器和编辑器（[JMeter 插件](#plugins) 项目的一部分）。
- [JEval](https://github.com/QAInsights/JEval) - 一个基于 Python 的实用程序，可评估 JMeter 测试计划并通过分析每个元素提供建议和最佳实践。
- [JMX Enhancer](https://www.jmxenhancer.com/) - 加快准备 JMeter 测试计划的解决方案。
- [jmx.js](https://www.vinodkd.org/jmx.js/) - 基于 Web 的 JMeter JMX 文件编辑器 💀。

### 公用事业

- [Hamster](https://github.com/QAInsights/hamster) - 从 Mac 菜单栏快速启动您的 JMeter 测试计划。

### 人工智能

- [Feather Wand](https://jmeter.ai) - JMeter 中的 AI 代理，集成了 Claude Code、Codex、OpenCode 和 Gemini。

## 应用性能管理集成

*与应用程序性能监控 (APM) 工具集成，以分析应用程序服务器、数据库服务器和 Web 服务的性能。*

<!--lint ignore double-link-->
- [Servers Performance Monitoring Plugin](https://jmeter-plugins.org/wiki/PerfMon/) - 来自 [JMeter Plugins](#plugins) 项目的服务器监控插件。
- [DX App Synthetic Monitor](https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/app-synthetic-monitor/SaaS/using/use-jmeter-scripts-to-test-web-servers.html) - 支持 JMeter 的事务监控和测试解决方案。
- 使用 New Relic 和 JMeter 进行性能修复：[第 1 部分](https://web.archive.org/web/20250811141928/https://moduscreate.com/blog/performance-remediation-using-new-relic-jmeter-part-1-3/)，[部分2](https://web.archive.org/web/20250809025316/https://moduscreate.com/blog/performance-remediation-using-new-relic-jmeter-part-2-3/)，[部分3](https://web.archive.org/web/20250719013947/https://moduscreate.com/blog/performance-remediation-using-new-relic-jmeter-part-3-of-3/)
- [Elastic APM integration](https://github.com/vdaburon/jmeter-elastic-apm) - 管理 Apache JMeter 脚本中弹性应用程序性能监控 API 的集成。

## JMeter 性能

- [JMeter Performance](https://cwiki.apache.org/confluence/display/jmeter/JMeterPerformance) - JMeter 跨版本性能的演变。
- [JMeter Performance and Tuning Tips](https://ubik-ingenierie.com/blog/jmeter_performance_tuning_tips/) - 由 Ubik Ingenierie 设计。
- 如何加速 JMeter：[第 1 部分](https://pflb.us/blog/how-to-speed-up-jmeter-part-1/)，[第 2 部分](https://pflb.us/blog/how-to-speed-up-jmeter-part-2/)

## 提示与技巧

- [JMeter tips](https://web.archive.org/web/20221126233834/https://www.webwob.com/html/jmeter_tips.html) - JMeter 提示和技巧的便签本。

## 书籍

<!--lint ignore double-link-->
- [Apache JMeter: A Practical Beginner's Guide to Automated Testing and Performance Measurement for Your Websites](https://books.google.com/books?id=nX8oKIEvUcYC) - 作者：Emily H. Halili（Packt 出版社）。
- [Performance Testing with JMeter 2.9](https://books.google.com/books?id=fpWmv3wPT64C) - 作者：Bayo Erinle（[Packt Publishing](https://www.packtpub.com/product/performance-testing-with-jmeter-29/9781782165842)）；使用 Apache JMeter 测试 Web 应用程序的指南以及实用的实践示例。
- [Performance Testing with JMeter, 2nd Edition](https://books.google.com/books?id=6ditCAAAQBAJ) - 作者：Bayo Erinle（[Packt Publishing](https://www.packtpub.com/product/performance-testing-with-jmeter/9781784394813)）。
- [Performance Testing with JMeter 3, 3rd Edition](https://books.google.com/books?id=BedDDwAAQBAJ) - 作者：Bayo Erinle（[Packt Publishing](https://www.packtpub.com/product/performance-testing-with-jmeter-3-third-edition/9781787285774)）。
- [JMeter Cookbook](https://books.google.com/books?id=gJUeBQAAQBAJ) - 作者：Bayo Erinle（[Packt Publishing](https://www.packtpub.com/product/jmeter-cookbook/9781783988280)）； 70 个富有洞察力且实用的秘诀可帮助成功使用 Apache JMeter。
- [JMeter by Example](https://books.google.com/books?id=iWeJDAEACAAJ) - 作者：Sai Matam 和 Jagdeep Jain ([Leanpub](https://leanpub.com/jmeterbyexample))；一个简单、实用、分步的教程，用于衡量网站的性能。
- [Pro Apache JMeter: Web Application Performance Testing](https://books.google.com/books?id=YJ4xDwAAQBAJ) - 作者：Sai Matam 和 Jagdeep Jain（[Apress](https://link.springer.com/book/10.1007/978-1-4842-2961-3)）。
- [Master Apache JMeter: From load testing to DevOps](https://books.google.com/books?id=D_amDwAAQBAJ) - 作者：Antonio Gomes Rodrigues、Bruno Demion (Milamber) 和 Philippe Mouawad（[Leanpub](https://leanpub.com/master-jmeter-from-load-test-to-devops)、[Packt Publishing](https://www.packtpub.com/product/master-apache-jmeter-from-load-testing-to-devops/9781839217647))。
- [Advanced JMeter Testing](https://leanpub.com/advanced_jmeter_testing) - 作者：Penny Curich（[Leanpub](https://leanpub.com/advanced_jmeter_testing)），为 Apache JMeter 5.0 编写自定义组件的指南。

## 培训和课程

- [JMeter: Performance and Load Testing (Feb 2019)](https://www.linkedin.com/learning/jmeter-performance-and-load-testing) - 通过领英学习。
- [Advanced JMeter (Jul 2020)](https://www.linkedin.com/learning/advanced-jmeter) - 通过领英学习。
- [JMeter Training Courses](https://www.nobleprog.co.uk/cc/apachejmetertesting) - 作者：NobleProg。
- [BlazeMeter University](https://www.blazemeter.com/university) - 由 BlazeMeter 提供。
- [JMeter Courses collection](https://www.udemy.com/topic/jmeter/) - 由乌德米.
- [Web Applications (and Mobile Apps) Performance Testing with JMeter](http://pragmatictestlabs.com/web-applications-mobile-apps-performance-testing-jmeter/) - 由实用测试实验室提供。
- [Training courses on Load Testing with Apache JMeter](https://ubik-ingenierie.com/blog/jmeter-trainings-by-contributors-and-committers/) - 由 Ubik Ingenierie 设计。
- [Apache JMeter Training](https://qainsights.com/apache-jmeter-training/) - 由 QAInsights 提供。
- [JMeter Getting Started Course (Apr 2019)](https://www.pluralsight.com/courses/jmeter-getting-started) - 由 Pluralsight 提供。

## 视频

- [JMeter Tutorials](https://www.youtube.com/c/AutomationStepByStep/search?query=jmeter) - 通过逐步自动化。
- [Learn Apache JMeter Series](https://www.youtube.com/playlist?list=PLJ9A48W0kpRIjLkZ32Do9yDZXnnm7_uj_) - 由 QAInsights 提供。
- [JMeter / Devops/ CI-CD / Cloud](https://www.youtube.com/c/xavki-linux/search?query=jmeter) - 作者：xavki :fr:。

## 社区

### 博客

- [BlazeMeter Blog](https://www.blazemeter.com/blog) - BlazeMeter 关于 JMeter 和性能测试的博客。
- [Ubik Load Pack Blog](https://ubik-ingenierie.com/blog/category/jmeter/) - Ubik 工程博客。
- [TestAutomationGuru Blog](https://www.testautomationguru.com/category/jmeter/) - 有关测试自动化的技术博客。
- [RedLine13 Blog](https://www.redline13.com/blog/tag/jmeter/) - RedLine13 博客中的 JMeter 文章。
- [JMeter Blog](https://shantonusarker.blogspot.com/p/jmeter.html) - 另一个使用 JMeter 进行性能和自动化测试的博客。
- [OctoPerf Blog](https://blog.octoperf.com/categories/jmeter/) - OctoPerf 关于 JMeter 和负载测试的博客。
- [Abstracta JMeter Archives](https://abstracta.us/blog/tag/jmeter/) - 关于 JMeter 的摘要博客。
- [JMeter Basics](https://thatsabug.com/tags/#jmeter-series) - 若昂·法里亚斯着。

### 论坛

<!--lint ignore double-link-->
- [JMeterPlugins Google 群组](https://groups.google.com/g/jmeter-plugins)

### 推特

<!--lint ignore double-link-->
- [@ApacheJMeter](https://x.com/apachejmeter) - Apache JMeter 负载测试工具的官方 Twitter 帐户。
- [@jmeter_plugins](https://x.com/jmeter_plugins) - JMeter 负载测试工具的自定义插件项目的 Twitter 帐户。
- [@BlazeMeter](https://x.com/BlazeMeter) - Blazemeter 的官方 Twitter 帐户，它是基于 JMeter 的 DevOps 性能工程平台。
- [@masterjmeter](https://x.com/masterjmeter) - 《掌握 Apache JMeter 从负载测试到 DevOps》(#books)一书的官方账号。
- [@ubikloadpack](https://x.com/ubikloadpack) - [Ubik Load Pack](#plugins) 的 Twitter 帐户，用于视频流和复杂协议负载测试的自定义 JMeter 插件。

### 问答

- [Stack Overflow 上的“jmeter”](https://stackoverflow.com/questions/tagged/jmeter)
- [Gitter 上的“jmeter”](https://app.gitter.im/#/room/#aliesbelik_jmeter-chat:gitter.im)
- [Slack 上的“#jmeter”](https://jmeterusers.slack.com/)
- [Reddit 上的“r/jmeter”](https://www.reddit.com/r/jmeter/)

## 相关

### 很棒的清单

- [Awesome Software Quality](https://github.com/ligurio/sqa-wiki) - 免费软件测试和验证资源列表。
- [Awesome Testing](https://github.com/TheJambo/awesome-testing) - 测试资源的精选列表。
- [Awesome Tsung](https://github.com/aliesbelik/awesome-tsung) - 开源多协议分布式负载测试工具，用 Erlang 开发。
- [Awesome Gatling](https://github.com/aliesbelik/awesome-gatling) - 基于Scala、Akka和Netty的开源负载和性能测试框架。
- [Awesome k6](https://github.com/grafana/awesome-k6) - 以开发人员为中心的开源性能监控和负载测试解决方案。
- [Awesome Locust](https://github.com/aliesbelik/awesome-locust) - 用 Python 编写的开源可扩展负载测试框架。

### 其他

- [How They Load Test](https://github.com/aliesbelik/how-they-load) - 关于世界各地的公司如何执行负载测试的公开可用资源的精选集合。
- [Load Testing Toolkit](https://github.com/aliesbelik/load-testing-toolkit) - 用于调试、基准测试、负载和压力测试代码或服务的开源工具集合。

## 贡献

请首先查看 [CONTRIBUTING](CONTRIBUTING.md) 指南。
