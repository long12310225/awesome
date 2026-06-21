# 👁️‍🗨️很棒的 VLM 架构 | [双视图](https://dualview.ai) [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
![VLM](https://github.com/gokayfem/Awesome-VLM-Architectures/assets/88277926/5c9ee091-1f37-4d92-8398-a7d4e006c014)

**视觉语言模型 (VLM)** 采用多模式架构，可同时处理图像和文本数据。他们可以执行**视觉问答（VQA）**、**图像字幕**和**文本到图像搜索**类型的任务。 VLM 利用交叉注意力的多模态融合、掩码语言建模和图像文本匹配等技术将视觉语义与文本表示联系起来。该存储库包含有关著名视觉语言模型 (VLM) 的信息，包括有关其架构、训练过程和用于训练的数据集的详细信息。 **单击展开以了解每种架构的更多详细信息**
- 📙 <a href="https://github.com/gokayfem/ComfyUI_VLM_nodes">访问我的其他存储库以尝试 ComfyUI 上的视觉语言模型</a>

## 内容

- [Architectures](#architectures)
- [重要参考资料](#important-references)
- [Tools](#tools)

## 型号

[LLaVA](#llava-大型语言和视觉助手---视觉指令调整) | [LLaVA 1.5]（#llava-15-改进的基线与视觉指令调整）| [LLaVA 1.6](#llava-16-llava-next-improved-reasoning-ocr-and-world-knowledge) | [PaliGemma](#paligemma-a-versatile-and-transferable-3b-vision-language-model) | [PaliGemma 2](#paligemma-2-a-family-of-versatile-vlms-for-transfer) | [AIMv2](#aimv2-多模态自回归大视觉编码器预训练) | [Apollo](#apollo-大型多模态模型中视频理解的探索) | [ARIA](#aria-an-open-multimodal-native-mixture-of-experts-model) | [EVE](#eve-unveiling-encoder-free-vision-language-models) | [EVEv2](#evev2-improved-baselines-for-encoder-free-vision-language-models) | [Janus-Pro](#janus-pro-unified-multimodal-understanding-and- Generation-with-data-and-model-scaling)| [LLaVA-CoT](#llava-cot-let-vision-language-models-reason-step-by-step) | [LLM2CLIP](#llm2clip-强大的语言模型解锁更丰富的视觉表示)| [Maya](#maya-an-instruction-finetuned-multilingual-multimodal-model) | [MiniMax-01](#minimax-01-scaling-foundation-models-with-lightning-attention) | [NVLM](#nvlm-开放前沿-类-多模式-llms) | [OmniVLM](#omnivlm-a-token-compressed-sub-billion-parameter-vision-language-model-for-efficient-on-device-inference)| [Pixtral 12B](#pixtral-12b-a-cutting-edge-开放多模式语言模型) | [Sa2VA](#sa2va-marrying-sam2-with-llava-for-dense-grounded-understanding-of-images-and-video)| [Tarsier2](#tarsier2-advancing-大视觉-语言模型-从详细的视频描述到全面的视频理解) | [UI-TARS](#ui-tars-pioneering-automated-gui-interaction-with-native-agents) | [VideoChat-Flash](#videochat-flash-hierarchical-compression-for-long-context-video-modeling) | [VideoLLaMA 3](#videollama-3-frontier-multimodal-foundation-models-for-image-and-video-understanding)| [Llama 3.2-Vision](#llama-32-vision-enhanced-multimodal-capability-built-on-llama-3) | [SmolVLM](#smolvlm-小型高效且开源视觉语言模型) | [IDEFICS](#idefics) | [IDEFICS2](#idefics2) | [IDEFICS3-8B](#idefics3-8b-构建和更好地理解视觉语言模型) | [InternLM-XComposer2](#internlm-xcomposer2-掌握自由形式文本图像合成和视觉语言大模型理解) | [InternLM-XComposer2-4KHD](#internlm-xcomposer2-4khd-a-pioneering-大视觉语言模型处理分辨率从 336 像素到 4k 高清) | [InternLM-XComposer-2.5](#internlm-xcomposer-25-a-多功能大视觉语言模型支持长上下文输入和输出) | [InternVL 2.5](#internvl-25-扩展开源多模式模型的性能边界，具有模型数据和测试时间缩放) | [DeepSeek-VL](#deepseek-vl-走向真实世界视觉语言理解) | [DeepSeek-VL2](#deepseek-vl2-mixture-of-experts-vision-language-models-for-advanced-multimodal-understanding) | [MANTIS](#mantis-mastering-multi-image-understanding-through-interleaved-instruction-tuning) | [Qwen-VL](#qwen-vl-a-versatile-vision-language-model-for-understanding-localization-text-reading-and-beyond) | [Qwen2-VL](#qwen2-vl-a-强大的开源视觉语言模型用于图像和视频理解) | [Qwen2.5-VL]（qwen 系列中的#qwen25-vl-增强视觉语言功能）| [moondream1](#moondream1-and-moondream2) | [moondream2](#moondream1-and-moondream2) | [Moondream-next](#moondream-next-紧凑视觉语言模型，具有增强功能) | [SPHINX-X](#sphinx-x-多模态大语言模型系列的缩放数据和参数) | [BLIP](#blip-bootstrapping-语言-图像-预训练) | [BLIP-2](#blip-2-bootstrapping-language-image-pre-training-with-frozen-image-encoders-and-large-language-models) | [xGen-MM (BLIP-3)](#xgen-mm-blip-3-用于构建强大且可靠的大型多模式模型的开源框架) | [InstructBLIP](#instructblip-towards-general- Purpose-vision-language-models-with-instruction-tuning)| [KOSMOS-1]（#kosmos-1-语言并非您所需要的所有与语言模型对齐感知）| [KOSMOS-2](#kosmos-2-grounding-multimodal-large-language-models-to-the-world) | [ConvLLaVA](#convllava-hierarchical-backbones-as-visual-encoder-for-large-multimodal-models)| [Parrot](#parrot-多语言-视觉-指令-调整) | [OMG-LLaVA](#omg-llava-桥接-图像级-对象级-像素级-推理-和理解) | [EVLM](#evlm-an-efficient-vision-la

## 工具

|工具|描述 |
|------|-------------|
| [双视图](https://dualview.ai) |用于 VLM 输出、图像、视频和 AI 提示的免费并排比较工具 |

## 架构

## **LLaVA：大型语言和视觉助手 - 视觉指令调整**

LLaVA 使用简单的线性层将预训练语言模型 (Vicuna) 与视觉编码器 (CLIP) 无缝集成，创建一个能够有效处理和理解语言图像指令的强大架构。

[![arXiv](https://img.shields.io/badge/arXiv-2304.08485-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2304.08485) [![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/haotian-liu/LLaVA) [![Gradio](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://llava.hliu.cc/)  
刘浩天、李春元、吴庆阳、李龙在
<p align="center">
<img src="https://github.com/gokayfem/Awesome-VLM-Architectures/assets/88277926/722f0fbb-ea52-4a8a-ab1e-bec45ca7d04f" />
</p>
<详情>
<summary>ℹ️<i>更多信息</i></summary>
  
**LLaVA**：LLaVA 架构的核心是预训练语言模型与视觉模型的融合，专门设计用于有效处理和理解语言图像指令数据。这种集成使 LLaVA 能够利用两种模型的独特优势，利用 CLIP 视觉编码器进行强大的图像特征提取，并利用 Vicuna 语言模型进行复杂的语言指令处理。该架构的一个值得注意的特点是使用**简单的线性层**将图像特征桥接到词嵌入空间，从而促进视觉和语言表示之间的无缝对齐。 LLaVA 的训练方法被精心构建为两阶段指令调整程序。最初，模型进行预训练，重点关注特征对齐，利用仔细过滤的数据集将图像特征与 LLM 词嵌入同步。随后，该模型针对多模式聊天机器人功能和科学 QA 等定制任务进行端到端微调，目的是提高其遵循指令的能力。这种复杂的训练方案的基础是使用通过 GPT-4 生成的多模式指令跟踪数据，将图像文本对转换为有利于指令跟踪任务的格式。文本和图像数据的对齐是通过**可训练的投影矩阵**实现的，将视觉特征转换为统一维度空间内的语言嵌入标记，从而增强模型对视觉和文本进行内聚编码的能力。用于LLaVA训练和评估的数据集经过战略性选择，以增强其多模态能力。经过过滤的 CC3M 数据集是预训练、对齐视觉和语言特征的基础，而使用 GPT-4 生成的 LLaVA-Instruct-158K 数据集对于在不同的多模态任务上微调模型至关重要。此外，ScienceQA 数据集在评估 LLaVA 在多模态推理任务中的熟练程度方面发挥着关键作用，展示了该模型的全面训练及其显着推进多模态交互和理解领域的潜力。
</详情>

## **LLaVA 1.5：通过视觉指令调整改进基线**

LLaVA 1.5 通过用更强大的多层感知器 (MLP) 替换其初始线性投影来增强其多模态理解，从而能够更深入地集成来自 CLIP-ViT-L-336px 的视觉特征和语言数据。

[![arXiv](https://img.shields.io/badge/arXiv-2310.03744-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2310.03744)  
刘昊天、李春元、李宇恒、李永载
<p align="center">
<img src="https://github.com/gokayfem/Awesome-VLM-Architectures/assets/88277926/c7112b75-3b86-48a2-9c0f-f1dc1dc6ee06" />
</p>
<详情>
<summary>ℹ️<i>更多信息</i></summary>
    
**LLaVA 1.5**：此迭代引入了一种精致的架构，其中包含 CLIP-ViT-L-336px 视觉编码器以及**多层感知器 (MLP) 投影层**。这种组合不仅提高了模型的数据效率，还提高了其在各种基准测试中的性能，展示了多模式理解的飞跃。该架构的核心组件，即用于视觉编码的 CLIP-ViT-L 和用于视觉语言跨模态连接的 MLP，协同工作，增强模型集成和解释视觉和语言输入的能力。LLaVA 1.5 中对训练方法进行了优化，利用两阶段方法，强调高效的特征对齐和针对专为学术任务定制的 VQA 数据进行微调，在 11 个基准上实现前所未有的性能。该论文强调了向更复杂的多模态对齐技术的转变，**用更强大的**MLP视觉语言连接器**取代了原始的线性投影**。这一战略改进促进了视觉和语言数据更深入、更细致的整合。此外，采用基于MLP的视觉语言连接器进行对齐融合方法进一步增强了模型有效融合视觉和文本表示的能力，确保嵌入空间中更紧密的对齐。VQA-v2、GQA和其他面向学术任务的VQA数据集等数据集的利用，丰富了OCR和区域级感知数据，强调了模型增强的视觉理解和推理能力。这些数据集在提升 LLaVA 1.5 的性能方面发挥着至关重要的作用，使其能够利用面向学术任务的数据设定新标准。通过这些进步，LLaVA 1.5 不仅突破了多模态学习的界限，还为该领域的未来研究树立了新的基准。
</详情>

## **LLaVA 1.6：LLaVA-NeXT 改进了推理、OCR 和世界知识**

LLaVA-NeXT 在 LLaVA-1.5 的基础上取得了进步，融合了高分辨率图像处理、增强视觉推理和 OCR 功能，同时通过其前身的知识转移和完善的培训过程保持数据高效设计。

[![GitHub](https://badges.aleen42.com/src/github.svg)](https://llava-vl.github.io/blog/2024-01-30-llava-next/)  
刘浩天、李春元、李宇恒、李波、张远汉、沉盛、李勇杰
<p align="center">
<img src="https://github.com/gokayfem/Awesome-VLM-Architectures/assets/88277926/032ef144-ec10-41da-80a1-2cecd66c86ee" />
</p>  
<详情>
<summary>ℹ️<i>更多信息</i></summary>
    
**LLaVA-NeXT**：代表着在 LLaVA-1.5 奠定的基础上，具有视觉功能的大型语言模型的发展向前迈出了重要一步。该模型引入了多项增强功能，旨在提高图像分辨率、视觉推理、光学字符识别 (OCR) 和世界知识的整合，同时保留其前身的简约和数据高效设计。 LLaVA-NeXT 的架构针对高性能进行了优化，支持高达 672x672、336x1344 和 1344x336 像素的输入图像分辨率。这一改进促进了更详细的视觉感知，再加上增强的视觉指令调整数据混合，显着增强了模型的推理和 OCR 功能。此外，LLaVA-NeXT 通过使用 SGLang 实现高效部署，这一功能强调了其设计对性能和数据效率的关注。训练 LLaVA-NeXT 需要不到 100 万个视觉指令调整样本，利用 LLaVA-1.5 的**预训练连接器**来实现高效的知识传输。训练过程非常迅速，利用 32 个 A100 GPU，大约在一天内完成，这证明了该模型的高效设计和部署策略。 LLaVA-NeXT 中的对齐技术尤其值得注意，它利用高分辨率图像和高质量数据混合来增强模型在视觉对话和指令遵循方面的能力。该模型使用动态高分辨率技术（称为“AnyRes”），可以有效处理不同分辨率的图像，提高模型的整体视觉理解能力。训练 LLaVA-NeXT 时使用的数据集（包括 LAION-GPT-V、ShareGPT-4V、DocVQA、SynDog-EN、ChartQA、DVQA 和 AI2D）均经过精心挑选，以增强模型的视觉推理、OCR 功能和理解能力图表和图表。这一战略选择旨在提高模型在各种多模式任务中的性能，强调其处理和理解复杂视觉信息的能力增强。通过这些改进，LLaVA-NeXT 为语言和视觉交叉点的模型树立了新的基准，在视觉推理、OCR 以及多模态背景下的世界知识应用方面提供了前所未有的功能。
</详情>

## **PaliGemma：多功能且可转移的 3B 视觉语言模型**

PaliGemma 是一个紧凑的开源视觉语言模型，旨在轻松转移到各种任务。它将强大的 SigLIP 图像编码器与 Gemma-2B 语言模型相结合，在 40 多种不同的任务上实现了强大的性能，包括标准 VLM 基准、遥感和分割。 PaliGemma 使用多阶段方法进行预训练，重点是最大化学习信号的密度并提供具有不同图像分辨率的不同检查点。这种多功能的基础模型可以轻松地针对特定任务进行微调，并且可以作为研究人员和从业者探索 VLM 功能的宝贵工具。

[![arXiv](https://img.shields.io/badge/arXiv-2407.07726-b31b1b.svg?style=flat-square)](https://arxiv.org/pdf/2407.07726) [![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/google-research/big_vision/blob/main/big_vision/configs/proj/paligemma/README.md) [![HuggingFace](https://img.shields.io/badge/🤗-Open%20In%20Spaces-blue.svg)](https://huggingface.co/spaces/big-vision/paligemma)  
卢卡斯·拜尔、安德烈亚斯·施泰纳、安德烈·苏萨诺·平托、亚历山大·科列斯尼科夫、小王、丹尼尔·萨尔茨、马克西姆·诺伊曼、易卜拉欣·阿卜杜尔莫辛、迈克尔·察南、埃马努埃莱·布利亚雷洛、托马斯·翁特蒂纳、丹尼尔·凯瑟斯、斯坎达·科普拉、刘芳宇、亚当·格瑞克纳、阿列克谢·格里森科、尼尔·霍尔斯比、马诺·库马尔、Keran Rong、 Julian Eisenschlos、Rishabh Kabra、Matthias Bauer、Matko Bošnjak、Xi Chen、Matthias Minderer、Paul Voigtlaender、Ioana Bica、Ivana Balazevic、Joan Puigcerver、Pinelopi Papalampidi、Olivier Henaff、Xi Xiong、Radu Soricut、Jeremiah Harmsen、翟晓华

<p align="center">
<img src="https://github.com/user-attachments/assets/186371d0-6861-4b68-b32e-fee77cc75ef2" />
</p>

<详情>
<summary>ℹ️<i>更多信息</i></summary>

PaliGemma 是一个高度通用且可转移的 30 亿参数视觉语言模型 (VLM)，经过精心设计，可广泛应用于各种视觉语言任务。其基础在于两个强大组件的集成：SigLIP-So400m 视觉编码器（尽管尺寸紧凑，但仍以其卓越的性能而闻名）和 Gemma-2B 语言模型（Gemma 系列中的预训练自回归解码器模型）。这种组合使 PaliGemma 能够有效地处理和理解视觉和文本信息，使其擅长处理从图像字幕和视觉问答到遥感和分割等更专业的任务。 PaliGemma 的架构精简且高效。它使用简单的线性投影将 SigLIP 编码器提取的视觉特征与 Gemma 语言模型的词汇标记对齐，从而实现两种模式的无缝融合。 PaliGemma 培训的一个关键方面是强调“学习信号密度”，优先考虑广泛的技能和知识，而不是实现高零样本性能。这种方法涉及多阶段预训练过程，首先使用公开可用的检查点对各个组件进行单模态预训练，然后对大规模视觉语言任务的多种混合进行广泛的多模态预训练。值得注意的是，PaliGemma 偏离了在预训练期间冻结图像编码器的常见做法，使其能够从字幕等复杂任务中学习空间和关系理解。为了进一步增强其功能，PaliGemma 经历了分辨率提高阶段，在更高分辨率的图像上进行训练，使其能够处理受益于更精细视觉细节的任务。这种多阶段预训练过程会产生一系列具有不同图像分辨率（224px、448px 和 896px）的三个 PaliGemma 检查点，每个检查点都经过广泛的视觉知识的预训练。这些检查点作为强大的基础模型，可以轻松转移到特定的下游任务。 PaliGemma 的可迁移性通过其在 30 多个学术基准测试中的出色表现得到了证明，其中包括涉及多个图像的基准测试，例如 NLVR2 和短视频理解任务。该模型能够以最少的微调快速适应新任务，凸显了其多功能性，并使其成为探索和提升 VLM 功能的宝贵工具。此外，该模型的开源性质及其简单的架构和训练方法，鼓励 VLM 社区内进行进一步的研究和实验，推动更强大、更通用的多模式人工智能系统的发展。
</详情>

## **PaliGemma 2：用于传输的多功能 VLM 系列**

PaliGemma 2 是基于 Gemma 2 语言模型并结合 SigLIP-So400m 视觉编码器的开放视觉语言模型 (VLM) 的升级系列。它提供三种尺寸（3B、10B、28B）和三种分辨率（224px²、448px²、896px²）的模型，并经过多个阶段的培训以实现广泛的知识转移。  PaliGemma 2 在各种任务上都取得了最先进的结果，包括与 OCR 相关的挑战，如表格/分子/乐谱识别和长格式字幕。

[![arXiv](https://img.shields.io/badge/arXiv-2412.03555-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2412.03555)
[![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/google-research/big_vision/blob/main/big_vision/configs/proj/paligemma/README.md)
[![HuggingFace](https://img.shields.io/badge/🤗-Open%20In%20Spaces-blue.svg)](https://huggingface.co/collections/google/paligemma-2-release-67500e1e1dbfdd4dee27ba48)  
Andreas Steiner、André Susano Pinto、Michael Tschannen、Daniel Keysers、小王、Yonatan Bitton、Alexey Gritsenko、Matthias Minderer、Anthony Sherbondy、龙尚邦、秦思扬、Reeve Ingle、Emanuele Bugliarello、Sahar Kazemzadeh、Thomas Mesnard、Ibrahim Alabdulmohsin、Lucas Beyer 和翟晓华

<p align="center">
<img src="https://github.com/user-attachments/assets/4ce402be-d644-4143-a57c-9e7f4d811d95" width="600"/>
</p>

<详情>
<summary>ℹ️<i>更多信息</i></summary>

PaliGemma 2 紧密遵循其前身 PaliGemma 的架构。  它使用预先训练的 SigLIP-So400m 视觉编码器。该编码器的嵌入使用*线性投影*映射到 Gemma 2 语言模型的输入空间。  然后将组合的视觉和文本嵌入输入 Gemma 2 模型，该模型以自回归方式生成输出。  该模型具有三种尺寸变体（Gemma 2 组件中的 2B、9B 和 27B 参数，对应于 3B、10B 和 28B 总参数），并在三种分辨率（224x224、448x448 和 896x896 像素）下进行训练。  这样可以分析模型大小、分辨率和传输性能之间的相互作用。输入图像与输入文本标记连接起来，Gemma 2 自回归地用答案补全这个前缀。 PaliGemma 2 的训练遵循三阶段方法，类似于原始的 PaliGemma： **阶段 1：** 将预训练的 SigLIP-So400m 和 Gemma 2 检查点组合在一起，并在 10 亿个示例的多模式任务混合物上联合训练。图像分辨率为 224px²。 **第 2 阶段：** 继续以 448px² 分辨率训练 5000 万个示例，然后以 896px² 训练 1000 万个示例。受益于更高分辨率的任务的权重会增加。 **第 3 阶段：** 微调目标任务上第 1 或第 2 阶段的检查点。训练数据混合包括字幕、接地字幕、OCR、视觉问答 (VQA)、检测和实例分割。值得注意的是，训练数据严重依赖于公开可用的专业模型中的“机器生成的标签”，“避免使用大型商业 VLM”来生成标签。 **Gemma 2 语言模型：** 核心升级是使用更新且功能更强大的 Gemma 2 系列语言模型，取代 PaliGemma 中原始的 Gemma 模型。  **分辨率和模型大小缩放：** PaliGemma 2 系统地探讨了图像分辨率和语言模型大小对传输性能的影响。  这是一个关键贡献，因为大多数先前的工作并没有通过一致的训练方案来共同研究这些因素。
</详情>

## **AIMv2：大视觉编码器的多模态自回归预训练**

AIMv2 是一个通用视觉编码器系列，可自回归生成图像块和文本标记，在多模态图像理解方面实现最先进的性能，并在定位、接地和分类等视觉基准测试中取得出色的结果，展示了可扩展性和效率。

[![arXiv](https://img.shields.io/badge/arXiv-2411.14402-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2411.14402)
[![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/apple/ml-aim)
[![HuggingFace](https://img.shields.io/badge/🤗-Open%20In%20Spaces-blue.svg)](https://huggingface.co/apple/aimv2-large-patch14-224)  
恩里科·菲尼、穆斯塔法·舒克、大卫·哈尔迪曼、赛·艾塔拉茹、亚历山大·托舍夫、马辛·艾希纳、莫因·纳比、李秀君、菲利普·杜夫特、米哈尔·克莱因、维克托·G·图里西·达·科斯塔、路易斯·贝蒂恩、甘哲、阿拉丁·埃尔-努比

<p align="center">
<img src="https://github.com/user-attachments/assets/c89a0be9-8743-4800-8d3c-ec51a4c99f4d" width="600"/> <!-- Replace with the actual URL -->
</p>

<详情>
<summary>ℹ️<i>更多信息</i></summary>


AIMv2（自回归图像模型 v2）引入了一种用于大规模视觉编码器的新颖预训练方法，该方法将自回归预训练扩展到包含图像和文本的多模态设置。核心架构将 Vision Transformer (ViT) 编码器与因果多模态解码器配对。视觉编码器处理原始图像块（使用前缀注意），而多模态解码器自回归生成图像块（使用像素 MSE 损失）和文本标记（使用交叉熵损失）。至关重要的是，图像补丁和文本标记被视为单个统一的序列。这使得模型能够学习视觉和文本信息的联合表示。图像始终添加到文本序列的开头。培训流程精简、高效。它类似于 AIM 和 LLM，仅依赖于自回归目标。没有专门的批次间通信方法或需要过大的批次大小。这与对比方法（例如 CLIP、SigLIP）形成鲜明对比，后者通常在训练和扩展方面更具挑战性。训练数据由公开可用的数据集（DFN-2B、COYO）和专有数据集（HQITP）组成，包括替代文本和合成标题。 AIMv2 表现出强大的扩展特性，通过增加数据或模型参数不断提高性能。该模型系列包括 3 亿至 30 亿个参数的变体。一个关键的优化是在视觉编码器中使用前缀注意力，无需微调即可在推理过程中实现双向注意力。其他架构选择包括 SwiGLU 和 RMSNorm 的结合，其灵感来自于最近在语言建模方面取得的成功。 AIMv2 在各种任务中表现出色。与最先进的视觉语言预训练方法相比，它在多模式理解基准上表现良好。它还在开放词汇目标检测和指代表达理解方面表现出强大的性能，超越了 DINOv2。此外，它还通过冷冻树干实现了令人印象深刻的识别性能。该模型支持原生图像分辨率并适应零样本识别，展示了其灵活性。包括高分辨率适应在内的训练后策略进一步增强了模型的能力。消融研究证明了联合图像和文本建模、验证设计选择并探索缩放特征的重要性。
</详情>

## **Apollo：大型多模态模型中视频理解的探索**


Apollo 是最先进的大型多模态模型 (LMM) 系列，专为视频理解而设计，通过利用“缩放一致性”并探索采样、架构、数据组合和训练计划等视频特定方面，在不同模型大小上实现卓越性能。 7B 模型是该技术的开端，Apollo-3B 的性能优于大多数现有的 7B 模型。

[![arXiv](https://img.shields.io/badge/arXiv-2412.10360-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2412.10360)
[![GitHub](https://badges.aleen42.com/src/github.svg)](https://apollo-lmms.github.io/)  
Orr Zohar、王晓涵、Yann Dubois、Nikhil Mehta、肖童、Philippe Hansen-Estruch、于立成、王晓芳、Felix Juuefei-Xu、Ning Chang、Serena Yeung-Levy、Xide Xia

<p align="center">
<img src="https://github.com/user-attachments/assets/9222064a-d7a3-4e6b-a14d-bc9a5c679450" width="600" /> 
</p>

<详情>
<summary>ℹ️<i>更多信息</i></summary>


Apollo 利用具有 1.5B、3B 和 7B 参数的 Qwen2.5 系列大型语言模型 (LLM)。关键的架构创新是 SigLIP-SO400M 图像编码器和 InternVideo2 视频编码器的组合。两个编码器的特征在输入到感知器重采样器之前会按通道进行插值和连接，每帧输出 32 个令牌。根据经验，这种组合优于其他编码器选择。该模型采用 3 阶段训练方法。重要的是，本文引入了“缩放一致性”的概念，证明在较小模型和数据集（达到临界大小）上做出的设计决策可以有效地转移到更大的模型。这允许更有效的实验。该论文还提倡在训练期间进行每秒帧数（fps）采样，而不是统一帧采样，并展示了其优越性。最佳令牌数量是每帧 8-32 个。它还包括一个精心策划的基准测试 ApolloBench，与现有基准测试相比，该基准测试将评估时间缩短了 41 倍，同时保持高度相关性并专注于时间推理和感知。该探索还包括令牌重采样，表明感知器重采样具有良好的性能。还讨论了令牌集成：在从不同帧派生的视频令牌之间添加令牌（文本、学习等）
或剪辑足以实现有效的令牌集成。还讨论了训练阶段，得出的结论是，逐步解冻不同阶段的不同组件会带来卓越的模型训练动态。最后，讨论了视频编码器的训练。该论文的结论是，仅对视频数据进行微调视频编码器可以进一步提高整体性能，
特别是在推理和特定领域的任务上。还研究了数据构成。结论是数据混合很重要，包括适量的文本数据并保持
轻微的视频混合可带来最佳性能。

</详情>

## **ARIA：开放的多模式本地专家混合模型**

ARIA 是一种开源、多模式原生专家混合 (MoE) 模型，旨在无缝集成和理解文本、代码、图像和视频等多种模式，从而实现同类产品中最先进的性能。它具有用于高效参数利用的细粒度 MoE 解码器、轻量级视觉编码器以及构建语言理解、多模态理解、长上下文处理和指令跟踪功能的 4 阶段训练管道。

[![arXiv](https://img.shields.io/badge/arXiv-2410.05993-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2410.05993)
[![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/rhymes-ai/Aria)
[![HuggingFace](https://img.shields.io/badge/🤗-Open%20In%20Spaces-blue.svg)](https://huggingface.co/blog/RhymesAI/aria)  
李东旭、刘玉栋、吴浩宁、王悦、沉志奇、曲博文、牛鑫耀、周范、黄承恩、李彦鹏、朱崇彦、任晓怡、李超、叶一凡、刘鹏、张立欢、严汉舒、王国银、陈蓓、李俊楠

<p align="center">
<img src="https://github.com/user-attachments/assets/efe4a7ba-756a-4da8-b261-5a0093f28b03" width="600"/>
</p>

<详情>
<summary>ℹ️<i>更多信息</i></summary>

ARIA 的架构以细粒度专家混合 (MoE) 解码器为中心，它比传统的密集解码器更高效。  这种 MoE 方法在总共 24.9B 个参数中激活每个文本标记 3.5B 个参数和每个视觉标记 3.9B 个参数。该模型在每个 MoE 层使用 66 名专家，其中 2 名专家在所有输入中共享常识知识，并由路由器为每个令牌激活 6 名专家。视觉编码器是一个轻量级（438M参数）Vision Transformer（ViT）与投影模块相结合。  ViT 以各种分辨率（中、高和超高）处理图像，并保留纵横比。投影模块使用交叉注意力和 FFN 层将图像嵌入转换为视觉标记，然后由 MoE 将其与文本标记集成。 ARIA的训练采用4阶段管道：（1）语言预训练（6.4T文本标记，8K上下文窗口）； （2）多模态预训练（400B多模态标记，包括交错的图像文本、合成图像标题、文档转录和QA、视频标题和QA）； (3) 多模态长上下文预训练（将上下文扩展到64K token）； (4) 多模式后训练（后面带有 20B 令牌的指令）。  数据管理过程非常严格，结合了重复数据删除、质量过滤和数据集群等技术。训练基础设施使用专家并行性和 ZeRO-1 数据并行性的组合来避免管道并行性，这有助于在不需要张量并行性的情况下实现高效训练。负载平衡损失和 z 损失用于稳定训练。
该论文表明，尽管有模态通用专家，但 ARIA 在预训练期间自然会发展专家专业化。  对专家激活的分析显示了多个层面上明显的视觉专业化，特别是对于图像、视频和 PDF 内容。  ARIA 在处理长上下文多模态数据方面也表现出了出色的性能，超越了其他开放模型，并在长视频和文档理解等任务中与专有模型展开了有利的竞争。
</详情>



## **EVE：推出无编码器视觉语言模型**

EVE 是一种无编码器的视觉语言模型 (VLM)，可在统一的仅解码器架构中直接处理图像和文本，无需单独的视觉编码器。它仅使用 3500 万个可公开访问的数据，在多个视觉语言基准测试中实现了与基于编码器的相似大小的 VLM 的竞争性能，并且该模型可以有效地处理具有任意长宽比的高分辨率图像。

[![arXiv](https://img.shields.io/badge/arXiv-2406.11832-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2406.11832)
[![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/baaivision/EVE)
[![HuggingFace](https://img.shields.io/badge/🤗-Open%20In%20Spaces-blue.svg)](https://huggingface.co/BAAI/EVE-7B-HD-v1.0)  
刁海文、崔玉峰、李晓彤、王跃泽、路虎川、王新龙
<p align="center">
<img src="https://github.com/user-attachments/assets/c10e987d-9e11-41d7-968c-617b60d3b0bd" width="600"/>
</p>

<详情>
<summary>ℹ️<i>更多信息</i></summary>

**EVE（无编码器视觉语言模型）**：该模型的独特之处在于完全删除了 VLM 中常见的视觉编码器组件。  相反，它直接将视觉信息集成到仅解码器的架构中（基于 Vicuna-7B）。  这是通过直接处理图像补丁的新颖的**补丁嵌入层 (PEL)** 与**补丁对齐层 (PAL)** 相结合来实现的，**补丁对齐层 (PAL)** 有助于从预先训练的视觉编码器 (CLIP-ViT-L/14) 进行学习，而无需更新编码器本身。  至关重要的是，EVE 在推理过程中“不”使用传统的图像编码器。 **PEL** 使用卷积层和平均池化从输入图像创建 2D 特征图。  然后，它在有限的感受野内采用交叉注意力（CA1）来增强这些特征。特殊的“<CLS>”标记提供了每个补丁特征的整体视图，并且在每行补丁特征之后插入可学习的换行符“<SPL>”来表示2D结构。 **PAL** 将 EVE 的补丁功能与来自冻结的、预先训练的视觉编码器 (CLIP-ViT-L/14) 的功能对齐。这是分层完成的，聚合解码器多个层的特征并使用逐层交叉注意（CA3）机制。  EVE 特征和视觉编码器特征之间的均方误差 (MSE) 损失促进了对齐。  视觉编码器的这种“隐式”监督提高了视觉理解。  重要的是，PAL“仅”在训练过程中使用，而不是推理过程中使用。培训过程分三个阶段进行： **LLM 指导的预训练：** 仅训练 PEL 和 PAL，将视觉特征与冻结的 LLM (Vicuna-7B) 对齐。  此阶段使用总训练数据的子集 (16M)。 **生成预训练：** 使用完整的 33M 数据集对整个模型（包括 LLM）进行训练。同时使用文本预测（交叉熵损失）和视觉对齐（MSE 损失）。 **监督微调：** 整个模型在遵循指令的数据集（LLaVA-mix-665K 等）上进行微调。让 EVE 在没有视觉编码器的情况下也能正常工作的关键创新是： **以 LLM 为中心的预对齐：** 第 1 阶段对于防止模型崩溃和加速收敛至关重要。  *在*全面培训法学硕士之前*调整视觉特征至关重要。 **通过额外监督实现视觉识别能力：** PAL 在训练期间提供来自预先训练的视觉编码器的监督，这增强了视觉理解，而在推理过程中不需要编码器。 **灵活的输入处理：** 该架构自然地处理任意纵横比和分辨率的图像，无需调整大小、填充或分区。不依赖视觉编码器：图像直接输入到LLM模型中。
EVE 使用由 3300 万个公开可用的图像文本对组成的精选数据集进行预训练，并带有由 Emu2 和 LLaVA-1.5 生成的字幕。监督微调利用 LLaVA-mix-665K、AI2D、DocVQA 等数据集。
</详情>

好的，让我们分解所提供的有关 EVEv2 的论文中的信息，并创建与您的示例类似的特征提取。

## **EVEv2：改进无编码器视觉语言模型的基线**

EVEv2 代表了无编码器视觉语言模型 (VLM) 的重大进步，通过引入“分而治之”架构解决了以前方法的局限性，该架构可最大限度地提高扩展效率、减少模态间干扰，并通过卓越的数据效率实现强大的性能。

[![arXiv](https://img.shields.io/badge/arXiv-2406.11832-b31b1b.svg?style=flat-square)](https://github.com/baaivision/EVE/blob/main/EVEv2/images/EVEv2.0.pdf)
[![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/baaivision/EVE/blob/main/EVEv2/README.md)
[![HuggingFace](https://img.shields.io/badge/🤗-Open%20In%20Spaces-blue.svg)](https://huggingface.co/BAAI/EVE-7B-HD-v2.0)  
刁海文、李晓彤、崔玉峰、王悦泽、邓浩歌、潘婷、王文轩、路虎川、王新龙

<p align="center">
<img src="https://github.com/user-attachments/assets/23a33fe6-d4c5-4a9d-b45f-f5612f7848a5" width="600"/>  
</p>

<详情>
<summary>ℹ️<i>更多信息</i></summary>

EVEv2 不同于传统的基于编码器的 VLM 方法。  它不依赖预先训练的视觉编码器（如 CLIP），而是直接在仅解码器的大型语言模型 (LLM) 内构建视觉感知。  主要架构特征包括： **分而治之：** 这是核心创新。  EVEv2 没有在整个 LLM 中混合视觉和文本信息，而是引入了*特定于模态的*组件。  这意味着单独的注意力矩阵（查询、键、值）、层归一化层以及视觉和文本标记的前馈网络。  这减少了干扰并允许更有效的学习。  它是一个完全稀疏的、仅解码器的架构。 **补丁嵌入层：**从头开始*学习极简补丁嵌入层。  这避免了预训练视觉编码器的归纳偏差。  它使用两个卷积层（Conv1 和 Conv2）来处理图像块。 **无损编码：** 与一些使用离散标记化（可能丢失信息）的无编码器模型不同，EVEv2 旨在对视觉信息进行无损编码。 **法学硕士适应：** 该架构旨在无缝适应现有的法学硕士。  论文用Vicuna-7B和Qwen2-7B进行了实验。 **多阶段训练：** 使用四阶段训练过程： **LLM 引导的预对齐：** 使用重新字幕网络数据 (EVE-recap-10M) 仅训练补丁嵌入层。  LLM 被冻结。这在视觉和文本表示之间建立了基本的一致性。 **视觉感知学习：** LLM 中的视觉层使用逐渐增大的数据集和图像分辨率进行训练。  LLM的权重仍然被冻结。 **视觉-文本完全对齐：**整个网络更新。 **监督微调（SFT）：**整个模型在问答和指令跟踪数据集上进行微调。 **DenseFusion++：** 引入了一种新的高效字幕引擎来生成高质量的图像文本对以进行训练。  这对于从头开始建立强大的视觉感知至关重要。它利用了多名视觉专家。 **数据效率：** 研究的一个重点是证明，由于其高效的架构，EVEv2 可以使用比基于编码器的同类模型“更少”的数据实现强大的性能。
</详情>




## **Janus-Pro：通过数据和模型扩展实现统一多模式理解和生成**

Janus-Pro 通过优化训练策略、扩展训练数据和扩大模型大小，在原始 Janus 模型的基础上进行了显着改进，从而增强了多模态理解、文本到图像指令跟踪和生成稳定性。

[![arXiv](https://img.shields.io/badge/arXiv-2501.17811-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2501.17811)
[![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/deepseek-ai/Janus)
[![HuggingFace](https://img.shields.io/badge/🤗-Open%20In%20Spaces-blue.svg)](https://huggingface.co/deepseek-ai/Janus-Pro-7B)  
陈小康、吴志宇、刘兴超、潘子正、刘文、谢振达、余兴凯、阮冲

<p align="center">
<img src="https://github.com/user-attachments/assets/657b0f2a-7a0e-4aed-a214-a33485990790" width="600"/>
</p>

<详情>
<summary>ℹ️<i>更多信息</i></summary>

Janus-Pro 保留了 Janus 的核心架构，它将视觉编码解耦以实现多模态理解和生成。  它使用统一的自回归变压器，但使用单独的编码器来理解（SigLIP）和生成（VQ tokenizer）。理解编码器提取语义特征，通过“理解适配器”将其扁平化并映射到法学硕士的输入空间。  生成编码器将图像转换为离散 ID，并通过“生成适配器”进行扁平化和映射。这些特征序列被连接起来并馈送到法学硕士。  该模型包括一个内置预测头（来自法学硕士）和一个用于图像生成的随机初始化预测头。 Janus-Pro 的主要改进在于三个方面： **优化训练策略：** Janus-Pro 使用三阶段训练过程。 **第一阶段：** 重点训练适配器和图像头，在 ImageNet 上进行更长时间的训练，改进参数初始化。 **第二阶段：**统一预训练，更新所有组件*除了*理解和生成编码器。  至关重要的是，它从这个阶段“删除”了 ImageNet 数据，并仅使用“正常”文本到图像数据，从而提高了效率。 **第三阶段：**监督微调，进一步更新理解编码器。数据比例（多模态：文本：文本到图像）从 7:3:10 调整为 5:1:4，在不牺牲生成的情况下提高多模态理解。 **数据扩展：** Janus-Pro 显着扩展了训练数据。 **多模态理解：** 从 DeepSeek-VL2 等来源添加约 9000 万个样本，包括图像标题 (YFCC)、表格/图表/文档理解 (Docmatix)、MEME 理解和中文对话数据。 **视觉生成：** 添加约 7200 万个“合成”美学数据样本，在统一预训练期间以 1:1 的比例平衡真实数据和合成数据。这提高了生成稳定性和美学质量。 **模型缩放：** Janus-Pro 从 1.5B 扩展到 7B LLM 参数 (DeepSeek-LLM)。  这显着提高了理解和生成的收敛速度。训练使用序列长度 4096、SigLIP-Large-Patch16-384 进行理解，并使用码本为 16,384 的 VQ 分词器进行生成。适配器是两层 MLP。培训是使用分布式培训框架 HAI-LLM 进行的。评估是在 GQA、MME、SEED、MMB、MM-Vet、MMMU（用于理解）和 GenEval、DPG-Bench（用于生成）等基准上进行的。  Janus-Pro 在统一的多模态模型中取得了最先进的结果，展示了多模态理解和文本到图像生成方面的显着改进。
</详情>

## **LLaVA-CoT：让视觉语言模型逐步推理**

LLaVA-CoT 是一种新颖的视觉语言模型 (VLM)，旨在执行自主、多阶段推理，使其能够通过独立参与总结、视觉解释、逻辑推理和结论生成的连续阶段来处理复杂的视觉问答任务。

[![arXiv](https://img.shields.io/badge/arXiv-2411.10440-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2411.10440)
[![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/PKU-YuanGroup/LLaVA-CoT)
[![HuggingFace](https://img.shields.io/badge/🤗-Open%20In%20Spaces-blue.svg)](https://huggingface.co/Xkev/Llama-3.2V-11B-cot)  
徐国伟、金鹏、李浩、宋一兵、孙立超、袁莉

<p align="center">
<img src="https://github.com/user-attachments/assets/1a5e32f0-4ffc-4514-8401-25777c2fac10" width="600"/>
</p>

<详情>
<summary>ℹ️<i>更多信息</i></summary>

LLaVA-CoT 基于 Llama-3.2-Vision 模型，引入了结构化的四阶段推理过程：摘要（简要概述任务）、标题（描述相关图像部分）、推理（详细分析）和结论（提供最终答案）。  每个阶段都标有特定标签（<SUMMARY>、<CAPTION>、<REASONING>、<CONCLUSION>）以保持清晰。与传统的思维链（CoT）提示不同，LLaVA-CoT通过首先组织问题和已知信息，然后进行详细推理，最后得出结论来促进结构化思维。该模型在新编译的 LLaVA-CoT-100k 数据集上进行训练。该数据集集成了来自各种视觉问答源的样本，并提供结构化推理指令。该数据集包含 99k 图像和问题答案对，使用 GPT-4o 提供详细信息。数据收集自一般 VQA 数据集（ShareGPT4V、ChartQA、A-OKVQA、DocVQA、PISC、CLEVR）和科学目标 VQA（AI2D、GeoQA+、ScienceQA、CLEVR-Math）。  该论文还提出了一种新颖的推理时间阶段级波束搜索方法。该方法在推理过程的*每个*阶段生成多个候选结果，选择最好的结果继续，从而提高性能和可扩展性。这与传统的 best-of-N 或句子级集束搜索形成对比。整个模型使用监督微调进行训练。
</详情>

## **LLM2CLIP：强大的语言模型解锁更丰富的视觉表示**

LLM2CLIP 是一种微调方法，它将大型语言模型 (LLM) 与预训练的 CLIP 视觉编码器集成在一起。它利用法学硕士处理和理解长标题、开放世界知识的能力来改进模型。

[![arXiv](https://img.shields.io/badge/arXiv-2411.04997-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2411.04997)
[![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/microsoft/LLM2CLIP)
[![HuggingFace](https://img.shields.io/badge/🤗-Open%20In%20Spaces-blue.svg)](https://huggingface.co/microsoft/LLM2CLIP-EVA02-B-16)  
黄伟全、吴傲奇、杨一凡、罗旭芳、杨雨清、胡亮、戴奇、戴希阳、陈东东、罗冲、邱莉莉

<p align="center">
<img src="https://github.com/user-attachments/assets/44d6952e-98ea-4875-bd9c-0a09a683bcbb" width="600"/>
</p>

<详情>
<summary>ℹ️<i>更多信息</i></summary>

LLM2CLIP 是微调方法。它将 LLM（大型语言模型）集成到已经预训练的 CLIP 视觉编码器中。试图解决的主要问题是： LLM的文本理解能力并没有体现在CLIP模型上。作者强调，由于 LLM 输出特征的可分离性较差，直接将 LLM 合并到 CLIP 中通常会失败。  为了解决这个问题，他们引入了两阶段方法。 **第 1 阶段：字幕对比 (CC) 微调：** LLM（特别是 Llama-3 8B）使用图像字幕数据集 (CC3M) 上的对比学习框架进行微调。这个阶段*不训练自回归能力*，相反，它将因果注意力转变为双向，将其用作编码器。这一阶段的目标是使用有监督的 SimCSE 损失来提高 LLM 输出空间的判别能力，使其更容易区分不同的标题。 **第 2 阶段：CLIP 视觉编码器微调：** 预训练的 CLIP 视觉编码器使用 CC 微调的 LLM 进行微调，现在充当“超级”文本编码器。  法学硕士的梯度在此阶段被“冻结”，以保留其所获得的知识并降低计算成本。  LLM 之后添加可学习的适配器（线性层），以方便与 CLIP 视觉编码器对齐。
在 LLM 微调期间使用字幕到字幕对比框架，而不是典型的图像文本对比损失。  这迫使法学硕士为描述同一图像的不同标题生成不同的表示。它使用监督式 SimCSE。制作模型编码器。在 CLIP 微调期间冻结 LLM 对于效率和保存 LLM 知识至关重要。这些适配器弥补了冻结的 LLM 和 CLIP 视觉编码器之间的差距。该方法的效率出奇的高，只需要少量的开源数据（15M 甚至 3M 的图像文本对），在某些情况下只需要一次训练。它利用 LoRA（低秩适应）进行高效的微调。 LLM2CLIP 可以有效地利用密集字幕（详细的图像描述），这是标准 CLIP 的一个已知限制。使用 ShareCaptioner 修改的 CC-3M（用于 CC 微调）、Wikitext-103 以及用于 CLIP 微调的 CC-3M、CC-12M、YFCC-15M 和 Recaption-1B 的组合。论文表明，在对 LLM 的输出空间进行微调后，使用 LLM 会产生显着的影响，并且它大大提高了下游任务的性能。
</详情>

## **Maya：指令微调的多语言多模式模型**

Maya 是一种开源多模态多语言视觉语言模型 (mVLM)，旨在解决当前 VLM 在处理低资源语言和多样化文化背景方面的局限性，通过创建新的多语言图像文本预训练数据集、执行毒性分析和缓解以及微调以增强文化和语言理解来实现。

[![arXiv](https://img.shields.io/badge/arXiv-2412.07112-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2412.07112)
[![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/nahidalam/maya)
[![HuggingFace](https://img.shields.io/badge/🤗-Open%20In%20Spaces-blue.svg)](https://huggingface.co/maya-multimodal/maya)  
Nahid Alam、Karthik Reddy Kanjula、Bala Krishna S Vegesna、SM Iftekhar Uddin、Drishti Sharma、Abhipsha Das、Shayekh Bin Islam、Surya Guthikonda、Timothy Chung、Anthony Susevski、Ryan Sze-Yin Chan、Roshan Santhosh、Snegha A、Chen Liu、Isha Chaturvedi、Ashvanth.S、Snehanshu穆克吉，阿尔哈姆·费克里·阿吉

<p align="center">
<img src="https://github.com/user-attachments/assets/f413afd9-3eee-4a5e-940a-b148fdf3189b" width="600"/>  <!--  Dummy Image -->
</p>

<详情>
<summary>ℹ️<i>更多信息</i></summary>

**架构：** Maya 基于 LLaVA 1.5 框架构建。  由于 Aya 强大的多语言能力（经过 23 种语言训练），它使用 Aya-23 8B 模型作为其大语言模型 (LLM)。  至关重要的是，它用 SigLIP“取代”了 LLaVA 中使用的 CLIP 视觉编码器。  这是由于 SigLIP 的卓越性能、多语言支持以及处理可变长度图像补丁的能力（允许更灵活的输入大小）。  来自 SigLIP 的视觉特征（“Zv = g(Xv)”）通过可训练的投影矩阵（“W”，具有 GELU 激活的 2 层 MLP）传递，以将它们与 LLM 的嵌入空间对齐，产生视觉特征“Hv”。  该架构对于此类模型来说是相当标准的，它将视觉和文本特征连接起来以输入到法学硕士。训练过程包括两个主要阶段：预训练和微调。 **预训练：** 该模型在新创建的多语言图像文本数据集上进行预训练。  该数据集源自纯英语 LLaVA 预训练数据集（558k 图像文本对），并使用复杂的翻译管道翻译成另外七种语言（中文、法语、西班牙语、俄语、印地语、日语和阿拉伯语）。  该管道使用 Aya 35B 模型、优化的提示工程（使用 BLEU 和 N-gram 分数根据经验确定）以及带有质量检查的批处理方法。至关重要的是，该数据集经过*毒性过滤*。  LLaVAGuard 和 Toxic-BERT 用于识别和删除有毒图像标题对，创建数据集的“无毒”版本（删除 7,531 张有毒图像）。预训练使用 1e-3 的学习率和余弦调度器。预训练期间仅训练投影矩阵。 **微调：** 然后使用 PALO 150K 指令调优数据集（涵盖 10 种语言）对预训练模型进行指令调优。  使用冻结视觉编码器和 LLM 进行全面微调（与 LoRA 不同）。核心对齐技术是可训练的投影矩阵（2 层 MLP），它将 SigLIP 视觉特征映射到 Aya-23 LLM 的嵌入空间。这是一种简单但有效的方法，在许多 VLM 中都很常见。论文“明确”指出，他们在此阶段“没有”使用更复杂的对齐技术，例如门控软注意力（Flamingo）或 Q-Former（BLIP-2），并将这些技术保留到未来的工作中。 **预训练数据集：** 通过翻译和过滤 LLaVA 预训练数据集创建的新多语言数据集。  该数据集是本文的关键贡献。  详细描述了翻译过程和毒性过滤。 **指令调优数据集：** PALO 150K 指令调优数据集。 **评估数据集**：PALO 多语言评估、VizWiz、GQA、ScienceQA、TextVQA、POPE、MMBench、MM-Vet、MME。 **多语言图像文本预训练数据集：** 包含 8 种语言的 558,000 张图像的新数据集。 **毒性分析和缓解：** 对原始 LLaVA 数据集中的毒性进行彻底分析并创建无毒版本。这是一个重要且新颖的方面。 **多语言模型：** 模型 (Maya) 在理解文化和语言细微差别方面表现出改进的性能，特别是与主要使用英语数据训练的模型相比。结果表明，Maya 的性能与类似大小的模型 (LLaVA-7B) 相当或更好，并且在多语言基准测试中通常接近较大模型 (PALO-13B) 的性能。毒性过滤对整体性能的影响很小，这表明去除有毒内容不会丢失有价值的信息。该论文包括定量基准结果和证明模型功能的定性示例。
</详情>

## **MiniMax-01：利用闪电注意力缩放基础模型**

MiniMax-01 是一系列大型基础模型，包括 MiniMax-Text-01 和 MiniMax-VL-01，其性能可与顶级模型（如 GPT-4o 和 Claude-3.5-Sonnet）相媲美，同时提供更长的上下文窗口（最多 400 万个令牌）。  它通过一种新颖的架构实现了这一目标，该架构结合了闪电注意力（一种高效的线性注意力变体）、专家混合（MoE）和优化的训练/推理框架。

[![arXiv](https://img.shields.io/badge/arXiv-2501.08313-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2501.08313)
[![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/MiniMax-AI/MiniMax-01)
[![HuggingFace](https://img.shields.io/badge/🤗-Open%20In%20Spaces-blue.svg)](https://huggingface.co/MiniMaxAI/MiniMax-VL-01)  
MiniMax、李奥年、龚邦伟、博杨、单博吉、刘昶、朱成、张春浩、郭从超、陈大、李东、焦恩伟、李庚新、张国军、孙浩海、董厚泽、朱家岱、庄佳琪、宋佳元、朱金、韩静涛、李景阳、谢俊斌、徐俊浩、严俊杰、张凯顺、肖克成、康可喜、乐韩、王乐阳、于连飞、冯立恒、郑林、柴林波、兴龙、鞠美芝、池明远、张墨智、黄培凯、牛鹏程、李鹏飞、赵鹏宇、杨奇、徐启迪、王切翔、王勤、李秋辉、冷锐涛、史胜民、余淑琪、李思辰、朱松泉、黄涛、梁天润、孙伟高、伟轩孙伟宇成、李文凯、宋向军、苏晓、韩晓东、张新杰、侯新柱、徐敏、邹迅、沉旭阳、宫彦、朱英杰、周一鹏、钟怡然、胡勇毅、范远翔、余悦、杨宇峰、李雨浩、黄雨楠、李云吉、黄云鹏、徐云志、毛雨欣、李泽涵、李泽康、陶泽伟、应泽文、丛朝阳、秦真、范振华、余志航、蒋卓、吴子佳

<详情>
<summary>ℹ️<i>更多信息</i></summary>

**混合注意力：**核心创新是混合注意力机制。  它主要使用“闪电注意力”（TransNormer 线性注意力的 I/O 感知实现）来提高效率。  然而，为了保持强大的检索能力，它策略性地在每七个 Transnormer 块之后插入一个具有 SoftMax 注意力的标准 Transformer 块（具有闪电注意力）。  这是与纯线性注意力模型的一个关键区别，后者经常难以完成检索任务。 **混合专家 (MoE)：** 为了有效扩展模型，MiniMax-01 在前馈层中采用了混合专家 (MoE) 架构。  它拥有 4560 亿个庞大参数，但每个代币仅激活 459 亿个参数，使用 32 位专家和 top-2 路由策略。  这允许较大的模型容量，而不会相应增加每个令牌的计算成本。 **视觉语言模型 (MiniMax-VL-01)：** 视觉语言模型 (MiniMax-VL-01) 基于 MiniMax-Text-01，集成了轻量级视觉转换器 (ViT) 模块。  它使用动态分辨率策略，将输入图像调整为各种尺寸（从 336x336 到 2016x2016），并连接调整大小的补丁和标准缩略图中的特征。  它“不”对视觉特征使用池化或下采样，而是依赖于架构的长上下文功能。展示了大规模线性注意力的可行性，实现了与顶级模型相当的性能，同时显着扩展了上下文窗口。 **长上下文能力：** 支持高达400万个token的上下文输入，在长上下文评估方面表现强劲。 **高效的训练和推理框架：** 引入了几种新颖的算法和工程优化，以有效地处理混合架构、MoE 和长上下文。
**预训练：** 精心策划的语料库，包含学术文献、书籍、网络内容和编程代码。 **视觉语言预训练 (VL-01)：** 大量图像字幕数据集（6.94 亿对）和包含 1 亿张具有细粒度描述的图像的数据集。 **视觉语言指令数据 (VL-01)：** 由各种图像相关任务合成的全面且多样化的基于指令的数据集。 **对齐数据集**也被提及，但在 ocr 中没有详细说明。 **Hybrid Attention：** 核心融合方法是混合注意力机制，将闪电注意力（线性）的效率与softmax注意力的检索能力结合起来。 **MoE 路由：** MoE 架构及其 top-2 路由策略允许选择性激活专家，在不增加每个代币计算成本的情况下增强模型容量。  全局路由器用于负载平衡。 **视觉语言融合 (VL-01)：** 使用两层 MLP 将 ViT 的视觉特征投影到 LLM 的嵌入空间中。  直接使用原始的高维视觉特征，无需池化或下采样，利用该架构的长上下文功能。 **Varlen Ring Attention 和 LASP+：** 这些算法可以在训练和推理过程中有效处理长的、可变长度的序列和数据打包。训练后和对齐：使用各种技术进行对齐。

</详情>

## **NVLM：开放前沿级多模式法学硕士**

NVLM 1.0 是一系列多模式大语言模型 (LLM)，在视觉语言任务上取得了最先进的结果，可与专有和开放访问模型相媲美。它展示了多模态训练后纯文本性能的改进，并提供了纯解码器和基于交叉注意的架构的全面比较，引入了一种新颖的混合架构和用于高分辨率图像的一维图块标记设计。

[![arXiv](https://img.shields.io/badge/arXiv-2409.11402-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2409.11402)
[![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/NVIDIA/Megatron-LM/tree/NVLM-1.0)
[![HuggingFace](https://img.shields.io/badge/🤗-Open%20In%20Spaces-blue.svg)](https://huggingface.co/nvidia/NVLM-D-72B)  
戴文亮、李娜妍、王博新、杨卓林、刘子涵、Jon Barker、Tuomas Rintamaki、Mohammad Shoeybi、Bryan Catanzaro、Wei Ping
<p align="center">
<img src="https://github.com/user-attachments/assets/da882643-ac1d-4566-8287-cd8da3897a88" width="600"/>
</p>

<详情>
<summary>ℹ️<i>更多信息</i></summary>

**NVLM（NVIDIA 视觉语言模型）** 引入了一系列具有三种主要架构的模型：NVLM-D（仅解码器）、NVLM-X（基于交叉注意力）和 NVLM-H（混合）。  所有模型共享一个共同的视觉路径，采用具有动态高分辨率 (DHR) 处理功能的冷冻 InternViT-6B-448px-V1-5 视觉编码器。  DHR 涉及将输入图像划分为图块（最多 6 个，具有不同的纵横比）和缩小的全局“缩略图”图块。  这些图块由视觉编码器处理，每个图块的 1024 个标记通过像素混洗被下采样到 256 个。 **NVLM-D（仅解码器）：** 通过 2 层 MLP 投影仪将视觉编码器连接到 LLM（Qwen2-72B-Instruct 或 Nous-Hermes-2-Yi-34B）。  它引入了一种新颖的*一维图块标记*设计来处理高分辨率图像。基于文本的图块标签（例如“<tile_1>”）被插入到每个图块的扁平化图像标记之前，以向 LLM 提供位置信息。  训练包括预训练（冻结LLM和视觉编码器，仅训练MLP）和监督微调（SFT）（解冻LLM和MLP）。  至关重要的是，其中包含高质量的纯文本 SFT 数据集，以维持/提高纯文本性能。 **NVLM-X（基于交叉注意力）：** 使用门控交叉注意力层来处理图像标记，类似于 Flamingo，但“没有”感知器重采样器。  图像特征通过一层 MLP 投影到 LLM 的隐藏维度。  门控 X 注意力层与 LLM 自注意力层交错。  训练还包括预训练和 SFT 阶段。 LLM 主干在 SFT 期间解冻，并使用高质量的纯文本数据集。还使用一维图块标签，但在 X-attention 层内。 **NVLM-H（混合）：** 结合了 NVLM-D 和 NVLM-X 的各个方面。  缩略图标记由 LLM 的自注意层（如 NVLM-D）处理，而常规图块标记由门控交叉注意层（如 NVLM-X）处理。  其目的是平衡多模态推理与计算效率。它还在交叉注意力中使用一维图块标签。与简单地连接图像标记或使用 2D 网格/边界框标签相比，一维图块标记设计显着提高了性能，尤其是在 OCR 相关任务上。作者强调，即使在预训练期间，数据集质量和任务多样性也比纯粹的规模更重要。 NVLM 模型在视觉语言和纯文本任务上均取得了出色的性能。  这是通过在 SFT 期间包含高质量的纯文本数据集并结合多模态数学和推理数据来实现的。解码器 VS X-Attention：基于交叉注意力的模型在高分辨率图像中更有效。然而，解码器模型在 OCR 相关任务中提供了统一的多模型推理和更高的准确性。根据开源数据集进行整理，包括字幕（COCO、CC3M、SBU、LAION-115M）、VQA（VQAv2、Visual Genome、DVQA）、文档理解（Docmatix）、OCR/Scene-Text（各种数据集）和数学（CLEVR-Math）。  重视质量而非数量。面向任务的数据集的多样化集合，包括字幕、VQA、图表/图表理解、文档理解、OCR、数学和科学数据集。来自各种来源（ShareGPT、SlimOrca、EvolInstruct 等）和类别（一般、数学、编码）的高质量纯文本数据对于维持/提高纯文本性能至关重要。  使用 GPT-40 和 GPT-40-mini 精制而成。 NVLM 模型在各种视觉语言基准（MMMU、MathVista、OCRBench、AI2D、ChartQA、DocVQA、TextVQA、RealWorldQA、VQAv2）和纯文本基准（MMLU、GSM8K、MATH、HumanEval）上进行评估。
</详情>

## **OmniVLM：用于高效设备上推理的令牌压缩、数十亿参数的视觉语言模型**

OmniVLM 是一种包含数十亿个参数的视觉语言模型，专为高效的设备端推理而设计，具有令牌压缩机制，可将视觉令牌序列长度从 729 减少到 81，从而在保持视觉语义保真度的同时大幅削减计算开销。它使用Qwen2.5-0.5B-Instruct模型，Google的SigLIP-400M。

[![arXiv](https://img.shields.io/badge/arXiv-2412.11475-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2412.11475)
[![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/NexaAI/nexa-sdk)
[![HuggingFace](https://img.shields.io/badge/🤗-Open%20In%20Spaces-blue.svg)](https://huggingface.co/NexaAIDev/OmniVLM-968M)  
陈伟、李志远、辛硕
<p align="center">
<img src="https://github.com/user-attachments/assets/da2a140a-5efe-4499-addc-8ccbb3e9792a" width="600"/>
</p>

<详情>
<summary>ℹ️<i>更多信息</i></summary>

OmniVLM 解决了在资源受限的边缘设备上部署视觉语言模型 (VLM) 的挑战。  它通过新颖的令牌压缩机制和多阶段训练管道来实现这一目标。核心创新是**图像令牌压缩**，它将投影层内的嵌入尺寸从 [batch_size, 729, hide_size] 转换为 [batch_size, 81, hide_size]。令牌数量减少 9 倍是通过重塑实现的，这是在与基于卷积的方法进行经验比较后选择的。模型架构（图 1）基于 LLaVA 框架，采用 Google 的 SigLIP-400M 作为视觉编码器、Qwen2.5-0.5B-Instruct 作为基础语言模型、多层感知器 (MLP) 作为投影层。  训练流程由三个阶段组成：(1) 对大规模图像标题对（主要来自 LLaVA 预训练数据集）进行预训练，以学习视觉语言对齐，仅训练投影层； (2) 对混合数据集（LLaVA、UnimmChat 和内部数据）进行 **监督微调 (SFT)**，以提高上下文理解和对话连贯性，在冻结视觉编码器的同时训练投影仪和 LLM； (3) **最小编辑直接偏好优化 (DPO)**，使用教师模型对基本模型的输出创建最小编辑的校正，形成选择-拒绝对以进行偏好学习，再次冻结视觉编码器并训练投影仪和 LLM。  DPO 流程利用 GPT-4V 生成合成训练对。大量实验表明，81 个令牌配置提供了计算效率和模型性能之间的最佳平衡。 OmniVLM 在 ScienceQA、POPE 和 MMMU 等基准测试中优于 nanoLLAVA，展示了改进的推理、多模态理解和泛化能力。至关重要的是，它实现了显着更快的推理速度（与笔记本电脑上的 nanoLLAVA 相比，首个令牌时间缩短了 9.1 倍，解码速度提高了 1.5 倍，移动设备上的 TTFT 加快了 8 倍），使其适合部署在智能手机和笔记本电脑等边缘设备上。
</详情>

## **Pixtral 12B：尖端的开放式多模态语言模型**

Pixtral 12B 是 Mistral AI 开发的 120 亿参数多模态语言模型，旨在出色地理解图像和文本，在各种多模态基准测试中实现领先的性能。 VLM 的核心构建在变压器架构之上。 VLM 的一个强大方面是，Pixtral 12B 从头开始​​使用新的视觉编码器进行训练，以原生支持可变图像尺寸和纵横比。

[![arXiv](https://img.shields.io/badge/arXiv-2410.07073-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2410.07073)
[![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/huggingface/transformers/blob/main/docs/source/en/model_doc/pixtral.md)
[![HuggingFace](https://img.shields.io/badge/🤗-Open%20In%20Spaces-blue.svg)](https://huggingface.co/mistralai/Pixtral-12B-2409)  
普拉韦什·阿格拉沃尔、西蒙·安东尼亚克、艾玛·布·汉娜、巴蒂斯特·布特、德文德拉·查普洛、杰西卡·查德诺夫斯基等。 （米斯特拉尔人工智能科学团队）
<p align="center">
<img src="https://github.com/user-attachments/assets/5187d3c0-e284-40eb-bb94-53105c8cbe11" width="600"/>
</p>

<详情>
<summary>ℹ️<i>更多信息</i></summary>

**Pixtral 12B** 有两个主要组件：*视觉编码器 (Pixtral-ViT)*，用于标记图像；以及*多模态解码器*，用于在给定文本和图像序列的情况下预测下一个标记。 Pixtral 可以将任意数量的图像作为输入，只要它们适合其 128K 上下文窗口。 **视觉编码器 (Pixtral-ViT)** 使用新颖的 ROPE-2D 实现从头开始进行训练，使其能够以其原始分辨率和纵横比处理图像。该模型可以在延迟受限的设置中灵活地处理低分辨率图像，同时在需要细粒度推理时处理高分辨率图像。为了区分具有相同数量的补丁但不同纵横比的图像，在图像行之间插入 **[IMAGE BREAK]** 标记。此外，图像序列末尾有一个 **[IMAGE END]** 标记。该模型采用**门控 FFN** 架构，在隐藏层中实现门控，而不是注意块中的标准前馈层。为了处理单个批次中的图像，该模型沿着序列维度展平图像并将它们连接起来。构造块对角掩码是为了防止不同图像的补丁之间的注意力泄漏。传统的学习和绝对位置嵌入被 **ROPE-2D** 取代，它允许处理可变的图像尺寸。 Pixtral 的 **多模态解码器** 构建在 Mistral Nemo 12B [15] 之上，Mistral Nemo 12B [15] 是一个 120 亿参数的纯解码器语言模型。解码器使用因果自注意力。视觉编码器通过两层全连接网络连接到多模态解码器。该论文将 Pixtral 描述为一种指令调整模型，在大规模交错图像和文本文档上进行了预训练。该论文贡献了一个名为 **MM-MT-Bench** 的开源基准，用于评估视觉语言模型。 Pixtral 擅长多模式指令跟踪，超越了同类开源模型
在 MM-MT-Bench 基准上。
</详情>

## **Sa2VA：将 SAM2 与 LLaVA 结合，实现对图像和视频的深入理解**

Sa2VA 是一个用于对图像和视频进行深入理解的统一模型，将 SAM-2 视频分割模型与 LLaVA 视觉语言模型集成在一起。它支持广泛的图像和视频任务，例如引用分割和对话，将所有输入（文本、图像、视频）视为共享 LLM 空间中的令牌，生成指导 SAM-2 进行精确掩模生产的指令令牌。

[![arXiv](https://img.shields.io/badge/arXiv-2501.04001-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2501.04001)
[![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/magic-research/Sa2VA)
[![HuggingFace](https://img.shields.io/badge/🤗-Open%20In%20Spaces-blue.svg)](https://huggingface.co/papers/2501.04001)  
袁浩波、李向太、张涛、黄子龙、徐世林、季顺平、佟云海、陆奇、冯嘉世、杨明轩

<p align="center">
<img src="https://github.com/user-attachments/assets/7527a503-4987-4401-961b-f52532788b1f" width="600"/>
</p>

<详情>
<summary>ℹ️<i>更多信息</i></summary>

Sa2VA 利用预训练的类似 LLaVA 的模型（包含视觉编码器、视觉投影层和 LLM）并附加 SAM-2。  至关重要的是，它采用“解耦设计”，其中 SAM-2 的解码器和内存模块被冻结。这保留了 SAM-2 的感知和跟踪功能，并使 Sa2VA 成为即插即用模块，可使用较新的 MLLM 进行更新。 LLM 和 SAM-2 之间的连接是一个特殊的“[SEG]”标记。 LLM 生成此标记，其隐藏状态充当 SAM-2 解码器的时空提示，该解码器生成分段掩码。该模型经过端到端训练，展示了可扩展性。该训练使用统一的指令调整格式来执行各种任务：参考分割、视觉问答（VQA）以及图像和视频的基础对话生成（GCG）。它将所有图像、视频和提示视为视觉标记。一个关键方面是与多个数据集（包括图像和视频数据）的协同训练。作者介绍了 *Ref-SAV*，这是一个自动标记的数据集，在复杂视频场景中包含超过 72,000 个对象表达，并手动验证 Ref-SAV 中的 2,000 个视频对象，以对引用视频对象分割进行基准测试。一种简单的掩模跟踪方法重新利用了 SAM-2 的知识。该模型将所有任务表述为单个指令调整过程。用于协同训练的数据集是：LLAVA 1.5 (665K)、RefCOCO (17K)、RefCOCO+ (17K)、RefCOCOg (22K)、Grand-f (214K)、ChatUniVi (100K)。 Ref-YTVOS (3.5K)、MeVIS (0.6K)、ReVOS (1.7K) 和 Ref-SAV (37K)。
</详情>

## **Tarsier2：推进大型视觉语言模型从详细的视频描述到全面的视频理解**

Tarsier2 是一种最先进的大型视觉语言模型 (LVLM)，擅长生成详细而准确的视频描述，并展示出卓越的通用视频理解能力。它可扩展预训练数据，在监督微调期间执行细粒度时间对齐，并使用基于模型的采样和直接偏好优化 (DPO) 来提高性能，其性能优于 GPT-4o 和 Gemini 1.5 Pro 等模型。

[![arXiv](https://img.shields.io/badge/arXiv-2501.07888-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2501.07888) [![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/bytedance/tarsier) [![HuggingFace](https://img.shields.io/badge/🤗-Open%20In%20Spaces-blue.svg)](https://huggingface.co/omni-research/Tarsier-7b)  
袁丽萍、王嘉伟、孙浩淼、张雨辰、林媛

<p align="center">
<img src="https://github.com/user-attachments/assets/e6626842-69ac-4547-8c4b-cb260dd349ca" width="600"/>
</p>

<详情>
<summary>ℹ️<i>更多信息</i></summary>

Tarsier2 采用简单的架构，由视觉编码器、视觉适配器和大型语言模型 (LLM) 组成，专门基于 Qwen2-VL 构建。  该模型经历了三个阶段的训练过程：预训练、监督微调 (SFT) 和使用直接偏好优化 (DPO) 的强化学习 (RL)。  与其前身 Tarsier 相比，一个关键改进是预训练数据集从 1100 万个视频文本对显着扩展至 4000 万个视频文本对。此次扩展包括对1100万个评论视频（电影和电视剧的解释和分析）的精心收集和过滤，提供丰富的上下文信息。  在 SFT 阶段，Tarsier2 在包含 15 万个实例的数据集上进行训练，每个实例都有详细的视频描述和与每个描述事件相对应的特定帧注释。  与传统的视频字幕对齐相比，这种“细粒度时间对齐”提供了提高准确性并减少幻觉的监督。 SFT 阶段分两步进行。第一步是帧与事件的对齐。然后，模型的输出做出更加人性化的风格。最后的训练阶段采用 DPO 和自动生成的偏好数据。负样本是通过损坏视频（剪辑切换、剪辑反转、剪辑裁剪和下采样）创建的，并且偏好数据过滤方法（使用 AutoDQ）可确保高质量的对。  Tarsier2 在 15 项公共基准测试中取得了最先进的结果，展示了其在视频问答、视频接地、幻觉测试和具身问答等任务中的多功能性。  还发布了重述数据集 Tarsier2-Recap-585K。
</详情>

## **UI-TARS：开创性的与本机代理的自动化 GUI 交互**

UI-TARS 是一种原生 GUI 代理模型，仅在屏幕截图上运行，执行类似人类的交互（键盘和鼠标操作）。与依赖包装商业模型（例如 GPT-4o）的框架不同，UI-TARS 是一种端到端模型，在感知、基础和任务执行方面在 10 多个 GUI 代理基准上实现了最先进的 (SOTA) 性能，显着优于复杂的框架。

[![arXiv](https://img.shields.io/badge/arXiv-2501.12326-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2501.12326) [![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/bytedance/UI-TARS) [![HuggingFace](https://img.shields.io/badge/🤗-Open%20In%20Spaces-blue.svg)](https://huggingface.co/bytedance-research/UI-TARS-7B-SFT)  
秦雨佳、叶一宁、方俊杰、王浩明、梁世豪、田世作、张军达、李家豪、李云欣、黄世爵、钟万军、李宽野、杨家乐、苗宇、林卧宇、刘龙翔、徐江、马千里、李静宇、肖晓君、蔡凯、李闯、郑耀伟、金朝林、李陈、小周、王敏朝、陈浩丽、李兆建、杨海华、刘海峰、林峰、彭涛、刘鑫、石光

<p align="center">
<img src="https://github.com/user-attachments/assets/9dccbdf3-a0ab-4ae4-930b-09a974f14a03" width="600"/>
</p>

<详情>
<summary>ℹ️<i>更多信息</i></summary>

UI-TARS 利用了多项关键创新：(1) **增强感知**，利用大规模 GUI 屏幕截图数据集进行上下文感知理解和 UI 元素的精确字幕； （2）**统一动作建模**，将动作标准化到跨平台的统一空间，通过大规模的动作轨迹实现精准落地； (3) **System-2 Reasoning**，包含多步骤决策的深思熟虑的推理，包括任务分解、反思和里程碑识别； (4) **使用反射在线跟踪进行迭代训练**，通过自动收集、过滤和细化数百个虚拟机上的交互跟踪来解决数据瓶颈。  该模型经过迭代训练并通过反思进行调整，不断从错误中学习并以最少的人为干预适应新情况。  该架构将屏幕截图作为输入，并使用视觉语言模型（VLM），特别是 Qwen-2-VL 7B 和 72B，来处理视觉信息并生成动作。  操作空间是跨平台（移动、桌面、Web）统一的，包括单击、键入、滚动和拖动等操作。  受 ReAct 框架的启发，通过在每个行动之前生成明确的“想法”来注入推理。这些想法是通过精心策划的 GUI 教程和增强的操作轨迹相结合产生的，并结合了任务分解、长期一致性、里程碑识别、试错和反思等模式。  训练过程涉及多个阶段，首先是使用 GUI 屏幕截图和相关元数据的精选数据集增强感知。  该数据集支持元素描述、密集字幕、状态转换字幕、问题回答和标记集提示等任务。通过创建大规模的动作轨迹数据集并使用基础数据将元素描述与空间坐标配对，可以改进动作建模。  该模型结合使用监督微调 (SFT) 和直接偏好优化 (DPO) 进行训练，并通过反射调整从错误中学习。
</详情>


## **VideoChat-Flash：用于长上下文视频建模的分层压缩**

VideoChat-Flash 是一个设计用于处理多模式大语言模型 (MLLM) 中的长格式视频内容的系统。它引入了分层视觉令牌压缩（HiCo）方法来减少计算负载，同时保留基本细节，并使用多阶段学习方法和新的长视频数据集（LongVid）来在长视频和短视频基准上实现最先进的性能。

[![arXiv](https://img.shields.io/badge/arXiv-2501.00574-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2501.00574) [![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/OpenGVLab/VideoChat-Flash) [![HuggingFace](https://img.shields.io/badge/🤗-Open%20In%20Spaces-blue.svg)](https://huggingface.co/OpenGVLab/VideoChat-Flash-Qwen2_5-2B_res448)  
李新浩、王毅、余嘉硕、曾翔宇、朱雨涵、黄海安、高剑飞、李坤昌、何一楠、王晨婷、乔宇、王亚丽、王利民

<p align="center">
<img src="https://github.com/user-attachments/assets/49048795-6a76-41e7-b441-1313d0813630" width="600"/>
</p>

<详情>
<summary>ℹ️<i>更多信息</i></summary>

**分层视觉令牌压缩（HiCo）：**这是核心创新。  它在两个级别上压缩视频信息： **剪辑级压缩：** 视频被分为剪辑。  视觉编码器 (UMT-L) 处理每个剪辑，压缩器（与 MLP 合并的令牌）减少视觉令牌的数量。  这利用了帧间冗余。  **视频级压缩：** 在 LLM (Qwen2-7B) 交互过程中，使用渐进式视觉 dropout 策略进一步减少视觉标记。  这利用了法学硕士关注浅层的整个背景和更深层次的具体细节的想法。  它结合了均匀滤除（浅层）和文本引导选择（深层）。 **视觉编码器：** UMT-L@224 [30]（一种视频编码器，比 SigLIP 等图像编码器更高效）。 **视觉语言连接器：** 压缩器（令牌合并），后跟 MLP 投影。 **大型语言模型（LLM）：** Qwen2-7B。 **多阶段从短到长的学习：**这是一个至关重要的训练策略：**第 1 阶段：视频语言对齐：** 使用图像-文本和短视频-文本对（每个 0.5M）训练压缩器和 MLP。 **第 2 阶段：短视频预训练：** 通过更多图像 (3.5M) 和短视频 (2.5M) 增强视觉理解。 **第 3 阶段：联合短视频和长视频指令调整：** 使用指令跟踪数据对图像 (1.1M)、短视频 (1.7M) 和长视频 (0.7M) 的混合进行微调。 **第 4 阶段：高效高分辨率后期微调：** 通过对第 3 阶段数据的子集 (25%) 微调视频编码器来适应更高分辨率（224 至 448）。 **动态视频采样：** 使用双采样策略：针对短视频（捕捉运动）的密集采样 (15 fps) 和针对长视频（捕捉事件）的稀疏采样 (1 fps)。 **Timestamp-aware Prompt：** 使用简单的文本提示向模型提供时间戳信息：“视频持续 N 秒，从中统一采样 T 帧。 **LongVid：** 论文中介绍的一种新的大规模长视频指令调优数据集。它包含跨越 5 个任务类型的 114,228 个长视频和 3,444,849 个问答对。它利用了现有数据集（Ego4D、 HowTo100M、HD-Vila、MiraData）并生成密集的事件标签。**混合训练数据：**在训练期间使用短视频和长视频的组合**NIAH（视频干草堆中的针）**用于测试模型理解长上下文的能力。

</详情>

## **VideoLLaMA 3：图像和视频理解的前沿多模态基础模型**

VideoLLaMA3 是一种以视觉为中心的多模态基础模型，专为图像和视频理解而设计，强调优先考虑高质量图像文本数据的训练范例和框架，以及适应性强的视觉编码器和视频令牌压缩，以实现最先进的性能。

[![arXiv](https://img.shields.io/badge/arXiv-2501.13106-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2501.13106v1)
[![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/DAMO-NLP-SG/VideoLLaMA3)
[![HuggingFace](https://img.shields.io/badge/🤗-Open%20In%20Spaces-blue.svg)](https://huggingface.co/papers/2501.13106)  
张伯强、李克涵、程泽森、胡志强、袁宇谦、陈冠正、冷思聪、姜玉明、张航、李欣、金鹏、张文琪、王帆、冰立东、赵德利

<p align="center">
<img src="https://github.com/user-attachments/assets/350a1228-c14e-45ed-b59f-e99608ee9a7d" width=600/>
</p>

<详情>
<summary>ℹ️<i>更多信息</i></summary>

**VideoLLaMA3**在其训练范式和框架设计中引入了以视觉为中心的方法，专注于增强图像和视频理解能力。  核心架构包含预训练的视觉编码器（SigLIP）、视频压缩器（DiffFP）、投影仪和大型语言模型（LLM - Qwen2.5）。该模型采用四阶段训练过程：1）**视觉编码器适应**，其中视觉编码器适应使用场景图像、文档数据和场景文本图像来接受可变分辨率的图像； 2) **视觉-语言对齐**，使用大规模图像文本数据（包括详细的标题、文档和图表）和少量纯文本数据联合调整视觉编码器、投影仪和LLM； 3）**多任务Fine-tuning**，合并下游任务的图文数据和通用视频字幕数据； 4) **以视频为中心的微调**，使用一般视频、流视频、临时视频、纯图像和纯文本数据。一项关键创新是**任何分辨率视觉标记化 (AVT)**，它允许视觉编码器通过用旋转位置嵌入 (RoPE) 替换固定位置嵌入来处理任何分辨率的图像和视频。  这使得能够处理具有可变形状和最小信息丢失的图像。  对于视频输入，**差分帧修剪器 (DiffFP)** 充当视频压缩器，通过比较像素空间中时间连续补丁之间的 1-范数距离并修剪冗余补丁来减少视觉标记的数量。  这使得视频表示更加紧凑和精确。每个阶段的训练数据混合都经过精心策划，强调高质量的图像文本数据。视觉编码器适应阶段使用 VL3-Syn7M-short、LLaVA-Pretrain-558k 等数据集和文档数据集。视觉语言对齐阶段通过详细的标题、OCR 数据和带有边界框的细粒度数据对此进行了扩展。多任务微调阶段添加问答数据和一般视频字幕数据。最后，以视频为中心的微调阶段包括一般视频、流视频和时间基础数据。这种“以视觉为中心”的方法，优先考虑图像理解作为视频理解的基础，与 AVT 和 DiffFP 一起，使 VideoLLaMA3 在图像和视频基准测试中实现强大的性能。
</详情>

## **Llama 3.2-Vision：基于 Llama 3 的增强型多模式功能**

Llama 3.2-Vision 通过多模式功能扩展了 Llama 3 纯文本模型，使其能够处理文本和图像。该模型有 11B 和 90B 参数大小，利用具有交叉注意层的视觉适配器将来自单独视觉编码器的图像表示集成到核心 Llama 3 LLM 中，在视觉识别、图像推理、字幕和视觉问答方面实现了强大的性能。

[![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/meta-llama/llama-models) [![HuggingFace](https://img.shields.io/badge/🤗-Open%20In%20Spaces-blue.svg)](https://huggingface.co/meta-llama/Llama-3.2-11B-Vision)  
元
<p align="center">
<img src="https://github.com/user-attachments/assets/f6428237-8607-4de1-975d-dfc4c683b7a3" width=600/>
</p>

<详情>
<summary>ℹ️<i>更多信息</i></summary>

**Llama 3.2-Vision** 基于 Llama 3 架构构建，这是一种使用优化转换器的自回归语言模型。  它添加了一个由交叉注意力层组成的“视觉适配器”，以合并视觉信息。  该适配器从*单独的视觉编码器*（不是核心 Llama 3 模型的一部分）接收输入，允许模型处理图像而无需直接将其转换为文本标记。提示中的“<|image|>”标签表示图像的存在，并指示通过交叉注意力集成视觉信息的位置。这种集成发生在图像标签“之后”，并影响“后续”文本标记。该模型支持 128k token 的上下文长度，并利用分组查询注意力 (GQA)。该模型系列接受了 6B 个图像-文本对的训练。预训练数据截止日期为2023年12月，支持英语、德语、法语、意大利语、葡萄牙语、印地语、西班牙语和泰语。然而，图像文本任务只有英文版本。该模型的训练涉及针对指令调整版本的监督微调（SFT）和人类反馈强化学习（RLHF）。基本模型适用于使用特定提示格式的带有或不带有图像的文本完成。  经过指令调整的模型擅长视觉问答 (VQA)、文档 VQA (DocVQA)、图像字幕和图像文本检索等任务。训练过程包括预训练和退火阶段，利用大量数据和重要的计算资源（H100 GPU）。关键功能包括处理文本和图像输入、回答有关图像的问题、生成说明文字以及执行视觉推理。  当提示中存在图像时，该模型*不*支持内置工具调用（如“brave_search”或“wolfram_alpha”）；工具调用仅适用于纯文本输入。  预期用例涵盖广泛的应用程序，但使用受到 Llama 3.2 社区许可和可接受使用政策的限制，特别是在语言和潜在滥用方面。 Meta 强调负责任的部署方法，包括提供 Llama Guard 等安全工具，并鼓励开发人员实施适当的保护措施。该模型经过了广泛的评估，包括红队和对 CBRNE、儿童安全和网络攻击等关键风险的评估。
</详情>

## **SmolVLM：小型、高效、开源的视觉语言模型**

SmolVLM 是一种 2B 参数视觉语言模型 (VLM)，其内存占用实现了最先进的性能，为多模式任务提供了小型、快速且内存高效的解决方案。  它完全开源，所有模型检查点、数据集、训练配方和工具均在 Apache 2.0 许可证下发布，支持本地部署、降低推理成本和用户定制。

[![arXiv](https://img.shields.io/badge/Blog-SmolVLM%20Blog-b31b1b.svg?style=flat-square)](https://huggingface.co/blog/smolvlm)
[![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/huggingface/smollm)
[![HuggingFace](https://img.shields.io/badge/🤗-Open%20In%20Spaces-blue.svg)](https://huggingface.co/HuggingFaceTB/SmolVLM-Instruct)  
安德烈斯·马拉菲奥蒂、梅尔韦·诺扬、米克尔·法雷、埃利·巴科什、佩德罗·昆卡

<p align="center">
<img src="https://github.com/user-attachments/assets/901ed802-5c1c-4733-ab2a-6b61514b9c71" width="600"/>
</p>

<详情>
<summary>ℹ️<i>更多信息</i></summary>

SmolVLM 基于 Idefics3 的架构构建，利用 Transformer 中的类似实现，但存在关键差异以提高效率。它用更小的 SmolLM2 1.7B 模型取代了 Llama 3.1 8B 语言主干。  采用了更积极的图像压缩策略，使用像素洗牌策略将视觉信息减少了 9 倍（与 Idefics3 中的 4 倍相比）。  这允许 384x384 的补丁，并且形状优化的 SigLIP 用作具有 14x14 内部补丁的视觉主干。与 Transformer 中的其他 VLM 相比，该模型展示了卓越的内存使用率，从而实现高效的设备上推理。  例如，对单个图像和提示进行编码仅需要 1.2k 个令牌，明显少于 Qwen2-VL 等模型。这种效率意味着更快的预填充和生成吞吐量。 SmolVLM 在 MMMU、MathVista、MMStar、DocVQA 和 TextVQA 等基准测试中取得了出色的性能。利用其长上下文功能，它在基本视频分析方面也显示出了可喜的结果。训练涉及使用 RoPE 基值调整等技术以及对长上下文和短上下文数据集的混合进行微调等技术，将 SmolLM2 的上下文窗口扩展到 16k 令牌。 VLM 训练使用了一个主要基于 The Cauldron 和 Docmatix 的精选训练数据集。检查点选择基于多个视觉语言基准的加权指标。该模型与 VLMEvalKit 集成以方便评估，并且可以通过 Transformers 库轻松使用和微调。  TRL 集成允许应用直接偏好优化 (DPO)。提供了一个笔记本用于在 VQAv2 上进行微调，甚至可以在消费级 GPU 的限制内进行 LoRA、QLoRA 或完全微调选项。
</详情>

## **Idefics2**

IDEFICS2 是一种 8B 参数开源视觉语言模型，通过结合 SigLIP 视觉编码器、Mistral-7B LLM 和具有 MLP 投影的感知器池层来高效处理交错图像和文本序列，以实现稳健的文本编码，在 OCR 和文档理解等任务中表现出色。

[![arXiv](https://img.shields.io/badge/arXiv-2405.02246-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2405.02246) [![Gradio](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/HuggingFaceM4/idefics-8b)  
雨果·劳伦松、莱奥·特隆雄、马蒂厄·科德、维克多·桑
<p align="center">
<img src="https://github.com/gokayfem/awesome-vlm-architectures/assets/88277926/c197c8c5-8da2-4d96-8999-8e05e81f1506" />
</p>  
<详情>
<summary>ℹ️<i>更多信息</i></summary>
  
IDEFICS2 是一个 8B 参数开源视觉语言模型，擅长处理交错的图像和文本序列。 IDEFICS2 采用专为高效处理图像和文本序列而设计的视觉语言架构。它采用 SigLIP 模型作为视觉编码器，以原始分辨率和纵横比从图像中提取特征。 Mistral-7B 模型作为 LLM 骨干，提供语言理解和生成功能。对于文本编码，IDEFICS2 利用 **感知器池层** 和 **MLP 投影** 将视觉特征与 LLM 的嵌入空间集成。视觉编码器、LLM 和文本编码器的组合使 IDEFICS2 能够处理各种多模式任务，特别关注 OCR 和文档理解。  该模型在包括 OBELICS、LAION Coco 和 PMD 在内的多样化数据集上进行训练，并提供用于 OCR 任务的附加数据。在 The Cauldron 和 OpenHermes-2.5 等指令数据集上进行微调。
</详情>

## **Idefics3-8B：构建和更好地理解视觉语言模型**

Idefics3-8B 是一种功能强大的开源视觉语言模型 (VLM)，其性能显着优于其前身 Idefics2-8B，同时仅在开放数据集上进行高效且专门的训练。它利用简单的管道并引入了 Docmatix（用于文档理解的海量数据集），以在各种多模式基准的大小类别内实现最先进的性能。

[![arXiv](https://img.shields.io/badge/arXiv-2408.12637-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2408.12637) [![HuggingFace](https://img.shields.io/badge/🤗-Open%20In%20Spaces-blue.svg)](https://huggingface.co/spaces/HuggingFaceM4/idefics3)  
雨果·劳伦松、安德烈斯·马拉菲奥蒂、维克多·桑、莱奥·特隆雄
<p align="center">
<img src="https://github.com/user-attachments/assets/5e61fec2-b41b-4ad8-a167-1966f169b866" />
</p>

<详情>
<summary>ℹ️<i>更多信息</i></summary>

Idefics3-8B 建立在预训练单峰模型的基础上，特别是 Llama 3.1 指令作为语言模型，SigLIP-SO400M 作为视觉编码器。它采用自注意力架构，其中视觉特征被视为标记，并在输入 LLM 之前与文本标记连接起来。为了增强 OCR 功能并解决每个图像的视觉标记有限的瓶颈，Idefics3-8B 使用简单的像素洗牌策略替换了 Idefics2 中使用的感知器重采样器，类似于 InternVL-1.5。该策略将图像隐藏状态的数量减少了 4 倍，从而可以将较大的图像（高达 364x364 像素）编码为 169 个视觉标记。该模型在训练和推理过程中均采用图像分割策略，将原始图像分割为 364x364 像素图块的矩阵。为了保留这些图块的 2D 结构和位置信息，在每行图块之后插入一个文本标记“\n”，并将缩小的原始图像附加到序列中。此外，每个图块前面都添加了指示其在矩阵中位置的文本标记。训练过程包括预训练和监督微调的三个阶段。在第一个预训练阶段，主干（LLM 和视觉编码器）被冻结，并且仅训练新初始化的参数。最大图像分辨率逐渐从364²增加到1820²。从第二阶段开始，使用 DoRA（LoRA 的一种变体）有效地训练主干网，并将更大的图像引入训练数据中。最后的预训练阶段侧重于使用大型合成数据集进行训练，包括 Docmatix、Websight、LNQA、PixelProse 和 ChartGemma。在监督微调期间，NEFTune 噪声应用于输入，并且仅根据答案标记计算损失。前两个预训练阶段的学习率保持恒定，并在最后的预训练阶段和监督微调期间线性衰减到零。 Idefics3-8B 展示了相对于 Idefics2 的显着改进，特别是在文档理解任务方面，在 DocVQA 上实现了 13.7 点的改进。这凸显了 Docmatix 数据集的有效性以及 Idefics3-8B 中所做的架构选择。该模型还在 MMMU、MathVista、MMStar 和 TextVQA 等各种多模态基准测试中实现了其尺寸类别中最先进的性能，展示了其强大的视觉理解和推理能力。
</详情>

## **InternLM-XComposer2：掌握视觉语言大模型中的自由形式文本图像合成和理解**

InternLM-XComposer2 通过使用新颖的 Partial LoRA 模块将 CLIP 预训练视觉编码器与强大的 InternLM-2 LLM 连接起来，在自由格式文本图像合成和理解方面表现出色，从而实现视觉和语言标记的有效对齐，从而增强多模态理解。

[![arXiv](https://img.shields.io/badge/arXiv-2401.16420-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2401.16420) [![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/InternLM/InternLM-XComposer) [![Gradio](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/Willow123/InternLM-XComposer)  
董晓义、张攀、臧宇航、曹宇航、王斌、欧阳林克、魏西林、张松阳、段浩东、曹茂松、张文伟、李伊宁、严航、高阳、张新月、李伟、李静文、陈凯、何从辉、张兴成、乔宇、林大华、王嘉琪
<p align="center">
<img src="https://github.com/gokayfem/Awesome-VLM-Architectures/assets/88277926/732d3b7b-02de-42d3-ae76-800bf035b391" />
</p> 
<详情>
<summary>ℹ️<i>更多信息</i></summary>
    
**InternLM-XComposer2**：该模型引入了一种复杂的架构，利用视觉编码器和大型语言模型 (LLM)，通过部分低秩适应 (LoRA) 模块互连。这种创新设置使 InternLM-XComposer2 能够利用视觉编码器生成的视觉标记以及从标记化文本派生的语言标记，有效地处理图像和文本。使用 CLIP 进行图像语言对比学习预训练的视觉编码器和充当具有多语言功能的 LLM 的 InternLM-2 是该架构的关键组件。 **部分 LoRA** 模块的独特之处在于，通过专门应用于视觉标记的低等级适应来对齐视觉和语言标记，从而增强模型的多模态理解和处理效率。 InternLM-XComposer2 的训练方法是多方面的，重点是微调视觉编码器和部分 LoRA，以使视觉标记与跨各种数据集的 LLM 保持一致。这个过程涉及一般语义对齐、世界知识对齐和视觉能力增强，以细化模型解释图像信息和组成文本图像内容的能力。有监督微调进一步包括多任务训练和自由形式的文本图像合成，旨在优化模型在利用图像信息进行全面的文本图像生成和理解方面的性能。 InternLM-XComposer2中的对齐技术和融合方法利用部分LoRA模块来有效集成不同模态，从而丰富LLM的模态特定知识，同时保留其固有功能。通过部分 LoRA 对视觉标记进行选择性增强，使模型能够在视觉和文本领域表现出强大的性能，促进多模态理解中的详细感知、逻辑推理和广泛的知识集成。该模型采用各种数据集，包括 ShareGPT4V-PT、COCO、Nocaps、TextCaps 等，用于预训练和监督微调。这些数据集为 InternLM-XComposer2 配备了广泛的功能，包括通用语义对齐、世界知识对齐、视觉能力增强以及促进自由格式文本图像合成，标志着视觉语言大模型领域的重大进步。
</详情>

## **InternLM-XComposer2-4KHD：开创性的大型视觉语言模型，可处理从 336 像素到 4K 高清的分辨率**

InternLM-XComposer2-4KHD 在其前身的基础上，通过采用动态分辨率和自动补丁配置，在 LVLM 中开创了高分辨率图像处理的先河，适应从 336 像素到 4K 高清的分辨率，以增强视觉理解而不失真。

[![arXiv](https://img.shields.io/badge/arXiv-2404.06512v1-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2404.06512v1)  
董晓义、张攀、臧宇航、曹宇航、王斌、欧阳林科、张松阳、段浩东、张文伟、李伊宁、严航、高阳、陈喆、张新月、李伟、李静文、王文海、陈凯、何从辉、张兴成、戴继峰、乔宇、林大华、王佳琪
<p align="center">
<img src="https://github.com/gokayfem/awesome-vlm-architectures/assets/88277926/c09b67fb-32eb-43de-82fa-96c3af22caf4" />
</p> 
<详情>
<summary>ℹ️<i>更多信息</i></summary>
  
**InternLM-XComposer2-4KHD**：尖端的大视觉语言模型 (LVLM) 旨在处理高达 4K 高清及以上的超高分辨率，同时还支持 336 像素以上的各种分辨率。该模型建立在 InternLM-XComposer2 架构之上，结合了新颖的**动态分辨率和自动补丁配置**技术。这使得模型能够根据输入图像的纵横比动态调整补丁布局和计数，从而能够高效处理高分辨率图像，同时保留其原始比例。为了解决可变补丁配置引起的潜在歧义，引入了换行标记来描述补丁标记行，从而显着提高了性能。 InternLM-XComposer2-4KHD 在多种数据集上进行了预训练，包括图像标题对、概念知识和 OCR 数据集，专注于增强高分辨率和结构图像理解。有监督微调进一步结合了混合分辨率策略，对需要细粒度细节的任务（例如 HD-OCR 任务）采用更高分辨率，并为其他任务动态调整分辨率。这种方法使模型能够在高分辨率场景和一般视觉语言理解任务中表现出色。
</详情>

## **InternLM-XComposer-2.5：支持长上下文输入和输出的多功能大视觉语言模型**

InternLM-XComposer-2.5 (IXC-2.5) 是一种多功能大视觉语言模型 (LVLM)，旨在处理长上下文输入和输出，在各种文本图像理解和合成任务中表现出色。它的性能可与 GPT-4V 相媲美，并且 7B LLM 后端要小得多，这证明了其效率和可扩展性。

[![arXiv](https://img.shields.io/badge/arXiv-2407.03320-b31b1b.svg?style=flat-square)](https://arxiv.org/pdf/2407.03320) [![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/InternLM/InternLM-XComposer) [![HuggingFace](https://img.shields.io/badge/🤗-Open%20In%20Spaces-blue.svg)](https://huggingface.co/spaces/Willow123/InternLM-XComposer)  
张潘、董小一、臧宇航、曹宇航、钱瑞、陈林、郭启鹏、段浩东、王斌、欧阳林克、张松阳、张文伟、李伊宁、高阳、孙鹏、张新月、李伟、李静文、王文海、严航、何从辉、张兴成、陈凯、戴继峰、乔宇、林大华、王佳琪

<p align="center">
<img src="https://github.com/user-attachments/assets/1330a013-930b-4b23-90dc-94616b59ca0b" />
</p>

<详情>
<summary>ℹ️<i>更多信息</i></summary>

InternLM-XComposer-2.5 建立在其之前的迭代（IXC-2 和 IXC-2-4KHD）的基础上，并具有三组件架构：轻量级 **OpenAI ViT-L/14 视觉编码器**、强大的 InternLM2-7B LLM 以及用于在视觉和语言模态之间高效对齐的 **Partial LoRA**。 IXC-2.5支持多种输入方式，包括文本、单/多图像和视频。它利用统一动态图像分区策略来处理高分辨率图像和视频，调整它们的大小并将它们填充成更小的块，同时保留纵横比。对于视频，沿短边对帧进行采样和连接，创建高分辨率的合成图像。该模型使用各种数据集分三个阶段进行预训练：一般语义对齐、世界知识对齐和视觉能力增强。在预训练期间，LLM 被冻结，视觉编码器和 Partial LoRA 进行微调，以使视觉标记与 LLM 保持一致。然后对涵盖各种任务的数据集集合进行监督微调，包括字幕、视觉问答、多轮 QA、科学 QA、图表 QA、数学 QA、OCR QA、视频理解和对话。这个微调过程涉及使用加权数据采样策略和每个组件的特定学习率计划来联合训练所有组件。 IXC-2.5还引入了两个新颖的应用程序：制作网页和撰写高质量的文本图像文章。对于网页生成，该模型根据合成和真实网络数据的组合进行训练，使其能够根据屏幕截图、说明或简历文档生成 HTML、CSS 和 JavaScript 代码。对于文章撰写，IXC-2.5 利用思想链 (CoT) 和直接偏好优化 (DPO) 技术来提高书面内容的质量。这包括使用 CoT 重写原始提示，使用不同的随机种子生成不同的响应，以及训练奖励模型来选择首选响应，最终生成更具创意和高质量的文章。
</详情>

## **InternVL 2.5：通过模型、数据和测试时间缩放扩展开源多模式模型的性能边界**

InternVL 2.5 是一个先进的多模态大型语言模型 (MLLM) 系列，它建立在 InternVL 2.0 的基础上，保留其核心架构，同时增强训练和测试策略以及数据质量，以与 GPT-4o 和 Claude-3.5-Sonnet 等领先的商业模型相媲美。

[![arXiv](https://img.shields.io/badge/arXiv-2412.05271-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2412.05271)
[![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/OpenGVLab/InternVL)
[![HuggingFace](https://img.shields.io/badge/🤗-Open%20In%20Spaces-blue.svg)](https://huggingface.co/OpenGVLab/InternVL2_5-78B)  
陈喆、王伟云、曹越、刘扬州、高张伟、崔二飞、朱金国、叶胜龙、田浩、刘朝阳、谷立新、王学慧、李青云、任益民、陈子轩、罗佳鹏、王家豪、谭江、王博、何从辉、石博天、张兴成、吕韩、王一、邵文琪、楚沛、屠忠英、何童、吴志勇、邓慧鹏、葛嘉业、陈凯、张开鹏、王利民、窦敏、路乐伟、朱喜洲、卢童、林大华、乔宇、戴继峰、王文海
<p align="center">
<img src="https://github.com/user-attachments/assets/d1651bde-a587-4b60-83e4-40468d6442ee" width="600"/>
</p>

<详情>
<summary>ℹ️<i>更多信息</i></summary>

**InternVL 2.5** 保留了其前身的“ViT-MLP-LLM”架构，通过 2 层 MLP 投影仪将预训练的 InternViT（InternViT-6B 或 InternViT-300M）与不同大小的 LLM（InternLM 2.5、Qwen 2.5）相结合。一个关键功能是像素 unshuffle 操作，将每个 448x448 图像图块的视觉标记从 1024 个减少到 256 个，从而提高了高分辨率处理的可扩展性。该模型架构支持动态分辨率，通过将图像划分为 448x448 块来适应图像长宽比。  至关重要的是，除了单图像和纯文本数据外，InternVL 2.0 和 2.5 还包含多图像和视频数据。训练策略涉及三阶段流程：(1) MLP 预热，仅训练 MLP 投影仪；(2) 可选的 ViT 增量学习，训练视觉编码器和 MLP 以增强视觉特征提取，特别是对于网络规模数据中罕见的领域；(3) 完整模型指令调整，其中整个模型在高质量多模态指令数据集上进行训练。  采用渐进式扩展策略，从较小的法学硕士开始并逐步扩大，从而允许视觉编码器与较大的法学硕士有效对齐。  训练增强功能包括随机 JPEG 压缩（为了保证真实世界图像质量的鲁棒性）和损失重新加权（为了平衡不同长度响应的贡献）。使用“nmax”（最大切片数）和重复因子（“r”）等参数来控制数据采样频率来优化数据组织。数据打包策略将多个样本连接成更长的序列，以提高 GPU 利用率。一个重要的贡献是数据过滤管道，用于删除低质量样本，特别是那些具有重复模式的样本，从而减轻重复生成的风险，这是 MLLM 中的一个常见问题。数据混合包括广泛的任务（字幕、一般 QA、数学、图表、OCR 等）和模式（单图像、多图像、视频、文本）。该模型在多种基准上进行了全面评估，包括多学科推理（MMMU、MMMU-Pro）、文档理解（DocVQA）、多图像/视频理解、现实世界理解、多模态幻觉检测、视觉基础、多语言能力和纯语言处理。
</详情>

## **DeepSeek-VL：迈向现实世界视觉语言理解**

DeepSeek-VL 利用结合了 SigLIP-L 和 SAM-B 的混合视觉编码器，通过有效处理高分辨率图像并通过两层混合 MLP 适配器将提取的特征与 DeepSeek LLM 主干集成，在现实世界视觉语言理解方面表现出色。

[![arXiv](https://img.shields.io/badge/arXiv-2401.16420-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2403.05525) [![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/deepseek-ai/DeepSeek-VL) [![Gradio](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/deepseek-ai/DeepSeek-VL-7B)  
卢浩宇、刘文、张波、王秉轩、董凯、刘波、孙景祥、任同正、李卓书、杨浩、孙耀峰、邓成奇、徐汉伟、谢振达、阮冲
<p align="center">
<img src="https://github.com/gokayfem/awesome-vlm-architectures/assets/88277926/7b7283d2-b2d5-4ab6-891a-18a9760ef7ca" />
</p> 
<详情>
<summary>ℹ️<i>更多信息</i></summary>

**DeepSeek-VL**：采用混合视觉编码器架构，融合用于语义理解的 **SigLIP-L 编码器**和用于高分辨率细节提取的 **SAM-B 编码器**。这样可以高效处理 1024x1024 图像，同时捕获全局和细粒度的视觉特征。 **两层混合 MLP 适配器**然后将这些功能与 DeepSeek LLM 主干集成。该模型在多种数据集上进行了预训练，其中包括网页屏幕截图、PDF、OCR、图表以及来自 Common Crawl、Web 代码、电子书和 arXiv 文章等来源的基于知识的内容。使用基于真实用户场景的精选指令调整数据集进一步完善这种预训练，并将其分类为涵盖识别、转换、分析、推理、评估和安全任务的综合分类法。通过将这些多样化的数据与其独特的架构和融合策略相结合，DeepSeek-VL 旨在在广泛的现实世界视觉语言应用程序中提供强大的性能。
</详情>

## **DeepSeek-VL2：用于高级多模态理解的专家混合视觉语言模型**

DeepSeek-VL2 是一系列先进的大型专家混合 (MoE) 视觉语言模型，通过结合高分辨率图像的动态平铺视觉编码策略并利用具有多头潜在注意力的 DeepSeekMoE 模型进行高效推理，显着改进了其前身 DeepSeek-VL。它经过大型视觉语言数据集的训练，在任务中显示出最佳性能。

[![arXiv](https://img.shields.io/badge/arXiv-2412.10302-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2412.10302)
[![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/deepseek-ai/DeepSeek-VL2)
[![HuggingFace](https://img.shields.io/badge/🤗-Open%20In%20Spaces-blue.svg)](https://huggingface.co/spaces/deepseek-ai/deepseek-vl2-small)  
吴志宇、陈小康、潘子正、刘兴超、刘文、戴大麦等。

<p align="center">
<img src="https://github.com/user-attachments/assets/6bf7a0ce-5fa1-46ae-9f24-cb75df607a19" />
</p>

<详情>
<summary>ℹ️<i>更多信息</i></summary>

DeepSeek-VL2 基于 LLaVA 风格的架构构建。它由三个核心模块组成：(1) 视觉编码器、(2) 视觉语言适配器和 (3) 专家混合语言模型。它引入了两个主要增强功能：动态平铺策略和使用具有多头潜在注意力的 DeepSeekMOE 语言模型。动态平铺策略通过将高分辨率图像分割成平铺来解决固定分辨率编码器的局限性。它使用单个 SigLIP-SO400M-384 视觉编码器。一组候选分辨率 CR = {(m·384, η·384) |定义m∈N,n∈N,1≤m,n,mn≤9}，代表不同的长宽比。对于输入图像，选择 CR 中最小化填充的最佳分辨率。然后，调整大小的图像被划分为 384 × 384 像素的 m₁ × n₁ 局部图块，以及一个全局缩略图图块。 SigLIP-SO400M-384 处理所有 (1 + m¡ × n₁) 图块，每个图块产生 1152 维的 729 个视觉嵌入 (27x27)。为了提高效率，对多个 (>2) 图像禁用动态平铺。 2x2 像素洗牌将每个图块的视觉标记压缩为 14x14（196 个标记）。添加特殊标记：全局缩略图中每行末尾有 14 个 <tile_newline> 标记（总共 210 个标记）； m₁ · 局部图块最后一列末尾的 14 个 <tile_newline> 标记；以及全局缩略图和局部图块之间的 <view_separator> 标记。总视觉序列长度为 210 + 1 + m₁ · 14 × (nį · 14 + 1)。该序列通过两层 MLP 投影到 LLM 的嵌入空间中。该语言模型利用 DeepSeekMoE，以多头潜在注意力 (MLA) 为特色来压缩键值 (KV) 缓存，从而提高推理速度和吞吐量。 MoE架构进一步提高了效率。 MoE 训练期间使用全局偏差术语来实现负载平衡。 DeepSeek-VL2 具有三种变体（Tiny、Small 和 Base），分别具有 1.0B、2.8B 和 4.5B 激活参数。训练数据分为三个阶段构建：(1) VL 对齐、(2) VL 预训练和 (3) 监督微调 (SFT)。对齐阶段使用 ShareGPT4V（120 万个样本）。预训练数据结合了VL和纯文本数据（70/30比例），包括交错的图文数据（WIT、WikiHow、OBELICS、万卷和内部数据）、图像字幕数据（具有质量增强和过滤的各种开源数据集）、OCR数据（LaTeX OCR、12M RenderedText和内部数据）、通用VQA数据、表格/图表/文档理解数据（PubTabNet、FinTabNet、Docmatix）、网络到代码和绘图到 Python 数据（Websight 和 Python 绘图）、带有视觉提示的 QA、视觉基础数据和基础对话数据。 SFT 数据包括增强的一般视觉问答数据、清理的 OCR 和文档理解数据、增强的表格和图表理解数据、改进的推理/逻辑/数学数据、教科书/学术问题以及扩展的网络到代码和绘图到 Python 数据、视觉基础数据、基础对话数据。 SFT 阶段使用纯文本数据集。培训方法涉及三阶段管道。第一阶段使用图像文本配对数据训练视觉编码器和视觉语言适配器 MLP，保持语言模型固定。第 2 阶段使用约 800B 图像文本标记执行视觉语言预训练，所有参数均已解锁。第三阶段进行监督微调。强调视觉理解，并且仅根据文本标记计算损失。与之前的工作不同，固定分辨率视觉编码器在训练期间进行调整。

</详情>


## **MANTIS：通过交错指令调整掌握多图像理解**

MANTIS 是一系列开源大型多模态模型，在多图像视觉语言任务上展示了最先进的性能。通过专注于使用精心策划的多图像数据集进行指令调整，MANTIS 使用比使用大量网络数据集训练的模型少得多的数据实现了卓越的结果。这种高效的方法为利用有限的资源开发强大的多图像 LMM 开辟了新途径。

[![arXiv](https://img.shields.io/badge/arXiv-2405.01483-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2405.01483) [![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/TIGER-AI-Lab/Mantis) [![Gradio](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/TIGER-Lab/Mantis)  
蒋东福、何煊、曾华野、丛伟、Max Ku、刘谦、陈文虎
<p align="center">
<img src="https://github.com/gokayfem/awesome-vlm-architectures/assets/88277926/dd4bbdf4-5ab9-4e12-89bd-94c5beb2d114" />
</p> 
<详情>
<summary>ℹ️<i>更多信息</i></summary>

**Mantis**：强大且高效的多图像大型多模态模型 (LMM)，证明对嘈杂的网络数据进行大规模预训练并不是在复杂的视觉语言任务中实现最先进性能的唯一途径。相反，MANTIS 专注于使用高质量、学术级数据进行指令调整，在各种多图像基准测试中取得了显着的结果，同时使用的数据明显少于同行。 MANTIS 成功的核心是精心策划的 MANTIS-INSTRUCT 数据集，这是一个 721K 多图像指令数据的集合，经过精心设计，旨在灌输四种关键技能：共同参考、比较、推理和时间理解。这些技能为 MANTIS 提供了一个全面的工具包，用于应对多图像理解的挑战。共同引用使模型能够理解自然语言中的“第二图像”等引用，并正确识别输入中的相应图像。比较培养了分析和识别多个图像之间细微差异和共性的能力，这是一项对于视觉相似性评估和差异描述等任务至关重要的技能。推理使模型能够超越简单的比较，通过将其世界知识与从多个图像中提取的信息相结合来做出复杂的推理，从而使其能够解决复杂的逻辑推理难题并回答具有挑战性的多图像问题。最后，时间理解使 MANTIS 能够处理和理解图像序列，捕获视频、漫画和其他时间视觉数据的动态方面。 MANTIS 利用基于现有预训练 LLM（例如 LLaMA-3）和来自 CLIP 或 SigLIP 的视觉变换器编码器的简单而有效的架构。多模式投影仪与 LLaVA 中使用的投影仪类似，可将视觉嵌入与文本嵌入对齐，从而促进它们在法学硕士中的无缝集成。这种简化的方法避免了 Q-Former 等先前架构的复杂性，同时保留了高性能。对五个多图像基准测试（包括 NLVR2、QBench、BLINK、MVBench 和新策划的 Mantis-Eval 数据集）的广泛评估证明了 MANTIS 的卓越性能，超越了现有的开源 LMM，甚至可以与强大的 GPT-4V 的结果相媲美。值得注意的是，MANTIS 超越了 Idefics2-8B（一种在 200 倍大的交错多图像数据上预训练的模型），展示了使用高质量学术级数据进行指令调整的有效性。此外，MANTIS 保留了与现有最​​先进模型相当的强大单图像性能，展示了其多功能性和适应性。 MANTIS 令人印象深刻的结果，结合其高效的训练和开源特性，为传统的大量预训练方法提供了令人信服的替代方案，为寻求以最少的计算资源开发强大且多功能的多图像 LMM 的研究人员和从业者提供了新的可能性。
</详情>

## **Qwen-VL：用于理解、本地化、文本阅读等的多功能视觉语言模型**

Qwen-VL 的独特之处在于，通过新颖的视觉语言适配器将视觉转换器与大型语言模型集成，采用交叉注意力机制来精确对齐视觉和语言数据，在各种视觉语言任务中实现高性能。

[![arXiv](https://img.shields.io/badge/arXiv-2308.12966-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2308.12966) [![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/qwenlm/qwen-vl) [![Gradio](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/Qwen/Qwen-VL-Plus)  
白金泽、白帅、杨树生、王士杰、谭思南、王鹏、林俊阳、周常、周静仁
<p align="center">
<img src="https://github.com/gokayfem/Awesome-VLM-Architectures/assets/88277926/c9358aad-63e2-44d3-b3af-38e9d4f6aeaa" />
</p> 
<详情>
<summary>ℹ️<i>更多信息</i></summary>
    
**Qwen-VL**：代表视觉语言领域的先进架构，构建在基础大型语言模型上，并集成了用于视觉编码的视觉变换器 (ViT)。该模型因其处理和对齐视觉和语言数据的创新方法而脱颖而出，具有配备交叉注意机制的**视觉语言适配器**。这些机制能够有效压缩图像特征并将其集成到语言模型中，这是实现视觉输入和文本之间精确对齐的关键组件。该架构的设计重点是优化图像特征的处理，采用位置感知策略在与文本信息合并时保持视觉数据的空间相关性。Qwen-VL 的训练方法被精心构建为**三个不同的阶段**，从对各种弱标记图像-文本对集合的**初始预训练**开始。接下来是**多任务预训练**，利用高质量的注释数据集和更大的输入分辨率来完善模型在各种任务（例如指令跟踪和对话）中的能力。最后阶段涉及**监督微调**，进一步磨练模型在一系列视觉语言任务中的性能。特殊标记和边界框输入分别用于区分图像和文本输入，并实现细粒度的视觉理解。Qwen-VL 的对齐技术是创新的，在其视觉语言适配器中采用交叉注意机制来有效融合视觉和文本特征。这种方法通过使用位置编码确保特征压缩后空间信息的保存。该模型利用广泛的数据集进行训练，包括 LAION-en、LAION-zh 和其他各种用于预训练的数据集，以及用于多任务预训练的专用数据集（如 GQA、VGQA 和 VQAv2）。这些数据集有助于支持广泛的视觉语言任务，强调多语言能力、细粒度的视觉理解以及模型在字幕、视觉问答、基础和 OCR 任务方面的熟练程度。
</详情>

## **Qwen2-VL：用于图像和视频理解的强大开源视觉语言模型**

Qwen2-VL 是 Qwen 视觉语言模型系列的最新版本，它建立在 Qwen-VL 架构的基础上，并引入了显着的增强功能，以提高对图像和视频的理解。它在各种任务中表现出色，包括视觉问答、对话、内容创建，甚至对手机和机器人等设备进行基于代理的控制。

[![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/QwenLM/Qwen2-VL) [![HuggingFace](https://img.shields.io/badge/🤗-Open%20In%20Spaces-blue.svg)](https://huggingface.co/collections/Qwen/qwen2-vl-66cee7455501d7126940800d)  
白、金泽与白、帅与杨、树生与王、世杰与谭、司南与王、彭与林、俊阳与周、常与周、景仁

<p align="center">
<img src="https://github.com/user-attachments/assets/37c2fb7a-66e1-475f-86e4-f00b4ac1c879" />
</p>

<详情>
<summary>ℹ️<i>更多信息</i></summary>

Qwen2-VL 继续利用 Qwen-VL 的核心架构，将具有约 6 亿参数的 Vision Transformer (ViT) 和 Qwen2 语言模型相结合。该 ViT 旨在无缝处理图像和视频输入。 Qwen2-VL 的关键架构改进包括朴素动态分辨率支持和多模态旋转位置嵌入 (M-ROPE)。朴素动态分辨率允许模型通过将任意图像分辨率映射到动态数量的视觉标记来处理任意图像分辨率。这确保了模型输入准确地反映图像的信息内容，无论其原始分辨率如何。这种方法更符合人类视觉感知，适应不同的图像尺寸和分辨率。 M-ROPE 增强了模型捕获多模式输入中的位置信息的能力。它将原始的旋转嵌入解构为三个部分，分别表示时间、高度和宽度信息。这使得法学硕士能够同时处理和集成 1D 文本、2D 视觉（图像）和 3D 视频位置信息，从而更全面地理解输入序列。这些架构增强与强大的训练过程相结合，使 Qwen2-VL 能够在各种视觉理解基准上实现最先进的性能，包括 MathVista、DocVQA、RealWorldQA 和 MTVQA。它还可以理解时长超过 20 分钟的视频，从而实现基于视频的高质量问答、对话和内容创作。此外，Qwen2-VL的复杂推理和决策能力使其能够与手机、机器人等设备集成，基于视觉输入和文本指令进行自动操作。该模型还支持对图像中文本的多语言理解，包括大多数欧洲语言、日语、韩语、阿拉伯语和越南语，从而扩大了其对全球用户群的适用性。
</详情>

## **Qwen2.5-VL：Qwen 系列中增强的视觉语言功能**

Qwen2.5-VL 代表了 Qwen 系列视觉语言模型的重大进步，提供改进的图像识别、精确的对象定位、增强的文本识别、文档解析和视频理解，同时还可以作为能够在计算机和手机上使用的视觉代理。

[![arXiv](https://img.shields.io/badge/Blog-Qwen%20Team%20Blog-b31b1b.svg?style=flat-square)](https://qwenlm.github.io/blog/qwen2.5-vl/)
[![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/QwenLM/Qwen2.5-VL)
[![HuggingFace](https://img.shields.io/badge/🤗-Open%20In%20Spaces-blue.svg)](https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct)  
启文团队

<p align="center">
<img src="https://github.com/user-attachments/assets/59f0878d-42c1-4013-af78-406b2f4763fe" width=600/> 
</p>

<详情>
<summary>ℹ️<i>更多信息</i></summary>

Qwen2.5-VL 建立在其前身 Qwen2-VL 的基础上，在时间和空间尺度的感知方面有了重大改进，并简化了网络结构以提高效率。 **全球图像识别：** 扩展的识别能力涵盖大量类别，包括地标、物体，甚至电影/电视 IP。 **精确的对象接地：** 使用边界框和基于点的表示进行对象定位，并使用坐标和属性的标准化 JSON 输出，从而实现分层定位。 **增强文本识别 (OCR)：** 改进了多场景、多语言、多方向的文本识别和本地化，并增强了文档处理等应用程序的信息提取。 **强大的文档解析：** 引入“QwenVL HTML”格式，利用 HTML 从文档、杂志、研究论文、网页和移动屏幕截图中提取布局信息。 **增强的视频理解：** 通过动态帧率 (FPS) 训练和绝对时间编码，支持对超长视频（每小时尺度）的理解。  实现二级事件定位和关键点总结。 **视觉代理功能：** 可以充当计算机和手机使用的视觉代理，能够推理和动态指导工具。能够完成预订航班等任务。 **时间和图像大小感知** 在空间维度上，该模型能够将不同的图像大小适应为标记，并通过检测框直接表示坐标。在时间维度上，模型可以通过时间维度来理解时间的节奏。 **视觉编码器** 原生动态分辨率 ViT 是从头开始训练的。窗口注意力用于最小化计算负载。该模型具有三种尺寸（3B、7B 和 72B 参数），提供基础版本和指令调整版本。  72B-Instruct 模型在各种基准测试中实现了具有竞争力的性能，在文档和图表理解方面表现出色。  较小的模型也表现出强大的性能，7B-Instruct 模型在多项任务中优于 GPT-4o-mini，3B 模型超过了之前的 Qwen2-VL 7B 模型的性能。这些模型使用 18 万亿个代币进行训练。未来的发展旨在进一步增强问题解决、推理和多模态集成。
</详情>

## **moondream1 和 Moondream2**

Moondream1和moondream2是视觉语言模型，其中moondream2建立在moondream1的SigLIP视觉编码器和Phi-1.5语言骨干之上，通过结合MLP投影仪来增强视觉和文本表示对齐。

[![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/vikhyat/moondream) [![Gradio](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/vikhyatk/moondream2)  
@vikhyatk
<p align="center">
<img src="https://github.com/gokayfem/awesome-vlm-architectures/assets/88277926/e979d327-3423-4a91-92f2-02a3dc3189a8" />
</p> 
<详情>
<summary>ℹ️<i>更多信息</i></summary>
  
**moondream1 和 Moondream2**：一系列视觉语言模型。 Moondream1 是一个 1.6B 参数模型，利用 **SigLIP** 作为视觉编码器和 **Phi-1.5** 作为语言主干，在 LLaVA 数据集上进行训练。 Moondream2 在此基础上进行了扩展，利用使用 SigLIP 和 Phi-1.5 的权重初始化的 1.86B 参数模型。它采用 **MLP 投影仪**来桥接视觉和文本表示，从而有可能增强视觉语言对齐并提高各种任务的性能。
</详情>

## **Moondream-next：具有增强功能的紧凑视觉语言模型**

Moondream 是一种紧凑（1.9B 参数）视觉语言模型 (VLM)，优先考虑实用性和可访问性，提供结构化输出（JSON、XML、Markdown、CSV）、改进的 OCR 和新颖的实验性凝视检测功能等功能，同时保持快速性能和易于部署。

[![arXiv](https://img.shields.io/badge/Blog-Moondream%20Blog-b31b1b.svg?style=flat-square)](https://moondream.ai/)
[![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/vikhyat/moondream)
[![HuggingFace](https://img.shields.io/badge/🤗-Open%20In%20Spaces-blue.svg)](https://huggingface.co/vikhyatk/moondream-next)


<详情>
<summary>ℹ️<i>更多信息</i></summary>

Moondream 的特点是体积特别小（1.9B 参数），同时支持较大、更专业的模型中常见的广泛功能。该架构在提供的文本中没有明确详细说明，但提到了对“视觉层”的改进，以实现更好的 OCR 性能。  这提出了一种结构，其中视觉输入由视觉编码器处理，然后与语言模型集成。  关键功能是它能够在单个统一模型中执行多个视觉 AI 任务（“功能”），包括：对象检测、字幕、视觉查询、指向（x、y 坐标检索）和新添加的凝视检测。  该模型还新支持结构化输出格式，直接生成 JSON、XML、Markdown 或 CSV 格式的输出，使与应用程序的集成变得更加容易。 “凝视检测”功能被特别强调为一项新颖的实验性功能，表明对标准基准之外的现实世界应用的关注。  尽管文本指出增加了“文档查询和理解”的培训以增强 OCR，但培训数据和过程并未得到彻底描述。该模型的创建者表达了对基准的谨慎态度，承认其局限性和操纵潜力，但也强调了此版本中改进的基准分数，表明实用性和可衡量性能之间的平衡。它不依赖外部 api。
</详情>

## **SPHINX-X：缩放一系列多模态大型语言模型的数据和参数**

SPHINX-X 通过简化其架构以使用两种视觉编码器 CLIP-ConvNeXt 和 DINOv2 来完善多模态大语言模型，并实施高效的单阶段训练过程以增强跨不同多模态任务的性能。

[![arXiv](https://img.shields.io/badge/arXiv-2402.05935-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2402.05935) [![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/alpha-vllm/llama2-accessory) [![Model](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/Alpha-VLLM/SPHINX)  
高鹏、张仁瑞、刘克里斯、邱龙天、黄思源、林伟峰、赵世田、耿世杰、林子怡、金鹏、张开鹏、邵文琪、徐超、何从辉、何军军、邵浩、潘路、李洪生、乔宇
<p align="center">
<img src="https://github.com/gokayfem/Awesome-VLM-Architectures/assets/88277926/1c4e9a86-9a21-4911-bcb6-d2a79c181510" />
</p> 
<详情>
<summary>ℹ️<i>更多信息</i></summary>
    
**SPHINX-X**：代表多模态大型语言模型 (MLLM) 开发的高级迭代，建立在其前身 SPHINX 的基础上，通过优化架构和训练效率。 SPHINX-X 中引入的核心修改包括消除冗余视觉编码器、合并**可学习的跳过标记**以绕过**完全填充的子图像**，以及将多阶段训练过程简化为单一的**一体化训练**范例。这种方法旨在提高模型在广泛的多模式任务中的效率和有效性。 SPHINX-X 的架构保留了两个关键的视觉编码器 **CLIP-ConvNeXt 和 DINOv2**，确保强大的文本图像对齐功能，特别是对于高分辨率图像和不同的宽高比。这种简化的模型架构为视觉和文本提供了统一的编码方法，强调可扩展且高效的训练方法。训练策略是全面的，直接涉及广泛的多模态数据集中的所有模型参数，其中包含涵盖语言、视觉和视觉语言任务的公共资源。此外，SPHINX-X 通过专门策划的 OCR 密集型和标记集数据集丰富了该数据集，以进一步扩展模型的多功能性和泛化能力。 SPHINX-X 中使用的数据集旨在促进跨多个领域的深入、全面的理解，增强模型在 OCR、文档布局检测和细粒度多模式理解方面的性能。通过对具有不同参数大小和多语言功能的各种基础大型语言模型 (LLM) 进行训练，SPHINX-X 实现了一系列 MLLM，这些模型展示了多模态性能与所涉及的数据和参数规模之间的强相关性。这一策略使 SPHINX-X 在多模态大语言模型性能方面树立了新的基准，显着提高了该领域处理复杂、多领域任务的能力。
</详情>

## **BLIP：引导语言-图像预训练**

BLIP 引入了多功能的编码器-解码器多模态混合 (MED) 架构，将视觉转换器和基于 BERT 的文本编码器与交叉注意力层集成在一起，从而实现跨广泛任务的统一视觉语言理解和生成。

[![arXiv](https://img.shields.io/badge/arXiv-2201.12086-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2201.12086) [![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/salesforce/BLIP)  
李俊男、李东旭、熊彩明、Steven Hoi
<p align="center">
<img src="https://github.com/gokayfem/Awesome-VLM-Architectures/assets/88277926/27db1037-2b48-4097-9891-019ba77fc536" />
</p>  
<详情>
<summary>ℹ️<i>更多信息</i></summary>
    
**BLIP**：通过其多模态混合编码器-解码器 (MED) 架构引入了一种创新方法来统一视觉语言理解和生成。该架构被设计为高度通用的，能够用作单模态编码器、基于图像的文本编码器或基于图像的文本解码器。这种灵活性使 BLIP 能够熟练地处理各种视觉语言任务，展示其在各种应用程序中的适应性。 MED 架构包含用于编码图像的 Visual Transformer、用于处理文本信息的基于 BERT 的文本编码器、用于促进图像文本交互的附加**交叉注意力层**，以及用于基于图像输入生成文本的**因果自注意力层**。这些组件使 BLIP 能够支持三个关键功能：单独模态的编码、基于图像的文本编码以及从图像中解码文本，从而涵盖从理解到生成的全面任务。BLIP 的训练方法基于三个预训练目标的联合优化：图像文本对比学习 (ITC)、图像文本匹配 (ITM) 和图像条件语言建模 (LM)。这些目标旨在分别对齐视觉和文本特征、学习细粒度的图像文本对齐以及从图像生成文本。该模型混合使用人工注释和网络收集的噪声图像文本对进行训练，平衡手动注释数据的精度与从网络收集的数据的规模和多样性。这种方法确保了 BLIP 在视觉语言任务中的性能的鲁棒性和可扩展性。为了多模态信息的对齐和融合，BLIP 采用 ITC 和 ITM 损失来实现精确的文本图像对齐，利用多模态表示来准确捕获视觉和文本数据之间的细微关系。该架构的交叉注意力层在将视觉信息合并到文本编码器以进行基于图像的文本编码方面发挥着至关重要的作用。同时，对解码器中自注意力层的修改有助于文本生成，有效地合并视觉和文本以进行统一处理。 BLIP 的预训练利用了多种数据集，包括 COCO、Visual Genome、Conceptual Captions、Conceptual 12M、SBU Captions 和 LAION。这些数据集有助于学习广泛的视觉语言任务，具有高质量的人工注释对和广泛的网络数据集，为全面的预训练提供了必要的深度和广度。
</详情>

## **BLIP-2：使用冻结图像编码器和大型语言模型引导语言图像预训练**

BLIP-2 利用冻结的预训练图像编码器和大型语言模型的强大功能，通过轻量级查询转换器 (Q-Former) 将它们连接起来，以有效提取和集成视觉特征，从而增强视觉语言理解和生成。

[![arXiv](https://img.shields.io/badge/arXiv-2301.12597-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2301.12597) [![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/salesforce/LAVIS/tree/main/projects/blip2) [![Gradio](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/Salesforce/BLIP2)  
戴文亮、李俊男、李东旭、孟发忠、赵俊奇、王伟胜、李博阳、冯柏斯、许文迪
<p align="center">
<img src="https://github.com/gokayfem/Awesome-VLM-Architectures/assets/88277926/604460f9-478c-4cc1-ba35-287447c04b26" />
</p>  
<详情>
<summary>ℹ️<i>更多信息</i></summary>
    
**BLIP-2**：模型架构集成了冻结的预训练图像编码器和大型语言模型（LLM），采用轻量级**查询转换器（Q-Former）**来促进这些模式之间的交互。 Q-Former 在提取和集成与文本查询相关的视觉特征方面发挥着至关重要的作用，从而可以根据视觉输入更细致地理解和生成语言。BLIP-2 的训练方法是围绕两阶段预训练策略构建的。最初，它专注于利用冻结图像编码器学习视觉语言表示。随后，它利用冻结的法学硕士的能力，进入视觉到语言的生成学习。该策略与 Q-Former 中可学习查询向量的使用相结合，可实现有效的视觉语言对齐。通过提取语言信息视觉表示的融合方法进一步增强对齐过程，然后将其与法学硕士的输出合成以生成相关的文本描述。包括 COCO、Visual Genome、CC3M、CC12M、SBU 和 LAION400M 在内的各种数据集支撑着 BLIP-2 的全面预训练体系。这些数据集提供了丰富多样的图像文本对，对于跨广泛的视觉表示和语言生成任务训练模型至关重要。该模型的架构和训练方法旨在解决与视觉和语言预训练相关的高昂成本，为开发多模式理解和生成能力提供更有效的途径。
</详情>

## **xGen-MM (BLIP-3)：用于构建强大且负责任的大型多模式模型的开源框架**

xGen-MM (BLIP-3) 是 Salesforce 开发的一个综合框架，用于训练一系列开源大型多模态模型 (LMM)，旨在在各种视觉语言任务中表现出色。它提供精心策划的数据集、简化的训练方案、模型架构以及一套能够执行各种视觉语言任务的开放式 LMM。 xGen-MM 专注于可扩展性，使用简化的架构和统一的训练目标来实现对更大、更多样化的数据集的训练。该框架还包括一个安全调整模型，以减少有害行为并促进负责任的人工智能开发。

[![arXiv](https://img.shields.io/badge/arXiv-2408.08872-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2408.08872) [![HuggingFace](https://img.shields.io/badge/🤗-Open%20In%20Spaces-blue.svg)](https://huggingface.co/collections/Salesforce/xgen-mm-1-models-and-datasets-662971d6cecbf3a7f80ecc2e)  
薛乐、舒曼丽、Anas Awadalla、王军、颜安、Senthil Purushwalkam、周宏禄、Viraj Prabhu、戴雨桐、Michael S Ryoo、Shrikant Kendre、张洁宇、秦灿、张舒、陈嘉智、于宁、谭俊涛、Tulika Manoj Awalgaonkar、Shelby Heinecke、王欢、Yejin Choi、Ludwig Schmidt、陈泽元、Silvio Savarese、Juan Carlos Niebles、蔡明熊、徐冉

<p align="center">
<img src="https://github.com/user-attachments/assets/e6e166c8-871e-420c-bbf1-b64c3c22e06a" />
</p>

<详情>
<summary>ℹ️<i>更多信息</i></summary>

xGen-MM (BLIP-3) 是 xGen-MultiModal 的缩写，通过为 LMM 开发提供完整的生态系统来解决以前开源工作的局限性。其方法的核心是利用多样化、大规模和高质量的多模态数据，这使得 xGen-MM 能够实现与开源和专有 LMM 相比的竞争性能。 xGen-MM 没有依赖其前身 BLIP-2 中使用的复杂 Q-Former 架构和多个训练目标，而是通过采用更具可扩展性的视觉令牌采样器（感知器重采样器）并将训练目标统一为文本令牌上的单个自回归损失来简化流程。这种简化可以实现更大规模的训练，并将模型集中于从丰富的多模态环境中有效学习。此外，xGen-MM 还融入了安全措施，引入了带有 DPO 的安全调整模型，以减轻幻觉等潜在有害行为，并促进负责任的人工智能开发。通过开源其模型、数据集和微调代码，xGen-MM 旨在增强研究社区的能力并促进 LMM 领域的进步，使这些强大的工具更易于使用，并鼓励进一步探索其功能。
</详情>

## **InstructBLIP：通过指令调整实现通用视觉语言模型**

InstructBLIP 通过向其查询转换器 (Q-Former) 引入指令调整来增强 BLIP-2 框架，使模型能够提取指令感知的视觉特征，并在不同的视觉语言任务中实现最先进的零样本性能。

[![arXiv](https://img.shields.io/badge/arXiv-2305.06500v2-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2305.06500v2) [![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/salesforce/LAVIS/tree/main/projects/instructblip) [![Gradio](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/hysts/InstructBLIP)  
戴文亮、李俊男、李东旭、孟发忠、赵俊奇、王伟胜、李博阳、冯柏斯、许文迪
<p align="center">
<img src="https://github.com/gokayfem/Awesome-VLM-Architectures/assets/88277926/5839e3a6-6fb8-469c-b84e-d60a851c1642" />
</p> 
<详情>
<summary>ℹ️<i>更多信息</i></summary>
    
**InstructBLIP**：代表了通过指令调整开发视觉语言模型的先进步骤，建立在预训练的 BLIP-2 模型的功能之上。它集成了图像编码器、大型语言模型 (LLM) 和**查询转换器 (Q-Former)**，该查询转换器经过专门微调以桥接视觉和语言组件，同时保持图像编码器和 LLM 静态。该架构能够提取指令感知的视觉特征，从而增强模型对不同教学环境的响应能力。训练 InstructBLIP 涉及仔细选择 11 个任务类别的 26 个数据集，并将其转换为指令调整格式，以培养模型在广泛的视觉语言任务中的适应性。该模型采用平衡采样策略和标准语言建模损失，并通过涉及场景文本的数据集的 OCR 标记进行增强，以微调其指令跟踪功能。通过 Q-Former 进行指令感知视觉特征提取的独特方法允许模型根据指令的特定要求定制特征提取，从而显着提高可见和不可见任务的性能。实现细节揭示了 InstructBLIP 架构的灵活性，得益于 BLIP-2 框架的模块化设计，该架构可以轻松适应各种 LLM。该模型在各种视觉语言任务中展示了最先进的零样本性能，在零样本评估中优于 BLIP-2 和 Flamingo 等之前的模型，并在对特定下游任务进行微调时取得了显着的结果。 InstructBLIP 的开源可用性及其在不同基准上的性能凸显了其作为通用视觉语言模型的潜力。
</详情>

## **KOSMOS-1：语言并不是您所需要的全部：使感知与语言模型保持一致**

KOSMOS-1 是一种多模态大语言模型，利用 MAGNETO 和 XPOS 增强的基于 Transformer 的架构来无缝处理文本和各种模态，通过对各种网络规模多模态语料库进行训练，使感知与语言模型保持一致，从而增强零样本和少样本学习能力。

[![arXiv](https://img.shields.io/badge/arXiv-2302.14045-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2302.14045) [![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/microsoft/unilm)  
黄少涵、董立、王文辉、郝雅茹、Saksham Singhal、马舒明、吕腾超、崔磊、Owais Khan Mohammed、Barun Patra、刘强、Kriti Aggarwal、Zewen Chi、Johan Bjorck、Vishrav Chaudhary、Subhojit Som、Xia Song、Furu Wei
<p align="center">
<img src="https://github.com/gokayfem/Awesome-VLM-Architectures/assets/88277926/33fd99a9-e89a-4905-8917-f03452fd5e6a" />
</p> 
<详情>
<summary>ℹ️<i>更多信息</i></summary>
    
**KOSMOS-1**：一种变革性的多模态大语言模型，经过精心设计，旨在协调一般模态的感知与语言模型，促进零样本学习、少样本学习和自回归输出生成。 KOSMOS-1 的核心采用基于 Transformer 的因果语言模型架构，擅长处理文本和各种其他模态。这种创新方法得到了关键架构组件的支持，包括用于输入序列处理的基于 Transformer 的解码器、用于文本和模态矢量编码的嵌入模块，以及用于架构增强的 **MAGNETO 和 XPOS** 的集成。这些元素共同使模型能够熟练地导航和处理多模式信息。 KOSMOS-1的训练方案的特点是综合利用网络规模的多模态语料库，其中包括单模态数据、跨模态配对数据和交错多模态数据，强调下一个令牌预测任务以优化令牌的对数似然。这种方法确保了模型的坚实基础，增强了其跨各种模式理解和生成内容的能力。此外，所采用的对齐技术尤其值得注意。通过利用交错的图像文本数据，KOSMOS-1 以前所未有的方式将一般模态的感知能力与语言模型结合起来，从而丰富了模型的理解和解释能力。 KOSMOS-1 的训练数据集（包括 The Pile、Common Crawl、英语 LAION-2B、LAION-400M、COYO-700M 和概念字幕）经过精心挑选，具有双重目的：通过文本语料库促进表征学习和语言任务，并通过图像字幕对和交错数据使感知与语言模型保持一致。这种数据集的战略选择不仅增强了模型的语言能力，而且显着增强了其小样本能力，标志着感知和语言模型集成的一个重要里程碑。
</详情>

### **KOSMOS-2：为世界奠定多模态大型语言模型的基础**

KOSMOS-2 扩展了 KOSMOS-1 架构，使用链接到文本范围的离散位置标记来合并接地图像文本对，有效地将文本锚定到特定图像区域，从而增强多模态理解和参考准确性。

[![arXiv](https://img.shields.io/badge/arXiv-2306.14824-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2306.14824) [![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/microsoft/unilm/tree/master/kosmos-2) [![Gradio](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/ydshieh/Kosmos-2)  
彭志良、王文辉、董立、郝亚茹、黄少涵、马树明、魏福如
<p align="center">
<img src="https://github.com/gokayfem/Awesome-VLM-Architectures/assets/88277926/17420c9c-759d-4690-bfc8-e8d7792111e7" />
</p> 
<详情>
<summary>ℹ️<i>更多信息</i></summary>
    
**KOSMOS-2**：建立在 KOSMOS-1 的基础架构之上，保留了基于 Transformer 的因果语言模型架构和训练目标，同时通过将基础图像文本对纳入其训练方案来引入重大创新。这一补充旨在弥合视觉和文本信息之间的差距，从而实现对多模式内容更有凝聚力的理解。该模型通过在基于图像文本对的网络规模数据集（称为 GRIT）上进行训练而脱颖而出，其中包括转换为离散位置标记的边界框的连续坐标。这些标记与文本范围错综复杂地链接在一起，创建了无缝集成视觉和文本元素的统一输入表示。 KOSMOS-2 的训练是广泛且多方面的，利用基础图像文本对、单模态文本语料库、图像标题对和交错图像文本数据来营造强大的学习环境。该模型的训练利用大批量大小并采用 AdamW 优化器，在 256 个 V100 GPU 上运行。通过使用视觉语言和纯语言指令数据集进行指令调整来增强此过程，旨在改进模型跨不同模式的理解和处理能力。接地技术是 KOSMOS-2 的关键方面，其中**边界框的连续坐标**被转换为**离散位置标记**。然后，这些标记与相应的文本范围链接，将文本输出锚定到特定的视觉输入，从而增强模型精确引用和描述特定图像区域或对象的能力。 KOSMOS-2 的对齐技术和融合方法在其直接理解和引用图像特定部分的能力方面发挥着关键作用，它采用将图像嵌入与接地文本和位置标记相结合的统一输入表示。这种方法不仅提高了模型的参考精度，而且提高了其整体多模态理解。该模型使用各种数据集进行训练，包括专门创建的用于基础功能的 GRIT 数据集，以及单模态文本语料库、图像标题对和交错的图像文本数据，以增强其语言理解、多模态感知和上下文学习能力。通过这些创新，KOSMOS-2 代表了多模式大语言模型基础上的重大进步，提供了将文本和视觉信息紧密联系起来的增强功能。
</详情>

## **ConvLLaVA：分层骨干网作为大型多模态模型的视觉编码器**

ConvLLaVA 通过将视觉变换器 (ViT) 替换为分层主干网 ConvNeXt 作为视觉编码器，解决了高分辨率大型多模态模型 (LMM) 中视觉变换器 (ViT) 的局限性。这种架构转变旨在减少由过多的视觉标记和通常与 ViT 相关的二次复杂性造成的计算负担，特别是在处理高分辨率图像时。

[![arXiv](https://img.shields.io/badge/arXiv-2405.15738-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2405.15738) [![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/alibaba/conv-llava) [![HuggingFace](https://img.shields.io/badge/🤗-Open%20In%20Spaces-blue.svg)](https://huggingface.co/papers/2405.15738)  
葛春江、程思杰、王子明、袁佳乐、高远、宋军、宋世吉、高黄、郑博

<p align="center">
<img src="https://github.com/user-attachments/assets/ad7e129a-f958-4b30-8327-7df509994bea" />
</p>

<详情>
<summary>ℹ️<i>更多信息</i></summary>

ConvLLaVA 利用分层卷积神经网络 ConvNeXt 固有的信息压缩功能。 ConvLLaVA 与依赖 ViT 的传统 LMM 不同，它采用 **五级 ConvNeXt 架构** 作为其视觉编码器。该编码器在各个阶段逐步压缩视觉信息，与 ViT 相比，显着减少了生成的视觉标记的数量。该架构反映了其他流行的通用 LMM，如 LLaVA、Qwen-VL 和 VILA，由视觉编码器 (ConvNeXt)、大型语言模型（LLM - 本例中为 Vicuna）和视觉语言投影仪（两层 MLP）组成。 ConvNeXt 编码器处理输入图像并生成潜在的视觉嵌入。然后，视觉语言投影仪将这些嵌入投影到 LLM 的嵌入空间中。最后，将投影的视觉嵌入与 LLM 的标记生成器生成的文本嵌入连接起来，并将该组合输入输入到 LLM 中。整个模型是使用语言建模损失进行训练的。为了进一步增强 ConvLLaVA 的性能，作者引入了两个关键优化：首先，他们更新了预训练的 ConvNeXt 权重而不是冻结它们，从而使模型能够适应高分辨率输入并提高视觉表示的质量。其次，他们引入了一个额外的 ConvNeXt 阶段，有效地创建了一个五阶段架构（ConvNeXt†），进一步压缩视觉信息，使模型能够处理更高的分辨率（高达 1536x1536），同时生成可管理数量的视觉标记（576）。与基于 ViT 的模型相比，这种分层压缩方法与 ConvNeXt 的线性空间复杂性相结合，显着减少了 LLM 的计算负担，使 ConvLLaVA 成为高分辨率多模态任务的更高效和可扩展的解决方案。
</详情>

## **Parrot：多语言视觉指令调整**

Parrot 解决了多模式大语言模型 (MLLM) 中的“多语言侵蚀”问题，其中主要基于以英语为中心的数据训练的模型难以理解和响应其他语言。它通过使用文本指导将视觉标记与特定于语言的嵌入对齐来实现这一目标，从而有效增强模型的多语言能力。

[![arXiv](https://img.shields.io/badge/arXiv-2406.02539-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2406.02539) [![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/AIDC-AI/Parrot)  
孙海龙、周大伟、李杨、卢世银、易超、陈庆国、徐兆、罗伟华、张开复、詹德传、叶汉佳

<p align="center">
<img src="https://github.com/user-attachments/assets/467964a0-4ccc-4cec-802a-c93b310d3118" />
</p>

<详情>
<summary>ℹ️<i>更多信息</i></summary>

Parrot 基于 LLaVA 框架构建，利用预先训练的 CLIP ViT-L/14 作为视觉编码器，使用 Qwen1.5-Chat 作为 LLM。该架构由三个主要组件组成：视觉编码器、大型语言模型 (LLM) 和多语言**专家混合 (MoE)** 模块。视觉编码器处理输入图像并生成视觉特征，然后使用学习投影仪将其投影到 LLM 的嵌入空间中。为了应对多语言挑战，Parrot 引入了一种新颖的文本引导机制。它首先计算视觉特征的类标记和从输入提示派生的文本嵌入之间的交叉注意力。然后，该交叉注意力输出被输入 MoE 模块的路由器，该路由器预测激活每个语言专家的概率。每个专家都是经过专门训练的 MLP，可以将英语偏向的视觉嵌入转换为特定于语言的表示。路由器根据输入语言选择最相关的专家，并将他们的输出组合起来生成最终的特定于语言的视觉嵌入。然后，使用加权和将这些嵌入与原始视觉嵌入相结合，确保模型保留跨不同语言有效处理视觉信息的能力。整个过程允许 Parrot 在语言级别将视觉标记与文本嵌入对齐，有效缓解多语言侵蚀并增强模型理解和响应多种语言的能力。
</详情>

## **OMG-LLaVA：桥接图像级、对象级、像素级推理和理解**

OMG-LLaVA 提出了一种新颖的框架，将图像级、对象级和像素级推理和理解统一在一个多模态大语言模型 (MLLM) 中。它利用用于视觉编码的冻结通用分段模型 (OMG-Seg) 和用于文本理解和响应生成的大型语言模型 (LLM) 的强大功能，在单个优雅的架构中实现各种多模式任务。

[![arXiv](https://img.shields.io/badge/arXiv-2406.19389-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2406.19389) [![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/lxtGH/OMG-Seg) [![HuggingFace](https://img.shields.io/badge/🤗-Open%20In%20Spaces-blue.svg)](https://huggingface.co/papers/2406.19389)  
张涛、李向太、郝飞、袁浩博、吴胜琼、季顺平、陈变来、严水成

<p align="center">
<img src="https://github.com/user-attachments/assets/c2830cc5-ab00-4c48-898e-a077cdc7b947" />
</p>

<详情>
<summary>ℹ️<i>更多信息</i></summary>

OMG-LLaVA 由两个主要组件组成：一个冻结的通用感知模块（基于 OMG-Seg）和一个大语言模型（LLM）。通用感知模块负责将输入图像和视觉提示编码为三种类型的视觉标记：以像素为中心、以对象为中心、以及从视觉提示导出的以对象为中心。以像素为中心的标记由 **ConvNeXt-L 基于 CLIP 图像编码器** 生成，捕获密集的图像特征。以对象为中心的标记由 OMG 解码器生成，该解码器将可学习的对象查询和视觉提示查询作为输入，并关注图像特征以提取对象级信息。该解码器可以通过对注意蒙版应用约束来处理点、框和蒙版提示。为了弥合冻结感知模块和法学硕士之间的差距，引入了一种新颖的“感知先验嵌入”策略。该策略使用从分割掩模和置信度分数导出的掩模分数将图像特征与来自 OMG 解码器的对象查询融合。然后将生成的加权对象查询添加到图像特征中以生成以像素为中心的视觉标记，为法学硕士提供丰富的对象级信息。以对象为中心的视觉标记直接取自 OMG 解码器的前景对象查询。两种类型的视觉标记以及文本指令标记都被输入到 LLM，LLM 负责理解用户的意图并生成适当的响应。 LLM 输出文本响应和以对象为中心的视觉标记，然后由冻结的 OMG 解码器进行解码以生成分段掩码。这种统一的架构允许 OMG-LLaVA 执行广泛的任务，包括图像字幕、视觉问答、指代分割、推理分割、基础对话生成和区域字幕，所有这些都在一个模型中完成。
</详情>

## **EVLM：一种用于视觉理解的高效视觉语言模型**

EVLM 是一种高效的多模态语言模型，旨在最大限度地降低计算成本，同时最大限度地提高模型全面感知视觉信号的能力。它通过采用交叉注意力机制和分层 ViT 特征，解决了处理长序列视觉信号（特别是视频数据）的挑战，在图像和视频字幕等任务中实现了具有竞争力的性能。

[![arXiv](https://img.shields.io/badge/arXiv-2407.14177-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2407.14177) [![HuggingFace](https://img.shields.io/badge/🤗-Open%20In%20Spaces-blue.svg)](https://huggingface.co/papers/2407.14177)  
陈凯兵、沉东、钟汉文、钟华松、夏奎、徐迪、袁伟、胡逸飞、文斌、张天科、刘昌毅、范德文、肖慧慧、吴嘉宏、杨范、李思泽、张迪

<p align="center">
<img src="https://github.com/user-attachments/assets/87563a37-e65e-44d4-a0e1-aea452ae313c" />
</p>

<详情>
<summary>ℹ️<i>更多信息</i></summary>

EVLM 基于 Flamingo 架构构建，包含视觉编码器、大型语言模型和门控交叉注意力层。为了增强视觉感知，EVLM 利用 4.4B EVA2-CLIP-E-Plus 模型作为视觉编码器，通过从 Transformer 的最后 40 层均匀采样 8 个特征序列来提取分层视觉特征。然后，这些特征被顺序输入到 Flamingo 模型的不同门控交叉注意力层中。与 Flamingo 使用单个媒体令牌图像不同，EVLM 将其替换为一组 16 个可学习令牌，旨在捕获类似于 Q-former 的视觉特征。注意机制的设计允许每组可学习标记仅与相应的图像交互，而文本序列仅与多模态序列中的前一个图像交互。这种方法确保了视觉和文本信息之间的有效交互。对于语言模型，EVLM 采用 Qwen-14B-Chat 1.0，因其在内容理解和逻辑推理方面的强大性能而被选中。在语言模型的每个转换器层之前插入门控交叉注意层，以根据视觉输入对其进行调节。为了进一步增强模型有效性并扩展可训练参数，交叉注意力层应用了专家混合（MoE）机制。这涉及到将基本模型的 FFN 复制并分割为多个细粒度的专家，并由路由层为每个令牌选择适当的专家集。该模型经历了三阶段的训练过程：多模态预训练、多任务持续预训练、多模态指令微调。预训练的重点是使用双语图像文本标题和网络类型多模态数据的大规模数据集，跨模态对齐和多模态数据内的内在关系建模。持续的预训练进一步增强了模型的视觉问答能力，而指令微调则利用各种高质量指令调优数据激活其指令跟随能力。
</详情>

## **SlowFast-LLaVA：视频大语言模型的强大免训练基线**

SlowFast-LLaVA (SF-LLaVA) 是一种免训练的视频大语言模型，可以有效捕获视频中的详细空间语义和远程时间上下文，而不需要对视频数据进行任何额外的微调。它通过利用受动作识别模型启发的双流 SlowFast 设计来实现这一目标，使其能够处理更多的帧，并在各种视频基准上优于现有的免训练方法。

[![arXiv](https://img.shields.io/badge/arXiv-2407.15841-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2407.15841) [![HuggingFace](https://img.shields.io/badge/🤗-Open%20In%20Spaces-blue.svg)](https://huggingface.co/papers/2407.15841)  
徐明泽、高明飞、甘哲、陈红友、赖正峰、刚海明、康凯、Afshin Dehghan

<p align="center">
<img src="https://github.com/user-attachments/assets/6e1e2f43-86a7-42e3-998a-24bbd8f1c741" />
</p>

<详情>
<summary>ℹ️<i>更多信息</i></summary>

SF-LLaVA 基于 LLaVA-NeXT 框架构建，并利用类似于动作识别中的 SlowFast 网络的双流方法来处理视频输入。该模型首先从输入视频中均匀采样 N 帧。然后，这些帧由视觉编码器（例如 CLIP-L）独立处理，然后由视觉语言适配器进行特征对齐。然后将生成的帧特征输入两个独立的路径：慢速和快速。 **慢速路径**专注于通过以较高的空间分辨率处理较少数量的帧（Nslow）（例如，具有 24x24 标记的 8 帧）来捕获详细的空间语义。它应用小步幅（例如 1x2）的空间池来聚合特征并减少标记的数量。 **Fast 路径** 专注于通过以较低空间分辨率（例如，具有 4x4 标记的 64 帧）处理所有 N 帧 (Nfast = N) 来捕获时间上下文和运动线索。它将积极的空间池应用于每个帧以优先考虑时间信息。然后，来自两条路径的特征被展平并连接，形成平衡空间细节和时间上下文的全面视频表示。然后，将此聚合特征向量与文本提示和问题一起输入 LLM (LLaVA-NeXT) 以生成最终答案。这种免训练的方法消除了对视频数据集进行昂贵的微调的需要，使得 SF-LLaVA 非常高效并且能够适应各种视频场景。作者在八个基准测试中展示了 SF-LLaVA 在三种不同视频问答任务（开放式视频QA、多项选择视频QA 和文本生成）上的有效性，展示了其与现有免训练方法相比的卓越性能，甚至超越了一些最先进的监督微调视频 LLM。
</详情>

## **INF-LLaVA：多模态大语言模型的高分辨率图像感知**

INF-LLaVA 是一种新颖的多模态大语言模型 (MLLM)，旨在有效处理高分辨率图像。它通过引入两个创新模块来解决现有基于裁剪和双编码器方法的局限性：双视角裁剪模块（DCM）和双视角增强模块（DEM）。 DCM 从局部和全局角度将高分辨率图像分割成子图像，保留详细信息和上下文信息。 DEM 促进局部和全局特征之间的有效交互，增强模型对复杂视觉关系的理解。广泛的评估证明了 INF-LLaVA 在各种基准上的卓越性能，在视觉语言任务中建立了新的最先进的技术。

[![arXiv](https://img.shields.io/badge/arXiv-2407.16198-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2407.16198) [![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/WeihuangLin/INF-LLaVA) [![HuggingFace](https://img.shields.io/badge/🤗-Open%20In%20Spaces-blue.svg)](https://huggingface.co/papers/2407.16198)  
马一伟、王志斌、孙小帅、林伟黄、周强、季佳怡、季蓉蓉

<p align="center">
<img src="https://github.com/user-attachments/assets/641027c4-a5eb-42e8-8486-b58f3508c553" />
</p>

<详情>
<summary>ℹ️<i>更多信息</i></summary>

INF-LLaVA 通过解决高分辨率图像感知的关键挑战，突破了多模态大型语言模型 (MLLM) 的界限。它旨在利用高分辨率图像中丰富的细节，而不会屈服于传统 MLLM 架构所施加的计算限制。 INF-LLaVA 通过一种复杂的方法实现了这一目标，该方法结合了创新的裁剪和特征增强技术，从而产生了一个能够同时捕获细粒度局部细节和全面的全球背景的模型。 INF-LLaVA 的核心是双视角裁剪模块 (DCM)，这是一种通过整合本地和全球视角超越传统方法的战略裁剪策略。这种双视角方法确保每个提取的子图像不仅保留准确分析所必需的复杂细节，而且还保留对于理解对象之间的关系至关重要的更广泛的上下文信息。局部视角裁剪以高分辨率保留连续视觉信息，捕捉单个对象和区域的本质，而全局视角裁剪则利用独特的交错技术来保留高分辨率图像中对象之间的整体空间关系。这种平衡的组合确保模型能够感知“树”和“森林”，从而实现对视觉场景的整体理解。为了进一步增强模型的理解，INF-LLaVA 引入了双视角增强模块 (DEM)。该模块促进了视觉编码器提取的局部和全局特征之间高效且有效的交互，丰富了多尺度信息的表示。 DEM 没有直接依赖于高分辨率特征上计算成本高昂的交叉注意力，而是采用了资源效率更高的策略。它利用 2D 位置先验将全局视角子图像特征连接回原始图像的形状，从而有效地重新创建全局上下文的高分辨率表示。然后从局部角度重新裁剪这些重新组合的特征，并在相应的局部和全局子图像之间进行交叉注意，以通过细粒度的局部细节增强全局特征。对称过程增强了全局背景下的局部特征。这种精心设计的局部和全局特征之间的交互确保了最终的表示不仅细节丰富，而且能够认识到更广泛的背景。然后，双重增强功能通过线性连接器投影为与 LLM 兼容的格式。然后，法学硕士处理组合的视觉和文本信息，以生成连贯且上下文相关的响应。通过对包括 ScienceQA-img、OKVQA、SEEDBench、MMBench、AI2D、LLaVA-Bench-in-the-wild 和 MMMU 在内的各种基准进行广泛评估，INF-LLaVA 展示了其优于现有 MLLM 的性能。它能够有效处理高分辨率图像，同时保持计算效率，在该领域建立了新的最先进技术。 INF-LLaVA 的开源版本及其预训练模型和代码，为进一步研究和探索多模态大语言模型中的高分辨率图像感知铺平了道路，突破了多模态理解的界限，并支持开发更强大、更通用的人工智能系统。
</详情>


## **VILA²：VILA 增强版 VILA**

VILA²（VILA-augmented-VILA）引入了一种新颖的方法来解决训练视觉语言模型（VLM）中数据数量和质量的限制。 VILA² 不依赖昂贵的人工注释或专有模型的提炼，而是利用 VLM 本身迭代地完善和增强其预训练数据，从而显着提高性能，并在开源模型中的 MMMU 排行榜上取得最先进的结果。

[![arXiv](https://img.shields.io/badge/arXiv-2407.17453-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2407.17453) [![HuggingFace](https://img.shields.io/badge/🤗-Open%20In%20Spaces-blue.svg)](https://huggingface.co/papers/2407.17453)  
方云浩、朱立庚、路遥、王彦、Pavlo Molchanov、Jang Hyun Cho、Marco Pavone、宋韩、殷红旭

<p align="center">
<img src="https://github.com/user-attachments/assets/b7602734-1163-49aa-bf78-27ae42a520bd" />
</p>

<详情>
<summary>ℹ️<i>更多信息</i></summary>

VILA² 采用两步迭代过程：自我增强和专家增强。自增强循环侧重于通过使用模型本身重新描述其预训练数据来增强 VLM 的一般知识。此过程从在数据集上训练的初始 VLM (VILA0) 开始，该数据集通常具有简短的标题，例如 COYO。然后使用 VILA0 为相同图像生成更长、更详细的标题，从而创建合成数据集。该增强数据集与原始数据相结合，用于训练 VLM (VILA1) 的下一次迭代。该循环可以重复多次，每次迭代都会提高字幕质量，进而提高 VLM 的性能。然而，这种自我增强过程最终会达到饱和。为了克服这一限制，VILA² 引入了**专家增强环**。这涉及针对特定下游任务微调自我增强的 VLM，创建具有空间感知、OCR 和接地等领域专业知识的专业 VLM。然后，这些专家被用来重新描述预训练数据，重点关注他们的特定领域知识。然后，自我增强的 VLM 会根据这些专家重述的数据进行重新训练，进一步提高其性能。这种方法利用了预训练中的大量数据和微调过程中获得的专业知识之间的协同作用。 VILA²的架构遵循标准的自回归VLM设计，由大语言模型（LLM）、视觉编码器和图像文本投影仪组成。作者使用不同的 LLM（Llama2-7B、Llama3-8B-Instruct 和 Yi-34B）和视觉编码器（SigLIP 和 InternViT-6B）进行了实验。他们还引入了视觉标记的 4 倍下采样，以降低计算成本。训练过程遵循典型的三阶段范例：投影仪初始化、视觉语言预训练和视觉指令调整。 VILA² 在各种基准测试（包括通用 VQA、面向文本的 VQA、通用多模态基准测试和图像字幕）上展示了比以前最先进的方法显着的性能改进。这凸显了所提出的自我和专家增强技术在增强 VLM 培训和实现最先进结果方面的有效性。
</详情>

## **MiniCPM-V：手机上的 GPT-4V 级别 MLLM**

MiniCPM-V 是一系列高效的多模态大型语言模型 (MLLM)，专为部署在手机和个人电脑等端侧设备上而设计。最新版本 MiniCPM-Llama3-V 2.5 实现了与 GPT-4V、Gemini Pro 和 Claude 3 相当的性能，同时体积显着更小、效率更高，证明了在资源有限的设备上部署强大的 MLLM 的可行性。

[![arXiv](https://img.shields.io/badge/arXiv-2408.01800-b31b1b.svg?style=flat-square)](https://arxiv.org/pdf/2408.01800) [![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/OpenBMB/MiniCPM-V) [![HuggingFace](https://img.shields.io/badge/🤗-Open%20In%20Spaces-blue.svg)](https://huggingface.co/openbmb/MiniCPM-V-2_6)  
姚远、于天宇、张敖、王崇义、崔俊波、朱红基、蔡天池、李浩宇、赵伟林、何志辉、陈千宇、周华荣、邹振声、张浩业、胡胜鼎、郑志、周杰、蔡杰、韩旭、曾国阳、李大海、刘志远、孙茂松

<p align="center">
<img src="https://github.com/user-attachments/assets/d943871a-ca05-46d6-9572-7fe02dda1495" />
</p>

<详情>
<summary>ℹ️<i>更多信息</i></summary>

MiniCPM-V 专注于实现性能和效率之间的平衡，这对于端侧设备上的实际应用至关重要。该模型架构由三个关键模块组成：视觉编码器、压缩层和LLM。对于视觉编码器，MiniCPM-V 采用 SigLIP SoViT-400m/14，因其效率和有效性而被选中。为了处理具有不同纵横比的高分辨率图像，该模型采用了自适应视觉编码方法。这涉及将输入图像划分为在分辨率和纵横比方面更好匹配 ViT 预训练设置的切片。使用评分函数来选择切片的最佳划分，确保与 ViT 的预训练良好匹配。然后按比例调整每个切片的大小并进行插值以适合 ViT 的输入大小。经过视觉编码后，每个切片由1024个token表示，导致多个切片的token数量较多。为了解决这个问题，采用了令牌压缩模块，使用一层交叉注意力和适量的查询来将每个切片的视觉令牌压缩为 64 或 96 个令牌。这显着降低了计算成本和内存占用，使该模型适合端侧部署。还引入了空间模式来指示每个切片相对于整个图像的位置，进一步增强模型对空间关系的理解。然后，压缩的视觉标记与文本输入一起输入 LLM，该 LLM 基于早期版本的 MiniCPM 2B 和 MiniCPM-Llama3-V 2.5 的 Llama3-Instruct 8B。训练过程包括三个阶段：预训练、监督微调和 RLAIF-V（视觉 AI 反馈强化学习）。预训练的目的是使视觉模块与法学硕士的输入空间保持一致，并学习基础的多模态知识。它涉及三个阶段：预热压缩层、扩展视觉编码器的输入分辨率以及使用自适应视觉编码策略训练视觉模块。有监督的微调利用高质量的视觉问答数据集进一步增强了模型的知识和交互能力。 SFT 数据分为两部分：一部分侧重于基本识别能力，另一部分侧重于生成详细响应和遵循指令。最后，RLAIF-V 用于缓解 MLLM 中常见的幻觉问题。这涉及为指令生成多个响应，使用分而治之策略评估其正确性，然后在偏好数据集上使用直接偏好优化 (DPO) 来优化模型。 MiniCPM-V 在各种基准测试中展示了令人印象深刻的性能，包括通用多模态基准、OCR 基准和多语言多模态交互，同时足够高效，适合在手机上部署。这突显了突破端侧 MLLM 界限并为用户设备带来强大 AI 功能的潜力。
</详情>

## **MiniCPM-o-2.6：用于视觉、语音和多模态直播的 GPT-4o 级 MLLM**

MiniCPM-o-2.6 是一款功能强大的 8B 参数多模态大语言模型 (MLLM)，在视觉、语音和多模态直播方面表现出色，在多项基准测试中实现了与 GPT-4o 相当的性能，同时保持了在边缘设备上部署的高效率。

[![arXiv](https://img.shields.io/badge/Blog-MiniCPM%20Team%20Blog-b31b1b.svg?style=flat-square)](https://openbmb.notion.site/MiniCPM-o-2-6-A-GPT-4o-Level-MLLM-for-Vision-Speech-and-Multimodal-Live-Streaming-on-Your-Phone-185ede1b7a558042b5d5e45e6b237da9)
[![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/OpenBMB/MiniCPM-o)
[![HuggingFace](https://img.shields.io/badge/🤗-Open%20In%20Spaces-blue.svg)](https://huggingface.co/openbmb/MiniCPM-o-2_6)  
开放BMB

<p align="center">
<img src="https://github.com/user-attachments/assets/cb066a40-8da7-4775-b002-7c054697f1ec" width=600/>
</p>

<详情>
<summary>ℹ️<i>更多信息</i></summary>

MiniCPM-o-2.6 采用端到端全模态架构。  它集成了多个预训练组件： **视觉编码器：** SigLip-400M **音频编码器：** Whisper-medium-300M **文本转语音 (TTS)：** ChatTTS-200M **大型语言模型 (LLM)：** Qwen2.5-7B。这些组件进行端到端连接和训练。  一个关键的创新就是“全模态直播机制”。这涉及： **在线模态编码器/解码器：** 离线编码器和解码器转换为在线版本以处理流输入和输出。 **时分复用 (TDM)：** LLM 主干内的 TDM 机制处理全模式流。它将并行流（视频、音频）划分为短时间片内的顺序信息。  **可配置的语音建模：** 多模式系统提示（包括文本和音频提示）允许在推理过程中进行灵活的语音配置，从而实现语音克隆和基于描述的语音创建。
</详情>

## **LLaVA-OneVision：轻松的视觉任务传输**

LLaVA-OneVision 是一系列开放式大型多模态模型 (LMM)，旨在在各种计算机视觉场景中表现出色，包括单图像、多图像和视频理解。它通过整合 LLaVA-NeXT 博客系列的见解，重点关注数据、模型和视觉表示，突破了开放 LMM 的性能界限。值得注意的是，LLaVA-OneVision 展示了强大的迁移学习功能，使其能够利用从图像数据中学到的知识在视频理解任务中表现出色。

[![arXiv](https://img.shields.io/badge/arXiv-2408.03326-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2408.03326) [![Website](https://img.shields.io/badge/🌐-Website-blue)](https://llava-vl.github.io/blog/2024-08-05-llava-onevision/) [![HuggingFace](https://img.shields.io/badge/🤗-Open%20In%20Spaces-blue.svg)](https://huggingface.co/papers/2408.03326)  
李博、张远涵、郭东、张仁瑞、李锋、张浩、张凯辰、李彦伟、刘子伟、李春元

<p align="center">
<img src="https://github.com/user-attachments/assets/abe36db3-571d-4068-b532-7512d4a5fcc5" />
</p>

<详情>
<summary>ℹ️<i>更多信息</i></summary>

LLaVA-OneVision继承了LLaVA系列的极简设计，旨在有效利用LLM和视觉模型的预训练能力，同时促进强大的扩展。该架构由三个关键组件组成：大型语言模型 (LLM)、视觉编码器和投影仪。作者选择 Qwen-2 作为法学硕士，因为它具有强大的语言能力和各种可用的模型大小。对于视觉编码器，他们选择了 SigLIP，事实证明，SigLIP 在开放视觉编码器中可以产生更高的 LMM 性能。使用 2 层 MLP 作为投影仪，将图像特征映射到词嵌入空间，创建一系列视觉标记。该模型采用了一种称为“Higher AnyRes”的灵活视觉表示策略，该策略建立在 LLaVA-NeXT 中引入的原始 AnyRes 策略的基础上。该策略涉及将输入图像划分为多个作物，每个作物具有适合视觉编码器的分辨率，然后应用双线性插值来减少每个作物的标记数量（如果需要）。这使得模型能够有效地处理高分辨率图像和视频，同时保留重要的视觉细节。 **Higher AnyRes**的具体配置适应不同场景：单图、多图、视频。对于单图像数据，使用较大的最大空间配置来保持原始图像分辨率，并分配大量视觉标记来有效表示视觉信号。对于多图像数据，仅考虑基础图像分辨率，无需多次裁剪并节省计算资源。对于视频数据，每帧的大小都会调整为基本图像分辨率，并使用双线性插值来减少每帧的令牌数量，从而允许处理更多的帧。培训过程遵循三阶段课程学习方法：语言图像对齐、高质量知识学习和视觉指令调整。第一阶段的重点是使用 LLaVA 对齐数据集将视觉特征与 LLM 的嵌入空间对齐。第二阶段使用来自三大类的高质量数据来细化和增强模型的知识库：重新字幕的详细描述数据、文档/OCR数据以及中文和语言数据。最后阶段涉及视觉指令调整，其中模型在具有首选响应的不同视觉任务集上进行训练。该阶段进一步分为两个阶段：单图像训练和OneVision训练。单图训练侧重于单图场景，而OneVision训练将模型的能力扩展到多图和视频场景，从而实现任务转移和新兴能力。 LLaVA-OneVision 在各种基准测试中展示了最先进的性能，包括单图像、多图像和视频任务，展示了其在处理不同视觉场景方面的有效性和多功能性。
</详情>

## **VITA：迈向开源交互式全方位多模式法学硕士**

VITA 是第一个开源多模态大型语言模型 (MLLM)，能够同时处理和分析视频、图像、文本和音频模态，同时提供先进的多模态交互体验。它通过将架构创新与高级培训和开发策略相结合，解决了现有开源模型的局限性，这些模型通常在理解或交互方面表现出色，但很少两者兼而有之。

[![arXiv](https://img.shields.io/badge/arXiv-2408.05211-b31b1b.svg?style=flat-square)](https://arxiv.org/pdf/2408.05211) [![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/VITA-MLLM/VITA) [![HuggingFace](https://img.shields.io/badge/🤗-Open%20In%20Spaces-blue.svg)](https://huggingface.co/VITA-MLLM)  
付超友、林浩佳、龙祖伟、沉云航、赵猛、张一帆、王雄、尹迪、马龙、郑夏武、何冉、季蓉蓉、吴云生、单彩凤、孙兴

<p align="center">
<img src="https://github.com/user-attachments/assets/94e2b781-0c86-47df-ac18-76ebc71bb349" />
</p>

<详情>
<summary>ℹ️<i>更多信息</i></summary>

VITA 以 Mixtral 8x7B 模型作为其语言基础，因其强大的性能和稀疏专家混合 (SMoE) 架构而被选中。为了增强中文能力，用中文术语扩展词汇量，并使用高质量的双语文本语料库对模型进行双语指令调优。这确保了中文和英文的熟练程度。对于视觉模态，VITA 采用 InternViT-300M-448px 作为视觉编码器，以 448x448 分辨率处理图像，并在通过两层 MLP 视觉连接器后生成 256 个令牌。使用动态修补策略来处理高分辨率图像，而视频则被视为图像的特殊情况，并根据视频长度进行帧采样。对于音频模态，使用 Mel Filter Bank 块来处理输入音频，然后是 4xCNN 下采样层和 24 层变压器，从而每 2 秒的音频产生 25 个令牌。两层 MLP 用作音频-文本模态连接器。训练流程由三个阶段组成：LLM 指令调优、多模态对齐和多模态指令调优。 LLM 指令调整的重点是增强基础 LLM 的双语能力。多模态对齐旨在通过为每种模态训练单独的编码器和连接器来弥合文本和其他模态之间的表示差距。这涉及收集和整理大规模、高质量的多模态数据集，包括图像描述、通用图像 QA、OCR 和图表数据、通用视频描述、通用视频 QA 和纯文本数据。多模态指令调整进一步完善了模型遵循指令和理解不同模态的能力。引入了专门设计的状态令牌来区分输入查询的类型（有效音频、噪声音频或文本），从而实现推理过程中的非唤醒交互。为了实现自然的多模态人机交互，VITA引入了两大关键创新：非唤醒交互和音频中断交互。这些是在部署期间使用双工管道实现的。两个 VITA 模型同时运行：一个用于生成对用户查询的响应（生成模型），另一个用于监视环境音频（监视模型）。监控模型使用 SileroVAD 进行语音活动检测，并根据状态令牌过滤掉噪声音频。如果检测到有效的音频查询，监控模型会中断生成模型，合并历史上下文，并响应最新的查询。然后，两个模型交换身份，确保持续监控和无缝交互。VITA 在各种单模态和多模态基准测试中展示了强大的性能，展示了其在多语言、视觉和音频理解方面强大的基础能力。虽然在某些领域仍落后于闭源同行，但 VITA 代表了迈向开源交互式全模式法学硕士的重要一步，为该领域的未来研究和开发铺平了道路。
</详情>

## **EAGLE：探索混合编码器的多模态法学硕士的设计空间**

EAGLE 是一系列开源多模态大型语言模型 (MLLM)，它利用视觉编码器的组合在各种基准上实现最先进的性能，特别是在涉及 OCR 和文档理解的任务中。该研究的重点是系统地探索具有多个视觉编码器的 MLLM 的设计空间，旨在确定最佳设计选择并提高 MLLM 感知。

[![arXiv](https://img.shields.io/badge/arXiv-2408.15998-b31b1b.svg?style=flat-square)](https://arxiv.org/pdf/2408.15998) [![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/NVlabs/EAGLE) [![HuggingFace](https://img.shields.io/badge/🤗-Open%20In%20Spaces-blue.svg)](https://huggingface.co/spaces/NVEagle/Eagle-X5-13B-Chat)  
石敏、刘福晓、王世豪、廖世佳、Subhashree Radhakrishnan、黄德安、殷宏旭、Karan Sapra、Yaser Yacoob、Humphrey Shi、Bryan Catanzaro、Andrew陶、Jan Kautz、Zhiding Yu、Guilin Liu

<p align="center">
<img src="https://github.com/user-attachments/assets/4e057a78-3fad-4a04-9a05-0f5361a8255b" />
</p>

<详情>
<summary>ℹ️<i>更多信息</i></summary>

EAGLE 基于 LLaVA 架构构建，由大型语言模型、视觉编码器和投影层组成。核心创新在于整合多个视觉专家，每个专家都针对不同的任务和分辨率进行了预训练，以增强模型感知和理解不同视觉信息的能力。该研究探索了该设计空间的各个方面，包括高分辨率适应、融合范式和最佳编码器组合。它引入了预对齐训练阶段来解决以视觉为中心的编码器和语言标记之间的表示不一致问题。训练过程包括三个渐进阶段：视觉语言预对准、联合投影仪训练和监督微调。 EAGLE 在各种基准测试中实现了最先进的性能，在 OCR 和文档理解任务中展现出显着的优势。该研究强调了系统设计空间探索的重要性，以及将多个视觉专家与简化的融合策略和预对准训练阶段相结合以构建高性能 MLLM 的有效性。
</详情>

## **Eagle 2：从头开始构建前沿视觉语言模型的训练后数据策略**

Eagle 2 是一系列视觉语言模型 (VLM)，采用以数据为中心的方法开发，专注于训练后数据策略以实现最先进的性能。这些模型建立在开源组件的基础上，并优先考虑数据多样性和质量，使用三阶段训练配方和视觉编码器平铺混合 (MoVE) 架构，实现与更大的专有模型相匹配或超越的结果。

[![arXiv](https://img.shields.io/badge/arXiv-2501.14818-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2501.14818)
[![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/NVlabs/EAGLE)
[![HuggingFace](https://img.shields.io/badge/🤗-Open%20In%20Spaces-blue.svg)](https://huggingface.co/nvidia/Eagle2-9B)  
李志琪、陈果、刘世龙、王世豪、赵一林、Subhashree Radhakrishnan、Nadine Chang、Matthieu Le、黄德安、Ilia Karmanov、Lukas Voegtle、Jose M. Alvarez、Bryan Catanzaro、Jan Kautz、Andrew陶、Vibashan VS、Yishen Ji、Shiyi Lan、Hao、Karan Sapra、Amala Deshmukh、Tuomas Rintamaki、Philipp Fischer、Timo Roman、Tong Lu、Guilin Liu、Zhiding Yu

<p align="center">
<img src="https://github.com/user-attachments/assets/e4280077-c80f-4cca-bd8f-3122a322520e" width="600"/>  <!-- Placeholder, no single architecture image -->
</p>

<详情>
<summary>ℹ️<i>更多信息</i></summary>

**Eagle 2** 采用“多样性第一，然后质量”的数据策略，从超过 180 个数据源的庞大、多样化的池开始，然后进行严格的过滤和选择。该架构使用视觉编码器 (MoVE) 的平铺混合，特别是 SigLIP 和 ConvNeXt-XXLarge，并通过图像平铺处理高分辨率。  每个图像图块均由通道级联的 MoVE 进行编码。视觉编码器输出通过简单的 MLP 连接器与 LLM (Qwen2.5) 连接和对齐。  使用三阶段训练方案：第一阶段训练连接器以对齐模式；第 1.5 阶段在大型、多样化的数据集上训练完整模型；第 2 阶段对高质量指令调整数据集进行微调。  至关重要的是，“所有”可用的视觉指令数据都用于阶段 1.5，而不仅仅是字幕/知识数据。  平衡数据打包解决了现有开源框架的限制。核心贡献是详细的数据策略。  这涉及： (1) **数据收集**：通过被动收集（监控 arXiv、HuggingFace）和主动搜索（通过错误分析解决“水桶效应”）构建高度多样化的数据池（180 多个来源）。 (2) **数据过滤**：根据不匹配的问答对、不相关的图像问题对、重复的文本和数字格式问题等标准删除低质量样本。 (3) **数据选择**：根据SSCD图像嵌入上的数据源多样性、分布和K均值聚类来选择最佳子集，以确保跨类型的平衡（对于图表数据等特别有用）。 (4) **数据增强**：通过思想链 (CoT) 解释生成、基于规则的 QA 生成以及将简短答案扩展为较长答案等技术，从输入图像中挖掘信息。 (5) **数据格式化：**去除不必要的修饰。培训采用三阶段方法：
**第 1 阶段：** 通过训练 MLP 连接器来调整语言和图像模式。
**阶段 1.5：** 使用大规模、多样化的数据集（2160 万样本）训练*完整*模型。与常见的两阶段方法不同，此处使用*所有*可用的视觉指令数据，从而带来显着的改进。
**第 2 阶段：** 在精心策划的高质量视觉指令调整数据集（460 万样本）上微调完整模型。该模型使用 AdamW 进行训练。 Eagle 2 在各种多模式基准测试中表现出强大的性能，匹配或超越前沿开源和一些闭源 VLM。
</详情>

## **Florence-2：深入探讨其统一架构和多任务功能**

Florence-2 在视觉基础模型方面取得了重大进展，旨在实现单一、多功能的表示，能够通过统一的、基于提示的方法处理广泛的视觉和视觉语言任务。与以前专门处理特定任务的模型不同，Florence-2 被设计为多面手，擅长使用简单的文本指令执行任务，类似于大型语言模型 (LLM) 的操作方式。

[![arXiv](https://img.shields.io/badge/arXiv-2311.06242-b31b1b.svg?style=flat-square)](https://arxiv.org/pdf/2311.06242) [![HuggingFace](https://img.shields.io/badge/🤗-Open%20In%20Spaces-blue.svg)](https://huggingface.co/spaces/gokaygokay/Florence-2)  
肖斌、吴海平、徐伟建、戴希阳、胡厚东、陆玉茂、曾敏、刘策、袁璐

<p align="center">
<img src="https://github.com/user-attachments/assets/f9c1f95b-ba6a-4a55-bf52-fa043b339d27" />
</p>

<详情>
<summary>ℹ️<i>更多信息</i></summary>

Florence-2 拥有一个复杂的架构，由两个关键组件组成：图像编码器和多模态编码器-解码器。图像编码器由强大的 DaViT 架构提供支持，可将输入图像转换为一系列视觉标记嵌入，从而有效捕获视觉信息。然后，这些视觉嵌入与源自特定任务提示的文本嵌入相结合。这种视觉和语言信息的融合由基于标准变压器的多模态编码器-解码器进行处理。该组件充当模型的大脑，仔细分析组合输入并以文本形式生成所需的输出。这种统一的架构具有管理各种任务的一组参数，无需进行特定于任务的修改，从而形成精简且高效的模型。这种设计理念反映了 NLP 社区的趋势，具有一致底层结构的模型因其多功能性和易于开发而受到青睐。 Florence-2 的功能涵盖多种任务，展示了其卓越的适应性。它擅长生成详细的图像标题，通过丰富的文本描述捕捉图像的本质。它的强大功能延伸到视觉基础，根据文本短语准确定位图像中的特定对象或区域。 Florence-2 在开放词汇对象检测方面也表现出了令人印象深刻的性能，可以通过名称识别对象，即使这些对象不是其训练数据的一部分。此功能突出了模型概括其知识和理解新视觉概念的能力。此外，Florence-2 还可以处理密集区域字幕，为图像中的多个区域提供详细描述，甚至执行光学字符识别 (OCR)，从图像中提取文本。这种广泛的功能使 Florence-2 成为众多应用程序的强大工具，突破了人工智能中多模态理解的界限。
</详情>

## **MULTIINSTRUCT：通过指令调优改进多模态零样本学习**

MULTIINSTRUCT 以 OFA 模型为基础，在多样化数据集上采用基于 Transformer 的序列到序列架构和指令调优技术，在统一空间内有效对齐文本和图像标记，以增强多模态零样本学习。

[![arXiv](https://img.shields.io/badge/arXiv-2212.10773-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2212.10773) [![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/vt-nlp/multiinstruct)  
徐志阳、沉颖、黄立夫
<p align="center">
<img src="https://github.com/gokayfem/Awesome-VLM-Architectures/assets/88277926/bedfc8b1-7aff-44af-b605-4470ad030bdf" />
</p> 
<详情>
<summary>ℹ️<i>更多信息</i></summary>
    
**MULTIINSTRUCT**：引入了一种新颖的方法，通过利用指令调整来增强多模态零样本学习，该方法建立在 **OFA（全能快速适配器）** 的基础上作为其核心预训练多模态模型。该模型采用基于 Transformer 的序列到序列架构，可在统一的令牌空间内有效地对指令、文本、图像和边界框的混合进行编码。这种设计使 MULTIINSTRUCT 能够通过全面的编码器-解码器框架处理和解释各种输入类型，包括可选图像。编码器组件致力于处理不同的输入和指令，而解码器的任务是生成相应的输出。 MULTIINSTRUCT 训练方法的核心是对特定于模型的 MULTIINSTRUCT 数据集的创新使用，以及合并来自多个任务的实例的指令调整技术。这种方法结合了随机洗牌和指令模板采样以进行批量训练，显着丰富了学习过程。此外，该模型利用 NATURAL INSTRUCTIONS 数据集，通过混合指令调优和顺序指令调优探索高级迁移学习策略。该策略不仅增强了模型在广泛的多模态任务中的适应性，而且还提高了其在零样本学习场景中的性能。 MULTIINSTRUCT 采用的对齐技术（例如字节对编码和 VQ-GAN）在对齐统一词汇表中的文本和图像标记方面发挥着至关重要的作用。这种无缝集成使模型能够有效地处理和解释各种类型的输入和输出。使用统一的序列到序列架构有利于视觉和语言模式的更深入集成和对齐，强调了该模型弥合不同类型数据之间差距的创新方法。用于训练和微调的数据集，即 MULTIINSTRUCT 和 NATURAL INSTRUCTIONS，经过专门选择，以增强模型处理多模态任务和指令的能力，展示其在增强多模态零样本学习方面的多功能性和有效性。
</详情>

## **MouSi：多视觉专家视觉语言模型**

MouSi 通过整合 CLIP 和 SAM 等多个视觉专家，利用多专家融合网络将其输出和接口与 Vicuna 等强大的 LLM 相结合，从而突破了 VLM 的界限，从而能够更全面地理解和处理视觉信息。

[![arXiv](https://img.shields.io/badge/arXiv-2401.17221-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2401.17221) [![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/fudannlplab/mousi)  
范晓然、季涛、姜长浩、李硕、金森杰、宋思睿、王俊科、洪博阳、陈路、郑国栋、张明、黄彩双、郑锐、奚志恒、周宇豪、窦诗涵、叶俊杰、严航、桂涛、张琪、邱锡鹏、黄轩静、吴祖轩、蒋玉刚
<p align="center">
<img src="https://github.com/gokayfem/Awesome-VLM-Architectures/assets/88277926/7e09c9d8-4c18-4970-9a24-b5e538285a72" />
</p> 
<详情>
<summary>ℹ️<i>更多信息</i></summary>
    
**MouSi**：代表了一种视觉语言模型（VLM）的创新方法，将多个视觉专家集成到一个统一的架构中，旨在超越依赖单一视觉组件的模型固有的局限性。该架构利用多专家融合网络，该网络融合了不同视觉专家的输出，例如用于图像文本匹配的 CLIP 和用于图像分割的 SAM。该网络有助于与预先训练的大型语言模型 (LLM) 建立有效的接口，特别是利用像 Vicuna v1.5 这样的模型。 MouSi 的特点是采用多专家视觉编码器，从池中选择相关专家，并具有两种类型的**多专家融合网络：投影融合方法和 Q-Former 融合方法。** MouSi 的训练方法的特点是两阶段方法。最初，在预训练阶段，纯文本 LLM 和多专家编码器都保持静态，训练重点直接放在多视觉融合网络上。随后，在微调阶段，LLM 被激活，使用高质量的监督数据集与多视觉融合网络结合进行训练。这种方法确保 MouSi 受益于强大的现有语言模型，同时增强其处理和集成复杂视觉信息的能力。为了对齐和融合多模态输入，MouSi 采用其多专家融合网络来合并各个视觉专家的输出，将它们与视觉输入标记对齐。这种对齐对于视觉和文本的紧密编码至关重要，这一过程可以通过投影融合方法或更复杂的 Q-Former 融合方法来促进。这些方法可以将多通道视觉信息有效压缩为可以与文本数据一起有效处理的格式。 MouSi 训练方案中使用的数据集包括用于预训练的 LCS-558K 和 LAION-CC-SBU 集合，旨在对齐文本和图像表示空间，以及用于微调的多样化高质量 SFT 数据集，从而增强模型在广泛的多模态任务中的性能。
</详情>

## **LaVIN：便宜且快速：针对大型语言模型的高效视觉语言指令调整**

LaVIN 通过采用混合模态适配器 (MM-Adapter) 提供了一种高效且经济高效的视觉语言指令调整方法，显着减少了可训练参数，并无需进行大量预训练即可简化法学硕士的优化过程。

[![arXiv](https://img.shields.io/badge/arXiv-2305.15023v3-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2305.15023v3) [![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/luogen1996/lavin)  
罗根、周依依、任天河、陈胜新、孙小帅、季蓉蓉
<p align="center">
<img src="https://github.com/gokayfem/Awesome-VLM-Architectures/assets/88277926/8afc8259-fa72-4e52-8080-a4ea12208e32" />
</p> 
<详情>
<summary>ℹ️<i>更多信息</i></summary>
    
**LaVIN**：该模型引入了模态混合适应（MMA）学习机制，这是一种利用**轻量级适配器**来微调视觉语言（VL）指令任务的法学硕士的开创性方法。 LaVIN 架构的核心是**混合模态适配器（MM-Adapter）**，它使用最少的适配模块将图像编码器连接到 LLM，从而允许通过相对较少的参数对多模态 LLM 进行简化优化。 LaVIN 的训练方法非常高效，采用 MMA 策略仅对插入的适配器进行微调，从而将优化参数数量显着减少到三到五百万之间。这种方法大大降低了训练时间和存储要求，避免了额外的 VL 预训练的需要。 MM-Adapter 有助于促进单模态和多模态指令之间的无缝转换，从而增强模型对各种 VL 任务的适应性。此外，它还采用动态路由功能来调整输入特征的适应性，从而实现视觉和文本嵌入的有效集成。 LaVIN 的性能和多功能性通过其在不同数据集（包括 ScienceQA、Alphaca-52k 和 LLaVA-158k）上的应用得到进一步证明。 ScienceQA 用于评估模型的多模态问答能力，而 Alphaca-52k（纯文本）和 LLaVA-158k（文本图像对）数据集则用于完善和扩展 LaVIN 作为多模态聊天机器人的功能。这种数据集的战略性使用强调了 LaVIN 先进的视觉语言理解，说明了其为多模式学习和交互领域做出重大贡献的潜力。
</详情>

## **Nous-Hermes-2-Vision - 米斯特拉尔 7B**

Nous-Hermes-2-Vision 基于 OpenHermes-2.5 构建，集成了高效的 SigLIP-400M 视觉编码器，并将自定义数据集与函数调用功能结合在一起，使其不仅能够理解视觉和文本信息，还能从图像中提取特定文本，从而提升其作为视觉语言动作模型的功能。

[![Model](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/NousResearch/Nous-Hermes-2-Vision-Alpha)  
该项目由 qnguyen3 和 teknium 领导。
<详情>
<summary>ℹ️<i>更多信息</i></summary>
    
**Nous-Hermes-2-Vision**：代表了视觉语言模型领域的显着进步，通过集成两个关键增强功能来区分其区别，从而将其功能提升到超越传统模型的水平。该模型是其前身 **OpenHermes-2.5-Mistral-7B** 的演变，并通过结合 **SigLIP-400M** 显着提高性能和效率，摆脱对大型 3B 视觉编码器的标准依赖，从而脱颖而出。此外，它还引入了一个包含函数调用功能的自定义数据集，将其转换为更动态的视觉语言动作模型。 Nous-Hermes-2-Vision 的训练使用了多样化的数据集，其中包括来自 LVIS-INSTRUCT4V 的 220K 图像、来自 ShareGPT4V 的 60K 图像、150K 私有函数调用数据以及来自 teknium 的 OpenHermes-2.5 的 50K 对话。如此多样化的数据集确保了模型能够熟练地完成广泛的视觉语言任务，包括物体识别、指令跟踪和对话理解。该模型采用集成视觉和语言的创新方法，特别是通过使用自定义数据集进行函数调用，允许以支持面向操作的任务和自动化的方式将视觉和文本编码在一起。 Nous-Hermes-2-Vision 的一个关键功能是它能够与图像交互，从视觉内容中提取有价值的文本信息，从而能够以自然语言进行详细分析和响应。该模型对 SigLIP-400M 的利用强调了这一功能，选择更轻量级、更高效的架构，同时增强视觉语言任务的性能。该模型进一步丰富了自定义数据集，其中包括**函数调用**，允许通过特定标签从图像中提取书面信息，从而扩大了开发人员和研究人员的应用范围。尽管具有创新功能，但 Nous-Hermes-2-Vision 的早期使用暴露了一些挑战，例如 EOS 代币的幻觉和垃圾邮件。认识到这些问题后，由 Quan Nguyen 和 Teknium 领导的研究团队致力于发布更新版本来解决这些问题，表明他们致力于完善模型功能。
</详情>

## **TinyGPT-V：通过小骨干的高效多模态大型语言模型**

TinyGPT-V 通过将紧凑的 EVA-ViT 视觉编码器与线性投影层和强大的 Phi-2 语言模型相结合，优先考虑多模态大语言模型的效率，尽管尺寸较小，但在视觉语言任务中实现了稳健的性能。

[![arXiv](https://img.shields.io/badge/arXiv-2312.16862v1-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2312.16862v1) [![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/DLYuanGod/TinyGPT-V) [![Gradio](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/llizhx/TinyGPT-V)  
袁正庆、李朝旭、孙立超
<p align="center">
<img src="https://github.com/gokayfem/Awesome-VLM-Architectures/assets/88277926/3e7c93bc-7963-4c2e-b207-226a03d152ca" />
</p> 
<详情>
<summary>ℹ️<i>更多信息</i></summary>
    
**TinyGPT-V**：引入了一个紧凑而强大的架构，专为高效的多模式大型语言模型应用程序而设计，利用小型主干来简化处理。该模型集成了视觉编码器，特别是 Vision Transformer (ViT) 的 EVA、**线性投影层**和 Phi-2 语言模型，构成其核心组件。视觉编码器在训练期间保持不活动状态，专注于各个阶段的图像分辨率调整以增强图像理解。 **线性投影层**，特别是结合了 BLIP-2 中的**Q-Former 层**，旨在有效地将视觉特征嵌入到语言模型中，减少需要训练的参数数量。 Phi-2大型语言模型骨干是一个拥有27亿参数的模型，在推理和语言理解方面表现出色，可通过文本边界框描述有效处理包括空间定位任务在内的视觉语言操作。 TinyGPT-V的训练分为四个阶段：预热、预训练、指令微调和多任务学习。每个阶段都经过精心设计，逐步增强模型基于视觉输入理解和生成语言的能力，特别强调后期的类人学习和对话能力。在这些阶段中使用 LAION、CC3M、SBU 等数据集支持模型在视觉语言理解、生成和任务执行（例如视觉问答和图像字幕）方面的开发。 TinyGPT-V 架构的一个值得注意的方面是规范化技术和 LoRA（低秩适应）的实施，以稳定训练并优化模型在不同模式下的性能。这些机制解决了多模态数据计算中的 NaN 或 INF 值等挑战，提高了训练的稳定性和效率。此外，该模型采用多任务指令模板来管理任务模糊性，利用 MiniGPT-v2 令牌来执行特定于任务的指令，从而促进精确、准确的任务执行。
</详情>

## **CoVLM：通过通信解码在大型语言模型中组合视觉实体和关系**

CoVLM 的独特之处在于，它使用新颖的通信令牌来实现 CLIP ViT-L 图像编码器、YOLOX 检测网络和 Pythia 语言模型之间的动态交互，从而促进复杂的通信，从而在视觉语言任务中实现卓越的组合推理。

[![arXiv](https://img.shields.io/badge/arXiv-2311.03354v1-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2311.03354v1)  
李俊艳、陈德林、洪一宁、陈振芳、陈培豪、沉义康、甘闯
<p align="center">
<img src="https://github.com/gokayfem/Awesome-VLM-Architectures/assets/88277926/80e807cb-c2cf-491a-a3b4-1223afde1981" />
</p> 
<详情>
<summary>ℹ️<i>更多信息</i></summary>
    
**CoVLM**：该模型的方法独特，采用一组新颖的**通信令牌**，促进视觉编码器、检测网络和语言模型 (LLM) 之间的动态交互。 CoVLM 的架构集成了 CLIP ViT-L 图像编码器和 YOLOX 检测网络，以及用于语言处理的预训练 Pythia 模型。这些组件协同工作，指导法学硕士在文本上下文中组合视觉实体和关系，从而增强模型与视觉编码器和检测网络动态通信的能力。 CoVLM 在多样化且广泛的图像文本数据集上进行了预训练，该数据集包含来自各种来源的 9700 万个图像文本对。这个广泛的数据集支持模型的基础管道，这对于将文本跨度与图像中相应的视觉实体相关联至关重要。该模型利用特殊的通信令牌来促进其视觉和语言组件之间的迭代通信，从而实现复杂形式的自上而下和自下而上的通信。这种通信是在视觉语言任务中实现高性能的关键，因为它允许模型在语言标记和视觉嵌入之间无缝集成和交互。预训练所使用的数据集，如 COCO、CC3M、CC12M、Visual Genome、SBU 和 LAION400M 等数据集均经过精心挑选，以增强模型有效地处理图文对的能力。这一战略选择旨在促进文本描述与其相应的视觉实体的关联，从而提高模型在一系列多模态任务中的整体性能。 CoVLM 将视觉检测网络与法学硕士集成的创新方法将组合推理提升到了一个新的水平，使其与之前的视觉语言模型区分开来。
</详情>

## **GLaMM：像素接地大型多模态模型**

GLaMM 在像素级基础方面表现出色，它利用包含全局和区域图像编码器、LLM、基础图像编码器和像素解码器的五组件架构，允许全面的视觉理解和图像内的精确对象定位。

[![arXiv](https://img.shields.io/badge/arXiv-2311.03356-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2311.03356) [![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/mbzuai-oryx/groundingLMM)  
Hanoona Rasheed、Muhammad Maaz、Sahal Shaji Mullappilly、Abdelrahman Shaker、Salman Khan、Hisham Cholakkal、Rao M. Anwer、Erix Xing、Ming-Hsuan Yang、Fahad S. Khan
<p align="center">
<img src="https://github.com/gokayfem/Awesome-VLM-Architectures/assets/88277926/ccb22206-6a48-4b77-8cc1-094fe86d72fd" />
</p> 
<详情>
<summary>ℹ️<i>更多信息</i></summary>
    
**GLaMM**：GLaMM 的核心包含五个基本组件：**全局图像编码器、区域编码器、语言模型 (LLM)、基础图像编码器和像素解码器**。该架构旨在促进与视觉内容的广泛交互，从通过全局图像编码器进行场景级理解，到通过区域编码器进行详细区域级解释，再到通过接地图像编码器进行精确的像素级对象接地。 Pixel Decoder 组件通过生成**分割蒙版**进一步丰富了模型的功能，使 GLaMM 能够以高保真度响应文本和视觉提示。 GLaMM 的训练方法涉及双途径方法，包括自动和手动数据注释管道，以创建 Grounding-anything 数据集 (GranD)。 GranD 对于模型的训练至关重要，尤其是其接地对话生成 (GCG) 任务，提供了基于 8.1 亿个区域的丰富的 750 万个独特概念，并配有分段掩模。该数据集不仅支持 GLaMM 的预训练和微调阶段，还强调了其生成与视觉刺激上下文相关的基础对话的独特能力。 GLaMM 中的对齐技术利用视觉到语言 (V-L) 投影层，促进将图像特征映射到语言空间，从而确保有效的文本图像对齐。此外，该模型采用语言到提示（L-P）投影层，将与分割相关的文本嵌入转换到解码器空间中。这种双投影系统可实现视觉和文本的集成编码，增强了 GLaMM 的像素级基础能力，并将其定位为多模式交互领域的重大进步。
</详情>

## **COSMO：具有交错预训练的对比流线型多模态模型**

COSMO 通过将 Vision Transformer 与分区大语言模型相结合，提出了一种简化的多模态框架，通过语言建模和对比损失函数的组合来优化交错数据序列的处理。

[![arXiv](https://img.shields.io/badge/arXiv-2401.00849v1-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2401.00849v1) [![GitHub](https://badges.aleen42.com/src/github.svg)](http://fingerrec.github.io/cosmo)  
Alex Jinpeng Wang、Linjie Li、Kevin Qinghong Lin、Jianfeng Wang、Kevin Lin、Zhengyuan Yang、Lijuan Wang、Mike Cheng Shou
<p align="center">
<img src="https://github.com/gokayfem/Awesome-VLM-Architectures/assets/88277926/0c256daa-1573-4110-a665-5927ee2e293f" />
</p> 
<详情>
<summary>ℹ️<i>更多信息</i></summary>
    
**COSMO**：该框架的独特之处在于其架构融合了视觉编码器，利用 Open-CLIP 的 Vision Transformer (ViT) 和分区大语言模型 (LLM)。法学硕士被系统地分为专门用于单模态文本处理和多模态数据处理的部分，旨在简化交错数据序列的整体处理。引入额外的对比损失组件作为提高分类和生成任务性能的策略脱颖而出。 COSMO 的训练是通过语言建模损失和对比损失的独特组合进行的，重点是交错文本和视觉序列的有效管理。该过程通过使用 AdamW 优化器、余弦学习率计划以及分布在 128 个 NVIDIA V100 GPU 上的 DeepSpeed fp16 精度的实现进行了优化。 LLM 划分为专用组件的策略证明了该框架对处理大量数据序列的计算效率和功效的承诺。该模型的对齐技术非常先进，具有可学习的查询，可促进所有标记的全局关注，以及对**文本融合层**的附加查询，优化模型对标记集的理解，并通过对比损失增强图像文本对齐。 **多模态融合的门控交叉注意力层**通过在输入和输出特征通道中引入瓶颈，显着减少了可学习参数。这种轻量级融合方法对于整合视觉信息以实现精确的下一个标记预测至关重要。 COSMO 的训练利用了各种数据集，包括 CC3M、SBU、LAION400M、DataComp1B、MMC4、WebVid 和 Howto-Interlink7M。 Howto-Interlink7M 的推出尤其强调了该模型通过高质量注释字幕提高视频语言理解的创新方法，展示了其在 14 个不同下游任务中的有效性。
</详情>

## **火拉瓦**

FireLLaVA 开辟了新天地，将用于高级语言理解的 CodeLlama 34B Instruct 模型与基于 CLIP-ViT 的视觉解释组件相结合，在包含边界框标签和标题的独特数据集上进行训练，以在视觉语言对话中表现出色。

[![Model](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/fireworks-ai/FireLLaVA-13b)   

<详情>
<summary>ℹ️<i>更多信息</i></summary>
    
**FireLLaVA**：作为 LLaVA 家族中的第一个同类产品，FireLLaVA 集成了双组件架构，利用 CodeLlama 34B Instruct 模型进行细致的语言理解和类似于 OpenAI 的 CLIP-ViT 的视觉解释组件。该模型的独特之处在于它使用边界框标签和标题来生成视觉语言对话，这种方法强调了其多模式训练的创新方法。 FireLLaVA 的训练方案经过精心设计，利用了 588K 行视觉问答和对话数据。该数据集将原始 LLaVA 数据与 Fireworks.ai 新生成的数据合并在一起，展示了一种独特的指令微调方法，可增强模型理解和阐明连接文本和视觉输入的响应的能力。边界框标签和标题的集成不仅可以作为生成训练数据的机制，而且还可以促进文本和图像数据的对齐，这是实现连贯的多模态理解的关键一步。尽管 FireLLaVA 架构中用于对齐融合的具体方法仍未得到描述，但可以推断嵌入融合在合成视觉和文本输入中发挥着关键作用。通过利用原始 LLaVA 培训材料和 Fireworks.ai 的专有数据，FireLLaVA 为开发能够应对商业应用复杂性的 VLM 开辟了先例。该模型体现了视觉语言建模领域的重大进步，提供了对 OSS 模型为不断发展的多模式人工智能研究和部署做出贡献的潜力的见解。
</详情>

## **u-LLaVA：通过大型语言模型统一多模态任务**

u-LLaVA 引入了一种新颖的基于投影仪的架构，通过将专门的专家模型与中央大语言模型 (LLM) 连接来统一多模态任务，从而通过两阶段训练方法实现无缝模态对齐和高效的多任务学习。

[![arXiv](https://img.shields.io/badge/arXiv-2311.05348-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2311.05348) [![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/OPPOMKLab/u-LLaVA)  
徐金金、徐立武、杨宇哲、李翔、谢艳春、黄一杰、李亚倩
<p align="center">
<img src="https://github.com/gokayfem/Awesome-VLM-Architectures/assets/88277926/dcb6b046-fa56-4a02-9123-2ef2185c635a" />
</p> 
<详情>
<summary>ℹ️<i>更多信息</i></summary>
  
**u-LLaVA**：代表了将大型语言模型 (LLM) 与专门的专家模型集成以解决各种多模式任务的开创性方法。该架构旨在利用法学硕士作为中心枢纽的优势，促进无缝模态调整和多任务学习。通过一种新颖的**基于投影仪的结构**，该结构结合了 CLIP 的 Vision Transformer (ViT-L/14) 和 LLaMA2，u-LLaVA 引入了一个能够处理不同模式和任务的灵活框架。该系统集成了用于模态和任务表达的特殊令牌，以及用于分割、接地和修复的专用模块，以丰富其多模态功能。 u-LLaVA 的训练方法分两个不同的阶段执行，从粗粒度对齐开始，以确保不同模态的表示空间对齐。这一基础步骤对于为进一步、更细致的针对特定任务的调整建立共同基础至关重要。接下来，细粒度对齐阶段的重点是细化特定于任务的指令数据，优化目标应用程序的模型性能。这种双阶段训练方法确保 u-LLaVA 能够以最少的额外训练要求有效地适应各种任务。 u-LLaVA 有效性的核心在于其创新地使用了基于投影仪的对齐技术和融合方法，从而实现了法学硕士框架内视觉和文本表示的集成。通过投影仪映射隐藏状态和文本嵌入，u-LLaVA 促进模态融合，利用法学硕士中嵌入的广泛知识来解决复杂的任务。用于训练的数据集（包括 LLaVA CC3M、Conversation-58K、Detail-23K 等）经过精心策划，以支持模型在图像字幕、视频字幕、视觉问答 (VQA)、参考表达理解 (RES)、语义分割和显着对象检测/分割等任务中的多功能功能。这种数据集的战略选择和组织强调了 u-LLaVA 通过大型语言模型推进多模式任务统一的承诺。
</详情>

## **MoE-LLaVA：大型视觉语言模型的专家组合**

MoE-LLaVA 引入了一种新颖的方法，将专家混合 (MoE) 纳入大型视觉语言模型中，使用可学习路由器有选择地激活专家模块来处理特定令牌，从而提高效率并实现对多模式输入的细致理解。

[![arXiv](https://img.shields.io/badge/arXiv-2401.15947-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2401.15947) [![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/PKU-YuanGroup/MoE-LLaVA) [![Gradio](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/LanguageBind/MoE-LLaVA)  
林斌、唐振宇、叶阳、崔家喜、朱斌、金鹏、黄金发、张俊武、宁木南、李源
<p align="center">
<img src="https://github.com/gokayfem/Awesome-VLM-Architectures/assets/88277926/0e5e214b-be64-4aac-aba4-04c97970b9de" />
</p> 
<详情>
<summary>ℹ️<i>更多信息</i></summary>
    
**MoE-LLaVA**：通过将**混合专家 (MoE)** 集成到复杂的架构框架中，代表了大型视觉语言模型开发的创新飞跃。该模型的特点是稀疏设计，其中单个令牌被定向到基于**可学习路由器**的专家选择，确保只有前 k 个专家被激活以进行任何给定令牌的处理。这种方法不仅提高了模型的效率，而且通过利用不同类型信息的专门处理路径，提高了模型处理多样化和复杂数据输入的能力。 MoE-LLaVA 架构的核心是几个关键组件，包括视觉编码器、**视觉投影 MLP 层**、**词嵌入层**、**多头自注意力块**、**前馈神经网络**，以及值得注意的是 **MoE 块**本身。这些元素通过使用层归一化和残差连接无缝集成，建立了一个强大且适应性强的框架，能够进行深入的多模态理解。 MoE-LLaVA 的训练方法精心构建为三个阶段，每个阶段都旨在逐步提高模型集成和处理视觉和文本数据的熟练程度。这包括图像标记的初始适应、除视觉编码器之外的所有 LLM 参数的训练以及 MoE 层的专门训练，后者利用前一阶段的初始化权重来实现最佳性能。 MoE-LLaVA 采用的对齐技术和融合方法对于实现文本和图像模式的和谐集成至关重要。通过利用可学习的路由器将令牌动态分配给最合适的专家，并随后通过 LLM 和 MoE 模块的组合来处理这些令牌，该模型实现了对多模式输入的细致入微的理解。整个训练阶段使用的数据集（从用于预训练的 LLaVA-PT 到用于多模态指令调整的 Hybrid-FT，以及用于微调 MoE 层的 LLaVA-FT）进一步强调了该模型在广泛的多模态任务中完善其理解的能力。这种对不同数据集的战略部署不仅有利于模型功能的全面调整，而且还强调了其在推进视觉语言处理领域的潜力。
</详情>

## **BLIVA：一个简单的多模式法学硕士，可以更好地处理文本丰富的视觉问题**

BLIVA 通过视觉助手增强了 InstructBLIP 模型，将编码的补丁嵌入与学习的查询嵌入结合起来，以增强法学硕士对文本丰富的视觉上下文的理解，从而擅长处理复杂的视觉问题。

[![arXiv](https://img.shields.io/badge/arXiv-2308.09936v3-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2308.09936v3) [![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/mlpc-ucsd/bliva)  
胡文波、徐一凡、李毅、李伟跃、陈泽元、屠卓文
<p align="center">
<img src="https://github.com/gokayfem/Awesome-VLM-Architectures/assets/88277926/44c53b8a-ad35-4eca-a68b-63af32e6ccf1" />
</p> 
<详情>
<summary>ℹ️<i>更多信息</i></summary>
    
**BLIVA**：该模型建立在 InstructBLIP 的基础上，结合了视觉助手来增强其对文本丰富的视觉上下文的理解和处理。 BLIVA 的架构旨在通过将从 InstructBLIP 学习到的查询嵌入与直接投影的编码补丁嵌入相融合，捕获查询解码过程中可能被忽视的视觉内容的复杂性。 BLIVA 的核心组件包括视觉塔，负责将视觉输入编码为补丁嵌入； **Q-former**，它优化了查询嵌入；以及连接视觉和语言领域的**投影层**，使法学硕士能够访问丰富的视觉知识。 BLIVA 的训练方法围绕两阶段方案构建：对源自字幕数据集的图像文本对进行初始预训练，然后使用视觉问答 (VQA) 数据进行指令调整。这个过程首先对用于补丁嵌入的投影层进行预训练，然后对 Q-former 和投影层进行微调，而图像编码器和 LLM 保持静态以防止灾难性遗忘。这种方法确保 BLIVA 能够很好地适应视觉信息，从而增强其处理复杂视觉问题的能力。 BLIVA 的对齐技术和融合方法因其将学习的查询嵌入与利用编码补丁嵌入的附加视觉辅助分支相集成而脱颖而出。通过连接这些嵌入并将它们直接输入到 LLM，BLIVA 显着提高了模型的文本图像视觉感知能力。这种增强的多模态理解通过使用不同的数据集得到进一步证明，包括用于预训练的图像字幕数据集、用于增强性能的指令调整 VQA 数据，以及 YTTB-VQA（YouTube 缩略图视觉问答对），以展示 BLIVA 在处理富含文本的图像方面的熟练程度及其对实际应用的适用性。
</详情>

## **MobileVLM：适用于移动设备的快速、强大且开放的视觉语言助手**

MobileVLM 提供了一种针对移动设备优化的视觉语言模型，该模型将 CLIP ViT-L/14 视觉编码器与高效的 MobileLLaMA 语言模型和轻量级下采样投影仪 (LDP) 相结合，从而在移动设备的限制内实现有效的多模态处理和对齐。

[![arXiv](https://img.shields.io/badge/arXiv-2312.16886-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2312.16886) [![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/meituan-automl/mobilevlm)  
褚香香、乔李萌、林欣阳、徐爽、杨洋、胡一鸣、魏飞、张新宇、张博、魏晓琳、沉春华
<p align="center">
<img src="https://github.com/gokayfem/Awesome-VLM-Architectures/assets/88277926/59a06109-ba49-4299-951c-d7c0c562bca3" />
</p> 
<详情>
<summary>ℹ️<i>更多信息</i></summary>
    
**MobileVLM**：引入了一个紧凑而强大的架构，旨在促进移动设备上高效的视觉语言任务，通过混合专用组件和专为边缘计算环境定制的简化培训方法而脱颖而出。 MobileVLM 的核心集成了基于分辨率为 336x336 的 CLIP ViT-L/14 模型的视觉编码器、MobileLLaMA（一种针对移动设备优化的语言模型）以及**轻量级下采样投影仪 (LDP)**，后者以最小的计算开销弥合了视觉和文本数据之间的差距。组件之间的这种协同作用确保 MobileVLM 能够有效地处理和调整多模式输入，使其非常适合资源效率至关重要的移动应用程序。 MobileVLM 的训练方案分为三个不同的阶段，每个阶段都对模型的开发做出独特的贡献。最初，语言模型使用以文本为中心的 RedPajama v1 数据集进行预训练，奠定了坚实的语言基础。随后的监督微调利用人类和 ChatGPT 之间的多轮对话，完善模型的对话能力。最后阶段涉及在不同的多模式数据集上训练集成视觉语言模型，使 MobileVLM 具备解释和响应视觉和文本刺激的能力。这种全面的训练方法确保 MobileVLM 实现性能和效率之间的平衡，使其擅长处理移动平台上复杂的视觉语言交互。 MobileVLM 有效性的核心是轻量级下采样投影仪 (LDP)，这是一种专为高效对齐视觉和文本特征而设计的新颖组件。通过采用适合移动设备的操作（例如深度卷积），LDP 能够对视觉标记进行下采样，以匹配语言模型的输入维度，保留空间信息，同时最大限度地减少计算需求。这种对齐机制与视觉和文本嵌入的有效融合相结合，使 MobileVLM 能够在移动环境中保持高水平的准确性和响应能力。通过使用精心挑选的数据集，包括用于语言预训练的 RedPajama v1 和用于综合视觉语言建模的各种多模态数据集，MobileVLM 展示了其以卓越的效率应对基于移动的视觉语言任务挑战的能力。
</详情>

## **FROZEN：使用冻结语言模型进行多模式少样本学习**

FROZEN 通过将预训练的冻结语言模型与可训练的视觉编码器 (NF-ResNet-50) 配对来实现多模态少镜头学习，该编码器将图像转换为动态视觉前缀，允许模型在视觉数据的上下文中处理和生成语言，而不改变其核心语言功能。

[![arXiv](https://img.shields.io/badge/arXiv-2106.13884-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2106.13884)  
Maria Tsimpoukelli、Jacob Menick、Serkan Cabi、S.M. Ali Eslami、Oriol Vinyals、Felix Hill
<p align="center">
<img src="https://github.com/gokayfem/Awesome-VLM-Architectures/assets/88277926/4156475d-e501-495e-98bb-66efdd5b03f7" />
</p> 
<详情>
<summary>ℹ️<i>更多信息</i></summary>
    
**FROZEN**：提出了一种创新方法，将现有语言模型的少量学习能力扩展到多模态领域，特别针对视觉和语言元素的集成，而无需更改基本语言模型参数。该方法引入了一种视觉编码器，特别是**NF-ResNet-50**，旨在将图像转换为连续的嵌入序列。这些嵌入充当基于 Transformer 架构的预训练自回归语言模型的输入的视觉前缀，使语言模型能够处理和生成与给定视觉上下文相关的内容。核心创新在于系统的模块化，这是通过保持语言模型的权重静态而**仅在训练期间更新视觉编码器**来实现的。这种方法利用概念字幕数据集，重点关注图像字幕对的对齐来训练视觉编码器，从而简化视觉数据到语言模型的集成。 FROZEN 的架构的特点是使用动态视觉前缀，这与前缀调整中典型的传统静态文本提示不同。这种动态前缀是通过将视觉编码器的输出线性映射和重塑为一系列嵌入来实现的，反映了传统语言模型调整中基于文本的前缀标记的功能。这种机制使模型能够更流畅地适应多模式输入，增强其解释和生成与视觉数据上下文一致的语言的能力。动态视觉前缀的使用是 FROZEN 能够通过上下文学习提高多模式环境中任务绩效的关键因素，为应对将视觉信息融入语言生成过程的挑战提供了一种新颖的解决方案。概念字幕数据集的利用是 FROZEN 训练方法的核心，使**视觉编码器能够熟练地将图像**转换为语言模型可以处理的格式。该数据集具有增强模型对视觉内容及其相关语言描述的理解的双重目的，从而有助于生成准确且上下文相关的字幕。静态语言模型与可训练视觉编码器的战略组合封装了 FROZEN 的多模式少样本学习方法，提供了将视觉数据集成到语言模型中的简化且有效的途径。
</详情>

## **Flamingo：用于少样本学习的视觉语言模型**

Flamingo 开创了基于感知器的 VLM 架构，该架构利用感知器重采样器和门控交叉注意力密集层，使其能够处理交错的文本和视觉序列，从而在各种多模式任务中实现令人印象深刻的几次学习性能。

[![arXiv](https://img.shields.io/badge/arXiv-2204.14198v2-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2204.14198v2)  
让-巴蒂斯特·阿雷拉克、杰夫·多纳休、宝琳·吕克、安托万·米奇、伊恩·巴尔、亚娜·哈森、卡雷尔·伦克、阿瑟·门施、凯蒂·米利肯、马尔科姆·雷诺兹、罗马·林、伊丽莎·卢瑟福、塞尔坎·卡比、韩腾达、宫志涛、西娜·萨曼古伊、玛丽安·蒙泰罗、雅各布·梅尼克、塞巴斯蒂安·博尔若、安德鲁·布洛克、阿伊达Nematzadeh、Sahand Sharifzadeh、Mikolaj Binkowski、Ricardo Barreira、Oriol Vinyals、Andrew Zisserman、Karen Simonyan
<p align="center">
<img src="https://github.com/gokayfem/Awesome-VLM-Architectures/assets/88277926/b46ebf3e-67fc-401e-a6ea-6f4797da372d" />
</p> 
<详情>
<summary>ℹ️<i>更多信息</i></summary>
    
**Flamingo**：代表视觉语言模型 (VLM) 领域的创新方法，专门设计用于在少量学习任务中表现出色。该模型的特点是能够处理与图像或视频等视觉数据交织在一起的文本标记序列，以生成文本输出。 Flamingo 架构的核心是采用基于感知器的框架，该框架能够熟练地管理高分辨率视觉输入。这种设计选择通过**感知器重采样器**将大型视觉特征图转换为简洁的视觉标记，从而能够处理复杂的多模式信息流。 Flamingo 进一步完善其架构，采用了**门控交叉注意力密集 (GATED XATTN-DENSE) 层**，这些层在根据视觉输入调节语言模型方面发挥着关键作用，从而促进基于视觉上下文的细致理解和语言生成。 Flamingo 的训练方案既广泛又多样，包含从网络上挑选的大量数据集。这包括交错图像和文本数据、图像文本对和视频文本对的丰富混合，这些数据共同有助于模型强大的少样本学习能力。 Flamingo 训练的一个独特方面是其策略是最小化给定视觉输入的每个数据集的文本预期负对数似然的加权和。这种方法与所有数据集的梯度积累策略相结合，确保从不同的多模态环境中进行全面学习。训练中使用的数据集，即 MultiModal MassiveWeb (M3W)、ALIGN 数据集、长文本和图像对 (LTIP) 以及视频和文本对 (VTP)，每个数据集都有特定的用途。 M3W 有助于对交错文本和图像数据进行训练，对图像-文本对进行 ALIGN，对高质量图像-文本对进行 LTIP，以及对视频-文本对进行 VTP，从而确保 Flamingo 能够胜任不同的视觉语言任务。在其对齐技术中，Flamingo 引入了图像因果建模方法来有效管理文本到图像的交叉注意力，允许模型有选择地关注序列中紧邻给定文本标记之前的图像的视觉标记。门控交叉注意力层进一步增强了这种能力，该层采用 tanh 门控机制将这些层的输出与残差连接的输入表示合并。这种对齐融合方法确保 Flamingo 能够无缝集成视觉和文本嵌入，强调其创新架构和训练的广度。通过这些机制，Flamingo 在整合视觉和文本数据进行语言模型训练方面取得了重大进步，展示了其在少量学习场景中的多功能性和有效性。
</详情>

## **OpenFlamingo：用于训练大型自回归视觉语言模型的开源框架**

OpenFlamingo 是 DeepMind Flamingo 的开源版本，将 CLIP ViT-L/14 视觉编码器与 7B 参数语言模型相结合，利用冻结的交叉注意力模块在解码过程中进行高效且有效的多模态融合，从而在各种视觉语言任务上取得令人印象深刻的性能。

[![arXiv](https://img.shields.io/badge/arXiv-2308.01390-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2308.01390) [![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/mlfoundations/open_flamingo)  
阿纳斯·阿瓦达拉、艾琳娜·高、乔什·加德纳、杰克·海塞尔、优素福·哈纳菲、朱万荣、卡利亚尼·马拉特、约纳坦·比顿、萨米尔·加德雷、佐川诗织、杰尼亚·吉采夫、西蒙·科恩布里斯、高庞伟、加布里埃尔·伊尔哈科、米切尔·沃茨曼、路德维希·施密特
<详情>
<summary>ℹ️<i>更多信息</i></summary>
    
**OpenFlamingo**：代表了视觉和语言模型集成方面的创新飞跃，提供了 DeepMind Flamingo 框架的开源改编。该模型的结构围绕用于编码视觉输入的 CLIP Vision Transformer Large (ViT-L/14) 和用于语言处理的 70 亿参数多模态预训练 Transformer (MPT-7B) 的强大组合。该架构的独特之处在于，它在语言模型的每四个解码器块中包含交叉注意模块，该模型在训练期间保持冻结状态。这些模块对于模型在解码过程中专注地将视觉信息与文本上下文合并的能力至关重要，从而增强其多模态理解。 OpenFlamingo 的培训方法基于利用互联网庞大数据环境的综合策略。它利用包含 LAION-2B 和 Common Crawl (C4) 数据集的多模态版本的丰富数据集组合，重点关注图像文本对序列。这种方法是通过在 64 个 A100 80GB GPU 组成的令人印象深刻的阵列上进行分布式数据并行训练来实现的，利用自动 BF16 混合精度来优化性能。该模型的对齐技术受到原始 Flamingo 设计理念的启发，该理念强调保持核心视觉和语言模型静态的重要性，同时动态训练连接的**交叉注意模块**进行解码。这种选择性的训练过程确保 OpenFlamingo 能够有效地融合视觉和文本数据，从而显着提高其根据视觉提示生成相关文本的熟练程度。此外，所使用的数据集有助于提高 OpenFlamingo 理解复杂视觉文本交互的能力。该模型专门针对图像文本序列进行了训练，在需要对视觉内容进行细致解释的任务中表现出了卓越的性能，例如字幕、视觉问答和图像分类。这种对多模态数据集的战略重点强调了该模型弥合视觉感知和语言表达之间差距的目的，标志着多模态人工智能领域的重大进步。通过这些架构创新和培训策略，OpenFlamingo 为视觉语言任务领域的开源模型设立了新标准。
</详情>

## **IDEFICS**

IDEFICS 是一种受 Flamingo 启发的 80B 参数视觉语言模型，可处理交错的图像和文本序列，利用 GPT-4 和基于 Flamingo 的架构实现强大的多模态理解，并在各种基于网络的数据集（包括专门的 OBELICS 数据集）上进行训练。

[![Model](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/HuggingFaceM4/idefics-80b)
<详情>
<summary>ℹ️<i>更多信息</i></summary>
    
**IDEFICS**：代表“800 亿个参数的视觉和语言模型”，它是一个强大的模型，旨在模仿 Flamingo 的功能，同时集成处理多模式输入方面的重大进步。该模型旨在接受图像和文本序列，生成反映对视觉和文本信息的深刻理解的文本输出。 IDEFICS 的架构建立在 GPT-4 和 Flamingo 奠定的基础上，在单一模型框架内展示了视觉和语言处理能力的和谐融合。这种战略设计使 IDEFICS 能够有效地处理和解释复杂的多模式输入，在集成视觉语言模型领域树立了新的先例。在开发过程中，IDEFICS 面临与损失峰值相关的挑战，通过回滚策略和学习率的精确调整，有效缓解了这些挑战。引入辅助 z 损失来标准化 logits，显着增强训练稳定性。该模型采用 Flamingo 的方法进行对齐，利用预先训练的视觉和语言骨干来培养细致入微的跨模式理解。尽管视觉和文本嵌入融合技术的具体细节仍处于保密状态，但推断该模型采用了类似于 Flamingo 的“交叉注意机制”，促进了视觉和文本数据的复杂集成。 IDEFICS 在 OBELICS（精心策划的交错图像文本网络文档集合）和其他网络抓取数据集上进行培训，旨在在多模式任务中表现出色。特别是 OBELICS 数据集，旨在通过提供对较长文本上下文和各种 Web 文档类型的访问来增强模型的性能。这一战略数据集选择强调了 IDEFICS 致力于提高其在一系列多模式应用程序中的熟练程度，利用网络文档中丰富多样的内容来完善其理解和输出生成能力。
</详情>

## **PaLI：联合缩放的多语言语言图像模型**

PaLI 是一种联合缩放的多语言语言图像模型，它利用统一的界面来处理单模态和多模态任务，将强大的 ViT-e 视觉编码器与基于 mT5 的文本编码器-解码器 Transformer 集成，以实现全面的语言和视觉理解。

[![arXiv](https://img.shields.io/badge/arXiv-2209.06794-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2209.06794) [![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/google-research/big_vision)  
陈曦、王晓、Lucas Beyer、Alexander Kolesnikov、吴家林、Paul Voigtlaender、Basil Mustafa、Sebastian Goodman、Ibrahim Alabdulmohsin、Piotr Padlewski、Daniel Salz、Xi Xiong、Daniel Vlasic、Filip Pavetic、Keran Rong、Tianli Yu、Daniel Keysers、Xiaohua Zhai、Radu Soricut
<p align="center">
<img src="https://github.com/gokayfem/Awesome-VLM-Architectures/assets/88277926/2565afb0-901c-4438-9488-c73a86261aa5" />
</p> 
<详情>
<summary>ℹ️<i>更多信息</i></summary>
    
**PALI**：该模型因其能够通过统一的界面处理单模态（语言或视觉）和多模态（语言和视觉一起）任务而脱颖而出，该界面接受图像和文本作为输入，随后生成文本作为输出。 PALI 的架构巧妙地将基于预先训练的 mT5 模型的文本编码器-解码器 Transformer 与由名为 ViT-e 的视觉 Transformer (ViT) 处理的视觉标记集成在一起。 ViT-e 标志着视觉处理方面的重大进步，拥有多达 40 亿个参数，为语言模型中视觉组件的集成树立了新的先例。 PALI 模型利用预先训练的单峰检查点，优化其训练过程的效率。 PALI 的训练方法稳健且多样化，融合了多种预训练任务，旨在增强模型在广泛的下游应用中的能力。利用庞大的图像语言数据集 WebLI（涵盖 100 多种语言的 100 亿张图像和文本），PALI 经历了全面的两阶段训练制度。其中包括特别关注其最大模型变体 PALI-17B 的高分辨率训练。这种方法确保 PALI 不仅是多语言的，而且非常擅长处理和理解复杂的视觉和文本数据。 PALI 采用的对齐和融合技术尤其值得注意。通过采用统一的建模接口，该模型以与任务无关的视角来处理各种任务，使其能够在不同类型的视觉和语言任务之间无缝过渡。视觉和文本的融合是通过**交叉注意机制**实现的，其中来自视觉 Transformer 的一系列视觉标记与文本编码器-解码器 Transformer 集成。该方法能够高效且有效地混合多模态信息。 WebLI、概念字幕和来自 WebLI 的 OCR 数据等数据集以及 VQ2A-CC3M 和 Open Images 等数据集的使用进一步丰富了 PALI 的培训，使其具备广泛且多功能的多模式能力。这种熟练程度涵盖多语言设置、字幕、OCR 和视觉问答 (VQA)，确保 PALI 对各种语言和任务的全面理解和生成能力。
</详情>

## **PaLI-3 视觉语言模型：更小、更快、更强**

PaLI-3 提出了一种强大而高效的视觉语言模型，它将对比预训练的 2B SigLIP 视觉模型与 3B UL2 Transformer 集成在一起，通过强调可扩展性和鲁棒性的多阶段训练过程，在字幕和视觉问答等任务中取得了令人印象深刻的性能。

[![arXiv](https://img.shields.io/badge/arXiv-2310.09199-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2310.09199) [![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/kyegomez/PALI3)  
陈曦、王晓、Lucas Beyer、Alexander Kolesnikov、吴家林、Paul Voigtlaender、Basil Mustafa、Sebastian Goodman、Ibrahim Alabdulmohsin、Piotr Padlewski、Daniel Salz、Xi Xiong、Daniel Vlasic、Filip Pavetic、Keran Rong、Tianli Yu、Daniel Keysers、Xiaohua Zhai、Radu Soricut
<p align="center">
<img src="https://github.com/gokayfem/Awesome-VLM-Architectures/assets/88277926/92d34b30-b13b-44ed-90b5-3c8568a9b634" />
</p> 
<详情>
<summary>ℹ️<i>更多信息</i></summary>
    
**PaLI-3**：其架构集成了对比预训练的 2B **SigLIP 视觉模型** 和 3B 编码器-解码器 UL2 Transformer，专注于视觉和文本数据的高效处理。 PaLI-3 的训练方法包括**图像编码器在大量图像文本数据上的对比预训练**、后续的多模态训练以及分辨率增加阶段以进一步完善其性能。这些阶段确保 PaLI-3 在 Web 规模图像文本数据、RefCOCO、WebLI、CC3M-35L 和各种 VQA 数据集等数据集的支持下，实现对视觉位置文本和对象定位的细致理解。 PaLI-3 的视觉组件利用以对比方式预训练的视觉转换器，强调效率、可扩展性和鲁棒性。这种方法允许对图像嵌入组件进行更细致的预训练，当与文本嵌入结合使用时，可以增强模型基于视觉输入理解和生成文本的能力。完整模型在 UL2 编码器-解码器框架内采用这些视觉标记以及嵌入的输入文本标记，展示了其为字幕和视觉问答 (VQA) 等任务生成文本输出的能力。 PaLI-3 的训练过程涉及几个关键阶段，首先是使用网络上的图像文本对对图像编码器进行单峰预训练。接下来是多模态训练，其中图像编码器和文本编码器-解码器被组合并在任务和数据的混合上进行训练，重点关注视觉上的文本和对象检测。分辨率增加阶段通过使用高分辨率输入微调模型来进一步增强性能。最后，任务专业化涉及在各个基准任务上微调 PaLI-3，在广泛的应用程序中优化其性能。
</详情>

## **PaLM-E：一种具体的多模态语言模型**

PaLM-E 的创新之处在于，将包括图像和传感器读数在内的连续感官数据嵌入到预先训练的 PaLM 模型的语言表示空间中，使其能够处理和生成反映物理世界的具体推理和理解的文本。

[![arXiv](https://img.shields.io/badge/arXiv-2303.03378-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2303.03378) [![GitHub](https://badges.aleen42.com/src/github.svg)](https://palm-e.github.io)  
Danny Driess、Fei Xia、Mehdi S.M. Sajjadi、Corey Lynch、Aakanksha Chowdhery、Brian Ichter、Ayzaan Wahid、Jonathan Tompson、Quan Vuong、于天河、黄文龙、Yevgen Chebotar、Pierre Sermanet、Daniel Duckworth、Sergey Levine、Vincent Vanhoucke、Karol Hausman、Marc Toussaint、Klaus格雷夫、曾安迪、伊戈尔·莫达奇、皮特·弗洛伦斯
<p align="center">
<img src="https://github.com/gokayfem/Awesome-VLM-Architectures/assets/88277926/67e5bbc7-1800-46e8-8ef1-b3b72a901a12" />
</p> 
<详情>
<summary>ℹ️<i>更多信息</i></summary>
    
**PaLM-E**：通过将连续的具体观察（从图像和状态估计到各种传感器模态）集成到预训练语言模型的语言嵌入空间中，代表了多模态语言模型开发的创新步骤。它利用仅解码器的大语言模型 (LLM) 架构，可自回归生成文本完成，并考虑多模式输入。 PaLM-E 的核心架构利用预先训练的 PaLM 作为其语言主干，并通过编码器对其进行增强，将传感器模态转换为与语言模型的嵌入维度兼容的**向量序列**。这种集成允许连续传感器信息与文本数据的无缝组合，从而制作模型处理的多模态句子。 PaLM-E 的训练方法是全面的、端到端的，利用由连续观察和文本信息组成的数据集。该模型对非前缀标记采用交叉熵损失函数，其训练方案包括用于图像特征提取的预训练视觉变换器 (ViT) 以及新颖的预训练输入编码器。该方法允许模型训练的灵活性，包括冻结预训练组件或跨不同数据集共同训练它们的选项。该策略确保 PaLM-E 受益于预训练模型的深度和针对连续数据的定制编码器的特异性。 PaLM-E 的对齐技术和融合方法对其操作至关重要，利用编码器将连续传感器数据有效地集成到语言嵌入空间中。这种集成有助于理解和生成反映文本和传感器输入混合的响应，模仿具体推理。该模型通过其**自我关注层**处理多模态句子（传感器观察和文本的交错序列），类似于处理传统文本标记的方式。这种方法确保了视觉和文本信息的一致编码。 PaLM-E 的训练利用了各种数据集，包括大规模视觉和语言数据以及专门的机器人任务数据集，旨在在广泛的具体推理任务中表现出色。这种多样化的培训背景使 PaLM-E 能够利用跨领域迁移学习，增强其在特定机器人应用和一般视觉语言任务等方面的能力。
</详情>

## **MiniGPT-4：通过高级大语言模型增强视觉语言理解**

MiniGPT-4 通过使用单个线性投影层将预训练的 Vision Transformer 和 Q-Former 连接到冻结的 Vicuna LLM，无缝地融合了视觉和语言处理，通过专注于高效对齐和增强生成质量的两阶段训练方法实现了令人印象深刻的视觉语言理解。

[![arXiv](https://img.shields.io/badge/arXiv-2304.10592v2-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2304.10592v2) [![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/vision-cair/minigpt-4)  
朱德耀、陈军、沉小倩、李翔、Mohamed Elhoseiny
<p align="center">
<img src="https://github.com/gokayfem/Awesome-VLM-Architectures/assets/88277926/0e5ff945-1271-4189-8dd9-b0abd88eacc1" />
</p> 
<详情>
<summary>ℹ️<i>更多信息</i></summary>
    
**MiniGPT-4**：通过精心设计的架构呈现视觉和语言处理功能的高级集成，该架构将冻结的视觉编码器与冻结的高级大语言模型 (LLM)（特别是 Vicuna）结合起来。 MiniGPT-4 的核心是其对齐视觉和语言模态的新颖方法：它采用**单个线性投影层**来桥接预训练的 Vision Transformer (ViT) 和 **Q-Former** 与 Vicuna LLM。这种设计选择强调了对效率的承诺，重点是利用现有的、强大的组件来实现视觉功能与复杂语言功能的无缝集成。 MiniGPT-4 的训练方法分为两个不同的阶段，优化视觉和语言特征的初始对齐以及随后生成可靠性和自然度的增强。最初，MiniGPT-4 在 4 个 A100 GPU 上进行 20,000 个步骤的训练，批量大小为 256，利用来自 Conceptual Captions、SBU 和 LAION 等来源的组合数据集来获取基础视觉语言知识。此阶段对于建立视觉编码器和 Vicuna LLM 之间的基本一致性至关重要。微调的第二阶段利用包含 3,500 个详细图像描述的精选数据集，对于完善模型输出至关重要，重点是生成更详细、可靠且自然流畅的文本。 MiniGPT-4 训练方案中数据集的战略使用强调了其双重目标：基础视觉语言对齐以及输出自然度和细节的增强。初始数据集有助于视觉和语言元素的基本集成，而详细图像描述的精选数据集可显着提高模型生成细致且准确的自然语言描述的能力。通过这种全面、分阶段的训练方法，MiniGPT-4在高效的视觉语言对齐和高质量、详细的文本输出的生成之间实现了精细的平衡，标志着视觉语言理解领域向前迈出了重要一步。
</详情>

## **MiniGPT-v2：大语言模型作为视觉语言多任务学习的统一接口**

MiniGPT-v2 通过线性投影层将静态 Visual Transformer 连接到 7B 参数 LLaMA-2-chat 语言模型，充当视觉语言多任务学习的统一接口，通过三阶段训练方法高效处理高分辨率图像并在各种任务中表现出色。

[![arXiv](https://img.shields.io/badge/arXiv-2310.09478v3-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2310.09478v3)  
陈军、朱德耀、沉小倩、李翔、刘泽春、张鹏川、Raghuraman Krishnamoorthi、Vikas Chandra、熊云阳、Mohamed Elhoseiny
<p align="center">
<img src="https://github.com/gokayfem/Awesome-VLM-Architectures/assets/88277926/2354442a-0e96-4010-8b4f-8bc3d666427e" />
</p> 
<详情>
<summary>ℹ️<i>更多信息</i></summary>
    
**MiniGPT-v2**：一种复杂的模型，旨在作为视觉语言多任务学习的统一界面，利用视觉主干与大型语言模型的创新集成。该架构的核心是将视觉变换器（ViT）作为其视觉主干，在训练过程中保持静态，并使用**线性投影层**，有效地将每四个相邻的视觉标记合并为一个。然后，这些合并的令牌被投影到 LLaMA-2-chat（一个 70 亿参数语言模型）的特征空间中，促进高分辨率图像（448x448 像素）的处理。这种结构使 MiniGPT-v2 能够有效地弥合视觉输入和语言模型处理之间的差距，满足各种视觉语言任务的需求。 MiniGPT-v2 采用的训练方法特别值得注意，它包含一个三阶段策略，全面涵盖知识获取和特定任务性能增强的范围。最初，该模型接触到弱标记和细粒度数据集的混合，重点关注广泛的视觉语言理解。培训逐渐转向更细粒度的数据，以磨练特定任务的改进。在最后阶段，MiniGPT-v2 在多模态指令和语言数据集上进行训练，旨在完善其对多模态指令的响应。在训练过程中使用特定于任务的标识符标记在减少歧义和锐化任务区分方面发挥着至关重要的作用，使模型能够熟练地应对视觉语言任务的复杂性。为了支持其广泛的训练和操作能力，MiniGPT-v2 利用了各种各样的数据集，包括 LAION、CC3M、SBU、GRIT-20M、COCO 标题等，每个数据集都被选择来完成训练过程的不同阶段——从广泛的知识获取到特定于任务的改进和复杂的多模式指令处理。这一战略数据集的使用强调了 MiniGPT-v2 在广泛的视觉语言环境中吸收和应用知识的能力，将其定位为不断发展的多任务学习界面领域中的多功能工具。
</详情>

## **LLaVA-Plus：学习使用创建多模式代理的工具**

LLaVA-Plus 通过将不同的视觉和视觉语言模型集成到技能存储库中，开创了多模式代理的创建，使代理能够通过对综合多模式指令跟踪数据的端到端培训来有效地学习和使用工具。

[![arXiv](https://img.shields.io/badge/arXiv-2311.05437-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2311.05437) [![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/LLaVA-VL/LLaVA-Plus-Codebase)  
刘世龙、程浩、刘浩天、张浩、李峰、任天和、邹雪艳、杨建伟、苏航、朱军、张雷、高剑锋、李春元
<p align="center">
<img src="https://github.com/gokayfem/Awesome-VLM-Architectures/assets/88277926/1ede1c4f-bdeb-48e0-ae8e-ccfbee1dea51" />
</p> 
<详情>
<summary>ℹ️<i>更多信息</i></summary>
    
**LLaVA-Plus**：代表多模式代理设计的创新飞跃，将各种视觉和视觉语言预训练模型集成到综合技能存储库中。这种集成使 LLaVA-Plus 能够利用端到端培训来系统地扩展其功能，使其能够根据用户的多模式输入激活和组合相关工具。 LLaVA-Plus 的架构以表示**多模态指令跟踪数据**的统一方案为中心，这对于其先进的端到端训练的多模态指令跟踪功能至关重要。该模型的特点是其训练方法，利用精心策划的多模式指令跟踪数据，涵盖广泛的任务，包括视觉理解、生成、外部知识检索及其组合。这种方法允许 LLaVA-Plus 通过指令调整来整合新工具，从而通过学习有效地使用这些工具来扩展其能力。训练数据集——COCO、HierText、InfoSeek、JourneyDB和Instruct P2P——经过精心挑选，以增强模型对视觉理解技能的训练，例如检测、分割、字幕、OCR和外部知识检索，以及生成任务和技能组合。 LLaVA-Plus 采用独特的对齐技术和融合方法，在人机交互会话期间利用原始视觉信号来提高工具使用性能、规划和推理。这些技术通过将用户输入、工具激活提示和执行结果组合成统一的对话格式，实现视觉和文本嵌入的无缝集成。这种战略方法不仅有利于增强模型与其用户之间的交互，而且还显着提高了模型在处理复杂的多模式任务时的整体性能和多功能性。
</详情>

## **巴克拉瓦**

BakLLaVA 通过采用 LLaVA 1.5 架构增强的 Mistral 7B 基础来提升 LLaVA 框架，在多样化的数据集上进行细致的两阶段训练过程，以在多模式基准测试中实现卓越的性能，超越 Llama 2 13B 等竞争对手。

[![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/skunkworksai/bakllava) [![Model](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/SkunkworksAI/BakLLaVA-1)
<详情>
<summary>ℹ️<i>更多信息</i></summary>
    
**BakLLaVA**：代表了 AI 模型领域的创新进步，与其前身 LLaVA 相比，其在架构上的显着增强使其脱颖而出。 BakLLaVA 的开发重点是将多模式功能集成到语言模型中，它利用 **Mistral 7B** 基础，并通过先进的**LLaVA 1.5 架构**进行增强，以突破各种基准测试中的性能界限。该模型经过精心设计，在多个基准测试中超越了 Llama 2 13B 等著名的前辈模型，展示了其底层架构的效率和有效性。BakLLaVA 的训练方法特别值得注意，它采用了一个特征对齐阶段，利用 600K 过滤的 CC3M 图像来建立强大的视觉语言连接。这一过程由视觉指令调整阶段进行补充，其中使用了 150K GPT 生成的多模式指令，这意味着将视觉和文本编码在一起的定制方法。这种方法不仅增强了特征对齐，还优化了模型的广泛概念覆盖范围、训练效率和整体性能。 BakLLaVA 的架构受益于多样化的数据集编译，包括来自 LAION/CC/SBU 的 558K 过滤图像文本对（以 BLIP 为标题），以及 158K GPT 生成的多模态指令跟踪数据、450K 面向学术任务的 VQA 数据和 40K ShareGPT 数据等。这种广泛的数据集收集对于模型的训练至关重要，可确保广泛的概念覆盖并增强模型在特征对齐和视觉指令调整方面的能力。数据集的战略选择强调了 BakLLaVA 致力于推进人工智能对复杂视觉和文本信息的理解和处理，为多模式人工智能模型设定新标准。
</详情>

## **CogVLM：预训练语言模型的视觉专家**

CogVLM 通过专用视觉专家模块增强预训练语言模型，在每一层中结合 QKV 矩阵和 MLP，以实现深度视觉语言特征对齐，从而在图像字幕和视觉问答等多模态任务中实现卓越性能。

[![arXiv](https://img.shields.io/badge/arXiv-2311.03079v2-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2311.03079v2) [![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/thudm/cogvlm)  
王伟瀚、吕青松、于文猛、洪文一、季奇、王彦、季俊辉、杨卓毅、赵雷、宋熙轩、徐家政、徐斌、李娟子、董宇晓、丁明、唐杰
<p align="center">
<img src="https://github.com/gokayfem/Awesome-VLM-Architectures/assets/88277926/93d951e1-ad49-47fd-9135-c11bc69d49bc" />
<details> 
<summary>ℹ️ <i>More Information</i></summary>  
    
**CogVLM**: This approach enables the model to deeply fuse vision-language features, enhancing its ability to process and understand multimodal inputs. The architecture of CogVLM is built around several key components: a Vision Transformer (ViT) encoder, **an MLP adapter**, a pretrained large language model akin to GPT, and the innovative visual expert module. These components work in tandem to facilitate the model's advanced capabilities in handling complex visual and textual information. The training methodology for CogVLM is comprehensive, encompassing both pretraining and fine-tuning phases. During pretraining, the model undergoes learning with a focus on image captioning loss and Referring Expression Comprehension (REC) across an extensive dataset comprising over 1.5 billion image-text pairs and a visual grounding dataset featuring 40 million images. The fine-tuning phase employs a unified instruction-supervised approach across a variety of visual question-answering datasets, further refining the model's performance. CogVLM's alignment techniques are particularly noteworthy, employing **a visual expert module** in each layer that leverages a **QKV (Query, Key, Value) matrix** and an **MLP (Multilayer Perceptron)** to achieve deep visual-language feature alignment. This method not only allows for the seamless integration of image features into the language model's processing layers but also significantly enhances the model's overall multimodal processing capabilities. The datasets employed in training and refining CogVLM include LAION-2B, COYO-700M, a visual grounding dataset of 40 million images, and several visual question-answering datasets like VQAv2, OKVQA, TextVQA, OCRVQA, and ScienceQA. These datasets serve multiple purposes, from pretraining and instruction alignment to enhancing the model's proficiency in tasks such as image captioning and referring expression comprehension. Through this strategic use of diverse datasets, CogVLM is positioned to excel in a wide array of multimodal tasks, marking a significant advancement in the field of vision-language models.
</details> 

## **CogVLM2: Enhanced Vision-Language Models for Image and Video Understanding**

CogVLM2 is a family of open-source visual language models designed to push the boundaries of image and video understanding. This new generation builds upon the success of previous CogVLM models, focusing on enhanced vision-language fusion, efficient high-resolution architecture, and broader modalities and applications.

[![arXiv](https://img.shields.io/badge/arXiv-2408.16500-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2408.16500) [![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/THUDM/CogVLM2) [![HuggingFace](https://img.shields.io/badge/🤗-Open%20In%20Spaces-blue.svg)](https://huggingface.co/collections/THUDM/cogvlm2-6645f36a29948b67dc4eef75)  
Wenyi Hong, Weihan Wang, Ming Ding, Wenmeng Yu, Qingsong Lv, Yan Wang, Yean Cheng, Shiyu Huang, Junhui Ji, Zhao Xue, Lei Zhao, Zhuoyi Yang, Xiaotao Gu, Xiaohan Zhang, Guanyu Feng, Da Yin, Zihan Wang, Ji Qi, Xixuan Song, Peng Zhang, Debing Liu, Bin Xu, Juanzi Li, Yuxiao Dong, Jie Tang  

<p align="center">
<img src="https://github.com/user-attachments/assets/f60247aa-66b3-486c-891c-c29cefe8aed4" />
</p>

<详情>
<summary>ℹ️<i>更多信息</i></summary>

CogVLM2 是专为全面图像和视频理解而设计的新一代视觉语言模型。它利用强大的 ViT 编码器从高分辨率图像或视频序列中提取视觉特征，然后通过卷积层进行下采样，并通过 SwiGLU 模块与语言表示对齐。该适配器有效地连接了视觉和语言模式，同时保留了关键的图像信息。然后，该模型利用视觉专家架构，将视觉特征集成到语言解码器的注意力模块和 FFN 模块中。这种方法可以实现深度视觉-语言融合，而不会损害模型固有的语言功能。值得注意的是，CogVLM2-Video 扩展了该架构来处理视频，将时间戳与多帧输入结合起来，以实现时间定位和问答功能。 CogVLM2 系列在各种基准测试中取得了最先进的结果，包括 MMBench、MM-Vet、TextVQA、MVBench 和 VCG-Bench，展示了其在各种图像和视频理解任务中的多功能性和有效性。
</详情>


## **雪貂：以任何粒度参考和接地任何地方的任何内容**

FERRET 是一种多模态大语言模型，通过使用将离散坐标与连续特征相结合的混合区域表示，在空间参考和基础方面表现出色，使其能够精确定位图像中的对象和区域，无论其复杂程度如何。

[![arXiv](https://img.shields.io/badge/arXiv-2310.07704v1-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2310.07704v1) [![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/apple/ml-ferret)  
游浩轩、张浩天、甘哲、杜宪志、张博文、王自瑞、曹亮亮、张世福、杨银飞
<p align="center">
<img src="https://github.com/gokayfem/Awesome-VLM-Architectures/assets/88277926/a5ff801f-d523-4383-8b89-e2499976b2bb" />
<details> 
<summary>ℹ️ <i>More Information</i></summary>  
    
**FERRET**: stands as a multimodal large language model (MLLM) that pioneers in spatially referring to any object within an image, irrespective of its shape or granularity, and grounding open-vocabulary descriptions with precision. The architecture of FERRET is distinguished by its hybrid region representation, which marries discrete coordinates with continuous features to depict image regions. This novel approach enables the model to handle a wide range of spatial referring tasks, from pinpointing precise locations to addressing more abstract, shapeless areas within images. At the core of FERRET's architecture are several key components: an image encoder tasked with deriving image embeddings, **a spatial-aware visual sampler** designed to extract regional continuous features, and a language model that integrates image, text, and region features. This intricate setup facilitates the model's unique ability to understand and generate language that refers to spatial elements in images with unprecedented accuracy. The training of FERRET is conducted on the GRIT dataset, which includes over 1.1 million samples imbued with hierarchical spatial knowledge. This process is augmented by spatial-aware visual sampling techniques that cater to the diverse shapes and densities found in spatial data, allowing for the simultaneous generation of text and coordinates for objects within images.FERRET's alignment techniques and fusion methods are particularly noteworthy. By blending discrete coordinates with continuous visual features, the model can process inputs of freely formed regions and ground descriptions in its outputs accurately. This capability is supported by a diverse dataset portfolio, including GRIT for its rich spatial annotations, and Visual Genome, RefCOCOs, and Flickr30k for tasks such as object detection, phrase grounding, and evaluating the model's proficiency in referring and grounding. Through these methodologies, FERRET advances the field of multimodal language models by providing a versatile framework for spatial reasoning and language grounding in visual contexts.
</details> 

## **Fuyu-8B: A Multimodal Architecture for AI Agents**

Fuyu-8B introduces a streamlined architecture for AI agents by directly projecting image patches into a decoder-only transformer, simplifying multimodal processing by treating image and text tokens uniformly, and achieving efficient performance in vision-language tasks despite its straightforward design.

[![Link](https://img.shields.io/badge/https%3A%2F%2Fwww.adept.ai%2Fblog%2Ffuyu-8b?style=flat&label=Fuyu%208B
)](https://www.adept.ai/blog/fuyu-8b) [![Model](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/adept/fuyu-8b)  
Rohan Bavishi, Erich Elsen, Curtis Hawthorne, Maxwell Nye, Augustus Odena, Arushi Somani, Sağnak Taşırlar

<p align="center">
<img src="https://github.com/gokayfem/Awesome-VLM-Architectures/assets/88277926/61a75fb4-ced7-419c-bff7-7cb2e3ddc02d" />
</p> 
<详情>
<summary>ℹ️<i>更多信息</i></summary>
    
**Fuyu-8B**：专为数字代理量身定制的简化多模式模型，以其处理视觉数据的独特方法及其与文本信息的集成而著称。 Fuyu-8B架构的核心是一个仅解码器的变压器，这与依赖单独图像编码器的传统模型不同。这种设计有助于通过**线性投影**将图像块直接投影到变压器的初始层中，从而使 Fuyu-8B 能够处理任何分辨率的图像，而不需要复杂的训练阶段或集成特定于分辨率的机制。该架构的简单性不仅在于它对图像和文本数据的统一处理，还在于它消除了对交叉注意力机制或适配器的需要，简化了模型的训练和推理过程。在对齐技术方面，Fuyu-8B 采用了一种新颖的方法，从模型处理流程的一开始就将图像标记与文本标记同等对待。该方法消除了图像的单独位置嵌入，从而简化了文本和视觉数据之间的对齐过程。该模型支持任意图像分辨率和执行细粒度定位的能力对于需要详细视觉理解和文本交互的应用程序特别有利。 Fuyu-8B 开发中使用的数据集（包括 VQAv2、OKVQA、COCO Captions 和 AI2D）有助于根据标准图像理解任务（例如视觉问答和字幕生成）对模型进行基准测试。尽管 Fuyu-8B 主要关注数字代理中的应用，但这些数据集的选择确保了对其在更广泛的图像理解和多模态交互背景下的能力进行全面评估。通过其创新的架构和简单的方法，Fuyu-8B 为能够进行复杂多模态推理的人工智能代理的开发设定了新的方向。
</详情>

## **OtterHD：高分辨率多模态模型**

OtterHD-8B 受 Fuyu-8B 启发，使用位置嵌入将高分辨率图像（高达 1024x1024 像素）的像素级信息直接集成到其语言模型中，无需单独的视觉编码器，并能够精确解释详细的视觉输入和文本指令。

[![arXiv](https://img.shields.io/badge/arXiv-2311.04219v1-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2311.04219v1) [![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/luodian/otter) [![Gradio](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/Otter-AI/OtterHD-Demo)  
李波、张培源、杨靖康、张远涵、朴繁一、刘紫薇
<详情>
<summary>ℹ️<i>更多信息</i></summary>
    
**OtterHD-8B**：代表多模态模型设计的革命性一步，建立在 **Fuyu-8B 架构**的基础上，以卓越的精度解释高分辨率视觉输入。与受固定尺寸视觉编码器限制的传统模型不同，OtterHD-8B 能够处理灵活的输入尺寸，从而增强了满足各种推理要求的多功能性。该模型将像素级视觉信息直接集成到语言模型中，无需单独的视觉编码器，采用位置嵌入来理解不同的图像尺寸，并能够处理高达 1024x1024 像素的高分辨率图像。 OtterHD-8B 中的指令调整旨在适应各种图像分辨率，模型在多种数据集混合上进行训练，包括 LLaVA-Instruct、VQAv2、GQA、OKVQA、OCRVQA、A-OKVQA、COCO-GOI、COCO-Caption、TextQA、RefCOCO、COCO-ITM、ImageNet 和 LLaVA-RLHF。该训练使用 FlashAttention-2 和其他融合算子进行优化，并利用 PyTorch 和 HuggingFace 转换器。通过位置嵌入将像素级信息直接集成到语言模型中，使 OtterHD-8B 能够理解并生成对高分辨率图像以及文本指令的响应，而无需传统的视觉和文本嵌入融合方法。选择用于训练 OtterHD-8B 的数据集强调了其对广泛的视觉和语言任务的关注，包括问答、对象识别和文本图像对齐，旨在增强模型在这些领域的能力。通过直接处理图像块和文本指令，OtterHD-8B 避开了传统的融合方法，利用其架构来解释和响应复杂的多模态输入。这种方法不仅标志着在处理高分辨率图像方面的显着进步，而且还标志着模型理解视觉和文本数据并与之交互的整体能力的显着进步，使 OtterHD-8B 成为多模态模型领域的显着发展。
</详情>

## **SPHINX：多模态大型语言模型的权重、任务和视觉嵌入的联合混合**

SPHINX 通过在训练期间联合混合模型权重、任务和视觉嵌入，利用两阶段方法在预训练期间解冻 LLM (LLaMA-2)，以增强跨模态学习，并在各种视觉语言任务上取得令人印象深刻的性能，从而突破了多模态 LLM 的界限。

[![arXiv](https://img.shields.io/badge/arXiv-2311.07575v1-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2311.07575v1) [![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/alpha-vllm/)
林子怡、克里斯·刘、张仁瑞、高鹏、邱龙天、韩晓、韩秋、陈林、邵文琪、陈克勤、韩家明、黄思源、张一驰、何旭明、李洪生、乔宇
<p align="center">
<img src="https://github.com/gokayfem/Awesome-VLM-Architectures/assets/88277926/3a1bf3fa-d0c5-4692-b9a8-97bea41ce226" />
</p> 
<详情>
<summary>ℹ️<i>更多信息</i></summary>
    
**SPHINX**：作为一种多模态大语言模型 (MLLM) 脱颖而出，旨在通过创新方法增强语言和视觉的集成，其中包括**模型权重的联合混合**、调整任务和视觉嵌入。该模型的特别之处在于其在预训练期间解冻大型语言模型的方法，以促进更有效的跨模态学习。 SPHINX 的架构建立在结合视觉编码器、**两个线性投影层**的基础上，并利用 LLaMA-2 作为语言模型主干。它采用两阶段训练范式，强调视觉语言对齐的预训练，然后针对视觉指令跟踪任务进行微调。在训练方法领域，SPHINX 采用的策略强调**模型权重**、调整任务和视觉嵌入的联合混合，为稳健的跨模态知识获取开创了先例。这种方法辅以利用现实世界和合成数据的预训练方案，从而确保对各种视觉指令任务的全面理解。该模型引入了一种处理高分辨率图像的有效策略，利用混合尺度和子图像来适应不同的视觉输入。此外，SPHINX 通过集成全面的视觉嵌入、在预训练期间解冻 LLM 以及采用权重混合策略来跨不同网络架构和训练范例桥接特定领域的知识，从而实现视觉语言对齐。训练 SPHINX 时使用的数据集包括 LAION-400M、LAION-COCO、RefinedWeb、VQAV2、GQA、OKVQA、A-OKVQA、OCRVQA、TextCaps、COCO、LVIS、RefCOCO、VG 和 Flickr30k，具有多种用途。它们有助于实现多模式对齐、仅语言调整以及解决广泛的视觉问答和一般视觉任务。这些任务的范围从对象检测和人体姿势估计到参考对象定位和理解图像区域上下文中的描述。 SPHINX通过精心设计和战略训练方法，在多模态大语言模型领域树立了新标杆，提升了视觉语言融合能力。
</详情>

## **CLIP：对比语言-图像预训练**

CLIP 利用对比学习方法，在 4 亿图像文本对的海量数据集上训练单独的图像和文本编码器，以预测最相关的图像标题，从而为各种下游任务提供令人印象深刻的零样本传输能力，而无需特定于任务的训练数据。

[![arXiv](https://img.shields.io/badge/arXiv-2103.00020-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2103.00020) [![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/openai/CLIP)  
亚历克·雷德福、金钟旭、克里斯·哈拉西、阿迪亚·拉梅什、加布里埃尔·吴、桑迪尼·阿加瓦尔、吉里什·萨斯特里、阿曼达·阿斯克尔、帕梅拉·米什金、杰克·克拉克、格雷琴·克鲁格、伊利亚·苏茨克维尔
<p align="center">
<img src="https://github.com/gokayfem/Awesome-VLM-Architectures/assets/88277926/c335c342-9a2c-4d4e-83d6-d3077cc32643" />
</p> 
<详情>
<summary>ℹ️<i>更多信息</i></summary>
    
**CLIP**：模型代表了机器学习领域的突破性方法，旨在通过自然语言监督弥合视觉和文本信息之间的差距。其架构旨在理解和预测**给定图像最合适的标题**，这种方法源于对 4 亿图像文本对的庞大数据集的训练。这种广泛的训练使 CLIP 能够学习最先进的 (SOTA) 图像表示，并将这些知识应用于广泛的下游任务，而无需特定于任务的训练数据，从而促进零样本传输能力。 CLIP 的核心有两个主要组件：**图像编码器**和**文本编码器**。这些编码器使用对比学习方法进行训练，针对对比目标进行优化，旨在最大化正确图像文本对之间的余弦相似度，同时最小化错误图像文本对之间的余弦相似度。这个过程是通过**图像和文本嵌入之间的相似性分数的对称交叉熵损失**来实现的，使模型能够有效地将视觉概念与其语言描述联系起来。该模型泛化各种任务的能力通过其训练方法和所使用的特定数据集进一步增强。通过涵盖广泛的视觉概念并利用自然语言进行监督，CLIP 擅长学习可高度迁移到新任务和领域的表示。来自互联网的 4 亿图像文本对的自定义数据集在此过程中发挥着关键作用，为模型有效学习提供了所需的多样化且广泛的视觉和文本信息。通过这些创新，CLIP 为学习可迁移视觉模型设立了新标准，展示了自然语言在促进稳健和多功能视觉理解方面的力量。
</详情>

## **MetaCLIP：揭秘 CLIP 数据**

MetaCLIP 通过采用利用 CLIP 派生元数据的算法，从 CommonCrawl 等大量来源创建平衡且高质量的数据集，从而改进了训练视觉语言模型的数据管理流程，从而与在 CLIP 原始数据集上训练的模型相比，提高了性能和多样性。

[![arXiv](https://img.shields.io/badge/arXiv-2309.16671-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2309.16671) [![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/facebookresearch/MetaCLIP)  
徐胡、谢赛宁、谭小青、黄坡耀、Russell Howes、Vasu Sharma、李尚文、Gargi Ghosh、Luke Zettlemoyer、Christoph Feichtenhofer
<p align="center">
<img src="https://github.com/gokayfem/Awesome-VLM-Architectures/assets/88277926/a6c79d0e-a4c7-48c9-86b6-3a8cc9853e11" />
</p> 
<详情>
<summary>ℹ️<i>更多信息</i></summary>
    
**MetaCLIP**：代表机器学习数据管理领域的一种创新方法，特别针对通过源自 CLIP 概念的元数据利用来**训练数据集**。该模型旨在筛选广泛的原始数据池（例如 CommonCrawl 数据集），以生成高质量、平衡的子集，从而显着改善用于训练机器学习模型的数据的多样性和性能指标。 MetaCLIP 的本质在于其独特的架构，其中包含数据管理算法，该算法擅长利用元数据来平衡和丰富训练数据集的质量和多样性。 MetaCLIP 的架构是围绕这些**数据管理算法**构建的，这些算法通过从最初源自 CommonCrawl 的 4 亿个图像文本对的庞大集合中识别和组装平衡的高质量数据集，在框架中发挥着关键作用。与使用 CLIP 原始方法管理的数据集相比，此过程有助于 MetaCLIP 在各种基准测试（包括零样本 ImageNet 分类）上展示卓越性能。因此，MetaCLIP 采用的训练方法不仅仅是处理和学习数据，还包括智能地选择对训练过程最有利的数据，确保模型在具有代表性、多样性和高质量的数据集上进行训练。在 MetaCLIP 框架内使用 CommonCrawl 等数据集的目的是解决和克服 CLIP 原始数据集中观察到的局限性。通过整理包含 4 亿个图像文本对的平衡且高质量的数据集，MetaCLIP 在机器学习数据整理领域树立了新的先例。与之前的版本相比，训练数据集的这种策略性选择和增强使 MetaCLIP 能够显着提高标准基准测试的性能，凸显了数据集质量和多样性对于在机器学习任务中实现高性能的重要性。通过其创新的数据管理方法，MetaCLIP 为增强机器学习模型的能力提供了一条有前途的途径，特别是在需要强大的图像文本理解和分类的应用程序中。
</详情>

## **Alpha-CLIP：专注于您想要的任何地方的 CLIP 模型**

Alpha-CLIP 建立在 CLIP 模型的基础上，通过向图像编码器添加 alpha 通道来整合区域感知，并在数百万个 RGBA 区域文本对上进行训练，从而能够精确控制图像强调并增强需要详细空间理解的各种任务的性能。

[![arXiv](https://img.shields.io/badge/arXiv-22312.03818-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2312.03818) [![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/SunzeY/AlphaCLIP)  
孙泽一、方野、吴童、张攀、臧宇航、孔舒、熊元军、林大华、王嘉琪
<p align="center">
<img src="https://github.com/gokayfem/Awesome-VLM-Architectures/assets/88277926/07bd6161-1682-4954-97f3-3770258bfa8c" />
</p> 
<详情>
<summary>ℹ️<i>更多信息</i></summary>
  
**Alpha-CLIP**：对原始 CLIP 模型进行了重大增强，将区域感知纳入其全部功能中。该模型针对数百万个 RGBA 区域文本对进行了微调，使其能够保持 CLIP 的视觉识别能力，同时提供对图像内容重点的精确控制。通过将额外的 **alpha 通道集成到 CLIP 图像编码器**，Alpha-CLIP 可以在不修改基本 CLIP 权重的情况下进行详细的分割和特定于区域的处理，从而促进尊重视觉数据空间动态的细致入微的图像理解方法。
Alpha-CLIP 的训练利用了一种新颖的数据生成管道，旨在生成大量 RGBA 区域文本对。此过程涉及创建配备有前景 Alpha 通道的自然图像及其针对特定区域的相应引用表达式。这种方法不仅能够通过额外的 alpha 通道输入对模型进行微调，而且还支持其在各种任务中以更高的特异性执行的能力。这些任务范围从图像识别到多模态大语言模型，并扩展到 2D 和 3D 生成领域，展示了 Alpha-CLIP 的多功能性和广泛的适用性。 LAION-400M、LAION-5B 和 GRIT 等数据集在训练 Alpha-CLIP 中发挥着至关重要的作用，为初始训练提供广泛的图像，并为增强局部感知能力提供细粒度的掩模级标签。这种数据集的战略选择确保 Alpha-CLIP 不仅能够很好地完成一般视觉识别任务，而且能够进行细致入微的、特定区域的处理和理解，为语言和视觉交叉点的模型设定新标准。
</详情>

## **GLIP：扎根语言图像预训练**

GLIP 通过统一对象检测和短语基础，彻底改变了语言图像预训练，使其能够在训练过程中通过视觉和文本信息的深度集成来理解和执行需要对象级精度和语言意识的任务。

[![arXiv](https://img.shields.io/badge/arXiv-2112.03857-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2112.03857) [![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/microsoft/GLIP)  
Liunian Harold Li、Pengchuan 张、Haotian 张、Jianwei Yang、Chunyuan Li、Yiwuzhong、Lijuan Wang、Lu Yuan、Lei Zhang、Jenq-Neng Hwang、Kai-Wei Chang、Jianfeng Gao
<p align="center">
<img src="https://github.com/gokayfem/Awesome-VLM-Architectures/assets/88277926/06e6f8dc-fbd8-49da-8651-a22ee2edcf3d" />
</p> 
<详情>
<summary>ℹ️<i>更多信息</i></summary>
    
**GLIP**：一种新颖的方法，通过将对象检测重新定义为短语基础挑战，创新地统一了对象检测和短语基础的任务。这一战略改革使模型能够利用广泛的图像文本配对数据集进行预训练，使其具备理解和执行需要对象级精度、语言感知和语义丰富的视觉表示的任务的能力。 GLIP 架构的核心旨在深度集成视觉和文本信息，结合文本提示增强其对复杂视觉场景的理解。 GLIP 的架构由几个关键组件组成，包括视觉编码器，可以是卷积神经网络 (CNN) 或 Transformer，其任务是从图像内的区域或边界框提取特征。它还包括一个专门用于处理文本提示和预测头（框分类器和框回归器）的语言编码器，这些编码器使用**分类**和**定位损失**进行训练。 GLIP的一个显着特点是其图像和文本深度融合的方法，特别是在编码的后期阶段，它比传统方法更全面地融合视觉和文本信息。 GLIP 的训练方法与其架构一样具有创新性，采用统一的公式将检测和接地任务合并到一个单一的工作流程中。该模型经过端到端训练，优化了为**检测**（专注于定位和分类）和**接地**（以图像区域与提示中相应单词之间的对齐分数为中心）定义的损失。在训练过程中视觉和语言特征的深度整合至关重要，它有助于模型从成对的图像文本数据中有效学习的能力。用于训练 GLIP 的数据集（包括 COCO、OpenImages、Objects365、Visual Genome、Flickr30k-entities、LVIS 和 PhraseCut）经过精心挑选，涵盖了广泛的对象类别和场景，每个数据集都有一个独特的用途，从对象检测和短语基础到实例分割和引用表达分割。通过这种全面的培训，GLIP 在语言图像预训练领域开创了新的先例，展示了视觉和文本数据解释和交互的先进能力。
</详情>

## **ImageBind：一个嵌入空间将它们全部绑定**

ImageBind 通过创建一个单一的联合嵌入空间来彻底改变多模态学习，该空间集成了六种模态（图像、文本、音频、深度、热和 IMU 数据），通过图像配对数据作为中央绑定代理，允许跨不同数据类型进行零样本分类和检索。

[![arXiv](https://img.shields.io/badge/arXiv-2305.05665-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2305.05665) [![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/facebookresearch/imagebind)  
Rohit Girdhar、Alaaeldin El-Nouby、刘壮、Mannat Singh、Kalyan Vasudev Alwala、Armand Joulin、Ishan Misra
<p align="center">
<img src="https://github.com/gokayfem/Awesome-VLM-Architectures/assets/88277926/fbf8bcdd-b1bb-4fd8-8723-3c82e84ef759" />
</p> 
<详情>
<summary>ℹ️<i>更多信息</i></summary>
    
**ImageBind**：通过创建**联合嵌入空间**引入多模态学习的创新方法，该空间包含六种不同的模态：**图像、文本、音频、深度、热和 IMU（惯性测量单元）**数据。该模型独特地采用图像配对数据作为中央绑定代理，使其能够利用大规模视觉语言模型的功能将零样本功能扩展到新的、以前未链接的模式。通过这样做，ImageBind 不仅促进了不同数据类型的更深入集成，而且还为跨广泛应用程序的零样本分类和检索开辟了新途径。 ImageBind 架构的核心是基于变压器的设计，适合每种特定模式以确保最佳处理和表示。例如，它利用视觉转换器来处理图像数据，每个模态编码器都通过**特定模态的线性投影头**进行增强。这些调整对于在不同数据类型中保持统一的嵌入大小至关重要，确保模型能够有效地学习各种模式并将其链接在一起。这种一致性是 ImageBind 能够创建内聚且全面的嵌入空间以捕获每种数据类型的细微差别的关键。 ImageBind 背后的训练方法尤其值得注意。它采用对比学习，利用网络规模的图像文本数据和来自各种模式的自然发生的配对数据，例如视频音频和图像深度对。这种策略允许模型学习单个联合嵌入空间，而不需要所有模态同时出现，这是增强其灵活性和适用性的显着优势。 Audioset、SUN RGB-D、LLVIP 和 Ego4D 等数据集的使用对此过程至关重要，这些数据集可在模型的目标模式中提供自然配对的数据。这些数据集使 ImageBind 能够在针对每种模态定制的任务上实现紧急的零样本分类和检索性能，展示了该模型无缝导航和利用不同形式数据之间复杂相互作用的能力。
</详情>

## **SigLIP：语言图像预训练的 Sigmoid 损失**

SigLIP 为语言图像预训练引入了简单的成对 sigmoid 损失，允许在不影响性能的情况下进行大批量的可扩展训练，从而实现图像和文本表示之间的高效对齐。

[![arXiv](https://img.shields.io/badge/arXiv-2303.15343-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2303.15343)  
翟晓华、Basil Mustafa、Alexander Kolesnikov、Lucas Beyer
<p align="center">
<img src="https://github.com/gokayfem/Awesome-VLM-Architectures/assets/88277926/60018313-37dd-4dbd-8eb4-a3075fd26663" />
</p> 
<详情>
<summary>ℹ️<i>更多信息</i></summary>
    
**SigLIP**：一种新颖的语言图像预训练方法，提出**简单的成对 sigmoid 损失**。该方法与利用 softmax 归一化的标准对比学习形成对比，因为它直接对图像-文本对进行操作，而无需对归一化的成对相似性进行全局视图。这种方法的主要优点是其可扩展性，允许使用更大的批量大小而不影响性能。该架构利用视觉转换器进行图像处理，并利用传统转换器进行文本处理，并且 sigmoid 损失有利于图像-文本对的独立处理。通过检查改变负正比和选择示例对的影响，这种设计可以实现更高效的训练动态，特别是在大批量的情况下。训练方法侧重于利用大批量，深入研究批量大小变化如何影响模型性能的动态。 sigmoid 损失的引入至关重要，通过研究负例与正例的比率与示例对选择的优化之间的关系，使模型能够有效地进行大批量训练。 LiT 图像文本数据集和 WebLI 数据集的使用是模型训练不可或缺的一部分，旨在实现图像和文本之间对齐的表示空间。选择这些数据集是因为它们在评估零样本传输能力以及探索模型基于 sigmoid 损失的训练的可扩展性和效率方面很有用。从本质上讲，SigLIP 通过创新地使用 sigmoid 损失、提高可扩展性和训练效率，标志着语言图像预训练的重大进步。这种方法不仅通过消除全局标准化的需要来简化训练过程，而且还展示了模型对大规模数据处理的适应性。数据集的战略选择进一步强调了模型打造一致表示空间的能力，为高级零样本学习和高效多模态集成铺平了道路。
</详情>

## **ViT：一张图像值得 16x16 个单词：用于大规模图像识别的 Transformers**

Vision Transformer (ViT) 通过将 Transformer 架构应用于图像，将其处理为一系列固定大小的块，彻底改变了图像识别，从而证明图像识别可以受益于 Transformer 的强大功能，在大规模训练数据集的帮助下超越传统的卷积神经网络 (CNN) 方法。

[![arXiv](https://img.shields.io/badge/arXiv-2010.11929v2-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2010.11929v2) [![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/google-research/vision_transformer)  
阿列克谢·多索维茨基、卢卡斯·拜尔、亚历山大·科列斯尼科夫、德克·韦森博恩、翟晓华、托马斯·温特蒂纳、莫斯塔法·德赫哈尼、马蒂亚斯·明德勒、格奥尔格·海戈尔德、西尔万·盖利、雅各布·乌什科雷特、尼尔·霍尔斯比
<p align="center">
<img src="https://github.com/gokayfem/Awesome-VLM-Architectures/assets/88277926/b2f77966-c2e8-4204-ba90-be51196a7dee" />
</p> 
<详情>
<summary>ℹ️<i>更多信息</i></summary>
    
**视觉变压器 (ViT)**：通过将主要用于自然语言处理的变压器架构直接应用于图像，实现图像识别的范式转变。它创新地将图像处理为**一系列固定大小的补丁**，类似于**文本应用程序**中处理令牌的方式。这种方法是通过对标准变压器组件进行最少的修改来实现的，强调模型对视觉任务的适应性，而不依赖于卷积神经网络（CNN）的归纳偏差。 ViT 架构的特点是使用线性嵌入进行**图像补丁**和**位置嵌入**，这对于维护图像数据的空间层次结构至关重要。 ViT 的核心是标准 Transformer 编码器，包括多头自注意力（MSA）和多层感知器（MLP）块，并辅以层归一化和残差连接，强调了其处理视觉数据的效率和鲁棒性。 ViT 训练方法的特点是可扩展性以及数据集大小对其性能的重大影响。最初，ViT 在没有强大的正则化技术的情况下表现出适度的准确性。然而，它的性能随着训练规模的扩大而提升，通过对大型数据集进行广泛的预训练，展示了其超越传统 CNN 方法的潜力。这个过程凸显了数据集选择在 ViT 训练方案中的关键作用。在全面的预训练阶段之后，它在较小的数据集上进行了微调，利用 ImageNet-21k 和 JFT-300M 等大型数据集来增强模型在各种任务中的泛化和性能。所使用的数据集包括 ImageNet、CIFAR-100、VTAB、ImageNet-21k 和 JFT-300M，具有双重目的：对模型的图像分类能力进行基准测试，并评估其在有限数据下对不同任务的可迁移性，从而确立 ViT 在推进图像识别任务方面的多功能性和有效性。
</详情>

## 重要参考资料

- [视觉语言模型 (VLM) 指南，作者：Görkem Polat](https://encord.com/blog/vision-language-models-guide/)
- [VLM 入门，作者：Aman Chadha](https://aman.ai/primers/ai/VLM/#google_vignette)
- [广义视觉语言模型 作者：Lilian Weng](https://lilianweng.github.io/posts/2022-06-09-vlm/)
