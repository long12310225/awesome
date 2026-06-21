# 很棒的 TensorFlow  [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/jtoy/awesome)

精彩的 TensorFlow 实验、库和项目的精选列表。受到令人敬畏的机器学习的启发。

## 什么是 TensorFlow？

TensorFlow 是一个使用数据流图进行数值计算的开源软件库。换句话说，这是构建深度学习模型的最佳方法。

更多信息[此处](http://tensorflow.org)。



## 目录

<!-- MarkdownTOC depth=4 -->
- [Tutorials](#github-tutorials)
- [Models/Projects](#github-projects)
- [由 TensorFlow 提供支持](#github-powered-by)
- [Libraries](#libraries)
- [Tools/Utilities](#tools-utils)
- [Videos](#video)
- [Papers](#papers)
- [博客文章](#blogs)
- [Community](#community)
- [Books](#books)

<!-- /MarkdownTOC -->


<a name="github-tutorials" />

## 教程

* [TensorFlow Tutorial 1](https://github.com/pkmital/tensorflow_tutorials) - 从 TensorFlow 的基础知识到稍微有趣的应用
* [TensorFlow Tutorial 2](https://github.com/nlintz/TensorFlow-Tutorials) - 介绍基于Google的TensorFlow框架的深度学习。这些教程是 Newmu 的 Theano 的直接移植
* [TensorFlow Tutorial 3](https://github.com/Hvass-Labs/TensorFlow-Tutorials) - 这些教程面向深度学习和 TensorFlow 的初学者，其中包含详细记录的代码和 YouTube 视频。
* [TensorFlow Examples](https://github.com/aymericdamien/TensorFlow-Examples) - 适合初学者的 TensorFlow 教程和代码示例
* [Sungjoon's TensorFlow-101](https://github.com/sjchoi86/Tensorflow-101) - 使用 Jupyter Notebook 使用 Python 编写的 TensorFlow 教程
* [Terry Um’s TensorFlow Exercises](https://github.com/terryum/TensorFlow_Exercises) - 重新创建其他 TensorFlow 示例的代码
* [Installing TensorFlow on Raspberry Pi 3](https://github.com/samjabrahams/tensorflow-on-raspberry-pi) - TensorFlow 在 Raspberry Pi 上编译并正常运行
* [Classification on time series](https://github.com/guillaume-chevalier/LSTM-Human-Activity-Recognition) - 使用 LSTM 在 TensorFlow 中对手机传感器数据进行循环神经网络分类
* [Getting Started with TensorFlow on Android](https://omid.al/posts/2017-02-20-Tutorial-Build-Your-First-Tensorflow-Android-App.html) - 构建您的第一个 TensorFlow Android 应用
* [Predict time series](https://github.com/guillaume-chevalier/seq2seq-signal-prediction) - 学习在简单数据集上使用 seq2seq 模型作为对该架构提供的大量可能性的介绍
* [Single Image Random Dot Stereograms](https://github.com/Mazecreator/TensorFlow-SIRDS) - SIRDS 是一种在 2D 图像中呈现 3D 数据的方法。它允许瀑布式图的科学数据显示，没有因透视而隐藏的线。
* [CS20 SI: TensorFlow for DeepLearning Research](http://web.stanford.edu/class/cs20si/syllabus.html) - 斯坦福大学 2017 年 Tensorflow 课程 - [教学大纲](http://web.stanford.edu/class/cs20si/syllabus.html) - [非官方视频](https://youtu.be/g-EvyKpZjmQ?list=PLSPPwKHXGS2110rEaNH7amFGmaD5hsObs)
* [TensorFlow World](https://github.com/astorfi/TensorFlow-World) - 提供了简洁且即用型 TensorFlow 教程以及详细的文档。
* [Effective Tensorflow](https://github.com/vahidk/EffectiveTensorflow) - TensorFlow 操作指南和最佳实践。涵盖基础知识和高级主题。
* [TensorLayer](http://tensorlayer.readthedocs.io/en/latest/user/tutorial.html) - TensorFlow官方教程的模块化实现。 ([CN](https://tensorlayercn.readthedocs.io/zh/latest/user/tutorial.html))。
* [了解 Tensorflow Estimator API](https://www.lighttag.io/blog/tensorflow-estimator-api/) Estimator API 的概念概述、何时使用以及为何使用。
* [Introduction to TensorFlow for Artificial Intelligence, Machine Learning, and Deep Learning](https://www.coursera.org/learn/introduction-tensorflow) - Coursera 提供的 Tensorflow 简介
* [Convolutional Neural Networks in TensorFlow](https://www.coursera.org/learn/convolutional-neural-networks-tensorflow) - Tensorflow 中的卷积神经网络，由 Coursera 提供
* [TensorLayerX](https://tensorlayerx.readthedocs.io/en/latest/index.html#user-guide) - 像 PyTorch 一样使用 TensorFlow。 ([Api 文档](https://tensorlayerx.readthedocs.io/en/latest/index.html#))

<a name="github-projects" />

## 模型/项目

* [Tensorflow-Project-Template](https://github.com/Mrgemy95/Tensorflow-Project-Template) - 适合您的张量流项目的简单且设计良好的模板。
* [Domain Transfer Network](https://github.com/yunjey/dtn-tensorflow) - 无监督跨域图像生成的实现
* [Show, Attend and Tell](https://github.com/yunjey/show_attend_and_tell) - 基于注意力的图像标题生成器
* [Neural Style](https://github.com/cysmith/neural-style-tf) 神经风格的实现
* [SRGAN](https://github.com/tensorlayer/srgan) - 使用生成对抗网络的逼真单图像超分辨率
* [Pretty Tensor](https://github.com/google/prettytensor) - Pretty Tensor 提供了高级构建器 API
* [Neural Style](https://github.com/anishathalye/neural-style) - 神经风格的实现
* [AlexNet3D](https://github.com/denti/AlexNet3D) - AlexNet3D 的实现。简单的 AlexNet 模型，但具有 3D 卷积层 (conv3d)。
* [TensorFlow White Paper Notes](https://github.com/samjabrahams/tensorflow-white-paper-notes) - TensorFlow 白皮书的注释和摘要，以及 SVG 图形和文档链接
* [NeuralArt](https://github.com/ckmarkoh/neuralart_tensorflow) - 艺术风格神经算法的实现
* [Generative Handwriting Demo using TensorFlow](https://github.com/hardmaru/write-rnn-tensorflow) - 尝试实现 Alex Graves 论文中的随机手写生成部分
* [Neural Turing Machine in TensorFlow](https://github.com/carpedm20/NTM-tensorflow) - 神经图灵机的实现
* [GoogleNet Convolutional Neural Network Groups Movie Scenes By Setting](https://github.com/agermanidis/thingscoop) - 根据视频中出现的对象、地点和其他内容搜索、过滤和描述视频
* [Neural machine translation between the writings of Shakespeare and modern English using TensorFlow](https://github.com/tokestermw/tensorflow-shakespeare) - 这执行单语言翻译，从现代英语到莎士比亚，反之亦然。
* [Chatbot](https://github.com/Conchylicultor/DeepQA) - [“神经对话模型”]的实现(http://arxiv.org/abs/1506.05869)
* [Seq2seq-Chatbot](https://github.com/tensorlayer/seq2seq-chatbot) - 200 行代码的聊天机器人
* [DCGAN](https://github.com/tensorlayer/dcgan) - 深度卷积生成对抗网络
* [GAN-CLS](https://github.com/zsdonghao/text-to-image) - 生成对抗性文本到图像合成
* [im2im](https://github.com/zsdonghao/Unsup-Im2Im) - 使用生成对抗网络进行无监督图像到图像转换
* [Improved CycleGAN](https://github.com/luoxier/CycleGAN_Tensorlayer) - 未配对的图像到图像翻译
* [DAGAN](https://github.com/nebulaV/DAGAN) - 快速压缩感知 MRI 重建
* [Colornet - Neural Network to colorize grayscale images](https://github.com/pavelgonchar/colornet) - 神经网络对灰度图像进行着色
* [Neural Caption Generator](https://github.com/jazzsaxmafia/show_attend_and_tell.tensorflow) - 实施[“展示和讲述”](http://arxiv.org/abs/1411.4555)
* [Neural Caption Generator with Attention](https://github.com/jazzsaxmafia/show_attend_and_tell.tensorflow) - 实施[“展示、出席和讲述”](http://arxiv.org/abs/1502.03044)
* [Weakly_detector](https://github.com/jazzsaxmafia/Weakly_detector) - [“学习深度特征以实现判别性本地化”](http://cnnlocalization.csail.mit.edu/) 的实现
* [Dynamic Capacity Networks](https://github.com/jazzsaxmafia/dcn.tf) - 实施[“动态容量网络”](http://arxiv.org/abs/1511.07838)
* [HMM in TensorFlow](https://github.com/dwiel/tensorflow_hmm) - HMM 的维特比和前向/后向算法的实现
* [DeepOSM](https://github.com/trailbehind/DeepOSM) - 使用 OpenStreetMap 功能和卫星图像训练 TensorFlow 神经网络。
* [DQN-tensorflow](https://github.com/devsisters/DQN-tensorflow) - Devsisters.com 与 OpenAI Gym 一起使用 TensorFlow 实现 DeepMind 的“通过深度强化学习进行人类级控制”
* [Policy Gradient](https://github.com/zsdonghao/tensorlayer/blob/master/example/tutorial_atari_pong.py) - 玩 Atari 乒乓球
* [Deep Q-Network](https://github.com/zsdonghao/tensorlayer/blob/master/example/tutorial_frozenlake_dqn.py) - 用于玩冰湖游戏
* [AC](https://github.com/zsdonghao/tensorlayer/blob/master/example/tutorial_cartpole_ac.py) - 玩离散动作空间游戏（Cartpole）的演员评论家
* [A3C](https://github.com/zsdonghao/tensorlayer/blob/master/example/tutorial_bipedalwalker_a3c_continuous_action.py) - 连续动作空间的异步优势 Actor Critic (A3C)（Bipedal Walker）
* [DAGGER](https://github.com/zsdonghao/Imitation-Learning-Dagger-Torcs) - 用于玩[Gym Torcs](https://github.com/ugo-nama-kun/gym_torcs)
* [TRPO](https://github.com/jjkke88/RL_toolbox) - 对于连续和离散动作空间
* [Highway Network](https://github.com/fomorians/highway-cnn) - [“训练非常深的网络”](http://arxiv.org/abs/1507.06228) 的 TensorFlow 实现以及[博客文章](https://medium.com/jim-fleming/highway-networks-with-tensorflow-1e6dfa667daa#.ndicn1i27)
* [Hierarchical Attention Networks](https://github.com/tqtg/hierarchical-attention-networks) - [“用于文档分类的分层注意力网络”](https://www.cs.cmu.edu/~hovy/papers/16HLT-hierarchical-attention-networks.pdf) 的 TensorFlow 实现
* [Sentence Classification with CNN](https://github.com/dennybritz/cnn-text-classification-tf) - [“用于句子分类的卷积神经网络”](http://arxiv.org/abs/1408.5882) 的 TensorFlow 实现以及[博客文章](http://www.wildml.com/2015/12/implementing-a-cnn-for-text-classification-in-tensorflow/)
* [End-To-End Memory Networks](https://github.com/domluna/memn2n) - [端到端记忆网络]的实现(http://arxiv.org/abs/1503.08895)
* [Character-Aware Neural Language Models](https://github.com/carpedm20/lstm-char-cnn-tensorflow) - [字符感知神经语言模型]的 TensorFlow 实现(http://arxiv.org/abs/1508.06615)
* [YOLO TensorFlow ++](https://github.com/thtrieu/yolotf) - “YOLO：实时对象检测”的 TensorFlow 实现，经过训练并实际支持在移动设备上实时运行。
* [Wavenet](https://github.com/ibab/tensorflow-wavenet) - 这是用于音频生成的 [WaveNet 生成神经网络架构](https://deepmind.com/blog/wavenet-generative-model-raw-audio/) 的 TensorFlow 实现。
* [Mnemonic Descent Method](https://github.com/trigeorgis/mdm) - Tensorflow 实现 [“助记词下降法：用于端到端人脸对齐的循环过程”](http://ibug.doc.ic.ac.uk/media/uploads/documents/trigeorgis2016mnemonic.pdf)
* [CNN visualization using Tensorflow](https://github.com/InFoCusp/tf_cnnvis) - [“可视化和理解卷积网络”](https://www.cs.nyu.edu/~fergus/papers/zeilerECCV2014.pdf) 的 Tensorflow 实现
* [VGAN Tensorflow](https://github.com/Singularity42/VGAN-Tensorflow) - Vondrick 等人在 MIT 的 Tensorflow 实现 [“使用场景动态生成视频”](http://carlvondrick.com/tinyvideo/)。
* [3D Convolutional Neural Networks in TensorFlow](https://github.com/astorfi/3D-convolutional-speaker-recognition) - Torfi 等人在 TensorFlow 中实现了[“用于说话人验证应用的 3D 卷积神经网络”](https://arxiv.org/abs/1705.09422)。
* [U-Net](https://github.com/zsdonghao/u-net-brain-tumor) - 用于脑肿瘤分割
* [Spatial Transformer Networks](https://github.com/zsdonghao/Spatial-Transformer-Nets) - 学习变换函数
* [Lip Reading - Cross Audio-Visual Recognition using 3D Architectures in TensorFlow](https://github.com/astorfi/lip-reading-deeplearning) - Torfi 等人的 [“使用深度学习在野外进行跨视听识别”](https://arxiv.org/abs/1706.05739) 的 TensorFlow 实现
* [Attentive Object Tracking](https://github.com/akosiorek/hart) - 实施[“分层注意力循环跟踪”](https://arxiv.org/abs/1706.09262)
* [Holographic Embeddings for Graph Completion and Link Prediction](https://github.com/laxatives/TensorFlow-TransX) - 【知识图谱全息嵌入】的实现(http://arxiv.org/abs/1510.04935)
* [Unsupervised Object Counting](https://github.com/akosiorek/attend_infer_repeat) - [“参加、推理、重复”](https://papers.nips.cc/paper/6230-attend-infer-repeat-fast-scene-understanding-with-generative-models)的实施
* [Tensorflow FastText](https://github.com/apcode/tensorflow_fasttext) - 一个简单的基于嵌入的文本分类器，灵感来自 Facebook 的 fastText。
* [MusicGenreClassification](https://github.com/mlachmish/MusicGenreClassification) - 使用神经网络对 10 秒声音流中的音乐流派进行分类。
* [Kubeflow](https://github.com/kubeflow/kubeflow) - 用于轻松将 Tensorflow 与 Kubernetes 结合使用的框架。
* [TensorNets](https://github.com/taehoonlee/tensornets) - 40 多个带有预先训练权重的流行计算机视觉模型。
* [Ladder Network](https://github.com/divamgupta/ladder_network_keras) - 在 Keras 和 Tensorflow 中实现半监督学习的阶梯网络
* [TF-Unet](https://github.com/juniorxsound/TF-Unet) - 在 Keras 中实现的通用 U 网络用于图像分割
* [Sarus TF2 Models](https://github.com/sarus-tech/tf2-published-models) - 以干净、易于重用的 Tensorflow 2 代码实现的一长串最新生成模型（普通自动编码器、VAE、VQ-VAE、PixelCNN、门控 PixelCNN、PixelCNN++、PixelSNAIL、条件神经过程）。
* [Model Maker](https://www.tensorflow.org/lite/guide/model_maker) - 一个迁移学习库，可简化 TensorFlow Lite 模型的训练、评估和部署过程（支持：图像分类、对象检测、文本分类、BERT 问答、音频分类、推荐等；[API 参考](https://www.tensorflow.org/lite/api_docs/python/tflite_model_maker)）。


<a name="github-powered-by" />

## 由 TensorFlow 提供支持

* [YOLO TensorFlow](https://github.com/gliese581gg/YOLO_tensorflow) - “YOLO：实时目标检测”的实现
* [android-yolo](https://github.com/natanielruiz/android-yolo) - 使用由 TensorFlow 提供支持的 YOLO 网络在 Android 上进行实时对象检测。
* [Magenta](https://github.com/tensorflow/magenta) - 研究项目旨在推进音乐和艺术生成机器智能的最先进水平


<a name="libraries" />

## 图书馆

* [TensorFlow Estimators](https://www.tensorflow.org/guide/estimators) - 高级 TensorFlow API，极大地简化了机器学习编程（最初是 [tensorflow/skflow](https://github.com/tensorflow/skflow)）
* [R Interface to TensorFlow](https://tensorflow.rstudio.com/) - R 与 TensorFlow API 的接口，包括估算器、Keras、数据集等。
* [Lattice](https://github.com/tensorflow/lattice) - 在 TensorFlow 中实现单调校准插值查找表
* [tensorflow.rb](https://github.com/somaticio/tensorflow.rb) - 使用 SWIG 的 TensorFlow 本机接口
* [tflearn](https://github.com/tflearn/tflearn) - 具有更高级别 API 的深度学习库
* [TensorLayer](https://github.com/tensorlayer/tensorlayer) - 为研究人员和工程师提供的深度学习和强化学习库
* [TensorFlow-Slim](https://github.com/tensorflow/models/tree/master/inception/inception/slim) - 用于定义模型的高级库
* [TensorFrames](https://github.com/tjhunter/tensorframes) - Apache Spark 的 TensorFlow 绑定
* [TensorForce](https://github.com/reinforceio/tensorforce) - TensorForce：用于应用强化学习的 TensorFlow 库
* [TensorFlowOnSpark](https://github.com/yahoo/TensorFlowOnSpark) - 来自雅虎的倡议！使用 Apache Spark 启用分布式 TensorFlow。
* [caffe-tensorflow](https://github.com/ethereon/caffe-tensorflow) - 将 Caffe 模型转换为 TensorFlow 格式
* [keras](http://keras.io) - 适用于 TensorFlow 和 Theano 的最小模块化深度学习库
* [SyntaxNet: Neural Models of Syntax](https://github.com/tensorflow/models/tree/master/syntaxnet) - [Globally Normalized Transition-Based Neural Networks, Andor et al. 中描述的模型的 TensorFlow 实现。 （2016）]（http://arxiv.org/pdf/1603.06042.pdf）
* [keras-js](https://github.com/transcranial/keras-js) - 在浏览器中运行 Keras 模型（张量流后端），并支持 GPU
* [NNFlow](https://github.com/welschma/NNFlow) - 简单的框架允许通过将 ROOT NTuples 转换为 Numpy 数组来读入它们，然后在 Google Tensorflow 中使用它们。
* [Sonnet](https://github.com/deepmind/sonnet) - Sonnet 是 DeepMind 的库，构建在 TensorFlow 之上，用于构建复杂的神经网络。
* [tensorpack](https://github.com/ppwwyyxx/tensorpack) - TensorFlow 上的神经网络工具箱专注于训练速度和大型数据集。
* [tf-encrypted](https://github.com/mortendahl/tf-encrypted) - TensorFlow 之上的层，用于对加密数据进行机器学习
* [pytorch2keras](https://github.com/nerox8664/pytorch2keras) - 将 PyTorch 模型转换为 Keras（带有 TensorFlow 后端）格式
* [gluon2keras](https://github.com/stjordanis/gluon2keras) - 将 Gluon 模型转换为 Keras（带有 TensorFlow 后端）格式
* [TensorIO](https://doc-ai.github.io/tensorio/) - 用于将 TensorFlow Lite 模型部署到移动设备的轻量级跨平台库。
* [StellarGraph](https://github.com/stellargraph/stellargraph) - Machine Learning on Graphs，一个用于对图结构（网络结构）数据进行机器学习的 Python 库。
* [DeepBay](https://github.com/ElPapi42/DeepBay) - 用于实现通用架构堆栈的高级 Keras 补充，作为易于使用的即插即用模块
* [Tensorflow-Probability](https://www.tensorflow.org/probability) - 基于 TensorFlow 构建的概率编程可以轻松地将概率模型和深度学习在现代硬件上结合起来。
* [TensorLayerX](https://github.com/tensorlayer/TensorLayerX) - TensorLayerX：适用于所有硬件、后端和操作系统（包括 TensorFlow）的统一深度学习框架。
* [Txeo](https://github.com/rdabra/txeo) - TensorFlow 的现代 C++ 包装器。

<a name="tools-utils" />

## 工具/实用程序

* [Speedster](https://github.com/nebuly-ai/nebullvm/tree/main/apps/accelerate/speedster) - 自动应用 SOTA 优化技术，以在您的硬件上实现最大的推理加速。
* [Guild AI](https://guild.ai) - TensorFlow 的任务运行器和包管理器
* [ML Workspace](https://github.com/ml-tooling/ml-workspace) - 用于机器学习和数据科学的一体化 Web IDE。将 Tensorflow、Jupyter、VS Code、Tensorboard 和许多其他工具/库组合到一个 Docker 映像中。
* [create-tf-app](https://github.com/radi-cho/create-tf-app) - Tensorflow 项目构建器命令行工具，涵盖环境管理、linting 和日志记录。

<a name="video" />

## 视频

* [TensorFlow Guide 1](http://bit.ly/1OX8s8Y) - 安装和使用指南
* [TensorFlow Guide 2](http://bit.ly/1R27Ki9) - 第一个视频的继续
* [TensorFlow Basic Usage](http://bit.ly/1TCNmEY) - 基本用法指南
* [TensorFlow Deep MNIST for Experts](http://bit.ly/1L9IfJx) - 深入探讨 MNIST
* [TensorFlow Udacity Deep Learning](https://www.youtube.com/watch?v=ReaxoSIM5XQ) - 在具有 1Gb 数据的 Cloud 9 在线服务上免费安装 TensorFlow 的基本步骤
* [为什么 Google 希望每个人都能使用 TensorFlow](http://video.foxnews.com/v/4611174773001/why-google-wants-everyone-to-have-access-to-tensorflow/?#sp=show-clips)
* [TensorFlow 硅谷聚会视频 2016 年 1 月 19 日](http://blog.altoros.com/videos-from-tensorflow-silicon-valley-meetup-january-19-2016.html)
* [TensorFlow 硅谷聚会视频 2016 年 1 月 21 日](http://blog.altoros.com/videos-from-tensorflow-seattle-meetup-jan-21-2016.html)
* [Stanford CS224d Lecture 7 - Introduction to TensorFlow, 19th Apr 2016](https://www.youtube.com/watch?v=L8Y2_Cq2X5s&index=7&list=PLmImxx8Char9Ig0ZHSyTqGsdhb9weEGam) - CS224d 自然语言处理深度学习作者：Richard Socher
* [Diving into Machine Learning through TensorFlow](https://youtu.be/GZBIPwdGtkk?list=PLBkISg6QfSX9HL6us70IBs9slFciFFa4W) - Pycon 2016 俄勒冈州波特兰，[幻灯片](https://storage.googleapis.com/amy-jo/talks/tf-workshop.pdf) 和 [代码](https://github.com/amygdala/tensorflow-workshop)，作者：Julia Ferraioli、Amy Unruh、Eli Bixby
* [Large Scale Deep Learning with TensorFlow](https://youtu.be/XYwIDn00PAo) - 2016 年 Spark 峰会杰夫·迪恩 (Jeff Dean) 的主题演讲
* [Tensorflow and deep learning - without at PhD](https://www.youtube.com/watch?v=vq2nnJ4g6N0) - 作者：马丁·戈尔纳
* [Tensorflow and deep learning - without at PhD, Part 2 (Google Cloud Next '17)](https://www.youtube.com/watch?v=fTUwdXUFfI8) - 作者：马丁·戈尔纳
* [Image recognition in Go using TensorFlow](https://youtu.be/P8MZ1Z2LHrw) - 通过亚历克斯·普柳托



<a name="papers" />

## 论文

* [TensorFlow: Large-Scale Machine Learning on Heterogeneous Distributed Systems](http://download.tensorflow.org/paper/whitepaper2015.pdf) - 本文描述了 TensorFlow 接口以及我们在 Google 构建的该接口的实现
* [TensorFlow Estimators：管理高级机器学习框架中的简单性与灵活性](https://arxiv.org/pdf/1708.02637.pdf)
* [TF.Learn：TensorFlow 的分布式机器学习高级模块](https://arxiv.org/abs/1612.04251)
* [Comparative Study of Deep Learning Software Frameworks](http://arxiv.org/abs/1511.06435) - 这项研究是在几种类型的深度学习架构上进行的，我们评估了在单台机器上使用上述框架（多线程）CPU 和 GPU (Nvidia Titan X) 设置时的性能
* [Distributed TensorFlow with MPI](http://arxiv.org/abs/1603.02339) - 在本文中，我们扩展了最近提出的 Google TensorFlow，以便使用消息传递接口 (MPI) 在大规模集群上执行
* [Globally Normalized Transition-Based Neural Networks](http://arxiv.org/abs/1603.06042) - 本文描述了 [SyntaxNet](https://github.com/tensorflow/models/tree/master/syntaxnet) 背后的模型。
* [TensorFlow: A system for large-scale machine learning](https://arxiv.org/abs/1605.08695) - 本文描述了 TensorFlow 数据流模型与现有系统的对比，并展示了引人注目的性能
* [TensorLayer: A Versatile Library for Efficient Deep Learning Development](https://arxiv.org/abs/1707.08551) - 本文描述了一个多功能的 Python 库，旨在帮助研究人员和工程师高效地开发深度学习系统。 （2017年ACM MM最佳开源软件奖获得者）

<a name="blogs" />

## 官方公告

* [TensorFlow: smarter machine learning, for everyone](https://googleblog.blogspot.com/2015/11/tensorflow-smarter-machine-learning-for.html) - TensorFlow 简介
* [Announcing SyntaxNet: The World’s Most Accurate Parser Goes Open Source](http://googleresearch.blogspot.com/2016/05/announcing-syntaxnet-worlds-most.html) - 发布 SyntaxNet，“一个在 TensorFlow 中实现的开源神经网络框架，为自然语言理解系统提供了基础。

## 博客文章
* [官方 Tensorflow 博客](http://blog.tensorflow.org/)
* [为什么 TensorFlow 将改变 AI 游戏规则](https://archive.fo/o9asj)
* [TensorFlow for Poets](http://petewarden.com/2016/02/28/tensorflow-for-poets) - 回顾 TensorFlow 的实现
* [Introduction to Scikit Flow - Simplified Interface to TensorFlow](http://terrytangyuan.github.io/2016/03/14/scikit-flow-intro/) - 主要特点图示
* [Building Machine Learning Estimator in TensorFlow](http://terrytangyuan.github.io/2016/07/08/understand-and-build-tensorflow-estimator/) - 了解 TensorFlow Learn 估算器的内部结构
* [TensorFlow - 不仅仅用于深度学习](http://terrytangyuan.github.io/2016/08/06/tensorflow-not-just-deep-learning/)
* [indico 机器学习团队对 TensorFlow 的看法](https://indico.io/blog/indico-tensorflow)
* [The Good, Bad, & Ugly of TensorFlow](https://indico.io/blog/the-good-bad-ugly-of-tensorflow/) - 对六个月快速演变的调查（+ 技巧/技巧和修复丑陋问题的代码），Dan Kuster，Indico，2016 年 5 月 9 日
* [Fizz Buzz in TensorFlow](http://joelgrus.com/2016/05/23/fizz-buzz-in-tensorflow/) - 乔尔·格鲁斯的笑话
* [RNNs In TensorFlow, A Practical Guide And Undocumented Features](http://www.wildml.com/2016/08/rnns-in-tensorflow-a-practical-guide-and-undocumented-features/) - GitHub 上包含完整代码示例的分步指南。
* [使用 TensorBoard 在 TensorFlow 中可视化图像分类再训练](http://maxmelnick.com/2016/07/04/visualizing-tensorflow-retrain.html)
* [TFRecords 指南](http://warmspringwinds.github.io/tensorflow/tf-slim/2016/12/21/tfrecords-guide/) 语义分割和处理 TFRecord 文件格式。
* [TensorFlow Android Guide](https://blog.mindorks.com/android-tensorflow-machine-learning-example-ff0e9b2654cc) - Android TensorFlow 机器学习示例。
* [TensorFlow Optimizations on Modern Intel® Architecture](https://software.intel.com/en-us/articles/tensorflow-optimizations-on-modern-intel-architecture) - 基于英特尔/Google 合作，在基于英特尔® 至强® 和英特尔® 至强融核™ 处理器的平台上引入 TensorFlow 优化。
* [可口可乐的图像识别应用程序](https://developers.googleblog.com/2017/09/how-machine-learning-with-tensorflow.html)可口可乐的产品代码图像识别神经网络，具有用户输入反馈循环。
* [TensorFlow 是如何工作的](https://www.letslearnai.com/2018/02/02/how-does-the-machine-learning-library-tensorflow-work.html) 机器学习库 TensorFlow 是如何工作的？


<a name="community" />

## 社区

* [堆栈溢出](http://stackoverflow.com/questions/tagged/tensorflow)
* [推特上的 @TensorFlow](https://twitter.com/tensorflow)
* [Reddit](https://www.reddit.com/r/tensorflow)
* [邮件列表](https://groups.google.com/a/tensorflow.org/forum/#!forum/discuss)


<a name="books" />

## 书籍

* [使用 TensorFlow 进行机器学习第二版]([http://tensorflowbook.com](https://github.com/chrismattmann/MLwithTensorFlow2ed)) 作者：[Dr. Chris A. Mattmann](http://github.com/chrismattmann/)，加州大学洛杉矶分校首席数据和人工智能官，也是《Tika in Action》(https://www.manning.com/books/tika-in-action)一书的作者。这本书使人工智能和机器学习这个数学密集的话题对新手来说变得平易近人、实用。更新到Tensorflow2和本书的最新版本。
* [第一次接触 TensorFlow](http://www.jorditorres.org/first-contact-with-tensorflow/) 作者：Jordi Torres，UPC 巴塞罗那理工学院教授、巴塞罗那超级计算中心研究经理和高级顾问
* [Deep Learning with Python](https://machinelearningmastery.com/deep-learning-with-python/) - 使用 Keras 在 Theano 和 TensorFlow 上开发深度学习模型 作者：Jason Brownlee
* [TensorFlow for Machine Intelligence](https://bleedingedgepress.com/tensor-flow-for-machine-intelligence/) - 使用 TensorFlow 的完整指南，从图计算基础知识到深度学习模型，再到在生产环境中使用它 - Bleeding Edge Press
* [Getting Started with TensorFlow](https://www.packtpub.com/big-data-and-business-intelligence/getting-started-tensorflow) - 启动并运行 Google 最新的数值计算库，深入研究您的数据，作者：Giancarlo Zaccone
* [Hands-On Machine Learning with Scikit-Learn and TensorFlow](http://shop.oreilly.com/product/0636920052289.do) - 作者：Aurélien Geron，YouTube 视频分类团队前负责人。涵盖 ML 基础知识、使用 TensorFlow、最新的 CNN、RNN 和自动编码器架构以及强化学习 (Deep Q) 跨多个服务器和 GPU 训练和部署深度网络。
* [Building Machine Learning Projects with Tensorflow](https://www.packtpub.com/big-data-and-business-intelligence/building-machine-learning-projects-tensorflow) - 鲁道夫·博宁。本书涵盖了 TensorFlow 中的各种项目，揭示了 TensorFlow 在不同场景中可以做什么。本书提供了有关训练模型、机器学习、深度学习以及使用各种神经网络的项目。每个项目都是一项引人入胜且富有洞察力的练习，将教您如何使用 TensorFlow，并向您展示如何通过使用张量来探索数据层。
* [Deep Learning using TensorLayer](http://www.broadview.com.cn/book/5059) - 董浩等人。本书涵盖了深度学习以及使用 TensorFlow 和 TensorLayer 的实现。
* [TensorFlow 2.0 in Action](https://www.manning.com/books/tensorflow-in-action) - 作者：Thushan Ganegedara。这本使用 TensorFlow 2.0 新功能构建深度学习模型的实用指南充满了引人入胜的项目、简单的语言和最新算法的覆盖范围。
* [Probabilistic Programming and Bayesian Methods for Hackers](https://github.com/CamDavidsonPilon/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers) - 作者：卡梅伦·戴维森·皮隆。介绍使用张量流概率（或者 PyMC2/3）的贝叶斯方法和概率图形模型。



<a name="contributions" />

## 贡献

随时欢迎您的贡献！

如果您想对此列表做出贡献（请这样做），请向我发送拉取请求或联系我 [@jtoy](https://twitter.com/jtoy)
此外，如果您发现由于以下任一原因应弃用上面列出的任何存储库：

* 存储库的所有者明确表示“该库未维护”。
* 长期不承诺（2~3年）。

有关[指南]的更多信息(https://github.com/jtoy/awesome-tensorflow/blob/master/contributing.md)


<a name="credits" />

## 制作人员

* 一些 python 库是从 [vinta](https://github.com/vinta/awesome-python) 剪切并粘贴的
* 我从[此页面]（https://code.google.com/p/go-wiki/wiki/Projects#Machine_Learning）中找到的一些参考资料

