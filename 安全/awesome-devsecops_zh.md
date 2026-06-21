![太棒了](media/banner.png)

<p对齐=“中心”>
  <a href="https://awesome.re">
    <img alt="Awesome" src="https://awesome.re/badge-flat.svg">
</a>
</p>
<hr/>

> 策划最好的 DevSecOps 资源和工具。

[DevSecOps](https://www.rapid7.com/fundamentals/devsecops/) 是 [DevOps](https://www.atlassian.com/devops) 运动的延伸，旨在通过以开发人员为中心的安全工具和流程将安全实践引入开发生命周期。

欢迎贡献。通过拉取请求添加链接或创建问题以开始讨论。

<!-- omit in toc -->
## 内容
- [Resources](#resources)
  - [Articles](#articles)
  - [Books](#books)
  - [Communities](#communities)
  - [Conferences](#conferences)
  - [Newsletters](#newsletters)
  - [Podcasts](#podcasts)
  - [安全开发指南](#secure-development-guidelines)
  - [安全开发生命周期框架](#secure-development-lifecycle-framework)
  - [Toolchains](#toolchains)
  - [Training](#training)
  - [Wikis](#wikis)
- [Tools](#tools)
  - [依赖管理](#dependency-management)
  - [动态分析](#dynamic-analysis)
  - [基础设施即代码分析](#infrastructure-as-code-analysis)
  - [故意脆弱的应用程序](#intentionally-vulnerable-applications)
  - [Monitoring](#monitoring)
  - [保密管理](#secrets-management)
  - [秘密扫描](#secrets-scanning)
  - [静态分析](#static-analysis)
  - [供应链安全](#supply-chain-security)
  - [威胁建模](#threat-modelling)
- [相关列表](#related-lists)

## 资源

### 文章

- [Our Approach to Employee Security Training](https://www.pagerduty.com/blog/security-training-at-pagerduty/) - _寻呼机职责_ - 在组织内进行安全培训的指南。
- [DevSecOps: Making Security Central To Your DevOps Pipeline](https://spacelift.io/blog/what-is-devsecops) - _Spacelift_ - 一篇文章解释了 DevSecOps 的目标、其优势以及 DevSecOps 生命周期的外观。

### 书籍

- [Alice and Bob Learn Application Security](https://www.wiley.com/en-gb/Alice+and+Bob+Learn+Application+Security-p-9781119687405) - _Tanya Janca_ - 对于任何寻求从系统开发生命周期开始就纳入软件开发最佳安全实践的人来说，这是一个易于访问且全面的资源。

### 社区

- [DevSecCon](https://www.devseccon.com/) - _Snyk_ - 一个专门针对 DevSecOps 举办会议、博客、播客和 Discord 的社区。
- [TAG Security](https://tag-security.cncf.io/) - _云原生计算基础_ - TAG Security 促进协作以发现和生成资源，从而为整个云原生生态系统中的操作员、管理员、开发人员和最终用户提供安全访问、策略控制和安全。

### 会议

- [AppSec Day](https://appsecday.io/) - _OWASP_ - 由 OWASP 举办的澳大利亚应用程序安全会议。
- [DevSecCon](https://www.devseccon.com/) - _Snyk_ - 由 Snyk 运营的 DevSecOps 会议网络。

### 时事通讯

- [Shift Security Left](https://shift-security-left.curated.co/) - _Cossack Labs_ - 为具有安全意识的开发人员提供的免费双周通讯，涵盖应用程序安全、安全架构、DevSecOps、密码学、事件等，对构建者和（在较小程度上）破坏者有用。

### 播客

- [Absolute AppSec](https://absoluteappsec.com/) - _Seth Law 和 Ken Johnson_ - 关于当前事件和与应用程序安全相关的特定主题的讨论。
- [Application Security Podcast](https://podcast.securityjourney.com/) - _安全之旅_ - 采访行业专家，了解特定的应用程序安全概念。
- [BeerSecOps](https://blog.aquasec.com/devsecops-podcasts) - _Aqua Security_ - 打破开发、安全和运营的孤岛，讨论跨越这些主题领域的主题。
- [DevSecOps Podcast Series](https://soundcloud.com/owasp-podcast) - _OWASP_ - 与思想领袖和实践者讨论将安全性集成到开发生命周期中。
- [The Secure Developer](https://www.mydevsecops.io/the-secure-developer-podcast) - _Snyk_ - 关于软件开发人员的安全工具和最佳实践的讨论。

### 安全开发指南

- [Application Security Verification Standard](https://owasp.org/www-project-application-security-verification-standard/) - _OWASP_ - 安全要求和控制框架，可帮助开发人员设计和开发安全的 Web 应用程序。
- [Coding Standards](https://wiki.sei.cmu.edu/confluence/display/seccode/SEI+CERT+Coding+Standards) - _CERT_ - C、C++、Java 和 Android 开发的安全开发标准集合。
- [Fundamental Practices for Secure Software Development](https://safecode.org/wp-content/uploads/2018/03/SAFECode_Fundamental_Practices_for_Secure_Software_Development_March_2018.pdf) - _SAFECode_ - 在整个 SDLC 中实施关键安全开发实践的指南。
- [Proactive Controls](https://owasp.org/www-project-proactive-controls/) - _OWASP_ - OWASP 列出了每个软件开发项目中应实施的十大控件。
- [Secure Coding Guidelines](https://wiki.mozilla.org/WebAppSec/Secure_Coding_Guidelines) - _Mozilla_ - 包含安全 Web 应用程序开发的特定安全开发标准的指南。
- [Secure Coding Practices Quick Reference Guide](https://owasp.org/www-pdf-archive/OWASP_SCP_Quick_Reference_Guide_v2.pdf) - _OWASP_ - 用于验证是否遵循安全开发标准的清单。

### 安全开发生命周期框架

- [Building Security In Maturity Model (BSIMM)](https://www.bsimm.com/framework.html) - _Synopsys_ - 通过观察和分析领先软件安全计划的数据而创建的软件安全框架。
- [Secure Development Lifecycle](https://www.microsoft.com/en-us/securityengineering/sdl/practices) - _Microsoft_ - 作为安全开发生命周期框架的工具和实践的集合。
- [Secure Software Development Framework](https://csrc.nist.gov/CSRC/media/Publications/white-paper/2019/06/07/mitigating-risk-of-software-vulnerabilities-with-ssdf/draft/documents/ssdf-for-mitigating-risk-of-software-vulns-draft.pdf) - _NIST_ - 一个由安全开发生命周期的实践、任务和实施示例组成的框架。
- [Software Assurance Maturity Model](https://github.com/OWASP/samm) - _OWASP_ - 衡量和提高安全开发生命周期成熟度的框架。

### 工具链

- [Cloud Security and DevSecOps Best Practices _and_ Securing Web Application Technologies (SWAT) Checklist](https://www.sans.org/posters/cloud-security-devsecops-best-practices/) - _SANS_ - 海报包含安全 Web 应用程序技术 (SWAT) 检查表、SANS 云安全课程、云安全前 10 名、前 12 名 Kubernetes 威胁和安全 DevOps 工具链。
- [Periodic Table of DevOps Tools](https://xebialabs.com/periodic-table-of-devops-tools/) - _XebiaLabs_ - 按工具功能分类的 DevSecOps 工具集合。

### 培训

- [Application Security Education](https://github.com/duo-labs/appsec-education) - _Duo Security_ - 由 Duo 应用程序安全团队创建的培训材料，包括介绍性和高级培训演示以及动手实验室。
- [Cybrary](https://www.cybrary.it/) - _Cybrary_ - 基于订阅的在线课程，具有网络安全和 DevSecOps 专用类别。
- [PentesterLab](https://pentesterlab.com/) - _PentesterLab_ - 通过实验室实践了解和利用简单和高级的 Web 漏洞。
- [Practical DevSecOps](https://www.practical-devsecops.com) - _实用 DevSecOps_ - 使用最先进的基于浏览器的实验室通过实用 DevSecOps 向行业专家学习 DevSecOps 概念、工具和技术。
- [SafeStack](https://academy.safestack.io/) - _SafeStack_ - 针对软件开发团队的安全培训，旨在供个人、小型团队以及大型组织访问。
- [Secure Code Warrior](https://www.securecodewarrior.com/) - _Secure Code Warrior_ - 游戏化和实践安全开发培训，支持课程、评估和锦标赛。
- [SecureFlag](https://www.secureflag.com/platform.html) - _OWASP_ - 为开发人员和构建/发布工程师提供实践安全编码培训。
- [Security Training for Engineers](https://sudo.pagerduty.com/for_engineers/) - _Pager Duty_ - 由 PagerDuty 创建并开源的演示文稿，旨在为软件工程师提供安全培训。
- [Security Training for Everyone](https://sudo.pagerduty.com/for_everyone/) - _Pager Duty_ - 由 PagerDuty 创建并开源的演示文稿，用于为员工提供安全培训。
- [Semgrep Academy](https://academy.semgrep.dev/) - _Semgrep_ - 免费的点播课程，涵盖 API 安全、安全编码和应用程​​序安全等主题。
- [Web Security Academy](https://portswigger.net/web-security) - _PortSwigger_ - 一组用于学习和利用常见网络漏洞的材料和实验室。
- [WeHackPuple](https://wehackpurple.com/) - _WeHackPurple_ - 教授应用程序安全理论和实践技术课程的在线课程。

### 维基百科

- [DevSecOps Hub](https://snyk.io/devsecops/) - _Snyk_ - 介绍关键 DevSecOps 概念、流程和技术。
- [SecureFlag Knowledge Base](https://knowledge-base.secureflag.com/) - _OWASP_ - 有关软件漏洞及其预防方法的信息存储库。

## 工具

### 依赖管理

开源软件包允许开发人员无需编写所有代码即可实现功能，从而加快开发过程。然而，随着开源代码的出现，开源漏洞也随之而来。依赖管理工具通过识别和更新具有已知漏洞的包来帮助管理开源包中的漏洞。

- [Deepfence ThreatMapper](https://github.com/deepfence/ThreatMapper) - Apache v2，适用于 kubernetes、虚拟机和无服务器的强大运行时漏洞扫描器。
- [Dependabot](https://dependabot.com/) - _GitHub_ - 自动扫描 GitHub 存储库中的漏洞并创建拉取请求以合并修补的依赖项。
- [Dependency-Check](https://owasp.org/www-project-dependency-check/) - _OWASP_ - 使用 CLI 或构建服务器插件扫描依赖项以查找公开披露的漏洞。
- [Dependency-Track](https://dependencytrack.org/) - _OWASP_ - 随着时间的推移监控多个项目中易受攻击的依赖项的数量和严重性。
- [JFrog XRay](https://jfrog.com/xray/) - _JFrog_ - 对 JFrog Artifactory 中存储的工件进行安全性和合规性分析。
- [NPM Audit](https://docs.npmjs.com/cli/audit) - _NPM_ - npm CLI 中内置的节点包的漏洞包审核。
- [Renovate](https://renovate.whitesourcesoftware.com/) - _WhiteSource_ - 使用 CLI 或 git 存储库应用程序自动监控和更新多个框架和语言的软件依赖项。
- [Requires.io](https://requires.io/) - _Olivier Mansion 和 Alexis Tabary_ - Python 项目的自动化易受攻击依赖项监控和升级。
- [Snyk Open Source](https://snyk.io/product/open-source-security-management/) - _Snyk_ - 使用 Snyk 的专用漏洞数据库自动进行易受攻击的依赖项监控和升级。

### 动态分析

动态分析安全测试 (DAST) 是黑盒安全测试的一种形式，其中安全扫描器与正在运行的应用程序实例进行交互，模拟恶意活动以查找常见漏洞。 DAST工具通常用于渗透测试的初始阶段，可以发现跨站脚本、SQL注入、跨站请求伪造和信息泄露等漏洞。

- [Automatic API Attack Tool](https://github.com/imperva/automatic-api-attack-tool) - _Imperva_ - 根据 API 规范对 API 执行自动安全扫描。
- [BurpSuite Enterprise Edition](https://portswigger.net/burp/enterprise) - _PortSwigger_ - BurpSuite 的 Web 应用程序漏洞扫描器被渗透测试人员广泛使用，并通过 CI/CD 集成和对多个 Web 应用程序的持续监控进行了修改。
- [Gauntlt](https://github.com/gauntlt/gauntlt) - _Gauntlt_ - 行为驱动开发框架，使用通用安全工具和测试输出运行安全扫描，使用 Gherkin 语法定义。
- [Netz](https://github.com/spectralops/netz) - _Spectral_ - 使用 zgrab2 等发现互联网范围内的错误配置。
- [RESTler](https://github.com/microsoft/restler-fuzzer) - _Microsoft_ - 基于同行评审研究论文的有状态 RESTful API 扫描器。
- [SSL Labs Scan](https://github.com/ssllabs/ssllabs-scan) - _SSL Labs_ - 自动扫描 SSL / TLS 配置问题。
- [Zed Attack Proxy (ZAP)](https://github.com/zaproxy/zaproxy) - _OWASP_ - 开源 Web 应用程序漏洞扫描器，包括用于 CI/CD 集成的 API。

### 基础设施即代码分析

基础设施即代码允许将应用程序可靠地部署到一致的环境中。这不仅确保基础设施得到一致强化，而且还提供了静态和动态分析基础设施定义的机会，以发现易受攻击的依赖项、硬编码秘密、不安全的配置和安全配置中的意外更改。以下工具有助于此分析。

#### 多平台

- [Checkov](https://github.com/bridgecrewio/checkov) - _Bridgecrew_ - 扫描 Terraform、AWS CloudFormation 和 Kubernetes 模板是否存在不安全配置。
- [KICS](https://github.com/Checkmarx/kics) - _Checkmarx_ - 在开发周期的早期发现安全漏洞、合规性问题和基础设施配置错误。
- [Spectral DeepConfig](https://spectralops.io/blog/spectral-launches-deepconfig-to-ensure-no-misconfiguration-at-all-layers-of-software/) - _Spectral_ - 尽早在提交时发现基础设施和应用程序中的错误配置。
- [Terrascan](https://github.com/accurics/terrascan) - _Accurics_ - 检测整个基础设施即代码的合规性和安全违规行为，以在配置云原生基础设施之前降低风险。

<!-- omit in toc -->
#### 云的形成
- [Cfn Nag](https://github.com/stelligent/cfn_nag) - _Stelligent_ - 扫描 AWS CloudFormation 模板是否存在不安全的配置。

<!-- omit in toc -->
#### 集装箱
- [Clair](https://github.com/quay/clair) - _Red Hat_ - 扫描应用程序容器和 Docker 容器以查找公开披露的漏洞。
- [Dagda](https://github.com/eliasgranderubio/dagda/) - _Elías Grande_ - 将 Docker 容器中安装的操作系统和软件依赖版本与公共漏洞数据库进行比较，并执行病毒扫描。
- [Docker-Bench-Security](https://github.com/docker/docker-bench-security) - _Docker_ - Docker Bench for Security 是一个脚本，用于检查在生产中部署 Docker 容器的数十种常见最佳实践。
- [Grype](https://github.com/anchore/grype/) - _Anchore_ - 一个易于集成的开源漏洞扫描工具，用于容器镜像和文件系统。
- [Hadolint](https://github.com/hadolint/hadolint) - _Hadolint_ - 根据已知规则检查 Dockerfile 并验证 RUN 语句中的内联 bash 代码。
- [Snyk Container](https://snyk.io/product/container-vulnerability-management/) - _Snyk_ - 在 CI/CD 期间或通过持续监控扫描 Docker 和 Kubernetes 应用程序是否存在安全漏洞。
- [Trivy](https://github.com/aquasecurity/trivy) - _Aqua Security_ - 简单而全面的容器漏洞扫描器。

<!-- omit in toc -->
#### 地形
- [Regula](https://github.com/fugue/regula) - _Fugue_ - 在部署之前评估 Terraform 基础设施即代码是否存在潜在的安全错误配置和合规性违规。
- [Terraform Compliance](https://terraform-compliance.com/) - _terraform-compliance_ - 针对 terraform 的轻量级、安全性和合规性重点测试框架，可为您的基础设施即代码启用负面测试功能。
- [Tfsec](https://github.com/liamg/tfsec) - _Liam Galvin_ - 扫描 Terraform 模板是否存在安全配置错误以及不符合 AWS、Azure 和 GCP 安全最佳实践的情况。

<!-- omit in toc -->
#### 库伯内斯
- [Kubescape](https://kubescape.io/) - _云原生计算基础_ - 适用于 IDE、CI/CD 管道和集群的开源 Kubernetes 安全平台。
- [Kube-Score](https://github.com/zegl/kube-score) - _Gustav Westling_ - 扫描 Kubernetes 对象定义是否存在安全和性能配置错误。
- [Kubectrl Kubesec](https://github.com/controlplaneio/kubectl-kubesec) - _ControlPlane_ - kubesec.io 的插件，用于对 Kubernetes 资源执行安全风险分析。

#### 安西布尔
- [Ansible-Lint](https://github.com/ansible-community/ansible-lint) - _Ansible 社区_ - 检查手册中是否有可能需要改进的实践和行为。作为社区支持的项目，ansible-lint 仅支持 Ansible 的最后两个主要版本。

### 故意脆弱的应用程序

在开发安全测试和工具时，故意存在漏洞的应用程序通常很有用，可以为您提供运行测试并确保测试正确失败的地方。这些应用程序还有助于了解常见漏洞如何引入应用程序，并让您练习利用它们的技能。

- [Bad SSL](https://github.com/chromium/badssl.com) - _Chromium 项目_ - 运行多个 SSL / TLS 配置较差的 Web 服务器的容器。对于测试工具很有用。
- [Cfngoat](https://github.com/bridgecrewio/cfngoat) - _Bridgecrew_ - 用于在 AWS 中创建故意不安全的服务堆栈的 Cloud Formation 模板。非常适合测试 Cloud Formation 基础设施作为上述代码分析工具。
- [CI/CD Goat](https://github.com/cider-security-research/cicd-goat) - _Cider Security_ - 故意存在漏洞的 CI/CD 环境。通过多重挑战学习 CI/CD 安全性。
- [Damn Vulnerable Web App](http://www.dvwa.co.uk/) - _Ryan Dewhurst_ - 一个 Web 应用程序，提供一个安全的环境来理解和利用常见的 Web 漏洞。
- [Juice Shop](https://github.com/bkimminich/juice-shop) - _OWASP_ - 包含 OWASP 十大安全漏洞等的 Web 应用程序。
- [Kubernetes Goat](https://github.com/madhuakula/kubernetes-goat) - _Madhu Akula_ - 故意设置易受攻击的集群环境来学习和练习 Kubernetes 安全性。
- [NodeGoat](https://github.com/OWASP/NodeGoat) - _OWASP_ - 一个 Node.js Web 应用程序，演示并提供了解决常见安全漏洞的方法。
- [Pentest-Ground](https://pentest-ground.com/) - _Pentest-Tools.com_ - Pentest-Ground 是一个免费游乐场，其中故意存在易受攻击的 Web 应用程序和网络服务。
- [Terragoat](https://github.com/bridgecrewio/terragoat) - _Bridgecrew_ - Terraform 模板，用于在 AWS、Azure 和 GCP 中创建故意不安全的服务堆栈。非常适合测试 Terraform 基础设施作为上述代码分析工具。
- [Vulnerable Web Apps Directory](https://owasp.org/www-project-vulnerable-web-applications-directory) - _OWASP_ - 用于学习目的的易受攻击的 Web 应用程序的集合。
- [WrongSecrets](https://github.com/OWASP/wrongsecrets) - _OWASP_ - 易受攻击的应用程序，其中包含展示如何不使用机密的示例


### 监控
在发布之前测试和强化我们的软件是不够的。我们还必须监控生产软件的使用情况、性能和错误，以捕获我们可能需要响应或解决的恶意行为和潜在安全缺陷。有多种工具可用于监控生产软件和基础设施的不同方面。

- [Csper](https://csper.io/report-uri) - _Csper_ - 一组内容安全策略工具，可以测试策略、监控 CSP 报告并提供指标和警报。
- [Streamdal](https://streamdal.com) - _Streamdal_ - 在应用程序代码中嵌入隐私控制，以在 PII 进入和离开系统时检测和监控 PII，防止其到达意外的数据库、数据流或管道。

### 保密管理

我们编写的软件需要使用机密（密码、API 密钥、证书、数据库连接字符串）来访问资源，但我们无法将机密存储在代码库中，因为这会使它们容易受到损害。秘密管理工具提供了一种安全存储、访问和管理秘密的方法。

- [Ansible Vault](https://docs.ansible.com/ansible/latest/user_guide/vault.html) - _Ansible_ - 在 Ansible 管道中安全地存储机密。
- [AWS Key Management Service (KMS)](https://aws.amazon.com/kms/) - _Amazon AWS_ - 在 AWS 中创建和管理加密密钥。
- [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/) - _Amazon AWS_ - 在 AWS 中安全存储可检索的应用程序机密。
- [Azure Key Vault](https://azure.microsoft.com/en-au/services/key-vault/) - _Microsoft Azure_ - 在 Azure 中安全地存储机密。
- [BlackBox](https://github.com/StackExchange/blackbox) - _StackExchange_ - 加密代码存储库中的凭据。
- [Chef Vault](https://github.com/chef/chef-vault) - _Chef_ - 在 Chef 中安全地存储秘密。
- [CredStash](https://github.com/fugue/credstash) - _Fugue_ - 使用 KMS 和 DynamoDB 在 AWS 中安全地存储机密。
- [CyberArk Application Access Manager](https://www.cyberark.com/products/privileged-account-security-solution/application-access-manager/) - _Cyber​​Ark_ - 应用程序的秘密管理，包括秘密轮换和审计。
- [Docker Secrets](https://docs.docker.com/engine/swarm/secrets/) - _Docker_ - 存储和管理对 Docker 群中机密的访问。
- [Git Secrets](https://github.com/awslabs/git-secrets) - _Amazon AWS_ - 扫描 git 存储库以查找代码或提交消息中提交的秘密。
- [Gopass](https://github.com/gopasspw/gopass) - _Gopass_ - 依赖 Git 和 gpg 的团队的密码管理器。管理加密文件和存储库中的机密。
- [Google Cloud Key Management Service (KMS)](https://cloud.google.com/kms) - _Google Cloud Platform_ - 在 GCP 内安全存储机密。
- [HashiCorp Vault](https://www.vaultproject.io/) - _HashiCorp_ - 通过 UI、CLI 或 HTTP API 安全存储机密。
- [Keyscope](https://github.com/SpectralOps/keyscope) - _Spectral_ - Keyscope 是一个用 Rust 构建的开源密钥和秘密工作流程工具（验证、失效等）。
- [Pinterest Knox](https://github.com/pinterest/knox) - _Pinterest_ - 安全地存储、轮换和审核机密。
- [Secrets Operations (SOPS)](https://github.com/mozilla/sops) - _Mozilla_ - 加密存储在 YAML、JSON、ENV、INI 和 BINARY 文件中的密钥。
- [Teller](https://github.com/spectralops/teller) - _Spectral_ - 为开发人员提供的秘密管理工具 - 永远不要让命令行留下秘密。


### 秘密扫描

即使存储库是私有的，源代码控制也不是存储凭据、API 密钥或令牌等机密的安全位置。秘密扫描工具可以扫描和监视 git 存储库和拉取请求的秘密，并可用于防止秘密被提交，或查找和删除已提交到源代码管理的秘密。

- [CredScan](https://secdevtools.azurewebsites.net/helpcredscan.html) - _Microsoft_ - 一种凭据扫描工具，可以作为 Azure DevOps 管道中的任务运行。
- [Detect Secrets](https://github.com/Yelp/detect-secrets) - _Yelp_ - 一个恰当命名的模块，用于（惊喜，惊喜）检测代码库中的秘密。
- [GitGuardian](https://www.gitguardian.com/) - _GitGuardian_ - 一个基于 Web 的解决方案，可扫描和监控公共和私人 git 存储库中的秘密。
- [Gitleaks](https://github.com/zricethezav/gitleaks) - _Zachary Rice_ - Gitleaks 是一个 SAST 工具，用于检测 git 存储库中的硬编码秘密，例如密码、API 密钥和令牌。
- [git-secrets](https://github.com/awslabs/git-secrets) - _AWS 实验室_ - 扫描提交、提交消息并合并秘密。对 AWS 秘密模式的本机支持，但可以配置为支持其他模式。
- [Nightfall](https://nightfall.ai/solutions/product/github) - _Nightfall_ - 一个基于 Web 的平台，用于监控多个 SDLC 工具（包括 GitHub 存储库）中的敏感数据泄露。
- [Repo-supervisor](https://github.com/auth0/repo-supervisor) - _Auth0_ - 秘密扫描工具，可以作为 CLI、Docker 容器或在 AWS Lambda 中运行。
- [SpectralOps](https://spectralops.io) - _Spectral_ - 自动代码安全、秘密、令牌和敏感数据扫描。
- [truffleHog](https://github.com/trufflesecurity/truffleHog) - _Truffle Security_ - 在 git 存储库中搜索秘密，深入挖掘提交历史记录和分支。

### 静态分析

静态分析安全测试 (SAST) 工具可扫描软件中的漏洞，而无需执行目标软件。通常，静态分析会扫描源代码是否存在安全缺陷，例如使用不安全函数、硬编码机密和配置问题。 SAST 工具通常以 IDE 插件和 CLI 的形式出现，可以集成到 CI/CD 管道中。

<!-- omit in toc -->
#### 多语言支持

- [DevSkim](https://github.com/microsoft/DevSkim) - _Microsoft_ - 一组 IDE 插件、CLI 和其他工具，为多种编程语言提供安全分析。
- [Graudit](https://github.com/wireghoul/graudit/) - _Eldar Marcussen_ - 使用自定义或预配置的正则表达式签名查找潜在安全缺陷的 Grep 源代码。
- [Hawkeye](https://github.com/hawkeyesec/scanner-cli) - _Hawkeyesec_ - 用于项目安全、漏洞和一般风险突出显示的模块化 CLI 工具。
- [LGTM](https://lgtm.com/) - _Semmle_ - 使用自定义或内置 CodeQL 查询扫描和监控代码是否存在安全漏洞。
- [RIPS](https://www.ripstech.com/) - _RIPS Technologies_ - PHP、Java 和 Node.js 项目的自动静态分析。
- [SemGrep](https://semgrep.dev/) - _r2c_ - Semgrep 是一种快速、开源、静态分析工具，可以在编辑器、提交和 CI 时间查找错误并强制执行代码标准。
- [SonarLint](https://www.sonarlint.org/) - _SonarSource_ - 一个 IDE 插件，突出显示潜在的安全问题、代码质量问题和错误。
- [SonarQube](https://www.sonarqube.org/) - _SonarSource_ - 扫描代码以查找安全和质量问题，支持多种语言。

<!-- omit in toc -->
#### C/C++

- [FlawFinder](https://github.com/david-a-wheeler/flawfinder) - _David Wheeler_ - 扫描 C / C++ 代码以查找潜在的安全漏洞。

<!-- omit in toc -->
#### C#

- [Puma Scan](https://github.com/pumasecurity/puma-scan) - _Puma Security_ - 一个 Visual Studio 插件，用于扫描 .NET 项目是否存在潜在的安全缺陷。

<!-- omit in toc -->
#### 配置文件
- [Conftest](https://github.com/instrumenta/conftest) - _Instrumenta_ - 创建自定义测试来扫描任何配置文件是否存在安全缺陷。
- [Selefra](https://github.com/selefra/selefra) - _Selefra_ - 一款开源策略即代码软件，可为多云和 SaaS 提供分析。

<!-- omit in toc -->
#### 爪哇

- [Deep Dive](https://discotek.ca/deepdive.xhtml) - _Discotek.ca_ - JVM 部署单元的静态分析，包括 Ear、War、Jar 和 APK。
- [Find Security Bugs](https://github.com/find-sec-bugs/find-sec-bugs/) - _OWASP_ - 用于 Java Web 应用程序安全审核的 SpotBugs 插件。支持 Eclipse、IntelliJ、Android Studio 和 SonarQube。
- [SpotBugs](https://github.com/spotbugs/spotbugs) - _SpotBugs_ - Java 应用程序的静态代码分析。

<!-- omit in toc -->
#### JavaScript

- [ESLint](https://eslint.org/) - _JS Foundation_ - JavaScript 的 Linting 工具，具有多个可用的安全 linting 规则。

<!-- omit in toc -->
#### 去

- [Golang Security Checker](https://github.com/securego/gosec) - _securego_ - 用于扫描 Go 代码是否存在潜在安全缺陷的 CLI 工具。

<!-- omit in toc -->
#### .NET

- [Security Code Scan](https://github.com/security-code-scan/security-code-scan) - _安全代码扫描_ - C# 和 VB.NET 应用程序的静态代码分析。

<!-- omit in toc -->
#### PHP

- [Phan](https://github.com/phan/phan) - _Phan_ - 对 PHP 应用程序进行广泛的静态分析，并提供对安全扫描功能的一些支持。
- [PHPCS Security Audit](https://github.com/FloeDesignTechnologies/phpcs-security-audit) - _Floe_ - PHP 静态分析，包含 PHP、Drupal 7 和 PHP 相关 CVE 的规则。
- [Progpilot](https://github.com/designsecurity/progpilot) - _Design Security_ - PHP 源代码的静态分析。

<!-- omit in toc -->
#### 蟒蛇

- [Bandit](https://github.com/PyCQA/bandit) - _Python 代码质量权威_ - 查找 Python 代码中的常见安全漏洞。

<!-- omit in toc -->
#### 红宝石

- [Brakeman](https://github.com/presidentbeef/brakeman) - _Justin Collins_ - 静态分析工具，用于检查 Ruby on Rails 应用程序是否存在安全漏洞。
- [DawnScanner](https://github.com/thesp0nge/dawnscanner) - _Paolo Perego_ - 对 Ruby 脚本和 Web 应用程序进行安全扫描。支持 Ruby on Rails、Sinatra 和 Padrino 框架。


### 供应链安全

供应链攻击有不同的形式，针对 SDLC 中本质上是第三方的部分：CI 中的工具、已执行的外部代码等等。供应链安全工具可以防御此类攻击。

- [Harden Runner GitHub Action](https://github.com/step-security/harden-runner) - _StepSecurity_ - 在 GitHub 托管的运行器 (Ubuntu VM) 上安装安全代理，以防止凭据泄露、检测受损的依赖项和构建工具，以及检测构建期间源代码的篡改。
- [Overlay](https://github.com/os-scar/overlay) - _SCAR_ - 一个浏览器扩展，可帮助开发人员在选择开源包之前对其进行评估。
- [Preflight](https://github.com/spectralops/preflight) - _Spectral_ - 帮助您验证脚本和可执行文件，以减轻 CI 和其他系统中的供应链攻击，例如最近的 [Codecov 黑客攻击](https://spectralops.io/blog/credentials-risk-supply-chain-lessons-from-the-codecov-breach/)。
- [Sigstore](https://www.sigstore.dev/) - sigstore 是一组免费使用的开源工具，包括 [fulcio](https://github.com/sigstore/fulcio)、[cosign](https://github.com/sigstore/cosign) 和 [rekor](https://github.com/sigstore/rekor)，处理所需的数字签名、验证和来源检查，使开源软件的分发和使用更加安全。
- [Syft](https://github.com/anchore/syft/) - _Anchore_ - 用于从容器映像和文件系统生成软件物料清单 (SBOM) 的 CLI 工具。

### 威胁建模

威胁建模是一项工程实践，旨在识别代表有价值事物风险的威胁、漏洞和攻击向量。  基于对威胁的了解，我们可以设计、实施和验证安全控制措施以减轻威胁。以下工具列表有助于威胁建模过程。

- [Awesome Threat Modelling](https://github.com/hysnsec/awesome-threat-modelling) - _实用 DevSecOps_ - 威胁建模资源的精选列表。
- [SecuriCAD](https://www.foreseeti.com/) - _Forseeti_ - 处理 IT 基础设施的建模和攻击模拟。
- [IriusRisk](https://iriusrisk.com/) - _IriusRisk_ - 绘制威胁模型并捕获威胁和对策并管理风险。
- [Raindance Project](https://github.com/devsecops/raindance) - _DevSecOps_ - 使用攻击图来识别可能导致妥协的攻击面和对手策略。
- [SD Elements](https://www.securitycompass.com/sdelements/threat-modeling/) - _安全指南针_ - 识别威胁并对其进行排名，生成可操作的任务并跟踪相关票证。
- [Threat Dragon](https://owasp.org/www-project-threat-dragon/) - _OWASP_ - 威胁模型图表工具。
- [Threat Modelling Tool](https://www.microsoft.com/en-us/securityengineering/sdl/threatmodeling) - _Microsoft_ - 威胁模型绘图工具。
- [Threatspec](https://threatspec.org/) - _Threatspec_ - 将威胁建模定义为代码。

## 相关列表

- [Awesome Dynamic Analysis](https://github.com/analysis-tools-dev/dynamic-analysis/) - _Matthias Endler_ - 动态分析工具和代码质量检查器的集合。
- [Awesome Platform Engineering](https://github.com/shospodarets/awesome-platform-engineering/) - _平台工程_解决方案、工具和资源的精选列表
- [Awesome Static Analysis](https://github.com/analysis-tools-dev/static-analysis/) - _Matthias Endler_ - 静态分析工具和代码质量检查器的集合。
- [Awesome Threat Modelling](https://github.com/hysnsec/awesome-threat-modelling) - _实用 DevSecOps_ - 威胁建模资源的精选列表。
- [Vulnerable Web Apps Directory](https://owasp.org/www-project-vulnerable-web-applications-directory) - _OWASP_ - 用于学习目的的易受攻击的 Web 应用程序的集合。
