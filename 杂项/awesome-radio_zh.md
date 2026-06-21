# 很棒的电台 [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

精选的精彩无线电资源列表。灵感来自 Awesome-*。

我最近拿出我的 CB 收音机并将其安装在我的卡车上。这启发了我
创建一个包含我找到的所有无线电相关资源的开源存储库
有帮助和我关于这个主题的笔记。

该项目针对的是喜欢无线电通信各个方面的黑客。
虽然很多此类技术不可供公民使用并且受到严格监管
FCC 的规定，仅仅了解它的任何事情都是很特别的。我一直感兴趣
了解广播的来龙去脉，以及聆听新旧故事。

## 一般

### 友情链接

* [电台（维基百科）](http://en.wikipedia.org/wiki/Radio)
* [无线电频谱（维基百科）](http://en.wikipedia.org/wiki/Radio_spectrum)
* [Skywave（跳过）（维基百科）](http://en.wikipedia.org/wiki/Skywave)
* [来自一个的神秘信号
直升机](http://www.windytan.com/2014/02/mystery-signal-from-helicopter.html)
* [便携式特别提款权](http://hackaday.io/project/1538-PortableSDR)
* [N0NBH's Solar-Terrestrial Data](http://www.hamqsl.com/solar2.html) - 当前
日地数据，并解释其对高频传播的影响
和传播预测。

## CB

公民频段无线电（CB）是一种双向无线电频谱，专用于开放使用
任何人几乎任何目的。在美国和许多其他国家，
不需要许可证即可运营。 CB 由 26.965 之间的 40 个通道组成
MHz 和 27.405 MHz，其中通道 09 专用于紧急情况。

CB 在卡车司机和无线电爱好者中更受欢迎，但它的用处
并不止于此。非常适合乘坐流行的卡车运输进行长途旅行
路线。您可以调到 19 频道（非官方卡车司机频道）并获取
实时交通更新、备用路线和事故警告。

如果有一个经过适当调谐的良好天线，则可以预期的典型范围
您的 CB 距离约为 2 - 5 英里（3.2 - 8 公里）。

### 一般用途

我在吉普车和卡车司机论坛上找到了很多信息。来自我自己的
根据经验，我听说的 CB 变速箱中大约有一半包含手柄
某种。我也听到很多脏话，所以我不会不小心出汗
放开“操”或“屎”。

CB 是公开的。非常公开。这似乎是一件“没什么”的事情，但随着
当前这一代人几乎只使用手机，很容易忘记
使用像 CB 收音机这样“原始”的东西本质上是[广播到
世界](http://en.wikipedia.org/wiki/Citizens_band_radio#Working_skip)。

卡车司机倾向于使用 19 频道。这是监控交通的好频道
条件。

9 频道仅供紧急情况使用。此频道上没有一般性的闲聊。如果你
出了故障，或者你的车着火了，除了拨打 911，这是一个很好的选择
发送帮助的频道。

在波特兰周围，我在 6、17 和 28 频道上听到很多闲聊声。这些是
有趣对话的好渠道。

### 驻波比

[SWR](http://en.wikipedia.org/wiki/Standing_wave_ratio)，或驻波比
是将天线连接到收音机时的效率衡量标准。

最佳比例是 1:1，但最终可能会得到 1.3:1 左右。任何东西
高于 2:1 应该被视为禁忌，因为它会损坏您的收音机
造成传输不良。阅读[如何调整
SWR](http://www.rightchannelradios.com/tuning-cb-antenna- adjustment-swr)。

### 安装移动 CB

正确安装 CB 的关键是 A) 不损坏无线电硬件和 B)
在接收端和发射端都获得良好的范围和质量。

遵循以下文章中的建议将确保您拥有高质量的
设置。

### 友情链接

* [Right Channel Radios](http://www.rightchannelradios.com/) - 不错的网上商店
用于零件、无线电、天线和安装座。
* [CB Slang](http://www.cbslang.com/) - 大部分都很幽默，但也很有帮助。
* [CB 俚语（维基百科）](http://en.wikipedia.org/wiki/List_of_CB_slang)
* [CB 谈话和礼仪](http://www.jeepforum.com/forum/f8/cb-radio-etiquette-jeep-trail-1169815/)
* [Skip](http://cbradiomagazine.com/Articles/How%20to%20Shoot%20Skip.htm)
* [愚蠢的 CB 手柄](http://www.somethingawful.com/news/cb-handles/)
* [CB 常见问题解答](http://www.advancedspecialties.net/cb-radio-faq.htm)
* [频率表](http://www.radioreference.com/apps/db/?aid=7731)

## SDR（软件无线电）

软件定义无线电是一种定义组件的方法，这些组件通常是
硬件（例如滤波器和放大器）作为软件。它已经存在了一段时间了
虽然，但随着运行 SDR 所需的数字电子设备的成本变得越来越高
越来越便宜，我们看到黑客玩和建造的人数增加
与特别提款权。

我希望有本节的贡献者。

### 友情链接

* [Gqrx](http://gqrx.dk/)
* [.NET 上的 sdrsharp](http://sdrsharp.com)

### 硬件
* __推荐的入门硬件__ 在低端，
[RTL-SDR](http://sdr.osmocom.org/trac/wiki/rtl-sdr) 是一款超便宜的 USB
加密狗，围绕它建立了一个繁荣的社区。
* 在成本范围的另一边，[pervices](http://www.pervices.com/)
制作一些真正高吞吐量的 PCIe 设备，供您需要记录所有数据时使用
曾经的交通。软件和社区对此的支持不太好，
不过（你可以责怪@outofculture）。
* 您还可以浏览[大
列表](https://gnuradio.org/redmine/projects/gnuradio/wiki/Hardware) 的所有
兼容的硬件。
* 天线有自己的选择和权衡体系，我对此有所了解
什么也没有。

### 软件
根据您使用的硬件，它可能附带一些演示软件
玩弄。这对于有机会看到一些波浪和
开始了解什么是可能的。否则，[GNU
Radio](https://gnuradio.org/redmine/) 将前往您消磨时间的地方。
它主要只是一个库，但它也有一个支持 GUI 用于组合
然后输出 python 的处理块。一旦你感觉更舒服了，你
也可以只使用 GNURadio 进行任何设备调整、设置和 I/O，然后使用
numpy 用于信号处理数学。

仅仅可视化和手动检查信号就是学习的一个有价值的部分
如何与他们合作。 [Baudline](http://www.baudline.com/) 是一个陈旧的东西
的事情，但这是最好的。预先警告，学习 UI 不会到来
对任何人来说都很容易。

## 业余无线电（又称业余无线电）

业余无线电的爱好有着悠久而光荣的传统。第一个收音机
业余爱好者是无线电技术的真正先驱。业余爱好者“发明”和改进
许多早期的无线电技术，并且是第一个传输音乐、广播的
播放，并向少数拥有新式收音机的人提供信息
接收器。

第二次世界大战后，业余无线电的爱好蓬勃发展。广播俱乐部如雨后春笋般涌现
在世界各地的学校里，孩子们每晚回家建造一些新的
装置，或者通过无线与某人聊天。这些年轻人
成为技术专业的中流砥柱，并发展了许多
我们今天使用的现代技术。
([WIA](http://www.wia.org.au/licenses/foundation/about/))

[什么是业余无线电？](http://www.arrl.org/what-is-ham-radio)

### 友情链接

* 美国无线电中继联盟 - [ARRL](http://www.arrl.org/)
* 澳大利亚无线研究所 [WIA](http://www.wia.org.au/)
* 英国无线电协会 - [RSGB](http://rsgb.org/)
* 巴基斯坦业余无线电协会 - [PARS](http://www.pakhams.com/)
* [国际业余无线电联盟](http://www.iaru.org/)
* [日本小行星任务](http://www.arrl.org/news/amateur-radio-transponder-will-accompany-japanese-asteroid-mission-into-deep-space)
* [慢扫描电视](https://en.wikipedia.org/wiki/Slow-scan_television)

我希望有本节的贡献者。

### 业余无线电执照

* 在[美国](http://www.arrl.org/getting-licensed) 有三个许可证
课程——技术员、普通和额外。
* [基金会许可证](http://www.wia.org.au/licenses/foundation/about/)
澳大利亚。
* [基金会许可证]
(http://rsgb.org/main/clubs-training/for-students/foundation/) 在英国。
* 在
[巴基斯坦](http://www.pakhams.com/index.php?option=com_content&view=article&id=75&Itemid=92)
首先您申请 SWL（短波收听者）会员资格，然后您
有资格[申请 HAM
许可证](http://www.pta.gov.pk/index.php?option=com_content&view=article&id=466%3Aamateur-wireless-license&catid=138%3Aguidelines&Itemid=349)。

## 公共健康与安全

美国的警察和消防部门通常通过集群无线电进行通信。
这使得在没有树干跟踪的情况下很难使用普通接收器进行扫描
能力。请参阅 [trunking](#trunking) 部分了解更多信息。

### 集群

虽然并不严格针对公共卫生和安全，但它通常是第一个
当谈论集群无线电时，我会想到这一点。

集群无线电是一种数字双向通信形式，其中多个
组织可以共享一小部分真实频率而无需聆听
另一个组织的对话。用户可以选择逻辑通道或
组和基站将找到一个空频率进行传输。

### 友情链接

* [项目25](http://www.project25.org/)
* [项目 25 维基百科](http://en.wikipedia.org/wiki/Project_25)
* [集群无线电维基百科](http://en.wikipedia.org/wiki/Trunked_radio_system)
