# GitHub 备忘单 [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
Git 和 GitHub 的一些很酷的隐藏功能和不那么隐藏的功能的集合。本备忘单的灵感来自 [Zach Holman](https://github.com/holman) 在 2012 年 Aloha Ruby Conference 上的 [Git 和 GitHub Secrets](http://confreaks.tv/videos/aloharuby2012-git-and-github-secrets) 演讲（[幻灯片](https://speakerdeck.com/holman/git-and-github-secrets)）以及他的 [更多 Git 和 GitHub] Secrets](https://vimeo.com/72955426) 在 WDCNZ 2013 上的演讲（[幻灯片](https://speakerdeck.com/holman/more-git-and-github-secrets)）。

*短链接：[`http://git.io/sheet`](http://git.io/sheet)*

*Read this in other languages: [English](README.md), [한국어](README.ko.md), [日本語](README.ja.md), [简体中文](README.zh-cn.md), [正體中文](README.zh-tw.md).*

GitHub Cheat Sheet 由 [Snapshot：使用 AI 创建交互式专业品质产品照片](https://www.snapshotapp.io/) 赞助

## 目录
  - [GitHub](#github)
    - [忽略空格](#ignore-whitespace)
    - [调整制表符间距](#adjust-tab-space)
    - [按作者提交历史记录](#commit-history-by-author)
    - [克隆存储库](#cloning-a-repository)
    - [Branch](#branch)
      - [将所有分支与另一个分支进行比较](#compare-all-branches-to-another-branch)
      - [比较分支](#comparing-branches)
      - [比较分叉存储库中的分支](#compare-branches-across-forked-repositories)
    - [Gists](#gists)
    - [Git.io](#gitio)
    - [键盘快捷键](#keyboard-shortcuts)
    - [存储库中的行突出显示](#line-highlighting-in-repositories)
    - [通过提交消息关闭问题](#closing-issues-via-commit-messages)
    - [交叉链接问题](#cross-link-issues)
    - [锁定对话](#locking-conversations)
    - [拉取请求的 CI 状态](#ci-status-on-pull-requests)
    - [Filters](#filters)
    - [Markdown 文件中的语法突出显示](#syntax-highlighting-in-markdown-files)
    - [Emojis](#emojis)
    - [Images/GIFs](#imagesgifs)
      - [在 GitHub Wiki 中嵌入图像](#embedding-images-in-github-wiki)
    - [快速报价](#quick-quoting)
    - [将剪贴板图像粘贴到评论](#pasting-clipboard-image-to-comments)
    - [快速授权](#quick-licensing)
    - [任务列表](#task-lists)
      - [Markdown 文档中的任务列表](#task-lists-in-markdown-documents)
    - [相关链接](#relative-links)
    - [GitHub 页面的元数据和插件支持](#metadata-and-plugin-support-for-github-pages)
    - [查看文档中的 YAML 元数据](#viewing-yaml-metadata-in-your-documents)
    - [渲染表格数据](#rendering-tabular-data)
    - [渲染 PDF](#rendering-pdf)
    - [恢复拉取请求](#revert-a-pull-request)
    - [Diffs](#diffs)
      - [渲染散文差异](#rendered-prose-diffs)
      - [可区分贴图](#diffable-maps)
      - [扩展差异中的上下文](#expanding-context-in-diffs)
      - [Pull 请求的差异或补丁](#diff-or-patch-of-pull-request)
      - [渲染和比较图像](#rendering-and-diffing-images)
    - [Hub](#hub)
    - [贡献指南](#contribution-guidelines)
      - [贡献文件](#contributing-file)
      - [ISSUE_TEMPLATE 文件](#issue_template-file)
      - [PULL_REQUEST_TEMPLATE 文件](#pull_request_template-file)
    - [Octicons](#octicons)
    - [GitHub 学生开发包](#github-student-developer-pack)
    - [GitHub 资源](#github-resources)
      - [GitHub 讲座](#github-talks)
    - [SSH 密钥](#ssh-keys)
    - [个人资料图片](#profile-image)
    - [存储库模板](#repository-templates)
  - [Git](#git)
    - [从工作树中删除所有已删除的文件](#remove-all-deleted-files-from-the-working-tree)
    - [以前的分行](#previous-branch)
    - [Stripspace](#stripspace)
    - [检查拉取请求](#checking-out-pull-requests)
    - [空提交](#empty-commits)
    - [样式化的 Git 状态](#styled-git-status)
    - [样式化的 Git 日志](#styled-git-log)
    - [git查询](#git-query)
    - [git grep](#git-grep)
    - [合并分支](#merged-branches)
    - [修复和自动挤压](#fixup-and-autosquash)
    - [用于浏览本地存储库的 Web 服务器](#web-server-for-browsing-local-repositories)
    - [Git 配置](#git-configurations)
      - [Aliases](#aliases)
      - [Auto-Correct](#auto-correct)
      - [Color](#color)
    - [Git 资源](#git-resources)
      - [Git 书籍](#git-books)
      - [git 视频](#git-videos)
      - [git 文章](#git-articles)


## GitHub
### 忽略空格
将 `?w=1` 添加到任何 diff URL 将仅删除空白中的任何更改，使您只能看到已更改的代码。

![Diff without whitespace](https://camo.githubusercontent.com/797184940defadec00393e6559b835358a863eeb/68747470733a2f2f6769746875622d696d616765732e73332e616d617a6f6e6177732e636f6d2f626c6f672f323031312f736563726574732f776869746573706163652e706e67)

[*阅读有关 GitHub 秘密的更多信息。*](https://github.com/blog/967-github-secrets)

### 调整制表符间距
将 `?ts=4` 添加到 diff 或文件 URL 会将制表符显示为 4 个空格宽，而不是默认的 8 个空格。可以调整 `ts` 之后的数字以适合您的偏好。这不适用于 Gists 或原始文件视图，但 [Chrome 扩展](https://chrome.google.com/webstore/detail/tab-size-on-github/ofjbgncegkdemndciafljngjbdpfmbkn) 可以自动执行此操作。

这是添加 `?ts=4` 之前的 Go 源文件：

![Before, tab space example](http://i.imgur.com/GIT1Fr0.png)

...这是添加 `?ts=4` 后的结果：

![After, tab space example](http://i.imgur.com/70FL4H9.png)

### 按作者提交历史记录
要查看作者对存储库的所有提交，请将 `?author={user}` 添加到 URL。

```
https://github.com/rails/rails/commits/master?author=dhh
```

![DHH commit history](http://i.imgur.com/S7AE29b.png)

[*阅读有关提交视图之间差异的更多信息。*](https://help.github.com/articles/differences- Between-commit-views/)

### 克隆存储库
克隆存储库时，可以将“.git”保留在末尾。

```bash
$ git clone https://github.com/tiimgreen/github-cheat-sheet
```

[*阅读有关 Git `clone` 命令的更多信息。*](http://git-scm.com/docs/git-clone)

### 分公司
#### 将所有分支与另一个分支进行比较

如果您转到存储库的 [Branches](https://github.com/tiimgreen/github-cheat-sheet/branches) 页面，“提交”按钮旁边：

```
https://github.com/{user}/{repo}/branches
```

...您将看到未合并到主分支的所有分支的列表。

从这里您可以访问比较页面或通过单击按钮删除分支。

![Compare branches not merged into master in rails/rails repo - https://github.com/rails/rails/branches](http://i.imgur.com/0FEe30z.png)

#### 比较分支
要使用 GitHub 比较分支，请将 URL 更改为如下所示：

```
https://github.com/{user}/{repo}/compare/{range}
```

其中 `{range} = master...4-1-stable`

例如：

```
https://github.com/rails/rails/compare/master...4-1-stable
```

![Rails branch compare example](http://i.imgur.com/tIRCOsK.png)

`{range}` 可以更改为：

```
https://github.com/rails/rails/compare/master@{1.day.ago}...master
https://github.com/rails/rails/compare/master@{2014-10-04}...master
```

*此处，日期的格式为“YYYY-MM-DD”*

![Another compare example](http://i.imgur.com/5dtzESz.png)

分支也可以在“diff”和“patch”视图中进行比较：

```
https://github.com/rails/rails/compare/master...4-1-stable.diff
https://github.com/rails/rails/compare/master...4-1-stable.patch
```

[*阅读有关比较跨时间提交的更多信息。*](https://help.github.com/articles/comparing-commits-across-time/)

#### 比较分叉存储库中的分支
要使用 GitHub 比较分叉存储库中的分支，请将 URL 更改为如下所示：

```
https://github.com/{user}/{repo}/compare/{foreign-user}:{branch}...{own-branch}
```

例如：

```
https://github.com/rails/rails/compare/byroot:master...master
```

![Forked branch compare](http://i.imgur.com/Q1W6qcB.png)

### 要点
[Gists](https://gist.github.com/) 是一种处理少量代码的简单方法，无需创建成熟的存储库。

![Gist](http://i.imgur.com/VkKI1LC.png?1)

将 `.pibb` 添加到任何 Gist URL 的末尾（[像这样](https://gist.github.com/tiimgreen/10545817.pibb)），以获得适合嵌入到任何其他站点的 *仅 HTML* 版本。

Gists 可以被视为存储库，因此可以像其他存储库一样进行克隆：

```bash
$ git clone https://gist.github.com/tiimgreen/10545817
```

![Gists](http://i.imgur.com/BcFzabp.png)

这意味着您还可以修改 Gists 并将更新推送到 Gists：

```bash
$ git commit
$ git push
Username for 'https://gist.github.com':
Password for 'https://tiimgreen@gist.github.com':
```

但是，Gists 不支持目录。所有文件都需要添加到存储库根目录中。
[*阅读有关创建要点的更多信息。*](https://help.github.com/articles/creating-gists/)

### Git.io
[Git.io](http://git.io) 是 GitHub 的简单 URL 缩短器。

![Git.io](http://i.imgur.com/6JUfbcG.png?1)

您还可以使用 Curl 通过纯 HTTP 使用它：

```bash
$ curl -i http://git.io -F "url=https://github.com/..."
HTTP/1.1 201 Created
Location: http://git.io/abc123

$ curl -i http://git.io/abc123
HTTP/1.1 302 Found
Location: https://github.com/...
```

[*阅读有关 Git.io 的更多信息。*](https://github.com/blog/985-git-io-github-url-shortener)

### 键盘快捷键
在存储库页面上时，键盘快捷键可让您轻松导航。

- 按“t”将打开文件浏览器。
- 按“w”将调出分支选择器。
- 按“s”将聚焦当前存储库的搜索字段。按 ↓ 选择“All GitHub”选项，将字段更改为搜索整个 GitHub。
- 按“l”将编辑现有问题的标签。
- **查看文件时**按“y”（例如，“https://github.com/tiimgreen/github-cheat-sheet/blob/master/README.md”）会将您的 URL 更改为一个，这实际上会冻结您正在查看的页面。如果此代码发生更改，您仍然可以看到当前看到的内容。

要查看当前页面的所有快捷方式，请按“?”：

![Keyboard shortcuts](http://i.imgur.com/y5ZfNEm.png)

[阅读有关您可以使用的搜索语法的更多信息。](https://help.github.com/articles/search-syntax/)

### 存储库中的行突出显示
例如，将“#L52”添加到代码文件 URL 的末尾或简单地单击行号将突出显示该行号。

它还适用于范围，例如“#L53-L60”，要选择范围，按住“shift”并单击两行：

```
https://github.com/rails/rails/blob/master/activemodel/lib/active_model.rb#L53-L60
```

![Line Highlighting](http://i.imgur.com/8AhjrCz.png)

### 通过提交消息关闭问题
如果特定提交修复了问题，则任何关键字“fix/fixes/fixed”、“close/closes/lated”或“resolve/resolves/resolved”，后跟问题编号，一旦提交到存储库的默认分支，就会关闭该问题。

```bash
$ git commit -m "Fix screwup, fixes #12"
```

这将结束问题并引用结束提交。

![Closing Repo](http://i.imgur.com/Uh1gZdx.png)

[*阅读有关通过提交消息关闭问题的更多信息。*](https://help.github.com/articles/looking-issues-via-commit-messages/)

### 交叉链接问题
如果您想链接到同一存储库中的另一个问题，只需输入哈希“#”，然后输入问题编号，它将自动链接。

要链接到另一个存储库中的问题，“{user}/{repo}#ISSUE_NUMBER”，例如“tiimgreen/toc#12”。

![Cross-Link Issues](https://camo.githubusercontent.com/447e39ab8d96b553cadc8d31799100190df230a8/68747470733a2f2f6769746875622d696d616765732e73332e616d617a6f6e6177732e636f6d2f626c6f672f323031312f736563726574732f7265666572656e6365732e706e67)

### 锁定对话
拉取请求和问题现在可以由存储库的所有者或协作者锁定。

![Lock conversation](https://cloud.githubusercontent.com/assets/2723/3221693/bf54dd44-f00d-11e3-8eb6-bb51e825bc2c.png)

这意味着不是该项目合作者的用户将无法再发表评论。

![Comments locked](https://cloud.githubusercontent.com/assets/2723/3221775/d6e513b0-f00e-11e3-9721-2131cb37c906.png)

[*阅读有关锁定对话的更多信息。*](https://github.com/blog/1847-locking-conversations)


### 拉取请求的 CI 状态
如果设置正确，每次您收到 Pull 请求时，[Travis CI](https://travis-ci.org/) 都会构建该 Pull 请求，就像您每次进行新提交时一样。详细了解如何[Travis CI 入门](http://docs.travis-ci.com/user/getting-started/)。

[![Travis CI status](https://cloud.githubusercontent.com/assets/1687642/2700187/3a88838c-c410-11e3-9a46-e65e2a0458cd.png)](https://github.com/octokit/octokit.rb/pull/452)

[*阅读有关提交状态 API 的更多信息。*](https://github.com/blog/1227-commit-status-api)

### 过滤器

问题和拉取请求都允许在用户界面中进行过滤。

对于 Rails 存储库：https://github.com/rails/rails/issues，通过选择标签“activerecord”构建以下过滤器：

`是：问题标签：activerecord`

但是，您还可以找到所有未标记为 activerecord 的问题：

`是：问题-标签：activerecord`

此外，这也适用于拉取请求：

`是：pr -标签：activerecord`

Github 有用于显示打开或关闭的问题和拉取请求的选项卡，但您
还可以查看合并的拉取请求。  只需将以下内容放入过滤器中即可：

`是：合并`

[*阅读有关搜索问题的更多信息。*](https://help.github.com/articles/searching-issues/)

最后，github 现在允许您按 Status API 的状态进行过滤。

仅具有成功状态的拉取请求：

`状态：成功`

[*阅读有关在 Status API 上搜索的更多信息。*](https://github.com/blog/2014-filter-pull-requests-by-status)

### Markdown 文件中的语法突出显示
例如，要在 Markdown 文件中语法高亮显示 Ruby 代码，请编写：

    ```ruby
    require 'tabbit'
    table = Tabbit.new('Name', 'Email')
    table.add_row('Tim Green', 'tiimgreen@gmail.com')
    puts table.to_s
    ```

这将产生：

```ruby
require 'tabbit'
table = Tabbit.new('Name', 'Email')
table.add_row('Tim Green', 'tiimgreen@gmail.com')
puts table.to_s
```

GitHub 使用 [Linguist](https://github.com/github/linguist) 来执行语言检测和语法突出显示。您可以通过仔细阅读[语言 YAML 文件](https://github.com/github/linguist/blob/master/lib/linguist/languages.yml) 找出哪些关键字有效。

[*阅读有关 GitHub Flavored Markdown 的更多信息。*](https://help.github.com/articles/github-flavored-markdown/)

### 表情符号
可以使用 `:name_of_emoji:` 将表情符号添加到拉取请求、问题、提交消息、存储库描述等中。

GitHub 上支持的表情符号的完整列表可以在 [emoji-cheat-sheet.com](http://www.emoji-cheat-sheet.com/) 或 [scotch-io/All-Github-Emoji-Icons](https://github.com/scotch-io/All-Github-Emoji-Icons) 中找到。
方便的表情符号搜索引擎可以在 [emoji.muan.co](http://emoji.muan.co/) 找到。

GitHub 上使用最多的 5 个表情符号是：

1. `:shipit:`
2.`：闪闪发光：`
3. `:-1:`
4. `:+1:`
5.`：拍手：`

### 图片/GIF
图像和 GIF 可以添加到评论、自述文件等中：

```
![Alt Text](http://www.sheawong.com/wp-content/uploads/2013/08/keephatin.gif)
```

可以通过直接调用来使用存储库中的原始图像：

```
![Alt Text](https://github.com/{user}/{repo}/raw/master/path/to/image.gif)
```

![Peter don't care](http://www.sheawong.com/wp-content/uploads/2013/08/keephatin.gif)

所有图像都缓存在 GitHub 上，因此如果您的主机出现故障，图像将仍然可用。

#### 在 GitHub Wiki 中嵌入图像
在 Wiki 页面中嵌入图像的方法有多种。有标准的 Markdown 语法（如上所示）。但还有一种语法允许指定图像的高度或宽度之类的操作：

```markdown
[[ http://www.sheawong.com/wp-content/uploads/2013/08/keephatin.gif | height = 100px ]]
```

其产生：

![Just a screenshot](http://i.imgur.com/J5bMf7S.png)

### 快速报价
当您在评论线程中想要引用某人之前说过的内容时，突出显示文本并按“r”，这会将其以块引用格式复制到文本框中。

![Quick Quote](https://f.cloud.github.com/assets/296432/124483/b0fa6204-6ef0-11e2-83c3-256c37fa7abc.gif)

[*阅读有关快速引用的更多信息。*](https://github.com/blog/1399-quick-quotes)

### 将剪贴板图像粘贴到评论

_（仅适用于 Chrome 浏览器）_

截图并将其添加到剪贴板（mac：`cmd-ctrl-shift-4`）后，您只需将图像粘贴（`cmd-v / ctrl-v`）到评论部分，它将自动上传到 github。

![Pasting Clipboard Image to Comments](https://cloud.githubusercontent.com/assets/39191/5794265/39c9b65a-9f1b-11e4-9bc7-04e41f59ea5f.png)

[*阅读有关问题附件的更多信息。*](https://help.github.com/articles/issue-attachments/)

### 快速授权
创建存储库时，GitHub 为您提供添加预制许可证的选项：

![License](http://i.imgur.com/Chqj4Fg.png)

您还可以通过 Web 界面创建新文件，将它们添加到现有存储库中。当输入名称“LICENSE”时，您将获得使用模板的选项：

![License](http://i.imgur.com/fTjQict.png)

也适用于“.gitignore”。

[*阅读有关开源许可的更多信息。*](https://help.github.com/articles/open-source-licensing/)

### 任务列表
在“问题”和“拉取请求”中，可以使用以下语法添加复选框（注意空格）：

```
- [ ] Be awesome
- [ ] Prepare dinner
  - [ ] Research recipe
  - [ ] Buy ingredients
  - [ ] Cook recipe
- [ ] Sleep
```

![Task List](http://i.imgur.com/jJBXhsY.png)

当它们被点击时，它们将在纯 Markdown 中更新：

```
- [x] Be awesome
- [ ] Prepare dinner
  - [x] Research recipe
  - [x] Buy ingredients
  - [ ] Cook recipe
- [ ] Sleep
```

[*阅读有关任务列表的更多信息。*](https://help.github.com/articles/writing-on-github/#task-lists)

#### Markdown 文档中的任务列表
在完整的 Markdown 文档中，现在可以使用以下语法添加**只读**清单：

```
- [ ] Mercury
- [x] Venus
- [x] Earth
  - [x] Moon
- [x] Mars
  - [ ] Deimos
  - [ ] Phobos
```

- [ ] 水星
- [x] 金星
- [x] 地球
- [x] 月亮
- [x] 火星
- [ ] 火卫二
- [ ] 火卫一

[*阅读有关 Markdown 文档中任务列表的更多信息。*](https://github.com/blog/1825-task-lists-in-all-markdown-documents)

### 相关链接
链接到内部内容时，建议在 Markdown 文件中使用相对链接。

```markdown
[Link to a header](#awesome-section)
[Link to a file](docs/readme)
```

每当 URL 更改时（例如，存储库重命名、用户名更改、项目分叉），绝对链接都必须更新。使用相对链接可以使您的文档轻松独立。

[*阅读有关相对链接的更多信息。*](https://help.github.com/articles/relative-links-in-readmes/)

### GitHub 页面的元数据和插件支持
在 Jekyll 页面和帖子中，存储库信息在“site.github”命名空间中可用，并且可以使用“{{ site.github.project_title }}”等方式显示。

Jemoji 和 jekyll-mentions 插件使您的 Jekyll 帖子和页面中的 [emoji](#emojis) 和 [@mentions](https://github.com/blog/821) 能够像您在 GitHub.com 上的存储库交互时所期望的那样工作。

[*阅读有关 GitHub Pages 的存储库元数据和插件支持的更多信息。*](https://github.com/blog/1797-repository-metadata-and-plugin-support-for-github-pages)

### 查看文档中的 YAML 元数据
许多博客网站，例如 [Jekyll](http://jekyllrb.com/) 和 [GitHub Pages](https://pages.github.com)，都依赖于帖子开头的一些 YAML 格式的元数据。 GitHub 会将这些元数据呈现为水平表格，以便于阅读

![YAML metadata](https://camo.githubusercontent.com/47245aa16728e242f74a9a324ce0d24c0b916075/68747470733a2f2f662e636c6f75642e6769746875622e636f6d2f6173736574732f36343035302f313232383236372f65303439643063362d323761302d313165332d396464382d6131636432323539393334342e706e67)

[*阅读有关在文档中查看 YAML 元数据的更多信息。*](https://github.com/blog/1647-viewing-yaml-metadata-in-your-documents)

### 渲染表格数据
GitHub 支持以“.csv”（逗号分隔）和“.tsv”（制表符分隔）文件形式呈现表格数据。

![Tabular data](https://camo.githubusercontent.com/1b6dd0157ffb45d9939abf14233a0cb13b3b4dfe/68747470733a2f2f662e636c6f75642e6769746875622e636f6d2f6173736574732f3238323735392f3937363436322f33323038336463652d303638642d313165332d393262322d3566323863313061353035392e706e67)

[*阅读有关渲染表格数据的更多信息。*](https://github.com/blog/1601-see-your-csvs)

### 渲染 PDF

GitHub 支持渲染 PDF：

![PDF](https://cloud.githubusercontent.com/assets/1000669/7492902/f8493160-f42e-11e4-8cea-1cb4f02757e7.png)

[*阅读有关渲染 PDF 的更多信息。*](https://github.com/blog/1974-pdf-viewing)

### 恢复拉取请求
合并拉取请求后，您可能会发现它没有任何帮助，或者合并拉取请求是一个错误的决定。

您可以通过单击拉取请求页面中提交右侧的 **恢复** 按钮来恢复它，以创建一个拉取请求，并恢复对此特定拉取请求的更改。

![Revert button](https://camo.githubusercontent.com/0d3350caf2bb1cba53123ffeafc00ca702b1b164/68747470733a2f2f6769746875622d696d616765732e73332e616d617a6f6e6177732e636f6d2f68656c702f70756c6c5f72657175657374732f7265766572742d70756c6c2d726571756573742d6c696e6b2e706e67)

[*阅读有关恢复拉取请求的更多信息*](https://github.com/blog/1857-introducing-the-revert-button)

### 差异
#### 渲染散文差异
提交和拉取请求，包括 GitHub 支持的渲染文档（例如 Markdown）、功能*源*和*渲染*视图。

![Source / Rendered view](https://github-images.s3.amazonaws.com/help/repository/rendered_prose_diff.png)

单击“渲染”按钮以查看将在渲染文档中显示的更改。添加、删除和编辑文本时，渲染散文视图非常方便：

![Rendered Prose Diffs](https://f.cloud.github.com/assets/17715/2003056/3997edb4-862b-11e3-90be-5e9586edecd7.png)

[*阅读有关渲染散文差异的更多信息。*](https://github.com/blog/1784-rendered-prose-diffs)

#### 可区分贴图
每当您在 GitHub 上查看包含地理数据的提交或拉取请求时，GitHub 都会呈现更改内容的可视化表示。

[![Diffable Maps](https://f.cloud.github.com/assets/282759/2090660/63f2e45a-8e97-11e3-9d8b-d4c8078b004e.gif)](https://github.com/benbalter/congressional-districts/commit/2233c76ca5bb059582d796f053775d8859198ec5)

[*阅读有关 diffable 贴图的更多信息。*](https://github.com/blog/1772-diffable-more-customizable-maps)

#### 扩展差异中的上下文
使用差异的装订线中的“展开”按钮，您可以通过单击显示其他上下文行。您可以继续单击“展开”，直到显示整个文件，并且该功能在 GitHub 呈现差异的任何地方都可用。

![Expanding Context in Diffs](https://f.cloud.github.com/assets/22635/1610539/863c1f64-5584-11e3-82bf-151b406a272f.gif)

[*阅读有关在差异中扩展上下文的更多信息。*](https://github.com/blog/1705-expanding-context-in-diffs)

#### Pull 请求的差异或补丁
您可以通过添加“.diff”或“.patch”来获取拉取请求的差异
扩展名到 URL 的末尾。例如：

```
https://github.com/tiimgreen/github-cheat-sheet/pull/15
https://github.com/tiimgreen/github-cheat-sheet/pull/15.diff
https://github.com/tiimgreen/github-cheat-sheet/pull/15.patch
```

`.diff` 扩展名将以纯文本形式提供：

```
diff --git a/README.md b/README.md
index 88fcf69..8614873 100644
--- a/README.md
+++ b/README.md
@@ -28,6 +28,7 @@ All the hidden and not hidden features of Git and GitHub. This cheat sheet was i
 - [Merged Branches](#merged-branches)
 - [Quick Licensing](#quick-licensing)
 - [TODO Lists](#todo-lists)
+- [Relative Links](#relative-links)
 - [.gitconfig Recommendations](#gitconfig-recommendations)
     - [Aliases](#aliases)
     - [Auto-correct](#auto-correct)
@@ -381,6 +382,19 @@ When they are clicked, they will be updated in the pure Markdown:
 - [ ] Sleep

(...)
```

#### 渲染和比较图像
GitHub 可以显示多种常见的图像格式，包括 PNG、JPG、GIF 和 PSD。此外，还有多种方法可以比较这些图像格式版本之间的差异。

[![Diffable PSD](https://cloud.githubusercontent.com/assets/2546/3165594/55f2798a-eb56-11e3-92e7-b79ad791a697.gif)](https://github.com/blog/1845-psd-viewing-diffing)

[*阅读有关渲染和比较图像的更多信息。*](https://help.github.com/articles/rendering-and-diffing-images/)

### 枢纽
[Hub](https://github.com/github/hub) 是一个命令行 Git 包装器，它为您提供了额外的功能和命令，使您可以更轻松地使用 GitHub。

这允许您执行以下操作：

```bash
$ hub clone tiimgreen/toc
```

[*查看 Hub 提供的一些更酷的命令。*](https://github.com/github/hub#commands)

### 贡献指南
GitHub 支持添加 3 个不同的文件，帮助用户为您的项目做出贡献。
这些文件可以放置在存储库的根目录中，也可以放置在根目录下的“.github”目录中。

#### 贡献文件
将“CONTRIBUTING”或“CONTRIBUTING.md”文件添加到存储库的根目录或“.github”目录中，将在贡献者创建问题或打开拉取请求时添加指向您文件的链接。

![Contributing Guidelines](https://camo.githubusercontent.com/71995d6b0e620a9ef1ded00a04498241c69dd1bf/68747470733a2f2f6769746875622d696d616765732e73332e616d617a6f6e6177732e636f6d2f736b697463682f6973737565732d32303132303931332d3136323533392e6a7067)

[*阅读有关贡献指南的更多信息。*](https://github.com/blog/1184-contributing-guidelines)

#### ISSUE_TEMPLATE 文件
您可以为项目中打开的所有新问题定义一个模板。当用户创建新问题时，此文件的内容将预先填充新问题框。将“ISSUE_TEMPLATE”或“ISSUE_TEMPLATE.md”文件添加到存储库的根目录或“.github”目录中。

[*阅读有关问题模板的更多信息。*](https://github.com/blog/2111-issue-and-pull-request-templates)

[问题模板文件生成器](https://www.talater.com/open-source-templates/)

![GitHub Issue template](https://cloud.githubusercontent.com/assets/25792/13120859/733479fe-d564-11e5-8a1f-a03f95072f7a.png)

#### PULL_REQUEST_TEMPLATE 文件
您可以为项目中打开的所有新拉取请求定义模板。当用户创建拉取请求时，此文件的内容将预先填充文本区域。将“PULL_REQUEST_TEMPLATE”或“PULL_REQUEST_TEMPLATE.md”文件添加到存储库的根目录或“.github”目录中。

[*阅读有关拉取请求模板的更多信息。*](https://github.com/blog/2111-issue-and-pull-request-templates)

[拉取请求模板文件生成器](https://www.talater.com/open-source-templates/)

### 奥克蒂康斯
GitHub 的图标（Octicons）现已开源。

![Octicons](https://og.github.com/octicons/octicons@1200x630.png)

[*阅读有关 GitHub Octicons 的更多信息*](https://octicons.github.com)

### GitHub 学生开发包

如果您是学生，您将有资格获得 GitHub 学生开发者包。这为您提供免费信用、免费试用和早期访问对您开发有帮助的软件。

![GitHub Student Developer Pack](http://i.imgur.com/9ru3K43.png)

[*阅读有关 GitHub 学生开发包的更多信息*](https://education.github.com/pack)

### GitHub 资源
|标题 |链接 |
| ----- | ---- |
| GitHub 探索 | https://github.com/explore |
| GitHub 博客 | https://github.com/blog |
| GitHub 帮助 | https://help.github.com/ |
| GitHub 培训 | https://training.github.com/ |
| GitHub 开发者 | https://developer.github.com/ |
| Github Education（为学生提供免费微型帐户和其他东西）| https://education.github.com/ |
| GitHub 最佳实践 | [最佳实践列表](https://www.datree.io/resources/github-best-practices) |

#### GitHub 讲座
|标题 |链接 |
| ----- | ---- |
| GitHub 如何使用 GitHub 构建 GitHub | https://www.youtube.com/watch?v=qyz3jkOBbQY |
|与 GitHub 的 Scott Chacon 一起介绍 Git | https://www.youtube.com/watch?v=ZDR433b0HJY |
| GitHub 如何不再工作 | https://www.youtube.com/watch?v=gXD1ITW7iZI |
| Git 和 GitHub 的秘密 | https://www.youtube.com/watch?v=Foz9yvMkvlA |
|更多 Git 和 GitHub 秘密 | https://www.youtube.com/watch?v=p50xsL-iVgU |

### SSH 密钥

您可以通过访问以下地址获取纯文本格式的公共 ssh 密钥列表：

```
https://github.com/{user}.keys
```

例如[https://github.com/tiimgreen.keys](https://github.com/tiimgreen.keys)

[*阅读有关访问公共 ssh 密钥的更多信息。*](https://changelog.com/github-exposes-public-ssh-keys-for-its-users/)

### 个人资料图片

您可以通过访问以下地址获取用户的个人资料图片：

```
https://github.com/{user}.png
```

例如[https://github.com/tiimgreen.png](https://github.com/tiimgreen.png)

### 存储库模板

您可以在存储库上启用模板，允许任何人复制目录结构和文件，从而允许他们立即使用这些文件（例如用于教程或编写样板代码）。这可以在存储库的设置中启用。

![Convert](https://i.postimg.cc/hGCrVm9F/Template.gif)

更改为模板存储库将提供一个新的 URL 端点，该端点可以共享并立即允许用户将您的存储库用作模板。或者，他们可以转到您的存储库并单击“用作模板”按钮。

![Template](https://i.postimg.cc/L8PKCHx0/New-Template.gif)

[*阅读有关使用存储库作为模板的更多信息*](https://github.blog/2019-06-06-generate-new-repositories-with-repository-templates/)

## git
### 从工作树中删除所有已删除的文件
当您使用“/bin/rm”删除大量文件时，您可以使用以下命令将它们从工作树和索引中删除，从而无需单独删除每个文件：

```bash
$ git rm $(git ls-files -d)
```

例如：

```bash
$ git status
On branch master
Changes not staged for commit:
	deleted:    a
	deleted:    c

$ git rm $(git ls-files -d)
rm 'a'
rm 'c'

$ git status
On branch master
Changes to be committed:
	deleted:    a
	deleted:    c
```

### 以前的分行
要移动到 Git 中的上一个分支：

```bash
$ git checkout -
# Switched to branch 'master'

$ git checkout -
# Switched to branch 'next'

$ git checkout -
# Switched to branch 'master'
```

[*阅读有关 Git 分支的更多信息。*](http://git-scm.com/book/en/Git-Branching-Basic-Branching-and-Merging)

### 条带空间

Git 剥离空间：

- 去除尾随空白
- 折叠换行符
- 在文件末尾添加换行符

调用命令时必须传递一个文件，例如：
```bash
$ git stripspace < README.md
```

[*阅读有关 Git `stripspace` 命令的更多信息。*](http://git-scm.com/docs/git-stripspace)

### 检查拉取请求

Pull 请求是 GitHub 存储库上的特殊分支，可以通过多种方式在本地检索：

检索特定的拉取请求并将其临时存储在“FETCH_HEAD”中，以便快速进行“比较”或“合并”：

```bash
$ git fetch origin refs/pull/[PR-Number]/head
```

通过 refspec 获取所有 Pull Request 分支作为本地远程分支：

```bash
$ git fetch origin '+refs/pull/*/head:refs/remotes/origin/pr/*'
```

或者通过在存储库的“.git/config”中添加这些相应的行来设置远程自动获取拉取请求：

```
[remote "origin"]
    fetch = +refs/heads/*:refs/remotes/origin/*
    url = git@github.com:tiimgreen/github-cheat-sheet.git
```

```
[remote "origin"]
    fetch = +refs/heads/*:refs/remotes/origin/*
    url = git@github.com:tiimgreen/github-cheat-sheet.git
    fetch = +refs/pull/*/head:refs/remotes/origin/pr/*
```

对于基于分叉的拉取请求贡献，“签出”代表拉取请求的远程分支并从中创建本地分支非常有用：

```bash
$ git checkout pr/42 pr-42
```

或者，如果您要处理更多存储库，您可以在全局 git 配置中全局配置获取拉取请求。

```bash
git config --global --add remote.origin.fetch "+refs/pull/*/head:refs/remotes/origin/pr/*"
```

这样，您就可以在所有存储库中使用以下简短命令：

```bash
git fetch origin
```

```bash
git checkout pr/42
```

[*阅读有关在本地检查拉取请求的更多信息。*](https://help.github.com/articles/checking-out-pull-requests-locally/)

### 空提交
通过添加“--allow-empty”，可以在不更改代码的情况下推送提交：

```bash
$ git commit -m "Big-ass commit" --allow-empty
```

一些用例（有意义）包括：

- 注释大量新工作或新功能的开始。
- 当您对项目进行与代码无关的更改时进行记录。
- 与使用您的存储库的人进行交流。
- 存储库的第一次提交：`git commit -m "Initial commit" --allow-empty`。

### 样式化的 Git 状态
运行：

```bash
$ git status
```

产生：

![git status](http://i.imgur.com/qjPyvXb.png)

通过添加`-sb`：

```bash
$ git status -sb
```

这是产生的：

![git status -sb](http://i.imgur.com/K0OY3nm.png)

[*阅读有关 Git `status` 命令的更多信息。*](http://git-scm.com/docs/git-status)

### 样式化的 Git 日志
运行：

```bash
$ git log --all --graph --pretty=format:'%Cred%h%Creset -%C(auto)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit --date=relative
```

产生：

![git log --all --graph --pretty=format:'%Cred%h%Creset -%C(auto)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit --date=relative](http://i.imgur.com/58eOtkW.png)

感谢 [Palesz](http://stackoverflow.com/users/88355/palesz)

*可以使用[此处](https://github.com/tiimgreen/github-cheat-sheet#aliases)中的说明为其设置别名。*

[*阅读有关 Git `log` 命令的更多信息。*](http://git-scm.com/docs/git-log)

### git查询
Git 查询允许您搜索所有以前的提交消息并找到与查询匹配的最新消息。

```bash
$ git show :/query
```

其中“query”（区分大小写）是您要搜索的术语，然后查找最后一个术语并提供有关已更改行的详细信息。

```bash
$ git show :/typo
```
![git show :/query](http://i.imgur.com/icaGiNt.png)

*按“q”退出。*


### git grep

Git Grep 将返回与模式匹配的行列表。

运行：
```bash
$ git grep aliases
```
将显示包含字符串 *aliases* 的所有文件。

![git grep aliases](http://i.imgur.com/DL2zpQ9.png)

*按“q”退出。*

您还可以使用多个标志进行更高级的搜索。例如：

* `-e` 下一个参数是模式（例如，正则表达式）
* `--and`、`--or` 和 `--not` 组合多种模式。

像这样使用它：
```bash
 $ git grep -e pattern --and -e anotherpattern
```

[*阅读有关 Git `grep` 命令的更多信息。*](http://git-scm.com/docs/git-grep)

### 合并分支
运行：

```bash
$ git branch --merged
```

将为您提供已合并到当前分支的所有分支的列表。

反之：

```bash
$ git branch --no-merged
```

将为您提供尚未合并到当前分支的分支列表。

[*阅读有关 Git `branch` 命令的更多信息。*](http://git-scm.com/docs/git-branch)

### 修复和自动挤压
如果之前的提交有问题（可以是 HEAD 中的一个或多个），例如“abcde”，请在修改问题后运行以下命令：
```bash
$ git commit --fixup=abcde
$ git rebase abcde^ --autosquash -i
```
[*阅读有关 Git `commit` 命令的更多信息。*](http://git-scm.com/docs/git-commit)
[*阅读有关 Git `rebase` 命令的更多信息。*](http://git-scm.com/docs/git-rebase)

### 用于浏览本地存储库的 Web 服务器
使用 Git `instaweb` 命令立即浏览 `gitweb` 中的工作存储库。此命令是一个简单的脚本，用于设置 `gitweb` 和用于浏览本地存储库的 Web 服务器。

```bash
$ git instaweb
```

打开：

![Git instaweb](http://i.imgur.com/Dxekmqc.png)

[*阅读有关 Git `instaweb` 命令的更多信息。*](http://git-scm.com/docs/git-instaweb)

### Git 配置
您的 .gitconfig 文件包含所有 Git 配置。

#### 别名
别名是让您定义自己的 git 调用的助手。例如，您可以设置“git a”来运行“git add --all”。

要添加别名，请导航到“~/.gitconfig”并按以下格式填写：

```
[alias]
  co = checkout
  cm = commit
  p = push
  # Show verbose output about tags, branches or remotes
  tags = tag -l
  branches = branch -a
  remotes = remote -v
```

...或者在命令行中输入：

```bash
$ git config --global alias.new_alias git_function
```

例如：

```bash
$ git config --global alias.cm commit
```

对于具有多个函数的别名，请使用引号：

```bash
$ git config --global alias.ac 'add -A . && commit'
```

一些有用的别名包括：

|别名 |命令 |输入什么 |
| --- | --- | --- |
| `git cm` | `git 提交` | `git config --global alias.cm commit` |
| `git co` | `git checkout` | `git config --global alias.co checkout` |
| `git ac` | `git add . -A``git 提交` | `git config --global alias.ac '!git add -A && git commit'` |
| `git st` | `git status -sb` | `git config --global alias.st 'status -sb'` |
| `git 标签` | `git tag -l` | `git config --global alias.tags 'tag -l'` |
| `git 分支` | `git 分支 -a` | `git config --global alias.branches 'branch -a'` |
| `git 清理` | `git 分支 --merged \| grep -v '*' \| xargs git 分支 -d` | `git config --global alias.cleanup "!gitbranch --merged \| grep -v '*' \| xargs gitbranch -d"` |
| `git 远程` | `git 远程-v` | `git config --global alias.remotes 'remote -v'` |
| `git lg` | `git log --color --graph --pretty=format:'%Cred%h%Creset -%C(黄色)%d%Creset %s %Cgreen(%cr) %C(粗体蓝色)<%an>%Creset' --abbrev-commit --` | `git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit --"` |

*一些别名取自 [@mathiasbynens](https://github.com/mathiasbynens) 点文件：https://github.com/mathiasbynens/dotfiles/blob/master/.gitconfig*

#### 自动更正
Git 为拼写错误的命令提供建议，如果启用自动更正，则可以自动修复并执行该命令。通过指定一个整数来启用自动更正，该整数是 git 运行更正命令之前的十分之一秒的延迟。零是默认值，不会进行任何校正，负值将不延迟地运行校正后的命令。

例如，如果您输入“git comit”，您将得到：

```bash
$ git comit -m "Message"
# git: 'comit' is not a git command. See 'git --help'.

# Did you mean this?
#   commit
```

可以像这样启用自动更正（有 1.5 秒延迟）：

```bash
$ git config --global help.autocorrect 15
```

所以现在命令 `git comit` 将自动更正为 `git commit`，如下所示：

```bash
$ git comit -m "Message"
# WARNING: You called a Git command named 'comit', which does not exist.
# Continuing under the assumption that you meant 'commit'
# in 1.5 seconds automatically...
```

git 重新运行命令之前的延迟是为了让用户有时间中止。

#### 颜色
要为 Git 输出添加更多颜色：

```bash
$ git config --global color.ui 1
```

[*阅读有关 Git `config` 命令的更多信息。*](http://git-scm.com/docs/git-config)

### Git 资源
|标题 |链接 |
| ----- | ---- |
| Git 官方网站 | http://git-scm.com/ |
|官方 Git 视频教程 | http://git-scm.com/videos |
|代码学校尝试 Git | http://try.github.com/ |
| Git 入门参考和教程 | http://gitref.org/|
|官方 Git 教程 | http://git-scm.com/docs/gittutorial | http://git-scm.com/docs/gittutorial |
|日常 Git | http://git-scm.com/docs/everyday |
| Git 沉浸 | http://gitimmersion.com/ |
|吉特神| https://github.com/gorosgobe/git-god |
|计算机科学家的 Git | http://eagain.net/articles/git-for-computer-scientists/ | http://eagain.net/articles/git-for-computer-scientists/ |
| Git 魔法 | http://www-cs-students.stanford.edu/~blynn/gitmagic/ | http://www-cs-students.stanford.edu/~blynn/gitmagic/ |
| Git 可视化游乐场 | http://onlywei.github.io/explain-git-with-d3/#freeplay |
|学习 Git 分支 | http://pcottle.github.io/learnGitBranching/ |
|有用的 .gitignore 模板集合 | https://github.com/github/gitignore |
| Unixorn 的 git-extra-commands git 脚本集合 | https://github.com/unixorn/git-extra-commands |

#### Git 书籍
|标题 |链接 |
| ----- | ---- |
|使用 Git 进行实用的版本控制 | https://pragprog.com/titles/tsgit/pragmatic-version-control-using-git | https://pragprog.com/titles/tsgit/pragmatic-version-control-using-git |
|专业 Git | http://git-scm.com/book |
| Git 内部结构 PluralSight | https://github.com/pluralsight/git-internals-pdf |
| Git 的战壕 | http://cbx33.github.io/gitt/ | http://cbx33.github.io/gitt/
|使用 Git 进行版本控制 | http://www.amazon.com/Version-Control-Git-collaborative-development/dp/1449316387 |
| Git 实用指南 | https://pragprog.com/titles/pg_git/pragmatic-guide-to-git | https://pragprog.com/titles/pg_git/pragmatic-guide-to-git |
| Git：适合所有人的版本控制 | https://www.packtpub.com/application-development/git-version-control-everyone | https://www.packtpub.com/application-development/git-version-control-everyone

#### git 视频
|标题 |链接 |
| ----- | ---- |
| Git 上的 Linus Torvalds | https://www.youtube.com/watch?v=4XpnKHJAok8 |
| Scott Chacon 介绍 Git | https://www.youtube.com/watch?v=ZDR433b0HJY |
| Git 从零开始 | https://www.youtube.com/watch?v=MYP56QJpDr4 |
|图、散列和压缩，天哪！ | https://www.youtube.com/watch?v=ig5E8CcdM9g |
| GitHub 培训和指南 | https://www.youtube.com/watch?list=PLg7s6cbtAD15G8lNyoaYDuKZSKyJrgwB-&v=FyfwLX4HAxM |

#### git 文章
|标题 |链接 |
| ----- | ---- |
| GitHub 流程 | http://scottchacon.com/2011/08/31/github-flow.html |
|迁移到 Git 大文件存储 (Git LFS) | http://vooban.com/en/tips-articles-geek-stuff/migration-to-git-lfs-for-developing-deep-learning-applications-with-large-files/|
