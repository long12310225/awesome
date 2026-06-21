# 很棒的 RxJava [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

[<img src =“http://reactivex.io/assets/Rx_Logo_S.png”align =“right”width =“100”>](http://reactivex.io/)

> 使用 [RxJava](https://github.com/ReactiveX/RxJava) 的有用资源

*受到[awesome](https://github.com/sindresorhus/awesome)列表的启发。*

## 绑定

* [RxAndroid](https://github.com/ReactiveX/RxAndroid) - RxJava 的 Android 特定绑定。
* [RxBinding](https://github.com/JakeWharton/RxBinding) - 来自平台和支持库的 Android UI 小部件的 RxJava 绑定 API。
* [rx-preferences](https://github.com/f2prateek/rx-preferences) - Android 的反应式“SharedPreferences”。
* [RxPermissions](https://github.com/tbruyelle/RxPermissions) - 由 RxJava 提供支持的 Android M 运行时权限。
* [SQLBrite](https://github.com/square/sqlbrite) - 围绕 SQLiteOpenHelper 和 ContentResolver 的轻量级包装器，它向查询引入了反应式流语义。
* [Android-ReactiveLocation](https://github.com/mcharmas/Android-ReactiveLocation) - 将 Google Play Service API 封装在出色的 RxJava Observables 中的小型库，将样板代码降至最低。
* [ReactiveNetwork](https://github.com/pwittchen/ReactiveNetwork) - Android 库使用 RxJava Observables 监听网络连接状态和 WiFi 信号强度的变化。
* [ReactiveSensors](https://github.com/pwittchen/ReactiveSensors) - Android 库使用 RxJava Observables 监控硬件传感器。
* [RxPalette](https://github.com/hzsweers/RxPalette) - Android 上 Palette 库的 RxJava 绑定。
* [rxjava-jdbc](https://github.com/davidmoten/rxjava-jdbc) - 使用 jdbc 和 RxJava Observables 进行数据库调用的高效执行和功能组合。
* [rxjava-file](https://github.com/davidmoten/rxjava-file) - RxJava 可观察文件，包括 NIO 事件。
* [RxTuples](https://github.com/pakoito/RxTuples) - 与 RxJava 一起使用的简单元组。
* [RxAnimationBinding](https://github.com/blipinsk/RxAnimationBinding) - 用于 Android 动画的 RxJava 绑定 API。

## 公用事业
* [RxJavaAsyncUtil](https://github.com/ReactiveX/RxJavaAsyncUtil) - RxJava 的异步实用程序。
* [RxJavaJoins](https://github.com/ReactiveX/RxJavaJoins) - 连接 RxJava 的运算符。
* [RxJavaMath](https://github.com/ReactiveX/RxJavaMath) - RxJava 的数学运算符。
* [RxJavaString](https://github.com/ReactiveX/RxJavaString) - 
RxJava 的字符串和字节运算符。
* [RxJavaComputationExpressions](https://github.com/ReactiveX/RxJavaComputationExpressions) - RxJava 的计算表达式。
* [rxjava-extras](https://github.com/davidmoten/rxjava-extras) - 与 RxJava 一起使用的实用程序。
* [RxActions](https://github.com/pakoito/RxActions) - 与 RxJava 一起使用的简单 ActionN 组合。
* [RxRelay](https://github.com/JakeWharton/RxRelay) - RxJava 类型既是 Observable 又是 Action1。
* [Frodo](https://github.com/android10/frodo) - 用于记录 RxJava Observables 和订阅者的 Android 库。
* [RxPartialApplication](https://github.com/pakoito/RxPartialApplication) - FuncN 和 ActionN 在 RxJava 上的简单部分应用。
* [RxCurrying](https://github.com/pakoito/RxCurrying) - RxJava 上 FuncN 和 ActionN 的简单柯里化。
* [RxEither](https://github.com/eleventigers/rxeither) - 任一类型为 RxJava。
* [RxReplayingShare](https://github.com/JakeWharton/RxReplayingShare) - 一个 RxJava 转换器，结合了 replay(1)、publish() 和 refCount() 运算符。
* [RxFunctions](https://github.com/pakoito/RxFunctions) - 与 RxJava 一起使用的高级函数组合。
* [rxlint](https://bitbucket.org/littlerobots/rxlint) - RxJava 代码的 Android lint 规则。
* [RxComprehensions](https://github.com/pakoito/RxComprehensions) - 通过抽象链式 flatMap、concatMap 和 switchMap 来减少 RxJava 中的样板代码。

## 测试
* [assertj-rx](https://github.com/ribot/assertj-rx) - RxJava Observables 的 AssertJ 断言。
* [rxpresso](https://github.com/novoda/rxpresso) - 使用 RxJava 对 Android 应用程序进行简单的 Espresso UI 测试。

## 指南

* [RxJava-Android-Samples](https://github.com/kaushikgopal/RxJava-Android-Samples) - 通过示例学习 Android 版 RxJava。
* [Intro-To-RxJava](https://github.com/Froussios/Intro-To-RxJava) - 关于 RxJava 的详尽教程。

## 文章

* [Rx glitches aren't actually a problem](http://staltz.com/rx-glitches-arent-actually-a-problem.html) - 故障是 Observables 发出的暂时的不一致。安德烈·斯塔尔茨 (André Staltz) 探讨了为什么这并不是一个真正的问题。
* [RxJava's repeatWhen and retryWhen, explained](http://blog.danlew.net/2016/01/25/rxjavas-repeatwhen-and-retrywhen-explained/) - `repeatWhen` 和 `retryWhen` 乍一看相当令人困惑。 Dan Lew 深入解释了运算符。
* [RxJava - The Problem with Subjects](http://tomstechnicalblog.blogspot.co.uk/2016/03/rxjava-problem-with-subjects.html) - 托马斯·尼尔德解释了为什么“Subject”不是万能药。

## 工具

* [RxMarbles](http://rxmarbles.com/) - Rx Observables 的交互图。

## 社区

* [谷歌集团](http://groups.google.com/d/forum/rxjava)
* [StackOverflow](http://stackoverflow.com/search?q=rx-java)
* [Twitter 上的“@RxJava”](http://twitter.com/RxJava)
* [Gitter 上的“ReactiveX/RxJava”](https://gitter.im/ReactiveX/RxJava)
* [GitHub 问题](https://github.com/ReactiveX/RxJava/issues)

## 许可证

[![CC0](https://i.creativecommons.org/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

在法律允许的范围内，[Jokubas Dargis](http://jokubasdargis.net/) 已放弃本作品的所有版权以及相关或邻接权。
