<!--lint disable remark-lint:awesome-list-item-->

#

<!-- [![Awesome](https://awesome.re/badge-flat2.svg)](https://awesome.re) -->
<div align="center">
  <img src="./.refs/imgs/awesome-github-copilot.svg" alt="Awesome Copilot Agents" height="300">
</div>

<h4align="center">✨ 精选的 GitHub 说明、提示、技能、MCP 和自定义代理 Markdown 文件列表，可增强您的 GitHub Copilot AI 体验。</h4>

<!--lint enable remark-lint:awesome-badge-->

<p对齐=“中心”>
  <a href="https://awesome.re">
    <img src="https://awesome.re/badge-flat2.svg" alt="Awesome">
</a>
</p>

<hr>

<p对齐=“中心”>
 <a href="CONTRIBUTING.md">📖 Contribution Guide</a>
</p>
<br>

## 内容

- [为什么选择副驾驶特工](#why-copilot-agents)
- [Instructions](#instructions)
  - [样板文件和模板](#boilerplates--templates)
  - [语言和堆栈](#language--stack)
  - [框架/库](#framework--library)
  - [Tools](#tools)
  - [Workflows](#workflows)
- [Prompts](#prompts)
  - [人工智能开发任务](#ai-development-tasks)
- [定制代理](#custom-agents)
  - [人工智能发展模式](#ai-development-mode)
- [代理技巧](#agent-skills)
- [MCPs](#mcps)
- [如何使用](#how-to-use)

## 为什么选择副驾驶特工

自定义说明、提示、代理技能、代理 MCP 和自定义代理通过提供有关存储库的上下文详细信息（例如您的团队遵循的工作流程类型、工具和其他项目特定详细信息（例如编码风格、使用的框架或项目特定规则））来帮助指导 GitHub Copilot。

**提示**：在 [VS Code 文档](https://code.visualstudio.com/docs/copilot/customization/overview) 中了解有关在 VS Code 中自定义 GitHub Copilot 的更多信息。

## 使用说明

指令为 Copilot 提供特定于存储库的上下文，例如编码标准、框架或工作流程，以改进代码建议。

### 样板文件和模板

#### 模板

- [General Language](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/boilerplate-and-templates/standard-language.instructions.md) - 用于构建说明文件的标准语言模板。

#### 样板文件

- [Standard IaC Tools Boilerplate](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/boilerplate-and-templates/standard-iac-tools.instructions.md) - 基础设施即代码工具的标准工具样板。

### 语言和堆栈

#### C

- [Standard Focus](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/languages/c/c.instructions.md) - 使用 POSIX/GNU libc 的系统库、CLI 工具和嵌入式应用程序。

#### C-夏普

- [Standard Focus](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/languages/csharp/csharp.instructions.md) - 具有现代 C# 模式和最佳实践的 .NET 应用程序。

#### C++

- [Standard Focus](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/languages/cplusplus/cplusplus.instructions.md) - 使用 STL、RAII 和性能优化的现代 C++ 开发。

#### 去

- [Standard Focus](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/languages/go/go.instructions.md) - 选择微服务、CLI 工具和并发应用程序。

#### 爪哇

- [Standard Focus](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/languages/java/java.instructions.md) - 使用 Spring 框架和现代模式进行企业 Java 开发。

#### JavaScript

- [Standard Focus](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/languages/javascript/javascript.instructions.md) - 采用 ES6+、Node.js 和浏览器开发的现代 JavaScript。

#### 科特林

- [Standard Focus](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/languages/kotlin/kotlin.instructions.md) - 用于 Android 开发和多平台项目的 Kotlin。

#### 卢阿

- [Standard Focus](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/languages/lua/lua.instructions.md) - 用于嵌入式系统、游戏开发和自动化的 Lua 脚本。

#### 蟒蛇

- [Standard Focus](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/languages/python/python.instructions.md) - 用于 Web 应用程序、数据科学和自动化的 Python 开发。

#### 铁锈

- [Standard Focus](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/languages/rust/rust.instructions.md) - 使用 Rust 的所有权模型和内存安全进行系统编程。

#### 斯威夫特

- [Standard Focus](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/languages/swift/swift.instructions.md) - 使用 Swift 和 SwiftUI 进行 iOS 和 macOS 开发。

#### 打字稿

- [Standard Focus](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/languages/typescript/typescript.instructions.md) - 适用于 Web 和 Node.js 应用程序的 TypeScript 开发。

### 框架/库

#### Cobra CLI（转到）

- [Charmbracelet Bubbles CLI](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/frameworks/cobra-cli-go/charmbracelet-cli.instructions.md) - 使用 Charm 的 Bubble Tea 框架和 Golang Cobra CLI 的交互式终端应用程序。

#### Node.js（打字稿）

- [Azure Function App](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/frameworks/nodejs-typescript/azure-function-app.instructions.md) - 使用 TypeScript Node.js 的 Azure Function 应用。
- [Express API](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/frameworks/nodejs-typescript/express-api.instructions.md) - 使用 Express.js 和 TypeScript Node.js 进行 REST API 开发。

### 工具

#### 内容管理系统 (CMS)

##### 德鲁帕尔

- [Standard Focus for Drupal 11](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/tools/cms/drupal/drupal-11.instructions.md) - Drupal 11 模块和主题开发。

#### 基础设施即代码 (IaC)

##### 地形

- [Standard Focus](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/tools/infra-as-code/terraform/terraform.instructions.md) - 标准 Terraform 说明。
- [Atmos](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/tools/infra-as-code/terraform/atmos-terraform.instructions.md) - 使用 Atmos 框架进行 Terraform 工作流程编排。

### 工作流程

#### AI开发说明

人工智能辅助开发的综合工作流程，具有结构化的规划、任务生成和执行方法。

- [PRD Creation](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/workflows/ai-development-instructions/prd-creation.instructions.md) - 创建详细的产品需求文档。
- [Task Generation](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/workflows/ai-development-instructions/task-generation.instructions.md) - 将 PRD 分解为可操作的开发任务。
- [Task Execution](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/instructions/workflows/ai-development-instructions/task-execution.instructions.md) - 通过适当的测试和 Git 实践来系统地执行任务。

## 提示

提示是可重复使用的任务或工作流程说明，可帮助指导 Copilot 执行特定操作或生成某些输出。

### 人工智能开发任务

人工智能辅助开发的综合工作流程，具有结构化的规划、任务生成和执行方法。

- [PRD Creation Prompt](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/prompts/ai-development-tasks/prd-creation.prompt.md) - 使用提示任务创建详细的产品需求文档。
- [Task Generation Prompt](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/prompts/ai-development-tasks/task-generation.prompt.md) - 使用提示任务将 PRD 分解为可操作的开发任务。
- [Task Execution Prompt](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/prompts/ai-development-tasks/task-execution.prompt.md) - 通过适当的测试和使用提示任务的 Git 实践来系统地执行任务。

## 定制代理

[自定义代理](https://code.visualstudio.com/docs/copilot/customization/custom-agents) 可让您在 VS Code 中为特定开发角色（如安全审核员、规划员或架构师）设置不同的 AI 角色，每个角色都有自己的说明、工具和行为。您还可以使用切换在指导工作流程（例如，规划→实施→审查）中在这些专业代理之间移动，并保留相关上下文。

内置的可用自定义代理有：

- 代理
- 询问
- 编辑
- 计划
- AIAgentExpert
- 配置自定义代理（创建您自己的）

### 人工智能发展模式

- [Architect](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/agents/ai-development-mode/architect.agent.md) - 设计和规划软件系统。
- [Clean Code](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/agents/ai-development-mode/clean-code.agent.md) - 使用干净代码最佳实践编写干净、可读且可维护的代码。
- [Debugger](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/agents/ai-development-mode/debugger.agent.md) - 调试您的应用程序代码以找到修复程序。
- [PRD Creation](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/agents/ai-development-mode/prd-creation.agent.md) - 构建产品需求文档 (PRD)。

## 代理技巧

代理技能是可移植的、[开放标准](https://agentskills.io/home)、版本控制的指令、脚本和资源文件夹，代理可以根据需要发现和加载这些文件夹，以便更准确、更高效地执行任务。它们让代理获得领域专业知识、新功能和可重复的工作流程，同时使这些相同的技能可以在不同的兼容代理产品和团队中重复使用。

### 一般

- [Calculator](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/skills/calculator/SKILL.md) - 执行任意精度算术计算，包括加法、减法、乘法、除法和指数。
- [Jira CLI](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/skills/jira-cli/SKILL.md) - 从命令行与 Jira 交互，以创建、列出、查看、编辑和过渡问题，管理冲刺和史诗，以及执行常见的 Jira 工作流程。
- [Skill Creator](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md) - 创建新技能、修改和改进现有技能以及衡量技能绩效。

### 文件

- [docx](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/skills/documents/docx/README.md) - 文档创建、编辑和分析，支持跟踪更改、注释、格式保存和文本提取。
- [pdf](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/skills/documents/pdf/README.md) - PDF 操作工具包，用于提取文本和表格、创建新的 PDF、合并/拆分文档以及处理表单。
- [pptx](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/skills/documents/pptx/README.md) - 演示文稿创建、编辑和分析。
- [xlsx](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/skills/documents/xlsx/README.md) - 电子表格创建、编辑和分析，支持公式、格式设置、数据分析和可视化。

### 云

- [Az CLI](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/skills/cloud/az-cli/SKILL.md) - 用于执行或询问 Azure CLI 命令的 Azure CLI 文档。
- [Azure Prices](https://github.com/Code-and-Sorts/awesome-copilot-agents/tree/main/skills/cloud/azure-prices/SKILL.md) - 使用 Azure 零售价格 API 查找并比较 Azure 服务定价。

### 发展

- [Playwright CLI](https://github.com/microsoft/playwright-cli/blob/main/skills/playwright-cli/SKILL.md) - 自动化浏览器交互、测试网页并使用 Playwright 测试。
- [Frontend Design](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md) - 创建具有高设计质量的独特的生产级前端界面。
- [Webapp Testing](https://github.com/anthropics/skills/blob/main/skills/webapp-testing/SKILL.md) - 使用 Playwright 与本地 Web 应用程序交互并测试本地 Web 应用程序的工具包。

## MCP

MCP（模型上下文协议服务器）为代理提供了一种连接外部工具、API、数据源和本地功能的标准化方法。它们通过公开读取文件、浏览网页、查询云平台或通过通用协议与开发工具交互等操作，扩展了代理在普通聊天之外的功能。

本节重点介绍可添加到 Copilot 设置中的有用 MCP 服务器，以扩展用于研究、开发、自动化和云工作流程的代理功能。

### 通用 MCP

- [Knowledge Graph Memory](https://github.com/modelcontextprotocol/servers/tree/main/src/memory) - 为您的代理创建本地知识图，以记住不同聊天会话中的信息。
- [Filesystem](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem) - 批量读写文件、搜索文件内容、列出文件并验证文件路径。
- [Fetch](https://github.com/modelcontextprotocol/servers/blob/main/src/fetch) - 自动进行网页浏览，以便代理检索和处理网页内容，将 HTML 转换为 Markdown 以便于使用。
- [Sequential Thinking](https://github.com/modelcontextprotocol/servers/tree/main/src/sequentialthinking) - 将复杂的问题分解为结构化的步骤。
- [GitHub](https://github.com/github/github-mcp-server) - 允许您的代理访问存储库和工作流程管理。
- [Time](https://github.com/modelcontextprotocol/servers/blob/main/src/time) - 使代理能够获取当前时间信息并使用 IANA 时区名称执行时区转换，并自动检测系统时区。

### 开发 MCP

- [Playwright](https://github.com/microsoft/playwright-mcp) - Playwright MCP 可自动执行浏览器交互、测试网页并使用 Playwright 测试。
- [Context7](https://github.com/upstash/context7) - 在代理会话中注入特定于版本的代码文档，为代码生成提供正确的 API 文档。

### 云 MCP

- [Azure MCP](https://github.com/microsoft/mcp/blob/main/servers/Azure.Mcp.Server/README.md) - Azure MCP 服务器通过跨不同 Azure 服务的 Azure 上下文为您的代理提供强大的支持。
- [AWS Documentation](https://github.com/awslabs/mcp/tree/main/src/aws-documentation-mcp-server) - 用于访问 AWS 文档、搜索内容并获取建议的代理工具。
- [gcloud](https://github.com/googleapis/gcloud-mcp) - 使用 gcloud CLI 与 Google Cloud 环境交互的代理工具。
- [KubeStellar Console](https://github.com/kubestellar/console) - MCP 服务器将 AI 代理桥接到多集群 Kubernetes 环境，以实现集群管理、Pod 检查和实时可观察性。

## 如何使用

### 在 VSCode 中设置 Copilot

1. 将鼠标悬停在状态栏中的 Copilot 图标上，然后选择设置 Copilot。
2. 选择“**登录**”以登录您的 GitHub 帐户，或者选择“**使用 Copilot**”（如果您已登录）。

**提示**：阅读有关设置 [VS Code Copilot](https://code.visualstudio.com/docs/copilot/setup) 的更多信息。

### 设置说明

1. 使用最新的命名约定创建指令文件：
1.工作区指令（将`*.instructions.md`文件放在`.github/instructions/`目录中）。
2. 工作区提示（将`*.prompt.md`文件放在`.github/prompts/`目录中）。
3.工作区自定义代理（将`*.agent.md`文件放在`.github/agents`目录中）。
4. 工作区自定义技能（技能存储在具有定义技能行为的“SKILL.md”文件的目录中）。
5.工作区单指令（将`copilot-instructions.md`放在`.github`目录中）。

#### 文件类型

##### 说明文件

`.instructions.md` - 适用于特定文件或文件类型的上下文说明。

##### 提示文件

`.prompt.md` - 针对特定任务或工作流程的可重复使用的提示。

##### 自定义代理文件

`.agent.md` - VS Code 中针对特定开发角色的预定义 AI 角色行为。

##### 定制代理技能

`SKILLS.md` - 代理可以按需发现和加载的指令、脚本和资源的可移植、版本控制文件夹。

##### 格式化

使用 YAML 前面的内容指定“applyTo”、“mode”和“description”等元数据。

## 贡献

欢迎所有贡献！如果您想共享指令文件（`.instructions.md`）、提示文件（`.prompt.md`）、技能（技能文件夹中的`SKILL.md`）或自定义代理（`.agent.md`），请参阅[贡献指南](CONTRIBUTING.md)了解详细信息。
