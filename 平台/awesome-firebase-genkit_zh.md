<div align="center">

<!-- title -->

<!--lint ignore no-dead-urls-->

# Awesome Genkit <!-- omit from toc -->

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re) [![lint](https://github.com/xavidop/awesome-genkit/actions/workflows/lint.yaml/badge.svg)](https://github.com/xavidop/awesome-genkit/actions/workflows/lint.yaml) [![Track Awesome List](https://www.trackawesomelist.com/badge.svg)](https://www.trackawesomelist.com/xavidop/awesome-firebase-genkit/) 

<!-- subtitle -->

A collection of awesome things regarding the Genkit ecosystem.

<p align="center">
  <a href="CODE_OF_CONDUCT.md">Code Of Conduct</a>
  <a href="CONTRIBUTING.md">Contribution guide</a>
  <a href="https://github.com/xavidop/awesome-genkit/graphs/contributors">Contributors</a>
</p>

<!-- image -->
<picture>
  <source media="(prefers-color-scheme: light)" srcset="/assets/genkit-logo.png">
  <source media="(prefers-color-scheme: dark)" srcset="/assets/genkit-logo-dark.png">
  <img alt="Shows an illustrated sun in light mode and a moon with stars in dark mode." src="/assets/genkit-logo.png">
</picture>

<!-- description -->

Genkit 是一个旨在帮助您构建人工智能驱动的应用程序和功能的框架。它提供 Node.js 和 Go 的开源库，以及用于测试和调试的开发人员工具。

</div>

<!-- TOC -->

## 内容 <!-- 省略目录 -->
- [Plugins](#plugins)
  - [JavaScript - 官方](#javascript---official)
  - [JavaScript - 社区](#javascript---community)
  - [Python - 官方](#python---official)
  - [Golang - 官方](#golang---official)
  - [Golang - 社区](#golang---community)
  - [Dart - 官方](#dart---official)
  - [Java（非官方）- 社区](#java-unofficial---community)
- [API 参考](#api-references)
- [Books](#books)
- [Solutions](#solutions)
- [Talks](#talks)
- [Videos](#videos)
- [Articles](#articles)
- [Tutorials](#tutorials)
- [Follow](#follow)

<!-- CONTENT -->

## 插件

### JavaScript - 官方

1. 模型/嵌入插件
   - [`@genkit-ai/vertexai`](https://genkit.dev/docs/plugins/vertex-ai/) - Vertex AI 插件提供了多种 AI 服务的接口：Google 生成式 AI 模型、通过 Vertex AI 快速评估 API 的评估指标子集、矢量搜索。
   - [`@genkit-ai/googleai`](https://genkit.dev/docs/plugins/google-genai/) - Google Generative AI 插件通过 Gemini API 提供与 Google Gemini 模型的接口。
   - [`genkitx-ollama`](https://genkit.dev/docs/plugins/ollama/) - Ollama 插件提供与 Ollama 支持的任何本地 LLM 的接口。
   - [`@genkit-ai/compat-oai`](https://genkit.dev/docs/plugins/compat-oai/) - 兼容 OpenAI API 的插件。
   - [`@genkit-ai/compat-oai/xai`](https://genkit.dev/docs/plugins/xai/) - XAI API 插件。
   - [`@genkit-ai/compat-oai/openai`](https://genkit.dev/docs/plugins/openai/) - OpenAI API 插件。
2.矢量商店插件
   - [`@genkit-ai/dev-local-vectorstore`](https://genkit.dev/docs/rag/) - 用于开发目的的本地矢量存储插件。
3.其他插件
   - [`@genkit-ai/firebase`](https://genkit.dev/docs/plugins/firebase/) - Firebase 插件提供了与 Firebase 服务的多种集成：使用 Cloud Firestore 矢量存储的索引器和检索器、使用 Cloud Firestore 的跟踪存储、使用 Cloud Functions 的流部署、Firebase 身份验证用户的授权策略。
   - [`@genkit-ai/express`](https://genkit.dev/docs/plugins/express/) - Express 插件为 Genkit 提供了 Express 中间件。
   - [`@genkit-ai/mcp`](https://genkit.dev/docs/plugins/mcp/) - MCP 插件提供了 MCP（模型上下文协议）的接口。

### JavaScript - 社区

1. 模型/嵌入插件
   - [`genkitx-github`](https://github.com/xavidop/genkitx-github) - GitHub 模型 API 的插件。
   - [`genkitx-anthropic`](https://github.com/BloomLabsInc/genkit-plugins/tree/main/plugins/anthropic) - Anthropic AI API 插件。
   - [`genkitx-cohere`](https://github.com/BloomLabsInc/genkit-plugins/tree/main/plugins/cohere) - Cohere API 的插件。
   - [`genkitx-groq`](https://github.com/BloomLabsInc/genkit-plugins/tree/main/plugins/groq) - Groq API 的插件。
   - [`genkitx-mistral`](https://github.com/BloomLabsInc/genkit-plugins/tree/main/plugins/mistral) - Mistral AI API 插件。
   - [`genkitx-azure-openai`](https://github.com/BloomLabsInc/genkit-plugins/tree/main/plugins/azure-openai) - Azure OpenAI API 的插件。
   - [`genkitx-aws-bedrock`](https://github.com/xavidop/genkitx-aws-bedrock) - AWS Bedrock API 的插件。
   - [`genkitx-deepseek`](https://github.com/oddbit/genkitx-deepseek) - Deepseek 云 API 插件。
   - [`genkitx-huggingface`](https://github.com/aciescrest/genkit-huggingface) - 用于拥抱人脸推理 API 的插件。
2.矢量商店插件
   - [`genkitx-convex`](https://github.com/BloomLabsInc/genkit-plugins/tree/main/plugins/convex) - 凸向量存储插件。
   - [`genkitx-hnsw`](https://github.com/BloomLabsInc/genkit-plugins/tree/main/plugins/hnsw) - HNSW 矢量商店插件。
   - [`genkitx-qdrant`](https://github.com/qdrant/qdrant-genkit) - Qdrant 矢量商店插件。
   - [`genkitx-astra-db`](https://genkit.dev/docs/plugins/astra-db/) - AstraDB 矢量存储插件。
   - [`genkitx-pgvector`](https://genkit.dev/docs/plugins/pgvector/) - PostgeSQL (PGVector) 矢量存储插件。
   - [`genkitx-redis`](https://github.com/retzd-tech/genkitx-redis) - Redis 矢量存储插件。
   - [`genkitx-voiceflow`](https://github.com/xavidop/genkitx-voiceflow) - Voiceflow KB 插件。
   - [`genkitx-lancedb`](https://genkit.dev/docs/plugins/lancedb/) - LanceDB 矢量存储插件。
   - [`genkitx-pinecone`](https://genkit.dev/docs/plugins/pinecone/) - 松果矢量商店插件。
   - [`genkitx-chromadb`](https://genkit.dev/docs/plugins/chroma/) - Chroma 矢量商店插件。
   - [`genkitx-neo4j`](https://genkit.dev/docs/plugins/neo4j/) - Neo4j 矢量存储插件。
   - [`genkitx-cloud-sql-pg`](https://genkit.dev/docs/plugins/cloud-sql-pg/) - 用于 PostgreSQL 矢量存储的 Cloud SQL 插件。
   - [`genkitx-weaviate`](https://github.com/xavidop/genkitx-weaviate) - Weaviate 矢量商店插件。
   - [`genkitx-mongodb`](https://github.com/mongodb-partners/genkitx-mongodb/tree/main/plugin) - MongoDB 矢量存储插件。
3. 评估器插件
   - [`genkitx-promptfoo`](https://github.com/yukinagae/genkitx-promptfoo) - Promptfoo 评估插件。
4.其他插件
   - [`genkitx-graph`](https://github.com/TheFireCo/genkit-plugins/tree/main/plugins/graph) - 用于构建图形工作流程的插件。
   - [`@invertase/genkit-plugin-redis`](https://github.com/invertase/genkit-plugin-redis) - Genkit 的 Redis 插件，添加 Redis 以实现高效的状态存储、跟踪存储、缓存和速率限制。
   - [`genkitx-rxjs`](https://github.com/pavelgj/genkitx-rxjs) - Genkit 的简单 RxJS 帮助器/适配器。
   - [`@agentic/genkit`](https://docs.agentic.so/marketplace/ts-sdks/genkit) - Genkit SDK 的 Agentic Tools 适配器。
   - [`@auth0/ai-genkit`](https://genkit.dev/docs/plugins/auth0/) - Genkit 的官方 Auth0 插件，提供身份验证和授权功能。
   - [`genkitx-langfuse`](https://github.com/marcelfolaron/genkitx-langfuse) - 与 Langfuse 集成的插件，用于遥测和提示管理。
   - [`genkitx-posthog`](https://github.com/orchlab/genkitx-posthog) - 与 PostHog 集成以进行遥测和分析的插件。
   - [`ejentum-genkit`](https://github.com/ejentum/ejentum-genkit) - 插件，注册模型在生成之前调用的四个可代理调用的工具（推理、代码、反欺骗、内存）。每个调用都会从 Ejentum Reasoning Harness 中返回一个结构化的认知支架。

### Python - 官方
1. 模型/嵌入插件
   - [`google-genai`](https://genkit.dev/python/docs/reference/plugins/google-genai/) - Google Generative AI 插件通过 Gemini API 和 Vertex AI 模型提供与 Google Gemini 模型的接口。
   - [`ollama`](https://genkit.dev/python/docs/reference/plugins/ollama/) - Ollama 插件提供与 Ollama 支持的任何本地 LLM 的接口。
2.矢量商店插件
   - [`firestore`](https://genkit.dev/python/docs/reference/plugins/firestore/) - Firestore 插件提供 Firestore 矢量存储的接口。
   - [`dev_local_vectorstore`](https://genkit.dev/python/docs/reference/plugins/dev-local-vectorstore/) - 用于开发目的的本地矢量存储插件。
3.其他插件：
   - [`server flask`](https://genkit.dev/python/docs/flask/) - Flask 插件，用于使用 Genkit 构建 Web 应用程序。

### Golang - 官方

1. 模型/嵌入插件
   - [`googlegenai`](https://genkit.dev/go/docs/plugins/google-genai/) - Google Generative AI 插件通过 Gemini API 和 Vertex AI 模型提供与 Google Gemini 模型的接口。
   - [`ollama`](https://genkit.dev/go/docs/plugins/ollama/) - Ollama 插件提供与 Ollama 支持的任何本地 LLM 的接口。
   - [`compat_oai,compat_oai/openai,compat_oai/anthropic`](https://genkit.dev/go/docs/plugins/openai/) - 兼容 OpenAI API 的插件（OpenAI、Anthropic 提供商）。
2.矢量商店插件
   - [`pinecone`](https://genkit.dev/go/docs/plugins/pinecone/) - 松果矢量商店插件。
   - [`alloydb`](https://genkit.dev/go/docs/plugins/alloydb/) - AlloyDB 矢量存储插件。
   - [`localvec`](https://firebase.google.com/docs/genkit-go/rag) - 用于开发目的的本地矢量存储插件。
   - [`pgvector`](https://genkit.dev/go/docs/plugins/pgvector/) - PostgreSQL (PGVector) 矢量存储插件。
   - [`postgresql`](https://genkit.dev/go/docs/plugins/cloud-sql-pg/) - 用于 PostgreSQL 矢量存储的 Cloud SQL 插件。
   - [`weaviate`](https://github.com/firebase/genkit/tree/main/go/plugins/weaviate) - Weaviate 矢量商店插件。
3. 监控插件
   - [`googlecloud`](https://genkit.dev/go/docs/plugins/google-cloud/) - Google Cloud 插件将 Genkit 的遥测和日志记录数据导出到 Google Cloud 的操作套件。
4.其他插件：
   - [`mcp`](https://genkit.dev/go/docs/plugins/mcp/) - MCP 插件提供 MCP（托管上下文协议）的接口。

### Golang - 社区

1. 模型/嵌入插件
   - [`bedrock`](https://pkg.go.dev/github.com/xavidop/genkit-aws-bedrock-go) - AWS Bedrock API 的插件。
   - [`azureaifoundry`](https://pkg.go.dev/github.com/xavidop/genkit-azure-foundry-go) - Azure AI Foundry 的插件。
2.矢量商店插件
   - [`qdrant`](https://github.com/qdrant/qdrant-genkit/tree/main/go) - Qdrant 矢量商店插件。
3.监控插件：
   - [`opentelemetry`](https://github.com/xavidop/genkit-opentelemetry-go) - 用于监控 Genkit 应用程序的 OpenTelemetry 插件。

### Dart - 官方

1. 核心
   - [`genkit`](https://pub.dev/packages/genkit) - Genkit 的 Dart SDK，为文本生成、结构化输出、工具调用和代理工作流程提供统一的接口。
2. 模型/嵌入插件
   - [`genkit_google_genai`](https://pub.dev/packages/genkit_google_genai) - Genkit Dart 的 Google AI 插件。
   - [`genkit_anthropic`](https://pub.dev/packages/genkit_anthropic) - Genkit Dart 的 Anthropic 插件。
   - [`genkit_openai`](https://pub.dev/packages/genkit_openai) - Genkit Dart 的 OpenAI 插件。
   - [`genkit_chrome`](https://pub.dev/packages/genkit_chrome) - Genkit Dart 的 Chrome Prompt API (Gemini Nano) 插件。
   - [`genkit_firebase_ai`](https://pub.dev/packages/genkit_firebase_ai) - Genkit Dart 的 Firebase AI 插件。
3.其他插件
   - [`genkit_mcp`](https://pub.dev/packages/genkit_mcp) - Genkit Dart 的模型上下文协议 (MCP) 插件。
   - [`genkit_middleware`](https://pub.dev/packages/genkit_middleware) - Genkit Dart 的通用中间件（文件系统、技能、toolApproval）。
   - [`genkit_shelf`](https://pub.dev/packages/genkit_shelf) - Genkit Dart 的 Shelf HTTP 服务器集成。

### Java（非官方）- 社区

1. 核心
   - [`genkit-java`](https://github.com/genkit-ai/genkit-java/packages) - Genkit 的非官方 Java SDK，为构建 AI 应用程序提供 Java 支持。
2. 模型/嵌入插件
   - [`genkit-plugin-openai`](https://github.com/genkit-ai/genkit-java/tree/main/plugins/openai) - OpenAI 模型（GPT-4o、GPT-4o-mini 等）和嵌入的插件。
   - [`genkit-plugin-google-genai`](https://github.com/genkit-ai/genkit-java/tree/main/plugins/google-genai) - 用于 Google Gemini 模型和 Imagen 图像生成的插件。
   - [`genkit-plugin-anthropic`](https://github.com/genkit-ai/genkit-java/tree/main/plugins/anthropic) - Anthropic Claude 模型的插件。
   - [`genkit-plugin-aws-bedrock`](https://github.com/genkit-ai/genkit-java/tree/main/plugins/aws-bedrock) - 适用于 AWS Bedrock 模型（Amazon Nova、Claude、LLaMA、Mistral 等）的插件。
   - [`genkit-plugin-azure-foundry`](https://github.com/genkit-ai/genkit-java/tree/main/plugins/azure-foundry) - Azure AI Foundry 模型的插件。
   - [`genkit-plugin-xai`](https://github.com/genkit-ai/genkit-java/tree/main/plugins/xai) - XAI (x.ai) Grok 模型的插件。
   - [`genkit-plugin-deepseek`](https://github.com/genkit-ai/genkit-java/tree/main/plugins/deepseek) - DeepSeek 模型的插件。
   - [`genkit-plugin-cohere`](https://github.com/genkit-ai/genkit-java/tree/main/plugins/cohere) - Cohere Command 模型的插件。
   - [`genkit-plugin-mistral`](https://github.com/genkit-ai/genkit-java/tree/main/plugins/mistral) - Mistral AI 模型的插件。
   - [`genkit-plugin-groq`](https://github.com/genkit-ai/genkit-java/tree/main/plugins/groq) - Groq 超快速推理插件。
   - [`genkit-plugin-ollama`](https://github.com/genkit-ai/genkit-java/tree/main/plugins/ollama) - 本地 Ollama 模型的插件。
   - [`genkit-plugin-compat-oai`](https://github.com/genkit-ai/genkit-java/tree/main/plugins/compat-oai) - 适用于任何 OpenAI 兼容 API 端点的插件。
3.矢量商店插件
   - [`genkit-plugin-localvec`](https://github.com/genkit-ai/genkit-java/tree/main/plugins/localvec) - 用于开发的基于本地文件的矢量存储的插件。
   - [`genkit-plugin-firebase`](https://github.com/genkit-ai/genkit-java/tree/main/plugins/firebase) - Firebase 插件（Firestore 矢量搜索、云功能、遥测）。
   - [`genkit-plugin-weaviate`](https://github.com/genkit-ai/genkit-java/tree/main/plugins/weaviate) - Weaviate 矢量数据库插件。
   - [`genkit-plugin-postgresql`](https://github.com/genkit-ai/genkit-java/tree/main/plugins/postgresql) - 带有 pgvector 的 PostgreSQL 插件。
   - [`genkit-plugin-pinecone`](https://github.com/genkit-ai/genkit-java/tree/main/plugins/pinecone) - 松果矢量数据库插件。
4. 评估器插件
   - [`genkit-plugin-evaluators`](https://github.com/genkit-ai/genkit-java/tree/main/plugins/evaluators) - 用于预构建 RAGAS 式评估器的插件（忠实度、相关性等）。
5.其他插件
   - [`genkit-plugin-jetty`](https://github.com/genkit-ai/genkit-java/tree/main/plugins/jetty) - 使用 Jetty 12 的 HTTP 服务器插件。
   - [`genkit-plugin-spring`](https://github.com/genkit-ai/genkit-java/tree/main/plugins/spring) - 使用 Spring Boot 的 HTTP 服务器插件。
   - [`genkit-plugin-mcp`](https://github.com/genkit-ai/genkit-java/tree/main/plugins/mcp) - 用于模型上下文协议 (MCP) 客户端集成的插件。

## API 参考
1. [JavaScript](https://js.api.genkit.dev/) - JavaScript API 规范。
2. [Python](https://python.api.genkit.dev/) - Python API 规范。
3. [Golang](https://pkg.go.dev/github.com/firebase/genkit/go) - Golang API 规范。

## 书籍
1. [Mastering Genkit: Go Edition](https://mastering-genkit.github.io/mastering-genkit-go/) - 使用 Go 和 Genkit 构建可用于生产的 AI 应用程序。

## 解决方案

- [`internal AI`](https://github.com/tanabee/internal-ai) - 一款基于 Genkit 的开源内部 AI 聊天应用程序。
- [`Perplexity CLI`](https://github.com/xavidop/perplexity-cli) - 一种命令行界面 (CLI) 工具，利用 Genkit 通过利用来自模拟 Perplexity 工作原理的 Tavily AI 的网络搜索结果，为用户查询提供人工智能驱动的答案。
- [`GCP Cost MCP Server`](https://github.com/nozomi-koborinai/gcp-cost-mcp-server) - 使用 Genkit for Go 构建的 MCP 服务器，使 AI 助手能够直接估算 Google Cloud 成本，从而取代手动使用 GCP 定价计算器。
- [`Genkit Azure Function AI Foundry`](https://github.com/xavidop/genkit-azure-function-ai-foundry) - 演示如何将 Genkit 与 Azure Functions 和 Azure AI Foundry 结合使用的示例项目。
- [`Genkit AWS Lambda Bedrock`](https://github.com/xavidop/genkit-aws-lambda-bedrock) - 演示如何将 Genkit 与 AWS Lambda 和 Amazon Bedrock 结合使用的示例项目。
- [`Genkit Kraft`](https://github.com/DEEJ4Y/genkitkraft) - 一个基于 Genkit Go SDK 构建的自托管 LLM 代理平台，可让您通过可视化 UI、兼容 OpenAI 的 REST API 和 MCP 服务器支持来配置、测试和部署 AI 代理，以便与 Claude 等 AI 客户端一起使用。

## 会谈

- [Supercharge your app with Genkit](https://www.youtube.com/watch?v=eVud8llb_W0) - 关于如何使用 Genkit 增强您的应用程序的演讲。
- [Accelerating Generative AI App Development with Flutter & Genkit](https://speakerdeck.com/coborinai/accelerating-generative-ai-app-development-with-flutter-and-firebase-genkit) - 来自日本 Flutter 会议 FlutterGakkai 演示文稿的幻灯片，展示了如何将 Genkit 与 Flutter 集成以实现快速生成式 AI 应用程序开发。
- [Dart client for Genkit: Call Genkit Flows from Flutter/Dart - Slides](https://speakerdeck.com/coborinai/dart) - 来自 Google I/O Extended Tokyo 2025 闪电演讲的幻灯片，介绍了用于从 Flutter/Dart 应用程序调用 Genkit 流的 Dart 客户端库。
- [Dart client for Genkit: Call Genkit Flows from Flutter/Dart - Video](https://youtu.be/AakdczWQLzY?si=S5aT29miICHWQepM) - 来自 Google I/O Extended Tokyo 2025 闪电演讲的视频，介绍了用于从 Flutter/Dart 应用程序调用 Genkit 流的 Dart 客户端库。

## 视频
- [Getting started with Genkit/JS 1.0](https://www.youtube.com/watch?v=3p1P5grjXIQ) - 了解如何开始使用 Genkit/JS 1.0。
- [Getting started with Genkit (outdated)](https://www.youtube.com/watch?v=M8rfDySBBvM) - 有关如何开始使用 Genkit 的视频教程。
- [What are Genkit flows? (outdated)](https://youtu.be/ONR38NZK5FE) - 流是 Genkit 中的一个关键概念。了解它们的特别之处以及如何使用它们。
- [Build an Angular app with Genkit and deploy to Firebase (outdated)](https://youtu.be/TGHua_RtUjs) - 与 Pavel 一起构建 Angular 应用并将其部署到 Firebase。
- [DeepDive #1 - Genkit's reflection API and how it powers Genkit's developer UI (outdated)](https://youtu.be/CGVBR8quZac) - 了解 Genkit 开发人员 UI 如何通过反射 API 与 Genkit 进行通信。
- [Retrieval Augmented Generation (RAG) with Genkit (outdated)](https://youtu.be/p8ZlYAmbWHE) - 了解如何高效解析 PDF、使用 Genkit 的本地向量存储将其内容转换为可搜索向量，以及实施重新排序器以找出与您的查询最相关的文档。
- [Firebase After Hours #3 - Genkit: More than Meets the AI! (outdated)](https://youtu.be/VFPsp7aURWA?t=152s) - 与 Nohe 和 Peter 一起了解有关 Google 开源 AI 集成框架 Genkit 的更多信息。特邀嘉宾 Pavel Jbanov，Genkit 团队的首席工程师。
- [Firebase After Hours #4 - Genkit: Tooltime (outdated)](https://youtu.be/01XOIhh2ibA) - 了解如何通过使用工具调用将法学硕士连接到现实世界来赋予法学硕士超能力。

## 文章

- [Extracting structured data from PDFs using Gemini 2.0 and Genkit](https://firebase.blog/posts/2025/02/gemini-genkit-pdf-structured-data) - 了解如何使用 Gemini 2.0 和 Genkit 1.0 从 PDF 中提取结构化数据。
- [Genkit in Node, Building a Weather Service with AI Integration](https://xavidop.me/firebase/gcp/2025-02-28-firebase-genkit-node-tool/) - 探索如何使用 Express、GitHub 模型和工具在 Node.js 中使用 Genkit 构建天气服务。
- [Build Genkit Node.js apps with Dash Agents](https://medium.com/firebase-developers/build-firebase-genkit-nodejs-apps-with-dash-agents-skip-the-docs-258e067b3fdc) - 利用 Dash Agent 构建 Genkit Node.js 应用程序的分步指南。
- [Genkit with Gemma using Ollama](https://xavidop.me/firebase/gcp/2024-05-24-firebase-genkit-ollama/) - Firebase 项目使用 Gen AI Kit 和使用 Ollama 的 Gemma。
- [Master Gemma2 and Genkit](https://medium.com/firebase-developers/how-to-develop-using-the-gemma2-model-in-genkit-085f22ce68f3) - 了解如何将 Gemma2 与 Genkit 集成。
- [Unleash the Power of Function Calling with Genkit](https://medium.com/firebase-developers/implementing-function-calling-using-genkit-0c03f6cb9179) - 了解如何使用 Genkit 实现函数调用。
- [Unlocking the power of code execution in Genkit](https://medium.com/firebase-developers/getting-started-with-code-execution-in-genkit-c5391b45b321) - 了解如何在 Genkit 中集成 Python 代码。
- [Understanding Genkit flows with Czech language tricks](https://dev.to/denisvalasek/understanding-genkit-flows-with-czech-language-tricks-26i3) - 了解如何使用 Genkit 流并使用 Genkit UI 的功能。
- [Orchestrating Firebase and AI: 8 Genkit Architecture Patterns](https://medium.com/@nozomi-koborinai/orchestrating-firebase-and-ai-8-genkit-architecture-patterns-12e44db40345) - 使用 Genkit 集成 Firebase 和 AI 的 8 种架构模式指南。
- [High-Precision Responses with Genkits Google Search Integration](https://medium.com/firebase-developers/high-precision-responses-with-genkits-google-search-integration-7f142f5c9693) - 了解如何将 Google 搜索与 Genkit 集成。
- [How to Develop Firebase functions with Genkit](https://medium.com/@nozomi-koborinai/how-to-develop-firebase-genkit-functions-2677b386a227) - 通过 Genkit Firebase 产品集成对 Firebase 功能进行高效本地测试的实用指南。
- [Genkit for Go Developers: A Guide to Building LLM Applications](https://medium.com/@yukinagae/firebase-genkit-for-go-developers-a-guide-to-building-llm-applications-f96c51c34b10) - 使用 Genkit 的 Go 开发人员入门指南。
- [Orchestrating Firebase and AI: Genkit architecture example](https://docs.google.com/presentation/d/10F2hjzJhdInSuhDQ8G_B2raGz79mzTRIcWU_59Zh5Y8/edit?usp=sharing) - 在 GDG DevFest Tokyo 2024 的闪电演讲中发表。
- [Getting Started with AI Image Generation Apps on Flutter, Genkit, and Imagen 3](https://medium.com/@nozomi-koborinai/getting-started-with-ai-image-generation-apps-on-flutter-genkit-and-imagen-3-9a83c63cbdf3) - 使用 Flutter、Genkit 和 Google Imagen 3 构建 AI 图像生成应用程序的指南。
- [Extending Your AI Application with Genkit MCP](https://medium.com/@nozomi-koborinai/extending-your-ai-application-with-genkit-mcp-475d7533ca9e) - 了解如何使用 Genkit MCP 客户端集成 Google 地图，以查询 MCP 服务器以获得增强的基于位置的 AI 功能。
- [Understanding Model Context Protocol Through Building the Genkit for Dart MCP Plugin](https://koborin.ai/tech/mcp-deep-dive) - 深入探讨 MCP 规范，分享从为 Genkit Dart 实现 MCP 插件中获得的见解。
- [Genkit vs Agent Development Kit (ADK): Choosing the Right Google‑Backed AI Framework](https://medium.com/@nozomi-koborinai/genkit-vs-agent-development-kit-adk-choosing-the-right-google-backed-ai-framework-1744b73234ac) - 比较两个 Google 支持的人工智能框架，帮助开发人员选择适合自己需求的工具。
- [Dart Client for Genkit: Call Genkit Flows from Flutter/Dart](https://medium.com/@nozomi-koborinai/dart-client-for-genkit-call-genkit-flows-from-flutter-dart-b5a2c9b9400e) - 使用 Dart 客户端库从 Flutter 和 Dart 应用程序调用 Genkit 流的综合指南，具有流支持和类型安全性。
- [Gemini in your Slack workspace using Firebase & Genkit](https://dev.to/denisvalasek/gemini-in-your-slack-workspace-using-firebase-genkit-530c) - 了解如何使用 Genkit 作为 Slackbot 来集成 Gemini。
- [Set up RAG with Genkit and Firebase in 15 minutes](https://dev.to/denisvalasek/set-up-rag-with-genkit-and-firebase-in-15-minutes-50b2) - RAG、Genkit 以及使用 Firebase Firestore 作为矢量数据库简介。

## 教程

- [Slack Bot App](https://medium.com/firebase-developers/build-a-slack-bot-app-with-firebase-genkit-in-just-100-lines-71d4e49c9e08) - 有关如何使用 Genkit 构建 Slack Bot 应用程序的教程。

<!-- END CONTENT -->

## 关注

<!-- list people worth following on social sites (Twitter, LinkedIn, GitHub, YouTube etc.) -->

- [Firebase](https://x.com/firebase) - Firebase 的官方 Twitter 帐户。
- [Genkit Discord server](https://discord.gg/qXt5zzQKpc) - Genkit 的官方 Discord 服务器。
- [Genkit GitHub](https://github.com/firebase/genkit) - Genkit 的官方 GitHub 存储库。
- [Genkit Dart GitHub](https://github.com/genkit-ai/genkit-dart) - Genkit Dart 的官方 GitHub 存储库。
- [Genkit Java GitHub](https://github.com/genkit-ai/genkit-java) - Genkit Java 的非官方 GitHub 存储库。
