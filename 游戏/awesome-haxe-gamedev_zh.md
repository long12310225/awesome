<divalign="center"><a href="https://haxe.org/"><img src="images/haxe-logo.png"width="500"></a></div>

# 很棒的 Haxe 游戏开发 [![Awesome](https://awesome.re/badge-flat2.svg)](https://awesome.re)

**[Haxe 4](https://haxe.org/)** 的游戏开发资源精选列表，这是一种高级严格类型编程语言，用于生成跨平台本机代码。

请随时更新。

## 内容
* [游戏引擎](#game-engines)
* [低级引擎](#low-level-engine)
* [Physics](#physics)
* [Architecture](#architecture)
* [Networking](#networking)
* [序列化和存储](#serialization-and-storage)
* [Games](#games)
* [Miscellaneous](#miscellaneous)
* [Articles](#articles)
* [其他 haxe 列表](#other-haxe-lists)

## 游戏引擎

这些是 Haxe 4 兼容的游戏引擎
* [Armory (Kha)](https://github.com/armory3d/armory) - 一个开源 3D 游戏引擎，与 Blender 完全集成（“Web”、“Mobile”、“Desktop”、“Consoles”）。
* [Away3D](https://github.com/openfl/away3d) - OpenFL 的开源实时 3D 引擎（“Web”、“Mobile”、“Desktop”）。
* [ceramic](https://github.com/ceramic-engine/ceramic) - 跨平台 2D 框架（“Web”、“Mobile”、“Desktop”、“Unity”）。
* [HaxeFlixel (OpenFL)](https://github.com/HaxeFlixel/flixel) - 由 OpenFL 提供支持的免费跨平台 2D 游戏引擎（“Web”、“Mobile”、“Desktop”、“Consoles”）。
* [Haxegon (OpenFL)](https://github.com/haxegon/haxegon) - 适合初学者的编程库。由 OpenFL 和 Starling（“Web”、“移动”、“桌面”、“控制台”）提供支持。
* [Heaps](https://github.com/HeapsIO/heaps) - 高性能游戏框架（“Web”、“移动”、“桌面”、“控制台”）。
* [hxdefold](https://github.com/hxdefold/hxdefold) - Defold 游戏引擎的 Haxe/Lua 外部（`Web`、`Mobile`、`Desktop`）。
* [OpenFL](https://github.com/openfl/openfl) - 交互式游戏和应用程序开发库（“Web”、“Mobile”、“Desktop”、“Consoles”）。
* [Starling](https://github.com/openfl/starling) - “跨平台游戏引擎”，一种流行的 Stage3D 框架（“Web”、“Mobile”、“Desktop”）。
* [Stencyl (OpenFL)](https://github.com/Stencyl/stencyl-engine) - 无需代码即可创建 Flash、HTML5、iOS、Android 和桌面游戏（“移动”、“桌面”）。
* [unreal.hx](https://github.com/proletariatgames/unreal.hx) - Haxe 虚幻集成（“Web”、“移动”、“桌面”、“控制台”）。
* [HxGodot (Godot 4.0)](https://github.com/HxGodot/hxgodot) - Godot 4 的 Haxe GDExtension（“Web”、“Mobile”、“Desktop”、“Consoles”）。

## 低级引擎
* [Kha](https://github.com/Kode/Kha) - 超便携、高性能、开源多媒体框架（“Web”、“Mobile”、“Desktop”、“Consoles”）。
* [Lime](https://github.com/openfl/lime) - 为 Haxe 跨平台开发人员（“Web”、“移动”、“桌面”）提供灵活、轻量级的层。
* [linc_glfw](https://github.com/Sunjammer/linc_glfw) - 桌面 - GLFW 绑定（OpenGL、OpenGL ES 和 Vulkan 的多平台库）_（桌面）_。
* [NME](https://github.com/haxenme/nme) - 跨平台本机后端（“Web”、“Mobile”、“Desktop”）。
* [3DSHaxe](https://github.com/Krismowo/3DSHaxe) - 制作 3ds 自制软件！ （`3DS`）。

## 物理学
* [echo](https://github.com/AustinEast/echo/) - 简单物理库。
* [haxebullet](https://github.com/armory3d/haxebullet) - 子弹 3D 物理。
* [nape-haxe4](https://github.com/HaxeFlixel/nape-haxe4) - 物理引擎（颈背的原始 Haxe3 版本可以在[此处](https://github.com/deltaluca/nape)找到）。



## 建筑
```
IoC == Inversion of Control  
EC == Entity Component  
ECS == Entity-Component-System
FSM == Finite State Machine
MVC == Model View Controller
```

* [awe6](https://github.com/hypersurge/awe6) - `IoC`、`EC` - 倒置游戏框架，是一个专注于 Future Proofing 的开发工具。
* [ecx](https://github.com/eliasku/ecx) - `ECS` - 实体组件系统框架。
* [hexMachina](https://github.com/DoclerLabs/hexCore) - `MVC` - 一个强大的多模块 MVC 框架。
* [OSIS](https://github.com/Dvergar/OSIS) - `ECS` - 具有网络支持的实体组件系统架构。


## 网络
* [Anette](https://github.com/Dvergar/Anette) - 简单的网络库（无UDP）。
* [colyseus-hx](https://github.com/colyseus/colyseus-hx) - 多人游戏客户端。
* [haxe-simple-peer (js)](https://github.com/melonin/haxe-simple-peer) - Haxe externs 用于简单对等。
* [hxWebSockets](https://github.com/ianharrigan/hxWebSockets) - 适用于所有平台的 Websocket。
* 内置 - Heaps、OpenFL (HaxeFlixel & co)、Kha (Armory)。


## 序列化和存储
* [Bits](https://github.com/RealyUniqueName/Bits) - 具有无限数量位的二进制位标志。
* [CastleDB](https://github.com/ncannasse/castle) - 结构化静态数据库简化了协作。
* [hxbit](https://github.com/ncannasse/hxbit) - 二进制序列化和网络同步库。
* [PODStream](https://github.com/Dvergar/PODStream) - 普通旧数据序列化器。



<!--lint disable awesome-list-item-->
## 游戏
* [Darksburg](https://store.steampowered.com/app/939100/Darksburg/) - 堆-“桌面”。
* ![截图](https://raw.githubusercontent.com/Dvergar/awesome-haxe-gamedev/main/images/darksburg.jpg)
* [Dead Cells](https://dead-cells.com/) - 堆 - “桌面”、“控制台”。
* ![截图](https://raw.githubusercontent.com/Dvergar/awesome-haxe-gamedev/main/images/dead-cells.jpg)
* [Defender's Quest](http://www.defendersquest.com/) - HaxeFlixel (OpenFL) - `桌面`、`控制台`。
* ![截图](https://raw.githubusercontent.com/Dvergar/awesome-haxe-gamedev/main/images/defenders-quest.jpg)
* [Defender's Quest 2](https://store.steampowered.com/app/252190/Defenders_Quest_2_Mists_of_Ruin/) - HaxeFlixel (OpenFL) - `桌面`。
* ![截图](https://raw.githubusercontent.com/Dvergar/awesome-haxe-gamedev/main/images/defenders-quest-2.jpg)
* [Dicey Dungeons](http://diceydungeons.com/) - Haxegon (OpenFL) - “桌面”、“控制台”。
* ![截图](https://raw.githubusercontent.com/Dvergar/awesome-haxe-gamedev/main/images/dicey-dungeons.jpg)
* [Evoland](http://evoland.shirogames.com/) - 堆 - “桌面”、“移动”。
* ![截图](https://raw.githubusercontent.com/Dvergar/awesome-haxe-gamedev/main/images/evoland.jpg)
* [Northgard](http://northgard.net/) - 堆-“桌面”。
* ![截图](https://raw.githubusercontent.com/Dvergar/awesome-haxe-gamedev/main/images/northgard.jpg)
* [Papers, Please](http://papersplea.se/) - OpenFL -“桌面”、“iOS”、“PsVita”。
* ![截图](https://raw.githubusercontent.com/Dvergar/awesome-haxe-gamedev/main/images/papers-please.jpg)
* [Pocket Kingdom](https://store.steampowered.com/app/462620/Pocket_Kingdom/) - HaxePunk (OpenFL)-“桌面”。
* ![截图](https://raw.githubusercontent.com/Dvergar/awesome-haxe-gamedev/main/images/pocket-kingdom.jpg)
* [rymdkapsel](https://rymdkapsel.com/) - OpenFL -“桌面”、“移动”。
* ![截图](https://raw.githubusercontent.com/Dvergar/awesome-haxe-gamedev/main/images/rymdkapsel.jpg)
* [Spellbreak](https://playspellbreak.com/) - unreal.hx - `PC`、`PS`、`Xbox`、`Switch`。
* ![截图](https://raw.githubusercontent.com/Dvergar/awesome-haxe-gamedev/main/images/spellbreak.jpg)
* [The Westport Independent](http://www.doublezeroonezero.com/westport.html) - 豪华 - “桌面”、“移动”。
* ![截图](https://raw.githubusercontent.com/Dvergar/awesome-haxe-gamedev/main/images/westport-independent.jpg)
<!--lint enable-->


更多展示：
* [OpenFL 展示](https://www.openfl.org/showcase)
* [HaxeFlixel 展示](https://haxeflixel.com/showcase/)
* [itch.io 展示](https://itch.io/games/made-with-haxe)
* [HaxePunk 展示](https://haxepunk.com/games/)
* [火焰展示柜](https://github.com/aduros/flambe/wiki/Showcase)
* [卡展示](https://github.com/Kode/Kha/wiki/Games-Built-With-Kha)

## 杂项

### 3rd 方 API
* [SteamWrap](https://github.com/larsiusprime/SteamWrap) - SteamAPI 的本机扩展。
* [newgrounds](https://lib.haxe.org/p/newgrounds) - Newgrounds API。
* [hxgamejolt-api](https://github.com/MAJigsaw77/hxgamejolt-api) - GameJolt API 的 Haxe 绑定。

### 人工智能
[goap](https://gitlab.com/haath/goap) - 面向目标的人工智能行动规划器。

### 动画
* [spine-hx](https://github.com/jeremyfa/spine-hx) - Spine 运行时自动从官方 Java/libgdx 运行时转换而来。
* HaxeFlixel - Spine 解析器。
* [Heaps-Spine](https://github.com/Beeblerox/Heaps-Spine) - 堆的脊椎播放器。
* [heaps-aseprite](https://github.com/AustinEast/heaps-aseprite) - 以 Aseprite 格式加载和渲染精灵和动画。
* [openfl-aseprite](https://github.com/miriti/openfl-aseprite) - 以 Aseprite 格式加载和渲染精灵和动画。
* [openfl-spine](https://github.com/rainyt/openfl-spine) - 在OpenFL引擎中渲染Spine动画，可以通过Sprite和Tilemap来实现渲染处理。
* [ase](https://github.com/miriti/ase) - .ase/.aseprite 的文件格式读取器/写入器，无需外部依赖项。
* [flxgif](https://github.com/MAJigsaw77/flxgif) - Yagp 的 HaxeFlixel 的 Gif 播放器。

### 音频
* [sfxr-hx](https://github.com/jobf/sfxr-hx) - Sfxr 的纯 haxe 实现。

### 色彩处理
* [nxColor](https://github.com/oscarcs/nxColor) - 颜色处理库。

### 碰撞
* [differ](https://github.com/snowkit/differ) - 分离轴定理碰撞库。

### 计算机视觉
* [Vision](https://github.com/ShaharMS/Vision) - 跨平台计算机视觉库。

### 数据结构
* [polygonal-ds](https://github.com/polygonal/ds) - 游戏的数据结构。

### 对话
* [hxyarn](https://github.com/cxsquared/hxyarn) - Yarn 对话文件的解析器和运行器。

### 编辑
* [flixel-studio](https://github.com/Dovyski/flixel-studio) - HaxeFlixel 的游戏内编辑器。

### 帮手
* [deepnightLibs](https://github.com/deepnight/deepnightLibs) - 通用游戏开发目的库。

### 本地化
* [firetongue](https://github.com/larsiusprime/firetongue) - 翻译/本地化框架。

### 地图解析器
* [PyxelEdit Map Importer](https://github.com/Dvergar/PyxelEdit-Map-Importer) - 由编辑器 PyxelEdit 生成的地图的解析器。
* Heaps - Tiled 的内置解析器。
* HaxeFlixel - Tiled 和 Ogmo 的解析器。
* [LEd](https://github.com/deepnight/led-haxe-api) - 带有类型化编译时加载器的 2D 关卡编辑器。
* [TiledHX](https://github.com/yanrishatum/tiledhx) - 一个全面的现代 Tiled 解析器。

### 数学助手
* [hxmath](https://github.com/tbrosman/hxmath) - 面向游戏的数学库。
* [haxe-glm](https://github.com/hamaluik/haxe-glm) - 用于使用 2、3 和 4 维向量和矩阵以及四元数的工具集。
* [hx-vector2d](https://github.com/markknol/hx-vector2d) - 世界上最完整的 Vector2d / Point 类。具有运算符重载。

### 改装
* [polymod](https://github.com/larsiusprime/polymod) - 游戏/应用程序的原子模组框架。

### 颗粒
* [Sparkler](https://github.com/RudenkoArts/sparkler) - 模块化粒子系统。

### 货币化
* [extension-iap](https://github.com/charmdev/extension-iap) - 使用通用 API 为 OpenFL 项目提供应用内购买 (iOS) 和应用内计费 (Android) 的访问权限。 [this](https://github.com/HaxeExtension/extension-iap) 的分叉。

### 寻路
* [pathfinder](https://github.com/hypersurge/pathfinder) - 简单的 A* 寻路算法。
* [astar](https://gitlab.com/haath/astar) - 与框架无关的多功能 A-star 求解器库。

### 程序生成
* [Dungeon builder](https://github.com/julsam/dungeon-builder) - 一组地下城生成算法（适用于 hx4，略有改动）。

### 着色器
* [HGSL](https://github.com/saharan/HGSL) - Haxe 到 GL 着色语言。
* [parasol](https://github.com/47rooks/parasol) - HaxeFlixel 着色器库。

### 雪碧
* [haxe-aseprite](https://github.com/PongoEngine/haxe-aseprite) - .ase 和 .aseprite 文件的解析器。

### 纹理打包器
* [hxpk](https://github.com/bendmorris/hxpk) - libGDX 纹理打包器的端口。

### 补间
* [actuate](https://github.com/jgranick/actuate) - 灵活、快速的“补间”库。
* [YATL](https://github.com/Yanrishatum/yatl) - 另一个（Haxe）补间库。
* [TweenX/TweenXCore](https://github.com/shohei909/tweenx) - 吐温库。

### 用户界面
* [domkit](https://github.com/ncannasse/domkit) - 基于 CSS 组件的严格类型 UI 框架。
* [flixel-ui](https://github.com/HaxeFlixel/flixel-ui) - HaxeFlixel 的 GUI 库。
* [HaxeUI](http://haxeui.org/) - 具有多个框架后端的 UI 库（HTML5、Kha、OpenFL、PixiJS、WxWidgets 以及许多其他正在进行的工作）。
* [Feathers UI](https://feathersui.com/) - 用于创意前端项目的跨平台图形用户界面组件。

### 视频
* [hxCodec](https://github.com/polybiusproxy/hxCodec) - 添加 HaxeFlixel 和 OpenFL 上的本机视频播放。

## 文章
* [Flash已死，OpenFL万岁！](http://gamasutra.com/blogs/LarsDoucet/20140318/213407/Flash_is_dead_long_live_OpenFL.php)
* [闪光灯不见了，怎么办？](https://www.linkedin.com/pulse/flash-gone-what-now-matan-uberstein/)
* [我如何编写自己的 3D 游戏引擎并在 20 个月内发布一款游戏](https://kircode.com/post/how-i-wrote-my-own-3d-game-engine-and-shipped-a-game-with-it-in-20-months)
* [一年内开发 42 款游戏 — 疯狂的游戏开发](https://medium.com/@mknol/building-42-games-within-a-year-insane-game-development-5340d506068f)
* [通过 Unity 移植到控制台](https://do-games.com/blog/the-adventure-pals-console-tech-part1)

## 其他 haxe 列表
* [很棒的哈克斯](https://github.com/nadako/awesome-haxe)
* [很棒的雪具](https://github.com/anissen/awesome-snowkit)
* [很棒的 haxe js](https://github.com/MatthijsKamstra/awesome-haxe-js)
