# 很棒的 Docker<!-- 目录中省略 --> [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)][sindresorhus] [![Track Awesome List](https://www.trackawesomelist.com/badge.svg)](https://www.trackawesomelist.com/veggiemonk/awesome-docker/)

> Docker 项目的精选列表。

如果您想贡献，请先阅读 [CONTRIBUTING.md](https://github.com/veggiemonk/awesome-docker/blob/master/.github/CONTRIBUTING.md)。
如果此列表不完整，您可以做出贡献以使其完整。
如果您在此处看到某个链接（不再）合适，您可以通过提交 [pull request][editreadme] 来修复该链接以改进此文件。谢谢你！

**该项目必须是针对 Docker 的，而不仅仅是使用 Docker。**

> 经验法则：如果删除 Docker 集成不会破坏项目的价值主张，则它不属于此列表。

此列表的创建者和维护者不会收到任何形式的付款来接受任何贡献者所做的更改。
这个页面无论如何都不是官方的 Docker 产品。
它是项目链接列表，由志愿者维护。
欢迎大家做出贡献。
该存储库的目标是为开源项目建立索引，而不是为了盈利而做广告。

> Docker 是一个开放平台，供开发人员和系统管理员构建、发布和运行分布式应用程序。 Docker 由 Docker Engine（一种便携式、轻量级运行时和打包工具）和 Docker Hub（一种用于共享应用程序和自动化工作流程的云服务）组成，使应用程序能够从组件快速组装，并消除开发、QA 和生产环境之间的摩擦。因此，IT 可以更快地交付并在笔记本电脑、数据中心虚拟机和任何云上运行相同的应用程序（无需更改）。

_来源：_ [什么是 Docker](https://www.docker.com/why-docker/)

# 目录 <!-- 目录中省略 -->

<!-- TOC -->

- [Projects](#projects)
    - [引擎\&运行时](#engine--runtime)
    - [建立形象](#building-images)
        - [Builder](#builder)
        - [基础图像](#base-images)
        - [Dockerfile](#dockerfile)
        - [Linter](#linter)
    - [图像生命周期](#image-lifecycle)
        - [Registry](#registry)
        - [注册表 CLI](#registry-cli)
        - [图像扫描\&SBOM](#image-scanning--sbom)
        - [供应链](#supply-chain)
    - [运行容器](#running-containers)
        - [Composition](#composition)
        - [Orchestration](#orchestration)
        - [部署\&平台](#deployment--platforms)
        - [垃圾收集](#garbage-collection)
    - [网络\&代理](#networking--proxies)
        - [Networking](#networking)
        - [反向代理](#reverse-proxy)
    - [存储&数据](#storage--data)
    - [Observability](#observability)
    - [Security](#security)
    - [用户界面](#user-interfaces)
        - [Desktop](#desktop)
        - [Terminal](#terminal)
        - [Web](#web)
        - [集成开发环境](#ide-integrations)
    - [开发人员工作流程](#developer-workflow)
        - [API客户端](#api-client)
        - [CI/CD](#cicd)
        - [开发环境](#development-environment)
        - [Serverless](#serverless)
        - [Testing](#testing)
        - [Wrappers](#wrappers)
    - [容器内工具](#in-container-tooling)
- [学习资源](#learning-resources)
    - [从哪里开始](#where-to-start)
    - [从哪里开始（Windows）](#where-to-start-windows)
    - [书籍\和教程](#books--tutorials)
    - [很棒的清单](#awesome-lists)
    - [演示和示例](#demos-and-examples)
    - [好建议](#good-tips)
    - [树莓派\&ARM](#raspberry-pi--arm)
    - [安全文章](#security-articles)
    - [Videos](#videos)
    - [社区和聚会](#communities-and-meetups)
        - [Brazilian](#brazilian)
        - [English](#english)
        - [Russian](#russian)
        - [Spanish](#spanish)
- [随着时间的推移观星者](#stargazers-over-time)

<!-- /TOC -->

# 项目

## 官方项目

- [Moby](https://github.com/moby/moby)
- [码头工人中心](https://hub.docker.com)
- [Docker Compose](https://github.com/docker/compose/) - 使用 Docker 定义和运行多容器应用程序。
- [Docker Registry][distribution] - 用于打包、运输、存储和交付内容的 Docker 工具集

## 引擎和运行时

- [colima](https://github.com/abiosoft/colima) - 只需最少的设置即可在 macOS（和 Linux）上运行容器运行时。
- [containerd](https://github.com/containerd/containerd) - 开放且可靠的容器运行时。
- [cri-o](https://github.com/cri-o/cri-o) - 基于开放容器计划的 Kubernetes 容器运行时接口实现。
- [gVisor](https://github.com/google/gvisor) - 容器应用程序内核。
- [lxc](https://github.com/lxc/lxc) - LXC - Linux 容器。
- [Mocker](https://github.com/us/mocker) - 适用于 macOS 的 Docker 兼容容器 CLI，基于 Apple 的容器化框架构建。
- [podman](https://github.com/containers/libpod) - Libpod 是一个用于创建容器 pod 的库。波德曼的家。
- [runc](https://github.com/opencontainers/runc) - 用于根据 OCI 规范生成和运行容器的 CLI 工具。
- [runtime-tools](https://github.com/opencontainers/runtime-tools) - Oci-runtime-tool 是用于处理 OCI 运行时规范的工具集合。
- [youki](https://github.com/youki-dev/youki) - 用 Rust 编写的容器运行时，实现 OCI 运行时规范。

## 建立形象

### 建设者

旨在帮助或简化构建**新**图像的应用程序

- [ansible-bender](https://github.com/ansible-community/ansible-bender) - 一个利用“ansible”和“buildah”的工具。
- [apko](https://github.com/chainguard-dev/apko) - 来自 apk 包的声明式 OCI 映像生成器；可按设计重现。
- [buildah](https://github.com/containers/buildah) - 一种有助于构建 OCI 映像的工具。
- [BuildKit](https://github.com/moby/buildkit) - 并发、高效缓存且与 Dockerfile 无关的构建器工具包。
- [buildx](https://github.com/docker/buildx) - 用于由 BuildKit 支持的多平台构建的官方 Docker CLI 插件。
- [cekit](https://github.com/cekit/cekit) - openshift 使用不同构建引擎构建基础镜像的工具。
- [dlayer](https://github.com/orisano/dlayer) - Docker 层分析器。
- [docker-companion](https://github.com/mudler/docker-companion) - 用 Golang 编写的命令行工具，用于压缩和解压 docker 镜像。
- [docker-repack](https://github.com/orf/docker-repack) - 将 Docker 镜像重新打包成更小、更高效的版本，使其拉取速度显着加快。
- [DockerSlim](https://github.com/docker-slim/docker-slim) 缩小肥胖的 Docker 镜像，创建尽可能小的镜像。
- [earthly](https://github.com/earthly/earthly) - 使用 Dockerfile-meets-Makefile 语法进行容器化构建自动化。
- [essex](https://github.com/utensils/essex) - 基于 Docker 的项目的样板：Essex 是一个用 bash 编写的 CLI 实用程序，可通过 Makefile 驱动的工作流程快速设置干净且一致的 Docker 项目。
- [HPC Container Maker](https://github.com/NVIDIA/hpc-container-maker) - 从高级 Python 配方生成 Dockerfile，包括高性能计算组件的构建块。
- [img](https://github.com/genuinetools/img) - 独立、无守护程序、无特权的 Dockerfile 和 OCI 兼容容器映像生成器。
- [ko](https://github.com/ko-build/ko) - 将 Go 应用程序构建并部署为容器映像，无需 Dockerfile。
- [nix2container](https://github.com/nlewo/nix2container) - 使用 Nix 构建 OCI 映像，无需“docker load”往返。
- [packer](https://developer.hashicorp.com/packer/integrations/hashicorp/docker/latest/components/builder/docker) - Hashicorp 工具用于构建机器映像，包括与 Chef、puppet、ansible 等配置管理工具集成的 docker 映像。
- [Production-Ready Python Containers](https://pythonspeed.com/products/pythoncontainer/) - :yen：用于为 Python 应用程序创建生产就绪的 Docker 映像的模板。
- [RAUDI](https://github.com/cybersecsi/RAUDI) - 每当有新版本/更新/提交时，自动更新（并可选择推送到 Docker Hub）第 3 方软件的 Docker 映像的工具。
- [runlike](https://github.com/lavie/runlike) - 从运行的容器生成“docker run”命令和选项。
- [Whaler](https://github.com/P3GLEG/Whaler) - 将 Docker 镜像反转为 Dockerfile 的程序。


### 基础图像

最小的、强化的或专门构建的容器基础镜像。

- [Chainguard Images](https://github.com/chainguard-images/images) - 基于 Wolfi 构建的最小、签名、SBOM 证明的容器镜像。
- [distroless](https://github.com/GoogleContainerTools/distroless) - 以语言为中心的 docker 镜像，减去操作系统。
- [melange](https://github.com/chainguard-dev/melange) - 从声明性 YAML 构建 apk 包以与 apko 一起使用。
- [Wolfi](https://github.com/wolfi-dev/os) - Undistro Linux 专为容器设计；基于 glibc 的、签名的每日 SBOM。


### Dockerfile

- [Dockerfile Generator](https://github.com/ozankasikci/dockerfile-generator) `dfg` 既是一个 Go 库，也是一个使用各种输入通道生成有效 Dockerfile 的可执行文件。
- [Dockershelf](https://github.com/Dockershelf/dockershelf) - 一个存储库，用作通用、高效且精简的 docker 配方的收集器。图像每天通过 Travis cron 作业更新、测试和发布。
- [Trsuted Builds](https://dockerfile.github.io/) - 值得信赖的自动化 Docker 构建。 Dockerfile 项目维护 Dockerfile 的中央存储库，用于在 Docker 容器上运行的各种流行的开源软件服务。

### 短绒

- [Dockadvisor](https://github.com/deckrun/dockadvisor) - 具有 60 多个规则、质量评分和安全检查的轻量级 Dockerfile linter。
- [docker-image-size-limit](https://github.com/wemake-services/docker-image-size-limit) - 一个监控 docker 镜像大小的工具。
- [Hadolint](https://github.com/hadolint/hadolint) - 一个 Dockerfile linter，用于检查最佳实践、常见错误，并且还能够检查以“RUN”指令编写的任何 bash；。

## 图像生命周期

### 登记处

用于安全存储 Docker 映像的服务。

- [Amazon Elastic Container Registry](https://aws.amazon.com/ecr/) - ：日元：Amazon Elastic Container Registry (ECR) 是一个完全托管的 Docker 容器注册表，使开发人员可以轻松存储、管理和部署 Docker 容器映像。
- [Azure Container Registry](https://azure.microsoft.com/en-us/products/container-registry/#overview) - :yen：将 Docker 私有注册表作为一流的 Azure 资源进行管理。
- [Cloudsmith](https://cloudsmith.com/product/formats/docker-registry) - :yen：完全托管的包管理 SaaS，为公共和私有 Docker 注册表（以及许多其他注册表，包括 Kubernetes 生态系统的 Helm 图表）提供一流的支持。拥有慷慨的免费套餐，并且完全免费开源。
- [Container Registry Service](https://container-registry.com/) - ：日元：基于 Harbor 的容器管理解决方案，为团队和组织提供服务。免费套餐为私有存储库提供 1 GB 存储空间。
- [Cycle.io](https://cycle.io/) - ：日元：裸机容器托管。
- [DigitalOcean](https://www.digitalocean.com/products/container-registry) - ：日元：DigitalOcean 容器注册表。
- [Docker Hub](https://hub.docker.com/) 由 Docker Inc. 提供
- [Docker Registry v2][distribution] - 用于打包、运输、存储和交付内容的 Docker 工具集
- [Dragonfly](https://github.com/dragonflyoss/Dragonfly2) - 基于p2p技术，提供高效、稳定、安全的文件分发和图像加速。
- [GCP Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs) - :yen: Google Cloud Platform 上快速、私有的 Docker 镜像存储。
- [Gitea Container Registry](https://docs.gitea.com/usage/packages/container) - Gitea 中集成了 Docker 注册表，非常适合私有、小型镜像托管。
- [GitHub Container Registry](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry) - GitHub 用于存储和管理 Docker 映像的解决方案，与 GitHub Actions 紧密集成。
- [GitLab Container Registry](https://docs.gitlab.com/user/packages/container_registry/) - Registry 专注于在 GitLab CI 中使用其镜像。
- [Harbor](https://github.com/goharbor/harbor) 一个开源可信云原生注册表项目，用于存储、签名和扫描内容。支持复制、用户管理、访问控制和活动审核。
- [JFrog Artifactory](https://jfrog.com/artifactory/) - :yen: Artifact Repository Manager，也可以用作私有 Docker 注册表。
- [kontain.me](https://github.com/imjasonh/kontain.me) - 按需容器镜像注册表，用于在拉取镜像时构建和提供镜像。
- [Kraken](https://github.com/uber/kraken) - Uber 高度可扩展的 P2P docker 注册表，能够在几秒钟内分发 TB 级数据。
- [NORA](https://github.com/getnora-io/nora) - 轻量级多协议工件注册表在单个 32MB 二进制文件中支持 Docker、Maven、npm、Cargo 和 PyPI。拉取缓存、Web UI、Prometheus 指标、RBAC 身份验证。
- [nscr](https://github.com/jhstatewide/nscr) - 一个轻量级、独立的容器注册表，易于运行和维护。
- [Quay.io](https://quay.io/) - :yen：私有 Docker 存储库的安全托管。
- [Registryo](https://github.com/inmagik/registryo) - 用于本地 docker 注册表的基于 UI 和令牌的身份验证服务器。
- [RepoFlow](https://www.repoflow.io) - 一个简单易用的包管理平台，支持 Docker 以及 PyPI、Maven、npm 和 Helm 等其他格式。包括智能搜索、内置 Docker 图像扫描以及适合自托管和云使用的绝佳免费选项。
- [Sonatype Nexus Repository](https://www.sonatype.com/products/sonatype-nexus-repository) - 在整个软件供应链中管理二进制文件并构建工件。

### 注册表 CLI

用于检查、复制和操作 OCI/Docker 注册表中的映像的无守护程序命令行工具。

- [crane](https://github.com/google/go-containerregistry/tree/main/cmd/crane) - 用于操作来自“go-containerregistry”的注册表映像的轻量级 CLI。
- [go-containerregistry](https://github.com/google/go-containerregistry) - 用于处理容器注册表的 Go 库和 CLI 工具（“crane”、“gcrane”、“registry”）。
- [oras](https://github.com/oras-project/oras) - 在任何 OCI 注册表中推送和拉取任意 OCI 工件。
- [regctl](https://github.com/regclient/regclient) - 无守护程序注册表客户端；复制、检查、修改和签署 OCI 映像。
- [skopeo](https://github.com/containers/skopeo) - 使用远程图像注册表：检索信息、复制图像、签署内容。

### 图像扫描和SBOM

图像漏洞扫描器、SBOM 生成器和摘要固定工具。商业条目标记为“:yen:”。

- [Anchor](https://github.com/SongStitch/anchor/) - 一种通过将依赖项固定在 Dockerfile 中来确保可重复构建的工具。
- [Anchor Enterprise](https://anchore.com/) - :yen：根据自定义安全策略分析图像中的 CVE 漏洞。
- [Clair](https://github.com/quay/clair) - Clair 是一个开源项目，用于对 appc 和 docker 容器中的漏洞进行静态分析。
- [Docker Scout](https://github.com/docker/scout-cli) - 用于 SBOM 生成、漏洞分析和策略评估的官方 Docker CLI。
- [Grype](https://github.com/anchore/grype) - 针对容器镜像、文件系统和 SBOM 的漏洞扫描器。
- [oscap-docker](https://github.com/OpenSCAP/openscap) - OpenSCAP提供了oscap-docker工具，用于扫描Docker容器和镜像。
- [pindock](https://github.com/deadnews/pindock) - 在 Dockerfile 中固定和更新 Docker 映像摘要并撰写文件。
- [Syft](https://github.com/anchore/syft) - 用于从容器映像和文件系统生成软件物料清单 (SBOM) 的 CLI 工具和库。
- [Trivy](https://github.com/aquasecurity/trivy) - Aqua Security 的开源简单且全面的容器漏洞扫描器（适合 CI）。

### 供应链

容器镜像的签名、证明和来源。

- [cosign](https://github.com/sigstore/cosign) - OCI 工件的容器签名、验证和透明度日志。
- [in-toto](https://github.com/in-toto/in-toto) - 供应链认证框架；支持 SLSA 和联合签名来源。
- [policy-controller](https://github.com/sigstore/policy-controller) - Kubernetes 准入控制器在容器镜像上强制执行联合签名。
- [witness](https://github.com/in-toto/witness) - 跨构建管道生成并验证整体证明。

## 运行容器

### 成分

- [Composerize](https://github.com/magicmark/composerize) - 将 docker run 命令转换为 docker-compose 文件。
- [ctk](https://github.com/ctk-hq/ctk) - 用于基于容器的工作负载的可视化编辑器。
- [kompose](https://github.com/kubernetes/kompose) - 从 Docker Compose 转向 Kubernetes。
- [plash](https://github.com/ihucos/plash) - 容器运行和构建引擎 - 在 docker 内部运行。
- [podman-compose](https://github.com/containers/podman-compose) - 使用 podman 运行 docker-compose.yml 的脚本。
- [Smalte](https://github.com/roquie/smalte) - 在docker容器中动态配置需要静态配置的应用程序。

### 编排

- [CloudSlang](https://github.com/CloudSlang/cloud-slang) - CloudSlang 是一个用于创建 Docker 流程自动化的工作流引擎。
- [docker rollout](https://github.com/Wowu/docker-rollout) - Docker Compose 服务的零停机部署。
- [Kubernetes](https://github.com/kubernetes/kubernetes) - Google 的 Docker 容器开源编排系统。
- [Mesos](https://github.com/apache/mesos) - 用于容器、虚拟机和物理主机的资源/作业调度程序。
- [Nebula](https://github.com/nebula-orchestrator) - 旨在管理大规模分布式集群的 Docker 编排工具。
- [Nomad](https://github.com/hashicorp/nomad) - 轻松部署任何规模的应用程序。分布式、高可用、数据中心感知的调度程序。
- [Rancher](https://github.com/rancher/rancher) - 一个开源项目，为在生产中运行 Docker 提供了完整的平台。
- [Swarm-cronjob](https://github.com/crazy-max/swarm-cronjob) - 在 Swarm 上按时间安排创建作业。

### 部署和平台

自托管和托管云平台（PaaS/CaaS、部署自动化）。商业条目标记为“:yen:”。

- [Amazon ECS](https://aws.amazon.com/ecs/) - :yen：EC2 上支持 Docker 容器的管理服务。
- [Appfleet](https://appfleet.com/) - ：日元：用于在全球部署和管理容器化服务的边缘平台；将流量路由到最近的位置以实现低延迟。
- [Azure AKS](https://azure.microsoft.com/en-us/products/kubernetes-service/) - ：日元：完全托管的 Kubernetes 容器编排服务。
- [blackfish](https://gitlab.com/blackfish/blackfish) - 用于构建用于开发和生产的群体集群的 CoreOS VM。
- [BosnD](https://gitlab.com/n0r1sk/bosnd) - BosnD，水手长守护进程 - 用于动态更改容器环境的动态配置文件编写器和服务重新加载器。
- [caprover](https://github.com/caprover/caprover) - [以前称为 CaptainDuckDuck] 自动可扩展 Web 服务器包（自动 Docker+nginx） - Heroku on Steroids。
- [Cloud 66](https://www.cloud66.com) - ：日元：全栈托管容器管理即服务。
- [Cloud Run Compose](https://docs.cloud.google.com/run/docs/deploy-run-compose) - :yen: 将 `docker-compose.yaml` 文件作为托管服务直接部署到 Google Cloud Run。
- [Convox Rack](https://github.com/convox/rack) - Convox Rack 是构建在专家基础设施自动化和 DevOps 最佳实践之上的开源 PaaS。
- [docker-to-iac](https://github.com/deploystackio/docker-to-iac) - 将 docker run 和 commit 转换为 AWS、Render.com 和 DigitalOcean 的基础设施即代码模板。
- [doco-cd](https://github.com/kimdre/doco-cd) - 轻量级 GitOps 和持续部署工具，用于使用轮询和 Webhooks 部署 Docker Compose 项目和 Swarm 堆栈。
- [Dokku](https://github.com/dokku/dokku) - Docker 支持的迷你 Heroku 可帮助您构建和管理应用程序的生命周期。
- [Exoframe](https://github.com/exoframejs/exoframe) - 一种自托管工具，允许使用 Docker 进行简单的单命令部署。
- [Giant Swarm](https://www.giantswarm.io/) - ：日元：简单的微服务基础设施。在几秒钟内部署您的容器。
- [Google Container Engine](https://docs.cloud.google.com/kubernetes-engine/docs) - :yen：由 [Kubernetes][kubernetes] 提供支持的 Google 云计算上的 Docker 容器。
- [Grafeas](https://github.com/grafeas/grafeas) - 有关容器的元数据的通用 API，从图像和构建详细信息到安全漏洞。
- [Mesosphere DC/OS Platform](https://d2iq.com/products/dcos) - :yen：基于 Apache Mesos 构建的数据和容器集成平台。
- [OpenShift][openshift] - 一个基于 [Kubernetes][kubernetes] 构建的开源 PaaS，并由 [Red Hat](https://www.redhat.com/en) 针对 Docker 化应用程序开发和部署进行了优化
- [Red Hat OpenShift Dedicated](https://www.redhat.com/en/technologies/cloud-computing/openshift/dedicated) - ：日元：Amazon Web Services 和 Google Cloud 上完全托管的 Red Hat® OpenShift® 服务。
- [swarm-ansible](https://github.com/LombardiDaniel/swarm-ansible?tab=readme-ov-file) - Swarm-Ansible 使用 ansible 引导生产就绪的 swarm 集群。附带自动化 CI 工具，帮助监控和为 SSL 证书和简单身份验证预配置 traefik。带有私人注册表等等！
- [SwarmManagement](https://github.com/hansehe/SwarmManagement) - Swarm Management 是一个 python 应用程序，通过 pip 安装。该应用程序通过配置单个 yaml 文件来轻松管理 Docker Swarm，该文件描述要部署的堆栈以及要创建的网络、配置或机密。
- [Triton](https://www.joyent.com/) - ：日元：弹性容器原生基础设施。
- [Tsuru](https://github.com/tsuru/tsuru) - Tsuru 是一个可扩展的开源平台即服务软件。
- [werf](https://github.com/werf/werf) - Werf 是一个 CI/CD 工具，用于高效构建 Docker 镜像并使用 GitOps 将其部署到 Kubernetes。

### 垃圾收集

- [docker-custodian](https://github.com/Yelp/docker-custodian) - 保持 docker 主机整洁。
- [Docuum](https://github.com/stepchowfun/docuum) - 最近最少使用 (LRU) 驱逐 Docker 镜像。

## 网络和代理

### 网络

容器网络、覆盖网络、DNS/服务发现桥。

- [Calico][calico] - Calico 是一个纯第 3 层虚拟网络，允许多个 docker 主机上的容器相互通信。
- [docker-dns](https://github.com/bytesharky/docker-dns) - 适用于 Docker 容器的轻量级 DNS 转发器，在主机上解析具有自定义后缀（例如“.docker”）的容器名称，以简化服务发现。
- [Flannel](https://github.com/coreos/flannel/) - Flannel 是一个虚拟网络，为每个主机提供一个子网以供容器运行时使用。
- [netshoot](https://github.com/nicolaka/netshoot) - netshoot 容器拥有一组强大的网络工具，可以帮助解决 Docker 网络问题。
- [Pipework](https://github.com/jpetazzo/pipework) - 适用于 Linux 容器的软件定义网络，Pipework 可与“普通”LXC 容器以及出色的 Docker 配合使用。
- [registrator](https://github.com/gliderlabs/registrator) - Docker 的服务注册表桥。

### 反向代理

具有自动发现功能的容器感知反向代理、入口和 TLS 终止前端。

- [BunkerWeb](https://github.com/bunkerity/bunkerweb) - 开源和下一代 Web 应用程序防火墙 (WAF)。
- [caddy-docker-proxy](https://github.com/lucaslorentz/caddy-docker-proxy) - 基于 Caddy 的反向代理，配置有服务或容器标签。
- [caddy-docker-upstreams](https://github.com/invzhi/caddy-docker-upstreams) - Docker 为 Caddy 提供上游模块，配置了容器标签。
- [Docker Dnsmasq Updater](https://github.com/moonbuggy/docker-dnsmasq-updater) - 使用 Docker 容器主机名更新远程 dnsmasq 服务器。
- [docker-flow-proxy](https://github.com/docker-flow/docker-flow-proxy) - 每次部署新服务或扩展服务时重新配置代理。
- [Let's Encrypt Nginx-proxy Companion](https://github.com/nginx-proxy/docker-letsencrypt-nginx-proxy-companion) - nginx-proxy 的轻量级配套容器。它允许自动创建/续订 Let's Encrypt 证书。
- [mesh-router](https://github.com/Yundera/mesh-router) - 用于具有自动 HTTPS 路由的 Docker 容器的免费域 (nsl.sh) 提供商。使用 Wireguard VPN 跨网络安全地路由子域请求。非常适合自托管 NAS 和云部署。
- [Nginx Proxy Manager](https://github.com/jc21/nginx-proxy-manager) - 一个漂亮的 Web 界面，用于使用 SSL 代理基于 Web 的服务。
- [nginx-proxy][nginxproxy] - 使用 docker-gen 为 Docker 容器提供自动化 nginx 代理。
- [OpenResty Manager](https://github.com/Safe3/openresty-manager) - 最简单易用、功能强大、美观的 OpenResty Manager（Nginx 增强版），OpenResty Edge 的开源替代品。
- [Swarm Router](https://github.com/flavioaiello/swarm-router) - 用于 docker swarm 模式的基于零配置服务名称的路由器，采用全新且更安全的方法。
- [Træfɪk](https://github.com/containous/traefik) - 适用于 Docker、Mesos、Consul 等的自动反向代理和负载均衡器。

## 存储和数据

- [Label Backup](https://github.com/resulgg/label-backup) - 一个轻量级、Docker 感知的备份代理，可根据 Docker 标签自动发现和备份容器化数据库（PostgreSQL、MySQL、MongoDB、Redis）。支持本地存储和与 S3 兼容的目标，并通过 cron 表达式进行灵活调度。
- [Docker 卷备份](https://github.com/offen/docker-volume-backup) 将 Docker 卷备份到本地或任何 S3 兼容存储。
- [Netshare](https://github.com/ContainX/docker-volume-netshare) Docker NFS、AWS EFS、Ceph 和 Samba/CIFS 卷插件。
- [portworx](https://portworx.com) - ：日元：用于持久、共享和复制卷的去中心化存储解决方案。
- [quobyte](https://www.quobyte.com/) - :yen: 具有 docker 卷驱动程序的完全容错分布式文件系统。
- [REX-Ray](https://github.com/rexray/rexray) 提供与供应商无关的存储编排引擎。主要设计目标是为 Docker、Kubernetes 和 Mesos 提供持久存储。

## 可观察性

监控 Docker 主机、容器以及其中运行的服务。自托管和SaaS结合在一起；商业条目标记为“:yen:”。

- [ADRG](https://github.com/jaldertech/adrg) - 使用 cgroups v2 的动态 Docker 资源调控器来管理系统负载。
- [AppDynamics](https://github.com/Appdynamics/docker-monitoring-extension) - :yen: Docker 监控扩展使用 Unix Socket 或 TCP 从 Docker Remote API 收集指标。
- [Autoheal](https://github.com/willfarrell/docker-autoheal) - 自动监控并重新启动不健康的 docker 容器。
- [Better Stack](https://betterstack.com/community/guides/scaling-docker/) - :yen：与 Docker 兼容的可观察性堆栈，为容器化应用程序提供日志聚合和正常运行时间监控。
- [cAdvisor](https://github.com/google/cadvisor) - 分析运行容器的资源使用情况和性能特征。
- [Datadog](https://www.datadoghq.com/) - :yen：全栈监控服务，具有一流的 Docker、Kubernetes 和 Mesos 支持。
- [DLIA](https://github.com/zorak1103/dlia) - DLIA 是一种基于 AI 的 Docker 日志监控代理，它使用大型语言模型 (LLM) 来智能分析容器日志、检测异常并随时间提供上下文洞察。
- [docker-exporter](https://github.com/dlepaux/docker-exporter) - 用 Rust 编写的用于 Docker 容器指标的轻量级 Prometheus 导出器。 ARM64 (Raspberry Pi 5) 上正确的 cgroup v2 内存工作集，使用只读套接字以非 root 方式运行，约 7 MiB 空闲 RAM。
- [Docker-Sentinel](https://github.com/Will-Luck/Docker-Sentinel) - 通过每个容器的策略、回滚安全性和实时 Web 仪表板自动更新容器。
- [DockProbe](https://github.com/deep-on/dockprobe) - 单个容器中的轻量级 Docker 监控仪表板。实时指标、6 个异常检测规则、Telegram 警报和 16 个自动安全扫描。零配置，~50MB RAM。
- [DockProc](https://gitlab.com/n0r1sk/dockproc) - 进程级别容器的 I/O 监控。
- [dockprom](https://github.com/stefanprodan/dockprom) - 使用 Prometheus、Grafana、cAdvisor、NodeExporter 和 AlertManager 监控 Docker 主机和容器。
- [Doku](https://github.com/amerkurev/doku) - Doku 是一个简单的基于 Web 的应用程序，可让您监控 Docker 磁盘使用情况。
- [Dozzle](dozzle) - 使用浏览器或移动设备实时监控容器日志。
- [Drydock](https://github.com/CodesWhat/drydock) - 使用 Web 仪表板、23 个注册表提供程序、20 个通知触发器和分布式代理架构进行容器更新监控。
- [Dynatrace](https://docs.dynatrace.com/docs/observe/infrastructure-observability/container-platform-monitoring) - ：日元：无需安装代理或修改运行命令即可监控容器化应用程序。
- [Grafana Docker Dashboard Template](https://grafana.com/grafana/dashboards/179-docker-prometheus-monitoring/) - 适用于 Docker、Grafana 和 Prometheus 堆栈的模板。
- [Maintenant](https://github.com/kolapsis/maintenant) - Docker 和 Kubernetes 的自我发现基础设施监控。通过标签自动检测容器，并具有端点监控、心跳、TLS 证书、资源指标、更新智能和内置状态页面。具有嵌入式 SPA 的单个二进制文件。
- [Middleware](https://middleware.io/) - :yen：从统一的可观察平台监控 Docker 主机、容器、日志和应用程序性能。
- [Site24x7](https://www.site24x7.com/docker-monitoring.html) - :yen：用于 DevOps 和 IT 的 Docker 监控，SaaS 按主机付费模式。
- [Sysdig Monitor](https://www.sysdig.com/products/monitor) - ：日元：使用系统调用对容器进行监控、警报和故障排除的软件或 SaaS 服务； Docker 和 Kubernetes 的容器特定功能。
- [Wiremap](https://github.com/codeofmario/wiremap) - 一个自托管的可视化 Docker 网络拓扑浏览器，具有实时日志流、实时统计、嵌入式终端和容器检查功能。

## 安全性

容器强化、运行时安全、策略、合规性和取证。自托管与商业并存；商业条目标记为“:yen:”。

- [Aqua Security](https://www.aquasec.com) - ：日元：在任何平台上保护基于容器的应用程序从开发到生产的安全。
- [buildcage](https://github.com/dash14/buildcage) - 在 Docker 构建期间限制出站网络访问，以防止供应链攻击，充当 Docker Buildx 的嵌入式 BuildKit 远程驱动程序，并具有即用型 GitHub Actions。
- [CetusGuard](https://github.com/hectorm/cetusguard) - CetusGuard 是一个通过过滤对其 API 端点的调用来保护 Docker 守护进程套接字的工具。
- [Checkov](https://github.com/bridgecrewio/checkov) - 对基础设施即代码清单（Terraform、Kubernetes、Cloudformation、Helm、Dockerfile、Kustomize）进行静态分析，发现安全错误配置并修复它们。
- [container-explorer](https://github.com/google/container-explorer) - 用于从已安装的磁盘映像中探索 Docker 和 containerd 容器详细信息的取证实用程序。
- [Deepfence Threat Mapper](https://github.com/deepfence/ThreatMapper) - 适用于 kubernetes、虚拟机和无服务器的强大运行时漏洞扫描器。
- [Den](https://github.com/us/den) - 用于 AI 代理的自托管沙箱运行时，具有 Docker 容器、安全强化、REST API 和 WebSocket 支持。
- [docker-bench-security](https://github.com/docker/docker-bench-security) - 用于检查在生产中部署 Docker 容器的数十种常见最佳实践的脚本。
- [docker-socket-proxy](https://github.com/Tecnativa/docker-socket-proxy) - 针对 Docker API 套接字的基于 HAProxy 的细粒度过滤器；广泛用于向反向代理和家庭实验室堆栈公开受限套接字。
- [KICS](https://github.com/checkmarx/kics) - 基础设施即代码扫描工具，可在开发周期的早期发现安全漏洞、合规性问题和基础设施错误配置。可以延长附加政策。
- [Prisma Cloud](https://www.paloaltonetworks.com/prisma/cloud) - ：yen：（以前称为 Twistlock Security Suite）检测漏洞、强化容器映像并在应用程序的整个生命周期中强制执行安全策略。
- [segspec](https://github.com/dormstern/segspec) - 从 Docker Compose、Kubernetes 清单、Helm 图表和其他配置文件中提取网络依赖项，以生成带有证据跟踪的 Kubernetes NetworkPolicies。
- [Sysdig Falco](https://github.com/falcosecurity/falco) - Sysdig Falco 是一个开源容器安全监视器。它可以监控应用程序、容器、主机和网络活动，并对未经授权的活动发出警报。
- [Sysdig Secure](https://www.sysdig.com/solutions/cloud-detection-and-response-cdr) - :yen: Sysdig Secure 通过行为监控和防御解决运行时安全问题，并提供基于开源 Sysdig 的深度取证以进行事件响应。
- [Trend Micro DeepSecurity](https://www.trendmicro.com/en_us/business/products/hybrid-cloud/deep-security.html) - ：日元：趋势科技 DeepSecurity 为容器工作负载和主机提供运行时保护，以及运行前图像扫描，以识别漏洞、恶意软件和硬编码机密等内容。

## 用户界面

### 桌面

用于管理和监控 Docker 主机和集群的本机桌面应用程序

- [Docker DB Manager](https://github.com/AbianS/docker-db-manager) - 用于管理 Docker 数据库容器的桌面应用程序，具有可视化界面和一键操作。
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) - 官方原生应用程序。仅适用于 Windows 和 MacOS。
- [Simple Docker UI](https://github.com/felixgborrego/simple-docker-ui) - 基于电子构建。
- [Stevedore](https://github.com/slonopotamus/stevedore) - Windows 的良好 Docker 桌面替代品。支持 Linux 和 Windows 容器。 [slonopotamus](https://github.com/slonopotamus)。

### 终端

适用于 Docker 的 TUI、CLI 工具和 shell 集成。

- [d4s](https://github.com/jr-k/d4s) - 快速、键盘驱动的终端 UI，可利用 K9s 的人体工程学原理来管理 Docker 容器、Compose 堆栈和 Swarm 服务。
- [dcinja](https://github.com/Falldog/dcinja) - 适用于 docker 命令行环境的强大且最小二进制大小的模板引擎。
- [dctl](https://github.com/FabienD/docker-stack) - Dctl 是一个 Cli 工具，可以帮助开发人员在终端的任何位置执行所有 docker compose 命令等。
- [decompose](https://github.com/s0rg/decompose) - 适用于 Docker 环境的逆向工程工具。
- [dive](https://github.com/wagoodman/dive) - 用于探索 docker 镜像中每一层的工具。
- [docker pushrm](https://github.com/christian-korneck/docker-pushrm) - 一个 Docker CLI 插件，可让您将 README.md 文件从当前目录推送到 Docker Hub。还支持码头和港口。
- [docker-captain](https://github.com/lucabello/docker-captain) - 一个友好的 CLI，用于管理多个 Docker Compose 部署，由 Typer、Rich、questionary 和 sh 提供支持。
- [dockerfile-mode](https://github.com/spotify/dockerfile-mode) - 用于处理 Dockerfile 的 Emacs 模式。
- [dockerfilegraph](https://github.com/patrickhoefler/dockerfilegraph) - 可视化您的多阶段 Dockerfile。
- [dockly](https://github.com/lirantal/dockly) - 用于管理 Docker 容器的交互式 shell UI。
- [DockMate](https://github.com/shubh-io/dockmate) - 基于终端的轻量级 Docker 和 Podman 管理器，具有基于文本的用户界面。
- [DockSTARTer](https://github.com/GhostWriters/DockSTARTer) - DockSTARTer 可帮助您开始使用在 Docker 中运行的家庭服务器应用程序。
- [DockTUI](https://github.com/strmax195-hue/docktui) - 适用于 Docker 和 Compose 的快速、零依赖终端仪表板。
- [dprs](https://github.com/durableprogramming/dprs) - 以开发人员为中心的 TUI，用于通过实时日志流和容器管理来管理 Docker 容器。
- [dry](https://github.com/moncho/dry) - Docker 容器的交互式 CLI。
- [easydocker](https://github.com/joao-zanutto/easydocker) - 终端 UI 深受 k9s 启发，利用漂亮的 BubbleTea 图形。
- [goManageDocker](https://github.com/ajayd-san/gomanagedocker) - TUI 工具可通过合理的键绑定快速查看和管理 docker 对象，还支持开箱即用的 VIM 导航。
- [lazydocker](https://github.com/jesseduffield/lazydocker) - 管理一切的更懒惰的方式 docker。适用于 docker 和 docker-compose 的简单终端 UI，使用 Gocui 库用 Go 编写。
- [lazyjournal](https://github.com/Lifailon/lazyjournal) - 用于读取和过滤 Docker 和 Podman 容器的日志输出的接口，例如 [Dozzle](dozzle)，但适用于支持模糊查找、正则表达式和输出着色的终端。
- [oxker](https://github.com/mrjackwills/oxker) - 一个简单的 tui 来查看和控制 docker 容器。
- [proco](https://github.com/shiwaforce/poco) - Proco 将帮助您使用简单的 YAML 配置文件来组织和管理任何复杂程度的 Docker、Docker-Compose、Kubernetes 项目，以缩短从找到项目到在本地环境中初始化项目的过程。
- [scuba](https://github.com/JonathonReinhart/scuba) - 透明地使用 Docker 容器来封装软件构建环境。
- [supdock](https://github.com/segersniels/supdock) - 通过交互式提示，可以更直观地使用 Docker。
- [swarmcli](https://github.com/Eldara-Tech/swarmcli) - 以思维速度进行 Swarm 管理 — 具有实时日志流、对容器的即时 shell 访问、无缝端口转发和按需秘密揭示功能，让您可以完全控制 Docker Swarm，而不会中断流程。
- [tdocker](https://github.com/pivovarit/tdocker) - 用于日常容器操作的“docker ps”替代品。
- [wharf](https://github.com/idesyatov/wharf) - 受 k9s 启发的 Docker Compose TUI，具有 vim 式导航、带盲文图表的实时 CPU/MEM 监控、容器文件浏览器、SSH 远程主机支持和命令模式。

### 网络

- [Arcane](https://github.com/getarcaneapp/arcane) - 一个简单而现代的 Docker 管理平台，专为每个人而构建。
- [CASA](https://github.com/knrdl/casa) - 将少量容器的管理外包给您的同事。
- [Container Web TTY](https://github.com/wrfly/container-web-tty) - 通过 web-tty 连接您的容器。
- [Docker Registry Browser](https://github.com/klausmeyer/docker-registry-browser) - Docker 注册表 HTTP API v2 的 Web 界面。
- [docker-swarm-visualizer](https://github.com/dockersamples/docker-swarm-visualizer) - 可视化 Docker Swarm 上的 Docker 服务（用于运行演示）。
- [dockge](https://github.com/louislam/dockge) - 易于使用且反应式的自托管 docker compose.yaml 面向堆栈的管理器。
- [Komodo](https://github.com/mbecker20/komodo) - 在许多服务器上构建和部署软件的工具。
- [Portainer](https://github.com/portainer/portainer) - 用于管理 Docker 主机或 Docker Swarm 集群的轻量级管理 UI。
- [Swarmpit](https://github.com/swarmpit/swarmpit) - Swarmpit 为您的 Docker Swarm 集群提供简单易用的界面。您可以管理您的堆栈、服务、秘密、卷、网络等。
- [usulnet](https://github.com/fr4nsys/usulnet) - 一个完整且现代的 Docker 管理平台，专为系统管理员、devops 设计，具有企业级工具、cve 扫描器、ssh、网络上的 rdp 等。

### 集成开发环境

- JetBrains IDE（IntelliJ IDEA、GoLand、WebStorm、CLion 等）具有[内置 Docker 插件](https://www.jetbrains.com/help/idea/docker.html#managing-images)
- Eclipse [Docker 工具插件](https://www.eclipse.org/community/eclipse_newsletter/2016/july/article2.php)
- [docker.el](https://github.com/Silex/docker.el) 从 Emacs 管理 docker。

## 开发人员工作流程

### API客户端

- [contajners](https://github.com/lispyclouds/contajners) - 用于 OCI 容器引擎的惯用的、数据驱动的、REPL 友好的 Clojure 客户端。
- [Docker Client for JVM](https://github.com/gesellix/docker-client) - 用于 JVM 的 Docker 远程 api 客户端库，用 Groovy 编写。
- [Docker Client TypeScript](https://gitlab.com/masaeedu/docker-client) - JavaScript 的 Docker API 客户端，根据 moby 存储库的 Swagger API 定义自动生成。
- [docker-controller-bot](https://github.com/dgongut/docker-controller-bot) - 用于控制 Docker 容器的 Telegram 机器人。
- [docker-maven-plugin](https://github.com/fabric8io/docker-maven-plugin) - 用于运行和创建 Docker 映像的 Maven 插件。
- [Docker.DotNet](https://github.com/Microsoft/Docker.DotNet) - Docker 远程 API 的 C#/.NET HTTP 客户端。
- [Docker.Registry.DotNet](https://github.com/ChangemakerStudios/Docker.Registry.DotNet) - 用于与 Docker 注册表 API (v2) 交互的 .NET (C#) 客户端库。
- [dockerode](https://github.com/apocas/dockerode) - Docker Remote API node.js 模块。
- [go-dockerclient](https://github.com/fsouza/go-dockerclient/) - Docker 远程 API 的 HTTP 客户端。
- [Gradle Docker plugin](https://github.com/gesellix/gradle-docker-plugin) - Gradle 的 Docker 远程 api 插件。
- [Portainer stack utils](https://github.com/greenled/portainer-stack-utils) - 用于从 docker-compose yaml 文件在 Portainer 实例中部署/更新/取消部署 Docker 堆栈的 Bash 脚本。
- [sbt-docker](https://github.com/marcuslonnberg/sbt-docker) - 直接从 sbt 创建 Docker 镜像。

### 持续集成/持续交付

自托管 CI 引擎、构建加速器以及针对 Docker 工作流程的托管服务。商业条目标记为“:yen:”。

- [Buddy](https://buddy.works) - :yen：最好的 Git、构建和部署工具组合成一个强大的工具，增强了我们的开发能力。
- [Captain](https://github.com/harbur/captain) - 将您的 Git 工作流程转换为 Docker 容器，为持续交付做好准备。
- [CircleCI](https://circleci.com/) - :yen：从构建环境中推送或拉取 Docker 镜像，或者直接在 CircleCI 上构建和运行容器。
- [CodeFresh](https://octopus.com/codefresh) - :yen：Docker 应用程序的端到端构建、测试和共享，以及自动化测试。
- [ConcourseCI](https://concourse-ci.org) - ：日元：面向 DevOps 团队的面向管道的 CI SaaS 平台。
- [Defang](https://github.com/DefangLabs/defang) - 只需几分钟即可将 Docker Compose 部署到您最喜欢的云。
- [Depot](https://depot.dev) - :yen: 在云中快速构建 Docker 镜像。极快的计算、自动智能缓存和零配置。
- [Diun](https://github.com/crazy-max/diun) - 当 Docker 注册表上的映像或存储库更新时接收通知。
- [dockcheck](https://github.com/mag37/dockcheck) - 检查 docker 镜像更新的脚本，无需拉取，然后自动更新所选/所有容器。具有通知、修剪等功能。
- [Docker plugin for Jenkins](https://github.com/jenkinsci/docker-plugin/) - docker 插件的目标是能够使用 docker 主机动态配置从属设备，运行单个构建，然后拆除该从属设备。
- [Drone](https://github.com/drone/drone) - 基于 Docker 构建并使用 YAML 文件进行配置的持续集成服务器。
- [Gantry](https://github.com/shizunge/gantry) - 自动更新选定的 Docker swarm 服务。
- [GitLab Runner](https://gitlab.com/gitlab-org/gitlab-runner) - GitLab 集成了 CI，可以使用 GitLab 运行程序来测试、构建和部署您的代码。
- [Jaypore CI](https://github.com/theSage21/jaypore_ci) - 用 Python 配置的简单、非常灵活、强大的 CI/CD/自动化系统。离线和本地优先。
- [Kraken CI](https://github.com/Kraken-CI/kraken) - 现代 CI/CD、开源、本地部署系统，具有高度可扩展性并专注于测试。它的执行者之一是 Docker。发达。
- [Screwdriver](https://screwdriver.cd/) - ：日元：雅虎的开源构建平台，专为持续交付而设计。
- [Semaphore CI](https://semaphore.io/) - :yen：高性能云 CI，用于构建、测试容器并将其运送到生产环境。
- [Skipper](https://github.com/Stratoscale/skipper) - 轻松 Docker 化您的 Git 存储库。
- [Tekton CD](https://tekton.dev/) - 云原生管道资源。
- [TravisCI](https://www.travis-ci.com/) - :yen: 托管 GitHub 项目的 CI，支持 Docker。

### 开发环境

- [coder](https://github.com/coder/coder) - 由 Terraform 或 Docker 提供支持的远程开发机器。
- [dde](https://github.com/whatwedo/dde) - 基于Docker的本地开发环境工具集。
- [DIP](https://github.com/bibendi/dip) - CLI 实用程序，用于直接配置并与 docker-compose 配置的应用程序交互。
- [EnvCLI](https://github.com/EnvCLI/EnvCLI) - 将本地安装的 Node、Go 等替换为项目特定的 docker 容器。
- [Gebug](https://github.com/moshebe/gebug) - 该工具通过无缝启用调试器和热重载功能，使 Dockerized Go 应用程序的调试变得超级简单。
- [HarborPilot](https://github.com/potterwhite/HarborPilot) - 用于嵌入式 Linux 开发的自动化多平台 Docker 映像生成器（RK3588、RV1126、RK3568）。具有三层配置继承、基于PORT_SLOT的端口分配和跨版本Ubuntu支持（20.04/22.04/24.04）。
- [Lando](https://github.com/lando/lando) - Lando 适合那些想要快速指定并轻松启动开发项目所需的服务和工具的开发人员。
- [uniget](https://github.com/uniget-org/cli) - Uni(versal)get，容器工具及其他工具的安装程序和更新程序（以前称为 docker-setup）。
- [Zsh-in-Docker](https://github.com/deluan/zsh-in-docker) - 只需一行即可在 Docker 容器内安装 Zsh、Oh-My-Zsh 和插件！

### 无服务器

- [Apache OpenWhisk](https://github.com/apache/openwhisk) - 一个无服务器的开源云平台，可以执行响应任何规模事件的功能。
- [Koyeb](https://www.koyeb.com/) - :yen: Koyeb 是一个开发人员友好的无服务器平台，用于在全球部署应用程序。通过基于 git 的部署、本机自动缩放、全球边缘网络以及内置服务网格和发现，无缝运行 Docker 容器、Web 应用程序和 API。
- [OpenFaaS](https://github.com/openfaas/faas) - 适用于 Docker 和 Kubernetes 的完整无服务器功能框架。

### 测试

- [Container Structure Test](https://github.com/GoogleContainerTools/container-structure-test) - 通过检查命令的输出或文件系统的内容来验证图像结构的框架。
- [dgoss](https://github.com/goss-org/goss/tree/master/extras/dgoss) - 一个基于 YAML 的快速工具，用于验证 docker 容器。
- [Kurtosis](https://github.com/kurtosis-tech/kurtosis) - 用于多容器测试环境的可组合构建系统，为开发人员提供：用于环境配置的强大的类似 Python 的 SDK，用于验证环境行为和设置的编译时验证器，以及用于环境执行、监控和调试功能的运行时。
- [Pumba](https://github.com/alexei-led/pumba) - Docker 的混沌测试工具。可以部署在kubernetes和CoreOS集群上。

### 包装纸

- [Hokusai](https://github.com/artsy/hokusai) - 面向应用程序开发人员的 Docker + Kubernetes CLI；用于容器化应用程序并在整个开发、测试和发布周期中管理其生命周期。来自 [artsy](https://github.com/artsy)。
- [Preevy](https://github.com/livecycle/preevy) - Docker 和 Docker Compose 项目的预览环境。通过将拉取请求作为 CI 管道的一部分部署到云提供商，测试您的更改并从开发人员和非开发人员（产品/设计）获取反馈。
- [subuser](https://github.com/subuser-security/subuser) - 可以轻松地在 Docker 中安全、可移植地运行图形桌面应用程序。
- [udocker](https://github.com/indigo-dc/udocker) - 一种无需 root 权限即可在批处理或交互式系统中执行简单 docker 容器的工具。
- [Vagrant - Docker provider](https://developer.hashicorp.com/vagrant/docs/providers/docker/basics) - 好的起点是[vagrant-docker-example](https://github.com/bubenkoff/vagrant-docker-example)。

## 容器内工具

安装在容器内或设计为作为 [sidecar] 运行的工具和应用程序(https://learn.microsoft.com/en-us/azure/architecture/patterns/sidecar)

- [cdebug](https://github.com/iximiuz/cdebug) - 用于通过临时 sidecar 调试正在运行的容器的瑞士军刀；可与 Docker、containerd 和 Kubernetes 配合使用。
- [ckron](https://github.com/nicomt/ckron) - docker 的 cron 风格的作业调度程序。
- [CoreOS][coreos] - 用于大规模服务器部署的 Linux
- [docker-gen](https://github.com/jwilder/docker-gen) - 从 docker 容器元数据生成文件。
- [dockerize](https://github.com/powerman/dockerize) - 用于简化 Docker 容器中运行应用程序的实用程序。
- [GoSu](https://github.com/tianon/gosu) - 作为该特定用户运行该特定应用程序并退出管道（入口点脚本工具）。
- [is-docker](https://github.com/sindresorhus/is-docker) - 检查进程是否在 Docker 容器内运行。
- [microcheck](https://github.com/tarampampam/microcheck) - 纯 C 语言中的 Docker 容器轻量级运行状况检查实用程序（httpcheck 与 cURL 分别为 75 KB，而不是 9.3 MB） - http(s)、端口检查和并行执行。
- [Ofelia](https://github.com/mcuadros/ofelia/) - Ofelia 是一个基于 Go 构建的现代且占用空间少的作业调度程序，适用于 Docker 环境。 Ofelia 的目标是成为老式 cron 的替代者。支持从容器标签和/或配置文件进行配置。
- [su-exec](https://github.com/ncopa/su-exec) - 这是一个简单的工具，可以简单地执行具有不同权限的程序。该程序将直接执行，而不是像 su 和 sudo 一样作为子程序运行，这避免了 TTY 和信号问题。为什么要重新发明 gosu？这或多或少与 gosu 完全相同，但它只有 10kb 而不是 1.8MB。
- [supercronic](https://github.com/aptible/supercronic) - 与 Crontab 兼容的作业运行程序，专门设计用于在容器中运行。

# 学习资源

## 从哪里开始

- [使用 Docker 的好处](https://semaphore.io/blog/docker-benefits) 进行开发和交付，并提供实用的采用路线图。
- [Bootstrapping Microservices](https://www.manning.com/books/bootstrapping-microservices-with-docker-kubernetes-and-terraform) - 这是一份基于项目的实用指南，用于使用微服务构建应用程序，首先为单个微服务构建 Docker 映像并将其发布到私有容器注册表，最后将完整的微服务应用程序部署到生产 Kubernetes 集群。
- [Docker 课程](https://github.com/prakhar1989/docker-curriculum)：Docker 入门的综合教程。教授如何使用 Docker 并通过 Elastic Beanstalk 和 Elastic Container Service 在 AWS 上部署 Docker 化应用程序。
- [Docker 文档](https://docs.docker.com/)：官方文档。
- [Docker 初学者](https://github.com/groda/big_data/blob/master/docker_for_beginners.md)：为需要学习 Docker 基础知识的初学者提供的教程——从“Hello world!”开始与容器的基本交互，以及对基本概念的简单解释。
- [Docker 新手指南](https://www.youtube.com/watch?v=xsjSadjKXns) 为从未使用过 Docker 的开发人员和测试人员介绍 Docker。 （视频 1 点 40 分，2019 年 linux.conf.au 录制 — 新西兰基督城）
- [Docker katas](https://github.com/eficode-academy/docker-katas) 一系列实验将带您从“Hello Docker”到将容器化 Web 应用程序部署到服务器。
- [55 秒内简化 Docker](https://www.youtube.com/watch?v=vP_4DlOH1G4)：对 Docker 的动画高级介绍。将其视为可视化的 tl;dr，可以更轻松地深入了解更复杂的学习材料。
- [Docker Training](https://training.mirantis.com) - ：日元：
- [Dockerlings](https://github.com/furkan/dockerlings)：通过现代 TUI 和小型练习从终端内部学习 docker。
- [Docker 简介](https://blog.stephane-robert.info/docs/contenurs/moteurs-conteneurs/docker/) 在一个关于 DevSecOps 的法国网站上有专门的部分来掌握 Docker：从基础知识到最佳实践，包括优化、保护容器......
- [学习 Docker](https://github.com/dwyl/learn-docker)：分步教程和更多资源（视频、文章、备忘单）
- [Learn Docker (Visually)](https://pagertree.com/learn/docker/overview) - 以初学者为中心，对 Docker 的所有主要组件以及它们如何组合在一起进行高级概述。许多高质量的图像、示例和资源。
- [Play With Docker](https://training.play-with-docker.com/)：PWD 是从初学者到高级用户开始使用 Docker 的好方法。 Docker 直接在浏览器中运行。
- [西班牙语 Docker 命令实用指南](https://github.com/brunocascio/docker-espanol) 该西班牙语指南包含基本 docker 命令的使用以及现实生活中的示例。
- [使用 VScode 和 Docker 设置 Python 开发环境](https://github.com/RamiKrispin/vscode-python)：使用 VScode、Docker 和 Dev Container 扩展设置 Docker 化 Python 开发环境的分步教程。
- [Docker 手册](https://docker-handbook.farhan.dev/) 一本开源书籍，教您基础知识、最佳实践和一些中间 Docker 功能。本书托管在 [fhsinchy/the-docker-handbook](https://github.com/fhsinchy/the-docker-handbook) 上，项目托管在 [fhsinchy/docker-handbook-projects](https://github.com/fhsinchy/docker-handbook-projects) 存储库上。

**备忘单**

- [eon01](https://github.com/eon01/DockerCheatSheet)
- [dimonomid](https://github.com/dimonomid/docker-quick-ref) (PDF)
- [JensPiegsa](https://github.com/JensPiegsa/docker-cheat-sheet)
- [wsargent](https://github.com/wsargent/docker-cheat-sheet)（最受欢迎）

## 从哪里开始（Windows）

- [Windows 上的 Docker 位于防火墙后面](https://toedter.com/2015/05/11/docker-on-windows-behind-a-firewall/)
- [Docker Reference Architecture: Modernizing Traditional .NET Framework Applications](https://docs.mirantis.com/containers/v3.0/dockeree-ref-arch/app-dev/modernize-dotnet-apps.html) - 您将学习识别适合容器化（容器化的“直接迁移”方法）的 .NET Framework 应用程序类型。
- [Docker with Microsoft SQL 2016 + ASP.NET](https://blog.alexellis.io/docker-does-sql2016-aspnet/) 在 Docker 中运行 ASP.NET 和 SQL Server 工作负载的演示
- [在 Linux 和 Windows 容器中使用 Docker 探索 ASP.NET Core](https://www.hanselman.com/blog/exploring-aspnet-core-with-docker-in-both-linux-and-windows-containers) 使用 [Docker for Windows][docker-for-windows] 在 Linux 和 Windows 容器中运行 ASP.NET Core 应用程序
- [在 Windows 容器中运行旧版 ASP.NET 应用程序](https://blog.sixeyed.com/dockerizing-nerd-dinner-part-1-running-a-legacy-asp-net-app-in-a-windows-container/) 对旧版 ASP.NET 应用程序进行 Docker 化并作为 Windows 容器运行的步骤
- [Windows Containers and Docker: The 101](https://www.youtube.com/watch?v=N7SG2wEyQtM) - 20 分钟概述，使用 Docker 运行 PowerShell、ASP.NET Core 和 ASP.NET 应用程序。
- [Windows 容器快速入门](https://learn.microsoft.com/en-us/virtualization/windowscontainers/about/) Windows 容器概述，深入了解 Windows 10 和 Windows Server 2016 的快速入门

---

## 书籍和教程

- [云原生景观](https://github.com/cncf/landscape)
- [Docker Blog](https://www.docker.com/blog/) - 有关 Docker、社区和工具的定期更新。
- [Docker Certification](https://intellipaat.com/docker-training-course/?US) - :yen: 将帮助您通过实践项目和案例研究来学习 Docker 容器化、运行 Docker 容器、镜像创建、Dockerfile、Docker 编排、安全最佳实践等，并帮助您获得 Docker 认证助理。
- [Docker dev bookmarks](https://www.codever.dev/search?q=docker) - 使用标签 [docker](https://www.codever.dev/bookmarks/t/docker)。
- [Docker 实践，第二版](https://www.manning.com/books/docker-in-action-second-edition)
- [Docker 实践，第二版](https://www.manning.com/books/docker-in-practice-second-edition)
- [Docker packaging guide for Python](https://pythonspeed.com/docker/) - 有关 Python 的 Docker 打包细节的一系列详细文章。
- [通过一个月的午餐学习 Docker](https://www.manning.com/books/learn-docker-in-a-month-of-lunches)
- [Learn Docker](https://coursesity.com/blog/best-docker-tutorials/) - 学习 Docker - 精选的顶级在线 Docker 教程和课程列表。
- [编程社区精选的用于学习 Docker 的资源](https://hackr.io/tutorials/learn-docker)

## 很棒的清单

- [Awesome Compose](https://github.com/docker/awesome-compose) - Docker 编写示例。
- [很棒的 Kubernetes](https://github.com/ramitsurana/awesome-kubernetes)
- [Awesome Linux Container](https://github.com/Friz-zy/awesome-linux-containers) 比这个存储库更通用的容器。
- [Awesome Selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) 自由软件网络服务和 Web 应用程序列表，可以通过以经典方式运行（设置本地 Web 服务器并从那里运行应用程序）或在 Docker 容器中运行来本地托管。
- [很棒的系统管理员](https://github.com/n1trux/awesome-sysadmin)
- [ToolsOfTheTrade](https://github.com/cjbarber/ToolsOfTheTrade) SaaS 和本地应用程序列表

## 演示和示例

- [用于前端 Web 开发的带注释的 Docker 配置](https://nystudio107.com/blog/an-annotated-docker-config-for-frontend-web-development) 使用 Docker 的本地开发环境允许您将项目所需的 devops 作为配置进行收缩包装，从而使入门变得顺畅。
- [本地 Docker DB](https://github.com/alexmacarthur/local-docker-db) 许多数据库的 docker-compose 示例列表
- [Webstack-micro](https://github.com/ferbs/webstack-micro) 演示 Web 应用程序，展示如何使用 Docker Compose 设置 API 网关、集中式身份验证、后台工作人员和 WebSocket 作为容器化服务。

## 好建议

- [Docker 警告](http://docker-saigon.github.io/post/Docker-Caveats/) 关于在生产环境中运行 Docker 你应该了解什么（2016 年 4 月 11 日撰写）。
- [桌面上的 Docker 容器](https://blog.jessfraz.com/post/docker-containers-on-the-desktop/)
- [Docker 与 VM？结合两者实现云可移植性涅槃](https://www.flexera.com/blog/finops/)
- [不要在 Docker Compose 文件中重复使用锚点、别名和扩展名](https://medium.com/@kinghuang/docker-compose-anchors-aliases-extensions-a1e4105d70bd)
- [使用 Docker 的 GUI 应用程序](http://fabiorehm.com/blog/2014/09/11/running-gui-apps-with-docker/)

## 树莓派和ARM

- [Docker Pirates 用爆炸性的东西武装起来](https://blog.hypriot.com/) 有关集群、Swarm、Docker、Raspberry Pi 上 SD 卡预装映像的大量资源
- [只需三步即可在 RaspberryPi 上启动并运行 Docker](https://github.com/umiddelb/armhf/wiki/Get-Docker-up-and-running-on-the-RaspberryPi-%28ARMv6%29-in-three-steps)
- [git 将 docker 容器推送到 Linux 设备](https://www.balena.io) 现代 IoT DevOps，利用 git 和 Docker。
- [在armhf (ARMv7) 设备上安装、运行和使用Docker](https://github.com/umiddelb/armhf/wiki/Installing,-running,-using-docker-on-armhf-%28ARMv7%29-devices)

## 安全文章

- [为 Docker 带来新的安全功能](https://opensource.com/business/14/9/security-for-docker)
- [CVE 在 Docker 17.05 中使用多阶段构建扫描 Alpine 镜像](https://github.com/tomwillfixit/alpine-cvecheck)
- [Docker 安全部署指南](https://github.com/AonCyberLabs/Docker-Secure-Deployment-Guidelines)
- [Docker 安全 - 快速参考](https://binarymist.io/publication/docker-security/)
- [Docker 安全：您的集装箱是否牢固地固定在船上？幻灯片分享](https://www.slideshare.net/slideshow/docker-security-are-your-containers-tightly-secured-to-the-ship/43834790)
- [如何在官方 Docker 镜像上处理 CVE](https://github.com/docker-library/official-images/issues/1448)
- [Lynis是一个开源安全审计工具，包括Docker审计](https://cisofy.com/lynis/)
- [构建 Docker 镜像的安全最佳实践](https://linux-audit.com/tags/docker/)
- [Docker 安全团队负责人 (Diogo Mónica) 的软件工程电台采访](https://www.se-radio.net/2017/05/se-radio-episode-290-diogo-monica-on-docker-security/)
- [十个 Docker 镜像安全最佳实践备忘单](https://snyk.io/blog/10-docker-image-security-best-practices/)
- [前十个最流行的 Docker 镜像每个都至少包含 30 个漏洞](https://snyk.io/blog/top-ten-most-popular-docker-images-each-contain-at-least-30-vulnerabilities/)
- [使用最新的安全增强功能调整 Docker](https://opensource.com/business/15/3/docker-security-tuning)
- [使用 Docker 容器化 Node.js Web 应用程序的 10 个最佳实践](https://snyk.io/blog/10-best-practices-to-containerize-nodejs-web-applications-with-docker/)

## 视频

- [Andrew“Tianon”页面 (InfoSiftr) 为 Docker 做出贡献](https://www.youtube.com/watch?v=1jwo8-1HYYg) (34:31)
- [使用 Docker、Swarm 和一点点 Python 魔法来部署和扩展应用程序](https://www.youtube.com/watch?v=GpHMTR7P2Ms) (3:11:06)
- [Docker 和 SELinux，作者：Red Hat 的 Daniel Walsh](https://www.youtube.com/watch?v=zWGFqMuEHdw) (40:23)
- [Docker 课程](https://www.youtube.com/watch?v=UZpyvK6UGFo)（西班牙语）
- [面向开发人员的 Docker](https://www.youtube.com/watch?v=FdkNAjjO5yQ) (54:26)
- [从头开始 Docker](https://www.youtube.com/playlist?list=PLLhEJK7fQIxD-btrjrqdEfQHbkZnQrmqE) (1:22:01)
- [Docker：如何使用自己的私有注册表](https://www.youtube.com/watch?v=CAewZCBT4PI) (15:01)
- [生产中的 Docker](https://www.youtube.com/watch?v=Glk5d5WP6MI) (36:05)
- [Docker 入门到 Docker Compose](https://www.youtube.com/watch?v=G-s2GXGAjTk) (1:56:45)
- [从头开始的 Docker 注册表](https://www.youtube.com/playlist?list=PLLhEJK7fQIxAz3d4Fj3edq7UcxEhdTCBm) (44:40)
- [从头开始的 Docker Swarm](https://www.youtube.com/playlist?list=PLLhEJK7fQIxAY4gZd1Wl-GsLvg-e9Ap1e) (1:41:28)
- [使用插件扩展 Docker](https://vimeo.com/110835013) (15:21)
- [从本地 Docker 开发到生产部署](https://www.youtube.com/watch?v=7CZFpHUPqXw)
- [使用 Docker 和 EC2 的不可变基础设施，作者：Michael Bryzek (Gilt)](https://www.youtube.com/watch?v=GaHzdqFithc) (42:04)
- [Docker 和容器简介](https://www.youtube.com/watch?v=ZVaRK10HBjo) (3:09:00)
- [登录 Docker：您需要了解什么](https://vimeo.com/123341629) (51:27)
- [Docker 性能分析 - Jeremy Eder](https://www.youtube.com/watch?v=6f2E6PKYb0w) (1:36:58)
- [使用 Kubernetes 实现可扩展微服务](https://www.udacity.com/course/scalable-microservices-with-kubernetes--ud615) 免费 Udacity 课程
- [容器现状：与 CoreOS、VMware 和 Google 的辩论](https://www.youtube.com/watch?v=IiITP3yIRd8) (27:38)

## 社区和聚会

### 巴西人

- [Telegram 上的 Docker BR](https://telegram.me/dockerbr)

### 英语

- [Docker 社区](https://www.docker.com/community/)
- [码头工人事件](https://www.docker.com/events/)
- [Docker 在线聚会](https://www.meetup.com/en-AU/Docker-Online-Meetup/)
- [Docker Reddit 社区](https://www.reddit.com/r/docker/)

### 俄语

- [Docker 俄语社区](https://t.me/docker_ru)

### 西班牙语

- [Docker 技巧](https://dockertips.com/)

## 随着时间的推移观星者

[![Stargazers over time](https://starchart.cc/veggiemonk/awesome-docker.svg?variant=adaptive)](https://starchart.cc/veggiemonk/awesome-docker)

[印花布]：https://github.com/projectcalico/calico
[coreos]：https://github.com/coreos
[发行版]：https://github.com/docker/distribution
[docker-for-windows]：https://docs.docker.com/desktop/setup/install/windows-install/
[editreadme]：https://github.com/veggiemonk/awesome-docker/edit/master/README.md
[kubernetes]：https://kubernetes.io
[nginxproxy]：https://github.com/nginx-proxy/nginx-proxy
[openshift]：https://okd.io/
[sindresorhus]：https://github.com/sindresorhus/awesome

