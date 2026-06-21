# 很棒的 npm [<img src="https://github.com/npm/logos/blob/7fb0bc425e0dac1bab065217c4ed595594448db4/npm-transparent.png" width="200"align="right" alt="npm">](https://www.npmjs.com) [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> 很棒的 [npm](https://www.npmjs.com) 资源和技巧

[npm](https://en.wikipedia.org/wiki/Npm_(software)) 是 JavaScript 编程语言的包管理器，捆绑在 [Node.js](https://en.wikipedia.org/wiki/Node.js) 运行时中。

*贡献前请阅读[贡献指南](contributing.md)。*

## 内容

- [Articles](#articles)
- [Tools](#tools)
- [Packages](#packages)
- [Clients](#clients)
- [Tips](#tips)
- [FAQ](#faq)
- [Community](#community)
- [Documentation](#documentation)
- [Support](#support)
- [Related](#related)

## 文章

- [小型集中模块](https://github.com/sindresorhus/ama/issues/10#issuecomment-117766328)
- [Unix philosophy and Node.js](http://blog.izs.me/post/48281998870/unix-philosophy-and-nodejs) - 编写只做一件事并把它做好的程序。
- [编写小模块](https://web.archive.org/web/20180302125059/https://substack.net/how_I_write_modules)
- [Semver：入门](https://nodesource.com/blog/semver-a-primer/) *（必读！）*
- [Semver：波形符和插入符](https://nodesource.com/blog/semver-tilde-and-caret/)
- [离线安装npm包](https://addyosmani.com/blog/using-npm-offline/)
- [使用 npm run 实现任务自动化](https://web.archive.org/web/20180302164842/http://substack.net/task_automation_with_npm_run)
- [如何使用 npm 作为构建工具](https://www.keithcirkel.co.uk/how-to-use-npm-as-a-build-tool/)
- [在 macOS 和 Linux 上无需 sudo 全局安装 npm 包](https://github.com/sindresorhus/guides/blob/main/npm-global-without-sudo.md)
- [优化 npm 包的占用空间](https://medium.com/@goldglovecb/npm-needs-a-personal-trainer-537e0f8859c6)
- [The Art of Node](https://github.com/maxogden/art-of-node#modules) - 介绍 Node.js 和使用 npm 进行客户端开发。
- [Why npm scripts?](https://css-tricks.com/why-npm-scripts/) - 介绍带有常见包和脚本的 npm 脚本以及样板项目。

## 工具

### 网络

- [npms](https://npms.io) - 出色的包搜索，使用[无数指标](https://npms.io/about)对包质量进行深入分析。
- [NodeICO](https://nodei.co/) - 包徽章。
- [Libraries.io](https://libraries.io/npm) - 包发现。
- [npm-stat](http://npm-stat.com) - 包的统计图表。
- [npmgraph](http://npm.anvaka.com) - 依赖关系的可视化。
- [npm trends](http://www.npmtrends.com) - 比较一段时间内的包下载计数。
- [npm-top](https://gist.github.com/bcoe/dcc961b869bbf6685002) - npm 用户的下载量。
- [npm semver calculator](http://semver.npmjs.com) - 直观地探索 semver 范围匹配的软件包版本。
- [ghub.io](https://ghub.io) - 重定向到 npm 包的 GitHub 存储库。
- [moiva](https://moiva.io) - 发现并比较软件包。
- [npmx.dev](https://npmx.dev) - npm 注册表的快速而现代的查看器。

### 浏览器扩展

- [Octo-Linker](https://chrome.google.com/webstore/detail/octo-linker/jlmafbaeoofdegohdhinkhilhclaklkp) - Chrome 扩展可轻松浏览 GitHub 上的 npm 包。
- [npm-hub](https://chrome.google.com/webstore/detail/npm-hub/kbbbjimdjbjclaebffknlabpogocablj) - 用于探索 GitHub 存储库上的 npm 依赖关系的 Chrome 扩展。
- [github-npm-stats](https://chrome.google.com/webstore/detail/github-npm-stats/oomfflokggoffaiagenekchfnpighcef) - 在 GitHub 上查看 npm 下载统计信息。
- [npm-search-update](https://chrome.google.com/webstore/detail/npm-search-update/kagpoplamlmaonpddimnnigiojimihnh) - Chrome 扩展可快速搜索依赖项并监控 npm 注册表的更改。

### 命令行界面

- [zsh-better-npm-completion](https://github.com/lukechilds/zsh-better-npm-completion) - npm 更好的 ZSH 补全。
- [npkill](https://github.com/voidcosmos/npkill) - 轻松查找并删除旧的和沉重的 node_modules 文件夹。

## 套餐

### 出版

- [np](https://github.com/sindresorhus/np) - 更好的“npm 发布”。
- [publish-please](https://github.com/inikulin/publish-please) - 安全、优雅地发布包。
- [npm-release](https://github.com/phuu/npm-release) - 让发布到 npm 如此简单，一只小猫可能就能做到™。
- [pkgfiles](https://github.com/timoxley/pkgfiles) - 列出将在包中发布的所有文件。
- [release-it](https://github.com/webpro/release-it) - 自动发布 Git 存储库和/或 npm 包。变更日志生成、GitHub/GitLab 发布等。
- [semantic-release](https://github.com/semantic-release/semantic-release) - 全自动包发布。

### 登记处

- [npm-name](https://github.com/sindresorhus/npm-name-cli) - 检查 npm 上是否有可用的包名称。
- [package-json](https://github.com/sindresorhus/package-json) - 从 npm 注册表获取包的 package.json。
- [latest-version](https://github.com/sindresorhus/latest-version-cli) - 获取 npm 包的最新版本。
- [npm-keyword](https://github.com/sindresorhus/npm-keyword) - 获取带有特定关键字的 npm 包列表。
- [npm-user](https://github.com/sindresorhus/npm-user) - 获取 npm 用户的用户信息。
- [npm-email](https://github.com/sindresorhus/npm-email) - 获取 npm 用户的电子邮件。
- [npm-user-packages](https://github.com/kevva/npm-user-packages-cli) - 由 npm 用户获取包。
- [dpn](https://github.com/gillstrom/dpn) - 获取用户的 npm 包的依赖项。
- [npm-stats](https://github.com/hughsk/npm-stats) - 从 npm 注册表获取数据。
- [npm-cli-login](https://github.com/postmanlabs/npm-cli-login) - 登录 npm。
- [nrm](https://github.com/Pana/nrm) - 注册表管理员。
- [npm-register](https://github.com/dickeyxxx/npm-register) - 易于设置和维护 npm 注册表和代理。
- [verdaccio](https://github.com/verdaccio/verdaccio) - 轻量级私有 npm 代理注册表。
- [cloudsmith](https://cloudsmith.io/l/npm-registry/) - 完全托管的包管理 SaaS，支持公共和私有 npm 注册表（以及许多其他注册表）。
- [RepoFlow](https://www.repoflow.io) - 一个简单易用的包管理平台，可用于云和自托管部署。

### 其他

- [npm-home](https://github.com/sindresorhus/npm-home) - 打开包的 npm 页面。
- [gh-home](https://github.com/sindresorhus/gh-home) - 打开包的 GitHub 页面。
- [david](https://github.com/alanshaw/david) - 检查您的包依赖项是否已过期。
- [npm-check](https://github.com/dylang/npm-check) - 检查过时的、不正确的和未使用的依赖项，以及交互式更新。
- [npm-upgrade](https://github.com/th0r/npm-upgrade) - 以交互方式更新过时的 npm 依赖项。
- [npm-shrinkwrap](https://github.com/uber/npm-shrinkwrap) - 一致的收缩包装工具。
- [npm-windows-upgrade](https://github.com/felixrieseberg/npm-windows-upgrade) - 在 Windows 上升级 npm。
- [generator-nm](https://github.com/sindresorhus/generator-nm) - 搭建一个 npm 包。
- [package-up](https://github.com/sindresorhus/package-up) - 找到最近的 package.json 文件。
- [read-package-up](https://github.com/sindresorhus/read-package-up) - 读取最近的 package.json 文件。
- [normalize-package-data](https://github.com/npm/normalize-package-data) - 标准化包元数据。
- [package-config](https://github.com/sindresorhus/package-config) - 从最近的 package.json 获取命名空间配置。
- [npm-run-path](https://github.com/sindresorhus/npm-run-path) - 与全局二进制文件一样，按名称在终端中运行本地安装的二进制文件。
- [local-npm](https://github.com/nolanlawson/local-npm) - 使用 npm [离线](https://addyosmani.com/blog/using-npm-offline/)。
- [npe](https://github.com/zeke/npe) - 用于检查和编辑 package.json 中的属性的 CLI。
- [engine-deps](https://github.com/samccone/engine-deps) - 轻松管理 Node.js 版本特定的依赖项。
- [enpeem-search](https://github.com/amovah/enpeem-search) - 通过抓取 npm 网络搜索来搜索包。
- [npm-issues](https://github.com/seanzarrin/npm-issues) - 立即搜索所有软件包的已知问题。
- [john](https://github.com/davej/john) - 使 npm3 的平面依赖项更容易查找和排序。
- [ntl](https://github.com/ruyadorno/ntl) - 用于列出和运行 npm 任务的交互式 CLI 菜单。
- [decheck](https://github.com/egoist/decheck) - 在命令行中探索 npm 包的依赖关系。
- [shrinkpack](https://github.com/JamieMason/shrinkpack) - 锁定您的依赖项并离线安装。
- [redrun](https://github.com/coderaiser/redrun) - 从 package.json 扩展脚本以提高执行速度。
- [package-size](https://github.com/egoist/package-size) - 获取 npm 包的包大小。
- [synp](https://github.com/imsnif/synp) - 将yarn.lock 转换为package-lock.json，反之亦然。
- [npm-run-all](https://github.com/mysticatea/npm-run-all) - 用于并行或串行运行多个 npm 脚本的 CLI 工具。
- [onchange](https://github.com/Qard/onchange) - 监视文件和文件夹并在发生更改时运行命令。
- [cli-error-notifier](https://github.com/micromata/cli-error-notifier) - 当 npm 脚本失败时发送本机桌面通知。
- [luna](https://github.com/rvpanoz/luna) - 用于管理 npm 依赖项的应用程序。
- [emma-cli](https://github.com/maticzav/emma-cli) - 交互式 CLI 包搜索实用程序。
- [lockfile-lint](https://github.com/lirantal/lockfile-lint) - Lint 锁定文件可提高安全性和信任策略，以减少恶意包注入和不安全的锁定文件资源。

## 客户

- [yarn](https://github.com/yarnpkg/yarn) - 快速、可靠且安全的依赖关系管理。
- [npm](https://github.com/npm/cli) - 官方客户端。
- [pnpm](https://github.com/pnpm/pnpm) - 快速、节省磁盘空间的包管理器。

## 温馨提示

### 更新到最新的 npm 版本

```
$ npm install --global npm
```

*[Windows 用户，请阅读更多信息。](https://github.com/felixrieseberg/npm-windows-upgrade)*

### 命令别名

- `npm i`→`npm install`
- `npm i -D` → `npm install --save-dev`
- `npm t`→`npm test`
- `npm it` → `npm install && npm test`
- `npm r` → `npm uninstall`
- `npm un` → `npm uninstall`
- `npm up` → `npm update`

### 外壳别名

加快您常见的 npm 任务的速度。

在你的`.zshrc`/`.bashrc`中：

```sh
alias ni='npm install'
alias nid='npm install --save-dev'
alias nig='npm install --global'
alias nt='npm test'
alias nit='npm install && npm test'
alias nk='npm link'
alias nr='npm run'
alias ns='npm start'
alias nf='npm cache clean && rm -rf node_modules && npm install'
alias nlg='npm list --global --depth=0'
```

### 安装时不要添加到package.json

默认情况下，npm 将您安装的包添加到 package.json 中的“依赖关系”字段中（自 v5 起）。您可以通过指定“--no-save”标志来防止这种情况。您可以使用“--save-dev”/“-D”将包添加到“devDependency”：

```
$ npm install --save-dev ava
```

### 运行脚本

您可以使用 npm 轻松地[运行脚本](https://docs.npmjs.com/cli/run-script)，将脚本添加到 package.json 中的“scripts”字段，然后使用 npm run <script-name> 运行它们。运行“npm run”以查看可用的脚本。本地安装包的二进制文件在 [PATH](https://en.wikipedia.org/wiki/PATH_(variable)) 中可用，因此您可以按名称运行它们。

```json
{
	"name": "awesome-package",
	"scripts": {
		"cat": "cat-names"
	},
	"dependencies": {
		"cat-names": "^1.0.0"
	}
}
```

```
$ npm run cat
Max
```

所有 package.json 属性都作为环境变量[公开](https://docs.npmjs.com/misc/scripts#packagejson-vars)：

```json
{
	"name": "awesome-package",
	"scripts": {
		"name": "echo $npm_package_name"
	}
}
```

```
$ npm run name
awesome-package
```

#### 将选项传递给命令

您可以通过添加 `-- --flag` 将选项传递给您在 npm 脚本中使用的命令，如下例所示。 `--` [标记选项解析的结束](https://unix.stackexchange.com/questions/11376/what-does-double-dash-mean-also-known-as-bare-double-dash)，因此 `npm run` 将忽略它并将其传递给命令。

```json
{
	"name": "awesome-package",
	"scripts": {
		"xo": "xo",
		"xo:fix": "npm run xo -- --fix",
	}
}
```

*添加 `-- --fix ` 选项就像执行 `xo --fix`*。

#### 静音选项

`npm run` 有一个 `--silent` 选项，在组合 npm 脚本时特别有用。

假设您有一个用于检查 JavaScript 文件的设置，如下所示：

```json
{
	"name": "awesome-package",
	"scripts": {
		"xo": "xo",
		"xo:fix": "npm run xo --silent -- --fix",
	}
}
```

*使用“--silent”选项会减少终端中的输出。请参阅[此比较](https://twitter.com/mkuehnel/status/957965749473210369)。*

### 生命周期脚本

npm 附带了预定义的生命周期脚本（https://docs.npmjs.com/misc/scripts），如果在 package.json 中定义了它们，则它们会在特定条件下执行。

```json
{
	"name": "awesome-package",
	"scripts": {
		"prepublishOnly": "nsp check"
	},
	"devDependencies": {
		"nsp": "^3.0.0"
	}
}
```

这将在您的 npm 包通过“npmpublish”发布到注册表之前自动执行，以检查依赖项中的已知漏洞。

*注意：**prepublishOnly** 自 npm v4.0.0 起可用。请参阅 [npm 文档](https://docs.npmjs.com/misc/scripts#deprecation-note)。*

#### `npm start` 和 `npm test`

`npm start` 和 `npm test` 也是生命周期脚本，但不会自动执行。

```json
{
	"name": "awesome-package",
	"scripts": {
		"start": "node server.js",
		"test": "ava"
	},
	"devDependencies": {
		"ava": "^1.0.0"
	}
}
```

因此，它们可以简单地执行：

```console
$ npm test
$ npm start
```

#### `pre` 和 `post` 脚本

这些是特殊的生命周期脚本，可用于按顺序自动运行脚本。

```json
{
	"name": "awesome-package",
	"scripts": {
		"pretest": "eslint .",
		"test": "ava"
	},
	"devDependencies": {
		"eslint": "^4.19.0",
		"ava": "^1.0.0"
	}
}
```

```console
$ npm test
```

这将在运行测试之前检查您的文件。如果 linting 失败，测试将不会运行。或者更一般地说：如果按顺序运行的脚本之一以非 0 的退出代码退出，则不会执行以下脚本。

*注意：`pre` 和 `post` 脚本也可用于您的自定义 npm 脚本。因此，如果定义了，`npm run foo` 也将运行 `prefoo` 和 `postfoo`。*

### 使用“npx”运行脚本

`npm` [捆绑](https://medium.com/@maybekatz/introducing-npx-an-npm-package-runner-55f7d4bd282b) 与 `npx` (自 v5.2.0 起) — 一个执行包二进制文件的工具。每个命令都从本地“node_modules/.bin”目录或中央缓存执行，安装“<command>”运行所需的任何包。

```json
{
	"name": "awesome-package",
	"dependencies": {
		"cat-names": "^1.0.0"
	}
}
```

如果二进制文件已经安装，它将从“node_modules/.bin”执行。

```
$ npx cat-names
Max
```

但如果二进制文件丢失，它将首先安装。

```
$ npx dog-names
npx: installed 46 in 3.136s
Bentley
```

### 使用不同的 Node.js 版本运行命令

使用 npx（与 npm v5.2.0 或更高版本捆绑在一起）和 [`node-bin`](https://www.npmjs.com/package/node-bin) 包，您可以轻松地尝试不同 Node.js 版本中的代码，而无需使用 [`nvm`](http://nvm.sh)、[`nave`](https://github.com/isaacs/nave) 等版本管理器，或[`n`](https://github.com/tj/n)。

```
$ npx --package=node-bin@6.11.0 -- node --version
v6.11.0
```

### 链接本地包

有时，将包的本地版本作为依赖项可能会很有用。您可以使用“npm link”将一个本地包链接到另一个本地包。在您要使用的包中运行“npm link”。这将创建一个全局参考。然后进入原始包并运行“npm link <package-name>”以链接到另一个包。

```
$ cd rainbow
$ npm link
$ cd ../unicorn
$ npm link rainbow
```

您现在可以使用“rainbow”作为“unicorn”包中的依赖项。

### 从 GitHub 安装包

npm 支持使用简写直接从 GitHub 存储库安装包：

```
$ npm install sindresorhus/chalk
```

让我们瞄准特定的提交，因为主分支是一个移动目标：

```
$ npm install 'sindresorhus/chalk#51b8f32'
```

指定提交 SHA、分支、标签或不指定任何内容。

您还可以使用 semver 安装 Git 依赖项：*（需要 npm v5 或更高版本）*

```
$ npm install 'sindresorhus/chalk#semver:^2.0.0'
```

### 安装特定版本的软件包

```
$ npm install chalk@1.0.0
```


### 列出顶级已安装的软件包及其版本

```
$ npm ls --depth=0
```

### 命令帮助

获取命令的帮助文档：

```
$ npm help <command>
```

示例：

```
$ npm help install
```

### 包的独立版本

快速获取可浏览并可在浏览器中使用的包的独立版本。

```
https://wzrd.in/standalone/<package-name>[@<version>]
```

示例：

- <https://wzrd.in/standalone/object-assign>
- <https://wzrd.in/standalone/object-assign@4.0.0>

非常适合原型设计，但请下载文件或自行使用 Browserify 进行生产。

## 常见问题解答

- [检查node_modules与shrinkwrap](http://stackoverflow.com/questions/11459733/check-in-node-modules-vs-shrinkwrap)
- [Bower 和 npm 有什么区别？](http://stackoverflow.com/questions/18641899/what-is-the-difference-between-bower-and-npm)
- [package.json 版本控制中的“^”是什么意思？](http://stackoverflow.com/questions/22137778/what-does-mean-in-package-json-versioning)
- [查找已安装的 npm 包的版本](http://stackoverflow.com/questions/10972176/find-the-version-of-an-installed-npm-package)
- [package.json 中的dependency、devDependency 和peerDependency 之间有什么区别？](http://stackoverflow.com/questions/18875674/whats-the-difference-between-dependencies-devdependencies-and-peerdependencies)

## 社区

- [Freenode 上的“#npm”](http://webchat.freenode.net/?channels=npm)
- [堆栈溢出](https://stackoverflow.com/questions/tagged/npm)
- [Reddit](https://www.reddit.com/r/npm)
- [Twitter](https://twitter.com/npmjs)
- [Blog](https://blog.npmjs.org)

## 文档

- [Official](https://docs.npmjs.com)
- [Troubleshooting](https://github.com/npm/npm/wiki/Troubleshooting)
- [语义版本控制](https://docs.npmjs.com/getting-started/semantic-versioning)
- [修复 npm 权限](https://docs.npmjs.com/getting-started/fixing-npm-permissions)
- [package.json](https://docs.npmjs.com/files/package.json)
- [npm 运行脚本](https://docs.npmjs.com/cli/run-script)
- [统计API](https://github.com/npm/download-counts)

## 支持

- [npm.community](https://npm.community/c/support)
- [Twitter](https://twitter.com/npm_support)
- [联系表](https://www.npmjs.com/support)

## 相关

- [awesome-nodejs](https://github.com/sindresorhus/awesome-nodejs)
