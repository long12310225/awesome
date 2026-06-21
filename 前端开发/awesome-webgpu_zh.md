# 很棒的 WebGPU [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[<img src="https://www.w3.org/2023/02/webgpu-logos/webgpu-notext.svg"align="right" height="150">](https://www.w3.org/TR/webgpu/)


> 精心策划的 WebGPU 资源、库和工具列表。

WebGPU 是 [W3C](https://www.w3.org/) 的一项正在进行中的 Web 标准，用于现代 3D 和 GPU 计算。其目的是在从台式机到移动设备的最新 GPU 上获得最佳性能。与 WebGL 不同，WebGPU 不是现有本机 API 的端口。它借鉴了 Metal、Vulkan 和 Direct3D12 的概念。

## 内容

- [Websites](#websites)
- [浏览器支持](#browser-support)
- [Articles](#articles)
- [Tutorials](#tutorials)
- [Books](#books)
- [Libraries](#libraries)
- [调试器和分析器](#debuggers-and-profilers)
- [Gists](#gists)
- [Demos](#demos)
- [Videos](#videos)
- [Presentations](#presentations)
- [Community](#community)
- [错误报告](#bug-reporting)

## 网站

### 官方网站
- [GPUWeb](https://github.com/gpuweb/gpuweb) - 官方 GitHub 存储库。
- [官方 WebGPU 讲解器](https://gpuweb.github.io/gpuweb/explainer/)

### WebGPU 规格
- [History](https://www.w3.org/standards/history/webgpu/)
- [编辑草稿](https://gpuweb.github.io/gpuweb/)
### WGSL（WebGPU 着色语言）规范
- [工作草案](https://www.w3.org/TR/WGSL/)
- [编辑草稿](https://gpuweb.github.io/gpuweb/wgsl/)


### API文档
- [API quick reference and documentation](https://webgpu.rocks/) - WebGPU.rocks。
- [MDN](https://developer.mozilla.org/en-US/docs/Web/API/WebGPU_API) - MDN WebGPU API 参考。

### 杂项
- [谷歌开发者网站](https://developer.chrome.com/docs/web-platform/webgpu)
- [107 WebGPU Projects on GitHub](https://awesomeopensource.com/projects/webgpu) - AwesomeOpenSource.com。
- [r/WebGPU - Reddit](https://www.reddit.com/r/webgpu/) - WebGPU Reddit 子版块。
- [compute.toys](https://compute.toys/) - 计算着色器游乐场（如shaderoy）。
- [Shadeup](https://shadeup.dev/) - 使 WebGPU 实验变得更容易的语言/网站。
- [Tour of WGSL](https://google.github.io/tour-of-wgsl/) - WebGPU 着色语言的快速介绍。
- [WebGPU Experts Blog](https://www.webgpuexperts.com/blog) - 有关 WebGPU 的每月新闻。

## 浏览器支持
> 这是一项实验性技术
- [Implementation status](https://github.com/gpuweb/gpuweb/wiki/Implementation-Status) - 官方 W3C 组。
- [WebGPU browser support overview](https://caniuse.com/webgpu) - CanIUse.com WebGPU。

### 镀铬
> Chrome 和基于 Blink/Chromium 的浏览器支持 WebGPU
- [Desktop](https://www.google.com/chrome/) - Windows 和 macOS 默认支持 WebGPU。
- [Android](https://developer.chrome.com/blog/new-in-webgpu-121) - 默认支持 WebGPU。
- [Edge](https://www.microsoft.com/edge/) - 默认支持 WebGPU。

### 火狐浏览器
> WebGPU 支持仍处于实验阶段
- [Firefox Nightly](https://nightly.mozilla.org/) - 转到“about:config”并将“dom.webgpu.enabled”设置为 true。

### 狩猎之旅
> WebGPU 支持仍处于实验阶段
- [macOS Safari TP](https://developer.apple.com/safari/resources/) - 自 190 起默认启用 WebGPU。
- [macOS Safari](https://www.apple.com/safari/) - 在 macOS 26 Tahoe 或更高版本上默认启用 WebGPU；早期版本需要“WebGPU”功能标志。
- [iOS/iPadOS Safari](https://mil-tokyo.github.io/webdnn/docs/tips/enable_webgpu_ios.html) - iOS/iPadOS 26 或更高版本默认支持 WebGPU；早期版本需要“设置”→ `Safari` 右箭头; “高级”→ `功能标志` 右箭头; `WebGPU`。

## 文章

- [WebGPU](https://en.wikipedia.org/wiki/WebGPU) - 维基百科文章。
- [A Taste of WebGPU in Firefox](https://hacks.mozilla.org/2020/04/experimental-webgpu-in-firefox/) - Mozilla.org 文章，作者：Dzmitry Malyshau。
- [Point of WebGPU native](https://kvark.github.io/web/gpu/native/2020/05/03/point-of-webgpu-native) - 作者：德兹米特里·马利肖。
- [Graphics on the web and beyond with WebGPU](https://dmnsgn.medium.com/13c4ba049039) - 作者：[Damien Seguin](https://dmnsgn.medium.com/)。
- [Implementing WebGPU in Gecko](https://kvark.github.io/web/gpu/gecko/2019/12/10/gecko-webgpu) - 作者：[Dzmitry Malyshau](https://github.com/kvark)。
- [From WebGL to WebGPU in Construct](https://www.construct.net/en/blogs/ashleys-blog-2/webgl-webgpu-construct-1519) - 作者：阿什利·古伦。
- [A brief history of graphics on the web and WebGPU](https://www.construct.net/en/blogs/ashleys-blog-2/brief-history-graphics-web-1517) - 作者：阿什利·古伦。
- [WebGPU texture best practices](https://toji.github.io/webgpu-best-practices/img-textures.html) - 作者：布兰登·琼斯。
- [WebGPU Buffer upload best practices](https://toji.github.io/webgpu-best-practices/buffer-uploads.html) - 作者：布兰登·琼斯。
- [wgpu-rs on the web](https://gfx-rs.github.io/2020/04/21/wgpu-web) - Rust 图形法师。
- [Compiling Machine Learning to WASM and WebGPU with Apache TVM](https://tvm.apache.org/2020/05/14/compiling-machine-learning-to-webassembly-and-webgpu) - 作者：[Tianqi Chen](https://github.com/tqchen) & [Jared Roesch](https://github.com/jroesch)。
- [The WebAssembly App Gap](https://paulbutler.org/2020/the-webassembly-app-gap/) - 作者：[保罗·巴特勒](https://github.com/paulgb)。
- [Next-generation 3D Graphics on the web](https://webkit.org/blog/7380/next-generation-3d-graphics-on-the-web/) - Webkit.org 文章，作者：[Dean Jackson](https://twitter.com/grorgwork)。
- [Efficently rendering glTF models - A WebGPU Case Study](https://toji.github.io/webgpu-gltf-case-study/) - 作者：[布兰登·琼斯](https://github.com/toji)。
- [WebGPU - All of the cores, none of the canvas](https://surma.dev/things/webgpu/index.html) - 作者：[Surma](https://github.com/surma)。
- [WebGPU Fundamentals](https://webgpufundamentals.org/) - 一组帮助学习 WebGPU 的文章。
- [PBR in WebGPU: implementation details](https://tchayen.com/pbr-in-webgpu-implementation-details) - 作者：[Tomasz Czajecki](https://github.com/tchayen)。
- [I want to talk about WebGPU](https://cohost.org/mcc/post/1406157-i-want-to-talk-about-webgpu) - 作者：[Andi](https://mastodon.social/@mcc)。
- [From WebGL to WebGPU](https://developer.chrome.com/blog/from-webgl-to-webgpu/) - 通过谷歌。
- [WebGPU for Dummies](https://amirsojoodi.github.io/posts/WebGPU-for-Dummies/) - 作者：阿米尔·索乔迪。
- [WebGPU Timestamps](https://amirsojoodi.github.io/posts/WebGPU-Timestamp/) - 作者：阿米尔·索乔迪。
- [WebAssembly and WebGPU](https://developer.chrome.com/blog/io24-webassembly-webgpu-2) - 了解 WebAssembly 和 WebGPU 如何提高 Web 上的机器学习性能第 2 部分。

## 教程

- [Raw WebGPU](https://alain.xyz/blog/raw-webgpu) - [Alain Galvan](https://github.com/alaingalvan) 概述了如何编写 WebGPU 应用程序。
- [Basic WebGPU Rendering](https://dev.to/ndesmic/basic-webgpu-rendering-2kob) - 渲染场景的步骤摘要，作者：[@ndesmic](https://github.com/ndesmic)。
- [Get started with GPU Compute on the Web](https://web.dev/gpu-compute/) - 有关如何将 WebGPU 用于非图形应用程序的教程，作者：[François Beaufort](https://github.com/beaufortfrancois)。
- [面向 Metal 开发人员的 WebGPU 第 1 部分](https://metalbyexample.com/webgpu-part-one/) 和 [第 2 部分](https://metalbyexample.com/webgpu-part-two/) - Apple 的 GPU API Metal 中的 WebGPU 简介，作者：[Warren Moore](https://twitter.com/warrenm)。
- [使用 WebGPU 从 0 到 glTF：系列](https://www.willusher.io/graphics/2023/04/10/0-to-gltf-triangle/) [(repository)](https://github.com/Twinklebear/webgpu-0-to-gltf?tab=readme-ov-file) - 创建 glTF 模型查看器的教程，作者：[Will亚瑟小子](https://github.com/Twinklebear)。
- [Learn wgpu](https://sotrh.github.io/learn-wgpu/) - wgpu 的教程和示例，WebGPU 的 Rust 实现，作者：[@sotrh](https://github.com/sotrh)
- [LearningWebGPU 教程 (Chinese)](https://github.com/hjlld/LearningWebGPU) - 作者：[@hjlld](https://github.com/hjlld)。
- [Real-Time Ray-Tracing in WebGPU](https://maierfelix.github.io/2020-01-13-webgpu-ray-tracing/) - 使用 WebGPU 实现的修改版本以及 Vulkan 和 DX12 光线追踪扩展构建光线追踪器，作者：[Felix Maier](https://github.com/maierfelix)。
- [Build a compute rasterizer in WebGPU](https://github.com/OmarShehata/webgpu-compute-rasterizer/blob/main/how-to-build-a-compute-rasterizer.md) - 如何使用计算着色器构建完整的光栅化器，作者：[Omar Shehata](https://github.com/OmarShehata)。
- [WebGPU Engine Development (Chinese/English)](https://arche.graphics/docs/intro) - WebGPU Engine（C++和TypeScript）的开发流程。
- [Learn WebGPU for native C++ development](https://eliemichel.github.io/LearnWebGPU) - 有关使用 wgpu 或 Dawn 的桌面应用程序 WebGPU 的教程，作者：[@eliemichel](https://github.com/eliemichel)。

## 书籍

- [Practical WebGPU Graphics](https://books.google.com/books?id=tPQyEAAAQBAJ&printsec=frontcover) - 作者：[Jack Xu](https://github.com/jack1232)

## 图书馆

- [Babylon.js](https://doc.babylonjs.com/setup/support/webGPU) - 打开游戏和渲染引擎。
- [Three.js](https://threejs.org/) - 易于使用、轻量级、通用 3D 库。
- [PlayCanvas](https://playcanvas.com/) - 基于 WebGPU 的游戏引擎。
- [PixiJS](https://pixijs.com/) - 带有 WebGPU 渲染器的 2D 渲染引擎。
- [Dawn](https://dawn.googlesource.com/dawn) - Google 在 Chromium 中为 WebGPU 提供支持的实现可以用作独立包。
- [wgpu](https://github.com/gfx-rs/wgpu) - Firefox 中使用的 Mozilla 实现。与 Dawn 一样，可以作为独立包使用。
- [webgpu-headers](https://github.com/webgpu-native/webgpu-headers) - C/C++ 头文件。
- [sokol](https://github.com/floooh/sokol/) - 适用于 C 和 C++ 的简单 STB 风格跨平台库。
- [RedGPU](https://github.com/redcamel/RedGPU) - JavaScript WbeGPU 库，作者：[@redcamel](https://github.com/redcamel)。
- [WebGPU .NET](https://github.com/WaveEngine/WebGPU.NET) - .NET 绑定，构建在 wgpu 之上。
- [Deno](https://deno.com/) - 基于 V8 引擎的 JavaScript、TypeScript 和 WebAssembly 运行时。
- [RedCube](https://github.com/Reon90/redcube) - 基于 WebGPU 后端的 glTF 查看器。
- [hwoa-rang-gpu](https://github.com/gnikoloff/hwoa-rang-gpu) - Micro WebGPU 渲染和计算库。
- [wgsl_reflect](https://github.com/brendan-duncan/wgsl_reflect) - 用于 JavaScript 的 WebGPU 着色语言解析器和反射库。
- [Arche Graphics](https://github.com/yangfengzzz/Arche.js) - WebGPU 图形引擎。
- [WebGPU-C++](https://github.com/eliemichel/WebGPU-Cpp) - 一个单文件零开销 C++ 惯用包装器，作者：@eliemichel。
- [Use.GPU](https://usegpu.live) - 反应式/声明式 WebGPU 运行时。
- [GEngine](https://github.com/hpugis/GEngine) - 一个基于WebGPU的基础渲染引擎，作者：junwei.gu。
- [Thimbleberry](https://github.com/mighdoll/thimbleberry) - 可重复使用的 WebGPU 着色器和支持功能。
- [WebRTX](https://github.com/codedhead/webrtx) - WebGPU 光线追踪扩展。
- [SWGPU](https://github.com/jay19240/SWGPU) - 一个简单的 WebGPU 游戏引擎。
- [React Native WebGPU](https://github.com/wcandillon/react-native-webgpu) - 使用 Dawn 的 React Native 实现 WebGPU。
- [TypeGPU](https://typegpu.com/) - TypeScript API，用于构建、写入和读取具有推断类型安全的 GPU 缓冲区。
- [WESL](https://github.com/wgsl-tooling-wg/wesl-spec/blob/main/README.md) - 用于“import”、“@if”等的 WGSL 扩展。
- [WebGpGpu.ts](https://github.com/eddow/webgpgpu) - 用于访问计算着色器、浏览器或服务器端的 WebGPU 框架，无需陡峭的学习曲线。
- [spark.js](https://ludicon.com/sparkjs/) - 用于 WebGPU 的实时 GPU 纹理压缩库。
- [zephyr3d](https://zephyr3d.org/) - 基于 TypeScript 的 3D 渲染引擎，支持 WebGPU/WebGL。
- [ChartGPU](https://github.com/chartgpu/chartgpu) - 基于 WebGPU 构建的高性能图表库，以 60fps 处理 1M+ 数据点。

## 调试器和分析器
- [webgpu-inspector](https://github.com/brendan-duncan/webgpu_inspector) - WebGpu 的检查调试器。
- [webgpu-profiler](https://crates.io/crates/wgpu-profiler) - Rust + WebGPU 的分析器。

这些已经有一段时间没有更新了：
- [webgpu-devtools](https://github.com/takahirox/webgpu-devtools) - Web 浏览器扩展。
- [webgpu-debugger](https://github.com/webgpu/webgpu-debugger) - 早期调试器。

## 要点

- [2D](https://gist.github.com/munrocket/30e645d584b5300ee69295e54674b3e4) 和 [3D SDF 原语](https://gist.github.com/munrocket/f247155fc22ecb8edf974d905c677de1) - WGSL 中的有符号距离场原语，作者：[@munrocket](https://github.com/munrocket)。

## 演示

目前，演示在 Chrome/Edge 上效果最佳。

- [WebGPU Samples](https://webgpu.github.io/webgpu-samples/) - 一组演示 WebGPU API 使用的示例和演示 - [存储库](https://github.com/webgpu/webgpu-samples)
- [WebGPU first-person exploration of the Sponza Palace](https://toji.github.io/webgpu-test/) - WebGL、WebGL 2.0 和 WebGPU 之间的场景渲染比较，作者：Brandon Jones - [存储库](https://github.com/toji/webgpu-test)
- [WebGPU Clustered Shading](https://toji.github.io/webgpu-clustered-shading/) - 作者：布兰登·琼斯 - [存储库](https://github.com/toji/webgpu-clustered-shading)
- [WebGPU Metaballs](https://toji.github.io/webgpu-metaballs/) - 作者：布兰登·琼斯 - [存储库](https://github.com/toji/webgpu-metaballs)
- [WebGPU External Texture Test](https://toji.github.io/webgpu-external-test/) - 作者：布兰登·琼斯 - [存储库](https://github.com/toji/webgpu-external-test)
- [Online WGSL Editor](https://takahirox.github.io/online-wgsl-editor/) - 作者：[Takahiro](https://github.com/takahirox) - [存储库](https://github.com/takahirox/online-wgsl-editor)
- [Three.js WebGPU examples](https://threejs.org/examples/?q=webgpu) - 使用 WebGPU 渲染器的 Three.js 示例集合 - [存储库](https://github.com/mrdoob/ Three.js/tree/dev/examples#:~:text=webgpu_compute.html)
- [Spookyball](https://spookyball.com) - 万圣节主题的开源 Breakout 克隆，作者：Brandon Jones - [存储库](https://github.com/toji/spookyball)
- [Babylon.js Playground](https://playground.babylonjs.com/) - 作者：[Babylon.js](https://www.babylonjs.com/)（注意：选择右上角的“WebGPU”）。
- [PlayCanvas WebGPU Demos](https://playcanvas.vercel.app/) - 通过 [PlayCanvas](https://playcanvas.com/) （注意：选择右上角的“WebGPU”）。
- [Project Prismatic](https://play.projectprismatic.com) - Stratton Studios Unity 支持的 WebGPU 体验/演示。
- [WebGPU Particles](https://hsimpson.github.io/webgpu-particles/) - 计算并渲染粒子，作者：[Daniel Toplak](https://github.com/hsimpson) - [存储库](https://github.com/hsimpson/webgpu-articles)
- [An online WebGPU calculator](https://laskin.live) - 一个在线计算器，但你只能在远程朋友的 GPU 上使用它（通过 WebRTC） - [存储库](https://github.com/periferia-labs/laskin.live)
- [WebGPU Examples](https://tsherif.github.io/webgpu-examples/) - 在 WebGPU 中实现的渲染算法的一些示例，作者：[Tarek Sherif](https://github.com/tsherif) - [存储库](https://github.com/tsherif/webgpu-examples)
- [wgpu examples](https://wgpu.rs/examples/) - 来自 [wgpu](https://wgpu.rs) 库的官方示例列表 - [存储库](https://github.com/gfx-rs/wgpu/tree/trunk/examples)
- [Forest WebGPU](https://www.babylonjs.com/Demos/WebGPU/forestWebGPU.html) - 使用 Babylon.js 构建的场景。
- [WebGPU-Playground](https://06wj.github.io/WebGPU-Playground/) - 实验 WebGPU 的游乐场，作者：[@06wj](https://github.com/06wj) - [存储库](https://github.com/06wj/WebGPU-Playground)
- [Dawn RT](https://github.com/maierfelix/dawn-ray-tracing) - 带有光线追踪扩展的黎明之叉，作者：Felix Maier。
- [wgpu-load-test](https://github.com/MacTuitui/wgpu-load-test) - 由 [Alexis Andre](https://github.com/MacTuitui) 进行的 wgpu 压力测试。
- [WebGPU Compute 101 Demo](https://hello-webgpu-compute.glitch.me) - 使用计算着色器的简单示例。 [来源](https://glitch.com/edit/#!/hello-webgpu-compute)
- [WebGPU 2D Fluid Simulation](https://kishimisu.github.io/WebGPU-Fluid-Simulation/) - “游戏实时流体动力学”论文的实现，作者：[kishimisu](https://github.com/kishimisu) - [存储库](https://github.com/kishimisu/WebGPU-Fluid-Simulation)
- [WebGPU-Lab](https://s-macke.github.io/WebGPU-Lab/) - 演示和实验，重点关注计算着色器，作者：[Sebastian Macke](https://github.com/s-macke) - [存储库](https://github.com/s-macke/WebGPU-Lab)
- [WebGPU Live Demo Editor](https://www.wgsl.dev/editor) - [Hepp Maccoy](https://github.com/hepp) 的 WebGPU 示例集合 - [存储库](https://github.com/hepp/webgpu-examples)
- [Thimbleberry Image Transform Demo](https://thimbleberry.dev) - 使用 Thimbleberry 构建的图像处理应用程序，作者：[mighdoll](https://vis.social/@mighdoll) - [存储库](https://github.com/mighdoll/thimbleberry/tree/main/image-demo)
- [Shadowray Playground](https://shadowray.gl) - WebRTX 的演示，是具有光线追踪功能的 WebGPU API 的扩展，由 [codedhead](https://github.com/codedhead) 使用计算着色器实现。
- [Web Stable Diffusion](https://mlc.ai/web-stable-diffusion/#text-to-image-generation-demo) - 图像生成器 AI 模型的实现，由 CMU、OctoML、Catalyst 等人实现 - [存储库](https://github.com/mlc-ai/web-stable-diffusion)
- [WebLLM](https://mlc.ai/web-llm/) - LLM 推理引擎，由 CMU、华盛顿大学、OctoML 等人开发 - [存储库](https://github.com/mlc-ai/web-llm)
- [Shader Graph WGSL](https://deepkolos.github.io/shader-graph-wgsl/) - 基于节点的着色器编辑器，作者：[deepkolos](https://github.com/deepkolos) - [存储库](https://github.com/deepkolos/shader-graph-wgsl)
- [WebGPU Memory Model Testing](https://gpuharbor.ucsc.edu/webgpu-mem-testing/) - 内存模型测试套件，作者：[Reese Levine](https://github.com/reeselevine) 等人，加州大学圣克鲁斯分校 - [存储库](https://github.com/reeselevine/webgpu-litmus)
- [Marching Cubes WebGPU](https://conorpo.github.io/marching-cubes-webgpu/) - Marching 立方体实现，作者：[Conor O'Malley](https://github.com/conorpo) - [存储库](https://github.com/conorpo/marching-cubes-webgpu)
- [WebGPU Path Tracing](https://iamferm.in/webgpu-path-tracing/) - 由 WebGPU 计算着色器提供支持的路径跟踪器，作者：[Fermin Lozano](https://github.com/ferminLR) - [存储库](https://github.com/ferminLR/webgpu-path-tracing)
- [WebGPU real-time ray tracer](https://github.com/C-none/Web-RTRT/) - 实现 ReSTIR 算法的实时光线追踪器 - [存储库](https://github.com/C-none/Web-RTRT)
- [Real-Time GPU Texture Compression Demo](https://ludicon.com/sparkjs/gltf-demo/) - 展示实时纹理压缩的优势。将使用 KTX2 纹理的模型与 AVIF + Spark 进行比较。

## 视频

- [从 WebGL 到 WebGPU：Babylon js 的视角，作者：David Catuhe](https://www.youtube.com/watch?v=A2FxeEl4nWw)
- [下一代网络 3D 图形（Google I/O 2019）](https://www.youtube.com/watch?v=K2JzIUIHIhc)
- [WebGL to WebGPU (playlist)](https://www.youtube.com/playlist?list=PLMinhigDWz6f5Nm_GYGREYnaf9mzoNdjX) - 作者：[SketchpunkLabs](https://www.youtube.com/c/SketchpunkLabs)
- [WebGPU (playlist)](https://www.youtube.com/playlist?list=PLnTPVrg9-a1Ou2KXUniDr1HC7qgL2JD2x) - 作者：[Genka](https://www.youtube.com/channel/UCBTwKzJg-BR56tKWO5CT7XA)
- [WebGPU Graphics Programming Step-by-Step (playlist)](https://www.youtube.com/playlist?list=PL_UrKDEhALdKh0118flOjuAnVIGKFUJXN) - 作者：[徐博士实用编程](https://www.youtube.com/channel/UCg14XfqXim0vpgabU3T7tRg)
- [Introducing WebGPU: Unlocking modern GPU access for JavaScript](https://www.youtube.com/watch?v=m6T-Mq1BPXg) - 通过谷歌。
- [A proper look at WebGPU for native games](https://www.youtube.com/watch?v=DdMl4E7xQEY) - 作者：[马德里加尔](https://www.madrigalgames.com/)

## 演讲

- [Building WebGPU with Rust](https://fosdem.org/2020/schedule/event/rust_webgpu/) - 作者：Mozilla 的 Dzmitry Malyshau。

## 社区

- [GPU for the web community group](https://www.w3.org/community/gpu/) - W3C 社区。
- [Public GPU](https://lists.w3.org/Archives/Public/public-gpu/) - W3C 邮件列表。
- [Matrix WebGPU](https://matrix.to/#/#WebGPU:matrix.org) - 非官方渠道。
- [YC Point of WebGPU on native](https://news.ycombinator.com/item?id=23079200) - 关于本文的讨论。

## 错误报告

- [Webkit](https://bugs.webkit.org/buglist.cgi?bug_status=UNCONFIRMED&bug_status=NEW&bug_status=ASSIGNED&bug_status=REOPENED&component=WebGPU)
- [Firefox](https://bugzilla.mozilla.org/buglist.cgi?product=Core&component=Graphics%3A%20WebGPU)
- [Chromium](https://bugs.chromium.org/p/chromium/issues/list?q=component:Blink%3EWebGPU)

---

在法律允许的范围内，[Mik Bry](https://github.com/mikbry) 已放弃本作品的所有版权以及相关或邻接权。

欢迎投稿！首先阅读[贡献指南](contributing.md)。
