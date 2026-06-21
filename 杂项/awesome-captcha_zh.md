# 很棒的验证码 [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> 精彩验证码库和验证码破解工具的精选列表。

[CAPTCHA](https://en.wikipedia.org/wiki/CAPTCHA) 是一种在计算中用于确定用户是否为人类的质询-响应测试。


[English](README.md) | [中文](README-zh.md) | [Polish](README-pl.md)

## 内容

- [Libraries](#libraries)
- [Generation](#generation)
- [Crack](#crack)
  - [General](#general)
  - [Chinese](#chinese)
- [Tools](#tools)
- [Other](#other)
- [Maintainers](#maintainers)


## 图书馆

- [mewebstudio/captcha](https://github.com/mewebstudio/captcha) - Laravel 5 的验证码。
- [CGregwar/Captcha](https://github.com/Gregwar/Captcha) - PHP 验证码库。
- [trekjs/captcha](https://github.com/trekjs/captcha) - Node.js 的轻量级纯 JavaScript 验证码。没有 C/C++、没有 ImageMagick、没有 Canvas。
- [patchca](https://code.google.com/archive/p/patchca) - 用 Java 编写的简单但功能强大的 CAPTCHA 库。
- [google/recaptcha](https://github.com/google/recaptcha) - reCAPTCHA 的 PHP 客户端库，这是一项免费服务，可保护您的网站免受垃圾邮件和滥用。
- [ambethia/recaptcha](https://github.com/ambethia/recaptcha) - ruby 应用程序的 ReCaptcha 助手。
- [anhskohbo/no-captcha](https://github.com/anhskohbo/no-captcha) - Laravel 没有验证码 reCAPTCHA。
- [lorien/captcha_solver](https://github.com/lorien/captcha_solver) - 不同验证码解决服务的通用 python API。


## 一代
- [captcha-api](https://captcha-api.akshit.me) - 由 AI 提供支持的免费、快速且可靠的验证码 API
- [dchest/captcha](https://github.com/dchest/captcha) - Go包captcha实现了图像和音频验证码的生成和验证。
- [lepture/captcha](https://github.com/lepture/captcha) - 生成音频和图像验证码的验证码库。
- [lemonce/svg-captcha](https://github.com/lemonce/svg-captcha) - 在 Node.js 中生成 svg 验证码。
- [DoubleSpout/ccap](https://github.com/DoubleSpout/ccap) - Node.js 使用 c++ 库 CImg 生成验证码，无需安装任何其他库或软件。
- [contra/captchagen](https://github.com/contra/captchagen) - Node.js 的验证码生成。
- [jineshfrancs/CaptchaImageView](https://github.com/jineshfrancs/CaptchaImageView) - 自定义 ImageView 来生成验证码图像。
- [mcxtzhang/SwipeCaptcha](https://github.com/mcxtzhang/SwipeCaptcha) - Android平台刷卡验证码。
- [mojocn/base64Captcha](https://github.com/mojocn/base64Captcha) - Golang base64-captcha 支持数字、数字、字母、算术、音频和数字字母验证码。
- [koto-bank/kocaptcha](https://github.com/koto-bank/kocaptcha) - 一个简单的验证码服务，具有单个 API 端点，用 Rust 编写。
- [Captcheck](https://captcheck.netsyms.com) - 用 PHP 7 和 MySQL 编写的轻量级、自托管验证码服务。使用 Font-Awesome 中的一系列图标。纯文本辅助模式并支持纯键盘操作。
- [Securimage](https://www.phpcaptcha.org) - 开源免费 PHP 验证码脚本。
- [Lokno/click-captcha](https://github.com/Lokno/click-captcha) - 用于人工身份验证的基于点击的可视化验证码。
- [ArgoZhang/SliderCaptcha](https://github.com/ArgoZhang/SliderCaptcha) - 支持移动设备的滑块验证码。


## 裂纹

### 一般
- [arunpatala/captcha](https://github.com/arunpatala/captcha) - 使用火炬破解验证码。
- [zakizhou/CAPTCHA](https://github.com/zakizhou/CAPTCHA) - 在 TensorFlow 中实现验证码分类。
- [nladuo/captcha-break](https://github.com/nladuo/captcha-break) - 基于opencv2、tesseract-ocr和一些机器学习算法的验证码破解。
- [ypwhs/captcha_break](https://github.com/ypwhs/captcha_break) - 使用 CNN 和 Keras 破解验证码。
- [ptigas/simple-captcha-solver](https://github.com/ptigas/simple-captcha-solver) - python 中的简单验证码解算器🐍。
- [rickyhan/SimGAN-Captcha](https://github.com/rickyhan/SimGAN-Captcha) - 无需手动标记训练集即可解决验证码问题。
- [arunpatala/captcha.irctc](https://github.com/arunpatala/captcha.irctc) - 使用深度学习读取 irctc 验证码，准确率高达 98%。
- [JackonYang/captcha-tensorflow](https://github.com/JackonYang/captcha-tensorflow) - 使用 TensorFlow 和 CNN 模型求解图像验证码。
- [skyduy/CNN_keras](https://github.com/skyduy/CNN_keras) - CNN | Keras | CAPTCHA recognition（卷积神经网络、Keras框架、验证码识别）.
- [PatrickLib/captcha_recognize](https://github.com/PatrickLib/captcha_recognize) - 无需图像分割的图像识别验证码。
- [zhengwh/captcha-svm](https://github.com/zhengwh/captcha-svm) - 使用 svm 破解简单的验证码。
- [chxj1992/captcha_cracker](https://github.com/chxj1992/captcha_cracker) - 使用 CNN 破解验证码。
- [chxj1992/slide_captcha_cracker](https://github.com/chxj1992/slide_captcha_cracker) - 使用 Canny 算法破解幻灯片验证码的解决方案。
- [JasonLiTW/simple-railway-captcha-solver#english-version](https://github.com/JasonLiTW/simple-railway-captcha-solver#english-version) - 基于 CNN 的简单验证码求解器和模仿验证码风格的训练集生成器。
- [lllcho/CAPTCHA-breaking](https://github.com/lllcho/CAPTCHA-breaking) - 破解验证码。
- [ecthros/uncaptcha](https://github.com/ecthros/uncaptcha) - 以 85% 的准确率击败 Google 的音频 reCaptcha。
- [dessant/buster](https://github.com/dessant/buster) - 适用于人类和怪物的验证码解算器扩展。
- [kerlomz/captcha_trainer](https://github.com/kerlomz/captcha_trainer) - 基于CNN5/DenseNet+BLSTM/LSTM+CTC实现验证码识别。仅用于训练模型。

### 中文
- [burness/chinese_hand_write_rec](https://github.com/burness/tensorflow-101/tree/master/chinese_hand_write_rec/src) - 手写中文识别。
- [taosir/cnn_handwritten_chinese_recognition](https://github.com/taosir/cnn_handwritten_chinese_recognition) - 顾名思义，handwriting_chinese_recognition 与 cnn.
- [soloice/Chinese-Character-Recognition](https://github.com/soloice/Chinese-Character-Recognition) - 该项目展示了如何使用 CNN 执行汉字识别，这是一项比 MNIST 数字识别复杂得多的任务。
- [muchrooms/zheye](https://github.com/muchrooms/zheye) - 知乎倒立字中文验证码识别程序。
- [aaronshan/12306-captcha](https://github.com/aaronshan/12306-captcha) - 通过深度学习识别12306验证码。
- [nickliqian/cnn_captcha](https://github.com/nickliqian/cnn_captcha) - 使用cnn通过tensorflow识别验证码。


## 工具

- [Tesseract](https://github.com/tesseract-ocr/tesseract) - Tesseract 开源 OCR 引擎。
- [MotionCAPTCHA](https://github.com/wjcrowcroft/MotionCAPTCHA) - MotionCAPTCHA jQuery 插件 - 阻止垃圾邮件、绘制形状。
- [Negative-captcha](https://github.com/subwindow/negative-captcha) - 一个插件，可以让在 Rails 中创建负验证码的过程变得不那么痛苦。
- [Django-simple-captcha](https://github.com/mbi/django-simple-captcha) - 一个极其简单但高度可定制的 Django 应用程序，用于将验证码图像添加到任何 Django 表单。
- [Securimage](https://github.com/dapphp/securimage) - PHP 验证码脚本。
- [Captcha_solver](https://github.com/lorien/captcha_solver) - 验证码解决服务的通用 API。


## 其他

- [VisualCaptcha](https://github.com/emotionLoop/visualCaptcha) - VisualCaptcha 所有不同版本/存储库的集合。
- [Hashcash for PHP/JavaScript forms](https://github.com/007/hashcash-js) - 基于工作量证明的验证码替代方案，用于对抗垃圾邮件。


## 维护者

- [@ZYSzys](https://github.com/ZYSzys)


## 贡献

请这样做！查看 [contributing.md](contributing.md) 文件，或 [打开问题](https://github.com/ZYSzys/awesome-captcha/issues/new)！


## 许可证

[![CC0](http://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

在法律允许的范围内，[ZYSzys](https://github.com/ZYSzys) 已放弃本作品的所有版权以及相关或邻接权。
