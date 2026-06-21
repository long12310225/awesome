# 查安德 [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

**持续集成和持续交付**

作者：【theaiera.cn】(http://www.theaiera.cn)

精选的出色工具列表，用于：
持续集成
持续交付
软件集成
开发运营

- [ciandcd](#ciandcd)
- [Theory](#theory)
- [构建和发布系统](#build-and-release-system)
- [在线构建系统](#online-build-system)
- [Infrastructure](#infrastructure)
- [开发环境](#dev-env)
- [源代码管理](#source-code-management)
- [代码审查](#code-review)
- [Build](#build)
- [静态检查](#static-check)
- [动态检查](#dynamic-check)
- [绩效分析](#performance-analysis)
- [Coverage](#coverage)
- [Testing](#testing)
- [Package](#package)
- [Deploy](#deploy)
- [Delivery](#delivery)
- [配置工具](#provisioning-tools)
- [secure-tools](#secure-tools)
- [网络服务器](#web-server)
- [应用程序和容器](#applications-and-container)
- [操作系统和外壳](#os-and-shell)
- [数据库版本控制](#database-version-control)
- [有用的网站](#useful-sites)
- [会议并提交](#conference-and-submit)
- [Books](#books)
- [其他很棒的清单](#other-awesome-lists)
- [Contact](#contact)

## 理论
持续集成和持续交付的理论
* [continuousIntegration](http://martinfowler.com/articles/continuousIntegration.html)  
* [continuousdelivery](http://continuousdelivery.com)  
* [软件集成](https://en.wikipedia.org/wiki/System_integration)
* [CI/CD 管道](https://semaphoreci.com/blog/cicd-pipeline)
* [devopsdays](http://www.devopsdays.org)  
* [ci备忘单](https://dzone.com/refcardz/continuous-integration)
* [devops_roadmap](https://github.com/kamranahmedse/developer-roadmap)  

## 构建和发布系统
软件构建和发布、持续集成和持续交付的系统
* [Jenkins](http://jenkins-ci.org) 一个可扩展的开源持续集成服务器
* [Solano CI](https://www.solanolabs.com) 通过获得专利的自动并行化实现更快的持续集成和部署。查看结果速度加快 10 至 80 倍。 14 天免费试用。无需信用卡。
* [Concourse](https://concourse-ci.org) 管道被定义为单个声明性配置文件，而不是无数的复选框
* [BuildForge](https://jazz.net/downloads/rational-build-forge/) 自动化并加速构建和发布流程
* [ElectricFlow](http://electric-cloud.com/products/electricflow/) ElectricFlow/ElectricCommander 为分布式团队提供对基础设施、工具链和流程的共享控制和可见性。它加速并自动化软件交付流程，以实现跨多个构建-测试-部署管道的敏捷性、可预测性和安全性
* [Teamcity](http://www.jetbrains.com/teamcity/index.html) 准备工作，可扩展
开箱即用的开发人员友好构建服务器
* [bamboo](https://www.atlassian.com/software/bamboo) Bamboo 不仅仅可以运行构建和测试。它连接问题、提交、测试结果和部署，以便整个产品团队可以了解整个情况
* [go（旧的 snap-ci）](https://www.gocd.org/) 自动化并简化构建-测试-发布周期，以无忧、持续地交付产品
* [hudson](http://hudson-ci.org) Jenkins 的前一个
* [openbuildservice](http://openbuildservice.org) 开放构建服务 (OBS) 是一个通用系统，用于以自动、一致和可重复的方式从源构建和分发二进制包。您可以为各种操作系统和硬件架构发布软件包以及更新、附加组件、设备和整个发行版
* [buildbot](http://trac.buildbot.net) Buildbot 是一个持续集成系统，旨在自动化构建/测试周期。通过在每次发生更改时自动重建和测试树，可以在其他开发人员因故障而造成不便之前快速查明构建问题
* [Parabuild](http://www.viewtier.com/index.htm) Parabuild 是一个企业软件构建和发布管理系统，通过为软件团队提供几乎牢不可破的发布构建和持续集成来帮助他们按时发布
* [FinalBuilder](https://www.finalbuilder.com/) 使用 FinalBuilder 自动化构建过程非常简单。使用 FinalBuilder，您无需编辑 xml 或编写脚本。直观地定义和调试您的构建脚本，然后使用 Windows 调度程序调度它们，或将它们与 Continua CI、Jenkins 或任何其他 CI 服务器集成
* [VisualBuild](http://www.kinook.com/VisBuildPro/) Visual Build 使开发人员和构建大师能够轻松创建自动化、可重复的构建过程
* [cruisecontrol](http://www.cruisecontrolnet.org) CruiseControl.NET，一个自动持续集成服务器，使用 .NET Framework 实现
* [Continuum](http://continuum.apache.org/) Apache Continuum™ 是一款企业级持续集成服务器，具有自动构建、发布管理、基于角色的安全性以及与流行构建工具和源代码控制管理系统集成等功能
* [quickbuild](http://www.pmease.com/) GitHub 集成。强制搁置支持。 Coverity 报告渲染。 Subversion 外部变更检索。资源访问信息。显示等待步骤的原因。自定义构建和请求列。最喜欢的仪表板列表。可继承的环境变量。还有更多...
* [rexify](http://www.rexify.org//) perl 部署和配置管理
* [SimpleCI](https://github.com/simpleci/simpleci) 基于 Docker 的自托管 ci 系统。支持分布式构建缓存、外部提供者（GCE）、实时构建日志等。
* [pulse](http://zutubi.com)没有免费版本。
* [PHP Censor](https://github.com/php-censor/php-censor) 用于 PHP 项目的开源自托管持续集成服务器。
* [rundeck](http://rundeck.org) Rundeck 具有细粒度访问控制、内置作业调度程序以及定义向节点分派命令和脚本的工作流的能力。
* [cds](https://ovh.github.io/cds) CDS 是一个用 Go(lang) 编写的企业级持续交付和 DevOps 自动化平台。
* [Drone CI](https://drone.io/) Drone 是一个基于容器技术构建的持续交付系统。 Drone 使用简单的 YAML 配置文件（docker-compose 的超集）来定义和执行 Docker 容器内的 Pipelines。
* [Luigi](https://github.com/spotify/luigi) Luigi 是一个 Python 模块，可帮助您构建复杂的批处理作业管道。它处理依赖关系解析、工作流管理、可视化等。它还内置 Hadoop 支持。
* [Kraken CI](https://kraken.ci) Kraken CI 是一个现代 CI/CD、开源、本地系统，具有高度可扩展性并专注于测试。

## 在线构建系统
在线构建发布系统
* [appcircle.io](https://appcircle.io) - 带有在线设备模拟器的适用于 iOS 和 Android 的自动化移动 CI/CD/CT。
* [closeheat](http://closeheat.com) 静态网站与 GitHub 和云开发环境集成
* [travis-ci](https://travis-ci.org) github 和 bitbuckets 的 ci 服务器
* [cloudbees](https://www.cloudbees.com/) 企业 Jenkins 公司
* [elasticbox](https://elasticbox.com) 一种 DevOps 方法，专注于可重用的应用程序组件即服务，并使运营能够提供 IT 即服务
* [coveralls](https://coveralls.io) 跟踪项目一段时间内的代码覆盖率、文件更改以及标记您的 GitHub 存储库
* [shippable](https://app.shippable.com/) 托管基于 docker 的持续集成和部署服务
* [circleci](https://circleci.com) Web 应用程序的持续集成。
* [buildbox](https://buildkite.com/) 简单的自托管持续集成
* [drone](https://drone.io) 基于 Docker 构建的开源持续集成平台
* [appveyor](http://www.appveyor.com) 为繁忙的 Windows 提供持续集成和部署服务
* ~~[snap-ci](https://snap-ci.com) 轻松构建，按需部署~~。
* [codeship](https://codeship.com) 持续集成和交付变得简单
* [githost](https://githost.io) 无痛 GitLab CE 和 CI 托管
* [testling](https://ci.testling.com) 每次推送时自动进行浏览器测试
* [magnum-ci](https://magnum-ci.com) 托管私有存储库的持续集成和交付平台
* [wercker](http://wercker.com) 轻松测试和部署您的应用程序
* [codecov](https://codecov.io) 连续代码覆盖率。具有浏览器扩展和出色的拉取请求评论，可跟踪 GitHub/Bitbucket/Gitlab 存储库上随时间的覆盖情况
* [GitLab CI](https://about.gitlab.com/gitlab-ci/) - 基于红宝石。他们还提供 GitLab，用于管理 git 存储库。
* [IBM DevOps Services](https://hub.jazz.net) - 开发、跟踪、规划软件并将其部署到 IBM Bluemix 云平台上。
* [deploybot](https://deploybot.com) - 为整个团队在一个一致的流程中即时构建和交付代码。
* [Semaphore CI](https://semaphoreci.com/) - 快速且易于使用的持续集成和部署服务，具有原生 Docker 支持。
* [flow.ci](https://flow.ci/) - flow.ci，为塑造未来的创新者提供持续集成和交付服务。
* [Bitrise](https://www.bitrise.io/) 基于云的持续集成和移动交付，免费用于 OSS
* [Cirrus CI](https://cirrus-ci.org) 免费开源，支持 Linux、Windows、macOS 和 FreeBSD，灵活的托管 CI 服务
* [DeployPlace](https://deployplace.com) - 复杂的部署变得简单。只需几分钟即可从 git 或 CI 部署您的应用程序。
* [Buildkite](https://buildkite.com) - 为您的所有软件项目提供闪电般的快速测试和交付


## 监控
用于监控持续集成和持续交付状态的工具
* [CatLight](https://catlight.io) 为 Jenkins、TeamCity、Travis CI、Appveyor 和 TFS 构建状态监视器
* [Barklarm](https://www.barklarm.com/) 开源多平台警报监控器并构建支持 CCTray 规范和 Github Actions 的服务器状态。
* [CCMenu](http://ccmenu.org/) OSx 构建状态监视器，用于支持 CCTray 规范的服务器。

## 基础设施
硬件、虚拟机、fram管理、docker
* [GridWiki](http://wiki.gridengine.info/wiki/index.php/Main_Page) 网格 wiki 页面
* [UGE](http://www.univa.com) Univa 工作负载管理解决方案通过在数千台服务器之间有效共享工作负载，最大限度地提高现有计算资源的价值
* [SGE](http://gridscheduler.sourceforge.net) Grid Engine 通常用于计算机场或高性能计算 (HPC) 集群，负责接受、调度、分派和管理大量独立、并行或交互式用户作业的远程和分布式执行。它还管理和调度分布式资源的分配，例如处理器、内存、磁盘空间和软件许可证
* [LSF](http://www-03.ibm.com/systems/platformcomputing/products/lsf/) 平台负载共享工具（或简称 LSF）是一个用于分布式 HPC 环境的工作负载管理平台、作业调度程序。它可用于在许多不同架构的联网 Unix 和 Windows 系统上执行批处理作业
* [vmwarevshpere](http://www.vmware.com/products/vsphere) VMware vSphere（以前称为 VMware Infrastructure 4）是 VMware 的云计算虚拟化操作系统
* [citrixserver](http://www.citrix.com/products/xenserver/overview.html) XenServer 是适用于公共云和私有云的最佳服务器虚拟化平台，为 5 个最大的托管提供商云中的 4 个提供支持。  XenServer 在构建时考虑到了规模、安全性和多租户，可实现更高的灵活性和成本效率
* [miscrosofthyperv]（Docker - 为开发人员和系统管理员提供分布式应用程序的开放平台）微软虚拟化
* [amazon](http://aws.amazon.com/ec2/) 云中可扩展、按需付费的计算能力
* [mesosphere-dc/os](mesosphere.com) 作为数据中心操作系统，DC/OS 本身就是一个分布式系统、集群管理器、容器平台和操作系统。

## 开发环境
* [boxstarter](http://boxstarter.org/) 使用 Chocolatey 软件包可以轻松实现可重复、重新启动的弹性 Windows 环境安装。
* [T.A.D.S.样板](https://github.com/Thomvaill/tads-boilerplate) 使用 Ansible 设置 Docker Swarm 环境的样板
* [vagrantup](https://www.vagrantup.com/) 创建和配置轻量级、可重复且可移植的开发环境。
* [veewee](https://github.com/jedi4ever/veewee) 简化 vagrant box 的构建

## 源代码管理
版本控制和源代码管理工具
* [git](http://git-scm.com) Git 是一个免费开源的分布式版本控制系统，旨在快速高效地处理从小到大的项目
* [perforce](https://www.perforce.com/) 业界最可靠且经过验证的平台，用于版本控制代码、图像、文档......一切
* [clearcase](http://www-03.ibm.com/software/products/en/clearcase) IBM Rational ClearCase 是一个软件配置管理解决方案，提供版本控制、工作区管理、并行开发支持和构建审核
* [mercurial](https://www.mercurial-scm.org/) Mercurial 是一款免费的分布式源代码控制管理工具。它可以有效地处理任何规模的项目，并提供简单直观的界面
* [svn](http://subversion.apache.org) Subversion 是一个开源版本控制系统
* [gitlab](https://about.gitlab.com/) 开源自托管Git管理软件
* [github](https://github.com) 针对开源和私人开发项目的强大协作、审查和代码管理。
* [bitbuckets](https://bitbucket.org) 将您的代码植入云端。看着它成长。
* [teamfoundationservice](http://tfs.visualstudio.com) Visual Studio Online 基于 Team Foundation Server 的功能以及附加云服务，是您的开发项目的在线主页。只需几分钟即可在我们的云基础设施上启动并运行，无需安装或配置单个服务器。 Visual Studio Online 连接 Visual Studio、Eclipse、Xcode 和其他 Git 客户端，支持多种平台和语言的开发
* [phabricator](http://phabricator.org/) Phabricator 是开源 Web 应用程序的集合，可帮助软件公司构建更好的软件。
* [IBM DevOps Services](https://hub.jazz.net) - 存储、管理、编辑和协作处理您的源代码。然后部署到IBM Bluemix云平台上。

## 代码审查
代码审查工具
* [codecollaborator](http://smartbear.com/product/collaborator/overview/) Collaborator帮助开发、测试和管理团队协同工作，生成高质量的代码
* [crucible](https://www.atlassian.com/software/crucible/overview) 代码审查 = 高质量代码。使用 Crucible 灵活的审核工作流程审核代码、讨论更改、共享知识并识别缺陷。它的代码审查让 Subversion、CVS、Perforce 等变得轻松
* [reviewboard](https://www.reviewboard.org/) 审查委员会消除了代码审查的痛苦，为您节省时间、金钱和理智，让您可以专注于开发出色的软件
* [codestriker](http://codestriker.sourceforge.net) Codestriker 是一个开源 Web 应用程序，支持在线代码审查。支持传统的文档审查，以及审查由 SCM（源代码管理）系统和普通 unidiff 补丁生成的差异
* [getbarkeep](http://getbarkeep.org) 一种快速、有趣的代码审查方式
* [gerrit](https://code.google.com/p/gerrit/) Gerrit 是一个基于 Web 的代码审查系统，可促进使用 Git 版本控制系统的项目的在线代码审查
* [Codebrag](http://www.codebrag.com/) Codebrag 是一个简单的代码审查工具，使该流程适合您的团队。
* [Upsource](https://www.jetbrains.com/upsource/) 多语言代码审查工具，具有 PHP、JavaScript 和 Kotlin 的代码洞察、GitHub 集成、自动化工作流程、与 CI 服务器集成
* [Ebert](https://ebertapp.io) Ebert 对您的 GitHub 存储库进行持续静态分析，并将其直接发送到您的 Pull 请求，帮助您的团队专注于重要的事情并交付更好的软件。

## 构建
构建工具
* [gnumake](http://www.gnu.org/software/make/) GNU Make 是一个控制从程序源文件生成程序的可执行文件和其他非源文件的工具
* [gnuautoconf](http://www.gnu.org/software/autoconf/) Autoconf 是 M4 宏的可扩展包，可生成 shell 脚本来自动配置软件源代码包
* [mozillabuildtools](https://developer.mozilla.org/en-US/docs/Mozilla/Developer_guide/Build_Instructions) Mozilla 构建系统与 Mozilla 代码库的其他部分一样，是跨平台的。它使用传统的 Unix 风格的 autoconf 和 make 工具来构建各种应用程序（即使在非 UNIX 操作系统上）
* [scons](http://www.scons.org) SCons 是一个开源软件构建工具，即下一代构建工具。将 SCons 视为经典 Make 实用程序的改进的跨平台替代品，具有类似于 autoconf/automake 的集成功能和 ccache 等编译器缓存。简而言之，SCons 是一种更简单、更可靠、更快速的软件构建方式
* [cmake](https://cmake.org/) cmake 提供强大的跨平台软件开发解决方案。了解我们如何帮助您的团队高效管理软件项目的构建、测试和打包流程
* [msbuild](http://msdn.microsoft.com/en-us/library/dd393574.aspx) Microsoft Build Engine 是一个用于构建应用程序的平台。该引擎也称为 MSBuild，为项目文件提供 XML 架构，用于控制构建平台处理和构建软件的方式。 Visual Studio 使用 MSBuild，但它不依赖于 Visual Studio。通过在项目或解决方案文件上调用 msbuild.exe，您可以在未安装 Visual Studio 的环境中编排和构建产品
* [ant](http://ant.apache.org) Ant 可用于试验可以用目标和任务来描述的任何类型的流程。 Ant 的主要已知用途是构建 Java 应用程序。
* [maven](http://maven.apache.org) Apache Maven 是一个软件项目管理和理解工具。基于项目对象模型 (POM) 的概念，Maven 可以通过中央信息来管理项目的构建、报告和文档。
* [gradle](http://gradle.org/) Gradle 是构建自动化演变而来的。 Gradle 可以自动构建、测试、发布、部署等软件包或其他类型的项目，例如生成的静态网站、生成的文档或其他任何内容。
* [ElectricacCelerator](http://electric-cloud.com/products/electricaccelerator) 如果构建和测试需要很长时间才能完成，则持续交付就不是连续的。 ElectricAccelerator 可将构建和测试速度提高 20 倍，从而缩短软件上市时间、基础设施利用率和开发人员生产力
* [SBT](http://www.scala-sbt.org/index.html) sbt 是一个用于 Scala 和 Java 项目的开源构建工具。
* [do](https://github.com/8gears/do) 地球上最简单的构建工具。不可知的多用途构建工具和构建文件。努力比通常的外壳地狱更好。


## 静态检查
软件静态检查工具
* [静态工具 wiki](https://en.wikipedia.org/wiki/List_of_tools_for_static_code_analysis) wiki 页面
* [coverity](http://www.coverity.com/) 持续衡量和提高整个开发组织的代码质量和安全性
* [fxcop](http://msdn.microsoft.com/en-us/library/bb429476%28VS.80%29.aspx) FxCop 是一个应用程序，用于分析托管代码程序集（面向 .NET Framework 公共语言运行时的代码）并报告有关程序集的信息，例如可能的设计、本地化、性能和安全性改进
* [cpd](http://pmd.sourceforge.net/pmd-4.3.0/cpd.html) 重复的代码可能很难找到，尤其是在大型项目中。但 PMD 的复制/粘贴检测器 (CPD) 可以为您找到它
* [sonar](http://www.sonarqube.org) SonarQube 是一个管理代码质量的开放平台
* [findbugs](http://findbugs.sourceforge.net) 查找 Java 程序中的错误
* [checkstyle](http://checkstyle.sourceforge.net) Checkstyle 是一个开发工具，可帮助程序员编写符合编码标准的 Java 代码

## 动态检查
软件动态检查工具
* [动态工具 wiki](https://en.wikipedia.org/wiki/Dynamic_program_analysis) wiki 页面
* [valgrind](http://valgrind.org) 自动检测许多内存管理和线程错误，并详细分析您的程序

## 绩效分析
软件性能分析工具
* [性能工具 wiki](https://en.wikipedia.org/wiki/List_of_performance_analysis_tools) wiki 页面

## 覆盖范围
软件测试覆盖率工具
* [代码覆盖率 wiki](https://en.wikipedia.org/wiki/Code_coverage) wiki 页面

## 测试
软件测试框架和工具
* [Testingautomation](https://en.wikipedia.org/wiki/Test_automation) 测试自动化 wiki 页面
* [softwareqatest](http://www.softwareqatest.com) 常见问题页面
* [qaforums](http://www.qaforums.com) SQA 论坛
* [opensourcetesting](http://www.opensourcetesting.org) 开源软件测试工具、新闻和讨论
* [selenium](http://www.seleniumhq.org) Selenium 使浏览器自动化
* [Monkey Test It](https://monkeytest.it) 具有 CURLable API 的免费自动化网站测试器
* [Assertible](https://assertible.com) GitHub 的持续部署后测试
* [Macaca](https://github.com/alibaba/macaca) 针对移动和桌面平台上的本机、混合、移动 Web 和 Web 应用程序的自动化测试解决方案

## 套餐
软件包及安装工具
* [installshield](http://www.installshield.com) 世界第一的软件安装解决方案 - 为 Windows 应用程序构建可靠的 MSI 安装程序
* [NSIS](http://nsis.sourceforge.net/Main_Page) NSIS (Nullsoft Scriptable Install System) 是一个用于创建 Windows 安装程序的专业开源系统。它被设计得尽可能小和灵活，因此非常适合互联网分发
* [rpm](http://rpm.org) RPM Package Manager (RPM) 是一个功能强大的命令行驱动的包管理系统，能够安装、卸载、验证、查询和更新计算机软件包
* [yum](http://yum.baseurl.org) Yum 是 rpm 系统的自动更新程序和软件包安装程序/删除程序
* [fpm](https://github.com/jordansissel/fpm) 有效的包管理！轻松、理智地为多个平台（deb、rpm 等）构建软件包。
* [wix](http://wixtoolset.org/) 最强大的工具集，可用于创建 Windows 安装体验。
* [packer](https://www.packer.io/) Packer 是一种从单一源配置为多个平台创建相同机器映像的工具。

## 部署
网站部署工具
* [jfrog](https://www.jfrog.com/) 是第一个二进制存储库管理解决方案，Artifactory 改变了整个软件发布周期中控制、存储和管理二进制文件的方式
* [xl-deploy](https://xebialabs.com/products/xl-deploy) 无代理、基于模型的应用程序部署
* [Jenkinsdeployplugin](https://wiki.jenkins-ci.org/display/JENKINS/Deploy%20Plugin)部署到tomcat
* [bintray](https://bintray.com) 自动分发软件版本的最快、最可靠的方法
* [Gitploy](https://www.gitploy.io/) 在几分钟内围绕 GitHub 构建部署系统

## 发货
软件交付工具
* [sl-release](https://xebialabs.com/products/xl-release) 编排您的持续交付管道。简单的。灵活的。端到端
* [archiva](http://archiva.apache.org/index.cgi) Apache Archiva™ 是一个可扩展的存储库管理软件，可帮助管理您自己的个人或企业范围的构建工件存储库。它是 Maven、Continuum 和 ANT 等构建工具的完美伴侣
* [nexus](http://www.sonatype.com/nexus) 存储库管理器（也称为组件管理器）的使用正在帮助软件开发团队在操作速度、效率和质量方面实现简单的提升
* [chocolatey](https://chocolatey.org/) Chocolatey NuGet 是一个机器包管理器，有点像 apt-get，但专为 Windows 构建
* [pulp](http://www.pulpproject.org/) Pulp 是一个用于管理内容存储库（例如软件包）并将该内容推送给大量消费者的平台。
* [herd](https://github.com/russss/Herd) 一个单命令的 BitTorrent 分发系统，基于 Twitter 的 Murder
* [murder](https://github.com/lg/murder) 使用来自 twitter.com 的 BitTorrent 和 BitTornado 库部署大型服务器

## 配置工具
配置工具
* [Ansible](http://www.ansible.com) 通过人类可读的剧本提供简单的基础设施管理工具
* [Puppet]() 在任何公共或私有云上构建、销毁和重建服务器
* [Chef](https://www.chef.io/chef/) 快速、可扩展且灵活的数据中心自动化软件
* [SaltStack](http://saltstack.com/community/) 极其简单的配置管理、应用程序部署、任务执行和多节点编排引擎
* [terraform](https://www.terraform.io) 使用基础设施即代码来配置和管理任何云、基础设施或服务

## 安全工具
安全工具
* [Deepfence Enterprise](https://deepfence.io) - 适用于 kubernetes、虚拟机和无服务器的全生命周期云原生工作负载保护平台。
* [Deepfence Threat Mapper](https://github.com/deepfence/ThreatMapper) - 适用于 kubernetes、虚拟机和无服务器的强大运行时漏洞扫描器。
* [whitesource](https://www.whitesourcesoftware.com/) 保护和管理软件中开源组件的最简单方法。

## 网络服务器
常用的网络服务器
* [apache](https://httpd.apache.org) 自 1996 年 4 月以来，Apache httpd 一直是 Internet 上最流行的 Web 服务器
* [nginx](http://nginx.org) 一个高性能的免费开源 Web 服务器，为互联网上最繁忙的网站提供支持
* [tomcat](http://tomcat.apache.org) Java Servlet 和 JavaServer Pages 技术的开源软件实现
* [jetty](http://www.eclipse.org/jetty/)  
Jetty 提供 Web 服务器和 javax.servlet 容器，并支持 SPDY、WebSocket、OSGi、JMX、JNDI、JAAS 和许多其他集成
* [HAProxy](http://www.haproxy.org/) - 基于软件的负载平衡、SSL 卸载和性能优化、压缩和一般 Web 路由。

## 操作系统和外壳
Linux shell、perl、python
* [awesome-shell](https://github.com/itech001/awesome-shell/blob/master/README.md)  
* [awesome-python](https://github.com/vinta/awesome-python)  
* [awesome-perl](https://github.com/hachiojipm/awesome-perl)  
* [awesome-sysadmin](https://github.com/kahun/awesome-sysadmin)  

## 应用程序和容器
VM应用程序和容器
* [docker](https://www.docker.com) Docker - 为开发人员和系统管理员提供分布式应用程序的开放平台
* [suseapplication](https://www.suse.com/products/susestudio/) 创建 suse 应用程序的工具

## 数据库版本控制
数据库版本控制系统
* [liquibase](http://www.liquibase.org) 数据库的源代码控制
* [flywaydb](http://flywaydb.org) 数据库迁移变得简单
* [Rumba RDBM](https://www.dbinvent.com/) 数据库迁移工具，支持纯 SQL 和声明式定义。
* [dbdeploy](http://dbdeploy.com) dbdeploy 是一个数据库变更管理工具。它适合想要以简单、受控、灵活和频繁的方式改进数据库设计或重构数据库的开发人员或 DBA
* [dbmaestro](http://www.dbmaestro.com/) 受控数据库持续交付是我们的业务

## 有用的网站
其他有用的页面
* [infoq](http://www.infoq.com)  
* [stackoverflow](http://stackoverflow.com)  

## 会议并提交
会议并提交
* [devops提交](http://devopssummit.sys-con.com)

## 书籍
* [Securing DevOps](https://manning.com/books/securing-devops?a_aid=securingdevops&a_bid=1353bcd8) - 一本关于利用 CI/CD 技术提高 Web 应用程序及其基础设施安全性的书。
* [Learning Continuous Integraion with TeamCity](https://www.packtpub.com/web-development/learning-continuous-integration-teamcity-raw) - 通过使用 TeamCity 针对不同的技术堆栈进行设置，掌握持续集成背后的原则和实践
* [Pipeline as Code](https://www.manning.com/books/pipeline-as-code) - 一本关于使用 Jenkins 为云原生应用程序（包括 K8s 和无服务器应用程序）构建 CI/CD 管道的书。
* [Continuous Delivery for Kubernetes](https://www.manning.com/books/continuous-delivery-for-kubernetes) - 借助适用于 Kubernetes 和云应用程序的开源工具，快速开启持续交付之旅
* [Continuous Delivery in Go](https://www.manning.com/books/continuous-delivery-in-go) - 本书向您展示如何构建优化开发流程的管道，以便您可以将软件无缝交付到生产环境。

## 其他很棒的清单
其他令人惊叹的很棒的列表可以在
* [awesome](https://github.com/sindresorhus/awesome)  
* [awesome-awesome](https://github.com/emijrp/awesome-awesome)  
* [awesome-awesomeness](https://github.com/bayandin/awesome-awesomeness)  
* [sysadmin](https://github.com/itech001/awesome-sysadmin)  
* [CI 工具比较](https://en.wikipedia.org/wiki/Comparison_of_continuous_integration_software)
* [ci 工具比较2](https://github.com/ciandcd/Continuous-Integration-services/blob/master/continuous-integration-services-list.md)
* [CI 工具比较 3](https://github.com/ligurio/Continuous-Integration-services)
* [awesome-docker](https://github.com/veggiemonk/awesome-docker)  
*[awesome-cicd](https://github.com/awsomecicd/awesomecicd.git)


## 联系方式
欢迎添加有关持续集成和持续交付的新内容。
我的电子邮件是：itech001@126.com。
  


