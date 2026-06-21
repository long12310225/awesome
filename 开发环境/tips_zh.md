## git 提示
> `git-tips` 集合，想添加您的提示吗？查看 [contributing.md](./contributing.md)

[English](http://git.io/git-tips) | [中文](https://github.com/521xueweihan/git-tips) | [Русский](https://github.com/Imangazaliev/git-tips) | [한국어](https://github.com/mingrammer/git-tips) | [Tiếng Việt](https://github.com/hprobotic/git-tips) | [日本語](https://github.com/isotai/git-tips) | [नेपाली](https://github.com/amarduwal/git-tips) | [Polski](https://github.com/mbiesiad/tips) | [فارسی](https://github.com/javadnikbakht/git-tips)

### __工具：__

* [git-tip](https://www.npmjs.com/package/git-tip) - 一个方便的 CLI 可以充分利用这些技巧。 （[在 Docker 容器中](https://github.com/djoudi5/docker-git-tip)）

📖 **[在这里阅读交互式 GitBook 文档！](https://git-tips.github.io/tips/)**

P.S: 所有这些命令都在 `git version 2.7.4 (Apple Git-66)` 上测试。

## 目录

* [基本操作](#basic-operations)
  * [提交之前的所有文件列表](#list-of-all-files-till-a-commit)
  * [快速切换到上一个分支](#quickly-switch-to-the-previous-branch)
  * [删除远程分支](#delete-remote-branch)
  * [删除远程标签](#delete-remote-tag)
  * [使用索引中的内容撤消本地更改（暂存）](#undo-local-changes-with-the-content-in-indexstaging)
  * [重写之前的提交消息](#reword-the-previous-commit-message)
  * [仅查看当前分支的提交历史记录](#see-commit-history-for-just-the-current-branch)
  * [修改作者。](#amend-author)
  * [暂存已更改文件的部分内容，而不是整个文件](#stage-parts-of-a-changed-file-instead-of-the-entire-file)
  * [使用cherry-pick跨分支选择提交](#pick-commits-across-branches-using-cherry-pick)
  * [从存储中获取单个文件](#grab-a-single-file-from-a-stash)
  * [从存储库创建新的工作树（git 2.5）](#create-new-working-tree-from-a-repository-git-25)
  * [从 HEAD 状态创建新的工作树](#create-new-working-tree-from-head-state)
  * [显示当前分支中尚未合并到 master 的所有提交](#show-all-commits-in-the-current-branch-yet-to-be-merged-to-master)
  * [修改之前的提交而不修改提交消息](#modify-previous-commit-without-modifying-the-commit-message)
  * [修剪引用以删除已在远程中删除的分支。](#prunes-references-to-remove-branches-that-have-been-deleted-in-the-remote)
  * [检索初始修订版的提交哈希值。](#retrieve-the-commit-hash-of-the-initial-revision)
  * [从捆绑包导入](#import-from-a-bundle)
  * [提交时忽略一个文件（例如更改日志）。](#ignore-one-file-on-commit-eg-changelog)
  * [按 ID 提取拉取请求到本地分支](#fetch-pull-request-by-id-to-a-local-branch)
  * [恢复已删除的文件。](#restore-deleted-file)
  * [将文件恢复到特定的提交哈希](#restore-file-to-a-specific-commit-hash)
  * [将您的提交标记为先前提交的修复。](#marks-your-commit-as-a-fix-of-a-previous-commit)
  * [提交期间跳过暂存区域。](#skip-staging-area-during-commit)
  * [互动舞台。](#interactive-staging)
  * [被忽略文件的状态。](#status-of-ignored-files)
  * [签出没有任何历史记录的新分支](#checkout-a-new-branch-without-any-history)
  * [通过二分查找来判罪](#find-guilty-with-binary-search)
  * [绕过预提交和 commit-msg githooks](#bypass-pre-commit-and-commit-msg-githooks)
  * [克隆单个分支](#clone-a-single-branch)
  * [创建并切换新分支](#create-and-switch-new-branch)
  * [显示按最近提交排序的所有本地分支](#show-all-local-branches-ordered-by-recent-commits)
  * [克隆存储库的浅表副本](#clone-a-shallow-copy-of-a-repository)
  * [强制推送到远程存储库](#force-push-to-remote-repository)
  * [按作者和标题分组提交](#group-commits-by-authors-and-title)
  * [强制推送但仍确保您不会覆盖其他人的工作](#forced-push-but-still-ensure-you-dont-overwrite-others-work)
  * [分支中的提交数](#number-of-commits-in-a-branch)
  * [添加对象注释](#add-object-notes)
  * [从另一个存储库应用提交](#apply-commit-from-another-repository)
  * [具体获取参考](#specific-fetch-reference)
  * [生成待处理更改的摘要](#generates-a-summary-of-pending-changes)
  * [显示 git 状态简短](#show-git-status-short)
  * [签出一天前的提交](#checkout-a-commit-prior-to-a-day-ago)
  * [将当前分支推送到远程存储库上的同名分支](#push-the-current-branch-to-the-same-name-on-the-remote-repository)
  * [将新的本地分支推送到远程存储库并跟踪](#push-a-new-local-branch-to-remote-repository-and-track)
  * [将子模块更新到最新提交](#update-a-submodule-to-the-latest-commit)
  * [复制存储库](#duplicating-a-repository)
* [Branching](#branching)
  * [列出所有已经合并到master的分支](#list-all-branches-that-are-already-merged-into-master)
  * [删除已经与master合并的分支](#remove-branches-that-have-already-been-merged-with-master)
  * [列出所有分支及其上游，以及分支上的最后一次提交](#list-all-branches-and-their-upstreams-as-well-as-last-commit-on-branch)
  * [跟踪上游分支](#track-upstream-branch)
  * [删除本地分支](#delete-local-branch)
  * [获取所有本地和远程分支的列表](#get-list-of-all-local-and-remote-branches)
  * [仅获取远程分支](#get-only-remote-branches)
  * [找出包含commit-hash的分支](#find-out-branches-containing-commit-hash)
  * [重命名分支](#rename-a-branch)
  * [归档“master”分支](#archive-the-master-branch)
  * [删除已压缩并合并到远程的本地分支。](#delete-local-branches-that-has-been-squash-and-merged-in-the-remote)
  * [将具有历史记录的分支导出到文件。](#export-a-branch-with-history-to-a-file)
  * [获取当前分支的名称。](#get-the-name-of-current-branch)
  * [显示当前分支上的最新标签。](#show-the-most-recent-tag-on-the-current-branch)
  * [列出所有正在开发的分支](#list-all-branch-is-wip)
  * [预格式化的补丁文件。](#preformatted-patch-file)
  * [切换到分支（结帐的现代替代方案）](#switch-to-a-branch-modern-alternative-to-checkout)
* [日志和历史](#log-and-history)
  * [显示 Git 附带的有用指南](#show-helpful-guides-that-come-with-git)
  * [按内容搜索变化](#search-change-by-content)
  * [显示特定文件随时间的变化](#show-changes-over-time-for-specific-file)
  * [列出所有冲突的文件](#list-all-the-conflicted-files)
  * [提交中更改的所有文件的列表](#list-of-all-files-changed-in-a-commit)
  * [自上次提交以来未暂存的更改](#unstaged-changes-since-last-commit)
  * [为提交而进行的更改](#changes-staged-for-commit)
  * [显示已分阶段和未分阶段的更改](#show-both-staged-and-unstaged-changes)
  * [两周以来发生了什么变化？](#what-changed-since-two-weeks)
  * [查看自 master 分叉以来所做的所有提交](#see-all-commits-made-since-forking-from-master)
  * [显示所有跟踪的文件](#show-all-tracked-files)
  * [显示所有未跟踪的文件](#show-all-untracked-files)
  * [显示所有被忽略的文件](#show-all-ignored-files)
  * [可视化版本树。](#visualize-the-version-tree)
  * [可视化树，包括仅从引用日志引用的提交](#visualize-the-tree-including-commits-that-are-only-referenced-from-reflogs)
  * [显示内联单词差异。](#show-inline-word-diff)
  * [使用常见的差异工具显示更改。](#show-changes-using-common-diff-tools)
  * [Branch1 中的提交不在 Branch2 中](#commits-in-branch1-that-are-not-in-branch2)
  * [列出 n 个最后提交](#list-n-last-commits)
  * [在编辑器中打开所有冲突的文件。](#open-all-conflicted-files-in-an-editor)
  * [查看提交日志中的 GPG 签名](#view-the-gpg-signatures-in-the-commit-log)
  * [从另一个分支提取文件。](#extract-file-from-another-branch)
  * [仅列出根提交和合并提交。](#list-only-the-root-and-merge-commits)
  * [列出对特定文件的提交和更改（甚至通过重命名）](#list-commits-and-changes-to-a-specific-file-even-through-renaming)
  * [在所有分支中搜索提交日志中的给定文本](#search-commit-log-across-all-branches-for-given-text)
  * [获取分支中的第一次提交（来自 master）](#get-first-commit-in-a-branch-from-master)
  * [显示给定文件每一行的作者、时间和最后修订](#show-the-author-time-and-last-revision-made-to-each-line-of-a-given-file)
  * [显示作者贡献了多少行](#show-how-many-lines-does-an-author-contribute)
  * [显示所有 git-notes](#show-all-the-git-notes)
  * [列出未推送的 git 提交](#list-unpushed-git-commits)
  * [添加所有内容，但空白会改变](#add-everything-but-whitespace-changes)
  * [归咎于一定范围](#blame-on-certain-range)
  * [显示 Git 逻辑变量。](#show-a-git-logical-variable)
  * [获取存储库名称。](#get-the-repo-name)
  * [日期范围之间的日志](#logs-between-date-range)
  * [从日志中排除作者](#exclude-author-from-logs)
  * [查看上次提交中更改的扩展详细信息](#view-expanded-details-of-changes-in-last-commit)
  * [可视化过去 30 天内 HEAD 的每个位置](#visualize-each-position-of-head-in-the-last-30-days)
* [合并和变基](#merging-and-rebasing)
  * [将“feature”变基为“master”并将其合并到 master ](#rebases-feature-to-master-and-merges-it-in-to-master-)
  * [变基前存储更改](#stash-changes-before-rebasing)
  * [Squash 修复提交正常提交。](#squash-fixup-commits-normal-commits)
  * [使用交互式变基更改前​​两次提交。](#change-previous-two-commits-with-an-interactive-rebase)
  * [找到两个分支的共同祖先](#find-common-ancestor-of-two-branches)
  * [更改分支基地](#change-a-branch-base)
* [Miscellaneous](#miscellaneous)
  * [日常使用 20 个左右的 Git 命令](#everyday-git-in-twenty-commands-or-so)
  * [取消跟踪文件而不删除](#untrack-files-without-deleting)
  * [不考虑跟踪文件的更改。](#dont-consider-changes-for-tracked-file)
  * [检查更改是否是版本的一部分。](#check-if-the-change-was-a-part-of-a-release)
  * [列出被忽略的文件。](#list-ignored-files)
  * [计算已解压的对象数量及其磁盘消耗。](#count-unpacked-number-of-objects-and-their-disk-consumption)
  * [从对象数据库中删除所有无法访问的对象。](#prune-all-unreachable-objects-from-the-object-database)
  * [立即浏览 gitweb 中的工作存储库。](#instantly-browse-your-working-repository-in-gitweb)
  * [在跟踪文件中查找与模式（正则表达式或字符串）匹配的行](#find-lines-matching-the-pattern-regex-or-string-in-tracked-files)
  * [备份未跟踪的文件。](#backup-untracked-files)
  * [以电子邮件的形式发送补丁集合](#send-a-collection-of-patches-as-emails)
* [Remotes](#remotes)
  * [更改远程 URL](#changing-a-remotes-url)
  * [获取所有远程引用的列表](#get-list-of-all-remote-references)
  * [添加远程名称](#adding-remote-name)
  * [列出所有当前配置的遥控器](#list-all-currently-configured-remotes)
  * [列出远程存储库中的引用](#list-references-in-a-remote-repository)
  * [刷新远程分支列表](#refresh-the-list-of-remote-branches)
* [设置和配置](#setup-and-config)
  * [推送后从历史记录中删除敏感数据](#remove-sensitive-data-from-history-after-a-push)
  * [在全局配置中更改作者后重置作者。](#reset-author-after-author-has-been-changed-in-the-global-config)
  * [获取 git bash 补全](#get-git-bash-completion)
  * [Git 别名](#git-aliases)
  * [始终变基而不是拉取时合并。](#always-rebase-instead-of-merge-on-pull)
  * [列出所有别名和配置。](#list-all-the-alias-and-configs)
  * [使 git 区分大小写。](#make-git-case-sensitive)
  * [添加自定义编辑器。](#add-custom-editors)
  * [自动更正拼写错误。](#auto-correct-typos)
  * [重用记录的解决方案，记录并重用以前的冲突解决方案。](#reuse-recorded-resolution-record-and-reuse-previous-conflicts-resolutions)
  * [删除全局配置中的条目。](#remove-entry-in-the-global-config)
  * [忽略提交时的文件模式更改](#ignore-file-mode-changes-on-commits)
  * [关闭 git 彩色终端输出](#turn-off-git-colored-terminal-output)
  * [具体颜色设置](#specific-color-settings)
  * [别名：git 撤消](#alias-git-undo)
* [编辑[本地/全局] git 配置](#edit-localglobal-git-config)
  * [列出所有 git 别名](#list-all-git-aliases)
  * [对远程服务器使用 SSH 而不是 HTTP](#use-ssh-instead-of-https-for-remotes)
  * [防止自动将 LF 替换为 CRLF](#prevent-auto-replacing-lf-with-crlf)
  * [编辑每个级别的配置](#edit-config-for-each-level)
* [Stashing](#stashing)
  * [保存跟踪文件的当前状态而不提交](#saving-current-state-of-tracked-files-without-committing)
  * [将未暂存更改的当前状态保存到跟踪文件](#saving-current-state-of-unstaged-changes-to-tracked-files)
  * [保存当前状态，包括未跟踪的文件](#saving-current-state-including-untracked-files)
  * [使用消息保存当前状态](#saving-current-state-with-message)
  * [保存所有文件的当前状态（忽略、未跟踪和跟踪）](#saving-current-state-of-all-files-ignored-untracked-and-tracked)
  * [显示所有已保存存储的列表](#show-list-of-all-saved-stashes)
  * [以补丁形式显示任何存储的内容](#show-the-contents-of-any-stash-in-patch-form)
  * [应用任何隐藏，而不从隐藏列表中删除](#apply-any-stash-without-deleting-from-the-stashed-list)
  * [应用最后的隐藏状态并将其从隐藏列表中删除](#apply-last-stashed-state-and-delete-it-from-stashed-list)
  * [删除所有存储的存储](#delete-all-stored-stashes)
* [子模块和子树](#submodules-and-subtrees)
  * [更新所有子模块](#update-all-the-submodules)
  * [将 git tracked 子文件夹部署到 gh-pages](#deploying-git-tracked-subfolder-to-gh-pages)
  * [使用子树将项目添加到存储库](#adding-a-project-to-repo-using-subtree)
  * [使用子树获取链接项目的存储库中的最新更改](#get-latest-changes-in-your-repo-for-a-linked-project-using-subtree)
* [Tagging](#tagging)
  * [创建本地标签](#create-local-tag)
  * [删除本地标签](#delete-local-tag)
* [撤消更改](#undoing-changes)
  * [与远程同步，覆盖本地更改](#sync-with-remote-overwrite-local-changes)
  * [Git 重置第一次提交](#git-reset-first-commit)
  * [重置：保留未提交的本地更改](#reset-preserve-uncommitted-local-changes)
  * [恢复：通过创建新提交来撤消提交](#revert-undo-a-commit-by-creating-a-new-commit)
  * [重置：放弃提交，建议用于私有分支](#reset-discard-commits-advised-for-private-branch)
  * [在删除未跟踪的文件/目录之前，请进行一次试运行以获取这些文件/目录的列表](#before-deleting-untracked-filesdirectory-do-a-dry-run-to-get-the-list-of-these-filesdirectories)
  * [强制删除未跟踪的文件](#forcefully-remove-untracked-files)
  * [强制删除未跟踪的目录](#forcefully-remove-untracked-directory)
  * [撤消假设不变。](#undo-assume-unchanged)
  * [清除“.gitignore”中的文件。](#clean-the-files-from-gitignore)
  * [试运行。 （任何支持试运行标志的命令都应该这样做。）](#dry-run-any-command-that-supports-dry-run-flag-should-do)
  * [取消暂存暂存文件](#unstaging-staged-file)
  * [恢复：恢复整个合并](#revert-reverting-an-entire-merge)
  * [恢复文件（重置/签出的现代替代方案--）](#restore-file-modern-alternative-to-resetcheckout---)

## 基本操作

### 提交之前的所有文件列表
```sh
git ls-tree --name-only -r <commit-ish>
```

### 快速切换到上一个分支
```sh
git checkout -
```
**替代方案：**
```sh
git checkout @{-1}
```

### 删除远程分支
```sh
git push origin --delete <remote_branchname>
```
**替代方案：**
```sh
git push origin :<remote_branchname>
```
```sh
git branch -dr <remote/branch>
```

### 删除远程标签
```sh
git push origin :refs/tags/<tag-name>
```

### 使用索引中的内容撤消本地更改（暂存）
```sh
git checkout -- <file_name>
```

### 重写之前的提交消息
```sh
git commit -v --amend
```

### 仅查看当前分支的提交历史记录
```sh
git cherry -v master
```

### 修改作者。
```sh
git commit --amend --author='Author Name <email@address.com>'
```

### 暂存已更改文件的部分内容，而不是整个文件
```sh
git add -p
```

### 使用cherry-pick跨分支选择提交
```sh
git checkout <branch-name> && git cherry-pick <commit-ish>
```

### 从存储中获取单个文件
```sh
git checkout <stash@{n}> -- <file_path>
```
**替代方案：**
```sh
git checkout stash@{0} -- <file_path>
```

### 从存储库创建新的工作树（git 2.5）
```sh
git worktree add -b <branch-name> <path> <start-point>
```

### 从 HEAD 状态创建新的工作树
```sh
git worktree add --detach <path> HEAD
```

### 显示当前分支中尚未合并到 master 的所有提交
```sh
git cherry -v master
```
**替代方案：**
```sh
git cherry -v master <branch-to-be-merged>
```

### 修改之前的提交而不修改提交消息
```sh
git add --all && git commit --amend --no-edit
```

### 修剪引用以删除已在远程中删除的分支。
```sh
git fetch -p
```
**替代方案：**
```sh
git remote prune origin
```

### 检索初始修订版的提交哈希值。
```sh
 git rev-list --reverse HEAD | head -1
```
**替代方案：**
```sh
git rev-list --max-parents=0 HEAD
```
```sh
git log --pretty=oneline | tail -1 | cut -c 1-40
```
```sh
git log --pretty=oneline --reverse | head -1 | cut -c 1-40
```

### 从捆绑包导入
```sh
git clone repo.bundle <repo-dir> -b <branch-name>
```

### 提交时忽略一个文件（例如更改日志）。
```sh
git update-index --assume-unchanged Changelog; git commit -a; git update-index --no-assume-unchanged Changelog
```

### 按 ID 提取拉取请求到本地分支
```sh
git fetch origin pull/<id>/head:<branch-name>
```
**替代方案：**
```sh
git pull origin pull/<id>/head:<branch-name>
```

### 恢复已删除的文件。
```sh
git checkout <deleting_commit> -- <file_path>
```

### 将文件恢复到特定的提交哈希
```sh
git checkout <commit-ish> -- <file_path>
```

### 将您的提交标记为先前提交的修复。
```sh
git commit --fixup <SHA-1>
```

### 提交期间跳过暂存区域。
```sh
git commit --only <file_path>
```

### 互动舞台。
```sh
git add -i
```

### 被忽略文件的状态。
```sh
git status --ignored
```

### 签出没有任何历史记录的新分支
```sh
git checkout --orphan <branch_name>
```

### 通过二分查找来判罪
```sh
git bisect start                    # Search start 
git bisect bad                      # Set point to bad commit 
git bisect good v2.6.13-rc2         # Set point to good commit|tag 
git bisect bad                      # Say current state is bad 
git bisect good                     # Say current state is good 
git bisect reset                    # Finish search 

```

### 绕过预提交和 commit-msg githooks
```sh
git commit --no-verify
```

### 克隆单个分支
```sh
git clone -b <branch-name> --single-branch https://github.com/user/repo.git
```

### 创建并切换新分支
```sh
git checkout -b <branch-name>
```
**替代方案：**
```sh
git branch <branch-name> && git checkout <branch-name>
```
```sh
git switch -c <branch-name>
```

### 显示按最近提交排序的所有本地分支
```sh
git for-each-ref --sort=-committerdate --format='%(refname:short)' refs/heads/
```

### 克隆存储库的浅表副本
```sh
git clone https://github.com/user/repo.git --depth 1
```

### 强制推送到远程存储库
```sh
git push -f <remote-name> <branch-name>
```

### 按作者和标题分组提交
```sh
git shortlog
```

### 强制推送但仍确保您不会覆盖其他人的工作
```sh
git push --force-with-lease <remote-name> <branch-name>
```

### 分支中的提交数
```sh
git rev-list --count <branch-name>
```

### 添加对象注释
```sh
git notes add -m 'Note on the previous commit....'
```

### 从另一个存储库应用提交
```sh
git --git-dir=<source-dir>/.git format-patch -k -1 --stdout <SHA1> | git am -3 -k
```

### 具体获取参考
```sh
git fetch origin master:refs/remotes/origin/mymaster
```

### 生成待处理更改的摘要
```sh
git request-pull v1.0 https://git.ko.xz/project master:for-linus
```

### 显示 git 状态简短
```sh
git status --short --branch
```

### 签出一天前的提交
```sh
git checkout master@{yesterday}
```

### 将当前分支推送到远程存储库上的同名分支
```sh
git push origin HEAD
```

### 将新的本地分支推送到远程存储库并跟踪
```sh
git push -u origin <branch_name>
```

### 将子模块更新到最新提交
```sh
cd <path-to-submodule>
git pull origin <branch>
cd <root-of-your-main-project>
git add <path-to-submodule>
git commit -m "submodule updated"
```

### 复制存储库
```sh
git clone --bare https://github.com/exampleuser/old-repository.git

git push --mirror https://github.com/exampleuser/new-repository.git
```

## 分支

### 列出所有已经合并到master的分支
```sh
git branch --merged master
```

### 删除已经与master合并的分支
```sh
git branch --merged master | grep -v '^\*' | xargs -n 1 git branch -d
```
**替代方案：**
```sh
git branch --merged master | grep -v '^\*\|  master' | xargs -n 1 git branch -d # will not delete master if master is not checked out
```

### 列出所有分支及其上游，以及分支上的最后一次提交
```sh
git branch -vv
```

### 跟踪上游分支
```sh
git branch -u origin/mybranch
```

### 删除本地分支
```sh
git branch -d <local_branchname>
```

### 获取所有本地和远程分支的列表
```sh
git branch -a
```

### 仅获取远程分支
```sh
git branch -r
```

### 找出包含commit-hash的分支
```sh
git branch -a --contains <commit-ish>
```
**替代方案：**
```sh
git branch --contains <commit-ish>
```

### 重命名分支
```sh
git branch -m <new-branch-name>
```
**替代方案：**
```sh
git branch -m [<old-branch-name>] <new-branch-name>
```

### 归档“master”分支
```sh
git archive master --format=zip --output=master.zip
```

### 删除已压缩并合并到远程的本地分支。
```sh
git branch -vv | grep ': gone]' | awk '{print $1}' | xargs git branch -D
```

### 将具有历史记录的分支导出到文件。
```sh
git bundle create <file> <branch-name>
```

### 获取当前分支的名称。
```sh
git rev-parse --abbrev-ref HEAD
```

### 显示当前分支上的最新标签。
```sh
git describe --tags --abbrev=0
```

### 列出所有正在开发的分支
```sh
git checkout master && git branch --no-merged
```

### 预格式化的补丁文件。
```sh
git format-patch -M upstream..topic
```

### 切换到分支（结帐的现代替代方案）
```sh
git switch <branch-name>
```
**替代方案：**
```sh
git switch -c <new-branch-name>
```

## 日志和历史

### 显示 Git 附带的有用指南
```sh
git help -g
```

### 按内容搜索变化
```sh
git log -S'<a term in the source>'
```

### 显示特定文件随时间的变化
```sh
git log -p <file_name>
```

### 列出所有冲突的文件
```sh
git diff --name-only --diff-filter=U
```

### 提交中更改的所有文件的列表
```sh
git diff-tree --no-commit-id --name-only -r <commit-ish>
```

### 自上次提交以来未暂存的更改
```sh
git diff
```

### 为提交而进行的更改
```sh
git diff --cached
```
**替代方案：**
```sh
git diff --staged
```

### 显示已分阶段和未分阶段的更改
```sh
git diff HEAD
```

### 两周以来发生了什么变化？
```sh
git log --no-merges --raw --since='2 weeks ago'
```
**替代方案：**
```sh
git whatchanged --since='2 weeks ago'
```

### 查看自 master 分叉以来所做的所有提交
```sh
git log --no-merges --stat --reverse master..
```

### 显示所有跟踪的文件
```sh
git ls-files -t
```

### 显示所有未跟踪的文件
```sh
git ls-files --others
```

### 显示所有被忽略的文件
```sh
git ls-files --others -i --exclude-standard
```

### 可视化版本树。
```sh
git log --pretty=oneline --graph --decorate --all
```
**替代方案：**
```sh
gitk --all
```
```sh
git log --graph --pretty=format:'%C(auto) %h | %s | %an | %ar%d'
```

### 可视化树，包括仅从引用日志引用的提交
```sh
git log --graph --decorate --oneline $(git rev-list --walk-reflogs --all)
```

### 显示内联单词差异。
```sh
git diff --word-diff
```

### 使用常见的差异工具显示更改。
```sh
git difftool [-t <tool>] <commit1> <commit2> <path>
```

### Branch1 中的提交不在 Branch2 中
```sh
git log Branch1 ^Branch2
```

### 列出 n 个最后提交
```sh
git log -<n>
```
**替代方案：**
```sh
git log -n <n>
```

### 在编辑器中打开所有冲突的文件。
```sh
git diff --name-only | uniq | xargs $EDITOR
```

### 查看提交日志中的 GPG 签名
```sh
git log --show-signature
```

### 从另一个分支提取文件。
```sh
git show <branch_name>:<file_name>
```

### 仅列出根提交和合并提交。
```sh
git log --first-parent
```

### 列出对特定文件的提交和更改（甚至通过重命名）
```sh
git log --follow -p -- <file_path>
```

### 在所有分支中搜索提交日志中的给定文本
```sh
git log --all --grep='<given-text>'
```

### 获取分支中的第一次提交（来自 master）
```sh
git log --oneline master..<branch-name> | tail -1
```
**替代方案：**
```sh
git log --reverse master..<branch-name> | head -6
```

### 显示给定文件每一行的作者、时间和最后修订
```sh
git blame <file-name>
```

### 显示作者贡献了多少行
```sh
git log --author='_Your_Name_Here_' --pretty=tformat: --numstat | gawk '{ add += $1; subs += $2; loc += $1 - $2 } END { printf "added lines: %s removed lines: %s total lines: %s
", add, subs, loc }' -
```
**替代方案：**
```sh
git log --author='_Your_Name_Here_' --pretty=tformat: --numstat | awk '{ add += $1; subs += $2; loc += $1 - $2 } END { printf "added lines: %s, removed lines: %s, total lines: %s
", add, subs, loc }' - # on Mac OSX
```

### 显示所有 git-notes
```sh
git log --show-notes='*'
```

### 列出未推送的 git 提交
```sh
git log --branches --not --remotes
```
**替代方案：**
```sh
git log @{u}..
```
```sh
git cherry -v
```

### 添加所有内容，但空白会改变
```sh
git diff --ignore-all-space | git apply --cached
```

### 归咎于一定范围
```sh
git blame -L <start>,<end>
```

### 显示 Git 逻辑变量。
```sh
git var -l | <variable>
```

### 获取存储库名称。
```sh
git rev-parse --show-toplevel
```

### 日期范围之间的日志
```sh
git log --since='FEB 1 2017' --until='FEB 14 2017'
```

### 从日志中排除作者
```sh
git log --perl-regexp --author='^((?!excluded-author-regex).*)$'
```

### 查看上次提交中更改的扩展详细信息
```sh
git show
```

### 可视化过去 30 天内 HEAD 的每个位置
```sh
git reflog
```

## 合并和变基

### 将“feature”变基为“master”并将其合并到 master
```sh
git rebase master feature && git checkout master && git merge -
```

### 变基前存储更改
```sh
git rebase --autostash
```

### Squash 修复提交正常提交。
```sh
git rebase -i --autosquash
```

### 使用交互式变基更改前​​两次提交。
```sh
git rebase --interactive HEAD~2
```

### 找到两个分支的共同祖先
```sh
git merge-base <branch-name> <other-branch-name>
```

### 更改分支基地
```sh
git rebase --onto <new_base> <old_base>
```

## 杂项

### 日常使用 20 个左右的 Git 命令
```sh
git help everyday
```

### 取消跟踪文件而不删除
```sh
git rm --cached <file_path>
```
**替代方案：**
```sh
git rm --cached -r <directory_path>
```

### 不考虑跟踪文件的更改。
```sh
git update-index --assume-unchanged <file_name>
```

### 检查更改是否是版本的一部分。
```sh
git name-rev --name-only <SHA-1>
```

### 列出被忽略的文件。
```sh
git check-ignore *
```

### 计算已解压的对象数量及其磁盘消耗。
```sh
git count-objects --human-readable
```

### 从对象数据库中删除所有无法访问的对象。
```sh
git gc --prune=now --aggressive
```

### 立即浏览 gitweb 中的工作存储库。
```sh
git instaweb [--local] [--httpd=<httpd>] [--port=<port>] [--browser=<browser>]
```

### 在跟踪文件中查找与模式（正则表达式或字符串）匹配的行
```sh
git grep --heading --line-number 'foo bar'
```

### 备份未跟踪的文件。
```sh
git ls-files --others -i --exclude-standard | xargs zip untracked.zip
```

### 以电子邮件的形式发送补丁集合
```sh
git send-email [<options>] <file|directory>…

git send-email [<options>] <format-patch options>
```

## 遥控器

### 更改远程 URL
```sh
git remote set-url origin <URL>
```

### 获取所有远程引用的列表
```sh
git remote
```
**替代方案：**
```sh
git remote show
```

### 添加远程名称
```sh
git remote add <remote-nickname> <remote-url>
```

### 列出所有当前配置的遥控器
```sh
git remote -v
```

### 列出远程存储库中的引用
```sh
git ls-remote git://git.kernel.org/pub/scm/git/git.git
```

### 刷新远程分支列表
```sh
git remote update origin --prune
```

## 设置和配置

### 推送后从历史记录中删除敏感数据
```sh
git filter-branch --force --index-filter 'git rm --cached --ignore-unmatch <path-to-your-file>' --prune-empty --tag-name-filter cat -- --all && git push origin --force --all
```

### 在全局配置中更改作者后重置作者。
```sh
git commit --amend --reset-author --no-edit
```

### 获取 git bash 补全
```sh
curl -L http://git.io/vfhol > ~/.git-completion.bash && echo '[ -f ~/.git-completion.bash ] && . ~/.git-completion.bash' >> ~/.bashrc
```

### Git 别名
```sh
git config --global alias.<handle> <command> 
git config --global alias.st status
```

### 始终变基而不是拉取时合并。
```sh
git config --global pull.rebase true
```
**替代方案：**
```sh
#git < 1.7.9
git config --global branch.autosetuprebase always
```

### 列出所有别名和配置。
```sh
git config --list
```

### 使 git 区分大小写。
```sh
git config --global core.ignorecase false
```

### 添加自定义编辑器。
```sh
git config --global core.editor '$EDITOR'
```

### 自动更正拼写错误。
```sh
git config --global help.autocorrect 1
```

### 重用记录的解决方案，记录并重用以前的冲突解决方案。
```sh
git config --global rerere.enabled 1
```

### 删除全局配置中的条目。
```sh
git config --global --unset <entry-name>
```

### 忽略提交时的文件模式更改
```sh
git config core.fileMode false
```

### 关闭 git 彩色终端输出
```sh
git config --global color.ui false
```

### 具体颜色设置
```sh
git config --global <specific command e.g branch, diff> <true, false or always>
```

### 别名：git 撤消
```sh
git config --global alias.undo '!f() { git reset --hard $(git rev-parse --abbrev-ref HEAD)@{${1-1}}; }; f'
```

### 编辑[本地/全局] git 配置
```sh
git config [--global] --edit
```

### 列出所有 git 别名
```sh
git config -l | grep alias | sed 's/^alias\.//g'
```
**替代方案：**
```sh
git config -l | grep alias | cut -d '.' -f 2
```

### 对远程服务器使用 SSH 而不是 HTTP
```sh
git config --global url.'git@github.com:'.insteadOf 'https://github.com/'
```

### 防止自动将 LF 替换为 CRLF
```sh
git config --global core.autocrlf false
```

### 编辑每个级别的配置
```sh
git config --edit --system

git config --edit --global

git config --edit --local
```

## 藏匿

### 保存跟踪文件的当前状态而不提交
```sh
git stash
```
**替代方案：**
```sh
git stash push
```

### 将未暂存更改的当前状态保存到跟踪文件
```sh
git stash -k
```
**替代方案：**
```sh
git stash --keep-index
```
```sh
git stash push --keep-index
```

### 保存当前状态，包括未跟踪的文件
```sh
git stash -u
```
**替代方案：**
```sh
git stash push -u
```
```sh
git stash push --include-untracked
```

### 使用消息保存当前状态
```sh
git stash push -m <message>
```
**替代方案：**
```sh
git stash push --message <message>
```

### 保存所有文件的当前状态（忽略、未跟踪和跟踪）
```sh
git stash -a
```
**替代方案：**
```sh
git stash --all
```
```sh
git stash push --all
```

### 显示所有已保存存储的列表
```sh
git stash list
```

### 以补丁形式显示任何存储的内容
```sh
git stash show -p <stash@{n}>
```

### 应用任何隐藏，而不从隐藏列表中删除
```sh
git stash apply <stash@{n}>
```

### 应用最后的隐藏状态并将其从隐藏列表中删除
```sh
git stash pop
```
**替代方案：**
```sh
git stash apply stash@{0} && git stash drop stash@{0}
```

### 删除所有存储的存储
```sh
git stash clear
```
**替代方案：**
```sh
git stash drop <stash@{n}>
```

## 子模块和子树

### 更新所有子模块
```sh
git submodule foreach git pull
```
**替代方案：**
```sh
git submodule update --init --recursive
```
```sh
git submodule update --remote
```

### 将 git tracked 子文件夹部署到 gh-pages
```sh
git subtree push --prefix subfolder_name origin gh-pages
```
**替代方案：**
```sh
git subtree push --prefix subfolder_name origin branch_name
```

### 使用子树将项目添加到存储库
```sh
git subtree add --prefix=<directory_name>/<project_name> --squash git@github.com:<username>/<project_name>.git master
```

### 使用子树获取链接项目的存储库中的最新更改
```sh
git subtree pull --prefix=<directory_name>/<project_name> --squash git@github.com:<username>/<project_name>.git master
```

## 标记

### 创建本地标签
```sh
git tag <tag-name>
```

### 删除本地标签
```sh
git tag -d <tag-name>
```

## 撤消更改

### 与远程同步，覆盖本地更改
```sh
git fetch origin && git reset --hard origin/master && git clean -f -d
```

### Git 重置第一次提交
```sh
git update-ref -d HEAD
```

### 重置：保留未提交的本地更改
```sh
git reset --keep <commit>
```

### 恢复：通过创建新提交来撤消提交
```sh
git revert <commit-ish>
```

### 重置：放弃提交，建议用于私有分支
```sh
git reset <commit-ish>
```

### 在删除未跟踪的文件/目录之前，请进行一次试运行以获取这些文件/目录的列表
```sh
git clean -n
```

### 强制删除未跟踪的文件
```sh
git clean -f
```

### 强制删除未跟踪的目录
```sh
git clean -f -d
```

### 撤消假设不变。
```sh
git update-index --no-assume-unchanged <file_name>
```

### 清除“.gitignore”中的文件。
```sh
git clean -X -f
```

### 试运行。 （任何支持试运行标志的命令都应该这样做。）
```sh
git clean -fd --dry-run
```

### 取消暂存暂存文件
```sh
git reset HEAD <file-name>
```

### 恢复：恢复整个合并
```sh
git revert -m 1 <commit-ish>
```

### 恢复文件（重置/签出的现代替代方案--）
```sh
git restore <file-name>
```
**替代方案：**
```sh
git restore --staged <file-name>
```
