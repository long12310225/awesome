# 很棒的 OpenTofu <!-- 在目录中省略 --> [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> 精彩的 OpenTofu 资源和工具的精选协作列表。

[OpenTofu](https://opentofu.org/) 允许您以声明方式管理您的基础设施。它是 Terraform 的开源、社区驱动的替代方案。

## 内容 <!-- 目录中省略 -->

- [Official](#official)
- [Community](#community)
- [Features](#features)
- [Tools](#tools)
  - [环境管理者](#environment-managers)
  - [Wrappers](#wrappers)
  - [CI](#ci)
  - [Tests](#tests)
  - [State](#state)
  - [Providers](#providers)
  - [Platforms](#platforms)
  - [Registry](#registry)
  - [Helpers](#helpers)
- [Learning](#learning)
- [Media](#media)
- [Podcasts](#podcasts)

## 官方

- [OpenTofu 存储库](https://github.com/opentofu/opentofu) 🎉
- [分叉公告](https://opentofu.org/announcement)
- [Registry](https://github.com/opentofu/registry)
- [注册 MCP 服务器](https://github.com/opentofu/opentofu-mcp-server#opentofu-mcp-server)
- [每周更新](https://github.com/opentofu/opentofu/discussions/categories/weekly-updates)
- [办公时间](https://www.youtube.com/watch?v=aEoMzUza6Ok&list=PLnVotLM2QsyhCc1_8PA7fbVF-ixt4_XAY)
- [技术指导委员会更新](https://github.com/opentofu/org/tree/main/TSC)

## 社区

*沟通渠道、聚会、新闻通讯和论坛。*

- [OpenTofu GitHub 讨论](https://github.com/orgs/opentofu/discussions)
- [OpenTofu 领英](https://www.linkedin.com/company/opentofuorg/)
- [OpenTofu Slack](https://opentofu.org/slack)
- [OpenTofu 推特](https://twitter.com/opentofuorg)

## 特点

<!--lint disable double-link-->

- [1.10 - 增强的移动和删除块](https://opentofu.org/docs/v1.10/intro/whats-new/#enhanced-moved-and-removed-blocks)
- [1.10 - 外部密钥提供商](https://opentofu.org/docs/v1.10/intro/whats-new/#external-key-providers)
- [1.10 - OCI 注册表支持](https://opentofu.org/docs/cli/oci_registries/)
- [1.10 - S3 本机状态锁定](https://opentofu.org/docs/v1.10/intro/whats-new/#native-s3-state-locking)
- [1.10 - 定位和排除文件](https://opentofu.org/docs/v1.10/intro/whats-new/#target-and-exclude-files)
- [1.9 - 使用 for_each 进行提供者迭代](https://opentofu.org/docs/v1.9/intro/whats-new/#provider-iteration-for_each)
- [1.9 - -exclude 标志](https://opentofu.org/docs/v1.9/intro/whats-new/#the--exclude-flag)
- [1.8 - 早期变量和局部变量评估](https://opentofu.org/docs/v1.8/intro/whats-new/#early-variablelocals-evaluation)
- [1.8 - 覆盖 OpenTofu (.tofu) 文件](https://opentofu.org/docs/v1.8/intro/whats-new/#override-files-for-opentofu-keeping-compatibility)
- [1.7 - 状态文件的端到端加密](https://opentofu.org/docs/v1.7/intro/whats-new/#state-encryption)
- [1.7 - 可循环导入块](https://opentofu.org/docs/v1.7/intro/whats-new/#loopable-import-blocks)
- [1.7 - 提供者定义的函数](https://opentofu.org/docs/v1.7/intro/whats-new/#provider-defined-functions)
- [1.7 - 移除方块](https://opentofu.org/docs/v1.7/intro/whats-new/#removed-block)
- [CanI.TF - Terraform 和 OpenTofu 之间的功能对等](https://cani.tf/)

<!--lint enable double-link-->

## 工具

### 环境管理者

- [arkade](https://github.com/alexellis/arkade) - CLI 和 Kubernetes 应用程序安装程序。
- [asdf-opentofu](https://github.com/virtualroot/asdf-opentofu) - asdf 版本管理器的 OpenTofu 插件。
- [tenv](https://github.com/tofuutils/tenv) - 用 Go 编写的 Terraform 和 OpenTofu 版本管理器。
- [tfswitcher](https://github.com/ASleepyCat/tfswitcher) - 用 Rust 编写的 Terraform 和 OpenTofu 版本切换器。
- [tofuenv](https://github.com/tofuutils/tofuenv) - OpenTofu 版本管理器受 tfenv 启发。

### 包装纸

*使用薄包装简化您的 OpenTofu 工作流程。*

- [Atmos](https://github.com/cloudposse/atmos) - 保持环境配置干燥的编排工具。
- [Terragrunt](https://github.com/gruntwork-io/terragrunt) - 保持配置干燥、使用多个模块并管理远程状态。
- [Terramate](https://github.com/terramate-io/terramate) - OpenTofu、Terraform、Kubernetes 等的自动化、编排和代码生成。
- [easy_infra](https://github.com/SeisoLLC/easy_infra) - Docker 容器可简化和安全地使用基础设施即代码。
- [pug](https://github.com/leg100/pug) - 面向高级用户的终端用户界面。
- [tf](https://github.com/dex4er/tf) - 更简洁、更友好的命令输出。
- [tfam](https://github.com/Ant0wan/tfam) - Rust 支持的并发 Terraform/OpenTofu 包装器应用，支持多部署。
- [tfexe](https://github.com/Ant0wan/tfexe) - Rust 支持的包装器，用于通过版本控制无缝执行 tfswitch 和 Terraform/OpenTofu。
- [tfwrapper](https://github.com/claranet/tfwrapper) - Python 包装器可简化 OpenTofu 的使用并实施最佳实践。

### CI

- [Atlantis](https://www.runatlantis.io/) - 通过拉取请求自动化工作流程。
- [Burrito](https://docs.burrito.tf/latest/overview/) - 在 Kubernetes 内运行的 TACoS（Terraform 自动化和协作软件）。
- [drifthound](https://github.com/treezio/drifthound) - 通过历史跟踪和通知进行连续基础设施偏差检测。
- [TF-via-PR](https://github.com/OP5dev/TF-via-PR) - GitHub Action 通过 PR 自动化来初始化、规划和应用 Terraform/OpenTofu。
- [pre-commit-opentofu](https://github.com/tofuutils/pre-commit-opentofu) - Git 预提交挂钩插件。
- [setup-opentofu](https://github.com/opentofu/setup-opentofu) - 在 GitHub Actions 工作流程中设置 OpenTofu CLI。
- [terraform-github-actions](https://github.com/dflook/terraform-github-actions) - OpenTofu 的 GitHub 操作。
- [tofu-controller](https://github.com/flux-iac/tofu-controller) - 适用于 Flux 的 GitOps OpenTofu 和 Terraform 控制器。
- [tofUI](https://github.com/65156/tofUI) - 以 HTML 格式轻松导出 OpenTofu 和 Terraform 计划，以获得更好的可读性。

### 测试

- [Terratest](https://github.com/gruntwork-io/terratest) - Go 库可以让您更轻松地为基础设施代码编写自动化测试。

### 状态

*分析和操作 OpenTofu 的状态。*

- [tfmigrate](https://github.com/minamijoyo/tfmigrate) - 状态迁移工具。
- [tfimport](https://github.com/coolapso/tfimport) - 自动化状态导入的工具。

### 供应商

*检查 OpenTofu 提供商并与之互动。*

- [tfschema](https://github.com/minamijoyo/tfschema) - 提供商的架构检查器。

### 平台

*Terraform Cloud 的替代品。*

- [digger](https://github.com/diggerhq/digger) - 开源 IaC 编排工具。 Digger 允许您在现有的 CI 管道中运行 IaC。
- [Stategraph](https://stategraph.com) - 消除状态文件瓶颈的状态后端。团队计划与资源级锁定并行，状态可通过 SQL 查询。
- [terrakube](https://github.com/AzBuilder/terrakube) - 具有私有注册表、远程状态、自定义流程、计划工作区和视觉状态的开源平台。
- [tofutf](https://github.com/tofutf/tofutf) - Terraform Enterprise 的开源替代方案，具有 SSO、团队管理、代理等功能。
- [Terrateam](https://github.com/terrateamio/terrateam) - Terraform Cloud/Enterprise 的开源替代方案。 GitOps 优先，专为现代 VCS 提供商的规模、安全性和可靠性而构建。

### 登记处

- [library.tf](https://library.tf/) - 提供者和模块的注册表索引器，具有见解和文档。
- [boring-registry](https://github.com/boring-registry/boring-registry) - 与 OpenTofu 兼容的开源模块和提供商注册表。
- [hermitcrab](https://github.com/seal-io/hermitcrab) - 与OpenTofu兼容的Registry网络镜像服务。
- [terrac](https://github.com/haoliangyu/terrac) - 与 OpenTofu 兼容的最小私有模块注册表。
- [GitLab Module Registry](https://docs.gitlab.com/ee/user/packages/terraform_module_registry/) - 使用 GitLab 项目作为 Terraform 模块的私有注册表。
- [terralist](https://github.com/terralist/terralist) - 提供者和模块的私有注册表。
- [citizen](https://github.com/outsideris/citizen) - 模块和提供程序的私有注册表，支持多个数据库和存储。
- [petra](https://github.com/devoteamgcloud/petra) - 使用 Google Cloud Storage 的私有注册表管理器。
- [tapir](https://github.com/PacoVK/tapir) - 具有 UI 的模块和提供程序的私有注册表。
- [terraform-registry](https://github.com/nrkno/terraform-registry) - 具有身份验证和支持多个后端的模块注册表。
- [terrareg](https://github.com/MatthewJohn/terrareg) - 带有 UI 的开源模块注册表、可选的 Git 集成和深入分析。
- [terustry](https://github.com/veepee-oss/terustry) - 提供商的代理注册机构。
- [tofuref](https://github.com/djetelina/tofuref) - OpenTofu 提供商注册表的 TUI。

### 帮手

- [OpenTofu Language Server](https://github.com/opentofu/tofu-ls) - OpenTofu 语言服务器。
- [VS Code Extension](https://open-vsx.org/extension/OpenTofu/vscode-opentofu) - 使用 OpenTofu 语言服务器的 Visual Studio Code 扩展添加了 OpenTofu 文件的编辑功能，例如语法突出显示、IntelliSense、代码导航、代码格式化、模块资源管理器。
- [zed Extension](https://github.com/ashpool37/zed-extension-opentofu) - Zed 编辑器的扩展。
- [terratag](https://github.com/env0/terratag) - CLI 工具允许将标签或标签应用于整组 OpenTofu/Terraform 文件。
- [tfupdate](https://github.com/minamijoyo/tfupdate) - 更新 Terraform / OpenTofu 配置中的版本限制。

## 学习

- [OpenTofu Course](https://killercoda.com/quincycheng/course/course_opentofu) - 互动教程。
- [Terraform in Depth](https://www.manning.com/books/terraform-in-depth) - 预订 OpenTofu 部分。
- [Infrastructure automation with OpenTofu](https://www.udemy.com/course/infrastructure-automation-with-opentofu-hands-on-devops/?couponCode=1D97F4D8FFE62E296BE1) - 通过讲座、测验、动手演示和编码练习来学习基础设施配置。
- [Migrating From Terraform To OpenTofu](https://www.youtube.com/watch?v=v9rJgtHzxUk) - OpenTofu 历史简介以及如何迁移。
- [Terraform Academy OpenTofu Practitioner Path](https://www.terraformacademy.app/max/labs/opentofu-basics.html) - 基于浏览器的交互式实验室涵盖使用 PBKDF2 和 AES-GCM 进行本机状态和计划加密，以及重用适用于 OpenTofu 1.6 及更高版本的 HCL 基础知识的完整从业者准备路径。

## 媒体

- [OSS EU 2023 - 公告](https://www.youtube.com/watch?v=Ha77rpusEDM&t=1190s)
- [OSS EU 2023 - 项目概述](https://www.youtube.com/watch?v=-8sOE9-icmY&t=15116s)
- [代码到云 - OpenTofu 入门](https://www.youtube.com/watch?v=HeUz6TMg82U)
- [CNCF - 2024 年欧洲 OpenTofu 日](https://www.youtube.com/playlist?list=PLnVotLM2Qsyiw_6Pd_9WxRRLdrUAs3c1c)
- [CNCF - 2024 年北美 OpenTofu 日](https://www.youtube.com/playlist?list=PLnVotLM2QsyhhCO5TgEUsAip601j3NUlm)
- [CNCF - 2025 年欧洲 OpenTofu 日](https://www.youtube.com/playlist?list=PLj6h78yzYM2P1WUOx9Ny6Q3JJxiAs1A3M)
- [CNCF - 2025 年北美 OpenTofu 日](https://www.youtube.com/playlist?list=PLj6h78yzYM2MATqCH0Tux6phUq9o4-lnG)

## 播客

<!-- DESC, from most recent to oldest. -->
- [SE 电台：OpenTofu 上的 Christian Mesh](https://se-radio.net/2025/01/se-radio-652-christian-mesh-on-opentofu/)
- [Kubernetes 播客 - OpenTofu，与 Ohad Maislish](https://kubernetespodcast.com/episode/232-opentofu/)
- [TheIaCPodcast - OpenTofu GA 发布、许可和 OSS 未来专家小组](https://www.theiacpodcast.com/episode/expert-panel-on-opentofu-ga-release-licensing-and-oss-future)
- [贡献者 - 社区驱动的 IaC](https://www.contributor.fyi/opentofu)
- [Ned 在云端 - IaC 直播](https://www.youtube.com/watch?v=p0vDydkUWB4)
- [DevOps 受阻 - Open Terraform 怎么样？](https://www.arresteddevops.com/open-tofu/)
- [OpenObservability - Terraform 不再开源。 OpenTF 是继任者吗？](https://www.youtube.com/watch?v=5QdUs9VKq5g)
- [TheCloudGambit - OpenTF 的未来](https://www.thecloudgambit.com/2236725/13576531-the-future-of-opentf-with-ohad-maislish)
- [Oxide 和朋友 - Terraform 的岔路口？](https://www.youtube.com/watch?v=QaU94LY891M)
- [变更日志 - OpenTF 用于开放 Terraform](https://changelog.com/podcast/556)
