# 很棒的 Scala Native [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
<a href="http://www.scala-native.org/"><img alt="Scala Native" align="right" width="250" height="250" src="logo.png"></a>

[Scala Native](http://www.scala-native.org/) 是针对[Scala 编程语言](https://www.scala-lang.org/) 的优化提前编译器。传统上，运行 Scala 程序需要虚拟机 [JVM](https://en.wikipedia.org/wiki/Java_virtual_machine)。 Scala Native 利用编译器发出[LLVM 中间表示](http://llvm.org/docs/LangRef.html)，而不是 JVM 字节码。然后，[LLVM](http://llvm.org/) 编译器基础结构用于生成本机库和可执行文件。由于 Scala Native 可执行文件是独立的程序，因此它们通常具有较短的启动时间和较低的内存消耗。这开辟了部署 Scala 程序的新途径，而以前虚拟机是限制因素。例如，开发人员可以为命令行或嵌入式设备编写程序。

## 内容
- [很棒的 Scala Native ](#awesome-scala-native-)
  - [Contents](#contents)
  - [教程和示例](#tutorials-and-examples)
  - [构建工具](#build-tools)
  - [函数式编程](#functional-programming)
  - [单元测试](#unit-tests)
  - [Bindings](#bindings)
  - [文件格式和解析器](#file-formats-and-parsers)
  - [Databases](#databases)
  - [网页开发](#web-development)
  - [Concurrency](#concurrency)
  - [Logging](#logging)
  - [Console](#console)
  - [Robotics](#robotics)
  - [Programs](#programs)
  - [Infrastructure](#infrastructure)
  - [Licence](#licence)

## 教程和示例
* [Giter8 template for a minimal Scala Native project](https://github.com/scala-native/scala-native.g8) - 最小 Scala Native 项目的官方 [Giter8](http://www.foundweekends.org/giter8/) 模板。
* [Hands on Scala Native](https://github.com/MasseGuillaume/hands-on-scala-native) - 使用 Ncurses 实现带宽监控器的教程。
* [Starter for Scala Native](https://github.com/GnaneshKunal/scala-native-starter) - 链接到自定义 C 库的 Scala Native 项目。
* [Building C code using sbt-jni](https://github.com/nadavwr/scala-native-sbt-jni-example) - 使用 [sbt-jni](https://github.com/jodersky/sbt-jni) 在 Scala Native 项目中编译 C 代码的示例。
* [Example project with external dependencies](https://github.com/lihaoyi/scala-native-example-app) - 使用外部依赖项生成 HTML 并运行测试套件的示例项目。
* [Starter for Gtk+ Projects](https://github.com/jokade/scalanative-gtk-seed.g8) - 使用 [Gtk+](https://developer.gnome.org/gtk3/stable/index.html) 的 Scala Native GUI 项目的 [Giter8](http://www.foundweekends.org/giter8/) 模板。
* [使用 scala Native 进行现代系统编程](https://pragprog.com/titles/rwscala/modern-systems-programming-with-scala-native/) 书。
* [在 Scala Native 中编写一个简单的 CLI 应用程序](https://github.com/ItoYo16u/prettytable-native)
## 构建工具
* [sbt](https://www.scala-sbt.org/) - Scala 的标准构建工具。
* [Mill](https://github.com/com-lihaoyi/mill) - 受 [Bazel](https://www.bazel.build/) 启发，构建力求简单的工具。
* [Bloop](https://github.com/scalacenter/bloop) - Scala 构建服务器和命令行工具可实现快速的开发人员工作流程。
* [Seed](https://github.com/tindzk/seed) - 基于Bloop的构建工具。受 [Cargo](https://github.com/rust-lang/cargo) 启发，专注于用户体验和跨平台构建。

## 函数式编程
* [Shapeless](https://github.com/milessabin/shapeless) - 通用编程库。
* [Squants](https://github.com/typelevel/squants) - 用于数量、测量单位和尺寸分析的 DSL。
* [scalaz](https://github.com/scalaz/scalaz) - 数据结构的类型类和实例。
* [nobox](https://github.com/xuwei-k/nobox) - 不可变的原始数组包装器，无需装箱。
* [PPrint](https://github.com/lihaoyi/PPrint) - 漂亮的打印值和类型。
* [SourceCode](https://github.com/lihaoyi/sourcecode) - 隐式提供类似于 C 中的“__LINE__”的元数据。
* [reactify](https://github.com/outr/reactify) - Scala 的函数式反应式编程框架。
* [chimney](https://github.com/scalalandio/chimney) - 无样板数据转换。
* [Quicklens](https://github.com/softwaremill/quicklens) - 修改深度嵌套的案例类字段。
* [Cats](https://github.com/typelevel/cats) - Scala 中函数式编程的抽象。

## 单元测试
* [µTest](https://github.com/lihaoyi/utest) - 用于单元测试的库。
* [minitest](https://github.com/monix/minitest) - 轻量级测试库。
* [scalaprops](https://github.com/scalaprops/scalaprops) - 用于基于属性的测试的库。
  * [scalaprops-shapeless](https://github.com/scalaprops/scalaprops-shapeless) - 生成任意 ADT 实例。
  * [scalaprops-cross-example](https://github.com/scalaprops/scalaprops-cross-example) - 跨平台示例。
* [ScalaCheck](https://github.com/typelevel/scalacheck) - Scala 基于属性的测试。
* [ScalaTest](https://github.com/scalatest/scalatest) - 测试库。
* [specs2](https://github.com/etorreborre/specs2) - Scala 软件规范。
* [Makeshift](https://github.com/nadavwr/makeshift) - 用于单元测试的库。
* [MUnit](https://github.com/scalameta/munit) - Scala 测试库，具有可操作的错误和可扩展的 API。

## 绑定
* [cmark](https://github.com/sparsetech/cmark-scala) - [cmark](https://github.com/commonmark/cmark) CommonMark 解析器库的绑定。
* [libuv](https://github.com/TimothyKlim/scala-native-libuv) - [libuv](https://github.com/libuv/libuv) 的绑定，异步 I/O 库。
* [SDL2 and OpenGL](https://github.com/regb/scalanative-graphics-bindings) - 图形框架 [SDL2](https://www.libsdl.org/) 和 [OpenGL](https://www.opengl.org) 的绑定。
* [Cocoa](https://github.com/jokade/scalanative-cocoa) - macOS 图形框架 [Cocoa](https://en.wikipedia.org/wiki/Cocoa_(API)) 的绑定。
* [GNU Scientific Library](https://github.com/ruivieira/scala-gsl) - [GNU 科学库 (GSL)](https://www.gnu.org/software/gsl) 的绑定。
* [BLAS](https://github.com/ekrich/sblas) - [BLAS](http://www.netlib.org/blas/) 的绑定，线性代数库。
* [Gtk+](https://github.com/jokade/scalanative-gtk) - [GTK+](https://www.gtk.org/) 图形工具包的绑定。
* [libsoup](https://github.com/jokade/scalanative-libsoup) - [libsoup](https://wiki.gnome.org/Projects/libsoup) HTTP 客户端/服务器库的绑定。
* [libui](https://github.com/lolgab/scalaui) - 基于[libui](https://github.com/andlabs/libui)的GUI框架。
* [GStreamer](https://github.com/jokade/scalanative-gstreamer) - [GStreamer](https://gstreamer.freedesktop.org) 多媒体框架的绑定。
* [Qt](https://github.com/jokade/scalanative-qt5) - [Qt](https://www.qt.io) 的绑定。
* [ncurses](https://github.com/edadma/ncurses) - [GNU Ncurses 库](https://www.gnu.org/software/ncurses/) 的绑定。
* [readline](https://github.com/edadma/readline) - [GNU Readline 库](https://www.gnu.org/software/readline/) 的绑定。
* [libsndfile](https://github.com/edadma/libsndfile) - 用于采样声音操作的 [Libsndfile](https://tiswww.cwru.edu/php/chet/libsndfile/rltop.html) C 库的绑定。
* [libpng](https://github.com/edadma/libpng) - 用于读取和写入 PNG 的 [libpng](http://www.libpng.org/) C 参考库的绑定。
* [libcairo](https://github.com/edadma/libcairo) - [Cairo](https://www.cairgraphics.org/) 2D 图形 C 库的绑定。
* [cairo-xlib](https://github.com/edadma/cairo-xlib) - [Cairo](https://www.cairgraphics.org/) 2D 图形 [XLib Surfaces](https://www.cairgraphics.org/manual/cairo-XLib-Surfaces.html) 的绑定以及 [XLib](https://www.x.org/releases/current/doc/libX11/libX11/libX11.html) 的绑定。
* [libyaml](https://github.com/edadma/libyaml) - 用于解析 [YAML](https://yaml.org/) 的 [LibYAML](https://pyyaml.org/wiki/LibYAML) C 库的绑定。
* [iup](https://github.com/edadma/iup) - 用于构建图形用户界面的 [IUP](https://www.tecgraf.puc-rio.br/iup/) 多平台工具包的绑定。

## 文件格式和解析器
* [msgpack4z](https://github.com/msgpack4z/msgpack4z-native) - 二进制序列化格式 [MessagePack](https://msgpack.org/) 的实现。
* [FastParse](https://github.com/com-lihaoyi/fastparse) - 用于定义和运行解析器的库。
* [scalatags](https://github.com/com-lihaoyi/scalatags) - HTML/XML 构建和呈现。
* [Pine](https://github.com/sparsetech/pine) - HTML/XML 解析、操作和呈现。
* [scala-json](https://github.com/MediaMath/scala-json) - JSON 解析器。
* [uPickle](https://github.com/com-lihaoyi/upickle) - uPickle：一个简单、快速、无依赖的 Scala JSON 和二进制 (MessagePack) 序列化库
* [toml-scala](https://github.com/sparsetech/toml-scala) - [TOML](https://github.com/toml-lang/toml) 具有编解码器派生的解析器。
* [argonaut](https://github.com/argonaut-io/argonaut) - 纯函数式 JSON 解析器和库。
* [ScalaPB](https://github.com/scalapb/ScalaPB) - Scala 的 [协议缓冲区](https://developers.google.com/protocol-buffers/) 编译器。
  * [scalapb-argonaut](https://github.com/scalapb-json/scalapb-argonaut) - 基于 [Argonaut](http://argonaut.io) 的 ScalaPB 的 JSON 和 Protocol Buffer 转换器。
* [sconfig](https://github.com/ekrich/sconfig) - [HOCON](https://github.com/ekrich/sconfig/blob/master/docs/original/HOCON.md) 解析器。
* [squiggly](https://github.com/edadma/squiggly) - Scala 的跨平台模板语言，受到 Liquid 和 Hugo 模板的启发。

## 数据库
* [scala-native-jdbc](https://github.com/lolgab/scala-native-jdbc) - 数据库访问层 [JDBC](https://en.wikipedia.org/wiki/Java_Database_Connectivity) 到 Scala Native 的端口。
* [SQLite4S](https://github.com/david-bouyssie/sqlite4s) - Java 库 [Sqlite4java](https://bitbucket.org/almworks/sqlite4java) 的端口。包括 SQLite 本机库的绑定。
* [libpq4s](https://github.com/david-bouyssie/libpq4s) - 异步 PostgreSQL C 库 libpq 的 Scala 包装器。
* [skunk](https://github.com/typelevel/skunk) - Scala + Postgres 的数据访问库。

## 网页开发
* [Trail](https://github.com/sparsetech/trail) - 路由库。
* [sttp](https://github.com/softwaremill/sttp) - HTTP 客户端库。
* [snunit](https://github.com/lolgab/snunit) - 基于 NGINX Unit 的 Scala Native HTTP 服务器。

## 并发性
* [scala-native-loop](https://github.com/scala-native/scala-native-loop) - Scala Native 的事件循环和面向异步的 IO
* [castor](https://github.com/com-lihaoyi/castor) - Scala 的轻量级类型 Actor 库。

## 记录
* [scribe](https://github.com/outr/scribe) - 快速而简单的日志库。
* [slogging](https://github.com/jokade/slogging) - 基于宏的 [Typesafe-logging](https://github.com/lightbend/scala-logging) 和 [SLF4J](https://www.slf4j.org/) 兼容日志库。

## 控制台
* [fansi](https://github.com/com-lihaoyi/fansi) - 用于创建 [ANSI 颜色字符串](https://en.wikipedia.org/wiki/ANSI_escape_code) 的库。
* [scopt](https://github.com/scopt/scopt) - 命令行参数解析器。
* [scala-optparse-applicative](https://github.com/xuwei-k/optparse-applicative) - Haskell 的 CLI 参数解析库的端口 [optparse-applicative](https://hackage.haskell.org/package/optparse-applicative)。
* [scallop](https://github.com/scallop/scallop) - 一个简单的 Scala CLI 解析库。
* [mainargs](https://github.com/com-lihaoyi/mainargs) - 用于 Scala 中命令行参数解析的小型、无依赖库。
* [decline](https://github.com/bkirwi/decline) - Scala 的可组合命令行解析器。

## 机器人技术
* [Potassium](https://github.com/Team846/potassium) - 编写机器人软件的框架。
* [WPILib](https://github.com/Team846/scala-native-wpilib) - 重新实现 [FIRST Robotics WPILib 库](http://first.wpi.edu/FRC/roborio/release/docs/java/)。

## 节目
* [sglgears](https://github.com/Milyardo/sglgears) - GL 端口 [gears.c](https://github.com/JoakimSoderberg/mesademos/blob/master/src/xdemos/glxgears.c)。
* [k8s-cli](https://github.com/fsat/k8s-cli) - CLI 工具，用于为基于 [Akka](https://akka.io/)、[Play Framework](https://www.playframework.com/) 和 [Lagom](https://www.lagomframework.com/) 的应用程序生成 [Kubernetes](https://kubernetes.io/) 资源。
* [Coursier](https://github.com/coursier/coursier) - Coursier 的 [`bootstrap` 命令](https://get-coursier.io/docs/cli-native-bootstrap) 生成本机启动器。
* [fractals](https://github.com/Rusty-Bike/fractals) - 具有基本动画支持的自相似分形生成器。
## 基础设施
* [Seed Docker image](https://hub.docker.com/r/tindzk/seed/tags) - 使用 [Seed](https://github.com/tindzk/seed) 进行跨平台构建的 Docker 映像。
* [scala-native-sbt-docker](https://github.com/ScalaWilliam/scala-native-sbt-docker) - Scala Native 和 sbt 的 Docker 镜像。

## 执照
<a rel="licence" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons Licence" style="border-width:0" src="https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/by.svg" /></a><br />This work is licenced under a <a rel="licence" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International Licence</a>.
