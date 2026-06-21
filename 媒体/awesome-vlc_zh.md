# 很棒的 VLC [<img src="https://cdn.worldvectorlogo.com/logos/vlc.svg"align="right" alt="VLC" width="128">](https://github.com/mfkl/awesome-vlc) [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> [VLC](https://www.videolan.org/vlc/) 是一个免费开源的跨平台多媒体播放器和框架，可以播放大多数多媒体文件以及 DVD、音频 CD、VCD 和各种流媒体协议。

这是有关 VLC 和 LibVLC 的精彩资源列表。

## 内容

- [Docs](#docs)
- [VLC 原生插件](#vlc-native-plugins)
- [VLC lua 扩展](#vlc-lua-extensions)
- [Apps](#apps)
- [Bindings](#bindings)
- [Tutorials](#tutorials)
- [Ebook](#ebook)
- [Community](#community)

## 文档

- [videolan.org](https://www.videolan.org/) - 一切开始的地方。
- [LibVLC API docs](https://videolan.videolan.me/vlc/group__libvlc.html) - LibVLC 引擎的文档。 C API。
- [Wiki](https://wiki.videolan.org/) - 这里有很多很棒的信息。
- [Code & Bug tracker](https://code.videolan.org/videolan/vlc/-/issues) - 最近从 Trac 移出，包含许多有关错误和功能请求的有价值的信息。
- [CLI flags](https://wiki.videolan.org/VLC_command-line_help) - 所有 VLC 命令行标志的综合列表。对于搜索在野外遇到的随机标志非常有用。

## VLC 原生插件

- [vlc-pause-click-plugin](https://github.com/nurupo/vlc-pause-click-plugin) - VLC 插件，可在鼠标单击时暂停/播放视频。
- [vlc-tip-plugin](https://github.com/aklexel/vlc-tip-plugin) - TIP（请翻译一下）是VLC媒体播放器的插件，可以帮助您通过观看视频来学习语言。
- [vlc-bittorrent](https://github.com/johang/vlc-bittorrent) - VLC 的 BitTorrent 插件。
- [vlc-plugin-marker](https://github.com/nemosharma6/vlc-plugin-marker) - 标记插件使您能够标记视频的重要部分。这些部分可以稍后查看，无需在整个视频中搜索。
- [vlc-win10smtc](https://github.com/spmn/vlc-win10smtc) - 将 VLC Media Player 与 Windows 10 系统媒体传输控件 (SMTC) 集成的插件。
- [vlc-mixer](https://github.com/lachie/vlc-mixer) - 用 Zig 编写的音频混合器 VLC 插件。

## VLC Web 和 lua 扩展

- [VideoLAN addons website](https://addons.videolan.org/browse/) - VideoLAN 插件网站。
- [vlc-delete](https://github.com/surrim/vlc-delete) - VLC 扩展用于从硬盘中删除视频。
- [TraktForVLC](https://github.com/XaF/TraktForVLC) - 自动 trakt.tv 您在 VLC 上观看的内容。
- [playlist-youtube-vlc](https://github.com/Abstraxt-AA/playlist-youtube-vlc) - 用于解析 Youtube 播放列表的 Lua 插件。
- [vlc-super-skipper](https://github.com/Trevelopment/vlc-super-skipper) - 自动跳过开头和结尾序列。
- [vlc-mcp-server](https://github.com/piebro/vlc-mcp-server) - MCP（模型上下文协议）服务器，使用 VLC HTTP API 和使用 LLM 的自然语言来播放和控制电影。
- [vlc-auto-dir-enqueue-prev-next](https://github.com/eltoro0815/vlc-auto-dir-enqueue-prev-next) - 文件开始播放后，会自动将同一目录中的上一首和下一首曲目添加到 VLC 播放列表中。

## 应用程序

- [VLC desktop](https://code.videolan.org/videolan/vlc) - 在 Linux/Windows (Qt) 和 macOS (Cocoa) 上运行的原始桌面应用程序。
- [VLC iOS](https://code.videolan.org/videolan/vlc-ios) - VLC for iOS 是 VLC 在 iOS/tvOS 平台上的官方端口。
- [VLC Android](https://code.videolan.org/videolan/vlc-android) - 适用于 Android、Android TV 和 ChromeOS 的 VLC。
- [VLC Benchmark (Beta)](https://code.videolan.org/videolan/vlc-bench) - 视频解码和渲染基准测试工具，基于VLC。

## 绑定

- [VLCKit](https://code.videolan.org/videolan/VLCKit) - Objective-C 中 macOS、iOS、iPadOS 和 tvOS 的 libvlc 绑定。
- [libvlcjni](https://code.videolan.org/videolan/vlc-android/-/tree/master/libvlc) - Android 平台的 libvlc 绑定。
- [vlc-unity](https://code.videolan.org/videolan/vlc-unity) - VLC 的 Unity3D 集成。
- [python-vlc](https://github.com/oaubert/python-vlc) - Python vlc 绑定。
- [vlcj](https://github.com/caprica/vlcj) - vlc 媒体播放器（桌面）的 Java 框架。
- [LibVLCSharp](https://github.com/videolan/libvlcsharp) - LibVLC 的跨平台 .NET/Mono 绑定。
- [libvlc-go](https://github.com/adrg/libvlc-go) - libVLC 和高级媒体播放器接口的 Go 绑定。
- [libvlcpp](https://code.videolan.org/videolan/libvlcpp/) - libvlc 的 C++ 绑定。
- [vlc.js (beta)](https://code.videolan.org/jbk/vlc.js) - WebAssembly 对 LibVLC 的支持。
- [flutter_vlc_player](https://github.com/solid-software/flutter_vlc_player) - Flutter 与 LibVLC 的绑定。
- [dart_vlc](https://github.com/alexmercerind/dart_vlc) - libvlc 的 Dart 绑定。
- [WebChimera.js](https://github.com/RSATom/WebChimera.js) - libvlc 的电子结合。
- [libvlc-zig](https://github.com/kassane/libvlc-zig) - libVLC 的 Zig 绑定。

## 教程

- [HLS Record tutorial](https://mfkl.github.io/hls/2018/10/10/How-to-record-HLS-stream-with-LibVLCSharp-and-.NET-Core.html) - 如何使用 LibVLCSharp 和 .NET Core 录制 HLS 流。
- [RTSP mosaic tutorial](https://mfkl.github.io/libvlc/rtsp/xamarin/forms/2018/12/05/crossplatform-RTSP-mosaic-views-with-libvlcsharp.html) - 使用 LibVLCSharp 的跨平台 RTSP 马赛克视图。
- [MediaElement tutorial](https://doumer.me/vlc-media-player-in-xamarinforms-alternative-avplayer-andmediaplayer) - Xamarin Forms 中的 VLC 媒体播放器控件。
- [LibVLC LLM Skill](https://github.com/mfkl/libvlc-skill) - Claude Code 插件，可让 AI 编码助手深入了解 libvlc API（3.x 和 4.x），即 VLC 媒体播放器背后的多媒体框架。
## 电子书

- [The Good Parts of LibVLC](https://mfkl.gumroad.com/l/libvlc-good-parts) - 第一本有关 VideoLAN 非营利组织和开源 LibVLC 开发人员 SDK 的电子书。

## 社区

- [Stack Overflow - LibVLC](https://stackoverflow.com/questions/tagged/libvlc) - Stack Overflow 上的 LibVLC。
- [Stack Overflow - VLC](https://stackoverflow.com/questions/tagged/vlc) - Stack Overflow 上的 VLC。
- [Mailing Lists](https://www.videolan.org/support/lists.html) - VideoLAN 开发人员邮件列表。
- [IRC](https://wiki.videolan.org/Contact_VideoLAN/#IRC) - VideoLAN IRC 信息。
- [Forum](https://forum.videolan.org/) - VideoLAN 官方论坛。
- [LibVLC Discord](https://discord.gg/3h3K3JF) - 官方 LibVLC 社区 Discord 服务器。
- [Twitter](https://twitter.com/videolan) - VideoLAN 官方 Twitter 帐户。
- [Reddit](https://www.reddit.com/r/vlc) - Reddit 上的非官方 VLC 社区。

## 贡献

欢迎[贡献](contributing.md)！
