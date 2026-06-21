# 令人惊叹的深度视觉 [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

计算机视觉深度学习资源的精选列表，灵感来自 [awesome-php](https://github.com/ziadoz/awesome-php) 和 [awesome-computer-vision](https://github.com/jbhuang0604/awesome-computer-vision)。

维护者 - [Jiwon Kim](https://github.com/kjw0612)、[Heesoo Myeong](https://github.com/hmyeong)、[Myungsub Choi](https://github.com/myungsub)、[Jung Kwon Lee](https://github.com/deruci)、[Taeksoo Kim](https://github.com/jazzsaxmafia)

该项目没有得到积极维护。

## 贡献
请随时[pull requests](https://github.com/kjw0612/awesome-deep-vision/pulls)添加论文。

[![Join the chat at https://gitter.im/kjw0612/awesome-deep-vision](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/kjw0612/awesome-deep-vision?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

## 分享
+ [在 Twitter 上分享](http://twitter.com/home?status=http://jiwonkim.org/awesome-deep-vision%0A计算机视觉深度学习资源)
+ [在 Facebook 上分享](http://www.facebook.com/sharer/sharer.php?u=https://jiwonkim.org/awesome-deep-vision)
+ [在 Google Plus 上分享](http://plus.google.com/share?url=https://jiwonkim.org/awesome-deep-vision)
+ [在 LinkedIn 上分享](http://www.linkedin.com/shareArticle?mini=true&url=https://jiwonkim.org/awesome-deep-vision&title=Awesome%20Deep%20Vision&summary=&source=)

## 目录
- [Papers](#papers)
  - [ImageNet 分类](#imagenet-classification)
  - [物体检测](#object-detection)
  - [物体追踪](#object-tracking)
  - [低层次视觉](#low-level-vision)
    - [Super-Resolution](#super-resolution)
    - [其他应用](#other-applications)
  - [边缘检测](#edge-detection)
  - [语义分割](#semantic-segmentation)
  - [视觉注意力和显着性](#visual-attention-and-saliency)
  - [物体识别](#object-recognition)
  - [人体姿势估计](#human-pose-estimation)
  - [了解CNN](#understanding-cnn)
  - [图像与语言](#image-and-language)
    - [图像字幕](#image-captioning)
    - [视频字幕](#video-captioning)
    - [问答](#question-answering)
  - [图像生成](#image-generation)
  - [其他主题](#other-topics)
- [Courses](#courses)
- [Books](#books)
- [Videos](#videos)
- [Software](#software)
  - [Framework](#framework)
  - [Applications](#applications)
- [Tutorials](#tutorials)
- [Blogs](#blogs)

## 论文

### ImageNet 分类
![classification](https://cloud.githubusercontent.com/assets/5226447/8451949/327b9566-2022-11e5-8b34-53b4a64c13ad.PNG)
（来自 Alex Krizhevsky、Ilya Sutskever、Geoffrey E. Hinton，使用深度卷积神经网络进行 ImageNet 分类，NIPS，2012 年。）
* 微软（深度残差学习）[[论文](http://arxiv.org/pdf/1512.03385v1.pdf)][[幻灯片](http://image-net.org/challenges/talks/ilsvrc2015_deep_residual_learning_kaiminghe.pdf)]
* 何凯明、张翔宇、任少清、孙健，图像识别中的深度残差学习，arXiv:1512.03385。
* Microsoft（PReLu/权重初始化）[[论文]](http://arxiv.org/pdf/1502.01852)
* 何凯明、张翔宇、任少清、孙健，深入研究整流器：在 ImageNet 分类上超越人类水平的性能，arXiv：1502.01852。
* 批量归一化 [[论文]](http://arxiv.org/pdf/1502.03167)
* Sergey Ioffe、Christian Szegedy，批量归一化：通过减少内部协变量偏移加速深度网络训练，arXiv：1502.03167。
* GoogLeNet [[论文]](http://arxiv.org/pdf/1409.4842)
* Christian Szegedy、Wei Liu、Yangqing Jia、Pierre Sermanet、Scott Reed、Dragomir Anguelov、Dumitru Erhan、Vincent Vanhoucke、Andrew Rabinovich，CVPR，2015 年。
* VGG-Net [[Web]](http://www.robots.ox.ac.uk/~vgg/research/very_deep/) [[Paper]](http://arxiv.org/pdf/1409.1556)
* Karen Simonyan 和 Andrew Zisserman，用于大规模视觉识别的超深卷积网络，ICLR，2015 年。
* AlexNet [[论文]](http://papers.nips.cc/book/advances-in-neural-information-processing-systems-25-2012)
* Alex Krizhevsky、Ilya Sutskever、Geoffrey E. Hinton，使用深度卷积神经网络进行 ImageNet 分类，NIPS，2012 年。

### 物体检测
![object_detection](https://cloud.githubusercontent.com/assets/5226447/8452063/f76ba500-2022-11e5-8db1-2cd5d490e3b3.PNG)
（来自 Shaoqing Ren、Kaiming He、Ross Girshick、Jian Sun，Faster R-CNN：利用区域提议网络实现实时目标检测，arXiv：1506.01497。）

* PVANET [[论文]](https://arxiv.org/pdf/1608.08021) [[代码]](https://github.com/sanghoon/pva-faster-rcnn)
* Kye-Hyeon Kim、Sanghoon Hong、Byungseok Roh、Yeongjae Cheon、Minje Park、PVANET：用于实时对象检测的深度但轻量级神经网络，arXiv：1608.08021
* OverFeat，纽约大学 [[论文]](http://arxiv.org/pdf/1312.6229.pdf)
* OverFeat：使用卷积网络进行集成识别、定位和检测，ICLR，2014 年。
* R-CNN，加州大学伯克利分校 [[Paper-CVPR14]](http://www.cv-foundation.org/openaccess/content_cvpr_2014/papers/Girshick_Rich_Feature_Hierarchies_2014_CVPR_paper.pdf) [[Paper-arXiv14]](http://arxiv.org/pdf/1311.2524)
* Ross Girshick、Jeff Donahue、Trevor Darrell、Jitendra Malik，用于精确对象检测和语义分割的丰富特征层次结构，CVPR，2014 年。
* SPP，微软研究院 [[论文]](http://arxiv.org/pdf/1406.4729)
* 何凯明、张翔宇、任少清、孙健，视觉识别深度卷积网络中的空间金字塔池化，ECCV，2014。
* Fast R-CNN，微软研究院 [[论文]](http://arxiv.org/pdf/1504.08083)
* Ross Girshick，Fast R-CNN，arXiv：1504.08083。
* Faster R-CNN，微软研究院 [[论文]](http://arxiv.org/pdf/1506.01497)
* Shaoqing Ren、Kaiming He、Ross Girshick、Jian Sun，Faster R-CNN：利用区域提议网络实现实时目标检测，arXiv：1506.01497。
* R-CNN 减去 R，牛津 [[论文]](http://arxiv.org/pdf/1506.06981)
* Karel Lenc、Andrea Vedaldi、R-CNN minus R、arXiv：1506.06981。
* 拥挤场景中的端到端人员检测 [[Paper]](http://arxiv.org/abs/1506.04878)
* Russell Stewart、Mykhaylo Andriluka，拥挤场景中的端到端人员检测，arXiv：1506.04878。
* 你只需看一次：统一、实时对象检测 [[论文]](http://arxiv.org/abs/1506.02640)、[[论文版本 2]](https://arxiv.org/abs/1612.08242)、[[C 代码]](https://github.com/pjreddie/darknet)、[[Tensorflow代码]](https://github.com/thtrieu/darkflow)
* Joseph Redmon、Santosh Divvala、Ross Girshick、Ali Farhadi，《你只看一次：统一、实时对象检测》，arXiv：1506.02640
* 约瑟夫·雷德蒙、阿里·法哈迪（版本 2）
* 内外网[[论文]](http://arxiv.org/abs/1512.04143)
* Sean Bell、C. Lawrence Zitnick、Kavita Bala、Ross Girshick，《Inside-Outside Net：使用跳过池和循环神经网络检测上下文中的对象》
*深度残差网络（当前最先进的）[[论文]](http://arxiv.org/abs/1512.03385)
* 何凯明、张翔宇、任少清、孙健，图像识别中的深度残差学习
*具有多重多实例学习的弱监督对象定位[[论文](http://arxiv.org/pdf/1503.00949.pdf)]
* R-FCN [[论文]](https://arxiv.org/abs/1605.06409) [[代码]](https://github.com/daijifeng001/R-FCN)
* Jifeng Dai、Yi Li、Kaiming He、Jian Sun、R-FCN：通过基于区域的全卷积网络进行目标检测
* SSD [[论文]](https://arxiv.org/pdf/1512.02325v2.pdf) [[代码]](https://github.com/weiliu89/caffe/tree/ssd)
* Wei Liu1、Dragomir Anguelov、Dumitru Erhan、Christian Szegedy、Scott Reed、Cheng-Yang Fu、Alexander C. Berg，SSD：单发 MultiBox 探测器，arXiv：1512.02325
* 现代卷积目标检测器的速度/精度权衡 [[Paper]](https://arxiv.org/pdf/1611.10012v1.pdf)
* Jonathan Huang、Vivek Rathod、Chen Sun、Menglong Zhu、Anoop Korattikara、Alireza Fathi、Ian Fischer、Zbigniew Wojna、Yang Song、Sergio Guadarrama、Kevin Murphy，Google Research，arXiv：1611.10012

### 视频分类
* Nicolas Ballas、Li Yao、Pal Chris、Aaron Courville，“深入研究卷积网络以学习视频表示”，ICLR 2016。 [[论文](http://arxiv.org/pdf/1511.06432v4.pdf)]
* Michael Mathieu、camille couprie、Yann Lecun，“超越均方误差的深度多尺度视频预测”，ICLR 2016。 [[论文](http://arxiv.org/pdf/1511.05440v6.pdf)]

### 物体追踪
* Seunghoon Hong、Tackgeun You、Suha Kwak、Bohyung Han，通过卷积神经网络学习判别显着图进行在线跟踪，arXiv:1502.06796。 [[论文]](http://arxiv.org/pdf/1502.06796)
* Hanxi Li、Yi Li 和 Fatih Porikli，DeepTrack：通过用于视觉跟踪的卷积神经网络学习判别特征表示，BMVC，2014 年。[[Paper]](http://www.bmva.org/bmvc/2014/files/paper028.pdf)
* N Wang、DY Yeung，学习视觉跟踪的深度紧凑图像表示，NIPS，2013。[[Paper]](http://winsty.net/papers/dlt.pdf)
* Chao Ma、Jia-Bin Huang、Xiaokang Yang 和 Ming-Hsuan Yang，视觉跟踪的分层卷积特征，ICCV 2015 [[论文](http://www.cv-foundation.org/openaccess/content_iccv_2015/papers/Ma_Hierarchical_Convolutional_Features_ICCV_2015_paper.pdf)] [[代码](https://github.com/jbhuang0604/CF2)]
* Lijun Wang、Wanli Ouyang、Xiaogang Wang 和 Huchuan Lu，全卷积网络视觉跟踪，ICCV 2015 [[论文](http://202.118.75.4/lu/Paper/ICCV2015/iccv15_lijun.pdf)] [[代码](https://github.com/scott89/FCNT)]
* Hyeonseob Namand Bohyung Han，学习用于视觉跟踪的多域卷积神经网络，[[论文](http://arxiv.org/pdf/1510.07945.pdf)] [[代码](https://github.com/HyeonseobNam/MDNet)] [[项目页面](http://cvlab.postech.ac.kr/research/mdnet/)]

### 低层次视觉

#### 超分辨率
* 迭代图像重建
* Sven Behnke：学习迭代图像重建。 IJCAI，2001。[[论文]](http://www.ais.uni-bonn.de/behnke/papers/ijcai01.pdf)
* Sven Behnke：学习神经抽象金字塔中的迭代图像重建。国际计算智能与应用杂志，卷。 1、没有。 4，第 427-438 页，2001 年。[[论文]](http://www.ais.uni-bonn.de/behnke/papers/ijcia01.pdf)
* 超分辨率 (SRCNN) [[Web]](http://mmlab.ie.cuhk.edu.hk/projects/SRCNN.html) [[Paper-ECCV14]](http://personal.ie.cuhk.edu.hk/~ccloy/files/eccv_2014_deepresolution.pdf) [[Paper-arXiv15]](http://arxiv.org/pdf/1501.00092.pdf)
* Chao Dong、Chen Change Loy、Kaiming He、Xiaoou Tang，学习图像超分辨率的深度卷积网络，ECCV，2014 年。
* Chao Dong、Chen Change Loy、Kaiming He、Xiaoou Tang，使用深度卷积网络的图像超分辨率，arXiv:1501.00092。
* 非常深的超分辨率
* Jiwon Kim、Jung Kwon Lee、Kyoung Mu Lee，使用非常深的卷积网络实现精确图像超分辨率，arXiv:1511.04587，2015。[[论文]](http://arxiv.org/abs/1511.04587)
* 深度递归卷积网络
* Jiwon Kim、Jung Kwon Lee、Kyoung Mu Lee，用于图像超分辨率的深度递归卷积网络，arXiv:1511.04491，2015。[[论文]](http://arxiv.org/abs/1511.04491)
* Casade稀疏编码网络
* Chaowen Wang、Ding Liu、Wei Han、Jianchao Yang 和 Thomas S. Huang，稀疏先验图像超分辨率深度网络。 ICCV，2015。 [[论文]](http://www.ifp.illinois.edu/~dingliu2/iccv15/iccv15.pdf) [[代码]](http://www.ifp.illinois.edu/~dingliu2/iccv15/)
* 超分辨率的感知损失
* Justin Johnson、Alexandre Alahi、李飞飞，实时风格迁移和超分辨率的感知损失，arXiv:1603.08155，2016。[[论文]](http://arxiv.org/abs/1603.08155) [[补充]](http://cs.stanford.edu/people/jcjohns/papers/fast-style/fast-style-supp.pdf)
* SRGAN
* Christian Ledig、Lucas Theis、Ferenc Huszar、Jose Caballero、Andrew Cunningham、Alejandro Acosta、Andrew Aitken、Alykhan Tejani、Johannes Totz、Zehan Wang、Wenzhe Shi，使用生成对抗网络的逼真单图像超分辨率，arXiv:1609.04802v3，2016。 [[论文]](https://arxiv.org/pdf/1609.04802v3.pdf)
* 其他
* Osendorfer、Christian、Hubert Soyer 和 Patrick van der Smagt，采用快速近似卷积稀疏编码的图像超分辨率，ICONIP，2014 年。[[Paper ICONIP-2014]](http://brml.org/uploads/tx_sibibtex/281.pdf)

#### 其他应用
* 光流 (FlowNet) [[论文]](http://arxiv.org/pdf/1504.06852)
* Philipp Fischer、Alexey Dosovitskiy、Eddy Ilg、Philip Häusser、Caner Hazırbaş、Vladimir Golkov、Patrick van der Smagt、Daniel Cremers、Thomas Brox，FlowNet：使用卷积网络学习光流，arXiv：1504.06852。
* 压缩伪影减少 [[Paper-arXiv15]](http://arxiv.org/pdf/1504.06993)
* Chao Dong、Yubin Deng、Chen Change Loy、Xiaoou Tang，通过深度卷积网络减少压缩伪影，arXiv：1504.06993。
* 模糊消除
* Christian J. Schuler、Michael Hirsch、Stefan Harmeling、Bernhard Schölkopf，学习去模糊，arXiv:1406.7444 [[Paper]](http://arxiv.org/pdf/1406.7444.pdf)
* 孙健、曹文飞、徐宗本、Jean Ponce，学习用于非均匀运动模糊去除的卷积神经网络，CVPR，2015 [[Paper]](http://arxiv.org/pdf/1503.00593)
* 图像反卷积 [[Web]](http://lxu.me/projects/dcnn/) [[Paper]](http://lxu.me/mypapers/dcnn_nips14.pdf)
* 李旭，Jimmy SJ。任正非，刘策，贾佳雅，用于图像反卷积的深度卷积神经网络，NIPS，2014。
* 深度边缘感知滤波器 [[Paper]](http://jmlr.org/proceedings/papers/v37/xub15.pdf)
* 李旭，Jimmy SJ。任，颜琼，廖仁杰，贾佳雅，深度边缘感知滤波器，ICML，2015。
* 使用卷积神经网络计算立体匹配成本 [[Paper]](http://www.cv-foundation.org/openaccess/content_cvpr_2015/papers/Zbontar_Computing_the_Stereo_2015_CVPR_paper.pdf)
* Jure Žbontar、Yann LeCun，使用卷积神经网络计算立体匹配成本，CVPR，2015 年。
* 彩色图像着色 Richard Zhang, Phillip Isola, Alexei A. Efros, ECCV, 2016 [[Paper]](http://arxiv.org/pdf/1603.08511.pdf), [[Code]](https://github.com/richzhang/colorization)
* Ryan Dahl，[[博客]](http://tinyclouds.org/colorize/)
* 通过修复进行特征学习[[Paper]](https://arxiv.org/pdf/1604.07379v1.pdf)[[Code]](https://github.com/pathak22/context-encoder)
* Deepak Pathak、Philipp Krahenbuhl、Jeff Donahue、Trevor Darrell、Alexei A. Efros，上下文编码器：通过 Inpainting 进行特征学习，CVPR，2016 年

### 边缘检测
![edge_detection](https://cloud.githubusercontent.com/assets/5226447/8452371/93ca6f7e-2025-11e5-90f2-d428fd5ff7ac.PNG)
（来自 Gedas Bertasius、Jianbo Shi、Lorenzo Torresani，DeepEdge：用于自上而下轮廓检测的多尺度分叉深度网络，CVPR，2015 年。）

* 整体嵌套边缘检测 [[Paper]](http://arxiv.org/pdf/1504.06375) [[Code]](https://github.com/s9xie/hed)
* 谢赛宁，涂卓文，整体嵌套边缘检测，arXiv:1504.06375。
* DeepEdge [[论文]](http://arxiv.org/pdf/1412.1123)
* Gedas Bertasius、Jianbo Shi、Lorenzo Torresani，DeepEdge：用于自上而下轮廓检测的多尺度分叉深度网络，CVPR，2015 年。
* DeepContour [[论文]](http://mc.eistar.net/UpLoadFiles/Papers/DeepContour_cvpr15.pdf)
* 沉伟、王兴刚、王岩、白翔、张志江，DeepContour：通过正共享损失学习的轮廓检测深度卷积特征，CVPR，2015。

### 语义分割
![semantic_segmantation](https://cloud.githubusercontent.com/assets/5226447/8452076/0ba8340c-2023-11e5-88bc-bebf4509b6bb.PNG)
（来自 Jifeng Dai、Kaiming He、Jian Sun，BoxSup：利用边界框监督卷积网络进行语义分割，arXiv：1503.01640。）
* PASCAL VOC2012 挑战赛排行榜（2016 年 9 月 1 日）
  ![VOC2012_top_rankings](https://cloud.githubusercontent.com/assets/3803777/18164608/c3678488-7038-11e6-9ec1-74a1542dce13.png)
（来自 PASCAL VOC2012 [排行榜](http://host.robots.ox.ac.uk:8080/leaderboard/displaylb.php?challengeid=11&compid=6)）
* SEC：种子、扩展和约束
* Alexander Kolesnikov、Christoph Lampert，种子、扩展和约束：弱监督图像分割的三个原则，ECCV，2016。 [[论文]](http://pub.ist.ac.at/~akolesnikov/files/ECCV2016/main.pdf) [[代码]](https://github.com/kolesman/SEC)
* 阿德莱德
* 林国胜、沈春华、Ian Reid、Anton van dan Hengel，语义分割深度结构化模型的高效分段训练，arXiv：1504.01013。 [[论文]](http://arxiv.org/pdf/1504.01013)（VOC2012排名第一）
* 林国胜、沈春华、Ian Reid、Anton van den Hengel，深度学习消息传递推理中的消息，arXiv：1508.02108。 [[论文]](http://arxiv.org/pdf/1506.02108)（VOC2012排名第4）
* 深度解析网络（DPN）
* Ziwei Liu、Xiaoxiao Li、Ping Luo、Chen Change Loy、Xiaoou Tang，通过深度解析网络进行语义图像分割，arXiv:1509.02634 / ICCV 2015 [[Paper]](http://arxiv.org/pdf/1509.02634.pdf)（VOC 2012 排名第二）
* CentraleSuperBoundaries，INRIA [[论文]](http://arxiv.org/pdf/1511.07386)
* Iasonas Kokkinos，使用深度学习在边界检测中超越人类，arXiv:1411.07386（VOC 2012 排名第四）
* BoxSup [[论文]](http://arxiv.org/pdf/1503.01640)
* Jifeng Dai、Kaiming He、Jian Sun，BoxSup：利用边界框监督卷积网络进行语义分割，arXiv：1503.01640。 （VOC2012排名第6）
* 浦项科技大学
* Hyeonwoo Noh、Seunghoon Hong、Bohyung Han，用于语义分割的学习反卷积网络，arXiv：1505.04366。 [[论文]](http://arxiv.org/pdf/1505.04366)（VOC2012排名第7）
* Seunghoon Hong、Hyeonwoo Noh、Bohyung Han，用于半监督语义分割的解耦深度神经网络，arXiv：1506.04924。 [[论文]](http://arxiv.org/pdf/1506.04924)
* Seunghoon Hong、Junhyuk Oh、Bohyung Han 和 Honglak Lee，利用深度卷积神经网络学习语义分割的可转移知识，arXiv:1512.07928 [[论文](http://arxiv.org/pdf/1512.07928.pdf)] [[项目页面](http://cvlab.postech.ac.kr/research/transfernet/)]
* 条件随机场作为循环神经网络 [[论文]](http://arxiv.org/pdf/1502.03240)
* 郑帅、Sadeep Jayasumana、Bernardino Romera-Paredes、Vibhav Vineet、Zhizhong Su、Dalong Du、Chang Huang、Philip H. S. Torr，条件随机场作为循环神经网络，arXiv:1502.03240。 （VOC2012排名第8）
* 深度实验室
* Liu-Chieh Chen、George Papandreou、Kevin Murphy、Alan L. Yuille，用于语义图像分割的 DCNN 的弱监督和半监督学习，arXiv：1502.02734。 [[论文]](http://arxiv.org/pdf/1502.02734)（VOC2012排名第9）
* 缩小 [[论文]](http://www.cv-foundation.org/openaccess/content_cvpr_2015/papers/Mostajabi_Feedforward_Semantic_Segmentation_2015_CVPR_paper.pdf)
* Mohammadreza Mostajabi、Payman Yadollahpour、Gregory Shakhnarovich，具有缩小功能的前馈语义分割，CVPR，2015 年
* 联合校准[[论文]](http://arxiv.org/pdf/1507.01581)
* Holger Caesar、Jasper Uijlings、Vittorio Ferrari，语义分割联合校准，arXiv：1507.01581。
* 用于语义分割的全卷积网络 [[Paper-CVPR15]](http://www.cv-foundation.org/openaccess/content_cvpr_2015/papers/Long_Fully_Convolutional_Networks_2015_CVPR_paper.pdf) [[Paper-arXiv15]](http://arxiv.org/pdf/1411.4038)
* Jonathan Long、Evan Shelhamer、Trevor Darrell，用于语义分割的全卷积网络，CVPR，2015 年。
* 超列 [[论文]](http://www.cv-foundation.org/openaccess/content_cvpr_2015/papers/Hariharan_Hypercolumns_for_Object_2015_CVPR_paper.pdf)
* Bharath Hariharan、Pablo Arbelaez、Ross Girshick、Jitendra Malik，用于对象分割和细粒度本地化的超列，CVPR，2015 年。
* 深度层次解析
* Abhishek Sharma、Oncel Tuzel、David W. Jacobs，语义分割的深度分层解析，CVPR，2015。[[Paper]](http://www.cv-foundation.org/openaccess/content_cvpr_2015/papers/Sharma_Deep_Hierarchical_Parsing_2015_CVPR_paper.pdf)
* 学习场景标签的分层特征 [[Paper-ICML12]](http://yann.lecun.com/exdb/publis/pdf/farabet-icml-12.pdf) [[Paper-PAMI13]](http://yann.lecun.com/exdb/publis/pdf/farabet-pami-13.pdf)
* Clement Farabet、Camille Couprie、Laurent Najman、Yann LeCun，使用多尺度特征学习、纯度树和最佳覆盖进行场景解析，ICML，2012 年。
* Clement Farabet、Camille Couprie、Laurent Najman、Yann LeCun，学习场景标签的分层特征，PAMI，2013 年。
* 剑桥大学 [[Web]](http://mi.eng.cam.ac.uk/projects/segnet/)
* Vijay Badrinarayanan、Alex Kendall 和 Roberto Cipolla“SegNet：用于图像分割的深度卷积编码器-解码器架构。” arXiv 预印本 arXiv:1511.00561, 2015。 [[论文]](http://arxiv.org/abs/1511.00561)
* Alex Kendall、Vijay Badrinarayanan 和 Roberto Cipolla “贝叶斯 SegNet：用于场景理解的深度卷积编码器-解码器架构中的模型不确定性。” arXiv 预印本 arXiv:1511.02680, 2015。 [[论文]](http://arxiv.org/abs/1511.00561)
* 普林斯顿
* Fisher Yu、Vladlen Koltun，“通过扩张卷积进行多尺度上下文聚合”，ICLR 2016，[[论文](http://arxiv.org/pdf/1511.07122v2.pdf)]
* 大学。华盛顿的艾伦·艾
* Hamid Izadinia、Fereshteh Sadeghi、Santosh Kumar Divvala、Yejin Choi、Ali Farhadi，“语义分割、视觉蕴涵和释义的句段短语表”，ICCV，2015 年， [[论文](http://www.cv-foundation.org/openaccess/content_iccv_2015/papers/Izadinia_Segment-Phrase_Table_for_ICCV_2015_paper.pdf)]
* 因瑞亚
* Iasonas Kokkinos，“利用深度学习确定边界检测的边界”，ICLR 2016，[[论文](http://arxiv.org/pdf/1511.07386v2.pdf)]
* 加州大学圣巴巴拉分校
* Niloufar Pourian、S. Karthikeyan 和 B.S. Manjunath，“通过学习图像部分社区进行基于弱监督图的语义分割”，ICCV，2015，[[论文](http://www.cv-foundation.org/openaccess/content_iccv_2015/papers/Pourian_Weakly_Supervised_Graph_ICCV_2015_paper.pdf)]

### 视觉注意力和显着性
![saliency](https://cloud.githubusercontent.com/assets/5226447/8492362/7ec65b88-2183-11e5-978f-017e45ddba32.png)
（来自 Nian Liu、Junwei Han、Dingwen Zhang、Shifeng Wen、Tianming Liu，使用卷积神经网络预测眼睛注视，CVPR，2015 年。）

* Mr-CNN [[论文]](http://www.cv-foundation.org/openaccess/content_cvpr_2015/papers/Liu_Predicting_Eye_Fixations_2015_CVPR_paper.pdf)
* Nian Liu、Junwei Han、Dingwen Zhang、Shifeng Wen、Tianming Liu，使用卷积神经网络预测眼睛注视，CVPR，2015 年。
* 学习对地标的顺序搜索 [[Paper]](http://www.cv-foundation.org/openaccess/content_cvpr_2015/papers/Singh_Learning_a_Sequential_2015_CVPR_paper.pdf)
* Saurabh Singh、Derek Hoiem、David Forsyth，学习地标的顺序搜索，CVPR，2015 年。
* 具有视觉注意力的多物体识别 [[Paper]](http://arxiv.org/pdf/1412.7755.pdf)
* Jimmy Lei Ba、Volodymyr Mnih、Koray Kavukcuoglu，具有视觉注意力的多目标识别，ICLR，2015 年。
* 视觉注意力的循环模型 [[Paper]](http://papers.nips.cc/paper/5542-recurrent-models-of-visual-attention.pdf)
* Volodymyr Mnih、Nicolas Heess、Alex Graves、Koray Kavukcuoglu，视觉注意力循环模型，NIPS，2014 年。

### 物体识别
* 使用卷积神经网络进行弱监督学习 [[Paper]](http://www.cv-foundation.org/openaccess/content_cvpr_2015/papers/Oquab_Is_Object_Localization_2015_CVPR_paper.pdf)
* Maxime Oquab、Leon Bottou、Ivan Laptev、Josef Sivic，对象定位是免费的吗？ – 卷积神经网络的弱监督学习，CVPR，2015。
* FV-CNN [[论文]](http://www.cv-foundation.org/openaccess/content_cvpr_2015/papers/Cimpoi_Deep_Filter_Banks_2015_CVPR_paper.pdf)
* Mircea Cimpoi、Subhransu Maji、Andrea Vedaldi，用于纹理识别和分割的深度过滤器库，CVPR，2015 年。

### 人体姿势估计
* Zhe Cao、Tomas Simon、Shih-En Wei 和 Yaser Sheikh，使用零件亲和力场进行实时多人 2D 姿势估计，CVPR，2017 年。
* Leonid Pishchulin、Eldar Insafutdinov、Siyu Tang、Bjoern Andres、Mykhaylo Andriluka、Peter Gehler 和 Bernt Schiele，Deepcut：多人姿势估计的联合子集划分和标签，CVPR，2016 年。
* Shih-En Wei、Varun Ramakrishna、Takeo Kanade 和 Yaser Sheikh，卷积姿势机，CVPR，2016 年。
* Alejandro Newell、Kaiyu Yang 和 Jia Deng，用于人体姿势估计的堆叠沙漏网络，ECCV，2016 年。
* Tomas Pfister、James Charles 和 Andrew Zisserman，用于视频中人体姿势估计的流动卷积网络，ICCV，2015 年。
* Jonathan J. Tompson、Arjun Jain、Yann LeCun、Christoph Bregler，用于人体姿势估计的卷积网络和图形模型的联合训练，NIPS，2014 年。

### 了解CNN
![understanding](https://cloud.githubusercontent.com/assets/5226447/8452083/1aaa0066-2023-11e5-800b-2248ead51584.PNG)
（摘自 Aravindh Mahendran、Andrea Vedaldi，通过反转理解深度图像表示，CVPR，2015 年。）

* Karel Lenc、Andrea Vedaldi，通过测量等方差和等价性来理解图像表示，CVPR，2015。 [[Paper]](http://www.cv-foundation.org/openaccess/content_cvpr_2015/papers/Lenc_Understand_Image_Representations_2015_CVPR_paper.pdf)
* Anh Nguyen、Jason Yosinski、Jeff Clune，深度神经网络很容易被愚弄：无法识别图像的高置信度预测，CVPR，2015。[[Paper]](http://www.cv-foundation.org/openaccess/content_cvpr_2015/papers/Nguyen_Deep_Neural_Networks_2015_CVPR_paper.pdf)
* Aravindh Mahendran、Andrea Vedaldi，通过反转理解深度图像表示，CVPR，2015。 [[Paper]](http://www.cv-foundation.org/openaccess/content_cvpr_2015/papers/Mahendran_Understand_Deep_Image_2015_CVPR_paper.pdf)
* Bolei Zhou、Aditya Khosla、Agata Lapedriza、Aude Oliva、Antonio Torralba，物体检测器出现在深度场景 CNN 中，ICLR，2015 年。[[arXiv 论文]](http://arxiv.org/abs/1412.6856)
* Alexey Dosovitskiy、Thomas Brox，用卷积网络反转视觉表示，arXiv，2015。[[论文]](http://arxiv.org/abs/1506.02753)
* Matthrew Zeiler、Rob Fergus，可视化和理解卷积网络，ECCV，2014 年。[[论文]](https://www.cs.nyu.edu/~fergus/papers/zeilerECCV2014.pdf)


### 图像与语言

#### 图像字幕
![image_captioning](https://cloud.githubusercontent.com/assets/5226447/8452051/e8f81030-2022-11e5-85db-c68e7d8251ce.PNG)
（来自 Andrej Karpathy、李飞飞，用于生成图像描述的深度视觉语义对齐，CVPR，2015 年。）

* UCLA / 百度 [[论文]](http://arxiv.org/pdf/1410.1090)
* 毛俊华、徐伟、杨易、王江、Alan L. Yuille，用多模态循环神经网络解释图像，arXiv:1410.1090。
* 多伦多 [[论文]](http://arxiv.org/pdf/1411.2539)
* Ryan Kiros、Ruslan Salakhutdinov、Richard S. Zemel，用多模态神经语言模型统一视觉语义嵌入，arXiv：1411.2539。
* 伯克利 [[论文]](http://arxiv.org/pdf/1411.4389)
* Jeff Donahue、Lisa Anne Hendricks、Sergio Guadarrama、Marcus Rohrbach、Subhashini Venugopalan、Kate Saenko、Trevor Darrell，用于视觉识别和描述的长期循环卷积网络，arXiv：1411.4389。
*谷歌[[论文]](http://arxiv.org/pdf/1411.4555)
* Oriol Vinyals、Alexander Toshev、Samy Bengio、Dumitru Erhan，展示和讲述：神经图像字幕生成器，arXiv：1411.4555。
* 斯坦福大学 [[Web]](http://cs.stanford.edu/people/karpathy/deepimagesent/) [[Paper]](http://cs.stanford.edu/people/karpathy/cvpr2015.pdf)
* Andrej Karpathy、李飞飞，生成图像描述的深度视觉语义对齐，CVPR，2015。
* UML / UT [[论文]](http://arxiv.org/pdf/1412.4729)
* Subhashini Venugopalan、Huijuan Xu、Jeff Donahue、Marcus Rohrbach、Raymond Mooney、Kate Saenko，使用深度循环神经网络将视频翻译为自然语言，NAACL-HLT，2015 年。
* CMU / 微软 [[Paper-arXiv]](http://arxiv.org/pdf/1411.5654) [[Paper-CVPR]](http://www.cs.cmu.edu/~xinleic/papers/cvpr15_rnn.pdf)
* Xinlei Chen，C. Lawrence Zitnick，学习图像标题生成的循环视觉表示，arXiv：1411.5654。
* Xinlei Chen，C. Lawrence Zitnick，Mind's Eye：图像字幕生成的循环视觉表示，CVPR 2015
* 微软[[论文]](http://arxiv.org/pdf/1411.4952)
* 方浩、Saurabh Gupta、Forrest Iandola、Rupesh Srivastava、邓力、Piotr Dollár、高剑峰、何晓东、Margaret Mitchell、John C. Platt、C. Lawrence Zitnick、Geoffrey Zweig，从字幕到视觉概念再到，CVPR，2015 年。
* 大学。蒙特利尔/大学。多伦多 [[Web](http://kelvinxu.github.io/projects/capgen.html)] [[Paper](http://www.cs.toronto.edu/~zemel/documents/captionAttn.pdf)]
* Kelvin Xu、Jimmy Lei Ba、Ryan Kiros、Kunghyun Cho、Aaron Courville、Ruslan Salakhutdinov、Richard S. Zemel、Yoshua Bengio，展示、出席和讲述：具有视觉注意力的神经图像字幕生成，arXiv:1502.03044 / ICML 2015
* Idiap / EPFL / Facebook [[论文](http://arxiv.org/pdf/1502.03671)]
* Remi Lebret、Pedro O. Pinheiro、Ronan Collobert，基于短语的图像字幕，arXiv:1502.03671 / ICML 2015
* UCLA / 百度 [[论文](http://arxiv.org/pdf/1504.06692)]
* 毛俊华、徐伟、杨易、王江、黄志恒、Alan L. Yuille，像孩子一样学习：从图像的句子描述中快速学习小说视觉概念，arXiv:1504.06692
* 硕士 + 伯克利
* Jacob Devlin、Saurabh Gupta、Ross Girshick、Margaret Mitchell、C. Lawrence Zitnick，探索图像字幕的最近邻方法，arXiv:1505.04467 [[论文](http://arxiv.org/pdf/1505.04467.pdf)]
* Jacob Devlin、Hao Cheng、Hao Fang、Saurabh Gupta、Li Deng、Xiaodong He、Geoffrey Zweig、Margaret Mitchell，图像字幕语言模型：怪癖和有效方法，arXiv:1505.01809 [[论文](http://arxiv.org/pdf/1505.01809.pdf)]
* 阿德莱德 [[论文](http://arxiv.org/pdf/1506.01144.pdf)]
* Qi Wu、Chunhua Shen、Anton van den Hengel、Lingqiao Liu、Anthony Dick，带有中间属性层的图像字幕，arXiv:1506.01144
*蒂尔堡[[论文](http://arxiv.org/pdf/1506.03694.pdf)]
* Grzegorz Chrupala、Akos Kadar、Afra Alishahi，通过图片学习语言，arXiv：1506.03694
* 大学。蒙特利尔 [[论文](http://arxiv.org/pdf/1507.01053.pdf)]
* Kyunghyun Cho、Aaron Courville、Yoshua Bengio，使用基于注意力的编码器-解码器网络描述多媒体内容，arXiv:1507.01053
*康奈尔大学[[论文](http://arxiv.org/pdf/1508.02091.pdf)]
* Jack Hessel、Nicolas Savva、Michael J. Wilber，神经图像字幕中的图像表示和新领域，arXiv：1508.02091
* MS + 城市大学。香港 [[论文](http://www.cv-foundation.org/openaccess/content_iccv_2015/papers/Yao_Learning_Query_and_ICCV_2015_paper.pdf)]
* Ting Yao、Tao Mei 和 Chong-Wah Ngo，“学习查询和图像相似度
与排名典型相关分析”，ICCV，2015

#### 视频字幕
* 伯克利 [[Web]](http://jeffdonahue.com/lrcn/) [[Paper]](http://arxiv.org/pdf/1411.4389.pdf)
* Jeff Donahue、Lisa Anne Hendricks、Sergio Guadarrama、Marcus Rohrbach、Subhashini Venugopalan、Kate Saenko、Trevor Darrell，用于视觉识别和描述的长期循环卷积网络，CVPR，2015 年。
* UT / UML / 伯克利 [[论文]](http://arxiv.org/pdf/1412.4729)
* Subhashini Venugopalan、Huijuan Xu、Jeff Donahue、Marcus Rohrbach、Raymond Mooney、Kate Saenko，使用深度循环神经网络将视频翻译为自然语言，arXiv：1412.4729。
* 微软[[论文]](http://arxiv.org/pdf/1505.01861)
* 潘英伟、梅涛、姚婷、李厚强、锐勇，桥梁视频和语言的联合建模嵌入和翻译，arXiv:1505.01861。
* UT / Berkeley / UML [[论文]](http://arxiv.org/pdf/1505.00487)
* Subhashini Venugopalan、Marcus Rohrbach、Jeff Donahue、Raymond Mooney、Trevor Darrell、Kate Saenko，序列到序列 - 视频到文本，arXiv：1505.00487。
* 大学。蒙特利尔/大学。舍布鲁克 [[论文](http://arxiv.org/pdf/1502.08029.pdf)]
* Li Yao、Atousa Torabi、Kyunghyun Cho、Nicolas Ballas、Christopher Pal、Hugo Larochelle、Aaron Courville，利用时间结构描述视频，arXiv:1502.08029
* MPI / 伯克利 [[论文](http://arxiv.org/pdf/1506.01698.pdf)]
* 安娜·罗尔巴赫、马库斯·罗尔巴赫、伯恩特·席勒，电影描述的长短故事，arXiv:1506.01698
* 大学。多伦多/麻省理工学院 [[论文](http://arxiv.org/pdf/1506.06724.pdf)]
* Yukun Zhu、Ryan Kiros、Richard Zemel、Ruslan Salakhutdinov、Raquel Urtasun、Antonio Torralba、Sanja Fidler，《对齐书籍和电影：通过观看电影和阅读书籍实现故事式视觉解释》，arXiv：1506.06724
* 大学。蒙特利尔 [[论文](http://arxiv.org/pdf/1507.01053.pdf)]
* Kyunghyun Cho、Aaron Courville、Yoshua Bengio，使用基于注意力的编码器-解码器网络描述多媒体内容，arXiv:1507.01053
* TAU / USC [[论文](https://arxiv.org/pdf/1612.06950.pdf)]
* Dotan Kaufman、Gil Levi、Tal Hassner、Lior Wolf，用于视频注释和摘要的时间细分，arXiv：1612.06950。

#### 问答
![question_answering](https://cloud.githubusercontent.com/assets/5226447/8452068/ffe7b1f6-2022-11e5-87ab-4f6d4696c220.PNG)
（来自 Stanislaw Antol、Aishwarya Agrawal、Jiasen Lu、Margaret Mitchell、Dhruv Batra、C. Lawrence Zitnick、Devi Parikh、VQA：视觉问答、CVPR、2015 SUNw：场景理解研讨会）

* 弗吉尼亚理工大学/MSR [[Web]](http://www.visualqa.org/) [[Paper]](http://arxiv.org/pdf/1505.00468)
* Stanislaw Antol、Aishwarya Agrawal、Jiasen Lu、Margaret Mitchell、Dhruv Batra、C. Lawrence Zitnick、Devi Parikh、VQA：视觉问答、CVPR、2015 SUNw：场景理解研讨会。
* MPI / 伯克利 [[Web]](https://www.mpi-inf.mpg.de/departments/computer-vision-and-multimodal-computing/research/vision-and-language/visual-turing-challenge/) [[Paper]](http://arxiv.org/pdf/1505.01121)
* Mateusz Malinowski、Marcus Rohrbach、Mario Fritz，询问你的神经元：一种基于神经的方法来回答有关图像的问题，arXiv：1505.01121。
* 多伦多 [[论文]](http://arxiv.org/pdf/1505.02074) [[数据集]](http://www.cs.toronto.edu/~mren/imageqa/data/cocoqa/)
* 任梦野、Ryan Kiros、Richard Zemel，图像问答：视觉语义嵌入模型和新数据集，arXiv:1505.02074 / ICML 2015 深度学习研讨会。
* 百度/加州大学洛杉矶分校 [[论文]](http://arxiv.org/pdf/1505.05612) [[数据集]]()
* 高浩源、毛俊华、周杰、黄志恒、王磊、徐伟，你在和机器说话吗？多语言图像问答数据集和方法，arXiv：1505.05612。
* POSTECH [[论文](http://arxiv.org/pdf/1511.05756.pdf)] [[项目页面](http://cvlab.postech.ac.kr/research/dppnet/)]
* Hyeonwoo Noh、Paul Hongsuck Seo 和 Bohyung Han，使用具有动态参数预测的卷积神经网络进行图像问答，arXiv：1511.05765
* CMU / 微软研究院 [[论文](http://arxiv.org/pdf/1511.02274v2.pdf)]
* 杨Z.、何X.、高J.、邓L. 和Smola, A. (2015)。用于图像问答的堆叠注意力网络。 arXiv：1511.02274。
* MetaMind [[论文](http://arxiv.org/pdf/1603.01417v1.pdf)]
* 熊彩明、史蒂芬·梅里蒂和理查德·索彻。 “用于视觉和文本问答的动态记忆网络。” arXiv：1603.01417（2016）。
* SNU + NAVER [[论文](http://arxiv.org/abs/1606.01455)]
* Jin-Hwa Kim、Sang-Woo Lee、Dong-Hyun Kwak、Min-Oh Heo、Jeonghee Kim、Jung-Woo Ha、Byoung-Tak 张，*用于视觉 QA 的多模态残差学习*，arXiv:1606:01455
* 加州大学伯克利分校 + 索尼 [[论文](https://arxiv.org/pdf/1606.01847)]
* Akira Fukui、Dong Huk Park、Daylen Yang、Anna Rohrbach、Trevor Darrell 和 Marcus Rohrbach，*用于视觉问答和视觉基础的多模态紧凑双线性池*，arXiv：1606.01847
* Postech [[论文](http://arxiv.org/pdf/1606.03647.pdf)]
* Hyeonwoo Noh 和 Bohyung Han，*通过 VQA 联合损失最小化训练循环应答单元*，arXiv：1606.03647
* SNU + NAVER [[论文](http://arxiv.org/abs/1610.04325)]
* Jin-Hwa Kim、Kyoung Woon On、Jeonghee Kim、Jung-Woo Ha、Byoung-Tak 张，*低秩双线性池的 Hadamard 产品*，arXiv：1610.04325。

### 图像生成
* 卷积/循环网络
* Aäron van den Oord、Nal Kalchbrenner、Oriol Vinyals、Lasse Espeholt、Alex Graves、Koray Kavukcuoglu。 “使用 PixelCNN 解码器生成条件图像”[[论文]](https://arxiv.org/pdf/1606.05328v2.pdf)[[代码]](https://github.com/kundan2510/pixelCNN)
* Alexey Dosovitskiy、Jost Tobias Springenberg、Thomas Brox，“学习使用卷积神经网络生成椅子”，CVPR，2015。[[Paper]](http://www.cv-foundation.org/openaccess/content_cvpr_2015/papers/Dosovitskiy_Learning_to_Generate_2015_CVPR_paper.pdf)
* Karol Gregor、Ivo Danihelka、Alex Graves、Danilo Jimenez Rezende、Daan Wierstra，“DRAW：用于图像生成的循环神经网络”，ICML，2015。 [[论文](https://arxiv.org/pdf/1502.04623v2.pdf)]
* 对抗性网络
* Ian J. Goodfellow、Jean Pouget-Abadie、Mehdi Mirza、Bing Xu、David Warde-Farley、Sherjil Ozair、Aaron Courville、Yoshua Bengio，生成对抗网络，NIPS，2014 年。[[论文]](http://arxiv.org/abs/1406.2661)
* Emily Denton、Soumith Chintala、Arthur Szlam、Rob Fergus，使用对抗网络拉普拉斯金字塔的深度生成图像模型，NIPS，2015。[[论文]](http://arxiv.org/abs/1506.05751)
* Lucas Theis、Aäron van den Oord、Matthias Bethge，“生成模型评估说明”，ICLR 2016。 [[论文](http://arxiv.org/abs/1511.01844)]
* 戴振文、Andreas Damianou、Javier Gonzalez、Neil Lawrence，“变分自动编码的深度高斯过程”，ICLR 2016。 [[论文](http://arxiv.org/pdf/1511.06455v2.pdf)]
* Elman Mansimov、Emilio Parisotto、Jimmy Ba、Ruslan Salakhutdinov，“通过注意的字幕生成图像”，ICLR 2016，[[论文](http://arxiv.org/pdf/1511.02793v2.pdf)]
* Jost Tobias Springenberg，“使用分类生成对抗网络进行无监督和半监督学习”，ICLR 2016，[[论文](http://arxiv.org/pdf/1511.06390v1.pdf)]
* Harrison Edwards、Amos Storkey，“与对手审查表征”，ICLR 2016，[[论文](http://arxiv.org/pdf/1511.05897v3.pdf)]
* Takeru Miyato、Shin-ichi Maeda、Masanori Koyama、Ken Nakae、Shin Ishii，“虚拟对抗训练的分布平滑”，ICLR 2016，[[论文](http://arxiv.org/pdf/1507.00677v8.pdf)]
* Jun-Yan Zhu、Philipp Krahenbuhl、Eli Shechtman 和 Alexei A. Efros，“自然图像流形上的生成视觉操作”，ECCV 2016。 [[论文](https://arxiv.org/pdf/1609.03552v2.pdf)] [[代码](https://github.com/junyanz/iGAN)] [[视频](https://youtu.be/9c4z6YsBGQ0)]
* 混合卷积网络和对抗网络
* Alec Radford、Luke Metz、Soumith Chintala，“深度卷积生成对抗网络的无监督表示学习”，ICLR 2016。 [[论文](http://arxiv.org/pdf/1511.06434.pdf)]

### 其他主题
* 视觉类比 [[论文](https://web.eecs.umich.edu/~honglak/nips2015-analogy.pdf)]
* Scott Reed、张一、张雨婷、Honglak Lee，深度视觉类比制作，NIPS，2015 年
* 表面法线估计 [[论文]](http://www.cv-foundation.org/openaccess/content_cvpr_2015/papers/Wang_Designing_Deep_Networks_2015_CVPR_paper.pdf)
* 王小龙、David F. Fouhey、Abhinav Gupta，设计用于表面法线估计的深度网络，CVPR，2015 年。
* 动作检测 [[论文]](http://www.cv-foundation.org/openaccess/content_cvpr_2015/papers/Gkioxari_Finding_Action_Tubes_2015_CVPR_paper.pdf)
* Georgia Gkioxari、Jitendra Malik，寻找动作管，CVPR，2015 年。
* 人群计数 [[论文]](http://www.cv-foundation.org/openaccess/content_cvpr_2015/papers/Zhang_Cross-Scene_Crowd_Counting_2015_CVPR_paper.pdf)
* 张聪、李红生、王晓刚、杨晓康，基于深度卷积神经网络的跨场景人群计数，CVPR，2015。
* 3D 形状检索 [[论文]](http://www.cv-foundation.org/openaccess/content_cvpr_2015/papers/Wang_Sketch-Based_3D_Shape_2015_CVPR_paper.pdf)
* 王芳、康乐、李毅，使用卷积神经网络进行基于草图的 3D 形状检索，CVPR，2015 年。
* 弱监督分类
* Samaneh Azadi、Jiashi Feng、Stefanie Jegelka、Trevor Darrell，“带有噪声标签的深度 CNN 的辅助图像正则化”，ICLR 2016，[[论文](http://arxiv.org/pdf/1511.07069v2.pdf)]
* 艺术风格 [[论文]](http://arxiv.org/abs/1508.06576) [[代码]](https://github.com/jcjohnson/neural-style)
* Leon A. Gatys、Alexander S. Ecker、Matthias Bethge，艺术风格的神经算法。
* 人类视线估计
* 张旭聪、Yusuke Sugano、Mario Fritz、Andreas Bulling，基于外观的野外注视估计，CVPR，2015。[[论文]](http://www.cv-foundation.org/openaccess/content_cvpr_2015/papers/Zhang_Appearance-Based_Gaze_Estimation_2015_CVPR_paper.pdf) [[网站]](https://www.mpi-inf.mpg.de/departments/computer-vision-and-multimodal-computing/research/gaze-based- human-computer-interaction/appearance-based-gaze-estimation-in-the-wild-mpiigaze/)
* 人脸识别
* Yaniv Taigman、Ming Yang、Marc'Aurelio Ranzato、Lior Wolf、DeepFace：缩小人脸验证方面与人类水平性能的差距，CVPR，2014 年。[[论文]](https://www.cs.toronto.edu/~ranzato/publications/taigman_cvpr14.pdf)
* 孙毅，梁丁，王晓刚，唐晓鸥，DeepID3：超深度神经网络人脸识别，2015。 [[论文]](http://arxiv.org/abs/1502.00873)
* Florian Schroff、Dmitry Kalenichenko、James Philbin，FaceNet：人脸识别和聚类的统一嵌入，CVPR，2015 年。[[论文]](http://arxiv.org/abs/1503.03832)
* 面部标志检测
* Yue Wu、Tal Hassner、KangGeon Kim、Gerard Medioni、Prem Natarajan，使用调整的卷积神经网络进行面部标志检测，2015 年。[[Paper]](http://arxiv.org/abs/1511.04031) [[项目]](http://www.openu.ac.il/home/hassner/projects/tcnn_landmarks/)

## 课程
* 深视
* [斯坦福] [CS231n：用于视觉识别的卷积神经网络](http://cs231n.stanford.edu/)
* [香港中文大学] [ELEG 5040：信号处理高级专题(深度学习导论)](https://piazza.com/cuhk.edu.hk/spring2015/eleg5040/home)
* 更多深度学习
* [斯坦福] [CS224d：自然语言处理的深度学习](http://cs224d.stanford.edu/)
* [牛津] [Nando de Freitas 教授的深度学习](https://www.cs.ox.ac.uk/people/nando.defreitas/machinelearning/)
* [纽约大学] [Yann LeCun 教授的深度学习](http://cilvr.cs.nyu.edu/doku.php?id=courses:deeplearning2014:start)

## 书籍
* 免费在线书籍
  * [深度学习 作者：Ian Goodfellow、Yoshua Bengio 和 Aaron Courville](http://www.iro.umontreal.ca/~bengioy/dlbook/)
  * [神经网络和深度学习 作者：Michael Nielsen](http://neuralnetworksanddeeplearning.com/)
  * [蒙特利尔大学 LISA 实验室的深度学习教程](http://deeplearning.net/tutorial/deeplearning.pdf)

## 视频
* 会谈
  * [深度学习、自学学习和无监督特征学习 作者：Andrew Ng](https://www.youtube.com/watch?v=n1ViNeWhC24)
  * [深度学习的最新进展 作者：Geoff Hinton](https://www.youtube.com/watch?v=vShMxxqtDDs)
  * [深度学习的不合理有效性作者：Yann LeCun](https://www.youtube.com/watch?v=sc-KbuZqGkI)
  * [Yoshua Bengio 的深度表示学习](https://www.youtube.com/watch?v=4xsVFLnHC_0)


## 软件
### 框架
* Tensorflow：谷歌使用数据流图进行数值计算的开源软件库 [[Web](https://www.tensorflow.org/)]
* Torch7：Lua 中的深度学习库，由 Facebook 和 Google Deepmind 使用 [[Web](http://torch.ch/)]
* 基于Torch的深度学习库：[[torchnet](https://github.com/torchnet/torchnet)],
* Caffe：BVLC 的深度学习框架 [[Web](http://caffe.berkeleyvision.org/)]
* Theano：Python 数学库，由 LISA 实验室维护 [[Web](http://deeplearning.net/software/theano/)]
* 基于 Theano 的深度学习库：[[Pylearn2](http://deeplearning.net/software/pylearn2/)]、[[Blocks](https://github.com/mila-udem/blocks)]、[[Keras](http://keras.io/)]、[[Lasagne](https://github.com/Lasagne/Lasagne)]
* MatConvNet：用于 MATLAB 的 CNN [[Web](http://www.vlfeat.org/matconvnet/)]
* MXNet：一个灵活高效的深度学习库，适用于异构分布式系统，支持多语言 [[Web](http://mxnet.io/)]
* Deepgaze：基于 CNN 的人机交互计算机视觉库 [[Web](https://github.com/mpatacchiola/deepgaze)]

### 应用领域
* 对抗训练
* 论文“生成对抗网络”的代码和超参数 [[Web]](https://github.com/goodfeli/adversarial)
* 理解和可视化
* “通过反转理解深度图像表示”的源代码，CVPR，2015。 [[Web]](https://github.com/aravindhm/deep-goggle)
* 语义分割
* 论文“用于精确对象检测和语义分割的丰富特征层次结构”的源代码，CVPR，2014。 [[Web]](https://github.com/rbgirshick/rcnn)
* 论文“Fully Convolutional Networks for Semantic Segmentation”的源代码，CVPR，2015。 [[Web]](https://github.com/longjon/caffe/tree/future)
* 超分辨率
* 动漫风格艺术的图像超分辨率 [[Web]](https://github.com/nagadomi/waifu2x)
* 边缘检测
* 论文“DeepContour：通过正共享损失学习的深度卷积特征进行轮廓检测”的源代码，CVPR，2015。 [[Web]](https://github.com/shenwei1231/DeepContour)
* 论文“整体嵌套边缘检测”的源代码，ICCV 2015。 [[Web]](https://github.com/s9xie/hed)

## 教程
* [CVPR 2014] [计算机视觉深度学习教程](https://sites.google.com/site/deeplearningcvpr2014/)
* [CVPR 2015] [利用 Torch 进行计算机视觉应用深度学习](https://github.com/soumith/cvpr2015)

## 博客
* [兔子洞深处：CVPR 2015 及以后@Tombone 的计算机视觉博客](http://www.computervisionblog.com/2015/06/deep-down-rabbit-hole-cvpr-2015-and.html)
* [CVPR 回顾和我们的目标@Zoya Bylinskii（麻省理工学院博士生）的博客](http://zoyathinks.blogspot.kr/2015/06/cvpr-recap-and-where-were-going.html)
* [Facebook 的 AI 绘画@Wired](http://www.wired.com/2015/06/facebook-googles-fake-brains-spawn-new-visual-reality/)
* [盗梦空间：深入探讨神经网络@Google Research](http://googleresearch.blogspot.kr/2015/06/inceptionism-going-deeper-into-neural.html)
* [实施神经网络](http://peterroelants.github.io/)
