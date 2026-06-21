# [精彩的深度学习资源](https://github.com/guillaume-chevalier/Awesome-Deep-Learning-Resources) [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

这是我最喜欢的深度学习资源的粗略列表。它对我学习如何进行深度学习很有用，我用它来重温主题或作为参考。
我（[Guillaume Chevalier](https://github.com/guillaume-chevalier)）建立了这个列表，并仔细阅读了此处列出的所有内容。


## 内容

- [Trends](#trends)
- [在线课程](#online-classes)
- [Books](#books)
- [帖子和文章](#posts-and-articles)
- [实用资源](#practical-resources)
  - [库和实现](#librairies-and-implementations)
  - [一些数据集](#some-datasets)
- [其他数学理论](#other-math-theory)
  - [梯度下降算法和优化](#gradient-descent-algorithms-and-optimization)
  - [复数和数字信号处理](#complex-numbers-and-digital-signal-processing)
- [Papers](#papers)
  - [循环神经网络](#recurrent-neural-networks)
  - [卷积神经网络](#convolutional-neural-networks)
  - [注意力机制](#attention-mechanisms)
  - [Other](#other)
- [YouTube 和视频](#youtube)
- [杂项。枢纽和链接](#misc-hubs-and-links)
- [License](#license)

<a name="trends" />

## 趋势

以下是从 2004 年至今（2017 年 9 月）的历史 [Google 趋势](https://www.google.ca/trends/explore?date=all&q=machine%20learning,deep%20learning,data%20science,computer%20programming)：
<p对齐=“中心”>
  <img src="google_trends.png" width="792" height="424" />
</p>

您可能还想查看 Andrej Karpathy 关于机器学习研究趋势的 [新帖子](https://medium.com/@karpathy/a-peek-at-trends-in-machine-learning-ab8a1085a106)。

我相信深度学习是让计算机更像人类思考的关键，并且具有很大的潜力。一些困难的自动化任务可以通过它轻松解决，而这在早期使用经典算法是不可能实现的。

由于原子晶体管尺寸的物理限制，关于计算机科学硬件指数进步率的摩尔定律现在对 GPU 的影响比对 CPU 的影响更大。我们正在转向并行架构
[[阅读更多](https://www.quora.com/Does-Moores-law-apply-to-GPUs-Or-only-CPUs)]。深度学习通过使用 GPU 在底层利用并行架构。最重要的是，深度学习算法未来可能会使用量子计算并应用于机器脑接口。

我发现智力和认知的关键是一个非常有趣的探索课题，但目前还没有被很好地理解。这些技术很有前景。


<a name="online-classes" />

## 在线课程

- **[DL&RNN 课程](https://www.dl-rnn-course.neuraxio.com/start?utm_source=github_awesome) - 我创建了这门关于深度学习和循环神经网络的内容丰富的密集课程。**
- [Machine Learning by Andrew Ng on Coursera](https://www.coursera.org/learn/machine-learning) - 知名入门级在线课程，拥有[证书](https://www.coursera.org/account/accomplishments/verify/DXPXHYFNGKG3)。授课人：Andrew Ng，斯坦福大学副教授；百度首席科学家； Coursera 主席兼联合创始人。
- [Deep Learning Specialization by Andrew Ng on Coursera](https://www.coursera.org/specializations/deep-learning) - Andrew Ng 的新系列 5 门深度学习课程，现在使用 Python，而不是 Matlab/Octave，并获得[专业证书](https://www.coursera.org/account/accomplishments/specialization/U7VNC3ZD9YD8)。
- [Deep Learning by Google](https://www.udacity.com/course/deep-learning--ud730) - 很好的中级到高级课程，涵盖高级深度学习概念，我发现一旦掌握了基础知识，它就有助于发挥创造力。
- [Machine Learning for Trading by Georgia Tech](https://www.udacity.com/course/machine-learning-for-trading--ud501) - 有趣的课程，用于获取应用于交易的机器学习基础知识以及一些人工智能和金融概念。我特别喜欢 Q-Learning 部分。
- [Neural networks class by Hugo Larochelle, Université de Sherbrooke](https://www.youtube.com/playlist?list=PL6Xpj9I5qXYEcOhn7TqghAJ6NAPrNmUBH) - Hugo Larochelle 在线免费提供有关神经网络的有趣课程，但我已经观看了其中一些视频。
- [GLO-4030/7030 Apprentissage par réseaux de neurones profonds](https://ulaval-damas.github.io/glo4030/) - 这是拉瓦尔大学教授 Philippe Giguère 教授的课程。我特别发现它对多头注意力机制的罕见可视化非常棒，可以在[第 13 周课程的第 28 张幻灯片](http://www2.ift.ulaval.ca/~pgiguere/cours/DeepLearning/09-Attention.pdf) 中进行思考。
- [Deep Learning & Recurrent Neural Networks (DL&RNN)](https://www.neuraxio.com/en/time-series-solution) - 关于深度学习和递归神经网络主题的最丰富、最密集的加速课程（滚动到最后）。

<a name="books" />

## 书籍

- [Clean Code](https://www.amazon.ca/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882) - 回到基础知识你这个傻瓜！了解如何为您的职业生涯打造干净的代码。这是迄今为止我读过的最好的书，即使这个列表与深度学习相关。
- [Clean Coder](https://www.amazon.ca/Clean-Coder-Conduct-Professional-Programmers/dp/0137081073) - 了解如何成为专业的程序员以及如何与经理互动。这对于任何编码职业都很重要。
- [How to Create a Mind](https://www.amazon.com/How-Create-Mind-Thought-Revealed/dp/B009VSFXZ4) - 音频版本很适合在通勤时听。这本书激发了人们对思维进行逆向工程并思考如何编写人工智能代码。
- [Neural Networks and Deep Learning](http://neuralnetworksanddeeplearning.com/index.html) - 本书涵盖了神经网络和深度学习背后的许多核心概念。
- [Deep Learning - An MIT Press book](http://www.deeplearningbook.org/) - 然而，在本书的一半部分，它包含了关于如何思考实际深度学习的令人满意的数学内容。
- [Some other books I have read](https://books.google.ca/books?hl=en&as_coll=4&num=100&uid=103409002069648430166&source=gbs_slider_cls_metadata_4_mylibrary_title) - 这里列出的一些书籍与深度学习关系不大，但在某种程度上仍然与此列表相关。

<a name="posts-and-articles" />

## 帖子和文章

- [Predictions made by Ray Kurzweil](https://en.wikipedia.org/wiki/Predictions_made_by_Ray_Kurzweil) - 雷·库兹韦尔 (Ray Kurzweil) 做出的中长期未来预测列表。
- [The Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) - 必须阅读 Andrej Karpathy 的文章——这就是我学习 RNN 的动力，它展示了 RNN 在最基本的 NLP 形式中可以实现的目标。
- [Neural Networks, Manifolds, and Topology](http://colah.github.io/posts/2014-03-NN-Manifolds-Topology/) - 重新审视神经元如何映射信息。
- [Understanding LSTM Networks](http://colah.github.io/posts/2015-08-Understanding-LSTMs/) - 解释了 LSTM 单元的内部工作原理，此外，结论中还包含有趣的链接。
- [Attention and Augmented Recurrent Neural Networks](http://distill.pub/2016/augmented-rnns/) - 对于视觉动画来说很有趣，它是对注意力机制的一个很好的介绍。
- [Recommending music on Spotify with deep learning](http://benanne.github.io/2014/08/05/spotify-cnns.html) - 非常适合对音频进行聚类 - 由 Spotify 的实习生发布。
- [Announcing SyntaxNet: The World’s Most Accurate Parser Goes Open Source](https://research.googleblog.com/2016/05/announcing-syntaxnet-worlds-most.html) - Parsey McParseface 诞生，神经语法树解析器。
- [Improving Inception and Image Classification in TensorFlow](https://research.googleblog.com/2016/08/improving-inception-and-image.html) - 非常有趣的 CNN 架构（例如：inception 风格的卷积层在减少参数数量方面很有前途且高效）。
- [WaveNet: A Generative Model for Raw Audio](https://deepmind.com/blog/wavenet-generative-model-raw-audio/) - 逼真的说话机器：完美的语音生成。
- [François Chollet's Twitter](https://twitter.com/fchollet) - Keras 的作者 - 拥有有趣的 Twitter 帖子和创新想法。
- [Neuralink and the Brain’s Magical Future](http://waitbutwhy.com/2017/04/neuralink.html) - 关于大脑和脑机接口的未来的发人深省的文章。
- [Migrating to Git LFS for Developing Deep Learning Applications with Large Files](http://vooban.com/en/tips-articles-geek-stuff/migrating-to-git-lfs-for-developing-deep-learning-applications-with-large-files/) - 轻松管理私人 Git 项目中的大文件。
- [The future of deep learning](https://blog.keras.io/the-future-of-deep-learning.html) - 弗朗索瓦·乔莱 (François Chollet) 对深度学习未来的思考。
- [Discover structure behind data with decision trees](http://vooban.com/en/tips-articles-geek-stuff/discover-structure-behind-data-with-decision-trees/) - 生成决策树并将其可视化，推断数据背后隐藏的逻辑。
- [Hyperopt tutorial for Optimizing Neural Networks’ Hyperparameters](http://vooban.com/en/tips-articles-geek-stuff/hyperopt-tutorial-for-optimizing-neural-networks-hyperparameters/) - 学会自动而不是手动地消除超参数空间。
- [Estimating an Optimal Learning Rate For a Deep Neural Network](https://medium.com/@surmenok/estimating-optimal-learning-rate-for-a-deep-neural-network-ce32f2556ce0) - 在任何一次完整训练之前估计最佳学习率的巧妙技巧。
 - [The Annotated Transformer](http://nlp.seas.harvard.edu/2018/04/03/attention.html) - 有助于理解“Attention Is All You Need”（AIAYN）论文。
 - [The Illustrated Transformer](http://jalammar.github.io/illustrated-transformer/) - 也有助于理解“Attention Is All You Need”（AIAYN）论文。
 - [Improving Language Understanding with Unsupervised Learning](https://blog.openai.com/language-unsupervised/) - 通过在庞大的语料库上进行无监督预训练，在许多 NLP 任务中实现了 SOTA。
 - [NLP's ImageNet moment has arrived](https://thegradient.pub/nlp-imagenet/) - 所有人都为 NLP 的 ImageNet 时刻欢呼。
 - [The Illustrated BERT, ELMo, and co. (How NLP Cracked Transfer Learning)](https://jalammar.github.io/illustrated-bert/) - 了解 NLP ImageNet 时刻使用的不同方法。
 - [Uncle Bob's Principles Of OOD](http://butunclebob.com/ArticleS.UncleBob.PrinciplesOfOod) - 不仅需要 SOLID 原则来编写干净的代码，而且众所周知的 REP、CCP、CRP、ADP、SDP 和 SAP 原则对于开发必须捆绑在不同独立软件包中的大型软件也非常重要。
 - [Why do 87% of data science projects never make it into production?](https://venturebeat.com/2019/07/19/why-do-87-of-data-science-projects-never-make-it-into-production/) - 数据不容忽视，团队和数据科学家之间的沟通对于正确集成解决方案非常重要。
 - [The real reason most ML projects fail](https://towardsdatascience.com/what-is-the-main-reason-most-ml-projects-fail-515d409a161f) - 专注于明确的业务目标，避免算法的枢轴，除非您有真正干净的代码，并且能够知道您的代码何时“足够好”。
 - [SOLID Machine Learning](https://www.umaneo.com/post/the-solid-principles-applied-to-machine-learning) - SOLID 原则应用于机器学习。
 
<a name="practical-resources" />

## 实用资源

<a name="librairies-and-implementations" />

### 库和实现
- [Neuraxle, a framwework for machine learning pipelines](https://github.com/Neuraxio/Neuraxle) - 用于构建和部署机器学习项目的最佳框架，并且与大多数框架兼容（例如：Scikit-Learn、TensorFlow、PyTorch、Keras 等）。
- [TensorFlow's GitHub repository](https://github.com/tensorflow/tensorflow) - 最著名的深度学习框架，包括高级和低级，同时保持灵活性。
- [skflow](https://github.com/tensorflow/skflow) - scikit-learn 的 TensorFlow 包装器。
- [Keras](https://keras.io/) - Keras 是另一个像 TensorFlow 一样有趣的深度学习框架，它大多是高级的。
- [carpedm20's repositories](https://github.com/carpedm20) - 许多有趣的神经网络架构都是由韩国人 Taehoon Kim（又名：Taehoon Kim）实现的。 carpedm20。
- [carpedm20/NTM-tensorflow](https://github.com/carpedm20/NTM-tensorflow) - 神经图灵机 TensorFlow 实现。
- [Deep learning for lazybones](http://oduerr.github.io/blog/2016/04/06/Deep-Learning_for_lazybones) - TensorFlow 中的迁移学习教程，用于通过预训练 CNN 的高级嵌入实现视觉，AlexNet 2012。
- [LSTM for Human Activity Recognition (HAR)](https://github.com/guillaume-chevalier/LSTM-Human-Activity-Recognition) - 我的关于在时间序列上使用 LSTM 进行分类的教程。
- [Deep stacked residual bidirectional LSTMs for HAR](https://github.com/guillaume-chevalier/HAR-stacked-residual-bidir-LSTMs) - 对之前项目的改进。
- [Sequence to Sequence (seq2seq) Recurrent Neural Network (RNN) for Time Series Prediction](https://github.com/guillaume-chevalier/seq2seq-signal-prediction) - 我的教程是关于如何预测数字的时间序列 - 可能是多通道的。
- [Hyperopt for a Keras CNN on CIFAR-100](https://github.com/guillaume-chevalier/Hyperopt-Keras-CNN-CIFAR-100) - 在 CIFAR-100 数据集上自动（元）优化神经网络（及其架构）。
- [ML / DL repositories I starred](https://github.com/guillaume-chevalier?direction=desc&page=1&q=machine+OR+deep+OR+learning+OR+rnn+OR+lstm+OR+cnn&sort=stars&tab=stars&utf8=%E2%9C%93) - GitHub 上有很多很棒的代码示例和项目。
- [Smoothly Blend Image Patches](https://github.com/guillaume-chevalier/Smoothly-Blend-Image-Patches) - [使用 U-Net 进行语义分割](https://vooban.com/en/tips-articles-geek-stuff/satellite-image-segmentation-workflow-with-u-net/) 平滑补丁合并。
- [Self Governing Neural Networks (SGNN): the Projection Layer](https://github.com/guillaume-chevalier/SGNN-Self-Governing-Neural-Networks-Projection-Layer) - 这样，您就可以在深度学习模型中使用单词，而无需训练或加载嵌入。
- [Neuraxle](https://github.com/Neuraxio/Neuraxle) - Neuraxle 是一个机器学习 (ML) 库，用于构建简洁的管道，提供正确的抽象以简化 ML 应用程序的研究、开发和部署。
- [Clean Machine Learning, a Coding Kata](https://github.com/Neuraxio/Kata-Clean-Machine-Learning-From-Dirty-Code) - 通过练习，学习良好的设计模式，以便以良好的方式进行机器学习。

<a name="some-datasets" />

### 一些数据集

我发现这些资源对于开发模型似乎很有趣。

- [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets.html) - 大量的机器学习数据集。
- [Cornell Movie--Dialogs Corpus](http://www.cs.cornell.edu/~cristian/Cornell_Movie-Dialogs_Corpus.html) - 这可以用于聊天机器人。
- [SQuAD The Stanford Question Answering Dataset](https://rajpurkar.github.io/SQuAD-explorer/) - 可以在线探索的问答数据集，以及在该数据集上表现良好的模型列表。
- [LibriSpeech ASR corpus](http://www.openslr.org/12/) - 巨大的免费英语语音数据集，性别和说话者均衡，似乎质量很高。
- [Awesome Public Datasets](https://github.com/caesar0301/awesome-public-datasets) - 很棒的公共数据集列表。
- [SentEval: An Evaluation Toolkit for Universal Sentence Representations](https://arxiv.org/abs/1803.05449) - 一个 Python 框架，用于在许多数据集（NLP 任务）上对句子表示进行基准测试。
- [ParlAI: A Dialog Research Software Platform](https://arxiv.org/abs/1705.06476) - 另一个 Python 框架，用于在许多数据集（NLP 任务）上对句子表示进行基准测试。


<a name="other-math-theory" />

## 其他数学理论

<a name="gradient-descent-algorithms-and-optimization" />

### 梯度下降算法和优化理论

- [Neural Networks and Deep Learning, ch.2](http://neuralnetworksanddeeplearning.com/chap2.html) - 反向传播算法如何工作的概述。
- [Neural Networks and Deep Learning, ch.4](http://neuralnetworksanddeeplearning.com/chap4.html) - 神经网络可以计算任何函数的视觉证明。
- [Yes you should understand backprop](https://medium.com/@karpathy/yes-you-should-understand-backprop-e2f06eab496b#.mr5wq61fb) - 揭示反向传播的注意事项以及在训练模型时了解这一点的重要性。
- [Artificial Neural Networks: Mathematics of Backpropagation](http://briandolhansky.com/blog/2013/9/27/artificial-neural-networks-backpropagation-part-4) - 用数学方式描绘反向传播。
- [Deep Learning Lecture 12: Recurrent Neural Nets and LSTMs](https://www.youtube.com/watch?v=56TYLaQN4N8) - 正确解释了 RNN 图的展开，并暴露了梯度下降算法的潜在问题。
- [Gradient descent algorithms in a saddle point](http://sebastianruder.com/content/images/2016/09/saddle_point_evaluation_optimizers.gif) - 可视化不同的优化器如何与鞍点交互。
- [Gradient descent algorithms in an almost flat landscape](https://devblogs.nvidia.com/wp-content/uploads/2015/12/NKsFHJb.gif) - 可视化不同的优化器如何与几乎平坦的景观交互。
- [Gradient Descent](https://www.youtube.com/watch?v=F6GSRDoB-Cg) - 好的，我已经在上面列出了 Andrew NG 的 Coursera 课程，但是这个视频作为介绍非常相关，并定义了梯度下降算法。
- [Gradient Descent: Intuition](https://www.youtube.com/watch?v=YovTqTY-PYY) - 上一个视频的后续内容：现在添加直觉。
- [Gradient Descent in Practice 2: Learning Rate](https://www.youtube.com/watch?v=gX6fZHgfrow) - 如何调整神经网络的学习率。
- [The Problem of Overfitting](https://www.youtube.com/watch?v=u73PU6Qwl1I) - 很好地解释了过度拟合以及如何解决该问题。
- [Diagnosing Bias vs Variance](https://www.youtube.com/watch?v=ewogYw5oCAI) - 了解神经网络预测中的偏差和方差以及如何解决这些问题。
- [Self-Normalizing Neural Networks](https://arxiv.org/pdf/1706.02515.pdf) - 令人难以置信的 SELU 激活函数的出现。
- [Learning to learn by gradient descent by gradient descent](https://arxiv.org/pdf/1606.04474.pdf) - RNN 作为优化器：引入 L2L 优化器，一种元神经网络。

<a name="complex-numbers-and-digital-signal-processing" />

### 复数和数字信号处理

好吧，信号处理可能与深度学习没有直接关系，但是研究在开发基于信号的神经架构方面有更多的直觉是很有趣的。

- [Window Functions](https://en.wikipedia.org/wiki/Window_function) - 维基百科页面列出了一些已知的窗口函数 - 请注意，[Hann-Poisson 窗口](https://en.wikipedia.org/wiki/Window_function#Hann%E2%80%93Poisson_window) 对于贪婪爬山算法（例如梯度下降）特别有趣。
- [MathBox, Tools for Thought Graphical Algebra and Fourier Analysis](https://acko.net/files/gltalks/toolsforthought/) - 傅里叶分析的新面貌。
- [How to Fold a Julia Fractal](http://acko.net/blog/how-to-fold-a-julia-fractal/) - 处理复数和波动方程的动画。
- [Animate Your Way to Glory, Math and Physics in Motion](http://acko.net/blog/animate-your-way-to-glory/) - 物理引擎中的收敛方法，并应用于交互设计。
- [Animate Your Way to Glory - Part II, Math and Physics in Motion](http://acko.net/blog/animate-your-way-to-glory-pt2/) - 使用四元数（用于处理 3D 旋转的数学对象）进行旋转和旋转插值的精美动画。
- [Filtering signal, plotting the STFT and the Laplace transform](https://github.com/guillaume-chevalier/filtering-stft-and-laplace-transform) - 关于信号处理的简单 Python 演示。


<a name="papers" />

## 论文

<a name="recurrent-neural-networks" />

### 循环神经网络

- [Deep Learning in Neural Networks: An Overview](https://arxiv.org/pdf/1404.7828v4.pdf) - You_Again 对深度学习的总结/概述，主要是关于 RNN 的。
- [Bidirectional Recurrent Neural Networks](http://www.di.ufpe.br/~fnj/RNA/bibliografia/BRNN.pdf) - 使用在时间轴上进行双向扫描的 RNN 进行更好的分类。
- [Learning Phrase Representations using RNN Encoder-Decoder for Statistical Machine Translation](https://arxiv.org/pdf/1406.1078v3.pdf) - 两个网络合二为一，形成 seq2seq（序列到序列）编码器-解码器架构。 RNN 编码器 - 具有 1000 个隐藏单元的解码器。 Adadelta 优化器。
- [Sequence to Sequence Learning with Neural Networks](http://papers.nips.cc/paper/5346-sequence-to-sequence-learning-with-neural-networks.pdf) - 在 WMT’14 英语到法语数据集上，具有 1000 个隐藏大小的 4 个堆叠 LSTM 单元，具有反向输入句子和波束搜索。
- [Exploring the Limits of Language Modeling](https://arxiv.org/pdf/1602.02410.pdf) - 在字符级 CNN 之上使用单词级 LSTM 的优秀递归模型，使用过多的 GPU 处理能力。
- [Neural Machine Translation and Sequence-to-sequence Models: A Tutorial](https://arxiv.org/pdf/1703.01619.pdf) - 对 NMT 主题的有趣概述，我主要阅读有关 RNN 的第 8 部分，并以 Attention 作为复习。
- [Exploring the Depths of Recurrent Neural Networks with Stochastic Residual Learning](https://cs224d.stanford.edu/reports/PradhanLongpre.pdf) - 基本上，在当前的情感分析案例中，残差连接可能比堆叠 RNN 更好。
- [Pixel Recurrent Neural Networks](https://arxiv.org/pdf/1601.06759.pdf) - 非常适合像 Photoshop 一样的“内容感知填充”来填充图像中缺失的补丁。
- [Adaptive Computation Time for Recurrent Neural Networks](https://arxiv.org/pdf/1603.08983v4.pdf) - 让 RNN 决定它们计算多长时间。我很想看看它与神经图灵机的结合效果如何。有关该主题的有趣的交互式可视化可以在[此处](http://distill.pub/2016/augmented-rnns/)找到。

<a name="convolutional-neural-networks" />

### 卷积神经网络

- [What is the Best Multi-Stage Architecture for Object Recognition?](http://yann.lecun.com/exdb/publis/pdf/jarrett-iccv-09.pdf) - “局部对比度标准化”的使用非常棒。
- [ImageNet Classification with Deep Convolutional Neural Networks](http://www.cs.toronto.edu/~fritz/absps/imagenet.pdf) - AlexNet，2012 ILSVRC，ReLU激活函数的突破。
- [Visualizing and Understanding Convolutional Networks](https://arxiv.org/pdf/1311.2901v3.pdf) - 对于“反卷积网络层”。
- [Fast and Accurate Deep Network Learning by Exponential Linear Units](https://arxiv.org/pdf/1511.07289v1.pdf) - CIFAR 视觉任务的 ELU 激活函数。
- [Very Deep Convolutional Networks for Large-Scale Image Recognition](https://arxiv.org/pdf/1409.1556v6.pdf) - 有趣的想法是，在池化之前堆叠多个 3x3 conv+ReLU，仅使用几个参数即可获得更大的滤波器尺寸。还有一个很好的“ConvNet 配置”表。
- [Going Deeper with Convolutions](http://www.cv-foundation.org/openaccess/content_cvpr_2015/papers/Szegedy_Going_Deeper_With_2015_CVPR_paper.pdf) - GoogLeNet：“Inception”层/模块的出现，其想法是将卷积层并行化为许多具有“相同”填充的不同大小的迷你卷积，并在深度上串联。
- [Highway Networks](https://arxiv.org/pdf/1505.00387v2.pdf) - 公路网：剩余连接。
- [Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift](https://arxiv.org/pdf/1502.03167v3.pdf) - 批量归一化（BN）：通过对整个批次求和来归一化层的输出，然后执行特定可训练量的线性重新缩放和移位。
- [U-Net: Convolutional Networks for Biomedical Image Segmentation](https://arxiv.org/pdf/1505.04597.pdf) - U-Net 是一种编码器-解码器 CNN，也具有跳跃连接，非常适合每像素级别的图像分割。
- [Deep Residual Learning for Image Recognition](https://arxiv.org/pdf/1512.03385v1.pdf) - 具有批量归一化层的非常深的残差层 - 又名“如何过度拟合具有太多层的任何视觉数据集，并在给定足够数据的情况下使任何视觉模型在识别时正常工作”。
- [Inception-v4, Inception-ResNet and the Impact of Residual Connections on Learning](https://arxiv.org/pdf/1602.07261v2.pdf) - 用于通过残差连接改进 GoogLeNet。
- [WaveNet: a Generative Model for Raw Audio](https://arxiv.org/pdf/1609.03499v2.pdf) - 使用基于扩张因果卷积的新架构生成史诗般的原始语音/音乐，以捕获更多音频长度。
- [Learning a Probabilistic Latent Space of Object Shapes via 3D Generative-Adversarial Modeling](https://arxiv.org/pdf/1610.07584v2.pdf) - 用于 3D 模型生成的 3D-GAN 和来自嵌入的有趣 3D 家具算术（就像带有 3D 家具表示的 word2vec 单词算术）。
- [Accurate, Large Minibatch SGD: Training ImageNet in 1 Hour](https://research.fb.com/publications/ImageNet1kIn1h/) - CNN 的分布式训练速度令人难以置信。
- [Densely Connected Convolutional Networks](https://arxiv.org/pdf/1608.06993.pdf) - 这种新的神经网络架构被命名为 DenseNet，荣获 CVPR 2017 最佳论文奖，在 CIFAR-10、CIFAR-100 和 SVHN 数据集上实现了最先进的性能改进。
- [The One Hundred Layers Tiramisu: Fully Convolutional DenseNets for Semantic Segmentation](https://arxiv.org/pdf/1611.09326.pdf) - 这种新的神经网络融合了 U-Net 和 DenseNet 的思想，特别适合图像分割中的巨大数据集。
- [Prototypical Networks for Few-shot Learning](https://arxiv.org/pdf/1703.05175.pdf) - 在损失中使用距离度量来从几个示例中确定对象属于哪个类。

<a name="attention-mechanisms" />

### 注意力机制

- [Neural Machine Translation by Jointly Learning to Align and Translate](https://arxiv.org/pdf/1409.0473.pdf) - LSTM 的注意力机制！大多数情况下，数字和公式及其解释对我来说是有用的。我在[此处]（https://www.youtube.com/watch?v=QuvRWevJMZ4）就该论文发表了演讲。
- [Neural Turing Machines](https://arxiv.org/pdf/1410.5401v2.pdf) - 杰出之处在于让神经网络学习一种算法，该算法在长时间依赖性上具有看似良好的泛化能力。序列回忆问题。
- [Show, Attend and Tell: Neural Image Caption Generation with Visual Attention](https://arxiv.org/pdf/1502.03044.pdf) - LSTM 在 CNN 特征图上的注意力机制创造了奇迹。
- [Teaching Machines to Read and Comprehend](https://arxiv.org/pdf/1506.03340v3.pdf) - 关于文本问答的一个非常有趣和有创意的工作，这是一个突破，与此有关。
- [Effective Approaches to Attention-based Neural Machine Translation](https://arxiv.org/pdf/1508.04025.pdf) - 探索注意力机制的不同方法。
- [Matching Networks for One Shot Learning](https://arxiv.org/pdf/1606.04080.pdf) - 通过使用注意力机制和查询来将图像与其他图像进行比较以进行分类，这是一种用低数据进行一次性学习的有趣方法。
- [Google’s Neural Machine Translation System: Bridging the Gap between Human and Machine Translation](https://arxiv.org/pdf/1609.08144.pdf) - 2016 年：在编码器/解码器上具有注意机制的堆叠残差 LSTM 是 NMT（神经机器翻译）的最佳选择。
- [Hybrid computing using a neural network with dynamic external memory](http://www.nature.com/articles/nature20101.epdf?author_access_token=ImTXBI8aWbYxYQ51Plys8NRgN0jAjWel9jnR3ZoTv0MggmpDmwljGswxVdeocYSurJ3hxupzWuRNeGvvXnoO8o4jTJcnAyhGuZzXJ1GEaD-Z7E6X_a9R-xqJ9TfJWBqz) - 基于 NTM 的可微记忆的改进：现在是可微神经计算机（DNC）。
- [Massive Exploration of Neural Machine Translation Architectures](https://arxiv.org/pdf/1703.03906.pdf) - 这产生了关于在框架 seq2seq 问题公式中进行 NMT 的边界的直觉。
- [通过在 Mel 频谱图上调节 WaveNet 进行自然 TTS 合成
预测](https://arxiv.org/pdf/1712.05884.pdf) - 用作声码器的 [WaveNet](https://arxiv.org/pdf/1609.03499v2.pdf) 可以以 Tacotron 2 LSTM 神经网络生成的梅尔频谱图为条件，注意从文本生成整齐的音频。
- [Attention is All You Need](https://arxiv.org/abs/1706.03762) (AIAYN) - Introducing multi-head self-attention Neural Networks with Positional Encoding to do Sentence-level NLP without any RNN or CNN - 本文是必读的（另请参阅[此说明](http://nlp.seas.harvard.edu/2018/04/03/attention.html）和[此可视化](http://jalammar.github.io/illusterated-transformer/) 的论文）。

<a name="other" />

### 其他

- [ProjectionNet: Learning Efficient On-Device Deep Networks Using Neural Projections](https://arxiv.org/abs/1708.00630) - 在深度神经网络中用单词投影替换单词嵌入，这不需要预先提取的字典，也不需要存储嵌入矩阵。
- [Self-Governing Neural Networks for On-Device Short Text Classification](http://aclweb.org/anthology/D18-1105) - 这篇论文是上面 ProjectionNet 的续篇。 SGNN 在 ProjectionNet 的基础上进行了详细阐述，优化也更加深入（另请参阅我的[尝试用代码重现论文](https://github.com/guillaume-chevalier/SGNN-Self-Governing-Neural-Networks-Projection-Layer) 并观看[演讲录音](https://vimeo.com/305197775)）。
- [Matching Networks for One Shot Learning](https://arxiv.org/abs/1606.04080) - 从其他示例列表（没有明确的类别）中对新示例进行分类，每个分类任务的数据量较低，但许多类似的分类任务有大量数据 - 这似乎比暹罗网络更好。总结一下：使用匹配网络，您可以直接优化示例之间的余弦相似度（就像自注意力产品会匹配一样），并将其直接传递给 softmax。我猜想匹配网络可能可以与 word2vec 的 CBOW 或 Skip-gram 中的负采样 softmax 训练一起使用，而无需进行任何上下文嵌入查找。


<a name="youtube" />

## YouTube 和视频

- [Attention Mechanisms in Recurrent Neural Networks (RNNs) - IGGG](https://www.youtube.com/watch?v=QuvRWevJMZ4) - 关于注意力机制的阅读小组的演讲（论文：联合学习对齐和翻译的神经机器翻译）。
- [Tensor Calculus and the Calculus of Moving Surfaces](https://www.youtube.com/playlist?list=PLlXfTHzgMRULkodlIEqfgTS-H1AY_bNtq) - 正确概括张量的工作原理，但仅仅观看一些视频就已经对理解这些概念有很大帮助。
- [Deep Learning & Machine Learning (Advanced topics)](https://www.youtube.com/playlist?list=PLlp-GWNOd6m4C_-9HxuHg2_ZeI2Yzwwqt) - 我发现有趣或有用的有关深度学习的视频列表，这是所有内容的混合。
- [Signal Processing Playlist](https://www.youtube.com/playlist?list=PLlp-GWNOd6m6gSz0wIcpvl4ixSlS-HEmr) - 我编写的一个关于 DFT/FFT、STFT 和拉普拉斯变换的 YouTube 播放列表 - 我对我的软件工程学士学位不包括信号处理课程（除了量子物理课程中的一点）感到很生气。
- [Computer Science](https://www.youtube.com/playlist?list=PLlp-GWNOd6m7vLOsW20xAJ81-65C-Ys6k) - 我编写的另一个 YouTube 播放列表，这次是关于各种 CS 主题。
- [Siraj's Channel](https://www.youtube.com/channel/UCWN3xxRkmTPmbKwht9FuE5A/videos?view=0&sort=p&flow=grid) - Siraj 提供有趣、快节奏的深度学习视频教程。
- [Two Minute Papers' Channel](https://www.youtube.com/user/keeroyz/videos?sort=p&view=0&flow=grid) - 对一些研究论文的有趣而浅薄的概述，例如关于 WaveNet 或神经风格迁移的论文。
- [Geoffrey Hinton interview](https://www.coursera.org/learn/neural-networks-deep-learning/lecture/dcm5r/geoffrey-hinton-interview) - 吴恩达（Andrew Ng）采访了杰弗里·辛顿（Geoffrey Hinton），后者谈论了他的研究和突破，并为学生提供了建议。
- [Growing Neat Software Architecture from Jupyter Notebooks](https://www.youtube.com/watch?v=K4QN27IKr0g) - 有关如何使用 Jupyter Notebooks 构建机器学习项目的入门知识。

<a name="misc-hubs-and-links" />

## 杂项。枢纽和链接

- [Hacker News](https://news.ycombinator.com/news) - 也许我是如何发现 ML 的——有趣的趋势在成为大事件之前就出现在该网站上。
- [DataTau](http://www.datatau.com/) - 这是一个类似于黑客新闻的中心，但专门针对数据科学。
- [Naver](http://www.naver.com/) - 这是一个韩语搜索引擎 - 讽刺的是，最好与谷歌翻译一起使用。令人惊讶的是，有时深度学习搜索结果和可理解的高级数学内容比谷歌搜索更容易出现。
- [Arxiv Sanity Preserver](http://www.arxiv-sanity.com/) - 具有 TF/IDF 功能的 arXiv 浏览器。
- [Awesome Neuraxle](https://github.com/Neuraxio/Awesome-Neuraxle) - Neuraxle 的一个很棒的列表，它是一个用于编码干净的生产级 ML 管道的 ML 框架。


<a name="license" />

## 许可证

[![CC0](http://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

在法律允许的范围内，[Guillaume Chevalier](https://github.com/guillaume-chevalier) 已放弃本作品的所有版权以及相关或邻接权。
