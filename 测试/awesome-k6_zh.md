<div align="center">
  <a href="https://k6.io/">
    <img src="assets/bert.png" alt="k6 mascot" width="300px">
  </a>

<!--lint disable awesome-heading-->
# 很棒的k6 [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
<!--lint enable awesome-heading-->

社区在（测试）<a href="https://k6.io/">k6</a> 上提供的资源集合。

<!-- lint disable double-link -->
欢迎贡献！首先阅读[贡献指南](contributing.md)。
<!-- lint enable double-link -->

</div>

## 内容

- [Articles](#articles)
- [Videos](#videos)
- [Examples/Templates](#examplestemplates)
- [Tools](#tools)
- [CI/CD](#cicd)
- [Extensions](#extensions)
- [Related](#related)


## 文章

- [k6 Learn](https://github.com/grafana/k6-learn) - 解释负载测试的原理以及如何使用 k6 进行负载测试的实际示例。
- [k6 OSS workshop](https://github.com/grafana/k6-oss-workshop) - 一个 2-3 小时的 k6 研讨会，其中包含使用 QuickPizza 演示应用程序的实用 k6 示例。
- [Beginner's guide to load testing with k6](https://link.medium.com/npI9sjDyyjb) - 分多个部分的入门指南，帮助您开始使用 k6。
- [Best practices organizing performance testing projects with k6](https://grafana.com/blog/2024/04/30/organizing-your-grafana-k6-performance-testing-suite-best-practices-to-get-started/) - 跨多个团队和项目扩展性能测试的指南。
  - [Part 2 - JavaScript tools, shared libraries, and TypeScript](https://grafana.com/blog/2024/05/02/setting-up-your-grafana-k6-performance-testing-suite-javascript-tools-shared-libraries-and-more/) - 使用 JavaScript 工具、共享库和 TypeScript 设置您的 k6 性能测试套件。
- [Distributed load testing with k6](https://feryn.eu/presentations/distributed-load-testing-k6-confoo23) - Thijs Feryn 出席 2023 年蒙特利尔国际食品博览会。
- [Load Testing with k6](https://medium.com/@dan.ryan.emmons/qa-load-testing-with-k6-io-c11c2afced04) - k6 的特性和功能的简要概述。
- [Test and visualize with InfluxDB, Grafana and K6](https://medium.com/@naoko.reeves/load-test-with-k6-and-visualize-with-influxdb-and-grafana-c6097a6f6d0a) - 设置负载测试并使用 grafana 仪表板将其可视化。
- [Open source load testing tool review 2020](https://grafana.com/blog/2020/03/03/open-source-load-testing-tool-review/) - 最流行的开源负载测试工具的详细比较。
- [Load Testing Your API with Swagger/OpenAPI and k6](https://k6.io/blog/load-testing-your-api-with-swagger-openapi-and-k6) - 根据 OpenAPI 规范生成 k6 负载测试脚本。
- [Load Testing Your API with Postman](https://grafana.com/blog/2020/04/19/load-testing-your-api-with-postman/) - 如何使用 Postman 集合来负载测试您的 API。
- [Load Testing & Black Friday capacity planning](https://medium.com/back-market-engineering/how-back-market-sres-prepared-for-black-friday-5f017f343408) - Back Market 如何通过基于 k6 的负载测试为黑色星期五做好准备。
- [Load Testing SQL Databases with k6](https://grafana.com/blog/2021/07/14/load-testing-sql-databases/) - 如何使用xk6-sql扩展直接测试SQL数据库。
- [Introducing TestRail in your K6 tests](https://dev.to/kwidera/introducing-testrail-in-you-k6-tests-eck) - 将 k6 输出报告给 TestRail。
- [Beautiful Load Testing With K6 and Docker Compose](https://medium.com/swlh/beautiful-load-testing-with-k6-and-docker-compose-4454edb3a2e3) - 如何使用 Docker Compose、K6、InfluxDB 和 Grafana 的出色组合来运行负载测试。
- [Load Testing with Azure DevOps and k6](https://medium.com/microsoftazure/load-testing-with-azure-devops-and-k6-839be039b68a) - 如何设置 Azure DevOps 以使用 k6、handleCallback 和 JUnit 执行自动化负载测试。
- [K6 — Custom Slack Integration: Metrics are the Magic of Tests](https://medium.com/geekculture/k6-custom-slack-integration-metrics-are-the-magic-of-tests-527aaf613595) - 如何使用handleSummary回调将k6输出结果发送到Slack。
- [Load testing with k6](https://levelup.gitconnected.com/load-testing-with-k6-48488c7946bb) - 使用 k6 进行负载、浸泡、压力、尖峰和烟雾测试。
- [How to write three times fewer lines of code when doing load testing](https://dev.to/tarantool/how-to-write-three-times-fewer-lines-of-code-when-doing-load-testing-9lb) - 在 Go 中构建 k6 扩展来测试 Tarantool。
- [负载测试。 k6 + TypeScript + Azure DevOps](https://alex-klaus.com/load-test-k6-typescript-azure/)
- [Performance testing with k6](https://blog.shanelee.name/2021/12/15/performance-testing-with-k6/) - 关于 API 性能测试，使用 Open API 和 TypeScript。
- [k6 introduces browser automation and Prometheus support in k6 OSS](https://grafana.com/blog/2021/11/24/k6-introduces-browser-automation-and-prometheus-support-in-k6-oss/) - 来自 Grafana 博客：ObservabilityCON 2021 上的功能公告。
- [Testing shift left observability with the Grafana Stack, OpenTelemetry, and k6](https://grafana.com/blog/2021/12/06/testing-shift-left-observability-with-the-grafana-stack-opentelemetry-and-k6/) - 来自 Grafana 博客：摩根大通平台工程执行总监 Vinodh Ravi 在 ObservabilityCON 2021 上的演讲摘要。

- [Umbraco 9 - What a Performance!](https://moriyama.co.uk/about-us/news/blog-umbraco-9-what-a-performance/) - 测试 Azure 上的 Umbraco v9 与 Umbraco v8 的性能，并比较 Windows 与 Linux。
- [On maintaining a k6 codebase, Part 1](https://filfreire.com/posts/k6_tricks_ep1) - 维护具有挑战性的 k6 负载测试代码库的个人技巧。
- [Distributed Load Testing With K6](https://engineering.empathy.co/distributed-load-testing-with-k6/) - 使用 k6-operator 和 Argo 工作流程设置分布式执行。
- [Load testing with k6 and k8s](https://www.toucantoco.com/en/tech-blog/tech-blog/load-testing-with-k6-and-k8s) - Toucan DevOps 团队解释了为什么他们选择 k6 作为负载测试工具以及如何将其部署在 k8s 上。

- [CloudPosse's Load Testing Stack](https://github.com/cloudposse/load-testing) - 使用 k6、Grafana 和 InfluxDB 进行负载测试堆栈。
- [实时压力：
AnyCable、k6、WebSockets 和 Yabeda](https://evilmartians.com/chronicles/real-time-stress-anycable-k6-websockets-and-yabeda) - Evil Martians 使用 k6 和 WebSockets 添加“实时压力”。
- [Scaling Confidently with the Load and Fault Team](https://robinhood.engineering/scaling-confidently-with-the-load-and-fault-team-122978333d9) - Robinhood 使用 k6 对 Kubernetes 系统进行负载测试。
- [Streamlining Performance Testing with K6 and ChatGPT](https://medium.com/@monish.correia/streamlining-performance-testing-with-k6-and-chatgpt-206c6c7db82b) - Monish Correia 使用 GitHub co-pilot 编写 k6 测试。

## 视频

- [k6 YouTube 频道](https://www.youtube.com/c/k6test)
- [How to use k6 Cloud for load testing](https://www.youtube.com/watch?v=ncxCIuo5tUU&list=PLJdv3RhAQXNGkRCp7Q0k77n5jif4qjz2o) - 一系列有关 k6 Cloud 入门的快速视频。
- [使用 k6 和 Grafana 进行负载测试简介（k6 数据源插件和 Prometheus Remote Write）](https://www.youtube.com/watch?v=tFsIgbqXbxM)
- [来自 Grafana ObservabilityCON：通过 Grafana 可观测性堆栈使用 k6 负载测试的介绍](https://grafana.com/go/observabilitycon/2021/k6-load-testing/)
- [来自 Grafana ObservabilityCON：使用 k6 和 Grafana 将性能测试构建到 CI 管道中，作者：Vonage 的 QA 工程师 Matthew Churcher](https://grafana.com/go/observabilitycon/2021/performance-testing-vonage/)
- [EveryoneCanContribute 咖啡馆：使用 k6 进行负载性能测试](https://youtu.be/_ty40gSaaw8)
- [播放列表 - 其他人对 k6 的评价](https://www.youtube.com/playlist?list=PLJdv3RhAQXNExTjuYN9ukawFHB7ucuejp)
  - [What is K6 & How to get started with k6](https://www.youtube.com/watch?v=ZAq87eZ1w2U) - 使用 k6 扩展实现可观察性的教程“Is it Observable?”
  - [Website Performance + Load Testing with K6 (k6.io) in 5 MINUTES!](https://www.youtube.com/watch?v=brasMBAezJY) - k6 的介绍性概述，展示如何根据 DevOps 指令从 HAR 文件创建测试。
  - [Performance Testing your web app with k6](https://www.youtube.com/watch?v=Hu1K2ZGJ_K4) - Chris James 介绍了开源负载和性能回归测试工具 k6，以及如何对 API 和网站进行负载测试。
  - [Application Load Testing with k6](https://www.youtube.com/watch?v=iQmItkazLOk) - Daniel Knittl-Frank @TechTalk Days 2021，k6 简介。
  - [Performance Testing From Zero to Hero with K6 & Azure](https://youtu.be/71N4_2Fv3I4?si=4eoRcvQfXNJR4aaa) - 何塞·路易斯·拉托雷·米拉斯 (Jose Luis Latorre Millas) 在 2021 年奥斯陆 NDC 上。
  - [AI-Powered K6 Testing: No Code, No Hassle, Just ChatGPT! 🦾🚀](https://www.youtube.com/watch?v=RYyPduBqGM4) - 在此视频中，Karthik K.K.演示 ChatGPT 如何在不编写任何代码的情况下创建 k6 测试。

## 示例/模板

- [k6 examples](https://grafana.com/docs/k6/latest/examples/) - k6 文档中常见示例的列表。
- [k6 QuickPizza examples](https://github.com/grafana/quickpizza) - 用于演示和研讨会的 Web 应用程序，包含多个 k6 示例。
- [k6-template-es6](https://github.com/grafana/k6-template-es6) - 使用 Webpack 和 Babel 的入门模板在 k6 测试中启用 ES6 功能。
- [k6-typescript-template](https://github.com/grafana/k6-template-typescript) - 使用 Webpack 捆绑器在 TypeScript 中编写 k6 测试的入门模板。
- [k6-rollup-example](https://github.com/grafana/k6-rollup-example) - 使用 Rollup 捆绑 k6 测试的示例。
- [Jahmilli/k6-example](https://github.com/Jahmilli/k6-example) - 使用 Vite（Rollup）捆绑器在 TypeScript 中编写 k6 测试的入门模板。
- [tom-miseur/k6-templates](https://github.com/tom-miseur/k6-templates/) - 针对 k6 项目的有意见的入门模板。
- [SwissLife-OSS/k6-multiscenario-template](https://github.com/SwissLife-OSS/K6-MultiScenario-template) - 使用K6实现多场景模板。
- [agilob/multiscenario-tests](https://b.agilob.net/programming/k6/multiscenario-tests/) - 一次运行多个场景。
- [Im5tu/template-k6](https://github.com/Im5tu/template-k6) - K6 性能测试套件模板。
- [mohsenny/k6-test-template](https://github.com/mohsenny/k6-test-template) - 负载测试框架。
- [kwidera/k6_framework](https://github.com/kwidera/k6_framework) - 另一个 k6 框架示例。
- [Sahanipe/pet_store](https://github.com/Sahanipe/pet_store) - Swagger PetStore API 的模块化脚本。
- [lreimer/continuous-k6k8s](https://github.com/lreimer/continuous-k6k8s) - 使用 cronjobs 在 Kubernetes 中持续运行 k6 测试。
- [luketn/docker-k6-grafana-influxdb](https://github.com/luketn/docker-k6-grafana-influxdb) - 演示如何使用 K6、Grafana 和 InfluxDB 的容器化实例运行负载测试。

## 工具

- [k6-to-junit](https://github.com/Mattihew/k6-to-junit) - 用于将 k6 输出转换为 JUnit XML 以便于 CI 轻松使用的工具。
- [k6-reporter](https://github.com/benc-uk/k6-reporter) - 用于将 k6 输出转换为 HTML 报告的工具。
- [k6-html-reporter](https://github.com/szboynono/k6-html-reporter) - 用于生成 k6 HTML 报告的工具。
- [har-to-k6](https://github.com/grafana/har-to-k6) - 用于将 HAR 录音转换为 k6 测试脚本的工具。
- [postman-to-k6](https://github.com/grafana/postman-to-k6) - 用于将 Postman 集合转换为 k6 测试脚本的工具。
- [k6 generator](https://github.com/OpenAPITools/openapi-generator) - 用于将 Swagger/OpenAPI 规范转换为 k6 测试脚本的工具。
- [jmeter-to-k6](https://github.com/grafana/jmeter-to-k6) - 用于将 JMeter 测试用例转换为 k6 测试脚本的工具。
- [jslib.k6.io](https://jslib.k6.io/) - 适用于 k6 脚本的实用实用程序库。
- [k6 for visual studio code](https://marketplace.visualstudio.com/items?itemName=k6.k6&ssr=false#overview) - 用于直接从 IDE 运行 k6 的市场扩展。
- [k6 for IntelliJ](https://plugins.jetbrains.com/plugin/16141-k6) - 基于 IntelliJ 的插件，用于在本地或从 IntelliJ IDE 在 [k6 Cloud](https://app.k6.io/) 中运行和调试 \[sic!\] k6 测试。
- [k6 Testkube 执行器](https://kubeshop.github.io/testkube/executor-k6/)
- [k6-junit](https://github.com/simbadltd/k6-junit) - k6 JUnit 摘要导出器库。
- [k6-expect](https://github.com/simbadltd/k6-expect) - k6 库，通过提供类似笑话的期望语法来简化以功能方式编写测试的过程。

## 持续集成/持续交付

- [k6 适用于 AWS CodeBuild](https://k6.io/blog/integrating-k6-with-aws-codebuild/)
- [k6 用于 Azure Pipelines](https://k6.io/blog/integrating-load-testing-with-azure-pipelines/)
- [k6 竹子](https://k6.io/blog/integrating-k6-with-bamboo/)
- [k6 好友](https://k6.io/blog/integrating-k6-with-buddy-devops/)
- [CircleCI 的 k6](https://grafana.com/blog/2022/03/06/load-testing-with-circleci/)
- [k6 代表举报者](https://grafana.com/blog/2022/04/28/deployment-time-testing-with-grafana-k6-and-flagger/)
- [k6 用于 GitHub 操作](https://k6.io/blog/load-testing-using-github-actions/)
- [k6 亚搏体育app](https://grafana.com/blog/2020/09/27/load-testing-with-gitlab/)
- [k6 用于 Google Cloud Build](https://k6.io/blog/integrating-k6-with-google-cloud-build/)
- [k6 詹金斯](https://k6.io/blog/integrating-load-testing-with-jenkins/)
- [k6 代表 Keptn](https://k6.io/blog/performance-testing-in-keptn-using-k6/)
- [k6 适用于 TeamCity](https://k6.io/blog/load-testing-using-teamcity-and-k6/)



## 扩展

- [k6 扩展](https://grafana.com/docs/k6/latest/extensions/)
- [GitHub Topic: xk6](https://github.com/topics/xk6) - 探索标有 xk6 标签的 k6 扩展。
- [Extension Registry](https://grafana.com/docs/k6/latest/extensions/explanations/extensions-registry/) - k6 扩展的精选列表。

### 官方

- [xk6-client-tracing](https://github.com/grafana/xk6-client-tracing) - 用于负载测试分布式跟踪后端的客户端。
- [xk6-disruptor](https://github.com/grafana/xk6-disruptor) - 注入故障来测试💣。
- [xk6-exec](https://github.com/grafana/xk6-exec) - 运行外部命令。
- [xk6-kubernetes](https://github.com/grafana/xk6-kubernetes) - 与 Kubernetes 集群交互。
- [xk6-loki](https://github.com/grafana/xk6-loki) - 用于负载测试 Loki 的客户端。
- [xk6-notification](https://github.com/grafana/xk6-notification) - 创建通知。
- [xk6-output-influxdb](https://github.com/grafana/xk6-output-influxdb) - 将结果导出到 InfluxDB v2。
- [xk6-output-kafka](https://github.com/grafana/xk6-output-kafka) - 将 k6 结果实时导出到 Kafka。
- [xk6-output-timescaledb](https://github.com/grafana/xk6-output-timescaledb) - 将 k6 结果导出到 TimescaleDB。
- [xk6-client-prometheus-remote](https://github.com/grafana/xk6-client-prometheus-remote) - 测试 Prometheus 远程写入性能。
- [xk6-sql](https://github.com/grafana/xk6-sql) - 对 SQL Server 进行负载测试（目前为 PostgreSQL、MySQL 和 SQLite3）。
- [xk6-ssh](https://github.com/grafana/xk6-ssh) - SSH。

### 社区

- [xk6-cable](https://github.com/anycable/xk6-cable) - 测试 Action Cable 和 AnyCable 功能。
- [xk6-coap](https://github.com/golioth/xk6-coap) - 与受限应用程序协议端点交互。
- [xk6-dotenv](https://github.com/szkiba/xk6-dotenv) - 从 .env 文件加载环境变量。
- [xk6-ethereum](https://github.com/distribworks/xk6-ethereum) - 以太坊协议的 K6 扩展。
- [xk6-faker](https://github.com/szkiba/xk6-faker) - 生成随机假数据。
- [xk6-file](https://github.com/avitalique/xk6-file) - 写入文件。
- [xk6-g0](https://github.com/szkiba/xk6-g0) - 用 golang 编写 k6 测试。
- [xk6-kafka](https://github.com/mostafa/xk6-kafka) - 对 Apache Kafka 进行负载测试。包括对 Avro 消息的支持。
- [xk6-kv](https://github.com/oleiade/xk6-kv) - 在 VU 之间共享键值数据。
- [xk6-mock](https://github.com/szkiba/xk6-mock) - 模拟 HTTP(S) 服务器。
- [xk6-mqtt](https://github.com/pmalhaire/xk6-mqtt) - MQTT 扩展。
- [xk6-nats](https://github.com/ydarias/xk6-nats) - 为 k6 测试提供 NATS 支持。
- [xk6-opentelemetry](https://github.com/thmshmm/xk6-opentelemetry) - 从测试脚本中生成 OpenTelemetry 信号。
- [xk6-output-elasticsearch](https://github.com/elastic/xk6-output-elasticsearch) - 将结果导出到 Elasticsearch 8.x。
- [xk6-output-prometheus-pushgateway](https://github.com/martymarron/xk6-output-prometheus-pushgateway) - 将结果导出到 Prometheus Pushgateway。
- [xk6-output-statsd](https://github.com/LeonAdato/xk6-output-statsd) - 允许将测试指标实时输出到 StatsD 服务。
- [xk6-output-timestream](https://github.com/leonyork/xk6-output-timestream) - 将结果导出到 AWS Timestream。
- [xk6-playwright](https://github.com/nicholasvuono/xk6-playwright) - 使用 Playwright 进行浏览器自动化和端到端 Web 测试。
- [xk6-prometheus](https://github.com/szkiba/xk6-prometheus) - k6 的 Prometheus HTTP 导出器。
- [xk6-prompt](https://github.com/Juandavi1/xk6-prompt) - 支持通过 UI 输入参数。
- [xk6-sse](https://github.com/phymbert/xk6-sse) - 服务器发送事件 (SSE) 的 k6 扩展。
- [xk6-tcp](https://github.com/NAlexandrov/xk6-tcp) - 向 TCP 端口发送数据。
- [xk6-top](https://github.com/szkiba/xk6-top) - 在测试运行期间更新终端上当前的 k6 指标摘要。

## 相关

- [How They Load Test](https://github.com/aliesbelik/how-they-load) - 关于世界各地的公司如何执行负载测试的资源集合。
- [Load Testing Toolkit](https://github.com/aliesbelik/load-testing-toolkit) - 用于调试、基准测试、负载和压力测试代码或服务的开源工具的集合。
- [awesome-http-benchmark](https://github.com/denji/awesome-http-benchmark) - HTTP 基准测试工具、测试/调试和restAPI (RESTful) 的集合。

## 贡献

<!-- lint disable double-link -->
想要帮助完善此列表吗？耶，太棒了！不过，在开始之前，请先查看我们的[行为准则](code_of_conduct.md) 和[贡献指南](contributing.md)。
<!-- lint enable double-link -->
