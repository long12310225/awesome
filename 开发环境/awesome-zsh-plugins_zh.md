# 很棒的 zsh 插件

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

## 状态

[![License](https://img.shields.io/github/license/unixorn/awesome-zsh-plugins.svg)](https://opensource.org/license/BSD-3-Clause)
![Awesomebot](https://github.com/unixorn/awesome-zsh-plugins/actions/workflows/awesomebot.yml/badge.svg)
[![GitHub stars](https://img.shields.io/github/stars/unixorn/awesome-zsh-plugins.svg)](https://github.com/unixorn/awesome-zsh-plugins/stargazers)
![Contributors](https://img.shields.io/github/contributors/unixorn/awesome-zsh-plugins.svg)
[![GitHub last commit](https://img.shields.io/github/last-commit/unixorn/awesome-zsh-plugins/main.svg)](https://github.com/unixorn/awesome-zsh-plugins)
[![Track Awesome List](https://www.trackawesomelist.com/badge.svg)](https://www.trackawesomelist.com/unixorn/awesome-zsh-plugins/)

ZSH 框架、插件、教程和主题的集合，灵感来自于各种很棒的列表集合。

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
## 目录

- [Disclaimer](#disclaimer)
- [Frameworks](#frameworks)
  - [alf](#alf)
  - [ansible-role-zsh](#ansible-role-zsh)
  - [ant-zsh](#ant-zsh)
  - [antibody](#antibody)
  - [antidote](#antidote)
  - [antigen-hs](#antigen-hs)
  - [antigen](#antigen)
  - [awesome-lazy-zsh](#awesome-lazy-zsh)
  - [ax-zsh](#ax-zsh)
  - [deer](#deer)
  - [dotzsh](#dotzsh)
  - [fresh](#fresh)
  - [gh-source](#gh-source)
  - [lazy.zsh](#lazyzsh)
  - [miniplug](#miniplug)
  - [oh-my-zsh](#oh-my-zsh)
  - [pms](#pms)
  - [prezto](#prezto)
  - [pumice](#pumice)
  - [rac](#rac)
  - [rat](#rat)
  - [ryzshrc](#ryzshrc)
  - [sheldon](#sheldon)
  - [shellx](#shellx)
  - [shplug](#shplug)
  - [thefly](#thefly)
  - [toasty](#toasty)
  - [usepkg](#usepkg)
  - [uz](#uz)
  - [x-cmd](#x-cmd)
  - [xc-manager](#xc-manager)
  - [yazt](#yazt)
  - [yzsh](#yzsh)
  - [zap](#zap)
  - [zapack](#zapack)
  - [zcomet](#zcomet)
  - [zdx](#zdx)
  - [zeesh](#zeesh)
  - [zef](#zef)
  - [zert](#zert)
  - [zgem](#zgem)
  - [zgen](#zgen)
  - [zgenom](#zgenom)
  - [zilsh](#zilsh)
  - [zim](#zim)
  - [Zinit](#zinit)
  - [zinit-4](#zinit-4)
  - [zit](#zit)
  - [zlugin](#zlugin)
  - [znap](#znap)
  - [zoppo](#zoppo)
  - [zpacker](#zpacker)
  - [zpico](#zpico)
  - [zplug](#zplug)
  - [zpm](#zpm)
  - [zr](#zr)
  - [zshing](#zshing)
  - [zsh-dot-plugin](#zsh-dot-plugin)
  - [zsh-mgr](#zsh-mgr)
  - [zsh-unplugged.](#zsh-unplugged)
  - [zshPlug](#zshplug)
  - [ztanesh](#ztanesh)
  - [ztheme](#ztheme)
  - [ztupide](#ztupide)
  - [zulu](#zulu)
  - [zush 🦥 - 中等性能的 ZSH 配置](#zush----mid-performance-zsh-configuration)
- [Setups](#setups)
  - [zgenom](#zgenom-1)
  - [zinit](#zinit-1)
- [Prerequisites](#prerequisites)
- [Tutorials](#tutorials)
  - [通用ZSH](#generic-zsh)
  - [Antigen](#antigen-1)
  - [Oh-My-Zsh](#oh-my-zsh-1)
  - [Prezto](#prezto-1)
  - [Zgen](#zgen-1)
  - [Zinit（né zplugin）](#zinit-n%C3%A9-zplugin)
  - [Windows 上的 ZSH](#zsh-on-windows)
    - [超级控制台 - 仅限 Windows](#superconsole---windows-only)
- [Plugins](#plugins)
- [Completions](#completions)
- [Themes](#themes)
- [Fonts](#fonts)
- [Installation](#installation)
  - [Antigen](#antigen-2)
  - [dotzsh](#dotzsh-1)
  - [Oh-My-Zsh](#oh-my-zsh-2)
  - [Prezto](#prezto-2)
  - [Zgen](#zgen-2)
  - [Zgenom](#zgenom-2)
  - [zplug](#zplug-1)
  - [zpm](#zpm-1)
- [编写新的插件和主题](#writing-new-plugins-and-themes)
- [其他资源](#other-resources)
  - [中山工具](#zsh-tools)
  - [其他有用的列表](#other-useful-lists)
  - [其他参考资料](#other-references)
- [Thanks](#thanks)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

*贡献前请阅读[贡献指南](Contributing.md)。*

## 免责声明

虽然我已尽力不添加嵌入恶意代码的条目，但我没有时间筛选列表中每个条目的来源。 _使用此列表中的项目需要您自担风险_。

此列表由版权所有者和贡献者“按原样”提供
以及任何明示或暗示的保证，包括但不限于
对适销性和特定用途适用性的默示保证是
否认。在任何情况下，版权所有者或贡献者均不承担任何责任
对于任何直接、间接、偶然、特殊、示范性或后果性的
损害（包括但不限于采购替代品或
服务；使用、数据或利润的损失；或业务中断）但是
造成的和任何责任理论，无论是合同责任、严格责任，
或因使用而产生的任何侵权行为（包括疏忽或其他方式）
即使已被告知可能会造成此类损害，也不得使用本软件。

## 框架

这些框架使自定义 ZSH 设置变得更加容易。

您可以在以下位置找到各种框架的性能计时比较。

- [rossmacarthur/zsh-plugin-manager-benchmark](https://github.com/rossmacarthur/zsh-plugin-manager-benchmark) - 包含最流行的 ZSH 框架的性能基准，包括安装时间和加载时间。
- [pm-perf-test](https://github.com/z-shell/pm-perf-test) - 用于在多个 ZSH 框架上运行性能测试的工具。

### 阿尔夫
![GitHub last commit](https://img.shields.io/github/last-commit/psyrendust/alf) ![GitHub Repo stars](https://img.shields.io/github/stars/psyrendust/alf)

**Alf** 是一个超快速且可配置的 ZSH 框架；它以 [Prezto](https://github.com/sorin-ionescu/prezto) 和 [Antigen](https://github.com/zsh-users/antigen) 为蓝本，同时在幕后利用 [Oh-My-Zsh](https://ohmyz.sh)；并提供标准默认值、别名、函数、自动完成、自动更新和可安装的提示主题和插件。

### ansible-角色-zsh
![GitHub last commit](https://img.shields.io/github/last-commit/viasite-ansible/ansible-role-zsh) ![GitHub Repo stars](https://img.shields.io/github/stars/viasite-ansible/ansible-role-zsh)

**ansible-role-zsh** 是一个零知识安装的 ansible 角色。它使用 [antigen](https://github.com/zsh-users/antigen) 来管理捆绑包和 [oh-my-zsh](ohmyz.sh)。可以有条件地加载捆绑包。默认情况下，它包括 powerlevel9k 主题、自动建议、语法突出显示和 [fzf-widgets](https://github.com/ytet5uy4/fzf-widgets) 和 [fzf-marks](https://github.com/urbainvaes/fzf-marks)。完全可定制。

### ant-zsh
![GitHub last commit](https://img.shields.io/github/last-commit/anthraxx/ant-zsh)
 ![GitHub Repo stars](https://img.shields.io/github/stars/anthraxx/ant-zsh)

**Ant-zsh** 是一个小型轻量级的 ZSH 配置环境，可满足特殊定制需求。它包括插件、主题和基本的便捷设置。

### 抗体
![GitHub last commit](https://img.shields.io/github/last-commit/getantibody/antibody)
 ![GitHub Repo stars](https://img.shields.io/github/stars/getantibody/antibody)

**Antibody** 是用 Golang 编写的更快、更简单的[抗原](https://github.com/zsh-users/antigen)。更多详细信息请访问 [http://getantibody.github.io/](http://getantibody.github.io/)。

### 解毒剂
![GitHub last commit](https://img.shields.io/github/last-commit/mattmc3/antidote)
 ![GitHub Repo stars](https://img.shields.io/github/stars/mattmc3/antidote)

**Antidote** 是一个 ZSH 插件管理器，从头开始考虑性能。

它速度很快，因为它可以同时执行操作，并生成一个超快的静态插件文件，您可以将其包含在 ZSH 配置中。

它是用 ZSH 原生编写的，经过了良好的测试，并从 [Antibody](https://github.com/getantibody/antibody) 停止的地方继续。

[use-omz](https://github.com/getantidote/use-omz) 可以轻松使用 [Oh-My-ZSH](https://github.com/ohmyzsh/ohmyzsh) 和解毒剂。

### 抗原-hs
![GitHub last commit](https://img.shields.io/github/last-commit/Tarrasch/antigen-hs)
 ![GitHub Repo stars](https://img.shields.io/github/stars/Tarrasch/antigen-hs)

**antigen-hs** 是 [antigen](https://github.com/zsh-users/antigen) 的替代品，针对启动 `zsh` 会话时的低开销进行了优化。它会自动为您克隆插件。

### 抗原
![GitHub last commit](https://img.shields.io/github/last-commit/zsh-users/antigen)
 ![GitHub Repo stars](https://img.shields.io/github/stars/zsh-users/antigen)

**Antigen** 是一小组功能，可帮助您轻松管理 shell (ZSH) 插件（称为捆绑包）。这个概念与典型的 vim+pathogen 设置中的捆绑包几乎相同。 Antigen 之于 ZSH，就像 Vundle 之于“vim”。 Antigen 可以加载 oh-my-zsh 主题和插件，并会自动为您克隆它们。

### 真棒懒惰 zsh
![GitHub last commit](https://img.shields.io/github/last-commit/AmJaradat01/awesome-lazy-zsh)
 ![GitHub Repo stars](https://img.shields.io/github/stars/AmJaradat01/awesome-lazy-zsh)

**Awesome-Lazy-ZSH** 是一个简化且可定制的 ZSH 设置工具，用于管理插件和主题。它通过易于使用的 CLI 界面简化了您的终端环境，使您能够有效地管理 .zshrc 配置。
特点

- 插件管理：轻松安装和管理插件。
- 主题定制：应用各种Zsh主题。
- 备份和恢复：保护您的 .zshrc 配置。
- 交互式 CLI：用户友好的设置选项。
- 依赖管理：自动检查 Git、Node.js 和 Homebrew。

### 斧头zsh
![GitHub last commit](https://img.shields.io/github/last-commit/alexbarton/ax-zsh)
 ![GitHub Repo stars](https://img.shields.io/github/stars/alexbarton/ax-zsh)

**Ax-ZSH** 是 ZSH 的模块化配置系统。它提供了合理的默认设置，并且可以通过插件进行扩展。

**Ax-ZSH** 与 [Powerlevel10k](https://github.com/romkatv/powerlevel10k) 和其他扩展很好地集成，包括与 [oh-my-zsh](https://ohmyz.sh/) 兼容的插件。

### 鹿
![GitHub last commit](https://img.shields.io/github/last-commit/ArtixLabs/deer)
 ![GitHub Repo stars](https://img.shields.io/github/stars/ArtixLabs/deer)

一个极简主义的 ZSH 插件管理器。

### 多兹什
![GitHub last commit](https://img.shields.io/github/last-commit/dotphiles/dotzsh)
 ![GitHub Repo stars](https://img.shields.io/github/stars/dotphiles/dotzsh)

**Dotzsh** 力求独立于平台和版本。在旧版本的 ZSH 下运行时，某些功能可能会丢失，但它应该会完全降级，并允许您在不同操作系统的多台计算机上使用相同的设置而不会出现问题。

### 新鲜的
![GitHub last commit](https://img.shields.io/github/last-commit/freshshell/fresh)
 ![GitHub Repo stars](https://img.shields.io/github/stars/freshshell/fresh)

**fresh** 是一个将其他人的 shell 配置（别名、函数等）源到您自己的配置文件中的工具。我们还支持 ackrc 和 gitconfig 等文件。将其视为点文件的 [Bundler](https://bundler.io)。

### gh源
![GitHub last commit](https://img.shields.io/github/last-commit/Yarden-zamir/gh-source) ![GitHub Repo stars](https://img.shields.io/github/stars/Yarden-zamir/gh-source)

**gh-source** 是一个为不喜欢插件管理器的人提供的插件管理器。这是一个简单的 shell 函数，作为采购步骤的一部分，从 GitHub 下载并安装插件。它被设计为与“zsh”一起使用，但它应该适用于任何 shell。

### 懒惰的zsh
![GitHub last commit](https://img.shields.io/github/last-commit/stanleyndachi/lazy.zsh) ![GitHub Repo stars](https://img.shields.io/github/stars/stanleyndachi/lazy.zsh)

对于 **lazy.zsh**，您的“.zshrc”是唯一的事实来源。使用相同的配置在任何地方重现相同的 ZSH 设置；没有框架，没有自动采购，没有隐藏行为。 **lazy.zsh** 安装、更新和跟踪插件，同时您可以准确控制它们的加载方式和时间。

### 迷你插头
![GitHub last commit](https://img.shields.io/github/last-commit/yerinalexey/miniplug) ![GitHub Repo stars](https://img.shields.io/github/stars/yerinalexey/miniplug)

**miniplug** 是 ZSH 的简约插件管理器。

- 重新采购`.zshrc`时不会崩溃或双重插件加载
- 与其他框架不同，Miniplug 不会污染您的“$PATH”
- 只做最低限度的管理插件

### 哦我的zsh
![GitHub last commit](https://img.shields.io/github/last-commit/ohmyzsh/ohmyzsh) ![GitHub Repo stars](https://img.shields.io/github/stars/ohmyzsh/oh-my-zsh)

**oh-my-zsh** 是一个社区驱动的框架，用于管理 ZSH 配置。包括 120 多个可选插件（rails、`git`、macOS、`hub`、`capistrano`、`brew`、`ant`、MacPorts 等）、超过 120 个主题让您的早晨更加有趣，还有一个自动更新工具，可以轻松跟上社区的最新更新。

### 经前综合症
![GitHub last commit](https://img.shields.io/github/last-commit/JoshuaEstes/pms)
 ![GitHub Repo stars](https://img.shields.io/github/stars/JoshuaEstes/pms)

PMS 允许您以有助于减少设置时间并提高工作效率的方式管理您的 shell。它支持主题（改变 shell 的外观）、插件（向 shell 添加功能）和点文件管理。

PMS 框架还允许您在不同的 shell 中使用相同的框架。在您的个人笔记本电脑上使用 ZSH，并在远程服务器上使用“bash”。想尝尝“鱼”吗？来吧，尝试不同的 shell。

### 普雷斯托
![GitHub last commit](https://img.shields.io/github/last-commit/sorin-ionescu/prezto)
 ![GitHub Repo stars](https://img.shields.io/github/stars/sorin-ionescu/prezto)

**Prezto** 通过合理的默认值、别名、函数、自动完成和提示主题丰富了 ZSH 命令行界面环境。 [https://github.com/belak/prezto-contrib](https://github.com/belak/prezto-contrib) 上有一些 [prezto](https://github.com/sorin-ionescu/prezto) 特定插件。

### 浮石
![GitHub last commit](https://img.shields.io/github/last-commit/ryutamaki/pumice)
 ![GitHub Repo stars](https://img.shields.io/github/stars/ryutamaki/pumice)

**Pumice** 是 ZSH 的轻量级插件管理器。

### 拉克
![GitHub last commit](https://img.shields.io/github/last-commit/lomarco/rac)
  ![GitHub Repo stars](https://img.shields.io/github/stars/lomarco/rac)

大多数 ZSH 插件管理器都很臃肿。他们尝试做太多事情 - 依赖图、延迟加载、配置注入 - 在此过程中，他们会减慢你的 shell 速度。

现实情况是，大多数用户甚至从未使用过其中 80% 的功能。 `rac` 故意被最小化。它所做的只是**下载插件**和**更新插件**。

### 老鼠
![GitHub last commit](https://img.shields.io/github/last-commit/gotokazuki/rat-zsh)
  ![GitHub Repo stars](https://img.shields.io/github/stars/gotokazuki/rat-zsh)

ZSH 的轻量级、快速且可复制的插件管理器。使用 🐭 和 🦀 制作 — 没有魔法，没有沉重的框架。

特点🐭✨

- 🚀 简单的设置
- 用单根卷线安装
- 只需在 .zshrc 中添加一行 eval 即可开始使用它
- ⚙️可配置且可复制
- 基于TOML的简单配置
- 自动插件加载顺序控制
- 🐙 GitHub 集成
- 从 GitHub 存储库获取插件
- 支持分支、标签和提交
- 自动处理 Git 子模块
- ⚡️ 轻量且快速
- 并行插件同步
- 内置 Rust 🦀
- 🔄 无缝更新
- 自我升级
-插件同步

### 雷兹什克
![GitHub last commit](https://img.shields.io/github/last-commit/ryzshrc/ryzshrc)
  ![GitHub Repo stars](https://img.shields.io/github/stars/ryzshrc/ryzshrc)

**ryzshrc** 是一个智能、创新的插件管理器，类似于 [Oh My Zsh](https://ohmyz.sh/)，旨在通过专业和炫酷的功能来增强您的终端体验。它通过提供高效的 shell 管理、时尚的主题和强大的插件来提高生产力。非常适合寻求现代智能方式使用终端的开发人员

### 谢尔顿
![GitHub last commit](https://img.shields.io/github/last-commit/rossmacarthur/sheldon)
  ![GitHub Repo stars](https://img.shields.io/github/stars/rossmacarthur/sheldon)

**sheldon** 是一个快速、可配置的 shell 插件管理器。

- 它可以管理：
- 任何“git”存储库。
- 分支/标签/提交支持。
- 对 GitHub 存储库的额外支持。
- 对要点的额外支持。
- 任意远程文件，只需指定URL。
- 本地插件，只需指定目录路径即可。
- 使用 [handlebars](http://handlebarsjs.com/) 模板的高度可配置的安装方法。
- 超快速并行安装。
- 使用 [TOML](https://github.com/toml-lang/toml) 语法的配置文件。
- 使用锁定文件可以更快地加载插件。

### 外壳x

适用于多个 shell 的通用脚本/插件加载器，包括“ZSH”。

- 有一个“插件”系统，允许您执行安装包、克隆存储库、导出变量、运行命令等操作。并且跨shell兼容。
- 具有统一的配置 shell 的方法，它使用多种方法之一来通过一组预定义的文件和文件夹来标准化主文件夹。它在其他文件夹之间定义了一个自动包含在“PATH”中的“~/bin”文件夹，因此它可以帮助您在所有系统上始终使用相同的方法。
- 在不同的文件夹中有不同的插件，这允许在某些环境中加载某些文件夹来加载变量或任何其他特殊配置。它还允许您轻松克隆其他用户的插件。
- 它提供了一组最小的库和二进制文件，其中捆绑了一组函数/别名/等。基于 SH/BASH（与其他 shell 兼容），可在插件上下文中使用以轻松执行某些操作。

### 什普拉格
![GitHub last commit](https://img.shields.io/github/last-commit/dtrugman/shplug)
 ![GitHub Repo stars](https://img.shields.io/github/stars/dtrugman/shplug)

**shplug** 是管理 shell 环境的简单解决方案。适用于“bash”和“zsh”。使用“git”存储库可以轻松地跨多台计算机同步您的环境。

### 苍蝇
![GitHub last commit](https://img.shields.io/github/last-commit/joknarf/thefly) ![GitHub Repo stars](https://img.shields.io/github/stars/joknarf/thefly)

**TheFly** 是一个 `bash`/`zsh`/`ksh` 插件管理器和环境传送器

使您的 shell 环境和插件在任何地方（主机/用户）都可用！

### 烤面包的
![GitHub last commit](https://img.shields.io/github/last-commit/CosmicToast/toasty-zsh) ![GitHub Repo stars](https://img.shields.io/github/stars/CosmicToast/toasty-zsh)

**Toasty** 是一个 ZSH 框架，旨在促进管理，而不是命令它。

### 使用包装
![GitHub last commit](https://img.shields.io/github/last-commit/gynamics/zsh-usepkg) ![GitHub Repo stars](https://img.shields.io/github/stars/gynamics/zsh-usepkg)

**Usepkg** 是一个最小的声明式 zsh 插件管理器。

支持：
- 使用声明的方法获取和加载插件
- 使用命令列出、检查、重新加载、更新和删除插件

依赖项：
- `zsh`
-gnu coreutils
- `git` （可选，如果您想从互联网克隆 git 存储库）
- `curl` （可选，如果你想通过 url 获取脚本文件）

优点：
- 极其简单和轻便，但足以使用。
- 与“zplug”等类似包相比，它的配置语法要简单得多。


### 乌兹
![GitHub last commit](https://img.shields.io/github/last-commit/maxrodrigo/uz)
 ![GitHub Repo stars](https://img.shields.io/github/stars/maxrodrigo/uz)

**uz** 是 ZSH 的微型插件管理器

### x命令
![GitHub last commit](https://img.shields.io/github/last-commit/x-cmd/x-cmd)
 ![GitHub Repo stars](https://img.shields.io/github/stars/x-cmd/x-cmd)

**x-cmd** 是一个使用 posix shell 和 awk 实现的工具集。它的大小非常小，并提供了许多有趣的功能。这是一个里程碑演示：https://x-cmd.com/

x-cmd提供的工具：
- [常用命令的包装器（例如 cd、ip、ps、tar、apt、brew）](https://x-cmd.com/mod/zuz)：与本机命令相比，这些包装的命令更智能且更易于使用。
- [轻量级包管理工具](https://x-cmd.com/pkg/)：我们使用 shell 和 awk 实现了一个轻量级包管理工具。通过它，您可以快速获取最常用的软件工具，如jq、7za、bat、nvim、python、node、go等。
- [有用网站的 CLI（例如 github.com、cht.sh）](https://x-cmd.com/mod/cht)：我们使用 shell 和 awk 封装了他们的 API，以供日常使用并在脚本中获取相应的服务。
- [AI工具](https://x-cmd.com/mod/openai)：我们提供了ChatGPT、Gemini、Jina.ai等CLI，并针对不同的应用场景封装了相应的快捷命令，例如用于与Gemini AI聊天的“@gemini”和用于使用AI翻译指定内容或命令结果的“@zh”。

### xc-经理
![GitHub last commit](https://img.shields.io/github/last-commit/Rakosn1cek/XC-Manager)
 ![GitHub Repo stars](https://img.shields.io/github/stars/Rakosn1cek/XC-Manager)

**XC-Manager** 是一个 Zsh 原生命令库，旨在弥合临时 shell 历史记录和永久别名之间的差距。它允许您存储复杂的单行文字和描述，并通过交互式 TUI 调用它们。

XC-Manager 提供的功能：
- **命令保管库**：将历史记录中的任何命令直接保存到主题保管库中（例如，工作、系统管理员、媒体）。
- **FZF TUI**：使用强大的、TTY 安全的“fzf”界面立即搜索并执行存储的命令。
- **别名升级**：将常用的存储命令提升为永久系统别名，无需手动编辑配置文件。
- **全局搜索**：同时查询所有 Vault 文件以查找一个特定标志或复杂管柱。

### 亚兹特
![GitHub last commit](https://img.shields.io/github/last-commit/bashelled/yazt)
 ![GitHub Repo stars](https://img.shields.io/github/stars/bashelled/yazt)

**Yazt** 是一个简单的 ZSH 主题管理器，易于维护，几乎与所有内容兼容。您可以在插件中使用提示，混合“n”匹配两个主题，并进行一些修改，您甚至可以在“bash”中使用它。

### yzsh
![GitHub last commit](https://img.shields.io/github/last-commit/yunielrc/yzsh)
 ![GitHub Repo stars](https://img.shields.io/github/stars/yunielrc/yzsh)

**yzsh** 是一个简单的 ZSH 框架，用于管理插件、主题、函数、别名和环境变量。

### 扎普
![GitHub last commit](https://img.shields.io/github/last-commit/zap-zsh/zap)
 ![GitHub Repo stars](https://img.shields.io/github/stars/zap-zsh/zap)

**:zap:zap** 是一个最小的 ZSH 插件管理器。

### 扎包
![GitHub last commit](https://img.shields.io/github/last-commit/aiya000/zsh-zapack)
 ![GitHub Repo stars](https://img.shields.io/github/stars/aiya000/zsh-zapack)

**zapack** 是一个基本的快速最小 ZSH 插件加载器。

### 兹彗星
![GitHub last commit](https://img.shields.io/github/last-commit/agkozak/zcomet)
 ![GitHub Repo stars](https://img.shields.io/github/stars/agkozak/zcomet)

**zcomet** 是一个简约的 ZSH 插件管理器，可以让您以惊人的速度快速进入提示，而无需缓存（请参阅基准测试）。除了加载和更新存储在“git”存储库中的插件之外，它还支持延迟加载插件（进一步减少启动时间）以及下载和获取代码片段。

### 兹德克斯
![GitHub last commit](https://img.shields.io/github/last-commit/landerox/zdx-suite)
 ![GitHub Repo stars](https://img.shields.io/github/stars/landerox/zdx-suite)

ZDX（Zsh 开发者体验套件）是一个精简的、终端优先的生产力套件和 ZSH 的自定义插件加载器。停止记住复杂的标志和参数。 ZDX 提供对您的日常 shell 工作流程的快速、模糊搜索驱动的访问。这些模块化、交互式套件和自定义插件由 [fzf](https://github.com/junegunn/fzf) 提供支持，可将您的终端转变为高性能开发人员仪表板。

### 泽什
![GitHub last commit](https://img.shields.io/github/last-commit/zeekay/zeesh)
 ![GitHub Repo stars](https://img.shields.io/github/stars/zeekay/zeesh)

**Zeesh** 是一个跨平台 ZSH 框架。它与 [oh-my-zsh](http://ohmyz.sh/) 类似，但不兼容。它具有模块化插件架构，使其易于扩展。它具有丰富的默认设置，但设计得尽可能轻量级。

### 泽夫
![GitHub last commit](https://img.shields.io/github/last-commit/declnix/zef)
 ![GitHub Repo stars](https://img.shields.io/github/stars/declnix/zef)

Nix 中的声明式 zsh 插件管理器，目标是 <50 毫秒冷启动。受到 nvf 的启发，围绕这样的想法构建：如果在构建时已知整个 shell 配置，则运行时可以是一个薄垫片。

### 泽尔特
![GitHub last commit](https://img.shields.io/github/last-commit/oxcl/zert)
 ![GitHub Repo stars](https://img.shields.io/github/stars/oxcl/zert)

**zert** 是一个纯 ZSH 插件管理器，围绕一个简单的想法构建：您的插件应该直接在“.zshrc”中声明，固定到精确的提交，并且可以在任何机器上重现 - 就像“npm”对 Node 项目所做的那样。

无需维护配置文件。无需记住用于添加插件的子命令。没有外部工具。只是 ZSH、`git` 和 `curl`。

特点

* **内联声明性语法** — 直接在 `.zshrc` 中声明插件。没有单独的配置文件，没有添加命令。
* **基于锁定文件的可重复性** - `zert.lock` 将每个插件固定到精确的 `git` 提交 SHA。承诺吧。分享一下。在任何地方复制它。
* **并行安装** — 使用 `git clone --filter=tree:0` 同时克隆多个插件，以实现最小带宽。
* **顺序、有序加载** — 插件的来源完全按照您声明它们的顺序。总是。
* **零外部 UI 依赖** — 完全由 ANSI 转义码构建的实时进度条和旋转器。
* **自我管理** - Zert 使用 `zert update zert` 进行自我更新，作为一流的插件进行管理。
* **Oh-My-Zsh / Prezto 兼容性** — 加载 OMZ 库和 Prezto 模块，无需安装任何一个框架。*

### 紫宝石
![GitHub last commit](https://img.shields.io/github/last-commit/qoomon/zgem)
 ![GitHub Repo stars](https://img.shields.io/github/stars/qoomon/zgem)

**zgem** 是 ZSH 的插件管理器，支持从 `git`、http 和本地文件加载和更新插件和主题。

### 兹根
![GitHub last commit](https://img.shields.io/github/last-commit/tarjoilija/zgen)
 ![GitHub Repo stars](https://img.shields.io/github/stars/tarjoilija/zgen)

**Zgen 目前并未得到积极维护**。我建议您使用 [zgenom](https://github.com/jandamm/zgenom) 分支，该分支得到积极维护，并不断获得新功能和错误修复。

**Zgen** 是 ZSH 的轻量级插件管理器，灵感来自 [Antigen](https://github.com/zsh-users/antigen)。目标是在启动 shell 时将开销降至最低，因为没有人喜欢等待。

### 兹格诺姆
![GitHub last commit](https://img.shields.io/github/last-commit/jandamm/zgenom)
 ![GitHub Repo stars](https://img.shields.io/github/stars/jandamm/zgenom)

ZSH 的轻量级插件管理器，它是一个扩展了出色的 [zgen](https://github.com/tarjoilija/zgen) 的分支，并提供更多功能和错误修复，同时完全向后兼容。

为了在新的终端会话期间保持快速加载，“zgenom”生成一个静态“init.zsh”文件，该文件除了获取插件并将它们附加到“fpath”之外什么也不做。

这样就不必在每个 shell 会话启动期间执行耗时的逻辑（插件检查、更新等），从而最大限度地减少启动时间。缺点是，每当您更新“.zshrc”中的插件列表时，您都必须使用“zgenom Reset”手动刷新初始化脚本。

Zgenom 可以加载 [oh-my-zsh](http://ohmyz.sh/) 兼容和 [prezto](https://github.com/sorin-ionescu/prezto) 兼容的插件和主题，并且当您将它们添加到插件列表时，会自动为您“git clone”插件。

### 齐尔什
![GitHub last commit](https://img.shields.io/github/last-commit/zilsh/zilsh)
 ![GitHub Repo stars](https://img.shields.io/github/stars/zilsh/zilsh)

**zilsh** 是一个 ZSH 配置系统，旨在更多地吸引高级用户并遵循 vim-pathogen 的简单方法。

### 齐姆
![GitHub last commit](https://img.shields.io/github/last-commit/zimfw/zimfw)
 ![GitHub Repo stars](https://img.shields.io/github/stars/zimfw/zimfw)

**Zim** 是一个 ZSH 配置框架，具有极快的速度和模块化扩展。

### 齐尼特
![GitHub last commit](https://img.shields.io/github/last-commit/zdharma-continuum/zinit) ![GitHub Repo stars](https://img.shields.io/github/stars/zdharma-continuum/zinit)

**Zinit** 是一个创新的，可能是（由于 Turbo）最快的插件管理器，支持：

- Turbo 模式 – ZSH 启动速度提高 80%！例如：不是 200 毫秒，而是 40 毫秒
- 完成管理（有选择地禁用和启用完成）
- 片段（↔ 通过 URL 下载的常规文件，例如：脚本）并通过它们支持 Oh My Zsh 和 Prezto 插件（→ 低开销）
- 附件（↔ Zinit 扩展）
- 报告（来自插件加载 – 插件不再是黑匣子）
- 插件卸载（允许例如：动态主题切换）
- `bindkey` 捕获和重新映射
- 包裹
- 干净的“fpath”（数组“$fpath”不用于添加完成和自动加载函数，因此它保持简洁，不臃肿）
- 服务↔单实例、后台插件
- 另外，一般来说：ZSH 插件标准中的所有机制 – Zinit 是该标准的参考实现。

该项目非常活跃——目前超过 3100 次提交。

### zinit-4
![GitHub last commit](https://img.shields.io/github/last-commit/psprint/Zinit-4)
 ![GitHub Repo stars](https://img.shields.io/github/stars/psprint/Zinit-4)

这是来自[原作者](https://github.com/psprint)的Zinit 4，他曾经从GitHub上删除了[Zinit](https://github.com/zdharma-continuum/zinit)存储库。这催生了一个社区驱动的 [zdharma-continuum](https://github.com/zdharma-continuum) 组织，该组织复兴了 psprint 的所有 ZSH 项目。 @zdharma-continuum 分支的主要创新是：

- AppImage分发（发布链接），
- 操作完成 - 按“Alt-Shift-A”和“Alt-Shift-C”来完成插件名称和ice修饰符，
- 主题 – 将 `$ZITHEM`E 设置为默认、蓝色和金色之一，以设置用于 Zinit 4 消息的颜色集，
- 新的ice `build` 相当于其他三个ice：`null`、`configure` 和`make install`，并且只需从源代码构建项目，并支持 autotools/CMake/Meson/Scons。

这些是最明显的变化，但还有更多（例如：支持使用以前构建的项目/`$ZPFX`中的库进行编译）。

### 青春痘
![GitHub last commit](https://img.shields.io/github/last-commit/thiagokokada/zit)
 ![GitHub Repo stars](https://img.shields.io/github/stars/thiagokokada/zit)

**zit** 是 ZSH 的插件管理器。它是最小的，因为它实现了作为插件管理器的最低要求：它允许用户从 `git` 存储库（以及仅 `git` 存储库，这就是这个名字的原因）安装插件，源插件并更新它们。它没有实现一些花哨的功能，例如清理已删除的插件、自动编译已安装的插件、oh-my-zsh/prezto/其他 ZSH 框架的别名、构建二进制文件、“$PATH”操作等。

### 兹卢金
![GitHub last commit](https://img.shields.io/github/last-commit/DrgnFireYellow/zlugin)
 ![GitHub Repo stars](https://img.shields.io/github/stars/DrgnFireYellow/zlugin)

**zlugin** 是一个非常轻量级的 ZSH 插件管理器。

### 兹纳普
![GitHub last commit](https://img.shields.io/github/last-commit/marlonrichert/zsh-snap) ![GitHub Repo stars](https://img.shields.io/github/stars/marlonrichert/zsh-snap)

**:zap:Znap** 是 ZSH 的轻量级插件管理器和 `git` 存储库管理器，易于理解。虽然专为 ZSH 插件量身定制，**Znap** 还可以用作管理“git”存储库的通用实用程序。

Znap 可以：

- 使任何提示立即出现。只需一条命令，即可将启动时间从约 200 毫秒缩短至约 40 毫秒。
- 异步编译您的插件和函数。
- 缓存那些昂贵的“eval $(commands)”。
- 并行克隆或拉取多个存储库。
- 重新克隆所有存储库，而无需重新输入它们。
- 多仓库管理
- 自动 `compinit` 和 `bashinit` - 您不再需要在 `.zshrc` 中使用它们，znap 将根据需要自动执行它们。

### 佐波
![GitHub last commit](https://img.shields.io/github/last-commit/zoppo/zoppo)
 ![GitHub Repo stars](https://img.shields.io/github/stars/zoppo/zoppo)

**Zoppo** 是 ZSH 的残缺配置框架。正如意大利谚语所说：“chi va con lo zoppo, impara a zoppicare”，我们意识到我们正在与一个跛子同行，而现在我们自己也将成为跛子。

### 打包机
![GitHub last commit](https://img.shields.io/github/last-commit/happyslowly/zpacker)
 ![GitHub Repo stars](https://img.shields.io/github/stars/happyslowly/zpacker)

**Zpacker** 是一个轻量级的 ZSH 插件和主题管理框架。

### 紫皮科
![GitHub last commit](https://img.shields.io/github/last-commit/thornjad/zpico)
 ![GitHub Repo stars](https://img.shields.io/github/stars/thornjad/zpico)

**zpico** 是一个微型 ZSH 包管理器。没有多余的装饰，没有臃肿，只有 2 kB 的 100% ZSH 代码，为您的 ZSH 环境提供完整的包管理。

ZSH 包管理器很丰富，但大多数都臃肿、缓慢或要求过高。最重要的是，不少已经被遗弃多年。 Zpico 并不寻求成为最好的，而是在功能与微小、快速的占用空间之间取得平衡。

### 塞插头
![GitHub last commit](https://img.shields.io/github/last-commit/zplug/zplug)
 ![GitHub Repo stars](https://img.shields.io/github/stars/zplug/zplug)

**:hibiscus: Zplug** 是下一代 ZSH 插件管理器。

- 可以管理一切
- [GitHub](https://github.com) 和 [Bitbucket](https://bitbucket.org) 上的 ZSH 插件/UNIX 命令
- Gist 文件 ([gist.github.com](https://gist.github.com/discover))
- 外部管理的插件，例如 [oh-my-zsh](https://github.com/ohmyzsh/ohmyzsh) 和 [prezto](https://github.com/sorin-ionescu/prezto) 插件/主题
- [GitHub Releases](https://help.github.com/articles/about-releases/) 上的二进制工件
- 本地插件
- 等等（您可以添加您的[自己的源](https://github.com/zplug/zplug/blob/master/doc/guide/External-Sources.md)！）
- 超快速并行安装/更新
- 支持延迟加载
- 分支/标签/提交支持
- 更新后、加载后挂钩
- 包之间的依赖关系
- 与 [antigen](https://github.com/zsh-users/antigen) 不同，不需要 ZSH 插件文件 (`*.plugin.zsh`)
- 交互界面（[fzf](https://github.com/junegunn/fzf)、[peco](https://github.com/peco/peco)、[zaw](https://github.com/zsh-users/zaw)等）
- 减少[启动时间]的缓存机制(https://github.com/zplug/zplug#vs)

### zpm
![GitHub last commit](https://img.shields.io/github/last-commit/zpm-zsh/zpm)
 ![GitHub Repo stars](https://img.shields.io/github/stars/zpm-zsh/zpm)

**zpm** (ZSH Plugin Manager) 是 [ZSH](http://www.zsh.org/) 的插件管理器，它结合了命令式和声明式方法。第一次运行时，“zpm”将执行复杂的逻辑并生成缓存，之后将仅使用缓存，因此这使得该框架非常快。

- 最快的插件管理器（真的，第一次运行后，根本不会使用`zpm`）
- 支持异步加载
- 包之间的依赖关系
- **zpm** 在 Linux、macOS、FreeBSD 和 Android 上运行。
- **zpm** 插件与 [oh-my-zsh](http://ohmyz.sh/) 兼容。

### 兹尔
![GitHub last commit](https://img.shields.io/github/last-commit/jedahan/zr)
 ![GitHub Repo stars](https://img.shields.io/github/stars/jedahan/zr)

**zr** 是一个用 Rust 编写的快速、简单的 ZSH 插件管理器，可以通过“cargo install zr”轻松安装。

### 志兴
![GitHub last commit](https://img.shields.io/github/last-commit/zakariaGatter/zshing)
 ![GitHub Repo stars](https://img.shields.io/github/stars/zakariaGatter/zshing)

**zshing** 是一个类似于 Vundle/Vim 的 ZSH 插件管理器，允许您...

- 在`~/.zshrc`中跟踪和配置您的插件
- 安装 ZSH 插件
- 更新 ZSH 插件
- 按名称搜索所有可用的 ZSH 插件
- 清理未使用的插件
- 在*单个命令*中运行上述操作
- 管理已安装插件的**源插件**

### zsh-dot-插件
![GitHub last commit](https://img.shields.io/github/last-commit/DuckzCantFly/zsh-dot-plugin) ![GitHub Repo stars](https://img.shields.io/github/stars/DuckzCantFly/zsh-dot-plugin)

**zsh-dot-plugin** 只需约 21 行代码即可自定义您的 `.zshrc`。基于 [zsh-unplugged](https://github.com/mattmc3/zsh_unplugged)。

### zsh管理器
![GitHub last commit](https://img.shields.io/github/last-commit/amt911/zsh-mgr)
 ![GitHub Repo stars](https://img.shields.io/github/stars/amt911/zsh-mgr)

一个简单的 zsh 插件管理器。特点：

- 自动更新所有插件。
- 自动更新。
- 两个自动更新程序的可配置时间间隔。

### zsh-拔掉插头。
![GitHub last commit](https://img.shields.io/github/last-commit/mattmc3/zsh_unplugged)
 ![GitHub Repo stars](https://img.shields.io/github/stars/mattmc3/zsh_unplugged)

**zsh-unplugged** 是一个_tiny_插件管理器。太长了；您的 ZSH 插件不需要一个庞大而臃肿的插件管理器。一个简单的约 20 行函数可能就足够了。

### 插件
![GitHub last commit](https://img.shields.io/github/last-commit/Atlas34/zshPlug)
 ![GitHub Repo stars](https://img.shields.io/github/stars/Atlas34/zshPlug)

**zshPlug** 是一个很大程度上基于 [zap](https://github.com/zap-zsh/zap) 的极简插件管理器。

### 兹塔内什
![GitHub last commit](https://img.shields.io/github/last-commit/miohtama/ztanesh)
 ![GitHub Repo stars](https://img.shields.io/github/stars/miohtama/ztanesh)

**Ztanesh** 旨在通过 ztanesh 项目提供的配置来提高您的 UNIX 命令行体验和生产力：这些工具将使您的 shell 更强大且更易于使用。

### 主题
![GitHub last commit](https://img.shields.io/github/last-commit/SkyyySi/ztheme)
 ![GitHub Repo stars](https://img.shields.io/github/stars/SkyyySi/ztheme)

**ztheme** 是 ZSH 的一个小型且快速的主题引擎。

### 兹图皮德
![GitHub last commit](https://img.shields.io/github/last-commit/mpostaire/ztupide)
 ![GitHub Repo stars](https://img.shields.io/github/stars/mpostaire/ztupide)

**ztupide** 是一个简单快速的 ZSH 插件管理器。它使用“zcompile”和异步加载来加快 shell 启动时间。

### 祖鲁语
![GitHub last commit](https://img.shields.io/github/last-commit/zulu-zsh/zulu)
 ![GitHub Repo stars](https://img.shields.io/github/stars/zulu-zsh/zulu)

**Zulu** 是 ZSH 5 或更高版本的环境管理器，旨在让您无需编写任何代码即可轻松管理 shell。

- 无需编辑文件即可轻松管理您的 shell 环境。
- 创建别名、函数和环境变量，并在下次 shell 启动时使用它们。
- 使用简单的命令从“$path”、“$fpath”和“$cdpath”添加和删除目录。
- 轻松安装软件包、插件和主题，并立即提供给您。

### zush 🦥 - 中等性能的 ZSH 配置
![GitHub last commit](https://img.shields.io/github/last-commit/shyndman/zush)
 ![GitHub Repo stars](https://img.shields.io/github/stars/shyndman/zush)

**zush** 是一种性能感知型 ZSH 配置，专为低于 200 毫秒的启动时间而设计，同时保持完整功能。

特点：

- 即时提示 - 基本提示立即出现，完整提示在约 129 毫秒后加载
- 插件管理 - 简单的 `zushp user/repo` 命令即可安装 GitHub 插件
- 延迟加载 - `nvm`、`pyenv`、`cargo` 等工具仅在需要时加载
- 自动编译 - 所有 ZSH 文件均使用“zcompile”编译以加快加载速度
- 智能缓存 - 环境更改缓存以供即时启动

## 设置

本节用于完整设置 dropins - 它们不是框架，但也不是简单的插件/主题。

### 兹格诺姆

- [zsh-quickstart-kit](https://github.com/unixorn/zsh-quickstart-kit) - 将 ZSH 与 [zgenom](https://github.com/jandamm/zgenom) 一起使用的简单快速入门。这会自动配置 ZSH 以使用 [zgenom](https://github.com/jandamm/zgenom) 加载精选的（但易于定制）插件集合，并定期自动更新自身、插件和快速入门套件本身。

### 齐尼特

- [ZPWR](https://github.com/MenkeTechnologies/zpwr) - 一个构建在 [Zinit](https://github.com/zdharma-continuum/zinit) 之上的极其强大的自定义终端环境，可实现最大速度。  完整的终端配置框架，包括 `zsh`、`tmux`、`fzf`、`vim` 和 spacemacs 配置。  它包括：

- 12.9k+ 标签完成
- 1.9k+ 别名
- 330+ git 别名
- 400 多个 zpwr 子命令
- 2.8k 功能
- 175+ zpwr 环境变量
- 175+ perl、python、bash、ZSH 脚本
- 2.8k 行 README.md
- 50k+ LOC
- 1线安装

## 先决条件

如果您使用的是 Mac，则每个操作系统更新附带的“zsh”通常非常陈旧。您可以使用“brew install zsh”来更新它。

这里的许多主题都使用特殊的字形来显示分支图标等。您需要在终端程序中使用 [Nerd Font](https://github.com/ryanoasis/nerd-fonts) 或与 Powerline 兼容的字体，否则您会在符号所在的位置看到丑陋的破损框。

以下是 Nerd Fonts 和 Powerline 兼容字体的一些很好的来源：

- [Awesome Terminal Fonts](https://github.com/gabrielelana/awesome-terminal-fonts) - 一系列字体，其中包括一些漂亮的等宽图标。
- [Cascadia Code](https://github.com/microsoft/cascadia-code) - 微软的卡斯卡迪亚代码
- [Commit Mono](https://commitmono.com) - 中性编程字体。
- [Fantasque Awesome Font](https://github.com/ztomer/fantasque_awesome_powerline) - 一个漂亮的等宽字体，用 Font-Awesome、Octoicons 和 Powerline-Glyphs 进行了修补。
- [Fira Mono](https://github.com/mozilla/Fira) - Mozilla 的 Fira 类型系列。
- [Hack](http://sourcefoundry.org/hack/) - 另一种与电力线兼容的字体，专为源代码和终端使用而设计。
- [Input Mono](https://input.djr.com/) - 专为代码设计的字体系列。它提供等宽字体和比例字体，并包括电力线字形。
- [Iosevka](https://be5invis.github.io/Iosevka/) - Iosevka 是一款开源细长等宽无衬线和板衬线字体，灵感来自 [Pragmata Pro](http://www.fsd.it/fonts/pragmatapro.htm)、M+ 和 [PF DIN Mono](https://www.myfonts.com/fonts/parachute/pf-din-mono/)，旨在成为编程的理想字体。
- [Monaspace](https://github.com/githubnext/monaspace) - Monaspace 是五个可互换的类型系列，每个系列都打包成三种不同的格式。您可以并排安装所有这些；他们的姓氏因家族和格式而不同。
- [Monoid](http://larsenwork.com/monoid/) - Monoid 可进行定制和优化，即使在低分辨率显示器上，也可以在 15 像素行高下以类似位图的清晰度进行编码。
- [Mononoki](https://madmalik.github.io/mononoki/) - Mononoki 是 Matthias Tellen 设计的一种字体，旨在增强代码格式。
- [More Nerd Fonts](https://www.nerdfonts.com/font-downloads) - 另一个收集书呆子字体下载的网站。
- [Nerd fonts](https://github.com/ryanoasis/nerd-fonts) - 超过 20 种修补字体（超过 1,700 种变体）的集合以及适用于 Powerline、devicons 和 vim-devicons 的 fontforge 字体修补程序 python 脚本：包括 Droid Sans、Meslo、AnonymousPro、ProFont、Inconsolta 等。这些可以使用“brew”安装 - 执行“brew tap homebrew/cask-fonts && brew install --cask fontname”
- [Powerline patched font collection](https://github.com/powerline/fonts) - 大约十几种字体的集合，经过修补以包含电力线字形。
- [Spacemono](https://github.com/googlefonts/spacemono) - Google 全新原创等宽显示字体系列。
- [Victor Mono](https://rubjo.github.io/victor-mono/) - Victor Mono 是一种免费编程字体，具有半连接草书斜体、符号连字（!=、->>、=>、===、<=、>=、++）以及拉丁文、西里尔文和希腊字符。

如果您正在寻找要使用的新字体，请查看 [www.codingfont.com](https://www.codingfont.com/) - 它以括号式锦标赛的形式呈现编程字体，并让您不断选择两个呈现选项中最好的一个，直到找到最终字体。

## 教程

### 通用ZSH

- [A Beautifully Productive Terminal Experience](https://mikebuss.com/2014/02/02/a-beautiful-productive-terminal-experience/) - 使用 [iTerm 2](https://www.iterm2.com/#/section/home)、[ZSH](https://en.wikipedia.org/wiki/Z_shell)、[Prezto](https://github.com/sorin-ionescu/prezto)、[Tmux](https://tmux.github.io) 和 [Tmuxinator](https://github.com/tmuxinator/tmuxinator) 组合的教程打造极其高效的开发人员工作流程。
- [A Guide to ZSH Completion With Examples](https://thevaluable.dev/zsh-completion-guide-examples/) - 通过示例解释 ZSH 自动完成配置。
- [adamnorwood-zsh](https://github.com/adamnorwood/adamnorwood-zsh/) - 基于 [oh-my-posh](https://ohmyposh.dev/) 的简约但可读的 ZSH 设置。
- [Arch Linux's ZSH introduction](https://wiki.archlinux.org/index.php/zsh) - 实际上并不是 Arch 或 Linux 特定的。
- [GH](https://github.com/gustavohellwig/gh-zsh) - 在基于 debian/Ubuntu 的 Linux 上设置 ZSH。安装 [Powerlevel10k](https://github.com/romkatv/powerlevel10k)、[zsh-completions](https://github.com/zsh-users/zsh-completions)、[zsh-autosuggestions](https://github.com/zsh-users/zsh-autosuggestions)、 [fast-syntax-highlighting](https://github.com/zdharma-continuum/fast-syntax-highlighting/) 等。
- [How To Make an Awesome Custom Shell with ZSH](https://linuxstans.com/how-to-make-an-awesome-custom-shell-with-zsh/) - 关于如何安装和配置 ZSH shell 的初学者友好教程。
- [commandlinepoweruser.com](https://commandlinepoweruser.com/) - Wes Bos 介绍 ZSH 和 oh-my-zsh 的视频。
- [Profiling ZSH](https://ellie.wtf/notes/profiling-zsh) - 关于分析 ZSH 设置以优化启动时间的好文章。
- [rs-example](https://github.com/al-jshen/zshplug-rs-example) - 一个示例插件，展示 Rust 程序如何侦听和处理来自 ZSH 的命令。
- [Why ZSH is Cooler than your Shell](https://www.slideshare.net/jaguardesignstudio/why-zsh-is-cooler-than-your-shell-16194692) - 幻灯片共享演示文稿。
- [zephyr](https://github.com/mattmc3/zephyr) - Zephyr 使用内置的 Zsh 功能来设置更好的默认选项、完成、键绑定、历史记录等等。
- [ZSH for Humans](https://github.com/romkatv/zsh4humans) - ZSH 的交钥匙配置旨在开箱即用。它将一组精选的 ZSH 插件组合成一个连贯的整体，感觉像是一个成品，而不是一个 DIY 入门套件。
- [ZSH Pony](https://github.com/mika/zsh-pony) - 涵盖在没有框架的情况下自定义 ZSH。
- [ZSH tips by Christian Schneider](http://strcat.de/zsh/#tipps) - Christian Schneider 提供的 ZSH 技巧的详尽列表。
- [ZSH Setup by Easy-Cloud-in](https://github.com/Easy-Cloud-in/zsh-setup) - 强大的 Zsh 环境设置，包含 Oh My Posh 主题、基本插件和高级搜索功能。该存储库提供脚本来自动配置具有现代功能和美观的终端。需要基于 Debian 或 Ubuntu 的系统。
- [ZSH Unplugged](https://github.com/mattmc3/zsh_unplugged) - 如果您想消除使用框架但仍然可以轻松使用插件，这是一个很好的资源。

### 抗原

- [belak/zsh-utils](https://github.com/belak/zsh-utils) - 一组最小的 ZSH 插件，旨在低摩擦和低复杂性。
- [mgdm.net/weblog/zsh-antigen/](https://mgdm.net/weblog/zsh-antigen/) - Michael Maclean 关于从 oh-my-zsh 切换到抗原的文章。
- [Oh-my-zsh is the Disease and Antigen is the Vaccine](https://joshldavis.com/2014/07/26/oh-my-zsh-is-a-disease-antigen-is-the-vaccine/) - 乔什·戴维斯 (Josh Davis) 对 Antigen 的介绍。

### 哦我的Zsh

- [Configuration to use Hyper.js as a ZSH terminal with a Windows Subsystem Linux on windows 10, with Oh My Zsh and the Powerlevel10k theme](https://github.com/jkergal/hyperjs-wsl-zsh-powerlevel10k-config-on-windows/) - 如何在 WSL 上运行 Oh-My-ZSH。
- [Getting started with oh-my-zsh](https://medium.com/@dienbui/using-oh-my-zsh-f65be6460d3f) - Dien Bui 的 oh-my-zsh 初学者指南
- [How to Install and Configure Z Shell in Ubuntu](https://github.com/profpan396/how-to-install-and-configure-zshell) - Amar Pan 的文章将引导您完成安装和配置 ZSH 的过程，包括如何更改主题和启用省时的自动建议插件。
- [iTerm2 + Oh-My-ZSH: Supercharge Your Mac Terminal](https://catalins.tech/improve-mac-terminal) - Catalin Pit 有关 macOS 上 Oh-My-ZSH 入门的教程。
- [Learn Zsh in 80 Minutes macOS](https://www.youtube.com/watch?v=MSPu-lYF-A8) - Karl Hadwen 在 macOS 上使用 Oh My Zsh 的初学者指南
- [Oh-My-Zsh! A Work of CLI Magic](https://medium.com/wearetheledger/oh-my-zsh-made-for-cli-lovers-installation-guide-3131ca5491fb) - Michiel Mulders Ubuntu 安装指南
- [One Key Linux Setup](https://github.com/miracleyoo/one-key-linux-setup) - `zsh`、`oh-my-zsh`、`tmux`、`python` 支持和其他软件包的简单设置（仅限 ubuntu）。
- [Speeding Up My ZSH Shell](https://scottspence.com/posts/speeding-up-my-zsh-shell) - 使用 OMZ 加速 ZSH 的快速指南

### 普雷斯托

- [A Beautifully Productive Terminal Experience](https://mikebuss.com/2014/02/02/a-beautiful-productive-terminal-experience) - Mike Buss 关于使用 Prezto、[Tmux](https://tmux.github.io) 和 Tmuxinator 的博客文章。
- [Migrate from Oh-My-Zsh to Prezto](http://jeromedalbert.com/migrate-from-oh-my-zsh-to-prezto/) - Jerome Dalbert 关于迁移到 Prezto 的博客文章。

### 兹根

- [rad-shell](https://github.com/brandon-fryslie/rad-shell) - 功能丰富、速度快如闪电的 shell 设置，由 [ZSH](http://www.zsh.org/)、[Prezto](https://github.com/sorin-ionescu/prezto) 和 [Zgen](https://github.com/tarjoilija/zgen) 提供支持。

### Zinit（né zplugin）

- [BlaCk-Void-Zsh](https://github.com/black7375/BlaCk-Void-Zsh) - :crystal_ball：很棒的、可定制的 Zsh 入门套件 :stars::stars:。包括电力线、[fzf](https://github.com/junegunn/fzf) 集成、某些终端中的天气和图像查看。
- [zinit-configs](https://github.com/zdharma-continuum/zinit-configs) - 真实世界的配置文件（基本上是 `.zshrc` 文件的集合）保存 [zinit](https://github.com/zdharma-continuum/zinit) 调用。

### Windows 上的 ZSH

#### 超级控制台 - 仅限 Windows

- `ConEmu`/`zsh` 开箱即用，配置为在 `ConEmu` 重新启动后恢复以前打开的选项卡和 shell 工作目录
- 启动新的 SuperConsole 会话时，在干净环境和继承环境之间进行选择
- 自定义彩色方案，各种命令的彩色输出
- 包括`MSYS2`，预安装`zsh`和必要的软件，使用zsh-grml-config
- 使用 [Antigen](https://github.com/zsh-users/antigen) 进行 ZSH 主题和配置管理
- 启用了许多 ZSH 插件来激活补全、突出显示和历史记录，以实现最舒适的使用
- 配置了对“MSYS2”环境的适当“git”和“git lfs”支持的 Git-for-Windows 存储库，已安装“git”客户端。
- “git”的“ssh-agent”开箱即用，将您的密钥添加到“ConEmu/msys64/ConEmu/msys64/home/user/.ssh”目录
- 由于 [agkozak-zsh-prompt](https://github.com/agkozak/agkozak-zsh-prompt)，非阻塞 ZSH 提示状态更新
- 为“MSYS2”定制的命令未找到处理程序建议安装什么包
- 将“nano”设置为主编辑器，启用“nano”语法突出显示
- 添加到“ConEmu/msys64/3rdparty”的自定义帮助程序脚本

## 插件

- [1password](https://github.com/agpenton/1password-zsh-plugin) - 添加 [1Password](https://1password.com/) 功能，包括包装“op”命令的“opswd”命令。它采用服务名称作为参数，并将该服务的密码复制到剪贴板。
- [256color](https://github.com/chrissicool/zsh-256color) - 以 256 色增强终端环境。它会查看所选的“TERM”环境变量，并查看是否有相应的 ncurses' terminfo 以及 256 种颜色可用。结果是一个多色终端（如果可用）。
- [abbr](https://github.com/yachtida/zsh-abbr-plugin) - ZSH 的轻量级缩写扩展 — 灵感来自 [fish](https://fishshell.com)，专为速度而打造。
- [abbr-path](https://github.com/felixgravila/zsh-abbr-path) - 添加一些 oh-my-fish 主题中的 `theme_title_use_abbreviated_pa​​th` 参数的功能。
- [abbr-preview](https://github.com/cohml/zsh-abbr-preview) - 在您键入时预览 [abbr](https://github.com/olets/zsh-abbr) 缩写。
- [abbr](https://github.com/olets/zsh-abbr) - 受鱼壳启发，管理自动扩展缩写，当您点击空格时，缩写会内联扩展。
- [abbrev-alias](https://github.com/momo-lab/zsh-abbrev-alias) - 提供类似于`vim`的缩写扩展的功能。
- [actiona](https://github.com/matthieusb/act) - 使从命令行调用 [actiona](https://github.com/Jmgr/actiona) 脚本变得更容易。包括制表符补全。
- [activate-py-environment](https://github.com/se-jaeger/zsh-activate-py-environment) - 在遍历目录时自动检测并激活您的 python 环境（`poetry`、`virtualenv` 和 `conda`）。
- [adguard-helper](https://github.com/MohamedElashri/adguard-helper) - 简化与 [AdGuard VPN CLI](https://github.com/AdguardTeam/AdGuardVPNCLI) 的交互。它提供用户友好的命令，通过提供更直观的界面来减少记住复杂标志和命令的需要。
- [adonisjs](https://github.com/baliestri/adonisjs.plugin.zsh) - 用于跳过“ace”命令的“node”部分的插件。
- [ai-cmd](https://github.com/kylesnowschwartz/zsh-ai-cmd) - 具有幽灵文本预览的自然语言到 shell 命令。需要 `curl`、[`jq`](https://stedolan.github.io/jq/) 和 Anthropic API 密钥。
- [ai-cmd](https://github.com/shanemcd/ai-cmd) - 通过 [Claude Code](https://docs.anthropic.com/en/docs/claude-code) 或 [Ollama](https://ollama.ai/) 使用 LLM 从自然语言生成 shell 命令。
- [ai-commands](https://github.com/muePatrick/zsh-ai-commands) - 向 GPT (gpt-4-turbo-preview) 请求 CLI 命令以实现所描述的目标操作。
- [airpods-battery](https://github.com/louis-thevenet/zsh-airpods-battery/) - 通过蓝牙查找 AirPods 并将其电池充电状态设置为“$RPROMPT”。
- [aish](https://github.com/chr15m/aish) - OpenAI 的即时 shell 脚本解决方案就在您的提示符中。
- [alacritty](https://github.com/casonadams/alacritty-shell) - 控制 [alacritty](https://github.com/alacritty/alacritty/wiki/Color-schemes) 配色方案。
- [alehouse](https://github.com/sticklerm3/alehouse) - 包含 [brew](https://brew.sh) 命令的短别名，灵感来自“betterbrew”。
- [alias-finder](https://github.com/akash329d/zsh-alias-finder) - 当您使用之前已设置别名的命令时显示别名。有助于记住您过去定义的别名。为了速度而编写为纯 ZSH 脚本。
- [alias-maker](https://github.com/MefitHp/alias-maker) - 允许您从命令行轻松创建和管理别名。
- [alias-tips](https://github.com/djui/alias-tips) - 一个 [oh-my-zsh](https://ohmyz.sh/) 插件，可帮助记住您定义过的那些别名。
- [allclear](https://github.com/givensuman/zsh-allclear) - 当您“cd”进入“$HOME”时清除终端。
- [allergen](https://github.com/stanislas/allergen) - 与 Antigen 一起使用的自定义 ZSH 插件的集合。
- [almostontop](https://github.com/Valiev/almostontop) - 每次在 shell 中执行新命令之前清除先前的命令输出。受到 `bash` 的 [alwaysontop](https://github.com/swirepe/alwaysontop) 插件的启发。
- [alt-and-select](https://github.com/raisty/alt-and-select) - 将“alt-c”（复制）、“alt-”v（粘贴）、“alt-x”（剪切）键盘快捷键绑定到命令：“copy-region-as-kill”、“yank”和“kill-region”。将执行命令重新映射为“alt-shift-X”。
- [ansible](https://github.com/sparsick/ansible-zsh) - [Ansible](https://www.ansible.com/) 的插件。
- [ansimotd](https://github.com/yuhonas/zsh-ansimotd) - 当登录 shell 启动时添加老式的酷 ANSI 艺术。
- [ansiweather](https://github.com/fcambus/ansiweather) - 终端中的天气，带有 ANSI 颜色和 Unicode 符号。
- [antidote-use-omz](https://github.com/getantidote/use-omz) - 使 [oh-my-zsh](https://ohmyz.sh/) 与 [antidote](https://getantidote.github.io/) 无缝使用。
- [antigen-git-rebase](https://github.com/smallhadroncollider/antigen-git-rebase) - Antigen/ZSH 脚本可帮助“git”变基。
- [anyframe](https://github.com/mollifier/anyframe) - ZSH 的 `peco`/`percol`/`fzf` 包装插件。
- [apache2](https://github.com/voronkovich/apache2.plugin.zsh) - 添加用于管理 Apache2 的别名和函数。
- [apparix](https://github.com/micans/apparix) - 命令行目录书签，具有跳转到书签、子目录选项卡完成、远程列表等功能。
- [apple-touchbar](https://github.com/zsh-users/zsh-apple-touchbar) - 在 [iTerm 2](https://iterm2.com) 中添加 MacBook Pro 触摸栏支持。
- [appup](https://github.com/Cloudstek/zsh-plugin-appup) - 当检测到当前目录（例如您的应用程序）中存在“docker-compose.yml”或“Vagrantfile”时，添加“start”、“stop”、“up”和“down”命令。只需运行“up”并开始编码！
- [apt](https://github.com/GeoLMg/apt-zsh-plugin) - 对于带有“apt”包管理器的发行版。为您提供安装缺失的程序。
- [arc-prompt](https://github.com/dkryaklin/arc-zsh-plugin) - Arc VCS 提示与分支显示、状态缓存、操作模式检测、agnoster 主题支持和别名集成。
- [arc-search](https://github.com/michaelsousajr/zsh-arc-search) - 直接从终端使用 Arc 浏览器进行快速搜索。具有搜索词的 URL 编码功能。
- [arc](https://github.com/anton-rudeshko/zsh-arc) - 添加 Yandex 版本控制系统的别名。
- [arch-aptstyle](https://github.com/MRoldL001/arch-aptstyle) - 旨在为从这些发行版过渡到 arch 的用户提供 Debian/Ubuntu 风格的“apt”命令包装器。需要“yay”或“paru”才能实现完整功能。
- [archlinux (fourdim)](https://github.com/fourdim/zsh-archlinux) - 定义 Arch Linux 上“pacman”的辅助函数。
- [archlinux (junker)](https://github.com/Junker/zsh-archlinux) - 基于 oh-my-zsh [archlinux](https://github.com/ohmyzsh/ohmyzsh/blob/master/plugins/archlinux) 插件。定义辅助函数和别名。
- [arduino](https://github.com/raghur/zsh-arduino) - 添加脚本以从命令行构建、上传和监控 arduino 草图。需要 [`jq`](https://stedolan.github.io/jq/)。
- [artisan](https://github.com/jessarcher/zsh-artisan) - ZSH 的 Laravel `artisan` 插件可帮助您从项目树中的任何位置运行 `artisan`，并具有制表符补全功能！
- [asciidoctor](https://github.com/sparsick/asciidoctor-zsh) - AsciiDoctor 的插件。
- [asdf (kiurchv)](https://github.com/kiurchv/asdf.plugin.zsh) - 可扩展版本管理器 [asdf](https://github.com/asdf-vm/asdf) 的集成和补全，支持 Ruby、Node.js、Elixir、Erlang 等。
- [asdf (zimfw)](https://github.com/zimfw/asdf) - 初始化 [asdf](https://github.com/asdf-vm/asdf)，如果尚未安装，则使用 `git` 安装它。另外，如果您使用 [direnv](https://github.com/asdf-community/asdf-direnv) 插件，则按照插件 [pro-tips](https://github.com/asdf-community/asdf-direnv/#pro-tips) 的建议，绕过垫片。
- [asdf-direnv](https://github.com/redxtech/zsh-asdf-direnv) - [asdf](https://github.com/asdf-vm/asdf) 和 [direnv](https://github.com/asdf-community/asdf-direnv) 的集成和补全。
- [asdf-prompt](https://github.com/CurryEleison/zsh-asdf-prompt) - 提供可在提示中使用的功能，显示当前工具版本的版本信息。
- [ask-opencode](https://github.com/andreacasarin/zsh-ask-opencode) - 将 OpenCode AI 与您的 shell 集成，允许您使用自然语言生成 shell 命令。按“Ctrl+O”将命令行中的任何文本转换为优化的 shell 命令。
- [ask](https://github.com/Licheam/zsh-ask) - 用作 ChatGPT API 前端，使您能够仅使用“cURL”和“jq”直接从 ZSH shell 与 ChatGPT 交互。
- [assistant](https://github.com/tarball0/zsh-assistant) - 使用 ollama 回答有关命令的问题。
- [assume-role](https://github.com/weizard/assume-role) - 允许您轻松承担 AWS IAM 角色。包括竣工情况。
- [async](https://github.com/mafredri/zsh-async) - 用于在 ZSH 中运行异步任务的库，无需任何外部工具。允许您运行多个异步作业，强制执行唯一作业（同一作业的多个实例将不会运行），刷新所有当前正在运行的作业并创建多个工作人员（每个工作人员都有自己的作业）。
- [atom-plugin](https://github.com/CorradoRossi/oh-my-zsh-atom-plugin) - 基于 [Sublime](https://github.com/valentinocossar/sublime) 插件，让您可以从 [iTerm 2](https://iterm2.com) 启动 [Atom](https://atom.io) 中的文件或文件夹。
- [atuin](https://github.com/ellie/atuin) - 用 SQLite 数据库替换现有的 shell 历史记录，并记录命令的附加上下文。此外，它还通过 Atuin 服务器提供机器之间可选且完全加密的历史记录同步。
- [aur-install](https://github.com/redxtech/zsh-aur-install) - 用于从 AUR 安装软件包的小插件。
- [auto-color-ls](https://github.com/gretzky/auto-color-ls) - 自动列出带有“colorls”的目录。
- [auto-fu.zsh](https://github.com/hchbaw/auto-fu.zsh) - 自动完整单词和列表选择。最初由 y.fujii <y-fujii at mimosa-pudica.net> 编写的 incr-0.2.zsh。
- [auto-ls (commanda-panda)](https://github.com/commanda-panda/zsh-auto-ls) - 如果“cd”上可用，则自动运行“ls”或“color-ls”。
- [auto-ls (desyncr)](https://github.com/desyncr/auto-ls) - 当 cd 到新目录时自动“ls”。
- [auto-notify](https://github.com/MichaelAquilina/zsh-auto-notify) - 当长时间运行的任务完成时自动发出通知。
- [auto-nvm](https://github.com/manlao/zsh-auto-nvm) - 自动切换到给定目录中指定的节点版本。
- [auto-pnpm-use](https://github.com/brunomacedo/zsh-auto-pnpm-use) - 自动加载`.nvmrc`或`.npmrc`中指定的节点版本。
- [auto-venv (skylor0tang)](https://github.com/Skylor-Tang/auto-venv) - 自动激活当前目录或其父目录中的Python虚拟环境。
- [autocomplete](https://github.com/marlonrichert/zsh-autocomplete) - 在您键入时自动列出补全内容，并提供直观的键绑定以供选择和插入它们。
- [autodark (cravend)](https://github.com/cravend/autodark) - 在用户指定的浅色和深色主题之间切换。仅适用于 macOS。
- [autodark (vbwx)](https://github.com/vbwx/zsh-autodark) - 如果启用了暗模式（仅限 macOS），则切换到另一个终端配置文件。
- [autodotenv](https://github.com/nocttuam/autodotenv) - 当您“cd”到包含“.env”文件的目录时，将提示您加载变量。
- [autoenv-extended](https://github.com/zpm-zsh/autoenv) - [zsh-autoenv](https://github.com/Tarrasch/zsh-autoenv) 插件的扩展版本。
- [autoenv](https://github.com/hyperupcall/autoenv) - 基于目录的环境。
- [autojump](https://github.com/wting/autojump) - 一个可学习的“cd”命令 - 从命令行轻松导航目录。安装 autojump-zsh 以获得最佳结果。
- [automated-actions](https://github.com/Fynardo/zsh-automated-actions) - 为 [automated-actions](https://github.com/app-sre/automated-actions) CLI 提供别名。
- [autopair](https://github.com/hlissner/zsh-autopair) - 一个 ZSH 插件，用于自动关闭、删除和跳过匹配的分隔符。仅在 ZSH 5.0.2 或更高版本上测试。
- [autoquoter](https://github.com/ianthehenry/zsh-autoquoter) - 一个 `zle` 小部件（“zsh 插件”），它将自动在某些命令的参数周围加上引号。
- [autosuggestions-plugin](https://github.com/jumbojett/zsh-autosuggestions-plugin) - 🐟 ZSH 中的 [Fish](https://fishshell.com/) 式自动建议。
- [autosuggestions](https://github.com/zsh-users/zsh-autosuggestions) - [Fish](https://fishshell.com/) 类似 ZSH 的快速/不显眼的自动建议。
- [autoswitch-virtualenv](https://github.com/MichaelAquilina/zsh-autoswitch-virtualenv) - ZSH 插件可在遍历目录时自动切换 python virtualenvs 和 pipelinevs。自动检测 [pipenv](https://pypi.org/project/pipenv/) 和 [poetry](https://python-poetry.org/) 项目。
- [autoupdate-antibody](https://github.com/spikespaz/autoupdate-antibody-zsh) - [Antibody](https://getantibody.github.io) 插件管理器的 [autoupdate-antigen](https://github.com/unixorn/autoupdate-antigen.zshplugin) 的一个分支，增加了与静态加载配合的能力。
- [autoupdate-antigen](https://github.com/unixorn/autoupdate-antigen.zshplugin) - [Antigen](https://github.com/zsh-users/antigen) 不会像 [oh-my-zsh](https://ohmyz.sh/) 那样进行自动更新。该插件添加了“antigen”、“antigen”和配置中加载的包的自动更新。
- [autoupdate-oh-my-zsh-plugins](https://github.com/TamCore/autoupdate-oh-my-zsh-plugins) - [oh-my-zsh](https://ohmyz.sh/) 不会自动更新非核心插件，该插件会自动更新 `$ZSH_CUSTOM` 目录中的 `git` 存储库。
- [autovenv (linnnus)](https://github.com/linnnus/autovenv) - 进入其父目录时自动激活 Python 虚拟环境。
- [autovenv (snovra-dev)](https://github.com/snovra-dev/zsh-autovenv) - 进入其父目录时自动激活 Python 虚拟环境。
- [aws-cli-mfa](https://github.com/joepjoosten/aws-cli-mfa-oh-my-zsh) - 基于 sweharris 的 [aws-cli-mfa](https://github.com/sweharris/aws-cli-mfa) 的 AWS CLI MFA 插件。支持在配置文件中指定“mfa_device”。
- [aws-mfa](https://github.com/FreebirdRides/oh-my-zsh-aws-mfa) - 用于使用 AWS MFA 的插件。
- [aws-plugin](https://github.com/pookey/zsh-aws-plugin) - 为“aws”命令添加辅助函数。包括 MFA 和“假设角色”助手。
- [aws-upload](https://github.com/borracciaBlu/aws-upload-zsh) - 使用“aws-upload”提高您的工作效率。
- [aws-vault (blimmer)](https://github.com/blimmer/zsh-aws-vault) - [aws-vault](https://github.com/99designs/aws-vault) 插件。包括制表符补全。
- [aws-vault (zsh-contrib)](https://github.com/zsh-contrib/zsh-aws) - [aws-vault](https://github.com/99designs/aws-vault) 与“tmux”中的每个窗口 AWS 配置文件支持集成。
- [aws-vault-profiles](https://github.com/jonscheiding/zsh-plugin-aws-vault-profiles) - 将 [aws-vault](https://github.com/99designs/aws-vault) 的使用与 `$AWS_PROFILE` 环境变量集成的插件。
- [aws](https://github.com/apachler/zsh-aws) - 从原始的 [oh-my-zsh](https://ohmyz.sh/) [aws](https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins/aws) 分叉。包括“awscli”的补全以及一些用于管理 AWS 配置文件并在提示中显示它们的实用程序。
- [aws2](https://github.com/drgr33n/oh-my-zsh_aws2-plugin) - 提供对 [awscli](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) 版本 2 的完成支持以及一些用于管理 AWS 配置文件并在提示中显示它们的实用程序。
- [awsmultiaccount](https://github.com/acidix/zsh-awsmultiaccount) - 管理 AWS 配置文件并在多账户组织中担任角色。它提供了辅助函数，可以轻松地在 AWS 配置文件之间切换并在不同账户中承担 OrganizationAccountAccessRole。需要 `aws` cli 和 [jq](https://stedolan.github.io/jq/)
- [awsp](https://github.com/suonto/awsp-zsh-plugin) - ZSH 的 AWS 配置文件管理。受到 oh-my-zsh 的 [aws](https://github.com/ohmyzsh/ohmyzsh/blob/master/plugins/aws/aws.plugin.zsh) 插件的启发。显示当前活动的 AWS 配置文件的详细信息。
- [awsssh](https://github.com/raisedadead/zsh-awsssh) - 列出、选择并“ssh”进入 EC2 实例。
- [awsume](https://github.com/Sordie/AWSume) - 该插件可以显示当前的 [awsume](https://github.com/trek10inc/awsume) 配置文件。
- [azcli](https://github.com/dmakeienko/azcli) - 用于使用 Azure cli 工具的帮助程序。
- [azure-keyvault](https://github.com/milespossing/Azure-Keyvault-Zsh) - 使通过 cli 使用 Azure keyvault 变得更加简洁。
- [azure-subscription](https://github.com/dmakeienko/azure-subscription-prompt) - 显示有关 Azure 当前订阅和租户的信息。
- [banner](https://github.com/drkhsh/zsh-banner) - 在会话启动时显示 ANSI/ASCII 艺术作品。
- [baseballfunfacts](https://github.com/richardmoyer/baseballfunfacts) - 在 shell 中随机打印与棒球相关的“有趣的事实”。取决于安装的“fortune”和“cowsay”。
- [bash-quote](https://github.com/jtprog/bash-quote) - 从 Bash.im 获取随机报价。
- [bash](https://github.com/chrissicool/zsh-bash) - 使 ZSH 更加兼容 Bash。它重新定义了源命令，使其更像“bash”。它还启用“bash”补全。
- [bat](https://github.com/fdellwing/zsh-bat) - 为 [bat](https://github.com/sharkdp/bat) 用户添加一些帮助程序别名。
- [battery_state](https://github.com/Jactry/zsh_battery_state) - 在右侧提示中显示电池状态。
- [bd](https://github.com/Tarrasch/zsh-bd) - 跳回特定目录，而不执行“cd ../../..”。
- [bepoptimist](https://github.com/sheoak/zsh-bepoptimist/) 重新映射法语 [bépo](http://bepo.fr/wiki/Accueil) 键盘的 vi 模式。
- [bitbucket-git-helpers](https://github.com/unixorn/bitbucket-git-helpers.plugin.zsh) - 添加帮助程序脚本以允许您创建 bitbucket PR 或在当前分支中打开目录。
- [bitwarden (casonadams)](https://github.com/casonadams/bitwarden-cli) - 使用 [fzf](https://github.com/junegunn/fzf) 的 [Bitwarden](https://bitwarden.com/download/) CLI 模糊查找器。需要 [jq](https://stedolan.github.io/jq/)。
- [bitwarden (game4move78)](https://github.com/Game4Move78/zsh-bitwarden) - 添加管理 [bitwarden](https://bitwarden.com/) 会话的功能。
- [bitwarden (kalsowerus)](https://github.com/kalsowerus/zsh-bitwarden) - 打开包含您的 [Bitwarden](https://bitwarden.com/) 金库项目的 [fzf](https://github.com/junegunn/fzf) 小部件。选择一个项目后，用户名或密码将被写入 shell 或复制到剪贴板中。需要 [fzf](https://github.com/junegunn/fzf)、`jq` 和 `bitwarden`。
- [blackbox](https://github.com/StackExchange/blackbox) - Stack Exchange 的工具包，用于将密钥/凭证安全地存储在“git”存储库中。
- [bob](https://github.com/wintermi/zsh-bob) - [bob](https://github.com/MordechaiHadad/bob) 插件是一个跨平台且易于使用的 Neovim 版本管理器。
- [bofh](https://github.com/fundor333/bofh) - 添加显示随机bofh命运的功能。
- [bol](https://github.com/ikhurramraza/bol) - 当您打开终端窗口时打印随机报价。
- [boss-docker](https://github.com/bossjones/boss-docker-zsh-plugin) - 管理 macOS 上的“docker”。
- [boss-git](https://github.com/bossjones/boss-git-zsh-plugin) - 为“git”添加一些方便的别名。
- [branch-manager](https://github.com/elstgav/branch-manager) - 用于管理“git”分支的插件。
- [brave](https://github.com/troykelly/oh-my-zsh-brave) - 管理 [Brave](https://brave.com) 个人资料。有了这个插件，您可以通过使用brave命令后跟配置文件名称来启动具有特定用户配置文件的Brave浏览器。该插件还实现了配置文件名称的自动完成功能，因此您不必手动输入整个配置文件名称。
- [brew (rhuang2014)](https://github.com/rhuang2014/brew) - [Homebrew](https://brew.sh/) 包管理器的独立插件。
- [brew (wintermi)](https://github.com/wintermi/zsh-brew) - [Homebrew](https://brew.sh/) 包管理器的简单插件。
- [brew-install](https://github.com/marceloclp/zsh-brew-install) - 在 WSL 上安装并加载 [brew](https://brew.sh)。
- [brew-switcher](https://github.com/fielding/zsh-brew-switcher) - 在 Apple Silicon Mac 上根据当前活动架构、arm64 或 x86_64 自动切换 Homebrew 安装。
- [browse-commit](https://github.com/adolfoabegg/browse-commit) - 允许您从命令行在浏览器中打开任何提交。
- [bruse](https://github.com/aubreypwd/zsh-plugin-bruse) - 可以轻松“brew link”不同版本的包。
- [btrfs-snapper](https://github.com/crisis1er/zsh-btrfs-snapper) - 用于 openSUSE Tumbleweed 上的 btrfs 文件系统管理和 snapper 快照控制的插件 — 原生工具中不提供的丰富命令、安全防护和过滤视图。
- [bumblebee](https://github.com/Niverton/zsh-bumblebee-plugin) - 用于在命令行中切换前置“optirun”的插件。
- [bw](https://github.com/begris/bw-zsh-plugin) - 提供格式化选项，并可通过 Bitwarden [CLI](https://bitwarden.com/download/) 轻松访问存储在 [Bitwarden](https://bitwarden.com) 中的凭证。该插件尝试在每个操作之前检索有效会话，因此不需要事先显式登录。
- [bws](https://github.com/elogiclab/zsh-bws) - 简化并改进从 [Bitwarden](https://bitwarden.com) 秘密管理器检索秘密。
- [c](https://github.com/sebastiangraz/c) - 添加一些“git”快捷方式。
- [calc (arzzen)](https://github.com/arzzen/calc.plugin.zsh) - ZSH 的计算器。
- [calc (sam-programs)](https://github.com/Sam-programs/zsh-calc) - 允许您运行没有前缀的数学计算。
- [calibre-zaw-source](https://github.com/junkblocker/calibre-zaw-source) - [Calibre - 电子书管理](https://calibre-ebook.com/) [zaw]来源(https://github.com/zsh-users/zaw)
- [caniuse](https://github.com/walesmd/caniuse.plugin.zsh) - 为 ZSH 添加[我可以使用](https://caniuse.com) 支持。
- [caper-bush](https://github.com/kobylinski/caper-bush) - 通过使用 AI 生成简明的、上下文感知的分阶段更改摘要，以提供深思熟虑的提交消息，增强了 Git 的选项卡自动完成功能。需要 OpenAI 密钥“jq”和“yq”。
- [careful_rm](https://github.com/MikeDacre/careful_rm) - “rm”的包装器，添加垃圾/回收和有用的警告。
- [case](https://github.com/rtuin/zsh-case) - 一个 ZSH 插件，添加两个别名“tolower”和“toupper”来切换输出情况。
- [ccline](https://github.com/jianshuo/ccline) - 在 zsh 提示符处输入一个想法（无命令，无前缀），然后从 Claude 或 Codex 获得答案。如果答案包含 shell 命令，请确认一次并运行它们。
- [ccusage](https://github.com/hydai/zsh-ccusage) - 直接在终端提示符中显示来自“ccusage”CLI 工具的实时 AI 使用成本。
- [cd-gitroot](https://github.com/mollifier/cd-gitroot) - 一个 ZSH 插件，用于 `cd` 到 `git` 存储库根目录。
- [cd-ls](https://github.com/zshzoo/cd-ls) - 在“cd”之后自动显示“ls”。
- [cd-reminder](https://github.com/bartboy011/cd-reminder) - 当“cd”进入指定目录时显示提醒。
- [cd-reporoot](https://github.com/P4Cu/cd-reporoot) - 一个 ZSH 插件，用于“cd”到当前存储库签出的根目录。
- [cd-ssh](https://github.com/jeffwalter/zsh-plugin-cd-ssh) - 当您不小心“cd”到服务器时，“ssh”到服务器。
- [cdbk](https://github.com/MikeDacre/cdbk) - 一个 ZSH 插件，允许轻松创建命名目录 - 您想要的任何目录的快捷方式。
- [cdc](https://github.com/evanthegrayt/cdc) - 可以更轻松地将目录更改为用户定义的目录列表的子目录。包括制表符补全、会话历史记录以及“pushd”、“popd”和“dirs”等效项。
- [cdh](https://github.com/johncassol/cdh) - 允许用户管理和浏览他们访问过的目录的历史记录。它维护目录的历史文件，并提供几个与该历史记录交互的命令。
- [cdhist](https://github.com/joknarf/cdhist) - cd 历史/子目录/locatedir 导航。简单的cd历史记录，别名内置`cd`添加`cd`历史记录，快速切换到已经访问过的目录，可以使用`locate`，`mlocate`或`plocate`快速cd到任何目录
- [cdr](https://github.com/willghatch/zsh-cdr) - 为 ZSH 轻松设置“cdr”。
- [change-case](https://github.com/mtxr/zsh-change-case) - 用于在命令行中快速切换大小写的插件。 ：太阳镜：
- [cheatsheet](https://github.com/0b10/cheatsheet) - 用于轻松查看、创建和编辑备忘单的插件。
- [check-deps](https://github.com/zpm-zsh/check-deps) - ZSH 插件的帮助程序，允许它们展示如何安装任何缺少的依赖项。如果您使用 [zpm](https://github.com/zpm-zsh/zpm) 框架，则适用于 Debian（以及 Ubuntu 等衍生产品）、Arch 及其衍生产品、Node.js 和 ZSH 插件。
- [chgo](https://github.com/sbfaulkner/chgo-plugin-zsh) - 克隆“chruby”，经过修改，可以轻松在多个 Go 版本之间切换。
- [claude-code-shell](https://github.com/ArielTM/zsh-claude-code-shell) - 使用 [Claude Code](https://claude.ai/claude-code) 将自然语言注释翻译为 shell 命令。
- [claude-shell](https://github.com/myk-org/claude-shell) - 使用 Claude AI 提供智能 shell 帮助。它提供了七个强大的功能来增强您的命令行体验：自然语言命令翻译、命令解释、错误修复、智能历史搜索以及用于高级回滚分析的 Kitty 终端集成。
- [claude](https://github.com/HundredAcreStudio/zsh-claude) - 使用 Claude AI 为 ZSH 提供 AI 支持的命令建议和解释。通过简单的按键绑定获取智能 shell 命令帮助。将自然语言转换为可执行的 shell 命令，或获取复杂命令的详细解释 - 一切都直接在您的终端中通过 Claude AI 集成实现。
- [clean-history](https://github.com/Automaat/zsh-clean-history) - 智能 ZSH 历史记录清理插件，可根据相似性分析自动删除拼写错误和失败的命令。删除与成功命令类似的失败命令，查找与常见变体类似的罕见命令，自动捕获命令成功/失败，调整相似性阈值和行为并在清理之前创建备份。
- [clean-project](https://github.com/wwilsman/zsh-clean-project) - 从项目中删除文件（默认情况下自动）。对于防止“.DS_Store”和“Thumbs.db”文件弄乱目录很有用。
- [cleanzip](https://github.com/Xeferis/cleanzip) - 帮助创建不含不应包含在其中的数据的 zip 文件。
- [clipboard](https://github.com/zpm-zsh/clipboard) - 添加跨平台帮助函数来访问系统剪贴板。适用于 macOS、X11（和 Wayland）和 Cygwin。
- [cmd-status](https://github.com/BlaineEXE/zsh-cmd-status) - 报告命令的状态，包括返回代码和持续时间。
- [cmd-time](https://github.com/TomfromBerlin/zsh-cmd-time) - 收集命令的执行时间并将结果导出到可在其他地方使用的变量。它与内置的[REPORTTIME](http://zsh.sourceforge.net/Doc/Release/Parameters.html)函数类似，但也略有不同。与设置“REPORTTIME”不同，它考虑用户和系统时间，而不仅仅是 CPU 时间。
- [cmdtime](https://github.com/tom-auger/cmdtime) - 显示从 [timer](https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins/timer) 插件分叉到终端的命令的持续时间。
- [code-review](https://github.com/xorkevin/code-review-zsh) - 在 `git merge-base target_branch base_branch` 和 `target_branch` 上启动 `git difftool`。
- [code-stats](https://gitlab.com/code-stats/code-stats-zsh) - 计算按键次数并将统计数据记录到 [Code::Stats](https://codestats.net/)。
- [codex](https://github.com/tom-doerr/zsh_codex) - 使您能够在命令行中使用 OpenAI 强大的 Codex AI。
- [coffee-time](https://github.com/gakimball/zsh-coffee-time) - 添加“caf”别名，该别名运行“caffeinate -dims”。额外的标志使一切保持清醒：系统、驱动器和显示器。
- [color-logging](https://github.com/p1r473/zsh-color-logging) - 提供了一个非常易于使用的日志记录库，其中包含 Pushbullet 和 Pushover 的通知，为“cat”和“ls”等工具着色，并提供了一个颜色库。
- [colored-man-pages-mod](https://github.com/zuxfoucault/colored-man-pages_mod) - 从 [ohmyzsh/ohmyzsh/plugins/colored-man-pages](https://github.com/ohmyzsh/ohmyzsh/blob/master/plugins/colored-man-pages/colored-man-pages.plugin.zsh) 分叉。对“man”输出进行着色。
- [colored-man-pages](https://github.com/ael-code/zsh-colored-man-pages) - 为“手册”页面着色。
- [colored-man-pages-plus](https://github.com/diverdale/colored-man-pages-plus) - 通过精心策划的真彩色主题、OSC-8 链接和自动亮/暗检测，按角色对“手册”页面进行语义着色。
- [colorize-functions](https://github.com/Freed-Wu/zsh-colorize-functions) - 为 ZSH 的函数着色。
- [colorize](https://github.com/zpm-zsh/colorize) - 对各种程序的输出进行着色。
- [colorls](https://github.com/Kallahan23/zsh-colorls) - 定义一些 colorls 函数的一些有用的快捷方式。
- [colors (Tarrasch)](https://github.com/Tarrasch/zsh-colors) - 可以更轻松地从 CLI 为文本着色。 `red foo` 就可以了。
- [colors (zpm-zsh)](https://github.com/zpm-zsh/colors) - ZSH 的增强颜色。
- [command-execution-timer](https://github.com/olets/command-execution-timer) - 显示执行交互式 shell 命令所需的时间。
- [command-not-found (freed-wu)](https://github.com/Freed-Wu/zsh-command-not-found) - 使用 ZSH 的“command-not-found”包在找不到命令时提供建议安装的包。
- [command-not-found (tarrasch)](https://github.com/Tarrasch/zsh-command-not-found) - [oh-my-zsh](https://ohmyz.sh) [command-not-found](https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins/command-not-found) 插件的镜像，因此您不必包含所有 oh-my-zsh。
- [command-note](https://github.com/KKRainbow/zsh-command-note.plugin) - 记录复杂的命令并对其进行注释。
- [command-time](https://github.com/popstas/zsh-command-time) - 显示 ZSH 和 [powerlevel9k](https://github.com/bhilburn/powerlevel9k) 中长命令的执行时间。与内置的`REPORTTIME`类似，但仅当用户+系统时间>=`REPORTTIME`时输出。
- [communism](https://github.com/victoria-riley-barnett/Communism/) - 显示当天马克思的名言。
- [compe](https://github.com/tamago324/compe-zsh) - 添加 [nvim-compe](https://github.com/hrsh7th/nvim-compe) 的补全。
- [conda (themysciradata)](https://github.com/ThemysciraData/conda.plugin.zsh) - 添加函数为 [conda](https://conda.io) 提供提示段并为某些基本函数提供别名。
- [conda (wardhanisukoco)](https://github.com/wardhanisukoco/zsh-plugin-conda/) - 自动加载 `conda` 并提供检测主题中使用的 `conda` 版本的功能。
- [conda-init](https://github.com/commiyou/conda-init-zsh-plugin) - 清理环境变量，这样 [conda](https://conda.io) 就不会弄乱 `tmux`。
- [condaenv](https://github.com/saravanabalagi/zsh-plugin-condaenv) - 提供一个 `condaenv_prompt_info` 函数，它返回当前的 `conda` 环境名称。
- [confer](https://github.com/SleepyBag/zsh-confer) - 尝试自动查找程序配置文件，以便您可以执行诸如“conf vim”之类的操作来编辑“vim”配置文件。
- [containers](https://github.com/redxtech/zsh-containers) - 在您安装的 [podman](https://podman.io) 和 [docker](https://docker.com) 命令之间提供别名和更好的互操作性。
- [copy-pasta](https://github.com/ChrisPenner/copy-pasta) - 像在 GUI 中一样将文件复制并粘贴到终端中。
- [copyzshell](https://github.com/rutchkiwi/copyzshell) - 一个 ZSH 插件，用于通过“ssh”将 shell 配置复制到另一台计算机。
- [cordova](https://github.com/andredestro/cordova-zsh-plugin) - 受 git 风格快捷方式（gco、gcb 等）启发，为 [Apache Cordova](https://cordova.apache.org/) 命令提供方便的别名。
- [cowsay](https://github.com/phucisstupid/cowsay.zsh) - 每次打开终端时都会显示一个带有“cowsay”的笑话。
- [crash](https://github.com/molovo/crash) - 为 ZSH 添加正确的错误处理、异常和 try/catch。
- [crayon-syntax](https://github.com/gsemet/crayon-syntax-zsh) - 适用于 Wordpress 的 Crayon 插件的 ZSH 语法突出显示。
- [cros-auto-notify](https://github.com/D3STY/cros-auto-notify-zsh) - 当长时间运行的任务完成时自动发出通知。适用于 macOS 和 Linux（如果安装了“hterm-notify”）。
- [crystal](https://github.com/veelenga/crystal-zsh) - [Crystal](https://github.com/crystal-lang/crystal) 的插件。
- [cvideo](https://github.com/aubreypwd/zsh-plugin-cvideo) - 使用“ffmpeg”快速压缩视频。
- [cwebp](https://github.com/adi-li/zsh-cwebpb) - 使用 Google 的“cwebp”工具以批处理模式将常见图像格式（JPG、PNG、GIF、BMP、TIFF）转换为 WebP 格式。
- [cycle-fav-dirs](https://github.com/cibinmathew/cycle-fav-dirs) - 一个可以循环浏览您最喜欢的目录的插件。
- [cycle-jobs](https://github.com/aemonge/zsh-cycle-jobs) - ZSH 循环作业插件是一个简单但功能强大的工具，它允许您使用单个键盘快捷键循环浏览后台作业，从而增强您的终端工作流程。该插件对于经常使用多个后台进程的开发人员和系统管理员特别有用。
- [czhttpd](https://github.com/jsks/czhttpd) - 一个用 99.9% 纯 ZSH 编写的简单 http 服务器。
- [databricks](https://github.com/SlavaYakovenko/zsh-databricks) - 增强了 Zsh 的 Databricks CLI 集成，具有方便的别名和配置文件管理。
- [dce](https://github.com/Onnokh/zsh-dce) - 帮助您快速导航到 Docker 容器，而不会丢失当前文件夹上下文。
- [ddev](https://github.com/voronkovich/ddev.plugin.zsh) - 用于设置 PHP 开发环境的 [ddev](https://github.com/drud/ddev) 工具的 ZSH 插件。
- [declare-zsh](https://github.com/z-shell/declare-zsh) - `.zshrc` 中的 [zinit](https://github.com/zdharma-continuum/zinit) 命令的解析器。它允许您从命令行对“.zshrc”执行以下操作 - 启用和禁用插件添加或删除片段。
- [deepx](https://github.com/GetAmbush/deepx-zsh-plugin) - 有用且有趣的命令集合，可改善工作流程和生活质量。
- [deer](https://github.com/Vifon/deer) - ZSH 的文件导航器深受 [ranger](https://ranger.github.io/) 的启发。
- [def](https://github.com/thevinter/def) - 允许您在您选择的任何目录中指定并运行默认命令。
- [defer](https://github.com/romkatv/zsh-defer) - 推迟执行“zsh”命令，直到“zsh”没有其他事情可做并正在等待用户输入。其预期目的是分阶段“zsh”启动。它的工作原理与 [zinit](https://github.com/zdharma-continuum/zinit) 中的 Turbo 模式类似。
- [deja-vu](https://github.com/justyntemme/zsh-deja-vu) - 根据运行的目录记录和检索命令历史记录。永远不要忘记几周前在项目文件夹中运行的复杂的“docker”或“git”命令。
- [delete-prompt](https://github.com/aoyama-val/zsh-delete-prompt) - ZSH 小部件用于删除当前行内的提示文本。当从网络或自述文件执行粘贴的命令时，它非常有用。检测到前导非字母数字字符 + 空格作为提示。
- [deno (cowboyd)](https://github.com/cowboyd/zsh-deno) - 有用的 [deno](https://deno.land/) 别名和设置。
- [deno (tricked-dev)](https://github.com/Tricked-dev/deno-zsh-plugin) - 如果尚未安装 deno，则在启动时自动将 [deno](https://deno.land/) 安装到 `$HOME/.deno`。
- [depot-tools](https://github.com/kuoe0/zsh-depot-tools) - 用于安装 chromium depot_tools 的简单 [oh-my-zsh](https://ohmyz.sh/) 插件。安装此插件会自动将所有 chromium depot_tools 添加到您的“$PATH”中。
- [dev](https://github.com/sbfaulkner/dev-plugin-zsh) - 提供 Shopify 内部开发工具的轻量级版本
- [dietpi](https://github.com/unixorn/dietpi.plugin.zsh) - 当您登录到运行 [dietpi](https://dietpi.com) 的计算机时，将 [dietpi](https://dietpi.com) 的实用程序添加到您的“$PATH”（并包含别名以使用“sudo”自动运行它们）。
- [diff-so-fancy](https://github.com/z-shell/zsh-diff-so-fancy) - 自动安装 [diff-so-fancy](https://github.com/so-fancy/diff-so-fancy) 并启用它在 ZSH 和 `git` 中的使用。
- [ding](https://github.com/jessetipton/ding) - 当长时间运行的 shell 命令完成时播放通知声音。
- [diractions](https://github.com/AdrieanKhisbe/diractions) - 允许您将简短的逻辑/助记名称映射到目录以快速访问它们，或在其中执行操作。
- [dirbrowse](https://github.com/giovannilupi/dirbrowse/) - [oh-my-zsh](https://ohmyz.sh) 中的 [dirbrowse](https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins/dircycle) 插件的定制版本。
- [dircolors-solarized (joel-porquet)](https://github.com/joel-porquet/zsh-dircolors-solarized) - Solarized dircolors 插件，可选择深色或浅色终端背景。
- [dircolors-solarized (pinelibg)](https://github.com/pinelibg/dircolors-solarized-zsh) - 启用 [GNU ls 的 Solarized 颜色主题](https://github.com/seebi/dircolors-solarized)。
- [directory-history](https://github.com/tymm/zsh-directory-history) - ZSH 的每个目录历史记录，以目录敏感的方式实现向前/向后导航以及子字符串搜索。
- [direnv](https://github.com/ptavares/zsh-direnv) - 用于安装和加载 [direnv](https://github.com/direnv/direnv.git) 的插件。受到 [zsh-pyenv](https://github.com/mattberther/zsh-pyenv) 的启发。
- [dirrc](https://github.com/gmatheu/shell-plugins) - 当存在于您通过“cd”进入的目录中时执行“.dirc”。
- [dirstack](https://github.com/gepoch/oh-my-zsh-dirstack) - 用于在单行上显示 dirstack 信息的插件。
- [diskfree](https://github.com/alex-crouch/zsh-diskfree/) - 在提示中显示磁盘上的可用空间。
- [diskguard](https://github.com/TomfromBerlin/diskguard) - ZSH 中写入操作的智能磁盘空间监控。
- [doas (anatolykopyl)](https://github.com/anatolykopyl/doas-zsh-plugin) - 按两次“ESC”即可轻松为当前或以前的命令添加“doas”前缀。
- [doas (senderman)](https://github.com/Senderman/doas-zsh-plugin) - 按两次“ESC”即可轻松为当前或以前的命令添加“doas”前缀。
- [docker-aliases](https://github.com/webyneter/docker-aliases) - 日常使用的“Docker”别名。
- [docker-compose](https://github.com/sroze/docker-compose-zsh-plugin) - 在提示符中显示“docker”容器状态。
- [docker-helpers](https://github.com/unixorn/docker-helpers.zshplugin) - “docker”帮助程序脚本的集合。
- [docker-machine](https://github.com/asuran/zsh-docker-machine) - ZSH 的 docker-machine 插件。
- [docker-run](https://github.com/rawkode/zsh-docker-run) - 返回“自然”运行命令，我们将处理容器。
- [dogesh](https://github.com/keithhamilton/oh-my-dogesh) - 狗化插件。
- [doppler](https://github.com/lsdcapital/zsh-doppler) - 在环境变量的 shell 提示符中显示当前的 [Doppler](https://doppler.com) 项目和配置。
- [dot-up](https://github.com/toku-sa-n/zsh-dot-up) - 将 `...`、`....`、`.....` 等转换为 `cd` 命令以导航父目录。
- [dotbare](https://github.com/kazhala/dotbare) - 在 [fzf](https://github.com/junegunn/fzf) 的帮助下进行交互式点文件管理。
- [dotfiles](https://github.com/vladmyr/dotfiles-plugin) - 使用“git”使您的点文件在多台计算机上保持同步。
- [dotpyvenv](https://github.com/jeanpantoja/dotpyvenv) - 当您“cd”进入目录时，自动切换到位于名为“.pyvenv”的目录中的Python虚拟环境（您之前使用virtualenv程序创建的）。
- [download](https://github.com/aubreypwd/zsh-plugin-download) - 使用“aria2c”下载文件的帮助程序。
- [dropbox](https://github.com/zpm-zsh/dropbox) - ZSH 的 [dropbox](https://www.dropbox.com/) 插件，提供 `dropbox-cli` 和 `dropbox-uploader` 命令。
- [drupal](https://github.com/yhaefliger/zsh-drupal) - 为常见任务添加别名，并为“drush”添加制表符完成功能。受到 [Artisan](https://github.com/jessarcher/zsh-artisan) 的启发。
- [dune-quotes](https://github.com/brokendisk/dune-quotes) - 随机沙丘报价生成器插件。
- [dune.zsh](https://github.com/bitpeppr/dune.zsh) - 该插件可随机显示大量沙丘报价中的报价。
- [duration](https://github.com/rtakasuke/zsh-duration) - 如果命令持续时间超过用户可设置的运行时间，则显示命令持续时间。
- [dwim](https://github.com/oknowton/zsh-dwim) - 尝试预测您下一步想要做什么。它提供了一个键绑定 (control-u)，它将用您接下来要运行的命令替换当前（或上一个）命令行。
- [easy-motion](https://github.com/IngoHeimbach/zsh-easy-motion) - ZSH 的 [vim-easymotion](https://github.com/easymotion/vim-easymotion) 端口。
- [ec2ssh](https://github.com/h3poteto/zsh-ec2ssh) - 列出 EC2 实例并轻松通过“ssh”登录实例。
- [edit-select](https://github.com/Michael-Matta1/zsh-edit-select) - 为 ZSH 命令行带来完整的文本编辑器体验：复制、剪切、粘贴、撤消/重做、键入替换以及本机 X11/Wayland 剪贴板集成，并支持 Shift+箭头和鼠标选择。
- [editing-workbench](https://github.com/commiyou/zsh-editing-workbench) - 添加理智、复杂的命令行编辑（例如增量历史词完成）。
- [edward cli](https://github.com/matthieusb/zsh-edward) - 为 [edward CLI 微服务启动器](https://github.com/yext/edward) 添加智能补全和 Alises。
- [elixir](https://github.com/gusaiani/elixir-oh-my-zsh) - 添加 Elixir、IEX、Mix、Kiex 和 Phoenix 的快捷方式。
- [emacs (cowboyd)](https://github.com/cowboyd/zsh-emacs) - 让 Emacs 成为 CLI 操作的默认设置，例如编辑 git 提交消息；设置方便的别名。
- [emacs (flinner)](https://github.com/Flinner/zsh-emacs) - 使用 Emacs 守护程序功能，允许用户快速打开框架，无论它们是通过“ssh”连接在终端中打开，还是在同一主机上打开 X 框架。
- [emoji-cli](https://github.com/b4b4r07/emoji-cli) - :scream：命令行上的表情符号补全。
- [emoji-fzf](https://github.com/pschmitt/emoji-fzf.zsh) - 可配置的 ZSH 插件，用于出色的 [emoji-fzf](https://github.com/noahp/emoji-fzf)。它深受 [emoji-cli](https://github.com/b4b4r07/emoji-cli) 的启发。
- [emojis](https://github.com/MichaelAquilina/zsh-emojis) - 通过方便的变量将大量 ASCII 艺术表情符号添加到您的环境中。
- [enhancd](https://github.com/b4b4r07/enhancd) - 一个简单的工具，通过记住用户访问的所有目录并将其用于路径名解析来提供增强的“cd”命令。
- [ensure-kube-context](https://github.com/do-i-need-a-username/ensure-kube-context) - 确保将“--context”标志传递给各种 Kubernetes 命令，例如“kubectl”、“cilium”、“stern”等。
- [env-secrets](https://github.com/singular0/zsh-env-secrets) - 自动从安全存储后端检索机密，并在 shell 初始化期间将其导出为环境变量。这样就无需在纯文本配置文件中存储敏感信息。适用于“pass”和 macOS 钥匙串。
- [envrc](https://github.com/fabiogibson/envrc-zsh-plugin) - 如果在目录中找到“.envrc”文件，则自动加载和卸载环境变量。
- [escape-backtick](https://github.com/bezhermoso/zsh-escape-backtick) - 双击“`”时快速插入转义反引号。
- [evalcache](https://github.com/mroth/evalcache) - 缓存二进制初始化命令（如“eval "$(hub alias -s)"”）的输出，通过从缓存加载而不是重新运行每个新的 shell 会话来帮助缩短 shell 启动时间。
- [evil-registers](https://github.com/zsh-vi-more/evil-registers) - 扩展 ZLE `vi` 命令以远程访问 `vim` 和 `nvim` 编辑器的命名寄存器以及系统选择和剪贴板。
- [exa (DarrinTisdale)](https://github.com/DarrinTisdale/zsh-aliases-exa) - 启用许多扩展 [exa](https://github.com/ogham/exa) 的别名，这是 `ls` 的现代替代品。
- [exa (mohamedelashri)](https://github.com/MohamedElashri/exa-zsh) - 添加 [exa](https://github.com/ogham/exa) 的别名，这是 `ls` 的现代替代品。
- [exa (ptavares)](https://github.com/ptavares/zsh-exa) - 安装并加载 [exa](https://github.com/ogham/exa.git)。
- [exa (ritchies)](https://github.com/RitchieS/zsh-exa/) - 添加别名以使使用 [exa](https://github.com/ogham/exa.git) 更容易。
- [exa (todie)](https://github.com/todie/exa.plugin.zsh) - [exa](https://github.com/ogham/exa) 的集成和补全，是 `ls` 的现代替代品。
- [exa (zap-zsh)](https://github.com/zap-zsh/exa) - 覆盖常用命令以使用 [ogham/exa](https://github.com/ogham/exa) 代替。
- [exa (zplugin)](https://github.com/zplugin/zsh-exa) - 将 `ls` 替换为 [ogham/exa](https://github.com/ogham/exa)。
- [exa (zshell)](https://github.com/z-shell/zsh-exa) - 将 `ls` 替换为 [ogham/exa](https://github.com/ogham/exa)。
- [exa-ls (zpm-zsh)](https://github.com/zpm-zsh/ls) - ls 的 Zsh 插件。
- [exa-ls](https://github.com/birdhackor/zsh-exa-ls-plugin) - 添加别名，以便您可以使用 [exa](https://github.com/ogham/exa) 作为 `ls` 和 `tree` 的直接替代品。
- [exercism](https://github.com/fabiokiatkowski/exercism.plugin.zsh) - [exercism.io](http://exercism.io/) 的插件。
- [expand-ealias](https://github.com/zigius/expand-ealias.plugin.zsh) - 用空格展开特定别名。
- [expand-space](https://github.com/spqw/zsh-alias-expand-space) - 按空格键时展开命令位置“zsh”别名。
- [expand](https://github.com/MenkeTechnologies/zsh-expand) - 使用空格键扩展常规别名、全局别名、不正确的拼写和短语、通配符、历史扩展和 $parameters。
- [expander](https://github.com/ianthehenry/zsh-expander) - 一个 `zle` 小部件，允许您编写自定义扩展器并使用 [fzf](https://github.com/junegunn/fzf) 选择它们。
- [explain-shell (brokentoaster)](https://github.com/brokentoaster/zsh-explainshell) - 使用 [lynx](https://lynx.browser.org/) 在 [explainshell.com](https://explainshell.com) 上查找当前命令行。
- [explain-shell (gmatheu)](https://github.com/gmatheu/shell-plugins) - 打开 [explainshell.com](https://explainshell.com) 上的命令。
- [extend-history](https://github.com/xav-b/zsh-extend-history) - 通过为历史记录中的每个命令添加退出代码来扩展命令历史记录。
- [ez-cmd](https://github.com/akgarhwal/ez-cmd) - 通过提供易于使用的快捷方式和别名来简化和简化常见的命令行任务。
- [ez-compinit](https://github.com/mattmc3/ez-compinit) - 包装 `compinit`，排队对 `compdef` 的调用，并将真正的 `compinit` 调用挂接到在 `.zshrc` 末尾运行的事件。这样你就可以获得尽早调用“compinit”的所有好处，而没有任何缺点。
- [eza (clavelm)](https://github.com/clavelm/eza-omz-plugin) - 将 `ls` 替换为 [eza-community/eza](https://github.com/eza-community/eza)。
- [eza (mohamedelashri)](https://github.com/MohamedElashri/eza-zsh) - 添加 [eza](https://github.com/eza-community/eza) 的别名，这是 `ls` 的现代替代品。
- [eza (twopizza9621536)](https://github.com/twopizza9621536/zsh-eza) - 将 `ls` 替换为 [eza-community/eza](https://github.com/eza-community/eza)。
- [eza (z-shell)](https://github.com/z-shell/zsh-eza) - 将 `ls` 替换为 [eza-community/eza](https://github.com/eza-community/eza)。
- [eza (zsh-contrib)](https://github.com/zsh-contrib/zsh-eza) - [eza](https://github.com/eza-community/eza) 插件，具有 Catppuccin 和 Rose Pine 主题、智能默认值和完整别名支持。
- [eza-ls](https://github.com/birdhackor/zsh-eza-ls-plugin) - 添加别名，允许 [eza](https://github.com/eza-community/eza) 充当“ls”和“tree”的直接替代品。
- [f-shortcuts](https://github.com/zpm-zsh/f-shortcuts) - 使用“F1”到“F12”键创建快捷工具栏。
- [fancy-ctrl-z](https://github.com/mdumitru/fancy-ctrl-z) - 对 [oh-my-zsh](http://ohmyz.sh/) 中的版本进行了破解，因此其他框架的用户不必导入所有 [oh-my-zsh](https://ohmyz.sh)。
- [fast-alias-tips](https://github.com/decayofmind/zsh-fast-alias-tips) - 帮助记住您定义并忘记的别名。移植自 [djui/alias-tips](https://github.com/djui/alias-tips)。 [sei40kr/zsh-fast-alias-tips](https://github.com/sei40kr/zsh-fast-alias-tips) 的活跃分支。
- [fast-syntax-highlighting](https://github.com/zdharma-continuum/fast-syntax-highlighting) - 优化和改进了“zsh-users/zsh-syntax-highlighting”——更好的响应时间、可切换的突出显示主题。
- [fastcache](https://github.com/QuarticCat/zsh-fastcache) - 缓存命令输出以缩短 shell 启动时间。
- [fauna](https://github.com/manojuppala/zsh-fauna) - 每次打开新终端或重新启动 zsh 时，都会显示丰富多彩的高品质 ANSI 艺术作品，并支持濒危和灭绝动物的 256 色终端。一次通过一个终端课程了解野生动物保护！
- [fav](https://github.com/ddnexus/fav) - ZSH/[fzf](https://github.com/junegunn/fzf) 插件使添加和调用重要目录的命名收藏夹变得非常容易。
- [favorite-directories](https://github.com/seletskiy/zsh-favorite-directories) - 快速跳转到您最喜欢的目录。
- [fd-plugin](https://github.com/MohamedElashri/fd-zsh) - 添加 [fd](https://github.com/sharkdp/fd) 的别名，这是 `find` 的现代替代品。
- [fd](https://github.com/aubreypwd/zsh-plugin-fd) - 使用 [fzf](https://github.com/junegunn/fzf) 浏览目录。
- [ffexport](https://github.com/Pakrohk/ffexport.plugin.zsh) - 轻量级 ZSH 原生视频导出管理器 — 配置文件驱动的 [FFmpeg](https://www.ffmpeg.org) 导出、持久 ZSH 选项卡完成、配置文件导入/导出以及 Instagram 和 YouTube 工作流程的安全默认设置。
- [figures](https://github.com/zpm-zsh/figures) - ZSH 的 Unicode 符号。
- [firebase (rmrs)](https://github.com/rmrs/firebase-zsh) - 在提示中添加一个指示符，表明您位于包含“firebase.json”文件（又名“firebase 项目”）的目录中。
- [firebase (seqi)](https://github.com/Seqi/firebase-zsh) - 在 Firebase 项目目录或子目录中显示当前工作项目或项目别名。
- [fishysave](https://github.com/dariogliendo/fishysave.zsh) - 直接从终端会话保存和更新函数和别名。
- [fixnumpad-osx](https://github.com/zackintosh/fixnumpad-osx.plugin.zsh) - 使 ZSH 能够识别 Apple 键盘的小键盘键。
- [flow-cli](https://github.com/Data-Wise/flow-cli) - ADHD 友好的 ZSH 工作流程工具。使用“work”在 10 秒内开始工作，使用“win”跟踪多巴胺的胜利情况，使用“dash”保持方向。包括适用于 git、R、Quarto 和 Claude Code 的智能调度程序。
- [flow-plugin](https://github.com/sandstorm/oh-my-zsh-flow-plugin) - 该插件使“flow”命令在 TYPO3 Flow 发行版的每个子目录中可用。
- [flutter-zsh-shortcuts](https://github.com/dizzpy/flutter-zsh-shortcuts) - 为 flutter 命令添加干净的别名。
- [fnm (dominik-schwabe)](https://github.com/dominik-schwabe/zsh-fnm) - 安装并加载 [快速节点管理器 (fnm)](https://github.com/Schniz/fnm)（如果缺少）。
- [fnm (sukkaw)](https://github.com/SukkaW/zsh-fnm) - 提供对 Node.js 版本管理器 [`fnm`](https://fnm.vercel.app) 的增强。
- [fnm (wintermi)](https://github.com/wintermi/zsh-fnm) - 用于快速简单的 Node.js 版本管理器 [fnm](https://github.com/Schniz/fnm) 的帮助插件。
- [forgit](https://github.com/wfxr/forgit) - `git` 的实用工具，利用模糊查找器 [fzf](https://github.com/junegunn/fzf)。
- [fuckmit](https://github.com/mingeme/zsh-fuckmit) - 为 [fuckmit](https://github.com/mingeme/fuckmit) 命令行工具（人工智能驱动的“git”提交消息生成器）提供有用的别名和函数。
- [functional](https://github.com/Tarrasch/zsh-functional) - ZSH 高阶函数。
- [fuzzy-search-and-edit](https://github.com/seletskiy/zsh-fuzzy-search-and-edit) - ZSH 插件，用于模糊搜索文件并立即在匹配的行上打开匹配的文件。
- [fuzzy-wd](https://github.com/spodin/zsh-fuzzy-wd) - 添加对使用 [WD](https://github.com/ohmyzsh/ohmyzsh/blob/master/plugins/wd) 插件扭曲的目录的模糊搜索。
- [fz](https://github.com/changyuheng/fz) - 将模糊搜索无缝添加到 [z](https://github.com/rupa/z) 的选项卡补全中，并让您轻松地在历史记录中的目录之间跳转。
- [fzf (gimbo)](https://github.com/gimbo/fzf.zsh) - 在 ZSH 中使用 [fzf](https://github.com/junegunn/fzf) 的帮助程序。需要 [brew.sh](https://brew.sh)。
- [fzf (scaryrawr)](https://github.com/scaryrawr/fzf.zsh) - 受 [PatrickF1/fzf.fish](https://github.com/PatrickF1/fzf.fish) 启发，添加了 [fzf](https://github.com/junegunn/fzf) 的键绑定。
- [fzf (unixorn)](https://github.com/unixorn/fzf-zsh-plugin/) - 启用 [fzf](https://github.com/junegunn/fzf) 历史记录和文件搜索。
- [fzf (zsh-contrib)](https://github.com/zsh-contrib/zsh-fzf) - 使用漂亮的 Catppuccin 和 Rose Pine 颜色主题配置 [fzf](https://github.com/junegunn/fzf)，添加文件和目录选择器键绑定，并连接您喜欢的编辑器和文件管理器 - 因此模糊查找从第一天起就感觉很自然。
- [fzf-copyq-clipboard](https://github.com/magidc/fzf-copyq-clipboard-zsh-plugin) - 添加对 [CopyQ](https://hluk.github.io/CopyQ/) 的 [fzf](https://github.com/junegunn/fzf) 支持。
- [fzf-dir-navigator](https://github.com/KulkarniKaustubh/fzf-dir-navigator) - 这是一个很酷且用户友好的 ZSH 目录导航插件，使用 [fzf](https://github.com/junegunn/fzf)，允许用户从任何地方切换到任何目录。它还维护最近访问的目录的历史记录。此外，您可以使用热键在 shell 会话中的目录之间来回移动。
- [fzf-fasd](https://github.com/wookayin/fzf-fasd) - 集成了 [fzf](https://github.com/junegunn/fzf) 和 [fasd](https://github.com/clvv/fasd) --- `z` 的 tab 补全与 `fzf` 的模糊搜索！
- [fzf-finder](https://github.com/leophys/zsh-plugin-fzf-finder) - 该插件可以与 [fzf](https://github.com/junegunn/fzf) 和（可选）[bat](https://github.com/sharkdp/bat) 和 [fd](https://github.com/sharkdp/fd) 进行很酷的搜索键绑定。返回到“find”和“cat”。在本地子目录树中搜索文件。
- [fzf-git-worktree](https://github.com/banyan/zsh-fzf-git-worktree) - 通过 [fzf](https://github.com/junegunn/fzf) 集成管理 `git` 工作树。
- [fzf-history-search](https://github.com/joshskidmore/zsh-fzf-history-search) - 将 `Ctrl+R` 替换为 [fzf](https://github.com/junegunn/fzf) 驱动的历史搜索，其中包括日期/时间。
- [fzf-it](https://github.com/micakce/fzf-it) - 使用 [fzf](https://github.com/junegunn/fzf) 功能使任何命令交互式包装。
- [fzf-marks](https://github.com/urbainvaes/fzf-marks) - 使用模糊查找器 [fzf](https://github.com/junegunn/fzf) 在 `bash` 和 `zsh` 中创建、导航和删除书签的小脚本。
- [fzf-nav](https://github.com/ivomac/zsh-fzf-nav) - 使用 [fzf](https://github.com/junegunn/fzf) 定义交互式文件/目录导航器。提供多种导航模式、git 集成和可自定义操作。
- [fzf-packagemanager](https://github.com/goarano/zsh-fzf-packagemanager) - 添加使用 [fzf](https://github.com/junegunn/fzf) 通过各种包管理器安装工具的命令。支持“apt”、“brew”和“dnf”。
- [fzf-pass](https://github.com/smeagol74/zsh-fzf-pass) - 使用 [fzf](https://github.com/junegunn/fzf) 和 [pass](https://www.passwordstore.org/) 更好地处理密码。
- [fzf-plugin](https://github.com/Atlas34/fzf-plugin) - [oh-my-zsh](https://github.com/ohmyzsh/ohmyzsh) 的 [fzf](https://github.com/junegunn/fzf) 插件已提取，因此可以轻松与其他插件管理器一起使用。
- [fzf-prezto](https://github.com/lildude/fzf-prezto) - Prezto 插件可查找 [fzf](https://github.com/junegunn/fzf) 的安装位置并启用其自动完成和键绑定。该插件用作 Prezto `zstyle` 配置选项。
- [fzf-tab-widgets](https://github.com/tom-power/fzf-tab-widgets) - 添加 [fzf-tab](https://github.com/Aloxaf/fzf-tab) 小部件。
- [fzf-tab](https://github.com/Aloxaf/fzf-tab) - 将 ZSH 的默认补全选择菜单替换为 [fzf](https://github.com/junegunn/fzf)。
- [fzf-tools](https://github.com/happycod3r/fzf-tools) - 为“alias”、“find”、“ls”、“man”、“printenv”等命令提供函数、别名和键绑定，这些命令旨在通过默认通过 [fzf](https://github.com/junegunn/fzf) 进行过滤来增强命令行工作流程，使您能够快速查找文件、从历史记录中搜索和运行命令、运行许多受支持类型的脚本、浏览“git”提交等。
- [fzf-utils](https://github.com/redxtech/zsh-fzf-utils) - 提供杀死进程并使用 [fzf](https://github.com/junegunn/fzf) 在路径中查找的功能。
- [fzf-widgets](https://github.com/ytet5uy4/fzf-widgets) - 为 [fzf](https://github.com/junegunn/fzf) 添加一些 ZLE 小部件。
- [fzfsh](https://github.com/ethan605/fzfsh) - 添加 `chezmoi`、`docker`、`git`、`kubectl` 和 `pass` 的 [fzf](https://github.com/junegunn/fzf) 插件。
- [fzy](https://github.com/aperezdc/zsh-fzy) - 使用 [fzy](https://github.com/jhawthorn/fzy) 进行某些模糊匹配操作的插件。
- [gcloud (johnstonskj)](https://github.com/johnstonskj/zsh-gcloud-plugin) - 将 gcloud SDK 添加到您的“$PATH”。
- [gcloud (wintermi)](https://github.com/wintermi/zsh-gcloud) - 查找已安装的 gcloud SDK 并在其中获取 zsh 文件以及 zsh 完成文件。
- [gcloud-project](https://github.com/avivl/gcloud-project) - 轻松选择 Google Cloud 项目。
- [gdbm](https://github.com/zdharma-continuum/zgdbm) - 添加 GBBM 作为插件。
- [gentoo](https://github.com/MattiaG-afk/gentoo-ohmyzsh) - 添加一些别名和函数以与 Gentoo Linux 配合使用。
- [geometry-datetime](https://github.com/desyncr/geometry-datetime) - [Geometry](https://github.com/geometry-zsh/geometry) 日期时间插件。在提示符中显示日期时间（`date` unix 命令）。
- [geometry-hydrate](https://github.com/jedahan/geometry-hydrate) - [Geometry](https://github.com/geometry-zsh/geometry) 插件提醒您补充水分。
- [geometry-npm-package-version](https://github.com/drager/geometry-npm-package-version) - [Geometry](https://github.com/geometry-zsh/geometry) 插件，用于显示当前文件夹的 npm 包版本。
- [geometry-rust-version](https://github.com/drager/geometry-rust-version) - [Geometry](https://github.com/geometry-zsh/geometry) 插件，用于在存在 `.rs` 或 `Cargo.toml` 时显示当前文件夹的 Rust 版本。
- [get-jquery](https://github.com/voronkovich/get-jquery.plugin.zsh) - 用于从 [code.jquery.com](https://code.jquery.com) 快速下载 jQuery 库的插件。
- [ghost-zeus](https://github.com/fontno/ghost_zeus) - 允许您将 [zeus](https://github.com/burke/zeus) 与普通的 Rails 命令一起使用。
- [ghq-gh-wiki-clone](https://github.com/shmokmt/ghq-gh-wiki-clone) - 一个 ZSH 插件，在 `ghq get` / `ghq clone` 获取存储库后，自动将其 GitHub Wiki（当 wiki 有页面时）克隆到该存储库的 .wiki 子目录中。
- [ghq-worktree](https://github.com/liquidcatmofu/zsh-ghq-worktree) - 集成 `ghq`、[fzf](https://github.com/junegunn/fzf) 和 `git worktree` 以最大限度地减少多存储库开发中的上下文切换成本。
- [gimbo-git](https://github.com/gimbo/gimbo-git.zsh) - [oh-my-zsh](https://ohmyz.sh/) [gi​​t 插件](https://github.com/robbyrussell/oh-my-zsh/blob/master/plugins/git/git.plugin.zsh) 别名的子集，加上一些新的别名，以及一些方便的函数。
- [gimme](https://github.com/folixg/gimme-ohmyzsh-plugin) - 使用 [gimme](https://github.com/travis-ci/gimme/) 管理 [Go](https://golang.org/) 安装。
- [git-acp](https://github.com/MenkeTechnologies/zsh-git-acp) - 将当前命令行作为提交消息，然后一键运行 `git pull`、`git add`、`git commit` 和 `git push`。
- [git-add-remote](https://github.com/caarlos0/git-add-remote) - 轻松将上游远程添加到您的“git”分支。
- [git-aliases (mdumitru)](https://github.com/mdumitru/git-aliases) - 对 [oh-my-zsh](http://ohmyz.sh/) 中的版本进行了破解，因此其他框架的用户不必导入所有 [oh-my-zsh](https://ohmyz.sh)。
- [git-aliases (peterhurford)](https://github.com/peterhurford/git-aliases.zsh) - 为常用的“git”命令的组合创建许多有用的别名。
- [git-aliases (remino)](https://github.com/remino/omz-plugin-git-aliases) - 将所有 `git xyz` 命令别名为 `gxyz`。还将“g”别名为“git”。
- [git-arc](https://github.com/jlduran/git-arc-oh-my-zsh-plugin) - 为 FreeBSD 开发工具 [git-arc](https://github.com/freebsd/freebsd-src/tree/main/tools/tools/git) 添加别名和函数。
- [git-branches](https://github.com/Schroefdop/git-branches) - 创建一个“git”分支菜单，您可以切换到该菜单，而无需输入长分支名称。
- [git-clean-branch](https://github.com/gobriansteele/git-clean-branch) - 清理死去的“git”分支。
- [git-cleanbranches](https://github.com/wu9o/ohmyzsh-cleanbranches) - 一个强大的统一清理工具，用于“git”分支，使用 [fzf](https://github.com/junegunn/fzf) 查找所有可以安全删除的分支。
- [git-commit-prefixer](https://github.com/dvigo/git-commit-prefixer) - 向“git”提交消息添加可配置前缀和可选图标（支持样式、图标主题和交互式选择）
- [git-commit-shortcuts](https://github.com/ashsajal1/git-commit-shortcuts) - 提供创建带有表情符号前缀和一致格式的标准化“git”提交消息的快捷方式。
- [git-complete-urls](https://github.com/rapgenic/zsh-git-complete-urls) - 增强 `git` 补全功能，以将剪贴板中的任何 URL 包含在远程补全中（例如，来自 `git clone`）。
- [git-extra-commands](https://github.com/unixorn/git-extra-commands) - 额外的“git”帮助程序脚本打包为插件。
- [git-flow-avh](https://github.com/nekofar/zsh-git-flow-avh) - 为 `git-flow` 命令添加短别名。
- [git-fuzzy](https://github.com/bigH/git-fuzzy) - `git` 的 CLI 接口严重依赖于 [fzf](https://github.com/junegunn/fzf)。
- [git-gen](https://github.com/sharif3271/git-gen) - 处理“git”批量分支删除和创建操作。
- [git-graph](https://github.com/Maks0u/git-graph) - 添加一个漂亮的“git”图表。
- [git-is-clean](https://github.com/aubreypwd/zsh-plugin-git-is-clean) - 该函数将返回 true 或 false，具体取决于它是否发现您的 git 存储库脏或不脏。
- [git-it-on](https://github.com/peterhurford/git-it-on.zsh) - 添加了在 GitHub 上当前分支中打开文件夹的功能。
- [git-lfs](https://github.com/nekofar/zsh-git-lfs) - 为 `git-lfs` 命令添加短别名。
- [git-patch](https://github.com/marvinroman/oh-my-zsh-git-patch-plugin) - 向 oh-my-zsh `git` 插件添加自定义函数和别名。
- [git-plugin (dark-kitt)](https://github.com/dark-kitt/zsh-git-plugin) - 显示当前目录和 git 分支的 `git` 集成。
- [git-plugin (rcruzper)](https://github.com/rcruzper/zsh-git-plugin) - 为 `git` 添加一些功能。
- [git-plugin-cheatsheet](https://github.com/rhorno/oh-my-zsh-git-plugin-cheatsheet) - 显示 `git` oh-my-zsh 插件可用的别名和函数。
- [git-profile](https://github.com/nemezo/zsh-git-profile) - 通过根据目录路径或存储库远程 URL 自动切换“user.name”、“user.email”和签名密钥来管理 ZSH 中的多个“git”帐户。切勿再次以错误的身份推送提交。
- [git-prompt-enhanced](https://github.com/LFabre/zsh-git-prompt-enhanced) - 提供有关“git”存储库的更详细信息。
- [git-prompt-useremail](https://github.com/mroth/git-prompt-useremail) - 添加 `git` user.email 的提示提醒。
- [git-prompt-watcher](https://github.com/shields/git-prompt-watcher) - 当 git 状态更改时自动更新提示，使用“fswatch”实时监控存储库文件。
- [git-prune (diazod)](https://github.com/diazod/git-prune) - 允许您删除已合并到本地“git”存储库中和/或合并到远程源“git”存储库中的所有分支。
- [git-prune (seinh)](https://github.com/Seinh/git-prune) - 简化删除“git”存储库中合并分支的插件。
- [git-scripts](https://github.com/packruler/zsh-git-scripts) - 添加 `git-squash-branch` 和 `git-remove-merged` 命令。
- [git-secret](https://github.com/sobolevn/git-secret) - 一个 bash 工具，用于将您的私人数据存储在“git”存储库中。
- [git-smart-commands](https://github.com/seletskiy/zsh-git-smart-commands) - 添加额外的 `git` 命令以使一些常见的 `git` 用法更加高效。
- [git-smart-commends-wrapper](https://github.com/jelek21/omz-git-smart-commands) - 包装 [git-smart-commands](https://github.com/seletskiy/zsh-git-smart-commands) 以使其与 [oh-my-zsh](https://ohmyz.sh) 插件系统兼容。
- [git-status](https://github.com/AyoubMounim/zsh-git-status/) - 使用有关当前“git”存储库的信息公开函数。
- [git-switch-branch-skim](https://github.com/okhiroyuki/zsh-git-switch-branch-skim) - 允许您使用 [skim](https://github.com/lotabout/skim) 切换 `git` 分支
- [git-sync](https://github.com/caarlos0-graveyard/zsh-git-sync) - 一个 ZSH 插件，用于同步“git”存储库并清理它们。
- [git-to-jj](https://github.com/elithrar/zsh-git-to-jj) - 帮助您在使用“git”命令时逐步学习[Jujutsu](https://github.com/jj-vcs/jj)（又名“jj”）瓷器。
- [git-worktree (alexiszamanidis)](https://github.com/alexiszamanidis/zsh-git-worktree) - 包装一些“git worktree”操作以实现简单性和生产力。包括 [fzf](https://github.com/junegunn/fzf) 工具。
- [git-worktree (trthomps)](https://github.com/trthomps/git-worktree-zsh-plugin) - 通过裸存储库支持增强了“git worktree”管理。该插件提供了使用“git”工作树的便捷命令，可以轻松地同时在多个分支上工作。
- [git-worktree-manager](https://github.com/tmbtech/zsh-git-worktree-manager) - 轻松管理“git”工作树。同时处理多个分支时简化您的工作流程。
- [git-worktrees](https://github.com/egyptianbman/zsh-git-worktrees) - 使“git”工作树更加实用。包括制表符补全。
- [git-wt](https://github.com/fingergohappy/git-wt) - 一个 ZSH 原生的 `git` 工作树工作流插件。
- [git](https://github.com/davidde/git) - 替换库存 [oh-my-zsh](https://ohmyz.sh/) `git` 插件。提供了很多有用的别名和函数。替换默认插件的动机源于这样一个事实：它存在一些不一致之处，使得一些流行的命令相当不直观，因此该插件使别名保持一致。
- [gitbutler](https://github.com/batuhan0sanli/gitbutler-omz) - [GitButler](https://gitbutler.com/) 的插件 — CLI 别名、Git 保护盾以及标准 OMZ 主题和 Powerlevel10k 的提示集成。
- [gitcd (SukkaW)](https://github.com/SukkaW/zsh-gitcd) - 将命令添加到“git clone”存储库并将“cd”添加到结果目录中。
- [gitcd (viko16)](https://github.com/viko16/gitcd.plugin.zsh) - 克隆后自动“cd”到“git”工作目录。
- [gitfast](https://github.com/tevren/gitfast-zsh-plugin) - 更新了 [oh-my-zsh](https://ohmyz.sh/) `gitfast` 插件的分支。
- [gitgo](https://github.com/ltj/gitgo) - 从命令行（仅限 macOS）在浏览器中打开 GitHub/GitLab 存储库。
- [github-folders](https://github.com/buzuloiu/zsh-github-folders) - 为您组织 GitHub 结账。
- [github](https://github.com/shakir-abdo/zsh-github-plugin) - 嵌入在 [oh-my-zsh](https://ohmyz.sh/) 中的原始 [GitHub 插件](https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins/github) 的分支。
- [gitignore](https://github.com/voronkovich/gitignore.plugin.zsh) - 用于创建“.gitignore”文件的插件。
- [gitio (denysdovhan)](https://github.com/denysdovhan/gitio-zsh) - 一个 ZSH 插件，用于使用 [git.io](https://git.io) 生成 GitHub 短 URL。
- [gitio (nicolodiamante)](https://github.com/nicolodiamante/gitio) - 使用 [git.io](https://git.io/) 来缩短 `git` url。
- [gitsync](https://github.com/washtubs/gitsync) - ZSH 插件可改进一个人在多台机器上的同一存储库上进行开发的工作流程。
- [goenv (bbenne10)](https://github.com/bbenne10/goenv) - 与 Python 的 virtualenvwrapper 类似地管理“$GOPATH”。
- [goenv (cda0)](https://github.com/CDA0/zsh-goenv/) - 用于安装、更新和加载 `goenv` 的插件。
- [goenv (heyvito)](https://github.com/heyvito/goenv.zsh) - 自动读取当前目录中的`.goenv`文件并设置`GOPRIVATE`环境变量。
- [going_places](https://github.com/or17191/going_places) - 一个有助于使用、创建和维护 shell 位置列表的插件。
- [golang](https://github.com/wintermi/zsh-golang) - 添加适用于 Go 编程语言工具链的工具。
- [golinks](https://github.com/slessans/oh-my-zsh-golinks-plugin) - 从您的终端启动 golinks。
- [gpg-agent](https://github.com/axtl/gpg-agent.zsh) - 该插件在设置 GPG 代理以充当 macOS 上的 SSH 代理时尝试做正确的事情。
- [gpg-crypt](https://github.com/Czocher/gpg-crypt) - ZSH 插件用于就地加密和解密文件或目录。
- [gpg](https://github.com/marvinroman/oh-my-zsh-gpg-plugin) - 添加有用的别名以使用“gpg”。
- [gpt](https://github.com/antonjs/zsh-gpt) - 启用从命令行查询 ChatGPT。
- [grep2awk](https://github.com/joepvd/grep2awk) - ZLE 小部件将 `grep` 命令转换为 `awk` 命令。
- [grunt-plugin](https://github.com/clauswitt/zsh-grunt-plugin) - 为 `grunt` 添加自动完成功能。
- [gsh](https://github.com/cjayross/gsh) - `git` 辅助函数的集合
- [gtm-terminal-plugin](https://github.com/git-time-metric/gtm-terminal-plugin) - [git 时间指标](https://github.com/git-time-metric/gtm) 的终端插件。
- [gtr](https://github.com/Zocker1999NET/zsh-gtr) - 允许使用标签名称 **release-YYYY-MM-DD-HH-MM*- 和标题 **Release YYYY-MM-DD HH:MM** 在 `git` 中快速标记版本。
- [guish](https://github.com/gcarrarom/oh-my-guish) - 实用函数和别名的集合。
- [gumsible](https://github.com/Lowess/gumsible-oh-my-zsh-plugin) - [Molecule](https://molecule.readthedocs.io/) 的包装插件。
- [gunstage](https://github.com/LucasLarson/gunstage) - 至少有八种方法可以在“git”存储库中取消暂存文件。这是一个用于撤消“git add”的命令行 shell 插件。
- [gvm (dgnest)](https://github.com/dgnest/zsh-gvm-plugin) - ZSH 的“gvm”（Go 版本管理器）插件。
- [gvm (yerinle)](https://github.com/yerinle/zsh-gvm) - 为“gvm”（Groovy 环境管理器）提供自动完成功能。
- [hab](https://github.com/alexdesousa/hab) - 如果在更改到新目录时发现文件“.envrc”中定义的操作系统环境变量，则会自动加载该变量。
- [hacker-quotes](https://github.com/oldratlee/hacker-quotes) - 当您打开终端时输出随机黑客报价。
- [haiku](https://github.com/alesr/oh-my-zsh-haiku-plugin) - 当航站楼开放时，每 24 小时打印一次俳句，促进工作与生活平衡和压力管理。
- [halfpipe](https://github.com/raimo/zsh-halfpipe) - 编辑 shell 管道并实时查看其输出更新。快速获得正确的正则表达式并保存在网络请求中。
- [hanami](https://github.com/davydovanton/hanami-zsh) - [hanami](http://hanamirb.org) 项目的 ZSH 插件。
- [hangul](https://github.com/gomjellie/zsh-hangul) - 当应该用英语输入时，自动将朝鲜文（한글，韩语）更正为英语。 영어를 타동으로 수정합니다。
- [hbt](https://github.com/lzambarda/hbt) - 基于过去命令使用情况的启发式 ZSH 建议系统。
- [hebzsh](https://github.com/admons/hebzsh) - 如果未找到以希伯来语键入的命令，则将翻译该命令，就像在具有美国英语布局的键盘上键入该命令一样，然后重试。
- [help](https://github.com/Freed-Wu/zsh-help) - 对使用“--help”运行的命令的输出进行着色。
- [hints](https://github.com/joepvd/zsh-hints) - 在编辑缓冲区下显示全局和参数标志以及其他不完整的信息。
- [hipchat](https://github.com/robertzk/hipchat.zsh) - 从 shell 发送 hipchat 消息。
- [hist-delete](https://github.com/p1r473/zsh-hist-delete-fzf/) - 从 zsh 的 [fzf](https://github.com/junegunn/fzf) Ctrl+R 历史搜索中删除历史项目。
- [hist](https://github.com/marlonrichert/zsh-hist) - 在 ZSH 中编辑您的历史记录，无需离开命令行。
- [histdb](https://github.com/larkery/zsh-histdb) - 将您的历史记录存储在 SQLite 数据库中。可以与 [zsh-autosuggestions](https://github.com/zsh-users/zsh-autosuggestions) 集成。
- [historikeeper](https://github.com/stiliajohny/historikeeper) - 捕获数据库中的历史记录。
- [history-enquirer](https://github.com/zthxxx/zsh-history-enquirer) - 通过更多交互和多行选择菜单增强历史搜索。需要 Node.js。
- [history-filter](https://github.com/MichaelAquilina/zsh-history-filter) - 允许您指定自动排除命令插入永久历史记录的模式。对于防止秘密被写入特别有用。
- [history-here](https://github.com/leonjza/history-here) - 绑定`^G`来快速切换当前shell历史文件位置。
- [history-on-success](https://github.com/nyoungstudios/zsh-history-on-success) - 从 zsh 历史文件中过滤掉不成功的命令，避免重复相同的错误。基于 Dean Scarff 的[博客文章](https://scarff.id.au/blog/2019/zsh-history-conditional-on-command-success/)。
- [history-popup](https://github.com/lcrespom/oh-my-zsh-history-popup) - 捕获“PageUp”键并使用“dialog”打开包含历史记录的弹出菜单，以便用户可以交互式地浏览它并选择历史记录行以返回到提示符。
- [history-search-multi-word](https://github.com/zdharma-continuum/history-search-multi-word) - ZSH 的语法突出显示、多词历史搜索器，绑定到 Ctrl-R，具有高级功能（例如，将历史条目跳转到历史顶部）。
- [history-substring-search](https://github.com/zsh-users/zsh-history-substring-search) - 需要在 `zsh-syntax-highlighting` 之后加载，否则它们都会崩溃。您还需要将按键绑定到其功能，详细信息请参见 README.md。
- [history-sync (vitobotta)](https://github.com/vitobotta/zsh-history-sync/) - 使用“git”私有存储库在计算机之间同步您的 ZSH 历史记录。使用“openssl”加密历史记录。
- [history-sync (wulfgarpro)](https://github.com/wulfgarpro/history-sync) - 一个用于 [GPG](https://www.gnupg.org/) 的 [oh-my-zsh](https://ohmyz.sh/) 插件，使用 `git` 加密、互联网同步 ZSH 历史记录。
- [history](https://github.com/b4b4r07/zsh-history) - 扩展历史记录，以便可以通过 SQL 查询。
- [histree](https://github.com/fuba/histree-zsh) - 与 [histree-core](https://github.com/fuba/histree-core) 集成，提供增强的命令历史记录和目录感知功能。
- [hitokoto](https://github.com/derry96/hitokoto) - 显示来自[hitokoto.cn](https://hitokoto.cn/)的随机引用。
- [homeassistant-cli](https://github.com/frosit/zsh-plugin-homeassistant-cli) - 为 [Home Assistant 命令行界面 (hass-cli)](https://github.com/home-assistant/home-assistant-cli) 提供完成和（配置）帮助程序。并允许与 [Home Assistant](https://home-assistant.io/) 实例进行命令行交互。
- [homebrew](https://github.com/digitalraven/omz-homebrew) - [homebrew](https://brew.sh) 插件，补充了 oh-my-zsh 中内置的插件，并且可以在启用它的情况下安全运行。
- [hooks](https://github.com/willghatch/zsh-hooks) - 添加缺失的钩子 - 供插件和个人使用。
- [host-switch](https://github.com/LockonS/host-switch) - 使开发过程中更容易切换不同的“/etc/hosts”文件。
- [hub-ci-zsh-plugin](https://github.com/raymondjcox/hub-ci-zsh-plugin) - 一个简单的插件，用于将 `hub` ci-status 添加到您的 ZSH 主题。
- [hub](https://github.com/soraliu/zsh-hub) - 用于分叉模型的 ZSH 插件。
- [hypnosnek](https://github.com/josephcourtney/hypnosnek) - 具有 p10k 集成的简单实用程序，用于管理“python”环境。
- [igit](https://github.com/ytakahashi/igit) - 使用 [fzf](https://github.com/junegunn/fzf) 交互式“git”命令。
- [incsearch](https://github.com/aoyama-val/zsh-incsearch) - ZSH 更友好的“vim”模式。在当前行内通过增量搜索移动光标。
- [ing](https://github.com/rummik/zsh-ing) - 简化的“ping”输出。
- [instant-repl](https://github.com/jandamm/instant-repl.zsh) - 为当前 ZSH 会话中的任何命令激活 REPL。
- [interactive-cd](https://github.com/changyuheng/zsh-interactive-cd) - “cd”的类似鱼的交互式选项卡完成。
- [iosctl](https://github.com/obayer/iosctl) - 快速访问运行模拟器的App、Data、Log。
- [ipip](https://github.com/SukkaW/zsh-ipip) - [IPIP](https://en.ipip.net) 插件。
- [ipnav](https://github.com/clebertmarctyson/oh-my-zsh-ipnav) - 为 IP 地址操作提供方便的别名和补全 [ip-navigator-cli](https://github.com/clebertmarctyson/ip-navigator-cli)。
- [iterm-tab-color](https://github.com/bernardop/iterm-tab-color-oh-my-zsh) - 在iTerm2中添加设置选项卡颜色的功能，并且可以根据cwd或正在执行的命令自动更改颜色。
- [iterm-tab-colors](https://github.com/tysonwolker/iterm-tab-colors) - 根据当前工作目录自动更改 iTerm 2 选项卡颜色。
- [iterm-tmux-color-tabs](https://github.com/remino/omz-plugin-iterm2-tmux-color-tabs) - iTerm2 中打开的每个新“tmux”选项卡都将具有默认或指定调色板中的下一个颜色。
- [iterm-touchbar](https://github.com/iam4x/zsh-iterm-touchbar) - 在 MacbookPro TouchBar 中显示 iTerm2 反馈（当前目录、git 分支和状态）。
- [iterm2-colors](https://github.com/shayneholmes/zsh-iterm2colors) - 从命令行管理 iTerm 2 的配色方案。
- [iterm2-shell-integration](https://github.com/gnachman/iterm2-shell-integration) - iTerm2 的 Shell 集成和实用程序。
- [iterm2-tabs](https://github.com/gimbo/iterm2-tabs.zsh) - 设置 iTerm 2 选项卡的颜色和标题。
- [iterm2](https://github.com/laggardkernel/zsh-iterm2) - 将 iTerm 2 的 ZSH 集成脚本打包到 ZSH 插件中，以避免污染您的 $HOME 目录，时间增加可忽略不计，仅 2ms。
- [iwd](https://github.com/zshzoo/iwd) - 与“$PWD”的概念类似，这个 ZSH 插件将您的初始工作目录保存在“$IWD”中，以便轻松返回到会话的起点。
- [jabba](https://github.com/2m/zsh-jabba) - 为 [jabba](https://github.com/shyiko/jabba) Java 版本管理器添加 shell 集成代码和补全。
- [jap](https://github.com/philipstuessel/jap) - 终端自动化框架。
- [java-zsh-plugin](https://github.com/Xetius/java-zsh-plugin) - 添加 `setjdk` 命令，以便您可以在不同版本的 jdk 之间轻松切换。
- [javaVersions](https://github.com/miguefl/javaVersions) - 使用单个命令在不同的 java 版本之间进行更改。
- [jdk-switch](https://github.com/LockonS/jdk-switch) - jdk版本之间切换。适用于 macOS 和 Linux。
- [jenkins](https://github.com/tomplex/jenkins-zsh) - ZSH 的 jenkins 插件，深受优秀的 jira 插件的启发。
- [jenv-lazy](https://github.com/shihyuho/zsh-jenv-lazy) - 用于延迟加载 jEnv 的 ZSH 插件。
- [jhipster](https://github.com/jhipster/jhipster-oh-my-zsh-plugin) - 添加 [jHipster](https://www.jhipster.tech/) 的命令。
- [jira-plus](https://github.com/gerges/oh-my-zsh-jira-plus) - 从命令行创建 JIRA 票证。
- [jirarc](https://github.com/aoantov/jirarc) - 提供重复的 [Jira-cli](https://github.com/ankitpokhrel/jira-cli) 命令的快捷方式。
- [jj](https://github.com/rkh/zsh-jj) - 添加对 [jujitsu](https://github.com/jj-vcs/jj) VCS 的支持。
- [journal](https://github.com/onurhanak/zsh-journal) - 允许您将注释附加到已运行的 shell 命令。当您稍后回顾时，可以方便地记住直线实际上在做什么。
- [jq](https://github.com/reegnz/jq-zsh-plugin) - 交互式构建 [jq](https://stedolan.github.io/jq/) 表达式。还支持[gojq](https://github.com/itchyny/gojq)。需要 [fzf](https://github.com/junegunn/fzf)。
- [jrgit](https://github.com/jrocha-dev/ohmyzsh-plugin-jrgit) - 提供一套功能来简化 Git 用户体验。它包括安装和配置“git”、使用 Git LFS 处理大文件、改进 diff 输出以及安全管理凭据和密钥的功能。
- [jumper](https://github.com/thestuckster/jumper) - 保存您当前的路径并允许您快速跳转到其他路径。
- [just-let-me-edit-my-files](https://github.com/asapelkin/zsh-just-let-me-edit-my-files) - 允许您在意外打开不可写文件时使用“sudo”重新启动编辑器。
- [k](https://github.com/supercrabtree/k) - 具有“git”状态装饰的 ZSH 目录列表。
- [k3d](https://github.com/dwaynebradley/k3d-oh-my-zsh-plugin) - 为 [k3d](https://k3d.io/) 添加别名和制表符补全。
- [k9s](https://github.com/acidix/zsh-k9s) - 为 [k9s](https://k9scli.io/) 提供迭代式 `$KUBECONFIG` 选择器。
- [kctl](https://github.com/yzdann/kctl) - 为“kubectl”添加帮助器别名。
- [kill-node](https://github.com/vmattos/kill-node) - 用于破坏“node”进程系列的 ZSH 插件。
- [kitsunebook](https://github.com/d12frosted/kitsunebook.plugin.zsh) - [oh-my-zsh](https://ohmyz.sh) 的 KitsuneBook 插件。
- [kittyback](https://github.com/pickle-slime/kittyback) - 自动更新和修改“kitty”终端模拟器的背景图像。
- [kiwi](https://github.com/fruitydog/kiwi.zsh-theme) - 以狗为主题，包括“git”状态和最后一个命令退出状态装饰器。
- [konsole-theme-changer](https://github.com/rocknrollMarc/zsh-konsole-theme-changer) - 从 ZSH 切换 konsole 主题。
- [kube-aliases](https://github.com/Dbz/kube-aliases) - 添加函数和别名，使使用“kubectl”更加愉快。
- [kube-ctx-manager](https://github.com/NotHarshhaa/kube-ctx-manager) - 面向 kubectl 高级用户的智能 shell 插件 - 模糊上下文切换、自动建议的别名以及直接内置于终端中的产品保护措施。
- [kube-ps1](https://github.com/jonmosco/kube-ps1) - “kubectl”的 ZSH 插件添加当前上下文和命名空间。
- [kubecolor (devopstales)](https://github.com/devopstales/zsh-kubecolor) - 添加“kubecolor”命令的别名。
- [kubecolor (droctothorpe)](https://github.com/droctothorpe/kubecolor) - 对“kubectl get events -w”的输出进行简化和着色
- [kubecolor (trejo08)](https://github.com/trejo08/kubecolor-zsh) - 从“kubectl”打印彩色输出。包括辅助函数。
- [kubeconfig-mgr](https://github.com/yhlooo/zsh-kubeconfig-mgr) - 使管理多个 kubeconfig 文件变得更容易。
- [kubectl-config-switcher](https://github.com/chmouel/kubectl-config-switcher/) - 通过“KUBECTL”环境变量在“~/.kube”中的配置文件之间切换。
- [kubectl-prompt](https://github.com/superbrothers/zsh-kubectl-prompt) - 在 ZSH 提示符中显示有关 kubectl 当前上下文和命名空间的信息。创建“ZSH_KUBECTL_CONTEXT”、“ZSH_KUBECTL_NAMESPACE”、“ZSH_KUBECTL_PROMPT”和“ZSH_KUBECTL_USER”变量，可用于自定义提示。
- [kubectl](https://github.com/mattbangert/kubectl-zsh-plugin) - 用于管理“kubectl”的 ZSH 插件。
- [kubectlenv](https://github.com/rafalmasiarek/oh-my-zsh-kubectlenv-plugin) - 在多个“kubectl”版本之间轻松切换。
- [kubectx (ptavares)](https://github.com/ptavares/zsh-kubectx) - 安装并加载 [kubectx](https://github.com/ahmetb/kubectx)。
- [kubectx (unixorn)](https://github.com/unixorn/kubectx-zshplugin) - 自动安装 [kubectx](https://github.com/ahmetb/kubectx) 和 `kubens`。
- [kubernetes](https://github.com/Dbz/zsh-kubernetes) - 添加 [kubernetes](https://kubernetes.io) 辅助函数和别名。
- [lacrimae](https://github.com/caIamity/lacrimae) - 从一组圣歌中打印一行。
- [lacy](https://github.com/lacymorrow/lacy) - 检测自然语言与 shell 命令并相应地进行路由。命令正常执行，问题发送给您的 AI 代理（Claude Code、Gemini、OpenCode、Codex）。实时颜色指示器和第一个单词语法突出显示每次击键时的更新。还支持 Bash 4+。
- [lando (joshuabedford)](https://github.com/JoshuaBedford/lando-zsh) - 别名函数的集合，允许在 [Lando](https://docs.lando.dev) 中使用 CLI，而无需输入 lando 来访问它们。
- [lando (mannuel)](https://github.com/mannuel/lando-alias-zsh) - 为各种 [Lando](https://docs.lando.dev/basics/usage.html#default-commands/) 命令添加别名。
- [laradock-workspace](https://github.com/rluders/laradock-workspace-zsh) - 提供 [Laradock](http://laradock.io/) 工作区的接口。
- [laravel (baliestri)](https://github.com/baliestri/laravel.plugin.zsh) - 用于在运行“artisan”命令时跳过“php”命令以及在运行“sail”命令时跳过“./sail”或“./vendor/bin/sail”命令的插件。
- [laravel (crazybooot)](https://github.com/crazybooot/laravel-zsh-plugin) - 添加 [Laravel](https://laravel.com/) 5、5.1、5.2 和 5.3 的快捷方式。
- [laravel-au](https://github.com/Saleh7/laravel-au-zsh-plugin) - 添加 [Laravel](https://laravel.com/) 6 的别名。
- [laravel-sail](https://github.com/ariaieboy/laravel-sail) - 添加 `sail` 命令的快捷方式。
- [laravelx](https://github.com/rsthegeek/oh-my-zsh-laravelx) - 为常见的 [Laravel](https://laravel.com/docs) 命令添加一些别名。
- [last-working-dir-tmux](https://github.com/Curly-Mo/last-working-dir-tmux) - 跟踪全局和每个 [tmux](https://github.com/tmux/tmux) 会话最后使用的工作目录，并自动跳转到新的 shell。
- [last-working-directory](https://github.com/mdumitru/last-working-dir) - [oh-my-zsh](http://ohmyz.sh/) 中版本的破解副本。跟踪上次使用的工作目录并自动跳转到新的 shell。
- [lazy-load](https://github.com/goarano/zsh-lazy-load) - 仅当您实际需要时才进行延迟加载选项卡补全。
- [lazyload](https://github.com/qoomon/zsh-lazyload) - 延迟加载命令并加快 ZSH 的启动时间。
- [learn](https://github.com/MenkeTechnologies/zsh-learn) - MySQL/MariadB 中的学习集合可保存、查询和测验您学到的所有内容。
- [lesaint-git](https://github.com/lesaint/lesaint-git) - 替换 [oh-my-zsh](https://ohmyz.sh) 兼容框架的 `git` 插件。
- [lesaint-mvn](https://github.com/lesaint/lesaint-mvn) - [oh-my-zsh](https://ohmyz.sh) 的 Maven 插件。
- [life-progress](https://github.com/bGZo/life-progress) - 按天、周、月和年龄显示您的生活进展。
- [liferay](https://github.com/david-gutierrez-mesa/liferay-zsh) - 添加用于 [liferay](https://github.com/liferay/liferay-portal) 开发的脚本。
- [line-bisect](https://github.com/Hoid/line-bisect) - 允许您通过一次击键将当前命令向左或向右平分，从而在终端中移动光标。
- [linkfile](https://github.com/JaumeRF/linkfile-zsh) - 添加您最喜欢的目录的快捷方式。
- [linus-rants](https://github.com/bhayward93/Linus-rants-ZSH) - 打开终端时输出随机的 Linus Torvalds 咆哮。
- [listbox](https://github.com/gko/listbox) - shell 的列表框元素。
- [llm-replace](https://github.com/m3at/zsh-llm-replace) - 将 LLM 集成到 shell 中以快速生成命令。需要“curl”和“jq”。
- [llm-suggestions](https://github.com/stefanheule/zsh-llm-suggestions) - 在提示符处输入英文，按下可定义的键，它就会使用 LLM 为您生成命令行。
- [locate-sublime-projects-cli](https://github.com/david-treblig/locate-sublime-projects-cli) - 允许搜索 [Sublime Text](https://www.sublimetext.com) 项目并在 Sublime 中打开它们。
- [logout-user](https://github.com/pressdarling/logout-user) - 提供注销另一个 macOS 用户会话的功能。
- [loremipsum](https://github.com/pfahlr/zsh_plugin_loremipsum) - 在命令行上生成 lorem ipsum 文本。从 [lipsum.com](https://www.lipsum.com) 获取其数据。
- [ls (twopizza9621536)](https://github.com/TwoPizza9621536/zsh-ls) - 为“ls”添加更多别名。
- [ls (zpm-zsh)](https://github.com/zpm-zsh/ls) - 对“ls”的输出进行着色。
- [lsd (tankeryang)](https://github.com/tankeryang/zsh-lsd) - 将 `ls` 和 `tree` 命令替换为 [lsd](https://github.com/Peltoche/lsd)。
- [lsd (wintermi)](https://github.com/wintermi/zsh-lsd) - 使用 [lsd](https://github.com/Peltoche/lsd) 覆盖 `ls` 和 `tree` 命令。
- [lsd (z-shell)](https://github.com/z-shell/zsh-lsd) - 将 `ls` 替换为 [lsd](https://github.com/Peltoche/lsd)。
- [lumberjack](https://github.com/molovo/lumberjack) - Lumberjack 是 shell 脚本的日志记录接口。
- [lux](https://github.com/pndurette/zsh-lux) - ZSH 插件可通过“lux”命令切换 macOS、iTerm 2、Visual Studio Code 以及其他项目和应用程序的明暗模式。高度可定制：可以通过定义变量来配置包含的项目。高度可扩展：可以通过定义函数来添加项目。包含一个“macos_is_dark”辅助函数，用于确定 macOS 深色模式是否处于活动状态以用于主题设置。
- [mac-packaging](https://github.com/Temikus/mac-packaging) - 一组用于企业 Mac 打包的常用函数 [Munki](https://www.munki.org/munki/)。
- [macos (joow)](https://github.com/joow/macos) - 适用于 macOS 的 ZSH 插件。
- [macos (zshzoo)](https://github.com/zshzoo/macos) - ZSH 为 macOS 用户提供了好东西。
- [macos-autoproxy](https://github.com/SukkaW/zsh-osx-autoproxy) - 根据 macOS 的系统首选项配置代理环境变量。
- [macos-theme](https://github.com/gakimball/zsh-macos-theme) - 添加主题命令，可在 macOS 中在浅色和深色模式之间切换。需要 [lux](https://github.com/pndurette/zsh-lux) 插件。
- [mage2docker](https://github.com/lukaszolszewski/mage2docker) - 可以轻松地使用 Docker 和 Magento 2。加速并简化容器上 Magento 2 中的常见命令，例如清理缓存、安装升级、编译 di 等。
- [magebox](https://github.com/JCombee/oh-my-zsh-magebox) - 添加了对 [magebox](https://magebox.dev/) 的支持 - Magento 2 和 MageOS 的现代开发环境。为“magebox”CLI 提供别名、缓存刷新助手、提示状态指示器和缓存选项卡完成。
- [magento-2](https://github.com/dambrogia/oh-my-zsh-plugin-magento-2) - 添加 `m2` 函数来运行 magento 二进制文件，添加制表符补全。
- [magic-enter](https://github.com/zshzoo/magic-enter) - 通过将 ZSH 命令绑定到你的 Enter 键上，让你的 Enter 键变得神奇。
- [manydots-magic](https://github.com/knu/zsh-manydots-magic) - 用于模拟 `...'==`../..' 等的 zle 调整。
- [markedit](https://github.com/zakariaGatter/MarkEdit) - 标记文件并使用现有标记的自动完成功能对其进行编辑。
- [markgate](https://github.com/zakariaGatter/MarkGate) - 允许您标记目录，以便您可以直接跳转到它们。
- [matecito](https://github.com/uvallasciani/matecito-zsh) - 检测您的语言和国家/地区，以您的母语显示本地作者的引言。简单、离线、无噪音。
- [maven-plugin](https://github.com/KyleChamberlin/zsh_maven_plugin) - [oh-my-zsh](https://ohmyz.sh/) maven 插件的一个分支。
- [media-sync](https://github.com/redxtech/zsh-media-sync) - 一个有助于在两个“rclone”位置之间复制媒体的插件。
- [mend](https://github.com/Rakosn1cek/mend) - 与发行版无关的助手，可以恢复失败的命令，处理丢失的库/PGP 密钥，并提供特定于硬件的软件包建议。
- [mercurial](https://github.com/hcgraf/zsh-mercurial) - 从 [oh-my-zsh](https://ohmyz.sh) 中提取，因此您可以使用它而无需 oh-my-zsh 的其余部分。
- [mfunc](https://github.com/hlohm/mfunc) - 允许您即时定义持久函数，无需将它们添加到配置文件中。这些功能将永久可用，直到您将其删除。这已经在人工智能的帮助下进行了大幅更新，并且基本上未经测试。使用风险自负。
- [mise (cowboyd)](https://github.com/cowboyd/zsh-mise) - 将 [mise](https://mise.jdx.dev/) 垫片添加到您的 `$PATH` 中。使用垫片策略，以便工具在非交互式 shell 中可用（例如 Emacs exec-path-from-shell）。
- [mise (wintermi)](https://github.com/wintermi/zsh-mise) - [mise](https://mise.jdx.dev/)（以前称为 rtx）的插件，一个快速的多语言版本管理器，替换`nvm`、`nodenv`、`rbenv`、`rvm`、`chruby`、`pyenv` 等工具。
- [mkarch](https://github.com/0xRZ/mkarch) - ZSH 插件允许您使用多种不同的压缩格式创建档案。
- [mkcd](https://github.com/azizoid/zsh-mkcd) - 提供 `mkcd` 命令，规范的 `mkdir` && `cd` 帮助器。
- [mkcd](https://github.com/marvinroman/oh-my-zsh-mkcd-plugin) - 允许用户创建一个目录，如果成功，则随后“cd”进入该目录。
- [mlir](https://github.com/oowekyala/mlir-zsh-plugin) - 为 [MLIR](https://mlir.llvm.org/) 开发人员添加了一些好处，包括“mlir-opt”的制表符补全及其输出的着色。
- [mode-switch.CLI](https://github.com/Gyumeijie/mode-switch.CLI) - 一个 ZSH 插件，用于在正常模式和“vi”模式之间切换命令行。
- [monorepo-plugin](https://github.com/zilongqiu/monorepo-zsh-plugin) - 用于 monorepo 管理的 ZSH 插件。
- [monthrename](https://github.com/NotTheDr01ds/zsh-plugin-monthrename) - 将月份名称重命名为文件名中的数字。
- [more-hooks-for-git](https://github.com/capsulescodes/more-hooks-for-git) - 为 `git add`、`git diff` 和 `git status` 添加额外的钩子。
- [mouse-status](https://github.com/gryffyn/mouse-status) - 根据状态代码更改鼠标颜色，使用 libratbag。
- [msf](https://github.com/sathish09/zsh_plugins/tree/master/msf) - [Metasploit](https://www.metasploit.com/) 处理程序插件，用于轻松启动处理程序。
- [multi-evalcache](https://github.com/rwwiv/multi-evalcache) - 受 [mroth/evalcache](https://github.com/mroth/evalcache) 启发，缓存多个评估负载以缩短启动时间。
- [mvn-contexts](https://github.com/artemy/zsh-mvn-contexts) - 允许在“maven”配置之间快速切换。
- [mycli](https://github.com/remino/omz-plugin-mycli-alias) - 添加带有登录路径的 [`mycli`](https://www.mycli.net) 别名。
- [mylocation](https://github.com/fALKENdk/mylocation) - 一个根据您的 IP 地址显示您当前位置的插件。
- [myservice](https://github.com/jarlor/zsh-myservice) - 旨在帮助您更方便地管理自定义 systemd 服务和 Docker 容器。该插件提供用户友好的命令，可以直接从命令行列出和检查自定义服务和 Docker 容器的状态。
- [mysql-colorize](https://github.com/zpm-zsh/mysql-colorize) - 为“mysql”表添加颜色。
- [mysql-login](https://github.com/remino/omz-plugin-mysql-alias) - 添加带有登录路径的 MySQL 别名。
- [mysql](https://github.com/voronkovich/mysql.plugin.zsh) - 添加一些处理`mysql`的函数。
- [n](https://github.com/gretzky/n.zsh) - 使用[n](https://github.com/tj/n)根据项目环境自动切换节点版本。
- [namelink](https://github.com/jthat/zsh-namelink) - 提供一组目录中的文件系统条目（通常是符号链接）到指定目录散列中的对应项的自动同步映射。
- [navi](https://github.com/icatalina/zsh-navi-plugin/) - [navi](https://github.com/denisidoro/navi) 插件。
- [navigation-tools](https://github.com/zdharma-continuum/zsh-navigation-tools) - 添加类似“htop”的kill、目录书签浏览器、多字增量历史搜索器等。
- [nerd-font-check](https://github.com/delorenj/nerd-font-check) - 如果不存在，则建议使用 [brew](https://brew.sh/) 安装 [Nerd Fonts](https://www.nerdfonts.com/font-downloads)。
- [new-file-from-template](https://github.com/zpm-zsh/new-file-from-template) - 从模板生成文件。
- [newvwp](https://github.com/aubreypwd/zsh-plugin-newvwp) - 使用 Valet 启动一个新的 WordPress 网站。
- [nhl-schedule](https://github.com/Matt561/zsh-nhl-schedule) - 检索并显示 NHL 赛程表。
- [nice-exit-code](https://github.com/bric3/nice-exit-code) - 将退出状态代码映射到人类可读的字符串。
- [nix-shell](https://github.com/chisui/zsh-nix-shell) - 允许您在“nix-shell”环境中使用 ZSH 作为默认 shell 的插件。
- [nlsh](https://github.com/PsychArch/nlsh) - 允许您使用自然语言与 shell 进行交互。支持多个LLM提供商（兼容OpenAI API）。包括对 X.ai 的 Grok 的支持。
- [nnvm](https://github.com/torifat/nnvm) - 根据`.nvmrc`自动切换节点版本。需要 [n](https://github.com/tj/n)。
- [no-ps2](https://github.com/romkatv/zsh-no-ps2) - 使用此插件时，如果键入的命令不完整，则 Enter 会插入换行符。没有PS2！
- [nobility](https://github.com/Twilight4/nobility) - 一个有组织的 shell 模块集合，旨在通过利用自动完成和预填充等 shell 集成来简化您的渗透测试工作流程，优化您的工作效率，并将您从处理笔记、无休止的复制和粘贴以及繁琐的命令编辑的麻烦中解放出来。
- [node-env-installer](https://github.com/shiro-saber/node-env-installer) - 使用 `nvm` 为当前项目安装新版本和模块。
- [node-path](https://github.com/andyrichardson/zsh-node-path) - 自动将当前目录的“npm”bin 添加到“$PATH”。
- [node](https://github.com/srijanshetty/node.plugin.zsh) - Srijan Shetty 的 ZSH Node.js 插件，可缓存“nvm”补全并自动加载“nvm”（如果存在）。
- [nodenv (c-uo)](https://github.com/C-uo/zsh-nodenv) - 在工作目录中查找“nodenv”并在找到时加载它。
- [nodenv (jsahlen)](https://github.com/jsahlen/nodenv.plugin.zsh) - 自动将 `nodenv` 及其补全加载到 shell 中。
- [nodenv (mattberther)](https://github.com/mattberther/zsh-nodenv) - 安装、更新和加载“nodenv”。受到 [zsh-rbenv](https://github.com/Meroje/zsh-rbenv) 的启发。
- [nodo](https://github.com/nicolodiamante/nodo) - 此插件可帮助您通过取消同步目录来防止“node_modules”目录填满您的 iCloud 存储，或者可以通过删除所选根目录中的所有“node_modules”目录来节省更多空间。这对于清理具有多个“node_modules”树的项目特别有用
- [nohup](https://github.com/micrenda/zsh-nohup) - 按“Ctrl-H”将“nohup”添加到当前命令。
- [noreallyjustfuckingstopalready](https://github.com/eventi/noreallyjustfuckingstopalready) - macOS 用户知道尝试弄清楚什么命令实际上刷新了他们的 macOS 版本上的 DNS 缓存的痛苦，而这个插件可以消除这种烦恼。
- [nota](https://github.com/0x61nas/nota.zsh) - 用于管理笔记列表的简单插件。
- [notenote](https://github.com/DrgnFireYellow/notenote/) - 使记笔记变得容易。
- [notes (aperezdc)](https://github.com/aperezdc/zsh-notes) - 受到 [terminal_velocity](https://www.seanh.cc/terminal_velocity/) 的启发，它提供了一个快速界面来创建和访问目录中的一组 [Markdown](https://en.wikipedia.org/wiki/Markdown) 文本文件。
- [notes (chipsenkbeil)](https://github.com/chipsenkbeil/zsh-notes) - 在 ZSH 中提供快速的笔记编辑体验。
- [notify (luismayta)](https://github.com/luismayta/zsh-notify) - ZSH 通知，自动安装依赖项和 r2d2 声音。
- [notify (marzocchi)](https://github.com/marzocchi/zsh-notify) - ZSH 的插件（在 macOS 和 Linux 上），如果终端应用程序位于后台（或命令的终端选项卡处于非活动状态），当命令以非零退出状态终止或完成时间超过 30 秒时，该插件会发布桌面通知。
- [npm (trystan2k)](https://github.com/trystan2k/zsh-npm-plugin) - 添加“npm”别名。基于 Oh-My-Zsh [npm](https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins/npm) 插件。
- [npm (zfben)](https://github.com/zfben/zsh-npm) - 使用“n”作为带有“noglob”前缀等的“npm”别名。基于 Oh-My-Zsh [npm](https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins/npm) 插件。
- [npms](https://github.com/torifat/npms) - 由 [fzf](https://github.com/junegunn/fzf) 提供支持的实用程序，用于交互地使用 npm 脚本。需要 [fzf](https://github.com/junegunn/fzf) 和 [jq](https://stedolan.github.io/jq/)。
- [nvim-appname](https://github.com/mehalter/zsh-nvim-appname) - 使用“NVIM_APPNAME”维护多个 Neovim 配置，并使用可用标志、可用 neovim 应用程序和 neovim 参数/标志的完整选项卡完成。需要 neovim v0.9+
- [nvim-switcher](https://github.com/dacarey/zsh-nvim-switcher) - 管理 `nvim` 发行版之间的切换，例如 [Lazyvim](https://www.lazyvim.org/)、[kickstart](https://github.com/nvim-lua/kickstart.nvim) 或自制配置。
- [nvm-auto-use (jrr997)](https://github.com/jrr997/zsh-nvm-auto-use) - 根据您当前的目录，使用 [nvm](https://github.com/nvm-sh/nvm) 自动管理您的 Node.js 版本。
- [nvm-auto-use (martvdmoosdijk)](https://github.com/martvdmoosdijk/zsh-nvm-auto-use) - 当检测到“.nvmrc”时，自动使用“nvm use”切换节点版本。
- [nvm-auto-use (tomsquest)](https://github.com/tomsquest/nvm-auto-use.zsh) - 每当您进入包含“.nvmrc”文件的目录时，都会自动调用“nvm use”，该文件中的字符串告诉“nvm”要使用哪个节点。
- [nvm-deferred](https://github.com/davidparsson/zsh-nvm-deferred) - 使用 [zsh-defer](https://github.com/romkatv/zsh-defer) 推迟加载 `nvm` oh-my-zsh 插件以加速 shell 启动。
- [nvm-lazy](https://github.com/davidparsson/zsh-nvm-lazy) - 用于延迟加载 oh-my-zsh 的 **nvm*- 插件的插件。它支持多个二进制/入口点的延迟加载“nvm”，默认值为“nvm”、“node”和“npm”。
- [nvm-pnpm-auto-switch](https://github.com/spencerbeggs/zsh-nvm-pnpm-auto-switch) - 更改目录时自动切换 Node.js 版本（使用“nvm”）并管理 pnpm 包管理器版本（使用“corepack”）。
- [nvm-x](https://github.com/seebeen/zsh-nvm-x) - ZSH 插件用于管理“nvm”，具有扩展的帮助程序和改进的工作流程。
- [nvm](https://github.com/lukechilds/zsh-nvm) - 用于安装、更新和加载“nvm”的 ZSH 插件。
- [oath](https://github.com/alexdesousa/oath) - 管理 2FA 身份验证 6 位数令牌。它受到这篇关于[使用oathtool进行两步验证](https://www.cyberciti.biz/faq/use-oathtool-linux-command-line-for-2-step-verification-2fa/)的文章的启发。
- [oh-my-gpt](https://github.com/vicotrbb/oh-my-gpt) - 提供易于使用的界面，可直接从终端与 OpenAI 的 GPT 模型进行交互。它允许您发送查询、分析文件并获得人工智能支持的各种任务的帮助。
- [oh-my-matrix](https://github.com/amstrad/oh-my-matrix) - 将您的终端变成矩阵。
- [oh-my-posh-manager](https://github.com/wintermi/zsh-oh-my-posh) - 管理 oh-my-posh 主题引擎，并提供默认的类似电力线的主题。
- [oh-my-tmux-manager](omt-manager) - 让您轻松管理“tmux”配置。
- [ohmyai](https://github.com/briques/ohmyai-zsh) - 针对 Zsh 的 AI 支持命令建议。输入您想要执行的操作，按热键，然后从 OpenAI 获取 shell 命令建议。
- [ollama](https://github.com/plutowang/zsh-ollama-command) - 将OLLAMA AI模型与[fzf](https://github.com/junegunn/fzf)集成，根据用户输入需求提供智能命令建议。
- [omz-full-autoupdate](https://github.com/Pilaton/OhMyZsh-full-autoupdate) - 自动更新 [oh-my-zsh](https://github.com/ohmyzsh/ohmyzsh) 插件和主题。
- [omz-git](https://github.com/aeons/omz-git) - [Oh-My-ZSH](https://ohmyz.sh/) 的 [git](https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins/git) 插件重新打包为独立的。
- [omz-themes-standalone](https://github.com/zshzoo/omz-themes-standalone) - 为您提供 [oh-my-zsh](https://github.com/ohmyzsh/ohmyzsh) 主题，而不需要 [Oh-My-ZSH](https://ohmyz.sh/) 附带的其他所有内容。
- [op](https://github.com/zsh-contrib/zsh-op) - 无缝 [1Password](https://1password.com/) CLI 集成。通过自动缓存、快速 shell 初始化和配置驱动的工作流程，从 1Password 管理环境变量和 SSH 密钥。
- [open-create-projects](https://github.com/marcossegovia/open-create-projects) - 在 Jetbrains 中打开/创建项目。
- [open-pr](https://github.com/caarlos0/zsh-open-pr) - 一个 ZSH 插件，用于从命令行打开拉取请求。
- [opencode (mskadu)](https://github.com/mskadu/zsh-opencode-plugin) - 添加对 [opencode](https://opencode.ai/) AI 编码代理的支持。
- [opencode (verlihirsh)](https://github.com/verlihirsh/zsh-opencode-plugin) - 停止谷歌搜索 shell 命令。只需用简单的英语描述您想要的内容，按 Tab 键即可获得您需要的确切命令。
- [openshift-origin](https://github.com/ryanswart/openshift-origin-zsh-plugin) - 添加一些常见 openshift origin (oc) 操作的快捷方式。
- [opera-gx](https://github.com/troykelly/oh-my-zsh-opera-gx) - 通过使用“opgx”命令后跟配置文件名称，可以使用特定用户配置文件启动 Opera GX。该插件还实现了配置文件名称的自动完成功能。
- [opp](https://github.com/hchbaw/opp.zsh) - Vim 的 ZSH 文本对象。
- [opt-path](https://github.com/jreese/zsh-opt-path) - 自动将 `~/opt` 子路径添加到您的 `$PATH` 中。
- [org-hopper](https://github.com/hjdarnel/org-hopper/) - 用 [fzf](https://github.com/junegunn/fzf) 包装 GitHub CLI。它允许您在给定 GitHub 组织的存储库之间快速跳转，如果本地副本尚不存在，则将其克隆到预定义位置。
- [osx-dev](https://github.com/marshallmick007/osx-dev-zsh-plugin) - 该插件添加了一些用于在 macOS 安装上维护各种服务器程序的命令。
- [osx](https://github.com/mwilliammyers/plugin-osx) - 添加一些常见的 macOS 相关别名和函数。
- [paci](https://github.com/iloginow/zsh-paci) - arch Linux 包管理器的插件。
- [pack](https://github.com/fourdim/zsh-pack/) - 使用 ZSH 打包您的源代码。
- [package-any-node](https://github.com/zdharma-continuum/zsh-package-any-node) - 轻松安装插件目录中的任何 Node 模块，通过 [Bin-Gem-Node](https://github.com/zdharma-continuum/z-a-bin-gem-node) 附件自动创建的垫片（即：转发器脚本）公开其二进制文件。
- [packer](https://github.com/BreakingPitt/zsh-packer) - 为 Hashicorp [packer](https://www.packer.io/) 添加别名和自动完成功能。
- [pantheon-terminal-notify](https://github.com/deyvisonrocha/pantheon-terminal-notify-zsh-plugin) - 长时间运行命令的后台通知。支持 Elementary OS Freya。
- [passwordless-history](https://github.com/jgogstad/passwordless-history) - 防止密码进入您的命令行历史记录。
- [paste-guard](https://github.com/stefanoamorelli/zsh-paste-guard) - 检测粘贴的命令并在执行前要求确认短语以防止剪贴板注入攻击 (MITRE ATT&CK T1204.004)。从“/dev/tty”读取确认，因此攻击者无法将确认嵌入到有效负载中。
- [path-ethic](https://github.com/sha1n/path-ethic) - 帮助快速轻松地管理您的“$PATH”。不会触及您现有的“.zshrc”、“.zprofile”，而是添加到现有环境之上。
- [patina](https://github.com/michel-kraemer/zsh-patina) - 用 Rust 编写的速度极快的 ZSH 语法荧光笔。
- [pctl](https://github.com/ytet5uy4/pctl) - 切换代理的环境变量。
- [peco-history](https://github.com/jimeh/zsh-peco-history) - 按“ctrl+R”时使用 Peco 搜索 shell 历史记录。
- [penmux](https://github.com/mfulz/zsh-penmux) - 会话管理器插件，用于渗透测试会话并跟踪报告中使用的终端会话。
- [pentest](https://github.com/jhwohlgemuth/oh-my-zsh-pentest-plugin) - 惰性渗透测试人员的别名和函数。
- [penv](https://github.com/Nhqml/penv-zsh-plugin) - 管理存储在“~/.local/share/py-venv/”中的“uv”Python虚拟环境。支持用于列出、激活（shell 和目录级别）、创建、删除和解释 env 激活原因的子命令。可以更轻松地用“uv”替换“pyenv”和“poetry”。
- [per-directory-history](https://github.com/jimhester/per-directory-history) - ZSH 的每个目录历史记录以及全局历史记录，以及使用“^G”在它们之间切换的能力。
- [percol](https://github.com/robturtle/percol.plugin.zsh) - 使用 [percol](https://github.com/mooz/percol) 以交互方式增量搜索历史记录/恢复后台作业。
- [perlbrew](https://github.com/tfiala/zsh-perlbrew/) - 如果尚未安装，则安装 [perlbrew](https://perlbrew.pl/) 并为您的 shell 初始化它。
- [pew](https://github.com/shosca/zsh-pew) - 使用 [pew](https://github.com/berdario/pew) 设置和管理 Python virtualenv，并在移动目录时自动切换 virtualenv。
- [pg](https://github.com/caarlos0-graveyard/zsh-pg) - 添加实用程序函数以与 [PostgreSQL](https://www.postgresql.org/) 一起使用。
- [pgconnect](https://github.com/ruslan-korneev/pgconnect-zsh) - 提供了一种使用“pgcli”和 [fzf](https://github.com/junegunn/fzf) 管理和连接 PostgreSQL 数据库的简单方法，以获得无缝的命令行体验。
- [ph-marks](https://github.com/lainiwa/ph-marks) - 从您的终端为 Pornhub 视频添加书签。
- [php-version-rcfile-switcher](https://github.com/xellos866/php-version_rcfile-switcher) - 如果目录中存在 rc 文件，则使用 [php-version](https://github.com/wilmoore/php-version) 自动在 php 版本之间切换。
- [php-version-switcher](https://github.com/Akollade/php-version-switcher.plugin.zsh) - 如果找到 `.php-version` 文件，则更改 php 版本。
- [phpcs](https://github.com/voronkovich/phpcs.plugin.zsh) - [PHP 代码嗅探器](https://github.com/squizlabs/PHP_CodeSniffer) 插件。
- [phpunit](https://github.com/voronkovich/phpunit.plugin.zsh) - [PHPUnit](https://phpunit.de/) 插件。
- [pi](https://github.com/nearsyh/pi-zsh-plugin) - 将 shell 中的 `:` 命令映射到 `pi -p` 调用，并保留每个 shell 的 `pi` 会话文件以保证连续性。
- [pins](https://github.com/mehalter/zsh-pins) - 用于固定目录的插件。就像具有选项卡补全功能的 CLI 文件夹书签管理器一样。
- [pip-app](https://github.com/sharat87/pip-app) - 可以轻松地将 python 应用程序安装到不同的 Python virtualenv 中，这样它们就不会与系统上的任何其他 python 要求发生冲突。
- [pip-env](https://github.com/iboyperson/zsh-pipenv) - 进入 `pipenv` 项目后自动激活 [pipenv](https://pipenv.readthedocs.io/en/latest/)。
- [pipe](https://github.com/pipe-felipe/zsh-pipe-plugin) - 功能强大的 ZSH 插件，具有 **跨发行版系统更新** 和 **清理**（支持 `apt`、`dnf`、`pacman`、`zypper`、`homebrew` 等）、Docker 容器/卷管理和开发环境增强功能。通过直观的命令简化多个 Linux 发行版的系统维护。可通过简单的配置系统进行扩展 - 有关详细信息，请参阅项目自述文件。
- [pipenv (owenstranathan)](https://github.com/owenstranathan/pipenv.zsh) - 如果该目录中有 Pipfile，则进入目录时自动激活 **pipenv**。包括 `pipenv` 补全。
- [pipenv (sudosubin)](https://github.com/sudosubin/zsh-pipenv) - 启用 `pipenv` 的 `$PATH` 并添加补全。
- [pipx](https://github.com/thuandt/zsh-pipx) - [pipx](https://github.com/pypa/pipx) 的自动补全。
- [pjfzf](https://github.com/K021/pjfzf) - 由 [fzf](https://github.com/junegunn/fzf) 提供支持的项目目录导航器。注册基本目录并通过基于频率的排序和文件预览来导航其子目录。
- [pkenv](https://github.com/ptavares/zsh-pkenv) - 安装并加载 [pkenv](https://github.com/iamhsa/pkenv.git)。
- [plenv](https://github.com/TwoPizza9621536/zsh-plenv) - 基于 jenv 的 perl [plev](https://github.com/tokuhirom/plev) 版本管理器插件。
- [plugin-ibtool](https://github.com/rgalite/zsh-plugin-ibtool) - 添加 ibtool 快捷方式以生成本地化的 XIB 文件。
- [plugin-rails](https://github.com/paraqles/zsh-plugin-rails) - Rails 的 ZSH 插件。
- [plugin-vscode](https://github.com/wuotr/zsh-plugin-vscode) - [Visual Studio Code](https://code.visualstudio.com/download) 插件，适用于 macOS、Windows 和 Linux 的文本编辑器。
- [plugin](https://github.com/darrenbutcher/plugin) - 从样板模板创建自定义 [oh-my-zsh](https://ohmyz.sh) 插件。非常以 oh-my-zsh 为中心，生成的插件可能需要编辑才能与其他框架一起使用。
- [pnpm (baliestri)](https://github.com/baliestri/pnpm.plugin.zsh) - 为许多常见的 [pnpm](https://pnpm.io/) 命令添加有用的别名。包括制表符补全。
- [pnpm (bgowers)](https://github.com/bgowers/omz-pnpm) - 为您实际输入的 [pnpm](https://pnpm.io/) 命令添加一小组别名和制表符补全。
- [pnpm (leizhenpeng)](https://github.com/Leizhenpeng/zsh-plugin-pnpm) - 为常见的 [pnpm](https://pnpm.io/) 命令添加有用的别名。
- [pnpm (mat2ja)](https://github.com/mat2ja/pnpm.plugin.zsh) - 更好的 [pnpm](https://pnpm.io/) 别名。
- [pnpm (ntnyq)](https://github.com/ntnyq/omz-plugin-pnpm) - 为常见的 [pnpm](https://pnpm.io/) 命令添加有用的别名。
- [pnpm-pick](https://github.com/rschaufler/zsh-pnpm-pick) - 从 [pnpm](https://pnpm.io/) 工作区中的任何包中模糊挑选一个脚本，并将命令加载到提示符中 - 可编辑、在历史记录中，并且在终端标题中可见。
- [poetry (darvid)](https://github.com/darvid/zsh-poetry) - 自动激活和停用 [Poetry](https://poetry.eustace.io/) 创建的 python virtualenvs。
- [poetry (murku)](https://github.com/murku/omz_poetry_plugin) - 为常用的 [Poetry](https://poetry.eustace.io/) 命令添加别名
- [poetry (sudosabin)](https://github.com/sudosubin/zsh-poetry) - 启用诗歌“$PATH”和自动完成。
- [popman](https://github.com/jdsee/popman) - 您是否曾经发现自己正在编写一个很长的命令并需要检查手册页？ Popman 可以让您立即弹出您正在键入的任何命令的手册页，并直接跳回到您上次停下的位置，使您的命令行体验更加流畅和高效。
- [popular.zsh](https://github.com/sajjadRabiee/popular-zsh) - 允许您使用“padd”、“p”和“pls”添加书签、模板并重新运行最常用的 ZSH 命令。支持 AES-256-CBC 加密秘密占位符、通过“paddh”捕获历史记录、制表符补全以及导出/导入（包括从 GitHub 存储库直接导入）。
- [portal](https://github.com/anasouardini/portal/) - 一个非常基本的脚本，用于跳转到/从路径跳转，而无需编写整个路径、打开多个终端会话或使用 [fzf](https://github.com/junegunn/fzf) 进行文件系统搜索。深受 [Z](https://github.com/rupa/z) 的启发。
- [posh-git-bash](https://github.com/lyze/posh-git-sh) - 在提示中添加 `git` status。
- [ppsmon](https://github.com/mzpqnxow/ppsmon) - 读取“/sys/class/net/$interface/”以跟踪数据包传输速率。它将当前速率存储到 RAM 支持的文件系统中的文件中，可以轻松访问该文件并在 shell 提示符中显示。由于使用了 `/sys`，仅适用于 Linux。
- [pr-cwd](https://github.com/zpm-zsh/pr-cwd) - 使用当前工作目录创建一个全局变量。插件与 [jocelynmallon/zshmarks](https://github.com/jocelynmallon/zshmarks) 集成。
- [pr-eol](https://github.com/zpm-zsh/pr-eol) - 显示可嵌入提示中的 EOL 符号。
- [pr-exec-time](https://github.com/zpm-zsh/pr-exec-time) - 添加一个可用于显示上次命令运行的执行时间的变量。
- [pr-git](https://github.com/zpm-zsh/pr-git) - 创建一个带有可在提示中显示的“git”状态信息的全局变量。
- [pr-is-root](https://github.com/zpm-zsh/pr-is-root) - 设置一个环境变量，您可以在以 root 身份运行时在自定义提示中使用。
- [pr-jobs](https://github.com/zpm-zsh/pr-jobs) - 创建一个环境变量，可用于在自定义提示中显示后台作业信息。
- [pr-node](https://github.com/zpm-zsh/pr-node) - 设置一个环境变量，可用于在自定义提示中显示 Node.js 信息。
- [pr-return](https://github.com/zpm-zsh/pr-return) - ZSH 插件，显示上次运行命令的退出状态。
- [pr-user](https://github.com/zpm-zsh/pr-user) - 创建可在提示中使用的全局变量。
- [presenter-mode](https://github.com/idadzie/zsh-presenter-mode) - 在演示期间扩展别名。它还增加了终端窗口的对比度以增强可视性。
- [pretty-time (sindresorhus)](https://github.com/sindresorhus/pretty-time-zsh) - 将秒转换为人类可读的字符串：165392 → 1d 21h 56m 32s。
- [pretty-time (zpm-zsh)](https://github.com/zpm-zsh/pretty-time) - 将原始秒转换为人类可读的字符串。
- [prettyping](https://github.com/unixorn/prettyping) - 在标准 ping 工具周围添加一个包装器，目的是使输出更漂亮、更丰富多彩、更紧凑且更易于阅读。
- [prezto-last-working-dir](https://github.com/JoniVanderheijden/prezto-last-working-dir) - 跟踪上次使用的工作目录并自动跳转到新的 shell，除非起始目录不是“$HOME”。包括“lwd”别名。
- [print-alias](https://github.com/brymck/print-alias) - 每当您在命令行中使用别名时，都会打印带有扩展别名的命令。
- [printc](https://github.com/philFernandez/printc) - 允许您通过简单的“printc”调用以 RGB 空间中的任何颜色进行打印。
- [printdocker](https://github.com/elvitin/printdocker-zsh-plugin) - 漂亮地打印 [docker](https://docker.com) 对象。
- [profile-secrets](https://github.com/gmatheu/shell-plugins) - 将敏感变量（API 令牌、密码等）安全地保存在终端初始化文件中。使用 gpg 用您的秘密来加密/解密文件。
- [proj-jumper](https://github.com/Kikolator/proj-jumper) - 一个轻量级的 ZSH 插件，可让您直接跳转到单个开发根目录下的任何项目文件夹 - 当该根目录位于可移动驱动器上时，这是完美的。
- [project (gko)](https://github.com/gko/project) - 在本地和 GitHub（私有或公共存储库）上创建 node/python/ruby 项目。
- [project (voronkovich)](https://github.com/voronkovich/project.plugin.zsh) - 用于管理项目的插件。
- [project-aliases](https://github.com/dvigo/project-aliases) - Zsh 插件自动加载和卸载每个项目的别名。
- [projen](https://github.com/p6m7g8/p6-zsh-projen-plugin) - 添加 [projen](https://github.com/projen/projen) 的别名。
- [prompt-dir-perms](https://github.com/xPMo/zsh-prompt-dir-perms) - 创建一个显示当前目录权限的段，您可以在 ZSH 提示符中使用。
- [prompt-generator](https://github.com/the10thWiz/zsh-prompt-generator) - 生成自定义主题。某些生成的主题需要与电力线兼容的字体。
- [proxy-plugin (escalate)](https://github.com/escalate/oh-my-zsh-proxy-plugin) - 快速启用和禁用代理 shell 环境设置。
- [proxy-plugin (xooooooooox)](https://github.com/xooooooooox/zsh-proxy) - 帮助管理 shell 环境中的代理设置。
- [proxy](https://github.com/SukkaW/zsh-proxy) - 为某些包管理器和软件配置代理设置。
- [psgrep](https://github.com/voidzero/omz-plugin-psgrep/) - 使“ps grep”从“ps aux |”的结果中隐藏自己的进程。 grep`。
- [pump](https://github.com/fab1o/pump-zsh) - 提供一组可配置的别名、函数和主题，以增强您的终端工作流程。需要 [jq](https://stedolan.github.io/jq/)、[gum](https://github.com/charmbracelet/gum)、[glow](https://github.com/charmbracelet/glow) 和 [GitHub CLI](https://cli.github.com/)。
- [purge-history-secrets](https://github.com/jotasixto/purge-history-secrets) - 使用 [gitleaks](https://github.com/gitleaks/gitleaks) 定期扫描您的 ZSH 历史记录中的机密，并在发现时清除它们。需要[jq](https://jqlang.github.io/jq/)。
- [pwp](https://github.com/ttkalcevic/pwp) - 提供了一种在终端提示符中显示当前工作路径的便捷方法，并列出当前工作目录及其父目录。此外，它还包括一个自定义命令......可以轻松导航到父目录。
- [pycalc (alalik)](https://github.com/alalik/pycalc) - 将 `=` 键变成 ZSH shell 中强大的、Python 支持的计算器。
- [pycalc (peibozhao)](https://github.com/peibozhao/pycalc) - 使用Python语法的ZSH计算器。
- [pyenv (mattberther)](https://github.com/mattberther/zsh-pyenv) - 受到 **zsh-rbenv** 的启发。安装、更新或加载“pyenv”，并添加额外的功能。
- [pyenv (twopizza9621536)](https://github.com/TwoPizza9621536/zsh-pyenv) - 基于 oh-my-zsh [pyenv](https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins/pyenv) 插件，并对 rbenv 和 jenv 插件进行了修改。
- [pyenv (xlshiz)](https://github.com/xlshiz/pyenv-zsh-plugin) - 将 [pyenv](https://github.com/pyenv/pyenv) 加载到当前 shell 中，并通过 pyenv_prompt_info 函数提供提示信息。如果可用的话，还会加载 [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv)。
- [pyenv-lazy-load](https://github.com/erikced/zsh-pyenv-lazy-load) - ZSH 中延迟加载 `pyenv` 的插件。
- [pyenv-lazy](https://github.com/davidparsson/zsh-pyenv-lazy) - 延迟加载 [pyenv](https://github.com/pyenv/pyenv)。第一次调用 `pyenv` 时执行初始 `eval "$(pyenv init -)"`。
- [pyvenv-fast](https://github.com/ACmyles/pyvenv-fast) - 使用一个命令启动 Python `venv`。设计用于 [dotpyvenv](https://github.com/jeanpantoja/dotpyvenv)。
- [q (cal2195)](https://github.com/cal2195/q) - 将类似“vim”的宏寄存器添加到您的 ZSH shell。
- [q (tomsquest)](https://github.com/tomsquest/q.plugin.zsh) - 尾部/删除脏调试工具 [Q](https://github.com/y0ssar1an/q) 的临时文件。
- [qiime2](https://github.com/misialq/zsh-qiime2) - 添加函数和别名，以便更轻松地使用 [Quiime 2](https://qiime2.org/)。
- [qqq](https://github.com/mejistus/zsh-plugin-qqq) - 将当前终端变成一个彩色旋转 ASCII 甜甜圈，其下方居中显示 5 行 ASCII 日期和时间。
- [quiet-accept-zle](https://github.com/AdrieanKhisbe/zsh-quiet-accept-line) - 使您能够运行键入的 ZSH 命令，而无需触发新的提示、历史记录条目或输出输出。
- [quoter](https://github.com/pxgamer/quoter-zsh) - 打开新终端会话时显示随机报价。
- [quotify](https://github.com/dpretet/zsh-quotify) - 启动时显示我们对的鼓舞人心的编码报价。
- [qwy](https://github.com/Ryooooooga/qwy) - ZSH 模糊补全插件。
- [randeme](https://github.com/ex-surreal/randeme) - 为每个会话选择一个随机主题。如果您不喜欢所选主题，可以运行“randeme_rm”以不再显示该主题。
- [random-quotes](https://github.com/vkolagotla/zsh-random-quotes) - 显示随机引用或事实。
- [ranger (niziL)](https://github.com/NiziL/ranger.plugin.zsh) - 为[ranger](https://github.com/ranger/ranger)提供提示元素。显示当前的“RANGER_LEVEL”，当环境变量未设置时不显示任何内容，当它等于 1 时显示一些内容，当它大于 1 时显示其他内容。
- [ranger (rc2dev)](https://github.com/rc2dev/ranger-zshz) - 将 [zsh-z](https://github.com/agkozak/zsh-z) 集成到 [ranger](https://github.com/ranger/ranger) 中。
- [ranger-autojump](https://github.com/fdw/ranger-autojump) - 向 [ranger](https://github.com/ranger/ranger) 控制台文件管理器添加 [autojump](https://github.com/wting/autojump) 支持。
- [ranger-zoxide](https://github.com/fdw/ranger-zoxide) - 向 [ranger](https://github.com/ranger/ranger) 控制台文件管理器添加 [zride](https://github.com/ajeetdsouza/zride) 支持。
- [raspberry-temp](https://github.com/cfunkz/zsh-raspberry-temp-plugin) - 通过“rpi-temp”别名测量 Raspberry pi 的温度。
- [raspberryPi4Temperature](https://github.com/KidesLeo/RaspberryPi4TemperaturePromptPlugin) - 将树莓派温度放入飞船提示段中
- [razer-status-code](https://github.com/michaelmcallister/razer-status-code) - 根据上次执行命令的状态更改 [Razer Mouse](https://openrazer.github.io/) 的颜色。需要 [OpenRazer](https://openrazer.github.io) Linux 驱动程序。
- [rbenv (elliottcable)](https://github.com/ELLIOTTCABLE/rbenv.plugin.zsh) - 来自 [oh-my-zsh](https://ohmyz.sh/) 的 `rbenv` 插件的更快分支。
- [rbenv (jsahlen)](https://github.com/jsahlen/rbenv.plugin.zsh) - 基于原始 [oh-my-zsh](https://ohmyz.sh/) `rbenv` 插件的变体。
- [rbenv (meroje)](https://github.com/Meroje/zsh-rbenv) - 受到 [https://github.com/lukechilds/zsh-nvm/](https://github.com/lukechilds/zsh-nvm/) 的启发，可以更轻松地使用 ruby​​ `rbenv` 环境。
- [rc-files](https://github.com/0b10/rc-files) - 增加编辑各种rc文件的快捷功能。
- [recall](https://github.com/mango-tree/zsh-recall) - 使使用命令历史记录更加容易。
- [redis](https://github.com/z-shell/redis) - 将运行 [redis-server](https://redis.io/) 并将其指向 `redis.conf` 配置文件。这可以与 [zdharma/zredis](https://github.com/z-shell/zredis) 插件一起使用，以在 shell 之间共享变量。
- [redo](https://github.com/joknarf/redo) - 添加交互式历史菜单来替换“Ctrl-R”和“ESC+/”。
- [reentry-hook](https://github.com/RobSis/zsh-reentry-hook) - 如果已删除并重新创建工作目录，则重新进入工作目录的插件。
- [release-fetcher](https://github.com/Game4Move78/zsh-release-fetcher) - 获取最新版本并检查您是否信任用于签署标签的身份。
- [reload](https://github.com/aubreypwd/zsh-plugin-reload) - 添加快速重新加载`.zshrc`的功能。
- [reminder](https://github.com/AlexisBRENON/oh-my-zsh-reminder) - 一个在每个提示上方显示提醒的插件。
- [replace-multiple-dots](https://github.com/momo-lab/zsh-replace-multiple-dots) - 将 `...` 转换为 `../..`
- [require](https://github.com/aubreypwd/zsh-plugin-require) - 添加“require commandname”的功能，然后（如果安装了[brew](https://brew.sh)）自动“brew install commandname”（如果尚未安装）。
- [revolver](https://github.com/molovo/revolver) - ZSH 脚本的进度旋转器。
- [riddle-me](https://github.com/vkolagotla/zsh-riddle-me) - 显示随机谜语。
- [ripz](https://github.com/jedahan/ripz) - 提醒您别名，以便您更多地使用它们。取决于 [ripgrep](https://github.com/BurntSushi/ripgrep)。
- [robo](https://github.com/shengyou/robo-zsh-plugin) - [Robo](https://github.com/consolidation/robo/) 的 ZSH 插件。
- [rockz](https://github.com/aperezdc/rockz) - Lua + LuaRocks 基于 VirtualZ 的虚拟环境管理器。
- [ros2-env](https://github.com/Butakus/ros2-env) - 管理 [ROS 2](https://github.com/ros2) 环境和工作区。
- [ros2-supercharged](https://github.com/danlil240/ros2-supercharged) - 来自三个优秀 ROS 2 shell 项目的最佳创意的精心组合，被重建为一个有凝聚力的现代 zsh 插件。包括 [fzf](https://github.com/junegunn/fzf) 工作区选择器、启动文件选择器、colcon 错误浏览器、域管理、提示段、命名工作区注册表 (rosws)、每个工作区发行版 + 覆盖链、从任何地方构建 cb 以及真正的 colcon argcomplete 完成。
- [rose-pine-man](https://github.com/const-void/rose-pine-man) - 为“手册”页面着色。
- [rtm-reminder](https://github.com/aranel616/rtm-reminder-zsh) - 每次执行命令后显示紧急 [Remember The Milk](https://www.rememberthemilk.com/) 任务。干净、非侵入性且仅限终端。
- [run-scripts](https://github.com/Aireck2/zsh-run-scripts) - 从“package.json”运行脚本。
- [rura](https://github.com/kiki-ki/rura) - 一个简单的 ZSH 插件，用于保存和跳转到目录。
- [rust (betterfetch)](https://github.com/betterfetch/zsh-plugin-rust) - 提供方便的别名来使用 Rust 的 Cargo、Rustc 和 Rustup 工具。
- [rust (cowboyd)](https://github.com/cowboyd/zsh-rust) - 配置您的 [rust](https://www.rust-lang.org/) 工具链，如果当前尚未安装 [rustup](https://rustup.rs)，请安装它。
- [rust (juici)](https://github.com/Juici/zsh-rust-completions) - Rust 的 ZSH 补全定义。
- [rust (wintermi)](https://github.com/wintermi/zsh-rust) - [rust](https://www.rust-lang.org/) 工具链的插件。
- [rvm](https://github.com/johnhamelink/rvm-zsh) - 启动 [rvm](https://github.com/rvm/rvm) 并添加可在用户的“$PATH”中访问的 ruby​​gem 二进制文件（如指南针）。
- [safe-kubectl](https://github.com/benjefferies/safe-kubectl) - 在运行 [kubectl](https://kubernetes.io/docs/reference/kubectl/) 时添加一些安全性，方法是在自最后一个“kubectl”命令之后的可定义秒数后警告您所处的上下文。
- [safe-paste](https://github.com/oz/safe-paste) - 一个安全粘贴插件。请参阅 Conrad Irwin 的 [bracketed-paste](https://cirw.in/blog/bracketed-paste) 博客文章。
- [safe-rm](https://github.com/mattmc3/zsh-safe-rm) - 添加安全“rm”功能，以便“rm”将文件放入操作系统的垃圾箱中，而不是永久删除它们。
- [safe-venv-auto](https://github.com/mavwolverine/zsh-safe-venv-auto) - 一个具有安全意识的 ZSH 插件，可在您浏览目录时自动激活和停用 Python 虚拟环境，并具有针对不受信任环境的内置保护。
- [sail](https://github.com/Razzaghnoori/Sailor/) - 为 [sail](https://laravel.com/docs/10.x/sail) 添加方便的别名。
- [saml2aws-auto](https://github.com/devndive/zsh-saml2aws-auto) - 当使用多个 AWS 配置文件时，例如您的阶段（开发、预生产、生产）的不同帐户可用于确定当前导出的配置文件以及令牌是否仍然有效。
- [saml2aws](https://github.com/onyxraven/zsh-saml2aws) - 添加对 [saml2aws](https://github.com/Versent/saml2aws) 的支持。
- [sandboxd](https://github.com/benvan/sandboxd) - 仅在需要时运行设置命令（例如，“eval "$(rbenv init -)”等），通过延迟加载加速您的 .zshrc 和 shell 启动。
- [saneopt](https://github.com/willghatch/zsh-saneopt) - Sane 默认使用 ZSH 选项，本着 [vim-sensible](https://github.com/tpope/vim-sensible) 的精神。
- [sb-upgrade](https://github.com/redxtech/zsh-sb-upgrade) - 自动更新种子箱上的应用程序的脚本。
- [scad](https://github.com/MicahElliott/scad) - Docker/Podman (SCAD) 的 Shell 彩色别名。定义 [docker](https://www.docker.com/) / [podman](https://podman.io) 别名和函数。这些别名遵循使用管理命令组织和调用“docker”的新风格，而不是众所周知的令人困惑的“随机单独命令”。需要 [GRC](https://github.com/garabik/grc) 和 [jq](https://github.com/jqlang/jq)。
- [schroot](https://github.com/fshp/schroot.plugin.zsh) - 在提示中显示当前的“chroot”名称。
- [sdkman](https://github.com/ptavares/zsh-sdkman) - 安装 [sdkman](https://github.com/sdkman) 并为其添加补全和别名。
- [sealion](https://github.com/xyproto/sealion) - 允许您设置刷新提示时将出现在终端中的提醒。
- [search-directory-history](https://github.com/cmaahs/search-directory-history) - 允许对使用 [per-directory-history](https://github.com/jimhester/per-directory-history) 插件创建的每个目录历史记录进行复杂搜索。
- [sed-sub](https://github.com/MenkeTechnologies/zsh-sed-sub) - 添加键绑定以在当前命令行上进行全局搜索和替换。
- [seedee](https://github.com/joknarf/seedee) - 使用命令行中的箭头键以交互方式浏览目录/访问目录的历史记录。
- [select-history-skim](https://github.com/okhiroyuki/zsh-select-history-skim) 使用 [skim](https://github.com/lotabout/skim) 翻阅您的历史记录。
- [select-with-lf](https://github.com/chmouel/zsh-select-with-lf) - 让用户使用 [lf](https://github.com/gokcehan/lf) 选择文件或目录。
- [select](https://github.com/z-shell/zsh-select) - 具有近似匹配和 uniq 模式的多术语搜索选择列表。
- [selector](https://github.com/joknarf/selector) - 使创建选择菜单变得容易。
- [send](https://github.com/robertzk/send.zsh) - 单个命令“git add”、“git commit”和“git push”可实现更快的“git”工作流程。
- [sensei-git](https://github.com/aswitalski/oh-my-zsh-sensei-git-plugin) - 添加许多“git”别名和辅助 shell 函数。
- [senv](https://github.com/joepvd/senv) - 在提示中报告敏感环境变量的存在
- [session-sauce](https://github.com/ChrisPenner/session-sauce) - 用于为所有项目创建和管理 tmux 会话的 [fzf](https://github.com/junegunn/fzf) 界面。
- [setenv](https://github.com/kalpakrg/setenv) - 当您更改目录时运行脚本。
- [setpath](https://github.com/mys721tx/set_path) - 将一些本地路径添加到“fpath”和“$PATH”中。
- [shelf](https://github.com/ecmma/shelf) - 可用于使用助记符添加书签和直接访问任何文件的实用程序。
- [shell-fns](https://github.com/Hdoc1509/shell-fns) - 包括 `git`、`neovim`、`npm`、`pip` 扩展功能。
- [shell-ng](https://github.com/joknarf/shell-ng) - 结合了 [joknarf](https://github.com/joknarf/) 的其他插件 - [selector](https://github.com/joknarf/selector)、[nerdp](https://github.com/joknarf/nerdp)、[redo](https://github.com/joknarf/redo)、[seedee](https://github.com/joknarf/seedee) 和[complete-ng](https://github.com/joknarf/complete-ng)。
- [shell-proxy](https://github.com/caesar0301/zsh-shell-proxy) - 这是一个纯用户空间程序，shell 代理设置器，用 Python3 和“zsh”编写。
- [shellcolor](https://github.com/SaltedBlowfish/zsh-shellcolor) - 根据当前目录中是否存在“.shellcolor”来更改终端背景颜色。
- [shellfirm](https://github.com/kaplanelad/shellfirm) - Shellfirm 是一个方便的实用程序，可帮助避免在没有额外批准步骤的情况下运行危险命令。当检测到危险模式时，您将立即收到一个小的提示挑战，以验证您的操作。
- [shellsense](https://github.com/venopyX/shellsense) - AI 驱动的 ZSH 插件旨在通过强大的功能和 AI 驱动的功能来增强您的终端体验。 ShellSense 使用 Python 开发，为各种任务提供简化的工作流程，使您的终端更加高效且用户友好。
- [shift-select](https://github.com/jirutka/zsh-shift-select) - ZSH 的 Emacs 移位选择模式 - 使用 Shift 在命令行中选择文本，就像在许多文本编辑器、浏览器和其他 GUI 程序中一样。
- [shortcuts](https://github.com/fairy-root/Zsh-Shortcuts-Plugin) - 使用 [oh-my-zsh](https://ohmyz.sh/) 的快捷方式插件提高您的终端生产力。通过强大的功能轻松管理命令快捷方式。
- [show-git-user](https://github.com/luisprgr/zsh-show-git-user) - 当您需要在同一台计算机上使用多个“git”用户时，此插件将在提示中显示哪个“git”用户名处于活动状态。
- [show-path](https://github.com/redxtech/zsh-show-path) - 提供逐行显示`$PATH`的函数。
- [simpleserver](https://github.com/sathish09/zsh_plugins/tree/master/simpleserver) - 用于轻松启动 python `SimpleHTTPServer` 和 `SimpleHTTPSServer` 的插件。
- [singularityenv](https://github.com/saravanabalagi/zsh-plugin-singularityenv) - 提供`singularityenv_prompt_info`函数返回当前的奇点环境名称
- [skaffold](https://github.com/todie/skaffold.plugin.zsh) - [skaffold](https://skaffold.dev) 本地 kubernetes 开发环境的 ZSH 集成和完成。
- [skim (casonadams)](https://github.com/casonadams/skim.zsh) - 尝试确定 [skim](https://github.com/lotabout/skim) 的安装位置，然后启用其模糊自动完成和按键绑定。
- [skim (hackerchai)](https://github.com/hackerchai/skim-zsh) - 添加对 [skim](https://github.com/lotabout/skim) 的支持
- [slugify](https://github.com/lashoun/slugify) - 将文件名和目录转换为网络友好的格式。
- [slurm](https://github.com/galhar/slurm) - 提供用于运行交互式 [SLURM](https://slurm.schedmd.com) 作业的便捷命令。
- [smart-cd](https://github.com/dbkaplun/smart-cd) - 在 chpwd 之后运行 `ls` 和 `git status`。
- [smart-command-not-found](https://github.com/rami-shalhoub/Smart-command-not-found) - 未找到命令时显示所有可用选项。
- [smart-files](https://github.com/vxfemboy/zsh-smart-files) - 通过提供文件路径的视觉反馈并在需要时自动创建目录来增强 CLI。它根据路径的状态（现有的、新的或权限被拒绝）以不同的颜色突出显示路径，并自动处理目录创建。
- [smart-history](https://github.com/lstasi/zsh-smart-history-plugin) - 将您最近的 ZSH 历史记录转换为由 Ollama 提供支持的命令建议。
- [smart-insert](https://github.com/lgdevlop/zsh-smart-insert) - 提供交互式小部件，用于使用 [`fd`](https://github.com/sharkdp/fd)、[`rg`](https://github.com/BurntSushi/ripgrep) 和 [`fzf`](https://github.com/junegunn/fzf) 搜索文件和内容。它将结果直接插入到您的 shell 中，并带有可选的命令前缀。
- [smartcache](https://github.com/QuarticCat/zsh-smartcache) - 缓存命令输出以加快 shell 启动时间。
- [smartinput](https://github.com/momo-lab/zsh-smartinput) - 当您键入括号或引号时，会自动添加相应的结束括号/引号。
- [smile](https://github.com/fundor333/smile) - 添加显示随机表情的功能。
- [snap-list](https://github.com/crisis1er/zsh-snap-list) - 为 openSUSE Tumbleweed 上的“sudo snapper list”提供辅助函数。
- [snap-new](https://github.com/crisis1er/zsh-snap-new) - 用引导流程替换原始的“snapper”命令：14 个场景表预先填充描述，并根据您要执行的操作建议正确的类型（标准与重要）。在执行之前，它会检查磁盘使用情况，显示现有快照上下文，并要求确认。 --cleanup-algorithm 时间线总是被设置的——你不能忘记它。
- [snap-rollback](https://github.com/crisis1er/zsh-snap-rollback) - 本机“snapper rollback”立即执行，无需安全检查。该插件添加了引导流程、快照摘要、双重确认、试运行模式和重启提醒。
- [snippets](https://github.com/willghatch/zsh-snippets) - 命令行片段扩展。
- [snr](https://github.com/raisedadead/zsh-snr) - 将第一个命令的选定输出传递到下一个命令。
- [solarized-man](https://github.com/zlsun/solarized-man) - [Oh-My-ZSH](https://ohmyz.sh/) 插件 colored-man-pages 的修改版本，针对终端中的 [solarized dark](https://github.com/altercation/solarized/blob/master/iterm2-colors-solarized/Solarized%20Dark.itermcolors) 主题进行了优化。
- [some-peco](https://github.com/MoeBensu/zsh-some-peco/) - 使用 [peco](https://github.com/peco/peco) 增强您的命令行体验，即提供快速目录导航和历史搜索。
- [sops-crypt](https://github.com/chaosimpact/sops-crypt) - Mozilla SOPS 插件，提供当前目录和子目录中文件的一键加密和解密。
- [spaceship-ocm](https://github.com/iamkirkbater/spaceship-ocm-plugin) - 查询您的 OpenShift Cluster Manager (ocm) 配置以显示您连接到的环境。需要在您的终端中安装 [NerdFont](https://www.nerdfonts.com/font-downloads)。
- [spack](https://github.com/Game4Move78/zsh-spack) - 包括一些有用的别名和函数，用于加载/卸载 [Spack](https://github.com/spack/spack) 生成的模块。由于它使用“module”命令，因此比“spack load”效率更高。
- [ssh-agent](https://github.com/sdiebolt/zsh-ssh-agent) - 如果“ssh-agent”尚未运行，则自动启动它。
- [ssh-connect](https://github.com/gko/ssh-connect) - 一个简单的“ssh”管理器。
- [ssh-host](https://github.com/obolientsev/ssh-host) - 使用 [fzf](https://github.com/junegunn/fzf) 管理 ssh。
- [ssh-plugin](https://github.com/paraqles/zsh-plugin-ssh) - `ssh` 插件。
- [ssh-quickconnect](https://github.com/breda/zsh-ssh-quickconnect) - 简单的实用程序，可从“ssh”配置和“known_hosts”文件快速连接到主机。
- [ssh-warrior](https://github.com/OfferPi/ssh-warrior) - 根据您通过 ssh 连接的主机自动更改终端背景颜色。需要支持 OSC 11 / OSC 111 转义序列的终端（Kitty、iTerm2、Alacritty、GNOME 终端等都工作得很好）。
- [sshinfo](https://github.com/SckyzO/zsh-sshinfo) - 在连接之前显示已解析的 SSH 连接详细信息（例如最终主机名、端口、用户和代理）。这对于验证 SSH 配置非常有用，尤其是在处理涉及别名、代理或多个配置文件的复杂设置时。
- [sshpky](https://github.com/jeffzhangc/sshpky_zsh_plugin) - 自动更新 `$ZSH_CUSTOM` 文件夹中的 git-repositories。
- [sshukh](https://github.com/anatolykopyl/sshukh-zsh-plugin) - 当您“ssh”进入服务器时，将更新您的“known_hosts”文件。
- [startify](https://github.com/NorthIsMirror/zsh-startify) - 显示最近使用的“vim”文件、shell-util 文件、活动的“tmux”会话、最近运行的“git”命令等。
- [startcache](https://github.com/rndjams/zsh-startcache) - 通过缓存缓慢的 `eval "$(tool init)"` 命令的输出并用基于时间的陈旧性替换 `compinit` 的 fpath-string 失效来加速 shell 启动。每个 shell 节省 110ms–1180ms，具体取决于配置。
- [startup-timer](https://github.com/paulmelnikow/zsh-startup-timer) - 打印 shell 启动所需的时间。
- [stashy](https://github.com/MisterRios/stashy) - 简化使用“git stash”的插件。
- [statify](https://github.com/vladmrnv/statify) - 进行基本统计分析的插件。
- [sublime](https://github.com/valentinocossar/sublime) - 与 [Oh My Zsh](https://ohmyz.sh/) 的官方 [Sublime](https://www.sublimetext.com/) 插件相同，但这会在当前 Sublime 窗口中打开文件（如果已打开）。
- [sudo (hcgraf)](https://github.com/hcgraf/zsh-sudo) - 来自 [oh-my-zsh](https://ohmyz.sh/) 的 `sudo` 插件，提取为独立的。在 emacs 模式或 vi 命令模式下按 *ESC-ESC- 在当前/上一个命令之前切换“sudo”。
- [sudo (none9632)](https://github.com/none9632/zsh-sudo/) - 通过输入“ESC”-“ESC”将“sudo”添加为当前命令的前缀。
- [sudo-previous-current](https://github.com/chmouel/zsh-sudo-previous-current) - 将“sudo”添加到当前行或上一个命令。它会尽力保持当前光标位置，以便您的流程不会受到干扰。
- [suffix-alias](https://github.com/srijanshetty/zsh-suffix-alias) - 使用ZSH的后缀别名直接在shell中打开文件。
- [sussysh](https://github.com/sussynuggetz/sussysh-zsh) - 基于 xiong-chiamiov。
- [svn-n-zsh](https://github.com/khrt/svn-n-zsh-plugin) - 重写库存 [oh-my-zsh](https://ohmyz.sh/) [svn](https://subversion.apache.org/) 插件。
- [switch-git](https://github.com/robin-mbg/switch-git) - 在“git”存储库之间轻松切换。只需输入 `sgr <您的存储库名称的某些部分>`，然后按 Enter 键即可。
- [symfony (voronkovich)](https://github.com/voronkovich/symfony.plugin.zsh) - [Symfony](https://symfony.com/) 的 ZSH 插件。
- [syntax-highlighting-filetypes](https://github.com/trapd00r/zsh-syntax-highlighting-filetypes) - ZSH 语法通过 dircolors 实时突出显示。
- [syntax-highlighting](https://github.com/zsh-users/zsh-syntax-highlighting) - 将语法突出显示添加到 ZSH 提示符中。确保在[zsh-users/zsh-history-substring-search](https://github.com/zsh-users/zsh-history-substring-search)之前加载此内容，否则它们都会崩溃。
- [sys-diver](https://github.com/ToruIwashita/sys-diver-zsh) - 用于目录更改或编辑器启动的 ZSH 插件，只需使用小部件进行关键操作，无需键入命令。
- [sysadmin-util](https://github.com/skx/sysadmin-util) - Steve Kemp 为系统管理员提供的工具脚本集合。
- [system-clipboard](https://github.com/kutsan/zsh-system-clipboard) - 添加了对“vi”模拟键盘映射的 ZLE（ZSH 行编辑器）剪贴板操作的键绑定支持。它可以在 Linux、macOS 和 Android 下运行（通过 Termux）。
- [system-update](https://github.com/cnlee1702/zsh-system-update) - 用于 [oh-my-zsh](https://ohmyz.sh/) 的智能、高效的系统更新插件，可处理 APT 包、Conda 环境和 pip 安装，并具有智能缓存，以最大限度地减少更新时间。
- [systemd](https://github.com/le0me55i/zsh-systemd) - 为“systemd”添加许多别名。
- [t3-shortcuts](https://github.com/murat-yasar/zsh-t3-shortcuts) - 处理 TYPO3 项目的快捷方式。提供快速导航命令来跳转 TYPO3 项目目录。
- [t32](https://github.com/chrissicool/zsh-t32) - Lauterbach Trace32 工具集的插件。它会自动注册字体并设置运行 t32 工具集所需的所有环境变量。
- [tab-title (p1r473)](https://github.com/p1r473/tab-title/) - 重命名 [tmux](https://github.com/tmux/tmux/wiki) 和 [screen](https://www.gnu.org/software/screen/manual/screen.html) 窗格和窗口。
- [tab-title (trystan2k)](https://github.com/trystan2k/zsh-tab-title) - 根据当前目录或正在运行的进程设置终端选项卡标题。从 [termsupport.zsh](https://github.com/ohmyzsh/ohmyzsh/blob/master/lib/termsupport.zsh) 分叉。
- [tailf](https://github.com/rummik/zsh-tailf) - 添加带有前缀换行符而不是尾随换行符的“tailf”函数。
- [take](https://github.com/amyreese/zsh-take) - 复制 [oh-my-zsh](https://ohmyz.sh/) 中的 `take`。
- [tasko](https://github.com/knid/tasko) - 允许您注释 [TaskWarrior](https://github.com/GothenburgBitFactory/taskwarrior) 任务。
- [telepresence](https://github.com/alexgervais/telepresence-ps1) - 将当前的 [Telepresence](https://www.telepresence.io/) 连接状态和上下文添加到 ZSH 提示符中。
- [temperatures](https://github.com/groberth/temperatures-zsh) - 一个轻量级、零依赖的插件，可直接在 ZSH 提示符中显示机器的 CPU 和（可选）GPU 温度。最初是为 Raspberry Pi 设计的，但适用于任何公开 `/sys/class/Thermal/` 的 Linux 系统。
- [tempit](https://github.com/idirxv/tempit) - 帮助您轻松创建、管理和导航临时目录。它提供了持久的跟踪系统，因此您的临时目录不会丢失。
- [terminal-aliases](https://github.com/dvir-levy/terminal-aliases) - 为 `terraform`、`git` 等添加了方便的别名。
- [terminal-app](https://github.com/the8/terminal-app.zsh) - 用于与新的 macOS El Capitan Terminal.app 功能集成的插件。
- [terminal-title](https://github.com/AnimiVulpis/zsh-terminal-title) - 添加“set-term-title”函数，可用于为终端窗口添加标题。
- [terminal-workload-report](https://github.com/LockonS/terminal-workload-report) - 一个计算并显示通过终端运行了多少命令的插件。
- [termux](https://github.com/zpm-zsh/termux) - 添加了对 [Termux](https://termux.com/) 的兼容性。
- [terraform (hanjunlee)](https://github.com/hanjunlee/terraform-oh-my-zsh-plugin) - 添加 [terraform](https://www.terraform.io/) 工作区以进行提示。
- [terraform (jsporna)](https://github.com/jsporna/terraform-zsh-plugin) - 使用别名和制表符补全功能扩展了原始的 [oh-my-zsh](https://ohmyz.sh/) 插件。将工作区（非默认情况下）添加到提示中。
- [terraform (macunha1)](https://github.com/macunha1/zsh-terraform) - 添加 [terraform](https://terraform.io/) 的便捷别名、选项卡补全和帮助函数，以在提示中添加 terraform 工作区。
- [terraform (ptavares)](https://github.com/ptavares/zsh-terraform) - 添加别名、函数和制表符补全。还安装 [terraform-docs](https://github.com/terraform-docs/terraform-docs)、[tfsec](https://github.com/aquasecurity/tfsec) 和 [tflint](https://github.com/terraform-linters/tflint)。
- [terraform (thuandt)](https://github.com/thuandt/zsh-terraform) - 添加 [terraform](https://terraform.io/) 的便捷别名，以及“terraform”和“terragrunt”的补全。
- [terragrunt](https://github.com/hanjunlee/terragrunt-oh-my-zsh-plugin) - [Terragrunt](https://github.com/gruntwork-io/terragrunt) 插件，[Terraform](https://terraform.io/) 的瘦包装器，提供额外的工具。
- [tfaws](https://github.com/jmischler72/tfaws) - 简化 AWS 和 Terraform 之间的上下文切换。提供自动 AWS SSO 登录、使用“.awsprofile”文件自动配置文件切换，并将 terraform 工作区/文件夹链接到配置文件。
- [tfenv](https://github.com/CDA0/zsh-tfenv) - 安装、更新和加载受 [zsh-pyenv](https://github.com/mattberther/zsh-pyenv) 启发的 `tfenv`
- [tfswitch](https://github.com/ptavares/zsh-tfswitch) - 安装并加载 [tfswitch](https://github.com/warrensbox/terraform-switcher)。
- [tgenv](https://github.com/ptavares/zsh-tgenv) - 安装并加载 [tgenv](https://github.com/cunymatthieu/tgenv.git)。包括手动更新“tgenv”的功能。
- [tgswitch](https://github.com/ptavares/zsh-tgswitch) - 安装并加载 [tgswitch](https://github.com/warrensbox/tgswitch)。
- [thefuck](https://github.com/laggardkernel/thefuck) - 加载具有缓存支持的 [thefuck](https://github.com/nvbn/thefuck)（一种纠正之前命令的工具），从而大大减少加载时间。
- [theia-dev-tools](https://github.com/taPublic/zsh-theia-dev-tools) - 使用 [theia-ide](https://github.com/theia-ide/theia) 的便捷功能。
- [tig](https://github.com/MenkeTechnologies/zsh-tig-plugin) - 为 [tig](https://github.com/jonas/tig) 添加一些高级绑定，并提供 `tig-pick` 脚本。
- [time-tracker](https://github.com/mike-fam/time-tracker-plugin) - 自动跟踪跨多个存储库的“git”分支所花费的时间。非常适合想要了解不同项目和分支之间的时间分配的开发人员。
- [timewarrior (ianmkenney)](https://github.com/ianmkenney/timewarrior_zsh_completion) - [timewarrior](https://timewarrior.net/) 时间跟踪应用程序的 Tab 补全。
- [timewarrior (svenXY)](https://github.com/svenXY/timewarrior) - 添加了对时间跟踪应用程序 [timewarrior](https://timewarrior.net/) 的支持。
- [tinted-shell](https://github.com/tinted-theming/tinted-shell) - 添加一个脚本，允许您更改 shell 的默认 ANSI 颜色，但最重要的是，更改 shell 256 颜色空间的颜色 17 到 21（如果您的终端支持）。该脚本可以尊重 shell 的原始明亮颜色（例如亮绿色仍然是绿色等），同时为 [Vim](https://www.vim.org) 等应用程序提供额外的 base16 颜色。
- [tipz](https://github.com/molovo/tipz) - 如果您有刚刚运行的命令的别名，则显示您的别名，类似于 [alias-tips](https://github.com/djui/alias-tips)。
- [title](https://github.com/zpm-zsh/title) - 允许您设置终端窗口标题。
- [titles](https://github.com/jreese/zsh-titles) - [tmux](https://tmux.github.io) 和 xterm 兼容终端的自动窗口和选项卡标题。
- [tm](https://github.com/kjhaber/tm.zsh) - 简化了创建新的 [tmux](https://tmux.github.io) 会话、附加到现有会话、在会话之间切换以及列出活动会话。
- [tmux (zpm-zsh)](https://github.com/zpm-zsh/tmux) - [tmux](https://tmux.github.io) 插件。
- [tmux (zsh-contrib)](https://github.com/zsh-contrib/zsh-tmux) - [tmux](https://tmux.github.io) 插件。包括基于运行命令的自动窗口标题更新、执行期间的命令名称显示、作业引用解析（fg、%1）到实际命令名称以及自动标题截断（最多 20 个字符）。
- [tmux-auto-title](https://github.com/mbenford/zsh-tmux-auto-title) - 自动将窗口/窗格的标题设置为当前前台命令。
- [tmux-rename](https://github.com/sei40kr/zsh-tmux-rename) - 自动重命名 [tmux](https://tmux.github.io) 窗口。
- [tmux-sessionizer](https://github.com/nikevsoft/tmux-sessionizer) - ThePrimeagen 上看到的 [tmux](https://tmux.github.io) 会话程序。
- [tmux-simple](https://github.com/TBSliver/zsh-plugin-tmux-simple) - 用于将 [tmux](https://tmux.github.io) 与 ZSH 结合使用的简单插件。
- [tmux-ssh-syncing](https://github.com/alberti42/tmux-ssh-syncing) - 将“tmux”窗口名称与活动的“ssh”会话同步。该插件动态更新 [`tmux`](https://tmux.github.io) 窗口名称，以反映同一窗口中活动的 `ssh` 会话的远程主机。当所有“ssh”会话关闭时，它还会恢复原始窗口名称。
- [tmux-vim-integration](https://github.com/jsahlen/tmux-vim-integration.plugin.zsh) - 从相邻的 [tmux](https://tmux.github.io) 窗格在正在运行的“vim”（或 NeoVim）会话中打开文件。
- [tmux-zsh-vim-titles](https://github.com/MikeDacre/tmux-zsh-vim-titles) - 为“tmux”、ZSH 和 Vim/NVIM 创建统一的模块化终端标题。
- [tmuxrepl](https://github.com/csurfer/tmuxrepl) - 简单的 ZSH 插件，具有 R-EP-L [tmux](https://tmux.github.io) 会话。
- [todotxt](https://github.com/Neluji/omz-todotxt) - 添加 [todo.sh](https://github.com/benignoc/alfred-todotxt/) 的别名。
- [toggl](https://github.com/natterstefan/toggl-zsh-plugin) - 添加“toggl-week”命令以显示 [toggl.com](https://toggl.com) 上跟踪的总工作时间
- [toggle-command-prefix](https://github.com/xPMo/zsh-toggle-command-prefix) - 添加一个小部件以切换命令的前缀。默认情况下，将 Alt+s 绑定到命令前面加上“sudo”。
- [toolbox](https://github.com/paxcoder/zsh-toolbox) - 自动更新 [homebrew](https://brew.sh) 插件。允许在启动和别名设置期间启用/禁用通知。
- [touchplus](https://github.com/raisedadead/zsh-touchplus) - 使用包含路径的“touch”创建文件。
- [traista](https://github.com/exaluc/traista) - 包括上次命令运行的“git”状态装饰和颜色编码的退出状态。深色终端主题效果更好。
- [travis](https://github.com/denolfe/zsh-travis) - 打开当前存储库的 [Travis CI](https://www.travis-ci.com/) 页面（如果存在）。
- [tre](https://github.com/redxtech/zsh-tre) - 使使用 [tre](https://github.com/dduan/tre#editor-aliasing) 更容易。
- [tsm](https://github.com/RobertAudi/tsm) - 添加 [tmux](https://tmux.github.io) 会话管理器。
- [tumult](https://github.com/unixorn/tumult.plugin.zsh) - 添加适用于 macOS 的工具。
- [ubuntualiases](https://github.com/GuilleDF/zsh-ubuntualiases) - Ubuntu 16 别名。
- [ugit](https://github.com/Bhupesh-V/ugit) - 允许您撤消上次的“git”操作。
- [uncloudium](https://github.com/Talon1024/omz-uncloudium) - 添加帮助程序脚本以从 Google Chrome 网上商店下载 crx 文件。
- [undo-dir](https://github.com/allisnulll/zsh-undo-dir) - 撤消和重做当前工作目录更改。
- [undollar](https://github.com/zpm-zsh/undollar) - 从终端提示符的开头去除美元符号。
- [unique-id](https://github.com/z-shell/zsh-unique-id) - 在其 shell 变量“$ZUID_ID”中提供标识正在运行的 Zshell 会话的唯一编号。除了这个唯一的数字之外，还在 shell 变量“$ZUID_CODENAME”中提供了唯一的代号。一个示例用例是将日志保存在文件“.../mylog-${ZUID_CODENAME}.log”中，以便两个不同的 Zshell 不会同时写入同一文件。
- [unix-simple](https://github.com/redxtech/zsh-unix-simple) - 一个以图形方式显示 UNIX 简单性的命令。
- [unraid](https://github.com/donbuehl/zsh-unraid) - 添加方便的别名和功能，用于直接从命令行管理 Unraid 服务器。
- [unwrap](https://github.com/foxleigh81/unwrap-zsh-plugin) - 允许您删除目录而不删除内容 - 它将它们放在该目录的父目录中。
- [up (cjayross)](https://github.com/cjayross/up) - 一种在目录中向上导航的简单方法。
- [up (peterhurford)](https://github.com/peterhurford/up.zsh) - 将向上命令添加到“cd”多个级别。
- [up-dir](https://github.com/sgpthomas/zsh-up-dir) - 将 `ctrl-h` 绑定到向上导航目录。这使得无需输入任何命令即可轻松访问几个目录。
- [update-zsh](https://github.com/AndrewHaluza/zsh-update-plugin) - 更新自定义 [oh-my-zsh](https://ohmyz.sh/) 插件。仅适用于 oh-my-zsh 框架。
- [url-highlighter](https://github.com/ascii-soup/zsh-url-highlighter) - ZSH 语法荧光笔的插件，如果 URL 响应“良好”状态，则将其变为绿色，否则变为红色。对于检查 URL 拼写错误很有用。
- [usb](https://github.com/NiziL/usb.plugin.zsh) - 一个用于快速安装和卸载 USB 驱动器的小插件。
- [uv-env](https://github.com/matthiasha/zsh-uv-env) - 自动使用[uv](https://github.com/astral-sh/uv)激活基于当前目录的虚拟环境。
- [uvenv](https://github.com/vincentto13/uvenv.plugin.zsh) - 扩展了原始 [oh-my-zsh](https://ohmyz.sh/) `venv` 模块的功能。
- [vagrant-box-wrapper](https://github.com/evanthegrayt/vagrant-box-wrapper) - [vagrant](https://www.vagrantup.com/) 的包装插件，允许从 box 目录外部调用“vagrant”命令。该插件还附带了一些额外的命令，有助于管理多个框，以及自定义选项卡完成。
- [valet (A909M)](https://github.com/A909M/valet-zsh-plugin) - 适用于 Debian/Ubuntu 上的 [Laravel Valet](https://laravel.com/docs/valet) 和 [Valet Linux](https://cpriego.github.io/valet-linux/)。提供智能自动完成、有用的别名和实用函数来简化您的本地开发工作流程。
- [valet (NasirNobin)](https://github.com/NasirNobin/zsh-valet/) - 从项目根目录读取 `.valetphprc` 并自动切换到该 PHP 版本。
- [vanilli.sh](https://github.com/yous/vanilli.sh) - shell 配置的轻量级起点。
- [vapor](https://github.com/notf0und/zsh-vapor) - Laravel [vapor](https://github.com/laravel/vapor-cli) ZSH 插件可帮助您从项目树中的任何位置运行“vapor”，并自动完成！
- [vcshr](https://github.com/aubreypwd/zsh-plugin-vcshr) - 帮助 vcsh 用户使用 `vcsh` 需要 GitHub 存储库，以便在 `~/.zshrc` 等中自动安装。
- [velocity](https://github.com/rahulsalvi/velocity-python) - ZSH 和 [tmux](https://tmux.github.io) 的基于 Powerline 的主题元素。
- [venv-lite](https://github.com/gimbo/venv-lite.zsh) - [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/) 的超轻量级克隆；它几乎希望您使用 [pyenv](https://github.com/pyenv/pyenv)（尽管您*不必），并且因为它基于 [`venv` 模块](https://docs.python.org/3/library/venv.html)，所以（创建）仅适用于 python >= 3.3。
- [venv-wrapper](https://github.com/glostis/venv-wrapper) - 提供 ZSH 功能，以便使用“venv”轻松管理虚拟环境。
- [venv](https://github.com/lucasheartcliff/venv) - 每次当前目录中有“venv/bin/activate”文件的路径时，都会自动运行“source venv/bin/activate”。
- [venvs](https://github.com/pawnhearts/venvs) - 自动切换 Python virtualenvs。支持项目文件夹（`~/myproject/venv`）和全局文件夹（如`~/.virtualenvs`）中的 venvs
- [vi-increment](https://github.com/zsh-vi-more/vi-increment) - 添加类似“vim”的递增/递减操作。
- [vi-mode (jeffreytse)](https://github.com/jeffreytse/zsh-vi-mode) - 💻 ZSH 更好、更友好的 `vi`(`vim`) 模式插件。
- [vi-mode (nyquase)](https://github.com/Nyquase/vi-mode) - 添加额外的类似“vi”的功能。
- [vi-mode (sinetoami)](https://github.com/sinetoami/vi-mode) - 向 ZSH 添加更多类似“vi”的功能。
- [vi-motions](https://github.com/zsh-vi-more/vi-motions) - 添加新的动作和文本对象，包括带引号/括号的文本和命令。
- [vi-quote](https://github.com/zsh-vi-more/vi-quote) - 添加引用或取消引用动议的操作。
- [viexchange](https://github.com/okapia/zsh-viexchange) - 一个“vi”模式插件，用于在缓冲区中的两个位置之间轻松交换文本，例如 vim-exchange。
- [vim-mode](https://github.com/softmoth/zsh-vim-mode) - 友好的“vi”模式绑定，添加基本的 Emacs 键、增量搜索、模式指示器等。
- [vim-plugin](https://github.com/nviennot/zsh-vim-plugin) - 允许您执行 `vim filename:123` 打开文件，并将光标置于特定行。
- [vimman](https://github.com/yonchu/vimman) - 查看 `vim` 插件手册（帮助），就像 ZSH 中的 `man` 一样。
- [vimto](https://github.com/laurenkt/zsh-vimto) - 改进了 ZSH `vi` 模式（bindkey -v）插件。
- [virtualenv-mod](https://github.com/mattcl/virtualenv-mod) - 修改后的 virtualenv ZSH 插件 [oh-my-zsh](https://ohmyz.sh)。
- [virtualenv-prompt](https://github.com/tonyseek/oh-my-zsh-virtualenv-prompt) - 来自上游 [oh-my-zsh](https://ohmyz.sh/) 的 virtualenv 插件的分支。添加对在 [oh-my-zsh](https://ohmyz.sh) 主题中自定义 virtualenv 提示符的支持。
- [virtualz](https://github.com/aperezdc/virtualz) - Python [virtualenv](https://virtualenv.pypa.io/en/latest/) 管理器受到 Adam Brenecki 的 [Virtualfish](https://github.com/adambrenecki/virtualfish) 的启发，用于 [Fish shell](http://fishshell.com/)，取代了 virtualenvwrapper。
- [virtuozzo-plugin](https://github.com/TamCore/virtuozzo-zsh-plugin) - 用于 [virtuozzo](https://docs.virtuozzo.com/master/index.html) 裸机虚拟化系统的 [oh-my-zsh](https://ohmyz.sh/) 插件。
- [visit](https://github.com/justinpchang/visit) - 自定义插件可实现更快的导航。
- [vivi](https://github.com/rufevean/vivi) - 将 Google 的 [Gemini](https://gemini.google.com) 语言模型 (LLM) 功能直接集成到您的终端中。它允许您向语言模型发送查询并接收人工智能生成的解决方案，所有这些都在您的终端内进行。该插件支持会话上下文，可以动态执行接收到的命令。
- [vivid](https://github.com/ryanccn/vivid-zsh) - 通过 [vivid](https://github.com/sharkdp/vivid) 更轻松地使用“LSCOLORS”。
- [vivid](https://github.com/zsh-contrib/zsh-vivid) - 用于 [vivid](https://github.com/sharkdp/vivid) 集成的插件，可生成和导出具有主题支持的“LS_COLORS”。
- [volta (cowboyd)](https://github.com/cowboyd/zsh-volta) - 无缝安装和配置 [Volta](https://volta.sh) Node.js 工具链管理器。
- [volta](https://github.com/ri7nz/zsh-volta) - 安装并加载 [Volta：JS 工具链作为代码](https://github.com/volta-cli/volta)。
- [vox](https://github.com/andrewbonnington/vox.plugin.zsh) - 一个 [oh-my-zsh](https://ohmyz.sh/) 插件，用于控制 [VOX](https://vox.rocks/)，这是一款适用于 macOS 的轻量级全功能音频播放器，可以播放多种格式，包括 FLAC 和 Ogg Vorbis。
- [vsc](https://github.com/davidtong/vsc.plugin.zsh) - macOS 上 [Visual Studio Code](https://code.visualstudio.com/) 的插件。
- [vscode (kasperhesthaven)](https://github.com/kasperhesthaven/vscode) - 简单的插件，可以更轻松地跨系统打开 [Visual Studio Code](https://code.visualstudio.com/)。
- [vscode (qianxinfeng)](https://github.com/qianxinfeng/zsh-vscode) - [Visual Studio Code](https://code.visualstudio.com/) 插件。
- [vscode-shell-integration](https://github.com/tolkonepiu/vscode-shell-integration-zsh-plugin) - 在 VS Code 终端中工作时，自动激活 [VS Code shell 集成](https://code.visualstudio.com/docs/terminal/shell-integration)。
- [vterm](https://github.com/randomphrase/vterm-zsh-plugin) - 允许您直接从 [vterm](https://github.com/vterm/vterm) shell 会话运行“emacs”命令。
- [vtex](https://github.com/xdigu/zsh-vtex) - 为 [vtex](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-vtex-io-cli-command-reference#default-commands) cli 命令添加帮助程序别名。
- [wakatime (sobolevn)](https://github.com/sobolevn/wakatime-zsh-plugin) - 跟踪您在终端上花费了多少[时间](https://wakatime.com/)。有每个项目的统计数据。
- [wakatime (wbingli)](https://github.com/wbingli/zsh-wakatime) - 使用 [wakatime](https://wakatime.com/) 自动跟踪 ZSH 中的命令时间。
- [warhol](https://github.com/unixorn/warhol.plugin.zsh) - 使用 [grc](https://github.com/garabik/grc) 配置着色。
- [warrior](https://github.com/OfferPi/zsh-warrior) - 使用本地大语言模型 ([Ollama](https://ollama.com/)) 将自然语言翻译为 ZSH 命令。
- [watch](https://github.com/enrico9034/zsh-watch-plugin) - 按“CTRL + W”即可轻松为当前或之前的命令加上 watch 前缀。
- [watson.zsh](https://github.com/bcho/Watson.zsh) - [watson](https://github.com/TailorDev/Watson) 时间管理系统的插件。
- [wd](https://github.com/mfaerevaag/wd) - Warp 目录允许您跳转到 ZSH 中的自定义目录，而无需使用“cd”。为什么？因为当文件夹被频繁访问或路径较长时，“cd”似乎效率低下。
- [web-search (anant-mishra1729)](https://github.com/Anant-mishra1729/web-search/) - 添加别名，以便直接从命令行使用 Google、Bing、Wiki、YouTube、Yahoo、Duck Duck Go、GitHub、Stack Overflow 和其他服务进行搜索。
- [web-search (sinetoami)](https://github.com/sinetoami/web-search) - 添加命令以直接从 CLI 运行 bing、google、yahoo 和 duckduckgo 搜索。
- [web-search (yabanahano)](https://github.com/Yabanahano/web-search) - 添加用于使用 Google、Wiki、Bing、YouTube 和其他流行服务进行搜索的别名。
- [welcome-banner](https://github.com/joshuadanpeterson/zsh-welcome-banner) - 显示带有随机报价的登录横幅。
- [westchange](https://github.com/TomiVidal99/westchange) - 允许您在目录之间快速切换。需要 [fzf](https://github.com/junegunn/fzf)。
- [which-jspm](https://github.com/zkuzmic/which-jspm/) - 根据在当前目录中检测到的锁定文件，将 `npm`、`yarn` 或 `pnpm` 添加到提示符末尾。
- [whisp](https://github.com/jaacob/whisp) - 为 OpenAI 的 Whisper CLI 工具添加幂等性和便利功能。它可以帮助您高效地转录音频文件，而无需重复工作。
- [whobrokemycode](https://github.com/cameronbroe/whobrokemycode) - 使用“gitblame”突出显示文件中最后更改特定行的位置。
- [window-title](https://github.com/olets/zsh-window-title) - 向您的终端窗口添加信息图块。
- [windows-title](https://github.com/mdarocha/zsh-windows-title) - 使用当前目录和最后运行的命令动态更新终端窗口标题。
- [wordle](https://github.com/zechris/zwordle) - Wordle for ZSH，带有制表符补全功能。
- [workon](https://github.com/bryanculver/workon.plugin.zsh) - 用于在项目之间跳转的简单实用程序。
- [worktree](https://github.com/jspears/worktree) - 添加包装 `git worktree` 的函数。
- [wpm](https://github.com/btror/wpm) - 让您可以测试终端中的打字速度、跟踪 WPM、准确性等。结果以方便的 JSON 格式保存，以便于跟踪。
- [wsl](https://github.com/florentinl/omz-wsl) - 添加辅助函数，以便在 WSL 中运行时更轻松地在 ZSH 中工作。
- [wsl2-ssh-pageant](https://github.com/antoinemartin/wsl2-ssh-pageant-oh-my-zsh-plugin) - 使用 Yubikey 存储的来自 WSL 的 GPG 密钥。这会将 [wsl2-ssh-pageant repo](https://github.com/BlackReloaded/wsl2-ssh-pageant) 中的指令打包为 ZSH 插件。
- [xdg-basedirs](https://github.com/krahlos/xdg-basedirs) - 根据 [XDG 基目录规范](https://specations.freedesktop.org/basedir-spec/latest/) 设置 XDG 基目录。该插件可确保您的环境配置正确，用于存储用户数据、缓存和配置文件。
- [xxh (ninagrosse)](https://github.com/ninagrosse/xxh-plugin-zsh-ohmyzsh) - [xxh](https://github.com/xxh/xxh) 插件需要 [xxh-plugin-prerun-cli-tools](https://github.com/ninagrosse/xxh-plugin-prerun-cli-tools)。
- [xxh (roman-geraskin)](https://github.com/roman-geraskin/xxh-plugin-zsh-zshrc) - [xxh-shell-zsh](https://github.com/xxh/xxh-shell-zsh) 的插件，将 `~/.zshrc` 复制到远程主机并使用 [xxh-shell-zsh](https://github.com/xxh/xxh-shell-zsh) 获取它。
- [yadm](https://github.com/juanrgon/yadm-zsh) - 如果本地“yadm”配置发生更改，则显示警告。
- [yapipenv](https://github.com/AnonGuy/yapipenv.zsh) - 如果“pipenv”检测到目录的“pip”环境存在，则自动激活目录的“pip”环境。
- [yazi-mount](https://github.com/splixx05/zsh-yazi-mount) - 通过 `udisksctl` 挂载 USB 分区，在 [yazi](https://github.com/sxyazi/yazi) 中打开它们，然后卸载它们 – 安全、干净且用户友好。
- [yazi-zoxide](https://github.com/fdw/yazi-zoxide-zsh) - 这个 [zsh](https://www.zsh.org) 插件只添加了一个快捷方式，但却展现了 [Zicide](https://github.com/ajeetdsouza/zride) 和 [yazi](https://github.com/sxyazi/yazi/) 的魔力。如果没有参数，`y`只会打开 yazi。如果您提供一个目录参数，则会在该目录中打开“yazi”。但是，如果您提供其他任何内容作为参数，则会使用该参数调用“zoxy”，并在此处打开“yazi”。
- [yeoman](https://github.com/edouard-lopez/yeoman-zsh-plugin) - Edouard Lopez 的 [Yeoman](http://yeoman.io/) 插件 [oh-my-zsh](https://ohmyz.sh/)，与 yeoman 版本 ≥1.0 兼容（包括选项和命令自动完成）。
- [you-should-use](https://github.com/MichaelAquilina/zsh-you-should-use) - ZSH 插件会提醒您使用您定义的别名。
- [youtube-dl-aliases](https://github.com/katrinleinweber/oh-my-zsh-youtube-dl-aliases) - 添加“yt”别名以从 YouTube 下载视频。
- [youtube-dl](https://github.com/joow/youtube-dl) - [youtube-dl](https://youtube-dl.org/) 的简单插件。
- [yup](https://github.com/redxtech/zsh-yup) - 添加辅助函数来升级 `yarn`/`npm` 项目中的所有依赖项。
- [z.lua](https://github.com/skywind3000/z.lua) - 一个命令行工具，可帮助您通过了解习惯来更快地导航。 [z.sh](https://github.com/rupa/z) 的替代方案，具有 Windows 和 posix shell 支持和各种改进。比 [fasd](https://github.com/whjvenyl/fasd) 和 autojump 快 10 倍，比 [z.sh](https://github.com/rupa/z) 快 3 倍。
- [zabb](https://github.com/Mellbourn/zabb) - `zabb` 是一个命令，它尝试找出目录的最短的令人难忘的缩写，[z](https://github.com/ajeetdsouza/zicide)可以使用该缩写来明确跳转到该目录。
- [zabrze](https://github.com/Ryooooooga/zabrze) - 一个 ZSH 缩写扩展插件。
- [zapmarks](https://github.com/iliutaadrian/zapmarks) - 提供对最常用的命令行书签的快速访问。它允许您轻松保存、搜索和执行复杂的命令。
- [zaw-src-package-managers](https://github.com/GeneralD/zaw-src-package-managers) - 用于多个包管理器的 [zaw](https://github.com/zsh-users/zaw) 的可选源：[rubygem](https://rubygems.org/) (ruby)、[pypi](https://pypi.python.org/pypi) (python)、[clib](https://github.com/clibs/clib) (C)、[appstore](https://github.com/mas-cli/mas) (Mac App Store)、 [homebrew](https://brew.sh/)（Mac CUI 应用程序）、[brewcask](https://caskroom.github.io/)（Mac GUI 应用程序）
- [zaw](https://github.com/zsh-users/zaw) - ZSH everything.el 之类的小部件。
- [zbrowse](https://github.com/zdharma-continuum/zbrowse) - 在进行 shell 工作时，经常会多次调用 `echo $variable`，以检查循环结果等。使用 ZBrowse，您只需按 `Ctrl-B`，即可调用 ZBrowse – Zshell 变量浏览器。
- [zce](https://github.com/hchbaw/zce.zsh) - Vim 的 EasyMotion / Emacs 的 ZSH 的 ace-jump-mode。
- [zcolors](https://github.com/marlonrichert/zcolors) - 使用 `$LS_COLORS` 为 Git 和 Zsh 提示符、补全和 [ZSH 语法突出显示](https://github.com/zsh-users/zsh-syntax-highlighting) 生成一致的主题。
- [zconvey](https://github.com/zdharma-continuum/zconvey) - 添加了向其他 ZSH 会话发送命令的功能，例如，您可以使用它在所有活动的 ZSH 会话上使用“cd $PWD”。
- [zed](https://github.com/eendroroy/zed-zsh) - 一个简单的 [z](https://github.com/rupa/z) 包装器，用于通过 ZSH 插件安装它。
- [zellij (jaeheonji)](https://github.com/jaeheonji/zsh-zellij-plugin) - 提供使用[zellij](https://github.com/zellij-org/zellij)的环境。需要[tmux](https://github.com/tmux/tmux)。已被作者弃用，现在[本地支持](https://zellij.dev/documentation/integration.html#autostart-on-shell-creation)。
- [zellij (tranzystorek-io)](https://codeberg.org/tranzystorekk/zellij.zsh) - 提供一个自动启动 [zellij](https://github.com/zellij-org/zellij) 作为终端多路复用器的环境。
- [zeno](https://github.com/yuki-yano/zeno.zsh) - 由 [Deno](https://deno.land/) 提供支持的模糊补全和实用插件。
- [zenplash](https://github.com/Chivier/zenplash) - 从存储在用户目录中的模板创建文件。
- [zenv](https://github.com/janitha/zenv) - 每个目录隔离工作 shell 环境（如 `direnv`，但使用新的 shell 实例来提供更清晰的隔离）。
- [zero](https://github.com/arlimus/zero.zsh) - 零既是一个插件，又是一个主题。有关安装详细信息，请参阅 GitHub 页面。包括 `git` 和 `hg` 状态装饰器。
- [zeza](https://github.com/duggum/zeza) - 管理和自定义 [eza](https://github.com/eza-community/eza)，非常丰富多彩的“ls”替代品。
- [zflai](https://github.com/zdharma-continuum/zflai) - ZSH 的快速日志记录框架。
- [zfzf](https://github.com/b0o/zfzf) - 一个由 [fzf](https://github.com/junegunn/fzf) 支持的 ZSH 文件选择器，可让您快速导航目录层次结构。
- [zgen-compinit-tweak](https://github.com/seletskiy/zsh-zgen-compinit-tweak) - 在[zgen](https://github.com/tarjoilija/zgen)完成所有加载后，使compinit仅运行一次。
- [zgenom-ext-eval](https://github.com/jandamm/zgenom-ext-eval/) - [zgenom](https://github.com/jandamm/zgenom) 用于创建内联插件的扩展。
- [zhooks](https://github.com/agkozak/zhooks) - 显示任何 ZSH 挂钩数组的内容以及已定义的任何挂钩函数的代码。对于调试很有用。
- [zi-rbenv](https://github.com/z-shell/zi-rbenv) - 如果您使用 [zi](https://github.com/z-shell/zi/)，则可以快速加载 `rbenv`。
- [zimfw-extras](https://github.com/PatTheMav/zimfw-extras) - [zimfw](https://github.com/zimfw/zimfw) 的自定义附加功能，打包到 zimfw 插件中。
- [zinfo_line](https://github.com/kmhjs/zinfo_line) - 为 ZSH 主题提供更多信息。
- [zinit-annex-bin-gem-node](https://github.com/zdharma-continuum/zinit-annex-bin-gem-node) - [zinit](https://github.com/zdharma-continuum/zinit) 扩展可在不更改 `$PATH` 的情况下公开二进制文件，安装 Ruby gems 和 Node 模块并轻松公开其二进制文件，并在更新关联的插件或代码片段时更新 gems 和模块。
- [zinit-annex-default-ice](https://github.com/zdharma-continuum/zinit-annex-default-ice) - 允许用户为多个 zinit 命令定义ices活动状态。
- [zinit-annex-man](https://github.com/zdharma-continuum/zinit-annex-man) - [Zinit](https://github.com/zdharma-continuum/zinit) 扩展，可为所有插件和片段生成手册页
- [zinit-annex-meta-plugins](https://github.com/zdharma-continuum/zinit-annex-meta-plugins) - 安装具有单个标签的插件组（仅限 [zinit](https://github.com/zdharma-continuum/zinit)）。
- [zinit-annex-patch-dl](https://github.com/zdharma-continuum/zinit-annex-patch-dl) - [zinit](https://github.com/zdharma-continuum/zinit) 扩展，通过提供的 `dl` 和 `patch` zinit 冰下载文件并应用补丁。
- [zinit-annex-readurl](https://github.com/zdharma-continuum/zinit-annex-readurl) - 添加了自动下载网页上托管 URL 的文件的最新版本的功能。
- [zinit-annex-rust](https://github.com/zdharma-continuum/zinit-annex-rust) - [zinit](https://github.com/zdharma-continuum/zinit) 扩展，用于在插件目录中安装 Rust 和 Cargo 包。
- [zinit-annex-submods](https://github.com/z-shell/z-a-submods) - [zinit](https://github.com/zdharma-continuum/zinit) 扩展，允许在插件或代码片段中安装和管理其他子模块。
- [zinit-annex-test](https://github.com/NorthIsMirror/z-a-test) - [zinit](https://github.com/zdharma-continuum/zinit) 扩展运行测试（例如通过 make test）——如果它找到其中任何一个——在安装和更新插件或代码片段之后。
- [zinit-annex-unscope](https://github.com/zdharma-continuum/zinit-annex-unscope) - 允许在不通过查询 Github API 指定用户名的情况下安装 [zinit](https://github.com/zdharma-continuum/zinit) 插件。
- [zinit-console](https://github.com/z-shell/zinit-console) - [zinit](https://github.com/zdharma-continuum/zinit) 插件管理器的半图形（curses）控制台。
- [zinsults](https://github.com/ahmubashshir/zinsults) - 如果命令失败则打印侮辱。
- [zjump](https://github.com/qoomon/zjump) - 简化ZSH目录导航；跳转到已访问过的父文件夹或子文件夹。
- [zledit](https://github.com/Piotr1215/zledit) - 通过覆盖提示、预览面板和就地编辑，模糊跳转到 ZSH 命令行上的任何标记。需要 [fzf](https://github.com/junegunn/fzf)。
- [zlitefetch](https://github.com/ippee/zlitefetch) - 轻量级系统信息插件。
- [zload](https://github.com/mollifier/zload) - ZSH 功能的热重载。实现快速发展。
- [zlong_alert](https://github.com/kevinywlui/zlong_alert.zsh) - 使用“notify-send”并在需要很长时间（默认值：15 秒）的命令完成时敲响铃声来提醒您。
- [zman](https://github.com/mattmc3/zman) - 使用[fzf](https://github.com/junegunn/fzf)快速浏览ZSH手册。
- [znotify](https://github.com/rudeigerc/znotify) - 一个简单的插件，用于向其他服务发送通知。
- [znvm](https://github.com/Ajnasz/znvm) - ZSH 的 [Node.js](https://nodejs.org) 版本管理器类似于 [nvm.sh](https://github.com/nvm-sh/nvm)，但速度更快。
- [zoc](https://github.com/TomerG2/zoc) - 加快 OpenShift `oc` 登录和令牌更新速度。
- [zoxide](https://github.com/ajeetdsouza/zoxide) - “cd”的快速替代品，可以了解您的习惯。
- [zplug-blame](https://github.com/jkcdarunday/zplug-blame) - 一个 [zplug](https://github.com/zplug/zplug) 特定插件，显示每个插件加载所需的时间。
- [zpy](https://github.com/AndydeCleyre/zpy) - 使用 [uv](https://github.com/astral-sh/uv) 或 [pip-tools](https://github.com/jazzband/pip-tools) 的 ZSH 前端管理 Python 环境、依赖项和独立的应用程序安装。
- [zramdisk](https://github.com/TomfromBerlin/zramdisk) - 用户友好的配置、创建、安装、卸载和管理压缩 RAM 磁盘。
- [zredis-cmd](https://github.com/z-shell/zredis-cmd) - 利用[zredis](https://github.com/zdharma-continuum/zredis)插件完成的变量共享来实现远程命令执行。
- [zredis](https://github.com/zdharma-continuum/zredis) - 添加 [Redis](https://redis.io/) 数据库支持，并带有 `database_key` <-> `shell_variable` 绑定。支持所有数据类型。
- [zservice-py3http](https://github.com/z-shell/zservice-py3http) - 使用标准库中的 Python 3 的 http 服务器为给定目录提供服务。
- [zsh-dev-navigator](https://github.com/dvigo/zsh-dev-navigator) - 一个最小的 ZSH 插件，可让您使用单个命令快速跳转到开发目录。
- [zsh-expand](https://github.com/MenkeTechnologies/zsh-expand) - 使用空格键扩展常规别名、全局别名以及不正确的拼写和短语。默认情况下也会扩展本机扩展，例如 glob、命令/进程替换、“=命令扩展”、历史扩展和“$parameters”，但可以将其关闭。
- [zsh-hookie-projects](https://github.com/aemonge/zsh-hookie-projects) - 通过智能挂钩、PowerLevel10k 集成和智能路径缩短进行与语言无关的项目检测。自动检测 100 多种项目类型，提供可定制的 on_project/off_project 挂钩，具有可转到项目根目录的智能“cd”命令，并包含一个漂亮的“hookie_dir”段，可缩短“~/projects/my-app”→“~/p/my-app”等路径。非常适合需要无缝项目感知 shell 行为的多语言开发人员。
- [zsh-in-docker](https://github.com/deluan/zsh-in-docker) - 自动将 ZSH + [oh-my-zsh](https://ohmyz.sh/) 安装到开发容器中。适用于 Alpine、Ubuntu、Debian、CentOS 或 Amazon Linux。
- [zsh-llm-assist](https://github.com/championswimmer/zsh-llm-assist) - 使用 Gemini CLI、Codex、Claude Code 或 OpenCode 的简单英语到 shell 命令建议以及 shell 命令到简单英语解释
- [zsh-make-completion](https://github.com/pksublime/zsh-make-completion) - 更正 zsh 的 `make` 选项卡补全。使用 make -qp 完全扩展 makefile 数据库，因此包含通过 $(eval $(call ...)) 生成的目标。结果按目录缓存，并在 Makefile 更改时自动失效。
- [zsh-not-vim](https://github.com/redxtech/zsh-not-vim) - 提供一个功能，自动让用户感到羞愧，因为他们忘记了他们不在“vim”中。
- [zsh-pkg-update-nag](https://github.com/madisonrickert/zsh-pkg-update-nag) - 在新 shell 启动时（频率限制为每 4 小时一次），检查您的 Homebrew 公式/桶、“npm -g”、“uv 工具”和 RubyGems 全局变量是否有可用更新，并在单个“Y/n/s”确认后提供升级它们。
- [zsh-select](https://github.com/z-shell/zsh-select) - 显示选择列表。它与`selecta`类似，但使用curses库进行显示，与[fzf](https://github.com/junegunn/fzf)相比，主要区别是近似匹配而不是模糊匹配。
- [zsh-vi-man](https://github.com/TunaCuma/zsh-vi-man) - zsh vi 模式的智能手册页查找。在任何命令或选项上按“Shift-K”即可立即打开其手册页，并可智能检测子命令、选项跳转、组合选项和管道支持。
- [zsh-watch](https://github.com/Thearas/zsh-watch) - 支持别名和补全的简单“watch”。
- [zsh-z (agkozak)](https://github.com/agkozak/zsh-z) - 快速跳转到您“最近”访问过的目录。 `z.sh` 的本机 ZSH 端口 - 没有 `awk`、`sed`、`sort` 或 `date`。
- [zsh-z (ptavares)](https://github.com/ptavares/zsh-z) - 安装并加载 [z](https://github.com/rupa/z.git)。
- [zshange_directory_recent](https://github.com/Kjeldgaard/zshange_directory_recent) - 更改到最近的目录。需要 [fzf](https://github.com/junegunn/fzf)。
- [zshcp](https://github.com/michaelsousajr/zshcp) - 适用于 Zsh 的轻量级且直观的剪贴板管理插件，可通过简单的复制粘贴操作增强命令行工作流程。
- [zshmarks](https://github.com/jocelynmallon/zshmarks) - Bashmarks 的端口（由 Todd Werth 开发），一个简单的命令行书签插件，用于 [oh-my-zsh](https://ohmyz.sh)。
- [zshrc-sync](https://github.com/Skylor-Tang/zshrc-sync) - 检测对 `.zshrc` 的更改，并在 `zsh` 退出时将它们推送到 github。
- [zshrc](https://github.com/freak2geek/zshrc) - 从项目范围加载本地“.zshrc”文件。
- [zshrpg](https://github.com/aliervo/zshrpg) - 一个将 [rpg-cli](https://github.com/facundoolano/rpg-cli/) 与 ZSH 完全集成的包装器！
- [zsnapac](https://github.com/johnramsden/zsh-zsnapac) - 用于在 Arch Linux 上拍摄 ZFS 升级前/升级后快照的插件。
- [zsnapshot](https://github.com/zdharma-continuum/zsnapshot) - 添加命令将当前 ZSH 状态转储到文件中，以便以后通过获取快照文件进行恢复。
- [ztouch](https://github.com/mjrafferty/ztouch) - 将最近历史命令、目录堆栈、模式之间循环和用户可映射命令的触摸栏控件添加到 macOS 上的触摸栏。
- [ztrace](https://github.com/zdharma-continuum/ztrace) - 捕获命令的输出，允许重用该输出，将其与历史内容粘合。
- [zui](https://github.com/zdharma-continuum/zui) - ZSH 用户界面库 – 使用 ZSH 进行类似 CGI+DHTML 的快速 TUI 应用程序开发。）
- [zypper-short](https://github.com/justanotherinternetguy/zypper-short) - OpenSuse Tumbleweed 的包管理器“zypper”的插件。

## 竣工数量

这些插件添加制表符补全，而不添加额外的函数或别名。

- [1password-op](https://github.com/unixorn/1password-op.plugin.zsh) - 加载 1Password 的 [op](https://developer.1password.com/docs/cli/get-started/) 命令行工具的自动补全功能。
- [aider](https://github.com/hmgle/aider-zsh-complete) - [aider](https://aider.chat/) 的 Tab 补全。
- [aircrack](https://github.com/Doc0x1/Aircrack-Zsh-Completions) - 添加了“airbase-ng”、“aircrack-ng”、“airdecap-ng”、“airdecloak-ng”、“aireplay-ng”、“airmon-ng”、“airodump-ng”、“airolib-ng”、“airserv-ng”、“airtun-ng”、“airventriloquist-ng”的补全。
- [alembic](https://github.com/datumbrain/oh-my-zsh-alembic) - 添加了 SQLAlchemy 数据库迁移工具 [Alembic](https://alembic.sqlalchemy.org/) 的补全。包括用于加快工作流程的辅助功能、命令别名和状态概览功能。
- [aliyun](https://github.com/thuandt/zsh-aliyun) - 添加[Aliyun CLI](https://github.com/aliyun/aliyun-cli)的补全。
- [ansible-server](https://github.com/viasite-ansible/zsh-ansible-server) - 完成 [viasite-ansible/ansible-server](https://github.com/viasite-ansible/ansible-server)。
- [antibody](https://github.com/sinetoami/antibody-completion) - 该插件为 [Antibody](https://github.com/getantibody/antibody) 插件管理器提供了完善功能。
- [appspec](https://github.com/perlpunk/App-AppSpec-p5) - 根据 YAML 规范生成 Bash 和 ZSH 的补全
- [argc-completions](https://github.com/sigoden/argc-completions) - 使用 [argc](https://github.com/sigoden/argc) 和 [jq](https://github.com/stedolan/jq) 添加 ZSH 选项卡补全。
- [atuin](https://github.com/marcelohmdias/zsh-atuin) - [Atuin](https://github.com/atuinsh/atuin) shell 历史记录系统的 Tab 补全。
- [audogombleed.sh](https://github.com/i-love-coffee-i-love-tea/audogombleed.sh) - 可以使用声明性语法轻松快速地生成完成文件，而无需编码。
- [autopkg-zsh-completion](https://github.com/fuzzylogiq/autopkg-zsh-completion) - autopkg 的完成情况。
- [aws_manager completions](https://github.com/EslamElHusseiny/aws_manager_plugin) - 添加“aws_manager”CLI 的补全。
- [aws-completions](https://github.com/eastokes/aws-plugin-zsh) - 添加对“awscli”的完成支持，以管理 AWS 配置文件/区域并在提示中显示它们。
- [bash-completions-fallback](https://github.com/3v1n0/zsh-bash-completions-fallback) - 当没有可用的本机 ZSH 时，支持命令的“bash”补全。
- [batect](https://github.com/batect/batect-zsh-completion/) - 为 [batect](https://batect.dev/) 构建系统添加选项卡补全。
- [berkshelf-completions](https://github.com/berkshelf/berkshelf-zsh-plugin) - 为berkshelf 添加制表符补全。
- [better-npm-completion](https://github.com/lukechilds/zsh-better-npm-completion) - 更好的“npm”选项卡补全。
- [bio](https://github.com/yamaton/zsh-completions-bio/) - 生物信息学工具的完成。
- [bitbake](https://github.com/antznin/zsh-bitbake) - 完成 [bitbake](https://git.openembedded.org/bitbake)。
- [bosh (krujos)](https://github.com/krujos/bosh-zsh-autocompletion) - 添加 [BOSH](https://github.com/cloudfoundry/bosh) 自动完成。
- [bosh (thomasmitchell)](https://github.com/thomasmitchell/bosh-complete) - [BOSH](https://github.com/cloudfoundry/bosh) 的 Tab 补全。
- [brew-completions](https://github.com/z-shell/brew-completions) - 将 [Homebrew Shell Completion](https://docs.brew.sh/Shell-Completion) 置于 ZSH 和 [ZI](https://github.com/z-shell/zi/) 的控制之下。
- [brew-services](https://github.com/vasyharan/zsh-brew-services) - [homebrew](https://brew.sh) 服务的完成插件。
- [buidler](https://github.com/gonzalobellino/buidler-zsh) - 为 NomicLabs Buidler 工具添加补全和有用的别名。
- [bw](https://github.com/CupricReki/zsh-bw-completion) - 添加 [Bitwarden](https://bitwarden.com/) 的补全。
- [cabal (d12frosted)](https://github.com/d12frosted/cabal.plugin.zsh) - 为 cabal 添加自动完成功能。
- [cabal (ehamberg)](https://github.com/ehamberg/zsh-cabal-completion) - 为 cabal 添加制表符补全。
- [carapace-bin](https://github.com/rsteube/carapace-bin) - 多 shell 多命令参数完成器。
- [cargo](https://github.com/MenkeTechnologies/zsh-cargo-completion) - 原始 oh-my-zsh 货物完成的所有功能，以及通过“货物添加”中的“货物搜索”对远程箱子的额外支持。
- [carthage](https://github.com/squarefrog/zsh-carthage) - 提供与 [Carthage](https://github.com/Carthage/Carthage) 一起使用的补全和别名。
- [cf-zsh-autocomplete](https://github.com/norman-abramovitz/cf-zsh-autocomplete-plugin) - 为所有 [Cloud Foundry CLI](https://docs.cloudfoundry.org/cf-cli/) 命令添加自动完成功能。
- [chezmoi](https://github.com/mass8326/zsh-chezmoi) - 添加 [chezmoi](https://www.chezmoi.io/) 的补全和别名。检测您是否有“git”别名并为它们生成“chezmoi”别名。
- [claude-code-zsh-completion](https://github.com/1160054/claude-code-zsh-completion) - 添加了 Anthropic 的 Claude Code CLI 的补全功能，支持 120 多种语言。包括 MCP 服务器、插件和会话 ID 的动态完成。
- [claudecode-completion](https://github.com/wbingli/zsh-claudecode-completion) - [Claude Code CLI](https://github.com/anthropics/claude-code) 的最小且始终最新的 zsh 补全。
- [click-completion](https://github.com/click-contrib/click-completion) - 添加对[Click](http://click.pocoo.org/)的自动补全支持，包括在选项卡补全过程中显示选项和命令帮助。
- [cod](https://github.com/dim-an/cod) - `bash`/`fish`/`zsh` 的补全恶魔，当它看到您使用 `--help` 运行某些内容时，它会动态创建补全函数。
- [codeception](https://github.com/shengyou/codeception-zsh-plugin) - 为 Codeception 测试框架添加命令完成。
- [codex](https://github.com/pressdarling/codex-zsh-plugin) - OpenAI 的 [codex](https://github.com/openai/codex) 工具的 Vibe 编码选项卡补全。在后台生成补全，这样就不会减慢 shell 的启动速度。包括可在 macOS 上获得流畅体验的增强功能。
- [comonicon](https://github.com/Roger-luo/ComoniconZSHCompletion.jl) - [comonicon](https://github.com/Roger-luo/Comonicon.jl) 的制表符补全。
- [complete-lastf](https://github.com/chougousui/complete-lastf) - 添加制表符补全以选择最近修改的文件或目录。
- [complete-mac](https://github.com/vitkabele/complete-mac) - 添加 macOS `ioreg`、`lsmp`、`scselect`、`system_profiler` 和 `tmutil` 命令的补全。
- [complete-ng](https://github.com/joknarf/complete-ng) - 通过交互式选择器菜单替换ZSH完成多项选择输出，浏览菜单内的目录，直接从菜单查看/编辑文件。
- [completion-sync](https://github.com/BronzeDeer/zsh-completion-sync) - 自动加载动态添加到“FPATH”或“XDG_DATA_DIRS”的补全。
- [completions (clarketm)](https://github.com/clarketm/zsh-completions) - 这包括 zsh-users[completions](https://github.com/zsh-users/zsh-completions)、zchee 的 [completions](https://github.com/zchee/zsh-completions)、nilsonholger 的 [osx-zsh-completions](https://github.com/nilsonholger/osx-zsh-completions) 和各种其他自定义完成。
- [completions (northismirror)](https://github.com/NorthIsMirror/zsh-completions) - ZSH 的额外完成情况。
- [completions (zchee)](https://github.com/zchee/zsh-completions) - 又一个制表符补全集合。
- [completions (zsh-users)](https://github.com/zsh-users/zsh-completions) - ZSH 额外完成的集合。
- [conda](https://github.com/conda-incubator/conda-zsh-completion) - [conda](http://conda.pydata.org/) 的 ZSH 选项卡补全。
- [copilot](https://github.com/scaryrawr/copilot.zsh) - 添加 [GitHub Copilot CLI](https://github.com/features/copilot/cli/) 的补全。
- [cpan](https://github.com/MenkeTechnologies/zsh-cpan-completion) - 添加 `cpan install word<tab>` 和 `cpanm install <tab>` 以完成远程 CPAN 软件包名称。
- [cross-compiler](https://github.com/Freed-Wu/zsh-completions-for-cross-compilers) - 在交叉编译方面，有很多工具，如x86_64-w64-mingw32-gcc、x86_64-linux-android32-clang、arm-none-eabi-gcc等。这个插件为它们提供了ZSH补全。
- [ctop](https://github.com/gantsign/zsh-plugins/tree/master/ctop) - [ctop](https://github.com/bcicen/ctop) 的 Tab 补全。
- [dagger](https://github.com/jygastaud/dagger-oh-my-zsh) - 完成匕首。
- [dbic](https://github.com/lejeunerenard/dbic-migration-env) - 自动为 DBIx::Class::Migration 的脚本和 Dancer 设置环境变量。
- [ddc](https://github.com/Shougo/ddc-zsh) - 为 [ddc](https://github.com/Shougo/ddc.vim) 添加制表符补全。
- [deno](https://github.com/marcelohmdias/zsh-deno) - [deno](https://deno.com/) 的制表符补全。
- [deoplete](https://github.com/zchee/deoplete-zsh) - [deoplete.nvim](https://github.com/Shougo/deoplete.nvim) 的 ZSH 补全
- [docker (chr-fritz)](https://github.com/chr-fritz/docker-completion.zshplugin) - 直接从 **Docker for Mac** 加载 `docker` ZSH 选项卡补全。
- [docker (felixr)](https://github.com/felixr/docker-zsh-completion) - 为“docker”添加制表符补全。
- [docker (greymd)](https://github.com/greymd/docker-zsh-completion) - 为“docker”和“docker-compose”添加制表符补全。
- [dotnet](https://github.com/MenkeTechnologies/zsh-dotnet-completion) - Dotnet 选项卡完成。
- [dropbox](https://github.com/zpm-zsh/dropbox) - Zsh 的 dropbox 插件，提供“dropbox-cli”和“dropbox-uploader”命令。
- [drush_zsh_completion](https://github.com/webflo/drush_zsh_completion) - ZSH 的 Drush 自动完成功能非常棒。
- [duell](https://github.com/jcxavier/oh-my-zsh-duell) - [duell](https://github.com/gameduell/duell) 的 ZSH 插件。
- [efibootmgr](https://github.com/wehlando/efibootmgr-zsh-completion) - `efibootmgr` 的 Tab 补全。
- [elm](https://github.com/kraklin/elm.plugin.zsh) - [elm](https://elm-lang.org/) 的制表符补全。
- [etcdctl](https://github.com/sheax0r/etcdctl-zsh) - 添加 etcdctl 选项卡补全。
- [expressvpn](https://github.com/tk7r/zsh-expressvpn) - 为 [expressVPN](https://www.expressvpn.com/support/vpn-setup/app-for-linux/) 客户端添加选项卡补全。
- [extract (le0me55i)](https://github.com/le0me55i/zsh-extract) - 定义一个名为 extract 的函数，用于提取您传递给它的存档文件，并支持多种存档文件类型。
- [extract (thetic)](https://github.com/thetic/extract) - oh-my-zsh 提取插件的分支。
- [fancy-completions](https://github.com/z-shell/zsh-fancy-completions) - 提供各种补全工具、库和集成。
- [flatpak](https://github.com/bilelmoussaoui/flatpak-zsh-completion) - [Flatpak](https://docs.flatpak.org/en/latest/using-flatpak.html) 的制表符补全。
- [fluxcd](https://github.com/l-umaca/omz-fluxcd-plugin) - 为 [FluxCD 命令行](https://fluxcd.io/flux/cmd/) 工具添加制表符补全，以及最常见的 Flux 命令的一些别名。
- [fly-zsh-autocomplete](https://github.com/Sbodiu-pivotal/fly-zsh-autocomplete-plugin) - 为所有 [Concourse CLI](https://concourse-ci.org/fly.html) 命令添加自动完成选项。
- [fnm](https://github.com/zap-zsh/fnm) - 为快速节点管理器 [fnm](https://github.com/Schniz/fnm) 添加选项卡补全。
- [fvm](https://github.com/olrtg/zsh-fvm) - 为 [Flutter Version Manager (FVM)](https://fvm.app/) 添加 Tab 键补全。
- [fzf-gcloud](https://github.com/mbhynes/fzf-gcloud) - 模糊完成导航和预览所有 Google Cloud SDK `gcloud` CLI 命令
- [fzf-rg](https://github.com/ppcamp/zsh-fzf-rg) - 使用 [fzf](https://github.com/junegunn/fzf)、[bat](https://github.com/sharkdp/bat) 和 [ripgrep](https://github.com/BurntSushi/ripgrep) 向终端添加一些功能。
- [fzf-tab-completion](https://github.com/lincheney/fzf-tab-completion) - 使用 GNU Readline 为 ZSH、“bash”和应用程序添加制表符补全。
- [fzf-zsh-completions](https://github.com/chitoku-k/fzf-zsh-completions) - [fzf](https://github.com/junegunn/fzf) 和 [ZSH](https://www.zsh.org/) 的模糊补全可以由默认为 `**` 的触发序列触发。
- [fzshell](https://github.com/mnowotnik/fzshell) - 从用户预定义的源中获取模糊补全。
- [gardenctl](https://github.com/holgerkoser/gardenctl) - [Gardener](https://github.com/gardener/gardenctl-v2) 命令行界面的 Tab 补全，以及常见 Gardenctl 命令的一些别名
- [gcloud (littleq0903)](https://github.com/littleq0903/gcloud-zsh-completion) - 添加 Google Cloud SDK 的补全。
- [gcloud (wintermi)](https://github.com/wintermi/zsh-gcloud) - 添加 Google Cloud 命令行界面 ([gcloud](https://cloud.google.com/cli) CLI) 补全。
- [gentoo](https://github.com/gentoo/gentoo-zsh-completions) - 为缺少上游完成脚本的各种 Gentoo 工具提供 ZSH 完成支持。
- [git-annex](https://github.com/Schnouki/git-annex-zsh-completion) - 允许大多数 git-annex 命令的制表符完成。
- [git-flow](https://github.com/bobthecow/git-flow-completion) - ZSH 对 [git-flow](http://github.com/nvie/gitflow) 的完成支持。
- [git-fzf](https://github.com/alexiszamanidis/zsh-git-fzf) - ZSH 插件包装了“git”操作，以实现简单性和生产力。它还包含补全并结合了对 [fzf](https://github.com/junegunn/fzf) 的支持。
- [git-profiles](https://github.com/baliestri/git-profiles.plugin.zsh) - 在单个“.gitconfig”文件中管理多个 git 用户。
- [git-recent-branches](https://github.com/Zacharyjlo/git-recent-branches) - 可以轻松查看和结帐最近签出的分支机构。
- [git-user-switch](https://github.com/dipodidae/zsh-plugin-git-user-switch) - 在多个 GitHub 用户帐户之间切换。它会自动更新您的 SSH 配置和 GitHub CLI (gh) 身份验证。
- [github-cli](https://github.com/sudosubin/zsh-github-cli) - GitHub cli 的 Tab 键补全。
- [gitlab-runner](https://github.com/pseyfert/zsh-gitlab-runner-completion) - gitlab-ci-multi-runner 的 ZSH 补全。
- [gradle-completion (gradle)](https://github.com/gradle/gradle-completion) - Bash 和 ZSH 对 gradle 的补全支持。
- [gradle-completion (ninrod)](https://github.com/ninrod/gradle-zsh-completion) - ZSH 对 gradle 的补全支持。
- [grid5000](https://github.com/pmorillon/grid5000-zsh-plugin) - Grid 5000 插件 - 添加主题、自动完成。
- [gstreamer](https://github.com/CraigCarey/gstreamer-tab) - [GStreamer](https://gstreamer.freedesktop.org/) 的 Tab 补全。
- [gulp (akoenig)](https://github.com/akoenig/gulp.plugin.zsh) - 在 Z-Shell (ZSH) 中自动完成 gulp.js 任务。
- [gulp (srijanshetty)](https://github.com/srijanshetty/gulp-autocompletion-zsh) - gulp 的自动补全。
- [hashlink](https://github.com/tong/zsh.plugin.hashlink) - 完成 [https://hashlink.haxe.org/](https://hashlink.haxe.org/)。
- [haskell](https://github.com/coot/zsh-haskell) - 添加了“cabal”、“ghc”和“ghc-pkgs”命令的补全。
- [haxelib](https://github.com/tong/zsh.plugin.haxelib) - haxelib 的完成。
- [helmfile](https://github.com/Downager/zsh-helmfile) - 添加“helm”的自动完成功能。
- [hledger](https://github.com/belegaps/omz-hledger-plugin) - 为 [hledger](https://hledger.org/) 提供别名和补全，这是一个功能强大的复式记账工具。
- [inshellisense](https://github.com/microsoft/inshellisense) - 为 shell 提供 IDE 风格的自动完成功能。它是一个用于自动完成的终端本机运行时，支持 600 多个命令行工具。 inshellisense 支持 Windows、Linux 和 MacOS 操作系统上的“bash”、“fish”、“zsh”和“pwsh”。
- [ipfs](https://github.com/hellounicorn/zsh-ipfs) - [星际文件系统](https://ipfs.tech) 的完成。
- [jenv](https://github.com/cmuench/zsh-jenv) - [jEnv](https://github.com/jenv/jenv) 的 Tab 补全。
- [joe](https://github.com/corvofeng/joe-completion) - 添加 [joe](https://github.com/karan/joe) gitignore 编辑器的补全。
- [jtool-completion](https://github.com/beaugalbraith/jtool-completion) - jtool 的 ZSH 补全。
- [justfile](https://github.com/JBarberU/zsh-justfile) - 为 [just](https://github.com/casey/just) 添加制表符补全。
- [jx](https://github.com/haysclark/zsh-jx) - 为 Jenkins-X cli 添加选项卡补全。
- [kafka](https://github.com/Dabz/kafka-zsh-completions) - Apache [kafka](https://kafka.apache.org) 的完成。
- [keybase](https://github.com/rbirnie/oh-my-zsh-keybase) - [keybase](https://book.keybase.io/docs/cli) 的完成。
- [kind](https://github.com/TomerFi/zsh-kind) - 加载 [kind](https://kind.sigs.k8s.io/) 的选项卡补全。
- [kitty](https://github.com/redxtech/zsh-kitty) - 完成 [kitty](https://sw.kovidgoyal.net/kitty/) 终端模拟器。
- [kompose](https://github.com/gantsign/zsh-plugins/tree/master/kompose) - 为 [Kompose](http://kompose.io/) 添加制表符补全。
- [kubeadm](https://github.com/gantsign/zsh-plugins/tree/master/kubeadm) - 为 [kubeadm](https://kubernetes.io/docs/reference/setup-tools/kubeadm/) 添加制表符补全。
- [kubectl (chrishrb)](https://github.com/chrishrb/zsh-kubectl) - 自动加载 [kubectl](https://github.com/kubernetes/kubectl) 的补全。
- [kubectl-fzf](https://github.com/bonnefoa/kubectl-fzf) - 快速而强大的 [fzf](https://github.com/junegunn/fzf) 支持的“kubectl”自动完成功能。
- [kubectl-plugin](https://github.com/MartinSimango/kubectl-plugin_completion) - 生成“kubectl”完成脚本以扩展“kubectl”自动完成功能以适应插件子命令。
- [kustomize](https://github.com/ralgozino/oh-my-kustomize) - 为 [kustomize](https://kustomize.io/) 添加制表符补全
- [lazycomplete](https://github.com/rsteube/lazycomplete) - shell 完成脚本的延迟加载。
- [lets-cli](https://github.com/lets-cli/lets-zsh-plugin) - 为 [lets](https://github.com/lets-cli/lets) cli 任务运行程序添加自动完成功能。
- [llm-cli-autocomplete-tool](https://github.com/duoyuncloud/zsh-llm-cli-autocomplete-tool) - 先进的 AI 支持的 ZSH 插件，具有 LoRA 微调、可导航 UI 和 [Ollama](https://ollama.com) 集成。
- [llm](https://github.com/eliyastein/llm-zsh-plugin) - 为 [LLM CLI 工具](https://llm.datasette.io/) 添加制表符补全。
- [ls-go](https://github.com/MohamedElashri/ls-go-zsh) - 为 [ls-go](https://github.com/acarl005/ls-go) 添加一些有用的别名。
- [mac](https://github.com/scriptingosx/mac-zsh-completions) - macOS 特定命令和第三方工具的补全文件。
- [macos](https://github.com/danydodson/zsh-completions) - 完成选定的 OSX 命令。该存储库的主要目的是创建高质量的自动完成，例如条件标志感知呈现和选项选择，以及最新且功能完整的自动完成。
- [mcfly](https://github.com/cantino/mcfly) - 使用智能搜索引擎替换默认的 ctrl-r shell 历史搜索，该搜索引擎会考虑您的工作目录和最近执行的命令的上下文。 McFly 的建议通过小型神经网络实时进行优先级排序。
- [mill](https://github.com/carlosedp/mill-zsh-completions) - Scala 的 [Mill](http://mill-build.com/) 构建工具的 Tab 补全。
- [miniconda](https://github.com/cmuench/zsh-miniconda) - [miniconda](https://docs.conda.io/en/latest/miniconda.html) 的制表符补全。
- [misc-completions](https://github.com/syohex/zsh-misc-completions) - 添加更多 UNIX 和 Perl 命令的补全。
- [mooseX-App](https://github.com/perlpunk/MooseX-App-Plugin-ZshCompletion) - Perl 模块 `MooseX::App` 的补全生成器。
- [more-completions](https://github.com/MenkeTechnologies/zsh-more-completions) - 13500 个 ZSH compsys 完成！大多数是由解析 --help 输出和手册页输出的 python 脚本生成的。因此，它们的质量参差不齐。架构前缀完成位于“architecture_src”目录中。
- [msfvenom](https://github.com/Green-m/msfvenom-zsh-completion) - Metasploit 的 Tab 补全。
- [mx-honey](https://github.com/mukel/mx-honey) - 提供 [mx](https://github.com/graalvm/mx) 的补全；用于开发 Graal 项目的命令行工具。它的目的是改进通常的工作流程“构建单元测试基准......”轻松发现并提供方便的别名。
- [myincr](https://github.com/gaojunbin/zsh-myincr/) - 通过自动建议和增量加快粘贴速度。
- [nestcli](https://github.com/behradkhodayar/nestcli-zsh) - [Nest.js CLI](https://github.com/nestjs/nest-cli) 的 Tab 补全。
- [newman](https://github.com/selop/newman-autocomplete) - 为 [Newman CLI](https://github.com/postmanlabs/newman) 提供自动完成功能。
- [ngrok](https://github.com/bostonaholic/ngrok.plugin.zsh) - 自动加载 [ngrok](https://ngrok.com) 及其补全到 shell 中。
- [nix](https://github.com/spwhitt/nix-zsh-completions) - 完成 [nix](https://nixos.org/nix/)、[NixOS](https://nixos.org/) 和 [NixOps](https://nixos.org/nixops/)。
- [node-ace](https://github.com/romch007/node-ace-zsh-completion) - “node ace”的完成。
- [nova](https://github.com/rbirnie/oh-my-zsh-nova) - 为 nova 提供自动完成功能。
- [npm-run](https://github.com/akoenig/npm-run.plugin.zsh) - 对“npm run”的自动补全支持。
- [npm-scripts-autocomplete](https://github.com/grigorii-zander/zsh-npm-scripts-autocomplete) - 显示当前目录的“package.json”中找到的脚本的自动完成建议。与“npm”和“yarn”一起使用。
- [nx](https://github.com/jscutlery/nx-completion) - [nx](https://nx.dev) 的完成情况。需要 [`jq`](https://stedolan.github.io/jq/)。
- [oh-my-update](https://github.com/utox39/oh-my-update) - 更新 [oh-my-zsh](https://ohmyz.sh/) 中的插件。
- [okta](https://github.com/sirhc/okta.plugin.zsh) - 为 [`aws-okta`](https://github.com/segmentio/aws-okta) 和 [okta-awscli](https://github.com/jmhale/okta-awscli) 命令提供命令行补全。
- [ollama](https://github.com/Katrovsky/zsh-ollama-completion) - 用于 Ollama AI 模型管理的 Tab 命令完成。
- [op](https://github.com/sirhc/op.plugin.zsh) - [1Password](https://1password.com/) 的 [op](https://1password.com/downloads/command-line/) 命令行工具的 Tab 补全。
- [openstack](https://github.com/florentinl/openstack-zsh-plugin) - 添加用于管理 [OpenStack](https://www.openstack.org/) 的函数和别名。
- [osx-zsh-completions](https://github.com/nilsonholger/osx-zsh-completions) - 某些 macOS 特定命令的 Tab 补全，例如“launchctl”。
- [packer](https://github.com/wakeful/zsh-packer) - 为 [packer](https://packer.io) 添加制表符补全。
- [pagerduty](https://github.com/jedelson-pagerduty/pagerduty-omz-plugin) - 添加 pagerduty [cli]( https://github.com/martindstone/pagerduty-cli ) 的补全
- [pandoc-completion](https://github.com/srijanshetty/zsh-pandoc-completion) - Pandoc补全插件。
- [parallels](https://github.com/benclark/parallels-zsh-plugin) - 添加 Parallels Desktop 的补全。
- [pass-zsh-completion](https://github.com/ninrod/pass-zsh-completion) - 方便的存储库可以轻松获取 ZSH 的 [pass](https://www.passwordstore.org/) 命令完成。
- [pip-completion](https://github.com/srijanshetty/zsh-pip-completion) - pip 自动补全插件。
- [pipenv (AlexGascon)](https://github.com/AlexGascon/pipenv-oh-my-zsh) - 为最常见的 pipelinev 命令启用别名。
- [pipenv (gangleri)](https://github.com/gangleri/pipenv) - 完成“pipenv”。
- [pmy](https://github.com/relastle/pmy) - 由 [fzf](https://github.com/junegunn/fzf) 提供支持的通用上下文感知 ZSH 补全引擎。
- [poetry](https://github.com/fourdim/zsh-poetry) - [poetry](https://python-poetry.org/) 的制表符补全。
- [prettier](https://github.com/sambergo/zsh-prettier-completion/) - [prettier](https://prettier.io/.) 的 Tab 补全
- [pytest-fzf](https://github.com/jszczepaniak/zsh-pytest-fzf) - 允许您使用 [fzf](https://github.com/junegunn/fzf) 选择 pytest 测试并将其插入终端。
- [python-args-completion](https://github.com/mejistus/python-args-completion) - 为使用 argparse 模块定义的 Python 脚本命令行参数提供自动完成功能。
- [python-module-completion](https://github.com/UshioA/zsh-python-module-completion) - python -m 命令的智能选项卡完成，具有分层模块导航和智能项目检测功能。
- [quickjump](https://github.com/fikovnik/zsh-quickjump) - 使用 [fasd](https://github.com/whjvenyl/fasd) 为最近的文件和目录添加对 [skim](https://github.com/lotabout/skim) 的制表符补全支持。
- [racket completion](https://github.com/racket/shell-completion) - 完成[Racket](http://racket-lang.org)。
- [rake-completion](https://github.com/unixorn/rake-completion.zshplugin) - 为 rakefile 目标添加快速制表符补全。
- [rancher](https://github.com/go/rancher-zsh-completion) - 添加 Rancher CLI 的补全。
- [rg](https://github.com/pressdarling/rg-zsh-plugin) - 提供 [ripgrep](https://github.com/BurntSushi/ripgrep) 的补全，这是一个快速的文件和文本搜索二进制文件。
- [rhoas](https://github.com/craicoverflow/rhoas-zsh-plugin) - 添加了 [rhoas](https://developers.redhat.com/products/red-hat-openshift-streams-for-apache-kafka/overview) 的补全。
- [rustup](https://github.com/pkulev/zsh-rustup-completion) - Rustup 的制表符补全。
- [s3cmd](https://github.com/FFKL/s3cmd-zsh-plugin) - 为 [s3cmd](https://s3tools.org/s3cmd) 添加制表符补全。
- [salesforce-cli](https://github.com/wadewegner/salesforce-cli-zsh-completion) - Salesforce CLI 的 ZSH 命令完成。需要 [jq](https://stedolan.github.io/jq/)。
- [saml2aws](https://github.com/sirhc/saml2aws.plugin.zsh) - 添加 [saml2aws](https://github.com/Versent/saml2aws) 的补全。
- [sdkman (matthieusb)](https://github.com/matthieusb/zsh-sdkman) - 为 [sdkman](https://sdkman.io/) 添加制表符补全。
- [sdkman (yongxingzhao)](https://github.com/yongxingzhao/zsh-sdkman) - 为 [sdkman](https://sdkman.io/) 添加制表符补全。
- [sfdx-autocomplete](https://github.com/jayree/sfdx-autocomplete-plugin) - Salesforce 自动完成插件 [sfdx](https://developer.salesforce.com/tools/salesforcecli)。
- [skate-actions](https://github.com/mjmccull0/skate-actions) - [skate](https://github.com/charmbracelet/skate) 个人键值存储的 Tab 补全。
- [speedtest](https://github.com/Yash-Singh1/zsh-plugin-speedtest) - 速度测试 [cli](https://www.speedtest.net/insights/blog/introducing-speedtest-cli/) 的 Tab 补全。
- [spring-boot-plugin](https://github.com/linux-china/oh-my-zsh-spring-boot-plugin) - 添加 [spring-boot](http://projects.spring.io/spring-boot/) 命令的自动补全。
- [ssh (sunlei)](https://github.com/sunlei/zsh-ssh) - 更好的主机完成“ssh”。
- [ssh (zpm-zsh)](https://github.com/zpm-zsh/ssh) - 添加“ssh”的主机完成。
- [ssh-agent (bobsoppe)](https://github.com/bobsoppe/zsh-ssh-agent) - 管理“ssh-agent”。
- [ssh-agent (hkupty)](https://github.com/hkupty/ssh-agent) - 自动启动“ssh-agent”来设置和加载“ssh”连接所需的任何凭据。
- [ssh-agent (twfksh)](https://github.com/twfksh/zsh-ssh-agent) - 一个用于在 ZSH 中管理 ssh-agent 的无膨胀实用程序插件。每当新的终端会话启动时，该插件就会自动启动并管理“ssh-agent”。运行 zsh-ssh-agent 后，您只需“ssh-add”一次密钥。该插件将处理其余的事情。
- [ssh-config-suggestions](https://github.com/yngc0der/zsh-ssh-config-suggestions) - 从 `~/.ssh/config` 加载 `ssh` 的完成。
- [supabase](https://github.com/Taimoor-Tariq/zsh-supabase) - [supabase cli] 的 Tab 补全(https://supabase.com/docs/guides/cli/getting-started)
- [symfony (Akollade)](https://github.com/Akollade/symfony.plugin.zsh) - 添加 [Symfony](https://symfony.com/) 的补全，包括 `bin/console` 和 `sf` 命令。
- [symfony-complete](https://github.com/voronkovich/symfony-complete.plugin.zsh) - 基于 [Symfony](https://symfony.com/doc/current/components/console.html) 的 CLI 应用程序的通用补全：`composer`、`php-cs-fix`、`bin/console`、`artisan`、`php-cs-fixer` 等。这支持子命令和 GNU 样式选项的自动补全 (`--help`)
- [tailscale (heroeslament)](https://github.com/HeroesLament/zsh-tailscale-plugin) - [tailscale](https://www.tailscale.com/) 的制表符补全和别名。
- [tailscale (hsrzq)](https://github.com/hsrzq/PluginForTailscale) - [tailscale](https://www.tailscale.com/) 的制表符补全。仅适用于 macOS。
- [tailscale-ssh](https://github.com/Seraphin-/zsh-tailscale-ssh) - 提供基于尾部状态的主机完成。它会自动删除 MagicDNS 后缀（如果存在）。
- [talosctl](https://github.com/RusMephist/talosctl-zsh-plugin) - [Talos Linux](https://www.talos.dev/v1.6/introduction/what-is-talos/) 的 Tab 补全。
- [task](https://github.com/targendaz2/taskfile) - [任务](https://taskfile.dev/) 的 Tab 补全。
- [taskbook](https://github.com/mastern2k3/taskbook-zsh-plugin) - 自动完成任务簿的任务编号。
- [terragrunt](https://github.com/jkavan/terragrunt-oh-my-zsh-plugin) - [Terragrunt](https://github.com/gruntwork-io/terragrunt) 的 Tab 补全。
- [test-kitchen](https://github.com/pelletiermaxime/test-kitchen-zsh-plugin) - 添加 [测试厨房](https://github.com/test-kitchen/test-kitchen)) 的补全。
- [tinygo](https://github.com/sago35/tinygo-autocmpl) - 为 [tinygo](https://tinygo.org/) 添加制表符补全。
- [tio](https://github.com/JBarberU/zsh-tio) - 为 tio 添加制表符补全
- [tmux pane words](https://gist.github.com/blueyed/6856354) - 用于完成 [tmux](https://tmux.github.io) 窗格中的单词的按键绑定。
- [tofu](https://github.com/marknefedov/oh-my-zsh-tofu) - 自动加载“tofu”的选项卡补全。
- [tshark](https://github.com/Yoswell/zsh_tshark_autocomplete) - 为 [TShark](https://tshark.dev/) 添加选项卡补全，为显示过滤器 (`-Y`) 和提取的字段 (`-e`) 提供深度、协议感知和分层自动补全。与仅建议平面协议名称或静态选项的传统 shell 补全不同，该工具了解 TShark 字段的内部结构。
- [tugboat](https://github.com/DimitriSteyaert/Zsh-tugboat) - 添加 [tugboat](https://github.com/petems/tugboat) 命令的自动完成功能。
- [umake](https://github.com/zlsun/umake) - Ubuntu umake 的制表符补全。
- [url-httplink](https://github.com/Valodim/zsh-_url-httplink) - 扩展了 ZSH 的 \_urls 补全，允许它补全 html 页面中的 url。
- [uv](https://github.com/lipov3cz3k/zsh-uv) - [uv](https://github.com/astral-sh/uv) 的制表符补全。
- [vert.x](https://github.com/davidafsilva/vert.x-omz-plugin) - 为 [vertx](https://vertx.io/) 命令提供自动完成功能。
- [vorpal](https://github.com/VorpalBlade/vorpal-zsh-completions) - 为一些上游似乎已经死亡的项目添加完成，包括 [duperemove](https://github.com/markfasheh/duperemove)、[optimus-manager](https://github.com/Askannz/optimus-manager) 和 [pacutils](https://github.com/andrewgregory/pacutils)。
- [web-open](https://github.com/AndrewHaluza/zsh-web-open) - 添加别名以打开网页。仅适用于 Ubuntu 20。
- [web-search](https://github.com/GowayLee/zsh_web_search) - 在默认浏览器中的指定搜索引擎中运行搜索。
- [wsl-notify](https://github.com/masonc15/wsl-notify-zsh) - 使用 [wsl-notify-send](https://github.com/stuartleeks/wsl-notify-send) 在命令花费时间超过 15 秒时发出通知。仅限 Windows。
- [xcode](https://github.com/keith/zsh-xcode-completions) - 一些 Xcode 命令行工具的补全 - `genstrings`、`nm`、`plutil`、`xcode-select`、`xcodebuild`、`xcrun`、`simctl`、`strings`、`swift-demangle`、`swift` 和 `lipo`。
- [yabai](https://github.com/Amar1729/yabai-zsh-completions) - 添加 macOS [yabai](https://github.com/koekeishiya/yabai/) 平铺窗口管理器的补全。
- [yarn-extra-completion](https://github.com/BuonOmo/yarn-extra-completion) - 受到 [lukechilds/zsh-better-npm-completion](https://github.com/lukechilds/zsh-better-npm-completion) 的启发。
- [yarn](https://github.com/g-plane/zsh-yarn-autocompletions) - 添加“yarn add”、“yarn remove”、“yarn Upgrade”、“yarn Why”和“yarn run”的自动完成功能。
- [yt-dlp](https://github.com/clavelm/yt-dlp-omz-plugin) - [yt-dlp](https://github.com/yt-dlp/yt-dlp) 的 Tab 补全。
- [zenquotes](https://github.com/aminelch/zenquotes) - 显示来自 [zenquotes.io](https://zenquotes.io) 的随机报价。
- [zoxide](https://github.com/jnooree/zoxide-zsh-completion) - [zoxy](https://github.com/ajeetdsouza/zicide) 的制表符补全。
- [zpacman](https://github.com/Yttehs-HDX/zsh-zpacman/) - 为 [zpacman](https://github.com/Yttehs-HDX/zpacman.git) 添加制表符补全。


## 主题

- [021011](https://github.com/guesswhozzz/021011.zsh-theme) - 极简主义。包括 VS Code 的单个“git”标记。
- [0i0](https://github.com/0i0/0i0.zsh-theme) - 针对深色终端窗口进行了优化，使用 nerdfont `git` 状态装饰。
- [14degree](https://github.com/saims0n/14degree-zsh-theme/) - 包括 `git`、`virtualenv` 和 `rvm` 状态装饰。
- [1999](https://github.com/DTan13/zsh1999) - 电力线式主题。包括“git”状态装饰、网络和电池状态。
- [7eth](https://github.com/chokri/zsh-theme) - 带有“git”状态装饰器的极简主题。
- [a](https://github.com/chammanganti/a-zsh-theme) - 带有当前目录和“git”状态装饰的简单主题。
- [abbr (theme)](https://github.com/PhilsLab/abbr-zsh-theme) - 显示当前目录路径的缩写版本，显示 Python virtualenv、Rust 版本、`git` 状态以及最后一个命令的退出代码。默认情况下在深色背景上效果很好，但可以轻松自定义颜色。
- [abhiyan](https://github.com/abhiyandhakal/abhiyan.zsh/) - 分段提示。包括“git”分支的装饰器、暂存文件计数、未暂存文件计数和未跟踪文件计数、用户名、当前工作目录和时间。需要与电力线兼容的字体。
- [absolute](https://github.com/NelsonBrandao/absolute) - 看起来非常干净的主题，带有“git”状态、“node”版本和最后一个命令的退出代码的装饰器。
- [abzt](https://github.com/stentibbing/abzt-zsh-theme) - 没有带有“git”状态和目录信息装饰器的废话主题。需要一个书呆子字体。
- [acenoster](https://github.com/himdek/Acenoster-ZSH-Theme) - 一个多用途主题，具有非常详细的“git”和“mercurial”支持。还包括 AWS 配置文件名称、虚拟环境名称（如果有）、后台任务数量、当前目录和上一个命令的退出代码（如果非零）的装饰器。
- [achab](https://github.com/niotna/antoinechab-theme) - 包括当前文件夹路径、当前用户和当前“git”分支的装饰器。装饰颜色可以轻松定制。
- [adamdodev](https://github.com/adamdodev/adamdodev-zsh-theme) - 包括“git”状态的装饰器、AWS 配置文件的名称、Azure 服务主体的名称、kubernetes 上下文、terraform 工作区、最后一个命令退出状态和当前工作目录。
- [adlee](https://github.com/adlee-was-taken/oh-my-zsh-osx/blob/master/adlee.zsh-theme) - macOS 主题，需要与 Powerline 兼容的字体。
- [adoz](daviosoo/adoz-zsh-theme) - 简约主题，重点关注紫色和蓝色色调。 Adoz 提供干净、现代的提示，显示重要信息，同时保持时尚的美感。通过设置环境变量进行高度可定制。包括 user@hostname、当前目录、时间戳和 `git` 状态的装饰器。
- [af-magic-dynamic](https://github.com/rslavin/af-magic-dynamic) - 具有动态路径缩短功能的 [af-magic](https://github.com/andyfleming/oh-my-zsh/blob/master/themes/af-magic.zsh-theme) 的修改版本。
- [afaq](https://github.com/afaq1337/afaq.zsh-theme) - 两行主题，带有主机名、本地 IP 地址、当前工作目录、当前时间、“git”状态和 Python virtualenv 的装饰器。
- [aflah-bhari](https://github.com/AflahB/aflah-bhari-zsh-theme) - oh-my-zsh 中的 [robbyrussell](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/robbyrussell.zsh-theme) 主题的修改版本。
- [aftermath](https://github.com/schanur/aftermath) - 在 shell 中运行每个命令后都会得到一个很好的摘要行。
- [agitnoster](https://github.com/dbestevez/agitnoster-theme) - 基于 [Oh My Zsh](https://github.com/ohmyzsh/ohmyzsh) 和 [bash-git-prompt](https://github.com/magicmonty/bash-git-prompt) 中包含的 [agnoster](https://gist.github.com/3712874) 主题。显示有关“git”状态的详细信息。
- [agkozak](https://github.com/agkozak/agkozak-zsh-prompt) - 使用三种异步方法来保持 ZSH 提示符响应，同时显示“git”状态和 SSH 连接指示符、退出代码和“vi”模式，以及缩写的“PROMPT_DIRTRIM”样式路径。非常可定制。即使在 Cygwin 和 MSYS2 上也是异步的。
- [agnopro](https://github.com/arhafizi/agnopro-zsh-theme) - 高性能、功能丰富的 ZSH 主题，具有智能上下文显示功能，受 Agnoster 启发并基于 Agnoster，但通过其他开发人员友好的功能进行了增强。包括当前目录、nodejs 版本、golang 版本、.Net 版本、`git` 状态、AWS 配置文件、user@host、后台作业和 Python 环境的装饰器。
- [agnoster (fcamblor)](https://github.com/fcamblor/oh-my-zsh-agnoster-fcamblor) - Solarized [Agnoster](https://gist.github.com/agnoster/3712874) 变体，带有 `git` 状态信息。需要 unicode 字体，并且最适合与 [solarized](https://github.com/altercation/solarized) 终端配合使用。
- [agnoster (fseguin)](https://github.com/fsegouin/oh-my-zsh-agnoster-mod-theme) - [agnoster](https://gist.github.com/agnoster/3712874) 具有正确提示的变体。
- [agnoster-gentoo](https://github.com/r7l/agnoster-gentoo-zsh-theme) - [Agnoster ZSH 主题](https://github.com/agnoster/agnoster-zsh-theme) 的 Gentoo 风格版本，包括 user@hostname 和 `git` 状态装饰。使用 unicode 字体效果更好。
- [agnoster-j](https://github.com/apjanke/agnosterj-zsh-theme) - 针对 [solarized](https://ethanschoonover.com/solarized/) 配色方案、`git` 或其他 VCS 工具以及 unicode 兼容字体进行了优化。包括上次命令运行状态、用户@主机名、`git`状态、工作目录、是否以 root 身份运行、后台作业是否正在运行以及其他信息的装饰器。
- [agnoster-mod](https://github.com/fsegouin/oh-my-zsh-agnoster-mod-theme) - [Agnoster](https://gist.github.com/agnoster/3712874) 具有右侧提示的变体。
- [agnoster-multiline](https://github.com/mxkrsv/agnoster-multiline) - 基于[Agnoster](https://github.com/agnoster/agnoster-zsh-theme)。包括当前目录和“git”状态的装饰器。需要带有 powerline 和 `git` 字形的字体。自动禁用 Linux tty 上的非 ASCII 字形。
- [agnoster-plus](https://github.com/jiahut/agnoster-plus.zsh-theme) - [Agnoster](https://gist.github.com/agnoster/3712874) 变体针对 [Solarized Dark](https://github.com/altercation/solarized/blob/master/iterm2-colors-solarized/Solarized%20Dark.itermcolors) 终端配色方案进行了优化。包括“git”状态。
- [agnoster-refresh](https://github.com/fusion94/Agnoster-refresh) - [Agnoster](https://gist.github.com/agnoster/3712874) 变体，包括电池和在线状态。
- [agnoster-repopath](https://github.com/ivanfurlan/agnoster-repopath-theme) - 基于 [Agnoster](https://github.com/agnoster/agnoster-zsh-theme) 和 [Passion](https://github.com/ChesterYue/ohmyzsh-theme-passion) 主题。包括 `git` 和 `mercurial` 状态、当前时间以及最后一个命令在提示符中进行装饰的时间。
- [agnoster-timestamp-newline](https://github.com/DylanDelobel/agnoster-timestamp-newline-zsh-theme) - [Agnoster](https://gist.github.com/agnoster/3712874) 添加了时间戳和换行符的变体。
- [agnoster](https://gist.github.com/agnoster/3712874) - 针对日光终端配色方案进行了优化，显示 `git` 装饰、user@host、工作目录、上一个命令的退出状态以及您是否以 root 权限运行。需要与电力线兼容的字体。
- [agnosterAfro](https://github.com/afrozalm/agnosterAfro) - 基于 [Powerline](https://github.com/Lokaltog/vim-powerline) 和 [Agnoster](https://gist.github.com/agnoster/3712874) 主题，并受到 [agnosterzak](https://github.com/zakaziko99/agnosterzak-ohmyzsh-theme) 的启发。
- [agnosterzak](https://github.com/zakaziko99/agnosterzak-ohmyzsh-theme) - 基于 [Agnoster](https://gist.github.com/agnoster/3712874)，显示电池寿命、日期和时间、`git` 状态、当前目录以及用户和主机信息。
- [ai-candy](https://github.com/SihaoLiu/ai-candy) - 响应式 [oh-my-zsh](https://github.com/ohmyzsh) 主题，适合跨容器、虚拟机和裸机工作的人工智能辅助开发人员。包括操作系统装饰器、内核信息、是否是“ssh”会话、“git”状态、GitHub 集成、AI 工具状态和智能缓存。
- [ai-hayasaka](https://github.com/aeghost/ai-hayasaka-zsh-theme) - 带有 `git` status、ruby env 和 python virtualenv 装饰器的极简主题。
- [air](https://github.com/Ivan-Kuzmichev/air) - 带有“git”状态装饰的极简主题。
- [akzsh](https://github.com/awkimball/akzsh) - 最适合深色终端主题，包括“git”装饰。
- [al-magic](https://github.com/Alustrat/al-magic/) - 克隆 oh-my-zsh [af-magic](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/af-magic.zsh-theme) 主题，并在提示右侧添加时间。
- [alarangeiras](https://github.com/alarangeiras/alarangeiras-zsh-theme/) - 带有“git”状态装饰的极简主题。
- [ale](https://github.com/alepimentel/ale-zsh) - 基于 fino 主题。包括 `git`、`virtualenv` 和 `node` 状态装饰。
- [alesrosina](https://github.com/alesrosina/oh-my-zsh-alesrosina-theme) - 包括“git”信息、当前目录和最后一个命令的返回状态的装饰器。
- [alien-minimal](https://github.com/eendroroy/alien-minimal) - 显示“git”状态的简约 ZSH 主题。
- [alien](https://github.com/eendroroy/alien) - Powerline 风格的 ZSH 主题，显示 `git` 装饰和最后一个命令的退出代码。比许多其他提示更快，因为它在后台进程中异步确定“git”装饰。
- [almel](https://github.com/Ryooooooga/almel) - 受到 [agnoster](https://github.com/agnoster/agnoster-zsh-theme) 的启发，用 Rust 编写。包括 `git` 状态、user@host、最后一个命令退出状态和工作目录装饰
- [aloy (garethclews)](https://github.com/garethclews/aloy) - [@elenapan's](https://github.com/elenapan/dotfiles) lena 主题的分支。包括 subnixr 的 [minimal](https://github.com/subnixr/minimal) 的 magic Enter，其中无需任何其他命令即可按 Enter 键打印出一些有用的 `ls`、`git` 和当前工作目录信息。
- [aloy (karetsu)](https://github.com/karetsu/aloy) - [@elenapan's](https://github.com/elenapan/dotfiles) lena ZSH 主题的分支。扩展以提供更多信息。它还包括 subnixr 的 [minimal](https://github.com/subnixr/minimal) 中的“magic Enter”，无需任何其他命令即可按 Enter 键打印出一些有用的“ls”、“git”和当前工作目录信息。
- [alp](https://github.com/zrut747/alp/) - 一个简单的主题，带有当前目录、根状态、用户名和主机的装饰。
- [alpha](https://github.com/Republic-Of-Lunar/alpha-zsh-theme) - 包括用户名@主机名和当前目录的装饰器。
- [alpharized](https://github.com/NicoSantangelo/Alpharized) - 优化以与 [solarized](http://ethanschoonover.com/solarized) 暗终端配合使用。它是 [avit 主题](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/avit.zsh-theme) 的修改版本。
- [amoyly](https://github.com/Br1an6/amoyly.zsh-theme) - 一个基于[Agnoster](https://gist.github.com/agnoster/3712874)的优雅且阅读舒适的主题。
- [amplify](https://github.com/clintfoster/ohmyzsh-theme-amplify) - 极简主义，包括 AWS Amplify 环境和 `git` 状态装饰。- [andy](https://github.com/andymcguinness/andys-theme) - 修改了 [bira](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/bira.zsh-theme) 主题，具有更好的 `git` 支持。
- [antoinechab](https://github.com/antoinechab/antoinechab-theme) - 包括 `git` 状态、用户名、时间和当前目录装饰。
- [antsy](https://github.com/jeffmhubbard/antsy-zsh-theme) - 显示 `git` 分支和状态装饰、virtualenv、退出状态、作业计数和 vi 模式指示器。
- [aofxta](https://github.com/aofxta/aofxta.zsh-theme/) - 包括最后一个命令的执行时间、`git` 信息、当前目录和当前时间的装饰器。
- [ap2](https://github.com/aungphyo-dev/ap2.zsh) - 使用时间、操作系统、当前目录、“git”状态和最后一个命令的退出状态的装饰器将它们最小化。
- [aperiodic](https://github.com/piccobit/aperiodic-zsh-theme) - 显示 `git` 装饰、用户、主机、是否为 root、活动的 Python 虚拟环境、当前的 Ruby 解释器、最后一个命令的视觉和数字状态、电源管理状态以及时间和日期。
- [aphrodite](https://github.com/win0err/aphrodite-terminal-theme) - 简约的主题，没有视觉噪音。仅显示必要的信息：当前用户、主机名、工作目录、“git”分支（如果存在）。黑色和白色终端看起来都很棒。
- [aplos](https://github.com/sunquan1991/aplos) - 最小的 ZSH 提示，包含工作目录、`git` 本地信息、`git` 远程信息、时间和退出代码。
- [apollo](https://github.com/mjrafferty/apollo-zsh-theme) - 高度可定制、兼容且高性能的 ZSH 主题，使用模块来启用功能。
- [aporia](https://github.com/fr3on/aporia) - 专为需要最先进终端环境的开发人员而设计。具有异步提示引擎：本机非阻塞后台工作程序 (zle -F) 可实现即时终端敏捷性、Go、Rust、Python、Node、Ruby、PHP、Java 和 C++ 的项目检测、Git 存储跟踪和虚拟环境和 Docker 的专用段，以及对幽灵文本自动建议和实时语法突出显示的内置支持。
- [appa](https://github.com/givensuman/appa-zsh-theme) - 一个基于 omz 的 [refined](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/refined.zsh-theme) 的整洁小主题。需要 [Nerd 字体](https://github.com/ryanoasis/nerd-fonts)。
- [apple (aramirol)](https://github.com/aramirol/apple-zsh-custom-themes) - 基于 [robbyrussell](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/robbyrussell.zsh-theme)，包含 `vcs` 状态装饰。通过在“.zshrc”中设置变量可自定义颜色。
- [apple (bjrowlett2)](https://github.com/bjrowlett2/apple-zsh-theme) - 带有“git”状态装饰的极简主题。
- [arael](https://github.com/aknackd/zsh-themes) - [gallifrey](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/gallifrey.zsh-theme) 的分叉。
- [archcraft](https://github.com/mrx04programmer/ZshTheme-ArchCraft) - 绿色主题，针对深色背景进行了优化。包括 `git` 状态装饰。
- [archie](https://github.com/dcavalcante/archie) - Arch Linux 启发了 ZSH 主题。基于 [norm](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/norm.zsh-theme) 主题。
- [archmocha](https://github.com/mikkurogue/archmocha/) - [catpucchin](https://github.com/JannoTjarks/catppuccin-zsh) 的一些摩卡主题带有 Arch Linux 风格。包括 user@hostname、当前目录和 `git` 状态的装饰器。
- [arctic-glow](https://github.com/Etto48/arcticglow-zsh-theme) - 基于 [agnoster](https://gist.github.com/3712874)。包括“git”状态、python 虚拟环境、当前目录、用户名和操作系统的装饰器。
- [arity](https://github.com/hybras/Arity-Zsh-Theme) - 一个简单的主题，旨在提高可读性并一目了然地提供概述。包括路径和“git”装饰。
- [arrow-minimal](https://github.com/maxim-usikov/arrow-minimal.zsh-theme) - 带有“git”装饰的最小 ZSH 主题。
- [arrow](https://github.com/milon/arrow-zsh-theme) - 最小主题，包括“git”状态装饰。
- [asciigit](https://github.com/cemsbr/asciigit) - 纯 ASCII 主题，适合不想使用带有额外字形的字体的“git”用户。
- [astral](https://github.com/xwmx/astral) - 带有禅宗模式的深色背景主题。与 zsh-users [zsh-syntax-highlighting](https://github.com/zsh-users/zsh-syntax-highlighting) 插件配合良好。包括最后一个命令的执行时间、运行时间、退出状态、计算机名称、当前路径、“ssh”状态和“git”状态的装饰器。
- [astro](https://github.com/iplaces/astro-zsh-theme) - 基于 `ys` 和 [robbyrussell](https://github.com/ohmyzsh/ohmyzsh/wiki/Themes#robbyrussell) 主题。
- [async](https://github.com/mje-nz/zsh-themes) - 显示当前目录、`git` 状态、最后一个命令的返回值（如果有错误代码）、后台作业数量、长时间运行命令的执行时间、当前 python virtualenv。
- [aterminal](https://github.com/guiferpa/aterminal) - 在提示中显示 Node.js、NPM、Docker、Go、Python、Elixir 和 Ruby 信息。
- [aub](https://github.com/FraSharp/aub) - 包括“git”和“hg”状态以及“host”处的“username”的装饰。
- [australis](https://github.com/Kimitzuni/australis-theme) - 带有“git”信息和当前目录装饰器的轻量级主题。需要来自 [oh-my-zsh](https://github.com/ohmyzsh) 的 `git` 插件。
- [avil](https://github.com/avil13/avil-zsh-theme) - 带有“git”装饰的简约主题。
- [avit-d2k](https://github.com/fdaciuk/avit-da2k) - 基于 oh-my-zsh [avit](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/avit.zsh-theme) 主题，有一些小改动。
- [avit-mod](https://github.com/zlsun/avit-mod) - oh-my-zsh 的 [avit](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/avit.zsh-theme) 主题的修改版本。
- [avoleo](https://github.com/flameleo11/avoleo-zsh-theme) - 每个命令都有日期和时间提示，以及历史命令编号。此外，它还使用特殊符号“⠾”和“⡶”来显示“git”信息（如果适用于当前路径）。它还支持基于 Gnome 终端默认调色板的自定义颜色。
- [aws](https://github.com/chiemerieezechukwu/aws-zsh-theme) - 基于 [robbyrussell](https://github.com/ohmyzsh/ohmyzsh/wiki/Themes#robbyrussell)，带有一个额外的装饰器，用于在设置时显示您的“$AWS_PROFILE”。
- [backbone](https://github.com/42LM/backbone-zsh-prompt) - 一个最低限度的单文件提示符，像走鹃 MEEP 一样快！米普。包括 `git` 状态和当前目录装饰。
- [baddcafe](https://github.com/dimgatz98/Baddcafe_zsh_theme) - 提供动态系统信息。包括“git”状态、CPU 使用情况、内存使用情况、电池电量、本地和全局 IP 地址、当前时间、当前目录和最后运行命令的退出状态的装饰器。
- [bahman](https://github.com/bahmanworld/bahman-zsh-theme) - 需要 [Nerd 字体](https://github.com/ryanoasis/nerd-fonts)。有 `git` 状态装饰器。
- [banana](https://github.com/sorcererxw/banana-zsh-theme) - 包括 `git` 状态装饰和当前目录。
- [bandit](https://github.com/Holger-Will/zsh_bandit) - 另一种电力线变体。
- [bar (anki-code)](https://github.com/anki-code/shell-prompt-theme-bar) - [p10k](https://github.com/romkatv/powerlevel10k) 的极简设置。
- [bar (xp-bar)](https://github.com/xp-bar/zsh-bar-theme) - 包括用户名、主机、密码、“git”状态装饰和 3 小时喝水提醒。
- [barion](https://github.com/SEbbaDK/barion) - 快速编译的提示符，带有紧凑的“git”状态概述。让人想起电力线。需要 [Crystal](https://crystal-lang.org/) 来构建。
- [base](https://github.com/Rodr1goTavares/based-zsh-theme) - 一个简约实用的 ZSH 主题，专为经常在远程服务器、VPS 或 VPN 上工作的开发人员和系统管理员而设计。包括您的公共 IP 地址、“git”状态和当前目录的装饰器。
- [bash](https://github.com/starseekist/bash-zsh-theme) - 看起来像默认的“bash”提示符。
- [bashi](https://github.com/eli-oat/bashi) - 针对 Ahmet Sülek 的 [Flat UI Terminal](https://github.com/ahmetsulek/flat-terminal) 主题和 Pasquale D'Silva 的 [Saturn Terminal](https://github.com/psql/saturn-colors) 主题进行了优化。
- [bashlover](https://github.com/Vu0811/bashlover) - 专为那些欣赏 ZSH shell 的强大功能但仍然喜欢类似于“bash”shell 的简单、经典界面的用户而设计。包括“git”信息、user@host 和当前工作目录的装饰器
- [bashplus](https://github.com/Elagoht/BashPlusZshTheme) - 默认“bash”提示符的彩色副本，带有“virtualenv”和“git”状态的装饰器。
- [bastard](https://github.com/jsundqvist/bastard.zsh-theme) - [ZIM](https://github.com/zimfw/zimfw) 的 [gitster](https://github.com/zimfw/gitster) 主题的修改版本。
- [bearable](https://github.com/JanmanX/bearable-zsh) - 适用于深色终端背景。
- [bearings](https://github.com/liamg/bearings) - 快速、干净、超级可定制的 shell 提示符。包括当前目录的装饰器、“git”状态、最后一个命令的退出代码、最后一个命令的持续时间、后台作业和用户名。
- [bedbugs](https://github.com/justino/zsh-theme-bedbugs) - 受到 [Agnoster](https://gist.github.com/agnoster/3712874) 的启发，这个多行提示符包括 `git` 状态信息、后台作业计数、工作目录、用户和主机名、Python virtualenv（如果存在）、最后一个命令的彩色返回值和 root/用户标志的装饰器。
- [beer](https://github.com/tcnksm/oh-my-zsh-beer-theme) - 灵感来自[cloud](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/cloud.zsh-theme)，但带有啤酒图标。
- [bender](https://github.com/specious/bender) - 带有 git 集成的奇特的两行提示符。
- [berghain](https://github.com/meshkinyar/berghain.zsh-theme) - 极简主义主题。包括最后一个命令运行的退出代码和“git”状态的装饰器。
- [bernkastel](https://github.com/JamesLaverack/bernkastel) - 基于 [ys](https://github.com/robbyrussell/oh-my-zsh/blob/master/themes/ys.zsh-theme)。包括 kubernetes 上下文、当前目录、最后一个命令退出状态和“git”状态的装饰。
- [better-robbyrussell](https://github.com/ymulenll/oh-my-zsh-better-robbyrussell) - oh-my-zsh 中的 [robbyrussell](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/robbyrussell.zsh-theme) 主题的修改版本保持了原始主题的简单性，同时添加了 AWS 配置文件感知。包括 AWS 配置文件的装饰器、带有可选截断的“git”分支显示、目录路径和上次命令运行的退出状态。
- [bgnoster](https://github.com/vvvvv/bgnoster.zsh-theme) - [Agnoster](https://gist.github.com/agnoster/3712874) 带有 unicode 符号的变体。
- [bigshrimp](https://github.com/taksyon/BigShrimp-zsh-theme) - 一个清晰简洁的主题，包括用户名@主机、当前目录和“git”状态的装饰器。
- [bigyls](https://github.com/Bigyls/Bigyls-zsh-theme) - 基于 [lpha3cho](https://github.com/sdcampbell/lpha3cho-Oh-My-Zsh-theme-for-pentesters)。包括日期、时间、IP 地址、`git` 状态、插件和当前目录的装饰器。
- [bira](https://github.com/zimfw/bira) - Oh-My-ZSH [bira](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/bira.zsh-theme) 主题的分支。包括工作目录、username@host、`git` 状态信息、Python [venv](https://docs.python.org/3/library/venv.html) 的装饰器以及最后一个命令出错时的状态代码。
- [birame](https://github.com/maniat1k/birame) - 基于[bira](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/bira.zsh-theme)。
- [biraskull](https://github.com/Shahryar-Pirooz/biraSkull.zsh-theme) - 基于 [bira](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/bira.zsh-theme)，包括 root 状态和 `git` 状态装饰。
- [biratime](https://github.com/vemonet/biratime) - 基于 [bira](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/bira.zsh-theme) 主题，但在提示中显示日期而不是用户名。
- [birav2](https://github.com/shahid64/birav2-theme) - 基于[bira](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/bira.zsh-theme)。包括 `git`、`rvm` 和 `virtualenv` 状态装饰。
- [black-Void](https://github.com/black7375/BlaCk-Void-Zsh) - 包括帐户信息、root 用户、使用 ssh、目录位置、写入权限和 vcs 信息修饰。
- [blackrain](https://github.com/ginfuru/zsh-blackrain) - 另一个“git”感知主题。
- [blaze](https://github.com/danieltodor/blaze) - 视觉上类似于电力线。需要“make”和“g++”。最适合您的终端设置为使用 [Nerd Font](https://github.com/ryanoasis/nerd-fonts)。包括当前目录的装饰器、最后一个命令的执行时间、最后一个命令的退出状态、`git`状态信息、日期、时间、用户名和主机。可以通过自定义段进行扩展。
- [blazux](https://github.com/blazux/omz-theme) - 包括 `git` 状态装饰和最后一个命令退出状态的笑脸/悲伤表情指示器。
- [blinks (max13ft)](https://github.com/max13fr/blinks.zsh-theme) - 为 oh-my-zsh 的 [blink](https://github.com/max13fr/blinks.zsh-theme) 主题添加 Mercurial 支持。
- [blinks-xfan](https://github.com/ixfan/blinks-xfan) - 基于现有主题[blinks](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/blinks.zsh-theme)。
- [bliss](https://github.com/joshjon/bliss-zsh) - 精致的主题可为您的工作空间注入色彩，但又不会压垮您的工作空间。设计用于与 [bliss iTerm](https://github.com/joshjon/bliss-iterm) 配色方案和 [bliss dircolors](https://github.com/joshjon/bliss-dircolors) 一起使用。包括 `git` 状态装饰。
- [blox](https://github.com/yardnsm/blox-zsh-theme) - 一个最小且快速的 ZSH 主题，向您展示您所需要的。它由块组成：每个块都显示在一对\[方括号\]内，您可以通过简单地创建函数来添加块。
- [bluehigh](https://github.com/hiroppy/bluehigh.zsh-theme) - 最小主题，显示“git”信息。
- [bluelines](https://github.com/apbarrero/bluelines) - 清晰和蓝色的主题。
- [bluo](https://github.com/varunpbardwaj/bluo) - 彩色提示段让人想起 [bullet-train](https://github.com/caiogondim/bullet-train.zsh) 或 [powerlevel10k](https://github.com/romkatv/powerlevel10k)。包括 `git` 状态装饰。
- [boban](https://github.com/TheEdgeOfRage/boban-zsh) - 基于 [Agnoster](https://github.com/agnoster/agnoster-zsh-theme) 的电力线样式文件。包括 user@hostname、`git` 状态、当前工作目录、python venv、AWS 配置文件、`$KUBECONFIG`、terraform 工作区和最后一个命令运行的退出状态的装饰器。需要 [Nerd Font](https://github.com/ryanoasis/nerd-fonts) 才能正确渲染符号。
- [bogo](https://github.com/cubasepp/zsh-bogo-theme) - 受到 [zeta](https://github.com/skylerlee/zeta-zsh-theme) 的启发。包括 `git` 和 ruby​​ 版本装饰。
- [boom](https://github.com/the0neWhoKnocks/zsh-theme-boom) - 多行主题，最适合深色背景。
- [born-in-the-purple](https://github.com/LeonardMH/born-in-the-purple) - 带有紫色主题的简单主题。灵感来自[Pure](https://github.com/sindresorhus/pure)。
- [bouni](https://github.com/Bouni/bouni-zsh-theme) - 包括 user@host、当前目录、活动 python virtualenv 和 `git` 状态的装饰器。
- [boxy](https://github.com/evil-tim/boxy-zsh-theme) - 与晒过的终端颜色配合良好。包括“用户名@主机名”、当前目录、“git”状态、最后一个命令的返回码以及最后一个命令运行时间的装饰器。
- [braundo](https://github.com/Braundo/braundo-zsh-theme) - 简单的主题，包含用户名、当前目录、“git”状态和时间戳。
- [bref](https://github.com/mpostaire/bref-zsh-prompt) - 一个简单的提示。它包括异步显示“git”状态的装饰器、“ssh”会话远程时的通知、电池电量和后台作业数量。
- [bright-catpuccin](https://github.com/Tailung42/bright_catppuccin_zsh_theme) - 充满活力、现代的 ZSH 提示音基于美丽的 Catppuccin Mocha 调色板，具有明亮的色彩氛围。包括`git`状态、python`venv`、conda env、智能路径截断、长时间运行命令的命令执行时间、可选的用户名@主机名、智能路径截断、后台作业和命令退出状态的装饰器。
- [brisa](https://github.com/ambrisolla/oh-my-zsh-brisa-theme) - 基于 [fino-time](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/fino-time.zsh-theme) 的多行主题。包括用户名、主机、当前目录和“git”状态的装饰。
- [bronze](https://github.com/reujab/bronze) - 一个跨 shell 可定制的类似电力线的提示符，带有用 go 编写的图标。需要 [nerd-fonts](https://github.com/ryanoasis/nerd-fonts)。
- [brs](https://github.com/evenhold/brs-zsh-theme) - 使用“audtool”在提示中显示当前歌曲。
- [bruh](https://github.com/haze/bruh) - 包括 `git` 状态装饰。
- [bryce-robbyrussell](https://github.com/Bryan-Cee/bryce-robbyrussell) - 受到 [powerline](https://github.com/Lokaltog/vim-powerline) 和 [robbyrussell](https://github.com/ohmyzsh/ohmyzsh/wiki/Themes#robbyrussell) 主题的启发。
- [bttf-color](https://github.com/yasuhiroki/bttf-color-zsh) - BTTF 颜色主题。包括 `git` 状态装饰。
- [bubblegum](https://github.com/ice-bear-forever/bubblegum-zsh) - 极简主义的亮粉色主题，带有三角形字形和您的工作目录，仅此而已 - 为您留下尽可能干净的外壳。
- [bubblified (hohmannr)](https://github.com/hohmannr/bubblified) - 受到 [agnoster](https://github.com/agnoster/agnoster-zsh-theme) 的启发。与 [nerdfonts](https://github.com/ryanoasis/nerd-fonts) 配合使用效果最佳。
- [bubblified (varaki)](https://github.com/varaki/bubblified-varaki.zsh-theme) - 基于[bubblified (hohmannr)](https://github.com/hohmannr/bubblified)。生根时改变颜色。包括显示 user@host 和当前目录的装饰器。
- [buddha](https://github.com/BuddhaDom/zsh-buddha) - 包括“git”状态、当前目录、上次命令运行的退出状态和用户名@主机名的装饰器。
- [buddy](https://github.com/hieudnm/zsh-buddy-theme) - 带有扩展系统的多语言支持、1730-1830 年的加班提醒、“git”状态装饰器、时间和虚拟环境信息、操作系统检测、不同时间和命令的 70 多个上下文消息。
- [bullet-train](https://github.com/caiogondim/bullet-train.zsh) - 受到 Powerline Vim 插件的启发。它旨在简单化，仅在相关时显示信息。
- [bunnyruni.min](https://github.com/mikeumus/bunnyruni.min) - [@jopcode's](https://github.com/jopcode) [bunnyruni](https://github.com/jopcode/oh-my-zsh-bunnyruni-theme) ZSH 主题，修改为仅显示时间和目录。
- [bunnyruni](https://github.com/jopcode/oh-my-zsh-bunnyruni-theme) - 简单、干净、美丽的主题。
- [bureau-env](https://github.com/angus-lherrou/bureau-env) - 修改 Oh-My-Zsh [Bureau](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/bureau.zsh-theme) 主题，在 `git` 块的左侧添加一个 Python 虚拟环境标签。
- [bureau-parrot](https://github.com/BenjaminGuzman/bureau-parrot) - 基于[bureau](https://github.com/robbyrussell/oh-my-zsh/blob/master/themes/bureau.zsh-theme)。包括 `git` 装饰。
- [bureau](https://github.com/isqua/bureau) - 清晰且内容丰富的两行提示。包括针对大型存储库优化的“git”状态。
- [burn](https://github.com/Xatra1/burn) - 包括 user@hostname 和当前目录的装饰器。
- [buster](https://github.com/grantbuster/buster_zsh_theme) - 与 WSL2 配合良好。大致基于 oh-my-zsh 中的 Fox 和 Jonathan 主题。
- [cabovianco](https://github.com/cabovianco/cabovianco-zsh-theme) - 包括“git”状态和当前目录的装饰器。
- [cactus](https://github.com/welksonramos/cactus) - 带有“git”状态装饰的极简主题。
- [cafeconbits](https://github.com/ricard-ferrero/cafeconbits-zsh-theme) - 带有咖啡杯图标的简单主题。包括 `git` 状态、当前目录和最后一个命令的退出状态的装饰器。
- [calma](https://github.com/luislve17/calma) - 极简主题，适用于深色背景。包括用于截断当前目录、“git”信息、时间和最后一个命令的退出状态的装饰器。
- [candy-fantasy](https://github.com/fffelix-huang/candy-fantasy) - [糖果王国](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/candy-kingdom.zsh-theme)主题的修改版本。
- [candy-light](https://git.sr.ht/~nicolairuckel/oh-my-zsh-candy-light) - 糖果主题的精简版。
- [capsule](https://github.com/42LM/capsule) - 一个简单的单文件终端提示符，完全可定制。显示分为胶囊（`TIMER`>`DIR`>`GIT`>`GIT ACTION`）。
- [carriage-return](https://github.com/treyssatvincent/carriage-return.zsh-theme) - omz 的 [robbyrussell](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/robbyrussell.zsh-theme) 添加了回车符。
- [catppuccin-powerlevel10k-themes](https://github.com/tolkonepiu/catppuccin-powerlevel10k-themes) - [Powerlevel10k](https://github.com/romkatv/powerlevel10k) 主题的灵感来自于 [**Catppuccin**](https://catppuccin.com/) 调色板。这些主题有多种样式可供选择，并支持所有四种 Catppuccin 调色板：**🌻 Latte**、**🪴 Frappé**、**🌺 Macchiato** 和 **🌿 Mocha**。
- [catpuccin-kali](https://github.com/Robinx0/catpuccin-kali-theme.zsh-theme) - 灵感来自 oh-my-posh catpuccin 主题。包括用户名@主机名、当前目录和“git”状态的装饰器。
- [catpuccin](https://github.com/JannoTjarks/catppuccin-zsh) - 极简主义主题。包括当前目录的装饰器、最后一个命令的退出状态和“git”状态。
- [cayun](https://github.com/comeacrossyun/ys-cayun.zsh-theme) - 在提示符中显示活动的 Python 版本和“git”装饰。
- [celestialorb](https://github.com/celestialorb/zsh-theme) - 受电力线启发的主题，作者：@celestialorb。包括 `git` 状态修饰、Kubernetes 集群信息（如果有）、当前 AWS 配置文件和区域以及活动 virtualenv。
- [cezhanne](https://github.com/gambardellawill/cezshanne) - 带有“git”状态装饰器的极简 ZSH 主题。需要 [Nerd 字体](https://www.nerdfonts.com)。
- [cf-ps1](https://github.com/mdan16/cf-ps1) - 在提示中显示 [Cloud Foundry](https://www.cloudfoundry.org/) 的当前基础、组织和空间。
- [ch4rli3](https://github.com/ch4rli3kop/ch4rli3.zsh-theme) - 精干而简单的主题。
- [chaffee](https://github.com/jasonchaffee/chaffee.zsh-theme) - 基于索林。显示 Java、Scala、Go、Node、Python 和 Ruby 的当前活动版本。
- [chaos](https://github.com/kusamaxi/chaos-zsh) - 受到 dogenpunk 和 smt 主题的启发，针对“git”用户和 Python 开发人员进行了优化。包括 `git` 状态、python 虚拟环境、后台作业、最后一个命令的错误状态、user@hostname 和当前目录的装饰器。需要带有表情符号的字体。
- [chaotic-beef](https://github.com/ARtoriouSs/chaotic-beef-zsh-theme) - Oh-My-Zsh 的一个小巧而美丽的主题，没有任何多余的东西。包括 `git` 状态装饰。
- [charged](https://github.com/robwierzbowski/charged-zsh-theme) - 针对 [solarized](https://github.com/altercation/solarized) 深色终端主题优化的 ZSH 提示符。
- [cheeky](https://github.com/kampanosg/zsh-cheeky-prompt) - 包括小鸡表情符号、当前目录的装饰器、“git”信息以及当前的 GCP 集群和项目。
- [chello](https://github.com/Abdalla981/chello) - 在深色背景上效果很好。取决于 [autojump](https://github.com/wting/autojump)、[zsh-autosuggestions](https://github.com/zsh-users/zsh-autosuggestions) 和 [zsh-syntax-highlighting](https://github.com/zsh-users/zsh-syntax-highlighting)。
- [chi](https://github.com/akinjide/chi) - 针对 macOS 上的 iTerm 2 用户优化的 ZSH 主题。
- [chill](https://github.com/JKerboeuf/chill.zsh-theme) - 具有当前工作目录、最后一个命令退出状态和“git”状态的装饰。
- [chinipage](https://github.com/andresemartinez/chinipage-zsh-theme) - 极简主题，包括“git”装饰。需要电力线兼容的字体和 [git-prompt](https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins/git-prompt) 插件。
- [chrisandrew.cl](https://github.com/chrisandrewcl/chrisandrew.cl.zsh-theme) - 包括 `git` 装饰。需要与电力线兼容的终端字体。
- [cinnabar](https://github.com/nvillapiano/zsh-theme---cinnabar) - 显示时间戳、大换行符、git 分支和状态。
- [clarity](https://github.com/nbitmage/clarity.zsh) - 专为简单性和可扩展性而设计。
- [classic](https://github.com/freakinu/classic-zsh-theme) - 一个经典的 UNIX 主题，带有用户名、主机、当前目录和“git”状态的装饰器。
- [classyTouch](https://github.com/yarisgutierrez/classyTouch_oh-my-zsh) - 最小、干净的主题，带有“git”支持。
- [classyTouchName](https://github.com/dylanroman03/classyTouchName) - 灵感来自 [classyTouch](https://github.com/yarisgutierrez/classyTouch_oh-my-zsh)。在深色背景下效果更好。包括 `git` 状态装饰。
- [clean (akz92)](https://github.com/akz92/clean) - 极简 ZSH 主题。
- [clean (brandonRoehl)](https://github.com/BrandonRoehl/zsh-clean) - [pure](https://github.com/sindresorhus/pure) 的极简变体。纯粹不干净，干净不纯粹。
- [clean (patr1ot)](https://github.com/Patr1ot/clean.zsh-theme) - 上游 [clean](https://github.com/ohmyzsh/ohmyzsh/wiki/Themes#clean) 的分叉，添加了主机信息。
- [cleansh](https://github.com/diegoos/cleansh) - 极简主义，包括 `git`、Ruby、node 和 Python 版本状态装饰。适用于标准字体。
- [clearance](https://github.com/H00N24/clearance-theme-oh-my-zsh) - 带有 `git`、nix-shell 和 virtualenv 状态装饰的简约主题。
- [clipper](https://github.com/Robert-96/clipper) - 极简 ZSH 主题，支持“git”。它包括 pwd、最后一个命令退出状态代码和“git”状态和分支的装饰。
- [cloudy](https://github.com/Huvik/Cloudy) - 最小多云 ZSH 主题。
- [clover](https://github.com/tzing/clover.zsh-theme) - 受到 [zeta](https://github.com/skylerlee/zeta-zsh-theme) 和 [pure](https://github.com/sindresorhus/pure) 的启发。
- [cmder-wsl](https://github.com/szyminson/cmder-wsl-zsh) - `cmder` 的配置文件，配置为使用 ZSH 和修改后的 [Agnoster](https://gist.github.com/agnoster/3712874) 主题在地震模式下工作。
- [cmder](https://github.com/potasiyam/cmder-zsh-theme) - 与 Cmder（流行的 Windows 终端模拟器）主题相匹配的 ZSH 主题。包括 `node` 和 `git` 状态装饰。
- [cn](https://github.com/shinqcn/cn-zsh/) - 包括 `username`、`directory` 和 `git` 状态装饰。
- [cobalt2](https://github.com/wesbos/Cobalt2-iterm) - Wes Bos 为 ZSH 和 iTerm 2 设计的 Cobalt 2 主题。
- [cobalt2git](https://github.com/alexeimun/cobalt2git) - 带有“git”扩展的 Cobalt 2 主题。
- [codemachine](https://github.com/CodeMonkeyMike/ZshTheme-CodeMachine) - 显示“git”信息的装饰器、是否通过“ssh”登录以及最后一个命令的返回码。
- [coffeenostor](https://github.com/CoffeeVector/coffeenostor-zsh-theme) - 基于 [agnoster](https://gist.github.com/3712874)，具有 vi 模式的右侧提示，以电力线外观显示“--INSERT--”和“--NORMAL--”。
- [collon](https://github.com/lambdalisue/collon.zsh) - 带有 `git` 状态装饰、cwd、时间、主机、最后一个命令的退出状态的轻量级主题。不需要特殊字体。
- [colorbira](https://github.com/CristianCantoro/colorbira-zsh-theme) - 允许每个主机提示着色，显示“rvm”、“virtualenv”和“git”信息。
- [common](https://github.com/jackharrisonsherlock/common) - 一个简单、干净和最小的提示，显示当前工作目录、主机名、AWS 保管库角色、后台作业、当前 SHA、最后一个命令的退出代码以及“git”分支和状态。
- [comxtohr](https://github.com/comxtohr/comxtohr-zsh-iterm-theme) - 色彩鲜艳的主题针对深色背景进行了优化。
- [coolmelon](https://github.com/omkarpai/coolmelon-zsh-theme/) - 包括 user@host、时间、当前目录、节点版本和 `git` 信息的装饰器。
- [cordial](https://github.com/stevelacy/cordial-zsh-theme) - 干净有效的 ZSH 主题，支持 git 和 npm。
- [cr](https://github.com/cruzrovira/cr-zsh-theme) - 包括目录、时间、主机名、最后一个命令退出状态和“git”状态修饰。
- [cramin](https://github.com/FelipeCRamos/craminzsh) - 基于 [hyperzsh](https://github.com/tylerreckart/hyperzsh) 的最小界面，支持 GitHub 插件。
- [cravend](https://github.com/cravend/theme) - 包括“hostname”装饰器（仅在活动的“ssh”会话中）和“git”状态装饰器。
- [crème fraîche](https://github.com/koenwoortman/creme-fraiche-zsh-theme) - 最适合轻型终端背景，包括“git”和“vi”模式状态装饰。
- [croque](https://github.com/Ryooooooga/croque) - 受电力线启发的主题，带有操作系统装饰器、user@host、`git` 信息、`git` 用户名、当前目录和最后一个命令的退出状态。
- [cryo-long](https://github.com/cryocaustik/cryo-long-zsh-theme) - [cryo](https://github.com/cryocaustik/cryo-zsh-theme/) 的变体，添加了主机名和当前目录的装饰器。
- [cryo](https://github.com/cryocaustik/cryo-zsh-theme) - 原始 oh-my-zsh 主题的独立克隆，添加了日期和时间。
- [cryptic](https://github.com/thederpykrafter/cryptic.zsh-theme) - 基于 [aphrodite-terminal-theme](https://github.com/win0err/aphrodite-terminal-theme)。包括当前目录、“git”状态、时间、用户名、主机名和虚拟环境的装饰器。
- [cute](https://github.com/dogrocker/oh-my-zsh-powerline-cute-theme) - macOS oh-my-zsh shell 主题，带有基于 Powerline Vim 插件的可爱表情符号。
- [cxzh](https://github.com/MakeWorkSimple/cxzh.zsh-theme) - 在深色背景上运行良好，具有“git”状态装饰。
- [cybensis](https://github.com/cybensis/cybensis-zsh-theme) - 基于 [af-magic](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/af-magic.zsh-theme)。包括`git`信息、`hg`信息和python virtualenv的装饰器。
- [cypher-ruby](https://github.com/ston1x/cypher-ruby) - 与 [cypher](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/cypher.zsh-theme) 类似，但包含活动的 Ruby 版本。
- [czsh](https://github.com/Cellophan/czsh) - [ZSH](https://en.wikipedia.org/wiki/Z_shell) 与 [oh-my-zsh](https://github.com/ohmyzsh/ohmyzsh) 和 [agnoster](https://github.com/agnoster/agnoster-zsh-theme) 主题位于容器中。
- [daily-emoji](https://github.com/huytran-wq/zsh-daily-emoji-theme/) - 根据星期几在每个命令的开头显示随机表情符号。
- [daily](https://github.com/ghlin/zsh-theme-daily) - 包括 `git` 和 `ssh` 状态装饰。
- [daivasmara](https://github.com/Daivasmara/daivasmara.zsh-theme) - 使用当前目录的装饰器（必要时截断）和“git”信息（包括自上次提交以来的时间）来冷却主题。
- [dalailahner](https://github.com/dalailahner/dalailahner.zsh-theme) - 极简主题，带有“git”状态、VCS 状态装饰器（基于 [Bart Trojanowski 的 zsh 提示符](http://www.jukie.net/bart/blog/pimping-out-zsh-prompt)）、用户名和当前目录。基于 Steve Losh 的 [Prose](https://github.com/sjl/oh-my-zsh/blob/master/themes/prose.zsh-theme) 主题。
- [damino](https://github.com/njdom24/Damino-Zsh-Theme) - 带有“git”装饰的最小电力线风格主题。
- [dangerroom](https://github.com/abbreviatedman/dangerroom) - 信息丰富、简约，最重要的是，以 X 战警为主题。包括“git”状态、工作目录、父目录和“vim”模式的装饰器。
- [dango](https://github.com/ann-kilzer/annkilzer.zsh-theme) - 包括当前目录和“git”状态的装饰。
- [danielparks](https://github.com/danielparks/danielparks-zsh-theme) - 在深色背景上效果很好。包括“git”状态的装饰器、“ssh”会话中的 user@host、最后一个命令的成功/失败、工作目录、python virtualenv、最后一个命令的执行时间以及是否以“root”身份运行。
- [daniloheraclio](https://github.com/daniloheraclio/daniloheraclio-zsh-theme) - 受到 [robbyrussell](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/robbyrussell.zsh-theme) 主题的启发。有 `git` 和最后一个命令退出状态装饰。需要 nerdfont 才能正确渲染。
- [dark-modern](https://github.com/d-exclaimation/vscode-dark-modern.zsh-theme) - 包括“git”状态和当前目录的装饰器。
- [darkblood-modular](https://github.com/InAnimaTe/darkblood-modular) - 此版本的流行 [darkblood](https://github.com/BinaryMuse/oh-my-zsh/blob/binarymuse/themes/darkblood.zsh-theme) 主题已通过近乎完全重写的模块化和一些新功能进行了增强。
- [darksoku](https://github.com/TooSchoolForCool/darksoku-zsh-theme) - 基于 `ys` 和 [astro](https://github.com/iplaces/astro-zsh-theme) 主题。
- [dbern](https://github.com/dbernhard-0x7CD/zsh-dbern-theme) - 包括电池状态和负载平均装饰。
- [delta (asavoy)](https://github.com/asavoy/delta-zsh-theme) - 最小的 ZSH 主题可减少干扰。包括 iTerm 颜色设置文件。
- [delta (dongri)](https://github.com/dongri/delta-zsh-theme) - 另一个带有嵌入“git”状态的最小主题。
- [delta-prompt](https://github.com/cusxio/delta-prompt) - 一个最小的 ZSH 提示符。
- [devj121](https://github.com/cjeonguk/devj121-zsh-theme) - 包括带有分支字形的“git”装饰。
- [dexter](https://github.com/shvenkat/zsh-theme-dexter) - 强调终端右侧（因此得名）的主题。
- [dfrx](https://github.com/Dofoerix/Dfrx-Prompt-Theme) - 哦我的豪华主题。包括当前目录的装饰器、最后一个命令的执行时间、根状态和时间。
- [dino](https://github.com/OdilonDamasceno/dino-zsh-theme) - 包括 Node、golang、flutter、lua、python 和 java 的装饰，还包括 `git` 装饰。需要书呆子字体。
- [dissonance](https://github.com/RyanScottLewis/theme-dissonance-zsh) - 附带自定义“LSCOLORS”和“LS_COLORS”设置文件，适用于深色和浅色终端主题。
- [diy-ys](https://github.com/aprilnops/zsh-theme) - [ys](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/ys.zsh-theme) 的变体，没有主机名或时间。
- [djkakaroto](https://github.com/djkakaroto/theme-zsh/) - 包括“git”状态装饰，适用于所有字体。
- [dkniffin](https://github.com/dkniffin/zsh-theme) - 包括“ruby”版本和“git”状态。
- [dmx](https://github.com/domix/dmx.zsh-theme) - 针对深色终端窗口进行了优化。
- [do-you-even-nix](https://github.com/miche1e/do-you-even-nix) - 简单的电力线风格主题旨在提高 [nix](https://nixos.org) 的功率。包括用户名@主机名、当前目录、“git”状态、是否在 nix shell 中以及当前目录中是否有 flake.nix 或 shell.nix 文件的装饰器。
- [domixgit](https://github.com/tariqdomi/ohmyzsh-domixgit) - 提示“git”状态和当前目录装饰器。
- [dongri](https://github.com/dongri/dongri.zsh-theme) - 显示默认分支和当前分支的极简主题。
- [doodleshell](https://github.com/cdodd/doodleshell-zsh-theme) - 极简主题，包括 `git`、`terraform` 和 `aws` 状态装饰。
- [doom](https://github.com/CMOISDEAD/doom-zsh) - 受厄运启发。看起来与电力线相似。具有可定制的段、“git”状态、“rust”、“Node.js”、“python”和“ruby”版本的装饰器。
- [dp](https://github.com/davidparsson/zsh-dp-theme) - 低对比度主题，显示当前 git 分支（如果存储库是脏的）以及“$PYENV_VERSION”的值。
- [dr4kk0nnys_v2](https://github.com/Dr4kk0nnys/Dr4kk0nnys_theme_ohmyzsh_v2/) - 适用于深色背景，包括“git”状态装饰。
- [dracula](https://github.com/dracula/zsh) - 适用于 Atom、Alfred、Chrome DevTools、iTerm 2、Sublime Text、Textmate、Terminal.app、Vim、Xcode 和 ZSH 的深色主题。
- [dragon (jeop10)](https://github.com/jeop10/dragon) - 受到 kali Linux 的启发。包括 `git` 状态和工作目录装饰。
- [dragon (sabertaximi)](https://github.com/sabertazimi/dragon-zsh-theme) - 简约，包括“git”状态信息。
- [drkat](https://github.com/katrinaalaimo/drkat-zsh-theme) - 让人想起[电力线](https://github.com/powerline/powerline)。包括目录、`git` 状态和主机名修饰。
- [droolmaw](https://github.com/isuke/droolmaw) - 可配置的提示符类似于 [Powerline](https://github.com/powerline/powerline)。需要 [Nerd 字体](https://github.com/ryanoasis/nerd-fonts)。包括用户名、当前目录、当前目录路径、日期时间、`git` 作者、`git` 状态、`mise` 语言版本和基于上次命令运行的退出状态的可配置消息的装饰器。
- [droolscar](https://github.com/isuke/droolscar) - [电力线](https://github.com/powerline/powerline) 变体。
- [dtheme](https://github.com/OlukaDenis/DTheme) - 针对使用 Solarized 终端配色方案和“git”的用户进行了优化。最适合使用 unicode 字体。
- [duckster](https://github.com/ducky/duckster) - [gitster](https://github.com/shashankmehta/dotfiles/blob/master/thesetup/zsh/.oh-my-zsh/custom/themes/gitster.zsh-theme) ZSH 主题的一个分支，更加新鲜。
- [ducula](https://github.com/janjoswig/Ducula) - 受到德古拉计划的启发。包括 `git` 状态装饰、用户名和主机名缩写、虚拟环境、当前工作目录、最后一个命令的返回状态和时间。
- [dustmod](https://github.com/bmihaila/dustmod) - 源自 oh-my-zsh 中的 [dst](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/dst.zsh-theme) 主题。
- [dwep](https://github.com/dwep1337/dwep-zsh-theme) - 包括用户名@主机名、当前目录和“git”状态的装饰器。
- [dyzsh](https://github.com/daotoyi/dyzsh-zsh-theme) - 基于 [astro](https://github.com/iplaces/astro-zsh-theme)。包括“git”分支和哈希、当前目录、用户、主机和时间的装饰器。
- [earthshaker](https://github.com/remusearthshaker/earthshaker.zsh) - 极简、朴实的 ZSH 主题，专为喜欢温暖、微妙力量和接地气美学的开发人员而设计。包括当前目录、`git` 状态和用户名@主机名的装饰器。
- [easytocloud](https://github.com/easytocloud/oh-my-easytocloud) - 基于[agnoster](https://github.com/agnoster/agnoster-zsh-theme)。包括 AWS 环境、“git”状态、用户名和当前目录的装饰器。
- [eckig](https://github.com/fouladi/eckig) - 带有 utf-8 图标的简约主题。包括“git”状态装饰和时钟。
- [efritas](https://github.com/erikfritas/efritas) - 包括用户名、主机名、`venv`、`rvm` 和 `git` 状态装饰。
- [eggshausted](https://github.com/inutano/eggshausted) - 一个“git”感知主题，适合那些厌倦了错误的人。
- [elagoht](https://github.com/Elagoht/Elagoht.zsh-theme) - 包括 user@hostname、当前目录、虚拟环境、`git` 状态、是否在 `ssh` 会话中运行以及最后一个命令的执行时间的装饰器。
- [elessar](https://github.com/fjpalacios/elessar-theme) - 基于 [gitster](https://github.com/shashankmehta/dotfiles/blob/master/thesetup/zsh/.oh-my-zsh/custom/themes/gitster.zsh-theme) 的 `git` 感知主题。需要与电力线兼容的字体。
- [elsa](https://github.com/faycito/elsa) - 包括 root 状态、pwd 和 `git` 状态装饰。
- [emojeer](https://github.com/lxynox/emojeer-ohmyzsh) - 表情符号风格的 [oh-my-zsh](https://ohmyz.sh/) 主题。
- [emoji](https://github.com/meiokubo-zz/emoji.zsh-theme) - 基于 [robbyrussell](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/robbyrussell.zsh-theme) oh-my-zsh 主题，其中“git”提示符替换为表情符号，以提高清晰度。
- [emojirussell](https://github.com/Bergiu/emojirussell) - 基于 [robbyrussell](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/robbyrussell.zsh-theme) oh-my-zsh 主题，具有当前工作目录的状态装饰、最后一个命令退出状态、`git` 分支和状态。
- [endless-dog](https://github.com/qwelyt/endless-dog) - 模仿 grml-zsh-config 的 oh-my-zsh 兼容主题。
- [enlightenment](https://github.com/w33tmaricich/enlightenment) - 包括“git”状态、“vi”模式指示器以及最后执行命令的时间的装饰。
- [enormous](https://github.com/leighmcculloch/zsh-theme-enormous) - 占用航站楼的大量空间。
- [erfan](https://github.com/ekm507/erfan-zsh-theme) - [af-magic](https://github.com/andyfleming/oh-my-zsh) 和 [macovsky](https://github.com/championswimmer/oh-my-zsh/blob/master/themes/macovsky.zsh-theme) 主题的组合。包括 `git` 和 `virtualenv` 状态装饰。
- [eriner](https://github.com/zimfw/eriner) - 受电力线启发的 [agnoster](https://github.com/agnoster/agnoster-zsh-theme) 提示主题的 Zim 分支。包括 `git` 状态装饰。
- [es6](https://github.com/suissa/oh-my-zsh-theme-es6) - 包括“git”状态的装饰器和当前目录的截断路径。
- [escape](https://github.com/fesmjke/escape/) - 包括“git”信息、用户名、时间、当前目录和最后一个命令退出状态的装饰器。
- [eubw](https://github.com/eptaccio/eubw-oh-my-zsh-theme) - 一个带有“git”信息的简单主题。
- [eucalyptus](https://github.com/relastle/eucalyptus) - 受 [agnoster](https://github.com/agnoster/agnoster-zsh-theme) 和 [powerlevel9k](https://github.com/bhilburn/powerlevel9k) 启发，为简约 vi 模式用户提供简单的一行主题。包括 `git` 状态指示器、`vi` 模式指示器、当前目录和当前路径。
- [even-more-emojis](https://github.com/odunlop/even-more-emojis) - 自定义版本的[表情符号](https://github.com/meiokubo-zz/emoji.zsh-theme)，添加了更多表情符号和更多信息。包括 `git` 状态、当前目录和最后一个命令的退出状态的装饰器。
- [excess](https://github.com/davydovanton/excess.zsh-theme) - 简单的 ZSH 颜色主题。
- [eyerelax](https://github.com/code-brewer/EyeRelax-zsh-theme) - 极简主题，带有“git”状态、venv/anaconda 环境、最后一个命令的执行时间和当前目录的装饰器。
- [ez-pz](https://github.com/mangosmoothie/ez-pz) - 带有“git”状态装饰的极简主题，灵感来自 [bureau](https://github.com/isqua/bureau)。
- [fall](https://github.com/jottenlips/seasonal-zshthemes) - 带有秋季图标的简约主题。包括 `git` 状态装饰。
- [fattyarrow](https://github.com/sohnryang/fattyarrow) - 最小的 ZSH 提示在深色背景上效果更好。
- [fbi](https://github.com/bateman/fbi-zsh-theme) - [Bureau](https://github.com/isqua/bureau) 的受电力线启发的分支，带有“nvm”环境、“git”状态、用户名@主机名和当前目录的装饰器。
- [fdT2K](https://github.com/FDT2k/FDT2K-theme) - 基于 [agnoster](https://github.com/agnoster/agnoster-zsh-theme)，预设包括 virtualenv、最后命令状态、`nvm`、`docker machine` 和 `git`、`hg` 和 `bzr` 状态装饰。
- [fe80](https://github.com/fe80/fe80.zsh-theme) - 包括`git`信息、当前目录、用户@主机名、时间和最后一个命令的返回码（当它非零时）的装饰器。
- [feder](https://github.com/samfeder/mac-themes/blob/master/feder.zsh-theme) - 干净、简单、兼容且有意义。在 Linux、Unix 和 Windows 上以 ANSI 颜色进行测试。
- [felipec](https://github.com/felipec/zsh-prompt-felipec) - 极简主题，带有当前目录、“git”状态、最后一个命令的退出代码和根状态的装饰器。
- [filthy](https://github.com/molovo/filthy) - 一个干净得令人厌恶的 ZSH 提示符。包括在“git”存储库中时“git”根路径的装饰器、“git”状态、基于上次命令运行的退出状态的提示字符以及上次运行命令的执行时间。
- [firefoxic](https://github.com/firefoxic/firefoxic-zsh-theme/) - [Bureau](https://github.com/isqua/bureau) 的分支，对节点和 `git` 装饰器进行了调整。
- [fish (raniconduh)](https://github.com/Raniconduh/zshfish) - ZSH 主题让人想起默认的“fish” shell 主题。包括 `git` 状态装饰。
- [fish (sbfkcel)](https://github.com/sbfkcel/oh-my-zsh-theme) - 极简主题，带有“git”状态、当前目录和用户名的装饰器。
- [fishbone++](https://github.com/EYH0602/Fishbonepp) - 受[oh-my-fish](https://github.com/oh-my-fish/oh-my-fish)主题fishbone和[oh-my-zsh](https://github.com/ohmyzsh)主题[typewriting](https://github.com/reobin/typewriting)影响的主题。包括当前目录的装饰器、`git` 状态、最后一个命令的退出状态。
- [fishy-lite](https://github.com/sudorook/fishy-lite) - oh-my-zsh 中原始 [fishy](https://github.com/ohmyzsh/ohmyzsh/wiki/themes#fishy) 主题的分支，删除了许多无关的内容以提高加载速度。包括电池电量表和“git”状态显示，可以在提示的右侧启用。
- [fishy2](https://github.com/akinjide/fishy2) - ZSH 主题的灵感来自 [original Fishy](https://github.com/ohmyzsh/ohmyzsh/wiki/themes#fishy)。
- [fluent-git](https://github.com/RobertKozak/fluent-git) - 显示上次命令执行的时间、错误代码、主机名、用户名、`git` 状态、kubernetes 集群和命名空间、路径和 ssh 连接状态。
- [flux](https://github.com/jmg-duarte/flux-zsh) - 带有“git”状态装饰的严肃简约主题。
- [forerunner](https://github.com/OpenReplyDE/zsh-forerunner) - [powerlevel9k](https://github.com/bhilburn/powerlevel9k) 的自定义设置。包括 `git` 状态装饰。
- [fortuity](https://github.com/VGamezz19/oh-my-zsh-fortuity-theme) - 包括最后一个命令的状态、`git` 信息和当前目录。
- [frank](https://github.com/ronmackley/frank-theme) - Frank 直击要点，在一行上简洁但易读地显示信息。弗兰克注重事实，只在重要的时候才告诉你额外的事情。
- [friendly-fiesta](https://github.com/bruino/friendly-fiesta) - [terminal-party](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/terminalparty.zsh-theme) 主题的分支。
- [frisk-arrow](https://github.com/BakeRolls/frisk-arrow) - 基于 [frisk](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/frisk.zsh-theme) oh-my-zsh-theme 的主题。
- [frisk-red](https://github.com/aishsingh/zsh/tree/master/frisk-red) - 来自 oh-my-zsh 的 [frisk](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/frisk.zsh-theme) 主题的红色版本。
- [fritz](https://github.com/fritzccc/fritz-zsh-theme) - 在深色背景上效果很好。包括 `git` 状态装饰。
- [frlo](https://github.com/fiorillo/frlo) - 使用计算机的主机名来显示（希望如此）独特的三色主题，以显示在提示中，以便您一目了然地知道您登录的是哪台计算机。
- [funkyberlin](https://github.com/Ottootto2010/funkyberlin-zsh-theme) - 色彩缤纷的两行主题，支持“git”和“svn”。
- [funkydrac](https://github.com/warshanks/funkydrac) - 基于 [funky](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/funky.zsh-theme) 的多个德古拉主题 omz 主题和基于 [oh-my-posh](https://github.com/JanDeDobbeleer/oh-my-posh) 的主题[外星人](https://github.com/JanDeDobbeleer/oh-my-posh/blob/main/themes/aliens.omp.json)
- [furio](https://github.com/hectorpalmatellez/furio-theme) - [Cloud](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/cloud.zsh-theme) oh-my-zsh 主题的分支。有不同的颜色和表情符号。
- [furry-umbrella](https://github.com/kb10uy/zsh-theme-furry-umbrella) - 色彩缤纷的主题，在深色背景上效果更好。
- [gabriel2m](https://github.com/gabriel2m/gabriel2m-oh-my-zsh-theme) - 极简主题，带有当前目录和“git”状态的装饰器。
- [gaia](https://github.com/gcaracuel/gaia.zsh-theme) - 最初是 [Bureau](https://github.com/isqua/bureau) 的一个分支，在提示中添加了新的虚拟环境信息：Kubernetes、virtualenv、rbenv 和 Java 版本。包括“git”状态集成。
- [gal](https://github.com/x6r/gal) - 基于 [gallois](https://github.com/ohmyzsh/ohmyzsh/commits/master/themes/gallois.zsh-theme) 的极简主题。
- [gallifrey-war](https://github.com/cdubos-fr/gallifrey-war) - 灵感来自 [gallifrey](https://github.com/ohmyzsh/ohmyzsh/wiki/Themes#gallifrey)。包括“git”信息、user@host 和当前目录的装饰器。
- [gallium](https://github.com/RickConsole/gallium) - 最小主题的灵感来自 [gal](https://github.com/x6r/gal) 和 [gallois](https://github.com/ohmyzsh/ohmyzsh/commits/master/themes/gallois.zsh-theme)。包括“username@host”、当前目录和“git”状态的装饰器。
- [garden](https://github.com/fecat233/garden) - 在深色终端背景下效果更好，包括“git”状态装饰。
- [garrett](https://github.com/chauncey-garrett/zsh-prompt-garrett) - Prezto 在您需要时提示您所需的信息。
- [gawaine](https://github.com/nicolaracco/gawaine.zsh-theme) - 尼古拉·拉科的主题曲。需要 `rvm` 和 `git` 插件。
- [gbt](https://github.com/jtyr/gbt) - Go Bullet Train 是一个高度可定制的提示生成器，其灵感来自 Bullet Train 和 [oh-my-zsh](https://github.com/robbyrussell/oh-my-zsh)，运行速度更快。包括许多不同状态的汽车。包括一个 [prompt-forwarding](https://github.com/jtyr/gbt#prompt-forwarding) 功能，使用户能够将用户定义的提示转发到远程计算机，并通过 SSH 在所有计算机上以及 Docker、Kubectl、Vagrant、MySQL 或 Screen 中获得相同外观的提示，而无需远程安装任何内容。
- [gcloud-prompt](https://github.com/ocadaruma/zsh-gcloud-prompt) - 在提示中显示当前的 gcloud 配置。
- [gentoo](https://github.com/ikelos/gentoo-zsh-theme) - 将 oh-my-zsh `gentoo` 主题分解为非 omz 用户的单独存储库。
- [geometry](https://github.com/geometry-zsh/geometry) - 一个最小的 ZSH 主题，可以将任何功能添加到左侧提示或（异步）右侧提示中。
- [geometryHostInfo](https://github.com/Fuzen-py/GeometryHostInfo) - 将主机信息添加到 [geometry](https://github.com/geometry-zsh/geometry) 主题。
- [gerry](https://github.com/GerryLarios/gerry-prompt) - 基于 [bureau](https://github.com/ohmyzsh/ohmyzsh/wiki/themes#bureau)，包括 `git` 状态、当前时间、用户名、主机名和当前目录的装饰。
- [get-to-work](https://github.com/Diogo13Antunes/Get_To_Work) - 简约设计，包括“git”状态、虚拟环境和时间的装饰器。
- [gg](https://github.com/YourBrightSmile/ggZshTheme) - 包括时间和“git”状态的装饰器。
- [ghoti](https://github.com/lonr/ghoti) - 模仿 `fish-shell` 默认提示符。包括 `git` 装饰。
- [gianu-alternative](https://github.com/zbentzinger/gianu-alternative-theme) - [OMZ Gianu](https://github.com/ohmyzsh/ohmyzsh/blob/61dd3682e69aa990a8a3589c5c61ea2e1edf8312/themes/gianu.zsh-theme) 的替代方案，根据权限更改提示。包括 `git` 状态和当前目录装饰器。
- [gideon](https://github.com/userhiren/oh-my-zsh-gideon-theme) - 受到 [avit](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/avit.zsh-theme) 的启发，包括 `git` 装饰、IP 地址、主机和路径。
- [gimbo](https://github.com/gimbo/gimbo.zsh-theme) - [purepower](https://github.com/romkatv/dotfiles-public/blob/master/.purepower) 的变体，具有更多功能、一点养眼效果和上下文相关的额外行。包括 `git` 状态修饰、历史记录编号、用户名/主机名上下文、目录状态、最后一个命令的状态（如果失败）以及 Python virtualenv 名称（如果存在）。
- [gimme](https://github.com/nralbrecht/gimmezsh) - 带有“git”集成的 ZSH 的简单主题。受到 [gitsome](https://github.com/mtully/gitsome) 主题的启发。
- [girazz](https://github.com/mdentremont/girazz) - 对 gnzh 主题的修改，将“vi”模式添加到右侧提示符中。
- [git-kali](https://github.com/Green0wl/zsh-git-kali-prompt) - 基于 [Kali 的信息性 `git` 提示](https://github.com/olivierverdier/zsh-git-prompt)。包括“git”状态、用户名@主机和当前目录的装饰器。
- [git-prompt (awgn)](https://github.com/awgn/git-prompt) - 针对“bash”、“zsh”和“fish”的快速“git”提示。
- [git-prompt (olivierverdier)](https://github.com/olivierverdier/zsh-git-prompt) - 显示有关当前“git”存储库的信息。特别是分支名称、与远程分支的差异、暂存或更改的文件数量等。
- [git-prompt (woefe)](https://github.com/woefe/git-prompt.zsh) - ZSH 的快速、可定制、纯 shell、异步 `git` 感知提示很大程度上受到 Olivier Verdier 的 [zsh-git-prompt](https://github.com/olivierverdier/zsh-git-prompt) 的启发，与 Fish shell 的“Informative VCS”提示非常相似。
- [git-prompt-kit](https://github.com/olets/git-prompt-kit) - 一组可配置的组件，用于以最少的编码创建功能丰富、高性能的 Git 感知 zsh 提示（也称为主题）。
- [git-simple](https://github.com/ZakharEl/git-simple-theme) - 简单的主题，包括详细的“git”状态装饰。
- [git-venv-prompt](https://github.com/walkingshamrock/zsh-git-venv-prompt) - 使用有关当前 Python 虚拟环境和 Git 状态（异步）的信息增强 Zsh 提示。它使用 zsh-async 为 Git 状态提供异步更新，并在提示符的第二行中显示虚拟环境。
- [gitbash](https://github.com/eddieantonio/gitbash-zsh-theme/) - 模仿 [Git for Windows](https://gitforwindows.org/) 的默认提示。包括 `git` status、user@host 和当前目录装饰器。
- [github](https://github.com/Debdut/github.zsh-theme/) - 受 GitHub 启发的主题。显示（截断的）当前目录、主机名和“git”状态的装饰器。包括浅色和深色模式，并检测 macOS 和 Linux 上的系统设置。
- [gitneko](https://github.com/gynamics/zsh-gitneko/) - 有一个 neko `(^>ω<^)` 提示符，其中包含 `git` 状态信息。
- [gitprompt.sh](https://github.com/danieldietrich/gitprompt.sh) - 适用于“bash”和“git”。 256色支持。包括“git”状态和当前目录的装饰器。
- [gitsome](https://github.com/mtully/gitsome) - 带有“git”信息的超级简单提示，针对[平板终端](https://github.com/ahmetsulek/flat-terminal)配色方案进行了优化。
- [gitstatus](https://github.com/kimyvgy/gitstatus-zsh-theme) - 显示命令和“git”状态装饰。
- [gitster (shashankmehta)](https://github.com/shashankmehta/dotfiles/blob/master/thesetup/zsh/.oh-my-zsh/custom/themes/gitster.zsh-theme) - 在“git”存储库中时，它显示“git”存储库根文件夹中的位置。当不在 `git` 存储库中时，它显示相对于 home 的路径，`~`。
- [gitster (zimfw)](https://github.com/zimfw/gitster) - shashankmehta 的 [gitster](https://github.com/shashankmehta/dotfiles/blob/master/thesetup/zsh/.oh-my-zsh/custom/themes/gitster.zsh-theme) 提示主题的 Zim 分支
- [gitsterv2](https://github.com/xakraz/gisterv2-zsh-theme) - 从原始的 [gitster](https://github.com/ohmyzsh/ohmyzsh/wiki/External-themes#gitster) 主题分叉。
- [gk3000](https://github.com/gk3000/gk3000-oh-my-zsh-theme) - 包括 `git` 状态修饰和当前目录的完整路径。
- [glider](https://github.com/MrRedacted/zsh-glider) - 基于 [strug](https://github.com/triplepoint Five/oh-my-zsh/blob/master/themes/strug.zsh-theme)。包括“git”状态、用户名、主机名和当前目录的装饰器。
- [glimmer](https://github.com/martnu/glimmer) - 包括 `git` 分支、时间和 user@host 装饰器。
- [gn-z11](https://github.com/xxidbr9/zsh_GN-z11-theme) - 包括“git”状态和最后一个命令的退出状态的装饰器。
- [gndx](https://github.com/gndx/gndx-zsh-theme) - 包括 `git` 状态、主机名、目录和最后一个命令退出状态装饰。
- [gnrnzh](https://github.com/PaoloneM/gnrnzh-zsh-theme) - 来自 oh-my-zsh 的 [gnzh.zsh-theme](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/gnzh.zsh-theme) 的定制。
- [gocilla](https://github.com/goranvasic/gocilla-iterm-zsh) - iTerm 2 和 ZSH 的主题。不包括 `git` 状态、user@host、路径和日期装饰器。
- [golden-prompt](https://github.com/Goldeneye128/golden-prompt) - 一个简单的提示，包含类似鱼的功能和“git”状态、当前目录的装饰器。
- [goprompt](https://github.com/NonLogicalDev/shell.async-goprompt) - 快如闪电。包括用于截断当前目录、最后命令持续时间和退出状态、vim 模式指示器、“git”信息、日期时间和父进程名称的装饰器。
- [gops](https://github.com/noxer/gops) - 类似电力线的快速提示。包括 `git` 状态、当前目录、根状态装饰。
- [gorchak](https://github.com/evgenygorchakov/oh-my-zsh-gorchak-theme/) - 受到 [robbyrussell](https://github.com/ohmyzsh/ohmyzsh/wiki/Themes#robbyrussell) 和 [af-magic](https://github.com/ohmyzsh/ohmyzsh/wiki/Themes#af-magic) 的启发。包括“git”信息和 Node.js 版本的装饰器。
- [grayt](https://github.com/evanthegrayt/grayt-zsh-theme) - 简单而信息丰富的主题，包括“git”装饰和最后一个命令的返回状态。
- [green-lambda](https://github.com/Ishidawg/minimal-green-lambda) - 极简主义 Lambda 主题。包括 `git` 装饰。
- [greencastle](https://github.com/GustavGroenborg/greencastle-zsh-theme/) - 简约主题，支持非常非常长的分支名称，而不会严重截断提示。该主题的灵感来自 [jonathan 主题](https://github.com/thlorenz/oh-my-zsh/blob/master/themes/jonathan.zsh-theme) 和 [robby russel 主题](https://github.com/thlorenz/oh-my-zsh/blob/master/themes/robbyrussell.zsh-theme)。包括当前目录的装饰器、“git”信息和最后一个命令运行的退出状态。
- [greenclean](https://github.com/dmicha16/greenclean) - [akz92/clean](https://github.com/akz92/clean) 的分叉，右侧有一个更绿色和永久的时钟。
- [griffin](https://github.com/GriffinLedingham/griffin.zsh-theme) - 极简主义，包括“git”状态装饰。
- [grs](https://github.com/gersontpc/zsh-theme-grs) - 包括 `git` 状态、用户 ID 和工作目录装饰器。
- [gruvbox (hgaiser)](https://github.com/hgaiser/gruvbox-zsh) - 从 [gruvbox](https://github.com/morhetz/gruvbox) `vim` 插件设置颜色。
- [gruvbox (sbugzu)](https://github.com/sbugzu/gruvbox-zsh) - 基于 [agnoster](https://gist.github.com/agnoster/3712874)，使用与 [gruvbox](https://github.com/morhetz/gruvbox) `vim` 插件相同的颜色。
- [guezwhoz](https://github.com/guesswhozzz/guezwhoz-zshell) - 极简主义，包括“git”状态装饰。
- [gugulenok](https://github.com/gugulen0k/gugulenok/) - 有深色和浅色两种模式。包括“git”状态、时间和当前目录的装饰器。
- [guri](https://github.com/victorfsf/guri) - 一个简单快速的 Oh-My-Zsh 主题，基于 [Pure](https://github.com/sindresorhus/pure) 的设计。
- [gus](https://github.com/gusye1234/Gus-zsh-theme/) - 可破解的瞬态主题。包括 conda、`git` 信息和当前目录的装饰器。
- [hackersaurus](https://github.com/bhilburn/hackersaurus) - 带有“git”状态和最后一个命令运行装饰器的退出代码的主题嵌入在提示中。与 [powerlevel9k](https://github.com/bhilburn/powerlevel9k) 相关。
- [halfeld](https://github.com/IgorHalfeld/halfeld-zsh-theme) - 带有“git”装饰的简约主题。
- [halil](https://github.com/5m0k3r/zsh-themes) - oh-my-zsh 的 [amuse](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/amuse.zsh-theme) 主题的分支。
- [hana-matcha](https://github.com/arturoalviar/hana-matcha-zsh-theme) - A simple theme with the first character being 花(hana), the kanji for flower. This theme was inspired by a keycap set called DSA Hana. This pairs well with the [hana atom](https://github.com/arturoalviar/hana-matcha-syntax) theme. Includes `git` status decorations.
- [handy](https://github.com/hanleylee/handy) - 色彩缤纷且轻巧的主题。显示 root 状态、`git` 状态、当前目录和 `user@hostname` 装饰。
- [hanpen](https://github.com/kojole/hanpen.zsh-theme) - 显示“git”分支和状态、最后一个命令退出代码、最后一个命令执行时间（如果超过“ZSH_THEME_HANPEN_CMD_MAX_EXEC_TIME”）。
- [hapin](https://github.com/hanamiyuna/hapin-zsh-theme/blob/master/hapin.zsh-theme) - 基于 Oxide，包括 `git` 状态装饰和当前用户/主机信息。
- [happy-coding](https://github.com/lexhuismans/happy-coding/) - [passion](https://github.com/ChesterYue/ohmyzsh-theme-passion) 的精简版本。包括时间、`git` 分支、最后命令执行时间和最后命令退出状态的装饰器。
- [hcompact](https://github.com/fusion809/zsh-theme) - 显示时间、操作系统（如果在 Linux 上，则包括发行版）、目录以及是否以 root 身份运行。
- [headline](https://github.com/Moarram/headline) - 响应式 ZSH 主题，具有 Git 状态信息和提示上方的彩色线。
- [heapbytes](https://github.com/heapbytes/heapbytes-zsh) - 包括当前目录的装饰器、tun0 ip（如果在 VPN 上）、wlan ip（不在 VPN 上时）和“git”信息。
- [heart](https://github.com/gko/heart) - 浅色背景的心形主题提示。
- [hedroed-bureau](https://github.com/Hedroed/hedroed-bureau.zsh-theme) - 基于 [bureau](https://github.com/ohmyzsh/ohmyzsh/wiki/Themes#bureau)，添加了 `git` 状态装饰和 `npm` 状态。
- [helb](https://github.com/helb/helb.zshtheme) - 松散地基于 Gentoo 的旧“bash”主题。包括`git`信息，最后一个命令的返回值，并为用户（`$`）和root（`#`）使用不同的用户名颜色和提示符。
- [hematite](https://github.com/bigdave/hematite) - 极简主义促销，试图仅显示在给定时间有效的状态装饰。
- [hex](https://github.com/hectorBrown/hex-zsh) - 很大程度上基于 [bira](https://github.com/ohmyzsh/ohmyzsh/wiki/Themes#bira) 和 [gruvbox](https://github.com/sbugzu/gruvbox-zsh)，而 [gruvbox](https://github.com/sbugzu/gruvbox-zsh) 又基于 [agnoster](https://gist.github.com/agnoster/3712874)。包括当前目录的装饰器、`git` 状态信息、活动的 python virtualenv、最后一个命令运行的退出状态。需要与电力线兼容的字体。
- [hexagon](https://github.com/diogoazevedos/hexagon) - 基于[geometry](https://github.com/geometry-zsh/geometry)的极简ZSH主题。
- [hfulldate](https://github.com/fusion809/zsh-theme) - 显示时间、日期、操作系统（如果在 Linux 上，则包括发行版）、目录以及是否以 root 身份运行。
- [hhktony](https://github.com/hhktony/hhktony.zsh-theme) - 灵感来自 robbyrussell 主题 + ssh 连接状态提示。
- [hietan](https://github.com/Hietan/Hietan_ZshTheme) - 包括当前目录、日期和时间、`git` 状态和最后一个命令运行的退出值的装饰器。需要 [Nerd 字体](https://github.com/ryanoasis/nerd-fonts)。
- [hijack](https://github.com/thegodheehee/hijack-zsh) - 包括 user@hostname、当前目录和 `git` 信息的装饰器。
- [hina](https://github.com/ucpr/hina) - 用“golang”编写，包括“git”状态装饰和 kubernetes 上下文。
- [hip-fellow](https://github.com/haitaim/hip-fellow) - 包括“git”状态装饰并适用于标准字体。
- [hipstersmoothie-p9x](https://github.com/hipstersmoothie/PowerlevelHipstersmoothie) - [powerlevel9k](https://github.com/bhilburn/powerlevel9k) 的变体。
- [ho-my-zsh](https://github.com/Mboukhal/hoMyZsh_theme) - 包括当前目录和“git”信息的装饰器。
- [hoffish](https://github.com/emilHof/hoffish-zsh-theme) - 如果 [agnoster](https://github.com/agnoster/agnoster-zsh-theme) 主题和 [fish](https://fishshell.com/) shell 有一个针对子项的 ZSH 主题。包括“git”状态的装饰器、当前目录的修剪路径、根状态、最后一个命令运行的退出状态和活动的 python virtualenv。需要 Powerline 字体和 [zsh-autosuggestions](https://github.com/zsh-users/zsh-autosuggestions) 和 [shrink-path](https://github.com/ohmyzsh/ohmyzsh/blob/master/plugins/shrink-path/shrink-path.plugin.zsh) 插件。
- [hogbal](https://github.com/hogbal/hogbal.zsh-theme) - 最适合深色背景和 256 色终端程序。包括 `virtualenv`、`git` 信息、`username@hostname` 和当前目录的装饰器。
- [home](https://github.com/sheerun/home) - 漂亮而简短的一行主题，让您有宾至如归的感觉。
- [hometown](https://github.com/olets/hometown-prompt) - 功能丰富、高性能的“git”感知 ZSH 主题，其中包含用户、主机、时间、当前工作目录及其父目录的分段，以及 Git 存储库中详细的完整 Git 状态。
- [honukai-iterm](https://github.com/oskarkrawczyk/honukai-iterm-zsh) - oh-my-zsh 和 iTerm 2 的 Honukai 主题和颜色。
- [hoozeeth](https://github.com/hooay233/Hoozeeth) - 极简主题，包括 user@hostname、日期和时间以及当前工作目录的装饰器。
- [horizontal](https://github.com/nuimk/horizontal) - 带水平分隔符的两行提示。
- [hornix](https://github.com/fusion809/zsh-theme) - 显示时间和日期、操作系统（如果在 Linux 上，则包括发行版）、目录以及是否以 root 身份运行。
- [horse-sh](https://github.com/emileswarts/horse-sh) - 一个非常简约的棕色/红色 ZSH 主题。
- [htb](https://github.com/ibyf0r3ns1cs/zsh-htb-theme) - 受到 HackTheBox 机器上的 pwnbox 的启发。包括 user@host、IP 地址和当前目录的装饰器。
- [hub](https://gist.github.com/hub23/c226b1c77446e099f7684b0d21c6b22a) - 简单干净，包括最后执行的命令的返回代码。
- [humbled](https://github.com/saravanabalagi/zsh-theme-humbled) - 一个干净而朴素的主题，具有左对齐的“condaenv”、“virtualenv”和“git”状态。需要 [condaenv](https://github.com/saravanabalagi/zsh-plugin-condaenv) 插件。
- [hyper](https://github.com/willmendesneto/hyper-oh-my-zsh) - 设计用于超级终端主题，包括“git”状态装饰。
- [hyperzsh](https://github.com/tylerreckart/hyperzsh) - 为您提供您正在处理的分支和存储库状态的全面概述，而不会使您的终端混乱。
- [iamskok](https://github.com/iamskok/iamskok.zsh-theme) - 在深色背景上效果很好。
- [iay](https://github.com/aaqaishtyaq/iay) - 用 Rust 编写的 `{ba,z}sh` 提示符。包括当前目录和“git”状态的装饰。
- [ice](https://github.com/Lenart12/ice.zsh-theme) - 对 [bureau](https://github.com/isqua/bureau) 主题与 [bira](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/bira.zsh-theme) 进行了非常轻微的修改。
- [ichirei](https://github.com/ichirei/ichirei.zsh-theme) - 丰富多彩的。包括“git”状态、时间和当前目录的装饰器。需要 [Nerd 字体](https://github.com/ryanoasis/nerd-fonts)。
- [icicle](https://github.com/JamesConlan96/Icicle) - 包括 `git` 状态装饰，以及是否以 root 身份运行。
- [igeek](https://github.com/Saleh7/igeek-zsh-theme) - 启动新终端会话时显示系统信息。
- [iggy](https://github.com/eugenk/zsh-prompt-iggy) - 一个超级快乐、很棒的 Powerline 风格、支持 `git` 的 **prezto only** 主题。
- [igorsilva](https://github.com/igor9silva/igorsilva-zsh-theme) - 显示当前目录、可自定义分隔符、当前分支和“git”状态装饰器。
- [iguanidae](https://github.com/btd1337/iguanidae-zsh-theme) - 包括 `git`、`nvm` 和 `venv` 装饰。
- [illusion](https://github.com/shabane/illusion) - 包括用户名、当前工作目录、`git` 状态和最后命令状态装饰器。
- [illuvia-gitster](https://github.com/lopezator/lluvia-gitster) - [ergenekonyigit/lambda-gitster](https://github.com/ergenekonyigit/lambda-gitster) 的分支，具有间距改进和更新的图标。包括 `git` 状态信息。
- [imp](https://github.com/igormp/Imp) - 基于 [zork](https://github.com/Bash-it/bash-it/wiki/Themes#zork) 并针对深色背景进行了优化。
- [imranic](https://github.com/alimranahmed/zsh-imranic-themes) - 极简主题，带有“git”状态、python virtualenv、rvm ruby​​ 版本、conda 版本、kube 状态和当前目录的装饰器。
- [infernus](https://github.com/jshiell/infernus-zsh-theme) - 极简主题，在深色背景上效果更好。
- [infinite](https://github.com/The-Infinitys/zsh-infinite) - 用 Rust 编写的高度可定制和动态的 ZSH 主题。 Infinite 提供了强大的 CLI 工具来管理 ZSH 提示符的外观，允许动态内容、复杂的着色和独特的视觉分隔符。
- [infoline](https://github.com/hevi9/infoline-zsh-theme) - 干净的主题，显示“git”状态、后台作业、远程主机和其他信息。
- [integral](https://github.com/Readf0x/integral-prompt) - 受数学启发，包括时间、当前目录和“git”状态的装饰器。
- [inthedeepspace](https://github.com/alionapermes/inthedeepspace/) - 基于 [intheloop](https://github.com/ohmyzsh/ohmyzsh/wiki/Themes#user-content-intheloop) 并受到 [vim-deep-space](https://github.com/tyrannicaltoucan/vim-deep-space) 的启发。
- [intheloop-powerline](https://github.com/zyphrus/intheloop-powerline) - [intheloop](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/intheloop.zsh-theme) 主题的扩展，用于使用电力线字体。
- [itg](https://github.com/itsthatguy/itg.zsh-theme) - 这是那个家伙的主题。
- [itlbv](https://github.com/itlbv/itlbv-ohmyzsh-theme) - 极简主义者。包括“git”状态和当前目录的装饰器。
- [ittecture](https://github.com/ittecture/ittecture-omz-theme) - 包括当前目录和“git”信息的装饰器。
- [ivabus](https://github.com/ivabus/ivabus-zsh-theme) - 受到 GitHub Codespaces 提示的启发。包括“git”状态、用户名和当前目录的装饰器。
- [ivy](https://github.com/ivyhjk/ohmyzsh-theme-ivy) - 在深色背景上效果很好。包括 user@host、`git` 状态和时间装饰器。基于 [obraun](https://github.com/ohmyzsh/ohmyzsh/wiki/Themes#obraun) 主题。
- [jacobin](https://github.com/Jsharkc/jacobin-zsh-theme) - 基于精致和 ys 主题，包括 `git` 状态装饰。包括可选的 iterm2 配色方案。
- [jake](https://github.com/JakeHuneau/Jake.zsh-theme) - 显示时间、当前目录和“git”分支信息，包括分支名称和红色 +（如果分支有未推送的更改）。
- [jam](https://github.com/jesusangelm/Jam-Zsh-Theme) - 针对深色背景进行了优化，包括“git”状态和“rvm”状态。
- [jax](https://github.com/jhammerberg/jax-theme) 让人想起电力线。包括当前目录和当前用户的装饰器。
- [jc](https://github.com/jclementex/jc-zsh-theme) - 对于深色终端背景，包括“git”状态信息。
- [jcl](https://github.com/jasonlewis/jcl-zsh-theme) - 松散地基于“ys”主题。
- [jeff](https://github.com/jbaranski/jeff-zsh-theme) - 基于 [bira](https://github.com/ohmyzsh/ohmyzsh/wiki/Themes#bira)。  包括 user@host、时间、当前目录和 `git` 状态的装饰器。
- [jerome](https://github.com/jeromescuggs/jerome-theme) - 基于 [dieter](https://github.com/jeromescuggs/jerome-theme) 主题的彩色主题，但具有黄色主机名。包括 `git` 装饰。
- [jhleeeme](https://github.com/JHLeeeMe/JHLeeeMe-Zsh-Theme) - 包括 `git` 和 python virtualenv 状态装饰、用户、密码、时间和系统名称。
- [jmsp](https://github.com/juacu7340/jmsp.zsh-theme) - 专注于简单性和 SSH 实用性。包括 `git` 状态和当前目录装饰器。
- [jmtech](https://github.com/jmaaltech/jmtech-zsh-theme) - 可定制的颜色和符号。包括“git”状态、上次命令运行的退出状态、“gpg”签名信息和时间戳的装饰器。 “git”状态图标需要 [Nerd Font](https://github.com/ryanoasis/nerd-fonts)。
- [jnooree](https://github.com/jnooree/jnooree-zsh-theme) - 极简主题，颜色改编自 [robbyrussell](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/robbyrussell.zsh-theme) 主题。包括“git”状态的装饰器，无论是否以非默认用户和当前工作目录运行。
- [joje](https://github.com/joje6/joje.zsh-theme) - 包括“git”状态和当前目录的装饰器。
- [jon](https://github.com/Jon-Schneider/jon.zsh-theme) - 简化的 [bira](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/bira.zsh-theme)，颜色为 [robbyrussell](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/robbyrussell.zsh-theme)。
- [jovial](https://github.com/zthxxx/jovial) - 显示主机、用户、路径、开发环境、`git` 分支以及哪个 `python` venv 处于活动状态的装饰器。
- [jpegleg](https://github.com/jpegleg/zshrc) - 与黑血主题类似，包括时间戳和“git”装饰。
- [js-magic](https://github.com/JSextonn/js-magic) - [af-magic](https://github.com/andyfleming/oh-my-zsh/blob/master/themes/af-magic.zsh-theme) 的简化版。包括当前工作目录和“git”状态装饰。
- [judgedim](https://github.com/judgedim/oh-my-zsh-judgedim-theme) - 极简提示。
- [just-another](https://github.com/supertassu/another-theme) - 只是另一个主题，当您通过 ssh 连接到另一台机器时带有主机名。
- [just-around-the-corner](https://github.com/DevinLeamy/just-around-the-corner) - 倒数着距离圣诞节还有几天。包括 `git` 状态装饰。
- [jwalter](https://github.com/jeffwalter/zsh-jwalter) - 具有“git”、“svn”、“npm”、“rvm”和网络感知的电力线风格主题。需要与电力线兼容的终端字体。
- [jyumpp](https://github.com/Jyumpp/jyumpp-zsh-theme) - Powerlevel 10K 的配置文件和安装程序。
- [kali-like](https://github.com/clamy54/kali-like-zsh-theme) - 受到 Kali Linux 默认 ZSH 主题的启发。包括 user@host、当前目录和 `git` 信息的装饰器。
- [kali](https://github.com/h4ck3r0/kali-theme) - 包括 `git` 装饰。
- [kalsowerus](https://github.com/kalsowerus/kalsowerus.zsh-theme) - 受电力线启发的彩色多行主题，包括“git”状态、目录、最后一个命令退出状态和“nvm”信息的装饰。
- [karu](https://github.com/zaari/karu) - 极简单行 ZSH 提示符。
- [kawaii](https://github.com/LeonidPilyugin/kawaii-oh-my-zsh/) - 具有终端和虚拟控制台模式。包括用户名、目录、最后命令退出状态、时间戳和“git”状态的装饰器。
- [keloran](https://github.com/Keloran/keloran.zsh-theme) - 包含其他主题的一些功能的主题。
- [kenton](https://github.com/notnek/zsh-theme) - 针对深色背景进行了优化，包括“git”状态信息。
- [kerneldiego](https://github.com/KernelDiego/kerneldiego-zsh-theme) - 一个简约而信息丰富的 Zsh 主题，具有干净的盒式布局、Git 集成和彩色提示指示器，可提高工作效率和视觉清晰度。
- [kevin](https://github.com/KevinParnell/Kevin-zsh) - 丰富多彩的主题，包括 iTerm 2 配色方案。
- [kgzsh](https://github.com/Kashugoyal/kgzsh) - 包括“git”状态装饰，在较暗的背景下效果很好。
- [kido](https://github.com/KidoThunder/kido-zsh-theme) - 基于“ys”和“robbyrussell”主题。包括最后一个命令运行的退出代码、python virtualenv 和 VCS 状态的装饰器。
- [kimwz](https://github.com/kimwz/kimwz-oh-my-zsh-theme) - 最小的主题。
- [kinda-fishy](https://github.com/folixg/kinda-fishy-theme) - 基于 Fishy 主题，但显示完整路径而不是缩写目录，并且仅在“ssh”会话和 docker 容器中显示 user@machine。
- [kindahv](https://github.com/kshnkvn/kindahv-zsh-theme) - 一个干净的 ZSH 主题，具有命令执行时间跟踪功能。
- [kiss](https://github.com/rileytwo/kiss) - 适用于 oh-my-zsh、VSCode、iTerm2、Neovim 和 RStudio 的简单主题。包括 `git` 状态装饰。
- [kketcham](https://github.com/prototype27/kketcham) - “git”信息上带有漂亮颜色的主题。
- [ko](https://github.com/JoshBenn/KoTheme-for-Oh-My-Zsh/) - 包括“git”状态和当前目录的装饰器。
- [kote](https://github.com/wendygaoyuan/kote-zsh-theme) - 最适合深色背景。包括 `git` 状态装饰。
- [kotterstep](https://github.com/sorenvonsarvort/kotterstep-zsh-theme) - 专为黑暗终端设计的两行主题，具有“git”装饰。
- [krak3n](https://github.com/krak3n/zsh-theme) - 显示 golang 版本和当前的 `git` 分支。
- [kraken](https://github.com/KrakenTheme/kraken-zsh) - ZSH 的深色主题。
- [ksposh](https://github.com/KSposh/ksposh-zsh-theme) - 包括 python 虚拟环境的装饰器、`git` 信息、当前目录和用户名。
- [kumavis](https://github.com/kumavis/kumavis-zsh-theme) - Agnoster 前叉针对日晒端子进行了优化。需要电力线兼容的字体。
- [kw](https://github.com/Kwpolska/kw.zsh-theme) - 带有“git”和“hg”状态信息的彩色主题，能够向主机名添加特定于主机的颜色。
- [kyuu](https://github.com/arturoalviar/kyuu-zsh-theme) - A simple theme with the first character being 九(kyuu), the number 9. The primary color is blue with a magenta accent. Includes `git` status decorations.
- [lacerate](https://github.com/Petrushevsky-A/Lacerate-zsh-theme) - 极简主题，带有“git”、“hg”和 python“venv”状态装饰。
- [laconic](https://github.com/Saka7/laconic.zsh-theme) - 带有“git”状态和当前目录装饰器的简单主题。
- [lagnoda](https://github.com/jashezan/lagnoda) 受到 [agnoster](https://gist.github.com/agnoster/3712874) 和 `lambda` 主题的启发。包括用户名@主机名、当前目录、`git`、`hg`或`bzr`状态、当前virtualenv、上次命令运行的退出状态和当前aws配置文件的装饰器。
- [lagune](https://github.com/noplay/lagune) - 一个最小的 ZSH 主题。
- [lambda (cdimascio)](https://github.com/cdimascio/lambda-zsh-theme) - 受到 lambda(https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/lambda.zsh-theme) 主题的启发。包括 `git` 状态装饰。
- [lambda (halfo)](https://github.com/halfo/lambda-mod-zsh-theme/) - 针对使用 unicode 兼容字体和终端应用程序的“git”用户优化的 ZSH 主题。
- [lambda-blazinggit](https://github.com/zalefin/lambda-blazinggit) - 包括快速、详细的“git”信息。需要 [Nerd Fonts](https://github.com/ryanoasis/nerd-fonts) 和 [gitstatus](https://github.com/romkatv/gitstatus) 插件。
- [lambda-gitster](https://github.com/ergenekonyigit/lambda-gitster) - 包含“git”信息的极简提示。
- [lambda-minimal](https://github.com/sohnryang/lambda-minimal-theme) - 基于 lambda 的简单主题，具有“git”状态和 virtualenv 信息。
- [lambda-mod](https://github.com/halfo/lambda-mod-zsh-theme) - 一个简单的 ZSH 主题，针对“git”使用进行了优化。
- [lambda-p](https://github.com/paimanbandi/lambda-p) - 受到 [lambda mod](https://github.com/halfo/lambda-mod-zsh-theme) 和 [Lambda V](https://github.com/vkaracic/lambdav-zsh-theme) 主题的启发。包括 `git` 状态装饰。
- [lambda-pure](https://github.com/marszall87/lambda-pure) - 一个最小的 ZSH 主题，基于 [pure](https://github.com/sindresorhus/pure)，添加了 Node.js 版本装饰器。
- [lambda-v](https://github.com/vkaracic/lambdav-zsh-theme) - Lambda 和 Fishy 主题的组合，包括“git”状态装饰。
- [lambda-zen](https://github.com/seamile/lambda-zen) - 受到 [lambda mod 主题](https://github.com/halfo/lambda-mod-zsh-theme) 的启发，带有图形化的“git”状态装饰。
- [lambder](https://github.com/avillen/zsh-theme-lambder) - 包括“git”状态装饰，最适合深色终端主题。
- [laniksj](https://github.com/LanikSJ/laniksj-zsh-theme) - 在深色背景上效果最佳。基于伟大的“ys”主题和 [Honukai ZSH 主题](https://github.com/oskarkrawczyk/honukai-iterm-zsh)。显示 root 状态和 `git` 状态装饰。
- [larn](https://github.com/tourcoder/larn.zsh-theme) - 一个干净且可定制的 oh my zsh 主题，与 Git 集成，专为黑暗终端设计。它具有彩色提示，带有“git”分支和状态指示器的装饰器、当前目录以及文件和目录的不同“ls”颜色。
- [lazyprodigy](https://github.com/drewlustro/lazyprodigy-zsh-theme) - 针对暗终端进行了优化，具有针对本地和远程系统的变体。
- [lcars](https://github.com/lgulliver/lcars-zsh-theme) - Oh My Zsh 的主题是《星际迷航：下一代 LCARS》，具有现代电力线风格的片段和真实的调色板。包括“git”状态、时间、路径、操作系统和电池电量的装饰器。
- [leafia](https://github.com/Ghostrick/leafia-prompt) - 叶茂盛的 prezto 主题，显示“git”状态信息。
- [lean](https://github.com/miekg/lean) - 灵感来自[pure](https://github.com/sindresorhus/pure)。具有“git”状态信息、最后一个命令运行的退出状态以及最后一个命令的运行时间的装饰器。
- [leon](https://github.com/prince-an/Leon_zshTheme) - 在浅色背景下效果很好。包括 `git` 状态、时间、用户名@主机、工作目录和最后一个命令退出状态装饰。
- [less-noise](https://github.com/ablil/less-noise) - 极简主题，带有“git”状态、当前目录和当前时间的装饰器。
- [leverage](https://github.com/gschnall/leverage) - 基于[minimal](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/minimal.zsh-theme)，使用颜色和额外的“Ø”字符，以更好地区分命令行提示符和输出。
- [lewis](https://github.com/lewisflude/oh-my-lewis) - 黑、白、红主题。显示 `git` 状态信息。
- [lgbt](https://github.com/nautilor/lgbt.zsh-theme) - 色彩缤纷的主题，带有当前目录和“git”状态的装饰器。
- [lgbtq](https://github.com/PhoenixSmaug/zsh-lgbtq-themes) - 适用于您的终端的 lgbtq 主题集合。
- [light](https://github.com/InfinityUniverse0/light-zsh) - 在浅色背景上效果最佳。包括 username@hostname、`git` status 和当前目录的装饰器。
- [lightbulb](https://github.com/lightbulb703/lightbulb-zsh-theme) - 包括内核、操作系统版本、正常运行时间和“git”的装饰。
- [lighthaus](https://github.com/lighthaus-theme/zsh) - 与 [Lighthaus](https://github.com/lighthaus-theme/lighthaus) 主题相得益彰的提示。显示“git”信息、GitHub/GitLab 徽标并显示发生的更改。
- [lila](https://github.com/raphaelivan/lila-zsh-theme) - 极简主题，最适合深色终端背景。
- [lilith](https://github.com/aknackd/zsh-themes) - 修改 [galllifrey](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/gallifrey.zsh-theme) 和 [hyperzsh](https://github.com/tylerreckart/hyperzsh)。
- [lime](https://github.com/yous/lime) - 简单且易于定制的 ZSH 主题。
- [limpide](https://github.com/shooteram/limpide) - [miloshadzic](https://github.com/ohmyzsh/ohmyzsh/wiki/themes#miloshadzic) 主题的修改版本，显示父目录和当前目录。
- [linear](https://github.com/MrYazdan/zsh-linear-theme) - 让人想起电力线。包括带有“git”状态、Pythonvirtualenv、当前目录和当前时间的段。
- [link](https://github.com/kylegl/link-zsh-theme) - 极简主义者。包括 `git` 状态和最后一个命令退出装饰。
- [linuxero](https://github.com/andreshincapier/linuxero) - 极简主义者。包括 root 状态、当前目录、`git` 状态、当前 ruby​​ rvm 环境和当前 python virtualenv 的装饰。
- [liquidprompt](https://github.com/nojhan/liquidprompt) - 功能齐全且精心设计的自适应提示，可在您需要时提供有用的信息。它会在您需要时向您显示您需要什么。当它发生变化时，您会注意到发生了什么变化，从而节省时间并减少挫败感。
- [lish](https://github.com/bashelled/lish) - 休闲主题。没有粗糙感，只是光滑。包括`git`、user@host、最后一个命令退出状态、当前目录、当前时间和根状态装饰器。
- [liver](https://github.com/RenoirTan/liver.zsh-theme) - 丰富多彩，包括“git”状态、用户、主机、当前存储库根装饰的当前路径和相对路径。
- [llama](https://github.com/PsychoLlama/llama.zsh-theme) - 挑剔的美洲驼使用的极简主义主题。
- [logico](https://github.com/logico/logico-zsh-theme) - 有“git”装饰。显示 vi 模式的远程状态和指示器。
- [lone-star](https://github.com/designfrontier/lonestar-zsh-theme/blob/master/lone-star.zsh-theme) - 基于 Sindre Sorhus 的纯粹主题的德克萨斯主题。
- [longsilvern](https://github.com/long263/longsilvern-zsh-theme) - 包括`git`和紧凑的`pwd`装饰。
- [lorond](https://github.com/lorond/zsh-lorond/) - [af-magic](https://github.com/andyfleming/oh-my-zsh/blob/master/themes/af-magic.zsh-theme)的精简版。包括“git”状态，适用于标准字体。
- [lperezp](https://github.com/lperezp/lperezp-zsh-theme) - 包括 user@hostname、`git` 状态、当前目录和最后一个命令运行的退出状态的装饰器。
- [lpha3cho](https://github.com/sdcampbell/lpha3cho-Oh-My-Zsh-theme-for-pentesters) - 针对渗透测试人员的 [intheloop](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/intheloop.zsh-theme) 主题的修改版本，其中包括渗透测试日志记录的日期、时间和 IP 地址。
- [luceast](https://github.com/LucEast/luceast-zsh-theme) - 针对“git”进行了优化。包括用户名、主机、时间和工作目录的装饰。
- [luckycoding](https://github.com/ZitherPeng/oh-my-zsh-luckycoding-theme) - 基于 [robbyrussell](https://github.com/robbyrussell/oh-my-zsh/blob/master/themes/robbyrussell.zsh-theme) 主题，包括 `git` 装饰和最后一个命令的退出代码。
- [ludvig](https://github.com/daviludvig/ludvig-theme-zsh) - 极简主义者。包括`git`状态、当前目录、当前时间和最后一个命令的退出状态的装饰器。
- [ludwigws](https://github.com/LudwigWS/my-zsh-theme) - [lambda-mod](https://github.com/halfo/lambda-mod-zsh-theme) 主题的变体。有“git”装饰，需要与电力线兼容的终端字体。
- [luke](https://github.com/xueguangl23/luke_zsh_theme) - 包括 `git` 装饰。基于 [frisk](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/frisk.zsh-theme) oh-my-zsh 主题。
- [lukerandall-extended](https://github.com/mpyw/oh-my-zsh-lukerandall-extended) - [lukerandall](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/lukerandall.zsh-theme) 主题的扩展版本。包括“git”状态和最后一个命令运行的状态的装饰。
- [lunachar](https://codeberg.org/ar-mo/armans-zsh-themes) - 极简主义主题。
- [macos](https://github.com/alejandromume/macos-zsh-theme) - 包括 `git` 状态装饰。
- [mad](https://github.com/MartinWie/ohmyzsh-theme-mad) - 包括 `git` 状态和最后命令执行时间装饰。
- [madas](https://github.com/utauyo/madas-zsh-theme) - 灵感来自 af-magic。包括“git”状态、user@host 以及最后一个命令是否失败的装饰器。
- [magento](https://github.com/cmuench/zsh-magento-cloud/blob/main/zsh-magento-cloud.plugin.zsh) - 添加 Magento Cloud 命令行界面 ([magento-cloud CLI](https://experienceleague.adobe.com/docs/commerce-cloud-service/user-guide/dev-tools/cloud-cli.html?lang=en)) 完成。
- [magicmace](https://github.com/zimfw/magicmace) - 受到 xero 的 ZSH 提示和 [eriner 的提示](https://github.com/zimfw/eriner) 的启发。包括活动 python `venv` 的状态代码、最后一个命令的退出状态、缩短的工作目录、`git` 状态装饰。
- [magico](https://github.com/IOsonoTAN/magico) - IOsonoTAN 的 magico 主题。
- [magpie](https://github.com/wdjcodes/magpie) - 具有自定义逻辑的极简主题，用于显示相对于当前“git”根目录的路径。包括时间、当前目录、用户名@主机名和“git”状态的装饰器。
- [mainnika](https://github.com/mainnika/zsh-theme-mainnika/) - 包括最后一个命令退出状态以及 1、5 和 15 分钟平均负载的装饰器。
- [maivana](https://github.com/nylo-andry/zsh-themes) - 包括“kubectl”上下文、“git”状态装饰。
- [majemoji](https://github.com/metalogica/majemoji) - 将随机表情符号添加到每个会话的提示中。包括 `git` 状态装饰。
- [malev](https://github.com/mvinan/malev-zsh-theme) - 有极简主义和普通两种变体。包括主机名、目录、`git` 状态和最后一个命令的退出状态的装饰器。
- [mantis](https://github.com/dann254/mantis-zsh-theme) - 带有“git”状态和信息装饰器的最小主题。
- [materialshell](https://github.com/carloscuesta/materialshell) - 为您的外壳设计的 [material design](https://material.io/guidelines/style/color.html) 主题，具有良好的对比度，并且在重要部分具有流行的颜色。旨在方便眼睛。
- [matrix](https://github.com/pot-code/matrix-zsh-theme) - [powerlevel9k](https://github.com/bhilburn/powerlevel9k) 的变体，风格看起来像《黑客帝国》电影三部曲中的东西。包括 `git` 状态装饰。
- [matter](https://github.com/mrobillard/matter-zsh-theme) - 显示“git”状态、AWS 保管库角色、后台作业、最后一个命令的退出代码和主机名。
- [mau](https://github.com/vichargrave/mau) - 带有猫风格的 ZSH 主题。包括 `git` 状态装饰。基于 [kphoen](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/kphoen.zsh-theme) 和 [smt](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/smt.zsh-theme) 主题。
- [mbolis](https://github.com/mbolis/mbolis-zsh-theme) - 包括 `git` 装饰、更改 root 用户提示颜色、活动作业和 [jenv](https://github.com/jenv/jenv) 集成。
- [mdmini](https://github.com/MarioDena/MDmini) - 包括 `git` 和 `ssh` 状态装饰。
- [meganerd](https://github.com/meganerd/meganerd-zsh/) - 灵感来自乔纳森.包括 `git` 状态、用户@主机名、当前目录、时间和最后一个命令的退出状态的装饰器。
- [megaprompt](https://github.com/willghatch/zsh-megaprompt) - 一个最大化的提示，包括键盘模式、所有权信息和其他上下文信息，以 λ 作为提示字符。需要 [hooks](https://github.com/willghatch/zsh-hooks) 插件。
- [metalmajor](https://github.com/deblauwetom/metalmajor-zsh-theme) - 包括 `git` 状态装饰，如果非零则显示最后一个命令的退出代码。
- [mexassi](https://github.com/Mexassi/mexassi-zsh-theme) - 检查“/sys/class/power_supply”文件夹以确定系统是否安装在笔记本电脑或台式机上。 grepping acpi 命令读取电池百分比并将其显示在提示中。包括 `git` 装饰。
- [mh-fzj](https://github.com/mh-firouzjaah/mh-fzj-oh-my-zsh-theme-v1) - 包括 `rvm` 和 `git` 状态装饰。
- [michaelpass](https://github.com/michaelpass/michaelpass.zsh-theme) - POSIX 友好的跨平台 [alanpeabody](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/alanpeabody.zsh-theme) mod w/方便的时间戳和完整的 git/ruby 支持。
- [michelebira](https://github.com/mortinger91/michelebira) - [bira](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/bira.zsh-theme) 主题的变体。包括“git”状态、用户名、当前目录和最后一个命令运行的返回码的装饰器。
- [midin](https://github.com/xlshiz/midin) - 在深色终端背景上运行良好，包括“git”状态装饰。
- [mike-was-here](https://github.com/leguim-repo/mike-was-here-theme/) - 极简主义，包括“git”状态装饰。
- [milight](https://github.com/frodoslaw/milight-zsh) - 带有“git”状态显示的最小 ZSH 提示，最适合深色终端背景。
- [mindful-space](https://github.com/syndbg/mindful-space-zsh-theme) - ZSH 主题考虑到空间。
- [minima](https://github.com/Brolly0204/zsh-minima) - 包括 `git`、`node`、`golang`、`yarn`、`php`、`docker` 和 `python` 状态装饰。
- [minimal (glsorre)](https://github.com/glsorre/minimal/) - 一个最小的异步 ZSH 主题，优化用于 [Fira Code](https://github.com/tonsky/FiraCode) 字体和 [Solarized Light](https://ethanschoonover.com/solarized) 终端主题。
- [minimal (subnixr)](https://github.com/subnixr/minimal) - 最小但功能丰富的主题。
- [minimal-improved](https://github.com/gdsrosa/minimal_improved) - 黑暗终端的主题，包括右侧提示中的“git”装饰。
- [minimal-os](https://github.com/nkurata/zsh-theme) - 带有有用的“git”状态和特定于系统的装饰器的极简提示。
- [minimal-terminal](https://github.com/Lissy93/minimal-terminal-prompt) - 包括用户名@主机、当前目录、`git`信息和最后一个命令的退出代码的装饰器。
- [minimal2](https://github.com/PatTheMav/minimal2) - 一个最小且可扩展的 ZSH 主题。从 [subnixr 的原始版本](https://github.com/subnixr/minimal) 分叉并改编为 [Zimfw](https://github.com/zimfw/zimfw)。
- [minimalx](https://github.com/lknix/zsh-theme-minimalx) - 灵感来自 oh-my-zsh 的 kolo 主题。
- [mint](https://github.com/FalconLee1011/mint-zsh-theme) - 包括当前目录的装饰器（无论是在笔记本电脑还是台式机上运行）以及“git”状态。
- [mira](https://github.com/mbStavola/mira) - 修改后的 [bira](https://github.com/ohmyzsh/ohmyzsh/wiki/Themes#bira) 包含时间信息和简化的启动提示。
- [mirage](https://github.com/robin-pfeiffer/ohmyzsh-mirage-theme/) - 包括“git”状态、最后一个命令退出代码、“sudo”时间戳文件是否存在以及当前活动的 Python 虚拟环境的提示装饰。
- [miramare](https://github.com/franbach/oh-my-deepin-miramare) - 包括 `git` 状态装饰。与[深度终端](https://www.deepin.org/en/original/deepin-terminal/)配合使用效果最佳。
- [misa](https://github.com/misalabs/misa.zsh-theme) - Misalabs 的 ZSH 主题。
- [mixed](https://github.com/dekermendzhy/mixed-zsh-theme) - 针对深色背景进行了优化。
- [mnml](https://github.com/mnml-theme/prompt) - 带有“git”状态装饰的最小主题。
- [mocha-fusion](https://github.com/saeed0xf/mocha-fusion) - 基于 [catpuccin](https://catppuccin.com/)。包括 `git`、当前目录和 username@host 装饰器。
- [mochi](https://github.com/mochidaz/zsh-themes) - 简单的主题，设计类似于 Rust 主要功能。包括 `git` 和 `hg` 状态装饰。
- [mochi2](https://github.com/mochidaz/zsh-themes) - 极简主义主题。包括 `git` 和 `hg` 状态装饰。
- [modern](https://github.com/BadRat-in/zsh-modern-theme) - 自动适应浅色和深色终端主题。该主题提供了干净且信息丰富的提示，包括 git 集成、命令执行时间和漂亮的彩虹目录路径。
- [moderno](https://github.com/obrassard/moderno-zsh) - 一个简单而现代的 ZSH 主题，灵感来自 Oh-My-ZSH 的 [robbyrussell](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/robbyrussell.zsh-theme) 主题。包括 `git` 状态装饰。
- [modesty](https://github.com/saravanabalagi/zsh-theme-modesty) - 一个干净而朴素的 ZSH 主题，其中“condaenv”、“virtualenv”和“git”状态装饰整齐地右对齐显示。需要 [condaenv](https://github.com/saravanabalagi/zsh-plugin-condaenv) 插件。
- [molokai-powerline](https://github.com/prikhi/molokai-powerline-zsh) - 基于[agnoster](https://gist.github.com/agnoster/3712874)。
- [momoyo](https://github.com/momoyo-droid/momoyo-zsh-theme) - 让人想起电力线。包括“git”状态、用户名和工作目录的装饰。
- [monsi](https://github.com/rafa-wine/monsi_oh-my-zsh_theme) - 包括 `git` 状态、最后一个命令退出状态和当前目录装饰器。
- [moon-lite](https://github.com/anotherlusitano/moon-light) - 极简主义者。包括“git”状态、当前目录和最后一个命令运行的退出状态的装饰器。
- [moonbloom](https://github.com/moonbloom-theme/zsh) - 适应终端模拟器的配色方案。包括当前目录和“git”状态的装饰器。
- [moonline](https://github.com/kagamilove0707/moonline.zsh) - 最小但易于扩展的提示。
- [moux](https://github.com/gagbo/moux) - 与深色终端背景配合良好，包括“RPROMPT”中的“git”装饰。
- [msys2](https://github.com/water-logger/MSYS2-Theme/) - 受到 MSYS2 的启发。包括 user@host、`git` 状态和当前目录的装饰器。
- [mu](https://github.com/seamile/mu-zsh-theme) - 改进了多个“git”状态的显示。受到 [lambda mod 主题](https://github.com/halfo/lambda-mod-zsh-theme) 的启发。需要与电力线兼容的字体。
- [multi-shell-repo-prompt](https://github.com/dotcode/multi-shell-repo-prompt) - 提供有关您所在存储库的有用信息（在提示中）。它目前适用于 [ZSH](https://en.wikipedia.org/wiki/Zsh) 下的 [Git](https://git-scm.com/) 和 [Mercurial](https://www.mercurial-scm.org/) 以及 [bash](https://en.wikipedia.org/wiki/Bash_%28Unix_shell%29)。
- [multiline](https://github.com/jan-auer/zsh-multiline) - 基于 [agnoster](https://github.com/agnoster/agnoster-zsh-theme) 的电力线风格主题。
- [muslim](https://github.com/nksoff/muslim) - 一个简单的最小 ZSH 提示主题。
- [musy](https://github.com/tonyke-bot/musy-zsh-theme) - 受到缪斯主题的启发。包括 `git` 状态装饰。
- [my](https://github.com/fabiendelpierre/my-zsh-theme/) - [kolo] 的变体(https://github.com/ohmyzsh/ohmyzsh/wiki/Themes#kolo)。
- [myzsh](https://github.com/MaxUlysse/myzsh) - Maxime Garcia 的 myzsh 主题。
- [mzt](https://github.com/honbey/mzt) - 设置“LS_COLORS”，为“diff”着色并包括“git”状态和当前工作目录装饰。
- [nablaman](https://github.com/kokkonisd/nablaman-zsh-theme) - 类似于 [powerlevel10k](https://github.com/romkatv/powerlevel10k)。包括最后一个命令的退出状态、user@hostname、`git` 状态和当前目录的装饰器。最适合深色终端主题。
- [nanika](https://github.com/justforuse/nanika-zsh-theme/) - [robbyrussell](https://github.com/ohmyzsh/ohmyzsh/wiki/Themes#robbyrussell) 的优化变体。包括 `git` 状态装饰。
- [nanofish](https://github.com/tweekmonster/nanofish) - 向纳米技术主题添加鱼式目录提示。
- [nbrylevv](https://github.com/nbrylevv/nbrylevv-zsh-theme) - 带有文本“git”状态装饰的简约主题。
- [nctu](https://github.com/leovincentseles/nctu.zsh-theme) - 轻量级主题，强调速度。包括 `git` 状态装饰。
- [neewbie](https://github.com/neewbee/neewbee.zsh-theme) - 带有“git”装饰的最小主题。基于 [robbyrussell](https://github.com/ohmyzsh/ohmyzsh/wiki/Themes#robbyrussell)。
- [neo++](https://gitlab.com/migoa/neo) - 比上面的更简单、更直观、更少集群。
- [neon-potato](https://github.com/algosuna/neon-potato) - 色彩缤纷且简约的主题。包括 `git` 装饰。
- [neon](https://github.com/sahariko/neon) - 一个漂亮且简约的 ZSH 主题，带有“git”装饰。
- [nerdish](https://gitlab.com/nyarla/zsh-theme-nerdish) - ZSH 的提示主题，使用 [Nerd Fonts](https://github.com/ryanoasis/nerd-fonts)。
- [nerdp](https://github.com/joknarf/nerdp) - 书呆子电力线风格的提示。需要 [Nerd 字体](https://github.com/ryanoasis/nerd-fonts)。包括 `git` 状态、用户名@主机名、当前目录、Python virtualenv、文件系统使用情况检查、1 分钟 CPU 负载、可用内存和时间的装饰器。
- [nerdps1](https://github.com/joknarf/nerdps1) - 让人想起电力线。需要 [Nerd 字体](https://github.com/ryanoasis/nerd-fonts)。包括 user@hostname、`git` 信息、截断的当前目录、python virtualenv、最后一个命令运行的退出状态和时间的装饰器。
- [nescalante](https://github.com/nescalante/zsh-theme) - 针对深色终端背景进行了优化，包括“git”装饰。
- [netmask](https://github.com/swomf/netmask-zsh-theme) - Termux-first 主题。包括 ip 地址、当前目录的完整路径、`git` 状态和 python 虚拟环境的装饰器。
- [neurosimple](https://github.com/davidsierradz/neurosimple-oh-my-zsh-theme) - 包括 `git` 装饰和 `vi` 模式指示器。
- [newt](https://github.com/softmoth/zsh-prompt-newt) - 胖而快的主题——由内而外都很漂亮，风格片段做得恰到好处。高度可定制，包括“git”、用户名、执行时间、目录、后台作业和编辑模式装饰。
- [newton](https://github.com/sebastienfilion/zsh.newton) - 包括 `git` 状态和外部 IP 地址修饰。
- [nextbike](https://github.com/meierjan/nextbike-zsh-theme) - 一个非常基本的主题，仅具有 macOS 自行车图标。
- [nidoranarion](https://git.sr.ht/~nicolairuckel/nidoranarion) - 色彩缤纷，显示“git”状态装饰。
- [nikitakot](https://github.com/nikitakot/nikitakot-oh-my-zsh-theme) - 小而简单的 oh-my-zsh 主题。显示当前目录和后面的 2 个目录，`git` 和 `nodejs` 状态装饰。
- [ninik](https://github.com/NimaNikfar/ninik-zsh-theme) - 受到 [agnoster](https://github.com/agnoster/agnoster-zsh-theme) 和 [ubunly](https://github.com/alejandromume/ubunly-zsh-theme) 的启发。包括操作系统、当前目录、python virtualenv 和 `git` 状态的装饰器。需要 [Nerd Font](https://github.com/ryanoasis/nerd-fonts) 或 Powerline 修补字体。
- [niotna](https://github.com/niotna/niotna-theme) - 包括“git”状态和当前目录的装饰器。可定制的颜色。
- [nknu](https://github.com/aanc/oh-my-zsh-nknu-theme) - 一个简单的 oh-my-zsh 主题。
- [nmaxcom](https://github.com/nmaxcom/nmaxcom-zsh-theme) - 带有“git”状态装饰的极简 ZSH 主题。
- [node](https://github.com/skuridin/oh-my-zsh-node-theme) - oh-my-zsh 的 Node.js 主题经过改进，可以更轻松地与其他插件管理器一起使用。
- [nodeys](https://github.com/marszall87/nodeys-zsh-theme) - 基于 ys 主题，添加了 Node.js 版本（来自 NVM 插件）。
- [noon](https://github.com/silky/noon.zsh-theme) - 有浅色和深色两种变体，显示“git”信息。
- [nord](https://github.com/TyWR/Nord-zsh) - 包括 `git` 状态装饰并显示活动的 conda 环境。
- [normanius](https://github.com/normanius/normanius-zsh-theme) - 源自[bira](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/bira.zsh-theme)。包括 `git` status、`user@host`、python `virtualenv` 和 ruby​​ `rvm` 版本的装饰器。
- [nothing](https://github.com/eendroroy/nothing) - 快如闪电，而且非常简单，因为它几乎什么都没有。
- [nova](https://github.com/body20002/nova) - 包括 `git` 状态装饰。覆盖`LS_COLORS`和`LSCOLORS`设置。
- [nox](https://github.com/kbrsh/nox) - 深色主题，显示当前工作目录和 git 状态。
- [nt9](https://github.com/lenguyenthanh/nt9-oh-my-zsh-theme) - 一个干净、无干扰且以“git”为中心的开发主题。显示相对于 `git` 根的路径（或在 `git` 存储库之外时为 `~`）、自上次提交以来的时间、当前 SHA、分支和分支状态。
- [nunorc](https://github.com/nunorc/nunorc.zsh-theme) - 极简主义主题，在深色背景上效果很好。包括 `git`、`mercurial` 和 `svn` satus 装饰。
- [nuqle](https://github.com/Nuqlear/nuqlezsh.zsh-theme) - prezto 和 oh-my-zsh 的简单主题。
- [nuts](https://github.com/rafaelsq/nuts.zsh-theme) - 极简主题，包括“git”状态装饰和时间。
- [oblong](https://github.com/Ansimorph/oblong) - 基于 [gitster](https://github.com/shashankmehta/dotfiles/blob/master/thesetup/zsh/.oh-my-zsh/custom/themes/gitster.zsh-theme) 和 [basher](https://gitlab.com/Spriithy/basher) 的简单“bash”主题。包括状态装饰以显示用户是否为 root、上次运行命令的退出状态、“git”分支及其干净/脏状态。
- [odie](https://github.com/masterodie/zsh-theme-odie/) - 在深色背景上效果很好。包括 `git` status、python virtualenv 和 `vi`-mode 状态装饰。
- [odin](https://github.com/tylerreckart/odin) - Odin 是一个“git”风格的 ZSH 主题。
- [odra](https://github.com/ErikBenavides/odra.zsh-theme) - 色彩鲜艳，在深色背景上效果很好。包括“git”状态、当前目录、用户名和最后一个命令的退出状态的装饰器。
- [oh-flowers](https://github.com/Flower7C3/oh-flowers-zsh-theme) - 带有“git”装饰的多行主题。
- [oh-my-git](https://github.com/arialdomartini/oh-my-git) - bash 和 ZSH 的固执己见的提示。
- [oh-my-posh](https://ohmyposh.dev/) - 不是 ZSH 特定的，但非常好并且可以与 ZSH 一起使用。允许您在所有 shell 中对提示使用相同的配置。
- [oh-my-via](https://github.com/badouralix/oh-my-via) - ZSH 主题主要是对 VIA 服务器上使用的历史主题进行分叉。
- [ohelm](https://github.com/devopsguy/ohelm-zsh-theme) - 包括当前目录的装饰器、“git”状态、最后一个命令的退出和“kubectl”上下文。
- [ohh IP](https://github.com/Ohh-Raven/ohh_IP) - 专为 CTF 设计的主题。包括 IP 地址和“git”状态的装饰器。
- [ohmypc](https://github.com/joselpadronc/OhMyPC) - 适用于深色终端窗口。包括 `git` 装饰。
- [om](https://github.com/sirshikher/zsh-om) - 最小主题，适用于深色背景，包括“git”状态装饰。
- [omszt](https://github.com/MU001999/omszt) - 带有“git”装饰的简约主题。
- [omuse](https://github.com/ouuan/omuse-zsh-theme) - 基于 Oh-My-ZSH 的 [amuse](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/amuse.zsh-theme)。具有“git”状态、时间、绝对密码、RAM 使用情况、最后一个命令使用的时间和最后一个命令退出状态的装饰。
- [ooh-matron](https://github.com/hulleyrob/ohmyzsh-theme-ooh-matron) - 使用装饰器实时提示最后一个命令的退出状态、用户名@主机名、IP 地址和“git”状态。
- [operator](https://github.com/nivv/operator-theme) - 干净简单的主题，与 [Menlo for Powerline](https://github.com/abertsch/Menlo-for-Powerline) 配合使用效果最佳。
- [ortiz (andres-ortizl)](https://github.com/andres-ortizl/ortiz-zsh-theme) - [eriner](https://github.com/zimfw/eriner) 的分支，带有命令和 k8s 上下文之间间隔的装饰。
- [ortiz (guezwhoz)](https://github.com/guesswhozzz/guezwhoz-zsh-theme) - [eriner](https://github.com/zimfw/eriner) 的简化分支，带有 `git` 状态、`kubectl` 上下文和经过时间装饰。
- [osx2](https://github.com/RizkiIqbal02/zsh-theme-custom) - 基于建筑工艺。极简主义者。包括当前目录的装饰器。
- [otter](https://github.com/OtterArkar/otter-zsh/) - 以水獭为主题的主题，带有“git”状态、user@host 和当前目录装饰器。
- [owczarczak](https://github.com/ThemysciraData/owczarczak.zsh-theme) - 受到 bira、dieter 和 [fino-time](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/fino-time.zsh-theme) 的启发。包括 `venv` 和 vcs 状态装饰。
- [owi](https://github.com/owitech/zsh-theme/) - 带有“git”状态装饰的极简主题。
- [owiewestside](https://github.com/owenstranathan/owiewestside.zsh-theme) - 包括 `git` 状态和 virtualenv 信息。
- [oxide](https://github.com/dikiaap/dotfiles/blob/master/.oh-my-zsh/themes/oxide.zsh-theme) - 简约和黑暗的 ZSH 主题。
- [ozono](https://github.com/sfabrizio/ozono-zsh-theme) - 🌏 OZ0NO - 让我们呼吸干净的 ZSH。
- [p9k-theme-pastel](https://github.com/iboyperson/p9k-theme-pastel) - [powerlevel10k](https://github.com/romkatv/powerlevel10k) 提示的主题，强调简单性，同时仍能传达重要信息。
- [pacmandoh](https://github.com/pacmandoh/omz-theme-pacmandoh) - 使用时尚的主题增强您的命令行。包括“git”集成装饰器、权限反馈、Python 环境支持和动态提示，所有这些都可以通过单个安装脚本和可选样式进行自定义。
- [pad](https://github.com/eproxus/pad.zsh-theme) - 简洁且丰富多彩的 oh-my-zsh 主题。
- [page](https://github.com/SLIB53/page-zsh-theme) - 一个简单的主题，支持 VCS。提示符显示当前工作目录的 1 级、分支和颜色编码的弯曲粗箭头。
- [palenight (jenssegers)](https://github.com/jenssegers/palenight.zsh-theme) - 允许显示主机信息，包括“git”分支装饰。
- [palenight (rhklite)](https://github.com/rhklite/palenight_zsh_theme) - 在提示中用图标显示详细的“git”状态信息。
- [panda](https://github.com/davymai/oh-my-zsh-panda-theme) - 包括 `git` 和 `root` 状态装饰。最好在深色背景上。
- [papercolor](https://github.com/erikschreier/PaperColor-themes) - ZSH、`vim` 和 `tmux` 的配色方案。包括 `git` 状态装饰。
- [paramour](https://github.com/espeon/paramour) - 简单干净，有“git”状态、用户名、时间、当前目录和用户名的装饰器。您的终端中需要 [Nerd Font](https://github.com/ryanoasis/nerd-fonts)。
- [paroape](https://github.com/ParoaPe/ParoaPe-zsh-theme) - 基于[lpha3cho](https://github.com/sdcampbell/lpha3cho-Oh-My-Zsh-theme-for-pentesters)
- [parrot](https://github.com/trabdlkarim/parrot-zsh-theme) - 基于 Parrot OS bash 主题。包括 user@host 的装饰器、`git` 信息、最​​后一个命令的退出状态、时间和当前目录。
- [passion](https://github.com/ChesterYue/ohmyzsh-theme-passion) - 包括当前时间、“git”状态、最后一个命令运行时间（以毫秒为单位）以及最后一个命令的退出状态的装饰。 macOS 上需要 coreutils。
- [pastel](https://github.com/iboyperson/pastel) - 受 [sugar-free](https://github.com/cbrock/sugar-free) 启发的 ZSH 主题。包括 `git` 装饰。
- [paulmanjarres](https://github.com/paul-manjarres/paulmanjarres-zsh-theme) - 基于 [robbyrussell](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/robbyrussell.zsh-theme)、[agnoster](https://gist.github.com/agnoster/3712874) 和 [nuts](https://github.com/rafaelsq/nuts.zsh-theme)。包括当前目录、`git` 状态和时间的装饰器。
- [pawsh](https://github.com/SergioBonatto/pawsh-zsh-theme) - Pawsh 是 oh-my-zsh 的超级卡哇伊 zsh 主题，灵感来自日本 neko 文化。你的提示变成了一张可爱的猫脸（ᓚᘏᗢ），它会根据你的命令的心情改变颜色。包括根状态的装饰器、基于上次命令运行的退出状态的提示颜色变化、当前目录、Python virtualenv、vi 模式指示器、git 状态和当前时间。
- [paxton](https://github.com/p1xt4n/ohmyzsh-theme-paxton) - 受到电力线的启发。包括“git”分支、时间、最后一个命令退出状态和当前目录的段。需要与电力线兼容的字体。
- [pbdevflow](https://github.com/pbarovsky/pbdevflow) - 专为与 [Nerd Fonts](https://github.com/ryanoasis/nerd-fonts) 一起使用而设计和优化。包括当前目录、`git` 状态和用户名的装饰器。
- [pbsegments](https://github.com/pbarovsky/pbsegments) - [oh-my-zsh](https://github.com/ohmyzsh/ohmyzsh) 的最小且视觉上吸引人的自定义主题。它具有干净、基于分段的提示，并针对可读性和可用性进行了优化。包括“git”状态、当前目录和用户名的装饰器。
- [pecodez](https://github.com/pecodez/pecodez-zsh-theme) - 针对暗终端进行了优化。具有“snyk”版本、“node”版本、AWS 配置文件、kubernetes 上下文和“git”状态的装饰器。
- [pedantic](https://github.com/nemeshnorbert/pedantic-zsh-theme) - 可定制的颜色和输出。包括用于详细“git”信息、root 状态、最后一个命令的退出状态、user@host、当前目录和时间的装饰器。
- [pentest-report](https://github.com/sikumy/ohmy-pentest-report) - 专为渗透测试人员设计，提供干净高效的提示，以简化审计和渗透测试期间的日常任务。该主题包括用于实时显示日期、时间、IP 地址、当前目录和最后执行命令的结果的装饰器。
- [persi](https://github.com/persiliao/persi-zsh-theme) - 包括 `git`、主机名和当前目录装饰。适用于浅色和深色背景。
- [phalanx](https://github.com/d-danilov/phalanx-zsh-theme) - 本着 [robbyrussell](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/robbyrussell.zsh-theme) 和 Pure Shell 主题精神的最小主题。
- [phi φ](https://github.com/LasaleFamine/phi-zsh-theme) - 一个干净简单的 ZSH 主题，灵感来自于 [Lambda (Mod) ZSH](https://github.com/halfo/lambda-mod-zsh-theme) 主题。
- [pi](https://github.com/tobyjamesthomas/pi) - 带有“git”状态装饰的简约主题。
- [piboy](https://github.com/sflems/piboy-zsh-theme) - ZSH 简洁优雅的多行主题。包括彩色时间戳、“git”和语法突出显示以及提升的根主题。
- [pickaxe](https://github.com/mikhaben/pickaxe-zsh-theme) - 包括“user@host”、当前目录、当前时间、conda 环境、节点版本和“git”状态的装饰器。
- [pico](https://github.com/PicoGeyer/zsh-pico-prompt) - 从 [zap-prompt](https://github.com/zap-zsh/zap-prompt) 修改的简单提示，带有“git”信息、user@hostname 和工作目录的装饰器。
- [pifabs](https://github.com/pifabs/pifabs-zsh-theme) - 带有“git”状态、用户名、主机和工作目录装饰器的最小主题。
- [pixelwave](https://github.com/arcnms/pixelwave) - 时尚、明亮、充满活力的主题，将老式像素氛围与现代高色彩渲染融为一体。它显示了彩虹“像素条”、霓虹色身份线（来自 lolcat）、您的完整路径和简洁的“git”状态。
- [plain-ui](https://github.com/purveshpatel511/plain-ui) - 极简主义，但包括“git”状态装饰。
- [plain](https://github.com/jimeh/plain.zsh-theme) - ZSH 的一个简单明了的主题，显示基本的“git”信息。
- [planet](https://github.com/borb/planet-zsh) - 来自 [oh-my-zsh](https://github.com/ohmyzsh/ohmyzsh) 的 [steef](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/steeef.zsh-theme) 的精简版本。
- [plankton](https://github.com/tobiaseichert/plankton-zsh-theme) - 主题简单，没有多余的装饰。
- [plantyhoe](https://github.com/totoroot/plantyhoe.zsh-theme) - 基于对植物和苹果的热爱的极简主义主题。包括 `git` 状态装饰。
- [platypus](https://github.com/fdv/platypus) - Platypus 是 Frédéric de Villamil 使用的 oh-my-zsh 的一个简单方便的主题。
- [pog7x](https://github.com/pog7x/pog7x-zsh-theme) - 与 unicode 一起使用。包括“git”信息、当前目录、最后一个命令退出状态和执行时间、时间、virtualenv、nvm、rvm、rust、go、kubernetes context 和 elixir 的装饰器。
- [pointer](https://github.com/gpinkard/pointer-zsh-theme) - 显示工作目录、最后一个命令的返回状态以及“git”当前分支。
- [polyglot](https://github.com/agkozak/polyglot) - `zsh`、`bash`、`ksh93`、`mksh`、`pdksh`、`dash` 和 busybox `ash` 的动态提示，使用基本 ASCII 符号（和颜色，如果可能）来显示用户名，无论是本地还是远程 `ssh` 会话，缩写路径，`git` 分支和状态，最后一个命令的退出状态（如果非零），使用 `virtualenv` 创建的任何虚拟环境， `venv`、`pipenv`、`poetry` 或 `conda`。
- [poncho](https://github.com/RainyDayMedia/oh-my-zsh-poncho) - RDM 的基本 oh-my-zsh 自定义主题。
- [poor-programmer](https://github.com/vishaltelangre/poor-programmer.zsh-theme) - 程序员的主题，包含 `git` 状态、ruby 版本和项目路径。
- [power](https://github.com/snakypy/zshpower) - 针对 python 开发人员进行了优化。包括 `git` 和 `pyenv` 状态装饰、用户名和主机。尝试安装其他插件和字体，因此在安装之前请阅读其说明。
- [powerbash](https://github.com/erikschreier/powerbash-zsh) - 适用于深色终端背景，包括“git”状态装饰。
- [powerless](https://github.com/martinrotter/powerless) - 受电力线启发的微小而简单的纯 ZSH 提示符。
- [powerlevel10k](https://github.com/romkatv/powerlevel10k) - 快速重新实现 [powerlevel9k](https://github.com/bhilburn/powerlevel9k) ZSH 主题。可以用作 powerlevel9k 的直接替代品，当给出相同的配置选项时，它将生成相同的提示，只是速度更快。
- [powerlevel9k](https://github.com/bhilburn/powerlevel9k) - Powerlevel9k 是 ZSH 的主题，它使用 [Powerline Fonts](https://github.com/powerline/fonts)。它可以与普通 ZSH 或 ZSH 框架一起使用，例如 [Oh-My-Zsh](https://github.com/ohmyzsh/ohmyzsh)、[Prezto](https://github.com/sorin-ionescu/prezto)、[Antigen](https://github.com/zsh-users/antigen) 和 [许多其他](https://github.com/bhilburn/powerlevel9k/wiki/Install-Instructions)。
- [powerlevelHipstersmoothie](https://github.com/hipstersmoothie/PowerlevelHipstersmoothie) - [powerlevel9k](https://github.com/bhilburn/powerlevel9k) 的附加组件。
- [powerline (brucehsu)](https://github.com/brucehsu/oh-my-zsh-powerline-theme) - 电力线的两线版本：一根用于信息，一根用于输入。
- [powerline (jeremy)](https://github.com/jeremyFreeAgent/oh-my-zsh-powerline-theme) - 另一种电力线主题。可很好配置，但至少需要一个支持 256 色的终端，并具有与电力线兼容的终端字体。
- [powerline-cute](https://github.com/dogrocker/oh-my-zsh-powerline-cute-theme) - 基于 [bullet-train](https://github.com/caiogondim/bullet-train.zsh)。
- [powerline-go](https://github.com/justjanne/powerline-go) - 一个漂亮且有用的低延迟提示，用 golang 编写。包括 `git` 和 `hg` 状态装饰、最后一个命令运行的退出状态、当前的 Python virtualenv，无论您是否在 [nix](https://nixos.org/) shell 中，并且都很容易扩展。
- [powerline-hs](https://github.com/rdnetto/powerline-hs) - 用 Haskell 编写的 [Powerline](https://github.com/powerline/powerline) 克隆。它比原始实现要快得多，并且使 shell 的响应速度明显更快。
- [powerline-pills](https://github.com/lucasqueiroz/powerline-pills-zsh) - 用 Ruby 编写，使用电力线字符来模拟带有有用信息的药丸。
- [powerline-shell (b-ryan)](https://github.com/b-ryan/powerline-shell) - 漂亮且有用的 Bash、ZSH、Fish 和 tcsh 提示生成器。包括 `git`、`svn`、`fossil` 和 `hg` 装饰、Python virtualenv 信息和最后一个命令退出状态。
- [powerline-shell (banga)](https://github.com/b-ryan/powerline-shell) - Bash、ZSH 和 Fish 的类似于 [powerline](https://github.com/Lokaltog/vim-powerline) 的提示。包括 `git`/`svn`/`hg`/`fossil` 分支的装饰器、最后一个命令退出状态、当前目录和当前 python virtualenv 的缩短路径，并且易于自定义/扩展。
- [powerline-train](https://github.com/sherubthakur/powerline-train) - 电力线变体。
- [powerline](https://github.com/carlcarl/powerline-zsh) - 类似 [Powerline](https://github.com/Lokaltog/vim-powerline) 的提示，基于 [powerline-bash](https://github.com/milkbikis/powerline-bash)。显示 virtualenv、`git` 状态信息和最后运行命令的退出代码。
- [powermore](https://github.com/primejade/powermore-zsh) - 从 [powerless](https://github.com/martinrotter/powerless) 分叉。显示“git”状态和当前目录的简单提示。
- [powerzeesh](https://github.com/sevaho/Powerzeesh) - 基于 Powerline 的 ZSH 主题。它的目标是简单，仅在相关时显示信息，并针对速度和外观进行了优化。受到 [Agnoster](https://github.com/agnoster/agnoster-zsh-theme) 和 [Powerline](https://github.com/jeremyFreeAgent/oh-my-zsh-powerline-theme) 的启发。
- [pre](https://github.com/leandromatos/pre-theme) - Sublime Text、Terminal、iTerm 2 和 ZSH 主题的集合。
- [predawn-shell](https://github.com/jamiewilson/predawn-shell) - 针对深色终端主题优化的主题。
- [prezto_powerline](https://github.com/davidjrice/prezto_powerline) - prezto 的电源线。显示 git 信息、RVM 版本。
- [prezto-cloud-prompt](https://github.com/klaude/prezto-cloud-prompt) - oh-my-zsh 云提示符的 Prezto 端口。
- [prezto-lambda](https://github.com/nixolas1/prezto-lambda) - Lambda 主题（用于 prezto）。
- [princess](https://github.com/mellypop/princess) - 以 [abhiyan.zsh](https://github.com/abhiyandhakal/abhiyan.zsh) 为蓝本，粉红色可能有点太多，表情符号可能太少。包括当前目录和“git”状态的装饰器。
- [probe](https://github.com/probe2k/probe_zsh) - 包括 `git` 状态装饰。
- [prompt_blocks](https://github.com/MiloradFilipovic/promptblocks) - 一个最小的 Node js + git 主题。包括“git”状态、节点版本和当前目录的装饰器。
- [prompt_j2](https://github.com/malinoskj2/prompt_j2) - 具有动态退出状态指示器，可以动态更改为两行以显示上下文。
- [prompt-powerline](https://github.com/Valodim/zsh-prompt-powerline) - 一个相当重量级的 ZSH 提示符，基于流行的同名“vim”插件中的 powerline 字体，非常适合深色背景。
- [prompt](https://github.com/nathanblair/prompt) - 在“sh”、“dash”、“ash”、“zsh”和“pwsh”之间一致的轻量级提示。包括 `git` 状态装饰。
- [promptor](https://github.com/MickaelBlet/Promptor) - 受电力线启发。包括“git”状态、用户名、主机名、工作目录和时间的装饰器。
- [promptus](https://github.com/willeccles/promptus) - 用 C 编写的简单、简约且可配置的 shell 提示符程序可用于使您的提示符在任何 shell 上都相同。包括退出代码和工作目录装饰。
- [pronto (arzezak)](https://github.com/arzezak/pronto) - 一个超级简单的提示，带有当前目录和“git”信息的装饰器。
- [pronto (jthat)](https://github.com/jthat/zsh-pronto) - 简单快速的主题，带有“git”装饰和计时信息。
- [prowpt](https://github.com/alpaca-honke/prowpt) - 简单、轻量级、可定制的类似电力线的提示符，带有“git”信息、用户、主机名、当前目录、时间和最后一个命令的退出状态的装饰器。
- [ps1.py](https://github.com/jwodder/ps1.py) - 具有 `git` 状态、截断的目录、`chroot` 和 `virtualenv` 提示装饰。
- [pumpkane](https://github.com/ColinZeDev/pumpkane-oh-my-zsh-theme) - 一个现代、色彩丰富、信息丰富的主题，旨在提高清晰度、美观性和生产力。它具有动态颜色、“git”状态集成、基于时间的着色和可选的昵称显示
- [punctual](https://github.com/dannynimmo/punctual-zsh-theme) - 易于定制，受[spaceship](https://github.com/denysdovhan/spaceship-prompt)的影响。
- [pure-agnoster](https://github.com/yourfin/pure-agnoster) - [pure](https://github.com/sindresorhus/pure) 和 [agnoster](https://gist.github.com/3712874) 的混搭。具有“git”装饰，并且适用于深色和浅色终端背景。
- [pure](https://github.com/sindresorhus/pure) - 一个漂亮、最小且快速的 ZSH 提示符。包括“git”状态装饰、如果最后一个命令失败则提示变为红色、在远程会话或容器中时的用户名和主机装饰以及进程运行时的当前文件夹和命令。
- [purify (banminkyoz)](https://github.com/banminkyoz/purify) - 一个简单、快速、酷炫的提示。
- [purify (kyoz)](https://github.com/kyoz/purify) - 干净而充满活力的主题，最适合深色背景。包括 `git` 状态装饰。
- [purity](https://github.com/petermbenjamin/purity) - 受到 [robbyrussell](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/robbyrussell.zsh-theme) 主题和 [pure](https://github.com/sindresorhus/pure) 提示的启发。
- [purpleblood](https://github.com/HFMorais/oh-my-zsh-purpleblood-theme/) - 基于[darkblood](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/darkblood.zsh-theme)。包括 `username@host`、`git` status 和当前目录的装饰器。
- [purr](https://github.com/mubinben/purr-zsh-theme) - 包括当前目录和“git”状态的装饰器。
- [purs](https://github.com/xcambar/purs) - 一个用 [Rust](https://www.rust-lang.org/) 编写的快速 [pure](https://github.com/sindresorhus/pure) 启发的提示。
- [pustelto](https://github.com/Pustelto/shell_theme) - 多彩主题的灵感来自 [Spaceship](https://github.com/denysdovhan/spaceship-prompt) 主题，包括 `git` 装饰。
- [pwn](https://github.com/gh05t-4/pwn-theme) - 包括 user@host、`git` 和 `hg` 状态、ruby 版本、python virtualenv 和当前工作目录的装饰器。
- [pyhack](https://github.com/williamcanin/pyhack) - 与深色终端主题配合良好。显示Python版本、Python包版本（pyproject.toml）和`git`当前分支信息。
- [qi3ber2](https://github.com/nichus/qi3ber2) - 深色多行主题。包括 `git`、最后一个命令装饰器的平均负载和退出代码。
- [qoomon](https://github.com/qoomon/zsh-theme-qoomon) - 针对深色背景进行了优化，包括“git”信息。主题存储库包括 iTerm 2 和终端颜色设置。
- [quantum](https://github.com/calebephrem/quantum-zsh) - 时尚、动态的 ZSH 主题，专为速度、风格和 shell 至上而打造。无论您是深入使用 Git 还是只是在终端中进行操作，Quantum 都会适应您的流程。
- [quewui](https://github.com/kauefontes/oh-my-quewui) - 简单干净的主题针对深色终端主题进​​行了优化。包括当前时间、用户、目录和“git”状态的装饰。
- [quietline](https://github.com/qwreey/quietline) - 受标题主题启发的简单主题。包括 `git` 状态、user@host 和当前目录的装饰器。
- [r](https://github.com/rafalkaron/r-zsh-theme) - 一个简单但信息丰富的 ZSH 主题。
- [r3nic1e](https://github.com/r3nic1e/r3nic1e) - [Agnoster](https://github.com/agnoster/agnoster-zsh-theme) 变体，包含电池状态、`git/hg` 状态、时间、kubernetes 上下文和命名空间、最后命令的非零退出代码和日期装饰。需要 Powerline 字体。
- [rabbit](https://github.com/Hera-Moon/My-rabbit-Zsh-Theme) - 针对“git”进行了优化。需要一个支持 unicode 的终端程序。包括“git”状态、当前工作目录和当前虚拟环境的装饰器。
- [racotecnic](https://github.com/elboletaire/zsh-theme-racotecnic) - 基于 af-magic 和 posh-git。
- [radius](https://github.com/erikcc02/radius-zsh-theme) - 包括 `git` 状态、用户名、主机名和目录装饰，以及 [desk](https://github.com/jamesob/desk) 支持。
- [rafiki](https://github.com/akabiru/rafiki-zsh) - 将表情符号添加到您的 ZSH 终端。
- [ramiel](https://github.com/aknackd/zsh-themes) - [node](https://github.com/skuridin/oh-my-zsh-node-theme) 的分叉。
- [random-emoji-robbyrussell](https://github.com/parwatcodes/random-emoji-robbyrussell) - 基于 [random-emoji](https://gist.github.com/oshybystyi/2c30543cd48b2c9ecab0) 和 `robbyrussell` 主题。
- [random-emoji](https://gist.github.com/oshybystyi/2c30543cd48b2c9ecab0) - 随机表情符号。
- [raspberrysh](https://github.com/MaxMalinowski/raspberrysh) - 包括 `git`、python、时间、当前主机和路径装饰。
- [raytek](https://github.com/Raytek/raytek-zsh-theme) - 简单而丰富多彩的主题，带有“git”状态装饰。
- [raz](https://github.com/razman786/ohmyzsh-theme-raz) - 最小提示，包括“git”状态装饰。
- [rb](https://github.com/rberenguel/rb-zsh-theme) - 基于 [Agnoster](https://gist.github.com/agnoster/3712874) 的电力线风格主题，针对 `git` 和 Solarized 终端进行了优化。需要与电力线兼容的字体。
- [rbjorklin](https://github.com/rbjorklin/rbjorklin-zsh-theme) - 针对日光终端配色方案进行了优化，包括“git”状态装饰。
- [redfox](https://github.com/saeed0xf/terminal-themes) - 包括当前目录的装饰器和狐狸图标。
- [redline](https://github.com/DrissTM/redline.zsh-theme) - 极简主义主题。包括 `git` 状态、时间、用户。
- [refined-flower](https://github.com/idaMakelaWork/refined-flower) - 需要一个可以处理表情符号的终端程序。包括 `git` 状态装饰器。
- [reggae](https://github.com/nmercado1986/zsh-reggae-theme) - 使用颜色编码的状态装饰将大量信息压缩到提示中。
- [rei](https://github.com/arturoalviar/rei-zsh-theme) - A simple theme with the first character 零(rei), the number 0. Includes `git` status decorations.
- [remiii](https://github.com/Remiii/remiii.zsh-theme) - 基于[Agnoster](https://github.com/agnoster/agnoster-zsh-theme)，针对[solarized](https://github.com/altercation/solarized)终端主题进​​行了优化。
- [remolueoend](https://github.com/remolueoend/remolueoend.zsh-theme) - 基于 [Agnoster](https://github.com/agnoster/agnoster-zsh-theme)，使用表情符号来跟踪 `git` 上下文。仅适用于 [Prezto](https://github.com/sorin-ionescu/prezto)。
- [renanborgez](https://github.com/renanborgez/ohmyzsh-theme-renanborgez) - 在深色背景上效果很好。包括“nvm”和“git”信息的装饰器。
- [rho](https://github.com/andrii-rieznik/rho-zsh-theme) - 极简主义主题。包括“git”状态、主机名和当前目录的装饰器。
- [ribbon](https://github.com/pyjamafish/ribbon-prompt) - 让人想起电力线。包括 Python `virtualenv` 装饰器。
- [rie](https://github.com/andrii-rieznik/rie-zsh-theme) - 极简主题，带有用户名、“git”状态和当前目录的装饰器。
- [rigel](https://github.com/othiagos/rigel-zsh-theme/) - 包括“git”信息、user@hostname 和当前目录的装饰器。
- [rio](https://github.com/foxit64/zsh-theme-rio) - 极简主题，带有“git”状态和当前目录的装饰器。
- [risbow](https://github.com/waddupp00/risbow) - 受 [risto](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/risto.zsh-theme) 启发的 ZSH 主题具有类似彩虹效果的 lolcat。
- [ritz](https://github.com/Ritzier/ritz.zsh-theme) - 包括时间、当前目录、“git”状态、退出状态和上次命令运行时间的装饰器。
- [river](https://github.com/revir/river-zsh-config) - 带有“git”信息的深色主题。
- [rkj-logik](https://github.com/logik93/rkj-logik.zsh-theme) - 基于 omz 的 [rkj](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/rkj.zsh-theme)。包括 user@host、当前目录、时间和日期的装饰器。
- [rkj-with-conda](https://github.com/cain986/rkj-with-conda-zsh-theme) - 基于 omz 的 [rkj](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/rkj.zsh-theme) 并添加 conda 环境和 `git` 状态装饰器。
- [robbyolivier](https://github.com/YuyeQingshan/robbyolivier) - 基于 [robbyrussell](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/robbyrussell.zsh-theme) 主题和 [zsh-git-prompt](https://github.com/olivierverdier/zsh-git-prompt) 项目的想法。
- [robbyrussell-fullpath](https://github.com/toytag/robbyrussell-fullpath.zsh-theme) - 原始的 [robbyrussell](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/robbyrussell.zsh-theme) 在提示中带有完整路径。
- [robbyrussell-plus](https://github.com/jackjyq/robbyrussell-plus-zsh-theme) - 基于 [robbyrussell](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/robbyrussell.zsh-theme)，添加主机名装饰器。
- [robbyrussell-WIP](https://github.com/ecbrodie/robbyrussell-WIP-theme) - 用输出装饰 `robbyrussell` 主题以指示 **WIP** 提交。
- [rocket](https://github.com/Alexandresl/rocket-zsh-theme) - 极简主题，包括 `git` 和 `hg` 状态装饰。
- [rougarou](https://github.com/RougarouTheme/rougarou-zsh) - 一个黑暗的主题。
- [rounded](https://github.com/daniilty/rounded-zsh-theme) - 包括当前目录和“git”状态装饰。
- [roundy](https://github.com/nullxception/roundy) - 快速、可爱、圆润的主题。包括“git”状态、当前目录和上次命令执行时间的装饰器。需要 [Nerd Font](https://github.com/ryanoasis/nerd-fonts) 和支持 unicode 的终端应用程序。
- [rs](https://github.com/sam-621/rs-zsh-theme) - 包括 `git` 装饰。需要支持 unicode 的终端。
- [rufus](https://github.com/runarsf/rufus-zsh-theme) - 针对深色背景进行了优化。
- [rummik](https://github.com/rummik/zsh-theme) - @rummik 的主题。支持 [psmin](https://gitlab.com/zick.kim/zsh/zsh-psmin)，以及提示中的 `git` 状态信息。
- [russtone](https://github.com/russtone/prompt-russtone) - 受到 [pure](https://github.com/sindresorhus/pure) 和 [sorin](https://github.com/sorin-ionescu/prezto) 的启发。包括 `git` 状态装饰。
- [ruweird](https://github.com/ruweird/ruweird.zsh-theme) - 极简主义者。有“git”状态和当前目录的装饰器。显示带有雨滴的雨伞，如果非零，则显示最后一个命令的退出代码。
- [rwahasugui](https://github.com/rafawhs/rwahasugui.zsh-theme/) - 包括“git”信息、当前时间、当前工作目录和活动 python virtualenv 的装饰器。
- [ryner](https://github.com/DoctorRyner/ryner-zsh-theme) - 丰富多彩的主题，包括`git`装饰和当前目录。
- [rzh](https://github.com/patwhatev/rzh) - 带有“git”状态的主题由表情符号表示。
- [s1ck3r](https://github.com/pseifer/s1ck3r) - 时尚、瞬态且节省空间。包括“vi”模式的装饰器、提升的权限、最后一个命令退出状态、后台作业是否正在运行、工作目录和“git”状态，
- [s1ck94](https://github.com/zimfw/s1ck94) - S1cK94 的最小提示符（第一个已弃用，现已消失）的分支。显示用户是否为 root、后台作业状态、vi 模式、最后一个命令的退出状态以及 `git` 状态装饰。
- [s7c](https://github.com/Samega7Cattac/s7c.zsh-theme) - 适合深色背景。包括 `git` 状态装饰。
- [sailormoon](https://github.com/Domanowska/zshSailorMoonThemes) - 美少女战士主题的集合。
- [samshell](https://github.com/samuelb/samshell) - 一个极简主义的 ZSH 主题，带有 `git`、kubernetes 和 python virtualenv 装饰。
- [saraiva](https://github.com/ruisaraiva19/saraiva-theme) - 包括“git”状态装饰，在黑暗的终端背景上运行良好。
- [sashimi](https://github.com/simonmader17/sashimi-zsh-theme) - 包括“git”状态和最后一个命令运行的退出状态的装饰器。
- [saturn](https://github.com/gantoreno/saturn-prompt) - 为那些热爱空间并希望在终端上拥有一些空间的人提供柔和简约的提示，具有炫酷的表情符号和高度可定制的提示元素（例如图标、颜色、时间格式等）。
- [savior](https://github.com/Savecoders/Savior-zsh-theme) - 极简主题，带有当前目录的装饰器、上次命令运行的退出状态和“git”状态。
- [schminitz-v2](https://github.com/mashdots/schminitz-v2) - 显示 `git` 状态、`user@host` 信息、最​​后一个命令的退出状态以及是否以 root 身份运行的装饰器。
- [schminitz](https://gist.github.com/schminitz/9931af23bbb59e772eec) - 显示使用 `:sh` 命令时 `vim` 是否在后台运行。
- [scythe](https://github.com/kostoskistefan/scythe) - 让人想起电力线的主题。包括 `git`、最后一个命令退出状态和目录装饰。
- [sdt](https://github.com/sdlea/omz-theme-sdt) - 包括当前目录和“git”状态的装饰器。
- [searocket](https://github.com/dk949/searocket/) - [spaceship](https://github.com/denysdovhan/spaceship-prompt)的精简版。包括工作目录、最后一个命令退出代码、用户、后台作业、`bun`、`d`、elm、go、nodejs、python、zig 和 `git` 状态的装饰器。需要“D”构建链。
- [seashell](https://github.com/jottenlips/seasonal-zshthemes) - 简约主题，带有海洋风格的表情符号装饰。包括 `git` 状态装饰。
- [seeker](https://github.com/tonyseek/oh-my-zsh-seeker-theme) - 这个主题使用了很多特殊的unicode字符来显得花哨，但是如果没有很好支持的字体，它可能会导致一些问题。
- [seltzer](https://github.com/GrantSeltzer/seltzer.zsh-theme) - 受节食者主题的启发，使用颜色编码来提供信息。
- [senpai](https://github.com/hiroru/senpai-zsh) - DevOps 的干净提示主题。包括“git”状态、kubernetes 上下文、AWS 配置文件、GCP 项目和 Azure 活动云的装饰器。
- [sensa](https://github.com/miccou/sensa-theme) - 包括“git”状态、GitHub 用户名和当前目录的装饰器。
- [sentinelx](https://github.com/Robinx0/sentinelX-theme) - 轻量级、高保真 Zsh 主题，针对渗透测试和红队进行了优化。它为长期运行的安全工具提供实时态势感知和流程跟踪。包括“git”状态的装饰器、实时进程微调器、VPN 状态、根状态和最后命令持续时间。
- [sepshell](https://github.com/sepehr/sepshell) - 基于旧的丢失的 taybalt 主题的干净且最小的 ZSH 主题，具有“git”二分/合并/变基模式和可配置的提示符号。
- [serenity](https://github.com/ars2062/serenity-zsh-theme) - 极简主义主题，在命令行上方的柔和颜色框中显示基本的上下文信息，使用 Unicode 分隔符保持干净而富有表现力。包括 root 状态、用户名、主机名、主机 IP 地址、`git` 状态和当前目录的装饰器。
- [seti_UX](https://github.com/ginfuru/iTerm-Seti_UX) - 一个简单的 oh-my-zsh 兼容主题，具有相应的 iTerm 2 配色方案。
- [sfz](https://github.com/mreinhardt/sfz-prompt.zsh) - 精益提示的演变，其本身就是纯粹的重写。
- [shades of purple](https://github.com/nmcc1212/shades-of-purple-windows-terminal/) - Windows 终端的紫色主题让人想起 [powerline](https://github.com/jeremyFreeAgent/oh-my-zsh-powerline-theme)。
- [shadow](https://github.com/agentshadow/shadow-zsh-theme) - 包括 `git` 状态、目录、主机名、用户名和时间装饰。
- [shayan](https://github.com/shayanh/shayan-zsh-theme) - 带有“git”状态装饰的简单主题。
- [shelby](https://github.com/athul/shelby) - 用纯“golang”编写的快速、轻量级和最小的提示。包括最后一个命令退出状态、“git”状态和当前工作目录的装饰。
- [shellder](https://github.com/simnalamburt/shellder) - 带有“git”分支装饰器的最小主题。需要与电力线兼容的字体。
- [shichi](https://github.com/arturoalviar/shichi-zsh-theme) - A simple theme with the first character being 七(shichi/nana), the number 7. The primary color is red with a yellow accent. Includes `git` status decorations.
- [shiftys](https://github.com/shifty0g/shiftys-zsh-theme/) - kali 主题的调整版本。
- [shiko](https://github.com/regarager/shiko-prompt) - 带有装饰器的简约提示，用于获取 VCS 信息和当前目录。
- [shini](https://github.com/bashelled/shini) - 一个小小的主题，只是喊出很小的声音。包括目录、用户名、主机名、时间和“git”装饰。
- [shinkansen](https://github.com/MRZ07/shinkansen.zsh-theme) - 快速、可定制且易于扩展的主题。包括活动 virtualenv 中 python 版本的装饰器、当前 ruby​​ 版本（如果您使用的是 `chruby`）、当前 Node.js 版本、当前 java 版本、当前 go 版本、当前 perl 版本（如果使用 `chperl`）、当前 elixir 版本、`git` 状态、时间、当前目录、最后一个命令的退出代码和执行时间以及可选的自定义消息。需要与电力线兼容的字体。
- [shirnschall](https://github.com/shirnschall/shirnschall-zsh-theme) - 包括 `git` status 和 `user@hostname` 装饰。
- [shiro (arturDobrowolski)](https://github.com/ArturDobrowolski/shiro-zsh-theme) - 包括当前目录、“git”状态、退出状态和上次命令运行的执行时间的装饰器。
- [shiro (shirozuki)](https://github.com/shirozuki/shiro-zsh-theme) - 包括当前目录的装饰器、“git”状态以及上次命令运行的执行时间和退出状态。
- [shocm](https://github.com/ericvanjohnson/shocm-zsh-themes) - 从 [sixlive](https://github.com/sixlive/sixlive-zsh-theme) 分叉。有“git”装饰。
- [short-ys](https://github.com/OREOmini/short-ys-zsh-theme) - 基于 [ys](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/ys.zsh-theme) 主题。包括 `git` 和 `hg` 状态装饰。
- [shrikant](https://github.com/shr1k4nt/shrikant_zsh_theme) - 包括 `git` 装饰。
- [shrug](https://github.com/to-var/shrug-zsh-theme) - 受到 [beer-theme](https://github.com/tcnksm/oh-my-zsh-beer-theme) 的启发，包括 `git` 状态和当前目录装饰。
- [shuttle](https://github.com/Pandademic/Shuttle/) - 用“golang”编写。具有操作系统、用户、当前目录和最后一个命令运行的退出代码的装饰器。
- [siegerts](https://github.com/siegerts/zsh-theme) - 在正确的提示符中包含 `git` 状态装饰。
- [silver](https://github.com/reujab/silver) - 一个跨 shell 可定制的类似电力线的提示符，很大程度上受到 [Agnoster](https://github.com/agnoster/agnoster-zsh-theme) 的启发。更快的 [bronze](https://github.com/reujab/bronze) 的 Rust 端口。需要 [书呆子字体](https://github.com/ryanoasis/nerd-fonts)。非常可配置，包括“git”状态装饰。
- [simpalt](https://github.com/m-lima/simpalt) - 基于 [Agnoster](https://github.com/agnoster/agnoster-zsh-theme) 的信息丰富的小型主题。
- [simpl](https://github.com/MrNeoTr1n0/simplzshell) - 极简主义主题注重优雅和简约。用于根状态、当前目录和“git”状态的装饰器。
- [simple (drNoob13)](https://github.com/drNoob13/SimpleZshTheme/) - 包括 python 虚拟环境、`git` 状态和当前目录的装饰器。
- [simple (pavdmyt)](https://github.com/pavdmyt/simple-oh-my-zsh-theme) - 基于 [robbyrussel](https://github.com/ohmyzsh/ohmyzsh/wiki/Themes#robbyrussell) 的极简主题，在 iTerm 的窗口标题栏中嵌入 `git` 状态信息，而不是在提示中使用空格。
- [simple (rkitover)](https://github.com/rkitover/sh-prompt-simple) - 一个简单、轻量且美观的提示符，即使在 MSYS2、Cygwin 和 WSL 等非常慢的 shell 中也能快速运行。它显示当前环境（发行版、操作系统等）短名称的装饰、“git”签出时的“git”分支，以及最后一个命令的退出状态（绿色复选标记表示成功，红色 X 标记表示非零退出）。
- [simple (savecoders)](https://github.com/Savecoders/simpleTheme-zsh-theme) - 简单简约的主题，带有“git”、“用户名”和执行状态装饰。
- [simple (tourcoder)](https://github.com/tourcoder/simple.zsh-theme) - 极简提示，包括“git”状态装饰。
- [simple (yhiraki)](https://github.com/yhiraki/zsh-simple-prompt) - 最少的提示，不需要特殊字体。
- [simple-agnoster](https://github.com/iwat/simple-agnoster.zsh-theme) - 受电力线启发的简单主题，带有“git”装饰。
- [simple-chack](https://github.com/chack93/simple-chack.zsh-theme) - 与日光终端配色方案配合良好。包括 `git` 状态装饰。
- [simple-git](https://github.com/BazaJayGee66/simple-git-theme) - 极简主题的灵感来自 [gitstatus](https://github.com/kimyvgy/gitstatus-zsh-theme)。包括 `git` 装饰。
- [simple-headless](https://github.com/H3xaChad/zsh-simple-headless-theme) - 最小的纯 ASCII 提示，仅显示您需要的内容。包括用于缩短当前目录路径的装饰器、Python 虚拟环境、节点版本、用户名@主机名和“git”信息。
- [simple-yet-beautiful](https://github.com/mathiasmoeller/simple-yet-beautiful-zsh-theme) - 极简主义主题。包括`git`状态和`user@host`提示装饰。
- [simple-zsh-catppuccin](https://github.com/ezswan/simple-zsh-catppuccin) - 基于 [Catppuccin Mocha](https://catppuccin.com/) 配色方案，改编自 [Dracula](https://github.com/dracula/zsh) 主题基础。该主题具有简单且实用的提示，支持 git 状态、时间显示、上下文和目录信息，并通过 ezswan 发现的十六进制颜色支持进行了增强。
- [simplezsh](https://github.com/fr0zn/simplezsh) - 具有“git”信息显示的最小主题。
- [simply-perfect](https://github.com/SetOfAllSets/simply-perfect-zsh-theme/) - 让人想起电力线和子弹头列车。包括“git”状态、当前目录、最后一个命令退出状态、当前时间和用户名的装饰器。
- [sinon](https://github.com/k-kinzal/oh-my-zsh-sinon-theme) - k-kinzal 的 sinon 主题。包括 `git` 状态装饰。
- [sit](https://github.com/svensen/sit.zsh-theme) - 带有“git”的极简主题，最后一个命令退出状态和路径装饰。
- [sixlive](https://github.com/sixlive/sixlive-zsh-theme) - 该主题有一个独特的目录列表。在“git”项目内部时，目录显示的范围仅限于当前存储库根目录。
- [sk9](https://github.com/skeiter9/sk9-zsh) - Skeiter9 的 ZSH 主题。
- [skeletor-syntax](https://github.com/ramonmcros/skeletor-syntax) - Atom、Prism 和 ZSH 主题系列的灵感来自《He-Man and the Masters of the Universe》中的 Skeletor。
- [skiff](https://github.com/xiaoshihou514/skiff) - 具有“git”状态和当前目录装饰器的轻量级 ZSH 主题。
- [skill (asafaeirad)](https://github.com/ASafaeirad/oh-my-zsh-skill-theme) - 包括工作目录、“git”工作分支、工作目录状态和跟踪分支状态的装饰。
- [skill (frontendmonster)](https://github.com/frontendmonster/oh-my-zsh-skill-theme) - 针对黑暗终端进行了优化，显示“git”状态装饰。
- [skondrashov](https://github.com/sergkondr/skondrashov-zsh-theme) - 极简主义者。包括“git”状态、当前 kubernetes 上下文和当前 AWS 配置文件的装饰器。
- [skull](https://github.com/tahadostifam/skull-zsh) - 包括 `git` 状态、python 虚拟环境和 ruby​​ `rvm` 状态装饰。
- [sleeplessmind](https://github.com/godbout/sleeplessmind-zsh-theme) - ZSH 主题的灵感来自 [gitster](https://github.com/shashankmehta/dotfiles/blob/master/thesetup/zsh/.oh-my-zsh/custom/themes/gitster.zsh-theme) 和 [odin](https://github.com/tylerreckart/odin)。
- [slick](https://github.com/nbari/slick) - 受到 [pure](https://github.com/sindresorhus/pure)、[purs](https://github.com/xcambar/purs) 和 [zsh-efgit-prompt](https://github.com/ericfreese/zsh-efgit-prompt) 的启发。需要“cargo”进行安装。
- [slimline](https://github.com/mengelbrecht/slimline) - 最小、快速、优雅的 ZSH 提示符。在正确的时间显示正确的信息。
- [sm](https://github.com/blyndusk/sm-theme) - 一个简约的主题，包括“git”状态装饰。
- [smail](https://github.com/nimacpp/themes-zsh) - 包括“git”状态、当前目录和上次命令运行的退出状态的装饰器。
- [small-terminal-diy](https://github.com/Sokkam/small-terminal-diy-theme) - [oh-my-zsh](https://github.com/ohmyzsh/ohmyzsh) 中的 [ys](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/ys.zsh-theme) 主题的变体。
- [smelly](https://github.com/Vicfs/smelly-theme/) - 极简提示符，包括 Python `venv` 和 `git` 状态的装饰器。
- [smiley](https://github.com/gsamokovarov/smiley.zsh-theme) - 提示时脸上有快乐和悲伤的表情。
- [snowflake](https://github.com/angelina-tsuboi/snowflake-zsh-theme) - 优雅、简单、整洁的 ZSH 主题，包括美观的冷色调，与深色主题相协调。
- [sobole](https://github.com/sobolevn/sobole-zsh-theme) - 受老式爱好启发的简约主题。没有冗长的噱头，没有表情符号，没有指尖陀螺，也没有其他视觉噪音。有浅色和深色两种模式。
- [soda-pop](https://github.com/im-adnan/soda-pop.zsh-theme) - 一个快速、可定制、高度可视化、纯 shell 异步 `git` 提示主题。它结合了信息丰富的 git 状态、执行跟踪器、丰富的泡泡糖/汽水美学以及针对浅色和深色模式优化的精确颜色映射。
- [softblobby](https://github.com/gsalami00/softblobby/) - 适合喜欢独角兽、粉色和紫色的人的主题。包括“git”信息、当前目录、时间和用户名的装饰器。
- [solarized-powerline (houjunchen)](https://github.com/houjunchen/solarized-powerline) - ZSH 的 Solarized 电力线风格主题。
- [solarized-powerline (KuoE0)](https://github.com/KuoE0/oh-my-zsh-solarized-powerline-theme) - 太阳能电力线变体。
- [solarizsh](https://github.com/paddykontschak/Solarizsh) - 修复了 robbyrussell 的 oh-my-zsh 主题的颜色，以便与 [solarized](https://github.com/altercation/solarized) 终端配合使用。
- [sorin-modified-dark](https://github.com/hrmeetsingh/sorin-modified-dark) - 基于[索林](https://github.com/ohmyzsh/ohmyzsh/wiki/Themes#sorin)。极简主义，添加“git”状态和当前目录的装饰器。
- [spaceship](https://github.com/denysdovhan/spaceship-prompt) - 带有 `git`、`nvm`、rvm/rbenv/chruby、python、`ssh` 和其他有用的状态装饰器的主题。
- [spaceshit](https://github.com/claudiosanches/spaceshit-zsh-theme) - [spaceship](https://github.com/denysdovhan/spaceship-prompt) 的美丽与极简设置的速度。包括当前目录、“git”状态、命令执行时间和颜色编码的成功/错误符号的装饰器。
- [spectere](https://github.com/Spectere/spectere-omz-theme) - 类似电力线。包括当前目录、根状态、“user@hostname”和“git”状态的装饰器。
- [spowerline](https://mbauhardt.github.io/spowerline/) - 用 scala 编写，灵感来自 [Agnoster](https://github.com/agnoster/agnoster-zsh-theme)、[tmux](https://tmux.github.io) powerline、vim powerline 和 vim status 插件。
- [spyrhoo](https://github.com/FajarKim/spyrhoo-zsh-theme) - 包括时间、`git` 和当前目录装饰。
- [ssfprompt](https://github.com/hugoh/zsh-ssfprompt) - 简单、纤薄、快速。包括 `ssh`、virtualenv 和 vcs 装饰。
- [staples](https://github.com/dersam/staples) - 基于[bureau](https://github.com/isqua/bureau)，如果通过 SSH 连接，则显示 `user@host`。
- [starboy](https://github.com/prdpx7/Starboy) - 一个简单的主题。
- [starship (wintermi)](https://github.com/wintermi/zsh-starship) - 一个使用 Starship 提示以及电力线主题的简单插件。
- [starship](https://starship.rs/) - 最小、快速、高度可定制。
- [starship2k](https://github.com/2KAbhishek/starship2k) - 包括电力线支持、多种语言和多行提示。包括“git”状态的装饰器。
- [statusline](https://github.com/el1t/statusline) - 响应式 ZSH 主题，可在您需要时提供信息片段。
- [steef (danihodovic)](https://github.com/danihodovic/steeef) - Oh-my-zsh steeef 主题作为独立存储库。此存储库背后的目的是避免在使用 steeef 主题时依赖 oh-my-zsh。 ZSH 插件管理器（例如 Antibody）可以使用该主题，而无需使用 oh-my-zsh。
- [steef (zelongguo)](https://github.com/ZelongGuo/steeef) - 基于 [zimfw steef 主题](https://github.com/zimfw/steeef)。包括 username@hostname、python venv、`git` 状态和当前目录的装饰器。需要 [git-info](https://github.com/zimfw/git-info)。
- [steef (zimfw)](https://github.com/zimfw/steeef) - [steeef](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/steeef.zsh-theme)主题的可定制版本。
- [steeple](https://github.com/erwanjugand/steeple-zsh-theme) - 带有“git”状态装饰的极简主题。
- [stellachar](https://codeberg.org/ar-mo/armans-zsh-themes) - 最小的，粉彩。
- [stigmata](https://github.com/VLtim43/stigmata.zsh-theme) - 包括 user@host 和当前目录的装饰器。
- [sublime](https://github.com/pjmp/sublime) - 一个崇高、干净、简约的 ZSH 主题，带有“git”状态装饰。
- [sugar-free](https://github.com/cbrock/sugar-free) - 基于 [Pure](https://github.com/sindresorhus/pure) 和 [Candy](https://github.com/BinaryMuse/oh-my-zsh/blob/binarymuse/themes/candy.zsh-theme) 主题。
- [sukeesh](https://github.com/sukeesh/sukeesh-zsh-theme) - 包括 `git` 状态装饰。在深色终端背景上效果更好。
- [sulfurium](https://github.com/Sulfurium/zsh-theme) - sulfuriumOS 的官方 ZSH 主题。
- [sunrise-ruby](https://github.com/ston1x/sunrise-ruby) - 与 [sunrise](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/sunrise.zsh-theme) 类似，但包含活动的 Ruby 版本。
- [sunrise](https://github.com/tech8i/zsh_sunrise) - 包括电池状态、当前目录、日期和时间的装饰器。
- [superkolo](https://github.com/Minipada/superkolo) - 将日期和返回状态添加到 [kolo](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/kolo.zsh-theme) 主题。
- [susi](https://github.com/carcruz/susi-zsh-iterm) - 包括“git”状态装饰和随附的 iTerm2 配色方案。
- [svs](https://github.com/SvS30/svs-theme) - 干净、无干扰的主题，带有“git”状态和当前路径装饰。
- [sy](https://github.com/ttttmr/sy-zsh-theme) - 基于 [ys](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/ys.zsh-theme)，包含 `git` 状态装饰。
- [t2colorful](https://github.com/AmirhosseinAbutalebi/t2colorful-oh.my.zsh) - 包括“git”信息、当前目录、最后一个命令退出状态和当前时间的装饰器。
- [t2er](https://github.com/t2er/t2er-zsh-theme) - 带有“git”装饰的简约主题。
- [tabaf](https://github.com/bvc3at/tabaf-zsh-theme) - 针对深色背景优化的最小 ZSH 主题。
- [tarcadia](https://github.com/Tarcadia/tarcadia-zsh-theme) - 基于[jonathan](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/jonathan.zsh-theme)。包括当前目录和“git”状态的装饰器。
- [taw-ys-venv](https://github.com/BrokeDudeAbula/taw-ys-venv) - 两行提示符，包含用户名、当前目录、`git` 信息和当前 Python `venv` 的装饰器。基于 [AzarAI-TOP/taw-ys-zsh-theme](https://github.com/AzarAI-TOP/taw-ys-zsh-theme)。
- [tcr](https://github.com/tulioribeiro/zsh-tcr-theme) - 极简主题，显示当前目录的装饰器、“git”状态信息和“nvm”版本。
- [teajay](https://github.com/Teajey/teajey-zsh-theme) - 改编自穆里拉索和鱼腥主题。包括“git”状态的装饰器、当前目录的路径（折叠以仅显示最相关的部分）以及上次命令运行的退出代码。
- [temeraf](https://github.com/filiptoma/temeraf-zsh) - 极简主题，带有“git”状态、时间戳和上次退出状态的装饰。
- [tepig-ys](https://github.com/thingerpig/tepig-ys.zsh-theme) - 包括 `git` 状态装饰和 conda/virtualenv 状态。
- [termux](https://github.com/rooted-cyber/Termux-zsh-theme) - 极简主义主题。
- [thayne](https://github.com/tmccombs/thayne.zsh-theme) - 包括最后一个命令的退出状态、运行时间（如果 > 1 秒）、当前时间、当前目录和 `git` 状态的装饰器。需要 [Nerd 字体](https://github.com/ryanoasis/nerd-fonts)。
- [the-time-lord](https://github.com/jhwhite/the-time-lord) - 基于 [galllifrey](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/gallifrey.zsh-theme) 的主题。
- [theme-line](https://github.com/yw9381/oh-my-zsh_theme_line) - 带有“git”状态的彩色主题。
- [themer](https://github.com/MrRedacted/zsh-themer) - 包括多种配色方案选项，以及“git”状态装饰器。 “.zsh-theme” 文件中还有多个图标可供选择。基于 [strug](https://github.com/triplepoint Five/oh-my-zsh/blob/master/themes/strug.zsh-theme)。
- [themeraf](https://github.com/oliver-svrcek/Themeraf) - 具有用于用户名、工作目录路径中的最后两个目录、“git”状态、时间戳、最后退出状态以及活动虚拟环境名称的装饰器。
- [theozera](https://github.com/theogandara/zsh-theme) - 包括“git”状态的装饰器、截断的当前目录以及最后一个命令运行的退出状态。
- [theta-async](https://github.com/jesec/zsh_theme_theta-async) - 异步版本的θ(https://github.com/eendroroy/theta)。包括 vcs 状态信息。
- [theta](https://github.com/eendroroy/theta) - 包括 `git` 和 `hg` 状态装饰。还有java、python、ruby、node、go和elixir版本信息。
- [theto](https://github.com/heyvito/theto-zsh-theme) - 简单的主题。  需要 [Nerd Fonts](https://nerdfonts.com/)，包括 `vi` 模式状态和 `git` 装饰。
- [thetraveler](https://github.com/bassopenguin/thetraveler) - 受到 theunraveler 的启发，使用符号来显示 `git` 状态。
- [thm](https://github.com/thm-unix/thm-zshtheme) - 包括 virtualenv、当前目录和 `git` 状态的装饰器。
- [thnikk](https://github.com/thnikk/zsh-theme-thnikk) - [spaceship](https://github.com/denysdovhan/spaceship-prompt) 主题的最小版本。
- [thygod](https://github.com/Thy-GoD/thy-god-zsh-theme) - 基于 [gnzh](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/gnzh.zsh-theme) 和 [bira](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/bira.zsh-theme)。包括一个“git”状态装饰器，并在命令失败时将提示更改为红十字。
- [thyme (chenhao-ye)](https://github.com/chenhao-ye/thyme) - 贝壳调味料。基于 [bira](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/bira.zsh-theme)、[gnzh](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/gnzh.zsh-theme) 和[bullet-train](https://github.com/caiogondim/bullet-train.zsh/blob/master/bullet-train.zsh-theme)。
- [thyme (kawamurakazushi)](https://github.com/kawamurakazushi/thyme) - 带有“git”状态装饰的简单主题。
- [toledo](https://github.com/mmatongo/toledo) - 带有“git”状态装饰的快速简约主题。适用于“zsh”、“bash”、“dash”和“yash”。
- [tonni4](https://github.com/AndreyPuzanov/tonni4-zsh-theme) - 包括时间和“git”状态装饰器。
- [topan](https://github.com/fudyartanto/topan-theme-oh-my-zsh) - 包含 `git` 信息；最好在深色背景上使用。
- [torim](https://github.com/Aggrathon/torim) - 受到 [sorin](https://github.com/zimfw/sorin)、[asciiship](https://github.com/zimfw/asciiship) 和 [mh](https://github.com/ohmyzsh/ohmyzsh/wiki/themes#mh) 主题的启发。包括 user@hostname 的装饰器（当通过 `ssh` 访问时）、工作目录的截断路径、是否以 root 身份运行、最后一个命令运行的错误代码（如果失败）、当前时间、长时间运行命令的持续时间、当前虚拟环境和 `git` 状态。
- [tq](https://github.com/kitian616/tq-zsh-theme) - 显示 `git` 状态、时间，需要与 Powerline 兼容的字体。
- [traffic](https://github.com/fcce/traffic-zsh-theme) - ZSH 的深色主题。
- [trajan](https://github.com/denisinla/trajan-zsh-theme) - ZSH 的深色主题。
- [transient](https://github.com/olets/zsh-transient-prompt) - 向您的 zsh 命令行添加临时提示符 — 也就是说，使当前命令行的提示符与过去命令行的提示符不同。例如，过去的提示可能不需要显示那么多的上下文信息。或者，您可能希望将过去的命令放在自己的行上，而不是添加提示前缀，以便更轻松地选择和复制。更多详细信息请访问 [zsh-transient-prompt.olets.dev](https://zsh-transient-prompt.olets.dev/)。
- [trinity](https://github.com/de-luca/Trinity) - 一个基于[geometry](https://github.com/geometry-zsh/geometry)的简单主题。包括 `git` 装饰。
- [trios](https://github.com/MrEchoFi/trios-zsh-theme) - 面向渗透测试人员、网络专家和 CTF 玩家的最小网络朋克 ZSH 提示。六边形子弹段、电蓝色突出显示和颜色编码的命令回显 - 蓝色表示成功，红色表示错误。不需要书呆子字体。
- [tron](https://github.com/iDoTron/tron-zsh-theme) - 包括 `git` 状态、工作目录、时间、user@host 和最后一个命令装饰的返回状态。
- [troopert](https://github.com/TrooperT/Troopert-theme/) - 包括“git”状态的装饰器、最后返回代码（如果非零）、完整密码和“$RPROMPT”的可配置显示。
- [tsotra](https://github.com/nylo-andry/zsh-themes) - 极简主题，包括“git”状态、k8s 上下文和“rvm”状态的装饰器。
- [turs](https://github.com/eikendev/turs) - 快速、最小的受 [Purs](https://github.com/xcambar/purs) 启发的提示。
- [tvline](https://github.com/thvitt/tvline) - 源自 [agnoster](https://gist.github.com/agnoster/3712874) 主题，添加了 powerline 字体增强功能。
- [twilight](https://github.com/Henryws/twilight-prompt) - 极简主义，但包括最后一个命令退出状态、“git”状态和“user@hostname”装饰。
- [type0](https://github.com/MikereDD/type0_zsh-theme) - 灵感来自 yarisgutierrez 的 [classyTouch](https://github.com/yarisgutierrez/classyTouch_oh-my-zsh)。包括 `git` 装饰。
- [typedark](https://github.com/BonnyAD9/TypeDark) - 与 [ZSH 语法突出显示](https://github.com/zsh-users/zsh-syntax-highlighting) 配合使用。
- [typewritten](https://github.com/reobin/typewritten) - 最小且内容丰富的主题，为重要的事情留出了空间。是否异步更新“git”装饰以提高速度。
- [ubunly](https://github.com/alejandromume/ubunly-zsh-theme) - 模仿 Kali Linux 控制台。注意 - 这个主题还重新绑定了很多键并设置了一堆主题应该保留的 ZSH 选项。
- [ubuntu-ish](https://github.com/Thesola10/zsh-ubuntu-ish) - 模仿默认的 Debian/Ubuntu `bash` 提示符。
- [ubuntu-with-vitamins](https://github.com/ureesoriano/zsh-ubuntu-with-vitamins-zim-theme) - 模仿默认的 Ubuntu 提示符，但带有“git”装饰。
- [ubuntu](https://github.com/janstuemmel/zsh-ubuntu-theme) - 最小主题，包括“git”状态装饰。
- [ultima](https://github.com/egorlem/ultima.zsh-theme) - 极简主义，包括 `git` 状态和当前目录装饰器。
- [ultimate](https://github.com/b4b4r07/ultimate) - 极简主题，带有“git”状态装饰器、vim 模式指示器和缩短路径。
- [ultimator](https://github.com/Ultimator14/ultimator-zsh-theme) - [Agnoster](https://gist.github.com/agnoster/3712874) 类似主题。包括当前目录、“user@host”、python virtualenv、后台作业、最后一个命令退出状态和“git”状态信息的装饰器。需要 [zsh-git-prompt](https://github.com/Ultimator14/zsh-git-prompt) 插件和 Nerdfonts。
- [ulyssesys](https://github.com/UlyssesZh/ulyssesys) - 具有当前目录的完整路径、最后一个命令的退出代码和“git”状态的装饰器。
- [unicorn](https://github.com/juliuscaesar/unicorn) - 包括根状态、virtualenv、nvm、rvm、当前目录、时间、当前目录和表情符号“git”信息的装饰器。灵感来自[野樱桃](https://github.com/mashaal/wild-cherry)。
- [unit-1](https://github.com/nerdbude/Unit-1) - 具有 ITWTB 颜色的极简主题。
- [userandnode](https://github.com/timhilton/userandnode) - 一个干净的主题，带有用户名、节点版本、当前目录和“git”信息的装饰器。
- [valuca](https://github.com/keyaedisa/Valuca) - [ducula](https://github.com/janjoswig/Ducula) 的变体。包括后台作业状态、用户名、主机名、virtualenv、当前目录、最后一个命令的退出代码、“git”信息和当前时间的装饰器。
- [vanan](https://github.com/avano/vanan.zsh-theme) - 使用详细的“git”信息增强您的终端。还包括“vi”模式的装饰器和最后一个命令运行的状态。
- [vehemence](https://github.com/H1N1-dev/vehemence-zsh) - 包括`pwd`、`user@host`、`tty`、时间、最后一个命令退出代码和`git`状态的装饰器。
- [velvet](https://github.com/dor133/velvet-zsh-theme) - 包括“git”状态、用户名、当前目录、最后一个命令的退出状态和时间的装饰器。
- [vercel](https://github.com/vercel/zsh-theme) - 带有“git”状态装饰的极简主题。
- [vertepommes](https://github.com/TheRojam/vertepommes-theme) - 基于 ys.包括 vcs 状态、用户名和当前目录装饰。
- [vinhnx](https://github.com/vinhnx/vinhnx.zsh-theme) - 修改自 [mgutz](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/mgutz.zsh-theme)。与 [Solarized](https://github.com/altercation/solarized) 配色方案一起使用时看起来很棒。
- [vitesse](https://github.com/rafaeldellaquila/zsh-vitesse-theme/blob/master/img/preview.png) - 受到 VS Code 的 [Vitesse](https://github.com/antfu/vscode-theme-vitesse) 主题的启发。包括 `git` 状态装饰。
- [voidy](https://github.com/rwejdling/voidy) - 从 lambda(https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/lambda.zsh-theme) 和 [robbyrussell](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/robbyrussell.zsh-theme) 主题借用元素并添加活动的 [aws-vault](https://github.com/99designs/aws-vault) 配置文件到提示的右侧。
- [vszambon-ocean](https://github.com/vzambon/vszambon_ocean-zsh-theme) - 包括当前目录的装饰器、“git”状态、日/夜图标、是否在“docker”容器内运行以及日期和时间。
- [vtex](https://github.com/charleseduardome/oh-my-zsh-vtex) - 包括 `git` 状态、当前目录、[VTEX](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-vtex-io-cli-command-reference#default-commands) 帐户和 VTEX 工作区的装饰器。
- [vulcan](https://github.com/Bruceboy/vulcan-zsh-theme) - 最小主题让人想起默认的“bash”主题。包括 `git` 装饰。
- [wade](https://github.com/wadehammes/wade.zsh-theme) - 流行的 ZSH 主题 [Agnoster](https://gist.github.com/agnoster/3712874) 和 [Fishy](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/fishy.zsh-theme) 的混搭，并进行了一些视觉调整。
- [wang-iterm](https://github.com/0532/wang-iterm-zsh) - 基于0532主题。
- [warm-colours](https://github.com/BastionAtackDev/Warm-Colours.zsh-theme/) - 包括 user@host、当前目录和日期时间的装饰器。
- [warm-springs](https://github.com/brtmax/warm-springs) - 温暖、质朴的 zsh 主题，灵感来自索诺玛的 [Warm Springs 农场](https://www.mazzocco.com/Our-Story/Vineyards/Warm-Springs-Ranch) 图像。
- [warmblood](https://github.com/D42H5/warmblood) - 基于[darkblood](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/darkblood.zsh-theme)。包括“git”信息、user@hostname 和当前目录的装饰器。
- [whale](https://github.com/whalesea520/whale-zsh-theme) - 快速重新实现鲸鱼主题。
- [whales](https://github.com/lbergelson/zsh_whales_theme) - 包括 `git` 状态、java 版本、最后一个命令返回状态和目录的装饰器。
- [wild-cherry](https://github.com/mashaal/wild-cherry) - 适用于 ZSH、iTerm 2、Sublime、Atom 和 Mou 的童话主题主题。
- [windows](https://github.com/juliavallina/windows-zsh-theme/) - 受到 Windows 命令提示符的启发。包括当前目录的装饰器。
- [winline](https://github.com/khuei/winline) - Greg Hurrell 的异步版本[提示](https://github.com/wincent/wincent/blob/master/aspects/dotfiles/files/.zshrc)。包括“git”状态、最后一个命令的持续时间、当前目录、嵌套 shell、根状态的装饰器。
- [wkentaro](https://github.com/wkentaro/wkentaro.zsh-theme) - 适合 Python 用户的简单主题。包括 virtualenv 和 `git` 状态装饰器。
- [work-line](https://github.com/afnizarnur/work-line) - 带有漂亮表情符号的主题。
- [workbench](https://github.com/u8slvn/oh-my-zsh-workbench-theme) - 包括 `git` 状态装饰、工作目录、最后一个命令的退出状态和当前的 `virtualenv`。
- [wormwood](https://github.com/ann-kilzer/annkilzer.zsh-theme) - 包括最后一个命令退出状态、当前目录和“git”状态的装饰器。
- [x](https://github.com/tharindu899/x-theme) - 包括可定制的横幅
- [xandermute](https://github.com/SoYoureAWaffleMan/xandermute-oh-my-zsh-theme/) - 带有“git”和当前目录装饰的极简主题。
- [xavi](https://github.com/onthedock/xavi.zsh-theme) - [gnzh](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/gnzh.zsh-theme) 主题的修改版本，带有“git”状态和当前目录的表情符号装饰。
- [xbira](https://github.com/ITAxReal/xbira) - 基于 [bira](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/bira.zsh-theme)，包括 `git` 状态、user@hostname、上次命令运行的退出状态和当前目录的装饰器。
- [xlk-simple](https://github.com/xuelingkang/xlk-simple-zsh-theme) - 带有“git”装饰的简单主题。
- [xm](https://github.com/Shiaoming/xm) - 黑暗终端的主题。有“git”装饰。
- [xor](https://github.com/xor3n/xor-zsh-theme) - 自我描述为简约且“功能匮乏”，包括“git”装饰。
- [xremix](https://github.com/xremix/oh-my-zsh-xremix-theme) - 基于 Jreese 主题插件的 oh-my-zsh shell 主题。
- [xris47](https://github.com/ivan-ristovic/xris47.zsh-theme) - 快速、简单且精简的主题。与 [tmux](https://github.com/tmux/tmux/wiki) 和 [vim-airline](https://github.com/vim-airline/vim-airline) 配合使用效果最佳。
- [xxf](https://gist.github.com/xfanwu/18fd7c24360c68bab884) - 显示当前“git”提交的缩短的哈希值和消息。
- [yairshefi](https://github.com/yaireclipse/yairshefi-ohmyzsh-theme) - 带有行分隔提示的最小主题。基于 [robbyrussell](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/robbyrussell.zsh-theme) 主题。
- [yazpt](https://github.com/jakshin/yazpt) - 一个干净、快速、美观的 ZSH 提示主题，精心整合了 Git/Subversion/TFVC 状态信息，与 Oh My Zsh 等流行的插件管理器集成，并且易于自定义和扩展。
- [yechen](https://github.com/liyechen/yechen.zsh-theme) - 带有“git”状态装饰的极简主题。
- [yeet](https://github.com/jeetelongname/Yeet-theme) - 带有“git”状态装饰的极简提示。
- [yellow peach](https://github.com/tomorrowbye/yellow-peach-theme) - 干净简约的设计。包括“user@hostname”、“git”状态、当前目录和当前时间的装饰器。
- [yellow-sea-diamonds](https://github.com/jimratliff/yellow-sea-diamonds-zsh-theme) - 包括“git”状态、当前目录、活动 python 虚拟环境以及最后一个命令运行的退出状态的装饰。
- [yindev](https://github.com/menyinch/yindev-zsh-theme) - `gndx` 的变体。包括“git”状态和当前目录的装饰。
- [ykali](https://github.com/JeffreyYAJ/ykali-zsh) - 为每个新的 ZSH 会话打印可修改的横幅。包括用户名、主机名、当前目录、wlan0 IP 和 `git` 信息的装饰器。
- [ykmam](https://github.com/julienvanderkluft/ykmam-zsh-theme/blob/master/ykmam.zsh-theme) - 修改自 [ys](https://github.com/cristiancavalli/ys-zsh-custom-theme) 主题并针对深色背景进行了优化。
- [ys-cluster](https://github.com/AndiH/oh-my-zsh-ys-cluster-theme) - [ys](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/ys.zsh-theme) 变体，支持使用大型集群的批量提交系统。支持 Slurm、LSF / IBM Spectrum LSF 和 PBS。
- [ys](https://github.com/cristiancavalli/ys-zsh-custom-theme) - 干净、简单、兼容且有意义的主题，适合深色背景。
- [ysm](https://github.com/hanbinpro/ysm-zsh-theme) - 带有“git”状态信息的简单 ZSH 主题。
- [ysr](https://github.com/raykle/ysr-zsh-theme) - 基于[ys](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/ys.zsh-theme)。包括 `git` 状态装饰。
- [yuki](https://github.com/yuki-torii/yuki-zsh-theme) - 黑暗优化的 ZSH 主题。
- [yuni](https://github.com/skippyr/yuni) - macOS 默认 ZSH 主题的现代版本，添加了原始主题所缺乏的基本开发人员功能。包括用于失败命令的退出代码、您的用户和主机名、缩短的当前目录路径、活动分支和权限装饰器的装饰器：如果您是普通用户，则为“%”；如果是 root，则为“#”；如果您没有修改当前目录的权限，则为“[!]”。适用于 macOS 14 Sonoma 或更高版本。
- [yuyuko](https://github.com/hylwxqwq/yuyuko.zsh-theme) - [ys](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/ys.zsh-theme) 的分支，受到 [yuyuko.vim](https://github.com/hylwxqwq/yuyuko.vim) 的启发。
- [yyl-ys](https://github.com/yunyuliu/yyl-ys.zsh-theme) - 包括 conda 和 venv 状态。
- [yz50](https://github.com/lacanlale/yz50-zsh) - 色彩缤纷，基于 [robbyrussell](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/robbyrussell.zsh-theme) 和 [crunch](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/crunch.zsh-theme) 主题。包括 `git` 状态装饰。
- [z4rr3t](https://github.com/inimicus/z4rr3t) - 基于 sindresorhus 的 [pure](https://github.com/sindresorhus/pure) 主题。
- [za-prompt](https://github.com/babarot/za-prompt) - 一个快速、最小且高度可定制的主题，具有 vi 模式支持和“git”状态、可定制路径和最后一个命令的退出代码的装饰器。
- [zap-robbyrussell](https://github.com/devadathanmb/zap-robbyrussell) - OMZ robbyrussell 主题，已修补以添加与 [zap](https://github.com/zap-zsh/zap) 的兼容性。
- [zcmder](https://github.com/bwpge/zcmder) - 受到 [Cmder](https://cmder.app/) 的启发，带有用于`git`信息、当前目录和根状态的装饰器。
- [zcraft](https://github.com/cpea2506/zcraft) - 极简主题，带有“git”状态、最后一个命令退出状态和最后一个命令所用时间的装饰。
- [zeit](https://github.com/zeit/zeit.zsh-theme) - 针对深色背景进行了优化，包括“git”状态信息。
- [zelda](https://github.com/SuperKnerdBros/zelda.zsh-theme) - 塞尔达风格的主题。包括 `git` 状态装饰。
- [zemm-blinks](https://github.com/aranasaurus/zemm-blinks.zsh-theme) - oh-my-zsh [blinks](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/blinks.zsh-theme) 的定制版本，具有 Mercurial 支持和其他更​​改。
- [zemoji](https://github.com/therzka/zemoji) - 基于[wild-cherry](https://github.com/mashaal/wild-cherry/tree/master/zsh)。包括退出状态、`virtualenv`、`nvm`、`rvm` 和 `git` 状态装饰。
- [zen (cybardev)](https://github.com/cybardev/zen.zsh) - “*NIX”系统的简约主题。包括上次命令运行的执行时间、当前目录和 vcs 状态信息的装饰器。
- [zen (TheCrazyGM)](https://github.com/TheCrazyGM/zen) - Oh-My-Zsh 的干净、信息丰富且可自定义的主题，可提供基本信息，而不会使您的终端混乱。它是为 Python 开发人员设计的，包括 SSH 检测、详细的 Git 状态信息和命令执行时间跟踪等智能功能。
- [zenith (husniadil)](https://github.com/husniadil/zenith-oh-my-zsh-theme) - 一个干净、现代的 Zsh 主题，专为效率和美观而设计。它采用冷色调调色板和直观的 Git 状态指示器，让您的终端工作流程保持顺畅且无干扰。包括用于颜色编码“git”状态、最后一个命令的退出状态和紧凑目录显示的装饰器。
- [zero (arlimus)](https://github.com/arlimus/zero.zsh) - Zero 的主题和插件。有浅色和深色终端背景的变体。
- [zero (shirozuki)](https://github.com/shirozuki/zero-zsh-theme) - 带有装饰器的简约提示，显示“git”状态、当前目录、退出状态和上次运行命令的执行时间。
- [zeroastro](https://github.com/zeroastro/zeroastro-zsh-theme) - 最适合深色背景，包括“git”状态装饰。
- [zerocake](https://github.com/ZeroPoke/ZeroCake.zsh-theme) - 在黑暗背景下效果更好。
- [zest](https://github.com/hash-bang/zsh-theme-zest) - ZSH 的功能主题。受 [zsh2000](https://github.com/consolemaverick/zsh2000)、[agnoster](https://gist.github.com/agnoster/3712874) 和 [powerline](https://github.com/jeremyFreeAgent/oh-my-zsh-powerline-theme) 主题影响。
- [zeta](https://github.com/skylerlee/zeta-zsh-theme) - 显示用户名、`git` 状态信息、机器名称、当前工作目录和最后一个命令的成功/失败状态的装饰。
- [zhiyin](https://github.com/AmyangXYZ/zhiyin-zsh-theme) - 包括用户@主机、当前工作目录和“git”状态信息的装饰器。
- [zido](https://github.com/SidonieBouthors/zido-zsh-theme) - 包括“git”状态和当前目录的装饰器。
- [zigbar](https://github.com/dbushell/zigbar) - 用之字写成。包括“git”状态、当前目录的装饰器。需要 [Nerd Font](https://www.nerdfonts.com/font-downloads)。
- [zinc](https://gitlab.com/robobenklein/zinc) - 一个极快的、纯粹的 ZSH、混合异步提示，灵感来自 [Powerlevel9k](https://github.com/bhilburn/powerlevel9k) 和 [Agnoster](https://github.com/agnoster/agnoster-zsh-theme)，易于扩展且高度可配置。它支持使用 [zsh-async](https://github.com/mafredri/zsh-async) 的异步段。
- [zish](https://github.com/RubixDev/zish/) - 基于 `fish` shell 的默认外观。
- [zlambda](https://github.com/wdhg/zlambda) - 极简主义，包括没有特殊字体要求的“git”装饰。
- [zodiac](https://github.com/adamalsen/zsh-zodiac) - 包括与当前年份相对应的动物表情符号。
- [zoo](https://github.com/salamantos/zoo_sh) - 带有动物表情符号的休闲主题。包括当前目录、时间和“git”状态的装饰器。
- [zp](https://github.com/Karitham/zp) - 快速提示，用“zig”编写。包括 `git` 状态和当前目录装饰器。
- [zprompts](https://github.com/z-shell/zprompts) - 使用原始“zsh”主题子系统的主题（提示）。
- [zqt](https://github.com/ladychili/zqt-zsh-theme) - oh-my-zsh 的 [maran](https://github.com/ohmyzsh/ohmyzsh/blob/master/themes/maran.zsh-theme) 主题的修改版本。
- [zsh1999](https://github.com/DTan13/zsh1999) - 包括网络连接、电池和“git”状态装饰。
- [zsh2000](https://github.com/consolemaverick/zsh2000) - 类似于 Powerline 的主题，包括 `rvm` 提示符、`git` 状态和分支、当前时间、用户、主机名、密码、退出状态、是否以 root 身份运行和后台作业状态。
- [zsh313](https://github.com/amirali313/zsh313-theme) - 带有“git”状态装饰的最小主题。
- [zshcomrade](https://github.com/landongn/zshcomrade) - ZSH 主题，同志！包括 `git` 状态装饰。
- [zshify](https://github.com/nrjdalal/zshify) - 一种简约的单命令安装，可自定义您的提示。需要 [npx](https://docs.npmjs.com/getting-started/installing-npm-packages-locally)。
- [zshiggy](https://github.com/malouro/zshiggy) - 包括“git”状态、“node.js”版本的装饰器。
- [zshred](https://github.com/redxtech/zshred) - 显示当前目录、`git` 装饰、最后一个命令的退出状态和时间。
- [zskai](https://github.com/dinizgab/zskai-theme) - 基于 Monokai 的简单主题。包括 user@hostname、时间、`git` 状态和当前工作目录的装饰器。
- [zunder](https://github.com/Warbacon/zunder-prompt) - 基于[gitstatus](https://github.com/romkatv/gitstatus)的简单快速的ZSH提示。
- [zwsh](https://github.com/naens/zwsh) - ZSH 的 Zpm3/Wordstar 模式/主题。
- [zys](https://github.com/ZYSzys/zys-zsh-theme) - 与 [Agnoster](https://github.com/agnoster/agnoster-zsh-theme) 类似，旨在根据上下文披露信息，具有电力线美感。
- [zzshell](https://github.com/thezzisu/zzshell) - 受到默认的 [Oh-My-Zsh](http://ohmyz.sh/) 主题的启发。显示退出代码和“git”状态装饰。不需要 Powerline 字体。

## 字体

此处列出的一些主题需要与 Powerline 兼容的字体，以下是其中一些：

- [Awesome Terminal Fonts](https://github.com/gabrielelana/awesome-terminal-fonts) - 一系列字体，包括一些漂亮的等宽图标。
- [Fantasque Awesome Font](https://github.com/ztomer/fantasque_awesome_powerline) - 一个漂亮的等宽字体，用 Font-Awesome、Octoicons 和 Powerline-Glyphs 进行了修补。
- [Fantasque-sans](https://github.com/belluzj/fantasque-sans) - 另一种与电力线兼容的字体。
- [Hack](https://sourcefoundry.org/hack/) - 另一种专为源代码设计的电力线兼容字体。
- [Input Mono](https://store.typenetwork.com/foundry/djr/series/input?family=input-mono) - 专为代码设计的字体系列。它提供等宽字体和比例字体，并包括电力线字形。
- [Iosevka](https://github.com/be5invis/Iosevka) - 程序员的字体，由代码构建。高度可定制。
- [Maple](https://github.com/subframe7536/maple-font) - 一种开源等宽字体，支持 Nerd Font，专注于平滑您的编码流程。
- [Monoid](https://larsenwork.com/monoid/) - Monoid 可进行定制和优化，即使在低分辨率显示器上，也可以在 15 像素行高下以类似位图的清晰度进行编码。
- [Nerd Fonts](https://github.com/ryanoasis/nerd-fonts) - 收集了超过 20 种修补字体（超过 2,000 种变体）以及适用于 Powerline、Font Awesome、Octicons、Devicons 和 Vim Devicons 的 FontForge 字体修补程序 Python 脚本。包括：Droid Sans、Meslo、源代码、AnonymousPro、Hack、ProFont、Inconsolata 等等。
- [Powerline patched font collection](https://github.com/powerline/fonts) - 大约十几种字体的集合，经过修补以包括电力线字形。
- [SFMono Nerd Font Ligaturized](https://github.com/shaunsingh/SFMono-Nerd-Font-Ligaturized) - macOS SFMano 字体的预修补 opentype 版本，支持连字和 Nerd 字体。
- [Terminus](http://files.ax86.net/terminus-ttf/) - Terminus 的 TTF 版本，包含电力线字形。

## 安装

如果您还没有首选的 ZSH 框架，我推荐 [zgenom](https://github.com/jandamm/zgenom)。它在 shell 会话启动期间增加了最小的开销，因为它仅在您更改插件列表时生成加载脚本，并且该加载脚本是在启动期间获取的，而不是每次都重新计算。

### 抗原

大多数这些插件可以通过将“antigen bundle githubuser/reponame”添加到您的 .zshrc 文件来安装。 Antigen 将在您下次启动“zsh”时自动为您克隆插件。您还可以使用“antigen bundle githubuser/reponame”将该插件添加到正在运行的 ZSH 中进行测试，然后再将其添加到“.zshrc”。

### 多兹什

1. 将新插件克隆到`.zsh.local/modules`中
2. 在`.zshrc`中加载插件模块
3. 打开新的 ZSH 终端窗口或选项卡

### 哦我的Zsh

1. `cd ~/.oh-my-zsh/custom/plugins`
2. `git 克隆仓库`
3. 将存储库添加到您的插件列表中

### 普雷斯托

1. 将插件克隆到 prezto 模块目录中
2. 将插件添加到您的 `.zpreztorc` 文件中
3. 打开新的终端窗口或选项卡

### 兹根

Zgen 没有得到积极维护。我建议您切换到 [Zgenom](https://github.com/jandamm/zgenom) 分支，这是。

### 兹格诺姆

大多数这些插件都可以通过将“zgenom load githubuser/reponame”添加到“.zshrc”文件中来安装，该文件与您执行其他“zgenom load”调用的函数相同。

当您执行“zgenom save”时，Zgenom 会自动为您克隆插件存储库。

### 塞插头

大多数这些插件都可以通过将 `zplug "githubuser/reponame"` 添加到您的 `.zshrc` 文件来安装。

### zpm

大多数这些插件都可以通过将“zpm load "githubuser/reponame"”添加到“.zshrc”文件中来安装。

## 编写新的插件和主题

我已经在[此处]（https://github.com/unixorn/awesome-zsh-plugins/blob/master/Writing_Plugins_and_Themes.md）记录了一些编写新插件和主题的建议。

还有更详细的[Zsh插件标准](https://zdharma-continuum.github.io/Zsh-100-Commits-Club/Zsh-Plugin-Standard.html)。

## 其他资源

### 中山工具

- [argcomplete](https://github.com/kislyuk/argcomplete) - 使用 Python 的“argparse”模块为程序生成制表符补全。
- [carapace](https://github.com/rsteube/carapace) - Bash、Elvish、Fish、Oil、Powershell、Xonsh 和 ZSH 的补全生成器。注意 - 这不会根据需要自动生成补全，您必须显式运行它才能为命令生成补全。
- [cgen](https://github.com/acristoffers/cgen) - 从单个 YAML 文件生成 Fish、Bash 和 ZSH 的 shell 补全以及手册页。不再需要为每个 shell 手写单独的完成文件。
- [completion-generator](https://github.com/RobSis/zsh-completion-generator) - 尝试从程序的帮助文本中读取选项列表并自动生成补全函数。请注意，这不会自动执行，您必须显式调用生成器来创建完成脚本。
- [completion-generators](https://github.com/zetlen/zsh-completion-generators) - 有一个工具名称表以及用于输出这些工具的完成脚本的命令。每次加载时，将检查该表并为“$PATH”中找到的每个工具运行完成命令，并将其输出保存到文件“toolnam”中。如果此存储库的路径位于“$fpath”中，则补全将立即生效。
- [complgen](https://github.com/adaszko/complgen) - 从类似手册页/EBNF 的语法生成 bash/fish/zsh 的完成脚本。生成的独立脚本仅需要存在目标 shell。
- [crazy-complete](https://github.com/crazy-complete/crazy-complete) - 每个程序都应该在 shell 中具有自动完成功能，以增强用户体验和生产力。 “crazy-complete”通过生成健壮且可靠的自动完成脚本来帮助解决此任务。
- [manpage-completion-generator](https://github.com/umlx5h/zsh-manpage-completion-generator) - 从手册页生成 ZSH 补全。需要由fish shell安装的[create_manpage_completions.py](https://github.com/fish-shell/fish-shell/blob/master/share/tools/create_manpage_completions.py)
- [oclif completion generator](https://github.com/MunifTanjim/oclif-plugin-completion) - 为缺少 shell 补全的命令生成 shell 补全。
- [oh-plugin](https://github.com/mbergo/oh-plugin) - 通过输入 `oh-plugin install repository_address` 帮助您安装 [oh-my-zsh](https://ohmyz.sh) 插件。
- [rust-zsh-plugin-cli](https://github.com/johnstonskj/rust-zsh-plugin-cli) - 该工具为 Zsh 插件搭建了内置最佳实践，包括用于干净卸载的函数跟踪、可选别名支持、自动加载函数以及用于 shellcheck 和 shellspec 的 CI/CD 工作流程。从最小、简单或完整模板中进行选择，以匹配您插件的复杂性。
- [scog](https://github.com/Agentrifat/scog) - Scog 是 Shell COMpletion 生成器。该工具可帮助您轻松管理和生成 shell 环境的命令完成。
- [shell-color-prompt-tool](https://github.com/kyletimmermans/shell-color-prompt-tool) - 帮助您创建“ZSH”或“bash”的自定义提示。
- [shellSpec](https://github.com/shellspec/shellspec) - 适用于 dash、bash、ksh、ZSH 和所有 POSIX shell 的全功能 BDD 单元测试框架。
- [shtab](https://github.com/iterative/shtab) - 自动为Python CLI应用程序生成shell选项卡完成脚本，支持“zsh”、“bash”和“tcsh”。
- [smucd](https://github.com/pro555161rblxs/smucd) - 具有交互式选择 UI 的模糊容错 CD 替换。
- [zargparse](https://github.com/ctil/zargparse) - 向其传递一个使用“argparse”的脚本，它会将 ZSH 补全写入您的当前目录。
- [zsh-ai-completions](https://github.com/iloveitaly/zsh-ai-completions) - AI 生成的 ZSH 补全
- [zsh-bench](https://github.com/romkatv/zsh-bench) - 交互式 ZSH 的基准。它测量交互式“zsh”的用户可见延迟：输入延迟、命令延迟等。
- [zshdb](https://github.com/rocky/zshdb) - ZSH 调试器。
- [zshelldoc](https://github.com/zdharma-continuum/zshelldoc) - 用于 shell 脚本的 Doxygen。解析 ZSH 和 Bash 脚本，输出带有函数列表、调用树、导出变量列表等的 Asciidoc 文档。
- [zunit](https://github.com/zunit-zsh/zunit) - ZSH 的强大单元测试框架。



### 其他有用的列表

- [awesome-devenv](https://github.com/jondot/awesome-devenv) - 一系列很棒的工具、资源和工作流程技巧，打造了一个很棒的开发环境。
- [awesome-sysadmin](https://github.com/n1trux/awesome-sysadmin) - 很棒的开源系统管理资源的精选列表。
- [Terminals Are Sexy](https://github.com/k4m4/terminals-are-sexy) - 为 CLI 爱好者精心策划的列表。

在 [真棒集合](https://github.com/sindresorhus/awesome) 中查找其他有用的 Awesome-* 列表

### 其他参考资料

- [ZSH参考卡](http://www.bash2zsh.com/zsh_refcard/refcard.pdf)和[zsh-lovers网站](https://grml.org/zsh/zsh-lovers.html)是必不可少的。

- [掌握 ZSH](https://github.com/rothgar/mastering-zsh) 是一个很棒的教程，它以基础知识为基础，向您展示高级 ZSH 用法、自定义和实际示例。

## 谢谢

非常感谢多年来所有的贡献者。如果没有您的帮助，这个列表就不会那么完整。

<a href="https://github.com/unixorn/awesome-zsh-plugins/graphs/contributors">
  <img src="https://contributors-img.web.app/image?repo=unixorn/awesome-zsh-plugins" />
</a>

使用 [contributors-img](https://contributors-img.web.app) 制作。
