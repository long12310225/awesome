# 很棒的安卓系统
[<img src="https://raw.githubusercontent.com/jstumpp/awesome-android/master/awesome-android.png">](https://github.com/jstumpp/awesome-android)

<p align="center">
  <a href="https://github.com/sindresorhus/awesome"><img alt="awesome" src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg" /></a>
  <a href="https://travis-ci.org/JStumpp/awesome-android"><img alt="Build Status" src="https://api.travis-ci.org/JStumpp/awesome-android.svg?branch=master" /></a>
  <img alt="PRs Welcome" src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg" />
</p>

# 关于
很棒的 Android [库](#libraries) 和 [资源](#resources) 的精选列表。对于一般的 Java 库，请查看 [awesome-java](https://github.com/akullpp/awesome-java)。

## 由 Instabug ❤️ 支持
### 通过用户的实时上下文洞察了解您的 Android 应用程序的运行情况
[![instabug-github](https://user-images.githubusercontent.com/10850625/65512691-fd45f280-ded9-11e9-8921-3528b98c30a7.png)](https://instabug.com/android/sdk?utm_source=awesomeandroid&utm_medium=spon&utm_content=banner)
>Instabug 帮助 Android 开发人员和产品团队轻松收集 bug 以及 Beta 测试人员和用户的反馈，以更快地迭代并交付高质量的应用程序。 Instabug 会自动附加屏幕截图、设备详细信息、网络日志、重现步骤以及解决问题和确定产品积压优先级所需的大量其他关键见解。
> 移动团队通过与 Github、Jira、Slack、Zendesk 等第三方工具无缝集成来加速工作流程。 [Instabug 为 Awesome Android 社​​区提供所有付费套餐 15% 的独家折扣。开始吧！](https://instabug.com/android/sdk/?utm_source=awesomeandroid&utm_medium=spon&utm_content=get-started)
[![](https://instabug-ga.appspot.com/UA-41982088-6/github/awesomeandroid?pixel)](https://instabug.com)


# 如何使用
Awesome-Android 对于那些需要在其应用程序上使用特定功能的人来说是一个令人惊叹的列表，因此最好的使用方法是：
- 只需按 command + F 即可搜索关键字
- 浏览我们的内容菜单

# 内容
- [Emulators](#emulators)
- [Libraries](#libraries)
    - [Charts](#charts)
    - [云服务](#cloud-services)
    - [依赖注入](#dependency-injection)
    - [安卓服务](#android-services)
    - [游戏开发](#game-development)
	- [Security](#security)
    - [GUI](#gui)
        - [ActionBar](#actionbar)
        - [Navigation](#navigation)
        - [Animations](#animations)
        - [Images](#images)
        - [Inputs](#inputs)
        - [加载图像](#loading-images)
        - [媒体选择器](#media-picker)
        - [Video](#video)
        - [Camera](#camera)
        - [现场验证](#field-validation)
    - [JSON](#json)
    - [碰撞监控](#crash-monitoring)
    - [Networking](#networking)
    - [Logger](#logger)
    - [Notifications](#notifications)
    - [Database](#database)
        - [ORM](#orm)
    - [REST](#rest)
    - [Testing](#testing)
    - [Tracking](#tracking)
    - [Maps](#maps)
    - [Utility](#utility)
    - [调试工具](#debugging-tools)
    - [Wireless](#wireless)
    - [聊天和消息传递](#chat--messaging)
    - [自定义对话框](#custom-dialog)
    - [版本检查](#version-checking)
    - [日期和时间](#date--time)
    - [运行时权限](#runtime-permissions)
    - [Other](#other)
- [Resources](#resources)
    - [代码示例](#code-examples)
    - [Podcasts](#podcasts)
    - [更多库列表](#more-lists-of-libraries)
- [发展替代方案](#development-alternatives)
    - [C#](#c)
    - [HTML、CSS 和 JavaScript](#html-css-and-javascript)
    - [Lua](#lua)
    - [Scala](#scala)
    - [Groovy](#groovy)
    - [Kotlin](#kotlin)
    - [Flutter](#flutter)
- [Performance](#performance)
- [其他很棒的清单](#other-awesome-lists)
- [Contributing](#contributing)

## 模拟器
- [AndY](https://andyroid.net)
- [ARChon](https://archon-runtime.github.io)
- [BlueStacks](https://www.bluestacks.com)
- [Genymotion](https://www.genymotion.com)
- [nox](https://www.bignox.com)

## 图书馆

### 图表

- [AChartEngine](https://github.com/ddanny/achartengine) - 图表引擎。
- [EazeGraph](https://github.com/blackfizz/EazeGraph) - 图表和图形库。
- [WilliamChart](https://github.com/diogobernardino/WilliamChart) - 具有良好运动功能的图表库。
- [HelloCharts](https://github.com/lecho/hellocharts-android) - 支持缩放、滚动和动画的图表和图形库。
- [MPAndroidChart](https://github.com/PhilJay/MPAndroidChart) - 一个支持手势缩放和拖动的Android图表和图形库。
- [ArcChartView](https://github.com/imaNNeoFighT/ArcChartView) - 绘制创意统计弧形图。
- [AnyChart](https://github.com/AnyChart/AnyChart-Android) - 数据可视化库，交互式图表。

### 云服务

- [CloudRail](https://cloudrail.com) - 统一 API 库：云存储、社交资料、支付、电子邮件、短信和 POI。

### 数据绑定

- [Anvil](https://github.com/anvil-ui/anvil) - 受 React 启发，用于创建反应式 UI 组件的小型库。提供数据绑定和事件监听器绑定，非常适合MVVM。
- [Data Binding Library](https://developer.android.com/topic/libraries/data-binding/) - 官方 Android 数据绑定库，用于编写声明性布局并最大限度地减少绑定应用程序逻辑和布局所需的粘合代码。

### 依赖注入

- [Dagger 2](https://github.com/google/dagger) - 适用于 Android 和 Java 的快速依赖注入器。
- [Butter Knife](http://jakewharton.github.io/butterknife/) - 查看 Android 的“注入”库。
- [ActivityStarter](https://github.com/MarcinMoskala/ActivityStarter) - Android 库提供了使用多个参数启动 Activity 的更简单方法。
- [AndroidAnnotations](https://github.com/androidannotations/androidannotations) - Java 注释在编译时进行依赖注入。
- [Toothpick](https://github.com/stephanenicolas/toothpick) - 用于 Java 的基于作用域树的依赖注入 (DI) 库。

### 安卓服务
- [Remoter](https://github.com/josesamuel/remoter) - 使用普通 java 接口的 Android Remote IPC 服务的 Android AIDL 的替代方案。
- [Service Connector](https://github.com/josesamuel/serviceconnector) - 将 Android 服务和回调绑定到字段和方法。

### 游戏开发

- [Libgdx](https://libgdx.badlogicgames.com/) - 跨平台游戏引擎和SDK。 [开源](https://github.com/libGDX/libGDX)
- [Vuforia](https://www.vuforia.com/) - 增强现实图书馆。
- [Unity](https://unity3d.com/unity/features/multiplatform) - 跨平台游戏创作系统。
- [Rajawali](https://github.com/Rajawali/Rajawali) - Android OpenGL ES 2.0/3.0 引擎
- [Cocos2d-x](https://cocos2d-x.org/) - 跨平台2D游戏框架。
- [JustWeEngine](https://github.com/lfkdsk/JustWeEngine) - 一个简单的开源 Android 原生游戏框架。

### 安全性

- [libsignal-protocol-java](https://github.com/signalapp/libsignal-protocol-java) - 一种适用于同步和异步消息传递环境的棘轮前向保密协议。
- [Themis](https://github.com/cossacklabs/themis) - 多语言框架，使典型的加密方案易于使用：静态数据、经过身份验证的数据交换、传输保护、身份验证等。

### 图形用户界面

- [Pull to refresh](https://developer.android.com/reference/android/support/v4/widget/SwipeRefreshLayout) - v4 支持库中提供了滑动刷新布局。
- [Cardslib](https://github.com/gabrielemariotti/cardslib) - 用于构建 UI 卡的 Android 库。
- [AndroidStaggeredGrid](https://github.com/etsy/AndroidStaggeredGrid) - 网格视图支持多列和不同大小的行。
- [Flow](https://github.com/square/flow) - 有助于将应用程序描述为适度独立屏幕集合的库。
- [SortableTableView](https://github.com/ISchwarz23/SortableTableView) - 一个 Android 库，包含一个简单的 TableView 和一个高级的 SortableTableView，提供大量自定义可能性来满足所有需求。
- [MaterialProgressBar](https://github.com/zhanghai/MaterialProgressBar) - Material Design ProgressBar 具有一致的外观。
- [AndroidFillableLoaders](https://github.com/JorgeCastilloPrz/AndroidFillableLoaders) - 使用 SVG 路径的可填充进度视图。创建有趣的应用程序徽标也是不错的选择。
- [NexusDialog](https://github.com/dkharrat/NexusDialog) - 让您只需很少的代码即可轻松快速地在 Android 中创建表单。
- [Snap RecyclerView Utils](https://github.com/prashantsolanki3/Snap-RecyclerView-Utils) - 填充单个或多个布局 RecyclerView 而不创建适配器。
- [MultiSnapRecyclerView](https://github.com/TakuSemba/MultiSnapRecyclerView) - 用于 RecyclerView 多次捕捉的 Android 库
- [SwipeableCard](https://github.com/michelelacorte/SwipeableCard) - 像街景一样实现刷卡！！
- [ElasticProgressBar](https://github.com/michelelacorte/ElasticProgressBar) - 漂亮的加载栏。
- [EntryScreenManager](https://github.com/kunall17/EntryScreenManager) - 简介/入门/演练/启动屏幕。
- [EasyIntro](https://github.com/meNESS/EasyIntro) - 适用于您的 Android 项目的灵活、易于使用、全合一的应用程序介绍库。
- [Material-Calendar-View](https://github.com/BlackBoxVision/material-calendar-view) - Material Design 日历兼容 API 8+
- [CrunchyCalendar](https://github.com/CleverPumpkin/CrunchyCalendar) - 具有无限滚动、日期范围选择和颜色自定义功能的材料日历小部件。
- [SmoothOverscrollableScrollView](https://github.com/vovaksenov99/OverscrollableScrollView) - 带有平滑滚动的小型自定义视图。您可以添加带有比例背景的标题
- [SectionedRecyclerViewAdapter](https://github.com/luizgrp/SectionedRecyclerViewAdapter) - 一个适配器，允许将 RecyclerView 拆分为带有页眉和/或页脚的部分。
- [DragListView](https://github.com/woxblom/DragListView) - 拖放以对列表、网格或板中的项目重新排序。
- [Animated Expanding ListView](https://github.com/LeonardoCardoso/Animated-Expanding-ListView) - 动画扩展 ListView 提供了有关展开或折叠列表视图项内容的精美动画。
- [TastyToast](https://github.com/yadav-rahul/TastyToast) - 带有图标和颜色的吐司。
- [DotLoader](https://github.com/bhargavms/DotLoader) - 带点的可定制加载动画。
- [PodSlider](https://github.com/bhargavms/PodSLider) - 符合材料设计规范的可定制滑块小部件。
- [TapTargetView](https://github.com/KeepSafe/TapTargetView) - 功能发现的材料设计指南中的点击目标的实现。
- [ShowCaseView](https://github.com/mreram/ShowCaseView) - ShowcaseView 库旨在通过有吸引力的平面叠加层向用户突出显示和展示应用程序的特定部分。
- [MaterialIntroScreen](https://github.com/TangoAgency/material-intro-screen) - 使用易于扩展的 API 实现材质介绍屏幕。
- [FloatingView](https://github.com/UFreedom/FloatingView) - FloatingView 可以通过炫酷的动画使目标视图漂浮在锚视图之上。
- [Timecon](https://github.com/alxrm/animated-clock-icon) - 易于使用的动画时钟图标
- [Audiogram](https://github.com/alxrm/audiowave-progressbar) - 轻量级音频进度条
- [Bubbles for Android](https://github.com/txusballesteros/bubbles-for-android) - Facebook 之类的聊天气泡库
- [Litho (By Facebook)](https://github.com/facebook/litho) - 用于在 Android 上构建高效 UI 的声明式框架。
- [MultiViewAdapter](https://github.com/DevAhamed/MultiViewAdapter) - Recyclerview 适配器库用于创建可组合视图持有者。
- [LGSnackbar](https://github.com/loregr/LGSnackbar) - 一个易于使用且可定制的原生 Android Snackbar 包装器，在多个活动中保持可见。
- [ShimmerLayout](https://github.com/team-supercharge/ShimmerLayout) - Android 应用程序的内存高效闪烁效果。
- [CircleProgressBar](https://github.com/emre1512/CircleProgressBar) - 一个简单的库，用于为 Android 创建圆形进度条。
- [Easy-Signature-Android](https://github.com/smalam119/Easy-Signature-Android) - 一个简单的 ui 库，提供可插入的签名视图。
- [Flashbar](https://github.com/aritraroy/Flashbar) - 一个高度可定制、功能强大且易于使用的 Android 警报库。
- [YuanaItemSettingView](https://github.com/andhikayuana/YuanaItemSettingView) - 适用于 Android 的可自定义项目设置视图。
- [Gradients](https://github.com/bakhtiyork/gradients) - 精美渐变的精选集合。
- [OneAdapter](https://github.com/ironSource/OneAdapter) - RecyclerView Adapter 具有多个模块和挂钩，可简化和增强使用，同时防止常见错误。

#### 分页
- [NoPaginate](https://github.com/NoNews/NoPaginate) - 简单的Android分页库

#### 操作栏
- [ActionBarSherlock](http://actionbarsherlock.com) - 适用于较旧 Android 版本的 ActionBar。
- [FadingActionBar](https://github.com/ManuelPeinado/FadingActionBar) - 可以在新的 Play 音乐应用中看到淡入淡出的操作栏效果。

#### 导航
- [SlidingMenu](https://github.com/jfeinstein10/SlidingMenu) - 用于创建带有滑入式菜单的应用程序的库。
- [SlidingTutorial](https://github.com/Cleveroad/slidingtutorial-android) - 简单的库，有助于创建很棒的滑动 Android 应用程序教程。
- [PagerSlidingTabStrip](https://github.com/astuetz/PagerSlidingTabStrip) - 用于在 ViewPager 的不同页面之间导航的交互式指示器。
- [Page View indicator](https://github.com/JakeWharton/ViewPagerIndicator) - 支持水平滚动 ViewPager。
- [RecyclerTabLayout](https://github.com/nshmura/RecyclerTabLayout) - 使用 RecyclerView 实现的高效 TabLayout 库。
- [MaterialDrawer](https://github.com/mikepenz/MaterialDrawer) - 简单的材质设计导航抽屉。
- [Debug-Artist](https://github.com/BaristaVentures/android-debug-artist) - 调试菜单可轻松启用泄漏金丝雀、手术刀等。
- [Floating-Navigation-View](https://github.com/andremion/Floating-Navigation-View) - 一个简单的浮动操作按钮，显示锚定的导航视图。

#### 动画
- [SmoothMotion](https://github.com/abdullahalhakimi/SmoothMotion) - 用于简化 Jetpack Compose 中的动画和过渡的 Kotlin 库。
- [Rebound](https://github.com/facebook/rebound) - Rebound 是一个模拟弹簧动力学的 Java 库。
- [Android View Animations](https://github.com/daimajia/AndroidViewAnimations) - 可爱的视图动画集合。
- [Android-Transition](https://github.com/kaichunlin/android-transition) - 允许轻松创建对用户输入做出反应的视图转换。
- [Android-View-Actions](https://github.com/dtx12/AndroidAnimationsActions) - 使创建复杂的视图动画变得容易。
- [Swipper](https://github.com/mdg-iitr/Swipper) - Android 库，用于通过滑动手势来控制音量、亮度和搜索。
- [Spotlight](https://github.com/TakuSemba/Spotlight) - Android 库，为教程或演练等点亮项目...

#### 图片

- [Crescento](https://github.com/developer-shivam/crescento) - 通过在图像视图下方添加曲线来探索材料设计的新风格。
- [android-crop](https://github.com/jdamcd/android-crop) - 用于裁剪图像的库项目。
- [CircularImageView](https://github.com/Pkmmte/CircularImageView) - 圆形图像的自定义视图，同时保持最佳的绘制性能。
- [Android-Image-Filter](https://github.com/ragnraok/android-image-filter) - 用于轻松应用图像滤镜的库项目。
- [Compressor](https://github.com/zetbaitsu/Compressor) - Compressor 是一个轻量级且功能强大的 Android 图像压缩库。
- [ShapeImageView](https://github.com/siyamed/android-shape-imageview) - 以不同形状显示图像的库。

#### 输入

- [FloatingLabel](https://github.com/hardik-trivedi/FloatingLabel) - FloatingLabel 允许您创建一个打击类型的EditText。 *没有 Gradle 或 Maven 支持。*
- [MaterialEditText](https://github.com/rengwuxian/MaterialEditText) - 支持浮动标签、单行省略号、最大/最小字符、帮助文本和具有自定义颜色的错误文本。
- [EmojiCompat](https://github.com/googlearchive/android-EmojiCompat) - 向您的应用添加表情符号
- [MaterialSearchBar](https://github.com/mancj/MaterialSearchBar) - Android 的材质设计搜索栏
- [InputMask](https://github.com/RedMadRobot/input-mask-android) - 基于模式的用户输入格式化器、解析器和验证器。
- [SweetPassword](https://github.com/jesusmartinoza/Sweet-Password) - 允许自定义切换按钮的密码 EditText
- [VoiceOverlay](https://github.com/algolia/voice-overlay-android) - 一个覆盖层，可获取用户的语音许可并在可自定义 UI 中以文本形式输入。

#### 查看寻呼机
- [Material Dots Indicators](https://github.com/tommybuonomo/dotsindicator) - 用于查看寻呼机的三种材质点指示器样式。

#### 加载图像

- [Picasso](https://github.com/square/picasso) - 一个强大的 Android 图像下载和缓存库。
- [Universal Image Loader](https://github.com/nostra13/Android-Universal-Image-Loader) - 异步、开箱即用的图像加载和缓存。
- [Glide](https://github.com/bumptech/glide) - 适用于 Android 的图像加载和缓存库，专注于平滑滚动，由 Google 推荐。
- [Fresco](https://github.com/facebook/fresco) - 用于管理图像及其使用的内存的 Android 库。
- [Glide Bitmap Pool](https://github.com/amitshekhariitbhu/GlideBitmapPool) - Glide Bitmap Pool 是一个用于重用位图内存的内存管理库。
- [Coil](https://github.com/coil-kt/coil) - 由 Kotlin 协程支持的 Android 图像加载。

#### 媒体选择器

- [MediaPicker](https://github.com/alhazmy13/MediaPicker) - Android 库，可让您为 Android 选择多个图像、视频或语音
- [Android Image Picker](https://github.com/esafirm/android-image-picker) - 一个可以轻松从图库中选择图像和视频的库。它还支持 GIF 和简单的相机动作

#### 视频

- [ijkplayer](https://github.com/Bilibili/ijkplayer) - 基于 FFmpeg n3.2 的 Android/iOS 视频播放器，支持 MediaCodec、VideoToolbox。
- [Exoplayer](https://github.com/google/ExoPlayer) - ExoPlayer 是 Android 的应用程序级媒体播放器，允许在本地和通过互联网播放音频和视频。
支持 HTTP 动态自适应流式传输 (DASH)、SmoothStreaming 和通用加密等功能
- [VideoPlayView](https://github.com/MarcinMoskala/VideoPlayView) - 自定义 Android 视图，包含视频播放器、播放/停止、加载程序和占位符图像。

#### 相机

- [MagicalCamera](https://github.com/fabian7593/MagicalCamera) - 拍摄或选择图库照片的简单方法，以及管理图片的其他功能。
- [Camera](https://github.com/duanhong169/Camera) - 使用Android相机拍摄照片和视频，基于camera2 api。

#### 现场验证
- [Convalida](https://github.com/WellingtonCosta/convalida) - 一种简单且基于注释的方法来验证您的输入字段。

### JSON

- [Gson](https://github.com/google/gson) - Gson 是一个 Java 库，用于将 Java 对象序列化和反序列化为 JSON。
- [Jackson JSON Processor](https://github.com/FasterXML/jackson) - 高性能 JSON 处理器。
- [Moshi](https://github.com/square/moshi) - 适用于 Android 和 Java 的现代 JSON 库。
### 碰撞监控

- [Fabric Crashlytics](https://get.fabric.io/) - 简单的崩溃报告解决方案。
- [HockeyApp](https://www.hockeyapp.net/) - 分发、崩溃报告、反馈和分析
- [Splunk MINT](https://mint.splunk.com/) - 监控、崩溃报告、实时数据、统计。
- [Bugsnag](https://www.bugsnag.com/) - 跨平台错误监控。免费等级。支持 SDK 和 NDK。错误报告包括有关设备、版本、用户的数据，并允许任意数据。
- [Catcho](https://github.com/alhazmy13/Catcho) - 不再强制关闭。
- [Apteligent](https://www.apteligent.com/) - 跨平台崩溃报告/分析解决方案。支持NDK日志。
- [Instabug](https://instabug.com/) - 错误报告、崩溃报告、应用内反馈。

### 网络

- [Ion](https://github.com/koush/ion) - 很好的 Android 网络库。
- [OkHttp](https://github.com/square/okhttp) - 适用于 Android 和 Java 应用程序的 HTTP+SPDY 客户端。
- [RoboSpice](https://github.com/stephanenicolas/robospice) - 使编写异步网络请求变得容易的库。
- [IceNet](https://github.com/anton46/IceNet) - 适用于 Android 的快速、简单且轻松的网络
- [Android Volley](https://developer.android.com/training/volley/) - 官方 Android HTTP 库，使联网变得更容易、更快。
- [IceSoap](https://github.com/AlexGilleran/IceSoap) - 适用于 Android 的简单、异步、基于注释的 SOAP。
- [node-android](https://github.com/InstantWebP2P/node-android) - 在 Android 上运行 Node.js。
- [HappyDns](https://github.com/qiniu/happy-dns-android) - 一个 Dns 库，用户可以使用自定义 dns 服务器，dnspod httpdns。仅支持A记录。
- [RESTMock](https://github.com/andrzejchm/RESTMock) - 用于在 Android Instrumentation 测试中模拟 API 响应的 HTTP Web 服务器。
- [Fast-Android-Networking](https://github.com/amitshekhariitbhu/Fast-Android-Networking) - 完整的快速 Android 网络库，还支持 HTTP/2。

### 记录器
- [logger](https://github.com/orhanobut/logger) - 简单、漂亮且功能强大的 Android 记录器
- [timber](https://github.com/JakeWharton/timber) - 具有小型可扩展 API 的记录器，它在 Android 的普通 Log 类之上提供实用程序。
- [LoggingInterceptor](https://github.com/ihsanbal/LoggingInterceptor) - 一个 OkHttp 拦截器，可以很好地记录请求和响应数据。
- [Bugfender](https://github.com/bugfender/BugfenderSDK-android-sample) - 上传日志并在线查看，专为移动设备打造
- [EzyLogger](https://github.com/afiqiqmal/EzyLogger) - 简单的轻量级记录器
- [Logback Android](https://github.com/tony19/logback-android) - Logback 移植到 Android，为 Android 应用程序提供高度可配置的日志框架。
- [LogDog](https://log.dog) - LogDog 是一个带有 Web UI 的远程调试/日志记录 sdk（iOS 和 Android）。实时捕获所有日志和请求并允许拦截它们。

### 通知
- [android-remote-notifications](https://github.com/kaiwinter/android-remote-notifications) - 从远程 JSON 文件中提取通知并将其显示在您的应用程序中。
- [Android HeartBeat Fixer](https://github.com/joaopedronardari/AndroidHeartBeatFixer) - 设置心跳间隔和用户从 GCM 接收推送通知的方式。

### 数据库
- [Cupboard](https://bitbucket.org/littlerobots/cupboard) - 通过直接数据库访问或通过 ContentProvider 框架轻松访问 sqlite。
- [DbInspector](https://github.com/infinum/android_dbinspector) - 提供一种简单的方法来查看应用内数据库的内容以进行调试。
- [SQLite Asset Helper](https://github.com/jgilfelt/android-sqlite-asset-helper) - 使用应用程序的原始资产文件管理数据库创建和版本管理。
- [Realm](https://github.com/realm/realm-java) - SQLite 和 ORM 的替代方案：简单、现代且快速！面向对象的API和多平台支持。
- [Realm Asset Helper](https://github.com/eggheadgames/android-realm-asset-helper) - 从 apk 资产文件夹复制领域数据库。有效处理只读领域数据库的版本控制。
- [RestorableSQLiteDatabase](https://github.com/yaa110/RestorableSQLiteDatabase) - 一个包装器，用于复制具有恢复功能的 android 的 SQLiteDatabase。
- [Nitrite Database](https://github.com/dizitart/nitrite-database) - 适用于 Android 的 NoSQL 嵌入式文档存储，具有 MongoDb 之类的 API。

#### ORM

- [requery](https://github.com/requery/requery) - 适用于 Java 和 Android 的编译时 ORM 和 SQL 查询库。
- [GreenDAO](http://greenrobot.org/greendao/) - 轻量且快速的 ORM 解决方案。
- [ORMLite](http://ormlite.com/sqlite_java_android_orm.shtml) - 适用于 JDBC 和 Android 的轻量级 ORM Java 包。
- [ActiveAndroid](http://www.activeandroid.com) - 活动记录风格的 ORM。
- [Sugar ORM](http://satyan.github.io/sugar/) - 使用 Android 数据库的极其简单的方法。
- [DBFlow](https://github.com/agrosner/DBFlow) - 快速而强大的 ORM，具有编译时注释处理功能。
- [NexusData](https://github.com/dkharrat/NexusData) - Android 的对象图和持久性框架。
- [SimpleNoSQL](https://github.com/Jearil/SimpleNoSQL) - 适用于 Android 的简单 NoSQL 客户端。意味着使用键/值对和一些基本查询的文档存储。对于避免 SQL 代码的麻烦很有用。
- [RxSimpleNoSQL](https://github.com/xmartlabs/RxSimpleNoSQL) - SimpleNoSQL 的反应式扩展。使用 Observables 操作实体。

### 休息

- [Retrofit](https://square.github.io/retrofit/) - Retrofit 将您的 REST API 转变为 Java 接口。
- [Spring for Android - Rest Template](https://github.com/spring-projects/spring-android) - Android 的 Rest 客户端。

### 测试

- [Robotium](https://github.com/robotiumtech/robotium) - 用于黑盒 UI 测试的测试自动化框架。
- [Roboletric](http://robolectric.org/) - 单元测试框架，用于在工作站的 JVM 内运行测试，而不是在模拟器中。
- [AssertJ Android](https://github.com/square/assertj-android) - AssertJ 断言适用于 Android。
- [Green Coffee](https://github.com/mauriciotogneri/green-coffee) - 在 Android 仪器测试中运行 Cucumber 测试。

### 追踪

- [MobileAppTracking](https://www.tune.com/) - 跨多个广告网络跟踪您的营销活动。
- [Mixpanel](https://mixpanel.com/) - 用于分析用户的分析平台。
- [Countly](https://count.ly) - 基于 Node.js、MongoDB 和 Linux 的开源移动和 Web 分析、推送通知和崩溃报告平台。
- [CleverTap](https://clevertap.com) - 具有 100 万个免费活动的分析平台和用户参与平台

### 地图

- [Google-Directions-Android](https://github.com/jd-alexander/Google-Directions-Android) - 允许您计算两个位置之间的方向并使用 Google Directions API 在 Google 地图上显示路线。
- [Android Maps Extensions](https://github.com/mg6maciej/android-maps-extensions) - 扩展 Google Maps Android API v2 的功能，添加标记聚类等
- [MapScaleView](https://github.com/pengrad/MapScaleView) - Google Maps Android API 的比例尺
- [GLMap](https://globus.software) - 具有 MapCSS 样式的跨平台离线矢量地图。包括离线搜索和离线导航。

### 实用性
- [Conceal SharedPreferences](https://github.com/afiqiqmal/SharedChamber) - 使用称为“隐藏”的 Facebook 安全加密来保护首选项。
- [EventBus](http://greenrobot.github.io/EventBus/) - EventBus 是一个可以简化应用程序不同部分之间通信的库。
- [Otto](https://github.com/square/otto) - Android 的事件总线。
- [Weak handler](https://github.com/badoo/android-weak-handler) - android.os.Handler 的内存更安全实现。
- [Byte Buddy](http://bytebuddy.net) - 支持 Android 的运行时代码生成库。
- [Secure Preference Manager](https://github.com/prashantsolanki3/Secure-Pref-Manager) - 适用于 Android 的安全首选项管理器。它使用各种加密来保护您的应用程序的共享首选项。
- [LeakCanary](https://github.com/square/leakcanary) - 当内存泄漏发生时捕获它们。
- [Drekkar](https://github.com/coshx/drekkar) - 用于 WebView 和 JS 的 Android 事件总线。
- [Androl4b](https://github.com/sh4hin/Androl4b) - 用于评估 Android 应用程序的虚拟机。
- [DroidMVP](https://github.com/andrzejchm/DroidMVP) - Android 库可帮助您将 MVP 以及被动视图和演示模型模式合并到您的应用程序中。
- [EasyDeviceInfo](https://github.com/nisrulz/easydeviceinfo) - 以超级简单的方式获取设备信息。
- [Shutter-Android](https://github.com/levibostian/Shutter-Android) - 从设备相机捕获照片/视频或从图库应用程序获取照片/视频，无需运行时权限。
- [Validator](https://github.com/anderscheow/Validator) - 用于验证 TextInputLayout 内文本的实用程序类。
- [Keyboard Visibility Event](https://github.com/viniciusmo/keyboard-visibility-event-android/) - 用于处理软键盘可见性更改事件的 DSL。
- [TimeIt](https://github.com/yashovardhan99/timeit) - 一个适用于 Android 的秒表库，可以轻松地在应用程序中启动、暂停、显示和维护多个秒表。
- [Reactor](https://github.com/oky2abbas/reactor) - Reactor 是一个快速且安全的 Android 键值库。
 
### 调试工具

- [Linx](https://github.com/pedrovgs/Lynx) - 在设备内部显示 logcat 以进行调试构建
- [Scalpel](https://github.com/JakeWharton/scalpel) - 在手机中以 3D 方式查看整个层次结构。
- [Stetho](https://github.com/facebook/stetho) - 从 Chrome 调试层次结构和网络。
- [Android Debug Database](https://github.com/amitshekhariitbhu/Android-Debug-Database) - Android 调试数据库是一个功能强大的库，用于调试 Android 应用程序中的数据库和共享首选项。
- [Android Debug Bridge - ADB](https://github.com/mzlogin/awesome-adb/blob/master/README.en.md) - 帮助调试 Android 设备的命令行工具
- [ADB Enhanced](https://github.com/ashishb/adb-enhanced) - 为开发人员提供的 ADB 命令行包装器，这样开发人员就不必记住深奥的版本相关命令
- [Pidcat](https://github.com/JakeWharton/pidcat) - 彩色命令行 ADB 包装器，仅显示特定应用程序包的日志条目
- [AppSpector](https://appspector.com) - 远程Android和iOS调试和数据采集服务。您可以调试网络、日志、SQLite 和模拟设备的地理位置。


### 无线

- [SmartGattLib](https://github.com/movisens/SmartGattLib) - 简化蓝牙 SMART 设备（又称蓝牙 4.0 中的低功耗蓝牙）的工作。

### 聊天和消息传递

- [Applozic Android Chat SDK](https://github.com/AppLozic/Applozic-Android-SDK) - Android 聊天和消息 SDK，用于将实时聊天和应用内消息添加到您的 Android 应用程序中。
- [Qiscus SDK](https://github.com/qiscus/qiscus-sdk-android) - Qiscus SDK 是一个轻量级且功能强大的 Android 聊天库。 Qiscus SDK 将允许您轻松地将 Qiscus 引擎与您的应用程序集成，以制作炫酷的聊天应用程序。
- [Kommunicate Live Chat SDK](https://github.com/Kommunicate-io/Kommunicate-Android-Chat-SDK) - Kommunicate 在 Android 中提供开源实时聊天 sdk。 Kommunicate 可让您在移动（Android、iOS）应用程序和网站中添加实时实时聊天和应用内消息传递，以获取客户支持。
- [CometChat Voice, Video and Text Chat SDK with UI](https://github.com/cometchat-go/android-chat-sdk-demo) - 使用 CometChat 在几分钟内将语音、视频和文本聊天添加到您的应用程序（和网站）。 CometChat 的 SDK 包括一个完整的现成 UI，因此您无需花费任何时间来构建它！这还不是全部，CometChat 还提供开箱即用的支持，包括实时翻译、白板、屏幕共享、好友同步、基于角色的访问控制、学分扣除等。
- [Build a one-on-one Android chat app using Kotlin](https://www.cometchat.com/tutorials/build-one-on-one-chat-in-your-android-app-using-kotlin/) - 使用 CometChat Pro 在几分钟内用 Kotlin 构建一对一的 Android 聊天应用程序。本教程讨论登录、获取联系人列表、用户状态指示器、发送/接收消息等功能。
- [Stream Chat](https://getstream.io/tutorials/android-chat/) - 用于实时聊天的综合 SDK 和组件，由 [Stream](https://getstream.io/chat/) 提供支持。
- [Add Push Notifications to Your Android Chat App Using Kotlin](https://www.cometchat.com/tutorials/android-chat-push-notifications/) - 借助 CometChat Pro 和 Firebase Cloud Messaging (FCM) 在 Kotlin 中的 Android 聊天应用中添加推送通知。

#### 自定义对话框

- [MediaRecorderDialog](https://github.com/alhazmy13/MediaRecorderDialog) - 用于录制音频、存储音频并在手机中播放的自定义对话框。
- [HijriDatePicker](https://github.com/alhazmy13/HijriDatePicker) - 提供了一个 hijri（伊斯兰日历）日期选择器，根据 Google 的选择器材料设计原则设计。
- [Noty](https://github.com/emre1512/Noty) - 用于创建动画警报/对话框/警告的简单库。

### 版本检查

 - [AppUpdater](https://github.com/javiersantos/AppUpdater) - 全面且功能丰富的库，包括对 Amazon 和 FDroid 支票的支持。
 - [Gandalf](https://github.com/btkelly/gandalf) - 全面的功能和“伴侣”iOS 解决方案。
 - [Siren](https://github.com/eggheadgames/Siren) - 模仿流行的同名 iOS 库的重点功能集。支持 Play 和亚马逊。
 - [Fit](https://github.com/KeithYokoma/Fit) - 没有 UI 的版本检查回调框架。

### 日期和时间

- [ThreeTen Android Backport](https://github.com/JakeWharton/ThreeTenABP) - 适用于 Android 的 JSR-310 向后移植版本。
- [Joda-Time Android](https://github.com/dlew/joda-time-android) - 具有 Android 专业化的 Joda-Time 库。
- [True Time](https://github.com/instacart/truetime-android) - Android NTP时间库。获取不受设备时钟时间变化影响的真实当前时间。

### 运行时权限

- [Permission Dispatcher](https://github.com/permissions-dispatcher/PermissionsDispatcher) - 简单的基于注释的 API 来处理运行时权限。
- [RxPermissions](https://github.com/tbruyelle/RxPermissions) - 由 RxJava 提供支持的 Android 运行时权限。
- [NoPermission](https://github.com/NoNews/NoPermission) - 用于权限请求的简单 Android 库。仅由一个类组成。
- [Ask-Permission](https://github.com/Kishanjvaghela/Ask-Permission) - 简单的运行时权限管理器。
- [Gota](https://github.com/alhazmy13/Gota) - 简化 Android 权限。
- [EasyPermissions](https://github.com/googlesamples/easypermissions) - EasyPermissions 是一个包装器库，用于在面向 Android M 或更高版本时简化基本系统权限逻辑。

### 付款方式

- [Square In-App Payments for Android](https://developer.squareup.com/docs/in-app-payments-sdk/build-on-android) - 将 Square 支付集成到您的移动应用程序中，并支持数字钱包和存储卡支持以实现快速结账。

### 其他

- [Licensee](https://github.com/cashapp/licensee) - Licensee 是一个 Gradle 插件，它会验证您的依赖图的许可证是否符合您的预期，否则您的构建会失败！
- [Android Support library](https://developer.android.com/topic/libraries/support-library/) - Android 支持库包是一组提供向后兼容版本的 Android 框架 API 的代码库。
- [Google Play Services](https://developers.google.com/android/guides/overview) - 用于访问 Google 服务的库，例如帐户同步、Google+（共享、单点登录）、Google 地图、位置 API、Google Play 游戏、云消息、Android 设备管理器等。
- [Tape](https://github.com/square/tape) - 适用于 Android 和 Java 的闪电般快速、事务性、基于文件的 FIFO。
- [Guava: Google Core Libraries for Java](https://github.com/google/guava) - 集合、缓存、原语支持、并发库、通用注释、字符串处理、I/O 等等。
- [Android Scripting](https://github.com/damonkohler/sl4a) - 允许在 Android 上运行脚本语言。
- [Android Priority Job Queue](https://github.com/yigit/android-priority-jobqueue) - 实施作业队列以轻松安排在后台运行的作业（任务），从而提高用户体验和应用程序稳定性。
- [RateMeMaybe](https://github.com/nspo/RateMeMaybe) - 询问用户是否想要打开 Play 商店来评价您的应用程序。
- [Easy Rating Dialog](https://github.com/fernandodev/easy-rating-dialog) - Lib 提供了一种简单的方法来显示评级应用程序的警报对话框。
- [ZXing Android-Integration](https://github.com/zxing/zxing) - 通过 Intent 与条码扫描仪集成。
- [Gradle Retrolambda Plugin](https://github.com/evant/gradle-retrolambda) - Android 上的 Java 8 Lambda！
- [RxJava](https://github.com/ReactiveX/RxJava) - RxJava – JVM 的反应式扩展 – 一个使用 Java VM 的可观察序列编写异步和基于事件的程序的库。
- [RxAndroid](https://github.com/ReactiveX/RxAndroid) - 添加最少的 RxJava 绑定，以便轻松编写反应式 Android java 代码。
- [RxBinding](https://github.com/JakeWharton/RxBinding) - RxBinding – 来自平台和支持库的 Android UI 小部件的 RxJava 绑定 API。
- [Caffeine](https://github.com/percolate/caffeine) - 有助于加快 Android 开发速度的实用程序类的集合。
- [AboutLibraries](https://github.com/mikepenz/AboutLibraries) - 自动生成“关于此应用程序”部分，其中包含所用库的列表。
- [AudioPlayerView](https://github.com/HugoMatilla/AudioPlayerView) - 从 URL 加载音频并具有基本播放工具的视图。
- [andle](https://github.com/Jintin/andle) - 命令行工具可帮助您同步依赖项、sdk 或构建工具版本。
- [Typography](https://github.com/workarounds/typography) - 一个 Android 库，可以轻松在视图中使用自定义字体。
- [Calligraphy](https://github.com/chrisjenx/Calligraphy) - Android 中的自定义字体是一种不错的方式。
- [transai](https://github.com/Jintin/transai) - 命令行工具可帮助您管理本地化字符串文件。
- [Android-Link-Preview](https://github.com/LeonardoCardoso/Android-Link-Preview) - 它从 URL 进行预览，获取标题、相关文本和图像等所有信息。
- [Sensey](https://github.com/nisrulz/sensey) - 瞬间检测手势。
- [UserAwareVideoView](https://github.com/kevalpatel2106/UserAwareVideoView) - 定制的视频视图将在用户不看设备屏幕时自动暂停视频！
- [Flexbox Layout](https://github.com/google/flexbox-layout) - FlexboxLayout 是一个库，它为 Android 带来了 CSS 灵活框布局模块的类似功能。
- [Agile Boiler Plate](https://github.com/xresco/Android-Agile-Boiler-Plate) - 样板基于 MVP 架构，完全基于使用 Dagger2 的依赖注入设计模式。
- [Gradle buildSrcVersions](https://github.com/jmfayard/buildSrcVersions) - 用于简化依赖关系管理的 kotlin dsl
- [Teller](https://github.com/levibostian/Teller-Android/) - Teller 方便下载、保存和读取应用程序的缓存数据。保持用户数据最新并删除那些烦人的加载屏幕！

## 资源

- [Programming Community Curated Resources for Learning Android Development](https://hackr.io/tutorials/learn-android-development) - Android 教程和课程由编程社区提交和投票。
- [Vogella Tutorials](https://www.vogella.com/tutorials/android.html) - Lars Vogel 的非常好的教程。
- [Android Design in Action 视频系列](https://www.youtube.com/playlist?list=PLWz5rJ2EKKc8j2B95zGMb8muZvrIy-wcF) Google Android 设计团队的视频系列。
- [Android DevBytes Video Series](https://www.youtube.com/playlist?list=PLWz5rJ2EKKc_XOgcRukSoKKjewFJZrKV0) - 它是 Android Design in Action 系列的技术对应部分。
- [Developing for Android](https://medium.com/google-developers/developing-for-android-introduction-5345b451567c) - Google 员工 Chet Hasae 等人撰写的一系列文章，回答了最常见的问题：“开发 Android 应用程序时需要记住哪些重要规则？”。
- [Android Hive Tutorials](https://www.androidhive.info) - 对于初学者来说非常好的教程。
- [Android Weekly](https://androidweekly.net) - 时事通讯，每周提供有关 Android 的信息。
- [Android Asset Studio](http://romannurik.github.io/AndroidAssetStudio/) - 图标和其他资源的生成器。
- [Android 操作栏样式生成器](http://jgilfelt.github.io/android-actionbarstylegenerator/)。
- [Device Art Generator](https://developer.android.com/distribute/marketing-tools/device-art-generator) - 将应用程序屏幕截图包裹在真实设备图稿中。
- [Android UI design resources](https://androiduiux.com/free-design-resources/) - 由 UI/UX 领域的 Google 开发者专家为您提供各种设计资源。
- [Pencil Project](https://pencil.evolus.vn/) - 一款开源原型设计软件。
- [How to Make Android Apps](https://www.youtube.com/playlist?list=PLGLfVvz_LVvSPjWpLPFEfOCbezi6vATIh) - Derek Banas 的视频教程。
- [android-blogs](https://github.com/vbauer/android-blogs) - 列出有关 Android 的博客。
- [Future Studio](https://futurestud.io/tutorials/tag/android) - 关于 Retrofit、Picasso、Glide 和 Gson 的丰富 Android 教程。
- [Android Tips & Tricks](https://github.com/nisrulz/android-tips-tricks) - 有关 Android 开发提示和技巧的速查表。
- [Associate Android Developer Certification Materials](https://github.com/Amejia481/Associate-Android-Developer-Certification) - 准备考试的材料集合。
- [Google Developers Training](https://developer.android.com/courses/) - Google 开发人员官方培训页面列出了针对初学者和经验丰富的开发人员的各种有用的学习资源。
- [Mindorks](https://mindorks.com/) - 成为一名完整、快乐的 Android 开发者。
- [AndroidVille](https://ayusch.com/) - 成为一名更好的 Android 工程师。致力于 Android 开发的网站，涵盖 RxJava、Android Zygote 等高级主题。
- [Android Stack Weekly](https://blog.canopas.com/tagged/canopas-android-weekly) - 有关 Android 世界新开发和更新的每周时事通讯。

### 代码示例
- [Android Architecture Blueprints](https://github.com/android/architecture-samples) - Android 架构蓝图项目演示了帮助解决或避免常见 Android 问题的策略。
- [Kotlin MVVM example](https://github.com/emedinaa/kotlin-mvvm) - 有关 MVVM（模型视图视图模型）模式的示例。
- [Kotlin VIPER example](https://github.com/OmiSoftNet/AndroidViperTemplate) - VIPER（视图交互器演示者实体路由器）模式的示例。
- [Complete-Google-Map-API-Tutorial](https://github.com/mohammadima3oud/Complete-Google-Map-API-Tutorial) - 通过完整的示例，了解如何从基础到高级使用 Android 版 Google Map API。
- [Android Modular Architecture](https://github.com/VMadalin/kotlin-sample-app) - Android 示例应用程序使用模块化、干净、可扩展、可测试的架构，采用 Kotlin 编写，遵循 Jetpack 的最佳实践。

### 播客
- [Fragmented](https://fragmentedpodcast.com/) 是 Android 开发者播客，Donn Felker 和 Kaushik Gopal 在其中谈论如何构建优秀的软件并成为更好的 Android 开发者。
- [Android Developers Backstage](http://androidbackstage.blogspot.com/) 是一个由 Android 开发者制作并为 Android 开发者服务的播客。该节目由 Android 工程团队的开发人员主持，涵盖了 Android 程序员感兴趣的话题，并对 Google Android 团队的工程师进行了深入的讨论和采访。
- [Android Dialogs](https://www.youtube.com/channel/UCMEmNnHT69aZuaOrE-dF6ug/feed) 是一个基于视频的播客，他们在其中与来自 Android 社​​区的人们进行了简短的对话。
- [The Context](https://github.com/artem-zinnatullin/TheContext-Podcast) 一个关于 Android 开发的播客，由 Hannes Dorfmann、Artem Zinnatullin 和精彩的嘉宾参与！
- [Talking Kotlin](https://talkingkotlin.com/) - 关于 Kotlin 等的播客。
- [Android Authority](https://www.androidauthority.com/podcast/) 是每周一次的 Android 播客，由 Android Authority 团队的 Adam Doud、Joe Hindy 和 Jonathan Feist 主持。
- [Android Central](https://www.androidcentral.com/podcast) - 是由 Android Central 团队主办的每周一次的 Android 播客。

### 更多库列表
- [The Android Arsenal](https://android-arsenal.com/) - Android 库的大列表
- [Square libraries](https://square.github.io/) - Square 多个高质量图书馆。
- [Awesome Android @LibHunt](https://android.libhunt.com) - 您的首选 Android 工具箱。
- [Android Store](https://mindorks.com/android/store) - 搜索 Android 库、项目和工具。

## 发展替代方案

我个人的建议是（目前）使用 android api 构建本机应用程序。 Scala 可以帮助使用更简洁的代码构建此本机应用程序，但它添加了许多方法（需要 Multidex）。 Kotlin 是一种现代语言，与 java 项目具有 100% 的互操作性**无需 multidex**。但在某些用例中，跨平台开发等替代方案也可能有用。

### C&#35;

- [Xamarin](https://visualstudio.microsoft.com/xamarin/) - 使用 C# 创建本机 iOS、Android、Mac 和 Windows 应用程序的框架。

### HTML、CSS 和 JavaScript

- [PhoneGap](https://phonegap.com) - Adobe 的开源框架，用于使用 HTML、CSS 和 JavaScript 创建跨平台移动应用程序。
- [Titanium](http://www.appcelerator.com/mobile-app-development-products/) - 使用 JavaScript 创建“本机”跨平台应用程序的开源框架。
- [NativeScript](https://www.nativescript.org/) - 一个开源框架，用于使用 JavaScript 从单个代码库构建本机 iOS 和 Android 应用程序。
- [React Native](https://github.com/facebook/react-native) - Facebook 提供的用于使用 React 构建本机应用程序的框架。
- [Ionic Framework](https://ionicframework.com) - 一个框架，用于使用 AngularJS 构建具有移动优化的 HTML、CSS 和 JS 的混合应用程序。
- [Apache Cordova](https://github.com/apache/cordova-android) - 基于 Cordova 的应用程序的核心是使用 Web 技术编写的应用程序：HTML、CSS 和 JavaScript。
- [Capacitor](https://github.com/ionic-team/capacitor) - 为 iOS、Android 和 Web 构建跨平台本机渐进式 Web 应用程序。非常有前途的科尔多瓦替代品。

### 卢阿
- [Corona SDK](https://coronalabs.com/product/) - 用于创建本机 iOS 和 Android 应用程序（尤其是游戏）的框架。

### 斯卡拉
- [Scaloid](https://github.com/pocorall/scaloid) - 使用 Scala 进行不那么痛苦的 Android 开发的库。
- [Macroid](https://github.com/47deg/macroid) - 适用于 Android 的模块化功能 UI 语言。

### 格罗维
- [Groovy on Android](http://melix.github.io/blog/2014/06/grooid.html) - Android 上的 Groovy 简介。
- [Groovy Language Support for Android](https://github.com/groovy/groovy-android-gradle-plugin) - 用于为 Android 编译 Groovy 的 Gradle 插件。
- [SwissKnife](https://github.com/Arasthel/SwissKnife) - 一个多用途 Groovy 库，包含使用注释的 Android 视图注入和线程化。

### 科特林
- [Anko](https://github.com/Kotlin/anko) - 由 JetBrains 用 Kotlin 编写的 Android DSL。
- [Kotterknife](https://github.com/JakeWharton/kotterknife) - 基于ButterKnife用Kotlin编写的Android视图注入
- [Android Kotlin Samples](https://github.com/irontec/android-kotlin-samples) - 一些用 Kotlin 编写的基本 Android 代码示例。
- [Kotlin coding puzzles](https://github.com/igorwojda/kotlin-coding-puzzle) - 一系列编程挑战有助于提高白板编码和解决问题的技能。
- [KAndroid](https://github.com/pawegio/KAndroid) - 轻量级库提供有用的扩展，以消除 Android SDK 中的样板代码。
- [RxKotlin/Pocket](https://github.com/RxKotlin/Pocket) - 这个应用程序帮助用户轻松保存链接，并且可以每周导出到 Evernote。
- [Android Clean Architecture - Kotlin](https://github.com/patrickyin/clean-architecture-android-kotlin) - 一个基础项目，使用 Uncle Bob 的干净架构、Kotlin 语言和最新的 Android 技术。
- [Koin](https://insert-koin.io/) - Kotlin 的轻量级依赖注入框架
- [AppDimens](https://github.com/bodenberg/appdimens) - 适用于任何屏幕的智能响应尺寸（FX、DY、DP、SP、对数）

### 颤动
- [Flutter](https://flutter.dev/) - Google 的移动应用 SDK 可在非常短的时间内为 Android 和 iOS 提供高质量的本机界面。

# 性能
- [awesome-android-performance](https://github.com/Juude/awesome-android-performance) - 用于性能优化的精彩 Android 教程、视频和工具列表。
- [Booster](https://github.com/didi/booster) - Booster是一款针对Android应用程序的优化工具包。

# 其他很棒的列表
其他令人惊叹的很棒的列表可以在 [awesome-awesomeness](https://github.com/bayandin/awesome-awesomeness) 列表中找到。

## 贡献

随时欢迎您的贡献！请先阅读[贡献指南](contributing.md)。
