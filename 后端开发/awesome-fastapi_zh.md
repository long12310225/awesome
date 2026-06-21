<!--lint disable double-link-->

# 很棒的 FastAPI | [![Awesome](https://awesome.re/badge-flat.svg)](https://github.com/sindresorhus/awesome)

> 与 FastAPI 相关的精彩内容的精选列表。

[FastAPI](https://fastapi.tiangolo.com/) 是一个现代、高性能、包含电池的 Python Web 框架，非常适合构建 RESTful API。

## 内容

- [第三方扩展](#third-party-extensions)
  - [Admin](#admin)
  - [Auth](#auth)
  - [CyberSecurity](#cybersecurity)
  - [Databases](#databases)
  - [依赖注入](#dependency-injection)
  - [开发者工具](#developer-tools)
  - [Email](#email)
  - [Utils](#utils)
- [Resources](#resources)
  - [官方资源](#official-resources)
  - [外部资源](#external-resources)
  - [Podcasts](#podcasts)
  - [Articles](#articles)
  - [Tutorials](#tutorials)
  - [Talks](#talks)
  - [Videos](#videos)
  - [Courses](#courses)
  - [最佳实践](#best-practices)
- [Hosting](#hosting)
  - [PaaS](#paas)
  - [IaaS](#iaas)
  - [Serverless](#serverless)
- [Projects](#projects)
  - [Boilerplate](#boilerplate)
  - [Docker 镜像](#docker-images)
  - [开源项目](#open-source-projects)
- [Sponsors](#sponsors)

## 第三方扩展

### 管理员

- [FastAPI Admin](https://github.com/fastapi-admin/fastapi-admin) - 功能管理面板提供用于对数据执行 CRUD 操作的用户界面。目前仅适用于 Tortoise ORM。
- [FastAPI Amis Admin](https://github.com/amisadmin/fastapi-amis-admin) - 高性能、高效且易于扩展的 FastAPI 管理框架。
- [Piccolo Admin](https://github.com/piccolo-orm/piccolo_admin) - 一个强大且现代的管理 GUI，使用 Piccolo ORM。
- [SQLAlchemy Admin](https://github.com/aminalaee/sqladmin) - 适用于 SQLAlchemy 模型的 FastAPI/Starlette 管理面板。
- [Starlette Admin](https://github.com/jowilf/starlette-admin) - FastAPI/Starlette 的管理框架，支持 SQLAlchemy、SQLModel、MongoDB 和 ODMantic。


### 授权

- [AuthX](https://github.com/yezz123/AuthX) - FastAPI 的可定制身份验证和 Oauth2 管理。
- [FastAPI Auth](https://github.com/dmontagu/fastapi-auth) - 可插入身份验证，支持具有 JWT 访问和刷新令牌的 OAuth2 密码流程。
- [FastAPI Azure Auth](https://github.com/Intility/fastapi-azure-auth) - 通过单租户和多租户支持对 API 进行 Azure AD 身份验证。
- [FastAPI Casbin Auth](https://github.com/officialpycasbin/fastapi-casbin-auth) - 通过Casbin支持RBAC、ReBAC、ABAC等多种访问控制模型的授权。
- [FastAPI Cloud Auth](https://github.com/tokusumi/fastapi-cloudauth) - FastAPI 和云身份验证服务（AWS Cognito、Auth0、Firebase 身份验证）之间的简单集成。
- [FastAPI Login](https://github.com/maxrdu/fastapi_login) - 帐户管理和身份验证（基于[Flask-Login](https://github.com/maxcountryman/flask-login)）。
- [FastAPI JWT Auth](https://github.com/IndominusByte/fastapi-jwt-auth) - JWT 身份验证（基于 [Flask-JWT-Extended](https://github.com/vimalloc/flask-jwt-extended)）。
- [FastAPI Permissions](https://github.com/holgi/fastapi-permissions) - 行级权限。
- [FastAPI Security](https://github.com/jacobsvante/fastapi-security) - 在 FastAPI 中将身份验证和授权作为依赖项实现。
- [FastAPI Simple Security](https://github.com/mrtolkien/fastapi_simple_security) - 可通过路径操作管理开箱即用的 API 密钥安全性。
- [FastAPI Users](https://github.com/fastapi-users/fastapi-users) - 帐户管理、身份验证、授权。

### 网络安全

- [FastAPI Guard](https://github.com/rennf93/fastapi-guard) - 速率限制、自动禁止 IP、渗透攻击检测、白名单/黑名单（国家/地区、IP、云提供商）、用户代理过滤、地理位置、Redis 持久性集成等。

### 数据库

#### ORM

- [Edgy ORM](https://github.com/dymmond/edgy) - 复杂的数据库变得简单。
- [FastAPI SQLAlchemy](https://github.com/mfreeborn/fastapi-sqlalchemy) - FastAPI 和 [SQLAlchemy](https://www.sqlalchemy.org/) 之间的简单集成。
- [Fastapi-SQLA](https://github.com/dialoguemd/fastapi-sqla) - FastAPI 的 SQLAlchemy 扩展，支持分页、异步和 pytest。
- [FastAPIwee](https://github.com/Ignisor/FastAPIwee) - 一种基于 [PeeWee](https://github.com/coleifer/peewee) 模型创建 REST API 的简单方法。
- [FastSQLA](https://github.com/hadrien/FastSQLA) - FastAPI 的异步 SQLAlchemy 2.0+ 扩展，具有 SQLModel 支持、内置分页等。
- [GINO](https://github.com/python-gino/gino) - 一个轻量级异步 ORM，构建在 SQLAlchemy 核心之上，适用于 Python asyncio。
  - [FastAPI示例](https://github.com/leosussan/fastapi-gino-arq-uvicorn)
- [ORM](https://github.com/encode/orm) - 异步 ORM。
- [ormar](https://collerek.github.io/ormar/) - Ormar 是一种异步 ORM，它使用 Pydantic 验证，可以直接在 FastAPI 请求和响应中使用，因此您只需维护一组模型。包括蒸馏器迁移。
  - [FastAPI Example](https://collerek.github.io/ormar/latest/fastapi/) - 将 FastAPI 与 ormar 结合使用。
- [Piccolo](https://github.com/piccolo-orm/piccolo) - 异步 ORM 和查询生成器，支持 Postgres 和 SQLite，带有电池（迁移、安全性等）。
  - [FastAPI Examples](https://github.com/piccolo-orm/piccolo_examples) - 将 FastAPI 与 Piccolo 结合使用。
- [Tortoise ORM](https://tortoise.github.io) - 受 Django 启发的易于使用的 asyncio ORM（对象关系映射器）。
  - [FastAPI Example](https://tortoise.github.io/examples/fastapi.html) - Tortoise-ORM FastAPI 集成的示例。
  - [教程：使用 FastAPI 设置 Tortoise ORM](https://web.archive.org/web/20200523174158/https://robwagner.dev/tortoise-fastapi-setup/)
  - [Aerich](https://github.com/tortoise/aerich) - Tortoise ORM 迁移工具。
- [Saffier ORM](https://github.com/tarsil/saffier) - 您唯一需要的 Python ORM。
- [SQLModel](https://sqlmodel.tiangolo.com/) - SQLModel（由 Pydantic 和 SQLAlchemy 提供支持）是一个用于通过 Python 代码和 Python 对象与 SQL 数据库进行交互的库。

#### 查询生成器

- [asyncpgsa](https://github.com/CanopyTax/asyncpgsa) - [asyncpg](https://github.com/MagicStack/asyncpg) 的包装器，与 [SQLAlchemy Core](https://docs.sqlalchemy.org/en/latest/core/) 一起使用。
- [Databases](https://github.com/encode/databases) - 在 [SQLAlchemy Core](https://docs.sqlalchemy.org/en/latest/core/) 表达式语言之上工作的异步 SQL 查询构建器。
- [PyPika](https://github.com/kayak/pypika) - 一个 SQL 查询构建器，展示了 SQL 语言的全部丰富性。

#### ODM

- [Beanie](https://github.com/BeanieODM/beanie) - MongoDB 的异步 Python ODM，基于 [Motor](https://motor.readthedocs.io/en/stable/) 和 [Pydantic](https://docs.pydantic.dev/latest/)，支持开箱即用的数据和模式迁移。
- [MongoEngine](https://github.com/MongoEngine/mongoengine) - 一个文档对象映射器（想想 ORM，但用于文档数据库），用于通过 Python 使用 MongoDB。
- [Motor](https://motor.readthedocs.io/) - MongoDB 的异步 Python 驱动程序。
- [ODMantic](https://art049.github.io/odmantic/) - AsyncIO MongoDB ODM 与 [Pydantic](https://docs.pydantic.dev/latest/) 集成。
- [PynamoDB](https://github.com/pynamodb/PynamoDB) - Amazon DynamoDB 的 pythonic 接口。

#### 其他工具

- [Pydantic-SQLAlchemy](https://github.com/tiangolo/pydantic-sqlalchemy) - 将 SQLAlchemy 模型转换为 [Pydantic](https://docs.pydantic.dev/latest/) 模型。
- [FastAPI-CamelCase](https://nf1s.github.io/fastapi-camelcase/) - 利用 [Pydantic](https://docs.pydantic.dev/latest/) 对 FastAPI 提供 CamelCase JSON 支持。
  - [CamelCase Models with FastAPI and Pydantic](https://medium.com/analytics-vidhya/camel-case-models-with-fast-api-and-pydantic-5a8acb6c0eee) - 扩展作者的随附博客文章。
 
### 依赖注入
- [Wireup](https://github.com/maldoinc/wireup) - 在 FastAPI 中以零运行时开销注入依赖项；跨 Web、CLI 或其他接口共享依赖项。

### 开发者工具

- [FastAPI Code Generator](https://github.com/koxudaxi/fastapi-code-generator) - 从 OpenAPI 文件创建 FastAPI 应用程序，从而实现架构驱动的开发。
- [FastAPI Client Generator](https://github.com/dmontagu/fastapi_client) - 根据 OpenAPI 规范生成 mypy 和 IDE 友好的 API 客户端。
- [FastAPI Cruddy Framework](https://github.com/mdconaway/fastapi-cruddy-framework) - FastAPI 的配套库，旨在将 Ruby on Rails、Ember.js 或 Sails.js 的开发效率引入 FastAPI 生态系统。
- [FastAPI MVC](https://github.com/fastapi-mvc/fastapi-mvc) - 开发人员生产力工具，用于制作高质量的 FastAPI 生产就绪 API。
- [FastAPI Profiler](https://github.com/sunhailin-Leo/fastapi_profiler) - joerick/pyinstrument 的 FastAPI 中间件，用于检查您的服务性能。
- [FastAPI Versioning](https://github.com/DeanWay/fastapi-versioning) - API 版本控制。
- [Jupyter Notebook REST API](https://github.com/Invictify/Jupter-Notebook-REST-API) - 将 Jupyter 笔记本作为 RESTful API 端点运行。
- [Manage FastAPI](https://github.com/ycd/manage-fastapi) - 用于生成和管理 FastAPI 项目的 CLI 工具。
- [msgpack-asgi](https://github.com/florimondmanca/msgpack-asgi) - 自动 [MessagePack](https://msgpack.org/) 内容协商。
- [python-cqrs](https://github.com/pypatterns/python-cqrs) - 事件驱动架构框架，具有 CQRS、事务发件箱、Saga 编排、无缝 FastAPI/FastStream 集成。

### 电子邮件

- [FastAPI Mail](https://github.com/sabuhish/fastapi-mail) - 用于发送电子邮件和附件（单独和批量）的轻量级邮件系统。

### 实用工具

- [Apitally](https://github.com/apitally/apitally-py) - FastAPI 的 API 分析、监控和请求日志记录。
- [ASGI Correlation ID](https://github.com/snok/asgi-correlation-id) - 请求 ID 记录中间件。
- [FastAPI Cache](https://github.com/comeuplater/fastapi_cache) - 一个简单的轻量级缓存系统。
- [FastAPI Cache](https://github.com/long2ice/fastapi-cache) - 一种缓存 FastAPI 响应和函数结果的工具，支持 Redis、Memcached、DynamoDB 和内存后端。
- [FastAPI Chameleon](https://github.com/mikeckennedy/fastapi-chameleon) - 添加 Chameleon 模板语言与 FastAPI 的集成。
- [FastAPI CloudEvents](https://github.com/sasha-tkachev/fastapi-cloudevents) - FastAPI 的 [CloudEvents](https://cloudevents.io/) 集成。
- [FastAPI Contrib](https://github.com/identixone/fastapi_contrib) - 一套自以为是的实用程序：分页、身份验证中间件、权限、自定义异常处理程序、MongoDB 支持和 Opentracing 中间件。
- [FastAPI FastCRUD](https://github.com/benavlabs/fastcrud)) - 强大的异步 CRUD 操作和灵活的端点创建实用程序。
- [FastAPI Events](https://github.com/melvinkcx/fastapi-events) - FastAPI 和 Starlette 的异步事件调度/处理库。
- [FastAPI FeatureFlags](https://github.com/Pytlicek/fastapi-featureflags) - FastAPI 功能标志的简单实现。
- [FastAPI Injectable](https://github.com/JasperSui/fastapi-injectable) - 在 CLI 工具、后台任务、工作人员等中的路由处理程序外部使用 FastAPI 的依赖项注入。
- [FastAPI Jinja](https://github.com/AGeekInside/fastapi-jinja) - 添加 Jinja 模板语言与 FastAPI 的集成。
- [FastAPI Lazy](https://github.com/yezz123/fastango) - 使用 FastAPI 启动项目的惰性包。
- [FastAPI Limiter](https://github.com/long2ice/fastapi-limiter) - FastAPI 的请求速率限制器。
- [FastAPI Listing](https://github.com/danielhasan1/fastapi-listing) - 一个使用基于组件的架构、内置查询分页器、排序器、django-admin 等过滤器等来设计/构建列表 API 的库。
- [FastAPI MQTT](https://github.com/sabuhish/fastapi-mqtt) - MQTT 协议的扩展。
- [FastAPI Opentracing](https://github.com/wesdu/fastapi-opentracing) - FastAPI 的 Opentracing 中间件和数据库跟踪支持。
- [FastAPI Pagination](https://github.com/uriyyo/fastapi-pagination) - FastAPI 的分页。
- [FastAPI Plugins](https://github.com/madkote/fastapi-plugins) - Redis 和调度程序插件。
- [FastAPI ServiceUtils](https://github.com/skallfass/fastapi_serviceutils) - 用于创建 API 服务的生成器。
- [FastAPI Shield](https://github.com/jymchng/fastapi-shield) - 通用 FastAPI 库，用于编写任何能够进行惰性依赖注入的通用端点装饰器。
- [FastAPI SocketIO](https://github.com/pyropy/fastapi-socketio) - FastAPI 和 SocketIO 的轻松集成。
- [FastAPI Utilities](https://github.com/fastapiutils/fastapi-utils) - 可重用实用程序：基于类的视图、响应推断路由器、定期任务、定时中间件、SQLAlchemy 会话、OpenAPI 规范简化。
- [FastAPI Websocket Pub/Sub](https://github.com/authorizon/fastapi_websocket_pubsub) - 经典的发布/订阅模式可以通过网络和跨云实时轻松访问和扩展。
- [FastAPI Websocket RPC](https://github.com/authorizon/fastapi_websocket_rpc) - 通过 Websockets 的 RPC（双向 JSON RPC）变得简单、强大且可用于生产。
- [OpenTelemetry FastAPI Instrumentation](https://github.com/open-telemetry/opentelemetry-python-contrib/tree/main/instrumentation/opentelemetry-instrumentation-fastapi) - 库提供 FastAPI Web 框架的自动和手动检测，检测由使用该框架的应用程序提供的 http 请求。
- [Prerender Python Starlette](https://github.com/BeeMyDesk/prerender-python-starlette) - 用于 Prerender 的 Starlette 中间件。
- [Prometheus FastAPI Instrumentator](https://github.com/trallnag/prometheus-fastapi-instrumentator) - 适用于 FastAPI 应用程序的可配置和模块化 Prometheus Instrumentator。
- [SlowApi](https://github.com/laurents/slowapi) - 速率限制器（基于 [Flask-Limiter](https://flask-limiter.readthedocs.io)）。
- [Starlette Context](https://github.com/tomwojcik/starlette-context) - 允许您在项目中的任何位置存储和访问请求数据，这对于日志记录很有用。
- [Starlette Exporter](https://github.com/stephenhillier/starlette_exporter) - FastAPI 和 Starlette 的又一普罗米修斯集成。
- [Starlette OpenTracing](https://github.com/acidjunk/starlette-opentracing) - Opentracing 支持 Starlette 和 FastAPI。
- [Starlette Prometheus](https://github.com/perdy/starlette-prometheus) - FastAPI 和 Starlette 的 Prometheus 集成。
- [Strawberry GraphQL](https://github.com/strawberry-graphql/strawberry) - 基于数据类的 Python GraphQL 库。
- [Pydantic Resolve](https://github.com/allmonday/pydantic-resolve) - 通过引入解析和后处理挂钩，将 pydantic 类变成强大的可组合计算容器。

## 资源

### 官方资源

- [Documentation](https://fastapi.tiangolo.com/) - 全面的文档。
- [Tutorial](https://fastapi.tiangolo.com/tutorial/) - 官方教程向您展示如何逐步使用 FastAPI 及其大部分功能。
- [Source Code](https://github.com/fastapi/fastapi) - 托管在 GitHub 上。
- [Discord](https://discord.com/invite/VQjSZaeJmf) - 与其他 FastAPI 用户聊天。

### 外部资源

- [TestDriven.io FastAPI](https://testdriven.io/blog/topics/fastapi/) - 多篇特定于 FastAPI 的文章，重点关注开发和测试生产就绪的 RESTful API、提供机器学习模型等。

### 播客

- [Build The Next Generation Of Python Web Applications With FastAPI](https://www.pythonpodcast.com/fastapi-web-application-framework-episode-259/) - 在 [Podcast Init](https://www.pythonpodcast.com/) 的这一集中，FastAPI 的创建者 [Sebastián Ramirez](https://tiangolo.com/) 分享了他构建 FastAPI 的动机以及它的幕后工作方式。
- [FastAPI on PythonBytes](https://pythonbytes.fm/episodes/show/123/time-to-right-the-py-wrongs?time_in_sec=855) - 该项目的概述很好。

### 文章

- [FastAPI 对我来说永远毁了 Flask](https://medium.com/data-science/fastapi-has-ruined-flask-forever-for-me-73916127da)
- [Why we switched from Flask to FastAPI for production machine learning](https://medium.com/@calebkaiser/why-we-switched-from-flask-to-fastapi-for-production-machine-learning-765aab9b3679) - 深入了解您可能想要从 Flask 迁移到 FastAPI 的原因。

### 教程

- [Async SQLAlchemy with FastAPI](https://stribny.name/posts/fastapi-asyncalchemy/) - 了解如何异步使用 SQLAlchemy。
- [使用 Keras、FastAPI、Redis 和 Docker 部署机器学习模型](https://medium.com/analytics-vidhya/deploy-machine-learning-models-with-keras-fastapi-redis-and-docker-4940df614ece)
- [Developing and Testing an Asynchronous API with FastAPI and Pytest](https://testdriven.io/blog/fastapi-crud/) - 使用测试驱动开发，使用 FastAPI、Postgres、Pytest 和 Docker 开发和测试异步 API。
- [FastAPI for Flask Users](https://amitness.com/posts/fastapi-vs-flask) - 通过与 Flask 的并排代码比较来学习 FastAPI。
- [Implementing FastAPI Services – Abstraction and Separation of Concerns](https://camillovisini.com/coding/abstracting-fastapi-services) - FastAPI 应用程序和服务结构可实现更易于维护的代码库。
- [Introducing FARM Stack - FastAPI, React, and MongoDB](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/integrations/fastapi-integration/) - 开始使用完整的 FastAPI Web 应用程序堆栈。
- [Multitenancy with FastAPI, SQLAlchemy and PostgreSQL](https://mergeboard.com/blog/6-multitenancy-fastapi-sqlalchemy-postgresql/) - 了解如何使 FastAPI 应用程序做好多租户准备。
- [Porting Flask to FastAPI for ML Model Serving](https://www.pluralsight.com/tech-blog/porting-flask-to-fastapi-for-ml-model-serving/) - Flask 与 FastAPI 的比较。
- [Real-time data streaming using FastAPI and WebSockets](https://stribny.name/posts/real-time-data-streaming-using-fastapi-and-websockets/) - 了解如何将 FastAPI 中的数据直接流式传输到实时图表中。
- [Running FastAPI applications in production](https://stribny.name/posts/fastapi-production/) - 将 Gunicorn 与 systemd 结合使用进行生产部署。
- [Serving Machine Learning Models with FastAPI in Python](https://medium.com/@8B_EC/tutorial-serving-machine-learning-models-with-fastapi-in-python-c1a27319c459) - 使用 FastAPI 作为 RESTful API 快速轻松地部署 Python 中的机器学习模型并为其提供服务。
- [Streaming video with FastAPI](https://stribny.name/posts/fastapi-video/) - 了解如何提供视频流。
- [Using Hypothesis and Schemathesis to Test FastAPI](https://testdriven.io/blog/fastapi-hypothesis/) - 将基于属性的测试应用于 FastAPI。

### 会谈

- [PyConBY 2020: Serve ML models easily with FastAPI](https://www.youtube.com/watch?v=z9K5pwb0rt8) - 从 Sebastian Ramirez 的演讲中，您将了解如何使用 FastAPI 轻松为您的 ML 模型构建生产就绪的 Web (JSON) API，包括默认的最佳实践。
- [PyCon UK 2019: FastAPI from the ground up](https://www.youtube.com/watch?v=3DLwPcrE5mA) - 本演讲展示了如何使用 FastAPI 从头开始​​为数据库构建简单的 REST API。

### 视频

- [Building a Stock Screener with FastAPI](https://www.youtube.com/watch?v=5GorMC2lPpk) - 当您使用 FastAPI 构建基于 Web 的股票筛选器时，您将了解 FastAPI 的许多功能，包括 Pydantic 模型、依赖项注入、后台任务和 SQLAlchemy 集成。
- [Building Web APIs Using FastAPI](https://www.youtube.com/watch?v=Pe66M8mn-wA) - 使用FastAPI构建Web应用程序编程接口（RESTful API）。
- [FastAPI - A Web Framework for Python](https://www.youtube.com/watch?v=PUhio8CprhI&list=PL5gdMNl42qynpY-o43Jk3evfxEKSts3HS) - 了解如何使用 FastAPI 进行数字验证。
- [FastAPI vs. Django vs. Flask](https://www.youtube.com/watch?v=9YBAOYQOzWs) - 2020 年哪个框架最适合 Python？哪个使用 async/await 最好？哪个最快？
- [Serving Machine Learning Models As API with FastAPI](https://www.youtube.com/watch?v=mkDxuRvKUL8) - 使用 FastAPI 构建机器学习 API。

### 课程

- [Test-Driven Development with FastAPI and Docker](https://testdriven.io/courses/tdd-fastapi/) - 了解如何使用 Python、FastAPI 和 Docker 构建、测试和部署文本摘要微服务。
- [Modern APIs with FastAPI and Python](https://training.talkpython.fm/courses/modern-fastapi-apis) - 该课程旨在让您使用 FastAPI 快速创建在云中运行的新 API。
- [Full Web Apps with FastAPI Course](https://training.talkpython.fm/courses/full-html-web-applications-with-fastapi) - 您将学习使用 FastAPI 构建完整的 Web 应用程序，相当于使用 Flask 或 Django 所做的事情。
- [The Definitive Guide to Celery and FastAPI](https://testdriven.io/courses/fastapi-celery/) - 了解如何将 Celery 添加到 FastAPI 应用程序以提供异步任务处理。

### 最佳实践

- [FastAPI Best Practices](https://github.com/zhanymkanov/fastapi-best-practices) - GitHub 存储库中的最佳实践集合。
- [FastAPI-Dishka-FastStream](https://github.com/faststream-community/fastapi-dishka-faststream) - 结合了 FastAPI、dishka、faststream、sqlalchemy、pydantic。
- [FastAPI Clean Example](https://github.com/ivan-borovets/fastapi-clean-example) - 使用 FastAPI 构建的干净架构后端示例。

## 托管

### 平台即服务

（平台即服务）

- [AWS 弹性豆茎](https://aws.amazon.com/elasticbeanstalk/)
- [Fly](https://fly.io) ([教程](https://fly.io/docs/python/frameworks/fastapi/), [从 Git 存储库部署](https://github.com/fly-apps/hello-fastapi))
- [谷歌应用引擎](https://cloud.google.com/appengine)
- [Heroku](https://www.heroku.com/)（[分步教程](https://tutlinks.com/create-and-deploy-fastapi-app-to-heroku/)、[Heroku 上的 ML 模型教程](https://testdriven.io/blog/fastapi-machine-learning/))
- [微软Azure应用服务](https://azure.microsoft.com/en-us/products/app-service/)

### 基础设施即服务

（基础设施即服务）

- [AWS EC2](https://aws.amazon.com/ec2/)
- [谷歌计算引擎](https://cloud.google.com/compute)
- [数字海洋](https://www.digitalocean.com/)
- [Linode](https://www.linode.com/)

### 无服务器

框架：

- [Chalice](https://github.com/aws/chalice)
- [Mangum](https://mangum.io/) - 用于使用 AWS Lambda 和 API Gateway 运行 ASGI 应用程序的适配器。
- [Vercel](https://vercel.com/) - （以前称为 Zeit）（[示例](https://github.com/Snailedlt/Markdown-Videos)）。

计算：

- [AWS Lambda](https://aws.amazon.com/lambda/)（[示例](https://github.com/iwpnd/fastapi-aws-lambda-example)）
- [谷歌云功能](https://cloud.google.com/functions)
- [Azure 函数](https://azure.microsoft.com/en-us/products/functions/)
- [Google Cloud Run](https://cloud.google.com/run)（[示例](https://github.com/anthonycorletti/cloudrun-fastapi)）

## 项目

### 样板文件

- [Full Stack FastAPI and PostgreSQL - Base Project Generator](https://github.com/fastapi/full-stack-fastapi-template) - 全栈 FastAPI 模板
，其中包括 FastAPI、React、SQLModel、PostgreSQL、Docker、GitHub Actions、自动 HTTPS 等（由 FastAPI 的创建者 [Sebastián Ramírez](https://github.com/tiangolo) 开发）。
- [FastAPI and Tortoise ORM](https://github.com/prostomarkeloff/fastapi-tortoise) - 强大但简单的 Web API 模板，带有 FastAPI（作为 Web 框架）和 Tortoise-ORM（通过数据库轻松工作）。
- [FastAPI Model Server Skeleton](https://github.com/eightBEC/fastapi-ml-skeleton) - 用于为机器学习模型提供生产就绪服务的骨架应用程序。
- [cookiecutter-spacy-fastapi](https://github.com/microsoft/cookiecutter-spacy-fastapi) - 使用 FastAPI 快速部署 spaCy 模型。
- [cookiecutter-fastapi](https://github.com/arthurhenrique/cookiecutter-fastapi) - FastAPI 项目的 Cookiecutter 模板使用：机器学习、Poetry、Azure Pipelines 和 pytest。
- [openapi-python-client](https://github.com/openapi-generators/openapi-python-client) - 从 OpenAPI 生成现代 FastAPI Python 客户端（通过 FastAPI）。
- [Pywork](https://github.com/vutran1710/YeomanPywork) - [Yeoman](https://yeoman.io/) 生成器用于构建 FastAPI 应用程序。
- [fastapi-gino-arq-uvicorn](https://github.com/leosussan/fastapi-gino-arq-uvicorn) - Python 中的高性能异步 REST API 模板。 FastAPI + GINO + Arq + Uvicorn（带 Redis 和 PostgreSQL）。
- [FastAPI and React Template](https://github.com/Buuntu/fastapi-react) - 使用 FastAPI、TypeScript、Docker、PostgreSQL 和 React 的全栈 cookiecutter 样板。
- [FastAPI Nano](https://github.com/rednafi/fastapi-nano) - 具有工厂模式架构的简单 FastAPI 模板。
- [FastAPI template](https://github.com/s3rius/FastAPI-template) - 灵活、轻量级的 FastAPI 项目生成器。它包括对 SQLAlchemy、多个数据库、CI/CD、Docker 和 Kubernetes 的支持。
- [FastAPI on Google Cloud Run](https://github.com/anthonycorletti/cloudrun-fastapi) - 使用 FastAPI、SQLModel 和 Google Cloud Run 构建 API 的样板。
- [FastAPI with Firestore](https://github.com/anthonycorletti/firestore-fastapi) - 使用 FastAPI 和 Google Cloud Firestore 构建 API 的样板。
- [fastapi-alembic-sqlmodel-async](https://github.com/vargasjona/fastapi-alembic-sqlmodel-async) - 这是一个使用 FastAPI、Alembic 和异步 SQLModel 作为 ORM 的项目模板。
- [fastapi-starter-project](https://github.com/mirzadelic/fastapi-starter-project) - 使用 FastAPI、SQLModel、Alembic、Pytest、Docker、GitHub Actions CI 的项目模板。
- [Full Stack FastAPI and MongoDB - Base Project Generator](https://github.com/mongodb-labs/full-stack-fastapi-mongodb) - 全栈、现代 Web 应用程序生成器，包括 FastAPI、MongoDB、Docker、Celery、React 前端、自动 HTTPS 等。
- [Uvicorn Poetry FastAPI Project Template](https://github.com/max-pfeiffer/uvicorn-poetry-fastapi-project-template) - 用于启动 FastAPI 应用程序的 Cookiecutter 项目模板。在 Kubernetes 上使用 Uvicorn ASGI 服务器的 Docker 容器中运行。支持AMD64和ARM64 CPU架构。

### Docker 镜像

- [inboard](https://github.com/br3ndonland/inboard) - Docker 镜像可为您的 FastAPI 应用程序提供支持并帮助您更快地交付。
- [uvicorn-gunicorn-fastapi-docker](https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker) - 由 Gunicorn 管理的 Uvicorn 的 Docker 镜像，用于 Python 3.7 和 3.6 中的高性能 FastAPI Web 应用程序，并具有性能自动调整功能。
- [uvicorn-gunicorn-poetry](https://github.com/max-pfeiffer/uvicorn-gunicorn-poetry) - 带有 Gunicorn 的 Docker 镜像，使用 Uvicorn 工作线程来运行 Python Web 应用程序。使用 Poetry 管理依赖关系并设置虚拟环境。支持AMD64和ARM64 CPU架构。
- [uvicorn-poetry](https://github.com/max-pfeiffer/uvicorn-poetry) - 带有 Uvicorn ASGI 服务器的 Docker 镜像，用于在 Kubernetes 上运行 Python Web 应用程序。使用 Poetry 管理依赖关系并设置虚拟环境。支持AMD64和ARM64 CPU架构。

### 开源项目

- [Astrobase](https://github.com/anthonycorletti/astrobase) - 随时随地简单、快速、安全的部署。
- [Awesome FastAPI Projects](https://github.com/Kludex/awesome-fastapi-projects) - 使用 FastAPI 的项目的组织列表。
- [Bitcart](https://github.com/bitcart/bitcart) - 为商家、用户和开发人员提供轻松设置和使用的平台。
- [Bali](https://github.com/bali-framework/bali) - 基于FastAPI和gRPC简化云原生微服务开发。
- [Bunnybook](https://github.com/pietrobassi/bunnybook) - 一个使用 FastAPI、React+RxJs、Neo4j、PostgreSQL 和 Redis 构建的小型社交网络。
- [Coronavirus-tg-api](https://github.com/egbakou/coronavirus-tg-api) - 用于跟踪全球冠状病毒（COVID-19、SARS-CoV-2）爆发的 API。
- [Dispatch](https://github.com/Netflix/dispatch) - 管理安全事件。
- FastAPI CRUD 示例：
  - [异步风味](https://github.com/testdrivenio/fastapi-crud-async)
  - [同步风味](https://github.com/testdrivenio/fastapi-crud-sync)
- [FastAPI with Observability](https://github.com/Blueswen/fastapi-observability) - 通过 OpenTelemetry 和 OpenMetrics 在 Grafana 上观察具有可观测性三大支柱的 FastAPI 应用程序：跟踪 (Tempo)、指标 (Prometheus)、日志 (Loki)。
- [DogeAPI](https://github.com/yezz123/DogeAPI) - 具有高性能的 API，可使用 OAuth2PasswordBearer 创建简单的博客和 CRUD。
- [FastAPI Websocket Broadcast](https://github.com/kthwaite/fastapi-websocket-broadcast) - Websocket“广播”演示。
- [FastAPI with Celery, RabbitMQ, and Redis](https://github.com/GregaVrbancic/fastapi-celery) - 使用 FastAPI 和 Celery 以及 RabbitMQ 作为任务队列、Redis 作为 Celery 后端以及 Flower 来监控 Celery 任务的最小示例。
- [FuturamaAPI](https://github.com/koldakov/futuramaapi) - 采用最佳实践构建的 REST 和 GraphQL 游乐场，提供 WebSockets、SSE、回调、秘密消息等。
- [JeffQL](https://github.com/yezz123/JeffQL/) - 使用 GraphQL 和 JWT 的简单身份验证和登录 API。
- [JSON-RPC Server](https://github.com/smagafurov/fastapi-jsonrpc) - 基于 FastAPI 的 JSON-RPC 服务器。
- [Mailer](https://github.com/rclement/mailer) - 用于静态网站的极其简单的邮件程序微服务。
- [Markdown-Videos](https://github.com/Snailedlt/Markdown-Videos) - 用于生成缩略图以嵌入到 Markdown 内容中的 API。
- [Nemo](https://github.com/harshitsinghai77/nemo-backend) - 与 Nemo 一起提高工作效率。
- [OPAL (Open Policy Administration Layer)](https://github.com/authorizon/opal) - 开放策略之上的实时授权更新；使用 FastAPI、Typer 和 FastAPI WebSocket pub/sub 构建。
- [OSBot-Fast-API](https://github.com/owasp-sbot/OSBot-Fast-API) - 类型安全的 FastAPI 包装器，提供中间件、HTTP 事件跟踪、AWS Lambda 集成、测试实用程序以及 Type_Safe、Pydantic 和数据类之间的自动转换。
- [Polar](https://github.com/polarsource/polar) - 为开发者提供的融资和货币化平台，使用 FastAPI、SQLAlchemy、Alembic 和 Arq 构建。
- [现实世界示例应用程序 - mongo](https://github.com/markqiu/fastapi-mongodb-realworld-example-app)
- [现实世界示例应用程序 - postgres](https://github.com/nsidnev/fastapi-realworld-example-app)
- [redis-streams-fastapi-chat](https://github.com/leonh/redis-streams-fastapi-chat) - 一个简单的 Redis Streams 支持的聊天应用程序，使用 Websockets、Asyncio 和 FastAPI/Starlette。
- [Sprites as a service](https://github.com/ljvmiranda921/sprites-as-a-service) - 使用元胞自动机生成您的个人 8 位头像。
- [Slackers](https://github.com/uhavin/slackers) - Slack Webhooks API。
- [TermPair](https://github.com/cs01/termpair) - 通过端到端加密从浏览器查看和控制终端。
- [Universities](https://github.com/ycd/universities) - 用于获取全球超过 9600 所大学信息的 API 服务。

## 赞助商

请查看我们的赞助商来支持这个开源项目：

<a href="https://testdriven.io/courses/tdd-fastapi/?ref=awesome-fastapi" target="_blank" title="Learn to build high-quality web apps with best practices"><img src="images/testdriven.svg"></a>
