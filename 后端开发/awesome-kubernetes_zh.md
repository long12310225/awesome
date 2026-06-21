# Awesome Kubernetes [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> 精选的 Kubernetes 工具、资源和工作负载列表。

## 目录

- [安装工具](#安装工具)
- [集群管理](#集群管理)
- [监控](#监控)
- [存储](#存储)
- [网络](#网络)
- [安全](#安全)
- [CI/CD](#cicd)
- [服务网格](#服务网格)
- [机器学习](#机器学习)
- [资源](#资源)

## 安装工具

- [Minikube](https://github.com/kubernetes/minikube) - 本地 Kubernetes。
- [Kind](https://github.com/kubernetes-sigs/kind) - Docker 内 Kubernetes。
- [K3s](https://github.com/k3s-io/k3s) - 轻量级 Kubernetes。
- [K3d](https://github.com/k3d-io/k3d) - Docker 内 K3s。
- [MicroK8s](https://github.com/canonical/microk8s) - 最小化 Kubernetes。
- [Kubeadm](https://github.com/kubernetes/kubeadm) - 集群创建工具。
- [Kubespray](https://github.com/kubernetes-sigs/kubespray) - Kubernetes 部署。

## 集群管理

- [Kubectl](https://github.com/kubernetes/kubectl) - CLI 工具。
- [Lens](https://github.com/lensapp/lens) - IDE。
- [Octant](https://github.com/vmware-archive/octant) - Web 控制台。
- [K9s](https://github.com/derailed/k9s) - 终端 UI。
- [Kubeshark](https://github.com/kubeshark/kubeshark) - API 流量分析。
- [OpenLens](https://github.com/MuhammedKalkan/OpenLens) - Lens 开源版。
- [KubeWeb](https://github.com/kubeweb/kubeweb) - Web UI。

## 监控

- [Prometheus](https://github.com/prometheus/prometheus) - 指标收集。
- [Grafana](https://github.com/grafana/grafana) - 仪表板。
- [Kube Prometheus Stack](https://github.com/prometheus-community/helm-charts) - 监控栈。
- [Grafana Loki](https://github.com/grafana/loki) - 日志聚合。
- [Jaeger](https://github.com/jaegertracing/jaeger) - 分布式追踪。
- [OpenTelemetry](https://github.com/open-telemetry/opentelemetry-operator) - 可观测性。
- [Kiali](https://github.com/kiali/kiali) - 服务网格 UI。
- [Metrics Server](https://github.com/kubernetes-sigs/metrics-server) - 资源指标。
- [Kured](https://github.com/kubereboot/kured) - 自动重启。

## 存储

- [Longhorn](https://github.com/longhorn/longhorn) - 分布式块存储。
- [Rook](https://github.com/rook/rook) - Ceph 存储编排。
- [OpenEBS](https://github.com/openebs/openebs) - 容器存储。
- [MinIO](https://github.com/minio/minio) - S3 兼容存储。
- [Ceph](https://github.com/ceph/ceph) - 分布式存储。
- [Kanister](https://github.com/kanisterio/kanister) - 备份恢复。

## 网络

- [Calico](https://github.com/projectcalico/calico) - 网络策略。
- [Cilium](https://github.com/cilium/cilium) - eBPF 网络。
- [Flannel](https://github.com/flannel-io/flannel) - 网络 CNI。
- [Weave](https://github.com/weaveworks/weave) - 网络 CNI。
- [MetalLB](https://github.com/metallb/metallb) - 负载均衡器。
- [Ingress Nginx](https://github.com/kubernetes/ingress-nginx) - Ingress 控制器。
- [Gateway API](https://github.com/kubernetes-sigs/gateway-api) - 网关 API。
- [Istio](https://github.com/istio/istio) - 服务网格。

## 安全

- [Kyverno](https://github.com/kyverno/kyverno) - 策略引擎。
- [OPA Gatekeeper](https://github.com/open-policy-agent/gatekeeper) - 策略控制器。
- [Falco](https://github.com/falcosecurity/falco) - 运行时安全。
- [Trivy](https://github.com/aquasecurity/trivy) - 漏洞扫描。
- [Cert Manager](https://github.com/cert-manager/cert-manager) - TLS 证书。
- [Vault](https://github.com/hashicorp/vault) - 密钥管理。
- [Sealed Secrets](https://github.com/bitnami-labs/sealed-secrets) - 加密 Secrets。
- [kube-bench](https://github.com/aquasecurity/kube-bench) - CIS 基准检查。
- [Kube Hunter](https://github.com/aquasecurity/kube-hunter) - 安全扫描。
- [kube-score](https://github.com/zegl/kube-score) - 配置检查。
- [Popeye](https://github.com/derailed/popeye) - 集群健康检查。

## CI/CD

- [Argo CD](https://github.com/argoproj/argo-cd) - GitOps CD。
- [Argo Workflows](https://github.com/argoproj/argo-workflows) - 工作流引擎。
- [Flux](https://github.com/fluxcd/flux2) - GitOps 工具。
- [Jenkins X](https://github.com/jenkins-x/jx) - CI/CD。
- [Tekton](https://github.com/tektoncd/pipeline) - CI/CD 框架。
- [Helm](https://github.com/helm/helm) - 包管理器。
- [Skaffold](https://github.com/GoogleContainerTools/skaffold) - 开发工具。
- [DevSpace](https://github.com/devspace-sh/devspace) - 开发流水线。

## 服务网格

- [Istio](https://github.com/istio/istio) - 服务网格。
- [Linkerd](https://github.com/linkerd/linkerd2) - 轻量服务网格。
- [Consul Connect](https://github.com/hashicorp/consul) - 服务网格。
- [Kuma](https://github.com/kumahq/kuma) - 服务网格。
- [Envoy](https://github.com/envoyproxy/envoy) - 代理。
- [OSM](https://github.com/openservicemesh/osm) - 开源服务网格。

## 机器学习

- [Kubeflow](https://github.com/kubeflow/kubeflow) - ML 平台。
- [Ray](https://github.com/ray-project/ray) - 分布式 AI。
- [Kserve](https://github.com/kserve/kserve) - ML 推理。

## 资源

- [Kubernetes 官方文档](https://kubernetes.io/docs/)
- [Kubernetes 博客](https://kubernetes.io/blog/)
- [Awesome Kubernetes 网站](https://ramitsurana.github.io/awesome-kubernetes/)
- [KubeWeekly](https://kubeweekly.io/) - 周刊。
- [Kubernetes Slack](https://slack.k8s.io/) - 社区 Slack。
- [Kubernetes on GitHub](https://github.com/kubernetes/kubernetes)
