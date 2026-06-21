```
 █████╗ ██╗    ██╗███████╗███████╗ ██████╗ ███╗   ███╗███████╗
██╔══██╗██║    ██║██╔════╝██╔════╝██╔═══██╗████╗ ████║██╔════╝
███████║██║ █╗ ██║█████╗  ███████╗██║   ██║██╔████╔██║█████╗
██╔══██║██║███╗██║██╔══╝  ╚════██║██║   ██║██║╚██╔╝██║██╔══╝
██║  ██║╚███╔███╔╝███████╗███████║╚██████╔╝██║ ╚═╝ ██║███████╗
╚═╝  ╚═╝ ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝
███████╗██╗  ██╗███████╗██╗     ██╗
██╔════╝██║  ██║██╔════╝██║     ██║
███████╗███████║█████╗  ██║     ██║
╚════██║██╔══██║██╔══╝  ██║     ██║
███████║██║  ██║███████╗███████╗███████╗
╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝
```

# 很棒的外壳 [![很棒][很棒的徽章]][很棒的链接]

精彩的命令行框架、工具包、指南和小发明的精选列表。受到 Awesome-php 的启发。这个很棒的集合也可以在 [Unix-Shell.ZEEF.com](https://unix-shell.zeef.com/caleb.xu) 上找到。
- [Shells](#shells)
- [命令行生产力](#command-line-productivity)
  - [目录导航](#directory-navigation)
- [Customization](#customization)
- [对于开发人员](#for-developers)
- [系统实用程序](#system-utilities)
- [下载和服务](#downloading-and-serving)
- [多媒体和文件格式](#multimedia-and-file-formats)
- [Applications](#applications)
- [Games](#games)
- [外壳包管理](#shell-package-management)
- [Shell脚本开发](#shell-script-development)
- [Guides](#guides)
- [**真棒 Zsh**][真棒-zsh]&nbsp; [![真棒][真棒-徽章]][真棒-zsh]
- [**很棒的鱼**][很棒的鱼] [![很棒][很棒的徽章]][很棒的鱼]
- [**很棒的 Bash**][很棒的 bash] [![很棒][很棒的徽章]][很棒的 bash]
- [其他很棒的清单](#other-awesome-lists)

## 贝壳

*选择您的基础外壳。*

* [bash](https://www.gnu.org/software/bash/) - GNU 项目的 shell (Bourne Again SHell)
* [elvish](https://elv.sh/) - 友好、富有表现力的 shell 功能，例如匿名函数和数据结构
* [es](https://wryun.github.io/es-shell/) - 可扩展 shell，基于 Plan 9 的 [rc](https://github.com/rakitzis/rc) shell
* [fish](https://fishshell.com) - 智能且用户友好的命令行 shell
* [ion](https://github.com/redox-os/ion) - 现代系统 shell，具有简单但功能强大的语法。它完全是用 Rust 编写的。
* [ksh93](https://github.com/att/ast) - 科恩壳牌
* [mksh](https://github.com/MirBSD/mksh) - MirBSD Korn 外壳
* [murex](https://github.com/lmorg/murex) - 更智能的 shell 和脚本环境，具有专为可用性、安全性和生产力而设计的高级功能（例如更智能的 DevOps 工具）
* [ngs](https://github.com/ngs-lang/ngs) - 专为运维创建的全功能脚本语言。 REPL 正在开发中。
* [nushell](https://github.com/nushell/nushell) - 用 Rust 编写的现代 shell
* [oksh](https://github.com/ibara/oksh) - 便携式 OpenBSD ksh
* [osh](https://www.oilshell.org) - Bash 兼容，与称为 Oil 的新型/现代 Unix shell 语言
* [pdksh](https://cvsweb.openbsd.org/cgi-bin/cvsweb/src/bin/ksh/) - 公共领域 Korn shell
* [powershell](https://docs.microsoft.com/en-us/powershell/scripting/overview) 一个跨平台任务自动化和配置管理框架，由命令行 shell 和脚本语言组成
* [shell++](https://github.com/alexst07/shell-plus-plus) - 友好且现代的函数式和面向对象的 shell 脚本语言
* [shenv](https://github.com/shenv/shenv) - 简单的 shell 版本管理
* [tcsh](https://www.tcsh.org/) - 具有文件名补全和命令行编辑功能的 C shell
* [xonsh](https://xon.sh) - Python 风格、BASHwards 风格的 shell 语言和命令提示符
* [yash](https://github.com/magicant/yash) - 符合 POSIX 标准的命令行 shell，内置支持基于命令历史记录的完成和预测
* [zsh](https://www.zsh.org) - 具有脚本语言的强大 shell

## 命令行生产力

*搜索、书签、多路复用和其他工具，让您的终端体验更加高效。*

* [AdvancedNewFile](https://github.com/tanrax/terminal-AdvancedNewFile) - 以递归方式快速创建文件和目录。受到 Vim 插件的启发。
* [ag](https://github.com/ggreer/the_silver_searcher) - 通过目录层次结构进行超快速字符串搜索
* [aliases](https://github.com/sebglazebrook/aliases) - bash 的上下文、动态、有组织的别名
* [arttime](https://github.com/reportaman/arttime) - 文字艺术之美与时钟、计时器、番茄钟++时间管理器的功能相结合
* [autoenv](https://github.com/hyperupcall/autoenv) - 基于目录的环境。
* [await](https://github.com/slavaGanzin/await) - 并行运行命令列表并等待其终止的单个二进制文件
* [bartib](https://github.com/nikolassv/bartib) - 命令行的简单时间跟踪器。它将所有跟踪活动的日志保存为纯文本文件，并允许您创建灵活的报告。
* [bashhub](https://github.com/rcaloras/bashhub-client) - :cloud：云中的 Bash 历史记录。已编制索引且可搜索。
* [boilr](https://github.com/tmrts/boilr) - 一个极快的 CLI 工具，用于从样板模板创建项目。
* [boom](https://github.com/holman/boom) - 在命令行中存储链接和片段
* [borg](https://github.com/ok-borg/borg) - 基于终端的 bash 命令搜索引擎
* [broot](https://github.com/Canop/broot) - 更好的目录导航方式
* [browsh](https://github.com/browsh-org/browsh) - 现代基于文本的浏览器
* [Buku](https://github.com/jarun/Buku) - 强大的命令行书签管理器
* [byobu](https://www.byobu.org) - 基于文本的窗口管理器和终端多路复用器
* [cod](https://github.com/dim-an/cod) - shell 的完成守护进程，它会在您调用 `--help` 命令时进行学习
* [CloudClip](https://github.com/skywind3000/CloudClip) - 您自己的云端剪贴板，在不同系统之间复制和粘贴带有要点的文本
* [ddgr](https://github.com/jarun/ddgr) - 从终端 DuckDuckGo
* [desk](https://github.com/jamesob/desk) - shell 的轻量级工作区管理器
* [direnv](https://github.com/direnv/direnv) - shell 的环境切换器，与 autoenv 进行比较
* [dnote](https://github.com/dnote/dnote) - 具有多设备同步和 Web 界面的简单命令行笔记本
* [eureka](https://github.com/simeg/eureka/) - :bulb：CLI 工具，无需离开终端即可输入和存储您的想法
* [fasd](https://github.com/clvv/fasd) - 命令行生产力增强器，提供对文件和目录的快速访问
* [fd](https://github.com/sharkdp/fd) - 一个简单、快速且用户友好的替代方案。
* [foxy](https://github.com/s-p-k/foxy) - 适用于 Firefox 和 surf 浏览器的纯文本书签。
* [fselect](https://github.com/jhspetersson/fselect) - 使用类似 SQL 的查询查找文件。
* [funky](https://github.com/bbugyi200/funky) - 扩展了 shell 函数的功能，使其更加强大和灵活。
* [fz](https://github.com/changyuheng/fz) - z 的无缝模糊选项卡完成
* [fzf](https://github.com/junegunn/fzf) - 命令行模糊查找器
* [gitmux](https://github.com/arl/gitmux) - 在 Tmux 状态栏中显示 Git 状态
* [googler](https://github.com/jarun/googler) - 来自终端的 Google 搜索、Google 站点搜索、Google 新闻
* [googlr](https://github.com/Astranno/googlr) - 命令行工具，可让您从终端搜索 Google。
* [has](https://github.com/kdabir/has) - `has` 帮助您检查路径上各种命令行工具及其版本的存在
* [how2](https://github.com/santinic/how2) - `how2` 找到在 Unix shell 中执行某些操作的最简单方法。它就像“man”，但你可以用自然语言查询它。
* [navi](https://github.com/denisidoro/navi) - 用于命令行的交互式备忘单工具
* [hhighlighter](https://github.com/paoloantinori/hhighlighter) - 对命令输出中的单词进行着色
* [hr](https://github.com/LuRsT/hr) - 您的终端的“<hr />”
* [hss](https://github.com/six-ddc/hss) - 具有自动完成和异步执行功能的交互式并行 ssh 客户端
* [hstr](https://github.com/dvorka/hstr) - Bash 历史建议框
* [k](https://github.com/supercrabtree/k) - k 是一个 Zsh 脚本，用于使目录列表更具可读性，添加 Git 状态、文件重量颜色和腐烂日期
* [k alias](https://github.com/lingtalfi/k) - 使用简单的单行代码获取酷别名（以及更多）
* [lf](https://github.com/gokcehan/lf) - 用 Go 编写的终端文件管理器，受到 ranger 的启发
* [lf.sh](https://github.com/suewonjp/lf.sh) - 通过更少的输入快速搜索文件并执行更多操作（grep、将路径复制到剪贴板等）
* [lowcharts](https://github.com/juan-leon/lowcharts) - 在终端中绘制低分辨率图形
* [Lmod](https://lmod.readthedocs.io/en/latest/) - 基于 Lua 的环境模块增强了基于 Tcl 的模块，同时向后兼容（与模块相比）
* [loop](https://github.com/Miserlou/Loop) - 使用单行代码编写和控制复杂的循环
* [marker](https://github.com/pindexis/marker) - 为您的 shell 命令添加书签
* [mackup](https://github.com/lra/mackup/) - 保持应用程序设置同步 (OS X/Linux)
* [mcfly](https://github.com/cantino/mcfly) - 浏览您的 shell 历史记录。伟大的苏格兰人！
* [modules](http://modules.sourceforge.net/) - 管理 shell 环境的基于 Tcl 的经典环境模块（与 Lmod、direnv 和 autoenv 相比）
* [nnn](https://github.com/jarun/nnn) - 文件浏览器和磁盘使用分析器具有出色的桌面集成
* [ok-sh](https://github.com/secretGeek/ok-bash) - 您从事许多不同的项目吗？在每个项目中，您使用的命令是否特定于该项目？您需要一个 .ok 文件。
* [parallel](https://www.gnu.org/software/parallel/) - 从标准输入并行构建和执行 shell 命令行
* [pass](https://www.passwordstore.org/) - 使用 GPG 加密和可选的 git 集成从命令行管理密码。
* [pathpicker](https://github.com/facebook/PathPicker) - 接受 grep、搜索、git 等输入；允许从输入结果中选择文件，然后您可以打开该文件或将其作为命令的参数提供。
* [pdd](https://github.com/jarun/pdd) - 带计时器的小型日期、时间差异计算器
* [percol](https://github.com/mooz/percol) - 为 UNIX shell 的传统管道概念添加了交互式过滤功能
* [q](https://github.com/cal2195/q) - Vim 类似 Bash 和 Zsh Shell 的宏寄存器
* [qfc](https://github.com/pindexis/qfc) - Bash 和 Zsh 的文件完成小部件
* [resh](https://github.com/curusarn/resh) - Zsh 和 Bash 的上下文 shell 历史记录
* [rg](https://github.com/BurntSushi/ripgrep) - ripgrep 是一个面向行的搜索工具，结合了 The Silver Searcher 的可用性和 GNU grep 的原始速度
* [screen](https://www.gnu.org/software/screen/) - GNU 终端多路复用器
* [shell-history](https://github.com/pawamoy/shell-history) - 使用 Highcharts 可视化您的 shell 使用情况
* [SHML](https://github.com/odb/shml) - 终端的样式框架（Shell 标记语言）
* [slugify](https://github.com/benlinton/slugify) - 将文件名和目录转换为网络友好格式的命令
* [sman](https://github.com/tokozedg/sman) - :bug：命令行片段管理器
* [spark](https://github.com/holman/spark) - ▂▃▅▂▇ 在你的 shell 中
* [spark.fish](https://github.com/jorgebucaran/spark.fish) - ▂▃▅ 迷你图生成器
* [sheet](https://github.com/oscardelben/sheet) - 命令行的文本片段
* [spot](https://github.com/rauchg/spot) - 小型文件搜索实用程序
- [snips](https://github.com/srijanshetty/snips) - 用于管理代码片段的命令行工具。
* [sqlline](https://github.com/julianhyde/sqlline) - 用于通过 JDBC 向关系数据库发出 SQL 的 Shell（多行、补全、突出显示、方言支持）
* [sshfs](https://github.com/osxfuse/sshfs) - 通过 SSH 挂载远程文件系统的工具
* [sudocabulary](https://github.com/badarsh2/Sudocabulary) - 从您的终端学习英语词汇
* [surfraw](https://gitlab.com/surfraw/Surfraw) - 无需浏览器即可从您的终端浏览特定站点并搜索网络。
* [task-manager](https://github.com/lingtalfi/task-manager) - 只需按两到三个按键即可执行所有脚本。
* [td-cli](https://github.com/darrikonn/td-cli) - 待办事项命令行管理器，用于跨多个项目组织和管理您的待办事项。
* [tere](https://github.com/mgunyho/tere) - cd + ls 的更快替代方案
* [thefuck](https://github.com/nvbn/thefuck) - 使用易于记忆的命令修复常见的 shell 错误
* [tldr](https://github.com/raylee/tldr-sh-client) - 用于 tldr、简化且社区驱动的手册页的全功能 bash 客户端
* [tmux](https://tmux.github.io/) - 惊人的终端多路复用器
* [undollar](https://github.com/xtyrrell/undollar) - undollar 会咬掉您刚刚粘贴到终端的命令尖端的美元符号
* [usql](https://github.com/xo/usql) - SQL 数据库的通用命令行界面。
* [v](https://github.com/rupa/v) - z 代表 vim。
* [wemux](https://github.com/zolrath/wemux) - 多用户 Tmux 变得简单
* [xiki](https://github.com/trogdoro/xiki) - 使shell控制台更加友好和强大
* [xplr](https://github.com/sayanarijit/xplr) - 一个可破解的、最小的、快速的 TUI 文件浏览器
* [xsv](https://github.com/BurntSushi/xsv) - 用 Rust 编写的快速 CSV 命令行工具包
* [xxh](https://github.com/xxh/xxh) - 无论您在何处通过 SSH，都可以携带您最喜爱的 shell。

### 目录导航

* [aliasme](https://github.com/Jintin/aliasme) - 用于快速更改目录的别名助手
* [autojump](https://github.com/wting/autojump) - 一个可学习的 cd 命令 - 从命令行轻松导航目录
* [bashmarks](https://github.com/huyng/bashmarks) - shell 的目录书签
* [bd](https://github.com/vigneshwaranr/bd) - 快速返回上一级目录
* [commacd](https://github.com/shyiko/commacd) - 在 Bash 中移动的更快方式
* [enhancd](https://github.com/b4b4r07/enhancd) - :rocket：带有交互式过滤器的下一代 cd 命令
* [goto](https://github.com/iridakos/goto) - 用于导航到支持自动完成的别名目录的 shell 实用程序
* [jump](https://github.com/gsamokovarov/jump) - Jump 通过了解您的习惯来帮助您更快地浏览文件系统。
* [lazy-cd](https://github.com/pedramamini/lazy-cd) - 用于对文件系统进行书签导航的简单 bash 命令，并通过 bash 完成完成。
* [up](https://github.com/shannonmoeller/up) - 按名称或计数提升目录；适用于 bash、zsh 和 Fish。
* [z](https://github.com/rupa/z) - z 是新的 j，哟
* [z.lua](https://github.com/skywind3000/z.lua) - 新的 cd 命令可帮助您通过了解习惯来更快地导航
* [zoxide](https://github.com/ajeetdsouza/zoxide) - 用 Rust 编写的一种更快的文件系统导航方式
* [zpyi](https://github.com/sakshamsharma/zpyi) - Python in Zsh - 在 shell 中轻松编写 python 脚本

## 定制化

*自定义提示、颜色主题等*

* [aphrodite-terminal-theme](https://github.com/win0err/aphrodite-terminal-theme) - 适用于 bash、fish 和 zsh 的性感终端的简约阿芙罗狄蒂主题（提示）
* [base16-builder](https://github.com/base16-builder/base16-builder) - Base16 生成器
* [bash-full-of-colors](https://github.com/slomkowski/bash-full-of-colors) - 具有屏幕、tmux、git 支持等功能的强大提示
* [bash-git-prompt](https://github.com/magicmonty/bash-git-prompt) - 为 Git 用户提供信息丰富且精美的 Bash 提示
* [bash-powerline](https://github.com/riobard/bash-powerline) - 纯 Bash 脚本中的 Powerline 风格的 Bash 提示符
* [bashstrap](https://github.com/barryclark/bashstrap) - 一种快速美化 OSX 终端的方法
* [bullet-train-oh-my-zsh-theme](https://github.com/caiogondim/bullet-train.zsh) - :bullettrain_side：基于 Powerline Vim 插件的 oh-my-zsh shell 主题
* [emojify](https://github.com/mrowa44/emojify) 命令行上的表情符号 :scream:
* [flatui-terminal-theme](https://dribbble.com/shots/1021755-Flat-UI-Terminal-Theme) - 终端颜色更漂亮
* [geometry](https://github.com/geometry-zsh/geometry) - 一个最小的 ZSH 主题，可以将任何功能添加到左侧提示或（异步）右侧提示中。
* [git-prompt](https://github.com/lvv/git-prompt) - 带有 Git、SVN 和 HG 模块的 Bash 提示符
* [gittify](https://github.com/momeni/gittify) - 丰富多彩的 Bash 提示符 + 自定义的 Git 别名
* [Gogh - Color Scheme](https://github.com/Mayccoll/Gogh) - Gnome 终端的配色方案
* [liquidprompt](https://github.com/nojhan/liquidprompt) - 功能齐全且精心设计的 Bash 和 Zsh 自适应提示
* [mysql-colorize](https://github.com/zpm-zsh/mysql-colorize) - mysql 命令行客户端的着色
* [oh-my-git](https://github.com/arialdomartini/oh-my-git) - bash 和 zsh 的固执己见的 git 提示符
* [oh-my-posh](https://ohmyposh.dev) - 适用于任何用 go 编写的 shell 和平台的提示主题引擎。
* [polyglot](https://github.com/agkozak/polyglot) - 信息丰富的 Git 提示符，适用于 bash、zsh、ksh、mksh、pdksh、oksh、dash、yash、busybox sh 和 osh
* [powerlevel10k](https://github.com/romkatv/powerlevel10k) - 超灵活超棒电力线ZSH主题
* [sexy-bash-prompt](https://github.com/twolfson/sexy-bash-prompt) - 带有颜色、Git 状态和 Git 分支的 Bash 提示符
* [starship](https://starship.rs/) - 用 Rust 编写的快速、可定制的跨 shell 提示符
* [synth-shell](https://github.com/andresgongora/synth-shell) - 带有可定制状态报告和精美 bash 提示的问候语

## 对于开发人员

*命令行开发、版本控制和部署。*

* [1Password SSH Agent](https://developer.1password.com/docs/ssh/) - 使用 1Password 通过生物识别解锁来验证 Git 和 SSH 工作流程
* [ack](https://beyondgrep.com/) - 针对源代码优化的类似 grep 的搜索工具。
* [add-gitignore](https://github.com/TejasQ/add-gitignore) - 交互式 CLI 可根据您的需求为您的项目生成 .gitignore。
* [bcal](https://github.com/jarun/bcal) - 用于存储转换和计算的字节计算器
* [bitwise](https://github.com/mellowcandle/bitwise) - curses 中基于终端的交互式位操纵器。
* [bocker](https://github.com/p8952/bocker) - Docker 用 100 行 bash 实现
* [cloc](https://github.com/AlDanial/cloc) - 计算代码行数
* [doclt](https://github.com/omgimanerd/doclt) - Digital Ocean 的命令行界面
* [dokku](https://github.com/dokku/dokku) - Docker 驱动的迷你 Heroku。您见过的最小的 PaaS 实施。
* [forgit](https://github.com/wfxr/forgit) - 利用模糊查找器 fzf 的“git”实用工具。
* [git-extra-commands](https://github.com/unixorn/git-extra-commands) - 许多 Git 额外实用程序。搅动、剪切分支、改进合并等等。
* [git-extras](https://github.com/tj/git-extras) - Git 实用程序——repo 摘要、repl、变更日志数量、作者提交百分比等
* [git-open](https://github.com/paulirish/git-open) - 输入“git open”以在浏览器中打开存储库的 GitHub 页面或网站
* [git-quick-stats](https://github.com/arzzen/git-quick-stats) - Git快速统计是一种简单高效的方式来访问git存储库中的各种统计信息。
* [git-semver](https://github.com/markchalloner/git-semver) - 用于简化语义版本控制和变更日志验证的 Git 插件
* [git-sh](https://github.com/rtomayko/git-sh) - 适合Git工作的定制Bash环境
* [gita](https://github.com/nosarthur/gita) - 用于管理多个 git 存储库的命令行工具。
* [hub](https://github.com/github/hub) - Hub 帮助您在 git 上获胜。
* [just](https://github.com/casey/just) - 用于保存和运行项目特定命令的任务运行器。
* [licins](https://github.com/dogoncouch/licins) - 将注释的软件许可证插入源代码中。
* [mkdkr](https://github.com/rosineygp/mkdkr) - Makefile + Docker = CI 管道
* [mr](https://myrepos.branchable.com) - 多存储库管理工具
* [nve](https://github.com/ehmicky/nve) - 在特定 Node.js 版本上运行任何命令。
* [overcommit](https://github.com/sds/overcommit) - 完全可配置且可扩展的 Git 挂钩管理器
* [pre-commit](https://pre-commit.com) - 用于管理和维护多语言预提交挂钩的框架
* [rebound](https://github.com/shobrook/rebound) - 当出现编译器错误时，立即在终端中浏览 Stack Overflow 结果
* [repren](https://github.com/jlevy/repren) - 命令行搜索、替换和文件重命名瑞士军刀
* [slap](https://github.com/slap-editor/slap) - 在 Node.js 上运行的类似 Sublime 的基于终端的文本编辑器
* [shipit](https://github.com/sapegin/shipit) - 简约的 SSH 部署
* [starring](https://github.com/ritz078/starring) - 自动为您在 GitHub 上使用的 npm 包加注星标。
* [tag](https://github.com/aykamko/tag) - 立即跳转到您的 AG 比赛。
* [trunk](https://www.npmjs.com/package/@trunkio/launcher) - 极快的元代码检查器和格式化程序
* [vmn](https://github.com/final-israel/vmn) - 基于 git 的自动版本控制和状态恢复解决方案，与语言或架构无关
* [wipe-modules](https://github.com/bntzio/wipe-modules) - 一个删除非活动项目的node_modules文件夹的小代理

## 系统实用程序

*操作系统相关工具，包括系统管理、系统调试以及文件和进程管理。*

* [atop](https://www.atoptool.nl) - ASCII 全屏性能监视器，能够报告所有进程的活动
* [bat](https://github.com/sharkdp/bat) - 带翅膀的“猫”克隆
* [bmon](https://github.com/tgraf/bmon) - 实时网络带宽监控和速率估计器，具有人性化的视觉输出
* [btop](https://github.com/aristocratos/btop) - Linux/OSX/FreeBSD 资源监视器
* [catcli](https://github.com/deadc0de6/catcli) - 用于离线数据的命令行目录工具
* [ccat](https://github.com/owenthereal/ccat) - ccat 是着色猫。它的工作方式与 cat 类似，但显示带有语法突出显示的内容。
* [exa](https://github.com/ogham/exa) - 现代版本的“ls”。
* [progress](https://github.com/Xfennec/progress) - 显示 `cp`、`rm`、`dd` 等进度的 Linux 工具...
* [stronghold](https://github.com/alichtman/stronghold) - 从终端轻松配置 MacOS 安全设置。
* [glances](https://github.com/nicolargo/glances) - 监视您的系统
* [goaccess](https://github.com/allinurl/goaccess) - GoAccess 是一个实时 Web 日志分析器和交互式查看器，在 \*nix 系统的终端中运行。
* [hblock](https://github.com/hectorm/hblock) - 基于主机文件的广告拦截器
* [histstat](https://github.com/vesche/histstat) - netstat 的历史记录
* [htop](https://github.com/hishamhm/htop) - 基于 ncurses 的交互式进程查看器，旨在成为更好的“top”
* [lnav](https://lnav.org) - 适用于小规模的高级日志文件查看器
* [logdissect](https://github.com/dogoncouch/logdissect) - 用于分析日志文件和其他数据的 CLI 实用程序和 Python API。
* [ls++](https://github.com/trapd00r/ls--) - 彩色 ls 类固醇
* [lsd](https://github.com/Peltoche/lsd) - LSDeluxe，重写了 GNU ls，添加了许多附加功能，如颜色、图标、树视图和更多格式选项。
* [lsp](https://github.com/dborzov/lsp) - 改进的“ls”，具有简单语言的文件描述和智能文件分组
* [maza](https://github.com/tanrax/maza-ad-blocking) - 本地广告拦截器。与 Pi-hole 类似，但位于本地并使用您的操作系统。
* [mtr](https://github.com/traviscross/mtr) - 单个网络诊断工具中的“traceroute”和“ping”程序的功能。
* [ncdu](https://dev.yorhel.nl/ncdu) - NCurses 磁盘使用情况
* [nmtui](https://github.com/NetworkManager/NetworkManager) - 用于控制 NetworkManager 的文本用户界面
* [powertop](https://github.com/fenrus75/powertop) - 电池/电源使用情况和设备统计信息监控命令行工具，带有调整选项。
* [prettyping](https://github.com/denilsonsa/prettyping) - 使“ping”的输出更漂亮、更丰富多彩、更紧凑、更易于阅读。
* [procdog](https://github.com/jlevy/procdog) - 对服务器等长寿命进程的轻量级命令行控制
* [quick-secure](https://github.com/marshyski/quick-secure) - 快速保护和强化 UNIX/Linux 系统
* [rng](https://github.com/nickolasburr/rng) - 将文件或标准输入中的行范围复制到标准输出。
* [tiptop](https://github.com/nschloe/tiptop) - 图形化命令行系统监视器。
* [wifi-wand](https://github.com/keithrbennett/wifiwand) - 用于在 MacOS 上管理 WiFi 的 Ruby 命令行应用程序（通过 `gem install wifi-wand` 安装）
* [xiringuito](https://github.com/ivanilves/xiringuito) - 基于 SSH 的“穷人专用 VPN”

## 下载和服务

*用 shell 脚本编写的自托管、轻量级服务器和网络工具。*

* [aria2](https://github.com/aria2/aria2) - aria2 是一个轻量级的多协议、多源、跨平台下载实用程序，在命令行中运行。它支持 HTTP/HTTPS、FTP、BitTorrent 和 Metalink
* [balls](https://github.com/jneen/balls) - 猛击球
* [bashttpd](https://github.com/avleen/bashttpd) - 用 Bash 编写的 Web 服务器
* [bashhub-server](https://github.com/nicksherron/bashhub-server) - 私有云外壳历史。 bashhub 的开源服务器
* [bitpocket](https://github.com/sickill/bitpocket) - “DIY Dropbox”或“2 路目录（r）同步并正确删除”
* [Dropbox-Uploader](https://github.com/andreafabrizi/Dropbox-Uploader) - Dropbox Uploader 是一个 Bash 脚本，可用于从 Dropbox 上传、下载、列出或删除文件
* [httpie](https://github.com/httpie/httpie) - HTTPie 是一个命令行 HTTP 客户端，一个用户友好的 cURL 替代品
* [HTTPLab](https://github.com/gchaincl/httplab) - 交互式 Web 服务器可让您检查 HTTP 请求并伪造响应。
* [Kapow!](https://github.com/BBVA/kapow) - 如果您可以编写脚本，就可以通过 HTTP 进行处理。
* [ngincat](https://github.com/jaburns/ngincat) - 使用 netcat 的小型 Bash HTTP 服务器
* [resty](https://github.com/micha/resty) - 可以在管道中使用的小型命令行 REST 客户端
* [shell2http](https://github.com/msoap/shell2http) - 用于执行 shell 命令的 HTTP 服务器。专为开发、原型设计或远程控制而设计
* [tshare](https://github.com/trikko/tshare) - 从命令行共享文件。
* [vesper](https://github.com/chris-rock/vesper) - 🍸Vesper 是 Bash/Unix Shell 的 HTTP 框架
* [xh](https://github.com/ducaale/xh) - 用于发送 HTTP 请求的友好且快速的工具
* [yt-dlp](https://github.com/yt-dlp/yt-dlp) - 用于从 YouTube.com 和其他视频网站下载视频的命令行程序

## 多媒体和文件格式

*处理视频和音频文件的工具。*

* [adb-export](https://github.com/sromku/adb-export) - 将 Android 内容提供程序导出为 CSV 格式
* [Android-Kitchen](https://github.com/dsixda/Android-Kitchen) - 用于 Android ROM 定制的基于文本的厨房。使用 shell 脚本并与 Cygwin/OS X/Linux 配合使用
* [Beets](https://github.com/beetbox/beets) - 音乐库管理器和 MusicBrainz 标记器
* [cmus](https://github.com/cmus/cmus) - 跨平台 cli 音频播放器。
* [dasel](https://github.com/tomwright/dasel) - 使用命令行中的选择器查询和更新数据结构。与 [jq](https://github.com/stedolan/jq) / [yq](https://github.com/kislyuk/yq) 相当，但支持 JSON、YAML、TOML 和 XML，且运行时依赖性为零。
* [dzr](https://github.com/yne/dzr) - 跨平台 Deezer.com 音频播放器。
* [fx](https://github.com/antonmedv/fx) - 匿名 JavaScript 函数的命令行 JSON 处理工具
* [gifgen](https://github.com/lukechilds/gifgen) - 简单的高质量 GIF 编码
* [image-scraper](https://github.com/sananth12/ImageScraper) - 一个很酷的命令行图像抓取器，具有很多功能。
* [imgp](https://github.com/jarun/imgp) - 极快的批量图像缩放器和旋转器
* [jc](https://github.com/kellyjonbrazil/jc) - 将命令输出、文件类型和常见字符串转换为 JSON 或 YAML，以便于在脚本中使用。
* [jo](https://github.com/jpmens/jo) - 一个小实用程序，用于从命令行参数创建 JSON 对象。
* [jq](https://github.com/stedolan/jq) - sed 用于 json 数据。您可以使用它来切片、过滤、映射和转换结构化数据
* [korkut](https://github.com/oguzhaninan/korkut) - 在命令行进行快速简单的图像处理。
* [library](https://github.com/chapmanjacobd/library) - 为音乐、视频、图像或在线媒体文件夹创建 SQLITE 数据库。像 Plex 一样播放和跟踪媒体，但仅限 CLI 界面，具有许多排序选项。
* [mpv](https://mpv.io/) - 允许您在 shell 和 GUI 中播放大多数音频和视频格式（使用 ASCII 字符）。
* [nehm](https://github.com/bogem/nehm) - 控制台工具，可以方便地下载、设置 IDv3 标签并添加到您的 SoundCloud 喜欢的 iTunes（如果您使用它）
* [PiCAST](https://github.com/lanceseidman/PiCAST) - PiCAST 将您 35 美元的 Raspberry Pi 变成类似 Chromecast 的设备
* [sejda](https://github.com/torakiki/sejda/) - PDF 文档的命令行操作（拆分、合并、旋转、转换为 jpg、提取文本等）
* [visidata](https://github.com/saulpw/visidata) - 用于探索和整理数据的终端电子表格多功能工具（csv/json/xml/xls/yaml/等）
* [xidel](https://github.com/benibela/xidel/) - 用于使用（图灵完备）XPath 和 XQuery 过滤、映射和创建 HTML/XML/JSON 数据的 Cli 工具。
* [xmlstarlet](http://xmlstar.sourceforge.net/) - 用于命令行 XML 格式化、过滤和操作的古老但功能强大的工具。
* [yq](https://github.com/mikefarah/yq) - yq 是一个便携式命令行 YAML 处理器

## 应用领域

*基于命令行的应用程序或对现有服务的命令行访问。*

* [ansiweather](https://github.com/fcambus/ansiweather) - 终端中的天气，带有 ANSI 颜色和 Unicode 符号
* [awless](https://github.com/wallix/awless) - 用于管理 AWS 的强大、创新和小型表面 CLI。
* [bashblog](https://github.com/cfenollosa/bashblog) - 处理博客发布的 Bash 脚本
* [carbon-now-cli](https://github.com/mixn/carbon-now-cli) - 🎨 美丽的代码图像 - 来自终端内部。
* [choosealicense-cli](https://github.com/lord63/choosealicense-cli) - 从您舒适的终端中选择 OSS 许可证
* [cointop](https://github.com/miguelmota/cointop) - 用于跟踪加密货币的最快、最具交互性的基于终端的 UI 应用程序
* [dstask](https://github.com/naggie/dstask) - 基于单个二进制终端的 TODO 管理器，每个任务具有基于 git 的同步 + Markdown 注释
* [editly](https://github.com/mifi/editly) - 命令行视频编辑器
* [facebook-cli](https://github.com/specious/facebook-cli) - Facebook 命令行工具
* [fanyi](https://github.com/afc163/fanyi) - 在终端中将英文翻译成中文
* [gcalcli](https://github.com/insanum/gcalcli) - Google 日历命令行界面
* [geeknote](https://github.com/VitaliyRodnenko/geeknote) - 命令行印象笔记客户端
* [haxor-news](https://github.com/donnemartin/haxor-news) - 像哈克斯一样浏览黑客新闻
* [hn-cli](https://github.com/rafaelrinaldi/hn-cli) - 从舒适的终端浏览黑客新闻
* [iponmap](https://github.com/nogizhopaboroda/iponmap) - 使用ip地址在世界地图上绘制点
* [isitup](https://github.com/lord63/isitup) - 检查网站是打开还是关闭
* [jrnl](https://github.com/jrnl-org/jrnl) - 一个简单的命令行日记应用程序，将您的日记存储在纯文本文件中
* [kanban.bash](https://github.com/coderofsalvation/kanban.bash) - 用于极简生产力 bash 黑客的命令行 ascii 看板（基于 csv）
* [ledger](https://github.com/ledger/ledger) - 命令行记账
* [licen](https://github.com/lord63/licen) - 生成您的许可证。又一个虱子，但用 Jinja2 和 docopt 实现
* [md2png](https://github.com/weaming/md2png) - 将 markdown 转换为 PNG 图像
* [moviemon](https://github.com/iCHAIT/moviemon) - 有关电影的一切都在命令行中。
* [nomino](https://github.com/yaa110/nomino) - 使用正则表达式、排序和映射文件选项批量重命名实用程序。
* [pcalc](https://github.com/alt-romes/programmer-calculator) - 专为处理多种数字表示形式、大小和整体接近位的程序员而设计的计算器。
* [pockyt](https://github.com/achembarpu/pockyt) - 阅读、管理和自动化您的 [Pocket](https://getpocket.com) 收藏。
* [pushblast](https://github.com/alebcay/pushblast) - 当 shell 程序退出时获取 PushBullet 通知
* [pushbullet-bash](https://github.com/Red5d/pushbullet-bash) - PushBullet API 的 Bash 接口
* [ranger](https://github.com/ranger/ranger) - 具有 VI 键绑定的控制台文件管理器。
* [Reddit Terminal Viewer](https://github.com/michael-lazar/rtv) - 从您的终端浏览 Reddit
* [SAWS](https://github.com/donnemartin/saws) - 强大的 AWS CLI
* [taskbook](https://github.com/klaussinani/taskbook) - 命令行栖息地的任务、看板和注释
* [taskwarrior](https://taskwarrior.org/) - 命令行 TODO 列表管理器
* [terjira](https://github.com/keepcosmos/terjira) - Jira 的命令行强大工具
* [ticker](https://github.com/achannarasappa/ticker) - 具有实时更新和仓位跟踪功能的终端股票报价器
* [vl](https://github.com/ellisonleao/vl) - 文本文档的 URL 链接检查器
* [wego](https://github.com/schachmat/wego) - 终端天气应用程序
* [whales](https://github.com/Gueils/whales) - 自动对应用程序进行 docker 化的工具
* [whereami](https://github.com/rafaelrinaldi/whereami) - 从 CLI 获取您的地理位置信息
* [wttr.in](https://github.com/chubin/wttr.in) - :partly_sunny：查看天气的正确方法 (curl wttr.in)

## 游戏

*只工作不玩耍是度过一天的粗俗方式。*

* [bash2048](https://github.com/mydzor/bash2048) - 2048游戏的Bash实现
* [minesweeper](https://github.com/feherke/Bash-script/tree/master/minesweeper) - 扫雷器的 Bash 实现
* [nudoku](https://github.com/jubalh/nudoku) - 用 C 编写的基于 ncurses 的数独游戏
* [piu-piu](https://github.com/vaniacer/piu-piu-SH) - bash 多人模式水平卷轴游戏！
* [sedtris](https://github.com/uuner/sedtris) - sed 中的俄罗斯方块
* [sed-scripts](https://github.com/aureliojargas/sed-scripts) - 使用 sed 编写的打砖块和推箱子
* [SHTAP](https://notimetoplay.org/engines/shtap/) - Bash 4 可重复使用的文本冒险引擎
* [tty-solitaire](https://github.com/mpereira/tty-solitaire) - 在您的终端上玩纸牌游戏！

## 外壳包管理

*用于管理多个 shell 配置的工具。有关 zsh 特定工具，请参阅 Zsh 部分。*

* [bash-it](https://github.com/Bash-it/bash-it) - 社区 Bash 框架
* [basher](https://github.com/basherpm/basher) - shell 脚本的包管理器
* [bashing](https://github.com/xsc/bashing) - 将猛击打成碎片
* [bpkg](https://www.bpkg.sh/) - JavaScript 有 npm，Ruby 有 Gems，Python 有 pip，现在 Shell 有 bpkg
* [dotdrop](https://github.com/deadc0de6/dotdrop) - 保存点文件一次，将其部署到任何地方
* [dotfiler](https://github.com/svetlyak40wt/dotfiler) - 与 Shell 无关的基于 git 的 dotfiles 包管理器，用 Python 编写。
* [fresh](https://github.com/freshshell/fresh) - 保持你的点文件新鲜
* [homeshick](https://github.com/andsens/homeshick) - 用 Bash 编写的 Git dotfile 同步器
* [shallow-backup](https://github.com/alichtman/shallow-backup) - 轻松创建已安装软件包、点文件等的轻量级文档
* [shundle](https://github.com/javier-lopez/shundle) - shell 脚本的插件管理器
* [vcsh](https://github.com/RichiH/vcsh) - 基于Git的配置管理器
* [yadm](https://yadm.io/) - 基于 Git 的点文件管理器支持加密、替代和引导

## Shell脚本开发

*用于编写、改进或组织 Bash 或其他 shell 脚本的工具*

* [ansi](https://github.com/fidian/ansi) - 纯 bash 中的 ANSI 转义码 - 更改文本颜色、定位光标等等
* [assert.sh](https://github.com/lehmannro/assert.sh) - Bash 单元测试框架
* [bashew](https://github.com/pforret/bashew) - bash 脚本创建器 - 从小型独立脚本到带有 CI/CD 和测试的复杂项目
* [bashful](https://github.com/jmcantrell/bashful) - 用于简化 Bash 脚本编写的库集合
* [Bashlets](https://github.com/reale/bashlets) - Bash 的模块化可扩展工具箱
* [bashly](https://bashly.dannyb.co/) - Bash 命令行框架和 CLI 生成器
* [bashmanager](https://github.com/lingtalfi/bashmanager) - 用于创建命令行工具的迷你 bash 框架
* [bashwithnails](https://github.com/mindaugasbarysas/bashwithnails) - 一个 Bash 框架，只是为了测试、依赖管理和打包的乐趣而编写
* [bash-language-server](https://github.com/bash-lsp/bash-language-server) - [LSP](https://microsoft.github.io/language-server-protocol/)基于Bash语言服务器
* [bash-modules](https://github.com/vlisivka/bash-modules) - 启用[非官方严格模式](http://redsymbol.net/articles/unofficial-bash-strict-mode/)的开发功能。
* [bats](https://github.com/bats-core/bats-core) - Bash自动化测试系统
* [composure](https://github.com/erichs/composure) - 编写、记录、版本化和组织您的 shell 函数
* [crash](https://github.com/molovo/crash) - ZSH 的正确错误处理、异常和 try/catch
* [critic.sh](https://github.com/Checksum/critic.sh) - 非常简单的 Bash 测试框架，带有覆盖率报告
* [dispatch](https://github.com/Mosai/workshop/blob/master/doc/dispatch.md) - 50 行可移植 shell 脚本中的命令行参数解析器。
* [esh](https://github.com/jirutka/esh) - 一个基于 shell 的简单模板引擎，用约 290 行 POSIX shell 和 awk 实现。
* [Fishtape](https://github.com/jorgebucaran/fishtape) - TAP 生产商和鱼类测试装置
* [getoptions](https://github.com/ko1nksm/getoptions) - 一个优雅的 shell 脚本选项解析器（sh、bash 和所有 POSIX shell）
* [getopts.fish](https://github.com/jorgebucaran/getopts.fish) - 鱼的 CLI 解析器
* [is.sh](https://github.com/qzb/is.sh) - 内置测试命令的替代方案，它将使您的“if”语句变得漂亮
* [lumberjack](https://github.com/molovo/lumberjack) - shell 脚本的日志记录接口
* [mo](https://github.com/tests-always-included/mo) - 纯 bash 中的胡子模板
* [optparse](https://github.com/nk412/optparse) - getopts 的 BASH 包装器，用于简单的命令行参数。
* [rerun](https://github.com/rerun/rerun) - 用于组织 keeper 脚本的模块化 shell 自动化框架
* [revolver](https://github.com/molovo/revolver) - shell 脚本的可重用进度旋转器
* [phases](https://github.com/sorokine/phases) - 微创 bash 预处理器，选择要运行的脚本部分
* [powscript](https://github.com/coderofsalvation/powscript) - 用 bash 编写的 bash 转译器（coffeescript for bash）
* [semver_bash](https://github.com/cloudflare/semver_bash) - Bash 中的语义版本控制
* [sh-semver](https://github.com/qzb/sh-semver) - 用于 bash 的 Semver 工具 - 查找与指定规则匹配的版本
* [shellcheck](https://github.com/koalaman/shellcheck) - shell脚本静态分析工具
* [shellfire](https://github.com/shellfire-dev/shellfire) - 命名空间、可组合 shell（bash、sh 和 dash）函数库的存储库
* [shellspec](https://github.com/shellspec/shellspec) - 适用于 dash、bash、ksh、zsh 和所有 POSIX shell 的全功能 BDD 单元测试框架
* [shfmt](https://github.com/mvdan/sh) - 支持 bash 的 shell 解析器、格式化程序和解释器；包括转移
* [shpec](https://github.com/rylnd/shpec) - 一个shell测试框架
* [shutit](https://ianmiell.github.io/shutit/) - 基于bash和pexpect的自动化框架
* [sub](https://github.com/basecamp/sub) - 一种组织节目的美味方式
* [ts](https://github.com/thinkerbot/ts) - shell测试脚本
* [urchin](https://github.com/tlevine/urchin) - 仅使用 shell 命令的惯用 shell 测试框架
* [shunit2](https://github.com/kward/shunit2) - 具有 JUnit/PyUnit 风格的 Bash 脚本单元测试框架。
* [rebash](https://github.com/jandob/rebash) - 脚本库/框架。功能：导入、例外、文档测试...
* [zunit](https://github.com/zunit-zsh/zunit) - 强大的 ZSH 单元测试框架

# 指南

* [Bash 官方参考手册](https://www.gnu.org/savannah-checkouts/gnu/bash/manual/bash.html)
* [Bash 黑客维基](https://web.archive.org/web/20230406205817/https://wiki.bash-hackers.org/)
* [Greg Wooledge 的（又名“灰猫”）wiki](https://mywiki.wooledge.org)。
具体来说，[Bash 指南](https://mywiki.wooledge.org/BashGuide)、[Bash 常见问题解答](https://mywiki.wooledge.org/BashFAQ) 和 [Bash 陷阱](https://mywiki.wooledge.org/BashPitfalls)
* [Google 的 Shell 风格指南](https://google.github.io/styleguide/shell.xml)
* [Linux 文档项目：Bash 编程 - 简介/操作方法](https://tldp.org/HOWTO/Bash-Prog-Intro-HOWTO.html)
* [Linux 文档项目：高级 Bash 脚本指南](https://tldp.org/LDP/abs/html/)
* [维基百科：Bash Shell 脚本](https://en.wikibooks.org/wiki/Bash_Shell_Scripting)
* [使用非官方的 Bash 严格模式（除非您喜欢调试）](http://redsymbol.net/articles/unofficial-bash-strict-mode/)
* [命令行的艺术](https://github.com/jlevy/the-art-of-command-line)
* [命令行学得够多就很危险](https://www.learnenough.com/command-line-tutorial/basics)
* [bash 学习指南](https://github.com/Idnan/bash-guide)
* [壳牌现场指南](https://raimonster.com/scripting-field-guide/)

# 其他很棒的列表

其他令人惊叹的很棒的列表可以在 [awesome-awesome](https://github.com/emijrp/awesome-awesome) 和 [awesome-awesomeness](https://github.com/bayandin/awesome-awesomeness) 中找到。

### 另请参阅

* [awesome-cli-apps](https://github.com/agarrharr/awesome-cli-apps)
* [真棒鱼][真棒鱼]
* [真棒-zsh][真棒-zsh]
* [真棒-bash][真棒-bash]
* [terminals-are-sexy](https://github.com/k4m4/terminals-are-sexy)

[真棒徽章]：https://raw.githubusercontent.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg
[真棒鱼]：https://github.com/jorgebucaran/awsm.fish
[很棒的链接]：https://github.com/sindresorhus/awesome
[awesome-zsh]：https://github.com/unixorn/awesome-zsh-plugins
[真棒bash]：https://github.com/awesome-lists/awesome-bash
