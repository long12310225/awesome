<p align="center">
  <br>
    <img src="awesome-actions.png" width="150"/>
  <br>
</p>

# 很棒的操作 [<!--lint 忽略 no-dead-urls-->![GitHub 操作状态 | sdras/awesome-actions](https://github.com/sdras/awesome-actions/workflows/Lint%20Awesome%20List/badge.svg)](https://github.com/sdras/awesome-actions/actions?workflow=Lint+Awesome+List) [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

> 与 GitHub Actions 相关的精彩内容的精选列表。

操作由存储库中的 GitHub 平台事件直接触发，并在 Linux、Windows 或 macOS 虚拟机上或在容器内运行按需工作流程作为响应。借助 GitHub Actions，您可以自动化从创意到生产的工作流程。

## 内容

- [官方资源](#official-resources)
  - [工作流程示例](#workflow-examples)
  - [官方行动](#official-actions)
  - [创建您的行动](#create-your-actions)
- [社区资源](#community-resources)
  - [GitHub 工具和管理](#github-tools-and-management)
  - [动作集合](#collection-of-actions)
  - [Utility](#utility)
  - [静态分析](#static-analysis)
  - [动态分析](#dynamic-analysis)
  - [Monitoring](#monitoring)
  - [请求请求](#pull-requests)
  - [GitHub 页面](#github-pages)
  - [通知和消息](#notifications-and-messages)
  - [Deployment](#deployment)
  - [外部服务](#external-services)
  - [前端工具](#frontend-tools)
  - [机器学习操作](#machine-learning-ops)
  - [Build](#build)
  - [Database](#database)
  - [Networking](#networking)
  - [Localization](#localization)
  - [Fun](#fun)
  - [备忘单](#cheat-sheet)
- [Tutorials](#tutorials)

## 官方资源

- [官方网站](https://github.com/features/actions)
- [官方文档](https://help.github.com/en/actions)
- [官方行动组织](https://github.com/actions)
  - [actions/virtual-environments](https://github.com/actions/virtual-environments) - GitHub Actions 虚拟环境。
  - [actions/runner](https://github.com/actions/runner) - GitHub Actions 的运行器。
- [GitHub 博客公告](https://github.blog/2018-10-17-action-demos/)

### 工作流程示例

- [actions/starter-workflows](https://github.com/actions/starter-workflows) - 入门工作流程管理。
- [actions/example-services](https://github.com/actions/example-services) - 使用服务容器的示例工作流程。

### 官方行动

<!--lint disable no-dead-urls-->

#### 工作流程工具操作

适用于您的工作流程的工具操作。

<!--lint ignore awesome-spell-check-->

- [actions/checkout](https://github.com/actions/checkout) - 在您的工作流程中设置存储库。
- [actions/upload-artifact](https://github.com/actions/upload-artifact) - 从您的工作流程上传工件。
- [actions/download-artifact](https://github.com/actions/download-artifact) - 从您的构建中下载工件。
- [actions/cache](https://github.com/actions/cache) - 在 GitHub Actions 中缓存依赖项并构建输出。
- [actions/github-script](https://github.com/actions/github-script) - 为 GitHub API 和工作流程上下文编写脚本。

#### GitHub 自动化操作

自动管理问题、拉取请求和发布。

- [actions/create-release](https://github.com/actions/create-release) - 通过 GitHub Release API 创建版本的操作。
- [actions/upload-release-asset](https://github.com/actions/upload-release-asset) - 通过 GitHub Release API 上传发布资产的操作。
- [actions/first-interaction](https://github.com/actions/first-interaction) - 用于过滤来自首次贡献者的拉取请求和问题的操作。
- [actions/stale](https://github.com/actions/stale) - 标记最近没有交互的问题和拉取请求。
- [actions/labeler](https://github.com/actions/labeler) - 自动标记拉取请求的操作。
- [actions/delete-package-versions](https://github.com/actions/delete-package-versions) - 从 GitHub Packages 中删除包的版本。

#### 设置操作

使用特定版本的编程语言设置 GitHub Actions 工作流程。

- [操作/设置节点：Node.js](https://github.com/actions/setup-node)
- [操作/设置-python：Python](https://github.com/actions/setup-python)
- [动作/设置-go：开始](https://github.com/actions/setup-go)
- [操作/设置-dotnet：.NET core sdk](https://github.com/actions/setup-dotnet)
- [actions/setup-haskell：Haskell（GHC 和 Cabal）](https://github.com/actions/setup-haskell)
- [操作/设置-java：Java](https://github.com/actions/setup-java)
- [操作/设置-ruby：Ruby](https://github.com/actions/setup-ruby)
- [动作/设置-elixir: Elixir](https://github.com/actions/setup-elixir)
- [动作/设置-朱莉娅：朱莉娅](https://github.com/julia-actions/setup-julia)

### 创建您的行动

#### JavaScript 和 TypeScript 操作

- [actions/toolkit](https://github.com/actions/toolkit) - 用于开发 GitHub Actions 的 GitHub ToolKit。
- [actions/hello-world-javascript-action](https://github.com/actions/hello-world-javascript-action) - 用于演示如何构建 JavaScript 操作的模板。
- [actions/javascript-action](https://github.com/actions/javascript-action) - 创建 JavaScript 操作。
- [actions/typescript-action](https://github.com/actions/typescript-action) - 创建 TypeScript 操作。
- [actions/http-client](https://github.com/actions/http-client) - 一个轻量级 HTTP 客户端，优化用于操作、带有泛型的 TypeScript 和异步等待。

#### Docker 容器操作

- [actions/hello-world-docker-action](https://github.com/actions/hello-world-docker-action) - 用于演示如何构建 Docker 操作的模板。
- [actions/container-toolkit-action](https://github.com/actions/container-toolkit-action) - 用于使用 actions/toolkit 创建容器操作的模板存储库。

## 社区资源

### GitHub 工具和管理

- [以声明方式设置 GitHub 标签](https://github.com/lannonbr/issue-label-manager-action)
- [以声明方式同步 GitHub 标签的操作](https://github.com/micnncim/action-label-syncer)
- [将版本添加到 GitHub](https://github.com/elgohr/Github-Release-Action)
- [将 docker 镜像发布到 Dockerhub](https://github.com/elgohr/Publish-Docker-Github-Action)
- [使用文件中的内容创建问题](https://github.com/peter-evans/create-issue-from-file)
- [使用资产发布 GitHub 版本](https://github.com/softprops/action-gh-release)
- [GitHub Project Automation+](https://github.com/alex-page/github-project-automation-plus) - 使用任何 Webhook 事件自动化 GitHub 项目卡。
- [使用 Web 界面在本地运行 GitHub Actions](https://github.com/phishy/wflow)
- [在终端中本地运行 GitHub Actions](https://github.com/nektos/act)
- [构建并发布 Android 调试 APK](https://github.com/ShaunLWM/action-release-debugapk)
- [为 GitHub Actions 生成连续的内部版本号](https://github.com/einaregilsson/build-number)
- [将 Git 更改推送到 GitHub 存储库，没有身份验证困难](https://github.com/ad-m/github-push-action)
- [根据您的事件生成发行说明](https://github.com/Decathlon/release-notes-generator-action)
- [根据提供的 markdown 文件创建 GitHub wiki 页面](https://github.com/Decathlon/wiki-page-creator-action)
- [自动神奇地标记您的拉取请求（使用提交的文件）](https://github.com/Decathlon/pull-request-labeler-action)
- [根据作者团队名称将标签添加到您的 Pull Request](https://github.com/JulienKode/team-labeler-action)
- [通过 PR/Push 获取文件更改列表](https://github.com/trilom/file-changes-action)
- [在任何工作流程中使用私有操作](https://github.com/InVisionApp/private-action-loader)
- [使用问题内容标记您的问题](https://github.com/damccorm/tag-ur-it)
- [回滚 GitHub 版本](https://github.com/author/action-rollback)
- [一段时间不活动后锁定已关闭的问题和拉取请求](https://github.com/dessant/lock-threads)
- [获取两个分支之间的提交差异计数](https://github.com/jessicalostinspace/commit-difference-action)
- [根据 Git 参考生成发行说明](https://github.com/metcalfc/changelog-generator)
- [对 GitHub 存储库和提交执行策略](https://github.com/talos-systems/conform)
- [根据问题描述自动标记问题](https://github.com/Renato66/auto-label)
- [将配置的 GitHub 操作更新到最新版本](https://github.com/fabasoad/ghacu)
- [创建问题分支](https://github.com/robvanderleek/create-issue-branch)
- [移除旧文物](https://github.com/c-hive/gha-remove-artifacts)
- [将 Git 提交数据公开为环境变量](https://github.com/rlespinasse/git-commit-data-action)
- [将定义的文件/二进制文件同步到 Wiki 或外部存储库](https://github.com/kai-tub/external-repo-sync-action)
- [基于任何文件创建/更新/删除 GitHub Wiki 页面](https://github.com/Andrew-Chen-Wang/github-wiki-action)
- [Prow GitHub Actions](https://github.com/jpmcb/prow-github-actions) - 策略执行、聊天操作和自动 PR 合并的自动化。
- [检查工作流程中的 GitHub 状态](https://github.com/crazy-max/ghaction-github-status)
- [以代码形式管理 GitHub 上的标签（创建/重命名/更新/删除）](https://github.com/crazy-max/ghaction-github-labeler)
- [持续向您的项目贡献者和依赖项分配资金](https://github.com/protontypes/libreselery)
- [GitHub 的 Herald 规则：向您的 PR 添加订阅者、受让人、标签等](https://github.com/gagoar/use-herald-action)
- [GitHub Codeowners Validator](https://github.com/mszostok/codeowners-validator) - 确保 GitHub CODEOWNERS 文件的正确性。它支持公共和私有 GitHub 存储库以及 GitHub Enterprise 安装。
- [Copybara Action](https://github.com/olivr/copybara-action) - 在存储库之间移动和转换代码（非常适合从一个单一存储库维护多个存储库）。

### 动作集合

- [使用 HashiCorp 的 Terraform](https://github.com/hashicorp/setup-terraform)
- [Yarn 1 的 GitHub 操作](https://github.com/Borales/actions-yarn)
- [Yarn 2 的 GitHub 操作](https://github.com/sergioramos/yarn-actions)
- [Golang 的 GitHub Actions](https://github.com/cedrickring/golang-action)
- [R 的 GitHub Actions 和随附的 #rstats 包](http://maxheld.de/ghactions/)
- [适用于 WordPress 的 GitHub 操作](https://github.com/10up/actions-wordpress/)
- [Composer 的 GitHub 操作](https://github.com/MilesChou/composer-action)
- [Flutter 的 GitHub 操作](https://github.com/subosito/flutter-action)
- [PHP 的 GitHub 操作](https://github.com/shivammathur/setup-php)
- [Rust 的 GitHub 操作](https://github.com/actions-rs)
- [适用于 Android 的 GitHub 操作](https://github.com/Malinskiy/action-android)
- [Logtalk 和 Prolog 的 GitHub Actions](https://github.com/logtalk-actions)
- [Deno 的 GitHub 操作](https://github.com/denolib/setup-deno)
- [Unity 的 GitHub 操作](https://github.com/webbertakken/unity-actions)
- [Octions - GitHub REST API 的 GitHub Actions](https://github.com/maxkomarychev/octions)
- [Docker 的 GitHub 操作](https://github.com/docker/github-actions)
- [适用于 AWS 的 GitHub 操作](https://github.com/clowdhaus/aws-github-actions)
- [行动中心](https://github.com/actionshub)

### 实用性

- [Setup `ssh-agent`](https://github.com/webfactory/ssh-agent) - 使用额外的 SSH 密钥运行“ssh-agent”来访问私有存储库。
- [自述文件的 GitHub Actions 徽章](https://github.com/atrox/github-actions-badge)
- [带有诗歌的 Python 项目的 GitHub Actions](https://github.com/abatilo/actions-poetry)
- [使用 pyenv 的 Python 项目的 GitHub Actions](https://github.com/gabrielfalcao/pyenv-action)
- [GitHub Actions 编译 LaTeX 文档](https://github.com/xu-cheng/latex-action)
- [更新 Maxmind 数据库](https://github.com/meetup/maxmind-updater)
- [Debug with SSH over tmate](https://github.com/mxschmitt/action-tmate) - 通过提供 SSH 连接直接调试操作。
- [解锁 git-crypt 文件](https://github.com/sliteteam/github-action-git-crypt-unlock)
- [Golang CGO 交叉编译器](https://github.com/crazy-max/ghaction-xgo)
- [在另一种架构上运行您的作业：arm32、aarch64 等](https://github.com/uraimo/run-on-arch-action)
- [生成目录](https://github.com/technote-space/toc-generator)
- [自动向问题添加标签或受让人](https://github.com/Naturalclar/issue-action)
- [当我们说 LGTM 时，以图像或 GIF 形式发送 LGTM 反应的操作](https://github.com/micnncim/action-lgtm-reaction)
- [跨多个范围生成内部版本号](https://github.com/zyborg/gh-action-buildnum)
- [发布 GitHub 版本工件](https://github.com/skx/github-action-publish-binaries)
- [Jekyll Diff Action](https://github.com/David-Byrne/jekyll-diff-action) - 对更改后构建的 Jekyll 站点进行比较，并将结果评论回 GitHub。
- [Branch Protection Bot](https://github.com/benjefferies/branch-protection-bot) - 暂时禁用并重新启用分支保护中的“包括管理员”选项。
- [Wait for commit statuses](https://github.com/WyriHaximus/github-action-wait-for-status) - 等待所有状态和检查成功或其中任何一个失败，并相应地设置其状态输出。
- [Get Latest Tag](https://github.com/WyriHaximus/github-action-get-previous-tag) - 从 git 获取上一个标签。
- [Create Milestone](https://github.com/WyriHaximus/github-action-create-milestone) - 根据标题和描述创建一个新的开放里程碑。
- [Close Milestone](https://github.com/WyriHaximus/github-action-close-milestone) - 关闭给定的里程碑。
- [强制执行分支命名规则的操作](https://github.com/deepakputhraya/action-branch-name)
- [公开一些 GitHub 变量的 slug](https://github.com/marketplace/actions/github-slug)
- [Awesome-lint 作为 GitHub 操作](https://github.com/max/awesome-lint)
- [编辑 JSON 文件](https://github.com/deef0000dragon1/json-edit-action)
- [构建 Slate 文档](https://github.com/Decathlon/slate-builder-action)
- [Read Properties](https://github.com/christian-draeger/read-properties) - 从“.properties”文件中读取值。
- [Write Properties](https://github.com/christian-draeger/write-properties) - 将值写入“.properties”文件。
- [Autotag](https://github.com/butlerlogic/action-autotag) - 当清单文件（即“package.json”）版本更改时自动生成新标签。
- [Apply templates with Jinja2](https://github.com/cuchi/jinja2-action) - 使用 Jinja2 模板引擎从模板生成文件。
- [Has Changes](https://github.com/UnicornGlobal/has-changes-action) - 检查前面的步骤是否有代码更改。
- [Mind Your Language Action](https://github.com/tailaiw/mind-your-language-action) - 检测问题和拉取请求中的攻击性评论，并警告发件人。
- [YAML/JSON/XML Converter](https://github.com/fabasoad/yaml-json-xml-converter-action) - 可互换地转换 YAML/JSON/XML 文件格式。
- [NSFW Detection](https://github.com/fabasoad/nsfw-detection-action) - 检测已提交文件中的 NSFW 内容。
- [Has Changed Path](https://github.com/MarceloPrado/has-changed-path) - 根据更改的路径有条件地运行操作。
- [Linguist](https://github.com/fabasoad/linguist-action) - 检查存储库并在输出中生成有关所用语言的信息。
- [Twilio Voice Call](https://github.com/fabasoad/twilio-voice-call-action/) - 使用定义的文本进行 Twilio 语音通话。
- [Setup Xcode](https://github.com/maxim-lobanov/setup-xcode) - 在适用于 macOS 映像的预安装 Xcode 版本之间切换。
- [Setup Xamarin](https://github.com/maxim-lobanov/setup-xamarin) - 在适用于 macOS 图像的 Xamarin 和 Mono 预安装版本之间切换。
- [Memer Action](https://github.com/Bhupesh-V/memer-action) - 程序员 Memes 的 GitHub 操作 xD。
- [Setup Cocoapods](https://github.com/maxim-lobanov/setup-cocoapods) - 设置特定版本的 Cocoapods。
- [Public IP](https://github.com/haythem/public-ip) - 查询 GitHub actions runner 的公共 IP 地址。
- [Lazarus/FPC 的 GitHub 操作](https://github.com/gcarreno/setup-lazarus)
- [Twilio Fax](https://github.com/fabasoad/twilio-fax-action/) - 使用您的 Twilio 帐户通过传真发送文档。
- [Setup Kubernetes tools](https://github.com/yokawasa/action-setup-kube-tools) - 在运行器上安装 Kubernetes 工具（kubectl、kustomize、helm、kubeval、conftest 和 yq）。
- [Setup Elastic Cloud Control Tool](https://github.com/yokawasa/action-setup-ecctl) - 在运行器上安装特定版本的 ecctl。
- [PowerShell Script](https://github.com/Amadevus/pwsh-script) - 使用工作流上下文（例如“$github.token”）和 cmdlet 运行 PowerShell 脚本，返回值 => 操作输出。
- [使用 VirusTotal 上传和扫描文件](https://github.com/crazy-max/ghaction-virustotal)
- [导入 GPG 密钥](https://github.com/crazy-max/ghaction-import-gpg)
- [Compress with UPX](https://github.com/crazy-max/ghaction-upx) - 可执行文件的终极加壳器。
- [Pull the New Go Module Version Into the Proxy Cache](https://github.com/andrewslotin/go-proxy-pull-action) - 确保最新版本的 Go 模块位于代理缓存中。还在发布时更新了 pkg.go.dev 文档。
- [Delete Run Artifacts](https://github.com/marketplace/actions/delete-run-artifacts) - 在工作流运行结束时删除所有工件。
- [GitHub Environment Variables Action](https://github.com/FranzDiebold/github-env-vars-action) - 公开环境变量，例如分支/标签名称、存储库 slug 和 ref slug。
- [GitHub Action Locks](https://github.com/abatilo/github-action-locks/blob/master/README.md) - 保证 GitHub Action 工作流程的原子执行。
- [Paths Filter](https://github.com/dorny/paths-filter) - 根据 PR、功能分支或推送提交修改的文件有条件地运行操作。
- [Minisauras](https://github.com/TeamTigers/minisauras) - 从基础分支中提取所有 JavaScript 和 CSS 文件，缩小它们并使用新分支创建拉取请求。
- [Website to GIF](https://github.com/PabloLec/website-to-gif) - 将任何网页转换为 GIF 以显示在您的自述文件、文档等中。
- [Interactive Inputs - Runtime workflow inputs](https://github.com/boasiHQ/interactive-inputs) - 在运行时为 GitHub Actions 工作流程添加动态输入

#### 环境

- [创建一个环境文件](https://github.com/SpicyPizza/create-envfile)
- [导出全局环境变量以用于后续的构建步骤](https://github.com/zweitag/github-actions)
- [以编程方式设置环境变量以在后续步骤中使用](https://github.com/allenevans/set-env)
- [安装Python的Conda环境](https://github.com/goanpeca/setup-miniconda)
- [设置 NativeScript](https://github.com/hrueger/setup-nativescript)
- [创建 JSON 环境文件](https://github.com/schdck/create-env-json)

#### 依赖关系

- [使用缓存安装 NPM 依赖项](https://github.com/bahmutov/npm-install)
- [Highlight New NPM Dependencies](https://github.com/hiwelo/new-dependencies-action) - 对拉取请求的评论新添加了 NPM 依赖项信息。
- [缓存 NPM 依赖项](https://github.com/c-hive/gha-npm-cache)
- [缓存 Yarn 依赖项](https://github.com/c-hive/gha-yarn-cache)

#### 语义版本控制

- [Next SemVers](https://github.com/WyriHaximus/github-action-next-semvers) - 根据给定的 semver 版本输出主要版本、次要版本和补丁版本的下一个版本。
- [给定搜索字符串获取最新的 SemVer 和分支名称](https://github.com/jessicalostinspace/github-action-get-regex-branch)
- [Cut Release Branch](https://github.com/jessicalostinspace/cut-release-action) - 在给定分支前缀和可选语义版本的情况下剪切发布分支。
- [Increment Semantic Version](https://github.com/christian-draeger/increment-semantic-version) - 根据给定的发布类型，更改给定的语义版本 (SemVer)。

### 静态分析

- [PHPStan 静态代码分析器操作](https://github.com/OskarStark/phpstan-ga)
- [GraphQL 检查器操作](https://github.com/kamilkisiela/graphql-inspector)
- [使用 PSScriptAnalyzer 进行 PowerShell 静态分析](https://github.com/devblackops/github-action-psscriptanalyzer)
- [运行 tfsec，并在 PR 上输出 reviewdog](https://github.com/reviewdog/action-tfsec)

#### 测试

- [通过 Puppeteer（无头 Chrome 节点 API）运行测试](https://github.com/ianwalter/puppeteer)
- [xUnit Slack Reporter：将 xUnit 报告中的测试摘要发送到 Slack 通道](https://github.com/ivanklee86/xunit-slack-reporter)
- [运行代码接收测试](https://github.com/joelwmale/codeception-action)
- [运行 TestCafe 测试](https://github.com/DevExpress/testcafe-action)
- [运行 Unity 测试](https://github.com/webbertakken/unity-test-runner)
- [运行赛普拉斯 E2E 测试](https://github.com/cypress-io/github-action)
- [使用 Molecule 测试 Ansible 角色](https://github.com/robertdebock/molecule-action)
- [使用 artillery.io 运行性能测试](https://github.com/kenju/github-actions-artillery)
- [使用 BuildPulse 检测片状测试](https://github.com/Workshop64/buildpulse-action)
- [显示 Jest 测试的内联代码注释](https://github.com/IgnusG/jest-report-action)
- [运行 Julia 测试](https://github.com/julia-actions/julia-runtest)

#### 棉绒

- [PHP 编码标准修复程序操作](https://github.com/OskarStark/php-cs-fixer-ga)
- [针对存储库中的 Dockerfile 运行 Hadolint](https://github.com/burdzwastaken/hadolint-action)
- [运行 ESLint，并在 PR 上输出 reviewdog](https://github.com/reviewdog/action-eslint)
- [基于 JavaScript 的 \*.workflow 文件 linter](https://github.com/OmarTawfik/github-actions-js)
- [使用 tflint 对 terraform 文件进行 Lint，并在 PR 上提供 reviewdog 输出](https://github.com/reviewdog/action-tflint)
- [autopep8：自动格式化 Python 代码以符合 PEP 8 风格指南](https://github.com/peter-evans/autopep8)
- [运行“ergebnis/composer-normalize”以确保您的 PHP 项目具有规范化的“composer.json”](https://github.com/ergebnis/composer-normalize-action)
- [运行“stolt/lean-package-validator”以确保您的包仅具有所需的“运行时”工件](https://github.com/raphaelstolt/lean-package-validator-action)
- [对 PR 事件运行 Go lint 检查](https://github.com/ArangoGutierrez/GoLinty-Action)
- [Node.js - 自动运行包使用的 `format` 和/或 `lint` 脚本](https://github.com/MarvinJWendt/run-node-formatter)
- [Stylelinter - 运行 stylelint 的 GitHub Action](https://github.com/exelban/stylelint)
- [运行 stylelint，并在 PR 上输出 reviewdog](https://github.com/reviewdog/action-stylelint)
- [PyCodeStyle Action - 一个 GitHub Action，通过 pycodestyle (autopep8) 反馈在您的 PR 上留下评论](https://github.com/ankitvgupta/pycodestyle-action)
- [wemake-python-styleguide - 有史以来最严格、最固执己见的 python linter，在 PR 上有可选的 reviewdog 输出](https://github.com/wemake-services/wemake-python-styleguide)
- [运行 TSLint 并进行状态检查和文件差异注释](https://github.com/mooyoul/tslint-actions)
- [Lint Pull 请求使用 commitlint 提交](https://github.com/wagoid/commitlint-github-action)
- [运行 Vint，并在 PR 上输出 reviewdog](https://github.com/reviewdog/action-vint)
- [运行拼写错误，并在 PR 上输出 reviewdog](https://github.com/reviewdog/action-misspell)
- [运行 golangci-lint，并在 PR 上输出 reviewdog](https://github.com/reviewdog/action-golangci-lint)
- [运行 shellcheck，并在 PR 上输出 reviewdog](https://github.com/reviewdog/action-shellcheck)
- [发现 Markdown 文档中不敏感、不考虑周全的写作](https://github.com/theashraf/alex-action)
- [运行 dotenv-linter - 像魅力一样检查您的 .env 文件，并在 PR 上提供可选的 reviewdog 输出](https://github.com/wemake-services/dotenv-linter)
- [运行 dotenv-linter，并在 PR 上输出 reviewdog](https://github.com/mgrachev/action-dotenv-linter)
- [显示并自动修复许多编程语言的 linting 错误](https://github.com/samuelmeuli/lint-action)
- [带注释的 PHP_CodeSniffer](https://github.com/chekalsky/phpcs-action)
- [Markdown 的 Linter（带有预设）](https://github.com/avto-dev/markdown-lint)
- [用于创建注释的 Stylelint 问题匹配器](https://github.com/xt0rted/stylelint-problem-matcher)
- [在 PR 上运行 sqlcheck 以识别 SQL 查询中的反模式](https://github.com/yokawasa/action-sqlcheck)
- [根据 Play 商店指南验证 Fastlane 供应元数据](https://github.com/ashutoshgngwr/validate-fastlane-supply-metadata)
- [运行 Golint 来检查你的 Golang 代码](https://github.com/Jerome1337/golint-action)

#### 安全性

- [适用于 Docker 镜像的漏洞扫描器](https://github.com/phonito/phonito-scanner-action)
- [自动批准并合并 Dependabot 更新](https://github.com/ridedott/dependabot-auto-merge-action)
- [在 Python 代码上运行 dlint security linter](https://github.com/xen0l/dlint-check)
- [AWS Secrets Manager Actions](https://github.com/say8425/aws-secrets-manager-actions) - 将 AWS Secrets Manager 密钥定义为环境值。
- [检查您的 AWS IAM 策略文档的正确性和安全问题](https://github.com/xen0l/iam-lint)
- [Secret Spreader](https://github.com/webfactory/secret-spreader) - 本身不是一个操作，而是一个跨存储库列表管理操作秘密的工具。
- [Secrets Sync Action](https://github.com/google/secrets-sync-action) - Action 跨多个存储库同步机密。
- [Snyk 测试动作](https://github.com/snyk/actions)
- [使用简单的 CLI 管理您的 GitHub Actions 机密](https://github.com/unfor19/githubsecrets)
- [SecretHub](https://github.com/secrethub/actions) - 为您的秘密提供单一事实来源，并根据需要将其加载到 GitHub Actions 中。

#### 代码覆盖率

- [使用 SonarCloud 扫码](https://github.com/sonarsource/sonarcloud-github-action)
- [将您的代码覆盖率发送至 codecov.io](https://github.com/codecov/codecov-action)
- [将代码覆盖率发布到 CodeClimate](https://github.com/paambaati/codeclimate-action)
- [更新存储库报告卡](https://github.com/creekorful/goreportcard-action)

### 动态分析

- [运行 Gofmt 检查 Golang 代码格式](https://github.com/Jerome1337/gofmt-action)
- [运行 Goimports 检查 Golang 导入顺序](https://github.com/Jerome1337/goimports-action)

### 监控

- [使用 Google Chrome 的 Lighthouse 测试审核网页](https://github.com/jakejarvis/lighthouse-action)
- [运行 Lighthouse 并将结果发布到 PR 和 Slack](https://github.com/foo-software/lighthouse-check-action)
- [使用 GitHub Actions 在 CI 中运行 Lighthouse](https://github.com/treosh/lighthouse-ci-action)
- [Go 的持续基准测试和基准可视化](https://github.com/bobheadxi/gobenchdata)
- [Size Limit Action](https://github.com/andresz1/size-limit-action) - 评论会比较 PR 中的 JS，如果超出限制则拒绝它们。
- [Check bundlephobia](https://github.com/carlesnunez/check-my-bundlephobia) - 根据bundlephobia.io 网站评论新的和修改的包大小，并拒绝超出阈值的 PR。

### 请求请求

- [根据受让人设置 PR 审阅者](https://github.com/pullreminders/assignee-to-reviewer-action)
- [在分支推送上打开或更新 PR（带有分支选择）](https://github.com/vsoch/pull-request-action)
- [自动调整 PR 基础](https://github.com/cirrus-actions/rebase)
- [一旦获得指定数量的批准，即可为 PR 贴上标签](https://github.com/pullreminders/label-when-approved-action)
- [根据匹配的文件模式向 PR 添加标签](https://github.com/banyan/auto-label)
- [自动批准 PR](https://github.com/hmarr/auto-approve-action)
- [根据配置文件自动添加审稿人到PR](https://github.com/kentaro-m/auto-assign-action)
- [根据分支名称模式向 PR 添加标签](https://github.com/TimonVS/pr-labeler-action)
- [根据差异的总大小向 PR 添加标签](https://github.com/pascalgn/size-label-action)
- [自动合并准备好的 PR](https://github.com/pascalgn/automerge-action)
- [验证 PR 是否包含票证参考](https://github.com/vijaykramesh/pr-lint-action)
- [在操作工作区中为存储库的更改创建 PR](https://github.com/peter-evans/create-pull-request)
- [维护 PR](https://github.com/seferov/pr-lint-action)
- [PR 的 ChatOps](https://github.com/machine-learning-apps/actions-chatops)
- [基于从分支名称中提取的文本的 PR 的前缀标题和正文](https://github.com/tzkhan/pr-update-action)
- [阻止 Autosquash 提交](https://github.com/xt0rted/block-autosquash-commits-action)
- [合并时自动碰撞和标记](https://github.com/anothrNick/github-tag-action)
- [使用过时的检查自动更新 PR，并压缩和合并与所有分支保护匹配的 PR](https://github.com/tibdex/autosquash)
- [Merge Pal - 自动更新和合并 PR](https://github.com/maxkomarychev/merge-pal-action)
- [对拉取请求标题强制执行命名约定](https://github.com/deepakputhraya/action-pr-title)
- [拉取请求卡住通知程序](https://github.com/jrylan/github-action-stuck-pr-notifier)
- [带 commitlint 的 Lint 拉取请求名称（如果压缩合并那就太棒了！）](https://github.com/JulienKode/pull-request-name-linter-action)
- [当目标分支检查失败时阻止 PR 合并](https://github.com/cirrus-actions/branch-guard)
- [获取由 Pull Request 更新的生成的静态站点屏幕截图](https://github.com/ssowonny/diff-pages-action)
- [根据拉取请求是否仍在进行中添加标签](https://github.com/AlbertHernandez/working-label-action)
- [Ticket Check Action](https://github.com/neofinancial/ticket-check-action) - 自动将票证或问题编号添加到所有 Pull 请求标题的开头。
- [使用正则表达式拉取请求 Lint](https://github.com/MorrisonCole/pr-lint-action)
- [拉请求地雷](https://github.com/tylermurry/github-pr-landmine)
- [基于 Checkstyle XML 报告注释 GitHub Pull 请求](https://github.com/staabm/annotate-pull-request-from-checkstyle)
- [Pull Request Stats](https://github.com/flowwer-dev/pull-request-stats) - 打印有关审稿人的相关统计数据。
- [Pull Request Description Enforcer](https://github.com/derkinderfietsen/pr-description-enforcer) - 强制执行拉取请求的描述。

### GitHub 页面

- [将 Zola 站点部署到 GitHub Pages](https://github.com/shalzz/zola-deploy-action)
- [构建Hugo静态内容站点并将其发布到gh-pages分支](https://github.com/khanhicetea/gh-actions-hugo-deploy-gh-pages)
- [使用自定义 Jekyll 插件和构建脚本构建 Jekyll 站点并将其部署回 Gh-Pages 分支](https://github.com/BryanSchuetz/jekyll-deploy-gh-pages)
- [Google Dataset Search Metadata](https://www.github.com/openschemas/extractors/) - 以及其他 schema.org 提取器，使数据集可从 GitHub 页面发现。
- [用于使用静态站点生成器部署到 GitHub Pages 的 GitHub Actions](https://github.com/peaceiris/actions-gh-pages)
- [Hexo 的 GitHub 操作](https://github.com/heowc/action-hexo)
- [将 Google Analytics 统计信息部署到 GitHub Pages](https://github.com/cristianpb/analytics-google)
- [由 GitHub Actions、Pages 和 Jekyll 提供支持的 Jupyter Notebook 博客平台](https://github.com/fastai/fastpages)
- [Deploy A Static Site to GitHub Pages](https://github.com/appleboy/gh-pages-action) - 部署到自定义目录并忽略文件夹/文件。
- [使用高级设置部署到 GitHub Pages](https://github.com/crazy-max/ghaction-github-pages)

### 通知和消息

- [发送不和谐通知](https://github.com/Ilshidur/action-discord)
- [作为机器人发布 Slack 消息](https://github.com/pullreminders/slack-action)
- [使用 Nexmo 从 GitHub Actions 发送短信](https://github.com/nexmo-community/nexmo-sms-action)
- [使用 Clockworksms 从 GitHub Actions 发送短信](https://github.com/bharathvaj1995/clockwork-sms-action)
- [发送电报消息](https://github.com/appleboy/telegram-action)
- [发送文件或短信至 Discord（自定义颜色、用户名或头像）](https://github.com/appleboy/discord-action)
- [使用拉取请求协作处理推文](https://github.com/gr2m/twitter-together)
- [通过 Techulus 的 Push 发送推送通知](https://github.com/techulus/push-github-action)
- [使用 SendGrid 发送电子邮件](https://github.com/peter-evans/sendgrid-action)
- [通过加入发送推送通知](https://github.com/ShaunLWM/action-join)
- [npm 的新包版本检查器](https://github.com/MeilCli/npm-update-check-action)
- [NuGet 的新包版本检查器](https://github.com/MeilCli/nuget-update-check-action)
- [Gradle 的新包版本检查器](https://github.com/MeilCli/gradle-update-check-action)
- [通过 Pushbullet 发送推送通知](https://github.com/ShaunLWM/action-pushbullet)
- [使用 Microsoft Graph 创建 Outlook 日历事件](https://github.com/anoopt/ms-graph-create-event)
- [关注 GitHub Wiki 页面更改并发布到 Slack](https://github.com/benmatselby/gollum-page-watcher-action)
- [使用 MessageBird 发送短信](https://github.com/nikitasavinov/messagebird-sms-action)
- [回复过时的机器人](https://github.com/c-hive/fresh-bot)
- [发送嵌入消息至 Discord](https://github.com/sarisia/actions-status-discord)
- [让您的 PR 与团队合作任务保持同步](https://github.com/Teamwork/github-sync)
- [发送 Microsoft Teams 通知](https://github.com/opsless/ms-teams-github-actions)

### 部署

- [部署到 Netlify](https://github.com/netlify/actions)
- [使用操作部署 Probot 应用程序](https://probot.github.io/docs/deployment/#github-actions)
- [将播放列表部署到 Spotify](https://github.com/swinton/SpotHub)
- [使用 vsce 部署 VS Code 扩展](https://github.com/lannonbr/vsce-action)
- [更新网站后清除 Cloudflare 缓存](https://github.com/jakejarvis/cloudflare-purge-action)
- [使用 DNS 控制部署 DNS 配置](https://github.com/koenrh/dnscontrol-action)
- [将主题部署到 Shopify](https://github.com/pgrimaud/action-shopify)
- [触发多个 GitLab CI Pipeline](https://github.com/appleboy/gitlab-ci-action)
- [触发多个 Jenkins 作业](https://github.com/appleboy/jenkins-action)
- [Homebrew Tap 的 GitHub Action](https://github.com/izumin5210/action-homebrew-tap)
- [通过 SSH 复制文件和工件](https://github.com/appleboy/scp-action)
- [执行远程 ssh 命令](https://github.com/appleboy/ssh-action)
- [将 Python 发行包发布到 PyPI](https://github.com/pypa/gh-action-pypi-publish)
- [将静态网站部署到 Azure 存储](https://github.com/feeloor/azure-static-website-deploy)
- [用于构建和发布包的跨平台 Chocolatey CLI](https://github.com/crazy-max/ghaction-chocolatey)
- [将 iOS Pod 库部署到 Cocoapods](https://github.com/michaelhenry/deploy-to-cocoapods-github-action)
- [腾讯云无服务器的 GitHub Action](https://github.com/Juliiii/action-scf)
- [发布 npm（预）版本](https://github.com/epeli/npm-release/)
- [将静态站点部署到 Surge.sh](https://github.com/yavisht/deploy-via-surge.sh-github-action-template)
- [GoReleaser 的 GitHub Action，Go 项目的发布自动化工具](https://github.com/goreleaser/goreleaser-action)
- [FTP 部署操作，使用 GitHub 操作将 GitHub 项目部署到 FTP 服务器](https://github.com/SamKirkland/FTP-Deploy-Action)
- [发布文章到Dev.to](https://github.com/tylerauerbeck/publish-to-dev.to-action)
- [语义发布行动](https://github.com/cycjimmy/semantic-release-action)
- [将集合部署到 Ansible Galaxy](https://github.com/artis3n/ansible_galaxy_collection)
- [将模块发布到 Puppet Forge](https://github.com/barnumbirr/action-forge-publish)
- [构建和发布 Electron 应用程序](https://github.com/samuelmeuli/action-electron-builder)
- [发布 Maven 包](https://github.com/samuelmeuli/action-maven-publish)
- [构建主题并将其部署到 Ghost CMS](https://github.com/TryGhost/action-deploy-theme)
- [将 Ansible 角色部署到 Ansible Galaxy](https://github.com/robertdebock/galaxy-action)
- [将一个或多个 JS 模块发布到注册表](https://github.com/author/action-publish)
- [使用 Slack 通过 2FA 发布包](https://github.com/erezrokah/2fa-with-slack-action)
- [在持续部署管道中序列化工作流运行](https://github.com/softprops/turnstyle)
- [Netlify 为每个提交部署 GitHub 操作](https://github.com/nwtgck/actions-netlify)
- [运行 Ansible Playbook](https://github.com/arillso/action.playbook)
- [将 Python 分发包发布到 Anaconda Cloud](https://github.com/fcakyon/conda-publish-action)
- [将 VS Code 扩展部署到 Visual Studio Marketplace 或 Open VSX 注册表](https://github.com/HaaLeo/publish-vscode-extension)
- [将 YouTube 视频部署到 Anchor.fm 播客](https://github.com/Schrodinger-Hat/youtube-to-anchorfm)
- [使用 AWS CodeDeploy 进行部署](https://github.com/webfactory/create-aws-codedeploy-deployment)

#### 码头工人

- [从 README.md 更新 Docker Hub 存储库描述](https://github.com/peter-evans/dockerhub-description)
- [将 Docker 映像发布到 GitHub 包注册表 (GPR)](https://github.com/machine-learning-apps/gpr-docker-publish)
- [在 Docker Hub 上更新存储库的“完整描述”](https://github.com/mpepping/github-actions/tree/master/docker-hub-metadata)
- [使用 Kaniko 构建 docker 镜像并将其发布到任何注册表](https://github.com/outillage/kaniko-action)
- [监控并限制您的 docker 镜像大小](https://github.com/wemake-services/docker-image-size-limit)
- [将 Docker 映像发布到 Amazon Elastic Container Registry (ECR)](https://github.com/appleboy/docker-ecr-action)
- [构建并推送 Docker 镜像缓存每个阶段以减少构建时间](https://github.com/whoan/docker-build-with-cache-action)
- [设置 Docker Buildx](https://github.com/crazy-max/ghaction-docker-buildx)
- [将分支或标签名称转换为 Docker 兼容的镜像标签](https://github.com/ankitvgupta/ref-to-tag-action/)
- [Update a Container Repository Description From README.md](https://github.com/marketplace/actions/update-container-description-action) - 支持的注册中心：Docker Hub、Quay、Harbor。

#### 库伯内斯

- [使用 Pulumi 部署到任何云或 Kubernetes](https://github.com/pulumi/actions)
- [使用 kubectl 部署到 Kubernetes](https://github.com/steebchen/kubectl)
- [从 Google Kubernetes Engine (GKE) 获取 Kubeconfig 文件](https://github.com/machine-learning-apps/gke-kubeconfig)
- [Kustomize Kubernetes 配置 YAML](https://github.com/karancode/kustomize-github-action)
- [使用 Krucible 创建 Kubernetes 集群进行测试](https://github.com/Krucible/krucible-github-action)

#### AWS

- [将目录同步/上传到 AWS S3 存储桶](https://github.com/jakejarvis/s3-sync-action)
- [将 Lambda 代码部署到现有函数](https://github.com/appleboy/lambda-action)

#### 地形

- [Generate terraform documentation](https://github.com/Dirrk/terraform-docs) - 使用 terraform-docs 为 terraform 模块生成文档。
- [使用 Terraform 验证和应用 GitHub 管理的示例](https://github.com/asgharlabs/github-terraform/tree/master/.github/workflows)

### 外部服务

- [使用 Jenkinsfile](https://github.com/jonico/jenkinsfile-runner-github-actions)
- [Firebase 的 GitHub 操作](https://github.com/w9jds/firebase-action)
- [内容迁移 CLI 的 GitHub Action](https://github.com/Shy/contentful-action)
- [Pixela 的 GitHub Actions (a-know/pi)](https://github.com/peaceiris/actions-pixela)
- [适用于 Google 云平台 (GCP) 的 GitHub Action](https://github.com/exelban/gcloud)
- [将文件上传到任何 OpenStack Swift 服务提供商](https://github.com/iksaku/openstack-swift-action)
- [用于将 Stack Overflow 帖子发送到 Slack 的 GitHub Action](https://github.com/logankilpatrick/StackOverflowBot)
- [承担 AWS 角色](https://github.com/nordcloud/aws-assume-role/)
- [使用 JSONbin 生成自定义响应](https://github.com/fabasoad/jsonbin-action)

### 前端工具

- [执行Gradle任务](https://github.com/MrRamych/gradle-actions)
- [JS Build Actions](https://github.com/elstudio/actions-js-build) - 运行 Grunt 或 Gulp 构建任务并提交文件更改。
- [Gatsby CLI 的 GitHub 操作](https://github.com/jzweifel/gatsby-cli-github-action)
- [运行 WebPageTest 审核并将结果打印为提交注释](https://github.com/JCofman/webPagetestAction)
- [Hugo 的 GitHub Actions 扩展](https://github.com/peaceiris/actions-hugo)
- [Generate OG Image](https://github.com/BoyWithSilverWings/generate-og-image) - 从 Markdown 文件生成可定制的开放图形图像。
- [mdBook 的 GitHub 操作](https://github.com/peaceiris/actions-mdbook)
- [Setup Mint](https://github.com/fabasoad/setup-mint-action) - 安装Mint（用于编写单页应用程序的编程语言）。
- [Gatsby AWS S3 Deployment](https://github.com/jonelantha/gatsby-s3-action) - 将 Gatsby 部署到 S3（支持 CloudFront）。

### 机器学习操作

- [提交 Argo 工作流程（与云无关）](https://github.com/machine-learning-apps/actions-argo)
- [向 GKE 提交 Argo 工作流程](https://github.com/machine-learning-apps/gke-argo)
- [根据权重和偏差查询实验跟踪结果](https://github.com/machine-learning-apps/wandb-action)
- [运行参数化 Jupyter Notebook](https://github.com/yaananth/run-notebook)
- [编译、部署和运行 Kubeflow Pipeline](https://github.com/NikeNano/kubeflow-github-action)
- [自动将数据科学存储库 Docker 化为 Jupyter 服务器](https://github.com/jupyterhub/repo2docker-action)
- [使用 GitHub Actions 进行 Azure 机器学习](https://github.com/machine-learning-apps/ml-template-azure)

### 构建

- [run-cmake](https://github.com/lukka/run-cmake) - 使用 [CMake](https://cmake.org) 和 [Ninja](https://ninja-build.org/) 构建 C/C++ 软件的多平台操作。
- [run-vcpkg](https://github.com/lukka/run-vcpkg) - 使用 [vcpkg](https://github.com/microsoft/vcpkg) 构建和安装 C/C++ 依赖项的多平台操作。
- [为多平台构建 Go 应用程序](https://github.com/izumin5210/action-go-crossbuild)
- [为 Maven 构建生成 ~/.m2/settings.xml](https://github.com/whelk-io/maven-settings-xml-action)
- [运行 Pascal 脚本](https://github.com/fabasoad/pascal-action)
- [Setup Brainfuck](https://github.com/fabasoad/setup-brainfuck-action) - 设置 Brainfuck 解释器。
- [将 Go 二进制文件发布到 GitHub 发布资产](https://github.com/wangyoucao577/go-release-action)
- [设置 COBOL](https://github.com/fabasoad/setup-cobol-action)
- [Check Gradle version](https://github.com/madhead/check-gradle-version) - 使您的 Gradle 版本保持最新。

### 数据库

- [Setup Cassandra Schema](https://github.com/fabasoad/setup-cassandra-action) - 从 Cassandra 集群顶部提供的文件夹运行脚本。

### 网络

- [Setup ZeroTier](https://github.com/zerotier/github-action) - 将您的跑步者连接到 ZeroTier 网络。

### 本地化

- [查找并自动修复代码中的拼写错误和语法问题](https://github.com/sobolevn/misspell-fixer-action)
- [Translation](https://github.com/fabasoad/translation-action) - 将文本从任何语言翻译成任何语言。

### 乐趣

- [Add equivalent of a like button in your README](https://github.com/ariary/Readme-Like-Button) - 可视化社区对自述文件某些部分的批准（可以用作民意调查）。

### 备忘单

- [GitHub Actions 品牌备忘单](https://haya14busa.github.io/github-action-brandings/)

## 教程

- [使用 Up 持续部署 Next.js 应用程序](https://medium.com/@romanenko/simple-ci-for-next-js-projects-with-apex-up-github-actions-6f0b1b9a5400)
- [将基于 Docker 的操作转换为 JavaScript/TypeScript](https://httgp.com/converting-github-actions-from-docker-to-javascript/)
- [适用于 Swift/iOS 项目的 GitHub Actions CI](https://medium.com/rosberryapps/github-actions-ci-for-swift-projects-c129baceed1a)
- [使用 GitHub 操作](https://jeffrafter.com/working-with-github-actions)
- [面向 Rails 开发人员的 GitHub Actions](https://www.youtube.com/watch?v=gGUXydw22zw)
- [GitHub Actions 降临节日历](https://www.edwardthomson.com/blog/github_actions_advent_calendar.html)
- [使用 GitHub Actions 实现零停机 Laravel 部署](https://atymic.dev/blog/github-actions-laravel-ci-cd/)
- [构建自定义 GitHub Actions Pluralsight 课程](https://www.pluralsight.com/courses/building-custom-github-actions/)
- [使用 Docker 和 GitHub Actions 持续将 Django 部署到 DigitalOcean](https://testdriven.io/blog/deploying-django-to-digitalocean-with-docker-and-github-actions/)
- [Deploying Self-Hosted GitHub Actions Runners with Docker](https://testdriven.io/blog/github-actions-docker/) - 使用 Docker 和 Docker Swarm 将自托管 GitHub Actions 运行器部署到 DigitalOcean。
- [在 AWS Spot 实例上设置自动缩放的自托管 GitHub Actions Runners](https://040code.github.io/2020/05/25/scaling-selfhosted-action-runners)
- [了解 GitHub Actions 的要点](https://gist.github.com/br3ndonland/f9c753eb27381f97336aa21b8d932be6)

> 如果您有更多资源可以分享，请随时发布 PR。查看 [contributing.md](contributing.md) 了解更多信息。
