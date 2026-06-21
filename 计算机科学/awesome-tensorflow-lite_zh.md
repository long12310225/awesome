<p align="center">
    <img src="images/awesome-tflite.png" alt="awesome tflite" width="500">
</p>

<!-- omit in toc -->
# 很棒的 TensorFlow Lite [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[TensorFlow Lite](https://www.tensorflow.org/lite) 是一组工具，可帮助转换和优化 TensorFlow 模型以在移动和边缘设备上运行。目前它在超过 40 亿台设备上运行！借助 TensorFlow 2.x，您可以使用 tf.Keras 训练模型，轻松将模型转换为 .tflite 并进行部署；或者您可以从模型动物园下载预训练的 TensorFlow Lite 模型。

这是一个很棒的 TensorFlow Lite 模型列表，其中包含示例应用程序、有用的工具和学习资源 -
* 展示社区使用 TensorFlow Lite 构建的内容
* 将所有样本并排放置，以便于参考
* 分享知识和学习资源

如果您想贡献并遵循[此处](CONTRIBUTING.md) 的指南，请提交 PR。

<!-- omit in toc -->
## 内容
- [过去的公告：](#past-announcements)
- [带样品的模型](#models-with-samples)
  - [计算机视觉](#computer-vision)
    - [Classification](#classification)
    - [Detection](#detection)
    - [Segmentation](#segmentation)
    - [风格转移](#style-transfer)
    - [Generative](#generative)
    - [事后估算](#post-estimation)
    - [Other](#other)
  - [Text](#text)
  - [Speech](#speech)
  - [Recommendation](#recommendation)
  - [Game](#game)
- [模型动物园](#model-zoo)
  - [TensorFlow Lite 模型](#tensorflow-lite-models)
  - [TensorFlow 模型](#tensorflow-models)
- [想法和灵感](#ideas-and-inspiration)
- [机器学习套件示例](#ml-kit-examples)
- [插件和 SDK](#plugins-and-sdks)
- [有用的链接](#helpful-links)
- [学习资源](#learning-resources)
  - [博客文章](#blog-posts)
  - [Books](#books)
  - [Videos](#videos)
  - [Podcasts](#podcasts)
  - [MOOCs](#moocs)

## 过去的公告：
以下是 TensorFlow Lite 过去发布的一些功能：
* [Announcement of the new converter](https://groups.google.com/a/tensorflow.org/d/msg/tflite/Z_h7706dt8Q/sNrjPj4yGgAJ) - 基于 [MLIR](https://medium.com/tensorflow/mlir-a-new-intermediate-representation-and-compiler-framework-beba999ed18d)，支持新类型模型的转换，例如 Mask R-CNN 和 Mobile BERT 等，支持功能控制流和转换过程中更好的错误处理。默认情况下在夜间构建中启用。
* [Android Support Library](https://github.com/tensorflow/tflite-support/tree/master/tensorflow_lite_support/java) - 使移动开发更容易（[Android](https://github.com/tensorflow/examples/blob/master/lite/examples/image_classification/android/EXPLORE_THE_CODE.md)示例代码）。
* [Model Maker](https://www.tensorflow.org/lite/guide/model_maker) - 只需几行代码即可轻松创建自定义[图像和文本](https://github.com/tensorflow/examples/tree/master/tensorflow_examples/lite/model_maker)分类模型。请参阅下面的图标分类器，了解社区提供的教程。
* [On-device training](https://blog.tensorflow.org/2019/12/example-on-device-model-personalization.html) - 终于来了！目前仅限于图像分类的迁移学习，但这是一个很好的开始。请参阅官方 [Android](https://github.com/tensorflow/examples/blob/master/lite/examples/model_personalization/README.md) 示例代码和社区中的另一代码（[博客](https://aqibsaeed.github.io/on-device-activity-recognition) | [Android](https://github.com/aqibsaeed/on-device-activity-recognition)）。
* [Hexagon delegate](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/g3doc/performance/hexagon_delegate.md) - 如何使用 Hexagon Delegate 加速移动和边缘设备上的模型推理。另请参阅博客文章[在 Qualcomm Hexagon DSP 上加速 TensorFlow Lite](https://blog.tensorflow.org/2019/12/acceleating-tensorflow-lite-on-qualcomm.html)。
* [Model Metadata](https://www.tensorflow.org/lite/convert/metadata) - 提供模型描述标准，还支持 [Code Gen 和 Android Studio ML 模型绑定](https://www.tensorflow.org/lite/inference_with_metadata/codegen)。

## 带样品的模型
以下是带有应用/设备实现和参考的 TensorFlow Lite 模型。
注意：其中包含来自 MediaPipe 的预训练 TensorFlow Lite 模型，您可以使用或不使用 MediaPipe 来实现。

### 计算机视觉

#### 分类

|任务|型号|应用程序\|参考|来源 |
| ------------------------------- |-------------------------------------------------------------------------------------------------------------------------------------------------------------------| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------       | -------------------|
|分类| MobileNetV1（[下载](https://storage.googleapis.com/download.tensorflow.org/models/tflite/mobilenet_v1_1.0_224_quant_and_labels.zip)) | [Android](https://github.com/tensorflow/examples/tree/master/lite/examples/image_classification/android) \| [iOS](https://github.com/tensorflow/examples/tree/master/lite/examples/image_classification/ios) \| [树莓派](https://github.com/tensorflow/examples/tree/master/lite/examples/image_classification/raspberry_pi) \| [概述](https://www.tensorflow.org/lite/models/image_classification/overview) |张量流.org |
|分类|移动网络V2 |在 Android 上识别花朵 [Codelab](https://codelabs.developers.google.com/codelabs/recognize-flowers-with-tensorflow-on-android/#0) \| [Android](https://github.com/tensorflow/examples/tree/master/lite/codelabs/flower_classification/android) | TensorFlow 团队 |
|分类|移动网络V2 |皮肤病变检测 [Android](https://github.com/AakashKumarNain/skin_cancer_detection/tree/master/demo) |社区 |
|分类|移动网络V2 |美国手语检测\| [Colab 笔记本](https://colab.research.google.com/drive/1xsunX7Qj_XWBZwcZLyjsKBg4RI0DNo2-?usp=sharing) \| [Android](https://github.com/sayannath/American-Sign-Language-Detection) |社区 |
|分类| CNN + 量化感知训练 |石头剪刀布检测【Colab Notebook】(https://colab.research.google.com/drive/1Wdso2N_76E8Xxniqd4C6T1sV5BuhKN1o?usp=sharing) \| [颤动](https://github.com/sayannath/American-Sign-Language-Detection) |社区 |
|分类| EfficientNet-Lite0（[下载](https://github.com/margaretmz/icon-classifier/blob/master/ml-code/icons-50.tflite)) |图标分类器 [Colab 和 Android](https://github.com/margaretmz/icon-classifier) \| [教程1](https://medium.com/swlh/icon-classifier-with-tflite-model-maker-9263c0021f72) \| [教程 2](https://medium.com/@margaretmz/icon-classifier-android-app-1fc0b727f761) |社区 |

#### 检测
|任务|型号|应用程序\|参考|来源 |
| -|-|-|-|
|物体检测|量化 COCO SSD MobileNet v1（[下载](https://storage.googleapis.com/download.tensorflow.org/models/tflite/coco_ssd_mobilenet_v1_1.0_quant_2018_06_29.zip)）| [Android](https://github.com/tensorflow/examples/tree/master/lite/examples/object_detection/android) \| [iOS](https://github.com/tensorflow/examples/tree/master/lite/examples/object_detection/ios) \| [概述](https://www.tensorflow.org/lite/models/object_detection/overview#starter_model) |张量流.org |
|物体检测|优洛 | [颤动](https://blog.francium.tech/real-time-object-detection-on-mobile-with-flutter-tensorflow-lite-and-yolo-android-part-a0042c9b62c6) \| [论文](https://arxiv.org/abs/1506.02640) |社区 |
|物体检测| [YOLOv5](https://tfhub.dev/neso613/lite-model/yolo-v5-tflite/tflite_model/1) | [Yolov5 推理](https://github.com/neso613/yolo-v5-tflite-model) |社区 |
|物体检测| MobileNetV2 SSD（[下载](https://github.com/google/mediapipe/tree/master/mediapipe/models/ssdlite_object_detection.tflite)) | [参考](https://github.com/google/mediapipe/blob/master/mediapipe/models/object_detection_saved_model/README.md) |媒体管道 |
|物体检测| MobileDet（[论文](https://arxiv.org/abs/2004.14525)) | [博客文章（包括 TFLite 转换过程）](https://sayak.dev/mobiledet-optimization/) | MobileDet 来自威斯康星大学麦迪逊分校和 Google，博客文章来自社区 |
|车牌检测| SSD MobileNet [（下载）](https://github.com/ariG23498/Flutter-License/blob/master/assets/detect.tflite) | [颤动](https://github.com/ariG23498/Flutter-License) |社区 |
|人脸检测| BlazeFace（[下载](https://github.com/google/mediapipe/tree/master/mediapipe/models/face_detection_front.tflite)) | [论文](https://sites.google.com/corp/view/perception-cv4arvr/blazeface) |媒体管道 |
|人脸认证 | [FaceNet](https://arxiv.org/pdf/1503.03832.pdf) | [Flutter](https://github.com/sayannath/Face-Authentication-App) |社区 |
|手部检测和跟踪 |手掌检测和手部标志（[下载](https://github.com/google/mediapipe/tree/master/mediapipe/models#hand-detection-and-tracking)) | [博客文章](https://mediapipe.page.link/handgoogleaiblog) \| [模型卡](https://mediapipe.page.link/handmc) \|  [Android](https://github.com/supremetech/mediapipe-demo-hand-detection) | MediaPipe 和社区 |

#### 细分
|任务|型号|应用程序\|参考|来源 |
| -|-|-|-|
|细分| DeepLab V3（[下载](https://storage.googleapis.com/download.tensorflow.org/models/tflite/gpu/deeplabv3_257_mv_gpu.tflite)）| [Android 和 iOS](https://github.com/tensorflow/examples/tree/master/lite/examples/image_segmentation/) \| [概述](https://www.tensorflow.org/lite/models/segmentation/overview) \| Flutter [图片](https://github.com/kshitizrimal/Flutter-TFLite-Image-Segmentation) \| [实时](https://github.com/kshitizrimal/tflite-realtime-flutter) \| [论文](https://arxiv.org/abs/1706.05587) | tf.org 和社区 |
|细分| [DeepLab V3 模型的不同变体](https://github.com/tensorflow/models/blob/master/research/deeplab/g3doc/model_zoo.md) |  [TF Hub](https://tfhub.dev/s?module-type=image-segmentation&publisher=sayakpaul) 上使用 Colab Notebooks 的模型 |社区 |
|细分| [DeepLab V3 模型](https://tfhub.dev/tensorflow/lite-model/deeplabv3/1/metadata/2?lite-format=tflite) |  [Android](https://github.com/farmaker47/Update_image_segmentation) \| [教程](https://farmaker47.medium.com/use-camerax-with-image-segmentation-android-project-d8656f35cea3) |社区 |
|头发分割| [下载](https://github.com/google/mediapipe/tree/master/mediapipe/models/hair_segmentation.tflite) | [论文](https://sites.google.com/corp/view/perception-cv4arvr/hair-segmentation) |媒体管道 |

#### 风格转移
|任务|型号|应用程序\|参考|来源 |
| -|-|-|-|
|风格转移| [任意图像风格化](https://github.com/tensorflow/magenta/tree/master/magenta/models/当中任意_image_stylization) | [概述](https://www.tensorflow.org/lite/models/style_transfer/overview) \| [Android](https://github.com/tensorflow/examples/tree/master/lite/examples/style_transfer/android) \| [颤动](https://github.com/PuzzleLeaf/flutter_tflite_style_transfer) | tf.org 和社区 |
|风格转移| .tflite 中质量更好的风格迁移模型 |  [TF Hub](https://tfhub.dev/sayakpaul/lite-model/ Arbitration-image-stylization-inceptionv3/dr/predict/1) 上使用 Colab Notebooks 的模型 |社区 |
|视频风格迁移 |下载：<br> [动态范围模型](https://tfhub.dev/sayakpaul/lite-model/任意-image-stylization-inceptionv3-dynamic-shapes/dr/transfer/1)) | [Android](https://github.com/farmaker47/video_style_transfer) \| [教程](https://medium.com/@farmaker47/android-implementation-of-video-style-transfer-with-tensorflow-lite-models-9338a6d2a3ea) |社区 |
|细分和风格转移| DeepLabV3 和风格迁移 [模型](https://github.com/margaretmz/segmentation-style-transfer/tree/master/ml) | [项目仓库](https://github.com/margaretmz/segmentation-style-transfer) \| [Android](https://github.com/margaretmz/segmentation-style-transfer/tree/master/android) \| [教程](https://medium.com/google-developer-experts/image-background-stylizer-part-1-project-intro-d68c4547e7e3) |社区 |
#### 生成式
|任务|型号|应用程序\|参考|来源 |
| -|-|-|-|
| GAN | [U-GAT-IT](https://github.com/taki0112/UGATIT) (Selfie2Anime) | [项目仓库](https://github.com/margaretmz/selfie2anime-with-tflite) \| [Android](https://github.com/margaretmz/selfie2anime-with-tflite/tree/master/android) \| [教程](https://medium.com/google-developer-experts/selfie2anime-with-tflite-part-1-overview-f97500800ffe) |社区 |
| GAN | [白盒CartoonGAN](https://github.com/SystemErrorWang/White-box-Cartoonization) ([下载](https://tfhub.dev/sayakpaul/lite-model/cartoongan/dr/1)) | [项目仓库](https://github.com/margaretmz/Cartoonizer-with-TFLite) \| [Android](https://github.com/margaretmz/Cartoonizer-with-TFLite/tree/master/android) \| [教程](https://blog.tensorflow.org/2020/09/how-to-create-cartoonizer-with-tf-lite.html) |社区 |
| GAN - 图像外推 | [TF Hub](https://tfhub.dev/sayakpaul/lite-model/boundless-quarter/dr/1) 上的无界 | [Colab 笔记本](https://colab.research.google.com/github/sayakpaul/Adventures-in-TensorFlow-Lite/blob/master/Boundless_TFLite.ipynb) \| [原始论文](https://arxiv.org/pdf/2003.06792v2.pdf) |社区 |
#### 事后估算
|任务|型号|应用程序\|参考|来源 |
| -|-|-|-|
|姿势估计| Posenet（[下载](https://storage.googleapis.com/download.tensorflow.org/models/tflite/posenet_mobilenet_v1_100_257x257_multi_kpt_stripped.tflite)) | [Android](https://github.com/tensorflow/examples/tree/master/lite/examples/posenet/android) \| [iOS](https://github.com/tensorflow/examples/tree/master/lite/examples/posenet/ios) \| [概述](https://www.tensorflow.org/lite/models/pose_estimation/overview) |张量流.org |
|基于姿势分类的视频游戏控制| MoveNet Lightning（[下载](https://github.com/NSTiwari/Video-Game-Control-using-Pose-Classification-and-TensorFlow-Lite/blob/main/movenet_lightning.tflite)) | [项目存储库](https://github.com/NSTiwari/Video-Game-Control-using-Pose-Classification-and-TensorFlow-Lite) |社区 |


#### 其他
|任务|型号|应用程序\|参考|来源 |
| -|-|-|-|
|低光图像增强 | [TF Hub 上的模型](https://tfhub.dev/sayakpaul/mirnet-fixed/1) | [项目仓库](https://github.com/sayakpaul/MIRNet-TFLite) \| [原始论文](https://arxiv.org/pdf/2003.06792v2.pdf) \| [颤动](https://github.com/sayannath/MIRNet-Flutter)|                                                                                                                           |社区 |
| OCR |[TF Hub 上的模型](https://tfhub.dev/tulasiram58827/lite-model/keras-ocr/dr/2) | [项目存储库](https://github.com/tulasiram58827/ocr_tflite) |社区


### 文字
|任务|型号|示例应用程序 |来源 |
| ------------------- |---------------------------------------------------------------------------------------------------------------------------------| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
|问答 |蒸馏伯特 | [Android](https://github.com/huggingface/tflite-android-transformers/blob/master/bert) |拥抱脸|
|文本生成| GPT-2 / DistilGPT2 | [Android](https://github.com/huggingface/tflite-android-transformers/blob/master/gpt2) |拥抱脸|
|文本分类| [下载](https://storage.googleapis.com/download.tensorflow.org/models/tflite/text_classification/text_classification.tflite) | [Android](https://github.com/tensorflow/examples/tree/master/lite/examples/text_classification/android) \|[iOS](https://github.com/khurram18/TextClassafication) \| [颤动](https://github.com/am15h/tflite_flutter_plugin/tree/master/example) | tf.org 和社区 |
|文本检测 | CRAFT 文本检测器（[论文](https://arxiv.org/pdf/1904.01941)) |[下载](https://github.com/tulasiram58827/craft_tflite/blob/main/models/craft_float_800.tflite?raw=true) \| [项目存储库](https://github.com/tulasiram58827/craft_tflite/) \| [博客1-转换为TFLite](https://tulasi.dev/craft-in-tflite) \| [Blog2-EAST 与 CRAFT](https://sayak.dev/optimizing-text- detectors/) \| [TF Hub 上的模型](https://tfhub.dev/tulasiram58827/lite-model/craft-text- detector/dr/1) \| Android（即将推出）|社区 |
|文本检测 | EAST 文本检测器（[论文](https://arxiv.org/abs/1704.03155)) |[TF Hub 上的模型](https://tfhub.dev/sayakpaul/lite-model/east-text- detector/dr/1) \| [转换和推理笔记本](https://colab.research.google.com/github/sayakpaul/Adventures-in-TensorFlow-Lite/blob/master/EAST_TFLite.ipynb) |社区 |

### 演讲
|任务|型号|应用程序\|参考|来源 |
| ------------------ |------------------------------------| ------------------------------------------------------------------------------------- | ------------ |
|语音识别 |深度语音 | [参考](https://github.com/mozilla/DeepSpeech/tree/master/native_client/java) |火狐 |
|语音识别 |符合者| [推理](https://github.com/neso613/ASR_TFLite) [Android](https://github.com/windmaple/tflite-asr) |社区 |
|语音合成 | Tacotron-2、FastSpeech2、MB-Melgan | [Android](https://github.com/TensorSpeech/TensorflowTTS/tree/master/examples/android) |张量语音 |
|语音合成(TTS) | Tacotron2、FastSpeech2、MelGAN、MB-MelGAN、HiFi-GAN、Parallel WaveGAN | [推理笔记本](https://github.com/tulasiram58827/TTS_TFLite/blob/main/End_to_End_TTS.ipynb) \| [项目库](https://github.com/tulasiram58827/TTS_TFLite/) |社区 |

### 推荐
|任务|型号|应用程序\|参考|来源 |
| ------------------ |------------------------------------| ------------------------------------------------------------------------------------- | ------------ |
|设备端推荐 | [双编码器](https://github.com/tensorflow/examples/tree/master/lite/examples/recommendation/ml) | [Android](https://github.com/tensorflow/examples/tree/master/lite/examples/recommendation/android) \| [iOS](https://github.com/zhuzilin/on-device_recommendation_tflite) \| [参考](https://blog.tensorflow.org/2020/09/introduction-to-tflite-on-device-recommendation.html) | tf.org 和社区 |

### 游戏
|任务|型号|应用程序\|参考|来源 |
| ------------------ |------------------------------------| ------------------------------------------------------------------------------------- | ------------ |
|游戏代理|强化学习 | [颤振](https://github.com/windmaple/planestrike-flutter) \| [教程](https://windmaple.medium.com/) |社区 |



## 模型动物园

### TensorFlow Lite 模型
这些是可以在应用程序和事物中实现的 TensorFlow Lite 模型：
* [MobileNet](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/README.md) - 预训练的 MobileNet v2 和 v3 模型。
* TensorFlow Lite 模型
  * [TensorFlow Lite models](https://www.tensorflow.org/lite/models) - 带有官方 Android 和 iOS 示例。
  * [Pretrained models](https://www.tensorflow.org/lite/guide/hosted_models) - 量化和浮点变体。
  * [TensorFlow Hub](https://tfhub.dev/) - 设置“Model format = TFLite”以查找 TensorFlow Lite 模型。

### TensorFlow 模型
这些是 TensorFlow 模型，可以转换为 .tflite，然后在应用程序和事物中实现：
* [TensorFlow models](https://github.com/tensorflow/models/tree/master/official) - 官方 TensorFlow 模型。
* [Tensorflow detection model zoo](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2_detection_zoo.md) - 在 COCO、KITTI、AVA v2.1、iNaturalist Species 数据集上进行预训练。

## 想法和灵感
* [E2E TFLite Tutorials](https://github.com/ml-gde/e2e-tflite-tutorials) - 查看此存储库以获取示例应用程序创意并为您的教程项目寻求帮助。项目完成后，TensorFlow Lite 模型、示例代码和教程的链接将添加到这个很棒的列表中。

## 机器学习套件示例
[ML Kit](https://developers.google.com/ml-kit) 是一款移动 SDK，可为移动开发者带来 Google 的 ML 专业知识。
* 2019-10-01 [ML Kit 翻译演示](https://codelabs.developers.google.com/codelabs/mlkit-android-translate/#0) - 材料设计教程 [Android](https://github.com/googlecodelabs/mlkit-android/tree/master/translate) (Kotlin) 示例 - 使用 ML Kit for Firebase 识别、识别来自实时摄像头的语言并翻译文本。
* 2019-03-13 [使用 ML Kit 的计算机视觉 - Flutter In Focus](https://youtu.be/ymyYUCrJnxU)。
* 2019-02-09 [Flutter + MLKit：名片邮件提取器](https://medium.com/flutter-community/flutter-mlkit-8039ec66b6a) - 一篇包含 [Flutter](https://github.com/DaemonLoki/Business-Card-Mail-Extractor) 示例代码的博客文章。
* 2019-02-08 [从 TensorFlow 到 ML Kit：通过机器学习为您的 Android 应用程序提供动力](https://speakerdeck.com/jinqian/from-tensorflow-to-ml-kit-power-your-android-application-with-machine-learning) - 与 [Android](https://github.com/xebia-france/magritte) (Kotlin) 示例代码的对话。
* 2018-08-07 [使用 TensorFlow Lite 在 Android 上构建自定义机器学习模型](https://medium.com/over-engineering/building-a-custom-machine-learning-model-on-android-with-tensorflow-lite-26447e53abf2)。
* 2018-07-20 [Flutter 中的 ML Kit 和人脸检测](https://flatteredwithflutter.com/ml-kit-and-face-detection-in-flutter/)。
* 2018-07-27 [Android 4 上的 ML Kit：地标检测](https://medium.com/google-developer-experts/exploring-firebase-mlkit-on-android-landmark-detection-part-four-5e86b8deac3a)。
* 2018-07-28 [Android 3 上的 ML Kit：条码扫描](https://medium.com/google-developer-experts/exploring-firebase-mlkit-on-android-barcode-scanning-part- Three-cc6f5921a108)。
* 2018-05-31 [Android 2 上的 ML Kit：人脸检测](https://medium.com/google-developer-experts/exploring-firebase-mlkit-on-android-face-detection-part-two-de7e307c52e0)。
* 2018-05-22 [Android 上的 ML Kit 1：简介](https://medium.com/google-developer-experts/exploring-firebase-mlkit-on-android-introducing-mlkit-part-one-98fcfedbeee0)。

## 插件和 SDK
* [Edge Impulse](https://www.edgeimpulse.com/) - 由 [@EdgeImpulse](https://twitter.com/EdgeImpulse) 创建，帮助您在云中为嵌入式设备训练 TensorFlow Lite 模型。
* [MediaPipe](https://github.com/google/mediapipe) - Google AI 的跨平台（移动、桌面和 Edge TPU）AI 管道。 （PM [明勇](https://twitter.com/realmgyong)) | [MediaPipe 示例](https://mediapipe.readthedocs.io/en/latest/examples.html)。
* [Coral Edge TPU](https://coral.ai/) - 谷歌的边缘硬件。 [Coral Edge TPU 示例](https://coral.ai/examples/)。
* [TensorFlow Lite Flutter Plugin](https://github.com/am15h/tflite_flutter_plugin/) - 提供类似于 TensorFlow Lite Java API 的 dart API，用于访问 TensorFlow Lite 解释器并在 flutter 应用程序中执行推理。 [pub.dev 上的 tflite_flutter](https://pub.dev/packages/tflite_flutter)。

## 有用的链接
* [Netron](https://github.com/lutzroeder/netron) - 可视化模型的工具。
* [AI benchmark](http://ai-benchmark.com/tests.html) - 用于对智能手机上的计算机视觉模型进行基准测试的网站。
* [Performance measurement](https://www.tensorflow.org/lite/performance/measurement) - 如何衡量 Android 和 iOS 上的模型性能。
* [Material design guidelines for ML](https://material.io/collections/machine-learning/patterns-for-machine-learning-powered-features.html) - 如何设计机器学习驱动的功能。一个很好的例子：[ML Kit Showcase App](https://github.com/firebase/mlkit-material-android)。
* [The People + AI Guide book](https://pair.withgoogle.com/) - 了解如何设计以人为本的人工智能产品。
* [Adventures in TensorFlow Lite](https://github.com/sayakpaul/Adventures-in-TensorFlow-Lite) - 显示 TensorFlow Lite 中重要转换过程和一般探索的存储库。
* [TFProfiler](https://github.com/iglaweb/TFProfiler) - 一款基于 Android 的应用程序，用于分析 TensorFlow Lite 模型并测量其在智能手机上的性能。
* [适用于微控制器的 TensorFlow Lite](https://www.tensorflow.org/lite/microcontrollers)
* [TensorFlow Lite Examples - Android](https://github.com/dailystudio/tensorflow-lite-examples-android) - 存储库重构并重写了 TensorFlow 官方网站中包含的所有 TensorFlow Lite Android 示例。
* [Tensorflow-lite-kotlin-samples](https://github.com/SunitRoy2703/Tensorflow-lite-kotlin-samples) - Kotlin 中的 Tensorflow Lite Android 示例应用程序集合，用于展示 [示例应用程序] 的不同类型的 kotlin 实现(https://www.tensorflow.org/lite/examples)


## 学习资源
有兴趣但不确定如何开始？这里有一些学习资源，无论您是该领域的初学者还是从业者，都会对您有所帮助。

### 博客文章

* 2021-11-09 [TensorFlow Lite 设备上训练](https://blog.tensorflow.org/2021/11/on-device-training-in-tensorflow-lite.html)
* 2021-09-27 [使用 TensorFlow Lite 进行光学字符识别：一个新的示例应用程序](https://blog.tensorflow.org/2021/09/blog.tensorflow.org202109optical-character-recognition.html)
* 2021-06-16 [https://blog.tensorflow.org/2021/06/easier-object-detection-on-mobile-with-tf-lite.html](https://blog.tensorflow.org/2021/11/on-device-training-in-tensorflow-lite.html)
* 2020 年 12 月 29 日 [YOLOv3 到 TensorFlow Lite 转换](https://medium.com/analytics-vidhya/yolov3-to-tensorflow-lite-conversion-4602cec5c239) - 作者：Nitin Tiwari。
* 2020-04-20 [TensorFlow Lite 的新增功能](https://blog.tensorflow.org/2020/04/whats-new-in-tensorflow-lite-from-devsum​​mit-2020.html) - 作者：Khanh LeViet。
* 2020-04-17 [优化样式传输以使用 TFLite 在移动设备上运行](https://blog.tensorflow.org/2020/04/optimizing-style-transfer-to-run-on-mobile-with-tflite.html) - 作者：Khanh LeViet 和 Luiz Gustavo Martins。
* 2020-04-14 [TensorFlow Lite 如何帮助您从原型到产品](https://blog.tensorflow.org/2020/04/how-tensorflow-lite-helps-you-from-prototype-to-product.html) - 作者：Khanh LeViet。
* 2019-11-08 [在带有 TensorFlow 的 MCU 上开始使用 ML](https://blog.article.io/2019/11/08/article-machine-learning-101/) - 作者：Brandon Satrom。
* 2019-08-05 [TensorFlow 模型优化工具包 — float16 量化使模型大小减半](https://blog.tensorflow.org/2019/08/tensorflow-model-optimization-toolkit_5.html) - 由 TensorFlow 团队提供。
* 2018-07-13 [使用 Cloud TPU 在 30 分钟内训练和服务实时移动物体检测器](https://blog.tensorflow.org/2018/07/training-and-serving-realtime-mobile-object- detector-cloud-tpus.html) - 作者：Sara Robinson、Aakanksha Chowdhery 和 Jonathan Huang。
* 2018-06-11 - [为什么机器学习的未来很小](https://petewarden.com/2018/06/11/why-the-future-of-machine-learning-is-tiny/) - 作者：Pete Warden。
* 2018-03-30 - [在 Android 上使用 TensorFlow Lite](https://blog.tensorflow.org/2018/03/using-tensorflow-lite-on-android.html)) - 作者：Laurence Moroney。

### 书籍
* 2021 年 12 月 1 日 [人工智能和机器学习设备上开发](https://learning.oreilly.com/library/view/ai-and-machine/9781098101732/)（早期访问）- 作者：Laurence Moroney ([@lmoroney](https://twitter.com/lmoroney))。
* 2020-10-01 [编码员的人工智能和机器学习](https://learning.oreilly.com/library/view/ai-and-machine/9781492078180/) - 作者：Laurence Moroney ([@lmoroney](https://twitter.com/lmoroney))。
* 2020-04-06 [使用 TensorFlow Lite、ML Kit 和 Flutter 进行移动深度学习](https://www.packtpub.com/product/mobile-deep-learning-with-tensorflow-lite-ml-kit-and-flutter/9781789611212)：构建可扩展的实际项目以在 Android 和 iOS 上实现端到端神经网络([GitHub](https://github.com/PacktPublishing/Mobile-Deep-Learning-Projects)) - 作者：Anubhav Singh ([@xprilion](https://github.com/xprilion)) 和 Rimjhim Bhadani ([@Rimjhim28](https://github.com/Rimjhim28))。
* 2020-03-01 用于计算机视觉的 Raspberry Pi ([完整包](https://www.pyimagesearch.com/raspberry-pi-for-computer-vision) | [TOC](https://www.pyimagesearch.com/2019/04/05/table-of-contents-raspberry-pi-for-computer-vision/)) - 由 PyImageSearch 团队：Adrian Rosebrock ([@PyImageSearch](https://twitter.com/PyImageSearch))、David Hoffman、Asbhishek Thanki、Sayak Paul ([@RisingSayak](https://twitter.com/RisingSayak)) 和 David Mcduffee。
* 2019-12-01 [TinyML](http://shop.oreilly.com/product/0636920254508.do) - 作者：Pete Warden ([@petewarden](https://twitter.com/petewarden)) 和 Daniel Situnayake ([@dansitu](https://twitter.com/dansitu))。
* 2019-10-01 [云、移动和边缘的实用深度学习](https://www.practicaldeeplearning.ai/) - 作者：Anirudh Koul ([@AnirudhKoul](https://twitter.com/AnirudhKoul))、Siddha Ganju ([@SiddhaGanju](https://twitter.com/SiddhaGanju)) 和 Meher Kasam （[@MeherKasam](https://twitter.com/MeherKasam))。

### 视频
* 2021-10-06 [与 Sunit Roy 一起为 TensorFlow Lite 做出贡献](https://youtu.be/sZayUoWW6nE) (Hacktoberfest 2021)
* 2020-07-25 [Android ML by Hoi Lam](https://youtu.be/m_bEh8YifnQ)（GDG 加尔各答聚会）。
* 2020-04-01 [从原型到生产的轻松设备上机器学习](https://youtu.be/ALxWJoh_BHw) (TF 开发峰会 2020)。
* 2020-03-11 [TensorFlow Lite：用于移动和物联网设备的机器学习](https://youtu.be/27Zx-4GOQA8)（TF 开发峰会 2020）。
* 2019-10-31 [主题演讲 - TensorFlow Lite：用于移动和物联网设备的机器学习](https://youtu.be/zjDGAiLqGk8)。
* 2019-10-31 [TensorFlow Lite：在设备上运行 ML 的解决方案](https://youtu.be/0SpZy7iouFU)。
* 2019-10-31 [TensorFlow模型优化：量化和剪枝](https://youtu.be/3JWRVx1OKQQ)。
* 2019-10-29 [TensorFlow 内部：TensorFlow Lite](https://youtu.be/gHN0jDbJz8E)。
* 2018-04-18 [Android 版 TensorFlow Lite（编码 TensorFlow）](https://youtu.be/JnhW5tQ_7Vo)。

### 播客
* 2020-08-08 [与 Hoi Lam 谈论机器学习](https://anchor.fm/talkingwithapples/episodes/Talking-Machine-Learning-with-Hoi-Lam-eiaj7v)。

### 慕课
* [Introduction to TensorFlow Lite](https://www.udacity.com/course/intro-to-tensorflow-lite--ud190) - 由 Daniel Situnayake (@dansitu)、Paige Bailey ([@DynamicWebPaige](https://twitter.com/DynamicWebPaige)) 和 Juan Delgado 开设的 Udacity 课程。
* [Device-based Models with TensorFlow Lite](https://www.coursera.org/learn/device-based-models-tensorflow) - Coursera 课程，作者：Laurence Moroney ([@lmoroney](https://twitter.com/lmoroney))。
* [The Future of ML is Tiny and Bright](https://www.edx.org/professional-certificate/harvardx-tiny-machine-learning) - 哈佛大学与 Google 合作创建的一系列 edX 课程。讲师 - Vijay Janapa Reddi、Laurence Moroney 和 Pete Warden。
