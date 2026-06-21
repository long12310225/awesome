<!-- lint ignore awesome-git-repo-age -->

# 很棒的 WezTerm [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

<img src="https://raw.githubusercontent.com/wez/wezterm/main/assets/icon/wezterm-icon.svg" align="right" width="144" />

> 很棒的 WezTerm 插件集合。 [插件指南](https://github.com/wezterm/wezterm/blob/main/docs/config/plugins.md)。发现一些很酷的东西？请[贡献](CONTRIBUTING.md)！

[WezTerm](https://wezfurlong.org/wezterm/) 是一个强大的跨平台终端模拟器和多路复用器，由 [@wez](https://github.com/wez) 编写，并在 [Rust](https://www.rust-lang.org) 中实现。

要增强您的 WezTerm 配置体验：

- [DrKJeff16/wezterm-types](https://github.com/DrKJeff16/wezterm-types) - WezTerm 类型注释可以作为补全源添加到编辑器中，以便在使用 WezTerm 的 Lua API 时提供代码帮助。包括社区插件支持。

## 内容

- [AI](#ai)
- [Keybinding](#keybinding)
- [Media](#media)
- [Neovim](#neovim)
- [Panes](#panes)
- [Session](#session)
- [标签栏](#tab-bar)
- [Themes](#themes)
- [Utility](#utility)

## 人工智能

- [Michal1993r/ai-helper.wezterm](https://github.com/Michal1993r/ai-helper.wezterm/tree/master) - 向 AI 请求 LM Studio 或 Google Gemini 的 CLI 帮助。
- [dimao/ai-commander.wezterm](https://github.com/dimao/ai-commander.wezterm) - 根据自然语言提示生成并选择 bash 命令。
- [EdenGibson/wezterm-quota-limit](https://github.com/EdenGibson/wezterm-quota-limit) - 在状态栏中显示 Claude API 使用配额，并带有颜色编码阈值和自动令牌刷新。
- [Eric162/wezterm-agent-deck](https://github.com/Eric162/wezterm-agent-deck) - 监控 AI 编码代理，在选项卡中显示状态点，并在代理需要关注时发出通知。
- [M-Marbouh/agent-quota.wezterm](https://github.com/M-Marbouh/agent-quota.wezterm) - 在状态栏中显示 Claude 和 Codex 配额使用情况，包括重置倒计时、进程感知状态和共享缓存。

## 按键绑定

- [MLFlexer/modal.wezterm](https://github.com/MLFlexer/modal.wezterm) - 预定义的类似 Vim 的模式键绑定，具有美观的 UI。
- [sravioli/chord.wz](https://github.com/sravioli/chord.wz) - Vim 风格的键符号、模态键表和提示栏。
- [sei40kr/wez-pain-control](https://github.com/sei40kr/wez-pain-control?tab=readme-ov-file) - 窗格控制键绑定，例如 tmux-pain-control。
- [sei40kr/wez-tmux](https://github.com/sei40kr/wez-tmux) - 移植的 tmux 键绑定。
- [selectnull/pinned-tabs.wezterm](https://github.com/selectnull/pinned-tabs.wezterm) - 允许您将键绑定分配给特定选项卡。
- [abidibo/wezterm-cmdpicker](https://github.com/abidibo/wezterm-cmdpicker) - 为键绑定添加命令调色板样式的模糊选择器。按触发键即可搜索并执行任何键绑定 — 用户定义的、配置的或 WezTerm 默认值。
- [annie444/sync-panes.wez](https://github.com/annie444/sync-panes.wez) - 将您的击键镜像到活动选项卡中的每个窗格 - 相当于 tmux 的“同步窗格”。

## 媒体

- [xarvex/presentation.wez](https://github.com/xarvex/presentation.wez) - 相当简单的演示模式切换。

## 尼奥维姆

- [mrjones2014/smart-splits.nvim](https://github.com/mrjones2014/smart-splits.nvim) - 提供用于 Neovim 和 WezTerm MUX 之间无缝窗格导航的插件。
- [winter-again/wezterm-config.nvim](https://github.com/winter-again/wezterm-config.nvim) - 直接从 Neovim 与 WezTerm 配置交互。

## 窗格

- [ChrisGVE/pivot_panes.wezterm](https://github.com/ChrisGVE/pivot_panes.wezterm) - 在水平和垂直分割之间切换窗格方向。
- [bad-noodles/stack.wez](https://github.com/bad-noodles/stack.wez) - 堆叠窗格模式，可使用多个窗格，但一次只能看到一个窗格。

## 会议

- [DavidRR-F/quick_domains.wezterm](https://github.com/DavidRR-F/quick_domains.wezterm) - 更快地搜索和附加到 (SSH) 域的方法。
- [isseii10/workspace-picker.wezterm](https://github.com/isseii10/workspace-picker.wezterm) - 与“zoxa”集成的工作区切换器。
- [JuanraCM/wsinit.wezterm](https://github.com/JuanraCM/wsinit.wezterm) - 管理和初始化工作区配置的简单而灵活的方法。
- [mikkasendke/sessionizer.wezterm](https://github.com/mikkasendke/sessionizer.wezterm) - 使用“fd”打开 Git 存储库作为自己的 WezTerm 工作区。
- [MLFlexer/resurrect.wezterm](https://github.com/MLFlexer/resurrect.wezterm) - 保存和恢复窗口、选项卡和窗格的状态。
- [MLFlexer/smart_workspace_switcher.wezterm](https://github.com/MLFlexer/smart_workspace_switcher.wezterm) - 在模糊查找和“zoxa”的工作空间之间切换。
- [vieitesss/workspacesionizer.wezterm](https://github.com/vieitesss/workspacesionizer.wezterm) - 受“tmux-sessionizer”启发的极快工作区选择器。
- [abidibo/wezterm-sessions](https://github.com/abidibo/wezterm-sessions) - 保存和恢复会话。
- [srackham/tabsets.wezterm](https://github.com/srackham/tabsets.wezterm) - 加载、保存、重命名和删除命名选项卡集。
- [ryanmsnyder/workspace-manager.wezterm](https://github.com/ryanmsnyder/workspace-manager.wezterm) - 通过智能工作区切换和键盘驱动的导航轻松导航项目。

## 标签栏

- [adriankarlen/bar.wezterm](https://github.com/adriankarlen/bar.wezterm) - 包含电池的可配置标签栏。
- [michaelbrusegard/tabline.wez](https://github.com/michaelbrusegard/tabline.wez) - 具有“lualine.nvim”配置格式的多功能且易于使用的复古标签栏。
- [rootiest/battery.wez](https://github.com/rootiest/battery.wez) - 用于复古标签栏的彩色且精美的电池组件。
- [yriveiro/wezterm-status](https://github.com/yriveiro/wezterm-status) - 复古标签栏的可配置状态。
- [yriveiro/wezterm-tabs](https://github.com/yriveiro/wezterm-tabs) - 复古标签栏的可配置标签。
- [pro-vi/wezterm-attention](https://github.com/pro-vi/wezterm-attention) - 将您的标签栏变成带有彩色标签指示器的通知系统。

## 主题

- [neapsix/wezterm](https://github.com/neapsix/wezterm) - 玫瑰松木主题，全天然松木、人造毛皮和一点 soho 氛围。
- [sravioli/kanagawa.wz](https://github.com/sravioli/kanagawa.wz) - Kanakawa.nvim 配色方案，包含 Wave、Dragon 和 Lotus 变体。
- [koh-sh/wezterm-theme-rotator](https://github.com/koh-sh/wezterm-theme-rotator) - 使用键盘快捷键循环浏览内置主题。
- [willytop8/Wezterm-Window-Tint](https://github.com/willytop8/Wezterm-Window-Tint) - 根据活动窗格的 Git 根为窗口框架、选项卡栏和状态徽章着色。

## 实用性

- [aureolebigben/wezterm-cmd-sender](https://github.com/aureolebigben/wezterm-cmd-sender) - 将命令发送到多个窗格。
- [ChrisGVE/dev.wezterm](https://github.com/ChrisGVE/dev.wezterm) - 用于开发和部署插件的位置解析器。
- [ChrisGVE/lib.wezterm](https://github.com/ChrisGVE/lib.wezterm) - 插件开发人员的常用实用函数库。
- [ChrisGVE/listeners.wezterm](https://github.com/ChrisGVE/listeners.wezterm) - 通过持久状态管理启用增强的事件侦听器功能。
- [dfsramos/wezterm-sync](https://github.com/dfsramos/wezterm-sync) - 通过私有 GitHub Gist 在计算机之间同步您的配置，外部依赖性为零。
- [lilaqua/tunicodes](https://gitlab.com/lilaqua/tunicodes) - 通过代码点插入 Unicode 字符。
- [zsh-sage/toggle_terminal.wez](https://github.com/zsh-sage/toggle_terminal.wez) - 易于使用的可切换终端窗口。
- [quantonganh/quickselect.wezterm](https://github.com/quantonganh/quickselect.wezterm) - 通过在 Helix 中打开它们来跳转到构建错误。
- [sravioli/lantern.wz](https://github.com/sravioli/lantern.wz) - 用于颜色方案、字体、GPU 适配器、窗口外观和自定义配置预设的选择器框架。
- [sravioli/log.wz](https://github.com/sravioli/log.wz) - 带有可插入接收器和严重性阈值的标记日志库。
- [sravioli/memo.wz](https://github.com/sravioli/memo.wz) - 记忆、缓存和持久状态管理。
- [sravioli/ribbon.wz](https://github.com/sravioli/ribbon.wz) - 为状态栏、选项卡标题和选择器预览构建样式文本段。
- [sravioli/sigil.wz](https://github.com/sravioli/sigil.wz) - 流程、工具和 UI 标签的图标和标识颜色注册表。
- [sravioli/warp.wz](https://github.com/sravioli/warp.wz) - 具有字符串、表、列表、路径和文件系统帮助程序的通用实用程序库。
- [btrachey/wezterm-replay](https://github.com/btrachey/wezterm-replay) - 解析命令输出并获取 URL、shell 命令等，并将其粘贴到下一个提示符中。
- [usrivastava92/widgets.wez](https://github.com/usrivastava92/widgets.wez) - 适用于 macOS、Linux 和 Windows 上的 CPU、RAM、电池、网络和磁盘的跨平台状态栏小部件。
