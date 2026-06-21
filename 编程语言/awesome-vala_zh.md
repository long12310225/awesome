# 很棒的瓦拉 [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[<img src=“vala.svg”align=“right”宽度=“100”>](https://vala.dev)

[Vala](https://vala.dev/) 的精选资源列表 - 一种依靠 GLib 和 GObject 使用现代高级抽象的编程语言，无需施加额外的运行时要求。

## 内容

- [Apps](#apps)
    - [密码学与安全](#cryptography--security)
    - [设计工具](#design-tools)
    - [开发工具](#development-tools)
    - [Games](#games)
    - [互联网浏览器](#internet-browsers)
    - [Music](#music)
    - [Personalization](#personalization)
    - [Productivity](#productivity)
    - [系统工具](#system-tools)
    - [Virtualization](#virtualization)
    - [Weather](#weather)
- [CLI工具](#cli-tools)
- [编辑器插件](#editor-plugins)
- [语言服务器](#language-servers)
- [Libraries](#libraries)
    - [Command-line](#command-line)
    - [Concurrency](#concurrency)
    - [密码学与安全](#cryptography--security-1)
    - [数据结构和数据类型](#data-structures--data-types)
    - [Databases](#databases)
    - [图形库](#graphics-libraries)
    - [图形用户界面编程](#gui-programming)
    - [IoC 和依赖注入](#ioc-and-dependency-injection)
    - [多媒体处理](#multimedia-processing)
    - [数值计算](#numerical-computation)
    - [Templating](#templating)
    - [文本处理](#text-processing)
    - [网页开发](#web-development)
    - [XML 和数据序列化](#xml--data-serialization)

## 应用程序

### 密码学与安全

- [Integrity Check](https://gitlab.com/vinarisoftware/integrity-check-gtk) - 用 Vala 和 GTK 编写的 Linux 应用程序，旨在获取文件的验证和（MD5、SHA1、SHA256）并与文件创建者提供的验证和进行比较。

### 设计工具

- [Akira](https://github.com/akiraux/Akira) - 用于 UI 和 UX 设计的原生 Linux 应用程序，内置于 Vala 和 GTK。
- [Birdfont](https://github.com/johanmattssonm/birdfont) - 用于创建 TTF、EOT、SVG 和 BIRDFONT 格式字体的字体编辑器。

### 开发工具

- [GitG](https://gitlab.gnome.org/GNOME/gitg) - [git](https://git-scm.com/) 的图形用户界面。
- [Kangaroo](https://github.com/dbkangaroo/kangaroo) - 适用于流行数据库的人工智能驱动的 SQL 客户端和管理工具。
- [VAMM (Vinari OS Apache & MariaDB Manager)](https://gitlab.com/XavierEduardo99/vamm-vinari-software) - 使用 GTK 3 GUI 管理 LAMP 服务。

### 游戏

- [GameHub](https://github.com/tkashkin/GameHub) - 适用于所有游戏的统一库。
- [High Score (GNOME Games)](https://gitlab.gnome.org/World/highscore) - GNOME 桌面的复古游戏应用程序。
- [Sage](https://github.com/antolius/sage) - 专为基本操作系统制作的密码破解游戏。
- [Warble](https://github.com/avojak/warble) - 使用 Vala 和 Gtk 为基础操作系统构建的原生 Linux 猜词游戏。

### 互联网浏览器

- [Starfish](https://github.com/starfish-app/Starfish) - 适用于基本操作系统的 Gemini 浏览器。

### 音乐

- [g4music](https://gitlab.gnome.org/neithern/g4music) - 一个用 GTK4 编写的漂亮、快速、流畅、轻量级的音乐播放器。

### 个性化

- [Korembi](https://github.com/cheesecakeufo/komorebi) - 适用于 Linux 的漂亮且可定制的壁纸管理器。

### 生产力

- [Annotator](https://github.com/phase1geo/Annotator) - 对图像进行注释以便更好地沟通。
- [Badger](https://github.com/elfenware/badger) - 提醒自己不要坐着盯着屏幕太久。
- [Blackbox](https://gitlab.gnome.org/raggesilver/blackbox) - 一个漂亮的 GTK 4 终端。
- [Dino](https://github.com/dino/dino) - 使用 GTK+/Vala 的现代 Jabber/XMPP 客户端。
- [Flowtime](https://github.com/Diego-Ivan/Flowtime) - GTK4 Libadwaita 番茄计时器。
- [geary](https://gitlab.gnome.org/GNOME/geary) - Geary 是一款围绕对话构建的电子邮件应用程序，适用于 GNOME 3 桌面。
- [GNOME Calculator](https://gitlab.gnome.org/GNOME/gnome-calculator) - 适用于 GNOME 桌面的计算器应用程序。
- [graphui](https://github.com/artemanufrij/graphui) - 基于graphviz的图可视化。
- [Ideogram](https://github.com/cassidyjames/ideogram) - 表情符号选择器应用程序。
- [Minder](https://github.com/phase1geo/Minder) - 思维导图应用程序。
- [Notejot](https://github.com/lainsce/notejot) - 愚蠢简单的笔记应用程序。
- [Notes-up](https://github.com/Philip-Scott/Notes-up) - Markdown 笔记编辑器和管理器。
- [Outliner](https://github.com/phase1geo/Outliner) - 轻松写出大纲。
- [Paper](https://gitlab.com/posidon_software/paper/) - 用 Markdown 做笔记。
- [pdfpc](https://github.com/pdfpc/pdfpc) - GTK 演示应用程序，支持 PDF 文件的多显示器。
- [Planify](https://github.com/alainm23/planify) - 具有为 GNU/Linux 设计的 Todoist 支持的任务管理器。
- [Spice-up](https://github.com/Philip-Scott/Spice-up) - 适用于现代 Linux 桌面的演示应用程序。
- [TextShine](https://github.com/phase1geo/TextShine) - 转换和操作文本。
- [TextSnatcher](https://github.com/RajSolai/TextSnatcher) - 轻松从图像复制文本。

### 系统工具

- [Connections](https://gitlab.gnome.org/GNOME/connections) - 适用于 GNOME 桌面环境的远程桌面客户端。
- [elementary OS App Center](https://github.com/elementary/appcenter) - 适用于基本操作系统的按需付费应用商店。
- [Man Helper](https://github.com/akarin123/manhelper) - 用于手册页的轻量级 GTK 前端。
- [Monitor](https://github.com/stsdc/monitor) - 管理进程并监控系统资源。
- [Peek](https://github.com/phw/peek) - 简单的动画 GIF 屏幕录像机，具有易于使用的界面。
- [SwayNotifiationCenter](https://github.com/ErikReider/SwayNotificationCenter) - 一个简单的基于 GTK 的 SwayWM 通知守护进程。

### 虚拟化

- [GNOME Boxes](https://gitlab.gnome.org/GNOME/gnome-boxes) - 用于访问虚拟机的简单 GNOME 3 应用程序。

### 天气

- [Meteo](https://gitlab.com/bitseater/meteo) - 使用 OpenWeatherMap API 的 GTK 天气应用程序。

## CLI工具

- [EasyDocs](https://github.com/watsonprojects/EasyDocs) - 快速阅读开发人员文档。
- [Spider](https://github.com/colinkiama/spider) - 快速生成 HTML5 网站结构。
- [Valdo](https://github.com/vala-lang/valdo) - 从模板创建新的 Vala 项目。

## 编辑器插件

- [Vala VSCode](https://github.com/vala-lang/vala-vscode) - Visual Studio Code 的插件，支持 Vala 的基本自动完成和语法突出显示。
- [Vala-TMBundle](https://github.com/technosophos/Vala-TMBundle) - 一个 TextMate 包，提供 Vala 语法高亮、代码补全等功能。Sublime Text 3 也可以使用这个插件。
- [language-vala-modern](https://atom.io/packages/language-vala-modern) - 在 Atom 中提供 Vala 语言支持。它是未维护的“语言-vala 包”的一个分支。
- [Vala Syntax 4 Sublime Text](https://launchpad.net/valasyntax4sublimetext) - Sublime Text 3 的基本插件，提供语法突出显示。

## 语言服务器

- [vala-language-server](https://github.com/vala-lang/vala-language-server) - 一种语言服务器，旨在根据语言服务器规范提供代码完成、格式化、语法突出显示以及其他所有功能。

## 图书馆

### 命令行

- [console-command](https://github.com/naaando/console-command) - 用于将命令行参数路由到命令模式对象的库，当前实现涵盖通过继承或使用闭包进行扩展。

### 并发性

- [gpseq](https://gitlab.com/kosmospredanie/gpseq) - Vala 和 GObject 的并行库。

### 密码学与安全

- [GnuTLS](https://www.gnutls.org/) - 一个安全通信库，实现 SSL、TLS 和 DTLS 协议及其相关技术。它提供了一个简单的 API 来访问安全通信协议以及解析和写入 X.509、PKCS #12 和其他所需结构的 API。

### 数据结构和数据类型

- [Graphene](https://github.com/ebassi/graphene) - 图形库类型的薄层。它提供了处理 3D 变换所需的常见类型：点、三角形、矩形、四边形、四元数、向量、矩阵、球体等。
- [Libgee](https://gitlab.gnome.org/GNOME/libgee) - 一个实用程序库，为常用数据结构（列表、映射、队列、树等）提供基于 GObject 的接口和类。
- [Numeric-GLib](https://github.com/arteymix/numeric-glib) - 通过 GCC 扩展的 GLib（和 Vala）数字数据类型的集合。它包括 128 位整数和浮点数、复杂类型、向量化运算和小数类型。
- [United](https://github.com/lcallarec/united) - 用于单位操作的库（如千克、米等）。
- [vul (Vala Utility Libraries)](https://gitlab.gnome.org/BZHDeveloper/vul) - Vala 的一组实用程序库，添加了：文本流处理（输入和输出）、JSON 序列化和反序列化以及存档压缩和提取。

### 数据库

- [Almanna ORM](https://github.com/AmbitionFramework/almanna) - Vala/GLib 的 Almanna ORM。

### 图形库

- [Babl](http://gegl.org/babl/) - 动态的、任意到任意的像素格式转换库。
- [Cairo](https://cairographics.org/) - 支持多种输出设备的 2D 图形库。这几乎是您在 Vala 中获得的默认库。
- [GEGL](http://gegl.org/) - 基于数据流的图像处理框架，提供浮点处理和无损图像处理能力。将其视为“图像响应式编程”。
- [GRX](https://github.com/ev3dev/grx) - 用于简单图形显示的图形库（想想 1 位显示器或 Adafruit 的 PiTFT 显示器）。它还包括键盘、鼠标、操纵杆和触摸屏输入支持。
- [GSVG (GObject SVG Library)](https://gitlab.com/gsvg/gsvg) - GSVG 致力于提供 W3C 标准 API 的 GLib GObject 实现。
- [live-chart](https://github.com/lcallarec/live-chart) - 基于 Cairo 的 Vala 和 GTK3 实时图表库。
- [SDL2](https://www.libsdl.org/) - 跨平台开发库，旨在通过 OpenGL、Direct3D 和 Vulkan 提供对音频、键盘、鼠标、操纵杆和图形硬件的低级访问。绑定包含在 Vala 中，将从 Vala 0.52 开始提供。

### 图形用户界面编程

- [GTK](https://www.gtk.org/) - Vala 中用于 GUI 开发的事实上的库。绑定包含在 vala 编译器中。

### IoC 和依赖注入

- [Vadi](https://github.com/nahuelwexd/Vadi) - 为了方便 Vala 开发人员使用依赖注入而开发的 IoC 容器。

### 多媒体处理

- [GStreamer](http://gstreamer.freedesktop.org/) - 用于创建多媒体应用程序的强大框架。

### 数值计算

- [balistica](https://github.com/fusilero/libbalistica) - 开源弹道模拟库。 [此处](https://github.com/fusilero/balistica) 有一个完整的计算器。
- [vast](https://github.com/rainwoodman/vast) - Vala 的生成建模项目。想想用 Vala 重写的 TensorFlow。

### 模板化

- [Compose](https://github.com/arteymix/compose) - Vala 的函数模板库。
- [template-glib](https://gitlab.gnome.org/GNOME/template-glib) - 模板扩展库，支持从模板调用 GObject Introspection。

### 文本处理

- [libcmark-vapi](https://github.com/fabrixxm/libcmark-vapi) - Vala 绑定 libcmark，C 语言的 CommonMark 解析和渲染库。

### 网页开发

- [Ambition](https://github.com/AmbitionFramework/ambition) - 用 Vala 编写的 Web 框架，考虑到 MVC 模式。有点无人维护（有人可以重构它以在幕后使用 Valum，也可能将其移至 Meson 😉）。
- [Valum](https://github.com/valum-framework/valum) - 完全用 Vala 编写的 Web 微框架。

### XML 和数据序列化

- [GXML](https://gitlab.gnome.org/GNOME/gxml/) - 用于操作 XML 的 GObject API 和从 GObject 到 XML 的可序列化框架。
- [Json-GLib](https://gitlab.gnome.org/GNOME/json-glib/) - 使用 GLib 和 GObject 实现完整的 JSON 解析器和生成器，并将 JSON 与 GLib 数据类型集成。
- [libyaml-glib](https://github.com/rainwoodman/libyaml-glib) - libyaml 的 GLib 绑定​​，以及理解 YAML 的 GObject 构建器。
