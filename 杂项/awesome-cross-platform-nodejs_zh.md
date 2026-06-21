<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="logo_dark.svg"/>
    <img alt="awesome-cross-platform-nodejs logo" src="logo.svg" width="500"/>
  </picture>
  <br>
  <a href="https://awesome.re">
	  <img src="https://awesome.re/badge.svg" alt="Awesome">
  </a>
  <p>A curated list of awesome developer tools for writing cross-platform Node.js code.</p>
</div>

## 内容

- [Resources](#resources)
- [Applications](#applications)
  - [开发环境](#development-environment)
  - [持续集成](#continuous-integration)
  - [Virtualization](#virtualization)
  - [Compatibility](#compatibility)
  - [Databases](#databases)
- [Libraries](#libraries)
  - [操作系统识别](#os-identification)
  - [Shell](#shell)
  - [Environment](#environment)
  - [Filesystem](#filesystem)
  - [Signals](#signals)
  - [Processes](#processes)
  - [Streams](#streams)
  - [桌面用户界面](#desktop-ui)
  - [Windows注册表](#windows-registry)
- [已知问题](#known-issues)
- [Support](#support)

## 资源

- [Core Node.js documentation](https://nodejs.org/en/docs/) - 特别是 [`os`](https://nodejs.org/api/os.html)、[`path`](https://nodejs.org/api/path.html)、[`fs`](https://nodejs.org/api/fs.html)、[`process`](https://nodejs.org/api/process.html) 和 [`child_process`](https://nodejs.org/api/child_process.html) 模块。
- [Cross-platform Node.js guide](https://github.com/ehmicky/cross-platform-node-guide) - 如何编写跨平台 Node.js 代码。
- [Microsoft Node.js Guidelines](https://github.com/Microsoft/nodejs-guidelines) - 在 Microsoft 平台上使用 Node.js 的提示、技巧和资源。
- [Writing Cross-Platform Node.js](http://shapeshed.com/writing-cross-platform-node/) - 很棒的教程，涵盖了编写跨平台代码时出现的许多常见问题：路径创建、脚本执行、换行符。
- [Cross-platform terminal characters](https://github.com/ehmicky/cross-platform-terminal-characters) - 适用于大多数终端和大多数操作系统的所有字符。

## 应用领域

### 开发环境

- [Node.js](https://nodejs.org/en/download/) - 适用于各种平台的 Node.js 安装程序。
- [nvm-windows](https://github.com/coreybutler/nvm-windows) - 管理 Windows 计算机上 Node.js 的多个安装。
- [nvm](https://github.com/creationix/nvm) / [n](https://github.com/tj/n) - 适用于 macOS/Linux 的节点版本管理器。
- [npm-windows-upgrade](https://github.com/felixrieseberg/npm-windows-upgrade) - 在 Windows 上升级 npm。
- [windows-build-tools](https://github.com/felixrieseberg/windows-build-tools) - 使用 npm 安装适用于 Windows 的 C++ 构建工具。

### 持续集成

- [AppVeyor](http://www.appveyor.com/) - 专注于Windows。免费套餐可用于 OSS 项目。
- [Travis](https://travis-ci.org/) - Windows/macOS/Linux。对于 OSS 项目免费。
- [Azure Pipelines](https://azure.microsoft.com/en-us/services/devops/pipelines/) - Windows/macOS/Linux。对于具有 10 个并行作业的 OSS 项目免费。
- [Github Action](https://github.com/features/actions) - Windows/macOS/Linux。 GitHub Actions 让您可以轻松实现所有软件工作流程的自动化。
- [Gitlab CI](https://docs.gitlab.com/ee/ci/) - Windows/macOS/Linux。 GitLab CI/CD 是 GitLab 内置的软件开发工具。

### 虚拟化

- [ievms](https://github.com/amichaelparker/ievms) - Microsoft 提供的免费虚拟机映像的自动安装程序，用于在多个版本的 IE 上进行测试。这些图像可用于跨平台测试各种技术，但请确保您阅读并理解 Microsoft 的许可。
- [VirtualBox](https://www.virtualbox.org/wiki/Downloads) - 用于运行 x86 虚拟机的通用软件。
- [Docker](https://www.docker.com/) - 用于在通用操作系统上创建、部署和管理虚拟化应用程序容器的软件平台，具有联盟工具的生态系统。

### 兼容性

- [Wine](https://www.winehq.org/) - 在 Linux、Mac、BSD 和 Solaris 上运行 Windows API 调用。
- [Cygwin](https://www.cygwin.com/) - 在 Windows 上运行 POSIX。
- [WSL](https://docs.microsoft.com/en-us/windows/wsl/install-win10) - 在 Windows 上运行 Linux 命令行（ELF 二进制执行、系统调用、文件系统、Bash、核心实用程序、常见应用程序）。
- [MinGW](http://www.mingw.org/) - Windows 上的“gcc”。
- [msys](http://www.mingw.org/wiki/msys) / [Git Bash](https://gitforwindows.org/) - Windows 上的 Bash。

### 数据库

- [Redis](https://github.com/tporadowski/redis) - Windows 版 Redis 的本机端口。

## 图书馆

### 操作系统识别

- [is-windows](https://github.com/jonschlinkert/is-windows) - 检测当前平台是否为Windows。
- [is-wsl](https://github.com/sindresorhus/is-wsl) - 检测当前平台是否为WSL（Windows Subsystem for Linux）。
- [getos](https://github.com/retrohacker/getos) - 检索当前操作系统，包括 Linux 发行版。
- [os-name](https://github.com/sindresorhus/os-name) - 获取当前操作系统的名称。
- [systeminformation](https://github.com/sebhildebrandt/systeminformation) - 硬件/软件系统信息。

### 壳牌

- [execa](https://github.com/sindresorhus/execa) - `child_process.{execFile,exec}` 的跨平台实现。
- [gulp-execa](https://github.com/ehmicky/gulp-execa) - Gulp.js 中的跨平台命令执行。
- [cross-spawn](https://github.com/IndigoUnited/node-cross-spawn) - `child_process.spawn()` 的跨平台实现。
- [shelljs](https://github.com/shelljs/shelljs) - 跨平台 Unix shell 命令。
- [node-windows](https://github.com/coreybutler/node-windows) - Windows 支持 Node.js 脚本（守护进程、事件日志、UAC 等）。
- [log-symbols](https://github.com/sindresorhus/log-symbols) - 带有 Windows 回退功能的各种日志级别的彩色符号。
- [figures](https://github.com/sindresorhus/figures) - 具有 Windows 后备功能的 Unicode 符号。
- [clipboardy](https://github.com/sindresorhus/clipboardy) / [clipboard-cli](https://github.com/sindresorhus/clipboard-cli) - 跨平台复制/粘贴。

### 环境

- [cross-env](https://github.com/kentcdodds/cross-env) - 设置跨平台环境变量。
- [user-home](https://github.com/sindresorhus/user-home) - 获取用户主目录的路径。跨平台。
- [username](https://github.com/sindresorhus/username) - 获取当前用户名。
- [osenv](https://github.com/npm/osenv) - 跨平台环境变量。
- [is-elevated](https://github.com/sindresorhus/is-elevated) - 检查进程是否正在以提升的权限运行。
- [which](https://github.com/npm/node-which) - Unix 的 `which` 的跨平台实现。

### 文件系统

- [rimraf](https://github.com/isaacs/rimraf) / [del](https://github.com/sindresorhus/del) - 删除文件和文件夹。跨平台。
- [make-dir](https://github.com/sindresorhus/make-dir) - 跨平台`mkdir -p`。
- [readdirp](https://github.com/paulmillr/readdirp) - `fs.readdir()` 的递归版本。
- [cpy](https://github.com/sindresorhus/cpy) - 复制文件。跨平台。
- [chokidar](https://github.com/paulmillr/chokidar) - 改进了跨平台文件观看。
- [graceful-fs](https://github.com/isaacs/node-graceful-fs) - 改进了“fs”模块，尤其是在 Windows 上。
- [fs-extra](https://github.com/jprichardson/node-fs-extra) - 将 `graceful-fs` 与更好的 JSON 文件读取和承诺相结合。
- [any-path](https://github.com/bcoe/any-path) - 从对象获取值时，可互换使用 Windows 和 POSIX 路径。
- [dev-null-cli](https://github.com/sindresorhus/dev-null-cli) - 跨平台`/dev/null`。
- [global-cache-dir](https://github.com/ehmicky/global-cache-dir) - 获取全局特定于操作系统的缓存目录。

### 信号

- [fkill](https://github.com/sindresorhus/fkill) - 杀死进程。跨平台。
- [signal-exit](https://github.com/tapjs/signal-exit) - 跨平台“退出”处理程序。
- [human-signals](https://github.com/ehmicky/human-signals) - 人性化的过程信号。

### 流程

- [ps-list](https://github.com/sindresorhus/ps-list) - 获取正在运行的进程。
- [process-exists](https://github.com/sindresorhus/process-exists) - 检查进程是否存在。

### 流

- [noop-stream](https://github.com/sindresorhus/noop-stream) - 跨平台 `fs.createReadStream('/dev/null')`。
- [random-bytes-readable-stream](https://github.com/sindresorhus/random-bytes-readable-stream) - 跨平台 `fs.createReadStream('/dev/urandom')`。

### 桌面用户界面

- [open](https://github.com/sindresorhus/open) - 打开网站、文件、可执行文件等内容。跨平台。
- [node-notifier](https://github.com/mikaelbr/node-notifier) - 跨平台桌面通知。

### Windows注册表

- [node-winreg](https://github.com/fresc81/node-winreg) - 访问 Windows 注册表。
- [rage-edit](https://github.com/MikeKovarik/rage-edit) - 访问/修改 Windows 注册表。
- [windows-registry-node](https://github.com/CatalystCode/windows-registry-node) - 访问/修改 Windows 注册表并设置文件关联。

## 已知问题

- [cmd.exe unicode woes](https://github.com/nodejs/node-v0.x-archive/issues/7940) - 默认情况下，“cmd.exe”在 Windows 上不显示 Unicode 字符。
- [spawn issues](https://github.com/nodejs/node-v0.x-archive/issues/2318) - Windows 和 Linux 之间的“child_process.spawn()”行为不一致。
- [exec() behavior between shells](https://github.com/isaacs/spawn-wrap#contracts-and-caveats) - 根据所使用的 shell，例如 bash 与 dash，“child_process.exec()”具有不一致的退出行为。

## 另请参阅

- [awesome-desktop-js](https://github.com/styfle/awesome-desktop-js) - 在桌面上构建 JavaScript 应用程序的工具列表。

## 支持

如果您发现错误或想添加更多信息，请_不要犹豫_
[在 GitHub 上提交问题](../../issues)。

无论个人背景如何，每个人都受到欢迎。我们强制执行
[行为准则](CODE_OF_CONDUCT.md) 为了促进积极和
包容的环境。

## 贡献

这个项目是用❤️制作的。最简单的回馈方式就是加星标
在线分享。

如果文档不清楚或有拼写错误，请单击页面的“编辑”
按钮（铅笔图标）并提出更正建议。

如果您想帮助我们修复错误或添加更多信息，请检查
我们的[指南](contributing.md)。欢迎拉取请求！

感谢这些优秀的人：

<!-- ALL-CONTRIBUTORS-LIST:START -->
<!-- prettier-ignore -->
<table><tr><td align="center"><a href="https://twitter.com/benjamincoe"><img src="https://avatars3.githubusercontent.com/u/194609?v=4" width="100px;" alt="Benjamin E. Coe"/><br /><sub><b>Benjamin E. Coe</b></sub></a><br /><a href="https://github.com/bcoe/awesome-cross-platform-nodejs/commits?author=bcoe" title="Code">💻</a> <a href="#ideas-bcoe" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/bcoe/awesome-cross-platform-nodejs/commits?author=bcoe" title="Documentation">📖</a></td><td align="center"><a href="https://twitter.com/ehmicky"><img src="https://avatars2.githubusercontent.com/u/8136211?v=4" width="100px;" alt="ehmicky"/><br /><sub><b>ehmicky</b></sub></a><br /><a href="https://github.com/bcoe/awesome-cross-platform-nodejs/commits?author=ehmicky" title="Code">💻</a> <a href="#ideas-ehmicky" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/bcoe/awesome-cross-platform-nodejs/commits?author=ehmicky" title="Documentation">📖</a></td><td align="center"><a href="https://sindresorhus.com"><img src="https://avatars1.githubusercontent.com/u/170270?v=4" width="100px;" alt="Sindre Sorhus"/><br /><sub><b>Sindre Sorhus</b></sub></a><br /><a href="https://github.com/bcoe/awesome-cross-platform-nodejs/commits?author=sindresorhus" title="Code">💻</a> <a href="#ideas-sindresorhus" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/bcoe/awesome-cross-platform-nodejs/commits?author=sindresorhus" title="Documentation">📖</a></td><td align="center"><a href="https://fb.com/RemoveU"><img src="https://avatars1.githubusercontent.com/u/19208123?v=4" width="100px;" alt="Hongarc"/><br /><sub><b>Hongarc</b></sub></a><br /><a href="#design-Hongarc" title="Design">🎨</a> <a href="https://github.com/bcoe/awesome-cross-platform-nodejs/commits?author=Hongarc" title="Documentation">📖</a> <a href="https://github.com/bcoe/awesome-cross-platform-nodejs/commits?author=Hongarc" title="Code">💻</a></td><td align="center"><a href="https://kentcdodds.com"><img src="https://avatars0.githubusercontent.com/u/1500684?v=4" width="100px;" alt="Kent C. Dodds"/><br /><sub><b>Kent C. Dodds</b></sub></a><br /><a href="#ideas-kentcdodds" title="Ideas, Planning, & Feedback">🤔</a></td><td align="center"><a href="https://nz.linkedin.com/in/jsonc11"><img src="https://avatars0.githubusercontent.com/u/5185660?v=4" width="100px;" alt="Jason Cooke"/><br /><sub><b>Jason Cooke</b></sub></a><br /><a href="https://github.com/bcoe/awesome-cross-platform-nodejs/commits?author=Jason-Cooke" title="Documentation">📖</a></td><td align="center"><a href="http://aronhafner.com"><img src="https://avatars0.githubusercontent.com/u/3322693?v=4" width="100px;" alt="Aron Hafner"/><br /><sub><b>Aron Hafner</b></sub></a><br /><a href="https://github.com/bcoe/awesome-cross-platform-nodejs/commits?author=alonalon" title="Documentation">📖</a></td></tr><tr><td align="center"><a href="https://github.com/ShPelles"><img src="https://avatars0.githubusercontent.com/u/43875468?v=4" width="100px;" alt="ShPelles"/><br /><sub><b>ShPelles</b></sub></a><br /><a href="https://github.com/bcoe/awesome-cross-platform-nodejs/commits?author=ShPelles" title="Documentation">📖</a></td><td align="center"><a href="https://github.com/Frederick-S"><img src="https://avatars1.githubusercontent.com/u/1182395?v=4" width="100px;" alt="Xiaodan Mao"/><br /><sub><b>Xiaodan Mao</b></sub></a><br /><a href="https://github.com/bcoe/awesome-cross-platform-nodejs/commits?author=Frederick-S" title="Documentation">📖</a></td><td align="center"><a href="https://github.com/jamestalmage"><img src="https://avatars0.githubusercontent.com/u/4082216?v=4" width="100px;" alt="James Talmage"/><br /><sub><b>James Talmage</b></sub></a><br /><a href="https://github.com/bcoe/awesome-cross-platform-nodejs/commits?author=jamestalmage" title="Documentation">📖</a></td><td align="center"><a href="http://sylvain.pontoreau.com"><img src="https://avatars3.githubusercontent.com/u/3357643?v=4" width="100px;" alt="Sylvain PONTOREAU"/><br /><sub><b>Sylvain PONTOREAU</b></sub></a><br /><a href="https://github.com/bcoe/awesome-cross-platform-nodejs/commits?author=spontoreau" title="Documentation">📖</a></td><td align="center"><a href="https://www.ceriously.com"><img src="https://avatars1.githubusercontent.com/u/229881?v=4" width="100px;" alt="Steven"/><br /><sub><b>Steven</b></sub></a><br /><a href="#ideas-styfle" title="Ideas, Planning, & Feedback">🤔</a></td></tr></table>

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification.

## License

[![License](https://img.shields.io/github/license/bcoe/awesome-cross-platform-nodejs.svg?color=4cc61e&logo=github)](https://creativecommons.org/licenses/by-sa/4.0/)
