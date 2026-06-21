# 用于科学音频的 Python
[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome) [![Build Status](https://github.com/faroit/awesome-python-scientific-audio/workflows/CI/badge.svg)](https://github.com/faroit/awesome-python-scientific-audio/actions?query=workflow%3ACI+branch%3Amaster+event%3Apush)

该存储库的目的是创建一个全面的、精选的与音频/音乐应用科学研究相关的 python 软件/工具列表。

## 内容

* [音频相关包](#audio-related-packages)
    - [Read/Write](#read-write)
    - [转换 - 通用 DSP](#transformations---general-dsp)
    - [特征提取](#feature-extraction)
    - [数据增强](#data-augmentation)
    - [语音处理](#speech-processing)
    - [环境声音](#environmenta)
    - [感知模型 - 听觉模型](#perceptial-models---auditory-models)
    - [源头分离](#source-separation)
    - [音乐信息检索](#music-information-retrieval)
    - [深度学习](#deep-learning)
    - [象征音乐 - MIDI - 音乐学](#symbolic-music---midi---musicology)
    - [实时应用](#realtime-applications)
    - [网络 - 音频](#web-audio)
    - [音频相关的 API 和数据集](#audio-related-apis-and-datasets)
    - [音频插件的包装器](#wrappers-for-audio-plugins)
* [Tutorials](#tutorials)
* [Books](#books)
* [科学论文](#scientific-papers)
* [其他资源](#other-resources)
* [相关列表](#related-lists)
* [Contributing](#contributing)
* [License](#license)


## 音频相关包

- 包裹总数：67

#### 读写

* [audiolazy](https://github.com/danilobellini/audiolazy) [:octocat:](https://github.com/danilobellini/audiolazy) [:package:](https://pypi.python.org/pypi/audiolazy/) - 用于 Python 的富有表现力的数字信号处理 (DSP) 包。
* [audioread](https://github.com/beetbox/audioread) [:octocat:](https://github.com/beetbox/audioread) [:package:](https://pypi.python.org/pypi/audioread/) - 跨库（GStreamer + Core Audio + MAD + FFmpeg）音频解码。
* [mutagen](https://mutagen.readthedocs.io/) [:octocat:](https://github.com/quodlibet/mutagen) [:package:](https://pypi.python.org/pypi/mutagen) - 读取和写入各种格式的各种音频元数据。
* [pyAV](http://docs.mikeboers.com/pyav/) [:octocat:](https://github.com/mikeboers/PyAV) - PyAV 是 FFmpeg 或 Libav 的 Pythonic 绑定。
* [pyfar](https://pyfar.readthedocs.io) [:octocat:](https://github.com/pyfar/pyfar) [:package:](https://pypi.org/project/pyfar/) - 使用 [pyfar.io](https://pyfar.readthedocs.io/en/stable/modules/pyfar.io.html) 模块读取音频文件、SOFA 文件和 COMSOL 数据。
* [(Py)Soundfile](http://pysoundfile.readthedocs.io/) [:octocat:](https://github.com/bastibe/PySoundFile) [:package:](https://pypi.python.org/pypi/SoundFile) - 基于 libsndfile、CFFI 和 NumPy 的库。
* [pySox](https://github.com/rabitt/pysox) [:octocat:](https://github.com/rabitt/pysox) [:package:](https://pypi.python.org/pypi/pysox/) - sox 的包装器。
* [stempeg](https://github.com/faroit/stempeg) [:octocat:](https://github.com/faroit/stempeg) [:package:](https://pypi.python.org/pypi/stempeg/) - STEMS 多流音频的读/写。
* [tinytag](https://github.com/devsnd/tinytag) [:octocat:](https://github.com/devsnd/tinytag) [:package:](https://pypi.python.org/pypi/tinytag/) - 读取 MP3、OGG、FLAC 和 Wave 文件的音乐元数据。

#### 转换 - 通用 DSP

* [acoustics](http://python-acoustics.github.io/python-acoustics/) [:octocat:](https://github.com/python-acoustics/python-acoustics/) [:package:](https://pypi.python.org/pypi/acoustics) - 对声学学家有用的工具。
* [AudioTK](https://github.com/mbrucher/AudioTK) [:octocat:](https://github.com/mbrucher/AudioTK) - DSP 滤波器工具箱（很多滤波器）。
* [AudioTSM](https://audiotsm.readthedocs.io/) [:octocat:](https://github.com/Muges/audiotsm) [:package:](https://pypi.python.org/pypi/audiotsm/) - 实时音频时间尺度修改程序。
* [Gammatone](https://github.com/detly/gammatone) [:octocat:](https://github.com/detly/gammatone) - Gammatone 滤波器组实现。
* [pyFFTW](http://pyfftw.github.io/pyFFTW/) [:octocat:](https://github.com/pyFFTW/pyFFTW) [:package:](https://pypi.python.org/pypi/pyFFTW/) - FFTW(3) 的包装器。
* [NSGT](https://grrrr.org/research/software/nsgt/) [:octocat:](https://github.com/grrrrr/nsgt) [:package:](https://pypi.python.org/pypi/nsgt) - 非平稳 gabor 变换，常数 q。
* [matchering](https://github.com/sergree/matchering) [:octocat:](https://github.com/sergree/matchering) [:package:](https://pypi.org/project/matchering/) - 自动参考音频母带制作。
* [MDCT](https://github.com/nils-werner/mdct) [:octocat:](https://github.com/nils-werner/mdct) [:package:](https://pypi.python.org/pypi/mdct) - MDCT 变换。
* [pydub](http://pydub.com) [:octocat:](https://github.com/jiaaro/pydub) [:package:](https://pypi.python.org/pypi/mdct) - 使用简单易用的高级界面操作音频。
* [pyfar](https://pyfar.readthedocs.io) [:octocat:](https://github.com/pyfar/pyfar) [:package:](https://pypi.org/project/pyfar/) - 使用 [pyfar.dsp](https://pyfar.readthedocs.io/en/stable/modules/pyfar.dsp.html) 模块执行针对声学信号定制的通用 DSP 和过滤。
* [pytftb](http://tftb.nongnu.org) [:octocat:](https://github.com/scikit-signal/pytftb) - MATLAB 时频工具箱的实现。
* [pyroomacoustics](https://github.com/LCAV/pyroomacoustics) [:octocat:](https://github.com/LCAV/pyroomacoustics) [:package:](https://pypi.python.org/pypi/pyroomacoustics) - 房间声学模拟（RIR 生成器）
* [PyRubberband](https://github.com/bmcfee/pyrubberband) [:octocat:](https://github.com/bmcfee/pyrubberband) [:package:](https://pypi.python.org/pypi/pyrubberband/) - [rubberband](http://breakfastquay.com/rubberband/) 的包装器，用于进行音调变换和时间拉伸。
* [PyWavelets](http://pywavelets.readthedocs.io) [:octocat:](https://github.com/PyWavelets/pywt) [:package:](https://pypi.python.org/pypi/PyWavelets) - Python 中的离散小波变换。
* [Resampy](http://resampy.readthedocs.io) [:octocat:](https://github.com/bmcfee/resampy) [:package:](https://pypi.python.org/pypi/resampy) - 采样率转换。
* [SFS-Python](http://www.sfstoolbox.org) [:octocat:](https://github.com/sfstoolbox/sfs-python) [:package:](https://pypi.python.org/pypi/sfs/) - 声场合成工具箱。
* [sound_field_analysis](https://appliedacousticschalmers.github.io/sound_field_analysis-py/) [:octocat:](https://github.com/AppliedAcousticsChalmers/sound_field_analysis-py) [:package:](https://pypi.org/project/sound-field-analysis/) - 分析、可视化和处理球形麦克风阵列记录的声场数据。
* [STFT](http://stft.readthedocs.io) [:octocat:](https://github.com/nils-werner/stft) [:package:](https://pypi.python.org/pypi/stft) - 用于短时傅立叶变换的独立包。

#### 特征提取

* [aubio](http://aubio.org/) [:octocat:](https://github.com/aubio/aubio) [:package:](https://pypi.python.org/pypi/aubio) - 特征提取器，用 C、Python 界面编写。
* [audioFlux](https://github.com/libAudioFlux/audioFlux) [:octocat:](https://github.com/libAudioFlux/audioFlux) [:package:](https://pypi.python.org/pypi/audioFlux) - 用于音频和音乐分析、特征提取的库。
* [audiolazy](https://github.com/danilobellini/audiolazy) [:octocat:](https://github.com/danilobellini/audiolazy) [:package:](https://pypi.python.org/pypi/audiolazy/) - 实时音频处理库，通用。
* [essentia](http://essentia.upf.edu) [:octocat:](https://github.com/MTG/essentia) - 音乐相关的低级和高级特征提取器，基于 C++，包括 Python 绑定。
* [python_speech_features](https://github.com/jameslyons/python_speech_features) [:octocat:](https://github.com/jameslyons/python_speech_features) [:package:](https://pypi.python.org/pypi/python_speech_features) - ASR 的常见语音特征。
* [pyYAAFE](https://github.com/Yaafe/Yaafe) [:octocat:](https://github.com/Yaafe/Yaafe) - YAAFE 特征提取器的 Python 绑定。
* [speechpy](https://github.com/astorfi/speechpy) [:octocat:](https://github.com/astorfi/speechpy) [:package:](https://pypi.python.org/pypi/speechpy) - 用于语音处理和识别的库，目前主要是特征提取。
* [spafe](https://github.com/SuperKogito/spafe) [:octocat:](https://github.com/SuperKogito/spafe) [:package:](https://pypi.org/project/spafe/) - 用于从音频文件中提取特征的 Python 库。

#### 数据增强

* [audiomentations](https://github.com/iver56/audiomentations) [:octocat:](https://github.com/iver56/audiomentations) [:package:](https://pypi.org/project/audiomentations/) - 音频数据增强。
* [muda](https://muda.readthedocs.io/en/latest/) [:octocat:](https://github.com/bmcfee/muda) [:package:](https://pypi.python.org/pypi/muda) - 音乐数据增强。
* [pydiogment](https://github.com/SuperKogito/pydiogment) [:octocat:](https://github.com/SuperKogito/pydiogment) [:package:](https://pypi.org/project/pydiogment/) - 音频数据增强。

#### 语音处理

* [aeneas](https://www.readbeyond.it/aeneas/) [:octocat:](https://github.com/readbeyond/aeneas/) [:package:](https://pypi.python.org/pypi/aeneas/) - 强制对齐器，基于 MFCC+DTW，超过 35 种语言。
* [deepspeech](https://github.com/mozilla/DeepSpeech) [:octocat:](https://github.com/mozilla/DeepSpeech) [:package:](https://pypi.org/project/deepspeech/) - 预训练的自动语音识别。
* [gentle](https://github.com/lowerquality/gentle) [:octocat:](https://github.com/lowerquality/gentle) - 基于 Kaldi 构建的强制对齐器。
* [Parselmouth](https://github.com/YannickJadoul/Parselmouth) [:octocat:](https://github.com/YannickJadoul/Parselmouth) [:package:](https://pypi.org/project/praat-parselmouth/) - [Praat](http://www.praat.org) 语音和语音分析、合成和操作软件的 Python 接口。
* [persephone](https://persephone.readthedocs.io/en/latest/) [:octocat:](https://github.com/persephone-tools/persephone) [:package:](https://pypi.org/project/persephone/) - 自动音素转录工具。
* [pyannote.audio](https://github.com/pyannote/pyannote-audio) [:octocat:](https://github.com/pyannote/pyannote-audio) [:package:](https://pypi.org/project/pyannote-audio/) - 用于说话人二值化的神经构建块。
* [pyAudioAnalysis](https://github.com/tyiannak/pyAudioAnalysis)² [:octocat:](https://github.com/tyiannak/pyAudioAnalysis) [:package:](https://pypi.python.org/pypi/pyAudioAnalysis/) - 特征提取、分类、二值化。
* [py-webrtcvad](https://github.com/wiseman/py-webrtcvad) [:octocat:](https://github.com/wiseman/py-webrtcvad) [:package:](https://pypi.python.org/pypi/webrtcvad/) - WebRTC 语音活动检测器的接口。
* [pypesq](https://github.com/vBaiCai/python-pesq) [:octocat:](https://github.com/vBaiCai/python-pesq) - PESQ 分数计算的包装器。
* [pystoi](https://github.com/mpariente/pystoi) [:octocat:](https://github.com/mpariente/pystoi) [:package:](https://pypi.org/project/pystoi) - 短期目标清晰度度量 (STOI)。
* [visqol-python](https://github.com/talker93/visqol-python) [:octocat:](https://github.com/talker93/visqol-python) [:package:](https://pypi.org/project/visqol-python/) - Google 的 ViSQOL 音频/语音质量指标 (MOS-LQO) 的端口，无需 Bazel 即可安装。
* [PyWorldVocoder](https://github.com/JeremyCCHsu/Python-Wrapper-for-World-Vocoder) [:octocat:](https://github.com/JeremyCCHsu/Python-Wrapper-for-World-Vocoder) - Morise 世界声码器的包装器。
* [Montreal Forced Aligner](https://montrealcorpustools.github.io/Montreal-Forced-Aligner/) [:octocat:](https://github.com/MontrealCorpusTools/Montreal-Forced-Aligner) - 强制对齐器，基于Kaldi（HMM），英语（其他可以训练）。
* [SIDEKIT](http://lium.univ-lemans.fr/sidekit/) [:package:](https://pypi.python.org/pypi/SIDEKIT/) - 说话人和语言识别。
* [SpeechRecognition](https://github.com/Uberi/speech_recognition) [:octocat:](https://github.com/Uberi/speech_recognition) [:package:](https://pypi.python.org/pypi/SpeechRecognition/) - 多个 ASR 引擎和 API 的包装器，在线和离线。

#### 环境声音

* [sed_eval](http://tut-arg.github.io/sed_eval) [:octocat:](https://github.com/TUT-ARG/sed_eval) [:package:](https://pypi.org/project/sed_eval/) - 用于声音事件检测的评估工具箱

#### 感知模型 - 听觉模型

* [cochlea](https://github.com/mrkrd/cochlea) [:octocat:](https://github.com/mrkrd/cochlea) [:package:](https://pypi.python.org/pypi/cochlea/) - 内耳模型。
* [Brian2](http://briansimulator.org/) [:octocat:](https://github.com/brian-team/brian2) [:package:](https://pypi.python.org/pypi/Brian2) - 尖峰神经网络模拟器，包括耳蜗模型。
* [Loudness](https://github.com/deeuu/loudness) [:octocat:](https://github.com/deeuu/loudness) - 感知响度，包括 Zwicker、Moore/Glasberg 模型。
* [pyloudnorm](https://www.christiansteinmetz.com/projects-blog/pyloudnorm) [:octocat:](https://github.com/csteinmetz1/pyloudnorm) - 音频响度计和标准化，实现 ITU-R BS.1770-4。
* [声场合成工具箱](http://www.sfstoolbox.org) [:octocat:](https://github.com/sfstoolbox/sfs-python) [:package:](https://pypi.python.org/pypi/sfs/) - 声场合成工具箱。

#### 源头分离

* [commonfate](https://github.com/aliutkus/commonfate) [:octocat:](https://github.com/aliutkus/commonfate) [:package:](https://pypi.python.org/pypi/commonfate) - 共同命运模型和转换。
* [NTFLib](https://github.com/stitchfix/NTFLib) [:octocat:](https://github.com/stitchfix/NTFLib) - 稀疏 Beta 散度张量分解。
* [NUSSL](https://interactiveaudiolab.github.io/project/nussl.html) [:octocat:](https://github.com/interactiveaudiolab/nussl) [:package:](https://pypi.python.org/pypi/nussl) - 整体源分离框架，包括 DSP 方法和深度学习方法。
* [NIMFA](http://nimfa.biolab.si) [:octocat:](https://github.com/marinkaz/nimfa) [:package:](https://pypi.python.org/pypi/nimfa) - 非负矩阵分解的几种风格。

#### 音乐信息检索

* [Catchy](https://github.com/jvbalen/catchy) [:octocat:](https://github.com/jvbalen/catchy) - 用于计算 Hook 发现的语料库分析工具。
* [和弦检测](https://github.com/sevagh/chord-detection) [:octocat:](https://github.com/sevagh/chord-detection) - 和弦检测和调估计的算法。
* [Madmom](https://madmom.readthedocs.io/en/latest/) [:octocat:](https://github.com/CPJKU/madmom) [:package:](https://pypi.python.org/pypi/madmom) - MIR 包，重点关注节拍检测、起始检测和和弦识别。
* [mir_eval](http://craffel.github.io/mir_eval/) [:octocat:](https://github.com/craffel/mir_eval) [:package:](https://pypi.python.org/pypi/mir_eval) - 各种 MIR 任务的常见分数。还包括 bss_eval 实现。
* [msaf](http://pythonhosted.org/msaf/) [:octocat:](https://github.com/urinieto/msaf) [:package:](https://pypi.python.org/pypi/msaf) - 音乐结构分析框架。
* [librosa](http://librosa.github.io/librosa/) [:octocat:](https://github.com/librosa/librosa) [:package:](https://pypi.python.org/pypi/librosa) - 一般音频和音乐分析。

#### 深度学习

* [Kapre](https://github.com/keunwoochoi/kapre) [:octocat:](https://github.com/keunwoochoi/kapre) [:package:](https://pypi.python.org/pypi/kapre) - Keras 音频预处理器
* [TorchAudio](https://github.com/pytorch/audio) [:octocat:](https://github.com/pytorch/audio) - PyTorch 音频加载器
* [nnAudio](https://github.com/KinWaiCheuk/nnAudio) [:octocat:](https://github.com/KinWaiCheuk/nnAudio) [:package:](https://pypi.org/project/nnAudio/) - 在 PyTorch 中使用 1D 卷积网络加速音频处理。

#### 象征音乐 - MIDI - 音乐学

* [Music21](http://web.mit.edu/music21/) [:octocat:](https://github.com/cuthbertLab/music21) [:package:](https://pypi.python.org/pypi/music21) - 计算机辅助音乐学工具包。
* [Mido](https://mido.readthedocs.io/en/latest/) [:octocat:](https://github.com/olemb/mido) [:package:](https://pypi.python.org/pypi/mido) - 实时 MIDI 包装器。
* [mingus](https://github.com/bspaans/python-mingus) [:octocat:](https://github.com/bspaans/python-mingus) [:package:](https://pypi.org/project/mingus) - 高级音乐理论和记谱包，具有 MIDI 文件和播放支持。
* [Pretty-MIDI](http://craffel.github.io/pretty-midi/) [:octocat:](https://github.com/craffel/pretty-midi) [:package:](https://pypi.python.org/pypi/pretty-midi) - 以良好/直观的方式处理 MIDI 数据的实用函数。

#### 实时应用

* [Jupylet](https://github.com/nir/jupylet) [:octocat:](https://github.com/nir/jupylet) - 减法、加法、FM 和基于样本的声音合成。
* [PYO](http://ajaxsoundstudio.com/software/pyo/) [:octocat:](https://github.com/belangeo/pyo) - 实时音频 DSP 引擎。
* [python-sounddevice](https://github.com/spatialaudio/python-sounddevice) [:octocat:](http://python-sounddevice.readthedocs.io) [:package:](https://pypi.python.org/pypi/sounddevice) - PortAudio 包装器通过 NumPy 提供实时音频 I/O。
* [ReTiSAR](https://github.com/AppliedAcousticsChalmers/ReTiSAR) [:octocat:](https://github.com/AppliedAcousticsChalmers/ReTiSAR) - 流式或基于 IR 的高阶球形麦克风阵列信号的双耳渲染。

#### 网络音频

* [TimeSide (Beta)](https://github.com/Parisson/TimeSide/tree/dev) [:octocat:](https://github.com/Parisson/TimeSide/tree/dev) - 高级音频分析、成像、转码、流媒体和标签。

#### 音频数据集和数据加载器

* [beets](http://beets.io/) [:octocat:](https://github.com/beetbox/beets) [:package:](https://pypi.python.org/pypi/beets) - 音乐库管理器和 [MusicBrainz](https://musicbrainz.org/) 标记器。
* [musdb](http://dsdtools.readthedocs.io) [:octocat:](https://github.com/sigsep/sigsep-mus-db) [:package:](https://pypi.python.org/pypi/musdb) - 解析和处理 MUSDB18 数据集。
* [medleydb](http://medleydb.readthedocs.io) [:octocat:](https://github.com/marl/medleydb) - 解析 [medleydb](http://medleydb.weebly.com/) 音频+注释。
* [Soundcloud API](https://github.com/soundcloud/soundcloud-python) [:octocat:](https://github.com/soundcloud/soundcloud-python) [:package:](https://pypi.python.org/pypi/soundcloud) - [Soundcloud API](https://developers.soundcloud.com/) 的包装器。
* [Youtube-Downloader](http://rg3.github.io/youtube-dl/) [:octocat:](https://github.com/rg3/youtube-dl) [:package:](https://pypi.python.org/pypi/youtube_dl) - 下载 youtube 视频（和音频）。
* [audiomate](https://github.com/ynop/audiomate) [:octocat:](https://github.com/ynop/audiomate) [:package:](https://pypi.python.org/pypi/audiomate/) - 加载不同类型的音频数据集。
* [mirdata](https://mirdata.readthedocs.io/en/latest/) [:octocat:](https://github.com/mir-dataset-loaders/mirdata) [:package:](https://pypi.python.org/pypi/mirdata) - 音乐信息检索 (MIR) 数据集的通用加载器。
#### 音频插件的包装器

* [VamPy Host](https://code.soundsoftware.ac.uk/projects/vampy-host) [:package:](https://pypi.python.org/pypi/vamp) - 接口编译的 vamp 插件。

## 教程

* [Python 旋风之旅](https://jakevdp.github.io/WhirlwindTourOfPython/) [:octocat:](https://github.com/jakevdp/WhirlwindTourOfPython
) - 针对研究人员和开发人员的 Python 基础知识快速介绍。
* [Numpy 和 Scipy 简介](http://www.scipy-lectures.org/index.html) [:octocat:](https://github.com/scipy-lectures/scipy-lecture-notes) - 强烈推荐的教程，涵盖了科学 Python 生态系统的大部分内容。
* [Numpy for MATLAB® Users](https://docs.scipy.org/doc/numpy/user/numpy-for-matlab-users.html) - 切换器的等效 Python 函数的简短概述。
* [MIR Notebooks](http://musicinformationretrieval.com/) [:octocat:](https://github.com/stevetjoa/stanford-mir) - 用于音乐信息检索 (MIR) 的教学 iPython 笔记本集合。
* [Selected Topics in Audio Signal Processing]( https://github.com/spatialaudio/selected-topics-in-audio-signal-processing-exercises) - 作为 iPython 笔记本进行练习。
* [实时编码音乐合成器](https://www.youtube.com/watch?v=SSyQ0kRHzis) 实时编码视频，展示如何使用 SoundDevice 库再现真实的声音。 [代码](https://github.com/cool-RR/python_synthesizer)。
* [pyfar examples](https://pyfar-gallery.readthedocs.io/en/latest/examples_gallery.html) - 用于声学研究的 python 包 (pyfar) 的简介和示例。

## 书籍

* [Python Data Science Handbook](https://github.com/jakevdp/PythonDataScienceHandbook) - Jake Vanderplas，优秀书籍和随附的教程笔记本。
* [Fundamentals of Music Processing](https://www.audiolabs-erlangen.de/fau/professor/mueller/bookFMP) - Meinard Müller，附带 Python 练习。

## 科学论文

* [Python for audio signal processing](http://eprints.maynoothuniversity.ie/4115/1/40.pdf) - John C. Glover、Victor Lazzarini 和 Joseph Timoney，2011 年 Linux 音频会议。
* [librosa：Python 中的音频和音乐信号分析](http://conference.scipy.org/proceedings/scipy2015/pdfs/brian_mcfee.pdf)，[视频](https://www.youtube.com/watch?v=MhOdbtPhbLU) - Brian McFee、Colin Raffel、Dawen Liang、Daniel P.W.埃利斯、马特·麦克维卡、埃里克·巴滕伯格、奥里奥尔·涅托，Scipy 2015。
* [pyannote.audio：说话人二值化的神经构建模块](https://arxiv.org/abs/1911.01255)、[视频](https://www.youtube.com/watch?v=37R_R82lfwA) - Hervé Bredin、Ruiqing Yin、Juan Manuel Coria、Gregory Gelly、Pavel Korshunov、Marvin Lavechin、Diego Fustes、Hadrien Titeux、Wassim Bouaziz、Marie-Philippe Gill，ICASSP 2020。

## 其他资源

* [Coursera Course](https://www.coursera.org/learn/audio-signal-processing) - 音频信号处理，巴塞罗那 UPF 和斯坦福大学基于 Python 的课程。
* [Digital Signal Processing Course](http://dsp-nbsphinx.readthedocs.io/en/nbsphinx-experiment/index.html) - 硕士课程材料（罗斯托克大学），包含许多 Python 示例。
* [Slack Channel](https://mircommunity.slack.com) - 音乐信息检索社区。

## 相关列表

已经有 [PythonInMusic](https://wiki.python.org/moin/PythonInMusic)，但它不是最新的，并且包含太多特别感兴趣的包，这些包大多与科学应用无关。 [Awesome-Python](https://github.com/vinta/awesome-python) 是一个大型的 Python 包精选列表。然而，音频部分非常小。

## 贡献

随时欢迎您的贡献！请先查看[贡献指南](CONTRIBUTING.md)。

如果我不确定这些库是否很棒，我将保留一些拉取请求，您可以通过添加 👍 来投票给它们。

## 执照

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
