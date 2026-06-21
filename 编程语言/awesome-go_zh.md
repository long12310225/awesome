# 很棒的围棋

<a href="https://awesome-go.com/"><img align="right" src="https://github.com/avelino/awesome-go/raw/main/tmpl/assets/logo.png" alt="awesome-go" title="awesome-go" /></a>

[![Build Status](https://github.com/avelino/awesome-go/actions/workflows/tests.yaml/badge.svg?branch=main)](https://github.com/avelino/awesome-go/actions/workflows/tests.yaml?query=branch%3Amain)
[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
[![Slack Widget](https://img.shields.io/badge/join-us%20on%20slack-gray.svg?longCache=true&logo=slack&colorB=red)](https://gophers.slack.com/messages/awesome)
[![Netlify Status](https://api.netlify.com/api/v1/badges/83a6dcbe-0da6-433e-b586-f68109286bd5/deploy-status)](https://app.netlify.com/sites/awesome-go/deploys)
[![Track Awesome List](https://www.trackawesomelist.com/badge.svg)](https://www.trackawesomelist.com/avelino/awesome-go/)
[![Last Commit](https://img.shields.io/github/last-commit/avelino/awesome-go)](https://github.com/avelino/awesome-go/commits/main)

We use the _[Golang Bridge](https://github.com/gobridge/about-us/blob/master/README.md)_ community Slack for instant communication, follow the [form here to join](https://invite.slack.golangbridge.org/).

<a href="https://www.producthunt.com/posts/awesome-go?utm_source=badge-featured&utm_medium=badge&utm_souce=badge-awesome-go" target="_blank"><img src="https://api.producthunt.com/widgets/embed-image/v1/featured.svg?post_id=291535&theme=light" alt="awesome-go - Curated list awesome Go frameworks, libraries and software | Product Hunt" style="width: 250px; height: 54px;" width="250" height="54" /></a>

**Sponsorships:**

_Special thanks to_

<div align="center">
<table cellpadding="5">
<tbody align="center">
<tr>
<td colspan="2">
<a href="https://bit.ly/awesome-go-digitalocean">
<img src="https://avelino.run/sponsors/do_logo_horizontal_blue-210.png" width="200" alt="Digital Ocean">
</a>
</td>
</tr>
</tbody>
</table>
</div>

**Awesome Go 没有月费**_，但我们有员工**努力**以保持其运行。用筹集到的善款来回报每一位参与者的努力！您可以看到我们如何计算计费和分配，因为它向整个社区开放。想成为该项目的支持者请点击[此处](mailto:avelinorun+oss@gmail.com?subject=awesome-go%3A%20project%20support)._

> 精选的精彩 Go 框架、库和软件列表。受到 [awesome-python](https://github.com/vinta/awesome-python) 的启发。

**贡献：**

请先快速浏览一下[贡献指南](https://github.com/avelino/awesome-go/blob/main/CONTRIBUTING.md)。感谢所有[贡献者](https://github.com/avelino/awesome-go/graphs/contributors)；你摇滚！

> _如果您在此处看到不再维护或不合适的包或项目，请提交拉取请求以改进此文件。谢谢！_

## 内容

<详情>
<summary>展开内容</summary>

- [很棒的围棋](#awesome-go)
  - [Contents](#contents)
  - [演员模型](#actor-model)
  - [人工智能](#artificial-intelligence)
  - [音频和音乐](#audio-and-music)
  - [认证与授权](#authentication-and-authorization)
  - [Blockchain](#blockchain)
  - [机器人建设](#bot-building)
  - [构建自动化](#build-automation)
  - [命令行](#command-line)
    - [高级控制台 UI](#advanced-console-uis)
    - [标准CLI](#standard-cli)
  - [Configuration](#configuration)
  - [持续集成](#continuous-integration)
  - [CSS 预处理器](#css-preprocessors)
  - [数据集成框架](#data-integration-frameworks)
  - [数据结构和算法](#data-structures-and-algorithms)
    - [位打包和压缩](#bit-packing-and-compression)
    - [钻头组](#bit-sets)
    - [布卢姆和布谷鸟过滤器](#bloom-and-cuckoo-filters)
    - [数据结构与算法合集](#data-structure-and-algorithm-collections)
    - [Iterators](#iterators)
    - [Maps](#maps)
    - [各种数据结构和算法](#miscellaneous-data-structures-and-algorithms)
    - [可空类型](#nullable-types)
    - [Queues](#queues)
    - [Sets](#sets)
    - [文本分析](#text-analysis)
    - [Trees](#trees)
    - [Pipes](#pipes)
  - [Database](#database)
    - [Caches](#caches)
    - [用 Go 实现的数据库](#databases-implemented-in-go)
    - [数据库架构迁移](#database-schema-migration)
    - [数据库工具](#database-tools)
    - [SQL 查询生成器](#sql-query-builders)
  - [数据库驱动程序](#database-drivers)
    - [与多个后端的接口](#interfaces-to-multiple-backends)
    - [关系数据库驱动程序](#relational-database-drivers)
    - [NoSQL 数据库驱动程序](#nosql-database-drivers)
    - [搜索和分析数据库](#search-and-analytic-databases)
  - [日期和时间](#date-and-time)
  - [分布式系统](#distributed-systems)
  - [动态域名解析](#dynamic-dns)
  - [Email](#email)
  - [嵌入式脚本语言](#embeddable-scripting-languages)
  - [错误处理](#error-handling)
  - [文件处理](#file-handling)
  - [Financial](#financial)
  - [Forms](#forms)
  - [Functional](#functional)
  - [游戏开发](#game-development)
  - [Generators](#generators)
  - [Geographic](#geographic)
  - [Go编译器](#go-compilers)
  - [Goroutines](#goroutines)
  - [GUI](#gui)
  - [Hardware](#hardware)
  - [Images](#images)
  - [物联网（IoT）](#iot-internet-of-things)
  - [作业调度程序](#job-scheduler)
  - [JSON](#json)
  - [Logging](#logging)
  - [机器学习](#machine-learning)
  - [Messaging](#messaging)
  - [微软办公软件](#microsoft-office)
    - [微软Excel](#microsoft-excel)
    - [微软Word](#microsoft-word)
  - [Miscellaneous](#miscellaneous)
    - [依赖注入](#dependency-injection)
    - [项目布局](#project-layout)
    - [Strings](#strings)
    - [Uncategorized](#uncategorized)
  - [自然语言处理](#natural-language-processing)
    - [语言检测](#language-detection)
    - [形态分析仪](#morphological-analyzers)
    - [Slugifiers](#slugifiers)
    - [Tokenizers](#tokenizers)
    - [Translation](#translation)
    - [Transliteration](#transliteration)
  - [Networking](#networking)
    - [HTTP 客户端](#http-clients)
  - [OpenGL](#opengl)
  - [ORM](#orm)
  - [包管理](#package-management)
  - [Performance](#performance)
  - [查询语言](#query-language)
  - [Reflection](#reflection)
  - [资源嵌入](#resource-embedding)
  - [科学与数据分析](#science-and-data-analysis)
  - [Security](#security)
  - [Serialization](#serialization)
  - [服务器应用程序](#server-applications)
  - [流处理](#stream-processing)
  - [模板引擎](#template-engines)
  - [Testing](#testing)
    - [测试框架](#testing-frameworks)
    - [Mock](#mock)
    - [模糊测试和增量调试/减少/收缩](#fuzzing-and-delta-debuggingreducingshrinking)
    - [Selenium 和浏览器控制工具](#selenium-and-browser-control-tools)
    - [注入失败](#fail-injection)
  - [文本处理](#text-processing)
    - [Formatters](#formatters)
    - [标记语言](#markup-languages)
    - [Parsers/Encoders/Decoders](#parsersencodersdecoders)
    - [正则表达式](#regular-expressions)
    - [Sanitation](#sanitation)
    - [Scrapers](#scrapers)
    - [RSS](#rss)
    - [Utility/Miscellaneous](#utilitymiscellaneous)
  - [第三方API](#third-party-apis)
  - [Utilities](#utilities)
  - [UUID](#uuid)
  - [Validation](#validation)
  - [版本控制](#version-control)
  - [Video](#video)
  - [网络框架](#web-frameworks)
    - [Middlewares](#middlewares)
      - [实际的中间件](#actual-middlewares)
      - [用于创建 HTTP 中间件的库](#libraries-for-creating-http-middlewares)
    - [Routers](#routers)
  - [WebAssembly](#webassembly)
  - [Webhooks 服务器](#webhooks-server)
  - [Windows](#windows)
  - [工作流程框架](#workflow-frameworks)
  - [XML](#xml)
  - [零信任](#zero-trust)
  - [代码分析](#code-analysis)
  - [编辑器插件](#editor-plugins)
  - [去生成工具](#go-generate-tools)
  - [去工具](#go-tools)
  - [软件包](#software-packages)
    - [开发运营工具](#devops-tools)
    - [其他软件](#other-software)
- [Resources](#resources)
  - [Benchmarks](#benchmarks)
  - [Conferences](#conferences)
  - [E-Books](#e-books)
    - [可供购买的电子书](#e-books-for-purchase)
    - [免费电子书](#free-e-books)
  - [Gophers](#gophers)
  - [Meetups](#meetups)
  - [风格指南](#style-guides)
  - [社交媒体](#social-media)
    - [Twitter](#twitter)
    - [Reddit](#reddit)
  - [Websites](#websites)
    - [Tutorials](#tutorials)
    - [引导式学习](#guided-learning)
  - [Contribution](#contribution)
  - [License](#license)

**[⬆ 回到顶部](#contents)**



</详情>

## 演员模型

_用于构建基于参与者的程序的库._

- [asyncmachine-go/pkg/machine](https://github.com/pancsta/asyncmachine-go/tree/main/pkg/machine) - 图形控制流库（AOP、参与者、状态机）。
- [Ergo](https://github.com/ergo-services/ergo) - 具有网络透明度的基于参与者的框架，用于在 Golang 中创建事件驱动的架构。受到 Erlang 的启发。
- [Goakt](https://github.com/Tochemey/goakt) - 使用协议缓冲区作为 Golang 消息的快速分布式 Actor 框架。
- [Hollywood](https://github.com/anthdm/hollywood) - 用 Golang 编写的极快且轻量级的 Actor 引擎。
- [ProtoActor](https://github.com/asynkron/protoactor-go) - Go、C# 和 Java/Kotlin 的分布式参与者。

**[⬆ 回到顶部](#contents)**

## 人工智能

_用于构建利用人工智能的程序的库。_

- [AegisFlow](https://github.com/saivedant169/AegisFlow) - AI 网关，用于路由、保护和监控 10 多个提供商之间的 LLM 流量。兼容 OpenAI 的 API、WASM 策略插件、金丝雀部署、实时仪表板。
- [Aetheris](https://github.com/Colin4k1024/Aetheris) - AI Agent 执行运行时具有事件源、检查点恢复和最多一次执行保证。用 Go 编写。
- [agent-sdk-go](https://github.com/agenticenv/agent-sdk-go) - Go SDK，用于在 Temporal 上构建持久的 AI 代理，支持工具、MCP、人工批准和子代理委托。
- [ai](https://github.com/joakimcarlsson/ai) - 一个 Go 工具包，用于跨多个提供商构建 AI 代理和应用程序，具有统一的 LLM、嵌入、工具调用和 MCP 集成。
- [chromem-go](https://github.com/philippgille/chromem-go) - 用于 Go 的嵌入式矢量数据库，具有类似 Chroma 的界面和零第三方依赖性。内存中，具有可选的持久性。
- [dakera-go](https://github.com/dakera-ai/dakera-go) - Dakera 自托管代理内存服务器的官方 Go 客户端 SDK，提供用于内存存储/调用、会话管理、命名空间操作和衰减配置的类型化接口。
- [fun](https://gitlab.com/tozd/go/fun) - 在 Go 中使用大型语言模型 (LLM) 的最简单但功能强大的方法。
- [goai](https://github.com/zendev-sh/goai) - 用于构建 AI 应用程序的 Go SDK。一个 SDK，20 多个提供商。受到 Vercel AI SDK 的启发。
- [hotplex](https://github.com/hrygo/hotplex) - AI Agent 运行时引擎，具有适用于 Claude Code、OpenCode、pi-mono 和其他 CLI AI 工具的长期会话。提供全双工流媒体、多平台集成和安全沙箱。
- [langchaingo](https://github.com/tmc/langchaingo) - LangChainGo 是一个用于开发由语言模型支持的应用程序的框架。
- [langgraphgo](https://github.com/smallnest/langgraphgo) - 一个用于使用 LLM 构建有状态、多参与者应用程序的 Go 库，基于 LangGraph 的概念构建，具有许多内置的 Agent 架构。
- [LocalAI](https://github.com/mudler/LocalAI) - 开源 OpenAI 替代方案，自托管 AI 模型。
- [localaik](https://github.com/harshaneel/localaik) - OpenAI 和 Gemini API 的 LocalStack 式本地模拟；单个 Docker 容器，llama.cpp + Gemma 3 后端。
- [mcp-go](https://github.com/mark3labs/mcp-go) - 模型上下文协议的 Go 实现，用于在 Go 中构建 MCP 服务器和客户端。
- [Ollama](https://github.com/jmorganca/ollama) - 在本地运行大型语言模型。
- [OllamaFarm](https://github.com/presbrey/ollamafarm) - 管理、负载平衡和故障转移 Ollamas 包。
- [otellix](https://github.com/oluwajubelo1/otellix) - OpenTelemetry 原生 LLM 可观察性和预算护栏，适用于成本受限的生产环境。
- [routex](https://github.com/Ad3bay0c/routex) - YAML 驱动的 Go 多代理 AI 运行时，具有 Erlang 风格的监督、MCP 工具服务器支持和 CLI。
- [trpc-agent-go](https://github.com/trpc-group/trpc-agent-go) - 用于构建基于 LLM 的多代理系统的框架。
- [web-researcher-mcp](https://github.com/zoharbabin/web-researcher-mcp) - MCP 服务器为 AI 助手提供网络搜索、内容提取和多源研究功能。单个二进制、5 个具有断路器故障转移功能的搜索提供程序、4 层抓取管道。
- [zenflow](https://github.com/zendev-sh/zenflow) - 多代理编排和工作流引擎。声明式 YAML 工作流程、具有中心辐射型邮箱的 LLM 协调员、安全交付。一个 YAML 文件，一个 Go 二进制文件。可在任何 goai 支持的提供商上运行。

**[⬆ 回到顶部](#contents)**

## 音频和音乐

_用于操作音频和音乐的库。_

- [beep](https://github.com/gopxl/beep) - 用于播放和音频操作的简单库。
- [flac](https://github.com/mewkiz/flac) - Native Go FLAC 编码器/解码器，支持 FLAC 流。
- [gaad](https://github.com/Comcast/gaad) - Native Go AAC 比特流解析器。
- [go-mpris](https://github.com/leberKleber/go-mpris) - mpris dbus 接口的客户端。
- [GoAudio](https://github.com/DylanMeeus/GoAudio) - Native Go 音频处理库。
- [gosamplerate](https://github.com/dh1tw/gosamplerate) - go 的 libsamplerate 绑定。
- [id3v2](https://github.com/bogem/id3v2) - Go 的 ID3 解码和编码库。
- [malgo](https://github.com/gen2brain/malgo) - 迷你音频库。
- [minimp3](https://github.com/tosone/minimp3) - 轻量级 MP3 解码器库。
- [music-theory](https://github.com/go-music-theory/music-theory) - Go 中的音乐理论模型。
- [Oto](https://github.com/hajimehoshi/oto) - 用于在多个平台上播放声音的低级库。
- [PortAudio](https://github.com/gordonklaus/portaudio) - Go 绑定 PortAudio 音频 I/O 库。
-[voxrai-ai](https://github.com/Voxray-AI/Voxray) - 具有 JSON 配置的 AI 语音代理，通过 WebSocket 和 WebRTC 的 STT → LLM → TTS 管道

**[⬆ 回到顶部](#contents)**

## 认证与授权

_用于实现身份验证和授权的库._

- [authboss](https://github.com/volatiletech/authboss) - 用于网络的模块化身份验证系统。它尝试删除尽可能多的样板文件和“困难的东西”，以便每次您在 Go 中启动一个新的 Web 项目时，您都可以插入它、配置它并开始构建您的应用程序，而无需每次都构建身份验证系统。
- [authgate](https://github.com/go-authgate/authgate) - 轻量级 OAuth 2.0 授权服务器，支持设备授权授予 ([RFC 8628](https://datatracker.ietf.org/doc/html/rfc8628))、使用 PKCE 的授权代码流 ([RFC 6749](https://datatracker.ietf.org/doc/html/rfc6749) + [RFC 7636](https://datatracker.ietf.org/doc/html/rfc7636))，以及用于机器对机器身份验证的客户端凭据授予。
- [branca](https://github.com/essentialkaos/branca) - 适用于 Golang 1.15+ 的 branca 代币 [规范实现](https://github.com/tuupola/branca-spec)。
- [casbin](https://github.com/hsluoyz/casbin) - 支持 ACL、RBAC 和 ABAC 等访问控制模型的授权库。
- [cookiestxt](https://github.com/mengzhuo/cookiestxt) - 提供cookies.txt文件格式的解析器。
- [go-githubauth](https://github.com/jferrl/go-githubauth) - 用于 GitHub 身份验证的实用程序：生成并使用 GitHub 应用程序和安装令牌。
- [go-guardian](https://github.com/shaj13/go-guardian) - Go-Guardian 是一个 golang 库，它提供了一种简单、干净且惯用的方式来创建强大的现代 API 和 Web 身份验证，支持 LDAP、Basic、Bearer token 和基于证书的身份验证。
- [go-iam](https://github.com/melvinodsa/go-iam) - 具有简单 UI 的开发人员优先身份和访问管理系统。
- [go-jose](https://github.com/go-jose/go-jose) - 相当完整地实现了 JOSE 工作组的 JSON Web 令牌、JSON Web 签名和 JSON Web 加密规范。
- [go-jwt](https://github.com/deatil/go-jwt) - Go 的 JWT（JSON Web 令牌）库。
- [go-jwt](https://github.com/pardnchiu/go-jwt) - JWT 身份验证包提供访问令牌和刷新令牌以及指纹识别、Redis 存储和自动刷新功能。
- [goiabada](https://github.com/leodip/goiabada) - 支持 OAuth2 和 OpenID Connect 的开源身份验证和授权服务器。
- [gologin](https://github.com/dghubble/gologin) - 用于使用 OAuth1 和 OAuth2 身份验证提供程序登录的可链接处理程序。
- [gorbac](https://github.com/mikespook/gorbac) - 在 Golang 中提供轻量级的基于角色的访问控制 (RBAC) 实现。
- [gosession](https://github.com/Kwynto/gosession) - 这是 GoLang 中 net/http 的快速会话。这个包也许是会话机制的最佳实现，或者至少它试图成为其中之一。
- [goth](https://github.com/markbates/goth) - 提供了一种简单、干净且惯用的方式来使用 OAuth 和 OAuth2。开箱即用地处理多个提供商。
- [jeff](https://github.com/abraithwaite/jeff) - 具有可插拔后端的简单、灵活、安全且惯用的 Web 会话管理。
- [jwt](https://github.com/pascaldekloe/jwt) - 轻量级 JSON Web 令牌 (JWT) 库。
- [jwt](https://github.com/cristalhq/jwt) - 适用于 Go 的安全、简单且快速的 JSON Web 令牌。
- [jwt-auth](https://github.com/adam-hanna/jwt-auth) - 用于 Golang http 服务器的 JWT 中间件，具有许多配置选项。
- [jwt-go](https://github.com/golang-jwt/jwt) - JSON Web Tokens (JWT) 的全功能实现。该库支持 JWT 的解析和验证以及生成和签名。
- [jwx](https://github.com/lestrrat-go/jwx) - Go 模块实现了各种 JWx（JWA/JWE/JWK/JWS/JWT，也称为 JOSE）技术。
- [keto](https://github.com/ory/keto) - “Zanzibar：Google 一致的全球授权系统”的开源 (Go) 实现。提供 gRPC、REST API、newSQL 以及简单且精细的权限语言。支持ACL、RBAC等多种访问模型。
- [loginsrv](https://github.com/tarent/loginsrv) - 具有可插入后端的 JWT 登录微服务，例如 OAuth2 (Github)、htpasswd、osiam。
- [oauth2](https://github.com/golang/oauth2) - goauth2 的继承者。通用 OAuth 2.0 包，附带 JWT、Google API、Compute Engine 和 App Engine 支持。
- [oidc](https://github.com/zitadel/oidc) - 易于使用的 OpenID Connect 客户端和服务器库，为 Go 编写，并经过 OpenID 基金会认证。
- [openfga](https://github.com/openfga/openfga) - 基于《Zanzibar: Google's Concrete, Global Authorization System》论文实现细粒度授权。由 [CNCF](https://www.cncf.io/) 支持。
- [osin](https://github.com/openshift/osin) - Golang OAuth2 服务器库。
- [otpgen](https://github.com/grijul/otpgen) - 用于生成 TOTP/HOTP 代码的库。
- [otpgo](https://github.com/jltorresm/otpgo) - 用于 Go 的基于时间的一次性密码 (TOTP) 和基于 HMAC 的一次性密码 (HOTP) 库。
- [paseto](https://github.com/o1egl/paseto) - 与平台无关的安全令牌 (PASETO) 的 Golang 实现。
- [permissions](https://github.com/xyproto/permissions) - 用于跟踪用户、登录状态和权限的库。使用安全 cookie 和 bcrypt。
- [scope](https://github.com/SonicRoshan/scope) - 在 Go 中轻松管理 OAuth2 范围。
- [scs](https://github.com/alexedwards/scs) - HTTP 服务器的会话管理器。
- [securecookie](https://github.com/chmike/securecookie) - 高效安全的 cookie 编码/解码。
- [session](https://github.com/icza/session) - Web 服务器的 Go 会话管理（包括对 Google App Engine - GAE 的支持）。
- [sessions](https://github.com/adam-hanna/sessions) - 用于 go http 服务器的极其简单、高性能、高度可定制的会话服务。
- [sessionup](https://github.com/swithek/sessionup) - 简单而有效的 HTTP 会话管理和识别包。
- [sjwt](https://github.com/brianvoe/sjwt) - 简单的 jwt 生成器和解析器。
- [spicedb](https://github.com/authzed/spicedb) - 受桑给巴尔启发的数据库，可实现细粒度授权。
- [x509proxy](https://github.com/vkuznet/x509proxy) - 用于处理 X509 代理证书的库。

**[⬆ 回到顶部](#contents)**

## 区块链

_构建区块链的工具._

- [cometbft](https://github.com/cometbft/cometbft) - 分布式、拜占庭容错、确定性状态机复制引擎。它是 Tendermint Core 的一个分支，并实现了 Tendermint 共识算法。
- [cosmos-sdk](https://github.com/cosmos/cosmos-sdk) - 在 Cosmos 生态系统中构建公共区块链的框架。
- [gno](https://github.com/gnolang/gno) - 使用 Golang 和 Gnolang 构建的综合智能合约套件，Gnolang 是一种确定性的、专门为区块链构建的 Go 变体。
- [go-ethereum](https://github.com/ethereum/go-ethereum) - 以太坊协议的官方 Go 实现。
- [gosemble](https://github.com/LimeChain/gosemble) - 一个基于 Go 的框架，用于构建 Polkadot/Substrate 兼容的运行时。
- [gossamer](https://github.com/ChainSafe/gossamer) - Polkadot Host 的 Go 实现。
- [kubo](https://github.com/ipfs/kubo) - Go 中的 IPFS 实现。它提供内容可寻址存储，可用于 DApp 中的去中心化存储。它基于 IPFS 协议。
- [lnd](https://github.com/lightningnetwork/lnd) - 闪电网络节点的完整实现。
- [nview](https://github.com/blinklabs-io/nview) - 卡尔达诺节点的本地监控工具。它是一个 TUI（终端用户界面），旨在适合大多数屏幕。
- [solana-go](https://github.com/gagliardetto/solana-go) - Go 库与 Solana JSON RPC 和 WebSocket 接口进行交互。
- [tendermint](https://github.com/tendermint/tendermint) - 高性能中间件，用于使用 Tendermint 共识和区块链协议将用任何编程语言编写的状态机转换为拜占庭容错复制状态机。
- [tronlib](https://github.com/kslamph/tronlib) - 一个全面的、可立即投入生产的 Go SDK，用于通过 TRC20 代币支持与 TRON 区块链进行交互。

**[⬆ 回到顶部](#contents)**

## 机器人建设

_用于构建和使用机器人的库。_

- [arikawa](https://github.com/diamondburned/arikawa) - Discord API 的库和框架。
- [bot](https://github.com/go-telegram/bot) - 具有附加 UI 组件的零依赖 Telegram Bot 库。
- [echotron](https://github.com/NicoNex/echotron) - Go 中 Telegram 机器人的优雅并发库。
- [go-joe](https://joe-bot.net) - 受 Hubot 启发但用 Go 编写的通用机器人库。
- [go-sarah](https://github.com/oklahomer/go-sarah) - 用于为所需的聊天服务（包括 LINE、Slack、Gitter 等）构建机器人的框架。
- [go-tg](https://github.com/mr-linch/go-tg) - 由官方文档生成用于访问 Telegram Bot API 的 Go 客户端库，其中包含用于构建复杂机器人的电池。
- [go-twitch-irc](https://github.com/gempir/go-twitch-irc) - 为 twitch.tv 聊天编写机器人的库
- [micha](https://github.com/onrik/micha) - Telegram bot api 的 Go 库。
- [slack-bot](https://github.com/innogames/slack-bot) - 为懒惰的开发人员准备好使用 Slack Bot：自定义命令、Jenkins、Jira、Bitbucket、Github...
- [slacker](https://github.com/slack-io/slacker) - 易于使用的框架来创建 Slack 机器人。
- [telebot](https://github.com/tucnak/telebot) - Telegram 机器人框架是用 Go 编写的。
- [telego](https://github.com/mymmrac/telego) - 适用于 Golang 的 Telegram Bot API 库，具有完整的一对一 API 实现。
- [telegram-bot-api](https://github.com/go-telegram-bot-api/telegram-bot-api) - 简单干净的 Telegram 机器人客户端。
- [TG](https://github.com/enetx/tg) - Go 的 Telegram Bot 框架。
- [wayback](https://github.com/wabarc/wayback) - Telegram、Mastodon、Slack 和其他消息平台的机器人可以存档网页。
- [ymsdk](https://github.com/rekurt/ymsdk) - 适用于 Yandex Messenger Bot API 的 Go SDK，具有类型安全模型、自动重试和速率限制处理。
   - [Wisp](https://github.com/wisp-trading/wisp) - Go 的事件驱动交易框架。现货、永续期货、预测市场。多交易所（Bybit、Hyperliquid、Polymarket）。

**[⬆ 回到顶部](#contents)**

## 构建自动化

_库和工具有助于构建自动化。_

- [1build](https://github.com/gopinath-langote/1build) - 命令行工具可轻松管理特定于项目的命令。
- [air](https://github.com/cosmtrek/air) - Air - Go 应用程序的实时重新加载。
- [anko](https://github.com/GuilhermeCaruso/anko) - 适用于多种编程语言的简单应用程序观察器。
- [gaper](https://github.com/maxclaus/gaper) - 当 Go 项目崩溃或某些监视的文件发生更改时，构建并重新启动该项目。
- [gilbert](https://go-gilbert.github.io) - 为 Go 项目构建系统和任务运行程序。
- [gob](https://github.com/kcmvp/gob) - [Gradle](https://docs.gradle.org/)/[Maven](https://maven.apache.org/) 类似 Go 项目的构建工具。
- [goyek](https://github.com/goyek/goyek) - 在 Go 中创建构建管道。
- [mage](https://github.com/magefile/mage) - Mage 是一个使用 Go 的类似 make/rake 的构建工具。
- [mmake](https://github.com/tj/mmake) - 现代制造。
- [realize](https://github.com/tockins/realize) - 去构建一个带有文件观察器的系统并实时重新加载。使用自定义路径运行、构建和监视文件更改。
- [rex](https://github.com/rexrun-dev/rex) - 零配置通用项目运行程序。检测您的堆栈（Go、Node、Python、Rust、PHP、Zig、Elixir）并运行正确的命令。
- [Task](https://github.com/go-task/task) - 简单的“制作”替代方案。
- [taskctl](https://github.com/taskctl/taskctl) - 并发任务运行程序。
- [xc](https://github.com/joerdav/xc) - 带有 README.md 定义任务的任务运行器，可执行 markdown。

**[⬆ 回到顶部](#contents)**

## 命令行

### 高级控制台 UI

_用于构建控制台应用程序和控制台用户界面的库._

- [asciigraph](https://github.com/guptarohit/asciigraph) - Go 包可在命令行应用程序中制作轻量级 ASCII 线图╭┈╯，无需其他依赖项。
- [aurora](https://github.com/logrusorgru/aurora) - 支持 fmt.Printf/Sprintf 的 ANSI 终端颜色。
- [box-cli-maker](https://github.com/box-cli-maker/box-cli-maker) - 在终端中渲染高度可定制的框。
- [bubble-table](https://github.com/Evertras/bubble-table) - 泡泡茶的交互式表格组件。
- [bubbles](https://github.com/charmbracelet/bubbles) - 用于泡茶的 TUI 组件。
- [bubbletea](https://github.com/charmbracelet/bubbletea) - 基于 Elm 架构的 Go 框架用于构建终端应用程序。
- [chroma16](https://github.com/arceus-7/chroma16) - 从单一种子颜色或字符串生成和谐的 16 色终端调色板。
- [crab-config-files-templating](https://github.com/alfiankan/crab-config-files-templating) - 用于 kubernetes 清单或通用配置文件的动态配置文件模板工具。
- [ctc](https://github.com/wzshiming/ctc) - 非侵入式跨平台终端颜色库不需要修改Print方法。
- [fx](https://github.com/antonmedv/fx) - 终端 JSON 查看器和处理器。
- [go-ataman](https://github.com/workanator/go-ataman) - 用于在终端中渲染 ANSI 彩色文本模板的 Go 库。
- [go-colorable](https://github.com/mattn/go-colorable) - 适用于 Windows 的可着色书写器。
- [go-colortext](https://github.com/daviddengcn/go-colortext) - 用于终端中颜色输出的 Go 库。
- [go-isatty](https://github.com/mattn/go-isatty) - golang 的 isatty。
- [go-palette](https://github.com/abusomani/go-palette) - Go 库使用 ANSI 颜色提供优雅且方便的样式定义。完全兼容并包装 [fmt 库](https://pkg.go.dev/fmt) 以实现漂亮的终端布局。
- [go-prompt](https://github.com/c-bata/go-prompt) - 用于构建强大的交互式提示的库，受到 [python-prompt-toolkit](https://github.com/jonathanslenders/python-prompt-toolkit) 的启发。
- [gocui](https://github.com/jroimartin/gocui) - Minimalist Go 库旨在创建控制台用户界面。
- [gommon/color](https://github.com/labstack/gommon/tree/master/color) - 样式终端文本。
- [gookit/color](https://github.com/gookit/color) - 终端显色工具库，支持16色、256色、RGB显色输出，兼容Windows。
- [lazyenv](https://github.com/lazynop/lazyenv) - 用于浏览、比较和编辑 .env 文件的 TUI。
- [lipgloss](https://github.com/charmbracelet/lipgloss) - 在终端中以声明方式定义颜色、格式和布局的样式。
- [loom](https://github.com/loom-go/loom) - 用于构建 TUI 的基于信号的反应组件框架。
- [marker](https://github.com/cyucelen/marker) - 匹配和标记彩色终端输出字符串的最简单方法。
- [mpb](https://github.com/vbauerster/mpb) - 终端应用程序的多进度条。
- [phoenix](https://github.com/phoenix-tui/phoenix) - 高性能 TUI 框架，具有 Elm 启发架构、完美的 Unicode 渲染和零分配事件系统。
- [progressbar](https://github.com/schollz/progressbar) - 适用于每个操作系统的基本线程安全进度条。
- [pterm](https://github.com/pterm/pterm) - 一个库，用于通过许多可组合的组件来美化每个平台上的控制台输出。
- [simpletable](https://github.com/alexeyco/simpletable) - 使用 Go 的终端中的简单表格。
- [spinner](https://github.com/briandowns/spinner) - Go 包可以轻松地为终端微调器提供选项。
- [tabby](https://github.com/cheynewallace/tabby) - 一个包含超级简单 Golang 表的小型库。
- [table](https://github.com/tomlazar/table) - 用于基于终端颜色的表格的小型库。
- [termbox-go](https://github.com/nsf/termbox-go) - Termbox 是一个用于创建跨平台基于文本的界面的库。
- [termdash](https://github.com/mum4k/termdash) - Go 终端仪表板基于 **termbox-go** 并受到 [termui](https://github.com/gizak/termui) 的启发。
- [termenv](https://github.com/muesli/termenv) - 为您的终端应用程序提供高级 ANSI 样式和颜色支持。
- [termui](https://github.com/gizak/termui) - Go 终端仪表板基于 **termbox-go** 并受到 [blessed-contrib](https://github.com/yaronn/blessed-contrib) 的启发。
- [uilive](https://github.com/gosuri/uilive) - 用于实时更新终端输出的库。
- [uiprogress](https://github.com/gosuri/uiprogress) - 用于在终端应用程序中渲染进度条的灵活库。
- [uitable](https://github.com/gosuri/uitable) - 使用表格数据提高终端应用程序可读性的库。
- [yacspin](https://github.com/theckman/yacspin) - 另一个 CLi Spinner 包，用于与终端微调器一起使用。
- [goscaf](https://github.com/iyashjayesh/goscaf) - goscaf 通过交互式 CLI 生成固执己见的、生产质量的 Go 项目样板。停止在项目之间复制粘贴骨架代码。

**[⬆ 回到顶部](#contents)**

### 标准CLI

_用于构建标准或基本命令行应用程序的库。_

- [acmd](https://github.com/cristalhq/acmd) - Go 中的简单、有用且固执己见的 CLI 包。
- [argparse](https://github.com/akamensky/argparse) - 受 Python argparse 模块启发的命令行参数解析器。
- [argv](https://github.com/cosiner/argv) - Go 库使用 bash 语法将命令行字符串拆分为参数数组。
- [boa](https://github.com/GiGurra/boa) - 结构标记中的声明性标志、环境变量、验证和配置文件。建立在眼镜蛇之上。
- [carapace](https://github.com/rsteube/carapace) - spf13/cobra 的命令参数完成生成器。
- [carapace-bin](https://github.com/rsteube/carapace-bin) - 多 shell 多命令参数完成器。
- [carapace-spec](https://github.com/rsteube/carapace-spec) - 使用规范文件定义简单的完成。
- [climax](https://github.com/tucnak/climax) - 具有“人性化面孔”的替代 CLI，本着 Go 命令的精神。
- [clîr](https://github.com/leaanthony/clir) - 一个简单明了的 CLI 库。无依赖性。
- [cmd](https://github.com/posener/cmd) - 扩展标准“flag”包以惯用的方式支持子命令等。
- [cmdr](https://github.com/hedzr/cmdr) - POSIX/GNU 风格、类似 getopt 的命令行 UI Go 库。
- [cobra](https://github.com/spf13/cobra) - 现代 Go CLI 交互的指挥官。
- [command-chain](https://github.com/rainu/go-command-chain) - 用于配置和运行命令链的 go 库 - 例如 UNIX shell 中的管道。
- [commandeer](https://github.com/jaffee/commandeer) - 开发友好的 CLI 应用程序：根据结构字段和标签设置标志、默认值和用法。
- [complete](https://github.com/posener/complete) - 在 Go + Go 命令 bash 补全中编写 bash 补全。
- [控制台](https://github.com/reeflective/console) Cobra 命令的闭环应用程序库，带有 oh-my-posh 提示等。
- [Dnote](https://github.com/dnote/dnote) - 具有多设备同步功能的简单命令行笔记本。
- [elvish](https://github.com/elves/elvish) - 一种富有表现力的编程语言和多功能的交互式 shell。
- [env](https://github.com/codingconcepts/env) - 基于标签的结构环境配置。
- [flaggy](https://github.com/integrii/flaggy) - 一个强大且惯用的标志包，具有出色的子命令支持。
- [flagvar](https://github.com/sgreben/flagvar) - Go 标准“flag”包的标志参数类型的集合。
- [flash-flags](https://github.com/agilira/flash-flags) - 超快速、零依赖、符合 POSIX 标准的标志解析库，可用作具有安全强化功能的直接 stdlib 替代品。
- [getopt](https://github.com/jon-codes/getopt) - 准确的 Go `getopt`，已针对 GNU libc 实现进行验证。
- [go-arg](https://github.com/alexflint/go-arg) - Go 中基于结构的参数解析。
- [go-flags](https://github.com/jessevdk/go-flags) - go 命令行选项解析器。
- [go-getoptions](https://github.com/DavidGamba/go-getoptions) - Go 选项解析器受到 Perl 的 GetOpt::Long 灵活性的启发。
- [go-readline-ny](https://github.com/nyaosorg/go-readline-ny) - 一个可定制的行编辑库，具有 Emacs 键绑定、Unicode 支持、完成和语法突出显示。用于 NYAGOS shell。
- [gocmd](https://github.com/devfacet/gocmd) - 用于构建命令行应用程序的 Go 库。
- [goopt](https://github.com/napalu/goopt) - 一个用于 Go 的声明式、基于结构标记的 CLI 框架，具有广泛的功能集，例如分层命令/标志、i18n、shell 完成和验证。
- [hashicorp/cli](https://github.com/hashicorp/cli) - 用于实现命令行界面的 Go 库。
- [hiboot cli](https://github.com/hidevopsio/hiboot/tree/master/pkg/app/cli) - 具有自动配置和依赖注入功能的 cli 应用程序框架。
- [job](https://github.com/liujianping/job) - JOB，把你的短期指挥当成长期工作。
- [kingpin](https://github.com/alecthomas/kingpin) - 支持子命令的命令行和标志解析器（由“kong”取代；见下文）。
- [liner](https://github.com/peterh/liner) - 用于命令行界面的类似 readline 的库。
- [mcli](https://github.com/jxskiss/mcli) - 一个最小但非常强大的 Go cli 库。
- [memsh](https://github.com/amjadjibon/memsh) - Go 中的虚拟 bash shell：针对内存文件系统 (afero) 执行 shell 命令，具有 WASM 插件支持和可嵌入的 HTTP 服务器。
- [mkideal/cli](https://github.com/mkideal/cli) - 基于 golang 结构标签的功能丰富且易于使用的命令行包。
- [mow.cli](https://github.com/jawher/mow.cli) - 用于构建具有复杂标志和参数解析和验证的 CLI 应用程序的 Go 库。
- [neuron-cli](https://github.com/steevin/neuron-cli) - 本地优先、与 Obsidian 兼容的终端知识管理器。
- [ops](https://github.com/nanovms/ops) - Unikernel 构建器/编排器。
- [orpheus](https://github.com/agilira/orpheus) - CLI 框架具有安全强化、插件存储系统和生产可观察性功能。
- [pflag](https://github.com/spf13/pflag) - Go 的 flag 包的直接替换，实现 POSIX/GNU 风格的 --flags。
- [readline](https://github.com/reeflective/readline) - Shell 库具有现代且易于使用的 UI 功能。
- [sflags](https://github.com/octago/sflags) - 基于结构的标志生成器，适用于 flag、urfave/cli、pflag、cobra、kingpin 和其他库。
- [structcli](https://github.com/leodido/structcli) - 消除 Cobra 样板：从 Go 结构以声明方式构建强大、功能丰富的 CLI。
- [strumt](https://github.com/antham/strumt) - 创建提示链的库。
- [subcmd](https://github.com/bobg/subcmd) - 另一种解析和运行子命令的方法。与标准“flag”包一起工作。
- [teris-io/cli](https://github.com/teris-io/cli) - 用于在 Go 中构建命令行界面的简单且完整的 API。
- [urfave/cli](https://github.com/urfave/cli) - 用于在 Go 中构建命令行应用程序的简单、快速且有趣的软件包（以前称为 codegangsta/cli）。
- [version](https://github.com/mszostok/version) - 收集并显示多种格式的 CLI 版本信息以及升级通知。
- [wlog](https://github.com/dixonwille/wlog) - 简单的日志记录界面，支持跨平台颜色和并发。
- [wmenu](https://github.com/dixonwille/wmenu) - cli 应用程序易于使用的菜单结构，提示用户做出选择。

**[⬆ 回到顶部](#contents)**

## 配置

_用于配置解析的库._

- [aconfig](https://github.com/cristalhq/aconfig) - 简单、有用且固执己见的配置加载器。
- [argus](https://github.com/agilira/argus) - 使用 MPSC 环形缓冲区、自适应批处理策略和通用格式解析（JSON、YAML、TOML、INI、HCL、属性）进行文件监视和配置管理。
- [azureappconfiguration](https://github.com/Azure/AppConfiguration-GoProvider) - 用于从 Go 应用程序使用 Azure 应用程序配置中的数据的配置提供程序。
- [bcl](https://github.com/wkhere/bcl) - BCL是一种类似于HCL的配置语言。
- [cleanenv](https://github.com/ilyakaznacheev/cleanenv) - 简约的配置读取器（来自文件、ENV 以及任何您想要的位置）。
- [config](https://github.com/JeremyLoy/config) - 云原生应用程序配置。只需两行即可将 ENV 绑定到结构。
- [config](https://github.com/num30/config) - 使用文件、环境变量或两行代码中的标志配置您的应用程序。
- [config](https://github.com/andreiavrammsd/config) - 基于结构的配置加载器，具有专用的配置文件解析器，支持环境变量、标志、默认值和验证。
- [configuration](https://github.com/BoRuDar/configuration) - 用于从环境变量、文件、标志和“默认”标签初始化配置结构的库。
- [configuro](https://github.com/sherifabdlnaby/configuro) - 来自 ENV 和 Files 的固执己见的配置加载和验证框架，专注于 12 因素兼容应用程序。
- [confiq](https://github.com/greencoda/confiq) - 用于配置 Go 结构解码器库的结构化数据格式 - 支持多种数据格式。
- [confita](https://github.com/heetch/confita) - 将配置从多个后端级联加载到结构中。
- [conflate](https://github.com/the4thamigo-uk/conflate) - 用于合并来自任意 URL 的多个 JSON/YAML/TOML 文件、针对 JSON 模式进行验证以及应用模式中定义的默认值的库/工具。
- [enflag](https://github.com/atelpis/enflag) - 面向容器、零依赖的配置库，统一了Env变量和Flag解析。使用泛型来保证类型安全，没有反射或结构标签。
- [env](https://github.com/caarlos0/env) - 将环境变量解析为 Go 结构（使用默认值）。
- [env](https://github.com/junk1tm/env) - 用于将环境变量加载到结构中的轻量级包。
- [env](https://github.com/syntaqx/env) - 一个环境实用程序包，支持解组为结构。
- [envconfig](https://github.com/vrischmann/envconfig) - 从环境变量中读取您的配置。
- [envh](https://github.com/antham/envh) - 管理环境变量的助手。
- [envyaml](https://github.com/yuseferi/envyaml) - 带有环境变量读取器的 Yaml。将秘密作为环境变量但将它们的配置加载为结构化 Yaml 会有所帮助。
- [fig](https://github.com/kkyr/fig) - 用于从文件和环境变量中读取配置的小型库（带有验证和默认值）。
- [genv](https://github.com/sakirsensoy/genv) - 通过 dotenv 支持轻松读取环境变量。
- [go-array](https://github.com/deatil/go-array) - 从 Map、Slice 或 json 读取或设置数据的 Go 包。
- [go-aws-ssm](https://github.com/PaddleHQ/go-aws-ssm) - 从 AWS System Manager - Parameter Store 获取参数的 Go 包。
- [go-external-config](https://github.com/go-external-config/go) - 受 Spring 启发的 Go 配置管理库。
- [go-external-config/aws](https://github.com/go-external-config/aws) - AWS 属性源支持 go-external-config。
- [go-external-config/consul](https://github.com/go-external-config/consul) - Consul 属性源支持 go-external-config。
- [go-external-config/vault](https://github.com/go-external-config/vault) - go-external-config 的 Vault 属性源支持。
- [go-cfg](https://github.com/dsbasko/go-cfg) - 该库提供了一种统一的方法来将配置数据从各种来源（例如 env、标志和配置文件（.json、.yaml、.toml、.env））读取到结构中。
- [go-conf](https://github.com/ThomasObenaus/go-conf) - 基于带注释的结构的用于应用程序配置的简单库。它支持从环境变量、配置文件和命令行参数中读取配置。
- [go-config](https://github.com/MordaTeam/go-config) - 用于处理应用程序配置的简单便捷的库。
- [go-ini](https://github.com/subpop/go-ini) - 编组和解组 INI 文件的 Go 包。
- [go-ssm-config](https://github.com/ianlopshire/go-ssm-config) - 用于从 AWS SSM（参数存储）加载配置参数的 Go 实用程序。
- [go-up](https://github.com/ufoscout/go-up) - 一个简单的配置库，具有递归占位符分辨率，没有什么魔力。
- [GoCfg](https://github.com/Jagerente/gocfg) - 配置管理器，具有基于结构标签的合约、自定义值提供程序、解析器和文档生成。可定制但简单。
- [goconfig](https://github.com/fulldump/goconfig) - 使用确定性优先级从标志、环境变量、config.json 和默认值填充 Go 结构。没有额外的依赖。
- [godotenv](https://github.com/joho/godotenv) - Ruby 的 dotenv 库的移植（从 `.env` 加载环境变量）。
- [GoLobby/Config](https://github.com/golobby/config) - GoLobby Config 是一个轻量级但功能强大的 Go 编程语言配置管理器。
- [gone/jconf](https://github.com/One-com/gone/tree/master/jconf) - 模块化 JSON 配置。保留您的配置结构以及它们配置的代码并将解析委托给子模块，而无需牺牲完整的配置序列化。
- [gonfig](https://github.com/milad-abbasi/gonfig) - 基于标签的配置解析器，它将来自不同提供者的值加载到类型安全结构中。
- [gookit/config](https://github.com/gookit/config) - 应用程序配置管理（加载、获取、设置）。支持 JSON、YAML、TOML、INI、HCL。多文件加载，数据覆盖合并。
- [harvester](https://github.com/beatlabs/harvester) - Harvester，一个易于使用的静态和动态配置包，支持播种、环境变量和 Consul 集成。
- [hedzr/store](https://github.com/hedzr/store) - 可扩展的高性能配置管理库，针对分层数据进行了优化。
- [hjson](https://github.com/hjson/hjson-go) - Human JSON，人类的配置文件格式。宽松的语法，更少的错误，更多的注释。
- [hocon](https://github.com/gurkankaymak/hocon) - 用于使用 HOCON（一种人类友好的 JSON 超集）格式的配置库，支持环境变量、引用其他值、注释和多个文件等功能。
- [ini](https://github.com/go-ini/ini) - Go打包读写INI文件。
- [ini](https://github.com/wlevene/ini) - INI 解析器和写入库、解组到结构、编组到 Json、写入文件、监视文件。
- [kelseyhightower/envconfig](https://github.com/kelseyhightower/envconfig) - 用于管理环境变量中的配置数据的 Go 库。
- [koanf](https://github.com/knadh/koanf) - 轻量级、可扩展的库，用于读取 Go 应用程序中的配置。内置对 JSON、TOML、YAML、env、命令行的支持。
- [konf](https://github.com/nil-go/konf) - 最简单的 API，用于从文件、环境、标志和云（例如 AWS、Azure、GCP）读取/监视配置。
- [konfig](https://github.com/lalamove/konfig) - 分布式处理时代 Go 的可组合、可观察和高性能配置处理。
- [kong](https://github.com/alecthomas/kong) - 命令行解析器支持任意复杂的命令行结构和其他配置源，例如 YAML、JSON、TOML 等（“kingpin”的后继者）。
- [nasermirzaei89/env](https://github.com/nasermirzaei89/env) - 用于读取环境变量的简单有用的包。
- [nfigure](https://github.com/muir/nfigure) - 来自命令行的基于每个库结构标记的配置（Posix 和 Go 风格）；环境、JSON、YAML
- [onion](https://github.com/goraz/onion) - Go 的基于层的配置，支持 JSON、TOML、YAML、属性、etcd、env 和使用 PGP 的加密。
- [piper](https://github.com/Yiling-J/piper) - 具有配置继承和密钥生成功能的 Viper 包装器。
- [sonic](https://github.com/bytedance/sonic) - 一个极快的 JSON 序列化和反序列化库。
- [swap](https://github.com/oblq/swap) - 根据构建环境递归地实例化/配置结构。 （YAML、TOML、JSON 和 env）。
- [typenv](https://github.com/diegomarangoni/typenv) - 简约、零依赖、类型化环境变量库。
- [uConfig](https://github.com/omeid/uconfig) - 轻量级、零依赖、可扩展的配置管理。
- [viper](https://github.com/spf13/viper) - 用尖牙去配置。
- [xdg](https://github.com/adrg/xdg) - 实施 [XDG 基本目录规范](https://specations.freedesktop.org/basedir-spec/latest/) 和 [XDG 用户目录](https://wiki.archlinux.org/index.php/XDG_user_directories)。
- [yamagiconf](https://github.com/romshark/yamagiconf) - Go 配置的 YAML 的“安全子集”。
- [zerocfg](https://github.com/chaindead/zerocfg) - 零努力、简洁的配置管理避免了样板文件和重复代码，支持具有优先级覆盖的多个源。

**[⬆ 回到顶部](#contents)**

## 持续集成

_帮助持续集成的工具。_

- [abstruse](https://github.com/bleenco/abstruse) - Abstruse 是一个分布式 CI 平台。
- [Bencher](https://bencher.dev/) - 一套连续基准测试工具，旨在捕获 CI 中的性能回归。
- [CDS](https://github.com/ovh/cds) - 企业级 CI/CD 和 DevOps 自动化开源平台。
- [dot](https://github.com/opnlabs/dot) - 一个最小的、本地第一个持续集成系统，使用 Docker 分阶段并发运行作业。
- [drone](https://github.com/drone/drone) - Drone 是一个基于 Docker 构建的持续集成平台，用 Go 编写。
- [go-beautiful-html-coverage](https://github.com/gha-common/go-beautiful-html-coverage) - 一个 GitHub Action，可免费跟踪拉取请求中的代码覆盖率，并提供精美的 HTML 预览。
- [go-fuzz-action](https://github.com/jidicula/go-fuzz-action) - 在 GitHub Actions 中使用 Go 1.18 的内置模糊测试。
- [go-semver-release](https://github.com/s0ders/go-semver-release) - 自动执行 Git 存储库的语义版本控制。
- [go-test-coverage](https://github.com/marketplace/actions/go-test-coverage) - 当测试覆盖率低于设定阈值时报告问题的 GitHub 操作。
- [gomason](https://github.com/nikogura/gomason) - 从干净的工作区测试、构建、签名和发布您的 go 二进制文件。
- [gotestfmt](https://github.com/GoTestTools/gotestfmt) - 去测试人类的输出。
- [goveralls](https://github.com/mattn/goveralls) - Go 集成 Coveralls.io 连续代码覆盖率跟踪系统。
- [muffet](https://github.com/raviqqe/muffet) - Go 中的快速网站链接检查器，请参阅[替代方案](https://github.com/lycheeverse/lychee#features)。
- [overalls](https://github.com/go-playground/overalls) - 多包 go 项目封面，适用于工作服等工具。
- [PikoCI](https://github.com/pikoci/pikoci) - 受 Concourse 启发的自托管 CI/CD。单个二进制文件、任何数据库、任何队列。 HCL 管道、可插入资源类型和运行器。
- [roveralls](https://github.com/LawrenceWoodman/roveralls) - 递归覆盖测试工具。
- [woodpecker](https://github.com/woodpecker-ci/woodpecker) - Woodpecker 是 Drone CI 系统的社区分支。

**[⬆ 回到顶部](#contents)**

## CSS 预处理器

_用于预处理 CSS 文件的库._

- [go-css](https://github.com/napsy/go-css) - 一个非常简单的 CSS 解析器，用 Go 编写。
- [go-libsass](https://github.com/wellington/go-libsass) - 包装到 100% Sass 兼容的 libsass 项目。

**[⬆ 回到顶部](#contents)**

## 数据集成框架

_执行 ELT / ETL 的框架_

- [Benthos](https://github.com/benthosdev/benthos) - 一系列协议之间的消息流桥。
- [CloudQuery](http://github.com/cloudquery/cloudquery) - 具有可插拔架构的高性能 ELT 数据集成框架。
- [confluence2md](https://github.com/gkoos/confluence2md) - 与 Markdown 爬虫和转换器的融合。
- [omniparser](https://github.com/jf-tech/omniparser) - 多功能 ETL 库，以流方式解析文本输入（CSV/txt/JSON/XML/EDI/X12/EDIFACT/等），并使用数据驱动模式将数据转换为 JSON 输出。

**[⬆ 回到顶部](#contents)**

## 数据结构和算法

### 位打包和压缩

- [bingo](https://github.com/iancmcc/bingo) - 将本机类型快速、零分配、保留字典顺序打包为字节。
- [binpacker](https://github.com/zhuangsirui/binpacker) - 二进制打包器和解包器帮助用户构建自定义二进制流。
- [bit](https://github.com/yourbasic/bit) - Golang 设置数据结构，具有额外的位操作功能。
- [crunch](https://github.com/superwhiskers/crunch) - Go 包实现了用于轻松处理各种数据类型的缓冲区。
- [go-ef](https://github.com/amallia/go-ef) - Elias-Fano 编码的 Go 实现。
- [roaring](https://github.com/RoaringBitmap/roaring) - Go 包实现压缩位集。

### 钻头组

- [bitmap](https://github.com/kelindar/bitmap) - Go 中的密集、零分配、支持 SIMD 的位图/位集。
- [bitset](https://github.com/bits-and-blooms/bitset) - Go 包实现位集。

### 布卢姆和布谷鸟过滤器

- [bloom](https://github.com/bits-and-blooms/bloom) - Go 包实现布隆过滤器。
- [bloom](https://github.com/zhenjl/bloom) - 用 Go 实现的布隆过滤器。
- [bloom](https://github.com/yourbasic/bloom) - Golang 布隆过滤器实现。
- [bloomfilter](https://github.com/OldPanda/bloomfilter) - Go 中的另一个 Bloomfilter 实现，与 Java 的 Guava 库兼容。
- [boomfilters](https://github.com/tylertreat/BoomFilters) - 用于处理连续、无界流的概率数据结构。
- [cuckoo-filter](https://github.com/linvon/cuckoo-filter) - Cuckoo filter：一个综合性的cuckoo过滤器，与其他工具相比，它是可配置的并且空间优化的，并且原始论文中提到的所有功能都可用。
- [cuckoofilter](https://github.com/seiflotfy/cuckoofilter) - Cuckoo 过滤器：Go 中实现的计数布隆过滤器的一个很好的替代方案。
- [ribbonGo](https://github.com/RibbonFilter/ribbonGo) - Ribbon 过滤器的第一个纯 Go 实现（实际上比 Bloom 和 Xor 小），用于节省空间的近似集成员资格查询。
- [ring](https://github.com/TheTannerRyan/ring) - Go 实现了一个高性能、线程安全的布隆过滤器。

### 数据结构与算法合集

- [algorithms](https://github.com/shady831213/algorithms) - 算法和数据结构。CLRS 研究。
- [go-datastructures](https://github.com/Workiva/go-datastructures) - 有用、高性能且线程安全的数据结构的集合。
- [gods](https://github.com/emirpasic/gods) - 转到数据结构。容器、集合、列表、堆栈、映射、BidiMap、树、哈希集等。
- [gostl](https://github.com/liyue201/gostl) - go的数据结构和算法库，旨在提供类似于C++ STL的功能。

### 迭代器

- [gloop](https://github.com/alvii147/gloop) - 使用 Go 的 range-over-func 功能实现方便的循环。
- [goterator](https://github.com/yaa110/goterator) - 迭代器实现提供映射和归约功能。
- [iter](https://github.com/disksing/iter) - C++ STL 迭代器和算法的 Go 实现。

### 地图

另请参阅 [Database](#database) 了解更复杂的键值存储，以及 [Trees](#trees) 了解更多
额外的有序地图实现。

- [cmap](https://github.com/lrita/cmap) - Go 的线程安全并发映射，支持使用“interface{}”作为键并自动扩展分片。
- [concurrent-swiss-map](https://github.com/mhmtszr/concurrent-swiss-map) - 使用 Swiss Map 实现高性能、线程安全的通用并发哈希映射。
- [dict](https://github.com/srfrog/dict) - 用于 Go 的类似 Python 的字典 (dict)。
- [go-shelve](https://github.com/lucmq/go-shelve) - Go 编程语言的持久性、类似地图的对象。支持多个嵌入式键值存储。
- [goradd/maps](https://github.com/goradd/maps) - Go 1.18+ 地图通用地图接口；安全地图；订购地图；有序、安全的地图；等等
- [hmap](https://github.com/lyonnee/hmap) - HMap 是一个并发、安全、通用的支持 Map 实现，旨在提供易于使用的 API。

### 各种数据结构和算法

- [combo](https://github.com/bobg/combo) - 组合运算包括排列、组合和替换组合。
- [concurrent-writer](https://github.com/free/concurrent-writer) - “bufio.Writer”的高并发直接替代品。
- [count-min-log](https://github.com/seiflotfy/count-min-log) - Go 实现 Count-Min-Log 草图：使用近似计数器进行近似计数（类似于 Count-Min 草图，但使用更少的内存）。
- [FSM](https://github.com/enetx/fsm) - Go 的 FSM。
- [fsm](https://github.com/cocoonspace/fsm) - 有限状态机包。
- [genfuncs](https://github.com/nwillc/genfuncs) - Go 1.18+ 泛型包的灵感来自于 Kotlin 的 Sequence 和 Map。
- [go-generics](https://github.com/bobg/go-generics) - 通用切片、映射、集合、迭代器和 goroutine 实用程序。
- [go-geoindex](https://github.com/hailocab/go-geoindex) - 内存中地理索引。
- [go-rampart](https://github.com/francesconi/go-rampart) - 确定间隔如何相互关联。
- [go-rquad](https://github.com/aurelien-rainone/go-rquad) - 具有高效点定位和邻居查找功能的区域四叉树。
- [go-tuple](https://github.com/barweiss/go-tuple) - Go 1.18+ 的通用元组实现。
- [go18ds](https://github.com/daichi-m/go18ds) - 使用 Go 1.18 泛型的 Go 数据结构。
- [gofal](https://github.com/xxjwxc/gofal) - Go 的小数 api。
- [gogu](https://github.com/esimov/gogu) - 一个全面、可重用且高效的并发安全泛型实用函数和数据结构库。
- [gota](https://github.com/kniren/gota) - Go 的数据帧、系列和数据整理方法的实现。
- [hide](https://github.com/emvi/hide) - ID 类型与散列编组，以防止将 ID 发送到客户端。
- [hyperloglog](https://github.com/axiomhq/hyperloglog) - HyperLogLog 实现具有 Sparse、LogLog-Beta 偏差校正和 TailCut 空间缩减。
- [quadtree](https://github.com/s0rg/quadtree) - 通用、零分配、100% 测试覆盖的四叉树。
- [slices](https://github.com/twharmon/slices) - 切片的纯通用函数。

### 可空类型

- [nan](https://github.com/kak-tus/nan) - 零分配 一个库中的可空结构，具有方便的转换函数、编组器和反编组器。
- [null](https://github.com/emvi/null) - 可以从 JSON 编组/取消编组的可空 Go 类型。
- [typ](https://github.com/gurukami/typ) - 空类型、安全原始类型转换以及从复杂结构中获取值。

### 队列

- [deheap](https://github.com/aalpar/deheap) - 双端堆（最小-最大堆），访问最小和最大元素的时间复杂度为 O(log n)。
- [deque](https://github.com/edwingeng/deque) - 高度优化的双端队列。
- [deque](https://github.com/gammazero/deque) - 快速环形缓冲区双端队列（双端队列）。
- [dqueue](https://github.com/vodolaz095/dqueue) - 简单、在内存中、零依赖、经过实战考验、线程安全的延迟队列。
- [goconcurrentqueue](https://github.com/enriquebris/goconcurrentqueue) - 并发 FIFO 队列。
- [hatchet](https://github.com/hatchet-dev/hatchet) - 分布式、容错的任务队列。
- [list](https://github.com/koss-null/list) - 一个通用的、线程安全的双链表，具有完整的迭代器支持和一个用于嵌入式使用的侵入式单链表；容器/列表的功能丰富的替代品。
- [memlog](https://github.com/embano1/memlog) - 受 Apache Kafka 启发，一种易于使用、轻量级、线程安全且仅附加的内存数据结构。
- [queue](https://github.com/adrianbrad/queue) - Go 的多个线程安全的通用队列实现。

### 套装

- [dsu](https://github.com/ihebu/dsu) - Go 中的不相交集数据结构实现。
- [golang-set](https://github.com/deckarep/golang-set) - Go 的线程安全和非线程安全高性能集。
- [goset](https://github.com/zoumo/goset) - Go 的一个有用的 Set 集合实现。
- [set](https://github.com/StudioSol/set) - 使用 LinkedHashMap 在 Go 中实现简单的集合数据结构。

### 文本分析

- [bleve](https://github.com/blevesearch/bleve) - Go 的现代文本索引库。
- [go-adaptive-radix-tree](https://github.com/plar/go-adaptive-radix-tree) - Go 实现自适应基数树。
- [go-edlib](https://github.com/hbollon/go-edlib) - 兼容 Unicode 的 Go 字符串比较和编辑距离算法库（Levenshtein、LCS、Hamming、Damerau levenshtein、Jaro-Winkler 等）。
- [levenshtein](https://github.com/agext/levenshtein) - 编辑距离和相似性度量，具有可定制的编辑成本和公共前缀的类似 Winkler 的奖励。
- [levenshtein](https://github.com/agnivade/levenshtein) - Go 中计算编辑距离的实现。
- [mspm](https://github.com/BlackRabbitt/mspm) - 用于信息检索的多字符串模式匹配算法。
- [parsefields](https://github.com/MonaxGT/parsefields) - 用于解析类似 JSON 的日志以收集独特字段和事件的工具。
- [ptrie](https://github.com/viant/ptrie) - 前缀树的实现。
- [radixtree](https://github.com/gammazero/radixtree) - 自适应基数树（前缀树或紧凑特里树）。
- [trie](https://github.com/derekparker/trie) - Go 中的 Trie 实现。

### 树木

- [graphlib](https://github.com/aio-arch/graphlib) - 拓扑排序库，DAG 图的排序和剪枝。
- [hashsplit](http://github.com/bobg/hashsplit) - 将字节流分割成块，并将块排列成树，边界由内容而不是位置确定。
- [merkle](https://github.com/bobg/merkle) - Merkle 根哈希和包含证明的空间高效计算。
- [skiplist](https://github.com/MauriceGit/skiplist) - 非常快的 Go Skiplist 实现。
- [skiplist](https://github.com/gansidui/skiplist) - Go 中的 Skiplist 实现。
- [treemap](https://github.com/igrmk/treemap) - 在引擎盖下使用红黑树的通用键排序映射。

### 管道

- [ordered-concurrently](https://github.com/tejzpr/ordered-concurrently) - Go 模块并发处理工作并按输入顺序在通道中返回输出。
- [parapipe](https://github.com/nazar256/parapipe) - FIFO 管道在每个阶段并行执行，同时保持消息和结果的顺序。
- [pipeline](https://github.com/hyfather/pipeline) - 具有扇入和扇出的管道的实现。
- [pipelines](https://github.com/nxdir-s/pipelines) - 用于并发处理的通用管道函数。

**[⬆ 回到顶部](#contents)**

## 数据库

### 缓存

_具有过期记录的数据存储、内存中分布式数据存储或基于文件的数据库的内存子集。_

- [bcache](https://github.com/iwanbk/bcache) - 最终一致的分布式内存缓存Go库。
- [BigCache](https://github.com/allegro/bigcache) - 用于千兆字节数据的高效键/值缓存。
- [cache2go](https://github.com/muesli/cache2go) - 内存中的 key:value 缓存，支持基于超时的自动失效。
- [cachego](https://github.com/faabiosr/cachego) - 用于多个驱动程序的 Golang 缓存组件。
- [clusteredBigCache](https://github.com/oaStuff/clusteredBigCache) - BigCache 具有集群支持和单个项目过期功能。
- [coherence-go-client](https://github.com/oracle/coherence-go-client) - 使用 gRPC 作为网络传输的 Go 应用程序的 Oracle Coherence 缓存 API 的完整实现。
- [couchcache](https://github.com/codingsince1985/couchcache) - 由 Couchbase 服务器支持的 RESTful 缓存微服务。
- [EchoVault](https://github.com/EchoVault/EchoVault) - 与 Redis 客户端兼容的嵌入式分布式内存数据存储。
- [fastcache](https://github.com/VictoriaMetrics/fastcache) - 用于大量条目的快速线程安全内存缓存。最大限度地减少 GC 开销。
- [GCache](https://github.com/bluele/gcache) - 支持过期缓存、LFU、LRU 和 ARC 的缓存库。
- [gdcache](https://github.com/ulovecode/gdcache) - golang实现的纯非侵入式缓存库，你可以用它来实现自己的分布式缓存。
- [go-cache](https://github.com/viney-shih/go-cache) - 一个灵活的多层Go缓存库，采用Cache-Aside模式来处理内存和共享缓存。
- [go-freelru](https://github.com/elastic/go-freelru) 一个无 GC、快速且通用的 LRU 哈希图库，具有可选的锁定、分片、驱逐和过期功能。
- [go-gcache](https://github.com/szyhf/go-gcache) - `GCache` 的通用版本，对可过期 Cache、LFU、LRU 和 ARC 的缓存支持。
- [go-mcache](https://github.com/OrlovEvgeny/go-mcache) - 快速内存键：值存储/缓存库。指针缓存。
- [gocache](https://github.com/eko/gocache) - 一个完整的 Go 缓存库，具有多个存储（内存、memcache、redis...）、可链接、可加载、指标缓存等。
- [gocache](https://github.com/yuseferi/gocache) - 具有高性能和自动清除功能的无数据竞争 Go ache 库
- [groupcache](https://github.com/golang/groupcache) - Groupcache 是一个缓存和缓存填充库，在许多情况下旨在替代 memcached。
- [icache](https://github.com/mdaliyan/icache) - 高性能、通用、线程安全、零依赖的缓存包。
- [imcache](https://github.com/erni27/imcache) - 通用内存缓存 Go 库。它支持过期、滑动过期、最大条目限制、驱逐回调和分片。
- [jetcache-go](https://github.com/mgtv-tech/jetcache-go) - 支持多级缓存的统一Go缓存库。
- [nscache](https://github.com/no-src/nscache) - 支持多种数据源驱动的Go缓存框架。
- [otter](https://github.com/maypok86/otter) - Go 的高性能无锁缓存。比 Ristretto 和朋友们快很多倍。
- [pocache](https://github.com/naughtygopher/pocache) - Pocache 是一个最小的缓存包，专注于抢占式乐观缓存策略。
- [ristretto](https://github.com/dgraph-io/ristretto) - 高性能内存绑定 Go 缓存。
- [sturdyc](https://github.com/viccon/sturdyc) - 具有高级并发功能的缓存库，旨在使 I/O 密集型应用程序健壮且高性能。
- [theine](https://github.com/Yiling-J/theine-go) - 高性能、近乎最佳的内存缓存，具有主动 TTL 过期和泛型功能。
- [timedmap](https://github.com/zekroTJA/timedmap) - 具有过期键值对的映射。
- [ttlcache](https://github.com/jellydator/ttlcache) - 具有项目过期和泛型的内存缓存。
- [ttlcache](https://github.com/cheshir/ttlcache) - 内存中键值存储，每条记录都有 TTL。

### 用 Go 实现的数据库

- [badger](https://github.com/dgraph-io/badger) - Go 中的快速键值存储。
- [bbolt](https://github.com/etcd-io/bbolt) - Go 的嵌入式键/值数据库。
- [Bitcask](https://git.mills.io/prologic/bitcask) - Bitcask 是一个用纯 Go 编写的可嵌入、持久且快速的键值 (KV) 数据库，由于采用了 bitcask 磁盘布局 (LSM+WAL)，因此具有可预测的读/写性能、低延迟和高吞吐量。
- [buntdb](https://github.com/tidwall/buntdb) - 用于 Go 的快速、可嵌入、内存中键/值数据库，具有自定义索引和空间支持。
- [clover](https://github.com/ostafen/clover) - 用纯 Golang 编写的轻量级面向文档的 NoSQL 数据库。
- [cockroach](https://github.com/cockroachdb/cockroach) - 可扩展、地理复制、事务性数据存储。
- [Coffer](https://github.com/claygod/coffer) - 支持事务的简单 ACID 键值数据库。
- [column](https://github.com/kelindar/column) - 具有位图索引和事务功能的高性能、柱状、可嵌入内存存储。
- [CovenantSQL](https://github.com/CovenantSQL/CovenantSQL) - CovenantSQL是区块链上的SQL数据库。
- [Databunker](https://github.com/paranoidguy/databunker) - 为遵守 GDPR 和 CCPA 而构建的个人身份信息 (PII) 存储服务。
- [dgraph](https://github.com/dgraph-io/dgraph) - 可扩展、分布式、低延迟、高吞吐量图数据库。
- [DiceDB](https://github.com/DiceDB/dice) - 一个针对现代硬件优化的开源、快速、反应式内存数据库。更高的吞吐量和更低的中值延迟，使其成为现代工作负载的理想选择。
- [diskv](https://github.com/peterbourgon/diskv) - 本地磁盘支持的键值存储。
- [dolt](https://github.com/dolthub/dolt) - Dolt – 这是数据的 Git。
- [eliasdb](https://github.com/krotik/eliasdb) - 无依赖关系的事务性图形数据库，具有 REST API、短语搜索和类似 SQL 的查询语言。
- [godis](https://github.com/hdt3213/godis) - Golang实现了高性能Redis服务器和集群。
- [goleveldb](https://github.com/syndtr/goleveldb) - 在 Go 中实现 [LevelDB](https://github.com/google/leveldb) 键/值数据库。
- [hare](https://github.com/jameycribbs/hare) - 一个简单的数据库管理系统，将每个表存储为行分隔 JSON 的文本文件。
- [immudb](https://github.com/codenotary/immudb) - immudb 是一个轻量级、高速的不可变数据库，适用于用 Go 编写的系统和应用程序。
- [influxdb](https://github.com/influxdb/influxdb) - 用于指标、事件和实时分析的可扩展数据存储。
- [ledisdb](https://github.com/siddontang/ledisdb) - Ledisdb是一个基于LevelDB的类似于Redis的高性能NoSQL。
- [levigo](https://github.com/jmhodges/levigo) - Levigo 是 LevelDB 的 Go 包装器。
- [libradb](https://github.com/amit-davidson/LibraDB) - LibraDB是一个简单的数据库，只有不到1000行代码可供学习。
- [LinDB](https://github.com/lindb/lindb) - LinDB是一个可扩展、高性能、高可用性的分布式时间序列数据库。
- [lotusdb](https://github.com/flower-corp/lotusdb) - 与 lsm 和 b+tree 兼容的快速 k/v 数据库。
- [lynxdb](https://github.com/lynxbase/lynxdb) - 轻量级列式日志分析数据库，具有受 SPL 启发的管道式查询语言。
- [Milvus](https://github.com/milvus-io/milvus) - Milvus 是一个用于嵌入管理、分析和搜索的矢量数据库。
- [moss](https://github.com/couchbase/moss) - Moss 是一个简单的 LSM 键值存储引擎，用 100% Go 编写。
- [nanotdb](https://github.com/aymanhs/nanotdb) - 针对低功耗硬件进行优化的轻量级、零依赖性、仅附加时间序列数据库和仪表板。
- [NoKV](https://github.com/feichai0017/NoKV) - 适用于分布式文件系统、对象存储和 AI 数据集工作负载的本机元数据服务。
- [NornicDB](https://github.com/orneryd/NornicDB) - 高性能图+向量数据库（Neo4j和qDrant兼容），专注于人工智能系统的低延迟图碎片检索。
- [nutsdb](https://github.com/xujiajun/nutsdb) - Nutsdb 是一个用纯 Go 编写的简单、快速、可嵌入、持久的键/值存储。它支持完全可序列化的事务和许多数据结构，例如列表、集合、排序集。
- [objectbox-go](https://github.com/objectbox/objectbox-go) - 具有 Go API 的高性能嵌入式对象数据库 (NoSQL)。
- [pebble](https://github.com/cockroachdb/pebble) - RocksDB/LevelDB 启发了 Go 中的键值数据库。
- [piladb](https://github.com/fern4lvarez/piladb) - 基于堆栈数据结构的轻量级RESTful数据库引擎。
- [pogreb](https://github.com/akrylysov/pogreb) - 用于读取密集型工作负载的嵌入式键值存储。
- [prometheus](https://github.com/prometheus/prometheus) - 监控系统和时间序列数据库。
- [pudge](https://github.com/recoilme/pudge) - 使用 Go 的标准库编写的快速且简单的键/值存储。
- [redka](https://github.com/nalgeon/redka) - Redis 用 SQLite 重新实现。
- [rosedb](https://github.com/roseduan/rosedb) - 基于LSM+WAL的嵌入式k-v数据库，支持string、list、hash、set、zset。
- [rotom](https://github.com/xgzlucario/rotom) - 使用Golang构建的小型Redis服务器，兼容RESP协议。
- [rqlite](https://github.com/rqlite/rqlite) - 基于 SQLite 构建的轻量级分布式关系数据库。
- [tempdb](https://github.com/rafaeljesus/tempdb) - 临时项目的键值存储。
- [tidb](https://github.com/pingcap/tidb) - TiDB 是一个分布式 SQL 数据库。灵感源自 Google F1 的设计。
- [tiedot](https://github.com/HouzuoGuo/tiedot) - 由 Golang 提供支持的 NoSQL 数据库。
- [unitdb](https://github.com/unit-io/unitdb) - 适用于物联网、实时消息传递应用程序的快速时间序列数据库。使用 github.com/unit-io/unitd 应用程序通过 tcp 或 websocket 通过 pubsub 访问unitdb。
- [Vasto](https://github.com/chrislusf/vasto) - 分布式高性能键值存储。在磁盘上。最终一致。哈。能够在不中断服务的情况下扩大或缩小。
- [VictoriaMetrics](https://github.com/VictoriaMetrics/VictoriaMetrics) - 快速、资源高效且可扩展的开源时间序列数据库。可用作 Prometheus 的长期远程存储。支持 PromQL。
- [minisql](https://github.com/RichardKnop/minisql) - 嵌入式单文件 SQL 数据库。
- 
### 数据库架构迁移

- [atlas](https://github.com/ariga/atlas) - 数据库工具包。 CLI 旨在帮助公司更好地处理数据。
- [avro](https://github.com/khezen/avro) - 发现 SQL 模式并将其转换为 AVRO 模式。查询 SQL 记录到 AVRO 字节中。
- [bytebase](https://github.com/bytebase/bytebase) - 为 DevOps 团队提供安全的数据库架构更改和版本控制。
- [darwin](https://github.com/GuiaBolso/darwin) - Go 的数据库模式演化库。
- [dbmate](https://github.com/amacneil/dbmate) - 一个轻量级的、与框架无关的数据库迁移工具。
- [go-fixtures](https://github.com/RichardKnop/go-fixtures) - Golang 优秀的内置数据库/sql 库的 Django 风格固定装置。
- [go-pg-migrate](https://github.com/lawzava/go-pg-migrate) - 用于 go-pg 迁移管理的 CLI 友好包。
- [go-pg-migrations](https://github.com/robinjoseph08/go-pg-migrations) - 一个 Go 包，可帮助使用 go-pg/pg 编写迁移。
- [goavro](https://github.com/linkedin/goavro) - 对 Avro 数据进行编码和解码的 Go 包。
- [godfish](https://github.com/rafaelespinoza/godfish) - 数据库迁移管理器，使用本机查询语言。支持cassandra、mysql、postgres、sqlite3。
- [goose](https://github.com/pressly/goose) - 数据库迁移工具。您可以通过创建增量 SQL 或 Go 脚本来管理数据库的演变。
- [gorm-seeder](https://github.com/Kachit/gorm-seeder) - Gorm ORM 的简单数据库播种器。
- [gormigrate](https://github.com/go-gormigrate/gormigrate) - Gorm ORM 的数据库模式迁移助手。
- [libschema](https://github.com/muir/libschema) - 在每个库中单独定义迁移。开源库的迁移。 MySQL 和 PostgreSQL。
- [migrate](https://github.com/golang-migrate/migrate) - 数据库迁移。 CLI 和 Golang 库。
- [migrator](https://github.com/lopezator/migrator) - 非常简单的 Go 数据库迁移库。
- [migrator](https://github.com/larapulse/migrator) - MySQL 数据库迁移器旨在运行功能迁移并使用直观的 Go 代码管理数据库架构更新。
- [schema](https://github.com/adlio/schema) - 用于在 Go 二进制文件中嵌入数据库/sql 兼容数据库的架构迁移的库。
- [skeema](https://github.com/skeema/skeema) - MySQL 的纯 SQL 模式管理系统，支持分片和外部在线模式更改工具。
- [soda](https://github.com/gobuffalo/pop/tree/master/soda) - MySQL、PostgreSQL 和 SQLite 的数据库迁移、创建、ORM 等。
- [sql-migrate](https://github.com/rubenv/sql-migrate) - 数据库迁移工具。允许使用 go-bindata 将迁移嵌入到应用程序中。
- [sqlize](https://github.com/sunary/sqlize) - 数据库迁移生成器。允许从模型和现有 SQL 中生成不同的 SQL 迁移。

### 数据库工具

- [chproxy](https://github.com/Vertamedia/chproxy) - ClickHouse 数据库的 HTTP 代理。
- [clickhouse-bulk](https://github.com/nikepan/clickhouse-bulk) - 收集小插入并向 ClickHouse 服务器发送大请求。
- [database-gateway](https://github.com/kazhuravlev/database-gateway) - 使用 ACL、日志和共享链接在生产中运行 SQL。
- [dbbench](https://github.com/sj14/dbbench) - 支持多个数据库和脚本的数据库基准测试工具。
- [dg](https://github.com/codingconcepts/dg) - 快速数据生成器，可从生成的关系数据生成 CSV 文件。
- [gatewayd](https://github.com/gatewayd-io/gatewayd) - 用于构建数据驱动应用程序的云原生数据库网关和框架。就像数据库的 API 网关一样。
- [go-mysql](https://github.com/siddontang/go-mysql) - 用于处理 MySQL 协议和复制的 Go 工具集。
- [go-postgres-s3-backup](https://github.com/nicobistolfi/go-postgres-s3-backup) - 无服务器 PostgreSQL 使用 AWS Lambda 备份到 S3，每日、每月和每年轮换。
- [gorm-multitenancy](https://github.com/bartventer/gorm-multitenancy) - 对 GORM 托管数据库的多租户支持。
- [GoSQLX](https://github.com/ajitpratap0/GoSQLX) - 高性能 SQL 解析器、格式化程序、linter 和安全扫描器，具有多方言支持和 WASM 游乐场。
- [hasql](https://golang.yandex/hasql) - 用于访问多主机 SQL 数据库安装的库。
- [octillery](https://github.com/knocknote/octillery) - 用于分片数据库的 Go 包（支持所有 ORM 或原始 SQL）。
- [onedump](https://github.com/liweiyi88/onedump) - 使用一个命令和配置即可将数据库从不同的驱动程序备份到不同的目的地。
- [pg_timetable](https://github.com/cybertec-postgresql/pg_timetable) - PostgreSQL 的高级调度。
- [pgrwl](https://github.com/pgrwl/pgrwl) - PostgreSQL 的云原生连续备份。
- [pgweb](https://github.com/sosedoff/pgweb) - 基于 Web 的 PostgreSQL 数据库浏览器。
- [pgxcli](https://github.com/Balaji01-4D/pgxcli) - 用 Go 编写的 PostgreSQL CLI 客户端，受到 pgcli 的启发。
- [prep](https://github.com/hexdigest/prep) - 使用准备好的 SQL 语句而不更改代码。
- [pREST](https://github.com/prest/prest) - 简化并加速任何 Postgres 应用程序（无论是现有的还是新的）的即时、实时、高性能开发。
- [rdb](https://github.com/HDT3213/rdb) - Redis RDB文件解析器，用于二次开发和内存分析。
- [rwdb](https://github.com/andizzle/rwdb) - rwdb 为多个数据库服务器设置提供只读副本功能。
- [vitess](https://github.com/youtube/vitess) - vitess 提供有助于扩展 MySQL 数据库以实现大规模 Web 服务的服务器和工具。
- [wescale](https://github.com/wesql/wescale) - WeScale 是一个数据库代理，旨在增强应用程序的可扩展性、性能、安全性和弹性。

### SQL 查询生成器

_用于构建和使用 SQL 的库._

- [bqb](https://github.com/nullism/bqb) - 轻量级且易于学习的查询生成器。
- [buildsqlx](https://github.com/arthurkushman/buildsqlx) - PostgreSQL 的 Go 数据库查询构建器库。
- [builq](https://github.com/cristalhq/builq) - 在 Go 中轻松构建 SQL 查询。
- [dbq](https://github.com/rocketlaunchr/dbq) - Go 的零样板数据库操作。
- [Dotsql](https://github.com/gchaincl/dotsql) - Go 库可帮助您将 sql 文件保存在一个位置并轻松使用它们。
- [gendry](https://github.com/didi/gendry) - 非侵入式 SQL 生成器和强大的数据绑定器。
- [godbal](https://github.com/xujiajun/godbal) - Go 的数据库抽象层（dbal）。支持SQL生成器并轻松获得结果。
- [goqu](https://github.com/doug-martin/goqu) - 惯用的 SQL 构建器和查询库。
- [gosql](https://github.com/twharmon/gosql) - SQL 查询构建器具有更好的空值支持。
- [Hotcoal](https://github.com/motrboat/hotcoal) - 保护您手工编写的 SQL 免受注入。
- [igor](https://github.com/galeone/igor) - PostgreSQL 的抽象层，支持高级功能并使用类似 gorm 的语法。
- [jet](https://github.com/go-jet/jet) - 用于在 Go 中编写类型安全 SQL 查询的框架，能够轻松地将数据库查询结果转换为所需的任意对象结构。
- [obreron](https://github.com/profe-ajedrez/obreron) - 快速且廉价的 SQL 构建器，它只做一件事：SQL 构建。
- [ormlite](https://github.com/pupizoid/ormlite) - 轻量级包，包含一些类似 ORM 的功能和 sqlite 数据库的帮助程序。
- [ozzo-dbx](https://github.com/go-ozzo/ozzo-dbx) - 强大的数据检索方法以及与数据库无关的查询构建功能。
- [patcher](https://github.com/Jacobbrewer1/patcher) - 强大的 SQL 查询生成器，可自动从结构生成 SQL 查询。
- [qry](https://github.com/HnH/qry) - 使用原始 SQL 查询从文件生成常量的工具。
- [relica](https://github.com/coregx/relica) - 类型安全的数据库查询生成器，具有零生产依赖性、LRU 语句缓存、批处理操作，并支持 JOIN、子查询、CTE 和窗口函数。
- [sg](https://github.com/go-the-way/sg) - 用 Go 编写的 SQL Gen，用于生成标准 SQL（支持：CRUD）。
- [sq](https://github.com/bokwoon95/go-structured-query) - Go 的类型安全 SQL 构建器和结构映射器。
- [sqlc](https://github.com/kyleconroy/sqlc) - 从 SQL 生成类型安全代码。
- [sqlf](https://github.com/leporo/sqlf) - 快速 SQL 查询生成器。
- [sqlh](https://github.com/kirill-scherba/sqlh) - 带有结构标签和 Go 泛型（CRUD、UPSERT、JOIN、基准测试）的零样板 SQL 助手。
- [sqlingo](https://github.com/lqs/sqlingo) - 用于在 Go 中构建 SQL 的轻量级 DSL。
- [sqrl](https://github.com/elgris/sqrl) - SQL 查询构建器，Squirrel 的分支，具有改进的性能。
- [Squalus](https://gitlab.com/qosenergy/squalus) - Go SQL 包上的薄层使执行查询变得更加容易。
- [Squirrel](https://github.com/Masterminds/squirrel) - Go 库可帮助您构建 SQL 查询。
- [xo](https://github.com/knq/xo) - 基于现有架构定义或支持 PostgreSQL、MySQL、SQLite、Oracle 和 Microsoft SQL Server 的自定义查询，为数据库生成惯用的 Go 代码。

**[⬆ 回到顶部](#contents)**

## 数据库驱动程序

### 与多个后端的接口

- [cayley](https://github.com/google/cayley) - 支持多个后端的图形数据库。
- [dsc](https://github.com/viant/dsc) - SQL、NoSQL、结构化文件的数据存储连接。
- [dynamo](https://github.com/fogfish/dynamo) - 一个简单的键值抽象，用于在 AWS 存储服务中存储代数和链接数据数据类型：AWS DynamoDB 和 AWS S3。
- [go-transaction-manager](https://github.com/avito-tech/go-transaction-manager) - 具有多个适配器（sql、sqlx、gorm、mongo...）的事务管理器控制事务边界。
- [gokv](https://github.com/philippgille/gokv) - Go 的简单键值存储抽象和实现（Redis、Consul、etcd、bbolt、BadgerDB、LevelDB、Memcached、DynamoDB、S3、PostgreSQL、MongoDB、CockroachDB 等）。
- [transactor](https://github.com/metalfm/transactor) - 带有数据库/sql、sqlx 和 pgx 适配器的类型安全事务边界抽象。

### 关系数据库驱动程序

- [avatica](https://github.com/apache/calcite-avatica-go) - 用于数据库/sql 的 Apache Avatica/Phoenix SQL 驱动程序。
- [bgc](https://github.com/viant/bgc) - BigQuery for go 的数据存储连接。
- [firebirdsql](https://github.com/nakagami/firebirdsql) - 适用于 Go 的 Firebird RDBMS SQL 驱动程序。
- [go-adodb](https://github.com/mattn/go-adodb) - 使用database/sql的Go的Microsoft ActiveX对象数据库驱动程序。
- [go-mssqldb](https://github.com/denisenkom/go-mssqldb) - 适用于 Go 的 Microsoft MSSQL 驱动程序。
- [go-oci8](https://github.com/mattn/go-oci8) - 使用数据库/sql 的 Go 的 Oracle 驱动程序。
- [go-rqlite](https://github.com/rqlite/gorqlite) - rqlite 的 Go 客户端，提供易于使用的抽象来使用 rqlite API。
- [go-sql-driver/mysql](https://github.com/go-sql-driver/mysql) - Go 的 MySQL 驱动程序。
- [go-sqlite3](https://github.com/mattn/go-sqlite3) - 使用数据库/sql 的 go 的 SQLite3 驱动程序。
- [go-sqlite3](https://github.com/ncruces/go-sqlite3) - 该Go模块与database/sql驱动程序兼容。它允许将 SQLite 嵌入到您的应用程序中，提供对其 C API 的直接访问，支持 SQLite VFS，并且还包含 GORM 驱动程序。
- [godror](https://github.com/godror/godror) - Go 的 Oracle 驱动程序，使用 ODPI-C 驱动程序。
- [gofreetds](https://github.com/minus5/gofreetds) - 微软 MSSQL 驱动程序。对 [FreeTDS](https://www.freetds.org) 进行包装。
- [KSQL](https://github.com/VinGarcia/ksql) - 一个简单而强大的 Golang SQL 库。
- [pgx](https://github.com/jackc/pgx) - PostgreSQL 驱动程序支持除数据库/sql 公开的功能之外的功能。
- [pig](https://github.com/alexeyco/pig) - 简单的[pgx](https://github.com/jackc/pgx)包装器可以轻松执行和[扫描](https://github.com/georgysavva/scany)查询结果。
- [pq](https://github.com/lib/pq) - 用于数据库/sql 的 Pure Go Postgres 驱动程序。
- [Sqinn-Go](https://github.com/cvilsmeier/sqinn-go) - SQLite 与纯 Go。
- [sqlhooks](https://github.com/qustavo/sqlhooks) - 将挂钩附加到任何数据库/sql 驱动程序。
- [sqlite](https://pkg.go.dev/modernc.org/sqlite) - sqlite 包是一个 sql/数据库驱动程序，使用 C SQLite3 库的 CGo-free 端口。
- [surrealdb.go](https://github.com/surrealdb/surrealdb.go) - SurrealDB Go 驱动程序。
- [ydb-go-sdk](https://github.com/ydb-platform/ydb-go-sdk) - 本机和数据库/sql 驱动程序 YDB（Yandex 数据库）。

### NoSQL 数据库驱动程序

- [aerospike-client-go](https://github.com/aerospike/aerospike-client-go) - Go 语言的 Aerospike 客户端。
- [arangolite](https://github.com/solher/arangolite) - ArangoDB 的轻量级 golang 驱动程序。
- [asc](https://github.com/viant/asc) - Aerospike for go 的数据存储连接。
- [forestdb](https://github.com/couchbase/goforestdb) - ForestDB 的 Go 绑定。
- [go-couchbase](https://github.com/couchbase/go-couchbase) - Go 中的 Couchbase 客户端。
- [go-mongox](https://github.com/chenmingyong0423/go-mongox) - 一个基于官方驱动程序的 Go Mongo 库，具有简化的文档操作、结构到集合的通用绑定、内置 CRUD、聚合、自动字段更新、结构验证、挂钩和基于插件的编程。
- [go-pilosa](https://github.com/pilosa/go-pilosa) - 转到 Pilosa 的客户端库。
- [go-rejson](https://github.com/nitishm/go-rejson) - 使用 Redigo golang 客户端的 redislabs ReJSON 模块的 Golang 客户端。在 Redis 中轻松存储和操作结构作为 JSON 对象。
- [gocb](https://github.com/couchbase/gocb) - 官方 Couchbase Go SDK。
- [gocosmos](https://github.com/btnguyen2k/gocosmos) - 适用于 Azure Cosmos DB 的 REST 客户端和标准“database/sql”驱动程序。
- [gocql](https://gocql.github.io) - Apache Cassandra 的 Go 语言驱动程序。
- [godis](https://github.com/piaohao/godis) - redis 客户端由 golang 实现，受到 jedis 的启发。
- [godscache](https://github.com/defcronyke/godscache) - Google Cloud Platform Go Datastore 包的包装器，使用 memcached 添加缓存。
- [gomemcache](https://github.com/bradfitz/gomemcache/) - Go 编程语言的 memcache 客户端库。
- [gomemcached](https://github.com/aliexpressru/gomemcached) - Go 的二进制 Memcached 客户端，支持使用一致哈希和 SASL 进行分片。
- [gorethink](https://github.com/dancannon/gorethink) - RethinkDB 的 Go 语言驱动程序。
- [goriak](https://github.com/zegl/goriak) - Riak KV 的 Go 语言驱动程序。
- [Kivik](https://github.com/go-kivik/kivik) - Kivik 为 CouchDB、PouchDB 和类似数据库提供了通用的 Go 和 GopherJS 客户端库。
- [mgm](https://github.com/kamva/mgm) - 基于 MongoDB 模型的 Go ODM（基于官方 MongoDB 驱动程序）。
- [mgo](https://github.com/globalsign/mgo) - （未维护）Go 语言的 MongoDB 驱动程序，在遵循标准 Go 习惯用法的非常简单的 API 下实现了丰富且经过良好测试的功能选择。
- [mongo-go-driver](https://github.com/mongodb/mongo-go-driver) - Go 语言的官方 MongoDB 驱动程序。
- [neo4j](https://github.com/cihangir/neo4j) - Golang 的 Neo4j Rest API 绑定。
- [neoism](https://github.com/jmcvetta/neoism) - Golang 的 Neo4j 客户端。
- [qmgo](https://github.com/qiniu/qmgo) - Go 的 MongoDB 驱动程序。它基于官方 MongoDB 驱动程序，但像 Mgo 一样更易于使用。
- [redeo](https://github.com/bsm/redeo) - Redis 协议兼容的 TCP 服务器/服务。
- [redigo](https://github.com/gomodule/redigo) - Redigo 是 Redis 数据库的 Go 客户端。
- [redis](https://github.com/redis/go-redis) - Golang 的 Redis 客户端。
- [rueidis](http://github.com/rueian/rueidis) - 具有自动流水线和服务器辅助客户端缓存功能的快速 Redis RESP3 客户端。
- [xredis](https://github.com/shomali11/xredis) - 类型安全、可定制、干净且易于使用的 Redis 客户端。

### 搜索和分析数据库

- [clickhouse-go](https://github.com/ClickHouse/clickhouse-go/) - 适用于 Go 的 ClickHouse SQL 客户端具有“database/sql”兼容性。
- [effdsl](https://github.com/sdqri/effdsl) - Go 的 Elasticsearch 查询构建器。
- [elastic](https://github.com/olivere/elastic) - Go 的 Elasticsearch 客户端。
- [elasticsql](https://github.com/cch123/elasticsql) - 在 Go 中将 sql 转换为 elasticsearch dsl。
- [elastigo](https://github.com/mattbaird/elastigo) - Elasticsearch 客户端库。
- [go-elasticsearch](https://github.com/elastic/go-elasticsearch) - Go 的官方 Elasticsearch 客户端。
- [goes](https://github.com/OwnLocal/goes) - 与 Elasticsearch 交互的库。
- [skizze](https://github.com/seiflotfy/skizze) - 概率数据结构服务和存储。
- [zoekt](https://github.com/sourcegraph/zoekt) - 基于三元组的快速代码搜索。

**[⬆ 回到顶部](#contents)**

## 日期和时间

_用于处理日期和时间的库._

- [approx](https://github.com/goschtalt/approx) - 持续时间扩展支持以天、周和年为单位的解析/打印持续时间。
- [carbon](https://github.com/dromara/carbon) - 一个简单、语义化且对开发人员友好的 golang 时间包。
- [carbon](https://github.com/uniplaces/carbon) - 简单的时间扩展，带有很多 util 方法，从 PHP Carbon 库移植。
- [cronrange](https://github.com/1set/cronrange) - 解析 Cron 风格的时间范围表达式，检查给定时间是否在任何范围内。
- [date](https://github.com/rickb777/date) - Augments Time 用于处理日期、日期范围、时间跨度、期间和一天中的时间。
- [dateparse](https://github.com/araddon/dateparse) - 在事先不知道格式的情况下解析日期。
- [durafmt](https://github.com/hako/durafmt) - Go 的持续时间格式化库。
- [feiertage](https://github.com/wlbr/feiertage) - 用于计算德国公共假期的函数集，包括。专注于德国各州（Bundesländer）。比如复活节、五旬节、感恩节……
- [go-anytime](https://github.com/ijt/go-anytime) - 解析日期/时间（如“下一个 12 月 22 日下午 3 点”）和范围（如“从今天到下周四”），而无需提前知道格式。
- [go-date-fns](https://github.com/chmenegatti/go-date-fns) - 一个全面的 Go 日期实用程序库，受 date-fns 启发，具有 140 多个纯且不可变的函数。
- [go-datebin](https://github.com/deatil/go-datebin) - 一个简单的日期时间解析 pkg。
- [go-faketime](https://github.com/harkaitz/go-faketime) - 一个简单的“time.Now()”，它遵循 faketime(1) 实用程序。
- [go-persian-calendar](https://github.com/yaa110/go-persian-calendar) - 在 Go (golang) 中实现波斯（阳历回历）日历。
- [go-str2duration](https://github.com/xhit/go-str2duration) - 将字符串转换为持续时间。支持 time.Duration 返回字符串等。
- [go-sunrise](https://github.com/nathan-osman/go-sunrise) - 计算给定位置的日出和日落时间。
- [go-week](https://github.com/stoewer/go-week) - 与 ISO8601 周日期配合使用的高效软件包。
- [gostradamus](https://github.com/bykof/gostradamus) - 用于处理日期的 Go 包。
- [iso8601](https://github.com/relvacode/iso8601) - 无需正则表达式即可有效解析 ISO8601 日期时间。
- [kair](https://github.com/GuilhermeCaruso/kair) - 日期和时间 - Golang 格式库。
- [now](https://github.com/jinzhu/now) - Now是golang的时间工具包。
- [strftime](https://github.com/awoodbeck/strftime) - C99 兼容的 strftime 格式化程序。
- [timespan](https://github.com/SaidinWoT/timespan) - 用于与时间间隔交互，定义为开始时间和持续时间。
- [timeutil](https://github.com/leekchan/timeutil) - golang 时间包的有用扩展（Timedelta、Strftime...）。
- [tuesday](https://github.com/osteele/tuesday) - 与 Ruby 兼容的 Strftime 函数。

**[⬆ 回到顶部](#contents)**

## 分布式系统

_帮助构建分布式系统的软件包._

- [arpc](https://github.com/lesismal/arpc) - 更有效的网络通讯，支持双向呼叫、通知、广播。
- [bedrock](https://github.com/z5labs/bedrock) - 为 Go 中快速开发服务和更多用例特定框架提供最小、模块化和可组合的基础。
- [capillaries](https://github.com/capillariesio/capillaries) - 分布式批量数据处理框架。
- [circuit](https://github.com/schigh/circuit) - 通过概率节流逐渐恢复的断路器。
- [cmd-stream-go](https://github.com/cmd-stream/cmd-stream-go) - Go 的高性能分布式命令模式库。
- [committer](https://github.com/vadiminshakov/committer) - 分布式事务管理系统（2PC/3PC实现）。
- [consistent](https://github.com/buraksezer/consistent) - 具有有限负载的一致散列。
- [consistenthash](https://github.com/mbrostami/consistenthash) - 与可配置副本的一致散列。
- [dht](https://github.com/anacrolix/dht) - BitTorrent Kademlia DHT 实施。
- [digota](https://github.com/digota/digota) - grpc 电子商务微服务。
- [dot](https://github.com/dotchain/dot/) - 使用运营转型/OT 进行分布式同步。
- [doublejump](https://github.com/edwingeng/doublejump) - 改进后的 Google 跳跃一致性哈希。
- [dragonboat](https://github.com/lni/dragonboat) - Go 中功能完整且高性能的多组 Raft 库。
- [Dragonfly](https://github.com/dragonflyoss/Dragonfly2) - 基于p2p技术提供高效、稳定、安全的文件分发和图像加速，成为云原生架构的最佳实践和标准解决方案。
- [drmaa](https://github.com/dgruber/drmaa) - 基于 DRMAA 标准的集群调度程序的作业提交库。
- [dynamolock](https://cirello.io/dynamolock) - DynamoDB 支持的分布式锁定实现。
- [dynatomic](https://github.com/tylfin/dynatomic) - 使用 DynamoDB 作为原子计数器的库。
- [emitter-io](https://github.com/emitter-io/emitter) - 使用 MQTT、Websockets 和爱心构建的高性能、分布式、安全和低延迟的发布-订阅平台。
- [evans](https://github.com/ktr0731/evans) - Evans：更具表现力的通用 gRPC 客户端。
- [failured](https://github.com/andy2046/failured) - 分布式系统的自适应应计故障检测器。
- [flowgraph](https://github.com/vectaport/flowgraph) - 基于流程的编程包。
- [gleam](https://github.com/chrislusf/gleam) - 纯 Go 和 Luajit 编写的快速且可扩展的分布式 Map/Reduce 系统，结合了 Go 的高并发性和 Luajit 的高性能，可独立运行或分布式运行。
- [glow](https://github.com/chrislusf/glow) - 易于使用的可扩展分布式大数据处理、Map-Reduce、DAG 执行，全部采用纯 Go 语言。
- [gmsec](https://github.com/gmsec/micro) - 一个Go分布式系统开发框架。
- [go-doudou](https://github.com/unionj-cloud/go-doudou) - 一个基于 Gossip 协议和 OpenAPI 3.0 规范的去中心化微服务框架。内置的 go-doudou cli 专注于低代码和快速开发，可以提高您的工作效率。
- [go-eagle](https://github.com/go-eagle/eagle) - 用于 API 或微服务的 Go 框架，带有方便的脚手架工具。
- [go-jump](https://github.com/dgryski/go-jump) - Google 的“Jump”一致性哈希函数的端口。
- [go-kit](https://github.com/go-kit/kit) - 微服务工具包，支持服务发现、负载均衡、可插拔传输、请求跟踪等。
- [go-micro](https://github.com/micro/go-micro) - 分布式系统开发框架。
- [go-mysql-lock](https://github.com/sanketplus/go-mysql-lock) - 基于MySQL的分布式锁。
- [go-pdu](https://github.com/pdupub/go-pdu) - 一个基于身份的去中心化社交网络。
- [go-sundheit](https://github.com/AppsFlyer/go-sundheit) - 一个库，旨在为 golang 服务定义异步服务运行状况检查提供支持。
- [go-zero](https://github.com/tal-tech/go-zero) - 一个 Web 和 RPC 框架。它的诞生是为了通过弹性设计确保繁忙站点的稳定性。内置的goctl大大提高了开发效率。
- [gorpc](https://github.com/valyala/gorpc) - 简单、快速且可扩展的 RPC 库，适用于高负载。
- [grpc-go](https://github.com/grpc/grpc-go) - gRPC的Go语言实现。基于 HTTP/2 的 RPC。
- [health](https://github.com/schigh/health) - 具有 Kubernetes 探针支持的 Go 服务运行状况检查器。
- [hprose](https://github.com/hprose/hprose-golang) - 非常新颖的 RPC 库，现在支持 25 种以上语言。
- [jsonrpc](https://github.com/osamingo/jsonrpc) - jsonrpc 包有助于实现 JSON-RPC 2.0。
- [jsonrpc](https://github.com/ybbus/jsonrpc) - JSON-RPC 2.0 HTTP 客户端实现。
- [K8gb](https://github.com/k8gb-io/k8gb) - 云原生 Kubernetes Global Balancer。
- [Kitex](https://github.com/cloudwego/kitex) - 一个高性能、强扩展性的Golang RPC框架，帮助开发者构建微服务。如果开发微服务时主要关注性能和可扩展性，Kitex 可能是一个不错的选择。
- [Kratos](https://github.com/go-kratos/kratos) - Go 中的模块化设计且易于使用的微服务框架。
- [liftbridge](https://github.com/liftbridge-io/liftbridge) - 用于 NATS 的轻量级容错消息流。
- [lock](https://github.com/ubgo/lock) - 具有 1 个 Go 接口和 5 个后端（filelock、flock、Redis、Postgres、etcd）的分布式锁系列 — 跨所有后端的隔离令牌、信号量模式和可观察性挂钩。
- [lura](https://github.com/luraproject/lura) - 具有中间件的超高性能 API 网关框架。
- [micro](https://github.com/micro/micro) - 适用于云及其他环境的分布式系统运行时。
- [mochi mqtt](https://github.com/mochi-co/mqtt) - 完全符合规范、可嵌入的高性能 MQTT v5/v3 代理，适用于 IoT、智能家居和 pubsub。
- [NATS](https://github.com/nats-io/nats-server) - NATS 是一种简单、安全且高性能的数字系统、服务和设备通信系统。
- [opentelemetry-go-auto-instrumentation](https://github.com/alibaba/opentelemetry-go-auto-instrumentation) - Golang 的 OpenTelemetry 编译时检测。
- [oras](https://github.com/oras-project/oras) - 容器注册表中 OCI 工件的 CLI 和库。
- [outbox](https://github.com/oagudo/outbox) - Go 中事务发件箱模式的轻量级库，不依赖于任何特定的关系数据库或代理。
- [outboxer](https://github.com/italolelis/outboxer) - Outboxer 是一个实现发件箱模式的 Go 库。
- [pglock](https://cirello.io/pglock) - PostgreSQL 支持的分布式锁定实现。
- [pjrpc](https://gitlab.com/pjrpc/pjrpc) - 具有 Protobuf 规范的 Golang JSON-RPC 服务器客户端。
- [raft](https://github.com/hashicorp/raft) - Raft 共识协议的 Golang 实现，由 HashiCorp 开发。
- [raft](https://github.com/etcd-io/raft) - Go 实现 Raft 共识协议，由 CoreOS 实现。
- [rain](https://github.com/cenkalti/rain) - BitTorrent 客户端和库。
- [redis-lock](https://github.com/bsm/redislock) - 使用 Redis 简化分布式锁定实现。
- [resgate](https://resgate.io/) - 实时 API 网关，用于构建 REST、实时和 RPC API，所有客户端均无缝同步。
- [rpcplatform](https://github.com/nexcode/rpcplatform) - 具有服务发现、负载平衡和相关功能的微服务框架。
- [rpcx](https://github.com/smallnest/rpcx) - 分布式可插拔RPC服务框架，如阿里巴巴Dubbo。
- [Semaphore](https://github.com/jexia/semaphore) - 一个简单的（微）服务编排器。
- [sleuth](https://github.com/ursiform/sleuth) - 用于 HTTP 服务之间的无主 p2p 自动发现和 RPC 的库（使用 [ZeroMQ](https://github.com/zeromq/libzmq)）。
- [sponge](https://github.com/zhufuyi/sponge) - 一个集成了自动代码生成、gin和grpc框架、基础开发框架的分布式开发框架。
- [Tarmac](https://github.com/tarmac-project/tarmac) - 使用 WebAssembly 编写函数、微服务或单体的框架
- [Temporal](https://github.com/temporalio/sdk-go) - 持久的执行系统使代码容错且简单。
- [torrent](https://github.com/anacrolix/torrent) - BitTorrent 客户端包。
- [trpc-go](https://github.com/trpc-group/trpc-go) - tRPC的Go语言实现，是一个可插拔的高性能RPC框架。

**[⬆ 回到顶部](#contents)**

## 动态域名解析

_更新动态 DNS 记录的工具。_

- [DDNS](https://github.com/skibish/ddns) - 以 Digital Ocean Networking DNS 作为后端的个人 DDNS 客户端。
- [dyndns](https://gitlab.com/alcastle/dyndns) - 后台 Go 进程会定期自动检查您的 IP 地址，并在您的地址发生变化时更新 Google 域的（一个或多个）动态 DNS 记录。
- [GoDNS](https://github.com/timothyye/godns) - 动态 DNS 客户端工具，支持 DNSPod 和 HE.net，用 Go 编写。

**[⬆ 回到顶部](#contents)**

## 电子邮件

_实现电子邮件创建和发送的库和工具。_

- [chasquid](https://blitiri.com.ar/p/chasquid) - 用 Go 编写的 SMTP 服务器。
- [douceur](https://github.com/aymerick/douceur) - HTML 电子邮件的 CSS 内联。
- [email](https://github.com/jordan-wright/email) - 一个强大且灵活的 Go 电子邮件库。
- [email-verifier](https://github.com/AfterShip/email-verifier) - 一个用于电子邮件验证的 Go 库，无需发送任何电子邮件。
- [go-dkim](https://github.com/toorop/go-dkim) - DKIM 库，用于签名和验证电子邮件。
- [go-email-normalizer](https://github.com/dimuska139/go-email-normalizer) - Golang 库，用于提供电子邮件地址的规范表示。
- [go-imap](https://github.com/BrianLeishman/go-imap) - 含电池 IMAP 客户端，具有自动重新连接、OAuth2、IDLE 支持和内置 MIME 解析功能。
- [go-imap](https://github.com/emersion/go-imap) - 用于客户端和服务器的 IMAP 库。
- [go-mail](https://github.com/wneessen/go-mail) - 一个简单的 Go 库，用于在 Go 中发送邮件。
- [go-message](https://github.com/emersion/go-message) - 用于互联网消息格式和邮件消息的流媒体库。
- [go-premailer](https://github.com/vanng822/go-premailer) - Go 中 HTML 邮件的内联样式。
- [go-simple-mail](https://github.com/xhit/go-simple-mail) - 非常简单的包，用于使用 SMTP Keep Alive 和两个超时发送电子邮件：连接和发送。
- [Hectane](https://github.com/hectane/hectane) - 提供 HTTP API 的轻量级 SMTP 客户端。
- [hermes](https://github.com/matcornic/hermes) - Golang 包，可生成干净、响应式的 HTML 电子邮件。
- [Maddy](https://github.com/foxcpp/maddy) - 一体化（SMTP、IMAP、DKIM、DMARC、MTA-STS、DANE）电子邮件服务器
- [mailchain](https://github.com/mailchain/mailchain) - 将加密的电子邮件发送到用 Go 编写的区块链地址。
- [mailgun-go](https://github.com/mailgun/mailgun-go) - 用于使用 Mailgun API 发送邮件的 Go 库。
- [MailHog](https://github.com/mailhog/MailHog) - 使用 Web 和 API 接口进行电子邮件和 SMTP 测试。
- [Mailpit](https://github.com/axllent/mailpit) - 面向开发人员的电子邮件和 SMTP 测试工具。
- [mailx](https://github.com/valord577/mailx) - Mailx 是一个可以更轻松地通过 SMTP 发送电子邮件的库。它是 golang 标准库“net/smtp”的增强。
- [mox](https://github.com/mjl-/mox) - 现代全功能安全邮件服务器，用于低维护、自托管电子邮件。
- [SendGrid](https://github.com/sendgrid/sendgrid-go) - SendGrid 用于发送电子邮件的 Go 库。
- [smtp](https://github.com/mailhog/smtp) - SMTP 服务器协议状态机。
- [smtpmock](https://github.com/mocktools/go-smtp-mock) - 轻量级可配置多线程假 SMTP 服务器。模拟您的测试环境的任何 SMTP 行为。
- [tickstem/verify](https://github.com/tickstem/verify) - 在电子邮件地址到达数据库之前对其进行验证：语法、MX 查找、一次性域和基于角色的收件箱。
- [truemail-go](https://github.com/truemail-rb/truemail-go) - 可配置的 Golang 电子邮件验证器/验证器。通过正则表达式、DNS、SMTP 等验证电子邮件。

**[⬆ 回到顶部](#contents)**

## 嵌入式脚本语言

_在你的 Go 代码中嵌入其他语言。_

- [anko](https://github.com/mattn/anko) - 用 Go 编写的脚本化解释器。
- [binder](https://github.com/alexeyco/binder) - 进入Lua绑定库，基于[gopher-lua](https://github.com/yuin/gopher-lua)。
- [cel-go](https://github.com/google/cel-go) - 快速、便携、非图灵完备的表达式评估，逐步打字。
- [ecal](https://github.com/krotik/ecal) - 一种简单的嵌入式脚本语言，支持并发事件处理。
- [expr](https://github.com/antonmedv/expr) - Go 的表达式求值引擎：快速、非图灵完备、动态类型、静态类型。
- [FrankenPHP](https://github.com/dunglas/frankenphp) - PHP 嵌入 Go，带有“net/http”处理程序。
- [gentee](https://github.com/gentee/gentee) - 可嵌入脚本编程语言。
- [gisp](https://github.com/jcla1/gisp) - Go 中的简单 LISP。
- [go-lua](https://github.com/Shopify/go-lua) - 将 Lua 5.2 VM 移植到纯 Go。
- [go-lua](https://github.com/speedata/go-lua) - 用纯 Go 实现的 Lua 5.4 VM。
- [go-php](https://github.com/deuill/go-php) - Go 的 PHP 绑定。
- [goal](https://codeberg.org/anaseto/goal) - 一种可嵌入的脚本数组语言。
- [goja](https://github.com/dop251/goja) - Go 中的 ECMAScript 5.1(+) 实现。
- [golua](https://github.com/aarzilli/golua) - Lua C API 的 Go 绑定。
- [gopher-lua](https://github.com/yuin/gopher-lua) - 用 Go 编写的 Lua 5.1 VM 和编译器。
- [gval](https://github.com/PaesslerAG/gval) - 一种用 Go 编写的高度可定制的表达式语言。
- [metacall](https://github.com/metacall/core) - 跨平台多语言运行时，支持 NodeJS、JavaScript、TypeScript、Python、Ruby、C#、WebAssembly、Java、Cobol 等。
- [ngaro](https://github.com/db47h/ngaro) - 可嵌入 Ngaro VM 实现，支持在 Retro 中编写脚本。
- [prolog](https://github.com/ichiban/prolog) - 嵌入式 Prolog。
- [purl](https://github.com/ian-kent/purl) - Perl 5.18.2 嵌入 Go 中。
- [starlark-go](https://github.com/google/starlark-go) - Starlark 的 Go 实现：类似 Python 的语言，具有确定性评估和密封执行。
- [starlet](https://github.com/1set/starlet) - [starlark-go](https://github.com/google/starlark-go) 的 Go 包装器，可简化脚本执行、提供数据转换以及有用的 Starlark 库和扩展。
- [tengo](https://github.com/d5/tengo) - Go 的字节码编译脚本语言。
- [Wa/凹语言](https://github.com/wa-lang/wa) - 嵌入 Go 的 Wa 编程语言。

**[⬆ 回到顶部](#contents)**

## 错误处理

_用于处理错误的库._

- [emperror](https://github.com/emperror/emperror) - Go 库和应用程序的错误处理工具和最佳实践。
- [eris](https://github.com/rotisserie/eris) - 在 Go 中处理、跟踪和记录错误的更好方法。与标准错误库和 github.com/pkg/errors 兼容。
- [errlog](https://github.com/snwfdhmp/errlog) - 可破解的包，用于确定错误的负责源代码（以及其他一些快速调试功能）。可就地插入任何记录器。
- [errors](https://github.com/emperror/errors) - 标准库错误包和 github.com/pkg/errors 的直接替换。提供各种错误处理原语。
- [errors](https://github.com/neuronlabs/errors) - 使用分类原语进行简单的 golang 错误处理。
- [errors](https://github.com/PumpkinSeed/errors) - 最简单的错误包装器，具有出色的性能和最小的内存开销。
- [errors](https://gitlab.com/tozd/go/errors) - 提供带有堆栈跟踪和可选结构化详细信息的错误。与 github.com/pkg/errors API 兼容，但不在内部使用它。
- [errors](https://github.com/naughtygopher/errors) - 内置 Go 错误的直接替换。这是一个最小的错误处理包，具有自定义错误类型、用户友好消息、Unwrap & Is。具有非常易于使用和简单的辅助功能。
- [errors](https://github.com/cockroachdb/errors) - Go 错误库具有通过网络的错误可移植性。
- [errorx](https://github.com/joomcode/errorx) - 一个功能丰富的错误包，包含堆栈跟踪、错误组合等。
- [exception](https://github.com/rbrahul/exception) - 一个简单的实用程序包，用于在 Golang 中使用 try-catch 进行异常处理。
- [go-errr](https://github.com/go-errr/go) - 具有 Catch/Recover 语义、包装错误链和 Go 堆栈跟踪的错误处理库。
- [Falcon](https://github.com/SonicRoshan/falcon) - 一个简单但功能强大的错误处理包。
- [Fault](https://github.com/Southclaws/fault) - 一种用于包装错误的人体工程学机制，以促进错误值的结构化元数据和上下文。
- [go-multierror](https://github.com/hashicorp/go-multierror) - Go (golang) 包，用于将错误列表表示为单个错误。
- [metaerr](https://github.com/quantumcycle/metaerr) - 一个库，用于创建自定义错误生成器，使用来自不同来源的元数据和可选的堆栈跟踪生成结构化错误。
- [multierr](https://github.com/uber-go/multierr) - 用于将错误列表表示为单个错误的包。
- [oops](https://github.com/samber/oops) - 使用上下文、堆栈跟踪和源片段进行错误处理。
- [tracerr](https://github.com/ztrue/tracerr) - 带有堆栈跟踪和源片段的 Golang 错误。

**[⬆ 回到顶部](#contents)**

## 文件处理

_用于处理文件和文件系统的库._

- [afero](https://github.com/spf13/afero) - Go 的文件系统抽象系统。
- [afs](https://github.com/viant/afs) - Go 的抽象文件存储（mem、scp、zip、tar、云：s3、gs）。
- [baraka](https://github.com/xis/baraka) - 一个轻松处理http文件上传的库。
- [checksum](https://github.com/codingsince1985/checksum) - 计算大型文件的消息摘要，例如 MD5、SHA256、SHA1、CRC 或 BLAKE2。
- [copy](https://github.com/otiai10/copy) - 递归复制目录。
- [fastwalk](https://github.com/charlievieth/fastwalk) - 快速并行目录遍历库（由[fzf](https://github.com/junegunn/fzf)使用）。
- [flop](https://github.com/homedepot/flop) - 文件操作库旨在镜像与 [GNU cp](https://www.gnu.org/software/coreutils/manual/html_node/cp-inspiration.html) 的功能奇偶校验。
- [gdu](https://github.com/dundee/gdu) - 带有控制台界面的磁盘使用分析器。
- [go-csv-tag](https://github.com/artonge/go-csv-tag) - 使用标签加载 csv 文件。
- [go-decent-copy](https://github.com/hugocarreira/go-decent-copy) - 为人类复制文件。
- [go-exiftool](https://github.com/barasher/go-exiftool) - Go 绑定 ExifTool，这是一个著名的库，用于从文件（图片、PDF、office 等）中提取尽可能多的元数据（EXIF、IPTC 等）。
- [go-gtfs](https://github.com/artonge/go-gtfs) - 在 go 中加载 gtfs 文件。
- [go-wkhtmltopdf](https://github.com/SebastiaanKlippert/go-wkhtmltopdf) - 将 HTML 模板转换为 PDF 文件的包。
- [gofs](https://github.com/no-src/gofs) - 开箱即用的跨平台实时文件同步工具。
- [gulter](https://github.com/adelowo/gulter) - 一个简单的 HTTP 中间件，可自动处理您所有的文件上传需求
- [gut/yos](https://github.com/1set/gut) - 简单可靠的文件操作包，例如文件、目录和符号链接的复制/移动/差异/列表。
- [gxpdf](https://github.com/coregx/gxpdf) - 适用于 Go 的现代全生命周期 PDF 库 — 解析、提取表格、生成和签署具有零 CGO 依赖性的文档。
- [higgs](https://github.com/dastoori/higgs) - 一个小型的跨平台 Go 库，用于隐藏/取消隐藏文件和目录。
- [iso9660](https://github.com/kdomanski/iso9660) - 用于读取和创建 ISO9660 磁盘映像的包
- [notify](https://github.com/rjeczalik/notify) - 文件系统事件通知库，具有简单的 API，类似于 os/signal。
- [opc](https://github.com/qmuntal/opc) - 加载 Go 的开放打包约定 (OPC) 文件。
- [parquet](https://github.com/parsyl/parquet) - 读取和写入 [parquet](https://parquet.apache.org) 文件。
- [pathtype](https://github.com/jonchun/pathtype) - 将路径视为其自己的类型，而不是使用字符串。
- [pdfcpu](https://github.com/pdfcpu/pdfcpu) - PDF 处理器。
- [skywalker](https://github.com/dixonwille/skywalker) - 打包以允许同时轻松地浏览文件系统。
- [todotxt](https://github.com/1set/todotxt) - Gina Trapani 的 [_todo.txt_](http://todotxt.org/) 文件的 Go 库，支持解析和操作 [_todo.txt_ 格式](https://github.com/todotxt/todo.txt) 的任务列表。
- [vfs](https://github.com/C2FO/vfs) - Go 的一组可插入、可扩展且固定的文件系统功能，适用于多种文件系统类型，例如 os、S3 和 GCS。

**[⬆ 回到顶部](#contents)**

## 金融

_会计和财务软件包._

- [accounting](https://github.com/leekchan/accounting) - golang 的货币和货币格式。
- [ach](https://github.com/moov-io/ach) - 自动清算所 (ACH) 文件的读取器、写入器和验证器。
- [bbgo](https://github.com/c9s/bbgo) - 用 Go 编写的加密货币交易机器人框架。包括常见的加密货币交易所API、标准指标、回测和许多内置策略。
- [currency](https://github.com/bojanz/currency) - 处理货币金额，提供货币信息和格式。
- [currency](https://github.com/naughtygopher/currency) - 高性能且准确的货币计算包。
- [dec128](https://github.com/jokruger/dec128) - 高性能 128 位定点十进制数。
- [decimal](https://github.com/shopspring/decimal) - 任意精度定点十进制数。
- [decimal](https://github.com/aytechnet/decimal) - 高性能64位十进制部分兼容[shopspring/decimal](https://github.com/shopspring/decimal)和int64，包括重量和长度。
- [decimal](https://github.com/govalues/decimal) - 具有无恐慌算术的不可变十进制数。
- [fpdecimal](https://github.com/nikolaydubina/fpdecimal) - 小定点小数的快速、精确的序列化和算术
- [fpmoney](https://github.com/nikolaydubina/fpmoney) - 快速简单的 ISO4217 定点十进制货币。
- [go-finance](https://github.com/alpeb/go-finance) - 用于货币时间价值（年金）、现金流、利率转换、债券和折旧计算的金融函数库。
- [go-finance](https://github.com/pieterclaerhout/go-finance) - 用于获取汇率、通过 VIES 检查增值税号以及检查 IBAN 银行帐号的模块。
- [go-money](https://github.com/rhymond/go-money) - 福勒货币模式的实施。
- [coinpaprika-api-go-client](https://github.com/coinpaprika/coinpaprika-api-go-client) - CoinPaprika 加密货币市场数据 API 的 Go 客户端。
- [go-nowpayments](https://github.com/matm/go-nowpayments) - 加密 NOWPayments API 的库。
- [gobl](https://github.com/invopop/gobl) - 发票和计费文档框架。基于 JSON 模式。自动执行税务计算和验证，并提供转换为全球格式的工具。
- [indicator](https://github.com/cinar/indicator) - 技术分析库提供财务指标、策略和回测框架。
- [ledger](https://github.com/formancehq/ledger) - 可编程财务分类账，为资金转移应用程序提供基础。
- [money](https://github.com/govalues/money) - 不可变的货币金额和汇率，具有无恐慌的算术。
- [ofxgo](https://github.com/aclindsa/ofxgo) - 查询 OFX 服务器和/或解析响应（使用示例命令行客户端）。
- [orderbook](https://github.com/i25959341/orderbook) - Golang 限价订单簿匹配引擎。
- [payme](https://github.com/jovandeginste/payme) - 用于 SEPA 付款的 QR 代码生成器（ASCII 和 PNG）。
- [paystack-sdk-go](https://github.com/samaasi/paystack-sdk-go) - 适用于 Paystack API 的全面、零依赖、完全类型化的 Go SDK。
- [swift](https://code.pfad.fr/swift/) - IBAN（国际银行帐号）的离线有效性检查和 BIC 检索（对于某些国家/地区）。
- [techan](https://github.com/sdcoffey/techan) - 技术分析库具有先进的市场分析和交易策略。
- [ticker](https://github.com/achannarasappa/ticker) - 终端股票观察者和股票仓位跟踪器。
- [transaction](https://github.com/claygod/transaction) - 嵌入式账户事务数据库，以多线程模式运行。
- [udecimal](https://github.com/quagmt/udecimal) - 适用于金融应用的高性能、高精度、零分配定点小数库。
- [vat](https://github.com/dannyvankooten/vat) - 增值税号验证和欧盟增值税税率。

**[⬆ 回到顶部](#contents)**

## 表格

_用于处理表单的库._

- [bind](https://github.com/robfig/bind) - 将表单数据绑定到任何 Go 值。
- [checker](https://github.com/cinar/checker) - Checker 通过结构标记中定义的规则或直接通过函数帮助验证用户输入。
- [conform](https://github.com/leebenson/conform) - 保持用户输入的检查。根据结构标签修剪、清理和清理数据。
- [form](https://github.com/go-playground/form) - 将 url.Values 解码为 Go 值并将 Go 值编码为 url.Values。双阵列和全地图支持。
- [formam](https://github.com/monoculum/formam) - 将表单的值解码为结构。
- [forms](https://github.com/albrow/forms) - 与框架无关的库，用于解析和验证支持多部分表单和文件的表单/JSON 数据。
- [gbind](https://github.com/bdjimmy/gbind) - 将数据绑定到任何 Go 值。可以使用内置和自定义表达式绑定功能；支持数据验证
- [gorilla/csrf](https://github.com/gorilla/csrf) - 针对 Go Web 应用程序和服务的 CSRF 保护。
- [httpin](https://github.com/ggicci/httpin) - 将 HTTP 请求解码为自定义结构，包括查询字符串、表单、HTTP 标头等。
- [nosurf](https://github.com/justinas/nosurf) - Go 的 CSRF 保护中间件。
- [qs](https://github.com/sonh/qs) - 用于将结构编码为 URL 查询参数的 Go 模块。
- [queryparam](https://github.com/tomwright/queryparam) - 将 `url.Values` 解码为标准或自定义类型的可用结构值。
- [roamer](https://github.com/slipros/roamer) - 通过使用简单的标签将 cookie、标头、查询参数、路径参数、主体绑定到结构体等，消除了用于解析 HTTP 请求的样板代码。

**[⬆ 回到顶部](#contents)**

## 功能性

_支持 Go 中函数式编程的包._

- [fp-go](https://github.com/repeale/fp-go) - 由 Golang 1.18+ 泛型提供支持的函数式编程助手集合。
- [fpGo](https://github.com/TeaEntityLab/fpGo) - Monad，Golang 的函数式编程功能。
- [fuego](https://github.com/seborama/fuego) - Go 中的功能实验。
- [FuncFrog](https://github.com/koss-null/FuncFrog) - 功能帮助程序库在通用切片 Go1.18+ 上提供 Map、Filter、Reduce 和其他流操作，并具有惰性评估和错误处理机制。
- [g](https://github.com/enetx/g) - Go 的函数式编程框架。
- [go-functional](https://github.com/BooleanCat/go-functional) - Go 中使用泛型的函数式编程
- [go-underscore](https://github.com/tobyhede/go-underscore) - 有用的 Go 集合实用程序的有用集合。
- [gofp](https://github.com/rbrahul/gofp) - 类似 lodash 的强大 Golang 实用程序库。
- [mo](https://github.com/samber/mo) - Monad 和流行的 FP 抽象，基于 Go 1.18+ 泛型（Option、Result、Either...）。
- [underscore](https://github.com/rjNemo/underscore) - 适用于 Go 1.18 及更高版本的函数式编程助手。
- [valor](https://github.com/phelmkamp/valor) - 可以选择包含值的通用选项和结果类型。

**[⬆ 回到顶部](#contents)**

## 游戏开发

_很棒的游戏开发库._

- [Ark](https://github.com/mlange-42/ark) - 用于 Go 的基于原型的实体组件系统 (ECS)。
- [Ebitengine](https://github.com/hajimehoshi/ebiten) - Go 中非常简单的 2D 游戏引擎。
- [ecs](https://github.com/andygeiss/ecs) - 基于 Golang 中的实体组件系统概念构建您自己的游戏引擎。
- [engo](https://github.com/EngoEngine/engo) - Engo 是一个用 Go 编写的开源 2D 游戏引擎。它遵循实体-组件-系统范例。
- [fantasyname](https://github.com/s0rg/fantasyname) - 幻想名称生成器。
- [g3n](https://github.com/g3n/engine) - Go 3D 游戏引擎。
- [go-astar](https://github.com/beefsack/go-astar) - A\* 寻路算法的 Go 实现。
- [go-sdl2](https://github.com/veandco/go-sdl2) - 转到 [Simple DirectMedia Layer](https://www.libsdl.org/) 的绑定。
- [go3d](https://github.com/ungerik/go3d) - 面向性能的 Go 2D/3D 数学包。
- [gogpu](https://github.com/gogpu/gogpu) - 基于 WebGPU 构建的具有窗口、输入和渲染功能的 GPU 应用程序框架 — 将 480 多行 GPU 代码减少到约 20 行，零 CGO（GoGPU 生态系统：[gg](https://github.com/gogpu/gg)、[ui](https://github.com/gogpu/ui)、[wgpu](https://github.com/gogpu/wgpu)、[naga](https://github.com/gogpu/naga)）。
- [gogpu/wgpu](https://github.com/gogpu/wgpu) - 使用 Vulkan、DX12 和 Metal 后端的 Pure Go WebGPU 实现，零 CGO（[GoGPU](https://github.com/gogpu) 生态系统的一部分）。
- [GOKe](https://github.com/kjkrol/goke) - 面向数据 (DOD)、基于原型的 ECS 引擎，利用 L1 缓存对齐的分块 SoA 布局，实现可预测、无级内存增长和零分配执行路径。
- [gonet](https://github.com/xtaci/gonet) - 使用 golang 实现的游戏服务器骨架。
- [goworld](https://github.com/xiaonanln/goworld) - 可扩展的游戏服务器引擎，具有空间实体框架和热插拔功能。
- [grid](https://github.com/s0rg/grid) - 具有光线投射、阴影投射和路径查找功能的通用 2D 网格。
- [Leaf](https://github.com/name5566/leaf) - 轻量级游戏服务器框架。
- [nano](https://github.com/lonng/nano) - 轻量级、实用、高性能的基于 golang 的游戏服务器框架。
- [Oak](https://github.com/oakmound/oak) - 纯围棋游戏引擎。
- [Pi](https://github.com/elgopher/pi) - 用于为现代计算机创建复古游戏的游戏引擎。受 Pico-8 启发并由 Ebitengine 提供支持。
- [Pitaya](https://github.com/topfreegames/pitaya) - 可扩展的游戏服务器框架，通过 C SDK 提供集群支持和适用于 iOS、Android、Unity 等的客户端库。
- [Pixel](https://github.com/gopxl/pixel) - 用 Go 手工制作的 2D 游戏库。
- [prototype](https://github.com/gonutz/prototype) - 用于使用最少的 API 创建桌面游戏的跨平台 (Windows/Linux/Mac) 库。
- [raylib-go](https://github.com/gen2brain/raylib-go) - Go 绑定 [raylib](https://www.raylib.com/)，一个简单易用的库，用于学习视频游戏编程。
- [termloop](https://github.com/JoelOtter/termloop) - 基于终端的 Go 游戏引擎，构建于 Termbox 之上。
- [tile](https://github.com/kelindar/tile) - 面向数据且缓存友好的 2D 网格库 (TileMap)，包括寻路、观察器和导入/导出。

**[⬆ 回到顶部](#contents)**

## 发电机

_生成 Go 代码的工具._

- [convergen](https://github.com/reedom/convergen) - 功能丰富的类型间复制代码生成器。
- [copygen](https://github.com/switchupcb/copygen) - 生成基于 Go 类型的任何代码，包括默认情况下不进行反射的类型到类型转换器（复制代码）。
- [generis](https://github.com/senselogic/GENERIS) - 代码生成工具提供泛型、自由格式宏、条件编译和 HTML 模板。
- [go-enum](https://github.com/abice/go-enum) - 从代码注释生成枚举的代码。
- [go-enum-encoding](https://github.com/nikolaydubina/go-enum-encoding) - 从代码注释生成枚举编码的代码。
- [go-apispec](https://github.com/antst/go-apispec) - 通过静态分析和自动框架检测，从 Go 源代码生成 OpenAPI 3.1 规范。
- [go-linq](https://github.com/ahmetalpbalkan/go-linq) - Go 的类似于 .NET LINQ 的查询方法。
- [goderive](https://github.com/awalterschulze/goderive) - 从输入类型派生函数
- [goverter](https://github.com/jmattheis/goverter) - 通过定义接口生成转换器。
- [GoWrap](https://github.com/hexdigest/gowrap) - 使用简单的模板为 Go 接口生成装饰器。
- [interfaces](https://github.com/rjeczalik/interfaces) - 用于生成接口定义的命令行工具。
- [jennifer](https://github.com/dave/jennifer) - 无需模板即可生成任意 Go 代码。
- [oapi-codegen](https://github.com/deepmap/oapi-codegen) - 该包包含一组实用程序，用于根据 OpenAPI 3.0 API 定义为服务生成 Go 样板代码。
- [protoc-gen-httpgo](https://github.com/MUlt1mate/protoc-gen-httpgo) - 从 protobuf 生成 HTTP 服务器和客户端。
- [typeregistry](https://github.com/xiaoxin01/typeregistry) - 动态创建类型的库。

**[⬆ 回到顶部](#contents)**

## 地理

_地理工具和服务器_

- [borders](https://github.com/kpfaulkner/borders) - 检测图像边框并转换为 GeoJSON 以进行 GIS 操作。
- [geoos](https://github.com/spatial-go/geoos) - 库提供空间数据和几何算法。
- [geoserver](https://github.com/hishamkaram/geoserver) - geoserver 是一个 Go 包，用于通过 GeoServer REST API 操作 GeoServer 实例。
- [gismanager](https://github.com/hishamkaram/gismanager) - 将您的 GIS 数据（矢量数据）发布到 PostGIS 和 Geoserver。
- [godal](https://github.com/airbusgeo/godal) - 去包装 GDAL。
- [H3](https://github.com/uber/h3-go) - H3 的 Go 绑定，这是一个分层六边形地理空间索引系统。
- [H3 GeoJSON](https://github.com/mmadfox/go-geojson2h3) - H3 索引和 GeoJSON 之间的转换实用程序。
- [H3GeoDist](https://github.com/mmadfox/go-h3geo-dist) - Uber H3geo 单元按虚拟节点的分布。
- [mbtileserver](https://github.com/consbio/mbtileserver) - 一个简单的基于 Go 的服务器，用于以 mbtiles 格式存储的地图图块。
- [osm](https://github.com/paulmach/osm) - 用于读取、写入和使用 OpenStreetMap 数据和 API 的库。
- [pbf](https://github.com/maguro/pbf) - OpenStreetMap PBF golang 编码器/解码器。
- [S2 geojson](https://github.com/pantrif/s2-geojson) - 将 geojson 转换为 s2 单元并在地图上演示一些 S2 几何特征。
- [S2 geometry](https://github.com/golang/geo) - Go 中的 S2 几何库。
- [simplefeatures](https://github.com/peterstace/simplefeatures) - simplesfeatures 是一个 2D 几何库，它提供了对几何进行建模的 Go 类型以及对其进行操作的算法。
- [Tile38](https://github.com/tidwall/tile38) - 具有空间索引和实时地理围栏的地理定位数据库。
- [Web-Mercator-Projection](https://github.com/jorelosorio/web-mercator-projection) 一个项目，可轻松使用和转换 LonLat、Point 和 Tile，以使用 Web Mercator 投影在地图中显示信息、标记等。
- [WGS84](https://github.com/wroge/wgs84) - 坐标转换和转换库（ETRS89、OSGB36、NAD83、RGF93、Web Mercator、UTM）。

**[⬆ 回到顶部](#contents)**

## Go编译器

_用于编译 Go 到其他语言的工具，反之亦然。_

- [bunster](https://github.com/yassinebenaid/bunster) - 将 shell 脚本编译为 Go。
- [c4go](https://github.com/Konstantin8105/c4go) - 将 C 代码转换为 Go 代码。
- [cxgo](https://github.com/gotranspile/cxgo) - 将 C 代码转换为 Go 代码。
- [esp32](https://github.com/andygeiss/esp32-transpiler) - 转译进入 Arduino 代码。
- [f4go](https://github.com/Konstantin8105/f4go) - 将 FORTRAN 77 代码转换为 Go 代码。
- [go2hx](https://github.com/go2hx/go2hx) - 编译器从 Go 到 Haxe 到 Javascript/C++/Java/C#。
- [gopherjs](https://github.com/gopherjs/gopherjs) - 从 Go 到 JavaScript 的编译器。

**[⬆ 回到顶部](#contents)**

## Goroutine

_管理和使用 Goroutines 的工具._

- [anchor](https://github.com/kyuff/anchor) - 用于管理微服务架构中组件生命周期的库。
- [ants](https://github.com/panjf2000/ants) - Go 中的高性能、低成本的 goroutine 池。
- [artifex](https://github.com/borderstech/artifex) - 使用基于工作线程的调度的简单 Golang 内存作业队列。
- [async](https://github.com/yaitoo/async) - 具有 async/await 风格的 Go 异步任务包。
- [async](https://github.com/reugn/async) - Go 的替代同步库（Future、Promise、Locks）。
- [async](https://github.com/studiosol/async) - 一种异步执行函数的安全方法，可以在出现紧急情况时恢复它们。
- [async-job](https://github.com/lab210-dev/async-job) - AsyncJob 是一个异步队列作业管理器，代码轻、清晰、速度快。
- [breaker](https://github.com/kamilsk/breaker) - 灵活的机制使执行流程可中断。
- [channelify](https://github.com/ddelizia/channelify) - 将您的函数转换为返回通道，以实现简单而强大的并行处理。
- [conc](https://github.com/sourcegraph/conc) - `conc` 是 Go 中结构化并发的工具带，使常见任务变得更容易、更安全。
- [concurrency-limiter](https://github.com/vivek-ng/concurrency-limiter) - 支持超时、动态优先级和 goroutine 上下文取消的并发限制器。
- [conexec](https://github.com/ITcathyh/conexec) - 一个并发工具包，可帮助以高效、安全的方式同时执行函数。它支持指定整体超时以避免阻塞，并使用goroutine池来提高效率。
- [cyclicbarrier](https://github.com/marusama/cyclicbarrier) - golang 的 CyclicBarrier。
- [execpool](https://github.com/hexdigest/execpool) - 围绕 exec.Cmd 构建的池，提前启动给定数量的进程，并在需要时将 stdin 和 stdout 附加到它们。与 FastCGI 或 Apache Prefork MPM 非常相似，但适用于任何命令。
- [flowmatic](https://github.com/carlmjohnson/flowmatic) - 结构化并发变得简单。
- [go-accumulator](https://github.com/nar10z/go-accumulator) - 事件累积及其后续处理的解决方案。
- [go-actor](https://github.com/vladopajic/go-actor) - 一个使用 Actor 模型编写并发程序的小型库。
- [go-floc](https://github.com/workanator/go-floc) - 轻松编排 goroutine。
- [go-flow](https://github.com/kamildrazkiewicz/go-flow) - 控制 goroutine 的执行顺序。
- [go-tools/multithreading](https://github.com/nikhilsaraf/go-tools) - 使用这个轻量级库和简单的 API 来管理 goroutine 池。
- [go-trylock](https://github.com/subchen/go-trylock) - TryLock 对 Golang 读写锁的支持。
- [go-waitgroup](https://github.com/pieterclaerhout/go-waitgroup) - 就像具有错误处理和并发控制的“sync.WaitGroup”。
- [go-workerpool](https://github.com/zenthangplus/go-workerpool) - Go WorkerPool 受到 Java 线程池的启发，旨在控制繁重的 Go 例程。
- [goccm](https://github.com/zenthangplus/goccm) - Go Concurrency Manager 包限制了允许同时运行的 goroutine 数量。
- [gohive](https://github.com/loveleshsharma/gohive) - 一个高性能且易于使用的 Go Goroutine 池。
- [gollback](https://github.com/vardius/gollback) - 异步简单函数实用程序，用于管理闭包和回调的执行。
- [gowl](https://github.com/hamed-yousefi/gowl) - Gowl 是一个流程管理和流程监控工具。无限工作池使您能够控制池和进程并监控其状态。
- [goworker](https://github.com/benmanns/goworker) - goworker 是一个基于 Go 的后台工作者。
- [gowp](https://github.com/xxjwxc/gowp) - gowp 是并发限制 goroutine 池。
- [gpool](https://github.com/Sherifabdlnaby/gpool) - 管理一个可调整大小的上下文感知 goroutine 池来绑定并发。
- [grpool](https://github.com/ivpusic/grpool) - 轻量级 Goroutine 池。
- [hands](https://github.com/duanckham/hands) - 进程控制器，用于控制多个goroutine的执行和返回策略。
- [Hunch](https://github.com/AaronJan/Hunch) - Hunch提供了“All”、“First”、“Retry”、“Waterfall”等功能，使异步流程控制更加直观。
- [kyoo](https://github.com/dirkaholic/kyoo) - 提供无限的作业队列和并发工作池。
- [neilotoole/errgroup](https://github.com/neilotoole/errgroup) - `sync/errgroup` 的直接替代方案，仅限于 N 个工作协程池。
- [nursery](https://github.com/arunsworld/nursery) - Go 中的结构化并发。
- [oversight](https://pkg.go.dev/cirello.io/oversight) - 监督是 Erlang 监督树的完整实现。
- [parallel-fn](https://github.com/rafaeljesus/parallel-fn) - 并行运行函数。
- [pond](https://github.com/alitto/pond) - 用 Go 编写的简约且高性能的 goroutine 工作池。
- [pool](https://github.com/go-playground/pool) - 有限的消费者 Goroutine 或无限的 Goroutine 池，以便更轻松地处理和取消 Goroutine。
- [rill](https://github.com/destel/rill) - 用于实现干净、可组合、基于通道的并发的 Go 工具包。
- [routine](https://github.com/timandy/routine) - `routine` 是 go 库的一个 `ThreadLocal`。它封装并提供了一些易用、非竞争、高性能的“goroutine”上下文访问接口，可以帮助你更优雅地访问协程上下文信息。
- [routine](https://github.com/x-mod/routine) - 带上下文的 go 例程控制，支持：Main、Go、Pool 和一些有用的 Executors。
- [semaphore](https://github.com/kamilsk/semaphore) - 信号量模式实现，具有基于通道和上下文的锁定/解锁操作超时。
- [semaphore](https://github.com/marusama/semaphore) - 基于 CAS 的快速可调整大小的信号量实现（比基于通道的信号量实现更快）。
- [stl](https://github.com/ssgreg/stl) - 基于软件事务内存（STM）并发控制机制的软件事务锁。
- [threadpool](https://github.com/shettyh/threadpool) - Golang 线程池实现。
- [tunny](https://github.com/Jeffail/tunny) - golang 的 Goroutine 池。
- [worker-pool](https://github.com/vardius/worker-pool) - goworker 是一个 Go 简单的异步工作池。
- [workerpool](https://github.com/gammazero/workerpool) - Goroutine 池限制任务执行的并发度，而不是排队的任务数量。
- [autopool](https://github.com/AshvinBambhaniya/autopool) - 用于 Go 的零配置、自动扩展工作池，具有优先级感知调度功能。

**[⬆ 回到顶部](#contents)**

## 图形用户界面

_用于构建 GUI 应用程序的库._

_工具包_

- [app](https://github.com/murlokswarm/app) - 打包以使用 GO、HTML 和 CSS 创建应用程序。支持：MacOS、Windows 正在进行中。
- [cimgui-go](https://github.com/AllenDang/cimgui-go) - 通过 [cimgui](https://github.com/cimgui/cimgui) 自动生成 [Dear ImGui](https://github.com/ocornut/imgui) 的 Go 包装器。
- [Cogent Core](https://github.com/cogentcore/core) - 用于构建在 macOS、Windows、Linux、iOS、Android 和 Web 上运行的 2D 和 3D 应用程序的框架。
- [DarwinKit](https://github.com/progrium/darwinkit) - 使用 Go 构建本机 macOS 应用程序。
- [energy](https://github.com/energye/energy) - 基于LCL（本机系统UI控制库）和CEF（Chromium嵌入式框架）的跨平台（Windows / macOS / Linux）
- [fyne](https://github.com/fyne-io/fyne) - 基于 Material Design 为 Go 设计的跨平台原生 GUI。支持：Linux、macOS、Windows、BSD、iOS 和 Android。
- [gio](https://gioui.org) - Gio 是一个用 Go 编写跨平台即时模式 GUI 的库。 Gio 支持所有主要平台：Linux、macOS、Windows、Android、iOS、FreeBSD、OpenBSD 和 WebAssembly。
- [go-gtk](https://mattn.github.io/go-gtk/) - GTK 的 Go 绑定。
- [go-sciter](https://github.com/sciter-sdk/go-sciter) - Sciter 的 Go 绑定：用于现代桌面 UI 开发的嵌入式 HTML/CSS/脚本引擎。跨平台。
- [Goey](https://bitbucket.org/rj/goey/src/master/) - 适用于 Windows / Linux / Mac 的跨平台 UI 工具包聚合器。 GTK、可可、Windows API
- [gogpu/ui](https://github.com/gogpu/ui) - GPU 加速的 GUI 工具包，包含 22 个小部件、3 个设计系统（Material、Fluent、Cupertino）、反应信号和零 CGO（[GoGPU](https://github.com/gogpu) 生态系统的一部分）。
- [goradd/html5tag](https://github.com/goradd/html5tag) - 用于输出 HTML5 标签的库。
- [gotk3](https://github.com/gotk3/gotk3) - GTK3 的 Go 绑定。
- [gowd](https://github.com/dtylman/gowd) - 使用 GO、HTML、CSS 和 NW.js 进行快速、简单的桌面 UI 开发。跨平台。
- [proton](https://github.com/CzaxStudio/proton) - Pure Go 立即模式 GUI 框架构建在 Gio 上，具有零 Cgo 依赖性。
- [qt](https://github.com/therecipe/qt) - Go 的 Qt 绑定（支持 Windows / macOS / Linux / Android / iOS / Sailfish OS / Raspberry Pi）。
- [Spot](https://github.com/roblillack/spot) - 反应式跨平台桌面 GUI 工具包。
- [ui](https://github.com/andlabs/ui) - Go 的平台本机 GUI 库。跨平台。
- [unison](https://github.com/richardwilkes/unison) - 用于 Go 桌面应用程序的统一图形用户体验工具包。支持 macOS、Windows 和 Linux。
- [Wails](https://wails.io) - Mac、Windows、Linux 桌面应用程序，具有使用内置操作系统 HTML 渲染器的 HTML UI。
- [walk](https://github.com/lxn/walk) - 适用于 Go 的 Windows 应用程序库套件。
- [webview](https://github.com/zserge/webview) - 具有简单双向 JavaScript 绑定的跨平台 Web 视图窗口（Windows / macOS / Linux）。

_互动_

- [AppIndicator Go](https://github.com/gopherlibs/appindicator) - libappindicator3 C 库的 Go 绑定。
- [gogpu/systray](https://github.com/gogpu/systray) - 适用于 Windows、macOS 和 Linux 的 Pure Go 系统托盘库，具有零 CGO（[GoGPU](https://github.com/gogpu) 生态系统的一部分）。
- [gosx-notifier](https://github.com/deckarep/gosx-notifier) - 适用于 Go 的 OSX 桌面通知库。
- [mac-activity-tracker](https://github.com/prashantgupta24/activity-tracker) - OSX 库用于通知计算机上的任何（可插入）活动。
- [mac-sleep-notifier](https://github.com/prashantgupta24/mac-sleep-notifier) - golang 中的 OSX 睡眠/唤醒通知。
- [robotgo](https://github.com/go-vgo/robotgo) - Go Native 跨平台 GUI 系统自动化。控制鼠标、键盘等。
- [systray](https://github.com/getlantern/systray) - 跨平台 Go 库在通知区域放置图标和菜单。
- [trayhost](https://github.com/shurcooL/trayhost) - 跨平台 Go 库，用于在主机操作系统的任务栏中放置图标。
- [zenity](https://github.com/ncruces/zenity) - 跨平台 Go 库和 CLI，用于创建与用户进行图形交互的简单对话框。

**[⬆ 回到顶部](#contents)**

## 硬件

_与硬件交互的库、工具和教程。_

- [arduino-cli](https://github.com/arduino/arduino-cli) - 官方 Arduino CLI 和库。可以独立运行，也可以合并到更大的 Go 项目中。
- [emgo](https://github.com/ziutek/emgo) - 用于编程嵌入式系统（例如 STM32 MCU）的类 Go 语言。
- [ghw](https://github.com/jaypipes/ghw) - Golang 硬件发现/检查库。
- [go-osc](https://github.com/hypebeast/go-osc) - 打开 Go 的声音控制 (OSC) 绑定。
- [go-rpio](https://github.com/stianeikeland/go-rpio) - Go 的 GPIO，不需要 cgo。
- [goroslib](https://github.com/aler9/goroslib) - Go 的机器人操作系统 (ROS) 库。
- [joystick](https://github.com/0xcafed00d/joystick) - 用于读取附加操纵杆状态的轮询 API。
- [moody](https://github.com/dinakars777/moody) - 适用于 macOS 的硬件事件个性守护程序。监控 USB、充电器、盖子和其他硬件事件，并以可定制的个性进行响应。
- [sysinfo](https://github.com/zcalusic/sysinfo) - 一个纯 Go 库，提供 Linux 操作系统/内核/硬件系统信息。

**[⬆ 回到顶部](#contents)**

## 图片

_用于操作图像的库._

- [bild](https://github.com/anthonynsimon/bild) - 纯 Go 语言的图像处理算法集合。
- [bimg](https://github.com/h2non/bimg) - 使用 libvips 进行快速高效图像处理的小软件包。
- [cameron](https://github.com/aofei/cameron) - Go 的头像生成器。
- [canvas](https://github.com/tdewolff/canvas) - 矢量图形转换为 PDF、SVG 或光栅化图像。
- [color-extractor](https://github.com/marekm4/color-extractor) - 没有外部依赖性的主颜色提取器。
- [darkroom](https://github.com/gojek/darkroom) - 具有可变存储后端和图像处理引擎的图像代理，重点关注速度和弹性。
- [geopattern](https://github.com/pravj/geopattern) - 从字符串创建美丽的生成图像图案。
- [gg](https://github.com/fogleman/gg) - 纯 Go 中的 2D 渲染。
- [gift](https://github.com/disintegration/gift) - 图像处理过滤器包。
- [gltf](https://github.com/qmuntal/gltf) - 高效且强大的 glTF 2.0 读取器、写入器和验证器。
- [go-cairo](https://github.com/ungerik/go-cairo) - 去绑定 cairo 图形库。
- [go-gd](https://github.com/bolknote/go-gd) - 去绑定GD库。
- [go-nude](https://github.com/koyachi/go-nude) - 使用 Go 进行裸体检测。
- [go-qrcode](https://github.com/yeqown/go-qrcode) - 生成具有个性化样式的二维码，允许调整颜色、块大小、形状和图标。
- [go-webcolors](https://github.com/jyotiska/go-webcolors) - webcolors 库从 Python 到 Go 的移植。
- [go-webp](https://github.com/kolesa-team/go-webp) - 使用 libwebp 对 webp 图片进行编码和解码的库。
- [gocv](https://github.com/hybridgroup/gocv) - 使用 OpenCV 3.3+ 的计算机视觉 Go 软件包。
- [gogpu/gg](https://github.com/gogpu/gg) - 使用类似 Canvas API 的 GPU 加速 2D 渲染，零 CGO（[GoGPU](https://github.com/gogpu) 纯 Go 图形生态系统的一部分）。
- [goimagehash](https://github.com/corona10/goimagehash) - Go 感知图像哈希包。
- [goimghdr](https://github.com/corona10/goimghdr) - imghdr 模块确定 Go 文件中包含的图像类型。
- [govatar](https://github.com/o1egl/govatar) - 用于生成有趣头像的库和 CMD 工具。
- [govips](https://github.com/davidbyttow/govips) - 一个闪电般的 Go 图像处理和大小调整库。
- [gowitness](https://github.com/sensepost/gowitness) - 在命令行上使用 go 和 headless chrome 对网页进行屏幕截图。
- [gridder](https://github.com/shomali11/gridder) - 基于网格的 2D 图形库。
- [image2ascii](https://github.com/qeesung/image2ascii) - 将图像转换为 ASCII。
- [imagick](https://github.com/gographics/imagick) - 绑定到 ImageMagick 的 MagickWand C API。
- [imaginary](https://github.com/h2non/imaginary) - 用于调整图像大小的快速而简单的 HTTP 微服务。
- [imaging](https://github.com/disintegration/imaging) - 简单的Go图像处理包。
- [imagor](https://github.com/cshum/imagor) - 使用 libvips 的快速、安全的图像处理服务器和 Go 库。
- [img](https://github.com/hawx/img) - 图像处理工具的选择。
- [ln](https://github.com/fogleman/ln) - Go 中的 3D 线条艺术渲染。
- [mergi](https://github.com/noelyahan/mergi) - 用于图像处理的 Tool & Go 库（合并、裁剪、调整大小、水印、动画）。
- [mort](https://github.com/aldor007/mort) - 用 Go 编写的存储和图像处理服务器。
- [mpo](https://github.com/donatj/mpo) - MPO 3D 照片的解码器和转换工具。
- [nativewebp](https://github.com/HugoSmits86/nativewebp) - 实现零外部依赖的原生 WebP 编码器。
- [picfit](https://github.com/thoas/picfit) - 用 Go 编写的图像调整大小服务器。
- [pt](https://github.com/fogleman/pt) - 用 Go 编写的路径跟踪引擎。
- [scout](https://github.com/jonoton/scout) - Scout 是一款用于 DIY 视频安全的独立开源软件解决方案。
- [smartcrop](https://github.com/muesli/smartcrop) - 找到适合任意图像和裁剪尺寸的良好裁剪。
- [steganography](https://github.com/auyer/steganography) - 用于 LSB 隐写术的 Pure Go 库。
- [stegify](https://github.com/DimitarPetrov/stegify) - 用于 LSB 隐写术的 Go 工具，能够隐藏图像中的任何文件。
- [svgo](https://github.com/ajstarks/svgo) - 用于生成 SVG 的 Go 语言库。
- [transformimgs](https://github.com/Pixboost/transformimgs) - Transformimgs 使用下一代格式调整 Web 图像的大小和优化图像。
- [webp-server](https://github.com/mehdipourfar/webp-server) - 简单且最小的图像服务器，能够存储、调整大小、转换和缓存图像。

**[⬆ 回到顶部](#contents)**

## 物联网（IoT）

_物联网编程设备的库._

- [connectordb](https://github.com/connectordb/connectordb) - 用于量化自我和物联网的开源平台。
- [devices](https://github.com/goiot/devices) - 适用于 IoT 设备的库套件，针对 x/exp/io 进行实验。
- [ekuiper](https://github.com/lf-edge/ekuiper) - 适用于物联网边缘的轻量级数据流处理引擎。
- [eywa](https://github.com/xcodersun/eywa) - Eywa 项目本质上是一个连接管理器，用于跟踪连接的设备。
- [flogo](https://github.com/tibcosoftware/flogo) - Project Flogo 是一个用于 IoT Edge 应用程序和集成的开源框架。
- [gatt](https://github.com/paypal/gatt) - Gatt 是一个用于构建蓝牙低功耗外设的 Go 软件包。
- [gobot](https://github.com/hybridgroup/gobot/) - Gobot 是机器人、物理计算和物联网的框架。
- [huego](https://github.com/amimof/huego) - 适用于 Go 的广泛 Philips Hue 客户端库。
- [iot](https://github.com/vaelen/iot/) - IoT 是一个用于实现 Google IoT Core 设备的简单框架。
- [periph](https://periph.io/) - 与低级板卡设施连接的外设 I/O。
- [rulego](https://github.com/rulego/rulego) - RuleGo 是一个轻量级、高性能、嵌入式、可编排的基于组件的物联网边缘规则引擎。
- [sensorbee](https://github.com/sensorbee/sensorbee) - 适用于物联网的轻量级流处理引擎。
- [shifu](https://github.com/Edgenesis/shifu) - Kubernetes 原生物联网开发框架。
- [smart-home](https://github.com/e154/smart-home) - 物联网自动化软件包。

**[⬆ 回到顶部](#contents)**

## 作业调度程序

_用于调度作业的库._

- [cdule](https://github.com/deepaksinghvi/cdule) - 具有数据库支持的作业调度程序库
- [cheek](https://github.com/bart6114/cheek) - 一个简单的类似 crontab 的调度程序，旨在提供 KISS 方法来进行作业调度。
- [clockwerk](https://github.com/onatm/clockwerk) - Go 包使用简单、流畅的语法来安排定期作业。
- [cronticker](https://github.com/krayzpipes/cronticker) - 支持 cron 计划的股票代码实现。
- [go-cron](https://github.com/rk/go-cron) - go 的简单 Cron 库，可以以不同的时间间隔执行闭包或函数，从每秒一次到每年一次的特定日期和时间。主要用于 Web 应用程序和长时间运行的守护进程。
- [go-cron](https://github.com/netresearch/go-cron) - Cron 作业调度程序，具有运行时调度更新、每个条目上下文、弹性中间件（重试、断路器、速率限制）和可观察性挂钩； robfig/cron 的后继者。
- [go-job](https://github.com/cybergarage/go-job) - 一个灵活且可扩展的 Go 作业调度和执行库。
- [go-quartz](https://github.com/reugn/go-quartz) - 简单、零依赖的 Go 调度库。
- [go-scheduler](https://github.com/pardnchiu/go-scheduler) - 支持标准 cron 表达式、自定义描述符、间隔和任务依赖性的作业调度程序。
- [gocron](https://github.com/go-co-op/gocron) - 轻松流畅的Go作业调度。这是 [jasonlvhit/gocron](https://github.com/jasonlvhit/gocron) 的一个积极维护的分支。
- [goflow](https://github.com/fieldryand/goflow) - 一个简单但功能强大的 DAG 调度程序和仪表板。
- [gron](https://github.com/roylee0704/gron) - 使用简单的 Go API 定义基于时间的任务，Gron 的调度程序将相应地运行它们。
- [gronx](https://github.com/adhocore/gronx) - Cron 表达式解析器、任务运行器和守护进程使用类似任务列表的 crontab。
- [JobRunner](https://github.com/bamzi/jobrunner) - 智能且功能齐全的 cron 作业调度程序，内置作业排队和实时监控。
- [leprechaun](https://github.com/kilgaloon/leprechaun) - 支持 webhook、cron 和经典调度的作业调度程序。
- [ofelia](https://github.com/netresearch/ofelia) - Docker 作业调度程序（Docker 的 crontab）； mcuadros/ofelia 的分支，添加了 Web UI、作业依赖项、重试和作业持久性。
- [pending](https://github.com/kahoon/pending) - 基于 ID 的去抖动任务调度程序，用于具有取消、正常关闭和可选并发限制的延迟任务。
- [sched](https://github.com/romshark/sched) - 具有快进时间能力的作业调度程序。
- [scheduler](https://github.com/carlescere/scheduler) - Cronjobs 调度变得简单。
- [scheduler](https://github.com/yuseferi/scheduler) - 具有延迟任务、批量 Redis 协调、重试、基于租约的恢复和版本化队列分区的原生分布式作业调度程序。
- [tasks](https://github.com/madflojo/tasks) - 一个易于使用的进程内调度程序，用于 Go 中的重复任务。
- [tickstem/cron](https://github.com/tickstem/cron) - 用于调度 HTTP cron 作业的 Go 客户端，具有执行历史记录、故障警报和 tsk-local，用于在没有实时凭据的情况下测试处理程序。
- [tickstem/heartbeat](https://github.com/tickstem/heartbeat) - Go 客户端进行死人交换机心跳监控：每次作业运行后 ping 一个 URL，如果 ping 停止到达，则通过电子邮件收到警报。

**[⬆ 回到顶部](#contents)**

## JSON

_用于处理 JSON 的库._

- [ajson](https://github.com/spyzhov/ajson) - 具有 JSONPath 支持的 golang 抽象 JSON。
- [ask](https://github.com/simonnilsson/ask) - 轻松访问地图和切片中的嵌套值。与encoding/json和其他包结合使用，将任意数据“解组”为Go数据类型。
- [dynjson](https://github.com/cocoonspace/dynjson) - 客户端可自定义动态 API 的 JSON 格式。
- [ej](https://github.com/lucassscaravelli/ej) - 简洁地从不同来源写入和读取 JSON。
- [epoch](https://github.com/vtopc/epoch) - 包含用于将 Unix 时间戳/纪元编组到内置时间/从内置时间解组的原语。JSON 中的时间类型。
- [fastjson](https://github.com/valyala/fastjson) - Go 的快速 JSON 解析器和验证器。没有自定义结构，没有代码生成，没有反射。
- [gabs](https://github.com/Jeffail/gabs) - 用于在 Go 中解析、创建和编辑未知或动态 JSON。
- [gjo](https://github.com/skanehira/gjo) - 用于创建 JSON 对象的小实用程序。
- [GJSON](https://github.com/tidwall/gjson) - 通过一行代码获取 JSON 值。
- [go-jsonerror](https://github.com/ddymko/go-jsonerror) - Go-JsonError 旨在让我们轻松创建遵循 JsonApi 规范的 json 响应错误。
- [go-respond](https://github.com/nicklaw5/go-respond) - 用于处理常见 HTTP JSON 响应的 Go 包。
- [gojmapr](https://github.com/limiu82214/gojmapr) - 通过 json 路径从复杂的 json 中获取简单的结构。
- [gojq](https://github.com/elgs/gojq) - Golang 中的 JSON 查询。
- [gojson](https://github.com/ChimeraCoder/gojson) - 从示例 JSON 自动生成 Go (golang) 结构定义。
- [htmljson](https://github.com/nikolaydubina/htmljson) - 在 Go 中将 JSON 丰富地呈现为 HTML。
- [JayDiff](https://github.com/yazgazan/jaydiff) - 用 Go 编写的 JSON diff 实用程序。
- [jettison](https://github.com/wI2L/jettison) - 适用于 Go 的快速且灵活的 JSON 编码器。
- [jscan](https://github.com/romshark/jscan) - 高性能零分配 JSON 迭代器。
- [JSON-to-Go](https://mholt.github.io/json-to-go/) - 将 JSON 转换为 Go 结构。
- [JSON-to-Proto](https://json-to-proto.github.io/) - 在线将 JSON 转换为 Protobuf。
- [json2go](https://github.com/m-zajac/json2go) - 高级 JSON 到 Go 结构的转换。提供可以解析多个 JSON 文档并创建适合所有文档的结构的包。
- [jsonapi-errors](https://github.com/AmuzaTkts/jsonapi-errors) - 基于 JSON API 错误参考的 Go 绑定。
- [jsoncolor](https://github.com/neilotoole/jsoncolor) - 输出彩色 JSON 的 `encoding/json` 的直接替换。
- [jsondiff](https://github.com/wI2L/jsondiff) - 基于 RFC6902（JSON 补丁）的 Go JSON diff 库。
- [jsonf](https://github.com/miolini/jsonf) - 用于突出显示格式和结构查询获取 JSON 的控制台工具。
- [jsongo](https://github.com/ricardolonga/jsongo) - 流畅的 API 让创建 Json 对象变得更加容易。
- [jsonhal](https://github.com/RichardKnop/jsonhal) - 简单的 Go 包，用于将自定义结构编组为 HAL 兼容的 JSON 响应。
- [jsonhandlers](https://github.com/abusomani/jsonhandlers) - JSON 库公开简单的处理程序，使您可以轻松地从各种来源读取和写入 json。
- [jsonic](https://github.com/sinhashubham95/jsonic) - 用于处理和查询 JSON 的实用程序，无需以类型安全的方式定义结构。
- [jsonvalue](https://github.com/Andrew-M-C/go.jsonvalue) - 一个快速、方便的非结构化 JSON 数据库，取代 `encoding/json`。
- [jzon](https://github.com/zerosnake0/jzon) - 具有标准兼容 API/行为的 JSON 库。
- [kazaam](https://github.com/Qntfy/kazaam) - 用于任意转换 JSON 文档的 API。
- [mapslice-json](https://github.com/mickep76/mapslice-json) - 使用 MapSlice 对 JSON 中的地图进行有序编组/解组。
- [marshmallow](https://github.com/PerimeterX/marshmallow) - 针对灵活用例的高性能 JSON 解组。
- [mp](https://github.com/sanbornm/mp) - 简单的 cli 电子邮件解析器。目前它接受 stdin 并输出 JSON。
- [OjG](https://github.com/ohler55/ojg) - Optimized JSON for Go 是一个高性能解析器，具有各种附加 JSON 工具，包括 JSONPath。
- [omg.jsonparser](https://github.com/dedalqq/omg.jsonparser) - 简单的 JSON 解析器，通过 golang 结构字段标签按条件进行验证。
- [SJSON](https://github.com/tidwall/sjson) - 用一行代码设置一个 JSON 值。
- [ujson](https://github.com/olvrng/ujson) - 适用于非结构化 JSON 的快速且最小的 JSON 解析器和转换器。
- [vjson](https://github.com/miladibra10/vjson) - Go 包，用于通过使用 Fluent API 声明 JSON 模式来验证 JSON 对象。

**[⬆ 回到顶部](#contents)**

## 记录

_用于生成和使用日志文件的库。_

- [caarlos0/log](https://github.com/caarlos0/log) - 丰富多彩的 CLI 记录器。
- [distillog](https://github.com/amoghe/distillog) - 蒸馏级别日志记录（将其视为 stdlib + 日志级别）。
- [glg](https://github.com/kpango/glg) - glg 是 Go 的简单且快速的分级日志库。
- [glo](https://github.com/lajosbencz/glo) - PHP Monolog 启发的日志记录工具具有相同的严重级别。
- [glog](https://github.com/golang/glog) - Go 的分级执行日志。
- [go-cronowriter](https://github.com/utahta/go-cronowriter) - 根据当前日期和时间自动旋转日志文件的简单编写器，例如 cronolog。
- [go-log](https://github.com/pieterclaerhout/go-log) - 具有堆栈跟踪、对象转储和可选时间戳的日志库。
- [go-log](https://github.com/subchen/go-log) - Go 中的简单且可配置的日志记录，具有级别、格式化程序和编写器。
- [go-log](https://github.com/siddontang/go-log) - 日志库支持级别和多处理程序。
- [go-log](https://github.com/ian-kent/go-log) - Go 中的 Log4j 实现。
- [go-logger](https://github.com/apsdehal/go-logger) - Go 程序的简单记录器，带有级别处理程序。
- [GoLogX](https://github.com/AyoubTadlaoui/GoLogX) - 仅附加、哈希链式、可选 Ed25519 签名的 slog 处理程序，具有离线篡改验证功能。
- [gone/log](https://github.com/One-com/gone/tree/master/log) - 快速、可扩展、功能齐全、std-lib 源兼容的日志库。
- [httpretty](https://github.com/henvic/httpretty) - 在终端上漂亮地打印常规 HTTP 请求以进行调试（类似于 http.DumpRequest）。
- [journald](https://github.com/ssgreg/journald) - Go 实现 systemd Journal 的原生日志记录 API。
- [kemba](https://github.com/clok/kemba) - 一个受 [debug](https://github.com/visionmedia/debug) 启发的小型调试日志记录工具，非常适合 CLI 工具和应用程序。
- [lazyjournal](https://github.com/Lifailon/lazyjournal) - 用于读取和过滤来自journalctl、文件系统、Docker 和 Podman 容器以及 Kubernetes Pod 的日志的 TUI。
- [log](https://github.com/aerogo/log) - 一种 O(1) 日志系统，允许您将一个日志连接到多个写入器（例如 stdout、文件和 TCP 连接）。
- [log](https://github.com/apex/log) - Go 的结构化日志记录包。
- [log](https://github.com/go-playground/log) - 简单、可配置且可扩展的 Go 结构化日志记录。
- [log](https://github.com/teris-io/log) - Go 的结构化日志接口将日志记录外观与其实现完全分开。
- [log](https://github.com/heartwilltell/log) - 标准日志包的简单分级日志记录包装器。
- [log](https://github.com/no-src/log) - 一个简单的开箱即用的日志框架。
- [log15](https://github.com/inconshreveable/log15) - 简单、强大的 Go 日志记录。
- [logdump](https://github.com/ewwwwwqm/logdump) - 多级日志记录包。
- [logex](https://github.com/chzyer/logex) - Golang日志库，支持跟踪和级别，由标准日志库包装。
- [logger](https://github.com/azer/logger) - Go 的简约日志库。
- [logo](https://github.com/mbndr/logo) - Golang 记录器到不同的可配置编写器。
- [logrus](https://github.com/Sirupsen/logrus) - Go 的结构化记录器。
- [logrusiowriter](https://github.com/cabify/logrusiowriter) - 使用 [logrus](https://github.com/sirupsen/logrus) 记录器实现 `io.Writer`。
- [logrusly](https://github.com/sebest/logrusly) - [logrus](https://github.com/sirupsen/logrus) 插件，用于将错误发送到 [Loggly](https://www.loggly.com/)。
- [logutils](https://github.com/hashicorp/logutils) - 用于在 Go (Golang) 中进行稍微更好的日志记录的实用程序，扩展了标准记录器。
- [logxi](https://github.com/mgutz/logxi) - 12 因素应用程序记录器，速度快，让您满意。
- [lumberjack](https://github.com/natefinch/lumberjack) - 简单的滚动记录器，实现 io.WriteCloser。
- [mlog](https://github.com/jbrodriguez/mlog) - go 的简单日志记录模块，具有 5 个级别、可选的旋转日志文件功能和 stdout/stderr 输出。
- [noodlog](https://github.com/gyozatech/noodlog) - 参数化 JSON 日志库，可让您混淆敏感数据并编组任何类型的内容。不再用打印指针代替值，也不再使用 JSON 字符串的转义字符。
- [onelog](https://github.com/francoispqt/onelog) - Onelog 是一个非常简单但非常高效的 JSON 记录器。它是所有场景中最快的 JSON 记录器。此外，它也是分配最低的记录器之一。
- [ozzo-log](https://github.com/go-ozzo/ozzo-log) - 支持日志严重性、分类和过滤的高性能日志记录。可以将过滤后的日志消息发送到各种目标（例如控制台、网络、邮件）。
- [phuslu/log](https://github.com/phuslu/log) - 高性能结构化日志记录。
- [pp](https://github.com/k0kubun/pp) - Go 语言的彩色漂亮打印机。
- [rollingwriter](https://github.com/arthurkiller/rollingWriter) - RollingWriter 是一个自动轮换的“io.Writer”实现，具有多种策略来提供日志文件轮换。
- [seelog](https://github.com/cihub/seelog) - 具有灵活调度、过滤和格式化的日志记录功能。
- [sentry-go](https://github.com/getsentry/sentry-go) - 适用于 Go 的 Sentry SDK。通过实时警报和性能监控来帮助监控和跟踪错误。
- [slf4g](https://github.com/echocat/slf4g) - Simple Logging Facade for Golang：简单的结构化日志记录；但功能强大、可扩展和可定制，从过去几十年的日志框架中汲取了大量经验。
- [slog](https://github.com/gookit/slog) - 适用于 Go 的轻量级、可配置、可扩展的记录器。
- [slog-formatter](https://github.com/samber/slog-formatter) - 用于构建您自己的 slog 和帮助程序的通用格式化程序。
- [slog-multi](https://github.com/samber/slog-multi) - slog.Handler 链（管道、扇出...）。
- [slogor](https://gitlab.com/greyxor/slogor) - 一个色彩缤纷的slog处理程序。
- [spew](https://github.com/davecgh/go-spew) - 为 Go 数据结构实现一个深度漂亮的打印机以帮助调试。
- [sqldb-logger](https://github.com/simukti/sqldb-logger) - Go SQL 数据库驱动程序的记录器，无需修改现有的 \*sql.DB stdlib 用法。
- [stdlog](https://github.com/alexcesaro/log) - Stdlog 是一个面向对象的库，提供分级日志记录。它对于 cron 作业非常有用。
- [structy/log](https://github.com/structy/log) - 一个简单易用的日志系统，简约但具有调试和区分消息的功能。
- [tail](https://github.com/hpcloud/tail) - Go 包力求模拟 BSD tail 程序的功能。
- [timberjack](https://github.com/DeRuina/timberjack) - 滚动记录器具有基于大小、基于时间和基于预定时钟的轮换，支持压缩和清理。
- [tint](https://github.com/lmittmann/tint) - 写入着色日志的 slog.Handler。
- [xlog](https://github.com/xfxdev/xlog) - Go 的插件架构和灵活的日志系统，具有级别控制、多个日志目标和自定义日志格式。
- [xlog](https://github.com/rs/xlog) - 用于具有灵活调度功能的“网络/上下文”感知 HTTP 处理程序的结构化记录器。
- [xylog](https://github.com/xybor-x/xylog) - 分级和结构化日志记录、动态字段、高性能、区域管理、简单配置和可读语法。
- [yell](https://github.com/jfcg/yell) - 另一个简约的日志库。
- [zap](https://github.com/uber-go/zap) - Go 中的快速、结构化、分级日志记录。
- [zax](https://github.com/yuseferi/zax) - 将 Context 与 Zap 记录器集成，这使得 Go 日志记录更加灵活。
- [zerolog](https://github.com/rs/zerolog) - 零分配 JSON 记录器。
- [zkits-logger](https://github.com/edoger/zkits-logger) - 一个强大的零依赖 JSON 记录器。
- [zl](https://github.com/nkmr-jp/zl) - 高开发人员经验，基于 zap 的记录器。它提供丰富的功能但易于配置。

**[⬆ 回到顶部](#contents)**

## 机器学习

_机器学习库._

- [Anneal](https://github.com/georgebuilds/anneal) - Go 中的机器学习编译器，一个带有 WebGPU 后端的从头开始的 tinygrad 端口。
- [bayesian](https://github.com/jbrukh/bayesian) - Golang 的朴素贝叶斯分类。
- [born](https://github.com/born-ml/born) - 受 Burn (Rust) 启发的深度学习框架，具有 autograd、类型安全张量和零 CGO GPU 加速。
- [catboost-cgo](https://github.com/mirecl/catboost-cgo) - 决策树库上的快速、可扩展、高性能梯度提升。 Golang 使用 Cgo 实现超快推理 CatBoost 模型。
- [CloudForest](https://github.com/ryanbressler/CloudForest) - 快速、灵活、多线程的决策树集合，用于纯 Go 中的机器学习。
- [datatrax](https://github.com/rbmuller/datatrax) - 数据工程和经典 ML 工具包，具有批处理、类型强制和 7 种零依赖的纯 Go 算法。
- [ddt](https://github.com/sgrodriguez/ddt) - 动态决策树，创建定义可定制规则的树。
- [eaopt](https://github.com/MaxHalford/eaopt) - 一个进化优化库。
- [evoli](https://github.com/khezen/evoli) - 遗传算法和粒子群优化库。
- [fonet](https://github.com/Fontinalis/fonet) - 用 Go 编写的深度神经网络库。
- [go-cluster](https://github.com/e-XpertSolutions/go-cluster) - k 模式和 k 原型聚类算法的 Go 实现。
- [go-deep](https://github.com/patrikeh/go-deep) - Go 中功能丰富的神经网络库。
- [go-fann](https://github.com/white-pony/go-fann) - 快速人工神经网络 (FANN) 库的 Go 绑定。
- [go-galib](https://github.com/thoj/go-galib) - 用 Go / golang 编写的遗传算法库。
- [go-pr](https://github.com/daviddengcn/go-pr) - Go 语言中的模式识别包。
- [gobrain](https://github.com/goml/gobrain) - 用 go 编写的神经网络。
- [godist](https://github.com/e-dard/godist) - 各种概率分布和相关方法。
- [goga](https://github.com/tomcraven/goga) - Go 的遗传算法库。
- [GoLearn](https://github.com/sjwhitworth/golearn) - Go 的通用机器学习库。
- [GoMind](https://github.com/surenderthakran/gomind) - Go 中的简单神经网络库。
- [goml](https://github.com/cdipaolo/goml) - Go 中的在线机器学习。
- [GoMLX](https://github.com/gomlx/gomlx) - Go 的加速机器学习框架。
- [gonet](https://github.com/dathoangnd/gonet) - 围棋神经网络。
- [Goptuna](https://github.com/c-bata/goptuna) - 用 Go 编写的黑盒函数贝叶斯优化框架。一切都将得到优化。
- [goRecommend](https://github.com/timkaye11/goRecommend) - 用 Go 编写的推荐算法库。
- [gorgonia](https://github.com/gorgonia/gorgonia) - 基于图形的计算库，例如 Theano for Go，它提供了构建各种机器学习和神经网络算法的原语。
- [gorse](https://github.com/zhenghaoz/gorse) - 用 Go 编写的基于协同过滤的离线推荐系统后端。
- [goscore](https://github.com/asafschers/goscore) - PMML 的 Go 评分 API。
- [gosseract](https://github.com/otiai10/gosseract) - 使用 Tesseract C++ 库进行 OCR（光学字符识别）的 Go 包。
- [hugot](https://github.com/knights-analytics/hugot) - Huggingface 转换器管道用于带有 onnxruntime 的 golang。
- [libsvm](https://github.com/datastream/libsvm) - libsvm golang版本基于LIBSVM 3.14衍生工作。
- [m2cgen](https://github.com/BayesWitnesses/m2cgen) - 一个 CLI 工具，用于将训练有素的经典 ML 模型转换为零依赖的本机 Go 代码，用 Python 编写，支持 Go 语言。
- [neural-go](https://github.com/schuyler/neural-go) - 用 Go 实现的多层感知器网络，通过反向传播进行训练。
- [ocrserver](https://github.com/otiai10/ocrserver) - 一个简单的 OCR API 服务器，非常容易由 Docker 和 Heroku 部署。
- [onnx-go](https://github.com/owulveryck/onnx-go) - Go 开放神经网络交换 (ONNX) 接口。
- [probab](https://github.com/ThePaw/probab) - 概率分布函数。贝叶斯推理。用纯 Go 编写。
- [randomforest](https://github.com/malaschitz/randomForest) - 易于使用的 Go 随机森林库。
- [regommend](https://github.com/muesli/regommend) - 推荐和协同过滤引擎。
- [shield](https://github.com/eaigner/shield) - 贝叶斯文本分类器，具有灵活的标记器和 Go 存储后端。
- [tfgo](https://github.com/galeone/tfgo) - 易于使用的 Tensorflow 绑定：简化了官方 Tensorflow Go 绑定的使用。在 Go 中定义计算图，加载并执行在 Python 中训练的模型。
- [Varis](https://github.com/Xamber/Varis) - Golang 神经网络。

**[⬆ 回到顶部](#contents)**

## 消息传递

_实现消息传递系统的库._

- [ami](https://github.com/kak-tus/ami) - 将客户端转至基于 Redis Cluster Streams 的可靠队列。
- [amqp](https://github.com/rabbitmq/amqp091-go) - 转到 RabbitMQ 客户端库。
- [APNs2](https://github.com/sideshow/apns2) - 适用于 Go 的 HTTP/2 Apple 推送通知提供程序 - 将推送通知发送到 iOS、tvOS、Safari 和 OSX 应用程序。
- [Asynq](https://github.com/hibiken/asynq) - 一个构建在 Redis 之上的简单、可靠、高效的 Go 分布式任务队列。
- [backlite](https://github.com/mikestefanello/backlite) - 类型安全、持久、嵌入式任务队列和带有 SQLite 的后台作业运行程序。
- [Beaver](https://github.com/Clivern/Beaver) - 实时消息服务器，用于在网络和移动应用程序中构建可扩展的应用程序内通知、多人游戏、聊天应用程序。
- [broker](https://github.com/qvcloud/broker) - 生产级消息传递抽象，具有适用于各种代理的统一 API 和内置 OpenTelemetry 集成。
- [Bus](https://github.com/mustafaturan/bus) - 用于内部通信的最小消息总线实现。
- [Centrifugo](https://github.com/centrifugal/centrifugo) - Go 中的实时消息传递（Websockets 或 SockJS）服务器。
- [Chanify](https://github.com/chanify/chanify) - 推送通知服务器将消息发送到您的 iOS 设备。
- [Commander](https://github.com/jeroenrinzema/commander) - 高级事件驱动的消费者/生产者，支持各种“方言”，例如 Apache Kafka。
- [Confluent Kafka Golang Client](https://github.com/confluentinc/confluent-kafka-go) - confluence-kafka-go 是 Confluence 的 Apache Kafka 和 Confluence 平台的 Golang 客户端。
- [dbus](https://github.com/godbus/dbus) - D-Bus 的本机 Go 绑定。
- [drone-line](https://github.com/appleboy/drone-line) - 使用二进制、docker 或 Drone CI 发送 [Line](https://at.line.me/en) 通知。
- [emitter](https://github.com/olebedev/emitter) - 使用 Go 方式发出事件，具有通配符、谓词、取消可能性和许多其他良好的胜利。
- [event](https://github.com/agoalofalife/event) - 模式观察器的实现。
- [EventBus](https://github.com/asaskevich/EventBus) - 具有异步兼容性的轻量级事件总线。
- [gaurun-client](https://github.com/osamingo/gaurun-client) - 用 Go 编写的 Gaurun 客户端。
- [Glue](https://github.com/desertbit/glue) - 强大的 Go 和 Javascript 套接字库（Socket.io 的替代品）。
- [go-eventbus](https://github.com/stanipetrosyan/go-eventbus) - Go 的简单事件总线包。
- [Go-MediatR](https://github.com/mehdihadeli/Go-MediatR) - 受 csharp MediatR 库启发，用于在事件驱动架构中处理中介模式和简化 CQRS 模式的库。
- [go-mq](https://github.com/cheshir/go-mq) - 具有声明性配置的 RabbitMQ 客户端。
- [go-notify](https://github.com/TheCreeper/go-notify) - freedesktop 通知规范的本机实现。
- [go-nsq](https://github.com/nsqio/go-nsq) - NSQ 的官方 Go 包。
- [go-res](https://github.com/jirenius/go-res) - 用于构建 REST/实时服务的包，其中客户端使用 NATS 和 Resgate 无缝同步。
- [go-vitotrol](https://github.com/maxatome/go-vitotrol) - Viessmann Vitotrol Web 服务的客户端库。
- [GoEventBus](https://github.com/Raezil/GoEventBus) - 速度极快、内存中、无锁的事件总线库
- [Gollum](https://github.com/trivago/gollum) - 一个 n:m 多路复用器，用于收集来自不同源的消息并将它们广播到一组目的地。
- [golongpoll](https://github.com/jcuga/golongpoll) - HTTP longpoll 服务器库，使 Web 发布-订阅变得简单。
- [gopush-cluster](https://github.com/Terry-Mao/gopush-cluster) - gopush-cluster 是一个 go Push 服务器集群。
- [gorush](https://github.com/appleboy/gorush) - 使用 [APNs2](https://github.com/sideshow/apns2) 和 google [GCM](https://github.com/google/go-gcm) 推送通知服务器。
- [gosd](https://github.com/alexsniffin/gosd) - 用于安排何时将消息分派到通道的库。
- [guble](https://github.com/smancke/guble) - 使用推送通知（Google Firebase Cloud Messaging、Apple 推送通知服务、SMS）以及 Websockets、REST API 的消息服务器，具有分布式操作和消息持久性。
- [hare](https://github.com/leozz37/hare) - 一个用户友好的库，用于发送消息和监听 TCP 套接字。
- [hub](https://github.com/leandro-lugaresi/hub) - Go 应用程序的消息/事件中心，使用发布/订阅模式，支持像rabbitMQ交换这样的别名。
- [hypermatch](https://github.com/SchwarzIT/hypermatch) - 一个非常快速且高效的 Go 库，用于将事件与大量规则进行匹配
- [jazz](https://github.com/socifi/jazz) - 一个简单的 RabbitMQ 抽象层，用于队列管理以及消息的发布和消费。
- [machinery](https://github.com/RichardKnop/machinery) - 基于分布式消息传递的异步任务队列/作业队列。
- [mangos](https://github.com/nanomsg/mangos) - 具有传输互操作性的 Nanomsg（“可扩展性协议”）的纯粹实现。
- [melody](https://github.com/olahol/melody) - 用于处理 websocket 会话的简约框架，包括广播和自动 ping/pong 处理。
- [Mercure](https://github.com/dunglas/mercure) - 服务器和库使用 Mercure 协议（构建在服务器发送事件之上）调度服务器发送的更新。
- [messagebus](https://github.com/vardius/message-bus) - messagebus 是一个 Go 简单的异步消息总线，非常适合在进行事件溯源、CQRS、DDD 时用作事件总线。
- [NATS Go Client](https://github.com/nats-io/nats.go) - NATS 的 Go 客户端
消息系统。
- [nsq-event-bus](https://github.com/rafaeljesus/nsq-event-bus) - NSQ 主题和频道的小型包装。
- [oplog](https://github.com/dailymotion/oplog) - REST API 的通用 oplog/复制系统。
- [pubsub](https://github.com/tuxychandru/pubsub) - go 的简单 pubsub 包。
- [Quamina](https://github.com/timbray/quamina) - 用于过滤消息和事件的快速模式匹配。
- [rabbitroutine](https://github.com/furdarius/rabbitroutine) - 处理 RabbitMQ 自动重新连接和发布重试的轻量级库。该库考虑到重新连接后需要在 RabbitMQ 中重新声明实体。
- [rabbus](https://github.com/rafaeljesus/rabbus) - amqp 交换和队列的小型包装器。
- [rabtap](https://github.com/jandelgado/rabtap) - RabbitMQ 瑞士军刀 cli 应用程序。
- [RapidMQ](https://github.com/sybrexsys/RapidMQ) - RapidMQ 是一个轻量级且可靠的库，用于管理本地消息队列。
- [Ratus](https://github.com/hyperonym/ratus) - Ratus 是一个 RESTful 异步任务队列服务器。
- [redisqueue](https://github.com/robinjoseph08/redisqueue) - redisqueue 提供了使用 Redis 流的队列的生产者和消费者。
- [rmqconn](https://github.com/sbabiv/rmqconn) - RabbitMQ 重新连接。 amqp.Connection 和 amqp.Dial 的包装。允许在连接断开时重新连接，然后再强制关闭对 Close() 方法的调用。
- [sarama](https://github.com/Shopify/sarama) - Apache Kafka 的 Go 库。
- [Uniqush-Push](https://github.com/uniqush/uniqush-push) - Redis 支持统一推送服务，用于向移动设备发送服务器端通知。
- [varmq](https://github.com/goptics/varmq) - 用于并发 Go 程序的与存储无关的消息队列和工作池。
- [Watermill](https://github.com/ThreeDotsLabs/watermill) - 高效地处理消息流。构建事件驱动的应用程序，支持事件源、基于消息的 RPC、传奇。可以使用传统的发布/订阅实现，例如 Kafka 或 RabbitMQ，也可以使用 HTTP 或 MySQL binlog。
- [zmq4](https://github.com/pebbe/zmq4) - 转到 ZeroMQ 版本 4 的接口。也可用于 [版本 3](https://github.com/pebbe/zmq3) 和 [版本 2](https://github.com/pebbe/zmq2)。

**[⬆ 回到顶部](#contents)**

## 微软办公软件

- [unioffice](https://github.com/unidoc/unioffice) - 用于创建和处理 Office Word (.docx)、Excel (.xlsx) 和 Powerpoint (.pptx) 文档的纯 go 库。

### 微软Excel

_用于使用 Microsoft Excel 的库._

- [cellwalker](https://github.com/chonla/cellwalker) - 按单元格名称虚拟遍历 Excel 单元格。
- [excelize](https://github.com/xuri/excelize) - 用于读写 Microsoft Excel™ 的 Golang 库(XLSX) 文件。
- [exl](https://github.com/go-the-way/exl) - Excel绑定Go编写的结构体。（仅支持Go1.18+）
- [go-excel](https://github.com/szyhf/go-excel) - 一个简单而轻便的阅读器，用于将类似关联数据库的 Excel 读取为表格。
- [xlsx](https://github.com/tealeg/xlsx) - 用于简化 Go 程序中最新版本的 Microsoft Excel 使用的 XML 格式的读取的库。
- [xlsx](https://github.com/plandem/xlsx) - 在 Go 程序中快速、安全地读取/更新现有 Microsoft Excel 文件。

### 微软Word

_用于使用 Microsoft Word 的库._

- [godocx](https://github.com/gomutex/godocx) - 用于读写 Microsoft Word (Docx) 文件的库。

**[⬆ 回到顶部](#contents)**

## 杂项

### 依赖注入

_用于处理依赖注入的库._

- [alice](https://github.com/magic003/alice) - Golang 的附加依赖注入容器。
- [autowire](https://github.com/tiendc/autowire) - 使用泛型和反射进行依赖注入。
- [boot-go](http://github.com/boot-go/boot) - 为 Go 开发人员使用反射进行基于组件的开发和依赖注入。
- [componego](https://github.com/componego/componego) - 基于组件的依赖注入框架，允许动态依赖替换，而无需在测试中重复代码。
- [cosban/di](https://gitlab.com/cosban/di) - 基于代码生成的依赖注入连接工具。
- [di](https://github.com/goava/di) - Go 编程语言的依赖注入容器。
- [dig](https://github.com/uber-go/dig) - 一个基于反射的 Go 依赖注入工具包。
- [dingo](https://github.com/i-love-flamingo/dingo) - 一个基于 Guice 的 Go 依赖注入工具包。
- [do](https://github.com/samber/do) - 基于泛型的依赖注入框架。
- [fx](https://github.com/uber-go/fx) - 基于依赖注入的 Go 应用程序框架（构建在 dig 之上）。
- [go-beans](https://github.com/go-beans/go) - 受 Spring 启发的 Go 依赖注入和应用程序生命周期框架。
- [Go-Spring](https://github.com/go-spring/spring-core) - 受 Spring Boot 启发的高性能 Go 框架，提供 DI、自动配置和生命周期管理，同时保持 Go 的简单性和高效性。
- [gocontainer](https://github.com/vardius/gocontainer) - 简单的依赖注入容器。
- [godi](https://github.com/junioryono/godi) - Microsoft 风格的 Go 依赖注入，具有作用域生命周期和泛型。
- [goioc/di](https://github.com/goioc/di) - 受 Spring 启发的依赖注入容器。
- [GoLobby/Container](https://github.com/golobby/container) - GoLobby Container 是一个轻量级但功能强大的 Go 编程语言 IoC 依赖注入容器。
- [gontainer](https://github.com/NVIDIA/gontainer) - Go 项目的依赖注入服务容器。
- [gontainer/gontainer](https://github.com/gontainer/gontainer) - 用于 GO 的基于 YAML 的依赖注入容器。它支持依赖关系的范围以及循环依赖关系的自动检测。 Gontainer 是并发安全的。
- [HnH/di](https://github.com/HnH/di) - 专注于干净的 API 和灵活性的 DI 容器库。
- [kinit](https://github.com/go-kata/kinit) - 可定制的依赖注入容器，具有全局模式、级联初始化和紧急安全终结。
- [kod](https://github.com/go-kod/kod) - 一个基于泛型的 Go 依赖注入框架。
- [linker](https://github.com/logrange/linker) - 基于反射的依赖注入和控制库反转，具有组件生命周期支持。
- [nject](https://github.com/muir/nject) - 用于库、测试、http 端点和服务启动的类型安全的反射框架。
- [ore](https://github.com/firasdarwish/ore) - 轻量级、通用且简单的依赖注入 (DI) 容器。
- [parsley](https://github.com/matzefriedrich/parsley) - 灵活且模块化的基于反射的 DI 库，具有范围上下文和代理生成等高级功能，专为大规模 Go 应用程序而设计。
- [wire](https://github.com/Fs02/wire) - Golang 的严格运行时依赖注入。

**[⬆ 回到顶部](#contents)**

### 项目布局

_**非官方**一套用于构建项目的模式。_

- [ardanlabs/service](https://github.com/ardanlabs/service) - 用于构建生产级可扩展 Web 服务应用程序的[入门套件](https://github.com/ardanlabs/service/wiki)。
- [cookiecutter-golang](https://github.com/lacion/cookiecutter-golang) - Go 应用程序样板模板，用于遵循生产最佳实践快速启动项目。
- [go-blueprint](https://github.com/Melkeydev/go-blueprint) - 允许用户使用流行的框架快速启动 Go 项目。
- [go-module](https://github.com/octomation/go-module) - 用 Go 编写的典型模块的模板。
- [go-rest-api-boilerplate](https://github.com/vahiiiid/go-rest-api-boilerplate) - AI 友好、生产就绪的 Go REST API 样板具有干净的架构、JWT 身份验证、RBAC、PostgreSQL、Docker 热重载和 Swagger 文档。
- [go-sample](https://github.com/zitryss/go-sample) - 具有真实代码的 Go 应用程序项目的示例布局。
- [go-starter](https://github.com/allaboutapps/go-starter) - 一个固执己见的生产就绪型 RESTful JSON 后端模板，与 VSCode DevContainers 高度集成。
- [go-todo-backend](https://github.com/Fs02/go-todo-backend) - Go Todo 后端示例使用产品微服务的模块化项目布局。
- [goapp](https://github.com/naughtygopher/goapp) - 构建和开发 Go Web 应用程序/服务的固执己见的指南。
- [gobase](https://github.com/wajox/gobase) - golang 应用程序的简单框架，具有真正 golang 应用程序的基本设置。
- [golang-standards/project-layout](https://github.com/golang-standards/project-layout) - Go 生态系统中常见的历史和新兴项目布局模式集。注意：尽管有 org-name，但它们并不代表官方 golang 标准，请参阅[此问题](https://github.com/golang-standards/project-layout/issues/117) 了解更多信息。尽管如此，有些人可能会发现这种布局很有用。
- [golang-templates/seed](https://github.com/golang-templates/seed) - Go 应用程序 GitHub 存储库模板。
- [goxygen](https://github.com/shpota/goxygen) - 在几秒钟内使用 Go 和 Angular、React 或 Vue 生成现代 Web 项目。
- [insidieux/inizio](https://github.com/insidieux/inizio) - 带插件的 Golang 项目布局生成器。
- [kickstart.go](https://github.com/raeperd/kickstart.go) - 简约的单文件 Go HTTP 服务器模板，无需第三方依赖。
- [modern-go-application](https://github.com/sagikazarmark/modern-go-application) - Go 应用程序样板和应用现代实践的示例。
- [nunu](https://github.com/go-nunu/nunu) - Nunu 是一个用于构建 Go 应用程序的脚手架工具。
- [pagoda](https://github.com/mikestefanello/pagoda) - 使用 Go 构建的快速、简单的全栈 Web 开发入门套件。
- [scaffold](https://github.com/catchplay/scaffold) - Scaffold 生成一个入门 Go 项目布局。让您专注于实现的业务逻辑。
- [wangyoucao577/go-project-layout](https://github.com/wangyoucao577/go-project-layout) - 关于如何构建 Go 项目布局的一组实践和讨论。

**[⬆ 回到顶部](#contents)**

### 弦乐

_用于处理字符串的库._

- [bexp](https://github.com/happy-sdk/happy/tree/main/pkg/strings/bexp) - Go 实现 Brace Expansion 机制来生成任意字符串。
- [caps](https://github.com/chanced/caps) - 大小写转换库。
- [go-formatter](https://gitlab.com/tymonx/go-formatter) - 实现由大括号“{}”格式字符串包围的**替换字段**。
- [gobeam/Stringy](https://github.com/gobeam/Stringy) - 字符串操作库，用于将字符串转换为驼峰式、蛇式、kebab 式/slugify 等。
- [str](https://github.com/schigh/str) - 用于组合转换的管道优先字符串工具包。
- [strcase](https://github.com/charlievieth/strcase) - 标准库的字符串/字节包的不区分大小写的实现。
- [stringFormatter](https://github.com/Wissance/stringFormatter) - 字符串格式化类似于 Python 或 C# 方式，具有附加文本格式化功能。
- [strutil](https://github.com/ozgio/strutil) - 字符串实用程序。
- [sttr](https://github.com/abhimanyu003/sttr) - 跨平台的 cli 应用程序对字符串执行各种操作。
- [xstrings](https://github.com/huandu/xstrings) - 从其他语言移植的有用字符串函数的集合。

**[⬆ 回到顶部](#contents)**

### 未分类

_这些库被放置在这里是因为其他类别似乎都不适合。_

- [anagent](https://github.com/mudler/anagent) - 具有依赖注入的简约、可插入 Golang evloop/定时器处理程序。
- [antch](https://github.com/antchfx/antch) - 一个快速、强大且可扩展的网络爬行和抓取框架。
- [archives](https://github.com/mholt/archives) - 一个跨平台、多格式的 Go 库，用于通过统一的 API 处理存档和压缩格式，并作为与 io/fs 兼容的虚拟文件系统。
- [autoflags](https://github.com/artyom/autoflags) - Go 包自动从结构体字段定义命令行标志。
- [avgRating](https://github.com/kirillDanshin/avgRating) - 根据威尔逊分数方程计算平均分数和评级。
- [banner](https://github.com/dimiro1/banner) - 将漂亮的横幅添加到您的 Go 应用程序中。
- [base64Captcha](https://github.com/mojocn/base64Captcha) - Base64captch 支持数字、数字、字母、算术、音频和数字字母验证码。
- [basexx](https://github.com/bobg/basexx) - 在各种数字基数的数字字符串之间进行转换、转换和转换。
- [battery](https://github.com/distatus/battery) - 跨平台、标准化的电池信息库。
- [bitio](https://github.com/icza/bitio) - 高度优化的 Go 位级读取器和写入器。
- [browscap_go](https://github.com/digitalcrab/browscap_go) - [浏览器功能项目](https://browscap.org/) 的 GoLang 库。
- [captcha](https://github.com/steambap/captcha) - captcha 包为验证码生成提供了一个易于使用、无偏见的 API。
- [common](https://github.com/kubeservice-stack/common) - 服务器框架的库。
- [conv](https://github.com/cstockton/go-conv) - Package conv 提供跨 Go 类型的快速直观的转换。
- [datacounter](https://github.com/miolini/datacounter) - 转到 reader/writer/http.ResponseWriter 的计数器。
- [fake-useragent](https://github.com/lib4u/fake-useragent) - 最新的简单 useragent faker 与 Golang 中的真实世界数据库
- [faker](https://github.com/pioz/faker) - Go 的随机假数据和结构生成器。
- [ffmt](https://github.com/go-ffmt/ffmt) - 美化人类的数据显示。
- [gatus](https://github.com/TwinProduction/gatus) - 自动化服务运行状况仪表板。
- [go-commandbus](https://github.com/lana/go-commandbus) - 用于 Go 的小型可插拔命令总线。
- [go-commons-pool](https://github.com/jolestar/go-commons-pool) - Golang 的通用对象池。
- [go-openapi](https://github.com/go-openapi) - 用于解析和利用 open-api 模式的包集合。
- [go-resiliency](https://github.com/eapache/go-resiliency) - golang 的弹性模式。
- [go-unarr](https://github.com/gen2brain/go-unarr) - RAR、TAR、ZIP 和 7z 档案的解压缩库。
- [gofakeit](https://github.com/brianvoe/gofakeit) - 用 go 编写的随机数据生成器。
- [goffi](https://github.com/go-webgpu/goffi) - Pure Go FFI 具有 libffi 风格的类型化调用接口和结构化错误处理，用于在没有 CGO 的情况下调用 C 库。
- [gommit](https://github.com/antham/gommit) - 分析 git 提交消息以确保它们遵循定义的模式。
- [gopsutil](https://github.com/shirou/gopsutil) - 用于检索进程和系统利用率（CPU、内存、磁盘等）的跨平台库。
- [gosh](https://github.com/osamingo/gosh) - 提供Go统计处理程序、结构体、测量方法。
- [gosms](https://github.com/haxpax/gosms) - 您自己的 Go 本地 SMS 网关可用于发送 SMS。
- [gotoprom](https://github.com/cabify/gotoprom) - 适用于官方 Prometheus 客户端的类型安全指标构建器包装器库。
- [gountries](https://github.com/pariz/gountries) - 公开国家和细分数据的包。
- [gtree](https://github.com/ddddddO/gtree) - 提供 CLI、Package 和 Web，用于通过 Markdown 或以编程方式创建树输出和目录。
- [health](https://github.com/alexliesenfeld/health) - 一个简单灵活的 Go 健康检查库。
- [health](https://github.com/dimiro1/health) - 易于使用、可扩展的健康检查库。
- [healthcheck](https://github.com/etherlabsio/healthcheck) - 用于 RESTful 服务的固执的并发健康检查 HTTP 处理程序。
- [hostutils](https://github.com/Wing924/hostutils) - 用于打包和解包 FQDN 列表的 golang 库。
- [indigo](https://github.com/osamingo/indigo) - 使用Sonyflake并通过Base58编码的分布式唯一ID生成器。
- [lk](https://github.com/hyperboloide/lk) - 一个简单的 golang 许可库。
- [llvm](https://github.com/llir/llvm) - 用于在纯 Go 中与 LLVM IR 交互的库。
- [metrics](https://github.com/pascaldekloe/metrics) - 用于度量仪器和 Prometheus 阐述的库。
- [morse](https://github.com/alwindoss/morse) - 用于与摩尔斯电码相互转换的库。
- [numa](https://github.com/lrita/numa) - NUMA 是一个实用程序库，用 go 编写。它帮助我们编写一些 NUMA-AWRED 代码。
- [pdfgen](https://github.com/hyperboloide/pdfgen) - 用于根据 Json 请求生成 PDF 的 HTTP 服务。
- [persian](https://github.com/mavihq/persian) - Go 中用于波斯语的一些实用程序。
- [purego](https://github.com/ebitengine/purego) - 一个无需 Cgo 即可从 Go 调用 C 函数的库。
- [sandid](https://github.com/aofei/sandid) - 地球上的每一粒沙子都有自己的ID。
- [shellwords](https://github.com/Wing924/shellwords) - 一个 Golang 库，用于根据 UNIX Bourne shell 的单词解析规则来操作字符串。
- [shortid](https://github.com/teris-io/shortid) - 分布式生成超短、唯一、非连续、URL 友好的 ID。
- [shoutrrr](https://github.com/containrrr/shoutrrr) - 通知库提供对各种消息服务的轻松访问，例如 slack、mattermost、gotify 和 smtp 等。
- [sitemap-format](https://github.com/mingard/sitemap-format) - 一个简单的站点地图生成器，带有一点语法糖。
- [stateless](https://github.com/qmuntal/stateless) - 用于创建状态机的流畅库。
- [stats](https://github.com/go-playground/stats) - 监控 Go MemStats + 系统统计信息，例如内存、交换和 CPU，并通过 UDP 发送到您想要记录等的任何地方...
- [turtle](https://github.com/hackebrot/turtle) - Go 的表情符号。
- [url-shortener](https://github.com/pantrif/url-shortener) - 一个现代、强大且健壮的 URL 缩短器微服务，支持 mysql。
- [VarHandler](https://github.com/azr/generators/tree/master/varhandler) - 生成样板 http 输入和输出处理。
- [varint](https://github.com/chmike/varint) - 一种比标准库中提供的更快的变长整数编​​码器/解码器。
- [xdg](https://github.com/rkoesters/xdg) - FreeDesktop.org (xdg) 在 Go 中实现的规范。
- [xkg](https://github.com/go-xkg/xkg) - X 键盘抓取器。
- [xz](https://github.com/ulikunitz/xz) - 用于读取和写入 xz 压缩文件的纯 golang 包。
**[⬆ 回到顶部](#contents)**

## 自然语言处理

_使用人类语言的库._

另请参见[文本处理](#text-processing) 和[文本分析](#text-analysis)。

### 语言检测

- [detectlanguage](https://github.com/detectlanguage/detectlanguage-go) - 语言检测 API Go 客户端。支持批量请求、短语或单字语言检测。
- [getlang](https://github.com/rylans/getlang) - 快速自然语言检测包。
- [guesslanguage](https://github.com/endeveit/guesslanguage) - 确定 unicode 文本的自然语言的函数。
- [lingua-go](https://github.com/pemistahl/lingua-go) - 准确的自然语言检测库，适用于长文本和短文本。支持检测混合语言文本中的多种语言。
- [whatlanggo](https://github.com/abadojack/whatlanggo) - Go 的自然语言检测包。支持 84 种语言和 24 种文字（书写系统，例如拉丁语、西里尔语等）。

### 形态分析仪

- [go-stem](https://github.com/agonopol/go-stem) - 波特词干算法的实现。
- [go2vec](https://github.com/danieldk/go2vec) - word2vec 嵌入的阅读器和实用函数。
- [go-propisyu](https://github.com/rekurt/go-propisyu) - 将数字转换为具有正确语法性别和名词词尾变化的俄语单词。
- [golibstemmer](https://github.com/rjohnsondev/golibstemmer) - Snowball libstemmer 库的 Go 绑定，包括 porter 2。
- [gosentiwordnet](https://github.com/dinopuguh/gosentiwordnet) - 使用Go中的sentiwordnet词典进行情感分析。
- [govader](https://github.com/jonreiter/govader) - 实施[VADER情绪分析](https://github.com/cjhutto/vaderSentiment)。
- [govader-backend](https://github.com/PIMPfiction/govader_backend) - [GoVader](https://github.com/jonreiter/govader) 的微服务实现。
- [kagome](https://github.com/ikawaha/kagome) - 用纯 Go 编写的 JP 形态分析器。
- [libtextcat](https://github.com/goodsign/libtextcat) - libtextcat C 库的 Cgo 绑定。保证与 2.2 版本兼容。
- [nlp](https://github.com/james-bowman/nlp) - 支持 LSA（潜在语义分析）的 Go 自然语言处理库。
- [paicehusk](https://github.com/rookii/paicehusk) - Paice/Husk 词干算法的 Golang 实现。
- [porter](https://github.com/a2800276/porter) - 这是 Martin Porter 对 Porter 词干算法的 C 实现的相当简单的移植。
- [porter2](https://github.com/zhenjl/porter2) - Porter 2 词干分析器速度非常快。
- [RAKE.go](https://github.com/afjoseph/RAKE.Go) - 快速自动关键词提取算法 (RAKE) 的 Go 端口。
- [snowball](https://github.com/goodsign/snowball) - 适用于 Go 的 Snowball 词干分析器端口（cgo 包装器）。提供词干提取功能[Snowball native](http://snowball.tartarus.org/)。
- [spaGO](https://github.com/nlpodyssey/spago) - Go 中独立的机器学习和自然语言处理库。
- [spelling-corrector](https://github.com/jorelosorio/spellingcorrector) - 西班牙语拼写校正器或创建您自己的拼写校正器。

### 弹头

- [go-slugify](https://github.com/mozillazg/go-slugify) - 制作漂亮的 slug，支持多种语言。
- [slug](https://github.com/gosimple/slug) - URL 友好的 slugify，支持多种语言。
- [Slugify](https://github.com/avelino/slugify) - Go slugify 处理字符串的应用程序。

### 分词器

- [gojieba](https://github.com/yanyiwu/gojieba) - 这是中文分词算法[jieba](https://github.com/fxsjy/jieba)的Go实现。
- [gotokenizer](https://github.com/xujiajun/gotokenizer) - 基于 Golang 字典和 Bigram 语言模型的分词器。 （目前仅支持中文分词）
- [gse](https://github.com/go-ego/gse) - 进行高效的文本分割；支持英文、中文、日文等。
- [MMSEGO](https://github.com/awsong/MMSEGO) - 这是中文分词算法[MMSEG](http://technology.chtsai.org/mmseg/)的GO实现。
- [segment](https://github.com/blevesearch/segment) - 用于执行 Unicode 文本分段的 Go 库，如 [Unicode 标准附件 #29](https://www.unicode.org/reports/tr29/) 中所述
- [sentences](https://github.com/neurosnap/sentences) - 句子分词器：将文本转换为句子列表。
- [shamoji](https://github.com/osamingo/shamoji) - shamoji 是用 Go 编写的单词过滤包。
- [stemmer](https://github.com/dchest/stemmer) - Go 编程语言的 Stemmer 包。包括英语和德语词干提取器。
- [textcat](https://github.com/pebbe/textcat) - 用于基于 n-gram 的文本分类的 Go 包，支持 utf-8 和原始文本。

### 翻译

- [ctxi18n](https://github.com/invopop/ctxi18n/) - 上下文感知 i18n，具有简短的 API、复数、插值和“fs.FS”支持。 YAML 语言环境定义基于 [Rails i18n](https://guides.rubyonrails.org/i18n.html)。
- [go-i18n](https://github.com/nicksnyder/go-i18n/) - 用于处理本地化文本的软件包和随附工具。
- [go-mystem](https://github.com/dveselov/mystem) - CGo 与 Yandex.Mystem 的绑定 - 俄罗斯形态分析仪。
- [go-pinyin](https://github.com/mozillazg/go-pinyin) - CN 汉字到汉语拼音转换器。
- [go-words](https://github.com/saleh-rahimzadeh/go-words) - Golang 项目的单词表和文本资源库。
- [gotext](https://github.com/leonelquinteros/gotext) - Go 的 GNU gettext 实用程序。
- [iuliia-go](https://github.com/mehanizm/iuliia-go) - 以各种可能的方式音译西里尔语 → 拉丁语。
- [spreak](https://github.com/vorlif/spreak) - 基于 gettext 背后的概念，适用于 Go 的灵活翻译和人性化库。
- [t](https://github.com/youthlin/t) - 另一个golang的i18n pkg，它遵循GNU gettext风格并支持.po / .mo文件：`t.T（gettext）`，`t.N（ngettext）`等。它包含一个cmd工具[xtemplate]（https://github.com/youthlin/t/blob/main/cmd/xtemplate），可以从text/html模板中将消息提取为pot文件。

### 音译

- [enca](https://github.com/endeveit/enca) - [libenca](https://cihar.com/software/enca/) 的最小 cgo 绑定，用于检测字符编码。
- [go-unidecode](https://github.com/mozillazg/go-unidecode) - Unicode 文本的 ASCII 音译。
- [gounidecode](https://github.com/fiam/gounidecode) - Go 的 Unicode 音译器（也称为 unidecode）。
- [transliterator](https://github.com/alexsergivan/transliterator) - 提供单向字符串音译，并支持特定于语言的音译规则。

**[⬆ 回到顶部](#contents)**

## 网络

_用于处理网络各个层的库。_

- [arp](https://github.com/mdlayher/arp) - arp 包实现了 ARP 协议，如 RFC 826 中所述。
- [bart](https://github.com/gaissmai/bart) - bart 包提供平衡路由表 (BART)，用于非常快速的 IP 到 CIDR 查找等。
- [buffstreams](https://github.com/stabbycutyou/buffstreams) - 通过 TCP 传输协议缓冲区数据变得容易。
- [canopus](https://github.com/zubairhamed/canopus) - CoAP 客户端/服务器实现 (RFC 7252)。
- [cdns](https://github.com/junevm/cdns) - 通过终端轻松更改 DNS 服务器。
- [cidranger](https://github.com/yl2chen/cidranger) - Go 的快速 IP 到 CIDR 查找。
- [cloudflared](https://github.com/cloudflare/cloudflared) - Cloudflare Tunnel 客户端（以前称为 Argo Tunnel）。
- [dhcp6](https://github.com/mdlayher/dhcp6) - 包 dhcp6 实现 DHCPv6 服务器，如 RFC 3315 中所述。
- [dns](https://github.com/miekg/dns) - 用于使用 DNS 的 Go 库。
- [dnsmonster](https://github.com/mosajjal/dnsmonster) - 被动 DNS 捕获/监控框架。
- [easytcp](https://github.com/DarthPestilane/easytcp) - 用 Go (Golang) 编写的轻量级 TCP 框架，使用消息路由器构建。 EasyTCP 可帮助您轻松、快速、轻松地构建 TCP 服务器。
- [ether](https://github.com/songgao/ether) - 用于发送和接收以太网帧的跨平台 Go 包。
- [ethernet](https://github.com/mdlayher/ethernet) - ethernet 包实现 IEEE 802.3 以太网 II 帧和 IEEE 802.1Q VLAN 标记的编组和解组。
- [event](https://github.com/cheng-zhongliang/event) - 用 Golang 编写的简单 I/O 事件通知库。
- [fasthttp](https://github.com/valyala/fasthttp) - fasthttp 包是 Go 的快速 HTTP 实现，比 net/http 快 10 倍。
- [fortio](https://github.com/fortio/fortio) - 负载测试库和命令行工具、高级回显服务器和 Web UI。允许指定一组每秒查询负载并记录延迟直方图和其他有用的统计数据并绘制它们的图表。 TCP、HTTP、gRPC。
- [ftp](https://github.com/jlaffaye/ftp) - ftp 包实现了 FTP 客户端，如 [RFC 959](https://tools.ietf.org/html/rfc959) 中所述。
- [ftpserverlib](https://github.com/fclairamb/ftpserverlib) - 功能齐全的 FTP 服务器库。
- [fullproxy](https://github.com/shoriwe/fullproxy) - 功能齐全的可编写脚本和守护程序可配置代理和旋转工具包，具有 SOCKS5、HTTP、原始端口和反向代理协议。
- [fwdctl](https://github.com/alegrey91/fwdctl) - 一个简单直观的 C​​LI，用于管理 Linux 服务器中的 IPTables 转发。
- [gaio](https://github.com/xtaci/gaio) - 前摄器模式下 Golang 的高性能异步 io 网络。
- [gev](https://github.com/Allenxuxu/gev) - gev 是一个基于 Reactor 模式的轻量级、快速非阻塞 TCP 网络库。
- [gldap](https://github.com/jimlambrt/gldap) - gldap 提供 LDAP 服务器实现，您可以为其 LDAP 操作提供处理程序。
- [gmqtt](https://github.com/DrmagicE/gmqtt) - Gmqtt是一个灵活、高性能的MQTT代理库，完全实现MQTT协议V3.1.1。
- [gnet](https://github.com/panjf2000/gnet) - `gnet` 是一个用纯 Go 编写的高性能、轻量级、非阻塞、事件驱动的网络框架。
- [gnet](https://github.com/fish-tennis/gnet) - `gnet` 是一个高性能网络框架，特别适用于游戏服务器。
- [gNxI](https://github.com/google/gnxi) - 使用 gNMI 和 gNOI 协议的网络管理工具集合。
- [go-getter](https://github.com/hashicorp/go-getter) - 使用 URL 从各种来源下载文件或目录的 Go 库。
- [go-multiproxy](https://github.com/presbrey/go-multiproxy) - 用于通过代理池发出 HTTP 请求的库，通过 http.Get/Post 替换或 http.Client RoundTripper 插件提供容错、负载平衡、自动重试、cookie 管理等功能
- [go-pcaplite](https://github.com/alexcfv/go-pcaplite) - 具有 HTTPS SNI 提取功能的轻量级实时数据包捕获库。
- [go-powerdns](https://github.com/joeig/go-powerdns) - Golang 的 PowerDNS API 绑定。
- [go-sse](https://github.com/lampctl/go-sse) - HTML 服务器发送事件的 Go 客户端和服务器实现。
- [fibersse](https://github.com/vinod-morya/fibersse) - 适用于 Fiber v3 的生产级服务器发送事件 (SSE)，具有事件合并、优先级通道、主题通配符、自适应限制和内置身份验证。
- [go-stun](https://github.com/ccding/go-stun) - Go 实现 STUN 客户端（RFC 3489 和 RFC 5389）。
- [gobgp](https://github.com/osrg/gobgp) - BGP 采用 Go 编程语言实现。
- [gopacket](https://github.com/google/gopacket) - 使用 libpcap 绑定进行数据包处理的 Go 库。
- [gopcap](https://github.com/akrennmair/gopcap) - 去包装 libpcap。
- [GoProxy](https://github.com/elazarl/goproxy) - 使用 Go 创建自定义 HTTP/HTTPS 代理服务器的库。
- [goshark](https://github.com/sunwxg/goshark) - goshark 包使用 tshark 来解码 IP 数据包并创建数据结构来分析数据包。
- [gosnmp](https://github.com/soniah/gosnmp) - 用于执行 SNMP 操作的 Native Go 库。
- [gotcp](https://github.com/gansidui/gotcp) - 用于快速编写 TCP 应用程序的 Go 包。
- [grab](https://github.com/cavaliercoder/grab) - 用于管理文件下载的 Go 包。
- [graval](https://github.com/koofr/graval) - 实验性 FTP 服务器框架。
- [gws](https://github.com/lxzan/gws) - 支持 AsyncIO 的高性能 WebSocket 服务器和客户端。
- [HTTPLab](https://github.com/gchaincl/httplab) - HTTPLabs 允许您检查 HTTP 请求并伪造响应。
- [httpproxy](https://github.com/wzshiming/httpproxy) - HTTP 代理处理程序和拨号程序。
- [iplib](https://github.com/c-robinson/iplib) - 用于处理 IP 地址（net.IP、net.IPNet）的库，灵感来自 python [ipaddress](https://docs.python.org/3/library/ipaddress.html) 和 ruby [ipaddr](https://ruby-doc.org/stdlib-2.5.1/libdoc/ipaddr/rdoc/IPAddr.html)
- [jazigo](https://github.com/udhos/jazigo) - Jazigo 是一个用 Go 编写的工具，用于检索多个网络设备的配置。
- [kcp-go](https://github.com/xtaci/kcp-go) - KCP - 快速可靠的 ARQ 协议。
- [kcptun](https://github.com/xtaci/kcptun) - 基于KCP协议的极其简单和快速的udp隧道。
- [lhttp](https://github.com/fanux/lhttp) - 强大的websocket框架，更轻松地构建您的IM服务器。
- [linkio](https://github.com/ian-kent/linkio) - 读取器/写入器接口的网络链路速度模拟。
- [llb](https://github.com/kirillDanshin/llb) - 这是一个非常简单但快速的代理服务器后端。对于快速重定向到具有零内存分配和快速响应的预定义域非常有用。
- [macwifi](https://github.com/jaisonerick/macwifi) - 适用于 macOS 13+ 的 Wi-Fi 扫描和钥匙串密码检索。
- [mdns](https://github.com/hashicorp/mdns) - Golang 中的简单 mDNS（多播 DNS）客户端/服务器库。
- [mqttPaho](https://eclipse.org/paho/clients/golang/) - Paho Go 客户端提供了一个 MQTT 客户端库，用于通过 TCP、TLS 或 WebSocket 连接到 MQTT 代理。
- [natiu-mqtt](https://github.com/soypat/natiu-mqtt) - MQTT 的极其简单、非分配、低级实现，非常适合嵌入式系统。
- [nbio](https://github.com/lesismal/nbio) - Pure Go 1000k+连接解决方​​案，支持tls/http1.x/websocket，基本兼容net/http，具有高性能、低内存成本、非阻塞、事件驱动、易于使用。
- [net](https://golang.org/x/net) - 该存储库包含补充的 Go 网络库。
- [netpoll](https://github.com/cloudwego/netpoll) - 字节跳动开发的一款高性能非阻塞I/O网络框架，专注于RPC场景。
- [NFF-Go](https://github.com/intel-go/nff-go) - 用于快速开发云和裸机高性能网络功能的框架（以前的 YANFF）。
- [nodepass](https://github.com/NodePassProject/nodepass) - 一种安全、高效的 TCP/UDP 隧道解决方案，可使用预先建立的 TCP/QUIC/WebSocket 或 HTTP/2 连接跨网络限制提供快速、可靠的访问。
- [peerdiscovery](https://github.com/schollz/peerdiscovery) - 使用 UDP 多播进行跨平台本地对等点发现的 Pure Go 库。
- [portproxy](https://github.com/aybabtme/portproxy) - 简单的 TCP 代理，为不支持 CORS 的 API 添加 CORS 支持。
- [psql-wire](https://github.com/jeroenrinzema/psql-wire) - PostgreSQL 服务器有线协议。构建您自己的服务器并开始提供连接..
- [publicip](https://github.com/polera/publicip) - publicip 包返回您面向公众的 IPv4 地址（互联网出口）。
- [quic-go](https://github.com/lucas-clemente/quic-go) - QUIC 协议在纯 Go 中的实现。
- [sdns](https://github.com/semihalev/sdns) - 具有 DNSSEC 支持的高性能、递归 DNS 解析器服务器，专注于保护隐私。
- [sftp](https://github.com/pkg/sftp) - sftp 包实现了 SSH 文件传输协议，如 <https://filezilla-project.org/specs/draft-ietf-secsh-filexfer-02.txt> 中所述。
- [ssh](https://github.com/gliderlabs/ssh) - 用于构建 SSH 服务器的高级 API（包装 crypto/ssh）。
- [sslb](https://github.com/eduardonunesp/sslb) - 这是一个超级简单的负载均衡器，只是一个实现某种性能的小项目。
- [stun](https://github.com/go-rtc/stun) - 执行 RFC 5389 STUN 协议。
- [tcpack](https://github.com/lim-yoona/tcpack) - tcpack是一个基于TCP的应用协议，用于在go程序中打包和解包字节流。
- [tspool](https://github.com/two/tspool) - TCP 库使用工作池来提高性能并保护您的服务器。
- [tun2socks](https://github.com/xjasonlyu/tun2socks) - 由 [gVisor](https://gvisor.dev/) TCP/IP 堆栈提供支持的 tun2socks 的纯 Go 实现。
- [utp](https://github.com/anacrolix/utp) - Go uTP微传输协议实现。
- [vssh](https://github.com/yahoo/vssh) - 用于通过 SSH 协议构建网络和服务器自动化的 Go 库。
- [water](https://github.com/songgao/water) - 简单的 TUN/TAP 库。
- [webrtc](https://github.com/pions/webrtc) - WebRTC API 的纯 Go 实现。
- [winrm](https://github.com/masterzen/winrm) - 使用 WinRM 客户端在 Windows 机器上远程执行命令。
- [xtcp](https://github.com/xfxdev/xtcp) - TCP 服务器框架，具有同步全双工通信、正常关闭和自定义协议。

**[⬆ 回到顶部](#contents)**

### HTTP 客户端

_用于发出 HTTP 请求的库._

- [axios4go](https://github.com/rezmoss/axios4go) - 受 Axios 启发的 Go HTTP 客户端库，提供简单直观的 API 来发出 HTTP 请求。
- [azuretls-client](https://github.com/Noooste/azuretls-client) - 易于使用的 HTTP 客户端 100% 欺骗 TLS/JA3 和 HTTP2 指纹。
- [fast-shot](https://github.com/opus-domini/fast-shot) - 使用 Go 最快且简单的 HTTP 客户端快速精确地达到您的 API 目标。
- [gentleman](https://github.com/h2non/gentleman) - 全功能插件驱动的 HTTP 客户端库。
- [go-cleanhttp](https://github.com/hashicorp/go-cleanhttp) - 轻松获取 stdlib HTTP 客户端，它不与其他客户端共享任何状态。
- [go-http-client](https://github.com/bozd4g/go-http-client) - 简单轻松地进行 http 调用。
- [go-ipmux](https://github.com/optimus-hft/go-ipmux) - 用于基于多个源 IP 复用 HTTP 请求的库。
- [go-otelroundtripper](https://github.com/NdoleStudio/go-otelroundtripper) - 转到 http.RoundTripper，它为 HTTP 请求发出开放遥测指标。
- [go-req](https://github.com/wenerme/go-req) - 声明式 golang HTTP 客户端。
- [go-retryablehttp](https://github.com/hashicorp/go-retryablehttp) - Go 中的可重试 HTTP 客户端。
- [go-zoox/fetch](https://github.com/go-zoox/fetch) - 一个强大、轻量级、简单的 Http 客户端，受到 Web Fetch API 的启发。
- [Grequest](https://github.com/lib4u/grequest) - 用于 http 请求的简单轻量级 golang 包。基于强大的net/http
- [grequests](https://github.com/levigross/grequests) - 伟大而著名的 Requests 库的 Go“克隆”。
- [hedge](https://github.com/bhope/hedge) - Go 的自适应对冲请求。基于 Google 的“The Tail at Scale”论文，以零配置减少 p99 延迟。
- [heimdall](https://github.com/gojektech/heimdall) - 具有重试和 hystrix 功能的增强型 http 客户端。
- [httpretry](https://github.com/ybbus/httpretry) - 通过重试功能丰富了默认的 go HTTP 客户端。
- [pester](https://github.com/sethgrid/pester) - 具有重试、退避和并发性的 Go HTTP 客户端调用。
- [req](https://github.com/imroc/req) - 使用 Black Magic 的简单 Go HTTP 客户端（更少的代码和更高的效率）。
- [request](https://github.com/monaco-io/request) - golang 的 HTTP 客户端。如果您有 axios 或 requests 的经验，您一定会喜欢它。没有第三个依赖。
- [requests](https://github.com/carlmjohnson/requests) - 对 Gopher 的 HTTP 请求。使用 context.Context 并且不隐藏底层 net/http.Client，使其与标准 Go API 兼容。还包括测试工具。
- [resty](https://github.com/go-resty/resty) - Go 的简单 HTTP 和 REST 客户端，受到 Ruby Rest-client 的启发。
- [rq](https://github.com/ddo/rq) - golang stdlib HTTP 客户端的更好接口。
- [sling](https://github.com/dghubble/sling) - Sling 是一个用于创建和发送 API 请求的 Go HTTP 客户端库。
- [surf](https://github.com/enetx/surf) - 高级 HTTP 客户端，具有 HTTP/1.1、HTTP/2、HTTP/3 (QUIC)、SOCKS5 代理支持和浏览器级 TLS 指纹识别。
- [tls-client](https://github.com/bogdanfinn/tls-client) - net/http.Client 与 HTTP 客户端类似，具有选择用于请求的特定客户端 TLS 指纹的选项。

**[⬆ 回到顶部](#contents)**

## OpenGL

_在 Go 中使用 OpenGL 的库._

- [gl](https://github.com/go-gl/gl) - Go OpenGL 的绑定（通过发光生成）。
- [glfw](https://github.com/go-gl/glfw) - GLFW 3 的 Go 绑定。
- [go-glmatrix](https://github.com/technohippy/go-glmatrix) - 转到 [glMatrix](https://glmatrix.net/) 库的端口。
- [goxjs/gl](https://github.com/goxjs/gl) - 跨平台 OpenGL 绑定（OS X、Linux、Windows、浏览器、iOS、Android）。
- [goxjs/glfw](https://github.com/goxjs/glfw) - 用于创建 OpenGL 上下文和接收事件的跨平台 glfw 库。
- [mathgl](https://github.com/go-gl/mathgl) - Pure Go 数学包专门用于 3D 数学，灵感来自 GLM。

**[⬆ 回到顶部](#contents)**

## ORM

_实现对象关系映射或数据映射技术的库。_

- [bob](https://github.com/stephenafamo/bob) - 用于 Go 的 SQL 查询生成器和 ORM/Factory 生成器。 SQLBoiler 的后继者。
- [bun](https://github.com/uptrace/bun) - SQL 优先的 Golang ORM。 go-pg 的后继者。
- [cacheme](https://github.com/Yiling-J/cacheme-go) - 用于 Go 的基于模式的类型化 Redis 缓存/记忆框架。
- [CQL](https://github.com/FrancoLiberali/cql) - 构建于 GORM 之上，添加基于自动生成代码的编译时验证查询。
- [ent](https://github.com/facebook/ent) - Go 的实体框架。简单但功能强大的 ORM，用于建模和查询数据。
- [go-dbw](https://github.com/hashicorp/go-dbw) - 封装数据库操作的简单包。
- [go-firestorm](https://github.com/jschoedt/go-firestorm) - 适用于 Google/Firebase Cloud Firestore 的简单 ORM。
- [go-sql](https://github.com/rushteam/gosql) - 一个简单的 MySQL ORM。
- [go-sqlbuilder](https://github.com/huandu/go-sqlbuilder) - 灵活且强大的 SQL 字符串生成器库以及零配置 ORM。
- [go-store](https://github.com/gosuri/go-store) - 简单快速的 Redis 支持的 Go 键值存储库。
- [golobby/orm](https://github.com/golobby/orm) - 简单、快速、类型安全、通用的 orm，让开发人员满意。
- [GORM](https://github.com/go-gorm/gorm) - Golang 的出色 ORM 库旨在对开发人员友好。
- [gormt](https://github.com/xxjwxc/gormt) - Mysql 数据库到 golang gorm 结构。
- [gorp](https://github.com/go-gorp/gorp) - Go Relational Persistence，Go 的 ORM 库。
- [grimoire](https://github.com/Fs02/grimoire) - Grimoire 是 golang 的数据库访问层和验证。 （支持：MySQL、PostgreSQL 和 SQLite3）。
- [lore](https://github.com/abrahambotros/lore) - 用于 Go 的简单且轻量级的伪 ORM/伪结构映射环境。
- [marlow](https://github.com/marlow/marlow) - 从项目结构生成 ORM 以确保编译时安全。
- [pop/soda](https://github.com/gobuffalo/pop) - MySQL、PostgreSQL 和 SQLite 的数据库迁移、创建、ORM 等。
- [Prisma](https://github.com/prisma/prisma-client-go) - Prisma Client Go，Go 的 Typesafe 数据库访问。
- [reform](https://github.com/go-reform/reform) - 基于非空接口和代码生成的更好的 Go ORM。
- [rel](https://github.com/go-rel/rel) - Golang 的现代数据库访问层 - 可测试、可扩展并精心打造为干净而优雅的 API。
- [SQLBoiler](https://github.com/volatiletech/sqlboiler) - ORM 生成器。生成适合您的数据库架构的功能强大且速度极快的 ORM。
- [upper.io/db](https://github.com/upper/db) - 通过使用包装成熟数据库驱动程序的适配器与不同数据源进行交互的单一接口。
- [XORM](https://gitea.com/xorm/xorm) - 简单而强大的 Go ORM。 （支持：MySQL、MyMysql、PostgreSQL、Tidb、SQLite3、MsSql 和 Oracle）。
- [Zoom](https://github.com/albrow/zoom) - 基于 Redis 构建的超快数据存储和查询引擎。

**[⬆ 回到顶部](#contents)**

## 包管理

_用于依赖项和包管理的官方工具_

- [go modules](https://golang.org/cmd/go/#hdr-Modules__module_versions__and_more) - 模块是源代码交换和版本控制的单元。 go 命令直接支持使用模块，包括记录和解决对其他模块的依赖关系。

_用于包和依赖项管理的非官方库。_

- [gup](https://github.com/nao1215/gup) - 更新通过“go install”安装的二进制文件。
- [modup](https://github.com/chaindead/modup) - 用于 Go 依赖项更新的终端 UI，具有过时模块检测和选择性升级功能。
- [syft](https://github.com/anchore/syft) - 用于从容器映像和文件系统生成软件物料清单 (SBOM) 的 CLI 工具和 Go 库。

**[⬆ 回到顶部](#contents)**

## 性能

- [ebpf-go](https://github.com/cilium/ebpf) - 提供用于加载、编译和调试 eBPF 程序的实用程序。
- [go-instrument](https://github.com/nikolaydubina/go-instrument) - 自动将跨度添加到所有方法和函数。
- [go-perfstat](https://github.com/go-perfstat/go) - Go 的轻量级性能统计和执行时间聚合。
- [jaeger](https://github.com/jaegertracing/jaeger) - 分布式追踪系统。
- [mm-go](https://github.com/joetifa2003/mm-go) - golang 的通用手动内存管理。
- [otelinji](https://github.com/hedhyw/otelinji) - OpenTelemetry 自动检测工具，用于向函数添加跨度。
- [pixie](https://github.com/pixie-labs/pixie) - 没有通过 eBPF 对 Golang 应用程序进行仪器跟踪。
- [profile](https://github.com/pkg/profile) - Go 的简单分析支持包。
- [statsviz](https://github.com/arl/statsviz) - Go 应用程序运行时统计数据的实时可视化。
- [tracer](https://github.com/kamilsk/tracer) - 简单、轻量级的追踪。

**[⬆ 回到顶部](#contents)**

## 查询语言

- [api-fu](https://github.com/ccbrown/api-fu) - 全面的 GraphQL 实现。
- [dasel](https://github.com/tomwright/dasel) - 使用命令行中的选择器查询和更新数据结构。与 jq/yq 类似，但支持 JSON、YAML、TOML 和 XML，且运行时依赖性为零。
- [gojsonq](https://github.com/thedevsaddam/gojsonq) - 用于查询 JSON 数据的简单 Go 包。
- [goven](https://github.com/SeldonIO/goven) - 适用于任何数据库模式的嵌入式查询语言。
- [gqlgen](https://github.com/99designs/gqlgen) - go 生成基于 graphql 服务器库。
- [grapher](https://github.com/reaganiwadha/grapher) - GraphQL 字段构建器利用 Go 泛型以及额外的实用程序和功能。
- [graphql](https://github.com/neelance/graphql-go) - 注重易用性的 GraphQL 服务器。
- [graphql-go](https://github.com/graphql-go/graphql) - Go 的 GraphQL 实现。
- [gws](https://github.com/Zaba505/gws) - Apollos 的“GraphQL over Websocket”客户端和服务器实现。
- [jsonpath](https://github.com/AsaiYusuke/jsonpath) - 用于基于 JSONPath 语法检索部分 JSON 的查询库。
- [jsonql](https://github.com/elgs/jsonql) - Golang 中的 JSON 查询表达式库。
- [jsonslice](https://github.com/bhmj/jsonslice) - 使用高级过滤器进行 Jsonpath 查询。
- [mql](https://github.com/hashicorp/mql) - 模型查询语言 (mql) 是数据库模型的查询语言。
- [play](https://github.com/paololazzari/play) - 一个 TUI 游乐场，用于试验您最喜欢的程序，例如 grep、sed、awk、jq 和 yq。
- [rql](https://github.com/a8m/rql) - REST API 的资源查询语言。
- [rqp](https://github.com/timsolov/rest-query-parser) - REST API 的查询解析器。查询中直接支持过滤、验证、“AND”、“OR”操作。
- [straf](https://github.com/SonicRoshan/straf) - 轻松将 Golang 结构转换为 GraphQL 对象。

**[⬆ 回到顶部](#contents)**

## 反思

- [copy](https://github.com/gotidy/copy) - 用于快速复制不同类型结构的包。
- [Deepcopier](https://github.com/ulule/deepcopier) - Go 的简单结构复制。
- [go-deepcopy](https://github.com/tiendc/go-deepcopy) - 快速深拷贝库。
- [goenum](https://github.com/lvyahui8/goenum) - 基于泛型和反射的通用枚举结构，允许您快速定义枚举并使用一组有用的默认方法。
- [gotype](https://github.com/wzshiming/gotype) - Golang源码解析，用法类似reflect包。
- [gpath](https://github.com/tenntenn/gpath) - 使用 Go 反射表达式简化访问结构体字段的库。
- [objwalker](https://github.com/rekby/objwalker) - 通过反射走过对象。
- [reflectpro](https://github.com/gontainer/reflectpro) - go 的调用者、复制者、获取者和设置者。
- [reflectutils](https://github.com/muir/reflectutils) - 使用反射的助手：结构标签解析；递归行走；从字符串填充值。

**[⬆ 回到顶部](#contents)**

## 资源嵌入

- [debme](https://github.com/leaanthony/debme) - 从现有的“embed.FS”子目录创建“embed.FS”。
- [embed](https://pkg.go.dev/embed) - Package embed 提供对正在运行的 Go 程序中嵌入的文件的访问。
- [rebed](https://github.com/soypat/rebed) - 从 Go 1.16 的 `embed.FS` 类型重新创建文件夹结构和文件
- [vfsgen](https://github.com/shurcooL/vfsgen) - 生成一个静态实现给定虚拟文件系统的 vfsdata.go 文件。

**[⬆ 回到顶部](#contents)**

## 科学与数据分析

_科学计算和数据分析库._

- [bradleyterry](https://github.com/seanhagen/bradleyterry) - 提供用于成对比较的 Bradley-Terry 模型。
- [calendarheatmap](https://github.com/nikolaydubina/calendarheatmap) - 简单 Go 中的日历热图受到 Github 贡献活动的启发。
- [chart](https://github.com/vdobler/chart) - Go 的简单图表绘制库。支持多种图表类型。
- [dataframe-go](https://github.com/rocketlaunchr/dataframe-go) - 用于机器学习和统计的数据框（类似于 pandas）。
- [decimal](https://github.com/db47h/decimal) - 包decimal实现任意精度十进制浮点运算。
- [entitydebs](https://github.com/ndabAP/entitydebs) - 一种社会科学工具，可通过内置的依赖解析器以编程方式分析非虚构文本中的实体。
- [evaler](https://github.com/soniah/evaler) - 简单的浮点算术表达式计算器。
- [ewma](https://github.com/VividCortex/ewma) - 指数加权移动平均线。
- [geom](https://github.com/skelterjohn/geom) - golang 的 2D 几何。
- [go-dsp](https://github.com/mjibson/go-dsp) - Go 的数字信号处理。
- [go-estimate](https://github.com/milosgajdos/go-estimate) - Go 中的状态估计和过滤算法。
- [go-gt](https://github.com/ThePaw/go-gt) - 用“Go”语言编写的图论算法。
- [go-hep](https://github.com/go-hep/hep) - 一组用于轻松执行高能物理分析的库和工具。
- [godesim](https://github.com/soypat/godesim) - 扩展/多变量 ODE 求解器框架，用于具有简单 API 的基于事件的模拟。
- [goent](https://github.com/kzahedi/goent) - GO 熵测量的实施。
- [gograph](https://github.com/hmdsefi/gograph) - 一个 golang 通用图库，提供数学图论和算法。
- [gonum](https://github.com/gonum/gonum) - Gonum 是一组 Go 编程语言的数字库。它包含矩阵、统计、优化等库。
- [gonum/plot](https://github.com/gonum/plot) - gonum/plot 提供了一个用于在 Go 中构建和绘制绘图的 API。
- [goraph](https://github.com/gyuho/goraph) - Pure Go图论库（数据结构、算法可视化）。
- [gosl](https://github.com/cpmech/gosl) - 前往科学图书馆，了解线性代数、FFT、几何、NURBS、数值方法、概率、优化、微分方程等。
- [GoStats](https://github.com/OGFris/GoStats) - GoStats 是一个开源 GoLang 数学统计库，主要用于机器学习领域，它涵盖了大多数统计测量功能。
- [graph](https://github.com/yourbasic/graph) - 基本图算法库。
- [hdf5](https://github.com/scigolib/hdf5) - 用于科学数据存储和交换的 HDF5 文件格式的 Pure Go 实现。
- [insyra](https://github.com/HazelnutParadise/insyra) - 具有统计、可视化、Parquet 支持和 Python 集成的数据分析库。
- [jsonl-graph](https://github.com/nikolaydubina/jsonl-graph) - 通过 graphviz 支持操作 JSONL 图表的工具。
- [matlab](https://github.com/scigolib/matlab) - 用于读写 MATLAB .mat 文件 (v5-v7.3) 的 Pure Go 库，无需 CGO。
- [MatProInterface.go](https://github.com/MatProGo-dev/MatProInterface.go) - MatProInterface.go 是一个开源包，用于在 Go 中定义数学程序（例如凸优化问题）。
- [matrix](https://github.com/Arceus-7/matrix) - 一个干净、通用、零依赖的 Go 矩阵数学包，支持算术、分解和线性系统求解。
- [ode](https://github.com/ChristopherRabotin/ode) - 常微分方程 (ODE) 求解器，支持扩展状态和基于通道的迭代停止条件。
- [orb](https://github.com/paulmach/orb) - 具有裁剪、GeoJSON 和 Mapbox Vector Tile 支持的 2D 几何类型。
- [pagerank](https://github.com/alixaxel/pagerank) - Go 中实现的加权 PageRank 算法。
- [piecewiselinear](https://github.com/sgreben/piecewiselinear) - 小型线性插值库。
- [PiHex](https://github.com/claygod/PiHex) - 针对十六进制数 Pi 实施“Bailey-Borwein-Plouffe”算法。
- [Poly](https://github.com/bebop/poly) - 用于工程有机体的 Go 包。
- [rootfinding](https://github.com/khezen/rootfinding) - 用于查找二次函数的根的求根算法库。
- [sparse](https://github.com/james-bowman/sparse) - 用于线性代数的 Go 稀疏矩阵格式，支持科学和机器学习应用程序，与 gonum 矩阵库兼容。
- [stats](https://github.com/montanaflynn/stats) - Golang 标准库中缺少常用函数的统计包。
- [streamtools](https://github.com/nytlabs/streamtools) - 用于处理数据流的通用图形工具。
- [taxonkit](https://github.com/shenwei356/taxonkit) - 实用高效的 NCBI 分类工具包；支持查询沿袭、重新格式化、过滤和创建自定义税务转储文件。
- [TextRank](https://github.com/DavidBelicza/TextRank) - TextRank 在 Golang 中实现，具有可扩展功能（摘要、加权、短语提取）和多线程（goroutine）支持。
- [topk](https://github.com/keilerkonzept/topk) - 基于 HeavyKeeper 算法的滑动窗口和常规 top-K 草图。
- [triangolatte](https://github.com/tchayen/triangolatte) - 二维三角测量库。允许将直线和多边形（均基于点）转换为 GPU 语言。

**[⬆ 回到顶部](#contents)**

## 安全性

_用于帮助您的应用程序更加安全的库。_

- [acmetool](https://github.com/hlandau/acme) - 具有自动续订功能的 ACME（Let's Encrypt）客户端工具。
- [acopw-go](https://sr.ht/~jamesponddotco/acopw-go/) - 适用于 Go 的小型加密安全密码生成器包。
- [acra](https://github.com/cossacklabs/acra) - 网络加密代理可保护基于数据库的应用程序免受数据泄露：强选择性加密、SQL 注入防护、入侵检测系统。
- [aes-ctr-drbg](https://github.com/sixafter/aes-ctr-drbg) - 根据 NIST SP 800-90A 中的规定，基于计数器模式 (AES-CTR-DRBG) 的 AES 的确定性随机位生成器。
- [age](https://github.com/FiloSottile/age) - 一个简单、现代且安全的加密工具（和 Go 库），具有小的显式密钥、无配置选项和 UNIX 风格的可组合性。
- [argon2-hashing](https://github.com/andskur/argon2-hashing) - Go 的 argon2 包的轻量级包装，与 Go 的标准库 Bcrypt 和 simple-scrypt 包密切相关。
- [autocert](https://pkg.go.dev/golang.org/x/crypto/acme/autocert) - 自动配置 Let's Encrypt 证书并启动 TLS 服务器。
- [BadActor](https://github.com/jaredfolkins/badactor) - 内存中、应用程序驱动的狱卒本着fail2ban 的精神构建。
- [beelzebub](https://github.com/mariocandela/beelzebub) - 安全的低代码蜜罐框架，利用人工智能进行系统虚拟化。
- [booster](https://github.com/anatol/booster) - 具有全盘加密支持的快速 initramfs 生成器。
- [canery](https://github.com/rluders/canery) - 具有可插入评估模型的最小、无状态授权引擎。
- [Cameradar](https://github.com/Ullaakut/cameradar) - 用于远程破解来自监控摄像头的 RTSP 流的工具和库。
- [certificates](https://github.com/mvmaasakkers/certificates) - 一个用于生成 tls 证书的自以为是的工具。
- [CertMagic](https://github.com/caddyserver/certmagic) - 成熟、稳健且强大的 ACME 客户端集成，用于完全托管的 TLS 证书颁发和续订。
- [Coraza](https://github.com/corazawaf/coraza) - 企业级、modsecurity 和 OWASP CRS 兼容的 WAF 库。
- [dongle](https://github.com/golang-module/dongle) - 一个简单、语义化且对开发人员友好的 golang 包，用于编码和解码以及加密和解密。
- [dotlock](https://github.com/ahmadraza100/dotlock) - 加密的 .env 保管库管理器具有交互式 TUI，用于跨多个环境和配置文件管理机密。
- [encid](https://github.com/bobg/encid) - 对加密的整数 ID 进行编码和解码。
- [entpassgen](https://github.com/andreimerlescu/entpassgen) - 熵密码生成器具有广泛的命令行参数，可安全地生成随机字符串，包括数字、密码以及使用与符号和数字混合的晦涩字典单词构建的密码。
- [firewalld-rest](https://github.com/prashantgupta24/firewalld-rest) - 用于动态更新 Linux 服务器上的防火墙规则的 REST 应用程序。
- [fort](https://github.com/djadmin/fort) - 通过 16 项检查审核 macOS 安全设置，报告分数，并在安全的情况下修复问题。单个二进制文件，可通过 Homebrew 安装。
- [go-generate-password](https://github.com/m1/go-generate-password) - 可以在 cli 上使用或作为库使用的密码生成器。
- [go-htpasswd](https://github.com/tg123/go-htpasswd) - Go 的 Apache htpasswd 解析器。
- [go-password-validator](https://github.com/lane-c-wagner/go-password-validator) - 基于原始加密熵值的密码验证器。
- [go-peer](https://github.com/number571/go-peer) - 用于创建安全和匿名去中心化系统的软件库。
- [go-yara](https://github.com/hillu/go-yara) - Go Bindings for [YARA](https://github.com/plusvic/yara)，“恶意软件研究人员（和其他人）的模式匹配瑞士刀”。
- [goArgonPass](https://github.com/dwin/goArgonPass) - Argon2 密码哈希和验证旨在与现有的 Python 和 PHP 实现兼容。
- [goSecretBoxPassword](https://github.com/dwin/goSecretBoxPassword) - 一个可能偏执的软件包，用于安全地散列和加密密码。
- [gost-crypto](https://github.com/rekurt/gost-crypto) - 由 OpenSSL gost-engine 支持的俄罗斯 GOST 加密标准（数字签名、Streebog 哈希、Kuznechik 密码、MGM AEAD）的 Go 库。
- [gspy](https://github.com/Mutasem-mk4/gspy) - 用于实时 Go 进程的取证 goroutine 到系统调用检查器。
- [Interpol](https://github.com/avahidi/interpol) - 用于模糊测试和渗透测试的基于规则的数据生成器。
- [leakhound](https://github.com/nilpoona/leakhound) - 静态分析工具可检测敏感结构字段的意外记录，防止日志中的数据泄漏。
- [lego](https://github.com/go-acme/lego) - Pure Go ACME 客户端库和 CLI 工具（与 Let's Encrypt 一起使用）。
- [luks.go](https://github.com/anatol/luks.go) - 用于管理 LUKS 分区的纯 Golang 库。
- [memguard](https://github.com/awnumar/memguard) - 用于处理内存中敏感值的纯 Go 库。
- [multikey](https://github.com/adrianosela/multikey) - 基于 Shamir 秘密共享算法的 N-out-of-N 密钥加密/解密框架。
- [nacl](https://github.com/kevinburke/nacl) - NaCL API 集的 Go 实现。
- [optimus-go](https://github.com/pjebs/optimus-go) - 使用 Knuth 算法进行 ID 哈希和混淆。
- [passlib](https://github.com/hlandau/passlib) - 面向未来的密码哈希库。
- [passwap](https://github.com/zitadel/passwap) - 提供不同密码哈希算法之间的统一实现
- [pii-shield](https://github.com/aragossa/pii-shield) - 用于 Kubernetes 的零代码日志清理 sidecar，可从日志中编辑 PII。
- [pm](https://github.com/nicola-strappazzon/password-manager) - 用 Go 编写的 Unix 风格密码管理器，通过 OpenPGP 加密保存您的数据。
- [procscope](https://github.com/Mutasem-mk4/procscope) - 流程范围的运行时调查器使用 eBPF 来跟踪流程生命周期、文件活动和网络连接。
- [qrand](https://github.com/bitfield/qrand) - ANU 量子数 (AQN) API 的客户端，提供量子力学安全的随机数据。
- [Razify](https://github.com/Hossiy21/razify) - CLI 用于扫描、验证和审核 .env 文件以查找泄露的机密和环境漂移。
- [redact](https://github.com/alesr/redact) - 使用可配置的管道从基于 slog 的日志中编辑敏感信息。
- [SafeDep/vet](https://github.com/safedep/vet) - 防范恶意开源包。
- [secret](https://github.com/rsjethani/secret) - 防止您的秘密泄露到日志、std\* 等中。
- [secure](https://github.com/unrolled/secure) - Go 的 HTTP 中间件有助于快速实现安全性。
- [secureio](https://github.com/xaionaro-go/secureio) - 基于 XChaCha20-poly1305、ECDH 和 ED25519 的“io.ReadWriteCloser”的密钥交换+身份验证+加密包装器和多路复用器。
- [simple-scrypt](https://github.com/elithrar/simple-scrypt) - Scrypt 包具有简单、明显的 API 和内置的自动成本校准。
- [ssh-vault](https://github.com/ssh-vault/ssh-vault) - 使用 ssh 密钥加密/解密。
- [sslmgr](https://github.com/adrianosela/sslmgr) - 通过 acme/autocert 的高级包装器可以轻松实现 SSL 证书。
- [teler-waf](https://github.com/kitabisa/teler-waf) - teler-waf 是一个 Go HTTP 中间件，提供 teler IDS 功能，以防御基于 Web 的攻击并提高基于 Go 的 Web 应用程序的安全性。它具有高度可配置性，并且易于集成到现有的 Go 应用程序中。
- [themis](https://github.com/cossacklabs/themis) - 用于解决典型数据安全任务（安全数据存储、安全消息传递、零知识证明身份验证）的高级密码库，可支持 14 种语言，最适合多平台应用程序。
- [urusai](https://github.com/calpa/urusai) - Urusai（日语中的“嘈杂”）是随机 HTTP/DNS 流量噪声生成器的 Go 实现，它通过在浏览时创建数字烟幕来帮助保护隐私。
- [veil](https://github.com/getveil/veil) - 本地 HTTPS 代理，对 AI 编码代理隐藏 API 凭据。操作系统钥匙串集成、格式感知占位符、SQLite 审核日志。


**[⬆ 回到顶部](#contents)**

## 序列化

_用于二进制序列化的库和工具._

- [bambam](https://github.com/glycerine/bambam) - 来自 go 的 Cap'n Proto 模式生成器。
- [bel](https://github.com/32leaves/bel) - 从 Go 结构/接口生成 TypeScript 接口。对于 JSON RPC 很有用。
- [binstruct](https://github.com/ghostiam/binstruct) - Golang 二进制解码器用于将数据映射到结构中。
- [cbor](https://github.com/fxamacker/cbor) - 小型、安全、简单的CBOR编解码库。
- [colfer](https://github.com/pascaldekloe/colfer) - Colfer 二进制格式的代码生成。
- [csvutil](https://github.com/jszwec/csvutil) - 高性能、惯用的 CSV 记录编码和解码为原生 Go 结构。
- [elastic](https://github.com/epiclabs-io/elastic) - 无论如何，在运行时在不同类型之间转换切片、映射或任何其他未知值。
- [fixedwidth](https://github.com/huydang284/fixedwidth) - 固定宽度文本格式（支持 UTF-8）。
- [fwencoder](https://github.com/o1egl/fwencoder) - Go 的固定宽度文件解析器（编码和解码库）。
- [go-capnproto](https://github.com/glycerine/go-capnproto) - Go 的 Cap'n Proto 库和解析器。
- [go-codec](https://github.com/ugorji/go) - 用于 msgpack、cbor 和 json 的高性能、功能丰富、惯用的编码、解码和 rpc 库，具有基于运行时的 OR 代码生成支持。
- [go-csvlib](https://github.com/tiendc/go-csvlib) - 高水平且功能丰富的CSV序列化/反序列化库。
- [goprotobuf](https://github.com/golang/protobuf) - 以库和协议编译器插件的形式支持 Google 的协议缓冲区。
- [gotiny](https://github.com/raszia/gotiny) - 高效的Go序列化库，gotiny几乎与生成代码的序列化库一样快。
- [jsoniter](https://github.com/json-iterator/go) - 高性能 100% 兼容的直接替换“encoding/json”。
- [mus-go](https://github.com/mus-format/mus-go) - Go 的 MUS 格式序列化器。
- [php_session_decoder](https://github.com/yvasiyarov/php_session_decoder) - 用于处理 PHP 会话格式和 PHP 序列化/反序列化函数的 GoLang 库。
- [pletter](https://github.com/vimeda/pletter) - 为消息代理包装原始消息的标准方法。
- [proto](https://github.com/emicklei/proto) - Google ProtocolBuffers .proto 文件的解析器和编写器。
- [structomap](https://github.com/tuvistavie/structomap) - 用于从静态结构轻松动态生成地图的库。
- [unitpacking](https://github.com/recolude/unitpacking) - 将单位向量打包成尽可能少的字节的库。

**[⬆ 回到顶部](#contents)**

## 服务器应用程序

- [algernon](https://github.com/xyproto/algernon) - HTTP/2 Web 服务器，内置对 Lua、Markdown、GCSS 和 Amber 的支持。
- [Caddy](https://github.com/caddyserver/caddy) - Caddy 是一种易于配置和使用的替代 HTTP/2 Web 服务器。
- [consul](https://www.consul.io/) - Consul 是一个用于服务发现、监控和配置的工具。
- [cortex-tenant](https://github.com/blind-oracle/cortex-tenant) - Prometheus 远程写入代理，根据指标标签添加 Cortex 租户 ID 标头。
- [devd](https://github.com/cortesi/devd) - 供开发人员使用的本地网络服务器。
- [discovery](https://github.com/Bilibili/discovery) - 用于弹性中间层负载平衡和故障转移的注册表。
- [dudeldu](https://github.com/krotik/dudeldu) - 一个简单的 SHOUTcast 服务器。
- [Easegress](https://github.com/megaease/easegress) - 具有可观察性和可扩展性的云原生高可用性/性能流量编排系统。
- [Engity's Bifröst](https://bifroest.engity.org/) - 高度可定制的 SSH 服务器，具有多种方式来授权用户如何执行其会话（本地或在容器中）。
- [etcd](https://github.com/etcd-io/etcd) - 用于共享配置和服务发现的高可用键值存储。
- [Euterpe](https://github.com/ironsmile/euterpe) - 自托管音乐流媒体服务器，具有内置 Web UI 和 REST API。
- [Fider](https://github.com/getfider/fider) - Fider 是一个收集和组织客户反馈的开放平台。
- [Flagr](https://github.com/checkr/flagr) - Flagr 是一项开源功能标记和 A/B 测试服务。
- [flipt](https://github.com/markphelps/flipt) - 用 Go 和 Vue.js 编写的独立功能标志解决方案
- [go-feature-flag](https://github.com/thomaspoignant/go-feature-flag) - 一个简单、完整、轻量级的自托管功能标志解决方案 100% 开源。
- [go-proxy-cache](https://github.com/fabiocicerchia/go-proxy-cache) - 带缓存的简单反向代理，用 Go 编写，使用 Redis。
- [gondola](https://github.com/bmf-san/gondola) - 基于 YAML 的 golang 反向代理。
- [goshs](https://github.com/patrickhener/goshs) - SimpleHTTPServer 替换为文件上传/下载、WebDAV、SFTP、SMB、TLS、身份验证和共享链接。
- [Kono](https://github.com/starwalkn/kono) - Go 中的轻量级可扩展 API 网关 - 并行扇出、灵活聚合和零配置魔法。
- [lets-proxy2](https://github.com/rekby/lets-proxy2) - 用于处理 https 的反向代理，并从 Lets-Encrypt 中发出证书。
- [minio](https://github.com/minio/minio) - Minio 是一个分布式对象存储服务器。
- [Moxy](https://github.com/sinhashubham95/moxy) - Moxy 是一个简单的模拟程序和代理应用程序服务器，您可以创建模拟端点以及代理请求，以防端点不存在模拟。
- [nginx-prometheus](https://github.com/blind-oracle/nginx-prometheus) - Nginx 日志解析器和 Prometheus 导出器。
- [nsq](https://nsq.io/) - 实时分布式消息平台。
- [OpenRun](https://github.com/openrundev/openrun) - Google Cloud Run 和 AWS App Runner 的开源替代品。在整个团队中轻松部署内部工具。
- [pocketbase](https://github.com/pocketbase/pocketbase) - PocketBase 是一个文件中的实时后端，由具有实时订阅、内置身份验证管理等功能的嵌入式数据库 (SQLite) 组成。
- [protoxy](https://github.com/camgraff/protoxy) - 将 JSON 请求正文转换为 Protocol Buffer 的代理服务器。
- [psql-streamer](https://github.com/blind-oracle/psql-streamer) - 将数据库事件从 PostgreSQL 流式传输到 Kafka。
- [riemann-relay](https://github.com/blind-oracle/riemann-relay) - 中继负载平衡黎曼事件和/或将其转换为 Carbon。
- [RoadRunner](https://github.com/spiral/roadrunner) - 高性能 PHP 应用服务器、负载均衡器和进程管理器。
- [SFTPGo](https://github.com/drakkan/sftpgo) - 功能齐全且高度可配置的 SFTP 服务器，具有可选的 FTP/S 和 WebDAV 支持。它可以为本地文件系统和云存储后端（例如 S3 和 Google Cloud Storage）提供服务。
- [Trickster](https://github.com/tricksterproxy/trickster) - HTTP 反向代理缓存和时间序列加速器。
- [wd-41](https://github.com/baalimago/wd-41) - 一个 (w)eb (d) 开发服务器，可在文件更改时自动实时重新加载。
- [Wish](https://github.com/charmbracelet/wish) - 制作 SSH 应用程序，就像那样！
- [Kono](https://github.com/starwalkn/kono) - Go 中的轻量级可扩展 API 网关 - 并行扇出、灵活聚合和零配置魔法。

**[⬆ 回到顶部](#contents)**

## 流处理

_用于流处理和反应式编程的库和工具。_

- [go-etl](https://github.com/Breeze0806/go-etl) - 用于数据源提取、转换和加载 (ETL) 的轻量级工具包。
- [go-streams](https://github.com/reugn/go-streams) - Go 流处理库。
- [goio](https://github.com/primetalk/goio) - Golang 的 IO、Stream、Fiber 的实现，受到出色的 Scala 库 cats 和 fs2 的启发。
- [gostream](https://github.com/mariomac/gostream) - 受 Java Streams API 启发的类型安全流处理库。
- [machine](https://github.com/whitaker-io/machine) - 用于编写和生成具有内置指标和可追溯性的流工作程序的 Go 库。
- [nibbler](https://github.com/naughtygopher/nibbler) - 用于微批量处理的轻量级软件包。
- [ro](https://github.com/samber/ro) - 响应式编程：用于事件驱动应用程序的声明式和可组合 API。
- [signals](https://github.com/coregx/signals) - 类型安全的反应式状态管理受到 Angular Signals 的启发，具有计算值、效果和依赖性跟踪。
- [stream](https://github.com/youthlin/stream) - Go Stream，如 Java 8 Stream：Filter/Map/FlatMap/Peek/Sorted/ForEach/Reduce...
- [StreamSQL](https://github.com/rulego/streamsql) - 用于实时数据处理的轻量级流式 SQL 引擎。

**[⬆ 回到顶部](#contents)**

## 模板引擎

_用于模板和词法分析的库和工具。_

- [bagme](https://github.com/boxesandglue/bagme) - HTML/CSS 到 PDF 的渲染，在纯 Go 中使用 TeX 质量的排版。
- [ego](https://github.com/benbjohnson/ego) - 轻量级模板语言，可让您在 Go 中编写模板。模板被翻译成 Go 并编译。
- [fasttemplate](https://github.com/valyala/fasttemplate) - 简单快速的模板引擎。替换模板占位符的速度比 [text/template](https://golang.org/pkg/text/template/) 快 10 倍。
- [gomponents](https://www.gomponents.com) - 纯 Go 中的 HTML 5 组件，看起来像这样：`func(name string) g.Node { return Div(Class("headline"), g.Textf("Hi %v!", name)) }`。
- [got](https://github.com/goradd/got) - 受 Hero 和 Fasttemplate 启发的 Go 代码生成器。包含文件、自定义标签定义、注入的 Go 代码、语言翻译等。
- [goview](https://github.com/foolin/goview) - Goview 是一个基于 golang html/template 的轻量级、简约且惯用的模板库，用于构建 Go Web 应用程序。
- [gox](https://github.com/doors-dev/gox) - HTML 模板作为一流的 Go 表达式，具有无缝编辑器支持。
- [htmgo](https://htmgo.dev) - 使用 go + htmx 构建简单且可扩展的系统
- [jet](https://github.com/CloudyKit/jet) - Jet 模板引擎。
- [liquid](https://github.com/osteele/liquid) - 实施 Shopify Liquid 模板。
- [maroto](https://github.com/johnfercher/maroto) - 创建 PDF 的 maroto 方法。 Maroto 受到 Bootstrap 的启发并使用 gofpdf。快速而简单。
- [pongo2](https://github.com/flosch/pongo2) - 类似 Django 的 Go 模板引擎。
- [quicktemplate](https://github.com/valyala/quicktemplate) - 快速、强大且易于使用的模板引擎。将模板转换为 Go 代码，然后编译。
- [Razor](https://github.com/sipin/gorazor) - Golang 的 Razor 视图引擎。
- [Soy](https://github.com/robfig/soy) - Go 的闭包模板（又名 Soy 模板），遵循 [官方规范](https://developers.google.com/closure/templates/)。
- [sprout](https://github.com/go-sprout/sprout) - Go 模板的有用模板函数。
- [tbd](https://github.com/lucasepe/tbd) - 使用占位符创建文本模板的一种非常简单的方法 - 公开额外的内置 Git 存储库元数据。
- [templ](https://github.com/a-h/templ) - 一种 HTML 模板语言，拥有出色的开发人员工具。
- [templator](https://github.com/alesr/templator) - Go 的类型安全 HTML 模板渲染引擎。

**[⬆ 回到顶部](#contents)**

## 测试

_用于测试代码库和生成测试数据的库。_

### 测试框架

- [apitest](https://apitest.dev) - 用于基于 REST 的服务或 HTTP 处理程序的简单且可扩展的行为测试库，支持模拟外部 http 调用和序列图的呈现。
- [arch-go](https://github.com/arch-go/arch-go) - Go 项目的架构测试工具。
- [assay](https://github.com/tushariitr-19/assay) - 与框架无关的评估库，用于通过确定性检查、CI 就绪退出代码和基于 YAML 的零代码测试来测试 Go 代理和 MCP 服务器。
- [assert](https://github.com/go-playground/assert) - 基本断言库与本机 go 测试一起使用，并带有用于自定义断言的构建块。
- [baloo](https://github.com/h2non/baloo) - 富有表现力且多功能的端到端 HTTP API 测试变得简单。
- [be](https://github.com/carlmjohnson/be) - 极简通用测试断言库。
- [biff](https://github.com/fulldump/biff) - 分叉测试框架，兼容BDD。
- [charlatan](https://github.com/percolate/charlatan) - 为测试生成假接口实现的工具。
- [commander](https://github.com/SimonBaeumer/commander) - 用于在 Windows、Linux 和 osx 上测试 cli 应用程序的工具。
- [cupaloy](https://github.com/bradleyjkemp/cupaloy) - 适用于您的测试框架的简单快照测试插件。
- [dbcleaner](https://github.com/khaiql/dbcleaner) - 用于测试目的的清理数据库，受到 Ruby 中“database_cleaner”的启发。
- [dft](https://github.com/abecodes/dft) - 用于测试（或更多）的轻量级、零依赖 Docker 容器。
- [dsunit](https://github.com/viant/dsunit) - SQL、NoSQL、结构化文件的数据存储测试。
- [embedded-postgres](https://github.com/fergusstrange/embedded-postgres) - 作为另一个 Go 应用程序或测试的一部分，在 Linux、OSX 或 Windows 上本地运行真实的 Postgres 数据库。
- [endly](https://github.com/viant/endly) - 声明式端到端功能测试。
- [envite](https://github.com/PerimeterX/envite) - 开发和测试环境管理框架。
- [fixenv](https://github.com/rekby/fixenv) - 夹具管理引擎，受到 pytest 夹具的启发。
- [flute](https://github.com/suzuki-shunsuke/flute) - HTTP 客户端测试框架。
- [frisby](https://github.com/verdverm/frisby) - REST API 测试框架。
- [gherkingen](https://github.com/hedhyw/gherkingen) - BDD 样板生成器和框架。
- [ginkgo](https://onsi.github.io/ginkgo/) - Go 的 BDD 测试框架。
- [gnomock](https://github.com/orlangure/gnomock) - 与在 Docker 中运行的真实依赖项（数据库、缓存，甚至 Kubernetes 或 AWS）进行集成测试，无需模拟。
- [go-carpet](https://github.com/msoap/go-carpet) - 用于在终端中查看测试覆盖率的工具。
- [go-cmp](https://github.com/google/go-cmp) - 用于在测试中比较 Go 值的包。
- [go-hit](https://github.com/Eun/go-hit) - Hit是一个用golang编写的http集成测试框架。
- [go-httpbin](https://github.com/mccutchen/go-httpbin) - HTTP 测试和调试工具，具有用于客户端测试的各种端点。
- [go-mutesting](https://github.com/jonbaldie/go-mutesting) - 使用 CI 质量门、覆盖感知 MSI、基线跟踪和 git-diff 过滤对 Go 进行突变测试。
- [go-mysql-test-container](https://github.com/arikama/go-mysql-test-container) - Golang MySQL testcontainer 帮助进行 MySQL 集成测试。
- [go-snaps](http://github.com/gkampitakis/go-snaps) - Golang 中类似玩笑的快照测试。
- [go-test-coverage](https://github.com/vladopajic/go-test-coverage) - 报告低于设定阈值的文件覆盖率的工具。
- [go-testdeep](https://github.com/maxatome/go-testdeep) - 极其灵活的golang深度比较，扩展了go测试包。
- [go-testing](https://github.com/tkrop/go-testing) - Go 测试扩展，允许简单设置强隔离的单元、组件和集成测试，提供扩展 gomock 和 gock 的高级模拟支持。
- [go-testpredicate](https://github.com/maargenton/go-testpredicate) - 具有广泛诊断输出的测试谓词样式断言库。
- [go-vcr](https://github.com/dnaeon/go-vcr) - 记录并重播您的 HTTP 交互，以进行快速、确定性和准确的测试。
- [goblin](https://github.com/franela/goblin) - Mocha 类似 Go 的测试框架。
- [goc](https://github.com/qiniu/goc) - Goc 是 Go 编程语言的综合覆盖率测试系统。
- [gocheck](https://labix.org/gocheck) - 更先进的测试框架替代 gotest。
- [GoConvey](https://github.com/smartystreets/goconvey/) - 具有 Web UI 和实时重新加载的 BDD 风格框架。
- [gocrest](https://github.com/corbym/gocrest) - 用于 Go 断言的可组合的类似 hamcrest 的匹配器。
- [godog](https://github.com/cucumber/godog) - Go 的 Cucumber BDD 框架。
- [gofight](https://github.com/appleboy/gofight) - Golang 路由器框架的 API 处理程序测试。
- [gogiven](https://github.com/corbym/gogiven) - 类似于 YATSPEC 的 Go BDD 测试框架。
- [gomatch](https://github.com/jfilipczyk/gomatch) - 创建用于根据模式测试 JSON 的库。
- [gomega](https://onsi.github.io/gomega/) - Rspec 类似匹配器/断言库。
- [Gont](https://github.com/stv0g/gont) - Go 网络测试工具包，用于测试使用 Linux 命名空间构建复杂的网络拓扑。
- [gospecify](https://github.com/stesla/gospecify) - 这提供了用于测试 Go 代码的 BDD 语法。使用过 rspec 等库的任何人都应该熟悉它。
- [gosuite](https://github.com/pavlo/gosuite) - 通过利用 Go1.7 的子测试，将具有设置/拆卸功能的轻量级测试套件引入“测试”。
- [got](https://github.com/ysmood/got) - 一个令人愉快的 golang 测试框架。
- [gotest.tools](https://github.com/gotestyourself/gotest.tools) - 用于增强 go 测试包并支持常见模式的包集合。
- [Hamcrest](https://github.com/rdrdr/hamcrest) - 用于声明性 Matcher 对象的流畅框架，当应用于输入值时，会产生自描述结果。
- [httpexpect](https://github.com/gavv/httpexpect) - 简洁、声明性且易于使用的端到端 HTTP 和 REST API 测试。
- [is](https://github.com/matryer/is) - 专业的 Go 轻量级测试迷你框架。
- [jsonassert](https://github.com/kinbiko/jsonassert) - 用于验证 JSON 有效负载是否正确序列化的包。
- [keploy](https://github.com/keploy/keploy) - 自动从 API 调用生成测试用例和数据模拟。
- [omg.testingtools](https://github.com/dedalqq/omg.testingtools) - 用于更改私有字段值以进行测试的简单库。
- [restit](https://github.com/yookoala/restit) - Go 微框架帮助编写 RESTful API 集成测试。
- [schema](https://github.com/jgroeneveld/schema) - 对请求和响应中使用的 JSON 模式进行快速、简单的表达式匹配。
- [should](https://github.com/Kairum-Labs/should) - 具有零依赖性、详细的结构差异和人类可读的错误消息的测试库。
- [stop-and-go](https://github.com/elgohr/stop-and-go) - 测试并发性的助手。
- [testcase](https://github.com/adamluzsi/testcase) - 行为驱动开发的惯用测试框架。
- [testcerts](https://github.com/madflojo/testcerts) - 在测试函数中动态生成自签名证书和证书颁发机构。
- [testcontainers-go](https://github.com/testcontainers/testcontainers-go) - 一个 Go 包，可以轻松创建和清理基于容器的依赖项以进行自动化集成/冒烟测试。干净、易于使用的 API 使开发人员能够以编程方式定义应作为测试一部分运行的容器，并在测试完成后清理这些资源。
- [testfixtures](https://github.com/go-testfixtures/testfixtures) - Rails 类似测试装置的助手，用于测试数据库应用程序。
- [Testify](https://github.com/stretchr/testify) - 标准 go 测试包的神圣扩展。
- [Testo](https://github.com/ozontech/testo) - 基于插件的测试框架，具有套件、并行测试、挂钩和参数化。受到 Pytest 的启发。
- [testsql](https://github.com/zhulongcheng/testsql) - 测试前从SQL文件生成测试数据，测试完成后清除。
- [testza](https://github.com/MarvinJWendt/testza) - 功能齐全的测试框架，具有漂亮的彩色输出。
- [tparse](https://github.com/mfridman/tparse) - 用于总结 go 测试输出的 CLI 工具。管道友好。与 go 测试标志兼容。
- [trial](https://github.com/jgroeneveld/trial) - 快速简单的可扩展断言，无需引入太多样板文件。
- [Tt](https://github.com/vcaesar/tt) - 简单而丰富多彩的测试工具。
- [wstest](https://github.com/posener/wstest) - 用于对 websocket http.Handler 进行单元测试的 Websocket 客户端。

### 模拟

- [connexions](https://github.com/cubahno/connexions) - 基于 OpenAPI 3.0 规范和文件，将多个 API 与有意义的响应、可配置延迟和错误代码相结合。
- [counterfeiter](https://github.com/maxbrunsfeld/counterfeiter) - 用于生成独立模拟对象的工具。
- [genmock](https://gitlab.com/so_literate/genmock) - 使用代码生成器来模拟系统，用于构建接口方法的调用。
- [go-localstack](https://github.com/elgohr/go-localstack) - 在 AWS 测试中使用 localstack 的工具。
- [go-sqlmock](https://github.com/DATA-DOG/go-sqlmock) - 用于测试数据库交互的模拟 SQL 驱动程序。
- [go-txdb](https://github.com/DATA-DOG/go-txdb) - 基于单事务的数据库驱动程序主要用于测试目的。
- [gomock](https://github.com/uber-go/mock) - Go 编程语言的模拟框架。
- [gomock](https://github.com/vibridi/gomock) - 用于生成类型化和与框架无关的接口模拟的 CLI 工具，并支持泛型。
- [govcr](https://github.com/seborama/govcr) - Golang 的 HTTP 模拟：记录和重放 HTTP 交互以进行离线测试。
- [hoverfly](https://github.com/SpectoLabs/hoverfly) - HTTP(S) 代理，用于通过可扩展的中间件和易于使用的 CLI 记录和模拟 REST/SOAP API。
- [httpmock](https://github.com/jarcoal/httpmock) - 轻松模拟来自外部资源的 HTTP 响应。
- [minimock](https://github.com/gojuno/minimock) - Go 接口的模拟生成器。
- [mockery](https://github.com/vektra/mockery) - 生成 Go 接口的工具。
- [mockfs](https://github.com/balinomad/go-mockfs) - 用于 Go 测试的模拟文件系统，具有错误注入和延迟模拟，构建于“testing/fstest.MapFS”之上。
- [mockhttp](https://github.com/tv42/mockhttp) - Go http.ResponseWriter 的模拟对象。
- [mooncake](https://github.com/GuilhermeCaruso/mooncake) - 一种为多种目的生成模拟的简单方法。
- [moq](https://github.com/matryer/moq) - 从任何接口生成结构的实用程序。该结构可以在测试代码中用作接口的模拟。
- [moxie](https://lesiw.io/moxie) - 在嵌入式结构上生成模拟方法。
- [pgxmock](https://github.com/pashagolub/pgxmock) - 一个实现 [pgx - PostgreSQL 驱动程序和工具包](https://github.com/jackc/pgx/) 的模拟库。
- [timex](https://github.com/cabify/timex) - 原生“time”包的测试友好替代品。
- [xgo](https://github.com/xhd2015/xgo) - 一个通用的专用函数模拟库。

### 模糊测试和增量调试/减少/收缩

- [go-fuzz](https://github.com/dvyukov/go-fuzz) - 随机测试系统。
- [Tavor](https://github.com/zimmski/tavor) - 通用模糊测试和增量调试框架。

### Selenium 和浏览器控制工具

- [bonk](https://github.com/joakimcarlsson/bonk) - 快速、隐秘优先的浏览器自动化库，使用基于 WebSocket 的 Chrome DevTools 协议，无需外部依赖。
- [cdp](https://github.com/mafredri/cdp) - Chrome 调试协议的类型安全绑定，可与实现该协议的浏览器或其他调试目标一起使用。
- [chromedp](https://github.com/knq/chromedp) - 一种驱动/测试 Chrome、Safari、Edge、Android Webview 和其他支持 Chrome 调试协议的浏览器的方法。
- [playwright-go](https://github.com/mxschmitt/playwright-go) - 浏览器自动化库，可使用单个 API 控制 Chromium、Firefox 和 WebKit。
- [rod](https://github.com/go-rod/rod) - 一个 Devtools 驱动程序，使 Web 自动化和抓取变得容易。
- [selenosis](https://github.com/alcounit/selenosis) - 无状态 Kubernetes 原生中心，通过自定义资源将 Selenium、Playwright 和 MCP 会话路由到按需浏览器 Pod。

### 注入失败

- [failpoint](https://github.com/pingcap/failpoint) - Golang 的 [failpoints](https://www.freebsd.org/cgi/man.cgi?query=fail) 实现。

**[⬆ 回到顶部](#contents)**

## 文本处理

_用于解析和操作文本的库._

另请参阅[自然语言处理](#natural-language-processing) 和[文本分析](#text-analysis)。

### 格式化程序

- [address](https://github.com/bojanz/address) - 处理地址表示、验证和格式化。
- [align](https://github.com/Guitarbum722/align) - 对齐文本的通用应用程序。
- [bytes](https://github.com/labstack/gommon/tree/master/bytes) - 格式化并解析数字字节值（10K、2M、3G 等）。
- [go-fixedwidth](https://github.com/ianlopshire/go-fixedwidth) - 固定宽度文本格式（带反射的编码器/解码器）。
- [go-humanize](https://github.com/dustin/go-humanize) - 将时间、数字和内存大小格式化为人类可读的格式。
- [gotabulate](https://github.com/bndr/gotabulate) - 使用 Go 轻松漂亮地打印表格数据。
- [sq](https://github.com/neilotoole/sq) - 将 SQL 数据库或 CSV 或 Excel 等文档格式的数据转换为 JSON、Excel、CSV、HTML、Markdown、XML 和 YAML 等格式。
- [textwrap](https://github.com/isbm/textwrap) - 在行尾换行文本。 Python 中“textwrap”模块的实现。

### 标记语言

- [bafi](https://github.com/mmalcek/bafi) - 使用模板将通用 JSON、BSON、YAML、XML 转换为任何格式。
- [bbConvert](https://github.com/CalebQ42/bbConvert) - 将 bbCode 转换为 HTML，允许您添加对自定义 bbCode 标签的支持。
- [blackfriday](https://github.com/russross/blackfriday) - Go 中的 Markdown 处理器。
- [go-output-format](https://github.com/drewstinnett/go-output-format) - 在命令行应用程序中将 go 结构输出为多种格式（YAML/JSON/等）。
- [go-toml](https://github.com/pelletier/go-toml) - 用于 TOML 格式的 Go 库，具有查询支持和方便的 cli 工具。
- [goldmark](https://github.com/yuin/goldmark) - 用 Go 编写的 Markdown 解析器。易于扩展、符合标准 (CommonMark)、结构良好。
- [goq](https://github.com/andrewstuart/goq) - 使用带有 jQ​​uery 语法的结构标记对 HTML 进行声明性解组（使用 GoQuery）。
- [html-to-markdown](https://github.com/JohannesKaufmann/html-to-markdown) - 将 HTML 转换为 Markdown。甚至可以与整个网站一起使用，并且可以通过规则进行扩展。
- [htmlquery](https://github.com/antchfx/htmlquery) - HTML 的 XPath 查询包允许您通过 XPath 表达式从 HTML 文档中提取数据或求值。
- [htmlyaml](https://github.com/nikolaydubina/htmlyaml) - 在 Go 中将 YAML 丰富地呈现为 HTML。
- [htree](https://github.com/bobg/htree) - 遍历、导航、过滤和以其他方式处理 [html.Node](https://pkg.go.dev/golang.org/x/net/html#Node) 对象的树。
- [mdsmith](https://github.com/jeduden/mdsmith) - 快速、自动修复 Markdown linter 和格式化程序。检查样式、可读性、结构和跨文件完整性。
- [mxj](https://github.com/clbanning/mxj) - 将 XML 编码/解码为 JSON 或 map[string]interface{}；使用点符号路径和通配符提取值。替换 x2j 和 j2x 软件包。
- [picoloom](https://github.com/alnah/picoloom) - 具有 CLI 和 Go 库 API 的 Markdown 到 PDF 转换器。
- [toml](https://github.com/BurntSushi/toml) - TOML 配置格式（带反射的编码器/解码器）。

### 解析器/编码器/解码器

- [allot](https://github.com/sbstjn/allot) - CLI 工具和机器人的占位符和通配符文本解析。
- [codetree](https://github.com/aerogo/codetree) - 解析缩进代码（python、pixy、scarlet 等）并返回树结构。
- [commonregex](https://github.com/mingrammer/commonregex) - Go 常用正则表达式的集合。
- [did](https://github.com/ockam-network/did) - Go 中的 DID（分散标识符）解析器和 Stringer。
- [doi](https://github.com/hscells/doi) - Go 中的文档对象标识符 (doi) 解析器。
- [editorconfig-core-go](https://github.com/editorconfig/editorconfig-core-go) - Go 的 Editorconfig 文件解析器和操纵器。
- [encdec](https://github.com/mickep76/encdec) - 包为编码器和解码器提供通用接口。
- [go-fasttld](https://github.com/elliotwutingfeng/go-fasttld) - 高性能有效顶级域名 (eTLD) 提取模块。
- [go-nmea](https://github.com/adrianmo/go-nmea) - Go 语言的 NMEA 解析器库。
- [go-querystring](https://github.com/google/go-querystring) - 用于将结构编码为 URL 查询参数的 Go 库。
- [go-vcard](https://github.com/emersion/go-vcard) - 解析并格式化 vCard。
- [godump](https://github.com/yassinebenaid/godump) - 轻松漂亮地打印任何 GO 变量，这是 Go 的 `fmt.Printf("%#v")` 的替代方案。
- [godump (goforj)](https://github.com/goforj/godump) - 漂亮的 Go 结构，具有 Laravel/Symfony 风格的转储、完整类型信息、彩色 CLI 输出、循环检测和私有字段访问。
- [gofeed](https://github.com/mmcdole/gofeed) - 在 Go 中解析 RSS 和 Atom feed。
- [gographviz](https://github.com/awalterschulze/gographviz) - 解析 Graphviz DOT 语言。
- [gonameparts](https://github.com/polera/gonameparts) - 将人名解析为单独的名称部分。
- [ltsv](https://github.com/Wing924/ltsv) - 适用于 Go 的高性能 [LTSV（标签制表符分隔值）](http://ltsv.org/) 阅读器。
- [normalize](https://github.com/avito-tech/normalize) - 清理、标准化和比较模糊文本。
- [parseargs-go](https://github.com/nproc/parseargs-go) - 理解引号和反斜杠的字符串参数解析器。
- [prattle](https://github.com/askeladdk/prattle) - 简单高效地扫描和解析 LL(1) 语法。
- [sh](https://github.com/mvdan/sh) - Shell 解析器和格式化器。
- [tokenizer](https://github.com/bzick/tokenizer) - 将任何字符串、切片或无限缓冲区解析为任何标记。
- [vdf](https://github.com/andygrunwald/vdf) - 用 Go 编写的 Valve 数据格式（称为 vdf）的词法分析器和解析器。
- [when](https://github.com/olebedev/when) - 具有可插入规则的自然 EN 和 RU 语言日期/时间解析器。
- [xj2go](https://github.com/stackerzzq/xj2go) - 将 xml 或 json 转换为 go 结构。

### 正则表达式

- [coregex](https://github.com/coregx/coregex) - 采用 Rust regex-crate 架构的生产正则表达式引擎：多引擎 DFA/NFA、SIMD 预过滤器、嵌入式 stdlib 替换。
- [genex](https://github.com/alixaxel/genex) - 计算正则表达式并将其扩展为所有匹配的字符串。
- [go-wildcard](https://github.com/IGLOU-EU/go-wildcard) - 简单轻量的通配符模式匹配。
- [goregen](https://github.com/zach-klippenstein/goregen) - 用于从正则表达式生成随机字符串的库。
- [regroup](https://github.com/oriser/regroup) - 使用结构标签和自动解析将正则表达式命名组匹配到 go 结构中。
- [rex](https://github.com/hedhyw/rex) - 正则表达式生成器。

### 环境卫生

- [bluemonday](https://github.com/microcosm-cc/bluemonday) - HTML 消毒剂。
- [gofuckyourself](https://github.com/JoshuaDoes/gofuckyourself) - 一个基于清理的 Go 脏话过滤器。

### 刮刀

- [colly](https://github.com/asciimoo/colly) - 快速而优雅的 Gophers 抓取框架。
- [dataflowkit](https://github.com/slotix/dataflowkit) - 网络抓取框架将网站转化为结构化数据。
- [go-recipe](https://github.com/kkyr/go-recipe) - 用于从网站上抓取食谱的包。
- [go-sitemap-parser](https://github.com/aafeher/go-sitemap-parser) - 用于解析站点地图的 Go 语言库。
- [GoQuery](https://github.com/PuerkitoBio/goquery) - GoQuery 为 Go 语言带来了类似于 jQuery 的语法和一组功能。
- [pagser](https://github.com/foolin/pagser) - Pagser 是一个简单、可扩展、可配置的解析和反序列化 html 页面，以基于 goquery 和 struct 标签为 golang 爬虫构建结构。
- [Tagify](https://github.com/zoomio/tagify) - 从给定源生成一组标签。
- [walker](https://github.com/cyucelen/walker) - 从任何来源无缝获取分页数据。包括简单且高性能的 API 抓取。
- [xurls](https://github.com/mvdan/xurls) - 从文本中提取 url。

### RSS

- [podcast](https://github.com/eduncan911/podcast) - Golang 中的 iTunes 兼容和 RSS 2.0 播客生成器

### 实用/杂项

- [ahocorasick](https://github.com/coregx/ahocorasick) - 高性能 Aho-Corasick 多模式字符串匹配，具有 DFA 编译和 SIMD 预过滤器，吞吐量高达 7 GB/s（[coregx](https://github.com/coregx) 生态系统的一部分）。
- [go-runewidth](https://github.com/mattn/go-runewidth) - 获取字符或字符串的固定宽度的函数。
- [kace](https://github.com/codemodus/kace) - 常见的大小写转换涵盖常见的缩写。
- [lancet](https://github.com/duke-git/lancet) - 一个类似于 Lodash 的综合性 Go 实用程序库
- [petrovich](https://github.com/striker2000/petrovich) - Petrovich 是根据给定语法情况变化俄语名字的库。
- [radix](https://github.com/yourbasic/radix) - 快速字符串排序算法。
- [TySug](https://github.com/Dynom/TySug) - 关于键盘布局的替代建议。
- [uniwidth](https://github.com/unilibs/uniwidth) - 具有 SWAR 优化、O(1) 查找表和 ZWJ 表情符号支持的高性能 Unicode 字符宽度计算。
- [w2vgrep](https://github.com/arunsupe/semantic-grep) - 语义 grep 工具，使用单词嵌入来查找语义相似的匹配项。例如，搜索“死亡”将找到“死”、“杀戮”、“谋杀”。

**[⬆ 回到顶部](#contents)**

## 第三方API

_用于访问第三方 API 的库。_

- [airtable](https://github.com/mehanizm/airtable) - 转到 [Airtable API](https://airtable.com/api) 的客户端库。
- [anaconda](https://github.com/ChimeraCoder/anaconda) - Twitter 1.1 API 的 Go 客户端库。
- [appstore-sdk-go](https://github.com/Kachit/appstore-sdk-go) - 用于 AppStore Connect API 的非官方 Golang SDK。
- [aws-encryption-sdk-go](https://github.com/chainifynet/aws-encryption-sdk-go) - [AWS 加密 SDK](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/index.html) 的非官方 Go SDK 实现。
- [aws-sdk-go](https://github.com/aws/aws-sdk-go-v2) - 适用于 Go 编程语言的官方 AWS 开发工具包。
- [bqwriter](https://github.com/OTA-Insight/bqwriter) - 高级 Go 库以高吞吐量将数据写入 [Google BigQuery](https://cloud.google.com/bigquery)。
- [brewerydb](https://github.com/naegelejd/brewerydb) - 用于访问 BreweryDB API 的 Go 库。
- [cachet](https://github.com/andygrunwald/cachet) - [Cachet（开源状态页面系统）](https://cachethq.io/) 的客户端库。
- [circleci](https://github.com/jszwedko/go-circleci) - 用于与 CircleCI 的 API 交互的 Go 客户端库。
- [clarifai](https://github.com/samuelcouch/clarifai) - 用于与 Clarifai API 接口的 Go 客户端库。
- [codeship-go](https://github.com/codeship/codeship-go) - 用于与 Codeship 的 API v2 交互的 Go 客户端库。
- [coinpaprika-go](https://github.com/coinpaprika/coinpaprika-api-go-client) - 用于与 Coinpaprika 的 API 交互的 Go 客户端库。
- [colony-sdk-go](https://github.com/TheColonyCC/colony-sdk-go) - Go 客户端库 [The Colony](https://thecolony.cc) — 一个公共社交网络，其用户是人工智能代理。
- [device-check-go](https://github.com/rinchsan/device-check-go) - 用于与 [iOS DeviceCheck API](https://developer.apple.com/documentation/devicecheck) 交互的 Go 客户端库 v1.
- [discordgo](https://github.com/bwmarrin/discordgo) - Go 绑定 Discord Chat API。
- [disgo](https://github.com/switchupcb/disgo) - Discord API 的 Go API 包装器。
- [dusupay-sdk-go](https://github.com/Kachit/dusupay-sdk-go) - Go 的非官方 Dusupay 支付网关 API 客户端
- [ethrpc](https://github.com/onrik/ethrpc) - 以太坊 JSON RPC API 的 Go 绑定。
- [facebook](https://github.com/huandu/facebook) - 支持 Facebook Graph API 的 Go 库。
- [fasapay-sdk-go](https://github.com/Kachit/fasapay-sdk-go) - 适用于 Golang 的非官方 Fasapay 支付网关 XML API 客户端。
- [fcm](https://github.com/maddevsio/fcm) - Firebase 云消息传递的 Go 库。
- [gads](https://github.com/emiddleton/gads) - Google Adwords 非官方 API。
- [gcm](https://github.com/Aorioli/gcm) - 用于 Google Cloud Messaging 的 Go 库。
- [geo-golang](https://github.com/codingsince1985/geo-golang) - 前往图书馆访问 [Google 地图](https://developers.google.com/maps/documentation/geocoding/intro)、[MapQuest](https://developer.mapquest.com/documentation/api/geocoding/)、[Nominatim](https://nominatim.org/release-docs/latest/api/Overview/)、[OpenCage](https://opencagedata.com/api)、 [Bing](https://msdn.microsoft.com/en-us/library/ff701715.aspx)、[Mapbox](https://www.mapbox.com/developers/api/geocoding/) 和 [OpenStreetMap](https://wiki.openstreetmap.org/wiki/Nominatim) 地理编码/反向地理编码 API。
- [github](https://github.com/google/go-github) - 用于访问 GitHub REST API v3 的 Go 库。
- [githubql](https://github.com/shurcooL/githubql) - 用于访问 GitHub GraphQL API v4 的 Go 库。
- [go-atlassian](https://github.com/ctreminiom/go-atlassian) - 用于访问 [Atlassian Cloud](https://www.atlassian.com/enterprise/cloud) 服务（Jira、Jira Service Management、Jira Agile、Confluence、Admin Cloud）的 Go 库
- [go-aws-news](https://github.com/circa10a/go-aws-news) - 转到应用程序和库以从 AWS 获取新内容。
- [go-chronos](https://github.com/axelspringer/go-chronos) - 用于与 [Chronos](https://mesos.github.io/chronos/) 作业调度程序交互的 Go 库
- [go-gerrit](https://github.com/andygrunwald/go-gerrit) - 转到客户端库进行 [Gerrit Code Review](https://www.gerritcodereview.com/)。
- [go-hacknews](https://github.com/PaulRosset/go-hacknews) - HackerNews API 的微型 Go 客户端。
- [go-here](https://github.com/abdullahselek/go-here) - 使用基于 HERE 位置的 API 的客户端库。
- [go-hibp](https://github.com/wneessen/go-hibp) - 简单的 Go 绑定到“Have I Been Pwned”API。
- [go-imgur](https://github.com/koffeinsource/go-imgur) - Go 客户端库 [imgur](https://imgur.com)
- [go-jira](https://github.com/andygrunwald/go-jira) - [Atlassian JIRA] 的 Go 客户端库(https://www.atlassian.com/software/jira)
- [go-lark](https://github.com/go-lark/lark) - 一款简单易用的【飞书】(https://open.feishu.cn/)和【Lark】(https://open.larksuite.com/)开放平台非官方SDK。
- [go-marathon](https://github.com/gambol99/go-marathon) - 用于与 Mesosphere 的 Marathon PAAS 交互的 Go 库。
- [go-myanimelist](https://github.com/nstratos/go-myanimelist) - 用于访问 [MyAnimeList API](https://myanimelist.net/apiconfig/references/api/v2) 的客户端库。
- [go-openai](https://github.com/sashabaranov/go-openai) - OpenAI ChatGPT、DALL·E、Go 的 Whisper API 库。
- [go-openproject](https://github.com/manuelbcd/go-openproject) - 用于与 [OpenProject](https://docs.openproject.org/api/) API 交互的 Go 客户端库。
- [go-postman-collection](https://github.com/rbretecher/go-postman-collection) - Go 模块可与 [Postman Collections](https://learning.getpostman.com/docs/postman/collections/creating-collections/) 配合使用（与 Insomnia 兼容）。
- [go-redoc](https://github.com/mvrilo/go-redoc) - 使用 [ReDoc](https://redocly.com/) 嵌入 Go 的 OpenAPI/Swagger 文档 ui。
- [go-restcountries](https://github.com/chriscross0/go-restcountries) - [REST Country API](https://countrylayer.com/) 的 Go 库。
- [go-salesforce](https://github.com/k-capehart/go-salesforce) - 用于与 [S​​alesforce REST API](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/resources_list.htm) 交互的客户端库。
- [go-sophos](https://github.com/esurdam/go-sophos) - Go 具有零依赖性的 [Sophos UTM REST API](https://www.sophos.com/en-us/medialibrary/PDFs/documentation/UTMonAWS/Sophos-UTM-RESTful-API.pdf?la=en) 客户端库。
- [go-swagger-ui](https://github.com/esurdam/go-swagger-ui) - 包含预编译的 [Swagger UI](https://swagger.io/tools/swagger-ui/) 的 Go 库，用于提供 swagger json。
- [go-telegraph](https://gitlab.com/toby3d/telegraph) - Telegraph 发布平台 API 客户端。
- [go-trending](https://github.com/andygrunwald/go-trending) - 用于访问 Github 上的 [趋势存储库](https://github.com/trending) 和 [开发人员](https://github.com/trending/developers) 的 Go 库。
- [go-unsplash](https://github.com/hbagdi/go-unsplash) - 转到 [Unsplash.com](https://unsplash.com) API 的客户端库。
- [go-xkcd](https://github.com/nishanths/go-xkcd) - 转到 xkcd API 的客户端。
- [go-yapla](https://gitlab.com/adrienK/go-yapla) - Yapla v2.0 API 的 Go 客户端库。
- [goagi](https://github.com/staskobzar/goagi) - 用于构建 Asterisk PBX agi/fastagi 应用程序的 Go 库。
- [goami2](https://github.com/staskobzar/goami2) - Asterisk PBX 的 AMI v2 库。
- [GoFreeDB](https://github.com/FreeLeh/GoFreeDB) - Golang 库在 Google Sheets 之上提供通用且简单的数据库抽象。
- [gogtrends](https://github.com/groovili/gogtrends) - 谷歌趋势非官方 API。
- [golang-tmdb](https://github.com/cyruzin/golang-tmdb) - 电影数据库 API v3 的 Golang 包装器。
- [golyrics](https://github.com/mamal72/golyrics) - Golyrics 是一个 Go 库，用于从 Wikia 网站获取音乐歌词数据。
- [gomalshare](https://github.com/MonaxGT/gomalshare) - Go 库 MalShare API [malshare.com](https://www.malshare.com/)
- [GoMusicBrainz](https://github.com/michiwend/gomusicbrainz) - 转到 MusicBrainz WS2 客户端库。
- [google](https://github.com/google/google-api-go-client) - 自动生成适用于 Go 的 Google API。
- [google-analytics](https://github.com/chonthu/go-google-analytics) - 简单的包装器，方便谷歌分析报告。
- [google-cloud](https://github.com/GoogleCloudPlatform/gcloud-golang) - Google Cloud API Go 客户端库。
- [gopaapi5](https://github.com/utekaravinash/gopaapi5) - [Amazon Product Advertising API 5.0](https://webservices.amazon.com/paapi5/documentation/) 的 Go 客户端库。
- [gopensky](https://github.com/navidys/gopensky) - [OpenSKY Network](https://opensky-network.org/) live API 的 Go 客户端实现（空域 ADS-B 和 S 模式数据）。
- [gosip](https://github.com/koltyakov/gosip) - SharePoint 的客户端库。
- [gostorm](https://github.com/jsgilmore/gostorm) - GoStorm 是一个 Go 库，它实现了在 Go 中编写与 Storm shell 通信的 Storm spout 和 Bolt 所需的通信协议。
- [hipchat](https://github.com/andybons/hipchat) - 该项目为 Hipchat API 实现了一个 golang 客户端库。
- [hipchat (xmpp)](https://github.com/daneharrigan/hipchat) - 通过 XMPP 与 HipChat 通信的 golang 包。
- [igdb](https://github.com/Henry-Sarabia/igdb) - [Internet Game Database API](https://api.igdb.com/) 的 Go 客户端。
- [ip2location-io-go](https://github.com/ip2location/ip2location-io-go) - IP2Location.io API 的 Go 包装器 [IP2Location.io](https://www.ip2location.io/)。
- [jokeapi-go](https://github.com/icelain/jokeapi) - Go 客户端 [JokeAPI](https://sv443.net/jokeapi/v2/)。
- [lark](https://github.com/chyroc/lark) - [飞书](https://open.feishu.cn/)/[Lark](https://open.larksuite.com/) 开放API Go SDK，支持所有开放API和事件回调。
- [lastpass-go](https://github.com/ansd/lastpass-go) - 转到 [LastPass](https://www.lastpass.com/) API 的客户端库。
- [libgoffi](https://github.com/clevabit/libgoffi) - 用于本机 [libffi](https://sourceware.org/libffi/) 集成的库适配器工具箱
- [libopenapi](https://github.com/pb33f/libopenapi) - 解析、验证和使用 OpenAPI、Swagger、Overlays 和 Arazzo 规范。
- [Medium](https://github.com/Medium/medium-sdk-go) - 适用于 Medium 的 OAuth2 API 的 Golang SDK。
- [megos](https://github.com/andygrunwald/megos) - 用于访问 [Apache Mesos](https://mesos.apache.org/) 集群的客户端库。
- [minio-go](https://github.com/minio/minio-go) - 用于 Amazon S3 兼容云存储的 Minio Go 库。
- [mixpanel](https://github.com/dukex/mixpanel) - Mixpanel 是一个库，用于跟踪事件并将 Mixpanel 配置文件更新从您的 go 应用程序发送到 Mixpanel。
- [newsapi-go](https://github.com/jellydator/newsapi-go) - 转到 [NewsAPI](https://newsapi.org/) 客户端。
- [openaigo](https://github.com/otiai10/openaigo) - 适用于 Go 的 OpenAI GPT3/GPT3.5 ChatGPT API 客户端库。
- [patreon-go](https://github.com/mxpv/patreon-go) - Patreon API 的 Go 库。
- [paypal](https://github.com/logpacker/PayPal-Go-SDK) - PayPal 支付 API 的包装。
- [playlyfe](https://github.com/playlyfe/playlyfe-go-sdk) - Playlyfe Rest API Go SDK。
- [pushover](https://github.com/gregdel/pushover) - Go 包装器用于 Pushover API。
- [rawg-sdk-go](https://github.com/dimuska139/rawg-sdk-go) - [RAWG 视频游戏数据库](https://rawg.io/) API 的 Go 库
- [shopify](https://github.com/rapito/go-shopify) - 转到 Library 向 Shopify API 发出 CRUD 请求。
- [simples3](https://github.com/rhnvrm/simples3) - 简单朴素的 AWS S3 库，使用 REST 和用 Go 编写的 V4 签名。
- [slack](https://github.com/slack-go/slack) - Go 中的 Slack API。
- [smite](https://github.com/sergiotapia/smitego) - Go 包用于包装对 Smite 游戏 API 的访问。
- [spec](https://github.com/oaswrap/spec) - 轻量级 OpenAPI 3.x 构建器，支持静态生成和流行框架，如 chi、echo、gin、fibre、mux 等。
- [spotify](https://github.com/rapito/go-spotify) - 前往 Library 访问 Spotify WEB API。
- [steam](https://github.com/sostronk/go-steam) - Go Library 与 Steam 游戏服务器交互。
- [stripe](https://github.com/stripe/stripe-go) - Stripe API 的 Go 客户端。
- [swag](https://github.com/zc2638/swag) - 没有注释，简单的 go 包装器来创建 swagger 2.0 兼容的 API。支持大多数路由框架，如built-in、gin、chi、mux、echo、httprouter、fasthttp等。
- [textbelt](https://github.com/dietsche/textbelt) - textbelt.com txt 消息 API 的 Go 客户端。
- [threads-go](https://github.com/tirthpatell/threads-go) - 具有 OAuth 2.0、速率限制和类型安全错误处理功能的 Meta Threads API 的 Go 客户端库。
- [Trello](https://github.com/adlio/trello) - Trello API 的 Go 包装器。
- [TripAdvisor](https://github.com/mrbenosborne/tripadvisor-golang) - TripAdvisor API 的 Go 包装器。
- [tumblr](https://github.com/mattcunningham/gumblr) - Tumblr v2 API 的 Go 包装器。
- [uptimerobot](https://github.com/bitfield/uptimerobot) - Uptime Robot v2 API 的 Go 包装器和命令行客户端。
- [vl-go](https://github.com/verifid/vl-go) - 围绕 VerifID 身份验证层 API 的客户端库。
- [webhooks](https://github.com/go-playground/webhooks) - GitHub 和 Bitbucket 的 Webhook 接收器。
- [wit-go](https://github.com/wit-ai/wit-go) - wit.ai HTTP API 的 Go 客户端。
- [ynab](https://github.com/brunomvsouza/ynab.go) - YNAB API 的 Go 包装器。
- [zooz](https://github.com/gojuno/go-zooz) - Zooz API 的 Go 客户端。

**[⬆ 回到顶部](#contents)**

## 公用事业

_让您的生活更轻松的通用实用程序和工具。_

- [abstract](https://github.com/maxbolgarin/abstract) - 用于消除业务逻辑中的样板代码的抽象和实用程序。
- [apm](https://github.com/topfreegames/apm) - 具有 HTTP API 的 Golang 应用程序的进程管理器。
- [backscanner](https://github.com/icza/backscanner) - 与 bufio.Scanner 类似的扫描器，但它以相反的顺序读取和返回行，从给定位置开始向后移动。
- [bed](https://github.com/itchyny/bed) - 用 Go 编写的类似 Vim 的二进制编辑器。
- [blank](https://github.com/Henry-Sarabia/blank) - 验证或删除字符串中的空格和空格。
- [bleep](https://github.com/sinhashubham95/bleep) - 对 Go 中的任意一组操作系统信号执行任意数量的操作。
- [boilr](https://github.com/tmrts/boilr) - 用于从样板模板创建项目的极快 CLI 工具。
- [boring](https://github.com/alebeck/boring) - 简单的命令行 SSH 隧道管理器。
- [changie](https://github.com/miniscruff/changie) - 自动化变更日志工具，用于准备具有大量自定义选项的版本。
- [chyle](https://github.com/antham/chyle) - 使用具有多种配置可能性的 git 存储库的变更日志生成器。
- [circuit](https://github.com/cep21/circuit) - 断路器模式的高效且功能完整的 Hystrix，类似于 Go 实现。
- [circuitbreaker](https://github.com/rubyist/circuitbreaker) - Go 中的断路器。
- [clipboard](https://github.com/golang-design/clipboard) - 📋 Go 中的跨平台剪贴板包。
- [clockwork](https://github.com/jonboulle/clockwork) - 一个简单的 golang 假时钟。
- [cmd](https://github.com/SimonBaeumer/cmd) - 用于在 osx、windows 和 linux 上执行 shell 命令的库。
- [config-file-validator](https://github.com/Boeing/config-file-validator) - 用于验证配置文件的跨平台工具。
- [contem](https://github.com/maxbolgarin/contem) - 直接上下文。上下文替换用于正常关闭 Go 应用程序。
- [cookie](https://github.com/syntaqx/cookie) - Cookie 结构解析和帮助程序包。
- [copy-pasta](https://github.com/jutkko/copy-pasta) - 通用多工作站剪贴板，使用类似 S3 的后端进行存储。
- [countries](https://github.com/biter777/countries) - 全面实施 ISO-3166-1、ISO-4217、ITU-T E.164、Unicode CLDR 和 IANA ccTLD 标准。
- [countries](https://github.com/pioz/countries) - 当您与 Go 国家/地区合作时所需的一切。
- [create-go-app](https://github.com/create-go-app/cli) - 一个强大的 CLI，用于通过运行一个命令来创建具有后端（Golang）、前端（JavaScript、TypeScript）和部署自动化（Ansible、Docker）的新的生产就绪项目。
- [cryptgo](https://github.com/Gituser143/cryptgo) - Crytpgo 是一款纯粹用 Go 编写的基于 TUI 的应用程序，用于实时监控和观察加密货币价格！
- [ctop](https://github.com/bcicen/ctop) - 用于容器指标的 [Top-like](https://ctop.sh) 接口（例如 htop）。
- [ctxutil](https://github.com/posener/ctxutil) - 上下文实用函数的集合。
- [cvt](https://github.com/shockerli/cvt) - 轻松安全地将任何值转换为另一种类型。
- [dbt](https://github.com/nikogura/dbt) - 一个用于从中央可信存储库运行自我更新签名二进制文件的框架。
- [Death](https://github.com/vrecan/death) - 使用信号管理 go 应用程序关闭。
- [debounce](https://github.com/floatdrop/debounce) - 用 Go 编写的零分配去抖动器。
- [delve](https://github.com/derekparker/delve) - 去调试器。
- [dive](https://github.com/wagoodman/dive) - 用于探索 Docker 镜像中每一层的工具。
- [dlog](https://github.com/kirillDanshin/dlog) - 编译时控制的记录器可以使您的版本更小，而无需删除调试调用。
- [EaseProbe](https://github.com/megaease/easeprobe) - 一个简单、独立、轻量级的工具，可以执行运行状况/状态检查守护进程，支持 HTTP/TCP/SSH/Shell/Client/... 探针，以及 Slack/Discord/Telegram/SMS... 通知。
- [equalizer](https://github.com/reugn/equalizer) - Go 的配额管理器和速率限制器集合。
- [ergo](https://github.com/cristianoliveira/ergo) - 管理在不同端口上运行的多个本地服务变得容易。
- [evaluator](https://github.com/nullne/evaluator) - 基于 s-表达式动态评估表达式。它简单且易于扩展。
- [Failsafe-go](https://github.com/failsafe-go/failsafe-go) - Go 的容错和弹性模式。
- [filetype](https://github.com/h2non/filetype) - 用于检查幻数签名来推断文件类型的小包。
- [filler](https://github.com/yaronsumel/filler) - 使用“fill”标签填充结构的小实用程序。
- [filter](https://github.com/gookit/filter) - 提供 Go 数据的过滤、清理和转换。
- [fzf](https://github.com/junegunn/fzf) - 用 Go 编写的命令行模糊查找器。
- [generate](https://github.com/go-playground/generate) - 在指定的路径或环境变量上递归运行 gogenerate，并且可以通过正则表达式进行过滤。
- [ghokin](https://github.com/antham/ghokin) - 并行格式化程序，没有小黄瓜的外部依赖性（黄瓜，behat...）。
- [git-time-metric](https://github.com/git-time-metric/gtm) - Git 的简单、无缝、轻量级时间跟踪。
- [git-tools](https://github.com/kazhuravlev/git-tools) - 帮助管理 git 标签的工具。
- [gitbatch](https://github.com/isacikgoz/gitbatch) - 在一处管理您的 git 存储库。
- [gitcs](https://github.com/knbr13/gitcs/) - Git Commits Visualizer，CLI 工具，用于可视化本地计算机上的 Git 提交。
- [go-actuator](https://github.com/sinhashubham95/go-actuator) - 基于 Go 的 Web 框架的生产就绪功能。
- [go-astitodo](https://github.com/asticode/go-astitodo) - 解析 GO 代码中的 TODO。
- [go-bind-plugin](https://github.com/wendigo/go-bind-plugin) - go：生成工具，用于包装 golang 插件导出的符号（仅限 1.8）。
- [go-bsdiff](https://github.com/gabstv/go-bsdiff) - Pure Go bsdiff 和 bspatch 库以及 CLI 工具。
- [go-clip](https://github.com/prashantgupta24/go-clip) - 适用于 Mac 的简约剪贴板管理器。
- [Go-Constant](https://github.com/sajjadrabiee/go-constant) - 通用类型常量集，具有针对 Go 缺失的枚举类型的安全字符串解析。
- [go-convert](https://github.com/Eun/go-convert) - go-convert 包使您能够将值转换为另一种类型。
- [go-countries](https://github.com/mikekonan/go-countries) - ISO-3166 代码的轻量级查找。
- [go-dry](https://github.com/ungerik/go-dry) - Go 的 DRY（不要重复）包。
- [go-events](https://github.com/deatil/go-events) - 一个 go event 和 event'subscribe 包，类似 wordpress 的钩子函数。
- [go-funk](https://github.com/thoas/go-funk) - 现代 Go 实用程序库提供帮助程序（映射、查找、包含、过滤、块、反向等）。
- [go-health](https://github.com/Talento90/go-health) - 健康包简化了您向服务添加健康检查的方式。
- [go-httpheader](https://github.com/mozillazg/go-httpheader) - 用于将结构编码到标头字段中的 Go 库。
- [go-lambda-cleanup](https://github.com/karl-cardenas-coding/go-lambda-cleanup) - 用于删除未使用或以前版本的 AWS Lambdas 的 CLI。
- [go-lock](https://github.com/viney-shih/go-lock) - go-lock是一个实现读写互斥锁和读写trylock而无需饥饿的锁库。
- [go-pattern-match](https://github.com/PhakornKiong/go-pattern-match) - 受 ts-pattern 启发的模式匹配库。
- [go-pkg](https://github.com/chenquan/go-pkg) - 一个 go 工具包。
- [go-problemdetails](https://github.com/mvmaasakkers/go-problemdetails) - 用于处理问题详细信息的软件包。
- [go-qr](https://github.com/piglig/go-qr) - 原生、高品质、简约的二维码生成器。
- [go-rate](https://github.com/beefsack/go-rate) - Go 的定时速率限制器。
- [go-safecast](https://github.com/ccoVeille/go-safecast) - 防止整数上溢和下溢的安全数字类型转换库（地址 gosec G115 和 CWE-190）。
- [go-sitemap-generator](https://github.com/ikeikeikeike/go-sitemap-generator) - 用 Go 编写的 XML 站点地图生成器。
- [go-snk](https://github.com/SharkByteSoftware/go-snk) - 用于切片、映射、字符串、错误、JSON、HTTP 和容器的类型安全通用帮助程序，组织为小型独立可采用的包。
- [go-trigger](https://github.com/sadlil/go-trigger) - Go-lang 全局事件触发器，使用 id 注册事件并从项目的任何位置触发事件。
- [go-tripper](https://github.com/rajnandan1/go-tripper) - Tripper 是 Go 的断路器包，可让您连接电路并控制电路的状态。
- [go-type](https://github.com/mikekonan/go-types) - 提供 Go 类型的库，用于存储/验证和传输 ISO-4217、ISO-3166 和其他类型。
- [goback](https://github.com/carlescere/goback) - 采用简单的指数退避包。
- [goctx](https://github.com/zerosnake0/goctx) - 通过高性能获得您的上下文价值。
- [godaemon](https://github.com/VividCortex/godaemon) - 编写守护进程的实用程序。
- [godoclive](https://github.com/syst3mctl/godoclive) - 使用 chi、gin 和 net/http 路由器的静态分析从 Go HTTP 处理程序生成交互式 API 文档。
- [godropbox](https://github.com/dropbox/godropbox) - 用于从 Dropbox 编写 Go 服务/应用程序的通用库。
- [gofn](https://github.com/tiendc/gofn) - 使用 Go 1.18+ 的泛型编写的高性能实用函数。
- [golarm](https://github.com/msempere/golarm) - 带有系统事件的火灾警报。
- [golog](https://github.com/mlimaloureiro/golog) - 简单且轻量级的 CLI 工具可用于时间跟踪您的任务。
- [gopencils](https://github.com/bndr/gopencils) - 小而简单的包可轻松使用 REST API。
- [goplaceholder](https://github.com/michiwend/goplaceholder) - 一个用于生成占位符图像的小型 golang 库。
- [goreadability](https://github.com/philipjkim/goreadability) - 使用 Facebook Open Graph 和 arc90 的可读性的网页摘要提取器。
- [goreleaser](https://github.com/goreleaser/goreleaser) - 尽可能快速、轻松地交付 Go 二进制文件。
- [goreporter](https://github.com/wgliang/goreporter) - Golang 工具，进行静态分析、单元测试、代码审查并生成代码质量报告。
- [goseaweedfs](https://github.com/linxGnu/goseaweedfs) - SeaweedFS 客户端库具有几乎完整的功能。
- [gostrutils](https://github.com/ik5/gostrutils) - 字符串操作和转换函数的集合。
- [gotenv](https://github.com/subosito/gotenv) - 从 Go 中的 `.env` 或任何 `io.Reader` 加载环境变量。
- [goval](https://github.com/maja42/goval) - 评估 Go 中的任意表达式。
- [graterm](https://github.com/skovtunenko/graterm) - 提供原语以在 Go 应用程序中执行有序（顺序/并发）优雅终止（也称为关闭）。
- [grofer](https://github.com/pesos/grofer) - 用Golang编写的系统和资源监控工具！
- [gubrak](https://github.com/novalagung/gubrak) - 带有语法糖的 Golang 实用程序库。它就像 lodash，但针对 golang。
- [handy](https://github.com/miguelpragier/handy) - 许多实用程序和帮助程序，例如字符串处理程序/格式化程序和验证程序。
- [healthcheck](https://github.com/kazhuravlev/healthcheck) - 一个简单而强大的 Kubernetes 就绪测试。
- [hostctl](https://github.com/guumaster/hostctl) - 一个 CLI 工具，可以使用简单的命令来管理 /etc/hosts。
- [htcat](https://github.com/htcat/htcat) - 并行和流水线 HTTP GET 实用程序。
- [hub](https://github.com/github/hub) - 将 git 命令与附加功能包装在一起，以便从终端与 github 进行交互。
- [immortal](https://github.com/immortal/immortal) - \*nix 跨平台（与操作系统无关）管理程序。
- [jet](https://github.com/NicoNex/jet) - Just Edit Text：一个快速而强大的工具，用于使用正则表达式查找和替换文件内容和名称。
- [jsend](https://github.com/clevergo/jsend) - JSend 的实现是用 Go 编写的。
- [json-log-viewer](https://github.com/hedhyw/json-log-viewer) - JSON 日志的交互式查看器。
- [jump](https://github.com/gsamokovarov/jump) - Jump 通过了解您的习惯来帮助您更快地导航。
- [just](https://github.com/kazhuravlev/just) - 只是用于处理通用数据结构的有用函数的集合。
- [koazee](https://github.com/wesovilabs/koazee) - 库受到惰性求值和函数式编程的启发，消除了使用数组的麻烦。
- [lang](https://github.com/maxbolgarin/lang) - 无需样板代码即可使用变量、切片和映射的通用单行代码。
- [lets-go](https://github.com/aplescia-chwy/lets-go) - Go 模块为云原生 REST API 开发提供常用实用程序。还包含 AWS 特定实用程序。
- [limiters](https://github.com/mennanov/limiters) - Golang 中分布式应用程序的速率限制器，具有可配置的后端和分布式锁。
- [lo](https://github.com/samber/lo) - 类似 Lodash 的 Go 库，基于 Go 1.18+ 泛型（映射、过滤器、包含、查找...）
- [loncha](https://github.com/kazu/loncha) - 高性能切片实用程序。
- [lrserver](https://github.com/jaschaephraim/lrserver) - Go 的 LiveReload 服务器。
- [mani](https://github.com/alajmo/mani) - CLI 工具可帮助您管理多个存储库。
- [mc](https://github.com/minio/mc) - Minio Client 提供了与 Amazon S3 兼容的云存储和文件系统配合使用的最少工具。
- [mergo](https://github.com/imdario/mergo) - 在 Golang 中合并结构和映射的帮助器。对于配置默认值很有用，避免混乱的 if 语句。
- [mimemagic](https://github.com/zRedShift/mimemagic) - Pure Go 超高性能 MIME 嗅探库/实用程序。
- [mimetype](https://github.com/gabriel-vasile/mimetype) - 基于幻数的 MIME 类型检测包。
- [minify](https://github.com/tdewolff/minify) - HTML、CSS、JS、XML、JSON 和 SVG 文件格式的快速压缩器。
- [minquery](https://github.com/icza/minquery) - 支持高效分页的 MongoDB / mgo.v2 查询（光标继续列出我们上次停下来的文档）。
- [moldova](https://github.com/StabbyCutyou/moldova) - 用于根据输入模板生成随机数据的实用程序。
- [mole](https://github.com/davrodpin/mole) - cli 应用程序可轻松创建 ssh 隧道。
- [mongo-go-pagination](https://github.com/gobeam/mongo-go-pagination) - 官方 mongodb/mongo-go-driver 包的 Mongodb 分页，支持普通查询和聚合管道。
- [mssqlx](https://github.com/linxGnu/mssqlx) - 数据库客户端库，任何主从的代理，主主结构。考虑到轻量化和自动平衡。
- [multitick](https://github.com/VividCortex/multitick) - 用于对齐代码的多路复用器。
- [netbug](https://github.com/e-dard/netbug) - 轻松远程分析您的服务。
- [nfdump](https://github.com/chrispassas/nfdump) - 读取 nfdump 网络流文件。
- [nostromo](https://github.com/pokanop/nostromo) - 用于构建强大别名的 CLI。
- [okrun](https://github.com/xta/okrun) - 去运行错误压路机。
- [olaf](https://github.com/btnguyen2k/olaf) - Twitter Snowflake 在 Go 中实现。
- [onecache](https://github.com/adelowo/onecache) - 支持多个后端存储（Redis、Memcached、文件系统等）的缓存库。
- [optional](https://github.com/kazhuravlev/optional) - 可选的结构字段和变量。
- [panicparse](https://github.com/maruel/panicparse) - 对相似的 goroutine 进行分组并对堆栈转储进行着色。
- [pattern-match](https://github.com/alexpantyukhin/go-pattern-match) - 模式匹配库。
- [peco](https://github.com/peco/peco) - 简单的交互式过滤工具。
- [pgo](https://github.com/arthurkushman/pgo) - PHP社区的便捷功能。
- [pm](https://github.com/VividCortex/pm) - 具有 HTTP API 的进程（即 goroutine）管理器。
- [pointer](https://github.com/xorcare/pointer) - 包指针包含用于简化基本类型可选字段的创建的帮助例程。
- [ptr](https://github.com/gotidy/ptr) - 提供用于简化从基本类型常量创建指针的函数的包。
- [rate](https://github.com/webriots/rate) - 具有令牌桶和 AIMD 策略的高性能限速库。
- [rclient](https://github.com/zpatrick/rclient) - 可读、灵活、易于使用的 REST API 客户端。
- [release](https://github.com/tomodian/release) - 用于 Keep-a-changelog 格式的变更日志的 CLI。
- [relimpact](https://github.com/hashmap-kz/relimpact) - Go 项目的快速 API 兼容性报告。
- [remote-touchpad](https://github.com/Unrud/remote-touchpad) - 从智能手机控制鼠标和键盘。
- [repeat](https://github.com/ssgreg/repeat) - 实施不同的退避策略对于重试操作和心跳很有用。
- [request](https://github.com/mozillazg/request) - Go HTTP 请求为人类™。
- [rerun](https://github.com/ivpusic/rerun) - 当源更改时重新编译并重新运行 go 应用程序。
- [rest-go](https://github.com/edermanoel94/rest-go) - 该包提供了许多使用 Rest api 的有用方法。
- [retro](https://github.com/goioc/retro) - 方便的错误重试库，具有广泛的灵活性（退避策略、上限等）。
- [retry](https://github.com/kamilsk/retry) - 最先进的功能机制可重复执行操作直至成功。
- [retry](https://github.com/percolate/retry) - 一个简单但高度可配置的 Go 重试包。
- [retry](https://github.com/thedevsaddam/retry) - 简单易用的 Go 重试机制包。
- [retry](https://github.com/shafreeck/retry) - 一个非常简单的库，可确保您的工作完成。
- [retry-go](https://github.com/avast/retry-go) - 用于重试机制的简单库。
- [retry-go](https://github.com/rafaeljesus/retry-go) - 对于 golang 来说，重试变得简单又容易。
- [robustly](https://github.com/VividCortex/robustly) - 弹性运行函数，捕获并重新启动恐慌。
- [rospo](https://github.com/ferama/rospo) - 简单可靠的 ssh 隧道，带有 Golang 中的嵌入式 ssh 服务器。
- [scan](https://github.com/blockloop/scan) - 直接扫描 golang `sql.Rows` 到结构体、切片或原始类型。
- [scan](https://github.com/wroge/scan) - 将 sql 行扫描为由泛型支持的任何类型。
- [scany](https://github.com/georgysavva/scany) - 用于将数据库中的数据扫描为 Go 结构等的库。
- [serve](https://github.com/syntaqx/serve) - 任何您需要的地方都有一个静态 http 服务器。
- [sesh](https://github.com/joshmedeski/sesh) - Sesh 是一个 CLI，可帮助您使用 zox 快速轻松地创建和管理 tmux 会话。
- [set](https://github.com/nofeaturesonlybugs/set) - 高性能且灵活的结构映射和松散类型转换。
- [shutdown](https://github.com/ztrue/shutdown) - 用于“os.Signal”处理的应用程序关闭挂钩。
- [silk](https://github.com/chrispassas/silk) - 读取 Silk Netflow 文件。
- [slice](https://github.com/psampaz/slice) - 用于常见 Go 切片操作的类型安全函数。
- [sliceconv](https://github.com/Henry-Sarabia/sliceconv) - 原始类型之间的切片转换。
- [slicer](https://github.com/leaanthony/slicer) - 使切片的使用变得更加容易。
- [sorty](https://github.com/jfcg/sorty) - 快速并发/并行排序。
- [sqlx](https://github.com/jmoiron/sqlx) - 在优秀的内置数据库/sql 包之上提供了一组扩展。
- [sqlz](https://github.com/rfberaldo/sqlz) - 数据库/sql 包的扩展，添加命名查询、结构扫描和批处理操作。
- [sshman](https://github.com/shoobyban/sshman) - 多个远程服务器上的authorized_keys 文件的SSH 管理器。
- [stacktower](https://github.com/stacktower-io/stacktower) - 受 XKCD #2347 启发，将依赖图可视化为物理塔结构。
- [statiks](https://github.com/janiltonmaciel/statiks) - 快速、零配置、静态 HTTP 文件管理服务器。
- [Storm](https://github.com/asdine/storm) - 简单而强大的 BoltDB 工具包。
- [structs](https://github.com/PumpkinSeed/structs) - 实现简单的函数来操作结构。
- [throttle](https://github.com/yudppp/throttle) - Throttle 是一个在每个持续时间内仅执行一个操作的对象。
- [tik](https://github.com/andy2046/tik) - 简单易用的 Go 计时轮包。
- [tome](https://github.com/cyruzin/tome) - Tome 旨在对简单的 RESTful API 进行分页。
- [toolbox](https://github.com/viant/toolbox) - 切片、映射、多重映射、结构、函数、数据转换实用程序。服务路由器、宏评估器、分词器。
- [UNIS](https://github.com/esemplastic/unis) - Go 中字符串实用程序的 Common Architecture™。
- [upterm](https://github.com/owenthereal/upterm) - 开发人员可以通过网络安全地共享终端/tmux 会话的工具。它非常适合远程结对编程、访问 NAT/防火墙后面的计算机、远程调试等。
- [usql](https://github.com/knq/usql) - usql 是 SQL 数据库的通用命令行界面。
- [util](https://github.com/shomali11/util) - 有用的实用函数的集合。 （字符串、并发、操作……）。
- [watchhttp](https://github.com/nikolaydubina/watchhttp) - 定期运行命令并将最新的 STDOUT 或其丰富的增量公开为 HTTP 端点。
- [wifiqr](https://github.com/reugn/wifiqr) - Wi-Fi 二维码生成器。
- [wuzz](https://github.com/asciimoo/wuzz) - 用于 HTTP 检查的交互式 cli 工具。
- [xferspdy](https://github.com/monmohan/xferspdy) - Xferspdy 在 golang 中提供二进制 diff 和 patch 库。
- [xpool](https://github.com/peczenyj/xpool) - 另一个使用泛型的 golang 类型安全对象池。
- [yogo](https://github.com/antham/yogo) - 从命令行检查 yopmail 邮件。

**[⬆ 回到顶部](#contents)**

## 通用唯一标识符

_用于处理 UUID 的库._

- [fastuuid](https://github.com/rekby/fastuuid) - 快速生成 UUIDv4 作为字符串或字节。
- [goid](https://github.com/jakehl/goid) - 生成并解析符合 RFC4122 的 V4 UUID。
- [gouid](https://github.com/twharmon/gouid) - 只需一次分配即可生成加密安全的随机字符串 ID。
- [guid](https://github.com/sdrapkin/guid) - 用于 Go 的快速加密安全 Guid 生成器（比“uuid”快约 10 倍）。
- [nanoid](https://github.com/aidarkhanov/nanoid) - 一个小型且高效的 Go 唯一字符串 ID 生成器。
- [sno](https://github.com/muyo/sno) - 具有嵌入式元数据的紧凑、可排序且快速的唯一 ID。
- [ulid](https://github.com/oklog/ulid) - Go 实现 ULID（通用唯一词典可排序标识符）。
- [uniq](https://gitlab.com/skilstak/code/go/uniq) - 使用命令轻松安全、快速的唯一标识符。
- [uuid](https://github.com/agext/uuid) - 使用快速或加密质量的随机节点标识符生成、编码和解码 UUID v1。
- [uuid](https://github.com/gofrs/uuid) - 通用唯一标识符（UUID）的实现。支持 UUID 的创建和解析。积极维护 satori uuid 的分支。
- [uuid](https://github.com/google/uuid) - 基于 RFC 4122 和 DCE 1.1 的 UUID Go 包：身份验证和安全服务。
- [uuidcheck](https://github.com/ashwingopalsamy/uuidcheck) - 一个小型、无依赖性的 Go 库，可根据标准 RFC 4122 格式验证 UUID，并将 UUIDv7() 转换为 UTC 时间戳。
- [wuid](https://github.com/edwingeng/wuid) - 极快的全球唯一号码生成器。
- [xid](https://github.com/rs/xid) - Xid 是一个全球唯一的 id 生成器库，可以直接在您的服务器代码中安全地使用。

**[⬆ 回到顶部](#contents)**

## 验证

_用于验证的库._

- [checkdigit](https://github.com/osamingo/checkdigit) - 提供校验位算法（Luhn、Verhoeff、Damm）和计算器（ISBN、EAN、JAN、UPC 等）。
- [go-validator](https://github.com/tiendc/go-validator) - 使用泛型的验证库。
- [gody](https://github.com/guiferpa/gody) - :balloon：Go 的轻量级结构验证器。
- [govalid](https://github.com/twharmon/govalid) - 对结构进行快速、基于标记的验证。
- [govalidator](https://github.com/asaskevich/govalidator) - 字符串、数字、切片和结构的验证器和清理器。
- [govalidator](https://github.com/thedevsaddam/govalidator) - 使用简单的规则验证 Golang 请求数据。深受 Laravel 请求验证的启发。
- [govy](https://github.com/nobl9/govy) - 基于功能接口的强类型验证规则，由泛型和无反射提供支持，重点关注制作清晰且信息丰富的错误消息。
- [hvalid](https://github.com/lyonnee/hvalid) hvalid是一个用Go语言编写的轻量级验证库。它提供了自定义的验证器接口和一系列常用的验证函数，帮助开发者快速实现数据验证。
- [jio](https://github.com/faceair/jio) - jio 是一个类似于 [joi](https://github.com/hapijs/joi) 的 json 模式验证器。
- [ozzo-validation](https://github.com/go-ozzo/ozzo-validation) - 支持使用常用代码构造中指定的可配置和可扩展的验证规则（而不是结构标记）对各种数据类型（结构、字符串、映射、切片等）进行验证。
- [validate](https://github.com/gookit/validate) - 用于数据验证和过滤的 Go 包。支持验证Map、Struct、Request(Form、JSON、url.Values、上传文件)数据和更多功能。
- [validate](https://github.com/gobuffalo/validate) - 该包提供了一个为 Go 应用程序编写验证的框架。
- [validator](https://github.com/go-playground/validator) - Go 结构和字段验证，包括跨字段、跨结构、地图、切片和数组潜水。
- [Validator](https://github.com/go-the-way/validator) - 用 Go 编写的轻量级模型验证器。包含 VF：Min、Max、MinLength、MaxLength、Length、Enum、Regex。
- [valix](https://github.com/marrow16/valix) 用于验证请求的 Go 包
- [Zog](https://github.com/Oudwins/zog) - 受 [Zod](https://github.com/colinhacks/zod) 启发的模式构建器，用于运行时值解析和验证。
**[⬆ 回到顶部](#contents)**

## 版本控制

_版本控制库._

- [cli](https://gitlab.com/gitlab-org/cli) - 一个开源 GitLab 命令行工具，将 GitLab 的炫酷功能带入您的命令行。
- [froggit-go](https://github.com/jfrog/froggit-go) - Froggit-Go 是一个 Go 库，允许对 VCS 提供程序执行操作。
- [ggc](https://github.com/bmf-san/ggc) - 具有传统命令行和交互式增量搜索 UI、工作流支持和可配置键绑定的 Git CLI 工具。
- [git-courer](https://github.com/Alejandro-M-P/git-courer) - 使用 Ollama 进行 Git 操作的本地 MCP 服务器来保存令牌并防止秘密泄漏。
- [git2go](https://github.com/libgit2/git2go) - Go 绑定 libgit2。
- [githooks](https://github.com/gabyx/githooks) - 每个存储库和共享 Git 挂钩，具有版本控制和自动更新功能。
- [gitty](https://github.com/Omibranch/gitty) - 单二进制 Git/GitHub CLI，用一个命令替换添加→提交→推送；人类可读的语法，没有外部依赖。
- [go-git](https://github.com/go-git/go-git) - 纯 Go 中高度可扩展的 Git 实现。
- [go-vcs](https://github.com/sourcegraph/go-vcs) - 在 Go 中操作和检查 VCS 存储库。
- [hercules](https://github.com/src-d/hercules) - 从 Git 存储库历史中获得高级见解。
- [hgo](https://github.com/beyang/hgo) - Hgo 是 Go 软件包的集合，提供对本地 Mercurial 存储库的读取访问。

**[⬆ 回到顶部](#contents)**

## 视频

_用于操作视频的库._

- [gmf](https://github.com/3d0c/gmf) - FFmpeg av\* 库的 Go 绑定。
- [go-astiav](https://github.com/asticode/go-astiav) - GO 中 ffmpeg 的更好 C 绑定。
- [go-astisub](https://github.com/asticode/go-astisub) - 操作 GO 中的字幕（.srt、.stl、.ttml、.webvtt、.ssa/.ass、图文电视、.smi 等）。
- [go-astits](https://github.com/asticode/go-astits) - 在 GO 中本地解析和解复用 MPEG 传输流 (.ts)。
- [go-mpd](https://github.com/unki2aut/go-mpd) - MPEG-DASH 清单文件的解析器和生成器库。
- [goav](https://github.com/giorgisio/goav) - FFmpeg 的全面 Go 绑定。
- [gortsplib](https://github.com/aler9/gortsplib) - Pure Go RTSP 服务器和客户端库。
- [hls-m3u8](https://github.com/Eyevinn/hls-m3u8) - HLS (M3U8) 播放列表的解析器和生成器；与规范保持同步。
- [manifestor](https://github.com/alanzng/manifestor) - 用于解析、过滤、转换和构建 HLS 和 DASH 清单的零依赖库。
- [libvlc-go](https://github.com/adrg/libvlc-go) - libvlc 2.X/3.X/4.X 的 Go 绑定（由 VLC 媒体播放器使用）。
- [mp4ff](https://github.com/Eyevinn/mp4ff) - 用于处理包含视频、音频、字幕或元数据的 MP4 文件的库和工具。
- [v4l](https://github.com/korandiz/v4l) - Linux 视频捕捉库，用 Go 编写。

**[⬆ 回到顶部](#contents)**

## 网络框架

_全栈网络框架._

- [Atreugo](https://github.com/savsgio/atreugo) - 高性能和可扩展的微 Web 框架，热路径中的内存分配为零。
- [Barf](https://github.com/opensaucerer/barf) - 基本上，这是一个用于构建基于 JSON 的 Web API 的卓越框架。它完全不引人注目，也没有重新发明轮子。它的设计使得入门既简单又快速，同时又足够灵活，可以应对更复杂的用例。
- [Beego](https://github.com/beego/beego) - beego 是一个用于 Go 编程语言的开源、高性能 Web 框架。
- [Confetti Framework](https://confetti-framework.github.io/docs/) - Confetti 是一个 Go Web 应用程序框架，具有富有表现力、优雅的语法。 Confetti 结合了 Laravel 的优雅和 Go 的简单性。
- [Don](https://github.com/abemedia/go-don) - 一个高性能且易于使用的 API 框架。
- [doors](https://github.com/doors-dev/doors) - 服务器驱动的框架，用于完全用 Go 构建有状态、反应式 Web 应用程序。
- [Echo](https://github.com/labstack/echo) - 高性能、简约的 Go Web 框架。
- [Fastschema](https://github.com/fastschema/fastschema) - 灵活的 Go Web 框架和 Headless CMS。
- [Fiber](https://github.com/gofiber/fiber) - 一个受 Express.js 启发的 Web 框架，基于 Fasthttp 构建。
- [Flamingo](https://github.com/i-love-flamingo/flamingo) - 可插入 Web 项目的框架。包括模块概念并提供 DI、Configareas、i18n、模板引擎、graphql、可观察性、安全性、事件、路由和反向路由等功能。
- [Flamingo Commerce](https://github.com/i-love-flamingo/flamingo-commerce) - 使用干净的架构（例如 DDD 以及端口和适配器）提供电子商务功能，您可以使用它们来构建灵活的电子商务应用程序。
- [Fuego](https://github.com/go-fuego/fuego) - 适合忙碌的 Go 开发人员的框架！从源代码生成 OpenAPI 3 规范的 Web 框架。
- [Gin](https://github.com/gin-gonic/gin) - Gin 是一个用 Go 编写的 Web 框架！它具有类似马提尼的 API，性能更好，速度提高了 40 倍。如果您需要性能和良好的生产力。
- [Ginrpc](https://github.com/xxjwxc/ginrpc) - gin参数自动绑定工具，gin rpc工具。
- [go-api-boot](https://github.com/SaiNageswarS/go-api-boot) - 一个 gRpc 优先的微服务框架。功能包括对 Mongo 的 ODM 支持、云资源支持（AWS/Azure/Google）以及为 gRpc 定制的流畅依赖注入。此外，直接支持 grpc-web，使浏览器无需代理即可访问所有 gRpc API。
- [Goa](https://github.com/goadesign/goa) - Goa 提供了一种在 Go 中开发远程 API 和微服务的整体方法。
- [GoFr](https://github.com/gofr-dev/gofr) - Gofr 是一个固执己见的微服务开发框架。
- [GoFrame](https://github.com/gogf/gf) - GoFrame是Golang的模块化、功能强大、高性能的企业级应用程序开发框架。
- [golamb](https://github.com/twharmon/golamb) - Golamb 使编写与 AWS Lambda 和 API Gateway 一起使用的 API 端点变得更加容易。
- [Gone](https://github.com/gone-io/gone) - 受 Spring 启发的轻量级依赖注入和 Web 框架。
- [goravel](https://github.com/goravel/goravel) - 受 Laravel 启发的 Web 框架，具有 ORM、身份验证、队列、任务调度和更多内置功能。
- [Goyave](https://github.com/go-goyave/goyave) - 功能齐全的 REST API 框架，旨在干净的代码和快速开发，具有强大的内置功能。
- [Hertz](https://github.com/cloudwego/hertz) - 一个高性能、强扩展性的Go HTTP框架，帮助开发者构建微服务。
- [hiboot](https://github.com/hidevopsio/hiboot) - hiboot 是一个高性能 Web 应用程序框架，具有自动配置和依赖注入支持。
- [Huma](https://github.com/danielgtaylor/huma/) - 现代 REST/GraphQL API 框架，具有内置 OpenAPI 3、生成的文档和 CLI。
- [httpsuite](https://github.com/rluders/httpsuite) - Go 的 HTTP 请求解析和 RFC 9457 问题响应，具有仅 stdlib 核心和可选验证。
- [iWF](https://github.com/indeedeng/iwf) - iWF 是一个用于开发长期运行的业务流程的一体化平台。它为利用数据库、ElasticSearch、消息队列、持久计时器等提供了方便的抽象，并具有干净、简单且用户友好的界面。
- [Lit](https://github.com/jvcoutinho/lit) - 适用于 Golang 的高性能声明式 Web 框架，旨在实现简单性和生活质量。
- [Microservice](https://github.com/claygod/microservice) - 用于创建微服务的框架，用 Golang 编写。
- [patron](https://github.com/beatlabs/patron) - Patron 是一个微服务框架，遵循最佳云实践，重点关注生产力。
- [Pnutmux](https://gitlab.com/fruitygo/pnutmux) - Pnutmux 是一个强大的 Go Web 框架，它使用正则表达式来匹配和处理 HTTP 请求。它提供了 CORS 处理、结构化日志记录、URL 参数提取、中间件和并发限制等功能。
- [Revel](https://github.com/revel/revel) - Go 语言的高生产力 Web 框架。
- [rk-boot](https://github.com/rookie-ninja/rk-boot) - 一个引导程序库，用于使用 Gin 和 gRPC 快速轻松地构建企业 go 微服务。
- [Ronykit](https://github.com/clubpay/ronykit) - 具有可插拔架构且性能非常出色的 Web 框架。
- [rux](https://github.com/gookit/rux) - 用于构建 golang HTTP 应用程序的简单快速的 Web 框架。
- [templui](https://github.com/axzilla/templui) - Go 和 Temple 的现代 UI 组件。
- [uAdmin](https://github.com/uadmin/uadmin) - 功能齐全的 Golang Web 框架，灵感来自 Django。
- [WebGo](https://github.com/naughtygopher/webgo) - 一个微框架，用于构建具有处理程序链接、中间件和上下文注入的 Web 应用程序。使用符合标准库的 HTTP 处理程序（即“http.HandlerFunc”）。
- [Xun](https://github.com/yaitoo/xun) - 基于 Go 内置 html/template 和 net/http 包的路由器构建的 Web 框架。它被设计为轻量级、快速且易于使用，同时提供简单直观的 API，用于构建具有中间件、路由和模板渲染等高级功能的 Web 应用程序。
- [Yokai](https://github.com/ankorstore/yokai) - 用于后端应用程序的简单、模块化和可观察的 Go 框架。
- [NotNet](https://github.com/nottechdm/notnet) - 一个轻量级的 Go 框架，用于构建快速、符合人体工程学的 RESTful API，具有中间件和灵活的路由。

**[⬆ 回到顶部](#contents)**

### 中间件

#### 实际的中间件

- [client-timing](https://github.com/posener/client-timing) - Server-Timing 标头的 HTTP 客户端。
- [CORS](https://github.com/rs/cors) - 轻松将 CORS 功能添加到您的 API。
- [echo-middleware](https://github.com/faabiosr/echo-middleware) - 具有日志记录和指标的 Echo 框架中间件。
- [formjson](https://github.com/rs/formjson) - 将 JSON 输入作为标准表单 POST 透明地处理。
- [go-fault](https://github.com/github/go-fault) - Go 的故障注入中间件。
- [Limiter](https://github.com/ulule/limiter) - Go 的简单速率限制中间件。
- [ln-paywall](https://github.com/philippgille/ln-paywall) - Go 中间件，用于通过闪电网络（比特币）根据每个请求将 API 货币化。
- [mid](https://github.com/bobg/mid) - 其他 HTTP 中间件功能：从处理程序返回惯用的错误；接收/响应 JSON 数据；请求追踪；等等。
- [rk-gin](https://github.com/rookie-ninja/rk-gin) - Gin 框架的中间件，具有日志记录、指标、身份验证、跟踪等功能。
- [rk-grpc](https://github.com/rookie-ninja/rk-grpc) - 具有日志记录、指标、身份验证、跟踪等功能的 gRPC 中间件。
- [Tollbooth](https://github.com/didip/tollbooth) - 速率限制 HTTP 请求处理程序。
- [XFF](https://github.com/sebest/xff) - 处理“X-Forwarded-For”标头和朋友。

#### 用于创建 HTTP 中间件的库

- [alice](https://github.com/justinas/alice) - Go 的无痛中间件链接。
- [catena](https://github.com/codemodus/catena) - http.Handler 包装器串联（与“链”相同的 API）。
- [chain](https://github.com/codemodus/chain) - 处理程序包装器与范围数据链接（基于网络/上下文的“中间件”）。
- [gores](https://github.com/alioygur/gores) - Go 包处理 HTML、JSON、XML 等响应。对于 RESTful API 很有用。
- [interpose](https://github.com/carbocation/interpose) - golang 的极简 net/http 中间件。
- [mediary](https://github.com/HereMobilityDevelopers/mediary) - 将拦截器添加到“http.Client”以允许请求/响应的转储/整形/跟踪/...。
- [muxchain](https://github.com/stephens2424/muxchain) - net/http 的轻量级中间件。
- [negroni](https://github.com/urfave/negroni) - Golang 惯用的 HTTP 中间件。
- [render](https://github.com/unrolled/render) - Go 包可轻松呈现 JSON、XML 和 HTML 模板响应。
- [renderer](https://github.com/thedevsaddam/renderer) - 适用于 Go 的简单、轻量级且更快的响应（JSON、JSONP、XML、YAML、HTML、File）渲染包。
- [stats](https://github.com/thoas/stats) - Go 中间件存储有关您的 Web 应用程序的各种信息。

**[⬆ 回到顶部](#contents)**

### 路由器

- [alien](https://github.com/gernest/alien) - 来自外太空的轻量且快速的 http 路由器。
- [bellt](https://github.com/GuilhermeCaruso/bellt) - 一个简单的 Go HTTP 路由器。
- [Bone](https://github.com/go-zoo/bone) - 闪电般快速的 HTTP 多路复用器。
- [Bxog](https://github.com/claygod/Bxog) - 适用于 Go 的简单且快速的 HTTP 路由器。它适用于不同难度、长度和嵌套的路线。他知道如何根据收到的参数创建 URL。
- [chi](https://github.com/go-chi/chi) - 基于网络/上下文构建的小型、快速且富有表现力的 HTTP 路由器。
- [fasthttprouter](https://github.com/buaazp/fasthttprouter) - 高性能路由器从“httprouter”分叉。第一个路由器适合“fasthttp”。
- [FastRouter](https://github.com/razonyang/fastrouter) - 用 Go 编写的快速、灵活的 HTTP 路由器。
- [Fox](https://github.com/fox-toolkit/fox) - 用于构建反向代理和 API 网关的高性能 HTTP 路由器，为运行时改变路由提供一流的支持。
- [fursy](https://github.com/coregx/fursy) - HTTP 路由器，具有类型安全的通用处理程序、从代码自动生成 OpenAPI 3.1 以及 RFC 9457 错误响应。
- [goblin](https://github.com/bmf-san/goblin) - 基于 trie 树的 golang http 路由器。
- [gocraft/web](https://github.com/gocraft/web) - Go 中的 Mux 和中间件包。
- [Goji](https://github.com/goji/goji) - Goji 是一个简约且灵活的 HTTP 请求多路复用器，支持“net/context”。
- [GoLobby/Router](https://github.com/golobby/router) - GoLobby Router 是一个用于 Go 编程语言的轻量级但功能强大的 HTTP 路由器。
- [goroute](https://github.com/goroute/route) - 简单但功能强大的 HTTP 请求多路复用器。
- [GoRouter](https://github.com/vardius/gorouter) - GoRouter 是一个 Server/API 微框架、HTTP 请求路由器、多路复用器、mux，为请求路由器提供支持“net/context”的中间件。
- [gowww/router](https://github.com/gowww/router) - 闪电般快速的 HTTP 路由器与 net/http.Handler 接口完全兼容。
- [httprouter](https://github.com/julienschmidt/httprouter) - 高性能路由器。使用它和标准的 http 处理程序来形成一个非常高性能的 Web 框架。
- [httptreemux](https://github.com/dimfeld/httptreemux) - 适用于 Go 的高速、灵活的基于树的 HTTP 路由器。灵感来自httprouter。
- [lars](https://github.com/go-playground/lars) - 是一个轻量级、快速且可扩展的零分配 HTTP 路由器，用于创建可定制的框架。
- [mux](https://github.com/gorilla/mux) - 用于 golang 的强大 URL 路由器和调度程序。
- [nchi](https://github.com/muir/nchi) - 基于 httprouter 构建的类似 chi 的路由器，具有基于依赖注入的中间件包装器
- [ngamux](https://github.com/ngamux/ngamux) - Go 的简单 HTTP 路由器。
- [ozzo-routing](https://github.com/go-ozzo/ozzo-routing) - 一个极快的 Go (golang) HTTP 路由器，支持正则表达式路由匹配。完全支持构建 RESTful API。
- [pure](https://github.com/go-playground/pure) - 是一个轻量级 HTTP 路由器，坚持标准“net/http”实现。
- [Siesta](https://github.com/VividCortex/siesta) - 用于编写中间件和处理程序的可组合框架。
- [vestigo](https://github.com/husobee/vestigo) - 适用于 go Web 应用程序的高性能、独立、HTTP 兼容的 URL 路由器。
- [violetear](https://github.com/nbari/violetear) - 转到 HTTP 路由器。
- [xmux](https://github.com/rs/xmux) - 基于“httprouter”的高性能复用器，具有“net/context”支持。
- [xujiajun/gorouter](https://github.com/xujiajun/gorouter) - 一个简单快速的 Go HTTP 路由器。

**[⬆ 回到顶部](#contents)**

## 网络组装

- [dom](https://github.com/dennwc/dom) - DOM 库。
- [Extism Go SDK](https://github.com/extism/go-sdk) - 用于构建插件系统和多语言应用程序的通用跨语言 WebAssembly 框架。
- [go-canvas](https://github.com/markfarnan/go-canvas) - 使用 HTML5 Canvas 的库，所有绘图都在 go 代码中。
- [tinygo](https://github.com/tinygo-org/tinygo) - Go编译器适合小地方。微控制器、WebAssembly 和命令行工具。基于LLVM。
- [vert](https://github.com/norunners/vert) - Go 和 JS 值之间的互操作。
- [wasmbrowsertest](https://github.com/agnivade/wasmbrowsertest) - 在浏览器中运行 Go WASM 测试。
- [webapi](https://github.com/gowebapi/webapi) - 从 WebIDL 生成的 DOM 和 HTML 的绑定。

**[⬆ 回到顶部](#contents)**

## Webhooks 服务器

- [webhook](https://github.com/adnanh/webhook) - 允许用户创建在服务器上执行命令的 HTTP 端点（挂钩）的工具。
- [HookRun](https://github.com/bluvenr/hookrun) - 轻量级 Webhook 操作引擎（~3MB 单个二进制文件，零 deps），使用令牌/HMAC/IP 身份验证和热重载执行来自 YAML 规则的命令和脚本。
- [webhooked](https://github.com/42Atomys/webhooked) - 强大的 Webhook 接收器：处理、保护、格式化和存储 Webhook 负载从未如此简单。
- [WebhookX](https://github.com/webhookx-io/webhookx) - 用于消息接收、处理和可靠传递的 Webhooks 网关。

**[⬆ 回到顶部](#contents)**

## 窗户

- [d3d9](https://github.com/gonutz/d3d9) - Direct3D9 的 Go 绑定。
- [go-ole](https://github.com/go-ole/go-ole) - golang 的 Win32 OLE 实现。
- [gosddl](https://github.com/MonaxGT/gosddl) - 从 SDDL 字符串到用户友好的 JSON 的转换器。 SDDL由四部分组成：所有者、主要组、DACL、SACL。
- [windowsupdate](https://github.com/ceshihao/windowsupdate) - 使用 go-ole 的 Windows 更新代理 API 的 Golang 绑定。

**[⬆ 回到顶部](#contents)**

## 工作流程框架

_用于创建工作流程的库._

- [Cadence-client](https://github.com/uber-go/cadence-client) - 一个用于编写工作流程和活动的框架，运行在 Uber 制作的 Cadence 编排引擎之上。
- [Dagu](https://github.com/dagu-go/dagu) - 无代码工作流程执行器。它执行以简单 YAML 格式定义的 DAG。
- [Flowbaker](https://github.com/flowbaker/flowbaker) - 用于构建、连接和自动化无代码工作流程的自托管执行引擎。
- [go-dag](https://github.com/rhosocial/go-dag) - 用 Go 开发的框架，用于管理由有向无环图描述的工作流程的执行。
- [go-taskflow](https://github.com/noneback/go-taskflow) - 具有集成可视化器和分析器的类似任务流的通用任务并行编程框架。
- [workflow](https://github.com/luno/workflow) - 与技术堆栈无关的事件驱动工作流框架。

**[⬆ 回到顶部](#contents)**

## XML

_用于操作 XML 的库和工具._

- [XML-Comp](https://github.com/xml-comp/xml-comp) - 简单的命令行 XML 比较器，可生成文件夹、文件和标签的差异。
- [xml2map](https://github.com/sbabiv/xml2map) - XML 到 MAP 转换器用 Golang 编写。
- [xmlquery](https://github.com/antchfx/xmlquery) - xmlquery 是用于 XML 查询的 Golang XPath 包。
- [xmlwriter](https://github.com/shabbyrobe/xmlwriter) - 基于 libxml2 的 xmlwriter 模块的过程式 XML 生成 API。
- [xpath](https://github.com/antchfx/xpath) - Go 的 XPath 包。
- [zek](https://github.com/miku/zek) - 从 XML 生成 Go 结构体。

## 零信任

_实现零信任架构的库和工具。_

- [Cosign](https://github.com/sigstore/cosign) - OCI 注册表中的容器签名、验证和存储。
- [in-toto](https://github.com/in-toto/in-toto-golang) - in-toto（提供保护软件供应链完整性的框架）python 参考实现的 Go 实现。
- [OpenZiti](https://github.com/openziti/ziti) - 一个完整的开源零信任覆盖网络。包括适用于多种语言的众多 SDK，例如 [golang](https://github.com/openziti/sdk-golang)，允许您将零信任原则直接嵌入到您的应用程序中。 [OpenZiti Test Kitchen](https://github.com/openziti-test-kitchen) 有许多示例可以从中汲取灵感，其中包括[零信任 ssh 客户端 - zssh](https://github.com/openziti-test-kitchen/zssh)
- [Spiffe-Vault](https://github.com/philips-labs/spiffe-vault) - 利用 Spiffe JWT 身份验证和 Hashicorp Vault 进行无秘密身份验证。
- [Spire](https://github.com/spiffe/spire) - SPIRE（SPIFFE 运行时环境）是一个 API 工具链，用于在各种托管平台上的软件系统之间建立信任。

## 代码分析

_源代码分析工具，也称为静态应用程序安全测试（SAST）工具。_

- [apicompat](https://github.com/bradleyfalzon/apicompat) - 检查 Go 项目的最新更改是否存在向后不兼容的更改。
- [asty](https://github.com/asty-org/asty) - 将 golang AST 转换为 JSON，将 JSON 转换为 AST。
- [blanket](https://gitlab.com/verygoodsoftwarenotvirus/blanket) - 毯子是一个工具，可以帮助您捕获Go包中没有直接单元测试的函数。
- [ChainJacking](https://github.com/Checkmarx/chainjacking) - 查找哪些 Go lang 直接 GitHub 依赖项容易受到 ChainJacking 攻击。
- [Chronos](https://github.com/amit-davidson/Chronos) - 静态检测竞争条件
- [dupl](https://github.com/mibk/dupl) - 代码克隆检测工具。
- [errcheck](https://github.com/kisielk/errcheck) - Errcheck 是一个用于检查 Go 程序中未检查错误的程序。
- [fatcontext](https://github.com/Crocmagnon/fatcontext) - Fatcontext 检测循环或函数文本中的嵌套上下文。
- [go-checkstyle](https://github.com/qiniu/checkstyle) - checkstyle是一个类似于java checkstyle的样式检查工具。这个工具的灵感来自于java checkstyle，golint。风格参考了Go Code Review Comments中的一些观点。
- [go-cleanarch](https://github.com/roblaszczak/go-cleanarch) - go-cleanarch 的创建是为了验证干净架构规则，例如依赖关系规则以及 Go 项目中包之间的交互。
- [go-critic](https://github.com/go-critic/go-critic) - 源代码 linter 带来了当前在其他 linter 中未实现的检查。
- [go-mod-outdated](https://github.com/psampaz/go-mod-outdated) - 查找 Go 项目过时依赖项的简单方法。
- [goast-viewer](https://github.com/yuroyoro/goast-viewer) - 基于 Web 的 Golang AST 可视化工具。
- [goimports](https://pkg.go.dev/golang.org/x/tools/cmd/goimports) - 自动修复（添加、删除）Go 导入的工具。
- [golang-ifood-sdk](https://github.com/arxdsilva/golang-ifood-sdk) - iFood API SDK。
- [golangci-lint](https://github.com/golangci/golangci-lint) - 一个快速的 Go linter 运行器。它并行运行 linter，使用缓存，支持“yaml”配置，与所有主要 IDE 集成，并包含数十个 linter。
- [golines](https://github.com/segmentio/golines) - 自动缩短 Go 代码中长行的格式化程序。
- [gomarklint](https://github.com/shinagawa-web/gomarklint) - 带有内置 HTTP 链接验证的 Markdown linter，单个二进制文件，不需要 Node.js。
- [GoPlantUML](https://github.com/jfeliu007/goplantuml) - 生成文本 plantump 类图的库和 CLI，其中包含有关结构和接口的信息以及它们之间的关系。
- [goreturns](https://github.com/sqs/goreturns) - 添加零值返回语句以匹配 func 返回类型。
- [gostatus](https://github.com/shurcooL/gostatus) - 命令行工具，显示包含 Go 包的存储库的状态。
- [lint](https://github.com/surullabs/lint) - 运行 linter 作为 go 测试的一部分。
- [php-parser](https://github.com/z7zmey/php-parser) - 用 Go 编写的 PHP 解析器。
- [revive](https://github.com/mgechev/revive) - 约 6 倍更快、更严格、可配置、可扩展且美观的“golint”替代品。
- [staticcheck](https://github.com/dominikh/go-tools/tree/master/cmd/staticcheck) - staticcheck 是“加强版”，它应用了您可能习惯于使用 ReSharper for C# 等工具进行的大量静态分析检查。
- [structalign](https://github.com/peczenyj/structalign) - 展示如何重新排序结构体的字段以使用更少的内存，打印差异而不是重写文件。
- [stto](https://github.com/mainak55512/stto) - 用纯 Go 编写的轻量级超快代码行计数器。
- [testifylint](https://github.com/Antonboom/testifylint) - 检查 [github.com/stretchr/testify](https://github.com/stretchr/testify) 使用情况的 linter。
- [tickgit](https://github.com/augmentable-dev/tickgit) - CLI 和 go 包用于显示代码注释 TODO（以任何语言）并应用“gitblame”来识别作者。
- [todocheck](https://github.com/preslavmihaylov/todocheck) - 静态代码分析器将代码中的 TODO 注释与问题跟踪器中的问题链接起来。
- [unconvert](https://github.com/mdempsky/unconvert) - 从 Go 源代码中删除不必要的类型转换。
- [usestdlibvars](https://github.com/sashamelentyev/usestdlibvars) - 检测使用 Go 标准库中的变量/常量的可能性的 linter。
- [vacuum](https://github.com/daveshanley/vacuum) - 一个超超快、轻量级的 OpenAPI linter 和质量检查工具。
- [validate](https://github.com/mccoyst/validate) - 自动验证带有标签的结构字段。
- [wrapcheck](https://github.com/tomarrell/wrapcheck) - 用于检查来自外部包的错误是否被包装的 linter。

**[⬆ 回到顶部](#contents)**

## 编辑器插件

_文本编辑器和 IDE 的插件._

- [coc-go language server extension for Vim/Neovim](https://github.com/josa42/coc-go) - 该插件向 Vim/Neovim 添加了 [gopls](https://github.com/golang/tools/blob/master/gopls/README.md) 功能。
- [Go Doc](https://github.com/msyrus/vscode-go-doc) - 一个 Visual Studio Code 扩展，用于在输出中显示定义并生成 go 文档。
- [Go plugin for JetBrains IDEs](https://plugins.jetbrains.com/plugin/9568-go) - JetBrains IDE 的 Go 插件。
- [go-mode](https://github.com/dominikh/go-mode.el) - GNU/Emacs 的 Go 模式。
- [gocode](https://github.com/nsf/gocode) - Go 编程语言的自动完成守护进程。
- [goimports-reviser](https://github.com/incu6us/goimports-reviser) - 用于导入的格式化工具。
- [goprofiling](https://marketplace.visualstudio.com/items?itemName=MaxMedia.go-prof) - 此扩展向 VS Code 添加了对 Go 语言的基准分析支持。
- [GoSublime](https://github.com/DisposaBoy/GoSublime) - 文本编辑器 SublimeText 3 的 Golang 插件集合，提供代码完成和其他类似 IDE 的功能。
- [gounit-vim](https://github.com/hexdigest/gounit-vim) - Vim 插件，用于根据函数或方法的签名生成 Go 测试。
- [vim-compiler-go](https://github.com/rjohnsondev/vim-compiler-go) - Vim 插件可在保存时突出显示语法错误。
- [vim-go](https://github.com/fatih/vim-go) - Vim 的 Go 开发插件。
- [vscode-go](https://github.com/golang/vscode-go) - Visual Studio Code (VS Code) 的扩展，提供对 Go 语言的支持。
- [Watch](https://github.com/eaburns/Watch) - 在文件更改时在 acme win 中运行命令。

**[⬆ 回到顶部](#contents)**

## 去生成工具

- [envdoc](https://github.com/g4s8/envdoc) - 从 Go 源文件生成环境变量的文档。
- [generic](https://github.com/usk81/generic) - Go 的灵活数据类型。
- [gocontracts](https://github.com/Parquery/gocontracts) - 通过将代码与文档同步，将按合同设计引入 Go。
- [godal](https://github.com/mafulong/godal) - 通过指定sql ddl文件生成golang对应的orm模型，可供gorm使用。
- [gonerics](https://github.com/bouk/gonerics) - Go 中的惯用泛型。
- [gotests](https://github.com/cweill/gotests) - 从源代码生成 Go 测试。
- [gounit](https://github.com/hexdigest/gounit) - 使用您自己的模板生成 Go 测试。
- [hasgo](https://github.com/DylanMeeus/hasgo) - 为您的切片生成受 Haskell 启发的函数。
- [options-gen](https://github.com/kazhuravlev/options-gen) - Dave Cheney 的文章“友好 API 的功能选项”中描述了功能选项。
- [re2dfa](https://gitlab.com/opennota/re2dfa) - 将正则表达式转换为有限状态机并输出Go源代码。
- [sqlgen](https://github.com/anqiansong/sqlgen) - 从 SQL 文件或 DSN 生成 gorm、xorm、sqlx、bun、sql 代码。
- [TOML-to-Go](https://xuri.me/toml-to-go) - 在浏览器中立即将 TOML 转换为 Go 类型。
- [xgen](https://github.com/xuri/xgen) - XSD（XML 架构定义）解析器和 Go/C/Java/Rust/TypeScript 代码生成器。

**[⬆ 回到顶部](#contents)**

## 去工具

- [decouple](https://github.com/bobg/decouple) - 找到可以用接口类型泛化的“过度指定”函数参数。
- [docs](https://github.com/go-oas/docs) - 自动为 GO 项目生成 RESTful API 文档 - 符合开放 API 规范标准。
- [go-callvis](https://github.com/TrueFurby/go-callvis) - 使用点格式可视化 Go 程序的调用图。
- [go-size-analyzer](https://github.com/Zxilly/go-size-analyzer) - 分析并可视化已编译的 Golang 二进制文件中依赖项的大小，深入了解它们对最终构建的影响。
- [go-swagger](https://github.com/go-swagger/go-swagger) - Go 的 Swagger 2.0 实现。 Swagger 是 RESTful API 的简单而强大的表示。
- [go-template-playground](https://bartventer.github.io/go-template-playground/) - 用于创建和测试 Go 模板的交互式环境。
- [godbg](https://github.com/tylerwince/godbg) - 实现 Rusts `dbg!` 宏，以便在开发过程中快速轻松地进行调试。
- [gomodrun](https://github.com/dustinblackman/gomodrun/) - 执行和缓存 go.mod 文件中包含的二进制文件的 Go 工具。
- [gotemplate.io](https://gotemplate.io/) - 用于实时预览“文本/模板”模板的在线工具。
- [gotestdox](https://github.com/bitfield/gotestdox) - 将 Go 测试结果显示为可读句子。
- [gothanks](https://github.com/psampaz/gothanks) - GoThanks 会自动为您的 go.mod github 依赖项加注星标，以这种方式向其维护者表达一些爱意。
- [gotutor](https://github.com/ahmedakef/gotutor) - 在线 Go 调试器和可视化工具。
- [govisual](https://github.com/doganarif/govisual) - 用于本地 Go Web 开发的零配置、纯 Go HTTP 请求可视化器和调试器。
- [igo](https://github.com/rocketlaunchr/igo) - igo to go 转译器（Go 语言的新语言功能！）
- [lensm](https://github.com/loov/lensm) - 去汇编和源查看器。
- [modver](https://github.com/bobg/modver) - 根据 [semver](https://semver.org/) 规则，比较 Go 模块的两个版本，以检查所需的版本号更改（主要、次要或补丁级别）。
- [MoniGO](https://github.com/iyashjayesh/monigo) - Go 应用程序的性能监控库。它提供对应用程序性能的实时洞察！ 🚀
- [OctoLinker](https://github.com/OctoLinker/browser-extension) - 使用 GitHub 的 OctoLinker 浏览器扩展高效地浏览 go 文件。
- [richgo](https://github.com/kyoh86/richgo) - 使用文本装饰丰富“go test”输出。
- [roumon](https://github.com/becheran/roumon) - 通过命令行界面监视所有活动 goroutine 的当前状态。
- [rts](https://github.com/galeone/rts) - RTS：对结构的响应。从服务器响应生成 Go 结构。
- [textra](https://github.com/ravsii/textra) - 提取 Go 结构体字段名称、类型和标签以进行过滤和导出。
- [typex](https://github.com/dtgorski/typex) - 检查 Go 类型及其传递依赖项，或者将结果导出为 TypeScript 值对象（或类型）声明。

**[⬆ 回到顶部](#contents)**

## 软件包

_用 Go 编写的软件._

**[⬆ 回到顶部](#contents)**

### 开发运营工具

- [abbreviate](https://github.com/dnnrly/abbreviate) - abbreviate 是一种使用可配置分隔符将长字符串转换为较短字符串的工具，例如将分支名称嵌入到部署堆栈 ID 中。
- [alaz](https://github.com/ddosify/alaz) - 轻松、低开销、基于 eBPF 的 Kubernetes 监控。
- [aptly](https://github.com/aptly-dev/aptly) - aptly 是一个 Debian 存储库管理工具。
- [aurora](https://github.com/xuri/aurora) - 基于 Web 的跨平台 Beanstalkd 队列服务器控制台。
- [aws-doctor](https://github.com/elC0mpa/aws-doctor) - 直接从您的终端诊断 AWS 成本、检测闲置资源并优化云支出 🩺 ☁️。
- [awsenv](https://github.com/soniah/awsenv) - 为配置文件加载 Amazon (AWS) 环境变量的小型二进制文件。
- [Balerter](https://github.com/balerter/balerter) - 一个自托管的基于脚本的警报管理器。
- [Blast](https://github.com/dave/blast) - 用于 API 负载测试和批处理作业的简单工具。
- [bombardier](https://github.com/codesenberg/bombardier) - 快速跨平台 HTTP 基准测试工具。
- [cassowary](https://github.com/rogerwelin/cassowary) - 用 Go 编写的现代跨平台 HTTP 负载测试工具。
- [chaosmonkey](https://github.com/Netflix/chaosmonkey) - 一种弹性工具，可帮助应用程序容忍随机实例故障。
- [colima](https://github.com/abiosoft/colima) - 只需最少的设置即可在 macOS（和 Linux）上运行容器运行时。
- [Ddosify](https://github.com/ddosify/ddosify) - 高性能负载测试工具，用 Golang 编写。
- [decompose](https://github.com/s0rg/decompose) - 用于生成和处理 Docker 容器连接图的工具。
- [Den](https://github.com/us/den) - 用于 AI 代理的自托管沙箱运行时。开源 E2B 替代方案。
- [DepCharge](https://github.com/centerorbit/depcharge) - 帮助协调大型项目中多个依赖项之间的命令执行。
- [dish](https://github.com/thevxn/dish) - 轻量级、远程可配置的监控服务。
- [Docker](https://www.docker.com/) - 面向开发人员和系统管理员的分布式应用程序的开放平台。
- [docker-go-mingw](https://github.com/x1unix/docker-go-mingw) - 用于使用 MinGW 工具链为 Windows 构建 Go 二进制文件的 Docker 映像。
- [docker-volume-backup](https://github.com/offen/docker-volume-backup) - 将 Docker 卷备份到本地或任何 S3、WebDAV、Azure Blob 存储、Dropbox 或 SSH 兼容存储。
- [Dockerfile-Generator](https://github.com/ozankasikci/dockerfile-generator) - 一个 go 库和一个可执行文件，可使用各种输入通道生成有效的 Dockerfile。
- [dogo](https://github.com/liudng/dogo) - 监控源文件的变化并自动编译运行（重启）。
- [drone-jenkins](https://github.com/appleboy/drone-jenkins) - 使用二进制、docker 或 Drone CI 触发下游 Jenkins 作业。
- [drone-scp](https://github.com/appleboy/drone-scp) - 使用二进制文件、docker 或 Drone CI 通过 SSH 复制文件和工件。
- [Dropship](https://github.com/chrismckenzie/dropship) - 通过 CDN 部署代码的工具。
- [easyssh-proxy](https://github.com/appleboy/easyssh-proxy) - Golang 包可通过 SSH 轻松远程执行，并通过“ProxyCommand”下载 SCP。
- [fac](https://github.com/mkchoi212/fac) - 用于修复 git 合并冲突的命令行用户界面。
- [Flannel](https://github.com/flannel-io/flannel) - Flannel 是一种容器网络结构，专为 Kubernetes 设计。
- [Fleet device management](https://github.com/fleetdm/fleet) - 适用于服务器和工作站的轻量级可编程遥测。
- [gaia](https://github.com/gaia-pipeline/gaia) - 使用任何编程语言构建强大的管道。
- [ghorg](https://github.com/gabrie30/ghorg) - 快速将整个组织/用户存储库克隆到一个目录中 - 支持 GitHub、GitLab、Gitea 和 Bitbucket。
- [Gitea](https://github.com/go-gitea/gitea) - Fork of Gogs，完全由社区驱动。
- [gitea-github-migrator](https://git.jonasfranz.software/JonasFranzDEV/gitea-github-migrator) - 将您的所有 GitHub 存储库、问题、里程碑和标签迁移到您的 Gitea 实例。
- [go-furnace](https://github.com/go-furnace/go-furnace) - 用 Go 编写的托管解决方案。在 AWS、GCP 或 DigitalOcean 上轻松部署您的应用程序。
- [go-rocket-update](https://github.com/mouuff/go-rocket-update) - 制作自我更新 Go 应用程序的简单方法 - 支持 Github 和 Gitlab。
- [go-selfupdate](https://github.com/sanbornm/go-selfupdate) - 使您的 Go 应用程序能够自我更新。
- [gobrew](https://github.com/cryptojuice/gobrew) - gobrew 可以让你轻松地在多个版本的 go 之间切换。
- [gobrew](https://github.com/kevincobain2000/gobrew) - 去版本管理器。用于安装和管理 Go 版本的超级简单工具。无需root即可安装go。 Gobrew 不需要 shell 重新哈希。
- [godbg](https://github.com/sirnewton01/godbg) - 基于 Web 的 gdb 前端应用程序。
- [Gogs](https://gogs.io/) - 采用 Go 编程语言的自托管 Git 服务。
- [goma-gateway](https://github.com/jkaninda/goma-gateway) - 轻量级 API 网关和反向代理，具有声明式配置、强大的中间件，并支持 REST、GraphQL、TCP、UDP 和 gRPC。
- [gonative](https://github.com/inconshreveable/gonative) - 创建 Go 版本的工具，可以交叉编译到所有平台，同时仍然使用支持 Cgo 的 stdlib 包版本。
- [govvv](https://github.com/ahmetalpbalkan/govvv) - “go build”包装器可轻松将版本信息添加到 Go 二进制文件中。
- [grapes](https://github.com/yaronsumel/grapes) - 轻量级工具，旨在通过 ssh 轻松分发命令。
- [GVM](https://github.com/moovweb/gvm) - GVM 提供了管理 Go 版本的接口。
- [Hey](https://github.com/rakyll/hey) - Hey 是一个向 Web 应用程序发送一些负载的小程序。
- [httpref](https://github.com/dnnrly/httpref) - httpref 是一个方便的 CLI 参考，用于 HTTP 方法、状态代码、标头以及 TCP 和 UDP 端口。
- [jcli](https://github.com/jenkins-zh/jenkins-cli) - Jenkins CLI 允许您以简单的方式管理 Jenkins。
- [k0s](https://github.com/k0sproject/k0s) - 零摩擦 Kubernetes 发行版。
- [k3d](https://github.com/k3d-io/k3d) - 在 Docker 中运行 CNCF 的 k3s 的小帮手。
- [k3s](https://github.com/k3s-io/k3s) - 轻量级的 Kubernetes。
- [k6](https://github.com/grafana/k6) - 一种使用 Go 和 JavaScript 的现代负载测试工具。
- [k9s](https://github.com/derailed/k9s) - Kubernetes CLI 以时尚的方式管理您的集群。
- [kala](https://github.com/ajvb/kala) - 简单、现代且高性能的作业调度程序。
- [kcli](https://github.com/cswank/kcli) - 用于检查 kafka 主题/分区/消息的命令行工具。
- [kepfi](https://github.com/Knuspii/kepfi) - 带有恢复箱和存储跟踪功能的 rm 的智能替代品。
- [kind](https://github.com/kubernetes-sigs/kind) - Kubernetes IN Docker - 用于测试 Kubernetes 的本地集群。
- [ko](https://github.com/google/ko) - 用于在 Kubernetes 上构建和部署 Go 应用程序的命令行工具
- [kool](https://github.com/kool-dev/kool) - 用于以简单方式管理 Docker 环境的命令行工具。
- [kubeblocks](https://github.com/apecloud/kubeblocks) - KubeBlocks 是一个开源控制平面，可在 K8s 上运行和管理数据库、消息队列和其他数据基础设施。
- [kubefwd](https://github.com/txn2/kubefwd) - 批量 Kubernetes 端口转发，每个服务具有唯一的 IP，用于本地开发。
- [kubernetes](https://github.com/kubernetes/kubernetes) - 来自 Google 的容器集群管理器。
- [kubeshark](https://github.com/kubeshark/kubeshark) - 适用于 Kubernetes 的 API 流量分析器，受 Wireshark 启发，专为 Kubernetes 构建。
- [KubeVela](https://github.com/kubevela/kubevela) - 云原生应用程序交付。
- [KubeVPN](https://github.com/kubenetworks/kubevpn) - KubeVPN 提供了一个云原生开发环境，可以无缝连接到您的 Kubernetes 集群网络。
- [KusionStack](https://github.com/KusionStack/kusion) - 统一的可编程配置技术堆栈，以“平台即代码”和“基础设施即代码”方法提供现代应用程序。
- [kwatch](https://github.com/abahmed/kwatch) - 立即监控和检测 Kubernetes(K8s) 集群中的崩溃情况。
- [lstags](https://github.com/ivanilves/lstags) - 用于跨不同注册表同步 Docker 映像的工具和 API。
- [lwc](https://github.com/timdp/lwc) - UNIX wc 命令的实时更新版本。
- [manssh](https://github.com/xwjdsh/manssh) - manssh 是一个命令行工具，用于轻松管理 ssh 别名配置。
- [Mantil](https://github.com/mantil-io/mantil) - 用于在 AWS 上构建无服务器应用程序的 Go 特定框架，使您能够专注于纯 Go 代码，而 Mantil 负责基础设施。
- [minikube](https://github.com/kubernetes/minikube) - 在本地运行 Kubernetes。
- [Moby](https://github.com/moby/moby) - 容器生态系统的协作项目，用于组装基于容器的系统。
- [Mora](https://github.com/emicklei/mora) - 用于访问 MongoDB 文档和元数据的 REST 服务器。
- [ostent](https://github.com/ostrost/ostent) - 收集并显示系统指标，并可选择中继到 Graphite 和/或 InfluxDB。
- [Packer](https://github.com/mitchellh/packer) - Packer 是一种从单一源配置为多个平台创建相同机器映像的工具。
- [Pewpew](https://github.com/bengadbois/pewpew) - 灵活的 HTTP 命令行压力测试器。
- [pingtower](https://github.com/crleonard/pingtower) - 适用于网站和 API 的轻量级自托管正常运行时间监视器。
- [PipeCD](https://github.com/pipe-cd/pipecd) - GitOps 风格的持续交付平台，可为任何应用程序提供一致的部署和操作体验。
- [podinfo](https://github.com/stefanprodan/podinfo) - Podinfo 是一个用 Go 制作的小型 Web 应用程序，展示了在 Kubernetes 中运行微服务的最佳实践。 Flux 和 Flagger 等 CNCF 项目使用 Podinfo 进行端到端测试和研讨会。
- [podman-tui](https://github.com/containers/podman-tui) - 用于 Podman 管理的终端 UI。
- [Pomerium](https://github.com/pomerium/pomerium) - Pomerium 是一个身份识别访问代理。
- [Rodent](https://github.com/alouche/rodent) - Rodent 帮助您管理 Go 版本、项目并跟踪依赖项。
- [s3-proxy](https://github.com/oxyno-zeta/s3-proxy) - 具有 GET、PUT 和 DELETE 方法和身份验证（OpenID Connect 和基本身份验证）的 S3 代理。
- [s3gof3r](https://github.com/rlmcpherson/s3gof3r) - 针对大型对象高速传输进出 Amazon S3 进行了优化的小型实用程序/库。
- [s5cmd](https://github.com/peak/s5cmd) - 极快的 S3 和本地文件系统执行工具。
- [Scaleway-cli](https://github.com/scaleway/scaleway-cli) - 从命令行管理裸机服务器（就像使用 Docker 一样轻松）。
- [script](https://github.com/bitfield/script) - 可以轻松地在 Go 中编写类似 shell 的脚本来执行 DevOps 和系统管理任务。
- [sg](https://github.com/ChristopherRabotin/sg) - 对一组 HTTP 端点（如 ab）进行基准测试，可以根据之前的响应使用每次调用之间的响应代码和数据来确定特定的服务器压力。
- [sigma](https://github.com/go-sigma/sigma) - OCI原生容器镜像注册中心，支持OCI原生工件、扫描工件、镜像构建等。
- [skm](https://github.com/TimothyYe/skm) - SKM 是一个简单而强大的 SSH 密钥管理器，它可以帮助您轻松管理多个 SSH 密钥！
- [StatusOK](https://github.com/sanathp/statusok) - 监控您的网站和 REST API。当您的服务器关闭或响应时间超过预期时，通过 Slack、电子邮件收到通知。
- [tau](https://github.com/taubyte/tau) - 使用无服务器 WebAssembly 功能、前端托管、CI/CD、对象存储、K/V 数据库和 Pub-Sub 消息传递等功能轻松构建云计算平台。
- [terraform-provider-openapi](https://github.com/dikhan/terraform-provider-openapi) - Terraform 提供程序插件，可根据包含公开的 API 定义的 OpenAPI 文档（以前称为 swagger 文件）在运行时动态配置自身。
- [tickstem/uptime](https://github.com/tickstem/uptime) - Go 客户端可通过 SSL 过期警报和可配置的响应断言进行 HTTP 正常运行时间监控。
- [tf-profile](https://github.com/datarootsio/tf-profile) - Terraform 运行的探查器。生成全局统计数据、资源级统计数据或可视化。
- [tlm](https://github.com/yusufcanb/tlm) - 本地 cli copilot，由 CodeLLaMa 提供支持
- [traefik](https://github.com/containous/traefik) - 支持多个后端的反向代理和负载均衡器。
- [trubka](https://github.com/xitonix/trubka) - 用于管理 Apache Kafka 集群并对其进行故障排除的 CLI 工具，通常能够向 Kafka 发布/使用协议缓冲区和纯文本事件。
- [Updatecli](https://github.com/updatecli/updatecli) - 通用声明性更新策略引擎。
- [uTask](https://github.com/ovh/utask) - 对 yaml 中声明的业务流程进行建模和执行的自动化引擎。
- [Vegeta](https://github.com/tsenart/vegeta) - HTTP 负载测试工具和库。已经9000多了！
- [wait-for](https://github.com/dnnrly/wait-for) - 等待某些事情发生（从命令行），然后再继续。轻松编排 Docker 服务和其他事物。
- [Wide](https://wide.b3log.org/login) - 使用 Golang 的基于 Web 的 Teams IDE。
- [winrm-cli](https://github.com/masterzen/winrm-cli) - 用于在 Windows 机器上远程执行命令的 CLI 工具。
- [zerohand](https://github.com/nilpoona/zerohand) - 一个简单高效的 Web API 负载测试工具。

**[⬆ 回到顶部](#contents)**

### 其他软件

- [Backrest](https://github.com/garethgeorge/backrest) - 基于 Web 的 UI 和协调器，用于静态备份。
- [Better Go Playground](https://goplay.tools) - Go Playground 具有语法高亮、代码完成和其他功能。
- [blocky](https://github.com/0xERR0R/blocky) - 快速、轻量级的 DNS 代理作为本地网络的广告拦截器，具有多种功能。
- [bluetuith](https://github.com/bluetuith-org/bluetuith) - 适用于 Linux 的 TUI 蓝牙管理器。
- [borg](https://github.com/crufter/borg) - 基于终端的 bash 片段搜索引擎。
- [boxed](https://github.com/tejo/boxed) - 基于 Dropbox 的博客引擎。
- [Chapar](https://github.com/chapar-rest/chapar) - Chapar 是一个用 go 构建的跨平台 Postman 替代品，旨在帮助开发人员测试他们的 api 端点。它支持http和grpc协议。
- [Cherry](https://github.com/rafael-santiago/cherry) - Go 中的小型网络聊天服务器。
- [Circuit](https://github.com/gocircuit/circuit) - Circuit 是一种可编程平台即服务 (PaaS) 和/或基础设施即服务 (IaaS)，用于管理、发现、同步和编排包含云应用程序的服务和主机。
- [Comcast](https://github.com/tylertreat/Comcast) - 模拟不良网络连接。
- [confd](https://github.com/kelseyhightower/confd) - 使用来自 etcd 或 consul 的模板和数据管理本地应用程序配置文件。
- [crawley](https://github.com/s0rg/crawley) - cli 的网络抓取/爬虫。
- [croc](https://github.com/schollz/croc) - 轻松安全地将文件或文件夹从一台计算机发送到另一台计算机。
- [CrunchyCleaner](https://github.com/Knuspii/CrunchyCleaner) - 适用于 Windows 和 Linux 的轻量级软件缓存清理工具。
- [Documize](https://github.com/documize/community) - 现代 wiki 软件集成了来自 SaaS 工具的数据。
- [dp](https://github.com/scryinfo/dp) - 通过与区块链进行数据交换的SDK，开发者可以轻松接入DAPP开发。
- [drive](https://github.com/odeke-em/drive) - 用于命令行的 Google Drive 客户端。
- [Duplicacy](https://github.com/gilbertchen/duplicacy) - 一款基于无锁重复数据删除思想的跨平台网络和云备份工具。
- [fjira](https://github.com/mk-5/fjira) - Attlasian Jira 基于模糊搜索的终端 UI 应用程序
- [Gebug](https://github.com/moshebe/gebug) - 该工具通过无缝启用调试器和热重载功能，使 Dockerized Go 应用程序的调试变得超级简单。
- [gfile](https://github.com/Antonito/gfile) - 通过 WebRTC 在两台计算机之间安全地传输文件，无需任何第三方。
- [Go Package Store](https://github.com/shurcooL/Go-Package-Store) - 显示 GOPATH 中 Go 软件包更新的应用程序。
- [go-peerflix](https://github.com/Sioro-Neoku/go-peerflix) - 视频流 torrent 客户端。
- [goblin](https://goblin.run) - 用 go lang 编写的 CLI 云构建器
- [GoBoy](https://github.com/Humpheh/goboy) - 用 Go 编写的 Nintendo Game Boy Color 模拟器。
- [gocc](https://github.com/goccmack/gocc) - Gocc 是一个用 Go 编写的 Go 编译器套件。
- [GoDocTooltip](https://github.com/diankong/GoDocTooltip) - Go Doc 站点的 Chrome 扩展，它在函数列表中将函数描述显示为工具提示。
- [Gokapi](https://github.com/Forceu/gokapi) - 用于共享文件的轻量级服务器，文件在一定的下载量或天数后就会过期。与 Firefox Send 类似，但没有公开上传。
- [GoLand](https://jetbrains.com/go) - 全功能的跨平台 Go IDE。
- [GoNB](https://github.com/janpfeifer/gonb) - 使用 Jupyter Notebooks 进行交互式 Go 编程（也适用于 VSCode、Binder 和 Google 的 Colab）。
- [GooseForum](https://github.com/leancodebox/GooseForum) - 使用 Go、Vue 和 Tailwind CSS 构建的自托管论坛平台。
- [Gor](https://github.com/buger/gor) - HTTP 流量复制工具，用于实时重播从生产到阶段/开发环境的流量。
- [Guora](https://github.com/meloalright/guora) - 一个用 Go 编写的类似 Quora 的自托管 Web 应用程序。
- [hoofli](https://github.com/dnnrly/hoofli) - 从 Chrome 或 Firefox 网络检查生成 PlantUML 图。
- [hotswap](https://github.com/edwingeng/hotswap) - 一个完整的解决方案，可以重新加载 Go 代码，而无需重新启动服务器、中断或阻止任何正在进行的过程。
- [hugo](https://gohugo.io/) - 快速而现代的静态网站引擎。
- [ide](https://github.com/thestrukture/ide) - 浏览器可访问的 IDE。专为 Go 设计。
- [joincap](https://github.com/assafmo/joincap) - 用于将多个 pcap 文件合并在一起的命令行实用程序。
- [JuiceFS](https://github.com/juicedata/juicefs) - 构建在 Redis 和 AWS S3 之上的分布式 POSIX 文件系统。
- [Juju](https://jujucharms.com/) - 与云无关的服务部署和编排 - 支持 EC2、Azure、Openstack、MAAS 等。
- [Layli](https://layli.app) - 以代码形式绘制漂亮的布局图。
- [Leaps](https://github.com/jeffail/leaps) - 使用操作转换的结对编程服务。
- [lgo](https://github.com/yunabe/lgo) - 使用 Jupyter 进行交互式 Go 编程。它支持代码补全、代码检查和 100% Go 兼容性。
- [limetext](https://limetext.github.io) - Lime Text 是一款功能强大且优雅的文本编辑器，主要用 Go 开发，旨在成为 Sublime Text 的免费开源软件继承者。
- [LiteIDE](https://github.com/visualfc/liteide) - LiteIDE 是一个简单、开源、跨平台的 Go IDE。
- [mac-cleanup-go](https://github.com/2ykwang/mac-cleanup-go) - 用于清理 macOS 缓存、日志和临时文件的预览优先 TUI。
- [mdv](https://github.com/Allra-Fintech/mdv) - CLI 工具，可在浏览器中呈现 Markdown 文件，具有实时重新加载、GFM、语法突出显示、美人鱼图和 PDF 导出功能。
- [mockingjay](https://github.com/quii/mockingjay-server) - 来自一个配置文件的虚假 HTTP 服务器和消费者驱动的合约。您还可以让服务器随机出现异常行为，以帮助进行更真实的性能测试。
- [myLG](https://github.com/mehrdadrad/mylg) - 用 Go 编写的命令行网络诊断工具。
- [naclpipe](https://github.com/unix4fun/naclpipe) - 用 Go 编写的基于 NaCL EC25519 的简单加密管道工具。
- [Neo-cowsay](https://github.com/Code-Hex/Neo-cowsay) - 🐮 牛赛重生了。为了新时代。
- [nes](https://github.com/fogleman/nes) - 用 Go 编写的任天堂娱乐系统 (NES) 模拟器。
- [onWatch](https://github.com/onllm-dev/onWatch) - 通过历史跟踪、警报和 Web 仪表板在本地监控跨提供商的 AI API 配额，以避免意外限制和预算超支。
- [Orbit](https://github.com/gulien/orbit) - 一个用于运行命令和从模板生成文件的简单工具。
- [peg](https://github.com/pointlander/peg) - Peg（解析表达式语法）是 Packrat 解析器生成器的实现。
- [Plik](https://github.com/root-gg/plik) - Plik 是 Go 中的临时文件上传系统（类似 Wetransfer）。
- [portal](https://github.com/SpatiumPortae/portal) - Portal 是一个快速、简单的命令行文件传输实用程序，可以从任何计算机传输到另一台计算机。
- [restic](https://github.com/restic/restic) - 重复数据删除备份程序。
- [sake](https://github.com/alajmo/sake) - 清酒是本地和远程主机的命令运行程序。
- [scc](https://github.com/boyter/scc) - Sloc Cloc and Code，一个非常快速、准确的代码计数器，具有复杂性计算和 COCOMO 估计功能。
- [Seaweed File System](https://github.com/chrislusf/seaweedfs) - 具有 O(1) 磁盘寻道功能的快速、简单且可扩展的分布式文件系统。
- [shell2http](https://github.com/msoap/shell2http) - 通过 http 服务器执行 shell 命令（用于原型设计或远程控制）。
- [Snitch](https://github.com/lucasgomide/snitch) - 当有人通过 Tsuru 部署任何应用程序时，通知您的团队和许多工具的简单方法。
- [sonic](https://github.com/go-sonic/sonic) - Sonic 是一个 Go 博客平台。简单而强大。
- [Stack Up](https://github.com/pressly/sup) - Stack Up，一个超级简单的部署工具——只是 Unix——可以把它想象成服务器网络的“make”。
- [stew](https://github.com/marwanhawari/stew) - 用于编译二进制文件的独立包管理器。
- [syncthing](https://syncthing.net/) - 开放、去中心化的文件同步工具和协议。
- [tcpdog](https://github.com/mehrdadrad/tcpdog) - 基于 eBPF 的 TCP 可观测性。
- [tinycare-tui](https://github.com/DMcP89/tinycare-tui) - 小型终端应用程序，显示过去 24 小时和一周的 git 提交、当前天气、一些自我护理建议、一个笑话以及您当前的待办事项列表任务。
- [tldx](https://github.com/brandonyoungdev/tldx) - 使用 RDAP、DNS 和 WHOIS 回退以及关键字排列生成的批量域可用性检查器。
- [toxiproxy](https://github.com/shopify/toxiproxy) - 用于模拟网络和系统条件以进行自动化测试的代理。
- [tsuru](https://tsuru.io/) - 可扩展的开源平台即服务软件。
- [vaku](https://github.com/lingrino/vaku) - CLI 和 API，用于 Vault 中基于文件夹的功能，例如复制、移动和搜索。
- [vFlow](https://github.com/VerizonDigital/vflow) - 高性能、可扩展且可靠的 IPFIX、sFlow 和 Netflow 收集器。
- [Wave Terminal](https://waveterm.dev) - Wave 是一款开源 AI 原生终端，专为无缝开发人员工作流程而构建，具有内联渲染、现代 UI 和持久会话。
- [wellington](https://github.com/wellington/wellington) - Sass 项目管理工具，通过 sprite 功能扩展了语言（如 Compass）。
- [woke](https://github.com/get-woke/woke) - 检测源代码中的非包容性语言。
- [yai](https://github.com/ekkinox/yai) - AI驱动的终端助手。
- [zs](https://git.mills.io/prologic/zs) - 一个极其最小的静态站点生成器。

**[⬆ 回到顶部](#contents)**

# 资源

_在哪里发现新的 Go 库._

**[⬆ 回到顶部](#contents)**

## 基准测试

- [autobench](https://github.com/davecheney/autobench) - 用于比较不同 Go 版本之间性能的框架。
- [go-benchmark-app](https://github.com/mrLSD/go-benchmark-app) - 强大的 HTTP 基准测试工具与 Аb、Wrk、Siege 工具混合在一起。收集统计数据和各种参数以进行基准测试和比较结果。
- [go-benchmarks](https://github.com/tylertreat/go-benchmarks) - 很少有其他的 Go 微基准测试。将一些语言功能与替代方法进行比较。
- [go-http-routing-benchmark](https://github.com/julienschmidt/go-http-routing-benchmark) - Go HTTP 请求路由器基准测试和比较。
- [go-json-benchmark](https://github.com/zerosnake0/go-json-benchmark) - 进行 JSON 基准测试。
- [go-ml-benchmarks](https://github.com/nikolaydubina/go-ml-benchmarks) - Go 中机器学习推理的基准。
- [go-web-framework-benchmark](https://github.com/smallnest/go-web-framework-benchmark) - Go Web 框架基准测试。
- [go_serialization_benchmarks](https://github.com/alecthomas/go_serialization_benchmarks) - Go 序列化方法的基准。
- [gocostmodel](https://github.com/PuerkitoBio/gocostmodel) - Go语言常见基本操作的基准。
- [golang-benchmarks](https://github.com/SimonWaldherr/golang-benchmarks) - golang 基准的集合。
- [golang-sql-benchmark](https://github.com/tyler-smith/golang-sql-benchmark) - 流行的 Go 数据库/SQL 实用程序的基准集合。
- [gospeed](https://github.com/feyeleanor/GoSpeed) - 用于计算语言构造速度的 Go 微基准。
- [kvbench](https://github.com/jimrobinson/kvbench) - 键/值数据库基准。
- [skynet](https://github.com/atemerev/skynet) - Skynet 1M 线程微基准测试。
- [speedtest-resize](https://github.com/fawick/speedtest-resize) - 比较 Go 语言的各种图像调整大小算法。
- [vizb](https://github.com/goptics/vizb) - 用于以 4D 形式可视化 Go 基准数据的 CLI 工具。

**[⬆ 回到顶部](#contents)**

## 会议

- [GoCon](https://gocon.connpass.com/) - 日本东京。
- [GoDays](https://www.godays.io/) - 德国柏林。
- [GoLab](https://golab.io/) - 意大利佛罗伦萨。
- [GopherCon](https://www.gophercon.com/) - 美国每年都有不同地点。
- [GopherCon Africa](https://gophercon.africa/) - 肯尼亚内罗毕。
- [GopherCon Australia](https://gophercon.com.au/) - 澳大利亚悉尼。
- [GopherCon Brazil](https://gopherconbr.org) - 巴西弗洛里亚诺波利斯。
- [GopherCon China](https://gophercon.com.cn) - 中国上海。
- [GopherCon Europe](https://gophercon.eu/) - 德国柏林。
- [GopherCon India](https://gopherconindia.org/) - 印度浦那。
- [GopherCon Israel](https://www.gophercon.org.il/) - 以色列特拉维夫。
- [GopherCon Russia](https://www.gophercon-russia.ru) - 俄罗斯莫斯科。
- [GopherCon Singapore](https://gophercon.sg) - 新加坡丰树商业城。
- [GopherCon UK](https://www.gophercon.co.uk/) - 英国伦敦。
- [GopherCon Vietnam](https://gophercon.vn/) - 越南胡志明市。
- [GoWest Conference](https://www.gowestconf.com/) - 美国李海。

**[⬆ 回到顶部](#contents)**

## 电子书

### 可供购买的电子书

- [100 个围棋错误：如何避免它们](https://www.manning.com/books/100-go-mistakes-how-to-avoid-them)
- [Black Hat Go](https://nostarch.com/blackhatgo) - 为黑客和渗透测试人员进行编程。
- [用 Go 构建 Orchestrator](https://www.manning.com/books/build-an-orchestrator-in-go)
- [Continuous Delivery in Go](https://www.manning.com/books/continuous-delivery-in-go) - 这本持续交付实用指南向您展示如何快速建立自动化管道，以改进您的测试、代码质量和最终产品。
- [Creative DIY Microcontroller Project With TinyGo and WebAssembly](https://www.packtpub.com/product/creative-diy-microcontroller-projects-with-tinygo-and-webassembly/9781800560208) - 介绍 TinyGo 编译器以及涉及 Arduino 和 WebAssembly 的项目。
- [Effective Go: Elegant, efficient, and testable code](https://www.manning.com/books/effective-go) - 解锁 Go 对程序设计的独特视角，开始编写简单、可维护、可测试的 Go 代码。
- [For the Love of Go](https://bitfieldconsulting.com/books/love) - 一本针对 Go 初学者的入门书籍。
- [Go in Practice, Second Edition](https://www.manning.com/books/go-in-practice-second-edition) - 关于 Go 开发细节的实用指南，涵盖标准库和 Go 强大生态系统中最重要的工具。
- [Know Go: Generics](https://bitfieldconsulting.com/books/generics) - 理解和使用 Go 中泛型的指南。
- [Lets-Go](https://lets-go.alexedwards.net) - 使用 Go 创建快速、安全且可维护的 Web 应用程序的分步指南。
- [Lets-Go-Further](https://lets-go-further.alexedwards.net) - 在 Go 中构建 API 和 Web 应用程序的高级模式。
- [The Power of Go: Tests](https://bitfieldconsulting.com/books/tests) - Go 测试指南。
- [The Power of Go: Tools](https://bitfieldconsulting.com/books/tools) - 在 Go 中编写命令行工具的指南。
- [用 Go 编写编译器](https://compilerbook.com)
- [Writing An Interpreter In Go](https://interpreterbook.com) - 本书介绍了数十种编写惯用的、富有表现力的、高效的 Go 代码的技术，避免了常见的陷阱。

### 免费电子书

- [Go 开发者笔记本](https://leanpub.com/GoNotebook/read)
- [Go 编程简介](http://www.golang-book.com/)
- [Build a blockchain from scratch in Go with gRPC](https://github.com/volodymyrprokopyuk/go-blockchain) - 使用 gRPC 在 Go 中有效学习并逐步从头开始构建区块链的基础实用指南。
- [使用 Golang 构建 Web 应用程序](https://astaxie.gitbooks.io/build-web-application-with-golang/content/en/)
- [使用 Go 构建 Web 应用程序](https://codegangsta.gitbooks.io/building-web-apps-with-go/content/)
- [Go 101](https://go101.org) - 一本专注于 Go 语法/语义和各种细节的书。
- [Go AST Book (Chinese)](https://github.com/chai2010/go-ast-book) - 一本专注于 Go `go/*` 包的书。
- [Go Faster](https://leanpub.com/gofaster) - 本书旨在缩短您的学习曲线，帮助您更快地成为一名熟练的 Go 程序员。
- [Go Succinctly](https://github.com/thedevsir/gosuccinctly) - 波斯语。
- [Go with the domain](https://threedots.tech/go-with-the-domain/) - 这本书展示了如何通过实际重构来应用 DDD、Clean Architecture 和 CQRS。
- [GoBooks](https://github.com/dariubs/GoBooks) - 精选的 Go 书籍列表。
- [How To Code in Go eBook](https://www.digitalocean.com/community/books/how-to-code-in-go-ebook) - 针对初次开发者的 600 页 Go 简介。
- [学习围棋](https://www.miek.nl/downloads/Go/Learning-Go-latest.pdf)
- [使用 Go 进行网络编程](https://jan.newmarch.name/golang/)
- [围棋实用课程](https://www.practical-go-lessons.com/)
- [宇宙飞船标准库之旅](https://blasrodri.github.io/spaceship-go-gh-pages/)
- [Go 编程语言](https://www.gopl.io/)
- [Golang 标准库示例（中文）](https://github.com/polaris1119/The-Golang-Standard-Library-by-Example)
- [小Go书](https://github.com/karlseguin/the-little-go-book)
- [Go 的 Web 应用程序反教科书](https://github.com/thewhitetulip/web-dev-golang-anti-textbook/)

**[⬆ 回到顶部](#contents)**

## 地鼠

- [Free Gophers Pack](https://github.com/MariaLetta/free-gophers-pack) - 由 Maria Letta 制作的 Gopher 图形包，包含矢量和光栅插图和情感人物。
- [Go-gopher-Vector](https://github.com/keygx/Go-gopher-Vector) - Go gopher 矢量数据 [.ai，.svg]。
- [gopher-logos](https://github.com/GolangUA/gopher-logos) - 可爱的地鼠标志。
- [gopher-stickers](https://github.com/tenntenn/gopher-stickers)
- [gophericons](https://github.com/shalakhin/gophericons)
- [gopherize.me](https://github.com/matryer/gopherize.me) - Gopher化你自己。
- [gophers](https://github.com/ashleymcnamara/gophers) - 阿什利·麦克纳马拉 (Ashley McNamara) 的地鼠艺术作品。
- [gophers](https://github.com/egonelbre/gophers) - 自由地鼠。
- [gophers](https://github.com/rogeralsing/gophers) - 随机地鼠图形。
- [gophers](https://github.com/sillecelik/go-gopher) - 地鼠阿米古鲁米玩具图案。
- [gophers](https://github.com/scraly/gophers) - Aurélie Vache 的《地鼠》。

**[⬆ 回到顶部](#contents)**

## 聚会

- [巴塞尔 Go 聚会](https://www.meetup.com/Basel-Go-Meetup/)
- [贝尔法斯特地鼠队](https://www.meetup.com/Belfast-Gophers/)
- [贝尔格莱德 Golang 聚会](https://www.meetup.com/golang-serbia/)
- [柏林戈朗](https://www.meetup.com/golang-users-berlin/)
- [布里斯班地鼠队](https://www.meetup.com/Brisbane-Golang-Meetup/)
- [Bärner Go 聚会 - 瑞士伯尔尼](https://www.meetup.com/berner-go-meetup/)
- [去爱尔兰 - 都柏林](https://www.meetup.com/goireland/)
- [Go 语言纽约](https://www.meetup.com/golanguagenewyork/)
- [去伦敦用户组](https://www.meetup.com/Go-London-User-Group/)
- [参加远程聚会](https://www.meetup.com/Go-Remote-Meetup/)
- [去多伦多](https://www.meetup.com/go-toronto/)
- [亚特兰大 Go 用户组](https://www.meetup.com/Go-Users-Group-Atlanta/)
- [GoBandung](https://www.meetup.com/GoBandung/)
- [GoBridge，旧金山，加利福尼亚州](https://www.meetup.com/gobridge/)
- [GoCracow - 克拉科夫, 波兰](https://www.meetup.com/GoCracow/)
- [GoJakarta](https://www.meetup.com/GoJakarta/)
- [阿姆斯特丹 Golang](https://www.meetup.com/golang-amsterdam/)
- [戈兰阿根廷](https://www.meetup.com/Golang-Argentina/)
- [戈朗雅典](https://www.meetup.com/Athens-Gophers/)
- [马里兰州巴尔的摩戈朗](https://www.meetup.com/BaltimoreGolang/)
- [戈朗班加罗尔](https://www.meetup.com/Golang-Bangalore/)
- [Golang 贝洛奥里藏特 - 巴西](https://www.meetup.com/go-belo-horizonte/)
- [戈朗波士顿](https://www.meetup.com/bostongo/)
- [保加利亚](https://www.meetup.com/Golang-Bulgaria/)
- [Golang 英国卡迪夫](https://www.meetup.com/Cardiff-Go-Meetup/)
- [哥本哈根Golang](https://www.meetup.com/Go-Cph/)
- [Golang 库里蒂巴 - 巴西](https://www.meetup.com/GolangCWB/)
- [Golang DC，阿灵顿，弗吉尼亚州](https://www.meetup.com/Golang-DC/)
- [英国多塞特郡戈朗](https://www.meetup.com/golang-dorset/)
- [爱沙尼亚](https://www.meetup.com/Golang-Estonia/)
- [印度戈朗古尔冈](https://www.meetup.com/Gurgaon-Go-Meetup/)
- [Golang 汉堡 - 德国](https://www.meetup.com/Go-User-Group-Hamburg/)
- [戈兰以色列](https://www.meetup.com/Go-Israel/)
- [加德满都戈朗](https://www.meetup.com/Golang-Kathmandu/)
- [戈朗利马 - 秘鲁](https://www.meetup.com/Golang-Peru/)
- [里昂高朗](https://www.meetup.com/Golang-Lyon/)
- [戈朗马赛](https://www.meetup.com/fr-FR/Golang-Marseille/)
- [墨尔本戈兰](https://www.meetup.com/golang-mel/)
- [米兰高朗](https://www.meetup.com/golang-milano/)
- [戈朗东北](https://www.meetup.com/en-AU/Golang-North-East/)
- [巴黎高朗](https://www.meetup.com/Golang-Paris/)
- [波兰](https://www.meetup.com/Golang-Poland/)
- [戈朗浦那](https://www.meetup.com/Golang-Pune/)
- [戈朗罗马](https://www.meetup.com/golangroma/)
- [鹿特丹戈朗](https://www.meetup.com/golang-rotterdam/)
- [新加坡Golang](https://www.meetup.com/golangsg/)
- [戈朗 斯德哥尔摩](https://www.meetup.com/Go-Stockholm/)
- [Golang 澳大利亚悉尼](https://www.meetup.com/golang-syd/)
- [圣保罗 Golang - 巴西](https://www.meetup.com/golangbr/)
- [台北高朗](https://www.meetup.com/golang-taipei-meetup/)
- [塞萨洛尼基Golang](https://www.meetup.com/thessaloniki-golang-meetup/)
- [都灵Golang](https://www.meetup.com/golang-torino/)
- [戈朗土耳其](https://kommunity.com/goturkiye)
- [Golang 温哥华, BC](https://www.meetup.com/golangvan/)
- [Golang 奥地利维也纳](https://www.meetup.com/viennago/)
- [Golang 莫斯卡夫](https://www.meetup.com/Golang-Moscow/)
- [GoSF - 加利福尼亚州旧金山](https://www.meetup.com/golangsf)
- [伊斯坦布尔戈朗](https://www.meetup.com/Istanbul-Golang/)
- [拉各斯地鼠队](https://www.meetup.com/GolangNigeria/)
- [内罗毕地鼠队](https://www.meetup.com/nairobi-gophers/)
- [西雅图 Go 程序员](https://www.meetup.com/golang/)
- [乌克兰 Golang 用户组](https://www.meetup.com/uagolang/)
- [犹他州 Go 用户组](https://www.meetup.com/utahgophers/)
- [女性出行者 - 旧金山，加利福尼亚州](https://www.meetup.com/Women-Who-Go/)
- [苏黎世地鼠队 - 苏黎世, 瑞士](https://www.meetup.com/zurich-gophers/)

_在此处添加您所在城市/国家的群组（发送 **PR**）_

**[⬆ 回到顶部](#contents)**

## 风格指南

- [bahlo/go-styleguide](https://github.com/bahlo/go-styleguide)
- [CockroachDB](https://github.com/cockroachdb/cockroach/blob/master/docs/style.md)
- [GitLab](https://docs.gitlab.com/ee/development/go_guide/)
- [Google](https://google.github.io/styleguide/go/)
- [Hyperledger](https://github.com/hyperledger/fabric/blob/release-1.4/docs/source/style-guides/go-style.rst)
- [Thanos](https://thanos.io/tip/contributing/coding-style-guide.md/)
- [Trybe](https://github.com/betrybe/playbook-go/blob/main/README_EN.md)
- [Uber](https://github.com/uber-go/guide/blob/master/style.md)

**[⬆ 回到顶部](#contents)**

## 社交媒体

### 推特

- [@GoDiscussions](https://twitter.com/GoDiscussions)
- [@golang](https://twitter.com/golang)
- [@golang_news](https://twitter.com/golang_news)
- [@golangch](https://twitter.com/golangch)
- [@golangweekly](https://twitter.com/golangweekly)

**[⬆ 回到顶部](#contents)**

### 红迪网

- [r/golang](https://www.reddit.com/r/golang/)

**[⬆ 回到顶部](#contents)**

## 网站

- [Awesome Go @LibHunt](https://go.libhunt.com) - 您的首选 Go 工具箱。
- [Awesome Golang Workshops](https://github.com/amit-davidson/awesome-golang-workshops) - 精彩的 golang 研讨会精选列表。
- [Awesome Remote Job](https://github.com/lukasz-madon/awesome-remote-job) - 精选的精彩远程工作列表。他们中的很多人都在寻找 Go 黑客。
- [awesome-awesomeness](https://github.com/bayandin/awesome-awesomeness) - 其他令人惊叹的很棒的列表的列表。
- [awesome-go-extra](https://github.com/xwjdsh/awesome-go-extra) - 解析 Awesome-go README 文件并生成一个包含存储库信息的新 README 文件。
- [Code with Mukesh](https://codewithmukesh.com/categories/golang) - 软件工程师和博客@codewithmukesh.com。
- [Coding Mystery](https://codingmystery.com) - 使用 Go 解决令人兴奋的密室逃脱编程挑战。
- [CodinGame](https://www.codingame.com/) - 通过使用小游戏作为实际例子来解决交互式任务来学习围棋。
- [Go Blog](https://blog.golang.org) - Go 官方博客。
- [Go Code Club](https://www.youtube.com/watch?v=nvoIPQYdx9g&list=PLEcwzBXTPUE_YQR7R0BRtHBYJ0LN3Y0i3) - 一群 Gophers 每周阅读并讨论一个不同的 Go 项目。
- [Go Community on Hashnode](https://hashnode.com/n/go) - Hashnode 上的 Gophers 社区。
- [Go Forum](https://forum.golangbridge.org) - 讨论 Go 的论坛。
- [Go Projects](https://github.com/golang/go/wiki/Projects) - Go 社区 wiki 上的项目列表。
- [Go Proverbs](https://go-proverbs.github.io/) - 罗布·派克的《Go Proverbs》。
- [Go Report Card](https://goreportcard.com) - Go 包的成绩单。
- [go.dev](https://go.dev/) - Go 开发者的中心。
- [gocryforhelp](https://github.com/ninedraft/gocryforhelp) - 需要帮助的 Go 项目集合。开始你的 Go 开源之路的好地方。
- [Golang Developer Jobs](https://golangjob.xyz) - 专门针对 Golang 相关角色的开发人员职位。
- [Golang News](https://golangnews.com) - 有关 Go 编程的链接和新闻。
- [Golang Nugget](https://golangnugget.com) - 最佳 Go 内容的每周综述，每周一发送到您的收件箱。
- [Golang Weekly](https://discu.eu/weekly/golang/) - 每个星期一有关 Go 的项目、教程和文章。
- [golang-nuts](https://groups.google.com/forum/#!forum/golang-nuts) - 转到邮件列表。
- [Gopher Community Chat](https://invite.slack.golangbridge.org) - 加入我们新的 Gophers Slack 社区（[了解它是如何产生的](https://blog.gopheracademy.com/gophers-slack-community/)）。
- [Gophercises](https://gophercises.com/) - 为初露头角的地鼠提供免费编码练习。
- [json2go](https://m-zajac.github.io/json2go) - 高级 JSON 到 Go 结构转换 - 在线工具。
- [justforfunc](https://www.youtube.com/c/justforfunc) - 专门介绍 Go 编程语言提示和技巧的 YouTube 频道，由 Francesc Campoy [@francesc](https://twitter.com/francesc) 主持。
- [Learn Go Programming](https://blog.learngoprogramming.com) - 通过插图学习 Go 概念。
- [Libs.tech](https://libs.tech/go) - 很棒的 Go 库和隐藏的宝石
- [用 Golang 制作](https://madewithgolang.com/?ref=awesome-go)
- [pkg.go.dev](https://pkg.go.dev/) - 开源 Go 包的文档。
- [studygolang](https://studygolang.com) - 中国的studygolang社区。
- [Trending Go repositories on GitHub today](https://github.com/trending?l=go) - 寻找新 Go 库的好地方。
- [TutorialEdge - Go 语言](https://tutorialedge.net/course/golang/)

**[⬆ 回到顶部](#contents)**

### 教程

- [50 Shades of Go](https://golang50shades.github.io/) - 新 Golang 开发人员的陷阱、陷阱和常见错误。
- [A Comprehensive Guide to Structured Logging in Go](https://betterstack.com/community/guides/logging/logging-in-go/) - 深入研究 Go 中的结构化日志记录世界，特别关注最近接受的 slog 提案，该提案旨在将具有级别的高性能结构化日志记录引入标准库。
- [A Guide to Golang E-Commerce](https://snipcart.com/blog/golang-ecommerce-ponzu-cms-demo?utm_term=golang-ecommerce-ponzu-cms-demo) - 构建一个用于电子商务的 Golang 网站（包括演示）。
- [A Tour of Go](https://tour.golang.org/) - Go 的互动之旅。
- [Build a Database in 1000 lines of code](https://link.medium.com/O9YQlx89Htb) - 用 1000 行代码从零构建 NoSQL 数据库。
- [Build web application with Golang](https://github.com/astaxie/build-web-application-with-golang) - Golang 电子书介绍了如何使用 golang 构建 Web 应用程序。
- [Building and Testing a REST API in Go with Gorilla Mux and PostgreSQL](https://semaphoreci.com/community/tutorials/building-and-testing-a-rest-api-in-go-with-gorilla-mux-and-postgresql) - 我们将在强大的 Gorilla Mux 的帮助下编写 API。
- [Building Go Web Applications and Microservices Using Gin](https://semaphoreci.com/community/tutorials/building-go-web-applications-and-microservices-using-gin) - 熟悉 Gin 并了解它如何帮助您减少样板代码并构建请求处理管道。
- [Caching Slow Database Queries](https://medium.com/@rocketlaunchr.cloud/caching-slow-database-queries-1085d308a0c9) - 如何缓存缓慢的数据库查询。
- [Canceling MySQL](https://medium.com/@rocketlaunchr.cloud/canceling-mysql-in-go-827ed8f83b30) - 如何取消 MySQL 查询。
- [CodeCrafters Golang Track](https://app.codecrafters.io/tracks/go) - 通过构建自己的 Redis、Docker、Git 和 SQLite 来掌握高级 Go。具有 goroutine、系统编程、文件 I/O 等功能。
- [Design Patterns in Go](https://github.com/shubhamzanwar/design-patterns) - 用 Go 实现的编程设计模式的集合。
- [Games With Go](https://www.youtube.com/watch?v=9D4yH7e_ea8&list=PLDZujg-VgQlZUy1iCqBbe5faZLMkA3g2x) - 教学编程和游戏开发的视频系列。
- [Go By Example](https://gobyexample.com/) - 使用带注释的示例程序实际介绍 Go。
- [Go Cheat Sheet](https://github.com/a8m/go-lang-cheat-sheet) - Go 的参考卡。
- [Go database/sql tutorial](http://go-database-sql.org/) - 数据库/sql 简介。
- [Go in 7 days](https://github.com/harrytran103/7_days_of_go) - 在 7 天内了解有关 Go 的所有内容（来自 Nodejs 开发人员）。
- [Go Language Tutorial](https://www.javatpoint.com/go-tutorial) - 学习Go语言教程。
- [Go Tutorial](https://www.tutorialspoint.com/go/index.htm) - 学习 Go 编程。
- [Go WebAssembly 教程 - 构建一个简单的计算器](https://tutorialedge.net/golang/go-webassembly-tutorial/)
- [go-clean-template](https://github.com/evrone/go-clean-template) - Golang 服务的简洁架构模板。
- [go-patterns](https://github.com/tmrts/go-patterns) - Go 设计模式、配方和习语的精选列表。
- [Golang for Node.js Developers](https://github.com/miguelmota/golang-for-nodejs-developers) - 用于学习的 Golang 与 Node.js 对比示例。
- [Golang Tutorial Guide](https://www.freecodecamp.org/news/golang-tutorial-list-free-courses-learn-go-programming-language/) - 学习 Go 编程语言的免费课程列表。
- [golang-examples](https://github.com/SimonWaldherr/golang-examples) - 很多学习Golang的例子。
- [Golangbot](https://golangbot.com/learn-golang-series/) - Go 编程入门教程。
- [GopherCoding](https://gophercoding.com/) - 代码片段和教程的集合，可帮助解决日常问题。
- [GopherSnippets](https://gophersnippets.com/) - 包含 Go 编程语言测试和可测试示例的代码片段。
- [Gosamples](https://gosamples.dev/) - 可让您解决日常代码问题的代码片段集合。
- [GraphQL with Go](https://hasura.io/learn/graphql/backend-stack/languages/go/) - 了解如何通过代码生成创建 Go GraphQL 服务器和客户端。还包括创建 REST 端点。
- [Hackr.io](https://hackr.io/tutorials/learn-golang) - 从 golang 编程社区提交和投票的最佳在线 golang 教程中学习 Go。
- [Hex Monscape](https://github.com/Haraj-backend/hex-monscape) - 使用六边形架构编写可维护代码的入门指南。
- [How to Benchmark: dbq vs sqlx vs GORM](https://medium.com/@rocketlaunchr.cloud/how-to-benchmark-dbq-vs-sqlx-vs-gorm-e814caacecb5) - 了解如何在 Go 中进行基准测试。作为案例研究，我们将对 dbq、sqlx 和 GORM 进行基准测试。
- [How To Deploy a Go Web Application with Docker](https://semaphoreci.com/community/tutorials/how-to-deploy-a-go-web-application-with-docker) - 了解如何使用 Docker 进行 Go 开发以及如何构建生产 Docker 镜像。
- [How to Implement Role-Based Access Control (RBAC) Authorization in Golang](https://www.permit.io/blog/role-based-access-control-rbac-authorization-in-golang) - 在 Golang 中实现基于角色的访问控制 (RBAC) 的指南，包括代码示例，涵盖使用基于角色的授权来保护应用程序端点的各种方法。
- [How to Use Godog for Behavior-driven Development in Go](https://semaphoreci.com/community/tutorials/how-to-use-godog-for-behavior-driven-development-in-go) - 开始使用 Godog - 一个用于构建和测试 Go 应用程序的行为驱动开发框架。
- [Learn Go with 1000+ Exercises](https://github.com/inancgumus/learngo) - 通过数千个示例、练习和测验来学习 Go。
- [Learn Go with TDD](https://github.com/quii/learn-go-with-tests) - 通过测试驱动开发来学习 Go。
- [Learning Go by examples](https://dev.to/aurelievache/learning-go-by-examples-introduction-448n) - 系列文章以通过具体应用为例学习Golang语言。
- [Microservices with Go](https://www.youtube.com/playlist?list=PLmD8u-IFdreyh6EUfevBcbiuCKzFk0EW_) - 深入研究使用 Go 构建微服务，包括 gRPC。
- [package main](https://www.youtube.com/packagemain) - 关于 Go 编程的 YouTube 频道。
- [Programming with Google Go](https://www.coursera.org/specializations/google-golang) - Coursera 专业化，从头开始学习 Go。
- [Scaling Go Applications](https://betterstack.com/community/guides/scaling-go/) - 有关在生产中构建、部署和扩展 Go 应用程序的所有内容。
- [世界上最简单的 Golang WebAssembly 介绍](https://medium.com/@martinolsansky/webassembly-with-golang-is-fun-b243c0e34f02)
- [Understanding Go in a visual way](https://dev.to/aurelievache/series/26234) - 直观地学习围棋
- [W3basic Go Tutorials](https://www.w3basic.com/golang/) - W3Basic 提供了深入的教程和组织良好的内容来学习 Golang 编程。
- [Your basic Go](https://yourbasic.org/golang) - 大量教程和操作方法的集合。

**[⬆ 回到顶部](#contents)**

### 引导式学习

- [The Go Developer Roadmap](https://roadmap.sh/golang) - 新的 Go 开发人员可以遵循的可视化路线图来帮助他们学习 Go。
- [The Go Interview Practice](https://github.com/RezaSi/go-interview-practice) - 一个 GitHub 存储库，提供 Go 技术面试准备的编码挑战。
- [The Go Learning Path](https://tutorialedge.net/paths/golang/) - 包含免费和优质资源的指导学习路径。
- [The Go Skill Tree](https://labex.io/skilltrees/go) - 结合了免费和优质资源的结构化学习路径。

**[⬆ 回到顶部](#contents)**

## 贡献

我们欢迎贡献！请参阅我们的 [CONTRIBUTING.md](https://github.com/avelino/awesome-go/blob/main/CONTRIBUTING.md) 以获取指南。

## 许可证

该项目已根据 [MIT 许可证](https://github.com/avelino/awesome-go/blob/main/LICENSE) 获得许可 - 有关详细信息，请参阅许可证文件。
