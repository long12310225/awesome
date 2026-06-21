<!--lint ignore double-link-->
# 很棒的 WP-CLI [<img src="assets/wp-cli-bw-trans-filled-tight@311x160.png" alt="WP-CLI 徽标"align="right" height="80">](https://wp-cli.org/) [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

<!--lint ignore double-link-->
[WP-CLI](https://wp-cli.org/) 是 WordPress 的命令行界面。它提供了 WordPress 管理仪表板的完整替代方案，通常甚至超越了其功能或支持新的用例。它还附带了丰富的第三方命令生态系统，这些命令捆绑在 Composer 包中或直接集成到 WordPress 插件或主题中。

## 内容

- [官方链接](#official-links)
- [第三方包](#third-party-packages)
	- [包发现](#package-discovery)
	- [著名的包](#notable-packages)
- [教程和指南](#tutorials--guides)
- [Contribute](#contribute)

## 官方链接

直接属于官方 WP-CLI 团队的所有相关内容。

<!--lint ignore double-link-->
- [wp-cli.org](https://wp-cli.org/) - WP-CLI 项目的主页。
- [WP-CLI handbook](https://make.wordpress.org/cli/handbook/) - 有关如何使用或扩展 WP-CLI 的指南。
- [WP-CLI command reference](https://developer.wordpress.org/cli/commands/) - 所有官方 WP-CLI 命令的参考文档。
- [Make WordPress.org - CLI](https://make.wordpress.org/cli/) - 为 WP-CLI 做出贡献的主要入口点。
  - [Contributing guide](https://make.wordpress.org/cli/handbook/contributing/) - 为该工具或其基础设施做出贡献所需了解的一切。
  - [Official MakeWP Slack](https://make.wordpress.org/chat/) - 官方 Slack 团队，讨论对 WordPress 及其团队的所有国际贡献。
    - [#cli channel](http://wordpress.slack.com/messages/cli/) - WP-CLI 和 WordPress CLI 团队的官方支持渠道。
  - [Good first issues](https://make.wordpress.org/cli/good-first-issues/) - 有关问题清单的范围和复杂性有限。
- [WP-CLI GitHub organization](https://github.com/wp-cli) - WP-CLI 源代码的规范主页。
  - [WP-CLI framework repository](https://github.com/wp-cli/wp-cli) - 支持所有命令的 WP-CLI 框架的源代码。
  - [WP-CLI bundle repository](https://github.com/wp-cli/wp-cli-bundle) - WP-CLI“二进制文件”的源代码及其组装方式。
  - [WP-CLI tests repository](https://github.com/wp-cli/wp-cli-tests) - 所有 WP-CLI 存储库中使用的测试框架。

## 第三方包

非官方的第三方软件包。

### 包发现

搜索您可以使用的第三方软件包的方法。

- [Packagist.org search by WP-CLI package type](https://packagist.org/?type=wp-cli-package) - 按类型“wp-cli-package”过滤的 Composer 包。
- [GitHub.com search for WP-CLI integrations](https://github.com/search?q=WP_CLI%3A%3Aadd_command%28+NOT+Akismet_CLI+NOT+elementor+NOT+WordCamp_CLI_Miscellaneous+NOT+W3TotalCache_Command+path%3A*.php+language%3APHP+-org%3Awp-cli+-path%3Avendor+-path%3Awp-content+-path%3Apublic+-path%3Adeployer+-path%3Aweb+-path%3Asrc%2Fvendor+-path%3Aapp+-path%3Awordpress+-path%3Aentity-command.php+-path%3Aclass-wc-cli.php+-path%3Awp-cli-bp.php+NOT+is%3Afork+-path%3Aextension-command.php+-path%3Acron-command.php+-path%3Awp-seo-main.php+-path%3Aplugins+-path%3Adata+-path%3Abackup+-path%3Ademo+-path%3Awordcamp.org+-path%3Awordpress.org+-path%3Alanguage-command.php+-path%3Aredirection-cli.php+-path%3Athemes+-path%3Alibrary+-path%3Aeval-command+-path%3Arole-command+-path%3Awidget-command+-path%3Acache-command.php+-path%3Awp-app+-path%3Apublic_html+-path%3Aqueue.php+-path%3AmyWeb+-path%3Adocroot+-path%3Awebsite&type=code) - 对使用“WP_CLI::add_command()”的存储库进行严格的预过滤搜索。

### 著名的包

常用的第三方包。

- [Yoast/wp-cli-faker](https://github.com/Yoast/wp-cli-faker) - 出于测试目的生成虚假 WordPress 和 WooCommerce 内容。
- [aaemnnosttv/wp-cli-login-command](https://github.com/aaemnnosttv/wp-cli-login-command) - 使用安全的无密码魔术链接登录 WordPress。
- [schlessera/wp-cli-psysh](https://github.com/schlessera/wp-cli-psysh) - 将 WP-CLI shell 标准 REPL 替换为 [PsySH](http://psysh.org/)。
- [php-stubs/wp-cli-stubs](https://github.com/php-stubs/wp-cli-stubs) - 用于静态分析的 WP-CLI 函数和类声明存根。

## 教程和指南

有关如何充分利用 WP-CLI 的网站、电子书、PDF、讲座和幻灯片。

- [An Introduction to WP-CLI](https://pascalbirchler.com/an-introduction-to-wp-cli/) - 介绍性文章，介绍 WP-CLI 的主要概念和一些流行用例。
- [Controlling WordPress through the Command Line](https://wordpress.tv/2017/05/22/alain-schlesser-controlling-wordpress-through-the-command-line-introduction-to-wp-cli/) - 介绍性演讲涵盖了命令行的基础知识，适合以前从未使用过控制台的人。
- [WP Bullet WP-CLI Guides](https://guides.wp-bullet.com/category/wp-cli/) - 基于片段的指南，可解决特定的用例。
- [Siteground Webinar: Learn How WP-CLI Can Make Your Life Easier](https://www.youtube.com/watch?v=DlxbRYpZdQg) - 有关如何使用 WP-CLI 改进工作流程的实际示例。
- [CaptainCore Cookbook](https://captaincore.io/cookbook/) - 用于自动化 WordPress 维护的 WP-CLI 命令和 bash 脚本的集合。

## 贡献

欢迎投稿！首先阅读[贡献指南](contributing.md)。
