# 很棒的集成 [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> 精彩的系统集成软件、模式和资源的精选列表。

系统集成是将不同 IT 系统（组件）连接在一起以作为一个整体进行功能协作的过程。

## 内容
- [Projects](#projects)
  - [人工智能网关](#ai-gateway)
  - [API管理](#api-management)
  - [API设计](#api-design)
  - [API文档](#api-documentation)
  - [API网关](#api-gateway)
  - [API测试](#api-testing)
  - [B2B整合](#b2b-integration)
  - [业务规则引擎](#business-rules-engine)
  - [业务流程管理](#business-process-management)
  - [变更数据捕获](#change-data-capture)
  - [数据整合](#data-integration)
  - [数据映射解决方案](#data-mapping-solution)
  - [企业服务总线](#enterprise-service-bus)
  - [集成框架](#integration-frameworks)
  - [集成平台即服务](#integration-platform-as-a-service)
  - [消息传递即服务](#messaging-as-a-service)
  - [托管文件传输](#managed-file-transfer)
  - [主数据管理](#master-data-management)
  - [消息代理](#message-broker)
  - [机器人过程自动化](#robotic-process-automation)
  - [模式注册表](#schema-registry)
  - [自助服务集成](#self-service-integration)
  - [流处理](#stream-processing)
  - [Webhook 基础设施](#webhook-infrastructure)
  - [工作流引擎](#workflow-engine)
- [集成模式](#integration-patterns)
  - [企业集成模式](#enterprise-integration-patterns)
  - [集成架构模式](#integration-architecture-patterns)
  - [微服务 API 模式](#microservice-api-patterns)
  - [SOA模式](#soa-patterns)
- [Resources](#resources)
  - [API规范](#api-specification)
  - [API 风格指南](#api-style-guides)
  - [Articles](#articles)
  - [Books](#books)
  - [Certifications](#certifications)
  - [Connectors](#connectors)
  - [数据格式](#data-formats)
  - [整合风格](#integration-styles)
  - [市场分析](#market-analysis)
  - [Protocols](#protocols)
  - [标准API](#standard-apis)
  - [结构和验证](#structure-and-validation)

---
## 项目
### 人工智能网关
*AI 网关将 API 网关概念应用于 AI 工作负载。它们为多个 LLM 提供商和代理工具提供了统一的入口点，处理交叉问题，例如路由、故障转移、速率限制、成本跟踪、护栏和可观察性 - 越来越多地包括 MCP 和 A2A 等面向代理的协议。*
- [agentgateway (⭐3.2k)](https://github.com/agentgateway/agentgateway) - 用于代理 AI 连接的开源数据平面，为代理到工具 (MCP) 和代理到代理 (A2A) 通信提供安全性、可观察性和治理。
- [Envoy AI Gateway (⭐1.7k)](https://github.com/envoyproxy/ai-gateway) - 一个基于 Envoy Proxy 构建的开源网关，用于管理从应用程序客户端到 GenAI 服务的请求流量，并具有统一的 API 访问和使用限制。
- [Kong AI Gateway](https://konghq.com/products/kong-ai-gateway) - 基于 Kong Gateway 构建的多 LLM AI 网关，通过专用插件提供语义缓存、提示安全性和 AI 可观察性。
- [LiteLLM (⭐50k)](https://github.com/BerriAI/litellm) - 一个 LLM 网关，通过统一的 OpenAI 兼容 API 公开 100 多个模型提供商，并具有支出跟踪、回退和速率限制功能。
- [Portkey AI Gateway (⭐12k)](https://github.com/Portkey-AI/gateway) - 一个快速 AI 网关，可通过单个 API 路由到 250 多个具有护栏、缓存、重试和负载平衡功能的 LLM。

<!--lint disable-->
**[⬆ 回到顶部](#contents)**
<!--lint enable-->
### API管理
*API 管理解决方案提供了处理整个 API 生命周期的综合方法。它们使开发人员能够创建、发布、保护和监控 API，确保系统之间高效可靠的通信。这些工具具有身份验证、速率限制和分析等功能，可提供集中控制和增强的安全性，从而更轻松地跨不同平台和环境管理和扩展 API。*
- [Akana API Management Platform](https://www.akana.com/products/api-platform) - 提供全面的生命周期管理，实现跨多云环境的快速数字化转型和强大的合规性。
- [Amazon API Management](https://aws.amazon.com/api-gateway/api-management/) - 利用 AWS 可扩展性和安全性来高效创建、监控和管理 API。
- [Amplify API Management Platform](https://www.axway.com/en/products/amplify-api-management-platform) - 提供开放、敏捷的 API 管理方法，具有强大的集成和灵活的部署选项。
- [Anypoint Platform](https://www.mulesoft.com/platform/api/manager) - 将 API 设计、集成和管理整合到一个统一平台中，简化连接和开发。
- [Apigee](https://cloud.google.com/apigee) - 为 Google 的企业级 API 管理提供强大的分析、安全性和可扩展性。
- [Azure API Management](https://azure.microsoft.com/en-us/services/api-management/) - 混合多云解决方案，通过全面的安全性和分析简化 API 生命周期管理。
- [Boomi API Management](https://boomi.com/platform/api-management/) - Boomi 企业平台内的云原生 API 管理，涵盖整个 API 生命周期，并跨环境进行集中控制。
- [DigitMarket API Manager](https://www.torryharris.com/products/digitmarket-api-manager-for-api-management) - 通过端到端生命周期管理和增强的运营洞察力，将 API 转变为战略业务工具。
- [Gravitee.io API Management (⭐421)](https://github.com/gravitee-io/gravitee-api-management) - 一个轻量级的开源平台，提供灵活的 API 治理、强大的安全性和简单的配置。
- [IBM API Connect](https://www.ibm.com/cloud/api-connect) - 提供可扩展、安全且直观的环境，用于跨云创建、管理 API 并从中获利。
- [IBM webMethods API Management](https://www.ibm.com/products/webmethods-api-management) - 提供全面的 API 生命周期管理套件，可无缝集成本地和云系统。
- [Kong Enterprise](https://konghq.com/products/kong-enterprise) - 云原生企业级解决方案，通过丰富的插件架构增强 API 连接、微服务编排和安全性。
- [Layer7 API Management](https://www.broadcom.com/products/software/api-management) - 通过持续的生命周期管理和高级集成功能，确保安全高效的 API 开发。
- [Red Hat 3scale API Management](https://www.redhat.com/en/technologies/jboss-middleware/3scale) - 通过云原生方法和强大的扩展功能简化 API 货币化和治理。
- [Sensedia API Management](https://www.sensedia.com/api-management-platform) - 提供具有高级安全性、性能监控和简化集成的全生命周期 API 解决方案。
- [Traefik API Management](https://traefik.io/traefik-hub) - 为喜欢更少 ClickOps 和更多 GitOps 驱动的 API 生命周期工作流程的 DevOps 和平台工程团队提供 API 管理即代码平台。
- [Tyk API Management](https://tyk.io/api-lifecycle-management/) - 提供注重灵活性、强大的安全性和可扩展性的高性能、开源 API 管理。
- [WSO2 API Manager (⭐986)](https://github.com/wso2/product-apim) - 一个完全开源的 API 平台，提供强大的治理、灵活的部署和社区驱动的创新。
- [Zuplo API Management](https://zuplo.com) - 一个以开发人员为中心的轻量级平台，具有 GitOps 集成、快速边缘部署、广泛的 OpenAPI 支持和无缝货币化。
<!--lint disable-->
**[⬆ 回到顶部](#contents)**
<!--lint enable-->
### API设计
*API 设计、文档和生命周期自动化工具简化了 API 的创建、维护和发展过程。这些工具提供了有效的方法来设计一致且可扩展的 API、生成全面的文档以及自动化 API 生命周期的各个阶段，从而增强开发人员体验并促进 API 采用。*
- [Apicurio Studio (⭐1k)](https://github.com/apicurio/apicurio-studio) - 一种基于 Web 的开源 API 设计工具，利用 OpenAPI 规范。
- [Dredd (⭐4.2k)](https://github.com/apiaryio/dredd) - 使用此与语言无关的 CLI 工具根据后端实现验证 API 描述文档。
- [oasdiff (⭐1.2k)](https://github.com/oasdiff/oasdiff) - 比较 OpenAPI 规范并检测重大更改，并以多种输出格式生成更改日志。
- [OpenAPI Diff (⭐1k)](https://github.com/OpenAPITools/openapi-diff) - 将 OpenAPI 规范与版本控制进行比较，并可视化 HTML 或 Markdown 格式的差异。
- [OpenAPI Generator (⭐26k)](https://github.com/OpenAPITools/openapi-generator) - 使用这个强大的 OpenAPI Spec 工具自动创建 API 客户端库、服务器存根、文档和配置文件。
- [OpenAPI Style Validator (⭐237)](https://github.com/OpenAPITools/openapi-style-validator) - 使用这个灵活且可定制的样式验证器确保您的 OpenAPI 规范符合您组织的标准。
- [OpenAPI-GUI (⭐1.4k)](https://github.com/Mermade/openapi-gui) - 使用这个直观的图形用户界面轻松创建和验证 OpenAPI 规范。
- [Redocly CLI (⭐1.4k)](https://github.com/Redocly/redocly-cli) - 使用可配置的规则集和插件检查、捆绑和预览 OpenAPI 描述。
- [Spectral (⭐3.1k)](https://github.com/stoplightio/spectral) - 使用此支持 OpenAPI 3.0 和 2.0 以及 AsyncAPI 的 linter 工具检测并修复 JSON/YAML 文件中的错误。
- [Swagger Editor (⭐9.4k)](https://github.com/swagger-api/swagger-editor) - 使用专门为基于 OpenAPI 的 API 构建的开源编辑器，轻松创建、描述和记录您的 API。
- [vacuum (⭐1k)](https://github.com/daveshanley/vacuum) - 超快的 OpenAPI linter 和质量分析工具，与 Spectral 规则集兼容。
- [Zally (⭐944)](https://github.com/zalando/zally) - 使用可提供广泛分析和反馈的 linter 工具确保 OpenAPI 规范的质量。

<!--lint disable-->
**[⬆ 回到顶部](#contents)**
<!--lint enable-->
### API文档
*探索一系列旨在创建、维护和呈现清晰、简洁且用户友好的 API 文档的工具和平台。这些资源促进开发人员之间的无缝协作，并实现 API 功能和规范的有效沟通。*
- [Bump.sh](https://bump.sh/) - 从 OpenAPI 和 AsyncAPI 定义生成托管 API 文档和变更日志，并自动检测重大变更。
- [DapperDox (⭐417)](https://github.com/DapperDox/dapperdox) - 通过轻松定制和自动更新，根据 OpenAPI/Swagger 规范生成优雅的交互式 API 文档。
- [Fern (⭐3.6k)](https://github.com/fern-api/fern) - 从 OpenAPI 或其自己的 API 定义格式生成 SDK 和交互式 API 文档。
- [OpenAPI Explorer (⭐349)](https://github.com/Rhosys/openapi-explorer) - 根据 OpenAPI 规范创建直观的交互式用户界面，简化 API 探索和测试。
- [RapiDoc (⭐1.8k)](https://github.com/rapi-doc/RapiDoc) - 通过响应式设计和丰富的配置选项生成高度可定制的交互式 API 文档。
- [ReadMe](https://readme.com/) - 托管开发人员中心将 OpenAPI 定义转化为带有使用指标的交互式、个性化 API 文档。
- [Redoc (⭐25k)](https://github.com/Redocly/redoc) - 提供简洁、现代的文档，具有高级主题、多语言支持和无缝集成。
- [Scalar (⭐15k)](https://github.com/scalar/scalar) - 通过集成的 API 客户端和广泛的框架集成，呈现来自 OpenAPI/Swagger 文档的现代交互式 API 参考。
- [Slate (⭐36k)](https://github.com/slatedocs/slate) - 将 Markdown 转换为时尚的静态 API 文档，具有直观的导航和清晰的代码示例。
- [SpectaQL (⭐1.2k)](https://github.com/anvilco/spectaql) - 为 GraphQL 模式生成静态、可定制的文档，使复杂的 API 结构易于理解。
- [Stoplight Elements (⭐2.4k)](https://github.com/stoplightio/elements) - 提供模块化、有吸引力的 UI 组件，用于构建全面的 API 参考和教程文档。
- [SwaggerHub](https://swagger.io/tools/swaggerhub/) - 集成的 API 设计和文档中心，可增强团队协作、版本控制和自动化测试。
- [Swagger UI (⭐28k)](https://github.com/swagger-api/swagger-ui) - 提供交互式浏览器内工具，用于直接根据 OpenAPI 规范可视化和测试 API。
- [Zudoku (⭐543)](https://github.com/zuplo/zudoku) - 基于 OpenAPI 构建的可定制框架，专注于通过高质量文档提供卓越的开发人员体验。

<!--lint disable-->
**[⬆ 回到顶部](#contents)**
<!--lint enable-->
### API网关
*API 网关充当客户端应用程序和后端服务之间的中介，支持请求路由、身份验证、速率限制和缓存等关键功能。它们通过为各种服务提供统一的入口点来简化管理、保护和监控 API 的过程。*
- [Apinto (⭐1.6k)](https://github.com/eolinker/apinto) - 基于 Golang 的网关，为现代架构提供动态路由、多租户和强大的 API 访问控制。
- [Ambassador Edge Stack](https://www.getambassador.io/products/edge-stack/api-gateway/) - Kubernetes 原生 API 网关，专为具有灵活路由和高级安全功能的大规模环境而设计。
- [Apache APISIX (⭐16k)](https://github.com/apache/apisix) - 高性能、动态网关，具有实时流量管理和强大的插件集成功能。
- [Apache ShenYu (⭐8.7k)](https://github.com/apache/shenyu) - Java 原生网关，擅长协议转换、服务代理和全面的 API 治理。
- [Envoy Gateway (⭐2.7k)](https://github.com/envoyproxy/gateway) - 基于 CNCF Envoy 的网关，具有 Gateway API、mTLS、JWT 和其他内置组件。
- [Gloo Edge (⭐161)](https://github.com/solo-io/gloo) - 基于 Envoy 代理的网关，为微服务生态系统提供高级流量控制、增强的安全性和可观察性。
- [Higress (⭐8.6k)](https://github.com/higress-group/higress) - 基于Envoy和Istio的下一代云原生网关，提供高性能、易于使用和丰富的插件扩展性。
- [Kong API Gateway (⭐43k)](https://github.com/Kong/kong) - 可扩展的云原生网关，通过广泛的插件支持和无缝微服务集成简化 API 管理。
- [KrakenD API Gateway (⭐2.6k)](https://github.com/devopsfaith/krakend-ce) - 具有高效中间件配置、强大安全性和无缝扩展的超高性能网关。
- [Ocelot (⭐8.7k)](https://github.com/ThreeMammals/Ocelot) - 基于 .NET 的网关，为轻量级 API 管理提供直观的路由和轻松集成。
- [Spring Cloud Gateway (⭐4.8k)](https://github.com/spring-cloud/spring-cloud-gateway) - 利用 Spring 生态系统为微服务提供强大的路由、过滤和安全性。
- [Traefik API Gateway (⭐63k)](https://github.com/traefik/traefik) - 将 Traefik Proxy（一种完全声明式应用程序代理）与企业级访问控制、分布式安全性和高级集成相结合。
- [Tyk API Gateway (⭐10k)](https://github.com/TykTechnologies/tyk) - 企业级开源网关，支持 REST、GraphQL、TCP 和 gRPC，具有高级速率限制和分析功能。

<!--lint disable-->
**[⬆ 回到顶部](#contents)**
<!--lint enable-->
### API测试
*API 测试工具部分提供了开发人员可以用来测试 REST API 和消息代理的软件工具和框架列表。本部分包括用于测试 REST API 和消息代理的 GUI 客户端、用于验证 API 使用者和提供者之间兼容性的合约测试工具、用于模拟 API 响应的模拟工具，以及用于自动化测试过程的各种测试工具和框架。*
- API客户端
   - [Bruno (⭐44k)](https://github.com/usebruno/bruno) - 一个快速、离线的 API 客户端，专为 git 友好的工作流程和无缝测试而设计。
   - [curl (⭐42k)](https://github.com/curl/curl) - 一种用于跨多种协议传输数据的多功能命令行工具，对于快速 API 测试至关重要。
   - [curlie (⭐3.6k)](https://github.com/rs/curlie) - 一个现代的、用户友好的curl 前端，结合了简单性和强大的性能。
   - [gRPC UI (⭐5.9k)](https://github.com/fullstorydev/grpcui) - 用于 gRPC API 的基于 Web 的交互式工具，提供基于浏览器的界面，用于通过动态表单生成来测试和探索 gRPC 服务。
   - [grpcurl (⭐12k)](https://github.com/fullstorydev/grpcurl) - 用于与 gRPC 服务器交互的命令行工具，支持检查和调用 RPC 方法，并支持服务器反射和协议缓冲区文件。
   - [Hoppscotch (⭐79k)](https://github.com/hoppscotch/hoppscotch) - 一种基于 Web 的轻量级 API 开发工具，通过直观的界面提供实时测试。
   - [HTTPie (⭐38k)](https://github.com/httpie/httpie) - 直观的 C​​LI HTTP 客户端，可简化 API 请求的创建和响应的检查。
   - [HttpMaster](https://www.httpmaster.net/) - 用于 HTTP 测试和调试的免费轻量级桌面工具。
   - [Insomnia (⭐38k)](https://github.com/Kong/insomnia) - 跨平台客户端，可简化 REST 和 GraphQL 服务的 API 调试和测试。
   - [posting (⭐12k)](https://github.com/darrenburns/posting) - 一个基于终端的现代 API 客户端，专为高效、无缝的 API 交互而设计。
   - [Postman](https://www.postman.com/product/api-client/) - 用于 API 开发和测试的行业标准工具，具有自动化、模拟服务器和协作文档功能。
   - [Requestly (⭐6.7k)](https://github.com/requestly/requestly) - 专为现代开发人员构建的轻量级 Git 友好 API 客户端。
   - [resty (⭐2.6k)](https://github.com/micha/resty) - 一个小型的命令行 REST 客户端，以 curl 周围的 shell 函数的形式实现，方便从终端快速探索 API。
   - [SoapUI (⭐1.6k)](https://github.com/SmartBear/soapui) - 一个全面的开源解决方案，用于测试具有广泛自动化功能的 SOAP 和 REST Web 服务。
   - [Wombat (⭐1.4k)](https://github.com/rogchap/wombat) - 跨平台桌面 gRPC 客户端，具有自动原型解析、TLS 支持和直观的 UI，用于测试一元、流式传输和双向 gRPC 请求。
   - [xh (⭐7.8k)](https://github.com/ducaale/xh) - 快速、友好的 CLI HTTP 客户端，通过改进的性能、HTTP/2 支持和内置的curl 转换重新实现了 HTTPie 的设计。
   - [Yaade (⭐1.9k)](https://github.com/EsperoTech/yaade) - 一个自托管的协作式 API 开发环境，专为团队共享而设计，具有多用户支持、持久存储以及对 REST、WebSockets 和 Markdown 文档的支持。
   - [Yaak (⭐18k)](https://github.com/mountain-loop/yaak) - 一个快速、隐私优先的桌面 API 客户端，适用于 REST、GraphQL、WebSocket、服务器发送事件和 gRPC，采用离线优先设计，使用 Tauri 和 React 构建。
- 合同测试
   - [Pact](https://docs.pact.io/) - 消费者驱动的合约测试的事实上的标准，以大多数主要语言实现，并有一个用于在团队之间共享合约的代理。
   - [Specmatic (⭐381)](https://github.com/specmatic/specmatic) - 将 OpenAPI、AsyncAPI 和 gRPC 规范转化为可执行合约，以进行合约驱动的开发和测试。
   - [Spring Cloud Contract (⭐730)](https://github.com/spring-cloud/spring-cloud-contract) - 针对 JVM 应用程序的消费者驱动的合约测试，从 Groovy 或 YAML 合约定义生成测试和存根。
- MQ客户端
   - [JMSToolBox (⭐228)](https://github.com/jmstoolbox/jmstoolbox) - 通用 JMS 客户端，跨各种代理提供广泛的兼容性和简化的消息传递测试。
   - [kcat (⭐5.7k)](https://github.com/edenhill/kcat) - Apache Kafka 的轻量级命令行工具，提供高效的消息生产和消费。
   - [MQTT Explorer (⭐3.9k)](https://github.com/thomasnordquist/MQTT-Explorer) - 详细的 MQTT 客户端提供结构化主题可视化和直观的调试。
   - [Offset Explorer](https://www.kafkatool.com) - 用于管理 Apache Kafka 集群的综合 GUI，具有用户友好的监控和管理工具。
   - [Service Bus Explorer (⭐2.1k)](https://github.com/paolosalvatori/ServiceBusExplorer) - 适用于 Azure 服务总线的高级 GUI，可实现主题、队列和订阅的深入测试和无缝管理。
- 模拟工具
   - [Hoverfly (⭐2.4k)](https://github.com/SpectoLabs/hoverfly) - 轻量级 API 模拟工具，可实现快速 HTTP(S) 服务虚拟化以实现高效测试。
   - [Imposter (⭐410)](https://github.com/outofcoffee/imposter) - 灵活的模拟服务器，支持 REST、OpenAPI、SOAP 等，可模拟不同的 API 行为。
   - [Microcks (⭐1.9k)](https://github.com/microcks/microcks) - 用于 API 模拟和测试的 Kubernetes 原生工具，支持 AsyncAPI、OpenAPI 和 Postman Collections。
   - [Mock Service Worker (MSW) (⭐17k)](https://github.com/mswjs/msw) - 用于浏览器和 Node.js 的无缝 API 模拟库，可拦截网络级别的请求。
   - [Mockable](https://www.mockable.io/) - 一种易于配置的服务，用于创建自定义 HTTP 响应，非常适合快速原型设计和测试。
   - [Mockbin (⭐140)](https://github.com/zuplo/mockbin) - 一个简单的端点生成器，用于通过实时日志记录和反馈来测试 HTTP 请求。
   - [Mockoon (⭐8.2k)](https://github.com/mockoon/mockoon) - 一个用户友好的工具，用于设计和运行模拟 REST API，具有实时模拟和轻松设置的功能。
   - [MockServer (⭐4.8k)](https://github.com/mock-server/mockserver) - 一个强大的解决方案，用于模拟任何基于 HTTP/HTTPS 的服务，简化集成测试。
   - [Mocky (⭐2k)](https://github.com/MockyAbstract/Mocky) - 一项免费在线服务，可生成用于测试 API 端点的自定义 HTTP 响应。
   - [Prism (⭐4.9k)](https://github.com/stoplightio/prism) - 一个开源 HTTP 模拟服务器，可复制 API 行为以进行早期测试和验证。
   - [WireMock (⭐7.2k)](https://github.com/wiremock/wiremock) - 强大而灵活的 API 模拟工具，为全面测试提供可靠、实时的模拟。
- 测试工具和框架
   - [Apache JMeter (⭐9.4k)](https://github.com/apache/jmeter) - 一个功能丰富的工具，用于跨不同的 Web 应用程序和服务进行负载测试和性能分析。
   - [Artillery (⭐8.9k)](https://github.com/artilleryio/artillery) - 一个完整的负载测试平台，支持 HTTP、WebSocket、Socket.io、gRPC 等，并在 AWS Lambda 和 Fargate 上进行云原生无服务器扩展。
   - [Gatling (⭐6.9k)](https://github.com/gatling/gatling) - 强大的负载测试框架，具有开发人员友好的 DSL，可提供详细的性能指标。
   - [Hurl (⭐19k)](https://github.com/Orange-OpenSource/hurl) - 用于使用纯文本语法运行 HTTP 请求的命令行工具，非常适合 API 测试和 CI/CD 集成，支持链接、捕获值和综合断言。
   - [Keploy (⭐17k)](https://github.com/keploy/keploy) - 一种以开发人员为中心的 API 和集成测试工具，可使用 eBPF 从实际流量中自动生成测试和数据模拟，支持任何语言而无需更改代码。
   - [ghz (⭐3.3k)](https://github.com/bojand/ghz) - 一个简单的 gRPC 基准测试和负载测试工具，支持各种负载计划、并发控制和详细的性能指标。
   - [Grafana k6 (⭐30k)](https://github.com/grafana/k6) - 用于 CI/CD 的开源、JS 脚本化负载测试工具。
   - [Karate (⭐8.8k)](https://github.com/karatelabs/karate) - 一个统一的测试框架，将 API 自动化、模拟和性能测试与简单、富有表现力的语法相结合。
   - [Pyresttest (⭐1.1k)](https://github.com/svanoort/pyresttest) - 基于 Python 的测试工具，提供简单的 YAML/JSON 驱动的 REST API 测试和微基准测试。
   - [REST Assured (⭐7.1k)](https://github.com/rest-assured/rest-assured) - 一种 Java DSL，通过直观的语法和无缝集成到 CI 管道中来简化 REST API 测试。
   - [RESTler (⭐2.9k)](https://github.com/microsoft/restler-fuzzer) - 一种有状态的 REST API 模糊测试工具，可通过从 OpenAPI 规范智能推断生产者-消费者依赖关系来自动发现安全性和可靠性错误。
   - [Schemathesis (⭐3.3k)](https://github.com/schemathesis/schemathesis) - 用于基于属性的 API 模式测试的 Python 库，通过强大的边缘情况检测确保可靠性。
   - [Taurus (⭐2.1k)](https://github.com/Blazemeter/taurus) - 一个开源自动化框架，通过直观的配置和集成支持简化持续测试。

<!--lint disable-->
**[⬆ 回到顶部](#contents)**
<!--lint enable-->
### B2B整合
*企业对企业 (B2B) 集成工具支持贸易伙伴之间以电子方式交换业务文档（例如订单、发票和发货通知），通常通过 AS2 和 AS4 等传输协议使用 X12 和 EDIFACT 等 EDI 标准。*
- [OpenAS2 (⭐232)](https://github.com/OpenAS2/OpenAs2App) - AS2 协议的基于 Java 的开源实现，用于通过 HTTP 进行安全、签名和加密的文档交换。
- [phase4 (⭐221)](https://github.com/phax/phase4) - 可嵌入的轻量级 Java 库实现 AS4 消息传递协议，包括 Peppol 和 CEF/eDelivery 配置文件。
- [Smooks (⭐416)](https://github.com/smooks/smooks) - 用于处理和转换结构化数据（例如 EDI、XML、CSV 和 JSON）的可扩展 Java 框架。

<!--lint disable-->
**[⬆ 回到顶部](#contents)**
<!--lint enable-->
### 业务规则引擎
*业务规则引擎和业务规则管理系统 (BRMS) 是允许组织定义、管理和执行业务规则的软件系统。这些规则用于自动化决策流程、执行业务策略并确保法规遵从性。 BRMS 为组织提供了一种集中管理其业务规则并快速轻松地对其进行更改的方法，而无需更改底层代码。对于需要敏捷并快速响应不断变化的市场条件的企业来说，这是一个宝贵的工具。*
- [Drools (⭐6.2k)](https://github.com/apache/incubator-kie-drools) - 支持高级决策模型和表示法 (DMN) 的开源引擎，与 Eclipse IDE 集成，可实现高效的规则开发。
- [FICO Blaze Advisor](https://www.fico.com/en/products/fico-blaze-advisor) - 企业级决策引擎，为业务和技术用户提供直观的界面，以快速创建和管理规则。
- [IBM ODM](https://www.ibm.com/products/operational-decision-manager) - 可扩展的决策管理系统，可简化规则编写、测试和更新，同时确保合规性和敏捷性。
- [NxBRE (⭐133)](https://github.com/ddossot/NxBRE) - 专门的 .NET 开源规则引擎，提供专为 Microsoft 环境定制的高效规则处理。
- [OpenL Tablets (⭐198)](https://github.com/openl-tablets/openl-tablets) - 灵活的开源决策管理系统，可简化业务规则和决策表的定义和执行。
- [Progress Corticon](https://www.progress.com/corticon) - 模型驱动的 BRMS 支持快速、无代码规则创建，从而提供高性能的自动化决策并保证完整性。
- [ZEN Engine (⭐1.7k)](https://github.com/gorules/zen) - 用 Rust 编写的跨平台开源业务规则引擎，通过决策表、函数和表达式的互连图执行 JSON 决策模型。

<!--lint disable-->
**[⬆ 回到顶部](#contents)**
<!--lint enable-->
### 业务流程管理
*BPM 解决方案是帮助企业简化和自动化其运营流程以提高效率和生产力的软件工具。这些解决方案通常提供流程建模、工作流管理、任务自动化和报告等功能。它们可用于自动化各种流程，从数据输入等简单任务到涉及多个部门和利益相关者的复杂工作流程。*
- [Appian BPM Suite](https://appian.com/platform/complete-automation/business-process-management-bpm.html) - 低代码 BPM 平台使 IT 和公民开发人员能够快速构建以流程和案例为中心的应用程序。
- [IBM Business Automation Workflow](https://www.ibm.com/products/business-automation-workflow) - 结合工作流程自动化和 BPM 的集成平台，以优化运营流程和决策。
- [Oracle BPM Suite](https://www.oracle.com/middleware/technologies/bpm.html) - 全面的解决方案提供强大的流程建模、工作流程自动化和实时分析，以推动卓越运营。
- [Pega Platform](https://www.pega.com/products/platform) - 先进的 BPM 和 RPA 平台具有智能流程自动化和劳动力分析功能，可简化运营。
- [TIBCO BPM Enterprise](https://www.tibco.com/products/business-process-management) - 企业 BPM 解决方案提供流程自动化、文档和预测分析，以提高绩效和决策。

<!--lint disable-->
**[⬆ 回到顶部](#contents)**
<!--lint enable-->
### 变更数据捕获
*更改数据捕获 (CDC) 解决方案可以实时识别和捕获对数据库、数据仓库和其他数据源中的数据所做的更改。这些工具持续监控数据变化并将其传播到下游系统，从而实现实时数据同步、事件驱动架构并维护分布式系统之间的数据一致性。 CDC 对于现代数据架构、微服务和实时分析至关重要。*
- [AWS Database Migration Service](https://aws.amazon.com/dms/) - 具有 CDC 支持的托管迁移和复制服务，可保持数据库、数据仓库和数据湖同步。
- [Debezium (⭐12k)](https://github.com/debezium/debezium) - 用于捕获变更数据的开源分布式平台，可将现有数据库转换为事件流以进行实时数据集成。
- [IBM InfoSphere CDC](https://www.ibm.com/products/infosphere-change-data-capture) - 企业 CDC 解决方案可捕获并交付数据更改，对源系统的影响最小且延迟较低。
- [Maxwell's daemon (⭐4.2k)](https://github.com/zendesk/maxwell) - 一种适用于 MySQL 的开源 CDC 工具，可读取数据库二进制日志并将行级更改以 JSON 形式流式传输到 Kafka、Kinesis 或其他目标等系统。
- [Oracle GoldenGate](https://www.oracle.com/integration/goldengate/) - 企业级实时数据集成和复制解决方案，为异构数据库和云平台提供全面的CDC能力。
- [PeerDB (⭐3.1k)](https://github.com/PeerDB-io/peerdb) - Postgres 首个 CDC 平台，用于从 PostgreSQL 到数据仓库、队列和存储的快速、简单复制。
- [Qlik Replicate](https://www.qlik.com/us/products/qlik-replicate) - 通用数据复制软件，为现代数据架构和分析提供实时 CDC 功能。
- [Striim](https://www.striim.com/) - 实时数据集成和流平台，具有从数据库到云分析目标的基于日志的 CDC。

<!--lint disable-->
**[⬆ 回到顶部](#contents)**
<!--lint enable-->
### 数据整合
*ETL（提取、转换、加载）和 ELT（提取、加载、转换）是用于集成和合并多个来源的数据的过程。本节介绍了一系列用于执行这些任务的开源和商业工具，包括数据摄取、转换以及加载到数据仓库或其他数据存储系统中。*
- [Airbyte (⭐21k)](https://github.com/airbytehq/airbyte) - 灵活的开源数据集成平台，可构建 ELT 管道，将数据从不同来源转移到现代目的地。
- [Apache InLong (⭐1.4k)](https://github.com/apache/inlong) - 一站式、全场景的海量数据集成框架，支持数据摄取、同步、订阅，具有实时ETL能力。
- [Apache NiFi (⭐6.1k)](https://github.com/apache/nifi) - 具有可视化界面的自动化数据集成工具，可跨系统无缝提取、转换和交付数据。
- [Apache SeaTunnel (⭐9.3k)](https://github.com/apache/seatunnel) - 高性能分布式数据集成平台，支持跨数百个连接器的批量和流同步。
- [CloverDX](https://www.cloverdx.com/) - 企业 ETL 套件提供强大的数据转换和工作流程编排，以实现可扩展的集成。
- [Conduit (⭐600)](https://github.com/ConduitIO/conduit) - 用 Go 编写的轻量级数据集成工具，使用内置或独立连接器在系统之间传输数据，并兼容 Kafka Connect。
- [dlt (⭐5.4k)](https://github.com/dlt-hub/dlt) - 开源 Python 库，用于将数据管道构建为代码，具有开箱即用的模式演化和增量加载功能。
- [Estuary Flow (⭐934)](https://github.com/estuary/flow) - 多功能、可扩展的平台，为 ETL 和 ELT 管道提供实时和批量数据集成。
- [Fivetran](https://www.fivetran.com/) - 托管 ELT，可将 700 多个源同步到数据仓库。
- [Hevo](https://hevodata.com/) - 无代码、全自动数据管道平台，支持广泛集成，简化复杂的数据工作流程。
- [IBM DataStage](https://www.ibm.com/products/datastage) - 强大的平台，可清理、转换和提供可靠的数据，为企业提供值得信赖的见解。
- [Informatica PowerCenter](https://www.informatica.com/products/data-integration/powercenter.html) - 企业级解决方案，通过全面的数据集成管理简化大数据和云分析。
- [Meltano (⭐2.5k)](https://github.com/meltano/meltano) - 声明式代码优先数据集成引擎，通过版本控制的管道配置运行 Singer Tap 和目标。
- [Microsoft SSIS](https://docs.microsoft.com/en-us/sql/integration-services/sql-server-integration-services) - 经过验证的数据集成解决方案，用于使用 SQL Server 在企业环境中构建可扩展的 ETL 流程。
- [Oracle Data Integrator](https://www.oracle.com/middleware/technologies/data-integrator.html) - 综合平台，可解决批量加载、实时流程和支持 SOA 的端到端数据管理服务。
- [Pentaho Data Integration (⭐8.3k)](https://github.com/pentaho/pentaho-kettle) - 直观、可视化的 ETL 工具，无需大量编码即可简化跨多个来源的数据摄取、混合和清理。
- [SAS Data Management](https://www.sas.com/en_us/software/data-management.html) - 强大的解决方案，可转换、集成和保护数据，以提高整个企业的质量和可靠性。
- [Singer (⭐1.3k)](https://github.com/singer-io/getting-started) - 用于编写移动数据的脚本的开源标准，定义提取“点击”和加载“目标”之间基于 JSON 的协议。
- [Stitch](https://www.stitchdata.com/) - 开发人员友好的 SaaS ETL 服务，可以轻松地将数据从众多来源提取到数据仓库中，以进行简化的分析。
- [Talend Data Integration](https://www.talend.com/products/integrate-data/) - 多功能平台，可将不同的数据源统一为可行的见解，以支持明智的业务决策。

<!--lint disable-->
**[⬆ 回到顶部](#contents)**
<!--lint enable-->
### 数据映射解决方案
*数据映射工具用于定义和转换不同系统、应用程序和格式之间的数据。这些工具允许将数据从源映射到目标，从而允许数据转换和集成。本节涵盖不同的数据映射解决方案，可用于促进不同用例的数据映射和转换过程。*
- [Altova MapForce](https://www.altova.com/mapforce) - 图形数据映射解决方案可实现任意到任意的转换，降低复杂性并加速集成项目。
- [AtlasMap (⭐212)](https://github.com/atlasmap/atlasmap) - 基于 Web 的交互式工具，通过直观的界面简化了 Java、XML、CSV 和 JSON 数据源之间的映射。
- [DataSonnet (⭐37)](https://github.com/datasonnet/datasonnet-mapper) - 基于 Jsonnet 构建的基于模板的数据转换库，专为系统集成而定制。
- [JOLT (⭐1.6k)](https://github.com/bazaarvoice/jolt) - 基于 Java 的 JSON 转换库，使用规范驱动的方法轻松进行 JSON 到 JSON 的转换。
- [JSLT (⭐695)](https://github.com/schibsted/jslt) - 强大的 JSON 查询和转换语言，灵感来自 jq 和 XPath，专为快速灵活的数据操作而设计。
- [JSONata (⭐2.6k)](https://github.com/jsonata-js/jsonata) - JSON 数据的轻量级查询和转换语言。
- [Kaoto (⭐107)](https://github.com/KaotoIO/kaoto) - 适用于 Apache Camel 的可视化数据映射器，具有支持 XML、JSON、CSV 和 XSLT 转换的拖放界面。 AtlasMap 的后继者。

<!--lint disable-->
**[⬆ 回到顶部](#contents)**
<!--lint enable-->
### 企业服务总线
*企业服务总线 (ESB) 解决方案通过提供允许不同系统和应用程序交换信息的通信层，促进不同系统和应用程序的集成。 ESB 提供一系列功能，例如消息路由、转换、协议转换和数据中介。它们通常支持各种消息传递模式和通信协议，并提供用于管理和监控消息流量的集中式平台。*
- [Anypoint Platform](https://www.mulesoft.com/platform/enterprise-integration) - 全面的集成解决方案，利用强大的 ESB 功能来连接和编排不同的系统。
- [CData Arc](https://www.cdata.com/arc/) - 集成平台（以前称为 ArcESB），可跨应用程序同步数据、简化合作伙伴连接并自动化 EDI 和 MFT 工作流程。
- [IBM App Connect](https://www.ibm.com/cloud/app-connect) - 连接不同应用程序和协议的强大集成解决方案，确保整个企业的无缝数据流。
- [IBM webMethods Integration](https://www.ibm.com/products/webmethods-integration) - 综合平台，可加速应用程序集成并简化异构系统之间的连接。
- [NServiceBus (⭐2.1k)](https://github.com/Particular/NServiceBus) - 开发人员友好、基于 .NET 的服务总线可简化消息传递并有效协调服务集成。
- [Oracle Service Bus](https://www.oracle.com/middleware/technologies/service-bus.html) - 功能强大的 ESB 解决方案，可虚拟化和管理服务交互，以降低集成复杂性。
- [Oracle SOA Suite](https://www.oracle.com/middleware/technologies/soasuite.html) - 全面的 SOA 平台，可将服务编排到组合应用程序中，从而推动高效的业务流程集成。
- [Red Hat build of Apache Camel](https://developers.redhat.com/products/redhat-build-of-apache-camel/overview) - 红帽支持 Apache Camel（红帽 Fuse 的后继者）发行版，用于构建云原生集成。
- [TIBCO BusinessWorks](https://www.tibco.com/products/tibco-businessworks) - 企业级集成平台实施经过验证的混合集成模式，以实现可靠的数据交换。
- [UltraESB](https://www.adroitlogic.com/products/ultraesb/) - 高性能 ESB 专为通过零拷贝代理和非阻塞 IO 技术实现极高的吞吐量而设计。
- [WSO2 Enterprise Integrator (⭐398)](https://github.com/wso2/product-ei) - 以 API 为中心的云原生集成平台，为现代软件架构提供强大的分布式功能。

<!--lint disable-->
**[⬆ 回到顶部](#contents)**
<!--lint enable-->
### 集成框架
*集成框架部分包括软件工具和库，可帮助开发人员在其应用程序中实施和管理集成模式。这些框架基于完善的企业集成模式 (EIP)，该模式为设计和实施集成解决方案提供了标准词汇和架构。本节中的框架可以通过提供预构建的连接器、消息路由和转换功能来帮助简化集成不同系统、应用程序和数据源的过程。*
- [Apache Camel (⭐6.2k)](https://github.com/apache/camel) - 具有 300 多个数据库、消息传递、API、云服务和企业系统连接器的集成框架。支持 Spring Boot 和 Quarkus 运行时，并包括通过 A2A 和 MCP 协议的 AI 代理互操作性。
- [Ballerina (⭐3.8k)](https://github.com/ballerina-platform/ballerina-lang) - 创新的编程语言，旨在轻松创建和集成网络服务和 API。
- [Frank!Framework (⭐162)](https://github.com/frankframework/frankframework) - 低代码 Java 消息传递框架，通过可配置的 XML 设置简化系统连接和数据集成。
- [MassTransit (⭐7.7k)](https://github.com/MassTransit/MassTransit) - .NET 分布式应用程序框架，在 RabbitMQ、Azure Service Bus 和 Amazon SQS 等传输之上提供一致的消息传递抽象。
- [Spring Cloud Stream (⭐1k)](https://github.com/spring-cloud/spring-cloud-stream) - 用于构建通过 Kafka、RabbitMQ 等的绑定器抽象连接到共享消息系统的事件驱动微服务的框架。
- [Spring Integration (⭐1.6k)](https://github.com/spring-projects/spring-integration) - Spring 生态系统的扩展，使用经过验证的企业集成模式提供开箱即用的集成功能。
- [Wolverine (⭐2.2k)](https://github.com/JasperFx/wolverine) - 适用于 .NET 的简单消息传递和命令总线框架，具有内置的持久消息传递和传输（如 RabbitMQ 和 Kafka）。

<!--lint disable-->
**[⬆ 回到顶部](#contents)**
<!--lint enable-->
### 集成平台即服务
*集成平台即服务 (iPaaS) 是一个基于云的平台，使企业能够轻松集成不同的系统、应用程序和数据源。它提供了一个统一的平台来管理各个系统之间的数据流，简化集成不同系统和自动化工作流程的过程。 iPaaS 工具通常提供用于设计、部署和管理集成的可视化界面，以及用于与流行系统和服务集成的预构建连接器和 API。*
- [Anypoint Platform](https://www.mulesoft.com/platform/saas/cloudhub-ipaas-cloud-based-integration) - 将 API 管理和集成结合到一个平台中，实现跨不同应用程序的无缝连接。
- [Azure Logic Apps](https://azure.microsoft.com/en-us/products/logic-apps) - Microsoft 的 iPaaS，用于使用数百个适用于云和本地系统的预构建连接器构建自动化工作流程。
- [Boomi AtomSphere](https://boomi.com/platform) - 云原生智能平台，可轻松连接系统，同时实现集成流程自动化。
- [Camel K (⭐919)](https://github.com/apache/camel-k) - 基于 Apache Camel 构建的轻量级 Kubernetes 原生集成平台，直接在 Kubernetes 和 OpenShift 上运行集成路由作为云原生无服务器服务。
- [Celigo Integration Platform](https://www.celigo.com/platform/) - 用户友好的 iPaaS 具有预构建模板，可实现快速 SaaS 到 SaaS 集成和直观的拖放设计。
- [Jitterbit Harmony](https://www.jitterbit.com/platform/ipaas) - 全面的集成解决方案提供预构建的工作流程和自动化模板，以加速业务流程。
- [IBM Cloud Integration](https://www.ibm.com/cloud/integration) - 下一代平台利用人工智能来简化集成、提高可扩展性并加快部署。
- [IBM webMethods](https://www.ibm.com/products/webmethods) - 一体化集成平台，可统一应用程序、简化流程并提高整体效率。
- [Informatica Intelligent Cloud Services](https://www.informatica.com/products/cloud-integration.html) - 云数据管理工具套件，可提高生产力并简化应用程序和数据集成。
- [OpenText Alloy](https://businessnetwork.opentext.com/enterprise-data-management/) - 企业数据管理解决方案，将基本集成转变为可行的见解和更明智的决策。
- [Oracle Integration Cloud Service](https://www.oracle.com/integration/application-integration/) - 强大的平台，具有针对 SaaS 和本地应用程序的预构建连接，可简化集成流程。
- [SAP Integration Suite](https://www.sap.com/products/technology-platform/integration-suite.html) - 云原生解决方案提供预构建适配器、API 管理和事件代理以实现端到端连接。
- [SnapLogic Intelligent Integration Platform](https://www.snaplogic.com/products/intelligent-integration-platform) - 人工智能驱动的平台，可快速连接应用程序和数据，确保高效且可扩展的集成。
- [TIBCO Cloud Integration](https://docs.tibco.com/products/tibco-cloud-integration-ipaas) - 灵活、API 主导和事件驱动的平台使您能够快速集成几乎任何系统。
- [Tray.io](https://tray.ai/) - 具有拖放界面的低代码自动化平台，可以轻松构建可扩展的集成和工作流程。
- [Workato](https://www.workato.com/) - 统一集成和工作流程自动化解决方案，可简化复杂流程并提高运营效率。

<!--lint disable-->
**[⬆ 回到顶部](#contents)**
<!--lint enable-->
### 消息传递即服务
*云消息传递即服务 (MaaS) 是指基于云的消息传递平台，可在分布式应用程序和服务之间实现可靠、安全且可扩展的通信。这些平台提供各种消息传递模式，例如发布-订阅、请求-回复和流式传输。它们还提供消息路由、过滤、转换和持久化等功能，并支持各种协议和 API 以与不同系统集成。*
- [Amazon MQ](https://aws.amazon.com/amazon-mq) - 完全托管的消息代理支持 Apache ActiveMQ 和 RabbitMQ，确保可靠且安全的消息传递。
- [Amazon MSK](https://aws.amazon.com/msk) - 托管 Apache Kafka 服务，可简化集群设置、扩展和实时数据流。
- [Amazon SQS](https://aws.amazon.com/sqs) - 可靠、完全托管的队列服务，可解耦微服务并无缝扩展分布式应用程序。
- [Amazon SNS](https://aws.amazon.com/sns) - 托管的发布/订阅消息服务，可以灵活地通知订阅者并支持各种传送协议。
- [Alibaba Cloud Message Queue for Apache Kafka](https://www.alibabacloud.com/product/kafka) - 高吞吐量的 Kafka 服务与阿里云无缝集成，可实现实时数据处理。
- [Alibaba Cloud Message Queue for RabbitMQ](https://www.alibabacloud.com/product/rabbitmq) - 可扩展的 RabbitMQ 解决方案为分布式消息传递提供低延迟和高吞吐量。
- [Alibaba Cloud Message Service](https://www.alibabacloud.com/product/message-service) - 分布式消息服务，确保解耦系统之间可靠的数据传输。
- [AlibabaMQ for Apache RocketMQ](https://www.alibabacloud.com/product/mq) - 强大的消息队列服务支持异步通信，具有高可用性和持久性。
- [Anypoint MQ](https://www.mulesoft.com/platform/anypoint-mq-message-queue) - 与 Anypoint Platform 集成的企业级消息传递服务，可实现灵活可靠的消息编排。
- [Azure Event Hubs](https://azure.microsoft.com/en-us/products/event-hubs/) - 高吞吐量、完全托管的事件摄取（发布-订阅）服务本身支持 Kafka 协议。
- [Azure Service Bus](https://azure.microsoft.com/en-us/services/service-bus/) - 支持多种模式和协议的云消息解决方案，可实现稳健的企业集成。
- [CloudAMQP](https://www.cloudamqp.com/) - 托管 RabbitMQ 服务具有直观的 Web 控制台、高级分析和无缝可扩展性。
- [Confluent Cloud](https://www.confluent.io/confluent-cloud/) - 完全托管的 Kafka 服务提供架构注册、连接器和治理等企业功能。
- [Google Cloud Managed Service for Apache Kafka](https://cloud.google.com/products/managed-service-for-apache-kafka) - 简化了 Google Cloud 上实时流应用程序的 Kafka 部署和管理。
- [Google Cloud Pub/Sub](https://cloud.google.com/pubsub) - 高吞吐量消息服务，支持具有灵活交付模型的事件驱动架构。
- [Huawei Cloud Distributed Message Service](https://www.huaweicloud.com/intl/en-us/product/dms.html) - 完全托管的消息传递服务可确保应用程序之间的安全、可扩展且可靠的通信。
- [Huawei Cloud Distributed Message Service for Kafka](https://www.huaweicloud.com/intl/en-us/product/dmskafka.html) - 托管 Kafka 解决方案可简化扩展和管理，同时提供高性能和安全性。
- [IBM MQ on Cloud](https://www.ibm.com/cloud/mq) - 企业消息传递服务，在云环境中跨应用程序提供安全、可靠的数据传输。
- [IronMQ](https://www.iron.io/mq) - 弹性的云原生消息队列，专为可扩展且可靠地处理大容量消息而设计。
- [Oracle Cloud Streaming](https://www.oracle.com/cloud/cloud-native/streaming/) - 无服务器实时事件流平台，兼容 Apache Kafka，可实现高效数据处理。
- [Solace PubSub+ Cloud](https://solace.com/products/platform/cloud/) - 集成事件流平台提供对数据管道的全面可见性和控制。
- [Yandex Message Queue](https://cloud.yandex.com/en/services/message-queue) - 云消息服务与 Amazon SQS API 兼容，可轻松与现有系统集成。
- [Yandex Managed Service for Apache Kafka](https://cloud.yandex.com/en/services/managed-kafka) - 完全托管的 Kafka 服务，具有自动扩展、监控和维护功能，可实现无忧流式传输。

<!--lint disable-->
**[⬆ 回到顶部](#contents)**
<!--lint enable-->
### 托管文件传输
*托管文件传输 (MFT) 解决方案提供安全可靠的文件传输功能，帮助组织满足法规遵从性要求、提高运营效率并降低数据泄露风险。 MFT 软件通常包括加密、数字签名、用户访问控制和详细审核日志等功能，以确保数据安全传输并可以在整个传输过程中进行跟踪。*
- [Axway Managed File Transfer](https://www.axway.com/en/products/managed-file-transfer) - 强大的平台提供先进的安全性以及跨企业系统高效、可靠的数据传输。
- [CData Arc MFT](https://www.cdata.com/arc/mft/) - 企业级 MFT 解决方案（以前称为 ArcESB）具有直观的界面和强大的自动化功能，可简化文件交换。
- [GlobalSCAPE EFT](https://www.globalscape.com/eft) - 强化的文件传输服务器可确保关键任务数据的端到端加密、自动化和合规性。
- [GoAnywhere MFT](https://www.goanywhere.com/products/goanywhere-mft) - 全面的解决方案提供集中、安全的文件传输以及自动化和完整的审核日志记录。
- [IBM Sterling Secure File Transfer](https://www.ibm.com/products/secure-file-transfer) - 可扩展的高性能 MFT 平台专为安全、快速且可靠的文件交换而设计。
- [IBM webMethods MFT](https://www.ibm.com/products/webmethods-mft) - 集成的托管文件传输解决方案，支持跨混合环境的灵活部署。
- [JSCAPE MFT Server](https://www.jscape.com/products/file-transfer-servers/jscape-mft-server) - 安全、与协议无关的平台，具有自动化和合规性。
- [Oracle Managed File Transfer](https://www.oracle.com/middleware/technologies/mft/managed-file-transfer.html) - 简化企业运营的安全文件交换和管理的综合平台。
- [Progress MOVEit](https://www.progress.com/moveit) - 安全、自动化的文件传输解决方案，为受监管行业提供有保证的交付、加密和合规性工具。
- [TIBCO Managed File Transfer](https://www.tibco.com/products/tibco-managed-file-transfer) - 集中式 MFT 平台具有强大的自动化和安全功能，旨在支持多种文件传输场景。
- [Titan MFT Server](https://southrivertech.com/titan-mft-server/) - 企业级 MFT 服务器提供高可用性、故障转移功能和高效的大规模文件自动化。

<!--lint disable-->
**[⬆ 回到顶部](#contents)**
<!--lint enable-->
### 主数据管理
*主数据管理 (MDM) 解决方案可帮助组织跨不同系统、应用程序和部门创建单一、权威的准确且一致的数据源。这些工具提供数据分析、清理、丰富和治理功能，使组织能够提高数据质量、减少错误并提高运营效率。*
- [IBM InfoSphere Master Data Management](https://www.ibm.com/products/ibm-infosphere-master-data-management) - 集中数据治理的综合平台，确保整个企业的一致性和准确性。
- [Informatica Multidomain MDM](https://www.informatica.com/products/master-data-management/multidomain-mdm.html) - 用于管理和治理所有领域的主数据、提高整体数据质量的集成解决方案。
- [Oracle Enterprise Data Management](https://www.oracle.com/performance-management/enterprise-data-management/) - 强大的工具，可集中主数据以支持更快、更有效的决策和运营敏捷性。
- [Reltio](https://www.reltio.com/products/multidomain-mdm) - 云原生、多域 MDM 平台将数据质量、治理和实时分析相结合，提供 360° 视图。
- [SAP Master Data Governance](https://www.sap.com/products/master-data-governance.html) - 集中式解决方案可整合和管理主数据，以确保一致性和高质量。
- [SAS MDM](https://support.sas.com/en/software/mdm-support.html) - 统一平台将不同来源的数据集成到准确的主记录中，以提高效率。
- [Stibo MDM](https://www.stibosystems.com/platform) - 经过验证的多域 MDM 解决方案专注于数据透明度和治理，以提供单一事实来源。
- [Teradata MDM](https://www.teradata.co.uk/Products/Applications/Master-Data-Management) - 通过维护准确的参考数据来建立一致的分析基础，以提高投资回报率。
- [TIBCO EBX](https://www.tibco.com/products/ebx) - 用于治理和管理共享数据资产、确保一致性并实现更明智决策的综合平台。

<!--lint disable-->
**[⬆ 回到顶部](#contents)**
<!--lint enable-->
### 消息代理
*消息代理是一种中间件，它通过促进消息交换来允许不同应用程序或系统之间进行通信。它们可以处理不同的消息传递模式，例如点对点、发布-订阅和请求-回复，并提供消息转换、路由和过滤等功能。*
- [Apache ActiveMQ (⭐2.4k)](https://github.com/apache/activemq) - 实现 JMS 的开源代理，可实现同步和异步消息传递之间的无缝转换。
- [Apache Artemis (⭐1k)](https://github.com/apache/artemis) - 多协议消息代理，支持各种行业标准协议，例如 AMQP 1.0、MQTT 3.1.1、MQTT 5 和 STOMP。
- [Apache EventMesh (⭐1.7k)](https://github.com/apache/eventmesh) - 动态事件驱动的应用程序运行时，充当无服务器事件中间件，用于解耦应用程序和后端代理。
- [Apache Iggy (⭐4.3k)](https://github.com/apache/iggy) - 用 Rust 编写的持久消息流平台，支持 QUIC、TCP 和 HTTP 传输，具有高吞吐量和低延迟。
- [Apache Kafka (⭐32k)](https://github.com/apache/kafka) - 分布式、高吞吐量系统，专为实时数据流和容错处理而设计。
- [Apache Pulsar (⭐15k)](https://github.com/apache/pulsar) - 多功能发布/订阅和流媒体平台，为现代应用程序提供可扩展、低延迟的消息传递。
- [Apache Qpid (⭐70)](https://github.com/apache/qpid-broker-j) - 符合 AMQP 规范的消息传递工具，支持企业级消息传递的多语言。
- [Apache RocketMQ (⭐22k)](https://github.com/apache/rocketmq) - 高性能分布式消息传递平台专为低延迟和高吞吐量而设计。
- [AutoMQ (⭐10k)](https://github.com/AutoMQ/automq) - 无状态、与 Kafka 兼容的代理在 S3 级对象存储上运行，可实现弹性扩展并降低成本。
- [BlazingMQ (⭐3.1k)](https://github.com/bloomberg/blazingmq) - 分布式消息队列系统专注于满足现代工作流程需求的效率和可靠性。
- [Centrifugo (⭐10k)](https://github.com/centrifugal/centrifugo) - 可扩展的实时消息传递服务器，最大限度地减少向在线用户传递事件的延迟。
- [Eclipse Mosquitto (⭐10k)](https://github.com/eclipse/mosquitto) - 轻量级 MQTT 代理针对低功耗设备进行了优化，具有强大的加密和身份验证功能。
- [ElasticMQ (⭐2.8k)](https://github.com/softwaremill/elasticmq) - 具有 Amazon SQS 兼容接口的内存消息队列，提供具有可选 UI 和队列持久性的独立或嵌入式部署。
- [EMQX (⭐16k)](https://github.com/emqx/emqx) - 专为物联网和工业应用而构建的高性能 MQTT 代理，确保可扩展的消息传递。
- [HiveMQ (⭐1.2k)](https://github.com/hivemq/hivemq-community-edition) - MQTT 代理专为大规模可靠的物联网消息传递而构建，具有开源社区版本和丰富的扩展系统。
- [IBM MQ](https://www.ibm.com/products/mq) - 企业级消息传递解决方案提供强大的功能、高可用性和多协议支持。
- [KubeMQ](https://kubemq.io/) - Kubernetes 原生消息代理和队列系统，专为可扩展性、高可用性和无缝云集成而设计。
- [LavinMQ (⭐964)](https://github.com/cloudamqp/lavinmq) - 实现 AMQP 0-9-1 和 MQTT 协议的高性能消息队列服务器，采用 Crystal 构建，可实现卓越的吞吐量和最小的资源使用量。
- [Magistrala (⭐2.6k)](https://github.com/absmach/magistrala) - 分布式、事件驱动的消息传递基础设施，支持多种协议（HTTP、MQTT、WebSocket、CoAP），具有强大的安全性和物联网功能。
- [NATS (⭐20k)](https://github.com/nats-io/nats-server) - 轻量级、高性能消息系统，非常适合微服务和云原生架构。
- [NSQ (⭐25k)](https://github.com/nsqio/nsq) - 实时分布式消息传递平台旨在大规模运行，每天通过去中心化拓扑处理数十亿条消息。
- [Oracle AQ](https://www.oracle.com/database/technologies/advanced-queuing.html) - Oracle 数据库内的集成消息传递解决方案，提供可靠、高效的消息传递。
- [RabbitMQ (⭐13k)](https://github.com/rabbitmq/rabbitmq-server) - 实施 AMQP 的流行开源代理，以可靠性、集群和易用性而闻名。
- [Red Hat AMQ](https://www.redhat.com/en/technologies/jboss-middleware/amq) - 基于开源技术的企业消息传递平台，提供可扩展且可靠的消息传递。
- [Redpanda (⭐12k)](https://github.com/redpanda-data/redpanda) - 兼容 Kafka 的流媒体平台消除了 Zookeeper，提供高性能和低延迟。
- [RMQ (⭐1.6k)](https://github.com/wellle/rmq) - 用 Go 编写的 Redis 支持的消息队列，提供灵活的队列管理、批量消费者和高效的交付模式。
- [TIBCO Enterprise Message Service](https://www.tibco.com/products/tibco-enterprise-message-service) - 基于标准的 JMS 实现可实现应用程序之间高效、稳健的消息交换。
- [VerneMQ (⭐3.5k)](https://github.com/vernemq/vernemq) - 高性能分布式 MQTT 代理，专为现代环境中可扩展且高效的消息传递而设计。
- [ZeroMQ (⭐10k)](https://github.com/zeromq/libzmq) - 高性能异步消息传递库，为分布式应用程序提供无代理、基于套接字的消息传递模式。

<!--lint disable-->
**[⬆ 回到顶部](#contents)**
<!--lint enable-->
### 机器人过程自动化
*机器人流程自动化 (RPA) 解决方案是可在业务流程中自动执行重复性、基于规则的任务的软件工具。 RPA 机器人可以准确、快速地执行数据输入、数据提取和数据处理等任务，从而使人类工作者能够专注于更复杂的任务。*
- [Automation Anywhere](https://www.automationanywhere.com/) - 智能自动化生态系统可通过先进的 RPA 功能简化业务流程并减少错误。
- [Blue Prism](https://www.blueprism.com/products/intelligent-rpa-automation/) - 无代码平台提供强大、可扩展的自动化，以最大限度地减少手动任务并提高生产力。
- [OpenRPA (⭐2.9k)](https://github.com/open-rpa/openrpa) - 企业级开源机器人流程自动化套件。
- [Robot Framework (⭐11k)](https://github.com/robotframework/robotframework) - 一个开源自动化框架，具有人性化的关键字语法，使技术和非技术用户能够经济高效地创建测试脚本和自动化业务流程，通过广泛的库和集成支持 Web、API、移动和数据库自动化。
- [TagUI (⭐6.3k)](https://github.com/aisingapore/TagUI) - 一款开源 RPA 工具，通过 20 多种人类语言的自然语言脚本实现自动化民主化，使非程序员能够自动化 Web、桌面和数据任务，同时通过 Python 和 R 集成 AI/ML 功能以实现智能流程自动化。
- [Tungsten RPA](https://www.tungstenautomation.com/products/rpa) - 由人工智能驱动的无代码自动化解决方案，可提高整个工作流程的准确性、效率和合规性。
- [UiPath](https://www.uipath.com/product) - 全面的 RPA 平台可自动执行日常任务，从而实现跨企业的可扩展数字化转型。
- [WorkFusion](https://www.workfusion.com/platform/) - 企业自动化解决方案将 RPA 与智能自动化相结合，以简化复杂的工作流程。

<!--lint disable-->
**[⬆ 回到顶部](#contents)**
<!--lint enable-->
### 模式注册表
*架构注册表提供了一个中央存储库，用于管理和验证消息和事件数据的架构（例如 Avro、JSON Schema 和 Protobuf）。随着模式的发展，它们强制执行兼容性规则，使生产者和消费者能够在事件驱动的架构中安全地交换数据。*
- [Apicurio Registry (⭐813)](https://github.com/Apicurio/apicurio-registry) - API 设计和架构的开源注册表，支持 Avro、Protobuf、JSON Schema、OpenAPI 和 AsyncAPI 工件，并具有可配置的兼容性规则。
- [AWS Glue Schema Registry](https://docs.aws.amazon.com/glue/latest/dg/schema-registry.html) - 托管注册表，用于验证和控制流数据模式的演变，与 MSK、Kinesis 和 Flink 集成。
- [Azure Schema Registry](https://learn.microsoft.com/en-us/azure/event-hubs/schema-registry-overview) - 托管在 Azure 事件中心的架构注册表，可集中事件驱动应用程序的架构管理和治理。
- [Confluent Schema Registry (⭐2.4k)](https://github.com/confluentinc/schema-registry) - 广泛使用的 Kafka 注册表，为 Avro、JSON Schema 和 Protobuf schema 提供 RESTful 接口和兼容性检查。
- [Karapace (⭐618)](https://github.com/Aiven-Open/karapace) - Confluence Schema Registry 和 Kafka REST API 的开源、直接替代品。

<!--lint disable-->
**[⬆ 回到顶部](#contents)**
<!--lint enable-->
### 自助服务集成
*自助服务和公民集成工具旨在使非技术用户能够构建集成，而无需广泛的编程知识。这些工具通常具有拖放界面和针对流行应用程序和服务的预构建连接器。*

- [Activepieces (⭐22k)](https://github.com/activepieces/activepieces) - 开源、自托管自动化平台，具有无代码可视化生成器和数百个连接器（“部件”），定位为 Zapier 的替代品。
- [Automatisch (⭐13k)](https://github.com/automatisch/automatisch) - 开源业务自动化工具，可连接流行的服务，而无需与第三方共享您的数据。
- [Huginn (⭐49k)](https://github.com/huginn/huginn) - 自托管系统，用于构建监控服务并代表您行事的代理，例如 IFTTT 的可破解版本。
- [IFTTT](https://ifttt.com/) - 易于使用的平台，通过简单的条件语句连接 Web 服务，支持自定义工作流程创建。
- [Make (Integromat)](https://www.make.com) - 低代码自动化工具，具有可视化界面、高级数据转换和模块化工作流程执行。
- [Microsoft Power Automate](https://powerautomate.microsoft.com) - 基于云的服务，具有直观的界面，用于创建无缝集成不同应用程序的自动化工作流程。
- [n8n (⭐192k)](https://github.com/n8n-io/n8n) - 开源工作流程自动化工具，具有 400 多个连接器，让您可以完全控制数据和集成。
- [Node-RED (⭐23k)](https://github.com/node-red/node-red) - 低代码、基于流程的编程工具，用于通过基于浏览器的可视化编辑器将硬件设备、API 和在线服务连接在一起。
- [Pipedream (⭐11k)](https://github.com/PipedreamHQ/pipedream) - 以开发人员为中心的集成平台，将数千个预构建的触发器和操作与 Node.js、Python、Go 和 Bash 中的代码级控制相结合。
- [Zapier](https://zapier.com/) - 直观的平台，连接数百个 Web 服务以创建高效、无代码的自动化。

<!--lint disable-->
**[⬆ 回到顶部](#contents)**
<!--lint enable-->
### 流处理
*流处理框架和引擎实时转换、丰富、连接和聚合连续的事件流。它们通过在动态数据之上添加状态计算（窗口、一次性处理和事件时间语义）来补充消息代理。*
- [Apache Beam (⭐8.6k)](https://github.com/apache/beam) - 用于批处理和流处理管道的统一编程模型，可跨运行器（例如 Flink、Spark 和 Google Cloud Dataflow）移植。
- [Apache Flink (⭐26k)](https://github.com/apache/flink) - 具有状态计算、一次性语义和大规模事件时间处理的分布式流处理框架。
- [Apache Spark (⭐43k)](https://github.com/apache/spark) - 统一分析引擎，其结构化流 API 在 Spark SQL 引擎上提供可扩展、容错的流处理。
- [Arroyo (⭐4.9k)](https://github.com/ArroyoSystems/arroyo) - Rust 原生流处理引擎，可让用户使用 SQL 构建实时管道，专为无服务器操作而设计。
- [Bytewax (⭐2k)](https://github.com/bytewax/bytewax) - 基于 Timely Dataflow 构建的 Python 流处理框架，将 Python 的生态系统与 Rust 性能相结合。
- [Kafka Streams](https://kafka.apache.org/documentation/streams/) - 用于直接在 Apache Kafka 之上构建流应用程序和微服务的客户端库。
- [ksqlDB (⭐304)](https://github.com/confluentinc/ksql) - 专为 Kafka 上的流处理应用程序构建的数据库，使用 SQL 进行查询。
- [Redpanda Connect (⭐8.6k)](https://github.com/redpanda-data/connect) - 用于在系统之间转换和路由数据的声明式流处理器和连接器工具包（以前称为 Benthos）。
- [RisingWave (⭐9k)](https://github.com/risingwavelabs/risingwave) - 与 Postgres 兼容的流数据库，用于事件流的增量、实时物化视图。

<!--lint disable-->
**[⬆ 回到顶部](#contents)**
<!--lint enable-->
### Webhook 基础设施
*大规模可靠地发送、接收和操作 Webhook 的工具 - 涵盖交付重试、签名和验证、扇出、事件日志和重播。*
- [Convoy (⭐2.8k)](https://github.com/frain-dev/convoy) - 开源 Webhooks 网关，用于发送和接收具有重试、速率限制和管理仪表板功能的 Webhooks。
- [Hookdeck](https://hookdeck.com/) - 用于接收、排队、转换和重播 Webhook 和其他事件流量的托管事件网关。
- [Svix (⭐3.2k)](https://github.com/svix/svix-webhooks) - 使用开源服务器的 Webhook 发送服务，为 Webhook 提供商处理签名、重试和端点管理。

<!--lint disable-->
**[⬆ 回到顶部](#contents)**
<!--lint enable-->
### 工作流引擎
*支持设计、执行和监控复杂工作流程或业务流程的软件工具。工作流引擎提供了一种自动化和简化业务流程的方法，而编排引擎则有助于管理不同系统或服务之间的交互。*
- [Activiti (⭐10k)](https://github.com/Activiti/Activiti) - 以 Java 为中心的轻量级 BPMN 引擎，可高效执行业务工作流程，同时注重简单性。
- [Apache Airflow (⭐45k)](https://github.com/apache/airflow) - 用于以编程方式创建、调度和监控工作流程的平台，非常适合管理复杂的数据管道。
- [Argo Workflows (⭐16k)](https://github.com/argoproj/argo-workflows) - 容器原生工作流引擎，专为在基于 Kubernetes 的云原生环境中编排并行作业而设计。
- [AWS Step Functions](https://aws.amazon.com/step-functions/) - 无服务器编排服务，用于将 AWS 服务和自定义逻辑组合到可视状态机工作流程中。
- [Azkaban (⭐4.5k)](https://github.com/azkaban/azkaban) - 分布式调度程序，可简化大规模数据处理环境中作业依赖性的管理。
- [Bonita (⭐174)](https://github.com/bonitasoft/bonita-engine) - 具有设计器界面的开源 BPMN 引擎，用于构建和自动化复杂的业务流程。
- [Cadence (⭐9.3k)](https://github.com/uber/cadence) - 容错、有状态的平台，可以可靠地编排长时间运行的工作流程和复杂的应用程序。
- [Camunda (⭐4.1k)](https://github.com/camunda/camunda) - 流程编排平台构建在水平可扩展的 Zeebe 引擎上，具有完整的 BPMN 和 DMN 支持。
- [Conductor (⭐31k)](https://github.com/conductor-oss/conductor) - 持久的工作流编排引擎最初在 Netflix 构建，现在在原始存储库存档后由社区维护。
- [Dagster (⭐15k)](https://github.com/dagster-io/dagster) - 数据编排器具有声明性的、基于资产的编程模型，用于构建和观察数据管道。
- [Elsa Core (⭐7.7k)](https://github.com/elsa-workflows/elsa-core) - .NET Core 库可无缝集成到任何应用程序中以执行和管理工作流。
- [Flowable (⭐9.3k)](https://github.com/flowable/flowable-engine) - 紧凑、高效的开源引擎集，用于自动化和扩展企业工作流程。
- [Google Cloud Workflows](https://cloud.google.com/workflows) - 无服务器编排将 Google Cloud 服务和基于 HTTP 的 API 组合成可靠、有状态的工作流程。
- [Inngest (⭐5.4k)](https://github.com/inngest/inngest) - 事件驱动的持久执行平台，可在现有服务内运行可靠的步骤函数。
- [jBPM (⭐1.7k)](https://github.com/kiegroup/jbpm) - 用于自动化业务流程和决策的综合工具包，具有强大的工作流程管理功能。
- [Kestra (⭐27k)](https://github.com/kestra-io/kestra) - 事件驱动的声明性协调器，具有 YAML 中定义的工作流程以及数百个用于数据和基础设施自动化的插件。
- [LittleHorse (⭐379)](https://github.com/littlehorse-enterprises/littlehorse) - 基于 Kafka Streams 构建的高吞吐量、低延迟微服务编排引擎，具有多种语言的 SDK。
- [Prefect (⭐22k)](https://github.com/PrefectHQ/prefect) - 现代、开发人员友好的编排工具针对数据管道和复杂的工作流程进行了优化。
- [Restate (⭐4k)](https://github.com/restatedev/restate) - 耐用的执行引擎，用于将弹性工作流程、事件驱动的服务和有状态处理程序构建为纯代码。
- [StackStorm (⭐6.4k)](https://github.com/StackStorm/st2) - 强大的自动化引擎，结合传感器、触发器和工作流程来协调复杂的 IT 流程。
- [Temporal (⭐20k)](https://github.com/temporalio/temporal) - 开源工作流即代码平台，旨在构建可靠、可扩展且容错的应用程序。
- [Windmill (⭐16k)](https://github.com/windmill-labs/windmill) - 开源开发者平台，可将 Python、TypeScript、Go 等脚本转换为工作流程、内部 UI 和计划作业。

<!--lint disable-->
**[⬆ 回到顶部](#contents)**
<!--lint enable-->
## 集成模式
*集成模式为企业内常见的集成问题提供标准化的解决方案。企业集成模式（EIP）提供了一种用于描述集成问题和解决方案的通用语言，而集成架构模式则解决了企业架构师的高级问题。面向服务的架构 (SOA) 模式为设计和实现面向服务的架构提供指导，确保服务可扩展、可重用和松散耦合。*
### 企业集成模式
*图案来自 Gregor Hohpe 和 Bobby Woolf 所著的书。*
- [Aggregator](https://www.enterpriseintegrationpatterns.com/patterns/messaging/Aggregator.html) - 我们如何组合各个相关消息的结果，以便将它们作为一个整体进行处理？
- [Canonical Data Model](https://www.enterpriseintegrationpatterns.com/patterns/messaging/CanonicalDataModel.html) - 在集成使用不同数据格式的应用程序时，如何最大限度地减少依赖性？
- [Channel Adapter](https://www.enterpriseintegrationpatterns.com/patterns/messaging/ChannelAdapter.html) - 如何将应用程序连接到消息传递系统以便它可以发送和接收消息？
- [Channel Purger](https://www.enterpriseintegrationpatterns.com/patterns/messaging/ChannelPurger.html) - 如何防止通道上的“剩余”消息干扰测试或正在运行的系统？
- [Claim Check](https://www.enterpriseintegrationpatterns.com/patterns/messaging/StoreInLibrary.html) - 如何在不牺牲信息内容的情况下减少整个系统发送的消息的数据量？
- [Command Message](https://www.enterpriseintegrationpatterns.com/patterns/messaging/CommandMessage.html) - 如何使用消息传递来调用另一个应用程序中的过程？
- [Competing Consumers](https://www.enterpriseintegrationpatterns.com/patterns/messaging/CompetingConsumers.html) - 消息客户端如何同时处理多条消息？
- [Composed Message Processor](https://www.enterpriseintegrationpatterns.com/patterns/messaging/DistributionAggregate.html) - 当处理由多个元素组成的消息（每个元素可能需要不同的处理）时，如何维护整体消息流？
- [Content Enricher](https://www.enterpriseintegrationpatterns.com/patterns/messaging/DataEnricher.html) - 如果消息发起者没有提供所有必需的数据项，我们如何与另一个系统通信？
- [Content Filter](https://www.enterpriseintegrationpatterns.com/patterns/messaging/ContentFilter.html) - 当您只对少数数据项感兴趣时，如何简化对大消息的处理？
- [Content-Based Router](https://www.enterpriseintegrationpatterns.com/patterns/messaging/ContentBasedRouter.html) - 我们如何处理单个逻辑功能（例如库存检查）的实现分布在多个物理系统上的情况？
- [Control Bus](https://www.enterpriseintegrationpatterns.com/patterns/messaging/ControlBus.html) - 我们如何有效地管理分布在多个平台和广泛地理区域的消息系统？
- [Correlation Identifier](https://www.enterpriseintegrationpatterns.com/patterns/messaging/CorrelationIdentifier.html) - 收到回复的请求者如何知道这是针对哪个请求的回复？
- [Datatype Channel](https://www.enterpriseintegrationpatterns.com/patterns/messaging/DatatypeChannel.html) - 应用程序如何发送数据项以便接收者知道如何处理它？
- [Dead Letter Channel](https://www.enterpriseintegrationpatterns.com/patterns/messaging/DeadLetterChannel.html) - 消息系统将如何处理它无法传递的消息？
- [Detour](https://www.enterpriseintegrationpatterns.com/patterns/messaging/Detour.html) - 如何通过中间步骤路由消息以执行验证、测试或调试功能？
- [Document Message](https://www.enterpriseintegrationpatterns.com/patterns/messaging/DocumentMessage.html) - 如何使用消息传递在应用程序之间传输数据？
- [Durable Subscriber](https://www.enterpriseintegrationpatterns.com/patterns/messaging/DurableSubscription.html) - 订阅者在没有监听消息时如何避免丢失消息？
- [Dynamic Router](https://www.enterpriseintegrationpatterns.com/patterns/messaging/DynamicRouter.html) - 如何避免路由器对所有可能目的地的依赖，同时保持其效率？
- [Envelope Wrapper](https://www.enterpriseintegrationpatterns.com/patterns/messaging/EnvelopeWrapper.html) - 现有系统如何参与对消息格式（例如消息头字段或加密）提出特定要求的消息交换？
- [Event Message](https://www.enterpriseintegrationpatterns.com/patterns/messaging/EventMessage.html) - 如何使用消息传递将事件从一个应用程序传输到另一个应用程序？
- [Event-Driven Consumer](https://www.enterpriseintegrationpatterns.com/patterns/messaging/EventDrivenConsumer.html) - 应用程序如何在消息可用时自动使用消息？
- [Format Indicator](https://www.enterpriseintegrationpatterns.com/patterns/messaging/FormatIndicator.html) - 如何设计消息的数据格式以适应未来可能的变化？
- [Guaranteed Delivery](https://www.enterpriseintegrationpatterns.com/patterns/messaging/GuaranteedMessaging.html) - 即使消息系统出现故障，发送者如何确保消息能够送达？
- [Idempotent Receiver](https://www.enterpriseintegrationpatterns.com/patterns/messaging/IdempotentReceiver.html) - 消息接收者如何处理重复的消息？
- [Invalid Message Channel](https://www.enterpriseintegrationpatterns.com/patterns/messaging/InvalidMessageChannel.html) - 消息接收者如何优雅地处理接收到的毫无意义的消息？
- [Message](https://www.enterpriseintegrationpatterns.com/patterns/messaging/Message.html) - 通过消息通道连接的两个应用程序如何交换信息？
- [Message Dispatcher](https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessageDispatcher.html) - 单个通道上的多个消费者如何协调他们的消息处理？
- [Message Expiration](https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessageExpiration.html) - 发送者如何指示消息何时应被视为过时，从而不应被处理？
- [Message Translator](https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessageTranslator.html) - 使用不同数据格式的系统如何通过消息传递相互通信？
- [Message Broker](https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessageBroker.html) - 如何将消息的目的地与发送者分离并保持对消息流的集中控制？
- [Message Bus](https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessageBus.html) - 什么是一种架构，可以使单独的应用程序能够以解耦的方式协同工作，以便可以轻松添加或删除应用程序而不影响其他应用程序？
- [Message Channel](https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessageChannel.html) - 一个应用程序如何使用消息传递与另一个应用程序进行通信？
- [Message Endpoint](https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessageEndpoint.html) - 应用程序如何连接到消息传递通道来发送和接收消息？
- [Message Filter](https://www.enterpriseintegrationpatterns.com/patterns/messaging/Filter.html) - 组件如何避免接收无趣的消息？
- [Message History](https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessageHistory.html) - 如何有效地分析和调试松耦合系统中的消息流？
- [Message Router](https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessageRouter.html) - 如何解耦各个处理步骤，以便消息可以根据一组条件传递到不同的过滤器？
- [Message Sequence](https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessageSequence.html) - 消息传递如何传输任意大量的数据？
- [Message Store](https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessageStore.html) - 我们如何在不影响消息传递系统的松散耦合和瞬态性质的情况下报告消息信息？
- [Messaging Bridge](https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessagingBridge.html) - 如何连接多个消息传递系统，以便一个系统上可用的消息在其他系统上也可用？
- [Messaging Gateway](https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessagingGateway.html) - 如何封装应用程序其余部分对消息传递系统的访问？
- [Messaging Mapper](https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessagingMapper.html) - 如何在域对象和消息传递基础设施之间移动数据，同时保持两者相互独立？
- [Normalizer](https://www.enterpriseintegrationpatterns.com/patterns/messaging/Normalizer.html) - 如何处理语义上相同但以不同格式到达的消息？
- [Pipes and Filters](https://www.enterpriseintegrationpatterns.com/patterns/messaging/PipesAndFilters.html) - 如何对消息进行复杂的处理，同时又保持独立性和灵活性？
- [Point-to-Point Channel](https://www.enterpriseintegrationpatterns.com/patterns/messaging/PointToPointChannel.html) - 呼叫者如何确定只有一位接收者会收到文档或执行呼叫？
- [Polling Consumer](https://www.enterpriseintegrationpatterns.com/patterns/messaging/PollingConsumer.html) - 当应用程序准备就绪时，应用程序如何消费消息？
- [Process Manager](https://www.enterpriseintegrationpatterns.com/patterns/messaging/ProcessManager.html) - 当所需的步骤在设计时可能未知并且可能不连续时，我们如何通过多个处理步骤路由消息？
- [Publish-Subscribe Channel](https://www.enterpriseintegrationpatterns.com/patterns/messaging/PublishSubscribeChannel.html) - 发送者如何向所有感兴趣的接收者广播事件？
- [Recipient List](https://www.enterpriseintegrationpatterns.com/patterns/messaging/RecipientList.html) - 我们如何将消息路由到动态指定的收件人列表？
- [Request-Reply](https://www.enterpriseintegrationpatterns.com/patterns/messaging/RequestReply.html) - 当应用程序发送消息时，如何从接收者那里得到响应？
- [Resequencer](https://www.enterpriseintegrationpatterns.com/patterns/messaging/Resequencer.html) - 我们如何才能将相关但无序的消息流恢复到正确的顺序？
- [Return Address](https://www.enterpriseintegrationpatterns.com/patterns/messaging/ReturnAddress.html) - 回复者如何知道将回复发送到哪里？
- [Routing Slip](https://www.enterpriseintegrationpatterns.com/patterns/messaging/RoutingTable.html) - 当步骤顺序在设计时未知并且每个消息可能有所不同时，我们如何通过一系列处理步骤连续路由消息？
- [Scatter-Gather](https://www.enterpriseintegrationpatterns.com/patterns/messaging/BroadcastAggregate.html) - 当消息需要发送给多个收件人且每个收件人都可能发送回复时，如何维护整体消息流？
- [Selective Consumer](https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessageSelector.html) - 消息消费者如何选择它希望接收哪些消息？
- [Service Activator](https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessagingAdapter.html) - 应用程序如何设计可通过各种消息传递技术和非消息传递技术调用的服务？
- [Smart Proxy](https://www.enterpriseintegrationpatterns.com/patterns/messaging/SmartProxy.html) - 如何跟踪向请求者指定的返回地址发布回复消息的服务上的消息？
- [Splitter](https://www.enterpriseintegrationpatterns.com/patterns/messaging/Sequencer.html) - 如果消息包含多个元素，并且每个元素可能必须以不同的方式处理，我们如何处理它？
- [Test Message](https://www.enterpriseintegrationpatterns.com/patterns/messaging/TestMessage.html) - 但是，如果组件正在主动处理消息，但由于内部故障而导致传出消息出现乱码，会发生什么情况？
- [Transactional Client](https://www.enterpriseintegrationpatterns.com/patterns/messaging/TransactionalClient.html) - 客户端如何通过消息系统控制其交易？
- [Wire Tap](https://www.enterpriseintegrationpatterns.com/patterns/messaging/WireTap.html) - 如何检查在点对点通道上传输的消息？

<!--lint disable-->
**[⬆ 回到顶部](#contents)**
<!--lint enable-->
### 集成架构模式
*用于以高效、无缝的方式连接系统和应用程序的设计模式。*
- [API-led Connectivity pattern](https://github.com/chanakaudaya/solution-architecture-patterns/blob/master/vendor-neutral/API-led-Connectivity-Pattern.md) - 使用API连接不同的系统和应用程序。
- [Anti Corruption Layer Pattern](https://github.com/chanakaudaya/solution-architecture-patterns/blob/master/vendor-neutral/Anti-Corruption-Layer-Pattern.md) - 添加一个层来隔离和转换系统之间的数据。
- [Change Data Capture Pattern](https://github.com/chanakaudaya/solution-architecture-patterns/blob/master/vendor-neutral/Introduction-to-Change-Data-Capture.md) - 实时捕获并传播对数据库或数据源所做的更改。
- [Hybrid API Management pattern](https://github.com/chanakaudaya/solution-architecture-patterns/blob/master/vendor-neutral/Hybrid-API-Management-Pattern.md) - 使用中央控制平面管理跨越云和本地环境的 API。
- [Hybrid Integration pattern](https://github.com/chanakaudaya/solution-architecture-patterns/blob/master/vendor-neutral/Hybrid-Integration-Pattern.md) - 使用集成技术组合来集成部署在本地和云中的系统和应用程序。

<!--lint disable-->
**[⬆ 回到顶部](#contents)**
<!--lint enable-->
### 微服务 API 模式
*MAP（微服务 API 模式）是针对设计、实现和维护基于消息的 API 时遇到的常见问题的一组经过验证的解决方案。它重点关注 API 调用期间交换的消息表示或有效负载及其对 API 的设计和运行时质量的影响。 API 规范和实施的正确管理对于其长期维护至关重要。*
- 基金会
    - [Frontend Integration](https://microservice-api-patterns.org/patterns/foundation/FrontendIntegration) - 物理上与服务器端业务逻辑和数据存储分离的客户端最终用户界面如何使用计算结果、数据源中搜索的结果集以及有关数据实体的详细信息进行填充和更新？应用程序前端如何调用后端中的活动或向后端上传数据？
    - [Backend Integration](https://microservice-api-patterns.org/patterns/foundation/BackendIntegration) - 独立构建并单独部署的分布式应用程序及其部件如何交换数据并触发相互活动，同时保持系统内部概念完整性，而不引入不需要的耦合？
    - [Public API](https://microservice-api-patterns.org/patterns/foundation/PublicAPI) - 如何向组织外部分布在全球、国家和/或地区的无限和/或未知数量的 API 客户端提供 API？
    - [Community API](https://microservice-api-patterns.org/patterns/foundation/CommunityAPI) - 如何将 API 的可见性和访问权限限制为一个封闭的用户组，该用户组不为单个组织单位工作，而是为多个法人实体（例如公司、非营利/非政府组织和政府）工作？
    - [Solution-Internal API](https://microservice-api-patterns.org/patterns/foundation/SolutionInternalAPI) - 如何将 API 的访问和使用限制为应用程序，例如同一或另一个逻辑层和/或物理层中的组件？
    - [API Description](https://microservice-api-patterns.org/patterns/foundation/APIDescription) - API 提供商与其客户之间应共享哪些知识？这些知识应该如何记录？

- 责任
- 端点角色
        - [Processing Resource](https://microservice-api-patterns.org/patterns/responsibility/endpointRoles/ProcessingResource) - API 提供商如何允许其客户端触发其中的操作？
        - [Information Holder Resource](https://microservice-api-patterns.org/patterns/responsibility/endpointRoles/InformationHolderResource) - 如何在 API 中公开领域数据，但其实现仍然隐藏？ API 如何公开数据实体，以便 API 客户端可以同时访问和/或修改这些实体，而不影响数据完整性和质量？
- 运营职责
        - [State Creation Operation](https://microservice-api-patterns.org/patterns/responsibility/operationResponsibilities/StateCreationOperation) - API 提供商如何允许其客户报告提供商需要了解的事件（例如，触发即时或稍后处理）？
        - [Retrieval Operation](https://microservice-api-patterns.org/patterns/responsibility/operationResponsibilities/RetrievalOperation) - 如何检索远程方（即 API 提供商）提供的信息以满足最终用户的信息需求或允许进一步的客户端处理？
        - [State Transition Operation](https://microservice-api-patterns.org/patterns/responsibility/operationResponsibilities/StateTransitionOperation) - 客户端如何发起导致提供者端应用程序状态更改的处理操作？ API 客户端和 API 提供商如何分担执行和控制业务流程及其活动所需的责任？
        - [Computation Function](https://microservice-api-patterns.org/patterns/responsibility/operationResponsibilities/ComputationFunction) - 客户端如何调用提供者端的无副作用远程处理以根据其输入计算结果？
- 信息持有者类型
        - [Operational Data Holder](https://microservice-api-patterns.org/patterns/responsibility/informationHolderEndpointTypes/OperationalDataHolder) - API 如何支持想要创建、读取、更新和/或删除代表操作数据的域实体实例的客户端：这些数据的生命周期相当短暂，在日常业务操作期间经常更改，并且具有许多传出关系？
        - [Master Data Holder](https://microservice-api-patterns.org/patterns/responsibility/informationHolderEndpointTypes/MasterDataHolder) - 如何设计一个 API，提供对长期存在、不经常更改且会被许多客户端引用的主数据的访问？
        - [Reference Data Holder](https://microservice-api-patterns.org/patterns/responsibility/informationHolderEndpointTypes/ReferenceDataHolder) - 在 API 端点中应该如何处理在许多地方引用、寿命较长且对客户端不可变的数据？如何在对处理资源或信息持有者资源的请求和响应中使用此类参考数据？
        - [Link Lookup Resource](https://microservice-api-patterns.org/patterns/responsibility/informationHolderEndpointTypes/LinkLookupResource) - 消息表示如何引用其他可能很多且经常更改的 API 端点和操作，而不将消息接收者绑定到这些端点的实际地址？
        - [Data Transfer Resource](https://microservice-api-patterns.org/patterns/responsibility/informationHolderEndpointTypes/DataTransferResource) - 两个或多个通信参与者如何在彼此不认识、无法同时可用的情况下交换数据，即使数据在其接收者为人所知之前就已发送？
- 结构
- 表示元素
        - [Atomic Parameter](https://microservice-api-patterns.org/patterns/structure/representationElements/AtomicParameter) - 如何在 API 客户端和 API 提供者之间交换简单的非结构化数据（例如数字、字符串、布尔值或二进制数据块）？
        - [Atomic Parameter List](https://microservice-api-patterns.org/patterns/structure/representationElements/AtomicParameterList) - 如何将多个相关的原子参数组合在一个表示元素中，以便每个参数保持简单，但它们的相关性在 API 描述和运行时消息交换中变得明确？
        - [Parameter Tree](https://microservice-api-patterns.org/patterns/structure/representationElements/ParameterTree) - 当定义复杂的表示元素并在运行时交换此类相关元素时，如何表达包含关系？
        - [Parameter Forest](https://microservice-api-patterns.org/patterns/structure/representationElements/ParameterForest) - 如何将多个参数树公开为 API 操作的请求或响应负载？
- 元素刻板印象
        - [Data Element](https://microservice-api-patterns.org/patterns/structure/elementStereotypes/DataElement) - 如何在 API 客户端和 API 提供者之间交换域/应用程序级信息，而不暴露 API 中的提供者内部数据定义？从数据管理的角度来看，API客户端和API提供者如何解耦？
        - [Metadata Element](https://microservice-api-patterns.org/patterns/structure/elementStereotypes/MetadataElement) - 如何使用附加信息来丰富消息，以便接收者可以正确解释消息内容，而不必对数据语义的假设进行硬编码？
        - [Id Element](https://microservice-api-patterns.org/patterns/structure/elementStereotypes/IdElement) - 如何在设计时和运行时区分 API 元素？当应用领域驱动设计时，如何识别已发布语言的元素？
        - [Link Element](https://microservice-api-patterns.org/patterns/structure/elementStereotypes/LinkElement) - 如何在请求和响应消息负载中引用 API 端点和操作，以便可以远程调用它们？
- 特殊目的代表
        - [API Key](https://microservice-api-patterns.org/patterns/structure/specialPurposeRepresentations/APIKey) - API 提供商如何识别和验证客户及其请求？
        - [Error Report](https://microservice-api-patterns.org/patterns/structure/specialPurposeRepresentations/ErrorReport) - API 提供商如何通知其客户有关通信和处理故障的信息？如何使这些信息独立于底层通信技术和平台（例如，表示状态代码的协议级标头）？
        - [Context Representation](https://microservice-api-patterns.org/patterns/structure/specialPurposeRepresentations/ContextRepresentation) - API 使用者和提供者如何在不依赖任何特定远程协议的情况下交换上下文信息？如何使请求中的身份信息和质量属性对对话中的相关后续请求可见？
- 质量
- 参考管理
        - [Embedded Entity](https://microservice-api-patterns.org/patterns/quality/referenceManagement/EmbeddedEntity) - 当接收者需要了解多个相关信息元素时，如何避免发送多条消息？
        - [Linked Information Holder](https://microservice-api-patterns.org/patterns/quality/referenceManagement/LinkedInformationHolder) - 即使 API 处理相互引用的多个信息元素，如何才能保持消息较小？
- 数据传输简约
        - [Pagination](https://microservice-api-patterns.org/patterns/quality/dataTransferParsimony/Pagination) - API 提供商如何在不压倒客户的情况下提供大量结构化数据？
        - [Wish List](https://microservice-api-patterns.org/patterns/quality/dataTransferParsimony/WishList) - API 客户端如何在运行时告知 API 提供者其感兴趣的数据？
        - [Wish Template](https://microservice-api-patterns.org/patterns/quality/dataTransferParsimony/WishTemplate) - API 客户端如何向 API 提供者通知其感兴趣的嵌套数据？如何灵活、动态地表达这种偏好？
        - [Conditional Request](https://microservice-api-patterns.org/patterns/quality/dataTransferParsimony/ConditionalRequest) - 当频繁调用返回很少变化的数据的 API 操作时，如何避免不必要的服务器端处理和带宽使用？
        - [Request Bundle](https://microservice-api-patterns.org/patterns/quality/dataTransferParsimony/RequestBundle) - 如何减少请求和响应的数量，提高通信效率？

- 质量管理和治理
        - [Pricing Plan](https://microservice-api-patterns.org/patterns/quality/qualityManagementAndGovernance/PricingPlan) - API 提供商如何计量 API 服务的消耗并对其进行收费？
        - [Rate Limit](https://microservice-api-patterns.org/patterns/quality/qualityManagementAndGovernance/RateLimit) - API 提供商如何防止 API 客户端过度使用 API？
        - [Service Level Agreement](https://microservice-api-patterns.org/patterns/quality/qualityManagementAndGovernance/ServiceLevelAgreement) - API 客户端如何了解 API 及其端点操作的特定服务质量特征？如何以可衡量的方式定义和传达这些特征以及不满足这些特征的后果？

- 进化
    - [Version Identifier](https://microservice-api-patterns.org/patterns/evolution/VersionIdentifier) - API 提供商如何向客户端表明其当前功能以及可能存在不兼容的更改，以防止由于未发现的解释错误而导致客户端故障？
    - [Semantic Versioning](https://microservice-api-patterns.org/patterns/evolution/SemanticVersioning) - 利益相关者如何比较 API 版本以立即检测它们是否兼容？
    - [Two In Production](https://microservice-api-patterns.org/patterns/evolution/TwoInProduction) - 提供商如何在不破坏现有客户端且无需在生产中维护大量 API 版本的情况下逐步更新 API？
    - [Aggressive Obsolescence](https://microservice-api-patterns.org/patterns/evolution/AggressiveObsolescence) - API 提供商如何在保证服务质量水平的情况下减少维护整个 API 或其部分（例如端点、操作或消息表示）的工作量？
    - [Experimental Preview](https://microservice-api-patterns.org/patterns/evolution/ExperimentalPreview) - 提供商如何才能在引入新 API 或新 API 版本时降低客户的风险，并获得早期采用者的反馈，而不必过早冻结 API 设计？
    - [Limited Lifetime Guarantee](https://microservice-api-patterns.org/patterns/evolution/LimitedLifetimeGuarantee) - 提供商如何让客户知道他们可以依赖已发布版本的 API 多长时间？
    - [Eternal Lifetime Guarantee](https://microservice-api-patterns.org/patterns/evolution/EternalLifetimeGuarantee) - 提供商如何支持无法或不愿意迁移到较新 API 版本的客户？

<!--lint disable-->
**[⬆ 回到顶部](#contents)**
<!--lint enable-->
### SOA模式
*SOA 模式是设计解决方案，为开发灵活且可重用的面向服务的应用程序提供指南和最佳实践。这些模式解决了面向服务的应用程序设计的各个方面，包括服务识别、交互、组合和粒度。*
- 基本库存模式
   - [Canonical Protocol](https://patterns.arcitura.com/soa-patterns/design_patterns/canonical_protocol) - 定义服务之间的通用通信协议以实现互操作性和解耦。
   - [Canonical Schema](https://patterns.arcitura.com/soa-patterns/design_patterns/canonical_schema) - 定义用于在服务之间交换数据的标准数据模型和格式。
   - [Domain Inventory](https://patterns.arcitura.com/soa-patterns/design_patterns/domain_inventory) - 识别特定域内的服务类型并对其进行分类。
   - [Enterprise Inventory](https://patterns.arcitura.com/soa-patterns/design_patterns/enterprise_inventory) - 建立单一的、企业范围的服务清单，以最大限度地重用和重组。
   - [Logic Centralization](https://patterns.arcitura.com/soa-patterns/design_patterns/logic_centralization) - 将业务逻辑集中在服务层内，以减少冗余并提高一致性。
   - [Service Layers](https://patterns.arcitura.com/soa-patterns/design_patterns/service_layers) - 根据服务封装的逻辑类型将服务组织为逻辑层。
   - [Service Normalization](https://patterns.arcitura.com/soa-patterns/design_patterns/service_normalization) - 确保库存内的服务边界不重叠，避免冗余功能。

- 逻辑库存层模式
   - [Entity Abstraction](https://patterns.arcitura.com/soa-patterns/design_patterns/entity_abstraction) - 抽象数据实体以简化数据访问并减少耦合。
   - [Process Abstraction](https://patterns.arcitura.com/soa-patterns/design_patterns/process_abstraction) - 抽象流程以提高可重用性和可维护性。
   - [Utility Abstraction](https://patterns.arcitura.com/soa-patterns/design_patterns/utility_abstraction) - 抽象通用实用程序以减少重复并提高一致性。
   - [Micro Task Abstraction](https://patterns.arcitura.com/soa-patterns/design_patterns/micro_task_abstraction) - 将任务分解为更小、更精细的任务，以便于管理。

- 库存集中模式
   - [Policy Centralization](https://patterns.arcitura.com/soa-patterns/design_patterns/policy_centralization) - 集中策略以减少重复并提高一致性。
   - [Process Centralization](https://patterns.arcitura.com/soa-patterns/design_patterns/process_centralization) - 集中流程以提高可重用性和可维护性。
   - [Rules Centralization](https://patterns.arcitura.com/soa-patterns/design_patterns/rules_centralization) - 集中业务规则以减少重复并促进一致性。
   - [Schema Centralization](https://patterns.arcitura.com/soa-patterns/design_patterns/schema_centralization) - 集中数据模式以减少重复并提高一致性。

- 库存实施模式
   - [Canonical Resources](https://patterns.arcitura.com/soa-patterns/design_patterns/canonical_resources) - 为跨服务的通用功能定义一组标准资源。
   - [Cross-Domain Utility Layer](https://patterns.arcitura.com/soa-patterns/design_patterns/cross_domain_utility_layer) - 建立跨多个域清单共享的通用实用程序服务层。
   - [Dual Protocols](https://patterns.arcitura.com/soa-patterns/design_patterns/dual_protocols) - 允许服务清单支持两种通信协议以平衡互操作性和性能。
   - [Inventory Endpoint](https://patterns.arcitura.com/soa-patterns/design_patterns/inventory_endpoint) - 定义用于访问库存资源的标准端点。
   - [Service Grid](https://patterns.arcitura.com/soa-patterns/design_patterns/service_grid) - 提供用于管理和扩展服务的框架。
   - [State Repository](https://patterns.arcitura.com/soa-patterns/design_patterns/state_repository) - 存储和管理服务状态信息。
   - [Stateful Services](https://patterns.arcitura.com/soa-patterns/design_patterns/stateful_services) - 维护跨服务调用的状态信息。
   - [Augmented Protocols](https://patterns.arcitura.com/soa-patterns/design_patterns/augmented_protocols) - 通过附加功能增强协议。

- 库存治理模式
   - [Canonical Expression](https://patterns.arcitura.com/soa-patterns/design_patterns/canonical_expression) - 定义库存数据的标准表达语言。
   - [Canonical Versioning](https://patterns.arcitura.com/soa-patterns/design_patterns/canonical_versioning) - 定义库存资源的标准版本控制方案。
   - [Metadata Centralization](https://patterns.arcitura.com/soa-patterns/design_patterns/metadata_centralization) - 集中元数据以减少重复并提高一致性。

- 基础服务模式
   - [Agnostic Capability](https://patterns.arcitura.com/soa-patterns/design_patterns/agnostic_capability) - 抽象服务功能以提高灵活性。
   - [Agnostic Context](https://patterns.arcitura.com/soa-patterns/design_patterns/agnostic_context) - 抽象服务上下文以提高灵活性。
   - [Functional Decomposition](https://patterns.arcitura.com/soa-patterns/design_patterns/functional_decomposition) - 将服务分解为更小、更易于管理的组件。
   - [Non-Agnostic Context](https://patterns.arcitura.com/soa-patterns/design_patterns/non_agnostic_context) - 将单一用途、不可重用的逻辑封装在专用服务中，以便仍然可以在清单中对其进行管理。
   - [Service Encapsulation](https://patterns.arcitura.com/soa-patterns/design_patterns/service_encapsulation) - 封装服务功能以提高可维护性。

- 服务实施模式
   - [Partial State Deferral](https://patterns.arcitura.com/soa-patterns/design_patterns/partial_state_deferral) - 暂时推迟部分服务状态数据以优化内存和资源消耗。
   - [Partial Validation](https://patterns.arcitura.com/soa-patterns/design_patterns/partial_validation) - 仅验证相关数据以提高性能。
   - [Redundant Implementation](https://patterns.arcitura.com/soa-patterns/design_patterns/redundant_implementation) - 实现服务的多个版本以提高灵活性。
   - [Service Data Replication](https://patterns.arcitura.com/soa-patterns/design_patterns/service_data_replication) - 跨多个服务复制数据以提高性能。
   - [Service Façade](https://patterns.arcitura.com/soa-patterns/design_patterns/service_facade) - 为复杂的服务提供简化的界面，以提高可用性。
   - [UI Mediator](https://patterns.arcitura.com/soa-patterns/design_patterns/ui_mediator) - 在用户界面和底层服务之间进行中介以提高可用性。
   - [Reference Data Centralization](https://patterns.arcitura.com/soa-patterns/design_patterns/reference_data_centralization) - 集中参考数据以减少重复并提高一致性。
   - [Microservice Deployment](https://patterns.arcitura.com/soa-patterns/design_patterns/microservice_deployment) - 将服务部署为独立、自治的单元，以提高可扩展性和弹性。
   - [Containerization](https://patterns.arcitura.com/soa-patterns/design_patterns/containerization) - 如何为具有高性能恢复和可扩展性要求的服务提供最大支持的环境？

- 服务安全模式
   - [Exception Shielding](https://patterns.arcitura.com/soa-patterns/design_patterns/exception_shielding) - 通过正确处理异常来防止安全漏洞。
   - [Message Screening](https://patterns.arcitura.com/soa-patterns/design_patterns/message_screening) - 筛选消息中是否存在恶意内容。
   - [Service Perimeter Guard](https://patterns.arcitura.com/soa-patterns/design_patterns/service_perimeter_guard) - 保护服务边界以防止未经授权的访问。
   - [Trusted Subsystem](https://patterns.arcitura.com/soa-patterns/design_patterns/trusted_subsystem) - 在子系统之间建立信任以提高安全性。

- 服务契约设计模式
   - [Concurrent Contracts](https://patterns.arcitura.com/soa-patterns/design_patterns/concurrent_contracts) - 允许服务合同的多个版本同时共存。
   - [Contract Centralization](https://patterns.arcitura.com/soa-patterns/design_patterns/contract_centralization) - 集中服务合同以提高一致性并减少重复。
   - [Contract Denormalization](https://patterns.arcitura.com/soa-patterns/design_patterns/contract_denormalization) - 允许服务合同包含冗余功能，以满足具有不同数据交换要求的消费者。
   - [Decoupled Contract](https://patterns.arcitura.com/soa-patterns/design_patterns/decoupled_contract) - 将服务合同与其实施分离，以提高灵活性。
   - [Validation Abstraction](https://patterns.arcitura.com/soa-patterns/design_patterns/validation_abstraction) - 抽象验证逻辑以提高可重用性和可维护性。

- 遗留封装模式
   - [File Gateway](https://patterns.arcitura.com/soa-patterns/design_patterns/file_gateway) - 提供访问旧版基于文件的系统的网关。
   - [Legacy Wrapper](https://patterns.arcitura.com/soa-patterns/design_patterns/legacy_wrapper) - 包装遗留系统以将其作为服务公开。
   - [Multi-Channel Endpoint](https://patterns.arcitura.com/soa-patterns/design_patterns/multi_channel_endpoint) - 提供多个通信通道来访问遗留系统。

- 服务治理模式
   - [Compatible Change](https://patterns.arcitura.com/soa-patterns/design_patterns/compatible_change) - 允许在不破坏现有客户端的情况下更改服务。
   - [Decomposed Capability](https://patterns.arcitura.com/soa-patterns/design_patterns/decomposed_capability) - 将服务功能分解为更小、更易于管理的部分。
   - [Distributed Capability](https://patterns.arcitura.com/soa-patterns/design_patterns/distributed_capability) - 将服务功能分解为更小、更易于管理的部分。
   - [Proxy Capability](https://patterns.arcitura.com/soa-patterns/design_patterns/proxy_capability) - 提供远程服务代理功能，以提高性能并减少网络开销。
   - [Service Decomposition](https://patterns.arcitura.com/soa-patterns/design_patterns/service_decomposition) - 将整体服务分解为更小、更易于管理的部分。
   - [Service Refactoring](https://patterns.arcitura.com/soa-patterns/design_patterns/service_refactoring) - 重构服务以改进其设计和性能。
   - [Termination Notification](https://patterns.arcitura.com/soa-patterns/design_patterns/termination_notification) - 通知客户服务终止。
   - [Version Identification](https://patterns.arcitura.com/soa-patterns/design_patterns/version_identification) - 标识服务的版本。

- 能力构成模式
   - [Capability Composition](https://patterns.arcitura.com/soa-patterns/design_patterns/capability_composition) - 将多种服务能力结合起来，创造出一种新的能力。
   - [Capability Recomposition](https://patterns.arcitura.com/soa-patterns/design_patterns/capability_recomposition) - 重组现有的服务能力以创建新的能力。

- 服务消息传递模式
   - [Asynchronous Queuing](https://patterns.arcitura.com/soa-patterns/design_patterns/asynchronous_queuing) - 使用消息队列来解耦服务，提高可扩展性和可靠性。
   - [Event-Driven Messaging](https://patterns.arcitura.com/soa-patterns/design_patterns/event_driven_messaging) - 使用事件触发服务调用，减少耦合。
   - [Intermediate Routing](https://patterns.arcitura.com/soa-patterns/design_patterns/intermediate_routing) - 使用中间路由节点来提高性能和灵活性。
   - [Messaging Metadata](https://patterns.arcitura.com/soa-patterns/design_patterns/messaging_metadata) - 使用元数据来描述和管理服务消息。
   - [Reliable Messaging](https://patterns.arcitura.com/soa-patterns/design_patterns/reliable_messaging) - 确保分布式环境中的消息传递和可靠性。
   - [Service Agent](https://patterns.arcitura.com/soa-patterns/design_patterns/service_agent) - 充当远程服务的代理以提高性能并减少网络开销。
   - [Service Callback](https://patterns.arcitura.com/soa-patterns/design_patterns/service_callback) - 使用回调在服务之间进行通信。
   - [Service Instance Routing](https://patterns.arcitura.com/soa-patterns/design_patterns/service_instance_routing) - 基于服务实例路由消息以提高性能和可扩展性。
   - [Service Messaging](https://patterns.arcitura.com/soa-patterns/design_patterns/service_messaging) - 描述服务之间的通信。
   - [State Messaging](https://patterns.arcitura.com/soa-patterns/design_patterns/state_messaging) - 使用消息来管理分布式环境中的状态信息。

- 组合实现模式
   - [Agnostic Sub-Controller](https://patterns.arcitura.com/soa-patterns/design_patterns/agnostic_sub_controller) - 将子控制器与主控制器分离，以提高可重用性和可维护性。
   - [Atomic Service Transaction](https://patterns.arcitura.com/soa-patterns/design_patterns/atomic_service_transaction) - 使用事务来确保多个服务调用之间的原子性和一致性。
   - [Compensating Service Transaction](https://patterns.arcitura.com/soa-patterns/design_patterns/compensating_service_transaction) - 扭转失败交易的影响。
   - [Composition Autonomy](https://patterns.arcitura.com/soa-patterns/design_patterns/composition_autonomy) - 使服务能够在组合内自主运行。

- 服务交互安全模式
   - [Brokered Authentication](https://patterns.arcitura.com/soa-patterns/design_patterns/brokered_authentication) - 通过经纪人对客户进行身份验证。
   - [Data Confidentiality](https://patterns.arcitura.com/soa-patterns/design_patterns/data_confidentiality) - 确保分布式环境中的数据机密性。
   - [Data Origin Authentication](https://patterns.arcitura.com/soa-patterns/design_patterns/data_origin_authentication) - 验证消息的来源。
   - [Direct Authentication](https://patterns.arcitura.com/soa-patterns/design_patterns/direct_authentication) - 直接对客户端进行身份验证。

- 转型模式
   - [Data Format Transformation](https://patterns.arcitura.com/soa-patterns/design_patterns/data_format_transformation) - 转换数据格式以实现互操作性。
   - [Data Model Transformation](https://patterns.arcitura.com/soa-patterns/design_patterns/data_model_transformation) - 转换数据模型以实现互操作性。
   - [Protocol Bridging](https://patterns.arcitura.com/soa-patterns/design_patterns/protocol_bridging) - 不同协议之间的桥梁以实现互操作性。

- REST 启发的模式
   - [Entity Linking](https://patterns.arcitura.com/soa-patterns/design_patterns/entity_linking) - 链接相关资源以实现导航和发现。
   - [Lightweight Endpoint](https://patterns.arcitura.com/soa-patterns/design_patterns/lightweight_endpoint) - 为资源访问提供轻量级端点。
   - [Reusable Contract](https://patterns.arcitura.com/soa-patterns/design_patterns/reusable_contract) - 重用通用合约以提高一致性并减少重复。
   - [Content Negotiation](https://patterns.arcitura.com/soa-patterns/design_patterns/content_negotiation) - 协商客户端和服务器之间的内容格式。
   - [Endpoint Redirection](https://patterns.arcitura.com/soa-patterns/design_patterns/endpoint_redirection) - 将客户端重定向到替代端点。
   - [Idempotent Capability](https://patterns.arcitura.com/soa-patterns/design_patterns/idempotent_capability) - 确保可以多次执行相同的操作而不更改系统状态。

<!--lint disable-->
**[⬆ 回到顶部](#contents)**
<!--lint enable-->
## 资源
*一些有用的规范、标准、文章和文档。*
### API规范
- [API Blueprint (⭐8.6k)](https://github.com/apiaryio/api-blueprint) - 一种用于设计和记录 API 的强大高级语言，使软件工程师能够轻松协作并创建高效的 API。
- [Arazzo Specification (⭐440)](https://github.com/OAI/Arazzo-Specification) - 一种与编程语言无关的标准表示形式，用于描述 API 调用序列（工作流）及其依赖关系。
- [AsyncAPI (⭐5.2k)](https://github.com/asyncapi/spec) - 开发事件驱动架构 (EDA) 的重要工具，使工程师能够构建更好的工具生态系统。
- [CloudEvents (⭐5.7k)](https://github.com/cloudevents/spec) - 用于以通用格式描述事件数据的规范，以提供跨服务、平台和系统的互操作性。
- [GraphQL (⭐14k)](https://github.com/graphql/graphql-spec) - 用于构建高效 API 的复杂查询语言和运行时，使工程师能够轻松从现有系统检索数据。
- [JSON:API (⭐7.7k)](https://github.com/json-api/json-api) - 用于构建 API 的标准化规范，可简化资源、关系和元数据的表示，使软件工程师更轻松地创建高效的 API。
- [OpenAPI (ex.Swagger) (⭐31k)](https://github.com/OAI/OpenAPI-Specification) - 用于创建 RESTful API 的与语言无关的规范，使人类和机器无需源代码或文档即可理解服务的功能。
- [RAML (⭐3.8k)](https://github.com/raml-org/raml-spec) - 一种 RESTful API 建模语言，允许软件工程师通过对资源、端点和交互进行建模来设计和创建高效的 API。
- [Standard Webhooks (⭐1.6k)](https://github.com/standard-webhooks/standard-webhooks) - 用于轻松、安全、可靠地发送 Webhook 的开源工具和指南。
- [TypeSpec (⭐5.7k)](https://github.com/microsoft/typespec) - 一种高度可扩展的语言，用于描述 API 数据形状和协议，能够编译为 OpenAPI、JSON Schema、Protobuf 和其他格式。
- [WSDL](http://www.w3.org/TR/wsdl20) - 一种强大的基于 XML 的接口描述语言，用于基于 SOAP 的服务，使软件工程师能够描述 Web 服务的功能并自动创建客户端代码。

<!--lint disable-->
**[⬆ 回到顶部](#contents)**
<!--lint enable-->
### API 风格指南
- [API Stylebook](https://apistylebook.com/) - 来自 Atlassian、Cisco 和 Zalando 等公司的公开 API 设计指南集合，由 Arnaud Lauret 策划。
- [Google API Improvement Proposals](https://google.aip.dev/) - 设计文档将 Google 的 API 设计决策编撰成文，为面向资源的 API 提供编号、可引用的指导。
- [Google Cloud API Design Guide](https://cloud.google.com/apis/design) - 网络 API 的通用设计指南，在 Google 内部用于 gRPC 和 REST API。
- [Microsoft REST API Guidelines (⭐23k)](https://github.com/microsoft/api-guidelines) - Microsoft 设计一致的 REST API 的全公司指南，包括 Microsoft Graph 特定的附录。
- [Zalando RESTful API and Event Guidelines](https://opensource.zalando.com/restful-api-guidelines/) - 用于设计 RESTful API 和事件模式的综合性、固执己见的指南，被其他组织广泛重用。

<!--lint disable-->
**[⬆ 回到顶部](#contents)**
<!--lint enable-->
### 文章
- [API-Security-Checklist (⭐23k)](https://github.com/shieldfy/API-Security-Checklist) - 有关 REST API 安全性的最佳实践。
- [建筑风格和
基于网络的软件架构的设计](https://www.ics.uci.edu/~fielding/pubs/dissertation/top.htm) - Roy Fielding 的论文定义了 REST。
- [Enterprise Integration Using REST](http://martinfowler.com/articles/enterpriseREST.html) - 讨论非公共 API 的限制和灵活性，以及​​跨多个团队进行大规模 RESTful 集成的经验教训。
- [Richardson Maturity Model](http://martinfowler.com/articles/richardsonMaturityModel.html) - 由 Martin Fowler 解释，最初由 Leonard Richardson 提出。
- [Web API Design: Crafting interfaces that developers love](https://pages.apigee.com/rs/apigee/images/api-design-ebook-2012-03.pdf) - 为开发人员创建一致、直观且用户友好的 Web API。

<!--lint disable-->
**[⬆ 回到顶部](#contents)**
<!--lint enable-->
### 书籍
- [API Design Patterns](https://www.manning.com/books/api-design-patterns) - JJ Geawax 面向资源的 API 的设计模式目录，涵盖命名、分页、版本控制等。
- [Building Event-Driven Microservices](https://www.oreilly.com/library/view/building-event-driven-microservices/9781492057888/) - Adam Bellemare 通过事件驱动架构大规模利用组织数据的指南。
- [Designing Data-Intensive Applications](https://dataintensive.net/) - Martin Kleppmann 深入探讨了可靠、可扩展和可维护的数据系统背后的思想，包括复制、分区和流处理。
- [Enterprise Integration Patterns](https://www.enterpriseintegrationpatterns.com/) - Gregor Hohpe 和 Bobby Woolf 的 65 种消息传递模式目录；异步集成的基础书籍。
- [Flow Architectures](https://www.oreilly.com/library/view/flow-architectures/9781492075882/) - James Urquhart 谈论流媒体、事件驱动集成的未来及其对业务的影响。
- [Patterns for API Design](https://api-patterns.org/book/) - 这本书是 Olaf Zimmermann 及其合著者所著的《微服务 API 模式语言》的姊妹篇，介绍如何简化与松散耦合消息交换的集成。
- [Principles of Web API Design](https://www.informit.com/store/principles-of-web-api-design-delivering-value-with-9780137355631) - James Higginbotham 的流程驱动方法设计 Web API，从需求到文档提供价值。

<!--lint disable-->
**[⬆ 回到顶部](#contents)**
<!--lint enable-->
### 认证证书
<详情>
<summary>API学院</summary>
  
- [API Designer](https://apiacademy.learnupon.com/lpaths/4147453/courses/262369/details) - 验证您对 API 设计基础知识和最佳实践的理解。
- [API Product Manager](https://apiacademy.learnupon.com/lpaths/4147453/courses/262371/details) - 展示您将 API 作为产品进行管理的熟练程度。
- [API Security Architect](https://apiacademy.learnupon.com/lpaths/4147453/courses/262370/details) - 验证您在使用现代架构保护 API 方面的专业知识。
  
</详情>
<详情>
<summary>APIsec 大学</summary>
  
- [API Documentation Best Practices](https://www.apisecuniversity.com/courses/api-documentation-best-practices) - 这个 2 小时的课程涵盖了创建、自动化和发布开发人员、合作伙伴和用户喜爱的 API 文档所需了解的所有内容。您还将了解为什么 API 文档是强有力的治理、有效的 API 安全性和实现 API 业务目标的基础。
- [API Penetration Testing](https://www.apisecuniversity.com/courses/api-penetration-testing) - API 渗透测试课程涵盖了成为 APIsec 专业人员的所有关键主题。该实践课程包括超过 12 小时的现场指导，并提供有关 API 黑客技术以及如何发现漏洞的详细实验。
- [API Security for PCI Compliance](https://www.apisecuniversity.com/courses/api-security-for-pci-compliance) - 这个时长 60 分钟的课程探讨了新的 PCI DSS 4.0 要求，并详细介绍了 API 合规性安全义务。 DSS 4.0 有史以来引入了 API 安全问题 - 注册以了解这对您的组织有何影响。
- [API Security Fundamentals](https://www.apisecuniversity.com/courses/api-security-fundamentals) - 这个 90 分钟的课程涵盖了 API 的核心威胁以及如何防止违规。了解 OWASP API 安全性 Top 10，检查真实世界的 API 攻击，并了解 API 安全性的 3 个支柱。
- [Certified API Security Analyst](https://www.apisecuniversity.com/courses/certified-api-security-analyst-exam) - CASA 考试旨在测试您在 API 安全威胁、风险和最佳实践方面的专业知识。学生应完成 OWASP API 安全及其他课程！在尝试获得 CASA 认证之前，请先参加课程。
- [OWASP API Security Top 10](https://www.apisecuniversity.com/courses/owasp-api-security-top-10-and-beyond) - 这门 90 分钟的课程深入探讨了 2023 年版 OWASP API 安全前 10 名，并涵盖了未进入前 10 名的关键概念。
- [Securing API Servers](https://www.apisecuniversity.com/courses/securing-api-servers) - 了解确保 API 服务器安全的关键概念 - 从 CORS 到错误处理再到速率限制等。
  
</详情>
<详情>
<摘要>阿波罗</摘要>

- [Apollo Graph Developer - Associate Certification](https://www.apollographql.com/tutorials/exams/apollo-graph-associate) - 获得此认证的开发人员拥有 GraphQL 和 Apollo 工具套件的扎实基础知识，可以设计架构、运行 Apollo Server 4 并在前端使用 Apollo Client 3 执行查询。

- [Apollo Graph Developer - Professional Certification](https://www.apollographql.com/tutorials/certifications/apollo-graph-professional) - 获得此认证的开发人员表明对 Apollo Federation 概念非常熟悉。他们可以应用这些概念来构建联邦超级图或将现有的整体图移动到联邦。

</详情>
<详情>
<摘要>布米</摘要>
  
- [Associate Administrator Certification](https://community.boomi.com/s/learning-plan-detail-standard?ltui__urlRecordId=aOM6S0000008OIKWA2&ltui__urlRedirect=learning-plan-detail-standard) - 验证个人在管理 Boomi 平台方面的基础知识和技能，重点是平台监控、故障排除和安全。
- [Associate Developer Certification](https://community.boomi.com/s/learning-plan-detail-standard?ltui__urlRecordId=aOM6S0000008OIeWAM&ltui__urlRedirect=learning-plan-detail-standard) - 展示考生对使用 Boomi 平台构建和部署集成流程的基本了解，包括设计模式、部署和错误处理。
- [Associate EDI for X12 Certification](https://community.boomi.com/s/learning-plan-detail-standard?ltui__urlRecordId=aOM6S0000008OIFWA2&ltui__urlRedirect=learning-plan-detail-standard) - 验证个人使用 Boomi 设计、开发和管理与 X12 标准的电子数据交换 (EDI) 集成的熟练程度，涵盖 EDI 文档结构和贸易伙伴管理等基本概念。
- [Associate Flow Essentials Certification](https://community.boomi.com/s/learning-plan-detail-standard?ltui__urlRecordId=aOM6S0000008OIZWA2&ltui__urlRedirect=learning-plan-detail-standard) - 展示考生使用 Boomi Flow 创建和管理业务应用程序的知识，重点是工作流设计、用户界面和数据集成。
- [Associate Master Data Hub Certification](https://community.boomi.com/s/learning-plan-detail-standard?ltui__urlRecordId=aOM6S0000008OIPWA2&ltui__urlRedirect=learning-plan-detail-standard) - 强调考生对使用 Boomi Master Data Hub 确保跨系统数据质量和一致性的理解，重点关注数据建模、治理和同步。
- [Development and Application Architecture Certification](https://community.boomi.com/s/learning-plan-detail-standard?ltui__urlRecordId=aOM6S0000008OJOWA2&ltui__urlRedirect=learning-plan-detail-standard) - 确认个人在 Boomi 平台上设计和实施复杂集成解决方案和应用程序架构的专业知识，包括最佳实践和性能优化。
- [Professional API Design Certification](https://community.boomi.com/s/learning-plan-detail-standard?ltui__urlRecordId=aOM6S0000008OKzWAM&ltui__urlRedirect=learning-plan-detail-standard) - 展示考生使用 Boomi 设计、开发和管理 API 的能力，包括 RESTful API 原则、API 安全性和版本控制。
- [Professional API Management Certification](https://community.boomi.com/s/learning-plan-detail-standard?ltui__urlRecordId=aOM6S0000008OIyWAM&ltui__urlRedirect=learning-plan-detail-standard) - 验证个人使用 Boomi 平台管理 API 整个生命周期的专业知识，包括 API 部署、监控和分析。
- [Professional Developer Certification](https://community.boomi.com/s/learning-plan-detail-standard?ltui__urlRecordId=aOM6S0000008OJrWAM&ltui__urlRedirect=learning-plan-detail-standard) - 认可候选人在使用 Boomi 开发、部署和管理集成流程方面的深入知识和技能，重点是高级数据转换和错误处理技术。
- [Professional Flow Developer Certification](https://community.boomi.com/s/learning-plan-detail-standard?ltui__urlRecordId=aOM6S0000008OIUWA2&ltui__urlRedirect=learning-plan-detail-standard) - 展示个人使用 Boomi Flow 设计、开发和管理业务应用程序的高级能力，包括复杂的工作流程设计、自定义 UI 组件以及与外部系统的集成。
- [Professional Linux Operational Administrator Certification](https://community.boomi.com/s/learning-plan-detail-standard?ltui__urlRecordId=aOM6S0000008OI5WAM&ltui__urlRedirect=learning-plan-detail-standard) - 确认考生在 Linux 系统上管理 Boomi 的熟练程度，涵盖系统安装、配置、安全性和性能优化等主题。
- [Professional Windows Operational Administrator Certification](https://community.boomi.com/s/learning-plan-detail-standard?ltui__urlRecordId=aOM6S0000008OIAWA2&ltui__urlRedirect=learning-plan-detail-standard) - 验证个人在 Windows 系统上管理 Boomi 的专业知识，重点关注系统安装、配置、安全性和性能优化。
  
</详情>
<详情>
<摘要>IBM</摘要>
  
- [IBM Certified Solution Developer – App Connect Enterprise V11](https://www.ibm.com/training/certification/C0003107#exam) - 验证您是否具备使用 IBM App Connect V11.0 开发、部署、调整和支持平台无关的消息流应用程序的中级知识和经验。
- [IBM Certified Solution Implementer – API Connect v10.0.3](https://www.ibm.com/training/certification/C0002604#exam) - 展示您使用 IBM API Connect v10.0.3 开发、发布、配置和管理 API 的中级知识和技能。

</详情>
<详情>
<summary>Gravitee</summary>

- [Event-native API Management Foundations](https://gravitee.getlearnworlds.com/course/gravitee-event-native-api-management-foundations) - 事件原生 API 管理基础知识。
- [Event-native API Management Professional](https://gravitee.getlearnworlds.com/course/gravitee-enap-certification) - 重点介绍一些更高级的 API 管理概念，以及有关如何使用 Gravitee API 管理的基础知识。
  
</详情>
<详情>
<摘要>孔</摘要>
  
- [Kong Gateway Certified Associate](https://konghq.com/academy/exam-preparation) - 在 Kong Gateway 上为开发人员、DevOps 和架构师验证您的入门级知识和技能。

</详情>
<详情>
<摘要>Mulesoft</摘要>
  
- [MuleSoft Certified Developer - Level 1](https://training.mulesoft.com/certification/developer-mule4-level1) - 验证您使用 MuleSoft 设计、构建、测试和调试、部署和管理基本 API 和集成的知识和技能。
- [MuleSoft Certified Developer - Level 2](https://training.mulesoft.com/certification/developer-mule4-level2) - 验证您开发可用于生产的 Mule 应用程序的能力，这些应用程序可以解决和平衡关键的非功能性需求，包括监控、性能、可维护性、可靠性和安全性。
- [MuleSoft Certified Integration Architect - Level 1](https://training.mulesoft.com/certification/architect-integration-level1) - 验证您将功能和非功能需求转化为集成接口和实现的知识和技能。
- [MuleSoft Certified Platform Architect - Level 1](https://training.mulesoft.com/certification/architect-platform-level1) - 验证您的知识和技能，以指导使用 Anypoint Platform 在整个组织中通过 API 主导的连接，从各个集成解决方案中建立有效的应用程序网络。

</详情>
<详情>
<摘要>甲骨文</摘要>

- [Oracle Business Process Management Suite 12c Certified Implementation Specialist](https://education.oracle.com/oracle-business-process-management-suite-12c-essentials/pexam_1Z0-435) - 验证您在实施 Oracle BPM Suite 12c 解决方案方面的专业知识。
- [Oracle Cloud Platform Application Integration 2025 Certified Professional](https://education.oracle.com/oracle-cloud-infrastructure-2024-application-integration-professional/pexam_1Z0-1042-25) - 验证您对 Oracle Application Integration 的理解以实施这些云服务。
- [Oracle Data Integrator 12c Certified Implementation Specialist](https://education.oracle.com/oracle-data-integrator-12c-certified-implementation-specialist/trackp_379) - 验证您在销售或实施 Oracle Data Integration 12c 解决方案方面的专业知识。
- [Oracle SOA Suite 12c Certified Implementation Specialist](https://education.oracle.com/oracle-soa-suite-12c-essentials/pexam_1Z0-434) - 验证您在实施基于 Oracle SOA Suite 12c 的解决方案方面的专业知识。

</详情>
<详情>
<摘要>红帽</摘要>
 
- [Red Hat Certified Specialist in API Management](https://www.redhat.com/en/services/certification/red-hat-certified-specialist-api-management) - 验证使用红帽 3scale API 管理平台创建和维护企业 API 的能力。
- [Red Hat Certified Specialist in Business Rules](https://www.redhat.com/en/services/certification/rhcs-business-rules) - 检查使用红帽 JBoss BRMS 执行涉及业务逻辑实施和管理的任务所需的知识、技能和能力。
- [Red Hat Certified Specialist in Cloud-native Integration](https://www.redhat.com/en/services/certification/rhcs-cloud-native-integration) - 验证基于红帽 Fuse、Camel 和 API 创建和维护企业集成服务的能力。
- [Red Hat Certified Specialist in Event-Driven Development with Kafka](https://www.redhat.com/en/services/certification/red-hat-certified-specialist-event-driven-development-kafka) - 验证使用 Apache Kafka 和 Apache Kafka Streams 开发应用程序的能力。
  
</详情>
<详情>
<摘要>SAP</摘要>
  
- [SAP Certified Associate - Integration Developer](https://learning.sap.com/certifications/sap-certified-associate-integration-developer) - 验证候选人是否拥有 SAP Integration Suite 配置文件所需的基础和核心知识。
  
</详情>
<详情>
<摘要>SnapLogic</摘要>

- [SnapLogic Administrator Certification](https://learn.snaplogic.com/snaplogic-administrator-certification) - 评估您处理 SnapLogic 实例管理任务的能力。
- [SnapLogic Architect Certification](https://learn.snaplogic.com/snaplogic-architect-certification) - 评估您对 SnapLogic 平台的集成参考架构和关键策略的了解，涵盖 SnapLogic 架构、Snaplex 要求、管道生命周期管理、高级数据转换、API 管理、可恢复管道和最佳实践等主题。
- [SnapLogic Developer Certification](https://learn.snaplogic.com/snaplogic-developer-certification) - 测试您在使用 SnapLogic SDK、实现 Snap 功能的不同部分以及构建自定义 Snap 方面的专业知识。
- [SnapLogic Integrator Accreditation](https://learn.snaplogic.com/snaplogic-accreditation) - 它专为那些想要增强所有核心 SnapLogic 概念专业知识的人士而设计，以满足跨行业和业务线的各种集成需求。
- [SnapLogic Integrator Certification](https://learn.snaplogic.com/snaplogic-integrator-certification-1) - 重点关注初学者培训、超级任务、管道迁移以及涵盖各种集成端点的用户帮助视频等主题。

</详情>
<详情>
<摘要>TIBCO</摘要>

- [TIBCO BusinessWorks Associate](https://www.credly.com/org/citrix/badge/tca-tibco-businessworks) - 检查对 Business Studio 和 TIBCO Cloud Integration 的理解，设计应用程序组件（模块、WSDL、REST API），开发集成应用程序以及测试、部署和管理应用程序。
- [TIBCO BusinessWorks Certified Professional](https://www.credly.com/org/citrix/badge/tcp-tibco-businessworks) - 验证在最少的监督下设计、开发、部署、监控和管理中等复杂度的 TIBCO BusinessWorks 应用程序的能力。
- [TIBCO BusinessWorks Container Edition Certified Professional](https://www.credly.com/org/citrix/badge/tcp-tibco-businessworks-container-edition) - 验证在最少的监督下开发、部署和管理具有平均复杂性的 TIBCO BusinessWorks Container Edition 应用程序的能力。
- [TIBCO BPM Enterprise Associate](https://www.credly.com/org/citrix/badge/tca-tibco-bpm-enterprise) - 检查对 TIBCO BPM 特性和功能的理解、开发和管理业务流程以及部署和测试流程应用程序。
- [TIBCO BPM Enterprise Certified Professional](https://www.credly.com/org/citrix/badge/tcp-tibco-bpm-enterprise) - 验证使用 TIBCO BPM Enterprise Suite 设计、开发、部署和管理业务流程的能力。
- [TIBCO Cloud Associate Certification](https://www.credly.com/org/citrix/badge/tca-tibco-cloud) - 验证使用 TIBCO Cloud 所需的技能和知识，包括其关键组件和功能。
- [TIBCO Cloud API Management Associate](https://www.credly.com/org/citrix/badge/tca-tibco-cloud-api-management) - 涵盖 API 定义创建和测试、API 密钥身份验证以及使用开发人员门户和 I/O 文档等主题。
- [TIBCO Cloud API Management Certified Professional](https://www.credly.com/org/citrix/badge/tcp-tibco-cloud-api-management) - 验证实施 TIBCO Cloud Mesh、基于 OAuth 的安全性以及管理 SOAP 服务的能力。
- [TIBCO Cloud Integration Associate](https://www.credly.com/org/citrix/badge/tca-tibco-cloud-integration) - 验证使用 TIBCO Cloud Integration 所需的技能和知识，包括其连接、开发和集成功能。
- [TIBCO Cloud Integration - Connect Associate](https://www.credly.com/org/citrix/badge/tca-tibco-cloud-integration-connect) - 检查 TIBCO Cloud Integration 的 Connect 功能的使用情况、安装本地代理、创建连接和集成应用程序以及配置流程。
- [TIBCO Cloud Integration - Connect Certified Professional](https://www.credly.com/org/citrix/badge/tcp-tibco-cloud-integration-connect) - 检查连接的创建和管理，确保连接安全，并对与 TIBCO Cloud Integration 中的连接相关的问题进行故障排除。
- [TIBCO Cloud Integration Certified Professional](https://www.credly.com/org/citrix/badge/tcp-tibco-cloud-integration) - 检查有关功能和优势、集成、开发和连接应用程序、使用 API 建模器和模拟功能创建 API 等方面的知识。
- [TIBCO Messaging Associate](https://www.credly.com/org/citrix/badge/tca-tibco-messaging) - 涵盖 TIBCO 企业消息服务 (EMS)、TIBCO FTL、TIBCO eFTL 等主题，以及 Apache Kafka、Apache Pulsar 和 Eclipse Mosquitto 等其他消息传递技术。
- [TIBCO Messaging Certified Professional](https://www.credly.com/org/citrix/badge/tcp-tibco-messaging) - 验证使用 TIBCO Messaging 及其组件所需的技能和知识，包括 TIBCO Enterprise Message Service (EMS)、TIBCO FTL 和 TIBCO eFTL。
  
</详情>
<详情>
<摘要>工作</摘要>

- [Workato Automation Pro I](https://academy.workato.com/enterprise-automation-i-exam) - 业务自动化流程的基础知识。
- [Workato Automation Pro II](https://academy.workato.com/enterprise-automation-ii-exam) - 先进实用的自动化方法。
- [Workato Automation Pro III](https://academy.workato.com/automation-pro-iii-exam) - 深入的系列徽章模块可最大限度地发挥 Workato 的潜力。

</详情>
<详情>
<摘要>WSO2</摘要>

- [WSO2 Certified API Manager Developer - V3](https://wso2.com/training/certification/certified-api-manager-developer/) - 评估您使用 WSO2 API Manager V3 设计、开发和发布 API 的专业知识，包括 API 生命周期管理、访问控制和 API 文档。
- [WSO2 Certified API Manager Developer - V4 - Micro Integrator Profile](https://wso2.com/training/certification/certified-api-manager-developer-v4-micro-integrator-profile/) - 使用 WSO2 API Manager V4 的 Micro Integrator 配置文件验证您在设计、开发和发布 API 方面的专业知识。它涵盖了 Micro Integrator 上下文中的 API 生命周期管理、访问控制和 API 文档。
- [WSO2 Certified API Manager Expert - V3](https://wso2.com/training/certification/certified-api-manager-expert/) - 确认您使用 WSO2 API Manager V3 进行 API 管理的高级技能和知识，包括 API 创建、发布、安全、策略实施和分析。
- [WSO2 Certified API Manager Expert - V4 - API Management Profile](https://wso2.com/training/certification/api-manager-expert-v4-api-management-profile/) - 展示您熟练使用 WSO2 API Manager V4 执行 API 管理任务，例如创建、发布和保护 API，以及实施策略和分析。
- [WSO2 Certified Enterprise Integrator Developer - V7 - Micro Integrator](https://wso2.com/training/certification/certified-enterprise-integrator-developer-micro-integrator/) - 验证您使用 WSO2 Enterprise Integrator V7 的 Micro Integrator 配置文件来开发、部署和管理集成解决方案的知识和技能。
- [WSO2 Certified Enterprise Integrator Developer - V7 - Streaming Integrator](https://wso2.com/training/certification/certified-enterprise-integrator-developer-streaming-integrator/) - 展示您使用 WSO2 Enterprise Integrator V7 的 Streaming Integrator 配置文件来开发、部署和管理实时数据集成和流分析解决方案的专业知识。
- [WSO2 Certified Enterprise Integrator Expert - V6](https://wso2.com/training/certification/certified-enterprise-integrator6-expert/) - 测试您使用 WSO2 Enterprise Integrator V6 进行复杂集成场景的深入知识和技能，包括最佳实践、故障排除和性能调整。
- [WSO2 Certified Solutions Architect Associate](https://wso2.com/training/certification/certified-solutions-architect-associate/) - 评估您对 WSO2 产品架构的基本概念和原理的理解，以及您使用 WSO2 技术设计和实施解决方案的能力。

</详情>

<!--lint disable-->
**[⬆ 回到顶部](#contents)**
<!--lint enable-->

### 连接器
- [JCA](https://projects.eclipse.org/projects/ee4j.jca) - 定义 Jakarta EE 应用程序组件连接到企业信息系统的标准架构。以前称为 Java EE 连接器体系结构和 J2EE 连接器体系结构。
- [Kafka Connect](https://kafka.apache.org/documentation/#connect) - 一种用于在 Apache Kafka 和其他系统之间可扩展且可靠地传输数据的工具。

<!--lint disable-->
**[⬆ 回到顶部](#contents)**
<!--lint enable-->
### 数据格式
- [Apache Avro (⭐3.2k)](https://github.com/apache/avro) - 数据序列化系统，提供紧凑、快速、高效的结构化数据序列化。它支持模式演化，允许高效的数据压缩，并且旨在与大数据处理框架良好配合。
- [Apache Thrift (⭐10k)](https://github.com/apache/thrift) - 最初由 Facebook 开发的序列化和 RPC 框架，可从单个接口定义文件生成跨语言绑定。
- [BSON](https://bsonspec.org/) - 用于类似 JSON 文档的二进制编码序列化格式，旨在轻量级且高效。它支持丰富的数据类型，广泛应用于NoSQL数据库，例如MongoDB。
- [Cap'n Proto (⭐13k)](https://github.com/capnproto/capnproto) - 一种极快的数据交换格式和 RPC 系统，其零拷贝编码可兼作有线格式和内存中表示。
- [CBOR](https://cbor.io/) - 简洁二进制对象表示 (RFC 8949)，一种二进制数据格式，具有类似 JSON 的数据模型，专为小消息大小和受限设备而设计。
- [CSV](https://datatracker.ietf.org/doc/html/rfc4180) - 一种简单且广泛使用的数据格式，以纯文本形式存储表格数据。它易于阅读和编写，并且可以被大多数编程语言处理。
- 用于在贸易伙伴之间交换业务文档的 EDI 标准。
   - [UN/EDIFACT](https://unece.org/trade/uncefact/introducing-unedifact) - 适用于行政、商业和运输的联合国 EDI 标准，在北美以外地区占主导地位。
   - [X12](https://x12.org/) - ANSI 认可的 EDI 标准在北美广泛用于订单、发票和医疗保健索赔等交易。
- [FlatBuffers (⭐26k)](https://github.com/google/flatbuffers) - 来自 Google 的高效跨平台序列化库，允许直接访问序列化数据，而无需解析或解包。
- [JSON](https://datatracker.ietf.org/doc/html/rfc8259) - 一种轻量级且易于读取的数据格式，广泛用于数据交换。它支持多种数据类型，并且与多种编程语言兼容。
   - [NDJSON (⭐830)](https://github.com/ndjson/ndjson-spec) - 用于在流协议中分隔 JSON 对象的标准。它可以高效处理大型 JSON 数据集，广泛应用于大数据处理。
   - [JSON Lines](https://jsonlines.org/) - 一种文本格式，用于存储每行一个记录的结构化数据。
   - [JSON Text Sequence](https://datatracker.ietf.org/doc/html/rfc7464) - RFC 7464 中定义，描述用于传输或存储单个 JSON 文本序列的特定格式。
- [MessagePack (⭐7.4k)](https://github.com/msgpack/msgpack) - 一种高效的二进制序列化格式，可让您在多种语言（如 JSON）之间交换数据，但更小、更快。
- [Protocol Buffers (⭐71k)](https://github.com/protocolbuffers/protobuf) - 一种与语言无关和平台无关的序列化机制，旨在高效且可扩展。它支持丰富的数据类型，广泛应用于分布式系统，例如gRPC和Apache Kafka。
- [XML](https://www.w3.org/TR/xml11/) - 一种灵活且广泛使用的标记语言，用于存储和交换结构化数据。它支持丰富的数据类型，并且兼容多种编程语言。
- [YAML (⭐477)](https://github.com/yaml/yaml-spec) - 一种人性化且易于阅读的数据序列化格式，广泛用于配置文件和数据交换。它支持丰富的数据类型，并且与大多数编程语言兼容。

<!--lint disable-->
**[⬆ 回到顶部](#contents)**
<!--lint enable-->
### 整合风格
- [File Transfer](https://www.enterpriseintegrationpatterns.com/patterns/messaging/FileTransferIntegration.html) - 应用程序之间通过文件交换来交换数据。
- [Messaging](https://www.enterpriseintegrationpatterns.com/patterns/messaging/Messaging.html) - 应用程序使用消息传递基础设施交换消息。
- [Remote Procedure Invocation](https://www.enterpriseintegrationpatterns.com/patterns/messaging/EncapsulatedSynchronousIntegration.html) - 应用程序通过网络调用远程服务器上的函数或过程。
- [Shared Database](https://www.enterpriseintegrationpatterns.com/patterns/messaging/SharedDataBaseIntegration.html) - 多个应用程序通过公共数据库访问和操作相同的数据。

<!--lint disable-->
**[⬆ 回到顶部](#contents)**
<!--lint enable-->
### 市场分析
- API管理
  - [Gartner 全生命周期 API 管理的关键功能](https://www.gartner.com/doc/code/468184)
  - [Gartner 全生命周期 API 管理魔力象限](https://www.gartner.com/doc/code/464116)
  - [Forrester Wave：API 管理解决方案](https://www.forrester.com/go?objectid=RES159081)
- 业务流程管理
  - [Gartner 智能业务流程管理套件的关键功能](https://www.gartner.com/doc/code/292486)
  - [Gartner 智能业务流程管理套件魔力象限](https://www.gartner.com/doc/code/345694)
- ETL
  - [Gartner 数据集成工具的关键功能](https://www.gartner.com/doc/code/464068)
  - [Gartner 数据集成工具魔力象限](https://www.gartner.com/doc/code/450251)
- 平台即服务
  - [Gartner 企业集成平台即服务的关键功能](https://www.gartner.com/doc/code/434187)
  - [Gartner 企业集成平台即服务魔力象限](https://www.gartner.com/doc/code/397953)
  - [Forrester Wave：企业 iPaaS](https://www.forrester.com/report/the-forrester-wave-tm-enterprise-ipaas-q4-2021/RES176201)
- 机器人流程自动化
  - [Gartner 机器人流程自动化关键功能](https://www.gartner.com/doc/code/465756)
  - [Gartner 机器人流程自动化魔力象限](https://www.gartner.com/doc/code/441474)
  - [Forrester Wave：机器人流程自动化](https://www.forrester.com/go?objectid=RES161538)

<!--lint disable-->
**[⬆ 回到顶部](#contents)**
<!--lint enable-->
### 协议
- [A2A](https://a2a-protocol.org/latest/) - 用于 AI 代理互操作性的代理到代理协议。使代理能够通过代理卡发现彼此、交换消息以及跨框架和供应商委派任务。由 Google 创建，由 Linux 基金会管理。
- [AMQP 0-9-1](https://www.rabbitmq.com/resources/specs/amqp0-9-1.pdf) - 一种消息队列协议，支持在应用程序或系统之间交换消息。 AMQP 0-9-1 提供可靠性、安全性和灵活性来处理复杂的消息传递场景。
- [AMQP 1.0](http://docs.oasis-open.org/amqp/core/v1.0/os/amqp-core-overview-v1.0-os.html) - 一种被广泛接受的消息队列协议，可在系统之间提供可靠、可互操作且高效的消息传递。 AMQP 1.0 支持广泛的消息传递场景，非常适合复杂的企业级应用程序。
- [AS2](https://datatracker.ietf.org/doc/html/rfc4130) - 一种通过 HTTP/S 安全可靠地传输 EDI 和其他业务文档的协议，使用 S/MIME 进行签名和加密。
- [AS4](https://docs.oasis-open.org/ebxml-msg/ebms/v3.0/profiles/AS4-profile/v1.0/AS4-profile-v1.0.html) - ebMS 3.0 的 OASIS 配置文件，用于安全、基于 Web 服务的 B2B 文档交换，在 Peppol 等电子政务网络中得到广泛认可。
- [CoAP](http://coap.technology/) - 专为物联网 (IoT) 生态系统中受限设备而设计的专用应用程序协议。 CoAP 提供了一种轻量级、低开销的通信机制来支持资源受限的设备。
- [gRPC](https://grpc.io/) - 一个高性能、开源 RPC 框架，使用 HTTP/2 和 Protocol Buffers，支持流式传输、可插入负载平衡和身份验证。
- [HTTP](https://httpwg.org/specs/) - 一种广泛使用的协议，可促进 Web 服务器和客户端之间的通信。 HTTP 支持通过互联网传输数据，使 Web 应用程序能够无缝运行。
- [JSON-RPC](https://www.jsonrpc.org/specification) - 一种简单、轻量级的远程过程调用协议，支持使用 JSON 数据在系统之间进行通信。 JSON-RPC 提供无状态通信，适用于资源受限的设备。
- [MCP](https://modelcontextprotocol.io/) - 用于 AI 代理到工具连接的模型上下文协议。标准化 AI 代理如何发现外部工具、数据源和 API 并与之交互。由 Anthropic 创建，由 Linux 基金会管理。
- [MQTT](https://mqtt.org/mqtt-specification/) - 一种轻量级且高效的发布-订阅协议，支持设备之间的消息传递。 MQTT 可实现低开销通信，非常适合物联网和移动应用。
- [OpenMessaging (⭐287)](https://github.com/openmessaging/specification) - 用于分布式消息传递的云原生、供应商中立的开放规范。
- [Server-Sent Events](https://html.spec.whatwg.org/multipage/server-sent-events.html) - WHATWG 标准，用于通过纯 HTTP 将基于文本的事件流从服务器推送到客户端。
- [SOAP](https://www.w3.org/TR/soap/) - 一种使用 XML 实现系统间通信的消息传递协议。 SOAP 支持广泛的消息传递场景，包括分布式计算和企业应用程序。
- [STOMP](https://stomp.github.io/) - 一种消息传递协议，可在系统之间提供简单的、面向文本的通信。 STOMP 非常适合低延迟、高性能消息传递场景。
- [WebSocket](https://datatracker.ietf.org/doc/html/rfc6455) - 一种通过单个 TCP 连接提供全双工、双向通信通道的协议，非常适合实时应用程序。

<!--lint disable-->
**[⬆ 回到顶部](#contents)**
<!--lint enable-->
### 标准API
- [FHIR](https://www.hl7.org/fhir/) - HL7 的快速医疗保健互操作性资源标准，定义用于交换医疗保健数据的 RESTful API 和资源格式。
- [JDBC](https://docs.oracle.com/javase/8/docs/technotes/guides/jdbc/) - 基于 Java 的 API，提供对关系数据库的通用数据访问。 JDBC 提供了一致且高效的数据访问和操作方式，使其成为开发人员的流行选择。
- [JMS](https://javaee.github.io/jms-spec/) - 一种消息 API，使 Java 应用程序能够发送和接收消息。 JMS 支持可靠的消息传递，广泛应用于企业级应用程序。
- [ODBC](https://docs.microsoft.com/en-us/sql/odbc/reference/odbc-overview) - 一种被广泛接受的 API，提供从各种数据库管理系统访问数据的标准化方法。 ODBC 提供了访问数据的一致接口，使开发数据库应用程序变得容易。
- [OData](https://www.odata.org/) - 一种开放协议，支持创建和使用可查询且可互操作的 REST API。 OData 简化了 REST API 的开发并提供了访问数据的标准化方法。
- [Open Banking](https://www.openbanking.org.uk/) - 英国标准定义了安全 API，使银行能够与授权的第三方提供商共享帐户和支付数据。

<!--lint disable-->
**[⬆ 回到顶部](#contents)**
<!--lint enable-->
### 结构和验证
- [JSON Schema (⭐5k)](https://github.com/json-schema-org/json-schema-spec) - 用于验证 JSON 数据结构的强大工具。 JSON Schema 使开发人员能够确保 JSON 数据符合特定的结构，从而更容易处理和操作。
- [Schematron](https://www.schematron.com) - 基于规则的验证语言，使开发人员能够定义和验证业务规则、数据报告、质量控制和其他验证场景。 Schematron 提供了一种灵活的方法来验证 XML 文档。
- [XML Schema](https://www.w3.org/TR/xmlschema11-1/) - 一种模式语言，提供用于描述 XML 文档的结构和约束内容的工具。 XML Schema 使开发人员能够确保 XML 数据符合特定的结构，从而更容易处理和操作。

<!--lint disable-->
**[⬆ 回到顶部](#contents)**
<!--lint enable-->
## 贡献
随时欢迎您的贡献！请先查看[贡献指南](https://github.com/stn1slv/awesome-integration/blob/main/CONTRIBUTING.md)。
