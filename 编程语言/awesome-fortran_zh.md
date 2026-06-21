# 很棒的 Fortran [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
精彩的 Fortran 框架、库和软件的精选列表。灵感来自 @Wolg 的 [awesome-swift](https://github.com/Wolg/awesome-swift)。

- [很棒的 Fortran](#awesome-fortran)
	- [功能库](#functional-libraries)
	- [图形库](#graphics-libraries)
	- [数学库](#math-libs)
	- [JSON操作](#json-manipulation)
	- [XML操作](#xml-manipulation)
	- [日期和时间操作](#date-and-time-manipulation)
	- [Testing](#testing)
	- [Encoding-Decoding](#encoding-decoding)
  - [支持便携性](#portability-enabling)
  - [命令行解析](#command-line-parsing)
  - [编译和构建](#compiling-and-building)
  - [Preprocessor](#preprocessor)
  - [自动记录](#automatic-documentation)
  - [计算流体动力学](#computational-fluid-dynamics)
  - [Docker](#docker)
  - [Web](#web)
- [Resources](#resources)
  - [Fortran 网站](#fortran-websites)
	- [Fortran 视频](#fortran-videos)
- [其他很棒的清单](#other-awesome-lists)
- [Contributing](#contributing)

## 功能库
* [Functional Fortran](https://github.com/wavebitscientific/functional-fortran) - 现代 Fortran 的函数式编程。


## 图形库
*用于绘图、图形和 GUI 的库*

* [DISLIN](https://www.mps.mpg.de/dislin/) - 高级图形和用户界面库。
* [f90gl](https://math.nist.gov/f90gl/) - OpenGL 的官方 NIST Fortran 90 绑定的公共域实现。
* [F03GL](http://www-stone.ch.cam.ac.uk/pub/f03gl/index.xhtml) - OpenGL 库的 Fortran 2003 接口，以及 GLU 和 GLUT 工具包。
* [gtk-fortran](https://github.com/vmagnin/gtk-fortran/wiki) - 使用 [GTK+](https://www.gtk.org/) 构建图形用户界面 (GUI) 的跨平台库。  与 [Glade](https://glade.gnome.org/) RAD 工具结合使用时非常有用。
* [PGPLOT](https://www.astro.caltech.edu/~tjp/pgplot/) - 跨平台科学图形库。
* [VTKFortran](https://github.com/szaghi/VTKFortran) - 纯 Fortran (2003+) 库，用于写入和读取符合 VTK 标准的数据。

## 数学库
*用于计算和其他数学运算的库。*

* [BLAS](http://www.netlib.org/blas/) - 用于发布库的应用程序编程接口标准，以执行基本的线性代数运算，例如向量和矩阵乘法。
* [CERNLIB](http://cernlib.web.cern.ch/cernlib/) - CERN 程序库是一个大型通用库和模块的集合，在 CERN 中央计算机上以源代码和目标代码形式维护和提供
* [EISPACK](http://www.netlib.org/eispack/) - 用于矩阵特征值和特征向量数值计算的软件库，用 FORTRAN 编写
* [FGSL](https://www.lrz.de/services/software/mathematik/gsl/fortran/index.html) - [GNU 科学库]的可移植、基于对象的 Fortran 接口(https://www.lrz.de/services/software/mathematik/gsl/)
* [IMSL](https://www.imsl.com/products/imsl-fortran-libraries) - IMSL Fortran 数值库是高性能计算商业数学和统计库的标准
* [Lis](https://www.ssisc.org/lis/index.en.html) - 线性系统迭代求解器库
* [NAG Fortran Library](https://www.nag.co.uk/content/nag-library-fortran) - NAG Fortran 库由专家制作，可用于各种应用程序，以其卓越的性能而享誉全球，拥有数百个完整记录和测试的例程，是可用的最大的数学和统计算法集合
* [netCDF](https://github.com/Unidata/netcdf-fortran) - 一组软件库和自描述、独立于机器的数据格式，支持创建、访问和共享面向阵列的科学数据。
* [OpenBLAS](https://github.com/xianyi/OpenBLAS) - 最快的开源 BLAS 库之一。  几乎与英特尔 MKL 一样快。

## JSON操作
*使用 Fortran 语言操作 JSON 数据的库。*

* [FSON](https://github.com/josephalevin/fson) - Fortran 95 JSON 解析器。
* [json-fortran](https://github.com/jacobwilliams/json-fortran) - Fortran 2008 JSON API。

## XML操作
*使用 Fortran 语言操作 XML 数据的库。*

* [fox](https://github.com/andreww/fox) - Fortran XML 库
* [xml-fortran](https://sourceforge.net/projects/xml-fortran/) - 用于读写 XML 文件的全 Fortran 解决方案。

## 日期和时间操作
*使用 Fortran 语言进行日期和时间操作的库。*

* [datetime-fortran](https://github.com/wavebitscientific/datetime-fortran) - Fortran 2003 日期和时间操作库，仿照 Python 的日期时间库建模。

## 测试
*用于测试代码库和生成测试数据的库。*

* [FRUIT](https://sourceforge.net/projects/fortranxunit/) - FORTRAN 单元测试框架，用 FORTRAN 95 编写
* [Ftunit](http://flibs.sourceforge.net/ftnunit.html) - Fortran 单元测试框架，作者：Arjen Markus
* [pFUnit](https://sourceforge.net/projects/pfunit/) - 由 NASA 和 NGC TASC 的开发人员开发的带有 MPI 扩展的 Fortran 单元测试框架。  使用并行代码和面向对象的设计。
* [Vegetables](https://gitlab.com/everythingfunctional/vegetables) - 为了更健康的代码库，多吃蔬菜

## 编码-解码
*使用 Fortran 语言对数据进行编码和解码的库。*

* [BeFoR64](https://github.com/szaghi/BeFoR64) - ForRtran 穷人的 Base64 编码/解码库。用于现代（2003 年以上）Fortran 项目的 base64 编码/解码的 KISS 库。

## 支持便携性
*用于实现代码可移植性的库。*

* [PENF](https://github.com/szaghi/PENF) - 用于确保代码可移植性的纯 Fortran (2003+) 库。

## 命令行解析
*用于解析命令行和构建用户界面的库。*

* [FLAP](https://github.com/szaghi/FLAP) - Fortran 命令行参数解析器，适合穷人。一个 KISS 库，用于为现代（2003 年以上）Fortran 项目轻松构建漂亮的命令行界面 (CLI)。
* [options.f90](https://github.com/cngilbreth/optionsf90) - 现代 Fortran 的选项和输入处理。

## 编译和构建
*用于编译和构建 Fortran 项目的库。*

* [FoBiS](https://github.com/szaghi/FoBiS) - 为穷人设计的 Fortran 建筑系统。用于自动构建现代 Fortran 项目的 KISS 工具。

## 预处理器
*用于条件编译的库、用于简化代码的宏以及包含其他源文件、模板系统。*

* [Blockit/PyF95++](http://blockit.sourceforge.net/) - 一个相当简单的 Python 框架，用于将代码（或任何文本文件）块解析为嵌套块。 BlockIt 框架已被用于为 Fortran 95/2003 语言以及一些语言扩展创建模板功能。
* [PreForM](https://github.com/szaghi/PreForM) - Fortran 穷人的预处理器。

## 自动记录
*用于构建文档的库。*

* [FORD](https://github.com/cmacmackin/ford) - 现代 Fortran 程序的自动文档生成器。

## 计算流体动力学
*CFD 计算库*

* [MFC](https://github.com/MFlowCode/MFC) - 百亿亿级多相可压缩流求解器，通过 OpenACC 进行 GPU 加速。 2025 年戈登贝尔奖决赛入围者。
* [OFF](https://github.com/szaghi/OFF/tree/testing) - 开源有限体积流体动力学代码。

## 码头工人

* [Unoficial Image](https://hub.docker.com/r/baekjoon/onlinejudge-fortran/) - docker 镜像由 @baekjoon 提供

## 网络

* [Fortran Machine](https://github.com/mapmeld/fortran-machine) - 用 Fortran 90 编写的 MVC Web 堆栈

# 资源
用于提高 Fortran 开发技能和知识的各种资源，例如书籍、网站和文章。

## Fortran 网站

* [The Fortran Company](https://www.fortran.com/) - FORTRAN 编程语言的主页。
* [Fortran Dev](https://fortrandev.wordpress.com/) - Fortran 开发博客。
* [Fortran WIKI](http://fortranwiki.org/fortran/show/HomePage) - 讨论 Fortran 编程语言和科学计算各个方面的开放场所。

## Fortran 视频

* [GNU FORTRAN Lesson 1](https://www.youtube.com/watch?v=qUy8M10uZRU) - 有关 Fortran 编程语言的视频。

# 其他很棒的列表

其他令人惊叹的很棒的列表可以在 [awesome-awesomeness](https://github.com/bayandin/awesome-awesomeness) 列表中找到。

# 贡献

随时欢迎您的贡献！请提交拉取请求或创建问题以将新框架、库或软件添加到列表中。不要提交过去 6 个月内未更新或不够出色的项目。
