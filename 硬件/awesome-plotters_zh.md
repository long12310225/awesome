# 很棒的绘图仪 [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

计算机控制绘图机和其他视觉艺术机器人的代码和资源的精选列表。

## 内容

- [开始使用](#getting-started)
- [Hardware](#hardware)
  - [Plotters](#plotters)
  - [电机控制器](#motor-controllers)
  - [配件和适配器](#accessories-and-adapters)
  - [Pens](#pens)
- [Software](#software)
  - [HPGL](#hpgl)
  - [G-code](#g-code)
  - [绘图仪控制](#plotter-control)
  - [矢量创建](#vector-creation)
  - [矢量实用程序](#vector-utilities)
  - [Fonts](#fonts)
- [灵感、指导和研究](#inspiration-instruction-and-research)
- [手册、蜉蝣、论文和专利](#manuals-ephemera-papers-and-patents)
  - [Manuals](#manuals)
  - [Ephemera](#ephemera)
  - [Papers](#papers)
  - [Patents](#patents)
- [Courses](#courses)
- [Community](#community)
- [绘图仪艺术品出售](#plotter-art-for-sale)
- [其他很棒的东西](#other-awesomes)

## 开始使用

一系列简短的资源可帮助您开始使用笔式绘图仪。

- [What is a pen plotter 2022?](https://www.youtube.com/watch?v=J1NpYzETm3M) - 关于 2022 年现代绘图仪的精彩视频介绍。
- [An Intro to Pen Plotters](https://medium.com/quarterstudio/an-intro-to-pen-plotters-29b6bd4327ba) - 有关旧 HPGL 绘图仪入门的好信息。
- [An Introduction to Pen Plotting](https://mrmrs.cc/writing/pen-plotting-intro/) - 另一篇有关现代笔式绘图仪的入门文章。
- [Pen Plotter Programming: The Basics](https://medium.com/@fogleman/pen-plotter-programming-the-basics-ec0407ab5929) - 向量路径编程的一些基础知识，包括排序、连接和简化。
- [Pen Plotter Art & Algorithms](https://mattdesl.svbtle.com/pen-plotter-1) - 介绍如何创建用于绘图的生成图形，分为两部分。
- [How to Draw Generative Art with an Axidraw Pen Plotter](https://www.dirtalleydesign.com/blogs/news/how-to-draw-prints-with-an-axidraw-pen-plotter) - 许多不错的提示（并非全部针对 Axidraw），还有一些钢笔评论和方便的 3D 打印工具。

## 硬件

### 绘图仪

笔式绘图仪可用于构建或购买、历史信息和修复项目。

- [AxiDraw](https://shop.evilmadscientist.com/productsmenu/846) - 来自邪恶疯狂科学家的笔式绘图仪。
- [NextDraw](https://bantamtools.com/collections/bantam-tools-nextdraw) - 新的 AxiDraw，现在来自 Bantam Tools。
- [ArtFrame](https://bantamtools.com/collections/artframe) - Bantam Tools 的强大平板笔式绘图仪。
- [Line-us](https://www.line-us.com) - 一个可爱的小启动机器人绘图臂。
- [Drawing Robot](https://www.thingiverse.com/thing:2349232) - 3D 可打印 AxiDraw 克隆，带有运行 grbl 固件的 Arduino CNC Shield 控制器。
- [4xiDraw](https://www.instructables.com/id/4xiDraw/) - 另一个可 3D 打印的 AxiDraw 克隆，带有运行 grbl 固件的 Arduino CNC Shield 控制器。
- [WaterColorBot](https://watercolorbot.com) - XY 艺术机器人和用水彩颜料绘图的软件。
- [EggBot](https://egg-bot.com) - 用于蛋形和球形物体的笔式绘图仪。
- [HP Pen Plotters](https://www.hpmuseum.net/exhibit.php?class=4&cat=24) - 来自 HPGL 标准创建者的老式台式和落地笔式绘图仪。 7475A 型号非常常见，通常可以在 eBay 上找到。
- [Roland Pen Plotters](https://www.youtube.com/watch?v=6_pwzqPk6Gg) - 老式平板 HPGL 笔式绘图仪。在 eBay 上搜索“roland dxy”。
- [Blot](https://blot.hackclub.com) - 来自 Hack Club 的开源 DIY 笔式绘图仪，带有基于浏览器的生成艺术编辑器。
- [BrachioGraph](https://www.brachiograph.art) - 一款廉价而简单的绘图仪，由操纵杆、伺服系统和运行 Python 的 Raspberry Pi 制成。这是来自创建者的 [PyCon UK 上的 BrachioGraph 演讲视频](https://www.youtube.com/watch?v=u4Jh1daCl60)。
- [Arduino CNC Drawing Machine](https://www.diymachines.co.uk/arduino-cnc-drawing-machine) - 一个相当简单的 3D 打印 AxiDraw 风格绘图仪，具有良好的视频文档。
- [PlotterXY](https://github.com/jamescarruthers/PlotterXY) - coreXY 绘图仪由挤压件、3D 打印部件和廉价的 3D 打印机控制板制成。
- [NextDraw](https://store.bantamtools.com/collections/bantam-tools-nextdraw) - [Bantam Tools](https://www.bantamtools.com) 是流行的 AxiDraw 笔式绘图仪的后继者。
- [openBrushograph](https://github.com/openBrushograph/openBrushograph_hardware) - 开源可 3D 打印 XY 龙门架和 Z 平台，专为自动画笔和钢笔绘画而设计。
- [Lego-Pen-Plotter](https://github.com/Jormono1/Lego-Pen-Plotter) - 笔式绘图仪完全由乐高积木构建，并使用 PyBricks 和 Python 进行编程。
- [Makelangelo 5](https://www.marginallyclever.com/products/makelangelo-5/) - Polargraph 机器人可以在墙壁、窗户或画架上绘图。
- [复兴 Apple 410 彩色绘图仪](https://www.nycresistor.com/2017/12/13/reviving-the-apple-410-color-plotter/)
- [Apple-410](https://github.com/phooky/Apple-410) - Apple 410 彩色绘图仪文档、驱动程序和 ROM 转储。

### 电机控制器

用于驱动步进电机和控制笔式绘图仪的硬件。

- [grblShield](https://github.com/synthetos/grblShield) - 使用 grbl 固件将 [Arduino](https://www.arduino.cc) 转变为基于 G 代码的运动控制器所需的所有步进电机控制硬件。 ([adafruit](https://www.adafruit.com/product/1750))
- [TinyG](https://github.com/synthetos/TinyG) - 功能更强大、更强大的基于 G 代码的 6 轴运动控制硬件。 ([adafruit](https://www.adafruit.com/product/1749))
- [Arduino CNC Shield](https://blog.protoneer.co.nz/arduino-cnc-shield) - 适用于 Arduino 的 Grbl 兼容步进电机控制扩展板，类似于 grblShield。
- [Raspberry Pi CNC Hat](https://wiki.protoneer.co.nz/Raspberry_Pi_CNC) - 带有步进控制器和运行 grbl 的微控制器的 Raspberry Pi 附加板。与 Pi 的串行引脚接口。
- [EBB Driver Board](https://shop.evilmadscientist.com/productsmenu/188) - 基于 USB 的双步进电机控制器板，最初为 EggBot 设计。

### 配件和适配器

电缆、串行适配器和替换零件。

- [WiFi232](http://biosrhythm.com/?page_id=1453) - 通过 DB25 插头将 Wifi 转为 RS-232 串行。无线控制您的串行绘图仪。
- [Plotter Cable Pinout](http://sites.music.columbia.edu/cmc/chiplotle/plotter_cable.pdf) - 适用于大多数 HP 和 Roland 绘图仪的绘图仪电缆示意图。在 eBay 或 Amazon 上搜索“DB9 至 DB25 串行零调制解调器电缆”或类似产品，即可找到待售产品。
- [PlotAdapter](https://github.com/rhalkyard/plotadapter) - “HP 绘图仪的串行 GPIB 转换器”使用 Arduino 微控制器将串行 HPGL 转换为某些旧 HP 绘图仪所期望的 GPIB/HP-IB。
- [Replacement Pen Carousel Turret Carriage Holder for HP 7475A Plotter](https://obsoletetech.us/products/replacement-pen-carousel-turret-carriage-holder-for-hp-7475a-plotter) - 3D 打印替换零件。
- [Replacement Geneva Drive Wheel Gear for HP 7475A Plotter Pen Carousel](https://obsoletetech.us/products/replacement-geneva-drive-wheel-gear-for-hp-7475a-plotter-pen-carousel) - 3D 打印的常见损坏零件的替代品。

### 钢笔

笔适配器、安装座和建议。

- [Sharpie Fine Point Plotter Adapter](https://www.printables.com/model/156721-sharpie-fine-point-plotter-adapter) - 3D 打印适配器，用于将标准 Sharpie 装入 HP-GL 绘图仪中。
- [Parametric 3d-Printable Plotter Pen Adapter](https://openjscad.xyz/#https://gist.githubusercontent.com/beardicus/d668c0f6b96be53d16dc/raw/plotter-pen-adapter.jscad) - 适用于各种笔的可调节模型打印适配器。
- [Plotter Pen STL Models](https://www.printables.com/model/156722-plotter-pen) - 短标准绘图笔和长标准绘图笔的精确 STL 模型。
- [Pens for AxiDraw](https://wiki.evilmadscientist.com/Pens_for_AxiDraw) - 适合一般绘图仪滥用的笔列表。
- [Pens for EggBot](https://wiki.evilmadscientist.com/Pen_choices) - 以鸡蛋和玻璃为重点的笔建议，但仍然普遍适用的信息。
- [JetPens - The Best White Ink Pens](https://www.jetpens.com/blog/The-Best-White-Ink-Pens/pt/340) - 对许多白色墨水笔的全面回顾，并附有其覆盖特性的图片。

## 软件

### HPGL

HPGL 是大多数旧笔式绘图仪和许多新乙烯基切割机使用的基于文本的协议。

- [Chiplotle](https://github.com/drepetto/chiplotle) - 用于生成 HPGL 并与串行绘图仪连接的 Python 库。
- [Chiplotle3](https://github.com/cyprienh/chiplotle3) - Chiplotle 分支已更新以实现 Python 3.x 兼容性。
- [HPGL Reference Guide](https://www.isoplotec.co.jp/HPGL/eHPGL.htm) - 基于 HTML 的 HPGL 参考。
- [HP 7475A Interfacing and Programming Manual](https://archive.org/details/HP7475AInterfacingandProgrammingManual) - 包含完整 HPGL 参考的扫描 PDF 手册。
- [djipco/hpgl](https://github.com/djipco/hpgl) - 一个 Node.js 库，用于与 HPGL 兼容的绘图仪和打印机进行通信。
- [hp2xx](https://www.gnu.org/software/hp2xx) - 用于将 HPGL 转换为其他矢量和光栅格式的 GNU 工具。也可以用作X11中的预览。
- [vec](https://github.com/anachrocomputer/vec) - 用于生成带有海龟图形界面的 HPGL 的示例 C 代码。
- [d3-hpgl](https://github.com/aubergene/d3-hpgl) - HTML Canvas API 的适配器，以便您可以使用流行的 [D3](https://d3js.org) 库输出 HPGL。
- [HPGL Viewer](https://github.com/drskullster/HPGLViewer) - 使用 JavaScript 和 HTML5 画布的 HPGL 查看器。
- [HPGL Sender](https://github.com/LgHS/hpgl-sender) - 用于预览 HPGL 并将其发送到绘图仪的 Web 界面。
- [HPGLGraphics](https://github.com/ciaron/HPGLGraphics) - 用于编写 HPGL 文件的处理库。
- [processing2hpgl](https://github.com/awdriggs/processing2hpgl) - 一个处理库，允许在处理草图中与 HPGL 笔式绘图仪直接通信。

### G代码

G 代码是用于控制 CNC 机床的基于文本的标准。尽管它是为工业机器设计的，但它在许多爱好者 3D 打印机固件中的使用使其在小型 DIY 项目中也无处不在。

- [grbl](https://github.com/grbl/grbl) - 适用于 Atmega 328 微控制器和 Arduino 的高性能 G 代码解释固件。
- [cncjs](https://github.com/cncjs/cncjs) - 基于网络的界面，控制运行 grbl、TinyG 或其他基于 G 代码的固件的 CNC 机器。
- [node-gcode](https://github.com/ryansturmer/node-gcode) - Node.js G 代码解释器和模拟器。
- [svg2gcode](https://github.com/em/svg2gcode) - 用于将 SVG 转换为 G 代码的 Node.js 命令行实用程序。
- [svg2gcode](https://github.com/vishpat/svg2gcode) - 用于将 SVG 快速转换为 G 代码的 Python 实用程序。
- [jscut](http://jscut.org/) - 一个基于 Web 的实用程序，用于将 SVG 转换为 G 代码。
- [Universal-G-Code-Sender](https://github.com/winder/Universal-G-Code-Sender) - 基于 Java 的 grbl 兼容跨平台 G 代码发送器。
- [ChiliPeppr Hardware Fiddle](http://chilipeppr.com) - 基于网络的模块化工作区，用于可视化 G 代码和控制硬件。
- [gcode-generative-for-processing](https://github.com/o0morgan0o/gcode-generative-for-processing) - 处理库，旨在从简单的形状创建 gcode。 （专为与 Creality CR10 配合使用而设计）
- [gcodeplot](https://github.com/arpruss/gcodeplot) - 用于将 SVG 和 HPGL 转换为 3 轴 CNC 机床的 G 代码的 Python 实用程序。
- [fabnodes](https://extensions.blender.org/add-ons/fabnodes/) - Blender 插件可将几何节点刀具路径导出为 G 代码。

### 绘图仪控制

用于控制绘图仪硬件的软件。

- [axidraw](https://github.com/evil-mad/axidraw) - Inkscape 的官方 AxiDraw 扩展。
- [axi](https://github.com/fogleman/axi) - AxiDraw v3 的非官方 Python 库。
- [bCNC](https://github.com/vlachoudis/bCNC) - grbl 的跨平台 G 代码发送器和 CNC 控制软件。
- [xy](https://github.com/fogleman/xy) - Makeblock XY 绘图仪机器人套件的​​实用程序。
- [LaserGRBL](https://github.com/arkypita/LaserGRBL) - 适用于 grbl 控制器的激光优化 Windows GUI。可重新用于 DIY 笔式绘图仪，使用螺线管进行笔向上/向下运动。
- [Line-us Inkscape Plugin](https://github.com/Line-us/Inkscape-Plugin) - 直接从 Inkscape 将绘图发送到 Line-us 绘图仪。
- [Line-us API Examples](https://github.com/Line-us/Line-us-Programming) - Line-us 绘图仪基于 G 代码的 API 的示例代码。
- [@beardicus/line-us](https://github.com/beardicus/line-us) - 用于从 Node 或浏览器控制 Line-us 机器的 JavaScript 库。
- [PenPlotter](https://github.com/RickMcConney/PenPlotter) - 使用重复器固件的极谱仪控制器。
- [Makelangelo-firmware](https://github.com/MarginallyClever/Makelangelo-firmware) - Makelangelo 极坐标图机器人的固件。
- [RoboPaint](https://github.com/evil-mad/robopaint) - WaterColorBot 软件。
- [AxiTurtle](https://github.com/ralphcrutzen/AxiTurtle) - 处理中 AxiDraw 的海龟图形。
- [GRBL-Plotter](https://github.com/svenhb/GRBL-Plotter) - 绘图仪优化的适用于 grbl 控制器的 Windows GUI，具有 SVG 和 DXF 导入功能，以及灵活的笔向上/向下控制。
- [saxi](https://github.com/nornagon/saxi) - AxiDraw 的驱动程序和库。使用恒定加速度运动规划并自动调整纸张大小。
- [MP2300-Tools](https://github.com/Jan--Henrik/MP2300-Tools) - 用于将 HPGL 转换为 Graphtec 的 GPGL 格式的软件，以及用于 Graphtec 绘图仪笔适配器的 CAD 文件。
- [Inkcut](https://github.com/inkcut/inkcut) - 用于控制 2D 绘图仪、切割机、雕刻机和 CNC 机器的应用程序。
- [plottie](https://github.com/mossblaser/plottie) - 用于通过 SVG 输入控制 Silhouette 绘图仪和切割机的命令行工具。
- [py_silhouette](https://github.com/mossblaser/py_silhouette) - 用于控制 Silhouette 绘图仪和切割机的 Python 库。
- [pypenwriter](https://github.com/Lana-chan/pypenwriter) - 用于转换 SVG 绘图并将其发送到 Panasonic PenWriter 系列打字机绘图仪的 Python 脚本。

### 矢量创建

从头开始或通过从其他格式转换来创建矢量图稿的工具。

- [Inkscape](https://inkscape.org) - 流行的跨平台开源矢量图形编辑器。
- [p5.js](https://p5js.org) - “JavaScript 库使艺术家、设计师、教育工作者和初学者可以轻松编码”。
- [Paper.js](http://paperjs.org) - “矢量图形脚本的瑞士军刀”。
- [ln](https://github.com/fogleman/ln) - 用 Go 编写的基于矢量的 3D 渲染器。
- [autotrace](https://github.com/autotrace/autotrace) - 将位图图像转换为矢量图形。
- [stipplegen](https://github.com/evil-mad/stipplegen) - 从位图图像创建有趣的点画图画。 （[博客文章](https://www.evilmadscientist.com/2012/stipplegen2)）
- [SquiggleDraw](https://github.com/gwygonik/SquiggleDraw/commits/master) - “SquiggleDraw 将从图像创建 SVG 文件，使用亮度来改变正弦波的幅度”。
- [svgurt](https://svgurt.com) - 基于网络的 PNG 到 SVG 创意面条机。
- [maptrace](https://github.com/mzucker/maptrace) - 通过跟踪光栅图像生成无懈可击的多边形矢量图。
- [Drawbot_image_to_gcode_v2](https://github.com/Scott-Cooper/Drawbot_image_to_gcode_v2) - 创建用于绘图机器人的 G 代码。
- [blackstripes](https://github.com/fullscreennl/blackstripes-python-extensions) - 将 PNG 图像转换为 SVG 线条图。
- [penplot](https://github.com/mattdesl/penplot) - JavaScript 绘图仪艺术的开发环境。
- [penkit](https://github.com/paulgb/penkit) - 用于创建基于线条的 SVG 图形的 Python 库。
- [generativeExamples](https://github.com/digitalcoleman/generativeExamples) - 生成可绘制 PDF 的示例处理代码。
- [Let's make map](https://svg-exporter.netlify.app) - 用于从 Mapzen 切片导出 SVG 地图的基于 Web 的工具。
- [LineDream](https://linedream.marcrleonard.com/) - 可以导出 SVG 的 Python 生成艺术库。
- [SuperformulaSVG for web](https://jasonwebb.github.io/SuperformulaSVG-for-web) - 生成线条艺术网络应用程序。
- [scribbleplot](https://github.com/bleeptrack/scribbleplot) - 处理中的乱写图像转换。
- [Maker.js](https://maker.js.org) - 用于为 CNC 和激光切割机创建 2D 矢量绘图的库。
- [Turtletoy](https://turtletoy.net) - 基于浏览器的 JavaScript 海龟图形 API，具有 SVG 导出功能。
- [cozyvec](https://github.com/brubsby/cozyvec) - 用于绘图仪艺术和推文绘图的 Web/独立终端环境。
- [makio135/plotter](https://observablehq.com/collection/@makio135/plotter) - 一个 [Observable](https://observablehq.com/) 笔记本集合，充满了面向绘图仪的工作。
- [PlotterFun](https://mitxela.com/plotterfun/) - 基于浏览器的图像到 SVG 转换器，类似于 SquiggleDraw。
- [SVG.js](https://svgjs.dev/) - 用于创建、操作和动画 SVG 的无依赖轻量级库。
- [Components AI](https://components.ai/) - 用于探索生成空间的实验计算设计平台。
- [DrawingBotV3](https://github.com/SonarSonic/DrawingBotV3) - 用于将图像转换为线条图的跨平台软件。
- [linedraw](https://github.com/LingDong-/linedraw) - 用于将图像转换为粗略矢量线图的 Python 工具。
- [plotter.vision](https://plotter.vision/) - 用于删除 STL 文件隐藏线以生成可绘制 SVG 的交互式网站。还支持红/蓝 3D 眼镜。
- [plotting-maps](https://github.com/piebro/plotting-maps) - 一个简单的 Web 工具，用于创建 OpenStreetMap SVG 地图以进行绘图。
- [ThreadPlotter](https://github.com/LiciaHe/threadPlotter) - “使用 X-Y 绘图仪设计和制作精致的打孔针刺绣的工具包”。
- [PINTR](https://javier.xyz/pintr) - 从图像中绘制随机线条图。
- [REVDANCATT Plotter Tools](https://revdancatt.com/penplotter/) - 一堆基于 Web 的笔式绘图仪工具，具有 SVG 输出。
- [Flow Lines](https://msurguy.github.io/flow-lines/) - 使用 SVG 路径/折线生成流线表示的工具。
- [UJI](https://doersino.github.io/uji/) - 一个基于网络的生成艺术，具有 SVG 导出功能。
- [Rad Lines](https://msurguy.github.io/rad-lines/) - 一个基于 Web 的径向线矢量生成工具，具有 SVG 导出功能。
- [Peak Map](https://anvaka.github.io/peak-map/) - 一个基于网络的工具，用于从地图数据生成山脊折线图。

### 矢量实用程序

用于操作和优化基于矢量的文件格式的工具。

- [svgsort](https://github.com/inconvergent/svgsort) - 绘制 SVG 文件的路径规划可减少提笔移动的时间。
- [svgoutline](https://github.com/mossblaser/svgoutline) - 用于从 SVG 中提取笔画和轮廓作为线段的 Python 库。
- [svgo](https://github.com/svg/svgo) - 基于 Node.js 的工具，用于优化 SVG 文件。
- [Polargraph Optimizer](https://github.com/ezheidtmann/polargraph-optimizer) - 优化极坐标图的绘制计划。
- [penkit-optimize](https://github.com/paulgb/penkit/tree/master/optimizer) - 一个 SVG 优化器，使用车辆路径求解器来最大限度地减少绘图时间。
- [svg-crowbar](https://github.com/NYTimes/svg-crowbar) - 仅适用于 Chrome 的书签，用于从 HTML 文档中提取 SVG。
- [vpype](https://github.com/abey79/vpype) - 以绘图仪为中心的基于 Python 的 CLI 实用程序，用于生成和操作 SVG，包括缩放和优化路径。
- [SVG Cropper](https://msurguy.github.io/svg-cropper-tool/) - 一种基于浏览器的工具，用于使用不同的基元、自定义形状或其他 SVG 裁剪 SVG。

### 字体

单行矢量字体或“雕刻字体”。

- [Summary of single line fonts](http://imajeenyus.com/computer/20150110_single_line_fonts/index.shtml) - 良好的信息以及其他资源和字体的链接。
- [Hershey Vector Font](http://paulbourke.net/dataformats/hershey) - 60 年代的矢量字体“.fnt”格式。包括对字体原始数据格式的良好概述。
- [hershey-fonts](https://github.com/kamalmostafa/hershey-fonts) - Hershey 字体的 C 库和原始字体数据。
- [svg-fonts](https://gitlab.com/oskay/svg-fonts) - SVG 格式的单行字体，主要与 [Hershey Text](https://gitlab.com/oskay/hershey-text) Inkscape 插件一起使用。
- [CNC Text Tool](https://msurguy.github.io/cnc-text-tool/) - 基于浏览器的好时文本工具，可导出为 SVG。
- [hf2gcode](https://github.com/Andy1978/hf2gcode) - 从具有 Hershey 字体的文本生成 G 代码。
- [FifteenTwenty: Commodore 1520 plotter font](https://github.com/scruss/FifteenTwenty) - [博客文章](https://scruss.com/blog/2016/04/23/fifteentwenty-commodore-1520-plotter-font/) 关于从原始 ROM 创建此字体的信息。
- [从尸体上拔牙：从 Apple 410 彩色绘图仪中提取矢量字体](https://www.nycresistor.com/2017/12/29/pulling-teeth-from-a-corpse-extracting-the-vector-font-from-the-apple-410-color-plotter/)

## 灵感、指导和研究

博客文章、文章、教程、图库、视频等等。

- [On Generative Algorithms](https://inconvergent.net/generative) - 由 13 部分组成的有趣算法的精彩演练。
- [Roland DG DXY-990](https://hackaday.io/project/12276-roland-dg-dxy-990) - 罗兰平板绘图仪快速入门指南。
- [The Cohen-Sutherland Line Clipping Algorithm](https://sighack.com/post/cohen-sutherland-line-clipping-algorithm) - 有趣算法的详细解释和示例。
- [Vera Molnár](https://www.surfacemag.com/articles/vera-molnar-in-thinking-machines-at-moma) - OG 绘图艺术家。
- [Hektor](http://juerglehni.com/works/hektor) - 2002 年最初的基于电缆的绘图机器人。
- [Surface Projection](https://nb.paulbutler.org/surface-projection/) - 使用 Python 和 penplot 深入研究表面投影和隐藏线去除。
- [Fractal Generation with L-Systems](https://nb.paulbutler.org/l-systems/) - 创建基于线的分形图形的技术。
- [Introduction to TSP art](https://wiki.evilmadscientist.com/TSP_art) - 旅行商问题（单路径）艺术资源。
- [Hidden wireframe removal](https://trmm.net/Hidden_Wireframe) - 用于删除 STL 文件线框的代码的讨论和链接。
- [The Best XY Plotters in 2020](https://all3dp.com/2/pen-plotters-best-xy-plotters/) - 对 AxiDraw 及其克隆的良好概述，以及一些 DIY 选项。
- [Orbis Tertius](https://www.glkitty.com/pages/orbistertius.html) - 带有火星地形绘图仪输出的沉浸式数字装置。
- [Tech Tangents: Plotting For The First Time - HP 7470A](https://www.youtube.com/watch?v=tk4c4WMZJZ8) - 精彩视频展示了通过 HP 85 计算机操作 HP 7470A。
- [CuriousMarc: HP 7475A Plotter and HPGL Demo](https://www.youtube.com/watch?v=Tr7Mbw9gLpk) - HP 7475A 绘制一些演示的视频。
- [CuriousMarc: Refilling or Replacing Vintage HP Plotter Pens](https://www.youtube.com/watch?v=h-oj4HrTH14) - 视频展示了如何打开、清洁和填充老式 HP 绘图笔。
- [Commodore 1520 Plotter Demonstration](https://www.youtube.com/watch?v=QwPTluBvKLU) - Commodore 1520 绘图仪运行的视频，包括该机构的掩护镜头。
- [Tech Tangents: Gold Standard Plotter - HP 7475A](https://www.youtube.com/watch?v=8785ktWD7vQ) - 该视频包含一些 HPGL 和绘图仪历史记录，以及通过 IBM 5160 微型计算机操作 HP 7475A。
- [curiousmarc.com: HP 7475A Plotter](https://www.curiousmarc.com/computing/hp-7475a-plotter) - 大量信息、蜉蝣、绘图文件、三个 YouTube 视频以及 HP 7475A 的 3D 打印替换部件。
- [From Lettering Guides to CNC Plotters](https://www.typotheque.com/articles/from-lettering-guides-to-cnc-plotters) - “技术刻字工具简史”。
- [Building an interactive plotter art installation](https://lostpixels.io/writings/building-interactive-plotter-art) - SIGGRAPH 2023 上交互式绘图仪艺术展的精彩文章（带视频）。
- [Taxan KPL 710 Demo Plot](https://www.youtube.com/watch?v=Xms3sZONQjo) - Taxan KPL 710 运行演示图的手持录音。
- [Sweet-P Six Shooter SP-600 Plotter Demonstration](https://www.youtube.com/watch?v=xE9LVOMbKxk) - Sweet-P SP-600 运行演示图的录音。
- [Bottle Plotter](https://vgnotepad.blogspot.com/2024/04/bottle-plotter.html) - 关于构建用于在酒瓶上绘图的圆柱形笔式绘图仪的博客文章。
- [Buildlog.net Atari 1020 Plotter Retrofit](https://www.buildlog.net/blog/2019/10/inktober-project-2019-post-5/) - 有关将 Atari 1020 绘图仪转换为使用基于 ESP32 的 GRBL 控制器的博客文章和视频。
- [Texas Instruments HX-1000 Plotter Photos](http://www.hexbus.com/TI-99_4A_Home_Computer_Page/Hexbus_HX-1000_Printer_Plotter.html) - 绘图仪外观、内部和包装的照片库。
- [Making cheap HP plotter pens](https://scruss.com/blog/2014/04/06/making-cheap-hp-plotter-pens-yet-another-hp-gl-viewer/) - 博客文章主要是关于使用乙烯基刀具部件作为笔架。
- [Marcel Schwittlick and The Long Run](https://www.artxcode.io/journal/marcel-schwittlick-the-long-run) - 对马塞尔的采访，以及他的工作和工作空间的大量照片和视频。
- [Lars Wander and Mixing Paint With Code](https://www.artxcode.io/journal/lars-wander-interview) - 拉斯·万德 (Lars Wander) 访谈，以及艺术作品和视频。
- [Flatulence, Crystals, and Happy Little Accidents by Nick Fitzgerald (RustConf 2019)](https://www.youtube.com/watch?v=Ho3xr4b60Zg) - RustConf 的演讲很少涉及 Rust，更多的是关于生成艺术和笔式绘图仪的创作过程。
- [Recreating Retro Plotter Art, by Sher Minn (Plotter People #1)](https://www.youtube.com/watch?v=OR_TzMFhv50) - 会议演讲涉及许多伟大的计算机和绘图仪历史。
- [20+ Questions About My Plotter Painting Practice](https://www.eyesofpanda.com/project/plotter_painting_q_a/) - 问答博客文章包含有关更多绘画绘图的大量详细信息。
- [如何使用机器人绘图机进行水彩画：对 Licia He 的采访](https://www.dirtalleydesign.com/blogs/news/how-to-watercolor-painting-with-a-robotic-drawing-machine-an-interview-with-licia-he)
- [300 Days with Plotters](https://liciahe.medium.com/300-days-with-plotters-14159ab64034) - Licia He 撰写的关于成功的 100 天策划挑战的博客文章。
- [罗兰 DXY 1300 绘图仪自检](https://www.youtube.com/watch?v=BMVq8vuH4sw)
- [Vintage Aritma 0507 Plotter drawing Sierpinski triangles in one stroke](https://www.youtube.com/watch?v=kfL3K8mQp5I) - Aritma Minigraf 0507 视频。
- [绘图仪（Artima Minigraf 0507）](https://www.youtube.com/watch?v=Xso0gfLp8IE&t=34s)
- [https://jiristepanovsky.cz/project.php?p=13plotter](https://jiristepanovsky.cz/project.php?p=13plotter) - 有关捷克斯洛伐克 Aritma Minigraf 0507 绘图仪的博客文章。
- [Aritma Minigraf 0507 上的另一幅图画](https://www.youtube.com/watch?v=EwFyIusdH7g)
- [Aritma Minigraf 0507 绘制航天飞机](https://www.youtube.com/watch?v=YY0ivdyhLpo)
- [Drawing an Etch-Mask Directly onto a PCB using a Vintage Plotter](https://www.youtube.com/watch?v=nkxiFXCnbj8&t=131s) - 视频描述中有一些关于该绘图仪的有趣细节。
- [OrCAD 386 and a plotter Colorgraf Aritma 512](http://simandl.cz/stranky/elektro/spoje/pcb.htm) - 关于使用 Colorgraf 512 绘图仪和 OrCAD 386 制作印刷电路板的文章。
- [Early Computer Art in the 50s and 60s](https://www.amygoodchild.com/blog/computer-art-50s-and-60s) - 很好的艺术史课程，有很多与绘图相关的艺术家。
- [Coding My Handwriting](https://www.amygoodchild.com/blog/cursive-handwriting-in-javascript) - 使用 p5.js 和一些自定义工具创建手写体的伟大探索。

## 手册、蜉蝣、论文和专利

扫描的绘图仪手册、营销蜉蝣、学术论文和专利。感谢 [Internet Archive](https://archive.org) 托管其中的大部分内容。

### 手册

按公司名称和产品名称的字母顺序排序。

- [苹果彩色绘图仪用户手册](https://archive.org/details/AppleColorPlotter)
- [Aritma Colorgraf 512](http://simandl.cz/stranky/elektro/colorgraf/colorgraf_a.htm) - 带有扫描原理图和手册的网站。
- [Atari 1020 Color Printer Owner's Guide (1982)](https://archive.org/details/atari-1020-color-printer) - 更高质量的扫描也可作为 [buildlog.net 上的 PDF](https://www.buildlog.net/blog/wp-content/uploads/2019/09/atari-1020-color-printer-owners-guide.pdf) 获得
- [Atari 1020 彩色打印机现场服务手册 (1983)](https://archive.org/details/atari1020colorprinterfieldservicemanualrev.011983atari)
- [CalComp Artisan Plus 1023/1025/1026 用户指南 (1990)](https://archive.org/details/calcomp-artisan-plus-1023-1025-1026-users-guide)
- [CalComp 笔式绘图仪编程 (1968)](https://archive.org/details/bitsavers_calcompProlottersJun68_2464236)
- [Commodore 1520 打印机绘图仪手册 (1983)](https://archive.org/details/1520PrinterPlotterUsersManualStyleA)
- [Commodore 1520 打印机绘图仪手册](https://archive.org/details/1520PrinterPlotterusersManualStyleB)
- [控制数据 165/165-2 绘图仪手册](https://archive.org/details/bitsavers_cdc160139c_4086972)
- [Esterline Angus Spartan X-Y Recorder Instruction Manual](https://archive.org/details/manualsplus_03665) - 修订版 1178。
- [Esterline Angus Spartan X-Y Recorder Instruction Manual (1980)](https://archive.org/details/manualsplus_03659) - 修订版 1080、1178、0480。
- [Esterline Angus XY530 型记录仪使用说明书](https://archive.org/details/manualsplus_03657)
- [Esterline Angus XY575 型记录仪使用手册 (1976)](https://archive.org/details/manualsplus_03641)
- [Fluke 1771A 智能数字绘图仪用户手册 (1983)](https://archive.org/details/manualsplus_03096)
- [格柏 GS750 Plus 用户手册 (1995) (manualslib)](https://www.manualslib.com/manual/465193/Gerber-Gs750-Plus.html)
- [Gerber Signmaker IVB 用户手册 (1983) (manualslib)](https://www.manualslib.com/manual/464167/Gerber-Signmaker-Ivb.html)
- [Graphtec 笔式绘图仪 MP303 系列维修手册 (2004)](https://archive.org/details/manualzilla-id-5807113)
- [Houston Instrument DMP-160 绘图仪操作手册](https://archive.org/details/houston-instrument-dmp-160-series-plotters-operation-manual)
- [Houston Instrument DM/PL 命令语言 (1984)](https://archive.org/details/hi-dmpl-command-language)
- [休斯顿仪器 DMP-40V 操作手册 (1988)](https://archive.org/details/dmp-40v)
- [休斯顿仪器 HIPLOT DMP-51/52 操作手册 (1985)](https://archive.org/details/hi-dmp-51-52-operation-manual)
- [DM/PL 智能绘图仪的休斯顿仪器接口说明 (1983)](https://archive.org/details/hi-interface-notes-dm-pl-plotters)
- [休斯顿仪表台组装程序 DMP-50 系列绘图仪](https://archive.org/details/hi-stand-assembly-procedure-dmp-50-series-plotter)
- [Houston Instrument DMP-60 系列绘图仪操作手册 (1990)](https://archive.org/details/houston-instruments-dmp-60-manual)
- [HP 7470A 互连指南](https://archive.org/details/manualzilla-id-7029812)
- [HP 7470A 操作员手册 (manualslib)](https://www.manualslib.com/manual/1089592/Hp-7470a.html)
- [HP 7475A 图形绘图仪操作和互连手册](https://archive.org/details/HP7475AOperationManual)
- [HP-75 绘图仪 ROM 外部参考规范 (1982) (PDF)](https://literature.hpcalc.org/community/hp75-plotter-ers.pdf)
- [HP 7570A DraftPro 绘图仪硬件支持手册](https://archive.org/details/7570adraftproplotterhardwaresupportmanual0757090000201pagesdec86)
- [HP 7580B 绘图仪服务手册 (1986)](https://archive.org/details/hp-7580-b-plotter-service-manual)
- [HP 7585B 绘图仪服务手册 (1983)](https://archive.org/details/bitsavers_hpplotter0_18190273)
- [HP DraftPro 绘图仪用户指南 (1986)](https://archive.org/details/draftproplotterusersguide0757090017163pagesmay86)
- [HP DraftPro 绘图仪程序员参考 (1986)](https://archive.org/details/draftproprogrammersreference0757090001387pagessep86)
- [Mutoh ET202 划线器（德文）](https://archive.org/details/mutoh-et202-leichtgemacht)
- [Olivetti PL10 微型绘图仪用户指南 (1983)](https://archive.org/details/olivettipl10microplotter)
- [Olivetti P6060 编程手册 (1979)（意大利语）](https://archive.org/details/olivettip6060prestazionigrafiche)
- [飞利浦 X-Y 平板记录仪 PM 8120 (1971)](https://archive.org/details/manualsplus_03520)
- [Radio Shack TRS-80 绘图仪打印机手册](https://archive.org/details/Plotter_Printer_19xx_Radio_Shack)
- [Radio Shack TRS-80 彩色图形打印机操作手册](https://archive.org/details/cgp-115_operation_manual)
- [Radio Shack TRS-80 彩色图形打印机服务手册](https://archive.org/details/cgp-115-service-manual)
- [罗兰DXY-880操作手册（1984年）](https://archive.org/details/RolandDXY880PlotterOperationManual)
- [罗兰DXY-980操作手册（1985年）](https://archive.org/details/rolanddxy980operationmanual)
- [罗兰DXY-990操作手册（1986年）](https://archive.org/details/roland-dxy-990)
- [Roland DXY-1300 -1200 -1100 命令参考手册](https://archive.org/details/rolanddxy130012001100commandreferencemanualaf)
- [罗兰 DXY-1350A -1150A 用户手册 (1997) (manualslib)](https://www.manualslib.com/manual/884553/Roland-Dxy_1350.html)
- [罗兰 DPX-2000 用户手册](https://archive.org/details/roland-dpx-2000-manual)
- [Roland DPX-3300 操作手册 (GitHub)](https://github.com/sismoke/Roland-DPX-3300/blob/master/manual/DPX-3300.pdf)
- [Roland DPX-3300 服务说明 (1987)](https://archive.org/details/dpx-3300-service-manual)
- [罗兰 DPX-3300 原理图 (1987)](https://archive.org/details/dpx-3300-schematics)
- [Roland DPX-3700A DPX-2700A 用户手册（Roland 直接下载）](https://downloadcenter.rolanddg.com/contents/manuals/DPX-3700A+2700A_USE_E_R8.pdf)
- [罗兰 XY 绘图仪 DXY-1350A DXY-1150A 用户手册 (1997)](https://archive.org/details/manualzilla-id-5691908)
- [Rotring 管状绘图仪点实用技巧和信息](https://archive.org/details/rotingtubularplotterpointprakticaltipsandinformation)
- [Rotring NC 划线器 CS 50 操作手册 (1989)](https://archive.org/details/rotring_NC-scriber_CS_50_Operating_Instructions)
- [SEGA SP-400 Operation Manual](https://archive.org/details/sega-sp-400) - 这并不以可翻页的形式出现在档案馆中，但原始页面扫描仍然可供下载。
- [Sekonic SPL-450+/SPL-455 用户手册 (1990)（德语）](https://archive.org/details/sekonicspl450spl455)
- [西门子 C1613 绘图仪手册（德文）](https://archive.org/details/SiemensC1613Manual)
- [银簧彩色 PenGraph EB-50 操作手册 (1984)](https://archive.org/details/silver-reed-colour-pengraph-eb-50-operating-manual)
- [Taxan X-Y 绘图仪 KPL 710 使用手册](https://pzwiki.wdka.nl/mediadesign/File:Taxan_kpl710_x-y_plotter.pdf)
- [Tectronix 4662 交互式数字绘图仪用户手册 (1976)](https://archive.org/details/bitsavers_tektronix42InteractiveDigitalPlotterUserManualNov1_40423494)
- [Tectronix HC100 使用手册 (1987)](https://archive.org/details/manualsonline-id-212d14c3-7d2f-4e64-906f-1a22e86d1f35/)
- [松下RK-P400C 4色绘图笔说明书](https://archive.org/details/panasonic-rk-p-400-c-manual)
- [松下手写笔手册摘录：RS232 协议部分](https://archive.org/details/panasonicpenwriterprotocol)
- [(Unknown Brand) LP 2002 Photo Plotter Attachment Operating Manual (German)](https://archive.org/details/lp-2002-betriebsanleitung/) - 另请参阅 [Martin Bircher 的帖子](https://mastodon.social/@artandtech/109382879937442706) 以及该设备的图片。

### 蜉蝣属

老式广告、营销材料和宣传视频。

- [分时外设 TSP-212 手册](https://archive.org/details/TNM_Time_Share_Peripherals_-_TSP-212_plotting_sys_20170630_0194)
- [Hewlett-Packard Journal Volume 29 Number 1](https://archive.org/details/Hewlett-Packard_Journal_Vol._29_No._1_1977-09_Hewlett-Packard) - 有关 HP 9872A 和 7221A 笔式绘图仪开发的多篇文章。
- [Hewlett-Packard Journal Volume 32 Number 10](https://archive.org/details/Hewlett-Packard_Journal_Vol._32_No._10_1981-10_Hewlett-Packard) - 有关 HP 7580A 型绘图仪开发的多篇文章。
- [Hewlett-Packard Journal Volume 32 Number 11](https://archive.org/details/Hewlett-Packard_Journal_Vol._32_No._11_1981-11_Hewlett-Packard) - 有关 HP 7580A 型绘图仪开发的多篇文章。
- [Hewlett-Packard Journal Volume 33 Number 12 (1982)](https://archive.org/details/Hewlett-Packard_Journal_Vol._33_No._12_1982-12_Hewlett-Packard) - 有关 HP 7470A 型绘图仪的多篇文章。
- [CalComp 精密图形系统 900/728 手册 (1970)](https://archive.org/details/TNM_CalComp_-_Precision_graphics_system_900-728_20170630_0196)
- [数字绘图通讯 (1967)](https://archive.org/details/TNM_Digital_Plotting_Newsletter_march-april_1967__20171014_0114)
- [Versatec 打印机和绘图仪手册 (1977)](https://archive.org/details/TNM_Versatec_printers_and_plotters_-_Versatec_a_X_20180227_0009)
- [Versatec 打印机/绘图仪、绘图仪和输出系统 (1981)](https://archive.org/details/TNM_Printer-plotters_plotters_and_output_systems__20171113_0057)
- [Roland Users Group Volume 2 Number 4 (1984)](https://archive.org/details/RolandUsersGroupVolume2Number41984/page/n39/mode/2up) - _计算机和绘图仪取代绘图桌和铅笔_第 36 页文章（PDF 第 40 页）。
- [Omega-t Systems FasPlot 绘图仪手册](https://archive.org/details/TNM_Omega-t_Systems_-_FasPlot_Plotter_20170630_0254)
- [Commodore 计算机绘图仪 CBM 8075 手册（德语）](https://archive.org/details/Plotter_CBM8075_198x_Commodore_DE)
- [Strobe 100 型图形绘图仪手册 (1980)](https://archive.org/details/TNM_Strope_Model_100_graphics_plotter_-_Strobe_In_20180506_0009)
- [Byte Magazine Vol 12 No 4 (1987) 中的 Roland DG 绘图仪广告](https://archive.org/details/byte-magazine-1987-04/page/n159/mode/2up) ([via @OldTechAdverts](https://twitter.com/OldTechAdverts/status/1454558415355850755))
- [Auerbach On Digital Plotters And Image Digitizers (1972)](https://archive.org/details/auerbachondigitalplottersandimagedigitizers) - 一本关于绘图仪和数字化仪的书。
- [CalComp 图形产品手册 (1981)](https://archive.org/details/TNM_CalComp_graphics_products_plotters_and_printe_20171101_0032)
- [CalComp Plotters in 1968](https://www.youtube.com/watch?v=AAc4VLR6-Dg) - 展示平板 CalComp 绘图仪及其输出的宣传视频。
- [Houston Instrument DMP-41 和 DMP-42 绘图仪手册](https://archive.org/details/hi-dmp-41-42-brochure)
- [Houston Instrument DMP-51/52 系列手册](https://archive.org/details/hi-dmp-51-52-brochure)
- [Houston Instrument 全息图绘图仪手册](https://archive.org/details/TNM_Omnigraphic_Plotter_20171016_0228)
- [Sweet-P Plotter Brochure and Price List](https://archive.org/details/bitsavers_enterCompuersonalPlotterprricelistBrochure_4929854) - 四页彩色营销手册，附有建议零售价表。
- [IEEE Electronic Systems News Autumn (1985)](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=5345111) - 三色 Penman 机器人绘图仪回顾。
- [Apple II Business Graphics Film (1982)](https://archive.org/details/apple-ii-business-graphics) - 4:57 有一个 Strobe Model 100 图形绘图仪绘制条形图。
- [Elektor Magazine Selbstbauplotter MONDRIAN II (1990) (German)](https://archive.org/details/elektor_202310) - 另请参阅 [GrabCAD 上该绘图仪的模型](https://grabcad.com/library/plotter-mondrian-1)。
- [IBM 7374 和 7375 彩色绘图仪手册 (PDF)](https://www.1000bit.it/ad/bro/ibm/IBM737xColorPlotters.pdf)

### 论文

关于笔式绘图仪、艺术和相关主题的学术论文。

- [Toward Aesthetic Guidelines for Paintings with the Aid of a Computer (1975) (paywall)](https://www.jstor.org/stable/1573236) - 维拉·莫尔纳尔.
- [笔式绘图仪作为使用可解决方案处理的纳米材料进行快速设备原型设计的低成本平台 (2023) (PDF)](https://onlinelibrary.wiley.com/doi/pdf/10.1002/adem.202300226)
- [溶胶-凝胶技术和笔式绘图仪打印制备 V2O5 薄膜](https://www.proquest.com/docview/2791602751?sourcetype=Scholarly%20Journals)
- [PatternPortrait：把我画得像你的涂鸦一样 (2024)](https://arxiv.org/abs/2401.13001)
- [我可以教机器人复制线条艺术吗（2019）](https://arxiv.org/abs/1910.07860)
- [Tools, Tricks, and Hacks: Exploring Novel Digital Fabrication Workflows on #PlotterTwitter](https://dl.acm.org/doi/abs/10.1145/3411764.3445653) - 关于绘图仪社区新颖工作流程的研究论文（[视频摘要](https://www.youtube.com/watch?v=xqhT-8ElJ68)）。
- [维拉·莫尔纳的电脑绘画](https://www.researchgate.net/publication/338896073_Vera_Molnar's_Computer_Paintings)

### 专利

与绘图仪技术相关的专利。

- [通用 X-Y 绘图笔适配器](https://patents.google.com/patent/US4943817)

## 课程

关于绘图仪和生成艺术的深入课程和教程。

- [Painting with Plotters](https://www.eyesofpanda.com/project/painting_with_plotters/) - Licia He 正在进行的课程。

## 社区

在哪里可以找到其他绘图仪和绘图机器人朋友。

- [PlotterArt Reddit 子版块](https://www.reddit.com/r/PlotterArt)
- [AxiDraw Reddit 子版块](https://www.reddit.com/r/axidraw)
- [生成艺术子版块](https://www.reddit.com/r/generative)
- [Plotter People](https://plotterpeople.github.io/) - 面对面的聚会（目前为止是旧金山和纽约），包括演讲和绘图艺术画廊。
- [DrawingBots Discord Forum](https://discordapp.com/invite/XHP3dBg) - 具有活跃社区的 Discord 论坛。
- [PlotterFiles](https://plotterfiles.com/) - 用于共享绘图仪 SVG 文件的社区。
- #PenPlotter - [Bluesky](https://bsky.app/search?q=%23PenPlotter) 和 [Mastodon](https://mastodon.social/search?q=%23PenPlotter) 主题标签具有良好的绘图活动。

## 绘图仪艺术品出售

在线销售绘图仪艺术品的艺术家。

- [亚当·富勒](https://adamfuhrer.bigcartel.com)
- [AndyMakes](https://shop.andymakes.com/)
- [阿尔扬·范德梅吉](https://dutchplottr.nl/en/)
- [EmergentDesign](https://emergentdesign.bigcartel.com/products)
- [inconvergent](http://buy.inconvergent.net)
- [英格丽德·伯灵顿](https://wares.lifewinning.com)
- [迈克尔·福格曼](https://www.michaelfogleman.com/plotter)
- [米歇尔·钱德拉](https://www.dirtalleydesign.com/)
- [保罗·理查兹](https://shop.paulrickards.com)
- [佩德罗·阿尔科塞尔](https://store.pedroalcocer.com/)

## 其他很棒的东西

相关精彩列表供进一步探索。

- [awesome-generative-art](https://github.com/kosmos/awesome-generative-art)
- [awesome-creative-coding](https://github.com/terkelg/awesome-creative-coding)
- [awesome-3d-engines-for-plotters](https://github.com/msurguy/awesome-3d-engines-for-plotters)
