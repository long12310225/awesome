# 太棒了 - 被引用最多的深度学习论文

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

【注意】由于自2017年以来每天发布的深度学习论文数量巨大，该列表不再维护。

被引用最多的深度学习论文精选列表（2012-2016）

我们相信，无论其应用领域如何，都存在值得阅读的“经典”深度学习论文。我们不想提供大量的论文，而是希望提供一个“精选列表”，列出一些在某些研究领域被视为“必读”的优秀深度学习论文。

## 背景

在此列表之前，还有其他*很棒的深度学习列表*，例如，[Deep Vision](https://github.com/kjw0612/awesome-deep-vision) 和 [Awesome Recurrent Neural Networks](https://github.com/kjw0612/awesome-rnn)。此外，在这个列表出来之后，另一个针对深度学习初学者的很棒的列表，名为[深度学习论文阅读路线图](https://github.com/songrotek/Deep-Learning-Papers-Reading-Roadmap)，也被许多深度学习研究人员创建和喜爱。

尽管“路线图列表”包含许多重要的深度学习论文，但读完它们对我来说还是感到不知所措。正如我在引言中提到的，我相信开创性的著作可以给我们带来教训，无论其应用领域如何。因此，我想在这里介绍**前 100 篇深度学习论文**，作为概述深度学习研究的一个很好的起点。

要每天获取新发布论文的新闻，请关注我的 [twitter](https://twitter.com/TerryUm_ML) 或 [facebook 页面](https://www.facebook.com/terryum.io/)！

## 很棒的列表标准

1. 建议2012年至2016年发表的**前100篇深度学习论文**列表。
2. 如果一篇论文被添加到列表中，则应删除另一篇论文（通常来自“2016年的更多论文”部分）以保留前100篇论文。（因此，删除论文与添加论文一样也是重要的贡献）
3. 重要但未能入围的论文将列在“超过前100名”部分。
4. 近6个月或2012年之前发表的论文请参见“新论文”和“旧论文”部分。

*（引用标准）*
- **< 6 个月** ：*新论文*（通过讨论）
- **2016**：+60 次引用或“2016 年更多论文”
- **2015**：+200 次引用
- **2014**：+400 次引用
- **2013**：+600 次引用
- **2012**：+800 次引用
- **~2012** ：*旧论文*（通过讨论）

请注意，我们更喜欢可应用于各种研究的开创性深度学习论文，而不是应用论文。因此，一些符合标准的论文可能不会被接受，而另一些则可以。这取决于论文的影响力、对其他研究的适用性、研究领域的稀缺性等等。

**我们需要您的贡献！**

如果您有任何建议（缺失的论文、新论文、关键研究人员或拼写错误），请随时编辑并提出请求。
（请阅读[贡献指南](https://github.com/terryum/awesome-deep-learning-papers/blob/master/Contributing.md)以获取进一步的说明，尽管只是让我知道论文的标题也可以对我们做出很大的贡献。）

（更新）您可以使用[this](https://github.com/terryum/awesome-deep-learning-papers/blob/master/fetch_papers.py)下载所有前100篇论文，并使用[this](https://github.com/terryum/awesome-deep-learning-papers/blob/master/get_authors.py)收集所有作者姓名。此外，还提供所有前 100 篇论文的 [bib 文件](https://github.com/terryum/awesome-deep-learning-papers/blob/master/top100papers.bib)。谢谢 doodhwala、[Sven](https://github.com/sunshinemyson) 和 [grepinsight](https://github.com/grepinsight)！

+ 谁能贡献一下获取Top-100论文作者统计数据的代码吗？


## 内容

* [理解/概括/迁移](#understanding--generalization--transfer)
* [优化/培训技术](#optimization--training-techniques)
* [无监督/生成模型](#unsupervised--generative-models)
* [卷积网络模型](#convolutional-neural-network-models)
* [图像分割/目标检测](#image-segmentation--object-detection)
* [图片/视频/等](#image--video--etc)
* [自然语言处理/RNN](#natural-language-processing--rnns)
* [语音/其他领域](#speech--other-domain)
* [强化学习/机器人](#reinforcement-learning--robotics)
* [2016 年更多论文](#more-papers-from-2016)

*（超过前100名）*

* [新论文](#new-papers) : 少于 6 个月
* [旧论文](#old-papers) : 2012 年之前
* [HW / SW / 数据集](#hw--sw--dataset) : 技术报告
* [书籍/调查/评论](#book--survey--review)
* [视频讲座/教程/博客](#video-lectures--tutorials--blogs)
* [附录：超过 Top 100](#appendix-more-than-top-100) : 更多未在列表中的论文

* * *

### 理解/概括/迁移
- **在神经网络中提取知识** (2015)，G. Hinton 等人。 [[pdf]](http://arxiv.org/pdf/1503.02531)
- **深度神经网络很容易被愚弄：对无法识别的图像进行高置信度预测** (2015)，A. Nguyen 等人。 [[pdf]](http://arxiv.org/pdf/1412.1897)
- **深度神经网络中的特征可转移性如何？** (2014)，J. Yosinski 等人。 [[pdf]](http://papers.nips.cc/paper/5347-how-transferable-are-features-in-deep-neural-networks.pdf)
- **CNN 特征现成：令人震惊的识别基线** (2014)，A. Razavian 等人。 [[pdf]](http://www.cv-foundation.org//openaccess/content_cvpr_workshops_2014/W15/papers/Razavian_CNN_Features_Off-the-Shelf_2014_CVPR_paper.pdf)
- **使用卷积神经网络学习和传输中级图像表示** (2014)，M. Oquab 等人。 [[pdf]](http://www.cv-foundation.org/openaccess/content_cvpr_2014/papers/Oquab_Learning_and_Transferring_2014_CVPR_paper.pdf)
- **可视化和理解卷积网络** (2014)，M. Zeiler 和 R. Fergus [[pdf]](http://arxiv.org/pdf/1311.2901)
- **Decaf：用于通用视觉识别的深度卷积激活功能** (2014)，J. Donahue 等人。 [[pdf]](http://arxiv.org/pdf/1310.1531)

<!---[Key researchers]  [Geoffrey Hinton](https://scholar.google.ca/citations?user=JicYPdAAAAAJ), [Yoshua Bengio](https://scholar.google.ca/citations?user=kukA0LcAAAAJ), [Jason Yosinski](https://scholar.google.ca/citations?hl=en&user=gxL1qj8AAAAJ) -->

### 优化/培训技术
- **训练非常深的网络** (2015)，R. Srivastava 等人。 [[pdf]](http://papers.nips.cc/paper/5850-training-very-deep-networks.pdf)
- **批量归一化：通过减少内部协变量偏移加速深度网络训练** (2015)，S. Loffe 和 C. Szegedy [[pdf]](http://arxiv.org/pdf/1502.03167)
- **深入研究整流器：在 imagenet 分类上超越人类水平的性能** (2015)，K. He 等人。 [[pdf]](http://www.cv-foundation.org/openaccess/content_iccv_2015/papers/He_Delving_Deep_into_ICCV_2015_paper.pdf)
- **Dropout：防止神经网络过度拟合的简单方法** (2014)，N. Srivastava 等人。 [[pdf]](http://jmlr.org/papers/volume15/srivastava14a/srivastava14a.pdf)
- **Adam：随机优化方法** (2014)，D. Kingma 和 J. Ba [[pdf]](http://arxiv.org/pdf/1412.6980)
- **通过防止特征检测器的共同适应来改进神经网络** (2012)，G. Hinton 等人。 [[pdf]](http://arxiv.org/pdf/1207.0580.pdf)
- **超参数优化的随机搜索** (2012) J. Bergstra 和 Y. Bengio [[pdf]](http://www.jmlr.org/papers/volume13/bergstra12a/bergstra12a)

<!---[Key researchers] [Geoffrey Hinton](https://scholar.google.ca/citations?user=JicYPdAAAAAJ), [Yoshua Bengio](https://scholar.google.ca/citations?user=kukA0LcAAAAJ), [Christian Szegedy](https://scholar.google.ca/citations?hl=en&user=3QeF7mAAAAAJ), [Sergey Ioffe](https://scholar.google.ca/citations?user=S5zOyIkAAAAJ), [Kaming He](https://scholar.google.ca/citations?hl=en&user=DhtAFkwAAAAJ), [Diederik P. Kingma](https://scholar.google.ca/citations?hl=en&user=yyIoQu4AAAAJ)-->

### 无监督/生成模型
- **像素递归神经网络** (2016)，A. Oord 等人。 [[pdf]](http://arxiv.org/pdf/1601.06759v2.pdf)
- **改进 GAN 训练技术** (2016)，T. Salimans 等人。 [[pdf]](http://papers.nips.cc/paper/6125-improved-techniques-for-training-gans.pdf)
- **使用深度卷积生成对抗网络进行无监督表示学习** (2015)，A. Radford 等人。 [[pdf]](https://arxiv.org/pdf/1511.06434v2)
- **DRAW：用于图像生成的循环神经网络** (2015)，K. Gregor 等人。 [[pdf]](http://arxiv.org/pdf/1502.04623)
- **生成对抗网络** (2014)，I. Goodfellow 等人。 [[pdf]](http://papers.nips.cc/paper/5423-generative-adversarial-nets.pdf)
- **自动编码变分贝叶斯** (2013)，D. Kingma 和 M. Welling [[pdf]](http://arxiv.org/pdf/1312.6114)
- **使用大规模无监督学习构建高级特征** (2013)，Q. Le 等人。 [[pdf]](http://arxiv.org/pdf/1112.6209)

<!---[Key researchers] [Yoshua Bengio](https://scholar.google.ca/citations?user=kukA0LcAAAAJ), [Ian Goodfellow](https://scholar.google.ca/citations?user=iYN86KEAAAAJ), [Alex Graves](https://scholar.google.ca/citations?user=DaFHynwAAAAJ)-->
### 卷积神经网络模型
- **重新思考计算机视觉的初始架构** (2016)，C. Szegedy 等人。 [[pdf]](http://www.cv-foundation.org/openaccess/content_cvpr_2016/papers/Szegedy_Rethinking_the_Inception_CVPR_2016_paper.pdf)
- **Inception-v4、inception-resnet 以及残差连接对学习的影响** (2016)，C. Szegedy 等人。 [[pdf]](http://arxiv.org/pdf/1602.07261)
- **深度残差网络中的身份映射** (2016)，K. He 等人。 [[pdf]](https://arxiv.org/pdf/1603.05027v2.pdf)
- **用于图像识别的深度残差学习** (2016)，K. He 等人。 [[pdf]](http://arxiv.org/pdf/1512.03385)
- **空间变压器网络** (2015)，M. Jaderberg 等人，[[pdf]](http://papers.nips.cc/paper/5854-spatial-transformer-networks.pdf)
- **深入卷积** (2015)，C. Szegedy 等人。  [[pdf]](http://www.cv-foundation.org/openaccess/content_cvpr_2015/papers/Szegedy_Going_Deeper_With_2015_CVPR_paper.pdf)
- **用于大规模图像识别的超深卷积网络** (2014)，K. Simonyan 和 A. Zisserman [[pdf]](http://arxiv.org/pdf/1409.1556)
- **细节中的魔鬼回归：深入研究卷积网络** (2014)，K. Chatfield 等人。 [[pdf]](http://arxiv.org/pdf/1405.3531)
- **OverFeat：使用卷积网络集成识别、定位和检测** (2013)，P. Sermanet 等人。 [[pdf]](http://arxiv.org/pdf/1312.6229)
- **Maxout 网络** (2013)，I. Goodfellow 等人。 [[pdf]](http://arxiv.org/pdf/1302.4389v4)
- **网络中的网络** (2013)，M. Lin 等人。 [[pdf]](http://arxiv.org/pdf/1312.4400)
- **使用深度卷积神经网络进行 ImageNet 分类** (2012)，A. Krizhevsky 等人。 [[pdf]](http://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks.pdf)

<!---[Key researchers]  [Christian Szegedy](https://scholar.google.ca/citations?hl=en&user=3QeF7mAAAAAJ), [Kaming He](https://scholar.google.ca/citations?hl=en&user=DhtAFkwAAAAJ), [Shaoqing Ren](https://scholar.google.ca/citations?hl=en&user=AUhj438AAAAJ), [Jian Sun](https://scholar.google.ca/citations?hl=en&user=ALVSZAYAAAAJ), [Geoffrey Hinton](https://scholar.google.ca/citations?user=JicYPdAAAAAJ), [Yoshua Bengio](https://scholar.google.ca/citations?user=kukA0LcAAAAJ), [Yann LeCun](https://scholar.google.ca/citations?hl=en&user=WLN3QrAAAAAJ)-->

### 图像：分割/对象检测
- **您只需查看一次：统一实时对象检测** (2016)，J. Redmon 等人。 [[pdf]](http://www.cv-foundation.org/openaccess/content_cvpr_2016/papers/Redmon_You_Only_Look_CVPR_2016_paper.pdf)
- **用于语义分割的全卷积网络** (2015)，J. Long 等人。 [[pdf]](http://www.cv-foundation.org/openaccess/content_cvpr_2015/papers/Long_Fully_Convolutional_Networks_2015_CVPR_paper.pdf)
- **Faster R-CNN：通过区域提议网络实现实时目标检测** (2015)，S. Ren 等人。 [[pdf]](http://papers.nips.cc/paper/5638-faster-r-cnn-towards-real-time-object-detection-with-region-proposal-networks.pdf)
- **Fast R-CNN** (2015)，R. Girshick [[pdf]](http://www.cv-foundation.org/openaccess/content_iccv_2015/papers/Girshick_Fast_R-CNN_ICCV_2015_paper.pdf)
- **用于精确对象检测和语义分割的丰富特征层次结构** (2014)，R. Girshick 等人。 [[pdf]](http://www.cv-foundation.org/openaccess/content_cvpr_2014/papers/Girshick_Rich_Feature_Hierarchies_2014_CVPR_paper.pdf)
- **用于视觉识别的深度卷积网络中的空间金字塔池** (2014)，K. He 等人。 [[pdf]](http://arxiv.org/pdf/1406.4729)
- **使用深度卷积网络和全连接 CRF 进行语义图像分割**，L. Chen 等人。 [[pdf]](https://arxiv.org/pdf/1412.7062)
- **学习场景标记的分层特征** (2013)，C. Farabet 等人。 [[pdf]](https://hal-enpc.archives-ouvertes.fr/docs/00/74/20/77/PDF/farabet-pami-13.pdf)

<!---[Key researchers]  [Ross Girshick](https://scholar.google.ca/citations?hl=en&user=W8VIEZgAAAAJ), [Jeff Donahue](https://scholar.google.ca/citations?hl=en&user=UfbuDH8AAAAJ), [Trevor Darrell](https://scholar.google.ca/citations?hl=en&user=bh-uRFMAAAAJ)-->

### 图片/视频/等
- **使用深度卷积网络的图像超分辨率** (2016)，C. Dong 等人。 [[pdf]](https://arxiv.org/pdf/1501.00092v3.pdf)
- **艺术风格的神经算法** (2015)，L. Gatys 等人。 [[pdf]](https://arxiv.org/pdf/1508.06576)
- **用于生成图像描述的深度视觉语义对齐** (2015)，A. Karpathy 和 L. Fei-Fei [[pdf]](http://www.cv-foundation.org/openaccess/content_cvpr_2015/papers/Karpathy_Deep_Visual-Semantic_Alignments_2015_CVPR_paper.pdf)
- **展示、参与和讲述：具有视觉注意力的神经图像标题生成** (2015)，K. Xu 等人。 [[pdf]](http://arxiv.org/pdf/1502.03044)
- **展示和讲述：神经图像字幕生成器** (2015)，O. Vinyals 等人。 [[pdf]](http://www.cv-foundation.org/openaccess/content_cvpr_2015/papers/Vinyals_Show_and_Tell_2015_CVPR_paper.pdf)
- **用于视觉识别和描述的长期循环卷积网络** (2015)，J. Donahue 等人。 [[pdf]](http://www.cv-foundation.org/openaccess/content_cvpr_2015/papers/Donahue_Long-Term_Recurrent_Convolutional_2015_CVPR_paper.pdf)
- **VQA：视觉问答** (2015)，S. Antol 等人。 [[pdf]](http://www.cv-foundation.org/openaccess/content_iccv_2015/papers/Antol_VQA_Visual_Question_ICCV_2015_paper.pdf)
- **DeepFace：缩小人脸验证方面与人类水平性能的差距** (2014)，Y. Taigman 等人。 [[pdf]](http://www.cv-foundation.org/openaccess/content_cvpr_2014/papers/Taigman_DeepFace_Closing_the_2014_CVPR_paper.pdf)：
- **使用卷积神经网络进行大规模视频分类** (2014)，A. Karpathy 等人。 [[pdf]](http://vision.stanford.edu/pdf/karpathy14.pdf)
- **用于视频中动作识别的双流卷积网络** (2014)，K. Simonyan 等人。 [[pdf]](http://papers.nips.cc/paper/5353-two-stream-convolutional-networks-for-action-recognition-in-videos.pdf)
- **用于人类动作识别的 3D 卷积神经网络** (2013)，S. Ji 等人。 [[pdf]](http://machinelearning.wustl.edu/mlpapers/paper_files/icml2010_JiXYY10.pdf)

<!---[Key researchers]  [Oriol Vinyals](https://scholar.google.ca/citations?user=NkzyCvUAAAAJ), [Andrej Karpathy](https://scholar.google.ca/citations?user=l8WuQJgAAAAJ)-->

<!---[Key researchers]  [Alex Graves](https://scholar.google.ca/citations?user=DaFHynwAAAAJ)-->

### 自然语言处理/RNN
- **命名实体识别的神经架构** (2016)，G. Lample 等人。 [[pdf]](http://aclweb.org/anthology/N/N16/N16-1030.pdf)
- **探索语言建模的局限性** (2016)，R. Jozefowicz 等人。 [[pdf]](http://arxiv.org/pdf/1602.02410)
- **教机器阅读和理解** (2015)，K. Hermann 等人。 [[pdf]](http://papers.nips.cc/paper/5945-teaching-machines-to-read-and-comprehend.pdf)
- **基于注意力的神经机器翻译的有效方法** (2015)，M. Luong 等人。 [[pdf]](https://arxiv.org/pdf/1508.04025)
- **作为循环神经网络的条件随机场** (2015)，S. Cheng 和 S. Jayasumana。 [[pdf]](http://www.cv-foundation.org/openaccess/content_iccv_2015/papers/Zheng_Conditional_Random_Fields_ICCV_2015_paper.pdf)
- **内存网络** (2014)，J. Weston 等人。 [[pdf]](https://arxiv.org/pdf/1410.3916)
- **神经图灵机** (2014)，A. Graves 等人。 [[pdf]](https://arxiv.org/pdf/1410.5401)
- **通过共同学习对齐和翻译进行神经机器翻译** (2014)，D. Bahdanau 等人。 [[pdf]](http://arxiv.org/pdf/1409.0473)
- **使用神经网络进行序列到序列学习** (2014)，I. Sutskever 等人。 [[pdf]](http://papers.nips.cc/paper/5346-sequence-to-sequence-learning-with-neural-networks.pdf)
- **使用 RNN 编码器-解码器学习短语表示以进行统计机器翻译** (2014)，K. Cho 等人。 [[pdf]](http://arxiv.org/pdf/1406.1078)
- **用于建模句子的卷积神经网络** (2014)，N. Kalchbrenner 等人。 [[pdf]](http://arxiv.org/pdf/1404.2188v1)
- **用于句子分类的卷积神经网络** (2014)，Y. Kim [[pdf]](http://arxiv.org/pdf/1408.5882)
- **Glove：单词表示的全局向量** (2014)，J. Pennington 等人。 [[pdf]](http://anthology.aclweb.org/D/D14/D14-1162.pdf)
- **句子和文档的分布式表示** (2014)，Q. Le 和 T. Mikolov [[pdf]](http://arxiv.org/pdf/1405.4053)
- **单词和短语及其组合性的分布式表示** (2013)，T. Mikolov 等人。 [[pdf]](http://papers.nips.cc/paper/5021-distributed-representations-of-words-and-phrases-and-their-compositionality.pdf)
- **向量空间中单词表示的有效估计** (2013)，T. Mikolov 等人。  [[pdf]](http://arxiv.org/pdf/1301.3781)
- **情感树库上语义组合性的递归深度模型** (2013)，R. Socher 等人。 [[pdf]](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.383.1327&rep=rep1&type=pdf)
- **使用循环神经网络生成序列** (2013)，A. Graves。 [[pdf]](https://arxiv.org/pdf/1308.0850)

<!---[Key researchers]  [Kyunghyun Cho](https://scholar.google.ca/citations?user=0RAmmIAAAAAJ), [Oriol Vinyals](https://scholar.google.ca/citations?user=NkzyCvUAAAAJ), [Richard Socher](https://scholar.google.ca/citations?hl=en&user=FaOcyfMAAAAJ), [Tomas Mikolov](https://scholar.google.ca/citations?user=oBu8kMMAAAAJ), [Christopher D. Manning](https://scholar.google.ca/citations?user=1zmDOdwAAAAJ), [Yoshua Bengio](https://scholar.google.ca/citations?user=kukA0LcAAAAJ)-->

### 语音/其他领域
- **基于端到端注意力的大词汇量语音识别** (2016)，D. Bahdanau 等人。 [[pdf]](https://arxiv.org/pdf/1508.04395)
- **深度语音 2：英语和普通话端到端语音识别** (2015)，D. Amodei 等人。 [[pdf]](https://arxiv.org/pdf/1512.02595)
- **使用深度循环神经网络进行语音识别** (2013)，A. Graves [[pdf]](http://arxiv.org/pdf/1303.5778.pdf)
- **用于语音识别中声学建模的深度神经网络：四个研究小组的共同观点** (2012)，G. Hinton 等人。 [[pdf]](http://www.cs.toronto.edu/~asamir/papers/SPM_DNN_12.pdf)
- **用于大词汇量语音识别的上下文相关预训练深度神经网络** (2012) G. Dahl 等人。 [[pdf]](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.337.7548&rep=rep1&type=pdf)
- **使用深度信念网络的声学建模** (2012)，A. Mohamed 等人。 [[pdf]](http://www.cs.toronto.edu/~asamir/papers/speechDBN_jrnl.pdf)

<!---[Key researchers]  [Alex Graves](https://scholar.google.ca/citations?user=DaFHynwAAAAJ), [Geoffrey Hinton](https://scholar.google.ca/citations?user=JicYPdAAAAAJ), [Dong Yu](https://scholar.google.ca/citations?hl=en&user=tMY31_gAAAAJ)-->

### 强化学习/机器人
- **深度视觉运动策略的端到端训练** (2016)，S. Levine 等人。 [[pdf]](http://www.jmlr.org/papers/volume17/15-522/source/15-522.pdf)
- **通过深度学习和大规模数据收集学习机器人抓取的手眼协调** (2016)，S. Levine 等人。 [[pdf]](https://arxiv.org/pdf/1603.02199)
- **深度强化学习的异步方法** (2016)，V. Mnih 等人。 [[pdf]](http://www.jmlr.org/proceedings/papers/v48/mniha16.pdf)
- **使用双 Q 学习的深度强化学习** (2016)，H. Hasselt 等人。 [[pdf]](https://arxiv.org/pdf/1509.06461.pdf)
- **通过深度神经网络和树搜索掌握围棋游戏** (2016)，D. Silver 等人。 [[pdf]](http://www.nature.com/nature/journal/v529/n7587/full/nature16961.html)
- **通过深度强化学习进行持续控制** (2015)，T. Lillicrap 等人。 [[pdf]](https://arxiv.org/pdf/1509.02971)
- **通过深度强化学习实现人类水平的控制** (2015)，V. Mnih 等人。 [[pdf]](http://www.davidqiu.com:8888/research/nature14236.pdf)
- **用于检测机器人抓取的深度学习** (2015)，I. Lenz 等人。 [[pdf]](http://www.cs.cornell.edu/~asaxena/papers/lenz_lee_saxena_deep_learning_grasping_ijrr2014.pdf)
- **通过深度强化学习玩 atari** (2013)，V. Mnih 等人。 [[pdf]](http://arxiv.org/pdf/1312.5602.pdf))

<!---[Key researchers]  [Sergey Levine](https://scholar.google.ca/citations?user=8R35rCwAAAAJ), [Volodymyr Mnih](https://scholar.google.ca/citations?hl=en&user=rLdfJ1gAAAAJ), [David Silver](https://scholar.google.ca/citations?user=-8DNE4UAAAAJ)-->

### 2016 年更多论文
- **层归一化** (2016)，J. Ba 等人。 [[pdf]](https://arxiv.org/pdf/1607.06450v1.pdf)
- **通过梯度下降学习通过梯度下降**（2016），M. Andrychowicz 等人。 [[pdf]](http://arxiv.org/pdf/1606.04474v1)
- **神经网络的领域对抗训练** (2016)，Y. Ganin 等人。 [[pdf]](http://www.jmlr.org/papers/volume17/15-239/source/15-239.pdf)
- **WaveNet：原始音频生成模型** (2016)，A. Oord 等人。 [[pdf]](https://arxiv.org/pdf/1609.03499v2) [[web]](https://deepmind.com/blog/wavenet-generative-model-raw-audio/)
- **彩色图像着色** (2016)，R.Zhang 等人。 [[pdf]](https://arxiv.org/pdf/1603.08511)
- **自然图像流形上的生成视觉操作** (2016)，J. Zhu 等人。 [[pdf]](https://arxiv.org/pdf/1609.03552)
- **纹理网络：纹理和风格化图像的前馈合成** (2016)，D Ulyanov 等人。 [[pdf]](http://www.jmlr.org/proceedings/papers/v48/ulyanov16.pdf)
- **SSD：单次多盒检测器** (2016)，W. Liu 等人。 [[pdf]](https://arxiv.org/pdf/1512.02325)
- **SqueezeNet：AlexNet 级精度，参数减少 50 倍，模型大小 < 1MB** (2016)，F. Iandola 等人。 [[pdf]](http://arxiv.org/pdf/1602.07360)
- **Eie：压缩深度神经网络的高效推理引擎** (2016)，S. Han 等人。 [[pdf]](http://arxiv.org/pdf/1602.01528)
- **二值化神经网络：训练深度神经网络，其权重和激活被限制为 + 1 或 -1** (2016)，M. Courbariaux 等人。 [[pdf]](https://arxiv.org/pdf/1602.02830)
- **用于视觉和文本问答的动态记忆网络** (2016)，C. Xiong 等人。 [[pdf]](http://www.jmlr.org/proceedings/papers/v48/xiong16.pdf)
- **用于图像问答的堆叠注意力网络** (2016)，Z. Yang 等人。 [[pdf]](http://www.cv-foundation.org/openaccess/content_cvpr_2016/papers/Yang_Stacked_Attention_Networks_CVPR_2016_paper.pdf)
- **使用具有动态外部存储器的神经网络进行混合计算** (2016)，A. Graves 等人。 [[pdf]](https://www.gwern.net/docs/2016-graves.pdf)
- **谷歌的神经机器翻译系统：弥合人类和机器翻译之间的差距** (2016)，Y. Wu 等人。 [[pdf]](https://arxiv.org/pdf/1609.08144)

* * *


### 新论文
*值得一读的新发表论文（<6个月）*
- MobileNets：用于移动视觉应用的高效卷积神经网络 (2017)，Andrew G. Howard 等人。 [[pdf]](https://arxiv.org/pdf/1704.04861.pdf)
- 卷积序列到序列学习（2017），Jonas Gehring 等人。 [[pdf]](https://arxiv.org/pdf/1705.03122)
- 基于知识的神经对话模型 (2017)，Marjan Ghazvininejad 等人。 [[pdf]](https://arxiv.org/pdf/1702.01932)
- 准确、大型小批量 SGD：1 小时内训练 ImageNet (2017)，Priya Goyal 等人。 [[pdf]](https://research.fb.com/wp-content/uploads/2017/06/imagenet1kin1h3.pdf)
- TACOTRON：走向端到端语音合成（2017），Y. Wang 等人。 [[pdf]](https://arxiv.org/pdf/1703.10135.pdf)
- 深度照片风格迁移 (2017)，F. Luan 等人。 [[pdf]](http://arxiv.org/pdf/1703.07511v1.pdf)
- 进化策略作为强化学习的可扩展替代方案 (2017)，T. Salimans 等人。 [[pdf]](http://arxiv.org/pdf/1703.03864v1.pdf)
- 可变形卷积网络 (2017)，J. Dai 等人。 [[pdf]](http://arxiv.org/pdf/1703.06211v2.pdf)
- Mask R-CNN (2017)，K. He 等人。 [[pdf]](https://128.84.21.199/pdf/1703.06870)
- 学习利用生成对抗网络发现跨域关系（2017），T. Kim 等人。 [[pdf]](http://arxiv.org/pdf/1703.05192v1.pdf)
- 深度语音：实时神经文本转语音（2017），S. Arik 等人，[[pdf]](http://arxiv.org/pdf/1702.07825v2.pdf)
- PixelNet：像素的表示、像素的表示以及像素的表示（2017 年），A. Bansal 等人。 [[pdf]](http://arxiv.org/pdf/1702.06506v1.pdf)
- 批量重归一化：减少批量归一化模型中的小批量依赖性 (2017)，S. Ioffe。 [[pdf]](https://arxiv.org/abs/1702.03275)
- Wasserstein GAN (2017)，M. Arjovsky 等人。 [[pdf]](https://arxiv.org/pdf/1701.07875v1)
- 理解深度学习需要重新思考泛化（2017），C.Zhang 等人。 [[pdf]](https://arxiv.org/pdf/1611.03530)
- 最小二乘生成对抗网络（2016），X. Mao 等人。 [[pdf]](https://arxiv.org/abs/1611.04076v2)


### 旧论文
*2012年之前发表的经典论文*
- 无监督特征学习中单层网络的分析 (2011)，A. Coates 等人。 [[pdf]](http://machinelearning.wustl.edu/mlpapers/paper_files/AISTATS2011_CoatesNL11.pdf)
- 深度稀疏整流神经网络 (2011)，X. Glorot 等人。 [[pdf]](http://machinelearning.wustl.edu/mlpapers/paper_files/AISTATS2011_GlorotBB11.pdf)
- 自然语言处理（几乎）从头开始（2011），R. Collobert 等人。 [[pdf]](http://arxiv.org/pdf/1103.0398)
- 基于循环神经网络的语言模型（2010），T. Mikolov 等人。 [[pdf]](http://www.fit.vutbr.cz/research/groups/speech/servite/2010/rnnlm_mikolov.pdf)
- 堆叠式去噪自动编码器：使用局部去噪标准在深度网络中学习有用的表示（2010），P. Vincent 等人。 [[pdf]](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.297.3484&rep=rep1&type=pdf)
- 学习中级识别特征（2010），Y. Boureau [[pdf]](http://ece.duke.edu/~lcarin/boureau-cvpr-10.pdf)
- 训练受限玻尔兹曼机的实用指南（2010），G. Hinton [[pdf]](http://www.csri.utoronto.ca/~hinton/absps/guideTR.pdf)
- 了解训练深度前馈神经网络的难度 (2010)，X. Glorot 和 Y. Bengio [[pdf]](http://machinelearning.wustl.edu/mlpapers/paper_files/AISTATS2010_GlorotB10.pdf)
- 为什么无监督预训练有助于深度学习（2010），D. Erhan 等人。 [[pdf]](http://machinelearning.wustl.edu/mlpapers/paper_files/AISTATS2010_ErhanCBV10.pdf)
- 学习人工智能的深度架构 (2009)，Y. Bengio。 [[pdf]](http://sanghv.com/download/soft/machine%20learning,%20artificial%20intelligence,%20mathematics%20ebooks/ML/learning%20deep%20architectures%20for%20AI%20(2009).pdf)
- 用于分层表示的可扩展无监督学习的卷积深度信念网络 (2009)，H. Lee 等人。 [[pdf]](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.149.802&rep=rep1&type=pdf)
- 深度网络的贪婪逐层训练（2007），Y. Bengio 等人。 [[pdf]](http://machinelearning.wustl.edu/mlpapers/paper_files/NIPS2006_739.pdf)
- 使用神经网络降低数据维度，G. Hinton 和 R. Salakhutdinov。 [[pdf]](http://homes.mpimf-heidelberg.mpg.de/~mhelmsta/pdf/2006%20Hinton%20Salakhudtkinov%20Science.pdf)
- 深度信念网络的快速学习算法（2006），G. Hinton 等人。 [[pdf]](http://nuyoo.utm.mx/~jjf/rna/A8%20A%20fast%20learning%20algorithm%20for%20deep%20belief%20nets.pdf)
- 基于梯度的学习应用于文档识别（1998），Y. LeCun 等人。 [[pdf]](http://yann.lecun.com/exdb/publis/pdf/lecun-01a.pdf)
- 长短期记忆（1997），S. Hochreiter 和 J. Schmidhuber。 [[pdf]](http://www.mitpressjournals.org/doi/pdfplus/10.1162/neco.1997.9.8.1735)


### 硬件/软件/数据集
- SQuAD：100,000 多个文本机器理解问题（2016 年），Rajpurkar 等人。 [[pdf]](https://arxiv.org/pdf/1606.05250.pdf)
- OpenAI 健身房 (2016)，G. Brockman 等人。 [[pdf]](https://arxiv.org/pdf/1606.01540)
- TensorFlow：异构分布式系统上的大规模机器学习 (2016)，M. Abadi 等人。 [[pdf]](http://arxiv.org/pdf/1603.04467)
- Theano：用于快速计算数学表达式的 Python 框架，R. Al-Rfou 等人。
- Torch7：类似 matlab 的机器学习环境，R. Collobert 等人。 [[pdf]](https://ronan.collobert.com/pub/matos/2011_torch7_nipsw.pdf)
- MatConvNet：matlab 的卷积神经网络 (2015)，A. Vedaldi 和 K. Lenc [[pdf]](http://arxiv.org/pdf/1412.4564)
- Imagenet 大规模视觉识别挑战赛 (2015)，O. Russakovsky 等人。 [[pdf]](http://arxiv.org/pdf/1409.0575)
- Caffe：用于快速特征嵌入的卷积架构（2014），Y. Jia 等人。 [[pdf]](http://arxiv.org/pdf/1408.5093)


### 书籍/调查/评论
- 《深度学习的起源》（2017 年），H. Wang 和 Bhiksha Raj。 [[pdf]](https://arxiv.org/pdf/1702.07800)
- 深度强化学习：概述（2017），Y. Li，[[pdf]](http://arxiv.org/pdf/1701.07274v2.pdf)
- 神经机器翻译和序列到序列模型（2017）：教程，G. Neubig。 [[pdf]](http://arxiv.org/pdf/1703.01619v1.pdf)
- 神经网络和深度学习（书籍，2017 年 1 月），Michael Nielsen。 [[html]](http://neuralnetworksanddeeplearning.com/index.html)
- 深度学习（书籍，2016），Goodfellow 等人。 [[html]](http://www.deeplearningbook.org/)
- LSTM：搜索空间奥德赛 (2016)，K. Greff 等人。 [[pdf]](https://arxiv.org/pdf/1503.04069.pdf?utm_content=buffereddc5&utm_medium=social&utm_source=plus.google.com&utm_campaign=buffer)
- 变分自编码器教程 (2016)，C. Doersch。 [[pdf]](https://arxiv.org/pdf/1606.05908)
- 深度学习 (2015)，Y. LeCun、Y. Bengio 和 G. Hinton [[pdf]](https://www.cs.toronto.edu/~hinton/absps/NatureDeepReview.pdf)
- 神经网络中的深度学习：概述（2015），J. Schmidhuber [[pdf]](http://arxiv.org/pdf/1404.7828)
- 表征学习：回顾和新观点（2013），Y. Bengio 等人。 [[pdf]](http://arxiv.org/pdf/1206.5538)

### 视频讲座/教程/博客

*（讲座）*
- CS231n，用于视觉识别的卷积神经网络，斯坦福大学 [[web]](http://cs231n.stanford.edu/)
- CS224d，自然语言处理深度学习，斯坦福大学 [[web]](http://cs224d.stanford.edu/)
- Oxford Deep NLP 2017，自然语言处理深度学习，牛津大学 [[web]](https://github.com/oxford-cs-deepnlp-2017/lectures)

*（教程）*
- NIPS 2016 教程，长滩 [[web]](https://nips.cc/Conferences/2016/Schedule?type=Tutorial)
- ICML 2016 教程，纽约 [[web]](http://techtalks.tv/icml/2016/tutorials/)
- ICLR 2016 视频，圣胡安 [[web]](http://videolectures.net/iclr2016_san_juan/)
- 深度学习暑期学校 2016，蒙特利尔 [[web]](http://videolectures.net/deeplearning2016_montreal/)
- 湾区深度学习学校 2016，斯坦福 [[web]](https://www.bayareadlschool.org/)

*（博客）*
- OpenAI [[web]](https://www.openai.com/)
- 蒸馏 [[web]](http://distill.pub/)
- Andrej Karpathy 博客 [[web]](http://karpathy.github.io/)
- Colah 的博客 [[Web]](http://colah.github.io/)
- WildML [[Web]](http://www.wildml.com/)
- FastML [[web]](http://www.fastml.com/)
- 晨报 [[web]](https://blog.acolyer.org)

### 附录：前100名以上
*(2016)*
- 用于神经机器翻译的无显式分段的字符级解码器（2016），J. Chung 等人。 [[pdf]](https://arxiv.org/pdf/1603.06147)
- 使用深度神经网络对皮肤癌进行皮肤科医生级别的分类 (2017)，A. Esteva 等人。 [[html]](http://www.nature.com/nature/journal/v542/n7639/full/nature21056.html)
- 使用多重多实例学习的弱监督对象定位（2017），R. Gokberk 等人。 [[pdf]](https://arxiv.org/pdf/1503.00949)
- 使用深度神经网络进行脑肿瘤分割（2017），M. Havaei 等人。 [[pdf]](https://arxiv.org/pdf/1505.03540)
- 强迫教授：一种训练循环网络的新算法 (2016)，A. Lamb 等人。 [[pdf]](https://arxiv.org/pdf/1610.09038)
- 对抗性学习推理 (2016)，V. Dumoulin 等人。 [[web]](https://ishmaelbelghazi.github.io/ALI/)[[pdf]](https://arxiv.org/pdf/1606.00704v1)
- 了解卷积神经网络 (2016)，J. Koushik [[pdf]](https://arxiv.org/pdf/1605.09081v1)
- 让人类脱离循环：贝叶斯优化回顾 (2016)，B. Shahriari 等人。 [[pdf]](https://www.cs.ox.ac.uk/people/nando.defreitas/publications/BayesOptLoop.pdf)
- 循环神经网络的自适应计算时间（2016），A. Graves [[pdf]](http://arxiv.org/pdf/1603.08983)
- 密集连接的卷积网络 (2016)，G. Huang 等人。 [[pdf]](https://arxiv.org/pdf/1608.06993v1)
- 用于精确对象检测和分割的基于区域的卷积网络（2016），R. Girshick 等人。
- 具有基于模型的加速的连续深度 q 学习 (2016)，S. Gu 等人。 [[pdf]](http://www.jmlr.org/proceedings/papers/v48/gu16.pdf)
- 对 cnn/每日邮报阅读理解任务的彻底检查（2016 年），D. Chen 等人。 [[pdf]](https://arxiv.org/pdf/1606.02858)
- 使用混合词字符模型实现开放词汇神经机器翻译，M. Luong 和 C. Manning。 [[pdf]](https://arxiv.org/pdf/1604.00788)
- 用于自然语言处理的超深卷积网络 (2016)，A. Conneau 等人。 [[pdf]](https://arxiv.org/pdf/1606.01781)
- 高效文本分类的技巧包 (2016)，A. Joulin 等人。 [[pdf]](https://arxiv.org/pdf/1607.01759)
- 用于语义分割的深度结构化模型的高效分段训练（2016），G. Lin 等人。 [[pdf]](http://www.cv-foundation.org/openaccess/content_cvpr_2016/papers/Lin_Efficient_Piecewise_Training_CVPR_2016_paper.pdf)
- 学习构建用于问答的神经网络（2016），J. Andreas 等人。 [[pdf]](https://arxiv.org/pdf/1601.01705)
- 实时风格转移和超分辨率的感知损失（2016），J. Johnson 等人。 [[pdf]](https://arxiv.org/pdf/1603.08155)
- 使用卷积神经网络在野外阅读文本（2016），M. Jaderberg 等人。 [[pdf]](http://arxiv.org/pdf/1412.1842)
- 怎样才能提出有效的检测建议？ (2016)，J.Hosang 等人。 [[pdf]](https://arxiv.org/pdf/1502.05082)
- 内部-外部网络：使用跳跃池和循环神经网络检测上下文中的对象（2016），S. Bell 等人。 [[pdf]](http://www.cv-foundation.org/openaccess/content_cvpr_2016/papers/Bell_Inside-Outside_Net_Detecting_CVPR_2016_paper.pdf)。
- 通过多任务网络级联进行实例感知语义分割（2016），J. Dai 等人。 [[pdf]](http://www.cv-foundation.org/openaccess/content_cvpr_2016/papers/Dai_Instance-Aware_Semantic_Segmentation_CVPR_2016_paper.pdf)
- 使用 PixelCNN 解码器生成条件图像（2016），A. van den Oord 等人。 [[pdf]](http://papers.nips.cc/paper/6527-tree-structured-reinforcement-learning-for-sequential-object-localization.pdf)
- 具有随机深度的深度网络（2016），G. Huang 等人，[[pdf]](https://arxiv.org/pdf/1603.09382)
- 随机梯度 Langevin Dynamics 的一致性和波动 (2016)，Yee Whye Teh 等人。 [[pdf]](http://www.jmlr.org/papers/volume17/teh16a/teh16a.pdf)

*(2015)*
- 询问你的神经元：一种基于神经的方法来回答有关图像的问题 (2015)，M. Malinowski 等人。 [[pdf]](http://www.cv-foundation.org/openaccess/content_iccv_2015/papers/Malinowski_Ask_Your_Neurons_ICCV_2015_paper.pdf)
- 探索图像问答的模型和数据（2015），M. Ren 等人。 [[pdf]](http://papers.nips.cc/paper/5640-stochastic-variational-inference-for-hidden-markov-models.pdf)
- 你在和机器说话吗？多语言图像问题的数据集和方法（2015），H.Gao 等人。 [[pdf]](http://papers.nips.cc/paper/5641-are-you-talking-to-a-machine-dataset-and-methods-for-multilingual-image-question.pdf)
- Mind's eye：图像标题生成的循环视觉表示（2015），X. Chen 和 C. Zitnick。 [[pdf]](http://www.cv-foundation.org/openaccess/content_cvpr_2015/papers/Chen_Minds_Eye_A_2015_CVPR_paper.pdf)
- 从字幕到视觉概念再返回（2015），H. Fang 等人。 [[pdf]](http://www.cv-foundation.org/openaccess/content_cvpr_2015/papers/Fang_From_Captions_to_2015_CVPR_paper.pdf)。
- 迈向人工智能完整问答：一组先决玩具任务（2015），J. Weston 等人。 [[pdf]](http://arxiv.org/pdf/1502.05698)
- 有什么问题都可以问我：自然语言处理的动态记忆网络 (2015)，A. Kumar 等人。 [[pdf]](http://arxiv.org/pdf/1506.07285)
- 使用 LSTM 进行视频表示的无监督学习 (2015)，N. Srivastava 等人。 [[pdf]](http://www.jmlr.org/proceedings/papers/v37/srivastava15.pdf)
- 深度压缩：通过修剪、训练量化和霍夫曼编码来压缩深度神经网络（2015），S. Han 等人。 [[pdf]](https://arxiv.org/pdf/1510.00149)
- 改进了树结构长短期记忆网络的语义表示（2015），K. Tai 等人。 [[pdf]](https://arxiv.org/pdf/1503.00075)
- 字符感知神经语言模型（2015），Y. Kim 等人。 [[pdf]](https://arxiv.org/pdf/1508.06615)
- 作为外语的语法（2015），O. Vinyals 等人。 [[pdf]](http://papers.nips.cc/paper/5635-grammar-as-a-foreign-language.pdf)
- 信任区域政策优化（2015），J. Schulman 等人。 [[pdf]](http://www.jmlr.org/proceedings/papers/v37/schulman15.pdf)
- 超越短片段：用于视频分类的深度网络（2015）[[pdf]](http://www.cv-foundation.org/openaccess/content_cvpr_2015/papers/Ng_Beyond_Short_Snippets_2015_CVPR_paper.pdf)
- 用于语义分割的学习反卷积网络 (2015)，H. Noh 等人。 [[pdf]](https://arxiv.org/pdf/1505.04366v1)
- 使用 3d 卷积网络学习时空特征 (2015)，D. Tran 等人。 [[pdf]](http://www.cv-foundation.org/openaccess/content_iccv_2015/papers/Tran_Learning_Spatiotemporal_Features_ICCV_2015_paper.pdf)
- 通过深度可视化了解神经网络 (2015)，J. Yosinski 等人。 [[pdf]](https://arxiv.org/pdf/1506.06579)
- 循环网络架构的实证探索 (2015)，R. Jozefowicz 等人。  [[pdf]](http://www.jmlr.org/proceedings/papers/v37/jozefowicz15.pdf)
- 使用对抗网络拉普拉斯金字塔的深度生成图像模型（2015），E.Denton 等人。 [[pdf]](http://papers.nips.cc/paper/5773-deep-generative-image-models-using-a-laplacian-pyramid-of-adversarial-networks.pdf)
- 门控反馈循环神经网络 (2015)，J. Chung 等人。 [[pdf]](http://www.jmlr.org/proceedings/papers/v37/chung15.pdf)
- 通过指数线性单元 (ELUS) 进行快速准确的深度网络学习 (2015)，D. Clevert 等人。 [[pdf]](https://arxiv.org/pdf/1511.07289.pdf%5Cnhttp://arxiv.org/abs/1511.07289%5Cnhttp://arxiv.org/abs/1511.07289)
- 指针网络 (2015)，O. Vinyals 等人。 [[pdf]](http://papers.nips.cc/paper/5866-pointer-networks.pdf)
- 可视化和理解循环网络 (2015)，A. Karpathy 等人。 [[pdf]](https://arxiv.org/pdf/1506.02078)
- 基于注意力的语音识别模型 (2015)，J. Chorowski 等人。 [[pdf]](http://papers.nips.cc/paper/5847-attention-based-models-for-speech-recognition.pdf)
- 端到端内存网络（2015），S. Sukbaatar 等人。 [[pdf]](http://papers.nips.cc/paper/5846-end-to-end-memory-networks.pdf)
- 利用时间结构描述视频 (2015)，L. Yao 等人。 [[pdf]](http://www.cv-foundation.org/openaccess/content_iccv_2015/papers/Yao_Desribing_Videos_by_ICCV_2015_paper.pdf)
- 神经对话模型 (2015)，O. Vinyals 和 Q. Le。 [[pdf]](https://arxiv.org/pdf/1506.05869.pdf)
- 利用词嵌入的经验教训提高分布相似性，O. Levy 等人。 [[pdf]] (https://www.transacl.org/ojs/index.php/tacl/article/download/570/124)
- 基于堆栈长短期记忆的基于转换的依存解析 (2015)，C. Dyer 等人。 [[pdf]](http://aclweb.org/anthology/P/P15/P15-1033.pdf)
- 通过使用 LSTM 建模字符而不是单词来改进基于转换的解析 (2015)，M. Ballesteros 等人。 [[pdf]](http://aclweb.org/anthology/D/D15/D15-1041.pdf)
- 寻找形式中的函数：开放词汇单词表示的组合字符模型（2015），W. Ling 等人。 [[pdf]](http://aclweb.org/anthology/D/D15/D15-1176.pdf)


*(~2014)*
- DeepPose：通过深度神经网络进行人体姿势估计（2014），A. Toshev 和 C. Szegedy [[pdf]](http://www.cv-foundation.org/openaccess/content_cvpr_2014/papers/Toshev_DeepPose_Human_Pose_2014_CVPR_paper.pdf)
- 学习图像超分辨率的深度卷积网络（2014 年，C. Dong 等人 [[pdf]](https://www.researchgate.net/profile/Chen_Change_Loy/publication/264552416_Lecture_Notes_in_Computer_Science/links/53e583e50cf25d674e9c280e.pdf)
- 视觉注意力循环模型 (2014)，V. Mnih 等人。 [[pdf]](http://arxiv.org/pdf/1406.6247.pdf)
- 门控循环神经网络对序列建模的实证评估 (2014)，J. Chung 等人。 [[pdf]](https://arxiv.org/pdf/1412.3555)
- 解决神经机器翻译中的罕见单词问题（2014），M. Luong 等人。 [[pdf]](https://arxiv.org/pdf/1410.8206)
- 关于神经机器翻译的特性：编码器-解码器方法 (2014)，K. Cho 等人。等人。
- 循环神经网络正则化 (2014)，W. Zaremba 等人。 [[pdf]](http://arxiv.org/pdf/1409.2329)
- 神经网络的有趣特性 (2014)，C. Szegedy 等人。 [[pdf]](https://arxiv.org/pdf/1312.6199.pdf)
- 使用递归神经网络实现端到端语音识别（2014 年），A. Graves 和 N. Jaitly。 [[pdf]](http://www.jmlr.org/proceedings/papers/v32/graves14.pdf)
- 使用深度神经网络的可扩展对象检测（2014），D. Erhan 等人。 [[pdf]](http://www.cv-foundation.org/openaccess/content_cvpr_2014/papers/Erhan_Scalable_Object_Detection_2014_CVPR_paper.pdf)
- 关于深度学习中初始化和动量的重要性 (2013)，I. Sutskever 等人。 [[pdf]](http://machinelearning.wustl.edu/mlpapers/paper_files/icml2013_sutskever13.pdf)
- 使用 dropconnect 对神经网络进行正则化 (2013)，L. Wan 等人。 [[pdf]](http://machinelearning.wustl.edu/mlpapers/paper_files/icml2013_wan13.pdf)
- 学习场景标签的分层特征 (2013)，C. Farabet 等人。 [[pdf]](https://hal-enpc.archives-ouvertes.fr/docs/00/74/20/77/PDF/farabet-pami-13.pdf)
- 连续空间词表示中的语言规律（2013），T. Mikolov 等人。 [[pdf]](http://www.aclweb.org/anthology/N13-1#page=784)
- 大规模分布式深度网络（2012），J. Dean 等人。 [[pdf]](http://papers.nips.cc/paper/4687-large-scale-distributed-deep-networks.pdf)
- 使用神经网络的快速准确的依赖解析器。陈和曼宁。 [[pdf]](http://cs.stanford.edu/people/danqi/papers/emnlp2014.pdf)



## 致谢

感谢您做出的所有贡献。在提出拉取请求之前，请务必阅读[贡献指南](https://github.com/terryum/awesome-deep-learning-papers/blob/master/Contributing.md)。

## 许可证
[![CC0](http://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

在法律允许的范围内，[Terry T. Um](https://www.facebook.com/terryum.io/) 已放弃本作品的所有版权以及相关或邻接权。
