# 很棒的原子 [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

令人愉快的 Atom 软件包和资源的精选列表。如需更多精彩内容，请查看 [awesome](https://github.com/sindresorhus/awesome)。

## 目录

- [Syntax](#syntax)
- [Lint](#lint)
- [Build](#build)
- [Extensions](#extensions)
  - [Nuclide](#nuclide)
- [Themes](http://enrmarc.github.io/atom-theme-gallery/)
- [Collaboration](#collaboration)
  - [CodeSideStory](#codesidestory)
- [Uncategorized](#uncategorized)
  - [Nuclide](#nuclide)
  - [高级打开文件](#advanced-open-file)
  - [原子反转器](#atom-reverser)
  - [原子终端](#atom-terminal)
  - [自动完成模块导入](#autocomplete-module-import)
  - [Beautify](#beautify)
  - [代码预览](#code-peek)
  - [颜色选择器](#color-picker)
  - [复制粘贴](#copy-paste)
  - [CSS 声明排序器](#css-declaration-sorter)
  - [重复选择](#duplicate-selection)
  - [编辑器配置](#editor-config)
  - [Emmet](#emmet)
  - [文件图标](#file-icons)
  - [Fonts](#fonts)
  - [Git 时间机器](#git-time-machine)
  - [html-to-css](#html-to-css)
  - [iMDone](#imdone)
  - [Jumpy](#jumpy)
  - [合并冲突](#merge-conflicts)
  - [Minimap](#minimap)
  - [Pigments](#pigments)
  - [项目加号](#project-plus)
  - [排序线](#sort-lines)
  - [Sorter](#sorter)
  - [同步设置](#sync-settings)
  - [PlatformIO IDE 终端](#platformio-ide-terminal)
  - [TernJS](#ternjs)
  - [测试导航器](#test-navigator)
  - [Themer](#themer)
  - [切换引号](#toggle-quotes)

## 语法

语言包通过语法突出显示和/或扩展编辑器
特定语言或文件格式的片段。

 - [Angular](https://atom.io/packages/angularjs)
 - [Vue.js](https://atom.io/packages/language-vue)
 - [Dockerfile](https://atom.io/packages/language-docker)
 - [Markdown](https://atom.io/packages/language-markdown)
 - [React](https://atom.io/packages/react)
 - [Stylus](https://atom.io/packages/stylus)
 - [Pug](https://atom.io/packages/language-pug)
 - [Tcl](https://atom.io/packages/language-tcl)
 - [TypeScript](https://atom.io/packages/atom-typescript)

## 皮棉

如果你还没有释放出令人敬畏的必杀技：
> lint 最初是一个特定程序的名称，该程序在 C 语言源代码中标记了一些可疑且不可移植的结构（可能是错误）。该术语现在一般适用于标记以任何计算机语言编写的软件中的可疑使用情况的工具。

要启用 linting，您需要通用的 [linter](https://atom.io/packages/linter)，它为特定语言的提供程序插件提供接口。当前插件的完整列表可以在 [atomlinter.github.io](http://atomlinter.github.io/) 找到，几个例子是：

- C++
   - [linter-clang](https://atom.io/packages/linter-clang)
   - [linter-cppcheck](https://atom.io/packages/linter-cppcheck)
   - [linter-gcc](https://atom.io/packages/linter-gcc) - 即时 linting！
   - [linter-cpplint](https://atom.io/packages/linter-cpplint) - 检查谷歌风格指南
 - [CSS](https://atom.io/packages/linter-stylelint) - 风格林特
 - [JavaScript](https://atom.io/packages/linter-eslint) - 埃斯林特
 - [Python](https://atom.io/packages/linter-pylama) - 皮拉马
 - [SASS](https://atom.io/packages/linter-sass-lint) - sass-lint
 - [Stylus](https://atom.io/packages/linter-stylint) - 笔杆
 - [TypeScript](https://atom.io/packages/linter-tslint) - 茨林特

 ![atom-linter](https://camo.githubusercontent.com/70b6e697c9d793642414b4ea6d08dbb9678877b3/687474703a2f2f672e7265636f726469742e636f2f313352666d6972507a322e676966)

## 构建

要启用构建，您需要通用的 [build](https://atom.io/packages/build)，它为特定语言的提供程序插件提供接口，并添加与 [lint](#lint) 的集成。当前插件的完整列表可以在 [atombuild.github.io](http://atombuild.github.io/) 找到，一些示例是：

 - [AppleScript](https://atom.io/packages/build-applescript) - os编译
 - [C/C++/Objective C](https://atom.io/packages/build-xcodebuild) - xcodebuild
 - [CoffeeScript](https://atom.io/packages/build-coffee) - 咖啡
 - [GNU Make](https://github.com/AtomBuild/atom-build-make) - 使
 - [Sass](https://atom.io/packages/build-sass) - 萨斯
 - [TypeScript](https://atom.io/packages/build-tsc) - TSC

 ![atom-build](https://camo.githubusercontent.com/ca10be645c7a2024dddc550466e67d692fb411ed/68747470733a2f2f6e6f7365676c69642e6769746875622e696f2f746172676574732d6d616b652e676966)

## 扩展

#### 核素
> 一个用于 Web 和本机移动开发的开放 IDE，构建于由 [Facebook](https://github.com/facebook/nuclide) 维护的 Atom 之上。

![](https://nuclide.io/static/images/docs/promo-hack.png)

## 协作

#### 代码旁白
> Atom/Slack 集成可直接从编辑器启动有关代码的对话。记录屏幕并将其存档在行号旁边，以便为您的代码提供更多上下文。

![](https://storage.googleapis.com/codesidestory/static/media/atom_ss.c29b4b0b.png)

## 未分类

#### 高级打开文件
> 帮助Atom 用户轻松打开文件和文件夹。如果当前不存在，它还可以创建新文件和文件夹。

![](http://osmose.github.io/advanced-open-file/demo.gif)

#### 原子反转器
> 反转您当前的选择；例如从“假”到“真”

![Atom Reverser in action](https://i.imgur.com/YawGVsN.gif)

#### 原子终端
> 在 Atom 中使用“Ctrl-Shift-T”在当前文件的目录上启动终端应用程序。

![](https://raw.githubusercontent.com/karan/atom-terminal/master/terminal.gif)

#### 自动完成模块导入
> 通过 [Algolia](https://www.algolia.com/) 从 import/require 语句搜索并安装 npm 包

![](https://camo.githubusercontent.com/53350e9c6d303f60101e1644605fe62f529e45f2/687474703a2f2f672e7265636f726469742e636f2f643576695542385859372e676966)

#### 美化
> [美化](https://github.com/beautify-web/js-beautify)
HTML（包括[Handlebars](http://handlebarsjs.com/)），
CSS（包括[Sass](http://sass-lang.com/)和[LESS](http://lesscss.org/)），
JavaScript 以及 Atom 中的更多内容。

#### 代码预览
> 从当前编辑器的上下文中快速查看和编辑单独文件中的函数。

![Code Peek Demo](https://github.com/DFreds/code-peek-atom/blob/master/code-peek.gif?raw=true)

#### 颜色选择器
> 支持 HEX、HEXa、RGB、RGBa、HSL、HSLa、HSV、HSVa、VEC3、VEC4 的颜色选择器，并且能够在格式之间进行转换。它还检查 Sass 和 LESS 颜色变量。

![Color Picker in action](https://github.com/thomaslindstrom/color-picker/raw/master/preview.gif)

#### 复制粘贴
> 从剪贴板/缓冲区中输入您的代码。只需复制代码并点击快捷方式即可观看代码的输入。复制粘贴非常适合截屏视频和在线课程。

#### CSS 声明排序器
> 在 Atom 中对 CSS、Less 或 Sass 声明进行排序，永远不会厌倦。您可以从各种现成的订单中进行选择，以保持 CSS 整洁。

![CSS Declaration Sorter Demo](https://github.com/Siilwyn/css-declaration-sorter-atom/raw/master/show-off.gif)

#### 重复选择
> 如果有则复制所选内容，否则复制该行。

#### 编辑器配置
> [EditorConfig](http://editorconfig.org)帮助开发者在不同编辑器之间保持一致的编码风格

![atom-editor-config](https://f.cloud.github.com/assets/170270/2327994/dfe40cb4-a3f6-11e3-862f-894999973373.png)

#### 埃米特
> 大大提高 HTML 和 CSS 编写的插件。快捷方式可以扩展为完整的 HTML 或 CSS 选择器集。

#### 文件图标
> 将文件特定图标添加到atom 以改进视觉 grep。适用于树视图、模糊查找器和选项卡。

#### 字体
> 很多等宽字体。

#### Git 时间机器
> 它显示了当前文件随时间推移的提交的可视化图，您可以在时间图上单击它或将鼠标悬停在图上并查看某个时间范围内的所有提交。

![git-time-machine](https://i.github-camo.com/62085307dccead1c2f5efdf4d7a40f9cdb777b93/68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f6c6974746c656265652f6769742d74696d652d6d616368696e652f6d61737465722f7265736f75726365732f74696d656d616368696e652e676966)

#### html 到 css
> 根据选定的 HTML 生成 CSS 样板。支持 CSS、SCSS、Sass、LESS、BEM、JSX。

![html-to-css](https://camo.githubusercontent.com/b164c4b7b244006a7bcf7442d8c4b0812e4edcd0/687474703a2f2f64726163756c2e6b696c6c2e706c2f2537456172642f68746d6c746f6373732e676966)

#### 我受够了
> 代码中 TODO、FIXME、HACK 等的任务板。

![](https://cloud.githubusercontent.com/assets/441774/9805863/757d5532-5814-11e5-8759-4196bd92c822.gif)

#### 神经质
> 一个 Atom 包，可创建动态热键以在可见窗格中跳转文件。

![](https://raw.githubusercontent.com/DavidLGoldberg/jumpy/master/_images/jumpy.gif)

#### 合并冲突
> 解决 Atom 中的 git 合并冲突。

![](https://raw.github.com/smashwilson/merge-conflicts/master/docs/conflict-resolution.gif)

#### 小地图
> 完整源代码的预览。

#### 颜料
> 用于显示项目和文件中颜色的包。

![](http://abe33.github.io/atom-pigments/pigments.gif?raw=true)

#### 项目加号
> Atom 中的项目管理简直棒极了。

![](https://raw.githubusercontent.com/mehcode/atom-project-plus/master/project-plus.gif)

#### 排序线
> 对您的线路进行排序。永远不会厌倦。

![](https://camo.githubusercontent.com/59de82a667ea690b778abaa5ba8a407f8659ebb3/68747470733a2f2f662e636c6f75642e6769746875622e636f6d2f6173736574732f323938382f313739363839312f38356536396666322d366139332d313165332d383961632d3331393237663630343539322e676966)

#### 分拣机
> 对行、JSON、CSS、HTML、CSV 进行排序。恢复分号。尊重缩进。支持自然排序。

#### 同步设置
> 跨 Atom 实例同步包设置、键盘映射和已安装的包。

#### PlatformIO IDE 终端
> Atom 的终端包，包含主题、API 以及 PlatformIO IDE 的更多内容。
> 这是terminal-plus 的一个维护的（截至2017-07-13）分叉。

![](https://raw.githubusercontent.com/jeremyramin/terminal-plus/master/resources/demo.gif)

#### 特恩JS
> 使用 tern.js 和 autocomplete-plus 实现 Atom 的 Javascript 代码智能。

### 测试导航器
> 在测试和实施文件之间快速导航。

![Test Navigator Demo](https://github.com/DFreds/test-navigator-atom/blob/master/test-navigator.gif?raw=true)

#### 主题
> 从您最喜欢的颜色生成 Atom 语法/UI 主题包（以及其他工具的匹配主题）。

#### 切换引号
> 在单引号和双引号之间快速切换。

#### 树视图搜索栏
> 在树视图中快速查看。
