<!--lint disable awesome-badge awesome-list-item double-link no-heading-punctuation table-pipe-alignment table-cell-padding-->

# 🦜🕸Awesome LangGraph & LangChain Ecosystem ![Awesome](https://awesome.re/badge.svg) ![Last Updated](https://img.shields.io/github/last-commit/von-development/awesome-LangGraph)

>框架、模板和现实世界项目的权威索引，适合想要 ** 构建、观察、评估和部署 ** 使用LangChain + LangGraph堆栈的有状态、使用工具的人工智能代理的团队。

无论您是对第一个工作流程进行原型设计还是操作生产系统，此列表都映射了代理开发的整个生命周期，从 ** 使用核心库和集成构建 **，到 ** 观察 ** 使用平台工具运行、** 评估 ** 质量和行为以及 ** 部署 ** 可靠的代理应用程序。

** 你会发现什么 **
- 核心框架：LangChain、LangGraph、Deep Agents和LangSmith
- 用于构建、观察、评估和部署代理系统的资源
- 跨模型、载体存储、加载器和工具的集成和MCP工具
- 官方LangChain/LangGraph项目和预构建代理库
- 按用例分组的社区项目（RAG、网络自动化、研究、财务等）
- 入门模板和学习资源，快速提高生产力

欢迎捐款-请参阅[Contributing Guide](CONTRIBUTING.md)。

---

## 目录

- [什么是LangChain/图形生态系统](#hc209a8e6)
  - [生态系统组成部分：](#h34c3c658)
- [LangChain](#langchain)
- [LangGraph](#langgraph)
- [Deep Agents](#deep-agents)
- [LangSmith](#langsmith)
- [LangSmith Fleet](#langsmith-fleet)
- [LangChain 集成与合作伙伴](#h2467e8a1)
- [官方LangGraph项目](#h21126a9e)
  - [专业代理库](#h37eb0794)
  - [应用程序和代理](#h2bc8c2ec)
  - [开发工具](#h2c509530)
- [跨社区项目](#h093e2db6)
  - [生物与健康](#h4455e0f1)
  - [Web自动化和抓取](#hf5300b85)
  - [商业情报和市场研究](#h2bcd6e2e)
  - [聊天界面& GUI](#h39c9e35b)
  - [☁ Cloud & DevOps](#ha841fa3f)
  - [编码/开发代理](#hae02d35e)
  - [Customer Ops](#customer-ops)
  - [数据平台](#h0097a9cf)
  - [数据科学](#h098da08f)
  - [Developer Tools](#developer-tools)
  - [收件箱](#he75969b5)
  - [金融与金融科技](#hb4f9fdd1)
  - [营销](#h916801e9)
  - [媒体和播客](#hbd6acfdb)
  - [机器人技术和人工智能](#h6e7750c1)
  - [RAG &文档处理](#h1f29bfb6)
  - [研究代理](#h4ce1b6ec)
  - [Cybersecurity](#cybersecurity)
  - [安全与治理](#h8537577b)
  - [可持续发展](#h5e2872ce)
  - [收件箱模板和启动器](#h66ddf81d)
  - [工作场所和生产力](#h025ff342)
  - [学习资源](#h7356fd4c)
  - [官方- LangChain学院](#h8281dc78)
  - [社区课程](#h386b02ff)
  - [额外资源](#h74163a37)
  - [社区](#h888af1f2)
- [贡献](#hbb966aa6)
- [确认](#he83a256e)

<a name="hc209a8e6"></a>
## 🌐什么是LangChain/图形生态系统

</div>

**LangChain/图谱生态系统 ** 是一套全面的框架和平台，用于构建、部署和管理LLM-支持的应用程序。虽然 **LangGraph** 可以单独使用，但它可以与任何LangChain产品无缝集成，为开发人员提供了一套完整的构建代理工具。

<div align="center">
<img src="static/langchain_overview.png" width="500" alt="LangChain Ecosystem Overview">
<p><sub>资料来源：<a href="https://python.langchain.com/docs/introduction/">LangChain文档</a></sub></p>
</div>

<a name="h34c3c658"></a>
### 生态系统组成部分：

** LangChain** -提供集成和可组合组件以简化LLM应用程序开发。包含在LangGraph之上构建的代理抽象。

** LangGraph** -用于构建具有复杂工作流程、协作和内存管理的有状态多代理系统的核心框架。

** Deep Agents** -用于构建代理的代理工具，这些代理可以规划、分解复杂任务、使用子代理、使用文件系统工具管理大型上下文以及持久化长期内存。

** LangSmith** -用于观察、评估和部署AI代理和LLM应用程序的平台层，具有跟踪、提示工程、Agent Server部署、沙箱和操作工具。

** LangSmith Fleet** -一个无代码平台，用于从模板创建和管理人工智能代理、连接应用程序和帐户、自动化日常工作并通过批准和监督保持人类控制。

** LangChain集成与合作伙伴 ** -第三方集成和提供商包，可在整个人工智能生态系统中扩展LangChain的功能。这些集成包提供了标准化的界面，以与流行的人工智能服务、数据库和工具一起工作。

---

<div align="center">

<a name="langchain"></a>
## LangChain

</div>

**LangChain** 是使用大型语言模型（LLMs）构建应用程序的基础框架。它提供标准化的接口、可重复使用的组件和广泛的集成，使开发人员能够通过可组合的构建块创建复杂的人工智能应用程序。

<details>
<summary><strong>核心组件和用途 </strong></summary>️

** LangChain应用程序的基本构建模块和高级功能 ** -从基本组件到复杂的人工智能功能。

### 核心部件
* LangChain应用程序的基本构建模块 *

|组件|描述|
|-----------|-------------|
|** 0**|使用LLMs确定采取哪些行动的决策系统|
|** 0**|LLMs的统一接口和跨提供商嵌入模型|
|** 0**|组件之间的结构化通信格式|
|** [Tools](https://docs.langchain.com/oss/python/langchain/tools)**|代理的外部功能调用和集成|
|** 0**|用于维护对话上下文的工作记忆|
|** [Streaming](https://docs.langchain.com/oss/python/langchain/streaming)**|部分结果的实时响应处理|

### 高级用法
* 复杂人工智能应用程序的先进能力和技术 *

|特征|描述|
|---------|-------------|
|** 0**|在整个会话中存在的持久记忆|
|** [Guardrails](https://docs.langchain.com/oss/python/langchain/guardrails)**|针对代理输入、输出和工具使用的安全检查和政策执行|
|** 0**|优化提示和上下文管理的技术|
|** 0**|以特定格式和模式生成响应|
|** 0**|标准化工具集成和上下文共享|
|** 0**|针对敏感代理操作的审批工作流和基于中断的人工监督|
|** 0**|具有多个人工智能代理的协调系统|
|** 0**|高级文档检索和RAG模式|
|** [Runtime](https://docs.langchain.com/oss/python/langchain/runtime)**️|生产部署和运行时管理|
|** 0**|自定义处理层和请求/响应修改|

</details>

<details>
<summary> LangChain图书馆</strong></summary>️

|包|Python|TypeScript|描述|
|---------|--------|------------|-------------|
|**LangChain**|[`langchain`](https://github.com/langchain-ai/langchain/tree/master/libs/langchain)|[`langchain`](https://github.com/langchain-ai/langchainjs/tree/main/langchain)|包含链、代理、检索方法和认知架构的主要框架|
|**LangChain核心 **|[`langchain-core`](https://github.com/langchain-ai/langchain/tree/master/libs/core)|[`@langchain/core`](https://github.com/langchain-ai/langchainjs/tree/main/libs/langchain-core)|整个生态系统的基本抽象和运行时|
|** 社区 **|[`langchain-community`](https://github.com/langchain-ai/langchain/tree/master/libs/community)|[`@langchain/community`](https://github.com/langchain-ai/langchainjs/tree/main/libs/langchain-community)|第三方整合和社区贡献|
|**MCP适配器 **|[`langchain-mcp-adapters`](https://github.com/langchain-ai/langchain-mcp-adapters)|-|使Anthropic MCP工具与代理兼容|
|** 文本拆分器 **|[`langchain-text-splitters`](https://github.com/langchain-ai/langchain/tree/master/libs/text-splitters)|[`@langchain/textsplitters`](https://github.com/langchain-ai/langchainjs/tree/main/libs/langchain-textsplitters)|文档处理和文本拆分实用程序|
|** 实验性 **|[`langchain-experimental`](https://github.com/langchain-ai/langchain/tree/master/libs/experimental)|[`@langchain/experimental`](https://github.com/langchain-ai/langchainjs/tree/main/libs/langchain-experimental)|测试版功能和实验组件|
|**CLI工具 **|[`langchain-cli`](https://github.com/langchain-ai/langchain/tree/master/libs/cli)|-|用于项目管理的命令行界面|
|** 遗产 **|[`langchain-legacy`](https://github.com/langchain-ai/langchain/tree/master/libs/legacy)|-|v1.0之前版本的遗留组件（仅限Python）|
</details>

<details>
<summary> LangChain文件 </strong></summary>️️

访问当前统一文档体验和遗留重定向URL的官方LangChain文档：

<div align="center">

|Docs|Python|JavaScript|注意到|
|------|--------|------------|-------|
|** 当前开源收件箱 **|[Overview](https://docs.langchain.com/oss/python/langchain/overview)|[Overview](https://docs.langchain.com/oss/javascript/langchain/overview)|当前统一的LangChain OSS文档位于“docs.langchain.com”|
|** 遗留重定向 **|[Legacy Entry](https://python.langchain.com/docs/introduction/)|[Legacy Entry](https://js.langchain.com/docs/introduction/)|现在重定向到当前概述文档的旧URL|

</div>

** LLMs和IDE的AI可访问文档格式 ** - LangChain现在在“docs.langchain.com”上公开了一个统一的“llms. text”入口点，以便以编程方式访问LangChain、LangGraph、LangSmith和API引用中的最新文档。

### 可用文件

|范围|llms.txt|llms-full.txt|
|-------|----------|---------------|
|** 统一LangChain **|[docs.langchain.com/llms.txt](https://docs.langchain.com/llms.txt)|N/A|
|** 遗留重定向 **|[python.langchain.com/llms.txt](https://python.langchain.com/llms.txt)，[js.langchain.com/llms.txt](https://js.langchain.com/llms.txt)|N/A|

### 幅面差异化
- **' llms. text '** -统一索引文件，包含最新LangChain生态系统文档的链接和摘要
- ** 旧版`llms.txt` URL ** -当前重定向到统一文档文件的旧版Python和JavaScript端点

> ** 查看输出 **：即使有最新的文档，当前模型也可能不总是生成正确的代码。在生产使用之前始终审查生成的代码。

</details>

<n></n>

---

<div align="center">

<a name="langgraph"></a>
## LangGraph

</div>

**LangGraph** 是一个开源框架，用于将 **AI代理和多代理系统 ** 构建为图形，是 **LangChain生态系统 ** 的核心部分。它专注于 ** 代理编排 **，支持复杂的人工智能应用程序，这些应用程序可以维护状态、协调多个代理并通过基于图形的工作流程处理复杂的推理过程。

<details>
<summary><strong>核心功能 </strong></summary>️

|能力|描述|关键特征|
|------------|-------------|--------------|
|** 持久性 **|执行和失败的状态持续性|检查点、状态恢复、会话连续性|
|** 持久执行 **|构建在故障中持续存在并长时间运行的代理|自动恢复、故障恢复、长时间运行的工作流程|
|** 流媒体 **|实时执行，包含部分结果和实时更新|令牌流媒体、进度跟踪、响应式用户体验|
|* *️|用于人工输入、审查和干预的绘图仪执行|批准检查点、状态编辑、可搜索的工作流程|
|** 时间旅行 **|浏览代理执行历史记录和状态|状态调试、执行回放、历史分析|
|** 添加和管理内存 **|针对有状态代理的全面内存管理|短期工作记忆、长期坚持、记忆优化|
|** T27**|用于复杂工作流程组合的嵌套图形结构|模块化工作流程、可重用组件、分层执行|
|** 0**|具有单元和部分执行测试模式的地理图行为|节点测试、部分执行、基于检查指针的测试设置|
|** 0**|使用LangSmith跟踪和调试图形执行|执行跟踪、状态检查、运行时监控|

</details>

<details>
<summary> LangGraph图书馆和SDKs </strong></summary>️

|包|Python|TypeScript|描述|
|---------|--------|------------|-------------|
|**LangGraph**|[`langgraph`](https://github.com/langchain-ai/langgraph)|[`@langchain/langgraph`](https://github.com/langchain-ai/langgraphjs)|核心基于图的代理编排框架|
|**LangGraph CLI**|[`langgraph-cli`](https://github.com/langchain-ai/langgraph/tree/main/libs/cli)|[`@langchain/langgraph-cli`](https://github.com/langchain-ai/langgraphjs/tree/main/libs/langgraph-cli)|用于LangGraph开发和部署的命令行界面|
|**LangGraph SDK**|[Python SDK](https://docs.langchain.com/langgraph-platform/sdk)|[JavaScript SDK](https://docs.langchain.com/langgraph-platform/sdk)|官方SDK用于与 **LangGraph平台（服务器）** 和部署的应用程序交互|

</details>

<details>
<summary><strong>文档 LangGraph文档</strong></summary>️

访问当前统一开源文档中的官方LangGraph文档：

<div align="center">

|Docs|Python|JavaScript|注意到|
|------|--------|------------|-------|
|** 当前开源收件箱 **|[Overview](https://docs.langchain.com/oss/python/langgraph/overview)|[Overview](https://docs.langchain.com/oss/javascript/langgraph/overview)|当前LangGraph OSS文档位于“docs.langchain.com”|
|** 快速入门 **|[Quickstart](https://docs.langchain.com/oss/python/langgraph/quickstart)|[Quickstart](https://docs.langchain.com/oss/javascript/langgraph/quickstart)|使用工具、内存和流媒体构建第一个LangGraph应用程序|

</div>

** LLMs和IDE的AI可访问文档格式 ** - LangGraph文档是统一' docs.langchain.com ' docs体验的一部分，因此主要' llms. url '入口点在更广泛的生态系统文档中共享。

|范围|llms.txt|llms-full.txt|
|-------|----------|---------------|
|** 统一LangChain **|[docs.langchain.com/llms.txt](https://docs.langchain.com/llms.txt)|N/A|

</details>

<n></n>

---

<div align="center">

<a name="deep-agents"></a>
<a name="deep-agents"></a>
## Deep Agents

</div>

**Deep Agents** 是一个开源代理工具，用于构建代理，这些代理可以规划、委托给子代理、使用文件系统工具管理上下文，并为复杂的多步骤任务持久化长期内存。

<details>
<summary><strong>核心能力</strong></summary>

|能力|描述|关键特征|
|------------|-------------|--------------|
|** [Planning & Task Decomposition](https://docs.langchain.com/oss/python/deepagents/overview)**|将大型任务分解为可管理的步骤并跟踪进展|内置待办事项系统、自适应规划、多步骤执行|
|** 0**|通过文件系统工具卸载和管理大型上下文|虚拟文件系统、文件读/写/编辑工具、上下文压缩|
|** 0**|将工作委托给专业代理进行上下文隔离|内置任务委托、专门的子任务、更清晰的主代理上下文|
|** 0**|跨线程和会话持久有用信息|长期记忆、记忆储存、跨线程回忆|
|** [Human-in-the-Loop](https://docs.langchain.com/oss/python/deepagents/human-in-the-loop)**|为敏感操作添加审批检查点|批准控制、可预见的执行、工具级监督|
|** 0**|需要时在隔离环境中执行代码|沙箱后端、安全执行、远程运行时选项|
|** [Streaming](https://docs.langchain.com/oss/python/deepagents/streaming)**|实时流媒体中间输出和代理进度|实时进度更新、流式响应、响应式用户体验|
|** [Skills](https://docs.langchain.com/oss/python/deepagents/skills)**|具有可重复使用的特定任务专业知识扩展代理|技能目录、渐进披露、自定义说明|

</details>

<details>
<summary> Deep Agents SDK和CLI </strong></summary>️️

|包|Python|TypeScript|描述|
|---------|--------|------------|-------------|
|**Deep Agents SDK**|[`deepagents`](https://github.com/langchain-ai/deepagents)|[`deepagents`](https://github.com/langchain-ai/deepagents)|独立开源库，用于构建具有规划、子代理、文件系统工具和长期内存的代理|
|**Deep Agents CLI**|[CLI Docs](https://docs.langchain.com/oss/python/deepagents/cli/overview)|[CLI Docs](https://docs.langchain.com/oss/javascript/deepagents/cli/overview)|基于Deep Agents SDK构建的开源终端编码代理|

</details>

<details>
<summary><strong>文档 Deep Agents文档</strong></summary>️

访问当前统一开源文档中的官方Deep Agents文档：

<div align="center">

|Docs|Python|JavaScript|注意到|
|------|--------|------------|-------|
|** 当前开源收件箱 **|[Overview](https://docs.langchain.com/oss/python/deepagents/overview)|[Overview](https://docs.langchain.com/oss/javascript/deepagents/overview)|当前Deep Agents OSS文档位于“docs.langchain.com”|
|** 快速入门 **|[Quickstart](https://docs.langchain.com/oss/python/deepagents/quickstart)|[Quickstart](https://docs.langchain.com/oss/javascript/deepagents/quickstart)|使用工具、规划和内存构建第一个深度代理|
|**CLI**|[CLI Overview](https://docs.langchain.com/oss/python/deepagents/cli/overview)|[CLI Overview](https://docs.langchain.com/oss/javascript/deepagents/cli/overview)|基于Deep Agents SDK构建的终端编码代理|

</div>

** LLMs和IDE ** - Deep Agents文档的AI可访问文档格式可通过LangChain生态系统中使用的相同统一的`docs.langchain.com` docs索引获得。

|范围|llms.txt|llms-full.txt|
|-------|----------|---------------|
|** 统一LangChain **|[docs.langchain.com/llms.txt](https://docs.langchain.com/llms.txt)|N/A|

</details>

<n></n>

---

<div align="center">

<a name="langsmith"></a>
## LangSmith

</div>

**LangSmith** 是一个框架不可知的平台，用于构建、调试、评估和部署AI代理和LLM应用程序。无论是否使用LangChain的开源框架，它都可以使用，并将可观察性、及时工程、部署和运营工具整合到一个工作流程中。

<details>
<summary><strong>核心功能</strong></summary>🔹

|特征|描述|关键能力|
|---------|-------------|-----------------|
|* *🚀|将代理部署为生产就绪Agent Servers|托管部署、扩展、代理运行时、生产托管|
|** 0**|了解您的应用程序为更快地调试和提高可靠性而采取的每个步骤|跟踪、仪表板、警报、见解、自动化|
|** 0**|随着时间的推移测量和跟踪应用程序质量|离线实验，在线评估器，LLM-作为法官，评估器工具|
|** [Prompt Engineering](https://docs.langchain.com/langsmith/prompt-engineering)**️|通过内置版本控制和协作迭代提示|即时测试、版本控制、协作、提交历史记录|
|** 0**|在视觉界面中设计、测试和完善端到端应用程序|视觉开发、提示迭代、调试工作流程|
|** [Sandboxes](https://docs.langchain.com/langsmith/sandboxes)**|在隔离的执行环境中运行代码和工具|安全执行、沙箱SDK、受控运行时环境|
|** 平台 设置 **|配置LangSmith用于云、混合或自托管使用|管理控制、合规性、数据治理、基础设施选项|

</details>

<details>
<summary> LangSmith SDK </strong></summary>🔹🔹

|包|Python|TypeScript|描述|
|---------|--------|------------|-------------|
|**LangSmith 客户T61**|[`langsmith`](https://github.com/langchain-ai/langsmith-sdk)|[`langsmith`](https://github.com/langchain-ai/langsmith-sdk)|官方SDK用于LangSmith平台集成|

</details>

<details>
<summary> LangSmith文件</strong></summary>🔹

访问官方LangSmith平台文档：

<div align="center">

|收件箱区域|文件|注意到|
|-----------|---------------|-------|
|** 概览 **|[LangSmith Docs](https://docs.langchain.com/langsmith/home)|LangSmith平台的主要入口点|
|** 部署 **|[Deployment](https://docs.langchain.com/langsmith/deployment)|在生产中将代理部署为Agent Server|
|** 可观察性 **|[Observability](https://docs.langchain.com/langsmith/observability)|跟踪、仪表板、警报和监视工作流|
|** 评估 **|[Evaluation](https://docs.langchain.com/langsmith/evaluation)|人工智能系统的线下和在线评估工作流程|
|** 快速工程 **|[Prompt Engineering](https://docs.langchain.com/langsmith/prompt-engineering)|提示迭代、测试和版本控制|
|** 工作室 **|[Studio](https://docs.langchain.com/langsmith/studio)|用于构建和完善应用程序的视觉界面|
|** 沙箱 *|[Sandboxes](https://docs.langchain.com/langsmith/sandboxes)|工具和代码的隔离执行环境|
|**Agent Server**|[Agent Server](https://docs.langchain.com/langsmith/agent-server)|已部署代理的收件箱和API浮出水面|

</div>

** LLMs和IDE ** - LangSmith的AI可访问文档格式也包含在用于编程访问的统一&#39;docs.langchain.com&#39; docs索引中。

|范围|llms.txt|llms-full.txt|
|-------|----------|---------------|
|** 统一LangChain **|[docs.langchain.com/llms.txt](https://docs.langchain.com/llms.txt)|N/A|

</details>

<details>
<summary>可观察性<strong>LangSmith Claude代码插件</strong> - LangSmith用于Claude代码插件</summary>的可观察性插件

** 将LangSmith跟踪和可观察性直接集成到Claude代码工作流程中。**将Claude代码会话连接到LangSmith，以在IDE内捕获跟踪、监视运行并评估代理行为。

| | |
|---|---|
|** 仓库 **|[`langsmith-claude-code-plugins`](https://github.com/langchain-ai/langsmith-claude-code-plugins)|
|**GitHub星星 **|![GitHub stars](https://img.shields.io/github/stars/langchain-ai/langsmith-claude-code-plugins?style=social)|
|** 上次承诺 **|![GitHub last commit](https://img.shields.io/github/last-commit/langchain-ai/langsmith-claude-code-plugins)|

</details>

<n></n>

> [! TIP]
> ** 免费开始使用LangSmith！**在[langchain.com/langsmith](https://www.langchain.com/langsmith)注册，并按照[deployment quickstart](https://docs.langchain.com/langsmith/deployment-quickstart)、[observability quickstart](https://docs.langchain.com/langsmith/observability-quickstart)或[evaluation quickstart](https://docs.langchain.com/langsmith/evaluation-quickstart)，具体取决于您想从哪里开始。

<n></n>

---

<div align="center">

<a name="langsmith-fleet"></a>
<a name="langsmith-fleet"></a>
## LangSmith Fleet

</div>

**LangSmith Fleet** 是一个无代码工作空间，用于为实际工作构建人工智能代理。从模板开始或用简单的英语描述您的目标，连接Gmail、Google Calendar、Slack、Exa、Tavily和远程MCP服务器等工具，让代理自动化日常工作流程，同时保持人类的控制。

<details>
<summary><strong>核心功能</strong></summary>🔹

|特征|描述|关键能力|
|---------|-------------|-----------------|
|** 0**|无需编写代码即可创建和管理代理|基于模板的设置、AI辅助配置、可编辑指令|
|** 0**|通过应用程序集成将上下文和操作带入代理|Gmail、Google Calendar、Slack、Tavily、Exa、远程MCP服务器|
|** 0**|使用您的团队已经工作的代理|Slack与Microsoft Teams集成、渠道内工作流程|
|** [Schedules](https://docs.langchain.com/langsmith/fleet/schedules)**|自动运行重复性任务|每日简报、定期报告、定时自动化|
|** [Access & Oversight](https://docs.langchain.com/langsmith/fleet/access-and-oversight)**|让人类控制重要操作|审批流程、监督控制、更安全的自动化|
|** [Skills](https://docs.langchain.com/langsmith/fleet/skills)**|具有可重复使用的特定于任务的行为扩展代理|专业指令、可重复使用的工作流程、范围内的能力|

</details>

<details>
<summary> LangSmith Fleet文件</strong></summary>🔹

访问官方LangSmith Fleet文档：

<div align="center">

|收件箱区域|文件|注意到|
|-----------|---------------|-------|
|** 概览 **|[LangSmith Fleet](https://docs.langchain.com/langsmith/fleet)|Fleet的主要入口|
|** 快速入门 **|[Quickstart](https://docs.langchain.com/langsmith/fleet/quickstart)|构建您的第一个Fleet代理|
|** 要点 **|[Essentials](https://docs.langchain.com/langsmith/fleet/essentials)|连接、自动化、内存和批准|
|** 模板 **|[Templates](https://docs.langchain.com/langsmith/fleet/templates)|浏览现成的入门代理并自定义它们|
|** 工具 **|[Tools](https://docs.langchain.com/langsmith/fleet/tools)|将应用和服务连接到您的座席|
|** 频道 **|[Channels](https://docs.langchain.com/langsmith/fleet/channels)|使用Slack中的Fleet和团队工作流程|
|** 时间表 **|[Schedules](https://docs.langchain.com/langsmith/fleet/schedules)|触发重复性任务和自动化|

</div>
</details>

<details>
<summary> T56模板</strong></summary>🔹

Fleet包括用于实际工作流程的现成模板，例如：

- 每日日历简报
- 电子邮件助手
- LinkedIn Recruiter
- 社交媒体AI监控器
- 竞争对手研究

在此处浏览完整的模板目录：

[LangSmith Fleet Templates](https://docs.langchain.com/langsmith/fleet/templates)

</details>

<n></n>

---

<div align="center">

<a name="h2467e8a1"></a>
## LangChain 集成与合作伙伴

</div>

** 第三方集成和提供商包 ** 扩展了LangChain在人工智能生态系统中的功能。这些集成包提供了标准化的界面，以与流行的人工智能服务、数据库和工具一起工作。

<details>
<summary><strong>聊天模式</strong></summary>🔸

** 使用消息序列作为对话人工智能的输入/输出的语言模型。**支持工具调用、结构化输出、流媒体和多模式输入，以构建复杂的聊天应用程序。

- **Python**：[Browse providers](https://docs.langchain.com/oss/python/integrations/chat)
- **JavaScript**：[Browse providers](https://docs.langchain.com/oss/javascript/integrations/chat)

</details>

<details>
<summary><strong>工具和工具包</strong></summary>

** 使代理能够与外部系统交互。**定义工具调用和执行操作的输入模式。支持网络搜索、数据库查询、文件操作、浏览器控制和API集成。

- **Python**：[Browse providers](https://docs.langchain.com/oss/python/integrations/tools)
- **JavaScript**：[Browse providers](https://docs.langchain.com/oss/javascript/integrations/tools)

</details>

<details>
<summary><strong>中间件 2</summary>🔸

** 控制和自定义每一步的代理执行。**添加日志记录、再试、护栏、人工批准、速率限制、提示转换和其他执行时行为。

- **Python**：[Browse middleware](https://docs.langchain.com/oss/python/langchain/middleware/overview)
- **JavaScript**：[Browse middleware](https://docs.langchain.com/oss/javascript/langchain/middleware/overview)

</details>

<details>
<summary><strong>沙盒</strong></summary>🔸

** 在隔离执行环境中运行代理生成的代码。**沙盒为Shell访问、文件系统操作和代码执行提供了更安全的边界。

- **Python**：[Browse providers](https://docs.langchain.com/oss/python/integrations/sandboxes)
- **JavaScript**：-

</details>

<details>
<summary><strong>检查指针</strong></summary>🔸

** LangGraph状态的持久性后台。**使用内存中、SQL、Redis、MongoDB、云和其他检查点存储在交互中保存和恢复代理状态。

- **Python**：[Browse providers](https://docs.langchain.com/oss/python/integrations/checkpointers)
- **JavaScript**：-

</details>

<details>
<summary> <strong>猎犬</strong></summary>🔸🔸

** 结合密集和稀疏搜索方法的高级检索策略。**为RAG应用程序启用复杂的文档检索模式，包括混合搜索、重新排序和上下文感知检索。

- **Python**：[Browse providers](https://docs.langchain.com/oss/python/integrations/retrievers)
- **JavaScript**：[Browse providers](https://docs.langchain.com/oss/javascript/integrations/retrievers)

</details>

<details>
<summary><strong>文本拆分器</strong></summary>

** 将大文档分解为更小的、可管理的块。**在适应模型上下文窗口的同时保持语义一致性。对于RAG管道和文档处理工作流程至关重要。

- **Python**：[Browse providers](https://docs.langchain.com/oss/python/integrations/splitters)
- **JavaScript**：[Browse providers](https://docs.langchain.com/oss/javascript/integrations/splitters)

</details>

<details>
<summary><strong>嵌入模型</strong></summary>🔸

** 将原始文本转换为捕捉语义含义的固定长度载体。**使机器能够根据含义而不是确切的单词来比较和搜索文本。对于检索、语义搜索和排名工作流程至关重要。

- **Python**：[Browse providers](https://docs.langchain.com/oss/python/integrations/text_embedding)
- **JavaScript**：[Browse providers](https://docs.langchain.com/oss/javascript/integrations/text_embedding)

</details>

<details>
<summary> <strong> </strong></summary>🔸

** 数据库针对使用相似性指标存储和查询多维载体进行了优化。**与嵌入模型一起使用来支持语义搜索、检索和知识库应用程序。

- **Python**：[Browse providers](https://docs.langchain.com/oss/python/integrations/vectorstores)
- **JavaScript**：[Browse providers](https://docs.langchain.com/oss/javascript/integrations/vectorstores)

</details>

<details>
<summary><strong>文档加载器</strong></summary>🔸

** 集成从文件、网站、数据库、APIs和云系统中获取数据。**将不同的源转换为LangChain“文档”对象以进行下游处理。

- **Python**：[Browse providers](https://docs.langchain.com/oss/python/integrations/document_loaders)
- **JavaScript**：[Browse providers](https://docs.langchain.com/oss/javascript/integrations/document_loaders)

</details>

<n></n>

---

<div align="center">

<a name="h21126a9e"></a>
## 官方LangGraph项目

</div>

* 使用LangChain生态系统构建的应用程序和工具示例，范围从实验项目到展示不同功能和用例的生产就绪解决方案。*

<div align="center">

<a name="h37eb0794"></a>
### 专业代理库

</div>

* 针对特定用例和交互模式预构建的代理包：*

<details>
<summary> <strong>Computer Use Agent </strong> -自动化计算机交互和图形用户界面任务 </summary>️️

** 用于自动化计算机交互和图形用户界面任务的高级代理。**为复杂的桌面自动化工作流程提供复杂的屏幕交互功能、点击/打字自动化和视觉推理。

| | |
|---|---|
|**Python**|[`langgraph-cua-py`](https://github.com/langchain-ai/langgraph-cua-py)|
|**TypeScript**|[`langgraph-cua`](https://github.com/langchain-ai/langgraphjs/tree/main/libs/langgraph-cua)|
|**GitHub星星 **|![GitHub stars](https://img.shields.io/github/stars/langchain-ai/langgraph-cua-py?style=social)|
|** 上次承诺 **|![GitHub last commit](https://img.shields.io/github/last-commit/langchain-ai/langgraph-cua-py)|

</details>

<details>
<summary> <strong>Swarm Agent </strong> -协调多个专业代理 </summary>️️

** 用于分布式任务执行的多代理协调系统。**实现多个专业代理之间的动态任务分配和集体智能，共同解决复杂问题。

| | |
|---|---|
|**Python**|[`langgraph-swarm-py`](https://github.com/langchain-ai/langgraph-swarm-py)|
|**TypeScript**|[`langgraph-swarm`](https://github.com/langchain-ai/langgraphjs/tree/main/libs/langgraph-swarm)|
|**GitHub星星 **|![GitHub stars](https://img.shields.io/github/stars/langchain-ai/langgraph-swarm-py?style=social)|
|** 上次承诺 **|![GitHub last commit](https://img.shields.io/github/last-commit/langchain-ai/langgraph-swarm-py)|

</details>

<details>
<summary> <strong>主管</strong> -分层多代理协调 </summary>️

** 代理编排和工作流程监督系统。**为复杂的分层代理架构提供高级的多代理协调、任务委托和工作流程管理。

| | |
|---|---|
|**Python**|[`langgraph-supervisor-py`](https://github.com/langchain-ai/langgraph-supervisor-py)|
|**TypeScript**|[`langgraph-supervisor`](https://github.com/langchain-ai/langgraphjs/tree/main/libs/langgraph-supervisor)|
|**GitHub星星 **|![GitHub stars](https://img.shields.io/github/stars/langchain-ai/langgraph-supervisor-py?style=social)|
|** 上次承诺 **|![GitHub last commit](https://img.shields.io/github/last-commit/langchain-ai/langgraph-supervisor-py)|

</details>

<details>
<summary> <strong> MCP适配器</strong> -集成Anthropic MCP工具与代理 </summary>️

** LangChain代理的模型上下文协议集成。**提供工具兼容性和协议桥接，以无缝集成Anthropic MCP工具与代理工作流程。

| | |
|---|---|
|**Python**|[`langchain-mcp-adapters`](https://github.com/langchain-ai/langchain-mcp-adapters)|
|**TypeScript**|--|
|**GitHub星星 **|![GitHub stars](https://img.shields.io/github/stars/langchain-ai/langchain-mcp-adapters?style=social)|
|** 上次承诺 **|![GitHub last commit](https://img.shields.io/github/last-commit/langchain-ai/langchain-mcp-adapters)|

</details>

<details>
<summary> <strong>LangMem</strong> -构建具有持续学习能力的代理</summary>️

** 先进的内存管理系统，用于持久的代理学习。**为随着时间的推移而学习和改进的代理提供内存管理、体验回放和适应。

| | |
|---|---|
|**Python**|[`langmem`](https://github.com/langchain-ai/langmem)|
|**TypeScript**|--|
|**GitHub星星 **|![GitHub stars](https://img.shields.io/github/stars/langchain-ai/langmem?style=social)|
|** 上次承诺 **|![GitHub last commit](https://img.shields.io/github/last-commit/langchain-ai/langmem)|

</details>

<details>
<summary> <strong> BigTools </strong> -处理大规模工具生态系统 </summary>️

** 大规模刀具管理优化系统。**提供先进的刀具管理和智能选择优化，以高效处理复杂的刀具生态系统。

| | |
|---|---|
|**Python**|[`langgraph-bigtool`](https://github.com/langchain-ai/langgraph-bigtool)|
|**TypeScript**|--|
|**GitHub星星 **|![GitHub stars](https://img.shields.io/github/stars/langchain-ai/langgraph-bigtool?style=social)|
|** 上次承诺 **|![GitHub last commit](https://img.shields.io/github/last-commit/langchain-ai/langgraph-bigtool)|

</details>

<details>
<summary> <strong>Deep Agents</strong> -复杂的长期规划和执行 </summary>️

** 先进的代理，用于复杂、长期的规划和执行。**具有复杂的规划工具、子代理编排、文件系统访问以及用于处理复杂多步骤任务的详细提示。

| | |
|---|---|
|**Python**|[`deepagents`](https://github.com/langchain-ai/deepagents)|
|**TypeScript**|--|
|**GitHub星星 **|![GitHub stars](https://img.shields.io/github/stars/langchain-ai/deepagents?style=social)|
|** 上次承诺 **|![GitHub last commit](https://img.shields.io/github/last-commit/langchain-ai/deepagents)|

</details>

<details>
<summary> <strong>Open Deep Research2 -自动化博士级研究代理</summary>

** 可配置深度研究代理，用于自动化研究任务。**通过多模型支持、MCP兼容性和评估基准跨多个来源执行全面研究。在深度研究平台排行榜上取得与流行研究代理相当的表现。

| | |
|---|---|
|**Python**|[`open_deep_research`](https://github.com/langchain-ai/open_deep_research)|
|**TypeScript**|--|
|**GitHub星星 **|![GitHub stars](https://img.shields.io/github/stars/langchain-ai/open_deep_research?style=social)|
|** 上次承诺 **|![GitHub last commit](https://img.shields.io/github/last-commit/langchain-ai/open_deep_research)|

</details>

---

<div align="center">

<a name="h2bc8c2ec"></a>
### 应用程序和代理📱

</div>

* 展示不同模式和用例的完整应用示例：*

<details>
<summary> LangConnect<strong>LangConnect</strong> -托管的RAG服务，与FastAPI集成在一起</summary>️️

** 托管RAG服务与FastAPI和PostgreSQL/pgvector集成。**具有文档收集管理、语义搜索和对生产就绪RAG应用程序的Docker部署支持。

| | |
|---|---|
|** 仓库 **|[`langconnect`](https://github.com/langchain-ai/langconnect)|
|**GitHub星星 **|![GitHub stars](https://img.shields.io/github/stars/langchain-ai/langconnect?style=social)|
|** 上次承诺 **|![GitHub last commit](https://img.shields.io/github/last-commit/langchain-ai/langconnect)|

</details>

<details>
<summary> <strong>聊天LangChain</strong> -具有RAG的文档助理-基于搜索 </summary>️️

** 文档助手由RAG提供支持，基于语义搜索，具有智能查询分析。**具有自动内容索引、防重复、GenUI和复杂的文档跟踪系统。

| | |
|---|---|
|** 仓库 **|[`chat-langchain`](https://github.com/langchain-ai/chat-langchain)|
|**GitHub星星 **|![GitHub stars](https://img.shields.io/github/stars/langchain-ai/chat-langchain?style=social)|
|** 上次承诺 **|![GitHub last commit](https://img.shields.io/github/last-commit/langchain-ai/chat-langchain)|

</details>

<details>
<summary> <strong>Agent Inbox</strong> -人工智能代理交互的集中式接口</summary>

** 用于人工智能代理交互的集中式界面，具有实时通信。**包括适用于本地和云部署的中断处理和可配置响应系统。

| | |
|---|---|
|** 仓库 **|[`agent-inbox`](https://github.com/langchain-ai/agent-inbox)|
|**GitHub星星 **|![GitHub stars](https://img.shields.io/github/stars/langchain-ai/agent-inbox?style=social)|
|** 上次承诺 **|![GitHub last commit](https://img.shields.io/github/last-commit/langchain-ai/agent-inbox)|

</details>

<details>
<summary> <strong>Python Fullstack</strong> -具有现代UI的一体化聊天机器人模板 </summary>️

** 一体化聊天机器人模板，将React风格的代理与现代UI相结合。**采用FastHTML组件和Claude 3构建，具有单一部署架构和可扩展工具。

| | |
|---|---|
|** 仓库 **|[`langgraph-fullstack-python`](https://github.com/langchain-ai/langgraph-fullstack-python)|
|**GitHub星星 **|![GitHub stars](https://img.shields.io/github/stars/langchain-ai/langgraph-fullstack-python?style=social)|
|** 上次承诺 **|![GitHub last commit](https://img.shields.io/github/last-commit/langchain-ai/langgraph-fullstack-python)|

</details>

<details>
<summary> <strong> LangChain Next.js</strong> - Next.js LangChain.js </summary>的初始模板️

**Next.js入门模板展示LangChain.js模块。**包括流聊天、结构化输出、多步骤代理以及与Vercel AI SDK集成的RAG实施。

| | |
|---|---|
|** 仓库 **|[`langchain-nextjs-template`](https://github.com/langchain-ai/langchain-nextjs-template)|
|**GitHub星星 **|![GitHub stars](https://img.shields.io/github/stars/langchain-ai/langchain-nextjs-template?style=social)|
|** 上次承诺 **|![GitHub last commit](https://img.shields.io/github/last-commit/langchain-ai/langchain-nextjs-template)|

</details>

<details>
<summary> <strong>多模式研究员</strong> -研究和播客生成工作流程 </summary>️️

** 使用LangGraph和Gemini 2.5模型系列进行研究和播客生成工作流程。**具有视频理解、Google搜索集成和多说话者文本转语音功能，用于创建全面的研究报告和音频播客。

| | |
|---|---|
|** 仓库 **|[`multi-modal-researcher`](https://github.com/langchain-ai/multi-modal-researcher)|
|**GitHub星星 **|![GitHub stars](https://img.shields.io/github/stars/langchain-ai/multi-modal-researcher?style=social)|
|** 上次承诺 **|![GitHub last commit](https://img.shields.io/github/last-commit/langchain-ai/multi-modal-researcher)|

</details>

<details>
<summary> <strong>Deep Agents UI</strong> - Next.js Deep Agents </summary>

**Next.js接口，用于Deep Agents，具有流媒体支持和LangGraph平台集成。**通用人工智能代理能够通过可定制的UI组件处理不同复杂性的任务。

| | |
|---|---|
|** 仓库 **|[`deep-agents-ui`](https://github.com/langchain-ai/deep-agents-ui)|
|**GitHub星星 **|![GitHub stars](https://img.shields.io/github/stars/langchain-ai/deep-agents-ui?style=social)|
|** 上次承诺 **|![GitHub last commit](https://img.shields.io/github/last-commit/langchain-ai/deep-agents-ui)|

</details>

<details>
<summary> <strong>Gen UI计算机使用</strong> -适用于Computer Use Agents </summary>的生成UI Web应用程序️

** 一个生成式UI Web应用程序，用于与Computer Use Agent（CUA）交互。**使用'@langchain/langgraph-cua '预构建包，并具有计算机自动化和任务管理的现代化界面。

| | |
|---|---|
|** 仓库 **|[`gen-ui-computer-use`](https://github.com/bracesproul/gen-ui-computer-use)|
|**GitHub星星 **|![GitHub stars](https://img.shields.io/github/stars/bracesproul/gen-ui-computer-use?style=social)|
|** 上次承诺 **|![GitHub last commit](https://img.shields.io/github/last-commit/bracesproul/gen-ui-computer-use)|

</details>

<details>
<summary> <strong>Social Media Agent</strong> -从URL生成社交媒体帖子 </summary>️️

** 从URL生成Twitter和LinkedIn帖子，并可选择进行人工审查。**具有内容分析、平台特定的格式化和社交媒体内容创建的审批工作流程。

| | |
|---|---|
|** 仓库 **|[`social-media-agent`](https://github.com/langchain-ai/social-media-agent)|
|**GitHub星星 **|![GitHub stars](https://img.shields.io/github/stars/langchain-ai/social-media-agent?style=social)|
|** 上次承诺 **|![GitHub last commit](https://img.shields.io/github/last-commit/langchain-ai/social-media-agent)|

</details>

<details>
<summary> <strong>开放SWE</strong> -开源同步编码代理</summary>️

** 基于LangGraph构建的开源同步编码代理，用于长期运行的自主软件工程任务。**支持Anthropic和OpenAI模型，专为复杂的多步骤代码生成和修改工作流程而设计。

| | |
|---|---|
|** 仓库 **|[`open-swe`](https://github.com/langchain-ai/open-swe)|
|**GitHub星星 **|![GitHub stars](https://img.shields.io/github/stars/langchain-ai/open-swe?style=social)|
|** 上次承诺 **|![GitHub last commit](https://img.shields.io/github/last-commit/langchain-ai/open-swe)|

</details>

<div align="center">

<a name="h2c509530"></a>
### 🟩开发工具🛠

</div>

* 用于构建、可视化和部署LangGraph应用程序的开发工具：*

<details>
<summary>代码生成<strong>LangGraph Generator</strong> -代码生成和项目搭建</summary>️

** 用于LangGraph项目的自动代码生成工具。**将YML配置初始化为工作代码，提供项目脚手架，并自动创建模板以实现快速开发。

| | |
|---|---|
|** 仓库 **|[`langgraph-gen-py`](https://github.com/langchain-ai/langgraph-gen-py)|
|**GitHub星星 **|![GitHub stars](https://img.shields.io/github/stars/langchain-ai/langgraph-gen-py?style=social)|
|** 上次承诺 **|![GitHub last commit](https://img.shields.io/github/last-commit/langchain-ai/langgraph-gen-py)|

</details>

---

<div align="center">

<a name="h093e2db6"></a>
## 跨社区项目

</div>

* 发现社区使用LangGraph生态系统构建的令人惊叹的开源项目和创新工具。这些项目展示了跨不同领域和用例的现实应用程序，展示了LangGraph和LangChain框架的多功能性和强大功能。*

> ** 想添加您的项目吗？**有关如何将LangGraph/LangChain项目提交到此集合的详细信息，请参阅我们的[Contributing Guide](CONTRIBUTING.md)。

<div align="center">

<a name="h4455e0f1"></a>
### 🧬生物与健康

</div>

* 医疗保健、医学诊断、基因组研究和科学研究代理 *

|项目|描述|GitHub星星|
|---------|-------------|--------------|
|[souvikmajumder26/Multi-Agent-Medical-Assistant](https://github.com/souvikmajumder26/Multi-Agent-Medical-Assistant)|用于医疗诊断、研究和患者交互的人工智能多代理系统，具有LLMs、RAG和人在环验证|![GitHub stars](https://img.shields.io/github/stars/souvikmajumder26/Multi-Agent-Medical-Assistant?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/souvikmajumder26/Multi-Agent-Medical-Assistant)|
|[ArcInstitute/SRAgent](https://github.com/ArcInstitute/SRAgent)|用于自动化来自科学数据库的基因组研究和RNA测序工作流程的多代理框架|![GitHub stars](https://img.shields.io/github/stars/ArcInstitute/SRAgent?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/ArcInstitute/SRAgent)|

<div align="center">

<a name="hf5300b85"></a>
### 🌐Web自动化和抓取

</div>

* 浏览器控制、Web任务自动化和数据提取 *

|项目|描述|GitHub星星|
|---|---|---|
|[esinecan/agentic-ai-browser](https://github.com/esinecan/agentic-ai-browser)|具有行为缓存、多姆保真度和成功模式记录的Web自动化代理|![GitHub stars](https://img.shields.io/github/stars/esinecan/agentic-ai-browser?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/esinecan/agentic-ai-browser)|
|[browser-use/browser-use](https://github.com/browser-use/browser-use)|供人工智能代理控制网站和自动化任务的库|![GitHub stars](https://img.shields.io/github/stars/browser-use/browser-use?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/browser-use/browser-use)|
|[stanford-mast/blast](https://github.com/stanford-mast/blast)|用于浏览器增强LLM应用程序的高性能服务引擎，具有自动扩展和OpenAI兼容API|![GitHub stars](https://img.shields.io/github/stars/stanford-mast/blast?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/stanford-mast/blast)|
|[ScrapeGraphAI/scrapecraft](https://github.com/ScrapeGraphAI/scrapecraft)|用于通过LangGraph构建抓取工作流程的可视化编辑器、批量抓取和实时流媒体|![GitHub stars](https://img.shields.io/github/stars/ScrapeGraphAI/scrapecraft?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/ScrapeGraphAI/scrapecraft)|
|[nickhawn/news-agent](https://github.com/nickhawn/news-agent)|新闻爬虫，通过Tavily和内存个性化每日摘要|![GitHub stars](https://img.shields.io/github/stars/nickhawn/news-agent?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/nickhawn/news-agent)|
|[hermesagent/langchain-hermes](https://github.com/hermesagent/langchain-hermes)|LangChain工具，该工具可以屏幕截图任何URL并返回base 64图像以进行多模式LLM分析。基本使用无需注册。|![GitHub stars](https://img.shields.io/github/stars/hermesagent/langchain-hermes?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/hermesagent/langchain-hermes)|

<div align="center">

<a name="h2bcd6e2e"></a>
### 📊商业情报和市场研究

</div>

* 业务分析、市场研究和战略情报工具 *

|项目|描述|GitHub星星|
|---|---|---|
|[oba2311/analyst_agent](https://github.com/oba2311/analyst_agent)|具有趋势/情绪分析和报告生成功能的营销分析代理|![GitHub stars](https://img.shields.io/github/stars/oba2311/analyst_agent?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/oba2311/analyst_agent)|

<div align="center">

<a name="h39c9e35b"></a>
### 🖥聊天界面& GUI

</div>

* AI代理的前端应用程序、聊天界面和图形用户界面 *

|项目|描述|GitHub星星|
|---|---|---|
|[GaiZhenbiao/ChuanhuChatGPT](https://github.com/GaiZhenbiao/ChuanhuChatGPT)|ChatGPT/LLMs的图形用户界面，具有代理支持、网络搜索和知识库功能|![GitHub stars](https://img.shields.io/github/stars/GaiZhenbiao/ChuanhuChatGPT?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/GaiZhenbiao/ChuanhuChatGPT)|
|[CopilotKit/open-multi-agent-canvas](https://github.com/CopilotKit/open-multi-agent-canvas)|具有旅行/研究示例和MCP服务器的多代理聊天界面|![GitHub stars](https://img.shields.io/github/stars/CopilotKit/open-multi-agent-canvas?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/CopilotKit/open-multi-agent-canvas)|
|[teddynote-lab/LangConnect-Client](https://github.com/teddynote-lab/LangConnect-Client)|具有文档管理、语义/混合搜索和MCP集成的Streamlit RAG客户端|![GitHub stars](https://img.shields.io/github/stars/teddynote-lab/LangConnect-Client?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/teddynote-lab/LangConnect-Client)|

<div align="center">

<a name="ha841fa3f"></a>
### ☁ Cloud & DevOps

</div>

* 云基础设施管理、部署自动化和云资源管理 *

|项目|描述|GitHub星星|
|---------|-------------|--------------|
|[eosho/ARMA](https://github.com/eosho/ARMA)|Azure资源管理助理，具有多代理架构，用于资源配置和ARM模板验证|![GitHub stars](https://img.shields.io/github/stars/eosho/ARMA?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/eosho/ARMA)|

<div align="center">

<a name="hae02d35e"></a>
### 编码/开发代理

</div>

* 专门为软件开发、代码生成和编程协助而设计的人工智能代理 *

|项目|描述|GitHub星星|
|---------|-------------|--------------|
|[KodyKendall/LlamaBot](https://github.com/KodyKendall/LlamaBot)|Web开发编码代理，用于创建HTML/CSS/JavaScript项目和业务着陆页|![GitHub stars](https://img.shields.io/github/stars/KodyKendall/LlamaBot?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/KodyKendall/LlamaBot)|
|[AbhinavTheDev/coding-agent](https://github.com/AbhinavTheDev/coding-agent)|使用LangGraph代理通过自然语言辅助编码工作流程的开发工具|![GitHub stars](https://img.shields.io/github/stars/AbhinavTheDev/coding-agent?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/AbhinavTheDev/coding-agent)|
|[langtalks/swe-agent](https://github.com/langtalks/swe-agent)|软件工程多代理系统，具有研究人员和开发人员代理，用于自动化代码实施|![GitHub stars](https://img.shields.io/github/stars/langtalks/swe-agent?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/langtalks/swe-agent)|

<div align="center">

<a name="customer-ops"></a>
### 🛎Customer Ops

</div>

* 客户支持、CRM系统、服务管理和客户交互自动化 *

|项目|描述|GitHub星星|
|---|---|---|
|[kargarisaac/telegram_link_summarizer_agent](https://github.com/kargarisaac/telegram_link_summarizer_agent)|Telegram机器人使用LangGraph和多工具提取总结共享链接|![GitHub stars](https://img.shields.io/github/stars/kargarisaac/telegram_link_summarizer_agent?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/kargarisaac/telegram_link_summarizer_agent)|
|[raminmohammadi/ai-agent-smart-assist](https://github.com/raminmohammadi/ai-agent-smart-assist)|知识库+分类+支持团队问答（FAISS + RAG）|![GitHub stars](https://img.shields.io/github/stars/raminmohammadi/ai-agent-smart-assist?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/raminmohammadi/ai-agent-smart-assist)|

<div align="center">

<a name="h0097a9cf"></a>
### 数据平台

</div>

* 数据分析、可视化、商业智能和数据处理代理 *

|项目|描述|GitHub星星|
|---|---|---|
|[starpig1129/AI-Data-Analysis-MultiAgent](https://github.com/starpig1129/AI-Data-Analysis-MultiAgent)|具有可视化和报告生成的多代理数据分析|![GitHub stars](https://img.shields.io/github/stars/starpig1129/AI-Data-Analysis-MultiAgent?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/starpig1129/AI-Data-Analysis-MultiAgent)|
|[project-ryoma/ryoma](https://github.com/project-ryoma/ryoma)|用于分析、工程和可视化的数据代理框架，与LangChain集成|![GitHub stars](https://img.shields.io/github/stars/project-ryoma/ryoma?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/project-ryoma/ryoma)|
|[bididi-badidi/FYP-Data-Analysis-With-LLM](https://github.com/bididi-badidi/FYP-Data-Analysis-With-LLM)|使用LangGraph代理的自动化数据分析工作流程-通过LLMs进行数据集探索、统计分析和洞察生成的端到端管道|![GitHub stars](https://img.shields.io/github/stars/bididi-badidi/FYP-Data-Analysis-With-LLM?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/bididi-badidi/FYP-Data-Analysis-With-LLM)|

<div align="center">

<a name="h098da08f"></a>
### 数据科学

</div>

* 机器学习、统计分析和数据科学工作流程自动化 *

|项目|描述|GitHub星星|
|---------|-------------|--------------|
|[business-science/ai-data-science-team](https://github.com/business-science/ai-data-science-team)|人工智能驱动的数据科学团队，执行常见任务|![GitHub stars](https://img.shields.io/github/stars/business-science/ai-data-science-team?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/business-science/ai-data-science-team)|
|[leockl/sklearn-diagnose](https://github.com/leockl/sklearn-diagnose)|用于分析和调试scikit-learn机器学习模型的人工智能诊断工具|![GitHub stars](https://img.shields.io/github/stars/leockl/sklearn-diagnose?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/leockl/sklearn-diagnose)|
|[RichardKaranuMbuti/ScienceBridge](https://github.com/RichardKaranuMbuti/ScienceBridge)|科学研究加速器，分析数据集、生成假设并通过代码验证它们|![GitHub stars](https://img.shields.io/github/stars/RichardKaranuMbuti/ScienceBridge?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/RichardKaranuMbuti/ScienceBridge)|

<div align="center">

<a name="developer-tools"></a>
### 🛠Developer Tools

</div>

* 开发框架、工具包和开发基础设施 *

|项目|描述|GitHub星星|
|---|---|---|
|[akamai/patchdiff-ai](https://github.com/akamai/patchdiff-ai)|人工智能驱动的补丁差异分析工具，用于自动代码更改审查和安全分析|![GitHub stars](https://img.shields.io/github/stars/akamai/patchdiff-ai?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/akamai/patchdiff-ai)|
|[sanjeed5/ai-conversation-simulator](https://github.com/sanjeed5/ai-conversation-simulator)|与测试助理的模拟对话; LangSmith集成|![GitHub stars](https://img.shields.io/github/stars/sanjeed5/ai-conversation-simulator?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/sanjeed5/ai-conversation-simulator)|
|[DiTo97/deepagents-backends](https://github.com/DiTo97/deepagents-backends)|用于部署和管理Deep Agents应用程序的后台服务和基础设施|![GitHub stars](https://img.shields.io/github/stars/DiTo97/deepagents-backends?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/DiTo97/deepagents-backends)|
|[emanueleielo/compact-middleware](https://github.com/emanueleielo/compact-middleware)|Claude Code的压缩引擎作为插入式DeepAgents中间件|![GitHub stars](https://img.shields.io/github/stars/emanueleielo/compact-middleware?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/emanueleielo/compact-middleware)|
|[JoshuaC215/agent-service-toolkit](https://github.com/JoshuaC215/agent-service-toolkit)|使用FastAPI和Streamlit部署代理的工具包|![GitHub stars](https://img.shields.io/github/stars/JoshuaC215/agent-service-toolkit?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/JoshuaC215/agent-service-toolkit)|
|[HyperbolicLabs/Hyperbolic-AgentKit](https://github.com/HyperbolicLabs/Hyperbolic-AgentKit)|具有区块链/计算功能的代理套件|![GitHub stars](https://img.shields.io/github/stars/HyperbolicLabs/Hyperbolic-AgentKit?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/HyperbolicLabs/Hyperbolic-AgentKit)|
|[googleapis/genai-toolbox](https://github.com/googleapis/genai-toolbox)|代理ParticDB连接的基础设施（安全性、可观察性、池化）|![GitHub stars](https://img.shields.io/github/stars/googleapis/genai-toolbox?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/googleapis/genai-toolbox)|
|[Darwin-lfl/langmanus](https://github.com/Darwin-lfl/langmanus)|具有网络搜索、爬行、Python执行的自动化框架|![GitHub stars](https://img.shields.io/github/stars/Darwin-lfl/langmanus?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/Darwin-lfl/langmanus)|
|[hinthornw/trustcall](https://github.com/hinthornw/trustcall)|顽强的工具调用LangGraph|![GitHub stars](https://img.shields.io/github/stars/hinthornw/trustcall?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/hinthornw/trustcall)|
|[langasync/langasync](https://github.com/langasync/langasync)|LangChain的同步实用程序和扩展，支持高性能的Expressc工作流程|![GitHub stars](https://img.shields.io/github/stars/langasync/langasync?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/langasync/langasync)|
|[andrestorres123/delve](https://github.com/andrestorres123/delve)|非结构化数据的分类生成器|![GitHub stars](https://img.shields.io/github/stars/andrestorres123/delve?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/andrestorres123/delve)|
|[Bessouat40/RAGLight](https://github.com/Bessouat40/RAGLight)|适用于多个供应商的模块化/并行库|![GitHub stars](https://img.shields.io/github/stars/Bessouat40/RAGLight?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/Bessouat40/RAGLight)|
|[teddynote-lab/langgraph-mcp-agents](https://github.com/teddynote-lab/langgraph-mcp-agents)|MCP适用于LangGraph代理的集成工具包|![GitHub stars](https://img.shields.io/github/stars/teddynote-lab/langgraph-mcp-agents?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/teddynote-lab/langgraph-mcp-agents)|
|[cryxnet/deepmcpagent](https://github.com/cryxnet/deepmcpagent)|MCP-通过HTTP/SSE的第一个代理框架（LangChain/LangGraph）|![GitHub stars](https://img.shields.io/github/stars/cryxnet/deepmcpagent?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/cryxnet/deepmcpagent)|
|[cubaseuser123/Cellwise-LanGraph-NoteBook-Agent](https://github.com/cubaseuser123/Cellwise-LanGraph-NoteBook-Agent)|LangGraph代理，通过IPython挂钩在单元格执行时实时自动记录Jupyter笔记本|![GitHub stars](https://img.shields.io/github/stars/cubaseuser123/Cellwise-LanGraph-NoteBook-Agent?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/cubaseuser123/Cellwise-LanGraph-NoteBook-Agent)|
|[Azzedde/brainstormers](https://github.com/Azzedde/brainstormers)|精心策划的结构性头脑风暴链|![GitHub stars](https://img.shields.io/github/stars/Azzedde/brainstormers?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/Azzedde/brainstormers)|
|[rsrini7/mermaid2gif](https://github.com/rsrini7/mermaid2gif)|用于将Mermaid图表转换为动画GIF的工具，并可选择人工智能驱动的图表生成|![GitHub stars](https://img.shields.io/github/stars/rsrini7/mermaid2gif?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/rsrini7/mermaid2gif)|
|[zamalali/langchain-code](https://github.com/zamalali/langchain-code)|Multi-LLM CLI工具，具有ReAct & Deep模式，用于代码分析、功能实现和错误修复|![GitHub stars](https://img.shields.io/github/stars/zamalali/langchain-code?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/zamalali/langchain-code)|
|[Mediaeater/swarm.at](https://github.com/Mediaeater/swarm-at-ledger)|结算协议将每个LangGraph节点执行哈希链到具有信任分层代理身份的不可变审计分类帐中|![GitHub stars](https://img.shields.io/github/stars/Mediaeater/swarm.at?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/Mediaeater/swarm.at)|
|[eosho/langchain_terminal_agent](https://github.com/eosho/langchain_terminal_agent)|使用LangChain构建的安全、人性化的终端助理，在人类审查和监督下执行shell命令|![GitHub stars](https://img.shields.io/github/stars/eosho/langchain_terminal_agent?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/eosho/langchain_terminal_agent)|
|[davialabs/davia](https://github.com/davialabs/davia)|专为编码代理而设计的交互式、可编辑文档平台-将代理输出转化为实时、可查询的知识库|![GitHub stars](https://img.shields.io/github/stars/davialabs/davia?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/davialabs/davia)|
|[proactive-agent/langgraphics](https://github.com/proactive-agent/langgraphics)|实时LangGraph执行可视化工具-通过LangSmith/Langfuse跟踪集成逐节点动画实时代理图穿越|![GitHub stars](https://img.shields.io/github/stars/proactive-agent/langgraphics?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/proactive-agent/langgraphics)|
|[dkondo/agent-tackle-box](https://github.com/dkondo/agent-tackle-box)|LangGraph & LangChain代理的终端调试器-使用文本TUI和Python程序步进检查状态、工具调用和语义断点|![GitHub stars](https://img.shields.io/github/stars/dkondo/agent-tackle-box?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/dkondo/agent-tackle-box)|
|[YaVendio/olive](https://github.com/YaVendio/olive)|将普通Python功能转换为AI代理可访问的远程工具，简化LangGraph和其他代理框架的工具服务器创建|![GitHub stars](https://img.shields.io/github/stars/YaVendio/olive?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/YaVendio/olive)|
|[sardanaaman/langgraph-compass](https://github.com/sardanaaman/langgraph-compass)|用于对话LangGraph代理的智能后续问题生成模块-提高对话连续性和用户意图解析|![GitHub stars](https://img.shields.io/github/stars/sardanaaman/langgraph-compass?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/sardanaaman/langgraph-compass)|
|[Sean-V-Dev/HMLR-Agentic-AI-Memory-System](https://github.com/Sean-V-Dev/HMLR-Agentic-AI-Memory-System)|人工智能代理的持久活记忆层-跨会话存储和检索上下文，以支持长期运行的代理工作流程|![GitHub stars](https://img.shields.io/github/stars/Sean-V-Dev/HMLR-Agentic-AI-Memory-System?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/Sean-V-Dev/HMLR-Agentic-AI-Memory-System)|
|[chopratejas/headroom](https://github.com/chopratejas/headroom)|用于LLM应用程序的上下文优化代理层-压缩令牌使用、管理上下文窗口，并为LangChain、MCP和FastAPI堆栈提供OpenAI兼容的API|![GitHub stars](https://img.shields.io/github/stars/chopratejas/headroom?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/chopratejas/headroom)|
|[tb8412/qae-langgraph-example](https://github.com/tb8412/qae-langgraph-example)|具有可审计证书和基于约束的路由的LangGraph代理的确定性执行前安全认证|![GitHub stars](https://img.shields.io/github/stars/tb8412/qae-langgraph-example?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/tb8412/qae-langgraph-example)|

<div align="center">

<a name="he75969b5"></a>
### 收件箱

</div>

* 用于扩展LangGraph工作流程的可安装包和库 *

|包|描述|注册表|
|---|---|---|
|[MOSS LangGraph](https://pypi.org/project/moss-langgraph/)|LangGraph工作流程的加密签名。将具有ML-DSA-44量子后签名的防篡改审计跟踪添加到节点输出和状态转换。|[![PyPI](https://img.shields.io/pypi/v/moss-langgraph)]（https://pypi.org/project/moss-langgraph/）|
|[langchain-colony](https://pypi.org/project/langchain-colony/)|LangChain The Colony的集成-人工智能代理互联网。为代理提供LangChain-原生工具，供代理在社交平台上与780多个AI代理发布、评论、投票、发送消息和互动。|[![PyPI](https://img.shields.io/pypi/v/langchain-colony)]（https://pypi.org/project/langchain-colony/）|

<div align="center">

<a name="hb4f9fdd1"></a>
### 金融与金融科技

</div>

* 财务分析、交易、银行、投资研究和商业智能 *

|项目|描述|GitHub星星|
|---|---|---|
|[virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund)|带LangChain的多代理交易系统|![GitHub stars](https://img.shields.io/github/stars/virattt/ai-hedge-fund?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/virattt/ai-hedge-fund)|
|[sagar-n/deepagents](https://github.com/sagar-n/deepagents)|具有专业分析代理的股票研究助理|![GitHub stars](https://img.shields.io/github/stars/sagar-n/deepagents?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/sagar-n/deepagents)|
|[AKMessi/AI-IPO-Analyst](https://github.com/AKMessi/AI-IPO-Analyst)|具有PDF解析和市场数据丰富功能的IPO分析代理|![GitHub stars](https://img.shields.io/github/stars/AKMessi/AI-IPO-Analyst?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/AKMessi/AI-IPO-Analyst)|
|[johnsonhk88/AI-Bank-Statement-Document-Automation-By-LLM-And-Personal-Finanical-Analysis-Prediction](https://github.com/johnsonhk88/AI-Bank-Statement-Document-Automation-By-LLM-And-Personal-Finanical-Analysis-Prediction)|银行对账单解析+具有多代理工作流程的个人财务分析|![GitHub stars](https://img.shields.io/github/stars/johnsonhk88/AI-Bank-Statement-Document-Automation-By-LLM-And-Personal-Finanical-Analysis-Prediction?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/johnsonhk88/AI-Bank-Statement-Document-Automation-By-LLM-And-Personal-Finanical-Analysis-Prediction)|
|[OzorOwn/defi-mcp](https://github.com/OzorOwn/defi-mcp)|DeFi MCP服务器，带有12个工具：实时加密价格，多链钱包余额（9链），通过Jupiter和Li.Fi的DEX报价，以及275+资产的令牌搜索|![GitHub stars](https://img.shields.io/github/stars/OzorOwn/defi-mcp?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/OzorOwn/defi-mcp)|
|[AKMessi/dealscout](https://github.com/AKMessi/dealscout)|VC尽职调查AI代理与辩论子代理-产品分析师和市场分析师在达成联合投资结论之前争论对立的观点|![GitHub stars](https://img.shields.io/github/stars/AKMessi/dealscout?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/AKMessi/dealscout)|

<div align="center">

<a name="h916801e9"></a>
### 🎯营销

</div>

营销分析、内容策略和促销自动化

目前没有活跃的社区列表。

<a name="hbd6acfdb"></a>
### 🎥媒体和播客

* 内容创建、媒体处理、播客、多媒体生成和语音处理 *

|项目|描述|GitHub星星|
|---|---|---|
|[souzatharsis/podcastfy](https://github.com/souzatharsis/podcastfy)|将多模态内容转换为播客风格的对话|![GitHub stars](https://img.shields.io/github/stars/souzatharsis/podcastfy?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/souzatharsis/podcastfy)|
|[wassim249/YT-Navigator](https://github.com/wassim249/YT-Navigator)|在YouTube频道内容中导航和搜索|![GitHub stars](https://img.shields.io/github/stars/wassim249/YT-Navigator?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/wassim249/YT-Navigator)|
|[benjichat/voice_agent_base](https://github.com/benjichat/voice_agent_base)|在React UI中具有STT/DTS和网络搜索的语音代理|![GitHub stars](https://img.shields.io/github/stars/benjichat/voice_agent_base?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/benjichat/voice_agent_base)|
|[von-development/voice-file-agent](https://github.com/von-development/voice-file-agent)|带LangGraph ReAct的语音控制文件管理器|![GitHub stars](https://img.shields.io/github/stars/von-development/voice-file-agent?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/von-development/voice-file-agent)|

<div align="center">

<a name="h6e7750c1"></a>
### 🤖机器人技术和人工智能

</div>

* 机器人应用、体现人工智能和物理世界互动 *

|项目|描述|GitHub星星|
|---------|-------------|--------------|
|[RobotecAI/rai](https://github.com/RobotecAI/rai)|灵活的多智能体框架，用于在机器人中开发和部署指定的人工智能功能，并支持多模式交互|![GitHub stars](https://img.shields.io/github/stars/RobotecAI/rai?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/RobotecAI/rai)|

<div align="center">

<a name="h1f29bfb6"></a>
### RAG &文档处理

</div>

* 检索增强生成、文档聊天机器人和知识库系统 *

|项目|描述|GitHub星星|
|---|---|---|
|[GiovanniPasq/agentic-rag-for-dummies](https://github.com/GiovanniPasq/agentic-rag-for-dummies)|使用LangGraph -在几分钟内学习检索增强生成代理构建的模块化学习程序RAG|![GitHub stars](https://img.shields.io/github/stars/GiovanniPasq/agentic-rag-for-dummies?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/GiovanniPasq/agentic-rag-for-dummies)|
|[Goodnight77/Just-RAG](https://github.com/Goodnight77/Just-RAG)|统计RAG与LangGraph + Qdrant|![GitHub stars](https://img.shields.io/github/stars/Goodnight77/Just-RAG?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/Goodnight77/Just-RAG)|
|[IlyaRice/RAG-Challenge-2](https://github.com/IlyaRice/RAG-Challenge-2)|RAG具有自定义PDF解析、父检索和重新排序功能|![GitHub stars](https://img.shields.io/github/stars/IlyaRice/RAG-Challenge-2?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/IlyaRice/RAG-Challenge-2)|
|[LexStack-AI/LexReviewer](https://github.com/LexStack-AI/LexReviewer)|LangGraph-支持的法律PDF RAG服务，具有混合载体+BM25检索、流媒体聊天和具有边界框引用的引用感知答案以供突出显示。|![GitHub stars](https://img.shields.io/github/stars/LexStack-AI/LexReviewer?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/LexStack-AI/LexReviewer)|
|[TAMustafa/Local_Chat_RAG](https://github.com/TAMustafa/Local_Chat_RAG)|本地RAG聊天（Ollama），具有源代码和现代UI|![GitHub stars](https://img.shields.io/github/stars/TAMustafa/Local_Chat_RAG?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/TAMustafa/Local_Chat_RAG)|
|[bRAGAI/bRAG-langchain](https://github.com/bRAGAI/bRAG-langchain)|RAG的收件箱系列从基础到高级|![GitHub stars](https://img.shields.io/github/stars/bRAGAI/bRAG-langchain?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/bRAGAI/bRAG-langchain)|
|[catio-tech/graphqa](https://github.com/catio-tech/graphqa)|用于在没有复杂查询语言的情况下查询图形的自然语言图形分析框架|![GitHub stars](https://img.shields.io/github/stars/catio-tech/graphqa?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/catio-tech/graphqa)|
|[zamalali/DeepGit](https://github.com/zamalali/DeepGit)|通过混合检索和重新排序实现智能GitHub仓库发现的抽象工作流程|![GitHub stars](https://img.shields.io/github/stars/zamalali/DeepGit?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/zamalali/DeepGit)|

<div align="center">

<a name="h4ce1b6ec"></a>
### 研究代理

</div>

* 人工智能研究助理、学术工具和自动化研究工作流程 *

|项目|描述|GitHub星星|
|---|---|---|
|[bytedance/deer-flow](https://github.com/bytedance/deer-flow)|具有搜索/抓取/Python工具的深度研究框架|![GitHub stars](https://img.shields.io/github/stars/bytedance/deer-flow?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/bytedance/deer-flow)|
|[duartecaldascardoso/article-explainer](https://github.com/duartecaldascardoso/article-explainer)|用于理解具有人工智能解释和Swarm架构的研究文章的多代理系统|![GitHub stars](https://img.shields.io/github/stars/duartecaldascardoso/article-explainer?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/duartecaldascardoso/article-explainer)|
|[MODSetter/SurfSense](https://github.com/MODSetter/SurfSense)|整合个人知识产权和外部资源的研究代理|![GitHub stars](https://img.shields.io/github/stars/MODSetter/SurfSense?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/MODSetter/SurfSense)|
|[Intelligent-Internet/ii-researcher](https://github.com/Intelligent-Internet/ii-researcher)|带有BAML、多提供商抓取、可扩展流的深度搜索代理|![GitHub stars](https://img.shields.io/github/stars/Intelligent-Internet/ii-researcher?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/Intelligent-Internet/ii-researcher)|
|[pogjester/company-research-agent](https://github.com/pogjester/company-research-agent)|具有流媒体和过滤的公司研究管道|![GitHub stars](https://img.shields.io/github/stars/pogjester/company-research-agent?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/pogjester/company-research-agent)|
|[jolovicdev/shandu](https://github.com/jolovicdev/shandu)|来源评估和知识综合|![GitHub stars](https://img.shields.io/github/stars/jolovicdev/shandu?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/jolovicdev/shandu)|
|[LearningCircuit/local-deep-research](https://github.com/LearningCircuit/local-deep-research)|通过多个LLMs和网络搜索进行本地深度研究|![GitHub stars](https://img.shields.io/github/stars/LearningCircuit/local-deep-research?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/LearningCircuit/local-deep-research)|
|[assafelovic/gpt-researcher](https://github.com/assafelovic/gpt-researcher)|具有引用的报告导向研究代理|![GitHub stars](https://img.shields.io/github/stars/assafelovic/gpt-researcher?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/assafelovic/gpt-researcher)|
|[Just-Curieous/Curie](https://github.com/Just-Curieous/Curie)|ML/系统中经验实验代理|![GitHub stars](https://img.shields.io/github/stars/Just-Curieous/Curie?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/Just-Curieous/Curie)|
|[iblameandrew/local-deepsearch-academic](https://github.com/iblameandrew/local-deepsearch-academic)|使用S2 + RAPTOR索引发现学术论文|![GitHub stars](https://img.shields.io/github/stars/iblameandrew/local-deepsearch-academic?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/iblameandrew/local-deepsearch-academic)|
|[bernatsampera/event-deep-research](https://github.com/bernatsampera/event-deep-research)|从历史人物中提取结构化时间轴事件的多主体传记研究系统|![GitHub stars](https://img.shields.io/github/stars/bernatsampera/event-deep-research?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/bernatsampera/event-deep-research)|
|[microsoft/RD-Agent](https://github.com/microsoft/RD-Agent)|数据挖掘、论文分析、模型调整的研发自动化|![GitHub stars](https://img.shields.io/github/stars/microsoft/RD-Agent?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/microsoft/RD-Agent)|
|[SalesforceAIResearch/enterprise-deep-research](https://github.com/SalesforceAIResearch/enterprise-deep-research)|具有规划者、专业搜索代理和LangGraph上的Web UI的可控企业研究堆栈|![GitHub stars](https://img.shields.io/github/stars/SalesforceAIResearch/enterprise-deep-research?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/SalesforceAIResearch/enterprise-deep-research)|
|[lgesuellip/researcher_agent](https://github.com/lgesuellip/researcher_agent)|通过自动文档索引将网站转变为LLM准备好的研究内容|![GitHub stars](https://img.shields.io/github/stars/lgesuellip/researcher_agent?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/lgesuellip/researcher_agent)|
|[guy-hartstein/company-research-agent](https://github.com/guy-hartstein/company-research-agent)|由LangGraph和Tavily支持的大型公司尽职调查工具;具有Gemini/GPT的多代理框架，用于深入的公司研究和财务分析|![GitHub stars](https://img.shields.io/github/stars/guy-hartstein/company-research-agent?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/guy-hartstein/company-research-agent)|
|[OpenDCAI/Paper2Any](https://github.com/OpenDCAI/Paper2Any)|使用LangGraph代理将论文、文本或主题复制为可编辑的研究图表、技术路线图和演示幻灯片|![GitHub stars](https://img.shields.io/github/stars/OpenDCAI/Paper2Any?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/OpenDCAI/Paper2Any)|

<div align="center">

<a name="cybersecurity"></a>
### 🛠Cybersecurity

</div>

* 安全测试、红队自动化、对手模拟和防御验证代理 *

|项目|描述|GitHub星星|
|---|---|---|
|[PurpleAILAB/Decepticon](https://github.com/PurpleAILAB/Decepticon)|使用LangGraph编排、沙箱Kali工具、OPPLAN/RoE工作流程和攻击图存储器进行授权参与的自主红队代理。|![GitHub stars](https://img.shields.io/github/stars/PurpleAILAB/Decepticon?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/PurpleAILAB/Decepticon)|

<div align="center">

<a name="h8537577b"></a>
### 🌍安全与治理

</div>

* 行动验证、出处跟踪、故障关闭机制、及时注射保护 *

|项目|描述|GitHub星星|
|---|---|---|
|[aporthq/aport-agent-guardrails](https://github.com/aporthq/aport-agent-guardrails)|LangChain/LangGraph代理的预行动授权护栏;在执行之前检查工具调用是否符合OAP策略。|![GitHub stars](https://img.shields.io/github/stars/aporthq/aport-agent-guardrails?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/aporthq/aport-agent-guardrails)|
|[LembaGang/headless-oracle-v5](https://github.com/LembaGang/headless-oracle-v5)|故障关闭市场状态MCP。暂停有状态LangGraph代理在封闭市场或夏令时转换期间进入再试循环。|![GitHub stars](https://img.shields.io/github/stars/LembaGang/headless-oracle-v5?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/LembaGang/headless-oracle-v5)|
|[pic-standard](https://github.com/madeinplutofabio/pic-standard)|本地优先协议，用于代理操作之前的出处和意图验证（故障关闭、可验证的证据）。|![GitHub stars](https://img.shields.io/github/stars/madeinplutofabio/pic-standard?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/madeinplutofabio/pic-standard)|
|[sidclawhq/platform](https://github.com/sidclawhq/platform)|LangGraph代理人的批准和审计层。拦截工具调用，根据策略对其进行评估，并在执行之前将其保留以供人工审查。哈希链审计跟踪，13个框架集成。阿帕奇2.0。|![GitHub stars](https://img.shields.io/github/stars/sidclawhq/platform?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/sidclawhq/platform)|

<div align="center">

<a name="h5e2872ce"></a>
### 可持续发展

</div>

环境影响、绿色技术和可持续发展分析

目前没有活跃的社区列表。

<div align="center">

<a name="h66ddf81d"></a>
### 收件箱模板和启动器

</div>

* 用于构建LangGraph应用程序的即用型项目模板、样板和入门套件 *

|项目|描述|GitHub星星|
|---|---|---|
|[emanueleielo/deepagents-open-lovable](https://github.com/emanueleielo/deepagents-open-lovable)|开源Deep Agents实施与Lovable平台集成，以实现复杂的规划和执行工作流程|![GitHub stars](https://img.shields.io/github/stars/emanueleielo/deepagents-open-lovable?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/emanueleielo/deepagents-open-lovable)|
|[wassim249/fastapi-langgraph-agent-production-ready-template](https://github.com/wassim249/fastapi-langgraph-agent-production-ready-template)|FastAPI LangGraph代理的模板（日志记录、持久性、安全性）|![GitHub stars](https://img.shields.io/github/stars/wassim249/fastapi-langgraph-agent-production-ready-template?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/wassim249/fastapi-langgraph-agent-production-ready-template)|
|[gtesei/agentic_design_patterns](https://github.com/gtesei/agentic_design_patterns)|全面的、动手的设计模式集合，用于使用LangChain和LangGraph构建稳健的代理AI系统|![GitHub stars](https://img.shields.io/github/stars/gtesei/agentic_design_patterns?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/gtesei/agentic_design_patterns)|
|[NicholasGoh/fastapi-mcp-langgraph-template](https://github.com/NicholasGoh/fastapi-mcp-langgraph-template)|FastAPI模板与LangGraph + MCP和流式用户体验|![GitHub stars](https://img.shields.io/github/stars/NicholasGoh/fastapi-mcp-langgraph-template?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/NicholasGoh/fastapi-mcp-langgraph-template)|
|[lgesuellip/langgraph-whatsapp-agent](https://github.com/lgesuellip/langgraph-whatsapp-agent)|具有LangGraph和MCP的WhatsApp代理模板|![GitHub stars](https://img.shields.io/github/stars/lgesuellip/langgraph-whatsapp-agent?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/lgesuellip/langgraph-whatsapp-agent)|
|[ac12644/langgraph-starter-kit](https://github.com/ac12644/langgraph-starter-kit)|生产就绪的多代理初学者工具包，包含6种模式（Supervisor、Swarm、HITL、Structured Output、Research、RAG）、5个LLM提供程序、MCP集成、CLI脚手架和Fastify服务器|![GitHub stars](https://img.shields.io/github/stars/ac12644/langgraph-starter-kit?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/ac12644/langgraph-starter-kit)|

<div align="center">

<a name="h025ff342"></a>
### 🏢工作场所和生产力

</div>

* 办公自动化、生产力工具和工作场所管理 *

|项目|描述|GitHub星星|
|---|---|---|
|[ashumishra2104/AI_Travel_agent_Streamlit](https://github.com/ashumishra2104/AI_Travel_agent_Streamlit)|Streamlit基于人工智能旅行社，具有天气、搜索、货币转换和YouTube集成工具|![GitHub stars](https://img.shields.io/github/stars/ashumishra2104/AI_Travel_agent_Streamlit?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/ashumishra2104/AI_Travel_agent_Streamlit)|
|[eduly-ai/eduly](https://github.com/eduly-ai/eduly)|人工智能驱动的教育平台，提供个性化学习体验和辅导协助|![GitHub stars](https://img.shields.io/github/stars/eduly-ai/eduly?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/eduly-ai/eduly)|
|[emanueleielo/ciana-parrot](https://github.com/emanueleielo/ciana-parrot)|自托管AI个人助理，具有Telegram集成、预定任务、多提供商LLM支持和MCP服务器集成|![GitHub stars](https://img.shields.io/github/stars/emanueleielo/ciana-parrot?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/emanueleielo/ciana-parrot)|
|[tavily-ai/meeting-prep-agent](https://github.com/tavily-ai/meeting-prep-agent)|通过日历、搜索和个人资料研究进行会议准备|![GitHub stars](https://img.shields.io/github/stars/tavily-ai/meeting-prep-agent?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/tavily-ai/meeting-prep-agent)|
|[temporal-cortex/mcp](https://github.com/temporal-cortex/mcp)|确定性日历安排MCP服务器（带LangGraph示例）-日期时间分辨率、多日历可用性和原子预订|![GitHub stars](https://img.shields.io/github/stars/temporal-cortex/mcp?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/temporal-cortex/mcp)|
|[zamalali/InboxHero](https://github.com/zamalali/InboxHero)|电子邮件分类，阅读附件和起草回复|![GitHub stars](https://img.shields.io/github/stars/zamalali/InboxHero?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/zamalali/InboxHero)|
|[khoj-ai/khoj](https://github.com/khoj-ai/khoj)|自托管文档和网络的第二大脑|![GitHub stars](https://img.shields.io/github/stars/khoj-ai/khoj?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/khoj-ai/khoj)|
|[raj-maharajwala/AI_Agent_Chatbot_Synapse](https://github.com/raj-maharajwala/AI_Agent_Chatbot_Synapse)|搜索/生产力/数据代理与UI捆绑|![GitHub stars](https://img.shields.io/github/stars/raj-maharajwala/AI_Agent_Chatbot_Synapse?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/raj-maharajwala/AI_Agent_Chatbot_Synapse)|
|[pipeshub-ai/pipeshub-ai](https://github.com/pipeshub-ai/pipeshub-ai)|可完全扩展的工作场所人工智能平台，用于企业搜索和工作流程自动化;将Gmail、Slack、Notion、Google Drive与LangGraph-动力代理和知识图谱RAG连接起来|![GitHub stars](https://img.shields.io/github/stars/pipeshub-ai/pipeshub-ai?style=social)<br>![Last commit](https://img.shields.io/github/last-commit/pipeshub-ai/pipeshub-ai)|

---

<div align="center">

<a name="h7356fd4c"></a>
### 学习资源

</div>

<a name="h8281dc78"></a>
### 官方- LangChain学院

<details>
<summary><strong>基础课程</strong></summary>

|名称|描述|
|---|---|
|[Monitoring Production Agents](https://academy.langchain.com/collections/foundation)|了解如何监控和改进生产中的代理、跟踪成本、分析痕迹以及随着时间的推移观察质量和延迟。|
|[Building Reliable Agents](https://academy.langchain.com/collections/foundation)|通过LangSmith的迭代改进周期，将代理从第一次运行到生产就绪系统。|
|[Introduction to LangChain - Python](https://academy.langchain.com/collections/foundation)|了解如何使用LangChain使用预构建的架构和模型集成构建人工智能代理，然后使用LangSmith Observability调试它们。|
|[Introduction to Agent Observability & Evaluations](https://academy.langchain.com/courses/intro-to-langsmith)|通过LangSmith了解代理可观察性和评估的要点。|
|[Introduction to LangGraph - Python](https://academy.langchain.com/courses/intro-to-langgraph)|了解LangGraph的基础知识，以更精确和更控制地构建代理和多代理应用程序。|

</details>

<details>
<summary><strong>项目课程</strong></summary>

|名称|描述|
|---|---|
|[Deep Agents](https://academy.langchain.com/courses/deep-agents-with-langgraph)|了解Deep Agents的基本特征并为复杂、长时间运行的任务实施您自己的深度代理。|
|[Ambient Agents with LangGraph](https://academy.langchain.com/courses/ambient-agents/)|使用LangGraph构建环境电子邮件代理并使用LangSmith对其进行评估。|
|[Deep Research with LangGraph](https://academy.langchain.com/courses/deep-research-with-langgraph)|使用LangGraph构建深度研究代理，并使用LangSmith评估其绩效。|

</details>

<details>
<summary><strong>快速入门课程</strong></summary>

|名称|描述|
|---|---|
|[LangSmith Agent Builder](https://academy.langchain.com/courses/quickstart-agent-builder/)|开始使用日常语言为实际工作创建无代码代理。|
|[LangSmith Essentials](https://academy.langchain.com/courses/quickstart-langsmith-essentials)|了解LangSmith的要点，通过实时生产数据进行持续测试和改进。|
|[LangGraph Essentials - TypeScript](https://academy.langchain.com/courses/quickstart-langgraph-essentials-typescript)|通过构建电子邮件工作流程，了解TypeScript中的LangGraph要点。|
|[LangGraph Essentials - Python](https://academy.langchain.com/courses/langgraph-essentials-python)|通过构建电子邮件工作流程了解Python中的LangGraph要点。|
|[LangChain Essentials - TypeScript](https://academy.langchain.com/courses/quickstart-langchain-essentials-typescript)|了解TypeScript中LangChain的核心元素，包括“Create_Agent”、工具、MCP、流媒体和结构化输出。|
|[LangChain Essentials - Python](https://academy.langchain.com/courses/langchain-essentials-python)|了解Python中LangChain的核心元素，包括“Create_Agent”、工具、MCP、流媒体和结构化输出。|

</details>

<a name="h386b02ff"></a>
### 社区课程
- **[LangGraph — Develop LLM-Powered AI Agents (Udemy)](https://www.udemy.com/course/langgraph/)** -实用LangGraph代理模式。讲师：[emarco177](https://github.com/emarco177)。

<a name="h74163a37"></a>
### 📖额外资源

* 一份简短的教程、研讨会、博客和案例研究列表，您可以随着时间的推移不断增长。*

<details>
<summary><strong>课程</strong></summary>

|名称|描述|
|---|---|
|[Ava WhatsApp Agent Course](https://github.com/neural-maze/ava-whatsapp-agent-course)|使用LangGraph构建具有语音处理、图像生成和长期记忆的WhatsApp代理。|

</details>

<details>
<summary><strong>示例</strong></summary>

|名称|描述|
|---|---|
|[GenAI Agents](https://github.com/NirDiamant/GenAI_Agents)|代理实现示例和模式的集合。|
|[Generative AI](https://github.com/genieincodebottle/generative-ai)|全面的生成式人工智能资源中心，涵盖路线图，LangChain/LangGraph项目，RAG，多智能体模式，MCP和面试/编码准备。|

</details>

<details>
<summary> <strong> Tutuum </strong></summary>

|名称|描述|
|---|---|
|[RAG Techniques](https://github.com/NirDiamant/RAG_Techniques)|几个RAG实现和分步步行。|

</details>

<details>
<summary><strong>研讨会</strong>3

|名称|描述|
|---|---|
|[Grounding RAG Applications Workshop](https://github.com/carlyrichmond/webdevcon-grounding-rag-applications-workshop)|动手RAG聊天机器人+具有JavaScript和Elasticsearch的旅行规划代理。|

</details>

<details>
<summary><strong>博客</strong></summary>

|名称|描述|
|---|---|
|[LinkedIn — Practical Text-to-SQL](https://www.linkedin.com/blog/engineering/ai/practical-text-to-sql-for-data-analytics)|LinkedIn上使用文本转SQL进行搜索、发现和分析用例。|
|[Rakuten — From Hype to Real Tools](https://rakuten.today/blog/from-ai-hype-to-real-world-tools-rakuten-teams-up-with-langchain.html)|LangChain的合作伙伴详细信息和生产应用。|
|[Komodo Health — Enterprise Assistant](https://www.komodohealth.com/perspectives/new-gen-ai-assistant-empowers-the-enterprise/)|企业助理支持医疗保健领域的领域工作流程。|
|[Cisco Outshift — DevOps Agent via REST](https://outshift.cisco.com/blog/build-react-agent-application-for-devops-tasks-using-rest-apis)|使用REST APIs为DevOps任务构建React代理应用程序。|
|[Elastic — Security GenAI Features](https://www.elastic.co/blog/elastic-security-generative-ai-features)|安全工作流程的生成性人工智能功能。|

</details>

<details>
<summary><strong>谈话</strong></summary>

|名称|描述|
|---|---|
|[Uber — AI-Driven Developer Productivity](https://dpe.org/sessions/ty-smith-adam-huda/this-year-in-ubers-ai-driven-developer-productivity-revolution/)|Uber如何利用人工智能提高开发人员的生产力和代码生成。|

</details>

<details>
<summary>1 </strong></summary>

|名称|描述|
|---|---|
|[GitLab — Duo Workflow](https://handbook.gitlab.com/handbook/engineering/architecture/design-documents/duo_workflow/)|代码生成工作流程的架构文档。|

</details>

<details>
<summary><strong>案例研究</strong></summary>

|名称|描述|
|---|---|
|[Klarna — Domain Copilot](https://blog.langchain.dev/customers-klarna/)|特定领域任务的生产副驾驶。|
|[Minimal — Multi-Agent Customer Support](https://blog.langchain.dev/how-minimal-built-a-multi-agent-customer-support-system-with-langgraph-langsmith/)|根据LangGraph和LangSmith构建的客户支持系统。|
|[OpenRecovery — Clinical Copilot](https://blog.langchain.dev/customers-openrecovery/)|医疗保健运营的临床副驾驶。|
|[AppFolio — Embedded Copilots](https://blog.langchain.dev/customers-appfolio/)|房地产平台中的产品嵌入式并行驾驶仪。|
|[Infor — Product Copilots & Support](https://blog.langchain.dev/customers-infor/)|嵌入式产品体验、支持和并行驾驶员。|
|[AirTop — Browser Automation for Agents](https://blog.langchain.dev/customers-airtop/)|大型浏览器自动化平台。|
|[Athena Intelligence — Research & Summarization](https://blog.langchain.dev/customers-athena-intelligence/)|研究和总结生产中的工作流程。|
|[Captide — Agentic Equity Research](https://blog.langchain.dev/how-captide-is-redefining-equity-research-with-agentic-workflows-built-on-langgraph-and-langsmith/)|使用LangGraph + LangSmith代理工作流程进行股权研究。|

</details>

---

<div align="center">

<a name="h888af1f2"></a>
### 👥社区

</div>

|名称|类型|描述|
|---|---|---|
|[LangChain Community](https://www.langchain.com/join-community)|官方社区|是公告、讨论、活动和渠道的中央中心，以连接LangChain/LangGraph生态系统。|
|[LangChain Forum](https://forum.langchain.com/)|论坛|社区讨论论坛，用于提出问题、分享想法并与其他LangChain和LangGraph构建者联系。|

<div align="center">

---

<a name="hbb966aa6"></a>
## 🤝贡献

</div>

我们欢迎添加和修复！在打开问题或拉取请求之前，请阅读 **[Contributing Guide](CONTRIBUTING.md)** 了解提交流程、格式规则和类别指南。

---

<div align="center">

<a name="he83a256e"></a>
## 🙏确认

</div>

特别感谢[@langchain-ai](https://github.com/langchain-ai)团队构建了出色的框架和生态系统，使开发人员能够创建强大的人工智能应用程序。
