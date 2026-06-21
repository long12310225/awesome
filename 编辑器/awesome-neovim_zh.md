# 很棒的 Neovim [![Awesome](https://awesome.re/badge-flat.svg)](https://awesome.re)

<a href="https://neovim.io/"><img src="https://neovim.io/logos/neovim-mark-flat.png" align="right" width="144"/></a>

> 一系列很棒的 Neovim 插件。主要针对 Neovim 特定功能。
> 这意味着此处未列出与 Vim 兼容的插件。

[Neovim](https://neovim.io/) 是一个基于 Vim 的文本编辑器，旨在实现可扩展性和可用性，以鼓励新的应用程序和贡献。
它有一些[内置插件](https://neovim.io/doc/user/plugins.html#plugins) 以及丰富的 API，可供开发更多插件。

## 内容

- [插件管理器](#plugin-manager)
- [LSP](#lsp)
  - [Diagnostics](#diagnostics)
- [Completion](#completion)
- [AI](#ai)
- [编程语言支持](#programming-languages-support)
  - [Golang](#golang)
  - [网页开发](#web-development)
  - [Markdown 和 LaTeX](#markdown-and-latex)
- [Language](#language)
- [Syntax](#syntax)
- [Snippet](#snippet)
- [Register](#register)
- [Marks](#marks)
- [Search](#search)
- [模糊查找器](#fuzzy-finder)
- [文件浏览器](#file-explorer)
- [Project](#project)
- [Buffers](#buffers)
- [Color](#color)
- [Colorscheme](#colorscheme)
  - [配色方案创建](#colorscheme-creation)
  - [配色方案切换器](#colorscheme-switchers)
- [条形图和线形图](#bars-and-lines)
  - [Statusline](#statusline)
  - [Tabline](#tabline)
  - [Cursorline](#cursorline)
- [Startup](#startup)
- [Icon](#icon)
- [Media](#media)
- [做笔记](#note-taking)
- [Utility](#utility)
  - [CSV 文件](#csv-files)
- [Animation](#animation)
- [终端集成](#terminal-integration)
- [Debugging](#debugging)
  - [Quickfix](#quickfix)
- [Test](#test)
- [代码运行者](#code-runner)
- [Neovim Lua 开发](#neovim-lua-development)
- [Fennel](#fennel)
- [依赖管理](#dependency-management)
- [Git](#git)
  - [GitHub](#github)
- [Motion](#motion)
  - [基于护树者](#tree-sitter-based)
- [Keybinding](#keybinding)
- [Scrolling](#scrolling)
  - [Scrollbar](#scrollbar)
- [编辑支持](#editing-support)
  - [Comment](#comment)
  - [Folding](#folding)
- [Formatting](#formatting)
  - [Indent](#indent)
- [命令行](#command-line)
- [Session](#session)
- [远程开发](#remote-development)
- [实时预览](#live-preview)
- [分割和窗口](#split-and-window)
  - [Tmux](#tmux)
- [Game](#game)
  - [竞争性编程](#competitive-programming)
- [Toys](#toys)
- [Workflow](#workflow)
  - [统计追踪](#stats-tracking)
- [Database](#database)
- [预制配置](#pre-made-configuration)
- [External](#external)
  - [版本管理器](#version-manager)
  - [插件模板](#plugin-template)
  - [OS-specific](#os-specific)
- [Wishlist](#wishlist)
- [UI](#ui)
- [Resource](#resource)

## 插件管理器

- [alyxshang/nuwa.nvim](https://source.alyxshang.boo/alyxshang/nuwa.nvim) - 一个轻量级的包管理器。
- [lewis6991/pckr.nvim](https://github.com/lewis6991/pckr.nvim) - `wbthomason/packer.nvim` 的精神继承者。
- [savq/paq-nvim](https://github.com/savq/paq-nvim) - 用 Lua 编写的包管理器。
<!--lint disable double-link -->
- [NTBBloodbath/cheovim](https://github.com/NTBBloodbath/cheovim) - 用 Lua 编写的配置切换器。受到 [chemacs](https://github.com/plexus/chemacs) 的启发。
<!--lint enable double-link -->
- [folke/lazy.nvim](https://github.com/folke/lazy.nvim) - 一个现代的插件管理器，具有图形界面、异步执行、锁定文件等。
  - [cosmicbuffalo/super_lazy.nvim](https://github.com/cosmicbuffalo/super_lazy.nvim) - “folke”的“lazy.nvim”的扩展，允许想要组合共享/个人 Neovim 配置的大型团队使用多个锁定文件。
- [alex-popov-tech/store.nvim](https://github.com/alex-popov-tech/store.nvim) - 插件发现工具，具有每小时更新的数据库，以及“lazy.nvim”和“vim.pack”的一键安装。
- [lumen-oss/rocks.nvim](https://github.com/lumen-oss/rocks.nvim) - 受 Cargo 启发，使用 LuaRocks 进行插件管理的现代方法。
- [nvim-mini/mini.nvim#mini.deps](https://github.com/nvim-mini/mini.nvim/blob/main/readmes/mini-deps.md) - 用于管理其他插件的“mini.nvim”模块。使用 Git 和内置包来安装、更新、清理和快照插件。
- [wsdjeg/nvim-plug](https://github.com/wsdjeg/nvim-plug) - 用 Lua 编写的异步插件管理器。
- [piersolenski/plugin-addict.nvim](https://github.com/piersolenski/plugin-addict.nvim) - 一种快速安装插件的简单方法。
- [OriginCoderPulse/synapse.nvim](https://github.com/OriginCoderPulse/synapse.nvim) - 一个现代的、轻量级的插件管理器，具有漂亮的 UI、智能依赖管理、标签/分支支持和安装后命令执行。
- [zuqini/zpack.nvim](https://github.com/zuqini/zpack.nvim) - `vim.pack` 之上的薄层，用于支持延迟加载和 `lazy.nvim` 的声明性规范。
<!--lint disable double-link -->
[**⬆ 回到顶部**](#contents)
<!--lint enable double-link -->

## LSP

**（需要 Neovim 0.5）**

- [romus204/referencer.nvim](https://github.com/romus204/referencer.nvim) - 轻量级异步，使用 LSP 显示对函数、方法、类型等的引用。
- [Dan7h3x/signup.nvim](https://github.com/Dan7h3x/signup.nvim) - 一个具有出色功能的智能“lsp_signature”助手。
<!--lint disable awesome-spell-check-->
- [neovim/nvim-lspconfig](https://github.com/neovim/nvim-lspconfig) - LSP客户端快速启动配置。
<!--lint enable awesome-spell-check-->
- [nvim-lua/lsp-status.nvim](https://github.com/nvim-lua/lsp-status.nvim) - 这是一个插件/库，用于从内置 LSP 客户端生成状态行组件。
- [nvimdev/lspsaga.nvim](https://github.com/nvimdev/lspsaga.nvim) - 一个基于内置 LSP 的轻量级 LSP 插件，具有高性能的 UI。
- [kosayoda/nvim-lightbulb](https://github.com/kosayoda/nvim-lightbulb) - 每当“textDocument/codeAction”在当前光标位置可用时，该插件就会在符号栏中显示一个灯泡。
- [onsails/lspkind.nvim](https://github.com/onsails/lspkind.nvim) - 该插件将类似 VSCode 的图标添加到 LSP 补全中。
- [ojroques/nvim-lspfuzzy](https://github.com/ojroques/nvim-lspfuzzy) - 一个让 LSP 客户端使用 FZF 的小插件。
- [gfanto/fzf-lsp.nvim](https://github.com/gfanto/fzf-lsp.nvim) - 为内置 LSP 启用 FZF 模糊搜索的功能。
- [ray-x/lsp_signature.nvim](https://github.com/ray-x/lsp_signature.nvim) - 键入时会有 LSP 签名提示。
- [smjonas/inc-rename.nvim](https://github.com/smjonas/inc-rename.nvim) - 基于命令预览功能，提供增量LSP重命名命令。
- [rmagatti/goto-preview](https://github.com/rmagatti/goto-preview) - 在浮动窗口中预览本机 LSP 的 goto 定义调用。
- [jubnzv/virtual-types.nvim](https://github.com/jubnzv/virtual-types.nvim) - 将类型注释显示为虚拟文本。
- [marilari88/twoslash-queries.nvim](https://github.com/marilari88/twoslash-queries.nvim) - 提供内联虚拟文本，显示检查变量的 TypeScript 类型。
- [retran/meow.yarn.nvim](https://github.com/retran/meow.yarn.nvim) - 交互式 LSP 类型和调用层次结构资源管理器，具有树视图、实时预览、导航面包屑和自定义节点渲染器。
- [ray-x/navigator.lua](https://github.com/ray-x/navigator.lua) - 快速学习现有代码并轻松浏览代码。一把瑞士军刀让探索 LSP 和 Tree-sitter 符号变得轻而易举。
- [hedyhli/outline.nvim](https://github.com/hedyhli/outline.nvim) - “symbols-outline.nvim” 的一个显着增强和重构的分支。
- [stevearc/aerial.nvim](https://github.com/stevearc/aerial.nvim) - 用于浏览和快速导航的代码大纲窗口。
- [SmiteshP/nvim-navbuddy](https://github.com/SmiteshP/nvim-navbuddy) - 一个简单的弹出显示，使用 LSP 提供类似导航功能的面包屑。
- [tamago324/nlsp-settings.nvim](https://github.com/tamago324/nlsp-settings.nvim) - 使用 JSON 或 YAML 文件设置 LSP。
- [jakewvincent/texmagic.nvim](https://github.com/jakewvincent/texmagic.nvim) - 通过定义任意数量的自定义 LaTeX 构建引擎并使用神奇注释选择它们，增强 Texlab 的 lspconfig 设置。
- [aznhe21/actions-preview.nvim](https://github.com/aznhe21/actions-preview.nvim) - LSP 代码操作的完全可定制预览器。
- [mfussenegger/nvim-lint](https://github.com/mfussenegger/nvim-lint) - 异步 linter 插件，对内置语言服务器协议支持的补充。
- [b0o/SchemaStore.nvim](https://github.com/b0o/SchemaStore.nvim) - 提供对 [SchemaStore](https://github.com/SchemaStore/schemastore) 目录的访问。
- [j-hui/fidget.nvim](https://github.com/j-hui/fidget.nvim) - 用于 LSP 进度的独立 UI。
<!--lint disable double-link-->
- [scalameta/nvim-metals](https://github.com/scalameta/nvim-metals) - 使用内置 LSP 支持，在使用 Scala 语言服务器 [Metals](https://scalameta.org/metals/) 时提供更好的体验。
<!--lint enable double-link-->
- [junnplus/lsp-setup.nvim](https://github.com/junnplus/lsp-setup.nvim) - `nvim-lspconfig` 和 `mason-lspconfig` 的简单包装器，可轻松设置 LSP 服务器。
- [amrbashir/nvim-docs-view](https://github.com/amrbashir/nvim-docs-view) - 在侧面板中显示 LSP 悬停文档。
- [mfussenegger/nvim-jdtls](https://github.com/mfussenegger/nvim-jdtls) - 对 Eclipse JDT 语言服务器的内置 LSP 支持的扩展。
- [Kasama/nvim-custom-diagnostic-highlight](https://github.com/Kasama/nvim-custom-diagnostic-highlight) - 内联诊断弹出突出显示与“coc-nvim”非常相似，但基于“vim.diagnostic”。
- [mrcjkb/haskell-tools.nvim](https://github.com/mrcjkb/haskell-tools.nvim) - 无缝集成 Haskell 开发工具，如“haskell-language-server”和 Hoogle。
- [~chinmay/clangd_extensions.nvim](https://sr.ht/~chinmay/clangd_extensions.nvim) - 内置 LSP 客户端的不合规范的“clangd”功能。
- [ranjithshegde/ccls.nvim](https://github.com/ranjithshegde/ccls.nvim) - 使用 ccls LSP 的不合规格扩展并浏览 AST。
- [idanarye/nvim-buffls](https://github.com/idanarye/nvim-buffls) - 将 LSP 功能添加到特定缓冲区。
- [error311/wayfinder.nvim](https://github.com/error311/wayfinder.nvim) - 通过可保留的轨迹从当前符号引导代码探索。
- [DNLHC/glance.nvim](https://github.com/DNLHC/glance.nvim) - 用于预览、导航和编辑 LSP 位置的漂亮窗口。
- [linrongbin16/lsp-progress.nvim](https://github.com/linrongbin16/lsp-progress.nvim) - 高性能 LSP 进度状态。
- [jinzhongjia/LspUI.nvim](https://github.com/jinzhongjia/LspUI.nvim) - 包装 LSP 操作的现代且有用的 UI。
- [VidocqH/lsp-lens.nvim](https://github.com/VidocqH/lsp-lens.nvim) - 像 IDEA codelens 一样显示函数定义上方的函数引用。
- [chrisgrieser/nvim-dr-lsp](https://github.com/chrisgrieser/nvim-dr-lsp) - 状态行组件显示光标下令牌的 LSP 定义和引用的数量。
- [Wansmer/symbol-usage.nvim](https://github.com/Wansmer/symbol-usage.nvim) - 显示文档符号的引用、定义和实现。
- [creativenull/efmls-configs-nvim](https://github.com/creativenull/efmls-configs-nvim) - 为 efm-langserver 配置的非官方的 linter 和格式化程序集合，以便与内置 LSP 一起使用。
- [creativenull/diagnosticls-configs-nvim](https://github.com/creativenull/diagnosticls-configs-nvim) - 为诊断语言服务器配置的 linter 和格式化程序的非官方集合，以便与内置 LSP 一起使用。
- [hinell/lsp-timeout.nvim](https://github.com/hinell/lsp-timeout.nvim) - 自动启动/停止空闲/未使用的LSP服务器；保持较低的 RAM 使用率。
- [nvimtools/none-ls.nvim](https://github.com/nvimtools/none-ls.nvim) - Null-ls.nvim 重新加载/使用 Neovim 作为语言服务器通过 Lua 注入 LSP 诊断、代码操作等。
- [zeioth/none-ls-autoload.nvim](https://github.com/zeioth/none-ls-autoload.nvim) - 自动加载/自动卸载使用 mason 安装的 none-ls 源。它支持内置源和外部源。
- [vxpm/ferris.nvim](https://github.com/vxpm/ferris.nvim) - 与 Rust-Analyzer 的 LSP 扩展交互。
- [mrcjkb/rustaceanvim](https://github.com/mrcjkb/rustaceanvim) - 经过大量修改的 rust-tools.nvim 分支，不需要 `setup` 调用，也不依赖于 nvim-lspconfig。
- [soulis-1256/eagle.nvim](https://github.com/soulis-1256/eagle.nvim) - 鼠标悬停 LSP 提示。
- [stevanmilic/nvim-lspimport](https://github.com/stevanmilic/nvim-lspimport) - 自动解析未定义术语的导入。对于“pyright”语言服务器很有用。
- [jmbuhr/otter.nvim](https://github.com/jmbuhr/otter.nvim) - 为其他文档中嵌入的语言提供 LSP 功能和 nvim-cmp 补全源。
- [lopi-py/luau-lsp.nvim](https://github.com/lopi-py/luau-lsp.nvim) - 一个 luau-lsp 扩展来改善您的体验。
- [LukasPietzschmann/boo.nvim](https://github.com/LukasPietzschmann/boo.nvim) - 快速弹出一些由 LSP 支持的关于光标所在事物的信息。
- [zeioth/garbage-day.nvim](https://github.com/Zeioth/garbage-day.nvim) - 垃圾收集器，停止不活动的 LSP 客户端以释放 RAM。
- [ryan-WORK/ohm](https://github.com/ryan-WORK/ohm) - Neovim 的持久 LSP 进程管理器守护进程。修复了内存膨胀、诊断卡住、monorepo 服务器重复和会话降级。
- [rachartier/tiny-inline-diagnostic.nvim](https://github.com/rachartier/tiny-inline-diagnostic.nvim) - 显示更漂亮的诊断消息。在光标所在位置显示一行诊断消息，并带有图标和颜色。
- [chrisgrieser/nvim-lsp-endhints](https://github.com/chrisgrieser/nvim-lsp-endhints) - 在行尾显示 LSP 嵌入提示，而不是在行内。
- [rachartier/tiny-code-action.nvim](https://github.com/rachartier/tiny-code-action.nvim) - 提供了一种使用 Telescope 运行和可视化代码操作的简单方法。
- [mawkler/refjump.nvim](https://github.com/mawkler/refjump.nvim) - 使用 `]r`/`[r` 跳转到光标下项目的下一个/上一个 LSP 参考。
- [alexpasmantier/pymple.nvim](https://github.com/alexpasmantier/pymple.nvim) - 在文件移动/重命名时重构 Python 导入。
- [esmuellert/nvim-eslint](https://github.com/esmuellert/nvim-eslint) - 捆绑 VSCode ESLint 语言服务器并利用本机 LSP 客户端提供一体化 ESLint 体验。
- [Fildo7525/pretty_hover](https://github.com/Fildo7525/pretty_hover) - 高度可定制的悬停格式化程序，可扩展至blink.cmp。由于本机悬停支持多个 LSP 服务器。
- [yarospace/dev-tools.nvim](https://github.com/yarospace/dev-tools.nvim) - 用于自定义代码操作的进程内 LSP 服务器、增强的操作选择器、社区操作库以及用于创建您自己的操作的便捷界面。
- [SunnyTamang/neodoc.nvim](https://github.com/SunnyTamang/neodoc.nvim) - DocString 生成器，可帮助以“google”、“numpy”、“sphinx”等格式编写带有实时预览的函数/类文档字符串。
- [barreiroleo/ltex_extra.nvim](https://github.com/barreiroleo/ltex_extra.nvim) - LTeX LSP 扩展提供外部文件处理（规则和字典）。
- [chojs23/ts-bridge](https://github.com/chojs23/ts-bridge) - TypeScript 语言服务器 shim 将内置 LSP 客户端与“tsserver”桥接起来。
- [akioweh/lsp-document-highlight.nvim](https://github.com/akioweh/lsp-document-highlight.nvim) - 瞬时 LSP 符号参考在光标下突出显示。
- [nemanjamalesija/ts-expand-hover.nvim](https://github.com/nemanjamalesija/ts-expand-hover.nvim) - 逐步展开和折叠悬停浮动内的 TypeScript 类型别名。
- [mason-org/mason.nvim](https://github.com/mason-org/mason.nvim) - 轻松安装和管理 LSP 服务器、DAP 服务器、linter 和格式化程序。

### 诊断

- [sontungexpt/better-diagnostic-virtual-text](https://github.com/sontungexpt/better-diagnostic-virtual-text) - 增强诊断虚拟文本的显示。此功能旨在直接在编辑器中提供更加用户友好且信息丰富的诊断消息呈现。
- [~whynothugo/lsp_lines.nvim](https://git.sr.ht/~whynothugo/lsp_lines.nvim) - 使用真实代码行之上的虚拟行呈现诊断。
- [folke/trouble.nvim](https://github.com/folke/trouble.nvim) - 一个漂亮的诊断列表可以帮助您解决代码引起的所有问题。
- [piersolenski/wtf.nvim](https://github.com/piersolenski/wtf.nvim) - 人工智能驱动的诊断调试，有助于解释复杂的错误并提供定制的解决方案。
- [chrisgrieser/nvim-rulebook](https://github.com/chrisgrieser/nvim-rulebook) - 添加内联注释以忽略规则，或在线查找规则文档。
- [artemave/workspace-diagnostics.nvim](https://github.com/artemave/workspace-diagnostics.nvim) - 填充所有项目文件的诊断，而不仅仅是打开的文件。
- [Kurama622/clean-diagnostic](https://github.com/Kurama622/clean-diagnostic) - 使用虚拟文本显示诊断计数，并在浮动窗口中显示诊断详细信息。
<!--lint disable double-link -->
[**⬆ 回到顶部**](#contents)
<!--lint enable double-link -->

## 完成

- [ms-jpq/coq_nvim](https://github.com/ms-jpq/coq_nvim) - 快他妈的完成了。 SQLite，并发调度程序，数百小时的优化。
- [hrsh7th/nvim-cmp](https://github.com/hrsh7th/nvim-cmp) - 用 Lua 编写的补全引擎，“nvim-compe”的后继者。
  - [hrsh7th/cmp-cmdline](https://github.com/hrsh7th/cmp-cmdline) - 用于 cmdline 补全的 `nvim-cmp` 源。
  - [saadparwaiz1/cmp_luasnip](https://github.com/saadparwaiz1/cmp_luasnip) - “LuaSnip”的“nvim-cmp”源。
  - [hrsh7th/cmp-buffer](https://github.com/hrsh7th/cmp-buffer) - 缓冲区字的“nvim-cmp”源。
  - [hrsh7th/cmp-path](https://github.com/hrsh7th/cmp-path) - 文件系统路径的 `nvim-cmp` 源。
  - [hrsh7th/cmp-nvim-lsp](https://github.com/hrsh7th/cmp-nvim-lsp) - 内置 LSP 客户端的“nvim-cmp”源。
  - [hrsh7th/cmp-nvim-lsp-signature-help](https://github.com/hrsh7th/cmp-nvim-lsp-signature-help) - 用于显示来自 LSP 客户端的函数签名的“nvim-cmp”源。
  - [hrsh7th/cmp-nvim-lua](https://github.com/hrsh7th/cmp-nvim-lua) - Neovim Lua API 的 `nvim-cmp` 源代码。
  - [petertriho/cmp-git](https://github.com/petertriho/cmp-git) - “git”的“nvim-cmp”源。
  - [lukas-reineke/cmp-under-comparator](https://github.com/lukas-reineke/cmp-under-comparator) - `nvim-cmp` 函数可以更好地排序。
  - [SergioRibera/cmp-dotenv](https://github.com/SergioRibera/cmp-dotenv) - 环境变量的 `nvim-cmp` 源（来自系统和 `.env` 文件）。
- [nvim-mini/mini.nvim#mini.completion](https://github.com/nvim-mini/mini.nvim/blob/main/readmes/mini-completion.md) - 用于异步两阶段完成的“mini.nvim”模块。支持显示完成项信息和独立函数签名。
- [saghen/blink.cmp](https://github.com/saghen/blink.cmp) - 通过 LSP 和片段支持、签名帮助、命令行完成和自动括号支持（基于语义标记）实现真正快速的完成。
  - [saghen/blink.compat](https://github.com/saghen/blink.compat) - 在“blink.cmp”上使用“nvim-cmp”源的兼容层。
  - [Kasier-Yang/blink-cmp-avante](https://github.com/Kaiser-Yang/blink-cmp-avante) - Avante 的“blink-cmp”源。
  - [krissen/blink-cmp-bibtex](https://github.com/krissen/blink-cmp-bibtex) - BibTeX 引文文件的“blink.cmp”源。
  - [Kaiser-Yang/blink-cmp-git](https://github.com/Kaiser-Yang/blink-cmp-git) - Git 的 `blink.cmp` 源。
  - [disrupted/blink-cmp-conventional-commits](https://github.com/disrupted/blink-cmp-conventional-commits) - [常规提交](https://www.conventionalcommits.org/) 的 `blink.cmp` 源。
  - [mikavilpas/blink-ripgrep.nvim](https://github.com/mikavilpas/blink-ripgrep.nvim) - “ripgrep”/“git grep”的“blink.cmp”源。
  - [bydlw98/blink-cmp-env](https://github.com/bydlw98/blink-cmp-env) - `blink.cmp` 环境变量源。
  - [bydlw98/blink-cmp-sshconfig](https://github.com/bydlw98/blink-cmp-sshconfig) - “sshconfig”文件的“blink.cmp”源。
  - [mgalliou/blink-cmp-tmux](https://github.com/mgalliou/blink-cmp-tmux) - [tmux](https://github.com/tmux/tmux) 的 `blink.cmp` 源。
  - [moyiz/blink-emoji.nvim](https://github.com/moyiz/blink-emoji.nvim) - GitHub Markdown 表情符号的“blink.cmp”源。
  - [erooke/blink-cmp-latex](https://github.com/erooke/blink-cmp-latex) - LaTeX 的 `blink.cmp` 源。
  - [xieyonn/blink-cmp-dat-word](https://github.com/xieyonn/blink-cmp-dat-word) - `blink.cmp` 字典源。
  - [yaocccc/blink-cmp-cmdlinehistory](https://github.com/yaocccc/blink-cmp-cmdlinehistory) - cmdline 和搜索历史记录的 `blink.cmp` 源。
  - [FelipeLema/blink-cmp-vsnip](https://codeberg.org/FelipeLema/blink-cmp-vsnip) - `vim-vsnip` 的 `blink.cmp` 源。
  - [benborla/at-file.nvim](https://github.com/benborla/at-file.nvim) - 使用“@”完成文件路径的“blink.cmp”源。
- [zbirenbaum/copilot.lua](https://github.com/zbirenbaum/copilot.lua) - [GitHub/copilot.vim](https://github.com/github/copilot.vim) 的全功能 Lua 替代品。
- [brianaung/compl.nvim](https://github.com/brianaung/compl.nvim) - 构建在 Vim 的 ins-completion 机制之上的最小且无依赖的自动完成。
<!--lint disable double-link -->
[**⬆ 回到顶部**](#contents)
<!--lint enable double-link -->

## 人工智能

- [cursortab/cursortab.nvim](https://github.com/cursortab/cursortab.nvim) - 使用多个 AI 提供商编辑补全和光标预测。
- [carlos-algms/agentic.nvim](https://github.com/carlos-algms/agentic.nvim) - AI ACP 提供商（例如 Claude、Gemini、Codex、OpenCode 和 Cursor）的聊天界面。
- [BRONZowl/codux.nvim](https://github.com/BRONZowl/codux.nvim) - 在持久浮动终端中运行 OpenAI Codex 并发送文件、选择、诊断或文件资源管理器目标。
- [0xble/dotagent.nvim](https://github.com/0xble/dotagent.nvim) - Claude Code 和 Codex 风格的提示编辑器的命令和技能完成，可从本地代理命令和技能目录进行配置。
- [blob42/codegpt-ng.nvim](https://github.com/blob42/codegpt-ng.nvim) - 基于极简命令的人工智能编码，具有强大的模板系统。支持 Ollama、OpenAI 等。
- [ray-x/copilot-agent.nvim](https://github.com/ray-x/copilot-agent.nvim) - GitHub Copilot 代理运行时，具有本机工具执行、会话持久性和细粒度权限。
- [Aaronik/GPTModels.nvim](https://github.com/Aaronik/GPTModels.nvim) - GPTModels - 一个稳定、干净、多模型、基于窗口的 LLM AI 工具。
- [Robitx/gp.nvim](https://github.com/Robitx/gp.nvim) - ChatGPT 类似于您最喜欢的编辑器中的会话和可指导的文本/代码操作。
- [jackMort/ChatGPT.nvim](https://github.com/jackMort/ChatGPT.nvim) - 使用 OpenAI 的 ChatGPT API 轻松生成自然语言。
- [wsdjeg/chat.nvim](https://github.com/wsdjeg/chat.nvim) - 一个轻量级、可扩展的聊天插件，具有人工智能集成、多个提供商和内置工具。
- [CamdenClark/flyboy](https://github.com/CamdenClark/flyboy) - 在 Markdown 缓冲区中与 ChatGPT 进行简单交互。支持 GPT-4 和 Azure OpenAI。
- [gsuuon/model.nvim](https://github.com/gsuuon/model.nvim) - 通过提示生成器界面集成法学硕士。多提供商，包括 OpenAI（+ 兼容）、“PaLM”、“Hugging Face”以及“llamacpp”等本地引擎。
- [dense-analysis/neural](https://github.com/dense-analysis/neural) - 集成法学硕士以生成代码、与聊天机器人交互等。
- [jpmcb/nvim-llama](https://github.com/jpmcb/nvim-llama) - LLM（LLaMA 2 和 `llama.cpp`）包装器。
- [David-Kunz/gen.nvim](https://github.com/David-Kunz/gen.nvim) - 使用法学硕士（通过 Ollama）和可自定义提示生成文本。
- [kiddos/gemini.nvim](https://github.com/kiddos/gemini.nvim) - 绑定到 Google Gemini API。
- [olimorris/codecompanion.nvim](https://github.com/olimorris/codecompanion.nvim) - 副驾驶聊天般的体验，配有内联助手。支持 Anthropic、Gemini、Ollama 和 OpenAI。
- [you-n-g/simplegpt.nvim](https://github.com/you-n-g/simplegpt.nvim) - 提供一种简单而灵活的方式来构建问题并将其发送到 ChatGPT。
- [Exafunction/windsurf.nvim](https://github.com/Exafunction/windsurf.nvim) - 免费、超快的 Copilot 替代方案。支持 LSP 和 Tree-sitter。
- [GeorgesAlkhouri/nvim-aider](https://github.com/GeorgesAlkhouri/nvim-aider) - 无缝集成 Aider，提供人工智能辅助编码体验。
- [CopilotC-Nvim/CopilotChat.nvim](https://github.com/CopilotC-Nvim/CopilotChat.nvim) - GitHub Copilot 的聊天界面可让您直接询问与编码相关的问题并获得答案。
- [tzachar/cmp-ai](https://github.com/tzachar/cmp-ai) - 这是 nvim-cmp 的通用 AI 源，可轻松适应任何支持远程代码完成的 REST API。
- [milanglacier/minuet-ai.nvim](https://github.com/milanglacier/minuet-ai.nvim) - Minuet 提供来自 LLM 提供商的代码补全，包括 OpenAI（兼容）、Gemini、Claude、Ollama、Deepseek 等，并支持 nvim-cmp、blink.cmp 和虚拟文本前端。
- [yetone/avante.nvim](https://github.com/yetone/avante.nvim) - 与您的代码聊天，就像在 Cursor AI IDE 中一样。
- [Kurama622/llm.nvim](https://github.com/Kurama622/llm.nvim) - 免费的大语言模型 (LLM) 支持，提供与 LLM 交互的命令。
- [3v0k4/exit.nvim](https://github.com/3v0k4/exit.nvim) - 提示 LLM（大型语言模型）编写 Vim 命令。
- [k2589/LLuMinate.nvim](https://github.com/k2589/lluminate.nvim) - 通过将 LSP 悬停添加到剪贴板来丰富 LLM 的上下文。
- [milanglacier/yarepl.nvim#aider-extensions](https://github.com/milanglacier/yarepl.nvim/blob/main/extensions/README.md) - 与 TUI AI 编码助手 [aider-chat](https://aider.chat) 集成。
- [Davidyz/VectorCode](https://github.com/davidyz/vectorcode) - 通过存储库级 RAG 增强您的 LLM 体验。
- [dlants/magenta.nvim](https://github.com/dlants/magenta.nvim) - 利用编码助手进行聊天和代码生成。为 AI/LLM 代理提供探索和编辑代码的工具，例如 Aider、Cursor 和 Windsurf。
- [Flemma-Dev/flemma.nvim](https://github.com/Flemma-Dev/flemma.nvim) - 一流的人工智能工作空间。
- [heilgar/nochat.nvim](https://github.com/heilgar/nochat.nvim) - 通过 Ollama、Anthropic (Claude) 和 ChatGPT 等多个 AI 提供商，轻松生成类似光标的自然语言。
- [julwrites/llm-nvim](https://github.com/julwrites/llm-nvim) - 与 [LLM](https://github.com/simonw/llm) 工具全面集成。
- [azorng/goose.nvim](https://github.com/azorng/goose.nvim) - 与 [goose](https://block.github.io/goose) 无缝集成 - 无需离开编辑器即可使用强大的 AI 代理。
- [mozanunal/sllm.nvim](https://github.com/mozanunal/sllm.nvim) - 由 Simon Willison 的 LLM CLI 提供支持的编辑器内聊天：在 Markdown 缓冲区中流式回复、管理丰富的上下文（文件、URL、选择、诊断、shell 输出）、交互式切换模型，甚至查看令牌使用统计信息。
- [chatvim/chatvim.nvim](https://github.com/chatvim/chatvim.nvim) - 使用 xAI、OpenAI 和 Anthropic 的 AI 模型与 Markdown 文件聊天。
- [3ZsForInsomnia/code-companion-picker](https://github.com/3ZsForInsomnia/code-companion-picker) - 用于预览 CodeCompanion 提示和技能（使用 OpenSkills）的零食选择器集成。
- [3ZsForInsomnia/vs-code-companion](https://github.com/3ZsForInsomnia/vs-code-companion) - 用于将 VSCode 的 Markdown 提示导入 CodeCompanion 的工具。
- [3ZsForInsomnia/token-count.nvim](https://github.com/3ZsForInsomnia/token-count.nvim) - 显示当前缓冲区的令牌计数，以及 Lualine 和 NeoTree 的集成。
- [nishu-murmu/cursor-inline](https://github.com/nishu-murmu/cursor-inline) - 光标式内联 AI 编辑。选择代码，描述更改，并获得您可以接受或拒绝的内联突出显示编辑 - 类似于光标内联工作流程。
- [alsi-lawr/agent-term.nvim](https://github.com/alsi-lawr/agent-term.nvim) - 终端代理 UI 具有持久视图、基于钩子的轻量级编辑器上下文以及适用于任何本机 AI TUI 的可扩展预设。
- [ishiooon/codex.nvim](https://github.com/ishiooon/codex.nvim) - Codex IDE 集成，无需 API 密钥。
- [nickjvandyke/opencode.nvim](https://github.com/nickjvandyke/opencode.nvim) - OpenCode AI 助手集成。
- [taigrr/neocrush.nvim](https://github.com/taigrr/neocrush.nvim) - 与 Crush AI 编码助手集成，具有编辑突出显示、自动对焦、望远镜支持、终端和版本管理功能。
<!--lint disable double-link -->
[**⬆ 回到顶部**](#contents)
<!--lint enable double-link -->

## 编程语言支持

- [alessio-vivaldelli/java-creator-nvim](https://github.com/alessio-vivaldelli/java-creator-nvim) - 交互式 Java 文件创建器，具有自动包检测功能，支持类、接口、枚举、记录和抽象类。
- [Julian/lean.nvim](https://github.com/Julian/lean.nvim) - 支持[精益定理证明器](https://leanprover.github.io/)。
- [nvim-flutter/flutter-tools.nvim](https://github.com/nvim-flutter/flutter-tools.nvim) - 使用原生 LSP 构建 Flutter 和 Dart 应用程序。
- [brendalf/mix.nvim](https://github.com/brendalf/mix.nvim) - Mix（来自 Elixir）包装插件。
- [AckslD/swenv.nvim](https://github.com/AckslD/swenv.nvim) - 无需重启即可快速切换 Python 虚拟环境的小插件。
- [gennaro-tedesco/nvim-jqx](https://github.com/gennaro-tedesco/nvim-jqx) - JSON 文件的交互界面。
- [nanotee/sqls.nvim](https://github.com/nanotee/sqls.nvim) - SQL数据库连接插件+LSP客户端。
- [dmmulroy/tsc.nvim](https://github.com/dmmulroy/tsc.nvim) - 使用 TypeScript 编译器 (`tsc`) 进行异步项目范围的 TypeScript 类型检查，并将结果加载到快速修复列表中。
- [dmmulroy/ts-error-translator.nvim](https://github.com/dmmulroy/ts-error-translator.nvim) - Matt Pocock 的 VSCode 的“ts-error-translator”端口，用于将混乱且令人困惑的 TypeScript 错误转换为简单的英语。
- [chuwy/ucm.nvim](https://github.com/chuwy/ucm.nvim) - 浏览 [Unison](https://unison-lang.org/) 项目。
- [niuiic/typst-preview.nvim](https://github.com/niuiic/typst-preview.nvim) - 预览 Typst 文档，响应文件更改。
- [chomosuke/typst-preview.nvim](https://github.com/chomosuke/typst-preview.nvim) - 在浏览器中预览 Typst 文档，每次击键即时更新，以及代码和预览之间的交叉跳转。
- [quarto-dev/quarto-nvim](https://github.com/quarto-dev/quarto-nvim) - 用于处理 [Quarto](https://quarto.org/) 文档的工具。
- [iabdelkareem/csharp.nvim](https://github.com/iabdelkareem/csharp.nvim) - 增强 .NET 开发人员的开发体验。
- [neolooong/whichpy.nvim](https://github.com/neolooong/whichpy.nvim) - 切换Python解释器而无需重新启动LSP。
- [nvim-java/nvim-java](https://github.com/nvim-java/nvim-java) - 获得轻松 Java 体验所需的一切。
- [kiyoon/python-import.nvim](https://github.com/kiyoon/python-import.nvim) - 添加带有 Tree-sitter、LSP 等的 Python 导入语句。
- [kiyoon/haskell-scope-highlighting.nvim](https://github.com/kiyoon/haskell-scope-highlighting.nvim) - Haskell 语法高亮显示考虑了变量作用域。灵感来自教授的“上下文着色”。道格拉斯·克罗克福德。
- [apyra/nvim-unity.nvim](https://github.com/apyra/nvim-unity) - 使用 Neovim 作为默认 Unity 编辑器，并通过 OmniSharp 提供完整的 LSP 支持。
- [atomicptr/defold.nvim](https://github.com/atomicptr/defold.nvim) - 用于 Defold 游戏引擎的含电池开发环境。
- [onlyati/quadlet-lsp.nvim](https://github.com/onlyati/quadlet-lsp.nvim) - 为 Podman Quadlet 文件提供补全、悬停和其他语言服务器功能。
- [leblocks/hopcsharp.nvim](https://github.com/leblocks/hopcsharp.nvim) - 在 C# 存储库中提供无 LSP 导航和类型层次结构信息。
- [AnsonH/copy-python-path.nvim](https://github.com/AnsonH/copy-python-path.nvim) - 复制 Python 符号的引用或导入路径。
- [J-Cowsert/classlayout.nvim](https://github.com/J-Cowsert/classlayout.nvim) - 在浮动窗口中可视化 C/C++ 结构和类内存布局（字段偏移、填充、对齐）。
- [awsum-lang/awsum-nvim](https://github.com/awsum-lang/awsum-nvim) - LSP 客户端和 Tree-sitter 突出显示 [Awsum](https://awsum-lang.org) 编程语言。
- [cuducos.me/yaml.nvim](https://tangled.org/cuducos.me/yaml.nvim) - 处理 YAML 文件的实用程序。
- [mosheavni/yaml-companion.nvim](https://github.com/mosheavni/yaml-companion.nvim) - 使用“yaml-language-server”自动检测和选择 YAML 文件的模式，包括内置的 Kubernetes 支持。
- [gbprod/phpactor.nvim](https://github.com/gbprod/phpactor.nvim) - Lua 版本的 [phpactor](https://github.com/phpactor/phpactor)。
- [ta-tikoma/php.easy.nvim](https://github.com/ta-tikoma/php.easy.nvim) - PHP开发辅助方法：创建类、常量、方法、属性；简单的复制和删除实体。
- [TheLeoP/powershell.nvim](https://github.com/TheLeoP/powershell.nvim) - 一流的 PowerShell 编辑器集成。包括 LSP、调试（需要 nvim-dap）和 $psEditor API 支持。
- [Who5673/who5673-nasm](https://github.com/Who5673/who5673-nasm) - 帮助人们使用代码片段更快、更方便地编写 Netwide 汇编语言。
- [sachinsenal0x64/hot.nvim](https://github.com/sachinsenal0x64/hot.nvim) - 适用于任何编程语言的热重载器。
- [simonwinther/cppman.nvim](https://github.com/simonwinther/cppman.nvim) - 从 cppman 搜索 C++ 文档并在浮动窗口中查看结果，并由本地 SQLite 索引支持以实现快速查找。

### 戈兰

- [romus204/go-tagger.nvim](https://github.com/romus204/go-tagger.nvim) - 一个轻量级插件，用于管理 Go 文件中的结构字段标签。
- [ray-x/go.nvim](https://github.com/ray-x/go.nvim) - 基于 LSP 和 Tree-sitter 的 Golang 插件。
- [crusj/structrue-go.nvim](https://github.com/crusj/structrue-go.nvim) - 更好地结构化显示 Golang 符号信息。
- [crispgm/nvim-go](https://github.com/crispgm/nvim-go) - Golang 开发插件的最小实现。
- [olexsmir/gopher.nvim](https://github.com/olexsmir/gopher.nvim/) - 使 Golang 开发变得最简单的插件。
- [rafaelsq/nvim-goc.lua](https://github.com/rafaelsq/nvim-goc.lua) - 使用 Golang 代码覆盖率突出显示您的缓冲区。
- [crusj/hierarchy-tree-go.nvim](https://github.com/crusj/hierarchy-tree-go.nvim) - Golang 与“callHierarchy”UI 树集成。
- [yanskun/gotests.nvim](https://github.com/yanskun/gotests.nvim) - 使用 [gotests](https://github.com/cweill/gotests) 让 Go 测试变得简单。
- [maxandron/goplements.nvim](https://github.com/maxandron/goplements.nvim) - 可视化 Go 结构和接口实现。
- [Snikimonkd/cmp-go-pkgs](https://github.com/Snikimonkd/cmp-go-pkgs) - Go 包名称的 Cmp 源。
- [Yu-Leo/gosigns.nvim](https://github.com/Yu-Leo/gosigns.nvim) - 可视化一些 Go 提示：结构、接口和方法实现；去评论吧。
- [Yu-Leo/cmp-go-pkgs](https://github.com/Yu-Leo/cmp-go-pkgs) - Cmp 源提供要导入的 Go 包的名称。
- [fredrikaverpil/godoc.nvim](https://github.com/fredrikaverpil/godoc.nvim) - 模糊搜索 Go 包/符号并查看文档。
- [sjclayton/goplexity.nvim](https://github.com/sjclayton/goplexity.nvim) - Golang 的时间/空间 (Big-O) 复杂性分析器。

### 网页开发

- [rest-nvim/rest.nvim](https://github.com/rest-nvim/rest.nvim) - 用 Lua 编写的快速 HTTP 客户端。
- [lima1909/resty.nvim](https://github.com/lima1909/resty.nvim) - 快速且易于使用的 HTTP-Rest-Client。
- [mistweaverco/kulala.nvim](https://github.com/mistweaverco/kulala.nvim) - 最小的 HTTP 客户端接口。
- [heilgar/nvim-http-client](https://github.com/heilgar/nvim-http-client) - 易于使用的 HTTP 客户端，与 IntelliJ (JetBrains) HTTP 客户端语法兼容。
- [farias-hecdin/CSSVarViewer](https://github.com/farias-hecdin/CSSVarViewer) - 在虚拟文本中轻松可视化 CSS 变量的内容。
- [farias-hecdin/CSSVarHighlight](https://github.com/farias-hecdin/CSSVarHighlight) - 借助“mini.hipatterns”快速突出显示您在 CSS 变量中定义的颜色。
- [mawkler/jsx-element.nvim](https://github.com/mawkler/jsx-element.nvim) - JSX/TSX 文本对象和动作。
- [BibekBhusal0/nvim-shadcn](https://github.com/BibekBhusal0/nvim-shadcn) - 使用望远镜轻松添加 Shadcn UI 组件。
- [azratul/expose-localhost.nvim](https://github.com/azratul/expose-localhost.nvim) - 使用 cloudflared 或 ngrok 将您的本地服务器公开到互联网。
- [yelog/i18n.nvim](https://github.com/yelog/i18n.nvim) - 国际化 (i18n) 管理，LSP 支持“Vue”、“React”、“Java”等。
- [Kenzo-Wada/boundary.nvim](https://github.com/Kenzo-Wada/boundary.nvim) - 在 JSX 代码中内嵌显示“use client”标记，以可视化客户端组件边界。
- [abidibo/nvim-httpyac](https://github.com/abidibo/nvim-httpyac) - 提供与“httpYac”的集成。
- [rodrigoscc/nurl.nvim](https://github.com/rodrigoscc/nurl.nvim) - 带有用纯 Lua 定义的请求的 HTTP 客户端。
- [cjodo/convert.nvim](https://github.com/cjodo/convert.nvim) - 帮助进行 CSS 单位转换。
- [tednguyendev/recent_rails.nvim](https://github.com/tednguyendev/recent_rails.nvim) - 用于显示最近 Rails 操作、视图和错误的望远镜选择器。
- [ankushbhagats/liveserver.nvim](https://github.com/ankushbhagats/liveserver.nvim) - 实时服务器与智能命令和可点击的 lualine 切换集成。

### Markdown 和 LaTeX

- [iamcco/markdown-preview.nvim](https://github.com/iamcco/markdown-preview.nvim) - 通过同步滚动和灵活的配置在现代浏览器上预览 Markdown。
- [davidgranstrom/nvim-markdown-preview](https://github.com/davidgranstrom/nvim-markdown-preview) - 通过作业控制 API 使用 pandoc 和 live-server 在浏览器中进行 Markdown 预览。
- [jghauser/auto-pandoc.nvim](https://github.com/jghauser/auto-pandoc.nvim) - 利用 YAML 块轻松进行 pandoc 转换。
- [jghauser/follow-md-links.nvim](https://github.com/jghauser/follow-md-links.nvim) - 按 Enter 键可跟踪内部 Markdown 链接。
- [jubnzv/mdeval.nvim](https://github.com/jubnzv/mdeval.nvim) - 评估 Markdown 文档中的代码块。
- [kdheepak/panvimdoc](https://github.com/kdheepak/panvimdoc) - pandoc 到 vimdoc GitHub 操作。
- [frabjous/knap](https://github.com/frabjous/knap) - 用于为 Markdown、LaTeX 和其他文档创建自动更新预览的插件。
- [jbyuki/carrot.nvim](https://github.com/jbyuki/carrot.nvim) - Markdown 评估器 Lua 代码块。
- [Nedra1998/nvim-mdlink](https://github.com/Nedra1998/nvim-mdlink) - 简化创建和关注 Markdown 链接。
- [nfrid/markdown-togglecheck](https://github.com/nfrid/markdown-togglecheck) - 使用 Tree-sitter 切换任务列表复选框。
- [toppair/peek.nvim](https://github.com/toppair/peek.nvim) - 在 Web 视图窗口中预览 Markdown。
- [yaocccc/nvim-hl-mdcodeblock.lua](https://github.com/yaocccc/nvim-hl-mdcodeblock.lua) - 使用 Tree-sitter 突出显示 Markdown 代码块。
- [kiran94/edit-markdown-table.nvim](https://github.com/kiran94/edit-markdown-table.nvim) - 使用 Tree-sitter 编辑 Markdown 表。
- [richardbizik/nvim-toc](https://github.com/richardbizik/nvim-toc) - 轻松生成 Markdown 文件的目录。
- [Zeioth/markmap.nvim](https://github.com/Zeioth/markmap.nvim) - 将 Markdown 可视化为思维导图。
- [tadmccorkle/markdown.nvim](https://github.com/tadmccorkle/markdown.nvim) - 适用于 Markdown 文件的可配置工具，包括内联样式、链接和导航键盘映射、目录、改进的列表编辑等。
- [mpas/marp-nvim](https://github.com/mpas/marp-nvim) - 使用 Markdown 和 [Marp](https://marp.app/) 进行演示。
- [MeanderingProgrammer/render-markdown.nvim](https://github.com/MeanderingProgrammer/render-markdown.nvim) - 改进直接查看 Markdown 文件。
- [ChuufMaster/markdown-toc](https://github.com/ChuufMaster/markdown-toc) - 从任何其他 Markdown 文件在任何 Markdown 文件中生成 TOC，并具有可自定义级别的标题和表情符号的可供性，并确保它使用相对路径在 GitHub 上运行。
- [OXY2DEV/markview.nvim](https://github.com/OXY2DEV/markview.nvim) - 可破解的 Markdown、Typst、LaTeX、HTML（内联）和 YAML 渲染器。
- [gunasekar/markview-smart-tables.nvim](https://github.com/gunasekar/markview-smart-tables.nvim) - 在“markview.nvim”中自动调整和自动换行宽 Markdown 表格。
- [Kicamon/markdown-table-mode.nvim](https://github.com/Kicamon/markdown-table-mode.nvim) - Markdown 格式插件类似于 vim-table-mode，但用 Lua 编写。
- [SCJangra/table-nvim](https://github.com/SCJangra/table-nvim) - Markdown 表格编辑器，可在您键入时格式化表格。
- [timantipov/md-table-tidy.nvim](https://github.com/timantipov/md-table-tidy.nvim) - 简单的 Markdown 表格格式。
- [nvim-telescope/telescope-bibtex.nvim](https://github.com/nvim-telescope/telescope-bibtex.nvim) - Telescope 扩展用于搜索 BibTeX 条目并将其粘贴到您的 TeX 文件中。
- [Thiago4532/mdmath.nvim](https://github.com/Thiago4532/mdmath.nvim) - 一个 Markdown 方程预览器，使用 kitty 图形协议。
- [OXY2DEV/markdoc.nvim](https://github.com/OXY2DEV/markdoc.nvim) - 基于 Tree-sitter 的 `markdown -> vimdoc` 转换器。
- [YousefHadder/markdown-plus.nvim](https://github.com/YousefHadder/markdown-plus.nvim) - 为 Markdown 文件提供完整的编辑体验，包括通过简单快速的键盘映射对列表、链接、目录等进行支持。
- [Myzel394/easytables.nvim](https://github.com/Myzel394/easytables.nvim) - 通过实时预览和有用的助手轻松插入和编辑 Markdown 表格。
- [tttol/md-outline.nvim](https://github.com/tttol/md-outline.nvim) - 自动显示 Markdown 文件的大纲。
- [rogue-87/inlyne.nvim](https://github.com/rogue-87/inlyne.nvim) - [inlyne](https://github.com/Inlyne-Project/inlyne) Markdown 查看器的包装。
- [Prgebish/sigil.nvim](https://github.com/Prgebish/sigil.nvim) - 实现 Emacs 的“美化符号模式”，在编辑 LaTeX 和 Typst 文件时以可视方式用 Unicode 符号替换文本模式。
- [satozawa/graft.nvim](https://github.com/satozawa/graft.nvim) - 使用子树文本对象、Alt+hjkl 导航和结构操作对 Markdown 项目符号列表进行树形结构编辑。
- [kibi2/tirenvi.nvim](https://github.com/kibi2/tirenvi.nvim) - 通过无损往返编辑 Markdown 和 CSV 表。
<!--lint disable double-link -->
[**⬆ 回到顶部**](#contents)
<!--lint enable double-link -->

## 语言

- [potamides/pantran.nvim](https://github.com/potamides/pantran.nvim) - 使用交互式翻译窗口翻译您的文本。
- [niuiic/translate.nvim](https://github.com/niuiic/translate.nvim) - 通过 shell 命令调用任何翻译引擎。
- [tanloong/interlaced.nvim](https://github.com/tanloong/interlaced.nvim) - 帮助对齐双语并行文本。
- [sontungexpt/vietnamese.nvim](https://github.com/sontungexpt/vietnamese.nvim) - 越南语输入法引擎，原生支持在插入模式下输入越南语。
- [doodleEsc/translator.nvim](https://github.com/doodleEsc/translator.nvim) - 强大的人工智能翻译插件，利用 OpenAI 的 GPT 模型提供具有自然语言理解的高质量翻译。
- [kiyoon/Korean-IME.nvim](https://github.com/kiyoon/Korean-IME.nvim) - 独立于操作系统的韩语输入法，可将英语输入就地转换为韩语。
- [bennorichters/taal.nvim](https://github.com/bennorichters/taal.nvim) - 使用法学硕士改善多种语言的语法和拼写错误。
- [walkersumida/deepl.nvim](https://github.com/walkersumida/deepl.nvim) - 使用具有多种输出模式（浮动、替换、附加）的 DeepL API 翻译文本。
- [acidsugarx/babel.nvim](https://github.com/acidsugarx/babel.nvim) - 使用具有异步支持、浮动显示和多选择器集成的 Google 翻译翻译文本。
- [noir4y/comment-translate.nvim](https://github.com/noir4y/comment-translate.nvim) - 使用在线以及本地法学硕士或外部翻译人员翻译代码注释和字符串。
<!--lint disable double-link -->
[**⬆ 回到顶部**](#contents)
<!--lint enable double-link -->

## 语法

- [nvim-treesitter/nvim-treesitter](https://github.com/nvim-treesitter/nvim-treesitter) - 树保姆配置和抽象层。
- [romus204/tree-sitter-manager.nvim](https://github.com/romus204/tree-sitter-manager.nvim) - 适用于 Neovim 0.12+ 的轻量级 Tree-sitter 解析器管理器，用于替换存档的“nvim-treesitter”插件。
- [nvim-treesitter/nvim-treesitter-textobjects](https://github.com/nvim-treesitter/nvim-treesitter-textobjects) - 使用 Tree-sitter 查询创建您自己的文本对象。
- [RRethy/nvim-treesitter-textsubjects](https://github.com/RRethy/nvim-treesitter-textsubjects) - 位置和语法感知文本对象_做你的意思_。
- [kylechui/nvim-surround](https://github.com/kylechui/nvim-surround) - 用于添加/更改/删除周围分隔符对的插件。
- [nvim-mini/mini.nvim#mini.surround](https://github.com/nvim-mini/mini.nvim/blob/main/readmes/mini-surround.md) - 用于处理文本环境的“mini.nvim”模块（添加、删除、替换、查找、突出显示）。支持点重复、不同的搜索方法、“上一个”/“下一个”扩展映射、Tree-sitter 集成等等。
- [Hdoc1509/gh-actions.nvim](https://github.com/Hdoc1509/gh-actions.nvim) - GitHub Actions 的 Tree-sitter 语法和 LSP 查询配置。
- [m-demare/hlargs.nvim](https://github.com/m-demare/hlargs.nvim) - 使用 Tree-sitter 突出显示参数的定义和用法。
- [calops/hmts.nvim](https://github.com/calops/hmts.nvim) - 树管理员查询 Home Manager Nix 文件。
- [LhKipp/nvim-nu](https://github.com/LhKipp/nvim-nu) - 对 nushell 语言的基本编辑器支持。
- [desdic/agrolens.nvim](https://github.com/desdic/agrolens.nvim) - 使用 Telescope 或 FZF 通过 Tree-sitter 节点进行导航。
- [IndianBoy42/tree-sitter-just](https://github.com/IndianBoy42/tree-sitter-just) - [Justfiles](https://github.com/casey/just) 的树守护者语法。
- [fei6409/log-highlight.nvim](https://github.com/fei6409/log-highlight.nvim) - 通用日志语法突出显示和日志文件类型管理支持。
- [MeanderingProgrammer/treesitter-modules.nvim](https://github.com/MeanderingProgrammer/treesitter-modules.nvim) - 来自 nvim-treesitter 主分支的原始模块。
- [BibekBhusal0/tree-hierarchy.nvim](https://github.com/BibekBhusal0/tree-hierarchy.nvim) - 根据树保姆编辑文本和导航。
- [Sang-it/fluoride](https://github.com/Sang-it/fluoride) - 结构代码编辑器。从基于 Tree-sitter 的浮动窗口查看、重新排序、重命名和注释代码声明。
<!--lint disable double-link -->
[**⬆ 回到顶部**](#contents)
<!--lint enable double-link -->

## 片段

- [L3MON4D3/LuaSnip](https://github.com/L3MON4D3/LuaSnip) - 用 Lua 编写的片段引擎。
- [nvim-mini/mini.nvim#mini.snippets](https://github.com/nvim-mini/mini.nvim/blob/main/readmes/mini-snippets.md) - 用于管理和扩展片段的“mini.nvim”模块。支持LSP片段语法、灵活的加载器、模糊前缀匹配、交互式选择、具有丰富可视化的片段会话等等。
- [smjonas/snippet-converter.nvim](https://github.com/smjonas/snippet-converter.nvim) - 在最常见的代码片段格式之间转换代码片段，并使用几行 Lua 代码对其进行修改。
- [dcampos/nvim-snippy](https://github.com/dcampos/nvim-snippy) - 用 Lua 编写的 Snippet 插件，支持 [vim-snippets](https://github.com/honza/vim-snippets)。
- [ellisonleao/carbon-now.nvim](https://github.com/ellisonleao/carbon-now.nvim) - 从终端创建漂亮的代码片段。
- [TobinPalmer/rayso.nvim](https://github.com/TobinPalmer/rayso.nvim) - 使用 [ray.so](https://ray.so) 创建代码片段。
- [mrcjkb/haskell-snippets.nvim](https://github.com/mrcjkb/haskell-snippets.nvim) - LuaSnip 的 Haskell 代码片段，由 Tree-sitter 和 LSP 提供支持。
- [rafamadriz/friendly-snippets](https://github.com/rafamadriz/friendly-snippets) - 不同语言的预配置片段集。
- [cvigilv/esqueleto.nvim](https://github.com/cvigilv/esqueleto.nvim) - 创建新文件时使用的简单模板。
- [chrisgrieser/nvim-scissors](https://github.com/chrisgrieser/nvim-scissors) - 自动编辑和创建片段。
- [guilherme-puida/tesoura.nvim](https://github.com/guilherme-puida/tesoura.nvim) - 使用本机片段 API 的灵活片段系统。
<!--lint disable double-link -->
[**⬆ 回到顶部**](#contents)
<!--lint enable double-link -->

## 注册

- [bfredl/nvim-miniyank](https://github.com/bfredl/nvim-miniyank) - 类似killring 的插件，没有默认映射。
- [gennaro-tedesco/nvim-peekup](https://github.com/gennaro-tedesco/nvim-peekup) - 与 Vim 寄存器动态交互。
- [tversteeg/registers.nvim](https://codeberg.org/fosk/registers.nvim) - Vim 寄存器的非侵入式最小预览。
- [acksld/nvim-neoclip.lua](https://github.com/AckslD/nvim-neoclip.lua) - 与望远镜集成的剪贴板管理器。
- [tenxsoydev/karen-yank.nvim](https://github.com/tenxsoydev/karen-yank.nvim) - 通过删除、剪切和复制映射进行更有意的寄存器处理。
- [desdic/macrothis.nvim](https://github.com/desdic/macrothis.nvim) - 保存和加载宏/寄存器。
- [kr40/nvim-macros](https://github.com/kr40/nvim-macros) - 保存和加载宏的简单方法，具有备份和格式化选项。
<!--lint disable double-link -->
[**⬆ 回到顶部**](#contents)
<!--lint enable double-link -->

## 马克

- [cbochs/grapple.nvim](https://github.com/cbochs/grapple.nvim) - 提供标记、光标跟踪以及对重要项目文件的即时导航。
- [chentoast/marks.nvim](https://github.com/chentoast/marks.nvim) - 查看 Vim 标记并与之交互的用户体验更好。
- [ThePrimeagen/harpoon](https://github.com/ThePrimeagen/harpoon/tree/harpoon2) - 每个项目的自动更新和可编辑标记实用程序，用于快速文件导航。
- [otavioschwanck/arrow.nvim](https://github.com/otavioschwanck/arrow.nvim) - 与 harpoon 类似，但具有不同的用户体验，需要单键绑定和状态行支持。
- [ofirgall/open.nvim](https://github.com/ofirgall/open.nvim) - 使用自定义开启器打开当前单词，例如 GitHub 速记。
- [LeonHeidelbach/trailblazer.nvim](https://github.com/LeonHeidelbach/trailblazer.nvim) - TrailBlazer 引入了基于堆栈的标记系统，该系统使用项目范围标记实现全新的动态且超快速的工作流程。
- [tomasky/bookmarks.nvim](https://github.com/tomasky/bookmarks.nvim) - 带有全局文件存储的书签，用 Lua 编写。
- [LintaoAmons/bookmarks.nvim](https://github.com/LintaoAmons/bookmarks.nvim) - 您的新书签选项：简单而强大。
- [heilgar/bookmarks.nvim](https://github.com/heilgar/bookmarks.nvim) - 通过 Telescope 集成和 SQLite 存储管理线路书签。
- [desdic/marlin.nvim](https://github.com/desdic/marlin.nvim) - 与 harpoon 类似，但有一些关键区别，例如项目路径、拆分支持、无 UI。
- [fnune/recall.nvim](https://github.com/fnune/recall.nvim) - Recall 通过关注全球商标、简化其使用并增强其可见性和可导航性来完善商标的使用。
- [niuiic/track.nvim](https://github.com/niuiic/track.nvim) - 带描述的增强标记。跟踪阅读源代码的思维过程。
- [tristone13th/lspmark.nvim](https://github.com/tristone13th/lspmark.nvim) - 健全的项目书签，具有基于 LSP 的持久存储。
- [EvWilson/spelunk.nvim](https://github.com/EvWilson/spelunk.nvim) - 使用友好的用户界面以堆栈形式创建和管理书签。
- [2KAbhishek/markit.nvim](https://github.com/2KAbhishek/markit.nvim) - 改进了全局标记和项目范围书签，以快速导航文件。
- [zongben/navimark.nvim](https://github.com/zongben/navimark.nvim) - 一个简单而强大的带有望远镜的书签管理器。
- [Beargruug/skipper.nvim](https://github.com/Beargruug/skipper.nvim/) - 轻松在文件中的函数之间跳转。
- [mohseenrm/marko.nvim](https://github.com/mohseenrm/marko.nvim) - 在幕后，不同项目的全局标记管理。
- [y3owk1n/warp.nvim](https://github.com/y3owk1n/warp.nvim) - 简单的鱼叉替代方案，专注于文件之间的标记和导航。
- [walkersumida/fusen.nvim](https://github.com/walkersumida/fusen.nvim) - 便签书签，每个 Git 分支带有悬停注释和 Telescope 集成。
- [markgandolfo/dartboard.nvim](https://github.com/markgandolfo/dartboard.nvim) - 受 Harpoon 和 Lasso 的启发，标记文件并快速访问它们。
- [dimtion/guttermarks.nvim](https://github.com/dimtion/guttermarks.nvim) - 在缓冲区装订线中显示标记。
- [adithyasource/spearmint.nvim](https://github.com/adithyasource/spearmint.nvim) - 带端子支撑的轻型鱼叉式标记。
<!--lint disable double-link -->
[**⬆ 回到顶部**](#contents)
<!--lint enable double-link -->

## 搜索

- [2KAbhishek/seeker.nvim](https://github.com/2KAbhishek/seeker.nvim) - 构建在 `snacks.nvim` 之上的渐进式文件搜索器。
- [wurli/visimatch.nvim](https://github.com/wurli/visimatch.nvim) - 在视觉模式下向与当前选择匹配的任何文本添加突出显示。
- [kevinhwang91/nvim-hlslens](https://github.com/kevinhwang91/nvim-hlslens) - 帮助您更好地浏览搜索到的信息，无缝跳转匹配的实例。
- [rktjmp/highlight-current-n.nvim](https://github.com/rktjmp/highlight-current-n.nvim) - 突出显示当前 /, ?或 \* 在按 n 或 N 时在光标下匹配，然后退出。
- [ray-x/sad.nvim](https://github.com/ray-x/sad.nvim) - 太空时代 seD 集成。批处理文件编辑工具，[sad](https://github.com/ms-jpq/sad)的包装器。
- [s1n7ax/nvim-search-and-replace](https://github.com/s1n7ax/nvim-search-and-replace) - 从当前工作目录同时搜索和替换多个文件。
- [AckslD/muren.nvim](https://github.com/AckslD/muren.nvim/) - 通过交互式 UI 进行多次替换。
- [nvim-pack/nvim-spectre](https://github.com/nvim-pack/nvim-spectre) - 搜索和替换面板。
- [nvimdev/hlsearch.nvim](https://github.com/nvimdev/hlsearch.nvim) - 使用 n 或 N 时自动删除搜索突出显示并重新突出显示。
- [mangelozzi/rgflow.nvim](https://github.com/mangelozzi/rgflow.nvim) - 快速将 RipGrep 结果放入可编辑的 Quickfix 列表中，同时学习 RipGrep 的 CLI。
- [duane9/nvim-rg](https://github.com/duane9/nvim-rg) - 异步运行 RipGrep 并在快速修复窗口中查看结果。
- [FabianWirth/search.nvim](https://github.com/FabianWirth/search.nvim) - 不同望远镜选择器的选项卡。
- [backdround/improved-search.nvim](https://github.com/backdround/improved-search.nvim) - 添加搜索功能。
- [polirritmico/telescope-lazy-plugins.nvim](https://github.com/polirritmico/telescope-lazy-plugins.nvim) - 一个 Telescope 选择器，用于快速访问lazy.nvim 规范中的插件配置。
- [MagicDuck/grug-far.nvim](https://github.com/MagicDuck/grug-far.nvim) - 基于缓冲区的实时搜索并使用“rg”标志的全部功能进行替换。格鲁格喜欢。
- [chrisgrieser/nvim-rip-substitute](https://github.com/chrisgrieser/nvim-rip-substitute) - 通过增量预览、方便的 UI 和现代正则表达式语法在当前缓冲区或工作区中进行搜索和替换。
- [wsdjeg/flygrep.nvim](https://github.com/wsdjeg/flygrep.nvim) - 在浮动窗口中异步搜索文本。
- [prochri/telescope-all-recent.nvim](https://github.com/prochri/telescope-all-recent.nvim) - 适用于任何望远镜选择器的频率和新近度排序器。
- [mahyarmirrashed/search-and-replace.nvim](https://github.com/mahyarmirrashed/search-and-replace.nvim) - 为务实的工程师提供简单、有效的搜索和替换功能。
- [bravoecho/brook.nvim](https://github.com/bravoecho/brook.nvim) - 响应式、shell 安全的 ripgrep 搜索快速修复列表，具有本机 n/N 导航。
- [KieranCanter/candela.nvim](https://github.com/KieranCanter/candela.nvim) - 通过定义正则表达式模式来突出显示和/或隔离匹配行来分析日志。
- [ankushbhagats/match.nvim](https://github.com/ankushbhagats/match.nvim) - 最小化浮动搜索和替换，具有实时比赛跟踪、导航和快速替换功能。
<!--lint disable double-link -->
[**⬆ 回到顶部**](#contents)
<!--lint enable double-link -->

## 模糊查找器

- [nvim-telescope/telescope.nvim](https://github.com/nvim-telescope/telescope.nvim) - Telescope.nvim 是一个高度可扩展的(https://github.com/nvim-telescope/telescope.nvim/wiki/Extensions) 一个高度可扩展的列表模糊查找器。
- [vijaymarupudi/nvim-fzf](https://github.com/vijaymarupudi/nvim-fzf) - 使用 FZF 的 Lua API。允许 UI 速度和可用性完全异步。
- [camspiers/snap](https://github.com/camspiers/snap) - 可扩展的模糊查找器。与 Telescope 类似，并针对性能进行了优化，尤其是在大型代码库中进行 grep 时。
- [ibhagwan/fzf-lua](https://github.com/ibhagwan/fzf-lua) - Lua 版本的“fzf.vim”，高性能且完全异步，支持“nvim-web-devicons”、Git 指示器、LSP、quickfix/位置列表等。还支持 [`skim`](https://github.com/lotabout/skim) 作为其 fzf 二进制文件。
- [willyelm/pulse.nvim](https://github.com/willyelm/pulse.nvim) - 命令的单个入口点。使用前缀通过选择器快速访问诊断、Git 等。
- [jvgrootveld/telescope-zoxide](https://github.com/jvgrootveld/telescope-zoxide) - Telescope 集成了 [zride](https://github.com/ajeetdsouza/zride)，这是一个跟踪您的使用情况的智能目录选择器。
- [nvim-mini/mini.nvim#mini.fuzzy](https://github.com/nvim-mini/mini.nvim/blob/main/readmes/mini-fuzzy.md) - “mini.nvim”模块，具有执行一个字符串与其他字符串的模糊匹配以及快速望远镜排序器的功能。
- [axkirillov/easypick.nvim](https://github.com/axkirillov/easypick.nvim) - Easypick 可让您通过任意控制台命令轻松创建 Telescope 选择器。
- [linrongbin16/fzfx.nvim](https://github.com/linrongbin16/fzfx.nvim) - 每次击键都会更新的模糊查找器。
- [nvim-mini/mini.nvim#mini.pick](https://github.com/nvim-mini/mini.nvim/blob/main/readmes/mini-pick.md) - “mini.nvim”模块具有通用交互式非阻塞选择器，具有单窗口设计、可切换预览、灵活快速的默认匹配等等。
- [nvim-mini/mini.nvim#mini.extra](https://github.com/nvim-mini/mini.nvim/blob/main/readmes/mini-extra.md) - `mini.nvim` 模块，其模块具有额外的功能。包含 20 多个“mini.pick”选择器、“mini.ai”文本对象等。
- [fdschmidt93/telescope-egrepify.nvim](https://github.com/fdschmidt93/telescope-egrepify.nvim) - Telescope 插件可在 `live_grep` 中提供更好的 `rg` 标志。
- [nvim-telescope/telescope-media-files.nvim](https://github.com/nvim-telescope/telescope-media-files.nvim) - 使用 Telescope 预览图像、pdf、epub、视频和字体。
- [crispgm/telescope-heading.nvim](https://github.com/crispgm/telescope-heading.nvim) - Telescope 扩展可在 AsciiDoc、Markdown、Vimdoc 等标题之间切换。
- [bassamsdata/namu.nvim](https://github.com/bassamsdata/namu.nvim) - 灵活、时尚的模糊选择器、LSP 符号导航器等等。
- [folke/snacks.nvim#picker](https://github.com/folke/snacks.nvim/blob/main/docs/picker.md) - 用于导航 Neovim 宇宙的现代模糊查找器。
- [dmtrKovalenko/fff.nvim](https://github.com/dmtrKovalenko/fff.nvim) - 模糊文件选择器，具有文件索引的独立本机实现和防错模糊匹配器。包括所有 QOL 功能、文件预览（和图像）、频率排序、上次查询匹配、邻近度、Git 状态奖励等等。
- [wsdjeg/picker.nvim](https://github.com/wsdjeg/picker.nvim) - 简单的模糊查找器，包括文件、ctags 轮廓等。
- [juniorsundar/refer.nvim](https://github.com/juniorsundar/refer.nvim) - 一个不会妨碍您的极简选择器。
- [dtormoen/neural-open.nvim](https://github.com/dtormoen/neural-open.nvim) - 智能“snacks.nvim”选择器，教神经网络根据您接下来最有可能打开的内容对文件进行排名。
<!--lint disable double-link -->
[**⬆ 回到顶部**](#contents)
<!--lint enable double-link -->

## 文件浏览器

- [nvim-tree/nvim-tree.lua](https://github.com/nvim-tree/nvim-tree.lua) - 一个简单快速的文件浏览器树。
- [luukvbaal/nnn.nvim](https://github.com/luukvbaal/nnn.nvim) - 由 [nnn](https://github.com/jarun/nnn) 和 Lua 提供支持的文件浏览器。
- [tamago324/lir.nvim](https://github.com/tamago324/lir.nvim) - 简单的文件浏览器。
- [kevinhwang91/rnvimr](https://github.com/kevinhwang91/rnvimr) - 一个简单但令人惊叹的文件浏览器。
- [Xuyuanp/yanil](https://github.com/Xuyuanp/yanil) - Lua 中的另一个书呆子树。
- [ms-jpq/chadtree](https://github.com/ms-jpq/chadtree) - 文件管理器。比 NERDTree 更好。
- [rolv-apneseth/tfm.nvim](https://github.com/Rolv-Apneseth/tfm.nvim) - 与“fm-nvim”类似，它提供了几种流行终端文件管理器的集成（包括[yazi](https://github.com/sxyazi/yazi)）。
- [nvim-neo-tree/neo-tree.nvim](https://github.com/nvim-neo-tree/neo-tree.nvim) - 以任何适合您的风格浏览文件系统和其他树状结构，包括侧边栏、浮动窗口、“netrw”分割样式或同时使用所有样式。
- [theblob42/drex.nvim](https://github.com/TheBlob42/drex.nvim) - 一个用 Lua 编写的简单且可配置的文件浏览器。
- [SidOfc/carbon.nvim](https://github.com/SidOfc/carbon.nvim) - 用 Lua 编写的简单目录树查看器。
- [kiran94/s3edit.nvim](https://github.com/kiran94/s3edit.nvim) - 编辑来自 Amazon S3 的文件。
- [stevearc/oil.nvim](https://github.com/stevearc/oil.nvim) - 像缓冲区一样编辑文件系统。
- [kelly-lin/ranger.nvim](https://github.com/kelly-lin/ranger.nvim) - [Ranger](https://github.com/ranger/ranger) 集成。
- [mikavilpas/yazi.nvim](https://github.com/mikavilpas/yazi.nvim) - 与 Yazi 终端文件管理器集成。
- [simonmclean/triptych.nvim](https://github.com/simonmclean/triptych.nvim) - 受 Ranger 启发的目录浏览器。
- [nvim-mini/mini.nvim#mini.files](https://github.com/nvim-mini/mini.nvim/blob/main/readmes/mini-files.md) - “mini.nvim”模块提供具有列视图的文件浏览器，能够通过编辑文本来操作文件系统。可以在目录内部和目录之间创建/删除/重命名/复制/移动文件/目录。
- [prichrd/netrw.nvim](https://github.com/prichrd/netrw.nvim) - 将图标和自定义键绑定添加到 netrw。
- [X3eRo0/dired.nvim](https://github.com/X3eRo0/dired.nvim) - 受 Emacs Dired 启发的文件浏览器。
- [saifulapm/neotree-file-nesting-config](https://github.com/saifulapm/neotree-file-nesting-config) - `neo-tree.nvim` 的预定义文件嵌套规则。
- [Enigama/miss.nvim](https://github.com/Enigama/miss.nvim) - 带有更改的“未保存”文件的简单弹出窗口，允许您保存和打开它们。有助于避免忘记向 GitHub 或类似内容添加内容。
- [vodchella/hodur.nvim](https://github.com/vodchella/hodur.nvim) - 允许您快速打开文件或复制光标下的 URL。
- [A7Lavinraj/fyler.nvim](https://github.com/A7Lavinraj/fyler.nvim) - 文件管理器可以像树形视图的缓冲区一样编辑文件系统。
- [adriancmiranda/glimpse.nvim](https://github.com/adriancmiranda/glimpse.nvim) - 快速的多格式文件预览器，具有内联小猫图形支持、外部窗格预览以及文件浏览器和选择器的集成。
<!--lint disable double-link -->
[**⬆ 回到顶部**](#contents)
<!--lint enable double-link -->

## 项目

- [karnull/switchboard.nvim](https://github.com/karnull/switchboard.nvim) - 为每个语言或项目定义“运行”、“构建”或任何自定义命令/绑定，然后在各处使用相同的按键绑定。
- [Abstract-IDE/penvim](https://github.com/Abstract-IDE/penvim) - 项目的根目录和文档带有基于项目的配置加载器的缩进检测器。
- [windwp/nvim-projectconfig](https://github.com/windwp/nvim-projectconfig) - 根据项目目录加载 Neovim 配置。
- [DrKJeff16/project.nvim](https://github.com/DrKJeff16/project.nvim) - 项目经理负责项目根检测、文档化代码和大量改进，包括“snacks.nvim”、“fzf-lua”和“picker.nvim”支持。
- [klen/nvim-config-local](https://github.com/klen/nvim-config-local) - 从工作目录安全加载本地配置文件。
- [cljoly/telescope-repo.nvim](https://github.com/cljoly/telescope-repo.nvim) - 望远镜选择器可跳转到文件系统上的任何存储库（Git 或其他）。
- [otavioschwanck/telescope-alternate.nvim](https://github.com/otavioschwanck/telescope-alternate.nvim) - 使用望远镜在常见文件之间交替。
- [natecraddock/workspaces.nvim](https://github.com/natecraddock/workspaces.nvim) - 管理工作区目录。
- [GnikDroy/projections.nvim](https://github.com/GnikDroy/projections.nvim) - 小型项目+会话管理器。
- [nyngwang/suave.lua](https://github.com/nyngwang/suave.lua) - 多选项卡项目会话自动化。
- [desdic/telescope-rooter.nvim](https://github.com/desdic/telescope-rooter.nvim) - 确保始终从项目/根目录启动望远镜（并且仅启动望远镜）。
- [SalOrak/whaler.nvim](https://github.com/SalOrak/whaler.nvim) - 望远镜扩展可以在目录之间快速移动。
- [nvim-mini/mini.nvim#mini.visits](https://github.com/nvim-mini/mini.nvim/blob/main/readmes/mini-visits.md) - “mini.nvim”模块用于持续跟踪和重用文件系统访问。允许列出“最近”/“频繁”/“经常”访问，添加/删除访问和其他数据的标签。
- [LintaoAmons/cd-project.nvim](https://github.com/LintaoAmons/cd-project.nvim) - 您所需要的只是一种更简单的方法“cd”到另一个项目目录。
- [LucasTavaresA/headers.nvim](https://github.com/LucasTavaresA/headers.nvim) - 零配置页眉/页脚警告。
- [zongben/proot.nvim](https://github.com/zongben/proot.nvim) - 带望远镜的轻型项目导航器。
- [wsdjeg/rooter.nvim](https://github.com/wsdjeg/rooter.nvim) - 将工作目录更改为项目根目录。
- [cosmicbuffalo/root_swapper.nvim](https://github.com/cosmicbuffalo/root_swapper.nvim) - 轻量级根交换器，使用“lcd”根据当前缓冲区交换到适当的根目录。
- [mrjones2014/codesettings.nvim](https://github.com/mrjones2014/codesettings.nvim) - 轻松将项目本地设置（例如“.vscode/settings.json”）加载到 Neovim 0.11+ 本机 LSP 设置中。
- [josephschmitt/pj.nvim](https://github.com/josephschmitt/pj.nvim) - 自动项目发现，可配置深度，支持多个选择器（Snacks、Telescope、fzf-lua）。
- [martuscellifaria/ahoicpp.nvim](https://github.com/martuscellifaria/ahoicpp.nvim) - 以模块化方式设置 C++ 项目，并帮助新手完成该语言的繁重工作。
- [OscarCreator/rsync.nvim](https://github.com/OscarCreator/rsync.nvim) - 使用 rsync 自动将上/下项目同步到远程。
<!--lint disable double-link -->
[**⬆ 回到顶部**](#contents)
<!--lint enable double-link -->

## 缓冲器

- [TheLazyCat00/workspaces-nvim](https://github.com/TheLazyCat00/workspaces-nvim) - 将文件固定到项目工作区中的特定键，使您可以快速访问最重要的文件。
- [dzfrias/arena.nvim](https://github.com/dzfrias/arena.nvim) - 智能（基于频率）缓冲区切换器。
- [backdround/tabscope.nvim](https://github.com/backdround/tabscope.nvim) - 制作选项卡本地缓冲区。
- [akasataikisiti/tabLocalBuffer.nvim](https://github.com/akasataikisiti/tabLocalBuffer.nvim) - 保留每个选项卡的缓冲区列表，并提供其自己的 bnext / bprevious 样式导航，仅在当前选项卡内循环。
- [j-morano/buffer_manager.nvim](https://github.com/j-morano/buffer_manager.nvim) - 添加一个或多个缓冲区，对它们重新排序，将它们保存在文件中，或者从一个小的浮动窗口中轻松删除它们。
- [kazhala/close-buffers.nvim](https://github.com/kazhala/close-buffers.nvim) - 根据不同的情况删除多个Vim缓冲区。
- [sQVe/bufignore.nvim](https://github.com/sQVe/bufignore.nvim) - 取消列出与指定忽略源匹配的隐藏缓冲区。
- [rgroli/other.nvim](https://github.com/rgroli/other.nvim) - 打开当前缓冲区的替代文件。
- [chrisgrieser/nvim-early-retirement](https://github.com/chrisgrieser/nvim-early-retirement) - 通过在 x 分钟不活动后自动关闭缓冲区，将缓冲区送入提前退休状态。
- [axkirillov/hbac.nvim](https://github.com/axkirillov/hbac.nvim) - 自动关闭您不使用的缓冲区。
- [ChuufMaster/buffer-vacuum](https://github.com/ChuufMaster/buffer-vacuum) - 设置保持打开状态的最大缓冲区数量，并智能删除超过最大数量的最旧缓冲区。
- [mong8se/buffish.nvim](https://github.com/mong8se/buffish.nvim) - 一种以酒或醋为精神的缓冲液切换器。
- [BibekBhusal0/bufstack.nvim](https://github.com/BibekBhusal0/bufstack.nvim) - 跟踪最近访问的缓冲区并重新打开最近关闭的缓冲区。
- [francescarpi/buffon.nvim](https://github.com/francescarpi/buffon.nvim) - 缓冲导航、重组和关闭。
- [ahkohd/buffer-sticks.nvim](https://github.com/ahkohd/buffer-sticks.nvim) - 化妆品缓冲区指示器和选择器。
- [famiu/bufdelete.nvim](https://github.com/famiu/bufdelete.nvim) - 删除缓冲区而不丢失窗口布局。
- [wsdjeg/bufdel.nvim](https://github.com/wsdjeg/bufdel.nvim) - 删除缓冲区而不更改窗口布局。
- [m-demare/attempt.nvim](https://github.com/m-demare/attempt.nvim) - 管理和运行临时缓冲区。
<!--lint disable double-link -->
[**⬆ 回到顶部**](#contents)
<!--lint enable double-link -->

## 颜色

- [catgoose/nvim-colorizer.lua](https://github.com/catgoose/nvim-colorizer.lua) - 没有外部依赖性的高性能彩色荧光笔。
- [winston0410/range-highlight.nvim](https://github.com/winston0410/range-highlight.nvim) - 一个非常轻量级的插件（〜120loc），突出显示您在命令行中输入的范围。
- [folke/twilight.nvim](https://github.com/folke/twilight.nvim) - 使用 Tree-sitter 使您正在编辑的代码的非活动部分变暗。
- [uga-rosa/ccc.nvim](https://github.com/uga-rosa/ccc.nvim) - 超级强大的颜色选择器/着色器插件。
- [lcheylus/overlength.nvim](https://github.com/lcheylus/overlength.nvim) - 一个小插件，用于突出显示太长的行。
- [max397574/colortils.nvim](https://github.com/max397574/colortils.nvim) - 提供处理颜色的实用程序（选择器、转换）。
- [Mr-LLLLL/interestingwords.nvim](https://github.com/Mr-LLLLL/interestingwords.nvim) - 同时突出显示多个单词，并通过平滑滚动导航光标下的单词，在虚拟文本中显示搜索计数。
- [nvim-mini/mini.nvim#mini.hipatterns](https://github.com/nvim-mini/mini.nvim/blob/main/readmes/mini-hipatterns.md) - “mini.nvim”模块，用于使用可配置的荧光笔突出显示文本中的模式。与可配置的去抖延迟异步工作。
- [miversen33/sunglasses.nvim](https://github.com/miversen33/sunglasses.nvim) - 窗口切换时的动态配色方案/高亮调整器。
- [rasulomaroff/reactive.nvim](https://github.com/rasulomaroff/reactive.nvim) - 设置全局和特定于窗口的突出显示或在模式/操作符更改或窗口切换时触发回调。
- [moyiz/command-and-cursor.nvim](https://github.com/moyiz/command-and-cursor.nvim) - 进入命令模式时突出显示光标和视觉选择。
- [rachartier/tiny-devicons-auto-colors.nvim](https://github.com/rachartier/tiny-devicons-auto-colors.nvim) - 根据您当前的配色方案自动更新 nvim-web-devicons 颜色。
- [TaDaa/vimade](https://github.com/TaDaa/vimade) - 在窗口和缓冲区中调暗、淡入淡出、着色、动画和自定义颜色。
- [xzbdmw/colorful-menu.nvim](https://github.com/xzbdmw/colorful-menu.nvim) - 使用 Tree-sitter 为您的自动完成菜单着色。
- [nvzone/minty](https://github.com/nvzone/minty) - 制作精美的色彩工具。
- [3ZsForInsomnia/pacer.nvim](https://github.com/3ZsForInsomnia/pacer.nvim) - 通过一次突出显示一个单词并调暗当前段落之外的所有文本来创建阅读节奏 - 有些可以帮助您更快地阅读。
- [wsdjeg/cpicker.nvim](https://github.com/wsdjeg/cpicker.nvim) - 一个轻量级的调色板插件，支持多种颜色模型。
- [leolaurindo/tunnelvision.nvim](https://github.com/leolaurindo/tunnelvision.nvim) - 通过调暗不相关的线条，一次专注于一个符号。
<!--lint disable double-link -->
[**⬆ 回到顶部**](#contents)
<!--lint enable double-link -->

## 配色方案

每个配色方案都将具有下面列出的一个或多个标签。如果缺少标签
那么不支持：

<!--lint disable awesome-list-item-->
- **_`[TS]`_** - 有树保姆突出显示。
- **_`[LSP]`_** - 具有 LSP 语义标记支持。
- **_`[L/D]`_** - 有“浅色”和“深色”两种变体。
- **_`[Lua]`_** - 用 Lua 编写。
- **_`[Fnl]`_** - 用茴香写成。
<!--lint enable awesome-list-item-->

- [ThorstenRhau/token](https://github.com/ThorstenRhau/token) - **_`[TS][LSP][L/D][Lua]`_** Token 具有温暖的色调和仔细的对比，具有完整的 Tree-sitter 和 LSP 集成。
- [oskarnurm/koda.nvim](https://github.com/oskarnurm/koda.nvim) - **_`[TS][LSP][L/D][Lua]`_** 代码的安静伴侣。用 Lua 编写的极简配色方案。
- [yonatan-perel/lake-dweller.nvim](https://github.com/yonatan-perel/lake-dweller.nvim) - **_`[TS][LSP][Lua]`_** 黑暗且固执己见，选择性突出显示，旨在一目了然。
- [silentium-theme/silentium.nvim](https://github.com/silentium-theme/silentium.nvim) - **_`[TS][Luа]`_** 务实的单色主题，旨在通过仅突出显示需要的内容来提高阅读速度并减少眼睛疲劳。
- [serhez/teide.nvim](https://github.com/serhez/teide.nvim) - **_`[TS][LSP][L/D][Lua]`_** Folke 的 `tokyonight.nvim` 的一个分支，具有不同的调色板。
- [kuri-sun/yoda.nvim](https://github.com/kuri-sun/yoda.nvim) - **_`[TS][L/D][Lua]`_** 柔和的绿色调色板，用于集中、平衡的编辑。
- [wurli/cobalt.nvim](https://github.com/wurli/cobalt.nvim) - **_`[TS][LSP][Lua]`_** TextMate 经典蓝色主题的（大部分）忠实移植。
- [datsfilipe/min-theme.nvim](https://github.com/datsfilipe/min-theme.nvim) - **_`[TS][LSP][Lua]`_** 它是 Min 的端口，是 VSCode 的最小主题，用 Lua 编写。
- [github-main-user/lytmode.nvim](https://github.com/github-main-user/lytmode.nvim) - **_`[TS][LSP][Lua]`_** 受 Obsidian LYT-Mode 启发的独特中间主题。不太暗，也不太亮——刚刚好。
- [datsfilipe/vesper.nvim](https://github.com/datsfilipe/vesper.nvim) - **_`[TS][LSP][Lua]`_** 它是流行的 VS Code 主题 Vesper 的端口，用 Lua 编写。
- [sontungexpt/witch](https://github.com/sontungexpt/witch) - **_`[TS][LSP][L/D][Lua]`_** 主要 stinvim 发行版颜色方案包括调暗非活动窗口的默认功能，以及供用户使用的各种其他自定义选项。
- [Abstract-IDE/Abstract-cs](https://github.com/Abstract-IDE/Abstract-cs) - **_`[TS][LSP][Lua]`_** 用 Lua 编写的配色方案，专为 roshnivim 制作，支持 Tree-sitter。
- [rafamadriz/neon](https://github.com/rafamadriz/neon) - **_`[TS][LSP][L/D][Lua]`_** 可定制的配色方案，具有出色的斜体和粗体支持、深色和浅色变体。与 Tree-sitter 一起使用且美观。
- [tomasiser/vim-code-dark](https://github.com/tomasiser/vim-code-dark) - **_`[TS]`_** 深色配色方案很大程度上受到 VSCode 的 Dark+ 方案外观的启发。
- [Mofiqul/vscode.nvim](https://github.com/Mofiqul/vscode.nvim) - **_`[TS][L/D][Lua]`_** vim-code-dark 颜色方案的 Lua 端口，带有 VSCode 浅色和深色主题。
- [askfiy/visual_studio_code](https://github.com/askfiy/visual_studio_code) - **_`[TS][LSP][L/D][Lua]`_** 一个高度还原VSCode的主题。
- [marko-cerovac/material.nvim](https://github.com/marko-cerovac/material.nvim) - **_`[TS][LSP][L/D][Lua]`_** Material.nvim 是一个用 Lua 编写并基于材质调色板的高度可配置的颜色方案。
- [bluz71/vim-nightfly-colors](https://github.com/bluz71/vim-nightfly-colors) - **_`[TS][LSP][Lua]`_** 带有 Tree-sitter 支持的黑暗午夜配色方案。
- [bluz71/vim-moonfly-colors](https://github.com/bluz71/vim-moonfly-colors) - **_`[TS][LSP][Lua]`_** 带有 Tree-sitter 支持的深木炭配色方案。
- [ChristianChiarulli/nvcode-color-schemes.vim](https://github.com/ChristianChiarulli/nvcode-color-schemes.vim) - **_`[TS]`_** Nvcode、onedark、nord 颜色方案，支持 Tree-sitter。
- [folke/tokyonight.nvim](https://github.com/folke/tokyonight.nvim) - **_`[TS][LSP][L/D][Lua]`_** 用 Lua 编写的干净、深色和浅色主题，支持 LSP、Tree-sitter 和大量插件。
- [everviolet/nvim](https://github.com/everviolet/nvim) - **_`[TS][LSP][L/D][Lua]`_** 舒适的配色方案，适合舒适的早晨编码。
- [uhs-robert/oasis.nvim](https://github.com/uhs-robert/oasis.nvim) - **_`[TS][LSP][L/D][Lua]`_** Vim 的沙漠主题移植到 Neovim 并通过 12 个变体变得现代，这是彩虹每种颜色的黑暗主题的集合。
- [sainnhe/sonokai](https://github.com/sainnhe/sonokai) - **_`[TS][LSP]`_** 基于 Monokai Pro 的高对比度和鲜艳的配色方案。
- [nyoom-engineering/oxocarbon.nvim](https://github.com/nyoom-engineering/oxocarbon.nvim) - **_`[TS][LSP][L/D][Lua]`_** 用 Fennel 编写的深色和浅色主题，灵感来自 IBM Carbon。
- [mhartington/oceanic-next](https://github.com/mhartington/oceanic-next) - **_`[TS][L/D]`_** 海洋下一个主题。
- [nvimdev/zephyr-nvim](https://github.com/nvimdev/zephyr-nvim) - **_`[TS][Lua]`_** 带有 Tree-sitter 支持的深色方案。
- [rockerBOO/boo-colorscheme-nvim](https://github.com/rockerBOO/boo-colorscheme-nvim) - **_`[TS][Lua]`_** 一个为 LSP、Tree-sitter 手工支持的配色方案。
- [jim-at-jibba/ariake.nvim](https://github.com/jim-at-jibba/ariake.nvim) - **_`[TS][LSP][Lua]`_** 伟大的 Atom 主题的端口。美丽的深色配色方案。
- [Th3Whit3Wolf/onebuddy](https://github.com/Th3Whit3Wolf/onebuddy) - **_`[TS][L/D][Lua]`_** 光明与黑暗原子同一个主题。
- [ishan9299/modus-theme-vim](https://github.com/ishan9299/modus-theme-vim) - **_`[TS][L/D][Lua]`_** 这是 Protesilaos Stavrou 为 emacs 开发的配色方案。
- [sainnhe/edge](https://github.com/sainnhe/edge) - **_`[TS][LSP][L/D]`_** 受 Atom One 和 Material 启发的干净优雅的配色方案。
- [bkegley/gloombuddy](https://github.com/bkegley/gloombuddy) - **_`[TS][Lua]`_** 忧郁主题。
- [Th3Whit3Wolf/one-nvim](https://github.com/Th3Whit3Wolf/one-nvim) - **_`[TS][L/D][Lua]`_** Atom One 启发了深色和浅色配色方案。
- [Th3Whit3Wolf/space-nvim](https://github.com/Th3Whit3Wolf/space-nvim) - **_`[TS][L/D][Lua]`_** 受 spacemacs 启发的深色和浅色配色方案。
- [ray-x/aurora](https://github.com/ray-x/aurora) - **_`[TS][LSP][Lua]`_** 一个 24 位深色主题，支持 Tree-sitter 和 LSP。
- [ray-x/starry.nvim](https://github.com/ray-x/starry.nvim) - **_`[TS][LSP][L/D][Lua]`_** 现代配色方案的集合：`material`、`moonlight`、`dracula (blood)`、`monokai`、`mariana`、`emerald`、`earlysummer`、`middlenight_blue`、`darksolar`。
- [tanvirtin/monokai.nvim](https://github.com/tanvirtin/monokai.nvim) - **_`[TS][LSP][Lua]`_** 用 Lua 编写的 Monokai 主题。
- [ofirgall/ofirkai.nvim](https://github.com/ofirgall/ofirkai.nvim) - **_`[TS][LSP][Lua]`_** Monokai 主题，旨在感觉像 Sublime Text。
- [savq/melange-nvim](https://github.com/savq/melange-nvim) - **_`[TS][LSP][L/D][Lua]`_** 用 Lua 编写的暖色方案，支持各种终端模拟器。
- [fenetikm/falcon](https://github.com/fenetikm/falcon) - **_`[TS][Lua]`_** 终端、Vim 和朋友的配色方案。
- [andersevenrud/nordic.nvim](https://github.com/andersevenrud/nordic.nvim) - **_`[TS][Lua]`_** 北欧风格的配色方案。
- [AlexvZyl/nordic.nvim](https://github.com/AlexvZyl/nordic.nvim) - **_`[TS][Lua]`_** Nord 主题，但更温暖、更黑暗。支持多种插件和其他平台。
- [shaunsingh/nord.nvim](https://github.com/shaunsingh/nord.nvim) - **_`[TS][Lua]`_** 基于 Nord 调色板的配色方案。
- [Tsuzat/NeoSolarized.nvim](https://github.com/Tsuzat/NeoSolarized.nvim) - **_`[TS][LSP][L/D][Lua]`_** NeoSolarized 完全透明的配色方案。
- [svrana/neosolarized.nvim](https://github.com/svrana/neosolarized.nvim) - **_`[TS][LSP][Lua]`_** 使用 colorbuddy 的深色日光配色方案，可轻松定制。
- [ishan9299/nvim-solarized-lua](https://github.com/ishan9299/nvim-solarized-lua) - **_`[TS][Lua]`_** 用 Lua 编写的曝光配色方案。
- [jthvai/lavender.nvim](https://codeberg.org/jthvai/lavender.nvim) - **_`[TS][LSP][Lua]`_** 紫色深色模式配色方案；完全重写 shaunsingh/moonlight.nvim。
- [navarasu/onedark.nvim](https://github.com/navarasu/onedark.nvim) - **_`[TS][LSP][Lua]`_** 基于 Atom 的 One Dark 主题，用 Lua 编写的 One Dark 主题。
- [sainnhe/gruvbox-material](https://github.com/sainnhe/gruvbox-material) - **_`[TS][LSP]`_** Gruvbox 修改，具有更柔和的对比度和 Tree-sitter 支持。
- [sainnhe/everforest](https://github.com/sainnhe/everforest) - **_`[TS][LSP][L/D]`_** 基于绿色的配色方案，旨在温暖、柔和且养眼。
- [neanias/everforest-nvim](https://github.com/neanias/everforest-nvim) - **_`[TS][LSP][L/D][Lua]`_** Everforest 配色方案的 Lua 端口。
- [NTBBloodbath/doom-one.nvim](https://github.com/NTBBloodbath/doom-one.nvim) - **_`[TS][L/D][Lua]`_** doom-emacs 的 doom-one 的 Lua 端口。
- [dracula/vim](https://github.com/dracula/vim) - **_`[TS][LSP]`_** 著名的美丽黑暗动力主题。
- [Mofiqul/dracula.nvim](https://github.com/Mofiqul/dracula.nvim) - **_`[TS]`_** 用 Lua 编写的 Dracula 配色方案。
- [niyabits/calvera-dark.nvim](https://github.com/niyabits/calvera-dark.nvim) - **_`[TS][Lua]`_** [VSCode Calvara Dark](https://github.com/saurabhdaware/vscode-calvera-dark) 主题的端口，支持 Tree-sitter 和许多其他插件。
- [nxvu699134/vn-night.nvim](https://github.com/nxvu699134/vn-night.nvim) - **_`[Lua]`_** 用 Lua 编写的深色配色方案。
- [adisen99/codeschool.nvim](https://github.com/adisen99/codeschool.nvim) - **_`[TS][LSP][Lua]`_** 用 Lua 编写的 Codeschool 颜色方案，具有 Tree-sitter 和内置 LSP 支持。
- [projekt0n/github-nvim-theme](https://github.com/projekt0n/github-nvim-theme) - **_`[TS][LSP][L/D][Lua]`_** 一个 GitHub 主题，kitty，用 Lua 编写的 alacritty。支持内置LSP和Tree-sitter。
- [kdheepak/monochrome.nvim](https://github.com/kdheepak/monochrome.nvim) - **_`[TS][Lua]`_** 一种 16 位单色配色方案，使用 [HSLuv](https://www.hsluv.org/) 实现感知上不同的灰色，支持 Tree-sitter 和其他常用插件。
<!--lint disable awesome-spell-check-->
- [rose-pine/neovim](https://github.com/rose-pine/neovim) - **_`[TS][LSP][L/D][Lua]`_** 所有天然松木、人造毛皮和一点 soho 氛围，适合优雅的极简主义者。
<!--lint enable awesome-spell-check-->
- [zenbones-theme/zenbones.nvim](https://github.com/zenbones-theme/zenbones.nvim) - **_`[TS][LSP][L/D][Lua]`_** Vim/Neovim 颜色方案的集合，旨在使用对比度和字体变化突出显示代码。
- [catppuccin/nvim](https://github.com/catppuccin/nvim) - **_`[TS][LSP][L/D][Lua]`_** 温暖的中调深色主题，展现充满活力的自我！支持本机 LSP、Tree-sitter 等。
- [samesense/savitsky.nvim](https://github.com/samesense/savitsky.nvim) - **_`[TS][LSP][L/D][Lua]`_** 精心策划的调色板，灵感来自萨维茨基博物馆的绘画，建立在“catppuccin”之上。
- [FrenzyExists/aquarium-vim](https://github.com/FrenzyExists/aquarium-vim) - **_`[TS][L/D]`_** 深色但充满活力的配色方案。
- [EdenEast/nightfox.nvim](https://github.com/EdenEast/nightfox.nvim) - **_`[TS][LSP][L/D][Lua]`_** 柔和的深色、完全可定制的配色方案，支持 LSP、Tree-sitter 和各种插件。
- [ldelossa/vimdark](https://github.com/ldelossa/vimdark) - **_`[TS][L/D]`_** 适合夜间的最小 Vim 主题。松散地基于 vim-monotonic 和 chrome 的深色阅读器扩展。白天还包括浅色主题。
- [Everblush/nvim](https://github.com/Everblush/nvim) - **_`[TS][LSP][Lua]`_** 用 Lua 编写的深色、充满活力且美丽的配色方案。
- [adisen99/apprentice.nvim](https://github.com/adisen99/apprentice.nvim) - **_`[TS][L/D][Lua]`_** 基于 [Apprentice](https://github.com/romainl/Apprentice) 调色板用 Lua 编写的颜色方案，具有 Tree-sitter 和内置 LSP 支持。
- [olimorris/onedarkpro.nvim](https://github.com/olimorris/onedarkpro.nvim) - **_`[TS][L/D][Lua]`_** Atom 标志性的 One Dark 主题。可缓存、完全可定制、Tree-sitter 和 LSP 语义令牌支持。有浅色和深色两种版本。
- [rmehri01/onenord.nvim](https://github.com/rmehri01/onenord.nvim) - **_`[TS][LSP][L/D][Lua]`_** 一种结合了 Nord 和 Atom One Dark 调色板的配色方案，可提供更生动的编程体验。
- [nvim-mini/mini.nvim#colorschemes](https://github.com/nvim-mini/mini.nvim#plugin-color-schemes) - **_`[TS][LSP][L/D][Lua]`_** `mini.nvim` 中包含的配色方案。它们都优先考虑高对比度，以便在感知统一的色彩空间中读取文本和计算调色板。
- [luisiacc/gruvbox-baby](https://github.com/luisiacc/gruvbox-baby) - **_`[TS][LSP][Lua]`_** 具有完整 Tree-sitter 支持的现代 gruvbox 主题。
- [titanzero/zephyrium](https://github.com/titanzero/zephyrium) - **_`[TS][Lua]`_** 一个和风风格的主题，用 Lua 编写，支持 Tree-sitter。
- [rebelot/kanagawa.nvim](https://github.com/rebelot/kanagawa.nvim) - **_`[TS][LSP][L/D][Lua]`_** 受葛饰北斋名画颜色启发的深色配色方案。
- [thesimonho/kanagawa-paper.nvim](https://github.com/thesimonho/kanagawa-paper.nvim) - **_`[TS][LSP][L/D][Lua]`_** 将神奈川的浅色和深色配色方案与柔和的颜色重新混合。
- [kevinm6/kurayami.nvim](https://github.com/kevinm6/kurayami.nvim) - **_`[TS][LSP][Lua]`_** 仅深色主题，支持 Tree-sitter。
- [cpea2506/one_monokai.nvim](https://github.com/cpea2506/one_monokai.nvim) - **_`[TS][LSP][Lua]`_** 一个用 Lua 编写的 Monokai 主题。
- [phha/zenburn.nvim](https://github.com/phha/zenburn.nvim) - **_`[TS][Lua]`_** 低对比度深色方案，支持各种插件。
- [chrsm/paramount-ng.nvim](https://github.com/chrsm/paramount-ng.nvim) - **_`[TS][Lua]`_** 使用 Lush 编写的深色配色方案。支持护树人。
- [qaptoR-nvim/chocolatier.nvim](https://github.com/qaptoR-nvim/chocolatier.nvim) - **_`[TS][LSP][Lua]`_** 受 espresso/kimbie 启发的巧克力主题，改编自 ellisonleao/gruvbox.nvim 主题作为代码模板。
- [rockyzhang24/arctic.nvim](https://github.com/rockyzhang24/arctic.nvim) - **_`[TS][LSP][Lua]`_** 从 VSCode Dark+ 主题移植的配色方案，为编辑器和 UI 提供严格且精确的颜色选择。
- [ramojus/mellifluous.nvim](https://github.com/ramojus/mellifluous.nvim) - **_`[TS][LSP][L/D][Lua]`_** 令人愉悦且富有成效的配色方案。
- [lewpoly/sherbet.nvim](https://github.com/lewpoly/sherbet.nvim) - **_`[TS][Lua]`_** 舒缓的配色方案，支持流行的插件和 Tree-sitter。
- [Mofiqul/adwaita.nvim](https://github.com/Mofiqul/adwaita.nvim) - **_`[TS][LSP][L/D][Lua]`_** 基于 GNOME Adwaita 语法的颜色方案，支持流行的插件。
- [mellow-theme/mellow.nvim](https://github.com/mellow-theme/mellow.nvim) - **_`[TS][LSP][Lua]`_** 舒缓的深色配色方案，支持 Tree-sitter。
- [gbprod/nord.nvim](https://github.com/gbprod/nord.nvim) - **_`[TS][LSP][Lua]`_** 北极、北蓝、干净优雅的主题，基于 Nord Palette。
- [embark-theme/vim](https://github.com/embark-theme/vim) - **_`[TS]`_** 采用明亮色彩的深墨紫色主题。
- [nyngwang/nvimgelion](https://github.com/nyngwang/nvimgelion) - **_`[TS]`_** 新世纪福音战士但适用于 Vimmers。
- [maxmx03/fluoromachine.nvim](https://github.com/maxmx03/fluoromachine.nvim) - **_`[TS][LSP][Lua]`_** Synthwave x Fluoromachine 端口。
- [dasupradyumna/midnight.nvim](https://github.com/dasupradyumna/midnight.nvim) - **_`[TS][LSP][Lua]`_** 现代黑色主题，具有舒适的色彩对比，带来愉悦的视觉体验，并支持 LSP 和 Tree-sitter。
- [sonjiku/yawnc.nvim](https://github.com/sonjiku/yawnc.nvim) - **_`[TS][LSP][Lua]`_** 使用 pywal 进行主题化，并带有 Base16 风格。
- [uncleTen276/dark_flat.nvim](https://github.com/uncleTen276/dark_flat.nvim) - **_`[TS][LSP][Lua]`_** 一个用 Lua 编写的配色方案，移植自 Dark Flat iTerm2 主题，支持 LSP 和 Tree-sitter。
- [zootedb0t/citruszest.nvim](https://github.com/zootedb0t/citruszest.nvim) - **_`[TS][LSP][Lua]`_** 一种配色方案，其特点是明亮多汁的颜色组合，让人想起各种柑橘类水果，并具有 LSP 和 Tree-sitter 支持。
- [2nthony/vitesse.nvim](https://github.com/2nthony/vitesse.nvim) - **_`[TS][LSP][Lua]`_** Vitesse 主题 Lua 端口。
- [xero/miasma.nvim](https://github.com/xero/miasma.nvim) - **_`[TS][LSP]`_** 受树林启发的深色柔和配色方案。使用 lush 构建，支持 Tree-sitter、诊断、CMP、Git-Signs、Telescope、Which-key、Lazy 等。
- [Verf/deepwhite.nvim](https://github.com/Verf/deepwhite.nvim) - **_`[TS][LSP][Lua]`_** 受 [flatwhite-syntax](https://github.com/biletskyy/flatwhite-syntax) 和 [elegant-emacs](https://github.com/rougier/elegant-emacs) 启发的浅色方案。
- [judaew/ronny.nvim](https://github.com/judaew/ronny.nvim) - **_`[TS][LSP][Lua]`_** 深色配色方案，主要受到 Wimem Hazenberg 最初创建的 Monokai 的启发。
- [ribru17/bamboo.nvim](https://github.com/ribru17/bamboo.nvim) - **_`[TS][LSP][Lua]`_** 温暖的绿色主题。
- [cryptomilk/nightcity.nvim](https://github.com/cryptomilk/nightcity.nvim) - **_`[TS][LSP][Lua]`_** 受 Inkpot、Jellybeans、Gruvbox 和 Tokyonight 启发的深色配色方案，并支持 LSP。
- [polirritmico/monokai-nightasty.nvim](https://github.com/polirritmico/monokai-nightasty.nvim) - **_`[TS][LSP][L/D][Lua]`_** 一个基于 Lua 编写的 Monokai 调色板的深色/浅色主题，支持 LSP、Tree-sitter 和大量插件。
- [oxfist/night-owl.nvim](https://github.com/oxfist/night-owl.nvim) - **_`[TS][LSP][Lua]`_** [来自 VSCode 的 Night Owl colorcheme 端口](https://github.com/sdras/night-owl-vscode-theme)，支持 Tree-sitter 和语义标记。
- [micdzu/aalto.nvim](https://github.com/micdzu/aalto.nvim) - **_`[TS][LSP][L/D][Lua]`_** 具有感知 OKLCH 引擎的语义配色方案，具有四种语义角色以及深色和浅色变体。
- [miikanissi/modus-themes.nvim](https://github.com/miikanissi/modus-themes.nvim) - **_`[TS][LSP][L/D][Lua]`_** 无障碍主题，符合色彩对比度最高标准（WCAG AAA）。
- [alexmozaidze/palenight.nvim](https://github.com/alexmozaidze/palenight.nvim) - **_`[TS][LSP][Fnl]`_** Palenight 颜色方案支持 Tree-sitter、LSP _（包括语义标记）_ 和许多插件。
- [scottmckendry/cyberdream.nvim](https://github.com/scottmckendry/cyberdream.nvim) - **_`[TS][L/D][Lua]`_** 高对比度、未来主义和充满活力的色彩方案。
- [HoNamDuong/hybrid.nvim](https://github.com/HoNamDuong/hybrid.nvim) - **_`[TS][LSP][Lua]`_** 用 Lua 编写的黑暗主题。
- [sxwpb/halfspace.nvim](https://gitlab.com/sxwpb/halfspace.nvim) - **_`[TS][LSP][Lua]`_** 一种半浅色方案，可最大限度地减少眼睛融化。
- [bartekjaszczak/distinct-nvim](https://gitlab.com/bartekjaszczak/distinct-nvim) - **_`[TS][LSP][L/D][Lua]`_** 具有不同语法颜色的主题。支持 Tree-sitter 和语义突出显示。适合喜欢多色语法突出显示的人。
- [samharju/synthweave.nvim](https://github.com/samharju/synthweave.nvim) - **_`[TS][LSP][Lua]`_** Synthwave '84 颜色方案端口。
- [loganswartz/sunburn.nvim](https://github.com/loganswartz/sunburn.nvim) - **_`[TS][Lua]`_** 介于柔和色和日光色之间的配色方案，首先强调可读性和色调均匀性。
- [ptdewey/darkearth-nvim](https://github.com/ptdewey/darkearth-nvim) - **_`[TS][LSP][Fnl]`_** 一种支持 Tree-sitter 和 LSP 的深色和土色配色方案。
- [uloco/bluloco.nvim](https://github.com/uloco/bluloco.nvim) - **_`[TS][LSP][L/D][Lua]`_** 用于夜间和白天编码的精美而复杂的配色方案。支持 LSP、Tree-sitter 和所有您喜欢的插件。
- [slugbyte/lackluster.nvim](https://github.com/slugbyte/lackluster.nvim) - **_`[TS][LSP][Lua]`_** 一种令人愉快的灰度配色方案，对眼睛柔和，并且支持大量插件。
- [0xstepit/flow.nvim](https://github.com/0xstepit/flow.nvim) - **_`[TS][L/D][Lua]`_** 精心设计的颜色可帮助编码期间聚焦以及荧光细节。支持许多插件和工具。
- [samharju/serene.nvim](https://github.com/samharju/serene.nvim) - **_`[TS][Lua]`_** 舒缓且黑暗的 Tree-sitter/LSP 支持主题，可在使用更鲜艳的配色方案后放松您的眼睛。
- [killitar/obscure.nvim](https://github.com/killitar/obscure.nvim) - **_`[TS][LSP][Lua]`_** 受调色板 Mellow 启发的柔和深色配色方案。支持 Tree-sitter、LSP _（包括语义标记）_ 和许多插件。
- [bakageddy/alduin.nvim](https://github.com/bakageddy/alduin.nvim) - **_`[TS][LSP][Lua]`_** [alduin](https://github.com/AlessandroYorba/alduin) 主题到 Lua 的端口，支持 Tree-sitter 和语义突出显示。
- [diegoulloao/neofusion.nvim](https://github.com/diegoulloao/neofusion.nvim) - **_`[TS][LSP][Lua]`_** 与 Tree-sitter 兼容的主题，灵感来自 `gruvbox.nvim`。
- [bartekjaszczak/luma-nvim](https://gitlab.com/bartekjaszczak/luma-nvim) - **_`[TS][LSP][L/D][Lua]`_** 色彩缤纷的主题，具有暗/亮模式和可调节对比度。支持 Tree-sitter 和语义突出显示。
- [bartekjaszczak/finale-nvim](https://gitlab.com/bartekjaszczak/finale-nvim) - **_`[TS][LSP][Lua]`_** 平衡的深色主题，融合生动和柔和的色彩，带来舒适、高对比度的体验。支持 Tree-sitter 和语义突出显示。
- [m15a/nvim-srcerite](https://codeberg.org/m15a/nvim-srcerite) - **_`[TS][Lua]`_** 受 [Srcery](https://srcery.sh/) 启发的配色方案，基于 `nvim-highlite`。
- [neko-night/nvim](https://github.com/neko-night/nvim) - **_`[TS][LSP][L/D][Lua]`_** 适合各种品味和心情的色彩方案自助餐。
- [ptdewey/monalisa-nvim](https://github.com/ptdewey/monalisa-nvim) - **_`[TS][LSP][Lua]`_** 受蒙娜丽莎启发的深色多彩配色方案。
- [ntk148v/slack.nvim](https://github.com/ntk148v/slack.nvim) - **_`[TS][L/D][Lua]`_** 移植的 Slack 配色方案。
- [y3owk1n/base16-pro-max.nvim](https://github.com/y3owk1n/base16-pro-max.nvim) - **_`[TS][LSP][Lua]`_** 适用于现代 Neovim 的 Base16 — 不仅仅是颜色。
- [ellisonleao/gruvbox.nvim](https://github.com/ellisonleao/gruvbox.nvim) - **_`[TS][LSP][L/D][Lua]`_** Gruvbox 社区颜色方案 Lua 端口。
- [pmouraguedes/neodarcula.nvim](https://github.com/pmouraguedes/neodarcula.nvim) - **_`[TS][LSP][Lua]`_** 深色主题，支持透明度、调光、LSP 语义标记等。
- [jpwol/thorn.nvim](https://github.com/jpwol/thorn.nvim) - **_`[TS][LSP][L/D][Lua]`_** 丰富的绿色主题，带有深色和浅色选项。支持 LSP、透明度、许多插件等等。
- [calind/selenized.nvim](https://github.com/calind/selenized.nvim) - **_`[TS][LSP][L/D][Lua]`_** [selenized](https://github.com/jan-warchol/selenized) 的 Lua 端口，支持 Tree-sitter、`nvim-cmp`、GitSigns 等。
- [motaz-shokry/gruvbox.nvim](https://gitlab.com/motaz-shokry/gruvbox.nvim) - **_`[TS][L/D][Lua]`_** 一个新的 gruvbox 主题，其硬变体具有不同的背景颜色，并带有 4 个变体。
- [pebeto/dookie.nvim](https://github.com/pebeto/dookie.nvim) - **_`[TS][Lua]`_** 受 Plan9 的 acme 编辑器启发的配色方案。
- [metalelf0/jellybeans-nvim](https://github.com/metalelf0/jellybeans-nvim) - **_`[TS][Lua]`_** jellybeans 配色方案的端口。
- [lalitmee/cobalt2.nvim](https://github.com/lalitmee/cobalt2.nvim) - **_`[Lua]`_** 使用 colorbuddy 的 cobalt2 颜色方案的端口。
- [dybdeskarphet/gruvbox-minimal.nvim](https://github.com/dybdeskarphet/gruvbox-minimal.nvim) - **_`[TS][L/D][Lua]`_** Gruvbox Material 主题，概念上受到 Alabaster 的启发。
- [taigrr/cyberpunk.nvim](https://github.com/taigrr/cyberpunk.nvim) - **_`[TS][LSP][Lua]`_** 深色霓虹灯配色方案，黑色背景上有绿色、青色、黄色和红色高光。
- [ankushbhagats/pastel.nvim](https://github.com/ankushbhagats/pastel.nvim) - **_`[TS][LSP][L/D][Lua]`_** 优雅的柔和色彩方案，具有高级定制、样式和集成。
- [0x-ximon/acario.nvim](https://github.com/0x-ximon/acario.nvim) - **_`[TS][LSP][L/D][Lua]`_** 干净、高对比度的 Doom Emacs Acario 主题的移植版。
- [hyperb1iss/silkcircuit](https://github.com/hyperb1iss/silkcircuit) - **_`[TS][LSP][L/D][Lua]`_** 充满活力的赛博朋克色彩系统，有五种变体，40 多个插件集成，符合 WCAG AA 标准。支持多种编辑器、终端和 CLI 工具。
- [T-b-t-nchos/Aquavium.nvim](https://github.com/T-b-t-nchos/Aquavium.nvim) - **_`[TS][Lua]`_** 水族馆主题配色方案，设计用于透明终端背景。
- [54L1M/Oshen.nvim](https://github.com/54L1M/Oshen.nvim) - **_`[TS][LSP][L/D][Lua]`_** 受到夜间深海水的启发，完全源自五种源颜色。
- [marekh19/meowsoot.nvim](https://github.com/marekh19/meowsoot.nvim) - **_`[TS][LSP][L/D][Lua]`_** 深粉色-青色-淡紫色配色方案，其中字符串为黄色和绿色永远不会达到代码。
<!--lint disable double-link -->
[**⬆ 回到顶部**](#contents)
<!--lint enable double-link -->

### 配色方案创建

- [tjdevries/colorbuddy.nvim](https://github.com/tjdevries/colorbuddy.nvim) - 配色方案助手。用Lua写的！快速简单的配色方案。
- [norcalli/nvim-base16.lua](https://github.com/norcalli/nvim-base16.lua) - 用于设置 base16 主题的编程 Lua 库。
- [rktjmp/lush.nvim](https://github.com/rktjmp/lush.nvim) - 将 Neovim 主题定义为 Lua 中的 DSL，并提供实时反馈。
- [Iron-E/nvim-highlite](https://github.com/Iron-E/nvim-highlite) - 一个对开发人员来说逻辑“精简”的配色方案生成器。
- [nvim-mini/mini.nvim#mini.base16](https://github.com/nvim-mini/mini.nvim/blob/main/readmes/mini-base16.md) - `mini.nvim` 模块，可快速实现手动提供的调色板的 base16 主题。
- [ThemerCorp/themer.lua](https://github.com/ThemerCorp/themer.lua) - 一个简单的荧光笔，带有大量的配色方案。它还能够为 Vim/Neovim 和其他支持的应用程序（例如“kitty”和“alacritty”）创建颜色方案。
- [nvim-mini/mini.nvim#mini.colors](https://github.com/nvim-mini/mini.nvim/blob/main/readmes/mini-colors.md) - `mini.nvim` 模块用于调整和保存任何配色方案。还可以对某些颜色空间之间的过渡和转换进行动画处理。
- [nvim-mini/mini.nvim#mini.hues](https://github.com/nvim-mini/mini.nvim/blob/main/readmes/mini-hues.md) - `mini.nvim` 模块用于生成可配置的配色方案。仅将背景和前景色作为必需参数。可以调整非基色、饱和度、强调色、插件集成的色调数量。
- [loganswartz/polychrome.nvim](https://github.com/loganswartz/polychrome.nvim) - 一个 colorcheme 微框架，支持直接以多种不同格式指定颜色（sRGB、HSL、Oklab、XYZ 等，具有智能色度剪辑）、实时编辑预览和简单的 DSL。
- [svermeulen/text-to-colorscheme](https://github.com/svermeulen/text-to-colorscheme) - 允许用户使用 OpenAI 的 GPT API 生成带有文本提示的颜色方案。
- [RRethy/base16-nvim](https://github.com/RRethy/base16-nvim) - 一个 Base16 配色方案生成器。包括对 Tree-sitter 和 LSP 高亮组的支持。
<!--lint disable double-link -->
[**⬆ 回到顶部**](#contents)
<!--lint enable double-link -->

### 配色方案切换器

- [DrKJeff16/which-colorscheme.nvim](https://github.com/DrKJeff16/which-colorscheme.nvim) - 使用自定义或自动生成的“which-key.nvim”绑定在颜色方案之间循环。
- [itsfernn/auto-gnome-theme.nvim](https://github.com/itsfernn/auto-gnome-theme.nvim) - 遵循 GNOME 系统的亮/暗模式的快速配色方案切换器（基于“gsetting 监视器”）。
- [flashcodes-themayankjha/fkthemes.nvim](https://github.com/flashcodes-themayankjha/fkthemes.nvim) - 一个用 Lua 编写的快速、轻量级且功能强大的主题切换器。
- [4e554c4c/darkman.nvim](https://github.com/4e554c4c/darkman.nvim) - 遵循 Linux 上的系统暗模式设置。
- [f-person/auto-dark-mode.nvim](https://github.com/f-person/auto-dark-mode.nvim) - 按照 macOS 上的系统外观进行操作。
- [zaldih/themery.nvim](https://github.com/zaldih/themery.nvim) - 一种像 VSCode 一样动态更改颜色方案的新方法。
- [linrongbin16/colorbox.nvim](https://github.com/linrongbin16/colorbox.nvim) - 将所有 Ultra 配色方案加载到您的 Neovim 播放器中。
- [CWood-sdf/pineapple](https://github.com/CWood-sdf/pineapple) - 无需离开终端即可在配置中安装任何颜色方案。收集互联网上的所有配色方案，并允许您在安装之前预览它们。
- [BrunoCiccarino/gardenal](https://github.com/BrunoCiccarino/gardenal) - Gardenal 是一个主题切换器，它允许用户创建键盘快捷键，一键在主题之间切换。
- [LmanTW/themify.nvim](https://github.com/LmanTW/themify.nvim/tree/main) - 受 Themery.nvim 和 Lazy.nvim 启发的轻量级颜色方案管理器和切换器。
- [nishu-murmu/ThemeSwitch.nvim](https://github.com/nishu-murmu/ThemeSwitch.nvim) - 轻量级配色方案切换器。
- [Erl-koenig/theme-hub.nvim](https://github.com/Erl-koenig/theme-hub.nvim) - 通过望远镜选择器管理和安装配色方案。
<!--lint disable double-link -->
[**⬆ 回到顶部**](#contents)
<!--lint enable double-link -->

## 条形图和线形图

- [Bekaboo/deadcolumn.nvim](https://github.com/Bekaboo/deadcolumn.nvim) - 动态显示您的颜色列。
- [ecthelionvi/NeoColumn.nvim](https://github.com/ecthelionvi/NeoColumn.nvim) - 可切换的颜色列突出显示特定字符​​。
- [m4xshen/smartcolumn.nvim](https://github.com/m4xshen/smartcolumn.nvim) - 不需要时隐藏颜色列。
- [utilyre/barbecue.nvim](https://github.com/utilyre/barbecue.nvim) - 类似 winbar 的 VSCode。
- [Bekaboo/dropbar.nvim](https://github.com/Bekaboo/dropbar.nvim) - 类似 IDE 的面包屑，开箱即用。
- [SmiteshP/nvim-navic](https://github.com/SmiteshP/nvim-navic) - 一个简单的状态栏/winbar 组件，使用 LSP 显示当前的代码上下文。
- [luukvbaal/statuscol.nvim](https://github.com/luukvbaal/statuscol.nvim) - 可配置的“状态列”，带有内置段和点击处理程序。
- [mawkler/hml.nvim](https://github.com/mawkler/hml.nvim) - 将 `H`/`M`/`L` 指示符添加到您的行号中。
- [neur1n/noline.nvim](https://github.com/neur1n/noline.nvim) - 完全可定制的条形和线条组件，没有预设或限制。
- [OXY2DEV/bars.nvim](https://github.com/OXY2DEV/bars.nvim) - 创建自定义状态行、状态列、选项卡和窗口栏的起点/指南。
- [zaakiy/line-justice.nvim](https://github.com/zaakiy/line-justice.nvim) - 同时显示绝对行号和相对行号。

### 状态线

- [NTBBloodbath/galaxyline.nvim](https://github.com/NTBBloodbath/galaxyline.nvim) - 一个用 Lua 编写的轻量级且超快速的状态行插件。
- [tjdevries/express_line.nvim](https://github.com/tjdevries/express_line.nvim) - 支持协同例程、功能和作业。
- [sontungexpt/witch-line](https://github.com/sontungexpt/witch-line) - 基于参考概念的极快状态线。
- [nvim-lualine/lualine.nvim](https://github.com/nvim-lualine/lualine.nvim) - 易于配置、速度极快的状态栏。
- [adelarsq/neoline.vim](https://github.com/adelarsq/neoline.vim) - 使用 Lua 的轻量状态行/选项卡插件。
- [ojroques/nvim-hardline](https://github.com/ojroques/nvim-hardline) - 受 [vim-airline](https://github.com/vim-airline/vim-airline) 启发的状态行/缓冲区，旨在尽可能轻量和简单。
- [beauwilliams/statusline.lua](https://github.com/beauwilliams/statusline.lua) - 用 Lua 编写的零配置最小状态行，具有出色的集成和惊人的速度。
- [tamton-aquib/staline.nvim](https://github.com/tamton-aquib/staline.nvim) - Lua 中的现代轻量级状态栏。主要使用unicode符号来显示信息。
- [windwp/windline.nvim](https://github.com/windwp/windline.nvim) - 下一代状态栏。动画状态线。
- [konapun/vacuumline.nvim](https://github.com/konapun/vacuumline.nvim) - 受航空公司启发的 Galaxyline 配置。
- [nvim-mini/mini.nvim#mini.statusline](https://github.com/nvim-mini/mini.nvim/blob/main/readmes/mini-statusline.md) - `mini.nvim` 模块用于最小且快速的状态行。支持根据窗口宽度改变内容。
- [b0o/incline.nvim](https://github.com/b0o/incline.nvim) - 轻量级浮动状态线，旨在与 Neovim 的新全局状态线一起使用。
- [rebelot/heirline.nvim](https://github.com/rebelot/heirline.nvim) - 围绕递归继承设计的简洁状态线，速度极快且用途广泛。
- [Zeioth/heirline-components.nvim](https://github.com/Zeioth/heirline-components.nvim) - 30 多个“heirline.nvim”组件可开箱即用地创建完美的用户界面。
- [yaocccc/nvim-lines.lua](https://github.com/yaocccc/nvim-lines.lua) - 快速、轻便、可定制的状态行和选项卡（缓冲区）。
- [MunifTanjim/nougat.nvim](https://github.com/MunifTanjim/nougat.nvim) - 超可扩展的状态行/选项卡/winbar。
- [Mr-LLLLL/lualine-ext.nvim](https://github.com/Mr-LLLLL/lualine-ext.nvim) - 显示有关 lualine 的更多信息。
- [mikesmithgh/git-prompt-string-lualine.nvim](https://github.com/mikesmithgh/git-prompt-string-lualine.nvim) - 将 git-prompt-string 添加到您的状态行。
- [sschleemilch/slimline.nvim](https://github.com/sschleemilch/slimline.nvim) - 一个纤细、简约、固执己见的 Lua 状态栏。
- [tajirhas9/muslim.nvim](https://github.com/tajirhas9/muslim.nvim) - 在您的状态栏中获取祈祷时间和有用的伊斯兰必需品。

### 表格线

- [romgrk/barbar.nvim](https://github.com/romgrk/barbar.nvim) - 一个带有可重新排序、自动调整大小、可点击选项卡、图标、漂亮的突出显示、排序命令和神奇的跳转到缓冲区模式的选项卡。
- [akinsho/bufferline.nvim](https://github.com/akinsho/bufferline.nvim) - 使用 Lua 构建的时髦缓冲区。
- [crispgm/nvim-tabline](https://github.com/crispgm/nvim-tabline) - 用 Lua 编写的 `tabline.vim` 的端口。
- [alvarosevilla95/luatab.nvim](https://github.com/alvarosevilla95/luatab.nvim) - 用 Lua 编写的简单表格。
- [johann2357/nvim-smartbufs](https://github.com/johann2357/nvim-smartbufs) - 智能缓冲区管理。
- [willothy/nvim-cokeline](https://github.com/willothy/nvim-cokeline) - 为具有成瘾性格的人提供缓冲线。
- [tomiis4/BufferTabs.nvim](https://github.com/tomiis4/BufferTabs.nvim) - 简单而花哨的标签。
- [nvim-mini/mini.nvim#mini.tabline](https://github.com/nvim-mini/mini.nvim/blob/main/readmes/mini-tabline.md) - “mini.nvim”模块用于最小选项卡，在一个选项卡的情况下显示列出的缓冲区，否则返回默认值。
- [rafcamlet/tabline-framework.nvim](https://github.com/rafcamlet/tabline-framework.nvim) - 用户友好的框架，只需几行代码即可构建您梦想的选项卡。
- [nanozuki/tabby.nvim](https://github.com/nanozuki/tabby.nvim) - 一个最小的、可配置的选项卡行，允许使用选项卡作为工作区多路复用器。

### 光标线

- [ya2s/nvim-cursorline](https://github.com/ya2s/nvim-cursorline) - 突出显示光标单词和行。
- [sontungexpt/stcursorword](https://github.com/sontungexpt/stcursorword) - 突出显示光标下的单词（“nvim-cursorline”的改进和紧凑版本）。
- [RRethy/vim-illuminate](https://github.com/RRethy/vim-illuminate) - 通过内置 LSP 支持突出显示光标下的单词。
- [nvim-mini/mini.nvim#mini.cursorword](https://github.com/nvim-mini/mini.nvim/blob/main/readmes/mini-cursorword.md) - `mini.nvim` 模块用于自动突出显示光标下的单词（在可定制的延迟后显示）。
- [mawkler/modicator.nvim](https://github.com/mawkler/modicator.nvim) - 光标行号模式指示器。根据 Vim 模式更改 `CursorLineNr` 高亮显示。
<!--lint disable double-link -->
[**⬆ 回到顶部**](#contents)
<!--lint enable double-link -->

## 启动

- [nvimdev/dashboard-nvim](https://github.com/nvimdev/dashboard-nvim) - 受 doom-emacs 启发的极简主义仪表板。
- [goolord/alpha-nvim](https://github.com/goolord/alpha-nvim) - 一个快速且高度可定制的欢迎程序，例如 [vim-startify](https://github.com/mhinz/vim-startify)/dashboard-nvim。
- [nvim-mini/mini.nvim#mini.starter](https://github.com/nvim-mini/mini.nvim/blob/main/readmes/mini-starter.md) - 用于启动屏幕的“mini.nvim”模块。显示的项目是完全可定制的，可以使用带有即时视觉反馈的前缀查询来完成项目选择。
- [henriquehbr/nvim-startup.lua](https://sr.ht/~henriquehbr/nvim-startup.lua) - 显示启动时间。
- [max397574/startup.nvim](https://github.com/max397574/startup.nvim) - 完全可定制的问候语。
- [TobinPalmer/Tip.nvim](https://github.com/TobinPalmer/Tip.nvim) - 获取有关启动的简单提示。
- [CWood-sdf/spaceport.nvim](https://github.com/CWood-sdf/spaceport.nvim) - 开始屏幕可让您快速进入项目。
- [mong8se/actually.nvim](https://github.com/mong8se/actually.nvim) - 加载您实际要加载的文件。
- [Kurama622/profile.nvim](https://github.com/Kurama622/profile.nvim) - 仪表板，类似于 GitHub 主页。
- [leo-alvarenga/homecoming.nvim](https://github.com/leo-alvarenga/homecoming.nvim) - 一个极其简单、可定制且舒适的仪表板，具有合理的默认值和零配置要求。
- [Amansingh-afk/milli.nvim](https://github.com/Amansingh-afk/milli.nvim) - 带有捆绑动画和自定义图像或 GIF 支持的动画 ASCII 初始屏幕。
<!--lint disable double-link -->
[**⬆ 回到顶部**](#contents)
<!--lint enable double-link -->

## 图标

- [nvim-tree/nvim-web-devicons](https://github.com/nvim-tree/nvim-web-devicons) - [vim-devicons](https://github.com/ryanoasis/vim-devicons) 的 Lua 分支。
- [nvim-mini/mini.nvim#mini.icons](https://github.com/nvim-mini/mini.nvim/blob/main/readmes/mini-icons.md) - `mini.nvim` 模块作为通用图标提供程序。使用固定的一组突出显示组。支持各种类别、图标和样式自定义、缓存以提高性能。与内置文件类型匹配集成。
- [2KAbhishek/nerdy.nvim](https://github.com/2KAbhishek/nerdy.nvim/) - 查找并插入最新的书呆子字体字形。
- [stephansama/fzf-nerdfont.nvim](https://github.com/stephansama/fzf-nerdfont.nvim) - 使用“fzf-lua”选择 Nerd 字体图标的选择器。
<!--lint disable double-link -->
[**⬆ 回到顶部**](#contents)
<!--lint enable double-link -->

## 媒体

- [ricmonmol/nvim-music-player](https://github.com/ricmonmol/nvim-music-player) - 一个简单的音乐播放器，由“mpv”提供支持，用 Python 编写，包括 Telescope 浏览器。
- [melMass/echo.nvim](https://github.com/melMass/echo.nvim) - 为您的编辑工作流程提供无缝的声音集成。
- [~elisoli/nekovim](https://git.sr.ht/~elisoli/nekovim) - 灵活的 Discord 丰富的存在。
- [edluffy/hologram.nvim](https://github.com/edluffy/hologram.nvim) - 跨平台终端图像查看器。适用于 macOS 和 Linux。
- [HakonHarnes/img-clip.nvim](https://github.com/HakonHarnes/img-clip.nvim) - 轻松地将图像嵌入到任何标记语言中，例如 LaTeX、Markdown 或 Typst。
- [ekickx/clipboard-image.nvim](https://github.com/ekickx/clipboard-image.nvim) - 允许从剪贴板粘贴图像。
- [niuiic/cp-image.nvim](https://github.com/niuiic/cp-image.nvim) - 从剪贴板粘贴图像并插入参考代码。
- [askfiy/nvim-picgo](https://github.com/askfiy/nvim-picgo) - 允许您将图像上传到图像床，从而可以从互联网上的任何位置查看图像。
- [davidgranstrom/scnvim](https://github.com/davidgranstrom/scnvim) - SuperCollider 的前端。
- [Chaitanyabsrip/present.nvim](https://github.com/Chaitanyabsprip/present.nvim) - 用 Lua 编写的演示插件。
- [3rd/image.nvim](https://github.com/3rd/image.nvim) - 通过kitty的图形协议或ueberzugpp添加图像支持。
- [adelarsq/image_preview.nvim](https://github.com/adelarsq/image_preview.nvim) - 基于终端图像协议支持的图像预览。
- [niuiic/code-shot.nvim](https://github.com/niuiic/code-shot.nvim) - 拍一张代码的照片。
- [AntonVanAssche/music-controls.nvim](https://github.com/AntonVanAssche/music-controls.nvim) - 快速控制您最喜爱的音乐播放器（Spotify、VLC 等）。
- [neo451/feed.nvim](https://github.com/neo451/feed.nvim) - 用 Lua 编写的网络提要阅读器（RSS、Atom、JSON 提要）。
- [vyfor/cord.nvim](https://github.com/vyfor/cord.nvim) - 高度可扩展的 Discord 丰富存在。
- [iamt4nk/smm.nvim](https://github.com/iamt4nk/smm.nvim) - 允许控制 Spotify 播放的小型 TUI。
- [sanjay-np/nvim-yt-player](https://github.com/sanjay-np/nvim-yt-player) - 通过 IPC 套接字使用“mpv”和“yt-dlp”播放 YouTube 音频。
- [T-b-t-nchos/FMP7.nvim](https://github.com/T-b-t-nchos/FMP7.nvim) - 控制FMP7并播放FM/SSG/PCM驱动音乐文件（仅适用于Windows）。
<!--lint disable double-link -->
[**⬆ 回到顶部**](#contents)
<!--lint enable double-link -->

## 做笔记

- [DaFi-1/tasknvim](https://github.com/DaFi-1/tasknvim) - 一个简单的生活和个人发展工具，有助于组织目标、跟踪习惯和提高生产力。
- [niuiic/todo.nvim](https://github.com/niuiic/todo.nvim) - 简单但功能强大的基于文本的 TODO 管理器。
- [flashcodes-themayankjha/Fknotes.nvim](https://github.com/flashcodes-themayankjha/Fknotes.nvim) - 从项目内的任何位置记笔记、待办事项、搜索所有待办事项、获取提醒等等。
- [apdot/doodle](https://github.com/apdot/doodle) - 以开发人员为中心的知识库，具有项目/分支范围注释、双向链接、注释标记、图形视图、望远镜集成和 Git 同步。
- [sduras/duras_bridge](https://github.com/sduras/duras_bridge) - [duras](https://codeberg.org/duras/duras) 纯文本日常笔记的桥梁；从编辑器中追加、搜索和打开注释。
- [gmcusaro/ma.nvim](https://github.com/gmcusaro/ma.nvim) - 具有关系笔记导航和安全文件操作的最小 Markdown 知识管理。
- [jameswolensky/marker-groups.nvim](https://github.com/jameswolensky/marker-groups.nvim) - 保留持久的代码注释而不修改代码。
- [bngarren/checkmate.nvim](https://github.com/bngarren/checkmate.nvim) - 一个功能齐全的基于 Markdown 的 TODO 插件。
- [lfilho/note2cal.nvim](https://github.com/lfilho/note2cal.nvim) - 从 Markdown 笔记创建日历事件（仅限 macOS）。
- [0styx0/abbreinder.nvim](https://github.com/0styx0/abbreinder.nvim) - 缩写提醒。
- [jakewvincent/mkdnflow.nvim](https://github.com/jakewvincent/mkdnflow.nvim) - 流畅的 Markdown 笔记本导航和管理（创建链接、关注链接、创建和管理待办事项列表、参考书目文件等）。
- [jbyuki/nabla.nvim](https://github.com/jbyuki/nabla.nvim) - 记下你的科学笔记。
- [nvim-neorg/neorg](https://github.com/nvim-neorg/neorg) - 现代性与疯狂的可扩展性相遇。组织您生活的未来。
- [nvim-orgmode/orgmode](https://github.com/nvim-orgmode/orgmode) - 用 Lua 编写的 Org 模式克隆。
- [nfrid/due.nvim](https://github.com/nfrid/due.nvim) - 将日期字符串的到期时间显示为虚拟文本。
- [jbyuki/venn.nvim](https://github.com/jbyuki/venn.nvim) - 绘制 ASCII 图。
- [nvim-telekasten/telekasten.nvim](https://github.com/nvim-telekasten/telekasten.nvim) - 使用基于文本的 Markdown zettelkasten / wiki 并将其与基于望远镜.nvim 的日记混合。
- [zk-org/zk-nvim](https://github.com/zk-org/zk-nvim) - 提供与纯文本笔记助手“zk”的集成。
- [chrsm/impulse.nvim](https://github.com/chrsm/impulse.nvim) - 阅读 Notion.so 注释。
- [obsidian-nvim/obsidian.nvim](https://github.com/obsidian-nvim/obsidian.nvim) - Obsidian 插件，用 Lua 编写。
- [IlyasYOY/obs.nvim](https://github.com/IlyasYOY/obs.nvim) - 你的黑曜石以思考的速度进行笔记。
- [jghauser/papis.nvim](https://github.com/jghauser/papis.nvim) - 在您最喜欢的编辑器中管理您的参考书目。
- [Ostralyan/scribe.nvim](https://github.com/Ostralyan/scribe.nvim) - 做笔记，轻松。
- [serenevoid/kiwi.nvim](https://github.com/serenevoid/kiwi.nvim) - 具有必要功能的精简 VimWiki。
- [backdround/global-note.nvim](https://github.com/backdround/global-note.nvim) - 浮动窗口中的一个全局注释。
- [2KAbhishek/tdo.nvim](https://github.com/2KAbhishek/tdo.nvim) - 快速而简单的笔记。
- [slugbyte/whip.nvim](http://github.com/slugbyte/whip.nvim) - 一个超快速的最小暂存器管理插件，biew biew biew。
- [y3owk1n/dotmd.nvim](https://github.com/y3owk1n/dotmd.nvim) - 管理笔记、待办事项、日记条目和收件箱，全部使用 Markdown。
- [athar-qadri/scratchpad.nvim](https://github.com/athar-qadri/scratchpad.nvim) - 在您最喜欢的编辑器中轻松管理便签本。
- [echaya/neowiki.nvim](https://github.com/echaya/neowiki.nvim) - 现代 vimwiki 的后继者提供了一个开箱即用的最小、直观的工作流程，用于记笔记和完成工作 (GTD)。
- [happyeric77/joplin.nvim](https://github.com/happyeric77/joplin.nvim) - Joplin 注释了实用程序：树浏览器、搜索、打开和 Telescope 集成。
- [ymic9963/mdnotes.nvim](https://github.com/ymic9963/mdnotes.nvim) - 简单、改进且可扩展的 Markdown 笔记。
- [nbeversl/urtext_neovim](https://github.com/nbeversl/urtext_neovim) - Urtext 的实现。
- [losch/ztl](https://codeberg.org/losch/ztl) - 单个二进制文件中的快速静态音符生成器，​​内置所有内容。
- [indium114/studytools.nvim](https://github.com/indium114/studytools.nvim) - 各种实用程序可增强学习和笔记体验。
- [iwe-org/iwe.nvim](https://github.com/iwe-org/iwe.nvim) - 与“IWE”集成，这是一个专为基于 Markdown 的知识管理和笔记工作流程而设计的 LSP。
- [carloscalla/notepad.nvim](https://github.com/carloscalla/notepad.nvim) - 通过特定于存储库和全局记事本的支持，在 Markdown 中快速记笔记。
- [MattHandzel/taskwarrior.nvim](https://github.com/MattHandzel/taskwarrior.nvim) - 在缓冲区中编辑 Taskwarrior 任务，将任务渲染为 Markdown 复选框，使用 Vim 动作进行批量编辑，保存时进行差异化和应用。灵感来自 oil.nvim。
<!--lint disable double-link -->
[**⬆ 回到顶部**](#contents)
<!--lint enable double-link -->

## 实用性

- [StefanBartl/color_my_ascii.nvim](https://github.com/StefanBartl/color_my_ascii.nvim) - Markdown 代码块中 ASCII 艺术的彩色突出显示。
- [necrom4/calcium.nvim](https://github.com/necrom4/calcium.nvim) - 一个强大的 [`lua-lib-math`](https://www.lua.org/pil/18.html) 缓冲区内计算器，具有可视模式、函数和变量支持。
- [code-biscuits/nvim-biscuits](https://github.com/code-biscuits/nvim-biscuits) - 什锦饼干港。最终也得到了更多支持的语言。
- [rktjmp/paperplanes.nvim](https://github.com/rktjmp/paperplanes.nvim) - 将选择或缓冲区发布到在线粘贴箱。
- [axieax/urlview.nvim](https://github.com/axieax/urlview.nvim) - 浏览当前缓冲区中的所有 URL。
- [cxwx/lazyUrlUpdate.nvim](https://github.com/cxwx/lazyUrlUpdate.nvim) - 通过 `lazy.nvim` 更新光标下的插件。
- [sontungexpt/url-open](https://github.com/sontungexpt/url-open) - 打开光标下的 URL 并为其创建突出显示效果。
- [crusj/bookmarks.nvim](https://github.com/crusj/bookmarks.nvim) - 记住文件位置并按时间和频率排序。
- [jbyuki/instant.nvim](https://github.com/jbyuki/instant.nvim) - 用 Lua 编写的协作编辑插件，无依赖项。
- [chrisgrieser/nvim-genghis](https://github.com/chrisgrieser/nvim-genghis) - 方便的文件操作，用Lua编写。
- [figsoda/nix-develop.nvim](https://github.com/figsoda/nix-develop.nvim) - 运行“nixdevelop”而不重新启动 Neovim。
- [tenxsoydev/nx.nvim](https://github.com/tenxsoydev/nx.nvim) - Neovim API 实用程序包装器通过 Lua 键盘映射、突出显示、自动命令和选项提供更多便利。
- [mluders/comfy-line-numbers.nvim](https://github.com/mluders/comfy-line-numbers.nvim) - 将相对数字限制为仅在键盘上显示左侧数字。
- [ragnarok22/whereami.nvim](https://github.com/ragnarok22/whereami.nvim) - 通过获取您的当前位置来测试您的 VPN。
- [aPeoplesCalendar/apc.nvim](https://github.com/aPeoplesCalendar/apc.nvim) - “这一天”风格的日历，提供有关全球工人阶级运动和解放斗争历史的信息。
- [subnut/nvim-ghost.nvim](https://github.com/subnut/nvim-ghost.nvim) - GhostText 支持零依赖。
- [LintaoAmons/scratch.nvim](https://github.com/LintaoAmons/scratch.nvim) - 创建和管理临时文件。
- [0xJohnnyboy/scretch.nvim](https://github.com/0xJohnnyboy/scretch.nvim) - 通过选择器集成创建和管理暂存文件、暂存模板。
- [yutkat/confirm-quit.nvim](https://github.com/yutkat/confirm-quit.nvim) - 退出前确认。
- [bgaillard/readonly.nvim](https://github.com/bgaillard/readonly.nvim) - 包含敏感/秘密信息、密码、API 密钥、SSH 密钥等的文件的安全版本。
- [zeybek/camouflage.nvim](https://github.com/zeybek/camouflage.nvim) - 通过直观地屏蔽“.env”、“.json”、“.yaml”、“.toml”和“.properties”文件中的机密，在屏幕共享期间隐藏配置文件中的敏感值。
- [linrongbin16/gentags.nvim](https://github.com/linrongbin16/gentags.nvim) - 老派 vimers 的标签生成器/管理。
- [Zeioth/distroupdate.nvim](https://github.com/Zeioth/distroupdate.nvim) - 与发行版无关的更新程序，用于从配置的 Git 存储库获取最新更改。
- [terje/simctl.nvim](https://github.com/terje/simctl.nvim) - 与 iOS 模拟器交互。
- [mistricky/codesnap.nvim](https://github.com/mistricky/codesnap.nvim) - 功能丰富的快照插件，可以制作漂亮的代码快照。
- [AlejandroSuero/freeze-code.nvim](https://github.com/AlejandroSuero/freeze-code.nvim) - 在编辑器中使用 [freeze](https://github.com/charmbracelet/freeze) 的代码屏幕截图插件。
- [ysmb-wtsg/in-and-out.nvim](https://github.com/ysmb-wtsg/in-and-out.nvim) - 快速导航进出周围的角色。
- [ellisonleao/dotenv.nvim](https://github.com/ellisonleao/dotenv.nvim) - 极简的“.env”支持。
- [MisanthropicBit/decipher.nvim](https://github.com/MisanthropicBit/decipher.nvim) - 使用各种编解码器（例如 base64）对文本进行编码和解码。
- [philosofonusus/ecolog.nvim](https://github.com/philosofonusus/ecolog.nvim) - 复杂的一体化工具包，可处理“.env”文件和环境变量。
- [theKnightsOfRohan/hexer.nvim](https://github.com/theKnightsOfRohan/hexer.nvim) - 无需转换表即可在二进制表示形式之间轻松转换。
- [josephburgess/nvumi](https://github.com/josephburgess/nvumi) - 暂存缓冲区中的自然语言计算器。
- [redoxahmii/json-to-types.nvim](https://github.com/redoxahmii/json-to-types.nvim) - 将 JSON 对象转换为多种语言的类型定义。
- [ovk/endec.nvim](https://github.com/ovk/endec.nvim) - 使用 Base64、Base64URL 和 URL（百分比）编码对文本进行编码、解码和重新编码。
- [y3owk1n/time-machine.nvim](https://github.com/y3owk1n/time-machine.nvim) - 通过交互式时间线、差异预览、标记、实时重新加载树和清理功能来控制您的编辑历史记录。
- [athar-qadri/weather.nvim](https://github.com/athar-qadri/weather.nvim) - 实时天气和地震警报，支持 lualine 集成（无需 API 密钥）。
- [penaz91/MiniDYM](https://github.com/Penaz91/MiniDYM) - 一个非常小的“您的意思是”插件，建议用户可能想要打开的文件而不是创建新文件。
- [Owen-Dechow/videre.nvim](https://github.com/Owen-Dechow/videre.nvim) - 探索 JSON、YAML 和 TOML 文件作为基于嵌套单元/节点的图形表示。
- [mahyarmirrashed/famous-quotes.nvim](https://github.com/mahyarmirrashed/famous-quotes.nvim) - 获取历史上的名言并在启动时显示。
- [iquzart/toggleword.nvim](https://github.com/iquzart/toggleword.nvim) - 在光标下的常用代码关键字之间切换，例如 true ⇄ false、on ⇄ off、enabled ⇄disabled 和 dev ⇄ prod。
- [leblocks/toggle.nvim](https://github.com/leblocks/toggle.nvim) - 在光标下的常用单词之间切换，例如 _public_ ⇄ _private_ ⇄ _protected_。易于添加和覆盖内置切换。
- [piersolenski/brewfile.nvim](https://github.com/piersolenski/brewfile.nvim) - 管理您的 [Homebrew](https://brew.sh/) [Brewfile](https://docs.brew.sh/Brew-Bundle-and-Brewfile)。
- [gpanders/nvim-moonwalk](https://github.com/gpanders/nvim-moonwalk) - 在 Neovim 配置中的任何位置使用任何编译为 Lua 的语言。
- [johannww/tts.nvim](https://github.com/johannww/tts.nvim) - 基于 Microsoft Edge 在线服务的文本转语音工具。
- [doctorfree/cheatsheet.nvim](https://github.com/doctorfree/cheatsheet.nvim) - 可搜索的备忘单。
- [gaborvecsei/cryptoprice.nvim](https://github.com/gaborvecsei/cryptoprice.nvim) - 检查定义的加密货币的价格。
- [wsdjeg/mru.nvim](https://github.com/wsdjeg/mru.nvim) - 管理和显示您最近使用的 (MRU) 文件。
- [wsdjeg/ctags.nvim](https://github.com/wsdjeg/ctags.nvim) - 自动生成标签文件并更新标签选项。
- [leo-alvarenga/quoth.nvim](https://github.com/leo-alvarenga/quoth.nvim) - 一个轻量级、可配置的随机报价提供程序，具有延迟加载、自定义表格和过滤器。
- [indium114/cheaty.nvim](https://github.com/indium114/cheaty.nvim) - 一个简单的、可配置的备忘单。
- [indium114/unobtrusive-relnums.nvim](https://github.com/indium114/unobtrusive-relnums.nvim) - 符号栏中不显眼的相对行号。
- [glyccogen/imprint.nvim](https://github.com/glyccogen/imprint.nvim) - 通过 Playwright 和 headless Chromium 截取代码的所见即所得屏幕截图，保留您的配色方案和亮点。
- [emrearmagan/dockyard.nvim](https://github.com/emrearmagan/dockyard.nvim) - 用于管理容器、图像、网络和日志的 Docker 仪表板。
- [ChuYanLon/telegram.nvim](https://github.com/ChuYanLon/telegram.nvim) - 由 TDLib 支持的 Telegram 聊天客户端，支持实时消息传递、群组管理和媒体预览。
- [paulburgess1357/nvim-mcp](https://github.com/paulburgess1357/nvim-mcp) - MCP 服务器让 AI 代理通过 Neovim 的 msgpack-RPC 套接字访问缓冲区、命令和 LSP 诊断。

### CSV 文件

- [VidocqH/data-viewer.nvim](https://github.com/VidocqH/data-viewer.nvim) - 提供一个简单的表格视图来检查“csv”、“tsv”等数据文件。
- [theKnightsOfRohan/csvlens.nvim](https://github.com/theKnightsOfRohan/csvlens.nvim) - [YS-L/csvlens](https://github.com/YS-L/csvlens) 的端口，用于轻松预览表格数据。
- [emmanueltouzery/decisive.nvim](https://github.com/emmanueltouzery/decisive.nvim) - 轻松快速地查看和编辑 CSV 文件。
- [hat0uma/csvview.nvim](https://github.com/hat0uma/csvview.nvim) - 异步 CSV/TSV 表查看器，具有实时更新、可配置注释和分隔符以及多种显示模式。
<!--lint disable double-link -->
[**⬆ 回到顶部**](#contents)
<!--lint enable double-link -->

## 动画

- [LuxVim/nvim-luxmotion](https://github.com/LuxVim/nvim-luxmotion) - 流畅、高性能的运动和滚动动画 — 60fps 流畅的光标移动、单词跳转和视口滚动，全部合而为一。
- [sphamba/smear-cursor.nvim](https://github.com/sphamba/smear-cursor.nvim) - 在所有终端中使用涂抹效果对光标进行动画处理。灵感来自 Neovide 的动画光标。
- [nvim-mini/mini.nvim#mini.animate](https://github.com/nvim-mini/mini.nvim/blob/main/readmes/mini-animate.md) - `mini.nvim` 模块为常见的内置操作（光标移动、滚动、调整大小、窗口打开/关闭）添加开箱即用的动画。
- [rachartier/tiny-glimmer.nvim](https://github.com/rachartier/tiny-glimmer.nvim/) - 为各种操作添加微妙的动画。
- [y3owk1n/undo-glow.nvim](https://github.com/y3owk1n/undo-glow.nvim/) - 用于编辑操作（撤消、重做、复制、粘贴等）的动画发光/高亮效果，具有完全可定制的动画和外观。
- [gen740/SmoothCursor.nvim](https://github.com/gen740/SmoothCursor.nvim) - 将精美的子光标添加到signcolumn以显示滚动或跳转方向。
- [indium114/smudge.nvim](https://github.com/indium114/smudge.nvim) - 高性能的光标动画。
<!--lint disable double-link -->
[**⬆ 回到顶部**](#contents)
<!--lint enable double-link -->

## 终端集成

- [TheLazyCat00/runner-nvim](https://github.com/TheLazyCat00/runner-nvim) - 在浮动终端中运行命令并跟踪每个 CWD 执行的最后一个命令，从而可以轻松重复构建或测试命令。
- [LuxVim/nvim-luxterm](https://github.com/LuxVim/nvim-luxterm) - 浮动窗口终端会话管理器，提供优雅的多终端组织、实时预览和直观的导航以及现代 UI 设计。轻松管理、切换和定制多个终端。
- [waiting-for-dev/ergoterm.nvim](https://github.com/waiting-for-dev/ergoterm.nvim) - 无缝终端工作流程集成与基于智能选择器的终端选择、灵活的文本发送和持久配置。
- [ingur/floatty.nvim](https://github.com/ingur/floatty.nvim) - 一个微小（<200 LOC）但高度可定制的浮动终端管理器。
- [imranzero/multiterm.nvim](https://github.com/imranZERO/multiterm.nvim) - 轻松管理多个浮动终端窗口。
- [Dan7h3x/neaterm.nvim](https://github.com/Dan7h3x/neaterm.nvim) - 一个具有出色功能的小型智能终端/REPL 管理器。
- [nikvdp/neomux](https://github.com/nikvdp/neomux) - 从 shell 中通过 `:term` 命令控制 Neovim。
- [willothy/flatten.nvim](https://github.com/willothy/flatten.nvim) - 从当前 Neovim 实例中的终端缓冲区打开文件，而不是启动嵌套实例。
- [akinsho/toggleterm.nvim](https://github.com/akinsho/toggleterm.nvim) - 轻松管理多个终端窗口。
- [norcalli/nvim-terminal.lua](https://github.com/norcalli/nvim-terminal.lua) - 高性能文件类型模式，利用正确的颜色代码隐藏和突出显示缓冲区。
- [numToStr/FTerm.nvim](https://github.com/numToStr/FTerm.nvim) - 没有用 Lua 编写的废话浮动终端。
- [jghauser/kitty-runner.nvim](https://github.com/jghauser/kitty-runner.nvim) - 穷人的REPL。轻松将缓冲线和命令发送到 kitty 终端。
- [jlesquembre/nterm.nvim](https://github.com/jlesquembre/nterm.nvim) - 通过通知与终端进行交互。
- [s1n7ax/nvim-terminal](https://github.com/s1n7ax/nvim-terminal) - 一个简单易用的多终端插件。
- [logicmagix/tide42](https://github.com/logicmagix/tide42) - 基于 Neovim、tmux 和可编写脚本的工作流程构建的完全集成的终端 IDE。
- [samjwill/nvim-unception](https://github.com/samjwill/nvim-unception) - Neovim 会话的自动取消嵌套从终端缓冲区开始。
- [kassio/neoterm](https://github.com/kassio/neoterm) - 一些 `:terminal` 函数的包装。
- [nyngwang/NeoTerm.lua](https://github.com/nyngwang/NeoTerm.lua) - 为每个**缓冲区**连接一个终端，现在具有稳定的切换和惊人的光标恢复功能。
- [idanarye/nvim-channelot](https://github.com/idanarye/nvim-channelot) - 从 Lua 协程操作 Neovim 作业。
- [chomosuke/term-edit.nvim](https://github.com/chomosuke/term-edit.nvim) - 允许您像任何其他缓冲区一样在终端中编辑命令。
- [mikesmithgh/kitty-scrollback.nvim](https://github.com/mikesmithgh/kitty-scrollback.nvim) - 打开你的小猫回滚缓冲区。呜呜呜。
- [niuiic/terminal.nvim](https://github.com/niuiic/terminal.nvim) - 管理终端作为缓冲区，支持多终端。
- [NeViRAIDE/nekifoch.nvim](https://github.com/NeViRAIDE/nekifoch.nvim) - 管理 kitty 终端字体设置。
- [2KAbhishek/termim.nvim](https://github.com/2KAbhishek/termim.nvim/) - Neovim 终端，已改进。
- [samharju/yeet.nvim](https://github.com/samharju/yeet.nvim) - 在终端缓冲区或 tmux 窗格中运行 shell 命令。
- [isak102/ghostty.nvim](https://github.com/isak102/ghostty.nvim) - 保存时自动验证您的 Ghostty 配置。
- [laktak/tome](https://github.com/laktak/tome) - 适用于您的终端的交互式脚本剧本（可以选择使用 Tmux）。
- [Axot017/multiterm.nvim](https://github.com/Axot017/multiterm.nvim) - 具有键绑定的多个终端实例的轻量级管理器。
- [da-moon/telescope-toggleterm.nvim](https://github.com/da-moon/telescope-toggleterm.nvim) - 用于终端缓冲区的望远镜选择器。
- [benoror/gpg.nvim](https://github.com/benoror/gpg.nvim) - 对称编辑GPG加密文件。
- [gh-liu/nvim-winterm](https://github.com/gh-liu/nvim-winterm) - 多终端窗口管理器。
- [hawknewton/termyank.nvim](https://github.com/hawknewton/termyank.nvim) - 避免在终端缓冲区中拉出换行符。
<!--lint disable double-link -->
[**⬆ 回到顶部**](#contents)
<!--lint enable double-link -->

## 调试

- [mfussenegger/nvim-dap](https://github.com/mfussenegger/nvim-dap) - 调试适配器协议客户端实现。
- [sakhnik/nvim-gdb](https://github.com/sakhnik/nvim-gdb) - GDB、LLDB、PDB/PDB++ 和 BashDB 的瘦包装器。
- [rcarriga/nvim-dap-ui](https://github.com/rcarriga/nvim-dap-ui) - nvim-dap 的 UI。
- [pocco81/dap-buddy.nvim](https://github.com/pocco81/dap-buddy.nvim) - 管理 nvim-dap 的多个调试器。
- [Weissle/persistent-breakpoints.nvim](https://github.com/Weissle/persistent-breakpoints.nvim) - nvim-dap 的持久断点。
- [ofirgall/goto-breakpoints.nvim](https://github.com/ofirgall/goto-breakpoints.nvim) - 在 nvim-dap 的断点之间循环。
- [andrewferrier/debugprint.nvim](https://github.com/andrewferrier/debugprint.nvim) - 调试 print() 方式。
- [t-troebst/perfanno.nvim](https://github.com/t-troebst/perfanno.nvim) - 使用调用图分析数据注释您的代码。对 perf、flamegraph 和 LuaJIT 分析器的本机支持。
- [niuiic/dap-utils](https://github.com/niuiic/dap-utils.nvim) - 为使用 nvim-dap 提供更好体验的实用程序。
- [theHamsta/nvim-dap-virtual-text](https://github.com/theHamsta/nvim-dap-virtual-text) - nvim-dap 的虚拟文本支持。
- [chrisgrieser/nvim-chainsaw](https://github.com/chrisgrieser/nvim-chainsaw) - 加快日志创建速度。创建各种特定于语言的日志语句，例如变量、断言或时间测量的日志。
- [Willem-J-an/visidata.nvim](https://github.com/Willem-J-an/visidata.nvim) - 使用 visidata 的功能在“nvim-dap”中渲染 Pandas 数据帧。
- [igorlfs/nvim-dap-view](https://github.com/igorlfs/nvim-dap-view) - nvim-dap 的现代简约 UI。
- [Carcuis/dap-breakpoints.nvim](https://github.com/Carcuis/dap-breakpoints.nvim) - 使用 nvim-dap 的虚拟文本和弹出窗口显示来管理和创建高级断点。
- [ravsii/nvim-dap-envfile](https://github.com/ravsii/nvim-dap-envfile) - 对 nvim-dap 的自动 `envFile` 支持。
- [fschaal/azfunc.nvim](https://github.com/fschaal/azfunc.nvim) - 通过自动 DAP 集成无缝调试 Azure Functions。
- [evanmcpheron/rocketlog.nvim](https://github.com/evanmcpheron/rocketlog.nvim) - 通过日志和元数据搜索，无缝添加 JavaScript 和 TypeScript 文件的日志记录。
- [NickTsaizer/splitasm.nvim](https://github.com/NickTsaizer/splitasm.nvim) - 并排查看编译后的程序集输出和源代码，并同步光标移动。

### 快速修复

- [kevinhwang91/nvim-bqf](https://github.com/kevinhwang91/nvim-bqf) - 使快速修复窗口变得更好。
- [yorickpeterse/nvim-pqf](https://github.com/yorickpeterse/nvim-pqf) - 更漂亮的快速修复/位置列表窗口。
- [ashfinal/qfview.nvim](https://github.com/ashfinal/qfview.nvim) - 相当快速修复/位置视图，具有一致的路径缩短和折叠功能。
- [niuiic/quickfix.nvim](https://github.com/niuiic/quickfix.nvim) - Quickfix 的扩展功能，包括存储、恢复、制作、删除等。
- [stevearc/quicker.nvim](https://github.com/stevearc/quicker.nvim) - 改进了快速修复 UI 和可编辑快速修复缓冲区。
<!--lint disable double-link -->
[**⬆ 回到顶部**](#contents)
<!--lint enable double-link -->

## 测试

- [David-Kunz/jester](https://github.com/David-Kunz/jester) - 轻松运行和调试 Jest 测试。
- [klen/nvim-test](https://github.com/klen/nvim-test) - 用于运行测试的包装器。
- [nvim-neotest/neotest](https://github.com/nvim-neotest/neotest) - 用于与 Neovim 内的测试交互的可扩展框架。
- [andythigpen/nvim-coverage](https://github.com/andythigpen/nvim-coverage) - 在标志栏中显示覆盖范围信息。
- [quolpr/quicktest.nvim](https://github.com/quolpr/quicktest.nvim) - 在分割窗口或弹出窗口中运行测试并提供实时反馈。
- [zkucekovic/tdd.nvim](https://github.com/zkucekovic/tdd.nvim) - 根据 PSR-4 命名空间映射，打开或创建给定类的匹配 PHPUnit 测试文件。
- [nvim-neotest/neotest-jest](https://github.com/nvim-neotest/neotest-jest) - 用于运行 Jest 测试的 Neotest 适配器。
- [MisanthropicBit/neotest-busted](https://github.com/MisanthropicBit/neotest-busted) - Neotest 适配器，用于使用 Neovim 作为 Lua 解释器运行失败的测试。
- [mr-u0b0dy/crazy-coverage.nvim](https://github.com/mr-u0b0dy/crazy-coverage.nvim) - 显示代码覆盖率。
<!--lint disable double-link -->
[**⬆ 回到顶部**](#contents)
<!--lint enable double-link -->

## 代码运行者

- [rafcamlet/nvim-luapad](https://github.com/rafcamlet/nvim-luapad) - 用于运行 Lua 代码的交互式暂存器。
- [michaelb/sniprun](https://github.com/michaelb/sniprun) - 直接从 Neovim 运行任何语言的部分代码。
- [CRAG666/code_runner.nvim](https://github.com/CRAG666/code_runner.nvim) - 你可以拥有的最好的代码运行者，具有超能力。
- [is0n/jaq-nvim](https://github.com/is0n/jaq-nvim) - 只是 Lua 中的另一个 Quickrun 插件。
- [jedrzejboczar/toggletasks.nvim](https://github.com/jedrzejboczar/toggletasks.nvim) - 具有 JSON/YAML 配置的任务运行器，使用toggleterm.nvim 和 Telescope.nvim。
- [EthanJWright/vs-tasks.nvim](https://github.com/EthanJWright/vs-tasks.nvim) - 运行和管理项目作业，支持 VSCode 的“tasks.json”规范。
- [stevearc/overseer.nvim](https://github.com/stevearc/overseer.nvim) - 任务运行器和作业管理插件。
- [desdic/greyjoy.nvim](https://github.com/desdic/greyjoy.nvim) - 用于 Makefile、VSCode 任务、厨房等的模块化任务运行器。
- [Shatur/neovim-tasks](https://github.com/Shatur/neovim-tasks) - 有状态任务管理器专注于与构建系统的集成。
- [krady21/compiler-explorer.nvim](https://github.com/krady21/compiler-explorer.nvim) - 使用 [compiler-explorer](https://godbolt.org/) REST API 进行异步编译。
- [hadishahpuri/nvimlaunch](https://github.com/hadishahpuri/nvimlaunch) - 定义、运行和管理特定于项目的命令。
- [milanglacier/yarepl.nvim](https://github.com/milanglacier/yarepl.nvim) - 另一个 REPL，灵活，支持多种范例与 REPL 交互，并且原生点重复，无需其他依赖项。
- [Vigemus/iron.nvim](https://github.com/Vigemus/iron.nvim) - 嵌入了 30 多种语言的交互式 REPL。
- [Civitasv/cmake-tools.nvim](https://github.com/Civitasv/cmake-tools.nvim) - CMake 集成。
- [idanarye/nvim-moonicipal](https://github.com/idanarye/nvim-moonicipal) - 任务跑步者专注于快速变化的个人任务。
- [MarcHamamji/runner.nvim](https://github.com/MarcHamamji/runner.nvim) - 可定制的 Lua 代码运行器。
- [google/executor.nvim](https://github.com/google/executor.nvim) - 允许您在后台运行命令行任务并收到结果通知。
- [sektant1/executioner.nvim](https://github.com/sektant1/executioner.nvim) - 脚本选择器和运行器可从项目目录中查找并运行任何脚本（带或不带参数）。
- [Zeioth/compiler.nvim](https://github.com/Zeioth/compiler.nvim) - 用于构建和运行代码的编译器，无需配置任何内容。
- [Zeioth/makeit.nvim](https://github.com/Zeioth/makeit.nvim) - 基于监督者的 Makefile 运行程序。
- [jaytyrrell13/static.nvim](https://github.com/jaytyrrell13/static.nvim) - 运行静态站点生成器命令。
- [dasupradyumna/launch.nvim](https://github.com/dasupradyumna/launch.nvim) - 一个简单快速的任务启动器，允许动态动态配置任务，并可选支持调试。
- [benlubas/molten-nvim](https://github.com/benlubas/molten-nvim) - 允许通过 Jupyter 内核运行代码块。输出（包括图像输出）呈现在代码下方的浮动窗口中。
- [pianocomposer321/officer.nvim](https://github.com/pianocomposer321/officer.nvim) - 与dispatch.vim 类似，但使用overser.nvim。
- [speelbarrow/spLauncher.nvim](https://github.com/speelbarrow/spLauncher.nvim) - 我猜是为了启动任务。
- [al1-ce/just.nvim](https://github.com/al1-ce/just.nvim) - justfiles 的任务运行程序。
- [niuiic/task.nvim](https://github.com/niuiic/task.nvim) - 另一个高度可配置的任务管理器，可实现与任务的无缝交互。
- [chrisgrieser/nvim-justice](https://github.com/chrisgrieser/nvim-justice) - “just”任务运行程序的轻量级集成。
- [pewpewnor/pilot.nvim](https://github.com/pewpewnor/pilot.nvim) - 使用键绑定快速运行您的项目和文件，并配置如何动态运行它们。
- [ok97465/ipybridge.nvim](https://github.com/ok97465/ipybridge.nvim) - 运行 Python 代码、执行 Jupyter 单元、调试和探索变量。
- [wsdjeg/code-runner.nvim](https://github.com/wsdjeg/code-runner.nvim) - 具有范围支持的异步代码运行器。
- [mikeboiko/nvim-flow](https://github.com/mikeboiko/nvim-flow) - 文件范围的命令运行程序，具有 YAML 配置、命令预览、调试集成和回溯快速修复功能。
- [negativo/nx-nvim](https://github.com/negativo/nx-nvim) - 用于 NX monorepo 项目和目标的望远镜选择器，在拆分终端中运行选定的项目和目标。
<!--lint disable double-link -->
[**⬆ 回到顶部**](#contents)
<!--lint enable double-link -->

## Neovim Lua 开发

- [saghen/blink.lib](https://github.com/saghen/blink.lib) - 所有其他“blink.*”插件的通用实用程序。
- [folke/lazydev.nvim](https://github.com/folke/lazydev.nvim) - 更快的 LuaLS 设置。
- [lumen-oss/luarocks-tag-release](https://github.com/lumen-oss/luarocks-tag-release) - 将 Neovim 插件发布到 LuaRocks 的 GitHub 操作。
- [svermeulen/vimpeccable](https://github.com/svermeulen/vimpeccable) - 帮助用 Lua 或任何基于 Lua 的语言编写 .vimrc 的命令。
- [nvim-lua/plenary.nvim](https://github.com/nvim-lua/plenary.nvim) - 全体会议：全体会议；完全的;全部的;绝对;不合格。所有的Lua函数我都不想写两次。
- [tjdevries/vlog.nvim](https://github.com/tjdevries/vlog.nvim) - 单个文件，无依赖性，轻松复制和粘贴日志文件以添加到您的 Neovim Lua 插件中。
- [bfredl/nvim-luadev](https://github.com/bfredl/nvim-luadev) - REPL/调试控制台 Lua 插件。 `:Luadev` 命令将打开一个草稿窗口，其中显示执行 Lua 代码的输出。
- [jbyuki/one-small-step-for-vimkind](https://github.com/jbyuki/one-small-step-for-vimkind) - Neovim Lua 语言的适配器，允许调试 Neovim 实例中运行的任何 Lua 代码。
- [kkharji/sqlite.lua](https://github.com/kkharji/sqlite.lua) - SQLite/LuaJIT 绑定。
- [MunifTanjim/nui.nvim](https://github.com/MunifTanjim/nui.nvim) - UI 组件库。
- [nvim-mini/mini.nvim#mini.doc](https://github.com/nvim-mini/mini.nvim/blob/main/readmes/mini-doc.md) - `mini.nvim` 模块，用于从类似 EmmyLua 的注释生成帮助文件。允许通过钩子函数灵活定制输出。
- [milisims/nvim-luaref](https://github.com/milisims/nvim-luaref) - 内置 Lua 函数的参考。
- [DrKJeff16/nvim-luaref](https://github.com/DrKJeff16/nvim-luaref) - 从 `milisims/nvim-luaref` 分叉，添加内置 Lua 5.1 帮助文档。
- [nvim-mini/mini.nvim#mini.test](https://github.com/nvim-mini/mini.nvim/blob/main/readmes/mini-test.md) - `mini.nvim` 模块，带有用于编写广泛 Neovim 插件测试的框架，支持分层测试、挂钩、参数化、过滤、屏幕测试、“busted-style”模拟、可定制报告器等。
- [ray-x/guihua.lua](https://github.com/ray-x/guihua.lua) - 一个 Lua UI 库。包括 fzy 搜索栏、列表视图和树视图模块。
- [anuvyklack/animation.nvim](https://github.com/anuvyklack/animation.nvim) - 创建动画。
- [nfrid/treesitter-utils](https://github.com/nfrid/treesitter-utils) - 一些有用的树保姆方法。
- [svermeulen/nvim-lusc](https://github.com/svermeulen/nvim-lusc) - 添加对 Lua 中结构化异步/并发的支持。
- [gregorias/coop.nvim](https://github.com/gregorias/coop.nvim) - 与 Lua 协程的结构化并发。
- [CWood-sdf/banana.nvim](https://github.com/CWood-sdf/banana.nvim) - 插件 UI 的 HTML 渲染器。
- [OXY2DEV/helpview.nvim](https://github.com/OXY2DEV/helpview.nvim) - 一个可破解且精美的“vimdoc/help”文件查看器。
- [niuiic/omega.nvim](https://github.com/niuiic/omega.nvim) - 缺少Lua插件开发的功能。
- [2KAbhishek/utils.nvim](https://github.com/2KAbhishek/utils.nvim) - 强大的实用程序可加速插件开发。
- [YaroSpace/lua-console.nvim](https://github.com/YaroSpace/lua-console.nvim) - 用于 Neovim Lua 开发的方便便笺簿/REPL/调试控制台。
- [DrKJeff16/wezterm-types](https://github.com/DrKJeff16/wezterm-types) - LuaLS 的 WezTerm 配置类型注释，包括对社区插件的支持。
- [chrisgve/databox.nvim](https://github.com/chrisgve/databox.nvim) - 使用 [age](https://github.com/FiloSottile/age) 或兼容的加密工具对 Lua 表进行加密存储，以确保加密安全。
- [BirdeeHub/lze](https://github.com/BirdeeHub/lze) - Neovim 插件的延迟加载库。
- [lumen-oss/lz.n](https://github.com/lumen-oss/lz.n) - 一个简单的 Neovim 插件延迟加载库。
- [jrop/morph.nvim](https://github.com/jrop/morph.nvim) - 一个类似 React 的渲染器，用于构建交互式缓冲区/TUI。
<!--lint disable double-link -->
[**⬆ 回到顶部**](#contents)
<!--lint enable double-link -->

## 茴香

- [aileot/nvim-thyme](https://github.com/aileot/nvim-thyme) - 具有安全回滚和 [parinfer-rust](https://github.com/eraserhd/parinfer-rust) 集成的零开销 Fennel JIT 编译器。
- [Olical/aniseed](https://github.com/Olical/aniseed) - 使用 Fennel 配置和扩展 Neovim。
- [Olical/nfnl](https://github.com/Olical/nfnl) - 简化了 Aniseed 的后继者，在文件写入时将 Fennel 编译为 Lua。
- [Olical/conjure](https://github.com/Olical/conjure) - 交互式评估（Clojure、Fennel、Janet、Racket、Hy、MIT Scheme、Guile）。
- [rktjmp/hotpot.nvim](https://github.com/rktjmp/hotpot.nvim) - Neovim 内有无缝、透明的茴香。
- [udayvir-singh/tangerine.nvim](https://github.com/udayvir-singh/tangerine.nvim) - Tangerine 提供了一种轻松的方式将 Fennel 添加到您的配置中。
- [udayvir-singh/hibiscus.nvim](https://github.com/udayvir-singh/hibiscus.nvim) - 高度自以为是的宏可以优雅地编写您的配置。
<!--lint disable double-link -->
[**⬆ 回到顶部**](#contents)
<!--lint enable double-link -->

## 依赖管理

- [DrKJeff16/pipenv.nvim](https://github.com/DrKJeff16/pipenv.nvim) - 具有 `spinner.nvim` 集成的异步 `Pipenv` 管理器。
- [vuki656/package-info.nvim](https://github.com/vuki656/package-info.nvim) - 在 package.json 中将最新的包版本显示为虚拟文本。
- [Saecki/crates.nvim](https://github.com/Saecki/crates.nvim) - `Cargo.toml` 的 Rust 依赖管理。
- [piersolenski/import.nvim](https://github.com/piersolenski/import.nvim) - 根据您已在项目中导入的内容更快地导入模块。
- [Silletr/LazyDeveloperHelper](https://github.com/Silletr/LazyDeveloperHelper) - Python 依赖项管理器，自动添加到您的“requirements.txt”文件中。
- [JesperLundberg/projektgunnar.nvim](https://github.com/JesperLundberg/projektgunnar.nvim) - C# 依赖关系管理器支持处理项目和解决方案文件之间的引用。
- [cosmicbuffalo/gem_install.nvim](https://github.com/cosmicbuffalo/gem_install.nvim) - 安装 Ruby gems，触发“bundle install”和“gem install”，并带有进度和缓存，以防止安装失败时重试。
- [taigrr/glaze.nvim](https://github.com/taigrr/glaze.nvim) - Go 二进制文件的集中管理器，具有并行安装、自动更新检查和 Mason 风格的 UI。
<!--lint disable double-link -->
[**⬆ 回到顶部**](#contents)
<!--lint enable double-link -->

## git

- [YouSame2/inlinediff-nvim](https://github.com/YouSame2/inlinediff-nvim) - 提供更好的内联 Git diff 视图，旨在与您最喜欢的 Git 插件（例如 `gitsigns`）一起使用。
- [mrloop/telescope-git-branch.nvim](https://github.com/mrloop/telescope-git-branch.nvim) - 一个望远镜选择器，用于查找哪些文件并预览多次提交对 Git 分支所做的更改。
- [f-person/git-blame.nvim](https://github.com/f-person/git-blame.nvim) - 显示 Git 责任信息。
- [trevorhauter/gitportal.nvim](https://github.com/trevorhauter/gitportal.nvim) - 生成 Git 永久链接、在浏览器中打开它们、从永久链接本地加载文件等等。
- [lewis6991/gitsigns.nvim](https://github.com/lewis6991/gitsigns.nvim) - Git 集成：标志、大块动作、责备等。
- [nvim-mini/mini.nvim#mini.diff](https://github.com/nvim-mini/mini.nvim/blob/main/readmes/mini-diff.md) - “mini.nvim”模块用于交互式可视化缓冲区文本与其引用之间的差异。在文本区域中提供可切换的详细概述、内置应用/重置/文本对象/转到映射等。
- [nvim-mini/mini.nvim#mini.git](https://github.com/nvim-mini/mini.nvim/blob/main/readmes/mini-git.md) - `mini.nvim` 模块用于增强 Git 与当前 Neovim 进程的集成，实现 Git 相关数据的跟踪、`:Git` 用户命令以及探索 Git 历史的各种帮助程序。
- [NeogitOrg/neogit](https://github.com/NeogitOrg/neogit) - 一个 Magit 克隆，可能会改变一些东西以适应 Vim 哲学。
- [tveskag/nvim-blame-line](https://github.com/tveskag/nvim-blame-line) - 一个小插件，使用虚拟文本在当前行末尾打印 Git 责任信息。
- [linrongbin16/gitlinker.nvim](https://github.com/linrongbin16/gitlinker.nvim) - 维护了“ruifm's gitlinker”的分支，并通过错误修复、ssh 别名、指责支持和其他改进进行了重构。
- [tanvirtin/vgit.nvim](https://github.com/tanvirtin/vgit.nvim) - 可视化 Git 插件可增强您的 Git 体验。
- [dlyongemallo/diffview.nvim](https://github.com/dlyongemallo/diffview.nvim) - 单选项卡界面，可轻松循环浏览任何 Git 版本的所有修改文件的差异。维护 sindrets/diffview.nvim 的分支。
- [barrettruth/diffs.nvim](https://github.com/barrettruth/diffs.nvim) - 通过 Tree-sitter 支持 `vim-fugitive` 和 `&diff` 缓冲区来突出显示差异的语法。
- [kdheepak/lazygit.nvim](https://github.com/kdheepak/lazygit.nvim) - 用于调用lazygit的插件。
- [AckslD/nvim-gfold.lua](https://github.com/AckslD/nvim-gfold.lua) - 使用 [gfold](https://github.com/nickgerace/gfold) 切换存储库并具有状态行组件的插件。
- [aaronhallaert/advanced-git-search.nvim](https://github.com/aaronhallaert/advanced-git-search.nvim) - 使用 Telescope 按提交内容、消息和作者搜索您的 Git 历史记录。
- [9seconds/repolink.nvim](https://github.com/9seconds/repolink.nvim) - 为各种 Git Web 前端生成可共享的 HTTP 永久链接。
- [chrisgrieser/nvim-tinygit](https://github.com/chrisgrieser/nvim-tinygit) - 轻量级、灵活的 Git 客户端。
- [niuiic/git-log.nvim](https://github.com/niuiic/git-log.nvim) - 检查所选代码的 Git 日志。
- [2KAbhishek/co-author.nvim](https://github.com/2KAbhishek/co-author.nvim) - 快速将共同作者添加到提交中。
- [isak102/telescope-git-file-history.nvim](https://github.com/isak102/telescope-git-file-history.nvim) - 在特定提交处打开/预览当前文件的内容，而不使用“git checkout”。
- [moyiz/git-dev.nvim](https://github.com/moyiz/git-dev.nvim) - 编辑时打开远程 Git 存储库。
- [SuperBo/fugit2.nvim](https://github.com/SuperBo/fugit2.nvim) - Git GUI 由 [libgit2](https://libgit2.org) 提供支持。
- [Yu-Leo/blame-column.nvim](https://github.com/Yu-Leo/blame-column.nvim) - 显示 Git 责任信息。
- [yutkat/git-rebase-auto-diff.nvim](https://github.com/yutkat/git-rebase-auto-diff.nvim) - Git rebase 时自动显示 diff。
- [Kohei-Wada/yadm-git.nvim](https://github.com/Kohei-Wada/yadm-git.nvim) - 对 yadm 点文件的无缝 Git 插件支持。
- [axkirillov/unified.nvim](https://github.com/axkirillov/unified.nvim) - 直接在缓冲区中显示内联统一差异。
- [kokusenz/deltaview.nvim](https://github.com/kokusenz/deltaview.nvim) - 内联/统一差异查看器，具有 Tree-sitter 语法突出显示和 δ(https://github.com/dandavison/delta) 风格的差异突出显示，并具有增强的导航功能。
- [StackInTheWild/headhunter.nvim](https://github.com/StackInTheWild/headhunter.nvim) - 快速而简单的实用程序可用于查找和解决合并冲突。
- [yus-works/csc.nvim](https://github.com/yus-works/csc.nvim) - 从 Git 历史记录中学习的传统提交范围完成。
- [404pilo/aicommits.nvim](https://github.com/404pilo/aicommits.nvim) - 使用 AI 生成常规提交消息。
- [wsdjeg/git.nvim](https://github.com/wsdjeg/git.nvim) - 异步 Git 命令包装器插件，使用 `:Git` 命令而不是 `:!git`。
- [Mauritz8/gitstatus.nvim](https://github.com/Mauritz8/gitstatus.nvim) - 交互式 Git 状态窗口，支持暂存、取消暂存和提交文件。
- [esmuellert/codediff.nvim](https://github.com/esmuellert/codediff.nvim) - 使用用 C 实现的 VSCode 算法进行两层突出显示（行 + 字符级别）的并排比较。
- [ajatdarojat45/commitmate.nvim](https://github.com/ajatdarojat45/commitmate.nvim) - 遵循常见提交约定的人工智能辅助提交消息生成器。
- [Enigama/remarks.nvim](https://github.com/Enigama/remarks.nvim) - 附加到 Git 提交的个人开发者注释。
- [Salanoid/gitlogdiff.nvim](https://github.com/Salanoid/gitlogdiff.nvim) - 多个 Git 提交之间的差异，类似于 JetBrains 的 Git 日志。
- [Sengoku11/commitpad.nvim](https://github.com/Sengoku11/commitpad.nvim) - 使用持久的工作树隔离草稿、可视化 50/72 指南和 Markdown 缓冲区编写信息丰富的提交。
- [BibekBhusal0/nvim-git-utils](https://github.com/BibekBhusal0/nvim-git-utils) - 简单的命令让使用 Git 时的生活变得更轻松。
- [spacedentist/resolve.nvim](https://github.com/spacedentist/resolve.nvim) - 轻松解决合并冲突。
- [jceb/jiejie.nvim](https://github.com/jceb/jiejie.nvim) - “逃亡者”风格的柔术前端。
- [chojs23/ec](https://github.com/chojs23/ec) - 具有 3 个窗格的 TUI 原生 Git 合并工具。
- [harrisoncramer/GitLab.nvim](https://github.com/harrisoncramer/GitLab.nvim) - 查看拉取请求并管理其他 GitLab 资源。

### GitHub

- [pwntester/octo.nvim](https://github.com/pwntester/octo.nvim) - 处理 GitHub 问题和 PR。
- [ldelossa/gh.nvim](https://github.com/ldelossa/gh.nvim) - 用于执行代码审查的功能齐全的 GitHub 集成。
- [topaxi/pipeline.nvim](https://github.com/topaxi/pipeline.nvim) - 查看和调度 GitHub Actions 工作流程和 GitLab CI 管道运行。
- [rawnly/gist.nvim](https://github.com/rawnly/gist.nvim) - 从当前文件创建 GitHub Gist（由 gh 提供支持）。
- [2KAbhishek/octohub.nvim](https://github.com/2KAbhishek/octohub.nvim) - 通过简单的按键即可访问所有 gihub 存储库、统计数据等。
- [comatory/gh-co.nvim](https://github.com/comatory/gh-co.nvim) - 根据 GitHub 的“代码所有者”规范显示文件的代码所有者。
- [3ZsForInsomnia/revman.nvim](https://github.com/3ZsForInsomnia/revman.nvim) - 自动跟踪需要审核的 PR 并在 Octo.nvim 中打开它们。
- [cd-4/git-needy.nvim](https://github.com/cd-4/git-needy.nvim) - 在状态栏中记录需要检查的工作流程。
- [claydugo/browsher.nvim](https://github.com/claydugo/browsher.nvim) - 创建指向 GitHub 托管文件/行的提交固定链接。
- [gh-tui-tools/gh-review.nvim](https://github.com/gh-tui-tools/gh-review.nvim) - 查看 GitHub PR。
<!--lint disable double-link -->
[**⬆ 回到顶部**](#contents)
<!--lint enable double-link -->

## 运动

- [HawkinsT/pathfinder.nvim](https://github.com/HawkinsT/pathfinder.nvim) - 通过前瞻和更智能的文件、行/列号和链接分辨率增强 gf/gF/gx。还提供文件/链接的可视化目标、新的运动命令和链接描述检索。
- [nolleh/warp.nvim](https://github.com/nolleh/warp.nvim) - 根据标签从任何缓冲区跳转到文件路径、URL 和 Markdown 链接。
- [tris203/precognition.nvim](https://github.com/tris203/precognition.nvim) - 预识别使用虚拟文本和装订线标志来显示可用的动作。
- [smoka7/hop.nvim](https://github.com/smoka7/hop.nvim) - Hop 是一个类似 EasyMotion 的插件，允许您用尽可能少的击键跳转到文档中的任何位置。
- [ggandor/lightspeed.nvim](https://github.com/ggandor/lightspeed.nvim) - 类似 Sneak 的插件，通过提前显示的标签提供无与伦比的导航速度，消除输入搜索模式和选择目标之间的停顿。
- [ggandor/leap.nvim](https://github.com/ggandor/leap.nvim) - Lightspeed 的精致继承者，旨在建立一个广泛接受的标准接口扩展，以便在类似 Vim 的编辑器中移动。
- [ggandor/flit.nvim](https://github.com/ggandor/flit.nvim) - 增强了 Leap 的 f/t 动作。
- [ggandor/leap-spooky.nvim](https://github.com/ggandor/leap-spooky.nvim) - 远距离的怪异（跳跃）动作。
- [rasulomaroff/telepath.nvim](https://github.com/rasulomaroff/telepath.nvim) - 另一个 Leap 扩展，用于使用不同的方法执行远程操作。
- [folke/flash.nvim](https://github.com/folke/flash.nvim) - 使用搜索标签、增强的角色动作和 Tree-sitter 集成来导航您的代码。
- [nvim-mini/mini.nvim#mini.jump](https://github.com/nvim-mini/mini.nvim/blob/main/readmes/mini-jump.md) - `mini.nvim` 模块用于更智能地跳转到单个字符。
- [nvim-mini/mini.nvim#mini.jump2d](https://github.com/nvim-mini/mini.nvim/blob/main/readmes/mini-jump2d.md) - “mini.nvim”模块可通过迭代标签过滤在可见行内更智能地跳转。支持自定义跳转目标（点）、标签、挂钩、允许的窗口和线条等。
- [rlane/pounce.nvim](https://github.com/rlane/pounce.nvim) - 一个类似 EasyMotion 的插件，用于使用模糊搜索快速移动光标。
- [xiaoshihou514/squirrel.nvim](https://github.com/xiaoshihou514/squirrel.nvim) - 在 Tree-sitter 节点之间快速跳转。
- [abecodes/tabout.nvim](https://github.com/abecodes/tabout.nvim) - 跳出括号对、引号、对象等。
- [woosaaahh/sj.nvim](https://github.com/woosaaahh/sj.nvim) - 基于搜索的导航与快速跳转功能相结合。
- [cbochs/portal.nvim](https://github.com/cbochs/portal.nvim) - 基于并增强现有的跳转列表动作（即“<c-i>”和“<c-o>”）。
- [nvim-mini/mini.nvim#mini.bracketed](https://github.com/nvim-mini/mini.nvim/blob/main/readmes/mini-bracketed.md) - `mini.nvim` 模块用方括号前进/后退。
- [liangxianzhe/nap.nvim](https://github.com/liangxianzhe/nap.nvim) - 使用一个键在下一个/上一个缓冲区、选项卡、诊断等之间跳转。
- [chrisgrieser/nvim-spider](https://github.com/chrisgrieser/nvim-spider) - 像蜘蛛一样使用 w、e、b 动作。考虑驼峰命名法并跳过无关紧要的标点符号。
- [backdround/neowords.nvim](https://github.com/backdround/neowords.nvim) - 跳跃任何类型的单词。它可以很好地控制“w”、“e”、“b”、“ge”运动。
- [backdround/improved-ft.nvim](https://github.com/backdround/improved-ft.nvim) - 提高默认的“f”/“t”能力。
- [cosmicbuffalo/eyeliner.nvim](https://github.com/cosmicbuffalo/eyeliner.nvim) - 突出显示“f”/“t”动作的跳跃目的地。
- [Mr-LLLLL/treesitter-outer](https://github.com/Mr-LLLLL/treesitter-outer) - smart跳转到外节点。
- [Aaronik/Treewalker.nvim](https://github.com/aaronik/Treewalker.nvim) - 在抽象语法树中无缝移动。
- [timseriakov/spamguard.nvim](https://github.com/timseriakov/spamguard.nvim) - 检测过多的密钥垃圾邮件 (jjjj/kkkk) 并建议更有效的替代方案。
- [millerjason/neovimacs.nvim](https://github.com/millerjason/neovimacs.nvim) - 在插入模式下提供 Emacs 移动和缓冲区键绑定。
- [kiyoon/repeatable-move.nvim](https://github.com/kiyoon/repeatable-move.nvim) - 使用“;”和“,”键可重复任何动作。
- [kkew3/jieba.vim](https://github.com/kkew3/jieba.vim) - 中文的单词动作和单词文本对象。

### 基于护树者

- [mfussenegger/nvim-treehopper](https://github.com/mfussenegger/nvim-treehopper) - 区域选择，带有有关由 Tree-sitter 提供支持的文档 AST 节点的提示。
- [drybalka/tree-climber.nvim](https://github.com/drybalka/tree-climber.nvim) - 在树保姆的树上轻松导航，在多语言文件和正常模式下工作。
- [atusy/treemonkey.nvim](https://github.com/atusy/treemonkey.nvim) - 使用 Tree-sitter 节点进行区域选择。
- [kiyoon/treesitter-indent-object.nvim](https://github.com/kiyoon/treesitter-indent-object.nvim) - 由 Tree-sitter 提供支持的上下文感知缩进文本对象。
- [subev/sibling-jump.nvim](https://github.com/subev/sibling-jump.nvim) - 同级 Tree-sitter 节点之间的上下文感知导航。
<!--lint disable double-link -->
[**⬆ 回到顶部**](#contents)
<!--lint enable double-link -->

## 按键绑定

- [RutaTang/compter.nvim](https://github.com/RutaTang/compter.nvim) - 使用自定义模式增强和扩展“<C-a>”和“<C-x>”的功能。
- [zdcthomas/yop.nvim](https://github.com/zdcthomas/yop.nvim) - 轻松创建您自己的运算符（如“d”和“y”）。
- [chrisgrieser/nvim-recorder](https://github.com/chrisgrieser/nvim-recorder) - 简化和改进与宏交互的方式。
- [sontungexpt/bim.nvim](https://github.com/sontungexpt/bim.nvim) - 通过实时显示键入的键来增强插入模式键映射，无需等待 timeoutlen。它提供了响应灵敏且直观的插入模式体验，非常适合 ime 等复杂的输入工作流程。
- [folke/which-key.nvim](https://github.com/folke/which-key.nvim) - 显示一个弹出窗口，其中包含您开始键入的命令的可能的键绑定。
- [nvim-mini/mini.nvim#mini.clue](https://github.com/nvim-mini/mini.nvim/blob/main/readmes/mini-clue.md) - `mini.nvim` 模块显示下一个关键线索。具有选择加入触发器，在可定制的延迟后显示下一个关键信息，允许类似九头蛇的子模式等等。
- [mrjones2014/legendary.nvim](https://github.com/mrjones2014/legendary.nvim) - 将键盘映射、命令和自动命令定义为简单的 Lua 表，同时为它们创建图例（如 VSCode 的命令面板），与“which-key.nvim”集成。
- [Iron-E/nvim-cartographer](https://github.com/Iron-E/nvim-cartographer) - 用于 Lua 环境的更方便的 `:map`ping 语法。
- [LionC/nest.nvim](https://github.com/LionC/nest.nvim) - Lua 实用程序使用级联树简洁地映射键。还允许将 Lua 函数绑定到键。
- [slugbyte/unruly-worker.nvim](https://github.com/slugbyte/unruly-worker.nvim) - 一个非常有趣的 Workman 键盘布局替代键盘映射，具有许多强大的功能，可用于处理猛拉、标记、宏、LSP 等。使用 Lua 构建和配置。
- [FeiyouG/commander.nvim](https://github.com/FeiyouG/commander.nvim) - 以更有组织的方式创建和管理键绑定和命令，并通过 Telescope 快速搜索它们。
- [nvimtools/hydra.nvim](https://github.com/nvimtools/hydra.nvim) - 创建自定义子模式和菜单。 Emacs Hydra 端口。维护 anuvyklack/Hydra.nvim 的分支。
- [max397574/better-escape.nvim](https://github.com/max397574/better-escape.nvim) - 创建快捷方式以退出插入模式而不会造成延迟。
- [TheBlob42/houdini.nvim](https://github.com/TheBlob42/houdini.nvim) - 立即创建逃生模式的快捷方式。
- [Nexmean/caskey.nvim](https://github.com/Nexmean/caskey.nvim) - 使用声明性级联树进行键映射配置的实用程序，可以选择与“which-key”集成。
- [Wansmer/langmapper.nvim](https://github.com/Wansmer/langmapper.nvim) - 自动翻译非英语输入法的映射。
- [tris203/hawtkeys.nvim](https://github.com/tris203/hawtkeys.nvim) - 建议新的易于点击的键盘映射并查找当前键盘映射配置的问题。
- [mawkler/demicolon.nvim](https://github.com/mawkler/demicolon.nvim) - 除了重复“t”/“T”/“f”/“F”之外，还可以使用“;”和“,”键重复跳转到诊断（例如“]d”）和[nvim-treesitter-textobjects]（https://github.com/nvim-treesitter/nvim-treesitter-textobjects?tab=readme-ov-file#text-objects-move）（例如“]f”）。
- [nvim-mini/mini.nvim#mini.keymap](https://github.com/nvim-mini/mini.nvim/blob/main/readmes/mini-keymap.md) - `mini.nvim` 模块，具有用于进行特殊键映射的实用程序：多步骤操作（具有“智能”`<Tab>`、`<S-Tab>`、`<CR>`、`<BS>` 的内置步骤）、组合（更通用的“更好的逃脱”行为）。
- [notomo/gesture.nvim](https://github.com/notomo/gesture.nvim) - 鼠标手势插件。
<!--lint disable double-link -->
[**⬆ 回到顶部**](#contents)
<!--lint enable double-link -->

## 滚动

- [saghen/filler-begone.nvim](https://github.com/saghen/filler-begone.nvim) - 防止滚动超过缓冲区底部并显示不必要的填充线。
- [karb94/neoscroll.nvim](https://github.com/karb94/neoscroll.nvim) - 平滑滚动。
- [declancm/cinnamon.nvim](https://github.com/declancm/cinnamon.nvim) - 平滑滚动任何移动命令。
- [niuiic/scroll.nvim](https://github.com/niuiic/scroll.nvim) - 平滑滚动，自定义平滑策略。
- [rlychrisg/keepcursor.nvim](https://github.com/rlychrisg/keepcursor.nvim) - 用于控制屏幕如何在光标周围定位的函数集合。

### 滚动条

- [Xuyuanp/scrollbar.nvim](https://github.com/Xuyuanp/scrollbar.nvim) - 滚动条。
- [dstein64/nvim-scrollview](https://github.com/dstein64/nvim-scrollview) - 显示交互式滚动条。
- [petertriho/nvim-scrollbar](https://github.com/petertriho/nvim-scrollbar) - 显示诊断和搜索结果的可扩展滚动条。
- [nvim-mini/mini.nvim#mini.map](https://github.com/nvim-mini/mini.nvim/blob/main/readmes/mini-map.md) - “mini.nvim”模块用于显示带有缓冲区文本概述、滚动条和突出显示的浮动窗口。
- [gorbit99/codewindow.nvim](https://github.com/gorbit99/codewindow.nvim) - Minimap插件，与Tree-sitter和内置LSP紧密集成，向用户显示更多信息。
- [lewis6991/satellite.nvim](https://github.com/lewis6991/satellite.nvim) - 装饰滚动条。
- [wsdjeg/scrollbar.nvim](https://github.com/wsdjeg/scrollbar.nvim) - 浮动滚动条。
<!--lint disable double-link -->
[**⬆ 回到顶部**](#contents)
<!--lint enable double-link -->

## 编辑支持

- [DrKJeff16/boolean-toggle.nvim](https://github.com/DrKJeff16/boolean-toggle.nvim) - 在光标下在“true”和“false”之间切换。
- [DrKJeff16/shebang.nvim](https://github.com/DrKJeff16/shebang.nvim) - 在当前文件之上添加或修改 shebang。
- [nxhung2304/lastplace.nvim](https://github.com/nxhung2304/lastplace.nvim) - 重新打开文件时智能恢复光标位置。
- [attilarepka/header.nvim](https://github.com/attilarepka/header.nvim) - 在任何源文件中添加或更新版权和许可证标头。
- [rlychrisg/truncateline.nvim](https://github.com/rlychrisg/truncateline.nvim) - 截断长行，以便在屏幕左侧的开头丢失时跟踪您所在的位置。
- [zbirenbaum/neodim](https://github.com/zbirenbaum/neodim) - 调暗未使用的函数、变量、参数等的亮点。
- [nguyenvukhang/nvim-toggler](https://github.com/nguyenvukhang/nvim-toggler) - 反转文本，例如在“true”和“false”之间切换。
- [saifulapm/commasemi.nvim](https://github.com/saifulapm/commasemi.nvim) - 切换逗号和分号。
- [necrom4/convy.nvim](https://github.com/necrom4/convy.nvim) - 轻松在各种格式之间转换字符串。
- [qwavies/smart-backspace.nvim](https://github.com/qwavies/smart-backspace.nvim) - 上下文感知的退格键处理对、空格和缩进。
- [TheLazyCat00/replace-nvim](https://github.com/TheLazyCat00/replace-nvim) - 使用文本对象将部分代码替换为“+”寄存器的内容。
- [wurli/split.nvim](https://github.com/wurli/split.nvim) - 提供按分隔符分割文本的映射，给出本机 J 命令的逆命令。
- [csessh/stopinsert.nvim](https://github.com/csessh/stopinsert.nvim) - 不活动后自动退出插入模式。
- [windwp/nvim-ts-autotag](https://github.com/windwp/nvim-ts-autotag) - 使用 Tree-sitter 自动关闭和自动重命名 XML、HTML、JSX 标签。
- [windwp/nvim-autopairs](https://github.com/windwp/nvim-autopairs) - Lua 编写的极简主义汽车配对。
- [ZhiyuanLck/smart-pairs](https://github.com/ZhiyuanLck/smart-pairs) - Lua 编写的终极智能对。
- [nvim-mini/mini.nvim#mini.pairs](https://github.com/nvim-mini/mini.nvim/blob/main/readmes/mini-pairs.md) - 用于自动配对的“mini.nvim”模块具有最小的默认值和执行每个键映射的功能。
- [m4xshen/autoclose.nvim](https://github.com/m4xshen/autoclose.nvim) - 用 Lua 编写的极简自动关闭插件。
- [altermo/ultimate-autopair.nvim](https://github.com/altermo/ultimate-autopair.nvim) - 与扩展自动配对。
- [monaqa/dial.nvim](https://github.com/monaqa/dial.nvim) - 扩展增量/减量。
- [HiPhish/rainbow-delimiters.nvim](https://github.com/HiPhish/rainbow-delimiters.nvim) - 彩虹分隔符与树保姆。
- [AckslD/nvim-trevJ.lua](https://github.com/AckslD/nvim-trevJ.lua) - 与参数的 join-line (J) 相反，由 Tree-sitter 提供支持。
- [okuuva/auto-save.nvim](https://github.com/okuuva/auto-save.nvim) - 根据需要尽可能频繁地自动保存您的工作。可通过智能默认值进行自定义。维护 Pocco81/auto-save.nvim 的分支。
- [tmillr/sos.nvim](https://github.com/tmillr/sos.nvim) - 根据预定义的超时值自动保存所有修改的缓冲区。
- [folke/zen-mode.nvim](https://github.com/folke/zen-mode.nvim) - 无干扰编码。
- [andersevenrud/nvim_context_vt](https://github.com/andersevenrud/nvim_context_vt) - 显示当前上下文的虚拟文本。
- [nvim-treesitter/nvim-treesitter-context](https://github.com/nvim-treesitter/nvim-treesitter-context) - 显示当前函数/块上下文的浮动悬停。
- [mizlan/iswap.nvim](https://github.com/mizlan/iswap.nvim) - 交互式选择和交换函数参数、列表元素等。由树保姆提供支持。
- [Wansmer/sibling-swap.nvim](https://github.com/Wansmer/sibling-swap.nvim) - 与树保姆交换争论和其他兄弟姐妹的不同方式。
- [Wansmer/binary-swap.nvim](https://github.com/Wansmer/binary-swap.nvim) - 交换二进制表达式中的操作数和运算符：比较和数学运算。
- [nacro90/numb.nvim](https://github.com/nacro90/numb.nvim) - 以不显眼的方式查看线条。
- [Allendang/nvim-expand-expr](https://github.com/AllenDang/nvim-expand-expr) - 将表达式展开并重复到多行。
- [h-hg/fcitx.nvim](https://github.com/h-hg/fcitx.nvim) - 分别切换和恢复每个缓冲区的 fcitx 状态。
- [keaising/im-select.nvim](https://github.com/keaising/im-select.nvim) - 自动切换和恢复输入法取决于 Neovim 的编辑模式。
- [nvim-mini/mini.nvim#mini.trailspace](https://github.com/nvim-mini/mini.nvim/blob/main/readmes/mini-trailspace.md) - `mini.nvim` 模块用于自动突出显示尾随空白并具有删除它的功能。
- [smjonas/live-command.nvim](https://github.com/smjonas/live-command.nvim) - 具有即时视觉反馈的文本编辑：预览命令，例如 `:norm`、`:g`、宏等。
- [filipdutescu/renamer.nvim](https://github.com/filipdutescu/renamer.nvim) - 类似 VSCode 的重命名 UI，用 Lua 编写。
- [gbprod/cutlass.nvim](https://github.com/gbprod/cutlass.nvim) - 添加与“删除”分开的“剪切”操作的插件。
- [gbprod/substitute.nvim](https://github.com/gbprod/substitute.nvim) - 新的操作员动作可快速替换和交换文本。
- [gregorias/coerce.nvim](https://github.com/gregorias/coerce.nvim) - 更改关键字大小写。
- [nvim-mini/mini.nvim#mini.operators](https://github.com/nvim-mini/mini.nvim/blob/main/readmes/mini-operators.md) - `mini.nvim` 模块具有各种文本编辑操作符：替换、交换、乘法、排序、求值。
- [gbprod/yanky.nvim](https://github.com/gbprod/yanky.nvim) - 改进了 Yank 和 Put 功能。
- [sQVe/sort.nvim](https://github.com/sQVe/sort.nvim) - 智能支持按行和分隔符排序的排序插件。
- [booperlv/nvim-gomove](https://github.com/booperlv/nvim-gomove) - 一个完整的插件，用于移动和复制块和线，一次性完成折叠处理、重新缩进和撤消。
- [hinell/duplicate.nvim](https://github.com/hinell/duplicate.nvim) - 轻松复制线条和线条块；撤消和展开支持；完整的面向对象编程。
- [hinell/move.nvim](https://github.com/hinell/move.nvim) - 移动文本块； [fedepujol/move.nvim](https://github.com/fedepujol/move.nvim) 的分支。
- [willothy/moveline.nvim](https://github.com/willothy/moveline.nvim) - 轻松上下移动线条和块，移动时会自动处理缩进。用 Rust 编写。
- [nvim-mini/mini.nvim#mini.move](https://github.com/nvim-mini/mini.nvim/blob/main/readmes/mini-move.md) - `mini.nvim` 模块可在任何方向移动任何选择（按字符、按行、按块、正常模式下的当前行）。处理“v:count”和撤消历史记录。
- [gbprod/stay-in-place.nvim](https://github.com/gbprod/stay-in-place.nvim) - 使用移位和过滤操作时防止光标移动。
- [nvim-mini/mini.nvim#mini.ai](https://github.com/nvim-mini/mini.nvim/blob/main/readmes/mini-ai.md) - 用于扩展和创建“a”/“i”文本对象的“mini.nvim”模块。它增强了一些内置文本对象，创建了一组广泛的新文本对象（如“a*”、“a<Space>”、“a?”等），并允许用户创建自己的文本对象（通过 Lua 模式或函数）。支持点重复、不同的搜索方式、连续应用等。
- [Wansmer/treesj](https://github.com/Wansmer/treesj) - 拆分/连接代码块，如数组、散列、语句、对象、字典等。使用 Tree-sitter。受到最伟大的 splitjoin.vim 的启发。
- [bennypowers/splitjoin.nvim](https://github.com/bennypowers/splitjoin.nvim) - 拆分和连接各种语法结构。
- [nvim-mini/mini.nvim#mini.splitjoin](https://github.com/nvim-mini/mini.nvim/blob/main/readmes/mini-splitjoin.md) - 用于拆分和连接参数的“mini.nvim”模块。具有可定制的前钩和后钩。在评论中起作用。
- [shortcuts/no-neck-pain.nvim](https://github.com/shortcuts/no-neck-pain.nvim) - 将当前聚焦的缓冲区居中到终端的中间。
- [debugloop/telescope-undo.nvim](https://github.com/debugloop/telescope-undo.nvim) - 一个望远镜扩展，用于可视化您的撤消树和其中的模糊搜索变化。
- [chrisgrieser/nvim-various-textobjs](https://github.com/chrisgrieser/nvim-various-textobjs) - 包含 30 多个新文本对象的捆绑包。
- [XXiaoA/ns-textobject.nvim](https://github.com/XXiaoA/ns-textobject.nvim) - 很棒的 textobject 插件可与 nvim-surround 配合使用。
- [~nedia/auto-save.nvim](https://git.sr.ht/~nedia/auto-save.nvim) - 在`InsertLeave`和`TextChanged`上非常简单的自动保存。基于 Pocco81/AutoSave 但更轻。
- [nvim-mini/mini.nvim#mini.basics](https://github.com/nvim-mini/mini.nvim/blob/main/readmes/mini-basics.md) - “mini.nvim”模块，具有用于常见选项、映射和自动命令的可自定义配置预设。
- [niuiic/part-edit.nvim](https://github.com/niuiic/part-edit.nvim) - 单独编辑文件的一部分。
- [niuiic/divider.nvim](https://github.com/niuiic/divider.nvim) - 自定义代码分隔线。
- [ckolkey/ts-node-action](https://github.com/CKolkey/ts-node-action) - 用于在 Tree-sitter 节点上执行功能转换的框架。
- [tomiis4/hypersonic.nvim](https://github.com/tomiis4/hypersonic.nvim) - 提供 RegExp 的解释。
- [chrisgrieser/nvim-puppeteer](https://github.com/chrisgrieser/nvim-puppeteer) - 自动将字符串与 f 字符串或模板字符串相互转换。
- [nat-418/boole.nvim](https://github.com/nat-418/boole.nvim) - 切换布尔值和常见字符串值。
- [cshuaimin/ssr.nvim](https://github.com/cshuaimin/ssr.nvim) - 基于树保姆的结构搜索和替换。
- [Jxstxs/conceal.nvim](https://github.com/Jxstxs/conceal.nvim) - 使用 Tree-sitter 隐藏常见的样板代码。
- [hiberabyss/bzlops.vim](https://github.com/hiberabyss/bzlops.vim) - 帮助管理您的 bazel 构建规则。
- [altermo/iedit.nvim](https://github.com/altermo/iedit.nvim) - 编辑文本中的一个，同时以相同的方式编辑其他选定的文本。
- [ptdewey/yankbank-nvim](https://github.com/ptdewey/yankbank-nvim) - 在快速访问弹出菜单中启用对最近的复制和删除的简化访问。
- [SunnyTamang/select-undo.nvim](https://github.com/SunnyTamang/select-undo.nvim) - 允许用户撤消特定行或部分选择，而不影响文件的其余部分。
- [OXY2DEV/foldtext.nvim](https://github.com/OXY2DEV/foldtext.nvim) - 动态且风格化的折叠文本。
- [tummetott/unimpaired.nvim](https://github.com/tummetott/unimpaired.nvim) - [tpope/vim-unimpaired](https://github.com/tpope/vim-unimpaired) 的 Lua 端口。
- [daltongd/yanklock.nvim](https://github.com/daltongd/yanklock.nvim) - 暂时将粘贴寄存器锁定为“0”，并使用“d”、“c”和“s”动作，同时保持最新拉出的内容易于访问。
- [zongben/capsoff.nvim](https://github.com/zongben/capsoff.nvim) - 离开插入模式时关闭 CapsLock。
- [kobbikobb/move-lines.nvim](https://github.com/kobbikobb/move-lines.nvim) - 移动在虚拟模式下选择的线。
- [kiyoon/telescope-insert-path.nvim](https://github.com/kiyoon/telescope-insert-path.nvim) - 使用 Telescope 在当前缓冲区中插入文件路径。
- [zhisme/copy_with_context.nvim](https://github.com/zhisme/copy_with_context.nvim) - 复制包含文件路径和行号元数据的行，以便与上下文共享代码片段。
- [jake-stewart/multicursor.nvim](https://github.com/jake-stewart/multicursor.nvim) - 添加对多个游标的支持，这些游标可以按照您的预期工作。
- [brenton-leighton/multiple-cursors.nvim](https://github.com/brenton-leighton/multiple-cursors.nvim) - 一个多光标插件，可在正常、插入/替换或可视模式下工作，并且适用于几乎所有命令。
- [smoka7/multicursors.nvim](https://github.com/smoka7/multicursors.nvim) - 提供更直观的方式来编辑具有多个选择的重复文本。
- [tigion/swap.nvim](https://github.com/tigion/swap.nvim) - 快速切换光标下的单词或当前行中的模式。
- [XXiaoA/atone.nvim](https://github.com/XXiaoA/atone.nvim) - 用于可视化和管理撤消历史的撤消树。
- [nemanjamalesija/smart-paste.nvim](https://github.com/nemanjamalesija/smart-paste.nvim) - 使用三层缩进策略（indentexpr / Tree-sitter / heuristic）自动缩进粘贴的代码。

### 评论

- [jeangiraldoo/codedocs.nvim](https://github.com/jeangiraldoo/codedocs.nvim) - 一个强大且可定制的注释框架，支持多种语言和注释约定。
- [numToStr/Comment.nvim](https://github.com/numToStr/Comment.nvim) - 智能而强大的评论插件。支持评论字符串、动作、点重复等。
- [b3nj5m1n/kommentary](https://github.com/b3nj5m1n/kommentary) - 用 Lua 编写的评论插件。
- [gennaro-tedesco/nvim-commaround](https://github.com/gennaro-tedesco/nvim-commaround) - 用 Lua 编写的快速、轻便的评论插件。
- [folke/todo-comments.nvim](https://github.com/folke/todo-comments.nvim) - 突出显示、列出和搜索项目中的 TODO 注释。
- [kuri-sun/todoage.nvim](https://github.com/kuri-sun/todoage.nvim) - 显示您的 TODO 有多久了。
- [alexmozaidze/tree-comment.nvim](https://github.com/alexmozaidze/tree-comment.nvim) - 突出显示并配置 [tree-sitter-comment](https://github.com/stsewd/tree-sitter-comment) 的 TODO 注释。
- [terrortylor/nvim-comment](https://github.com/terrortylor/nvim-comment) - 使用内置的 commentstring 选项切换注释。
- [winston0410/commented.nvim](https://github.com/winston0410/commented.nvim) - 一个评论插件，支持计数和多种评论模式等等。
- [s1n7ax/nvim-comment-frame](https://github.com/s1n7ax/nvim-comment-frame) - 在源文件的基础上添加注释框。
- [danymat/neogen](https://github.com/danymat/neogen) - 更好的注释生成器，支持多种语言和注释约定。
- [nvim-mini/mini.nvim#mini.comment](https://github.com/nvim-mini/mini.nvim/blob/main/readmes/mini-comment.md) - 用于每行注释的“mini.nvim”模块。完全支持点重复。
- [LudoPinelli/comment-box.nvim](https://github.com/LudoPinelli/comment-box.nvim) - 使用方框和线条来澄清和美化您的评论。
- [JoosepAlviste/nvim-ts-context-commentstring](https://github.com/JoosepAlviste/nvim-ts-context-commentstring) - 根据文件中的光标位置设置“commentstring”选项。通过树保姆查询来检查位置。
- [LucasTavaresA/SingleComment.nvim](https://github.com/LucasTavaresA/SingleComment.nvim) - 始终单行，注释敏感，保留注释缩进。
- [Zeioth/dooku.nvim](https://github.com/Zeioth/dooku.nvim) - 生成并打开您的 HTML 代码文档。
- [georgeharker/comment-tasks.nvim](https://github.com/georgeharker/comment-tasks.nvim) - 让您的任务管理器及时了解代码中的 TODO 和 FIXME 注释。

### 折叠式

- [yaocccc/nvim-foldsign](https://github.com/yaocccc/nvim-foldsign) - 在标志栏上显示折叠。
- [soemre/commentless.nvim](https://github.com/soemre/commentless.nvim) - 折叠所有注释以更好地可视化您的代码逻辑，并在需要时展开它们。
- [jghauser/fold-cycle.nvim](https://github.com/jghauser/fold-cycle.nvim) - 循环折叠打开或关闭。
- [kevinhwang91/nvim-ufo](https://github.com/kevinhwang91/nvim-ufo) - 超折叠，具有现代外观和性能提升。
- [chrisgrieser/nvim-origami](https://github.com/chrisgrieser/nvim-origami) - 折叠时尽显优雅气质。
- [malbertzard/inline-fold.nvim](https://github.com/malbertzard/inline-fold.nvim) - 隐藏某些内联元素，例如长 CSS 类或“href”内容。
- [netmute/foldchanged.nvim](https://github.com/netmute/foldchanged.nvim) - 添加“FoldChanged”用户事件。
- [netmute/foldsigns.nvim](https://github.com/netmute/foldsigns.nvim) - 将折叠标记添加到符号列，以使折叠在编辑时更加明显。
<!--lint disable double-link -->
[**⬆ 回到顶部**](#contents)
<!--lint enable double-link -->

## 格式化

- [TheLazyCat00/simple-format](https://github.com/TheLazyCat00/simple-format) - 使用自定义正则表达式替换文本并突出显示组规则。
- [mhartington/formatter.nvim](https://github.com/mhartington/formatter.nvim) - 用 Lua 编写的格式运行程序。
- [sbdchd/neoformat](https://github.com/sbdchd/neoformat) - 代码格式化运行器。
- [cappyzawa/trim.nvim](https://github.com/cappyzawa/trim.nvim) - 修剪尾随空白和线条。
- [MunifTanjim/prettier.nvim](https://github.com/MunifTanjim/prettier.nvim) - 更漂亮的集成。
- [nvim-mini/mini.nvim#mini.align](https://github.com/nvim-mini/mini.nvim/blob/main/readmes/mini-align.md) - 用于交互式对齐文本的“mini.nvim”模块（带或不带即时预览）。
- [emileferreira/nvim-strict](https://github.com/emileferreira/nvim-strict) - 严格的本机代码风格格式，会暴露深层嵌套、超长行、尾随空白、尾随空行、TODO 和不一致的缩进。
- [~nedia/auto-format.nvim](https://git.sr.ht/~nedia/auto-format.nvim) - 设置自动命令以在保存时进行格式化，与本机 LSP 客户端格式化相比，更喜欢使用“null-ls”。
- [tenxsoydev/tabs-vs-spaces.nvim](https://github.com/tenxsoydev/tabs-vs-spaces.nvim) - 提示并修复偏离的缩进。
- [bennypowers/svgo.nvim](https://github.com/bennypowers/svgo.nvim) - 优化 SVG 文件。
- [niuiic/format.nvim](https://github.com/niuiic/format.nvim) - 一个异步、多任务、高度可配置的格式化插件。
- [elentok/format-on-save.nvim](https://github.com/elentok/format-on-save.nvim) - 结合了 LSP 和非 LSP 格式化的同步格式化程序（例如 `shfmt`、`stylua`、`prettier`）。专门针对保存时格式化。
- [stevearc/conform.nvim](https://github.com/stevearc/conform.nvim) - 与 LSP 配合良好的轻量级格式化引擎。
- [nvimdev/guard.nvim](https://github.com/nvimdev/guard.nvim) - 极简异步格式化和 linting 插件。
- [paul-louyot/toggle-quotes.nvim](https://github.com/paul-louyot/toggle-quotes.nvim) - 在引号之间切换。
- [wsdjeg/format.nvim](https://github.com/wsdjeg/format.nvim) - 异步代码格式化插件。

### 缩进

- [saghen/blink.indent](https://github.com/saghen/blink.indent) - 高性能缩进指南，每次击键都有范围。
- [nvimdev/indentmini.nvim](https://github.com/nvimdev/indentmini.nvim) - 一个使用 `nvim_set_decoration_provide` API 函数的最小且快速的缩进插件。
- [lukas-reineke/indent-blankline.nvim](https://github.com/lukas-reineke/indent-blankline.nvim) - Lua 中的 IndentLine 替代品具有更多功能和 Tree-sitter 支持。
- [LucasTavaresA/simpleIndentGuides.nvim](https://github.com/LucasTavaresA/simpleIndentGuides.nvim) - 使用内置变量的缩进指南。
- [nvim-mini/mini.nvim#mini.indentscope](https://github.com/nvim-mini/mini.nvim/blob/main/readmes/mini-indentscope.md) - 用于在缩进范围内可视化和操作的“mini.nvim”模块。支持自定义去抖延迟、动画风格以及范围计算算法的不同粒度选项。
- [NMAC427/guess-indent.nvim](https://github.com/NMAC427/guess-indent.nvim) - 自动压痕样式检测。
- [Darazaki/indent-o-matic](https://github.com/Darazaki/indent-o-matic) - 用 Lua 编写的愚蠢的自动快速压痕检测。
- [yaocccc/nvim-hlchunk](https://github.com/yaocccc/nvim-hlchunk) - 突出显示“{}”块。
- [shellRaining/hlchunk.nvim](https://github.com/shellRaining/hlchunk.nvim) - `nvim-hlchunk` 的 Lua 实现，包含更多功能，例如突出显示 `{}` 块、缩进、空格等。
- [VidocqH/auto-indent.nvim](https://github.com/VidocqH/auto-indent.nvim) - 当光标位于第一列并按“<TAB>”键时自动缩进光标，就像 VSCode 一样。
- [Mr-LLLLL/cool-chunk.nvim](https://github.com/Mr-LLLLL/cool-chunk.nvim) - 通过动画更简单、更快速地进行分块。
- [gh-liu/fold_line.nvim](https://github.com/gh-liu/fold_line.nvim) - 表示代码折叠的行，通过`:set fdm=indent`可以达到类似缩进的效果。
<!--lint disable double-link -->
[**⬆ 回到顶部**](#contents)
<!--lint enable double-link -->

## 命令行

- [notomo/cmdbuf.nvim](https://github.com/notomo/cmdbuf.nvim) - 替代命令行窗口插件。
- [gelguy/wilder.nvim](https://github.com/gelguy/wilder.nvim) - 模糊命令行自动完成的插件。
- [vzze/cmdline.nvim](https://github.com/vzze/cmdline.nvim) - 具有模糊自动完成功能的类似螺旋的命令行。
- [nvim-mini/mini.nvim#mini.cmdline](https://github.com/nvim-mini/mini.nvim/blob/main/readmes/mini-cmdline.md) - 用于命令行调整的“mini.nvim”模块。添加具有可自定义延迟的自动完成、具有固定候选词的自动更正以及浮动窗口中的自动查看命令范围。
<!--lint disable double-link -->
[**⬆ 回到顶部**](#contents)
<!--lint enable double-link -->

## 会议

- [rmagatti/auto-session](https://github.com/rmagatti/auto-session) - 一个小型的自动化会话管理器。
- [nvim-mini/mini.nvim#mini.sessions](https://github.com/nvim-mini/mini.nvim/blob/main/readmes/mini-sessions.md) - 用于会话管理（读、写、删除）的“mini.nvim”模块。
- [gennaro-tedesco/nvim-possession](https://github.com/gennaro-tedesco/nvim-possession) - 严肃的会话管理器。
- [olimorris/persisted.nvim](https://github.com/olimorris/persisted.nvim) - 通过 Git 分支、自动保存/自动加载和 Telescope 支持进行简单的会话管理。
- [folke/persistence.nvim](https://github.com/folke/persistence.nvim) - 简单的自动化会话管理。
- [Shatur/neovim-session-manager](https://github.com/Shatur/neovim-session-manager) - 围绕 :mksession 的简单包装。
- [jedrzejboczar/possession.nvim](https://github.com/jedrzejboczar/possession.nvim) - 灵活的会话管理，任意持久数据存储为 JSON。
- [niuiic/multiple-session.nvim](https://github.com/niuiic/multiple-session.nvim) - 提供多会话管理功能。
- [coffebar/neovim-project](https://github.com/coffebar/neovim-project) - 声明式项目管理，自动保存会话，使用 Telescope。
- [njayman/season.nvim](https://github.com/njayman/season.nvim) - 一个轻量级插件，用于根据当前工作目录管理会话。
- [Akmadan23/local-session.nvim](https://github.com/Akmadan23/local-session.nvim) - 一个快速、最小、隐式的基于当前工作目录的会话管理器，可以在 Lua 中轻松配置会话文件。
<!--lint disable double-link -->
[**⬆ 回到顶部**](#contents)
<!--lint enable double-link -->

## 远程开发

- [inhesrom/remote-ssh.nvim](https://github.com/inhesrom/remote-ssh.nvim) - 复制 VSCode 的 Remote-SSH 插件的基本底层功能，重点关注本地编辑体验，以避免远程“滞后”。浏览远程文件，通过完整的本地编辑体验编辑“远程缓冲区”（LSP、Tree-sitter、Telescope 集成和文件观察器）。
- [chipsenkbeil/distant.nvim](https://github.com/chipsenkbeil/distant.nvim) - 在舒适的本地环境中编辑文件、运行程序并在远程计算机上使用 LSP。
- [jamestthompson3/nvim-remote-containers](https://github.com/jamestthompson3/nvim-remote-containers) - 在 Docker 容器内进行开发，就像 VSCode 一样。
- [esensar/nvim-dev-container](https://github.com/esensar/nvim-dev-container) - 提供与 VSCode 的[远程容器开发](https://code.visualstudio.com/docs/remote/containers)插件类似的功能，以及支持在 Docker 容器中进行开发的其他功能。
- [miversen33/netman.nvim](https://github.com/miversen33/netman.nvim) - Lua 驱动的网络资源管理器。
- [niuiic/remote.nvim](https://github.com/niuiic/remote.nvim) - 使用本地配置编辑远程文件。
- [uhs-robert/sshfs.nvim](https://github.com/uhs-robert/sshfs.nvim) - 通过 SSHFS 安装远程系统，并具有智能选择器自动检测功能（Telescope/Oil/Snacks/Neo-tree/fzf-lua/Yazi/Ranger 等）。
- [nosduco/remote-sshfs.nvim](https://github.com/nosduco/remote-sshfs.nvim) - 通过 SSHFS 在远程计算机上探索、编辑和开发。
- [azratul/live-share.nvim](https://github.com/azratul/live-share.nvim) - 提供随时随地的远程协作功能，非常适合结对编程场景。
<!--lint disable double-link -->
[**⬆ 回到顶部**](#contents)
<!--lint enable double-link -->

## 实时预览

- [hat0uma/prelive.nvim](https://github.com/hat0uma/prelive.nvim) - 一个简单的基于 luv 的开发服务器，具有实时重新加载功能。
- [hat0uma/doxygen-previewer.nvim](https://github.com/hat0uma/doxygen-previewer.nvim) - Doxygen 文档的实时预览。
- [brianhuster/live-preview.nvim](https://github.com/brianhuster/live-preview.nvim) - 在浏览器中实时预览 HTML、Markdown 和 Asciidoc。
- [SUSTech-data/neopyter](https://github.com/SUSTech-data/neopyter) - 在 Neovim 中编辑并在 Jupyter Lab 中预览/运行。
- [kiyoon/jupynium.nvim](https://github.com/kiyoon/jupynium.nvim) - Selenium 自动化的 Jupyter Notebook 与 Neovim 实时同步。
- [gruvw/strudel.nvim](https://github.com/gruvw/strudel.nvim) - [strudel](https://strudel.cc) 的实时编码控制器。
- [ritschalex/jupyter_ascending.nvim](https://github.com/RitschAlex/jupyter_ascending.nvim) - 使用 Jupyter Ascending 无缝使用 Jupyter Notebook。
<!--lint disable double-link -->
[**⬆ 回到顶部**](#contents)
<!--lint enable double-link -->

## 分割和窗口

- [wsdjeg/tabman.nvim](https://github.com/wsdjeg/tabman.nvim) - 在选项卡及其包含的窗口之间导航。
- [~henriquehbr/ataraxis.lua](https://sr.ht/~henriquehbr/ataraxis.lua) - 用于提高代码可读性的禅宗模式。
- [yorickpeterse/nvim-window](https://github.com/yorickpeterse/nvim-window) - 轻松在窗口之间跳转。
- [sindrets/winshift.nvim](https://github.com/sindrets/winshift.nvim) - 轻松重新布置您的窗户。
- [nvim-focus/focus.nvim](https://github.com/nvim-focus/focus.nvim) - 用 Lua 编写的自动聚焦和自动调整分割/窗口大小！ Vim 在类固醇的帮助下分裂了。
- [anuvyklack/windows.nvim](https://github.com/anuvyklack/windows.nvim) - 自动扩展当前窗口的宽度。最大化并恢复它。所有这一切都带有精美的动画。
- [nvim-zh/colorful-winsep.nvim](https://github.com/nvim-zh/colorful-winsep.nvim) - 可配置的颜色分割线。
- [nyngwang/NeoNoName.lua](https://github.com/nyngwang/NeoNoName.lua) - 保留布局的缓冲区删除。
- [nvim-mini/mini.nvim#mini.bufremove](https://github.com/nvim-mini/mini.nvim/blob/main/readmes/mini-bufremove.md) - `mini.nvim` 模块用于在保存窗口布局时删除缓冲区（取消显示、删除、擦除）。
- [jyscao/ventana.nvim](https://github.com/jyscao/ventana.nvim) - 方便地翻转和移动您的窗口布局。
- [mrjones2014/smart-splits.nvim](https://github.com/mrjones2014/smart-splits.nvim) - 智能、无缝、定向导航和调整拆分大小。
- [altermo/nwm](https://github.com/altermo/nwm) - X11 窗口管理器。
- [MisanthropicBit/winmove.nvim](https://github.com/MisanthropicBit/winmove.nvim) - 轻松移动、交换窗口和调整窗口大小。
- [ycdzj/win-mover.nvim](https://github.com/ycdzj/win-mover.nvim) - 避免移动侧窗的窗户移动器。
- [mkajsjo/windowcolumns.nvim](https://github.com/mkajsjo/windowcolumns.nvim) - 列优先窗口管理。
- [aronjohanns/smooth-resize.nvim](https://github.com/aronjohanns/smooth-resize.nvim) - 使用默认的窗口调整大小映射平滑、连续地调整窗口大小。

### 多路复用器

- [aserowy/tmux.nvim](https://github.com/aserowy/tmux.nvim) - Tmux 集成具有窗格移动和调整大小的功能。
- [danielpieper/telescope-tmuxinator.nvim](https://github.com/danielpieper/telescope-tmuxinator.nvim) - tmuxinator 与 Telescope.nvim 的集成。
- [hkupty/nvimux](https://github.com/hkupty/nvimux) - 使用 Neovim 作为 tmux 替代品。
- [numToStr/Navigator.nvim](https://github.com/numToStr/Navigator.nvim) - 在 Neovim 拆分和 tmux 窗格之间顺畅导航。
- [declancm/windex.nvim](https://github.com/declancm/windex.nvim) - 窗口函数的集合，包括在 Neovim 分割和 tmux 窗格之间移动、关闭和最大化。
- [karnull/only-tmux.nvim](https://github.com/karnull/only-tmux.nvim) - 在同一窗口中使用 tmux 窗格扩展 `:only` 的功能，将它们移动到新窗口或关闭它们。
- [karshPrime/tmux-compile.nvim](https://github.com/karshPrime/tmux-compile.nvim) - 设置相同的键（如 F5）来运行每种语言的任何编译/运行命令，如 C 的“make”和 Rust 的“cargo build”，并让项目在新的 tmux 窗格或窗口中运行或编译。
- [EvWilson/slimux.nvim](https://github.com/EvWilson/slimux.nvim) - 将内容从当前缓冲区发送到可配置的 tmux 窗格。
- [juselara1/tmutils.nvim](https://github.com/juselara1/tmutils.nvim) - Tmux 实用程序支持发送线路、捕获内容、创建终端和管理 REPL。
- [kiyoon/tmux-send.nvim](https://github.com/kiyoon/tmux-send.nvim) - 将“nvim-tree”、“neo-tree”或“oil.nvim”中的缓冲区内容或文件路径复制并粘贴到另一个 tmux 窗格。
- [jkeresman01/tmux-switch.nvim](https://github.com/jkeresman01/tmux-switch.nvim) - 为 Tmux 提供模糊会话切换。
- [salorak/libtmux.nvim](https://github.com/salorak/libtmux.nvim) - 用于使用“tmux”API 的瘦包装器。
<!--lint disable double-link -->
[**⬆ 回到顶部**](#contents)
<!--lint enable double-link -->

## 游戏

- [alec-gibson/nvim-tetris](https://github.com/alec-gibson/nvim-tetris) - 将 Emacs 最大的功能带到 Neovim - 俄罗斯方块。
- [seandewar/nvimesweeper](https://github.com/seandewar/nvimesweeper) - 在您最喜欢的文本编辑器中玩扫雷。
- [seandewar/killersheep.nvim](https://github.com/seandewar/killersheep.nvim) - 杀人羊的港口。
- [rktjmp/playtime.nvim](https://github.com/rktjmp/playtime.nvim) - 空当接龙、深圳纸牌、密使等游戏合集。
- [Eandrju/cellular-automaton.nvim](https://github.com/Eandrju/cellular-automaton.nvim) - 它可以让您根据当前缓冲区的内容执行美观的细胞自动机动画。
- [alanfortlink/blackjack.nvim](https://github.com/alanfortlink/blackjack.nvim) - 经典的黑杰克游戏。
- [jim-fx/sudoku.nvim](https://github.com/jim-fx/sudoku.nvim) - 经典数独谜题。
- [csessh/aoc.vim](https://github.com/csessh/aoc.nvim) - 简单的小精灵，为您获取“代码降临”谜题输入。
- [seandewar/actually-doom.nvim](https://github.com/seandewar/actually-doom.nvim) - 编辑文本很无聊；玩《DOOM》吧！
- [piersolenski/skifree.nvim](https://github.com/piersolenski/skifree.nvim) - 玩 Windows 3.1 SkiFree 游戏。
- [xiangnongWu2233/rubiks-cube.nvim](https://github.com/xiangnongWu2233/rubiks-cube.nvim) - 带有自动解算器的可玩魔方。

### 竞争性编程

- [~chinmay/cphelper.nvim](https://git.sr.ht/~chinmay/cphelper.nvim) - 用 Lua 编写的竞争性编程的助手。
- [xeluxee/competitest.nvim](https://github.com/xeluxee/competitest.nvim) - 一个自动测试用例管理和检查竞争性编程竞赛的插件。
- [barrettruth/cp.nvim](https://github.com/barrettruth/cp.nvim) - 适用于流行竞赛平台（CodeForces、CSES 等）的竞争性编程工作流程，包括自动测试抓取、I/O 视图和差异面板。
- [kawre/leetcode.nvim](https://github.com/kawre/leetcode.nvim) - 解决 Leetcode 问题。
- [2KAbhishek/exercism.nvim](https://github.com/2KAbhishek/exercism.nvim) - 浏览并解决锻炼问题。
<!--lint disable double-link -->
[**⬆ 回到顶部**](#contents)
<!--lint enable double-link -->

## 玩具

- [folke/drop.nvim](https://github.com/folke/drop.nvim) - 支持仪表板的屏幕保护程序。
- [axsaucedo/neovim-power-mode](https://github.com/axsaucedo/neovim-power-mode) - 为您的编辑器提供组合计数器、粒子效果和爆炸。
- [jerrywang1981/keystroke.nvim](https://github.com/jerrywang1981/keystroke.nvim) - 键入时播放声音并执行其他操作。
- [cxwx/keywound.nvim](https://github.com/cxwx/keysound.nvim) - 每次击键都会播放声音，支持自定义声音。
<!--lint disable double-link -->
[**⬆ 回到顶部**](#contents)
<!--lint enable double-link -->

## 工作流程

- [letieu/jira.nvim](https://github.com/letieu/jira.nvim) - 使用漂亮的 UI 管理 Jira 任务。
- [m4xshen/hardtime.nvim](https://github.com/m4xshen/hardtime.nvim) - 帮助您建立良好的指挥流程和习惯。
- [saxon1964/neovim-tips](https://github.com/saxon1964/neovim-tips) - 提供数百个内置提示、技巧和快捷方式，具有自定义选择器界面，并且能够添加您自己的提示。
- [ecthelionvi/NeoComposer.nvim](https://github.com/ecthelionvi/NeoComposer.nvim) - 简化宏观管理、提高生产力并创建和谐的工作流程。
- [yagiziskirik/AirSupport.nvim](https://github.com/yagiziskirik/AirSupport.nvim) - 用于自定义快捷方式和命令的可搜索提醒窗口。
- [emrearmagan/atlas.nvim](https://github.com/emrearmagan/atlas.nvim) - 适用于 GitHub、GitLab、Bitbucket 和 Jira 的单一工作流程。
- [mateuszwieloch/automkdir.nvim](https://github.com/mateuszwieloch/automkdir.nvim) - 写入文件时自动创建不存在的父目录。
- [jghauser/mkdir.nvim](https://github.com/jghauser/mkdir.nvim) - 保存文件时自动创建丢失的目录。

### 统计追踪

- [aikhe/wrapped.nvim](https://github.com/aikhe/wrapped.nvim) - 通过统计数据、见解、历史记录、热图等可视化并检查您的配置活动。
- [gisketch/triforce.nvim](https://github.com/gisketch/triforce.nvim) - 游戏化的统计跟踪器，带有 XP、级别、成就和活动热图，适用于您与 lualine 集成的编码会话。
- [QuentinGruber/pomodoro.nvim](https://github.com/QuentinGruber/pomodoro.nvim) - 使用具有内置会话跟踪和休息提醒的番茄工作法。
- [gaborvecsei/usage-tracker.nvim](https://github.com/gaborvecsei/usage-tracker.nvim) - 跟踪您的 Neovim 使用情况并轻松可视化统计数据。
- [SunnyTamang/pendulum.nvim](https://github.com/SunnyTamang/pendulum.nvim) - 简单的计时器，用于为编码员、竞争性程序员、开发人员等创建基于时间的高效会话。
- [ptdewey/pendulum-nvim](https://github.com/ptdewey/pendulum-nvim) - 通过按需时间报告跟踪编码所花费的时间并收集见解。
- [ravsii/timers.nvim](https://github.com/ravsii/timers.nvim) - 计时器管理器，一个干净的 Lua API，支持多个计时器、持久性、UI 和插件集成。
- [Rtarun3606k/takatime](https://github.com/Rtarun3606k/takatime) - 使用 Go 和 MongoDB 的隐私优先 WakaTime 替代方案。
- [taigrr/blast.nvim](https://github.com/taigrr/blast.nvim) - NvimBlast 的活动跟踪客户端，具有按项目配置、monorepo 支持和隐私控制。
<!--lint disable double-link -->
[**⬆ 回到顶部**](#contents)
<!--lint enable double-link -->

## 数据库

- [zongben/dbout.nvim](https://github.com/zongben/dbout.nvim) - 管理数据库连接并直接使用 JSON 结果运行 SQL 查询。
- [kndndrj/nvim-dbee](https://github.com/kndndrj/nvim-dbee) - 交互式数据库客户端。
- [tashikomaaa/neomongo.nvim](https://github.com/tashikomaaa/neomongo.nvim) - 直接通过 Telescope 支持的仪表板探索、查询和编辑 MongoDB 集合。
- [zerochae/dbab.nvim](https://github.com/zerochae/dbab.nvim) - 具有现代 UI 和异步执行的轻量级数据库客户端。
- [joryeugene/dadbod-grip.nvim](https://github.com/joryeugene/dadbod-grip.nvim) - 具有内联单元格编辑功能的数据库编辑器、具有实时 SQL 预览的分阶段突变、模式浏览器、DDL、AI SQL 生成、FK 导航和 DuckDB/Parquet 支持。
- [clang-engineer/dadbod-vertica.nvim](https://github.com/clang-engineer/dadbod-vertica.nvim) - 通过官方 `vsql` 客户端实现 [vim-dadbod](https://github.com/tpope/vim-dadbod) 的 Vertica 适配器，并为 `vim-dadbod-ui` 提供架构树集成。
<!--lint disable double-link -->
[**⬆ 回到顶部**](#contents)
<!--lint enable double-link -->

## 预制配置

- [tokiory/neovim-boilerplate](https://github.com/tokiory/neovim-boilerplate) - 用于进行新配置的入门样板。
- [frans-johansson/lazy-nvim-starter](https://github.com/frans-johansson/lazy-nvim-starter) - 带有惰性插件管理器的入门样板。
- [abdellatif-temsamani/adev.nvim](https://github.com/abdellatif-temsamani/adev.nvim) - 经过过度设计的 Neovim 发行版，适合想要一切的开发人员。
- [pgosar/CyberNvim](https://github.com/pgosar/CyberNvim) - 世界上最简单、最可扩展的 Neovim 发行版。
- [sontungexpt/stinvim](https://github.com/sontungexpt/stinvim) - 全栈开发人员的配置。
- [Abstract-IDE/Abstract](https://github.com/Abstract-IDE/Abstract) - 配置以实现 Modern IDE 的强大功能。
- [SpaceVim/SpaceVim](https://spacevim.org) - 社区驱动的模块化 Vim/Neovim 发行版，灵感来自“spacemacs”。
- [CosmicNvim/CosmicNvim](https://github.com/CosmicNvim/CosmicNvim) - CosmicNvim 是一个轻量级且固执的 Web 开发配置，专门设计用于提供 COSMIC 编程体验。
- [artart222/CodeArt](https://github.com/artart222/CodeArt) - 完全用 Lua 编写的快速通用 IDE，带有适用于 Linux/Windows/macOS 的安装程序以及用于更新它的内置 `:CodeArtUpdate` 命令。
- [LazyVim/LazyVim](https://github.com/LazyVim/LazyVim) - 由 **lazy.nvim** 提供支持的成熟 IDE，可轻松自定义和扩展您的配置。
- [legobeat/l7-devenv](https://github.com/legobeat/l7-devenv) - 以安全为中心的 IDE，具有基于 Neovim 和 shell 的可破解（以正确的方式）框架。
- [crispybaccoon/chaivim](https://github.com/crispybaccoon/chaivim) - 易于配置的发行版，具有可靠的默认值和舒适的编辑器体验。
- [crivotz/nv-ide](https://github.com/crivotz/nv-ide) - 面向全栈开发人员的自定义配置（Rails、Ruby、PHP、HTML、CSS、SCSS、JavaScript）。
- [LunarVim/LunarVim](https://github.com/LunarVim/LunarVim) - 该项目旨在帮助人们从 VSCode 过渡到卓越的文本编辑体验。
- [hackorum/VapourNvim](https://github.com/hackorum/VapourNvim) - 配置以获得类似 Vim IDE 的终极体验。
- [siduck76/NvChad](https://github.com/siduck76/NvChad) - 尝试使 Neovim 的 CLI 与 IDE 一样实用，同时保持美观，减少臃肿。
- [cstsunfu/.sea.nvim](https://github.com/cstsunfu/.sea.nvim) - 模块化配置，具有漂亮的用户界面和一些有用的功能，例如番茄钟和窗口号码。
- [shaeinst/roshnivim](https://github.com/shaeinst/roshnivim) - 预定义的配置可以节省您数千个小时来将 Neovim 设置为 IDE。
- [AstroNvim/AstroNvim](https://github.com/AstroNvim/AstroNvim) - 美观且功能丰富的配置，可扩展且易于使用一组出色的插件。
- [shaunsingh/nyoom.nvim](https://github.com/shaunsingh/nyoom.nvim) - 用 Fennel 编写的速度极快、可配置、最小且“lispy”配置。
- [jrychn/moduleVim](https://github.com/jrychn/ModuleVim) - 后端和前端非常易于使用，自动安装 LSP。
- [imbacraft/dusk.nvim](https://github.com/imbacraft/dusk.nvim) - 一个轻量级的、美观的最小配置，用 Lua 编写，能够提供 Web 和 Java 开发。
- [nvim-lua/kickstart.nvim](https://github.com/nvim-lua/kickstart.nvim) - 您个人 Neovim 配置的启动点。
- [dam9000/kickstart-modular.nvim](https://github.com/dam9000/kickstart-modular.nvim) - 这是 nvim-lua/kickstart.nvim 的一个分支，从单个文件移动到多文件配置。
- [cunderw/nvim](https://github.com/cunderw/nvim) - 用于 JS/TS、Go 和 Java 开发的自定义、类似 IDE 的配置。
- [ldelossa/nvim-ide](https://github.com/ldelossa/nvim-ide) - 深受 VSCode 启发的全功能 IDE 层。
- [linrongbin16/lin.nvim](https://github.com/linrongbin16/lin.nvim) - 受“spf13-vim”启发，高度配置的 Neovim 发行版集成了大量用于开发的实用程序。
- [doctorfree/nvim-lazyman](https://github.com/doctorfree/nvim-lazyman) - 配置管理器和它自己的模块化配置。支持 40 多种预配置。
- [NormalNvim/NormalNvim](https://github.com/NormalNvim/NormalNvim) - 配置注重日常工作的稳定性。
- [chrisgrieser/nvim-kickstart-python](https://github.com/chrisgrieser/nvim-kickstart-python) - Neovim 配置的启动点（适用于 Python）。
- [mrcjkb/kickstart-nix.nvim](https://github.com/mrcjkb/kickstart-nix.nvim) - 用于 Neovim 派生的简单 [Nix flake](https://wiki.nixos.org/wiki/Flakes) 模板存储库，目标是简化从现有 Neovim 配置的迁移。
- [drybalka/clean.nvim](https://github.com/drybalka/clean.nvim) - 清理默认的按键映射和插件，只留下最基本的构建基础。
- [StratOS-Linux/StratVIM](https://github.com/StratOS-Linux/StratVIM) - 默认情况下，成熟的 Neovim 发行版包含在 [StratOS-Linux](https://github.com/StratOS-Linux) 中。
- [Shaobin-Jiang/IceNvim](https://github.com/Shaobin-Jiang/IceNvim) - 一个漂亮、强大、可定制的配置，速度非常快。
- [ayamir/nvimdots](https://github.com/ayamir/nvimdots) - 具有 NixOS 支持的良好配置和结构化配置。
- [adoyle-h/one.nvim](https://github.com/adoyle-h/one.nvim) - Lua 中的一体化配置框架。
- [nvim-mini/MiniMax](https://github.com/nvim-mini/MiniMax) - 一系列独立且经过广泛评论的配置，主要使用 MINI 工具。
- [TheItcor/MoaiVim](https://github.com/TheItcor/MoaiVim) - 模拟轻量级 IDE 的极简配置。
- [plutowang/nvim.pack](https://github.com/plutowang/nvim.pack) - 纯粹基于本机 Vim.pack 构建的声明式、事件驱动的延迟加载配置，可实现极高的启动性能。
<!--lint disable double-link -->
[**⬆ 回到顶部**](#contents)
<!--lint enable double-link -->

## 外部

这些工具在 Neovim 外部使用，以增强体验。

### 版本管理器

- [MordechaiHadad/bob](https://github.com/MordechaiHadad/bob) - 跨平台、易于使用的 Neovim 版本管理器。
- [NTBBloodbath/nvenv](https://github.com/NTBBloodbath/nvenv) - 一个轻量级且速度极快的 Neovim 版本管理器。
- [y3owk1n/nvs](https://github.com/y3owk1n/nvs) - 另一个带配置切换器的 Neovim 版本管理器。

### 插件模板

- [gennaro-tedesco/boilit](https://github.com/gennaro-tedesco/boilit) - 创建样板结构插件。
- [m00qek/plugin-template.nvim](https://github.com/m00qek/plugin-template.nvim) - 用于设置测试基础设施和 GitHub Actions 的插件模板。
- [ellisonleao/nvim-plugin-template](https://github.com/ellisonleao/nvim-plugin-template) - 另一个 Neovim 插件模板，使用了 GitHub 的模板功能。
- [2KAbhishek/template.nvim](https://github.com/2KAbhishek/template.nvim) - 用于快速启动插件开发的自以为模板。
- [jkeresman01/spring-initializr.nvim](https://github.com/jkeresman01/spring-initializr.nvim) - 具有 Telescope 支持的 UI 的 Scaffold Spring Boot 项目。
- [DrKJeff16/nvim-plugin-boilerplate](https://github.com/DrKJeff16/nvim-plugin-boilerplate) - 由脚本生成的新插件的文档模板。包括测试、CI 实用程序等。
- [chrisgrieser/nvim-pseudometa-plugin-template](https://github.com/chrisgrieser/nvim-pseudometa-plugin-template) - 新 Neovim 插件的模板。

### 特定于操作系统

- [chrisgrieser/alfred-neovim-utilities](https://github.com/chrisgrieser/alfred-neovim-utilities) - 通过 Alfred (macOS) 搜索 Neovim 插件和在线“:help”。
- [iamironz/android-nvim-plugin](https://github.com/iamironz/android-nvim-plugin) - 与 Gradle 集成的 Android 构建、部署和 logcat 命令。
- [massix/termux.nvim](https://github.com/massix/termux.nvim) - 与 Termux API 交互，可用于收集有关 Android 手机的各种信息以在状态行中显示（例如电池电量）。
- [m15a/flake-awesome-neovim-plugins](https://github.com/m15a/flake-awesome-neovim-plugins) - Nix flake 提供了一系列“awesome-neovim”插件作为 Nix 包。
<!--lint disable double-link -->
[**⬆ 回到顶部**](#contents)
<!--lint enable double-link -->

## 愿望清单

有插件可以解决的问题吗？将其添加到 [nvim-lua 愿望清单](https://github.com/nvim-lua/wishlist)。
<!--lint disable double-link -->
[**⬆ 回到顶部**](#contents)
<!--lint enable double-link -->

## 用户界面

- [OXY2DEV/ui.nvim](https://github.com/OXY2DEV/ui.nvim) - 用于自定义 UI 的蓝图/模板/指南。
- [mcauley-penney/visual-whitespace.nvim](https://github.com/mcauley-penney/visual-whitespace.nvim) - 查看视觉选择中的空白字符，例如 VSCode。
- [jrop/tuis.nvim](https://github.com/jrop/tuis.nvim) - 交互式 TUI 的集合，为各种 CLI 提供丰富的交互式 UI。
- [matbme/JABS.nvim](https://github.com/matbme/JABS.nvim) - 漂亮且最小的缓冲区切换器窗口。
- [rcarriga/nvim-notify](https://github.com/rcarriga/nvim-notify) - 一个精美的、可配置的通知管理器。
- [nvim-mini/mini.nvim#mini.notify](https://github.com/nvim-mini/mini.nvim/blob/main/readmes/mini-notify.md) - “mini.nvim”模块，用于在单个窗口中显示一个或多个突出显示的通知。提供 `vim.notify()` 实现的制造商并设置自动 LSP 进度更新。
- [folke/noice.nvim](https://github.com/folke/noice.nvim) - 高度实验性的插件，完全取代了消息、命令行和弹出菜单的 UI。
- [toppair/reach.nvim](https://github.com/toppair/reach.nvim) - 缓冲区、标记、标签页切换器。
- [ghillb/cybu.nvim](https://github.com/ghillb/cybu.nvim) - 循环缓冲区时显示带有上下文的通知窗口。
- [CosmicNvim/cosmic-ui](https://github.com/CosmicNvim/cosmic-ui) - Cosmic-UI 是特定 Vim 功能的简单包装。
- [sitiom/nvim-numbertoggle](https://github.com/sitiom/nvim-numbertoggle) - 自动在相对行号和绝对行号之间切换。
- [nkakouros-original/numbers.nvim](https://github.com/nkakouros-original/numbers.nvim) - 只要有意义就切换相对数字。
- [cpea2506/relative-toggle.nvim](https://github.com/cpea2506/relative-toggle.nvim) - 数字与相对数字之间平滑切换，支持多种数字组合，高度可定制。
- [LukasPietzschmann/telescope-tabs](https://github.com/LukasPietzschmann/telescope-tabs) - 使用望远镜在选项卡之间快速导航。
- [ariel-frischer/bmessages.nvim](https://github.com/ariel-frischer/bmessages.nvim) - 用可配置的自动更新缓冲区替换默认的“:messages”窗口。
- [markgandolfo/lightswitch.nvim](https://github.com/markgandolfo/lightswitch.nvim) - 使用“nui.nvim”库切换各种选项。
- [wsdjeg/calendar.nvim](https://github.com/wsdjeg/calendar.nvim) - 一个简单的浮动日历，支持扩展。
- [xieyonn/spinner.nvim](https://github.com/xieyonn/spinner.nvim) - 可扩展的微调框架，用于状态行、选项卡、winbar、缓冲区、cmdline 或光标旁边的动画微调器。
- [quickui.nvim](https://github.com/mjmjm0101/quickui.nvim) - 结构化、键盘驱动的菜单和带有嵌套导航的上下文菜单。
- [ln.nvim](https://github.com/markosnarinian/ln.nvim) - 活动窗口上的相对数字，其他地方的绝对数字。
- [nvim-mini/mini.nvim#mini.input](https://github.com/nvim-mini/mini.nvim/blob/main/readmes/mini-input.md) - “mini.nvim”模块，用于通过完全可定制的键和视图处理获取用户输入。可以显示为浮动窗口、状态行/选项卡/winbar、虚拟行/文本。提供 `vim.ui.input()` 实现。
<!--lint disable double-link -->
[**⬆ 回到顶部**](#contents)
<!--lint enable double-link -->

## 资源

- [Vimawesome](https://vimawesome.com/) - 展示 Vim 的各种插件，并为其他 Neovim 相关插件提供 [Neovim 标签](https://vimawesome.com/?q=tag:neovim)。
- [akrawchyk/awesome-vim#tools](https://github.com/akrawchyk/awesome-vim#tools) - Vim 插件和有用指南的简短列表。
- [Neovimcraft](https://neovimcraft.com) - 一个致力于搜索特定插件和在 Lua 中构建插件的指南的网站。
- [Dotfyle](https://dotfyle.com) - 用于共享和发现 Neovim 配置和插件的站点。
- [NeoLand](https://neoland.dev) - 一个制作精美的 Neovim 资源网站。
- [Weyaaron/nvim-training](https://github.com/Weyaaron/nvim-training) - 这是一款适合初学者的工具，可通过可重复的小任务来训练您的“肌肉记忆”。
- [Nvim.app](https://nvim.app) - Neovim 插件的现代搜索界面，为插件作者提供模糊搜索、过滤和自助更新。
- [ChuYanLon/chad46](https://github.com/ChuYanLon/chad46) - 94 个主题与 44 个亮点集成，每天从 NvChad/base46 同步。
<!--lint disable double-link -->
[**⬆ 回到顶部**](#contents)
<!--lint enable double-link -->
