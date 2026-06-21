# 真棒 GIF [![Awesome](https://awesome.re/badge-flat.svg)](https://awesome.re)

> 精选的精彩 [GIF](https://en.wikipedia.org/wiki/GIF) 资源列表。

与图形交换格式 (GIF) 相关的工具、脚本、库、示例和其他资源列表。

## 内容

<!--lint disable awesome-toc-->
- [通用工具](#general-tools)
- [Utilities](#utilities)
- [Libraries](#libraries)
	- [C++](#c)
	- [C#](#c-sharp)
	- [Haxe](#haxe)
	- [Java](#java)
	- [JavaScript](#javascript)
	- [PHP](#php)
	- [Objective-C](#objective-c)
	- [Swift](#swift)
- [GUI](#gui)
- [Hosting](#hosting)
- [在线工具](#online-tools)
- [Community](#community)
- [Scripts](#scripts)
	- [帧转 GIF](#frames-to-gif)
	- [GIF 转帧](#gif-to-frames)
	- [高品质 GIF](#high-quality-gif)
	- [优化 GIF](#optimize-gif)
	- [有损 GIF 压缩器](#lossy-gif-compressor)
	- [从视频制作 GIF](#making-gif-from-video)
	- [Cinemagraphs](#cinemagraphs)
	- [完美循环](#perfect-loop)
	- [YouTube 视频转 GIF](#youtube-video-to-gif)
- [Miscellaneous](#miscellaneous)

## 通用工具

- [FFmpeg](https://www.ffmpeg.org)
- [ImageMagick](https://imagemagick.org/script/index.php)
- [GraphicsMagick](http://www.graphicsmagick.org/) - 通常比 ImageMagick 更快。
- [MoviePy](https://zulko.github.io/moviepy/) - 用于视频编辑的 Python 模块。

## 公用事业

- [Gifgen](https://github.com/lukechilds/gifgen) - 简单的高质量 GIF 编码。
- [Gifify](https://github.com/jclem/gifify) - 将屏幕录制转换为 GIF。
- [Screengif](https://github.com/dergachev/screengif) - 创建动画 GIF 截屏视频。
- [Gifline](https://github.com/zehfernandes/gifline) - Chrome 扩展程序可将 GIF 放入您的电子邮件中。
- [Tty2gif](https://github.com/z24/tty2gif) - 将脚本及其输出记录为二进制和 GIF 格式。
- [Gifit](https://github.com/takempf/GIFit) - Chrome 扩展程序可将 YouTube 视频制作为 GIF。
- [Ccapture.js](https://github.com/spite/ccapture.js) - 捕获使用 HTML5 画布创建的动画。
- [Kap](https://getkap.co/) - 漂亮的开源应用程序，用于捕获屏幕并导出为 GIF。
- [gifski](https://github.com/ImageOptim/gifski) - 基于 libimagequant 的高质量 GIF 编码器。
- [Gifcurry](https://github.com/lettier/gifcurry) - 为 GIF 制作者提供的、Haskell 构建的开源编辑器。

## 图书馆

### C++

- [Gif-h](https://github.com/charlietangora/gif-h) - 用于创建动画 GIF 的 C++ 单标头库。
- [msf_gif](https://github.com/notnullnotvoid/msf_gif) - 用于创建动画 GIF 的 C/C++ 单标头库。

<h3 id="c-sharp">C#</h2>

- [dot-screencap](https://github.com/Speiser/dot-screencap) - 一个简单的库，用于录制屏幕并将其保存为动画 GIF。
- [WpfAnimatedGif](https://github.com/XamlAnimatedGif/WpfAnimatedGif) - 一个简单的库，用于在 WPF 中显示动画 GIF 图像。
- [XamlAnimatedGif](https://github.com/XamlAnimatedGif/XamlAnimatedGif) - 一个简单的库，用于在 XAML 应用程序（WPF、WinRT、Windows Phone）中显示动画 GIF 图像。
- [AnimatedGif](https://github.com/mrousavy/AnimatedGif) - 用于读取和创建动画 GIF 的高性能 .NET 库。

### 哈克西

- [Gif](https://github.com/snowkit/gif) - Haxe GIF 编码器。

### 爪哇

- [Android-gif-drawable](https://github.com/koral--/android-gif-drawable) - 用于在 Android 上显示动画 GIF 的视图和 Drawable。
- [GifImageView](https://github.com/felipecsl/GifImageView) - Android ImageView 处理动画 GIF 图像。
- [Gif-animation](https://github.com/extrapixel/gif-animation) - 用于播放和导出 GIF 的处理库。
- [Android-gif-encoder](https://github.com/nbadal/android-gif-encoder) - 适用于 Android 的动画 GIF 编码器。

### JavaScript

- [Gif.js](https://github.com/jnordberg/gif.js) - 从 DOM 创建 GIF。
- [Omggif](https://github.com/deanm/omggif) - GIF 89a 编码器和解码器。
- [Animated_GIF](https://github.com/sole/Animated_GIF) - 用于创建动画 GIF 的 JavaScript 库。
- [Gifffer](https://github.com/krasimir/gifffer) - 阻止自动播放 GIF 动画的 JavaScript 库。
- [Gifplayer](https://github.com/rubentd/gifplayer) - 用于播放和停止动画 GIF 的 JQuery 插件。
- [node-gify](https://github.com/tj/node-gify) - JavaScript 使用 FFmpeg 和 gifsicle 将视频转换为 GIF。
- [Gifencoder](https://github.com/eugeneware/gifencoder) - Node.js 的服务器端动画 GIF 生成。

### PHP

- [GifCreator](https://github.com/Sybio/GifCreator) - 从多个图像创建动画 GIF 的 PHP 类。
- [GifFrameExtractor](https://github.com/Sybio/GifFrameExtractor) - PHP 类分隔 GIF 动画的所有帧。

### Objective-C

- [FLAnimatedImage](https://github.com/Flipboard/FLAnimatedImage) - FlipBoard 的 iOS GIF 引擎。

### 斯威夫特

- [SwiftyGif](https://github.com/alexiscreuzot/SwiftyGif) - 高性能且易于使用的 Gif 引擎。
- [Gifu](https://github.com/kaishin/gifu) - Swift 中对 iOS 的动画 GIF 支持。

## 图形用户界面

- [Qgifer](https://sourceforge.net/projects/qgifer/)

## 托管

- [Imgur](https://imgur.com) - 最大文件上传为 50MB。

## 在线工具

- [EzGif](https://ezgif.com/) - 在线 GIF 制作器和图像编辑器。
- [Giflr](https://giflr.com/) - 用于制作或重新混合动画 GIF 的网络应用程序。
- [GIF Frame Extractor](https://giftoframes.org/) - 在线将动画 GIF 转换为单独的帧。

## 社区

- [Giphy.com](https://giphy.com)
- [/r/educationalgifs](https://www.reddit.com/r/educationalgifs/)

## 脚本

### 帧转 GIF

FFmpeg
```bash
ffmpeg -f image2 -i image%d.jpg animated.gif
```

图像魔术师
```bash
magick -delay 20 -loop 0 frames*.png animated.gif
```
适用于 GraphicsMagick、ImageMagick、FFmpeg 的 Bash 脚本 (```frames2gif.sh```)
```bash
#!/bin/bash
if [ $# -ne 5 ]; then
    echo "please provide the moviename and directory where to store the frames"
    echo "./frames2gif.sh [directory] [movie.mp4] [filename.gif] [gm|im|ffmpeg] [png|jpg]"
    exit 1
fi
    if [ "png" == "$5" ]; then
        suffix="png"
    else
        suffix="jpg"
    fi

    CONVERT=$(which magick)
    GM=$(which gm)
    FFMPEG=$(which ffmpeg)
    FFPROBE=$(which ffprobe)
    FPS=$($FFPROBE -show_streams -select_streams v -i "$2"  2>/dev/null | grep "r_frame_rate" | cut -d'=' -f2 | cut -d'/' -f1)
    echo "FPS: ${FPS}"
if [ "im" == "$4" ]; then # use imagemagick
    FPS=$(echo "1 / ${FPS} * 100" |bc -l)
    $CONVERT "$1/*.${suffix}"  -delay ${FPS} -loop 0 "$3"
elif [ "gm" == "$4" ]; then # use graphicsmagick
    FPS=$(echo "1 / ${FPS} * 100" |bc -l)
    $GM convert "$1/*.${suffix}"  -delay ${FPS} -loop 0 "$3"
else # use crappy gif-algorithm from ffmpeg
    $FFMPEG -f image2 -framerate ${FPS} -i "$1/%08d.${suffix}" "$3"
fi
```
来自 [DeepDreamVideo](https://github.com/graphific/DeepDreamVideo)，[来源](https://github.com/graphific/DeepDreamVideo/blob/master/frames2gif.sh)


### GIF 转帧

```bash
ffmpeg -i video.mpg image%d.jpg
```
```bash
magick animated.gif -coalesce image%05d.png
```

### 高品质 GIF

使用 FFmpeg / 基于此[文章](http://blog.pkh.me/p/21-high-quality-gif-with-ffmpeg.html)

- 生成调色板：

```bash
#!/bin/sh
start_time=30
duration=3
ffmpeg -y -ss $start_time -t $duration -i input.avi \
-vf fps=10,scale=320:-1:flags=lanczos,palettegen palette.png
```
- 使用调色板输出 GIF：

```bash
#!/bin/sh
start_time=30
duration=3
ffmpeg -ss $start_time -t $duration -i input.avi -i palette.png -filter_complex \
"fps=10,scale=320:-1:flags=lanczos[x];[x][1:v]paletteuse" output.gif
```

### 优化 GIF

```bash
magick output.gif -layers Optimize output_optimized.gif
```

### 有损 GIF 压缩器

```bash
./gifsicle -O3 --lossy=80 -o lossy-compressed.gif input.gif

```
[有损 Gif](https://kornel.ski/lossygif)


### 从视频制作 GIF

```python
from moviepy import VideoFileClip

clip = (VideoFileClip("input.avi")
        .subclipped((4,00.00),(5,00.00))
        .resized(0.3))
clip.write_gif("output.gif")

```
<!--lint ignore double-link-->
[文章](http://zulko.github.io/blog/2014/01/23/making-animated-gifs-from-video-files-with-python/#converting-a-video-excerpt-into-a-gif)

### 电影照片

冻结一个区域

```python
from moviepy import VideoFileClip, vfx

clip = (VideoFileClip("input.avi")
        .subclipped((4,00.00),(5,00.00))
        .resized(0.3)
        .with_effects([vfx.FreezeRegion(outside_region=(170, 230, 380, 320))]))
clip.write_gif("output.gif", fps=15)
```
<!--lint ignore double-link-->
[文章](http://zulko.github.io/blog/2014/01/23/making-animated-gifs-from-video-files-with-python/#freezing-a-region)

```bash
ffmpeg \
-ss ${starttime} -t ${duration} -i ${vidfile}                         `# body of loop` \
-ss TODO ${starttime} MINUS ${duration} -t ${fadetime} -i ${vidfile}  `# lead-in for crossfade` \
-loop 1 -i ${stillfile}                                               `# masked still image` \
-filter_complex "
  [0:v]setpts=PTS-STARTPTS[vid];                                      `# speed adjustment - not needed here, so noop`
  color=white,scale=3840x2160,fade=in:st=0:d=${fadetime}[alpha];      `# crossfade alpha, double length ahead of speed change`
  [1:v][alpha]alphamerge[am];                                         `# apply alpha to lead-in`
  [am]setpts=PTS+(${duration}-${fadetime})/TB[layer2];                  `# speed adjustment and offset for lead-in`
  [vid][layer2]overlay[oo];                                           `# overlay for crossfade`
  [oo][2:v]overlay=shortest=1[out1];                                  `# overlay still image`
  [out1]crop=w=${cropfactor}*iw:h=${cropfactor}*ih:y=${yoffset}*ih,scale=${outputwidth}:-1, `# crop and scale`
  eq=gamma=${gamma}:contrast=${contrast}:saturation=${saturation},unsharp                   `# final adjustments`
" -an output.mp4
```

### 完美循环

```python
from moviepy import VideoFileClip
from moviepy.video.tools.cuts import FramesMatches

clip = VideoFileClip("input.avi").resized(0.3)
scenes = FramesMatches.from_clip(clip, 10, 3)

selected_scenes = scenes.select_scenes(2, 1, 4, 0.5)
selected_scenes.write_gifs(clip.resized(width=450), "./outputs_directory")

```
[文章](http://zulko.github.io/blog/2015/02/01/extracting-perfectly-looping-gifs-from-videos-with-python-and-moviepy/)

### YouTube 视频转 GIF

- 通过 yt-dlp 下载并转换。

```bash
yt-dlp https://www.youtube.com/watch?v=V2XpsaLqXc8
```

[yt-dlp](https://github.com/yt-dlp/yt-dlp)

## 杂项

- [Why is the GIF I created so slow?](https://superuser.com/questions/569924/why-is-the-gif-i-created-so-slow/569967) - 使用ImageMagick解决GIF速度问题。

## 使用

使用此列表的最佳方法是：

- 通过浏览[内容](#contents)。
- 使用<kbd>command</kbd> + <kbd>F</kbd>搜索内容

## 制作人员

作者：[Craig Davison](https://davison.io) 和贡献者。

基于 [Ismail Baaj](https://ismailbaaj.fr) 的[恢复列表](https://github.com/sindresorhus/awesome/issues/872)。
