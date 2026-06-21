
<br/>
<div align="center">
  <img width="380px" src="https://raw.githubusercontent.com/viatsko/awesome-vscode/master/awesome-vscode-logo.png">
</div>
<br/>
<div align="center">

A curated list of delightful <a href="https://code.visualstudio.com/">Visual Studio Code</a>
packages and resources. For more awesomeness, check
out <a href="https://github.com/sindresorhus/awesome">awesome</a>.
<br/>
<br/>
<img src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg" alt="Awesome"/>
<img src="https://travis-ci.org/viatsko/awesome-vscode.svg" alt="Build Status"/>
</div>
<br/>

# 目录

- [目录](#table-of-contents)
- [Official](#official)
- [Syntax](#syntax)
- [从其他编辑器迁移](#migrating-from-other-editors)
  - [从 Vim 迁移](#migrating-from-vim)
  - [从 Atom 迁移](#migrating-from-atom)
  - [从 Sublime Text 迁移](#migrating-from-sublime-text)
  - [从 Visual Studio 迁移](#migrating-from-visual-studio)
  - [从 Intellij IDEA 迁移](#migrating-from-intellij-idea)
  - [骆驼驼峰](#camel-humps)
- [将 VS Code 与特定技术结合使用](#using-vs-code-with-particular-technologies)
- [Lint 和 IntelliSense](#lint-and-intellisense)
  - [1C](#1c)
  - [AutoHotkey](#autohotkey)
    - [自动热键增强版](#autohotkey-plus)
  - [Bash](#bash)
    - [bash 集成开发环境](#bash-ide)
    - [bash 调试](#bash-debug)
    - [Shellman](#shellman)
  - [C++](#c)
      - [More](#more)
  - [C#、ASP .NET 和 .NET Core](#c-asp-net-and-net-core)
  - [Clojure](#clojure)
    - [Calva](#calva)
  - [CSS](#css)
    - [CSS 预览](#css-peek)
  - [Go](#go)
  - [Groovy](#groovy)
  - [Haskell](#haskell)
  - [HLSL](#hlsl)
  - [Shell](#shell)
  - [Java](#java)
  - [JavaScript](#javascript)
    - [Linters](#linters)
    - [Framework-specific](#framework-specific)
    - [Chrome 调试器](#debugger-for-chrome)
    - [脸书流量](#facebook-flow)
    - [TypeScript](#typescript)
    - [Chrome 调试器](#debugger-for-chrome-1)
  - [MATLAB](#matlab)
  - [Markdown](#markdown)
    - [markdownlint](#markdownlint)
    - [Markdown 多合一](#markdown-all-in-one)
    - [降价表情符号](#markdown-emoji)
  - [PHP](#php)
    - [PHP 工具](#php-tools)
    - [IntelliSense](#intellisense)
    - [Laravel](#laravel)
    - [Twig](#twig)
    - [Smarty](#smarty)
      - [Smarty 模板支持](#smarty-template-support)
    - [其他扩展](#other-extensions)
    - [了解更多](#read-more)
  - [POV-Ray](#pov-ray)
  - [Python](#python)
    - [TensorFlow](#tensorflow)
  - [ReasonML](#reasonml)
  - [Rust](#rust)
  - [Terraform](#terraform)
- [GitHub](#github)
  - [GitHub](#github-1)
  - [GitHub 拉取请求和问题](#github-pull-requests-and-issues)
  - [GistPad](#gistpad)
  - [GitHub 操作](#github-actions)
  - [GitHub 存储库](#github-repositories)
  - [GitHub 拉取请求监视器](#github-pull-request-monitor)
- [Productivity](#productivity)
  - [ARM 模板查看器](#arm-template-viewer)
  - [Azure 宇宙数据库](#azure-cosmos-db)
  - [Azure 物联网工具包](#azure-iot-toolkit)
  - [Bookmarks](#bookmarks)
  - [浏览器预览（已弃用）](#browser-preview)
  - [颜色标签](#color-tabs)
  - [创建测试](#create-tests)
  - [Dendron](#dendron)
  - [Deploy](#deploy)
  - [重复动作](#duplicate-action)
  - [误差镜头](#error-lens)
  - [Toggle](#toggle)
  - [ES7 React/Redux/GraphQL/React-Native 片段](#es7-reactreduxgraphqlreact-native-snippets)
    - [Gi](#gi)
  - [Git 历史](#git-history)
  - [Git 项目经理](#git-project-manager)
  - [GitLink](#gitlink)
  - [GitLens](#gitlens)
  - [Git 指标](#git-indicators)
  - [亚搏体育appGitLab工作流程](#gitlab-workflow)
      - [摇篮任务](#gradle-tasks)
  - [图标字体](#icon-fonts)
  - [进口成本](#import-cost)
  - [Jira 和 Bitbucket](#jira-and-bitbucket)
  - [JS 参数注解](#js-parameter-annotations)
  - [Jumpy](#jumpy)
  - [Kanban](#kanban)
  - [实时服务器](#live-server)
  - [多个剪贴板](#multiple-clipboards)
  - [用于 VSCode 的 ngrok](#ngrok-for-vscode)
  - [Dotnet 核心测试资源管理器](#dotnet-core-test-explorer)
  - [国际化盟友](#i18n-ally)
  - [即时降价](#instant-markdown)
  - [npm 智能感知](#npm-intellisense)
  - [参数提示](#parameter-hints)
  - [部分差异](#partial-diff)
    - [将 JSON 粘贴为代码](#paste-json-as-code)
  - [路径自动完成](#path-autocomplete)
  - [路径智能感知](#path-intellisense)
  - [电动工具](#power-tools)
  - [PrintCode](#printcode)
  - [项目经理](#project-manager)
  - [项目仪表板](#project-dashboard)
  - [彩虹 CSV](#rainbow-csv)
  - [远程开发](#remote-development)
  - [远程 VSCode](#remote-vscode)
  - [休息客户端](#rest-client)
  - [文本电动工具](#text-power-tools)
  - [都都树](#todo-tree)
  - [切换引号](#toggle-quotes)
  - [打字稿解构](#typescript-destructure)
  - [WakaTime](#wakatime)
  - [Yo](#yo)
  - [Timing](#timing)
- [格式与美化](#formatting--beautification)
  - [更好地对齐](#better-align)
  - [自动重命名标签](#auto-rename-tag)
  - [beautify](#beautify)
    - [html2pug](#html2pug)
  - [ECMAScript 引用转换器](#ecmascript-quotes-transformer)
  - [粘贴和缩进](#paste-and-indent)
  - [排序线](#sort-lines)
  - [Surround](#surround)
  - [包裹选择](#wrap-selection)
  - [格式切换](#formatting-toggle)
  - [自动导入](#auto-import)
  - [shell-format](#shell-format)
  - [vscode 谷歌翻译](#vscode-google-translate)
  - [资源管理器图标](#explorer-icons)
    - [城市之光图标](#city-lights-icons)
    - [VSCode 图标](#vscode-icons)
    - [塞蒂图标](#seti-icons)
    - [材质图标主题](#material-icon-theme)
- [Uncategorized](#uncategorized)
  - [CodeRoad](#coderoad)
  - [代码运行者](#code-runner)
  - [编码时间](#code-time)
  - [颜色高光](#color-highlight)
  - [输出着色器](#output-colorizer)
  - [Dash](#dash)
  - [使用 Shell 命令进行编辑](#edit-with-shell-command)
  - [VS Code 的编辑器配置](#editor-config-for-vs-code)
  - [ftp-sync](#ftp-sync)
  - [突出显示 JSX/HTML 标签](#highlight-jsxhtml-tags)
  - [缩进彩虹](#indent-rainbow)
  - [iTerm2 主题同步](#iterm2-theme-sync)
  - [密码生成器](#password-generator)
  - [PlatformIO](#platformio)
  - [Polacode](#polacode)
  - [carbon-now-sh](#carbon-now-sh)
  - [Quokka](#quokka)
  - [Runner](#runner)
  - [Slack](#slack)
  - [Spotify](#spotify)
  - [SVG](#svg)
  - [SVG 查看器](#svg-viewer)
  - [文本标记（荧光笔）](#text-marker-highlighter)
  - [ESDOC MDN](#esdoc-mdn)
  - [接口生成器](#interface-generator)
  - [JFrog](#jfrog)
- [Themes](#themes)
  - [UI](#ui)
  - [Syntax](#syntax-1)
    - [2077 主题 by Endormi](#2077-theme-by-endormi)
    - [达斯汀·桑德斯的《旧希望》主题](#an-old-hope-theme-by-dustin-sanders)
    - [有明暗疣](#ariake-dark-by-wart)
    - [Mahmoud Ali 的 Atom One Dark 主题](#atom-one-dark-theme-by-mahmoud-ali)
    - [Emroussel雾化](#atomize-by-emroussel)
    - [香鱼 by Teabyii](#ayu-by-teabyii)
    - [亚历山大·埃克特 (Alexander Eckert) 的 Borealis 主题](#borealis-theme-by-alexander-eckert)
    - [甜心船长 by ultradracula](#captain-sweetheart-by-ultradracula)
    - [Yummygum 的城市之光](#city-lights-by-yummygum)
    - [Cobalt2 主题 官方作者：Wes Bos](#cobalt2-theme-official-by-wes-bos)
    - [Dracula 官方 Dracula 主题](#dracula-official-by-dracula-theme)
    - [博格丹·拉扎尔的边缘](#edge-by-bogdan-lazar)
    - [伊娃主题由fisheva设计](#eva-theme-by-fisheva)
    - [仙女牙线，作者：nopjmp 和 sailorhg](#fairy-floss-by-nopjmp-and-sailorhg)
    - [Thomas Pink 的 GitHub 主题](#github-theme-by-thomas-pink)
    - [Dimitar Nonov 的 Jellybeans 主题](#jellybeans-theme-by-dimitar-nonov)
    - [由 Whizkydee 设计的 Material Palenight 主题](#material-palenight-theme-by-whizkydee)
    - [Mattia Astorino 的材质主题](#material-theme-by-mattia-astorino)
    - [由 u29dc 制作的 Mno](#mno-by-u29dc)
    - [Monokai Oblique，作者：pushqrdx](#monokai-oblique-by-pushqrdx)
    - [Monokai Pro by monokai（商业）](#monokai-pro-by-monokai-commercial)
    - [莎拉·德拉斯纳的《夜猫子》](#night-owl-by-sarah-drasner)
    - [威尔斯通的塑料](#plastic-by-will-stone)
    - [Nord 由 arcticicestudio 设计](#nord-by-arcticicestudio)
    - [戴尔·里斯 (Dayle Rees) 的《Rainglow》](#rainglow-by-dayle-rees)
    - [Michael Kühnel 的轻松主题](#relaxed-theme-by-michael-kühnel)
    - [艾哈迈德·阿瓦伊斯的《紫色阴影》](#shades-of-purple-by-ahmad-awais)
    - [史莱姆主题由 smlombardi 设计](#slime-theme-by-smlombardi)
    - [Niketa 主题由 Dejan Toteff 设计](#niketa-theme-by-dejan-toteff)
- [值得关注的人](#people-to-follow)
- [扩展开发人员的资源](#resources-for-extension-developers)
  - [Documentation](#documentation)
  - [Libraries](#libraries)
  - [Tools](#tools)
- [在线课程](#online-courses)
  - [Visual Studio Code 高级用户课程（商业）](#visual-studio-code-power-user-course-commercial)
- [Contribute](#contribute)
- [License](#license)

# 官方

- [官方网站](https://code.visualstudio.com/)
- GitHub 上的[源代码](https://github.com/microsoft/vscode)
- [发布（稳定通道）](https://code.visualstudio.com/download)
- [发布（内部人士频道）](https://code.visualstudio.com/insiders)
- [每月迭代计划](https://github.com/Microsoft/vscode/issues?utf8=%E2%9C%93&q=label%3Aiteration-plan+)

# 语法

语言包通过语法突出显示和/或特定语言或文件格式的片段扩展了编辑器。

- [Arduino](https://marketplace.visualstudio.com/items?itemName=vsciot-vscode.vscode-arduino)
- [Befunge](https://marketplace.visualstudio.com/items?itemName=kagof.befunge)
- [Blink](https://marketplace.visualstudio.com/items?itemName=melmass.blink)
- [Bolt](https://marketplace.visualstudio.com/items?itemName=smkamranqadri.vscode-bolt-language)
- [Bond](https://marketplace.visualstudio.com/items?itemName=yiwwan.vscode-bond)
- [CMake](https://marketplace.visualstudio.com/items?itemName=twxs.cmake)
- [Dart](https://marketplace.visualstudio.com/items?itemName=Dart-Code.dart-code)
- [Dockerfile](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker)
- [EJS](https://marketplace.visualstudio.com/items?itemName=QassimFarid.ejs-language-support)
- [Elixir](https://marketplace.visualstudio.com/items?itemName=mjmcloug.vscode-elixir)
- [Elm](https://marketplace.visualstudio.com/items?itemName=sbrink.elm)
- [Erlang](https://marketplace.visualstudio.com/items?itemName=pgourlain.erlang)
- [F#](https://marketplace.visualstudio.com/items?itemName=Ionide.Ionide-fsharp)
- [Flatbuffers](https://marketplace.visualstudio.com/items?itemName=gaborv.flatbuffers)
- [Fortran](https://marketplace.visualstudio.com/items?itemName=Gimly81.fortran)
- [Hack(HHVM)](https://marketplace.visualstudio.com/items?itemName=pranayagarwal.vscode-hack)
- [Handlebars](https://marketplace.visualstudio.com/items?itemName=andrejunges.Handlebars)
- [Hive SQL](https://marketplace.visualstudio.com/items?itemName=josephtbradley.hive-sql)
- [Julia](https://marketplace.visualstudio.com/items?itemName=julialang.language-julia)
- [KL](https://marketplace.visualstudio.com/items?itemName=melmass.kl)
- [Kotlin](https://marketplace.visualstudio.com/items?itemName=mathiasfrohlich.Kotlin)
- [LaTeX](https://marketplace.visualstudio.com/items?itemName=torn4dom4n.latex-support)
- [MATLAB](https://marketplace.visualstudio.com/items?itemName=MathWorks.language-matlab)
- [Mason](https://marketplace.visualstudio.com/items?itemName=viatsko.html-mason)
- [openHAB](https://marketplace.visualstudio.com/items?itemName=openhab.openhab)
- [解析器3](https://marketplace.visualstudio.com/items?itemName=viatsko.parser3)
- [Pascal](https://marketplace.visualstudio.com/items?itemName=alefragnani.pascal) 或 [OmniPascal](https://marketplace.visualstudio.com/items?itemName=Wosi.omnipascal)（仅适用于 Windows）
- [Perl HTML 模板](https://marketplace.visualstudio.com/items?itemName=viatsko.perl-html-template)
- [POV-Ray](https://marketplace.visualstudio.com/items?itemName=jmaxwilson.vscode-povray)
- [Protobuf](https://marketplace.visualstudio.com/items?itemName=peterj.proto)
- [Ruby](https://marketplace.visualstudio.com/items?itemName=groksrc.ruby)
- [Scala](https://marketplace.visualstudio.com/items?itemName=scala-lang.scala)
- [着色器（*HLSL*、*GLSL*、*Cg*） ](https://marketplace.visualstudio.com/items?itemName=slevesque.shader)
- [Stylus](https://marketplace.visualstudio.com/items?itemName=sysoev.language-stylus)
- [Swift](https://marketplace.visualstudio.com/items?itemName=Kasik96.swift)
- [VEX](https://marketplace.visualstudio.com/items?itemName=melmass.vex)
- [Wenyan](https://github.com/antfu/wenyan-lang-vscode)
- [Zephir](https://marketplace.visualstudio.com/items?itemName=zephir-lang.zephir)

# 从其他编辑器迁移

VSCode 团队提供来自流行编辑器的键盘映射，使到 VSCode 的过渡几乎无缝且轻松。

## 从 Vim 迁移

> **Vim 模式** - 相对较新，但有前途的扩展，在 VSCode 中实现 Vim 功能

## 从 Atom 迁移

> Visual Studio Code 的流行 Atom 按键绑定

## 从 Sublime Text 迁移

> 适用于 VS Code 的流行 Sublime Text 按键绑定。

## 从 Visual Studio 迁移

> 适用于 VS Code 的流行 Visual Studio 按键绑定。

## 从 Intellij IDEA 迁移

> 适用于 VS Code 的流行 Intellij IDEA 按键绑定。

## 骆驼驼峰

> 就像 Visual Studio 和 Resharper 或 Intellij IDEA 一样

# 将 VS Code 与特定技术结合使用

Microsoft 创建了一系列使用 VS Code 和特定技术（主要是 Web）的方法。

请务必访问 [Microsoft/vscode-recipes](https://github.com/Microsoft/vscode-recipes)

# Lint 和 IntelliSense

如果你还没有释放出令人敬畏的必杀技：
> lint 最初是一个特定程序的名称，该程序在 C 语言源代码中标记了一些可疑且不可移植的结构（可能是错误）。该术语现在一般适用于标记以任何计算机语言编写的软件中的可疑使用情况的工具。

与其他一些编辑器不同，VS Code 支持 IntelliSense、linting、开箱即用的大纲，并且不需要任何单独的扩展来运行 linter 包。一些 linter 已经集成在 VS Code 中，您可以在官方文档的 [语言](https://code.visualstudio.com/Docs/languages/overview) 部分找到完整列表。

## 1C

- [1C/OScript](https://marketplace.visualstudio.com/items?itemName=1c-syntax.language-1c-bsl) - VSC 中丰富的 1С:Enterprise 8 (BSL) 语言支持 - 在 VSC 中向 *.bsl и *.os 文件添加语法突出显示，为 1С lang 添加 IntelliSense 和语法帮助程序

## 自动热键

### 自动热键增强版
> 语法突出显示、代码片段、转到定义、签名助手和代码格式化程序

## 重击

### bash 集成开发环境
> Bash 语言服务器

### bash 调试
> 基于 `bashdb` 的 Bash 脚本调试器扩展

![Bash Debug](https://user-images.githubusercontent.com/10897048/47375120-1a9a9b80-d722-11e8-819d-a0090540b2ba.gif)

### 谢尔曼
> Bash 脚本片段扩展

![Shellman](https://raw.githubusercontent.com/yousefvand/shellman/master/images/demo.gif)

## C++

- [C/C++](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools) - 预览 [Microsoft](https://www.microsoft.com) 的 C/C++ 扩展，详细信息请阅读 [官方博文](https://blogs.msdn.microsoft.com/vcblog/2016/03/31/cc-extension-for-visual-studio-code/)
- [Clangd](https://marketplace.visualstudio.com/items?itemName=llvm-vs-code-extensions.vscode-clangd) - 使用 clangd 为 VS Code 提供 C/C++ 语言 IDE 功能：代码完成、编译错误和警告、转到定义和交叉引用，包括管理、代码格式化、简单重构。
- [gnu-global-tags](https://marketplace.visualstudio.com/items?itemName=austin.code-gnu-global) - 借助 GNU Global 工具，为 C/C++ 提供 Intellisense。
- [YouCompleteMe](https://marketplace.visualstudio.com/items?itemName=RichardHe.you-complete-me) - 使用 [YouCompleteMe](http://ycm-core.github.io/YouCompleteMe/) 为 C/C++（以及 TypeScript、JavaScript、Objective-C、Golang、Rust）提供语义补全。
- [C/C++ Clang Command Adapter](https://github.com/mitaki28/vscode-clang) - 使用 Clang 命令完成和诊断 C/C++/Objective-C。
- [CQuery](https://github.com/cquery-project/vscode-cquery) - [C/C++ 语言服务器](https://github.com/jacobdufault/cquery) 支持数百万行代码库，由 libclang 提供支持。交叉引用、完成、诊断、语义突出显示等等。

#### 更多

- [微软关于使用VSCode进行远程C/C++开发的教程](https://devblogs.microsoft.com/cppblog/vscode-cpp-may-2019-update/)

## C#、ASP .NET 和 .NET Core

- [C#](https://marketplace.visualstudio.com/items?itemName=ms-dotnettools.csharp) - [Microsoft](https://www.microsoft.com) 的 C# 扩展，详细信息请阅读 [官方文档](https://code.visualstudio.com/docs/languages/csharp)
- [C# FixFormat](https://marketplace.visualstudio.com/items?itemName=Leopotam.csharpfixformat) - 修复使用/缩进/大括号/空行的格式
- [C# Extensions](https://marketplace.visualstudio.com/items?itemName=jchannon.csharpextensions) - 提供 IDE 扩展，加快您的开发工作流程。
- [MSBuild 项目工具](https://marketplace.visualstudio.com/items?itemName=tintoy.msbuild-project-tools)
- [VSCode 解决方案资源管理器](https://marketplace.visualstudio.com/items?itemName=fernandoescolar.vscode-solution-explorer)
- [.NET Core 测试资源管理器](https://marketplace.visualstudio.com/items?itemName=formulahendry.dotnet-test-explorer)

![.NET Core Test Explorer](https://raw.githubusercontent.com/formulahendry/vscode-dotnet-test-explorer/master/images/test-explorer-065.gif)

## 克洛尤尔

### 卡尔瓦
> 集成 REPL、linting、内联评估、测试运行器等。由 Cider 和 nRepl 提供支持。

![Calva](https://raw.githubusercontent.com/BetterThanTomorrow/calva/master/assets/howto/top-level-comment-eval.gif)

## CSS

### CSS 预览
> 直接从 HTML 中查看或跳转到 CSS 定义，就像在括号中一样！

![CSS Peek](https://raw.githubusercontent.com/pranaygp/vscode-css-peek/master/readme/symbolProvider.gif)

- [stylelint](https://marketplace.visualstudio.com/items?itemName=stylelint.vscode-stylelint) - Lint CSS/SCSS。
- [Autoprefixer](https://marketplace.visualstudio.com/items?itemName=mrmlnc.vscode-autoprefixer)
解析 CSS、SCSS、LESS 并自动添加供应商前缀。
  ![Autoprefixer](https://cloud.githubusercontent.com/assets/7034281/16823311/da82a3c6-496b-11e6-8d95-0bebbf0b9607.gif)

- [Intellisense for CSS class names](https://marketplace.visualstudio.com/items?itemName=Zignd.html-css-class-completion) - 根据工作区中的 CSS 文件为 HTML 类属性提供 CSS 类名称补全。还支持 React 的 className 属性。

  ![Intellisense CSS class names](https://i.imgur.com/5crMfTj.gif)

## 去

- [Go](https://marketplace.visualstudio.com/items?itemName=golang.Go) - 对Go语言的丰富语言支持。

## 格罗维

- [VsCode Groovy Lint](https://marketplace.visualstudio.com/items?itemName=NicolasVuillamy.vscode-groovy-lint) - Groovy lint、格式、美化和自动修复

![VsCode Groovy Lint](https://raw.githubusercontent.com/nvuillam/vscode-groovy-lint/master/images/vscode-anim.gif)

## 哈斯克尔

- [haskell-linter](https://marketplace.visualstudio.com/items?itemName=hoovercj.haskell-linter)
- [Haskell IDE engine](https://marketplace.visualstudio.com/items?itemName=alanz.vscode-hie-server) - 为堆栈和 Cabal 项目提供[语言服务器](https://github.com/haskell/haskell-ide-engine)。

## HLSL

- [HLSL Tools](https://marketplace.visualstudio.com/items?itemName=TimGJones.hlsltools) - 为在 VS Code 中编辑 HLSL 文件提供丰富的语言支持
  ![Example of statement completion using HLSL Tools for VS Code](https://github.com/tgjones/HlslTools/raw/master/src/ShaderTools.VSCode/art/statement-completion.gif)

## 壳牌

- [autocomplate-shell](https://marketplace.visualstudio.com/items?itemName=truman.autocomplate-shell)

## 爪哇

- [Red Hat 对 Java(TM) 的语言支持](https://marketplace.visualstudio.com/items?itemName=redhat.java)
- [Java 调试器](https://marketplace.visualstudio.com/items?itemName=vscjava.vscode-java-debug)
- [Java 的 Maven](https://marketplace.visualstudio.com/items?itemName=vscjava.vscode-maven)

- [Lombok](https://marketplace.visualstudio.com/items?itemName=GabrielBB.vscode-lombok)

## JavaScript

- [TS/JS 后缀补全](https://marketplace.visualstudio.com/items?itemName=ipatalas.vscode-postfix-ts)

![TS/JS postfix completion demo](https://github.com/ipatalas/vscode-postfix-ts/raw/master/images/demo-multiline.gif)

- [巴贝尔 JavaScript](https://marketplace.visualstudio.com/items?itemName=mgmcdermott.vscode-language-babel)
- [Visual Studio IntelliCode](https://marketplace.visualstudio.com/items?itemName=VisualStudioExptTeam.vscodeintellicode) - 此扩展提供人工智能辅助开发功能，包括自动完成和基于理解代码上下文的其他见解。
![Visual Studio IntelliCode](https://docs.microsoft.com/en-us/visualstudio/intellicode/media/python-intellicode.gif)

查看这两者之间的区别[此处](https://github.com/michaelgmcd/vscode-language-babel/issues/1)

### 短绒棉

- [tslint (deprecated)](https://marketplace.visualstudio.com/items?itemName=ms-vscode.vscode-typescript-tslint-plugin) - 用于 Visual Studio Code 的 TSLint（使用 `"tslint.jsEnable": true`）。
- [eslint](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint) - [eslint](https://eslint.org/) 的 Linter。
- [XO](https://marketplace.visualstudio.com/items?itemName=samverschueren.linter-xo) - [XO](https://github.com/xojs/xo) 的 Linter。
- [AVA](https://marketplace.visualstudio.com/items?itemName=samverschueren.ava) - [AVA](https://github.com/avajs/ava) 的片段。
- [Prettier](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode) - [Prettier](https://github.com/prettier/prettier-vscode) 的 Linter、格式化程序和漂亮打印机。
- [Code Spell Checker](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker) - Visual Studio Code 的拼写检查器（英文）。还通过外部扩展支持其他语言。

- [Schema.org Snippets](https://marketplace.visualstudio.com/items?itemName=austinleegordon.vscode-schema-dot-org) - [Schema.org](https://schema.org/) 的片段。

### 特定于框架的

- [Vetur](https://marketplace.visualstudio.com/items?itemName=octref.vetur) - Vue.js 工具包
![Vetur](截图/Vetur.png)

### Chrome 调试器

> VS Code 扩展，用于在 Chrome 浏览器或支持 Chrome 调试协议的其他目标中调试 JavaScript 代码。

### 脸书流量

- [Flow Language Support](https://marketplace.visualstudio.com/items?itemName=flowtype.flow-for-vscode) - 提供您期望的所有功能 - linting、智能感知、类型工具提示和点击定义
- [vscode-flow-ide](https://marketplace.visualstudio.com/items?itemName=gcazaciuc.vscode-flow-ide) - Visual Studio Code 的替代 Flowtype 扩展

### 打字稿

- [tslint (deprecated)](https://marketplace.visualstudio.com/items?itemName=ms-vscode.vscode-typescript-tslint-plugin) - 用于 Visual Studio 代码的 TSLint。

### Chrome 调试器

> VS Code 扩展，用于在 Chrome 浏览器或支持 Chrome 调试协议的其他目标中调试 JavaScript 代码。

## MATLAB
> 此扩展支持在 Visual Studio® Code 中编辑 MATLAB® 代码，并包括语法突出显示、代码分析、导航支持等功能。

未安装 MATLAB：
- 语法高亮
- 代码片段
- 评论
- 代码折叠

![Without MATLAB Installed](https://github.com/mathworks/MATLAB-extension-for-vscode/raw/HEAD/public/BasicFeatures.gif)

安装 MATLAB 后：
- 自动代码完成
- 源代码格式化（文档格式化）
- 代码导航
- 代码分析，例如持续代码检查和自动修复

![MATLAB Installed](https://github.com/mathworks/MATLAB-extension-for-vscode/raw/HEAD/public/AdvancedFeatures.gif)

## 降价

### 降价林特

> [markdownlint](https://github.com/DavidAnson/markdownlint) 的 Linter。

### Markdown 多合一

> 多合一 Markdown 插件（键盘快捷键、目录、自动预览、列表编辑等）

![Markdown All in One](https://user-images.githubusercontent.com/10897048/47027336-d8a9ac80-d199-11e8-9836-b8dbc4a97d1a.gif)

### 降价表情符号
> 为 VS Code 的内置 Markdown 预览添加表情符号语法支持

![Markdown Emoji](https://raw.githubusercontent.com/mjbvz/vscode-markdown-emoji/master/docs/example.png)

## PHP

### PHP 工具

> 对 PHP 语言的丰富语言支持：linting、调试、智能感知、自动完成、代码格式化、重构、单元测试、分析等。

![PHP Tools Intellisense demo screenshot](https://raw.githubusercontent.com/DEVSENSE/phptools-docs/master/docs/vscode/imgs/completion-tooltip.gif)

### 智能感知

这些扩展提供了略有不同的功能集。虽然第一个提供了更好的自动完成支持，但第二个似乎总体上具有更多功能。

- [PHP 英特尔芬斯](https://marketplace.visualstudio.com/items?itemName=bmewburn.vscode-intelephense-client)
- [PHP 智能感知](https://marketplace.visualstudio.com/items?itemName=felixfbecker.php-intellisense)

### 拉维尔

- [Laravel 5 Snippets](https://marketplace.visualstudio.com/items?itemName=onecentlin.laravel5-snippets) - Visual Studio Code 的 Laravel 5 代码片段
- [Laravel Blade Snippets](https://marketplace.visualstudio.com/items?itemName=onecentlin.laravel-blade) - Laravel Blade 片段和语法高亮支持

![Laravel blade snippets and syntax highlight support animation](https://raw.githubusercontent.com/onecentlin/laravel-blade-snippets-vscode/master/images/screenshot.gif)

- [Laravel Model Snippets](https://marketplace.visualstudio.com/items?itemName=ahinkle.laravel-model-snippets) - 使用 Laravel 模型片段快速启动并运行模型。

![Laravel Model Snippets animation](https://raw.githubusercontent.com/ahinkle/vscode-laravel-model-snippets/master/images/example.gif)

- [Laravel Artisan](https://marketplace.visualstudio.com/items?itemName=ryannaddy.laravel-artisan) - Visual Studio Code 中的 Laravel Artisan 命令

![Laravel Artisan commands within Visual Studio Code animation](https://raw.githubusercontent.com/TheColorRed/vscode-laravel-artisan/master/images/screens/make-controller.gif)

- [DotENV](https://marketplace.visualstudio.com/items?itemName=mikestead.dotenv) - 支持 dotenv 文件语法

![Support for dotenv file syntax screenshot](https://raw.githubusercontent.com/mikestead/vscode-dotenv/master/images/screenshot.png)

### 树枝

- [树枝语言2](https://marketplace.visualstudio.com/items?itemName=mblode.twig-language-2)

要在 .twig 文件中启用 Emmet 支持，您需要在设置中进行以下设置：

```json
{
  "emmet.includeLanguages": {
    "twig": "html"
  }
}
```

### 聪明人

#### Smarty 模板支持
> Smarty 模板支持格式化、折叠、片段、语法突出显示等。

![Smarty Template Support](https://raw.githubusercontent.com/aswinkumar863/smarty-vscode-support/master/images/preview.gif)

### 其他扩展

- [Format HTML in PHP](https://marketplace.visualstudio.com/items?itemName=rifi2k.format-html-in-php) - PHP 文件中 HTML 的格式。在保存操作之前运行，因此您仍然可以拥有 PHP 格式化程序。

![Format HTML in PHP](https://raw.githubusercontent.com/RiFi2k/format-html-in-php/master/format-html-in-php.gif)

- [Composer](https://marketplace.visualstudio.com/items?itemName=ikappas.composer)
- [PHP Debug](https://marketplace.visualstudio.com/items?itemName=felixfbecker.php-debug) - Visual Studio Code 的 XDebug 扩展
- [PHP 文档拦截器](https://marketplace.visualstudio.com/items?itemName=neilbrayfield.php-docblocker)
- [php cs fixer](https://marketplace.visualstudio.com/items?itemName=junstyle.php-cs-fixer) - 适用于 VS Code 的 PHP CS Fixer 扩展、php 格式化程序、php 代码美化工具
- [phpcs](https://marketplace.visualstudio.com/items?itemName=ikappas.phpcs) - 用于 Visual Studio Code 的 PHP CodeSniffer
- [phpfmt](https://marketplace.visualstudio.com/items?itemName=kokororin.vscode-phpfmt) - 用于 Visual Studio 代码的 phpfmt

### 了解更多

- [为 Drupal 配置 Visual Studio Code](https://www.drupal.org/docs/develop/development-tools/configuring-visual-studio-code)

## POV射线

- [POV-Ray](https://marketplace.visualstudio.com/items?itemName=jmaxwilson.vscode-povray) - 视觉光线追踪器 (POV-Ray) 扩展的持久性，包括常见 POV-Ray 场景元素的语法突出显示和片段，从 Visual Studio Code 中渲染当前场景

![Animated GIF of POV-Ray in Visual Studio Code](https://raw.githubusercontent.com/jmaxwilson/vscode-povray/master/images/vscode-povray-demo.gif)

## 蟒蛇

- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) - Linting、调试（多线程、Web 应用程序）、Intellisense、自动完成、代码格式化、代码片段、单元测试等。

### TensorFlow

- [TensorFlow Snippets](https://marketplace.visualstudio.com/items?itemName=vahidk.tensorflow-snippets) - 此扩展包含一组有用的代码片段，用于在 Visual Studio Code 中开发 TensorFlow 模型。

![TensorFlow Snippets GIF](https://raw.githubusercontent.com/vahidk/tensorflow-snippets/master/images/framework.gif)

## ReasonML

- [ReasonML](https://marketplace.visualstudio.com/items?itemName=jaredly.reason-vscode) - 智能感知、代码格式化、重构、代码镜头等等

## 铁锈

- [rust-analyzer](https://marketplace.visualstudio.com/items?itemName=rust-lang.rust-analyzer) - Linting、自动完成、代码格式化、片段等等

## 地形

- [Terraform](https://marketplace.visualstudio.com/items?itemName=hashicorp.terraform) - Hashicorp Terraform 的语法突出显示、linting、格式化和验证

# GitHub

## GitHub

> 提供 GitHub 工作流程支持。例如，浏览项目、问题、文件（当前行）、创建和管理拉取请求。计划支持其他提供商（例如 gitlab 或 bitbucket）。

## GitHub 拉取请求和问题

> 审查和管理 GitHub 拉取请求和问题

## 要点手册

> 允许您完全在编辑器中管理 GitHub Gists。您可以打开、创建、删除、分叉、加星标和克隆要点，然后无缝地开始编辑文件，就像它们是本地文件一样。它就像您自己的开发人员库，用于构建和引用代码片段、常用的配置/脚本、与编程相关的注释/文档以及交互式示例。

![GistPad gist management](https://user-images.githubusercontent.com/116461/69910156-96274b80-13fe-11ea-9be4-d801f4e9c377.gif)

## GitHub 操作

> 显示 GitHub Actions 工作流程和运行

## GitHub 存储库

> 远程浏览和编辑任何 GitHub 存储库

## GitHub 拉取请求监视器

> 此扩展使用 GitHub api 来监视拉取请求的状态，并让您知道何时需要合并或是否有人请求更改。

![GitHub Pull Request Monitor](https://raw.githubusercontent.com/erichbehrens/pull-request-monitor/master/images/statusBarItems.png)

# 生产力

## ARM 模板查看器

> 显示 Azure 资源管理器 (ARM) 模板的图形预览。该视图将显示带有官方 Azure 图标的所有资源以及资源之间的链接。

![Displays a graphical preview of Azure Resource Manager (ARM) templates](https://raw.githubusercontent.com/benc-uk/armview-vscode/master/assets/readme/screen1.png)

## Azure 宇宙数据库

> 在 VS Code 编辑器中浏览数据库

![Browse your database inside the vs code editor animation](https://media.giphy.com/media/fnK9fzP80e7YfO7JAq/giphy.gif)

## Azure 物联网工具包

> Azure IoT 开发所需的一切：与 Azure IoT 中心交互、管理连接到 Azure IoT 中心的设备以及使用 Azure IoT 中心的代码片段进行开发

![Code snippets for Azure IoT Hub screenshot](https://raw.githubusercontent.com/formulahendry/vscode-azure-iot-toolkit/master/images/device-explorer.png)

## 书签

> 标记行并跳转到它们

## 浏览器预览（已弃用）

> VS Code 的浏览器预览使您能够在编辑器中打开可以调试的真实浏览器预览。浏览器预览由 Chrome Headless 提供支持，并通过在新进程中启动无头 Chrome 实例来工作。这提供了一种在 VS Code 内渲染 Web 内容的安全方式，并启用了有趣的功能，例如编辑器内调试等！

![Browser Preview Demo](https://raw.githubusercontent.com/auchenberg/vscode-browser-preview/master/resources/demo.gif)

## 颜色标签

> 大型项目或单一存储库的扩展，可根据当前包为选项卡/标题栏着色

![Color your tabs and/or titlebar based on regex](https://raw.githubusercontent.com/oreporan/color-tabs-vscode/master/docs/coverGif.gif)

## 创建测试

> 快速生成测试文件的扩展。

![Create tests extension animation](https://media.giphy.com/media/1iqPhENd8SLd9SggeX/giphy.gif)

## 树突

> 一个扩展，可以将 Visual Studio Code 变成 PKM 工具，具有出色的 UX，使用 Markdown 文件来组织和引用任意数量的知识。无论您是使用 PARA 或 Zettelkasten 组织笔记、像 Roam 一样将笔记链接在一起，还是只是以临时方式创建笔记，Dendron 都可以提供帮助。将其视为第二个大脑，帮助您理解所有您关心的信息。奖励：如果也使用“dendron-cli”，Dendron 还可以通过 NextJS 发布静态站点。

![dendron.dendron](https://foundation-prod-assetspublic53c57cce-8cpvgjldwysl.s3-us-west-2.amazonaws.com/assets/images/graph-intro.gif)

## 部署

> 用于将工作区的文件上传或复制到目的地的命令。

![Upload/copy files animation](https://raw.githubusercontent.com/mkloubert/vs-deploy/master/img/demo.gif)

## 重复动作

> 能够复制文件和目录。

## 误差镜头

> 显示内联语言诊断（错误/警告/...）。

![error lens demo gif](https://user-images.githubusercontent.com/9638156/71784742-de421b00-3007-11ea-8862-8c6ea2836202.gif)

## 切换

> 通过您最喜欢的键绑定切换任何 VS Code 设置。

通过快捷方式切换“typescript.inlayHints.functionLikeReturnTypes.enabled”的示例：

![切换示例演示](截图/toggle-example.gif)

## ES7 React/Redux/GraphQL/React-Native 片段

> 在 ES7 中提供 Javascript 和 React/Redux 片段

![es7-reactreduxgraphqlreact-native-snippets](https://user-images.githubusercontent.com/37667437/46757404-aa365800-cce7-11e8-80ca-9207b7a68dea.png)

### 吉
> 生成 .gitignore 文件变得容易。

![.gitignore generation animation](https://raw.githubusercontent.com/hasit/vscode-gi/master/assets/gi.gif)

## Git 历史

> 查看 git 日志、文件或行历史记录

## Git 项目经理

> 自动索引您的 git 项目并让您轻松在它们之间切换

## 吉特链接

> 在浏览器中转到当前文件的在线链接并将链接复制到剪贴板中。

![GoTo current file online animation](https://raw.githubusercontent.com/qinezh/vscode-gitlink/master/images/how_to_use_it.gif)

## 吉特透镜

> 提供 Git CodeLens 信息（最近提交、作者数量）、按需内联责任注释、状态栏责任信息、文件和责任历史浏览器以及用于将更改与工作树或以前版本进行比较的命令。

![GitLens inline git information animation](https://raw.githubusercontent.com/eamodio/vscode-git-codelens/master/images/docs/gitlens-preview.gif)

## Git 指标

> 活动面板上类似 Atom 的 git 指示器

![git added indicator screenshot](https://raw.githubusercontent.com/lamartire/vscode-git-indicators/master/preview/added.png)
![git removed indicator screenshot](https://raw.githubusercontent.com/lamartire/vscode-git-indicators/master/preview/removed.png)
![git modified indicator screenshot](https://raw.githubusercontent.com/lamartire/vscode-git-indicators/master/preview/modified.png)

## 亚搏体育appGitLab工作流程
> 添加 GitLab 侧边栏图标以查看问题、合并请求和其他 GitLab 资源。  您还可以查看 GitLab CI/CD 管道的结果并检查“.gitlab-ci.yml”的语法。

#### 摇篮任务

> 在 VS Code 中运行 gradle 任务。

![Gradle Tasks](https://raw.githubusercontent.com/badsyntax/vscode-gradle/master/images/screencast.gif)

## 图标字体

> 流行图标字体的片段，例如 Font Awesome、Ionicons、Glyphicons、Octicons、Material Design Icons 等等！

## 进口成本

> 此扩展将在编辑器中内嵌显示导入包的大小。该扩展使用 webpack 和 babili-webpack-plugin 来检测导入的大小。

## Jira 和 Bitbucket

> 将 Jira 和 Bitbucket 的强大功能引入 VS Code - 使用 Atlassian for VS Code，您可以创建和查看问题、开始处理问题、创建拉取请求、进行代码审查、开始构建、获取构建状态等等！

![Jira and Bitbucket workflow](https://bitbucket.org/atlassianlabs/atlascode/raw/master/.readme/dev-workflow.gif)

## JS 参数注解

> 为 JS/TS 文件中的函数调用提供注释，为参数提供参数名称。

![JS Parameter Annotations](https://raw.githubusercontent.com/lannonbr/vscode-js-annotations/master/jsannotations.png)

## 神经质

> 提供快速光标移动，灵感来自 Atom 的同名包。

![Jumpy](https://cloud.githubusercontent.com/assets/2899448/19660934/0481c44c-9a32-11e6-87cc-1f8913922ccb.gif)

## 看板

![kanban](https://raw.githubusercontent.com/mkloubert/vscode-kanban/master/img/demo1.gif)

> 用于 Visual Studio Code 的简单看板，具有时间跟踪和 Markdown 支持。

## 实时服务器

> 启动具有静态和动态页面实时重新加载功能的开发本地服务器。

![live-server](https://raw.githubusercontent.com/ritwickdey/vscode-live-server/master/images/Screenshot/vscode-live-server-animated-demo.gif)

## 多个剪贴板

> 覆盖常规的复制和剪切命令以将选择保留在剪贴板环中

## 用于 VSCode 的 ngrok

> ngrok 允许您将本地计算机上运行的 Web 服务器公开到互联网。只需告诉 ngrok 您的 Web 服务器正在侦听哪个端口即可。此扩展允许您从 VSCode 命令面板控制 [ngrok](https://ngrok.com/)

![ngrok for VSCode](https://raw.githubusercontent.com/philnash/ngrok-for-vscode/master/images/start.gif)

## Dotnet 核心测试资源管理器

> 直接在编辑器中查看并运行 .NET Core 测试。

![View and run your .NET Core tests directly in the editor animation](https://raw.githubusercontent.com/formulahendry/vscode-dotnet-test-explorer/master/images/test-explorer.gif)

## 国际化盟友

> 🌍 VSCode 的多合一 i18n 扩展

![i18n Ally](https://raw.githubusercontent.com/antfu/i18n-ally/master/screenshots/overview.png)

## 即时降价

>简单地，在 vscode 中编辑 Markdown 文档，并在键入时立即在浏览器中预览它。

![Instant Markdown Screencast](https://raw.githubusercontent.com/dbankier/vscode-instant-markdown/master/vscode-instant-markdown.gif)

## npm 智能感知

> Visual Studio Code 插件可自动完成导入语句中的 npm 模块。

![npm-intellisense](https://raw.githubusercontent.com/ChristianKohler/NpmIntellisense/master/images/auto_complete.gif)

## 参数提示

> 提供JS/TS/PHP文件中函数调用的参数提示。

![Parameter Hints](https://raw.githubusercontent.com/dominicvonk/vscode-parameter-hints/master/preview.png)

## 部分差异

> 比较（差异）文件内、不同文件或剪贴板中的文本选择

![Partial Diff](https://raw.githubusercontent.com/ryu1kn/vscode-partial-diff/master/images/public.gif)

### 将 JSON 粘贴为代码

> 推断 JSON 的结构并粘贴为许多编程语言中的类型

![Paste JSON as Code](https://raw.githubusercontent.com/quicktype/quicktype-vscode/master/media/demo.gif)

## 路径自动完成

> 为 Visual Studio 代码提供路径补全。

![Path Autocomplete](https://raw.githubusercontent.com/ionutvmi/path-autocomplete/master/demo/path-autocomplete.gif)

## 路径智能感知

> 自动完成文件名的 Visual Studio Code 插件

![Autocompletion for filenames animation](https://i.giphy.com/iaHeUiDeTUZuo.gif)

## 电动工具

> 通过基于 Node.js 的脚本或 shell 命令等扩展 Visual Studio Code，无需编写单独的扩展

![Power Tools](https://raw.githubusercontent.com/egomobile/vscode-powertools/master/img/demo.gif)

## 打印代码

> PrintCode 将正在编辑的代码转换为 HTML 文件，通过浏览器显示并打印。

![PrintCode](https://raw.githubusercontent.com/nobuhito/vscode.printcode/master/printcode.gif)

## 项目经理

> 在项目之间轻松切换。

![Switch between projects screenshot](https://raw.githubusercontent.com/alefragnani/vscode-project-manager/master/images/project-manager-commands.png)

## 项目仪表板

> VSCode 项目仪表板是一个 Visual Studio Code 扩展，可让您以类似快速拨号的方式组织项目。将您经常访问的文件夹、文件和 SSH 遥控器固定到仪表板上以快速访问它们。

![Project Dashboard](https://user-images.githubusercontent.com/5564731/79053450-b7663700-7c3d-11ea-8498-bbfe7723b47f.gif)

## 彩虹 CSV
> 突出显示逗号、制表符、分号和管道分隔文件中的列、使用 CSVLint 进行一致性检查和检查、多光标列编辑、列修剪和重新对齐以及使用 RBQL 进行 SQL 样式查询。

![Rainbow CSV](https://i.imgur.com/PRFKVIN.png)

## 远程开发

> 允许用户打开容器、远程计算机、容器或适用于 Linux 的 Windows 子系统 (WSL) 中的任何文件夹，并利用 VS Code 的完整功能集。

![Remote SSH extension at work](https://microsoft.github.io/vscode-remote-release/images/ssh-readme.gif)

## 远程 VSCode

> 允许用户直接在 Visual Studio Code 中编辑来自远程服务器的文件。

## 休息客户端

> 允许您发送 HTTP 请求并直接在 Visual Studio Code 中查看响应。

![Send HTTP request and view response animation](https://raw.githubusercontent.com/Huachao/vscode-restclient/master/images/usage.gif)

## 文本电动工具

> 用于文本操作的多合一扩展：过滤 (grep)、删除行、插入数字序列和 GUID、将内容格式化为表格、更改大小写、转换数字等等。非常适合在日志中查找信息和操作文本。

![Text Power Tools](https://raw.githubusercontent.com/qcz/vscode-text-power-tools/89a1d9d7be3edfc9bcf112fe427c662655cb60cc/images/filtering.gif)

## 都都树

> 自定义 TODO 评论的关键字、突出显示和颜色。以及用于查看所有当前标签的侧边栏。

![Todo Tree](https://thumbs.gfycat.com/PowerlessWindyCivet-size_restricted.gif)

## 切换引号

> 在单引号、双引号和反引号之间循环

![Toggle Quotes](https://d3vv6lp55qjaqc.cloudfront.net/items/2V092N0u2O1a393Y0f28/Screen%20Recording%202018-10-04%20at%2009.26%20AM.gif?X-CloudApp-Visitor-Id=26998&v=e2908c88)

## 打字稿解构

> TypeScript 语言服务插件提供一组源操作以方便对象解构

![Typescript Destructure](https://raw.githubusercontent.com/tusaeff/vscode-typescript-destructure-plugin/master/assets/destructure-to-constant.gif)

## 瓦卡时间

> 自动时间跟踪器和生产力仪表板显示您在每个项目、文件、分支和语言中编码的时间。

## 哟

> 使用 [Yeoman](https://yeoman.io/) 的脚手架项目

![Using yeoman animation](https://raw.githubusercontent.com/SamVerschueren/vscode-yo/master/media/yo.gif)

## 时机

> 时间转换器扩展，可将时间戳转换为各种格式，并按需插入或仅显示它们。它还提供了一个简洁的悬停提供程序来立即美化纪元时间戳。所有功能都是高度可定制的。

![Timing](https://raw.githubusercontent.com/HaaLeo/vscode-timing/master/doc/Convert_Sample.gif)

# 格式与美化

## 更好地对齐

> 通过冒号（:)、赋值（=、+=、-=、*=、/=）和箭头（=>）对齐代码。它还支持逗号优先的编码风格和尾随注释。
>
> 并且它不需要您选择要对齐的内容，扩展程序会自行计算出来。

![Better Align](https://raw.githubusercontent.com/WarWithinMe/better-align/master/images/2.gif)

## 自动重命名标签

> 原生设置，只需将 `"editor.linkedEditing": true` 添加到您的 `settings.json` 文件中

> 自动重命名配对的 HTML/XML 标签

![Auto rename paired HTML/XML tags animation](https://raw.githubusercontent.com/formulahendry/vscode-auto-rename-tag/master/images/usage.gif)

## 美化

> 针对 VS Code 美化代码

### html2pug

> 在 Visual Studio Code 中将 html 转换为 pug，不再需要使用外部页面。

## ECMAScript 引用转换器

> 转换 ECMAScript 字符串文字的引号

![Transform quotes of ECMAScript string literals animation](https://cloud.githubusercontent.com/assets/970430/10563944/4cc04462-75d1-11e5-984b-41e0a21a72c3.gif)

## 粘贴和缩进

> 粘贴带有“正确”缩进的代码

![Indentation of pasted code animation](https://github.com/vikrantnegi/vscode-personal-preference-setting/blob/master/screenshots/pasteandindent.gif)

## 排序线

> 按特定顺序对文本行进行排序

![Sorts lines of text in specific order animation](https://raw.githubusercontent.com/Tyriar/vscode-sort-lines/master/images/usage-animation.gif)

## 环绕声

> 一个简单但功能强大的扩展，用于在代码块周围添加包装模板。

![Wrap a template around a code block](https://raw.githubusercontent.com/yatki/vscode-surround/master/images/demo.gif)

## 包裹选择

> 用一个或多个符号包裹选定内容或多个选定内容

![Wraps selection or multiple selections with symbol or multiple symbols animation](https://github.com/gko/wrap/blob/master/features.gif)

## 格式切换

> 只需单击一下即可打开和关闭格式化程序

## 自动导入
> 自动查找、解析并为所有可用导入提供代码操作和代码完成。适用于 Typescript 和 TSX。

![Auto import](https://camo.githubusercontent.com/c952445b4a04a9d358be991cc2d830f2a4c0f33b/68747470733a2f2f67696679752e636f6d2f696d616765732f6175746f696d706f72742e676966)

## shell格式
> shell 脚本 & Dockerfile & dotenv 格式

![shell-format](https://raw.githubusercontent.com/foxundermoon/vs-shell-format/master/image/shell_format.gif)

## vscode 谷歌翻译
> 快速翻译代码中选定的文本

![Vscode Google Translate](https://raw.githubusercontent.com/funkyremi/vscode-google-translate/master/demo.gif)

## 资源管理器图标

### 城市之光图标

![City Lights Icons](https://raw.githubusercontent.com/yummygum/city-lights-icons-vsc/master/city-lights-icon-preview.gif)

### VSCode 图标

![VSCode Icons](https://raw.githubusercontent.com/vscode-icons/vscode-icons/master/images/screenshot.gif)

### 塞蒂图标

![Seti Icons](https://raw.githubusercontent.com/hellopao/vscode-seti-icons/master/screenshot.png)

### 材质图标主题

![Material Icon Theme](https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/master/images/fileIcons.png)

# 未分类

## 代码之路

> 在您最喜欢的编辑器中播放交互式教程。

![CodeRoad Demo](https://raw.githubusercontent.com/coderoad/coderoad-vscode/master/docs/static/gif/coderoad-example.gif)

## 代码运行者

> 运行多种语言的代码片段或代码文件：C、C++、Java、JavaScript、PHP、Python、Perl、Ruby、Go、Lua、Groovy、PowerShell、BAT/CMD、BASH/SH、F# Script、C# Script、VBScript、TypeScript、CoffeeScript、Scala、Swift、Julia、Crystal、OCaml Script

![Run a snippet or file animation](https://raw.githubusercontent.com/formulahendry/vscode-code-runner/master/images/usage.gif)

## 编码时间

> 直接在 VS Code 中按项目和其他编程指标自动生成时间报告。

![Code Time](https://camo.githubusercontent.com/918d2dfc585074f3b20566723f3ab8ce32e9d23e/68747470733a2f2f737764632d7673636f64652e73332d75732d776573742d312e616d617a6f6e6177732e636f6d2f636f64652d74696d652d66656174757265732e706e67)

## 颜色高光

> 在编辑器中突出显示网页颜色

![Highlight web colors in your editor screenshot](https://cdn-images-1.medium.com/max/1600/1*ZwE7OHKR5opvDCJJOw9KeQ.png)

## 输出着色器
> VS Code 输出面板和日志文件的语法突出显示

![IBM.output-colorizer](https://raw.githubusercontent.com/IBM-Bluemix/vscode-log-output-colorizer/master/github-assets/screenshot-1.jpg)

## 冲刺

> Visual Studio Code 中的 Dash 集成

![Dash integration screenshot](https://cdn-images-1.medium.com/max/2000/1*sqGllC-pgXNaEBfB-cxG9Q.png)

## 使用 Shell 命令进行编辑

> 利用您最喜欢的 shell 命令来编辑文本

![Edit with Shell Command](https://raw.githubusercontent.com/ryu1kn/vscode-edit-with-shell/master/images/animations/public.gif)

## VS Code 的编辑器配置

> VS Code 的编辑器配置

## FTP 同步

> 自动将您的工作同步到远程 FTP 服务器

![Auto-sync your work to remote FTP server animation](https://i.imgur.com/W9h4pwW.gif)

## 突出显示 JSX/HTML 标签

> 突出显示文件中匹配的标签。

![](https://camo.githubusercontent.com/010b886fb93f49c56e4c7308ba0a5a1aca8a2db7/68747470733a2f2f692e696d67626f782e636f6d2f4455584c467657372e676966)

## 缩进彩虹

> 一个简单的扩展，使缩进更具可读性。

![indent-rainbow](https://raw.githubusercontent.com/oderwat/vscode-indent-rainbow/master/assets/example.png)

## iTerm2 主题同步

> 将选定的 VSCode 主题与 iTerm2 颜色配置文件同步

![iTerm2 Theme Sync](https://raw.githubusercontent.com/tusaeff/vscode-iterm2-theme-sync/master/screencast.gif)

## 密码生成器

> 使用我们的生成器工具创建安全密码。立即获取强密码，帮助防止安全威胁。

![Password Generator](https://raw.githubusercontent.com/ftonato/vscode-password-generator/master/preview.gif)

## 平台IO

> 物联网开发的开源生态系统：支持350+嵌入式板卡、20+开发平台、10+框架。 Arduino 和 ARM mbed 兼容。

![Build using platformio animation](https://raw.githubusercontent.com/formulahendry/vscode-platformio/master/images/build.gif)

## 波拉码

> 宝丽来为您的代码📸。

![Make a polaroid image of your code animation](https://raw.githubusercontent.com/octref/polacode/master/demo/usage.gif)

## 碳现在SH
> 将您的代码发送至 [carbon.now.sh](https://carbon.now.sh)。
 ![Send your code to carbon.now.sh animation](https://user-images.githubusercontent.com/6516758/46617867-df765680-caeb-11e8-8899-95778cdcceb7.gif)

## 短尾矮袋鼠

> VS Code 中 JavaScript 和 TypeScript 的快速原型设计平台，可以访问项目文件、内联报告、代码覆盖率和丰富的输出格式。

![Integrated JavaScript/TypeScript playground animation](https://quokkajs.com/assets/img/main-video.gif)

## 跑步者

> 直接从 VS Code 运行各种脚本

![Run various scripts right from VS Code animation](https://raw.githubusercontent.com/mattn/vscode-runner/master/images/screenshot.gif)

## 松弛

> 发送消息和代码片段，将文件上传到 Slack

![Send messages or code snippets to Slack animation](https://raw.githubusercontent.com/sozercan/vscode-slack/master/slack-upload.gif)

## Spotify
> 提供与 Spotify 桌面客户端的集成。在状态栏中显示当前播放的歌曲、搜索歌词并提供通过按钮和热键控制 Spotify 的命令。

![vscode-spotify](https://media.giphy.com/media/3ohhwMgeIj1MhEdBJe/giphy.gif)

## 静止无功发生器

> 强大的SVG语言支持扩展（测试版）。几乎拥有处理 SVG 所需的所有功能。

![SVG](https://raw.githubusercontent.com/lishu/vscode-svg/master/images/f1.png)

## SVG 查看器

> 在编辑器中查看 SVG 并将其导出为数据 URI 方案或 PNG。

![SVG Viewer](https://github.com/cssho/vscode-svgviewer/blob/master/img/preview.png)

## 文本标记（荧光笔）

> 同时用不同的颜色突出显示多个文本图案。可以使用编辑器的搜索功能来突出显示单个文本模式，但它不能同时突出显示多个模式，而这正是此扩展派上用场的地方。

![Text Marker (Highlighter)](https://raw.githubusercontent.com/ryu1kn/vscode-text-marker/master/images/animations/public.gif)

## ESDOC MDN

> 在编辑器中快速调出有用的 MDN 文档

![ESDOC MDN](https://raw.githubusercontent.com/samundrak/vscode-esdoc-mdn/master/demo.gif)

## 接口生成器

> 从 typescript 类快速生成接口定义

![Interface generator](https://raw.githubusercontent.com/dotupNET/dotup-vscode-interface-generator/master/images/video2.gif)

## 杰蛙

> 将项目依赖项的 JFrog Xray 扫描添加到 VS Code IDE。它允许开发人员直接在 VS Code IDE 中查看显示有关组件及其依赖项的漏洞信息的面板。该扩展还允许开发人员在 CI 服务器上构建、测试和扫描代码时跟踪代码的状态。

![JFrog](https://raw.githubusercontent.com/jfrog/jfrog-vscode-extension/master/resources/readme/gifs/show_in_dependency_tree.gif)

# 主题

## 用户界面

如果您足够勇敢，至少有两个适用于 VS Code 的自定义 UI：

- [Essence](https://github.com/essence-language/vscode-extension)
- [务实本质](https://github.com/orta/Essence)

## 语法

### 2077 主题 by Endormi

受赛博朋克 2077 启发的主题

<a href="https://vscodethemes.com/e/Endormi.2077-theme">
  <img src="./themes/screenshots/endormi.2077-theme.png" width="600" />
</a>

### 达斯汀·桑德斯的《旧希望》主题

VSCode 主题的灵感来自遥远的星系......

<a href="https://vscodethemes.com/e/dustinsanders.an-old-hope-theme-vscode">
  <img src="./themes/screenshots/dustinsanders.an-old-hope-theme-vscode.png" width="600" />
</a>

### 有明暗疣

深色 VSCode 主题的灵感源自日本传统色彩和 1000 年前创作的诗歌。

<a href="https://vscodethemes.com/e/wart.ariake-dark">
  <img src="./themes/screenshots/wart.ariake-dark.png" width="600" />
</a>

### Mahmoud Ali 的 Atom One Dark 主题

基于 Atom 的 One Dark 主题。

<a href="https://vscodethemes.com/e/akamud.vscode-theme-onedark">
  <img src="./themes/screenshots/akamud.vscode-theme-onedark.png" width="600" />
</a>

### Emroussel雾化

详细而准确的 Atom One Dark 主题。

<a href="https://vscodethemes.com/e/emroussel.atomize-atom-one-dark-theme">
  <img src="./themes/screenshots/atomize.png" width="600" />
</a>

### 香鱼 by Teabyii

简单的主题，明亮的色彩，提供三种版本——深色、浅色和海市蜃楼，适合全天舒适的工作。

<a href="https://vscodethemes.com/e/teabyii.ayu">
  <img src="./themes/screenshots/teabyii.ayu.png" width="600" />
</a>

### 亚历山大·埃克特 (Alexander Eckert) 的 Borealis 主题

VS Code 主题的灵感来自阿拉斯加北极光的平静色彩。

<a href="https://vscodethemes.com/e/eckertalex.borealis">
  <img src="./themes/screenshots/eckertalex.borealis.png" width="600" />
</a>

### 甜心船长 by ultradracula

凝灰岩但甜蜜的主题。

<a href="https://vscodethemes.com/e/ultradracula.captain-sweetheart">
  <img src="./themes/screenshots/ultradracula.captain-sweetheart.png" width="600" />
</a>

### Yummygum 的城市之光

🏙 Yummygum 的官方城市之光套件

<a href="http://citylights.xyz">
  <img src="./themes/screenshots/city-lights-yummygum.png" width="600" />
</a>

### Cobalt2 主题 官方作者：Wes Bos

🔥 Wes Bos 的官方主题。

<a href="https://vscodethemes.com/e/wesbos.theme-cobalt2">
  <img src="./themes/screenshots/wesbos.theme-cobalt2.png" width="600" />
</a>

### Dracula 官方 Dracula 主题

官方德古拉主题。适用于许多编辑器、shell 等的深色主题。

<a href="https://vscodethemes.com/e/dracula-theme.theme-dracula">
  <img src="./themes/screenshots/dracula-theme.theme-dracula.png" width="600" />
</a>

### 博格丹·拉扎尔的边缘

简单的主题，明亮的色彩，三种变体——夜空、宁静和海洋，适合全天舒适的工作。

<a href="https://vscodethemes.com/e/bogdanlazar.edge">
  <img src="./themes/screenshots/bogdanlazar.edge-theme.png" width="600" />
</a>

### 伊娃主题由fisheva设计

丰富多彩且语义化的着色代码主题。

<a href="https://vscodethemes.com/e/fisheva.eva-theme">
  <img src="./themes/screenshots/fisheva.eva-theme.png" width="600" />
</a>

### 仙女牙线，作者：nopjmp 和 sailorhg

由 sailorhg 制作的有趣的紫色粉彩/糖果/白日梦仙牙主题。

<a href="https://vscodethemes.com/e/nopjmp.fairyfloss">
  <img src="./themes/screenshots/nopjmp.fairyfloss.png" width="600" />
</a>

### Thomas Pink 的 GitHub 主题

Visual Studio Code 的 GitHub 主题。

<a href="https://vscodethemes.com/e/thomaspink.theme-github">
  <img src="./themes/screenshots/thomaspink.theme-github.png" width="600" />
</a>

### Dimitar Nonov 的 Jellybeans 主题

Visual Studio Code 的 Jellybeans 主题。

<a href="https://vscodethemes.com/e/DimitarNonov.jellybeans-theme">
  <img src="./themes/screenshots/jellybeans-theme.png" width="600" />
</a>

### 由 Whizkydee 设计的 Material Palenight 主题

Visual Studio Code 的优雅且多汁的类似材料的主题。

<a href="https://vscodethemes.com/e/whizkydee.material-palenight-theme">
  <img src="./themes/screenshots/whizkydee.material-palenight-theme.png" width="600" />
</a>

### Mattia Astorino 的材质主题

Visual Studio Code 现在最史诗般的主题。

<a href="https://vscodethemes.com/e/Equinusocio.vsc-material-theme">
  <img src="./themes/screenshots/Equinusocio.vsc-material-theme.png" width="600" />
</a>

### 由 u29dc 制作的 Mno

最小的单色主题。

<a href="https://vscodethemes.com/e/u29dc.mno">
  <img src="./themes/screenshots/u29dc.mno.png" width="600" />
</a>

### Monokai Oblique，作者：pushqrdx

Monokai 启发了 [Visual Studio Code](https://vscodethemes.com/e/pushqrdx.theme-monokai-oblique-vscode) 和 [Visual Studio IDE](https://github.com/pushqrdx/monokai) 的主题。

<a href="https://marketplace.visualstudio.com/items?itemName=pushqrdx.theme-monokai-oblique-vscode">
  <img src="./themes/screenshots/moblique.png" width="600" />
</a>

### Monokai Pro by monokai（商业）

为专业开发人员提供的精美功能，来自原始 Monokai 配色方案的作者。

<a href="https://vscodethemes.com/e/monokai.theme-monokai-pro-vscode">
  <img src="./themes/screenshots/1079cc76.png" width="600" />
</a>

### 莎拉·德拉斯纳的《夜猫子》

适合夜猫子的 VS Code 主题。在白天也很有效，但这个主题针对我们这些喜欢在深夜编码的人进行了微调。颜色选择考虑了色盲人士和弱光环境下的可及性。决策还基于阅读理解和最佳视觉效果的有意义对比。 ✨

<a href="https://marketplace.visualstudio.com/items?itemName=sdras.night-owl">
  <img src="./themes/screenshots/night-owl.png" width="600" />
</a>

### 威尔斯通的塑料

一个简单的主题。

<a href="https://vscodethemes.com/e/will-stone.plastic">
  <img src="./themes/screenshots/will-stone.plastic.png" width="600" />
</a>

### Nord 由 arcticicestudio 设计

北极、北蓝色、干净、优雅的 Visual Studio Code 主题。

<a href="https://vscodethemes.com/e/arcticicestudio.nord-visual-studio-code">
  <img src="./themes/screenshots/arcticicestudio.nord-visual-studio-code.png" width="600" />
</a>

### 戴尔·里斯 (Dayle Rees) 的《Rainglow》

320 多个精美语法和 UI 主题的集合。

<a href="https://vscodethemes.com/e/daylerees.rainglow">
  <img src="https://raw.githubusercontent.com/rainglow/examples/master/vscode/gloom-contrast.png" width="600" />
</a>

### Michael Kühnel 的轻松主题

轻松的主题，可以更轻松地看待事物。

<a href="https://vscodethemes.com/e/mischah.relaxed-theme">
  <img src="./themes/screenshots/relaxed-theme.png" width="600" />
</a>

### 艾哈迈德·阿瓦伊斯的《紫色阴影》

⚡ 专业主题，带有精心挑选的大胆紫色色调 💜，可与您的 VS Code 搭配。具有风格的自定义 VS Code 主题。

<a href="https://vscodethemes.com/e/ahmadawais.shades-of-purple">
  <img src="./themes/screenshots/ahmadawais.shades-of-purple.png" width="600" />
</a>

### 史莱姆主题由 smlombardi 设计

Visual Studio Code 的深色语法/工作台主题 - 针对 SCSS、HTML、JS、TS、Markdown 和 PHP 文件进行了优化。

<a href="https://vscodethemes.com/e/smlombardi.slime">
  <img src="./themes/screenshots/slime.png" width="600" />
</a>

### Niketa 主题由 Dejan Toteff 设计

18 个灯光主题的集合，按背景亮度分为 4 组。

 <a href="https://vscodethemes.com/e/mischah.relaxed-theme">
  <img src="./themes/screenshots/niketa-theme.png" width="600" />
</a>

# 要关注的人

VS Code 社区中各种人员的 Twitter 帐户列表

- [@code](https://twitter.com/code) - VS Code 官方 Twitter
- [@auchenberg](https://twitter.com/auchenberg) - VS 代码程序管理器
- [@BenjaminPasero](https://twitter.com/BenjaminPasero) - VS 代码开发
- [@chrisdias](https://twitter.com/chrisdias) - VS 代码程序管理器
- [@_clarkio](https://twitter.com/_clarkio) - 开发者倡导者@Azure。 VS Code 创作者发布精彩视频
- [@eamodio](https://twitter.com/eamodio) - GitLens 创建者
- [@ErichGamma](https://twitter.com/ErichGamma) - VS 代码开发
- [@IsidorN](https://twitter.com/@IsidorN) - VS 代码开发
- [@joaomoreno](https://twitter.com/joaomoreno) - VS 代码开发
- [@johannesrieken](https://twitter.com/johannesrieken) - VS 代码开发
- [@lannonbr](https://twitter.com/lannonbr) - vscode.rocks 和 JS 参数注释扩展的创建者
- [@maeschli](https://twitter.com/maeschli) - VS 代码开发
- [@mattbierner](https://twitter.com/mattbierner) - VS 代码开发
- [@MrAhmadAwais](https://twitter.com/MrAhmadAwais) - JS/WordPress 核心开发。 VSCode.pro 课程和 Shades of Purple 主题的创建者
- [@ramyanexus](https://twitter.com/ramyanexus) - VS 代码开发。 Go 扩展的维护者
- [@Tyriar](https://twitter.com/Tyriar) - VS 代码开发。 xterm.js 的创建者

# 扩展开发者资源

## 文档

- [Better Comments](https://marketplace.visualstudio.com/items?itemName=aaron-bond.better-comments) - Better Comments 扩展将帮助您在代码中创建更人性化的注释。
- [官方文档](https://code.visualstudio.com/docs) 的 [Visual Studio Code API](https://code.visualstudio.com/api) 部分

## 图书馆

- [vscode-test-content](https://github.com/mlewand-org/vscode-test-content) - 一种设置/获取编辑器内容及其选择的方法。对于单元测试特别有用。
- [typed-vscode](https://www.npmjs.com/typed-vscode) - 从扩展清单的贡献点生成类型

## 工具

- [Live Share](https://marketplace.visualstudio.com/items?itemName=MS-vsliveshare.vsliveshare) - Visual Studio Live Share 使您能够与其他人实时协作编辑和调试，无论您使用什么编程语言或正在构建的应用程序类型。
- [Online TextMate Themes Editor](https://tmtheme-editor.herokuapp.com/) - 由于 VS Code 支持 TextMate 主题，因此您可以在此在线编辑器中创建它们，然后使用 [Yo Code](https://code.visualstudio.com/docs/extensions/yocode) 工具创建新的 VS Code 包
- [Yo Code - 扩展生成器](https://code.visualstudio.com/docs/extensions/yocode)
- [Open in Code](https://github.com/sozercan/OpenInCode) - 用于在 Visual Studio Code 中打开当前文件夹的 macOS Finder 工具栏应用

![macOS Finder toolbar app to open current folder in Visual Studio Code animation](https://camo.githubusercontent.com/edbae5fe27d6c7af23218e60cb07e3a5061bbbab/687474703a2f2f692e696d6775722e636f6d2f4c6d56484978572e676966)

- [Themer](https://themer.dev) - 轻松为 VS Code 创建您自己的主题（以及与其他工具匹配的主题）。
- [Azure Tools for Visual Studio Code](https://github.com/bradygaster-zz/azure-tools-vscode) - Visual Studio Code 的此扩展为 Azure 开发人员提供了一些方便的命令，用于直接在编辑器中创建或访问资源。

![azure-tools-vscode](https://raw.githubusercontent.com/johnpapa/vscode-azure-functions-tools/master/images/json-schema-function.gif)

- [Mark down preview](https://marketplace.visualstudio.com/items?itemName=shd101wyy.markdown-preview-enhanced) - Markdown Preview Enhanced 是一个扩展，为您提供许多有用的功能，例如自动滚动同步、数学排版、美人鱼、PlantUML、pandoc、PDF 导出、代码块、演示文稿编写器等。它的很多想法都受到 Markdown Preview Plus 和 RStudio Markdown 的启发。

# 在线课程

## Visual Studio Code 高级用户课程（商业）

在使用 Sublime Text 10 年后，[Ahmad Awais](https://twitter.com/MrAhmadAwais/) 转向 VSCode，构建了 [Shades of Purple 主题](https://marketplace.visualstudio.com/items?itemName=ahmadawais.shades-of-purple)，并花费了 1,000 多个小时完善他的设置。他今天推出了 VSCode 高级用户课程来帮助您进行切换。您可以从以前的编辑器中引入所有自定义设置，并学习 HTML/CSS、Git/GitHub 和开源、增压 Markdown 以及从 JavaScript 到 PHP、Go、Python、C++、C#、ROR 的所有内容的高级用户工作流程。在本课程中，您还将学习如何安装/设置 50 多个扩展。

- [VSCode.pro](https://vscode.pro/) - 📺 长达 5 小时、65 个视频的 VSCode 课程。
- [Ahmad Awais](https://twitter.com/MrAhmadAwais/) - 🙌 紫色主题的创建者。 WP/JS 核心开发人员。 OSS 开发倡导者。

# 贡献

欢迎投稿！首先阅读[贡献指南](CONTRIBUTING.md)。

# 许可证

我根据开源许可证向您提供此存储库中的代码和资源。因为这是我的个人存储库，所以您收到的我的代码和资源的许可证来自我，而不是我的雇主 (Microsoft)。

[![CC0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

在法律允许的范围内，[Valerii Iatsko](https://viatsko.me) 已放弃本作品的所有版权以及相关或邻接权。
