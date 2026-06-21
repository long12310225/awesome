# 很棒的 Cloudflare [<img src="media/cf-logo.svg" width="250"align="right" alt="Cloudflare">](https://www.cloudflare.com) [![Awesome](https://awesome.re/badge-flat.svg)](https://awesome.re)

> 精彩的 [Cloudflare](https://www.cloudflare.com) 工作者食谱、开源项目、指南、博客和其他资源的精选列表。

Cloudflare 提供内容交付网络 (CDN) 服务、DDoS 缓解、互联网安全和分布式域名服务器 (DNS) 服务，位于访问者和 Cloudflare 用户的托管提供商之间，充当网站的反向代理。

## 内容

- [Community](#community)
- [Blog](#blog)
- [DNS](#dns)
- [Developers](#developers)
- [Apps](#apps)
  - [开源](#open-source)
- [Workers](#workers)
  - [Reference](#reference)
  - [Tools](#tools)
  - [Recipes](#recipes)
  - [AI](#ai)
- [Other](#other)

## 社区

- [Forum](https://community.cloudflare.com)
- [Reddit](https://www.reddit.com/r/CloudFlare)
- [Twitter 上的“@Cloudflare”](https://twitter.com/cloudflare)
- [Facebook](https://www.facebook.com/Cloudflare)
- [YouTube](https://www.youtube.com/cloudflare-)
- [GitHub](https://github.com/cloudflare)
- [GitHub 主题](https://github.com/topics/cloudflare)
- [堆栈交换](https://stackexchange.com/search?q=cloudflare)
- [堆栈溢出](https://stackoverflow.com/questions/tagged/cloudflare)
- [服务器故障](https://serverfault.com/questions/tagged/cloudflare)

## 博客

- [官方博客](https://blog.cloudflare.com)

## 域名系统

- [DNS Zone Files](https://github.com/irazasyed/dns-zone-files) - 准备导入通用配置区域文件，以便轻松配置各种服务。
- [Lexicon](https://github.com/AnalogJ/lexicon) - CLI 工具以标准化方式操作各种 DNS 提供商的 DNS 记录。
- [Th3inspector](https://github.com/Moham3dRiahi/Th3inspector) - 用于信息收集的多合一 CLI 工具。
- [Partner Panel](https://github.com/ZE3kr/Cloudflare-CNAME-Setup) - 托管合作伙伴为客户提供 DNS 管理面板的工具。
- [CFPMP](https://github.com/Netrvin/CFPMP) - 合作伙伴管理面板。
- [Flares](https://github.com/lfaoro/flares) - DNS备份工具。
- [Block Bad Bot Ruleset](https://github.com/SukkaW/cloudflare-block-bad-bot-ruleset) - 规则集的集合，用于使用防火墙规则阻止恶意爬虫。
- [Docker DDNS](https://github.com/oznu/docker-cloudflare-ddns) - Docker 镜像使用免费的 DNS 服务作为动态 DNS 提供商。
- [DDNS script for Synology](https://github.com/joshuaavalon/SynologyCloudflareDDNS) - Synology NAS 的 DDNS 脚本。
- [Dynamic DNS Bash](https://github.com/yulewang/cloudflare-api-v4-ddns) - bash 脚本中的动态 DNS 更新程序。
- [Dynamic DNS PHP](https://github.com/lyoshenka/cloudflare-ddns) - PHP 中的动态 DNS 更新器。
- [Dynamic DNS Python](https://github.com/adrienbrignon/cloudflare-ddns) - python 中的动态 DNS 更新器。
- [Multi-Provider DDNS Script](https://github.com/phuslu/ddns) - 多个提供商 ddns 脚本，无依赖关系。
- [Argo Tunnel Client](https://github.com/cloudflare/cloudflared) - Argo 隧道的 CLI 客户端，这是一个通过 Cloudflare 网络代理任何本地 Web 服务器的隧道守护进程。
- [Upper](https://github.com/ostark/upper) - 在网络服务器前面使用缓存代理可以显着加快工艺速度。
- [Cloud Buster](https://github.com/SageHack/cloud-buster) - 一个全面的渗透测试工具，用于检查站点是否存在源 IP 泄漏。
- [CLI Tool](https://github.com/danielpigott/cloudflare-cli) - 用于与 Cloudflare 交互的 CLI 工具。
- [Detector](https://github.com/k4m4/cloudflare-detect) - 检测站点是否在 Cloudflare 后面运行。
- [Scrape](https://github.com/Anorov/cloudflare-scrape) - 用于绕过反机器人页面的 Python 模块。
- [CloudFlair](https://github.com/christophetd/CloudFlair) - 用于查找受 CloudFlare 保护且公开暴露的网站的源服务器的工具。

## 开发商

- [Developers Hub](https://developers.cloudflare.com) - 开发人员文档，包括所有产品的 API 参考、文章和示例代码。
- [Open Source](https://cloudflare.github.io) - 官方开源项目。
- [API Docs](https://api.cloudflare.com) - API 文档。
- [Integration Resources](https://www.cloudflare.com/integrations) - 适用于内容管理系统、控制面板、云提供商、电子商务平台等的插件。
- [Technical Resources](https://www.cloudflare.com/technical-resources) - 技术工具和资源。
- [The Serverlist Newsletter](https://blog.cloudflare.com/serverlist) - serverlist 是 Cloudflare 策划的有关无服务器所有事物的时事通讯。

## 应用程序

> [Cloudflare Apps](https://www.cloudflare.com/apps/developers) 可让您将工具或服务发送到数百万个网站。任何 Cloudflare 客户都可以在几秒钟内预览并在其网站上安装您的代码。

- [应用程序目录](https://www.cloudflare.com/apps)
- [Documentation](https://www.cloudflare.com/apps/developer/docs/getting-started)
- [开发商基金](https://www.cloudflare.com/fund)
- [应用创意](https://github.com/cloudflare-apps/ideas)

### 开源

- [Official OSS Apps](https://github.com/cloudflare-apps) - 官方应用程序集合。
- [Logflare](https://github.com/Logflare/cloudflare-app) - 日志管理和事件分析。
- [OpWork.dev](https://github.com/hisorange/opwork) - 自托管 CloudFlare 员工管理平台。

## 工人

> [Cloudflare Workers](https://www.cloudflare.com/products/cloudflare-workers) 提供无服务器执行环境，允许您创建全新的应用程序或增强现有应用程序，而无需配置或维护基础设施。

### 参考

- [Documentation](https://workers.cloudflare.com/docs)
- [Tutorials](https://workers.cloudflare.com/docs/tutorials)
- [Runtime](https://workers.cloudflare.com/docs/reference/runtime)
- [工人KV](https://workers.cloudflare.com/docs/reference/storage)

### 工具

- [Wrangler](https://github.com/cloudflare/wrangler) - “wrangler” 是一个 CLI 工具，专为有兴趣使用 Cloudflare Worker 的人们而设计。
- [Playground](https://www.cloudflareworkers.com) - 直接在浏览器中针对任何站点预览和测试代码的简单、即时的方法。
- [Serverless Plugin](https://workers.cloudflare.com/docs/reference/tooling/serverless) - [无服务器框架](https://github.com/serverless/serverless) 的插件，用于使用 Workers 开发和部署无服务器应用程序。
- [Worker App Kit](https://github.com/postlight/cloudflare-worker-app-kit) - 用于创建、开发、测试和部署工作应用程序的便捷工具集。
- [GitHub Action](https://github.com/cpilsworth/cloudflare-worker-action) - 在推送到主分支时部署工作人员。
- [Workers KV Viewer](https://github.com/jroyal/cloudflare-workers-kv-viewer) - 基于 CLI 的交互式查看器，用于工作人员 KV 存储。
- [Redirect Management](https://forwarding.app) - 生成重定向工作人员。

### 食谱

- [Examples Collection](https://github.com/cloudflare/worker-examples) - 食谱集合。
- [Hello World JS Boilerplate](https://github.com/cloudflare/worker-template) - 用于在 JS 中启动工作项目的模板。
- [Hello World Rust Boilerplate](https://github.com/cloudflare/rustwasm-worker-template) - 使用 wasm-pack 启动工作项目的模板。
- [Router](https://github.com/cloudflare/worker-template-router) - 可与 REST API 或应用程序一起使用以实现基本路由逻辑的路由器。
- [Static](https://github.com/cloudflare/worker-template-static) - 从工作脚本中的原始字符串生成静态 HTML 或 JSON 页面。
- [Fetch](https://github.com/cloudflare/worker-template-fetch) - 发出 fetch 请求和生成 JSON post 请求的示例。
- [Incoming Request](https://github.com/ashleygwilliams/worker-template-requests) - 读取 JSON 类型和表单数据的 POST 请求正文的示例。
- [Redirect](https://github.com/cloudflare/worker-template-redirect) - 从 Worker 脚本发送单个和批量重定向的示例。
- [Img-Color](https://github.com/xtuc/img-color-worker) - 检索 png 或 jpeg 图像的主色。
- [Binast](https://github.com/xtuc/binast-cf-worker-template) - 通过工人为 binast 提供服务。
- [Pwnage Protection](https://github.com/detroitenglish/pw-pwnage-cfworker) - 安全密码评分和用户 pwnage 保护 api - [用法](https://community.cloudflare.com/t/estimate-strength-of-users-new-password-input-with-zxcvbn-and-query-haveibeenpwned-for-matches-against-known-hacked-accounts/26378)。
- [Cache Purger Proxy](https://gist.github.com/vdbelt/20f116236d2ebffa92f131e679c0551a) - 代理清除缓存请求 - [用法](https://community.cloudflare.com/t/worker-recipe-cache-purge-proxy/29978)。
- [URL Router](https://github.com/berstend/service-worker-router) - 快速 url 路由器 - [用法](https://community.cloudflare.com/t/open-source-fast-url-router-for-workers-js-typescript/33406)。
- [Edge Proxy](https://github.com/DigitalOptimizationGroup/cloudflare-edge-proxy) - 启用 A/B 测试、金丝雀发布、把关和 SEO A/B/N 测试。
- [Blue / Green Deployments](https://github.com/DigitalOptimizationGroup/blue-green-cloudflare-workers) - 使用金丝雀发布的蓝/绿部署的工作示例。
- [Preact PWA](https://github.com/DigitalOptimizationGroup/cloudflare-worker-preact-pwa) - Preact 渐进式 Web 应用程序。
- [CURL Interceptor](https://github.com/Gaafar/curl-worker) - 拦截来自“curl”命令的请求并返回不同的内容。
- [Worker with built-in Router](https://github.com/anderly/cloudflare-worker-routing) - 允许您将工作逻辑分成不同的功能和/或控制器。
- [Connecting to Google Storage](https://community.cloudflare.com/t/connecting-to-google-storage/32350) - 从 Google 云存储中提取文件。
- [CSRF Protection](https://gist.github.com/simonerni/3501b8de6320ac37398d08d9d2d08561) - 通过验证 origin/referer 标头来保护任何来源免受 CSRF 的影响。
- [URL Query Strings Parser](https://community.cloudflare.com/t/parse-url-query-strings-with-cloudflare-workers/90286) - 解析 url 查询字符串。
- [Regrex Replacement and Injection](https://community.cloudflare.com/t/perform-regex-replacements-and-inject-css-javascript-with-cloudflare-workers/90279) - 执行正则表达式替换并注入 CSS/JS。
- [Webpack Boilerplate](https://github.com/detroitenglish/cloudflare-workers-webpack-boilerplate) - 使用 webpack 构建、捆绑和部署工作人员的样板。
- [Basic Auth](https://github.com/dommmel/cloudflare-workers-basic-auth) - 使用基本身份验证进行保护。
- [Send Logs to Logdna](https://github.com/boynet/cf-logdna-worker) - 将日志发送到 logdna 的简单方法。
- [IP lookup service](https://github.com/matthewgall/beta.ipinfo.in) - 使用工作人员的 IP 查找服务。
- [Airtable Proxy](https://github.com/portable-cto/airtable-proxy-worker) - 允许您从前端向 Airtable API 发出安全请求。
- [TypeScript Workers](https://github.com/udacity/cloudflare-typescript-workers) - 用于构建经过测试的打字稿工作者的类型和模拟。
- [Proxies](https://github.com/GitbookIO/proxies-on-cloudflare) - 通过提供满足常见需求的高级代理原语，可以轻松构建工作程序。
- [Static Worker](https://github.com/manatarms/static-worker) - 提供可轻松托管静态网站的功能。
- [Bannero](https://github.com/nondanee/bannero) - 适用于简单桌面的 Bannero 图像 API。
- [Hasura](https://github.com/nathanwaters/hasura-cloudflare-worker) - 使用 hasura 的基于 Facebook 的授权和 graphql 代理查询的示例。
- [IP Redirects](https://community.cloudflare.com/t/ip-redirects/18285) - 根据用户的 IP 地址重定向用户。
- [Switch Image to WebP](https://github.com/vidaxl-com/cloudflare_webworkers/blob/master/examples/webp.js) - 如果支持，将图像重新路由到 webp。
- [Geographic Routing and Load Balancer](https://community.cloudflare.com/t/geographic-routing-and-load-balancing-with-cloudflare-workers/21900) - 地理路由和与工作人员的负载平衡。
- [UTM Tag Stripper](https://community.cloudflare.com/t/strip-utm-query-string/47941) - 去除查询字符串中的 UTM 标签。
- [Short URL Redirector](https://community.cloudflare.com/t/short-url-using-workers/39877) - 重定向短链接。
- [Repo Hunt](https://github.com/signalnerve/repo-hunt) - 每天寻找很酷的开源项目。
- [Performance Optimized Workers](https://github.com/pmeenan/cf-workers) - 工作脚本的集合，通常侧重于性能优化。
- [Google reCAPTCHA verification](https://github.com/HR/recaptcha-worker) - 处理 reCAPTCHA 表单的服务器端验证。
- [Cloudflare Workers Starter Kit](https://github.com/kriasoft/cloudflare-starter-kit) - - TypeScript 模板\w 多个 CF Worker、`*.env` 文件和本地测试。

### 人工智能

- [Moltworker](https://github.com/cloudflare/moltworker) - 在 Cloudflare Workers 上运行 Moltbot（以前称为 Clawdbot）。

## 其他

- [Support](https://support.cloudflare.com)
- [系统状态](https://www.cloudflarestatus.com)
- [网络地图](https://www.cloudflare.com/network)

## 贡献

欢迎投稿！首先阅读[贡献指南](contributing.md)。

## 许可证

[![CC0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0)

在法律允许的范围内，[Irfaq Syed](https://github.com/irazasyed) 已放弃所有版权和
本作品的相关或邻接权。

> Cloudflare 是 Cloudflare, Inc. 的注册商标。
