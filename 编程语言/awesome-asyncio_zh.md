> [!警告]
> 该项目正在寻找新家。我不再维护它了。
> 如果您想接管维护，请告诉我。
> 给我写一封电子邮件至 timo@furrer.life

# 很棒的异步 [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

> 精心策划的精彩 Python 异步框架、库、软件和资源列表。

Python 3.4 引入标准库的 Python [asyncio](https://docs.python.org/3/library/asyncio.html) 模块提供了使用协程编写单线程并发代码、通过套接字和其他资源复用 I/O 访问、运行网络客户端和服务器以及其他相关原语的基础结构。

Asyncio 并不是真正的全新技术，但几年来它似乎非常流行 - 特别是在 Python 社区以及 2014 年 3 月发布的 Python 3.4 中。
因此，要让自己及时了解最棒的软件包是非常困难的。
在这里找到一些*很棒的*包，如果您缺少一个，我们希望您根据您的建议[创建问题或拉取请求](https://github.com/timofurrer/awesome-asyncio/blob/master/CONTRIBUTING.md)。


## 内容

* [网络框架](#web-frameworks)
* [消息队列](#message-queues)
* [数据库驱动程序](#database-drivers)
* [Networking](#networking)
* [GraphQL](#graphql)
* [Testing](#testing)
* [替代循环](#alternative-loops)
* [Misc](#misc)
* [Writings](#writings)
* [Talks](#talks)
* [异步的替代方案](#alternatives-to-asyncio)

***

## 网络框架

*构建网络应用程序的库。*

* [FastAPI](https://github.com/tiangolo/fastapi) - 一个基于类型提示的高性能 Python 3.6+ API 框架。由 Starlette 和 Pydantic 提供支持。
* [Django](https://www.djangoproject.com/) - 一个成熟的高级 Python Web 框架，拥有庞大的社区和生态系统。
* [Starlette](https://github.com/encode/starlette) - 用于构建高性能服务的轻量级 ASGI 框架/工具包。
* [aiohttp](https://github.com/KeepSafe/aiohttp) - asyncio 的 Http 客户端/服务器 (PEP-3156)。
* [sanic](https://github.com/channelcat/sanic) - Python 3.5+ Web 服务器，专为快速运行而编写。
* [Quart](https://github.com/pallets/quart) - 一个 asyncio Web 微框架，具有与 Flask 相同的 API。
* [autobahn](https://github.com/crossbario/autobahn-python) - WebSocket 和 WAMP 支持 asyncio 和 Twisted，适用于客户端和服务器。
* [websockets](https://github.com/aaugustin/websockets/) - 一个用 Python 构建 WebSocket 服务器和客户端的库，重点关注正确性和简单性。
* [Tornado](http://www.tornadoweb.org/en/stable/) - 高性能 Web 框架和异步网络库。
* [uvicorn](https://github.com/encode/uvicorn) - 快如闪电的 ASGI 服务器。


## 消息队列

*使用消息队列实现应用程序的库。*

* [aioamqp](https://github.com/Polyconseil/aioamqp) - 使用 asyncio 实现 AMQP。
* [pyzmq](https://github.com/zeromq/pyzmq) - ZeroMQ 的 Python 绑定。
* [aiozmq](https://github.com/aio-libs/aiozmq) - 与 ZeroMQ 的替代 Asyncio 集成。
* [crossbar](https://github.com/crossbario/crossbar) - Crossbar.io 是一个用于分布式和微服务应用程序的网络平台。
* [asyncio-nats](https://github.com/nats-io/asyncio-nats) - NATS 消息系统的客户端。
* [aiokafka](https://github.com/aio-libs/aiokafka) - Apache Kafka 的客户端。

## 数据库驱动程序

*连接到数据库的库。*

* [asyncpg](https://github.com/MagicStack/asyncpg) - 适用于 Python/asyncio 的快速 PostgreSQL 数据库客户端库。
* [asyncpgsa](https://github.com/CanopyTax/asyncpgsa) - 具有 sqlalchemy 核心支持的 Asyncpg。
* [aiopg](https://github.com/aio-libs/aiopg/) - 用于访问 PostgreSQL 数据库的库。
* [aiomysql](https://github.com/aio-libs/aiomysql) - 用于访问 MySQL 数据库的库
* [aioodbc](https://github.com/aio-libs/aioodbc) - 用于访问 ODBC 数据库的库。
* [pymongo](https://github.com/mongodb/mongo-python-driver) - 官方 MongoDB Python 驱动程序，提供同步和异步 API。
* [redis-py](https://github.com/redis/redis-py) - Redis Python 客户端（现在包括 [aioredis](https://github.com/aio-libs/aioredis)）。
* [aiocouchdb](https://github.com/aio-libs/aiocouchdb) - CouchDB 客户端构建在 aiohttp (asyncio) 之上。
* [aioinflux](https://github.com/plugaai/aioinflux) - InfluxDB 客户端构建在 aiohttp 之上。
* [aioes](https://github.com/aio-libs/aioes) - 用于elasticsearch 的异步兼容驱动程序。
* [peewee-async](https://github.com/05bit/peewee-async) - 基于[peewee](https://github.com/coleifer/peewee)和aiopg的ORM实现。
* [GINO](https://github.com/fantix/gino) - 是一个基于 [SQLAlchemy](https://www.sqlalchemy.org/) 核心的轻量级异步 Python ORM，具有 [asyncpg](https://github.com/MagicStack/asyncpg) 方言。
* [Tortoise ORM](https://github.com/tortoise/tortoise-orm) - 原生多后端 ORM，具有类似 Django 的 API 和简单的关系管理。
* [Databases](https://github.com/encode/databases) - SQLAlchemy 核心的异步数据库访问，支持 PostgreSQL、MySQL 和 SQLite。
* [Prisma Client Python](https://github.com/RobertCraigie/prisma-client-py) - 由 Pydantic 提供支持并专为您的架构量身定制的自动生成的完全类型安全的 ORM - 支持 SQLite、PostgreSQL、MySQL、MongoDB、MariaDB 等。
* [Piccolo](https://github.com/piccolo-orm/piccolo) - 一个 ORM / 查询生成器，可以在异步和同步模式下工作，具有漂亮的管理 GUI 和 ASGI 中间件。
* [Beanie](https://beanie-odm.dev) - 基于 [pymongo](https://github.com/mongodb/mongo-python-driver) 和 [Pydantic](https://pydantic-docs.helpmanual.io) 构建的异步 MongoDB ODM。

## 网络

*在您的网络中进行通信的库。*

* [AsyncSSH](https://github.com/ronf/asyncssh) - 提供 SSHv2 协议的异步客户端和服务器实现。
* [aiodns](https://github.com/saghul/aiodns) - asyncio 的简单 DNS 解析器。
* [aioping](https://github.com/stellarbit/aioping) - ICMP (ping) 协议的快速异步实现。
* [httpx](https://github.com/encode/httpx) - Python 3 的异步 HTTP 客户端，具有与 [requests](https://github.com/psf/requests) 兼容的 API。

## GraphQL

*构建 GraphQL 服务器的库。*

* [Ariadne](https://ariadnegraphql.org) - 用于实现 GraphQL 服务器的模式优先 Python 库。
* [Tartiflette](https://tartiflette.io/) - 架构优先的 Python 3.6+ GraphQL 引擎构建在“libgraphqlparser”之上。
* [Strawberry](https://strawberry.rocks) - 代码优先的 Python 3 GraphQL 服务器，支持 Django、Flask 和 FastAPI/Starlette。

## 测试

*用于测试基于异步的应用程序的库。*

* [aiomock](https://github.com/nhumrich/aiomock/) - 一个支持异步方法的Python模拟库。
* [asynctest](https://github.com/Martiusweb/asynctest/) - 通过测试功能增强标准单元测试包。异步库
* [pytest-asyncio](https://github.com/pytest-dev/pytest-asyncio) - Pytest 对 asyncio 的支持。
* [aresponses](https://github.com/CircleUp/aresponses) - Asyncio http 模拟。类似于用于[请求](https://github.com/requests/requests)的[响应](https://github.com/getsentry/responses)库。
* [aioresponses](https://github.com/pnuckowski/aioresponses) - Python aiohttp 包中模拟/虚假 Web 请求的帮助程序。

## 替代循环

*替代异步循环实现。*

* [uvloop](https://github.com/MagicStack/uvloop) - 在 libuv 之上超快速实现 asyncio 事件循环。

## 杂项

*其他很棒的异步库。*

* [aiochan](https://github.com/zh217/aiochan) - CSP 风格的并发，具有基于 asyncio 的通道、选择和多处理。
* [aiocache](https://github.com/argaen/aiocache) - 不同后端的缓存管理器。
* [aiofiles](https://github.com/Tinche/aiofiles/) - 对 asyncio 的文件支持。
* [aiopath](https://github.com/alexdelorenzo/aiopath) - asyncio 的异步“pathlib”。
* [aiodebug](https://github.com/qntln/aiodebug) - 一个用于监视和测试异步程序的小型库。
* [aiorun](https://github.com/cjrh/aiorun) - `run()` 函数处理所有常见的启动和正常关闭的样板文件。
* [aiosc](https://github.com/artfwo/aiosc) - 轻量级开放声音控制实现。
* [aioserial](https://github.com/changyuheng/aioserial) - [pySerial](https://github.com/pyserial/pyserial) 的直接替代品。
* [aiozipkin](https://github.com/aio-libs/aiozipkin) - 使用 zipkin 进行 asyncio 的分布式跟踪工具
* [asgiref](https://github.com/django/asgiref) - 用于 ASGI 到 WSGI 集成的后端实用程序，包括sync_to_async 和 async_to_sync 函数包装器。
* [async_property](https://github.com/ryananguiano/async_property) - 用于异步属性的 Python 装饰器。
* [ruia](https://github.com/howie6879/ruia) - 一个基于 asyncio 的异步网页抓取微框架。
* [kubernetes_asyncio](https://github.com/tomplus/kubernetes_asyncio) - Kubernetes 的异步客户端库。
* [aiomisc](https://github.com/aiokitchen/aiomisc) - “asyncio”的其他实用程序。
* [taskiq](https://taskiq-python.github.io/) - 异步分布式任务管理器（如 celery，但异步）。

## 著作

*有关 asyncio 的文档、博客文章和其他精彩文章。*

* [Official asyncio documentation](https://docs.python.org/3/library/asyncio.html) - 异步 I/O、事件循环、协程和任务。
* [Short well-written intro to asyncio](https://masnun.com/python-generators-coroutines-native-coroutines-and-async-await/) - 生成器、协程、本机协程和异步/等待。
* [AsyncIO for the Working Python Developer](https://hackernoon.com/asyncio-for-the-working-python-developer-5c468e6e2e8e) - 从基本示例到 URL 获取，对异步编程进行了简要介绍。
* [Test limits of Python aiohttp](https://pawelmhm.github.io/asyncio/python/aiohttp/2016/04/22/asyncio-aiohttp.html) - 使用 python-aiohttp 发出 100 万个请求。
* [ASGI (Asynchronous Server Gateway Interface)](https://asgi.readthedocs.io/en/latest/) - WSGI 的精神继承者，旨在在支持异步的 Python Web 服务器、框架和应用程序之间提供标准接口。
* [First Principles Introduction to Asyncio](https://hackernoon.com/a-simple-introduction-to-pythons-asyncio-595d9c9ecf8c) - 对 asyncio 内部工作原理的非流行语第一原理介绍。
* [Developing and Testing an Asynchronous API with FastAPI and Pytest](https://testdriven.io/blog/fastapi-crud/) - 本教程介绍如何使用测试驱动开发 (TDD) 使用 FastAPI 来开发和测试异步 API。
* [Python Concurrency with asyncio](https://www.manning.com/books/python-concurrency-with-asyncio) - 了解如何使用并发编程和尖端的 asyncio 库来加速缓慢的 Python 代码。

## 会谈

*有关 asyncio 的精彩演讲的录音。*

* [感兴趣的主题 (Python Asyncio)](https://youtu.be/ZzfHjytDceU) | [截屏视频](https://youtu.be/lYe8W04ERnY) | [幻灯片](https://speakerdeck.com/dabeaz/topics-of-interest-async) - PyCon Brasil 2015 主题演讲 (David Beazley)。
* [Python Asynchronous I/O Walkthrough](https://www.youtube.com/playlist?list=PLpEcQSRWP2IjVRlTUptdD05kG-UkJynQT) - 8 部分代码演练（PhilipGuo）。
* [Async/await in Python 3.5 and why it is awesome](https://www.youtube.com/watch?v=m28fiN9y_r8&t=132s) - EuroPython 2016（尤里·塞利瓦诺夫）。
* [异步中的恐惧与等待：协程梦想之心的野蛮之旅](https://www.youtube.com/watch?v=E-1Y4kSsAFc) | [截屏视频](https://www.youtube.com/watch?v=Bm96RqNGbGo) - PyOhio 2016 主题演讲 (David Beazley)。
* [适合初学者的异步 Python](https://www.youtube.com/watch?v=iG6fr81xHKA) | [幻灯片](https://speakerdeck.com/pycon2017/miguel-grinberg-asynchronous-python-for-the-complete-beginner) - PyCon 2017 (Miguel Grinberg)。
* [Demystifying Python's Async and Await Keywords](https://www.youtube.com/watch?v=F19R_M4Nay4) - JetBrains TV 2020（迈克尔·肯尼迪）

## 异步的替代方案

*Python 中异步编程的替代方法，其中一些尝试支持与“asyncio”的某些兼容性，另一些则根本不兼容。*

* [curio](https://github.com/dabeaz/curio) - 协程并发库。
  * [Curio-Asyncio Bridge](https://github.com/dabeaz/curio/issues/190) - 基本 curio -> asyncio 协程桥。
* [trio](https://github.com/python-trio/trio) - 适用于人类和蛇人的 Pythonic 异步 I/O。
  * [trio-asyncio](https://github.com/python-trio/trio-asyncio) - 在 Trio 之上重新实现 asyncio mainloop。
* [AnyIO](https://github.com/agronholm/anyio) - 在 trio 或 asyncio 之上工作的高级异步并发和网络框架。
