# 很棒的opengl [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
[<img src="https://rawgit.com/eug/awesome-opengl/master/opengl-logo.svg"align="right" width="140">](https://www.opengl.org)

精彩的 OpenGL 库、调试器和资源的精选列表。

## 内容

* [Articles](#articles)
* [Books](#books)
* [Debug](#debug)
* [GLSL 编辑](#glsl-editors)
* [Libraries](#libraries)
* [型材装载机](#profile-loaders)
* [References](#references)
* [Talks](#talks)
* [Videos](#videos)
* [Websites](#websites)


## 文章

*OpenGL 文章（非教程）*

* [(2014) 使用 OpenGL 计算着色器进行光线追踪](https://github.com/LWJGL/lwjgl3-wiki/wiki/2.6.1.-Ray-tracing-with-OpenGL-Compute-Shaders-%28Part-I%29) 作者：**Kai Burjack** - 有关使用 OpenGL (LWJGL) 光线追踪的详细教程系列。
* [(2014) 让我对 OpenGL 感到疯狂的事情](http://richg42.blogspot.com.au/2014/05/things-that-drive-me-nuts-about-opengl.html) 作者：Rich Geldreich** - 对 GL API 的建设性（或非建设性）批评。
* [(2011) 图形管道之旅](https://fgiesen.wordpress.com/2011/07/09/a-trip-through-the-graphics-pipeline-2011-index) 作者：Fabian Giesen** - 关于 D3D/OpenGL 图形管道的全面而丰富的系列。
* [(2010) 什么是 OpenGL？](http://duriansoftware.com/joe/An-intro-to-modern-OpenGL.-Chapter-1:-The-Graphics-Pipeline.html) 作者：**Joe Groff** - 简要介绍 OpenGL 的构建块。


## 书籍

*有关 OpenGL 的热门书籍*

* [图形管道之旅](http://www.amazon.com/dp/1558603875)，作者：**Jim Blinn** - 一本热门书籍，包含有关图形管道的丰富信息，以及学习计算机图形学核心概念的最佳来源。
* [计算机图形学](http://www.amazon.com/dp/0321399528) 作者：**John F. Hughes 等人** - 计算机图形学确实是任何参与计算机图形学算法设计和实现的人的必备知识。然而，这不是一本专注于 OpenGL 的书，但包含了该技术的有价值的演示。
* [交互式计算机图形](http://www.amazon.com/dp/0132545233) 作者：Edward Angel 和 Dave Shreiner** - 它提供了几个使用 OpenGL 的示例，并且同时涵盖了多个方面，但如果您尝试自己学习 OpenGL，您可能会发现这没有帮助。
* [OpenGL ES 3.0 编程指南](http://www.amazon.com/dp/0321933885) 作者：**Dan Ginsburg 等人** - 它以清晰的方式呈现了使用 OpenGL ES 3.0 API 的所有必要信息。
* [OpenGL Insights](http://www.amazon.com/dp/1439893764) 作者：**Patrick Cozzi、Christophe Riccio** - 用于学习技术和技巧的丰富而全面的资源，涵盖 OpenGL 的多个高级主题。
* [OpenGL 编程指南](http://www.amazon.com/dp/0321773039)，作者：**Dave Shreiner 等人** - 它很好地涵盖了基础知识并提供了 API 的清晰参考。
* [OpenGL 着色语言](http://www.amazon.com/dp/0321637631) 作者：Randi J. Rost 等人** - 关于着色语言的非常清晰且写得很好的书。此外，它还提供了编写着色器的几种解释。
* [OpenGL SuperBible](http://www.amazon.com/dp/0321712617) 作者：Richard S. Wright 等人** - 它涵盖了计算机图形学的基本概念，并提供了使用 OpenGL 的清晰示例。毫无疑问，这是初学者的必备品。
* [实时渲染](http://www.amazon.com/dp/1568814240)，作者：**Tomas Akenine-Moller、Eric Haines 和 Naty Hoffman** - 它很好地解释了游戏引擎的概念、游戏客户端编程的基础以及理解 DirectX 和 OpenGL 的必要知识。


## 调试

*调试和分析库*

* [apitrace](http://apitrace.github.io) - 用于跟踪 OpenGL、Direct3D 和其他图形 API 的工具。
* [CodeXL](https://github.com/GPUOpen-Tools/CodeXL) - AMD 的工具套件包括调试器、分析器和帧/着色器分析。
* [GL-SL Debugger](http://glsl-debugger.github.io) - 用于调试 OpenGL 程序的工具。
* [GLIntercept](https://github.com/dtrebilco/glintercept) - Windows 的 OpenGL 函数调用拦截器。
* [Intel-GPA](https://software.intel.com/en-us/gpa) - 英特尔的 OpenGL 图形性能分析器。
* [NVIDIA® Nsight™](https://developer.nvidia.com/nvidia-nsight-visual-studio-edition) - 图形应用程序的开发平台。
* [RenderDoc](https://github.com/baldurk/renderdoc) - RenderDoc 是一个独立的图形调试工具。
* [tracy](https://github.com/wolfpld/tracy) - 适用于游戏和其他应用程序的实时远程遥测帧分析器。
* [vogl](https://github.com/ValveSoftware/vogl) - Valve 开发的 OpenGL 捕获和回放调试器。


## GLSL 编辑

*在线 GLSL 编辑器*

* [GLSL Sandbox](http://glslsandbox.com) - 片段着色器的在线实时编辑器。
* [GLSLbin](http://glslb.in) - 支持 [glslify](https://github.com/stackgl/glslify) 的片段着色器沙箱。
* [SHDR Editor](http://shdr.bkcore.com) - 实时 GLSL 着色器编辑器、查看器和验证器。
* [Shader Toy](https://www.shadertoy.com) - 最受欢迎的片段着色器实时编辑器。
* [ShaderFrog](http://shaderfrog.com/) - WebGL 着色器编辑器和合成器

## 图书馆

*适用于 OpenGL 应用程序的有用库*

* [assimp](https://github.com/assimp/assimp) - 用于以统一方式导入 3D 模型的便携式库。
* [Bullet](http://bulletphysics.org/wordpress) - 它提供最先进的碰撞检测、软体和刚体动力学。
* [fltk](https://www.fltk.org/) - 用于生成可移植 UI 小部件的 C++ 工具包。 [LGPLv2](https://www.fltk.org/COPYING.php)
* [freeGLUT](http://freeglut.sourceforge.net) - 成熟的库，允许创建/管理包含 OpenGL 上下文的窗口。
* [GLFW](http://www.glfw.org) - 用于创建窗口/与 OpenGL 上下文交互的现代库。
* [GLFM](https://github.com/brackeen/glfm) - 为移动设备和网络提供 OpenGL ES 上下文和输入事件。
* [glm](http://glm.g-truc.net/0.9.6/index.html) - 基于 GLSL 规范的图形软件数学库。
* [Magnum](https://github.com/mosra/magnum) - 它是现代 OpenGL 的 2D/3D 图形引擎。
* [MathFu](http://google.github.io/mathfu/) - 主要为注重简单性和效率的游戏开发的 C++ 数学库。
* [Newton](http://newtondynamics.com/forum/newton.php) - 这是一个跨平台的逼真物理。
* [OGLplus](http://oglplus.org) - 通过 OpenGL 实现面向对象外观的库集合。
* [SDL](http://www.libsdl.org) - 旨在提供对多媒体和图形硬件的低级访问。
* [SFML](http://www.sfml-dev.org) - 简单的界面可轻松开发游戏和多媒体应用程序。
* [SOIL](http://www.lonesock.net/soil.html) - 小型 C 库，主要用于将纹理上传到 OpenGL。 （参见 [SOIL2](https://bitbucket.org/SpartanJ/soil2)）
* [Pangolin](https://github.com/stevenlovegrove/Pangolin) - 用于管理 OpenGL 显示/交互和抽象视频输入的轻量级便携式快速开发库。
* [morphologica](https://github.com/ABRG-Models/morphologica) - 用于数据可视化的 OpenGL 图形引擎，尤其是数值模拟。
* [raylib](https://github.com/raysan5/raylib) - 一个简单易用的库，可让您享受视频游戏编程的乐趣。

## 型材装载机

*OpenGL 的配置文件加载器*

* [gl3w](https://github.com/skaslev/gl3w) - 简单的 OpenGL 核心配置文件加载器。
* [glad](https://github.com/Dav1dde/glad) - 基于官方规格的多配置文件加载生成器。
* [glbindify](https://github.com/nnesse/glbindify) - 用于生成 OpenGL、wgl 和 glX 的 C 绑定的命令行工具。
* [glbinding](https://github.com/cginternals/glbinding) - 配置文件加载器利用 C++11 功能来提供类型安全。
* [GLEW](http://glew.sourceforge.net) - 成熟的跨平台库来加载 OpenGL 扩展。


## 参考文献

*OpenGL参考*

* [docs.GL](http://docs.gl) - 它是 OpenGL 的替代文档。
* [OpenGL API Tables](http://web.eecs.umich.edu/~sugih/courses/eecs487/common/notes/APITables.xml) - 多个 OpenGL 和 GLSL 版本的 API 的快速参考。
* [OpenGL Cheat Sheet](https://www.khronos.org/files/opengl43-quick-reference-card.pdf) - OpenGL 4.3 命令和语法的快速参考卡。
* [OpenGL Docs](https://www.opengl.org/sdk/docs) - 官方文档网站。
* [OpenGL Wiki](https://www.opengl.org/wiki/Main_Page) - 官方 OpenGL 维基。


## 会谈

*OpenGL相关讲座*
* [Approaching Zero Driver Overhead in OpenGL](http://gdcvault.com/play/1020791/) - [幻灯片](http://www.slideshare.net/CassEveritt/approaching-zero-driver-overhead) - [AMA Reddit](https://www.reddit.com/r/gamedev/comments/21mbo8/we_are_the_authors_of_approaching_zero_driver) 作者：**Cass Everitt、Tim Foley、John McDonald、Graham Sellers** [1:15:54]
* [现代 OpenGL 如何从根本上减少驱动程序开销](https://www.youtube.com/watch?v=-bCeNzgiJ8I) 作者：**Cass Everitt、John McDonald** [51:13]
* [将您的游戏移至 OpenGL](https://www.youtube.com/watch?v=45O7WTc6k2Y) 作者：**Rich Geldreich、Dan Ginsburg、Peter Lohrmann、Jason Mitchell** [54:45]


## 视频

*OpenGL视频教程*

* [Jamie King](https://www.youtube.com/playlist?list=PLRwVmtr-pp06qT6ckboaOhnm9FxmzHpbY) - 有关现代 OpenGL 和 Qt 的综合教程。
* [MakingGamesWithBen](https://www.youtube.com/playlist?list=PLSPw4ASQYyymu3PfG9gxywSPghnSMiOAW) - 有关 OpenGL 和游戏开发的视频教程（分步）。
* [SIGGRAPH](https://www.youtube.com/user/ACMSIGGRAPH/playlists) - 关于计算机图形学的热门会议。
* [TheChernoProject](https://www.youtube.com/playlist?list=PLlrATfBNZ98foTJPJ_Ev03o2oq3-GGOS2) - C++ OpenGL 简介
* [thebennybox](https://www.youtube.com/user/thebennybox/playlists) - 有关 OpenGL 和游戏开发的视频教程。
* [ThinMatrix](https://www.youtube.com/user/ThinMatrix/playlists) - 有关 OpenGL 和使用 Java 进行游戏开发的视频教程。
* [sentdex](https://www.youtube.com/playlist?list=PLQVvvaa0QuDdfGpqjkEJSeWKGCP31__wD) - 有关使用 Python 的 OpenGL（立即模式）的视频教程。
* [Sonar Systems](https://www.youtube.com/playlist?list=PLRtjMdoYXLf6zUMDJVRZYV-6g6n62vet8) - 了解全新、现代的 OpenGL 3.0+。
* [Introduction to OpenGL](https://www.youtube.com/playlist?list=PLvv0ScY6vfd9zlZkIIqGDeG5TUWswkMox) - Mike Shah 提供的关于 C++ OpenGL 的视频教程。

## 网站

*OpenGL教程网站*

* [初学者 3D 游戏着色器](https://github.com/lettier/3d-game-shaders-for-beginners) 作者：**David Lettier**
* [学习 OpenGL](https://learnopengl.com) 作者：**Joey de Vries**
* [学习现代 3D 图形编程](https://bitbucket.org/alfonse/gltut/wiki/Home) 作者：**Jason L. McKesson**
* [灯塔 3D](http://www.lighthouse3d.com/tutorials/glsl-core-tutorial) 作者：**灯塔 3D**
* [现代 OpenGL](http://www.tomdalling.com/blog/category/modern-opengl) 作者：**Tom Dalling**
* [OpenGL 示例](https://github.com/McNopper/OpenGL) 作者：**Norbert Nopper**
* [OpenGL 一步一步](http://ogldev.atspace.co.uk) 作者：**Etay Meiri**
* [OpenGL 教程](https://open.gl) 作者：**Alexander Overvoorde**
* [OpenGL 教程](http://antongerdelan.net/opengl/index.html) 作者：**Anton Gerdelan**
* [OpenGL 教程](http://www.opengl-tutorial.org) 作者：**Bonder Wu**
* [OpenGL 教程](http://www.songho.ca/opengl) 作者：**Song Ho Ahn**

## 相关列表

*类似的精彩列表*
* [awesome](https://github.com/sindresorhus/awesome) - 精选的精彩清单。
* [awesome-computer-vision](https://github.com/jbhuang0604/awesome-computer-vision) - 精彩计算机视觉资源的精选列表。
* [awesome-webgl](https://github.com/sjfricke/awesome-webgl) - 精彩 WebGL 库、资源等的精选列表。
* [awesome-vulkan](https://github.com/vinjn/awesome-vulkan) - 精彩 Vulkan 项目和生态系统的精选列表。
* [gamedev](https://github.com/ellisonleao/magictools) - 关于游戏开发的精彩列表。
* [graphics-resources](https://github.com/mattdesl/graphics-resources) - 图形编程资源列表。


## 许可证

[![Creative Commons License](http://i.creativecommons.org/l/by/4.0/88x31.png)](http://creativecommons.org/licenses/by/4.0/)

本作品根据 [知识共享署名 4.0 国际许可证](http://creativecommons.org/licenses/by/4.0/) 获得许可。

## 贡献
有关详细信息，请参阅[贡献](https://github.com/eug/awesome-opengl/blob/master/CONTRIBUTING.md)。
