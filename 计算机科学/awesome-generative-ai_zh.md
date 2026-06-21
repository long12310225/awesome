# 很棒的生成人工智能 [![Awesome](https://awesome.re/badge-flat.svg)](https://awesome.re)

> 现代生成人工智能项目和服务的精选列表。

生成人工智能是一种通过使用经过大量数据训练的机器学习算法来创建图像、声音和文本等原始内容的技术。与其他形式的人工智能不同，它能够创造独特的、前所未见的输出，例如逼真的图像、数字艺术、音乐和写作。这些产出往往有自己独特的风格，甚至很难与人类创作的作品区分开来。生成式人工智能在艺术、娱乐、营销、学术界和计算机科学等领域有着广泛的应用。

欢迎对此列表做出贡献。在提交您的建议之前，请查看[贡献指南](CONTRIBUTING.md)，以确保您的参赛作品符合标准。通过 [pull requests](https://github.com/steven2358/awesome-generative-ai/pulls) 添加链接或创建一个 [issue](https://github.com/steven2358/awesome-generative-ai/issues) 来开始讨论。更多项目可以在 [发现列表](DISCOVERIES.md) 中找到，我们在其中展示了各种新兴的生成式 AI 项目。

## 内容

- [推荐阅读](#recommended-reading)
- [Text](#text)
- [Coding](#coding)
- [Agents](#agents)
- [Image](#image)
- [Video](#video)
- [Audio](#audio)
- [Other](#other)
- [学习资源](#learning-resources)
- [更多列表](#more-lists)

## 推荐阅读

- [How Large Language Models Will Transform Science, Society, and AI](https://hai.stanford.edu/news/how-large-language-models-will-transform-science-society-and-ai) - 文章总结了 GPT-3 模型的功能和局限性及其对社会的潜在影响。作者：Alex Tamkin 和 Deep Ganguli，2021 年 2 月 5 日。
- [Generative AI: A Creative New World](https://www.sequoiacap.com/article/generative-ai-a-creative-new-world/) - 对生成人工智能行业进行全面审视，提供历史视角和行业生态系统的深入分析。作者：Sonya Huang、Pat Grady 和 GPT-3，2022 年 9 月 19 日。
- [A Coming-Out Party for Generative A.I., Silicon Valley's New Craze](https://www.nytimes.com/2022/10/21/technology/generative-ai.html) - 关于生成式人工智能的兴起，特别是稳定扩散图像生成器的成功以及相关争议的文章。纽约时报，2022 年 10 月 21 日。
- [AI's New Creative Streak Sparks a Silicon Valley Gold Rush](https://www.wired.com/story/ais-new-creative-streak-sparks-a-silicon-valley-gold-rush/) - 文章介绍了对生成型人工智能初创公司日益增长的炒作和投资，以及各个行业探索其潜在应用的情况。连线，2022 年 10 月 27 日。
- [ChatGPT Heralds an Intellectual Revolution](https://www.wsj.com/articles/artificial-intelligence-generative-ai-chatgpt-kissinger-84512912) - 亨利·基辛格、埃里克·施密特和丹尼尔·胡滕洛彻的专栏文章。 《华尔街日报》，2023 年 2 月 24 日。

### 里程碑

- [OpenAI API](https://openai.com/blog/openai-api/) - 发布基于 GPT-3 的文本到文本通用 AI 模型的 OpenAI API。 OpenAI 博客，2020 年 6 月 11 日。
- [GitHub Copilot](https://github.blog/news-insights/product-news/introducing-github-copilot-ai-pair-programmer/) - 发布 Copilot，一款新的 AI 结对程序员，可帮助您编写更好的代码。 GitHub 博客，2021 年 6 月 29 日。
- [DALL·E 2](https://openai.com/blog/dall-e-2/) - 宣布发布 DALL·E 2，这是一种先进的图像生成系统，具有更高的分辨率、扩展的图像创建功能和各种安全缓解措施。 OpenAI 博客，2022 年 4 月 6 日。
- [Stable Diffusion Public Release](https://stability.ai/news-updates/stable-diffusion-public-release) - 宣布公开发布 Stable Diffusion，这是一种基于 AI 的图像生成模型，在广泛的互联网上进行训练，并根据 Creative ML OpenRAIL-M 许可证获得许可。稳定扩散博客，2022 年 8 月 22 日。
- [ChatGPT](https://openai.com/blog/chatgpt/) - ChatGPT 的发布，这是一种经过训练的对话模型，可以回答后续问题、承认错误、挑战不正确的前提并拒绝不适当的请求。 OpenAI 博客，2022 年 11 月 30 日。
- [Bing Search](https://blogs.microsoft.com/blog/2023/02/07/reinventing-search-with-a-new-ai-powered-microsoft-bing-and-edge-your-copilot-for-the-web/) - 微软宣布推出新版搜索引擎 Bing，由下一代 OpenAI 模型提供支持。 Microsoft 博客，2023 年 2 月 7 日。
- [LLaMA](https://ai.meta.com/blog/large-language-model-llama-meta-ai/) - Llama LLM，Meta 的基础性 650 亿参数大语言模型。元，2023 年 2 月 23 日。#opensource
- [GPT-4](https://openai.com/research/gpt-4) - 发布大型多式联运模型 GPT-4。 OpenAI 博客，2023 年 3 月 14 日。
- [DALL·E 3](https://openai.com/index/dall-e-3/) - DALL·E 3图像生成器发布。 OpenAI 博客，2023 年 9 月 20 日。
- [Sora](https://openai.com/research/video-generation-models-as-world-simulators) - 介绍大型视频生成模型 Sora。 OpenAI，2024 年 2 月 15 日。

## 文字

### 型号

- [OpenAI API](https://openai.com/api/) - OpenAI 的 API 提供对 GPT 模型的访问，以进行自然语言、编码、图像生成、音频和代理开发。
- [Gopher](https://deepmind.google/blog/language-modelling-at-scale-gopher-ethical-considerations-and-retrieval/) - DeepMind 的 Gopher 是一个 2800 亿参数的语言模型。
- [OPT](https://huggingface.co/facebook/opt-350m) - Facebook 的 Open Pretrained Transformers (OPT) 是一套仅包含解码器的预训练 Transformer。 [公告](https://ai.meta.com/blog/democratizing-access-to-large-scale-language-models-with-opt-175b/)。
- [Bloom](https://huggingface.co/docs/transformers/model_doc/bloom) - Hugging Face 的 BLOOM 是一个类似于 GPT-3 的模型，已经过 46 种不同语言和 13 种编程语言的训练。 #开源
- [Llama](https://www.llama.com/) - Meta 的开源大语言模型。 #开源
- [Claude](https://claude.ai/) - 与 Anthropic 的人工智能助手 Claude 交谈。
- [Vicuna-13B](https://lmsys.org/blog/2023-03-30-vicuna/) - 一个开源聊天机器人，通过对从 ShareGPT 收集的用户共享对话进行微调 LLaMA 进行训练。 #开源
- [Mistral](https://mistral.ai/en/models) - Mistral AI 的开放式法学硕士。 #开源
- [Grok](https://grok.x.ai/) - xAI 的法学硕士，具有[开源](https://github.com/xai-org/grok-1) 和开放权重。 #开源
- [Qwen](https://qwenlm.github.io/) - 阿里云自主研发的LLM系列。 [#opensource](https://github.com/QwenLM/Qwen)
- [DeepSeek](https://huggingface.co/deepseek-ai) - DeepSeek AI 的一系列开源法学硕士。 [#opensource](https://github.com/deepseek-ai)
- [MiniMax](https://www.minimax.io/) - 用于文本、语音、视频和音乐生成的多模态基础模型
- [Kimi K2](https://github.com/moonshotai/Kimi-K2) - Moonshot AI 用于代理任务的一系列开源 MoE 语言模型。 #开源
- [GLM](https://github.com/zai-org/GLM-5) - Z.ai 用于代理任务的一系列开源 MoE 语言模型。 #开源

### 聊天机器人

- [ChatGPT](https://chatgpt.com/) - OpenAI 的 ChatGPT 是一种以对话方式进行交互的大型语言模型。
- [Copilot](https://copilot.microsoft.com/) - Microsoft 的日常人工智能伴侣。
- [Gemini](https://gemini.google.com/) - 由 Google Deepmind 开发的多模态大语言模型家族。
- [Meta AI](https://www.meta.ai/) - Meta AI 助手可以完成工作、创建 AI 生成的图像、获取答案。建立在 Llama LLM 之上。
- [DeepSeek](https://www.deepseek.com/) - 由 DeepSeek 的开源语言模型提供支持的聊天机器人界面。 #开源
- [Character.AI](https://character.ai/) - Character.AI 可让您创建角色并与他们聊天。
- [Pi](https://pi.ai) - 可用作数字助理的个性化人工智能平台。
- [Qwen](https://chat.qwenlm.ai/) - Qwen 聊天机器人具有图像生成、文档处理、网络搜索集成、视频理解等功能。
- [Le Chat](https://chat.mistral.ai/) - Mistral AI 语言模型的聊天界面。
- [Kimi](https://www.kimi.com/) - Moonshot AI 的人工智能助手，具有聊天、深入研究、编码和多代理功能。
- [Z.ai](https://chat.z.ai/) - Z.ai 的人工智能聊天机器人和代理平台，由 GLM 模型系列提供支持。

### 自定义接口

- [LibreChat](https://librechat.ai/) - LibreChat 是一个免费的开源聊天界面，适用于人工智能助理。 [#opensource](https://github.com/danny-avila/LibreChat)。
- [Chatbot UI](https://www.chatbotui.com/) - 开源 ChatGPT UI。 [#opensource](https://github.com/mckaywrigley/chatbot-ui)。

### 搜索引擎

- [Perplexity AI](https://www.perplexity.ai/) - 人工智能驱动的搜索工具。
- [Exa](https://exa.ai/) - 语言模型驱动的搜索。
- [Phind](https://phind.com/) - 基于人工智能的搜索引擎。
- [You.com](https://you.com/) - 一个基于人工智能的搜索引擎，为用户提供定制的搜索体验，同时保持数据 100% 的私密性。
- [Komo](https://komo.ai/) - 人工智能驱动的搜索引擎。

### 本地搜索引擎

- [privateGPT](https://github.com/zylon-ai/private-gpt) - 利用法学硕士的力量，在没有互联网连接的情况下对您的文档提出问题。
- [quivr](https://github.com/QuivrHQ/quivr) - 转储所有文件并使用 LLM 和嵌入使用生成人工智能第二大脑与其聊天。

### 写作助理

- [Jasper](https://www.jasper.ai/) - 利用人工智能更快地创建内容。
- [Compose AI](https://www.compose.ai/) - Compose AI 是一款免费的 Chrome 扩展程序，通过人工智能驱动的自动完成功能，可将您的写作时间缩短 40%。
- [Rytr](https://rytr.me/) - Rytr 是一款 AI 写作助手，可帮助您创作高质量内容。
- [wordtune](https://www.wordtune.com/) - 个人写作助理。
- [HyperWrite](https://hyperwriteai.com/) - HyperWrite 可帮助您充满信心地写作，并更快地完成从构思到最终草稿的工作。
- [Moonbeam](https://www.gomoonbeam.com/) - 只需一小部分时间就能制作出更好的博客。
- [copy.ai](https://www.copy.ai/) - 使用人工智能编写更好的营销文案和内容。
- [ChatSonic](https://writesonic.com/chat) - 一款支持文本和图像创建的人工智能助手。
- [Anyword](https://anyword.com/) - Anyword 的人工智能写作助手可以为任何人生成有效的文案。
- [Hypotenuse AI](https://www.hypotenuse.ai/) - 将一些关键词转化为原创、富有洞察力的文章、产品描述和社交媒体文案。
- [Lavender](https://www.lavender.ai/) - 薰衣草电子邮件助手可帮助您在更短的时间内获得更多回复。
- [Lex](https://lex.page/) - 内置人工智能的文字处理器，让您可以更快地写作。
- [Jenni](https://jenni.ai/) - Jenni 是终极写作助手，可以节省您数小时的构思和写作时间。
- [QuillBot](https://quillbot.com) - 人工智能驱动的释义工具。
- [Postwise](https://postwise.ai/) - 使用 AI 撰写推文、安排帖子并增加您的关注者。
- [Copysmith](https://copysmith.ai/) - 适用于企业和电子商务的人工智能内容创建解决方案。

### ChatGPT 扩展

- [WebChatGPT](https://chromewebstore.google.com/detail/webchatgpt-chatgpt-with-i/lpfemeioodjbpieminkklglpmhlngfcn) - 使用网络上的相关结果来增强您的 ChatGPT 提示。
- [GPT for Sheets and Docs](https://workspace.google.com/marketplace/app/gpt_for_sheets_and_docs/677318054654) - 适用于 Google 表格和 Google 文档的 ChatGPT 扩展。
- [YouTube Summary with ChatGPT](https://chromewebstore.google.com/detail/youtube-summary-with-chat/nmmicjeknamkfloonkhhcjmomieiodli) - 使用 ChatGPT 总结 YouTube 视频。
- [AI Prompt Genius](https://chromewebstore.google.com/detail/ai-prompt-genius/jjdnakkfjnnbbckhifcfchagnpofjffo) - 发现、共享、导入和使用 ChatGPT 的最佳提示并在本地保存您的聊天历史记录。
- [ShareGPT](https://sharegpt.com/) - 分享您的 ChatGPT 对话并探索其他人分享的对话。
- [Merlin](https://www.getmerlin.in/) - 所有网站上的 ChatGPT Plus 扩展。
- [Jetwriter](https://jetwriter.ai/) - 适用于 Chrome、桌面和移动设备的 AI 写作助手。
- [ChatGPT for Jupyter](https://github.com/TiesdeKok/chat-gpt-jupyter-extension) - 在由 ChatGPT 提供支持的 Jupyter Notebooks 和 Jupyter Lab 中添加各种帮助函数。
- [editGPT](https://www.editgpt.app/) - 在 chatGPT 中轻松校对、编辑和跟踪内容更改。
- [Forefront](https://www.forefront.ai/) - 更好的 ChatGPT 体验。
- [ChatGPT for Sheets, Docs, Slides, Forms](https://workspace.google.com/marketplace/app/gpt_for_sheets_docs_forms_slides/466607203252) - 适用于 Google 表格、Google 文档、Google 幻灯片、Google 表单的 ChatGPT 扩展。
- [GPT for Gmail](https://workspace.google.com/marketplace/app/gpt_for_gmail_ai_email_assistant_gemini/899305976589) - Gmail 的人工智能电子邮件助手。

### 生产力

- [ChatPDF](https://www.chatpdf.com/) - 与任何 PDF 聊天。
- [Mem](https://mem.ai/) - Mem 是世界上第一个基于人工智能的个性化工作空间。增强您的创造力，使日常事务自动化，并自动保持井井有条。
- [Taskade](https://www.taskade.com/) - 使用 Taskade AI 概述任务、笔记、生成的结构化列表和思维导图。
- [Notion AI](https://www.notion.so/product/ai) - 编写更好、更高效的笔记和文档。
- [Nekton AI](https://nekton.ai) - 使用 AI 自动化您的工作流程。用通俗易懂的语言逐步描述您的工作流程。
- [Limitless](https://www.limitless.ai/) - 人工智能记忆助手，用于记录对话和会议、生成摘要以及跨应用程序和可选可穿戴设备搜索过去的交互。
- [NotebookLM](https://notebooklm.google/) - 一种与文档交互的研究和笔记在线工具，由 Google Gemini 提供支持。
- [Open Notebook](https://www.open-notebook.ai) - NotebookLM 的开源实现，具有更多灵活性和功能。 [#opensource](https://github.com/lfnovo/open-notebook)
- [Screenpipe](https://github.com/screenpipe/screenpipe) - 一种开源工具，用于记录屏幕和音频活动，具有人工智能驱动的搜索、自动化功能，并支持本地法学硕士。 #开源

### 会议助理

- [Otter.ai](https://otter.ai/) - 会议助手，可录制音频、编写笔记、自动捕获幻灯片并生成摘要。
- [Cogram](https://www.cogram.com/) - Cogram 在虚拟会议中自动记录并识别行动项目。
- [Sybill](https://www.sybill.ai/) - Sybill 通过结合文字记录和基于情感的见解，生成销售电话摘要，包括后续步骤、痛点和感兴趣的领域。
- [Loopin AI](https://www.loopinhq.com/) - Loopin 是一个协作会议工作区，不仅使您能够使用 AI 记录、转录和总结会议，还使您能够在日历上自动组织会议笔记。
- [Read AI](https://www.read.ai/) - 无论您在哪里工作，人工智能副驾驶都可以通过摘要、内容发现和建议使您的会议、电子邮件和消息更加高效。
- [Fireflies.ai](https://fireflies.ai) - 转录、总结、搜索和分析所有团队对话。

### 学术界

- [Elicit](https://elicit.org/) - Elicit 使用语言模型来帮助您自动化研究工作流程，例如文献综述的一部分。
- [genei](https://www.genei.io/) - 在几秒钟内总结学术文章，节省 80% 的研究时间。
- [Explainpaper](https://www.explainpaper.com/) - 阅读学术论文的更好方式。上传论文，突出显示令人困惑的文本，获取解释。
- [Consensus](https://consensus.app/search/) - Consensus是一个利用人工智能在科学研究中寻找答案的搜索引擎。
- [scite](https://scite.ai/) - 发现和评估科学文章的平台。
- [SciSpace](https://scispace.com/) - 用于理解科学文献的人工智能研究助理。
- [STORM](https://storm.genie.stanford.edu/) - 一个由法学硕士支持的知识管理系统，用于研究某个主题并生成带有引文的完整报告。 [#opensource](https://github.com/stanford-oval/storm/)
- [alphaXiv](https://www.alphaxiv.org) - 讨论、发现和阅读 arXiv 论文。
- [ASReview](https://asreview.nl/) - 开源人工智能驱动的系统评价工具，帮助研究人员高效筛选大量学术文献。 [#opensource](https://github.com/asreview/asreview)
- [Local Deep Research](https://github.com/LearningCircuit/local-deep-research) - 一种深度研究工具，用于通过本地或云法学硕士搜索学术资源、网络和私人文档。 [#opensource](https://github.com/LearningCircuit/local-deep-research)
- [Rayyan](https://www.rayyan.ai/) - 一个人工智能驱动的平台，用于通过协作筛选和数据管理工具管理系统文献综述。

### 排行榜

- [Arena](https://arena.ai/) - 众包人工智能基准测试的开放平台，由加州大学伯克利分校天空实验室的研究人员主持。
- [Artificial Analysis](https://artificialanalysis.ai/) - 人工分析提供客观基准和信息，帮助选择人工智能模型和托管提供商。
- [imgsys](https://imgsys.org/rankings) - fal.ai 的生成图像模型竞技场。
- [OpenRouter LLM Rankings](https://openrouter.ai/rankings) - 按应用程序的使用情况对语言模型进行排名和分析。
- [SEAL LLM Leaderboard](https://labs.scale.com/leaderboard) - 专家驱动的 LLM 基准和更新的 AI 模型排行榜。
- [LLM Stats](https://llm-stats.com/) - 跨基准、定价、速度和上下文窗口比较 AI 模型。

### 其他文本生成器

- [EmailTriager](https://www.emailtriager.com/) - 使用 AI 在后台自动起草电子邮件回复。
- [AI Poem Generator](https://www.aipoemgenerator.org) - 根据文本提示，人工智能诗歌生成器可以为您写一首关于任何主题的优美押韵诗。

## 编码

### 编码助理

- [GitHub Copilot](https://github.com/features/copilot) - GitHub Copilot 使用 OpenAI Codex 直接从编辑器实时建议代码和整个功能。
- [OpenAI Codex](https://platform.openai.com/docs/guides/code/) - OpenAI 的人工智能系统，可将自然语言翻译为代码。
- [Ghostwriter](https://blog.replit.com/ai) - Replit 推出的人工智能结对编程器。
- [Amazon Q](https://aws.amazon.com/q/) - AWS 生成式 AI 支持的助手，可帮助回答问题、编写代码和自动执行任务。
- [tabnine](https://www.tabnine.com/) - 通过全行和全功能代码完成来更快地编码。
- [Stenography](https://stenography.dev/) - 自动代码文档。
- [Mintlify](https://mintlify.com/) - 人工智能驱动的文档编写者。
- [AI2sql](https://www.ai2sql.io/) - 借助 AI2sql，工程师和非工程师无需了解 SQL 即可轻松编写高效、无错误的 SQL 查询。
- [Qodo](https://www.qodo.ai/) - AI 代码审查工具，具有 IDE、拉取请求和安全性的代理工作流程。
- [PR-Agent](https://github.com/The-PR-Agent/pr-agent) - 由人工智能驱动的工具，用于自动公关分析、反馈、建议等。
- [TurboPilot](https://github.com/ravenscroftj/turbopilot) - 一个自托管的 copilot 克隆，它使用 llama.cpp 背后的库在 4 GB RAM 中运行 60 亿个参数的 Salesforce Codegen 模型。
- [GPT-Code UI](https://github.com/ricklamers/gpt-code-ui) - OpenAI 的 ChatGPT 代码解释器的开源实现。 #开源
- [Open Interpreter](https://github.com/openinterpreter/open-interpreter) - OpenAI 的代码解释器在您的终端中本地运行。
- [Continue](https://www.continue.dev/) - 开源AI代码助手。连接任何模型和任何上下文，以在 IDE 内创建自定义自动完成和聊天体验。 [#opensource](https://github.com/Continuedev/Continue)
- [RooCode](https://github.com/RooCodeInc/Roo-Code) - 直接集成到 VS Code 中的人工智能驱动的自主编码代理。 [#opensource](https://github.com/RooCodeInc/Roo-Code)
- [Windsurf](https://windsurf.com/) - 一个 AI 原生 IDE，在整个开发过程中将代码编辑与高级 AI 辅助相结合。
- [Plandex](https://github.com/plandex-ai/plandex) - 适用于复杂任务的开源、基于终端的人工智能编程引擎。 [#opensource](https://github.com/plandex-ai/plandex)
- [Jupyter AI](https://github.com/jupyterlab/jupyter-ai) - Jupyter Notebook 和 JupyterLab 中的开源、可配置 AI 助手，支持 100 多个 LLM，包括 Ollama 和 GPT4All 的本地托管模型。 #开源
- [DataLine](https://dataline.app) - 人工智能驱动的数据分析和可视化工具。 [#opensource](https://github.com/RamiAwar/dataline)
- [v0](https://v0.dev) - React 和 Next.js 的提示驱动 UI 生成，创建可用于生产的组件。
- [Lovable](https://lovable.dev) - 对话式全栈应用程序生成，将想法转化为可部署的代码。
- [aider](https://aider.chat/) - 在您的终端中进行 AI 结对编程，支持多个 LLM 提供商。 [#opensource](https://github.com/paul-gauthier/aider)
- [Kilo](https://kilo.ai/) - 适用于 VS Code、JetBrains 和 CLI 的开源 AI 编码助手。 [#opensource](https://github.com/Kilo-Org/kilocode)

### 开发者工具

- [Cohere](https://cohere.com/) - Cohere 提供对高级大型语言模型和 NLP 工具的访问。
- [Haystack](https://haystack.deepset.ai/) - 使用语言模型构建 NLP 应用程序（例如代理、语义搜索、问答）的框架。
- [LangChain](https://langchain.com/) - 用于开发由语言模型支持的应用程序的框架。
- [gpt4all](https://github.com/nomic-ai/gpt4all) - 一个聊天机器人，接受了大量干净的助理数据的训练，包括代码、故事和对话。
- [LLM App](https://github.com/pathwaycom/llm-app) - 用于构建支持 LLM 的实时数据管道的开源 Python 库。
- [LMQL](https://lmql.ai/) - LMQL 是一种大型语言模型的查询语言。
- [LlamaIndex](https://www.llamaindex.ai/) - 用于基于外部数据构建 LLM 应用程序的数据框架。
- [Phoenix](https://phoenix.arize.com/) - Arize 提供的用于 ML 可观测性的开源工具，可在笔记本环境中运行。监控和微调 LLM、CV 和表格模型。
- [Cursor](https://cursor.com/) - Cursor 是未来的 IDE，专为与强大的 AI 进行结对编程而构建。
- [SymbolicAI](https://github.com/ExtensityAI/symbolicai) - 用于构建以法学硕士为核心的应用程序的神经符号框架。
- [Vanna.ai](https://vanna.ai/) - 用于 SQL 生成和相关功能的开源 Python RAG 框架。 [#opensource](https://github.com/vanna-ai/vanna)
- [Portkey](https://portkey.ai/) - 用于 LLM 监控、缓存和管理的全栈 LLMOps 平台。
- [agenta](https://github.com/agenta-ai/agenta) - 用于快速工程、评估和部署的开源端到端 LLMOps 平台。 #开源
- [Together AI](https://www.together.ai/) - 以极快的速度、低成本和生产规模对 AI 模型进行训练、微调和运行推理。
- [Gitingest](https://gitingest.com/) - 将任何 Git 存储库转换为其代码库的简单文本摘要，以便可以将其输入到任何 LLM 中。 [#opensource](https://github.com/cyclotruc/gitingest)
- [Repomix](https://repomix.com/) - 将您的代码库打包为人工智能友好的格式。 [#opensource](https://github.com/yamadashy/repomix)
- [llama.cpp](https://github.com/ggml-org/llama.cpp) - 在纯 C/C++ 中推断 Meta 的 LLaMA 模型（和其他模型）。 #开源
- [bitnet.cpp](https://github.com/microsoft/BitNet) - Microsoft 的 1 位 LLM 官方推理框架。 [#opensource](https://github.com/microsoft/BitNet)
- [OpenRouter](https://openrouter.ai/) - LLM 的统一界面。 [#opensource](https://github.com/OpenRouterTeam)
- [Ludwig](https://github.com/ludwig-ai/ludwig) - 用于构建自定义 AI 模型（如法学硕士和其他深度神经网络）的低代码框架。 [#opensource](https://github.com/ludwig-ai/ludwig)
- [Unsloth](https://unsloth.ai) - 用于微调 LLM 的 Python 库 [#opensource](https://github.com/unslothai/unsloth)。
- [OpenLIT](https://github.com/openlit/openlit) - OpenTelemetry 原生的开源 GenAI 和 LLM 可观测性平台，具有跟踪和指标。 #开源
- [Helicone AI](https://helicone.ai/) - 用于记录、监控和调试 AI 应用程序的开源 LLM 可观察平台。 [#opensource](https://github.com/Helicone/helicone)
- [Wren AI](https://www.getwren.ai/oss) - 具有语义层的开源文本到 SQL 和生成 BI 代理。 [#opensource](https://github.com/Canner/WrenAI)
- [Cleanlab](https://cleanlab.ai/tlm/) - 用于检测 LLM 输出中的幻觉并对其进行评分的 API。
- [Opik](https://github.com/comet-ml/opik) - 用于跟踪、评估和监控 LLM 应用程序的开源平台。 [#opensource](https://github.com/comet-ml/opik)
- [Langfuse](https://langfuse.com/) - 用于跟踪、评估、提示管理和指标的开源 LLM 工程平台。 [#opensource](https://github.com/langfuse/langfuse)
- [MLflow](https://mlflow.org/) - 一个开源平台，用于跟踪 ML 实验、评估模型和提示、部署模型以及添加 LLM 可观察性。 [#opensource](https://github.com/mlflow/mlflow)
- [rehydra](https://github.com/rehydra-ai/rehydra-sdk) - 一个零信任 SDK，用于在向 LLM 发送提示并无缝补充响应之前在本地对 PII 进行匿名化。
- [Agentset](https://agentset.ai/) - 用于构建和评估 RAG 和代理应用程序的开源平台。 [#opensource](https://github.com/agentset-ai/agentset)
- [Manifest](https://manifest.build) - 一个开源 LLM 路由器，可将代理请求路由到最具成本效益的模型，并具有使用限制和模型基准测试。 [#opensource](https://github.com/mnfst/manifest)
- [ai-i18n](https://github.com/i18n-actions/ai-i18n) - 使用 LLM（Claude、GPT、Ollama）自动翻译 i18n 本地化文件的 GitHub Action。 #开源
- [Groq](https://groq.com/) - 用于运行开源 LLM 的云推理 API，由定制 LPU 硬件提供支持。
- [Model Context Protocol](https://modelcontextprotocol.io/) - 用于将人工智能模型连接到外部工具和数据源的开放标准。 [MCP 注册表](https://registry.modelcontextprotocol.io/) [#opensource](https://github.com/modelcontextprotocol/modelcontextprotocol)
- [Steel Browser](https://github.com/steel-dev/steel-browser) - 用于 AI 代理的开源浏览器沙箱和自动化基础设施，具有会话管理、屏幕截图、PDF、代理和反机器人工具。 #开源
- [Bifrost](https://github.com/maximhq/bifrost) - 开源 LLM 网关，具有路由、负载平衡、护栏和 1000 多个模型的可观察性。 #开源

### 游乐场

- [OpenAI Playground](https://platform.openai.com/playground) - 探索资源、教程、API 文档和动态示例。
- [Google AI Studio](https://aistudio.google.com/) - 一个基于网络的工具，用于使用 Gemini 和实验模型进行原型设计。
- [GitHub Models](https://github.com/marketplace/models) - 查找并试验 AI 模型以开发生成式 AI 应用程序。

### 本地法学硕士部署

- [Ollama](https://github.com/ollama/ollama) - 在本地启动并运行大型语言模型。
- [Open WebUI](https://github.com/open-webui/open-webui) - 一个可扩展、功能丰富且用户友好的自托管人工智能平台，旨在完全离线运行。 #开源
- [Jan](https://jan.ai/) - 在您的计算机上本地和离线运行 Mistral 或 Llama2 等 LLM，或连接到远程 AI API。 [#opensource](https://github.com/janhq/jan)
- [Msty](https://msty.ai/) - 适用于本地和在线人工智能模型的简单而强大的界面。
- [PyGPT](https://pygpt.net/) - 个人桌面人工智能助手，具有聊天、视觉、代理、图像生成、工具和命令、语音控制等功能。 #开源
- [LLM](https://llm.datasette.io/) - 用于与远程和本地大型语言模型交互的 CLI 实用程序和 Python 库。 [#opensource](https://github.com/simonw/llm)
- [LM Studio](https://lmstudio.ai) - 在您的计算机上下载并运行本地 LLM。
- [RunThisLLM](https://runthisllm.com) - 查看您可以在您的硬件上运行哪些法学硕士。
- [Harbor](https://github.com/av/harbor) - 一种容器化工具包，用于通过一个命令运行本地 LLM 后端、UI 和支持服务。 #开源
- [off-grid-mobile](https://github.com/alichherawalla/off-grid-mobile-ai) - React Native 应用程序可在 iOS 和 Android 设备上运行 LLM、视觉模型和 Stable Diffusion，无需访问互联网。 #开源

## 代理商

### 自主代理

- [Auto-GPT](https://github.com/Significant-Gravitas/AutoGPT) - 一项让 GPT-4 完全自治的实验性开源尝试。
- [babyagi](https://github.com/yoheinakajima/babyagi) - 人工智能驱动的任务管理系统。
- [AgentGPT](https://github.com/reworkd/AgentGPT) - 在浏览器中组装、配置和部署自主 AI 代理。
- [GPT Engineer](https://github.com/AntonOsika/gpt-engineer) - 指定你想要它构建的内容，AI 会要求澄清，然后构建它。
- [GPT Prompt Engineer](https://github.com/mshumer/gpt-prompt-engineer) - 自动化提示工程。它生成、测试和排名提示以找到最好的提示。
- [MetaGPT](https://github.com/FoundationAgents/MetaGPT) - 多代理框架：给定一行需求，返回 PRD、设计、任务、存储库。
- [AutoGen](https://github.com/microsoft/autogen) - AutoGen 是一个框架，支持使用多个代理来开发 LLM 应用程序，这些代理可以相互对话来解决任务。
- [GPT Pilot](https://github.com/Pythagora-io/gpt-pilot) - 开发工具从头开始编写可扩展的应用程序，同时开发人员监督实施。
- [Devin](https://devin.ai/) - 认知实验室的自主人工智能软件工程师。
- [OpenHands](https://github.com/OpenHands/OpenHands) - 旨在应对软件工程复杂性的自主代理。 #开源
- [Davika](https://github.com/stitionai/devika) - 代理人工智能软件工程师。 #开源
- [n8n](https://n8n.io/) - 一个将人工智能功能与业务流程自动化相结合的工作流自动化平台。
- [Sauna](https://www.sauna.ai) - 专为复合上下文而构建的人工智能助手。它可以了解您的品味、检测隐藏的模式、增强您的大脑环境并主动工作。
- [Claude Code](https://code.claude.com) - Anthropic 的代理编码工具位于您的终端中，可帮助您将想法转化为代码。
- [Gemini CLI](https://geminicli.com) - 一款开源 AI 代理，可将 Gemini 的强大功能直接带入您的终端。 [#opensource](https://github.com/google-gemini/gemini-cli)
- [OpenCode](https://opencode.ai) - 开源人工智能编码代理。 [#opensource](https://github.com/anomalyco/opencode)
- [Mastra](https://mastra.ai) - 用于构建 AI 代理、工作流程和应用程序的 TypeScript 框架。 [#opensource](https://github.com/mastra-ai/mastra)
- [OpenClaw](https://openclaw.ai) - 您在自己的设备上运行的个人人工智能助手。 [#opensource](https://github.com/openclaw/openclaw)
- [moltbook](https://www.moltbook.com) - 人工智能代理的社交网络。
- [AgentMail](https://www.agentmail.to) - AI 代理的电子邮件收件箱。
- [Openwork](https://openwork.bot) - 人工智能代理相互雇佣、完成工作、验证结果并赚取代币。
- [Agent Skills](https://agentskills.io) - 开放格式和参考 SDK，用于打包 AI 代理的可重用功能和专业知识。 [#opensource](https://github.com/agentskills/agentskills)
- [PraisonAI](https://github.com/MervinPraison/PraisonAI) - 用于构建具有工作流程、工具集成和内存的多代理人工智能系统的框架。 #开源
- [Hermes Agent](https://hermes-agent.nousresearch.com) - 具有记忆、消息传递集成和沙盒工具执行功能的自我改进个人代理。 [#opensource](https://github.com/NousResearch/hermes-agent)
- [OpenAgents](https://github.com/openagents-org/openagents) - 用于构建具有多协议支持（WebSocket、gRPC、HTTP、MCP、A2A）的 AI 代理网络的开源平台。 #开源
- [Dorothy](https://github.com/Charlie85270/Dorothy) - 一款开源桌面应用程序，可同时协调多个 AI CLI 代理以及自动化和看板管理。 #开源
- [Hive](https://github.com/aden-hive/hive) - 具有自动生成图、演化循环和 MCP 集成的开源多代理框架。 #开源

### 定制助理

- [Poe](https://poe.com/) - Poe 允许访问各种机器人。
- [GPT Builder](https://chatgpt.com/gpts/editor) - 用于创建基于 GPT 的助手的助手。

## 图片

### 型号

- [DALL·E 2](https://openai.com/dall-e-2/) - OpenAI 的 DALL·E 2 是一种新的人工智能系统，可以根据自然语言的描述创建逼真的图像和艺术。
- [Stable Diffusion](https://huggingface.co/CompVis/stable-diffusion-v1-4) - Stability AI 的稳定扩散是一种最先进的文本到图像模型，可以从文本生成图像。 #开源
- [Midjourney](https://www.midjourney.com/) - Midjourney 是一个独立的研究实验室，致力于探索新的思维媒介并扩展人类的想象力。
- [Imagen](https://imagen.research.google/) - Imagen by Google 是一种文本到图像的扩散模型，具有前所未有的照片真实感和深层次的语言理解能力。
- [Make-A-Scene](https://ai.meta.com/blog/greater-creative-control-for-ai-image-generation/) - Meta 的 Make-A-Scene 是一种多模式生成人工智能方法，将创造性控制权交给使用它的人，允许他们通过文本描述和自由草图来描述和说明他们的愿景。
- [DragGAN](https://github.com/XingangPan/DragGAN) - 拖动您的 GAN：生成图像流形上基于点的交互式操作。
- [Flux](https://github.com/black-forest-labs/flux) - Black Forest Labs 提供的文本到图像模型，具有高质量的逼真输出。 #开源

### 服务

- [Craiyon](https://www.craiyon.com/) - Craiyon（原名 DALL-E mini）是一个 AI 模型，可以根据任何文本提示绘制图像。
- [DreamStudio](https://stability.ai/dreamstudio) - DreamStudio 是一个易于使用的界面，用于使用稳定扩散图像生成模型创建图像。
- [Artbreeder](https://www.artbreeder.com/) - Artbreeder 是一种新型的创意工具，通过让协作和探索变得更容易来增强用户的创造力。
- [Magic Eraser](https://magicstudio.com/magiceraser/) - 在几秒钟内从图像中删除不需要的东西。
- [Imagine by Magic Studio](https://magicstudio.com/imagine) - Magic Studio 的一款工具，让您通过描述您的想法来表达自己。
- [Alpaca](https://www.getalpaca.io/) - 稳定的扩散 Photoshop 插件。
- [Patience.ai](https://www.patience.ai/) - Patience.ai 是一款使用稳定扩散（Stability.AI 开发的尖端人工智能）创建图像的应用程序。
- [GenShare](https://www.genshare.io/) - 在几秒钟内免费生成艺术作品。拥有并分享您所创造的东西。多媒体生成工作室，使设计和创造力民主化。
- [Playground](https://playground.com/) - Playground 是一款免费的在线人工智能图像创建器。用它来创作艺术、社交媒体帖子、演示文稿、海报、视频、徽标等。
- [modyfi](https://www.modyfi.com/) - 一个基于浏览器的设计平台，具有人工智能驱动的图像生成、动画和实时协作功能。
- [PhotoRoom](https://www.photoroom.com/) - 仅使用手机即可创建产品和肖像图片。删除背景、更改背景并展示产品。
- [Photo AI](https://photoai.com/ai-avatars) - 创建您自己的人工智能生成的头像。
- [ClipDrop](https://clipdrop.co/) - 由 [stability.ai](https://stability.ai/) 提供支持，无需摄影工作室即可创建专业视觉效果。
- [Lensa](https://prisma-ai.com/lensa) - 一款一体化图像编辑应用程序，包括使用稳定扩散生成个性化头像。
- [RunDiffusion](https://rundiffusion.com/) - 基于云的工作空间，用于创建人工智能生成的艺术。
- [Ideogram](https://ideogram.ai/) - 一个文本到图像的平台，使创意表达更容易。
- [Bing Image Creator](https://www.bing.com/images/create) - 基于 DALLE·3 的文本到图像生成器，具有安全功能。
- [KREA](https://www.krea.ai/) - 使用了解您的风格、概念或产品的人工智能生成高质量的视觉效果。
- [Nightcafe](https://creator.nightcafe.studio/) - NightCafe Creator 是一款人工智能艺术生成器应用程序，具有多种人工智能艺术生成方法。
- [Leonardo AI](https://leonardo.ai/) - 以前所未有的质量、速度和风格为您的项目创建生产质量的视觉资产。
- [Recraft](https://www.recraft.ai/) - 一款 AI 工具，可让创作者轻松生成和迭代原始图像、矢量艺术、插图、图标和 3D 图形。
- [Reve Image](https://reve.com/) - 一个从头开始训练的模型，在迅速遵守、美观和排版方面表现出色。
- [Magnific](https://www.magnific.com/) - 由人工智能驱动的设计工具，包括图像生成、背景去除和创意模板。
- [FigureLabs](https://www.figurelabs.ai/) - 一种人工智能工具，用于根据文本描述或草图生成矢量格式的可供出版的科学图表。

### 平面设计

- [Brandmark](https://brandmark.io/) - 基于人工智能的标志设计工具。
- [Gamma](https://gamma.app/) - 无需任何格式化和设计工作即可创建精美的演示文稿和网页。
- [Microsoft Designer](https://designer.microsoft.com/) - 令人惊叹的设计瞬间完成。
- [Napkin](https://www.napkin.ai/) - 用于从文本生成图表、图表和信息图表的 AI 工具。

### 图片库

- [Lexica](https://lexica.art/) - 稳定的扩散搜索引擎。
- [OpenArt](https://openart.ai/) - 搜索 10M+ 提示，并通过稳定扩散、DALL·E 2 生成 AI 艺术。
- [PromptHero](https://prompthero.com/) - Stable Diffusion、ChatGPT、Midjourney 等模型的搜索提示。
- [PromptBase](https://promptbase.com/) - 搜索顶级提示工程师的提示。出售您自己的提示。

### 模型库

- [Civitai](https://civitai.com/) - 社区驱动的人工智能模型共享工具。
- [Stable Diffusion Models](https://rentry.org/sdmodels) - rentry.org 上稳定扩散检查点的完整列表。

### 稳定的扩散资源

- [Stable Horde](https://stablehorde.net/) - 稳定扩散工作人员的众包分布式集群。
- [DiffusionDB](https://diffusiondb.com/) - Stable Diffusion 的所有公共应用程序、开发人员工具、指南和插件的列表。 [Airtable 版本](https://airtable.com/shr0HlBwbw3nZ8Ht3/tblxOCylXV8ynh7ti)。
- [PublicPrompts](https://publicprompts.art/) - 稳定扩散的免费提示集合。
- [Hugging Face Diffusion Models Course](https://github.com/huggingface/diffusion-models-class) - [@huggingface](https://github.com/huggingface) 提供的扩散模型在线课程的 Python 材料。
- [ComfyUI](https://github.com/comfyanonymous/ComfyUI) - 用于构建和运行稳定扩散工作流程的基于节点的界面。 [#opensource](https://github.com/comfyanonymous/ComfyUI)

## 视频

- [Runway](https://runwayml.com/) - 神奇的人工智能工具、实时协作、精确编辑等等。您的下一代内容创建套件。
- [Synthesia](https://www.synthesia.io/) - 在几分钟内从纯文本创建视频。
- [Colossyan](https://www.colossyan.com/) - 专注于学习和发展的视频创作者。使用人工智能头像创建多种语言的教育视频。
- [Fliki](https://fliki.ai/) - 使用人工智能语音在几分钟内创建文本到视频和文本到语音内容。
- [Pictory](https://pictory.ai/) - Pictory 强大的人工智能使您能够使用文本创建和编辑专业品质的视频。
- [Pika](https://pika.art/) - 一个将想法转化为视频的平台，可将您的创造力付诸实践。
- [HeyGen](https://app.heygen.com/) - 只需几分钟即可将脚本转换为带有可自定义 AI 头像的对话视频。
- [Luma Dream Machine](https://lumalabs.ai/app) - 一种 AI 模型，可根据文本和图像快速制作高质量、逼真的视频。
- [KLING AI](https://kling.ai/) - 用于创建富有想象力的图像和视频的工具。
- [Hailuo AI](https://hailuoai.video/) - 人工智能驱动的文本到视频生成器。
- [Google Flow](https://labs.google/fx/tools/flow) - 来自 Google 的人工智能电影制作工具，由 Veo 提供支持。
- [Seedance 2.0](https://seed.bytedance.com/en/seedance2_0) - Niobotics ByteDance 开发的图像到视频和文本到视频模型。
- [MaxVideoAI](https://maxvideoai.com/examples) - 用于生成和比较多个 AI 视频模型的视频的工作区。
- [HyperFrames](https://hyperframes.heygen.com/) - 人工智能代理通过编写 HTML、CSS 和 JavaScript 来渲染视频的框架。 [#opensource](https://github.com/heygen-com/hyperframes)

### 头像

- [D-ID](https://www.d-id.com/) - 只需按一下按钮即可创建会说话的化身并与之互动。
- [HeyGen](https://app.heygen.com/) - 只需几分钟即可将脚本转换为带有可自定义 AI 头像的对话视频。
- [Affogato](https://affogato.ai/) - 为 TikTok、Reels 和 Shorts 制作人工智能生成的产品视频广告。

### 动画

- [Autodesk Flow Studio](https://www.autodesk.com/products/flow-studio) - AI 驱动的工具，用于将 CG 角色制作动画并将其合成为真人镜头。

## 音频

### 文字转语音

- [Eleven Labs](https://elevenlabs.io/) - 人工智能语音发生器。
- [Resemble AI](https://www.resemble.ai/) - 用于文本转语音的人工智能语音生成器和语音克隆。
- [WellSaid](https://www.wellsaid.io/) - 实时将文本转换为语音。
- [TorToiSe](https://github.com/neonbjb/tortoise-tts) - 经过训练、注重质量的多语音文本转语音系统。 #开源
- [Bark](https://github.com/suno-ai/bark) - 基于转换器的文本到音频模型。 #开源
- [TTS WebUI](https://github.com/rsxdalv/TTS-WebUI) - 用于运行多个文本转语音、音乐生成和音频工具的 Web UI。 #开源

### 语音转文字

- [Whisper](https://openai.com/index/whisper/) - 通过大规模弱监督实现鲁棒语音识别。 [#opensource](https://github.com/openai/whisper)
- [Wispr Flow](https://wisprflow.ai/) - Flow 通过无缝语音听写为计算机上的任何应用程序提供快速书写。
- [Vibe Transcribe](https://thewh1teagle.github.io/vibe/) - 轻松进行音频和视频转录的一体化解决方案。 [#opensource](https://github.com/thewh1teagle/vibe)
- [whisper.cpp](https://github.com/ggml-org/whisper.cpp) - OpenAI 的 Whisper 模型在 C/C++ 中的移植。 #开源
- [whisper-ctranslate2](https://github.com/Softcatala/whisper-ctranslate2) - 与原始 OpenAI 客户端兼容的 Whisper CLI 客户端，使用 CTranslate2 进行更快的推理。 [#opensource](https://github.com/Softcatala/whisper-ctranslate2)

### 音乐

- [Harmonai](https://www.harmonai.org/) - 我们是一个社区驱动的组织，发布开源生成音频工具，使每个人都能更轻松地进行音乐制作并从中获得乐趣。
- [Mubert](https://mubert.com/) - 为内容创作者、品牌和开发者提供的免版税音乐生态系统。
- [MusicLM](https://google-research.github.io/seanet/musiclm/examples/) - 谷歌研究的一个模型，用于从文本描述生成高保真音乐。
- [AudioCraft](https://audiocraft.metademolab.com/) - Meta 提供的满足生成音频需求的一站式代码库。包括用于音乐的 MusicGen 和用于声音的 AudioGen。 #开源
- [Stable Audio](https://stability.ai/stable-audio) - Stable Audio 是 Stability AI 的首款用于音乐和音效生成的产品。
- [AIVA](https://www.aiva.ai/) - 基于人工智能的音乐生成助手。有 250 多种款式可供选择。
- [Suno AI](https://suno.com/) - 任何人都可以创作出美妙的音乐。不需要任何工具，只需要想象力。从你的思想到音乐。
- [Udio](https://www.udio.com/) - 发现、创作并与世界分享音乐。

## 其他

- [PromptBase](https://promptbase.com/) - 买卖质量提示的市场有 DALL·E、GPT-3、Midjourney、Stable Diffusion。
- [This Image Does Not Exist](https://thisimagedoesnotexist.com/) - 测试您判断图像是人类生成还是计算机生成的能力。
- [Have I Been Trained?](https://haveibeentrained.com/) - 检查您的图像是否已用于训练流行的 AI 艺术模型。
- [AI Dungeon](https://aidungeon.io/) - 这是一款基于文本的冒险故事游戏，由您执导（并主演），而人工智能则将其变为现实。
- [Clickable](https://www.clickable.so/) - 利用人工智能在几秒钟内生成广告。适用于所有营销渠道的精美、品牌一致且转化率高的广告。
- [Scale Spellbook](https://scale.com/genai-platform) - 使用 Scale Spellbook 构建、比较和部署大型语言模型应用程序。
- [Scenario](https://www.scenario.com/) - 人工智能生成的游戏资产。
- [Teleprompter](https://github.com/danielgross/teleprompter) - 设备上的会议人工智能可以倾听您的声音并提出富有魅力的报价建议。
- [FinChat](https://finchat.io/) - FinChat 利用人工智能生成有关上市公司和投资者问题的答案。
- [Morpher AI](https://morpher.com/ai) - Morpher AI 为任何市场提供实时洞察和分析。
- [Whimsical AI](https://whimsical.com/ai) - GPT 支持的思维导图、流程图和可视化工具，用于快速创意开发和流程组织。
- [Selfies with Sama](https://selfies-with-sama.vost.ai) - 与现实生活中的亿万富翁合影！

## 学习资源

- [Learn Prompting](https://learnprompting.org/) - 关于与人工智能通信的免费开源课程。
- [Prompt Engineering Guide](https://github.com/dair-ai/Prompt-Engineering-Guide) - 快速工程指南和资源。
- [ChatGPT prompt engineering for developers](https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/) - Isa Fulford (OpenAI) 和 Andrew Ng (DeepLearning.AI) 的短期课程。
- [OpenAI Cookbook](https://github.com/openai/openai-cookbook) - 使用 OpenAI API 的示例和指南。
- [OpenAI Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering) - 从大型语言模型中获得更好结果的策略和策略。
- [PromptPerfect](https://promptperfect.jina.ai/) - 用于快速工程的工具。
- [Anthropic courses](https://github.com/anthropics/courses) - Anthropic 的教育课程。
- [Build a Large Language Model (From Scratch)](https://www.manning.com/books/build-a-large-language-model-from-scratch) - 建立自己的工作法学硕士指南，作者：Sebastian Raschka。
- [Prompt Engineering for Vision Models](https://www.deeplearning.ai/short-courses/prompt-engineering-for-vision-models/) - 免费的 DeepLearning.AI 短期课程，介绍如何使用自然语言、边界框、分割掩模、坐标点和其他图像来提示计算机视觉模型。
- [Build a Reasoning Model (From Scratch)](https://www.manning.com/books/build-a-reasoning-model-from-scratch) - 从头开始构建有效推理模型的指南，作者：Sebastian Raschka。
- [Build an AI Agent (From Scratch)](https://www.manning.com/books/build-an-ai-agent-from-scratch) - 一本关于使用工具、内存、规划和多代理系统构建人工智能代理的书。
- [Build a DeepSeek Model (From Scratch)](https://www.manning.com/books/build-a-deepseek-model-from-scratch) - 一本关于实现 DeepSeek 风格的 LLM 架构、训练和蒸馏方法的书。
- [AI Governance](https://www.manning.com/books/ai-governance) - 一本关于生成人工智能系统的治理、风险、合规性、安全性、隐私和监督的书。
- [AnimatedLLM](https://animatedllm.github.io/) - 交互式可视化解释大型语言模型如何工作。 [#opensource](https://github.com/kasnerz/animated-llm)
- [Transformer Explainer](https://poloclub.github.io/transformer-explainer/) - 基于 Transformer 的 LLM 如何工作的交互式可视化，在浏览器中运行实时 GPT-2 模型。 [#opensource](https://github.com/poloclub/transformer-explainer)

## 更多列表

- [Tools and Resources for AI Art](https://pharmapsychotic.com/tools.html) - 用于生成 AI 的 Google Colab 笔记本的大量列表，作者：[@pharmapsychotic](https://twitter.com/pharmapsychotic)。
- [The Generative AI Application Landscape](https://twitter.com/sonyatweetybird/status/1584580362339962880) - 红杉资本的 [Sonya Huang](https://twitter.com/sonyatweetybird) 绘制了生成式 AI 生态系统的信息图。
- [Startups - @builtwithgenai](https://airtable.com/shr6nfE9FOHp17IjG/tblL3ekHZfkm3p6YT) - 由 [@builtwithgenai](https://twitter.com/builtwithgenai) 提供的 Airtable 列表。
- [The Generative AI Index](https://airtable.com/shrH4REIgddv8SzUo/tbl5dsXdD1P859QLO) - [Scale Venture Partners](https://www.scalevp.com/generative-ai) 提供的 Airtable 列表。
- [Generative AI for Games](https://twitter.com/gwertz/status/1593268767269670912) - 致力于游戏生成人工智能的公司的市场地图，作者：[a16z](https://a16z.com/)。
- [Generative Deep Art](https://github.com/filipecalegario/awesome-generative-ai) - 用于艺术用途的生成深度学习工具、作品、模型等的精选列表，作者：[@filipecalegario](https://github.com/filipecalegario/)。
- [GPT-3 Demo](https://gpt3demo.com/) - 展示 GPT-3 示例、演示、应用程序、展示和 NLP 用例。
- [GPT-4 Demo](https://gpt4demo.com/) - GPT-4 应用程序和用例。
- [The Generative AI Landscape](https://github.com/ai-collection/ai-collection) - 一系列很棒的生成式人工智能应用程序。
- [Molecular design](https://github.com/AspirinCode/papers-for-molecular-design-using-DL) - 使用生成人工智能和深度学习的分子设计列表。
- [Open LLMs](https://github.com/eugeneyan/open-llms) - 可用于商业用途的开放式法学硕士列表。
- [Awesome Music AI](https://github.com/steven2358/awesome-music-ai) - 用于音乐创作、生成和分析的人工智能工具精选列表。
- [Awesome AI Market Maps](https://github.com/joylarkin/Awesome-AI-Market-Maps) - [Joy Larkin](https://twitter.com/joy) 整理了 2026 年、2025 年和 2024 年人工智能市场地图列表。
- [Awesome RAG Production](https://github.com/Yigtwxx/Awesome-RAG-Production) - 用于构建生产 RAG 系统的工具和资源的精选列表。

### ChatGPT 上的列表

- [Awesome ChatGPT](https://github.com/humanloop/awesome-chatgpt) - 由 [@jordn](https://github.com/jordn) 提供的 ChatGPT 和 GPT-3 出色工具、演示、文档的精选列表。
- [Awesome ChatGPT Prompts](https://github.com/f/prompts.chat) - 与 ChatGPT 模型一起使用的提示示例集合。
- [FlowGPT](https://flowgpt.com/) - 通过最佳提示来扩大您的工作流程。
- [ChatGPT Prompts for Data Science](https://github.com/travistangvh/ChatGPT-Data-Science-Prompts) - ChatGPT 的有用数据科学提示存储库。
- [Awesome ChatGPT](https://github.com/sindresorhus/awesome-chatgpt) - ChatGPT 的另一个很棒的列表。
