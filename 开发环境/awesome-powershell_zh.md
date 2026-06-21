# 很棒的 PowerShell

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome) [![Link Verification](https://github.com/janikvonrotz/awesome-powershell/actions/workflows/markdownLinkDaily.yml/badge.svg)](https://github.com/janikvonrotz/awesome-powershell/actions/workflows/markdownLinkDaily.yml)

令人愉快的 [PowerShell](https://en.wikipedia.org/wiki/PowerShell) 软件包和资源的精选列表。

PowerShell 是一种跨平台（Windows、Linux 和 macOS）自动化和配置工具，针对处理结构化数据（例如 JSON、CSV、XML 等）、REST API 和对象模型进行了优化。
它包括一个命令行 shell 和相关的脚本语言。

## 内容

* [API 包装器](#api-wrapper)
* [Blogs](#blogs)
* [Books](#books)
* [构建工具](#build-tools)
* [代码和包存储库](#code-and-package-repositories)
* [命令行生产力](#commandline-productivity)
* [Communities](#communities)
* [Data](#data)
* [文档助手](#documentation-helper)
* [编辑器和 IDE](#editors-and-ides)
* [Frameworks](#frameworks)
* [互动学习](#interactive-learning)
* [Logging](#logging)
* [模块开发模板](#module-development-templates)
* [包管理器](#package-managers)
* [并行处理](#parallel-processing)
* [Podcasts](#podcasts)
* [Security](#security)
* [SharePoint](#sharepoint)
* [SQL服务器](#sql-server)
* [Testing](#testing)
* [Themes](#themes)
* [UI](#ui)
* [Videos](#videos)
* [Webserver](#webserver)
* [Misc](#misc)

## API 包装器

* [HipChatAdmin](https://github.com/cofonseca/HipChatAdmin) - 通过 HipChat API 与 Atlassian HipChat 进行简单集成的模块。
* [PSGitHub](https://github.com/pcgeek86/PSGitHub) - 模块包含通过其 REST API 管理 GitHub 的命令。
* [Posh-GitHub](https://github.com/Iristyle/Posh-GitHub) - 公开 GitHub API 的 Cmdlet。
* [Posh-Gist](https://github.com/dfinke/Posh-Gist) - 用于与 GitHub Gist 交互的 Cmdlet。
* [PSGist](https://github.com/dotps1/PSGist) - 与 GitHub Gists 一起使用的模块。
* [PSAppVeyor](https://github.com/dotps1/PSAppVeyor) - 与 AppVeyor REST API 交互的模块。
* [PSSlack](https://github.com/RamblingCookieMonster/PSSlack) - 用于简单 Slack 集成的模块。
* [ConfluencePS](https://atlassianps.org/module/ConfluencePS/) - 用于在 powershell 中与 Atlassian 的 Confluence 交互的模块（通过使用 API）。
* [JiraPS](https://atlassianps.org/module/JiraPS/) - 用于在 powershell 中与 Atlassian 的 Jira 交互的模块（通过使用 API）。
* [PSTelegramAPI](https://github.com/mkellerman/PSTelegramAPI) - Telegram API 模块
* [PSTeams](https://github.com/EvotecIT/PSTeams) - 用于将格式化消息发送到 Microsoft Teams 频道的模块。
* [PSURLScanio](https://github.com/sysgoblin/PSURLScanio) - [urlscan.io](https://urlscan.io/) 的模块，是扫描和分析网站的服务。

## 博客

* [Windows PowerShell Blog](https://devblogs.microsoft.com/powershell/) - PowerShell 团队官方博客。
* [Learn PowerShell | Achieve More](http://learn-powershell.net/) - Boe Prox 的个人博客，由脚本专家主持。
* [PowerShellMagazine](http://www.powershellmagazine.com/) - 很棒的杂志。
* [PowerShellExplained](https://powershellexplained.com) - 凯文·马凯特的个人博客
* [Doug Finke](https://dfinke.github.io/#blog) - [PowerShell for Developers](http://shop.oreilly.com/product/0636920024491.do) 的作者。
* [Mike F. Robbins](http://mikefrobbins.com/) - 微软 MVP。 SAPIEN 技术 MVP。 Windows PowerShell TFM 第 4 版的合著者。
* [Adam the Automator](https://adamtheautomator.com/) - Adam Bertram 和朋友撰写的有关自动化、云计算和 DevOps 的引人入胜的技术内容。
* [Clear-Script](https://vexx32.github.io/) - 乔尔（萨洛）弗朗西斯的个人博客。

## 书籍

* [Exploring PowerShell Automation](https://www.manning.com/books/exploring-powershell-automation) - 免费的电子书示例，可让您概述如何管理您的环境。
* [PowerShell in Depth](https://www.manning.com/books/powershell-in-depth) - 管理员的首选参考。每个主要的 shell 技巧、技术和策略都得到了解释和演示，为管理员在 shell 中执行的几乎所有操作提供了全面的参考。
* [Windows PowerShell in Action, Third Edition](https://www.manning.com/books/windows-powershell-in-action-third-edition) - 综合参考指南的最新修订版。
* [Learn Windows PowerShell in a Month of Lunches, Third Edition](https://www.manning.com/books/learn-windows-powershell-in-a-month-of-lunches-third-edition) - 专为忙碌的 IT 专业人员设计的创新教程。只需每天留出一小时（午餐时间就完美），持续一个月，您就能以超乎想象的速度实现 Windows 任务的自动化。
* [Learn PowerShell in a Month of Lunches, Linux and macOS Edition](https://www.manning.com/books/learn-powershell-in-a-month-of-lunches-linux-and-macos-edition) - 以任务为中心的教程，用于使用 Microsoft PowerShell 管理 Linux 和 macOS 系统。
* [Learn PowerShell Scripting in a Month of Lunches](https://www.manning.com/books/learn-powershell-scripting-in-a-month-of-lunches) - 开发、测试和部署脚本的过程以及工具制作艺术的指南。
* [Windows PowerShell Networking Guide](https://leanpub.com/windowspowershellnetworkingguide/read) - Windows 网络的语言特定指南。
* [PowerShell Notes for Professionals](https://goalkicker.com/PowerShellBook/PowerShellNotesForProfessionals.pdf) - 笔记和片段的汇编。
* [PowerShell for SysAdmins: Workflow Automation Made Easy](https://nostarch.com/powershellsysadmins) - 了解如何管理和自动化您的桌面和服务器环境。
* [Practical Automation with PowerShell](https://www.manning.com/books/practical-automation-with-powershell) - 了解如何使用 PowerShell 构建、组织和共享有用的自动化。
* [Learn dbatools in a Month of Lunches](https://www.manning.com/books/learn-dbatools-in-a-month-of-lunches) - 了解如何使用 PowerShell 和出色的 dbatools 模块自动化 SQL Server。
* [Tiny PowerShell Projects](https://www.manning.com/books/tiny-powershell-projects) - 使用 PowerShell 进行系统管理的实践教程。

## 构建工具

* [psake](https://github.com/psake/psake) - 受 rake（又名 Ruby 中的 make）和烘焙（又名 Boo 中的 make）启发而构建自动化工具。
* [Invoke-Build](https://github.com/nightroman/Invoke-Build) - 受 psake 启发构建和测试自动化工具。
* [PSDeploy](https://github.com/RamblingCookieMonster/PSDeploy) - 为简化多种类型的部署而构建的模块。
* [BuildHelpers](https://github.com/RamblingCookieMonster/BuildHelpers) - 适用于 CI/CD 场景的各种辅助函数。
* [YDeliver](https://github.com/manojlds/YDeliver) - 针对 .NET 项目的构建和部署框架。

## 代码和包存储库

* [GitHub](https://github.com/search?l=powershell&q=stars%3A%3E1&s=stars&type=Repositories) - 正在寻找开源 PowerShell 项目？大概就在这里。
* [PowerShell Gallery](https://www.powershellgallery.com/) - 官方 PowerShell 包存储库，由 PowerShellGet 使用。
* [PowerShell Test Gallery](https://www.poshtestgallery.com/) - PowerShell 库的测试版本。开发新模块时很有用。

## 命令行生产力

* [Dotenv](https://github.com/insomnimus/ps-dotenv) - 通过 .env 文件提供目录特定环境，类似于 direnv。
* [posh-git](https://github.com/dahlbyk/posh-git) - 提供 Git/PowerShell 集成的 PowerShell 脚本集。
* [PSReadLine](https://github.com/lzybkr/PSReadLine) - Bash 启发了 PowerShell 的 readline 实现。保留会话之间的历史记录，添加反向历史搜索，并使命令行整体体验更好。
* [TabExpansionPlusPlus](https://github.com/lzybkr/TabExpansionPlusPlus) - PowerShell 模块使自定义选项卡补全变得更容易，并添加自定义参数补全器库。
* [Jump-Location](https://github.com/tkellogg/Jump-Location) - PowerShell `cd` 会读懂您的想法。 [Autojump](https://github.com/wting/autojump) PowerShell 实现。 **`未维护`**
* [Zlocation](https://github.com/vors/ZLocation) * [z.sh](https://github.com/rupa/z) PowerShell 实现。类似于跳转位置。
* [thefuck](https://github.com/nvbn/thefuck) - 出色的应用程序，可以纠正您之前的控制台命令（通过输入“fuck”）。
* [PSFzf](https://github.com/kelleyma49/PSFzf) - 一个包装了 [fzf](https://github.com/junegunn/fzf) 的 PowerShell 模块，这是一个用于命令行的模糊文件查找器。
* [pslinq](https://github.com/manojlds/pslinq) - 适用于 PowerShell 的 LINQ (LINQ2Objects)。
* [posh-with](https://github.com/JanJoris/posh-with) - 使用单个工具为连续工作流程添加命令前缀。
* [poco](https://gist.github.com/yumura/8df37c22ae1b7942dec7)* [peco](https://github.com/peco/peco) 实现。交互式过滤工具。
* [PSDirTag](https://github.com/wtjones/PSDirTag) - DirTags 是相对路径，在 PowerShell 提示符中显示为变量，并在您导航时更新。在浏览文件夹结构时节省击键次数。
* [PSUtil](https://github.com/PowershellFrameworkCollective/PSUtil) - 旨在让用户的控制台生活更加便捷。它包括快捷键、别名、按键绑定和便利功能，旨在提高效率和减少打字。
* [Microsoft.PowerShell.UnixCompleters](https://github.com/PowerShell/Modules/tree/master/Modules/Microsoft.PowerShell.UnixCompleters) - 获取本机 Unix 实用程序的参数完成。需要 zsh 或 bash。
* [PSDepend](https://github.com/RamblingCookieMonster/PSDepend/) - PowerShell 依赖处理程序
* [PSScriptTools](https://github.com/jdhitsolutions/PSScriptTools) - 一组 PowerShell 函数，您可以使用它们来增强您自己的函数和脚本或促进在控制台中的工作。
* [zoxide](https://github.com/ajeetdsouza/zoxide) - 导航文件系统的更好方法。用 Rust 编写，跨 shell，比其他自动跳转程序快得多。

## 社区

* [PowerShell.org](http://powershell.org/) - 论坛、峰会、社区博客文章等等。
* [/r/PowerShell](http://www.reddit.com/r/powershell) - Reddit PowerShell 社区。
* [Slack PowerShell team](https://poshcode.org/slack) - 专用于 PowerShell 的大型聊天室。与 irc.freenode.net 上的“#PowerShell”桥接。
* [Research Triangle PowerShell User Group](https://www.meetup.com/Research-Triangle-PowerShell-Users-Group/) - 非常活跃的 PowerShell 和自动化用户组。第一个和第三个星期三开会。欢迎所有技能水平的人。

## 数据

* [hjson-powershell](https://github.com/TomasBouda/hjson-powershell) - 用于 [HJSON](https://hjson.github.io/) 和 JSON 之间转换的简单 powershell 模块。
* [ImportExcel](https://github.com/dfinke/ImportExcel) - 用于导入/导出 Excel 电子表格的模块，无需 Excel。
* [powershell-yaml](https://github.com/cloudbase/powershell-yaml) - 用于 YAML 格式操作的 PowerShell CmdLets。
* [PSWriteHTML](https://github.com/EvotecIT/PSWriteHTML) - PSWriteHTML 是一个 PowerShell 模块，可让您轻松创建 HTML。
* [PSWritePDF](https://github.com/EvotecIT/PSWritePDF) - 用于在 Windows / Linux 和 MacOS 上创建、编辑、分割、合并 PDF 文件的模块。
* [PSWriteWord](https://github.com/EvotecIT/PSWriteWord) - 用于在未安装 Microsoft Word 的情况下创建 Microsoft Word 文档的模块。

## 文档助手

* [platyPS](https://github.com/PowerShell/platyPS) - 用 Markdown 编写 PowerShell 外部帮助。
* [Invoke-CreateModuleHelpFile](https://github.com/gravejester/Invoke-CreateModuleHelpFile) - PowerShell 函数为模块及其所有命令创建 HTML 帮助文件。
* [PScribo](https://github.com/iainbrighton/PScribo) - PowerShell文档框架可以基于PowerShell的DSL（领域特定语言）创建HTML、Word、文本文件。

## 编辑器和 IDE

* [PowerShell Studio](https://www.sapien.com/software/powershell_studio) - 功能强大的 PowerShell IDE，带有模块、帮助和用户界面开发工具、高 DPI 支持和定期更新。
* [PowerShell for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=ms-vscode.PowerShell) - 为 [Visual Studio Code](https://code.visualstudio.com) 编辑器提供 IntelliSense、代码导航、脚本分析、脚本调试等。
* [PowerShell ISE](https://docs.microsoft.com/en-us/powershell/scripting/components/ise/introducing-the-windows-powershell-ise) - Microsoft Windows 附带官方 PowerShell 开发环境。
* [ISE Steroids](http://www.powertheshell.com/isesteroids/) - PowerShell ISE 的附加组件提供了一组丰富的附加功能来完善 ISE 开发体验。
* [PowerShell Plus](https://www.idera.com/productssolutions/freetools/powershellplus) - 全部集成在一个 IDE 中。
* [SublimeText package](https://github.com/SublimeText/PowerShell) - Sublime Text 的 PowerShell 语言支持。
* [Atom package](https://github.com/jugglingnutcase/language-powershell) - Atom 的 PowerShell 语言支持。

## 框架

* [Carbon](http://get-carbon.org/) - 用于自动化 Windows 计算机配置的 DevOps。
* [PowerShell PowerUp](https://github.com/janikvonrotz/PowerShell-PowerUp) - 强大的服务器管理框架。
* [PSCX](https://github.com/Pscx/Pscx) - PowerShell 社区扩展 - 一组有用的附加 cmdlet。
* [PSFramework](https://github.com/PowershellFrameworkCollective/psframework) - 轻松将配置、日志记录等添加到您自己的 PowerShell 模块中。
* [Kansa](https://github.com/davehull/Kansa) - 事件响应框架。

## 互动学习

* [PSKoans](https://github.com/vexx32/PSKoans) - 通过 Pester 单元测试来学习 PowerShell 语言的一种简单、有趣且交互式的方式。
* [Jupyter-PowerShell](https://github.com/Jaykul/Jupyter-PowerShell) - PowerShell 的 Jupyter 内核。

## 记录

* [PoShLog](https://github.com/PoShLog/PoShLog) - 基于 [Serilog](https://serilog.net) 构建的跨平台、可扩展日志记录模块。

## 模块开发模板

* [Plaster](https://github.com/PowerShell/Plaster) - Plaster 是一个用 PowerShell 编写的基于模板的文件和项目生成器。
* [PSModuleDevelopment](https://github.com/PowershellFrameworkCollective/PSModuleDevelopment) - 凭借该模块的低入门门槛和休闲便利性，2 分钟即可开始使用模块模板。
* [Catesta](https://github.com/techthoughts2/Catesta) - Catesta 是一个 PowerShell 模块项目生成器。它使用模板快速搭建测试并为各种 CI/CD 平台构建集成。

## 包管理器

* [PowerShellGet](https://github.com/powershell/powershellget) - PowerShellGet 是 PowerShell 的包管理器。软件包可在 [PowerShellGallery](https://www.PowerShellGallery.com) 上找到。
* [Chocolatey](https://chocolatey.org/) - 适用于 Windows 的包管理器。在 Windows 上管理软件的合理方法。
* [GitLab](https://github.com/akamac/GitLabProvider) - 使用 GitLab 服务器作为包提供程序。
* [Scoop](https://scoop.sh) - 适用于 Windows 的命令行安装程序。
* [PowerShell App Deployment Toolkit](https://psappdeploytoolkit.com/) - 提供一组函数来执行常见的应用程序部署任务并在部署期间与用户交互。

## 并行处理

* [PoshRSJob](https://github.com/proxb/PoshRSJob) - 提供 PSJobs 的替代方案，在后台运行命令时性能更高，开销更少。
* [Invoke-Parallel](https://github.com/RamblingCookieMonster/Invoke-Parallel) - 此函数将接受脚本或脚本块，并针对指定对象并行运行它。
* [PSThreadJob](https://github.com/PaulHigin/PSThreadJob) - 用于基于线程而不是进程运行并发作业的模块。

## 播客

* [PowerScripting](https://powershell.org/category/podcast/) - 由 Jon Walz 和 Hal Rottenberg 主持的每周节目。
* [The PowerShell News Podcast](https://powershellnews.podbean.com/) - 此播客是有关 PowerShell 的最新新闻。

## 安全性

* [PowerShellArsenal](https://github.com/mattifestation/PowerShellArsenal) - 用于帮助逆向工程师的模块。
* [PowerTools](https://github.com/Veil-Framework/PowerTools) - 专注于进攻行动的项目集合。
* [PowerForensics](https://github.com/Invoke-IR/PowerForensics) - 适用于 Windows 的流行实时磁盘取证平台。
* [PowerSploit](https://github.com/PowerShellMafia/PowerSploit) - 开发后框架。
* [PowerShellEmpire](https://github.com/PowerShellEmpire/Empire) - 开发后代理。
* [PSReflect](https://github.com/mattifestation/PSReflect) - 在 PowerShell 中轻松定义内存中枚举、结构和 Win32 函数。对于攻击很有用，[示例](https://github.com/FuzzySecurity/PowerShell-Suite/tree/master/Bypass-UAC)。
* [BloodHound](https://github.com/BloodHoundAD/BloodHound) - 轻松识别原本无法快速识别的高度复杂的攻击路径。
* [Nishang](https://github.com/samratashok/nishang) - 为红队、渗透测试和进攻性安全启用脚本。
* [Harness](https://github.com/Rich5/Harness) - 交互式远程 PowerShell 有效负载。
* [Invoke-Obfuscation](https://github.com/danielbohannon/Invoke-Obfuscation) - PowerShell 混淆器。
* [p0wnedShell](https://github.com/Cn33liz/p0wnedShell) - PowerShell Runspace 后利用工具包。
* [PESecurity](https://github.com/NetSPI/PESecurity) - 用于检查 Windows 二进制文件 (EXE/DLL) 是否已使用 ASLR、DEP、SafeSEH、StrongNaming 和 Authenticode 进行编译的模块。
* [Powershellery](https://github.com/nullbind/Powershellery) - 用于一般黑客攻击的 Powershell 脚本。
* [PowerUpSQL](https://github.com/NetSPI/PowerUpSQL) - 用于攻击 SQL Server 的工具包。

## 共享点

* [AutoSPInstaller](https://autospinstaller.com/) - 自动化 SharePoint 2010-2019 安装脚本。
* [SPReplicator](https://github.com/potatoqualitee/SPReplicator) - SPReplicator 有助于将 SharePoint 列表数据复制到 CSV、SQL Server、SharePoint 本身等/从 CSV、SQL Server、SharePoint 本身等复制。
* [SharePoint2019Commands](https://github.com/sassdawe/SharePoint2019Commands) - PowerShell 模块可帮助您自动加载所有 SharePoint 2019 cmdlet。

## SQL服务器

* [dbatools](https://dbachecks.io) - 帮助 SQL Server 专业人员通过实例迁移等提高工作效率。
* [SimplySql](https://github.com/mithrandyr/SimplySql) - SimplySql 是一个模块，它提供了一组直观的 cmdlet，用于与抽象供应商详细信息的数据库进行通信。基本模式是连接到数据库，执行一个或多个sql。

## 测试

* [Pester](https://github.com/pester/Pester) - PowerShell BDD 风格的测试框架。
* [Format-Pester](https://github.com/equelin/format-pester) - 用于记录 Pester 结果的 PowerShell 模块 - 使用 [PScribo](https://github.com/iainbrighton/PScribo) 将 Pester 结果导出到 HTML、Word、文本文件。
* [Selenium](https://github.com/adamdriscoll/selenium-powershell) - 用于运行 Selenium WebDriver 的 PowerShell 模块。
* [PSScriptAnalyzer](https://github.com/PowerShell/PSScriptAnalyzer) - PSScriptAnalyzer 通过对正在分析的脚本应用一组内置或自定义规则来提供脚本分析并检查脚本中潜在的代码缺陷。

## 主题

* [Oh-My-Posh](https://github.com/jandedobbeleer/oh-my-posh) - 可以通过一个命令启用大量漂亮的主题（包括许多很棒的电力线主题）。
* [PoshColor](https://github.com/JustABearOz/PoshColor) - 常见命令的颜色输出，支持自定义主题。
* [Powerline](https://github.com/Jaykul/PowerLine) - PowerShell 类提供更丰富的输出和提示。
* [Starship](https://github.com/starship/starship) - 适用于任何 shell 的最小、速度极快且高度可定制的提示。

## 用户界面

* [AnyBox](https://github.com/dm3ll3n/AnyBox) - 旨在通过易于定制的 WPF 窗口促进脚本输入/输出。
* [BurntToast](https://github.com/Windos/BurntToast) - 用于在 Microsoft Windows 10 上创建和显示 Toast 通知的模块。
* [Graphical](https://github.com/PrateekKumarSingh/graphical) - 用于绘制彩色控制台 2D 图形（散点图、条形图、折线图）的模块。
* [GraphicalTools](https://github.com/PowerShell/GraphicalTools) - 混合了 PowerShell 和 GUI 的模块！ - 基于 Avalonia 和 gui.cs 构建。
* [PS-Menu](https://github.com/chrisseroka/ps-menu) - 用于呈现交互式控制台菜单的简单模块。
* [PSWriteColor](https://github.com/EvotecIT/PSWriteColor) - Write-Color 是 Write-Host 的包装器，允许您创建具有彩色输出的漂亮脚本。
* [Terminal-Icons](https://github.com/devblackops/Terminal-Icons) - 在终端中显示文件和文件夹图标的模块。
* [psInlineProgress](https://github.com/gravejester/psInlineProgress) - 在 PowerShell 中编写内联进度条。

## 视频

* [PowerShell Unplugged with Jeffrey Snover and Don Jones Ignite 2017](https://www.youtube.com/watch?v=D15vh-ryJGk) - PowerShell 的发明者谈论“帮助您自动化和管理混合云的最新、最酷的 PowerShell 功能”。专注于 PowerShell 社区。
* [Getting Started With PowerShell 3.0 Jump Start](https://mva.microsoft.com/en-US/training-courses/getting-started-with-powershell-30-jump-start-8276) - 快速入门系列适用于没有 PowerShell 经验但想要快速学习的 IT 专业人员。
* [Advanced Tools & Scripting with PowerShell 3.0](https://channel9.msdn.com/Series/advpowershell3) - IT 专业人员可以参加这个高级 PowerShell 课程，了解如何将实时管理和自动化脚本转变为有用的可重用工具和 cmdlet。
* [What's New in PowerShell v5](https://mva.microsoft.com/en-US/training-courses/whats-new-in-powershell-v5-16434) - 通过对PowerShell 5.0版本中一些令人兴奋的新功能的描述。
* [PowerShell Open Source Project](https://channel9.msdn.com/series/PowerShell-Open-Source-Project) - 视频集彻底展示了​​ PowerShell 开源项目如何在 Linux 上运行。
* [PowerShell on Linux and Open Source](https://channel9.msdn.com/Blogs/hybrid-it-management/PowerShell-on-Linux-and-Open-Source) - 简要介绍PowerShell开源项目以及它如何在Linux上运行。
* [PowerShell](https://channel9.msdn.com/Shows/MsftPowerShell) - 本节目将包括有关 PowerShell 自动化平台、所需状态配置 (DSC)、基础设施即代码以及相关概念的视频！这些视频由 Windows PowerShell 的 Microsoft MVP Trevor Sullivan 创建。
* [Learn Windows PowerShell in a Month of Lunches - Don Jones](https://www.youtube.com/watch?v=6CRTahGYnws&list=PL6D474E721138865A) - 同名书籍的视频伴侣。
* [Best Practices for Script Design - Don Jones](https://www.youtube.com/watch?v=Lni4KjGMgu4) - 唐·琼斯 (Don Jones) 讨论了脚本设计原则和最佳实践。
* [PowerShell Toolmaking (1 of 3) - Don Jones](https://www.youtube.com/watch?v=KprrLkjPq_c) - 工具制造（3 中的 1）- 唐·琼斯。
* [PowerShell Toolmaking (2 of 3) - Don Jones](https://www.youtube.com/watch?v=U849a17G7Ro) - 工具制造（3 之 2）- 唐·琼斯。
* [PowerShell Toolmaking (3 of 3) - Don Jones](https://www.youtube.com/watch?v=GXdmjCPYYNM) - 工具制造（3 / 3）- 唐·琼斯。
* [Sophisticated Techniques of Plain Text Parsing - Tobias Weltner](https://www.youtube.com/watch?v=Hkzd8spCfCU) - 对于文本解析很有参考价值。
* [Monad Manifesto Revisited - Jeffrey Snover](https://www.youtube.com/watch?v=j0EX5R2nnRI) - Jeffrey Snover 反思了该语言的起源及其发展方向。
* [AD Forensics with PowerShell - Ashley McGlone](https://www.youtube.com/watch?v=VrDjiVbZZE8) - 很多AD相关的脚本和分析技术。
* [Windows PowerShell What's New in V2 - SAPIEN](https://www.youtube.com/watch?v=85Yrs5ezxHE&list=PL6ue9e1DXqDv74YTX91gYonfFsweNmrDK) - 旧而金。其中大部分内容仍然非常相关。
* [All Things Microsoft PowerShell](https://www.youtube.com/watch?v=IHrGresKu2w&list=PLCGGtLsUjhm2k22nFHHdupAK0hSNZVfXi) - 另一种通用语言参考。
* [Research Triangle PowerShell User Group YouTube Channel](https://www.youtube.com/rtpsug/) - 社区成员提供的大量用户组会议和演示。超过 150 小时的内容。
* [The anatomy of the Get-Help command in PowerShell](https://www.youtube.com/watch?v=cEswNaXxJ9g) - 软件工程师 Tyler Leonhardt 介绍了 Powershell 帮助系统。

## 网络服务器

* [Flancy](https://github.com/toenuff/flancy) - Windows PowerShell 的 Web 微框架。
* [Pode](https://github.com/Badgerati/Pode) - Pode 是一个跨平台 PowerShell 框架，用于创建 Web 服务器来托管 REST API、网站和 TCP/SMTP 服务器。
* [Polaris](https://github.com/PowerShell/Polaris) - 适用于 PowerShell 的跨平台、简约 Web 框架。
* [WebCommander](https://github.com/vmware/webcommander) - 在友好的 Web GUI 中或通过 Web 服务运行脚本并查看结果。

## 杂项

* [DbgShell](https://github.com/Microsoft/DbgShell) - Windows 调试器引擎的 PowerShell 前端。
* [m2cgen](https://github.com/BayesWitnesses/m2cgen) - 一个 CLI 工具，用于将经过训练的经典 ML 模型转换为零依赖的本机 PowerShell 代码。
* [poke](https://github.com/oising/poke) - PowerShell 的超酷反射模块。
像没有人在监视一样探索和调用私有 API。
对于安全研究、测试和快速破解很有用。
* [WSLab](https://github.com/microsoft/WSLab) - Windows Server 快速实验室部署脚本。
* [PoshBot](https://github.com/poshbotio/PoshBot) - 基于 Powershell 的机器人框架。
* [PoShKeePass](https://github.com/PSKeePass/PoShKeePass) - 用于使用 [KeePass](https://keepass.info) 数据库的模块。
