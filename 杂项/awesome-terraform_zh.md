# 很棒的 Terraform <!-- 目录中省略 --> [![Awesome](https://cdn.jsdelivr.net/gh/sindresorhus/awesome@d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

[![Link Checker](https://github.com/shuaibiyy/awesome-tf/actions/workflows/link-checker.yml/badge.svg)](https://github.com/shuaibiyy/awesome-tf/actions/workflows/link-checker.yml)
[![Misspell Check](https://github.com/shuaibiyy/awesome-tf/actions/workflows/misspell.yml/badge.svg)](https://github.com/shuaibiyy/awesome-tf/actions/workflows/misspell.yml)
[![Not Found Check](https://github.com/shuaibiyy/awesome-tf/actions/workflows/notfound.yml/badge.svg)](https://github.com/shuaibiyy/awesome-tf/actions/workflows/notfound.yml)

> [HashiCorp 的 Terraform](https://www.terraform.io/) 上的精选资源列表。
> [<img src="https://raw.githubusercontent.com/shuaibiyy/awesome-terraform/master/terraform.svg"align="right" width="100">](https://terraform.io)
> 欢迎您的[贡献](https://github.com/shuaibiyy/awesome-tf/blob/master/contributing.md)！

Terraform 使您能够安全且可预测地创建、更改和改进生产基础设施。它是一个开源工具，可将 API 编码为声明性配置文件，这些文件可以在团队成员之间共享、视为代码、进行编辑、审查和版本控制。

## 内容 <!-- 目录中省略 -->

- [Legend](#legend)
- [官方资源](#official-resources)
- [Community](#community)
- [Books](#books)
- [学习与学习](#learning-and-studying)
- [Apps](#apps)
- [教程和博客文章](#tutorials-and-blog-posts)
  - [初学者指南](#beginner-guides)
  - [编写自定义提供程序](#writing-custom-providers)
  - [How-To](#how-to)
  - [多环境配置](#multi-environment-configuration)
  - [Azure](#azure)
  - [AWS](#aws)
  - [谷歌云](#google-cloud)
  - [Miscellaneous](#miscellaneous)
- [社区模块](#community-modules)
- [自托管注册表](#self-hosted-registries)
- [托管注册中心](#managed-registries)
- [Providers](#providers)
  - [Hashicorp 支持的提供商](#hashicorp-supported-providers)
  - [供应商支持的提供商](#vendor-supported-providers)
  - [社区提供者](#community-providers)
- [Testing](#testing)
- [Tools](#tools)
  - [CI](#ci)
  - [VS 代码扩展](#vs-code-extensions)
- [Libraries](#libraries)
- [Boilerplates](#boilerplates)
- [自托管 Terraform 平台](#self-hosted-terraform-platforms)
- [托管 Terraform 平台：heavy\_dollar\_sign：](#managed-terraform-platforms-heavy_dollar_sign)
- [Terraform 企业工具](#terraform-enterprise-tooling)
- [Videos](#videos)
- [编辑器插件](#editor-plugins)
- [License](#license)

## 传奇

- 与 _terraform >= 0.12_ 不兼容：ghost：
- 被遗弃的：头骨：
- 货币化：heavy_dollar_sign：

## 官方资源

- [Hashicorp Terraform 博客](https://www.hashicorp.com/en/blog/products/terraform)
- [地形简介](https://developer.hashicorp.com/terraform/intro)
- [地形文档](https://developer.hashicorp.com/terraform/docs)
- [地形学习](https://developer.hashicorp.com/terraform/tutorials)

## 社区

- [weekly.tf - Terraform Weekly Newsletter](https://www.weekly.tf/) - 每周通讯，涵盖 Terraform 新闻、开源项目、公告和讨论。
- [完整的 Terraform 文档作为 PDF 文件（每晚更新）](https://github.com/antonbabenko/terraform-docs-as-pdf) :skull:
- [Terraform AWS 模块](https://github.com/terraform-aws-modules) + [元配置存储库](https://github.com/terraform-aws-modules/meta)
- [Terraform 错误跟踪器](https://github.com/hashicorp/terraform/issues)
- [Terraform 备忘单](https://vivid-badger-c30.notion.site/Terraform-Cheatsheet-352d7b505fb980618d5de73aa086d1d4)
- [Terraform 社区模块](https://github.com/terraform-community-modules)
- [Terraform Twitter 社区](https://twitter.com/i/communities/1501688565884928007) <!-- markdown-link-check-disable-line -->
- [地形讨论](https://discuss.hashicorp.com/c/terraform-core/27)
- [Terraform 提供程序/模块注册表](https://registry.terraform.io/)
- [Terraform PDF 文档](https://github.com/dohsimpson/terraform-doc-pdf) :skull:
- [Terraform 路线图](https://roadmap.sh/terraform)
- [Terragrunt 参考架构](https://github.com/antonbabenko/terragrunt-reference-architecture) :skull:
- [The Claude Agent Skill for Terraform and OpenTofu - testing, modules, CI/CD, and production patterns](https://github.com/antonbabenko/terraform-skill) - Claude Terraform 和 OpenTofu 的代码技能 — 测试、模块设计、CI/CD 工作流程和生产模式。
- [awesome-terraform-compliance](https://github.com/antonbabenko/awesome-terraform-compliance) - 用于 Terraform 合规性和安全性的工具、框架和资源的精选列表。
- 特定语言社区：
  - [Telegram（乌克兰语社区）](https://t.me/terraform_ukraine)

## 书籍

- [关于 Terraform 的大书](https://www.amazon.com/Big-Little-Book-Terraform-Omos-ebook/dp/B07PWYPNX8/)
- [使用 Docker、Kubernetes 和 Terraform 引导微服务，第二版](https://www.manning.com/books/bootstrapping-microservices-second-edition)
- [深入探讨 Azure 上的 Terraform](https://link.springer.com/book/10.1007/978-1-4842-7328-9)
- [Terraform 入门，第二版。](https://www.amazon.com/Getting-Started-Terraform-production-infrastructure/dp/1788623533/)
- [HashiCorp 基础设施自动化认证指南](https://www.amazon.com/HashiCorp-Infrastructure-Automation-Certification-Guide-ebook/dp/B092KM7LXC/)
- [IaC 从 Terraform 开始（韩语）](https://product.kyobobook.co.kr/detail/S000202478097)
- [基础设施即代码](https://www.oreilly.com/library/view/infrastructure-as-code/9781491924334/)
- [基础设施即代码的模式和实践：以 Python 和 Terraform 为例](https://www.manning.com/books/infrastructure-as-code-patterns-and-practices)
- [Terraform Best Practices](https://www.terraform-best-practices.com/) - [开源电子书](https://github.com/antonbabenko/terraform-best-practices)
- [地形食谱](https://www.amazon.com/Terraform-Cookbook-Efficiently-Infrastructure-platforms/dp/1800207557)
- [Terraform for Ops 电子书](https://www.terraformforops.com)
- [行动中的 Terraform](https://www.manning.com/books/terraform-in-action)
- [深度地形](https://www.manning.com/books/terraform-in-depth)
- [Terraform：启动和运行，第三版。](https://www.terraformupandrunning.com/)
- [地形书](https://terraformbook.com/)

## 学习与学习

- [Terraform Academy](https://www.terraformacademy.app) - 交互式 Terraform / IaC 学习平台，提供实践实验室、认证准备（HashiCorp、AWS、GCP、Azure、Docker、Kubernetes、GitOps）、AI 辅导和进度跟踪。另请参阅 [SRE 专业提示博客](https://www.terraformacademy.app/protips/?cat=sre-pro-tips) 和下面的移动/PWA 应用程序。
- [compliance.tf docs](https://compliance.tf/docs/) - SOC 2、PCI DSS、HIPAA、NIST 800-53 和 35 多个其他合规性控制的免费 Terraform 实现 — 用于编写合规基础设施代码的开放参考。

## 应用程序

用于随时随地学习和使用 Terraform 的移动、桌面和 PWA 应用程序。

- [Terraform Academy — iOS](https://apps.apple.com/us/app/terraform-academy/id6745738634) - 适用于 Terraform Academy 交互式学习平台的本机 iOS 应用程序。实践实验室、认证准备（HashiCorp、AWS、GCP、Azure、Docker、Kubernetes、GitOps）、AI 辅导和跨设备进度同步。
- [Terraform Academy — Android](https://play.google.com/store/apps/details?id=com.terraformacade1.app) - 适用于 Terraform Academy 学习平台的本机 Android 应用程序，具有与 iOS 和 Web 版本相同的实验室、证书准备和 AI 辅导。
- [Terraform Academy — PWA / Web App](https://www.terraformacademy.app/) - Terraform Academy 的可安装渐进式 Web 应用程序版本。离线工作，安装到任何平台上的主屏幕，并与移动应用程序同步进度。

## 教程和博客文章

### 初学者指南

- [A Comprehensive Guide to Terraform](https://www.gruntwork.io/blog/a-comprehensive-guide-to-terraform) - 《Terraform：启动和运行》作者的一系列博客文章指导读者从开始使用 Terraform 到在现实世界中使用它。
- [Using Terraform for Cloud Deployments - Part 1](https://dev.to/koenighotze/using-terraform-for-cloud-deployments---part-1) - 配置 EC2 实例。
- [Hello, world: The Fargate/Terraform tutorial I wish I had](https://section411.com/2019/07/hello-world/) - 描述从头开始设置 ECS Fargate 集群的博客文章
- [Terraform Security Guide](https://sysdig.com/blog/terraform-security-best-practices/) - 描述使用 Terraform 时的安全最佳实践的博客文章
- [Building a SaaS API? Don't Forget Your Terraform Provider](https://www.speakeasy.com/blog/build-terraform-providers) - 为什么你应该编写一个 terraform 提供程序
- [Complete Terraform Course in French (Free)](https://blog.stephane-robert.info/docs/infra-as-code/provisionnement/terraform/introduction/) - 这是一门全面且免费的法语课程，旨在掌握 Terraform，从初学者到高级用法，提供实践示例和最佳实践。

### 编写自定义提供程序

- [Creating custom terraform providers](https://blog.pelo.tech/creating-custom-terraform-providers-341311823fa2) - 创建自定义提供程序的指南。
- [Writing a Terraform provider](https://web.archive.org/web/20220516140659/http://blog.jfabre.net/2017/01/22/writing-terraform-provider/) - 创建自定义提供程序的指南。
- [Writing Custom Providers](https://developer.hashicorp.com/terraform/plugin/sdkv2) - 创建自定义提供程序的官方文档。
- [Terraform Provider Code generation](https://www.speakeasy.com/docs/terraform/create-terraform) - 根据 OpenAPI 规范生成 terraform 提供程序的指南（供应商支持）

### 操作方法

- [How To Write OPA for Terraform](https://scalr.com/learning-center/opa-series-part-1-open-policy-agent-and-terraform) - 如何使用开放策略代理来评估和实施 Terraform 计划上的策略
- [Deploying Discourse with Terraform](https://www.hashicorp.com/en/blog/deploying-discourse-with-terraform) - 展示 Terraform 如何通过一个命令在 DigitalOcean 上创建 Discourse 的运行实例。
- [Deploying Django to AWS ECS with Terraform](https://testdriven.io/blog/deploying-django-to-ecs-with-terraform/) - 了解如何使用 Terraform 启动在 ECS 上运行 Django 应用程序所需的 AWS 基础设施。
- [使用 Wercker 和 Terraform 轻松将 Seneca 微服务部署到 ECS：第一部分](https://chiefy.github.io/easily-deploy-a-seneca-microservice-to-ecs-with-wercker-and-terraform-part-i/)， [II](https://chiefy.github.io/easily-deploy-a-seneca-microservice-to-ecs-with-wercker-and-terraform-part-ii/) & [III](https://chiefy.github.io/easily-deploy-a-seneca-microservice-to-ecs-with-wercker-and-terraform-part-iii/) - 说明如何将 Terraform 合并到微服务中部署管道。
- [Terraform for a Highly Available VPN between AWS and Azure](https://web.archive.org/web/20210616132857/https://deployeveryday.com/2020/04/13/vpn-aws-azure-terraform.html) - 用于在 AWS 和 Azure 之间部署高度可用的 VPN 的 Terraform 代码。
- [Terraforming 1Password](https://1password.com/blog/terraforming-1password) - 1Password 如何从 CloudFormation 迁移到 Terraform。
- [Tutorial: How to Use Terraform to Deploy OpenStack Workloads](https://web.archive.org/web/20170611135511/http://www.stratoscale.com/blog/openstack/tutorial-how-to-use-terraform-to-deploy-openstack-workloads/) - 说明使用 OpenStack Terraform 提供程序部署 Web 服务器是多么容易。
- [Zero Downtime Updates with HashiCorp Terraform](https://www.hashicorp.com/en/blog/zero-downtime-updates-with-terraform) - 确保基础设施零停机。
- [Google Cloud Platform for 10$ a month using terraform](https://github.com/nufailtd/terraform-budget-gcp) - 展示如何使用 terraform 创建安全的 Google Kubernetes 集群、Google Cloud Run 服务和其他基础设施元素，每月费用不到 [10 美元](https://nufailtd.github.io/budget-gcp/)。
- [Infracost + Terraform + GitHub Actions = Automate Cloud Cost Management](https://medium.com/better-programming/infracost-terraform-github-actions-automate-cloud-cost-management-a62b329f2834) - 如何在 Terraform 开发过程中使用 Infracost 作为管理云成本的护栏。
- [How To Wrap Your Terraform Provider for Pulumi](https://www.speakeasy.com/blog/pulumi-terraform-provider) - 让您的 terraform 提供商 pulumi 做好准备
- [How to Build an AWS Account Vending Machine](https://medium.com/@StackGuardian/how-to-build-an-aws-account-vending-machine-by-stackguardian-f2895e35a27b) - 使用 StackGuardian 编排的 Terraform 堆栈进行自动化、自助式 AWS 账户生命周期管理，并具有基于 SSM 的分配、EventBridge 清理触发器和 Tirith 策略实施。

### 多环境配置

- [Terraform Design Patterns: the Terrafile](https://bensnape.com/2016/01/14/terraform-design-patterns-the-terrafile/) - 使用 Terrafile 管理 Terraform 项目中的 Terraform 模块及其版本。
- [Terraform, VPC, and why you want a tfstate file per env](https://charity.wtf/2016/03/30/terraform-vpc-and-why-you-want-a-tfstate-file-per-env/) - 在具有多个环境的大型项目中使用 Terraform 时遇到的一些问题以及如何避免这些问题。
- [Using Pipelines to Manage Environments with Infrastructure as Code](https://medium.com/@kief/https-medium-com-kief-using-pipelines-to-manage-environments-with-infrastructure-as-code-b37285a1cbf5) - 解释构建管道以处理从一种环境到另一种环境的基础设施变化的不同方法。

### 天蓝色

- [Learning HashiCorp Terraform](https://web.archive.org/web/20201108000713/https://www.g10s.io/hashicorp-terraform/) - Azure 指南。
- [New Terraform Azure Automation Resources](https://bgelens.nl/terraform-automation-resources/) - Azure 自动化。
- [Terraforming Azure PaaS](https://devkimchi.com/2019/01/21/terraforming-azure-paas/) - 在 Azure 上部署 PaaS 资源。

### AWS

- [AWS Lambda the Terraform Way](https://github.com/nsriram/lambda-the-terraform-way) - 除了执行函数之外，还可以使用 Terraform 深入了解 AWS Lambda。还包括与 S3、API Gateway、DynamoDB、Kinesis、SQS 集成的指南。
- [Managing AWS Lambda Functions with Terraform](https://spacelift.io/blog/terraform-aws-lambda) - AWS Lambda 的用途是什么以及如何使用 Terraform 管理 AWS Lambda 函数？

### 谷歌云

- [Managing infrastructure as code with Terraform, Cloud Build, and GitOps](https://docs.cloud.google.com/docs/terraform/resource-management/managing-infrastructure-as-code) - 使用 Terraform、Cloud Build 和 GitOps 设置和管理基础设施即代码。
- [Getting started with Terraform on Google Cloud](https://docs.cloud.google.com/docs/terraform/create-vm-instance) - 使用 Terraform 在 Google Cloud 中创建虚拟机并启动基本的 Python Flask 服务器。
- [Managing Cloud Infrastructure with Terraform](https://www.skills.google/course_templates/746) - 使用 Terraform 部署 Kubernetes 负载均衡器服务、使用 Terraform 部署基于 HTTPS 内容的负载均衡器、使用 Terraform 进行模块化负载均衡 - 区域负载均衡器、使用 Terraform 自定义提供程序、使用 Terraform 部署 Cloud SQL、使用 Terraform 在 Google Cloud 和 AWS 之间构建 VPN。
- [Hashicorp Terraform Tutorials for Google Cloud](https://developer.hashicorp.com/terraform/tutorials/gcp-get-started) - 开始使用 Google Cloud 上的 Terraform。
- [IAC - Terraform and Terragrunt on Google Cloud](https://www.academeez.com/courses/terraform) - 关于使用 Terraform/OpenTofu 和 Terragrunt 在 Google Cloud 上创建基础设施的开源 MIT 许可课程
- [Self-host n8n on Google Cloud Run](https://github.com/datawranglerai/self-host-n8n-on-gcr) - Terraform 配置和指南，用于通过 Redis 使用 Cloud SQL、Secret Manager 和可选队列模式在 Cloud Run 上部署 n8n 工作流自动化。

### 杂项

- [Sharing data between Terraform configurations](https://web.archive.org/web/20230927082422/https://jamesmckay.net/2016/09/sharing-data-between-terraform-configurations/) - 说明如何使用远程状态在 Terraform 配置之间共享数据。
- [The Segment AWS Stack](https://web.archive.org/web/20250322120753/https://segment.com/blog/the-segment-aws-stack/) - 显示由 Terraform 提供支持的基础设施的幕后花絮，该基础设施解决了 [Segment](https://segment.com/) 上的[百万美元工程问题](https://segment.com/blog/the-million-dollar-eng-problem/)。
- [超可靠基础设施即代码的 3 大 Terraform 测试策略](https://www.contino.io/insights/top-3-terraform-testing-strategies-for-ultra-reliable-infrastructure-as-code)
- [Two Weeks with Terraform](https://charity.wtf/2016/02/23/two-weeks-with-terraform/) - 一些在野外使用 Terraform 来之不易的经验，以及一些操作智慧。
- [Terraform: Beyond the Basics with AWS](https://aws.amazon.com/blogs/apn/terraform-beyond-the-basics-with-aws/) - 使用 Terraform 来配置示例 AWS 架构的演示说明。
- [Terraform cost estimation](https://github.com/antonbabenko/terraform-cost-estimation) - 来自 Terraform 计划 (0.12+) 或状态文件的匿名、免费成本估算。也可在浏览器中访问 [terraform-cost-estimation.com](https://terraform-cost-estimation.com)。
- [如何调试 Terraform 项目：教程](https://spacelift.io/blog/terraform-debug)

## 社区模块

有关此处未列出的更多社区模块，请参阅 [Terraform 模块注册表](https://registry.terraform.io/)。

- [nis2shield/infrastructure](https://github.com/nis2shield/infrastructure) - 用于自动化 NIS2 合规性和安全基础设施部署的 Terraform 模块。
- [rancher-terraform-digitalocean](https://github.com/lunagt/rancher-terraform-digitalocean) - digitalocean 上的 Rancher 服务器。
- [segmentio/stack](https://github.com/segmentio/stack) - 使用 AWS、Docker 和 ECS 配置生产基础设施。 ：头骨：
- [terraform-aws-account-lookup](https://github.com/be-bold/terraform-aws-account-lookup) - 此 Terraform 模块允许查询 AWS 账户，并以各种映射或完整列表的形式输出账户，能够将搜索过滤器应用于账户列表，并使用子模块按现有标签对账户进行分组。
- [terraform-aws-alb](https://github.com/terraform-aws-modules/terraform-aws-alb) - 在 AWS 上创建应用程序负载均衡器（经过验证的模块）。
- [terraform-aws-appconfig](https://github.com/terraform-aws-modules/terraform-aws-appconfig) - 在 AWS 上创建 AWS AppConfig 资源。
- [terraform-aws-atlantis](https://github.com/terraform-aws-modules/terraform-aws-atlantis) - 创建 Terraform 配置以在 AWS Fargate 上运行 [Atlantis](https://runatlantis.io)。支持 Github、Gitlab 和 BitBucket。
- [terraform-aws-autoscaling](https://github.com/terraform-aws-modules/terraform-aws-autoscaling) - 创建自动缩放组和启动配置（已验证的模块）。
- [terraform-aws-customer-gateway](https://github.com/terraform-aws-modules/terraform-aws-customer-gateway) - 在 AWS 上创建客户网关。
- [terraform-aws-datadog-forwarders](https://github.com/terraform-aws-modules/terraform-aws-datadog-forwarders) - 在 AWS 上创建资源以将日志/指标转发到 Datadog。
- [terraform-aws-dms](https://github.com/terraform-aws-modules/terraform-aws-dms) - 在 AWS 上创建 AWS DMS（数据库迁移服务）资源。
- [terraform-aws-dynamodb-table](https://github.com/terraform-aws-modules/terraform-aws-dynamodb-table) - 在 AWS 上创建 DynamoDB 表。
- [terraform-aws-ec2-instance](https://github.com/terraform-aws-modules/terraform-aws-ec2-instance) - 在 AWS 上创建 EC2 实例。
- [terraform-aws-ecr](https://github.com/cloudposse/terraform-aws-ecr) - 管理 AWS ECR 上的 Docker 容器注册表。
- [terraform-aws-ecs](https://github.com/terraform-aws-modules/terraform-aws-ecs) - 在 AWS 上创建 AWS ECS 资源。
- [terraform-aws-efs](https://github.com/cloudposse/terraform-aws-efs) - 定义 EFS 文件系统。
- [terraform-aws-eks](https://github.com/terraform-aws-modules/terraform-aws-eks) - 在 AWS 上创建 Elastic Kubernetes 服务（非常受欢迎的模块）。
- [terraform-aws-elb](https://github.com/terraform-aws-modules/terraform-aws-elb) - 在 AWS 上创建弹性负载均衡器（经过验证的模块）。
- [terraform-aws-eventbridge](https://github.com/terraform-aws-modules/terraform-aws-eventbridge) - 在 AWS 上创建 EventBridge 资源。
- [terraform-aws-jenkins-ha-agents](https://github.com/neiman-marcus/terraform-aws-jenkins-ha-agents) - 基于 EC2 的 Jenkins 部署，具有 HA（现货）代理。在 EFS 上运行以实现不变性。完全可定制，具有合理的默认值。
- [terraform-aws-jenkins](https://github.com/cloudposse-archives/terraform-aws-jenkins) - 使用 Jenkins 构建 Docker 映像，将其保存到 ECR 存储库，并将其部署到运行 Docker 堆栈的 Elastic Beanstalk。 ：头骨：
- [terraform-aws-key-pair](https://github.com/cloudposse/terraform-aws-key-pair) - 自动生成 SSH 密钥对（公钥/私钥）。
- [terraform-aws-lambda-auto-package](https://github.com/nozaq/terraform-aws-lambda-auto-package) - 一个 terraform 模块，用于定义 lambda 函数，自动构建和打包源文件以进行 lambda 部署。
- [terraform-aws-lambda](https://github.com/terraform-aws-modules/terraform-aws-lambda) - Terraform 模块，用于构建依赖项和包，并以无数组合创建 AWS Lambda 资源。
- [terraform-aws-managed-service-prometheus](https://github.com/terraform-aws-modules/terraform-aws-managed-service-prometheus) - 在 AWS 上创建 AWS Managed Service for Prometheus (AMP) 资源。
- [terraform-aws-modules](https://github.com/terraform-aws-modules) - 社区支持的 Terraform AWS 模块集合（包括官方 AWS 模块）。
- [terraform-aws-msk-kafka-cluster](https://github.com/terraform-aws-modules/terraform-aws-msk-kafka-cluster) - 在 AWS 上创建 AWS MSK（Kafka 托管流）资源。
- [terraform-aws-notify-slack](https://github.com/terraform-aws-modules/terraform-aws-notify-slack) - 创建 SNS 主题和 Lambda 函数，用于向 Slack 发送通知。
- [terraform-aws-postgresql-rds](https://github.com/azavea/terraform-aws-postgresql-rds) - 在 RDS 上创建 PostgreSQL。
- [terraform-aws-rds-aurora](https://github.com/terraform-aws-modules/terraform-aws-rds-aurora) - 在 AWS 上创建 RDS Aurora 集群资源（已验证模块）。
- [terraform-aws-rds-proxy](https://github.com/terraform-aws-modules/terraform-aws-rds-proxy) - 在 AWS 上创建 AWS RDS 代理资源。
- [terraform-aws-rds](https://github.com/terraform-aws-modules/terraform-aws-rds) - 在 AWS 上创建 RDS 资源（已验证模块）。
- [terraform-aws-redshift](https://github.com/terraform-aws-modules/terraform-aws-redshift) - 在 AWS 上创建 Redshift 资源。
- [terraform-aws-route53](https://github.com/terraform-aws-modules/terraform-aws-route53) - 在 AWS 上创建 Route53 资源。
- [terraform-aws-s3-bucket](https://github.com/terraform-aws-modules/terraform-aws-s3-bucket) - 在 AWS 上创建 S3 存储桶资源。
- [terraform-aws-secure-baseline](https://github.com/nozaq/terraform-aws-secure-baseline) - 使用基于 CIS Amazon Web Services Foundations 的安全基线配置设置您的 AWS 账户。
- [terraform-aws-security-group](https://github.com/terraform-aws-modules/terraform-aws-security-group) - 在 AWS 上创建 EC2-VPC 安全组（已验证模块）。
- [terraform-aws-ssh-bastion-service](https://github.com/joshuamkite/terraform-aws-ssh-bastion-service) - Terraform 计划将 ssh 堡垒部署为 AWS 上的无状态服务。
- [terraform-aws-transit-gateway](https://github.com/terraform-aws-modules/terraform-aws-transit-gateway) - 在 AWS 上创建 Transit Gateway 资源。
- [terraform-aws-vpc](https://github.com/terraform-aws-modules/terraform-aws-vpc) - 在AWS上创建VPC资源（经过验证且非常流行的模块）。
- [terraform-aws-vpn-gateway](https://github.com/terraform-aws-modules/terraform-aws-vpn-gateway) - 在 AWS 上创建 VPN 网关资源。
- [Azure Verified Modules](https://azure.github.io/Azure-Verified-Modules/) - Microsoft 官方拥有的经过验证的 Azure Terraform 模块集合，编纂了 WAF 最佳实践以实现一致的基础设施部署。
- [terraform-azurerm-aks](https://github.com/kjanshair/terraform-azurerm-aks) - 在 Azure 上创建 AKS 资源。
- [terraform-azurerm-iis](https://github.com/ghostinthewires/terraform-azurerm-iis-install) - 在 Azure VM 实例上安装 IIS 服务器。
- [terraform-azurerm-mysql](https://github.com/foreverXZC/terraform-azurerm-mysql) - 在 Azure 上创建 MySql 数据库。
- [terraform-azurerm-redis](https://github.com/rahulkhengare/terraform-azurerm-redis) - 在 Azure 上创建 Redis。
- [terraform-azurerm-sqlserver](https://github.com/metadevpro/terraform-azurerm-sqlserver-seed) - 在 Azure 上创建 SQL Server 数据库。
- [terraform-cloudflare-maintenance](https://github.com/adinhodovic/terraform-cloudflare-maintenance) - 使用 Cloudflare Workers 创建维护页面的模块。
- [terraform-digitalocean-droplet](https://registry.terraform.io/modules/terraform-digitalocean-modules/droplet/digitalocean/latest) - 用于管理 DigitalOcean Droplet 和相关资源的 Terraform 模块。
- [terraform-ecs-jenkins](https://github.com/shuaibiyy/terraform-ecs-jenkins) - 使用 Terraform 在 AWS ECS 上配置 Jenkins。
- [terraform-gce-atlantis](https://github.com/runatlantis/terraform-gce-atlantis) - 创建 Terraform 配置以在 Google 计算引擎上运行 [Atlantis](https://runatlantis.io)。
- [terraform-google-project-factory](https://github.com/terraform-google-modules/terraform-google-project-factory) - 使用共享 VPC、IAM、API 等创建和配置 Google Cloud Platform 项目。
- [terraform-kubestack](https://github.com/kbst/terraform-kubestack) - Kubestack 是 Kubernetes 平台工程团队的一个框架，用于在一个 Terraform 代码库中定义整个云原生堆栈，并通过 GitOps 不断安全地发展平台。
- [terraform-linode-k8s](https://registry.terraform.io/modules/linode/k8s/linode/latest) - 在 Linode 实例上安装 Kubernetes。
- [terraform-nixos](https://github.com/nix-community/terraform-nixos) - 一组旨在部署 NixOS 的 Terraform 模块。
- [terraform-static-website-s3-cloudfront](https://github.com/sergej-brazdeikis/terraform-static-website-s3-cloudfront) - 基于变量在 AWS S3 和 Cloudfront 上创建静态网站。
- [tf_aws_bastion_s3_keys](https://github.com/terraform-community-modules/tf_aws_bastion_s3_keys) - 在 AWS EC2 上创建堡垒主机。
- [typhoon](https://github.com/poseidon/typhoon) - 带有 Terraform 的最小且免费的 Kubernetes 发行版。

## 自托管注册表

- [anthology](https://github.com/erikvanbrakel/anthology) - 私有 Terraform 注册表实现作为官方注册表的替代方案。
- [boring-registry](https://github.com/boring-registry/boring-registry) - 具有 API 密钥身份验证和 Blob 存储支持的私有 Terraform 模块/提供程序注册表
- [citizen](https://github.com/outsideris/citizen) - 私有 Terraform 模块/提供者注册表
- [nrkno/terraform-registry](https://github.com/nrkno/terraform-registry) - 具有模块化存储后端的私有 Terraform 注册表。
- [petra](https://github.com/devoteamgcloud/petra) - 私有 Terraform 注册表管理器
- [philips-labs/terraform-registry](https://github.com/philips-labs/terraform-registry) - Terraform 注册表，用于服务 Github 上托管的任意 Terraform 提供程序版本
- [tapir](https://github.com/PacoVK/tapir) - 私人 Terraform 注册表。
- [terraform-simple-registry](https://github.com/apparentlymart/terraform-simple-registry) - Terraform 注册表协议的简单实现。
- [Terrareg](https://github.com/matthewjohn/terrareg) - Terraform 模块注册表。
- [terustry](https://github.com/veepee-oss/terustry) - 开源 terraform 提供程序注册表，充当 gitlab 或 github 版本的代理。
- [terralist](https://github.com/terralist/terralist) - Terraform 私有注册表，用于可通过 REST API 管理的模块和提供程序。

## 托管注册中心

- [Azure Verified Modules](https://azure.github.io/Azure-Verified-Modules/) - Microsoft 官方计划为 Azure 资源和架构模式提供经过验证、符合标准的 Terraform（和 Bicep）模块，与架构完善的框架保持一致。
- [cloudsmith](https://docs.cloudsmith.com/formats/terraform-modules-repository) - 为内部和外部客户提供托管包托管服务。 ：重美元符号：

## 供应商

### Hashicorp 支持的提供商

- [terraform-provider-aws](https://github.com/hashicorp/terraform-provider-aws) - 亚马逊网络服务提供商。
- [terraform-provider-azurerm](https://github.com/hashicorp/terraform-provider-azurerm) - Azure 的提供商。
- [terraform-provider-docker](https://github.com/hashicorp/terraform-provider-docker) - Docker 的提供者。 ：头骨：
- [terraform-provider-google](https://github.com/hashicorp/terraform-provider-google) - Google 云平台的提供商。
- [terraform-provider-helm](https://github.com/hashicorp/terraform-provider-helm) - Helm 的提供者。
- [terraform-provider-kubernetes](https://github.com/hashicorp/terraform-provider-kubernetes) - Kubernetes 的提供者。
- [terraform-provider-vsphere](https://github.com/vmware/terraform-provider-vsphere) - VMware vSphere 提供商。

### 供应商支持的提供商

- [terraform-provider-alicloud](https://github.com/aliyun/terraform-provider-alicloud) - 阿里云的提供商。
- [terraform-provider-artifactory](https://github.com/jfrog/terraform-provider-artifactory) - [JFrog Artifactory](https://jfrog.com/artifactory/) 的提供商。
- [terraform-provider-atlas](https://github.com/ariga/terraform-provider-atlas) - [Atlas](https://atlasgo.io/) 的提供者。
- [terraform-provider-azapi](https://github.com/Azure/terraform-provider-azapi) - Azure 资源管理器 Rest API 的提供程序
- [terraform-provider-azuredevops](https://github.com/microsoft/terraform-provider-azuredevops) - Azure DevOps (VSTS) 的提供商。
- [terraform-provider-buildkite](https://github.com/buildkite/terraform-provider-buildkite) - Buildkite 的提供者。
- [terraform-provider-checkly](https://github.com/checkly/terraform-provider-checkly) - 管理 [Checkly](https://www.checklyhq.com) 资源以进行 API 和 E2E 监控。
- [terraform-provider-coder](https://github.com/coder/terraform-provider-coder) - [Coder](https://coder.com) 的提供商
- [terraform-provider-confluent](https://github.com/confluentinc/terraform-provider-confluent) - Confluence 的提供者。
- [terraform-provider-datadog](https://github.com/DataDog/terraform-provider-datadog) - Datadog 的提供者。
- [terraform-provider-devhelm](https://github.com/devhelmhq/terraform-provider-devhelm) - [DevHelm](https://devhelm.io) 正常运行时间监控提供程序 — 将监视器、警报通道和状态页面作为代码进行管理。
- [terraform-provider-digitalocean](https://github.com/digitalocean/terraform-provider-digitalocean) - DigitalOcean 的提供商。
- [terraform-provider-dominos](https://github.com/nat-henderson/terraform-provider-dominos) - 多米诺披萨供应商。
- [terraform-provider-elasticstack](https://github.com/elastic/terraform-provider-elasticstack) - Elasticsearch 和 Kibana 的提供商。
- [terraform-provider-env0](https://github.com/env0/terraform-provider-env0) - [env0](https://www.env0.com/) 的提供者
- [terraform-provider-github](https://github.com/integrations/terraform-provider-github) - GitHub 的提供商。
- [terraform-provider-gitlab](https://github.com/gitlabhq/terraform-provider-gitlab) - GitLab 的提供商。
- [terraform-provider-graphql](https://github.com/sullivtr/terraform-provider-graphql) - GraphQL 查询和突变的提供者。
- [terraform-provider-hcloud](https://github.com/hetznercloud/terraform-provider-hcloud) - Hetzner 云提供商。
- [terraform-provider-healthchecksio](https://github.com/kristofferahl/terraform-provider-healthchecksio) - 管理 healthchecks.io 资源的提供者。
- [terraform-provider-heroku](https://github.com/heroku/terraform-provider-heroku) - Heroku 的提供者。
- [terraform-provider-ibm](https://github.com/IBM-Cloud/terraform-provider-ibm) - IBM Cloud 的提供商。
- [terraform-provider-iterative](https://github.com/iterative/terraform-provider-iterative) - Terraform 插件在构建时考虑了机器学习。
- [terraform-provider-k8s](https://github.com/banzaicloud/terraform-provider-k8s) - 简单的 Kubernetes 提供程序，适用于任何清单。
- [terraform-provider-keycloak](https://github.com/keycloak/terraform-provider-keycloak) - 用于管理 [Keycloak](https://www.keycloak.org/) 身份提供商服务器设置的提供商。
- [terraform-provider-linode](https://github.com/btobolaski/terraform-provider-linode) - Linode 的提供商。
- [terraform-provider-openstack](https://github.com/terraform-provider-openstack/terraform-provider-openstack) - OpenStack 插件。
- [terraform-provider-panos](https://github.com/PaloAltoNetworks/terraform-provider-panos) - [Palo Alto Networks 下一代防火墙](https://www.paloaltonetworks.com/network-security) 的提供商。
- [terraform-provider-phare](https://github.com/phare/terraform-provider-phare) - [Phare](https://phare.io) 的 Terraform 提供程序。
- [terraform-provider-planetscale](https://github.com/planetscale/terraform-provider-planetscale) - [PlanetScale](https://planetscale.com) 的 Terraform 提供程序（Vitess 和 Postgres）。
- [terraform-provider-qovery](https://github.com/Qovery/terraform-provider-qovery) - [Qovery](https://www.qovery.com/) 的提供商 — 管理 AWS、GCP、Azure 和 Scaleway 上的 Kubernetes 部署、环境、应用程序、数据库、Helm 图表和 Terraform 服务。
- [terraform-provider-pingdom](https://github.com/russellcardullo/terraform-provider-pingdom) - 管理 Pingdom 资源的提供者。 ：头骨：
- [terraform-provider-rancher2](https://github.com/rancher/terraform-provider-rancher2) - Rancher v2 的提供者。
- [terraform-provider-scalr](https://github.com/Scalr/terraform-provider-scalr) - [Scalr](https://www.scalr.com/) 的提供商
- [terraform-provider-secrethub](https://github.com/secrethub/terraform-provider-secrethub) - SecretHub 的提供商。 ：头骨：
- [terraform-provider-sigsci](https://github.com/signalsciences/terraform-provider-sigsci) - 信号科学提供商。
- [terraform-provider-snowflake](https://github.com/snowflakedb/terraform-provider-snowflake) - Snowflake 数据仓库的提供者。
- [terraform-provider-spinnaker](https://github.com/armory-io/terraform-provider-spinnaker) - [Spin​​naker](https://spinnaker.io/) 的提供商。
- [terraform-provider-spotinst](https://github.com/spotinst/terraform-provider-spotinst) - Spotinst 的提供者。
- [terraform-provider-stripe](https://github.com/franckverrot/terraform-provider-stripe) - Stripe 的提供者。
- [terraform-provider-ucloud](https://github.com/ucloud/terraform-provider-ucloud) - 管理UCloud资源的提供商。
- [terraform-provider-uptimerobot](https://github.com/louy/terraform-provider-uptimerobot) - 管理 uptimerobot 资源的提供者。 ：头骨：
- [terraform-provider-vaulted](https://github.com/sumup-oss/terraform-provider-vaulted) - 通过 Terraform 加密的 HashiCorp Vault 机密可以存储在 SCM（例如 Git）中。
- [terraform-provider-scp](https://github.com/splunk/terraform-provider-scp) - Splunk 云平台提供商。

### 社区提供者

- [terraform-provider-docker](https://github.com/kreuzwerker/terraform-provider-docker) - Terraform Docker 提供商。
- [terraform-provider-minio](https://github.com/aminueza/terraform-provider-minio) - 用于管理 MinIO S3 存储桶和 IAM 用户的 Terraform 提供程序。
- [terraform-provider-proxmox](https://github.com/Telmate/terraform-provider-proxmox) - Terraform Proxmox 提供商。
- [terraform-provider-terracurl](https://github.com/devops-rob/terraform-provider-terracurl) - 提供程序对您的目标端点进行托管和非托管 API 调用。
- [terraform-provider-uname](https://github.com/julienlevasseur/terraform-provider-uname) - 为 Terraform 命名提供程序。
- [terraform-provider-value](https://github.com/pseudo-dynamic/terraform-provider-value) - Terraform 的价值提供者。
- [terraform-provider-multipass](https://github.com/todoroff/terraform-provider-multipass) - Multipass 的 Terraform 提供者。
- [terraform-provider-openrouter](https://github.com/cloudopsworks/terraform-provider-openrouter) - 以代码形式管理 OpenRouter：工作区、护栏、支出限制的 API 密钥和组织成员。 Terraform + OpenTofu。
- [terraform-provider-plancost](https://github.com/plancost/terraform-provider-plancost) - 用于 Azure 成本估算和成本护栏的 Terraform 提供程序。

## 测试

- [clarity](https://github.com/xchapter7x/clarity) - 用于单元测试的 Terraform 声明性测试框架。 ：头骨：
- [kitchen-terraform](https://github.com/newcontext-oss/kitchen-terraform) - 提供一组 Test Kitchen 插件，使系统能够使用 Test Kitchen 聚合 Terraform 配置并使用 InSpec 控件验证生成的 Terraform 状态。 ：头骨：
- [rspec-terraform](https://github.com/bsnape/rspec-terraform) - RSpec 测试您的 Terraform 模块。 ：头骨：
- [terraform_validate](https://github.com/elmundio87/terraform_validate) - 协助在 Terraform 中执行用户定义的标准。 ：头骨：
- [terraform-compliance](https://github.com/terraform-compliance/cli) - Terraform 文件的 BDD 测试。
- [terratest](https://github.com/gruntwork-io/terratest) - Terratest 是一个 Go 库，可以更轻松地为基础设施代码编写自动化测试。

## 工具

- [AIaC](https://github.com/gofireflyio/aiac) - 人工智能基础设施即代码生成器
- [AirIAM](https://github.com/bridgecrewio/AirIAM) - AirIAM 是 AWS IAM 最小化 Terraform 执行框架权限的工具。
- [asdf](https://github.com/asdf-community/asdf-hashicorp) - [asdf](https://github.com/asdf-vm/asdf) 版本管理器的 HashiCorp 插件
- [astro](https://github.com/uber/astro/) - Astro 是一个用于将多个 Terraform 执行作为单个命令进行管理的工具。 ：幽灵：
- [atlantis](https://github.com/runatlantis/atlantis) - 通过 GitHub 在 Terraform 上进行协作的统一工作流程。
- [atmos](https://github.com/cloudposse/atmos) - 一种通用工具，可将深度合并的 YAML 转换为模块输入。
- [aws2tf](https://github.com/aws-samples/aws2tf) - 自动将现有 AWS 资源导入 Terraform 并输出 Terraform HCL 代码。
- [aztfexport](https://github.com/Azure/aztfexport) - 一种将现有 Azure 资源置于 Terraform 管理之下的工具。
- [balcony](https://oguzhan-yilmaz.github.io/balcony/) - 用于轻松读取 AWS API 的 CLI 工具。还生成 Terraform 导入块和实际的 Terraform 资源代码。
- [blast radius](https://github.com/28mm/blast-radius) - Terraform 依赖图的交互式可视化。 ：头骨：
- [cf-terraforming](https://github.com/cloudflare/cf-terraforming) - 一个命令行实用程序，可帮助改造您现有的 Cloudflare 资源。
- [cfnctl](https://github.com/rogerwelin/cfnctl) - Cfnctl 将 Terraform cli 体验引入 AWS Cloudformation。
- [Checkov](https://github.com/bridgecrewio/checkov/) - Terraform静态分析工具，terraform>=0.12
- [cloud-audit](https://github.com/gebalamariusz/cloud-audit) - AWS 安全审核 CLI 具有修复引擎，可生成用于修复错误配置的 Terraform 代码。
- [Coder](https://coder.com/) - Coder 通过 Terraform 在您的基础设施上配置软件开发环境。
- [coretech/terrafile](https://github.com/coretech/terrafile) - 系统地管理来自 Github 的外部模块，以便在 Terraform（用 Go 编写）中使用。 ：头骨：
- [driftctl](https://github.com/snyk/driftctl) - 检测、跟踪基础设施漂移并发出警报 :skull:
- [drifthound](https://github.com/drifthoundhq/drifthound) - 通过历史跟踪和通知进行连续基础设施偏差检测。
- [dxw/terrafile](https://github.com/dxw/terrafile) - 系统地管理来自 Github 的外部模块，以便在 Terraform（用 Ruby 编写）中使用。
- [flora](https://github.com/ketchoop/flora) - Terraform 版本管理器。
- [fogg](https://github.com/chanzuckerberg/fogg) - 一种消除管理 terraform 存储库繁琐工作的工具。
- [former2](https://github.com/iann0036/former2) - 从您的 AWS 账户中的现有资源生成 terraform 配置。
- [fuzzy-terraform-rm](https://github.com/paololazzari/fuzzy-terraform-rm) - 一个模糊查找器命令行工具，用于从 terraform 状态中删除资源。
- [gaia](https://github.com/gaia-app/gaia) - Gaia 是一个用于您的模块的 Terraform 🌍 UI，以及自助服务基础设施 👨‍💻。 ：头骨：
- [hcl2json](https://github.com/tmccombs/hcl2json) - 将 hcl2 转换为 json。
- [hcldump](https://github.com/magodo/hcldump) - 转储 HCL (v2) 抽象语法树。
- [hcledit (mercari)](https://github.com/mercari/hcledit) - 去package编辑HCL配置
- [hcledit (minamijoyo)](https://github.com/minamijoyo/hcledit) - HCL 的命令行编辑器。
- [hclgrep](https://github.com/magodo/hclgrep) - HCL(v2) 的基于语法的 grep。
- [hq](https://github.com/miller-time/hq) - 命令行 HCL 处理器
- [iam-policy-json-to-terraform](https://github.com/flosell/iam-policy-json-to-terraform) - 用于将 JSON 格式的 IAM 策略转换为 Terraform aws_iam_policy_document 的小工具
- [Infracost](https://github.com/infracost/infracost) - CLI 和拉取请求中 Terraform 的云成本估算。
- [inframap](https://github.com/cycloidio/inframap) - 读取您的 tfstate 或 HCL 以生成特定于每个提供商的图表，仅显示最重要/相关的资源。
- [InfraScan](https://infrascan.soldevelo.com) - 高级基础设施审核器，用于 Terraform、AWS 和 Kubernetes 的成本和安全性分析。
- [InfraSketch](https://infrasketch.cloud) - 基于浏览器的免费工具，可将 Terraform HCL 和 Docker Compose 可视化为架构图。支持 AWS 和 Azure。无需注册，无需凭据。
- [json2hcl](https://github.com/kvz/json2hcl) - 将 JSON 转换为 HCL，反之亦然。 ：幽灵：
- [k2tf](https://github.com/sl1pm4t/k2tf) - Kubernetes YAML 到 Terraform HCL 转换器。
- [Kapitan](https://github.com/kapicorp/kapitan) - 从库存驱动模板生成 Terraform/OpenTofu JSON 和其他基础设施配置。
- [KICS](https://github.com/Checkmarx/kics) - 扫描 IaC 项目是否存在安全漏洞、合规性问题和基础设施配置错误。目前正在处理 Terraform 项目、Kubernetes 清单、Dockerfile、AWS CloudFormation 模板和 Ansible playbook。
- [layerform](https://github.com/briefercloud/layerform) - Layerform 帮助工程师使用纯 .tf 文件创建可重用的环境堆栈。非常适合多个“暂存”环境。 ：头骨：
- [library.tf](https://library.tf) - Library.tf 的构建和设计不仅可以为您提供 Terraform 和 OpenTofu 的所有注册表信息，还可以提供您做出决策所需的所有见解。快速找到受支持和维护且不存在错误的模块或提供程序。
- [modules.tf-lambda](https://github.com/antonbabenko/modules.tf-lambda) - 基础设施作为代码生成器，从使用 [Cloudcraft.co](https://cloudcraft.co) 创建的可视化图表到 Terraform。
- [para](https://github.com/paraterraform/para) - 缺少的第 3 方插件管理器和 Terraform/Terragrunt 的“瑞士军刀”——只是一个促进所有工作流程的工具。 ：头骨：
- [pike](https://github.com/jamesWoolfenden/pike) - Pike 计算构建 Terraform 所需的权限或 IAM 策略。
- [pipeform](https://github.com/magodo/pipeform) - Terraform 运行时 TUI
- [platform-skills](https://github.com/nitinjain999/platform-skills) - Terraform 的 AI 辅助现场手册：IAM 最小权限审查、爆炸半径分析、状态影响、提供商限制和回滚规划。作为 Claude、Codex、Cursor 和 Copilot 插件使用。
- [pluralith](https://www.pluralith.com/) - Terraform 状态可视化和基础设施文档的自动生成。 ：重美元符号：
- [pre-commit-terraform](https://github.com/antonbabenko/pre-commit-terraform) - Terraform 和 Terragrunt 的预提交 git hook：自动格式化、验证、更新文档、运行安全检查、估算成本等。
- [pretf](https://github.com/raymondbutcher/pretf) - 使用 Python 生成 Terraform 配置的嵌入式 Terraform 包装器。请参阅 [pretf 文档](https://pretf.readthedocs.io/en/latest/) :skull:
- [prettyplan for TF 0.12+](https://github.com/cloudandthings/terraform-pretty-plan) - Prettyplan for TF 0.12+（[可在此处在线获取](https://cloudandthings.github.io/terraform-pretty-plan/)）是一个小工具，可帮助您轻松查看大型 Terraform 计划。
- [prettyplan](https://github.com/chrislewisdev/prettyplan) - Prettyplan（[可在此处在线获取](https://chrislewisdev.github.io/prettyplan/)）是一个小工具，可帮助您轻松查看大型 Terraform 计划。 ：幽灵：
- [pug](https://github.com/leg100/pug) - terraform 高级用户的终端用户界面。
- [pytest-terraform](https://github.com/cloud-custodian/pytest-terraform) - pytest terraform 插件，具有固定装置和离线重播支持。
- [python-terrafile](https://github.com/claranet/python-terrafile) - 系统地管理来自 Github 的外部模块以在 Terraform 中使用。
- [regula](https://github.com/fugue/regula) - 在部署之前评估 Terraform 基础设施即代码是否存在潜在的 AWS、Azure 和 Google Cloud 安全配置错误和合规性违规行为。
- [redc](https://github.com/wgpsec/redc) - 基于Terraform构建的下一代红队基础设施自动化工具，支持多云部署（阿里云、腾讯云、AWS等），一键部署即可创建、配置和销毁红队环境。
- [renovate-config](https://github.com/SpotOnInc/renovate-config) - Renovatebot 的可共享配置预设，对于 DevOps 人员特别有用。
- [Riftmap](https://riftmap.dev) - 跨存储库依赖关系和变更影响引擎，可扫描 Terraform、Docker、Helm 等的多存储库基础设施，以可视化哪些内容依赖于哪些内容，以及当某些内容发生变化时哪些内容会中断。
- [rover](https://github.com/im2nguyen/rover) - 交互式 Terraform 状态和配置资源管理器。
- [ruby-terraform](https://github.com/infrablocks/ruby_terraform) - 用于调用 terraform 命令的简单 Ruby 包装器。
- [ReleaseRun Terraform Provider Matrix](https://releaserun.com/tools/terraform-checker/) - 免费浏览器工具，用于检查 Terraform 和 OpenTofu 版本之间的 Terraform 提供程序版本兼容性。
- [sato](https://github.com/JamesWoolfenden/sato) - Sato 帮助您将遗留的 Cloudformation 转换为 Terraform。
- [scenery](https://github.com/dmlittle/scenery) - 另一个 Terraform 计划输出美化器。 : 幽灵: : 骷髅:
- [scratchrelaxtv](https://github.com/YakDriver/scratchrelaxtv) - 帮助模块开发的简单 Python 工具 - 从“main.tf”中提取变量以生成“variables.tf”并从“variables.tf”创建模块使用存根。
- [serverless.tf - Doing serverless with Terraform](https://serverless.tf/) - serverless.tf 是一个固执己见的开源框架，用于使用 Terraform 在 AWS 上开发、构建、部署和保护无服务器应用程序和基础设施。 [阅读更多](https://github.com/antonbabenko/serverless.tf)。
- [ReleaseRun Terraform Security Scanner](https://releaserun.com/tools/terraform-security/) - 基于浏览器的免费“.tf”文件扫描仪。检查硬编码凭据、打开 0.0.0.0/0 端口、公共 S3/RDS、未加密存储、缺少删除保护。 A-F级。无需安装。
- [Shisho](https://github.com/flatt-security/shisho) - Terraform 的轻量级静态分析器。
- [Speakeasy](https://www.speakeasy.com/) - 根据 OpenAPI 规范生成 terraform 提供程序。
- [stacks](https://github.com/cisco-open/stacks) - Stacks，Terraform 代码预处理器
- [tads-boilerplate](https://github.com/Thomvaill/tads-boilerplate) - Ansible 和 Terraform 的强大功能 + Docker Swarm 的简单性 = 基础设施即代码和 DevOps 最佳实践。
- [tau](https://github.com/avinor/tau) - Tau 是 terraform 之上的一个薄包装器，用于管理多个部署、依赖项和机密。 ：头骨：
- [tenv](https://github.com/tofuutils/tenv) - OpenTofu/Terraform/Terragrunt 版本管理器。
- [terraboard](https://github.com/camptocamp/terraboard) - 用于检查 Terraform 状态的 Web 仪表板。
- [terraboot](https://github.com/MastodonC/terraboot) - DSL 用于生成 terraform 配置并运行它。
- [terracognita](https://github.com/cycloidio/terracognita) - 从现有云提供商读取（反向 Terraform）并在 Terraform 配置上生成基础设施即代码。
- [terracost](https://github.com/cycloidio/terracost) - CLI 中 Terraform 的云成本估算。
- [terracove](https://elementtech.github.io/terracove/) - 递归测试目录树的 Terraform 差异和覆盖范围。
- [TerraDepot](https://github.com/derBroBro/TerraDepot) - Terraform 状态存储库，基于默认的 http 远程后端。允许对 AWS S3 上的 tfstate 进行集中管理。
- [terradozer](https://github.com/chenrui333/terradozer) - Terraform 无需配置文件即可销毁。
- [terraeasy](https://github.com/jaceq/terraeasy) - 简单的 Terraform 包装器
- [terraform-ai-skills](https://github.com/anmolnagpal/terraform-ai-skills) - GitHub Copilot、Claude 和 ChatGPT 的人工智能技能可自动执行批量 Terraform 模块管理 — 提供程序升级、工作流程标准化，并在 AWS、GCP、Azure 和 DigitalOcean 上的 10-200 多个存储库中进行发布。
- [terraform-aws-clickops-notifier](https://github.com/cloudandthings/terraform-aws-clickops-notifier) - 在 AWS 控制台中采取操作时收到通知。
- [terraform-bundle](https://github.com/hashicorp/terraform/tree/main/tools/terraform-bundle) - 轻松构建包含 Terraform 二进制文件以及提供程序二进制文件的捆绑包。对于 CI 和气隙 Terraform Enterprise 很有用。
- [terraform-cdk](https://github.com/hashicorp/terraform-cdk) - Terraform 的 CDK（云开发工具包）允许开发人员使用熟悉的编程语言来定义云基础设施并通过 HashiCorp Terraform 进行配置。
- [terraform-cleaner](https://github.com/sylwit/terraform-cleaner) - 检测 terraform 模块中未使用变量的微型实用程序。
- [terraform-credentials-vault](https://github.com/oulman/terraform-credentials-vault) - Terraform“凭证助手”插件，允许通过环境变量为 Terraform 原生服务（私有模块注册表、Terraform Cloud 等）提供凭证。
- [terraform-diff](https://github.com/contentful-labs/terraform-diff) - 始终知道您需要在哪里运行 Terraform 计划并申请！
- [terraform-docs](https://github.com/terraform-docs/terraform-docs) - 从 terraform 模块生成文档的快速实用程序。
- [terraform-graph-beautifier](https://github.com/pcasteran/terraform-graph-beautifier) - 命令行工具允许将 terraform graph 命令几乎不可用的输出转换为更有意义和解释性的内容。
- [terraform-iam-policy-validator](https://github.com/awslabs/terraform-iam-policy-validator) - CLI 根据 AWS IAM 最佳实践验证 Terraform 模板中的 AWS IAM 策略。
- [terraform-landscape](https://github.com/coinbase/terraform-landscape) - *（仅 0.11 及更早版本）* 改进 Terraform 的计划输出，使其更易于阅读和理解。
- [terraform-operator](https://github.com/GalleyBytes/terraform-operator) - 用于处理 Terraform 操作的 Kubernetes CRD。
- [terraform-plan-parser](https://github.com/lifeomic/terraform-plan-parser) - 命令行实用程序和 JavaScript API，用于从“terraform plan”解析标准输出并将其转换为 JSON。 ：鬼：
- [terraform-provisioner](https://github.com/shuaibiyy/terraform-provisioner) - 用于管理相同 Terraform 脚本的多个规定的工具。
- [terraform-rake-tasks](https://github.com/gina-alaska/terraform-rake-tasks) - 用于管理 terraform 计划的共享 Rake 任务。
- [terraform-repl](https://github.com/paololazzari/terraform-repl) - terraform 控制台包装器，可提供更好的交互式控制台体验。
- [Terraform-Visual](https://github.com/hieven/terraform-visual) - 一个简单但功能强大的工具来可视化 Terraform 计划。
- [terravision](https://github.com/patrickchugh/terravision) - 使用官方 AWS/Azure/GCP 图标和设计标准从 Terraform 代码生成专业的云架构图。通过 CI/CD 集成运行 100% 客户端。
- [terraform.py](https://github.com/mantl/terraform.py) - 用于解析 Terraform 状态文件的 Ansible 动态清单脚本。 ：头骨：
- [terraformer](https://github.com/chenrui333/terraformer) - 用于从现有基础设施生成 terraform 文件的 CLI 工具。基础设施到代码。支持许多提供商。
- [terraforming](https://github.com/dtan4/terraforming) - 将现有 AWS 资源导出为 Terraform 样式（tf、tfstate）。类似于“地形改造者”。 ：头骨：
- [terraformize](https://github.com/naorlivne/terraformize) - 通过简单的 REST API 端点应用\销毁 Terraform 模块。 ：头骨：
- [terraformsh](https://github.com/pwillis-els/terraformsh) - Bash 中的包装器，用于更轻松的 CLI UX 和 DRY 分层配置
- [terragrunt-atlantis-config](https://github.com/transcend-io/terragrunt-atlantis-config) - 为 Terragrunt 项目生成 Atlantis 配置。
- [terragrunt](https://github.com/gruntwork-io/terragrunt) - Terragrunt 是 Terraform 的瘦包装器，它提供了额外的工具来保持 Terraform 配置干燥、使用多个 Terraform 模块以及管理远程状态。
- [terrahelp](https://github.com/opencredo/terrahelp) - 命令行实用程序旨在提供补充功能，这些功能有时在使用 Terraform 时很有用。
- [terrahub](https://github.com/tfxor/terrahub) - TerraHub 是 terraform 自动化和编排工具。无缝集成到 console.terrahub.io，这是一个企业友好型 GUI，可显示实时 terraform 执行情况，以及历史 terraform 运行的审核和报告功能。 ：重美元符号：
- [terramagic](https://github.com/miltlima/terramagic) - 用于自动创建文件夹和 terraform 文件的向导工具，用 Python 编写！
- [terramate](https://github.com/terramate-io/terramate) - 用于管理多个 Terraform 堆栈的工具，支持更改检测和代码生成
- [terrap-cli](https://github.com/sirrend/terrap-cli) - Terrap - 一个强大的 CLI 工具，可以扫描您的基础设施并识别任何所需的更改。
- [terrars](https://github.com/andrewbaxter/terrars) - Terrars 是一个用 Rust 构建 Terraform 堆栈的工具。这是 CDK 的替代方案。
- [terrascan](https://github.com/tenable/terrascan) - Terraform 模板静态代码分析的安全性和最佳实践测试集合
- [terrascope](https://github.com/spilliams/terrascope) - 为 terraform monorepos 构建协调器。
- [terrashine](https://isawan.github.io/terrashine/) - Terrashine 是一个 terraform 提供程序镜像 1 实现，它通过在请求提供程序时自动缓存依赖项来工作。
- [terraspace](https://terraspace.cloud) - Terraform 框架
- [terrastate](https://github.com/rohinivsenthil/terrastate) - Visual Studio Code 扩展用于监视/部署/销毁工作区中的 Terraform 资源
- [terratag](https://github.com/env0/terratag) - Terratag 是一个 CLI 工具，使 Terraform 用户能够在整个 AWS、Azure 和 GCP 资源集上自动创建和维护标签。
- [tf-init-booster](https://github.com/hayorov/terraform-init-booster) - 一个 Pre-terraform 例程，可加速大型蓝图的 terraform 模块下载。
- [tf-profile](https://github.com/datarootsio/tf-profile/) - Terraform 运行的探查器。生成全局统计数据、资源级统计数据或可视化。
- [tf-summarize](https://github.com/dineshba/tf-summarize) - 用于打印 terraform 计划摘要的命令行实用程序
- [tf-why](https://github.com/Raj-glitch-max/tf.why) - CLI 工具，通过 CloudTrail 查找将 Terraform 漂移归因于引起该漂移的 AWS 参与者。
- [tfaction](https://github.com/suzuki-shunsuke/tfaction) - 固执的 Terraform 工作流的 GitHub Actions 集合
- [tfautomv](https://github.com/busser/tfautomv) - 自动生成 Terraform“移动”块以进行无痛重构
- [tfcmt](https://github.com/suzuki-shunsuke/tfcmt) - CLI 用于通知计划结果并作为 Pull Request 评论进行应用。
- [tfedit](https://github.com/minamijoyo/tfedit) - Terraform 的重构工具。
- [tfenv](https://github.com/tfutils/tfenv) - Terraform 版本管理器受到 rbenv 的启发。
- [tfgen](https://github.com/0xDones/tfgen) - Terraform 代码生成器可实现一致的代码库和 DRY。
- [tfgpt](https://github.com/flavius-dinu/tfgpt) - 一个 CLI 工具，将 Terraform 与 OpenAI 的 GPT-3.5 Turbo 集成，为 Terraform 命令和概念提供解释。
- [tfimport](https://github.com/coolapso/tfimport) - 用于自动将现有基础设施导入 tfstate 的 CLI 工具。
- [tfjson](https://github.com/palantir/tfjson) - 用于读取 Terraform 计划文件并将其转储为 JSON 的实用程序。 ：头骨：
- [tfk8s](https://github.com/jrhouston/tfk8s) - 用于将 Kubernetes YAML 清单转换为 Terraform HCL 的工具
- [tflint](https://github.com/terraform-linters/tflint) - Terraform linter 用于检测“terraform plan”无法检测到的错误
- [tfmake](https://github.com/tfmake/tfmake) - 利用 make 的力量实现 Terraform 自动化。
- [tfmask](https://github.com/cloudposse-archives/tfmask) - Terraform 实用程序用于屏蔽“terraform plan”和“terraform apply”中的选择输出：skull：
- [tfmigrate](https://github.com/minamijoyo/tfmigrate) - 适用于 GitOps 的 Terraform 状态迁移工具。
- [tfmigrator](https://github.com/tfmigrator/cli) - Go 库和 CLI 迁移 Terraform 配置和状态
- [tfmv](https://github.com/suzuki-shunsuke/tfmv) - 重命名 Terraform 资源并生成移动块
- [tfocus](https://github.com/nwiizo/tfocus) - tfocus 是一个超级交互式工具，用于在特定资源上选择和执行 Terraform 计划/应用。将其视为“应急工具” - 不适合日常使用。
- [tfprovidercheck](https://github.com/suzuki-shunsuke/tfprovidercheck) - 用于防止执行恶意 Terraform Provider 的 CLI
- [tfproviderlint](https://github.com/bflad/tfproviderlint) - Terraform Provider Lint 工具。
- [tfrepl](https://github.com/ysoftwareab/tfrepl) - Terraform REPL，为您提供完整的 shell 体验。基于Readline。没有依赖性。保存配置更改。历史。
- [tfreveal](https://github.com/breml/tfreveal) - 一个 Terraform 实用程序，用于显示 Terraform 计划，并显示所有秘密（敏感）值。
- [tfscaffold](https://github.com/tfutils/tfscaffold) - 用于控制多环境多组件 terraform 管理的 AWS 基础设施的框架。
- [tfschema](https://github.com/minamijoyo/tfschema) - Terraform 提供者的架构检查器。
- [tfsec](https://github.com/aquasecurity/tfsec) - Terraform 静态分析工具，支持 terraform <0.12 & >=0.12 并直接与 HCL 解析器集成以获得更好的结果。
- [tfsort](https://github.com/AlexNabokikh/tfsort) - 用于对 Terraform 变量和输出进行排序的 CLI 实用程序。
- [tftarget](https://github.com/future-architect/tftarget) - 用于交互执行 `terraform xxx -target={...}` 的 CLI 工具。
- [tftree](https://github.com/busser/tftree) - 在终端中显示 Terraform 模块调用堆栈。
- [tftui](https://github.com/idoavrah/terraform-tui) - Terraform 状态的文本用户界面。
- [tfupdate](https://github.com/minamijoyo/tfupdate) - 更新 Terraform 配置中的版本约束。
- [tfvar](https://github.com/shihanng/tfvar) - tfvar 扫描您的 Terraform 配置或模块，并将变量提取为您选择的格式（tfvar、环境变量等）以进行编辑。
- [tfvaultenv](https://github.com/oulman/tfvaultenv) - tfvaultenv 从 HashiCorp Vault 读取机密，并使用这些机密输出各种 Terraform 提供程序的环境变量。
- [tfwrapper](https://github.com/manheim/tfwrapper) - Rubygem 提供 rake 任务来正常运行 Hashicorp Terraform。
- [tfmcp](https://github.com/nwiizo/tfmcp) - 一个 CLI 工具，可帮助您通过模型上下文协议 (MCP) 与 Terraform 交互，从而允许 Claude 等 AI 助手管理和操作 Terraform 环境。
- [tgf](https://github.com/coveooss/tgf) - Terragrunt 前端，用于通过 Docker 执行 Terragrunt/Terraform。
- [threatcl](https://github.com/threatcl/threatcl) - 使用 HCL 记录您的威胁模型
- [tofuenv](https://github.com/tofuutils/tofuenv) - OpenTofu 版本管理器受 tfenv 启发
- [tpm](https://github.com/Madh93/tpm) - Terraform 提供程序的包管理器。
- [travelgrunt](https://github.com/ivanilves/travelgrunt) - cd [mono]repos 内无疲劳！
- [trupositive](https://github.com/trupositive-ai/trupositive) - 零配置包装器，自动将 Git 元数据（提交 SHA、分支、存储库）注入到所有 Terraform 管理的资源中。
- [validIaC](https://github.com/gofireflyio/validiac) - ValidIaC 结合了最好的开源工具，帮助确保 Terraform 最佳实践、卫生和安全。
- [xterrafile](https://github.com/devopsmakers/xterrafile) - 从模块注册表、git 或本地目录系统地管理外部模块，以便在 Terraform（用 Go 编写）中使用。 ：头骨：
- [yj](https://github.com/sclevine/yj) - CLI - 在 YAML、TOML、JSON 和 HCL 之间转换。保留地图顺序。
- [yor](https://github.com/bridgecrewio/yor) - 自动标记和跟踪基础设施作为代码框架（Terraform、Cloudformation 和 Serverless）。
- [zephy](https://github.com/henrybravo/zephy) - *当您的云资源标记策略不足时*，将订阅中部署的 Azure 资源与 Terraform Enterprise（HCP 和自托管）工作区管理的资源进行比较。

### CI

- [setup-terraform](https://github.com/hashicorp/setup-terraform) - 在 GitHub Actions 工作流程中设置 Terraform CLI。
- [terraform-plan](https://github.com/cds-snc/terraform-plan) - GitHub Action 用于运行 Terraform 计划并添加包含更改的注释。
- [terraform-risk-assessor](https://github.com/Liam-Johnston/terraform-risk-assessor) - GitHub Action，使用 AI 分析 Terraform 计划更改并评论拉取请求的风险评估。

### VS 代码扩展

- [HashiCorp 地形](https://marketplace.visualstudio.com/items?itemName=hashicorp.terraform)
- [vscode-terraform-live-graph](https://github.com/adamiBs/vscode-terraform-live-graph) - 适用于 Visual Studio Code 的 Terraform Live Graph Extension 是一个插件，可让您在编码时生成实时 Terraform 图表。
- [tf-nav](https://marketplace.visualstudio.com/items?itemName=owenrumney.tf-nav) - Terraform 导航扩展可通过易于导航的树视图按文件类型创建资源索引。

## 图书馆

- [hcl-rs](https://github.com/martinohmann/hcl-rs) - 用于 Rust 的 HCL 解析和编码库，支持 serde
- [hcl4j](https://github.com/wondrify/hcl4j) - Java 中的 HCL 解析器
- [nu_plugin_hcl](https://github.com/Yethal/nu_plugin_hcl) - [Nushell](https://github.com/nushell/nushell) 的 HCL 解析器插件
- [pyhcl](https://github.com/virtuald/pyhcl) - Python 中的 HCL 解析器
- [python-hcl2](https://github.com/amplify-education/python-hcl2/) - Python 中的 HCL2 解析器
- [rhcl](https://github.com/winebarrel/rhcl) - 纯 Ruby HCL 解析器 :skull:
- [tree-sitter-hcl](https://github.com/tree-sitter-grammars/tree-sitter-hcl) - 树守护者的 HCL 语法

## 样板文件

- [Solo-Engineer Stack](https://github.com/sarmakska/terraform-stack) - 单个 Terraform 存储库将 Vercel + Supabase + Cloudflare + DigitalOcean 连接为独立 SaaS 平台。其中一个“terraform apply”提供了一个 Next.js 项目、一个环境变量通过管道传输到 Vercel 的 Supabase 项目、一个带有 R2 和 Workers KV 的 Cloudflare 区域，以及一个具有监控功能的 DigitalOcean Droplet。
- [Terraform Generator](https://github.com/sudokar/generator-tf-module) - 在测试框架（terratest 和 kitchen-terraform）支持下为新的 terraform 模块或项目搭建脚手架
- [Terraform GitOps Framework](https://www.kubestack.com) - 在一个免费开源框架中为 AKS、EKS 和 GKE Kubernetes 集群构建可靠的自动化所需的一切。

## 自托管 Terraform 平台

- [Lynx](https://github.com/clivern/lynx) - 快速、安全且可靠的 Terraform 后端。它具有用户友好的仪表板、项目和环境管理、状态版本控制、锁定和快照支持。
- [OTF](https://github.com/leg100/otf) - 开放 Terraforming Framework，这是 Terraform Enterprise 的开源替代方案，具有完整的 Terraform CLI 集成。
- [Terrakube](https://docs.terrakube.io) - Terraform Enterprise 的开源替代品，具有私有注册表、远程状态、自定义流程、计划工作区和视觉状态。
- [Digger](https://digger.dev) - Terraform Cloud 的开源替代方案 - 运行 Terraform 计划并在 CI 中应用作业。
- [cloud-concierge](https://github.com/dragondrop-cloud/cloud-concierge) - 开源，将非托管资源编码为 Terraform、检测偏差以及云成本和安全分析，以 Pull 请求形式交付。
- [Stack-Lifecycle-Deployment](https://github.com/D10S0VSkY-OSS/Stack-Lifecycle-Deployment) - 开源解决方案，定义和管理在云中使用和配置的资源的完整生命周期。
- [Burrito](https://github.com/padok-team/burrito) - TACoS Kubernetes Operator - “ArgoCD for Terraform”
- [Terrateam](https://terrateam.io) - Terraform Cloud/Enterprise 的开源替代方案，GitOps 优先，具有本机 GitHub 集成，专为规模、安全性和可靠性而设计。


## 托管 Terraform 平台：heavy_dollar_sign：

- [compliance.tf](https://compliance.tf) - Terraform 模块内置 SOC 2、PCI DSS、HIPAA、NIST 800-53 和 35 多个其他框架。不合规的配置在任何应用之前都会在“terraform plan”中失败。 ：重美元符号：
- [ControlMonkey](https://www.controlmonkey.io/) - 具有 Terraform/OpenTofu 代码生成、云库存和 IaC 覆盖范围的 Terraform Cloud 替代方案。包括开箱即用的策略、偏差修复和 ClickOps 活动扫描器。 ：重美元符号：
- [Firefly](https://www.firefly.ai/) - 利用 CI 工具替代 Terraform Cloud。 Firefly 平台还会扫描您的云以评估 IaC 覆盖范围和漂移检测。 ：重美元符号：
- [Scalr](https://www.scalr.com/) - Terraform Enterprise 的替代方案，具有 OPA 集成、组织结构、自定义挂钩、与其他 DevOps 平台的本机集成以及集中报告。 ：重美元符号：
- [Stategraph](https://stategraph.com) - Terraform 和 OpenTofu 没有状态文件瓶颈。用真实的数据库替换平面状态文件。团队并行计划，状态可通过 SQL 查询，并且计划在几秒钟而不是几分钟内运行。 ：重美元符号：
- [env0](https://www.env0.com/) - 具有 OPA 集成、自定义流程和 Terragrunt 支持的 Terraform Cloud/Enterprise 替代方案：heavy_dollar_sign：
- [Brainboard](https://www.brainboard.co) - 从任何云提供商（AWS、GCP、Azure）开始，以可视化方式设计、部署和管理现代云基础设施：heavy_dollar_sign：
- [Spacelift](https://spacelift.io/) - Terraform 云/企业的替代方案。 Terraform 协作基础设施交付平台：heavy_dollar_sign：
- [StackGuardian](https://stackguardian.io/) - 基础设施编码和编排平台，可将现有云资源转换为 IaC，具有 Tirith、OPA 和 Checkov 的策略驱动工作流程，并支持私有运行时和无代码模板。 ：重美元符号：

## Terraform 企业工具

- [terraform-enterprise-cli](https://github.com/skierkowski/terraform-enterprise-cli) - Terraform Enterprise 命令行界面。
- [terraform-enterprise-client](https://github.com/skierkowski/terraform-enterprise-client) - Terraform Enterprise API Ruby 客户端和命令行工具。
- [terraform-enterprise-migrator](https://github.com/sil-org/tfc-ops) - 用于将 Terraform Enterprise 环境从旧版本迁移到新版本 Terraform Enterprise 的脚本。

## 视频

- [Your Weekly Dose of Terraform](https://www.youtube.com/channel/UCGH0yYPvlCN1VjSFMGVmFgQ) - YouTube 频道，每周进行直播，内容涵盖 Terraform 新闻、评论、采访、问答、实时编码以及一些 Terraform 黑客攻击。
- [Terraform explained in 15 mins](https://www.youtube.com/watch?v=l5k1ai_GBDE) - Terraform 在 15 分钟内进行了解释。
- [Terraform Course](https://www.youtube.com/watch?v=SLB_c_ayRMo) - 自动化您的 AWS 云基础设施。
- [How to Build Reusable, Composable, Battle tested Terraform Modules](https://www.youtube.com/watch?v=LVgP63BkhKQ) - Yevgeniy Brikman 谈论如何编写 Terraform 代码，使其可重用、可组合和可测试。该演示文稿重点介绍了 Terraform 模块，但还简要清晰地解释了创建 Terraform 是为了解决什么问题，以及 Terraform 基础知识的简短演示（约 39 分钟，2017 年 10 月）。
- [Building Scalable, Repeatable Infrastructure in the Cloud with Terraform](https://www.youtube.com/watch?v=cG7pcksTAnY) - 演示 Terraform 如何通过使用托管 PostgreSQL 在 AWS 中部署 TeamCity 来实现基础设施即代码实践。
- [Creating a Google Compute Instance with Terraform](https://www.youtube.com/watch?v=fo3VX33Zx0c) - 使用 Terraform 代码创建 Google 计算实例的示例。
- [Creating a Terraform Provider for Just About Anything](https://www.hashicorp.com/resources/creating-terraform-provider-for-anything) - 通过本演练了解如何为 Terraform 提供程序做出贡献或创建您自己的提供程序。
- [Evolving Your Infrastructure with Terraform](https://www.youtube.com/watch?v=wgzgVm7Sqlk) - OpenCredo 的 CTO 在一些有趣的用例的帮助下，广泛介绍了如何在现实世界中使用 Terraform。
- [使用 Terraform 和 Nomad 实现多云](https://www.youtube.com/watch?v=e42A4aBZUkQ)。
- [How to Extend the Terraform Provider List](https://www.youtube.com/watch?v=2BvpqmFpchI) - 在本次演讲中，Paul 将逐步介绍 terraform 提供程序的创建过程。
- [Orchestrating Containers with Terraform and Consul](https://www.infoq.com/presentations/terraform-consul/) - Mitchell Hashimoto 展示了如何使用 Terraform 来部署和扩展容器化工作负载。
- [Production ChaosMonkey with Terraform](https://www.youtube.com/watch?v=CPI6W3LK0-g) - DigitalOcean 如何使用 Terraform 运行生产集成测试。
- [Running a Terraform Environment at Scale](https://www.youtube.com/watch?v=3JVGSq7QIS0) - 使用数百个 AWS 账户大规模运行 Terraform。
- [Setup Continuous Integration for a Terraform module](https://www.youtube.com/watch?v=vuJ6bjYKUcA) - 使用 CI 和 Kitchen-Terraform 来测试、标记和发布我们的 Terraform 模块的示例，该模块创建了一个 Google 计算实例。
- [State of Terraform Providerland](https://www.youtube.com/watch?v=ar1PF5iDtbg) - Terraform 提供程序如何工作以及如何编写。
- [Terraform At Scale](https://www.youtube.com/watch?v=RldRDryLiXs) - Segment 如何使用 Terraform。
- [Terraform w/ Lee Trout](https://www.youtube.com/watch?v=p2ESyuqPw1A) - 重点关注开发模式以及如何有效构建 Terraform 代码。
- [Terraforming the Composable World](https://www.youtube.com/watch?v=cHrOXPatFeg) - 将 Terraform 与本地裸机配置集成。
- [Test and verify a Google Compute Instance with Kitchen-Terraform](https://www.youtube.com/watch?v=kiH3-LEveek) - 使用 Kitchen-Terraform 测试创建 Google Compute 的 Terraform 代码的示例。
- [Untangling Terraform Through Refactoring](https://www.youtube.com/watch?v=OH6iDKaXpZs) - 如何以最小的风险谨慎地重构 Terraform 代码。
- [Complete Terraform Course - From BEGINNER to PRO! (Learn Infrastructure as Code)](https://www.youtube.com/watch?v=7xngnjfIlK4) - 从初学者到专业人士的完整课程，不关注云提供商，采用通用方法

## 编辑器插件

- [Emacs terraform 模式](https://github.com/hcl-emacs/terraform-mode)
- [Intellij](https://plugins.jetbrains.com/plugin/7808-terraform-and-hcl)
- [Terraform-ls](https://github.com/hashicorp/terraform-ls)（Terraform 语言服务器）
- [Terraform-lsp](https://github.com/juliosueiras/terraform-lsp)（Terraform 的语言服务器协议）
- [vim-hcl](https://github.com/jvirtanen/vim-hcl) - HCL 的语法突出显示
- [Vim-Terraform-Completion](https://github.com/juliosueiras/vim-terraform-completion)
- [Vim-Terraform](https://github.com/hashivim/vim-terraform)

## 许可证

[![CC0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

在法律允许的范围内，Shuaib Yunus 放弃了本作品的所有版权以及相关或邻接权。
