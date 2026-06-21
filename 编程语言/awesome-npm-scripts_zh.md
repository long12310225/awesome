<!--lint ignore awesome-heading-->
# 很棒的 npm 脚本 [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[<img src="npm-logo.png"align="right"width="150">](https://www.npmjs.com)

> 使用 npm 作为构建工具一切都很棒。

您可能还喜欢 [awesome-npm](https://github.com/sindresorhus/awesome-npm)。

**注意：我目前太忙，无法主动扩展此列表；因此，我决定将其作为一个[OPEN开源项目](http://openopensource.github.io/)。做出重大和有价值贡献的个人将获得对该项目的承诺访问权限，以做出他们认为合适的贡献。**

## 内容

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Articles](#articles)
- [Videos/Talks](#videostalks)
- [任务运行器](#task-runners)
- [文件观察者](#file-watchers)
- [开发服务器](#dev-servers)
- [跨平台实用程序](#cross-platform-utilities)
  - [实用包](#utility-packs)
- [其他实用程序](#other-utilities)
- [Miscellaneous](#miscellaneous)
- [跨平台 Shell 参考](#cross-platform-shell-reference)
- [`npm run` 参考](#npm-run-reference)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## 文章

- [Why we should stop using Grunt & Gulp](https://www.keithcirkel.co.uk/why-we-should-stop-using-grunt/) - Keith Cirkel 的博客文章。
- [How to Use npm as a Build Tool](https://www.keithcirkel.co.uk/how-to-use-npm-as-a-build-tool/) - 《为什么我们应该停止使用 Grunt & Gulp》的续集。
- [Why I Left Gulp and Grunt for npm Scripts](https://medium.freecodecamp.com/why-i-left-gulp-and-grunt-for-npm-scripts-3d6853dd22b8) - 科里·豪斯的文章。
- [Helpers and tips for npm run scripts](http://michael-kuehnel.de/tooling/2018/03/22/helpers-and-tips-for-npm-run-scripts.html) - Michael Kühnel 撰写的博客文章涵盖高级主题。
- [Running cross-platform tasks via npm package scripts](https://exploringjs.com/nodejs-shell-scripting/ch_package-scripts.html) - Axel Rauschmayer 博士撰写的最全面的 npm 脚本使用指南。

## 视频/讲座

- [Advanced front-end automation with npm scripts](https://www.youtube.com/watch?v=0RYETb9YVrk) - Kate Hudson 在 Nordic.js 2015 上的演讲。
- [How to create a build system with npm scripts](http://www.penta-code.com/how-to-create-a-build-system-with-npm-scripts/) - 有关设置前端构建系统的视频教程系列。

## 任务运行器

用于并行或顺序运行多个命令或 npm 脚本的工具。

- [script-runner](https://github.com/paulpflug/script-runner) - 具有简洁语法的简单任务运行程序。
- [npm-run-all](https://github.com/mysticatea/npm-run-all) - 功能齐全的任务运行程序。
- [redrun](https://github.com/coderaiser/redrun) - 从 package.json 扩展脚本以提高执行速度。

## 文件观察者

用于监视源文件并在任何文件发生更改时运行构建命令的工具。

- [onchange](https://github.com/Qard/onchange) - `onchange <glob> -- <命令>`。
- [watch](https://github.com/mikeal/watch) - `watch <命令> <目录>`。

## 开发服务器

- [http-server](https://github.com/indexzero/http-server) - 简单的零配置命令行 http 服务器。
- [live-server](https://github.com/tapio/live-server) - 具有实时重新加载功能的简单开发 http 服务器。

## 跨平台实用程序

用于执行常见命令行任务而无需担心跨平台兼容性的实用程序。

- [rimraf](https://github.com/isaacs/rimraf) - 删除文件或目录；就像“rm -rf”。
- [del-cli](https://github.com/sindresorhus/del-cli) - 更安全的文件和文件夹删除。
- [mkdirp](https://github.com/substack/node-mkdirp) - 创建目录，如果需要则创建父目录；就像`mkdir -p`。
- [cpr](https://github.com/davglass/cpr) - Node.js 的“cp -r”。
- [cpy-cli](https://github.com/sindresorhus/cpy-cli) - 文件/目录复制/重命名。
- [copyfiles](https://github.com/calvinmetcalf/copyfiles) - 将文件列表复制到目录中。
- [sync-files](https://github.com/byteclubfr/node-sync-files) - 类似于“rsync”的目录与监视模式同步。
- [echo-cli](https://github.com/iamakulov/echo-cli) - 具有 JS 转义序列支持的跨平台“echo”。
- [clear-cli](https://github.com/sindresorhus/clear-cli) - 清除终端。
- [cross-env](https://github.com/kentcdodds/cross-env) - 设置脚本的环境变量，unix 风格。
- [cross-os](https://github.com/milewski/cross-os) - 运行特定于平台的 npm 脚本。
- [ntee](https://github.com/stefanmaric/ntee) - 从标准输入读取并写入标准输出和文件的实用程序；就像 Unix 的 `tee` 一样。
- [catw](https://github.com/substack/catw) - 将文件打印到标准输出，并具有可选的监视模式；有点像 Unix 的“cat”。

### 实用包

- [shx](https://github.com/shelljs/shx) - 在 Node.js 中实现的常见 Unix 实用程序的集合；用法示例：`shx rm somefile`。

## 其他实用程序

- [hashmark](https://github.com/keithamus/hashmark) - 获取文件内容并输出为名称中包含哈希值的新文件。
- [gzip-size-cli](https://github.com/sindresorhus/gzip-size-cli) - 获取文件或标准输入的 gzip 压缩大小。
- [opn-cli](https://github.com/sindresorhus/opn-cli) - 使用用户首选的应用程序打开网站、文件、可执行文件等。
- [headr](https://github.com/heldr/headr) - 将标题/横幅信息添加到文件中。
- [Bower files CLI](https://github.com/thompsonemerson/bower-files-cli) - 在命令行上获取主要的 Bower 文件。
- [cli-error-notifier](https://github.com/micromata/cli-error-notifier) - 当 npm 脚本失败时发送本机桌面通知。

## 杂项

- [screwy](https://github.com/samueleaton/screwy) - npm 脚本 GUI。
- [Forrest](https://github.com/stefanjudis/forrest) - npm 脚本桌面客户端。
- [run-npm](https://github.com/timoxley/npm-run) - 运行本地安装的节点模块可执行文件。对于调试 npm 脚本很有用。
- [npm-quick-run](https://github.com/bahmutov/npm-quick-run) - 通过前缀快速运行 npm 脚本，无需输入全名。
- [edit-script](https://github.com/RyanZim/edit-script) - 从命令行编辑 npm 脚本，无需担心 JSON 转义。
- [ntl](https://github.com/ruyadorno/ntl) - 用于列出和运行 npm 脚本的交互式 cli 菜单。

## 跨平台 Shell 参考

在 Unix 和 Windows 上工作相同的 shell 操作符和命令的快速参考。

- 使用“&&”按顺序运行命令。如果命令失败，脚本将退出。
- 使用“|”将一个命令的标准输出通过管道传输到下一个命令的标准输入。 (`做某事 | 做别的事`)
- 使用“>”将命令的标准输出写入文件。 (`做某事>文件`)
- 使用“<”将文件的内容发送到命令的标准输入。 (`命令<文件`)
- 使用“cd <dir>”将当前工作目录更改为“<dir>”。请注意，在 Windows 上，“cd”单独打印当前工作目录，但在 \*nix 上将工作目录更改为“~”。

## `npm run` 参考

您可以使用“npm run-script”或“npm run”；它们都做同样的事情，但是 `npm run` 更短。

- 只需运行“npm run”即可打印脚本列表。
- 运行“npm run script”（其中“script”是脚本的名称）将运行“prescript”、“script”和“postscript”；按这个顺序。
- 你不能嵌套`pre`和`post`钩子（即`preprescript`不起作用）。
- 您可以通过将“--”传递给“npm run”，然后传递参数来将参数传递给脚本。示例：给定脚本 `"mocha": "mocha"`，您可以运行 `npm run mocha -- --reporter xunit`。这有效地运行了“mocha --reporter xunit”。
- 运行“npm test”与运行“npm run test”相同。这同样适用于“npm start”和“npm stop”。
- 您可以运行“npm run <script> -s”来静默默认的 npm 输出（对于在另一个脚本中调用脚本很有用）。

## 贡献

请参阅 [CONTRIBUTING.md](https://github.com/RyanZim/awesome-npm-scripts/blob/master/CONTRIBUTING.md)。
