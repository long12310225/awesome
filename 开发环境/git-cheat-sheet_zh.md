# Git 和 Git 流程备忘单
[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

<p align="center">
    <img alt="Git" src="./Img/git-logo.png" height="190" width="455">
</p>

---

## 📖 关于

这份全面的 Git 备忘单可帮助您掌握 Git 命令，而无需记住所有内容。无论您是初学者还是经验丰富的开发人员，本指南都提供了基本 Git 操作的快速参考。

**欢迎贡献！** 请随意：
- 修复语法错误
- 添加新命令
- 翻译成您的语言
- 改进解释

---
## 📋 目录

- [🔧 设置](#-setup)
- [⚙️ 配置文件](#️-configuration-files)
- [🆕 创建存储库](#-create-repository)
- [📝 局部变化](#-local-changes)
- [🔍 搜索](#-search)
- [📖 提交历史](#-commit-history)
- [📁 移动/重命名](#-move--rename)
- [🌿 分支和标签](#-branches--tags)
- [🔄 更新并发布](#-update--publish)
- [🔀 合并和变基](#-merge--rebase)
- [↩️ 撤消](#️-undo)
- [🌊 Git 流程](#-git-flow)
- [🌍其他语言](#-other-languages)

---

## 🔧 设置

### 查看配置

**显示当前配置：**
```bash
git config --list
```

**显示存储库配置：**
```bash
git config --local --list
```

**显示全局配置：**
```bash
git config --global --list
```

**显示系统配置：**
```bash
git config --system --list
```

### 用户配置

**设置版本历史记录的名称：**
```bash
git config --global user.name "[firstname lastname]"
```

**设置您的电子邮件地址：**
```bash
git config --global user.email "[valid-email]"
```

### 显示和编辑器设置

**启用自动命令行着色：**
```bash
git config --global color.ui auto
```

**为提交设置全局编辑器：**
```bash
git config --global core.editor vi
```

---

## ⚙️ 配置文件

|范围 |地点 |命令标志 |
|-------|----------|--------------|
| **存储库** | `<repo>/.git/config` | `--本地` |
| **用户** | `~/.gitconfig` | `--全局` |
| **系统** | `/etc/gitconfig` | `--系统` |

---

## 🆕 创建存储库

### 克隆现有存储库

**通过 SSH：**
```bash
git clone ssh://user@domain.com/repo.git
```

**通过 HTTPS：**
```bash
git clone https://domain.com/user/repo.git
```

### 初始化新存储库

**在当前目录中创建存储库：**
```bash
git init
```

**在特定目录中创建存储库：**
```bash
git init <directory>
```

---

## 📝 局部变化

### 检查状态和差异

**查看工作目录状态：**
```bash
git status
```

**显示跟踪文件的更改：**
```bash
git diff
```

**显示特定文件中的更改：**
```bash
git diff <file>
```

### 分期变更

**添加所有当前更改：**
```bash
git add .
```

**添加特定文件：**
```bash
git add <filename1> <filename2>
```

**交互式添加文件的各个部分：**
```bash
git add -p <file>
```

### 提交变更

**提交所有跟踪的文件更改：**
```bash
git commit -a
```

**提交分阶段更改：**
```bash
git commit
```

**提交消息：**
```bash
git commit -m 'message here'
```

**跳过暂存并提交消息：**
```bash
git commit -am 'message here'
```

**承诺具体日期：**
```bash
git commit --date="`date --date='n day ago'`" -am "<Commit Message Here>"
```

### 修改上次提交

> ⚠️ **警告：** 不要修改已发布的提交！

**修改上次提交：**
```bash
git commit -a --amend
```

**修改而不更改提交消息：**
```bash
git commit --amend --no-edit
```

**更改提交者日期：**
```bash
GIT_COMMITTER_DATE="date" git commit --amend
```

**更改作者日期：**
```bash
git commit --amend --date="date"
```

### 隐藏更改

**暂时保存当前更改：**
```bash
git stash
```

**应用最后隐藏的更改：**
```bash
git stash apply
```

**应用特定的存储：**
```bash
git stash apply stash@{stash_number}
```
> 使用 `git stash list` 查看可用的存储

**删除最后一个藏匿处：**
```bash
git stash drop
```

**将未提交的更改移至另一个分支：**
```bash
git stash
git checkout branch2
git stash pop
```

---

## 🔍 搜索

### 文本搜索

**搜索所有文件中的文本：**
```bash
git grep "Hello"
```

**具体版本搜索：**
```bash
git grep "Hello" v2.5
```

### 提交搜索

**查找引入特定关键字的提交：**
```bash
git log -S 'keyword'
```

**使用正则表达式搜索：**
```bash
git log -S 'keyword' --pickaxe-regex
```

---

## 📖 提交历史

### 基本历史

**显示所有提交（详细）：**
```bash
git log
```

**显示提交（每行）：**
```bash
git log --oneline
```

**显示特定作者的提交：**
```bash
git log --author="username"
```

**显示特定文件的更改：**
```bash
git log -p <file>
```

### 高级历史

**比较分支：**
```bash
git log --oneline <origin/master>..<remote/master> --left-right
```

**显示谁更改了什么以及何时更改：**
```bash
git blame <file>
```

### 参考日志

**显示参考日志：**
```bash
git reflog show
```

**删除参考日志：**
```bash
git reflog delete
```

---

## 📁 移动/重命名

**重命名文件：**
```bash
git mv Index.txt Index.html
```

---

## 🌿 分支和标签

### 列出分支机构

**列出当地分支机构：**
```bash
git branch
```

**列出所有分支（本地+远程）：**
```bash
git branch -a
```

**列出远程分支：**
```bash
git branch -r
```

**列出合并的分支：**
```bash
git branch --merged
```

### 切换并创建分支

**切换到现有分支：**
```bash
git checkout <branch>
```

**创建并切换到新分支：**
```bash
git checkout -b <branch>
```

**切换到上一个分支：**
```bash
git checkout -
```

**从现有分支创建分支：**
```bash
git checkout -b <new_branch> <existing_branch>
```

**从特定提交创建分支：**
```bash
git checkout <commit-hash> -b <new_branch_name>
```

**创建分支而不切换：**
```bash
git branch <new-branch>
```

**创建跟踪分支：**
```bash
git branch --track <new-branch> <remote-branch>
```

### 分行营运

**从不同分支签出单个文件：**
```bash
git checkout <branch> -- <filename>
```

**应用来自另一个分支的特定提交：**
```bash
git cherry-pick <commit hash>
```

**重命名当前分支：**
```bash
git branch -m <new_branch_name>
```

**删除本地分支：**
```bash
git branch -d <branch>
```

**强制删除本地分支：**
```bash
git branch -D <branch>
```
> ⚠️ **警告：** 您将丢失未合并的更改！

### 标签

**在 HEAD 处创建标签：**
```bash
git tag <tag-name>
```

**创建带注释的标签：**
```bash
git tag -a <tag-name>
```

**创建带有消息的标签：**
```bash
git tag <tag-name> -am 'message here'
```

**列出所有标签：**
```bash
git tag
```

**列出带有消息的标签：**
```bash
git tag -n
```

---

## 🔄 更新并发布

### 远程管理

**列出配置的遥控器：**
```bash
git remote -v
```

**显示远程信息：**
```bash
git remote show <remote>
```

**添加新遥控器：**
```bash
git remote add <remote> <url>
```

**重命名远程：**
```bash
git remote rename <remote> <new_remote>
```

**删除遥控器：**
```bash
git remote rm <remote>
```
> ℹ️ **注意：** 这只会删除本地远程引用，而不是远程存储库本身。

### 获取和拉动

**下载更改而不合并：**
```bash
git fetch <remote>
```

**下载并合并更改：**
```bash
git pull <remote> <branch>
```

**从主分支获取更改：**
```bash
git pull origin master
```

**使用变基拉动：**
```bash
git pull --rebase <remote> <branch>
```

### 推送和发布

**发布本地更改：**
```bash
git push <remote> <branch>
```

**删除远程分支：**
```bash
# Git v1.7.0+
git push <remote> --delete <branch>

# Git v1.5.0+
git push <remote> :<branch>
```

**发布标签：**
```bash
git push --tags
```

---

## 🔀 合并和变基

### 合并操作

**将分支合并到当前 HEAD 中：**
```bash
git merge <branch>
```

**全局配置合并工具：**
```bash
git config --global merge.tool meld
```

**使用配置的合并工具：**
```bash
git mergetool
```

### 变基操作

> ⚠️ **警告：** 不要对已发布的提交进行变基！

**将当前 HEAD 重新设置为分支：**
```bash
git rebase <branch>
```

**中止变基：**
```bash
git rebase --abort
```

**解决冲突后继续rebase：**
```bash
git rebase --continue
```

### 冲突解决

**将文件标记为已解决：**
```bash
git add <resolved-file>
```

**删除已解析的文件：**
```bash
git rm <resolved-file>
```

### 压制提交

**用于挤压的交互式变基：**
```bash
git rebase -i <commit-just-before-first>
```

**壁球配置示例：**
```
# Before
pick <commit_id>
pick <commit_id2>
pick <commit_id3>

# After (squash commit_id2 and commit_id3 into commit_id)
pick <commit_id>
squash <commit_id2>
squash <commit_id3>
```

---

## ↩️ 撤消

### 放弃更改

**放弃所有本地更改：**
```bash
git reset --hard HEAD
```

**取消暂存所有文件：**
```bash
git reset HEAD
```

**放弃特定文件中的更改：**
```bash
git checkout HEAD <file>
```

### 复位操作

**重置为之前的提交（放弃所有更改）：**
```bash
git reset --hard <commit>
```

**重置为远程分支状态：**
```bash
git reset --hard <remote/branch>
# Example: git reset --hard upstream/master
```

**重置保留更改为未暂存：**
```bash
git reset <commit>
```

**重置保留未提交的本地更改：**
```bash
git reset --keep <commit>
```

### 恢复提交

**恢复提交（创建具有相反更改的新提交）：**
```bash
git revert <commit>
```

### 清理忽略的文件

**删除意外提交的应忽略的文件：**
```bash
git rm -r --cached .
git add .
git commit -m "remove ignored files"
```

---

## 🌊 Git 流程

**改进的 Git 流程：** [git-flow-avh](https://github.com/petervanderdoes/gitflow-avh)

### 📋 目录
- [🔧 设置](#setup-1)
- [🚀 开始使用](#getting-started)
- [✨ 特点](#features)
- [🎁 发布](#make-a-release)
- [🔥 修补程序](#hotfixes)
- [📊 命令概述](#commands-overview)

---

### 🔧 设置 {#setup-1}

> **先决条件：** 需要安装有效的 Git。 Git-flow 适用于 macOS、Linux 和 Windows。

**macOS（自制）：**
```bash
brew install git-flow-avh
```

**macOS（MacPorts）：**
```bash
port install git-flow
```

**Linux（基于 Debian）：**
```bash
sudo apt-get install git-flow
```

**Windows（Cygwin）：**
> 需要 wget 和 util-linux
```bash
wget -q -O - --no-check-certificate https://raw.githubusercontent.com/petervanderdoes/gitflow/develop/contrib/gitflow-installer.sh install <state> | bash
```

---

### 🚀 开始使用

Git-flow 需要初始化来自定义您的项目设置。

**初始化（交互式）：**
```bash
git flow init
```
> 您将回答有关分支命名约定的问题。建议使用默认值。

**初始化（使用默认值）：**
```bash
git flow init -d
```

---

### ✨ 特点

功能用于为即将发布的版本开发新功能。它们通常仅存在于开发人员存储库中。

**启动新功能：**
```bash
git flow feature start MYFEATURE
```
> 基于“develop”创建功能分支并切换到它

**完成特征：**
```bash
git flow feature finish MYFEATURE
```
> 这将：
> 1. 将 MYFEATURE 合并到“开发”中
> 2.删除feature分支
> 3.切换回“开发”

**发布功能（用于协作）：**
```bash
git flow feature publish MYFEATURE
```

**获取已发布的功能：**
```bash
git flow feature pull origin MYFEATURE
```

**追踪原点功能：**
```bash
git flow feature track MYFEATURE
```

---

### 🎁 发布

版本支持准备新的生产版本，允许修复小错误并准备元数据。

**开始发布：**
```bash
git flow release start RELEASE [BASE]
```
> 从“开发”创建发布分支。 （可选）指定 [BASE] 提交 SHA-1。

**发布版本：**
```bash
git flow release publish RELEASE
```

**追踪远程发布：**
```bash
git flow release track RELEASE
```

**完成发布：**
```bash
git flow release finish RELEASE
```
> 这将：
> 1. 将release分支合并到'master'
> 2. 标记发布
> 3. 向后合并发布到“开发”
> 4.删除发布分支

> 💡 **不要忘记：** 使用 `git push --tags` 推送您的标签

---

### 🔥 修补程序

修补程序解决了实时生产版本中的关键问题。它们从 master 上的相应标签分支出来。

**启动修补程序：**
```bash
git flow hotfix start VERSION [BASENAME]
```

**完成修补程序：**
```bash
git flow hotfix finish VERSION
```
> 合并回“develop”和“master”，并标记主合并

---

### 📊 命令概述

<p align="center">
    <img alt="Git Flow Commands" src="./Img/git-flow-commands.png" height="270" width="460">
</p>

### 🌊 Git 流程架构

<p align="center">
    <img alt="Git Flow Schema" src="Img/git-flow-commands-without-flow.png">
</p>

---


## 🌍其他语言

该备忘单有多种语言版本：

|语言 |链接 |
|----------|------|
| 🇸🇦 阿拉伯语 | [git-cheat-sheet-ar.md](./other-sheets/git-cheat-sheet-ar.md) |
| 🇧🇩 孟加拉语 | [git-cheat-sheet-bn.md](./other-sheets/git-cheat-sheet-bn.md) |
| 🇧🇷 巴西葡萄牙语 | [git-cheat-sheet-pt_BR.md](./other-sheets/git-cheat-sheet-pt_BR.md) |
| 🇨🇳 中文 | [git-cheat-sheet-zh.md](./other-sheets/git-cheat-sheet-zh.md) |
| 🇩🇪 德语 | [git-cheat-sheet-de.md](./other-sheets/git-cheat-sheet-de.md) |
| 🇬🇷 希腊语 | [git-cheat-sheet-el.md](./other-sheets/git-cheat-sheet-el.md) |
| 🇮🇳 印地语 | [git-cheat-sheet-hi.md](./other-sheets/git-cheat-sheet-hi.md) |
| 🇰🇷 韩语 | [git-cheat-sheet-ko.md](./other-sheets/git-cheat-sheet-ko.md) |
| 🇵🇱 波兰语 | [git-cheat-sheet-pl.md](./other-sheets/git-cheat-sheet-pl.md) |
| 🇪🇸 西班牙语 | [git-cheat-sheet-es.md](./other-sheets/git-cheat-sheet-es.md) |
| 🇹🇷 土耳其语 | [git-cheat-sheet-tr.md](./other-sheets/git-cheat-sheet-tr.md) |

---

## 🤝 贡献

我们欢迎贡献！您可以：

- 🐛 报告错误或拼写错误
- ✨ 添加新的 Git 命令
- 🌍 翻译成新语言
- 💡改进解释
- 📝 增强格式

**如何贡献：**
1. 分叉这个存储库
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交您的更改（`git commit -m 'Add some AmazingFeature'`）
4.推送到分支（`git push origin feature/AmazingFeature`）
5. 发起拉取请求

---

## 📄 许可证

该项目是开源的，可在 [MIT 许可证](LICENSE) 下使用。

---

<p align="center">
    <b>⭐ Star this repository if you found it helpful!</b>
</p>

