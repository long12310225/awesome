# 很棒的 Vulkan [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

<img src="https://raw.githubusercontent.com/SaschaWillems/Vulkan/master/images/vulkanlogoscene.png" alt="Vulkan demo scene" height="256px">

很棒的 Vulkan 库、调试器和资源的精选列表。受到 [awesome-opengl](https://github.com/eug/awesome-opengl) 和其他很棒的东西的启发。

* **[硬件支持](#hardware-support)**
* **[SDK](#sdk)**
* **[IHV 文档](#document)**
* **[教程](#tutorial)**
* **[应用程序](#apps)**
* **[样本](#样本)**
* **[库](#libraries)**
* **[绑定](#绑定)**
* **[工具](#tools)**
* **[书籍](#书籍)**
* **[论文](#论文)**
* **[科罗诺斯](#khronos)**
* **[社区](#community)**

## 硬件支持
* [gpuinfo](http://vulkan.gpuinfo.org/) - Vulkan 硬件数据库，作者：Sascha Willems
*  [Khronos](https://www.khronos.org/vulkan)
*  [NVIDIA](https://developer.nvidia.com/Vulkan)
    * [桌面版驱动程序](https://developer.nvidia.com/vulkan-driver)
    * [安卓驱动程序](https://developer.nvidia.com/vulkan-android)
    * [Tegra (L4T) Linux 驱动程序](https://developer.nvidia.com/embedded/vulkan)
*  [AMD](http://www.amd.com/en-gb/innovations/software-technologies/technologies-gaming/vulkan)
    * [开源驱动程序](https://github.com/GPUOpen-Drivers/AMDVLK)
*  [Imagination](https://www.imgtec.com/developers/powervr-sdk-tools/)
* 英特尔
    * [开源驱动程序](https://01.org/linuxgraphics/blogs/jekstrand/2016/open-source-vulkan-drivers-intel-hardware/)
    * [Windows 驱动程序](https://software.intel.com/en-us/blogs/2016/03/14/new-intel-vulkan-beta-1540204404-graphics-driver-for-windows-78110-1540)
*  [Qualcomm](https://developer.qualcomm.com/software/adreno-gpu-sdk/gpu)
* 手臂
    * [Mali GPU 最佳实践](https://developer.arm.com/solutions/graphics/developer-guides/mali-gpu-best-practices)

## 软件开发工具包
* [适用于 Windows 和 Linux](https://vulkan.lunarg.com/signin)
* [对于安卓](https://developer.android.com/ndk/guides/graphics/index.html)

## 文件
*  [AMD](http://gpuopen.com/tag/vulkan/)
    * [Vulkan 障碍解释](http://gpuopen.com/vulkan-barriers-explained/)
    * [Vulkan 快速路径](https://gpuopen.com/wp-content/uploads/2016/03/VulkanFastPaths.pdf)
    * [让您的游戏大放异彩 - 使用 AMD CodeXL 优化 DirectX 12 和 Vulkan 性能	](https://gpuopen.com/wp-content/uploads/2016/03/Let_your_game_shine_optimizing_DirectX-12_and_Vulkan-performance_with_AMD_CodeXL.pdf)
    * [D3D12 和 Vulkan：经验教训	 ](https://gpuopen.com/wp-content/uploads/2016/03/d3d12_vulkan_lessons_learned.pdf)
    * [向镇上的新渲染 API 问好！](http://gpuopen.com/say-hello/)
    * [Vulkan 渲染通道](http://gpuopen.com/vulkan-renderpasses/)
    * [性能推文系列：障碍、栅栏、同步](http://gpuopen.com/performance-tweets-series-barriers-fences-synchronization/)
    * [使用 Vulkan™ 验证层](http://gpuopen.com/using-the-vulkan-validation-layers/)
    * [Vulkan 应用程序中最常见的错误](https://gpuopen.com/wp-content/uploads/2016/05/Most-common-mistakes-in-Vulkan-apps.pdf)
	* [Vulkan 设备内存](http://gpuopen.com/vulkan-device-memory/)
*  [NVIDIA](https://developer.nvidia.com/taxonomy/term/586)
    * [Vulkan 设备生成的命令](https://developer.nvidia.com/device-generated-commands-vulkan)
    * [让 Vulkan 为 VR 做好准备](https://developer.nvidia.com/getting-vulkan-ready-vr)
    * [GPU 驱动渲染](http://on-demand.gputechconf.com/gtc/2016/presentation/s6138-christoph-kubisch-pierre-boudier-gpu-driven-rendering.pdf)
    * [GDC 16 - 使用 OpenGL 和 Vulkan 进行高性能、低开销渲染](http://developer.download.nvidia.com/gameworks/events/GDC2016/mschott_lbishop_gl_vulkan.pdf)
    * [GDC 16 - Vulkan 和 NVIDIA - 要点](http://developer.download.nvidia.com/gameworks/events/GDC2016/Vulkan_Essentials_GDC16_tlorach.pdf)
    * [踏上前往伏尔甘 (Vulkan) 的旅程](https://developer.nvidia.com/engaging-voyage-vulkan)
    * [Vulkan 着色器资源绑定](https://developer.nvidia.com/vulkan-shader-resource-binding)
    * [Vulkan 内存管理](https://developer.nvidia.com/vulkan-memory-management)
    * [类似于 Vulkan 的 OpenGL](https://developer.nvidia.com/opengl-vulkan)
    * [从 OpenGL 过渡到 Vulkan](https://developer.nvidia.com/transitioning-opengl-vulkan)
    * [Siggraph 15 演讲 - NVIDIA GPU 上的 Vulkan](http://on-demand.gputechconf.com/siggraph/2015/presentation/SIG1501-Piers-Daniell.pdf)
*  [Arm](https://developer.arm.com/solutions/graphics/apis/vulkan)
    * [移动开发者 Vulkan 最佳实践教程](https://github.com/ARM-software/vulkan_best_practice_for_mobile_developers)
    * [Vulkan 在 Arm 架构上的主要特性](https://developer.arm.com/-/media/Files/pdf/graphics-and-multimedia/Vulkan%20API%20key%20features%20on%20ARM%20architecture.pdf)
    * [将图形引擎移植到 Vulkan API](https://community.arm.com/groups/arm-mali-graphics/blog/2016/02/16/porting-a-graphics-engine-to-the-vulkan-api)
    * [让您的引擎为移动设备上的 Vulkan 做好准备](https://developer.arm.com/-/media/Files/pdf/graphics-and-multimedia/Get%20Your%20Engine%20Ready%20for%20Vulkan%20on%20Mobile.pdf)
    * [Vulkan 中的多线程](https://community.arm.com/groups/arm-mali-graphics/blog/2016/04/19/massively-multi-thread-for-vulkan)
* [Mali Vulkan SDK 教程](https://developer.arm.com/products/software/mali-sdks/vulkan) 和 [幻灯片](https://developer.arm.com/graphics/vulkan/vulkan-tutorials)
* 英特尔
* [没有秘密的 API：Vulkan 简介](https://github.com/GameTechDev/IntroductionToVulkan) [[许可证](https://github.com/GameTechDev/IntroductionToVulkan/blob/master/license.txt)]
        * [第 1 部分：开始](https://software.intel.com/en-us/api-without-secrets-introduction-to-vulkan-part-1)
        * [第 2 部分：交换链](https://software.intel.com/en-us/api-without-secrets-introduction-to-vulkan-part-2)
        * [第 3 部分：第一个三角形](https://software.intel.com/en-us/api-without-secrets-introduction-to-vulkan-part-3)
        * [第 4 部分：顶点属性](https://software.intel.com/en-us/articles/api-without-secrets-introduction-to-vulkan-part-4)
* [Imagination](http://blog.imgtec.com/tag/vulkan)
    * [在 PowerVR 上使用 Vulkan 进行高效渲染](https://imagination-technologies-cloudfront-assets.s3.amazonaws.com/idc-docs/gdc16/6_Efficient%20rendering%20with%20Vulkan%20on%20PowerVR.pdf)
    * [使用新的 PowerVR 图形框架迁移到 Vulkan](https://www.imgtec.com/webinar/migrating-to-vulkan-with-the-powervr-framework/)
    * [从 OpenGLES 迁移到 Vulkan](https://www.imgtec.com/downloads/download-info/migrating-from-opengl-es-to-vulkan/)
* 三星
    * [Siggraph 2016 - 移动设备最佳实践](https://community.arm.com/cfs-file/__key/telligent-evolution-extensions-calendar-calendarfiles/00-00-00-00-05/2_2D00_mmg_2D00_siggraph2016_2D00_best_2D00_practice_2D00_andrew.pdf)
* [Vulkan 使用推荐](https://developer.samsung.com/game/usage)（适用于移动设备）
* 史诗
    * [UE4 Mobile 上高效使用 Vulkan](https://community.arm.com/cfs-file/__key/telligent-evolution-extensions-calendar-calendarfiles/00-00-00-00-05/6_2D00_mmg_2D00_siggraph2016_2D00_vulkan_2D00_smedis.pdf)
*科罗诺斯
   * [Vulkan 指南](https://github.com/KhronosGroup/Vulkan-Guide)
* [LunarG](https://lunarg.com)
    * [Vulkan SDK](https://vulkan.lunarg.com/)
    * [Vulkan SDK 版本兼容性](https://www.lunarg.com/news-insights/white-papers/vulkan-sdk-version-compatibility/)
    * [推出新的 Vulkan 配置器](https://www.lunarg.com/news-insights/white-papers/vulkan-validation-layers/)
    * [Vulkan 的统一验证层](https://www.lunarg.com/news-insights/white-papers/unified-validation-layer-for-vulkan/)
    * [Vulkan 同步验证快速入门指南](https://www.lunarg.com/news-insights/white-papers/vulkan-synchronization-validation-quick-start-guide/)
    * [Vulkan 同步验证指南](https://www.lunarg.com/news-insights/white-papers/guide-to-vulkan-synchronization-validation/)
    * [Vulkan GPU 辅助验证](https://www.lunarg.com/news-insights/white-papers/vulkan-gpu-assisted-validation/)
    * [Spirv-Opt 中的自动 RelaxedPrecision 装饰和转换](https://www.lunarg.com/news-insights/white-papers/automatic-relaxedprecision-decoration-and-conversion-in-spirv-opt/)
    * [使用spirv-opt 进行 SPIR-V 合法化和尺寸减小](https://www.lunarg.com/news-insights/white-papers/spir-v-legalization-and-size-reduction-with-spirv-opt/)
    * [所有白皮书](https://www.lunarg.com/vulkan-white-papers/)
* 社区
    * [VulkanHub](https://vkdoc.net) 

## 教程
* [How to Learn Vulkan](https://www.jeremyong.com/c++/vulkan/graphics/rendering/2018/03/26/how-to-learn-vulkan.html) - 关于如何学习 Vulkan 的元帖子
* [I Am Graphics And So Can You](https://www.fasterthan.life/blog/2017/7/11/i-am-graphics-and-so-can-you-part-1) - 博客文章风格的教程，适合图形学习 Vulkan 的新手。
* [Vulkan Game Engine Tutorial](https://www.youtube.com/watch?v=Y9U9IE0gVHA) - Brendan Galea 在 YouTube 上制作 vulkan 游戏引擎的教程系列。
* [Kohi Game Engine Series](https://www.youtube.com/watch?v=dHPuU-DJoBM&list=PLv8Ddw9K0JPg1BEO-RS-0MYs423cvLVtj) - “Vulkan 游戏引擎系列，我们使用 C 和 Vulkan 从头开始​​制作游戏引擎”。
* [迁移到 Vulkan（Khronos UK 5 月 16 日）](https://www.khronos.org/assets/uploads/developers/library/2016-uk-chapter-moving-to-vulkan/Moving-to-Vulkan_Khronos-UK_May16.pdf)
* [jhenriques 的教程](http://jhenriques.net/development.html)
* [卢纳格的教程](https://vulkan.lunarg.com/doc/sdk/1.0.26.0/windows/tutorial.html)
* [Mike Bailey's Vulkan Page](http://web.engr.oregonstate.edu/~mjb/vulkan/) - 提供丰富的 Vulkan 课程幻灯片。 [CC BY-NC-ND 4.0]
* [Qualcomm Video Tutorial Series](https://developer.qualcomm.com/software/adreno-gpu-sdk/tutorial-videos) - 更倾向于移动设备上的 Vulkan。
* [Raw Vulkan](https://alain.xyz/blog/raw-vulkan) - 概述如何从头开始编写 Vulkan 应用程序。
* 符号图
    * [An overview of next-generation graphics APIs](http://nextgenapis.realtimerendering.com/) - 涵盖Vulkan、D3D12等。
* [Overv 教程](https://vulkan-tutorial.com/) 和 [其 github 存储库](https://github.com/Overv/VulkanTutorial)。 [CC BY-SA 4.0]
* [vulkan-sxs](https://github.com/philiptaylor/vulkan-sxs) - 逐步解释 Vulkan API 和 [vulkan-sync](https://github.com/philiptaylor/vulkan-sync) - 以更精确的形式重新表述 Vulkan 对执行依赖项的要求。 [麻省理工学院]
* [Vulkan in 30 minutes](https://renderdoc.org/vulkan-in-30-minutes.html) - 由博杜克。
* [Vulkan 演示和教程](https://github.com/Z80Fan/VulkanDemos)。 [麻省理工学院]
* [Vulkan 指南](https://vkguide.dev)。 [麻省理工学院]
* [Vulkan Lecture Series](https://www.youtube.com/playlist?list=PLmIqTlJ6KsE1Jx5HV4sd2jOe3V1KMHHgn) - 由维也纳工业大学计算机图形学研究室的 Johannes Unterguggenberger 进行的大学讲座。涵盖基本和高级主题，例如：Vulkan 基础知识、交换链、资源和描述符、命令和命令缓冲区、管道和阶段、实时光线追踪和同步。

## 应用程序
* [The Talos Principle](http://www.croteam.com/talos-principle-will-support-vulkan-first-screenshot-released/) - 由克罗团队。
* [Dota2](https://github.com/ValveSoftware/Dota-2-Vulkan/) - 由阀门。
* [Basemark](https://www.basemark.com/blog/basemark-extends-its-benchmarking-lead-with-a-vulkan-performance-test/) - 由 Basemark 提供。
* [GFXBench 5](https://kishonti.net/news_single.jsp?id=31133884) - 基肖蒂.
* [ProtoStar](https://www.unrealengine.com/blog/epic-games-unveils-protostar-at-samsung-galaxy-unpacked) - 由 Epic 开发，采用虚幻引擎 4 技术构建。
* [DDraceNetwork](https://github.com/ddnet/ddnet/) - 具有可选 [Vulkan 后端](https://github.com/ddnet/ddnet/blob/master/src/engine/client/backend/vulkan/backend_vulkan.cpp) 的协作 2D 平台游戏。 - [zlib](https://github.com/ddnet/ddnet/blob/master/license.txt) [网站](https://ddnet.tw/)
* [Doom](https://en.wikipedia.org/wiki/Doom_(2016_video_game)) - 由 id Software 制作。
* [vkQuake](https://github.com/Novum/vkQuake) - 基于 QuakeSpasm 的 Vulkan Quake 端口。 [通用公共许可证]
* [vkQuake2](https://github.com/kondrak/vkQuake2) - id Software 的 Quake 2 v3.21 支持 Vulkan（Windows 和 Linux）。 [通用公共许可证]
* [q2vkpt](https://github.com/cschied/q2vkpt/) - 实时路径追踪器 VKPT 集成到 q2pro Quake 2 客户端中。 [通用公共许可证]
* [Linux port of SteamVR](https://github.com/ValveSoftware/SteamVR-for-Linux) - SteamVR 构建在 Vulkan API 之上。
* [3DMark](https://www.futuremark.com/pressreleases/compare-vulkan-and-directx-12-performance-with-3dmark) - 3DMark API 开销测试。
* [Q2RTX](https://github.com/NVIDIA/Q2RTX) - NVIDIA 在 Quake II 中实现 RTX 光线追踪。 [[许可证](https://github.com/NVIDIA/Q2RTX/blob/master/license.txt)]

## 样品
* Khronos [Vulkan 示例](https://github.com/KhronosGroup/Vulkan-Samples) [[许可证](https://github.com/KhronosGroup/Vulkan-Samples/blob/master/LICENSE)]
* Sascha Willems 的 [样本](https://github.com/SaschaWillems/Vulkan) 和 [Sponza 的延迟渲染](https://github.com/SaschaWillems/VulkanSponza) 以及他的演讲[Khronos_meetup_munich](https://www.saschawillems.de/blog/2016/04/11/khronos-chapter-munich-vulkan-slides/)。
*（不完整）Sascha Willems 的 [示例端口](https://github.com/jvm-graphics-labs/Vulkan) 到 Kotlin
* Sascha Willems 的 [Vulkan-glTF-PBR](https://github.com/SaschaWillems/Vulkan-glTF-PBR) - 使用 glTF 2.0 模型通过 Vulkan 进行基于物理的渲染。 [麻省理工学院]
* [移动开发人员的 Vulkan 最佳实践示例](https://github.com/ARM-software/vulkan_best_practice_for_mobile_developers)
* 谷歌
* [LunarG 示例的 Android 端口](https://github.com/googlesamples/vulkan-basic-samples)。
* [android 教程](https://github.com/googlesamples/android-vulkan-tutorials)。
* [nvpro-samples](https://github.com/nvpro-samples) - NVIDIA DesignWorks 示例。 [[许可证](https://github.com/nvpro-samples/gl_vk_threaded_cadscene/blob/master/LICENSE)]
    * [gl_vk_chopper](https://github.com/nvpro-samples/gl_vk_chopper) - 简单的 vulkan 渲染示例。
    * [gl_vk_threaded_cadscene](https://github.com/nvpro-samples/gl_vk_threaded_cadscene) - 使用各种技术渲染 CAD 场景的 OpenGL 和 Vulkan 比较以及相关的[博客](https://developer.nvidia.com/vulkan-opengl-threaded-cad-scene-sample)。
    * [gl_vk_bk3dthreaded](https://github.com/nvpro-samples/gl_vk_bk3dthreaded) - 使用“工作线程”进行 3D 渲染的 Vulkan 示例。
    * [gl_vk_supersampled](https://github.com/nvpro-samples/gl_vk_supersampled) - Vulkan 示例显示了高质量的超级采样渲染。
* [NVIDIA GameWorks Samples](https://github.com/NVIDIAGameWorks/GraphicsSamples) - GameWorks 跨平台图形 API 示例。 [[许可证](https://github.com/NVIDIAGameWorks/GraphicsSamples/blob/master/license.txt)]
* [LunarG 的样本](https://github.com/LunarG/VulkanSamples)
* [vkcube](https://github.com/krh/vkcube) - 来自 krh 的“vkcube”示例，在 X、wayland 和 VT 控制台下工作
DRM/公里。
* [Stardust from Intel](https://github.com/GameTechDev/stardust_vulkan) - Stardust 示例应用程序使用 Vulkan 图形 API 来高效渲染动画粒子云。 [[许可证](https://github.com/GameTechDev/stardust_vulkan/blob/master/license.txt)]
* [基于 QuakeSpasm 的 Vulkan Quake 端口](https://github.com/Novum/vkQuake)。
* [C# Samples](https://github.com/FacticiusVir/SharpVk-Samples) - Overv 的教程移植到 [SharpVk](https://github.com/FacticiusVir/SharpVk) [MIT]
* [Vulkan-Forward-Plus-Renderer](https://github.com/WindyDarian/Vulkan-Forward-Plus-Renderer) - VFPR - Vulkan Forward Plus 渲染器。 [麻省理工学院]
* [Laugh Engine](https://github.com/jian-ru/laugh_engine) - 实时 PBR 渲染器的 Vulkan 实现。
* [tinyrenderers](https://github.com/chaoticbob/tinyrenderers) - Vulkan 和 D3D12 渲染器的单标头实现。
* [TLVulkanRenderer](https://github.com/trungtle/TLVulkanRenderer) - 我关于实时透明度的硕士论文的简单的基于 Vulkan 的渲染器。 [CC BY-SA 4.0]
* [Vulkan-Hpp Samples](https://github.com/jherico/Vulkan) - Sascha Willems 的 Fork 使用 Vulkan-Hpp 的优秀 Vulkan 示例。
* [SDF Font Demo](https://github.com/kocsis1david/font-demo) - 通过估计符号距离在 Vulkan 中渲染文本。 [麻省理工学院]
* [vulkantoy](https://github.com/jpystynen/vulkantoy) - 使用 Vulkan 的 Shadertoy 图像着色器测试应用程序。 [麻省理工学院]
* [GL_vs_VK](https://github.com/RippeR37/GL_vs_VK) - OpenGL 和 Vulkan API 在性能方面的比较。 [麻省理工学院]
* [Vulkan Basic Graphics Samples](https://github.com/vcoda/basic-graphics-samples) - 使用 Magma 库编写的简单图形示例集合。
* [简单 RTX Vulkan 光线追踪教程](https://github.com/iOrange/rtxON)。 [麻省理工学院]
* [Ray Tracing In One Weekend (Vulkan RTX)](https://github.com/GPSnoopy/RayTracingInVulkan) - 使用 Vulkan 和 NVIDIA 的 RTX 扩展实现 Peter Shirley 的《One Weekend 光线追踪》一书。
* [Gears VK](https://github.com/jeffboody/gearsvk) - Gears VK 是著名的“gears”演示到 Vulkan/Android/Linux 的重大修改端口。 [麻省理工学院]
* [Hello triangle，](https://github.com/maierfelix/VK_KHR_ray_tracing) 基于 Vulkan 光线追踪扩展。 [麻省理工学院]
* [Simple Animation Blender](https://github.com/Red1C3/Simple-Animation-Blender) - 实时 1D 动画混合器和播放器，使用 Vulkan 作为图形后端，使用 ImGui 作为 GUI。 [麻省理工学院]

## 图书馆
* 2D
   * [imgui](https://github.com/ocornut/imgui) - 立即模式图形用户界面。 [麻省理工学院]
   * [Skia](https://skia.googlesource.com/skia) - Google 的 2D 图形库有一个 [Vulkan](https://skia.org/user/special/vulkan) [后端](https://github.com/google/skia/tree/master/src/gpu/vk)，在跨平台[示例应用程序](https://skia.org/user/sample/viewer) 及其自己的[窗口库](https://github.com/google/skia/tree/master/tools/viewer) 中进行了演示。 [BSD 3 条款] [网站](https://skia.org)
   * [VKVG](https://github.com/jpbruyere/vkvg) - Vulkan 2D 图形库，API 遵循与 Cairo 图形库相同的模式，但具有新功能。

* 计算
   * [libvc](https://github.com/alexhultman/libvc) - 用于 C++ 的 Vulkan 计算。  [[许可证](https://github.com/alexhultman/libvc/blob/master/LICENSE)]
   * [Vulkan Kompute](https://github.com/axsaucedo/vulkan-kompute) - 速度极快且轻量级的 Vulkan 计算框架针对高级 GPU 处理用例进行了优化。 [阿帕奇许可证2.0]
   * [ncnn](https://github.com/Tencent/ncnn) - 具有基于 Vulkan 的 GPU 推理的高性能神经网络推理框架。 [BSD 3 条款]
   * [vuh](https://github.com/Glavnokoman/vuh) - 基于Vulkan的C++ GPGPU计算框架。 [麻省理工学院]
   * [VkFFT](https://github.com/DTolm/VkFFT) - 高效的 Vulkan FFT 库 [MPL-2.0 许可证]

* 低水平
   * [Vulkan Memory Allocator](https://github.com/GPUOpen-LibrariesAndSDKs/VulkanMemoryAllocator) - 易于集成 AMD 的 Vulkan 内存分配库。 [麻省理工学院]
* [VulkanMemoryAllocator-Hpp] (https://github.com/malte-v/VulkanMemoryAllocator-Hpp) - VMA 的 C++ 绑定，如 Vulkan-HPP
   * [Fossilize](https://github.com/Themaister/Fossilize) - 各种持久性 Vulkan 对象类型的序列化格式。 [麻省理工学院]
   * [vk-bootstrap](https://github.com/charles-lunarg/vk-bootstrap) - C++ 实用程序库可通过自动创建实例、物理设备、设备和交换链来快速启动 Vulkan 开发。 [麻省理工学院]
   * [Google's vulkan-cpp-library](https://github.com/google/vulkan-cpp-library) - 使用 C++11 的 Vulkan 抽象库实现内存、资源管理、类型和线程安全以及系统独立性。 [阿帕奇]
   * [FrameGraph](https://github.com/azhirnov/FrameGraph) - 将框架表示为任务图的 Vulkan 抽象层。 [BSD 2 条款]
   * [V-EZ](https://github.com/GPUOpen-LibrariesAndSDKs/V-EZ) - 针对专业工作站 ISV 的 Vulkan API 的轻量级中间件层。 [麻省理工学院]
   * [Vookoo](https://github.com/andy-thomason/Vookoo) - Vookoo 是一组无依赖实用程序，用于协助构建和更新 Vulkan 图形数据结构。 [麻省理工学院]
   * [vpp](https://github.com/nyorain/vpp) - 现代 C++ Vulkan 抽象注重性能和简单的界面。 [麻省理工学院]
   * [VulkanSceneGraph](https://github.com/vsg-dev) - Vulkan/C++17 场景图项目，[OpenSceneGraph](http://www.openscenegraph.org) 的继承者。
   * [Vulkan-WSIWindow](https://github.com/renelindsay/Vulkan-WSIWindow) - 用于创建 Vulkan 窗口并处理输入事件的多平台库。 [阿帕奇许可证2.0]
   * [Screen 13](https://github.com/attackgoat/screen-13) - 易于使用的 Rust Vulkan 渲染图。 [麻省理工学院]

* 框架、引擎、高级渲染
   * [Acid](https://github.com/Equilibrium-Games/Acid) - 高速 C++17 Vulkan 游戏引擎。 [麻省理工学院]
   * [AMD's Anvil](https://github.com/GPUOpen-LibrariesAndSDKs/Anvil) - Vulkan 的跨平台框架。 [[许可证](https://github.com/GPUOpen-LibrariesAndSDKs/Anvil/blob/master/LICENSE.txt)]
   * [Auto-Vk](https://github.com/cg-tuwien/Auto-Vk) - 现代 C++ 的 Vulkan 便利性和生产力层，位于 Vulkan-Hpp 之上，由维也纳工业大学计算机图形学研究单位开发。 [麻省理工学院]
   * [Auto-Vk-Toolkit](https://github.com/cg-tuwien/Auto-Vk-Toolkit) - 围绕 [Auto-Vk](https://github.com/cg-tuwien/Auto-Vk) 的 C++ 框架，用于快速原型设计、研究和教学，由维也纳工业大学计算机图形学研究单位开发。 [MIT 框架代码]
   * [bgfx](https://github.com/bkaradzic/bgfx#bgfx---cross-platform-rendering-library) - 跨平台、与图形 API 无关的“自带引擎/框架”风格渲染库。 [[BSD-2-clause](https://github.com/bkaradzic/bgfx/blob/master/LICENSE)]
   * [bsf](https://github.com/GameFoundry/bsf) - 用于开发实时图形应用程序的现代 C++14 库。 [麻省理工学院]
* [Cinder](https://github.com/cinder/Cinder) 和[故事](https://libcinder.org/notes/vulkan) [背后](https://forum.libcinder.org/#Topic/23286000002614007)。 [BSD]
   * [DemoFramework](https://github.com/NXPmicro/gtec-demo-framework) - NXP GTEC C++11 跨平台演示框架，包括 Vulkan、OpenGL ES、OpenVX、OpenCL、OpenVG 和 OpenCV 的大量示例。 [[BSD-3-clause](https://github.com/NXPmicro/gtec-demo-framework/blob/master/License.md)]
   * [Diligent Engine](https://github.com/DiligentGraphics/DiligentEngine) - 一个现代跨平台低级图形库，支持 OpenGL/GLES、Direct3D11/12 和 Vulkan。 [阿帕奇许可证2.0]
   * [Falcor](https://github.com/NVIDIAGameWorks/Falcor) - 来自 NVIDIA 的实时渲染框架，主要支持 DX12，并有实验性的 Vulkan 支持。 [BSD 3 条款]
* [glfw](https://github.com/glfw/glfw) 和 [指南](http://www.glfw.org/docs/3.2/vulkan.html)。  [[许可证](https://github.com/glfw/glfw/blob/master/LICENSE.md)]
   * [Intrinsic Engine](https://github.com/begla/Intrinsic) - Intrinsic 是一个基于 Vulkan 的跨平台图形和游戏引擎。 [阿帕奇许可证2.0]
* [GPUOpen 的介绍性 Vulkan 示例](https://github.com/GPUOpen-LibrariesAndSDKs/HelloVulkan)。 [麻省理工学院]
   * [liblava](https://github.com/liblava/liblava) - 现代 C++ 且易于使用的框架。 [麻省理工学院]
   * [Logi](https://github.com/UL-FRI-LGM/Logi) - 轻量级面向对象的 Vulkan 抽象框架。 [BSD 2 条款]
   * [Lugdunum](https://github.com/Lugdunum3D/Lugdunum) - 使用 Vulkan 和现代 C++14 构建的现代跨平台 3D 渲染引擎。 [麻省理工学院]
   * [Nabla](https://github.com/Devsh-Graphics-Programming/Nabla) - 适用于 PC/Linux/Android 的 Vulkan、OptiX 和 CUDA 互操作模块化渲染库和框架。 [阿帕奇许可证2.0]
   * [openFrameworks](https://github.com/openframeworks-vk/openFrameworks) - 最著名的 C++ 创意编码框架。 [麻省理工学院]
   * [PowerVR SDK](https://github.com/powervr-graphics/Native_SDK) - C++ 跨平台 3D 图形 SDK，可加速 Vulkan 和 GLES 的开发。 [[许可证](https://github.com/powervr-graphics/Native_SDK/blob/4.1/LICENSE_POWERVR_SDK.txt)]
   * [Pumex](https://github.com/pumexx/pumex) - 跨平台 Vulkan 渲染器实现帧图和简单场景图。能够同时在多个表面上渲染 [MIT]
   * [SDL](https://discourse.libsdl.org/t/sdl-2-0-6-released/23109) - 在 SDL_vulkan.h 中添加了跨平台 Vulkan 图形支持。 [zlib]
* [small3d](https://www.gamedev.net/projects/515-small3d/)，基于Tiny Vulkan的C++跨平台游戏开发框架[BSD 3-clause]
   * [Spectrum](https://github.com/mwalczyk/spectrum_core) - 围绕 Vulkan 的正在进行的框架和抽象层。
   * [Tephra](https://github.com/Dolkar/Tephra) - 现代 C++17 图形和计算库填补了 Vulkan 和 OpenGL 等高级 API 之间的空白。 [麻省理工学院]
   * [The-Forge](https://github.com/ConfettiFX/The-Forge) - DirectX 12、Vulkan、macOS Metal 2 渲染框架。 [阿帕奇许可证2.0]
   * [VKFS](https://github.com/MHDtA-dev/VKFS) - 跨平台易于使用的C++框架，可让您快速初始化Vulkan并获得现成的环境。提供基本 Vulkan 对象的高级抽象。
   * [Vulkan Launchpad](https://github.com/cg-tuwien/VulkanLaunchpad) - 适用于 Windows、macOS 和 Linux 的 Vulkan 框架。特别适合 Vulkan 初学者，由维也纳工业大学计算机图形学研究单位在大学教育中使用。 [麻省理工学院]
       * [Vulkan Launchpad Starter](https://github.com/cg-tuwien/VulkanLaunchpadStarter) - 包含附加功能和资产的入门模板。 [[许可证]](https://github.com/cg-tuwien/VulkanLaunchpadStarter/blob/main/LICENSE)

* 其他API互操作和实现
   * [visor](https://github.com/baldurk/visor) - Vulkan Ignoble 软件光栅化器。 [麻省理工学院]
   * [VulkanOnD3D12](https://github.com/Chabloom/VulkanOnD3D12) - 适用于 D3D12 的 Vulkan API。 [阿帕奇许可证2.0]
   * [rostkatze](https://github.com/msiglreith/rostkatze) - Vulkan 位于 D3D12 上的 C++ 实现 🐈[Apache License 2.0]
   * [VK9](https://github.com/disks86/VK9) - 使用 Vulkan 的 Direct3D 9 兼容层
   * [VUDA](https://github.com/jgbit/vuda) - 提供 CUDA 运行时 API 接口的纯头文件库。 [麻省理工学院]
   * [clspv](https://github.com/google/clspv) - OpenCL C 到 Vulkan 计算着色器子集的原型编译器。 [阿帕奇许可证2.0]
   * [MoltenVK](https://github.com/KhronosGroup/MoltenVK/) - 在 iOS 和 macOS 上运行 Vulkan。 [阿帕奇-2.0]
   * [Zink](https://gitlab.freedesktop.org/kusma/mesa/tree/zink) - Vulkan 之上的 OpenGL 实现，是 Mesa 项目的一部分。 [麻省理工学院]
   * [glo / OpenGL Overload](https://github.com/g-truc/glo) - Vulkan 之上的 OpenGL 实现。
   * [gfx-portability](https://github.com/gfx-rs/portability) - 基于 [gfx-rs](https://github.com/gfx-rs/gfx/) 在 Metal 和 D3D12 上实现 Vulkan 可移植性。

* 光线追踪
   * [Quartz](https://github.com/Nadrin/Quartz) - 基于物理的 Vulkan RTX 路径追踪器，具有类似 ES7 的声明性场景描述语言。 [LGPL-3.0]

* 科学的
   * [datoviz](https://github.com/datoviz/datoviz) - 使用 Vulkan 实现高性能 GPU 交互式科学数据可视化。 [麻省理工学院]
   * [iMSTK](https://gitlab.kitware.com/iMSTK/iMSTK) - 用于使用 Vulkan 和 VTK 后端构建手术模拟的 C++ 工具包。 [阿帕奇许可证2.0]
  
* 着色器
   * [glslang](https://github.com/KhronosGroup/glslang) - 用于将 glsl 编译为spirv 的库 [BSD 3-Clause]
   * [SPIRV-Cross](https://github.com/KhronosGroup/SPIRV-Cross) - 用于spirv反射的库，简化Vulkan管道布局的创建[Apache-2.0许可证]

* 已过时⚠️
   * [VkHLF](https://github.com/nvpro-pipeline/VkHLF) - Vulkan 高级框架。 [[许可证]](https://github.com/nvpro-pipeline/VkHLF/blob/master/LICENSE.txt)

## 绑定
* [ash](https://github.com/MaikKlein/ash) - Rust 的 Vulkan 绑定。 [麻省理工学院]
* [gfx-rs](https://github.com/gfx-rs/gfx) - 适用于 Rust 的低开销、类似 Vulkan 的 GPU API。 [阿帕奇许可证2.0]
* [libvulkan.lua](https://github.com/CapsAdmin/ffibuild/blob/master/vulkan/vulkan.lua) - Vulkan 的 Lua 绑定。
* [dvulkan](https://github.com/ColonelThirtyTwo/dvulkan) - 自动生成 Vulkan 的 D 绑定。
* [ErupteD](https://github.com/ParticlePeter/ErupteD) - 另一个为 Vulkan 自动生成的 D 绑定。
* [flextGL](https://github.com/mosra/flextgl) - 最小的 Vulkan header/loader 生成器和关于它的[博客文章](http://blog.magnum.graphics/hacking/simple-efficient-vulkan-loading-with-flextgl/)。
* [Silk.NET](https://github.com/dotnet/Silk.NET) - Vulkan 等的 C# 绑定。 [麻省理工学院]
* [vulkan](https://github.com/expipiplus1/vulkan) - Vulkan 和 Vulkan 内存分配器的 Haskell 绑定 [BSD-3-Clause]
* [nvk](https://github.com/maierfelix/nvk) - Vulkan 的 JavaScript 绑定。 [麻省理工学院]
* [racket-vulkan](https://github.com/zyrolasting/racket-vulkan) - Vulkan 的 Racket 绑定以及[详细实施说明](https://sagegerard.com/racket-vulkan-notes-index.html)。 [麻省理工学院]
* [Vulkan-hpp](https://github.com/KhronosGroup/Vulkan-Hpp) 开源 Vulkan C++ API 源自 NVIDIA 以及有关它的[博客](https://developer.nvidia.com/open-source-vulkan-c-api)。
* [VulkanSharp](https://github.com/mono/VulkanSharp) - Vulkan 的 C# 绑定。 [麻省理工学院]
* [Vulkano](https://github.com/vulkano-rs/vulkano) - Vulkan API 周围安全且丰富的 Rust 包装器。 [麻省理工学院]
* [LWJGL](https://www.lwjgl.org/) - 轻量级 Java 游戏库 3 具有 Vulkan 绑定。 [BSD]
* [SharpVk](https://github.com/FacticiusVir/SharpVk) - Vulkan 与 Linq-to-SPIR-V 和 [NuGet 包](https://www.nuget.org/packages/SharpVk) 的 C# 绑定。 [麻省理工学院]
* [vulkan](https://github.com/realitix/vulkan) - 使用 CFFI 生成的 Vulkan 的终极 Python 绑定。 [阿帕奇许可证2.0]
* [vulkan-go](https://github.com/vulkan-go/vulkan) - Go 绑定 Vulkan。 [麻省理工学院]
* [PasVulkan](https://github.com/BeRo1985/pasvulkan) - Vulkan 绑定以及 Object Pascal 的高级包装器库 [Zlib]
* [vulkan-zig](https://github.com/Snektron/vulkan-zig) - Zig 的 Vulkan 绑定生成器 [MIT]
* [VK²](https://github.com/kotlin-graphics/vkk)，Vulkan 的 Kotlin 包装器：代码表现力和安全性满足图形功能 [Apache 许可证 2.0]
* [Vortice.Vulkan](https://github.com/amerkoleci/Vortice.Vulkan) - .NET Standard 2.0 和 .NET5 C# 绑定 [MIT]
* [Raw Node.js Vulkan API](https://github.com/hydra2s/node-vulkan-api) - Node.JS 的新 Vulkan 绑定，与 LWJGL-3 或 NVK 类似。
* [Deno Vulkan](https://github.com/deno-windowing/vulkan) - Deno 的 Vulkan API 绑定。 [阿帕奇许可证2.0]

## 工具
* [Nsight™ Visual Studio 版本 5.2+](https://developer.nvidia.com/nvidia-nsight-visual-studio-edition)。
* [LoaderAndValidationLayers](https://github.com/KhronosGroup/Vulkan-LoaderAndValidationLayers) - 来自 KhronosGroup。 [阿帕奇许可证2.0]
* [renderdoc](https://github.com/baldurk/renderdoc) - 由 baldurk 开发，一个独立的图形调试工具。 [麻省理工学院]
    * [RDCtoVkCpp](https://github.com/azhirnov/RDCtoVkCpp) - 将 RenderDoc Vulkan 捕获转换为可编译且可执行的 C++ 代码。 [麻省理工学院]
* [VulkanTools](https://github.com/LunarG/VulkanTools) - LunarG 的工具包括图层和配置器。 [阿帕奇许可证2.0]
* [VKtracer](https://www.vktracer.com) - 适用于 Vulkan 的通用且易于使用的分析器。
* [CodeXL](https://github.com/GPUOpen-Tools/CodeXL) - CodeXL 开源。 [麻省理工学院]
* [Qualcomm Adreno GPU Tools](https://developer.qualcomm.com/software/adreno-gpu-sdk/tools) - 示例、Adreno 推荐层、Adreno GPU 最佳实践文档。
* [Qualcomm Snapdragon Profiler](https://developer.qualcomm.com/software/snapdragon-profiler) - 包括 Adreno GPU 的 Vulkan 跟踪和帧捕获。
* [Arm Mobile Studio](https://www.arm.com/products/development-tools/graphics/arm-mobile-studio) - 包括可轻松跟踪图形性能问题的 Arm 图形分析器和可提供全系统性能视图的 Arm Streamline 性能分析器，以快速确定 CPU 和 GPU 的瓶颈。
* [Open Capture and Analytics Tool (OCAT)](https://github.com/GPUOpen-Tools/OCAT) - 为 D3D11、D3D12 和 Vulkan 提供 FPS 叠加和性能测量。 [麻省理工学院]
* [gapid](https://github.com/google/gapid) - 图形 API 调试器，可以跟踪和重放 Android OpenGL ES 和 Vulkan 应用程序。 [阿帕奇许可证2.0]
* [Arm - PerfDoc](https://github.com/ARM-software/perfdoc) - 针对马里应用程序开发人员最佳实践文档的验证层。 [麻省理工学院]
* [glsl_trace](https://github.com/azhirnov/glsl_trace) - 用于 Vulkan 和 OpenGL 着色器调试和分析的库。 [麻省理工学院]
* [MangoHud](https://github.com/flightlessmango/MangoHud) - Vulkan 和 OpenGL 叠加用于监控 FPS、温度、CPU/GPU 负载。 [麻省理工学院]

## 书籍
* [计算机图形学和 Vulkan API 简介](https://www.amazon.com/Introduction-Computer-Graphics-Vulkan-API/dp/1548616176) 作者：**Kenwright** - 使用 Vulkan API 从基础实用角度向读者介绍令人兴奋的计算机图形学主题。
* [Learning Vulkan](https://www.amazon.com/Learning-Vulkan-Parminder-Singh/dp/1786469804) - 作者：**Parminder Singh** - 使用易于理解的示例开始使用 Vulkan API 及其编程技术。
  * [书中的例子](https://github.com/PacktPublishing/Learning-Vulkan)
* [Vulkan Cookbook](https://www.amazon.com/Vulkan-Cookbook-Pawel-Lapinski/dp/1786468158) - 作者：**Pawel Lapinski** - 探索广泛的图形编程和 GPU 计算方法，以充分利用 Vulkan API。
  * [书中的例子](https://github.com/PacktPublishing/Vulkan-Cookbook)
* [Vulkan Programming Guide](https://www.amazon.com/Vulkan-Programming-Guide-Official-Learning/dp/0134464540) - 作者：**Graham Sellers** 和 **John Kessenich** - 为许多领域引入了强大的 3D 开发技术。
* [Mastering Graphics Programming with Vulkan](https://www.amazon.com/Mastering-Graphics-Programming-Vulkan-state/dp/1803244798/ref=sr_1_1?keywords=mastering+graphics+programming+with+vulkan&qid=1678290788&sprefix=mastering+graphics+%2Caps%2C255&sr=8-1) - 由 **Marco Castorina** 和 **Gabriel Sassone** 开发现代渲染引擎，从基本原理到最先进的技术。

## 论文
* [通往 Vulkan 之路：在图形入门课程中教授现代低级 API](https://www.cg.tuwien.ac.at/research/publications/2022/unterguggenberger-2022-vulkan)，作者：**Johannes Unterguggenberger**、**Bernhard Kerbl** 和 **Michael Wimmer**，Eurographics 2022 - 教育论文
* 直接链接到[论文](https://www.cg.tuwien.ac.at/research/publications/2022/unterguggenberger-2022-vulkan/unterguggenberger-2022-vulkan-paper.pdf)。
* [YouTube](https://youtu.be/ZG0ct4V6c0k) 上预先录制的演示文稿。

## 科罗诺斯
* 规格
* Vulkan 1.0 核心 API ([分块 HTML](https://registry.khronos.org/vulkan/specs/1.0/html/index.html)) ([PDF](https://registry.khronos.org/vulkan/specs/1.0/pdf/vkspec.pdf)) ([单文件HTML](https://registry.khronos.org/vulkan/specs/1.0/html/vkspec.html))
* Vulkan 1.0 核心 API + Khronos 定义的扩展 ([分块 HTML](https://registry.khronos.org/vulkan/specs/1.0-wsi_extensions/html/index.html)) ([PDF](https://registry.khronos.org/vulkan/specs/1.0-wsi_extensions/pdf/vkspec.pdf)) ([单个文件HTML](https://registry.khronos.org/vulkan/specs/1.0-wsi_extensions/html/vkspec.html))
* Vulkan 1.0 核心 API + 所有注册扩展 ([分块 HTML](https://registry.khronos.org/vulkan/specs/1.0-extensions/html/index.html)) ([PDF](https://registry.khronos.org/vulkan/specs/1.0-extensions/pdf/vkspec.pdf)) ([单文件HTML](https://registry.khronos.org/vulkan/specs/1.0-extensions/html/vkspec.html))
* Vulkan 1.1 核心 API ([分块 HTML](https://registry.khronos.org/vulkan/specs/1.1/html/index.html)) ([PDF](https://registry.khronos.org/vulkan/specs/1.1/pdf/vkspec.pdf)) ([单文件HTML](https://registry.khronos.org/vulkan/specs/1.1/html/vkspec.html))
* Vulkan 1.1 核心 API + Khronos 定义的扩展 ([分块 HTML](https://registry.khronos.org/vulkan/specs/1.1-khr-extensions/html/index.html)) ([PDF](https://registry.khronos.org/vulkan/specs/1.1-khr-extensions/pdf/vkspec.pdf)) ([单个文件HTML](https://registry.khronos.org/vulkan/specs/1.1-khr-extensions/html/vkspec.html))
* Vulkan 1.1 核心 API + 所有注册扩展 ([Chunked HTML](https://registry.khronos.org/vulkan/specs/1.1-extensions/html/index.html)) ([PDF](https://registry.khronos.org/vulkan/specs/1.1-extensions/pdf/vkspec.pdf)) ([单文件HTML](https://registry.khronos.org/vulkan/specs/1.1-extensions/html/vkspec.html))
* Vulkan 1.2 核心 API ([分块 HTML](https://registry.khronos.org/vulkan/specs/1.2/html/index.html)) ([PDF](https://registry.khronos.org/vulkan/specs/1.2/pdf/vkspec.pdf)) ([单文件HTML](https://registry.khronos.org/vulkan/specs/1.2/html/vkspec.html))
* Vulkan 1.2 核心 API + Khronos 定义的扩展 ([分块 HTML](https://registry.khronos.org/vulkan/specs/1.2-khr-extensions/html/index.html)) ([PDF](https://registry.khronos.org/vulkan/specs/1.2-khr-extensions/pdf/vkspec.pdf)) ([单个文件HTML](https://registry.khronos.org/vulkan/specs/1.2-khr-extensions/html/vkspec.html))
* Vulkan 1.2 核心 API + 所有注册扩展 ([Chunked HTML](https://registry.khronos.org/vulkan/specs/1.2-extensions/html/index.html)) ([PDF](https://registry.khronos.org/vulkan/specs/1.2-extensions/pdf/vkspec.pdf)) ([单文件HTML](https://registry.khronos.org/vulkan/specs/1.2-extensions/html/vkspec.html))
* Vulkan 1.3 核心 API ([分块 HTML](https://registry.khronos.org/vulkan/specs/1.3/html/index.html)) ([PDF](https://registry.khronos.org/vulkan/specs/1.3/pdf/vkspec.pdf)) ([单文件HTML](https://registry.khronos.org/vulkan/specs/1.3/html/vkspec.html))
* Vulkan 1.3 核心 API + Khronos 定义的扩展 ([分块 HTML](https://registry.khronos.org/vulkan/specs/1.3-khr-extensions/html/index.html)) ([PDF](https://registry.khronos.org/vulkan/specs/1.3-khr-extensions/pdf/vkspec.pdf)) ([单个文件HTML](https://registry.khronos.org/vulkan/specs/1.3-khr-extensions/html/vkspec.html))
* Vulkan 1.3 核心 API + 所有注册扩展 ([Chunked HTML](https://registry.khronos.org/vulkan/specs/1.3-extensions/html/index.html)) ([PDF](https://registry.khronos.org/vulkan/specs/1.3-extensions/pdf/vkspec.pdf)) ([单文件HTML](https://registry.khronos.org/vulkan/specs/1.3-extensions/html/vkspec.html))
* 快速参考表
    * [Vulkan 1.0 快速参考表](https://www.khronos.org/registry/vulkan/specs/1.0/refguide/Vulkan-1.0-web.pdf)
    * [Vulkan 1.1 快速参考表](https://www.khronos.org/registry/vulkan/specs/1.1/refguide/Vulkan-1.1-web.pdf)
* [一致性测试 (CTS)](https://github.com/KhronosGroup/Vulkan-CTS)
* 会议和演讲
    * [GDC 2016 演示](https://www.khronos.org/developers/library/2016-gdc)
    * [2016 年英国分会：转向 Vulkan](https://www.khronos.org/developers/library/2016-uk-chapter-moving-to-vulkan)
    * [SIGGRAPH 2016 BOF - Vulkan](https://www.youtube.com/watch?v=CsHMiEQgrLA)
    * [SIGGRPAH 2016 最佳实践圆桌会议](https://www.youtube.com/watch?v=owuJRPKIUAg)
    * [2016 年英国 Vulkan 开发日](https://www.khronos.org/developers/library/2016-vulkan-devday-uk)
    * [2016 Vulkan DevDay 首尔](https://www.khronos.org/developers/library/2016-Vulkan-DevU-Seoul)
    * [2017 Vulkan DevU 温哥华](https://www.khronos.org/developers/library/2017-vulkan-devu-vancouver)
    * [2017 年 Vulkan 加载器网络研讨会](https://www.khronos.org/developers/library/2017-vulkan-loader-webinar)
    * [SIGGRAPH 2017 BOF - Vulkan](https://www.youtube.com/watch?v=Nx0u-9ZwrmQ)
    * [2018 Vulkan 蒙特利尔开发日](https://www.khronos.org/developers/library/2018-vulkan-montreal-dev-day)
    * [2018 硫化！](https://www.khronos.org/developers/library/2018-vulkanised)
    * [SIGGRAPH 2018 BOF - Vulkan](https://www.youtube.com/watch?v=FCAM-3aAzXg&t=18350s)

## 社区
* [自由节点IRC](http://webchat.freenode.net/?channels=Vulkan)
* [谷歌+](https://plus.google.com/communities/108983304183191634377)
* [科诺斯论坛](https://forums.khronos.org/forumdisplay.php/114-Vulkan)
*  [Reddit](https://www.reddit.com/r/vulkan/)
* [堆栈溢出](http://stackoverflow.com/questions/tagged/vulkan)
*  [Discord](https://discord.com/invite/tFdvbEj)

## 相关列表
* [awesome](https://github.com/sindresorhus/awesome) - 精选的精彩列表。
* [awesome-opengl](https://github.com/eug/awesome-opengl) - 很棒的 OpenGL 库、调试器和资源的精选列表。
* [gamedev](https://github.com/ellisonleao/magictools) - 关于游戏开发的精彩列表。
* [graphics-resources](https://github.com/mattdesl/graphics-resources) - 图形编程资源列表。
* [awesome-d3d12](https://github.com/vinjn/awesome-d3d12) - 精彩 D3D12 库、调试器和资源的精选列表。

## 许可证

[![Creative Commons License](http://i.creativecommons.org/l/by/4.0/88x31.png)](http://creativecommons.org/licenses/by/4.0/)

本作品根据 [知识共享署名 4.0 国际许可证](http://creativecommons.org/licenses/by/4.0/) 获得许可。

## 贡献
有关详细信息，请参阅[贡献](https://github.com/vinjn/awesome-vulkan/blob/master/CONTRIBUTING.md)。
