<h1对齐=“中心”>
  <a href="https://git-scm.com/">
  <img width="455" src="https://github.com/compscilauren/awesome-git-hooks/blob/master/git-logo.png" alt="Awesome Git Hooks"></a><br>Awesome Git Hooks
</h1>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome Lists"></a>
  <a href="https://github.com/CompSciLauren/awesome-git-hooks/blob/master/CONTRIBUTING.md"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square" alt="PRs welcome"></a>
</p>

# 很棒的 Git Hooks

> :anchor：易于使用的 Git 挂钩，用于在 Git 工作流程中自动执行任务。

Git 挂钩是自定义脚本，可用于自动执行 Git 命令之前或之后触发的任务。这些钩子有两组：客户端和服务器端。客户端钩子由提交和合并等操作触发，而服务器端钩子在网络操作上运行，例如接收推送的提交。该存储库包含有用的资源以及各种可以轻松自定义以服务于不同目的的 Git 挂钩脚本。

:heavy_check_mark: 没有什么可安装/下载的

:heavy_check_mark: 代码有详细记录

:heavy_check_mark: 拿起来就走！复制您要使用的代码并粘贴到您的 .git/hooks 文件夹中

_永远_欢迎贡献！请参阅我们的[贡献指南](CONTRIBUTING.md)。另外，如果您在下面找不到所需的脚本，您可以[创建一个新问题](https://github.com/CompSciLauren/awesome-git-hooks/issues/new?assignees=&labels=enhancement&template=new-git-hook-script-request.md&title=)来请求它。

## 内容

- [Git 挂钩脚本](#git-hook-scripts)
  - [commit-msg](#commit-msg)
  - [post-checkout](#post-checkout)
  - [post-update](#post-update)
  - [pre-commit](#pre-commit)
  - [prepare-commit-msg](#prepare-commit-msg)
  - [pre-push](#pre-push)
  - [pre-rebase](#pre-rebase)
  - [query-watchman](#query-watchman)
  - [update](#update)
- [快速入门](#quick-start)
- [Tools](#tools)
- [书面指南](#written-guides)
- [视频指南](#video-guides)

## Git 挂钩脚本

注意：每个脚本旁边的图标表示它是用什么语言编写的。

|图标|语言 |
| -------------------------------------------------------- | -------- |
| <img width="14" src="bash-icon.png" alt="Bash 图标"> | `bash` |
| <img width="14" src="python-icon.png" alt="Python 图标"> | `蟒蛇` |
| <img width="14" src="perl-icon.png" alt="Perl 图标"> | `perl` |

### 提交消息

- [enforce-insert-issue-number](https://github.com/CompSciLauren/awesome-git-hooks/blob/master/commit-msg-hooks/enforce-insert-issue-number.hook) - 确保用户没有删除由prepare-commit-msg/insert-issue-number.hook生成的ISSUE-\[#]字符串。 <img width="14" src="python-icon.png" alt="Python 图标">

### 结账后

- [delete-pyc-files](https://github.com/CompSciLauren/awesome-git-hooks/blob/master/post-checkout-hooks/delete-pyc-files.hook) - 每次签出新分支时删除所有 .pyc 文件。 <img width="14" src="python-icon.png" alt="Python 图标">
- [new-branch-alert](https://github.com/CompSciLauren/awesome-git-hooks/blob/master/post-checkout-hooks/new-branch-alert.hook) - 首次签出新分支时显示一条消息。 <img width="14" src="bash-icon.png" alt="Bash 图标">

### 更新后

- [update-server-info](https://github.com/CompSciLauren/awesome-git-hooks/blob/master/post-update-hooks/update-server-info.hook) - 准备一个打包的存储库以通过哑传输（例如http）使用。 <img width="14" src="bash-icon.png" alt="Bash 图标">

### 预提交

- [dotenvx](https://github.com/CompSciLauren/awesome-git-hooks/blob/master/pre-commit-hooks/dotenvx.hook) - 防止将“.env”文件提交到代码中。 <img width="14" src="bash-icon.png" alt="Bash 图标">
- [format-code](https://github.com/CompSciLauren/awesome-git-hooks/blob/master/pre-commit-hooks/format-code.hook) - 运行命令格式化代码并重新添加格式化后修改的所有文件。 <img width="14" src="bash-icon.png" alt="Bash 图标">
- [search-term](https://github.com/CompSciLauren/awesome-git-hooks/blob/master/pre-commit-hooks/search-term.hook) - 如果在代码中找到特定术语，则提交失败。 <img width="14" src="bash-icon.png" alt="Bash 图标">
- [spell-check-md-files](https://github.com/CompSciLauren/awesome-git-hooks/blob/master/pre-commit-hooks/spell-check-md-files.hook) - 检查扩展名为 .md 的文件是否存在拼写错误。 <img width="14" src="bash-icon.png" alt="Bash 图标">
- [verify-name-and-email](https://github.com/CompSciLauren/awesome-git-hooks/blob/master/pre-commit-hooks/verify-name-and-email.hook) - 如果 user.name 或 user.email 不正确，则提交失败。 <img width="14" src="bash-icon.png" alt="Bash 图标">

### 准备-提交-消息

- [include-git-diff-name-status](https://github.com/CompSciLauren/awesome-git-hooks/blob/master/prepare-commit-msg-hooks/include-git-diff-name-status.hook) - 将“Git diff --name-status -r”的输出包含到消息中，位于“Git status”输出之前。 <img width="14" src="bash-icon.png" alt="Bash 图标">
- [insert-issue-number](https://github.com/CompSciLauren/awesome-git-hooks/blob/master/prepare-commit-msg-hooks/insert-issue-number.hook) - 将问题编号插入提交消息的开头。 <img width="14" src="python-icon.png" alt="Python 图标">

### 预推

- [prevent-bad-push](https://github.com/CompSciLauren/awesome-git-hooks/blob/master/pre-push-hooks/prevent-bad-push.hook) - 防止推送日志消息以“WIP”（正在进行的工作）开头的提交。 <img width="14" src="bash-icon.png" alt="Bash 图标">

### 预变基

- [prevent-rebase](https://github.com/CompSciLauren/awesome-git-hooks/blob/master/pre-rebase-hooks/prevent-rebase.hook) - 防止已合并到“下一个”分支的主题分支被重新定基，因为允许它会导致重新定基已经发布的历史记录。 <img width="14" src="bash-icon.png" alt="Bash 图标">

### 查询守望者

- [fsmonitor-watchman](https://github.com/CompSciLauren/awesome-git-hooks/blob/master/query-watchman-hooks/fsmonitor-watchman.hook) - 输出到 stdout 自给定时间以来已修改的所有文件。 <img width="14" src="perl-icon.png" alt="Perl 图标">

### 更新

- [update](https://github.com/CompSciLauren/awesome-git-hooks/blob/master/update-hooks/prevent-unannotated-tags.hook) - 阻止未注释的标签进入。 <img width="14" src="bash-icon.png" alt="Bash 图标">

## 快速入门

1. 选择一个钩子，任何钩子！如果您不确定从哪里开始，请尝试“验证姓名和电子邮件”。
2. 导航到项目的 hooks 文件夹 (.git/hooks)。
3. 您应该会看到其中已有的文件列表。创建一个名为您要使用的确切提交类型的新文件（例如：“commit-msg”、“pre-rebase”、“pre-commit”等）。不要给它延期。

![创建新文件](create-new-file.gif)

4. 打开新文件并粘贴您从此存储库中选择的挂钩中的代码（例如：[verify-name-and-email.hook](https://github.com/CompSciLauren/git-hooks/blob/master/pre-commit-hooks/verify-name-and-email.hook)）。
5. 保存文件。完毕！现在Git钩子将被自动触发。

## 工具

- [Husky](https://github.com/typicode/husky) - 使用漂亮的用户界面管理 Git 挂钩。

- [Overcommit](https://github.com/sds/overcommit) - 完全可配置且可扩展的 Git 挂钩管理器。

- [Git Build Hook Maven Plugin](https://github.com/rudikershaw/git-build-hook) - 在 Maven 构建期间安装 Git 挂钩和配置。

- [CaptainHook](https://github.com/CaptainHookPhp/captainhook) - PHP 开发人员的 Git hooks 管理器。

- [pre-commit](https://github.com/pre-commit/pre-commit) - 用于管理和维护多语言预提交挂钩的框架。

## 书面指南

- [Git hooks 文档位于 git-scm.com](https://git-scm.com/docs/githooks)

- [Scott Chacon 和 Ben Straub 撰写的 Git Pro 书籍](https://git-scm.com/book/en/v2)

- [Git Hook 简介](https://www.sitepoint.com/introduction-git-hooks/)

- [Atlassian Git Hooks 教程](https://www.atlassian.com/ru/git/tutorials/git-hooks)

- [简单的 Git 与 husky 挂钩](https://www.vojtechruzicka.com/githooks-husky/)

- [上瘾的 Git](https://www.javascriptjanuary.com/blog/git-hooked 'Git Hooked')

- [如何使用 Git Hooks 自动化开发和部署任务](https://www.digitalocean.com/community/tutorials/how-to-use-git-hooks-to-automate-development-and-deployment-tasks)

- [使用 Git Hooks 自动化您的工作流程](https://hackernoon.com/automate-your-workflow-with-git-hooks-fef5d9b2a58c)

- [在 Git Hook 中使用 JavaScript](https://medium.com/@Sergeon/using-javascript-in-your-git-hooks-f0ce09477334 'Using JavaScript in Your Git Hooks')

- [深入了解 Git Hooks](https://dzone.com/articles/an-in-depth-look-at-git-hooks)

- [Git 挂钩和实际用途。是的，即使在 Windows 上也是如此。](https://www.tygertec.com/git-hooks-practical-uses-windows/)

- [使用 Direnv 自动管理 Git Hooks](https://knpw.rs/blog/direnv-git-hooks)

## 视频指南

- [Git Hooks 第 1 部分 - 入门](https://www.youtube.com/watch?v=aB3eq52sZSU)

- [Git 挂钩和实际用途。是的，即使在 Windows 上也是如此。](http://www.youtube.com/watch?feature=player_embedded&v=fMYv6-SZsSo&t=140s)

## 执照

[![CC0](http://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)<br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/1.0/">Creative Commons Attribution 1.0 International License</a>.
