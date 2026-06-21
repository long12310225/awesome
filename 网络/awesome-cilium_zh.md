# 很棒的纤毛 [![Awesome](https://awesome.re/badge.svg)](https://github.com/sindresorhus/awesome)

> Cilium 是一个开源网络项目，为容器化应用程序、微服务和虚拟机提供网络和安全功能。

最近 [Cilium](https://docs.cilium.io/en/stable) 推出了一个关于 eBPF 的优秀网站，名为 [ebpf.io](https://ebpf.io/)。它的目的与此列表类似，包含[eBPF 简介](https://ebpf.io/what-is-ebpf)。

## 内容

- [参考文档](#reference-documentation)
- [纤毛相关项目](#cilium-related-projects)
- [文章和演示文稿](#articles-and-presentations)
- [社区活动](#community-events)
- [社区和贡献](#community-and-contributing)
- [实践内容](#hands-on-contents)

## 参考文档

- [Website](https://cilium.io) - Cilium 官方网站，最初由 [Isovalent](https://isovalent.com/) 创建。
- [Official GitHub repository](https://github.com/cilium) - Cilium 项目的 GitHub 存储库。
- [A cookbook of installing Cilium on AWS EKS](https://github.com/littlejo/cilium-eks-cookbook) - 在 EKS 中安装 Cilium 的多种方法。
- [Cilium Certified Associate Study Guide](https://github.com/isovalent/CCA-Study-Guide) - 帮助 Cilium 社区准备 CNCF 的 Cilium 认证助理 (CCA) 考试的学习指南。

## 纤毛相关项目

- [Cilium](https://github.com/cilium/cilium) - 适用于各种容器运行时（例如 Kubernetes、Docker 和 Mesos）的网络插件。它利用 eBPF 等 Linux 内核功能为应用程序提供快速、安全的网络和负载平衡。
- [eBPF](https://github.com/cilium/ebpf) - 允许在 Linux 内核中进行动态、可编程数据包过滤和网络分析的技术。
- [Cilium Proxy](https://github.com/cilium/proxy) - 高性能 HTTP、TCP 和 gRPC 代理，可自动注入 Kubernetes Pod。它提供负载平衡、运行状况检查和 L7 可见性等功能。
- [Cilium Cluster Mesh](https://docs.cilium.io/en/v1.9/gettingstarted/clustermesh/) - 使用加密隧道将多个 Kubernetes 集群安全地连接在一起。它支持跨集群的无缝通信和服务发现，同时保持强大的安全边界。
- [Hubble](https://github.com/cilium/hubble) - 由 Cilium 社区构建的网络可见性和监控工具。它提供网络流量的实时可见性，使操作员能够深入了解应用程序行为、解决连接问题并实施网络安全策略。
- [Cilium Operator](https://docs.cilium.io/en/stable/internals/cilium_operator/) - Kubernetes Operator，可简化 Kubernetes 集群内 Cilium 的部署和管理。它可以自动执行部署 Cilium 代理、配置 eBPF 策略和处理升级等任务。
- [Tetragon](https://github.com/cilium/tetragon) - 运行时安全实施和可观察性工具。
- [Cilium Mesh](https://isovalent.com/blog/post/introducing-cilium-mesh/) - 连接在云、本地或边缘运行的 Kubernetes 工作负载、虚拟机和物理服务器。
- [NetworkPolicy Editor](https://editor.networkpolicy.io/) - 创建、可视化和共享 Kubernetes 网络策略。
- [Prometheus & Grafana for Cilium](https://github.com/cilium/cilium/tree/main/examples/kubernetes/addons/prometheus) - 从 Cilium 收集指标并将其存储在 Prometheus 中以进行分析和警报。
- [Cilium Helm Chart](https://artifacthub.io/packages/helm/cilium/cilium) - 可用于在 Kubernetes 上部署 Cilium 的 Helm 图表。
- [Hubble adaptor for OpenTelemetry](https://github.com/cilium/hubble-otel) - 允许使用 OpenTelemetry 收集器导出哈勃流数据。
- [Packet, where are you?](https://github.com/cilium/pwru) - 基于 eBPF 的 Linux 内核网络调试器。
- [Coroot](https://github.com/coroot/coroot) - 将遥测数据转化为可行的见解，帮助您快速识别和解决应用程序问题。
- [Pixie](https://github.com/pixie-io/pixie) - 即时 Kubernetes 原生应用程序可观察性。
- [caretta](https://github.com/groundcover-com/caretta) - 即时 K8s 服务依赖关系图，直接到您的 Grafana。
- [Netreap](https://github.com/cosmonic-labs/netreap) - Nomad 的 Cilium 控制器实现。
- [Gloo Network](https://www.solo.io/products/gloo-network/) - 使由 eBPF 提供支持的 Cilium-CNI 能够为现代应用程序提供网络、数据包过滤和可观察性。
- [Bpfilter instead of iptables for routing](https://www.admin-magazine.com/Archive/2019/50/Bpfilter-offers-a-new-approach-to-packet-filtering-in-Linux) - Bpfilter 提供了一种在 Linux 中进行数据包过滤的新方法。

![image](https://github.com/seifrajhi/awesome-cilium/assets/26981510/b2236520-ea4c-400d-a5fd-15850a8bf420)

- [Inter-node traffic control](https://docs.cilium.io/en/latest/network/kubernetes/policy/#ciliumclusterwidenetworkpolicy) - 适用于整个集群（非命名空间）的策略，并为您提供将节点指定为源和目标的方法。
- [BPF and XDP Reference Guide](http://docs.cilium.io/en/latest/bpf/) - 来自 Cilium 项目的指南。
- [Why is the kernel community replacing iptables with BPF?](https://cilium.io/blog/2018/04/17/why-is-the-kernel-community-replacing-iptables/) - Cilium 发表的关于 eBPF 和 bpfilter 背后动机的博客文章，其中包含示例以及使用 eBPF 和 bpfilter 的其他项目的链接。
- [Bpfilter: Linux firewall with eBPF sauce](https://qmo.fr/docs/talk_20180316_frnog_bpfilter.pdf) - 幻灯片来自 Quentin Monnet 的演讲，内容涉及 eBPF 背景并将 bpfilter 与 iptables 进行比较。
- [Cilium: Networking & Security for Containers with BPF & XDP](http://www.slideshare.net/ThomasGraf5/clium-container-networking-with-bpf-xdp) - 具有负载均衡器用例。
- [Cilium: Networking & Security for Containers with BPF & XDP](http://www.slideshare.net/Docker/cilium-bpf-xdp-for-containers-66969823) - [视频](https://www.youtube.com/watch?v=TnJF7ht3ZYc&list=PLkA60AVN3hh8oPas3cq2VA9xB7WazcIgs)。
- [Cilium: Fast IPv6 container Networking with BPF and XDP](http://www.slideshare.net/ThomasGraf5/cilium-fast-ipv6-container-networking-with-bpf-and-xdp) - 使用 BPF 和 XDP 进行快速 IPv6 容器网络。
- [Cilium: BPF & XDP for containers](https://fosdem.org/2017/schedule/event/cilium/) - 用于容器的 BPF 和 XDP。
- [Learning ebpf book](https://github.com/lizrice/learning-ebpf) - 学习 eBPF，O'Reilly 出版！您可以在此处找到示例的虚拟机配置。

## 文章和演示文稿

- [eBPF log analytics in your Kubernetes cluster](https://www.parseable.io/blog/ebpf-log-analytics) - 利用 Cilium 的 Tetragon 捕获基于 eBPF 的文件访问日志并将其发送到 Parseable 进行警报和进一步分析。
- [Introduction to Cilium](https://www.youtube.com/watch?v=80OYrzS1dCA) - 由 Isovalent 的 Thomas Graf 和 Liz Rice 主持的直播，涵盖与 eBPF 和 Cilium 相关的所有内容。
- [Cilium CNI](https://medium.com/itnext/cilium-cni-a-comprehensive-deep-dive-guide-for-networking-and-security-enthusiasts-588afbf72d5c) - 面向网络和安全爱好者的全面深入指南。
- [Cilium for Kubernetes networking](https://blog.palark.com/why-cilium-for-kubernetes-networking/) - 我们为什么使用它以及为什么我们喜欢它。
- [A generic introduction to Cilium](https://opensource.googleblog.com/2016/11/cilium-networking-and-security.html) - Cilium 的一般介绍。
- [A podcast interviewing Thomas Graf](http://blog.ipspace.net/2016/10/fast-linux-packet-forwarding-with.html) - Ivan Pepelnjak 于 2016 年 10 月在 eBPF、P4、XDP 和 Cilium 上采访 Thomas。
- [How eBPF streamlines the service mesh](https://thenewstack.io/how-ebpf-streamlines-the-service-mesh/) - 探索 eBPF 如何帮助我们简化服务网格，使数据平面更高效、更易于部署。
- [From Amazon VPC CNI to Cilium with zero downtime](https://medium.com/codex/migrate-to-cilium-from-amazon-vpc-cni-with-zero-downtime-493827c6b45e) - 从 Amazon VPC CNI 迁移到 Cilium，停机时间为零。
- [Cilium CNI and OKE on Oracle Cloud](https://medium.com/oracledevs/cni-adventures-with-kubernetes-on-oracle-cloud-cilium-5c6f011746d5) - Kubernetes 与 Oracle Cloud 上的 Cilium CNI 和 OKE 联网。
- [Cilium in Azure Kubernetes Service (AKS)](https://learn.microsoft.com/en-us/azure/aks/azure-cni-powered-by-cilium) - 在 Azure Kubernetes 服务 (AKS) 中配置由 Cilium 提供支持的 Azure CNI。
- [eCHO News NEWSLETTER](https://www.linkedin.com/newsletters/echo-news-6937495018668482560/) - eCHO 新闻，每两周一次总结 eBPF 和 Cilium 的所有内容。
- [Exploring eBPF and XDP](https://naftalyava.com/example-xdp-ebpf-code-for-handling-ingress-traffic/) - 如何开始使用 XDP 的基本示例。
- [eBPF - Rethinking the Linux Kernel](https://docs.google.com/presentation/d/1AcB4x7JCWET0ysDr0gsX-EIdQSTyBtmi6OAW7bE0jm0/edit#slide=id.g6e43ab8f8d_0_612) - Linux 内核的 eBPF 类似 JavaScript 的功能。
- [Learn how Tetragon can stop CVEs with YAML](https://djalal.opendz.org/post/prevent-kernel-overlayfs-ubuntu-cves-with-yaml/) - 使用 YAML (bpf) 防止 Ubuntu 内核上的 Overlayfs 权限升级。
- [Cilium + Istio](https://www.solo.io/blog/cilium-1-14-istio/) - 使用 Istio 快速浏览 Cilium 1.14。
- [Cilium: Decoding the packet path with security groups for pods in EKS](https://medium.com/@amitmavgupta/security-groups-for-pods-in-eks-cilium-and-networking-f809cf72fc31) - 使用 EKS 中 Pod 的安全组解码数据包路径。
- [Cilium mutual auth … DIY](https://xxradar.medium.com/cilium-mutual-auth-diy-5d5036a82cf9) - 快速完成在自我管理的 Kubernetes 集群上设置 Cilium、mtls。
- [Istio service mesh with ALB in EKS](https://medium.com/@amitmavgupta/installing-cilium-in-azure-kubernetes-service-byocni-with-no-kube-proxy-825b9007b24b) - 与 iptables 相比，以 BYOCNI 模式无缝安装 Cilium 并利用 eBPF 功能。
- [Kubernetes LoadBalance service using Cilium BGP control plane](https://medium.com/@valentin.hristev/kubernetes-loadbalance-service-using-cilium-bgp-control-plane-8a5ad416546a) - 演练在最小的 K3s Kubernetes 集群中为负载均衡器服务创建基于 Cilium 的支持的过程。
- [eBPF-based networking with Cilium](https://b-nova.com/en/home/content/ebpf-based-networking-with-cilium) - 它是什么以及它能做什么？
- [Deploying Red Hat OpenShift with Cilium](https://isovalent.com/blog/post/deploying-red-hat-openshift-with-cilium/) - 有关部署 Cilium 和 Red Hat OpenShift 的教程。
- [Setting up EKS Amazon clusters, adding Cilium to projects using Terraform and Helm, supporting GitOps, and using Karpenter for efficient resource utilization and cost savings](https://aws.plainenglish.io/architecting-for-resilience-crafting-opinionated-eks-clusters-with-karpenter-cilium-cluster-mesh-c87cee1df934) - 弹性架构：使用 Karpenter 和 Cilium Cluster Mesh 制作固执己见的 EKS 集群。
- [Kubernetes Gateway API with Cilium](https://kubito.dev/posts/kubernetes-gateway-api-cilium/) - 有关如何有效配置 Cilium 以在 Kubernetes 环境中设置网关 API 的指南。
- [How to migrate from Red Hat OpenShiftSDN/OVN-Kubernetes to Cilium](https://veducate.co.uk/migrate-red-hat-openshiftsdn-ovn-kubernetes-cilium/) - 从 OpenShiftSDN 或 OVN-Kubernetes 迁移到 Cilium 的分步过程。
- [Setup basic L4 load balancing with Cilium CNI and Ubuiqiti Edge Router](https://www.viktorious.nl/2024/01/05/setup-basic-l4-load-balancing-with-cilium-cni-and-ubuiqiti-edge-router/) - 使用 Cilium CNI 和 Ubuiqiti 边缘路由器设置基本的 L4 负载平衡。

## 社区活动

- [CiliumCon](https://cilium.io/events/) - 为 Cilium 用户、贡献者和新社区成员举办的全天同地活动。
- [Isovalent Security Summer School 2023](https://isovalent.com/events/2023-07-security-summer-school/) - 虚拟安全暑期学校，设有动手实验室。了解 Cilium、Tetragon 和 Hubble 如何帮助提高 Kubernetes 安全性。
- [Isovalent's cilium related events](https://isovalent.com/events/) - 以不同声音、创新公司和伟大想法为特色的活动。

## 社区和贡献

- [Slack channel](https://cilium.herokuapp.com/) - 如需实时对话和快速提问，请加入 Cilium Slack 工作区。
- [Twitter](https://twitter.com/ciliumproject) - 在 Twitter 上关注 Cilium，了解最新新闻和公告。
- [YouTube](https://www.youtube.com/c/eBPFCiliumCommunity) - 观看来自 Cilium 和 eBPF 社区的视频。
- [Contributors](https://github.com/cilium/cilium/graphs/contributors) - 对主要的贡献。

## 实践内容

- [Isovalent library for Cilium](https://isovalent.com/resource-library/) - 查找视频、案例研究、博客、书籍、实验室和分析师报告。
- [Cilium Learning Tracks](https://isovalent.com/learning-tracks/) - 面向云网络工程师、安全专业人员、平台工程师、平台运维人员（服务网格）和云架构师的课程。
- [K0S Cilium Playground](https://github.com/xinity/k0s_cilium_playground) - 完全基于 bash 的 k0s Cilium Clustermesh 支持的游乐场。
- [Podcast: Kubernetes Unpacked Podcast](https://packetpushers.net/podcast/kubernetes-unpacked-022-kubernetes-networking-and-abstraction-with-cilium-and-ebpf/) - Kubernetes Unpacked 022：使用 Cilium 和 eBPF 进行 Kubernetes 网络和抽象。
- [From Zero to Cluster Mesh: Installing and Configuring Cilium CNI on Kubernetes](https://www.youtube.com/watch?v=z8Kifl3M3LU&list=PLQpKr4_0p0jEIGtCeV4VcGd_-Jf49e1JY) - 如何安装和配置 Cilium CNI 并跨 Kubernetes 集群启用其高级集群网格功能。
- [Cilium and SPIRE integration](https://github.com/accuknox/cilium-spire-tutorials) - 有关 Cilium 和 SPIRE 集成的教程。
- [Cilium Network policies Library](https://github.com/kubearmor/policy-templates/tree/main) - 社区为 KubeArmor 和 Cilium 整理的系统和网络策略模板列表。
- [Kyverno policies for Cilium Network Policies](https://github.com/adobeSlash/cilium-kyverno) - 用于控制 Cilium 网络策略创建的 Kyverno 策略示例。

## 贡献

> 注意：Cilium 是一项令人兴奋的技术，其生态系统正在不断发展。我们希望得到_you_的帮助，使这个很棒的列表保持最新状态，并尽我们所能提高其信噪比。请随时留下[任何反馈](https://github.com/seifrajhi/awesome-cilium/issues)。

_请在贡献之前阅读[贡献指南](CONTRIBUTING.md)。_
