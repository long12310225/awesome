# 很棒的 VBA！[VBALogo](./resources/VBALogo.png) [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

Visual Basic for Applications (VBA) 是 Microsoft 事件驱动编程语言 Visual Basic 6.0 (VB6) 的实现，内置于大多数桌面 Microsoft Office 应用程序中。

这是 VBA 和 VB6 的库和资源的精选列表。

由于 VBA 的性质，许多库并不适用于所有操作系统、所有 Office 应用程序或所有体系结构 (x64/x86)，因此我们使用符号系统。 [在这里阅读更多相关信息](#symbology)。

## 内容

- [图书馆藏书](#library-collections)
- [Libraries](#libraries)
  - [嵌入式编程语言](#embedded-programming-languages)
  - [数据格式（JSON、CSV、XML 等）](#data-formats)
  - [数据结构（数组列表和字典）](#data-structures)
  - [数学库](#math-libraries)
  - [数据库工具](#database-tools)
  - [用户表单工具](#userform-tools)
  - [低级工具](#low-level-tools)
  - [解析器/解释器](#parsers--interpreters)
  - [网络工具](#web-tools)
- [开发者工具](#developer-tools)
- [Examples](#examples)
  - [算法、代码优化和性能测试](#algorithms-code-optimisation-and-performance-testing)
  - [用户界面功能区](#ui-ribbon)
  - [用户界面用户表单](#ui-userforms)
  - [低级示例](#low-level-examples)
  - [AddIns](#addins)
  - [游戏/有趣的项目](#games--fun-projects)
- [外部工具](#external-tools)
- [风格指南](#style-guides)
- [Information](#information)
- [Resources](#resources)
  - [Win32 API 资源](#win32-api-resources)
  - [VB6 / VBScript](#vb6--vbscript)
  - [Websites](#websites)
  - [Books](#books)
  - [YouTube](#youtube)
  - [Forums](#forums)

---

## 图书馆藏书

- [![p_win]](#-) [![p_nom]](#-) [![a_all]](#-) ![GHStars](https://img.shields.io/github/stars/sancarn/stdVBA?style&logo=github&label) [stdVBA](http://github.com/sancarn/stdVBA) - 包含许多自动化和实用类的框架。注重代码紧凑性和长期可维护性。
- [![p_win]](#-) [![p_nom]](#-) [![a_all]](#-) [![o_32]](#-) ![GHStars](https://img.shields.io/github/stars/kellyethridge/VBCorLib?style&logo=github&label) [VbCorLib](https://github.com/kellyethridge/VBCorLib) - 一个框架，它带来了许多强大的 .NET 类到 VBA/VB6。
- [![p_win]](#-) [![p_nom]](#-) [![a_all]](#-) ![GHStars](https://img.shields.io/github/stars/RelaxTools/Hidennotare?style&logo=github&label) [Hidennotare](https://github.com/RelaxTools/Hidennotare) - 日本作者 RelaxTools 的框架。包含大量的类、接口和表单。

## 图书馆

### 嵌入式编程语言

- [![p_win]](#-) [![p_mac]](#-) [![a_all]](#-) ![GHStars](https://img.shields.io/github/stars/ECP-Solutions/ASF?style&logo=github&label) [高级脚本框架 (ASF)](https://github.com/ECP-Solutions/ASF) - 具有类似 JavaScript 的完整脚本平台语法、原生 Office 生态系统集成、继承类、专业调试、零依赖和 VS Code 扩展。
- [![p_win]](#-) [![p_nom]](#-) [![a_all]](#-) ![GHStars](https://img.shields.io/github/stars/jet2jet/vb2clr?style&logo=github&label) [vb2clr](https://github.com/jet2jet/vb2clr) - 使用 .NET CLR 从 VBA 使用 C#运行时。
- [![p_win]](#-) [![p_mac]](#-) [![a_all]](#-) ![GHStars](https://img.shields.io/github/stars/ECP-Solutions/VBA-Expressions?style&logo=github&label) [VBA 表达式](https://github.com/ECP-Solutions/VBA-Expressions) - 强大的字符串表达式计算器专注于数学和数据处理。
- 来自图书馆馆藏：
- [![p_win]](#-) [![p_nom]](#-) [![a_all]](#-) 在 `stdVBA` 中找到 `stdLambda` - 完整的编程语言，包括对象操作、调用堆栈等。
	
### 数据格式

#### JSON

- [![p_win]](#-) [![p_mac]](#-) [![a_all]](#-) ![GHStars](https://img.shields.io/github/stars/cristianbuse/VBA-FastJSON?style&logo=github&label) [VBA-FastJSON](https://github.com/cristianbuse/VBA-FastJSON) - 快速、跨平台、原生json 解析器和序列化器。内存高效（非递归）、符合 RFC 8259、UTF8 支持
- [![p_win]](#-) [![p_nom]](#-) [![a_all]](#-) [mdJSON](https://www.vbforums.com/showthread.php?871695-VB6-VBA-JSON-parsing-to-built-in-VBA-Collections-with-JSON-Path-support) - 用于提取路径的点符号的 JSON 库。
- [![p_win]](#-) [![p_nom]](#-) [![a_all]](#-) [JSONBag](https://www.vbforums.com/showthread.php?738845-VB6-JsonBag-Another-JSON-Parser-Generator) - 使用 shebang 表示法从 JSON 字符串中提取密钥。还可以使用此库构建 JSON。
- 来自图书馆馆藏：
- [![p_win]](#-) [![p_nom]](#-) [![a_all]](#-) 在 `stdVBA` 中找到 `stdJSON` - 如上所述。

#### CSV

- [![p_win]](#-) [![p_mac]](#-) [![a_all]](#-) ![GHStars](https://img.shields.io/github/stars/ws-garcia/VBA-CSV-interface?style&logo=github&label) [VBA-CSV-interface](https://github.com/ws-garcia/VBA-CSV-interface) - 功能强大，速度快以及符合 RFC-4180 的综合 CSV/TSV/DSV 数据管理库。
- 来自图书馆馆藏：
- [![p_win]](#-) [![p_nom]](#-) [![a_all]](#-) 在 `Hidennotare` 中找到 `csvWriter` 和 `csvReader`。

#### XML

- [![p_win]](#-) [![p_mac]](#-) [![a_all]](#-) ![GHStars](https://img.shields.io/github/stars/VBA-tools/VBA-XML?style&logo=github&label) [VBA-XML](https://github.com/VBA-tools/VBA-XML) - XML 转换和解析。

#### 邮政编码

- [![p_win]](#-) [![p_nom]](#-) [![a_all]](#-) ![GHStars](https://img.shields.io/github/stars/cristianbuse/Excel-ZipTools?style&logo=github&label) [Excel-ZipTools](https://github.com/cristianbuse/Excel-ZipTools/tree/master) - 解析、读取和从 Zip 文件中提取数据。纯vba编写。
- [![p_win]](#-) [![p_nom]](#-) [![a_all]](#-) ![GHStars](https://img.shields.io/github/stars/KallunWillock/vbaSquash?style&logo=github&label) [vbaSquash](https://github.com/KallunWillock/vbaSquash/tree/master) - 压缩并使用 Windows 8+ 上提供的内置“cabinet.dll”函数解压缩文件和字节数组。提供对压缩算法“MSZIP”、“XPRESS”、“XPRESS_HUFF”和“LZMS”的访问。

#### PDF

- [![p_win]](#-) [![p_mac]](#-) [![a_all]](#-) ![GHStars](https://img.shields.io/github/stars/PerditionC/vbaPDF?style&logo=github&label) [vbaPDF](https://github.com/PerditionC/vbaPDF) - 用于简单修改 PDF 文件的 VBA 代码（读入、合并、写入）出）。

### 数据结构

#### 数组列表

- [![p_win]](#-) [![p_mac]](#-) [![a_all]](#-) ![GHStars](https://img.shields.io/github/stars/Senipah/VBA-Better-Array?style&logo=github&label) [更好的数组](https://github.com/Senipah/VBA-Better-Array/tree/master/src) - 数组类提供更现代语言中的功能。
- 来自图书馆馆藏：
- [![p_win]](#-) [![p_nom]](#-) [![a_all]](#-) [![o_32]](#-) 在 `VbCorLib` 中找到 `ArrayList` - 如上所述。
- [![p_win]](#-) [![p_nom]](#-) [![a_all]](#-) 在 `stdVBA` 中找到 `stdArray` - 如上所述。还包括搜索数组或从回调执行检查的方法。


#### 词典

- [![p_win]](#-) [![p_mac]](#-) [![a_all]](#-) ![GHStars](https://img.shields.io/github/stars/cristianbuse/VBA-FastDictionary?style&logo=github&label) [VBA-FastDictionary](https://github.com/cristianbuse/VBA-FastDictionary) -快速、跨平台、原生词典。脚本字典的替代品。
- [![p_win]](#-) [![p_mac]](#-) [![a_all]](#-) ![GHStars](https://img.shields.io/github/stars/VBA-tools/VBA-Dictionary?style&logo=github&label) [VBA-Dictionary](https://github.com/VBA-tools/VBA-Dictionary) - 存储的字典对象键值对。
- [![p_win]](#-) [![p_nom]](#-) [![a_all]](#-) ![GHStars](https://img.shields.io/github/stars/SSlinky/VBA-ExtendedDictionary?style&logo=github&label) [VBA-ExtendedDictionary](https://github.com/SSlinky/VBA-ExtendedDictionary) - 使用的字典对象Scripting.Dictionary 但公开了一些额外的有用功能。
- [![p_win]](#-) [![p_mac]](#-) [![a_all]](#-) [cHashList](https://www.vbforums.com/showthread.php?834515-Simple-and-fast-lightweight-HashList-Class-(no-APIs)) - 简单、快速且轻量级的 HashList 类，不使用 Win32 API。但是需要字符串键。
- [![p_win]](#-) [![p_nom]](#-) [![a_all]](#-) [CollectionEx](https://www.vbforums.com/showthread.php?834579-Wrapper-for-VB6-Collections) - 使用检索和检查键是否存在的方法扩展默认 VBA(/VB6) 集合。 <!--TODO: 这被列为 p_win，但老实说，如果有正确的 API 声明，这可能在 mac 上工作。值得测试，请参阅 MemoryTools for Copy Memory 声明-->
- [![p_win]](#-) [![p_nom]](#-) [![a_all]](#-) [![o_32]](#-) [clsTrickHashTable](https://www.vbforums.com/showthread.php?788247-VB6-Hash-table) - 使用运行时注入的机器代码的哈希表。完全替代脚本字典，具有额外功能。
- 来自图书馆馆藏：
- [![p_win]](#-) [![p_nom]](#-) [![a_all]](#-) [![o_32]](#-) 在 `VbCorLib` 中找到 `HashTable` - 如上所述。
    <!-- Hidennotare, though it simply wraps Scripting.Dictioanry... -->

### 数学库

- [![p_win]](#-) [![p_mac]](#-) [![a_all]](#-) ![GHStars](https://img.shields.io/github/stars/Beakerboy/VBA-Math-Objects?style&logo=github&label) [VBA-Math-Objects](https://github.com/Beakerboy/VBA-Math-Objects) - 矩阵和向量图书馆。
- [![p_win]](#-) [![p_mac]](#-) [![a_all]](#-) ![GHStars](https://img.shields.io/github/stars/ws-garcia/VBA-float?style&logo=github&label) [VBA Float](https://github.com/ws-garcia/VBA-float ) - 执行计算的实用程序大整数和有数千位的有理数。

### 数据库工具

- [![p_win]](#-) [![p_nom]](#-) [![a_xl]](#-) [![o_dll]](#- '需要外部 DLL') ![GHStars](https://img.shields.io/github/stars/EtienneLenoir/duckdb-vba?style&logo=github&label) [DuckDB VBA](https://github.com/EtienneLenoir/duckdb-vba) - 用于 Excel/VBA 的嵌入式 DuckDB OLAP 引擎，通过轻量级 DLL 桥使用本机 DuckDB C API。无需 ODBC 设置或外部服务器；支持快速 DuckDB SQL 分析、字典查找、范围/数组摄取、Parquet/CSV/JSON 工作流程、DuckDB/SQLite/PostgreSQL 连接以及 Access-to-DuckDB 迁移。

- [![p_win]](#-) [![p_nom]](#-) [![a_all]](#-) ![GHStars](https://img.shields.io/github/stars/Beakerboy/VBA-SQL-Library?style&logo=github&label) [SQL 库](https://github.com/Beakerboy/VBA-SQL-Library) - psql 的 OOP SQL 库， mssql、mysql数据库。

### 用户表单工具

- [![p_win]](#-) [![p_nom]](#-) [![a_all]](#-) ![GHStars](https://img.shields.io/github/stars/fafalone/cTaskDialog64?style&logo=github&label) [任务对话框](https://github.com/fafalone/cTaskDialog64) - 此 1 类中的大量 UI 功能，严格动态和模块化的方式。非常适合数据输入表单。另请参阅 [vbforums](https://www.vbforums.com/showthread.php?777021-VB6-TaskDialogIndirect-Complete-class-implementation-of-Vista-Task-Dialogs) 帖子以获取更多信息。
- [![p_win]](#-) [![p_nom]](#-) [![a_all]](#-) ![GHStars](https://img.shields.io/github/stars/fafalone/ucSimplePlayer?style&logo=github&label) [![o_dll]](#- '需要外部 OCX') [ucSimplePlayer](https://github.com/fafalone/ucSimplePlayer) - 简单的视频播放器用户控件。
- [![p_win]](#-) [![p_nom]](#-) [![a_all]](#-) ![GHStars](https://img.shields.io/github/stars/fafalone/ucWebView2?style&logo=github&label) [![o_dll]](#- '需要外部 OCX') [ucWebView2](https://github.com/fafalone/ucWebView2) - WebView2 用户控件。
- [![p_win]](#-) [![p_nom]](#-) [![a_all]](#-) ![GHStars](https://img.shields.io/github/stars/fafalone/ucAniGifEx?style&logo=github&label) [![o_dll]](#- '需要外部 OCX') [ucAniGifEx](https://github.com/fafalone/ucAniGifEx) - 动画 GIF 用户控件。
- [![p_win]](#-) [![p_nom]](#-) [![a_all]](#-) ![GHStars](https://img.shields.io/github/stars/todar/VBA-Material-Design?style&logo=github&label) [Material UI](https://github.com/todar/VBA-Material-Design) - 使用 Material UI 让您的用户窗体感觉现代。
- [![p_win]](#-) [![p_mac]](#-) [![a_all]](#-) ![GHStars](https://img.shields.io/github/stars/todar/VBA-Userform-EventListener?style&logo=github&label) [Easy EventListener](https://github.com/todar/VBA-Userform-EventListener) - 整合所有事件处理将一个用户表单放入 1 个回调中。
- [![p_win]](#-) [![p_nom]](#-) [![a_all]](#-) [伪控制数组](http://addinbox.sakura.ne.jp/Breakthrough_P-Ctrl_Arrays_Eng.htm) - 合并用户窗体的所有事件处理的最佳方法。演示“ConnectToConnectionPoint” API 的用法。也值得一看[此类](https://stackoverflow.com/questions/61855925/reducing-withevent-declarations-and-subs-with-vba-and-activex#answer-61893857)。
- [![p_win]](#-) [![p_nom]](#-) [![a_all]](#-) ![GHStars](https://img.shields.io/github/stars/krishKM/Modern-UI-Components-for-VBA?style&logo=github&label) [![o_dll]](#- '需要外部 DLL') [现代 UI Components](https://github.com/krishKM/Modern-UI-Components-for-VBA) - 自定义现代外观控件。
- [![p_win]](#-) [![p_nom]](#-) [![a_all]](#-) ![GHStars](https://img.shields.io/github/stars/rubberduck-vba/MVVM?style&logo=github&label) [MVVM](https://github.com/rubberduck-vba/MVVM) - 用于可维护的用户表单开发的模型-视图-视图模型基础设施。
- [![p_win]](#-) [![p_nom]](#-) [![a_all]](#-) ![GHStars](https://img.shields.io/github/stars/todar/VBA-Userform-Animations?style&logo=github&label) [VBA 用户表单转换和动画](https://github.com/todar/VBA-Userform-Animations) - 一个优秀的实现库动画缓动到用户窗体中。
- [![p_win]](#-) [![p_nom]](#-) [![a_all]](#-) ![GHStars](https://img.shields.io/github/stars/thetrik/VbTrickTimer?style&logo=github&label) [Trick's Timer](https://github.com/thetrik/VbTrickTimer) - 如果您需要连续运行一段代码并且无法访问“Application.OnTime”（和/或您需要以超过每秒一次的速度运行它），这就是适合您的课程！另请查看[论坛帖子](https://www.vbforums.com/showthread.php?875635-VB6-VBA-Timer-class)以获取更多信息。限制：需要模态形式。
- [![p_win]](#-) [![p_nom]](#-) [![a_all]](#-) ![GHStars](https://img.shields.io/github/stars/cristianbuse/VBA-SafeTimer?style&logo=github&label) [VBA-SafeTimer](https://github.com/cristianbuse/VBA-SafeTimer) - 可靠， VBA 的无崩溃计时器。可以安全地调试和停止代码。有或没有表格均可使用。
- [![p_win]](#-) [![p_nom]](#-) [![a_all]](#-) [拖放文件路径](https://www.mrexcel.com/board/threads/vba-drag-drop-filepath.843330/page-6#post-5898495) - 允许您的用户表单处理拖放文件。
- [![p_win]](#-) [![p_nom]](#-) [![a_all]](#-) [后期绑定 Web 浏览器控件事件](https://www.vbforums.com/showthread.php?847773-VB6-elevated-IE-Control-usage-with-HTML5-elements-and-COM-Event-connectors) - 一种在 a 中锁定 Web 浏览器事件的技术后期绑定方式。
- [![p_win]](#-) [![p_nom]](#-) [![a_all]](#-) [![o_paid]](#- '~每个控件/应用程序 2 英镑') [Mark 的用户表单工具](https://www.kubiszyn.co.uk/) - 众多 UI 工具和漂亮的用户表单。
- [![p_win]](#-) [![p_nom]](#-) [![a_all]](#-) ![GHStars](https://img.shields.io/github/stars/cristianbuse/VBA-UserForm-MouseScroll?style&logo=github&label) [VBA-UserForm-MouseScroll](https://github.com/cristianbuse/VBA-UserForm-MouseScroll) - 允许在 MSForms 控件和用户窗体上滚动鼠标滚轮。
- [![p_win]](#-) [![p_mac]](#-) [![a_all]](#-) [MSForms（纯 VBA）树视图控件](https://jkp-ads.com/Articles/treeview.asp) - JKP 和 Peter Thornton 完全用 VBA 编码的树视图控件替代品。
- [![p_win]](#-) [![p_mac]](#-) [![a_all]](#-) [MSForms（纯 VBA）列表框控件](https://app.monstercampaigns.com/c/fxzxd8wfvl4mnf4zmnp3/) - 精选于[此]视频](https://www.youtube.com/watch?v=QYW1SlKfKdM)。它具有大量有用的功能，例如排序、过滤、单选或多选（带有全选和取消全选）、页面导航和悬停突出显示，
- [![p_win]](#-) [![p_nom]](#-) [![a_all]](#-) [自定义用户表单标题栏颜色](https://www.mrexcel.com/board/threads/using-winapi-to-change-the-color-on-the-title-bar-of-a-userform.1205894/page-2#post-5892050)
- [![p_win]](#-) [![p_nom]](#-) [![a_all]](#-) [多色列表框类](https://www.mrexcel.com/board/threads/multicolor-drag-n-drop-listbox-class-win32.1206334/)
- [![p_win]](#-) [![p_nom]](#-) [![a_all]](#-) [在 VBA 中使用 GDIPlus](https://arkham46.developpez.com/articles/office/clgdiplus/) - GDIPlus 可用于创建类似“canvas”的元素，可以在其中绘制任何图像。另外请查看同一作者的这个 [GDI32](https://arkham46.developpez.com/articles/office/clgdi32/) 类。
- [![p_win]](#-) [![p_nom]](#-) [![a_all]](#-) [在 VBA 中使用 OpenGL](https://arkham46.developpez.com/articles/office/vbaopengl/?page=Page_1) - OpenGL 是一个跨语言、跨平台的应用程序编程接口，用于渲染 2D 和 3D 矢量图形。在本文中，GDIPlus 类的作者。
- [![p_win]](#-) [![p_nom]](#-) [![a_all]](#-) [![o_32]](#-) [VB6 Graph Control](https://vb6awards.blogspot.com/2017/11/vb6-graph-control.html) - 如果没有 `PictureBox` 兼容替代品，则无法在 VBA 中本地工作，但性能极高无论如何，图形控制。
- [![p_win]](#-) [![p_nom]](#-) [![a_xl]](#-) ![GHStars](https://img.shields.io/github/stars/tarboh/WebView2-For-Excel-VBA?style&logo=github&label) [WebView2 for Excel VBA](https://github.com/tarboh/WebView2-For-Excel-VBA) – A轻量级包装器，在用户窗体上公开 Microsoft Edge WebView2，支持 HTML/JS UI、渲染以及与 VBA 的双向通信。有效替代了 WebBrowser 控件。

### 低级工具

- [![p_win]](#-) [![p_mac]](#-) [![a_all]](#-) ![GHStars](https://img.shields.io/github/stars/cristianbuse/VBA-MemoryTools?style&logo=github&label) [VBA-MemoryTools](https://github.com/cristianbuse/VBA-MemoryTools) -提供超快的复制内存替代方案。
- [![p_win]](#-) [![p_nom]](#-) [![a_all]](#-) [安全子类化](https://www.mrexcel.com/board/threads/intercepting-resetting-of-vba-editor-as-well-as-unhandled-errors-for-safe-subclassing.1024295/) - 提供子类化 Excel/Word/PowerPoint 的功能窗口或用户表单以执行进一步的自动化。在后面的线程中还有一个从其他应用程序子类化其他窗口的示例。
- [![p_win]](#-) [![p_nom]](#-) [![a_all]](#-) ![GHStars](https://img.shields.io/github/stars/Greedquest/vbInvoke?style&logo=github&label) [调用私有模块函数](https://github.com/Greedquest/vbInvoke/tree/main) - 您也可以查看[Greedo 的代码审查](https://codereview.stackexchange.com/questions/274532/low-level-vba-hacking-making-private-functions-public)。
- [![p_win]](#-) [![p_nom]](#-) [![a_all]](#-) [![o_32]](#-) [通用 DLL 调用](http://www.vbforums.com/showthread.php?781595-VB6-Call-Functions-By-Pointer-(Universall-DLL-Calls)) - 可以使用的库在“STDCALL”和“CDECL”中调用任何函数指针、DLL 或对象的函数。
- [![p_win]](#-) [![p_nom]](#-) [![a_all]](#-) ![GHStars](https://img.shields.io/github/stars/Greedquest/vbInvoke?style&logo=github&label) [vbInvoke](https://github.com/Greedquest/vbInvoke) - `Application.Run` 但基于 COM，可以调用私有模块方法。
- [![p_win]](#-) [![p_mac]](#-) [![a_all]](#-) ![GHStars](https://img.shields.io/github/stars/cristianbuse/VBA-StateLossCallback?style&logo=github&label) [VBA 状态丢失回调](https://github.com/cristianbuse/VBA-StateLossCallback) - A用于 VBA 状态丢失的无崩溃检测器。在以下情况下可能会发生状态丢失： 有人在未处理的错误中单击“结束”；单击VBA停止按钮；您进入设计模式；应用程序退出。
- [![p_win]](#-) [![p_nom]](#-) [![a_all]](#-) ![GHStars](https://img.shields.io/github/stars/Ariche2/VBAStack?style&logo=github&label) [VBAStack](https://github.com/Ariche2/VBAStack) - 用于在运行时从 Office 应用程序检索 VBA 调用堆栈信息的库。作者还做了一个【纯VBA原生版本】(https://www.reddit.com/r/vba/comments/1qrf29m/update_to_vbastack_can_now_work_in_vba6_as_well/)。
- 来自图书馆馆藏：
- [![p_win]](#-) [![p_nom]](#-) [![a_all]](#-) 在 `stdVBA` 中找到 `stdCOM` - COM 自动化的一站式商店，从通过偏移量调用接口到提取类型信息。
- [![p_win]](#-) [![p_nom]](#-) [![a_all]](#-) 在 `stdVBA` 中找到 `stdReg` - 从搜索到设置值的注册表自动化。

### 解析器/解释器

- [![p_win]](#-) [![p_nom]](#-) [![a_all]](#-) ![GHStars](https://img.shields.io/github/stars/sihlfall/vba-regex?style&logo=github&label) [vba-regex](https://github.com/sihlfall/vba-regex) - 原生正则表达式解析器和运行时引擎。
- [![p_win]](#-) [![p_nom]](#-) [![a_all]](#-) ![GHStars](https://img.shields.io/github/stars/wqweto/VbPeg?style&logo=github&label) [VbPeg](https://github.com/wqweto/VbPeg) - VBA 的解析器生成器。将像[this](https://github.com/wqweto/VbPeg/blob/master/test/Runner/peg/Kscope/grammar.peg)这样的PEG语法转换成[像这样的VBA代码](https://github.com/wqweto/VbPeg/blob/master/test/Runner/peg/Kscope/cKscope.cls)。如果您在 VBA 中实现新的编程语言，则非常有用。 Wqweto 还包含一些数学表达式解析器作为测试。
- [![p_win]](#-) [![p_mac]](#-) [![a_all]](#-) [Volpi 的数学表达式解析器](https://web.archive.org/web/20100703220609/http://digilander.libero.it/foxes/mathparser/MathExpressionsParser.htm) - 快速数学表达式解析器。不允许调用对象，没有调用堆栈。
- [![p_win]](#-) [![p_nom]](#-) [![a_all]](#-) ![GHStars](https://img.shields.io/github/stars/Excel-lent/ClooWrapperVBA?style&logo=github&label) [ClooWrapperVBA](https://github.com/Excel-lent/ClooWrapperVBA) - 从 VBA 执行 OpenCL，使用 GPU 或 CPU。

### 网络工具

- [![p_win]](#-) [![p_mac]](#-) [![a_all]](#-) ![GHStars](https://img.shields.io/github/stars/VBA-tools/VBA-Web?style&logo=github&label) [VBA-Web](https://github.com/VBA-tools/VBA-Web) - 连接 VBA、Excel、Access 和 Office for Windows 和Mac 到 Web 服务和 Web。
- [![p_win]](#-) [![p_nom]](#-) [![a_all]](#-) ![GHStars](https://img.shields.io/github/stars/vbacollective/wasabi?style&logo=github&label) [Wasabi](https://github.com/vbacollective/wasabi) - 原生 WebSocket、WSS、MQTT 和原始 TCP 客户端VBA。纯VBA、单文件、零依赖。
- [![p_win]](#-) [![p_mac]](#-) [![a_all]](#-) ![GHStars](https://img.shields.io/github/stars/EagleAglow/vba-websocket-async?style&logo=github&label) [VBA-WebSocket](https://github.com/EagleAglow/vba-websocket) - Microsoft 示例代码用于可与回显服务器结合使用的 WebSocket 客户端。还有由微软代码的发现者构建的[一个类](https://github.com/EagleAglow/vba-websocket-class)和一个[异步版本](https://github.com/EagleAglow/vba-websocket-async)。
- [![p_win]](#-) [![p_nom]](#-) [![a_all]](#-) [![o_32]](#-) ![GHStars](https://img.shields.io/github/stars/wqweto/VbAsyncSocket?style&logo=github&label) [vbAsyncSocket](https://github.com/wqweto/VbAsyncSocket) - VB6 的简单而精简的 WinSock API 包装器松散地基于 MFC 中的原始 CAsyncSocket 包装器。
- [![p_win]](#-) [![p_nom]](#-) [![a_all]](#-) ![GHStars](https://img.shields.io/github/stars/sancarn/stdVBA-Inspiration?style&logo=github&label) [边缘自动化](https://www.codeproject.com/Tips/5307593/Automate-Chrome-Edge-using-VBA) - 使用 devtools 协议自动化 Chromium Edge。 [此处 GitHub 备份](https://github.com/sancarn/stdVBA-Inspiration/tree/master/ChromeEdgeAutomation)。
- [![p_win]](#-) [![p_nom]](#-) [![a_all]](#-) ![GHStars](https://img.shields.io/github/stars/PerditionC/VBAChromeDevProtocol?style&logo=github&label) [Chrome 自动化（通过 devtools 协议）](https://github.com/PerditionC/VBAChromeDevProtocol) -使用 chrome devtools 协议自动化 Chrome。
- [![p_win]](#-) [![p_nom]](#-) [![a_all]](#-) ![GHStars](https://img.shields.io/github/stars/GCuser99/SeleniumVBA?style&logo=github&label) [SeleniumVBA](https://github.com/GCuser99/SeleniumVBA) - 直接从 VBA 驱动 selenium webdriver。如果您没有安装驱动程序，库将尝试为您下载并运行它。然而 AV 可能会限制该进程的运行。
- [![p_win]](#-) [![p_nom]](#-) [![a_xl]](#-) ![GHStars](https://img.shields.io/github/stars/michaelneu/webxcel?style&logo=github&label) [webxcel](https://github.com/michaelneu/webxcel) - 运行 RESTful 后端的网络服务器。创建者还撰写了一篇[文章](https://dev.to/michaelneu/to-vba-and-beyond---building-a-restful-backend-using-plain-microsoft-excel-macros-76n)，介绍它在 dev.to 上的工作原理。
- 来自图书馆馆藏：
- [![p_win]](#-) [![p_nom]](#-) [![a_all]](#-) 在 `stdVBA` 中找到 `stdHTTP` - 连接并查询 Web 服务。


## 开发者工具

- [![p_win]](#-) [![p_nom]](#-) [![a_all]](#-) [![o_inst]](#-) [Rubberduck](https://rubberduckvba.com/) - 一个开源 COM 插件项目，与 Visual Basic 编辑器集成，向熟悉的 IDE 添加现代功能。适用于 VBA6、VBA7.x (x86/x64)，是的，也适用于 VB6！
- [![p_win]](#-) [![p_nom]](#-) [![a_xl]](#-) ![GHStars](https://img.shields.io/github/stars/spences10/VBA-IDE-Code-Export?style&logo=github&label) [VBA-IDE-Code-Export](https://github.com/spences10/VBA-IDE-Code-Export) - Addin 包含与 git （或任何 VCS）一起使用的代码导入器和导出器。
- [![p_win]](#-) [![p_nom]](#-) [![a_xl]](#-) [![a_wd]](#-) [![o_pass]](#-) - [RibbonX](https://www.andypope.info/vba/ribboneditor_2010.htm) - AndyPope 的可视化功能区编辑器。
- [![p_win]](#-) [![p_nom]](#-) [![a_xl]](#-) [自定义 UI XML 编辑器](https://yoursumbuddy.com/ribbon-customui-xml-editor/) - 用于直接添加、编辑和验证功能区 XML 的插件 (Excel 2010+)。
- [![p_win]](#-) [![p_nom]](#-) [![a_xl]](#-) [![a_ac]](#-) [![a_wd]](#-) [![a_pp]](#-) [![o_paid]](#-) [Ribbon Creator](https://ribboncreator2021.de/en/) - 一个优秀且直观的工具用于开发功能区的所见即所得界面。免费共享软件版本允许每个功能区导出最多两个选项卡。
- [![p_win]](#-) [![p_nom]](#-) [![a_all]](#-) [![o_paid]](#- '成本高达 $79') [MZ-Tools](https://www.mztools.com/) - 提供开发工具的 VBE 插件。
- [![p_win]](#-) [![p_nom]](#-) [![a_all]](#-) ![GHStars](https://img.shields.io/github/stars/wqweto/VbPeg?style&logo=github&label) [VbPeg](https://github.com/wqweto/VbPeg) - VBA 的解析器生成器。将像[this](https://github.com/wqweto/VbPeg/blob/master/test/Runner/peg/Kscope/grammar.peg)这样的PEG语法转换成[像这样的VBA代码](https://github.com/wqweto/VbPeg/blob/master/test/Runner/peg/Kscope/cKscope.cls)。如果您要在 VBA 中实现新的编程语言，这非常有用。
- [![p_win]](#-) [![p_nom]](#-) [![a_all]](#-) [VBA 资源文件编辑器](http://leandroascierto.com/blog/vba-resource-file-editor/) - 将其他文件存储在 excel/word/powerpoint 文件中，以便以后使用这个方便的工具使用。
- [![p_win]](#-) [![p_nom]](#-) [![a_all]](#-) [![o_32]](#-) [vbRichClient](https://vbrichclient.com/#/en/About/) - 充满有用库的外部客户端。
- [![p_win]](#-) [![p_nom]](#-) [![a_all]](#-) [![o_paid]](#- '£170-£205 许可证每个开发') [vbWatchDog](https://www.everythingaccess.com/vbwatchdog.asp) - `vbWatchdog` 破解 VBA 运行时以提供模块名称、过程名称和发生错误的行号发生。
- [![p_win]](#-) [![p_nom]](#-) [![a_all]](#-) [DLL 函数查看器](https://www.mrexcel.com/board/threads/dll-export-viewer-vba-based.1220909/) - 允许从 DLL 导出函数名称。
- [![p_win]](#-) [![p_nom]](#-) [![a_all]](#-) ![GHStars](https://img.shields.io/github/stars/sancarn/stdVBA-examples?style&logo=github&label) [辅助功能Inspector](https://github.com/sancarn/stdVBA-examples/tree/main/Examples/Inspector-Accessibility-v2) - 用于应用程序中可访问性的检查器/资源管理器。对于自动化很有用。
- [![p_win]](#-) [![p_nom]](#-) [![a_all]](#-) ![GHStars](https://img.shields.io/github/stars/sancarn/stdVBA-examples?style&logo=github&label) [运行对象表Inspector](https://github.com/sancarn/stdVBA-examples/tree/main/Examples/Inspector-RunningObjectTable) - 运行对象表 (ROT) 的检查器，可以获取全局运行 COM 对象的表。
- [![p_win]](#-) [![p_nom]](#-) [![a_all]](#-) ![GHStars](https://img.shields.io/github/stars/sancarn/stdVBA-examples?style&logo=github&label) [剪贴板Inspector](https://github.com/sancarn/stdVBA-examples/tree/main/Examples/Inspector-Clipboard) - 允许检查剪贴板中保存的数据。对于在其他应用程序中使用剪贴板进行逆向工程很有用。
- [![p_win]](#-) [![p_nom]](#-) [![a_all]](#-) ![GHStars](https://img.shields.io/github/stars/sancarn/stdVBA-examples?style&logo=github&label) [注册表Inspector](https://github.com/sancarn/stdVBA-examples/tree/main/Examples/Inspector-Registry) - 允许检查 win32 注册表。基本上相当于 regedit，但完全用 VBA 实现。
- [![p_win]](#-) [![p_nom]](#-) [![a_all]](#-) ![GHStars](https://img.shields.io/github/stars/sancarn/stdVBA-examples?style&logo=github&label) [JSON Inspector](https://github.com/sancarn/stdVBA-examples/tree/main/Examples/Inspector-JSON) - JSON 数据的检查器，也可以按需调用作为检查 API 响应的开发工具。
- [![p_win]](#-) [![p_nom]](#-) [![a_all]](#-) ![GHStars](https://img.shields.io/github/stars/KallunWillock/vbaXray?style&logo=github&label) [vbaXray](https://github.com/KallunWillock/vbaXray) - 一个纯 VBA 类，如下所示：直接从 Office 二进制文件检查并导出 VBA 源代码


## 示例

### 算法、代码优化和性能测试

- [VBSpeed](http://www.xbeat.net/vbspeed/) - Visual Basic 性能站点 - 专注于 VB6，但可转移到 VBA。

### 用户界面功能区

- [Access Ribbon](https://www.accessribbon.de/en/) - 有关开发自定义功能区 XML 的优秀信息资源。虽然主要针对 Access，但它同样适用于 Excel、Word 和 PowerPoint。
- [Ron de Bruin - Ribbons/QAT](https://jkp-ads.com/rdb/) - 有关开发自定义功能区和上下文菜单的信息/示例的领先资源。 （托管于 Jan Karel Pieterse 的网站）
- [Office MSO Icons](http://www.spreadsheet1.com/office-excel-ribbon-imagemso-icons-gallery-page-01.html) - 功能区图标通常可以使用 Office 应用程序中预先存在的 1500 个（本网站上的 3 页）MSO 图标之一。

### 用户界面用户表单

- [![p_win]](#-) [![p_nom]](#-) [![a_all]](#-) [拖放控件](https://www.vbforums.com/showthread.php?888843-Load-image-into-STATIC-control-Win32&p=5496575&viewfull=1#post5496575) - 拖放图像控件围绕用户表单。
- [![p_win]](#-) [![p_nom]](#-) [![a_all]](#-) ![GHStars](https://img.shields.io/github/stars/KallunWillock/EZPZMouseController?style&logo=github&label) [EZPZMouseController](https://github.com/KallunWillock/EZPZMouseController/) - 一个使用本机 Microsoft Ink Collector 检测鼠标滚轮和鼠标移动事件的示例。

### 低级示例

- [![p_win]](#-) [![p_nom]](#-) [![a_all]](#-) [迭代 ROT](https://www.mrexcel.com/board/threads/how-to-target-instances-of-excel.1118789/page-2#post-5395037) - 迭代运行对象表 (ROT) 以查找 Excel 工作簿的示例实例。
- [![p_win]](#-) [![p_nom]](#-) [![a_all]](#-) [通过 IAccessible 迭代 Excel 实例](https://www.mrexcel.com/board/threads/how-to-target-instances-of-excel.1118789/page-2#post-5395519) - 在某些情况下，Excel 实例未注册到 ROT。然而，Excel 应用程序实现了“IAccessible”，它不仅可以用于自动化 UI，还可以用于从 hwnd 获取 Excel 实例。
- [![p_win]](#-) [![p_nom]](#-) [![a_xl]](#-) [Excel 屏幕阅读器](https://www.mrexcel.com/board/threads/excel-screen-reader-upon-navigating-with-the-mouse-with-vba-alone.1162338/) - 不仅是 UI 自动化的示例，也是使用 SAPI 执行文本的示例到演讲。

<!-- ### VBE UI -->

### 插件

- [![p_win]](#-) [![p_nom]](#-) [![a_xl]](#-) [MenuRighter](https://yoursumbuddy.com/blog/menurighter/) - MenuRighter 是一个 Excel 插件，可让您修改右键菜单。您几乎可以添加其他右键菜单或 Excel 2003 的“经典”菜单中的任何控件。
- [![p_win]](#-) [![p_nom]](#-) [![a_xl]](#-) [Sam Rad 的 DatePicker](http://samradapps.com/datepicker/) - 用于 Excel 的视觉效果令人印象深刻且专业的 DatePicker 插件。仅工作表/不能与用户表单一起使用。
- [![p_win]](#-) [![p_mac]](#-) [![a_xl]](#-) [Excel 名称管理器](https://jkp-ads.com/excel-name-manager.asp) - 由 JKP、Charles Williams 和 Matthew Henson 替换的增强型名称管理器。入围 2025 年最佳 Microsoft Excel 插件类别决赛。
- [![p_win]](#-) [![p_mac]](#-) [![a_xl]](#-) [Excel Flex Find](https://jkp-ads.com/excel-flexfind.asp) - JKP 的增强型查找和替换替换，将搜索范围扩展到对象和 VBA 代码。
- [![p_win]](#-) [![p_mac]](#-) [![a_wd]](#-) ![GHStars](https://img.shields.io/github/stars/joey-melo/vba-syntax-higlight?style&logo=github&label) [Word VBA 语法荧光笔](https://github.com/joey-melo/vba-syntax-higlight/tree/main) - 用于 Word 文档的自定义语法突出显示工具。

### 游戏/有趣的项目

- [![p_win]](#-) [![p_nom]](#-) [![a_xl]](#-) ![GHStars](https://img.shields.io/github/stars/DylanTallchiefGit/xlStudio?style&logo=github&label) [xlStudio](https://github.com/DylanTallchiefGit/xlStudio) - Microsoft 的 DAW优秀。另请观看精彩的[视频](https://youtu.be/RFdCM2kHL64)。
- [![p_win]](#-) [![p_nom]](#-) [![a_xl]](#-) [Cellivization](https://s0lly.itch.io/cellivization) - 用 Excel 创建的一款很酷的类似 RTS 的游戏。另请观看精彩的[视频](https://www.youtube.com/watch?v=PzETBRcr_i8)。
- [![p_win]](#-) [![p_nom]](#-) [![a_xl]](#-) [Arkanoid](http://leandroascierto.com/blog/juego-arkanoid-en-excel/) - Arkanoid，一款复古街机游戏，用 Excel 构建。在某些机器上它比其他机器运行得更快。
- [![p_win]](#-) [![p_nom]](#-) [![a_xl]](#-) ![GHStars](https://img.shields.io/github/stars/rubberduck-vba/Battleship?style&logo=github&label) [战舰](https://github.com/rubberduck-vba/Battleship)
- [![p_win]](#-) [![p_nom]](#-) [![a_ac]](#-) [Pacman](https://arkham46.developpez.com/articles/office/clgdiplus/tuto/tutoclgdiplusgame3/?page=Page_11#LXXIV)
- [![p_win]](#-) [![p_nom]](#-) [![a_xl]](#-) ![GHStars](https://img.shields.io/github/stars/raspberrypioneer/ExcelCommodroid?style&logo=github&label) [ExcelCommodroid](https://github.com/raspberrypioneer/ExcelCommodroid/tree/main) - Commodore 计算机加载程序在 Windows 上使用 MS Excel。仅 VBA7。
- [![p_win]](#-) [![p_nom]](#-) [![a_all]](#-)[![o_32]](#-) ![GHStars](https://img.shields.io/github/stars/M2000Interpreter/Environment?style&logo=github&label) [M2000Interpreter](https://github.com/M2000Interpreter/Environment)

## 外部工具

- [![p_win]](#-) [![p_mac]](#-) ![GHStars](https://img.shields.io/github/stars/decalage2/oletools?style&logo=github&label) [![a_misc]](# "Python") [oletools](https://github.com/decalage2/oletools) - 可用于解码 VBA P 代码的 Python 工具（VBA 的中间语言）。
- [![p_win]](#-) [![p_mac]](#-) [![a_misc]](#- 'VBA 计划，但截至 2022 年 5 月 27 日只能编译为 exe') [twinBasic](https://twinbasic.com/) - VBA 兼容的解析器、评估器和编译器。
- [![p_win]](#-) [![p_mac]](#-) ![GHStars](https://img.shields.io/github/stars/serkonda7/vscode-vba?style&logo=github&label) [![a_misc]](# "VSCode") [vscode-vba](https://github.com/serkonda7/vscode-vba) - 添加的扩展VBA 编辑器支持 Visual Studio Code。
- [![p_win]](#-) [![p_mac]](#-) ![GHStars](https://img.shields.io/github/stars/SSlinky/VBA-LanguageServer?style&logo=github&label) [![a_misc]](# "VSCode") [VBA Pro](https://marketplace.visualstudio.com/items?itemName=NotisDataAnalytics.vba-lsp) - VSCode 扩展，添加基于语言服务协议的增强型 VBA 支持。源代码也在 [GitHub 上](https://github.com/SSlinky/VBA-LanguageServer)。
- [![p_win]](#-) [![p_mac]](#-) ![GHStars](https://img.shields.io/github/stars/DecimalTurn/VBA-Build?style&logo=github&label) [![a_misc]](# "Github") [VBA Build](https://github.com/DecimalTurn/VBA-Build) - 自动构建的 Github 操作提交时的 VBA 项目。
- [![p_win]](#-) [![p_mac]](#-) ![GHStars](https://img.shields.io/github/stars/Beakerboy/MS-OVBA?style&logo=github&label) [![a_misc]](# "Python") [VBA 项目编译器](https://github.com/Beakerboy/MS-OVBA) - 可用于编译 VBA 的 python 库项目。还有一个内置的[Excel插件生成器](https://github.com/Beakerboy/Excel-Addin-Generator)，由同一作者制作！您可以在[此处](https://github.com/sancarn/awesome-vba/issues/35)查看作者的相关项目列表。
- [![p_win]](#-) [![p_nom]](#-) [![o_paid]](#- '将获得许可') [![o_dll]](#- '使用外部 exe') [WinVBA](https://winvba.com/) - 用于 Visual Basic for Applications (VBA) 开发的现代 IDE。

## 风格指南

- [RubberDuck's style guide](https://rubberduckvba.wordpress.com/2021/05/29/rubberduck-style-guide/) - 有一些很棒的中级-高级指导。
- [VB6 编码约定](https://docs.microsoft.com/en-us/previous-versions/visualstudio/visual-basic-6/aa240822(v%3dvs.60)) - VBA 中使用的变量/类/模块命名约定。对 VBE 中的组织有很大帮助（除非你有橡皮鸭）。

## 信息

- [Thunder - The birth of Visual Basic](http://www.forestmoon.com/birthofvb/birthofvb.html) - 一篇关于 VB7/VBA 诞生的小文章。
- [My First Bill Gates Review](https://www.joelonsoftware.com/2006/06/16/my-first-billg-review/) - Excel 团队的项目经理 Joel Spolsky 讲述了他的第一次 Bill Gates 评论。乔尔添加了许多功能，例如“IDispatch”、“变体”、“对于每个”和“随着”。它还讨论了从 Lotus 123 移植到 Excel 的可怕的日期错误。
- [Ruby, EB and DLL composition](https://github.com/sancarn/stdVBA-Inspiration/blob/master/_OtherDocumentation/VBA%20and%20VB6%20History%20-%20Eb%20and%20Ruby/VBA%20History.md) - 由俄罗斯 VBer `Хакер` 创建的 [VBStreets 文章](http://bbs.vbstreets.ru/viewtopic.php?f=101&t=56551) 的翻译副本。详细介绍了该语言的历史中 VB6 和 VBA dll 的组成。
- [PCode Internals](https://www.vbforums.com/showthread.php?884919-pcode-internals) - VBA 被编译为 PCode。了解较低级别的 P 代码是人们非常感兴趣和研究的主题。
- [How many lines of code in EB](http://bbs.vbstreets.ru/viewtopic.php?f=101&t=56633) - 俄罗斯 VBer“Хакер”的未翻译文章估计了 VB6/VBA 中的代码行数。
- [SAFEARRAYS](https://www.vbforums.com/showthread.php?895566-RESOLVED-SAFEARRAY-Structure-for-an-Array) - 数组的内部结构。
- [Articles by Sancarn](https://sancarn.github.io/vba-articles) - Sancarn 撰写的有关 VBA 的各种文章，包括性能、VBA 的实际问题等。

## 资源

### Win32 API 资源

- [JKP API 声明](https://jkp-ads.com/Articles/apideclarations.asp)
- [Microsoft Office 代码兼容性检查器](https://docs.microsoft.com/en-us/previous-versions/office/office-2010/ee833946(v=office.14)) - Microsoft Office 代码兼容性检查器由 Microsoft 设计，用于解决将 Office 从 32 位升级到 64 位时与 VBA 代码的兼容性问题。微软尚未维护从其服务器下载该软件的链接，尽管该软件的版本显然可以在互联网上找到。

### VB6 / VBScript

- [Planet Source Code](https://github.com/Planet-Source-Code/PSCIndex) - 代码存储库 GitHub，保存了大量代码。该网站于 2023 年关闭，但幸运的是所有 VBA/VB6 示例今天都存档在 GitHub 上。可能不是之前在 PSC 网站上提供的项目/源代码的完整集合（？）。
- [vbAccelerator Archive](https://github.com/tannerhelland/vbAccelerator-Archive) - vbAccelerator 网站的存档副本（文章、源代码等）于 2015 年消失，于 2018 年重新出现，任何人都猜接下来会发生什么&hellip;主要是 VB6，但有用的 VBA 资源。

### 网站

- [Excel Development Platform Blog](https://exceldevelopmentplatform.blogspot.com/) - 处理高级主题/VBA 的博客。
- [MSDN VBA 文档](https://msdn.microsoft.com/en-us/vba/office-vba-reference)
- [MS-VBAL 语言规范](https://docs.microsoft.com/en-gb/openspecs/microsoft_general_purpose_programming_languages/ms-vbal/d5418146-0bd2-45eb-9c7a-fd9502722c74)
- [Ron de Bruin](https://web.archive.org/web/20230806005811/https://www.rondebruin.nl/index.htm) - 简单中级主题。注意：Ron 已存档所有这些站点，不会更新，并且某些信息已过时，但它仍然是 VBA 的令人难以置信的资源。
- [Bytecomb VBA Reference](https://bytecomb.com/vba-reference/) - 中级至高级主题。
- [Chip Pearson's website](http://www.cpearson.com/excel) - 对于初学者中级来说是很好的资源。
- [VBA for smarties](http://www.snb-vba.eu/inhoud_en.html) - 对大量数据结构和机制的重要参考。
- [Rubberduck Blog](https://rubberduckvba.wordpress.com/) - 中级至高级主题。
- [![a_ol]](#-) [Slipstick](https://www.slipstick.com/) - Diane Poremsky (MVP) 的网站，重点关注 Outlook 和 VBA。
- [![a_ol]](#-) [TechnicLee](https://techniclee.wordpress.com/) - Outlook 博客，许多示例，包括取决于用户请求的代码变化。
- [![a_pp]](#-) [PowerPoint VBA](https://pptvba.com/) - 一个致力于通过在 PowerPoint 中制作游戏来教授 VBA 的网站。
- [MS KB Archive](https://github.com/jeffpar/kbarchive/tree/master/id/vbwin) - 大量 vb6/vba 问题、解决方案和教程的存档。
- [Sancarn's vba-articles](https://sancarn.github.io/vba-articles/) - Sancarn 关于与 VBA 相关的各种主题的文章。
- [![a_ac]](#-) [不再设置](https://nolongerset.com) - 访问 Microsoft MVP Mike Wolfe 的 + VBA 站点。每周提供有关 TwinBasic 开发的最新信息。
- [![a_ac]](#-) [Isladogs on Access](https://isladogs.co.uk/) - Microsoft MVP Colin Riddington 的 Access + VBA 网站。 Access VBA 中的 VBA 项目的优秀资源。
- [![a_ac]](#-) [DevHut](https://www.devhut.net/) - 访问 Daniel Pineault 的 + VBA 站点。发表一系列深入探讨 VBA 各种用途的文章。 YouTube 帐户的配套网站。
- [![o_paid]](#- '通过网站提供的各种付费内容') [AnalystCave](https://analystcave.com/) - 专门用于 VBA 分析的网站。

### 书籍

- [Hard Core Visual Basic](https://classicvb.net/hardweb/mckinney.htm) - 新的 Visual Basic 5.0 版本的高级程序员指南。包括一组核心实用程序、快捷方式和问题解决方案，以实现各种功能程序。还有一本硬书。另请查看[评论和更正](https://jeffpar.github.io/kbarchive/kb/173/Q173840/)。
- [The VBA Developer's Handbook](https://www.academia.edu/29801473/VBA_Developers_Handbook_Second_Edition) - 为任何情况编写防弹 VBA 代码。对于使用 300 多种采用“Visual Basic for Applications”编程语言的产品的开发人员来说，本书是必不可少的资源。精装本在其他地方也有售。
- [Advanced Visual Basic 6](https://pdfcoffee.com/advanced-visual-basic-6-power-techniques-for-everyday-programs978020170712024922-pdf-free.html) - 日常计划的强力技巧 马修·科兰 (Matthew Curland)。精装本在其他地方也有售。
- [Professional Excel Development](https://oiipdf.com/download/professional-excel-development-the-definitive-guide-to-developing-applications-using-microsoft-excel-vba-and-net) - 在本书中，四位世界级的 Microsoft® Excel 开发人员提供了使用 Excel 构建功能强大、健壮且安全的应用程序的从头到尾的指导。还提供精装本。
- [![o_paid]](#- '~$6') [Excel VBA 傻瓜编程](https://www.google.com/search?q=Excel+VBA+Programming+For+Dummies+book) - 是时候进入下一个级别了 - 使用 Visual Basic for Applications (VBA) 创建您自己的自定义 Excel 2010 解决方案。这本实用的书使用分步说明和易于理解、友好的傻瓜风格，展示了您将了解如何使用 VBA、编写宏、自定义 Excel 应用程序以按照您想要的方式外观和工作、避免错误等等。
- [![o_paid]](#- '~$30') [使用 VBA 进行 Power 编程](https://www.wiley.com/en-us/Excel+2019+Power+Programming+with+VBA-p-9781119514916) - Excel 2019 使用 VBA 进行 Power 编程全面更新，涵盖了 Excel 2019 的所有最新工具和技巧。这本内容全面的书全面介绍了 Visual Basic for Applications (VBA)，介绍了开发大型和小型 Excel 应用程序所需的所有技术。
- [（电子书）VBA初学者](https://goalkicker.com/VBABook/)
- [（电子书）Excel VBA 初学者](https://goalkicker.com/ExcelVBABook/)

### YouTube

- [Excel Macro Mastery](https://www.youtube.com/c/Excelmacromastery) - 保罗·凯利 (MVP) - excelmacromastery.com。
- [Sigma Coding](https://www.youtube.com/c/SigmaCoding) - 大量教程 - 初学者到高级。深入研究其他内容创建者未探索过的 VBA 有趣领域。
- [WiseOwl's VBA tutorials](https://www.youtube.com/playlist?list=PLNIs-AWhQzckr8Dgmgb3akx_gFMnpxTN5) - VBA 的全面资源。适合初学者的完美入门。深入了解 VBA 的各个方面。庞大的播放列表涵盖了大多数类型的 VBA。
- [![o_paid]](#- '一些使用的库是非自由和开源软件并由 VBA A2Z 创建') [VBA A2Z](https://www.youtube.com/c/VBAA2Z) - 许多教程，一些付费内容。一系列有趣且不同的主题 - VBA 不同部分的深入教程，以及一些 .NET/VSTO 视频。重点关注 UI 开发。
- [Excel VBA 很有趣](https://www.youtube.com/c/ExcelVbaIsFun)
- [Excel for Freelancers](https://www.youtube.com/c/ExcelForFreelancers) - 从头到尾开发特定应用程序的实践教程。所有级别。
- [Leila Gharani](https://www.youtube.com/c/LeilaGharani) - 办公室范围的焦点 - 对初学者有用。
- [![o_paid]](#- '该视频来自一位顾问。他的许多视频都是付费的。') [了解 VBA](https://youtu.be/MFR_XARJjoY) - 使用 VBA 呈现和创建的一些出色的应用程序。
- [![a_ac]](#-) [D Pineault - 技术、编程等](https://www.youtube.com/channel/UC9lSC6AT4d0qour-aIbMjFQ) - Daniel Pineault 的 Youtube 频道。 DevHut 网站的配套频道。

### 论坛

- [Reddit](http://reddit.co.uk/r/vba) - 每日 VBA 问答。偶尔进行专业提示分享和展示与讲述图书馆出版。
- [Stack Overflow](https://stackoverflow.com/questions/tagged/vba) - 提问的好地方。重复的问题将被标记为重复，并将作者发送到正确的位置。
- [Chandoo](https://chandoo.org/wp/) - Chandoo 论坛 - Purna Duggirala (MVP) 的博客。非常活跃。
- [Visual Basic Discord](https://discord.gg/gpcSue9f) - VB.NET/VBA/VB6 狂热者的聊天室。
- [Excel Discord](https://discord.gg/PU2vVDeb) - Discord 服务器由 Tim Heng（Excel MVP）主持，专注于帮助 Excel 用户。
- [MrExcel](https://www.mrexcel.com/board/) - 主要是 Excel 通用内容，但也可以在这里找到很多 VBA 内容。
- [Excel论坛](https://www.excelforum.com/)
- [![a_ol]](#-) [Slipstick](https://www.forums.slipstick.com) - Diane Poremsky (MVP) 的 Slipstick 网站 (Outlook VBA) 的优秀论坛。黛安回复很快，她的回答非常有帮助。
- [VBForums - Office Development](https://www.vbforums.com/forumdisplay.php?37-Office-Development) - 论坛重点关注 VB6/.NET 和 VBA 部分。
- [![a_ac]](#-) [Access World](https://www.access-programmers.co.uk/forums/forums/modules-vba.12/) - 重点关注 Access 和 Access VBA 的论坛。

## 脚注

### 符号学

由于 VBA 的性质，许多库并不适用于所有操作系统、所有 Office 应用程序或所有体系结构 (x64/x86)。某些库可能还需要外部资源（DLL、插件等），由于 VBA 缺少包管理器，这些资源可能很难使用。为了帮助您找到适合您需求的项目，这个很棒的列表使用以下符号系统。符号系统还具有可以提供更多信息的工具提示。

#### 平台兼容性

[p_all]: ./resources/Crown.svg '在所有平台上兼容'
[p_mac]: ./resources/AppleLogo.svg 'macOS'
[p_win]: ./resources/WindowsLogo.svg 'Windows 操作系统'
[p_now]: ./resources/NotApplicable.svg '不是 Windows 操作系统'
[p_nom]: ./resources/NotApplicable.svg '不是 macOS'

- [![p_win]](#-) [![p_mac]](#-) - 适用于所有平台
- [![p_win]](#-) [![p_nom]](#-) - 仅适用于 Windows 操作系统
- [![p_now]](#-) [![p_mac]](#-) - 仅适用于 Mac OS

#### 应用兼容性

[a_all]: ./resources/OfficeLogoPlus.svg '所有应用程序'
[a_wd]: ./resources/WordLogo.svg 'Word'
[a_xl]: ./resources/ExcelLogo.svg 'Excel'
[a_ac]: ./resources/AccessLogo.svg '访问'
[a_ol]: ./resources/OutlookLogo.svg 'Outlook'
[a_pp]: ./resources/PowerPointLogo.svg 'PowerPoint'
[a_misc]：./resources/Duck.svg

- [![a_all]](#-) - 所有应用程序
- [![a_wd]](#-) - 字
- [![a_xl]](#-) - Excel
- [![a_ac]](#-) - 访问
- [![a_ol]](#-) - 展望
- [![a_pp]](#-) - PowerPoint
- [![a_misc]](#- 'Misc') - 其他应用程序（MS Project、AutoCAD 等） - 在简短说明中指定

#### 其他重要信息

[o_32]: ./resources/32-Bit.svg '仅限 32 位'
[o_pass]: ./resources/Padlock.svg 'VBA 受密码保护'
[o_dll]：./resources/Dependency.svg
[o_inst]: ./resources/Installation.svg '需要安装'
[o_paid]：./resources/Money.svg

- [![o_32]](#-) - 仅 32 位
- [![o_pass]](#-) - 用 VBA 编写，但代码受密码保护
- [![o_dll]](#- '需要外部依赖项') - 需要外部依赖项，例如`.dll`、`.ocx`、`.o` 等
- [![o_inst]](#-) - 需要安装
- [![o_paid]](#- '链接包含/通向付费内容') - 链接包含/通向付费内容

## 贡献

随时欢迎您的贡献！请先查看[贡献指南](./Contributing.md)。
