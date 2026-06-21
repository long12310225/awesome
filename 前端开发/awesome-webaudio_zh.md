# 很棒的网络音频

[![Awesome](https://awesome.re/badge.svg)](https://github.com/sindresorhus/awesome#readme)

<img src="https://raw.githubusercontent.com/voodootikigod/logo.js/master/webaudio/webaudio-js.png" width="200px" alt="WebAudio">

> 精彩的 [WebAudio](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API) [packages](#packages) 和 [demos](#demos) 精选列表。

受到 [awesome](https://github.com/sindresorhus/awesome) 列表的启发。

请提出 [Pull-Request](https://github.com/notthetup/awesome-webaudio/pulls) 将一个很棒的 WebAudio 东西添加到此列表中。

## 内容

- [Packages](#packages)
  - [Frameworks](#frameworks)
  - [Libraries](#libraries)
  - [Utilities](#utilities)
  - [MIDI](#midi)
  - [Apps](#apps)
- [Resources](#resources)
  - [Tutorials](#tutorials)
  - [Books](#books)
  - [Newsletters](#newsletters)
  - [Community](#community)
- [Obsolete](#obsolete)

## 套餐

### 框架

- [Tone.js](https://github.com/Tonejs/Tone.js) - 用于在浏览器中制作交互式音乐的框架。
- [Bap](https://github.com/adamrenklint/bap) - 用于制作节拍和创作序列的工具包，灵感来自经典的 MPC60/2000。
- [Omnitone](https://github.com/GoogleChrome/omnitone) - 网络上的 Ambisonic 空间音频。
- [Mach1Spatial](https://github.com/Mach1Studios/m1-sdk) - 网络上基于矢量的平移空间音频。
- [Elementary](https://www.elementary.audio/) - 用于在网络上或本机应用程序上编写音频软件的声明式功能框架
- [React Native Audio API](https://github.com/software-mansion-labs/react-native-audio-api) - 基于react-native的原生应用程序的Web Audio API实现。

### 图书馆

- [smoothfade](https://github.com/notthetup/smoothfade) - 用于在两个 AudioNode 之间平滑淡入淡出的库。
- [virtual-audio-graph](https://github.com/benji6/virtual-audio-graph) - 用于以声明方式操作 Web 音频 API 的库。
- [XSound.js](https://xsound.app/) - 全栈库。
- [Sound.js](https://github.com/kittykatattack/sound.js) - 一个微型库，用于加载、播放和生成游戏和交互式应用程序的音效和音乐。
- [Meyda](https://github.com/meyda/meyda) - 音频特征提取库包括多种广泛使用的音频特征。
- [Wavesurfer.js](https://github.com/katspaugh/wavesurfer.js) - 使用 Web Audio 和 Canvas 进行交互式可导航音频可视化。
- [Audiojs](https://github.com/audiojs/audio) - 使您能够更轻松地存储、读取和写入 PCM 音频数据的对象。
- [Tuna](https://github.com/Theodeus/tuna) - 音频效果库。
- [Rythm.js](https://okazari.github.io/Rythm.js/) - 一个让你的页面跳舞的 JavaScript 库。
- [Howler.js](https://github.com/goldfire/howler.js) - 一个全面的库，可回退到 HTML5 音频。
- [Circular Audio Wave](https://github.com/kelvinau/circular-audio-wave) - 一个使用 Web Audio API 和 ECharts 进行圆形波音频可视化的 JS 库。
- [Wad](https://github.com/rserota/wad) - 网络音频 DAW。使用 Web Audio API 进行动态声音合成。这就像你耳朵里的 jQuery。
- [p5.sound](https://p5js.org/reference/#/libraries/p5.sound) - 将网络音频功能添加到创意编码库 [p5.js](https://p5js.org/) 的扩展。
- [@magenta/music](https://github.com/magenta/magenta-js/tree/master/music) - 一个 JavaScript 库，通过对 Webaudio API 进行一些简洁的抽象，使用机器学习模型并在浏览器中生成音乐。
- [soundfont-player](https://www.npmjs.com/package/soundfont-player) - 声音字体加载器/播放器，使用 WebAudio API 播放 MIDI 声音。
- [html-midi-player](https://github.com/cifkao/html-midi-player) - HTML 元素可轻松实现 MIDI 播放和可视化，无需编写任何自定义 JS 代码，但可根据需要编写脚本和设置样式。
- [MusicXML Player](https://github.com/infojunkie/musicxml-player) - 一个 TypeScript 组件，使用 Web 音频和 Web MIDI 在浏览器中加载和播放 MusicXML 文件。
- [waveform-path](https://github.com/jerosoler/waveform-path) - 用于生成 svg 波形路径的库。
- [wave-audio-path-player](https://github.com/jerosoler/wave-audio-path-player) - 可使用波形自定义的简单音频播放器 Web 组件。
- [dsssp](https://github.com/NumberOneBot/dsssp) - React 组件库，用于可视化和管理音频过滤器，并支持拖放和转换。
- [tuning-fork](https://github.com/v-rusu/tuning-fork) - 一个可配置的客户端 JavaScript 库，用于通过实时音高检测进行吉他调音。

### 公用事业

- [Audion](https://github.com/google/audion) - Chrome 扩展程序将网络音频面板添加到开发人员工具中。
- [web-audio-generator](https://github.com/ISNIT0/webaudio-generator) - 用于生成网络音频代码的 UI。
- [Web Audio Studio](https://app.webaudio.studio) - 从代码生成的 Web 音频 API 图表的实时可视化工具。

### MIDI

- [midimessage](https://github.com/notthetup/midimessage) - 一个简单的 MIDI 消息解析器。
- [JZZ](https://github.com/jazz-soft/JZZ) - 适用于 Node.js 和所有主要浏览器的 MIDI 库。
- [JZZ-midi-Gear](https://github.com/jazz-soft/JZZ-midi-Gear) - 检索您的 MIDI 设备型号和制造商。
- [WEBMIDI.js](https://webmidijs.org/) - Web MIDI API 让一切变得简单。

### 应用程序

- [BassoonTracker](https://github.com/steffest/BassoonTracker) - Javascript 中的 MOD/XM 跟踪器。
- [LoopDrop App](https://github.com/mmckegg/loop-drop-app) - 使用 Web Audio 和 Web MIDI API 构建的 MIDI Looper、模块化合成器和采样器应用程序。
- [X Sound](https://xsound.app/) - 使用 XSound.js 的多声音应用程序。
- [Molgav](https://github.com/surikov/molgav) - 用于旋律交换的音乐步进音序器。
- [mod-synth.io](https://github.com/andrevenancio/mod-synth.io) - 创建您自己的模块化合成器，或模拟不同的合成器。
- [GridSound](https://gridsound.github.io) - 正在进行中的 DAW（数字音频工作站）。
- [Learning Music](https://learningmusic.ableton.com/) - 了解音乐制作的基础知识。
- [Super Oscillator](https://github.com/lukehorvat/super-oscillator) - 用于网络的交互式 3D 音乐合成器。
- [AudioNodes](https://audionodes.com) - 模块化音频制作套件，具有多轨音频混合、音频效果、参数自动化、MIDI 编辑、合成、云制作等功能。
- [waveform-playlist](https://github.com/naomiaro/waveform-playlist) - 具有画布波形预览的多轨网络音频编辑器和播放器。设置提示、淡入淡出并及时切换多个轨道。录制音轨或提供音频注释。将您的混音导出到 AudioBuffer 或 WAV！项目灵感来自 Audacity。
- [SoundCycle](https://github.com/scriptify/soundcycle) - 一个基于网络音频的 Loopstation，为音乐家提供效果和不同的循环模式。
- [DSP.audio Worklet Editor](https://dsp.audio/editor/) - 用于绘制草图和协作的在线音频工作集编辑器，带有采样器、MIDI 和分析器。类似于 JSFiddle，但用于 DSP。
- [AudioMass](https://audiomass.co/) - 免费、开源、基于网络的音频和波形编辑器。
- [Csound IDE](https://ide.csound.com/) - [CSound 编程语言](https://en.wikipedia.org/wiki/Csound) 的 Web IDE。
- [jamhub](https://github.com/fletcherist/jamhub) - 低延迟远程音乐协作和即兴演奏。
- [Web Audio Metronome](https://github.com/cwilso/metronome) - 使用 Web Audio 调度程序和 setTimeout 调度程序的节拍器应用程序
- [EarSketch](https://earsketch.gatech.edu/landing/#/) - 免费的教育编程环境，通过音乐创作和混音来教授 Python 和 Javascript
- [webaudio-tinysynth](https://github.com/g200kg/webaudio-tinysynth) - 一个用 JavaScript 编写的小型合成器，带有类似于音色图的 GM。
- [web-audio-beat-detector](https://github.com/meerasndr/sample-golang-app) - 使用 Web Audio API 的节拍检测实用程序
- [web-audio-mixer](https://github.com/jamesfiltness/web-audio-mixer) - 使用 Web Audio 构建的音频混合器。
- [Audio-motion interface](https://github.com/MaxAlyokhin/audio-motion-interface) - 一种网络合成器，可使用空间中的智能手机手势生成声音。
- [Topos](https://topos.raphaelforment.fr) - 受 Monome Teletype 启发的基于 Web 的实时编码环境。使用网络音频和 MIDI。
- [Online Sequencer](https://onlinesequencer.net) - 一个简单易用的音序器，具有丰富的功能，基于 Web Audio API。
- [Binary Synth](https://github.com/MaxAlyokhin/binary-synth) - 一个网络合成器，可以从任何文件的二进制代码生成声音。
- [dsssp-demo](https://github.com/NumberOneBot/dsssp-demo) - WebAudio 音乐播放器，具有 7 频段均衡器和滤波器预设。
- [SingMeter](https://www.singmeter.com/) - 基于浏览器的歌唱工具集合，包括音高检测器和音域测试。
- [Drumhaus](https://drumha.us/) - 基于浏览器的鼓机，具有步进排序、模式变化和律动编辑功能。
- [All-in-One Advanced BPM Tool](https://tapbpmhub.com/) - 通过点击或使用空格键立即测量歌曲速度。具有 MIDI 输入、可选的声音点击和实时 BPM 可视化。对于制作人、DJ、节奏游戏玩家来说必不可少。
- [synflow](https://synflow.org) [Github](https://github.com/k1ln/synflow) - 基于浏览器的模块化合成流引擎。具有所有 Web 音频 API 节点以及更多 Worklet（如声码器、混响等）。具有先进的流程自动化。
- [Tonalux](https://tonalux.org) - 基于浏览器的免费音频分析套件，具有实时频谱分析仪、LUFS 响度测量 (EBU R128)、A/B 参考比较和立体声相关性。使用 Web Audio API 和 WebAssembly 构建，完全在客户端运行。
- [mdrone](https://mdrone.org) - 在浏览器中运行的微音调无人机乐器。

## 资源

### 教程

- [WebAudio School](https://github.com/mmckegg/web-audio-school) - 一系列学习 WebAudio 的自学研讨会。
- [Web Audio API Understandable Reference](https://web-audio-api.firebaseapp.com/) - 该参考旨在让了解一些 JavaScript 和基本音频原理的人易于理解。
- [The Web Audio API: What Is It?](https://code.tutsplus.com/tutorials/the-web-audio-api-what-is-it--cms-23735) - WebAudio 简介。
- [Web Audio Basics](https://github.com/kylestetz/Web-Audio-Basics) - 越来越多的轻量级代码示例，每个示例都带有 CodePen 链接。
- [Web Audio Perf](https://padenot.github.io/web-audio-perf/) - 各种 AudioNode 的性能和有效资源利用的策略（来自 WAC2016）。
- [Percussion Synthesis Using Web Audio](https://github.com/irritant/WAC-2016-Tutorial) - 本教程将通过编写代码来合成简单的打击乐声音（来自 WAC2016）来介绍网络音频编程的基础知识。
- [Browser Noise: Web Audio Tutorials](https://www.youtube.com/playlist?list=PLLgJJsrdwhPywJe2TmMzYNKHdIZ3PASbr) - Dan Tramte 的视频教程播放列表，托管在 Audio Programmer YouTube 频道上。
- [audio-katas](https://github.com/survivejs/audio-katas) - 一系列自导式 katas，在此期间您将构建自己的 DAW，同时接触关键的 Web 音频 API。

### 书籍

- [JavaScript for Sound Artists](https://www.routledge.com/JavaScript-for-Sound-Artists-Learn-to-Code-with-the-Web-Audio-API/Turner-Leonard/p/book/9781138961531) - 使用网络音频作为所有示例的自下而上的 JavaScript/DOM 课程。
- [Web Audio API](https://webaudioapi.com/book/) - 旨在成为几乎没有数字音频专业知识的网络开发人员的跳板。面向游戏音频和交互式应用程序。

### 时事通讯

- [Web Audio Weekly Newsletter](https://www.webaudioweekly.com) - 每周回顾网络音频中发生的事情。

### 社区

- [Slack](https://web-audio-slackin.herokuapp.com/) - 用于讨论网络音频的 Slack。
- [Web Audio Conference](https://webaudioconf.com/) - 致力于网络音频技术和应用的国际会议。

## 过时的

自 2019 年 1 月以来没有活动或正式终止的项目。

- [Gibberish](https://github.com/gibber-cc/gibberish) - 一个 JavaScript DSP 库，使用代码生成技术创建 JIT 优化的音频回调。
- [lissajous](https://github.com/kylestetz/lissajous) - 用于编程音频性能的工具。
- [SSSynthesiser.js](https://github.com/surikov/SSSynthesiser.js) - 用于交互式音乐和声音效果的波表合成器。
- [WAAX](https://github.com/hoch/WAAX/) - 为浏览器构建音乐应用程序。
- [Band.js](https://github.com/meenie/band.js/) Web 音频 API 的接口，支持节奏、多种乐器、重复部分和复杂拍号。
- [reverbGen](https://github.com/adelespinasse/reverbGen) - 用于生成人工混响脉冲响应的 JavaScript 库。
- [TuneJS](https://github.com/abbernie/tune) - 微音阶和纯音阶的调音库。支持超过 3,000 种历史调音。
- [Beet.js](https://github.com/zya/beet.js) - 用于创建欧几里德节奏和多节奏的音序器库。
- [AudioKeys](https://github.com/kylestetz/AudioKeys) - 用于网络音频项目的 QWERTY 键盘。
- [web-audio-test-api](https://github.com/mohayonao/web-audio-test-api) - CI 的网络音频测试库。
- [javascript-karplus-strong](https://github.com/mrahtz/javascript-karplus-strong) - Karplus-Strong 吉他合成的 JavaScript/Web Audio 实现。
- [osc-msg](https://github.com/mohayonao/osc-msg) - 具有容错功能的 OSC 消息解码器/编码器。
- [Pizzicato](https://github.com/alemangui/pizzicato) - 旨在简化浏览器中声音的创建和操作的库。
- [Mooog](https://github.com/mattlima/mooog) - 受 jQuery 和混合表启发，可简化 AudioNode 工作的工具。
- [envelope-generator](https://github.com/itsjoesullivan/envelope-generator) - 用于网络音频的简单 ADSR 包络生成器。
- [audio contour](https://github.com/danigb/audio-contour) - 5 级音频包络发生器。
- [web-audio-recorder-js](https://github.com/higuma/web-audio-recorder-js) - 记录音频输入（Web Audio API AudioNode 对象）并编码为音频文件图像（Blob 对象）的库。
- [audiolet](https://github.com/oampo/Audiolet) - 用于在浏览器内进行实时音频合成和合成的 JavaScript 库。
- [playnote](https://github.com/createbits/playnote) - 在浏览器中演奏您最喜欢的乐器，具有复杂的音符间隔和音阶。
- [Recorderjs](https://github.com/mattdiamond/Recorderjs) - 用于录制/导出 Web Audio API 节点输出的插件。
- [resampler](https://github.com/notthetup/resampler) - 用于重新采样音频的实用程序。
- [bpm-detective](https://github.com/tornqvist/bpm-detective) - 检测歌曲或音频样本的 BPM。
- [web-audio-utils](https://github.com/mohayonao/web-audio-utils) - Web Audio API 常用的实用函数。
- [web-audio-oscillators](https://github.com/lukehorvat/web-audio-oscillators) - 网络音频自定义振荡器的集合。
- [midi-ports](https://github.com/AndrejHronco/midi-ports) - 方便的库，可以更轻松地使用连接的 MIDI 设备。
- [Midi Logger](http://outputchannel.com/midi-logger/) - 此 Midi 记录器会将所有 MIDI 输入打印到您的浏览器以进行调试。
- [Code Player](https://github.com/jcppman/code-player) - 一款实验性应用程序，让您的代码为您歌唱。
- [Web Audio Modules](https://www.webaudiomodules.org/) - 用于网络浏览器的合成器和音频效果处理器（API 和实现）。

## 许可证

[![CC0](http://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

在法律允许的范围内，[Chinmay Pendharkar](https://chinmay.audio/) 已放弃本作品的所有版权以及相关或邻接权。
