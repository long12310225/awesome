# 令人敬畏的人工智能

用于构建和交付人工智能系统的**必须使用、积极维护的资源**的精选集合。

重点：**人工智能工程**（RAG、代理、评估、护栏、部署）以及最好的书籍、指南、论文和一套*精心挑选的工具。

![](https://media.giphy.com/media/jeAQYN9FfROX6/giphy.gif)

---

## 📚 学习
_深刻、持久的知识——五年后仍然有价值。_

### 书籍
**现代实用**
- [Designing Machine Learning Systems](https://www.oreilly.com/library/view/designing-machine-learning/9781098107956/) - 可扩展、可维护的机器学习管道 (Chip Huyen)。
- [AI Engineering](https://www.oreilly.com/library/view/ai-engineering/9781098166298/) - 端到端人工智能产品构建（Chip Huyen）。
- [Build a Large Language Model from Scratch](https://www.manning.com/books/build-a-large-language-model-from-scratch) - 原始 PyTorch 中的变形金刚，逐层（Sebastian Raschka）。
- [Hands-On Large Language Models](https://www.llm-book.com/) - LLM 申请的视觉+实用指南（Jay Alammar、Maarten Grootendorst）。
- [LLM Engineer's Handbook](https://www.packtpub.com/en-us/product/llm-engineers-handbook-9781836200079) - 生产 LLMOps：微调、量化、服务（Labonne、Iusztin）。
- [The 100-Page Language Models Book](https://www.thelmbook.com/) - 从 n-gram 到 Transformer 的简洁、基于数学的路径 (Andriy Burkov)。
- [Generative Deep Learning (2nd Edition)](https://www.oreilly.com/library/view/generative-deep-learning/9781098134174/) - GAN、VAE、扩散模型（David Foster）。

**基础**
- [Artificial Intelligence: A Modern Approach](https://aima.cs.berkeley.edu/) - 规范的人工智能理论文本（Russell，Norvig）。
- [Deep Learning](https://www.deeplearningbook.org/) - 神经网络的数学基础（Goodfellow、Bengio、Courville）。
- [Deep Learning: Foundations and Concepts](https://www.bishopbook.com/) - Bishop的2024年更新；基于概率的现代深度学习（Bishop & Bishop）。
- [Understanding Deep Learning](https://udlbook.github.io/udlbook/) - 数学+直觉+Python笔记本（Simon Prince）。
- [Speech and Language Processing (3rd Edition)](https://web.stanford.edu/~jurafsky/slp3/) - NLP 参考资料在整个深度学习时代都保持最新（Jurafsky、Martin）。
- [Reinforcement Learning: An Introduction (2nd Edition)](https://web.stanford.edu/class/psych209/Readings/SuttonBartoIPRLBook2ndEd.pdf) - RL 基金会（萨顿、巴托）。

### 课程

**初学者**
- [谷歌生成式人工智能学习路径](https://www.cloudskillsboost.google/paths/118)
- [拥抱脸法学硕士课程](https://huggingface.co/learn/llm-course/chapter1/1)
- [Fast.ai——实用深度学习](https://course.fast.ai/)

**中级/高级**
- [斯坦福 CS324：大型语言模型](https://stanford-cs324.github.io/winter2022/)
- [全栈深度学习](https://fullstackdeeplearning.com/)
- [MIT 6.S191：深度学习简介](https://introtodeeplearning.com/)

**专注**
- [DeepLearning.AI 短期课程](https://learn.deeplearning.ai/)
- [Google DeepMind — 强化学习简介](https://www.youtube.com/playlist?list=PLqYmG7hTraZDM-OYHWgPebj2MfCFzFObQ)
- [Karpathy — 神经网络：从零到英雄](https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ)

### 里程碑式的论文
_塑造现代人工智能的研究——值得一读，以了解当今架构背后的“原因”。_
- [Attention Is All You Need](https://arxiv.org/abs/1706.03762) - 变压器架构。
- [Scaling Laws for Neural Language Models](https://arxiv.org/abs/2001.08361) - 模型/数据/计算扩展。
- [Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165) - GPT-3 功能。
- [Constitutional AI](https://arxiv.org/abs/2212.08073) - 更安全的模型对齐。

---

## 🛠 构建
_使用 AI 进行构建的工具链。_
_个人注意：你不需要大量的框架 - 从简单的 LLM 调用开始并逐步完善。_

### 指南和手册
- **[构建有效代理（人类）](https://www.anthropic.com/engineering/building- effective-agents)** — ⭐ 设计人工智能代理的模式、陷阱和权衡。
- [OpenAI Agents Guide](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf) - 建筑剂实用指南。
- [Google AI Agents Paper](https://www.kaggle.com/whitepaper-agents) - 来自 Google 的构建 AI 代理的实用指南。
- [Google Agents Companion Paper](https://www.kaggle.com/whitepaper-agent-companion) - 来自 Google 的配套指南。
- [OpenAI Cookbook](https://cookbook.openai.com/) - 使用 OpenAI API 的示例代码、秘诀和最佳实践。
- [LLM Engineer Handbook](https://github.com/SylphAI-Inc/LLM-engineer-handbook) - 为人工智能工程师提供有用链接的金矿。

### 框架
- [PocketFlow](https://the-pocket.github.io/PocketFlow/) - 极其简约的 AI 代理框架，仅 100 行代码。很棒的学习方式。
- [Google ADK](https://google.github.io/adk-docs/) - Google 的代理开发套件（Python、Java）。丰富的本地开发经验+A2A+MCP。
- [Pydantic-AI](https://ai.pydantic.dev/) - 基于 Pydantic 模型构建的类型化、结构化的 LLM 编排框架，可实现安全、可预测的输出。
- [LangGraph](https://www.langchain.com/langgraph) - 在 LangChain 之上构建具有状态图的多代理工作流程。
- [CrewAI](https://www.crewai.com/) - 具有结构化任务和人机交互控制的代理编排。
- [AutoGen](https://microsoft.github.io/autogen/) - Microsoft 的多代理对话和协作框架。
- [LlamaIndex](https://www.llamaindex.ai/) - 用于使用 LLM 摄取、索引和查询私有数据的数据框架。
- [Haystack](https://haystack.deepset.ai/) - 具有模块化管道的开源搜索/RAG 框架。
- [Docling](https://github.com/docling-project/docling) - 很棒的库，可以为 RAG 摄取任何类型的文档 ⭐

### 埃瓦尔斯
- [OpenAI Evals](https://github.com/openai/evals) - OpenAI 用于编写评估的框架。

### IDE
- [Cursor](https://cursor.sh/) - 由 LLM 支持的 IDE，用于多文件编辑和代码库感知聊天。
- [GitHub Copilot](https://github.com/features/copilot) - IDE 内代码补全、聊天和重构。

---

## 🤖 代理商
_将法学硕士转变为自主工作者的安全带。型号可互换；安全带就是产品。_

### 编码
_有关实时能力比较，请参阅 [Terminal-Bench](https://www.tbench.ai/leaderboards) 和 [SWE-bench](https://www.swebench.com/)。_

- [Claude Code](https://code.claude.com/) - Anthropic 的 CLI 代理；具有长上下文的多文件代码库重构。
- [Codex CLI](https://github.com/openai/codex) - OpenAI基于Rust的本地终端代理；轻量且快速。
- [Gemini CLI](https://github.com/google-gemini/gemini-cli) - Google官方开源终端代理；长上下文回购探索。
- [Cursor CLI](https://cursor.com/cli) - Cursor 的终端本机代理，具有沙盒权限。
- [Aider](https://aider.chat/) - Git 集成结对编程，具有外科手术式编辑和撤消功能。
- [OpenCode](https://opencode.ai/) - 与提供商无关的终端线束，具有强大的 TUI。
- [OpenHands](https://docs.all-hands.dev/) - 开源自主SWE平台；浏览器+ shell + 编辑器循环。
- [Cline](https://github.com/cline/cline) - 开源代理 IDE 扩展，具有强大的多提供商支持。
- [Continue](https://www.continue.dev/) - 具有源代码控制规则的开源 IDE + CLI 助手。
- [Goose](https://block.github.io/goose/) - Block 的可扩展、MCP 驱动的本地代理。
- [Factory Droid](https://factory.ai/product/cli) - 基准领先的多模型线束，具有 BYOK 本地执行。
- [Amp](https://ampcode.com/) - Sourcegraph 的商业代理编码工具具有强大的产品用户体验。
- [Mistral Vibe](https://mistral.ai/products/vibe) - Mistral 的代理编码 CLI，由 Devstral 提供支持。
- [Qwen Code](https://github.com/QwenLM/qwen-code) - 阿里巴巴的终端编码代理，针对Qwen模型进行了优化。
- [Pi](https://pi.dev/) - 高度可定制的端子线束；最小基本提示，扩展驱动。
- [Nanocoder](https://github.com/Nano-Collective/nanocoder) - Ollama 和 LM Studio 的私人本地优先代理。
- [Kilo CLI](https://kilo.ai/cli) - 多模式代理，具有 500 多个模型的统一网关。

---

## 🧠 模型
_最先进的模态模型._

### 💬 语言
主要前沿实验室。

- [ChatGPT](https://openai.com/chatgpt/overview/) - 最适合一般推理、工具使用和最广泛的生态系统。
- [Claude](https://www.anthropic.com/claude) - 最适合长上下文分析、编码和结构化思维。
- [Gemini](https://gemini.google.com/) - 最适合多模式任务和 Google 生态系统集成。
- [Grok](https://x.ai/) - 最适合通过 X 和很长的上下文获取实时信息。
- [Llama](https://www.llama.com/) - 用于自托管和微调的最佳开放重量系列。
- [Mistral](https://mistral.ai/) - 最适合轻量级、高性能开放式模型。
- [DeepSeek](https://deepseek.com/) - 最适合使用开放权重进行经济有效的推理。
- [Qwen](https://qwenlm.github.io/) - 最适合多语言和中文优先的应用程序。
- [Kimi](https://www.kimi.com/) - 最适合遵循长上下文指令。
- [GLM](https://chatglm.cn/) - 开放重量的前沿中国模型。
- [Cohere](https://cohere.com/) - 最适合具有强大检索增强生成 API 的企业法学硕士。

### 🖼 图片
- [GPT Image](https://openai.com/index/introducing-chatgpt-images-2-0/) - OpenAI 的集成图像生成与近乎完美的文本渲染。
- [Midjourney](https://www.midjourney.com/) - 艺术和逼真的图像。
- [Adobe Firefly](https://www.adobe.com/sensei/generative-ai/firefly.html) - 集成到创意云；商业安全。
- [Ideogram](https://ideogram.ai/) - 生成的图像中的文本精确、清晰。
- [Flux](https://blackforestlabs.ai/) - 高分辨率、可即时编辑、开放重量的图像。

### 🎥 视频
- [Google Veo](https://deepmind.google/technologies/veo/) - 具有同步音频的高质量视频。
- [Runway](https://runwayml.com/) - 视频编辑+生成，具有精细的创意控制。
- [Kling](https://klingai.com/) - 电影般的、逼真的视频生成。

### 🎙 音频
- [ElevenLabs](https://elevenlabs.io/) - 高质量的文本转语音和语音克隆。
- [Suno](https://suno.ai/) - AI音乐由文字提示。

### 📊 比较
_实时基准、定价和最新模型版本。_
- [OpenRouter](https://openrouter.ai/models) - 统一 API + 涵盖约 300 种型号的实时定价。
- [LMArena](https://lmarena.ai/leaderboard) - 文本、图像和视频的人类偏好 Elo 排名。
- [Artificial Analysis](https://artificialanalysis.ai/) - 供应商之间的速度、价格和质量基准。

---

## 📡 关注
_保持最新状态而不被噪音淹没。_

### 时事通讯
- [破败的人工智能](https://www.therundown.ai/)
- [AlphaSignal](https://alphasignal.ai/)
- [超人人工智能](https://www.superhuman.ai/)
- [人工智能工程师](https://newsletter.owainlewis.com)

---
