# 很棒的乳胶 [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[![LaTeX Logo](https://upload.wikimedia.org/wikipedia/commons/thumb/9/92/LaTeX_logo.svg/220px-LaTeX_logo.svg.png)](https://www.latex-project.org/)

> 这是 [(La)TeX 排版系统](https://www.latex-project.org/) 的精彩内容的精选列表。

## 内容

<!-- TOC depthFrom:2 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [很棒的乳胶  ](#awesome-latex--)
  - [Contents](#contents)
  - [学习 LaTeX](#learning-latex)
  - [Distributions](#distributions)
  - [Docker 镜像](#docker-images)
  - [Engines](#engines)
    - [网络上的 LaTeX 公式](#latex-formulas-on-the-web)
  - [Editors](#editors)
    - [LaTeX-focused](#latex-focused)
    - [通用文本编辑器](#general-purpose-text-editors)
    - [在线编辑](#online-editors)
  - [参考书目工具](#bibliography-tools)
  - [构建工具](#build-tools)
    - [GitHub 操作](#github-actions)
  - [杂项。工具](#misc-tools)
    - [质量检查工具](#quality-check-tools)
    - [以方程为中心的工具](#tools-centered-around-equations)
  - [兼容 LaTeX 的 GUI 工具](#latex-compatible-gui-tools)
  - [Packages](#packages)
    - [References](#references)
    - [Tables](#tables)
    - [Graphics](#graphics)
      - [PSTricks](#pstricks)
      - [TikZ](#tikz)
    - [源代码](#source-code)
    - [Typography](#typography)
    - [演示文稿、幻灯片](#presentations-slides)
  - [Templates](#templates)
  - [Symbols](#symbols)
  - [Resources](#resources)
  - [Showcases](#showcases)
  - [Tutorials](#tutorials)
  - [Books](#books)
  - [Blogs](#blogs)
  - [社交媒体](#social-media)
  - [Meta Awesome-LaTeX](#meta-awesome-latex)
  - [Legend](#legend)

<!-- /TOC -->

## 学习 LaTeX

指导如何学习 LaTeX


## 发行版

- [MacTeX](https://tug.org/mactex/) - macOS 最常见的 LaTeX 发行版，基本上是 TeXLive，并添加了一些 Mac 专用工具。 ![麦克]
- [TeX Live](https://www.tug.org/texlive/) - 适用于类 Unix 操作系统（包括 GNU/Linux）的最常见 LaTeX 发行版。也适用于 Windows。 ![Linux] ![Windows]
- [MikTeX](https://miktex.org) - 最常见的适用于 Windows 的 LaTeX 发行版，但也适用于 Mac、Linux 或作为 Docker 映像。  ![linux] ![windows] ![mac] ![foss]

## Docker 镜像

当您的目标是无需安装即可运行的 LaTeX 环境时，Docker 镜像可能是您的选择。

- [reitzig/texlive-docker](https://github.com/reitzig/texlive-docker) - 具有软件包安装可能性的最小 TeXLive 系统
- [Island of TeX/texlive](https://gitlab.com/islandoftex/images/texlive) - 基于 debian 的完整 TeXLive 系统
- [dante-ev/docker-texlive](https://github.com/dante-ev/docker-texlive) - 基于 debian 的完整 TeXLive 系统，添加了预装的 pandoc、perl 和 python

## 发动机

- [pdfTeX](https://www.tug.org/applications/pdftex/) - TeX 编译器可以立即生成 PDF 文件而不是 DVI 文件（现在，这是许多用户的标准编译器）。 ![开源]
- [XeTeX](http://xetex.sourceforge.net) - TeX 编译器提供比 TeX/pdfTeX 更好的 unicode 和字体支持（即您可以使用操作系统的字体而不仅仅是 TeX 字体）。 ![开源]
- [LuaTeX](https://www.luatex.org) - (La)TeX 编译器支持用于脚本编写的 Lua 代码，并且比标准 TeX/pdfTeX 改进了 unicode 和字体支持。 ![开源]
- [tectonic](https://tectonic-typesetting.GitHub.io/en-US/) - 由 XeTeX 和 TeXLive 提供支持的现代独立 (La)TeX 编译器。 ![开源]

### 网络上的 LaTeX 公式

- [Auto-LaTeX Equations with Google Docs](https://sites.google.com/site/autolatexequations) - 直接在 Google 文档中呈现高质量的数学方程。
- [MathJaX](https://www.mathjax.org) - JavaScript 引擎在网络上呈现数学公式。结果看起来真的很顺利。 ![开源]
- [mimeTeX](https://ctan.org/pkg/mimetex) - mimeTeX 是一个相当古老的工具，可以将 LaTeX 公式渲染为网站的 PNG 图形，而实际上不需要在服务器上安装 LaTeX。 ![开源]
- [mathTeX](https://ctan.org/pkg/mathtex) - mathTeX 是 mimeTeX 的后继者：它可以生成更漂亮的图像，但需要在服务器上安装 LaTeX。 ![开源]
- [KaTeX](https://khan.GitHub.io/KaTeX/) - KaTeX 是可汗学院制作的数学渲染库，专注于快速加载时间。所有输出都被处理为纯 HTML，而不是固定图像。 ![开源]
- [Franklin.jl](https://franklinjl.org/) - Julia 中的静态站点生成器，具有 KaTeX 支持、代码评估、类似 LaTeX 的命令和可选的预渲染。 ![开源]
- [xhub](https://github.com/nschloe/xhub) - 允许您在 GitHub 页面中使用 LaTeX 的浏览器扩展。 ![开源]

## 编辑

因为用记事本编辑 LaTeX 代码并不好。
那里有很多编辑器，以下是最棒的编辑器。
LaTeX 编辑器的完整列表在 [tex.stackexchange.com](https://tex.stackexchange.com/) 上收集为 [LaTeX 编辑器/IDE 的大列表](https://tex.stackexchange.com/q/339/9075)。

- [List of popular LaTeX editors](https://tex.stackexchange.com/questions/339/latex-editors-ides) - 社区维护的流行 LaTeX 编辑器列表，包括屏幕截图和简短说明。

### 以 LaTeX 为中心

一些最出色的 LaTeX 编辑器就是这样做的：编辑 LaTeX。

- [Kile](https://kile.sourceforge.io) - 伟大的 LaTeX 编辑器最初来自 Linux/KDE 社区。它在 Windows 和 macOS 上也运行良好。 ![开源]
- [TeXMaker](https://www.xm1math.net/texmaker/) - 相当不错的 Kile 替代品。
- [TeXStudio](https://www.texstudio.org) - 源自 TeXMaker 的跨平台 LaTeX 编辑器。
- [WinEdt](https://www.winedt.com) - 许多人都信赖的 LaTeX 编辑器。仅适用于！[Windows]。
- [TeXnicCenter](https://www.texniccenter.org) - 相当古老但免费且不错的 LaTeX 编辑器。 ![窗口]
- [LyX](https://www.lyx.org) - 跨平台所见即所得编辑器，在幕后使用 LaTeX 来渲染文档。 ![开源]
- [TeXShop](https://pages.uoregon.edu/koch/texshop/) - MacTeX 中包含的 LaTeX 文档的严肃编辑器。 ![麦克]
- [TeXWorks](https://www.tug.org/texworks/) - 这是一款实用的 LaTeX 代码编辑器，以 TeXShop 为蓝本，但它是跨平台的。 ![开源]
- [BakomaTex](https://www.bakoma-tex.com) - 商业 LaTeX 编辑器允许使用其源代码和所见即所得编辑文档。
- [Texifier](https://www.texifier.com/) - 适用于 macOS 和 iOS 的商业 LaTeX 编辑器，具有出色的功能（文档概述、同步 PDF 显示、自动完成、跨设备同步等），永远不会妨碍写作。 ![麦克]

### 通用文本编辑器

这些编辑器不是只会一招的小马：当然，他们编辑 LaTeX，但他们可以做更多的事情！

- [Atom](https://atom.io) [![Atom][awesome]](https://github.com/mehcode/awesome-atom) ![foss]
  - [LaTeXTools](https://atom.io/packages/latextools) - 同名 Sublime Text 包的 Atom 端口。 ![开源]

- [Sublime Text](https://www.sublimetext.com) [![Sublime Text][awesome]](https://github.com/dreikanter/sublime-bookmarks)
  - [LaTeXing](https://github.com/LaTeXing/LaTeXing) - 用于编辑 LaTeX 的免费插件。 ![开源]
  - [LaTeXTools](https://github.com/SublimeText/LaTeXTools) - Sublime Text 的免费 LaTeX 插件。 ![开源]

- [Emacs](https://www.gnu.org/software/emacs/) [![Emacs][awesome]](https://github.com/emacs-tw/awesome-emacs) ![foss]
  - [AucTeX](https://www.gnu.org/software/auctex/) - LaTeX 的 Emacs 插件，还可以显示方程和图形的预览。 ![开源]
  - [RefTeX](https://www.gnu.org/software/auctex/reftex) - LaTeX 的 Emacs 插件添加了对标签、参考文献和引文的支持。 ![开源]

- [Vim](https://www.vim.org) [![Vim][awesome]](https://github.com/mhinz/vim-galore) ![foss]
- [Vim-LaTeX](http://vim-latex.sourceforge.net) ![foss]
  - [LaTeX Live Preview](https://github.com/xuhdev/vim-latex-live-preview) - 立即预览您的 LaTeX 文档。 ![开源]
  - [vimtex](https://github.com/lervag/vimtex) - 用于编辑 LaTeX 文件的现代 vim 插件。具有多种功能，包括实时预览和向前搜索。 ![开源]

- [IntelliJ](https://www.jetbrains.com/idea/)
  - [TeXiFy-IDEA](https://github.com/Hannah-Sten/TeXiFy-IDEA) - IntelliJ IDEA 的免费 LaTeX 插件。 ![开源]

- [VS Code](https://code.visualstudio.com/) [![VS Code][awesome]](https://github.com/viatsko/awesome-vscode) ![foss]
  - [LaTeX Workshop](https://github.com/James-Yu/LaTeX-Workshop) - Visual Studio Code 的 LaTeX 扩展！[foss]
  - [LTeX](https://marketplace.visualstudio.com/items?itemName=valentjn.vscode-ltex) - LanguageTool 语法/拼写检查！[foss]
  - [a-nau/latex-devcontainer](https://github.com/a-nau/latex-devcontainer) - Devcontainer 设置可轻松使用 LaTeX，无需本地安装！[foss]

### 在线编辑

在线编辑器可让您协作编辑文档。

- [List of popular online LaTeX editors](https://tex.stackexchange.com/questions/3/compiling-documents-online/1654#1654) - 社区维护的流行在线 LaTeX 编辑器列表，包括方程编辑器。
- [Authorea](https://www.authorea.com) - 具有内置 git 支持和参考书目工具的在线编辑器。
- [OpenAI Prism](https://prism.openai.com) - 具有实时协作功能的在线编辑器。
- [Modern LaTeX Editor](https://github.com/InMDev/Modern-LaTeX-Editor) - 在线编辑器，无需注册的混合代码编辑器 + 可视化编辑器，将 Notion/Google 文档/Microsoft Word 类编辑与原始 LaTeX 代码块混合在一起。
- [Octree](https://www.useoctree.com) - 具有人工智能写作辅助的在线编辑器。
- [Overleaf](https://www.overleaf.com) - 在线编辑器，还具有所见即所得编辑器和 git 支持。
  - [olcli](https://github.com/aloth/olcli) - Overleaf 的命令行界面可从终端同步、管理和编译项目。 ![开源]
- [SciTeX Cloud](https://github.com/ywatanabe1989/scitex-cloud) - 自托管在线编辑器，具有 AI 助手集成、图形/表格/引文管理、实时协作和 MCP 服务器（29 种工具）。 ![开源]
- [WebLaTeX](https://github.com/sanjib-sen/weblatex) - 基于 Web 的 vscode，具有 Git 集成 + Copilot + 语法和拼写检查器 + 基于 GitHub Codespace 和 Dev 容器的实时协作支持。
- [Papeeria](https://papeeria.com) - 具有内置 git 支持的在线编辑器。
- [JaxEdit](https://zohooo.GitHub.io/jaxedit/) - 在线 LaTeX 编辑器，具有实时预览和精美的演示模式。
- [Vexlio](https://vexlio.com/) - 在线图表编辑器，内置 LaTeX 方程支持，包括实时预览和轻松导出。
- [TeXbrain](https://tex.swimmingbrain.dev) - 基于浏览器的免费开源 LaTeX 编辑器，具有浏览器内编译、实时 PDF 预览和 Git 集成。无需帐户或安装。 ![开源]

## 参考书目工具

- [JabRef](https://www.jabref.org) - 非常强大的跨平台（Java）bibtex 编辑器。 ![mac] ![windows] ![linux] ![foss]
- [Papis](https://github.com/papis/papis) - 极其可定制，
强大而简单的跨平台（Python）库管理器。它有一个非常
完整的命令行界面、多个 GUI 和脚本编写功能。
![linux] ![mac] ![foss]
- [Bibdesk](http://bibdesk.sourceforge.net) - 很棒的参考书目编辑器！[mac]。
- [Zotero](https://www.zotero.org) - 浏览器的参考管理器，还可以导出到 bibtex 并与许多 LaTeX 编辑器集成。 ![mac] ![windows] ![linux] ![foss]
- [Mendeley](https://www.mendeley.com) - 用于管理您的参考资料和 PDF 的应用程序和云客户端。可以同步到您的 LaTeX 工作流程的 bibtex 文件。 ![mac] ![windows] ![linux]
- [betterbib](https://github.com/nschloe/betterbib) - 用于改进 BibTeX 文件的命令行实用程序。从在线资源获取信息。 ![mac] ![windows] ![linux] ![foss]
- [OneCite](https://github.com/HzaCode/OneCite) - 通用引文管理和学术参考工具包，可将杂乱的参考文献转换为格式完美的引文。支持 DOI、arXiv ID、标题等，并以 BibTeX、APA 和 MLA 格式输出。 ![mac] ![windows] ![linux] ![foss]
- [CrossRef Local](https://github.com/ywatanabe1989/crossref-local) - 本地 CrossRef 数据库（1.67 亿篇论文），具有全文搜索、影响因子数据、用于参考书目丰富的 Python API 和 MCP 服务器（15 个工具）。 ![开源]
- [OpenAlex Local](https://github.com/ywatanabe1989/openalex-local) - 本地 OpenAlex 数据库（284M 学术著作），具有用于文献发现的摘要和语义搜索，以及 MCP 服务器。 ![开源]

## 构建工具

编译 LaTeX 文档可能很乏味，构建工具可以帮助您管理编译过程。

- [Arara](https://www.ctan.org/pkg/arara) ([GitHub repo](https://github.com/islandoftex/arara)) - 简单的工具，允许您指定在文档中调用哪些工具，并且可以很容易地扩展。 ![开源]
- [latexmk](https://www.ctan.org/pkg/latexmk) - 许多 LaTeX 编辑器（LaTeXing、TeXShop 等）常用的构建工具来构建 LaTeX 文件。 ![开源]

### GitHub 操作

- [xu-cheng/latex-action](https://github.com/xu-cheng/latex-action) - GitHub Action 编译 LaTeX 文档
- [dante-ev/latex-action](https://github.com/dante-ev/latex-action) - DANTE e.V. 用于编译 LaTeX 文档的 GitHub 操作。提供完整的 TeXLive 以及预安装的 perl 和 python。

## 杂项。工具

- [CaTeX](https://github.com/Alexis-benoist/CaTeX) - 连接 LaTeX 文档，注意正确合并序言。
- [Pandoc](https://pandoc.org) - 该程序将几乎任何文档格式（LaTeX、DOC、Markdown 等）转换为几乎任何其他格式。一个很好的工具，可以帮助使用多种格式的工作流程。 ![开源]
- [SciTeX Writer](https://github.com/ywatanabe1989/scitex-writer) - 稿件编译系统，包含稿件、修订和补充材料模板，以及图形、表格和引文处理，以及 MCP 服务器（38 个工具）。 ![开源]

### 质量检查工具

- [ChkTeX](https://www.nongnu.org/chktex/) - LaTeX 文档的 Linter / 代码检查器。 ![开源]
- [blacktex](https://github.com/nschloe/blacktex) - 命令行工具，可替换常见的 LaTeX 反模式并清理文件。 ![windows] ![linux] ![mac] ![foss]
- [TeXtidote](https://github.com/sylvainhalle/textidote) - LaTeX 文档的跨平台 (Java) 拼写、语法和样式检查器。 ![windows] ![linux] ![mac] ![foss]

### 以方程为中心的工具

- [Codecogs Eqn Editor](https://editor.codecogs.com/) - 在线 LaTeX 方程编辑器，可让您生成包含方程的图形。
- [EqualX](https://equalx.sourceforge.io/) - 图形化 LaTeX 公式编辑器。 ![windows] ![linux] ![foss]
- [KLaTeXFormula](https://klatexformula.sourceforge.io) - LaTeXit 的跨平台替代品。 ![开源]
- [Laeqed](https://www.thrysoee.dk/laeqed/) - 跨平台 LaTeX 公式到 PNG 转换器。 ![windows] ![linux] ![mac] ![foss]
- [LaTeXEqEdit](http://latexeqedit.sourceforge.net/) - 适用于 Windows 的 LaTeX 公式编辑器。 ![窗户] ![福斯]
- [LaTeXiT](https://www.chachatelier.fr/latexit/) - LaTeXit 是一个方程编辑器，可以轻松地将渲染的方程（如 PDF、PNG 等）拖放到 Mac 上的非 LaTeX 文档中。 ![麦克]
- [LaTeX to Image](https://thomasahle.com/latex2png/) - 将 LaTeX 转换为 PNG、JPEG 或 SVG 图像。大符号菜单和简单的拖放方程。
- [pix2tex](https://lukas-blecher.github.io/LaTeX-OCR/) - LaTeX OCR ![windows] ![linux] ![mac] ![foss]
- [Image to LaTeX](https://www.underleaf.ai/tools/image-to-latex) - 由人工智能驱动的转换器，可将手写笔记、方程式或表格的图像转换为干净的 LaTeX 代码。

## 兼容 LaTeX 的 GUI 工具

- [TikzEdt](https://www.tikzedt.org)（也：[GitHub 存储库](https://github.com/hchapman/tikzedt)） - TikZ 图片的所见即所得和基于文本的编辑器。 ![开源]
- [TikZ-Editor](https://github.com/fredokun/TikZ-Editor) - TikZ 人物的实时预览编辑器。 ![mac] ![linux] ![foss]
- [IPE](https://ipe.otfried.org) - 与 LaTeX 命令和文档完美集成的绘图工具。 ![开源]
- [GeoGebra](https://www.geogebra.org/) - 跨平台几何工具，输出到 TikZ。 ![开源]
- [Dia](https://wiki.gnome.org/Apps/Dia) - 跨平台图表工具，可以导出到 PSTricks 和 MetaPost 代码。 ![开源]
- [TikZiT](https://tikzit.GitHub.io) - 用于使用 PGF/TikZ 创建图形和字符串图的 GUI 工具。 ![windows] ![linux] ![mac] ![foss]
- [LaTeXDraw](https://latexdraw.sourceforge.net/) - 基于矢量的绘图工具，以 LaTeX 为一等公民。 ![windows] ![linux] ![mac] ![foss]

## 套餐

- [CTAN](https://www.ctan.org) - 综合 TeX 存档网络是寻找有用的软件包和文档的地方。

### 参考文献

- [Cross-reference packages explained](https://tex.stackexchange.com/a/36312/9075) - 详细阐述交叉引用包（cleveref、varioref、theoremref、nameref 等）：使用哪个，哪个冲突？

### 表格

- [Excel2LaTeX](https://www.ctan.org/pkg/excel2latex?lang=en) - Excel（2010 及更早版本）宏用于生成 LaTeX“表格”代码。 ![Windows] ![Mac]
- [csv2latex](http://freshmeat.sourceforge.net/projects/csv2latex) - 将 CSV 文件从您喜爱的程序转换为 LaTeX“表格”文件。 ![linux] ![mac]
- [Tables Generator](https://www.tablesgenerator.com) - 该网站提供了一个图形界面来输入表格并为 LaTeX、Markdown、HTML 等生成格式正确的代码。
- [pgfplotstable](https://www.ctan.org/pkg/pgfplotstable?lang=en) - 该软件包以各种显示格式显示四舍五入到所需精度的数值表。它甚至可以读取 CSV 文件并直接包含在您的 LaTeX 文档中。

### 图形

#### PST技巧

PSTricks 是一个很棒的库，可以绘制包含在 PostScript/DVI 文件中的图形。

#### 蒂克兹

TikZ 是一个非常棒的软件包，其中包含许多插件，可让您从 LaTeX 文档中创建图形。
通常，使用“pdflatex”比使用 PSTricks 更容易。

- [TeXample](https://www.texample.net) - 关于 LaTeX 的博客，其中包含大量 TikZ 人物。
- [pgfplots](http://pgfplots.sourceforge.net) - 真正很棒的绘图库，位于 TikZ/pgf 之上并采用 TikZ/pgf 风格。该库可以加载 CSV 数据文件、执行一些计算并创建漂亮的绘图。
- [A very minimal introduction to TikZ (PDF)](https://cremeronline.com/LaTeX/minimaltikz.pdf) - TikZ 世界的简短介绍性文档，由 Jacques Crémer 撰写。
- [PetarV-/TikZ](https://github.com/PetarV-/TikZ) - Petar Veličković 收集的可供出版的 PGF/TikZ 人物。
- [matlab2tikz](https://github.com/matlab2tikz/matlab2tikz) - 将 MATLAB 绘图转换为 PGFPlots/TikZ。 ![windows] ![linux] ![mac] ![foss]
- [tikzplotlib](https://github.com/nschloe/tikzplotlib) - 将您的 matplotlib 图转换为 PGFPlots/TikZ。 ![windows] ![linux] ![mac] ![foss]
- [TikZBlog](https://latexdraw.com) - 关于如何在 LaTeX 中绘制插图的分步教程。

### 源代码

- [minted](https://www.ctan.org/pkg/minted) - minted 包使用 [pygments](https://pygments.org/) 生成列表。通过这种方式，LaTeX 能够格式化 300 多种编程和标记语言以及其他文本格式。

### 版式

- [microtype](https://ctan.org/pkg/microtype) - 该软件包通过启用边距字距调整和字体扩展来改善文档的外观。

### 演示文稿、幻灯片

- [nics](https://nics.nilcons.com/) - 这是 Beamer 的一个固执己见的替代方案，我们创建它的目的是让常见任务变得非常简单，并且默认情况下呈现精美。  有很棒的文档和详细的备忘单来帮助您入门。

## 模板

- [LaTeX templates](https://www.latextemplates.com) - 用于 LaTeX 的论文、海报、简历、论文、书籍、演示文稿等模板的集合。
- [Ultimate Beamer Theme List](https://github.com/martinbjeldbak/ultimate-beamer-theme-list) - 链接到各种投影仪主题以及 PDF 预览。
- [LaTeX Beamer Theme Overview](https://github.com/UweZiegenhagen/LaTeX-Beamer-Theme-Overview/blob/main/OVERVIEW.md) - TeXLive 中包含的 Beamer 主题的视觉概述
- [TeXtured](https://github.com/jdujava/TeXtured) - 排版优雅、干净且结构化的 LaTeX 模板（主要用于论文）。

## 符号

- [Comprehensive LaTeX symbol list](https://www.ctan.org/tex-archive/info/symbols/comprehensive/) - 非常广泛的 LaTeX 符号列表。提供 [A4](https://mirrors.ctan.org/info/symbols/compressive/symbols-a4.pdf) 和 [letter](https://mirrors.ctan.org/info/symbols/compressive/symbols-letter.pdf) 尺寸。
- [Detexify](https://detexify.kirelabs.org/classify.html) - 您绘制符号，此站点/应用程序将告诉您 LaTeX 命令。

## 资源

- [TUG](https://www.tug.org) - TeX 用户组是与其他 (La)TeX 用户联系的一种方式。
- [TeXDoc](https://texdoc.net) - “texdoc”实用程序的在线界面，用于浏览 LaTeX 包和文档。
- [Dickimaw Books: LaTeX resources](https://www.dickimaw-books.com/latexresources.html) - 对 LaTeX 有用的资源的精彩概述。
- [LaTeX cookbook](https://latex-cookbook.net) - TeXample 的兄弟姐妹，包含相当多的示例代码。
- [Visual FAQ](https://ctan.org/pkg/visualfaq) - 排版问题以及相应 TeX FAQ 答案的链接。
- [MartinThoma's LaTeX example](https://github.com/MartinThoma/LaTeX-examples/) - 包含示例 LaTeX 文档的 GitHub 存储库。
- [LaTeX community](https://latex.org/forum) - 关于 LaTeX 的论坛。
- 德语：[Neue TeX FAQ](https://texfragen.de) - 现代和更新的德语 LaTeX FAQ。
- [BibTeX Style Examples](http://www.cs.stir.ac.uk/~kjt/software/latex/showbst.html) - 常见 BibTeX 样式（BST 文件）的输出示例。
- [TeX World](https://tex.world/) - 由 TeX 用户组、DANTE 和 GUTenberg 支持的网站。
- [TeXnique](https://texnique.xyz) - 一款 LaTeX 排版游戏。

## 展示柜

- [Showcase of beautiful typography done in TeX & friends](https://tex.stackexchange.com/questions/1319/showcase-of-beautiful-typography-done-in-tex-friends) - 一组展示 LaTeX 强大功能的示例。
- [Showcase of beautiful invitations in TeX](https://tex.stackexchange.com/q/281415/9075) - 使用 LaTeX 排版的邀请函展示。
- [Showcase of "programming your document" paradigm](https://tex.stackexchange.com/q/219774/9075) - LaTeX 文档集合，演示如何像编程语言一样使用 LaTeX。
- [TUG: TeX showcase](https://www.tug.org/texshowcase/) - TUG 的网站展示了 LaTeX 功能的一些示例。
- [Awesome LaTeX drawing](https://github.com/xinychen/awesome-latex-drawing) - 使用 LaTeX 的学术绘图示例精选列表

## 教程

- [LearnLaTeX.org](https://www.learnlatex.org/) - 基于浏览器的 LaTeX 教程。
- [The (Not So) Short Introduction to LaTeX2e](https://mirrors.ctan.org/info/lshort/english/lshort.pdf) - 对 LaTeX 的非常全面的介绍。
- [Begin LaTeX in minutes](https://github.com/luong-komorebi/Begin-Latex-in-minutes) - 为初学者简要介绍 LaTeX，帮助您轻松使用 LaTeX。
- [Getting to Grips with LaTeX](https://www.andy-roberts.net/writing/latex) - 完整的指南，涵盖了您需要了解的有关 LaTeX 的大部分内容。
- [LaTeX introductions in languages other than English](https://tex.stackexchange.com/questions/84384/latex-introductions-in-languages-other-than-english/84385) - 多种语言的介绍集。

## 书籍

- [Wikibooks: LaTeX](https://en.wikibooks.org/wiki/LaTeX) - LaTeX 维基百科。不是真正的纸质书，但内容同样丰富。
- [《乳胶伴侣》，F. Mittelbach (2004)](https://www.informit.com/store/latex-companion-9780201362992)
- [LaTeX 图形伴侣，M. Goossens (2007)](https://www.informit.com/store/latex-graphics-companion-9780321508928)
- [TeX 按主题 (2007)](https://ctan.org/pkg/texbytopic)
- [不耐烦的 TeX (2020)](https://ctan.org/pkg/impatient)
- [Formatting Information (2020)](https://latex.silmaril.ie/formattinginformation) - 这是《*格式化信息 - 使用 LATEX 排版简介》* 的基于 HTML5 的在线版本。自 2000 年代初以来，它一直在不断更新。

## 博客

- [TeXblog](https://texblog.net) - 关于 LaTeX 和所有相关内容的博客。
- [texblog.org](https://texblog.org) - 有关 LaTeX 和相关主题（教程、包、代码片段等）的博客。
- [TeX Talk](https://tex-talk.net) - TeX Stack Exchange 网站的博客，包含新闻和采访。
- [TeX Hour](https://texhour.github.io/) - 每周一次视频会议

## 社交媒体

- [LinkedIn：TeX/LaTeX 用户组](https://www.linkedin.com/groups/1600297)
- [Twitter: @TeXtip](https://twitter.com/TeXtip) - [John D. Cook](https://www.johndcook.com/) 提供的与 (La)TeX 相关的提示。
- [TeX.StackExchange](https://tex.stackexchange.com) - StackExchange TeX 部分。
- [TopAnswers TeX](https://topanswers.xyz/tex) - 为 TeX 和朋友提供的免费开源问答网站

---

<!-- Icons -->

## Meta Awesome-LaTeX

如果您想做出贡献，请阅读我们的 [CONTRIBUTING](CONTRIBUTING.md) 指南。

## 传奇

当程序“仅”可用于这些平台时，会显示指示 Mac、Linux 和 Windows 兼容性的图标。因此，没有这些图标意味着该软件是完全跨平台的。

|       标志|描述 |
|:-------------------:|:-------------------------------------------------------|
| ！[mac] | [macOS](https://www.apple.com/macos) |
| ！[Linux] | [GNU/Linux](https://www.gnu.org) |
| ！[窗口] | [微软Windows](https://www.microsoft.com/windows) |
| ！[自由开源软件] | [免费开源软件](https://opensource.org) |

---

所有商标均为其各自所有者的财产。

[mac]：https://cdn.jsdelivr.net/gh/egeerardyn/awesome-LaTeX@700138fe725574e1741f148df6d1f77a8aa07eee/fig/apple.svg
[linux]：https://cdn.jsdelivr.net/gh/egeerardyn/awesome-LaTeX@700138fe725574e1741f148df6d1f77a8aa07eee/fig/linux.svg
[Windows]：https://cdn.jsdelivr.net/gh/egeerardyn/awesome-LaTeX@700138fe725574e1741f148df6d1f77a8aa07eee/fig/windows.svg
[foss]：https://cdn.jsdelivr.net/gh/egeerardyn/awesome-LaTeX@700138fe725574e1741f148df6d1f77a8aa07eee/fig/foss.svg
[真棒]：https://cdn.jsdelivr.net/gh/sindresorhus/awesome@d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg
