<!-- omit in toc -->
# 很棒的定制 [![Awesome](https://raw.githubusercontent.com/sindresorhus/awesome/main/media/badge.svg)](https://github.com/sindresorhus/awesome)

<p align="center">
  <a href="https://kustomize.io">
    <img src="img/awesome-kustomize.svg" width="90%">
  </a>
</p>

> 精彩的 Kustomize 资源的精选和协作列表。

[Kustomize](https://kustomize.io) 引入了一种无需模板的方式来自定义 Kubernetes 清单。它是可扩展的，并使用纯声明式方法进行配置自定义，帮助您高效管理基础设施即代码 (IaC)。

欢迎贡献，通过 [pull requests](https://github.com/aabouzaid/awesome-kustomize/pulls) 添加链接或创建问题来开始讨论。

推动它前进并在您的存储库中添加项目徽章以支持社区！ ⭐

降价：

```text
[![Awesome Kustomize](https://devopshive.com/badges/awesome-kustomize.svg)](https://github.com/DevOpsHiveHQ/awesome-kustomize)
```

预览：

[![Awesome Kustomize](https://raw.githubusercontent.com/DevOpsHiveHQ/awesome-kustomize/main/img/awesome-kustomize-badge.svg)](https://github.com/DevOpsHiveHQ/awesome-kustomize)

<!-- omit in toc -->
## 内容

- [Overview](#overview)
- [Plugins](#plugins)
  - [Generators](#generators)
  - [Transformers](#transformers)
  - [Validators](#validators)
- [Guides](#guides)
  - [Novice](#novice)
  - [Intermediate](#intermediate)
  - [Advanced](#advanced)
  - [提示和技巧](#tips--tricks)
- [Snippets](#snippets)
- [Misc](#misc)
- [相关列表](#related-lists)

## 概述

Kustomize 作为独立的二进制文件工作，也内置于 `kubectl` 中（自 v1.14 起）。它可以与现成的应用程序一起使用，例如 **Helm 图表**。此外，它还与各种 **GitOps** 工具深度集成，例如 ArgoCD、Flux 等。

## 插件

Kustomize 有 3 种插件类型：“generator”、“transformer”和“validator”。

> 注意事项
>
> 如果您是插件开发者，强烈建议支持新的插件标准
> [KRM 函数](https://github.com/kubernetes-sigs/kustomize/blob/master/cmd/config/docs/api-conventions/functions-spec.md)。

### 发电机

- [Secretize](https://github.com/bbl/secretize) - 从各种来源生成 Kubernetes Secret。它就像一把瑞士军刀，但用于 Kubernetes 秘密（Containerized KRM、Exec KRM、Exec）。
- [SopsSecretGenerator](https://github.com/goabout/kustomize-sopssecretgenerator/) - 从 sops 加密文件生成 Secret（Exec KRM、Exec）。
- [KSops](https://github.com/viaduct-ai/kustomize-sops) - 从 sops 加密文件生成 Secrets (Exec)。
- [PolicyGenerator](https://github.com/open-cluster-management-io/policy-generator-plugin) - 生成开放集群管理策略 (Exec)。
- [KRMFfnBuiltin](https://github.com/kaweezle/krmfnbuiltin) - 运行内置发电机变压器 (Exec)。
- [Merger](https://github.com/aabouzaid/kustomize-plugin-merger) - 通过使用无模式 StrategyMerge（容器化 KRM、Exec KRM）扩展 Kustomize 合并策略来无缝生成清单。

### 变形金刚

- [HelmValuesTransformer](https://github.com/openinfradev/kustomize-helm-transformer) - 转换 HelmRelease CustomResource 中的值。它有助于在单个转换器文件 (Exec) 中管理许多 HelmRelease 值。
- [TemplateTransformer](https://github.com/joshdk/template-transformer) - 提供一组 KRM 函数来就地运行内置变压器（容器化 KRM、Exec KRM）。

### 验证者

- [KubeconformValidator](https://github.com/aabouzaid/kustomize-kubeconformvalidator) - 使用嵌入式 Kubeconform（容器化 KRM、Exec KRM）验证 Kubernetes 清单。

## 指南

根据指南的级别或类型定制指南，例如📰文章、📺视频、🧪实验室。

### 新手

- 📰 [使用 Kustomize 对 Kubernetes 对象进行声明式管理](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/kustomization/) - Kustomize 的官方 Kubernetes 文档任务。
- 📰 [使用 Kustomize 配置 Kubernetes](https://cloud.google.com/anthos-config-management/docs/concepts/kustomize) - 指南可帮助您开始使用 Kustomize、了解其预期用例，并找到将其与其他 Google Cloud 工具一起使用的资源。
- 📺 [使用 Kustomize 整理 YAML 混乱](https://www.youtube.com/watch?v=1fCAwFGX38U) - 演讲展示了 Kustomize 如何帮助管理越来越多的服务和环境中的 Kubernetes YAML 文件。
- 📺 [Kustomize：使用无模板 YAML 部署您的应用程序](https://www.youtube.com/watch?v=ahMIBxufNR0) - 演讲介绍了 Kustomize，这是一个声明性应用程序管理系统，允许将部署描述为无模板 YAML。

### 中级

- 🧪 [ArgoCD GitOps 教程 - 使用 Kustomize](https://redhat-scholars.github.io/argocd-tutorial/argocd-tutorial/03-kustomize.html) - 动手实验涵盖在 GitOps 中使用 Kustomize，并介绍 Kustomize 语法和部署 Kustomized 应用程序。
- 📰 [使用 Kustomize 自定义现成 Helm 图表的 3 种方法](https://tech.aabouzaid.com/2020/09/3-ways-to-customize-off-the-shelf-helm-charts-with-kustomize-kubernetes.html) - 指南涵盖了一起使用 Kustomize 和 Helm 的 3 种不同方法。
- 📰 [通过 Cluster API 使用 Kustomize 组件](https://blog.scottlowe.org/2021/11/01/using-kustomize-components-with-cluster-api/) - 使用 Kustomize 组件的清晰用例。

### 高级

- 📰 [高级 Kustomize 功能](https://www.innoq.com/en/blog/advanced-kustomize-features/) - 指南涵盖 5 种以上高级 Kustomize 功能。
- 📰 [为 Kubernetes 自定义资源设置 OpenAPI 补丁策略](https://tech.aabouzaid.com/2022/11/set-openapi-patch-strategy-for-kubernetes-custom-resources-kustomize.html) - 指南展示了如何提供一个模式来控制 CRD 的补丁策略。
- 📺 [使用客户端自定义资源自定义 Kustomize](https://www.youtube.com/watch?v=YlFUv4F5PYc) - 演讲涵盖通过插件扩展 Kustomize 以满足常见但特殊的应用程序需求。
- 📺 [拥有您的 YAML：通过插件扩展 Kustomize](https://www.youtube.com/watch?v=Xoh_OpLoVtI) - 演讲展示了如何使用 Kustomize 外部插件创建自定义资源。
- 📰 [Kustomize 通过 KRM 功能增强](https://www.innoq.com/en/blog/kustomize-enhancement-with-krm-functions/) - 详细指南涵盖了 KRM 概念以及如何在 Kustomize 插件中使用它。

### 提示与技巧

- 📰 [从 Kustomize 基础删除清单](https://tech.aabouzaid.com/2021/05/delete-a-manifest-from-kustomize-base.html) - 使用 Kustomize 补丁删除命名清单的便捷方法。
- 📰 [在单个资源上应用 Kustomize 内置变压器](https://tech.aabouzaid.com/2022/04/apply-kustomize-builtin-transformers-on-a-single-resource.html) - 一种在特定资源上使用内部变压器的方法。
- 📰 [将额外数据传递到容器化 KRM 功能](https://tech.aabouzaid.com/2022/12/pass-extra-data-to-the-containerized-krm-function.html) - 与容器化 KRM 功能共享数据的不同情况。


## 片段

代码片段是 Kustmoize 特定用例的示例，可以帮助完成常见的日常操作。

- [Add Pod security context](https://github.com/3deep5me/awesome-kustomize/blob/add-security-context-component/snippets/add-pod-security-context/kustomization.yaml) - 确保安全上下文已添加到 Pod 中的容器中。

## 杂项

- [Asdf-kustomize](https://github.com/Banno/asdf-kustomize) - 用于 asdf 版本管理器的 Kustomize 插件。


## 相关列表

- [Awesome Kubernetes](https://github.com/ramitsurana/awesome-kubernetes) - 精彩的 Kubernetes 资源精选列表。
- [Awesome Kubectl plugins](https://github.com/ishantanu/awesome-kubectl-plugins) - 很棒的 Kubectl 插件的精选列表。
- [Awesome Helm](https://github.com/cdwv/awesome-helm) - 精选的 Helm 图表和资源列表。
