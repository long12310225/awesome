# 很棒的点文件 [![很棒][2]][1]

点文件资源的精选列表。受到 [awesome][3] 列表的启发。请注意，某些文章或工具可能看起来
旧的或过时的，但这通常意味着它们经过了战斗考验并且成熟（就像点文件本身一样）。随意
提出新文章、项目或工具！

## 文章

### 简介

- [点文件入门][4]、[Lars Kappert][5]
- [点文件入门][6]、[Dries Vints][7]
- [管理点文件][8]、[Lars Kappert][5]
- [点文件应该被分叉][9]，[Zach Holman][10]
- [点文件发现][11]、[永利荷兰][12]
- [我做点文件！][13]，[Jogendra][14]

### 教程

- [设置新的 (OS X) 开发机器：第 3 部分 - 点文件和自定义 SSH 配置][15]
- [使用点文件从零到英雄设置 Mac 开发机器][16]
- [使用 Git 和 GitHub 管理你的点文件][17]
- [conf.d 类似于 zsh/bash 点文件的目录][18]
- [管理你的点文件][19]
- [存储点文件的最佳方式：裸露的 Git 存储库][20]
- [点文件管理][21]

### 外壳启动

- [Shell 启动脚本][22]
- [Zsh/Bash 启动文件加载顺序][23]

### 使用特定工具

- [使用 GNU Stow 管理你的点文件][24]
- [使用 GNU Stow 管理点文件符号链接][25]
- [Ansible 提供的点文件和开发工具][26]

## 查找 dotfiles 存储库

有许多很棒的点文件存储库，每个存储库都包含自己的灵感和精华。一种方式可以通过
他们是[在 GitHub 上搜索“dotfiles”][27]。

另请参阅：

- [谷歌搜索“dotfiles”][28]
- [Archlinux合集][29]
- 提示：在 GitHub 上搜索文件名，例如[路径：\*\*/.gitconfig][30]。

## 点文件存储库示例

最受欢迎、维护良好且协作的点文件存储库和框架的集合。部分项目
仅包含点文件。其他的则更进一步，允许您轻松添加自己的自定义点文件，其中一些包括
管理点文件和插件的脚本。

### 重击

|标题 |描述 |焦点 |
| :---------------------------- | :------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------- |
| [猛击][31] |社区 bash 框架。                    |自动完成、主题、别名、自定义函数。结构良好的框架 |
| [Mathias 的点文件][32] | macOS 的明智黑客默认设置 | 🔧 .files，包括 \~/.macos — macOS 的明智黑客默认设置 |
| [webpro 的点文件][33] | macOS 点文件 | Bash、Homebrew、Brew Cask、Git、Node.js、Hammerspoon。                                                                        |
| [rootbeersoup 的点文件][34] |轻松配置 Bash、Vim 和 macOS |一个`卷曲\| sh` 安装程序和 Makefile 为永久或临时配置提供可移植且轻松的设置。 |

### 兹什

|标题 |描述 |焦点|
| :------------------------- | :------------------------------------------------------------------------------------------------------------------ | :----------------------------------------------------------------------------------------------------------------------------------------------- |
| [Nick Khan 的点文件][35] |用于使用 Zsh 和 Homebrew 配置 macOS 环境的个人点文件。没有多余的东西，只有我实际使用的东西。 | Zsh、Git（带别名）、Visual Studio Code、Ghostty、shell 别名、合理的 macOS 默认值、自定义 CLI 脚本等。
| [thoughtbot 点文件][36] | vim、zsh、git 和 tmux 配置文件集 | Zsh、vim、tmux、git、自制软件。使用[rcm][37]。                                                                                                   |
| [哦我的zsh][38] |用于管理 zsh 配置的社区驱动框架。                                                     | Oh My Zsh 是一个开源的、社区驱动的框架，用于管理您的 Zsh 配置 |
| [普雷兹托][39] | Zsh 的配置框架。                                                                                |使用合理的默认值、别名、函数、自动完成和提示主题丰富命令行界面环境。                      |
| [Dries 的点文件][40] | macOS 点文件的简化方法 | Zsh、Oh My Zsh、macOS、Homebrew、Mackup |
| [sobolevn 的点文件][41] | Dotfiles 为开发者带来快乐 | macOS、zsh、brew、vscode、codespaces、python、node、elixir |
| [yutkat 的点文件][42] |维护良好的点文件，使用 CI 来测试和测量启动速度。                                            | Zsh、Neovim、Wezterm、swaywm 在 Arch/Ubuntu/Fedora Linux 上工作。                                                                                |
| [卢克的空米][43] |我的点文件（由 LARBS 部署）| Zsh、vim/nvim、zsf |
| [2KAbhishek 的dot2k][44] |精心制作、可扩展的点文件，具有多平台支持 | CLI 工具为核心，具有针对不同平台（windows/mac/android）、编辑器和窗口管理器的扩展 |
| [齐姆][45] |模块化、可定制且速度极快的 Zsh 框架 | Zim 是一个 Zsh 配置框架，它捆绑了插件管理器、有用的模块和各种主题，而不会影响速度。 |

### 鱼

|标题 |描述 |焦点 |
| :-------------------- | :---------------------------------------------------- | :------------------------------------------------------------------------------- |
| [哦我的鱼][46] | Fish Shell 框架 |核心基础设施允许您安装软件包来扩展/修改您的 shell |
| [保罗的点文件][47] | paul 的 Fish、bash、git 等配置文件。好东西。 | Fish、macOS、Homebrew、自定义 Shell 函数 |

### 安西布尔

|标题 |描述 |焦点 |
| :---------------------- | :------------------------------------------- | :------------------------------------------------------------------------------ |
| [.点][48] |新的和升级的点文件，现在与 Ansible 一起使用！ |使用 Ansible 完全自动化的桌面设置、配置和维护 |
| [Mac 开发手册][49] |通过 Ansible 设置和配置 Mac |完整的 macOS 开发机器设置，包括 Homebrew、点文件、应用程序和操作系统配置 |
| [sloria 的点文件][50] | sloria 的 dotfiles 作为 Ansible 角色 |使用单个命令设置完整的本地开发环境 |

## 工具

- [Ansible][51] - 极其简单的配置管理、应用程序部署、任务执行和多节点
编排引擎。
- [chezmoi][52] - 跨多台计算机安全地管理您的点文件。
- [comtrya][53] - localhost 的配置管理，用 Rust 编写，适用于 Linux、BSD、macOS 和 Windows。
- [dotbot][54] - 引导你的点文件的工具。
- [dotdrop][55] - 保存你的点文件一次，然后将它们部署到任何地方。
- [dotter][56] - 用 Rust 编写的点文件管理器和模板器。
- [dots][57] - 有意见的点文件生成器，允许快速配置多个不同的窗口管理器
操作系统！
- [Fisher][58] - Fish 的包管理器。
- [新鲜][59] - 保持你的点文件新鲜。 Fresh 是一个从中获取 shell 配置（别名、函数等）的工具
其他的到你自己的配置文件中。
- [GNU Stow][60] - 符号链接场管理器，它采用位于单独的软件和/或数据的不同包
文件系统上的目录，并使它们看起来安装在同一位置。
- [home-manager][61] - 使用 Nix 管理用户环境。
- [homeshick][62] - 用 Bash 编写的 Git 点文件同步器。
- [lnk][63] - Git 原生点文件管理，无需额外配置。
- [mackup][64] - 保持应用程序设置同步 (macOS/Linux)。
- [OpenBoot][65] - Mac 开发环境管理器，可捕获和恢复 Homebrew 包、点文件、shell
通过交互式 TUI 配置和 macOS 首选项。
- [rcm][37] - rc 文件（dotfile）管理。
- [rotz][66] - 用 Rust 编写的完全跨平台的点文件管理器和开发环境引导程序。
- [themer][67] - 从点文件中管理和生成跨开发工具的主题。
- [toml-bombadil][68] - 模板化和管理您的点文件。
- [xdg-ninja][69] - 一个 shell 脚本，用于检查 $HOME 中是否有不需要的文件和目录。
- [yadm][70] - 使用共享 Git 存储库和一些工具来管理多台计算机上的文件集合的工具
附加功能。
- [yolk][71] - 点文件管理器通过注释进行内联模板，因此文件即使未部署也保持有效。

### macOS

- [dockutil][72] - 用于管理停靠项的命令行工具。
- [mas][73] - Mac App Store 命令行界面。

## 杂项

- [dotfiles.github.io][74] - GitHub 上的点文件非官方指南。
- [文件系统层次结构标准][75] - Linux 发行版中的目录结构和目录内容。
- [XDG 基本目录规范][76] - [摘要][77]
- [快捷方式的教训][78] - “隐藏”或“点”文件的想法是如何诞生的，作者：Rob Pike（最初发布于
谷歌+）。

## 相关列表

- [很棒的开发环境][79] - 精选的很棒的工具、资源和工作流程技巧列表，打造了很棒的开发
环境。
- [Awesome Fish][80] - 鱼壳的软件包、提示和资源的精选列表。
- [Awesome Shell][81] - 精选的很棒的命令行框架、工具包、指南和小发明列表。
- [很棒的系统管理][82] - 令人惊叹的开源系统管理资源的精选列表。
- [很棒的 Zsh 插件][83] - 适合与 oh-my-zsh、antigen 和 Prezto 一起使用的 Zsh 插件列表。
- [终端很性感][84] - 为 CLI 爱好者精心策划的终端框架、插件和资源列表。

## 存档/废弃的项目

- [抗原][85]
- [bashdot][86]
- [绑带][87]
- [战斗学校][88]
- [博克][89]
- [苹果酒][90]
- [开发设置][91]
- [点][92]
- [点文件][93]
- [点斯托][94]
- [Eduardo 的点文件][95]
- [省略号][96]
- [安置][97]
- [霍尔曼做点文件][98]
- [想家][99]
- [凯文的点文件][100]
- [科迪][101]
- [macOS 默认值][102]
- [osxc][103]
- [珍珠][104]
- [rkalis 的点文件][105]
- [vcsh][106]（[文章][107]、[文章][108]）
- [亚德][109]
- [零.sh][110]

## 许可证

[![CC0][112]][111]

在法律允许的范围内，[Lars Kappert][113] 已放弃本内容的所有版权以及相关或邻接权
工作。

[1]：https://awesome.re
[2]：https://awesome.re/badge.svg
[3]：https://github.com/sindresorhus/awesome
[4]：https://www.webpro.nl/articles/getting-started-with-dotfiles
[5]：https://github.com/webpro
[6]：https://driesvints.com/blog/getting-started-with-dotfiles/
[7]：https://github.com/driesvints
[8]：https://www.webpro.nl/articles/managing-your-dotfiles
[9]：https://zachholman.com/2010/08/dotfiles-are-meant-to-be-forked/
[10]：https://zachholman.com
[11]：https://wynnnetherland.com/journal/dotfiles-discovery/
[12]：https://wynnnetherland.com
[13]：https://jogendra.dev/i-do-dotfiles
[14]：https://jogendra.dev
[15]：https://mattstauffer.com/blog/setting-up-a-new-os-x-development-machine-part-3-dotfiles-rc-files-and-ssh-config/
[16]：https://code.tutsplus.com/setting-up-a-mac-dev-machine-from-zero-to-hero-with-dotfiles--net-35449t
[17]：http://blog.smalleycreative.com/tutorials/using-git-and-github-to-manage-your-dotfiles/
[18]：https://chr4.org/blog/2014/09/10/conf-dot-d-like-directories-for-zsh-slash-bash-dotfiles/
[19]：https://www.anishathalye.com/2014/08/03/managing-your-dotfiles/
[20]：https://www.atlassian.com/git/tutorials/dotfiles
[21]：https://mitxela.com/projects/dotfiles_management
[22]：https://blog.flowblok.id.au/2013-02/shell-startup-scripts.html
[23]：https://shreevatsa.wordpress.com/2008/03/30/zshbash-startup-files-loading-order-bashrc-zshrc-etc/
[24]：http://brandon.invergo.net/news/2012-05-26-using-gnu-stow-to-manage-your-dotfiles.html
[25]：https://spin.atomicobject.com/manage-dotfiles-gnu-stow/
[26]：http://palcu.blogspot.com/2014/06/dotfiles-and-dev-tools-provisioned-by.html
[27]：https://github.com/search?q=dotfiles&type=Repositories
[28]: https://www.google.nl/search?q=dotfiles
[29]：https://wiki.archlinux.org/index.php/Dotfiles
[30]: https://github.com/search?type=code&q=path%3A**%2F.gitconfig
[31]：https://github.com/Bash-it/bash-it
[32]：https://github.com/mathiasbynens/dotfiles
[33]：https://github.com/webpro/dotfiles
[34]：https://github.com/darylabbate/dotfiles
[35]：https://github.com/nicksp/dotfiles/
[36]：https://github.com/thoughtbot/dotfiles
[37]：https://github.com/thoughtbot/rcm
[38]：https://ohmyz.sh
[39]：https://github.com/sorin-ionescu/prezto
[40]：https://github.com/driesvints/dotfiles
[41]：https://github.com/sobolevn/dotfiles
[42]：https://github.com/yutkat/dotfiles
[43]：https://github.com/LukeSmithxyz/voidrice
[44]：https://github.com/2KAbhishek/dots2k
[45]：https://github.com/zimfw/zimfw
[46]: https://github.com/oh-my-fish/oh-my-fish
[47]：https://github.com/paulirish/dotfiles
[48]：https://github.com/Addvilz/dots
[49]：https://github.com/geerlingguy/mac-dev-playbook
[50]：https://github.com/sloria/dotfiles
[51]：https://www.ansible.com
[52]：https://github.com/twpayne/chezmoi
[53]：https://github.com/comtrya/comtrya
[54]：https://github.com/anishathalye/dotbot
[55]：https://github.com/deadc0de6/dotdrop
[56]：https://github.com/SuperCuber/dotter
[57]：https://github.com/ulises-jeremias/dotfiles
[58]：https://github.com/jorgebucaran/fisher
[59]：https://freshshell.com
[60]：http://www.gnu.org/software/stow/
[61]：https://github.com/nix-community/home-manager
[62]：https://github.com/andsens/homeshick
[63]：https://github.com/yarlson/lnk
[64]：https://github.com/lra/mackup
[65]：https://github.com/openbootdotdev/openboot
[66]：https://github.com/volllly/rotz
[67]：https://github.com/themerdev/themer
[68]：https://github.com/oknozor/toml-bombadil
[69]：https://github.com/b3nj5m1n/xdg-ninja
[70]：https://github.com/TheLocehiliosan/yadm
[71]：https://github.com/elkowar/yolk
[72]：https://github.com/kcrawford/dockutil
[73]：https://github.com/mas-cli/mas
[74]: https://dotfiles.github.io/
[75]：https://en.wikipedia.org/wiki/Filesystem_Hierarchy_Standard
[76]：https://specations.freedesktop.org/basedir-spec/basedir-spec-latest.html
[77]：https://wiki.archlinux.org/title/XDG_Base_Directory
[78]：https://web.archive.org/web/20180827160401/https://plus.google.com/+RobPikeTheHuman/posts/R58WgWwN9jp
[79]：https://github.com/jondot/awesome-devenv
[80]：https://github.com/jorgebucaran/awsm.fish
[81]: https://github.com/alebcay/awesome-shell
[82]：https://github.com/awesome-foss/awesome-sysadmin
[83]: https://github.com/unixorn/awesome-zsh-plugins
[84]：https://github.com/k4m4/terminals-are-sexy
[85]：http://antigen.sharats.me
[86]：https://github.com/bashdot/bashdot
[87]：https://github.com/barryclark/bashstrap
[88]：https://github.com/spencergibb/battleschool
[89]：https://github.com/mattly/bork
[90]：https://github.com/msanders/cider
[91]：https://github.com/donnemartin/dev-setup
[92]：https://github.com/kazhala/dotbare
[93]：https://github.com/jbernard/dotfiles
[94]：https://github.com/clayrisser/dotstow
[95]：https://github.com/eduardolundgren/dotfiles
[96]：https://github.com/ellipsis/ellipsis
[97]：https://github.com/tversteeg/emplace
[98]：https://github.com/holman/dotfiles
[99]：https://github.com/technicalpickles/homesick
[100]：https://github.com/kdeldycke/dotfiles
[101]：https://github.com/jh3y/kody
[102]：https://github.com/kevinSuttle/macOS-Defaults
[103]: http://osxc.github.io
[104]: https://github.com/pearl-core/pearl
[105]: https://github.com/rkalis/dotfiles
[106]：https://github.com/RichiH/vcsh
[107]：https://blog.tfnico.com/2014/03/managing-dot-files-with-vcsh-and-myrepos.html
[108]：https://www.kunxi.org/blog/2014/02/manage-dotfiles-using-vcsh-and-mr/
[109]: http://skwp.github.io/dotfiles/
[110]: https://github.com/zero-sh/zero.sh
[111]：https://creativecommons.org/publicdomain/zero/1.0/
[112]: https://licensebuttons.net/p/zero/1.0/88x31.png
[113]: https://www.webpro.nl
