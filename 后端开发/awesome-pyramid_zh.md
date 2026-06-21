# 令人敬畏的金字塔
[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
[！[IRC
Freenode](https://img.shields.io/badge/irc-freenode-blue.svg)](https://webchat.freenode.net/?channels=pyramid)

精彩金字塔应用程序、项目和资源的精选列表。灵感来自和
基于[awesome-python](https://github.com/vinta/awesome-python/)。

- [令人敬畏的金字塔](#awesome-pyramid)
    - [管理界面](#admin-interface)
    - [资产管理](#asset-management)
    - [Async](#async)
    - [Authentication](#authentication)
    - [Authorization](#authorization)
    - [缓存和会话](#caching--session)
    - [Debugging](#debugging)
    - [Email](#email)
    - [Forms](#forms)
    - [Media-Management](#media-management)
    - [RESTful API](#restful-api)
    - [Search](#search)
    - [Security](#security)
    - [Services](#services)
    - [Settings](#settings)
    - [Storage](#storage)
    - [任务队列](#task-queue)
    - [Testing](#testing)
    - [Translations](#translations)
    - [Web 前端集成](#web-frontend-integration)
    - [Workflows](#workflows)
    - [Other](#other)
- [Projects](#projects)
    - [Framework](#framework)
    - [CMS](#cms)
    - [Cookiecutters](#cookiecutters)
    - [e-Commerce](#e-commerce)
    - [项目管理](#project-management)
    - [Other](#other)
- [Resources](#resources)
    - [Books](#books)
    - [Websites](#websites)
    - [Conferences](#conferences)
    - [Videos](#videos)
    - [谁使用它？](#who-uses-it)
- [Contributing](#contributing)

## 管理界面

*扩展管理界面、添加或改进功能的软件包。*

* [pyramid_formalchemy](https://github.com/FormAlchemy/pyramid_formalchemy) - 
基于FormAlchemy为金字塔提供CRUD接口。
* [pyramid_sacrud](https://github.com/sacrud/pyramid_sacrud) - 金字塔 CRUD 接口。
为 Pyramid 提供管理 Web 界面。
与经典的 CRUD 不同，pyramid_sacrud 允许覆盖和灵活性
自定义您的界面，类似于 django.contrib.admin 但使用
不同的后端提供资源。 [新架构](
<http://pyramid-sacrud.readthedocs.io/pages/contribute/architecture.html>）
建立在资源和机制遍历的基础上，允许在各种情况下使用它。
    * [ps_alchemy](https://github.com/sacrud/ps_alchemy) - Pyramid_sacrud 的扩展
它提供了 SQLAlchemy 模型。
    * [ps_tree](https://github.com/sacrud/ps_tree) - 扩展为
[pyramid_sacrud](https://github.com/sacrud/pyramid_sacrud) 显示
作为树的记录列表。这适用于以下模型
[sqlalchemy_mptt](https://github.com/uralbash/sqlalchemy_mptt)。
* [Websauna](https://websauna.org/docs/) - Pyramid 的全栈应用框架

## 资产管理

*帮助管理项目静态资产的包。*

* [pyramid_webassets](https://github.com/sontek/pyramid_webassets) - 金字塔
用于使用 webassets 库的扩展。
* [pyramid_bowerstatic](https://github.com/mrijken/pyramid_bowerstatic) - 
将 Bowerstatic 集成到 Pyramid 中

## 异步

* [aiopyramid](https://github.com/housleyjk/aiopyramid) - 使用运行金字塔
异步。
* [gevent-socketio](https://github.com/abourget/gevent-socketio) - 
gevent-socketio 是 Socket.IO 协议的 Python 实现，
最初由 LearnBoost 为 Node.js 开发，然后移植到其他
语言。
* [Stargate](https://github.com/boothead/stargate) - Stargate 是一个软件包
使用优秀的方法向金字塔应用程序添加 WebSockets 支持
用于长时间运行连接的 eventlet 库。
* [channelstream](https://github.com/AppEnlight/channelstream) - websocket 通信服务器（gevent）。

## 认证

*改进或扩展 Pyramid 身份验证方法的软件包。*

* [pyramid_ldap](https://github.com/Pylons/pyramid_ldap) - LDAP
Pyramid 的身份验证策略。
* [pyramid_ldap3](https://github.com/Cito/pyramid_ldap3) - 提供 LDAP 身份验证
基于 ldap3 包的 Pyramid 应用程序的服务。
* [pyramid_who](https://github.com/Pylons/pyramid_who) - 认证策略
使用 repoze.who 2.0 API 进行金字塔。
* [velruse](https://github.com/bbangert/velruse) - 简化第三方
Web 应用程序的身份验证。它支持大多数身份验证
[提供商](https://github.com/bbangert/velruse/tree/master/velruse/providers)。
* [pyramid_simpleauth](https://github.com/thruflo/pyramid_simpleauth) - 会议
Pyramid 应用程序基于身份验证和基于角色的安全性
* [Python Social Auth](https://github.com/omab/python-social-auth) - 社交
支持大量的认证/注册机制
[提供商](https://github.com/omab/python-social-auth#auth-providers)。
* [Authomatic](https://github.com/authomatic/authomatic) - 简单而强大
Python Web 应用程序的授权/身份验证客户端库。
* [apex](https://github.com/cd34/apex) - Pyramid 工具包，一个 Pylons 项目，
使用 Velruse (OAuth) 和/或本地添加身份验证和授权
数据库、CSRF、ReCaptcha、会话、Flash 消息和 I18N。
* [pyramid_authsanity](https://github.com/usingnamespace/pyramid_authsanity) - 
这将使安全身份验证策略变得更简单，并且易于使用
使用后端。
* [pyramid_jwt](https://github.com/wichert/pyramid_jwt) - 这个套餐
使用 [JSON Web Tokens] 实现 Pyramid 的身份验证策略。
该标准（[RFC 7519]）通常用于保护后端 API。的
优秀的[PyJWT]库用于JWT编码/解码逻辑。
* [pyramid_ipauth](https://github.com/mozilla-services/pyramid_ipauth) - 
基于远程IP地址的金字塔认证策略。

[JSON Web 令牌]：https://jwt.io/
[RFC 7519]：https://tools.ietf.org/html/rfc7519
[PyJWT]：https://pyjwt.readthedocs.io/en/latest/


## 授权

*与授权基础设施和权限相关的包。*

* [ziggurat_foundations](https://github.com/ergo/ziggurat_foundations) - 
与框架无关的 sqlalchemy 类集，用于构建应用程序
需要权限的任务很简单。
* [pyramid_multiauth](https://github.com/mozilla-services/pyramid_multiauth) - 
代理堆栈的 Pyramid 的身份验证策略
身份验证策略。
* [pyramid_authstack](https://github.com/wichert/pyramid_authstack) - 使用
Pyramid 的多种身份验证策略。
* [horus](https://github.com/Pylons/horus) - 用户注册及登录系统
适用于 Pyramid Web 框架。
* [pyramid_yosai](https://github.com/YosaiProject/pyramid_yosai) - Pyramid 与 Python 应用程序安全框架集成，具有授权（rbac 权限和角色）、身份验证（2fa totp）、会话管理和广泛的审计跟踪 https://yosaiproject.github.io/yosai/

## 缓存和会话

*有助于缓存和会话的包。*

* [pyramid_beaker](https://github.com/Pylons/pyramid_beaker) - 烧杯会议
Pyramid 的工厂后端，也是缓存配置器。
* [为什么你想切换到
[dogpile.cache](http://techspot.zzzeek.org/2012/04/19/using-beaker-for-caching-why-you-ll-want-to-switch-to-dogpile.cache/)
* [pyramid_redis_sessions](https://github.com/ericrasmussen/pyramid_redis_sessions) - 
由 Redis 支持的 Pyramid Web 框架会话工厂。
* [pyramid_dogpile_cache](https://github.com/moriyoshi/pyramid_dogpile_cache) - 
Pyramid的dogpile.cache配置包
* [pyramid_sessions](https://github.com/joulez/pyramid_sessions) - 多个
Pyramid Web 框架的会话支持
* [pyramid_nacl_session](https://github.com/Pylons/pyramid_nacl_session) - 
定义一个加密的、基于pickle的cookie序列化器，使用
[PyNacl](http://pynacl.readthedocs.io/en/latest/secret/) 生成
cookie 状态的对称加密。

## 调试

*帮助寻找错误的软件包。*

* [pyramid_debugtoolbar](https://github.com/Pylons/pyramid_debugtoolbar) - 
提供了一个调试工具栏，在您开发 Pyramid 时非常有用
应用程序。
* [pyramid_exclog](https://github.com/Pylons/pyramid_exclog) - 一个包，其中
记录金字塔应用程序的异常。
* [pyramid_debugtoolbar_dogpile](https://github.com/jvanasco/pyramid_debugtoolbar_dogpile) - 
对pyramid_debugtoolbar 的dogpile 缓存支持
* [pyramid_ipython](https://github.com/Pylons/pyramid_ipython) - Python
Pyramid 的 pshell 的绑定
* [pyramid_bpython](https://github.com/Pylons/pyramid_bpython) - 蟒蛇
Pyramid 的 pshell 的绑定
* [pyramid_pycallgraph](https://github.com/disko/pyramid_pycallgraph) - 金字塔补间为每个请求生成调用图图像

## 电子邮件

*帮助管理电子邮件发送的软件包。*

* [pyramid_mailer](https://github.com/Pylons/pyramid_mailer) - 一个包用于
从您的 Pyramid 应用程序发送电子邮件。
* [pyramid_marrowmailer](https://github.com/domenkozar/pyramid_marrowmailer) - 
marrow.mailer 的 Pyramid 集成包，以前称为 TurboMail
* [pyramid_mailgun](https://github.com/evannook/pyramid_mailgun) - Pyramid 框架的 Mailgun 集成。

## 表格

*扩展表单功能或添加新类型表单的包。*

* [deform](https://github.com/Pylons/deform) - 是一个Python HTML表单生成
图书馆。
* [colander](https://github.com/Pylons/colander) - A
用于字符串、映射和的序列化/反序列化/验证库
列表。
* [WTForms](https://github.com/wtforms/wtforms) - 是一种灵活的形式
用于 python Web 开发的验证和渲染库。
* [ColanderAlchemy](https://github.com/stefanofontanelli/ColanderAlchemy) - 
帮助您自动生成基于 SQLAlchemy 的 Colander 模式
映射的类。
* [marshmallow](https://github.com/marshmallow-code/marshmallow) - A
用于将复杂对象与简单 Python 相互转换的轻量级库
数据类型（即（反）序列化和验证）。

## 媒体管理

* [pyramid_elfinder](https://github.com/uralbash/pyramid_elfinder) - 这是
elfinder 文件管理器的连接器，为金字塔框架编写。
* [pyramid_storage](https://github.com/danjac/pyramid_storage) - 这是一个用于在 Pyramid 框架应用程序中处理文件上传的包。

## RESTful API

*用于开发 RESTful API 的软件包。*

* [cornice](https://github.com/Cornices/cornice) - 提供帮助者
使用 Pyramid 构建和记录 REST-ish Web 服务，并具有不错的默认值
行为。它负责以自动化方式遵循 HTTP 规范
尽可能的方式。
* [rest_toolkit](https://github.com/wichert/rest_toolkit) - 是一个Python包
它提供了一种非常方便的方式来构建REST服务器。它是建立在
金字塔顶端，但你不需要了解太多金字塔就能使用
休息工具包。
* [pyramid_royal](https://github.com/hadrien/pyramid_royal) - 皇家是一个
金字塔扩展可以简化 RESTful Web 应用程序的编写。
* [cliquet](https://github.com/mozilla-services/cliquet) - Cliquet 是一个工具包
简化 HTTP 微服务的实施，例如数据驱动的 REST
API。
* [webargs](https://github.com/sloria/webargs) - 一个友好的解析库
HTTP 请求参数，内置对流行 Web 框架的支持。
* [ramses](https://github.com/ramses-tech/ramses) - 使用生成 RESTful API
拉姆。它使用 Nefertari 提供 ElasticSearch 支持的视图。
* [nefertari](https://github.com/ramses-tech/nefertari) - 奈菲尔塔莉是一个休息者
API 框架位于 Pyramid 和 ElasticSearch 之上。
* [pyramid_swagger](https://github.com/striglia/pyramid_swagger) - 方便
使用 Swagger 定义和验证 Pyramid Web 应用程序中的接口的工具。 （Swagger 2.0文档）
* [pyramid-openapi3](https://github.com/niteoweb/pyramid_openapi3) - 根据 OpenAPI 3.0 文档验证金字塔视图。与 Pyramid_swagger 类似，但适用于 OpenAPI 3.0。
* [pyramid_jsonapi](https://github.com/colinhiggs/pyramid-jsonapi) - 自动
使用以下命令从数据库创建 [JSON API](http://jsonapi.org/) 标准 API
sqlAlchemy ORM 和金字塔框架。
* [pyramid_apispec](https://github.com/ergo/pyramid_apispec) - 创建一个开放API
使用 apispec 和 Marshmallow 模式的规范文件。


## 搜索

*为项目提供搜索功能的包。*

* [hypatia](https://github.com/Pylons/hypatia) - Python 索引和
搜索系统。

## 安全性

*提高项目安全性的软件包。*

## 服务

* [pyramid_sms](https://github.com/websauna/pyramid_sms) - 
Pyramid Web 框架的 SMS 服务。

## 设置

*帮助管理项目可配置性的包。*

* [pyramid_zcml](https://github.com/Pylons/pyramid_zcml) - Zope配置
Pyramid 的标记语言配置支持。
* [pyramid_services](https://github.com/mmerickel/pyramid_services) - 定义了一个
用于访问可插入服务层的模式和辅助方法
在您的金字塔应用程序中。
* [hupper](https://github.com/Pylons/hupper) - 为开发人员提供的进程监视器/重新加载器
可以监视文件的更改并重新启动进程。

## 存储

*扩展现有存储后端功能的软件包或
提供新的存储后端。*

* [pyramid_tm](https://github.com/Pylons/pyramid_tm) - 集中交易
Pyramid 应用程序的管理（无中间件）。
* [zope.sqlalchemy](https://github.com/zopefoundation/zope.sqlalchemy) - 
SQLAlchemy 与事务管理的集成。
* [Zope 事务管理器对我意味着什么（以及
你）]（https://metaclassical.com/what-the-zope-transaction-manager-means-to-me-and-you/）
* [pyramid_sqlalchemy](https://github.com/wichert/pyramid_sqlalchemy) - 
提供了一些基本的粘合剂，以方便将 SQLAlchemy 与 Pyramid 结合使用。
* [pyramid_zodbconn](https://github.com/Pylons/pyramid_zodbconn) - 佐德数据库
Pyramid 的数据库连接管理。
* [pyramid_mongoengine](https://github.com/marioidival/pyramid_mongoengine) - 
基于flask-mongoengine的pyramid-mongoengine包
* [pyramid_mongodb](https://github.com/niallo/pyramid_mongodb) - 
基本 Pyramid Scaffold 可轻松使用 MongoDB 与 Pyramid Web 框架进行持久化
* [pyramid-excel](https://github.com/pyexcel-webwares/pyramid-excel) - Pyramid-Excel 基于 [pyexcel](https://github.com/pyexcel/pyexcel)，可以轻松使用/生成通过 HTTP 协议以及文件系统存储在 Excel 文件中的信息。该库可以将excel数据转换为列表列表、记录列表（字典）、列表字典。反之亦然。因此，它可以让您专注于基于金字塔的 Web 开发中的数据，而不是文件格式。

## 任务队列

*使任务/后台队列的使用变得更容易的软件包。*

* [pyramid_celery](https://github.com/sontek/pyramid_celery) - 金字塔
与 celery 集成的配置。允许您使用金字塔 .ini 文件
配置 celery 并在 celery 任务中进行金字塔配置。
* [pyramid_rq](https://github.com/wichert/pyramid_rq) - 支持使用rq
带金字塔的排队系统。最简单的监控和使用方式
Pyramid 项目中的 [RQ](http://python-rq.org)。

## 模板

* [pyramid_mako](https://github.com/Pylons/pyramid_mako) - Mako 模板
Pyramid Web 框架的系统绑定。
* [pyramid_chameleon](https://github.com/Pylons/pyramid_chameleon) - 变色龙
金字塔的模板编译器。
* [pyramid_jinja2](https://github.com/Pylons/pyramid_jinja2) - 金贾2
Pyramid Web 框架的模板系统绑定。
* [Tonnikala](https://github.com/ztane/Tonnikala) - Python 模板引擎
与金字塔集成
* [Kajiki](https://github.com/nandoflorestan/kajiki) - 提供快速格式良好的 XML 模板，具有 [Pyramid 集成](https://github.com/nandoflorestan/kajiki/blob/master/kajiki/integration/pyramid.py)

## 测试

*帮助测试代码或生成测试数据的包。*

* [webtest](https://github.com/Pylons/webtest) - 包装任何 WSGI 应用程序并且
无需启动即可轻松向该应用程序发送测试请求
HTTP 服务器。

## 翻译

*软件包有助于完成项目翻译任务。*

* [lingua](https://github.com/wichert/lingua) - Lingua 是一个包含工具的软件包
从代码中提取可翻译的文本，并检查现有的
翻译。它取代了 gettext 中 xgettext 命令的使用，或者
来自 Babel 的 pybabel。
* [pyramid_i18n_helper](https://github.com/sahama/pyramid_i18n_helper) - 帮助程序创建新的 smgid 并将 msgid 翻译为本地语言。

## Web 前端集成

* [PyramidVue](https://github.com/eddyekofo94/pyramidVue) - Pyramid 和 VueJs (JavaScript) 模板以及热模块替换入门模板。

## 工作流程

*进行流程、程序和/或业务任务管理的软件包。*

## 其他

* [pyramid_layout](https://github.com/Pylons/pyramid_layout) - 金字塔附加组件
用于管理 UI 布局。
* [pyramid_skins](https://github.com/Pylons/pyramid_skins) - 这个套餐
提供了一个简单的框架来将代码与模板和资源集成。
* [waitress](https://github.com/Pylons/waitress) - 女服务员本来就是一个
生产质量的纯 Python WSGI 服务器，具有非常可接受的性能。
除了 Python 标准库中的依赖项之外，它没有任何依赖项。
* [pyramid_handlers](https://github.com/Pylons/pyramid_handlers) - 类似物
Pyramid 的 Pylons 式“控制器”。
* [pyramid_rpc](https://github.com/Pylons/pyramid_rpc) - RPC 服务附加组件
Pyramid，以比pyramid_xmlrpc更可扩展的方式支持XML-RPC
支持 JSON-RPC 和 AMF。
* [pyramid_autodoc](https://github.com/SurveyMonkey/pyramid_autodoc) - 狮身人面像
用于记录 Pyramid API 的扩展。
* [pyramid_pages](https://github.com/uralbash/pyramid_pages) - 提供了一个
Pyramid 应用程序的树页面集合。这非常相似
到 django.contrib.flatpages 但具有树结构和遍历算法
在 URL 调度中。
* [paginate](https://github.com/Pylons/paginate) - Python 分页模块。
* [pyramid_tablib](https://github.com/lxneng/pyramid_tablib) - tablib渲染器
（xlsx、xls、csv）用于金字塔
* [tomb_routes](https://github.com/sontek/tomb_routes) - 简单的实用程序库
围绕金字塔路由
* [pyramid_extdirect](https://github.com/jenner/pyramid_extdirect) - 这个金字塔插件为 ExtJS 中包含的 ExtDirect Sencha API 提供了一个路由器。 ExtDirect 允许直接通过 JavaScript 运行服务器端回调，无需额外的 AJAX 样板。
* [pyramid_retry](https://github.com/Pylons/pyramid_retry) - Pyramid_retry 是 Pyramid 的执行策略，它包装请求，并可以在向客户端指示失败之前在某些“可重试”错误条件下重试可配置的次数。

# 项目

*杰出的金字塔项目。*

## 框架

* [Ringo](http://www.ringo-framework.org/) - Ringo是一个基于Python的高级
Web 应用程序框架构建在金字塔之上。该框架可以使用
构建基于表单的管理或管理软件。
* [cone.app](https://github.com/conestack/cone.app) - 金字塔顶部的综合 Web 应用程序存根。

## 内容管理系统

* [nive_cms](https://github.com/nive/nive_cms) - Nive 很专业
基于python的移动和桌面网站的盒子内容管理系统
和网络框架金字塔。请参阅网站 cms.nive.co 了解
详细信息。
* [substanced](https://github.com/Pylons/substanced) - 应用服务器
建立在 Pyramid Web 框架之上。它提供了一个用户界面
管理内容以及库和实用程序，这使得您可以轻松地
创建应用程序。
* [Kotti](https://github.com/Kotti/Kotti) - 一个用户友好、重量轻且
可扩展的网络内容管理系统。基于 Pyramid 和 SQLAlchemy。
* [KARL](https://karlproject.readthedocs.io/en/latest/) - 一个中等大小的
应用程序（大约 80K 行 Python 代码）构建在 Pyramid 之上。它是
一个开源网络
用于协作、组织内联网和知识管理的系统。
它提供维基、日历、手册、搜索、标记、
评论和文件上传。请参阅 KARL 站点进行下载和安装
详细信息。
  
## 饼干切割机

* [Pylons](https://github.com/Pylons?q=cookiecutter) - 官方 cookiecutter 模板
* [Pyramid Runner](https://github.com/asif-mahmud/pyramid_runner) - 最小金字塔
脚手架旨在提供一个入门模板来构建小型到大型的 Web 服务。
  
* 基于遍历的应用程序
* 仅 JSON 响应
* JWT认证策略
* Alembic 用于数据库修订
* 对基础测试、视图和模型基础进行一些简单修改以减少打字


## 电子商务

## 其他

* [cluegun](https://github.com/Pylons/cluegun) - 一个简单的pastebin应用程序
基于洛基·伯特的 ClueBin。它演示了表单处理、安全性和
在 Pyramid 应用程序中使用 ZODB。
* [shootout](https://github.com/Pylons/shootout) - 一个例子“想法
Carlos de la Guardia 和 Lukasz Fidosz 的“竞赛”申请。它
演示 URL 调度、简单身份验证、与 SQLAlchemy 的集成
和pyramid_simpleform。
* [virginia](https://github.com/Pylons/virginia) - 一个非常简单的动态
文件渲染应用程序。它愿意呈现结构化文本
文件系统目录中的文档、HTML 文档和图像。也是
遍历的一个很好的例子。该应用程序的早期版本运行
repoze.org 网站。
* [Akhet](https://docs.pylonsproject.org/projects/akhet/en/latest/) - A
Pyramid 库和演示应用程序具有类似 Pylons 的感觉。其最为人所知的
其以前的应用程序支架帮助用户从
Pylons 和那些更喜欢类似 Pylons 的 API 的人。脚手架已经
已退役，但演示版起着类似的作用。
* [Khufu Project](http://khufuproject.github.io/) - 胡夫是一个应用程序
Pyramid 的脚手架提供了与 Jinja2 一起使用的环境
SQL炼金术。
* [Ptah](https://github.com/ptahproject/ptah) - Ptah 是一个快速、有趣、开放的
源码高级Python Web开发环境。
* [warehouse](https://github.com/pypa/warehouse) - 仓库是下一个
旨在替换遗留代码库的生成Python包存储库
目前为 PyPI 提供支持。
* [travelcrm](https://github.com/mazvv/travelcrm) - TravelCRM 是一款有效的免费开源应用程序，适用于从小型到大型网络的各级旅行社的客户关系自动化。
* [RhodeCode](https://rhodecode.com/) - 企业源代码管理平台。它跨 Mercurial、Git 和 Subversion 存储库应用统一的用户控制、权限、代码审查和工具集成。世界各地不断壮大的大型软件团队都使用 RhodeCode 在安全的防火墙后环境中进行协作。

## 项目管理

* [AppEnlight](https://getappenlight.com/) - Web 的性能、异常和正常运行时间监控

# 资源

在哪里发现新的金字塔应用程序和项目。

## 书籍

* [Python Web Frameworks](http://www.oreilly.com/web-platform/free/python-web-frameworks.csp) - 深入了解顶部的详细信息
六个 Python 框架：Django、Flask、Tornado、Bottle、Pyramid 和 CherryPy。

## 网站

* [Try Pyramid](https://trypyramid.com/) - 小起点，大完成，
保持完成的框架。官方网站。

## 会议

* [Sushi Sprint 在日本东京举行的 PloneConf 2018](https://2018.ploneconf.org/sprints)（2018 年 11 月 10 日至 11 日）
* [德国慕尼黑金字塔研讨会](https://pyconweb.com/talks/28-05-2017/pyramid-workshop)（2017年5月28日上午10:30 - 中午12:30）
* [PloneConf 2017](https://2017.ploneconf.org/) - 巴塞罗那Plone数字体验大会（2017年10月16日~22日）
* [PloneConf 2016](https://2016.ploneconf.org/) - 波士顿Plone数字体验大会（2016年10月17日至23日）
* [DragonSprint 2016](http://dragonsprint.com/) - DragonSprint 是 Pyramid 上为期一周的冲刺。冲刺赛将于 12 月第一周（5 日至 9 日）在欧盟斯洛文尼亚卢布尔雅那举行。主要的两个冲刺主题是 Pyramid 2.0 和 Pyramid for Newcomers。


## 视频
* [官方网站的视频列表](https://docs.pylonsproject.org/projects/pyramid_cookbook/en/latest/misc/videos.html)
* [Talk Python Training 的在线视频课程](https://training.talkpython.fm/courses/all)
* [使用 Python 和金字塔的 Web 应用程序
框架](http://shop.oreilly.com/product/0636920041900.do) -
在此 Web 应用程序中使用 Python 和 Pyramid Framework 进行培训
当然，专家作者 Paul Everitt 将教您所需的功能
用于 Python Web 开发，以及 Pyramid 的独特功能。这个
课程专为已经具备 Python 基础知识的用户而设计。

您将首先了解单文件 Web 应用程序、模板和
多条路线和视图。从那里，Paul 将教您有关 MyApp
Python 包、视图和路由以及模板和静态资源。这个
视频教程还涵盖表单、数据库、会话、身份验证
和授权，以及 JSON。最后，您将了解可扩展性，
包括自定义配置设置、扩展和覆盖，以及
自定义视图谓词。

完成此基于计算机的培训课程后，您将拥有
对 Python Web 所需的功能有了基本的了解
Pyramid 的开发和独特功能。

## 谁使用它？

* [使用的项目、网站、公司和组织
Pyramid](https://trypyramid.com/community-powered-by-pyramid.html) - 将您的项目添加到列表中

# 贡献

只需分叉并发送带有您出色的 Pyramid 应用程序、项目或的拉取请求
资源。

## 执照

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

在法律允许的范围内，@uralbash 已放弃所有版权和相关内容
或本作品的邻接权。
