# 很棒的加特林 [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
<!--lint ignore double-link match-punctuation -->
[<img src =“assets/images/gadling-logo.svg”align =“right”width =“260”alt =“加特林”>]（https://gadling.io/）
<!--lint ignore double-link-->
精心策划的资源集合，涵盖使用 [Galing](https://gadling.io/) 进行负载测试的各个方面以及相关内容：插件、集成、测试技术、DevOps 实践等。
<!--lint ignore double-link-->
> [Gadling](https://gadling.io/) 是一个基于 Scala、Akka 和 Netty 的开源负载和性能测试框架。

## 内容

- [官方资源](#official-resources)
- [开始使用](#getting-started)
- [Tutorials](#tutorials)
- [分布式测试](#distributed-testing)
- [Tools](#tools)
  - [Plugins](#plugins)
  - [Frameworks](#frameworks)
  - [Reporting](#reporting)
  - [Sandbox](#sandbox)
  - [Miscellaneous](#miscellaneous)
- [CI](#ci)
- [测试管理](#test-management)
- [培训和课程](#trainings--courses)
- [Videos](#videos)
  - [Talks](#talks)
  - [视频教程](#video-tutorials)
- [Community](#community)
- [Related](#related)
  - [很棒的清单](#awesome-lists)
  - [Other](#other)

## 官方资源
<!--lint ignore double-link-->
- [Homepage](https://gatling.io/)
- [Documentation](https://docs.gatling.io/)
- [源代码](https://github.com/gatling/gatling)

## 开始使用

- [初步了解 Gattle，一个基于 DSL 的负载测试工具](https://callistaenterprise.se/blogg/teknik/2014/04/16/a-first-look-at-gatling-a-dsl-based-load-test-tool/)
- [加特林：将您的性能测试提升到一个新的水平](https://www.thoughtworks.com/insights/blog/gatling-take-your-performance-tests-next-level)
- [使用加特林进行负载测试。完整指南](https://www.james-willett.com/gatling-load-testing-complete-guide/)

## 教程

- [使用 Galing 对 gRPC 服务进行负载测试](https://medium.com/@georgeleung_7777/load-testing-grpc-services-with-gatling-990025c77055)
- [为 AWS Lambda 创建自定义 Ga特林协议](https://callistaenterprise.se/blogg/teknik/2016/11/26/gatling-custom-protocol/)
- [使用 Ga特林定制 DSL 进行负载测试 ZeroMQ](https://mintbeans.com/load-testing-zeromq-with-gatling/)

## 分布式测试

- [使用 Gattle 和 Kubernetes 进行分布式负载测试](https://debijenkorf.tech/https-medium-com-annashepeleva-distributed-load-testing-with-gatling-and-kubernetes-93ebce26edbe)
- [Ga特林 – 扩展您的负载测试](https://web.archive.org/web/20210625094528/http://www.nimrodstech.com/gatling-cluster-load-testing/)
- [Distributed Gatling](https://github.com/Abiy/distGatling) - 在分布式/集群环境中运行加特林模拟测试的解决方案。
- [gatling-operator](https://github.com/st-tech/gatling-operator) - 使用 Kubernetes 操作符自动化分布式加特林负载测试。

## 工具

### 插件

- [gatling-sbt-plugin](https://github.com/gatling/gatling-sbt-plugin) - Gattle SBT 插件将 Gattle 与 SBT 集成，允许使用 Gadling 作为测试框架。
- [gatling-build-plugin](https://github.com/gatling/gatling-build-plugin) - 一个 SBT 插件，用于在 Gadling 项目的构建中共享通用设置。
- [gatling-maven-plugin](https://github.com/gatling/gatling-maven-plugin) - 加特林 Maven 扩展。
- [gatling-gradle-plugin](https://github.com/gatling/gatling-gradle-plugin) - Gradle 的加特林插件。
- [gatling-remote-sbt](https://github.com/Pravoru/gatling-remote-sbt) - 用于加特林负载测试的远程执行插件。
- [gatling-junitrunner](https://github.com/Pravoru/gatling-junitrunner) - 加特林模拟的 JUnit 包装器。
- [gatling-grpc](https://github.com/phiSgr/gatling-grpc) - gRPC 的 Gatting 负载测试插件。
- [gatling-aws](https://github.com/callistaenterprise/gatling-aws) - AWS Lambda 的 Ga特林自定义协议。
- [gatling-xmpp-protocol](https://github.com/TLmaK0/gatling-xmpp-protocol) - XMPP 协议，用于使用加特林对 XMPP 服务器进行压力测试。
- [gatling-jwt](https://bitbucket.org/atlassianlabs/gatling-jwt/) - Gatrin 2.0 的扩展，可帮助发出 JWT 签名的请求。
- [gatling-mqtt](https://github.com/mnogu/gatling-mqtt) - 用于压力测试 MQTT 的 Gattle 插件。
- [gatling-kafka](https://github.com/mnogu/gatling-kafka) - 用于压力测试 Apache Kafka 协议的 Gattle 插件。
- [gatling-kafka](https://github.com/Amerousful/gatling-kafka) - 卡夫卡的加特林插件。
- [gatling-kafka-plugin](https://github.com/galax-io/gatling-kafka-plugin) - 用于在 Ga特林中支持 Kafka 的插件。
- [gatling-amqp-plugin](https://github.com/galax-io/gatling-amqp-plugin) - 用于支持 Gattle (3.2.x) 中的 AMQP 性能测试的插件。
- [gatling-jdbc-plugin](https://github.com/galax-io/gatling-jdbc-plugin) - 用于 JDBC 支持的简单 Ga特林插件。
- [gatling-picatinny](https://github.com/galax-io/gatling-picatinny) - 具有一系列扩展 Gatting DSL 的有用函数的库。
- [gatling-sql](https://github.com/tmcgrath/gatling-sql) - 用于 JDBC 或 Spark Thrift 服务器压力测试的 Gattle 扩展。
- [gatling-tcp-extensions](https://github.com/scalecube/gatling-tcp-extensions) - 加特林的 TCP 扩展。
- [gatling-thrift](https://github.com/3tty0n/gatling-thrift) - Apache Thrift 的 Gattle 第三方插件。
- [gatling-bolt](https://github.com/sarmbruster/gatling-bolt) - 支持 Ga特林 Neo4j Bolt 协议。
- [gatling-zeromq](https://github.com/softwaremill/gatling-zeromq) - ZeroMQ 协议的加特林压力测试插件。
- [gatling-dubbo](https://github.com/youzan/gatling-dubbo) - 用于在 Apache Dubbo 上运行负载测试的 Gattle 插件。
- [gatling-wait](https://github.com/Amerousful/gatling-wait) - 简化等待特定事件的插件，允许自定义条件、尝试管理和错误处理。

### 框架

- [Kraken](https://github.com/OctoPerf/kraken) - 基于 OctoPerf 的 Gadling 的负载测试 IDE。
- [Karate Gatling](https://docs.karatelabs.io/extensions/performance-testing/) - 重新使用空手道 API 测试作为 Gattle 执行的性能测试。
- [Taurus](https://gettaurus.org/docs/Gatling/) - Taurus 框架中的加特林执行器。
- [Carrier](https://github.com/carrier-io) - 持续测试执行平台能够使用定制的 JMeter 和 Gadling 容器执行负载测试。
- [Gatlytron](https://github.com/Performetriks/Gatlytron) - 加特林基础框架，方便入门。

### 报告

- [gatling-report](https://github.com/nuxeo/gatling-report) - 解析 Gattle 模拟.log 文件以输出 CSV 统计数据或使用 Plotly 图表构建 HTML 报告。
- [gatling2allure](https://github.com/biski/gatling2allure) - 将 Gatting 日志转换为 Allure 报告。
- [gatling-elasticsearch](https://github.com/Amerousful/gatling-elasticsearch-logs) - Logger 解析原始 Gatting 日志并将其发送到 Elasticsearch。

### 沙盒

- [gatling-scaffold](https://github.com/robsonbittencourt/gatling-scaffold) - 使用 Gattle、InfluxDB 和 Grafana 的负载测试项目的基础。
- [perfiz](https://github.com/znsio/perfiz) - 基于 Gattle 的 Docker 化 API 性能测试设置，具有 Grafana 仪表板和 Prometheus 监控。

### 杂项

- [dakiya](https://github.com/rupeshmore/dakiya) - 将 Postman 集合转换为 Ga特林脚本。
- [gatling-template.g8](https://github.com/galax-io/gatling-template.g8) - 用于 Gattle 性能测试项目的 Giter8 模板。

## CI

- [Gatling Jenkins Plugin](https://github.com/jenkinsci/gatling-plugin) - [Jenkins 插件](https://plugins.jenkins.io/gadling/) 用于 Ga特林。
- [run-gatling](https://github.com/liatrio/run-gatling) - GitHub Action 可轻松将 Gattle 性能测试集成到 GitHub 工作流程。

## 测试管理

- [Performance and load testing with Gatling](https://docs.getxray.app/space/XRAYCLOUD/44565472/Performance+and+load+testing+with+Gatling) - 与 Jira 和 Gattle 上的 Xray 测试管理集成。

## 培训和课程

- [Gatling Courses](https://www.udemy.com/topic/gatling/) - 由乌德米.
- [Performance Test Automation 101: Gatling, Lighthouse, & Jenkins](https://www.educative.io/courses/performance-test-automation-101-gatling-lighthouse-jenkins) - 通过教育。

## 视频

### 会谈

- [Load Testing Done Right with Gatling](https://www.youtube.com/watch?v=VUPTaPms210) - Stéphane Landelle @ Voxxed Days 贝尔格莱德 2015。
- [Load Testing Crash Course with Gatling](https://www.youtube.com/watch?v=RiM1GsVSbzM) - Stéphane Landelle @ Devoxx 比利时 2022。
- [Load Testing Made Easy with Gatling](https://www.youtube.com/watch?v=8Eplj8BvugA) - Rafał Piotrowski @ Scala Days 2023 马德里。

### 视频教程

- [Performance Testing with Gatling](https://www.youtube.com/playlist?list=PLd4gvNaNZ4T3NCWsv3zwHYlLGtr9s1-Fz) - Tomi Tiihonen 的教程系列。
- [Gatling Tutorials for Beginners](https://www.youtube.com/playlist?list=PLw_jGKXm9lIYpTotIJ-R31pXS7qqwXstt) - 詹姆斯·威利特 (James Willett) 的教程系列。

## 社区

- [加特林社区](https://community.gatling.io/)
- [Stack Overflow 上的“加特林”](https://stackoverflow.com/questions/tagged/gatling+or+scala-gatling+or+gatling-java+or+gatling-plugin)
- [Twitter 上的“@GattleTool”](https://x.com/gatlingtool)

## 相关

### 很棒的清单

- [Awesome Software Quality](https://github.com/ligurio/sqa-wiki) - 免费软件测试和验证资源列表。
- [Awesome Testing](https://github.com/TheJambo/awesome-testing) - 测试资源的精选列表。
- [Awesome JMeter](https://github.com/aliesbelik/awesome-jmeter) - 用 Java 编写的开源负载测试和性能测量工具。
- [Awesome Tsung](https://github.com/aliesbelik/awesome-tsung) - 开源多协议分布式负载测试工具，用 Erlang 开发。
- [Awesome k6](https://github.com/grafana/awesome-k6) - 以开发人员为中心的开源性能监控和负载测试解决方案。
- [Awesome Locust](https://github.com/aliesbelik/awesome-locust) - 用 Python 编写的开源可扩展负载测试框架。

### 其他

- [How They Load Test](https://github.com/aliesbelik/how-they-load) - 关于世界各地的公司如何执行负载测试的公开可用资源的精选集合。
- [Load Testing Toolkit](https://github.com/aliesbelik/load-testing-toolkit) - 用于调试、基准测试、负载和压力测试代码或服务的开源工具集合。

## 贡献

欢迎贡献！<br>
请首先查看 [CONTRIBUTING](CONTRIBUTING.md) 指南。
