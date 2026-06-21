# 很棒的开发环境 [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

一系列很棒的工具、资源和工作流程技巧，打造了一个很棒的开发环境。

受到 [awesome-go](https://github.com/avelino/awesome-go) 的启发，而 [awesome-go](https://github.com/avelino/awesome-go) 又受到 [awesome-python](https://github.com/vinta/awesome-python) 的启发。

### 贡献

[指南](https://github.com/jondot/awesome-devenv/blob/master/CONTRIBUTING.md) 调整并改编自 `awesome-go` - 谢谢！

但简而言之：

* 列表按字母顺序排序
* 如果您认为某个项目不应该出现在此处 [打开问题](https://github.com/jondot/awesome-devenv/issues/new)


非常感谢[贡献者列表](https://github.com/jondot/awesome-devenv/graphs/contributors) 上的每个人:)


# 内容

_注意：对于特定于操作系统的工具，请尽量用 `OSX/WIN/*NIX/LIN` 进行标记_



- [Admins](#admins)
- [Benchmarking](#benchmarking)
- [Data](#data)
- [Diagnostics](#diagnostics)
- [Desktop](#desktop)
- [Documentation](#documentation)
- [Dotfiles](#dotfiles)
- [Editors](#editors)
  - [Atom](#atom)
  - [崇高的文字](#sublime-text-3)
  - [Vim](#vim)
  - [IntelliJ](#intellij)
  - [VSCode](#visual-studio-code)
- [Git](#git)
- [Misc](#misc)
- [Notifications](#notifications)
- [Orchestration](#orchestration)
- [Presentation](#presentation)
- [Shell](#shell)
- [Text](#text)
- [Terminal](#terminal)
- [Workflow](#workflow)


## 管理员
*管理数据库、权限等的工具*

* [hss](https://github.com/six-ddc/hss) - 再也不用输入烦人的 ssh 命令了。
* [MongoHub](https://github.com/fotonauts/MongoHub-Mac/releases) - mongo 的本机 OSx 客户端
* [Robomongo](http://robomongo.org/) - MongoDB 的跨平台管理员


## 标杆管理
*对代码或服务进行基准测试的工具*

* [阿帕奇基准（AB）](http://httpd.apache.org/docs/2.2/programs/ab.html)
* [boom](https://github.com/rakyll/boom)
* [httperf](http://www.hpl.hp.com/research/linux/httperf/)
* [phantomas](https://github.com/macbre/phantomas) - 网站性能评估工具
* [siege](http://www.joedog.org/siege-home/)
* [Vegeta](https://github.com/tsenart/vegeta)
* [wrk](https://github.com/wg/wrk)
* [redis-faina](https://github.com/Instagram/redis-faina) Instagram 的 Redis 计数器/计时统计基于 MONITOR 命令


## 数据
*处理线上和线下数据的工具*

* [s3cmd](https://github.com/s3tools/s3cmd) - Amazon 的 S3 CLI 工具


## 诊断
*在工作时检查诊断系统的工具*

* [glances](https://github.com/nicolargo/glances)
* [nmon](http://nmon.sourceforge.net/pmwiki.php)
* [gtop](https://github.com/aksakalli/gtop)


## 桌面
*用于改进和修改普通桌面的工具*

* [Alfred](http://www.alfredapp.com/) - OSX 生产力应用程序 `/OSX/`
* [hydra](https://github.com/sdegutis/hydra) - 为您的桌面编写脚本
`/OSX/`
* [Keycastr](https://github.com/sdeken/keycastr) - 出示你的钥匙
呈现/铸造 `/OSX/`

## 文档
*记录项目的工具*

* [Log4brains](https://github.com/thomvaill/log4brains) - 文档即代码知识库，用于管理项目的架构决策记录 (ADR) 并将其自动发布为静态网站。


## 点文件

* [dotfiles.github.io](https://dotfiles.github.io/) - 收集的点文件资源。包含带有点文件引导程序的部分以及各种 shell 和编辑器的框架列表。
* [Zach Holman's](https://github.com/holman/dotfiles) - oh-my-zsh、osx、Zsh、vi、Ruby、Git 等
* [Mathias Bynens's](https://github.com/mathiasbynens/dotfiles) - .files，包括 ~/.osx — OS X 的明智黑客默认值
* [Thoughtbot's](https://github.com/thoughtbot/dotfiles) - 一组 vim、zsh、git 和 tmux 配置文件
* [Paul Miller's](https://github.com/paulmillr/dotfiles) - 丰富多彩且强大的 OS X 配置文件和实用程序


## 编辑
*只有适合您最喜欢的编辑器的出色工具和插件*

### 原子

* [atom-beautify](https://github.com/Glavin001/atom-beautify) - 在 Atom 中美化 HTML（包括 Handlebars）、CSS（包括 Sass 和 Less）、JavaScript 等。
* [file-icons](https://github.com/DanBrooker/file-icons) - 将文件特定图标添加到 Atom 以改进视觉 grep。
* [highlight-selected](https://github.com/richrace/highlight-selected) - 双击某个单词可在整个打开的文件中突出显示该单词。
* [minimap](https://github.com/atom-minimap/minimap) - 完整源代码的图形化映射（预览）。
* [minimap-git-diff](https://github.com/atom-minimap/minimap-git-diff) - Atom git-diff 包的小地图绑定。
* [minimap-highlight-selected](https://github.com/atom-minimap/minimap-highlight-selected) - 高亮选中的包的小地图绑定。
* [atom-project-manager](https://github.com/danielbrodin/atom-project-manager) - 轻松访问您的所有项目，并使用项目特定的设置和选项来管理它们。
* [atom-tree-view-git-status](https://github.com/subesokun/atom-tree-view-git-status) - 在 Atom 树视图中显示 Git 存储库状态。
* [atom-pigments](https://github.com/abe33/atom-pigments) - 用于显示项目和文件中颜色的 Atom 包。

### 维姆

* [Completor](https://github.com/maralla/completor.vim) - 异步自动完成，支持全向和语义完成。
* [Powerline](https://github.com/Lokaltog/powerline) - 改进了缓冲区的状态栏。
* [snipmate](https://github.com/garbas/vim-snipmate) - 文本片段与 Textmate 片段兼容。
* [The Ultimate Vim Distribution](http://vim.spf13.com/) - spf13-vim 是 Vim、GVim 和 MacVim 的 vim 插件和资源的发行版。

### 崇高文本3

* [AdvancedNewFile](https://github.com/skuroda/Sublime-AdvancedNewFile) - 文件创建插件。
* [Emmet](https://github.com/sergeche/emmet-sublime)
* [Git Gutter](https://github.com/jisaacks/GitGutter) - 在编辑器窗口的边缘显示更改/添加的行。
* [jsFormat](https://github.com/jdc0589/JsFormat) - JavaScript 格式化。
* [LiveReload](https://github.com/dz0ny/LiveReload-sublimetext2) - LiveReload 插件。
* [MarkdownEditing](https://github.com/SublimeText-Markdown/MarkdownEditing) - Markdown 语法理解和良好的配色方案。
* [Package Control](https://sublime.wbond.net/installation) - Sublime Text 包管理器。
* [RubyTest](https://github.com/maltize/sublime-text-2-ruby-tests) - 用于运行 Ruby 测试的插件。
* [Side Bar Enhancments](https://github.com/titoBouzout/SideBarEnhancements) - Sublime Text 侧边栏的增强。文件和文件夹。
* [Sublime Git](https://github.com/kemayo/sublime-text-git) - Sublime 的 Git 集成。
* [Sublime Linter](https://github.com/SublimeLinter/SublimeLinter3/) - 交互式代码检查。
* [TrailingSpaces](https://github.com/SublimeText/TrailingSpaces) - 突出显示尾随空格并立即将其删除。

### 智能

* [keymap](https://github.com/jondot/keymaps/) - 混合 Vim/ReSharper/Intellij 键盘映射

### 视觉工作室代码

* [Dev Git Repo](https://github.com/Microsoft/vscode) - VS Code 的 Github 代码存储库
* [Monaco Editor Git Repo](https://github.com/microsoft/monaco-editor) - 基于浏览器的底层编辑器的 Github 代码存储库

#### 扩展
* [VS Code Extension Marketplace](https://marketplace.visualstudio.com/search?target=VSCode&category=All%20categories) - 扩展的官方网站
* [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) - 官方 Python 扩展
* [Sync settings](https://marketplace.visualstudio.com/items?itemName=Shan.code-settings-sync) - VS 代码设置的设置和扩展同步的出色扩展

## git
*打造精彩 Git 体验的工具和插件*

* [awesome-github](https://github.com/fffaraz/awesome-github) - Faraz Fallahi 维护着 GitHub 和 Git 资源的精选列表。
* [gh](https://github.com/jingweno/gh) - 快速 GitHub 命令行客户端（集线器端口到 Go）
* [git-extra-commands](https://github.com/unixorn/git-extra-commands) - 收集的 git 帮助脚本
* [git-extras](https://github.com/visionmedia/git-extras) - GIT 实用程序——repo 摘要、repl、变更日志数量、作者提交百分比等
* [git-it-on](https://github.com/peterhurford/git-it-on.zsh) - ZSH 插件，添加一个 gitit 命令，用于在当前分支中打开 github 上的当前目录
* [git-secret](https://github.com/sobolevn/git-secret) - 一个 bash 工具，用于将您的私人数据存储在 git 存储库中。
* [git-semver](https://github.com/markchalloner/git-semver) - 一个 git 插件，使语义版本控制 2.0.0 和更改日志管理更容易。
* [git-sweep](https://github.com/arc90/git-sweep) - 安全地删除已合并到主干的分支
* [git-up](https://github.com/aanand/git-up) - 更好的“git pull”
* [hub](https://hub.github.com/) - git CLI 包装器，使使用 GitHub 变得更容易
* [scm_breeze](https://github.com/ndbroadbent/scm_breeze) 简化您的 git 工作流程
* [tig](http://jonas.nitro.dk/tig/) - 一个基于 ncurses 的 git 文本模式界面

## 杂项
*其他类别无法找到归属的有用工具*

* [Fenix Web Server](https://fenixwebserver.com) - 具有按钮共享功能的多主机本地静态 Web 服务器（桌面应用程序）。
* [ML Workspace](hhttps://github.com/ml-tooling/ml-workspace) - 用于机器学习和数据科学的基于网络的一体化开发环境。
* [Mockoon](https://mockoon.com) - API / HTTP REST 模拟桌面应用程序
* [HTTP Toolkit](https://httptoolkit.tech) - HTTP 检查和调试桌面应用程序

## 通知
*通知开发人员工作环境变化的工具*

* [CatLight](https://catlight.io) - 开发人员的状态通知程序。检查持续交付版本的状态并显示桌面通知。

## 编排
*用于编排出色的开发环境的工具*

* [azk](https://github.com/azukiapp/azk) - 用于编排开发环境的轻量级开源引擎
* [Nanobox](https://github.com/nanobox-io/nanobox) - 微 PaaS (μPaaS)，用于创建可部署在任何地方的一致、隔离的开发环境 https://nanobox.io。

## 介绍
*展示作品的工具*

* [bespoke.js](https://github.com/markdalgleish/bespoke.js) - DIY演示微框架
* [hacker-slides](https://github.com/msoedov/hacker-slides) - 基于 Reveal.js 的演示工具
* [impress.js](https://github.com/impress/impress.js) - 基于 CSS3 转换和过渡功能的演示框架
* [mithril-slides](https://github.com/wulab/mithril-slides) - 用 Mithril 编写的受 Keynote 启发的演示应用程序
* [remark](https://github.com/gnab/remark) - 浏览器上基于 Markdown 的演示
* [reveal.js](https://github.com/hakimel/reveal.js/) - 浏览器上基于 Markdown 的演示
* [deck.js](https://github.com/imakewebthings/deck.js) - 浏览器上基于 Markdown 的演示
* [vimdeck](https://github.com/tybenz/vimdeck) - 存在于你的 Vim 中
* [WebSlides](https://github.com/jlantunez/webslides) - 使 HTML 演示变得简单

## 壳牌
*拥有出色的 shell 环境的工具*

* [awesome-zsh-plugins](https://github.com/unixorn/awesome-zsh-plugins) - 可与 [zgen](https://github.com/tarjoilija/zgen) 和其他 [oh-my-zsh](https://github.com/robbyrussell/oh-my-zsh/) 兼容的 zsh 框架使用的 zsh 插件列表
* [fish-shell](https://github.com/fish-shell/fish-shell) - 用户友好的命令行 shell
* [hss](https://github.com/six-ddc/hss) - 再也不用输入烦人的 ssh 命令了。
* [oh-my-fish](https://github.com/oh-my-fish/oh-my-fish) - 用于管理 Fish shell 配置的框架，灵感来自 oh-my-zsh。
* [oh-my-zsh](https://github.com/robbyrussell/oh-my-zsh/) - 用于管理 zsh 配置的社区驱动框架。
* [zgen](https://github.com/tarjoilija/zgen) - 用于管理 zsh 配置的更快框架，向后兼容 oh-my-zsh 插件
* [zsh](http://www.zsh.org/) - 专为交互式使用而设计的 shell，尽管它也是一种功能强大的脚本语言。
* [shellcheck](https://github.com/koalaman/shellcheck) - 外壳的绒毛。将在 shell 脚本中发现不推荐使用和/或危险的用法
* [zsh quickstart kit](https://github.com/unixorn/zsh-quickstart-kit) - 设置 zsh 和 zgen 的快速介绍

## 文字
*用于处理文本文件的工具 - 搜索、替换、处理*

* [ack](https://github.com/petdance/ack2) - 基于 Perl 的
比 grep 工具更好。
* [ag](https://github.com/ggreer/the_silver_searcher) - 一个基于 C 的代码搜索工具，类似于 ack，但速度更快
* [peco](https://github.com/peco/peco) - 交互式过滤，如交互式 Grep
* [ripgrep](https://github.com/BurntSushi/ripgrep) - 比 grep 更快，用 Rust 编写


## 终端
*用于终端和终端工作的工具和插件*

* [autojump](https://github.com/joelthelion/autojump) - 记得你的
文件夹并根据部分回忆跳转到它们（例如“j proj”将跳转
到“/home/Users/yourself/projects”。
* [fasd](https://github.com/clvv/fasd) 命令行生产力增强器，提供对文件和目录的快速访问。
* [freshenv](https://github.com/raiyanyahya/freshenv) - 配置、共享、管理本地和云开发人员环境。
* [homebrew](http://brew.sh) - 使用单个命令可以轻松在“OS X”系统上安装开源软件包。
* [hss](https://github.com/six-ddc/hss) - 再也不用输入烦人的 ssh 命令了。
* [httpie](http://httpie.org/) 命令行 HTTP 客户端，用户友好的 cURL 替代品。
* [iTerm2](http://www.iterm2.com/) - 一个很棒的终端替代品 `/OSX/`
* [jq](https://stedolan.github.io/jq/) - 一个轻量级且灵活的命令行 JSON 处理器
* [oh-my-zsh](https://github.com/robbyrussell/oh-my-zsh) - 的
令人难以置信的 ZSH 插件。
* [Pipe Viewer](http://www.ivarch.com/programs/pv.shtml) - 通过管道监控数据进度的工具
* [tmux](https://tmux.github.io/) 很棒的终端多路复用器。
* [zoxide](https://github.com/ajeetdsouza/zoxide) - 导航文件系统的更好方法。用 Rust 编写，跨 shell，比其他自动跳转程序快得多。


## 工作流程
*使用代码改善日常工作流程的工具和插件*

* [fswatch](https://github.com/alandipert/fswatch) - 一个手表工具
将发出 FS 事件，您可以按需运行命令。注意-
也是“fswatch-run”。
* [guard](https://github.com/guard/guard) - 具有庞大插件生态系统的 FS 监视工具
* [just](https://github/casey/just) - 任务运行程序，用于方便地保存和运行特定于项目的命令。与 make 类似，但更好
* [LiveReload](http://livereload.com/) - FS 监视和预处理器作为“/OSX/”和“/WIN/”的桌面应用程序，具有互补的浏览器扩展
  * [guard-livereload](https://github.com/guard/guard-livereload) - Guard 插件与 LiveReload 的浏览器扩展兼容
* [simplehttp](https://github.com/snwfdhmp/simplehttp) 通过 http 开始提供本地目录的最快、最简单的方法。
* [watchman](https://github.com/facebook/watchman) - 脸书更好
`watch` - 请注意它作为一项服务运行。
* [Zappr](https://github.com/zalando/zappr) - GitHub 集成旨在通过启用/禁用拉取请求批准检查来增强您的项目工作流程。
* [ergo](https://github.com/cristianoliveira/ergo) - 管理在不同端口上运行的多个本地服务变得容易。
* [Prodmodel](https://github.com/prodmodel/prodmodel) - 构建数据科学管道工具。
* [Gebug](https://github.com/moshebe/gebug) - 该工具通过无缝启用调试器和热重载功能，使 Dockerized Go 应用程序的调试变得超级简单。
