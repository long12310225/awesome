<br/>
<p对齐=“中心”>
  <img src="https://raw.githubusercontent.com/donnemartin/data-science-ipython-notebooks/master/images/aws.png">
</p>
<br/>

# 很棒的AWS [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

精彩的 AWS 库、开源存储库、指南、博客和其他资源的精选列表。

受到 [awesome](https://github.com/sindresorhus/awesome) 列表的启发。

## AWSome 的火热计

* 拥有 0100+ 颗星星的仓库：:fire:
* 拥有 0200+ 颗星星的回购协议：:fire::fire:
* 拥有 0500+ 颗星星的仓库::fire::fire::fire:
* 拥有 1000 多颗星星的仓库：:fire::fire::fire::fire:
* 拥有 2000+ 颗星星的仓库：:fire::fire::fire::fire::fire:

不在“The Fiery Meter of AWSome”上的存储库仍然很棒，请参阅[关于存储库 AWSomeness 的说明](https://github.com/donnemartin/awesome-aws/blob/master/CONTRIBUTING.md#a-note-on-repo-awsomeness)。

### `awesome-aws` Python 模块

[![Build Status](https://travis-ci.org/donnemartin/awesome-aws.svg?branch=master)](https://travis-ci.org/donnemartin/awesome-aws) [![Codecov](https://img.shields.io/codecov/c/github/donnemartin/awesome-aws.svg)](https://codecov.io/github/donnemartin/awesome-aws) [![PyPI version](https://badge.fury.io/py/awesome-aws.svg)](http://badge.fury.io/py/awesome-aws)

Python 模块 [`awesome-aws`](https://github.com/donnemartin/awesome-aws/tree/master/awesome) 定期扫描 [Awesome AWS](https://github.com/donnemartin/awesome-aws) 上的存储库，以保持 `Fiery Meter of AWSome` 的准确性。

## 贡献

欢迎贡献！

查看[贡献指南](https://github.com/donnemartin/awesome-aws/blob/master/CONTRIBUTING.md)。

另请查看[观察列表](https://github.com/donnemartin/awesome-aws/issues/34)。

## 索引

* [SDK 和示例](#sdks-and-samples)
    * [Android](#android-sdk)
    * [C++](#c-sdk)
    * [Clojure](#clojure-sdk)
    * [Go](#go-sdk)
    * [iOS](#ios-sdk)
    * [IoT](#iot-sdk)
    * [Java](#java-sdk)
    * [JavaScript](#javascript-sdk)
    * [Haskell](#haskell-sdk)
    * [Perl](#perl-sdk)
    * [PHP](#php-sdk)
    * [Python](#python-sdk)
    * [Ruby](#ruby-sdk)
    * [Rust](#rust-sdk)
    * [Scala](#scala-sdk)
    * [Xamarin](#xamarin-sdk)
    * [Unity](#unity-sdk)
    * [.NET](#net-sdk)
* [命令行工具](#command-line-tools)
    * [通用命令行界面](#universal-command-line-interface)
    * [Windows PowerShell](#windows-powershell)
* [集成开发环境工具包](#ide-toolkits)
    * [Eclipse 工具包](#eclipse-toolkit)
    * [视觉工作室工具包](#visual-studio-toolkit)
* [开源存储库](#open-source-repos)
    * [API网关](#api-gateway)
    * [CLI](#cli)
    * [CloudFormation](#cloudformation)
    * [CloudSearch](#cloudsearch)
    * [CloudTrail](#cloudtrail)
    * [CloudWatch](#cloudwatch)
    * [代码部署](#code-deploy)
    * [代码管道](#code-pipeline)
    * [Cognito](#cognito)
    * [数据管道](#data-pipeline)
    * [设备农场](#device-farm)
    * [DynamoDB](#dynamodb)
    * [弹性豆茎](#elastic-beanstalk)
    * [弹性容器服务](#elastic-container-service)
    * [弹性文件系统](#elastic-file-system)
    * [弹性MapReduce](#elastic-mapreduce)
    * [弹性搜索](#elastic-search)
    * [Elasticache](#elasticache)
    * [Glacier](#glacier)
    * [Kinesis](#kinesis)
    * [Lambda](#lambda)
    * [机器学习](#machine-learning)
    * [移动分析](#mobile-analytics)
    * [OpsWorks](#opsworks)
    * [Redshift](#redshift)
    * [53号公路](#route-53)
    * [S3](#s3)
    * [SNS](#sns)
    * [SQS](#sqs)
    * [Data](#data)
    * [DevOps](#devops)
    * [Security](#security)
    * [Accompanying](#accompanying-repos)
    * [Miscellaneous](#miscellaneous-repos)
* [指南、书籍、文档和培训](#guides-books-documentation-and-training)
    * [入门指南](#getting-started-guides)
    * [一般指南](#general-guides)
    * [Books](#books)
    * [Whitepapers](#whitepapers)
    * [Documentation](#documentation)
    * [Training](#training)
    * [案例研究：由 AWS 提供支持](#case-studies-powered-by-aws)
* [Social](#social)
    * [Blogs](#blogs)
    * [推特影响者](#twitter-influencers)
    * [脸书页面](#facebook-pages)
    * [YouTube 频道](#youtube-channels)
    * [领英群组](#linkedin-groups)
    * [Subreddits](#subreddits)
    * [Conferences](#conferences)
* [最新 KPI 和统计数据](#latest-kpis-and-stats)
* [核心服务附录](#appendix-of-core-services)
    * [简单英语服务](#services-in-plain-english)
    * [Compute](#compute-services)
    * [Networking](#networking-services)
    * [企业应用](#enterprise-applications)
    * [Analytics](#analytics-services)
    * [人工智能](#artificial-intelligence)
    * [管理工具](#management-tools)
    * [安全与身份](#security-and-identity-services)
    * [物联网](#internet-of-things-service)
    * [流动服务](#mobile-services)
    * [存储和内容交付](#storage-and-content-delivery-services)
    * [Databases](#databases)
    * [申请服务](#application-services)
    * [开发者工具](#developer-tools)
    * [杂项服务](#miscellaneous-services)
* [Contributing](#contributing)
* [Credits](#credits)
* [其他很棒的清单](#other-awesome-lists)
* [联系方式](#contact-info)
* [License](#license)

## SDK 和示例

*AWS 和社区 SDK 包含示例和文档，按语言分组。*

<br/>
<p对齐=“中心”>
  <img src="http://i.imgur.com/TK96G8T.png">
</p>
<br/>

### 安卓软件开发工具包

* [回购:火::火::火:](https://github.com/aws/aws-sdk-android)
* [带有示例的仓库 :fire::fire::fire:](https://github.com/awslabs/aws-sdk-android-samples)
* [Install](http://sdk-for-android.amazonwebservices.com/latest/aws-android-sdk.zip)
* [Docs](https://aws.amazon.com/documentation/sdk-for-android/)
* [了解更多](https://aws.amazon.com/mobile/sdk/)

### C++ SDK

* [回购：火：：火：：火：：火：](https://github.com/awslabs/aws-sdk-cpp)
* [带有示例的博客](https://aws.amazon.com/blogs/aws/introducing-the-aws-sdk-for-c/)

*C++ SDK 是一个实验室项目，文档和/或示例有限。*

### Clojure SDK

* [回购:火::火::火:](https://github.com/mcohen01/amazonica)
* [Install](https://github.com/mcohen01/amazonica#installation)
* [Docs](https://github.com/mcohen01/amazonica#documentation)

*Clojure SDK 是一个社区项目，文档和/或示例有限。*)

### 去SDK

* [回购：火：：火：：火：：火：：火：](https://github.com/aws/aws-sdk-go)
* [Install](https://github.com/aws/aws-sdk-go/wiki)
* [Docs](http://docs.aws.amazon.com/sdk-for-go/api/)
* [了解更多](https://aws.amazon.com/sdk-for-go/)

相关回购：

* [goamz/goamz :火::火:](https://github.com/goamz/goamz)

### iOS SDK

* [回购：火：：火：：火：：火：](https://github.com/aws/aws-sdk-ios)
* [带有示例的仓库 :fire::fire::fire::fire:](https://github.com/awslabs/aws-sdk-ios-samples)
* [Install](http://sdk-for-ios.amazonwebservices.com/latest/aws-ios-sdk.zip)
* [Docs](https://aws.amazon.com/documentation/sdk-for-ios/)
* [了解更多](https://aws.amazon.com/mobile/sdk/)

### 物联网SDK

* [Arduino 仓库](https://github.com/awslabs/aws-sdk-arduino)
* [C :fire::fire::fire 的回购协议：](https://github.com/aws/aws-iot-device-sdk-embedded-C)
* [JavaScript 存储库 :fire::fire::fire:](https://github.com/aws/aws-iot-device-sdk-js)
* [Arduino Yun 的仓库：fire：](https://github.com/aws/aws-iot-device-sdk-arduino-yun/)
* [Docs](http://docs.aws.amazon.com/iot/latest/developerguide/what-is-aws-iot.html)

*物联网 SDK 是一个实验室项目，文档和/或示例有限。*

### 开发工具包

* [回购：火：：火：：火：：火：：火：](https://github.com/aws/aws-sdk-java)
* [带有示例的仓库 :fire::fire:](https://github.com/awslabs/aws-java-sample)
* [Install](http://sdk-for-java.amazonwebservices.com/latest/aws-java-sdk.zip)
* [Docs](https://aws.amazon.com/documentation/sdk-for-java/)
* [了解更多](https://aws.amazon.com/sdk-for-java/)

### JavaScript SDK

* [回购：火：：火：：火：：火：：火：](https://github.com/aws/aws-sdk-js)
* [带有示例的仓库 :fire::fire:](https://github.com/awslabs/aws-nodejs-sample)
* [Install](http://docs.aws.amazon.com/AWSJavaScriptSDK/guide/node-intro.html)
* [Docs](https://aws.amazon.com/documentation/sdk-for-javascript/)
* [了解更多](https://aws.amazon.com/sdk-for-node-js/)

相关回购：

* [aws/aws-amplify :fire::fire::fire::fire::fire:](https://github.com/aws/aws-amplify)
* [奇尔茨/awssum :火::火:](https://github.com/chilts/awssum)
* [mirkokiefer/aws-lib :fire::fire::fire:](https://github.com/mirkokiefer/aws-lib)
* [SaltwaterC/aws2js :fire::fire:](https://github.com/SaltwaterC/aws2js)

### 哈斯克尔软件开发工具包

* [回购:火::火::火:](https://github.com/brendanhay/amazonka)
* [Docs](http://hackage.haskell.org/packages/#cat:AWS)

相关回购：

* [aristidb/aws :fire::fire:](https://github.com/aristidb/aws)

*Haskell SDK 是一个社区项目，文档和/或示例有限。*

### Perl SDK

* [回购：火：](https://github.com/pplu/aws-sdk-perl)
* [带有示例的回购协议：fire：](https://github.com/pplu/aws-sdk-perl/tree/master/examples)
* [Install](https://github.com/pplu/aws-sdk-perl#installation)
* [Docs](https://metacpan.org/pod/Paws)
* [了解更多](https://metacpan.org/pod/Paws)

*Perl SDK 是一个社区项目。*

### PHP SDK

* [回购：火：：火：：火：：火：：火：](https://github.com/aws/aws-sdk-php)
* [带有示例的回购协议](https://github.com/awslabs/aws-php-sample)
* [Install](http://docs.aws.amazon.com/aws-sdk-php/v3/guide/getting-started/installation.html)
* [Docs](https://aws.amazon.com/documentation/sdk-for-php/)
* [了解更多](https://aws.amazon.com/sdk-for-php/)

相关回购：

* [aws-sdk-php-laravel :fire::fire::fire::fire:](https://github.com/aws/aws-sdk-php-laravel)
* [aws-sdk-php-silex](https://github.com/aws/aws-sdk-php-silex)
* [aws-sdk-php-zf2：火：](https://github.com/aws/aws-sdk-php-zf2)

### Python SDK

* [回购：火：：火：：火：：火：：火：](https://github.com/boto/boto3)
* [带有示例的回购协议：fire：](https://github.com/awslabs/aws-python-sample)
* [Install](http://github.com/boto/boto#installation)
* [Docs](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
* [了解更多](http://github.com/boto/boto/blob/develop/README.rst#boto)

相关回购：

* [boto3 :火::火::火::火::火:](https://github.com/boto/boto3)
* [botocore :火::火::火::火:](https://github.com/boto/botocore)

### 红宝石SDK

* [回购：火：：火：：火：：火：：火：](https://github.com/aws/aws-sdk-ruby)
* [带有 S3 示例的存储库](https://github.com/awslabs/aws-ruby-sample)
* [Install](http://docs.aws.amazon.com/sdk-for-ruby/v3/developer-guide/setup-install.html)
* [Docs](https://aws.amazon.com/documentation/sdk-for-ruby/)
* [示例 :fire::fire::fire::fire::fire:](https://github.com/awsdocs/aws-doc-sdk-examples/tree/master/ruby/example_code/)

相关回购：

* [aws-sdk-rails:fire::fire::fire:](https://github.com/aws/aws-sdk-rails)
* [appoxy/aws:火::火:](https://github.com/appoxy/aws)
* [rightscale/right_aws :fire::fire:](https://github.com/rightscale/right_aws)

### Rust SDK

* [回购：火：：火：：火：：火：：火：](https://github.com/rusoto/rusoto)
* [Install](https://github.com/rusoto/rusoto#installation)
* [Docs](https://docs.rs/rusoto_core/)

*Rust SDK 是一个社区项目，文档和/或示例有限。*

### 斯卡拉软件开发工具包

* [Repo](https://github.com/awslabs/aws-scala-sdk)

相关回购：

* [atlassian/aws-scala](https://bitbucket.org/atlassian/aws-scala)
* [seratch/AWScala :fire::fire::fire:](https://github.com/seratch/AWScala)

*Scala SDK 是一个实验室项目，文档和/或示例有限。*

### 统一SDK

* [回购：火：](https://github.com/aws/aws-sdk-unity)
* [带有示例的回购协议：fire：](https://github.com/awslabs/aws-sdk-unity-samples)
* [Install](https://s3.amazonaws.com/aws-unity-sdk/latest/aws-unity-sdk.zip)
* [Docs](http://docs.aws.amazon.com/mobile/sdkforunity/developerguide/)

### Xamarin SDK

* [Repo](https://github.com/awslabs/aws-sdk-xamarin)
* [带有示例的博客](https://blog.xamarin.com/amazon-web-services-aws-mobile-sdks-for-xamarin-now-available/)

*Xamarin SDK 是一个实验室项目，文档和/或示例有限。*

### .NET SDK

* [回购：火：：火：：火：：火：](https://github.com/aws/aws-sdk-net)
* [带有示例的回购协议](https://github.com/awslabs/aws-auto-scaling-console-sample)
* [Install](http://sdk-for-net.amazonwebservices.com/latest/AWSToolsAndSDKForNet.msi)
* [Docs](https://aws.amazon.com/documentation/sdk-for-net/)
* [了解更多](https://aws.amazon.com/sdk-for-net/)
* [样品：火：](https://github.com/awslabs/aws-sdk-net-samples)

## 命令行工具

*AWS 和社区命令行工具以及示例和文档。*

<br/>
<p对齐=“中心”>
  <img src="https://raw.githubusercontent.com/donnemartin/data-science-ipython-notebooks/master/images/commands.png">
</p>
<br/>

### 通用命令行界面

* [回购：火：：火：：火：：火：：火：](https://github.com/aws/aws-cli)
* [Install](http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-set-up.html)
* [Docs](https://aws.amazon.com/documentation/cli/)
* [了解更多](https://aws.amazon.com/cli/)

相关回购：

* [awslabs/aws-shell :fire::fire::fire::fire::fire:](https://github.com/awslabs/aws-shell)
* [多尼马丁/锯:火::火::火::火::火:](https://github.com/donnemartin/saws)

### Windows PowerShell

* [Install](http://sdk-for-net.amazonwebservices.com/latest/AWSToolsAndSDKForNet.msi)
* [Docs](https://aws.amazon.com/documentation/powershell/)
* [了解更多](https://aws.amazon.com/powershell/)

## 集成开发环境工具包

*带有示例和文档的官方 IDE 工具包。*

<br/>
<p对齐=“中心”>
  <img src="http://i.imgur.com/x4nu914.png">
</p>
<br/>

### Eclipse 工具包

* [Install](http://docs.aws.amazon.com/AWSToolkitEclipse/latest/ug/tke_setup.html)
* [Docs](https://aws.amazon.com/documentation/awstoolkiteclipse/)
* [了解更多](https://aws.amazon.com/eclipse/)

### 视觉工作室工具包

* [Install](http://sdk-for-net.amazonwebservices.com/latest/AWSToolsAndSDKForNet.msi)
* [Docs](https://aws.amazon.com/documentation/aws-toolkit-visual-studio/)
* [了解更多](https://aws.amazon.com/visualstudio/)

## 开源存储库

*AWS 和社区开源项目，按服务分组。  有关更多详细信息，请参阅[关于 Repo AWSomeness 的说明](https://github.com/donnemartin/awesome-aws/blob/master/CONTRIBUTING.md#a-note-on-repo-awsomeness)。*

<br/>
<p对齐=“中心”>
  <img src="http://i.imgur.com/wbhTgga.png">
</p>
<br/>

### API网关

AWS 存储库：

* [api-gateway-secure-pet-store :fire::fire:](https://github.com/awslabs/api-gateway-secure-pet-store) - 通过 Lambda 获得 Cognito 凭证。
* [aws-apigateway-sdk-java](https://github.com/awslabs/aws-apigateway-sdk-java) - 适用于 Java 的 SDK。
* [aws-apigateway-swagger-importer :fire::fire::fire:](https://github.com/awslabs/aws-apigateway-importer) - 与 Swagger 配合使用的工具。

社区回购：

* [Contribute](https://github.com/donnemartin/awesome-aws/blob/master/CONTRIBUTING.md)

### 命令行界面

AWS 存储库：

* [awscli-aliases :fire::fire:](https://github.com/awslabs/awscli-aliases) - AWS CLI 别名的存储库。
* [amazon-ecs-cli :fire::fire::fire::fire:](https://github.com/aws/amazon-ecs-cli) - ECS CLI 使用相同的 Docker Compose 文件格式和熟悉的 Compose 命令。
* [aws-cli :fire::fire::fire::fire::fire:](https://github.com/aws/aws-cli) - 通用命令行界面。
* [aws-shell :fire::fire::fire::fire::fire:](https://github.com/awslabs/aws-shell)
* [awscli-cookbook](https://github.com/awslabs/awscli-cookbook) - 安装 CLI 工具并提供一组 LWRP 以在厨师食谱中使用。
* [awsmobile-cli :fire:](https://github.com/aws/awsmobile-cli) - JavaScript 生态系统中前端开发人员的 CLI 体验。

社区回购：

* [achiku/jungle :fire::fire::fire:](https://github.com/achiku/jungle) - EC2和ELB cli的操作应该更简单。
* [dbcli/athenacli :fire:](https://github.com/dbcli/athenacli) - 适用于 AWS Athena 服务的 CLI 工具，可以自动完成和语法突出显示。
* [donnemartin/saws :fire::fire::fire::fire::fire:](https://github.com/donnemartin/saws) - 强大的 AWS 命令​​行界面。
* [timkay/aws :fire::fire:](https://github.com/timkay/aws) - 轻松通过命令行访问 Amazon EC2、S3、SQS、ELB 和 SDB。
* [wallix/awless :fire::fire::fire::fire::fire:](https://github.com/wallix/awless) - 用于 Go 中的 EC2、IAM 和 S3 的强大 CLI。
* [99designs/aws-vault :fire::fire::fire::fire::fire:](https://github.com/99designs/aws-vault) - 一种用 Go 编写的安全存储 AWS 凭证的工具。

### 云形成

AWS 存储库：

* [aws-cdk :fire::fire::fire::fire::fire:](https://github.com/aws/aws-cdk) - 用于在代码中定义云基础设施的框架。
* [aws-cfn-custom-resource-examples](https://github.com/awslabs/aws-cfn-custom-resource-examples) - 自定义资源示例。
* [aws-cfn-resource-bridge](https://github.com/aws/aws-cfn-resource-bridge) - 自定义资源框架。
* [cfn-python-lint :fire::fire::fire::fire::fire:](https://github.com/awslabs/cfn-python-lint) - 用于检查/验证 CloudFormation 的工具。
* [cfncluster-cookbook](https://github.com/awslabs/cfncluster-cookbook) - 示例食谱。
* [cfncluster :fire::fire::fire:](https://github.com/awslabs/cfncluster) - 部署和维护 HPC 集群的框架。

社区回购：

* [Appliscale/perun](https://github.com/Appliscale/perun) - 用于检查/验证和管理 CloudFormation 模板和堆栈的 CLI 工具。
* [bazaarvoice/cloudformation-ruby-dsl :fire::fire:](https://github.com/bazaarvoice/cloudformation-ruby-dsl) - 用于创建模板的 Ruby DSL。
* [beaknit/cform :fire:](https://github.com/beaknit/cform) - SublimeText 插件。
* [cloudreach/sceptre :fire::fire::fire::fire:](https://github.com/cloudreach/sceptre) - 用于自动化 CloudFormation 的 CLI 工具。
* [cloudtools/troposphere :fire::fire::fire::fire::fire:](https://github.com/cloudtools/troposphere) - 用于创建描述的 Python 库。
* [peterkh/cumulus :fire::fire:](https://github.com/peterkh/cumulus) - 管理堆栈。
* [envato/stack_master :fire::fire:](https://github.com/envato/stack_master) - 用于管理 CloudFormation 堆栈的 CLI 工具。
* [sparkleformation/sfn](https://github.com/sparkleformation/sfn) - 用于堆栈管理的 CLI。
* [sparkleformation/sparkle_formation :fire::fire:](https://github.com/sparkleformation/sparkle_formation) - 用于模板创建的 Ruby DSL。
* [Stelligent/cfn_nag :fire::fire::fire::fire:](https://github.com/stelligent/cfn_nag) - CloudFormation 模板的 Linting 工具

### 云搜索

AWS 存储库：

* [cloudsearchable](https://github.com/awslabs/cloudsearchable) - ActiveRecord 风格的 ORM 查询接口。

社区回购：

* [Contribute](https://github.com/donnemartin/awesome-aws/blob/master/CONTRIBUTING.md)

### 云踪

AWS 存储库：

* [aws-cloudtrail-processing-library](https://github.com/aws/aws-cloudtrail-processing-library) - 轻松使用和处理日志文件。

社区回购：

* [AppliedTrust/traildash :fire::fire:](https://github.com/AppliedTrust/traildash) - 光滑的仪表板。
* [GorillaStack/auto-tag :fire::fire:](https://github.com/GorillaStack/auto-tag) - 在创建时自动标记 AWS 资源，以进行成本分配。

### 云观察

AWS 存储库：

* [cloudwatch-logs-subscription-consumer :fire::fire:](https://github.com/awslabs/cloudwatch-logs-subscription-consumer) - Kinesis 流阅读器。
* [ecs-cloudwatch-logs](https://github.com/awslabs/ecs-cloudwatch-logs) - 关于使用 Amazon ECS 和 Amazon CloudWatch 日志的博客文章中的资产。
* [logstash-output-cloudwatchlogs](https://github.com/awslabs/logstash-output-cloudwatchlogs) - 将日志发送到 CloudWatch 的 Logstash 插件。
* [opsworks-cloudwatch-logs-cookbooks](https://github.com/awslabs/opsworks-cloudwatch-logs-cookbooks) - OpsWorks 示例食谱。

社区回购：

* [jorgebastida/awslogs :fire::fire::fire::fire::fire:](https://github.com/jorgebastida/awslogs) - 用于查询组、流和事件的简单 CLI。
* [newrelic-platform/newrelic_aws_cloudwatch_plugin :fire:](https://github.com/newrelic-platform/newrelic_aws_cloudwatch_plugin) - 新的遗物插件。

### 代码部署

AWS 存储库：

* [aws-codedeploy-agent :fire::fire:](https://github.com/aws/aws-codedeploy-agent) - 样品代理。
* [aws-codedeploy-plugin :fire:](https://github.com/awslabs/aws-codedeploy-plugin) - 詹金斯插件。
* [aws-codedeploy-samples :fire::fire::fire:](https://github.com/awslabs/aws-codedeploy-samples) - 示例和模板场景。

社区回购：

* [Contribute](https://github.com/donnemartin/awesome-aws/blob/master/CONTRIBUTING.md)

### 代码管道

AWS 存储库：

* [aws-codepipeline-custom-job-worker](https://github.com/awslabs/aws-codepipeline-custom-job-worker) - 创建自定义操作时开发您自己的工作人员。
* [aws-codepipeline-jenkins-aws-codedeploy_linux](https://github.com/awslabs/aws-codepipeline-jenkins-aws-codedeploy_linux) - Linux 的四阶段管道。
* [aws-codepipeline-plugin-for-jenkins](https://github.com/awslabs/aws-codepipeline-plugin-for-jenkins) - 詹金斯插件。
* [aws-codepipeline-s3-aws-codedeploy_linux :fire:](https://github.com/awslabs/aws-codepipeline-s3-aws-codedeploy_linux) - Linux 的简单管道。
* [AWSCodePipeline-Jenkins-AWSCodeDeploy_Windows](https://github.com/awslabs/AWSCodePipeline-Jenkins-AWSCodeDeploy_Windows) - Windows 的四阶段管道。
* [AWSCodePipeline-S3-AWSCodeDeploy_Windows](https://github.com/awslabs/AWSCodePipeline-S3-AWSCodeDeploy_Windows) - Windows 的简单管道。

社区回购：

* [Contribute](https://github.com/donnemartin/awesome-aws/blob/master/CONTRIBUTING.md)

### 认知

AWS 存储库：

* [amazon-cognito-android](https://github.com/aws/amazon-cognito-android) - 适用于 Android 的同步 SDK。
* [amazon-cognito-developer-authentication-sample](https://github.com/awslabs/amazon-cognito-developer-authentication-sample) - 认证样本。
* [amazon-cognito-dotnet](https://github.com/aws/amazon-cognito-dotnet) - 适用于 .NET 的同步 SDK。
* [amazon-cognito-ios](https://github.com/aws/amazon-cognito-ios) - 适用于 iOS 的同步 SDK。
* [amazon-cognito-js :fire::fire:](https://github.com/aws/amazon-cognito-js) - JavaScript 同步 SDK。
* [amazon-cognito-streams-sample](https://github.com/awslabs/amazon-cognito-streams-sample) - 使用 Streams 示例。
* [cognito-sample-nodejs :fire:](https://github.com/awslabs/cognito-sample-nodejs) - Node.js 的示例应用程序。

社区回购：

* [capeless/warrant :fire::fire:](https://github.com/capless/warrant) - 用于使用 Cognito 的 Python 库。
* [rahulpsd18/cognito-backup-restore :fire:](https://github.com/rahulpsd18/cognito-backup-restore) - 用于备份和恢复 Cognito 用户池的工具。

### 数据管道

AWS 存储库：

* [data-pipeline-samples :fire::fire:](https://github.com/awslabs/data-pipeline-samples) - 样本管道。

社区回购：

* [Contribute](https://github.com/donnemartin/awesome-aws/blob/master/CONTRIBUTING.md)

### 设备农场

AWS 存储库：

* [aws-device-farm-appium-tests-for-sample-app](https://github.com/awslabs/aws-device-farm-appium-tests-for-sample-app) - Appium TestNG Android 测试。
* [aws-device-farm-calabash-tests-for-sample-app](https://github.com/awslabs/aws-device-farm-calabash-tests-for-sample-app) - 葫芦 Android 测试。
* [aws-device-farm-gradle-plugin](https://github.com/awslabs/aws-device-farm-gradle-plugin) - 摇篮插件。
* [aws-device-farm-jenkins-plugin](https://github.com/awslabs/aws-device-farm-jenkins-plugin) - 詹金斯插件。
* [aws-device-farm-sample-app-for-android :fire:](https://github.com/awslabs/aws-device-farm-sample-app-for-android) - Android 应用程序示例。

社区回购：

* [Contribute](https://github.com/donnemartin/awesome-aws/blob/master/CONTRIBUTING.md)

### 动态数据库

AWS 存储库：

* [aws-dotnet-session-provider](https://github.com/aws/aws-dotnet-session-provider) - ASP.NET 应用程序的会话状态提供程序。
* [aws-dotnet-trace-listener](https://github.com/aws/aws-dotnet-trace-listener) - System.Diagnostics 的跟踪侦听器，可用于记录事件。
* [aws-dynamodb-encryption-java :fire:](https://github.com/awslabs/aws-dynamodb-encryption-java) - Java 加密客户端。
* [aws-dynamodb-examples :fire::fire:](https://github.com/awslabs/aws-dynamodb-examples) - 使用 Java SDK 的示例。
* [aws-dynamodb-mars-json-demo](https://github.com/awslabs/aws-dynamodb-mars-json-demo) - 存储和索引 NASA JPL 火星图像。
* [aws-dynamodb-session-tomcat](https://github.com/aws/aws-dynamodb-session-tomcat) - Apache Tomcat 的会话存储。
* [aws-sessionstore-dynamodb-ruby](https://github.com/aws/aws-sessionstore-dynamodb-ruby) - 处理 Ruby Web 应用程序的会话。
* [dynamodb-cross-region-library :fire::fire:](https://github.com/awslabs/dynamodb-cross-region-library) - 跨区域复制。
* [dynamodb-geo :fire::fire:](https://github.com/awslabs/dynamodb-geo) - 用于创建和查询地理空间数据的库。
* [dynamodb-import-export-tool](https://github.com/awslabs/dynamodb-import-export-tool) - 导入和导出示例。
* [dynamodb-online-index-violation-detector](https://github.com/awslabs/dynamodb-online-index-violation-detector) - 查找在线 GSI 的哈希键和范围键的违规行为。
* [dynamodb-streams-kinesis-adapter](https://github.com/awslabs/dynamodb-streams-kinesis-adapter) - 用于使用和处理 DynamoDB 流中的数据的 Kinesis 接口。
* [dynamodb-tictactoe-example-app](https://github.com/awslabs/dynamodb-tictactoe-example-app) - 轻量级Python应用程序。
* [dynamodb-titan-storage-backend :fire::fire:](https://github.com/awslabs/dynamodb-titan-storage-backend) - Titan 的存储后端。
* [dynamodb-transactions :fire::fire:](https://github.com/awslabs/dynamodb-transactions) - 跨多个项目和表执行原子写入和隔离读取。
* [logstash-input-dynamodb :fire:](https://github.com/awslabs/logstash-input-dynamodb) - Logstash 输入插件。

社区回购：

* [channl/dynamodb-lambda-autoscale :fire::fire:](https://github.com/channl/dynamodb-lambda-autoscale) - 使用 Lambda 自动缩放 DynamoDB 预置容量。
* [lyft/confidant :fire::fire::fire::fire:](https://github.com/lyft/confidant) - 存储秘密，静态加密。
* [sebdah/dynamic-dynamodb :fire::fire::fire:](https://github.com/sebdah/dynamic-dynamodb) - 提供自动缩放。
* [sensedeep/dynamodb-onetable :fire::fire::fire:](https://github.com/sensedeep/dynamodb-onetable) - 使用 NodeJS 进行单表设计的 DynamoDB 库。

### 弹性豆茎

AWS 存储库：

* [aws-eb-glassfish-dockerfiles](https://github.com/aws/aws-eb-glassfish-dockerfiles) - GlassFish 泊坞窗文件。
* [aws-eb-python-dockerfiles](https://github.com/aws/aws-eb-python-dockerfiles) - Python docker 文件。
* [eb-demo-php-simple-app :fire:](https://github.com/awslabs/eb-demo-php-simple-app) - 简单的 PHP 应用程序。
* [eb-docker-multiple-ports](https://github.com/awslabs/eb-docker-multiple-ports) - 使用 Docker 镜像的简单 Node.js 和 Tomcat 应用程序。
* [eb-docker-nginx-proxy :fire:](https://github.com/awslabs/eb-docker-nginx-proxy) - 使用 PHP-FPM 和 Nginx Docker 映像的简单 PHP 应用程序。
* [eb-docker-virtual-hosting](https://github.com/awslabs/eb-docker-virtual-hosting) - 使用 Docker 映像的简单 PHP、Tomcat 和 Nginx 应用程序。
* [eb-node-express-sample :fire::fire:](https://github.com/awslabs/eb-node-express-sample) - 示例快递应用程序。
* [eb-node-express-signup](https://github.com/awslabs/eb-node-express-signup) - Express 框架和 Bootstrap Node.js 示例应用程序。
* [eb-node-express](https://github.com/awslabs/eb-node-express) - 开发人员指南中引用的示例应用程序。
* [eb-py-flask-signup-worker](https://github.com/awslabs/eb-py-flask-signup-worker) - 说明工作者角色的 Python 应用程序。
* [eb-py-flask-signup :fire::fire:](https://github.com/awslabs/eb-py-flask-signup) - 使用 Flask 和 Bootstrap 的 Python 注册表单应用程序。
* [eb-python-flask](https://github.com/awslabs/eb-python-flask) - 简单的 Python 和 Flask 应用程序。
* [eb-wif-sample](https://github.com/awslabs/eb-wif-sample) - 使用 Web Identity Federation 的示例登录应用程序。

社区回购：

* [alienfast/elastic-beanstalk :fire:](https://github.com/alienfast/elastic-beanstalk) - Gem 具有用于 Rails 应用程序的 rake 配置和部署。
* [ThoughtWorksStudios/eb_deployer :fire::fire:](https://github.com/ThoughtWorksStudios/eb_deployer) - 蓝绿部署自动化。

### 弹性计算云

AWS 存储库：

* [Contribute](https://github.com/donnemartin/awesome-aws/blob/master/CONTRIBUTING.md)

社区回购：

* [alestic/ec2-consistent-snapshot :fire::fire:](https://github.com/alestic/ec2-consistent-snapshot) - 在 EC2 中启动一致的 EBS 快照。
* [ConradIrwin/aws-name-server :fire::fire::fire:](https://github.com/ConradIrwin/aws-name-server) - DNS 服务器可让您按名称查找实例。
* [cristim/autospotting :fire::fire::fire::fire::fire:](https://github.com/autospotting/autospotting) - 使用兼容的现货实例自动滚动替换 AutoScaling 组中的按需 EC2 实例。
* [evannuil/aws-snapshot-tool :fire::fire:](https://github.com/evannuil/aws-snapshot-tool) - 自动执行 EBS 快照和轮换。
* [kelseyhightower/kubernetes-the-hard-way :fire::fire::fire::fire::fire:](https://github.com/kelseyhightower/kubernetes-the-hard-way) - 在 EC2 上艰难地引导 Kubernetes。没有脚本。
* [mirakui/ec2ssh :fire::fire:](https://github.com/mirakui/ec2ssh) - SSH 配置管理器。
* [openebs/openebs :fire::fire::fire::fire::fire:](https://github.com/openebs/openebs) - 容器化块存储 QoS SLA、跨可用区和环境的分层和副本策略，以及可预测和可扩展的性能。
* [skavanagh/EC2Box :fire::fire:](https://github.com/skavanagh/EC2Box) - 基于 Web 的 SSH 控制台可同时管理多个实例。
* [wbailey/claws :fire:](https://github.com/wbailey/claws) - CLI 驱动的控制台与 capistrano 集成。

### 弹性容器服务

AWS 存储库：

* [amazon-ecs-agent :fire::fire::fire::fire:](https://github.com/aws/amazon-ecs-agent) - 在容器上运行并启动容器的代理。
* [amazon-ecs-amazon-efs](https://github.com/awslabs/amazon-ecs-amazon-efs) - 保留容器中的数据。
* [amazon-ecs-init :fire:](https://github.com/aws/amazon-ecs-init) - RPM 开发用于支持 Amazon ECS 容器代理。
* [blox :fire::fire::fire:](https://github.com/blox/blox) - 用于在 ECS 上构建自定义调度程序的开源工具。
* [ecs-blue-green-deployment :fire::fire:](https://github.com/awslabs/ecs-blue-green-deployment) - ECS上的蓝绿部署。
* [ecs-cloudwatch-logs](https://github.com/awslabs/ecs-cloudwatch-logs) - 使用 Amazon ECS 和 Amazon CloudWatch 日志获取的博客资产。
* [ecs-demo-php-simple-app :fire:](https://github.com/awslabs/ecs-demo-php-simple-app) - 简单的 PHP 应用程序。
* [ecs-mesos-scheduler-driver :fire:](https://github.com/awslabs/ecs-mesos-scheduler-driver) - 集成 Apache Mesos。
* [ecs-refarch-continuous-deployment :fire::fire::fire:](https://github.com/awslabs/ecs-refarch-continuous-deployment) - 使用 CodePipeline 持续部署到 ECS 的参考架构。
* [ecs-task-kite](https://github.com/awslabs/ecs-task-kite) - 用于任务间通信的简单大使容器。
* [lambda-ecs-worker-pattern :fire::fire:](https://github.com/awslabs/lambda-ecs-worker-pattern) - 使用 SQS 和 ECS 扩展 Lambda。
* [py-flask-signup-docker](https://github.com/awslabs/py-flask-signup-docker) - Python 示例应用程序。
* [service-discovery-ecs-consul :fire:](https://github.com/awslabs/service-discovery-ecs-consul) - 来自博客的资产，通过 Consul 和 Amazon ECS 进行服务发现。

社区回购：

* [Lumoslabs/broadside](https://github.com/lumoslabs/broadside) - 用于部署容器化应用程序修订版的命令行工具。
* [Stelligent/mu :fire::fire::fire:](https://github.com/stelligent/mu) - 通过 CodeBuild 和 CodePipeline 简化 ECS 部署的命令行工具。

### 弹性文件系统

AWS 存储库：

* [amazon-ecs-amazon-efs](https://github.com/awslabs/amazon-ecs-amazon-efs) - 保留 ECS 中的数据。

社区回购：

* [Contribute](https://github.com/donnemartin/awesome-aws/blob/master/CONTRIBUTING.md)

### 弹性MapReduce

AWS 存储库：

* [emr-bootstrap-actions :fire::fire::fire:](https://github.com/awslabs/emr-bootstrap-actions) - 示例引导操作。
* [emr-sample-apps](https://github.com/awslabs/emr-sample-apps) - 示例应用程序。

社区回购：

* [Yelp/mrjob :fire::fire::fire::fire::fire:](https://github.com/Yelp/mrjob) - 在 Hadoop 或 EMR 上运行 MapReduce 作业。

### 弹性搜索

AWS 存储库：

* [logstash-output-amazon_es :fire::fire:](https://github.com/awslabs/logstash-output-amazon_es) - Logstash 输出插件用于签名和导出事件。
* [opsworks-elasticsearch-cookbook](https://github.com/awslabs/opsworks-elasticsearch-cookbook) - OpsWorks Elasticsearch 示例手册。

社区回购：

* [elastic/elasticsearch-cloud-aws :fire::fire::fire:](https://github.com/elastic/elasticsearch-cloud-aws) - Elasticsearch 插件。

### 弹性疼痛

AWS 存储库：

* [aws-elasticache-cluster-client-libmemcached](https://github.com/awslabs/aws-elasticache-cluster-client-libmemcached) - Libmemcached 库支持。
* [aws-elasticache-cluster-client-memcached-for-java](https://github.com/awslabs/aws-elasticache-cluster-client-memcached-for-java) - Java 客户端。
* [aws-elasticache-cluster-client-memcached-for-php](https://github.com/awslabs/aws-elasticache-cluster-client-memcached-for-php) - 连接到 ElastiCache 的增强型 PHP 库。
* [elasticache-cluster-config-net](https://github.com/awslabs/elasticache-cluster-config-net) - Enyim 的 MemcachedClient 的配置对象以启用自动发现。

社区回购：

* [Contribute](https://github.com/donnemartin/awesome-aws/blob/master/CONTRIBUTING.md)

### 冰川

社区回购：

* [vsespb/mt-aws-glacier :fire::fire::fire:](https://github.com/vsespb/mt-aws-glacier) - Perl 多线程多部分同步到 Glacier。

### 运动

AWS 存储库：

* [amazon-kinesis-aggregators :fire:](https://github.com/awslabs/amazon-kinesis-aggregators) - 提供了一种创建实时聚合的简单方法。
* [amazon-kinesis-client-net](https://github.com/awslabs/amazon-kinesis-client-net) - .NET 客户端库。
* [amazon-kinesis-client-nodejs :fire::fire:](https://github.com/awslabs/amazon-kinesis-client-nodejs) - Node.js 的客户端库。
* [amazon-kinesis-client-python :fire::fire:](https://github.com/awslabs/amazon-kinesis-client-python) - Python 客户端库。
* [amazon-kinesis-client-ruby :fire:](https://github.com/awslabs/amazon-kinesis-client-ruby) - Ruby 客户端库。
* [amazon-kinesis-client :fire::fire::fire:](https://github.com/awslabs/amazon-kinesis-client) Amazon Kinesis 的客户端库。
* [amazon-kinesis-connectors :fire::fire:](https://github.com/awslabs/amazon-kinesis-connectors) - 用于与其他 AWS 和非 AWS 服务集成的库。
* [amazon-kinesis-data-visualization-sample :fire:](https://github.com/awslabs/amazon-kinesis-data-visualization-sample) - 示例数据可视化应用程序。
* [amazon-kinesis-learning](https://github.com/awslabs/amazon-kinesis-learning) - 学习 Kinesis 开发。
* [amazon-kinesis-producer :fire::fire:](https://github.com/awslabs/amazon-kinesis-producer) - 制作人库。
* [amazon-kinesis-scaling-utils :fire::fire:](https://github.com/awslabs/amazon-kinesis-scaling-utils) - 提供扩展流的能力。
* [aws-fluent-plugin-kinesis :fire::fire:](https://github.com/awslabs/aws-fluent-plugin-kinesis) - 流畅的插件。
* [dynamodb-streams-kinesis-adapter](https://github.com/awslabs/dynamodb-streams-kinesis-adapter) - DynamoDB 流适配器。
* [kinesis-log4j-appender](https://github.com/awslabs/kinesis-log4j-appender) - Log4J 附加程序。
* [kinesis-poster-worker](https://github.com/awslabs/kinesis-poster-worker) - 简单的多线程Python Poster 和Worker。
* [kinesis-storm-spout :fire:](https://github.com/awslabs/kinesis-storm-spout) - Storm 的喷口。
* [mqtt-kinesis-bridge](https://github.com/awslabs/mqtt-kinesis-bridge) - Python 中的简单 MQTT 桥接器。

社区回购：

* [Contribute](https://github.com/donnemartin/awesome-aws/blob/master/CONTRIBUTING.md)

### 拉姆达

AWS 存储库：

* [amazon-elasticsearch-lambda-samples :fire::fire:](https://github.com/awslabs/amazon-elasticsearch-lambda-samples) - 从 S3 和 Kinesis 为 Elasticsearch 摄取数据。
* [awslabs/aws-sam-local :fire::fire::fire::fire::fire:](https://github.com/awslabs/aws-sam-local) - 用于本地开发和测试无服务器应用程序的 CLI 工具。
* [aws-lambda-go :fire::fire::fire::fire::fire:](https://github.com/aws/aws-lambda-go) - 帮助 Go 开发人员开发 Lambda 函数的库、示例和工具。
* [aws-lambda-java-libs :fire::fire:](https://github.com/aws/aws-lambda-java-libs) - 接口定义和辅助类的官方镜像。
* [aws-lambda-redshift-loader :fire::fire::fire:](https://github.com/awslabs/aws-lambda-redshift-loader) - 红移装载机。
* [chalice :fire::fire::fire::fire::fire:](https://github.com/awslabs/chalice) - Python 无服务器微框架。
* [create-thumbnails-lambda](https://github.com/awslabs/create-thumbnails-lambda) - 使用 grunt-aws-lambda 插件帮助您开发和测试。
* [lambda-ecs-worker-pattern :fire::fire:](https://github.com/awslabs/lambda-ecs-worker-pattern) - 使用 SQS 和 ECS 扩展 Lambda。
* [lambda-refarch-fileprocessing :fire::fire:](https://github.com/awslabs/lambda-refarch-fileprocessing) - 实时文件处理的参考架构。
* [lambda-refarch-iotbackend :fire::fire:](https://github.com/awslabs/lambda-refarch-iotbackend) - 用于创建 IoT 后端的参考架构。
* [lambda-refarch-mobilebackend :fire::fire::fire:](https://github.com/awslabs/lambda-refarch-mobilebackend) - 用于创建移动后端的参考架构。
* [lambda-refarch-webapp :fire::fire::fire::fire:](https://github.com/awslabs/lambda-refarch-webapp) - 用于创建 Web 应用程序的参考架构。

社区回购：

* [alestic/lambdash :fire::fire::fire:](https://github.com/alestic/lambdash) - Lambda shell - 在 Lambda 环境中运行 sh 命令。
* [Alephbet/gimel :fire::fire:](https://github.com/Alephbet/gimel) - 使用 Lambda 运行您自己的 A/B 测试后端。
* [apex/apex ](https://github.com/apex/apex) - 具有 Go 支持的最小 AWS Lambda 函数管理器。
* [claudiajs/claudia :fire::fire::fire::fire::fire:](https://github.com/claudiajs/claudia) - 轻松将 Node.js 项目部署到 Lambda 和 API Gateway。
* [cloudnative/lambda-chat :fire::fire:](https://github.com/cloudnative/lambda-chat) - 一个没有服务器的聊天应用程序。
* [danilop/LambdAuth :fire::fire::fire::fire:](https://github.com/danilop/LambdAuth) - 身份验证服务示例。
* [eawsy/aws-lambda-go :fire::fire::fire:](https://github.com/eawsy/aws-lambda-go) - 在 Lambda 上执行 Go 的快速而干净的方法。
* [garnaat/kappa :fire::fire::fire:](https://github.com/garnaat/kappa) - Kappa 是一个 CLI 工具，可以更轻松地部署、更新和测试 AWS Lambda 的功能。
* [goadapp/goad :fire::fire::fire::fire:](https://github.com/goadapp/goad) - 由 Lambda 驱动的高度分布式负载测试工具。
* [graphcool/chromeless :fire::fire::fire::fire::fire:](https://github.com/graphcool/chromeless) - 通过 Lambda 自动化 Chrome。
* [grycap/scar :fire::fire::fire:](https://github.com/grycap/scar) - 在 AWS Lambda 中透明地执行 Docker 映像之外的容器。
* [jeremydaly/lambda-api :fire::fire::fire::fire:](https://github.com/jeremydaly/lambda-api) - 适用于无服务器应用程序的轻量级 Web 框架。
* [jimpick/lambda-comments :fire::fire::fire:](https://github.com/jimpick/lambda-comments) - 使用 Lambda 构建的博客评论系统。
* [jorgebastida/gordon :fire::fire::fire::fire::fire:](https://github.com/jorgebastida/gordon) - Gordon 是一个使用 CloudFormation 创建、连接和部署 AWS Lambda 的工具。
* [ks888/LambStatus :fire::fire::fire::fire:](https://github.com/ks888/LambStatus) - 受 StatusPage.io 启发、基于 AWS Lambda 构建的状态页面系统。
* [kubek2k/lambdoku :fire::fire::fire:](https://github.com/kubek2k/lambdoku) - 使用 Lambda 时的类似 Heroku 的体验。
* [lambci/lambci :fire::fire::fire::fire::fire:](https://github.com/lambci/lambci) - 基于 Lambda 构建的持续集成系统。
* [littlstar/s3-lambda :fire::fire::fire::fire:](https://github.com/littlstar/s3-lambda) - Lambda 在具有并发控制（each、map、reduce、filter）的 S3 对象上运行。
* [mentum/lambdaws :fire::fire::fire::fire:](https://github.com/mentum/lambdaws) - 轻松部署、运行并获得结果。
* [Miserlou/Zappa :fire::fire::fire::fire::fire:](https://github.com/Miserlou/Zappa) - 使用 AWS Lambda + API 网关的无服务器 WSGI Python Web 应用程序。
* [nficano/python-lambda :fire::fire::fire::fire:](https://github.com/nficano/python-lambda) - 用于在 Lambda 中开发和部署无服务器 Python 代码的工具包。
* [serverless/serverless :fire::fire::fire::fire::fire:](https://github.com/serverless/serverless) 无服务器应用程序框架（以前称为 JAWS）。
* [Tim-B/grunt-aws-lambda :fire::fire:](https://github.com/Tim-B/grunt-aws-lambda) - 咕噜插件。
* [trek10inc/aws-lambda-debugger :fire::fire:](https://github.com/trek10inc/aws-lambda-debugger) - 用于在 Node 6.10 上运行的 Lambda 函数的远程调试工具

### 机器学习

AWS 存储库：

* [machine-learning-samples :fire::fire::fire:](https://github.com/awslabs/machine-learning-samples) - 示例应用程序。

社区回购：

* [Contribute](https://github.com/donnemartin/awesome-aws/blob/master/CONTRIBUTING.md)

### 移动分析

AWS 存储库：

* [aws-sdk-mobile-analytics-js](https://github.com/aws/aws-sdk-mobile-analytics-js) - JavaScript SDK。

社区回购：

* [Contribute](https://github.com/donnemartin/awesome-aws/blob/master/CONTRIBUTING.md)

### 行动工厂

AWS 存储库：

* [opsworks-attribute-customization](https://github.com/awslabs/opsworks-attribute-customization) - 属性定制示例。
* [opsworks-capistrano](https://github.com/awslabs/opsworks-capistrano) - Capistrano 与实例。
* [opsworks-cloudwatch-logs-cookbooks](https://github.com/awslabs/opsworks-cloudwatch-logs-cookbooks) - CloudWatch 示例食谱。
* [opsworks-cookbooks :fire::fire::fire::fire:](https://github.com/aws/opsworks-cookbooks) - 厨师食谱。
* [opsworks-demo-php-photo-share-app](https://github.com/awslabs/opsworks-demo-php-photo-share-app) - 简单的 PHP 照片共享应用程序。
* [opsworks-demo-php-simple-app](https://github.com/awslabs/opsworks-demo-php-simple-app) - 简单的 PHP 应用程序。
* [opsworks-demo-rails-photo-share-app](https://github.com/awslabs/opsworks-demo-rails-photo-share-app) - Rails 应用程序示例。
* [opsworks-elasticsearch-cookbook](https://github.com/awslabs/opsworks-elasticsearch-cookbook) - Elasticsearch 示例食谱。
* [opsworks-example-cookbooks :fire:](https://github.com/awslabs/opsworks-example-cookbooks) - 与示例应用程序一起使用的食谱。
* [opsworks-first-cookbook](https://github.com/awslabs/opsworks-first-cookbook) - 食谱用于演示简单的食谱。
* [opsworks-windows-demo-](https://github.com/awslabs/opsworks-windows-demo-nodejs) - 示例 Node.JS 应用程序。
* [opsworks-windows-demo-cookbooks](https://github.com/awslabs/opsworks-windows-demo-cookbooks) - Windows 食谱。
* [todo-sample-app-cookbooks](https://github.com/awslabs/todo-sample-app-cookbooks) - 与 todo-sample-app 关联的自定义食谱。

社区回购：

* [Contribute](https://github.com/donnemartin/awesome-aws/blob/master/CONTRIBUTING.md)

### 红移

AWS 存储库：

* [aws-lambda-redshift-loader :fire::fire::fire:](https://github.com/awslabs/aws-lambda-redshift-loader) - Lambda 数据库加载器。
* [amazon-redshift-utils :fire::fire::fire::fire::fire:](https://github.com/awslabs/amazon-redshift-utils) - 将最佳列编码应用于现有表。

社区回购：

* [Lumoslabs/aleph](https://github.com/lumoslabs/aleph) - 用于编写和运行 Redshift 的全功能 Web 应用程序
查询。支持查询的修订跟踪并具有基本的可视化支持。
* [getredash/redash :fire::fire::fire::fire::fire:](https://github.com/getredash/redash/) - 一个 Web 应用程序，允许轻松查询现有数据库、共享数据集并以不同方式将其可视化。最初是为了与 Redshift 配合使用而开发的，并且得到了大力支持。
* [everythingMe/redshift_console](https://github.com/EverythingMe/redshift_console) - 一个用于监控和管理 Redshift 集群的简单工具。第一个版本具有用于监视正在运行的查询、WLM 队列和表/模式的基本工具。

### 53号公路

AWS 存储库：

* [route53-infima :fire::fire:](https://github.com/awslabs/route53-infima) - 管理服务级别的故障隔离。

社区回购：

* [barnybug/cli53 :fire::fire::fire::fire:](https://github.com/barnybug/cli53) - cli53 是 Amazon Route 53 的命令行工具，提供 BIND 格式的导入和导出以及 Route 53 域的简单命令行管理。
* [winebarrel/roadworker :fire::fire:](https://github.com/winebarrel/roadworker) - Roadworker 是一个管理 Route53 的工具。它使用DSL定义Route53的状态，并根据DSL更新Route53。

### S3

社区回购：

* [anomalizer/ngx_aws_auth :fire::fire:](https://github.com/anomalizer/ngx_aws_auth) - 实现经过身份验证的请求的代理。
* [bloomreach/s4cmd :fire::fire::fire::fire:](https://github.com/bloomreach/s4cmd) - S3命令行工具，对于大文件来说比S3cmd更快。
* [CulturalMe/meteor-slingshot :fire::fire::fire:](https://github.com/CulturalMe/meteor-slingshot) - 在流星中上传文件。
* [danilop/yas3fs :fire::fire::fire:](https://github.com/danilop/yas3fs) - 另一种 S3 支持的文件系统，受到 s3fs 的启发。
* [grippy/node-s3](https://github.com/grippy/node-s3) - 用于管理存储桶的 Node.js 应用程序。
* [jubos/fake-s3 :fire::fire::fire::fire::fire:](https://github.com/jubos/fake-s3) - 模拟大多数命令的轻量级 S3 克隆。
* [kahing/goofys :fire::fire::fire::fire::fire:](https://github.com/kahing/goofys) - 用 Go 编写的 Amazon S3 Filey 系统。
* [littlstar/s3renity :fire::fire::fire::fire:](https://github.com/littlstar/s3renity) - 具有并发控制的批处理函数（each、map、reduce、filter、join）
* [marcel/aws-s3 :fire::fire::fire:](https://github.com/marcel/aws-s3) - Amazon S3 REST API 的 Ruby 实现。
* [mardix/flask-cloudy :fire::fire:](https://github.com/mardix/flask-cloudy) - 烧瓶扩展。
* [MathieuLoutre/grunt-aws-s3 :fire::fire:](https://github.com/MathieuLoutre/grunt-aws-s3) - 咕噜插件。
* [mickael-kerjean/filestash :fire::fire::fire::fire::fire:](https://github.com/mickael-kerjean/filestash) - S3 的现代 Web 客户端。
* [minio/mc :fire::fire::fire::fire::fire:](https://github.com/minio/mc) - 用于文件系统和云存储的 Minio 客户端。
* [minio/minio :fire::fire::fire::fire::fire:](https://github.com/minio/minio) - 与S3兼容的对象存储服务器。
* [mumrah/s3-multipart :fire:](https://github.com/mumrah/s3-multipart) - 通过 Python 并行上传/下载到 S3。
* [ncw/rclone :fire::fire::fire::fire::fire:](https://github.com/ncw/rclone) - Rsync 适用于各种云存储提供商，例如 S3。
* [owocki/s3_disk_util :fire:](https://github.com/owocki/s3_disk_util) - S3 磁盘使用 (du) 实用程序。
* [peak/s5cmd :fire::fire::fire:](https://github.com/peak/s5cmd) - 具有通配符和批处理命令支持的快速 S3 和本地文件系统执行工具。
* [pgherveou/gulp-awspublish :fire::fire:](https://github.com/pgherveou/gulp-awspublish) - 吞咽插件。
* [rlmcpherson/s3gof3r :fire::fire::fire::fire:](https://github.com/rlmcpherson/s3gof3r) - 快速、并发、流式访问，包括 CLI。
* [s3git/s3git :fire::fire::fire::fire:](https://github.com/s3git/s3git) - CLI 工具允许您创建分布式、去中心化和版本化的存储库。
* [s3fs-fuse/s3fs-fuse :fire::fire::fire::fire::fire:](https://github.com/s3fs-fuse/s3fs-fuse) - 允许 Linux 和 Mac OS X 通过 FUSE 挂载 S3 存储桶。
* [s3tools/s3cmd :fire::fire::fire::fire::fire:](https://github.com/s3tools/s3cmd) - 用于管理 S3 和 CloudFront 的 CLI。
* [schickling/git-s3 :fire::fire:](https://github.com/schickling/git-s3) - 将您的 git 存储库部署到存储桶。
* [sorentwo/carrierwave-aws :fire::fire:](https://github.com/sorentwo/carrierwave-aws) - CarrierWave 适配器。
* [spring-projects/aws-maven :fire::fire:](https://github.com/spring-projects/aws-maven) - S3 的 Maven Wagon。
* [tongwang/s3fs-c :fire:](https://github.com/tongwang/s3fs-c) - 安装存储桶以在本地文件系统上使用。
* [mishudark/s3-parallel-put :fire::fire:](https://github.com/mishudark/s3-parallel-put) - 支持并行上传的 CLI。
* [waynehoover/s3_direct_upload :fire::fire::fire:](https://github.com/waynehoover/s3_direct_upload) - 使用 CORS 直接上传到 Amazon S3
* [weavejester/clj-aws-s3 :fire:](https://github.com/weavejester/clj-aws-s3) - Clojure 的客户端库。

### SES

社区回购：

* [drewblas/aws-ses :fire::fire::fire:](https://github.com/drewblas/aws-ses) - 提供简单的 ruby DSL 和接口。
* [microapps/MoonMail :fire::fire::fire::fire:](https://github.com/microapps/MoonMail) - 使用 SES 和 Lambda 拍摄数十亿封电子邮件。

### 简单的工作流程

AWS 存储库：

* [aws-flow-ruby :fire:](https://github.com/aws/aws-flow-ruby) - 创建后台作业和多步骤工作流程。
* [aws-flow-ruby-samples](https://github.com/awslabs/aws-flow-ruby-samples) - 适用于 Ruby 的 AWS Flow Framework 示例。
* [aws-flow-ruby-opsworks-helloworld](https://github.com/awslabs/aws-flow-ruby-opsworks-helloworld) - 你好世界样本。

社区回购：

* [Contribute](https://github.com/donnemartin/awesome-aws/blob/master/CONTRIBUTING.md)

### 简单数据库

社区回购：

* [rjrodger/simpledb :fire:](https://github.com/rjrodger/simpledb) - Node.js 库。

### 社交网络服务

AWS 存储库：

* [aws-php-sns-message-validator :fire:](https://github.com/aws/aws-php-sns-message-validator) - PHP 的消息验证。

社区回购：

* [Contribute](https://github.com/donnemartin/awesome-aws/blob/master/CONTRIBUTING.md)

### 质量安全体系

AWS 存储库：

* [amazon-sqs-java-messaging-lib :fire:](https://github.com/awslabs/amazon-sqs-java-messaging-lib) - 持有Java消息服务与SQS通信。

社区回购：

* [phstc/shoryuken :fire::fire::fire::fire:](https://github.com/phstc/shoryuken) - 一个超高效的基于 SQS 线程的 Ruby 消息处理器。

### 数据

AWS 存储库：

* [aws-data-wrangler :fire::fire::fire::fire::fire:](https://github.com/awslabs/aws-data-wrangler) - 连接 Pandas DataFrames 和 AWS 数据相关服务。

社区回购：

* [donnemartin/data-science-ipython-notebooks :fire::fire::fire::fire::fire:](https://github.com/donnemartin/data-science-ipython-notebooks) - 大数据/数据科学笔记本。
* [everpeace/vagrant-mesos :fire::fire:](https://github.com/everpeace/vagrant-mesos) - 使用 Vagrant 启动您的 Mesos 集群。
* [jhorey/ferry :fire::fire:](https://github.com/jhorey/ferry) - 使用 Docker 定义、运行和部署大数据应用程序。
* [nathanmarz/storm-deploy :fire::fire::fire:](https://github.com/nathanmarz/storm-deploy) - Storm集群的一键部署。

### 开发运营

社区回购：

* [cloud-custodian/cloud-custodian :fire::fire::fire::fire::fire:](https://github.com/cloud-custodian/cloud-custodian) - 用于管理的规则引擎，用于资源查询、过滤和操作的 yaml 中的 DSL。
* [chef-cookbooks/aws :fire::fire:](https://github.com/chef-cookbooks/aws) - aws Chef 食谱的开发存储库。
* [colinbjohnson/aws-missing-tools :fire::fire::fire::fire:](https://github.com/colinbjohnson/aws-missing-tools) - 用于管理资源的工具，包括 EC2、EBS、RDS 和 Route53。
* [k1LoW/awspec :fire::fire::fire::fire:](https://github.com/k1LoW/awspec) - RSpec 测试您的资源。
* [mitchellh/vagrant-aws :fire::fire::fire::fire::fire:](https://github.com/mitchellh/vagrant-aws) - 使用 Vagrant 管理您的 EC2 和 VPC 实例。
* [NixOS/nixops :fire::fire::fire::fire:](https://github.com/NixOS/nixops) - 使用 NixOS 来配置 EC2 实例、S3 存储桶和其他资源。

### 安全性

AWS 存储库：

* [aws-sha256-agentcs](https://github.com/awslabs/aws-sha256-agentcs) - SHA256 代理兼容性扫描仪。
* [aws-tvm-anonymous](https://github.com/awslabs/aws-tvm-anonymous) - 用于匿名注册的令牌自动售货机。
* [aws-tvm-identity](https://github.com/awslabs/aws-tvm-identity) - 用于身份注册的令牌自动售货机。
* [s2n :fire::fire::fire::fire::fire:](https://github.com/awslabs/s2n) - TLS/SSL 协议的实现。

社区回购：

* [AdRoll/hologram :fire::fire::fire:](https://github.com/AdRoll/hologram) - 在开发人员笔记本电脑上轻松、轻松地获得凭据。
* [alex/letsencrypt-aws :fire::fire::fire:](https://github.com/alex/letsencrypt-aws) - 自动配置和更新证书。
* [bridgecrewio/checkov :fire::fire::fire::fire::fire:](https://github.com/bridgecrewio/checkov) - Terraform 静态分析，验证安全最佳实践。
* [cloudsploit/scans :fire::fire::fire::fire:](https://github.com/cloudsploit/scans) - 检测安全风险。
* [iSECPartners/Scout2 :fire::fire::fire::fire:](https://github.com/iSECPartners/Scout2) - 安全审计工具。
* [jordanpotti/AWSBucketDump :fire::fire::fire::fire:](https://github.com/jordanpotti/AWSBucketDump) - 用于在 S3 存储桶中查找感兴趣文件的安全工具。
* [Netflix/bless :fire::fire::fire::fire::fire:](https://github.com/Netflix/bless) - 作为 Lambda 函数运行的 SSH 证书颁发机构。
* [Netflix/security_monkey :fire::fire::fire::fire::fire:](https://github.com/Netflix/security_monkey) - 监控策略更改并对不安全配置发出警报。
* [RiotGames/cloud-inquisitor :fire::fire:](https://github.com/RiotGames/cloud-inquisitor) - 加强所有权和数据安全的工具。
* [salesforce/policy_sentry :fire::fire::fire::fire:](https://github.com/salesforce/policy_sentry/) - IAM 最低权限策略生成器。
* [sebsto/AWSVPN :fire:](https://github.com/sebsto/AWSVPN) - 在云中启动私有 VPN 服务器。
* [trailofbits/algo :fire::fire::fire::fire::fire:](https://github.com/trailofbits/algo) - 在 EC2 和其他云服务上设置个人 IPSEC VPN。
* [ttlequals0/autovpn :fire::fire::fire::fire:](https://github.com/ttlequals0/autovpn) - 创建按需一次性 OpenVPN 端点。

### 随附的回购协议

AWS 存储库：

*伴随博客、培训活动和会议的存储库。*

* [aws-arch-backoff-simulator :fire:](https://github.com/awslabs/aws-arch-backoff-simulator) - AWS 架构博客的抖动和退避模拟器。
* [aws-big-data-blog :fire::fire::fire:](https://github.com/awslabs/aws-big-data-blog) - 来自 AWS 大数据博客的示例。
* [aws-demo-php-simple-app](https://github.com/awslabs/aws-demo-php-simple-app) - 来自 AWS 博客的 PHP 应用程序。
* [aws-mobile-sample-wif](https://github.com/awslabs/aws-mobile-sample-wif) - 来自 AWS 移动开发工具包博客的示例。
* [aws-mobile-self-paced-labs-samples](https://github.com/awslabs/aws-mobile-self-paced-labs-samples) - 来自自定进度实验室的 Android 贪吃蛇游戏。
* [aws-quickstart](https://github.com/aws-quickstart/) - AWS 快速入门的官方存储库。
* [aws-spot-labs :fire::fire::fire:](https://github.com/awslabs/aws-spot-labs) - 使用 AWS Spot 实例的最佳实践。
* [aws-training-demo :fire:](https://github.com/awslabs/aws-training-demo) - 来自技术培训师社区的演示。
* [java-meme-generator-sample](https://github.com/awslabs/java-meme-generator-sample) - re:Invent 2012 的 Meme 生成应用程序。
* [railsconf2013-tech-demo :fire:](https://github.com/awslabs/railsconf2013-tech-demo) - RailsConf 2013 的 Seahorse 演示。
* [reinvent2013-js-blog-demo](https://github.com/awslabs/reinvent2013-js-blog-demo) - 来自 re:Invent 2013 的演示博客应用程序。
* [reinvent2013-mobile-photo-share](https://github.com/awslabs/reinvent2013-mobile-photo-share) - re:Invent 2014 的移动照片共享应用程序。
* [reinvent2014-scalable-site-management](https://github.com/awslabs/reinvent2014-scalable-site-management) - re:Invent 2014 中的可扩展站点管理示例。
* [reinvent2015-dev309](https://github.com/awslabs/reinvent2015-dev309) - re:Invent 2015 的大规模指标分析。
* [timely-security-analytics](https://github.com/awslabs/timely-security-analytics) - 2015 年 re:Invent 2015 的安全分析样本。
* [todo-sample-app](https://github.com/awslabs/todo-sample-app) - 来自 RailsConf 2014 的简单“Todo”应用程序。

社区回购：

* [startup-class/setup :fire::fire:](https://github.com/startup-class/setup) - 用于启动工程 MOOC 的 EC2 设置文件。

### 杂项回购协议

AWS 存储库：

* [amediamanager](https://github.com/awslabs/amediamanager) - 媒体经理。
* [aws-hal-client-java](https://github.com/awslabs/aws-hal-client-java) - 超文本应用程序语言的 Java 客户端。
* [aws-model-validators](https://github.com/awslabs/aws-model-validators) - 用于验证 AWS 服务 JSON 模型文件的工具。
* [aws-sdk-js-sample-video-transcoder](https://github.com/awslabs/aws-sdk-js-sample-video-transcoder) - 示例跨平台视频转码器应用程序。
* [simplebeerservice :fire::fire:](https://github.com/awslabs/simplebeerservice) - 连接云的 kegerator，将实时传感器数据流式传输到 AWS。

社区回购：

* [bcoe/thumbd :fire::fire:](https://github.com/bcoe/thumbd) - 基于 Node.js/ImageMagick 的图像缩略图服务。
* [cdkpatterns/serverless :fire::fire::fire::fire:](https://github.com/cdk-patterns/serverless) - 在 AWS CDK 中构建的可部署无服务器架构模式。
* [Comcast/cmb :fire::fire:](https://github.com/Comcast/cmb) - 高可用性、水平可扩展的排队和通知服务。
* [convox/rack :fire::fire::fire::fire:](https://github.com/convox/rack) - AWS 上的开源 PaaS。
* [devops-israel/aws-inventory :fire::fire:](https://github.com/devops-israel/aws-inventory) - 在单个网页上显示您的所有 AWS 资源。
* [donnemartin/dev-setup :fire::fire::fire::fire:](https://github.com/donnemartin/dev-setup) - 各种开发人员工具和 AWS 服务的 Mac 设置。
* [dtan4/terraforming :fire::fire::fire::fire::fire:](https://github.com/dtan4/terraforming) - 将现有资源导出为 Terraform 样式（tf、tfstate）。
* [segmentio/stack :fire::fire::fire::fire::fire:](https://github.com/segmentio/stack) - 一组用于配置生产基础设施的 Terraform 模块。
* [j2labs/microarmy ](https://github.com/j2labs/microarmy) - 部署微型实例，发起协同围攻。
* [jpillora/grunt-aws :fire:](https://github.com/jpillora/grunt-aws) - Node.JS SDK 中的 Grunt 接口。
* [jvehent/haproxy-aws :fire::fire:](https://github.com/jvehent/haproxy-aws) - 有关使用 HAProxy 构建 HTTPS 堆栈的文档。
* [localstack/localstack :fire::fire::fire::fire::fire:](https://github.com/localstack/localstack) - 功能齐全的本地 AWS 云堆栈。离线开发和测试您的云应用程序！
* [meducation/propono :fire::fire:](https://github.com/meducation/propono) - Ruby 中易于使用的发布/订阅。
* [mozilla/awsbox :fire::fire::fire:](https://github.com/mozilla/awsbox) - EC2 之上的轻量级 PaaS，用于部署节点应用程序。
* [Netflix/aminator :fire::fire::fire:](https://github.com/Netflix/aminator) - 用于创建 EBS AMI 的工具。
* [Netflix/archaius :fire::fire::fire::fire::fire:](https://github.com/Netflix/archaius) - 配置管理 API 库。
* [Netflix/asgard :fire::fire::fire::fire::fire:](https://github.com/Netflix/asgard) - 用于应用程序部署和云管理的 Web 界面。
* [Netflix/aws-autoscaling :fire::fire:](https://github.com/Netflix/aws-autoscaling) - 使用自动扩展和记录最佳实践的工具。
* [Netflix/chaosmonkey :fire::fire::fire::fire::fire:](https://github.com/Netflix/chaosmonkey) - 帮助应用程序容忍随机实例故障的弹性工具。
* [Netflix/eureka :fire::fire::fire::fire::fire:](https://github.com/Netflix/eureka) - 用于弹性中间层负载平衡和故障转移的服务注册表。
* [Netflix/EVCache :fire::fire::fire::fire:](https://github.com/Netflix/EVCache) - 分布式内存数据存储。
* [Netflix/Fenzo :fire::fire::fire:](https://github.com/Netflix/Fenzo) - Mesos 框架的可扩展调度程序。
* [Netflix/ice :fire::fire::fire::fire::fire:](https://github.com/Netflix/ice) - 使用情况和成本监控工具。
* [Netflix/ribbon :fire::fire::fire::fire::fire:](https://github.com/Netflix/ribbon) - 具有内置软件负载平衡器的远程过程调用库。
* [Netflix/SimianArmy :fire::fire::fire::fire::fire:](https://github.com/Netflix/SimianArmy) - 让您的云保持最佳运行状态的工具。
* [Netflix/zuul :fire::fire::fire::fire::fire:](https://github.com/Netflix/zuul) - 提供动态路由、监控、弹性、安全性等的边缘服务。
* [niftylettuce/gulp-aws-splash :fire::fire:](https://github.com/niftylettuce/gulp-aws-splash) - 开源 LaunchRock 替代品。构建漂亮的启动页面。
* [puppetlabs/puppetlabs-aws :fire:](https://github.com/puppetlabs/puppetlabs-aws) - 用于管理资源以构建基础设施的 Puppet 模块。
* [mhart/react-server-routing-example :fire::fire:](https://github.com/mhart/react-server-routing-example) - React 中的通用客户端/服务器路由和数据示例。
* [Similarweb/finala :fire::fire::fire:](https://github.com/similarweb/finala) - 资源云扫描仪，可分析和报告浪费和未使用的资源，以减少不必要的开支。
* [snowplow/snowplow :fire::fire::fire::fire::fire:](https://github.com/snowplow/snowplow) - 企业级 Web、移动和事件分析，由 Hadoop、Kafka、Kinesis、Redshift 和 Elasticsearch 提供支持。
* [Spinnaker/spinnaker :fire::fire::fire::fire::fire:](https://github.com/Spinnaker/spinnaker) - asgard 的后继支持管道等。
* [spulec/moto :fire::fire::fire::fire::fire:](https://github.com/spulec/moto) - 允许您的 python 测试轻松模拟 boto 库。

## 指南、书籍、文档和培训

*操作方法、培训、白皮书、文档和案例研究。*

<br/>
<p对齐=“中心”>
  <img src="http://i.imgur.com/LxYDN5K.png">
</p>
<br/>

### 入门指南

AWS 指南：

* [AWS 入门](http://docs.aws.amazon.com/gettingstarted/latest/awsgsg-intro/gsg-aws-intro.html)
* [入门教程](http://docs.aws.amazon.com/gettingstarted/latest/awsgsg-intro/gsg-aws-tutorials.html)
    * [运行虚拟服务器](http://docs.aws.amazon.com/gettingstarted/latest/awsgsg-intro/gsg-aws-tutorials.html#d0e2614)
    * [存储文件](http://docs.aws.amazon.com/gettingstarted/latest/awsgsg-intro/gsg-aws-tutorials.html#d0e2683)
    * [共享数字媒体](http://docs.aws.amazon.com/gettingstarted/latest/awsgsg-intro/gsg-aws-tutorials.html#d0e2755)
    * [部署网站](http://docs.aws.amazon.com/gettingstarted/latest/awsgsg-intro/gsg-aws-tutorials.html#d0e2767)
    * [托管网站 (Linux)](http://docs.aws.amazon.com/gettingstarted/latest/awsgsg-intro/gsg-aws-tutorials.html#d0e2836)
    * [托管网站 (Windows)](http://docs.aws.amazon.com/gettingstarted/latest/awsgsg-intro/gsg-aws-tutorials.html#d0e2908)
    * [运行数据库](http://docs.aws.amazon.com/gettingstarted/latest/awsgsg-intro/gsg-aws-tutorials.html#d0e2980)
    * [分析您的数据](http://docs.aws.amazon.com/gettingstarted/latest/awsgsg-intro/gsg-aws-tutorials.html#d0e3065)

社区指南：

* [Contribute](https://github.com/donnemartin/awesome-aws/blob/master/CONTRIBUTING.md)

### 一般指南

AWS 指南：

* [分析大数据](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-gs.html)
* [使用 AWS 管理控制台](http://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/getting-started.html)
* [使用 Elastic Beanstalk 部署 Web 应用程序](http://docs.aws.amazon.com/gettingstarted/latest/deploy/overview.html)
* [托管 Web 应用程序](http://docs.aws.amazon.com/gettingstarted/latest/wah-linux/web-app-hosting-intro.html)
* [托管 .NET Web 应用程序](http://docs.aws.amazon.com/gettingstarted/latest/wah/web-app-hosting-intro.html)
* [托管静态网站](http://docs.aws.amazon.com/gettingstarted/latest/swh/website-hosting-intro.html)
* [快速入门部署指南](https://aws.amazon.com/documentation/quickstart/)

社区指南：

* [打开 AWS 指南:fire::fire::fire::fire::fire:](https://github.com/open-guides/og-aws)

### 书籍

* Amazon Web Services 实际应用 [Manning](https://www.manning.com/books/amazon-web-services-in-action) 或 [Amazon.com](http://amzn.com/1617292885)
* AWS Lambda 实际应用 [Manning](https://www.manning.com/books/aws-lambda-in-action) 或 [Amazon.com](http://amzn.com/1617293717) - [代码库 :fire::fire:](https://github.com/danilop/AWS_Lambda_in_Action)

### 白皮书

* [AWS 架构完善的框架](https://d0.awsstatic.com/whitepapers/architecture/AWS_Well-Architected_Framework.pdf)
* [Whitepapers](https://aws.amazon.com/whitepapers/)

### 文档

* [Documentation](https://aws.amazon.com/documentation/)
* [AWS 计费和成本管理](https://aws.amazon.com/documentation/account-billing/)
* [AWS 市场](https://aws.amazon.com/documentation/marketplace/)
* [AWS 支持](https://aws.amazon.com/documentation/aws-support/)
* [AWS 一般参考](http://docs.aws.amazon.com/general/latest/gr/)
* [AWS 术语表](http://docs.aws.amazon.com/general/latest/gr/glos-chap.html)

### 培训

* [培训和认证](https://aws.amazon.com/training/)
* [Webinars](https://aws.amazon.com/about-aws/events/)

### 案例研究：由 AWS 提供支持

* [Adobe](https://aws.amazon.com/solutions/case-studies/adobe/)
* [AdRoll](https://aws.amazon.com/solutions/case-studies/adroll/)
* [Airbnb](https://aws.amazon.com/solutions/case-studies/airbnb/)
* [Autodesk](https://aws.amazon.com/solutions/case-studies/autodesk/)
* [Citrix](https://aws.amazon.com/solutions/case-studies/citrix/)
* [Comcast](https://aws.amazon.com/solutions/case-studies/comcast/)
* [Coursera](https://aws.amazon.com/solutions/case-studies/coursera/)
* [Docker](https://aws.amazon.com/solutions/case-studies/docker/)
* [道琼斯](https://aws.amazon.com/solutions/case-studies/dow-jones/)
* [Dropbox](https://www.dropbox.com/)
* [Dropcam](https://aws.amazon.com/solutions/case-studies/dropcam/)
* [Expedia](https://aws.amazon.com/solutions/case-studies/expedia/)
* [Foursquare](https://aws.amazon.com/solutions/case-studies/foursquare/)
* [IMDb](https://aws.amazon.com/solutions/case-studies/imdb/)
* [Instrumental](https://instrumentalapp.com/blog/aws-kinesis/)
* [Intuit](https://aws.amazon.com/solutions/case-studies/soasta-intuit/)
* [强生公司](https://aws.amazon.com/solutions/case-studies/johnson-and-johnson/)
* [Lionsgate](https://aws.amazon.com/solutions/case-studies/lionsgate/)
* [mlbam](https://aws.amazon.com/solutions/case-studies/major-league-baseball-mlbam/)
* [NASA](https://aws.amazon.com/solutions/case-studies/nasa-jpl-curiosity/)
* [Netflix](https://aws.amazon.com/solutions/case-studies/netflix/)
* [Nike](https://web.archive.org/web/20150910200649/http://aws.amazon.com/solutions/case-studies/nike/)
* [Nokia](https://web.archive.org/web/20161210062336/https://aws.amazon.com/solutions/case-studies/nokia/)
* [PBS](https://aws.amazon.com/solutions/case-studies/pbs/)
* [Pfizer](https://web.archive.org/web/20161210034734/https://aws.amazon.com/solutions/case-studies/pfizer/)
* [Philips](https://aws.amazon.com/solutions/case-studies/philips/)
* [Reddit](https://web.archive.org/web/20150905070945/https://aws.amazon.com/solutions/case-studies/reddit/)
* [Samsung](https://aws.amazon.com/solutions/case-studies/samsung/)
* [Siemens](https://aws.amazon.com/solutions/case-studies/siemens/)
* [Slack](https://aws.amazon.com/solutions/case-studies/slack/)
* [Spotify](https://web.archive.org/web/20180608043124/https://aws.amazon.com/solutions/case-studies/spotify/)
* [Swiftkey](https://web.archive.org/web/20160410051253/https://aws.amazon.com/solutions/case-studies/swiftkey/)
* [天气公司](https://aws.amazon.com/solutions/case-studies/the-weather-company/)
* [Ticketmaster](https://aws.amazon.com/solutions/case-studies/ticketmaster/)
* [时代公司](https://aws.amazon.com/solutions/case-studies/time-inc/)
* [Twilio](https://aws.amazon.com/solutions/case-studies/twilio/)
* [美国国务院](https://aws.amazon.com/solutions/case-studies/exchangesconnect/)
* [Ubisoft](https://aws.amazon.com/solutions/case-studies/ubisoft/)
* [Yelp](https://aws.amazon.com/solutions/case-studies/yelp-docker/)
* [Zillow](https://aws.amazon.com/solutions/case-studies/zillow/)

## 社交

*博客、讨论组、会议和社交媒体。*

<br/>
<p对齐=“中心”>
  <img src="http://i.imgur.com/kRRBa1e.png">
</p>
<br/>

### 博客

AWS 博客：

* [官方博客](https://aws.amazon.com/blogs/aws/)
    * [Brasil](https://aws.amazon.com/pt/blogs/aws-brasil/)
    * [China](https://aws.amazon.com/cn/blogs/china/)
    * [Germany](https://aws.amazon.com/de/blogs/germany/)
    * [Japan](https://aws.amazon.com/jp/blogs/news/)
    * [Korea](http://aws.amazon.com/ko/blogs/korea/)
* [DevOps](https://aws.amazon.com/blogs/devops/)
* [Architecture](https://aws.amazon.com/blogs/architecture/)
* [大数据](https://aws.amazon.com/blogs/big-data/)
* [Compute](https://aws.amazon.com/blogs/compute/)
* [Mobile](https://aws.amazon.com/blogs/mobile/)
* [Messaging](https://aws.amazon.com/blogs/messaging-and-targeting/)
* [Java](https://aws.amazon.com/blogs/developer/category/programing-language/java/)
* [PHP](https://aws.amazon.com/blogs/developer/category/programing-language/php/)
* [Ruby](https://aws.amazon.com/blogs/developer/category/programing-language/ruby/)
* [.NET](https://aws.amazon.com/blogs/developer/category/programing-language/dot-net/)
* [Security](https://aws.amazon.com/blogs/security/)
* [Startup](https://medium.com/aws-activate-startup-blog)
* [合作伙伴网络](https://aws.amazon.com/blogs/apn/)
* [SAP](https://aws.amazon.com/blogs/awsforsap/)

社区博客：

* [All Things Distributed](http://www.allthingsdistributed.com/) - Werner Vogels，AWS 首席技术官。
* [Things I Like...](http://jeff-barr.com/) - Jeff Barr，AWS 首席布道师。
* [Netflix 技术博客](http://techblog.netflix.com/)
* [工程博客精选列表](https://github.com/kilimchoi/engineering-blogs)
* [AWS 极客](https://www.awsgeek.com/)

### 推特影响者

AWS 推文：

* [@awscloud](https://twitter.com/awscloud) - 官方 Twitter 源。
* [@AWS_Partners](https://twitter.com/AWS_Partners)
* [@AWSIdentity](https://twitter.com/AWSIdentity)
* [@AWSMarketplace](https://twitter.com/AWSMarketplace)
* [@AWSreInvent](https://twitter.com/AWSreInvent) - re:Invent 的官方 Twitter 帐户。
* [@AWSStartups](https://twitter.com/AWSStartups)
* [@ajassy](https://twitter.com/ajassy) - 安迪·贾西：高级副总裁。
* [@Ianmmmm](https://twitter.com/Ianmmmm) - Ian Massingham - 技术传播者。
* [@jeffbarr](https://twitter.com/jeffbarr) - 杰夫·巴尔：首席布道者。
* [@mndoci](https://twitter.com/mndoci) - 迪帕克·辛格：EC2 总经理。
* [@mza](https://twitter.com/mza) - 马特·伍德：产品策略。
* [@Werner](https://twitter.com/Werner) - 沃纳·沃格尔斯：首席技术官。
* [社区英雄、布道者等](https://twitter.com/awscloud/lists)

社区推文：

* [@kennwhite](https://twitter.com/kennwhite)
* [@esh](https://twitter.com/esh)
* [@garnaat](https://twitter.com/garnaat)
* [@quinnypig](https://twitter.com/quinnypig)
* [@awsgeek](https://twitter.com/awsgeek)

### 脸书页面

AWS 页面：

* [amazonwebservices](https://www.facebook.com/amazonwebservices) - 官方脸书页面。
* [awsreinvent](https://www.facebook.com/awsreinvent) - re:Invent 的官方 Facebook 页面。

社区页面：

* [Contribute](https://github.com/donnemartin/awesome-aws/blob/master/CONTRIBUTING.md)

### YouTube 频道

AWS 渠道：

* [AmazonWebServices](https://www.youtube.com/user/AmazonWebServices)
* [AWSDeutsch](https://www.youtube.com/user/AWSAktuell)
* [AWSJapan](https://www.youtube.com/user/AmazonWebServicesJP)
* [AWSKorea](https://www.youtube.com/user/AWSKorea)
* [AWSLatinAmerica](https://www.youtube.com/channel/UCvaUAVzIIGsRNlUDWkQFCeA)
* [AWSTutorialSeries](https://www.youtube.com/user/awstutorialseries)
* [AWSWebinars](https://www.youtube.com/user/AWSwebinars)

社区渠道：

* [退格学院](https://www.youtube.com/channel/UCav3fsasRc5VOqvZiT5avgw)
* [云学院](https://www.youtube.com/channel/UCeRY0LppLWdxWAymRANTb0g/videos)
* [Linux学院](https://www.youtube.com/user/pineheadtv/playlists)

### 领英群组

AWS 页面：

* [亚马逊网络服务](https://www.linkedin.com/company/amazon-web-services)

社区团体：

* [亚马逊 AWS 架构师](https://www.linkedin.com/grp/home?gid=4387417)
* [亚马逊 AWS 架构师、工程师、开发人员、顾问、企业家专家](https://www.linkedin.com/grps?gid=3748455)
* [适用于企业的亚马逊网络服务 (AWS)](https://www.linkedin.com/grps?gid=5122002)
* [亚马逊网络服务架构师](https://www.linkedin.com/grps?gid=4233997)
* [亚马逊网络服务社区网络](https://www.linkedin.com/grp/home?gid=49531)
* [亚马逊网络服务爱好者](https://www.linkedin.com/grps?gid=2485626)
* [亚马逊网络服务用户](https://www.linkedin.com/grps?gid=86137)

### 子版块

* [/r/aws/](https://www.reddit.com/r/aws/)
* [/r/AWS_cloud/](https://www.reddit.com/r/AWS_cloud/)

### 会议

AWS 会议：

* [re:Invent](https://reinvent.awsevents.com/) - 年度用户大会。该活动包括主题演讲、培训和认证机会、超过 250 场技术会议、合作伙伴博览会、下班后活动等。
* [Summits](https://aws.amazon.com/summits/) - 全球一日活动旨在向新客户介绍 AWS 平台，并为现有客户提供深入的技术内容，帮助他们利用 AWS 取得更大成功。
* [AWSome Day](https://aws.amazon.com/events/awsome-day/awsome-day-online/) - 全球一日活动由 AWS Education 的技术讲师授课，非常适合想要了解如何开始使用 AWS 云的 IT 专业人员、开发人员和技术经理。

社区会议：

* [Contribute](https://github.com/donnemartin/awesome-aws/blob/master/CONTRIBUTING.md)

## 最新 KPI 和统计数据

*最新关键绩效指标和其他有趣的统计数据。*

<br/>
<p对齐=“中心”>
  <img src="http://i.imgur.com/KP2TmJv.png">
</p>
<br/>

* 过去 30 天内有超过 100 万活跃客户。<sup>[1](https://www.youtube.com/watch?v=D5-ifl7KJ00)</sup>
* 年收入运行率超过 70 亿美元的业务。<sup>[1](https://www.youtube.com/watch?v=D5-ifl7KJ00)</sup>
* 收入同比增长 81%。<sup>[1](https://www.youtube.com/watch?v=D5-ifl7KJ00)</sup>
* EC2 使用率同比增长 95%。<sup>[1](https://www.youtube.com/watch?v=D5-ifl7KJ00)</sup>
* S3 数据传输量同比增长 120%。<sup>[1](https://www.youtube.com/watch?v=D5-ifl7KJ00)</sup>
* S3 拥有数万亿个对象，并且经常达到每秒 150 万个请求的峰值。<sup>[2](http://highscalability.com/blog/2015/1/12/the-stunning-scale-of-aws-and-what-it-means-for-the-future-o.html)</sup>
* 数据库服务使用量同比增长 127%。<sup>[1](https://www.youtube.com/watch?v=D5-ifl7KJ00)</sup>
* 年收入运行率为 10 亿美元的业务。<sup>[1](https://www.youtube.com/watch?v=D5-ifl7KJ00)</sup>
* 每天创建 200 万个新 EBS 卷。<sup>[4](https://www.youtube.com/watch?v=OuyUbvtgfDk)</sup>
* 客户已启动超过 1500 万个 Hadoop 集群。<sup>[3](http://www.forbes.com/sites/benkepes/2014/11/25/scale-beyond-compressive-some-aws-numbers/)</sup>
* 为数据中心提供 102Tbps 网络容量。<sup>[2](http://highscalability.com/blog/2015/1/12/the-stunning-scale-of-aws-and-what-it-means-for-the-future-o.html)</sup>
* 自 2014 年以来推出了 500 多项主要新功能和服务。<sup>[1](https://www.youtube.com/watch?v=D5-ifl7KJ00)</sup>
* 所有其他 14 家云提供商的总容量是 AWS 的 1/5。<sup>[2](http://highscalability.com/blog/2015/1/12/the-stunning-scale-of-aws-and-what-it-means-for-the-future-o.html)</sup>
* 每天，AWS 都会增加足够的新服务器容量来支持亚马逊的所有全球基础设施，当时亚马逊还是年收入 70 亿美元的企业（2004 年）。<sup>[2](http://highscalability.com/blog/2015/1/12/the-stunning-scale-of-aws-and-what-it-means-for-the-future-o.html)</sup>

## 核心服务附录

*官方服务附录，按服务类别分组。*

### 简单英语服务

* [Amazon Web Services in Plain English](https://www.expeditedssl.com/aws-in-plain-english) - 娱乐性和教育性，社区贡献。

### 计算服务

* [Auto Scaling](https://aws.amazon.com/autoscaling/) - 根据策略、计划和运行状况检查启动或终止 EC2 实例。
* [Batch](https://aws.amazon.com/batch/) - 大规模运行批处理作业。
* [Blox](https://blox.github.io/) - 用于在 ECS 上构建自定义调度程序的开源项目。
* [EC2 Container Service (ECS)](https://aws.amazon.com/ecs/) - 支持 EC2 实例上的 Docker 容器。
* [EC2 Systems Manager](https://aws.amazon.com/ec2/systems-manager/) - 轻松配置和管理 EC2 和本地系统。
* [Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/) - 提供云中应用程序的快速部署和管理。
* [Elastic Compute Cloud (EC2)](http://aws.amazon.com/ec2/) - 使用 Xen 提供可扩展的虚拟专用服务器。
* [Elastic GPUs](https://aws.amazon.com/ec2/Elastic-GPUs/) - 将低成本 GPU 连接到 EC2 实例以实现图形加速。
* [Elastic Load Balancing (ELB)](https://aws.amazon.com/elasticloadbalancing/) - 自动在多个 EC2 实例之间分配传入流量。
* [Lambda](https://aws.amazon.com/lambda/) - 运行代码以响应事件并自动管理 EC2 实例。
* [Lightsail](https://amazonlightsail.com/) - 启动和管理简单的虚拟专用服务器。
* [Virtual Private Cloud (VPC)](https://aws.amazon.com/vpc/) - 创建一组逻辑上隔离的 EC2 实例，这些实例可以使用 VPN 连接连接到现有网络。

### 网络服务

* [Direct Connect](https://aws.amazon.com/directconnect/) - 提供与 AWS 的专用连接，以实现更快、更便宜的数据吞吐量。
* [Elastic Load Balancing (ELB)](https://aws.amazon.com/elasticloadbalancing/) - 自动在多个 EC2 实例之间分配传入流量。
* [Route 53](https://aws.amazon.com/route53/) - 提供高度可用且可扩展的域名系统 (DNS) Web 服务。
* [Virtual Private Cloud (VPC)](https://aws.amazon.com/vpc/) - 创建一组逻辑上隔离的 EC2 实例，这些实例可以使用 VPN 连接连接到现有网络。

### 企业应用

* [WorkDocs](https://aws.amazon.com/workdocs/) - 提供完全托管、安全的企业存储和共享服务。
* [WorkMail](https://aws.amazon.com/workmail/) - 提供托管电子邮件和日历服务。
* [WorkSpaces](https://aws.amazon.com/workspaces/) - 为最终用户提供基于云的桌面体验。
* [Workspaces Application Manager (WAM)](http://aws.amazon.com/workspaces/applicationmanager/) - 简化 WorkSpaces 的部署和管理。

### 分析服务

* [Athena](https://aws.amazon.com/athena/) - 即时查询S3上的数据。
* [Data Pipeline](https://aws.amazon.com/datapipeline/) - 通过在服务之间处理和移动数据来提供工作负载管理。
* [Elastic MapReduce (EMR)](http://aws.amazon.com/elasticmapreduce/) - 托管在 EC2 和 S3 上运行的 Hadoop 和 Spark 框架。
* [Elasticsearch Service (ES)](https://aws.amazon.com/elasticsearch-service/) - 托管 Elasticsearch，一种流行的开源搜索和分析引擎。
* [Glue](https://aws.amazon.com/glue/) - 准备数据并将其加载到数据存储中。
* [Kinesis](https://aws.amazon.com/kinesis/) - 提供对大型分布式数据流的实时数据处理。
* [Kinesis Analytics](https://aws.amazon.com/kinesis/analytics/) - 对流数据编写标准 SQL 查询，而无需学习任何新的编程技能。
* [Kinesis Firehose](https://aws.amazon.com/kinesis/firehose/) - 捕获流数据并将其自动加载到 S3 和 Redshift 中。
* [Quicksight](https://aws.amazon.com/quicksight/) - 提供云驱动的商业智能，成本仅为传统 BI 解决方案的 1/10。
* [Redshift](https://aws.amazon.com/redshift/) - 提供具有列式存储和多节点计算的 PB 级数据仓库。

### 人工智能

* [Lex](https://aws.amazon.com/lex/) - 通过语音或文本构建对话界面。
* [Machine Learning](https://aws.amazon.com/machine-learning/) - 提供托管机器学习技术。
* [Polly](https://aws.amazon.com/polly/) - 将文本变成栩栩如生的语音。
* [Rekognition](https://aws.amazon.com/rekognition/) - 基于深度学习的图像分析。

### 管理工具

* [CloudFormation](https://aws.amazon.com/cloudformation/) - 提供基于文件的接口来配置其他资源。
* [CloudTrail](https://aws.amazon.com/cloudtrail/) - 提供所有活动的日志。
* [CloudWatch](https://aws.amazon.com/cloudwatch/) - 从 EC2 开始，提供对 AWS 云资源和应用程序的监控。
* [Command Line Interface (CLI)](https://aws.amazon.com/cli/) - 提供 CLI 来管理所有服务。
* [Config](https://aws.amazon.com/config/) - 提供所有资源的详细视图。
* [Management Console (AWS Console)](https://aws.amazon.com/console/) - 用于管理所有服务的基于 Web 的界面。
* [OpsWorks](https://aws.amazon.com/opsworks/) - 使用 Chef 提供 EC2 服务的配置。
* [Personal Health Dashboard](https://aws.amazon.com/premiumsupport/phd/) - 您对服务健康状况的个性化视图。
* [Service Catalog](https://aws.amazon.com/servicecatalog/) - 服务目录允许 IT 管理员创建、管理批准的产品组合并将其分发给最终用户，然后最终用户可以在个性化门户中访问所需的产品。

### 安全和身份服务

* [Certificate Manager](https://aws.amazon.com/certificate-manager/) - 让您可以轻松预置、管理和部署 SSL/TLS 证书以用于 AWS 服务。
* [CloudHSM](https://aws.amazon.com/cloudhsm/) - 通过在 AWS 云中使用专用硬件安全模块 (HSM) 设备，帮助满足数据安全方面的企业、合同和法规合规性要求。
* [Directory Service](https://aws.amazon.com/directoryservice/) - 一种托管服务，允许您将资源与现有的本地 Microsoft Active Directory 连接或在 AWS 云中设置新的独立目录。
* [Identity and Access Management (IAM)](https://aws.amazon.com/iam/) - 隐式服务，用于验证对各种服务的访问的身份验证基础结构。
* [Inspector](https://aws.amazon.com/inspector/) - 自动化安全评估服务，有助于提高部署在 AWS 上的应用程序的安全性和合规性。
* [Key Management Service (KMS)](https://aws.amazon.com/kms/) - 一种托管服务，可让您轻松创建和控制用于加密数据的加密密钥。
* [Shield](https://aws.amazon.com/shield/) - 托管 DDoS 防护。
* [WAF](https://aws.amazon.com/waf/) - 用于监控和管理 CloudFront 发行版的 Web 应用程序防火墙服务。

### 物联网服务

* [IoT](https://aws.amazon.com/iot/) - 通过 MQTT 和 HTTP，在联网物体（例如传感器、执行器、嵌入式设备或智能设备）与 AWS 云之间实现安全、双向通信。

### 流动服务

* [API Gateway](https://aws.amazon.com/api-gateway/) - 用于发布、维护和保护 Web 服务 API 的服务。
* [Cognito](https://aws.amazon.com/cognito/) - 提供用户身份和数据同步。
* [Device Farm](https://aws.amazon.com/device-farm/) - 针对物理设备上的 iOS、Android 和 Fire OS 应用程序的应用程序测试服务。
* [Mobile Analytics](https://aws.amazon.com/mobileanalytics/) - 用于收集、可视化和理解应用程序使用数据的服务。
* [Mobile Hub](https://aws.amazon.com/mobile/) - 提供集成控制台，帮助您构建、测试和监控移动应用程序。
* [Pinpoint](https://aws.amazon.com/pinpoint/) - 移动应用程序的定向推送通知。
* [Simple Notification Service (SNS)](https://aws.amazon.com/sns/) - 为应用程序提供托管的多协议“推送”消息传递。

### 存储和内容交付服务

* [CloudFront](https://aws.amazon.com/cloudfront/) - 用于将对象分发到请求者附近的位置的内容分发网络 (CDN)。
* [Elastic Block Store (EBS)](https://aws.amazon.com/ebs/) - 为 EC2 提供持久的块级存储卷。
* [Elastic File System (EFS)](https://aws.amazon.com/efs/) - EC2 实例的文件存储服务。
* [Glacier](https://aws.amazon.com/glacier/) - 提供低成本、长期存储选项，用于归档数据。
* [Import/Export](https://aws.amazon.com/importexport/) - 使用便携式存储设备进行传输，加速将大量数据移入和移出 AWS。
* [Simple Storage Service (S3)](https://aws.amazon.com/s3/) - 提供基于Web 服务的存储。
* [Storage Gateway](https://aws.amazon.com/storagegateway/) - 具有基于云的备份功能的 iSCSI 块存储虚拟设备。

### 数据库

* [Aurora](https://aws.amazon.com/rds/aurora/) - MySQL 和 PostgreSQL 兼容关系数据库，性能得到改进。
* [DynamoDB](https://aws.amazon.com/dynamodb/) - 提供由 SSD 支持的可扩展、低延迟的 NoSQL 在线数据库服务。
* [ElastiCache](https://aws.amazon.com/elasticache/) - 为 Web 应用程序提供内存缓存（Memcached、Redis）。
* [Redshift](https://aws.amazon.com/redshift/) - 提供具有列式存储和多节点计算的 PB 级数据仓库。
* [Relational Database Service (RDS)](https://aws.amazon.com/rds/) - 提供可扩展的数据库服务器，支持 MySQL、Oracle、SQL Server、PostgreSQL 和 MariaDB。
* [Schema Conversion Tool](https://aws.amazon.com/documentation/SchemaConversionTool/) - 可帮助您将数据库架构从 Oracle 或 Microsoft SQL Server 数据库转换为 RDS MySQL 数据库实例或 Aurora 数据库集群的应用程序。
* [SimpleDB](https://aws.amazon.com/simpledb/) - 允许开发人员对结构化数据运行查询。

### 申请服务

* [API Gateway](https://aws.amazon.com/api-gateway/) - 用于发布、维护和保护 Web 服务 API 的服务。
* [AppStream](https://aws.amazon.com/appstream/) - 适用于应用程序和游戏的灵活、低延迟的流媒体服务。
* [CloudSearch](https://aws.amazon.com/cloudsearch/) - 提供基本的全文搜索和文本内容索引。
* [DevPay](https://aws.amazon.com/devpay/) - 提供计费和帐户管理。
* [Elastic Transcoder (ETS)](https://aws.amazon.com/elastictranscoder/) - 提供 S3 托管视频的视频转码。
* [Flexible Payments Service (FPS)](https://payments.amazon.com/developer) - 提供小额支付接口。
* [Simple Email Service (SES)](https://aws.amazon.com/ses/) - 提供批量和事务性电子邮件发送。
* [Simple Notification Service (SNS)](https://aws.amazon.com/sns/) - 为应用程序提供托管的多协议“推送”消息传递。
* [Simple Queue Service (SQS)](https://aws.amazon.com/sqs/) - 为 Web 应用程序提供托管消息队列。
* [Simple Workflow (SWF)](https://aws.amazon.com/swf/) - 用于构建可扩展、有弹性的应用程序的工作流服务。
* [Step Functions](https://aws.amazon.com/step-functions/) - 协调分布式应用程序的组件。

### 开发者工具

* [CodeBuild](https://aws.amazon.com/codebuild/) - 构建并测试代码。
* [CodeCommit](https://aws.amazon.com/documentation/codecommit/) - 托管 Git 版本控制服务。
* [CodeDeploy](https://aws.amazon.com/codedeploy/) - 提供到 EC2 实例的自动代码部署。
* [CodePipeline](https://aws.amazon.com/documentation/codepipeline/) - 持续交付服务。
* [Command Line Interface (CLI)](https://aws.amazon.com/cli/) - 提供 CLI 来管理所有服务。
* [X-Ray](https://aws.amazon.com/xray/) - 分析和调试您的应用程序。

### 杂项服务

* [Fulfillment Web Service](https://aws.amazon.com/about-aws/whats-new/2008/03/19/announcing-amazon-fulfillment-web-service/) - 为卖家提供编程式 Web 服务，以便使用亚马逊配送将商品往返亚马逊。
* [Mechanical Turk](https://www.mturk.com/mturk/welcome) - 管理分配给多人的小型工作单元。
* [Partner Network (APN)](https://aws.amazon.com/partners/) - 为合作伙伴提供技术信息以及销售和营销支持，以增加商机。
* [Product Advertising API](http://docs.aws.amazon.com/AWSECommerceService/latest/GSG/Welcome.html) - 提供对产品数据和电子商务功能的访问。

## 制作人员

查看[制作人员名单](https://github.com/donnemartin/awesome-aws/blob/master/CREDITS.md)。

## 其他很棒的清单

其他很棒的列表可以在 [awesome](https://github.com/sindresorhus/awesome) 和 [awesome-awesomeness](https://github.com/bayandin/awesome-awesomeness) 中找到。

## 联系方式

请随时与我联系讨论任何问题、疑问或意见。

我的联系信息可以在我的 [GitHub 页面](https://github.com/donnemartin) 上找到。

## 许可证

*我根据开源许可证向您提供此存储库中的代码和资源。  因为这是我的个人存储库，所以您收到的我的代码和资源的许可证来自我，而不是我的雇主 (Facebook)。*

版权所有 2017 唐恩·马丁

知识共享归属 4.0 国际许可 (CC BY 4.0)

    http://creativecommons.org/licenses/by/4.0/
