# Awesome-开源摄影
[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

很棒的免费开源摄影软件和库的列表。还有视频工具。如需更多精彩内容，请查看 [awesome](https://github.com/sindresorhus/awesome)。


- [General](#general)
- [相机固件模块](#camera-firmware-mods)
- [Libraries](#libraries)
	- [Canon](#canon)
	- [GoPro](#gopro)
	- [Sony](#sony)
- [Utilities](#utilities)
- [模拟摄影](#analogue-photography)
- [RAW 图像开发人员](#raw-image-developers)
- [HDR 专用软件](#hdr-specific-software)
- [全景拼接](#panorama-stitching)
- [照片整理者](#photo-organizers)
- [EXIF 编辑器](#exif-editors)
- [照片下载器](#photo-downloaders)
- [相机系绳](#camera-tetherers)
- [显示器色彩校正](#monitor-color-correction)
- [360° 图像](#360-images)
- [替代图像查看器](#alternative-image-viewers)
- [有用的 GIMP 模组或脚本](#useful-gimp-mods-or-scripts)
- [Communities](#communities)
- [Resources](#resources)
- [Video](#video)
	- [通用工具](#general-tools)
	- [合成软件](#compositing-software)
	- [视频库](#video-libraries)
- [Scripts](#scripts)
	- [视频转全景](#video-to-panorama)

## 一般

- [GIMP](http://www.gimp.org/) - 用于图像处理的瑞士刀。
- [PhotoFlow](https://github.com/aferrero2707/PhotoFlow) - 一种非破坏性照片修饰程序，包括 RAW 图像显影。
- [ImageMagick](http://www.imagemagick.org/) - 一套用于修改和处理图像的命令行实用程序。
- [GraphicsMagick](http://www.graphicsmagick.org/) - GraphicsMagick 通常比 ImageMagick 更快。

## 相机固件模块

- [CHDK](http://chdk.wikia.com/wiki/CHDK) - Canon Hack 开发套件，适用于佳能相机。
- [Magic Lantern](http://magiclantern.fm/) - 一种软件增强功能，可为佳能数​​码单反相机提供更多功能。
- [Autoexec Hack](https://github.com/KonradIT/autoexechack) - GoPro 相机的黑客汇编。
- [PTool Firmware Manipulation Tool](http://www.gh1-hack.info/) - 更改松下相机的视频录制参数。
- [Nikon Hacker](https://nikonhacker.com/wiki/Main_Page) - Nikon Patch 和 Nikon Emulator，2 个用于尼康相机的软件。
- [Xiaomi Yi Autoexec](https://github.com/PJanisio/Xiaomi_Yi_autoexec) - 小米小蚁相机自动执行脚本和模组的编译。

## 图书馆

- [LibGphoto2](https://github.com/gphoto/libgphoto2) - C APi 用于数码相机访问和远程控制。 Java、Python、C# 以及更多绑定。

### 佳能

- [OfxCanon](https://github.com/roxlu/ofxCanon) - Canon EDSK 的 OpenFrameworks 插件。
- [Edsdk4j](https://github.com/kritzikratzi/edsdk4j) - 适用于 Java 的佳能 SDK。

### 戈普罗
- [GoPro](https://github.com/kschzt/gopro) - 用于从 Node.js 控制 GoPro Hero 3 相机的 API。
- [GoPro](https://github.com/DenisCarriere/gopro) - GoPro Hero 4 - Python API。
- [GoPro](https://github.com/joshvillbrandt/goprohero) - 一个 Python 库和一个 CLI，可通过 http 与 GoPro HERO3、HERO3+ 和 HERO4 相机连接。
- [GoPro.Hero](https://github.com/r1pper/GoPro.Hero) - 用于访问和控制 GoPro HERO 的轻量级 C# 库。

### 索尼

- [SonyPy](https://github.com/storborg/sonypy) - 索尼相机远程 API 的 Python 模块。

## 公用事业

- [Timelapse-sony](https://github.com/ThibaudM/timelapse-sony) - Android 应用程序，用于通过“使用智能手机控制”模式或通过 NFC 连接创建延时摄影。
- [Remoteyourcam-usb](https://github.com/crazymaik/remoteyourcam-usb) - 通过 USB 从 Android 设备控制佳能或尼康 DSLR 相机。
- [digiCamControl](https://github.com/dukus/digiCamControl) - 单反相机远程控制开源软件。

## 模拟摄影

- [Digitaltruth](https://www.digitaltruth.com/devchart.php) - 电影发展图。

## RAW 图像开发人员

- [Darktable](http://www.darktable.org/) - 开源摄影工作流程应用程序和 RAW 开发人员。
- [RawTherapee](http://rawtherapee.com/) - 跨平台原始图像处理程序。
- [Photivo](http://photivo.org/photivo/start?redirect=1) - 多平台照片处理器，适用于 16 位精度的 RAW 和位图图像。
- [Raw Studio](https://github.com/rawstudio/rawstudio) - 读取和操作来自数码相机的 RAW 图像。
- [UFRaw](http://ufraw.sourceforge.net/) - 用于读取和操作数码相机原始图像的实用程序。
- [DCRaw](http://www.cybercom.net/~dcoffin/dcraw/) - 在 Linux 中解码原始数码照片。
- [Lightzone](http://lightzoneproject.org/) - 适用于 Windows/Mac/Linux 的开源数字暗室软件。
- [Fotoxx](http://www.kornelix.com/fotoxx.html) - 用于编辑照片和其他图像的 Linux 程序。

## HDR 专用软件
- [Luminance](https://github.com/LuminanceHDR/LuminanceHDR) - HDR 成像的完整工作流程。
- [QPSFTMO](http://theplaceofdeadroads.blogspot.com/2006/07/qpfstmo-hdr-tone-mapping-gui-for-linux_04.html) - 适用于 Linux 的 HDR 色调映射 GUI。
- [PFS Tools](http://pfstools.sourceforge.net/) - 一组用于读取、写入和操作 HDR 图像和视频帧的命令行程序。

## 全景拼接

- [Hugin](http://hugin.sourceforge.net/) - 易于使用的跨平台全景成像工具链。
- [Panorama Tools](http://www.panoramatools.com/) - 用于将多个源图像重新投影和混合成多种类型的沉浸式全景的框架。

## 照片整理者

- [Shotwell](http://yorba.org/shotwell/) - GNOME 3 的照片管理器。
- [DigiKam/ShowFoto](http://www.digikam.org/drupal/about?q=about/overview) - KDE/Gnome 桌面的开源照片管理器。
- [GPhoto](http://www.gphoto.org/) - 一个程序和库框架，允许用户从数码相机下载图片。
- [Lychee](http://lychee.electerious.com/) - 一个美观且易于使用的照片管理系统，您可以在服务器上运行，以管理和共享照片。
- [Simple Gallery](https://github.com/SimpleMobileTools/Simple-Gallery/) - 一款 Android 图库应用程序，用于查看与 Android 图库类似的照片和视频，支持文件复制/移动/重命名/删除/共享。
- [Leaf Pic](https://github.com/HoraApps/LeafPic/) - Material Design 的 Android 画廊替代品。
- [A Photo Manager](https://github.com/k3b/APhotoManager/) - 管理 Android 上的本地照片：图库、带照片地图的地理标记、标签、查找、排序、查看、复制、删除、发送...
- [PhotoPrism](https://photoprism.org/) - PhotoPrism™ 是一个基于服务器的应用程序，用于浏览、组织和共享您的个人照片集。

## EXIF 编辑器
- [ExifTool](http://owl.phy.queensu.ca/~phil/exiftool/) - 用于读取、写入和操作图像、音频和视频元数据的程序。
- [Exiv2](https://github.com/Exiv2/exiv2/) - Exiv2 是一个 C++ 库和命令行实用程序，用于读取、写入、删除和修改 Exif、IPTC、XMP 和 ICC 图像元数据。

## 照片下载器

- [Rapid Photo Downloader](http://www.damonlynch.net/rapid/index.html) - 适用于 Linux 桌面的照片和视频下载器。

## 相机系绳

- [Entangle](http://entangle-photo.org/) - Entangle 提供了一个 GUI，用于使用完全由计算机控制的数码相机拍照。

## 显示器色彩校正

- [Hughski](http://www.hughski.com/index.html)
- [DisplayCal](http://displaycal.net/) - 开源显示器校准和表征。

## 360° 图像

- [Open360viewer](https://github.com/TheGreyDiamond/open360viewer) - 开源 360° 媒体查看器。


## 替代图像查看器

- [Geeqie](http://geeqie.sourceforge.net/) - 用于类 Unix 操作系统的图像查看器和图像组织程序。
- [FEH](http://feh.finalrewind.org/) - X11 图像查看器。

## 有用的 GIMP 模组或脚本

- [GIMP 插件注册表](http://registry.gimp.org/)
- [Cinepaint](http://sourceforge.net/projects/cinepaint/files/CinePaint/) - 一个基于 GIMP 的电影位图帧绘制和修饰程序。

## 社区
- [Flickr 开源摄影组](https://www.flickr.com/groups/83823859@N00/)
- [/r/FOSSPhotography](http://reddit.com/r/fossphotography) - reddit 上有关免费开源摄影软件的社区。
- [Google+ 上的开源摄影社区](https://plus.google.com/u/0/communities/110647644928874455108)
- [Facebook 上的开源摄影小组](https://www.facebook.com/groups/326042310770868/)
- [Reddit 上的开源摄影子](https://www.reddit.com/r/opensourcephotography)
- [500px 开源摄影组](https://500px.com/groups/open-source-photography)
- [PIXLS.US](https://pixls.us) - 致力于使用免费软件工具进行高质量摄影的教程、工作流程和展示的社区

## 资源
- [Unsplash.com](https://unsplash.com/) - 免费（做任何你想做的）高分辨率照片，[已授权](https://medium.com/unsplash/the-unsplash-license-f6fb7de5c95a) 根据 Unsplash 许可证（[更改自CC0](https://medium.com/unsplash/why-we-moved-from-the-creative-commons-zero-license-to-the-unsplash-license-598f76386489))
- [Pexels.com](https://pexels.com/) - 版税免费高分辨率库存照片，[许可](https://www.pexels.com/photo-license/) 根据知识共享零 (CC0)
- [Pixabay.com](https://pixabay.com/) - 免版税库存照片和视频，[已获得知识共享零 (CC0) 许可](https://pixabay.com/en/service/faq/)。
- [Shutterography.com](https://www.shutterography.com) - 免费照片。

## 视频

### 通用工具

- [FFmpeg](https://www.ffmpeg.org/) - 完整的跨平台解决方案
录制、转换和流式传输音频和视频。
- [Virtualdub](http://www.virtualdub.org/) - 用于基本编辑和编码的免费视频工具。

### 合成软件

- [Natron](https://github.com/MrKepzie/Natron) - 基于节点的合成器，其原理与电影和电视后期制作中使用的最先进工具相同。
- [ButtleOFX](https://github.com/buttleofx/ButtleOFX) - 一个简单、用户友好的开源合成软件。
- [Blender](https://www.blender.org/) - 这个开源 3D 图形具有视频编辑工具。
- [Shotcut](https://github.com/mltframework/shotcut) - 免费、开源、跨平台的视频编辑器。

### 视频库

- [OpenFX](http://openfx.sourceforge.net/) - 用于 2D 视觉效果的开放插件 API。
- [TuttleOFX](https://github.com/tuttleofx/TuttleOFX) - 一个基于OpenFX插件格式的图像处理框架。
- [Vid.stab](https://github.com/georgmartius/vid.stab) - 一个视频稳定库，可以插入 Ffmpeg 和 Transcode。
- [Frei0r](https://github.com/dyne/frei0r) - 大量免费和便携式视频插件。

## 脚本

### 视频转全景

使用 [FFmpeg](https://www.ffmpeg.org/) 和 [Hugin](http://hugin.sourceforge.net/)。

```bash
#!/bin/bash
mkdir -p /tmp/images
ffmpeg -i video.avi -r 5 -qscale 3  tmp/images/image-%3d.jpg
pto_gen -o tmp/hugin.pto tmp/images/*.jpg
cpfind --multirow -o tmp/hugin.pto tmp/hugin.pto
cpclean -o tmp/hugin.pto tmp/hugin.pto
linefind -o tmp/hugin.pto tmp/hugin.pto
autooptimiser -a -l -s -m -o tmp/hugin.pto tmp/hugin.pto
pano_modify -o tmp/hugin.pto --center --fov=AUTO --canvas=70% tmp/hugin.pto
pto2mk -o tmp/hugin.mk -p tmp/output tmp/hugin.pto
make -f tmp/hugin.mk all
```

![license](https://i.creativecommons.org/l/by-nc/4.0/88x31.png)


