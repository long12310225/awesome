# 很棒的尼克斯 [![Awesome](https://awesome.re/badge.svg)](https://github.com/sindresorhus/awesome)

<a href="https://nixos.org">
  <picture>
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/NixOS/nixos-artwork/master/logo/nixos.svg">
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/NixOS/nixos-artwork/master/logo/nixos-white.png">
    <img src="https://raw.githubusercontent.com/NixOS/nixos-artwork/master/logo/nixos.svg" align="right" width="250" alt="NixOS logo">
  </picture>
</a>

Nix 社区中最佳资源的精选列表。

<br>

[Nix](https://github.com/nixos/nix) 是一款适用于 Linux 和其他 Unix 系统的强大包管理器，使包管理变得可靠且可重复。

*贡献前请阅读[贡献指南](CONTRIBUTING.md)。*

## 内容

* [Resources](#resources)
    * [Learning](#learning)
    * [Discovery](#discovery)
* [安装介质](#installation-media)
* [频道历史](#channel-history)
* [部署工具](#deployment-tools)
* [Virtualisation](#virtualisation)
* [命令行工具](#command-line-tools)
* [Development](#development)
* [DevOps](#devops)
* [编程语言](#programming-languages)
    * [Arduino](#arduino)
    * [Clojure](#clojure)
    * [Crystal](#crystal)
    * [Elm](#elm)
    * [Gleam](#gleam)
    * [Haskell](#haskell)
    * [Haxe](#haxe)
    * [Julia](#julia)
    * [Lean](#lean)
    * [Node.js](#nodejs)
    * [OCaml](#ocaml)
    * [PHP](#php)
    * [PureScript](#purescript)
    * [Python](#python)
    * [Ruby](#ruby)
    * [Rust](#rust)
    * [Scala](#scala)
    * [Zig](#zig)
* [NixOS 模块](#nixos-modules)
* [NixOS 配置编辑器](#nixos-configuration-editors)
* [Overlays](#overlays)
* [Distributions](#distributions)
* [Community](#community)

## 资源

### 学习

* [Building a Rust service with Nix](https://fasterthanli.me/series/building-a-rust-service-with-nix) - 关于使用 Nix 创建 Rust 应用程序的深入博客系列。
* [Explainix](https://zaynetro.com/explainix) - 直观地解释 Nix 语法。
* [How to Learn Nix](https://ianthehenry.com/posts/how-to-learn-nix/) - 它就像 Let's Play，但用于晦涩的软件文档。
* [Nix - A One Pager](https://code.tvl.fyi/about/nix/nix-1p) - Nix 语言的一页介绍。
* [nix-book](https://saylesss88.github.io) - NixOS 综合指南
强化和配置。
* [Nix from First Principles: Flake Edition](https://tonyfinn.com/blog/nix-from-first-principles-flake-edition/) - 使用 Nix 功能、Flakes 以及使用 Nix 进行开发的现代速成课程。
* [Nix in 100 Seconds](https://www.youtube.com/watch?v=FJVFXsNzYZQ) - Fireship 的 YouTube 视频在 100 秒内介绍了 Nix。
* [Nix Notes](https://github.com/noteed/nix-notes) - 关于 Nix 的简短注释的集合，每个注释都贡献于相同的虚拟机映像。
* [Nix Pills](https://nixos.org/guides/nix-pills/) - 最好的学习方法是通过示例。
* [Nix Shorts](https://github.com/alper/nix-shorts) - 关于如何使用 Nix 的简短说明集合，针对 Nix Flakes 进行了更新。
* [Nix Starter Config](https://github.com/Misterio77/nix-starter-configs) - 一些简单的 Nix Flake 模板，用于 NixOS + 家庭管理器的入门。
* [nix.dev](https://nix.dev/) - 为开发人员提供的关于使用 Nix 生态系统完成工作的固执己见的指南。
* [NixOS & Flakes Book](https://github.com/ryan4yin/nixos-and-flakes-book) - 一本针对初学者的非官方且固执己见的 NixOS & Flakes 书籍。
* [NixOS Asia Tutorial Series](https://nixos.asia/en/tutorial) - 关于使用 Nix Flakes、NixOS、家庭管理器等的一系列高级教程。
* [NixOS in Production](https://leanpub.com/nixos-in-production) - pdf 格式的免费（按需付费）书籍。
* [Official Nix manual](https://nix.dev/manual/nix/stable/) - Nix 官方手册的最新稳定版本，最好用作参考指南。接收可用更新。
* [Official NixOS manual](https://nixos.org/manual/nixos/stable/) - NixOS 官方手册的最新稳定版本，教程和参考指南的组合。接收可用更新。
* [Official Nixpkgs manual](https://nixos.org/manual/nixpkgs/stable/) - Nixpkgs 官方参考手册的最新稳定版本。接收可用更新。
* [Tour of Nix](https://nixcloud.io/tour/) - 关于 Nix 语言结构的在线交互式教程。
* [Wombat's Book of Nix](https://mhwombat.codeberg.page/nix-book/) - 关于 Nix 和 flake 的全书介绍。
* [Zero to Nix](https://zero-to-nix.com/) - 由确定系统创建的以薄片为中心的 Nix 及其概念指南，可帮助初学者快速入门。

### 发现

* [Home Manager Option Search](https://home-manager-options.extranix.com/) - 搜索所有 2000 多个 Home Manager 选项并了解如何使用它们。
<!-- * [Hound](https://search.nix.gsc.io) - Handily search across all or selected Nix-related repositories. -->
* [Nix Package Versions](https://lazamar.co.uk/nix-versions/) - 查找频道中可用的软件包的所有版本以及您可以从中下载该软件包的修订版。
* [nix-search-tv](https://github.com/3timeslazy/nix-search-tv) - CLI 模糊查找器，用于查找 Nixpkgs、Home Manager 等的软件包和选项。
* [Noogle](https://noogle.dev/) - Nix API 搜索引擎允许根据函数的类型和其他属性来搜索函数。
* [NüschtOS Search](https://github.com/NuschtOS/search) - 简单快速的静态页面 NixOS 选项搜索。
* [Searchix](https://searchix.ovh/) - 从 NixOS、Darwin 和 Home Manager 中搜索 Nix 软件包和选项。

## 安装介质

* [nix-installer-scripts](https://github.com/dnkmmr69420/nix-installer-scripts) - 运行官方安装程序，但也会进行一些调整，例如为 selinux 添加 fcontext 并在默认配置文件之外安装 nix，这样您就不会意外卸载它。
* [nix-installer](https://github.com/DeterminateSystems/nix-installer) - 官方 Nix 安装脚本的固定替代方案。
* [nixos-anywhere](https://github.com/nix-community/nixos-anywhere) - 通过 SSH 在各处安装 NixOS。
* [nixos-generators](https://github.com/nix-community/nixos-generators) - 采用 NixOS 配置并构建多种不同的映像类型，包括 VirtualBox VM、Azure 映像和安装 ISO。
* [nixos-infect](https://github.com/elitak/nixos-infect) - 将正在运行的非 NixOS Linux 主机替换为 NixOS。
* [nixos-up](https://github.com/samuela/nixos-up) - 超级简单的 NixOS 安装程序，可以从安装 ISO 中使用。

## 频道历史

* [`npc`](https://github.com/samestep/npc) - CLI 用于查看和平分 Nixpkgs 通道历史记录。
* [Nix Infra Status](https://status.nixos.org) - 获取每个 Nix 通道的年龄和当前 Git 提交。
* [Nix Review Tools Reports](https://malob.github.io/nix-review-tools-reports/) - 显示主要 Hydra 作业集有问题的依赖项（导致最多失败构建的依赖项）的报告。
<!-- * [Nixpkgs Bot](https://git.maralorn.de/nixos-config/tree/packages/nixpkgs-bot) - A Matrix bot to track when a Nixpkgs pull request reaches a relevant branch. -->
* [nixpkgs PR tracker](https://nixpk.gs/pr-tracker.html) - 用于跟踪 PR 是否已进入频道的跟踪器。

## 部署工具

* [bento](https://github.com/rapenne-s/bento/) - 一个 KISS 部署工具，可让您的 NixOS 队列（服务器和工作站）保持最新状态。
* [Clan](https://clan.lol) - 一种对等部署工具，内置对机密的支持和管理分布式网络的模块系统。
* [Colmena](https://github.com/zhaofengli/colmena) - 一个简单的、无状态的 NixOS 部署工具，以 NixOps 和 morph 为模型。
* [comin](https://github.com/nlewo/comin) - 一种从 Git 存储库持续提取的部署工具。
* [deploy-rs](https://github.com/serokell/deploy-rs) - 一个简单的多配置文件 Nix-flake 部署工具。
* [krops](https://cgit.krebsco.de/krops/about/) - 用于远程或本地部署 NixOS 系统的轻量级工具包。
* [KubeNix](https://github.com/hall/kubenix) - 使用 Nix 的 Kubernetes 资源构建器。
* [KuberNix](https://github.com/saschagrunert/kubernix) - 通过 Nix 包的单依赖 Kubernetes 集群。
* [morph](https://github.com/DBCDK/morph) - 用于管理现有 NixOS 主机的工具。
* [Nixery](https://github.com/tazjin/nixery) - 与 Docker 兼容的容器注册表，可通过 Nix 临时构建镜像。
* [Nixinate](https://github.com/MatthewCroughan/nixinate) - Nix flake 库，提供用于通过 SSH 管理现有 NixOS 主机的应用程序输出。
* [Nixlets](https://gitlab.com/TECHNOFAB/nixlets) - 与 Helm 类似，但仅使用 Nix，在底层使用 Kubenix。
* [NixOps](https://github.com/NixOS/nixops) - Nix 官方部署工具，兼容 AWS、Hetzner 等。
* [pushnix](https://github.com/arnarg/pushnix) - 简单的 cli 实用程序，可推送 NixOS 配置并使用 ssh 触发重建。
* [terraform-nixos](https://github.com/nix-community/terraform-nixos) - 一组旨在部署 NixOS 的 Terraform 模块。
* [terranix](https://terranix.org) - 使用 Nix 和 NixOS 模块系统编写 Terraform 代码。

## 虚拟化

* [extra-container](https://github.com/erikarvstedt/extra-container) - 从命令行运行声明性 NixOS 容器。
* [microvm](https://github.com/microvm-nix/microvm.nix) - 基于 NixOS 的 MicroVM。
* [nixos-shell](https://github.com/Mic92/nixos-shell) - 使用 Nix 进行简单的无头虚拟机配置（类似于 Vagrant）。

## 命令行工具

* [alejandra](https://github.com/kamadorueda/alejandra) - 一个固执己见的 Nix 代码格式化程序，针对速度和一致性进行了优化。
* [angrr](https://github.com/linyinfeng/angrr) - Auto Nix GC 根保留。该工具只是根据符号链接目标的修改时间删除自动 GC 根。
* [comma](https://github.com/nix-community/comma) - 快速运行任何二进制文件；将“nix run”和“nix-index”包装在一起。
* [deadnix](https://github.com/astro/deadnix) - 扫描 Nix 文件中的死代码。
* [devenv](https://github.com/cachix/devenv) - 一个基于 Nix 的工具，用于快速、可重复地创建开发人员 shell 环境。
* [dix](https://github.com/faukah/dix) - 迪夫·尼克斯；一个超快速的工具来区分 Nix 相关的东西。
* [manix](https://github.com/mlvzk/manix) - 查找 Nixpkgs、NixOS 和 Home Manager 的配置选项和功能文档。
* [nh](https://github.com/nix-community/nh) - 利用“dix”和“nix-output-monitor”为“nix”、“nixos-rebuild”、“home-manager”和 nix-darwin CLI 提供更好的输出。
* [nix-alien](https://github.com/thiagokokada/nix-alien) - 在 Nix/NixOS 上轻松运行未修补的二进制文件。
* [nix-diff](https://github.com/Gabriella439/nix-diff) - 解释为什么两个 Nix 推导不同的工具。
* [nix-du](https://github.com/symphorien/nix-du) - 可视化要删除哪些 gc-roots 以释放 Nix 存储中的一些空间。
* [nix-index](https://github.com/nix-community/nix-index) - 快速找到包含特定文件的 Nix 软件包。
* [nix-init](https://github.com/nix-community/nix-init) - 通过哈希预取、依赖推断、许可证检测等功能从 URL 生成 Nix 包。
* [nix-melt](https://github.com/nix-community/nix-melt) - 类似 Ranger 的 flake.lock 查看器。
* [nix-output-monitor](https://github.com/maralorn/nix-output-monitor) - 在构建推导时生成有用的图表和统计数据的工具。
* [nix-prefetch](https://github.com/msteen/nix-prefetch) - 用于更新源校验和的通用工具。
* [nix-tree](https://github.com/utdemir/nix-tree) - 交互式浏览 Nix 派生的依赖关系图。
* [nixfmt](https://github.com/NixOS/nixfmt) - Nix 代码的格式化程序，旨在轻松应用统一的样式。
* [nixos-cli](https://github.com/nix-community/nixos-cli) - 适用于常见 NixOS 工具的可配置一体化 CLI，重点是改善用户体验。
* [nixpkgs-hammering](https://github.com/jtojnar/nixpkgs-hammering) - Nixpkgs 包表达式的固执己见的 linter。
* [nurl](https://github.com/nix-community/nurl) - 从存储库 URL 生成 Nix fetcher 调用。
* [nvd](https://git.sr.ht/~khumba/nvd) - 两个存储路径之间的软件包版本差异；它对于比较重建时的 NixOS 各代特别有用。
* [optnix](https://git.sr.ht/~watersucks/optnix) - Nix 模块系统的基于终端的选项搜索器。
* [statix](https://github.com/oppiliappan/statix) - 用于检查和修复 Nix 代码中的反模式的 linter/fixer。

## 发展

* [Arion](https://github.com/hercules-ci/arion) - 在 Nix/NixOS 的帮助下运行“docker-compose”。
* [attic](https://github.com/zhaofengli/attic) - 多租户 Nix 二进制缓存。
* [cached-nix-shell](https://github.com/xzfc/cached-nix-shell) - “nix-shell”替代品，使用缓存快速打开后续 shell。
* [Cachix](https://www.cachix.org) - 托管二进制缓存服务；对于开源项目免费。
* [compose2nix](https://github.com/aksiksi/compose2nix) - 从 Docker Compose 项目生成 NixOS 配置。
* [Conflake](https://ratson.github.io/conflake/) - 包括电池、自动加载文件、基于约定的“flake.nix”配置框架。
* [Devbox](https://github.com/jetify-com/devbox) - 即时、可移植且可预测的开发环境。
* [devshell](https://github.com/numtide/devshell) - `mkShell` 具有额外的位和 toml 配置选项，以便能够加入非 nix 用户。
* [dream2nix](https://github.com/nix-community/dream2nix) - 一个用于自动将包从其他构建系统转换到 Nix 的框架。
* [flake-utils-plus](https://github.com/gytis-ivaskevicius/flake-utils-plus) - 轻量级 Nix 库 flake，用于轻松进行 NixOS flake 配置。
* [flake-utils](https://github.com/numtide/flake-utils) - Pure Nix flake 实用函数可帮助编写 flake。
* [flake.parts](https://github.com/hercules-ci/flake-parts) - Flakes 的最小 Nix 模块框架：将您的 Flakes 拆分为模块并使用社区模块完成工作。
* [flakelight](https://github.com/nix-community/flakelight) - 旨在最大程度减少样板代码的模块化片状框架。
* [flox](https://github.com/flox/flox) - 管理和共享开发环境、打包项目以及在任何地方发布工件。
* [gitignore.nix](https://github.com/hercules-ci/gitignore.nix) - 功能最齐全且易于使用的“.gitignore”集成。
* [haumea](https://github.com/nix-community/haumea) - Nix 语言基于文件系统的模块系统与传统编程语言类似，支持文件层次结构和可见性。
* [lorri](https://github.com/nix-community/lorri/) - 一个更好的“nix-shell”，用于增强 direnv 的开发。
* [make-shell](https://github.com/nicknovitski/make-shell) - `mkShell` 满足模块的需求，是 `pkgs.mkShell` 功能的模块化几乎直接替代品。
* [MCP-NixOS](https://github.com/utensils/mcp-nixos) - 一个 MCP 服务器，为 AI 助手提供有关 NixOS 软件包、选项、Home Manager 和 nix-darwin 配置的准确信息。
* [namaka](https://github.com/nix-community/namaka) - 基于 haumea 的 Nix 快照测试。
* [nil](https://github.com/oxalica/nil) - NIx 语言服务器，用于在 Nix 中编写的增量分析助手。
* [niv](https://github.com/nmattia/niv/) - 通过包固定轻松管理 Nix 项目的依赖关系。
* [nix2container](https://github.com/nlewo/nix2container) - 使用 Nix 构建高效的容器构建工作流程。
* [nix-direnv](https://github.com/nix-community/nix-direnv) - direnv 环境自动加载器的快速加载器和 flake 兼容配置。
* [nix-health](https://github.com/juspay/nix-health) - 一个检查 Nix 安装运行状况的程序。此外，各个项目可以在其“flake.nix”中配置自己的健康检查。
* [nix-oci](https://github.com/Dauliac/nix-oci) - 一个薄片部件模块，用于使用 nix2container 构建最小的、可重复的 OCI 容器。
* [nix-update](https://github.com/Mic92/nix-update) - 更新 nix 软件包的版本/源哈希。
* [nixd](https://github.com/nix-community/nixd) - Nix 语言服务器，基于 Nix 库。
* [nixpkgs-review](https://github.com/Mic92/nixpkgs-review) - 验证 Nixpkgs 中的拉取请求是否正确构建的最佳工具。
* [Nixtest](https://gitlab.com/TECHNOFAB/nixtest) - Nix 的测试框架，具有快照和单元测试支持、JUnit 生成等。
* [npins](https://github.com/andir/npins) - 一个简单的工具，用于处理 Nix 项目中不同类型的依赖关系。它的灵感来自于 Niv，并且与 Niv 相当。
* [pog](https://github.com/jpetrucciani/pog) - 一种执行 bash 脚本的新的、强​​大的方法。 Pog 是一个功能强大的 Nix 库，它改变了开发人员创建命令行界面 (CLI) 的方式。
* [pre-commit-hooks.nix](https://github.com/cachix/git-hooks.nix) - 在提交时和 CI 上运行 linter/formatters。
* [rnix-lsp](https://github.com/nix-community/rnix-lsp) - Nix 的语法检查语言服务器。
* [robotnix](https://github.com/nix-community/robotnix) - 适用于 Android (AOSP) 映像的声明性且可重现的构建系统。
* [services-flake](https://github.com/juspay/services-flake) - 用于 Nix flakes 的类似 NixOS 的服务配置框架。
* [Snowfall Lib](https://github.com/snowfallorg/lib) - 一个库，通过强加固执己见的文件结构，可以轻松管理您的 Nix flake。
* [templates](https://github.com/nix-community/templates) - 使用 Nix flakes 的多种语言的项目模板。
* [treefmt-nix](https://github.com/numtide/treefmt-nix) - 一个格式化程序，允许使用单个命令格式化所有项目文件，所有这些都通过单个“.nix”文件进行。

## 开发运营

* [Nix GitLab CI](https://gitlab.com/TECHNOFAB/nix-gitlab-ci) - 在纯 Nix 中定义 GitLab CI 管道，并具有对所有 Nix 包（包括缓存）的完全访问权限。
* [nixidy](https://github.com/arnarg/nixidy) - 带有 Nix 和 Argo CD 的 Kubernetes GitOps。
* [Standard](https://github.com/divnix/std) - 一个固执己见的 Nix Flakes 框架，可让大型项目中的 Nix 代码井井有条，并配有针对 DevOps 场景优化的友好 CLI/TUI。

## 编程语言

### Arduino

* [nixduino](https://github.com/boredom101/nixduino) - 基于 Nix 的工具可帮助构建 Arduino 草图。

### 克洛尤尔

* [clj-nix](https://github.com/jlesquembre/clj-nix) - Clojure 项目的 Nix 辅助函数。

### 水晶

* [crystal2nix](https://github.com/nix-community/crystal2nix) - 将 `shard.lock` 转换为 Nix 表达式。

### 榆树

* [elm2nix](https://github.com/cachix/elm2nix) - 将 `elm.json` 转换为 Nix 表达式。

### 微光

* [nix-gleam](https://github.com/arnarg/nix-gleam) - 适用于 Gleam 应用程序的通用 Nix 构建器。

### 哈斯克尔

* [cabal2nix](https://github.com/NixOS/cabal2nix) - 将 Cabal 文件转换为 Nix 构建表达式。
* [haskell-flake](https://github.com/srid/haskell-flake) - 用于 Haskell 开发的“flake-parts”Nix 模块。
* [haskell.nix](https://github.com/input-output-hk/haskell.nix) - Nixpkgs 的替代 Haskell 基础设施。
* [nix-haskell-mode](https://github.com/matthewbauer/nix-haskell-mode) - Emacs 中的自动 Haskell 设置。
* [nixkell](https://github.com/pwm/nixkell) - 使用 Nix 和 direnv 的 Haskell 项目模板。

### 哈克西
* [haxix](https://github.com/MadMcCrow/haxix) - Nix flake 构建 haxe/Heaps.io 项目。
* [kebab](https://github.com/bwkam/kebab) - Nix 的 Haxe 软件包。

### 朱莉娅

* [Manifest2Nix.jl](https://codeberg.org/aniva/Manifest2Nix.jl) - 一个 Nix 库，用于通过预编译创建可重现的 Julia 构建和实验。

### 精益

* [lean4-nix](https://github.com/lenianiva/lean4-nix) - Nix flake 为 Lean 4 和 `lake2nix` 构建。

### Node.js

* [Napalm](https://github.com/nix-community/napalm) - 支持使用轻量级 npm 注册表在 Nix 中构建 npm 包。
* [node2nix](https://github.com/svanderburg/node2nix) - 从 `package.json` （或 `package-lock.json`）生成 Nix 表达式（以文件形式存储）。
* [npmlock2nix](https://github.com/nix-community/npmlock2nix) - 从 `package-lock.json` （内存中）生成 Nix 表达式，主要用于 Web 项目。

### 奥卡米尔

* [opam2nix](https://github.com/timbertson/opam2nix) - 从 opam 包生成 Nix 表达式。

### PHP

* [composer-plugin-nixify](https://github.com/stephank/composer-plugin-nixify) - Composer 插件可帮助 Nix 打包。
* [composer2nix](https://github.com/svanderburg/composer2nix) - 生成 Nix 表达式来构建 Composer 包。
* [composition-c4](https://github.com/fossar/composition-c4) - 支持从“composer.lock”构建 Composer 包（使用 IFD）。
* [nix-phps](https://github.com/fossar/nix-phps) - Flake 包含旧的和未维护的 PHP 版本（用于 CI 使用）。
* [nix-shell](https://github.com/loophp/nix-shell/) - 用于 PHP 开发的 Nix shell。

### 纯脚本

* [Easy PureScript Nix](https://github.com/justinwoo/easy-purescript-nix) - 一个通过 Nix 轻松使用 PureScript 和其他工具的项目。
* [purs-nix](https://github.com/purs-nix/purs-nix) - CLI 和库组合设计用于使用 Nix 管理 PureScript 项目。它提供了可在您的项目中使用的 Nix API，以及用于管理开发过程的命令行界面。

### 蟒蛇

* [poetry2nix](https://github.com/nix-community/poetry2nix) - 直接从 [Poetry's](https://python-poetry.org/) `poetry.lock` 构建 Python 包。无需转换步骤。
* [uv2nix](https://github.com/pyproject-nix/uv2nix) - 将 [`uv` 工作空间](https://docs.astral.sh/uv/concepts/projects/workspaces/) 转换为纯 Nix 派生。

### 红宝石

* [Bundix](https://github.com/nix-community/bundix) - 为 Bundler 管理的应用程序生成 Nix 表达式。
* [ruby-nix](https://github.com/inscapist/ruby-nix) - 使用 Nix 生成可重现的 ruby​​/bundler 应用程序环境。

### 铁锈

* [cargo2nix](https://github.com/cargo2nix/cargo2nix) - 粒度缓存、开发 shell、Nix 和 Rust 集成。
* [crane](https://github.com/ipetkov/crane) - 一个 Nix 库，用于构建具有增量工件缓存的 Cargo 项目。
* [fenix](https://github.com/nix-community/fenix) - 适用于 nix 的 Rust 工具链和 Rust 分析器每晚。
* [naersk](https://github.com/nix-community/naersk) - 直接从“Cargo.lock”构建 Rust 包。无需转换步骤。
* [nix-cargo-integration](https://github.com/90-008/nix-cargo-integration) - 一个可以轻松轻松地集成 Cargo 项目的库。
* [nixpkgs-mozilla](https://github.com/mozilla/nixpkgs-mozilla) - Mozilla 与 Rust 工具链和 Firefox 的叠加。
* [rust-nix-templater](https://github.com/90-008/rust-nix-templater) - 为 Rust 项目生成 Nix 构建和开发文件。
* [rust-overlay](https://github.com/oxalica/rust-overlay) - 二进制分布式 Rust 工具链的纯且可重现的 nix 覆盖。

### 斯卡拉

* [sbt-derivation](https://github.com/zaninime/sbt-derivation) - sbt 的 mkDerivation，类似于 buildGoModule。

### 之字形

* [zig2nix](https://github.com/Cloudef/zig2nix) - 用于打包、构建和运行 Zig 项目的 Flake。
* [zon2nix](https://github.com/nix-community/zon2nix) - 将“build.zig.zon”中的依赖项转换为 Nix 表达式。

## NixOS 模块

* [base16.nix](https://github.com/SenchoPens/base16.nix) - [base16](https://github.com/chriskempson/base16) 颜色方案中的主题程序的 Flake 方式，包括胡子模板支持。
* [Home Manager](https://github.com/nix-community/home-manager) - 像 NixOS 一样管理您的用户配置。
* [impermanence](https://github.com/nix-community/impermanence) - 允许您选择要在重新启动之间保留哪些文件和目录。
* [musnix](https://github.com/musnix/musnix) - 在 NixOS 中进行实时音频工作。
* [nix-bitcoin](https://github.com/fort-nix/nix-bitcoin) - 用于比特币节点的模块和包，具有更高层协议，强调安全性。
* [nix-darwin](https://github.com/nix-darwin/nix-darwin) - 就像在 NixOS 上一样管理 macOS 配置。
* [nix-mineral](https://github.com/cynicsketch/nix-mineral) - 方便合理地强化NixOS。
* [nix-topology](https://github.com/oddlama/nix-topology) - 直接从 NixOS 配置生成基础架构和网络图。
* [NixOS hardware](https://github.com/NixOS/nixos-hardware) - NixOS 配置文件可优化不同硬件的设置。
* [NixOS-WSL](https://github.com/nix-community/NixOS-WSL) - 用于在 Linux 的 Windows 子系统上运行 NixOS 的模块。
* [NixVim](https://github.com/nix-community/nixvim) - 使用 Nix 模块和 Nixpkg 构建的 Neovim 发行版。
* [Self Host Blocks](https://github.com/ibizaman/selfhostblocks) - 基于 NixOS 模块并专注于最佳实践的模块化服务器管理。
* [Simple Nixos Mailserver](https://gitlab.com/simple-nixos-mailserver/nixos-mailserver) - 一个完整的邮件服务器，使用 NixOS 模块进行管理。
* [Stylix](https://github.com/nix-community/stylix) - NixOS 的系统范围配色和排版。

## NixOS 配置编辑器

### 桌面应用程序

* [Nix Software Center](https://github.com/snowfallorg/nix-software-center) - 安装和管理 Nix 软件包。 Rust 和 GTK 中的桌面应用程序。
* [NixOS Configuration Editor](https://github.com/snowfallorg/nixos-conf-editor) - NixOS 配置的图形编辑器。 Rust 和 GTK 中的桌面应用程序。

### 网页界面

* [MyNixOS](https://mynixos.com/) - Nix flake 的图形编辑器。创建和管理 NixOS 和 Nix home-manager 的配置和模块。与其说是 Nix 编辑器，不如说是 Nix 生成器，因为它不允许导入 Nix 文件。

## 叠加层

* [awesome-nix-hpc](https://github.com/freuk/awesome-nix-hpc) - 高性能计算包集。
* [neovim-nightly-overlay](https://github.com/nix-community/neovim-nightly-overlay) - 每日更新 Neovim 夜间套餐。
* [nixpkgs-firefox-darwin](https://github.com/bandithedoge/nixpkgs-firefox-darwin) - 自动更新适用于 macOS 的 Firefox 二进制包。
* [nixpkgs-wayland](https://github.com/nix-community/nixpkgs-wayland) - 尖端的 Wayland 软件包。
* [NUR](https://github.com/nix-community/NUR/) - Nix 用户存储库。所有覆盖层之母，允许访问用户存储库并通过属性安装包。
* [System Manager](https://github.com/numtide/system-manager) - 一个基于 Nix 构建的非 NixOS Linux 系统配置工具。
* [zig-overlay](https://github.com/mitchellh/zig-overlay) - 封装 Zig 编译器的 Nix flake。该 flake 镜像了 Zig 官方构建的二进制文件，而不是从源代码构建它们。

## 发行版

* [nixbsd](https://github.com/nixos-bsd/nixbsd) - 带有 FreeBSD 内核的 NixOS 分支。
* [NixNG](https://github.com/nix-community/NixNG) - 与 NixOS 类似的 GNU/Linux 发行版，最大的区别在于对容器和轻量级的关注。
* [SnowflakeOS](https://snowflakeos.org/) - 基于 NixOS 的 Linux 发行版，注重初学者友好性和易用性。

## 社区

* [#nix:nixos.org](https://matrix.to/#/#nix:nixos.org)
* [Libera.Chat 上的#nixos](https://web.libera.chat/?nick=Guest?#nixos)
* [Discord - Nix/Nixos（非官方）](https://discord.com/invite/BMUCQx6)
* [Discourse](https://discourse.nixos.org/) - 获得帮助和讨论 Nix 相关主题的最佳场所。
* [NixCon](https://nixcon.org/) - Nix 和 NixOS 的贡献者和用户的年度社区会议。
* [维基（官方）](https://wiki.nixos.org/wiki/Main_Page)
* [维基（非官方）](https://nixos.wiki/wiki/Main_Page)
