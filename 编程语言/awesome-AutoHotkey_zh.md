# 很棒的自动热键 [![AutoHotkey](https://img.shields.io/badge/Language-AutoHotkey-yellowgreen.svg)](https://autohotkey.com/)

精彩的 [AutoHotkey](https://autohotkey.com/) 库、库发行版、脚本、工具和资源的精选列表。受到其他[很棒的列表](https://github.com/bayandin/awesome-awesomeness)的启发。请在贡献之前阅读 [CONTRIBUTING.md](https://github.com/ahkscript/awesome-AutoHotkey/blob/master/.github/CONTRIBUTING.md)。

过时或已停产，但仍然与历史相关的项目可以在 [Historical.md](https://github.com/ahkscript/awesome-AutoHotkey/blob/master/Historical.md) 上找到

发展状态：
[![Build Status](https://travis-ci.org/ahkscript/awesome-AutoHotkey.svg)](https://travis-ci.org/ahkscript/awesome-AutoHotkey) [![awesome_bot](https://img.shields.io/badge/PoweredBy-awesome_bot-yellow.svg)](https://github.com/dkhamsing/awesome_bot)

<!-- Note: be sure to use unique anchor tags for each item in the table of contents -->
* [很棒的自动热键](#awesome-autohotkey)
 * [Libraries](#libraries)
    * [Clipboard](#clipboard)
    * [Console](#console)
    * [数据格式](#libraries-data-format)
    * [数据结构和算法](#libraries-data-structs-algorithms)
    * [Database](#database)
    * [Filesystem](#filesystem)
    * [Graphics](#libraries-graphics)
    * [GUI](#libraries-gui)
    * [Hotkeys](#hotkeys)
    * [Joystick](#joystick)
    * [Maths](#maths)
    * [Memory](#memory)
    * [Networking](#networking)
    * [绘图（图形、条形图、图表等）](#libraries-plotting)
    * [System](#libraries-system)
    * [文本操作](#text-manipulation)
  * [图书馆发行版](#library-distributions)
  * [Scripts](#scripts)
    * [Clipboard](#scripts-clipboard)
    * [Filesystem](#scripts-filesystem)
    * [Graphics](#scripts-graphics)
    * [GUI](#scripts-gui)
    * [Maths](#scripts-maths)
    * [Mouse](#mouse)
    * [Typing](#typing)
    * [窗口管理](#window-management)
    * [Games](#games)
  * [Tools](#tools)
    * [Interpreter](#interpreter)
    * [Decompilers](#decompilers)
    * [Debugging](#debugging)
    * [集成开发环境](#integrated-development-environment)
    * [GUI 所见即所得构建器](#gui-wysiwyg-builders)
    * [脚本记录者和作家](#script-recorders-and-writers)
    * [网络语法荧光笔](#web-syntax-highlighters)
    * [Others](#tools-others)
    * [（用于）其他编程语言](#use-in-other-programming-languages)
  * [Tutorials](#tutorials)
    * [Classes](#tutorials-classes)
    * [COM](#tutorials-com)
    * [GUI](#tutorials-gui)
    * [MCode（机器代码）](#tutorials-mcode)
  * [Resources](#resources)
    * [Documentation](#documentation)
    * [Books](#books)
    * [快速入门指南](#quick-start-guides)
    * [Websites](#websites)
  * [Forks](#forks)
    * [AutoHotkey_H](#autohotkey_h)

<hr/>

## 图书馆
*有用的 AutoHotkey 库列表。库是具有一些可重用功能的代码，可以与您自己的代码组合以创建新功能。*

### 剪贴板
* [WinClip](http://www.apathysoftworks.com/ahk/WinClip.zip) - by Deo - WinClip 是一个剪贴板操作类，扩展了 AutoHotkey 的剪贴板功能，包括对 RTF、HTML 和图像的支持。论坛主题：[链接](https://autohotkey.com/board/topic/74670-class-winclip-direct-clipboard-manipulations/)。

### 控制台
* [AHKonsole](https://github.com/G33kDude/Console) - G33kdude - 基于类的 AutoHotkey 库，用于控制台支持。该库使您能够创建一个代表要与之交互的控制台的对象，以及多个控制台缓冲区对象以促进双缓冲。论坛主题：[链接](https://autohotkey.com/boards/viewtopic.php?f=6&t=4955)。
* [LibCon](https://github.com/joedf/LibCon.ahk) - 作者：joedf - 用于控制台支持的 AutoHotkey 库。该库使您能够编写控制台应用程序并与其他控制台实例交互。基本上，这个库促进了与控制台的编写和交互有关的任何事情。论坛主题：[链接](https://autohotkey.com/boards/viewtopic.php?t=17)。

### <a name="libraries-data-format"></a>数据格式
* [AHK_ctable](https://github.com/hoppfrosch/AHK_cTable) - 作者：hoppfrosch - 处理表格格式字符串的库 - 论坛帖子：[链接](https://autohotkey.com/board/topic/61256-object-table/://autohotkey.com/board/topic/61256-object-table/page-2?&#entry467816)。
* [AutoHotkey-JSON](https://github.com/cocobelgica/AutoHotkey-JSON) - 由 cocobelgica - AutoHotkey 的 JSON 库.论坛主题：[链接](https://autohotkey.com/boards/viewtopic.php?f=6&t=627)。
* [CSV](https://github.com/hi5/CSV) - 由 trueski/kdoske - 使用 CSV 文件和列表视图函数的库。论坛主题：[链接](https://autohotkey.com/boards/viewtopic.php?f=6&t=34853)。
* [List manipulation functions](http://www.hars.us/SW/List.ahk) - by Laszlo - 操作逗号分隔列表的函数库。论坛主题：[链接](https://autohotkey.com/board/topic/3020-list-manipulation-functions/)。
* [ObjCSV](https://github.com/JnLlnd/ObjCSV/) - JnLlnd - 用于将 CSV 文件加载/保存到对象和列表视图功能的库。论坛主题：[链接](https://autohotkey.com/boards/viewtopic.php?f=6&t=41)。
* [ObjDump/ObjLoad](https://autohotkey.com/boards/viewtopic.php?f=6&t=3573) - by HotKeyIt - 将对象序列化/反序列化到变量/内存/从变量/内存中序列化/反序列化。
* [SerDes](https://github.com/cocobelgica/AutoHotkey-SerDes) - by cocobelgica - 序列化/反序列化 AutoHotkey 对象结构。论坛主题：[链接](https://autohotkey.com/boards/viewtopic.php?f=6&t=4212)。
* [Table](https://github.com/Jim-VxE/AHK-Lib-Table) - VxE - 用于操作表格 (TSV) 格式和列表视图函数中的字符串的库。论坛主题：[链接](https://autohotkey.com/board/topic/61540-lib-string-based-table-manipulation-v028/)。
* [XA](https://github.com/hi5/XA) - by trueski/hi5 - 将数组序列化为 XML 或从 XML 序列化数组。论坛主题：[链接](https://autohotkey.com/boards/viewtopic.php?f=6&t=34849)。

### <a name="libraries-data-structs-algorithms"></a>数据结构和算法
* [Facade](https://github.com/Shambles-Dev/AutoHotkey-Facade) - by Shambles - 一组函数式编程库。 - 论坛主题：[链接](https://www.autohotkey.com/boards/viewtopic.php?f=6&t=59253)
* [HashTable](https://github.com/Shambles-Dev/AutoHotkey-HashTable) - 作者：Shambles - AutoHotkey 的哈希表实现。
* [LibCrypt](https://github.com/ahkscript/LibCrypt.ahk) - 由不同作者编写 - 加密和编码函数的集合。
* [Type_Checking](https://github.com/Shambles-Dev/AutoHotkey-Type_Checking) - 作者：Shambles - AutoHotkey 的类型检查 - 论坛帖子：[链接](https://www.autohotkey.com/boards/viewtopic.php?f=6&t=59857)

### 数据库
* [AHKDb](https://github.com/AHKDb/AHKDb) - by AHKDb - 用于制表符分隔数据的数据库。
* [ahkDBA](https://github.com/IsNull/ahkDBA) - IsNull - 一个 OOP-SQL 数据库访问框架。论坛主题：[链接](https://autohotkey.com/board/topic/71179)。
* [Class_SQLiteDB](https://github.com/AHK-just-me/Class_SQLiteDB) - by just Me - AHK SQLite API 包装类。论坛主题：[链接](https://autohotkey.com/boards/viewtopic.php?t=1064)。
* [Leya - MySQL API](https://github.com/kevgk/Leya) - 作者：kevgk - 在 autohotkey 中使用 MySQL 数据库，无需向客户端公开服务器凭据。

### 文件系统
* [FileGetProperties](https://autohotkey.com/boards/viewtopic.php?f=6&t=3806) - by kon - 用于检索扩展文件属性的函数。

### <a name="libraries-graphics"></a>图形
* [GDIp](https://github.com/tariqporter/Gdip/) - by tic - 功能齐全的库，有助于与 Microsoft 的 gdiplus.dll 交互 - 论坛主题：[链接](https://autohotkey.com/boards/viewtopic.php?f=6&t=6517)。
* [ImagePut](https://github.com/iseahound/ImagePut) - by iseahound - 用于转换为文件、流、窗口、base64、url、光标、屏幕坐标、剪贴板、指针、句柄等的图像库。支持 AutoHotkey v1 和 v2。 - 论坛主题：[链接](https://www.autohotkey.com/boards/viewtopic.php?f=6&t=76301&p=330615)
* [AHKv2-GDIP](https://github.com/mmikeww/AHKv2-Gdip) - 上述 GDI+ 库的更新与 AHK v1.1 和 AHK v2 兼容 - 论坛主题：[链接](https://autohotkey.com/boards/viewtopic.php?f=6&t=6517)。
* [GDIp_ImageSearch](https://autohotkey.com/board/topic/71100-) - by tic - 使用 gdiplus.dll 在屏幕上搜索图像实例的库。请参阅该线程的末尾以获取 MasterFocus 的改进版本，或者在此处查看他的 [GitHub 存储库](https://github.com/MasterFocus/AutoHotkey/tree/master/Functions/Gdip_ImageSearch)
* [Simple GDI class](https://autohotkey.com/boards/viewtopic.php?f=6&t=5820) - by GeekDude - 旨在使低级 GDI 函数的使用变得简单的类。
* [Particle System](https://github.com/acorns/Particle-System) - by tidbit - 一个简单的类，使用 GDI+ 将粒子添加到 GUI 或屏幕上。论坛主题：[链接](https://autohotkey.com/boards/viewtopic.php?f=6&t=26485)。

### <a name="libraries-gui"></a>图形用户界面

#### 组合框
* [CbAutoComplete](https://github.com/pulover/cbautocomplete) - by Pulover - 自动完成 AHK 组合框中键入的值.论坛主题：[链接](https://autohotkey.com/boards/viewtopic.php?f=6&t=15002)

#### 自定义控件
* [Rebar](https://github.com/Pulover/Class_Rebar) - by Pulover - AutoHotkey Rebar 自定义控件的 AHK 类。论坛主题：[链接](https://autohotkey.com/boards/viewtopic.php?f=6&t=139)
* [Toolbar](https://github.com/Pulover/Class_Toolbar) - by Pulover - AutoHotkey 工具栏自定义控件的 AHK 类。论坛主题：[链接](https://autohotkey.com/boards/viewtopic.php?f=6&t=138)

#### 编辑
* [Edit v2.0](https://autohotkey.com/boards/viewtopic.php?f=6&t=5063) - by jballi - 用于显示和编辑文本的轻量级且功能惊人的默认编辑控件的库。论坛主题：[链接](https://autohotkey.com/boards/viewtopic.php?f=6&t=5063)

#### 一般
* [AutoXYWH](https://autohotkey.com/boards/viewtopic.php?f=6&t=1079) - by tmplinshi - 调整 GUI 大小时自动移动控件并调整其大小。
* [TaskDialog](https://github.com/AHK-just-me/TaskDialog) - 作者：Just Me - Win Vista+ 的增强型 MsgBox - [链接](https://autohotkey.com/boards/viewtopic.php?f=6&t=4635)
* [OnWin](https://github.com/cocobelgica/AutoHotkey-Util/blob/master/OnWin.ahk) - by cocobelgica - 在窗口事件上调用函数（WinWaitXXX 异步）。论坛主题：[链接](https://autohotkey.com/boards/viewtopic.php?f=6&t=6463)
* [CGUI](https://github.com/lipkau/CGUI/) - 作者：ChrisS85 - AutoHotkey 的面向对象 GUI 库。论坛主题：[链接](https://autohotkey.com/boards/viewtopic.php?f=6&t=26990)
* [Class_ScrollGUI](https://github.com/AHK-just-me/Class_ScrollGUI) - by just me - 创建一个可滚动 GUI 作为 AHK GUI 窗口的父窗口。论坛主题：[链接](https://autohotkey.com/boards/viewtopic.php?f=6&t=6316)

#### 列表框
* [LBEX](https://github.com/AHK-just-me/LBEX) - by [just me](https://github.com/AHK-just-me) - 列表框实用函数的集合。论坛主题：[链接](https://autohotkey.com/boards/viewtopic.php?f=6&t=4755)
* [TransparentListBox](https://github.com/AHK-just-me/Class_TransparentListBox) - by just Me - 为 AHK GUI 提供透明列表框控件。论坛主题：[链接](https://autohotkey.com/boards/viewtopic.php?f=6&t=108)

#### 列表视图
* [LV_Colors](https://github.com/AHK-just-me/Class_LV_Colors/) - by just Me - GUI ListView 的单元格或行的单独背景和/或文本颜色。论坛主题：[链接](https://autohotkey.com/boards/viewtopic.php?f=6&t=1081)
* [LV_EX](https://github.com/AHK-just-me/LV_EX) - 仅由我编写 - AHK GUI ListView 控件的一些附加功能。论坛主题：[链接](https://autohotkey.com/boards/viewtopic.php?f=6&t=1256)
* [LV_InCellEdit](https://github.com/AHK-just-me/Class_LV_InCellEdit/) - by just Me - ListView 控件的单元格内编辑。论坛主题：[链接](http://https://autohotkey.com/boards/viewtopic.php?f=6&t=1076)
* [LV_Rows](https://github.com/Pulover/Class_LV_Rows) - by Pulover - AHK ListView 控件的附加功能。论坛主题：[链接](https://autohotkey.com/boards/viewtopic.php?f=6&t=137)

#### 菜单
* [[Lib] 菜单](https://autohotkey.com/boards/viewtopic.php?t=3068) - 由我个人编写 - 一些与 AHK 菜单相关的功能。论坛主题：[链接](https://autohotkey.com/boards/viewtopic.php?t=3068)

#### 网络
* [Neutron](https://github.com/G33kDude/Neutron.ahk/) - G33kDude - 用于使用 AutoHotkey 构建基于 HTML 的用户界面的工具集。论坛主题：[链接](https://www.autohotkey.com/boards/viewtopic.php?f=6&t=76865)

### 热键
* [CHotkeyControl](https://autohotkey.com/boards/viewtopic.php?f=6&t=9087) - byvillainC - 替换 AHK 热键 GuiControl，支持鼠标按钮等（部分成熟）。
* [HParse](https://autohotkey.com/board/topic/92805-) - by Avi - 将有意义的快捷键 (Ctrl+X) 转换为 AutoHotkey 语法 (^x) 的函数。

### 操纵杆
* [CvJoyInterface](https://autohotkey.com/boards/viewtopic.php?t=5705) - byvillainC - 使用 AHK 控制 vJoy 虚拟操纵杆.
* [JoystickWrapper](https://autohotkey.com/boards/viewtopic.php?f=19&t=28889) - byvilanC - 完全基于事件，8 轴，128 个按钮，4 POV 操纵杆读取（C# DLL，使用 Lexikos 的 CLR）。
* [XInput](https://autohotkey.com/board/topic/35848-xinput-xbox-360-controller-api/) - by Lexikos - 使用 XInput 读取 XBOX 游戏手柄（独立读取 L/R 触发器的唯一方法），控制隆隆电机。

### 数学
* [calc()](https://autohotkey.com/board/topic/59087-func-calc-math-expression-evaluation-incl-brackets/?p=655135) - 数学表达式评估包括括号。
* [Eval](https://github.com/pulover/eval) - 作者：Pulover - 评估字符串中的表达式。论坛主题：[链接](https://autohotkey.com/boards/viewtopic.php?f=6&t=13565)
* [Scientific Maths](https://autohotkey.com/board/topic/93516-) - by Avi - 促进高精度数学的图书馆。
* [Time()](https://autohotkey.com/board/topic/42668-time-count-days-hours-minutes-seconds-between-dates/) - by HotkeyIt - 计算日期之间的天数、小时、分钟、秒数。论坛主题：[链接](https://autohotkey.com/board/topic/42668-time-count-days-hours-mines-seconds- Between-dates/)

### 内存

* [classMemory](https://github.com/Kalamity/classMemory) - RHCP (Kalamity) - 具有模式扫描的 AHK 内存读/写类。论坛主题：[链接](https://www.autohotkey.com/boards/viewtopic.php?t=1177)

### 网络
* [AHKhttp](https://github.com/Skiouros/AHKhttp) - 基本 HTTP 服务器。论坛 [链接](https://autohotkey.com/boards/viewtopic.php?f=6&t=4890)
* [AHKsock](https://github.com/jleb/AHKsock) - 由 TheGood - 基于函数的套接字库。支持TCP。论坛 [链接](https://autohotkey.com/board/topic/53827-ahksock-a-simple-ahk-implementation-of-winsock-tcpip/)
* [Chrome.ahk](https://github.com/G33kDude/Chrome.ahk) - 作者：G33kDude - 使用本机 AutoHotkey 自动化 Google Chrome - 论坛 [链接](https://www.autohotkey.com/boards/viewtopic.php?t=42890)
* [FTP](https://github.com/jNizM/Class_FTP) - 作者：jNizM - FTP 会话的 AutoHotkey 包装器（类） - 论坛 [链接](https://www.autohotkey.com/boards/viewtopic.php?f=6&t=79142&p=344445#p344445)
* [Rufaydium WebDriver](https://github.com/Xeo786/Rufaydium-Webdriver) - 由 Xeo786 - Webdriver 库支持任何基于 Chromium 的浏览器，仅需要 webdriver （无 selenium/websocket） - 论坛 [link](https://www.autohotkey.com/boards/viewtopic.php?f=6&p=457302)
* [Socket Class (überarbeitet)](https://autohotkey.com/board/topic/94376-) - by Bentschi - 基于类的套接字库。支持 TCP 和 UDP。
* [Socket.ahk](https://github.com/G33kDude/Socket.ahk) - 作者：GeekDude - 基于 Bentschi 的 Socket 库 - 论坛 [链接](https://autohotkey.com/boards/viewtopic.php?f=6&t=35120)
* [WebSocket.ahk](https://github.com/G33kDude/WebSocket.ahk) - 作者：GeekDude - 基于类的 WebSocket 库 - 论坛 [链接](https://autohotkey.com/boards/viewtopic.php?f=6&t=35117)
* [WinSCP.ahk](https://github.com/lipkau/WinSCP.ahk) - 作者：Lipkau - Lib 允许在 AHK 中使用 WinSCP

### <a name="libraries-plotting"></a>绘图（图表、条形图、图表等）
* [BarChart](https://autohotkey.com/board/topic/82959-barchart/) - 通过 Learning One - 用于制作条形图的库。下载[链接](https://dl.dropboxusercontent.com/u/171417982/AHK/BarChart/BarChart.zip)。
* [Excel Charts](https://autohotkey.com/board/topic/88438-excel-charts/) - by Xx7 - 用于在 Excel 中创建图形的库，将图形保存为图像并将其显示在 GUI 中。
* [XGraph](https://autohotkey.com/boards/viewtopic.php?t=3492) - by SKAN - 用于以图形方式绘制实时数据的函数库。
* [SVGraph](https://github.com/CapnOdin/SVGraph) - 作者：CapnOdin - SVGraph 将图形和图表引入 AutoHotkey。论坛 [链接](https://autohotkey.com/boards/viewtopic.php?f=6&t=23892)
* [gdiChartLib](https://github.com/nnnik/gdiChartLib) - 作者：nnnik - 用于自动热键的 gdip 图表库。论坛 [链接](https://autohotkey.com/boards/viewtopic.php?f=6&t=31533)

### <a name="libraries-system"></a>系统
* [RunAsTask](https://autohotkey.com/boards/viewtopic.php?t=4334) - by SKAN - 自动提升脚本，无需 UAC 提示。
* [Vista Audio Control Functions](https://github.com/ahkscript/VistaAudio) - by Lexikos - 提供一些 SoundSet/SoundGet 子命令的替代方法，以及 SoundSet/SoundGet 不支持的一些附加功能。论坛主题：[链接](https://autohotkey.com/board/topic/21984-vista-audio-control-functions/?p=143564)

### 文本操作
* [String Things](https://autohotkey.com/boards/viewtopic.php?f=6&t=53) - by tidbit - 独立的字符串操作函数。
* [TF](https://github.com/hi5/TF) - by hi5 - 用于操作文本文件（例如 *.txt、*.ahk、*.html、*.css 等）和字符串（或变量）的函数。论坛主题：[链接](https://autohotkey.com/boards/viewtopic.php?f=6&t=576)。

## 图书馆发行版
*有用的 AutoHotkey 库发行版列表。图书馆分发是一个用于分发图书馆的系统。*

* [ahk-libs](https://github.com/rshipp/ahk-libs) - Ryan Shipp 的图书馆收藏。
* [ASPDM](https://github.com/ahkscript/ASPDM) - package/stdlib 由 [ahkscript](https://github.com/ahkscript) 人员分发和管理。 Trello [链接](https://trello.com/b/XVP4M76d/package-stdlib-distribution-and-management)。
* [pAHKlight](https://github.com/hi5/pAHKlight) - AutoHotkey 库、类、函数和工具的轻量级指南。

## 脚本
*有用的 AutoHotkey 脚本列表。脚本是旨在用作独立程序的代码，并不意味着与其他代码集成。*

### <a name="scripts-clipboard"></a>剪贴板
* [CL3](https://github.com/hi5/CL3) - 带有插件（搜索、预定义插槽、ClipChain、FIFO、编辑器等）的剪贴板管理器（仅限文本）。论坛主题 [链接](https://autohotkey.com/boards/viewtopic.php?f=6&t=814)。
* [ClipBoardMonitor](https://github.com/536/my-startup-ahk-scripts/blob/master/startup/ClipBoardMonitor/ClipBoardMonitor.ahk) - 监视剪贴板更改，显示文本字数统计工具提示或图片临时 GUI。
* [Clipjump](http://clipjump.sourceforge.net/) - 是一个适用于 Windows 的多剪贴板管理实用程序。源代码：[GitHub](https://github.com/aviaryan/Clipjump)。论坛主题：[链接 1](https://autohotkey.com/boards/viewtopic.php?f=6&t=401)、[链接 2](https://autohotkey.com/board/topic/91488-clipjump-the-ultimate-clipboard-manager-updated-0708/)。

### <a name="scripts-filesystem"></a>文件系统
* [Belvedere](https://github.com/adampash/belvedere) - 根据文件名、扩展名、大小、期限等设置对文件执行操作（移动、复制、删除等）的规则。更多信息[链接](http://lifehacker.com/341950/belvedere-automates-your-self-cleaning-pc)。
* [QuickAccessPopup](https://github.com/JnLlnd/QuickAccessPopup) - 多用途启动器和文件切换器。网站[链接](https://www.quickaccesspopup.com/)。
* [SpicyKeys](https://spicykeys.github.io/) - 使用热键在 Windows 资源管理器中打开或移动/复制选定的文件。论坛主题：[链接](https://www.autohotkey.com/boards/viewtopic.php?f=6&t=97171)

### <a name="scripts-graphics"></a>图形
* [Fun with GDIPlus](https://autohotkey.com/boards/viewtopic.php?f=6&t=6071) - 有趣的 GDI+ 示例。

### <a name="scripts-gui"></a>图形用户界面
* [Examples of Non-Standard GUIs (ActiveX, GDI, etc.)](https://autohotkey.com/boards/viewtopic.php?f=6&t=3851) - 使用非标准方法生成漂亮的用户界面的 GUI 示例。


### <a name="scripts-maths"></a>数学
* [Monster](https://autohotkey.com/board/topic/15675-monster-evaluate-math-expressions-in-strings/) - 评估字符串中的数学表达式（计算器）。
* [Unit Converter](https://autohotkey.com/board/topic/39359-unit-converter/) - 单位转换器，具有最常见的英语和科学单位以及从长度到密度到导热系数的最常见数量。还包括物理和数学常数部分。

### 鼠标
* [EitherMouse](http://www.EitherMouse.com) - 多个鼠标、单独设置、自动交换第二个鼠标上的鼠标按钮。论坛主题：[链接](https://autohotkey.com/boards/viewtopic.php?f=6&t=3648)。
* [MouseGestureL](http://www.vector.co.jp/download/file/winnt/util/fh633547.html) - 通过鼠标手势控制应用程序。手势和动作可以通过可定制的界面来定义。英语和日语文档 - 日语主页 [链接](http://hp.vector.co.jp/authors/VA018351/mglahk.html)
* [Radial Menu](https://autohotkey.com/board/topic/46856-radial-menu-scripts-updated-07122014/) - 强大的热键、启动器、鼠标手势系统等等（可换肤） - 论坛主题：[链接](https://autohotkey.com/board/topic/46856-radial-menu-scripts-updated-07122014/)

### 打字
* [AutoComplete](https://github.com/Uberi/Autocomplete) - 在您键入时建议并完成单词。论坛主题：[链接](https://autohotkey.com/board/topic/60998-autocomplete/)。
* [DateHotkey](https://github.com/tiuub/DateHotkey) - 热键可轻松接收当前、过去或即将到来的日期字符串。论坛主题：[链接](https://www.autohotkey.com/boards/viewtopic.php?f=6&t=89929)
* [Half-QWERTY](https://autohotkey.com/board/topic/1257-half-qwerty-one-handed-typing/page-6#entry216183) - 单手打字。使用空格键作为修饰符，用户只需用一只手即可生成全尺寸键盘两侧的字符。通过论坛帖子了解更多信息：[链接](https://autohotkey.com/board/topic/1257-half-qwerty-one-handed-typing/)
* [KeyPress OSD](https://github.com/marius-sucan/KeyPress-OSD) - 屏幕显示以清晰可见的文本大小显示按下的每个按键或鼠标按钮。论坛主题：[链接](https://autohotkey.com/boards/viewtopic.php?f=6&t=225)
* [Lintalist](http://lintalist.github.io/) - 可搜索的交互式列表，可使用插件复制和粘贴文本。论坛主题：[链接](https://autohotkey.com/boards/viewtopic.php?f=6&t=3378)。
* [Portable Keyboard Layout](http://pkl.sourceforge.net/) - 帮助人们学习更好、更高效的键盘布局，例如 Dvorak、Colemak 或 Asset。论坛主题：[链接](https://autohotkey.com/board/topic/25991-portable-keyboard-layout/)。
* [Static Hands](https://github.com/almogtavor/static-hands) - 超级有用的快捷键，带有 CapsLock 键，无需在打字时移动手。超级简单。没有学习曲线。
* [Thumbscript](https://autohotkey.com/board/topic/27198-beta-thumbscript-ahk/) - 允许您使用数字键盘进行输入，每个字母只需按 2 次数字。文档：[链接](http://thumbscript.com/howitworks.html)
* [TypingAid](https://github.com/ManiacDC/TypingAid/releases) - 在您键入时建议并完成单词。论坛主题：[链接](https://autohotkey.com/boards/viewtopic.php?f=6&t=5644) GitHub [链接](https://github.com/ManiacDC/TypingAid)。

### 窗口管理
* [Automatic Window Manager](https://autohotkey.com/boards/viewtopic.php?f=6&t=17907) - 保存和恢复每个进程的最后一个窗口位置。论坛主题：[链接](https://autohotkey.com/boards/viewtopic.php?f=6&t=17907)
* [bug.n](https://github.com/fuhsjr00/bug.n) - 平铺窗口管理器。论坛主题：[链接](https://autohotkey.com/board/topic/30332-bugn-tiling-window-manager/)
* [Min2Tray](http://junyx.breadfan.de/Min2Tray/) - 最小化窗口到托盘等。论坛主题：[链接](https://autohotkey.com/board/topic/4173-min2tray-v179-minimize-window-to-tray-much-more/)
* [Open-Show-Apps](https://github.com/JuanmaMenendez/AutoHotkey-script-Open-Show-Apps) - 打开、恢复或最小化所需的 Windows 或 Chrome 的应用程序。论坛主题：[链接](https://www.autohotkey.com/boards/viewtopic.php?f=6&t=63579&p=272220#p272220)
* [SnapX](https://github.com/benallred/SnapX/releases) - 通过接管其热键（Win+左/右等）并提供对捕捉位置和大小的更细粒度的控制来增强 Windows/Aero Snap。适用于多个显示器、分辨率和 DPI 级别。
* [WindowPadX](https://github.com/hoppfrosch/WindowPadX) - 工具，在多显示器环境中提供一些有用的功能。 _WindowPadX 是 WindowPad 的增强版，最初由 Lexikos 发布，请参阅原始论坛帖子：[链接](https://autohotkey.com/board/topic/19990-windowpad-window-moving-tool/)_

### 游戏
* [Achromatic - ProgressPlatformer](https://github.com/Uberi/ProgressPlatformer/releases) - 平台游戏。论坛主题：[链接](https://autohotkey.com/board/topic/64529-achromatic-progressplatformer-refined/)，GitHub：[链接](https://github.com/Uberi/ProgressPlatformer)
* [AHK Mahjong Solitaire](https://autohotkey.com/boards/codeboxplus/download/183219-1) - 麻将游戏。论坛主题：[链接](https://autohotkey.com//boards/viewtopic.php?f=19&t=40133)
* [F1 Racer](https://www.dropbox.com/sh/01ucst7jeybn9ed/AABCItk8VKlfVp67T0P_DJFia) - 2 或 4 人赛车游戏。论坛主题：[链接](https://autohotkey.com/boards/viewtopic.php?f=19&t=4307&p=24024&hilit=racing#p24024)
* [Infection](https://autohotkey.com/boards/download/file.php?id=3349&sid=b3444f44c767f7698ede586c81d40fe2) - 棋盘游戏。也称为 Ataxx。论坛主题：[链接](https://autohotkey.com/board/topic/35504-game-manytetris-customizable-pocket-tetris/)
* [Ishido](https://github.com/flibioahk/ishido/archive/master.zip) - 复古益智游戏。论坛主题：[链接](https://autohotkey.com/boards/viewtopic.php?t=31825https://github.com/flibioahk/ishido)，GitHub：[链接](https://github.com/flibioahk/ishido)
* [ManyTetris](http://sector-seven.net/assets/stuff/ManyTetris.zip) - 多个俄罗斯方块变体。论坛主题：[链接](https://autohotkey.com/board/topic/35504-game-manytetris-customizable-pocket-tetris/)
* [Out of the Sea](http://ludumdare.com/compo/ludum-dare-24/?action=preview&uid=14126) - 尽量通过进化来避免被钓鱼。 GitHub：[链接](https://github.com/Uberi/Ludum-Dare-24)
* [PABI Logical](https://github.com/bichlepa/PABI-Logical/releases) - amiga 游戏 Logical 的重制版。论坛主题：[链接](https://autohotkey.com/boards/viewtopic.php?f=6&t=33267)，GitHub：[链接](https://github.com/bichlepa/PABI-Logical)
* [Sudoku](https://autohotkey.com/boards/codeboxplus/download/77645-1) - 数独游戏和求解器。论坛主题：[链接](https://autohotkey.com/boards/viewtopic.php?t=15291)

## <a name="tools"></a>工具
*有用的 AutoHotkey 工具列表。专为 AutoHotkey* 制作的工具

### 口译员
* [AutoHotkey](https://autohotkey.com/download/) - AutoHotkey 解释器安装程序和二进制文件。
* [AutoHotkey DLL](https://github.com/HotKeyIt/ahkdll-v1-release/) - AutoHotkey.dll 为其他编程和脚本语言打开了 AutoHotkey 的世界。论坛主题：[链接](https://autohotkey.com/board/topic/39588-autohotkeydll/)。文档[链接](http://hotkeyit.ahk4.net/files/AutoHotkey-txt.html)。
* [AutoHotkey build for CE](http://www.autohotkey.net/%7EMicha/AutohotkeyCE/AutoHotkeyCEUni.CAB) - 适用于掌上电脑/WinCE/智能手机的 AutoHotkey。论坛主题：[链接](https://autohotkey.com/board/topic/24776-autohotkey-for-pocket-pcs-wince-smartphones/)。文档[链接](http://www.autohotkey.net/~Micha/AutohotkeyCE/html/index.htm)。
* [AHK_X11](https://github.com/phil294/AHK_X11) phil294 针对 Linux 的 AutoHotkey v1.0.24 的基本但实用的实现。 [论坛](https://www.autohotkey.com/boards/viewtopic.php?f=81&t=106640)
* [IronAHK](https://github.com/polyethene/IronAHK) - 跨平台 .NET 重写 - *未完成*。
* [Keysharp](https://bitbucket.org/mfeemster/keysharp/src/master/) - mfeemster 的 IronAHK 的延续。 [论坛](https://www.autohotkey.com/boards/viewtopic.php?f=80&t=77248)

### 调试
* [[Class] Console](https://autohotkey.com/boards/viewtopic.php?f=6&t=2116) - 该类旨在简化脚本的调试，从简单的文本处理到输出和记录数据和数组。 GitHub [链接](https://github.com/AfterLemon/Class_Console)。
* [Print Array](https://autohotkey.com/board/topic/70490-print-array/) - 在 GUI 中打印数组内容的函数。
* [Yunit](https://github.com/Uberi/Yunit) - 由 Uberi 和 infogulch 开发 - AutoHotkey 的简单单元测试框架。

### 反编译器
* [AutoHotkey decompiler](https://gist.github.com/Uberi/3334552#file-decompiler-ahk) - AHK 1.1+ 论坛主题：[链接](https://autohotkey.com/board/topic/82986-ahk-l-decompiler-payload-method/)。
* [AutoHotkey decompiler - classic](https://autohotkey.com/docs/Scripts.htm#exe2ahk) - AHK 1.0 不适用于密码或 /nodecompile 受保护的文件。

### 集成开发环境
* [AHK Studio](https://autohotkey.com/boards/viewtopic.php?f=6&t=300) - 基于 SciLexer.dll 的 AutoHotkey IDE。
* [Adventure (formerly AutoGUI)](https://www.autohotkey.com/boards/viewtopic.php?f=64&t=89901) - 由 [Alguimist](https://autohotkey.com/boards/memberlist.php?mode=viewprofile&u=64723) - AHK IDE 提供有用的内置插件和 GUI 设计器。
* [AutoHotFlow](https://www.dropbox.com/s/99cwiqpzlx4mtuz/AutoHotFlow%20Installation.exe?dl=1) - 绘制您的应用程序。论坛主题：[链接](https://autohotkey.com/boards/viewtopic.php?f=6&t=6399)。 GitHub [链接](https://github.com/bichlepa/AutoHotFlow)。
* [DRAKON Editor](https://autohotkey.com/boards/viewtopic.php?f=6&t=3108) - AutoHotkey 的可视化编程（使用 DRAKON 图）。
* [Notepad++ for AutoHotkey](https://autohotkey.com/boards/viewtopic.php?f=7&t=50) - AutoHotkey 流行代码编辑器 Notepad++ 的设置。
* [SciTE4AutoHotkey](http://fincs.ahk4.net/scite4ahk/) - 基于 SciTE 的 AutoHotkey IDE。
* [SublimeAutoHotkey](https://github.com/ahkscript/SublimeAutoHotkey) - SublimeText 的 AutoHotkey AHK 语言包，包括语法突出显示、注释切换、自动完成、构建系统定义、ahkrun、ahkcompile、ahkrunpiped 命令。
* [Sublime 4 AutoHotkey](https://autohotkey.com/board/topic/91066-sublime-4-autohotkey-updated-1311/) - Sublime 4 AutoHotkey 是 Sublime Text 文本编辑器的补丁，增加了对 AutoHotkey 的支持。 -（已停产）
* [vim-AHKcomplete](https://github.com/huleiak47/vim-AHKcomplete) - Vim 插件添加自动完成功能。 （全方位完成）
* [Vim autohotkey-ahk](https://github.com/vim-scripts/autohotkey-ahk) - Vim 插件为 AutoHotkey 添加语法突出显示。
* [VSCode extension](https://marketplace.visualstudio.com/items?itemName=slevesque.vscode-autohotkey) - Visual Studio Code (VSCode) 插件为 AutoHotkey 添加语法突出显示。
* [AutoHotkey Plus Plus](https://marketplace.visualstudio.com/items?itemName=mark-wiemer.vscode-autohotkey-plus-plus) VS Code 的 AutoHotkey IntelliSense、调试和语言支持，由 Mark Wiemer 从 AutoHotkey Plus 由 cweijan 分叉

### GUI 所见即所得构建器
* [Adventure (formerly AutoGUI)](https://www.autohotkey.com/boards/viewtopic.php?f=64&t=89901) - 作者：[Alguimist](https://autohotkey.com/boards/memberlist.php?mode=viewprofile&u=64723) - WYSIWIG GUI 设计器和脚本编辑器。
* [GUI Creator (formerly Basic GUI Creator)](https://autohotkey.com/boards/viewtopic.php?f=6&t=303) - AutoHotkey 的所见即所得 GUI 创建器。
* [MagicBox](https://autohotkey.com/boards/viewtopic.php?p=100953#p100953) - by [Alguimist](https://autohotkey.com/boards/memberlist.php?mode=viewprofile&u=64723) - MagicBox 是一个辅助创建消息框的开发工具。论坛主题：[链接](https://autohotkey.com/boards/viewtopic.php?p=100953#p100953)。

### 脚本记录者和作家
* [Pulover’s Macro Creator](http://www.macrocreator.com/) - 免费的自动化工具和脚本生成器。推荐给初学者。论坛主题：[链接](https://autohotkey.com/boards/viewtopic.php?f=6&t=143)。 GitHub [链接](https://github.com/Pulover/PuloversMacroCreator)。

### 网络语法荧光笔
* [highlight.js](https://highlightjs.org/) - 用 JavaScript 编写的语法荧光笔，支持 130 多种语言（包括 AutoHotkey）。
* [PrismJs](https://autohotkey.com/boards/viewtopic.php?f=22&t=3942) - 轻量级最小 AutoHotkey 语法突出显示。
* [Syntax Highlighter](https://github.com/aviaryan/highlighter-ahk-zenburn) - AutoHotkey 的旧版语法荧光笔默认支持行号。

### <a name="tools-others"></a>其他
* [GoTo](https://autohotkey.com/board/topic/95009-) - 适用于任何文本编辑器的插件，可帮助您跳转到活动文件中的标签、热键、热字符串和函数。
* [GoToTilla](https://gist.github.com/hoppfrosch/4b4943b1311fd6a92f02) - 允许跳转到 AHK 源代码中的令牌的插件。
* [Context sensitive help in any editor](https://autohotkey.com/board/topic/94493-) - 适用于任何文本编辑器的插件，可通过按 F1 提供上下文相关帮助。
* [CodeQuickTester](https://autohotkey.com/boards/viewtopic.php?f=6&t=6113) - by GeekDude - 一个轻量级的动态代码测试器。
* [iWB2 Learner](https://sourceforge.net/projects/ahkcn/files/Recommended/iWB2%20Learner/) - 作者：jethro - iWB2 Learner 是一个用于收集有关 Internet Explorer 网页信息的工具。论坛主题：[链接](https://autohotkey.com/board/topic/84258-iwb2-learner-iwebbrowser2/)
* [AHK-EXE-Swapper](https://autohotkey.com/boards/viewtopic.php?f=6&t=6310) - byvillainC - 赶紧换AHK版本吧！论坛主题：[链接](https://autohotkey.com/boards/viewtopic.php?f=6&t=6310)。
* [AEI](https://github.com/joedf/AEI.ahk) - by joedf - 显示 AutoHotkey 环境信息和 AHK 支持相关系统信息，并带有一个带有进度条自动下载的精美更新检查器.论坛主题：[链接](https://autohotkey.com/boards/viewtopic.php?f=6&t=5825)。
* [WinSpy](https://autohotkey.com/boards/viewtopic.php?f=6&t=28220) - by Alguimist - 用 AHK 编写的有用的窗口间谍/信息工具。

### （用于）其他编程语言
* [AutoHotkey.dll](https://hotkeyit.github.io/v2/docs/AutoHotkeyDll.htm) - [AutoHotkey_H](#autohotkey_h) 发行版的一部分。从您的其他语言加载 autohotkey.dll，并将正常的 AHK 代码传递到 dll 文件以执行。请参阅此处以获取[导出函数](https://hotkeyit.github.io/v2/docs/AHKH_Features.htm)的列表。一些较旧的链接：[python示例](https://autohotkey.com/board/topic/56938-simple-python-intergration-example/)、[c/c++示例](https://autohotkey.com/board/topic/39588-autohotkeydll/://autohotkey.com/board/topic/39588-autohotkeydll/page-10?&#entry321945)、[论坛链接](https://autohotkey.com/board/topic/39588-autohotkeydll/)
* [.NET Framework Interop (CLR, C#, VB)](https://dl.dropbox.com/u/20532918/Lib/CLR-1.2.zip) - 论坛主题：[链接](https://autohotkey.com/boards/viewtopic.php?f=6&t=4633)。
* [ActiveScript - Host VBScript and JScript in-process](https://autohotkey.com/boards/viewtopic.php?f=6&t=4555) - 提供与 VBScript 和 JScript 等活动脚本语言的接口，而不依赖于 64 位程序无法使用的 Microsoft ScriptControl。
* [Exo-Javascript](https://github.com/Aurelain/Exo) - 使用 JavaScript 编写 AHK - 论坛帖子：[链接](https://autohotkey.com/boards/viewtopic.php?f=6&t=5714)、Exo-CLI（交互式命令行）[链接](https://github.com/joedf/Exo-CLI.ahk)。
* [LibLua](https://autohotkey.com/board/topic/40690-ahk-lua-interop-stdlib-proof-of-concept/) - *注意：lua.ahk 和 lua_ahkfunctions.ahk 可以在[此处](https://code.google.com/archive/p/wow-vending-machine/source)*找到。
* [Machine code functions: Bit Wizardry](https://autohotkey.com/board/topic/19483-machine-code-functions-bit-wizardry/) - 教程 [链接](https://autohotkey.com/boards/viewtopic.php?f=7&t=32)，C/C++ 到 MCode Generator 论坛 [链接](https://autohotkey.com/boards/viewtopic.php?f=6&t=4642)。
* [Embed Perl](http://thomaslauer.com/comp/Calling_Perl_from_AHK_or_AU3) - 论坛主题：[链接](https://autohotkey.com/board/topic/11249-embedding-perl/)。
* [PAHK](https://code.google.com/archive/p/pahk) - 论坛主题：[链接](https://autohotkey.com/board/topic/89022-pahk-python-package-to-extend-python-with-autohotkey/)。
* [PYAHK](https://bitbucket.org/kitsu/pyahk/downloads) - 文档[链接](https://pyahk.readthedocs.io/en/latest/)。
* [ahk](https://github.com/spyoungtech/ahk) - AutoHotkey 的 Python 包装器 - 论坛帖子：[链接](https://www.autohotkey.com/boards/viewtopic.php?f=6&t=63184)
* [AutoHotkey.py](https://github.com/Perlence/AutoHotkey.py) - 用 Python 编写 AutoHotkey 脚本 - 论坛帖子：[链接](https://www.autohotkey.com/boards/viewtopic.php?f=6&t=86025)

## 教程
*有用的 AutoHotkey 教程列表。*

### <a name="tutorials-classes"></a>课程
* [Classes in AHK, Basic tutorial](https://autohotkey.com/boards/viewtopic.php?f=7&t=6033) - AutoHotkey 类基础教程。
* [Classes in AHK, a Dissection (Advanced)](https://autohotkey.com/boards/viewtopic.php?f=7&t=6177) - AutoHotkey 类高级教程。

### <a name="tutorials-com"></a>COM
* [MS Office COM Basics](https://autohotkey.com/boards/viewtopic.php?f=7&t=8978) - 将 AutoHotkey 与 MS Office 结合使用。

### <a name="tutorials-gui"></a>图形用户界面
* [Use HTML and CSS for your GUIs!](https://autohotkey.com/boards/viewtopic.php?f=7&t=4588) - 使用 HTML 和 CSS 创建 GUI。

### <a name="tutorials-mcode"></a>MCode（机器代码）
* [MCode Tutorial](https://autohotkey.com/boards/viewtopic.php?f=7&t=32) - MCode（机器代码）教程。

## 资源
*有用的 AutoHotkey 资源列表。与 AutoHotkey 相关的各种网站、文档、指南、视频和文章。*

### 文档
* [Official documentation](https://autohotkey.com/docs/AutoHotkey.htm) - 官方更新 AutoHotkey 文档。 GitHub [链接](https://github.com/Lexikos/AutoHotkey_L-Docs)。
 
### 书籍
* [ahkbook](http://ahkscript.github.io/ahkbook/projectinfo.html) - 一本关于 AutoHotkey 的书（尚未完成）。论坛主题：[链接](https://autohotkey.com/board/topic/73014-ahkbook-a-free-online-book-for-autohotkey/)。

### 快速入门指南
* [Official quick start tutorial](https://autohotkey.com/docs/Tutorial.htm) - 官方快速入门教程 - 最初由 tidbit 编写。论坛主题：[链接](https://autohotkey.com/boards/viewtopic.php?f=7&t=27)。

### 网站
* [autohotkey.com](https://autohotkey.com/) - AutoHotkey 脚本语言的官方网站（下载、论坛、文档）。
* [autohotkey.com/foundation](https://autohotkey.com/foundation) - [AutoHotkey Foundation LLC](https://autohotkey.com/foundation/) 的官方网页，这是一家为此软件成立的非营利性 LLC（有限责任公司）。组织证书 (pdf) [链接](https://autohotkey.com/certificate_of_organization.pdf)。
* [ahkscript GitHub organization](https://github.com/ahkscript) - 官方 ahkscript GitHub 组织。

## 叉子
*AHK 的分支为核心语言添加了新功能*

### 自动热键_H
* [AutoHotkey_H](https://hotkeyit.github.io/v2/) - AHK_H 在原始 AutoHotkey 的基础上添加了功能，并使用 NewThread() 函数或 AutoHotkey.dll 提供真正的多线程。 [v1 更改的完整列表](https://hotkeyit.github.io/v1/docs/AutoHotkey.htm) + [v2 更改的完整列表](https://hotkeyit.github.io/v2/docs/AutoHotkey.htm)

## 许可证

[![Creative Commons License](https://licensebuttons.net/l/by/4.0/88x31.png)](http://creativecommons.org/licenses/by/4.0/)

本作品根据 [知识共享署名 4.0 国际许可证](http://creativecommons.org/licenses/by/4.0/) 获得许可。
