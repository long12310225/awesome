<!--lint ignore no-dead-urls awesome-license-->
# 很棒的谷歌云 [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
<!--lint ignore double-link-->
[<img src="https://www.gstatic.com/images/branding/productlogos/google_cloud/v8/web-96dp/logo_google_cloud_color_1x_web_96dp.png"align="right">](https://cloud.google.com)

<!--lint ignore double-link-->
[Google Cloud](https://cloud.google.com) 的精彩应用程序、工具和资源的精选列表。

Google Cloud 是一套模块化云服务，包括计算、数据存储、数据分析和机器学习，以及一组管理工具。

如果您是 Google Cloud 新手，可以通过[免费试用](https://cloud.google.com/free-Trial/) 进行尝试。

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
## 内容

- [General](#general)
- [Compute](#compute)
  - [应用引擎](#app-engine)
  - [云功能](#cloud-functions)
  - [云跑](#cloud-run)
  - [Kubernetes 引擎](#kubernetes-engine)
- [Cross-product](#cross-product)
  - [Python](#python)
  - [Security](#security)
- [云端人工智能](#cloud-ai)
  - [云视觉API](#cloud-vision-api)
- [存储和数据库](#storage--databases)
- [Monorepo](#monorepo)
  - [Bazel、gRPC、协议缓冲区](#bazel-grpc-protocol-buffers)
- [大数据](#big-data)
  - [Apache Beam 和数据流](#apache-beam--dataflow)
  - [Bigtable](#bigtable)
  - [BigQuery](#bigquery)
  - [Pub/Sub](#pubsub)
- [互动学习资源](#interactive-learning-resources)
- [其他很棒的清单](#other-awesome-lists)
- [关于本文档](#about-this-document)
  - [License](#license)
  - [Disclaimer](#disclaimer)
  - [Contributing](#contributing)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## 一般

- ["The Google Cloud Developer Cheat Sheet" by Greg Wilson](https://github.com/gregsramblings/google-cloud-4-words) - 用 4 个或更少的单词描述 Google Cloud 系列中的所有产品的列表。
- ["Google Cloud - Jumpstart, Tutorials & Community!" by David das Neves](https://www.linkedin.com/pulse/google-cloud-jumpstart-tutorials-community-david-das-neves/) - 有关 GCP 的其他链接，包括教程、解决方案和社区。

## 计算

- [Google Compute Engine](https://cloud.google.com/products/compute/) - 从应用程序平台到容器再到虚拟机，云计算可根据您的需求量身定制。

### 应用引擎

- [Running Parse server on Google App Engine](https://cloud.google.com/nodejs/resources/frameworks/parse-server) - 使用示例 Node.js 应用程序在 Google App Engine 上部署并运行 Parse 服务器。
- [SlackEngine](https://github.com/thesandlord/SlackEngine) - 在 Google App Engine 上运行的 Slack 邀请程序。

### 云功能

- [Functions Framework](https://github.com/GoogleCloudPlatform/functions-framework) - 用于编写可移植 Google Cloud 函数的一组开源库。

- [Goblet](https://github.com/anovis/goblet) - 一个使用 Google Cloud 函数进行无服务器 Python 应用程序开发的开源库。

### 云跑

- [Awesome Cloud Run](https://github.com/steren/awesome-cloudrun) - 精彩的 Cloud Run 应用程序的广泛列表。

### Kubernetes 引擎

- [GKE Policy Automation](https://github.com/google/gke-policy-automation) - 用于根据配置最佳实践验证 GKE 集群的工具和策略库。

- [Real-time Simon Says](https://github.com/grpc-ecosystem/grpc-simon-says) - 如果你小时候玩过70年代的掌上游戏《西蒙》，你就知道这是什么。有适用于 Web、IoT (arduino)、Android 和命令行的示例客户端。使用 [gRPC](https://grpc.io) 构建用于双向流，并使用 [Kubernetes](https://kubernetes.io) 构建可扩展性。

<!--lint ignore double-link-->
- [Click to Deploy Charts Repo](https://github.com/GoogleCloudPlatform/click-to-deploy/tree/master/k8s) - [Google Cloud Marketplace](https://cloud.google.com/marketplace) 上列出的 Google Click to Deploy 解决方案的来源。提供几个示例，其中包含有关如何在 [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine) 集群中安装的详细自述文件。

<!--lint ignore double-link-->
- [Bank of Anthos](https://github.com/GoogleCloudPlatform/bank-of-anthos/) - 模拟银行支付处理网络的基于 HTTP 的 Web 应用程序示例。它在 [Google Kubernetes Engine (GKE)](https://cloud.google.com/kubernetes-engine) 上运行，并展示了许多其他 Google Cloud 产品，例如 [Anthos Service Mesh (ASM)](https://cloud.google.com/anthos/service-mesh)、[Anthos Config Management (ACM)](https://cloud.google.com/anthos/config-management)、[Cloud操作](https://cloud.google.com/products/operations)、[Cloud SQL](https://cloud.google.com/sql/docs)、[Cloud Build](https://cloud.google.com/build) 和 [Cloud Deploy](https://cloud.google.com/deploy)。

<!--lint ignore double-link-->
- [Online Boutique](https://github.com/GoogleCloudPlatform/microservices-demo/) - 模拟电子商务商店的基于 gRPC 的 Web 应用程序示例。它在 [Google Kubernetes Engine (GKE)](https://cloud.google.com/kubernetes-engine) 上运行，由 5 种不同语言的 11 个微服务构建，并展示了许多其他 Google Cloud 产品。

## 叉积

### 蟒蛇

- [Talisman](https://github.com/GoogleCloudPlatform/flask-talisman) - 为 [Flask](http://flask.pocoo.org/) 应用程序提供简单的安全标头（HTTPS、HSTS 和 CSP）。

### 安全性

- [Forseti](https://forsetisecurity.org/) - 扫描您的 GCP 资源，确保访问控制按照您的预期设置，并防止不安全的更改。

## 云端人工智能

- [Google Cloud AI](https://cloud.google.com/products/ai/) - 快速、大规模、易于使用的人工智能产品和服务。

### 云视觉API

- [Bot for Facebook Messenger](https://github.com/jshin49/fb-vision-bot) - 该机器人使用 Google Cloud Vision API 来检测发送给它的图像中的人脸、标签、地标、徽标、文本、显式内容和属性。

## 存储和数据库

- [Google Cloud Storage](https://cloud.google.com/products/storage/) - 满足您所有数据需求的存储。
- [Cloud Datastore adapter for the JSData ORM](https://github.com/GoogleCloudPlatform/js-data-cloud-datastore) - `js-data-cloud-datastore` 是 [JSData](http://www.js-data.io) 的适配器，是 Node.js 和浏览器的 ORM。

## 莫诺雷波

### Bazel、gRPC、协议缓冲区

- [StartupOS](https://github.com/google/startup-os) - 包含使用 Google 开源工具和部署到云的示例的 monorepo。

## 大数据

- [Google Cloud Big Data](https://cloud.google.com/products/big-data/) - 使用 Google Cloud 数据分析产品高效捕获、处理和分析数据。

### Apache Beam 和数据流

- [Dataflow Templates](https://github.com/GoogleCloudPlatform/DataflowTemplates) - Google 提供的 Cloud Dataflow 模板管道用于解决简单的云内数据任务。
- [Scio](https://github.com/spotify/scio) - 用于 Google Cloud Dataflow 和 Apache Beam 的 Scala API。

### 大表

- [Heroic](https://github.com/spotify/heroic) - 时间序列数据库，使用 Google Cloud Bigtable 作为存储后端。
- [OpenTSDB](http://opentsdb.net/) - 时序数据库，使用Google Cloud Bigtable作为存储后端； [将其部署在 GKE 上](https://cloud.google.com/solutions/opentsdb-cloud-platform)。
- [JanusGraph](http://janusgraph.org/) - 分布式图数据库，使用Google Cloud Bigtable作为存储后端； [将其部署在 GKE 上](https://cloud.google.com/solutions/running-janusgraph-with-bigtable)。
- [TensorFlow](https://www.tensorflow.org/) - 机器学习框架，与 Google Cloud Bigtable 良好集成，作为高性能 ML 模型训练的源和汇；与 CPU、GPU 和 TPU 一起使用。 [使用 TensorFlow + Cloud Bigtable 训练 ResNet-50 模型](https://cloud.google.com/tpu/docs/tutorials/bigtable-resnet)。

### 大查询

- [Apache Zeppelin](http://zeppelin.apache.org/) - 用于交互式分析的基于网络的笔记本，与 Google BigQuery 配合使用。
- [Dekart](https://dekart.xyz/) - 基于 Kepler.gl 的 Google BigQuery 地理空间分析工具。
- [SQLtools for BigQuery](https://github.com/evidence-dev/sqltools-bigquery-driver) - 用于运行查询和探索数据库的 VSCode 扩展。
- [BigQuery Utils](https://github.com/GoogleCloudPlatform/bigquery-utils) - 用于 BigQuery 中迁移和数据仓库操作的有用脚本、udf、视图和其他实用程序。
- [Spark-BigQuery](https://github.com/spotify/spark-bigquery) - 在 Apache Spark、SQL 和 DataFrames 中支持 Google BigQuery。

### 发布/订阅

- [PSQ](https://github.com/GoogleCloudPlatform/psq) - 受 [rq](http://python-rq.org/) 启发的 Python 分布式任务队列，使用 Google Cloud Pub/Sub。

## 互动学习资源

- [Google Cloud Training Docs](https://cloud.google.com/compute/docs/tutorials) - 谷歌自己的云实用指南。
- [Google Cloud Community Documentation](https://cloud.google.com/community/tutorials/) - 按照 Google Cloud 社区提交的这些分步演练和教程，了解如何使用 Google Cloud 服务。
- [Qwiklabs](https://google.qwiklabs.com) - 用于学习云计算并获得徽章的动手实验室。
- [Google Cloud Codelabs](https://codelabs.developers.google.com/cloud) - GCP Codelabs 涵盖 Google Cloud 基础知识、计算、数据、移动、监控、机器学习和网络等主题。
- [Play with Kubernetes](https://labs.play-with-k8s.com) - 一个简单、互动且有趣的学习 Kubernetes 的游乐场。
- [Google Cloud Coursera Courses](https://www.coursera.org/googlecloud) - Coursera 上可用的 Google Cloud 课程列表。

## 其他很棒的清单
<!--lint ignore double-link-->
- [Awesome](https://github.com/sindresorhus/awesome) - 真棒中的真棒。
- [Awesome Firebase](https://github.com/jthegedus/awesome-firebase) - 基于 Google Cloud 构建的应用开发平台。
- [Awesome Go](https://github.com/avelino/awesome-go) - Google 设计的一种静态类型、编译型高级编程语言。
- [Awesome Kubernetes](https://github.com/ramitsurana/awesome-kubernetes) - 用于自动化软件部署、扩展和管理的开源容器编排系统。
- [Awesome TensorFlow](https://github.com/jtoy/awesome-tensorflow) - 用于机器学习和人工智能的免费开源软件库。
- [Awesome GCP Certifications](https://github.com/ddneves/awesome-gcp-certifications) - 通过行业认可的 Google Cloud 认证展示您的知识和技能。
- [Awesome Cloud Build](https://github.com/Timtech4u/awesome-cloudbuild) - 来自 Google Cloud 的无服务器 CI/CD 平台。
- [Awesome Bigtable](https://github.com/zrosenbauer/awesome-bigtable) - 用于大规模机器学习、运营分析和面向用户的应用程序的低延迟 NoSQL 数据库服务。
- [Awesome Spanner](https://github.com/rakyll/awesome-spanner) - 高度可扩展的数据库，将无限的可扩展性与关系语义相结合。


## 关于本文档

### 许可证
<!--lint ignore double-link-->
[![Creative Commons License](https://i.creativecommons.org/l/by/4.0/88x31.png)](https://creativecommons.org/licenses/by/4.0/)
<!--lint ignore double-link-->
本作品根据 [知识共享署名 4.0 国际许可证](https://creativecommons.org/licenses/by/4.0/) 获得许可。

### 免责声明

此列表不是 Google 官方产品。此列表中的链接也不一定指向官方 Google 产品。

### 贡献

如果您发现或构建了使用 Google Cloud 的出色内容，请按照 [CONTRIBUTING.md](CONTRIBUTING.md) 中的说明将其包含在此处。
