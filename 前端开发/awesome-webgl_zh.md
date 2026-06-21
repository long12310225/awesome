# 很棒的 WebGL [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

[<img src="webgl_logo.png"align="right"width="175">](https://www.khronos.org/webgl/)

这是一个精选的 WebGL 库、资源等等的列表。

## 什么是 WebGL

WebGL（Web 图形库）是一个 JavaScript API，用于在其中渲染交互式 3D 计算机图形和 2D 图形
任何兼容的网络浏览器，无需使用插件。 WebGL 完全集成到所有 Web 标准中
浏览器允许 GPU 加速使用物理和图像处理以及效果作为网页画布的一部分。

WebGL 元素可以与其他 HTML 元素混合，并与页面的其他部分或页面背景合成。
WebGL 程序由用 JavaScript 编写的控制代码和在计算机图形上执行的着色器代码组成
处理单元 (GPU)。

## 内容
* [WebGL](#webgl)
* [网页GL 2](#webgl-2)
* [WebVR](#webvr)
* [Libraries](#libraries)
* [Community](#community)

## 网页GL

> 所有与 WebGL 相关的事情

### WebGL 子类别
* [Articles](#articles)
* [博客系列](#blog-series)
* [Books](#books)
* [错误报告](#bug-reporting)
* [GLSL 编辑](#glsl-editors)
* [References](#references)
* [Talks](#talks)
* [Tools/Debugging](#toolsdebugging)
  * [Chrome 专用工具/调试器](#chrome-specific-toolsdebugger)
  * [Firefox 专用工具/调试器](#firefox-specific-toolsdebugger)
* [Tutorials](#tutorials)
* [Videos](#videos)

### 文章

> WebGL 文章和/或博客文章（非教程）

* [Context Loss & Preloading](https://medium.com/@mattdesl/non-intrusive-webgl-cebd176c281d#.gyc6h9mr5) - 当您遇到可怕的上下文丢失时如何管理 WebGL。
* [WebGL Off the Main Thread](https://hacks.mozilla.org/2016/01/webgl-off-the-main-thread/) - 如何在 WebGL 中使用 Web Workers。
* [Optimizing Scenes for Better WebGL Performance](https://www.soft8soft.com/docs/manual/en/introduction/Optimizing-WebGL-performance.html) - 事实证明，优化技术对于创建基于 WebGL 的交互效果非常有效。
* [First steps in WebGL](https://dev.to/aralroca/first-steps-in-webgl-385c) - 通过绘制三角形了解 WebGL 是什么及其工作原理。

### 博客系列

> WebGL 主题博客系列

* [Codeflow](http://codeflow.org/tags/webgl.html) - 许多关于不同技巧和技术的博客。
* [Real-Time Rendering](http://www.realtimerendering.com/blog/tag/webgl/) - 这是《实时渲染》一书的博客。
* [WebGL Best Practices](https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API/WebGL_best_practices) - Mozilla 的官方最佳实践集。
* [WebGL Insights](http://webglinsights.blogspot.com/) - 这是_WebGL Insights_ 一书的博客。
* [WebGL Month](https://github.com/lesnitsky/webgl-month) - 一个月的每日 WebGL 教程。
* [WebGL Image Processing](https://maximmcnair.com/webgl-image-processing) - 涵盖 WebGL 中的一系列_图像处理_算法，例如颜色校正、混合模式、阈值、抖动、卷积和胶片颗粒。

### 书籍

> 有关 WebGL 的热门书籍

* [交互式计算机图形学：使用 WebGL 自上而下的方法](https://www.amazon.com/Interactive-Computer-Graphics-Top-Down-Approach/dp/0133574849)，作者：**Edward Angel** 和 **Dave Shreiner** - 适合计算机科学与工程专业的本科生、具有良好编程技能的其他学科的学生以及对使用最新版本 WebGL 的计算机动画和图形感兴趣的专业人士。
* [专业 WebGL 编程](https://www.amazon.com/Professional-WebGL-Programming-Developing-Graphics/dp/1119968860) 作者：**Andreas Anyuru** - 有关使用 WebGL 开发硬件加速 3D 图形所需了解的一切。
* [使用 HTML5 和 WebGL 进行 3D 应用程序编程](https://www.amazon.com/Programming-Applications-HTML5-WebGL-Visualization/dp/1449362966)，作者：**Tony Parisi** - 使用 HTML5 和相关技术（例如 CSS3 和 WebGL（新兴的 Web 图形标准））创建高性能、视觉效果令人惊叹的 Web 3D 应用程序。
* [WebGL 初学者指南](https://www.amazon.com/WebGL-Beginners-Guide-Diego-Cantor/dp/184969172X)，作者：**Diego Cantor** 和 **Brandon Jones** - 适用于想要通过 WebGL 投入 3D Web 开发的 JavaScript 开发人员。
* [WebGL Hotshot](https://www.amazon.com/WebGL-Hotshot-Mitch-Williams-ebook/dp/B00KLAJ65Y) 作者：**Mitch Williams** - 适合希望扩展 3D 图形概念知识并拓宽现有技能的网页设计师。
* [WebGL Insights](https://github.com/WebGLInsights/WebGLInsights.github.io/releases/download/v1.0/WebGL.Insights.-.Patrick.Cozzi.pdf) 作者：Patrick Cozzi** - 通过汇集经验丰富的 WebGL 引擎和应用程序开发人员、GPU 供应商、浏览器开发人员、研究人员和教育工作者的贡献，为中级和高级 WebGL 开发人员展示实际技术。
  * [本书的个人网站](http://www.webglinsights.com/)
* [WebGL 编程指南：使用 WebGL 进行交互式 3D 图形编程](https://www.amazon.com/WebGL-Programming-Guide-Interactive-Graphics/dp/0321902920)，作者：**Kouichi Matsuda** 和 **Rodger Lea** - WebGL 编程指南将帮助您快速开始交互式 WebGL 3D 编程，即使您事先没有 HTML5、JavaScript、3D 图形、数学或OpenGL。

### 错误报告

> 从长远来看，报告错误对每个人都有帮助

* [Chrome Bug Report](https://bugs.chromium.org/p/chromium/issues/list) - Chrome 相关错误
* [Khronos Github Issue Page](https://github.com/KhronosGroup/WebGL/issues) - 规范或一致性相关的错误
* [Mozilla BugZilla](https://bugzilla.mozilla.org) - 火狐浏览器相关错误
* [WebKit Bugzilla](https://bugs.webkit.org/enter_bug.cgi?assigned_to=cmarrin%40apple.com&attachurl=&blocked=&bug_file_loc=http%3A%2F%2F&bug_severity=Normal&bug_status=NEW&comment=&component=WebGL&contenttypeentry=&contenttypemethod=autodetect&contenttypeselection=text%2Fplain&data=&dependson=&description=&flag_type-1=X&flag_type-3=X&form_name=enter_bug&keywords=&maketemplate=Remember%20values%20as%20bookmarkable%20template&op_sys=Mac%20OS%20X%2010.5&priority=P2&product=WebKit&rep_platform=PC&short_desc=&version=528%2B%20%28Nightly%20build%29) - Safari 相关错误

### GLSL 编辑

> 在线 GLSL 编辑器
>
> 注意：[WebGL 必须符合 OpenGL ES 着色语言版本 1.00](https://www.khronos.org/registry/webgl/specs/1.0.3/#4.3)
> 
> [GLSL 版本 1.00 官方规范](https://www.khronos.org/registry/OpenGL/specs/es/2.0/GLSL_ES_Specification_1.00.pdf)
>
> [Open ES 版本 2.0.25 的官方规范](https://www.khronos.org/registry/OpenGL/specs/es/2.0/es_full_spec_2.0.pdf)

* [Fractal Lab](http://hirnsohle.de/test/fractalLab/) - 在线分形浏览器可让您探索 2D 和 2D 分形。
* [GLSL Sandbox](http://glslsandbox.com) - 片段着色器的在线实时编辑器。
* [GLSLbin](http://glslb.in) - 支持 [glslify](https://github.com/glslify/glslify) 的片段着色器沙箱。
* [Shader Toy](https://www.shadertoy.com) - 最受欢迎的片段着色器实时编辑器。
* [ShaderFrog](https://shaderfrog.com/) - WebGL 着色器编辑器和作曲家。
* [SHDR Editor](http://shdr.bkcore.com) - 实时 GLSL 着色器编辑器、查看器和验证器。
* [ShaderExpo](https://anuraghazra.github.io/ShaderExpo/) - 无依赖性着色器编辑器，具有内嵌错误日志、自动完成、模型和纹理加载功能。

### 参考文献

> WebGL 参考

* [Google Project ANGLE](https://github.com/google/angle) - Windows 平台上 Google Chrome 和 Mozilla Firefox 的默认 WebGL 后端。
* [Khronos Official Wiki](https://www.khronos.org/webgl/wiki/) - WebGL 的官方 wiki。
* [WebVR Community Group](https://www.w3.org/community/immersive-web/) - 该组织的目标是帮助将高性能虚拟现实引入开放网络。
* [WebGL Errata](https://www.khronos.org/webgl/wiki/Errata_to_the_WebGL_Specification) - 图形驱动程序中的已知错误会影响一致性套件，从而影响代码的可移植性。
* [WebGL Extensions](https://www.khronos.org/registry/webgl/extensions/) - WebGL 扩展列表
* [WebGL Reference Card](https://www.khronos.org/files/webgl/webgl-reference-card-1_0.pdf) - 用于打印的 WebGL 1.0 API 快速参考卡。
* [WebGL Source Code](https://github.com/KhronosGroup/WebGL) - 源代码可供查看和贡献。
* [WebGL Spec Sheet](https://www.khronos.org/registry/webgl/specs/1.0/) - 有关 WebGL 的所有详细信息。


### 会谈

> WebGL相关讲座

* [List of Presentations](https://www.khronos.org/webgl/wiki/Presentations) - Khronos 提供的各种 WebGL 相关演示的列表。
* [Next-Generation 3D Graphics on the Web](https://www.youtube.com/watch?v=K2JzIUIHIhc) - Ricardo Cabello (MrDoob) 在 Google I/O 19 上的演讲。

### 工具/调试

> 用于开发和调试 WebGL 的工具

* [Khronos Dev Tools](https://github.com/KhronosGroup/WebGLDeveloperTools) - 有用的 WebGL 开发工具，旨在用作 ES6 模块。
* [Spector.js](https://spector.babylonjs.com/) - 用于探索 WebGL 场景并排除故障的不可知 JavaScript 框架。
* [WebGL Inspector](http://benvanik.github.io/WebGL-Inspector/) - 受 gDEBugger 和 PIX 启发的工具，其目标是使高级 WebGL 应用程序的开发变得更容易。
* [WebGl Playground](http://jessevdk.github.io/webgl-play/) - 该编辑器可让您以方便的方式同时处理 JavaScript 代码和 GLSL 顶点/片段着色器（如果有）。一切都按照您的意愿组织、格式化并突出显示。
* [WebGL Report](http://webglreport.com/?v=1) - 查看浏览器对 WebGL 支持的详细信息的方法。
* [WebGL Support Stats](http://webglstats.com/) - 交互式仪表板显示不同浏览器和设备中对 WebGL 功能的支持。
* [WebGL Texture Tester](http://toji.github.io/texture-tester/) - 尝试加载 WebGL 支持的每种纹理格式之一，旨在快速显示您的浏览器/设备支持哪些格式。
* [Web Tracing Framework](http://google.github.io/tracing-framework/index.html) - 用于跟踪和调查复杂 Web 应用程序的库、工具和可视化工具集。

#### Chrome 专用工具/调试器

* [GLSL Shader Editor Extension](https://github.com/spite/ShaderEditorExtension) - Chrome DevTools 扩展可帮助您在浏览器中实时编辑着色器。
* [Spector.js Extension](https://chrome.google.com/webstore/detail/spectorjs/denbgaamihkadbghdceggmchnflmhpmk) - 轻松探索 WebGL 和 WebGL2 场景并排除故障。
* [Webgl Insight](https://github.com/3Dparallax/insight) - Chrome 扩展 WebGL 调试工具包提供多种功能。

#### Firefox 专用工具/调试器

* [Canvas Debugger](https://hacks.mozilla.org/2014/03/introducing-the-canvas-debugger-in-firefox-developer-tools/) - 如何使用 Firefox 的开发人员工具调试 WebGL 着色器的快速教程。
* [Firefox Developer Tools](https://developer.mozilla.org/en-US/docs/Tools) - 所有 Firefox 调试器工具的官方列表。
* [Shader Editor](https://hacks.mozilla.org/2013/11/live-editing-webgl-shaders-with-firefox-developer-tools/) - 如何使用 Firefox 的开发人员工具调试 WebGL 着色器的快速教程。

### 教程

> 在线 WebGL 教程（非视频）

* [Directional Shadow Mapping](http://chinedufn.com/webgl-shadow-mapping-tutorial/) - 实时定向光阴影映射背后的概念。
* [Get Started Tutorial](https://www.khronos.org/webgl/wiki/Tutorial) - Khronos 的教程如何启动并运行 WebGL。
* [Getting Started with WebGL](https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API/Tutorial/Getting_started_with_WebGL) - Mozilla 基金会 WebGL 入门指南。
* [Learn WebGL](https://www.tutorialspoint.com/webgl/index.htm) - 教程 一组让您熟悉 WebGL 术语的文章。
* [Learning WebGL](http://learningwebgl.com/blog/?page_id=1217) - 来自《WebGL Up and Running》作者的教程。
* [Multitexturing using a Blendmap](http://chinedufn.com/webgl-multitexture-blend-map-tutorial/) - 如何使用混合贴图对地形进行多重纹理。
* [Particle Effects via Billboards](http://chinedufn.com/webgl-particle-effect-billboard-tutorial/) - 通过应用称为广告牌的技术来创建粒子效果。
* [The Book of Shaders](https://thebookofshaders.com/) - 温和的分步指导，让您了解片段着色器抽象而复杂的世界。
* [WebGL Academy](http://www.webglacademy.com/) - 简化的在线 IDE，具有自动缩进、HTML、Javascript、GLSL 和 Python 语法突出显示功能。您可以运行代码并下载项目。
* [WebGL Fundamentals](https://webglfundamentals.org/) - 包含代码示例和现场演示的一系列在线教程。
* [WebGL Workshop](http://webgl-workshop.com/) - 交互式研讨会可帮助您启动并运行 WebGL。

### 视频

> WebGL 相关视频

* [An Introduction to WebGL Programming](https://www.youtube.com/watch?v=tgVLb6fOVVc&feature=youtu.be) - SIGGRAPH 大学提供的 3 小时 WebGL 概述。
* [WebGL Tutorials - YouTube](https://www.youtube.com/playlist?list=PLjcVFFANLS5zH_PeKC6I8p0Pt1hzph_rt) - YouTube 上 Indigo Code 的系列讲座式视频教程。

## 网页GL 2

> 有关即将推出的 WebGL 2 规范的信息
>
> 一般与 WebGL 有关的任何内容都可以在 [WebGL](#WebGL) 部分中找到

### WebGL 2 子类别
* [Articles](#articles-1)
* [References](#references-1)
* [Tutorials](#tutorials-1)
* [Videos](#videos-1)

### 文章

> WebGL 2 文章和/或博客文章（非教程）

* [WebGL 2 What's New](https://webgl2fundamentals.org/webgl/lessons/webgl2-whats-new.html) - 查看 WebGL 2 中添加的新功能。
* [What's Coming in WebGL 2.0](https://blog.tojicode.com/2013/09/whats-coming-in-webgl-20.html) - 了解 WebGL 2 即将推出的功能。
* [WebGL 2 SIGGRAPH Asia 2015](https://docs.google.com/presentation/d/1Orx0GB0cQcYhHkYsaEcoo5js3c5-pv7ahPniIRIzzfg/edit#slide=id.p) - 谷歌的 Zenyao Mo 和 Ken Russell 在 SIGGRAPH Asia 2015 期间的演讲。
* [WebGL 2 Lands in Firefox](https://hacks.mozilla.org/2017/01/webgl-2-lands-in-firefox/) - 信息从 Firefox 51 开始支持 WebGL 2。
* [WebGL 2 Basics](http://www.realtimerendering.com/blog/webgl-2-basics/) - 有关 WebGL 2 入门的博客文章。
* [WebGL 2 New Features](http://www.realtimerendering.com/blog/webgl-2-new-features/) - 关于 WebGl 2 中的新增功能和酷炫功能的博客文章。

### 参考文献

> WebGL 2 参考

* [WebGL 2 Spec Sheet (Editor Draft)](https://www.khronos.org/registry/webgl/specs/latest/2.0/) - 有关 WebGL 2 的所有详细信息。
* [WebGL 2 Reference Card](https://www.khronos.org/files/webgl20-reference-guide.pdf) - 用于打印的 WebGL 2.0 API 快速参考卡。
* [WebGL 2 Compatible Chart](https://caniuse.com/#feat=webgl2) - 显示当前支持 WebGL 2 的浏览器的图表

### 教程
* [WebGL 2 Fundamentals](https://webgl2fundamentals.org/) - 包含代码示例和现场演示的一系列在线教程。
* [WebGL 2 Samples](http://webglsamples.org/WebGL2Samples/) - 许多不同的 WebGL 2 作品的重要来源以及非常好的评论。
* [WebGL 2 Examples](https://github.com/tsherif/webgl2examples) - 在原始 WebGL 2 中实现的渲染算法。
* [WebGL 2 & GLSL Primer: A Zero-to-Hero, Spaced-Repetition Guide](https://github.com/GregStanton/webgl2-glsl-primer) - 通过一系列指导课程了解 WebGL2 和 GLSL，每个课程都分为原子问答卡，并集成了实践项目和解决方案代码。

### 视频

> WebGL相关视频

* [Fun with WebGL 2.0](https://www.youtube.com/playlist?list=PLMinhigDWz6emRKVkVIEAaePW7vtIkaIF) - 有关 WebGL 2 入门的视频教程系列，仍在积极添加视频。
* [WebGL 2.0 is Here: What You Need To Know](https://www.youtube.com/watch?v=Xf65duJ_QFs) - Khronos 网络研讨会 2017 年 4 月。
    * [Slides](https://www.khronos.org/assets/uploads/developers/library/2017-webgl-webinar/Khronos-Webinar-WebGL-20-is-here_What-you-need-to-know_Apr17.pdf)

## 网络VR

> 有关新的和即将推出的 WebVR 生态系统不同部分的信息
>
> 所有项目都与更多开发人员相关，而不是与在哪里可以找到作为娱乐的 WebVR 内容相关

### WebVR 子类别

* [Articles](#articles-2)
* [博客系列](#blog-series-1)
* [Platforms](#platforms)
* [References](#references-2)

### 文章

> WebVR 文章和/或博客文章（非教程）

### 博客系列

> 维护 WebVR 重点主题的博客系列

* [Mozilla VR Blog](https://blog.mozvr.com/) - Firefox 制造商专注于 WebVR 的博客。

### 平台

> WebVR设计的体验平台

* [JanusVR](https://janusvr.com/) - 网页作为通过门户互连的协作 3D 网络空间。

### 参考文献

> WebVR 参考资料

* [Browser Support](https://webvr.rocks/) - 显示浏览器、耳机和操作系统的支持。
* [Mozilla VR](https://mixedreality.mozilla.org/) - Mozilla 的官方 WebVR 页面。
* [UX of VR](https://www.uxofvr.com/) - 精选资源列表，帮助在 WebVR 中创建良好的用户体验。
* [WebXR Device API](https://immersive-web.github.io/webxr/) - WebXR 的 W3C API 草案。
* [WebVR Spec](https://w3c.github.io/webvr/) - 官方 W3C WebVR 规范（旧版）。
  * [如何阅读 WebVR 规格](https://dassur.ma/things/reading-specs/)

## 图书馆

> [有关不同库的更多详细信息可以在 Libraries 目录中找到。](https://github.com/sjfricke/awesome-webgl/tree/master/Libraries)

### 二维
* [p2.js](https://github.com/schteppe/p2.js) - 用 JavaScript 编写的 2D 刚体物理引擎。
* [Phaser](https://phaser.io/) - 适用于 Canvas 和 WebGL 的开源 HTML5 2D 游戏框架，支持移动网络浏览器。
* [PixiJS](http://www.pixijs.com/) - 基于 WebGL 的强大 2D Javascript 渲染器。
* [Planck.js](https://github.com/shakiba/planck.js) - 用于跨平台 HTML5 游戏开发的 2D 物理引擎。
* [Stage.js](https://github.com/shakiba/stage.js) - 用于跨平台 HTML5 游戏开发的 2D 库。

### 计算（GPGPU）

#### 计算机视觉
* [GammaCV](https://gammacv.com) - 用于浏览器的 WebGL 加速计算机视觉库。

#### 颗粒
* [Phenomenon](https://github.com/vaneenige/phenomenon) - 非常小的低级 WebGL 库，提供提供高性能体验的要素。

### 地图和可视化
* [Cesium](https://cesiumjs.org/) - 世界级 3D 地球仪和地图的开源库。
* [Deck.gl](http://deck.gl/) - React 的 WebGL 叠加套件提供了一组高性能的数据可视化叠加。
* [Luma.gl](https://luma.gl/) - WebGL2 支持的框架，用于 GPU 驱动的数据可视化和计算。
* [MapMetrics GL](https://github.com/MapMetrics/mapmetrics-gl) - Mapbox GL JS 兼容地图库，具有内置矢量切片、地理编码、路由和搜索。
* [xeokit](https://xeokit.io/) - 适用于 AEC/BIM 应用程序的 Web 图形 SDK，具有 3D 图块、真实世界坐标和双精度。

### 数学
* [glMatrix](http://glmatrix.net/) - 用于高性能 WebGL 应用程序的 Javascript 矩阵和矢量库。
* [Sylvester](http://sylvester.jcoglan.com/) - Sylvester 是一个 JavaScript 向量、矩阵和几何库。
* [TWGL](http://twgljs.org/) - 唯一的目的是让 WebGL API 的使用更加简洁。

### 渲染
* [GLBoost](https://github.com/emadurandal/GLBoost) - 3D 图形极客的渲染库。
* [GrimoireGL](https://grimoire.gl/) - Web 工程师和 CG 工程师之间的桥梁。
* [Hilo3d](https://github.com/hiloteam/Hilo3d) - 用于 3D 游戏的 WebGL 渲染引擎。

### 物理学
* [Ammo.js](https://github.com/kripken/ammo.js/) - 使用 Emscripten 将 Bullet 物理引擎直接移植到 JavaScript。
* [Cannon.js](http://schteppe.github.io/cannon.js/) - 轻量且简单的网络 3D 物理引擎。

### 网页GL 2
* [PicoGL.js](https://tsherif.github.io/picogl.js/) - 最小的仅 WebGL 2 渲染库。

### 网络VR
* [A-Frame](https://aframe.io/) - 用于构建虚拟现实体验的 Web 框架。
  * [Awesome-AFrame](https://github.com/aframevr/awesome-aframe)
* [Hologram](https://hologram.cool/) - 桌面应用程序可让您以交互方式创建 WebVR 并对其进行原型设计，无需具备任何编码知识。
* [LÖVR](https://lovr.org/) - 使用 Lua 创建 VR 的简单框架。
* [React 360](https://facebook.github.io/react-360/) - 使用 React 构建 VR 网站和交互式 360 度体验。
* [Primrose](https://github.com/capnmidnight/Primrose/) - 在浏览器中快速构建 VR 应用程序原型。

### 其他
* [Babylon.js](https://www.babylonjs.com/) - 用于使用 HTML5、WebGL 和 Web Audio 构建 3D 游戏的完整 JavaScript 框架。
* [Blend4Web](https://www.blend4web.com/en/) - Internet 上交互式 3D 可视化工具。
* [ClayGL](http://claygl.xyz/) - 用于构建可扩展的 Web3D 应用程序的 WebGL 图形库。
* [CopperLicht](https://www.ambiera.com/copperlicht/index.html) - 用于创建游戏和 3D 应用程序的 JavaScript 库和 WebGL 3D 引擎。
* [GLGE](http://www.glge.org/) - Javascript 库旨在简化 WebGL 的使用。
* [Lightgl.js](https://github.com/evanw/lightgl.js) - 轻量级且显式的库可帮助原型设计。
* [OSG.js](https://cedricpinson.github.io/osgjs-website/) - 基于 OpenSceneGraph 概念的 WebGL 框架与 WebGL 交互。
* [Pex-gl](http://vorg.github.io/pex/) - Plask/Node.js 和 WebGL 中用于计算思维的 JavaScript 库。
* [PlayCanvas](https://playcanvas.com/) - 构建互动体验的游戏引擎平台。
* [Pocket.gl](https://github.com/gportelli/pocket.gl) - 完全可定制的 webgl 着色器沙箱，可嵌入到您的页面中。
* [Regl](http://regl.party/) - 轻量声明式无状态库，WebGL 的功能抽象。
* [Scene.js](http://scenejs.org/) - 基于 WebGL 的可扩展引擎，用于高细节 3D 可视化。
* [Three.js](https://threejs.org/) - 旨在创建一个易于使用、轻量级的 3D 库。
* [Turbulenz](https://github.com/turbulenz/turbulenz_engine) - 模块化 3D 和 2D 游戏框架，用于为浏览器、桌面和移动设备制作 HTML5 支持的游戏。
* [Verge3D](https://www.soft8soft.com/verge3d/) - 一个艺术家友好的工具包，用于创建 3D Web 体验。
* [Whitestorm.js](https://whs.io/) - 使用物理开发 3D Web 应用程序的框架。

## 社区
* [堆栈溢出](https://stackoverflow.com/questions/tagged/webgl)
* [Reddit](https://www.reddit.com/r/webgl/)
* [Facebook](https://www.facebook.com/groups/webgl/about/)
* [Twitter](https://twitter.com/webgl)
* [自由节点IRC](http://webchat.freenode.net/?channels=webgl)
* [科诺斯论坛](https://community.khronos.org/c/other-standards/webgl)
* [谷歌集团](https://groups.google.com/forum/#!forum/webgl-dev-list)
* [谷歌+](https://plus.google.com/communities/114915309361980512257)
* [公共邮件列表](https://www.khronos.org/webgl/public-mailing-list/)
* [WebVR Slack](http://webvr-slack.herokuapp.com/)
* [WebVR 公共邮件列表](https://lists.w3.org/Archives/Public/public-webvr/)
* 活跃的聚会小组
  * [加利福尼亚州旧金山](https://www.meetup.com/WebGL-Developers-Meetup/)
  * [加利福尼亚州山景城](https://www.meetup.com/Silicon-Valley-HTML5-WebGL-Meetup/)
  * [英国伦敦](https://www.meetup.com/WebGL-Workshop-London/)
  * [纽约州纽约市](https://www.meetup.com/NYC-WebGL-Developers/)

## 相关列表

> 类似的精彩列表

* [awesome](https://github.com/sindresorhus/awesome) - 精选的精彩列表。
* [awesome-opengl](https://github.com/eug/awesome-opengl) - 很棒的 OpenGL 库、调试器和资源的精选列表。灵感来自于很棒的东西。
* [awesome-vulkan](https://github.com/vinjn/awesome-vulkan) - 精彩 Vulkan 项目和生态系统的精选列表。
* [gamedev](https://github.com/ellisonleao/magictools) - 关于游戏开发的精彩列表。
* [glTF](https://github.com/KhronosGroup/glTF) - 专为 Web 设计的运行时 3D 资产交付。
* [graphics-resources](https://github.com/mattdesl/graphics-resources) - 图形编程资源列表。

## 贡献
有关详细信息，请参阅[贡献](https://github.com/sjfricke/awesome-webgl/blob/master/CONTRIBUTING.md)。

## 测试
Travis CI 测试自动化感谢 [awesome_bot](https://github.com/dkhamsing/awesome_bot)！

## 许可证

[![CC0](http://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

在法律允许的范围内，[Spencer Fricke](https://github.com/sjfricke) 已放弃本作品的所有版权以及相关或邻接权。
