# 精彩的广播 [![Awesome](https://cdn.jsdelivr.net/gh/sindresorhus/awesome@d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
为广播公司精心挑选的令人惊叹的开源资源列表。

* [精彩的广播](#awesome-broadcasting-)
  * [动画、图形和视频播放](#animation-graphics--video-playout)
  * [时钟和工作室屏幕](#clocks--studio-screens)
  * [Codecs](#codecs)
  * [Communication](#communication)
  * [配套屏幕](#companion-screens)
  * [联网电视](#connected-tvs)
  * [控制系统](#control-systems)
  * [分布式媒体处理](#distributed-media-processing)
  * [Documentation](#documentation)
  * [数字视频广播和无线网络](#dvb--wifi)
  * [混合无线电](#hybrid-radio)
  * [LiveIP](#liveip)
  * [媒体播放器](#media-players)
  * [Metadata](#metadata)
  * [监控和质量控制](#monitoring--quality-control)
  * [多媒体内容处理](#multimedia-content-processing)
  * [网络和存储测试](#network--storage-testing)
  * [NMOS](#nmos)
  * [Podcasting](#podcasting)
  * [广播制作](#radio-production)
  * [清单自动化](#rundown-automation)
  * [SCTE-35 和 SCTE-104](#scte-35--scte-104)
  * [软件无线电](#software-defined-radio)
  * [Streaming](#streaming)
  * [Subtitling](#subtitling)
  * [视频制作](#video-production)
* [Resources](#resources)
  * [Blogs](#blogs)
  * [Websites](#websites)
* [Contributing](#contributing)

## 动画、图形和视频播放

* [Aurena](https://github.com/thaytan/aurena) - 一种网络分布式媒体播放系统。
* [Blender](https://projects.blender.org/blender/blender) - 3D 创建套件，支持 3D 建模、动画、运动跟踪、视频编辑等（概述[此处](https://developer.blender.org/)）。
* [Bridge](https://github.com/svt/bridge) - 下一代图形控制软件，具有扩展支持。
* [caspar-obs-client](https://github.com/michalramus/caspar-obs-client) - Python GUI 应用程序用于 CasparCG 媒体服务器和 OBS Studio 之间的无缝集成。
* [CasparCG](http://www.casparcg.com/) - 一款专业的图形和视频播放软件，自 2006 年以来已在 24/7 广播中得到验证。
* [ffplayout](https://github.com/ffplayout/ffplayout) - 基于 Rust 和 FFmpeg 的文件夹或播放列表播放。
* [Macadam](https://github.com/Streampunk/macadam) - 支持 HTML/CSS（通过 [Electron](https://www.electronjs.org/)）和 SVG（通过 [Sevruga](https://github.com/Streampunk/sevruga)）图形的 Blackmagic Node.js 绑定。
* [Nebula](https://github.com/nebulabroadcast) - 媒体资产管理和广播自动化系统。
* [NodeCG](https://www.nodecg.dev/) - 使用 Node.js 广播在浏览器中渲染的图形。
* [OGraf](https://github.com/ebu/ograf) - 基于 HTML 的图形的开放规范，用于直播电视和后期制作工作流程。
* [Open Playout Automation](https://github.com/jaskie/PlayoutAutomation) - 基于 CasparCG 的 MCR 播出系统。
* [ossia](https://ossia.io/) - 一个免费的开源媒体音序器。
* [Sofie - TV Automation](https://github.com/Sofie-Automation/Sofie-TV-automation) - 用于新闻广播的 MOS 驱动自动化系统，具有许多库，例如设备控制。
* [SPX - Graphics Controller](https://github.com/TuomoKu/SPX-GC) - 用于实时视频制作和直播的图形控制客户端。
* [StreamShapers - Ferryman](https://github.com/Streamshapers/StreamShapers-Ferryman) - 用于从 Lottie.JSON 文件/Adobe AfterEffects 生成 HTML 图形的 Web 应用程序。
* [Studio TV Player](https://github.com/jaskie/StudioTVPlayer) - 具有 SDI、NDI 和 MPEG TS 输出的简单电视演播室播放器。

## 时钟和工作室屏幕

* [OATIS](https://github.com/jamiehull/OATIS) - 基于服务器的工作室时钟和计数系统，支持消息传递、物理 GPI 和 OSC 触发。
* [OnAirScreen](https://github.com/saschaludwig/OnAirScreen) - 跨平台“OnAir Lamp”解决方案，专门用于专业广播环境。
* [PiClock](https://github.com/simonhyde/PiClock) - 基于可定制网络的时钟、直播、麦克风直播和其他演播室指示器显示。
* [PiClock Advanced](https://github.com/ael/piclock_advanced) - PiRSClock-Full 的改进版本，更改了布局，添加了计时器和网络功能。
* [PiRSClock-Full](https://github.com/jdgwarren/pirsclockfull) - 无线电演播室时钟，带有麦克风、电话等演播室指示器。

## 编解码器

* [FLAC](https://www.xiph.org/flac/) - 免费无损音频编码，被一些广播公司用于音频交换、存储。
* [Lame](https://lame.sourceforge.io/) - 高质量 MPEG 音频第三层 (MP3) 编码器。
* [opencore-amr](https://sourceforge.net/projects/opencore-amr/) - 从 Android 开源项目中提取的音频编解码器，包括 AAC。
* [Opus](https://www.opus-codec.org/) - 完全开放、免版税、高度通用的音频编解码器。
* [Turing Codec](https://github.com/bbc/turingcodec) - 一款 H.265/HEVC 开源软件编码器，专为快速高效的视频压缩而设计。
* [TwoLame](https://www.twolame.org/) - MPEG 音频第 2 层 (MP2) 编码器。

## 通讯

* [Intercom Manager](https://github.com/Eyevinn/intercom-manager) + [Intercom Frontend](https://github.com/Eyevinn/intercom-frontend) - 基于 Eyevinn 为 SVT 构建的对讲系统。
* [DYI intercom](https://github.com/matiaspl/intercom) - 围绕 Murmur 服务器和基于 Rasperry Pi 的无头 Mumble 客户端构建的硬件 + 软件对讲解决方案。

## 配套屏幕

* [dial-discovery-ios](https://github.com/bbc/dial-discovery-ios) - 用于在 iOS 平台上通过 DIAL 协议发现设备的库。
* [dvbcss-synckit-ios](https://github.com/bbc/dvbcss-synckit-ios) - 用于与电视帧精确同步的配套屏幕应用程序的 iOS 库。
* [dvbcss-synctiming](https://github.com/BBC/dvbcss-synctiming) - 一种用于测量电视或伴侣同步准确程度的系统。
* [pydvbcss](https://github.com/BBC/pydvbcss) - 实施 DVB Companion Screens 和 Streams 协议以实现同步媒体播放。

## 联网电视

* [CPA Authorization Provider](https://github.com/ebu/cpa-auth-provider) - 将媒体设备与在线身份链接的参考实现（[相关存储库](https://tech.ebu.ch/code) 此处）。
* [HbbPlayer](https://github.com/Samsung/HbbPlayer) - 符合 HbbTV 和 W3C 规范的应用程序，可以从 URL 播放媒体。
* [TAL](http://bbc.github.io/tal/) - 电视应用层 (TAL) 是一个开源库，用于构建联网电视设备的应用程序。

## 控制系统

* [BUG](https://bbc.github.io/bug/) - 广播通用网关 - 通过浏览器控制各种广播和网络设备。
* [Bitfocus Companion](https://github.com/bitfocus/companion) - 使 Elgato Streamdeck 和其他控制器成为[越来越多的广播设备](https://bitfocus.io/connections) 的 Shotbox 表面。
* [Lawo EmberPlus](https://github.com/Lawo/ember-plus) - Ember Plus - 用于与广播控制系统连接的开放协议。
* [MIDIMonster](https://github.com/cbdevnet/midimonster) - 用于常见显示控制协议的轻量级适配器工具。

## 分布式媒体处理

* [StormCV](https://github.com/sensorstorm/StormCV) - Apache Storm + OpenCV = 大规模分布式图像和视频分析。

## 文档

* [Kronekeeper](https://github.com/nick-prater/kronekeeper) - 一个基于网络的应用程序，用于记录和管理 Krone 框架记录。

## 数字视频广播和无线网络

* [DTT 2 IP](https://github.com/ebu/dtt2ip) - Wifi 室内覆盖的广播到 IP 转换。
* [DVB Inspector](https://sourceforge.net/projects/dvbinspector/) - 开源 DVB 分析器。
* [DVBlast](https://www.videolan.org/projects/dvblast.html) - 一个简单而强大的 MPEG-2/TS 解复用和流媒体应用程序。
* [dvbshout](https://github.com/njh/dvbshout) - 用于将 DVB 音频发送到shoutcast 服务器或RTP 流的工具。
* [Opencaster](https://github.com/aventuri/opencaster) - 免费开源 MPEG2 传输流数据生成器和数据包操纵器。
* [Project X](https://sourceforge.net/projects/project-x/) - DVB 解复用工具。
* [ts2mpa](https://github.com/njh/ts2mpa) - 从 MPEG 传输流 (TS) 中提取 MPEG 音频的简单工具。
* [TSDuck](https://tsduck.github.io/) - 用于 MPEG/DVB 传输流测试、监控、集成、调试等的可扩展工具包。
* [WiFiBroadcast](https://befinitiv.wordpress.com/wifibroadcast-analog-like-transmission-of-live-video-data/) - 实时视频数据的模拟传输。

## 混合无线电

* [RadioDNS for Node.js](https://github.com/bbc/node-radiodns) - 在 Node.js 中执行 RadioDNS 解析和服务查找。
* [RadioDNS Manager](https://github.com/ebu/radiodns-manager) - 管理混合无线电服务的平台，例如RadioVIS、RadioEPG 和服务跟踪。
* [RadioTag.js](https://github.com/ebu/radiotag.js) - JavaScript 中的 RadioTag 客户端库。
* [RadioVIS Demo](https://github.com/bbc/RadioVisDemo) - Python 中的 RadioVIS 客户端应用程序。
* [RadioVIS Html Player](https://github.com/ebu/radiovis-html5player) - 使用 WebSocket 的 RadioVIS 播放器。
* [RadioVIS Stomp Server](https://github.com/bbc/node-radiovis-stomp-server) - 用 Node.js 编写的 RadioVIS STOMP 服务器。

## 实时IP
*IP 音频/视频和流媒体*

* [butt](https://danielnoethen.de/) - 使用此工具（butt）进行广播是一个易于使用的多操作系统流媒体工具。它支持 SHOUTcast 和 Icecast。
* [Cool Mic](https://coolmic.net/) - Android 音频直播 Icecast 源客户端应用程序。
* [DarkIce](http://www.darkice.org/) - 实时音频流媒体，从音频接口进行记录和编码，然后发送到流媒体服务器。
* [EBU LIST](https://github.com/ebu/pi-list) - Live IP 软件工具包可协助 EBU 成员实施基于 IP 的设施。
* [Icecast](https://icecast.org/) - 支持Ogg（Vorbis和Theora）、Opus、WebM和MP3的流媒体（音频/视频）服务器。
* [IRIS Broadcast](https://github.com/IrisBroadcast/irisbroadcast.github.io/) - 一个在瑞典成立的项目，旨在发布用于专业无线电广播的开源软件。
* [Kamailio](http://www.kamailio.org/) - 开放 SIP 服务器，通常用于使用 SIP (EBU ACIP) 通过 IP 进行音频贡献。
* 请参阅 [NMOS](#nmos) 列表，了解 AMWA 网络媒体开放规范以及开源实现和工具。
* [OpenOB](https://jamesharrison.github.io/openob/) - 开放外部广播项目，用于基于 Opus 的无线电贡献链接和演播室发射器链接。
* [PJSIP](https://www.pjsip.org/) - 实现 SIP、SDP、RTP、STUN、TURN 和 ICE 的开源多媒体库。
* [trx](https://www.pogo.org.uk/~mark/trx/) - 用于从 Linux 广播实时音频的简单工具集。
* [VideoIPath-Automation-Tool](https://github.com/SWR-MoIP/VideoIPath-Automation-Tool) - 用于自动化 VideoIPath 配置工作流程的 Python 包。

## 媒体播放器

* [Dash.js](https://github.com/ebu/dash.js) - 用于通过 Javascript 和兼容浏览器播放 MPEG DASH 的参考客户端实现。
* [GPAC](https://gpac.io/) - 多媒体播放器、打包器和工具。
* [IDJC](https://idjc.sourceforge.io/) - 带有两个主要媒体播放器的 GTK+ Shoutcast/Icecast 客户端。
* [Kodi](https://github.com/xbmc/xbmc) - 数字媒体软件媒体播放器和娱乐中心。
* [Media4DPlayer](https://github.com/ebu/media4Dplayer) - HTML5 播放器注重可访问性。
* [MPD](https://www.musicpd.org/) - 一个灵活、强大的服务器端应用程序，用于播放音乐。
* [mpg123](https://www.mpg123.de/) - 快速控制台 MPEG 音频播放器和解码器库。
* [Mixxx](https://mixxx.org/) - 一款免费、开源的 DJ 软件。
* [Peaks.js](https://codeberg.org/chrisn/peaks.js) - 基于浏览器的音频波形可视化。
* [rx-player](https://github.com/canalplus/rx-player) - 支持 MPEG-DASH 和 SmoothStreaming 的 HTML5/Javascript 视频播放器。
* [VLC](https://www.vlc.org) - 简单、快速且功能强大的媒体播放器。

## 元数据

* [BMXlib](https://github.com/ebu/bmx) - 用于读取和写入广播媒体文件的库和实用程序。主要支持MXF文件格式。
* [EBUCore](https://github.com/ebu/ebucore) - 用于维护 [EBUCore 架构](https://tech.ebu.ch/docs/tech/tech3293.pdf) 的 Github。
* [jebu-core](https://github.com/mikrosimage/jebu-core) - [EBU Tech 3293](https://tech.ebu.ch/publications/tech3293) EBU 核心元数据的 Java 端口，包括[音频定义模型](https://tech.ebu.ch/publications/tech3364)。
* [libadm](https://github.com/ebu/libadm) - 处理 C++11 库的音频定义模型 (ITU-R BS.2076)。
* [libklvanc](https://github.com/stoth68000/libklvanc) - 用于从 SDI 和 SMPTE ST 2110-40（CEA-708、AFD、SCTE-104 等）提取辅助数据的 C 库。
* [MAJ API](https://github.com/AMWA-TV/maj) - 用于读写 MXF 和 AAF 文件的纯 Java 库。
* [SDPoker](https://github.com/AMWA-TV/sdpoker) - 用于测试 SMPTE ST2110 SDP 文件的 CLI 工具和库。
* [TV-Anytime](https://github.com/ebu/tvanytime) - TV-Anytime 模式 github 维护页面。

## 监控和质量控制

* [a_Multiview](https://github.com/Bencosterton/a_MultiView) - 基于 Web 的 HLS 和 Youtube 链接多视图。
* [BeaqleJS](https://github.com/HSU-ANT/beaqlejs) - 用于创建基于浏览器的听力测试以进行主观音频质量评估的框架。
* [Jack Meter](https://github.com/njh/jackmeter) - JACK 基于文本控制台的 DPM（数字峰值表）。
* [Jmeters](http://kokkinizita.linuxaudio.org/linuxaudio/downloads/index.html) - JACK 的图形音频表集合，包括 VU、PPM 和 [EBU R 128](https://tech.ebu.ch/publications/r128) 响度表。
* [LTC-tools](https://github.com/x42/ltc-tools) - 用于处理线性时间码 (LTC) 和转换为 MIDI 时间码 (MTC) 的工具集合。
* [MediaConch](https://mediaarea.net/MediaConch) - Matroska、FFV1 和 PCM 的实施检查员、政策检查员和报告员。
* [MediaInfo](https://mediaarea.net/en/MediaInfo) - 方便地统一显示视频和音频文件最相关的技术和标签数据。
* [MXF Inspect](https://github.com/Myriadbits/MXFInspect) - 一个 Windows 工具，用于显示 MXF（材料交换格式）文件的内部结构。
* [Pi Audio Monitor](https://github.com/martim01/pam) - 适用于 Raspberry Pi 的音频监控，支持 S/PDIF、AES3、AES67、Livewire 和 Ravenna。
* [Photon](https://github.com/Netflix/photon) - 实施 SMPTE 互操作主格式 (IMF) 标准。
* [QCTools](https://github.com/bavc/qctools) - 用于视频保存的质量控制工具，用于分析数字化视频文件。
* [Rotter](https://github.com/njh/rotter) - JACK 的传输记录/音频记录器。
* [silan](https://github.com/x42/silan) - 音频文件静音分析器。
* [SilentJack](https://github.com/njh/silentjack) - JACK 的死气/静音探测器。
* [Sonic Visualiser](https://www.sonicvisualiser.org/) - 用于查看和分析音乐音频文件内容的应用程序。
* [VMAF](https://github.com/Netflix/vmaf) - 基于多方法融合的感知视频质量评估
* [Wisual](https://github.com/MarcAntoine-Arnaud/wisual) - 视觉质量评估的Web服务，支持PSNR、SSIM、VQM等。

## 多媒体内容处理

* [AvTranscoder](https://github.com/avTranscoder/avTranscoder) - 基于 FFmpeg/LibAV 的高级 API，用于重新包装或转码媒体，并具有 Java 和 Python 的绑定。
* [Beam Coder](https://github.com/Streampunk/beamcoder) - Node.js 与 FFmpeg 的本机绑定，支持通过 Promise 和流进行异步处理。
* [Bento4](https://github.com/axiomatic-systems/Bento4) - 全功能的 MP4 格式和 MPEG DASH C++ 类库和工具。
* [Brave](https://github.com/bbc/brave) - 基本实时 AV 编辑器 - 允许您在云端预览、混合和路由实时音频和视频流。
* [Codem-isoboxer](https://github.com/Dash-Industry-Forum/codem-isoboxer) 一个基于浏览器的小型 MPEG-4 (ISOBMFF) 解析器。
* [Dynamorse](https://github.com/Streampunk/node-red-contrib-dynamorse-core) - IT瑞士军刀——Node-RED媒体管道构建器，添加专业媒体处理节点。
* [EBU ADM Renderer](https://github.com/ebu/ebu_adm_renderer) - EBU ADM 渲染器的参考实现（[EBU Tech 3388](https://tech.ebu.ch/publications/tech3388)）
* [FFmbc](https://github.com/bcoudurier/FFmbc) - FFmpeg 专为广播和专业用途而定制。
* [FFmpeg](https://ffmpeg.org) - 用于录制、转换和流式传输音频和视频的跨平台解决方案。支持 SMPTE ST 2110。
* [Flowblade](https://github.com/jliljebl/flowblade) - 多轨非线性视频编辑器。
* [GStreamer](https://gstreamer.freedesktop.org/) - 用于构建媒体处理组件图的库。
* [Kelvinadon](https://github.com/Streampunk/kelvinadon) - Node.JS 纯 Javascript 模块，用于将 MXF 文件与 JSON 进行流式传输。
* [KFR](https://www.kfrlib.com/) - 快速、现代的 C++ DSP 框架、DFT/FFT、音频重采样、FIR/IIR、Biquad、EBU R 128。
* [L-SMASH](https://github.com/l-smash/l-smash/) - 严格符合规范的 ISOBMFF 库，具有完整的 DASH 复用支持。
* [LibAV](https://github.com/libav/libav) - 开源音频和视频处理工具。
* [libbw64](https://github.com/ebu/libbw64) - 仅标头广播 Wave 64 (ITU-R BS.2088) C++11 库。
* [libear](https://github.com/ebu/libear) - 一个 C++11 库，用于根据 ITU-R BS.2127 建议书呈现 ADM 内容。
* [Libebur128](https://github.com/jiixyj/libebur128) - 实现 EBU R 128 响度标准化标准的库。
* [Loudness Validator](https://github.com/mikrosimage/loudness_validator) - 一组用于分析、可视化和校正响度的应用程序。
* [MP4Box.js](https://github.com/gpac/mp4box.js) - 用于在浏览器（和 NodeJS）中处理 MP4 文件的 JavaScript 库。
* [MXFLib](https://sourceforge.net/projects/mxflib/) - 用于读写 MXF 文件的多平台 C++ 库。
* [OBS-Studio](https://github.com/obsproject/obs-studio) - 用于直播和屏幕录制的软件。
* [Open Broadcast Encoder](https://github.com/ob-encoder) - 由开源组件构建的广播编码器。
* [rgain3](https://github.com/chaudum/rgain3) - 用于读取、写入和计算重播增益的工具和 Python3 库 - Felix Krull 的原始版本的分支。
* [rtmp](https://github.com/c-bata/rtmp) - Adobe RTMP 1.0 协议在 Go 中的服务器实现。
* [Snowmix](https://sourceforge.net/projects/snowmix/) - 现场视频混合器。
* [SoX](https://sourceforge.net/projects/sox/) - 声音处理程序的瑞士军刀。
* [SVT Encore](https://github.com/svt/encore) - 自托管视频转码平台，围绕 FFmpeg 构建。
* [TuttleOFX](https://github.com/tuttleofx/TuttleOFX) - 一个基于OpenFX插件标准的开源图像处理框架。
* [UPipe](https://github.com/cmassiot/upipe/) - 主要设计为多媒体播放器、转码器或流媒体的核心。
* [VideoContext](https://github.com/bbc/videocontext) - 用于创建交互式和响应式网络视频的实验性 HTML5/WebGL 库。
* [Voctomix](https://github.com/voc/voctomix) - 基于Python和GStreamer的可定制会议录音/混音/流媒体软件。

## 网络和存储测试

* [BBC Media Storage Meter](https://sourceforge.net/projects/msmeter/) - 用于测试网络附加（专业媒体）存储的应用程序。
* [Fio](https://github.com/axboe/fio) - 灵活的I/O测试仪
* [iPerf3](https://iperf.fr/) - TCP、UDP 和 SCTP 网络带宽测量工具。
* [SMPTE 2110-20 Analyzer](https://github.com/ebu/smpte2110-analyzer) - 分析器用于检查根据 SMPTE ST 2110 生成的网络数据包。
* [Wireshark dissector for TSL UMD protocol V3.1, V4](https://github.com/roddypratt/tslumd-wireshark) - 适用于 TSL UMD（监视器下显示）协议 V3.1 和 V4 的分析仪。
* [Wireshark dissectors for Video Routers](https://github.com/roddypratt/router_dissectors) - 适用于各种视频路由器/矩阵协议的分​​析仪。
* [SMPTE ST 2110 pcap 文件示例](https://github.com/NEOAdvancedTechnology/ST2110_pcap_zoo)

## NMOS

[网络媒体开放规范](https://specs.amwa.tv/nmos/) 本身是开源的。

* [AMWA NMOS Testing Tool](https://specs.amwa.tv/nmos-testing/) - 适用于 AMWA NMOS 系列规格的自动化测试套件，如 [JT-NM 测试](https://www.jt-nm.org/jt-nm-tested) 计划中所使用
* [BBC NMOS Joint Reference Implementation](https://github.com/bbc/nmos-joint-ri) - 用于构建 4 个虚拟机、IS-04/IS-05 节点、IS-04 注册表、BCP-003-02 授权服务器和 NMOS 测试工具的 Vagrant 配置。
* [DELTACAST IP Virtual Card NMOS samples](https://github.com/deltacasttv/nmos-ipvc-samples) - 通过 [nmos-cpp](https://github.com/sony/nmos-cpp) 演示多个 NMOS 标准与 DELTACAST IP 虚拟卡的集成。
* [Easy-NMOS](https://github.com/rhastie/easy-nmos) - 入门套件允许用户以最少的安装步骤启动简单的 NMOS 设置，由三个 Docker 容器组成：NMOS 注册表、虚拟 NMOS 节点和 AMWA NMOS 测试工具。
* [nmos-cpp](https://github.com/sony/nmos-cpp) - AMWA 网络媒体开放规范的 C++ 实现，包括 NMOS 注册表和工具包以及构建 NMOS 节点的示例。
* [nmos-device-control-mock](https://github.com/AMWA-TV/nmos-device-control-mock) - NMOS 控制和监控套件（IS-12、BCP-008-01、BCP-008-02）的模拟设备实现，用 Typescript 编写并在 NodeJS 堆栈上运行。
* [nmos-js](https://github.com/sony/nmos-js) - 一个简单的基于浏览器的 NMOS 客户端/控制器，带有 IS-04 注册表浏览器和 IS-05 连接管理。
* [NVIDIA NMOS Docker](https://hub.docker.com/r/rhastie/nmos-cpp) - 具有注册表和控制器的 Docker 容器，IS-04/05/08/07/09，BCP-003-01
* [NVIDIA NMOS 库](https://github.com/NVIDIA/nvnmos) (NvNmos) - 一个简单易用的 C/C++ 库，用于向您的应用程序添加 NMOS 节点，支持 IS-04、IS-05、BCP-002-01、BCP-002-02、BCP-004-01 等。

## 播客

* [AntennaPod](https://github.com/AntennaPod/AntennaPod) - 适用于 Android 的播客管理器 ([antennapod.org](https://antennapod.org/))。
* [Anytime Podcast Player](https://github.com/amugofjava/anytime_podcast_player) - 适用于 Android 和 iOS 的免费且易于使用的播客播放器 ([anytimeplayer.app](https://anytimeplayer.app/))。
* [Castopod](https://github.com/ad-aures/castopod) - 播客托管和广播 ([castopod.org](https://castopod.org/))。
* [gPodder](https://gpodder.github.io/) - 媒体聚合器和播客客户端。
* [Podlove Publisher](https://github.com/podlove/podlove-publisher) - WordPress 的播客发布商。
* [Podlove Web Player](https://github.com/podlove/podlove-ui) - 经播客优化、基于 HTML5 的视频和音频播放器。
* [Ultraschall](https://github.com/Ultraschall) - 插件套件和 UI 调整可与 DAW [Reaper](https://www.reaper.fm/) 一起使用，专为播客 ([ultraschall.fm](https://ultraschall.fm/)) 定制

## 广播制作

* [Airtime](https://github.com/sourcefabric/airtime) - 用于远程广播自动化的无线电管理应用程序（通过基于网络的时间表）。
* [Ardour](https://ardour.org/) - 数字音频工作站。
* [Audacity](https://www.audacityteam.org/) - 用于录制和编辑声音的跨平台软件。
* [AzuraCast](https://github.com/AzuraCast/AzuraCast) - 自托管网络无线电管理套件。
* [LibreTime](https://libretime.org/) - 无线电广播和自动化平台（Airtime 的分支）。
* [Liquidsoap](https://github.com/savonet/liquidsoap) - 用于多媒体流媒体的瑞士军刀（[文档](https://www.liquidsoap.info/doc.html)）。
* [OpenBroadcaster](https://www.openbroadcaster.com/) 开源 LPFM IPTV 广播自动化。 [此处的服务器和播放器代码](https://github.com/openbroadcaster)。
* [RAAR](https://github.com/radiorabe/raar) - 用于管理和浏览音频存档的 ruby​​ 应用程序。
* [Rivendell](https://github.com/ElvishArtisan/rivendell) - 完整的无线电广播自动化解决方案，已翻译成多种语言并在全球范围内使用。

## 清单自动化

* [OnTime](https://github.com/cpvalente/ontime) - 基于网络的实时事件计时系统，具有广播时钟视图。
* [SuperConductor](https://github.com/SuperFlyTV/SuperConductor) - CasparCG 服务器、BMD ATEM、OBS Studio、vMix、OSC 兼容设备、HTTP (REST) 兼容设备等的运行/播放控制器。

## SCTE-35 和 SCTE-104

* [threefive](https://github.com/superkabuki/threefive_is_scte35) - SCTE-35 MPEGTS 解析器和编码器。
* [wireshark-scte](https://github.com/m1tk4/wireshark-scte) - Wireshark 的 SCTE-104 协议解析器。
* [x9k3](https://github.com/superkabuki/x9k3) - 自适应比特率 HLS 分段器和 SCTE-35 注入器。

## 软件无线电

* [GNU Radio](https://www.gnuradio.org/) - 一种软件开发工具包，提供信号处理模块来实现软件无线电。
* [Gqrx SDR](https://www.gqrx.dk/) - 开源软件定义的无线电接收器 (SDR)。
* [ODR-mmbTools](https://www.opendigitalradio.org) - CRC-mmbTools 的分支。添加实时、DAB+、关联数据、分布式基础设施、SFN。
* [rtl-sdr](https://osmocom.org/projects/rtl-sdr/wiki/rtl-sdr) - 将基于 Realtek RTL2832 的 DVB 加密狗转变为 SDR 接收器。
* [welle.io](https://www.welle.io/) - 开源 DAB 和 DAB+ 软件定义无线电 (SDR)，支持 Airspy 和 rtlsdr。

## 流媒体

* [Owncast](https://github.com/owncast/owncast) - 自托管视频流平台（https://owncast.online/）
* [PeerTube](https://github.com/Chocobozzz/PeerTube) - ActivityPub 联合视频流平台直接在您的网络浏览器中使用 P2P。 （https://joinpeertube.org/）

## 字幕制作

* [CCExtractor](https://ccextractor.sourceforge.net/about-ccextractor.html) - 一种分析视频文件并生成独立字幕文件的工具。
* [EBU-TT-D Subtitling within dash.js](https://github.com/ebu/dash.js/tree/ebu-subtitling-dev) - dash.js 分叉，在 HTML/CSS 叠加中带有 EBU-TT-D 字幕。后来添加到[dash.js](https://github.com/ebu/dash.js)。
* [EBU-TT-D W3C XML Schema](https://github.com/ebu/ebu-tt-d-xsd/) - 信息丰富的 EBU-TT-D XML 架构，支持 EBU Tech 3380 的实施。
* [EBU-TT Live Interoperability Toolkit](https://github.com/ebu/ebu-tt-live-toolkit) - 用于生成、测试和分发 [EBU-TT Live](https://tech.ebu.ch/publications/tech3370) 字幕的组件。
* [GStreamer TTML subtitling package](https://github.com/BBC-archive/gst-ttml-subtitles) - GStreamer 管道解析和渲染 EBU-TT-D (TTML) 字幕的一种方法。
* [imscJS](https://github.com/sandflow/imscJS) - 用于将 IMSC1 文本和图像配置文件呈现为 HTML5 的 JavaScript 库。
* [IRT EBU-TT-D Application Samples](https://github.com/IRT-Open-Source/irt-ebu-tt-d-application-samples) - EBU-TT-D 示例文件、PNG 图像和 mp4 视频作为渲染参考。
* [Subtitle Edit](https://www.nikse.dk/SubtitleEdit) - 字幕编辑器。
* [Subtitling Conversion Framework (SCF)](https://github.com/Irt-Open-Source/scf) - 用于转换字幕格式的模块，包括。 EBU STL 和 EBU-TT 文件。
* [Timed Text Toolkit (ttt)](https://github.com/skynav/ttt) - 支持/使用 W3C 定时文本标记语言 (TTML) 的工具。
* [ttconv](https://github.com/sandflow/ttconv) - 字幕转换库和 CLI 工具。在 STL、SRT、TTML、SCC、TTML 和 WebVTT 文件之间进行转换。

## 视频制作

* [ATEM Tally Light with ESP8266](https://github.com/AronHetLam/ATEM_tally_light_with_ESP8266) - 使用 ESP8266 WiFi 模块的 ATEM 切换台无线计数灯，支持无限计数单位。
* [AutoMix](https://github.com/InsanityRadio/automix/) - 基于网络的 ATEM 视觉混合器控制界面，具有自动摄像机切换功能，专为可视化广播而设计。
* [MOS-connection](https://github.com/Sofie-Automation/sofie-mos-connection) - 用于作为 MOS 设备或 NRCS 进行连接和 MOS 消息传递的 JavaScript 库。
* [obs-shotlister](https://github.com/michalramus/obs-shotlister) - 用于现场制作的摄像机镜头队列管理器，具有 OBS Studio 集成、LAN Web 监控和 OSC 支持。
* [Open Lighting Architecture (OLA)](https://www.openlighting.org/ola/) - 用于照明行业的旅行适配器，用于互连 DMX-512、IP 和 USB。
* [Q Light Controller+ (QLC+)](https://www.qlcplus.org/) - DMX 或模拟照明系统（灯头、调光器等）的跨平台控制。
* [QPrompt Teleprompter App](https://qprompt.app) - 融合提词器软件，可与工作室提词器、平板电脑提词器、网络摄像头和手机配合使用。
* [TallyArbiter](https://tallyarbiter.com/) - 通过手机或低成本硬件为任何相机提供跨平台 Tally 接口和 Tally 灯。
* [TallyLights](https://github.com/michalramus/TallyLights) - 支持 TSL 3.1 和 5.0 协议的 DIY 提示灯，围绕 WeMos D1 Mini 微控制器构建。
* [vMix-EmberPlus](https://github.com/mattlamb99/vMix-EmberPlus) - vMix 到 EmberPlus 网关。从任何 EmberPlus 广播控制器（例如 Lawo 的 VSM 或 EVS 的 Cerebrum）控制 vMix。
* [wifi-tally](https://github.com/wifi-tally/wifi-tally) - 基于 NodeMCU/ESP8266 的经济实惠的支持 WiFi 的 Tally 灯系统，支持多个视频混合器。

# 资源
用于提高您的技能和知识的各种资源，例如书籍、网站和文章。

## 博客

* [BBC News Labs](https://github.com/BBC-News-Labs) - BBC 新闻实验室的开源项目。
* [BBC R&D](https://www.bbc.co.uk/rd) - BBC 研究与发展。查看每周笔记。
* [3D CineCast](http://3dcinecast.blogspot.com/) - 关于新媒体技术的策展。
* [Canal+](https://developers.canal-plus.com/) - CANAL+ 开源社区。
* [IRT Lab](https://web.archive.org/web/20210830075332/https://lab.irt.de/) - IRT 博客发布所有数字视听媒体技术的开发和演示。
* [The Netflix Tech Blog](https://netflixtechblog.com/) - Netflix 博客，专注于技术和技术问题。

## 网站

# 贡献
有关详细信息，请参阅[贡献](https://github.com/ebu/awesome-broadcasting/blob/master/CONTRIBUTING.md)。
