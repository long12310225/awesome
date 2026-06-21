# 很棒的微服务 [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

微服务架构相关原则和技术的精选列表。

**目录**

- [Platforms](#platforms)
- [框架/运行时](#frameworks--runtimes)
- [服务工具包](#service-toolkits)
  - [Polyglot](#polyglot)
  - [C](#c)
  - [C++](#c-1)
  - [C#](#csharp)
  - [D](#d)
  - [Erlang虚拟机](#erlang-vm)
  - [Go](#go)
  - [Haskell](#haskell)
  - [Java虚拟机](#java-vm)
  - [Node.js](#nodejs)
  - [Perl](#perl)
  - [PHP](#php)
  - [Python](#python)
  - [Ruby](#ruby)
  - [Rust](#rust)
- [前端/用户界面](#frontend--ui)
- [Capabilities](#capabilities)
  - [API 网关/边缘服务](#api-gateways--edge-services)
  - [配置与发现](#configuration--discovery)
  - [工作流程编排](#workflow-orchestration)
  - [Elasticity](#elasticity)
  - [作业调度程序/工作负载自动化](#job-schedulers--workload-automation)
  - [Logging](#logging)
  - [Messaging](#messaging)
  - [监控与调试](#monitoring--debugging)
  - [Reactivity](#reactivity)
  - [Resilience](#resilience)
  - [Security](#security)
  - [Serialization](#serialization)
  - [Storage](#storage)
  - [Testing](#testing)
- [持续集成和交付](#continuous-integration--delivery)
- [Web API 建模和文档](#web-api-modeling--documentation)
  - [Async](#async)
  - [GraphQL](#graphql)
  - [JSON](#json)
  - [REST](#rest)
- [标准/建议](#standards--recommendations)
  - [万维网](#world-wide-web)
  - [自我主权和权力下放](#self-sovereignty--decentralisation)
  - [HTTP/1.1](#http11)
  - [HTTP/2](#http2)
  - [QUIC](#quic)
  - [RPC](#rpc)
  - [Messaging](#messaging-1)
  - [Security](#security-1)
  - [服务发现](#service-discovery)
  - [数据格式](#data-formats)
  - [Vocabularies](#vocabularies)
  - [Unicode](#unicode)
- [组织设计/团队动力](#organization-design--team-dynamics)
- [企业与垂直行业](#enterprise--verticals)
- [Theory](#theory)
  - [文章与论文](#articles--papers)
  - [站点和组织](#sites--organizations)
- [License](#license)
- [Contributing](#contributing)

## 平台

- [1Backend](https://github.com/1backend/1backend) - AI原生微服务平台。
- [Jolie](https://jolie-lang.org) - 面向微服务的开源编程语言。
- [OpenWhisk](https://github.com/apache/openwhisk) - 无服务器开源云平台，执行功能以响应任何规模的事件。
- [Pulumi](https://pulumi.io/) - 用于云原生基础设施即代码的 SDK。使用您最喜欢的语言预览和管理应用程序和基础设施的更新，并持续部署到任何云（无需 YAML）。
- [Triton](https://github.com/joyent/triton) - 开源云管理平台，跨一个或多个数据中心提供下一代、基于容器、面向服务的基础设施。

## 框架/运行时

- [Akka](http://akka.io/) - 用于在 JVM 上构建高度并发、分布式和弹性的消息驱动应用程序的工具包和运行时。
- [Axon (c)](https://axoniq.io/) - 一个端到端的开发和基础设施平台，可在 JVM 上轻松开发和运行任何 DDD、CQRS 和事件源应用程序。
- [Ballerina](https://ballerina.io) - 云原生编程语言。
- [Bun](https://bun.sh/) - 快速的一体化 JavaScript 运行时。
- [Dapr](https://dapr.io) - 用于使用任何编程语言编写高性能微服务的开源运行时。
- [Deno](https://deno.land/) - JavaScript、TypeScript 和 WebAssembly 运行时具有安全的默认设置和出色的开发人员体验。
- [Eclipse Microprofile](https://microprofile.io/) - 一个开放论坛，通过跨多种实现进行创新并在共同感兴趣的领域进行协作以实现标准化，从而优化微服务架构的 Enterprise Java。
- [Erlang/OTP](https://github.com/erlang/otp) - 用于构建具有高可用性要求的大规模可扩展软实时系统的编程语言。
- [Finagle](http://twitter.github.io/finagle) - JVM可扩展的RPC系统，用于构建高并发服务器。
- [Gleam](https://gleam.run/) - 一种用于构建类型安全、可扩展系统的友好语言。
- [GraalVM](https://www.graalvm.org/) - 高性能运行时可显着提高应用程序性能和效率，是微服务的理想选择。
- [Helidon](https://helidon.io/) - 用于编写在由 Netty 提供支持的快速 Web 核心上运行的微服务的 Java 库集合。
- [Ice](https://github.com/zeroc-ice/ice) - 全面的 RPC 框架，支持 C++、C#、Java、JavaScript、Python 等。
- [Light-4j](https://github.com/networknt/light-4j) - 高吞吐量、低延迟、内存占用小且生产力更高的微服务平台。
- [Micronaut](http://micronaut.io/) - 一个基于 JVM 的现代全栈框架，用于构建模块化、易于测试的微服务应用程序。
- [Moleculer](http://moleculer.services/) - 适用于 Node.js、Java、Go 和 Ruby 的快速且强大的微服务框架。
- [Open Liberty](https://openliberty.io/) - 一个轻量级的开放框架，用于构建快速高效的云原生 Java 微服务。
- [Pears](https://github.com/holepunchto/pear) - 点对点运行时、开发和部署。
- [SmallRye](https://smallrye.io/) - 专为云开发量身定制的 API 和实现，包括 Eclipse MicroProfile。
- [Spin](https://github.com/fermyon/spin) - 一个开源框架，用于使用 WebAssembly 构建和运行快速、安全且可组合的云微服务。
- [ScaleCube](https://github.com/scalecube/scalecube) - 用于为 JVM 构建反应式微服务的工具包：低延迟、高吞吐量、可扩展且有弹性。
- [Vert.X](http://vertx.io/) - 用于在 JVM 上构建反应式应用程序的工具包。
- [Vert.X Toolbox](https://github.com/vert-x3/vertx-microservices-toolbox) - 一组用于构建反应式微服务应用程序的 Vert.x 组件。
- [Wangle](https://github.com/facebook/wangle) - 一个框架，提供一组通用的客户端/服务器抽象，用于以一致、模块化和可组合的方式构建服务。

## 服务工具包

### 多语言

- [GRPC](http://www.grpc.io/) - 一个高性能、开源、通用的 RPC 框架，将移动和 HTTP/2 放在首位。 C、C++、Java、Go、Node.js、Python、Ruby、Objective-C、PHP 和 C# 库。

### C

- [Lwan](http://lwan.ws/) - 高性能且可扩展的 Web 服务器。
- [uSockets](https://github.com/uNetworking/uSockets) - 用于异步应用程序的小型跨平台事件、网络和加密。

### C++
<!-- #c-1 anchor -->

- [Cap’n Proto RPC](https://capnproto.org/cxxrpc.html) - Cap’n Proto C++ RPC 实现。
- [C++ Micro Services](https://github.com/CppMicroServices/CppMicroServices) - 类似 OSGi 的 C++ 动态模块系统和服务注册表。
- [Enduro/X](https://github.com/endurox-dev/endurox/) - 适用于 GNU/Linux 的基于 XATMI 的服务框架。
- [Pistache](https://github.com/oktal/pistache) - 用 C++ 编写的高性能 REST 工具包。
- [Poco](http://pocoproject.org/) - 用于构建基于网络的应用程序和服务器的 C++ 类库。
- [Sogou Workflow](https://github.com/sogou/workflow) - 企业级编程引擎，旨在满足大部分后端开发需求。
- [uWebSockets](https://github.com/uNetworking/uWebSockets) - 简单、安全且符合标准的 Web 服务器，适合最苛刻的应用程序。

### 夏普

- [Awesome Microservices .NET Core](https://github.com/mjebrahimi/Awesome-Microservices-NetCore) :star: - .NET Core 中微服务的精彩培训系列、文章、视频、书籍、课程、示例项目和工具的集合。

### D

- [Vibe.d](http://vibed.org/) - 异步 I/O，不会妨碍您，用 D 编写。

### Erlang虚拟机

#### 灵丹妙药

- [Phoenix](http://www.phoenixframework.org/) - 用于构建 HTML5 应用程序、API 后端和分布式系统的框架。
- [Plug](https://github.com/elixir-lang/plug) - Web 应用程序之间可组合模块的规范和便利性。

#### 埃尔兰

- [Cowboy](https://github.com/ninenines/cowboy) - 用 Erlang 编写的小型、快速、模块化 HTTP 服务器。
- [Mochiweb](https://github.com/mochi/mochiweb) - 用于构建轻量级 HTTP 服务器的 Erlang 库。

### 去

- [Chi](https://github.com/go-chi/chi) - 用于构建 Go HTTP 服务的轻量级、惯用且可组合的路由器。
- [Echo](https://echo.labstack.com/) - 快速且简单的 Go HTTP 服务器框架。比其他产品快 10 倍。
- [Fiber](https://github.com/gofiber/fiber) - Express 启发的 Web 框架构建在 Fasthttp 之上，Fasthttp 是 Go 最快的 HTTP 引擎。旨在简化快速开发过程，同时考虑到零内存分配和性能。
- [Gin](https://github.com/gin-gonic/gin) - Gin 是一个用 Go (Golang) 编写的 HTTP Web 框架。它具有类似 Martini 的 API，性能更好，速度提高了 40 倍。
- [Goa](https://github.com/goadesign/goa) - Go 中基于设计的 HTTP 微服务。
- [GoFr](https://github.com/gofr-dev/gofr) - 一个固执己见的微服务开发框架，强调可扩展性和鲁棒性。旨在简化微服务的开发。
- [Go Chassis](https://github.com/go-chassis/go-chassis) - 一个用Go语言快速开发微服务的框架，很容易与一些云生态系统集成。
- [Go-micro](https://github.com/micro/go-micro) - 分布式系统开发框架。
- [Go-zero](https://github.com/tal-tech/go-zero) - 一个Web和rpc分布式系统开发框架。
- [Gorilla](http://www.gorillatoolkit.org/) - Go 编程语言的 Web 工具包。
- [Iris](https://github.com/kataras/iris) - 快速、简单且高效的 Go 微型 Web 框架。
- [Lura](https://github.com/luraproject/lura) - 使用中间件构建超性能 API 网关的框架。
- [RPCX](https://github.com/smallnest/rpcx) - 类似阿里巴巴Dubbo、微博Motan等基于NET/RPC的分布式RPC服务框架。

### 哈斯克尔

- [Scotty](https://github.com/scotty-web/scotty) - 受 Ruby 的 Sinatra 启发的微型 Web 框架，使用 WAI 和 Warp。
- [Servant](https://github.com/haskell-servant/servant) - 类型级 Web DSL。
- [Yesod](https://github.com/yesodweb/yesod) - Haskell RESTful Web 框架。

### Java虚拟机

#### 克洛尤尔

- [Compojure](https://github.com/weavejester/compojure) - 用于 Ring/Clojure 的简洁路由库。
- [Duct](https://duct-framework.org/) - Clojure 的服务器端框架。
- [System](https://github.com/danielsz/system) - 构建在 Stuart Sierra 的组件库之上，提供了一组现成的组件。
- [Tesla](https://github.com/otto-de/tesla-microservice) - Otto.de 的一些 Clojure 微服务的共同基础。

#### 爪哇

- [ActiveJ](https://github.com/activej/activej) - 用于复杂高负载分布式应用程序和类似 Memcached 的解决方案的轻量级快速库。
- [Airlift](https://github.com/airlift/airlift) - 用 Java 构建 REST 服务的框架。
- [Armeria](https://line.github.io/armeria/) - 基于 Java 8、Netty、Thrift 和 gRPC 构建的开源异步 HTTP/2 RPC/REST 客户端/服务器库。
- [Disruptor](https://github.com/LMAX-Exchange/disruptor) - 高性能线程间消息传递库。
- [Dropwizard](https://github.com/dropwizard/dropwizard) - 用于开发操作友好、高性能、RESTful Web 服务的 Java 框架。
- [Dubbo](https://github.com/apache/dubbo) - 阿里巴巴开源的一个基于java的高性能RPC框架。
- [Conjure](https://github.com/palantir/conjure-java-runtime) - 用于定义和创建 RESTish/RPC 服务器和客户端的自定义库集，基于 Feign 或 Retrofit 作为客户端，以 Dropwizard/Jersey 和 JAX-RS 服务定义作为服务器。
- [Jersey](https://github.com/eclipse-ee4j/jersey) - Java 中的 RESTful 服务。 JAX-RS 参考实现。
- [Quarkus](https://quarkus.io/) - 专为 OpenJDK HotSpot 和 GraalVM 量身定制的 Kubernetes Native Java 堆栈，采用最佳 Java 库和标准精心打造。
- [Ratpack](https://ratpack.io/) - 一组 Java 库，可促进快速、高效、可演进且经过良好测试的 HTTP 应用程序。提供了对 Groovy 语言的特定支持。
- [Spring Boot](http://projects.spring.io/spring-boot/) - 可以轻松创建独立的、生产级的基于 Spring 的应用程序。

#### 科特林

- [Http4k](https://www.http4k.org/) - 用纯 Kotlin 编写的轻量级但功能齐全的 HTTP 工具包，能够以功能一致的方式提供和使用 HTTP 服务。
- [Ktor](https://ktor.io/) - 使用 Kotlin 编程语言在互联系统中构建异步服务器和客户端的框架。

#### 斯卡拉

- [Finatra](http://twitter.github.io/finatra/) - 基于 Twitter-Server 和 Finagle 构建的快速、可测试的 Scala HTTP 服务。
- [Http4s](http://http4s.org/) - 一个最小的、惯用的 HTTP 的 Scala 接口
- [Play](https://www.playframework.com/) - 适用于 Java 和 Scala 的高速 Web 框架。

### Node.js

- [Actionhero](http://www.actionherojs.com/) - 具有集成集群功能和延迟任务的多传输 Node.js API 服务器。
- [Express](http://expressjs.com/) - 适用于 Node.js 的快速、无主见、简约的 Web 框架
- [Fastify](https://www.fastify.io/) - Fastify，快速且低开销的 Web 框架，适用于 Node.js。
- [FeathersJS](http://feathersjs.com/) - 适用于现代应用程序的开源 REST 和实时 API 层。
- [Hono](https://hono.dev/) - 适用于边缘的小型、简单且超快的 Web 框架。它适用于任何 JavaScript 运行时。
- [Koa](http://koajs.com/) - Node.js 的下一代 Web 框架
- [Loopback](http://loopback.io/) - Node.js 框架，用于创建 API 并轻松连接到后端数据源。
- [NestJS](https://docs.nestjs.com/) - Node.js 框架，用于构建具有内置微服务支持的高效且可扩展的服务器端应用程序。
- [Seneca](https://github.com/senecajs/seneca) - Node.js 的微服务工具包
- [Serverless](https://github.com/serverless/serverless) - 构建和维护在 AWS Lambda 和 API Gateway（以前称为 JAWS）上运行的 Web、移动和 IoT 应用程序。
- [tRPC](https://github.com/trpc/trpc) - 端到端类型安全 API。

### 珀尔

- [Cro](http://cro.services/) - 使用 Perl 6 创建反应式分布式系统的库。
- [Mojolicious](https://mojolicious.org/) - Perl 的下一代 Web 框架。

### PHP

- [API Platform](https://api-platform.com/) - 基于 Symfony 的 API 优先 Web 框架，支持 JSON-LD、Schema.org 和 Hydra。
- [Ecotone](https://docs.ecotone.tech/) - 基于 DDD、CQRS 和事件源架构原则的框架，提供构建块来创建可扩展和可扩展的应用程序。
- [Hyperf](https://github.com/hyperf/hyperf) - Hyperf 是一个基于 Swoole 4.5+ 的高性能且灵活的 PHP CLI 框架，由最先进的协程服务器和大量经过实战考验的组件提供支持。
- [Lumen](https://lumen.laravel.com/) - 速度惊人的微框架。
- [Slim](http://www.slimframework.com/) - 微框架可帮助您快速编写简单但功能强大的 Web 应用程序和 API。
- [Spiral](https://spiral.dev/) - 使用 [RoadRunner](https://roadrunner.dev/) 为长时间运行的应用程序设计的框架。它提供了高级功能，例如与 [Temporal](https://temporal.io/) 工作流引擎和 [Centrifugo](https://centrifugal.dev/) websocket 服务器集成。它对于微服务架构特别有效，为 REST API 和 gRPC 服务提供强大的支持。
- [Swoft](https://github.com/swoft-cloud/swoft/) - PHP 微服务协程框架，用于构建高性能 Web 系统、API、中间件和基础服务。
- [Symfony](https://symfony.com/) - 基于 Symfony 组件的微框架。

### 蟒蛇

- [Aiohttp](https://github.com/aio-libs/aiohttp) - asyncio 的 HTTP 客户端/服务器。
- [Bottle](https://bottlepy.org) - 适用于 Python 的快速、简单且轻量级的 WSGI 微型 Web 框架。
- [Connexion](https://github.com/zalando/connexion) - 基于 Flask 的 Python Swagger/OpenAPI 框架，具有自动端点验证和 OAuth2 支持。
- [Falcon](https://falconframework.org/) - 用于构建非常快速的应用程序后端和微服务的裸机 Python Web API 框架。
- [FastAPI](https://fastapi.tiangolo.com/) - 现代、快速（高性能）的 Web 框架，用于基于标准 Python 类型提示使用 Python 3.6+ 构建 API。
- [Flask](http://flask.pocoo.org/) - 基于 Werkzeug 和 Jinja 2 的微服务 Python 框架。
- [Nameko](https://github.com/onefinestay/nameko) - 用于构建微服务的 Python 框架。
- [Sanic](https://github.com/sanic-org/sanic) - Sanic 是一个类似 Flask 的 Python 3.5+ Web 服务器，旨在快速运行。
- [Tornado](http://www.tornadoweb.org/) - Web 框架和异步网络库。
- [Twisted](https://twisted.org/) - 事件驱动的网络编程引擎。
- [Web.py](https://github.com/webpy/webpy/) - Python 的极简 Web 框架。

### 红宝石

- [Grape](https://github.com/ruby-grape/grape) - 用于创建类似 REST 的 API 的固执己见的框架
- [Hanami](https://github.com/hanami) - Ruby 的现代 Web 框架。
- [Praxis](https://github.com/rightscale/praxis) - 用于设计和实现 API 的框架。
- [Scorched](https://github.com/wardrop/Scorched) - 用于 Ruby 的轻量级 Web 框架。
- [Sinatra](http://www.sinatrarb.com/) - Sinatra 是一种 DSL，用于以最少的工作在 Ruby 中快速创建 Web 应用程序。

### 铁锈

- [我们已经实现 Web 了吗？](https://www.arewewebyet.org/) :star: - Rust 中 Web 编程现状的总结。
- [Actix](https://actix.rs/) - 强大、实用且速度极快的 Rust Web 框架。
- [Tarpc](https://github.com/google/tarpc) - Rust 的 RPC 框架，注重易用性。
- [Tokio](https://tokio.rs) - 用于编写网络应用程序的异步运行时。
- [Tower](https://github.com/tower-rs/tower) - 用于构建强大的网络客户端和服务器的模块化和可重用组件库。
- [Wtx](https://github.com/c410-f3r/wtx) - HTTP/2 客户端/服务器框架。

## 前端/用户界面

- [Awesome Micro Frontends](https://github.com/ChristianUlbrich/awesome-microfrontends) :star: - 有关微前端的精选资源列表。
- [Electrode](https://github.com/electrode-io) - 通用 React/Node.js 应用程序平台。
- [Micro Frontends](https://micro-frontends.org) - 将微服务思想扩展到前端开发。
- [MiniApp White Paper](https://w3c.github.io/miniapp/white-paper/) - MiniApp标准化白皮书。

## 能力

### API 网关/边缘服务

> 请注意，[数据和控制平面](https://blog.envoyproxy.io/service-mesh-data-plane-vs-control-plane-2774e720f7fc)组件目前尚未分类。

- [Ambassador (c)](https://www.getambassador.io) - 用于基于 Envoy 构建的微服务的 Kubernetes 原生 API 网关。
- [APIcast](https://github.com/3scale/APIcast) - APIcast 是一个构建在 NGINX 之上的 API 网关。它是红帽 3scale API 管理平台的一部分。
- [Bunker Web](https://github.com/bunkerity/bunkerweb) - 默认情况下，Web 应用程序托管和反向代理是安全的。
- [Caddy](https://caddyserver.com/) - 具有自动 HTTPS 功能的可扩展 HTTP/2 Web 服务器。
- [Camel](http://camel.apache.org/) - 使您能够使用各种特定于域的语言定义路由和中介规则，包括基于 Java 的流畅 API、Spring 或 Blueprint XML 配置文件以及 Scala DSL。
- [Envoy](https://github.com/lyft/envoy) - 来自 Lyft 开发人员的开源边缘和服务代理。
- [HAProxy](https://github.com/haproxy/haproxy) - 可靠、高性能 TCP/HTTP 负载平衡器。
- [Istio](https://istio.io/) - 用于连接、管理和保护微服务的开放平台。
- [Keepalived](http://www.keepalived.org/) - 简单而强大的工具，用于 Linux 系统和基于 Linux 的基础设施的负载平衡和高可用性。
- [Kong](https://github.com/kong/kong) - API 的开源管理层。
- [KrakenD](http://krakend.io/) - 开源超高性能 API 网关。
- [Kuma](https://kuma.io/) - 用于服务网格和微服务的平台无关的开源控制平面。
- [Linkerd](https://linkerd.io/) - 适用于云原生应用程序的弹性服务网格。
- [Neutrino](https://github.com/eBay/Neutrino) - 可扩展的软件负载平衡器。
- [OpenResty](http://openresty.org/) - 构建在 Nginx 之上的快速 Web 应用程序服务器。
- [Open Service Mesh](https://openservicemesh.io/) - 轻量级且可扩展的云原生服务网格。
- [Otoroshi](https://www.otoroshi.io/) - 具有轻量级 API 管理的现代 HTTP 反向代理。
- [Pingora](https://github.com/cloudflare/pingora) - 用于构建快速、可靠和可发展的网络服务的库。
- [Skipper](https://github.com/zalando/skipper) - HTTP 路由器对于将路由与服务逻辑解耦很有用。
- [Spring Cloud Gateway](https://cloud.spring.io/spring-cloud-gateway/) - Spring MVC 之上的 API 网关。旨在提供一种简单而有效的方法来路由到 API。
- [Tengine](http://tengine.taobao.org/) - 具有一些高级功能的 Nginx 发行版。
- [Træfɪk](http://traefik.io/) - 现代 HTTP 反向代理和负载均衡器，可轻松部署微服务。
- [Traffic Server](https://github.com/apache/trafficserver) - 云服务的高性能构建块。
- [Tyk](https://tyk.io/) - 开源、快速且可扩展的 API 网关、门户和 API 管理平台。
- [Vulcand](https://github.com/vulcand/vulcand) - 由 Etcd 支持的编程负载均衡器。
- [Zuul](https://github.com/Netflix/zuul) - 提供动态路由、监控、弹性、安全性等的边缘服务。

### 配置与发现

- [Central Dogma](https://line.github.io/centraldogma/) - 基于Git、ZooKeeper和HTTP/2的开源高可用版本控制服务配置存储库。
- [Consul](https://www.consul.io/) - 服务发现和配置变得简单。分布式、高可用性和数据中心感知。
- [Etcd](https://github.com/coreos/etcd) - 用于共享配置和服务发现的高可用键值存储。
- [Eureka](https://github.com/Netflix/eureka/wiki/Eureka-at-a-glance) - 基于 REST 的服务，主要在 AWS 云中用于定位服务，以实现中间层服务器的负载平衡和故障转移。
- [Microconfig](https://microconfig.io) - 现代而简单的微服务配置管理方式。
- [Nacos](https://github.com/alibaba/nacos) - 易于使用的动态服务发现、配置和服务管理平台。
- [SkyDNS](https://github.com/skynetservices/skydns) - 用于公告和发现建立在 etcd 之上的服务的分布式服务。它利用 DNS 查询来发现可用的服务。
- [Spring Cloud Config](http://cloud.spring.io/spring-cloud-config/) - 为分布式系统中的外部化配置提供服务器和客户端支持。
- [ZooKeeper](https://zookeeper.apache.org/) - 开源服务器，可实现高度可靠的分布式协调。

### 工作流程编排

- [AWS Step Functions (c)](https://aws.amazon.com/step-functions/) - 使用可视化工作流程协调分布式应用程序和微服务的组件。
- [Cadence](https://cadenceworkflow.io/) - 无故障状态代码平台。
- [Conductor](https://github.com/Netflix/conductor) - 微服务编排引擎。
- [Inngest](https://github.com/inngest/inngest) - 耐用的功能可实现可靠的后台逻辑，从后台作业到复杂的工作流程。
- [Kestra](https://github.com/kestra-io/kestra) - 开源微服务事件驱动、与语言无关的编排和调度平台。
- [Temporal](https://github.com/temporalio/temporal) - 用于运行任何规模的关键任务代码的开源微服务编排平台。
- [Zeebe](https://camunda.com/platform/zeebe/) - 跨微服务定义、编排和监控业务流程。

### 弹性

- [Hazelcast](http://hazelcast.org/) - 开源内存数据网格。允许您跨服务器、集群和地理位置分布数据和计算，并管理非常大的数据集或高数据摄取率。技术成熟。
- [Helix](http://helix.apache.org/) - 通用集群管理框架，用于自动管理节点集群上托管的分区、复制和分布式资源。
- [Ignite](http://ignite.apache.org/) - 高性能、集成和分布式内存平台，用于实时计算和处理大规模数据集，比传统的基于磁盘或闪存技术快几个数量级。
- [Libp2p](https://libp2p.io/) - 用于构建对等网络应用程序的框架和协议套件。
- [Mesos](https://mesos.apache.org/) - 将 CPU、内存、存储和其他计算资源从机器（物理或虚拟）中抽象出来，使容错和弹性的分布式系统能够轻松构建和有效运行。
- [Nomad](https://www.nomadproject.io/) - 分布式、高可用、数据中心感知的调度程序。
- [Redisson](https://github.com/mrniko/redisson) - Redis 服务器之上的分布式且可扩展的 Java 数据结构。
- [Serf](https://www.serf.io/) - 用于集群成员资格、故障检测和编排的去中心化解决方案。
- [Valkey](https://github.com/valkey-io/valkey) - 一个新项目，在以前的开源 Redis 项目的基础上恢复开发。
- [Zenoh](https://zenoh.io/) - 发布/订阅/查询协议统一动态数据、静态数据和计算。将传统的发布/订阅与地理分布式存储、查询和计算有效地融合在一起。

### 作业调度程序/工作负载自动化

- [Celery](https://github.com/celery/celery) - 基于分布式消息传递的异步任务队列/作业队列。注重实时运行，支持调度。
- [Dkron](http://dkron.io/) - 分布式、容错作业调度系统。
- [Faktory](https://github.com/contribsys/faktory) - 与语言无关的持久后台作业服务器。
- [Rundeck (c)](http://rundeck.org/) - 作业调度程序和运行手册自动化。启用对现有脚本和工具的自助访问。
- [Schedulix](https://github.com/schedulix/schedulix) - 开源企业作业调度系统为先进系统环境中 IT 流程的专业自动化制定了突破性标准。

### 记录

- [Fluentd](http://www.fluentd.org/) - 用于统一日志记录层的开源数据收集器。
- [Graylog](https://www.graylog.org/) - 完全集成的开源日志管理平台。
- [Kibana](https://www.elastic.co/products/kibana) - 灵活的分析和可视化平台。
- [LogDNA (c)](https://logdna.com/) - 集中式日志管理软件。从任何平台实时收集、集中和分析任何数量的日志。
- [Logstash](https://www.elastic.co/logstash) - 用于管理事件和日志的工具。
- [Loki](https://github.com/grafana/loki) - 就像普罗米修斯一样，但是用于日志。

### 消息传递

- [ØMQ](http://zeromq.org/) - 无代理智能传输层。
- [ActiveMQ](http://activemq.apache.org/) - 强大的开源消息传递和集成模式服务器。
- [Aeron](https://github.com/real-logic/Aeron) - 高效可靠的 UDP 单播、UDP 组播和 IPC 消息传输。
- [Beanstalk](https://beanstalkd.github.io/) - 简单、快速的工作队列。
- [Bull](https://github.com/OptimalBits/bull) - 用于 Node.js 的快速可靠的基于 Redis 的队列。
- [Crossbar](https://github.com/crossbario/crossbar) - 适用于分布式和微服务应用程序的开源网络平台。它实现了开放的 Web 应用程序消息传递协议 (WAMP)。
- [Kafka](http://kafka.apache.org/) - 发布-订阅消息传递被重新考虑为分布式提交日志。
- [Malamute](https://github.com/zeromq/malamute) - ZeroMQ 企业消息代理。
- [Mosquitto](http://mosquitto.org/) - 实现 MQTT 协议的开源消息代理。
- [NATS](https://nats.io/) - 开源、高性能、轻量级云消息系统。
- [NSQ](http://nsq.io/) - 实时分布式消息平台。
- [Pulsar](https://pulsar.apache.org/) - 分布式发布-订阅消息系统。
- [RabbitMQ](https://www.rabbitmq.com/) - 基于 Erlang 的开源消息代理可以正常工作。
- [Redpanda](https://github.com/redpanda-data/redpanda/) - 面向开发人员的流数据平台：兼容 Kafka API、速度提高 10 倍、无 ZooKeeper 和 JVM。
- [RocketMQ](https://github.com/apache/incubator-rocketmq) - 诞生于阿里巴巴海量消息业务的低延迟、可靠、可扩展、易用的消息中间件。

### 监控与调试

- [Beats](https://www.elastic.co/beats/) - Elasticsearch 和 Logstash 的轻量级托运人。
- [Elastalert](https://github.com/yelp/elastalert) - 简单灵活的 Elasticsearch 警报。
- [Ganglia](http://ganglia.info/) - 用于集群和网格等高性能计算系统的可扩展分布式监控系统。
- [Grafana](http://grafana.org/) - 适用于 Graphite、InfluxDB 和 OpenTSDB 的开源、功能丰富的指标仪表板和图形编辑器。
- [Graphite](http://graphite.wikidot.com/) - 可扩展的实时绘图。
- [IOpipe (c)](https://www.iopipe.com/) - Amazon Lambda 的应用程序性能监控。
- [Jaeger](https://www.jaegertracing.io/) - 开源的端到端分布式跟踪
- [OpenTelemetry](https://opentelemetry.io/) - 高质量、无处不在的便携式遥测技术可实现有效的观测。
- [Prometheus](http://prometheus.io/) - 开源的服务监控系统和时间序列数据库。
- [Riemann](http://riemann.io/) - 监控分布式系统。
- [Sensu](https://github.com/sensu) - 监控当今的基础设施。
- [SkyWalking](https://skywalking.apache.org/) - 适用于分布式系统的应用程序性能监控工具，专为微服务、云原生和基于容器（Docker、K8s、Mesos）架构而设计。
- [Zabbix](http://www.zabbix.com/) - 开源企业级监控解决方案。
- [Zipkin](http://zipkin.io) - 分布式追踪系统。

### 反应性

- [Reactor.io](https://github.com/reactor) - 第二代响应式库，用于基于响应式流规范在 JVM 上构建非阻塞应用程序。
- [Reactive Kafka](https://github.com/akka/alpakka-kafka) - Apache Kafka 的反应式流 API。
- [ReactiveX](http://reactivex.io/) - 用于使用可观察流进行异步编程的 API。适用于惯用的 Java、Scala、C#、C++、Clojure、JavaScript、Python、Groovy、JRuby 等。
- [RSocket](https://rsocket.io/) - 提供反应式流语义的应用程序协议。

### 韧性

- [很棒的混沌工程](https://github.com/dastergon/awesome-chaos-engineering) :star: - 很棒的混沌工程资源的精选列表。
- [Raft Consensus](https://raft.github.io/) - 旨在易于理解的共识算法。它在容错性和性能上与Paxos相当。
- [Resilience4j](https://github.com/resilience4j/resilience4j) - 专为 Java8 和函数式编程设计的容错库。
- [Svix](https://svix.com) - Webhooks 服务，将具有完整重试计划、指数退避、签名验证和事件类型的 Webhooks 发送给您的用户。

### 安全性

- [Cerbos Hub](https://www.cerbos.dev/product-cerbos-hub) - 用于编写、测试和部署访问策略的授权管理系统。在微服务架构中构建可扩展、细粒度的授权。
- [Dex](https://github.com/coreos/dex) - 具有可插拔连接器的固定授权/目录服务。 OpenID Connect 提供商和第三方 OAuth 2.0 委托。
- [JWT](http://jwt.io/) - JSON Web 令牌是一种开放的行业标准 RFC 7519 方法，用于在两方之间安全地表示声明。
- [Keycloak](https://github.com/keycloak/keycloak) - 功能齐全且可扩展的身份验证服务。 OpenID Connect 提供商和第三方 OAuth 2.0 委托。
- [OAuth](http://oauth.net/2/) - 为 Web 应用程序、桌面应用程序、移动电话和客厅设备提供特定的授权流程。许多实现。
- [OpenID Connect](https://openid.net/certified-open-id-developer-tools/) - 实现当前 OpenID 规范和相关规范的库、产品和工具。
- [Open Ziti](https://openziti.io/) - 零信任安全和覆盖网络作为纯开源软件。
- [ORY](https://www.ory.sh/) - 开源身份基础设施和服务。
- [OWASP Agent Memory Guard](https://github.com/OWASP/www-project-agent-memory-guard) - AI 代理内存中毒的运行时防御层 (OWASP ASI06)。检测内存条目被篡改、内存路径中的提示注入以及秘密泄漏。 YAML 策略、微秒延迟、零外部依赖。
- [SCIM](https://simplecloud.info/) - 跨域身份管理系统。
- [Vault](https://www.vaultproject.io/) - 保护、存储和严格控制对现代计算中的令牌、密码、证书、API 密钥和其他机密的访问。

### 序列化

- [Avro](https://avro.apache.org/) - Apache 数据序列化系统以紧凑、快速、二进制数据格式提供丰富的数据结构。
- [Bond](https://github.com/microsoft/bond/) - 用于处理模式化数据的跨平台框架，在 Microsoft 的大规模服务中广泛使用。
- [BooPickle](https://github.com/ochrons/boopickle) - 用于高效网络通信的二进制序列化库。对于 Scala 和 Scala.js
- [Cap’n Proto](https://capnproto.org/) - 极其快速的数据交换格式和基于功能的 RPC 系统。
- [CBOR](http://cbor.io/) - 以多种语言实现 CBOR 标准 (RFC 7049)。
- [Cereal](http://uscilab.github.io/cereal/) - 用于序列化的 C++11 库。
- [Cheshire](https://github.com/dakrone/cheshire) - Clojure JSON 和 JSON SMILE 编码/解码。
- [Etch](http://etch.apache.org/) - 用于构建和使用网络服务的跨平台、语言和传输无关的框架。
- [Fastjson](https://github.com/alibaba/fastjson) - 快速 JSON 处理器。
- [Ffjson](https://github.com/pquerna/ffjson) - Go 的更快 JSON 序列化。
- [FST](https://github.com/RuedigerMoeller/fast-serialization) - 快速 Java 序列化下降了替换。
- [Jackson](https://github.com/FasterXML/jackson) - 用于处理 JSON 数据格式的多用途 Java 库。
- [Jackson Afterburner](https://github.com/FasterXML/jackson-module-afterburner) - Jackson 模块使用字节码生成来进一步加速数据绑定（序列化、反序列化吞吐量增加 30-40%）。
- [Kryo](https://github.com/EsotericSoftware/kryo) - Java序列化和克隆：快速、高效、自动。
- [Lite³](https://github.com/fastserial/lite3) - JSON 兼容的零拷贝序列化格式。
- [MessagePack](http://msgpack.org/) - 高效的二进制序列化格式。
- [Protostuff](https://github.com/protostuff/protostuff) - 一个序列化库，内置对向前向后兼容性（架构演化）和验证的支持。
- [SBinary](https://github.com/harrah/sbinary) - 用于描述 Scala 类型的二进制格式的库。
- [Thrift](http://thrift.apache.org/) - Apache Thrift 软件框架，用于可扩展的跨语言服务开发。
- [yyjson](https://github.com/ibireme/yyjson) - C 语言中最快的 JSON 库。

### 存储

- [Alluxio](https://github.com/Alluxio/alluxio) - 虚拟分布式存储系统。
- [Apache Cassandra](http://cassandra.apache.org) - 面向列并提供高可用性，无单点故障。
- [Aerospike (c)](http://www.aerospike.com/) - 高性能 NoSQL 数据库可大规模提供速度。
- [ArangoDB](https://www.arangodb.com/) - 分布式免费开源数据库，具有灵活的文档、图形和键值数据模型。
- [AtlasDB](https://github.com/palantir/atlasdb) - 键值存储之上的事务层。
- [Citus](https://github.com/citusdata/citus) - 分布式 PostgreSQL 作为扩展。
- [CockroachDB (c)](https://www.cockroachlabs.com/) - 模仿 Google Spanner 的云原生 SQL 数据库。
- [Couchbase](https://github.com/couchbase) - 专为提高性能、可扩展性和简化管理而设计的分布式数据库。
- [Crate (c)](https://crate.io/) - 具有 NoSQL 功能的可扩展 SQL 数据库。
- [Datomic](http://www.datomic.com/) - 完全事务性、云就绪、分布式数据库。
- [Druid](http://druid.io/) - 快速的面向列的分布式数据存储。
- [Elasticsearch](https://www.elastic.co/elasticsearch) - 开源分布式、可扩展且高度可用的搜索服务器。
- [Geode](http://geode.incubator.apache.org/) - 用于横向扩展应用程序的开源分布式内存数据库。
- [Infinispan](http://infinispan.org/) - 用于缓存的高并发键/值数据存储。
- [InfluxDB](https://github.com/influxdata/influxdb) - 用于指标、事件和实时分析的可扩展数据存储。
- [OpenTSDB](http://opentsdb.net) - 在 Apache HBase 之上编写的可扩展分布式时间序列数据库。
- [Pilosa](https://github.com/pilosa/pilosa) - 开源分布式位图索引，可显着加速跨多个海量数据集的查询。
- [RethinkDB](http://rethinkdb.com/) - 开源、可扩展的数据库使构建实时应用程序变得更加容易。
- [Secure Scuttlebutt](https://github.com/ssbc/docs) - 消息源的 P2P 数据库。
- [TiKV](https://github.com/tikv) - 分布式事务键值数据库。
- [Trino](https://trino.io/) - 用于大数据分析的快速分布式 SQL 查询引擎可帮助您探索数据世界。

### 测试

- [Goreplay](https://github.com/buger/goreplay) - 用于在测试环境中捕获和重放实时 HTTP 流量的工具。
- [Keploy](https://keploy.io) - 用于 API 测试和模拟的开源工具，通过捕获真实流量并将其转换为测试用例和存根，从而实现可靠的微服务测试。
- [Mitmproxy](https://mitmproxy.org/) - 一种交互式控制台程序，允许拦截、检查、修改和重放流量。
- [Mountebank](http://www.mbtest.org/) - 跨平台、多协议测试可通过网络进行双重测试。
- [Pact](https://docs.pact.io) - HTTP API 和非 HTTP 异步消息传递系统的合同测试框架。
- [RestQA](https://github.com/restqa/restqa) - 一种在本地管理微服务模拟、单元和性能测试的工具，具有一流的开发人员体验。
- [Specmatic](https://specmatic.io) - 将 API 规范（OpenAPI、AsyncAPI、GraphQL、gRPC 等）转换为可执行合约，用于自动化测试、服务虚拟化和向后兼容性验证，而无需编写代码。
- [Spring Cloud Contract](https://cloud.spring.io/spring-cloud-contract/) - TDD 到软件架构层面。
- [VCR](https://github.com/vcr/vcr) - 记录测试套件的 HTTP 交互，并在未来的测试运行期间重放它们，以实现快速、确定性、准确的测试。请参阅其他语言的实现的端口列表。
- [Wilma](https://github.com/epam/Wilma) - 组合的 HTTP/HTTPS 服务存根和透明代理解决方案。
- [WireMock](http://wiremock.org/) - 用于存根和模拟 Web 服务的灵活库。与通用模拟工具不同，它的工作原理是创建一个实际的 HTTP 服务器，您的测试代码可以连接到该服务器，就像连接真正的 Web 服务一样。
- [Hoverfly](https://github.com/spectolabs/hoverfly) - 面向开发人员和测试人员的轻量级服务虚拟化/API模拟工具。

## 持续集成和交付

- [Awesome CI/CD DevOps](https://github.com/ciandcd/awesome-ciandcd) :star: - 用于持续集成、持续交付和 DevOps 的出色工具的精选列表。

## Web API 建模和文档

### 异步
- [AsyncAPI](https://github.com/asyncapi/spec) - AsyncAPI 规范，定义异步 API 的行业标准。

### GraphQL

- [GraphQL](http://graphql.org/) - 查询语言旨在通过提供直观且灵活的语法和系统来描述其数据需求和交互来构建客户端应用程序。

### JSON

- [JSON:API](https://jsonapi.org/) - 客户端应如何请求获取或修改资源以及服务器应如何响应这些请求的规范。

### 休息

- [API Blueprint](https://apiblueprint.org/) - 适用于整个 API 生命周期的工具。使用它与其他人讨论您的 API。自动生成文档。或者测试套件。甚至一些代码。
- [OpenAPI](https://www.openapis.org/) - OpenAPI 规范 (OAS) 提供了在 API 生命周期的每个阶段传输信息的一致方法。
- [RAML](http://raml.org/) - RESTful API 建模语言，一种描述实用 RESTful API 的简单而简洁的方法。
- [ReDoc](https://github.com/Redocly/redoc) - OpenAPI/Swagger 生成的 API 文档。
- [Scalar](https://github.com/scalar/scalar) - 开源 API 平台：精美的 API 参考和一流的 OpenAPI/Swagger 支持。
- [Slate](https://github.com/slatedocs/slate) - 漂亮的 API 静态文档。
- [Spring REST Docs](http://projects.spring.io/spring-restdocs/) - 通过将手写文档与使用 Spring MVC Test 生成的自动生成的片段相结合来记录 RESTful 服务。
- [Swagger](https://swagger.io/) - RESTful API 的简单而强大的表示。

## 标准/建议

### 万维网

- [W3C.REC-Webarch](http://www.w3.org/TR/webarch/) - 万维网架构，第一卷。
- [RFC3986](https://tools.ietf.org/html/rfc3986) - 统一资源标识符 (URI)：通用语法。
- [RFC6570](https://tools.ietf.org/html/rfc6570) - URI 模板。
- [RFC7320](https://tools.ietf.org/html/rfc7320) - URI 设计和所有权。

### 自我主权和权力下放

- [DID](https://www.w3.org/TR/did-core/) - W3C 去中心化标识符 (DID) 规范：一种新型标识符，可实现可验证的去中心化数字身份。
- [DIDComm](https://github.com/decentralized-identity/didcomm-messaging) - 建立在 DID 去中心化设计之上的私人通信方法。
- [DIDComm Protocols](https://didcomm.org/) - 基于 DIDComm 构建的协议注册表，用于通过任何传输进行高信任、自我主权的交互。
- [IDSA](https://internationaldataspaces.org/) - 国际数据空间协会 (IDSA) 的使命是通过国际数据空间 (IDS) 创造全球数字经济的未来，国际数据空间是一个安全、主权的数据共享系统，所有参与者都可以在其中实现其数据的全部价值。

### HTTP/1.1

- [RFC7230](https://tools.ietf.org/html/rfc7230) - 消息语法和路由。
- [RFC7231](https://tools.ietf.org/html/rfc7231) - 语义和内容。
- [RFC7232](https://tools.ietf.org/html/rfc7232) - 有条件的请求。
- [RFC7233](https://tools.ietf.org/html/rfc7233) - 范围请求。
- [RFC7234](https://tools.ietf.org/html/rfc7234) - 缓存。
- [RFC7235](https://tools.ietf.org/html/rfc7235) - 验证。
- [RFC7807](https://tools.ietf.org/html/rfc7807) - HTTP API 的问题详细信息。

### HTTP/2

- [RFC7540](https://tools.ietf.org/html/rfc7540) - 超文本传输协议版本 2。

### 奎克

- [QUIC-WG](https://quicwg.org/) - IETF 工作组致力于为互联网提供下一代传输协议。
- [QUIC-Transport](https://tools.ietf.org/html/draft-ietf-quic-transport-27) - 基于 UDP 的多路复用和安全传输。

### 远程过程调用

- [JSON-RPC 2.0](http://www.jsonrpc.org/specification) - 一种无状态、轻量级远程过程调用 (RPC) 协议。
- [Open RPC](https://open-rpc.org/) - OpenRPC 规范为 JSON-RPC 2.0 API 定义了与编程语言无关的标准接口描述。

### 消息传递

- [AMQP](https://www.amqp.org/) - 高级消息队列协议。
- [MQTT](https://mqtt.org/) - MQ 遥测传输。
- [STOMP](https://stomp.github.io/) - 简单的面向文本的消息传递协议。

### 安全性

- [GNAP](https://datatracker.ietf.org/doc/html/draft-ietf-gnap-core-protocol) - 授权协商和授权协议定义了一种将授权委托给软件并将该委托传递给软件的机制。该委托可以包括对一组 API 的访问以及直接传递给软件的信息。<sup>DRAFT</sup>
- [OIDCONN](http://openid.net/connect/) - OpenID Connect 1.0 是 OAuth 2.0 协议之上的简单身份层。它允许客户端根据授权服务器执行的身份验证来验证最终用户的身份，并以可互操作和类似 REST 的方式获取有关最终​​用户的基本配置文件信息。
- [PASETO](https://paseto.io/) - Paseto 具有您所喜爱的 JOSE（JWT、JWE、JWS）的一切，而没有任何困扰 JOSE 标准的众多设计缺陷。 <sup>草稿</sup>
- [RFC5246](https://tools.ietf.org/html/rfc5246) - 传输层安全 (TLS) 协议版本 1.2。
- [RFC6066](https://tools.ietf.org/html/rfc6066) - TLS 扩展。
- [RFC6347](https://tools.ietf.org/html/rfc6347) - 数据报传输层安全版本 1.2。
- [RFC6749](https://tools.ietf.org/html/rfc6749) - OAuth 2.0 授权框架。
- [RFC6962](https://tools.ietf.org/html/rfc6962) - 证书透明度。
- [RFC7515](https://tools.ietf.org/html/rfc7515) - JSON Web 签名 (JWS) 表示使用基于 JSON 的数据结构通过数字签名或消息身份验证代码 (MAC) 保护的内容。
- [RFC7519](https://tools.ietf.org/html/rfc7519) - JSON Web Token (JWT) 是一种紧凑、URL 安全的方式，用于表示要在两方之间传输的声明。
- [RFC7642](https://tools.ietf.org/html/rfc7642) - SCIM：定义、概述、概念和要求。
- [RFC7643](https://tools.ietf.org/html/rfc7643) - SCIM：核心架构，提供平台中立的架构和扩展模型来表示用户和组。
- [RFC7644](https://tools.ietf.org/html/rfc7644) - SCIM：协议，一种应用程序级 REST 协议，用于在网络上配置和管理身份数据。

### 服务发现
- [DNS-SD](https://datatracker.ietf.org/doc/html/rfc6763) - 客户端使用标准 DNS 查询发现服务的命名实例列表的机制。
- [RFC2782](https://datatracker.ietf.org/doc/html/rfc2782) - 用于指定服务位置的 DNS RR (DNS SRV)。

### 数据格式

- [RFC4627](https://tools.ietf.org/html/rfc4627) - JavaScript 对象表示法 (JSON)。
- [RFC7049](https://tools.ietf.org/html/rfc7049) - 简明二进制对象表示（CBOR）。
- [BSON](http://bsonspec.org/) - 二进制 JSON (BSON)。
- [JSON-LD](http://json-ld.org/) - 用于链接数据的 JSON。
- [SBE](https://github.com/FIXTradingCommunity/fix-simple-binary-encoding) - 简单二进制编码（SBE）。
- [MSGPACK](https://github.com/msgpack/msgpack/blob/master/spec.md) - 消息包规范。

### 词汇

- [JSON Schema](http://json-schema.org/) - 允许您注释和验证 JSON 文档的词汇表。
- [Schema.org](http://schema.org/) - 协作性社区活动，其使命是在互联网、网页、电子邮件等上创建、维护和推广结构化数据的模式。

### 统一码

- [UNIV8](http://www.unicode.org/versions/Unicode8.0.0/) - 统一码联盟。 Unicode 标准，版本 8.0.0（加利福尼亚州山景城：Unicode 联盟，2015 年。ISBN 978-1-936213-10-8）。
- [RFC3629](https://tools.ietf.org/html/rfc3629) - UTF-8，ISO 10646 的一种转换格式。

## 组织设计/团队动力

- [委员会如何发明？](http://www.melconway.com/Home/pdf/committees.pdf) :small_orange_diamond:<sup>PDF</sup> - Melvin E. Conway，Datamation 杂志 1968 年。定义康威定律的原始文章。
- [Service per Team](https://microservices.io/patterns/decomposition/service-per-team.html) - 每个团队负责一项或多项业务功能（例如业务能力）。一个团队拥有一个由一个或多个模块组成的代码库。其代码库的大小不超过团队的认知能力。团队将其代码部署为一项或多项服务。除非已证明需要拥有多种服务，否则团队应该只拥有一项服务。
- [从团队认知负荷开始 - 团队拓扑](https://www.youtube.com/watch?v=haejb5rzKsM) :small_red_triangle:<sup>YT</sup> - DOES19 伦敦。 “整体架构与微服务”的争论通常集中在技术方面，而忽略了战略和团队动态。聪明思维的组织开始将团队认知负荷作为现代软件的指导原则，而不是技术。在本次演讲中，我们通过真实案例研究来解释如何以及为何。

## 企业与垂直行业

- [Commercetools](https://commercetools.com/) - 无头商务平台。
- [Equinox](https://www.infosysequinox.com/) - Infosys Equinox 是一个以人为本的商业和营销平台，支持跨任何渠道和接触点的丰富、超个性化体验。
- [Flamingo](https://www.flamingo.me/) - 构建灵活的现代电子商务应用程序的框架。
- [Medusa](https://medusajs.com/) - 无头开源商务平台。

## 理论

### 文章与论文

- [Autonomy, Hyperconnectivity, and Residual Causality](https://www.mdpi.com/2409-9287/6/4/81) - 通过复杂性科学理论对自适应超阈值系统设计的哲学介绍。
- [很棒的可扩展性](https://github.com/binhnguyennus/awesome-scalability) :star: - 更新且有组织的阅读列表，用于说明可扩展、可靠和高性能的大型系统的模式。著名工程师的文章和可靠的参考文献对概念进行了解释。案例研究取自为数百万至数十亿用户提供服务的经过实战考验的系统。
- [AKF Scale Cube](http://akfpartners.com/techblog/2008/05/08/splitting-applications-or-services-for-scale/) - 描述扩展服务的维度的模型。
- [CALM](http://db.cs.berkeley.edu/papers/cidr11-bloom.pdf) :small_orange_diamond:<sup>PDF</sup> - 逻辑单调性的一致性。
- [Canary Release](http://martinfowler.com/bliki/CanaryRelease.html) - 一种降低在生产中引入新软件版本的风险的技术，方法是缓慢地将更改推广到一小部分用户，然后再将其推广到整个基础设施并使每个人都可以使用。
- [CAP Theorem](http://blog.thislongrun.com/2015/03/the-cap-theorem-series.html) - 指出分布式计算机系统不可能同时提供以下所有三个保证：一致性、可用性和分区容错性。
- [无服务器计算的正式基础](https://arxiv.org/pdf/1902.05870.pdf) :small_orange_diamond:<sup>PDF</sup> - 无服务器计算抽象公开了一些低级操作细节，使程序员难以编写和推理其代码。本文通过提出 λ（无服务器计算本质的操作语义）来阐明这个问题。
- [Microservice Architecture](http://martinfowler.com/articles/microservices.html) - 将软件应用程序设计为可独立部署的服务套件的特定方法。
- [微服务 - 从设计到部署](https://www.f5.com/content/dam/f5/corp/global/pdf/ebooks/Microservices_Designing_Deploying.pdf) :small_orange_diamond:<sup>PDF</sup> - F5 有关微服务的七部分系列。
- [Microservices – Please, don’t](https://riak.com/posts/technical/microservices-please-dont/) - 关于微服务方法的一些问题的批评建议。
- [Microservices Trade-Offs](http://martinfowler.com/articles/microservice-trade-offs.html) - 思考微服务架构风格的成本和收益的指南。
- [Reactive Manifesto](http://www.reactivemanifesto.org/) - 反应式系统定义。
- [Reactive Streams](http://www.reactive-streams.org/) - 倡议为具有非阻塞背压的异步流处理提供标准。
- [ROCAS](http://resources.1060research.com/docs/2015/Resource-Oriented-Computing-Adaptive-Systems-ROCAS-1.2.pdf) :small_orange_diamond:<sup>PDF</sup> - 自适应系统的面向资源计算。
- [SECO](http://ceur-ws.org/Vol-746/IWSECO2011-6-DengYu.pdf) :small_orange_diamond:<sup>PDF</sup> - 了解软件生态系统：一种战略建模方法。
- [Testing Strategies in a Microservice Architecture](http://martinfowler.com/articles/microservice-testing/) - 管理多个可独立部署组件的额外测试复杂性的方法。
- [你的服务器作为一个函数](http://monkey.org/~marius/funsrv.pdf) :small_orange_diamond:<sup>PDF</sup> - 描述了三个抽象概念，它们结合起来呈现出一个强大的编程模型，用于构建安全、模块化和高效的服务器软件：可组合的 future、服务和过滤器。

### 站点和组织

- [Cloud Native Computing Foundation](https://www.cncf.io/) - 云原生计算基金会构建可持续的生态系统，并围绕一系列高质量项目培育社区，这些项目将容器编排为微服务架构的一部分。
- [CNCF Cloud Native Interactive Landscape](https://landscape.cncf.io/) - 云原生技术的交互景观。
- [Microservices Resource Guide](http://martinfowler.com/microservices/) - Martin Fowler 选择的文章、视频、书籍和播客可以让您更多地了解微服务架构风格。
- [Microservice Patterns](http://microservices.io/) - 微服务架构模式和最佳实践。
- [Microservice Antipatterns and Pitfalls](https://www.oreilly.com/ideas/microservices-antipatterns-and-pitfalls) - 微服务主要是已知的反模式和陷阱。

## 许可证

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png)](http://creativecommons.org/publicdomain/zero/1.0/)

## 贡献

请在提交建议之前阅读[贡献指南](https://github.com/mfornos/awesome-microservices/blob/master/CONTRIBUTING.md)。

请随意[提出问题](https://github.com/mfornos/awesome-microservices/issues) 或[创建拉取请求](https://github.com/mfornos/awesome-microservices/pulls) 添加您的内容。

:star2: 谢谢！
