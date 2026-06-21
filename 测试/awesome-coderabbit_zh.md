# 很棒的代码兔子 [![Awesome](https://awesome.re/badge-flat.svg)](https://awesome.re)

[CodeRabbit](https://www.coderabbit.ai) 是一款人工智能驱动的代码审查工具，可帮助开发团队提高代码质量并加快审查流程。它与流行的版本控制平台集成，并提供有关代码更改的智能反馈。

此精选列表涵盖了与 CodeRabbit 🐰 相关的最佳资源、教程和社区内容

## 内容

- [官方资源](#official-resources)
- [开始使用](#getting-started)
- [API参考](#api-reference)
- [配置举例](#configuration-examples)
- [集成指南](#integration-guides)
- [视频教程](#video-tutorials)
- [Blogs](#blogs)
- [媒体报道](#media-coverage)
- [社区评论](#community-reviews)
- [使用 CodeRabbit 的项目](#projects-using-coderabbit)

## 官方资源

- [Documentation](https://docs.coderabbit.ai) - 涵盖 CodeRabbit 各个方面的综合文档。
- [Blog](https://www.coderabbit.ai/blog) - 官方博客提供更新、教程和最佳实践。
- [FAQ](https://www.coderabbit.ai/faq) - 有关 CodeRabbit 的常见问题。
- [GitHub Repository](https://github.com/coderabbitai/ai-pr-reviewer) - 官方 AI PR 审阅者存储库。
- [LinkedIn](https://www.linkedin.com/company/coderabbitai/) - LinkedIn 官方形象。
- [Twitter](https://x.com/coderabbitai) - 官方 Twitter/X 帐户。
- [YouTube Channel](https://www.youtube.com/@CodeRabbitAI) - 包含教程和更新的官方 YouTube 频道。

## 开始使用

- [CodeRabbit Startup Program](https://www.coderabbit.ai/blog/coderabbit-startup-program) - 针对初创公司的特别计划。
- [AI Code Reviewer Examples](https://www.coderabbit.ai/blog/how-to-use-an-ai-code-reviewer-on-github-in-4-examples) - 使用 CodeRabbit 的四个实际示例。

## API参考

- [OpenAPI Documentation](https://docs.coderabbit.ai/api-reference/) - CodeRabbit 的 REST API 端点的完整 Swagger 文档。

## 配置举例

### 企业配置示例

探索来自不同项目的真实 CodeRabbit 配置。

```yaml
# yaml-language-server: $schema=https://coderabbit.ai/integrations/schema.v2.json
language: "en-US"
early_access: false
tone_instructions: 'You are an expert code reviewer in Java, TypeScript, JavaScript, and NodeJS. You work in an enterprise software developer team, providing concise and clear code review advice. You only elaborate or provide detailed explanations when requested.'
reviews:
  profile: "chill"
  request_changes_workflow: false
  high_level_summary: true
  poem: true
  review_status: true
  collapse_walkthrough: false
  auto_review:
    enabled: true
    drafts: false
    base_branches: ["pg", "release"]
  path_instructions:
    - path: "app/client/cypress/**/**.*"
      instructions: |
        Review the following e2e test code written using the Cypress test library. Ensure that:
        - Follow best practices for Cypress code and e2e automation
        - Avoid using cy.wait in code
        - Avoid using cy.pause in code
        - Avoid using agHelper.sleep()
        - Use locator variables for locators
        - Use data-* attributes for selectors
        - Avoid Xpaths, Attributes and CSS path
        - Avoid selectors like .btn.submit
        - Perform logins via API
        - Avoid using it.only
        - Use multiple assertions
        - Avoid string assertions
        - Ensure unique filenames
chat:
  auto_reply: true
```

在 [`configs/`](configs/) 目录中查找更多示例，按语言组织：

```
configs/
├── javascript/   # JavaScript project configurations
├── typescript/   # TypeScript project configurations
├── python/       # Python project configurations
├── go/          # Go project configurations
└── multi-language/ # Full-stack project configurations
```


## 集成指南

- [Azure DevOps Integration](https://www.coderabbit.ai/blog/getting-started-with-coderabbit-using-azure-devops) - 与 Azure DevOps 集成的指南。
- [CI/CD Pipeline Integration](https://www.coderabbit.ai/blog/how-to-run-static-analysis-on-your-ci-cd-pipelines-using-ai) - 将人工智能驱动的静态分析添加到 CI/CD 管道中。
- [Linear Board Integration](https://www.coderabbit.ai/blog/how-to-use-coderabbit-to-validate-issues-against-linear-board) - 线性板集成指南。
- [DevOps Pipeline Integration](https://www.coderabbit.ai/blog/how-to-integrate-ai-code-review-into-your-devops-pipeline) - 全面的 DevOps 集成指南。

## 视频教程

- [Getting Started Tutorial](https://www.youtube.com/watch?v=3SyUOSebG7E) - 新用户的官方分步指南。

## 博客

- [人工智能可以免费进行代码审查](https://tomaszs2.medium.com/ai-can-make-a-code-review-for-free-a559cf74efa5)
- [CodeRabbit 深入探究](https://www.coderabbit.ai/blog/coderabbit-deep-dive)
- [CodeRabbit 与其他：AI 代码审查工具](https://www.devtoolsacademy.com/blog/coderabbit-vs-others-ai-code-review-tools)
- [为什么开发人员讨厌 Linters](https://www.coderabbit.ai/blog/why-developers-hate-linters)
- [如何使用 CodeRabbit 自动进行 TypeScript 代码审查](https://www.coderabbit.ai/blog/how-to-automate-typescript-code-reviews-with-coderabbit)


## 媒体报道

- [TechCrunch Coverage](https://techcrunch.com/2024/08/15/coderabbit-raises-16m-to-bring-ai-to-code-reviews/) - TechCrunch 关于 CodeRabbit 1600 万美元融资的文章。
- [Silicon Angle Feature](https://siliconangle.com/2024/08/14/ai-code-review-startup-coderabbit-raises-16m-help-developers-debug-code-faster/) - 报道 CodeRabbit 的资金和使命。

## 社区评论

- [G2 Reviews](https://www.g2.com/products/coderabbit/reviews) - 已验证的用户评论和评级。
- [Developer Testimonials](https://tomaszs2.medium.com/ai-code-review-tool-coderabbit-replaces-me-and-i-like-it-b1350a9cda58) - CodeRabbit 的真实体验。

## 使用 CodeRabbit 的项目

> 以下是一些使用 CodeRabbit 进行人工智能驱动的代码审查的开源项目的列表。

- [Appsmith](https://github.com/appsmithorg/appsmith) - 用于构建内部工具的低代码平台[示例回顾](https://github.com/appsmithorg/appsmith/pull/37200)。
- [Crowd.dev](https://github.com/CrowdDotDev/crowd.dev) - 开源开发者社区平台[示例回顾](https://github.com/CrowdDotDev/crowd.dev/pull/2671)。
- [Documenso](https://github.com/documenso/documenso) - 开源 DocuSign 替代方案 [示例回顾](https://github.com/documenso/documenso/pull/1436)。
- [Formbricks](https://github.com/formbricks/formbricks) - 开源调查和体验管理解决方案[示例回顾](https://github.com/formbricks/formbricks/pull/4229)。
- [Neon](https://github.com/neondatabase/neon) - 无服务器 Postgres 数据库平台 [示例回顾](https://github.com/neondatabase/neon/pull/9100)。
- [NextUI](https://github.com/nextui-org/nextui) - 漂亮、快速、现代的 React UI 库 [示例回顾](https://github.com/nextui-org/nextui/pull/3680)。
- [Novu](https://github.com/novuhq/novu) - 开源通知基础设施[示例回顾](https://github.com/novuhq/novu/pull/5401)。
- [OpenObserve](https://github.com/openobserve/openobserve) - 云原生可观察性平台[示例回顾](https://github.com/openobserve/openobserve/pull/4865)。
- [Permify](https://github.com/Permify/permify) - 授权服务和策略引擎[示例回顾](https://github.com/Permify/permify/pull/1754)。
- [Pipedream](https://github.com/PipedreamHQ/pipedream) - 连接 API，速度非常快 [示例回顾](https://github.com/PipedreamHQ/pipedream/pull/14498)。
- [Plane](https://github.com/makeplane/plane) - 开源项目管理工具[示例回顾](https://github.com/makeplane/plane/pull/5933)。
- [Unkey](https://github.com/unkeyed/unkey) - API密钥管理解决方案[示例回顾](https://github.com/unkeyed/unkey/pull/2639)。
- [UploadThing](https://github.com/pingdotgg/uploadthing) - 现代网络的文件上传解决方案[示例回顾](https://github.com/pingdotgg/uploadthing/pull/1038)。
