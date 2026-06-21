[<img src="https://rawgit.com/hgupta9/awesome-actionscript3/master/AS3_AIR.png"align="right"width="150">](https://www.adobe.com/products/air.html)

# 很棒的 ActionScript 3 [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

> ActionScript 3 和 Adobe AIR 的精彩库和组件的精选列表。

[Adobe AIR](https://en.wikipedia.org/wiki/Adobe_AIR) 提供一组 API 来构建跨平台桌面/移动应用程序和游戏。 [ActionScript 3](https://en.wikipedia.org/wiki/ActionScript) 是 AIR 的编程语言。默认情况下包含强大的本机功能，例如文件系统、SQLite、传感器。要添加缺失的功能，您可以构建以本机语言编码的 ANE（Air Native Extensions）（例如，适用于 Windows 的 VC++、适用于 Android 的 Java、适用于 iOS 的 Swift/Objective-C）。要使用 GPU 渲染图形构建移动应用/游戏，请使用 [Starling](https://gamua.com/starling/) 框架和可选的 [Feathers UI](https://feathersui.com/)。 Adobe AIR 在移动游戏领域非常受欢迎。

欢迎贡献。要添加有用的项目，只需创建一个[问题](https://github.com/hgupta9/awesome-actionscript3/issues)。

## 内容

* [开发工具](#development-tools)
* [Frameworks](#frameworks)
* [用户界面](#user-interface)
* [Multimedia](#multimedia)
* [Database](#database)
* [文件格式](#file-formats)
* [Networking](#networking)
* [Utilities](#utilities)
* [Runtimes](#runtimes)
* [AIR 本机扩展](#air-native-extensions)
	

## 开发工具
*本部分包括商业工具以及免费/开源工具。*

#### 代码编辑器
* [FlashDevelop](http://flashdevelop.org/) - 适用于 AS3 和 AIR 的首屈一指的免费开源 IDE，具有代码完成、调试等功能。
* [Powerflasher FDT](http://fdt.powerflasher.com/) - 构建在 Eclipse 平台上的商业 IDE，用于开发 Adob​​e Flash/AIR 内容。
* [Adobe Flash Builder](https://www.adobe.com/products/flash-builder.html) - 用于在 Flex 框架上构建应用程序的商业 IDE（带有高级调试工具）。
* [Moonshine IDE](http://moonshine-ide.com/) - Moonshine 是一款免费开源中量级 IDE，使用 ActionScript 3 构建，适用于 ActionScript 3、Apache Flex®、Apache FlexJS® 和 Feathers 开发，并支持云和桌面。
* [IntelliJ IDEA](https://www.jetbrains.com/help/idea/building-actionscript-and-flex-applications.html) - 支持多种不同语言（包括 AS3）的商业 IDE。
* [Visual Studio Code](https://as3mxml.com/) - Visual Studio Code 的 AS3 和 MXML 语言扩展。在 Windows、macOS 和 Linux 上运行。

#### 实时调试器
* [Adobe Scout](https://www.adobe.com/products/scout.html) - 适用于 AIR 应用程序和游戏的高级视觉分析和调试工具（支持 Stage3D）。
* [De-Monster Debugger](https://github.com/MrTact/monsterdebugger) - 用于调试实时 AIR 应用程序中的图形和数据的高级工具。
* [De-Monster Debugger (Starling)](https://github.com/joshtynjala/monsterdebugger-client-starling) - De-Monster 调试器的分支，支持 Starling 框架。

#### 资产创造者
* [Adobe Animate CC](https://www.adobe.com/products/animate.html) - 用于创建矢量/精灵表的首映矢量图形和动画工具集。
* [TILED Map Editor](http://www.mapeditor.org/) - 灵活的瓦片地图编辑器，兼容各种 AS3 游戏引擎。
* [FlashMovieClipConverter](https://github.com/zenrobin/FlashMovieClipConverter) - 将 Flash MovieClip 转换为 Starling IAnimatable Sprite。

#### SWF 混淆器
* [secureSWF](http://www.kindi.com/) - 商业 AS3/AIR 混淆器，具有重命名、资产加密和自动代码优化功能。
* [irrFuscator](http://www.ambiera.com/irrfuscator/) - 用于 Flash 和 Flex SWF 文件的商业 AS3 混淆器。

#### SWF检查员
* [SWFWire](https://github.com/magicalhobo/SWFWire) - 高级 SWF 反编译器、检查器和调试器工具（[网站](http://www.swfwire.com/)）。
* [Velocity9](https://github.com/velocity9/Inspector) - 基本 SWF 检查器。

#### SWF 反编译器
* [AS3Sorcerer](http://www.as3sorcerer.com/) - Premiere AS3 反编译器，反编译精度为 99%（支持 SWF/SWC、Alchemy 操作码）。
* [Sothink Decompiler](http://www.sothink.com/product/flashdecompiler/) - AS2/AS3 的高级反编译器（支持 SWF 到 FLA/Flex 的资产提取和转换）。

#### ANE 开发工具
* [FreSharp](https://github.com/tuarua/FreSharp) - 使用 C# 以及 FlashRuntimeExtensions 的此 C# 包装器构建 ANE。
* [Swift-IOS-ANE](https://github.com/tuarua/Swift-IOS-ANE) - 使用 Swift 3 编写的适用于 iOS 10 的 ANE 入门套件。

## 框架
#### MVC框架

* [PureMVC](https://github.com/PureMVC/puremvc-as3-standard-framework) - Flash 的行业标准 MVC 框架（[多核](https://github.com/PureMVC/puremvc-as3-multicore-framework)）。
* [Robotlegs](https://github.com/robotlegs/robotlegs-framework) - Flash 的依赖注入、模块/视图/命令管理框架。
* [Hummingbird](https://github.com/flashapi/hummingbird) - 为 AS3、Mobile 和 Starling Framework 构建和部署强大的 MVC 应用程序。
* [Apollo](https://github.com/LaurentZuijdwijk/Apollo) - 依赖注入和消息传递框架，可以作为MVC项目的基础。
* [Somacore](https://github.com/soundstep/somacore_framework) - 基于事件的轻量级 AS3 MVC 框架。
* [Kote](https://github.com/whitered/Kote) - 快速、轻量级的 MVC 框架，汇集了 PureMVC 和 as3-signal 的优点。
* [StarlingMVC](https://github.com/CreativeBottle/starlingMVC) - 基于 Starling 的游戏的 IOC 框架。

#### 用户界面框架

* [Starling](https://gamua.com/starling/) - 基于 Stage3D 构建的高性能 2D 图形引擎。 API 与 Flash API 相同。 （[github]（https://github.com/Gamua/Starling-Framework），[帮助]（http://wiki.starling-framework.org/start））。
* [Feathers UI](https://feathersui.com/) - Starling Framework 的用户界面组件（[github](https://github.com/BowlerHatLLC/feathers)、[help](https://feathersui.com/help/index.html)）。
* [Flow](https://github.com/artman/Flow) - 使用布局、效果、数据绑定和远程处理框架来代替 Flex。
* [AS3Commons UI](https://github.com/AS3Commons/as3commons-ui) - 布局、焦点和键盘管理框架。
* [Swiz](https://github.com/swiz/swiz-framework) - 用于使用 AS3 和 Adob​​e Flex 创建 RIA 的极其简单的微架构。
* [Hiddenwood](https://github.com/raweden/Project-Hiddenwood) - 为 Web 应用程序项目开发的用户界面库，以 AS3 和 MVC 模式编写。
* [Elastic-Lists](https://github.com/MoritzStefaner/Elastic-Lists) - 流畅且强大的界面，用于分面浏览。
* [Apache Flex®](https://flex.apache.org/) - Apache Flex® SDK 是流行的 Adob​​e Flex SDK 的演变。 Apache Flex® SDK 是一个应用程序开发框架，可轻松为移动设备、Web 浏览器和桌面平台构建基于 Flash 的应用程序。
* [Apache Royale®](http://royale.apache.org/) - Apache Royale® 项目正在开发下一代 Apache Flex® SDK。 Royale 的目标是让用 MXML 和 ActionScript 开发的应用程序不仅可以在 Flash/AIR 运行时中运行，还可以在没有 Flash 的浏览器中本地运行、在移动设备上作为 PhoneGap/Cordova 应用程序运行，以及在嵌入式 JS 环境（例如 Chromium Embedded Framework）中运行。 Royale 有潜力允许您的 MXML 和 ActionScript 代码在比 Flash 目前更多的地方运行。

#### 游戏框架

* [CitrusEngine](http://citrusengine.com/) - 基于 Starling 和 Away3D 构建的专业级游戏引擎。
* [StarlingPunk](https://github.com/asaia/StarlingPunk) - 基于 Starling 构建的框架，可为您的游戏项目添加结构和组织。
* [FlashPunk](https://github.com/useflashpunk/FlashPunk) - 构建 2D 游戏的框架。提供图形、事件、输入、动画等。
* [Flixel](https://github.com/AdamAtomic/flixel) - 您可以扩展有用的基类来制作您自己的游戏对象。
* [Tetragon](https://github.com/NothingInteractive/tetragon) - 用于构建任何类型游戏的跨平台框架。提供资源管理、调试工具、多区域设置支持、分层可扩展性、面向游戏的数据结构等等。
* [Pixelizer](https://github.com/johanp/Pixelizer) - 用于构建 2D 游戏的基于组件的游戏引擎。提供渲染、动画、输入等。
* [AS3isolib](https://github.com/as3isolib/as3isolib.v1) - 等距库的开发是为了帮助创建等距投影游戏。
* [IsoHill](https://github.com/jadbox/IsoHill-Game-Engine) - 基于 Starling 构建的基于 GPU 的等距引擎，带有 TILED 地图解析器、图层等（[网站](http://www.isohill.com/)）。
* [YCanvas](https://github.com/jozefchutka/YCanvas) - 高性能 2D 图块渲染器和世界地图渲染器。
* [ND2D](https://github.com/lrrrs/nd2d) - 使用 Stage3D 的 GPU 加速 2D 游戏引擎 ([ND2Dx](https://github.com/NoRabbit/ND2Dx))。
* [Nexus](https://github.com/tversteeg/Nexus) - 使用 Stage3D 的 GPU 加速 2D 游戏引擎。

#### 3D框架

* [AwayBuilder](http://awaytools.com/awaybuilder/) - 用于导入、优化和烘焙来自各种来源的 3D 资源的可视化工作流程工具。
* [Away3D](https://github.com/away3d/away3d-core-fp11) - 适用于 Flash Player 11+ 的开源 GPU 加速 3D 引擎（[示例](https://github.com/away3d/away3d-examples-fp11)）。
* [Away3D OpenFL](https://github.com/away3d/away3d-core-openfl) - 适用于 Neko、HTML5 和本机 CPP 的 Away3D。 （[示例](https://github.com/away3d/away3d-examples-openfl)）。
* [AwayPhysics FP11](https://github.com/away3d/awayphysics-core-fp11) - AwayPhysics - Away3D FP 11 的 3D 物理库（[示例](https://github.com/away3d/awayphysicals-examples-fp11)）。
* [Alternativa3D](https://github.com/AlternativaPlatform/Alternativa3D) - Alternativa3D GPU 加速 3D 引擎（[示例](https://github.com/AlternativaPlatform/Alternativa3DExamples)）。
* [Flare3D](http://flare3d.com/) - 具有高性能引擎和关卡编辑器 IDE 的商业 3D 平台。
* [Zen3D](https://github.com/hgupta9/Zen3D) - 适用于 Adob​​e Flash 和 AIR 的高性能 3D 引擎（基于 GPU）。

#### 动画

* [GreenSock GSAP](https://greensock.com/gsap-as) - Flash 的行业标准动画库（TweenLite、TweenMax）([github](https://github.com/greensock/GreenSock-AS3))。
* [GTween](http://gskinner.com/libraries/gtween/) - 小型但强大的库，用于程序化补间、动画和过渡。
* [DragonBones](http://dragonbones.github.io/) - 使用 Starling 的高速骨骼动画以及从 Flash Pro 导出动画的工具。
* [FlashEff2](http://www.flasheff.com/) - Premiere 程序化动画库，具有 100 多种过渡和文本效果。
* [FlashEffNano](http://www.flasheffnano.com/) - FlashEff 过渡库针对移动设备进行了优化，拥有 750 种样式的 20 多种过渡。
* [StarlingGAFPlayer](https://github.com/zenrobin/StarlingGAFPlayer) - 使用 Starling 播放 GAF 动画（在 Flash Pro 中创作的动画）。

#### 信号

* [AS3-signals](https://github.com/robertpenner/as3-signals) - AS3 事件的新方法受到 C# 事件和 Qt 中的信号/槽的启发。
* [react-as3](https://github.com/tconkling/react-as3) - 信号/槽和函数反应式编程库。
* [Signaller](https://github.com/whitered/Signaller) - 发出信号执行限制调度权。
* [Fa-as3](https://github.com/fabrikagency/fa-as3) - 少写，多做框架，像 jQuery 一样建模。

#### 功能性

* [AS3FP](https://github.com/jadbox/AS3FP) - 基于 Haskell 和 Coffeescript 的函数式习语集合。
* [Raix](https://github.com/richardszalay/raix) - 反应式和交互式扩展简化了交互式数据（数组）或反应式数据（事件）的处理。
* [Fxp-as3](https://github.com/j3k0/fxp-as3) - 功能库的灵感来自于“最充足的指南”。

#### 单元测试

* [AS3unit](https://github.com/Hoten/as3unit) - ActionScript 3 的单元测试框架。
* [hamcrest-as3](https://github.com/drewbourne/hamcrest-as3) - 匹配器对象允许以声明方式定义“匹配”规则。
* [expect.as](https://github.com/krzysztof-o/expect.as) - ActionScript 3 的 BDD 风格断言库。
* [AS3spec](https://github.com/f1337/as3spec) - AS3 的小型 BDD 框架，受到 Bacon 和 RSpec 的启发。
* [Flexunit](https://github.com/flexunit/flexunit) - Actionscript 3 和 Flex 项目的 FlexUnit 项目。
* [ASunit](https://github.com/patternpark/asunit) - 唯一支持 Flash Player 6、7、8、9 和 10 的单元测试框架。
* [RobotEyes](https://github.com/Stray/RobotEyes) - TDD 的端到端测试。 WindowLicker 和 Drew Bourne 的 Mockolate 的混合体。

## 用户界面
#### 用户界面组件

* [MinimalComps](https://github.com/minimalcomps/minimalcomps) - Flash 的最小 ActionScript 3.0 UI 组件。
* [MadComponents](https://github.com/danfreeman/MadComponents) - 适用于 AS3 / AIR 的流行移动 UI 框架。
* [AsWing](https://github.com/dreamsxin/AsWing) - 开源 Flash ActionScript GUI 框架。
* [GPUI](https://github.com/inspirit/GPUI) - 基于 Stage3D (GPU) 的微型 GUI 库。
* [Falcon](https://github.com/HendrixString/Falcon) - Feathers 的响应式/灵活的移动用户界面控件。
* [Flex-maps](https://github.com/igorcosta/flex-maps) - Apache Flex 中地图的最终解决方案。
* [FlexBook](https://github.com/blvz/FlexBook) - Flex 的出色翻页组件。
* [Flex-Android-Material-Skins](https://github.com/quick6black/flex-Android-Material-Skins) - Flex Mobile 组件的 Android Material Design 皮肤。

#### 椋鸟组件

* [TabbedApplication](https://github.com/pol2095/Feathers-Extension-Tabbed-Application) - 基于视图的导航模型，可通过滑动来导航选项卡。
* [DataGrid](https://github.com/pol2095/Feathers-Extension-DataGrid) - 显示带有列标题和平滑滚动的数据网格。
* [DataTree](https://github.com/pol2095/Feathers-Extension-Tree) - 显示排列为可展开树的分层数据。
* [Canvas](https://github.com/pol2095/Feathers-Extension-Canvas) - 支持基本的矢量绘图功能。
* [CircleProgress](https://github.com/pol2095/Feathers-Extension-CircleProgress) - 使用径向进度条显示进度。
* [ZoomableControl](https://github.com/pol2095/Feathers-Extension-ZoomableControl) - 允许使用多点触控输入进行捏合缩放。
* [Toaster](https://github.com/pol2095/Feathers-Extension-Toaster) - 关于小弹出窗口中的操作的简单反馈。 。
* [Google Maps](https://github.com/ZwickTheGreat/feathers-maps) - Google Maps for Starling，针对移动设备进行了优化。

#### 布局

* [Adobe TLF](https://github.com/apache/flex-tlf) - Adobe/Apache Flex 文本布局框架 (TLF)。
* [TinyTLF](https://github.com/joelhooks/tinytlf) - 构建在 Flash/Flex 的 Flash 文本引擎之上的多功能文本布局框架。
* [TransformManager](https://greensock.com/TransformManager) - 作者：格林索克。显示对象的交互式缩放/旋转/移动。
* [TransformTool](https://github.com/senocular/TransformTool) - 用于在 2D 空间中操作对象的自由变换工具（AS、JS）。
* [Argilla-Mosaic](https://github.com/folletto/Argilla-Mosaic) - 动态布局库。
* [xrope](https://github.com/evan-liu/xrope) - 用于本机 AS3 显示对象的简单布局库。
* [miglayout-as](https://github.com/develar/miglayout-as) - MigLayout 的端口，一个功能强大的 Flash/Flex/FlashCocoa (SWT/Swing/JavaFX) 布局管理器。

#### 多点触控

* [TUIO Client](https://github.com/lagerkoller/tuio-as3) - 多点触控硬件的通用框架，支持 TUIO/FLC 和 TUIO/TCP ([web](http://www.tuio.org/?flash))。
* [Gestouch](https://github.com/fljot/Gestouch) - 多点触控手势识别库，用于构建更好的自然用户界面。
* [Gestures.IO](https://github.com/GesturesIO/gesturesio-as3) - 简化您创建基于手势的自然交互的方式。
* [TouchScript](https://github.com/TouchScript/TouchScript.as3) - 多点触控框架，使处理大型触摸表面上的复杂手势交互变得更加容易。

#### 游戏控制器

* [AS3dpad](https://github.com/duckleg/as3dpad) - 专为 Adobe AIR Mobile (Android/iOS) 设计的虚拟触摸屏游戏手柄。
* [Gamepad](https://github.com/iainlobb/Gamepad) - 使用键盘模拟模拟操纵杆输入。
* [Advanced_Joystick](https://github.com/justjoeyuk/Advanced_Joystick) - Starling Framework 的操纵杆，专为 Adob​​e AIR Mobile 设计。
* [AS3-Controller-Input](https://github.com/arkeus/as3-controller-input) - 与 Adob​​e AIR 的 Ouya 和 Xbox360 游戏控制器进行交互。

## 多媒体

#### 增强现实

* [FLARToolKit](https://github.com/Saqoosha/FLARToolKit) - 行业标准 ARToolkit 库的 AS3 端口，适用于 Flash Player 11。（[网站](http://www.libspark.org/wiki/saqoosha/FLARToolKit/en)）。
* [FLAREmulator](https://github.com/theflashbum/FLAREmulator) - 测试 AR 演示，看看使用或不使用网络摄像头时哪些有效，哪些无效。
* [FLARManager](http://words.transmote.com/wp/flarmanager/) - 使用 FLARToolkit/flare.tracker/flare.NFT 构建增强现实应用程序的轻量级框架。
* [NyARToolkitAS3](https://github.com/nyatla/NyARToolkitAS3) - NyARToolkit AS3 版本。基于标记的增强现实库。
* [EZFLAR](https://github.com/tcha-tcho/EZFLAR) - 一个简化 AR 工作方式的小包装。
* [IN2AR](https://github.com/inspirit/IN2ARSDKExamples) - IN2AR 跨平台增强现实引擎 SDK。

#### 数据可视化

* [Axiis](https://github.com/hgupta9/AxiisCharts) - 数据可视化框架，包括折线图、条形图、楔形图、柱形图、簇图、面积图、史密斯图和树形图。
* [Open Flash Charts](https://sourceforge.net/projects/openflashchart/) - 折线图、面积图、条形图、饼图、散点图。
* [Flare](https://github.com/prefuse/Flare) - 图表和图形，支持数据管理、视觉编码、动画和交互技术。
* [clearmaps](https://github.com/sunlightlabs/clearmaps) - 数据可视化的映射框架。
* [redada](https://github.com/geraldo/redada) - 使用 GraphML 文件对加权图进行交互式可视化。
* [Flextreemap](https://github.com/joshtynjala/flextreemap) - Adobe Flex 的 TreeMap 数据可视化组件。
* [GraphVisualizer](https://github.com/armisael/GraphVisualizer) - 一款用于绘制动态图形的 Flex 3 + ActionScript 3 Web 软件。
* [Weave](https://github.com/WeaveTeam/Weave) - 基于网络的分析和可视化环境。
* [Social-grid](https://github.com/Instrument/social-grid) - 社交媒体的抽象网格可视化。

#### 相机

* [CameraDetection](https://github.com/cataclysmicrewind/CameraDetection) - 摄像头检测。
* [Fluocam](https://github.com/Fluocode/Fluocam) - Starling 应用程序的虚拟相机。
* [WebcamRecorder](https://github.com/Stupeflix/WebcamRecorder) - 来自网络摄像头的无铬视频/音频/静态图像录制。
* [FlashyWrappers](https://github.com/rainbowcreatures/FlashyWrappers) - 从 Windows/Android/iOS/OSX 上的 AIR 应用程序录制视频。

#### 图片

* [Scale9Image](https://github.com/Tibus/Scale9Image) - 优化了八哥的scale9Grid图像。
* [ASImageLib](https://github.com/terrynoya/ASImageLib) - 用于动作脚本的 BMP/PNG 解码器。
* [Async-Image-Encoders](https://github.com/LeeBurrows/Async-Image-Encoders) - 将 BitmapData 对象异步编码为图像文件格式。
* [Flip-Planes-AS3](https://github.com/jamesflorentino/Flip-Planes-AS3) - 照片幻灯片效果。
* [AS3-transitions-lib](https://github.com/foo123/as3-transitions-lib) - 图像转换库。
* [Inspirit Image](https://github.com/hgupta9/InspiritImage) - FFT、SURF、边缘检测、流体求解器等
* [Inspirit GPUImage](https://github.com/inspirit/GPUImage) - 基于 GPU 的图像处理框架。
* [AS3potrace](https://github.com/PowerflasherBR/as3potrace) - POTrace 实现，将位图图像跟踪为矢量。
* [ATF-Encoder](https://github.com/plepers/ATF-Encoder) - 在纯 AS3 中编码/解码 ATF（Adobe 纹理格式）文件。
* [AS3-klt](https://github.com/motemen/as3-klt) - Kanade-Lucas-Tomasi 特征跟踪器实现。
* [BlurHash](https://github.com/roipeker/as3-blurhash) - ActionScript 3.0 中的 BlurHash 编码器/解码器实现..

#### 字体

* [Firetype](https://github.com/MaxDidIt/firetype) - 解析 OpenType 字体并使用 Stage3D 渲染它们。
* [BMFontRenderer](https://github.com/bengarney/BMFontRenderer) - BMFont 格式位图字体数据的 AS3 渲染器。
* [HanFont](https://github.com/kyoji2/HanFont) - 用于在 ActionScript 中嵌入中文字体的 AIR 应用程序。
* [Ficon.as](https://github.com/dv/Ficon.as) - 轻松包含图标字体的库。

#### 粒子

* [Flint](https://github.com/richardlord/Flint) - Flash 和 Flex 的粒子引擎。
* [Desuade Partigen](http://desuade.com/partigen) - Desuade Partigen 粒子生成系统（[github](https://github.com/andrewfitz/desuade)）。
* [Angulex](https://github.com/cosmindolha/ParticleDesigner) - Starling 框架的粒子设计器 (ActionScript 3)。
* [SAP](https://github.com/gonchar/SAP) - Starling 的粒子系统。
* [Starling-Particles](https://github.com/Gamua/Starling-Extension-Particle-System) - Starling 框架的粒子系统，与 71squared.com 的“粒子设计器”兼容。
* [MotionParticleSprite](https://github.com/bjeld/motionparticlesprite) - 在 Flash Pro 中设计运动路径并用它来引导 Starling 粒子。

#### 全景浏览器

* [Pantaloons](https://github.com/EyeSee360/Pantaloons) - 在 Flash Player 中查看全景。
* [SaladoPlayer](https://github.com/mstandio/SaladoPlayer) - 全景查看器。
* [PanoramicViewer](https://github.com/BrianMehrman/PanoramicViewer) - 3D 全景查看器。
* [Sphere_panorama](https://github.com/suzumura-ss/flash_sphere_panorama) - 具有用 AS3 (Alternativa3D) 编写的等距柱状纹理的全景播放器。
* [CuTy](https://github.com/fieldOfView/CuTy) - 基于 Flash 10 的 QTVR 全景查看器。

#### 二维码

* [Zxing AS3](https://github.com/zxing/zxing/tree/c1df162b95e07928afbd4830798cc1408af1ac67/actionscript) - QR 码检测和生成（[文档](https://zxing.github.io/zxing/)）。
* [AS3-qrcode-encoder](https://github.com/jbpin/as3-qrcode-encoder) - as3中的QR码编码器。
* [qrcode-as](https://github.com/yanbe/qrcode-as) - QR 码阅读器支持 Windows、Mac 和 Linux 上的网络摄像头。

#### 声音

* [SoundAS](https://github.com/treefortress/SoundAS) - 适用于 AS3 的现代轻量级声音管理器。
* [Standingwave3](https://github.com/maxl0rd/standingwave3) - 动态音频库。
* [Standingwave3-addons](https://github.com/charlesclements/standingwave3-addons) - SW3 的插件。
* [Soundtouch-as3](https://github.com/also/soundtouch-as3) - SoundTouch 声音处理库的 AS3 端口。
* [SeiON](https://github.com/cardin/SeiON) - 声音管理库。
* [AS3-Sound-Manager](https://github.com/GrupoW/as3-Sound-Manager) - Matt Przybylski 的声音管理器类的升级版本。
* [AS3sfxr](https://github.com/SFBTom/as3sfxr) - 将 sfxr 从 C++ 移植到 AS3，使用 Flash Player 10 的新声音和文件功能。
* [AS3-audio](https://github.com/singuerinc/as3-audio) - Actionscript 中的音频管理。
* [SiON](https://github.com/keim/SiON) - Flash 软件合成器。
* [FlashWavRecorder](https://github.com/michalstocki/FlashWavRecorder) - 录制音频并保存为 WAV。
* [Local-recorder](https://github.com/pauln/local-audio-recorder) - 本地录音机（无需流媒体服务器）。  目前需要 Flash Player 10.1 或更高版本。
* [Jukebox](https://github.com/AlwynW/Jukebox) - Actionscript 3 项目的音乐管理器。
* [Flod](https://github.com/photonstorm/Flod) - Amiga SoundTracker (MOD) 和 FastTracker (XM) 重播库。

#### 视频播放器

* [Flowplayer](https://github.com/flowplayer/flash) - Flowplayer Flash，Web 视频播放器。
* [Goplayer](https://github.com/dbrock/goplayer) - 用 ActionScript 3 编写的现代开源视频播放器。
* [OSFlashVideoPlayer](https://github.com/FlashJunior/OSFlashVideoPlayer) - 开源 Flash 视频播放器。
* [F4player](https://github.com/gokercebeci/f4player) - 开源 AS3 Flash 视频播放器。
* [dashas](https://github.com/castlabs/dashas) - 用 ActionScript 编写的 MPEG-DASH 播放器。
* [hlsplayer](https://github.com/erlyvideo/hlsplayer) - OSMF flash 框架的 HLS 播放器。
* [vgaplayer](https://github.com/euske/vgaplayer) - Adobe Flash Media Server 流 (RTMP) 的开源播放器。

## 数据库

#### SQLite
* [AS3Query](https://github.com/kemsky/as3Query) - 另一个用于 ActionScript 的 SQLite ORM 和查询 DSL。
* [AIRdb](https://github.com/dkeskar/airdb) - AIR ORM，用于在 AIR 和 Flex 应用程序中使用客户端 SQLite。支持 ActiveRecord 样式模型、迁移和关联。
* [Flexine](https://github.com/riadvice/Flexine) - 适用于 AIR 的 SQLite ORM。
* [AIR-sqlite](https://github.com/probertson/air-sqlite) - 用于在 AIR 中使用 SQLite 数据库的实用程序。

#### MongoDB
* [MongoAS3](https://github.com/s9tpepper/MongoAS3) - MongoDB 驱动程序。
* [ActionMongo](https://github.com/RIAlizer/ActionMongo) - MongoDB 驱动程序。

#### 沙发数据库
* [AS3couchdb](https://github.com/bustardcelly/as3couchdb) - 用于与 CouchDB 实例交互的客户端 API。
* [Soup](https://github.com/dima/soup) - 混合 CouchDB、Sinatra、AIR 和 RestfulX，创建具有撤消/重做功能的离线/在线就绪应用程序。

#### MySQL
* [AS3mysql](https://github.com/hgupta9/as3mysql) - MySQL 开源数据库的驱动程序。

#### PostgreSQL
* [Pegasus](https://github.com/uhoh-itsmaciek/pegasus) - PostgreSQL 开源数据库的驱动程序。

#### 动态数据库
* [AWS-dynamodb](https://github.com/ferf/aws-dynamodb-actionscript) - 用于访问 Amazon 的 AWS DynamoDB 的驱动程序。

#### 雷迪斯
* [AS3redis](https://github.com/zhangq0355/as3redis) - Redis 的驱动程序。

## 文件格式

#### 档案

* [FZip](https://github.com/claus/fzip) - 用于加载、修改和创建标准 ZIP 档案的成熟库。
* [ASZip](https://code.google.com/archive/p/aszip/) - 从 AS3 生成 ZIP 存档。
* [Untar-Worker](https://github.com/mesmotronic/as3-worker-untar) - 使用 AS3 Workers（后台线程）提取 TAR。

#### 3D 格式

* [AsCollada](https://github.com/timknip/ascollada) - 解析 COLLADA 3D 模型文件（[fork](https://github.com/david-gregory/ascollada)）。
* [AsBlender](https://github.com/timknip/asblender) - 解析 Blender .BLEND 文件。
* [AS3-bvh-parser](https://github.com/rkn14/as3-bvh-parser) - 解析 BVH 文件。
* [EasyAGAL](https://github.com/Barliesque/EasyAGAL) - 通过代码完成、代码提示、宏等简化 AGAL 着色器的开发。

#### CSV

* [CSV4AS3](https://github.com/lizardon/CSV4AS3) - 从 Apache Commons CSV 移植的 CSV 库。
* [Csvlib](https://github.com/51systems/csvlib) - CSV 解析器。

#### CSS

* [AS3csslib](https://github.com/heyfrench/as3csslib) - ActionScript 3.0 的 CSS3 解析器、选择器和样式引擎。
* [Fcss](https://github.com/theflashbum/fcss) - Flash 级联样式表库。
* [Stylekit-as3](https://github.com/videojuicer/stylekit-as3) - 使用 CSS3 的可换肤用户界面。
* [Sass4as](https://github.com/jeremyruppel/sass4as) - ActionScript 3 语法上很棒的样式表。
* [Jakute-CSS](https://github.com/kakenbok/Jakute-Styling-Engine) - Jakute 是 ActionScript/Flash 的 CSS 框架。
* [CSS.as](https://gist.github.com/trxcllnt/1161266) - 单文件 CSS 解析器，TinyTLF 项目的一部分。

#### BSON

* [ActionBSON](https://github.com/fminzoni/ActionBSON) - BSON 数据编码器/解码器。
* [MongoAS3](https://github.com/s9tpepper/MongoAS3) - MongoDB 驱动程序，其中包括 BSON I/O。

#### EXIF

* [AS3-exif-lib](https://github.com/unstoppable/actionscript-exif-reading-lib) - 解析 JPEG EXIF 数据。
* [Exif-as3](https://github.com/bashi/exif-as3) - 解析 JPEG EXIF 数据。

#### FXG

* [Fxg-as3-lib](https://github.com/pixelami/fxg-as3-lib) - 纯 AS3 FXG 渲染库（支持运行时渲染和 mxml）。
* [Fxg2as3](https://github.com/ZackPierce/fxg2as3) - 将 FXG 标记转换为可执行的 Actionscript 3 代码。

#### 动图

* [AS3gif](https://github.com/audreyt/as3gif) - 播放和编码动画 GIF。
* [GIF Player](https://github.com/theturtle32/Flash-Animated-GIF-Library) - 在 Flash 中播放动画 GIF。
* [Async-gif-decoder](https://github.com/honzabrecka/async-gif-decoder) - 异步 GIF 解码器和播放器。

#### 伊卡

* [AS3iCAL](https://github.com/nicolai86/as3.iCal) - 基于 RFC2445 规范的 iCal 解析器。

#### JSON

* [Actionjson](https://github.com/mherkender/actionjson) - 更快、更高级的 ActionScript 3 JSON 库。
* [Jameson](https://github.com/mattupstate/jameson) - JSON 文档对象映射器。
* [Serialkiller](https://github.com/benbjohnson/serialkiller) - JSON 和 XML 序列化库。
* [JsonMapper](https://github.com/kemsky/JsonMapper) - 类型化 JSON 解析器。
* [JSONTools](https://github.com/s9tpepper/JSONTools) - JSON 错误、JSWoof JSON 库的速度以及称为 E4J 的 E4X 样式查询。

#### 降价

* [Showdown.as](https://gist.github.com/cstrahan/648771) - showdown.js 的端口。
* [Actiondown](https://github.com/bbeaumont/Actiondown) - Javascript Showdown 的端口。
* [Markdownlib](https://github.com/Corsaair/markdownlib) - Markdown 的实现。

#### MP3

* [AS3id3lib](https://github.com/devxoul/as3id3lib) - 解析 MP3 ID3 数据。
* [AS3Icy](https://github.com/claus/as3icy) - 解码并播放来自 Shoutcast、Icecast 和 Limewire 的实时 MP3 流。

#### PDF

* [AlivePDF](https://code.google.com/archive/p/alivepdf/) - 客户端 PDF 生成（[github](https://github.com/riadvice/alivepdf)）。
* [PurePDF](https://github.com/sephiroth74/purePDF) - 完整的 PDF 库，Java iText 的端口。
* [HalcyonPDF](https://github.com/systemed/halcyon_pdf) - OpenStreetMap PDF 渲染器。
* [PDFCase](https://github.com/dickclaus/pdfcase) - PDF 库。
* [PDFView](https://github.com/jankapunkt/PDFView) - 从头开始构建的 PDF 查看器。

#### PSD

* [AS3-psd-parser](https://github.com/warrenseine/as3-psd-parser) - 解析 Photoshop PSD 文件并渲染为 BitmapData 对象。

#### 主权财富基金

* [AS3swf](https://github.com/claus/as3swf) - 用于解析、创建、修改和发布 SWF 文件的低级库。
* [AS3abc](https://github.com/imcj/as3abc) - 用于解析、创建、修改和发布 ABC（Actionscript 块代码）文件的低级库。
* [SWFWire](https://github.com/magicalhobo/SWFWire) - SWF 反编译器和检查器工具。
* [Abc-abstraction](https://github.com/krilnon/abc-abstraction) - 允许对 ABC 进行分析、操作、打包回 SWF 并运行。

#### 静止无功发生器

* [AS3SVGRenderer](https://github.com/LucasLorentz/AS3SVGRenderer) - Flash Player 的 SVG 渲染器。
* [SVGParser](https://github.com/millermedeiros/SVGParser) - FIVe3D 和 HTML5 画布的 SVG 解析器和渲染器。

#### XML

* [XMLSerializer](https://github.com/vapesolius/XMLSerializer) - 允许从 ActionScript 到 XML 以及从 XML 到 ActionScript 的数据序列化的库。
* [DynamicXMLParser](https://github.com/lmgerhard/DynamicXMLParser) - 将 xml 内容动态解析为预定义的数据类 (actionscript 3)。
* [Nudge](https://github.com/pluglimited/Nudge) - 将对象序列化/反序列化为 XML 的框架。
* [AStream](https://github.com/kokorin/AStream) - XML 到对象（反之亦然）的映射库是用 AS3 编写的。与 XStream 兼容。

#### XLSX

* [AS3-xlsx-reader](https://github.com/childoftv/as3-xlsx-reader) - 解析 Open XML Excel (.XLSX) 或 Open Office 电子表格。


## 联网
#### 数据加载器

* [GreenSock LoaderMax](https://github.com/greensock/GreenSock-AS3) - 提供一种简单而强大的方法来在运行时加载资源。
* [BulkLoader](https://github.com/arthur-debert/BulkLoader) - Actionscript 的批量资源加载库。
* [AssetLoader](https://github.com/Matan/AssetLoader) - 基于 AS3Signals 构建的 AS3 多文件/资产加载器。

#### 硬件

* [AS3midilib](https://github.com/heyfrench/as3midilib) - 使用 MIDI 文件和 MIDI 输入/输出设备。
* [AS3glue](https://code.google.com/archive/p/as3glue/) - Arduino 板的通信。
* [AS3-arduino](https://github.com/quetwo/as3-arduino-connector) - 将 Arduino 原型板连接到 Adob​​e AIR。
* [AIRkinect](https://github.com/AS3NUI/airkinect-2-core) - ANE 用于与 Microsoft Kinect 集成。 （[示例](https://github.com/AS3NUI/airkinect-2-examples)）。
* [KinectGate](https://github.com/cleoag/KinectGate) - KinectSDK 到 AS3 套接字门。
* [Kinect-Gestures](https://github.com/tonybeltramelli/Air-Kinect-Gesture-Lib) - AIR Kinect 手势库。
* [OpenTSPS](https://github.com/labatrockwell/openTSPS) - TSPS 是一个用于感知空间中人员的跨平台工具包。它对实时视频（Kinect、网络摄像头等）执行 openCV 操作，并将其作为 JSON（通过 WebSockets）、OSC、TUIO 或 TCP 发送到客户端。
* [LeapMotionAS3](https://github.com/logotype/LeapMotionAS3) - 与 LeapMotion 传感器集成（提供手势、图像、骨骼/骨骼 @ 210 FPS）。

#### 服务器

* [AIRhttp](https://github.com/leopoldodonnell/airhttp) - Adobe AIR 的 HTTP 服务器。
* [AIR-Server](https://github.com/wouterverweirder/AIR-Server) - Adobe AIR 的套接字服务器库。

#### 开放认证

* [Actionscript-oauth2](https://github.com/charlesbihis/actionscript-oauth2) - 与 OAuth 2.0 服务交互。
* [oauth-flex](https://github.com/oauth-io/oauth-flex) - Apache Flex/ActionScript 的 OAuth.io 插件。
* [oauth-as3](https://github.com/mlepicki/oauth-as3) - oauth-as3 库的 Mavenized RSL 版本 - ActionScript 3 的 OAuth。

#### HTTP协议

* [Hendrix-HTTP](https://github.com/HendrixString/Hendrix-HttP-AiR) - ActionScript 3 (as3) 的轻量级 HTTP 库，灵感来自 Square 的 OkHttp。
* [HTTPForm](https://github.com/dv/HTTPForm) - 模拟 multipart/form-data HTML 表单提交请求，包括文件上传。
* [AS3httpclient](https://github.com/abdul/as3httpclient) - HTTP 客户端实现。
* [AS3httpclient](https://github.com/gabriel/as3httpclient) - HTTP 客户端实现。
* [Amazon Web Services](https://github.com/satoshi7/ActionScript-API-for-AWS-Amazon-Web-Services-) - 适用于 AWS 的 AS3 API。

#### 对等

* [P2Plocal](https://github.com/palkan/as3_p2plocal) - 本地 RTMFP 连接。
* [Android-Flash-P2P](https://github.com/beautifycode/Android-Flash-P2P) - Client.swf 和具有 AIR 的 Android 设备之间的 P2P 通信。
* [NetGrouper](https://github.com/walpolea/NetGrouper) - NetGroup 和 RTMFP 多播功能的包装器，可通过本地网络或 Adob​​e Cirrus 创建快速的 P2P 多人游戏。
* [HydraP2P](https://github.com/devboy/HydraP2P) - 简化了 Flash Player 10.1 中引入的点对点 API。
* [GroupP2P](https://github.com/oohazard/GroupP2P) - 基于 P2P 的网络组。
* [HLS-P2P](https://github.com/lava-tech/hls-p2p) - 基于Flash OSMF的混合cdn&p2p hls解决方案。
* [P2Pmessaging](https://github.com/dreamsocket/actionscript-p2p_messaging) - 用于在 Flash 中执行 P2P 的简单消息传递框架。
* [ArcusNode](https://github.com/OpenRTMFP/ArcusNode) - RTMFP Rendevouz 服务，用于在 Node JS 上使用 Adob​​e Flash 进行对等辅助网络。

#### 插座

* [AS3WebSocket](https://github.com/theturtle32/AS3WebSocket) - 最终 WebSocket 草案 RFC6455 的 WebSocket 客户端实现。
* [SmartSocket](https://github.com/XaeroDegreaz/SmartSocket) - SmartSocket 是一个 Java 和 PHP 套接字服务器引擎，可以快速轻松地创建多用户应用程序。
* [FlashSocket.IO](https://github.com/simb/FlashSocket.IO) - 客户端从 AS3/AIR 客户端连接到 Socket.IO 服务器。
* [Socket.io](https://github.com/ascorbic/socket-io-actionscript) - Socket.IO Actionscript 3 客户端。
* [AMFsocket](https://github.com/chadrem/amf_socket) - 用于高性能网络通信的双向 RPC 库。
* [Sockpuppet](https://github.com/rjungemann/sockpuppet) - 使用 AMF 完成 Ruby/ActionScript 套接字客户端/服务器。
* [Socket.io-flash](https://github.com/sinnus/socket.io-flash) - 与 Socket.IO v.0.8+ 服务器的通信。
* [ws-flash-client](https://github.com/youurayy/ws-flash-client) - 可靠、简约的 WebSocket 客户端（在本机 WebSocket 不可用的情况下使用 Adob​​e Flash）。

#### 协议

* [GIT](https://github.com/nexussays/git-as3) - Git 的客户端实现。
* [AIRplay](https://github.com/mikkoh/AS3-Airplay) - Apple Airplay 的客户端实现。
* [TeaTime](https://github.com/aemoncannon/croqodile) - Croquet 项目 TeaTime 协议的 AS3/Erlang 实现。
* [XMPP](https://github.com/lyokato/as3xmppclient) - XMPP 库的客户端实现。
* [XMPP](https://github.com/bluef/kuching) - XMPP 库的轻量级实现。
* [AMQP](https://github.com/0x6e6562/as3-amqp) - AMQP 0-8 版本的客户端实现。
* [NTP](https://github.com/charlespalen/AS3-NTP-Implementation) - NTP 客户端（网络时间协议）的客户端实现。
* [FUDI](https://github.com/matthiasbreuer/FUDI-as3) - Puredata FUDI 协议的客户端实现。
* [BDD Cucumber](https://github.com/flashquartermaster/Cuke4AS3) - Flash ActionScript 的 BDD Cucumber 线协议实现。

#### 电子邮件

* [AIRXMail](https://github.com/hgupta9/AirXMail) - 完整的客户端电子邮件库，支持 SMTP、POP3 和 IMAP4。
* [AS3Mailer](https://github.com/Matan/AS3Mailer) - 使用服务器脚本发送电子邮件或调用 mailto。

## 公用事业

#### 人工智能

* [FiniteStateMachine](https://github.com/pzUH/FiniteStateMachine) - AI 机器人/代理的有限状态机。
* [N-GramPredictor](https://github.com/pzUH/N-GramPredictor) - AI 机器人/代理的 n-Gram 预测器。
* [Naive-BayesPredictor](https://github.com/pzUH/Naive-BayesPredictor) - AI 机器人/代理的朴素贝叶斯预测器。
* [HierarchicalStateMachine](https://github.com/pzUH/HierarchicalStateMachine) - AI 机器人/代理的分层状态机。
* [Godmode-as3](https://github.com/tconkling/godmode-as3) - 行为树实现（人工智能）。
* [DecisionTree](https://github.com/pzUH/DecisionTree) - AI 机器人/代理的二元决策树。
* [FuzzyStateMachine](https://github.com/pzUH/FuzzyStateMachine) - 用于 AI 机器人/代理的模糊状态机 (FuSM)。
* [SmartKid](https://github.com/skyfeiyun/SmartKid) - 适用于 2D 和 3D 游戏的强大 AI 引擎。

#### 异步

* [EasyAS-Worker](https://github.com/myflashlab/easyAS-Worker) - AIR Workers 的简化包装。
* [Worker-from-class](https://github.com/bortsen/worker-from-class) - 从类定义创建工人。

#### 加密货币

* [BlooddyCrypto](https://github.com/blooddy/blooddy_crypto) - 用于处理二进制数据的高性能库。该库包含 MD5、SHA-1、SHA-2、Base64、CRC32、JSON、PNG/JPEG 编码器。
* [AS3Crypto](https://github.com/timkurvers/as3-crypto) - Henri Torgemane 优秀的密码学库的分支（[patched](https://github.com/lyokato/as3crypto_patched)）。
* [AS3corelib](https://github.com/mikechambers/as3corelib) - MD5 和 SHA1 哈希、图像编码器和 JSON 序列化。
* [ASCrypt](https://github.com/Meychi/ASCrypt) - 具有适用于多种语言的类似 API 的加密库。
* [Nexuslib](https://github.com/nexussays/nexuslib-as3) - 反射、序列化、种子随机数生成、密码学、网络等等。
* [Hashlib](https://github.com/Corsaair/hashlib) - 超过 30 种不同的哈希函数。
* [XXTEA-AS3](https://github.com/xxtea/xxtea-as3) - ActionScript 3 的 XXTEA 加密算法库。
* [Gibberish-AES](https://github.com/NordMike/gibberish-aes-as3) - 完全符合 OpenSSL 标准的 ActionScript 3 库，用于 AES 加密。

#### 数据

 * [AS3Commons Collections](https://github.com/AS3Commons/as3commons-collections) - 适用于 AS3 的复杂且高性能的集合和迭代器。
 
#### 几何

* [AS3geometry](https://github.com/alecmce/as3geometry) - 基元、多边形、交叉点等
* [AS3GeomAlgo](https://github.com/azrafe7/as3GeomAlgo) - 几何算法的集合。 hxGeomAlgo 端口。
* [Coral](https://github.com/richardlord/Coral) - 3D 数学的高性能类（点、向量、矩阵、四元数）。
* [Csg.as](https://github.com/timknip/csg.as) - 3D 网格上的构造实体几何。
* [PathUtils](https://github.com/alinakipoglu/Actionscript-PathUtils) - 使用二次序列、贝塞尔序列和线序列。
* [Hilbert](https://github.com/nodename/Hilbert) - 来自 Cortesi/scurve 的希尔伯特曲线端口。
* [AS3AStar](https://github.com/tomnewton/AS3AStar) - 快速 A-Star 寻路算法。
* [A-star_pathfinder](https://github.com/kevhiggins/a-star_pathfinder) - A-Star 寻路界面，用于基于图块的地图。
* [As3Pathfinder](https://github.com/azakhary/As3Pathfinder) - 使用 Dijkstra 算法编写的网格路径查找库。

#### 数学

* [AS3Units](https://github.com/erussell/AS3Units) - NGUnit 的端口。解析、格式化以及测量单位之间的转换。
* [AS3LinAlg](https://github.com/inspirit/AS3LinAlg) - 线性代数库（Jacobi SVD、特征向量/值、Cholesky LU 等）。
* [Performance Primitives](https://github.com/martinkallman/performance-as3) - 以英特尔性能基元为模型的高性能数学。
* [Zexpression](https://github.com/Xorcerer/zexpression) - 使用函数和变量解析和评估数学表达式。
* [FlexibleMatrix](https://github.com/Lukx/FlexibleMatrix) - 多用途 Matrix 类。
* [AS3eval](http://eval.hurlant.com/) - 打包 Tamarin ESC 编译器以在 Flash Player 中工作。 （[替代]（https://github.com/SimonRichardson/as3-eval））。
* [FlashFormulaEditor](https://github.com/zasdfgbnm/FlashFormulaEditor) - 使用 Adob​​e Flex 制作的公式编辑器。

#### 文字

* [Linkify-as3](https://github.com/CodeCatalyst/linkify-as3) - 将 URL、电子邮件地址、电话号码转换为可点击的链接。
* [AS3hyphenation](https://github.com/gka/as3hyphenation) - Javascript 文本连字符库 Hyphenator.js 的端口。

## 运行时

#### 模拟器

* [NES Emulator](https://github.com/nesbox/emulator) - NES、Super Nintendo、Sega Mega Drive、GameBoy 视频游戏机的模拟器。
* [Commodore 64 Emulator](https://github.com/claus/fc64) - 用 Actionscript 3 编写的低级 Commodore 64 模拟器。
* [8080 Emulator](https://github.com/ozipi/As3_SpaceInvaders_Emulator) - 基于 intel 8080 处理器的 ActionScript 3 太空入侵者模拟器。
* [8-bit VM](https://github.com/OutOfTheVoid/AS3-8-bit-VM) - 用动作脚本编写的八位虚拟机。

#### 口译员

* [JS](https://github.com/theturtle32/RhinoAS3) - RhinoJS，Mozilla 的 Rhino JavaScript 解释器的端口。
* [Simple JS](https://github.com/sixsided/Simplified-JavaScript-Interpreter) - 基于 AS3 的 Javascript 解释器。
* [MIL](https://github.com/ser1zw/MIL) - 用 ActionScript 编写的 MIL 语言 VM 和解释器。
* [TALES](https://github.com/oaubert/tales4as) - ActionScript 的 TALES 解释器。
* [Scheme](https://github.com/hrundik/fScheme) - ActionScript 中的方案解释器。
* [Lisp](https://github.com/rzubek/as_lisp) - Lisp 方言用 Actionscript 编写，带有编译器和字节码解释器。
* [Lisp Compiler](https://github.com/aemoncannon/las3r) - AVM2 的 Lisp 编译器。
* [CannonML](https://github.com/abiyasa/cannonml_as3) - keim 的 CannonML（shmup 脚本语言）解释器。

## AIR 本机扩展

#### 音频ANE
* [SongPicker](https://github.com/richpixel/SongPickerANE) - 适用于 iOS 和 Android 的歌曲选择器/播放器 ANE。
* [SilentSwitch](https://github.com/StickSports/ANE-Silent-Switch) - 如果硬件静音开关打开，则适用于 iOS 的 ANE 将声音静音。
* [VolumePro](https://github.com/myflashlab/VolumePro-ANE) - 控制原生音乐流音量，您可以听到音量变化。
* [SystemVolume](https://github.com/nweber/SystemVolumeNativeExtension) - 与 iOS 和 Android 设备的系统音量交互。

#### 多媒体ANE
* [WebView (Tuarua)](https://github.com/tuarua/WebViewANE) - 适用于 OSX 10.10+、Windows 桌面、iOS 9.0+ 和 Android 21+ 的现代 WebView。在 Windows 上使用 CEF（Chromium 嵌入式框架），在 iOS/OSX 上使用 WKWebView，在 Android 上使用 WebView。
* [WebView (FlashLab)](https://github.com/myflashlab/webView-ANE) - StageWebView 的替代品，允许从 AIR 调用 Javascript 函数。
* [AVANE](https://github.com/tuarua/AVANE) - 用于使用 FFmpeg 构建视频编码应用程序。
* [PDF](https://github.com/myflashlab/PDF-ANE) - 允许您从 AIR 移动应用程序打开 PDF 文件。 Android 和 iOS 均受支持。
* [VideoPlayer](https://github.com/myflashlab/videoPlayer-ANE) - 在 Android 或 iOS 本机视频播放器中播放视频文件。
* [SurfaceVideoPlayer](https://github.com/myflashlab/surfaceVideoPlayer-ANE) - SurfacePlayer ANE 可帮助您在空中移动项目中播放视频文件。
* [Speech](https://github.com/myflashlab/speech-ANE) - 完全在后台将字符串转换为语音文件，反之亦然。
* [MyAR](https://github.com/myflashlab/AR-ANE-Samples) - AR ANE 基于 Metaio 的 SDK，支持 Android 和 iOS 64 位。
* [QR-zbar](https://github.com/saumitrabhave/qr-zbar-ane) - ANE 用于 QR 码阅读器。
* [Barcode](https://github.com/myflashlab/barcode-ANE) - 使用这款超快速条码扫描仪 ANE 扫描几乎任何条码类型。
* [Bullet](https://github.com/mziwisky/bullet-ane) - 子弹物理模拟库。

#### 文件系统 ANE
* [FileChooser](https://github.com/myflashlab/fileChooser-ANE) - 使用户能够从设备文件系统中选择文件。
* [ZipManager](https://github.com/myflashlab/zipManager-ANE) - 使用 Android 和 iOS 上的本机进程超快速地压缩或解压缩大型 zip 存档。
* [Spotlight](https://github.com/myflashlab/Spotlight-ANE) - 与 iOS 9 Spotlight 搜索集成，为搜索项和用户生成的内容建立索引。

#### 网络ANE
* [Firebase](https://github.com/myflashlab/Firebase-ANE) - Android 和 iOS 上的 Google Firebase API 与 ActionScript API 100% 相同。
* [DownloadManager](https://github.com/myflashlab/downloadManager-ANE) - 下载具有暂停/恢复支持的大型数据文件。
* [BitTorrent](https://github.com/tuarua/BitTorrentANE) - 用于构建支持 BitTorrent 的应用程序。

#### 硬件ANE
* [Bluetooth](https://github.com/myflashlab/bluetooth-ANE) - 扫描其他设备，连接并配对，并在它们之间传输数据。
* [GPS](https://github.com/myflashlab/GPS-ANE) - 通过自动检查最佳可用提供商，尽快获取当前设备的 GPS 位置。
* [GoogleVR](https://github.com/myflashlab/GoogleVR-ANE) - Google 虚拟现实 SDK 可供 AIR 开发人员使用。
* [Joystick-ANE](https://github.com/StackAndHeap/joystick-ane) - ANE 操纵杆库。
* [AIRControl](https://github.com/AlexanderOMara/AIRControl) - Adobe AIR 游戏控制器 ANE。
* [AIROUYAController](https://github.com/gaslightgames/AIROUYAController) - ANE 为 OUYA 控制器。
* [AIRKinectv2](https://github.com/Tastenkunst/AIRKinectv2) - 适用于 Windows SDK 的 Microsoft Kinect v2 的 ANE。
* [Serial/MIDI/DMX](https://github.com/benkuper/AIR-NativeExtensions) - AIRBonjour、NativeSerial、NativeDMXController、NativeMIDI、VirtualMIDI、扩展鼠标。
* [LeapMotionAS3](https://github.com/logotype/LeapMotionAS3) - 用于 LeapMotion 传感器的 ANE（提供手势、图像、骨骼/骨骼 @ 210 FPS）。

#### 系统ANE
* [TaskbarProgress](https://github.com/tuarua/TaskbarProgressANE) - 在 OSX 和 Windows 7/8/10 上显示任务栏进度。
* [DesktopToast](https://github.com/tuarua/DesktopToastANE) - 在 Windows 8/10 和 OSX 中显示交互式 Toast 通知。
* [AlarmManager](https://github.com/myflashlab/alarmManager-ANE) - 即使您的 AIR 应用程序已关闭，也可以运行计划任务。
* [InAppPayments](https://github.com/myflashlab/inAppPayments-ANE) - 适用于 Android 和 iOS 的相同应用内计费和应用内购买 ANE。
* [PermissionCheck](https://github.com/myflashlab/PermissionCheck-ANE) - 在您的 Adob​​e Air 应用程序中检查并请求权限。
* [RateMe](https://github.com/myflashlab/RateMe-ANE) - 要求您的用户以最有效的方式评价您的应用程序。
* [Statusbar](https://github.com/myflashlab/Statusbar-ANE) - 在运行时控制 AIR 应用程序中的状态栏。
* [Badge](https://github.com/myflashlab/Badge-ANE) - 控制 iOS 徽章值。
* [WinDebug](http://www.henke37.cjb.net/windebug/) - Windows ANE 控制应用程序、窗口、内存、断点、元数据、注册表等。
* [Can-Open-URL](https://github.com/StickSports/ANE-Can-Open-URL) - 适用于 iOS 的 ANE，用于检测是否安装了应用程序来处理特定的 URL 方案。

#### 社交ANE
* [Facebook](https://github.com/myflashlab/facebook-ANE) - 将 Facebook SDK 集成到您的 AIR 应用程序中。
* [GCM](https://github.com/myflashlab/GCM-ANE) - 在 Android 和 iOS 上使用 Google Cloud 消息传递。 。
* [Baidu](https://github.com/lilili87222/baidu-ane-for-ios-and-android) - 百度 ANE 适用于 iOS 和 Android。

#### 分析ANE
* [Admob](https://github.com/myflashlab/Admob-ANE) - Admob ANE。
* [GameServices](https://github.com/myflashlab/GameServices-ANE) - 适用于 Android+iOS 的 Google 游戏服务。
* [MoPub](https://github.com/StickSports/MoPub-ANE) - 用于 MoPub 广告的 ANE。
* [UMAnalytics](https://github.com/ColerYu/ANE-UMAnalytics) - 适用于 UMAnalytics SDK（iOS 和 Android）的 ANE。
* [Localytics](https://github.com/randori/ANE-Localytics) - 适用于移动 Adob​​e AIR 应用程序（iOS 和 Android）的 Localytics 分析。
* [Testflight](https://github.com/jlopez/ane-testflight) - 苹果测试飞行 ANE。
* [HockeyApp](https://github.com/airext/hockeyapp) - ANE 用于 Hockeyapp 测试和分发平台。
* [Chartboost](https://github.com/ChartBoost/air) - 用于带有编译脚本的 Chartboost SDK 的 ANE。
* [Devtodev](https://github.com/devtodev-analytics/air-sdk) - 为游戏开发者提供的全周期分析解决方案。
