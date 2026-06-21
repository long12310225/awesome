# 很棒的 WebAssembly [![Awesome](https://awesome.re/badge-flat2.svg)](https://awesome.re)
<a href="https://webassembly.org/"><img src="media/wasm-logo.png" alt="Wasm Logo" align="right" style="height: 120px; width: 120px"></a>
WebAssembly 资源、项目和社区的精选。
> [WebAssembly](https://webassemble.org/)（缩写为 Wasm）是基于堆栈的虚拟机的二进制指令格式。 Wasm 被设计为编程语言的可移植编译目标，支持在网络上部署客户端和服务器应用程序。

## 内容

- [Resources](#resources)
  - [Basics](#basics)
  - [Articles](#articles)
  - [Books](#books)
  - [Videos](#videos)
- [Projects](#projects)
  - [Compilers](#compilers)
  - [Runtimes](#runtimes)
  - [Libraries](#libraries)
  - [Tools](#tools)
  - [Frameworks](#frameworks)
- [Communities](#communities)

## 资源

### 基础知识

- [WebAssembly MDN](https://developer.mozilla.org/en-US/docs/WebAssembly)
- [WebAssembly 规范](https://webassembly.github.io/spec/)

### 文章

- [What is WebAssembly?](https://medium.com/javascript-scene/what-is-webassembly-the-dawn-of-a-new-era-61256ec5a8f6) - 埃里克·埃利奥特，2015。
- [7 Things You Should Know About WebAssembly](https://auth0.com/blog/7-things-you-should-know-about-web-assembly/) - 塞巴斯蒂安·佩罗特，2015。
- [WebAssembly Demystified](https://floooh.github.io/2017/06/09/webassembly-demystified.html) - 安德烈·韦斯弗洛格，2017。
- [Why WebAssembly?](https://medium.com/dfinity/why-webassembly-f21967076e4) - 安德烈亚斯·罗斯伯格，2018。
- [The world's easiest introduction to WebAssembly](https://medium.com/free-code-camp/webassembly-with-golang-is-fun-b243c0e34f02) - 马丁·奥尔桑斯基，2019。
- [The Future of Programming: WebAssembly & Life After JavaScript](https://www.sitepoint.com/future-programming-webassembly-life-after-javascript/) - 埃里克·埃利奥特，2024。
- [The Web Assembles](https://blog.scottlogic.com/ceberhardt/assets/white-papers/the-web-assembles.pdf) - 克里斯·普莱斯和科林·艾伯哈特，2017 年。
- [An Empirical Study of Real-World WebAssembly Binaries](https://dlehmann.eu/publications/WasmBench-www2021.pdf) - 亚伦·希尔比格、丹尼尔·莱曼和迈克尔·普拉德尔，2021 年。
- [Not So Fast: Analyzing the Performance of WebAssembly vs. Native Code](https://www.usenix.org/system/files/atc19-jangda.pdf) - Abhinav Jangda、Bobby Powers、Emery D. Berger 和 Arjun Guha，2019 年。
- [Provably-Safe Multilingual Software Sandboxing using WebAssembly](https://www.usenix.org/system/files/sec22-bosamiya.pdf) - Jay Bosamiya、Wen Shih Lim 和 Bryan Parno，2022 年。
- [Wasabi: A Framework for Dynamically Analyzing WebAssembly](https://software-lab.org/publications/asplos2019_Wasabi.pdf) - 丹尼尔·莱曼和迈克尔·普拉德尔，2019。
- [Bringing the Web up to Speed with WebAssembly](https://github.com/WebAssembly/spec/blob/main/papers/pldi2017.pdf) - 安德烈亚斯·哈斯、安德烈亚斯·罗斯伯格、德里克·L·舒夫、本·L·蒂策、迈克尔·霍尔曼、丹·戈曼、卢克·瓦格纳、阿隆·扎凯、JF·巴斯蒂安，2017 年。

### 书籍

- [Rust and WebAssembly](https://rustwasm.github.io/docs/book/) - 描述如何一起使用 Rust 和 WebAssembly 的开源书籍。
- [Programming WebAssembly with Rust](https://pragprog.com/titles/khrust/programming-webassembly-with-rust/) - 凯文·霍夫曼，2019。
- [The Art of WebAssembly](https://nostarch.com/art-webassembly) - 里克·巴特格莱恩，2021。

### 视频

- [WebAssembly](https://www.youtube.com/watch?v=NhAPPQqKCi8) - 尼克·布雷，2015。
- [What is WebAssembly?](https://www.youtube.com/watch?v=HktWin_LPf4) - 林·克拉克，2017。
- [Get Going with WebAssembly](https://www.youtube.com/watch?v=iTrx0BbUXI4) - 约翰·布兰德霍斯特，2018。
- [WebAssembly and the Death of JavaScript](https://www.youtube.com/watch?v=pBYqen3B2gc) - 科林·艾伯哈特，2018。

## 项目

### 编译器

- [Emscripten](https://emscripten.org/) - 将 C 和 C++ 编译为 WebAssembly。
- [AssemblyScript](https://www.assemblyscript.org/) - 类似 TypeScript 的语言编译为 WebAssembly。
- [Binaryen](https://github.com/WebAssembly/binaryen) - WebAssembly 的编译器基础设施。
- [TinyGo](https://tinygo.org/) - WebAssembly 的 Go 编译器。

### 运行时

- [Wasmtime](https://wasmtime.dev/) - 独立的 WebAssembly 运行时。
- [WasmEdge](https://github.com/WasmEdge/WasmEdge) - 高性能 WebAssembly 运行时。
- [WAVM](https://github.com/WAVM/WAVM) - WebAssembly 虚拟机。
- [Wasm3](https://github.com/wasm3/wasm3) - 小型、快速的 WebAssembly 解释器。
- [Wasmer](https://wasmer.io/) - 适用于桌面、云和边缘的 WebAssembly 运行时。

### 图书馆

- [wasm-bindgen](https://github.com/rustwasm/wasm-bindgen) - Rust 和 JavaScript 之间的互操作性。
- [wasmer-js](https://github.com/wasmerio/wasmer-js) - JavaScript 的 WebAssembly 运行时。
- [wasm-pack](https://github.com/rustwasm/wasm-pack) - 构建、测试和发布 Rust 生成的 Wasm。
- [Wabt](https://github.com/WebAssembly/wabt) - WebAssembly 二进制工具包。
- [WASI](https://github.com/WebAssembly/WASI) - WebAssembly 系统接口。

### 工具

- [Wasm Explorer](https://mbebenita.github.io/WasmExplorer/) - 可视化和调试 WebAssembly 二进制文件。
- [wasm2c](https://github.com/WebAssembly/wabt/tree/main/wasm2c) - 将 WebAssembly 二进制文件转换为 C。
- [Cross-Origin Isolation Checker](https://app.cinevva.com/tools/cross-origin-isolation-checker) - 检查页面是否跨源隔离（COOP/COEP）、SharedArrayBuffer 和多线程 WebAssembly 的要求。

### 框架

- [Blazor](https://blazor.net/) - 在 WebAssembly 上运行的 .NET Web 框架。
- [Yew](https://yew.rs/) - 使用 WebAssembly 构建 Web 应用程序的 Rust 框架。
- [Leptos](https://github.com/leptos-rs/leptos) - 适用于 WebAssembly Web 应用程序的全栈 Rust 框架。

## 社区

- [WebAssembly GitHub 组织](https://github.com/WebAssembly)
- [W3C WebAssembly 组](https://www.w3.org/wasm/)
- [WebAssembly Reddit 子版块](https://www.reddit.com/r/webassembly/)


## 贡献

欢迎贡献。在提交更改之前，请阅读[贡献指南](https://github.com/idematos/awesome-webassemble/blob/main/contributing.md)。
