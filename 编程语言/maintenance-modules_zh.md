# 维护模块 [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

[![NPM](https://nodei.co/npm/maintenance-modules.png)](https://www.npmjs.com/package/maintenance-modules)

该模块中没有代码，唯一的就是这个 README 文件。

这是可用于维护或开发模块的模块列表（排名不分先后）。

### henrikjoreteg 的修复包

一个适合真正疯狂的人的 package.json 文件清理器。以确定性的方式清理 package.json，以确保高质量、手工制作的 JSON。

```
npm i fixpack --save-dev
```

### 费罗斯标准

JavaScript 标准样式检查器/linter。不允许有选项！使用不可配置的固定设置来最大程度地减少自行车脱落。永远不要再对拉取请求提供样式反馈！

```
npm i standard --save-dev
```

### maxogden 的依赖性检查

检查您在代码中使用了哪些模块，然后确保它们在您的 package.json 中列为依赖项（反之亦然）。

```
npm i dependency-check --save-dev
```

### 由 finnp 创建模块

用于创建模块的常规步骤的帮助工具。创建空的 github 存储库，生成模块样板，运行 npm init，首先提交 + 推送等。

```
npm i create-module --save-dev
```

### travisjs 由 finnp 设计

travis 的命令行模块，特别针对管理节点模块的测试。帮助您快速添加 travis hook + 为您的自述文件生成 travis 徽章。

```
npm i travisjs --save-dev
```

### gh 页面部署，作者：meandave

使用一个命令部署到 gh-pages。允许您将静态构建设置添加到 package.json 中，然后使用此模块自动构建、部署并从 master 推送到 gh-pages。

```
npm i gh-pages-deploy --save-dev
```

### npm-release 由 phuu 发布

用于发布 npm 模块的小工具。碰撞、提交、标记、推送和发布。

```
npm i npm-release --save-dev
```

### npm 检查更新，作者：tjunnone

查找比 package.json 允许的更新版本的依赖项。

```
npm i npm-check-updates --save-dev
```

### NPE 泽克

节点包编辑器：一种 CLI，用于一次性检查和编辑 package.json 文件中的属性。让您无需手动编辑 JSON。

```
npm i npe -g
```

### package-json-to-readme by zeke

从 package.json 内容生成 README.md。使用 npm 模块，可以从 package.json 文件中的属性中收集大量信息：名称、描述、scripts.test、preferGlobal 等。这就是 package-json-to-readme 存在的原因。使用它生成一个不错的样板自述文件，然后从那里迭代。

```
npm i package-json-to-readme -g
```

### npmwd，作者：zeke

在浏览器中打开与 shell 当前工作目录匹配的 npm 包 URL。

```
npm i npmwd -g
```

### 沃尔夫森铸造厂

npm、bower、组件、PyPI、git 标签以及您可以编写的任何插件的发布管理器。一次发布到多个包存储库。

```
npm i foundry --save-dev
```

### boennemann 的语义释放

完全自动化您的包的发布。这不仅会决定要发布哪个版本，还会决定何时发布 - 所有这些都无需您再次关心。该软件包的目标是消除版本号和版本中的人为因素。查看自述文件以获取更多信息！

```
npm i semantic-release --save-dev
```

### Maxogden 的合作者

从 CLI 轻松将新协作者添加到 github 存储库 + npm 包中，然后生成包含新更新的协作者列表的“collaborators.md”文件。使用它可以将新的维护者添加到您的项目中。

```
npm i collaborator -g
```

### 垫片由 mafintosh 设计

Node.js 的预配置管道。 npm 脚本的更强大版本，但框架性不如 gulp 或 grunt。当您可能使用 Makefile 或 bash 脚本但希望管道跨平台时很有用。

```
npm i gasket --save-dev
```

### ngoldman 的模块初始化

命令行工具，可快速创建带有自述文件、许可证、贡献指南和其他好东西的新节点模块。

```
npm i module-init -g
```

### ngoldman 发布的 gh

在 GitHub 上为节点包创建版本。使用 Github Releases API 创建新版本。默认使用 package.json 和 CHANGELOG.md 中的信息。

```
npm i gh-release -g
```

### XO by sindresorhus

JavaScript 幸福风格 linter。强制执行严格的代码风格。没有决策。没有配置。它就是有效的！

```
npm i xo -g
```

### np 作者：sindresorhus

更好的“npm 发布”。在发布之前运行测试、更改版本、推送 git 提交/标签等等。

```
npm i np -g
```

## 维护 bash 脚本

```
alias patch='pre-version && npm version patch && post-version'
alias minor='pre-version && npm version minor && post-version'
alias major='pre-version && npm version major && post-version'
alias pre-version='git diff --exit-code && npm prune && npm install -q && npm test'
alias post-version='npm run --if-present build && git diff --exit-code && git push && git push --tags && npm publish'
```
