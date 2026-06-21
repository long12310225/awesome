# 很棒的 CDK [<img src="https://raw.githubusercontent.com/aws/aws-cdk/master/logo/default-128-dark.png"align="right" alt="CDK">](https://github.com/aws/aws-cdk) [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> 精彩的 [AWS 云开发套件](https://github.com/awslabs/aws-cdk) (AWS CDK) 开源项目、指南、博客和其他资源的精选列表。

AWS 云开发套件 (AWS CDK) 是一个开源软件开发框架，用于在代码中定义云基础设施。

## 内容

* [构建库](#construct-libraries)
  * [APIs](#apis)
  * [Databases](#databases)
  * [静态网站](#static-websites)
  * [Security](#security)
  * [Ops](#ops)
  * [Queue](#queue)
  * [CI/CD](#cicd)
  * [Monitoring](#monitoring)
  * [Workflows](#workflows)
  * [多账户设置](#multi-accounts-setup)
* [高级框架](#high-level-frameworks)
* [Scaffolding](#scaffolding)
* [语言支持](#language-support)
* [图书馆出版](#library-publishing)
* [Tools](#tools)
* [培训材料和示例代码](#training-materials-and-sample-code)
* [博客文章和演讲](#blog-posts--talks)
* [相关项目](#related-projects)
* [提示与技巧](#tips--tricks)

## 构建库

本节包括各种编程语言的代码库，这些代码库提供可在 CDK 应用程序中使用的构造。

### API

* [cdk-chalice](https://github.com/alexpulver/cdk-chalice) - AWS Chalice 的 AWS CDK 构造（适用于 AWS 的 Python 无服务器微框架）。
* [auto-cdk](https://github.com/wulfmann/auto-cdk) - 自动生成 api-gateway/lambda 与文件系统的集成（测试版）。
* [crow-api](https://github.com/thomasstep/crow-api) - 根据您的文件结构创建带有路由的无服务器 API。

### 数据库

* [aws-cdk-dynamodb-seeder](https://github.com/elegantdevelopment/aws-cdk-dynamodb-seeder) - DynamoDB 的简单 CDK 播种器。
* [cdk-tweet-sentiment](https://www.npmjs.com/package/cdk-tweet-sentiment) - 识别推文中的情绪并将其记录到 Amazon DynamoDB 表中。
* [cdk-dynamo-table-viewer](https://github.com/eladb/cdk-dynamo-table-viewer) - 通过公共 HTML 页面公开 Amazon DynamoDB 表的内容。
* [cdk-postgresql](https://github.com/botpress/cdk-postgresql) - 适用于 PostgreSQL 的 AWS CDK 构造。
* [cdk-sqlserver-seeder](https://github.com/kolomied/cdk-sqlserver-seeder) - 针对 SQL Server 数据库执行自定义 SQL 脚本的 CDK 构造。

### 静态网站

* [cdk-static-website](https://github.com/cloudcomponents/cdk-components/blob/master/packages/cdk-static-website) - CDK 组件使用 S3 创建静态网站、配置 CloudFront (CDN) 并通过 Route53 (DNS) 映射自定义域。
* [ness](https://github.com/nessjs/ness) - CDK 支持的 CLI 工具，用于将静态站点部署到您的 AWS 账户。

### 安全性

* [cdk-passwordless](https://github.com/farminf/aws-cdk-passwordless) - 构建使用用户池进行无密码身份验证。
* [cdk-iam-generator](https://github.com/srihariph/cdk-iam-generator) - 构建以使用 JSON 配置生成 IAM 托管策略和 IAM 角色。
* [c3](https://github.com/SSHcom/c3) - 能够遵守隐私和安全最佳实践。
* [cdk-iam-floyd](https://github.com/udondan/iam-floyd) - 具有流畅界面的 IAM 策略语句生成器。
* [k9-cdk](https://github.com/k9securityio/k9-cdk) - 构建轻松生成安全的 S3 存储桶策略。
* [cdk-cloudfront-authorization](https://github.com/cloudcomponents/cdk-constructs/tree/master/packages/cdk-cloudfront-authorization) - 使用 Lambda@Edge 进行 Cognito 身份验证的 CloudFront。
* [aws-firewall-factory](https://github.com/globaldatanet/aws-firewall-factory) - 部署、更新和暂存您的 WAF，同时通过 FMS 集中管理它们。
### 行动

* [cdk-instanceStopRule](https://github.com/tecracer/cdk-constructs/tree/master/packages/cdk-instanceStopRule) - CDK 组件创建一个带有 CloudWatch 规则的实例，以在一天结束时停止它。
* [cdk-time-bomb](https://github.com/jmb12686/cdk-time-bomb) - CDK 构造会在设定的时间后内爆您的 AWS CDK 堆栈。

### 队列

* [cdk-tweet-queue](https://www.npmjs.com/package/cdk-tweet-queue) - 使用来自 tweeter 搜索查询的推文填充 SQS 队列。
* [cdk-ses-template-mailer](https://github.com/mkrn/cdk-ses-template-mailer) - 构建创建 AWS SES 电子邮件模板 + 微服务以使用 AWS SES 发送模板化电子邮件。
* [cdk-sqs-monitored](https://github.com/kamilbiela/cdk-sqs-monitored) - SQS 构造有死信队列和配置的警报。

### 持续集成/持续交付

* [aws-delivlib](https://github.com/awslabs/aws-delivlib) - 综合用于多语言软件交付的 CI/CD 管道（由 CDK 本身使用）。
* [cdk-blue-green-container-deployment](https://github.com/cloudcomponents/cdk-constructs/tree/master/packages/cdk-blue-green-container-deployment) - 使用 CodeDeploy 进行蓝/绿容器部署。

### 监控

* [cdk-watchful](https://github.com/eladb/cdk-watchful) - CDK 应用程序的自动仪表板和警报。
* [aws-cdk-billing-alarm](https://github.com/alvyn279/aws-cdk-billing-alarm) - 构建为超出 AWS 账单上的金额设置电子邮件警报的结构。
* [cdk-monitoring-constructs](https://github.com/cdklabs/cdk-monitoring-constructs) - 使用高级 API 为您的 AWS 应用程序创建监控。自动生成仪表板。

### 工作流程

* [cdk-pull-request-check](https://github.com/cloudcomponents/cdk-components/blob/master/packages/cdk-pull-request-check) - 自动检查拉取请求的 CDK 组件。
* [cdk-github-webhook](https://github.com/cloudcomponents/cdk-components/blob/master/packages/cdk-github-webhook) - 提供 GitHub webhook 的 CDK 组件。
* [cdk-codepipeline-slack](https://github.com/cloudcomponents/cdk-components/blob/master/packages/cdk-codepipeline-slack) - 提供 #slack 审批工作流程的 CDK 组件。
* [cdk-codecommit-backup](https://github.com/cloudcomponents/cdk-components/tree/master/packages/cdk-codecommit-backup) - 将 CodeCommit 存储库备份到 S3。
* [Alexa Deployment Pipeline](https://github.com/taimos/cdk-constructs/tree/master/lib/alexa) - 构造它创建一个 CodePipeline，以使用 AWS SAM 和 DeployToAlexa 操作将 Alexa Skills 部署到 Lambda 和开发人员控制台。
* [cdk-developer-tools-notifications](https://github.com/cloudcomponents/cdk-constructs/tree/master/packages/cdk-developer-tools-notifications) - Slack / Microsoft Teams / 开发人员工具的电子邮件通知：CodeCommit、CodeBuild、CodeDeploy、CodePipeline。
* [aws-pdf-textract-pipeline](https://github.com/aeksco/aws-pdf-textract-pipeline) - ETL 管道，用于使用 Puppeteer 从 Web 抓取 PDF，使用 AWS Textract 将其内容转换为结构化数据，并将结果存储在 DynamoDB 中。

### 多账户设置
* [aws-bootstrap-kit](https://github.com/awslabs/aws-bootstrap-kit) - 使用 AWS Organization、AWS SSO、DNS 和 AWS CodePipeline 创建多账户设置。
* [cdk-organizations](https://github.com/pepperize/cdk-organizations) - CDK 构造有助于配置 AWS 组织、组织单位 (OU)、账户和策略。

## 高级框架

* [punchcard](https://github.com/punchcard/punchcard) - TypeScript 框架用于统一 CDK 的基础架构和运行时代码，因此您可以在一个 Node.js 应用程序的上下文中声明构造并实现运行时逻辑。
* [aws-cdk-pure](https://github.com/fogfish/aws-cdk-pure) - 一个使用 AWS CDK 开发纯功能性高阶云组件的工具包。
* [cdk-stepfunctions-patterns](https://github.com/kolomied/cdk-stepfunctions-patterns) - 一组 Step Functions 高级弹性模式。
* [Orkestra](https://github.com/knowsuchagency/orkestra) - 基于 AWS CDK 和 Step Functions 构建的事件驱动型 Airflow 替代方案。
* [SST](https://github.com/serverless-stack/serverless-stack) - 用于使用 CDK 构建无服务器应用程序的开源框架。它具有实时 Lambda 开发环境，可以在本地测试和调试 Lambda 函数，而无需重新部署它们。
* [Datajob](https://github.com/vincentclaes/datajob) - 在 AWS 上轻松构建和部署无服务器数据管道或机器学习管道。

## 脚手架

* [ReactJS + Cognito + CDK Starter](https://github.com/vbudilov/reactjs-cognito-starter) - ReactJS + Amazon Cognito + Amazon Amplify Framework 的入门项目，支持 AWS CDK。
* [cra-template-aws-cdk](https://github.com/luisfarzati/rnbw-aws-cdk/tree/master/packages/cra-template-aws-cdk) - 使用 AWS CDK 创建 React 应用程序模板，以开箱即用、简单地配置无服务器 React 应用程序。
* [create-cdk-app](https://github.com/cdk-tools/create-cdk-app) - 从模板创建 CDK 应用程序。
* [awscdk-jsii-template](https://github.com/pahud/awscdk-jsii-template) - GitHub 模板存储库，用于生成用于构建、测试和发布 AWS CDK 的 [JSII]((https://github.com/aws/jsii)) 构建库的就绪环境。

## 语言支持

* [AWS-CDK-Kotlin-DSL](https://github.com/justincase-jp/AWS-CDK-Kotlin-DSL) - [AWS CDK Java](https://mvnrepository.com/artifact/software.amazon.awscdk) 的包装器库。 CI每天自动生成代码并部署。
* [aws-cdk-maven-plugin](https://github.com/LinguaRobot/aws-cdk-maven-plugin) - 用于使用 Java 和 Maven 定义和部署 AWS CDK 应用程序的插件。
* [aws-lambda-nodejs-webpack](https://github.com/vvo/aws-lambda-nodejs-webpack) - 替代 Node.js lambda CDK 构造，使用 [webpack](https://webpack.js.org/)。
* [aws-lambda-nodejs-esbuild](https://github.com/floydspace/aws-lambda-nodejs-esbuild) - 替代 Node.js lambda CDK 构造，使用 [esbuild](https://github.com/evanw/esbuild)。

## 图书馆出版

* [GitHub Action](https://github.com/marketplace/actions/aws-cdk-action) - AWS CDK 的 GitHub 操作。
* [jsii-publish](https://github.com/udondan/jsii-publish) - [Docker 镜像](https://hub.docker.com/r/udondan/jsii-publish) 和 [GitHub 操作](https://github.com/marketplace/actions/jsii-publish)，用于构建和发布通过 [JSII](https://github.com/aws/jsii) 创建的 CDK 构造。

## 工具

* [CDK-Dia](https://github.com/pistazie/cdk-dia) - AWS CDK 的自动基础架构图。

## 培训材料和示例代码

* [Official CDK Examples](https://github.com/aws-samples/aws-cdk-examples) - AWS CDK 的一组示例项目。
* [CDK Serverless Workshop](https://cdkworkshop.com/) - 研讨会将指导您完成创建和部署 CDK 应用程序的过程。
* [Egghead.io 上的使用 AWS 云开发套件构建应用程序课程](https://egghead.io/courses/build-an-app-with-the-aws-cloud-development-kit?af=6p5abz)
* [Infrastructure is Code with the AWS CDK](https://youtu.be/Lh-kVC2r2AU) - re:Invent 2018 会议录音。
* [GitHub Changelog Crawler](https://github.com/aws-samples/aws-cdk-changelogs-demo) - 由 Nathan Peck 编写的成熟 CDK 应用程序，使用 Fargate、API Gateway、Lambda、CloudFront、S3、ElastiCache 和 Dynamodb。
* [ECS with CI/CD](https://github.com/rix0rrr/cdk-ecs-demo) - 使用CDK部署ECS应用程序的演示。
* [Example templates for aws cdk](https://github.com/tecracer/cdk-templates) - 来自多个 AWS 项目的工作 TypeScript 片段。
* [Lambda packaging asset](https://gitlab.com/josef.stach/aws-cdk-lambda-asset) - CDK 资产构建 lambda 函数并生成具有依赖项的 ZIP 文件。
* [Open CDK Guide](https://github.com/kevinslin/open-cdk) - CDK 开源指南和最佳实践。
* [Colorteller Example](https://github.com/denmat/colorteller-aws-cdk) - 使用 Fargate 和 Appmesh 的绝佳示例项目。
* [CDK Patterns](https://github.com/cdk-patterns/serverless) - 使用 CDK 构建的无服务器架构模式的开源集合。
* [Create a CI/CD pipeline using CodePipeline and CodeBuild](https://sbstjn.com/deploy-react-cra-with-cdk-codepipeline-and-codebuild.html) - GitHub 上的 [cra-pipeline](https://github.com/sbstjn/cra-pipeline) 项目展示了使用 AWS CodeBuild 部署静态 React 应用程序的 AWS CodePipeline。
* [React SPA with server-side rendering on AWS Lambda](https://sbstjn.com/serverless-create-react-app-server-side-rendering-ssr-lamda.html) - [cra-serverless](https://github.com/sbstjn/cra-serverless) 项目是一个无服务器架构，用于向使用 [create-react-app](https://create-react-app.dev) 创建的 React 网站添加预渲染。
* [Mini Tutorial: Setup AWS Lambda + ACM + API Gateway with AWS Cloud Development Kit](https://github.com/shaftoe/api-gateway-lambda-cdk-example) - 部署一个功能性公共 API，用于接收 HTML 表单（例如 /contact_us.html）POST 请求并将其数据传递到 Pushover 通知服务。
* [Example of REST API built with CDK](https://github.com/shaftoe/api-l3x-in) - 支持 REST API 的源代码位于 https://api.l3x.in/。
* [dilbert-feed](https://github.com/mlafeldt/dilbert-feed) - 一个用 Go 编写的无服务器应用程序，让您可以在 RSS 提要阅读器中享受 Dilbert，而无需任何广告。
* [django-postgres-vue-gitlab-ecs](https://gitlab.com/verbose-equals-true/django-postgres-vue-gitlab-ecs) - 使用 GitLab CI 通过 CDK 部署的示例 Django + Vue.js Web 应用程序。
* [nextjs-vercel-aws-cdk-example](https://github.com/vvo/nextjs-vercel-aws-cdk-example) - PostgreSQL (RDS)、EventBridge (crons) 和 SNS（后台作业）示例以及 Next.js 应用程序。
* [Create and Publish CDK Constructs Using projen and jsii](https://github.com/seeebiii/projen-test) - 包含示例代码的分步指南，用于使用 [projen](https://github.com/projen/projen) 和 `jsii` 创建新的 CDK 构造并将其发布到 npm、Maven Central、PyPi 和 NuGet。

## 博客文章和演讲

* [Introduction to how and why CDK](https://www.slideshare.net/ranguard/aws-cdk-introduction-191140240) - 作者：利奥·拉普沃斯。
* [How to Build a CDK Construct Library](https://garbe.io/blog/2019/03/26/construct-your-own-cdk-construct-library/) - 作者：菲利普·加布。
* [CDK All The Things: A Whirlwind Tour](https://kevinslin.com/aws/cdk_all_the_things/) - 作者：凯文·S·林
* [AWS CDK Developer Preview Announcement](https://aws.amazon.com/blogs/developer/aws-cdk-developer-preview/) - 首个 AWS CDK 开发者预览版于 2018 年 8 月 27 日发布。
* [Contributing to the AWS Cloud Development Kit](https://aws.amazon.com/blogs/developer/contributing-to-the-aws-cloud-development-kit/) - 作者：来自 Intuit 的 Mike Cowgill。
* [First look into AWS Cloud Development Kit](https://garbe.io/blog/2018/08/17/first-look-into-cdk/) - 作者：菲利普·加布。
* [Boost your AWS Infrastructure with the CDK](https://www.slideshare.net/philippgarbe/boost-your-aws-infrastructure-with-cdk) - Philipp Garbe 的 SlideShare。
* [Getting started with AWS CDK for Amazon ECS](https://aws.amazon.com/blogs/compute/getting-started-with-the-aws-cloud-development-kit-for-amazon-ecs/) - 作者：内森·佩克。
* [AWS re:Invent 2018, best of show: CDK](https://medium.com/allermedia-techblog/aws-re-invent-2018-best-of-show-cloud-development-kit-cdk-ad1755561ade) - Aller 媒体技术博客。
* [AWS Cloud Development Kit introduction with Live Demos](https://youtu.be/IIiIoMGTJec) - AWS 用户组芬兰聚会，2019 年 1 月。
* [AWS CDK — a glimpse into the future](https://medium.com/nordcloud-engineering/aws-cdk-a-glimpse-into-the-future-90db660f8a89) - 由 Nordcloud 工程公司提供。
* [AWS Infrastructure as Code with CDK](https://medium.com/avmconsulting-blog/aws-infrastructure-as-code-with-cdk-1d6fa013ce7d) - 作者：罗斯·罗兹。
* [Callbacks with AWS Step Functions](https://medium.com/swlh/callbacks-with-aws-step-functions-a3dde1bc7203) - 作者：罗斯·罗兹。
* [Using the CDK for CodePipelines Setup](https://www.stefreitag.de/wp/2019/03/07/using-aws-cdk-for-code-pipeline-setup/) - 作者：斯特凡·弗莱塔格。
* [Using the CDK for AWS MSK Setup](https://www.stefreitag.de/wp/2019/08/31/paths-are-made-by-walking-or-how-aws-cdk-and-msk-work-together/) - 作者：斯特凡·弗莱塔格。
* [Serverless Dotnet - E01: Intro to AWS CDK](https://youtu.be/c9UXHPX6-Ns) - 作者：杰克·斯科特。
* [GitHub repository](https://github.com/jakejscott/aws-cdk-phone-verify-api) - 作者：杰克·斯科特。
* [Infrastructure is Code with the AWS CDK](https://youtu.be/ZWCvNFUN-sU) - AWS 技术讲座网络研讨会。
* [tecRacer Amazon AWS Blog](https://aws-blog.de/tags/cdk.html) - Gernot Glawe 来自 aws-blog.de 的几篇博客文章。
* [Using CDK to build a UDP NLB Logging Service](https://youtu.be/dXTEVp0ATzo) - 由 ClouderDex 提供。
* [GitHub Repo](https://github.com/ClouderDex/CDK-UDP-NLB-Demo) - 由 ClouderDex 提供。
* [Purely Functional Cloud Components with AWS CDK](https://i.am.fog.fish/2019/08/23/purely-functional-cloud-with-aws-cdk.html) - 卜雾鱼。
* [Using the CDK to probe multiple accounts (sfn/lambda/sqs/sechub)](https://fudless.xyz/aws/seedecay/) - 来自 [fudless.xyz](https://fudless.xyz) 的博客文章。
* [Scheduled Lambda Functions and CI/CD pipeline with AWS CDK](https://medium.com/hatchsoftware/using-the-aws-cdk-to-build-scheduled-lambda-functions-13eb1674586e) - 作者：马丁·托伦。
* [GitHub Repo](https://github.com/HatchSoftware/automatic-aws-db-shutdown-cdk) - 作者：马丁·托伦。
* [AWS Client VPN with mutual TLS](https://lanwen.ru/posts/aws-client-vpn/) - 作者：基里尔·梅尔库舍夫。
* [CDK Step Functions](https://dev.to/elthrasher/exploring-aws-cdk-step-functions-1d1e) - 马特·摩根着。
* [Loading DynamoDB with Custom Resources](https://dev.to/elthrasher/exploring-aws-cdk-loading-dynamodb-with-custom-resources-jlf) - 马特·摩根着。
* [Loading DynamoDB with Provider Framework](https://dev.to/elthrasher/exploring-aws-cdk-a-million-a-minute-dynamodb-and-providerframework-e92) - 马特·摩根着。
* [German: React SPA und server-side rendering (SSR) mit AWS Lambda und CloudFront](https://superluminar.io/2020/02/07/react-spa-und-server-side-rendering-ssr-mit-aws-lambda-cloudfront-und-dem-cdk/) - 由 superluminar GmbH 提供。
* [Introducing AWS CDK with a real life Lambda and API gateway example](https://a.l3x.in/2020/02/04/migrating-from-terraform-to-cdk.html) - 作者：亚历山大·福廷。
* [CloudWatch Dashboards as Code (the Right Way) Using AWS CDK](https://medium.com/poka-techblog/cloudwatch-dashboards-as-code-the-right-way-using-aws-cdk-1453309c5481) - 作者：西蒙-皮埃尔·金格拉斯。
* [Coding the Jamstack missing parts: databases, crons & background jobs](https://dev.to/vvo/coding-the-jamstack-missing-parts-databases-crons-background-jobs-1bpj) - 文森特·沃耶着。
* [AWS CDK Continuous Integration and Delivery Using Travis CI](https://medium.com/better-programming/aws-cdk-continuous-integration-and-delivery-using-travis-ci-ee5dd7549434) - 作者：托马斯·辛普森。
* [Custom Resources with AWS CDK](https://medium.com/cyberark-engineering/custom-resources-with-aws-cdk-d9a8fad6b673?source=friends_link&sk=549fcf9d998bbea304bdd8d834aca9e6) - 作者：罗伊·本-约瑟夫。
* [Recommended AWS CDK project structure for Python applications](https://aws.amazon.com/blogs/developer/recommended-aws-cdk-project-structure-for-python-applications/) - 作者：亚历克斯·普尔弗。

## 相关项目

* [jsii](https://github.com/awslabs/jsii) - JavaScript 互操作接口，CDK 用于创建语言绑定的技术（当前支持 .NET、Java 和 Python）。
* [cdk8s](https://github.com/awslabs/cdk8s/) - 使用面向对象编程定义 Kubernetes 本机应用程序和抽象。
* [cdktf](https://github.com/hashicorp/terraform-cdk) - 使用编程构造定义基础设施资源并使用 HashiCorp Terraform 提供它们。
* [cdktg](https://github.com/hupe1980/cdk-threagile) - 敏捷威胁建模作为代码。

## 提示与技巧

* [Reflect on the CDK Type System](https://gist.github.com/eladb/68a009cf9c953b04a637bac5c40afdbc) - 探索 CDK 的类型系统。
* [Testing Your Construct Library CodeBuild Configuration Locally](https://github.com/aws/aws-codebuild-docker-images/tree/master/local_builds) - 使用 `jsii/superchain:latest` Docker 镜像。

## 贡献

欢迎投稿！首先阅读[贡献指南](contributing.md)。
