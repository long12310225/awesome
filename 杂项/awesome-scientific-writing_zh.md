# 很棒的科学写作 [![Awesome](https://awesome.re/badge-flat.svg)](https://github.com/sindresorhus/awesome)

> 科学写作可以超越 LaTeX，通过格式实现，
> 比如
> [Markdown](https://daringfireball.net/projects/markdown/)（及其多种风格），
> [reStructuredText](https://docutils.sourceforge.io/rst.html) 和
> [Jupyter 笔记本](https://jupyter.org/)。

:书签：意味着能够**无缝引用参考文献**。

:link: 意味着能够**交叉引用图中和部分
文件**。

## 内容

- [文字处理器](#word-processors)
- [Bibliography](#bibliography)
- [Illustrations](#illustrations)
- [转换器和滤波器](#converters-and-filters)
- [拼写检查和 Linting](#spell-checking-and-linting)
- [Templates](#templates)
  - [Articles](#articles)
  - [Books](#books)
- [Tutorials](#tutorials)
- [其他清单](#other-lists)

## 文字处理器

- [Marktext](https://github.com/marktext/marktext) - Markdown 文本编辑器。
- [R Studio](https://github.com/rstudio/rstudio) - R 的 IDE。
  - [bookdown](https://github.com/rstudio/bookdown) - R 包，方便用 R Markdown 编写书籍和长篇文章、报告：书签：：链接：。
  - [R Markdown](https://rmarkdown.rstudio.com/) - R 包将 R 写在 Markdown :bookmark: :link: 旁边。
- [Vim](https://www.vim.org/) - 命令行文本编辑器。
  - [fzf-bibtex](https://github.com/msprev/fzf-bibtex/#readme) - BibTeX 源
与使用 fzf（Go 中实现的模糊查找器）的 Vim 集成。
  - [vim-pandoc](https://github.com/vim-pandoc/vim-pandoc) - Pandoc 集成和 Vim 实用程序。
  - [vim-pandoc-syntax](https://github.com/vim-pandoc/vim-pandoc-syntax) - Vim 的 Pandoc 语法高亮显示。
- [Visual Studio Code](https://code.visualstudio.com/) - 支持 Markdown 的流行 IDE。
  - [Markdown All in One](https://github.com/yzhang-gh/vscode-markdown/#readme) - 增强型扩展
VSCode 中的 Markdown 支持，例如预览和自动完成等。
  - [Markdown Preview Enhanced](https://github.com/shd101wyy/markdown-preview-enhanced) - 潘多克
集成和实用程序。
- [Zettlr](https://www.zettlr.com/) - Markdown 编辑器有哪些
集成了CSL、BibLaTeX、Pandoc等众多工具
：书签：：链接：。

## 参考书目

参考管理器生成引文、BibTeX 和 BibLaTeX 文件。

- [Citation Style Language (CSL) styles](https://editor.citationstyles.org/) - 众包
存储库包含 9000 多种免费 CSL 引文样式和在线
编辑器来创建新的。
- [JabRef](https://www.jabref.org/) - 开源参考书目参考管理器。
- [Zotero](https://www.zotero.org/) - FOSS 工具，用于收集、组织、引用和
分享研究。
  - [Better BibTeX for Zotero](https://retorque.re/zotero-better-bibtex/) - 增强型
Zotero 的 BibTeX / BibLaTeX 集成。
- [ZoteroBib](https://zbib.org/) - 在线参考书目参考管理器。

## 插图

绘制插图本身已经让许多科学家发疯了。幸运的是，
有一些正式的语言可以用来创建漂亮的图形。

- [app.diagrams.net](https://app.diagrams.net/) - 开源、在线、桌面和
名为draw.io的容器可部署绘图软件。
- [graphviz](https://graphviz.org/) - 图形可视化软件
使用特定于域的 DOT 语言的网络。
- [Mermaid Live Editor](https://mermaid-js.github.io/mermaid-live-editor/) - 定义简单的图表而不是绘制它们。
- [Vega Lite](https://vega.github.io/vega-lite/examples/) - 定义图表和更复杂的图表。
- [PlantUML](https://plantuml.com/) - 定义 UML 图而不是绘制它们。

## 转换器和滤波器

补充文件和工具。

- [Cicero](https://cicero.xyz/) - 呈现 HTML 演示文稿的 Python 包
使用 remark 或 Reveal.js 从 Markdown 源中获取：link:。
- [docutils](https://docutils.sourceforge.io/docs/) - Python包可以
将reStructuredText转换为各种格式并提供命令行
执行此操作的工具：链接：。
- [Jupyter Book](https://jupyterbook.org/en/stable/) - 一个静态站点生成器，可以转换
将 CommonMark、MyST markdown 和 Jupyter 笔记本的集合集成到 HTML 网站中。
- [MyST](https://myst-parser.readthedocs.io/en/latest/) - 明显结构化的文本，
CommonMark markdown 的超集，具有类似 reStructuredText 的功能。
- [nbconvert](https://nbconvert.readthedocs.io/en/latest/) - 转换 Jupyter
将笔记本转换为 `reveal.js` 演示文稿、PDF、HTML、Markdown、
重构文本等等。
- [pandoc](https://pandoc.org/MANUAL) - 用于转换的 Haskell 库
将一种标记格式转换为另一种标记格式，以及使用此格式的命令行工具
图书馆：书签：：链接：。
  - [Pandoc filters](https://github.com/jgm/pandoc/wiki/Pandoc-Filters) - 名单
pandoc 的插件，它实现了额外的功能，例如引用和
交叉引用。
  - [Panflute](http://scorreia.com/software/panflute/) - Python式的替代品
约翰·麦克法兰的 pandocfilters。
- [Quarto](https://quarto.org) - 将 R Markdown 和 Jupyter Notebook 编译为 PDF、幻灯片和网站。支持 R、Python 和 Julia：书签：：链接：。

## 拼写检查和 Linting

- [GNU Aspell](http://aspell.net/) - 命令行拼写检查器。
- [Hunspell](http://hunspell.github.io/) - 命令行拼写检查器。
- [LanguageTool](https://languagetool.org/) - 开源语法、风格和
拼写检查器。
- [LanguageCheck](https://github.com/JohannesBuchner/languagecheck) - 分析科学 LaTeX 论文，从常见错误/歧义、时态一致性、a 与 an、拼写检查和段落主题句列表中提出改进建议。
- [Markdown lint tool](https://github.com/markdownlint/markdownlint) - Markdown 短绒。
- [proselint](https://github.com/amperser/proselint) - 用于散文的 Linter。
- [remarklint](https://github.com/remarkjs/remark-lint) - Markdown 短绒。
- [restructuredtext-lint](https://github.com/twolfson/restructuredtext-lint) - reStructuredText linter。
- [textlint](https://textlint.github.io/) - 用于文本的可插入 linting 工具
和降价。
- [textidote](https://sylvainhalle.github.io/textidote/) - 拼写、语法和
LaTeX 文档的样式检查。
- [Vale](https://github.com/errata-ai/vale) - 免费、开源的 linter
散文的构建考虑了速度和可扩展性。
- [write-good](https://github.com/btford/write-good) - 英语的 Naive linter
散文。

## 模板

可重用的简约示例。

### 文章

- [Paper Templates for GitHub Pages](https://github.com/dev-onejun/paper-templates-for-github-pages) - 基于 Markdown 的论文和简历/简历模板，通过 GitHub Pages 发布。

### 书籍

- [bookdown-demo](https://github.com/rstudio/bookdown-demo/#readme) - 最小
基于 R Markdown 和 bookdown 的书籍示例。
- [Eisvogel](https://github.com/Wandmalfarbe/pandoc-latex-template) - 干净的学术 pandoc LaTeX 模板。
- [撰写博士论文的模板
Markdown](https://github.com/tompollard/phd_thesis_markdown#readme) - 干净
组织文件，为撰写博士论文提供框架
主要是 Markdown 和一点点 LaTeX，并用 Pandoc 编译。

## 教程

如何出于科学目的生成文章和演示文稿。

- [3 frameworks into one — Write your next paper with R Studio!](https://blog.devgenius.io/write-your-whole-paper-in-r-it-is-better-77e1843f0c09) - 文章概述了结合 R Markdown（bookdown）、Zotero（文献管理）和 Notion（研究论文笔记）来撰写学术论文的工作流程。
- [Book on Riemann solvers](https://github.com/clawpack/riemann_book/#readme) - 这个
示例使用自定义“nbconvert”模板并展示如何存储您的
自动执行时没有输出（用于版本控制）的笔记本
在运行 `bookbook` 之前使用它们，以便 PDF 和 HTML 版本包括
输出。
- [Dennis Tenen and Grant Wythoff](https://programminghistorian.org/en/lessons/sustainable-authorship-in-plain-text-using-pandoc-and-markdown) - 使用 Pandoc 和 Markdown 实现纯文本的可持续作者身份。
- [Heads up! Quarto is here to stay. Immediately combine R & Python in your next document](https://blog.devgenius.io/heads-up-quarto-is-here-to-stay-aa861ef87491) - Quarto 的功能总结、为什么使用它以及它与 R Markdown 的比较。还包含针对 M1 Mac 用户如何解决网状结构常见问题的提示。
- [Write your dissertation in RMarkdown](https://ourcodingclub.github.io/tutorials/rmarkdown-dissertation/) - 创建复杂 PDF 文档的分步指南，包括文本、图形、参考文献、图像、格式等。
- [使用 Emacs 为 ACPD 撰写科学论文
Org-mode](https://www.draketo.de/english/emacs/writing-papers-in-org-mode-acpd) - 详细
通过与 LaTeX 无缝集成来撰写论文的教程
组织模式下的命令。

## 其他清单

- [很棒的 Jupyter](https://github.com/markusschanta/awesome-jupyter/#renderingpublishingconversion)
- [很棒的乳胶](https://github.com/egeerardyn/awesome-LaTeX/#readme)
- [很棒的降价](https://github.com/BubuAnabelas/awesome-markdown/#readme)
- [令人愉快的开放科学](https://codeberg.org/teaserbot-labs/delightful-open-science)

### 贡献

欢迎投稿！首先阅读[贡献指南](CONTRIBUTING.md)。
