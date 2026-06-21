<!--lint disable double-link awesome-toc-->
# 很棒的作曲家 [![Awesome](https://awesome.re/badge-flat.svg)](https://github.com/sindresorhus/awesome)

[<img src="https://raw.githubusercontent.com/jakoch/awesome-composer/master/logo-composer-transparent.png"align="right" width="150">](https://getcomposer.org/)

> Composer、Packagist、Satis、插件、脚本、视频、教程的精选资源列表。

您可能还喜欢 [awesome-php](https://github.com/ziadoz/awesome-php)。

*请在贡献之前阅读[贡献指南](https://github.com/jakoch/awesome-composer/blob/main/.github/CONTRIBUTING.md)。*

## 作曲家

- [官方网站](https://getcomposer.org/)
- [GitHub](https://github.com/composer/composer)
- [Issues](https://github.com/composer/composer/issues)
- [Source](https://github.com/composer/composer/tree/HEAD/src/Composer)
- [Documentation](https://getcomposer.org/doc/)
- [入门指南和安装说明](https://getcomposer.org/doc/00-intro.md)
- [在 Packagist 上查找软件包](https://packagist.org/)
- [CheatSheet](https://composer.json.jolicode.com/) - CLI 命令和“composer.json”架构概述。
- [Composer Installers](https://github.com/composer/installers) - 多个框架的 Composer 安装程序。

### 支持

#### 堆栈溢出

- 您可以使用以下标签：`composer-php`、`packagist`、`satis` + `php`。
- [问一个新问题](https://stackoverflow.com/questions/ask?tags=composer-php+php)
- [查找标记为“composer-php”的问题](https://stackoverflow.com/questions/tagged/composer-php)

#### IRC

- IRC 频道位于 `irc.freenode.org` 上：[#composer](https://irc.com/#composer) 用于用户，[#composer-dev](https://irc.com/#composer-dev) 用于开发。

---

## 插件

- [Documentation for Plugins](https://getcomposer.org/doc/articles/plugins.md) - 在编写 Composer 插件时，这个官方文档是一个很好的起点。
- [Composer-Asset-Plugin](https://github.com/fxpio/composer-asset-plugin) - Composer 的 npm/Bower 依赖关系管理器。
- [Composer-AWS](https://github.com/naderman/composer-aws) - 该插件加载存储库数据并从 Amazon S3 下载包（支持私有存储库的身份验证）。
- [Composer-Composition](https://github.com/bamarni/composition) - 提供 API，用于在运行时检查您的环境。
- [Composer-Suggest](https://github.com/nfreear/composer-suggest) - 使您能够根据关键字模式安装一组自定义的建议包。
- [Composer-Versions-Check](https://github.com/Soullivaneuh/composer-versions-check) - 使用更新命令后显示最新主要版本的过时软件包（显示“最新版本是 vX.Y.Z”）。
- [Composer-Changelogs](https://github.com/pyrech/composer-changelogs) - 提供更新摘要以及更改日志/发行说明/标签的链接。更新composer.lock 文件时，输出已准备好粘贴到提交消息中。
- [Composer-Merge-Plugin](https://github.com/wikimedia/composer-merge-plugin) - 在 Composer 运行时合并多个“composer.json”文件。
- [Composer-Bin-Plugin](https://github.com/bamarni/composer-bin-plugin) - 添加了对管理单个存储库中多个包的依赖关系或隔离 bin 依赖关系的支持。
- [Composer-Inheritance-Plugin](https://github.com/theofidry/composer-inheritance-plugin) - Wikimediacomposer-merge-plugin 的自定版本可与 Bamarnicomposer-bin-plugin 配合使用。
- [Composer-MonoRepo-Plugin](https://github.com/beberlei/composer-monorepo-plugin) - 该插件有助于管理单个存储库中多个包的依赖关系。
- [Composer-Patches-Plugin](https://github.com/netresearch/composer-patches-plugin) - 使您能够为任何包中的任何包提供补丁。当获取依赖项时，补丁将应用到顶部。
- [Composer-Patches](https://github.com/cweagans/composer-patches) - 该插件将本地或远程文件中的补丁应用于任何所需的包。
- [Composer-Patches](https://github.com/vaimo/composer-patches) - 将本地或远程文件中的补丁应用到属于给定 Composer 项目的任何包。
- [Composer-Patchset](https://github.com/mageops/php-composer-plugin-patchset) - 自动获取、更新补丁并将其应用到任何 Composer 包 - 将补丁集存储为 Composer 包本身。
- [Composer-Plugin-QA](https://github.com/Webysther/composer-plugin-qa) - 供作曲家执行 PHP 质量保证工具的综合插件。
- [Composer-Cleanup-Plugin](https://github.com/barryvdh/composer-cleanup-plugin) - 从供应商目录中删除测试和文档文件夹。
- [Composer-Cleaner](https://github.com/dg/composer-cleaner) - 该工具从供应商目录中删除不必要的文件和目录。
- [Composer-Ignore-Plugin](https://github.com/lichunqiang/composer-ignore-plugin) - 使您能够从供应商文件夹中删除文件和文件夹（以进行更干净、更小的生产部署）。它是 `.gitattributes` 的替代品。
- [Composer-Vendor-Cleaner](https://github.com/liborm85/composer-vendor-cleaner) - 插件通过 glob 模式语法从 `vendor` 目录中删除不必要的开发文件和目录。
- [Composer-Skrub](https://github.com/ssx/skrub) - 该插件有助于从 Composer 安装中删除垃圾并修剪构建大小。
- [Drupal Vendor Hardening Composer Plugin](https://github.com/drupal/core-vendor-hardening) - 从项目的供应商目录中删除无关的目录，并将 .htaccess 和 web.config 文件添加到项目供应商目录的根目录中。
- [Composer-Shared-Package-Plugin](https://github.com/Letudiant/composer-shared-package-plugin) - 允许您通过创建符号链接在项目之间共享选定的包。
- [Composer-Symlinker](https://github.com/e-picas/composer-symlinker) - 使您能够从不同的目录加载包（而不是从 /vendor 加载它们）。
- [Prestissimo](https://github.com/hirak/prestissimo) - 使用“phpext_curl”的并行下载器。
- [Composer-Curl-Plugin](https://github.com/ngyuki/composer-curl-plugin) - 该插件使用“phpext_curl”来下载包。
- [Composer-Custom-Directory-Installer](https://github.com/mnsami/composer-custom-directory-installer) - 一个 Composer 插件，用于在默认 Composer 安装路径（供应商文件夹）之外的自定义目录中安装不同类型的 Composer 包。
- [Composer-Dependency-Analyzer](https://github.com/shipmonk-rnd/composer-dependency-analyser) - 该插件有助于发现依赖关系问题，包括死的、未使用的、影子的和错位的依赖关系。
- [Composer-Dependency-Analyzer](https://packagist.org/packages/jms/composer-deps-analyzer) - 允许您为已安装的 Composer 项目构建依赖关系图。
- [Graph-Composer](https://github.com/clue/graph-composer) - 为项目的“composer.json”及其依赖项提供图形可视化。
- [PackageVersions](https://github.com/Ocramius/PackageVersions) - 提供对已安装的 Composer 依赖项版本的非常快速且轻松的访问。
- [PackageVersions Deprecated](https://github.com/composer/package-versions-deprecated) - 是 Ocramius/PackageVersions 的一个分支，提供与 PHP 7+ 上的 Composer 1 和 2 的兼容性。
- [Composer-Locator](https://github.com/mindplay-dk/composer-locator) - 提供一种查找给定 Composer 包名称的安装路径的方法。
- [PackageInfo](https://github.com/ThaDafinser/PackageInfo) - 使您能够检索所有包信息（如版本、标签、发布日期、描述）。
- [Composer-Git-Hooks](https://github.com/BrainMaestro/composer-git-hooks) - 一个用于轻松管理 Composer 配置中的 git hook 的库。
- [Symfony-Flex](https://github.com/symfony/flex) - 为 Symfony 包提供[基于配方](https://github.com/symfony/recipes)的安装和配置管理。
- [Narrowspark-Automatic](https://github.com/narrowspark/automatic) - 自动执行应用程序最常见的任务，增加软件包下载，添加作曲家安全审核等等。
- [PHPCodeSniffer-Composer-Installer](https://github.com/PHPCSStandards/composer-installer) - 该插件使您能够安装 [PHP_CodeSniffer](https://github.com/squizlabs/PHP_CodeSniffer) 编码标准（规则集）。
- [Composer-Warmup](https://github.com/jderusse/composer-warmup) - 该插件将命令“warmup-opcode”添加到 Composer，这会触发将项目中发现的所有 PHP 文件编译到 Opcache 中。
- [Foxy](https://github.com/fxpio/foxy) - 当安装或更新 Composer 包时，执行 npm/yarn 包安装操作的 Composer 插件。
- [NodeJS-Installer](https://github.com/thecodingmachine/nodejs-installer) - Node.js 和 npm 的安装程序。
- [Node-Composer](https://github.com/mariusbuescher/node-composer) - Node.js、npm 和yarn 的安装程序。
- [Imposter-Plugin](https://github.com/typisttech/imposter-plugin) - 将所有 Composer 供应商包包装在您自己的命名空间内。适用于 WordPress 插件。
- [Composer Preload](https://github.com/Ayesh/Composer-Preload) - 该插件生成一个“vendor/preload.php”文件来预热 Opcache。
- [PHP Inc](https://github.com/krakphp/php-inc) - 自动包含用于 autoload 和 autoload-dev 的文件，以方便在 Composer 加载的应用程序中使用函数和分组定义。
- [Composer Registry Manager](https://github.com/slince/composer-registry-manager) - 使您能够在不同的作曲家存储库之间切换。
- [Production-Dependencies-Guard](https://github.com/kalessil/production-dependencies-guard) - 防止开发包被添加到需求中并进入生产环境。
- [Composer-Plugin-Exclude-Files](https://github.com/mcaskill/composer-plugin-exclude-files) - 一个使用“文件”自动加载机制排除包所需文件的插件。
- [Composer-Downloads-Plugin](https://github.com/civicrm/composer-downloads-plugin) - 仅使用“url”和“path”下载外部资源（ZI​​P/TAR 文件）的轻量级机制。
- [Private-Composer-Installer](https://github.com/ffraenz/private-composer-installer) - 将包 URL 中的帮助程序外包敏感密钥安装到环境变量中。
- [CycloneDX-PHP-Composer](https://github.com/CycloneDX/cyclonedx-php-composer) - 为项目的依赖项创建 [CycloneDX](https://cyclonedx.org/)“软件物料清单”(SBOM)。 SBOM 通过 [OWASP DependencyTrack](https://dependencytrack.org/) 实现依赖性监控和风险分析。
- [Composer-Compile-Plugin](https://github.com/civicrm/composer-compile-plugin) - 允许 PHP 库定义简单、自由格式的编译任务。支持任何包中的安装后挂钩。
- [Composer-Link](https://github.com/SanderSander/composer-link) - 添加链接本地包进行开发的能力。
- [Composer-REPL](https://github.com/ramsey/composer-repl) - 该插件提供了“composer repl”命令，它为您提供了一个 PHP 语言 shell（读取-评估-打印循环）。
- [Composer-Diff](https://github.com/IonBazan/composer-diff) - 比较“composer.lock”更改并生成 Markdown 报告以在拉取请求描述中使用。
- [Composer-Velocita](https://github.com/isaaceindhoven/composer-velocita) - 使用 [Velocita](https://github.com/isaaceindhoven/velocita-proxy) 快速可靠地下载 Composer 包：一种缓存反向代理，不需要您修改项目。
- [Composer Translation Validator](https://github.com/move-elevator/composer-translation-validator) - 验证项目中的翻译文件，支持多种文件格式（关于不同的框架）并提供有用的验证器来进行比较、一致性和语法检查。

## 工具

- [Composer SemVer Checker](https://semver.madewithlove.com/) - 使您能够通过对 Packagist 托管的软件包进行语义版本检查来识别版本解析问题的约束。
- [Composer-Yaml](https://github.com/igorw/composer-yaml) - 该工具将 `composer.yml` 转换为 `composer.json`。
- [Studio](https://github.com/franzliedke/studio) - 用于开发 Composer 包的工作台。它是编辑供应商文件夹中的依赖项或使用 [PathRepositories](https://getcomposer.org/doc/05-repositories.md#path) 将依赖项的本地克隆加载到项目中的替代方法。
- [OctoLinker Browser Extension](https://github.com/OctoLinker/OctoLinker) - 使您能够在 GitHub 上导航 Composer/NPM 依赖项。
- [ComposerRequireChecker](https://github.com/maglnet/ComposerRequireChecker) - 一个 CLI 工具，用于分析依赖关系并验证包的源中没有使用未知的导入符号。
- [Composer-Unused](https://github.com/composer-unused/composer-unused) - 一个 CLI 工具，它扫描您的代码并显示未使用的 Composer 依赖项。
- [Composer-Normalize](https://github.com/ergebnis/composer-normalize) - 该插件通过重组和排序条目（规范化）帮助您保持“composer.json”文件的一致性。
- [Composer-Service](https://github.com/pborreli/composer-service) - 使您能够将 Composer 作为远程服务器上的服务运行。
- [Composer PreferLowest Checker](https://github.com/dereuromark/composer-prefer-lowest) - 严格将composer.json指定的最低版本与prefer-lowestcomposer update命令选项实际使用的版本进行比较。
- [Bramus/Composer-Autocomplete](https://github.com/bramus/composer-autocomplete) - Composer 的 Bash/Shell 自动完成脚本。
- [Composer/Xdebug-Handler](https://github.com/composer/xdebug-handler) - 帮助您在不加载 xdebug 扩展的情况下重新启动 CLI 进程。
- [Composer Semver Range Checker](https://gitlab.com/MattyRad/composer.guru) - 帮助检查作曲家约束的可满足范围的工具。

## 脚本

- [ParameterHandler](https://github.com/Incenteev/ParameterHandler) - 允许您在运行 Composer 安装或更新时管理忽略的参数。
- [Tooly](https://github.com/tommy-muehle/tooly-composer-script) - 管理项目“composer.json”中所需的 PHAR 文件。每个 PHAR 文件都将保存在 Composer 二进制目录中。每个 PHAR 可选择进行 GPG 验证。
- [Melody](https://github.com/sensiolabs/melody) - 单文件编写器脚本。
- [Composer-Travis-Lint](https://github.com/raphaelstolt/composer-travis-lint) - 允许您检查 Travis CI 配置文件 (`.travis.yml`)。
- [Composer-Multitest](https://github.com/raphaelstolt/composer-multitest) - 使您能够针对多个本地安装的 PHP 版本运行 Composer 脚本，这些版本由 PHPBrew 或 phpenv 管理。
- [ScriptsDev](https://github.com/neronmoon/scriptsdev) - 使您能够使用“scripts-dev”部分，该部分仅在开发模式下触发脚本。
- [PhantomJS-Installer](https://github.com/jakoch/phantomjs-installer) - 一个 Composer 包，它将 PhantomJS 二进制文件（Linux、Windows、Mac）安装到项目的 /bin 中。
- [Composer-Vendor-Cleanup](https://github.com/0xch/composer-vendor-cleanup) - 从供应商目录中删除列入白名单的不必要文件（如测试/文档等）的脚本。
- [Composer-Substitution-Plugin](https://github.com/villfa/composer-substitution-plugin) - Composer 插件用动态值替换“脚本”部分中的占位符。

## 服务

- [Dependabot](https://github.com/security/advanced-security) - Dependabot 是一项依赖项更新服务。它通过发送拉取请求来监视和更新您的依赖项。该服务对于公共回购和个人账户回购都是免费的。

---

## 教程

- [Composer 初学者指南](https://www.digitalocean.com/community/tutorials/a-beginners-guide-to-composer)
- [简短而简单的 Composer 教程](https://www.dev-metal.com/composer-tutorial/)
- [使用 Composer 轻松管理包](https://code.tutsplus.com/easy-package-management-with-composer--net-25530t)
- [使用 Composer 进行 PHP 依赖管理](https://www.sitepoint.com/re-introducing-composer/)
- [作曲家入门](https://daylerees.com/composer-primer/)
- [PHP Composer Magento 教程，作者：Alan Storm](https://alanastorm.com/php_composer_magento_tutorial/)
- [创建和使用 Composer 包](https://www.packtpub.com/en-us/learning/how-to-tutorials/creating-and-using-composer-packages/)

## 博客

- [霍尔迪·博贾诺（塞尔达克）](https://seld.be/)
- [尼尔斯·阿德曼（纳德曼）](https://naderman.de/)
- [作曲家稳定性标志](https://igor.io/2013/02/07/composer-stability-flags.html)
- [作曲家版本控制](https://igor.io/2013/01/07/composer-versioning.html)
- [使 PHP Composer 内存高效且快速的漫长旅程 (toflar)](https://medium.com/@yanick.witschi/the-long-journey-of-making-phps-composer-memory-efficient-and-fast-63d12944aaa8)

## 视频

- [作曲家最佳实践 2018 - Nils Adermann @ scotphp18](https://www.youtube.com/watch?v=eQkFjMfyqFY)
- [作曲家最佳实践 2018 - Nils Adermann @ phpday 2018](https://www.youtube.com/watch?v=EpvihKaQyLs)
- [管理依赖关系不仅仅是运行“composer update” - Nils Adermann @ phpsrb17](https://www.youtube.com/watch?v=QL6w8H2eHQE)
- [作曲家最佳实践 — Jordi Boggiano @ phptek 2015](https://www.youtube.com/watch?v=uNlYpSTiAcA)
- [奇妙的作曲家世界](https://symfonycasts.com/screencast/composer)
- [PHP 作曲家快速入门](https://www.youtube.com/watch?v=Ejr4Xqs9V2I)
- [Composer 如何帮助塑造新的 PHP 编写方式 - Nils Adermann @ Drupal Camp 法兰克福](https://www.youtube.com/watch?v=C2jfLM-Egvg)
- [Composer 包管理 - Nils Adermann @ T3CON12DE](https://www.youtube.com/watch?v=P4Qnp90TG0g)
- [Composer 2 - Jordi Boggiano @ Symfony UK 用户组 2020](https://www.youtube.com/watch?v=BAgwWhRo82w)
- [构建 Composer 内部结构的经验教训 - Jordi Boggiano @ CODEiD Odessa PHP Conference 2017](https://www.youtube.com/watch?v=pjvbn6TBZqM)

## 幻灯片

- 尼尔斯·阿德曼 (Nils Adermann) 的幻灯片
- 来源：https://naderman.de/slippy/src/
  - [PHP 重塑 - Composer 如何帮助塑造 PHP 编写新方式](https://naderman.de/slippy/src/?file=2014-04-13-PHP-Reinvented.html)
  - [作曲家更新](https://naderman.de/slippy/src/?file=2015-02-03-Composer-Update.html)
  - [重新设计 Composer PHP 的依赖管理](https://naderman.de/slippy/src/?file=2015-02-01-Dependency-Management-with-Composer-PHP-Reinvented.html)
- [管理依赖关系是
不仅仅是跑步
“作曲家更新”](https://naderman.de/slippy/slides/2017-06-30-DPC-Dependency-Management-is-more-than-composer-update.pdf)
- [作曲家
最佳实践@ T3DD17](https://naderman.de/slippy/slides/2017-07-13-T3DD17-Composer-Best-Practices.pdf)
- [控制你的
依赖关系
私人Packagist](https://naderman.de/slippy/slides/2017-07-14-T3DD17-Gain-control-over-your-dependency-with-private-packagist.pdf)
  - [Composer.lock 揭秘](https://naderman.de/slippy/slides/2018-01-26-composer-lock-demystified.pdf)
  - [Compoer 深度报道 @ Contao Konferenz 2018](https://naderman.de/slippy/slides/2018-06-08-Contao-Konferenz-2018-Composer-In-Depth.pdf)
  - [2018 年作曲家最佳实践](https://naderman.de/slippy/slides/2018-06-27-Composer-Best-Practices-2018.pdf)
  - [使用 Composer 最佳实践开发和部署 Magento](https://naderman.de/slippy/slides/2018-06-18-Developing-and-Deploying-Magento-with-Composer-Best-Practices.pdf)
  - [Composer 平台配置 (check-platform-reqs) @ SymfonCon 2018](https://naderman.de/slippy/slides/2018-12-07-SymfonCon-Composer-Platform-Config.pdf)
- Jordi Boggiano 的幻灯片
- 来源：http://slides.seld.be/
  - [使用 Composer 进行依赖管理 (2013)](http://slides.seld.be/?file=2013-10-04+Dependency+Management+with+Composer.html)
  - [深入作曲家 (2013)](http://slides.seld.be/?file=2013-10-05+In-Depth+with+Composer.html)
  - [作曲家最佳实践 (2015)](http://slides.seld.be/?file=2015-07-25+Composer+Best+Practices.html)
  - [作曲家简介 (2015)](http://slides.seld.be/?file=2015-06-30+Introduction+to+Composer.html)
  - [2016年作曲家](http://slides.seld.be/?file=2016-07-22+Composer+in+2016.html)
  - [构建 Composer 内部结构的经验教训 (2018)](http://slides.seld.be/?file=2018-04-20+Lessons+Learned+Building+the+Composer+Internals.html)

---

## 包装学家

[Packagist](https://packagist.org) 是 PHP 包存储库。

### 设置 Packagist 镜像

- [Packagist Mirror](https://github.com/Webysther/packagist-mirror) - 此脚本有助于设置 Packagist 镜像。它是 [Packagist Crawler](https://github.com/hirak/packagist-crawler) 的维护稳定版本。
- [Docker Image](https://github.com/Webysther/packagist-mirror-docker) - 此 Docker 映像有助于创建自定义的 Packagist 镜像。
- [Packagist Mirror from Indonesia](https://github.com/IndraGunawan/packagist-mirror) - 创建 Packagist 镜像的另一个实现。

### 包装镜

关于元数据镜像：https://packagist.org/mirrors

- 全球、CloudFlare - [packagist.pages.dev](https://packagist.pages.dev/)
- 北美
- 加拿大 - [packagist.org](https://packagist.org) *主镜像*
- 非洲
- 南非 - [packagist.co.za](https://packagist.co.za)
- 亚洲
- 中国 - [https://pkg.xyz/](https://pkg.xyz/)、[https://developer.aliyun.com/composer](https://developer.aliyun.com/composer)
- 印度 - [https://packagist.in/](https://packagist.in/)
- 日本 - [packagist.jp](https://packagist.jp)
- 韩国 - [https://packagist.kr/](https://packagist.kr/)

## 作曲家存储库

### 注册经理
- https://github.com/slince/composer-registry-manager - 该插件可以帮助您在不同的作曲家存储库之间切换。

### 私有存储库
- [fxpio/tug](https://github.com/fxpio/tug) - 使您能够在 AWS Serverless 上托管私有 Composer 注册表，为您的私有 PHP 包提供服务，这些包托管在 GitHub 或 GitLab 服务上。

### 私人包装师
- [Private Packagist Cloud](https://packagist.com) - Composer 存储库即服务，用于私有包以及从其他存储库镜像包。
- [Private Packagist Enterprise](https://packagist.com) - Private Packagist 的本地自托管版本。
- [Private Packagist API Client](https://github.com/packagist/private-packagist-api-client) - Private Packagist API 的 PHP 客户端。客户端处理身份验证、签名生成和对所有端点的访问。

### 雷普曼

- [repman.io](https://repman.io) & [repman-io/repman](https://github.com/repman-io/repman) - 私有 PHP 包存储库管理器和 Packagist 代理。
- [repman-io/composer-plugin](https://github.com/repman-io/composer-plugin) - 该插件可以通过为所有依赖项添加分发镜像 URL 来通过 Repman 下载（无需更新“composer.lock”文件）。

## Packagist 兼容的存储库

- [WordPress Packagist](https://wpackagist.org/) - 将 WordPress 插件和主题目录镜像为 Composer 存储库。
- [Asset Packagist](https://asset-packagist.org/) - 允许将 Bower 和 NPM 软件包安装为本机 Composer 软件包。
- [Firegento](https://packages.firegento.com/) - 提供 Magento 模块的 Composer 存储库。
- [Drupal Packagist](https://www.drupal.org/node/2822344) - Drupal 7 和 8 核心、模块和主题的 Composer 存储库。
- [Satis Server](https://github.com/lukaszlach/satis-server) - 此 docker 容器提供 Satis 服务器，使您能够运行私有、自托管 Composer 存储库，并支持 Git、Mercurial 和 Subversion、HTTP API、HTTPs 支持、webhook 处理程序和计划构建。
- [Cloudsmith](https://cloudsmith.com/) - 完全托管的包管理 SaaS，具有 PHP/Composer 支持（以及许多其他支持）。
- [Release Belt](https://github.com/Rarst/release-belt) - 自托管 Composer 存储库实施，可快速集成第三方非 Composer 版本的 ZIP 文件。
- [Packeton](https://github.com/vtsykun/packeton) - 供供应商使用的私有自托管 Composer 存储库。 Packagist 的分支，添加了对授权、客户用户、组、网络钩子的支持。
- [RepoFlow](https://www.repoflow.io) - 用于托管私有 Composer 注册表的简单快速的平台。还支持 Docker、npm、PyPI、Maven 和 RubyGems。为云和自托管设置提供免费选项。

### 萨蒂斯

- [GitLab-Composer](https://github.com/wemakecustom/gitlab-composer) - 这是 GitLab 存储库的分支/标签索引器。
- [Satisfy](https://github.com/project-satisfy/satisfy) - 具有 Web UI 的 Satis Composer 存储库管理器。
- [Satis Control Panel](https://github.com/realshadow/satis-control-panel) - 一个简单的 Web UI，用于通过可选的 CI 集成来管理您的 Satis 存储库。
- [Satis Go](https://github.com/benschw/satis-go) - 用于管理 Satis 配置并托管生成的 Composer 存储库的 Web 服务器。

### 托兰代理

- [ToranProxy](https://toranproxy.com/)（已弃用） - 除了提供 Composer 存储库之外，ToranProxy 还充当 Packagist 和 GitHub 的代理服务器。

---

## 版权

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

在法律允许的范围内，[Jens A. Koch](https://github.com/jakoch) 已放弃本作品的所有版权以及相关或邻接权。
