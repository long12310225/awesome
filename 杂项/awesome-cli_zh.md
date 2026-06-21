# 很棒的 CLI

Awesome CLI 是一个简单的命令行工具，为您提供了一个精美的命令行界面来深入了解 [Awesome](https://github.com/sindresorhus/awesome) 列表。

![很棒的 CLI](./assets/images/awesome-cli-banner.png)

![Build](https://github.com/umutphp/awesome-cli/workflows/Test%20&%20Build/badge.svg) ![WOSPM Checker](https://github.com/umutphp/awesome-cli/workflows/WOSPM%20Checker/badge.svg)

---
<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->


- [Introduction](#introduction)
- [如何使用](#how-to-use)
  - [互动模式](#interactive-mode)
  - [随机模式](#random-mode)
  - [惊喜模式](#surprise-mode)
- [如何安装](#how-to-install)
  - [Basic](#basic)
  - [构建为二进制文件](#build-as-binary)
  - [下载并使用官方二进制文件](#download-and-use-official-binary)
  - [CLI 选项](#cli-options)
  - [示例执行](#sample-execution)
- [如何贡献](#how-to-contribute)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->
---

## 简介

CLI 从根存储库 [sindresorhus/awesome](https://github.com/sindresorhus/awesome) 开始，并根据您的选择引导到最终存储库。它获取存储库的自述文件并解析它们以创建选择列表。因此，CLI 需要一个工作网络:)。它还使用文件缓存来缓存自述文件内容。您可以在主文件夹下找到名为“.awesomecache”的缓存文件夹。

![Avesome-cli 示例](./assets/images/awesome-cli.gif)

## 如何使用

### 互动模式

为了交互地使用awesome-cli，只需执行它而不给出任何选项。您将使用“↓ ↑ → ←”按钮浏览类别和存储库。您的选择将被保存以在[惊喜模式](#surprise-mode)中使用。

```bash
> $ awesome-cli
Use the arrow keys to navigate: ↓ ↑ → ← 
? Select from 'Awesome' list: 
  ▸ Platforms
    Programming Languages
    Front-End Development
    Back-End Development
    Computer Science
    Big Data
    Theory
    Books
    Editors
↓   Gaming
```

### 随机模式

您可以使用“随机”选项进入随机类别下的随机真棒存储库。

```bash
> $ awesome-cli random
awesome-cli Version 0.3.0
✔ Programming Languages
✔ Eta
✔ Community
✔ IRC
https://kiwiirc.com/client/irc.freenode.net/#eta-lang
```

### 惊喜模式

当您使用“惊喜”选项时，awesome-cli 将使用您之前在[交互模式](#interactive-mode) 中的选择来为您查找随机存储库。

```bash
> $ awesome-cli surprise
awesome-cli Version 0.3.0
✔ Back-End Development
✔ Docker
✔ Videos
✔ From Local Docker Development to Production Deployments
https://www.youtube.com/watch?v=7CZFpHUPqXw
```

## 如何安装

### 基础

按照步骤操作；

```bash
> $ git clone git@github.com:umutphp/awesome-cli.git
> $ cd awesome-cli
> $ go run main.go
```

### 构建为二进制文件

按照步骤操作；

```bash
> $ git clone git@github.com:umutphp/awesome-cli.git
> $ cd awesome-cli
> $ sudo go build -o /usr/local/bin/awesome-cli .
> $ awesome-cli
```

### 下载并使用官方二进制文件

访问【最新版本】(https://github.com/umutphp/awesome-cli/releases/latest)页面，下载对应的zip并解压。您可以使用 zip 文件中的二进制文件。

```bash
> $ cp /path/to/zip/extract/awesome-cli /usr/local/bin/awesome-cli
> $ awesome-cli
```

### CLI 选项

CLI 在交互模式下工作，没有任何给定的选项。但是，它也可以称为下面描述的一些选项；

```bash
> $ awesome-cli help
awesome-cli Version 0.6.0

Options of awesome-cli:
  help      To print this screen.
  random    To go to a random awesome content.
  surprise  To go to a surprise awesome content according to your previos choices.
  profile   To see your previous choices.
  reset     To clean your choices to start from the beginning.
  update    Update awesome-cli to the latest version.
```

### 示例执行

```bash
> $ awesome-cli random
awesome-cli Version 0.2.0
✔ Platforms
✔ Linux
✔ Applications
✔ Gedit
https://wiki.gnome.org/Apps/Gedit
```

## 如何贡献
请遵循 [CONTRIBUTING](CONTRIBUTING.md) 文件中的说明并注意 [CODE_OF_CONDUCT](CODE_OF_CONDUCT)。
