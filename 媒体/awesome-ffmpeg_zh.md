# 很棒的 FFmpeg [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> [FFmpeg](http://ffmpeg.org) 是一个用于录制、转换和流式传输音频和视频的跨平台解决方案。

<p align="center">
  <img width="400" src="https://cdn.rawgit.com/transitive-bullshit/awesome-ffmpeg/master/ffmpeg-logo.svg">
</p>


## 内容

- [Docs](#docs)
- [JavaScript](#javascript)
- [Native](#native)
- [Mobile](#mobile)
- [Tutorials](#tutorials)
- [Community](#community)


## 文档

由于 FFmpeg 功能的范围和复杂性，FFmpeg 的官方文档对于初学者来说很难理解。话虽如此，它们作为参考仍然非常有用。

- [FFmpeg.org](http://ffmpeg.org) - 一切开始的地方。
- [Filters](https://ffmpeg.org/ffmpeg-filters.html) - FFmpeg 强大的过滤器链（缩放、裁剪、连接、合并等）的文档。这是我使用 FFmpeg 时访问次数最多的链接之一。
- [Man page](https://man.cx/ffmpeg) - FFmpeg 官方手册页。
- [Wiki & Bug Tracker](https://trac.ffmpeg.org) - 这里有很多很棒的信息。
- [CLI flags](https://github.com/transitive-bullshit/ffmpeg-cli-flags/blob/master/readme.md) - 所有 FFmpeg 命令行标志的综合列表。对于搜索在野外遇到的随机标志非常有用。


## JavaScript

- [fluent-ffmpeg](https://github.com/fluent-ffmpeg/node-fluent-ffmpeg) - [FFmpeg](http://www.ffmpeg.org) 的流畅 API。如果您只使用此列表中的一种工具，则应该是这个。
- [ffmpeg-probe](https://github.com/transitive-bullshit/ffmpeg-probe) - ffprobe 的包装，用于获取有关媒体文件的信息。
- [ffmpeg-concat](https://github.com/transitive-bullshit/ffmpeg-concat) - 使用 FFmpeg 和性感的 OpenGL 过渡将视频列表连接在一起。
- [editly](https://github.com/mifi/editly) - 声明性视频编辑工具和库，具有流畅的动画和过渡。
- [ffmpeg-generate-video-preview](https://github.com/transitive-bullshit/ffmpeg-generate-video-preview) - 从视频生成有吸引力的图像条或 GIF 预览。
- [ffmpeg-extract-frame](https://github.com/transitive-bullshit/ffmpeg-extract-frame) - 从视频中提取单个帧。
- [ffmpeg-extract-frames](https://github.com/transitive-bullshit/ffmpeg-extract-frames) - 使用 FFmpeg 从视频中提取屏幕截图。
- [gif-extract-frames](https://github.com/transitive-bullshit/gif-extract-frames) - 从 GIF 中提取帧，包括帧间合并。
- [ffmpeg-extract-audio](https://github.com/transitive-bullshit/ffmpeg-extract-audio) - 从媒体文件中提取音频流。
- [ffmpeg-on-progress](https://github.com/transitive-bullshit/ffmpeg-on-progress) - 使用 Fluent-ffmpeg 可靠地报告进度的实用程序。
- [ffmpeg.js](https://github.com/Kagami/ffmpeg.js) - 通过 Emscripten 将 FFmpeg 移植到 JavaScript。允许在客户端有限地使用 FFmpeg。
- [ffmpeg-static](https://github.com/eugeneware/ffmpeg-static) - 为 macOS、Linux 和 Windows 提供静态 FFmpeg 二进制文件。对于 CI 测试非常有用。
- [tangerine](https://github.com/niftylettuce/tangerine) - 使用 Node.js、FFmpeg、WebSockets 和 Lad 的网络摄像头流服务。
- [ffparser](https://github.com/NiKlimenko/FFParser) - 按帧直接将输入流解析到代码中作为缓冲区。


## 本地人

- [ffmpeg-gl-transition](https://github.com/transitive-bullshit/ffmpeg-gl-transition) - 用于在视频流之间应用 GLSL 转换的 FFmpeg 过滤器 ([gl-transitions](https://gl-transitions.com/))。


## 手机

- [simplest ffmpeg mobile](https://github.com/leixiaohua1020/simplest_ffmpeg_mobile) - 适用于 Android 和 iOS 的 FFmpeg 示例。
- [ijkplayer](https://github.com/Bilibili/ijkplayer) - 基于FFmpeg的Android/iOS视频播放器。


## 教程

- [如何用不到 1k 行编写视频播放器](http://dranger.com/ffmpeg)
- [艰难地学习 FFmpeg libav](https://github.com/leandromoreira/ffmpeg-libav-tutorial)
- [Applying OpenGL Shaders with FFmpeg](https://nervous.io/ffmpeg/opengl/2017/01/31/ffmpeg-opengl) - 以及[后续](https://nervous.io/ffmpeg/opengl/2017/05/15/ffmpeg-pbo-yuv)。
- [FFmpeg 初学者食谱](https://github.com/talwrii/ffmpeg-cookbook)
- [用于视频自动化的 FFmpeg Cheatsheet](https://github.com/rendi-api/ffmpeg-cheatsheet)


## 社区

- [堆栈溢出](https://superuser.com/questions/tagged/ffmpeg)
- [邮件列表](https://www.ffmpeg.org/contact.html#MailingLists)
- [IRC](https://www.ffmpeg.org/contact.html#IRCChannels)


## 贡献

欢迎投稿！请先阅读[贡献指南](contributing.md)。


## 许可证

[![CC0](http://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](http://creativecommons.org/publicdomain/zero/1.0)

在法律允许的范围内，[Travis Fischer](https://github.com/transitive-bullshit) 已放弃本作品的所有版权以及相关或邻接权。

<a href="https://twitter.com/transitive_bs">在 Twitter 上关注我<img src="https://storage.googleapis.com/saasify-assets/twitter-logo.svg" alt="twitter" height="24px"align="center"></a>支持我的 OSS 工作
