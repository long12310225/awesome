<div align="center">
    <a href="https://krzjoa.github.io/awesome-python-data-science/"><img width="250" height="250" src="img/py-datascience.png" alt="pyds"></a>
    <br>
    <br>
    <br>
</div>

<h1对齐=“中心”>
很棒的 Python 数据科学
</h1>
<div align="center"><a href="https://github.com/sindresorhus/awesome">
<img src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg" alt="Awesome" border="0">
</a>
</div>
</br>

> 可能是 Python 数据科学软件的最佳精选列表

## 内容
- [Contents](#contents)
- [机器学习](#machine-learning)
	- [通用机器学习](#general-purpose-machine-learning)
  	- [梯度提升](#gradient-boosting)
	- [集成方法](#ensemble-methods)
	- [不平衡的数据集](#imbalanced-datasets)
	- [内核方法](#kernel-methods)
- [深度学习](#deep-learning)
	- [PyTorch](#pytorch)
	- [TensorFlow](#tensorflow)
    - [Keras](#keras)
 	- [JAX](#jax)
	- [Others](#others)
- [自动化机器学习](#automated-machine-learning)
- [自然语言处理](#natural-language-processing)
- [电脑试镜](#computer-audition)
- [计算机视觉](#computer-vision)
- [时间序列](#time-series)
- [强化学习](#reinforcement-learning)
- [图机器学习](#graph-machine-learning)
- [图操作](#graph-manipulation)
- [学习排名和推荐系统](#learning-to-rank-&-recommender-systems)
- [概率图形模型](#probabilistic-graphical-models)
- [概率方法](#probabilistic-methods)
- [型号说明](#model-explanation)
- [Optimization](#optimization)
- [基因编程](#genetic-programming)
- [特征工程](#feature-engineering)
	- [General](#general)
	- [特征选择](#feature-selection)
- [Visualization](#visualization)
	- [通用型](#general-purposes)
	- [互动情节](#interactive-plots)
	- [Map](#map)
	- [自动绘图](#automatic-plotting)
	- [NLP](#nlp)
- [数据处理](#data-manipulation)
	- [数据框](#data-frames)
	- [Pipelines](#pipelines)
	- [以数据为中心的人工智能](#data-centric-ai)
	- [综合数据](#synthetic-data)

- [TabGAN](https://github.com/Diyago/Tabular-data-generation) - 使用 GAN、扩散模型和 LLM 生成合成表格数据。 <img height="16" width="16" src="https://github.com/krzjoa/awesome-python-data-science/raw/master/img/sklearn_big.png" alt="sklearn">
- [Deployment](#deployment)
- [Statistics](#statistics)
- [分布式计算](#distributed-computing)
- [Experimentation](#experimentation)
- [数据验证](#data-validation)
- [Evaluation](#evaluation)
- [Computations](#computations)
- [网页抓取](#web-scraping)
- [空间分析](#spatial-analysis)
- [量子计算](#quantum-computing)
- [Conversion](#conversion)
- [Contributing](#contributing)
- [License](#license)

## 机器学习

### 通用机器学习
* [SciPy](https://scipy.org/) - Python 科学计算的基本算法
* [scikit-learn](https://scikit-learn.org/stable/) - Python 中的机器学习。 <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [PyCaret](https://github.com/pycaret/pycaret) - Python 中的开源、低代码机器学习库。  <img height="20" src="img/R_big.png" alt="R 灵感库">
* [Shogun](https://github.com/shogun-toolbox/shogun) - 机器学习工具箱。
* [xLearn](https://github.com/aksnzhy/xlearn) - 高性能、易于使用且可扩展的机器学习包。
* [cuML](https://github.com/rapidsai/cuml) - RAPIDS 机器学习库。 <img height="20" src="img/sklearn_big.png" alt="sklearn"> <img height="20" src="img/gpu_big.png" alt="GPU 加速">
* [modAL](https://github.com/cosmic-cortex/modAL) - Python3 的模块化主动学习框架。 <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [Sparkit-learn](https://github.com/lensacom/sparkit-learn) - PySpark + scikit-learn = Sparkit-learn。 <img height="20" src="img/sklearn_big.png" alt="sklearn"> <img height="20" src="img/spark_big.png" alt="基于 Apache Spark">
* [mlpack](https://github.com/mlpack/mlpack) - 可扩展的 C++ 机器学习库（Python 绑定）。
* [dlib](https://github.com/davisking/dlib) - 用于使用 C++（Python 绑定）制作现实世界机器学习和数据分析应用程序的工具包。
* [MLxtend](https://github.com/rasbt/mlxtend) - Python 数据分析和机器学习库的扩展和帮助模块。 <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [hyperlearn](https://github.com/danielhanchen/hyperlearn) - 速度提高 50% 以上，RAM 使用量减少 50% 以上，GPU 支持重写 Sklearn、Statsmodels。 <img height="20" src="img/sklearn_big.png" alt="sklearn"> <img height="20" src="img/pytorch_big2.png" alt="基于 PyTorch/兼容">
* [Reproducible Experiment Platform (REP)](https://github.com/yandex/rep) - 人类机器学习工具箱。 <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [scikit-multilearn](https://github.com/scikit-multilearn/scikit-multilearn) - python 的多标签分类。 <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [seqlearn](https://github.com/larsmans/seqlearn) - Python 的序列分类工具包。 <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [pystruct](https://github.com/pystruct/pystruct) - Python 的简单结构化学习框架。 <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [sklearn-expertsys](https://github.com/tmadl/sklearn-expertsys) - scikit learn 的高度可解释的分类器。 <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [RuleFit](https://github.com/christophM/rulefit) - 规则的实施。 <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [metric-learn](https://github.com/all-umass/metric-learn) - Python 中的度量学习算法。 <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [pyGAM](https://github.com/dswah/pyGAM) - Python 中的广义加性模型。
* [causalml](https://github.com/uber/causalml) - 使用机器学习算法提升建模和因果推理。 <img height="20" src="img/sklearn_big.png" alt="sklearn">

### 梯度提升
* [XGBoost](https://github.com/dmlc/xgboost) - 可扩展、可移植、分布式梯度提升。 <img height="20" src="img/sklearn_big.png" alt="sklearn"> <img height="20" src="img/gpu_big.png" alt="GPU 加速">
* [LightGBM](https://github.com/Microsoft/LightGBM) - 快速、分布式、高性能的梯度提升。 <img height="20" src="img/sklearn_big.png" alt="sklearn"> <img height="20" src="img/gpu_big.png" alt="GPU 加速">
* [CatBoost](https://github.com/catboost/catboost) - 决策树库的开源梯度提升。 <img height="20" src="img/sklearn_big.png" alt="sklearn"> <img height="20" src="img/gpu_big.png" alt="GPU 加速">
* [ThunderGBM](https://github.com/Xtra-Computing/thundergbm) - GPU 上的快速 GBDT 和随机森林。 <img height="20" src="img/sklearn_big.png" alt="sklearn"> <img height="20" src="img/gpu_big.png" alt="GPU 加速">
* [NGBoost](https://github.com/stanfordmlgroup/ngboost) - 用于概率预测的自然梯度提升。
* [TensorFlow Decision Forests](https://github.com/tensorflow/decision-forests) - 用于训练、服务和解释 Keras 决策森林模型的最先进算法的集合。 <img height="20" src="img/keras_big.png" alt="keras"> <img height="20" src="img/tf_big2.png" alt="TensorFlow">

### 集成方法
* [ML-Ensemble](http://ml-ensemble.com/) - 高性能集成学习。 <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [Stacking](https://github.com/ikki407/stacking) - 用 Python 编写的简单且有用的堆栈库。 <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [stacked_generalization](https://github.com/fukatani/stacked_generalization) - 用于机器学习堆叠泛化的库。 <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [vecstack](https://github.com/vecxoz/vecstack) - 用于堆叠的 Python 包（机器学习技术）。 <img height="20" src="img/sklearn_big.png" alt="sklearn">

### 不平衡的数据集
* [imbalanced-learn](https://github.com/scikit-learn-contrib/imbalanced-learn) - 使用各种技术执行欠采样和过采样的模块。 <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [imbalanced-algorithms](https://github.com/dialnd/imbalanced-algorithms) - 基于 Python 的不平衡数据学习算法实现。 <img height="20" src="img/sklearn_big.png" alt="sklearn"> <img height="20" src="img/tf_big2.png" alt="sklearn">

### 内核方法
* [pyFM](https://github.com/coreylynch/pyFM) - python 中的因式分解机。 <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [fastFM](https://github.com/ibayer/fastFM) - 因式分解机的库。 <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [tffm](https://github.com/geffy/tffm) - 任意阶因式分解机的 TensorFlow 实现。 <img height="20" src="img/sklearn_big.png" alt="sklearn"> <img height="20" src="img/tf_big2.png" alt="sklearn">
* [liquidSVM](https://github.com/liquidSVM/liquidSVM) - SVM 的实现。
* [scikit-rvm](https://github.com/JamesRitchie/scikit-rvm) - 使用 scikit-learn API 实现相关向量机。 <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [ThunderSVM](https://github.com/Xtra-Computing/thundersvm) - GPU 和 CPU 上的快速 SVM 库。 <img height="20" src="img/sklearn_big.png" alt="sklearn"> <img height="20" src="img/gpu_big.png" alt="GPU 加速">

## 深度学习

### 火炬
* [PyTorch](https://github.com/pytorch/pytorch) - Python 中的张量和动态神经网络具有强大的 GPU 加速功能。 <img height="20" src="img/pytorch_big2.png" alt="基于 PyTorch/兼容">
* [pytorch-lightning](https://github.com/Lightning-AI/lightning) - PyTorch Lightning 只是组织起来的 PyTorch。 <img height="20" src="img/pytorch_big2.png" alt="基于 PyTorch/兼容">
* [ignite](https://github.com/pytorch/ignite) - 帮助在 PyTorch 中训练神经网络的高级库。 <img height="20" src="img/pytorch_big2.png" alt="基于 PyTorch/兼容">
* [skorch](https://github.com/dnouri/skorch) - 一个封装 PyTorch 的 scikit-learn 兼容神经网络库。 <img height="20" src="img/sklearn_big.png" alt="sklearn"> <img height="20" src="img/pytorch_big2.png" alt="基于 PyTorch/兼容">
* [Catalyst](https://github.com/catalyst-team/catalyst) - 用于 PyTorch DL 和 RL 研究的高级实用程序。 <img height="20" src="img/pytorch_big2.png" alt="基于 PyTorch/兼容">
* [ChemicalX](https://github.com/AstraZeneca/chemicalx) - 基于 PyTorch 的深度学习库，用于药物对评分。 <img height="20" src="img/pytorch_big2.png" alt="基于 PyTorch/兼容">

### TensorFlow
* [TensorFlow](https://github.com/tensorflow/tensorflow) - Google 使用数据流图进行可扩展机器学习的计算。 <img height="20" src="img/tf_big2.png" alt="sklearn">
* [TensorLayer](https://github.com/zsdonghao/tensorlayer) - 面向研究人员和工程师的深度学习和强化学习库。 <img height="20" src="img/tf_big2.png" alt="sklearn">
* [TFLearn](https://github.com/tflearn/tflearn) - 深度学习库，具有适用于 TensorFlow 的更高级别 API。 <img height="20" src="img/tf_big2.png" alt="sklearn">
* [Sonnet](https://github.com/deepmind/sonnet) - 基于 TensorFlow 的神经网络库。 <img height="20" src="img/tf_big2.png" alt="sklearn">
* [tensorpack](https://github.com/ppwwyyxx/tensorpack) - TensorFlow 上的神经网络训练接口。 <img height="20" src="img/tf_big2.png" alt="sklearn">
* [tfdeploy](https://github.com/riga/tfdeploy) - 部署 TensorFlow 图以进行快速评估并导出到运行 numpy 的无 TensorFlow 环境。 <img height="20" src="img/tf_big2.png" alt="sklearn">
* [tensorflow-upstream](https://github.com/ROCmSoftwarePlatform/tensorflow-upstream) - TensorFlow ROCm 端口。 <img height="20" src="img/tf_big2.png" alt="sklearn"> <img height="20" src="img/amd_big.png" alt="可以在 AMD GPU 上运行">
* [TensorFlow Fold](https://github.com/tensorflow/fold) - 在 TensorFlow 中使用动态计算图进行深度学习。 <img height="20" src="img/tf_big2.png" alt="sklearn">
* [TensorLight](https://github.com/bsautermeister/tensorlight) - TensorFlow 的高级框架。 <img height="20" src="img/tf_big2.png" alt="sklearn">
* [Mesh TensorFlow](https://github.com/tensorflow/mesh) - 模型并行性变得更容易。 <img height="20" src="img/tf_big2.png" alt="sklearn">
* [Ludwig](https://github.com/uber/ludwig) - 一种工具箱，允许人们无需编写代码即可训练和测试深度学习模型。 <img height="20" src="img/tf_big2.png" alt="sklearn">

### 贾克斯
* [JAX](https://github.com/google/jax) - Python+NumPy 程序的可组合转换：微分、矢量化、JIT 到 GPU/TPU 等。
* [FLAX](https://github.com/google/flax) - 用于 JAX 的神经网络库，专为灵活性而设计。
* [Optax](https://github.com/google-deepmind/optax) - JAX 的梯度处理和优化库。

### 喀拉斯
* [Keras](https://keras.io) - 在 TensorFlow 之上运行的高级神经网络 API。  <img height="20" src="img/keras_big.png" alt="Keras 兼容">
* [keras-contrib](https://github.com/keras-team/keras-contrib) - Keras 社区贡献。 <img height="20" src="img/keras_big.png" alt="Keras 兼容">
* [Hyperas](https://github.com/maxpumperla/hyperas) - Keras + Hyperopt：一个方便的超参数的简单包装器。 <img height="20" src="img/keras_big.png" alt="Keras 兼容">
* [Elephas](https://github.com/maxpumperla/elephas) - 使用 Keras 和 Spark 进行分布式深度学习。 <img height="20" src="img/keras_big.png" alt="Keras 兼容">
* [qkeras](https://github.com/google/qkeras) - 量化深度学习库。 <img height="20" src="img/keras_big.png" alt="Keras 兼容">

### 其他
* [transformers](https://github.com/huggingface/transformers) - 适用于 Pytorch、TensorFlow 和 JAX 的最先进的机器学习。 <img height="20" src="img/pytorch_big2.png" alt="PyTorch 基于/兼容"> <img height="20" src="img/tf_big2.png" alt="sklearn">
* [Tangent](https://github.com/google/tangent) - 纯 Python 中的源到源可调试衍生物。
* [autograd](https://github.com/HIPS/autograd) - 高效计算 numpy 代码的导数。
* [Caffe](https://github.com/BVLC/caffe) - 一个快速开放的深度学习框架。
* [nnabla](https://github.com/sony/nnabla) - 索尼的神经网络库。

## 自动化机器学习
* [auto-sklearn](https://github.com/automl/auto-sklearn) - AutoML 工具包和 scikit-learn 估计器的直接替代品。 <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [Auto-PyTorch](https://github.com/automl/Auto-PyTorch) - PyTorch 的自动架构搜索和超参数优化。 <img height="20" src="img/pytorch_big2.png" alt="基于 PyTorch/兼容">
* [AutoKeras](https://github.com/keras-team/autokeras) - 用于深度学习的 AutoML 库。 <img height="20" src="img/keras_big.png" alt="Keras 兼容">
* [AutoGluon](https://github.com/awslabs/autogluon) - 适用于图像、文本、表格、时间序列和多模态数据的 AutoML。
* [TPOT](https://github.com/rhiever/tpot) - AutoML 工具，使用遗传编程优化机器学习管道。 <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [MLBox](https://github.com/AxeldeRomblay/MLBox) - 一个强大的自动化机器学习Python库。

## 自然语言处理
* [torchtext](https://github.com/pytorch/text) - 文本和 NLP 的数据加载器和抽象。 <img height="20" src="img/pytorch_big2.png" alt="基于 PyTorch/兼容">
* [KerasNLP](https://github.com/keras-team/keras-nlp) - 使用 Keras 的模块化自然语言处理工作流程。 <img height="20" src="img/keras_big.png" alt="基于 Keras/兼容">
* [spaCy](https://spacy.io/) - 工业级自然语言处理。
* [NLTK](https://github.com/nltk/nltk) - 支持自然语言处理研究和开发的模块、数据集和教程。
* [CLTK](https://github.com/cltk/cltk) - 古典语言工具包。
* [gensim](https://radimrehurek.com/gensim/) - 人类主题建模。
* [pyMorfologik](https://github.com/dmirecki/pyMorfologik) - <a href="https://github.com/morfologik/morfologik-stemming">Morfologik</a> 的 Python 绑定。
* [skift](https://github.com/shaypal5/skift) - Python fastText 的 Scikit-learn 包装器。 <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [Phonemizer](https://github.com/bootphon/phonemizer) - 适用于多种语言的简单文本到音素转换器。
* [flair](https://github.com/zalandoresearch/flair) - 最先进的 NLP 的非常简单的框架。

## 电脑试镜
* [torchaudio](https://github.com/pytorch/audio) - PyTorch 的音频库。 <img height="20" src="img/pytorch_big2.png" alt="基于 PyTorch/兼容">
* [librosa](https://github.com/librosa/librosa) - 用于音频和音乐分析的 Python 库。
* [Yaafe](https://github.com/Yaafe/Yaafe) - 音频特征提取。
* [aubio](https://github.com/aubio/aubio) - 用于音频和音乐分析的库。
* [Essentia](https://github.com/MTG/essentia) - 用于音频和音乐分析、描述和合成的库。
* [LibXtract](https://github.com/jamiebullock/LibXtract) - 一个简单、便携、轻量级的音频特征提取函数库。
* [Marsyas](https://github.com/marsyas/marsyas) - 音频信号的音乐分析、检索和合成。
* [muda](https://github.com/bmcfee/muda) - 用于增强带注释的音频数据的库。
* [madmom](https://github.com/CPJKU/madmom) - Python 音频和音乐信号处理库。

## 计算机视觉
* [torchvision](https://github.com/pytorch/vision) - 特定于计算机视觉的数据集、转换和模型。 <img height="20" src="img/pytorch_big2.png" alt="基于 PyTorch/兼容">
* [PyTorch3D](https://github.com/facebookresearch/pytorch3d) - PyTorch3D 是 FAIR 的可重用组件库，用于使用 3D 数据进行深度学习。 <img height="20" src="img/pytorch_big2.png" alt="基于 PyTorch/兼容">
* [KerasCV](https://github.com/keras-team/keras-cv) - Keras 的行业实力计算机视觉工作流程。 <img height="20" src="img/keras_big.png" alt="基于 MXNet">
* [OpenCV](https://github.com/opencv/opencv) - 开源计算机视觉库。
* [Decord](https://github.com/dmlc/decord) - 一个高效的视频加载器，用于深度学习，具有智能洗牌功能，非常容易理解。
* [MMEngine](https://github.com/open-mmlab/mmengine) - 用于训练深度学习模型的 OpenMMLab 基础库。 <img height="20" src="img/pytorch_big2.png" alt="基于 PyTorch/兼容">
* [scikit-image](https://github.com/scikit-image/scikit-image) - 图像处理 SciKit（SciPy 工具箱）。
* [imgaug](https://github.com/aleju/imgaug) - 用于机器学习实验的图像增强。
* [imgaug_extension](https://github.com/cadenai/imgaug_extension) - imgaug 的额外增强。
* [Augmentor](https://github.com/mdbloice/Augmentor) - 用于机器学习的 Python 图像增强库。
* [albumentations](https://github.com/albu/albumentations) - 快速图像增强库和其他库的易于使用的包装器。
* [LAVIS](https://github.com/salesforce/LAVIS) - 语言视觉智能的一站式图书馆。

## 时间序列
* [sktime](https://github.com/alan-turing-institute/sktime) - 具有时间序列的机器学习的统一框架。 <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [skforecast](https://github.com/JoaquinAmatRodrigo/skforecast) - 使用机器学习模型进行时间序列预测
* [darts](https://github.com/unit8co/darts) - 一个用于轻松操作和预测时间序列的 Python 库。
* [statsforecast](https://github.com/Nixtla/statsforecast) - 利用统计和计量经济模型进行快速预测。
* [mlforecast](https://github.com/Nixtla/mlforecast) - 基于机器学习的可扩展时间序列预测。
* [neuralforecast](https://github.com/Nixtla/neuralforecast) - 基于机器学习的可扩展时间序列预测。
* [tslearn](https://github.com/rtavenar/tslearn) - 专用于时间序列数据的机器学习工具包。 <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [tick](https://github.com/X-DataInitiative/tick) - 统计学习模块，特别强调时间相关建模。  <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [greykite](https://github.com/linkedin/greykite) - 接下来是一个灵活、直观、快速的预测库。
* [Prophet](https://github.com/facebook/prophet) - 自动预测程序。
* [PyFlux](https://github.com/RJT1990/pyflux) - Python 的开源时间序列库。
* [bayesloop](https://github.com/christophmark/bayesloop) - 概率编程框架，有助于时变参数模型的客观模型选择。
* [luminol](https://github.com/linkedin/luminol) - 异常检测和关联库。
* [dateutil](https://dateutil.readthedocs.io/en/stable/) - 标准日期时间模块的强大扩展
* [maya](https://github.com/timofurrer/maya) - 使得解析字符串和更改时区变得非常容易
* [Chaos Genius](https://github.com/chaos-genius/chaos_genius) - 机器学习驱动的分析引擎，用于异常值/异常检测和根本原因分析

## 强化学习
* [Gymnasium](https://github.com/Farama-Foundation/Gymnasium) - 单代理强化学习环境的 API 标准，具有流行的参考环境和相关实用程序（以前称为 [Gym](https://github.com/openai/gym)）。
* [PettingZoo](https://github.com/Farama-Foundation/PettingZoo) - 多代理强化学习环境的 API 标准，具有流行的参考环境和相关实用程序。
* [MAgent2](https://github.com/Farama-Foundation/MAgent2) - 用于具有大量代理的高性能多代理环境的引擎，以及一组参考环境。
* [Stable Baselines3](https://github.com/DLR-RM/stable-baselines3) - 一组基于 OpenAI Baselines 的强化学习算法的改进实现。
* [Shimmy](https://github.com/Farama-Foundation/Shimmy) - 适用于流行的外部强化学习环境的 API 转换工具。
* [EnvPool](https://github.com/sail-sg/envpool) - 适用于一般 RL 环境的基于 C++ 的高性能并行环境执行引擎（向量化 env）。
* [RLlib](https://ray.readthedocs.io/en/latest/rllib.html) - 可扩展的强化学习。
* [Tianshou](https://github.com/thu-ml/tianshou/#comprehensive-functionality) - 一个优雅的 PyTorch 深度强化学习库。 <img height="20" src="img/pytorch_big2.png" alt="基于 PyTorch/兼容">
* [Acme](https://github.com/google-deepmind/acme) - 强化学习组件和代理的库。
* [Catalyst-RL](https://github.com/catalyst-team/catalyst-rl) - 用于强化学习研究的 PyTorch 框架。 <img height="20" src="img/pytorch_big2.png" alt="基于 PyTorch/兼容">
* [d3rlpy](https://github.com/takuseno/d3rlpy) - 离线深度强化学习库。
* [DI-engine](https://github.com/opendilab/DI-engine) - OpenDILab 决策人工智能引擎。 <img height="20" src="img/pytorch_big2.png" alt="基于 PyTorch/兼容">
* [TF-Agents](https://github.com/tensorflow/agents) - TensorFlow 中的强化学习库。 <img height="20" src="img/tf_big2.png" alt="TensorFlow">
* [TensorForce](https://github.com/reinforceio/tensorforce) - 用于应用强化学习的 TensorFlow 库。 <img height="20" src="img/tf_big2.png" alt="TensorFlow">
* [TRFL](https://github.com/deepmind/trfl) - TensorFlow 强化学习。 <img height="20" src="img/tf_big2.png" alt="sklearn">
* [Dopamine](https://github.com/google/dopamine) - 强化学习算法快速原型设计的研究框架。
* [keras-rl](https://github.com/keras-rl/keras-rl) - Keras 的深度强化学习。 <img height="20" src="img/keras_big.png" alt="Keras 兼容">
* [garage](https://github.com/rlworkgroup/garage) - 用于可重复强化学习研究的工具包。
* [Horizon](https://github.com/facebookresearch/Horizon) - 应用强化学习的平台。
* [rlpyt](https://github.com/astooke/rlpyt) - PyTorch 中的强化学习。 <img height="20" src="img/pytorch_big2.png" alt="基于 PyTorch/兼容">
* [cleanrl](https://github.com/vwxyzjn/cleanrl) - 深度强化学习算法的高质量单文件实现，具有研究友好的功能（PPO、DQN、C51、DDPG、TD3、SAC、PPG）。
* [Machin](https://github.com/iffiX/machin) - 为pytorch设计的强化库。 <img height="20" src="img/pytorch_big2.png" alt="基于 PyTorch/兼容">
* [SKRL](https://github.com/Toni-SM/skrl) - 模块化强化学习库（在 PyTorch 和 JAX 上），支持 NVIDIA Isaac Gym、Isaac Orbit 和 Omniverse Isaac Gym。 <img height="20" src="img/pytorch_big2.png" alt="基于 PyTorch/兼容">
* [Imitation](https://github.com/HumanCompatibleAI/imitation) - 模仿和奖励学习算法的干净 PyTorch 实现。 <img height="20" src="img/pytorch_big2.png" alt="基于 PyTorch/兼容">

## 图机器学习
* [pytorch_geometric](https://github.com/rusty1s/pytorch_geometric) - PyTorch 的几何深度学习扩展库。 <img height="20" src="img/pytorch_big2.png" alt="基于 PyTorch/兼容">
* [pytorch_geometric_temporal](https://github.com/benedekrozemberczki/pytorch_geometric_temporal) - PyTorch 几何的时间扩展库。 <img height="20" src="img/pytorch_big2.png" alt="基于 PyTorch/兼容">
* [PyTorch Geometric Signed Directed](https://github.com/SherylHYX/pytorch_geometric_signed_directed) - PyTorch Geometric 的有符号/有向图神经网络扩展库。 <img height="20" src="img/pytorch_big2.png" alt="基于 PyTorch/兼容">
* [dgl](https://github.com/dmlc/dgl) - Python 包旨在在现有 DL 框架之上简化图形深度学习。 <img height="20" src="img/pytorch_big2.png" alt="基于PyTorch/兼容"> <img height="20" src="img/tf_big2.png" alt="TensorFlow"> <img height="20" src="img/mxnet_big.png" alt="基于MXNet">
* [GRAPE](https://github.com/AnacletoLAB/grape/tree/main) - GRAPE 是一个用于预测和评估的 Rust/Python 图表示学习库
* [Spektral](https://github.com/danielegrattarola/spektral) - 图的深度学习。 <img height="20" src="img/keras_big.png" alt="Keras 兼容">
* [StellarGraph](https://github.com/stellargraph/stellargraph) - 图上的机器学习。 <img height="20" src="img/tf_big2.png" alt="TensorFlow"> <img height="20" src="img/keras_big.png" alt="Keras 兼容">
* [Graph Nets](https://github.com/google-deepmind/graph_nets) - 在 Tensorflow 中构建图网络。 <img height="20" src="img/tf_big2.png" alt="TensorFlow">
* [TensorFlow GNN](https://github.com/tensorflow/gnn) - 用于在 TensorFlow 平台上构建图神经网络的库。 <img height="20" src="img/tf_big2.png" alt="TensorFlow">
* [Auto Graph Learning](https://github.com/THUMNLab/AutoGL) - 用于图机器学习的 autoML 框架和工具包。
* [PyTorch-BigGraph](https://github.com/facebookresearch/PyTorch-BigGraph) - 从大规模图结构数据生成嵌入。 <img height="20" src="img/pytorch_big2.png" alt="基于 PyTorch/兼容">
* [Auto Graph Learning](https://github.com/THUMNLab/AutoGL) - 用于图机器学习的 autoML 框架和工具包。
* [Karate Club](https://github.com/benedekrozemberczki/karateclub) - 用于图结构数据的无监督机器学习库。
* [Little Ball of Fur](https://github.com/benedekrozemberczki/littleballoffur) - 用于对图结构化数据进行采样的库。
* [GreatX](https://github.com/EdisonLeeeee/GreatX) - 基于 PyTorch 和 PyTorch Geometric (PyG) 的图形可靠性工具箱。 <img height="20" src="img/pytorch_big2.png" alt="基于 PyTorch/兼容">
* [Jraph](https://github.com/google-deepmind/jraph) - Jax 中的图神经网络库。
* [TRL](https://github.com/huggingface/trl) - 通过强化学习训练 Transformer 语言模型。
* [Cleora](https://github.com/BaseModelAI/cleora) - 图嵌入引擎。

## 图操作
* [Networkx](https://github.com/networkx/networkx) - Python 中的网络分析。
* [Rustworkx](https://github.com/Qiskit/rustworkx) - 用 Rust 实现的高性能 Python 图形库。
* [graph-tool](https://graph-tool.skewed.de/) - 一个高效的 Python 模块，用于图形（又称网络）的操作和统计分析。
* [igraph](https://github.com/igraph/python-igraph) - igraph 的 Python 接口。

## 学习排名和推荐系统
* [LightFM](https://github.com/lyst/lightfm) - LightFM（一种混合推荐算法）的 Python 实现。
* [Spotlight](https://maciejkula.github.io/spotlight/) - 使用 PyTorch 的深度推荐模型。
* [Surprise](https://github.com/NicolasHug/Surprise) - 用于构建和分析推荐系统的 Python scikit。
* [RecBole](https://github.com/RUCAIBox/RecBole) - 统一、全面、高效的推荐库。 <img height="20" src="img/pytorch_big2.png" alt="基于 PyTorch/兼容">
* [allRank](https://github.com/allegro/allRank) - allRank 是一个基于 PyTorch 的训练学习排序神经模型的框架。 <img height="20" src="img/pytorch_big2.png" alt="基于 PyTorch/兼容">
* [TensorFlow Recommenders](https://github.com/tensorflow/recommenders) - 用于使用 TensorFlow 构建推荐系统模型的库。 <img height="20" src="img/tf_big2.png" alt="TensorFlow"> <img height="20" src="img/keras_big.png" alt="Keras 兼容">
* [TensorFlow Ranking](https://github.com/tensorflow/ranking) - 学习 TensorFlow 排名。 <img height="20" src="img/tf_big2.png" alt="TensorFlow">

## 概率图形模型
* [pomegranate](https://github.com/jmschrei/pomegranate) - Python 的概率和图形模型。 <img height="20" src="img/pytorch_big2.png" alt="基于 PyTorch/兼容">
* [pgmpy](https://github.com/pgmpy/pgmpy) - 用于处理概率图形模型的 python 库。
* [pyAgrum](https://agrum.gitlab.io/) - 图形通用建模器。

## 概率方法
* [pyro](https://github.com/uber/pyro) - 一个基于 PyTorch 构建的灵活、可扩展的深度概率编程库。 <img height="20" src="img/pytorch_big2.png" alt="基于 PyTorch/兼容">
* [PyMC](https://github.com/pymc-devs/pymc) - Python 中的贝叶斯随机建模。
* [ZhuSuan](https://zhusuan.readthedocs.io/en/latest/) - 贝叶斯深度学习。 <img height="20" src="img/tf_big2.png" alt="sklearn">
* [GPflow](https://gpflow.readthedocs.io/en/latest/?badge=latest) - TensorFlow 中的高斯过程。 <img height="20" src="img/tf_big2.png" alt="sklearn">
* [InferPy](https://github.com/PGM-Lab/InferPy) - 深度概率建模变得简单。  <img height="20" src="img/tf_big2.png" alt="sklearn">
* [PyStan](https://github.com/stan-dev/pystan) - 使用 No-U-Turn 采样器（Python 接口）进行贝叶斯推理。
* [sklearn-bayes](https://github.com/AmazaspShumik/sklearn-bayes) - 使用 scikit-learn API 进行贝叶斯机器学习的 Python 包。 <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [skpro](https://github.com/alan-turing-institute/skpro) - [艾伦图灵研究所](https://www.turing.ac.uk/) 监督的与领域无关的概率建模预测框架。 <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [PyVarInf](https://github.com/ctallec/pyvarinf) - PyTorch 的贝叶斯深度学习方法和变分推理。 <img height="20" src="img/pytorch_big2.png" alt="基于 PyTorch/兼容">
* [emcee](https://github.com/dfm/emcee) - 用于仿射不变 MCMC 的 Python 集成采样工具包。
* [hsmmlearn](https://github.com/jvkersch/hsmmlearn) - 具有显式持续时间的隐藏半马尔可夫模型的库。
* [pyhsmm](https://github.com/mattjj/pyhsmm) - HSMM 和 HMM 中的贝叶斯推理。
* [GPyTorch](https://github.com/cornellius-gp/gpytorch) - PyTorch 中高斯过程的高效模块化实现。 <img height="20" src="img/pytorch_big2.png" alt="基于 PyTorch/兼容">
* [sklearn-crfsuite](https://github.com/TeamHG-Memex/sklearn-crfsuite) - 受 scikit-learn 启发的 CRFsuite API。 <img height="20" src="img/sklearn_big.png" alt="sklearn">

## 型号说明
* [dalex](https://github.com/ModelOriented/DALEX) - 用于探索和解释的模型不可知语言。 <img height="20" src="img/sklearn_big.png" alt="sklearn"><img height="20" src="img/R_big.png" alt="R 启发/移植的 lib">
* [Shapley](https://github.com/benedekrozemberczki/shapley) - 一个数据驱动的框架，用于量化机器学习集成中分类器的价值。
* [Alibi](https://github.com/SeldonIO/alibi) - 用于监控和解释机器学习模型的算法。
* [anchor](https://github.com/marcotcr/anchor) - “高精度模型无关解释”论文的代码。
* [aequitas](https://github.com/dssg/aequitas) - 偏见和公平审计工具包。
* [Contrastive Explanation](https://github.com/MarcelRobeer/ContrastiveExplanation) - 对比解释（箔树）。 <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [yellowbrick](https://github.com/DistrictDataLabs/yellowbrick) - 可视化分析和诊断工具有助于机器学习模型的选择。 <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [scikit-plot](https://github.com/reiinakano/scikit-plot) - 一个直观的库，用于向 scikit-learn 对象添加绘图功能。 <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [shap](https://github.com/slundberg/shap) - 解释任何机器学习模型的输出的统一方法。 <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [InterpretML](https://github.com/interpretml/interpret) - InterpretML 实现了可解释提升机 (EBM)，这是一种基于广义加性模型 (GAM) 的现代、完全可解释的机器学习模型。这个开源包还提供了 EBM、其他玻璃盒模型和黑盒解释的可视化工具。 <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [ELI5](https://github.com/TeamHG-Memex/eli5) - 用于调试/检查机器学习分类器并解释其预测的库。
* [Lime](https://github.com/marcotcr/lime) - 解释任何机器学习分类器的预测。 <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [FairML](https://github.com/adebayoj/fairml) - FairML 是一个Python 工具箱，用于审核机器学习模型的偏差。 <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [L2X](https://github.com/Jianbo-Lab/L2X) - 用于复制论文*学习解释：模型解释的信息理论视角*中的实验的代码。
* [PDPbox](https://github.com/SauceCat/PDPbox) - 部分依赖图工具箱。
* [PyCEbox](https://github.com/AustinRochford/PyCEbox) - Python 个体条件期望图工具箱。
* [Skater](https://github.com/datascienceinc/Skater) - 用于模型解释的 Python 库。
* [model-analysis](https://github.com/tensorflow/model-analysis) - TensorFlow 的模型分析工具。 <img height="20" src="img/tf_big2.png" alt="sklearn">
* [themis-ml](https://github.com/cosmicBboy/themis-ml) - 实现公平感知机器学习算法的库。 <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [treeinterpreter](https://github.com/andosa/treeinterpreter) - 解释 scikit-learn 的决策树和随机森林预测。 <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [AI Explainability 360](https://github.com/IBM/AIX360) - 数据和机器学习模型的可解释性和可解释性。
* [Auralisation](https://github.com/keunwoochoi/Auralisation) - CNN 中学习到的特征的可听化（针对音频）。
* [CapsNet-Visualization](https://github.com/bourdakos1/CapsNet-Visualization) - CapsNet 层的可视化，以更好地了解其工作原理。
* [lucid](https://github.com/tensorflow/lucid) - 用于研究神经网络可解释性的基础设施和工具的集合。
* [Netron](https://github.com/lutzroeder/Netron) - 用于深度学习和机器学习模型的可视化工具（没有 Python 代码，但可视化来自大多数 Python 深度学习框架的模型）。
* [FlashLight](https://github.com/dlguys/flashlight) - 神经网络的可视化工具。
* [tensorboard-pytorch](https://github.com/lanpa/tensorboard-pytorch) - PyTorch 的 Tensorboard（以及 chainer、mxnet、numpy...）。

## 基因编程
* [gplearn](https://github.com/trevorstephens/gplearn) - Python 中的遗传编程。 <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [PyGAD](https://github.com/ahmedfgad/GeneticAlgorithmPython) - Python 中的遗传算法。 <img height="20" src="img/pytorch_big2.png" alt="基于 PyTorch/兼容"> <img height="20" src="img/keras_big.png" alt="keras">
* [DEAP](https://github.com/DEAP/deap) - Python 中的分布式进化算法。
* [karoo_gp](https://github.com/kstaats/karoo_gp) - 具有 GPU 支持的 Python 遗传编程平台。 <img height="20" src="img/tf_big2.png" alt="sklearn">
* [monkeys](https://github.com/hchasestevens/monkeys) - Python 的强类型遗传编程框架。
* [sklearn-genetic](https://github.com/manuel-calzolari/sklearn-genetic) - scikit-learn 的遗传特征选择模块。 <img height="20" src="img/sklearn_big.png" alt="sklearn">

<a name="opt"></a>
## 优化
* [Optuna](https://github.com/optuna/optuna) - 超参数优化框架。
* [pymoo](https://github.com/anyoptimization/pymoo) - Python 中的多目标优化。
* [pycma](https://github.com/CMA-ES/pycma?tab=readme-ov-file) - CMA-ES 的 Python 实现。
* [Spearmint](https://github.com/HIPS/Spearmint) - 贝叶斯优化。
* [BoTorch](https://github.com/pytorch/botorch) - PyTorch 中的贝叶斯优化。 <img height="20" src="img/pytorch_big2.png" alt="基于 PyTorch/兼容">
* [scikit-opt](https://github.com/guofei9987/scikit-opt) - 用于优化的启发式算法。
* [sklearn-genetic-opt](https://github.com/rodrigo-arenas/Sklearn-genetic-opt) - 使用进化算法进行超参数调整和特征选择。 <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [SMAC3](https://github.com/automl/SMAC3) - 基于序列模型的算法配置。
* [Optunity](https://github.com/claesenm/optunity) - 是一个包含用于超参数调整的各种优化器的库。
* [hyperopt](https://github.com/hyperopt/hyperopt) - Python 中的分布式异步超参数优化。
* [hyperopt-sklearn](https://github.com/hyperopt/hyperopt-sklearn) - sklearn 的超参数优化。 <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [sklearn-deap](https://github.com/rsteca/sklearn-deap) - 在 scikit-learn 中使用进化算法代替网格搜索。 <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [sigopt_sklearn](https://github.com/sigopt/sigopt_sklearn) - scikit-learn 方法的 SigOpt 包装器。 <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [Bayesian Optimization](https://github.com/fmfn/BayesianOptimization) - 高斯过程全局优化的 Python 实现。
* [SafeOpt](https://github.com/befelix/SafeOpt) - 安全贝叶斯优化。
* [scikit-optimize](https://github.com/scikit-optimize/scikit-optimize) - 使用“scipy.optimize”接口进行基于顺序模型的优化。
* [Solid](https://github.com/100/Solid) - 用 Python 编写的全面的无梯度优化框架。
* [PySwarms](https://github.com/ljvmiranda921/pyswarms) - Python 中粒子群优化的研究工具包。
* [Platypus](https://github.com/Project-Platypus/Platypus) - 用于多目标优化的免费开源 Python 库。
* [GPflowOpt](https://github.com/GPflow/GPflowOpt) - 使用 GPflow 进行贝叶斯优化。 <img height="20" src="img/tf_big2.png" alt="sklearn">
* [POT](https://github.com/rflamary/POT) - Python 最佳传输库。
* [Talos](https://github.com/autonomio/talos) - Keras 模型的超参数优化。
* [nlopt](https://github.com/stevengj/nlopt) - 用于非线性优化的库（全局和局部、受约束或无约束）。
* [OR-Tools](https://developers.google.com/optimization) - Google 用于优化的开源软件套件；为六个求解器提供统一的编程接口：SCIP、GLPK、GLOP、CP-SAT、CPLEX 和 Gurobi。

## 特征工程

### 一般
* [Featuretools](https://github.com/Featuretools/featuretools) - 自动化特征工程。
* [Feature Engine](https://github.com/feature-engine/feature_engine) - 具有类似 sklearn 功能的特征工程包。 <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [OpenFE](https://github.com/IIIS-Li-Group/OpenFE) - 具有专家级性能的自动特征生成。
* [skl-groups](https://github.com/dougalsutherland/skl-groups) - 一个 scikit-learn 插件，用于操作基于集合/“组”的功能。 <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [Feature Forge](https://github.com/machinalis/featureforge) - 一组用于创建和测试机器学习功能的工具。 <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [few](https://github.com/lacava/few) - sklearn 的特征工程包装器。 <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [scikit-mdr](https://github.com/EpistasisLab/scikit-mdr) - 用于特征构建的多因子降维 (MDR) 的与 sklearn 兼容的 Python 实现。 <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [tsfresh](https://github.com/blue-yonder/tsfresh) - 从时间序列中自动提取相关特征。 <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [dirty_cat](https://github.com/dirty-cat/dirty_cat) - 对脏表格数据进行机器学习（特别是：用于分类和回归的基于字符串的变量）。 <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [NitroFE](https://github.com/NITRO-AI/NitroFE) - 移动窗口功能。 <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [sk-transformer](https://github.com/chrislemke/sk-transformers) - 各种 pandas 和 scikit-learn 兼容转换器的集合，用于各种预处理和特征工程步骤 <img height="20" src="img/pandas_big.png" alt="pandas 兼容">
* [tubular](https://github.com/azukds/tubular) - 用 [narwhals](https://github.com/narwhals-dev/narwhals) 编写的 scikit-learn 兼容变压器集合，它可以接受 Polars/pandas 输入并在后台使用所选的库。 <img height="20" src="img/sklearn_big.png" alt="sklearn"><img height="20" src="img/pandas_big.png" alt="pandas 兼容">


### 特征选择
* [scikit-feature](https://github.com/jundongl/scikit-feature) - Python 中的特征选择存储库。
* [boruta_py](https://github.com/scikit-learn-contrib/boruta_py) - Boruta 所有相关特征选择方法的实现。 <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [BoostARoota](https://github.com/chasedehan/BoostARoota) - 一种快速 xgboost 特征选择算法。 <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [scikit-rebate](https://github.com/EpistasisLab/scikit-rebate) - ReBATE 的 scikit-learn 兼容 Python 实现，ReBATE 是一套基于 Relief 的机器学习特征选择算法。 <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [zoofs](https://github.com/jaswinder9051998/zoofs) - 基于进化算法的特征选择库。

## 可视化
### 通用型
* [Matplotlib](https://github.com/matplotlib/matplotlib) - 使用 Python 绘图。
* [seaborn](https://github.com/mwaskom/seaborn) - 使用 matplotlib 进行统计数据可视化。
* [prettyplotlib](https://github.com/olgabot/prettyplotlib) - 轻松创建漂亮的 matplotlib 绘图。
* [python-ternary](https://github.com/marcharper/python-ternary) - 使用 matplotlib 的 Python 三元绘图库。
* [missingno](https://github.com/ResidentMario/missingno) - 缺少 Python 数据可视化模块。
* [chartify](https://github.com/spotify/chartify/) - Python 库使数据科学家可以轻松创建图表。
* [physt](https://github.com/janpipek/physt) - 改进的直方图。
### 互动情节
* [animatplot](https://github.com/t-makaro/animatplot) - 一个基于 matplotlib 构建的动画绘图 Python 包。
* [plotly](https://plot.ly/python/) - 一个 Python 库，可制作交互式和出版质量的图表。
* [Bokeh](https://github.com/bokeh/bokeh) - Python 的交互式 Web 绘图。
* [Altair](https://altair-viz.github.io/) - Python 的声明式统计可视化库。可以轻松地在代码内进行许多数据转换以创建图形
* [bqplot](https://github.com/bqplot/bqplot) - IPython/Jupyter 笔记本的绘图库
* [pyecharts](https://github.com/pyecharts/pyecharts) - 从图表和可视化库 [Echarts](https://github.com/apache/echarts) 迁移到 Python 的交互式视觉绘图库。<img height="20" src="img/pyecharts.png" alt="pyecharts"> <img height="20" src="img/echarts.png" alt="echarts">
### 地图
* [folium](https://python-visualization.github.io/folium/quickstart.html#Getting-Started) - 可以轻松地在交互式开放街道地图上可视化数据
* [geemap](https://github.com/giswqs/geemap) - 使用 Google Earth Engine (GEE) 进行交互式绘图的 Python 包
### 自动绘图
* [HoloViews](https://github.com/ioam/holoviews) - 停止绘制数据 - 对数据进行注释并让它自行可视化。
* [AutoViz](https://github.com/AutoViML/AutoViz)：用 1 行代码自动可视化数据（非常适合机器学习）
* [SweetViz](https://github.com/fbdesignpro/sweetviz)：用一行代码可视化和比较数据集、目标值和关联。

### 自然语言处理
* [pyLDAvis](https://github.com/bmabey/pyLDAvis): 可视化交互式主题模型

## 部署
* [fastapi](https://fastapi.tiangolo.com/) - 现代、快速（高性能）的 Web 框架，用于使用 Python 构建 API
* [streamlit](https://www.streamlit.io/) - 轻松部署机器学习模型
* [streamsync](https://github.com/streamsync-cloud/streamsync) - 前面没有代码，后面有Python。用于创建数据应用程序的开源框架。
* [gradio](https://github.com/gradio-app/gradio) - 在 3 分钟内使用 Python 为您的机器学习模型创建 UI。
* [Vizro](https://github.com/mckinsey/vizro) - 用于创建模块化数据可视化应用程序的工具包。
* [datapane](https://datapane.com/) - 用于将脚本和笔记本转变为交互式报告的 API 集合。
* [binder](https://mybinder.org/) - 启用共享并执行 Jupyter Notebooks
* [Deepnote](https://github.com/deepnote/deepnote) - Deepnote 是 Jupyter 的直接替代品，具有 AI 优先的设计、时尚的 UI、新块和本机数据集成。在您最喜欢的 IDE 中本地使用 Python、R 和 SQL，然后扩展到 Deepnote 云以实现实时协作、Deepnote 代理和可部署的数据应用程序。


## 统计数据
* [pandas_summary](https://github.com/mouradmourafiq/pandas-summary) - pandas 数据框描述功能的扩展。 <img height="20" src="img/pandas_big.png" alt="pandas 兼容">
* [Pandas Profiling](https://github.com/pandas-profiling/pandas-profiling) - 从 pandas DataFrame 对象创建 HTML 分析报告。 <img height="20" src="img/pandas_big.png" alt="pandas 兼容">
* [statsmodels](https://github.com/statsmodels/statsmodels) - Python 中的统计建模和计量经济学。
* [stockstats](https://github.com/jealous/stockstats) - 提供基于“pandas.DataFrame”的包装器“StockDataFrame”，并支持内联股票统计/指标。
* [weightedcalcs](https://github.com/jsvine/weightedcalcs) - 一个基于 pandas 的实用程序，用于计算加权平均值、中位数、分布、标准差等。
* [scikit-posthocs](https://github.com/maximtrp/scikit-posthocs) - 成对多重比较事后测试。
* [Alphalens](https://github.com/quantopian/alphalens) - 预测（阿尔法）股票因素的绩效分析。


## 数据处理

### 数据框
* [pandas](https://pandas.pydata.org/pandas-docs/stable/) - 强大的Python数据分析工具包。
* [polars](https://github.com/pola-rs/polars) - 快速多线程、混合核外 DataFrame 库。
* [Arctic](https://github.com/manahl/arctic) - 用于时间序列和刻度数据的高性能数据存储。
* [datatable](https://github.com/h2oai/datatable) - Python 的 Data.table。 <img height="20" src="img/R_big.png" alt="R 启发/移植的 lib">
* [pandas_profiling](https://github.com/pandas-profiling/pandas-profiling) - 从 pandas DataFrame 对象创建 HTML 分析报告
* [cuDF](https://github.com/rapidsai/cudf) - GPU 数据帧库。 <img height="20" src="img/pandas_big.png" alt="pandas 兼容"> <img height="20" src="img/gpu_big.png" alt="GPU 加速">
* [blaze](https://github.com/blaze/blaze) - NumPy 和 pandas 与大数据的接口。 <img height="20" src="img/pandas_big.png" alt="pandas 兼容">
* [pandasql](https://github.com/yhat/pandasql) - 允许您使用 SQL 语法查询 pandas DataFrame。 <img height="20" src="img/pandas_big.png" alt="pandas 兼容">
* [pandas-gbq](https://github.com/pydata/pandas-gbq) - 熊猫谷歌大查询。 <img height="20" src="img/pandas_big.png" alt="pandas 兼容">
* [xpandas](https://github.com/alan-turing-institute/xpandas) - 具有 Transformers 功能的通用 1d/2d 数据容器，用于 [艾伦图灵研究所](https://www.turing.ac.uk/) 的数据分析。
* [pysparkling](https://github.com/svenkreiss/pysparkling) - Apache Spark 的 RDD 和 DStream 接口的纯 Python 实现。 <img height="20" src="img/spark_big.png" alt="基于 Apache Spark">
* [modin](https://github.com/modin-project/modin) - 通过更改一行代码来加快 pandas 工作流程。 <img height="20" src="img/pandas_big.png" alt="pandas 兼容">
* [swifter](https://github.com/jmcarpenter2/swifter) - 一个以最快的可用方式有效地将任何函数应用于 pandas 数据框或系列的包。
* [pandas-log](https://github.com/eyaltrabelsi/pandas-log) - 一个包，允许提供有关基本 pandas 操作的反馈并发现业务逻辑和性能问题。
* [vaex](https://github.com/vaexio/vaex) - 适用于 Python、ML 的核外数据框架，以每秒 10 亿行的速度可视化和探索大型表格数据。
* [xarray](https://github.com/pydata/xarray) - Xarray 结合了 NumPy 和 pandas 的最佳功能，用于多维数据选择，通过用命名维度补充数字轴标签，实现更直观、简洁且不易出错的索引例程。

### 管道
* [pdpipe](https://github.com/shaypal5/pdpipe) - pandas DataFrames 的 Sasy 管道。
* [SSPipe](https://sspipe.github.io/) - Python 管道 (|) 运算符，支持 DataFrames、Numpy 和 Pytorch。
* [pandas-ply](https://github.com/coursera/pandas-ply) - pandas 的函数式数据操作。 <img height="20" src="img/pandas_big.png" alt="pandas 兼容">
* [Dplython](https://github.com/dodger487/dplython) - Python 的 Dplyr。 <img height="20" src="img/R_big.png" alt="R 启发/移植的 lib">
* [sklearn-pandas](https://github.com/scikit-learn-contrib/sklearn-pandas) - pandas 与 sklearn 的集成。 <img height="20" src="img/sklearn_big.png" alt="sklearn"> <img height="20" src="img/pandas_big.png" alt="pandas 兼容">
* [Dataset](https://github.com/analysiscenter/dataset) - 帮助您方便地处理随机或连续批次的数据并定义数据处理。
* [pyjanitor](https://github.com/ericmjl/pyjanitor) - 用于数据清理的清理 API。 <img height="20" src="img/pandas_big.png" alt="pandas 兼容">
* [meza](https://github.com/reubano/meza) - 用于处理表格数据的 Python 工具包。
* [Prodmodel](https://github.com/prodmodel/prodmodel) - 构建数据科学管道系统。
* [dopanda](https://github.com/dovpanda-dev/dovpanda) - 在分析环境中使用 pandas 的提示和技巧。 <img height="20" src="img/pandas_big.png" alt="pandas 兼容">
* [Hamilton](https://github.com/DAGWorks-Inc/hamilton) - 用于数据帧生成的微框架，应用由延迟计算的 Python 函数流指定的有向无环图。

### 以数据为中心的人工智能
* [cleanlab](https://github.com/cleanlab/cleanlab) - 标准的以数据为中心的人工智能包，用于数据质量和机器学习，包含混乱的真实数据和标签。
* [snorkel](https://github.com/snorkel-team/snorkel) - 一种弱监督快速生成训练数据的系统。
* [dataprep](https://github.com/sfu-db/dataprep) - 只需几行代码即可在 Python 中收集、清理和可视化您的数据。

### 综合数据

* [ydata-synthetic](https://github.com/ydataai/ydata-synthetic) - 一个利用最先进的生成模型生成合成表格和时间序列数据的包。 <img height="20" src="img/pandas_big.png" alt="pandas 兼容">

## 分布式计算
* [Horovod](https://github.com/uber/horovod) - 适用于 TensorFlow、Keras、PyTorch 和 Apache MXNet 的分布式训练框架。 <img height="20" src="img/tf_big2.png" alt="sklearn">
* [PySpark](https://spark.apache.org/docs/0.9.0/python-programming-guide.html) - 将 Spark 编程模型公开给 Python。 <img height="20" src="img/spark_big.png" alt="基于 Apache Spark">
* [Veles](https://github.com/Samsung/veles) - 分布式机器学习平台。
* [Jubatus](https://github.com/jubatus/jubatus) - 分布式在线机器学习的框架和库。
* [DMTK](https://github.com/Microsoft/DMTK) - 微软分布式机器学习工具包。
* [PaddlePaddle](https://github.com/PaddlePaddle/Paddle) - 并行分布式深度学习。
* [dask-ml](https://github.com/dask/dask-ml) - 分布式并行机器学习。 <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [Distributed](https://github.com/dask/distributed) - Python 中的分布式计算。

## 实验
* [mlflow](https://github.com/mlflow/mlflow) - 适用于机器学习生命周期的开源平台。
* [Neptune](https://neptune.ai) - 轻量级 ML 实验跟踪、结果可视化和管理工具。
* [dvc](https://github.com/iterative/dvc) - 数据版本控制|用于数据和模型的 Git |机器学习实验管理。
* [envd](https://github.com/tensorchord/envd) - 🏕️ 面向数据科学和 AI/ML 工程团队的机器学习开发环境。
* [Sacred](https://github.com/IDSIA/sacred) - 一个帮助您配置、组织、记录和重现实验的工具。
* [Ax](https://github.com/facebook/Ax) - 自适应实验平台。 <img height="20" src="img/sklearn_big.png" alt="sklearn">

## 数据验证
* [great_expectations](https://github.com/great-expectations/great_expectations) - 始终了解您的数据会带来什么结果。
* [pandera](https://github.com/unionai-oss/pandera) - 一个轻量级、灵活且富有表现力的统计数据测试库。
* [deepchecks](https://github.com/deepchecks/deepchecks) - 在模型开发、部署和生产过程中验证和测试 ML 模型和数据。 <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [evidently](https://github.com/evidentlyai/evidently) - 评估和监控 ML 模型从验证到生产的整个过程。
* [TensorFlow Data Validation](https://github.com/tensorflow/data-validation) - 用于探索和验证机器学习数据的库。
* [DataComPy](https://github.com/capitalone/datacompy) - 用于比较 Pandas、Polars 和 Spark 数据帧的库。它提供统计数据并允许用户调整匹配准确性。

## 评价
* [recmetrics](https://github.com/statisticianinstilettos/recmetrics) - 用于评估推荐系统的有用指标和图表库。
* [Metrics](https://github.com/benhamner/Metrics) - 机器学习评估指标。
* [sklearn-evaluation](https://github.com/edublancas/sklearn-evaluation) - 模型评估变得简单：绘图、表格和降价报告。 <img height="20" src="img/sklearn_big.png" alt="sklearn">
* [AI Fairness 360](https://github.com/IBM/AIF360) - 数据集和机器学习模型的公平性指标、解释和算法，以减轻数据集和模型中的偏差。
* [alibi-detect](https://github.com/SeldonIO/alibi-detect) - 用于异常值、对抗性和漂移检测的算法。<img height="20" src="img/alibi-detect.png" alt="sklearn">

## 计算
* [NumPy](https://numpy.org/) - 使用 Python 进行科学计算的基础包
* [Dask](https://github.com/dask/dask) - 并行计算与任务调度。 <img height="20" src="img/pandas_big.png" alt="pandas 兼容">
* [bottleneck](https://github.com/kwgoodman/bottleneck) - 用 C 编写的快速 NumPy 数组函数。
* [CuPy](https://github.com/cupy/cupy) - 使用 CUDA 加速的类似 NumPy 的 API。
* [scikit-tensor](https://github.com/mnick/scikit-tensor) - 用于多线性代数和张量分解的 Python 库。
* [numdifftools](https://github.com/pbrod/numdifftools) - 解决一个或多个变量的自动数值微分问题。
* [quaternion](https://github.com/moble/quaternion) - 向 numpy 添加对四元数的内置支持。
* [adaptive](https://github.com/python-adaptive/adaptive) - 用于数学函数自适应和并行采样的工具。
* [NumExpr](https://github.com/pydata/numexpr) - NumPy 的快速数值表达式评估器，配有集成计算虚拟机，可通过避免中间结果的内存分配来加速计算。

## 网页抓取
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)：适合初学者抓取静态网站的最简单的库
* [Scrapy](https://scrapy.org/)：快速且可扩展的抓取库。可以编写规则并创建自定义的抓取工具，而无需触及核心
* [Selenium](https://selenium-python.readthedocs.io/installation.html#introduction): 使用 Selenium Python API 像真实用户一样直观地访问 Selenium WebDriver 的所有功能。
* [Pattern](https://github.com/clips/pattern)：针对 Google、Twitter 和 Wikipedia 等成熟网站的高级抓取。还有NLP、机器学习算法和可视化
* [twitterscraper](https://github.com/taspinar/twitterscraper)：抓取 Twitter 的高效库

## 空间分析
* [GeoPandas](https://github.com/geopandas/geopandas) - 用于地理数据的 Python 工具。 <img height="20" src="img/pandas_big.png" alt="pandas 兼容">
* [PySal](https://github.com/pysal/pysal) - Python 空间分析库。

## 量子计算
* [qiskit](https://github.com/Qiskit/qiskit) - Qiskit 是一款开源 SDK，用于在电路、算法和应用模块级别与量子计算机配合使用。
* [cirq](https://github.com/quantumlib/Cirq) - 用于创建、编辑和调用噪声中级量子 (NISQ) 电路的 Python 框架。
* [PennyLane](https://github.com/XanaduAI/pennylane) - 量子机器学习、自动微分以及混合量子经典计算的优化。
* [QML](https://github.com/qmlcode/qml) - 用于量子机器学习的 Python 工具包。

## 转换
* [sklearn-porter](https://github.com/nok/sklearn-porter) - Transpile 将经过训练的 scikit-learn 估计器转换为 C、Java、JavaScript 等。
* [ONNX](https://github.com/onnx/onnx) - 打开神经网络交换。
* [MMdnn](https://github.com/Microsoft/MMdnn) - 一组帮助用户在不同深度学习框架之间进行互操作的工具。
* [treelite](https://github.com/dmlc/treelite) - 决策树森林的通用模型交换和序列化格式。

## 贡献
欢迎贡献！ ：太阳镜：</br>
阅读<a href=https://github.com/krzjoa/awesome-python-datascience/blob/master/CONTRIBUTING.md>贡献指南</a>。

## 许可证
本作品根据知识共享署名 4.0 国际许可证 - [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) 获得许可
