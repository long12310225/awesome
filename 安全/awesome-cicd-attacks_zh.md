# 令人敬畏的 CI/CD 攻击 [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
对与开发和部署代码相关的系统和流程进行进攻性研究。

## 内容

- [Techniques](#techniques)
  - [公开暴露的敏感数据](#publicly-exposed-sensitive-data)
  - [初始代码执行](#initial-code-execution)
  - [后利用](#post-exploitation)
  - [防御规避](#defense-evasion)
- [Tools](#tools)
- [案例研究](#case-studies)
- [类似项目](#similar-projects)

## 技巧
独特且有用的 CI/CD 攻击技术的精选列表。

### 公开暴露的敏感数据
- [(The) Postman Carries Lots of Secrets](https://trufflesecurity.com/blog/postman-carries-lots-of-secrets) - 由于混乱的 UI、分叉和秘密扫描不足，Postman 的公共 API 网络泄露了数千个秘密。
- [All the Small Things: Azure CLI Leakage and Problematic Usage Patterns](https://www.paloaltonetworks.com/blog/prisma-cloud/secrets-leakage-user-error-azure-cli/) - 由于使用模式，Azure CLI 会将机密泄露到 CI/CD 日志中。
- [Anyone can Access Deleted and Private Repository Data on GitHub](https://trufflesecurity.com/blog/anyone-can-access-deleted-and-private-repo-data-github) - 只要它是分叉网络的一部分。
- [Beyond S3: Exposed Resources on AWS](https://duo.com/blog/beyond-s3-exposed-resources-on-aws) - 暴露于互联网的公共 EBS、RDS、AMI 和 Elasticsearch 集群。
- [CloudQuarry: Digging for secrets in public AMIs](https://securitycafe.ro/2024/05/08/aws-cloudquarry-digging-for-secrets-in-public-amis/) - 研究人员在公共 AWS AMI 中发现了 500GB 的凭证、私有存储库和密钥，影响了各个行业。
- [Employee Personal GitHub Repos Expose Internal Azure and Red Hat Secrets](https://www.aquasec.com/blog/github-repos-expose-azure-and-red-hat-secrets/) - 员工的个人 GitHub 存储库暴露了内部 Azure 和 Red Hat 机密。
- [Fortune 500 at Risk: 250M Artifacts Exposed via Misconfigured Registries](https://www.aquasec.com/blog/250m-artifacts-exposed-via-misconfigured-registries/) - 公共注册表配置错误，软件工件包含敏感的专有代码和机密。
- [GitLab Secrets](https://github.com/RichardoC/gitlab-secrets) - 该工具可以显示已删除的 GitLab 提交，这些提交可能包含敏感信息并且无法通过公共 Git 历史记录访​​问。
- [Hidden GitHub Commits and How to Reveal Them](https://neodyme.io/en/blog/github_secrets/) - 该工具可以显示已删除的 GitHub 提交，这些提交可能包含敏感信息并且无法通过公共 Git 历史记录访​​问。
- [Holes in Your Bitbucket: Why Your CI/CD Pipeline Is Leaking Secrets](https://cloud.google.com/blog/topics/threat-intelligence/bitbucket-pipeline-leaking-secrets) - Bitbucket 安全变量通过工件对象泄露秘密；建议包括使用专用的秘密管理器和代码扫描。
- [Millions of Secrets Exposed via Web Application Frontends](https://web.archive.org/web/20230531032433/https://redhuntlabs.com/blog/millions-of-secrets-exposed-via-web-application-frontend/) - 通过 JavaScript 和调试页面在 Web 应用程序前端中暴露了数百万个秘密。
- [Publicly Exposed AWS Document DB Snapshots](https://ramimac.me/exposed-docdb) - 公开曝光的巴西 Cinemark AWS DocumentDB 快照揭示了数百万条客户记录。
- [Thousands of images on Docker Hub leak auth secrets, private keys](https://www.bleepingcomputer.com/news/security/thousands-of-images-on-docker-hub-leak-auth-secrets-private-keys/) - 研究人员发现数千个 Docker Hub 镜像泄露了私钥和 API 秘密。

### 初始代码执行
- [ActionsTOCTOU (Time Of Check to Time Of Use)](https://github.com/AdnaneKhan/ActionsTOCTOU/) - 一种工具，用于监视批准事件，然后使用指定为参数的本地文件快速替换 PR 头中的文件。
- [AWS Targeted by a Package Backfill Attack](https://www.mend.io/blog/aws-targeted-by-a-package-backfill-attack/) - 扫描内部包的提交历史记录以执行依赖混淆。
- [Can you trust ChatGPT's package recommendations?](https://vulcan.io/blog/ai-hallucinations-package-risk) - 利用生成式人工智能平台生成不存在的编码库的倾向来执行依赖混乱。
- [Can You Trust Your VSCode Extensions?](https://www.aquasec.com/blog/can-you-trust-your-vscode-extensions/) - 冒充流行的 VSCode 扩展并诱骗不知情的开发人员下载它们。
- [Deep dive into Visual Studio Code extension security vulnerabilities](https://snyk.io/blog/visual-studio-code-extension-security-vulnerabilities-deep-dive/) - VS Code 扩展存在漏洞（命令注入、路径遍历、zip slip），可能会危及开发人员的计算机。
- [Dependency Confusion: How I Hacked Into Apple, Microsoft and Dozens of Other Companies](https://medium.com/@alex.birsan/dependency-confusion-4a5d60fec610) - 研究人员上传了带有内部公司名称的恶意包，由于依赖关系混乱而获得了苹果、微软等公司的访问权限。
- [Dependency Confusions in Docker and remote pwning of your infra](https://www.errno.fr/DockerDependencyConfusion.html) - 当配置错误的 Docker 镜像拉取恶意公共镜像而不是私有镜像时，就会发生 Docker 依赖关系混乱。
- [Erosion of Trust: Unmasking Supply Chain Vulnerabilities in the Terraform Registry](https://boostsecurity.io/blog/erosion-of-trust-unmasking-supply-chain-vulnerabilities-in-the-terraform-registry) - Terraform 模块不受依赖关系锁定文件的保护，因此，看似无害的模块可能会引入恶意代码。
- [Fixing typos and breaching microsoft's perimeter](https://johnstawinski.com/2024/04/15/fixing-typos-and-breaching-microsofts-perimeter/) - 成为贡献者，绕过 GitHub 工作流审批要求。
- [GitHub Dataset Research Reveals Millions Potentially Vulnerable to RepoJacking](https://www.aquasec.com/blog/github-dataset-research-reveals-millions-potentially-vulnerable-to-repojacking/) - 由于组织重命名，数以百万计的 GitHub 存储库很容易受到 RepoJacking 的攻击，从而导致潜在的代码执行。
- [Gitloker attacks abuse GitHub notifications to push malicious OAuth apps](https://www.bleepingcomputer.com/news/security/gitloker-attacks-abuse-github-notifications-to-push-malicious-oauth-apps/) - 攻击者使用虚假 GitHub 通知来诱骗用户授权窃取存储库访问权限的恶意 OAuth 应用程序。
- [Hacking GitHub AWS integrations again](https://dagrz.com/writing/aws-security/hacking-github-aws-oidc/) - 攻击使用 OIDC 的错误配置管道。
- [How I hacked into Google's internal corporate assets](https://observationsinsecurity.com/2024/04/25/how-i-hacked-into-googles-internal-corporate-assets/) - 在代码中查找依赖关系以解决依赖混淆的更多方法。
- [How to completely own an airline in 3 easy steps](https://maia.crimew.gay/posts/how-to-hack-an-airline/) - 可通过互联网访问的配置错误的 CI 系统。
- [How We Hacked a Software Supply Chain for $50K](https://www.landh.tech/blog/20250211-hack-supply-chain-for-50k/) - 抓取目标的 JavaScript 前端文件，并使用 AST 来识别 import/require 语句，从而发现具有 NPM 凭据的公共容器。
- [Introducing MavenGate: a supply chain attack method for Java and Android applications](https://blog.oversecured.com/Introducing-MavenGate-a-supply-chain-attack-method-for-Java-and-Android-applications/) - 许多早已废弃的公共和流行图书馆仍在大型项目中使用。通过购买域名可以劫持项目的访问权限。
- [Keeping your GitHub Actions and workflows secure Part 1: Preventing pwn requests](https://securitylab.github.com/research/github-actions-preventing-pwn-requests/) - 将 pull_request_target 工作流触发器与不受信任 PR 的显式签出相结合可能会导致存储库受损。
- [Keeping your GitHub Actions and workflows secure Part 2: Untrusted input](https://securitylab.github.com/research/github-actions-untrusted-input/) - GitHub Actions 命令注入。
- [Malicious code analysis: Abusing SAST (mis)configurations to hack CI systems](https://medium.com/cider-sec/malicious-code-analysis-abusing-sast-mis-configurations-to-hack-ci-systems-13d5c1b37ffe) - 配置错误的 SAST 工具可被利用在 CI 系统上执行恶意代码，从而允许攻击者窃取凭据或部署恶意工件。
- [PPE — Poisoned Pipeline Execution](https://medium.com/cider-sec/ppe-poisoned-pipeline-execution-34f4e8d0d4e9) - 中毒管道执行 (PPE) 使攻击者无需直接访问即可在 CI/CD 系统中运行恶意代码。
- [Security alert: social engineering campaign targets technology industry employees](https://github.blog/2023-07-18-security-alert-social-engineering-campaign-targets-technology-industry-employees/) - 网络钓鱼 GitHub 用户下载并执行存储库。
- [The (In)security Landscape of AI-Powered GitHub Actions (Part 2/2)](https://www.wiz.io/blog/github-actions-security-ai-powered-actions-vulnerabilities) - AI 驱动的 GitHub Actions 中的漏洞。语法权限检查允许攻击者冒充受信任的应用程序和 Dependabot 代理混淆注入。
- [The Monsters in Your Build Cache – GitHub Actions Cache Poisoning](https://adnanthekhan.com/2024/05/06/the-monsters-in-your-build-cache-github-actions-cache-poisoning/) - 允许攻击者通过利用漏洞或依赖缺陷来破坏工作流，即使权限有限，攻击者窃取缓存令牌，填充缓存以强制驱逐，并用恶意代码替换合法条目。
- [Thousands of npm accounts use email addresses with expired domains](https://therecord.media/thousands-of-npm-accounts-use-email-addresses-with-expired-domains) - 维护者电子邮件劫持。
- [Understanding typosquatting methods - for a secure supply chain](https://bytesafe.dev/posts/understanding-typosquatting-methods/) - 域名仿冒涉及发布名称与合法软件包相似的恶意软件包，利用拼写错误注入恶意代码。
- [Vulnerable GitHub Actions Workflows Part 1: Privilege Escalation Inside Your CI/CD Pipeline](https://www.legitsecurity.com/blog/github-privilege-escalation-vulnerability) - GitHub 操作工作流程_运行 PE。
- [What the fork? Imposter commits in GitHub Actions and CI/CD](https://www.chainguard.dev/unchained/what-the-fork-imposter-commits-in-github-actions-and-ci-cd) - GitHub Actions 漏洞允许分叉提交绕过工作流程安全设置。
- [whoAMI: A cloud image name confusion attack](https://securitylabs.datadoghq.com/articles/whoami-a-cloud-image-name-confusion-attack/) - 使用 AWS AMI 的依赖关系混乱。
- [WordPress Plugin Confusion: How an update can get you pwned](https://vavkamil.cz/2021/11/25/wordpress-plugin-confusion-update-can-get-you-pwned/) - 无人认领的 WordPress 插件很容易通过插件目录被接管。

### 后利用
- [From Self-Hosted GitHub Runner to Self-Hosted Backdoor](https://www.praetorian.com/blog/self-hosted-github-runners-are-backdoors/) - 攻击者利用错误配置的运行程序和薄弱的 PAT 安全性来获得持久性、升级权限和横向移动。
- [Hacking Terraform State for Privilege Escalation](https://blog.plerion.com/hacking-terraform-state-privilege-escalation/) - 修改 Terraform 状态文件允许攻击者删除基础设施或通过自定义提供程序执行代码。
- [Hijacking GitHub runners to compromise the organization](https://www.synacktiv.com/publications/hijacking-github-runners-to-compromise-the-organization) - 使用 ubuntu-latest 标签注册 GitHub 运行程序将授予对最初为 GitHub 配置的运行程序指定的作业的访问权限。
- [How We Discovered Vulnerabilities in CI/CD Pipelines of Popular Open-Source Projects](https://cycode.com/blog/github-actions-vulnerabilities) - 提取 GitHub Actions 中的所有存储库和组织机密。
- [Invisible Ghost: Alarming Vulnerability in GitHub Copilot](https://www.apexhq.ai/blog/blog/invisible-ghost-alarming-vulnerability-in-github-copilot/) - 使用隐藏的 Unicode 字符来操纵 GitHub Copilot 的建议。
- [Leaking Secrets From GitHub Actions: Reading Files And Environment Variables, Intercepting Network/Process Communication, Dumping Memory](https://karimrahal.com/2023/01/05/github-actions-leaking-secrets/) - 可以通过多种方法从易受攻击的 GitHub Actions 工作流程中泄露机密：读取文件/环境变量、拦截通信和转储运行程序内存。
- [Living off the pipeline](https://github.com/boostsecurityio/lotp) - 盘点开发工具（通常是 CLI）如何具有鲜为人知的 RCE-By-Design 功能。
<!--lint ignore awesome-list-item-->
- [Registering self-hosted CircleCI runner](broken_links.md/#httpstwittercomalxk7istatus1524353383976558593t5esgwtom2218sgygy5vdoas19) - 可用于窃取恶意运行程序上执行的作业的秘密。
- [The GitHub Actions Worm: Compromising GitHub Repositories Through the Actions Dependency Tree](https://www.paloaltonetworks.com/blog/prisma-cloud/github-actions-worm-dependencies/) - 一种新颖的 GitHub Actions 蠕虫利用了动作依赖树。攻击者破坏某个操作，然后通过分支推送或标签覆盖来感染相关操作，从而递归地传播恶意软件。



### 防御规避
- [#redteam tip: want to discretely extract credentials from a CI/CD pipeline?](https://twitter.com/_alxk/status/1442519103885959172?s=21) - 草稿拉取请求不会提醒存储库贡献者，但仍会触发管道。
- [Abusing Repository Webhooks to Access Internal CI/CD Systems at Scale](https://www.paloaltonetworks.com/blog/prisma-cloud/repository-webhook-abuse-access-ci-cd-systems-at-scale/) - 用于触发 CI/CD 管道的存储库 Webhook 可能被滥用来访问内部系统。
- [Bypassing required reviews using GitHub Actions](https://medium.com/cider-sec/bypassing-required-reviews-using-github-actions-6e1b29135cc7) - GitHub Actions 可以绕过所需的审查，允许恶意代码推送到受保护的分支。
- [Forging signed commits on GitHub](https://iter.ca/post/gh-sig-pwn/) - GitHub API 中的一个错误允许伪造签名提交。通过利用内部 Codespaces API 端点中的正则表达式缺陷，攻击者可以创建由任何用户签名的提交，尽管有 GitHub 的 Web 流签名。
- [GitHub comments abused to push malware via Microsoft repo URLs](https://www.bleepingcomputer.com/news/security/github-comments-abused-to-push-malware-via-microsoft-repo-urls/) - 隐藏的 GitHub 评论链接。
- [How a Single Vulnerability Can Bring Down the JavaScript Ecosystem](https://www.landh.tech/blog/20240603-npm-cache-poisoning/) - 对 NPM 注册表的缓存中毒攻击导致包不可用。
- [One Supply Chain Attack to Rule Them All – Poisoning GitHub's Runner Images](https://adnanthekhan.com/2023/12/20/one-supply-chain-attack-to-rule-them-all/) - GitHub Actions 中存在一个严重漏洞，涉及 actions/runner-images 存储库中配置错误的自托管运行程序，可能会危及所有 GitHub 和 Azure 托管运行程序映像。
- [PR sneaking](https://github.com/mortenson/pr-sneaking) - 将恶意代码潜入 GitHub 拉取请求的方法。
- [Remove evidence of malicious pull requests on GitHub](https://x.com/adnanthekhan/status/1829116171045474374) - 将帐户的电子邮件更改为阻止列出的域，会自动禁止该帐户。
- [StarJacking – Making Your New Open Source Package Popular in a Snap](https://checkmarx.com/blog/starjacking-making-your-new-open-source-package-popular-in-a-snap/) - StarJacking 是一种攻击者使恶意开源软件包看起来很流行的技术。
- [The massive bug at the heart of the npm ecosystem](https://blog.vlt.sh/blog/the-massive-hole-in-the-npm-ecosystem) - NPM 明显混乱。
- [Trojan Source](https://trojansource.codes/) - 攻击者可以攻击源代码文件的编码来注入漏洞，而不是插入逻辑错误。
- [Unpinnable Actions: How Malicious Code Can Sneak into Your GitHub Actions Workflows](https://www.paloaltonetworks.com/blog/prisma-cloud/unpinnable-actions-github-security/) - GitHub Actions 即使固定到提交 SHA，仍然可以通过可变依赖项（例如 Docker 映像、未锁定的包或外部脚本）提取恶意代码。
- [Why npm lockfiles can be a security blindspot for injecting malicious modules](https://snyk.io/blog/why-npm-lockfiles-can-be-a-security-blindspot-for-injecting-malicious-modules/) - 恶意代码可以通过lockfiles（package-lock.json或yarn.lock）注入到npm项目中，因为这些机器生成的大型文件很少被彻底审查。
- [Working as unexpected](https://www.chainguard.dev/unchained/working-as-unexpected) - 创建一个 GitHub 分支，将分支保护规则模式与工作流文件相匹配，该工作流文件在推送时触发以获取对环境机密的访问权限。
- [Zuckerpunch - Abusing Self Hosted GitHub Runners at Facebook](https://marcyoung.us/post/zuckerpunch/) - 隐藏 GitHub PR 中的提交。

## 工具
- [ADOKit](https://github.com/xforcered/ADOKit) - Azure DevOps 服务攻击工具包。
- [Gato](https://github.com/praetorian-inc/gato) - GitHub 攻击工具包。
- [Gato-X](https://github.com/AdnaneKhan/Gato-X) - GitHub 攻击工具包 - 至尊版。
- [GH Archive](https://www.gharchive.org/) - 一个记录公共 GitHub 时间线、存档并使其易于访问以供进一步分析的项目。
- [GHTorrent Project](http://ghtorrent-downloads.ewi.tudelft.nl/mysql/) - GitHub API 数据的可查询离线镜像。 [教程](https://ghtorrent.github.io/tutorial/)。
- [git-dumper](https://github.com/arthaud/git-dumper) - 从网站转储 Git 存储库。
- [GitFive](https://github.com/mxrch/gitfive) - 用于调查 GitHub 配置文件的 OSINT 工具。
- [Grep.app](https://grep.app/) - 使用正则表达式搜索 GitHub。
- [Jenkins Attack Framework](https://github.com/Accenture/jenkins-attack-framework) - 该工具可以管理 Jenkins 任务，例如列出作业、转储凭据、运行命令/脚本以及管理 API 令牌。
- [Nord Stream](https://github.com/synacktiv/nord-stream) - 一种提取 CI/CD 环境中存储的秘密的工具。
- [pwn_jenkins](https://github.com/gquere/pwn_jenkins) - 有关攻击 Jenkins 服务器的说明。
- [Secrets Patterns Database](https://github.com/mazen160/secrets-patterns-db) - 最大的开源数据库，用于检测秘密、API 密钥、密码、令牌等。
- [Sourcegraph](https://sourcegraph.com/search) - 用于公共存储库的基于网络的代码搜索和导航工具。
- [Token-Spray](https://blog.projectdiscovery.io/nuclei-v2-5-3-release/) - 使用 Nuclei 自动进行令牌验证。
- [zizmor](https://github.com/zizmorcore/zizmor) - GitHub Actions 的静态分析。

## 案例研究
- [10 real-world stories of how we've compromised CI/CD pipelines](https://www.nccgroup.com/research-blog/10-real-world-stories-of-how-we-ve-compromised-cicd-pipelines/) - 示例包括利用 S3 错误配置、Jenkins 插件缺陷、GitLab 运行程序权限升级、Kubernetes pod 注释漏洞以及受损的开发人员笔记本电脑。
- [GitHub Actions Attack Diagram](https://github.com/jstawinski/GitHub-Actions-Attack-Diagram) - 包括在 Black Hat USA 2024 和 DEF CON 32 上提出的公开漏洞研究。
- [Playing with Fire – How We Executed a Critical Supply Chain Attack on PyTorch](https://johnstawinski.com/2024/01/11/playing-with-fire-how-we-executed-a-critical-supply-chain-attack-on-pytorch/) - 研究人员通过恶意拉取请求利用了一个关键的 PyTorch 漏洞，在自托管运行器上执行代码。

## 类似项目
- [CI/CD 管道的常见威胁矩阵](https://github.com/rung/threat-matrix-cicd)
- [开放软件供应链攻击参考 (OSC&R)](https://pbom.dev/)
- [软件供应链风险浏览器](https://riskexplorer.endorlabs.com/#/attack-tree)
- [SDLC Infrastructure Threat Framework (SITF)](https://github.com/wiz-sec-public/SITF) - 用于分析和防御针对软件开发生命周期基础设施的攻击的综合框架。
