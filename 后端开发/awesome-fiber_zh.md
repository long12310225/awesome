# 很棒的纤维 [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

<a href="https://gofiber.io">
  <picture alt="Fiber Logo" align="right" style="margin-right: 25px">
    <source height="75" media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/gofiber/docs/master/static/img/logo-dark.svg">
    <img height="75" alt="Fiber Logo" align="right" style="margin-right: 25px" src="https://raw.githubusercontent.com/gofiber/docs/master/static/img/logo.svg">
  </picture>
</a>

> **Fiber** 是一个受 [Express](https://github.com/expressjs/express) 启发的 **Web 框架**，构建在 [Fasthttp](https://github.com/valyala/fasthttp) 之上，[Fasthttp](https://github.com/valyala/fasthttp) 是 [Go](https://golang.org/doc/) 的 **最快** HTTP 引擎。旨在**简化**工作，实现**快速**开发，并考虑到**零内存分配**和**性能**。

精彩的 Fiber 中间件、样板、配方、文章和工具的精选列表。
<br>

## 内容

<!--lint disable awesome-toc-->
<!--lint disable awesome-git-repo-age-->

- [⚙️ 中间件](#%EF%B8%8F-middlewares)
  - [🧬 核心](#-core)
  - [🔗 外部](#-external)
  - [💻 贡献](#-contrib)
  - [🌱 第三方](#-third-party)
- [🚧 样板文件](#-boilerplates)
- [📁 食谱](#-recipes)
- [🛠️工具](#%EF%B8%8F-tools)
- [📖 文章](#-articles)
- [📺 视频](#-videos)
- [🤖 基准](#-benchmarks)

## ⚙️ 中间件

哪里可以找到 Fiber 中间件。

### 🧬 核心

Fiber 框架中包含的中间件列表。

- [Adaptor](https://github.com/gofiber/fiber/tree/main/middleware/adaptor) - 用于 net/http 处理程序与 Fiber 请求处理程序之间的转换器。
- [BasicAuth](https://github.com/gofiber/fiber/tree/main/middleware/basicauth) - 基本身份验证中间件提供 HTTP 基本身份验证。它会调用下一个处理程序来获取有效凭据，并调用 401 Unauthorized 来处理丢失或无效的凭据。
- [Cache](https://github.com/gofiber/fiber/tree/main/middleware/cache) - 拦截并缓存响应。
- [Compress](https://github.com/gofiber/fiber/tree/main/middleware/compress) - Fiber 的压缩中间件，默认支持 `deflate`、`gzip` 和 `brotli`。
- [CORS](https://github.com/gofiber/fiber/tree/main/middleware/cors) - 使用各种选项启用跨域资源共享 (CORS)。
- [CSRF](https://github.com/gofiber/fiber/tree/main/middleware/csrf) - 防止 CSRF 攻击。
- [Earlydata](https://github.com/gofiber/fiber/tree/main/middleware/earlydata) - 对 Fiber 的早期数据支持。
- [Encrypt Cookie](https://github.com/gofiber/fiber/tree/main/middleware/encryptcookie) - 加密 cookie 值的加密中间件。
- [EnvVar](https://github.com/gofiber/fiber/tree/main/middleware/envvar) - 通过提供可选配置来公开环境变量。
- [ETag](https://github.com/gofiber/fiber/tree/main/middleware/etag) - 让缓存更加高效并节省带宽，因为如果内容未更改，Web 服务器不需要重新发送完整响应。
- [Expvar](https://github.com/gofiber/fiber/tree/main/middleware/expvar) - 通过其 HTTP 服务器以 JSON 格式提供运行时公开的变体。
- [Favicon](https://github.com/gofiber/fiber/tree/main/middleware/favicon) - 如果提供了文件路径，则忽略日志中的图标或从内存中提供服务。
- [Healthcheck](https://github.com/gofiber/fiber/tree/main/middleware/healthcheck) - 添加用于就绪性和活性探针的运行状况检查端点。
- [Helmet](https://github.com/gofiber/fiber/tree/main/middleware/helmet) - 通过设置各种 HTTP 标头来帮助保护您的应用程序。
- [Idempotency](https://github.com/gofiber/fiber/tree/main/middleware/idempotency) - 发生重复请求时启用容错 API。
- [Keyauth](https://github.com/gofiber/fiber/tree/main/middleware/keyauth) - 密钥身份验证中间件提供基于密钥的身份验证。
- [Limiter](https://github.com/gofiber/fiber/tree/main/middleware/limiter) - 限速中间件。用于限制对公共 API 和/或端点的重复请求，例如密码重置。
- [Logger](https://github.com/gofiber/fiber/tree/main/middleware/logger) - HTTP 请求/响应记录器。
- [Pprof](https://github.com/gofiber/fiber/tree/main/middleware/pprof) - 以 pprof 可视化工具所需的格式提供运行时分析数据。
- [Proxy](https://github.com/gofiber/fiber/tree/main/middleware/proxy) - 允许您将请求代理到多个服务器。
- [Recover](https://github.com/gofiber/fiber/tree/main/middleware/recover) - 从堆栈链中任何位置的恐慌中恢复并将控制权交给集中式错误处理程序。
- [Redirect](https://github.com/gofiber/fiber/tree/main/middleware/redirect) - 处理 Fiber 中的 HTTP 重定向。
- [RequestID](https://github.com/gofiber/fiber/tree/main/middleware/requestid) - 为每个请求添加 requestid。
- [Responsetime](https://github.com/gofiber/fiber/tree/main/middleware/responsetime) - 向响应添加“X-Response-Time”标头。
- [Rewrite](https://github.com/gofiber/fiber/tree/main/middleware/rewrite) - 根据提供的规则重写 URL 路径，以实现向后兼容性或更清晰的链接。
- [Session](https://github.com/gofiber/fiber/tree/main/middleware/session) - 提供会话管理。注意：此中间件使用我们的存储包。
- [Skip](https://github.com/gofiber/fiber/tree/main/middleware/skip) - 当谓词为真时跳过包装的处理程序。
- [Static](https://github.com/gofiber/fiber/tree/main/middleware/static) - 提供来自本地或自定义文件系统的静态文件。
- [Timeout](https://github.com/gofiber/fiber/tree/main/middleware/timeout) - 添加请求的最长时间，如果超过则转发到 ErrorHandler。

### 🔗 外部

外部托管的中间件模块列表，由 [Fiber 团队](https://github.com/orgs/go Fiber/people) 维护。

- [storage](https://github.com/gofiber/storage) - 实现存储接口的预制存储驱动程序，设计用于与各种光纤中间件一起使用。
- [template](https://github.com/gofiber/template) - 该软件包包含 8 个模板引擎，可与 Fiber v1.10.x 一起使用，需要 Go 版本 1.13 或更高版本。

### ‍💻 贡献

由 Fiber 团队和社区维护的第三方中间件列表。

- [casbin](https://github.com/gofiber/contrib/tree/main/v3/casbin) - 由 Casbin 提供支持的 Fiber 授权中间件。
- [circuitbreaker](https://github.com/gofiber/contrib/tree/main/v3/circuitbreaker) - 光纤的断路器中间件。
- [fgprof](https://github.com/gofiber/contrib/tree/main/v3/fgprof) - 通过 fgprof 提供光纤分析支持。
- [hcaptcha](https://github.com/gofiber/contrib/tree/main/v3/hcaptcha) - 使用 hCaptcha 的机器人保护中间件。
- [i18n](https://github.com/gofiber/contrib/tree/main/v3/i18n) - 基于 go-i18n 构建的国际化中间件。
- [jwt](https://github.com/gofiber/contrib/tree/main/v3/jwt) - JSON Web Token (JWT) 身份验证中间件。
- [loadshed](https://github.com/gofiber/contrib/tree/main/v3/loadshed) - 减载中间件可在压力下保护光纤服务。
- [monitor](https://github.com/gofiber/contrib/tree/main/v3/monitor) - 服务器指标监视 Fiber 的中间件。
- [newrelic](https://github.com/gofiber/contrib/tree/main/v3/newrelic) - 新的 Relic 仪器支持 Fiber。
- [opa](https://github.com/gofiber/contrib/tree/main/v3/opa) - 对 Fiber 的开放策略代理 (OPA) 中间件支持。
- [otel](https://github.com/gofiber/contrib/tree/main/v3/otel) - OpenTelemetry 中间件对 Fiber 的支持。
- [paseto](https://github.com/gofiber/contrib/tree/main/v3/paseto) - 与平台无关的安全令牌 (PASETO) 身份验证中间件。
- [sentry](https://github.com/gofiber/contrib/tree/main/v3/sentry) - Fiber 与 Sentry 的错误监控和报告集成。
- [socketio](https://github.com/gofiber/contrib/tree/main/v3/socketio) - 受 Socket.IO 启发的 Fiber 的 WebSocket 包装中间件。
- [swaggo](https://github.com/gofiber/contrib/tree/main/v3/swaggo) - 用于在 Fiber 中提供 Swag 生成的 API 文档的中间件。
- [swaggerui](https://github.com/gofiber/contrib/tree/main/v3/swaggerui) - Swagger UI 中间件，用于在 Fiber 中提供 OpenAPI 规范。
- [testcontainers](https://github.com/gofiber/contrib/tree/main/v3/testcontainers) - 将测试容器与 Fiber 集成的服务实现。
- [WebSocket](https://github.com/gofiber/contrib/tree/main/v3/websocket) - Fiber 的基于 Fasthttp 的 WebSocket 集成，支持“fibre.Ctx”。
- [zap](https://github.com/gofiber/contrib/tree/main/v3/zap) - 使用 Zap 对 Fiber 进行日志记录中间件支持。
- [zerolog](https://github.com/gofiber/contrib/tree/main/v3/zerolog) - 使用 Zerolog 对 Fiber 进行日志记录中间件支持。

### 🌱 第三方

Fiber 社区创建的中间件列表。

- [shareed2k/fiber_tracing](https://github.com/shareed2k/fiber_tracing) - 使用 OpenTracing API 对 Fiber 框架进行中间件跟踪请求。
- [shareed2k/fiber_limiter](https://github.com/shareed2k/fiber_limiter) - 使用 Redis 作为速率限制存储的限制器，具有两种选择滑动窗口、gcra 漏桶的算法。
- [ansrivas/fiberprometheus](https://github.com/ansrivas/fiberprometheus) - 用于 go Fiber 的 Prometheus 中间件。
- [sacsand/gofiber-firebaseauth](https://github.com/sacsand/gofiber-firebaseauth) - Fiber Firebase 身份验证中间件。
- [aschenmaker/fiber-health-check](https://github.com/aschenmaker/fiber-health-check) - 健康检查中间件支持 Fiber️ 框架的健康检查。
- [elastic/apmfiber](https://github.com/elastic/apm-agent-go/tree/master/module/apmfiber) - Go Fiber 的 APM 代理。
- [eozer/fiber_ldapauth](https://github.com/eozer/fiber_ldapauth) - Fiber 的 LDAP 身份验证中间件。
- [fugue-labs/gollem](https://github.com/fugue-labs/gollem/tree/main/contrib/fiberhandler) - 处理程序适配器，将 gollem AI 代理包装为具有 SSE 流支持的 Fiber 处理程序。
- [DavidHoenisch/fiber-coraza](https://github.com/DavidHoenisch/fiber-coraza) - 适用于 Fiber 的 Coraza WAF 中间件，通过与 ModSecurity 兼容的规则提供 Web 应用程序防火墙保护。
- [darkweak/souin](https://github.com/darkweak/souin) - HTTP 缓存，符合 RFC 标准，可作为中间件替代 Varnish。
- [witer33/fiberpow](https://github.com/witer33/fiberpow) - 具有可定制工作量证明挑战的反 DDoS/Bot 中间件。
- [beyer-stefan/gofiber-minifier](https://github.com/beyer-stefan/gofiber-minifier) - 缩小 HTML5、CSS3 和 JavaScript 的中间件。
- [joffref/opa-middleware](https://github.com/Joffref/opa-middleware) - 为光纤提供 OPA 中间件集成。
- [vladfr/fiber-servertiming](https://github.com/vladfr/fiber-servertiming) - 一个中间件，用于根据 W3C 服务器计时规范添加服务器计时标头。
- [airbrake/gobrake](https://github.com/airbrake/gobrake/tree/master/examples/fiber) - 报告性能数据（路由统计信息）的 Airbrake 中间件。
- [samber/slog-fiber](https://github.com/samber/slog-fiber) - 使用 Go slog 库的记录器中间件。
- [mikhail-bigun/fiberlogrus](https://github.com/mikhail-bigun/fiberlogrus) - 使用 logrus 及其结构化日志记录功能的记录器中间件。
- [Idan-Fishman/fiber-bind](https://github.com/Idan-Fishman/fiber-bind) - 请求模式验证器中间件，用于验证请求正文、查询字符串参数、路由参数甚至表单文件等源。
- [rodrigoodhin/fiper](https://gitlab.com/rodrigoodhin/fiper) - FiPer 是一个库，它使用 JWT 为 Fiber 提供基于角色的访问控制 (RBAC)，并使用支持的两个 ORM 库提供数据库持久性：Gorm 和 Bun。
- [zeiss/fiber-goth](https://github.com/ZEISS/fiber-goth) - 用于将身份验证集成到 Fiber 应用程序的简单中间件。
- [zeiss/fiber-authz](https://github.com/ZEISS/fiber-authz) - 使用定义的 RBAC 模型来保护 Fiber 中的路由的中间件。
- [zeiss/fiber-htmx](https://github.com/ZEISS/fiber-htmx) - 在 Fiber 中使用 HTMX 的中间件。
- [jsorb84/ssefiber](https://github.com/jsorb84/ssefiber) - Fiber 的基本 SSE 实现。
- [streamerd/fibergun](https://github.com/streamerd/fibergun) - 用于 Fiber 的 GunDB 中间件。可以轻松集成 GunDB（一个去中心化数据库）。
- [apitally/apitally-go](https://github.com/apitally/apitally-go) - 用于 Fiber 的简单 API 监控工具。跟踪 API 使用情况、错误和性能，并包括请求日志记录和警报功能。
- [newrelic/go-agent](https://github.com/newrelic/go-agent/tree/master/v3/integrations/nrfiber) - 用于 Fiber 的官方 New Relic 中间件，用于管理 New Relic 监控仪器。
- [narmadaweb/limiter](https://github.com/narmadaweb/limiter) - 一款基于 Redis 的高性能 Fiber 速率限制器中间件，支持固定窗口、滑动窗口和令牌桶算法。
- [narmadaweb/gonify](https://github.com/narmadaweb/gonify) - 适用于 HTML5、CSS3、JavaScript、Json、XML 和 SVG 的 Fiber Minifying 中间件。
- [oaswrap/fiberopenapi](https://github.com/oaswrap/spec/tree/main/adapter/fiberopenapi) - 用于生成 OpenAPI 3.x 规范并具有自动路由文档的光纤适配器。

## 🚧 样板文件

Fiber 的预制样板。

- [gofiber/boilerplate](https://github.com/gofiber/boilerplate) - 官方纤维样板。
- [fiber-boilerplate](https://github.com/thomasvvugt/fiber-boilerplate) - Fiber web 框架的样板。
- [sujit-baniya/fiber-boilerplate](https://github.com/sujit-baniya/fiber-boilerplate) - 纤维网络框架顶部的样板，具有许多中间件和功能。
- [goravel/fiber](https://github.com/goravel/fiber) - Laravel 类似的样板，支持 Fiber。
- [create-go-app/fiber-go-template](https://github.com/create-go-app/fiber-go-template) - 用于创建 Go App CLI 的 Fiber 后端模板。
- [efectn/fiber-boilerplate](https://github.com/efectn/fiber-boilerplate) - 简单且可扩展的样板文件，可使用 Fiber 构建强大且有组织的 REST 项目。
- [embedmode/fiberseed](https://github.com/embedmode/fiberseed) - 具有许多中间件的纤维样板 API。
- [GalvinGao/gofiber-template](https://github.com/GalvinGao/gofiber-template) - 一个生产就绪、容器优先的固执己见的 go Fiber 项目模板。通过 envvars 进行配置，通过 go.uber.org/fx 进行 DI，通过 uptrace/bun 进行数据库，具有开箱即用的 MVC 文件夹结构和 CI/CD 支持。
- [mikhail-bigun/go-app-template](https://github.com/mikhail-bigun/go-app-template) - 干净的架构 Go 应用程序样板，具有丰富的 Fiber 实现。
- [felipeafonso/go-htmx-starter](https://github.com/FelipeAfonso/go-htmx-starter) - 用于 Go + HTMX 开发的前端固定样板，使用 Tailwind 和 Vite 进行捆绑和热重载。
- [amrebada/go-modules](https://github.com/amrebada/go-modules) - Go Fiber 的 Nest JS 类似结构。
- [ingeniousambivert/fiber-bootstrapped](https://github.com/ingeniousambivert/fiber-bootstrapped) - 受 FeathersJS 原则启发，采用以服务为中心的架构的 Go 项目工具包。
- [sebajax/go-vertical-slice-architecture](https://github.com/sebajax/go-vertical-slice-architecture) - 使用 Fiber 和 Uber dig 的垂直切片架构代码原型。可维护且可扩展的代码组织。
- [go-rat/fiber-skeleton](https://github.com/go-rat/fiber-skeleton) - Fiber 骨架为 Web 项目提供支持，支持基于线路的依赖注入。

## 📁 食谱

纤维食谱。

- [gofiber/recipes](https://github.com/gofiber/recipes) - 官方纤维食谱。
- [kiyonlin/fiblar-demo](https://github.com/kiyonlin/fiblar-demo) - Fiber v1 + 角度演示。
- [koddr/tutorial-go-fiber-rest-api](https://github.com/koddr/tutorial-go-fiber-rest-api) - 使用 Fiber 构建 Restful api 的教程。
- [firebase007/go-rest-api-with-fiber](https://github.com/firebase007/go-rest-api-with-fiber) - 带有 Fiber、日志记录、basicAuth 和 postgresql 的演示项目。
- [chawk/go_fiber_quickstart](https://github.com/chawk/go_fiber_quickstart) - 光纤快速启动示例项目。
- [EricLau1/go-fiber-auth-api](https://github.com/EricLau1/go-fiber-auth-api) - 使用 Fiber MongoDB 和 JWT 的 Golang 身份验证 API。
- [alpody/golang-fiber-realworld-example-app](https://github.com/alpody/golang-fiber-realworld-example-app) - 使用 Fiber、Gorm、Swagger 构建的真实后端 API 示例。
- [kubestellar/console](https://github.com/kubestellar/console) - 基于 Fiber 构建的人工智能驱动的多集群 Kubernetes 仪表板，具有实时可观察性和 CNCF 集成。
- [paundraP/golang-starter-template](https://github.com/paundraP/Go-Starter-Template) - Golang REST API 具有身份验证、授权和集成支付网关支持。

## 🛠️工具

多种使 Fiber 使用更轻松的工具。

- [Alibaba/opentelemetry-go-auto-instrumentation](https://github.com/alibaba/opentelemetry-go-auto-instrumentation) - 一种无需使用 OpenTelemetry API 更改任何代码即可监控光纤应用的工具。
- [deepmap/oapi-codegen](https://github.com/deepmap/oapi-codegen) - 根据 OpenAPI 3 规范生成 Go 客户端和服务器样板。
- [go-dawn/dawn](https://github.com/go-dawn/dawn) - Dawn 是一个固执己见的 Web 框架，提供基于 Fiber 的快速开发功能。
- [MUlt1mate/protoc-gen-httpgo](https://github.com/MUlt1mate/protoc-gen-httpgo) - 一个 protoc 插件，可从 proto 文件生成 Fiber HTTP 服务器和客户端代码。
- [ryanbekhen/feserve](https://github.com/ryanbekhen/feserve) - Feserve 是一个轻量级应用程序或 Docker 映像，用于服务前端和负载均衡器应用程序。
- [tompston/gomakeme](https://github.com/tompston/gomakeme) - 为 Fiber 或 Gin REST API 生成样板 + 端点。

## 📖 文章

社区撰写的有关 Fiber 的文章。

- [使用中间件和样板文件](https://dev.to/koddr/go-fiber-by-examples-working-with-middlewares-and-boilerplates-3p0m)
- [测试应用程序](https://dev.to/koddr/go-fiber-by-examples-testing-the-application-1ldf)
- [深入研究内置函数](https://dev.to/koddr/go-fiber-by-examples-delving-into-built-in-functions-1p3k)
- [Go Fiber 示例：Fiber Web 框架有何用处？](https://dev.to/koddr/go-fiber-by-examples-how-can-the-fiber-web-framework-be-useful-487a)
- [在 Go 上构建 RESTful API：隔离 Docker 容器中的 Fiber、PostgreSQL、JWT 和 Swagger 文档](https://dev.to/koddr/build-a-restful-api-on-go-fiber-postgresql-jwt-and-swagger-docs-in-isolated-docker-containers-475j)
- [光纤入门](https://dev.to/fenny/getting-started-with-fiber-36b6)
- [使用 Fiber 在 Go 中构建 Express 风格的 API](https://blog.logrocket.com/express-style-api-go-fiber/)
- [Fiber v1.9.6 如何将性能提高817%并保持快速、灵活和友好？](https://dev.to/koddr/fiber-v1-9-5-how-to-improve-performance-by-817-and-stay-fast-flexible-and-friendly-2dp6)
- [使用 Go、Fiber、Angular、MongoDB 和 Google Cloud Secret Manager 创建旅行列表应用](https://blog.yongweilun.me/create-a-travel-list-app-with-go-fiber-angular-mongodb-and-google-cloud-secret-manager-ck9fgxy0p061pcss1xt1ubu8t)
- [使用 Fiber 在 Go 中构建基本 REST API](https://tutorialedge.net/golang/basic-rest-api-go-fiber/)
- [使用 Fiber 在 Go 中创建快速 API](https://dev.to/jozsefsallai/creating-fast-apis-in-go-using-fiber-59m9)
- [从 Express 切换到 Fiber 值得吗？](https://dev.to/koddr/are-sure-what-your-lovely-web-framework-running-so-fast-2jl1)
- [光纤 v1.8。有什么新的、更新的和重新思考的？](https://dev.to/koddr/fiber-v1-8-what-s-new-updated-and-re-thinked-339h)
- [Fiber发布v1.7！有哪些新内容？它仍然快速、灵活且友好吗？](https://dev.to/koddr/fiber-v2-is-out-now-what-s-new-and-is-he-still-fast-flexible-and-friendly-3ipf)
- [欢迎使用 Fiber — 一个用 Go 编写的 Express.js 风格的 Web 框架，带有 ❤️](https://dev.to/koddr/welcome-to-fiber-an-express-js-styled-fastest-web-framework-written-with-on-golang-497)
- [极快的单元测试 - Fiber/fasthttp/http 内部结构](https://medium.com/trendyol-tech/golang-blazing-fast-unit-tests-fiber-fasthttp-http-internals-and-optimizing-http-server-tests-bbd1fe7b944b)
- [在 Go 中构建微服务：第 1 部分 - 项目设置、Docker 化](https://saadfarhan124.medium.com/building-microservices-in-go-part-1-e7e58893bc5e)
- [在 Go 中构建微服务：第 2 部分 - 实时重新加载](https://saadfarhan124.medium.com/building-microservices-in-go-part-2-f9c6c535805c)
- [在 Go 中构建微服务：第 3 部分 - 数据库、模型、迁移](https://saadfarhan124.medium.com/building-microservices-in-go-part-3-database-models-migrations-a4455121bb11)
- [使用 Go、Docker 和 PostgreSQL 从头开始构建 REST API](https://dev.to/divrhino/build-a-rest-api-from-scratch-with-go-and-docker-3o54)
- [使用 Go Fiber、Docker 和 PostgreSQL 构建全栈应用程序](https://dev.to/divrhino/build-a-fullstack-app-with-go-fiber-docker-and-postgres-1jg6)
- [使用 Go Fiber、Docker 和 PostgreSQL 创建 CRUD 应用程序](https://dev.to/divrhino/create-a-crud-app-with-go-fiber-docker-and-postgres-47e3)

## 📺 视频

由社区创建的有关 Fiber 的视频教程。

- [Fiber 是最好的 Go Web 框架吗？比杜松子酒更好吗？](https://youtu.be/10miByMOGfY)

## 🤖 基准

将 Fiber 与其他框架进行比较的几个基准。

- [TechEmpower](https://www.techempower.com/benchmarks/#section=data-r20&hw=ph&test=json) - 项目提供了广泛的 Web 应用程序框架领域的性能度量。
- [web-frameworks-benchmark](https://web-frameworks-benchmark.netlify.app/result) - 该项目旨在衡量各种编程语言框架之间的差异。
- [go-web-framework-benchmark](https://github.com/smallnest/go-web-framework-benchmark) - 该基准套件旨在比较 Go Web 框架的性能。

### 👍 贡献

贡献指南可以在 [CONTRIBUTING.md](https://github.com/go Fiber/awesome- Fiber/blob/master/CONTRIBUTING.md) 上找到

## ☕ 支持者

Fiber 是一个开源项目，依靠捐赠来支付账单，例如我们的域名、托管和无服务器基础设施。如果您想支持 Fiber，请成为 [GitHub 赞助商](https://github.com/sponsors/go Fiber)。

<!-- sponsors -->

### 📅 每月赞助商

<table>
<tr><td valign="top"><strong>🔥 Fiber Guardian</strong></td><td><a href="https://www.coderabbit.ai/?utm_source=cr_org&amp;utm_medium=github" title="@coderabbitai"><img src="https://github.com/coderabbitai.png" width="50" alt="@coderabbitai" /></a></td></tr>
<tr><td valign="top"><strong>☕ Fiber Supporter</strong></td><td><a href="https://ndole.studio" title="@NdoleStudio"><img src="https://github.com/NdoleStudio.png" width="34" alt="@NdoleStudio" /></a>&nbsp;<a href="https://cyberapper.ai" title="@petercool"><img src="https://github.com/petercool.png" width="34" alt="@petercool" /></a></td></tr>
<tr><td valign="top"><strong>🪴 Fiber Friend</strong></td><td><a href="https://github.com/simonheisstpeter" title="@simonheisstpeter"><img src="https://github.com/simonheisstpeter.png" width="32" alt="@simonheisstpeter" /></a>&nbsp;<a href="https://github.com/bsdrop" title="@bsdrop"><img src="https://github.com/bsdrop.png" width="32" alt="@bsdrop" /></a></td></tr>
</table>

### 🎁 一次性赞助商

<table>
<tr><td valign="top"><strong>🚀 Fiber Hero</strong></td><td><a href="https://www.thanks.dev" title="@thnxdev"><img src="https://github.com/thnxdev.png" width="40" alt="@thnxdev" /></a></td></tr>
</table>
<!-- sponsors -->
