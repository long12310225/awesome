# 很棒的 JSON [![Awesome](https://cdn.jsdelivr.net/gh/sindresorhus/awesome@d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
很棒的 JSON 库和资源的精选列表。

受到 [awesome](https://github.com/sindresorhus/awesome) 列表的启发。

[![Links](https://github.com/burningtree/awesome-json/actions/workflows/links.yml/badge.svg)](https://github.com/burningtree/awesome-json/actions/workflows/links.yml)

---

* [很棒的 JSON](#awesome-json)
  * [Applications](#applications)
  * [二进制序列化](#binary-serialization)
  * [浏览器扩展](#browser-extensions)
  * [命令行工具](#command-line-tools)
  * [Databases](#databases)
  * [Datasets](#datasets)
  * [数据建模](#data-modeling)
  * [数据生成](#data-generation)
  * [Differencing](#differencing)
  * [Editors](#editors)
  * [格式扩展](#format-extensions)
  * [前端组件](#frontend-components)
  * [Libraries](#libraries)
  * [Linters](#linters)
  * [在线工具](#online-tools)
  * [架构规范](#schema-specifications)
  * [Services](#services)
  * [Supersets](#supersets)
  * [相关格式](#related-formats)
  * [Resources](#resources)
  * [Templates](#templates)
  * [Testing](#testing)
  * [文本编辑器插件](#text-editor-plugins)
  * [Transformations](#transformations)
  * [Tutorials](#tutorials)
  * [Queries](#queries)
  * [JSON 架构前端组件](#json-schema-frontend-components)
  * [JSON 架构工具](#json-schema-tools)
  * [JSON 架构资源](#json-schema-resources)
  * [JSON 模式验证器](#json-schema-validators)
  * [Contribute](#contribute)

## 应用领域
* [Dadroit JSON Viewer](https://dadroit.com) - 非常快的 JSON 查看器，支持巨大（数 GB）文件、JSON 日志（JSON-Lines 和 ndjson）。

**操作系统X**
* [JSON Design Studio](https://stevespringett.com/free-tools/json-design-studio/) - 专业的架构创作环境。
* [Visual JSON](https://github.com/youknowone/VisualJSON) - 适用于 Mac OS X 的简单 JSON 漂亮查看器。（不活动）
* [JSONExport](https://github.com/Ahmed-Ali/JSONExport) - 将对象转换为当前支持的语言之一的类。

## 二进制序列化
* [BSON](https://bsonspec.org/) - 二进制 JSON。
* [MessagePack](https://msgpack.org/) - 一个极其高效的对象序列化库。
* [UBJSON](https://ubjson.org/) - 二进制 JSON 的通用兼容格式规范。
* [CBOR](https://datatracker.ietf.org/doc/html/rfc7049) - 简洁的二进制对象表示。
* [PSON](https://github.com/dcodeIO/PSON) - 协议JSON，超高效的二进制序列化格式。
* [JSON BinPack](https://www.jsonbinpack.org) - 基于 JSON Schema 的节省空间的二进制 JSON 序列化格式。

## 浏览器扩展
**镀铬**
* [JSON Formatter](https://chromewebstore.google.com/detail/json-formatter/bcjindcccaagfpapjjmafapmmgkkhgoa) ([github](https://github.com/callumlocke/json-formatter)) - 使 JSON 易于阅读。开源。
* [JSON Viewer](https://chromewebstore.google.com/detail/json-viewer/gbmdgpbipfallnflgajpaliibnhdgobh) ([github](https://github.com/tulios/json-viewer)) - 这是一个用于打印 JSON 和 JSONP 的 Chrome 扩展。
* [JSON Finder](https://chromewebstore.google.com/detail/json-finder/flhdcaebggmmpnnaljiajhihdfconkbj) ([github](https://github.com/rapee/jsonfinder)) - 像在 Finder 中一样浏览。
* [JSON Viewer Pro](https://chromewebstore.google.com/detail/json-viewer-pro/eifflpmocdbdmepbjaopkkhbfmdgijcc) ([github](https://github.com/rbrahul/Awesome-JSON-Viewer) - 一个开源 Chrome 扩展，用于通过语法突出显示和折叠或可视化图形浏览 JSON。
* [Discoverable JSON](https://chromewebstore.google.com/detail/json-manipulator-json-to/pcakbljjigdafljigcpbmjllkbhlncjg) ([github](https://github.com/noitcudni/discoverable-json)) - Gron 启发的扩展。将 JSON 文档转换为 JavaScript 表达式。具有过滤、删除、查找和替换功能。

**火狐**
* [JSONView](https://addons.mozilla.org/en-US/firefox/addon/jsonview/) ([github](https://github.com/bhollis/jsonview)) - 在浏览器中查看 JSON 文档。

**狩猎之旅**
* [JSONAce](https://apps.apple.com/us/story/id1377753262?id=com.acrogenesis.jsonace-56Q494QF3LL) ([github](https://github.com/acrogenesis/JSONAce)) - 格式和语法突出显示使用 ACE 编辑器在 Web 浏览器内查看的 JSON。
* [JSONView](https://apps.apple.com/us/story/id1377753262?id=com.acrogenesis.jsonview-56Q494QF3L) ([github](https://github.com/acrogenesis/jsonview-safari)) - JSONView Firefox 扩展的一个端口，用于格式化和语法突出显示在浏览器内部查看的 JSON

## 命令行工具
* [dsq](https://github.com/multiprocessio/dsq) - 用于针对 JSON、CSV、Excel、Parquet 等运行 SQL 查询的工具。
* [fx](https://github.com/antonmedv/fx) - 交互式终端工具。
* [jo](https://github.com/jpmens/jo) - 用于创建 JSON 对象的小实用程序
* [jsoncat](https://github.com/pantuza/jsoncat) - 在终端中使用颜色和调整选项卡大小来漂亮打印 Json。
* [jq](https://github.com/jqlang/jq) - 一个轻量级且灵活的命令行 JSON 处理器。
  * [jaq](https://github.com/01mf02/jaq) - jq 克隆专注于正确性、速度和简单性。用 Rust 编写。
  * [gojq](https://github.com/itchyny/gojq) - jq 的纯 Go 实现。更快一点，更便携。
* [JSONKit](https://github.com/vesper-astrena/jsonkit) - 瑞士军刀：格式化、验证、通过点表示法查询、差异、展平、转换为 CSV 和统计。零依赖，Python 3.10+。
* [livejq](https://github.com/kunalsin9h/livejq) - rust 中的替代“jq”实现，用于连续解析，而不会因无效 JSON 而崩溃
* [json](http://trentm.com/json/) - 用于在 Unix 命令行上处理 JSON 的“json”命令。
* [json-search](https://github.com/cosmo-ray/json-search) - 一个用于搜索 json 文件中的对象/值的小工具。
* [jshon](https://web.archive.org/web/20240206155217/http://kmkeen.com/jshon/) - 为 shell 内的最大便利性而设计的解析器。
* [jarg](http://jdp.github.io/jarg/) - shell 中的简写 JSON 和表单编码语法。
* [jsawk](https://github.com/micha/jsawk) - 与 awk 类似，但针对 JSON。
* [json-dotenv](https://github.com/decryptus/json-dotenv) - 操作并提取 json 格式的 envfiles。
* [gron](https://github.com/tomnomnom/gron) - 将 JSON 文件转换为可 grep 的离散分配。
* [jid](https://github.com/simeji/jid) - 增量挖掘机。通过使用 jq 等过滤查询以交互方式深入了解 JSON。
* [jiq](https://github.com/fiatjaf/jiq) - 这是“jid”和“jq”。您可以使用“jq”过滤查询以交互方式向下钻取。
* [jv](https://github.com/maxzender/jv) - jv（用于 jsonviewer）可帮助您查看 JSON。
* [jl](https://github.com/chrisdone/jl) - JSON 的函数式 sed。
* [oj](https://github.com/ohler55/ojg) - 快速灵活的命令行 JSON 处理器。
* [Parsrs](https://github.com/ShellShoccar-jpn/Parsrs) - 用纯 POSIX shellscript 编写的 CSV、XML 和数据文本解析器和生成器。包括`parsrj.sh`和`makrj.sh`。
* [visidata](https://github.com/saulpw/visidata) - 类似终端电子表格的工具，用于交互式探索数据。
* [jc](https://github.com/kellyjonbrazil/jc) - 将许多 CLI 工具、文件类型和常见字符串的输出转换为 JSON
* [logdy](https://github.com/logdyhq/logdy-core) - jq、tail、less、grep 和 awk 合并在一起，并在干净的 Web UI 中提供。
* [jsonskim](https://github.com/rxzzh/jsonskim) - 通过折叠数组和截断字符串来提取结构。 LLM 就绪输出。

## 数据库
* [MongoDB](https://www.mongodb.com/) - 开源文档数据库和领先的 NoSQL 数据库。
* [RethinkDB](https://rethinkdb.com/) - 一个开源分布式文档数据库，具有令人愉快且功能强大的查询语言。
* [EJDB](https://github.com/Softmotions/ejdb) - 嵌入式 JSON 数据库引擎在 MIT 许可下发布。 (三)
* [lowdb](https://github.com/typicode/lowdb) - 基于 lodash API 构建的平面文件数据库。 （Javascript）
* [Lawnchair](https://github.com/brianleroux/lawnchair) - 轻量级客户端文档存储。 （Javascript）
* [JSON ODM](https://github.com/konsultaner/jsonOdm) - 用于在服务器或浏览器中使用的 JavaScript 的对象文档映射器。 （Javascript）
* [JSON Server](https://github.com/typicode/json-server) - 在 30 秒内获得零编码的完整假 REST API。
* [Kinto](https://github.com/Kinto/kinto) - 具有同步和共享功能的轻量级 JSON 存储服务。
* [CouchDB](https://couchdb.apache.org/) - 无缝多主同步，可从大数据扩展到移动设备，具有直观的 HTTP/JSON API，专为可靠性而设计。
* [RxDB](https://github.com/pubkey/rxdb) - 事件驱动的 JSON 数据库，带有 JSON 模式、mango 查询和 CouchDB 同步。 （Javascript）
* [JSONlite](https://github.com/nodesocket/jsonlite) - 一个简单、独立、无服务器、零配置的 json 文档存储。 （重击）

## 数据集
* [country.io](http://country.io/data/) - 各种国家/地区相关数据集，如 JSON，包括货币、国家/地区代码、名称等
* [countries](https://github.com/mledoze/countries) - 世界国家。
* [MTG JSON](https://mtgjson.com/) - 最新的万智牌卡牌数据。
* [Heartstone JSON](https://hearthstonejson.com/) - 最新的《炉石传说》卡牌数据。
* [getCountries()](https://peric.github.io/GetCountries/) - 自定义国家数据的生成器。

## 数据建模
* [JSONModel](https://github.com/jsonmodel/jsonmodel) - 神奇的数据建模框架。 （目标-C）

## 数据生成
* [jsonymize](https://github.com/cameronhunter/jsonymize) - 从标准输入读取数据，匿名化，然后写入标准输出。
* [dyson](https://github.com/webpro/dyson) - 动态、假 JSON 的服务器。 （节点.js）

## 差异化
* [JSONPatch](https://jsonpatch.com/) - 描述文档更改的格式。
* [JSON-Patch](https://github.com/Starcounter-Jack/JSON-Patch) - JSON-Patch 标准 (RFC 6902) 的精简 JavaScript 实现。 （Javascript）
* [jiff](https://github.com/cujojs/jiff) - 基于 rfc6902 的 JSON 补丁和 diff。 （Javascript）
* [json-patch-php](https://github.com/mikemccabe/json-patch-php) - JSON 补丁的实现 (IETF RFC 6902) (PHP)
* [dffptch](https://github.com/paldepind/dffptch) - 一个使用紧凑 diff 格式进行比较和修补的微型库。 （Javascript）
* [jsondiffpatch](https://github.com/benjamine/jsondiffpatch) - JavaScript 对象的差异和补丁。 （Javascript）

## 编辑
* [FrontAid CMS](https://frontaid.io/) - 支持任意数据模型结构的内容管理系统。
* [JSON table editor](https://jsontable.app/) - 将 JSON 数组显示为表格，提供搜索、过滤和编辑功能。它支持多个 GB 的大文件。 （锈）。
* [JSONEdit](http://mb21.github.io/JSONedit/) - 作为 AngularJS 指令构建的用户友好的可视化编辑器。
* [JSON Crack](https://jsoncrack.com/) - 将您的 JSON 显示为图表

## 格式扩展
* [GeoJSON](https://geojson.org/) - 一种地理空间数据交换格式。
* [JSON-LD](https://json-ld.org/) - 一种轻量级链接数据格式。
* [JSON-RPC](https://www.jsonrpc.org/) - 一种无状态、轻量级远程过程调用 (RPC) 协议。
* [JSONP](https://en.wikipedia.org/wiki/JSONP) - 使用 JSON-P/JSONP 更安全的跨域 Ajax。
* [JsonML](http://www.jsonml.org/) - 一种紧凑格式，用于将基于 XML 的标记传输为 JSON，使其能够无损地转换回其原始形式。
* [JSON5](https://json5.org/) - 旨在使人类更容易手动编写和维护的扩展。
* [JSON6](https://github.com/d3x0r/json6) - 人类 JSON (ES6)。
* [JSON 1.1/JSONX](https://json-next.github.io/) - 进化版本 1.1，具有人类格式扩展，包括。注释、不带引号的多行字符串、可选的逗号和尾随逗号等等。
* [JSON Resume](https://jsonresume.org/) - 创建简历标准的开源倡议。
* [JSON Web Tokens](https://jwt.io/) - 一种紧凑的 URL 安全方式，用于表示在两方之间传输的声明。
* [JSON API](https://jsonapi.org/) - 构建 API 的标准。
* [JSON Activity Streams](https://activitystrea.ms/) - 一种在网络上联合社交活动的格式。
* [JSON-stat](https://github.com/jsonstat/jsonstat) - 用于数据传播的简单轻量级格式。
* [/contribute.json](https://www.contributejson.org/) - 使跨项目的开源贡献信息更容易访问。
* [NDJSON](https://github.com/ndjson/ndjson-spec) (Newline delimited JSON) - 在流协议中分隔 JSON 的标准。
* [survey.js](https://surveyjs.io/form-library) - 基于 JSON 的调查库。
* [JSON Meta Application Protocol (JMAP)](https://jmap.io/) - 一种用于高效同步基于 JSON 的数据对象的协议，支持推送和带外二进制数据上传/下载。
* [J<sub>ack</sub>SON: JSON secret keeper](https://github.com/rosehgal/jackson) - 在配置文件中存储秘密的 JSONic 方式。
* [Sequence JSON](https://github.com/soundio/music-json/) - 关于以 JSON 创建音乐序列数据的标准方法的提案。

## 前端组件
* [JSON editor jQuery plugin](https://github.com/DavidDurman/FlexiJsonEditor) - 您的网络应用程序/页面的组件。 （jQuery）
* [jqTree](http://mbraak.github.io/jqTree/) - 用于在 html 中显示树结构的小部件。 （jQuery）
* [jsTree](https://www.jstree.com/docs/json/) - jquery 插件，提供交互式树。 （jQuery）
* [Dynatable.js](https://github.com/alfajango/jquery-dynatable) - 一个有趣的、语义的、HTML5+JSON、交互式表格插件。 （jQuery）
* [JSON Formatter](https://github.com/mohsen1/json-formatter) - HTML 中可折叠 JSON 的 Angular 指令。 （AngularJS）
* [react-jsonschema-form](https://rjsf-team.github.io/react-jsonschema-form/) - 用于从 JSON Schema 构建 Web 表单的 React 组件。 （反应）
* [@textea/json-viewer](https://github.com/TexteaInc/json-viewer) - JSON 查看器的 React 组件。 （反应）
* [ngx-formly](https://github.com/ngx-formly/ngx-formly) - JSON 驱动/Angular 的动态表单

* [SmarkForm](https://smarkform.bitifet.net) - 增强 HTML 表单以导入/导出任何可能的数据，包括任意深度的数组和子表单。
## 图书馆
**C**
* [codables](https://codableslib.com/) - 声明性、类型丰富的（反）序列化器能够处理几乎任何数据类型。
* [Jansson](https://github.com/akheron/jansson) - 用于编码、解码和操作数据的 C 库。
* [jsmn](https://zserge.com/jsmn.html) - C 语言的简约解析器。它可以轻松集成到资源有限的项目或嵌入式系统中。
* [json-build](https://github.com/lcsmuller/json-build) - C 语言的简约串行器。它可以轻松集成到资源有限的项目或嵌入式系统中。
* [ojc](https://github.com/ohler55/ojc) - 一个快速的 JSON 解析器。

**C++**
* [ArduinoJson](https://github.com/bblanchon/ArduinoJson) - 一个高效的嵌入式系统库。
* [JSON++](https://github.com/tunnuz/json) - 用于 C++11 的独立 Flex/Bison 解析器。
* [json11](https://github.com/dropbox/json11) - C++11 的小型库。
* [Nlohmann JSON](https://github.com/nlohmann/json) - C++11 仅标头类。
* [qjson](https://github.com/qinyonghang/json) - 一个仅包含头文件的 C++17 快速库。
* [RapidJSON](https://github.com/Tencent/rapidjson) - 用于 C++ 的快速 JSON 解析器/生成器，具有 SAX/DOM 风格 API
* [simdjson](https://github.com/simdjson/simdjson) - 每秒解析千兆字节的 JSON。

**Clojure**
* [data.json](https://github.com/clojure/data.json) - Clojure 数据结构之间的解析器/生成器。

**Fortran**
* [JSON-Fortran](https://github.com/jacobwilliams/json-fortran) - 用于写入、读取和操作 JSON 文件和数据结构的 Fortran 库。

**去**
* [ojg](https://github.com/ohler55/ojg) - 高性能JSON处理和生成工具的集合。

**哈斯克尔**
* [aeson-qq](https://github.com/sol/aeson-qq) - Haskell 的 JSON 准引用器。
* [json-schema](http://hackage.haskell.org/package/json-schema) - Haskell 的 JSON 模式库
* [hjsonschema](http://hackage.haskell.org/package/hjsonschema) - Haskell 的 JSON Schema Draft 4 库

**Java**
* [JSON-java](https://github.com/stleary/JSON-java) - 参考实现。
* [快速 JSON 处理器](https://github.com/alibaba/fastjson)
* [Gson](https://github.com/google/gson) - 一个 Java 库，用于将 JSON 转换为 Java 对象，反之亦然。
* [Jackson](https://github.com/FasterXML/jackson) - 用于处理 JSON 数据格式的多用途 Java 库。
* [moshi](https://github.com/square/moshi) - 适用于 Android 和 Java 的现代 JSON 库。
* [essential-json](https://github.com/arkanovicz/essential-json) - 一个轻量级的 Java 库，用于序列化、解析和操作，具有干净而精确的 API。
* [dsl-json](https://github.com/ngs-doo/dsl-json) - 一个非常快速的流式 JSON 库。对字节数组进行操作。
* [mjson](https://github.com/bolerio/mjson) - 适用于 Java 的精益 JSON 库，具有紧凑、优雅的 API。

**Javascript**
* [JSON-js](https://github.com/douglascrockford/JSON-js) - JavaScript 中的 JSON。
* [JSON 3](https://bestiejs.github.io/json3/) - 现代实施。
* [oboe.js](https://github.com/jimhigson/oboe.js) - 流式方法通过在响应完成之前提供已解析的对象来加速 Web 应用程序。
* [FracturedJsonJs](https://www.npmjs.com/package/fracturedjsonjs) - 一个 JSON 格式化程序，可生成人类可读但相当紧凑的输出。
* [JsonHilo](https://github.com/xtao-org/jsonhilo) - 最小无损解析事件流，类似于 SAX。

**Objective-C**
* [JSONKit](https://github.com/johnezang/JSONKit) - Objective-C 库。
* [SBJson](https://github.com/SBJson/SBJson) - 解析一个或多个数据块。

**Perl**
* [JSON::Tiny](https://github.com/daoswald/JSON-Tiny) - 用于以简约方式编码和解码 JSON 的 Perl 模块。

**PL/SQL**
* [PL/JSON](https://github.com/pljson/pljson) - 用 PL/SQL 编写的通用 JSON 对象。

**PHP**
* [TOON PHP Lite](https://github.com/manojrammurthy/toon-php-lite) - 轻量级 TOON 编码器/解码器，用于人类可读、LLM 友好的结构化数据。 （PHP）。
* [Webmozart JSON](https://github.com/webmozart/json) - 强大的解码器/编码器，支持模式验证。

**Python**
* [simplejson](https://github.com/simplejson/simplejson) - 简单、快速、可扩展的编码器/解码器
* [jsonpickle](http://jsonpickle.github.io/) - 用于序列化任意对象图的库。
* [metamagic.json](https://pypi.org/project/metamagic.json/) - JSON 编码器的超快速 Python 3 实现。

**红宝石**
* [oj](https://github.com/ohler55/oj) - 作为 Ruby gem 的快速 JSON 解析器和对象编组器。
* [MultiJSON](https://github.com/intridea/multi_json) - 用于 JSON 处理的通用可交换后端。

**反应**
* [json2react](https://github.com/txgruppi/json2react) - 使用 JSON 创建 React 无状态组件。

**.NET**
* [jsonfx](https://github.com/jsonfx/jsonfx) - .NET 的序列化框架。
* [jsonapi-consumer](https://github.com/OKTAYKIR/jsonapi-consumer) - 用于使用 [JSON API 标准](https://jsonapi.org) 上基于 JSONAPI 的 API 的客户端框架。

**斯卡拉**
* [spray-json](https://github.com/spray/spray-json) - Scala 中的轻量级、干净且简单的实现。
* [circe](https://github.com/circe/circe) - Scala 的另一个 JSON 库。
* [scala-jsonapi](https://github.com/scala-jsonapi/scala-jsonapi) - 用于将 JSON:API 规范与 Play、Spray 和/或 Circe 后端集成的支持库。
* [jsoniter-scala](https://github.com/plokhotnyuk/jsoniter-scala) - 用于编译时生成超快 JSON 编解码器的 Scala 宏。

**外壳**
* [jshn](https://openwrt.org/docs/guide-developer/jshn) - shell 脚本中的 JSON 解析和生成库 (Ash/Bash)

**斯威夫特**
* [SwiftyJSON](https://github.com/SwiftyJSON/SwiftyJSON) - 在 Swift 中处理数据的更好方法。

* [yyjson](https://github.com/ibireme/yyjson) - C 中的高性能解析器和序列化器。
## 短绒棉
* [jsonlint](https://github.com/zaach/jsonlint) - 使用 CLI 的解析器和验证器。 （Javascript）
* [JSON Lint](https://github.com/Seldaek/jsonlint) - PHP 短绒检查。 （PHP）

## 在线工具
* [Dadroit V Web](https://dadroit.com/vweb/) - 用于大文件的浏览器内查看器，具有树视图、正则表达式搜索和使用身份验证的 URL 加载。完全客户端。
* [DataFormatter Pro](https://dataformatterpro.com/) - 基于浏览器的格式化程序、验证程序、差异和具有树视图的转换器。
* [JSON Blob](https://jsonblob.com/) - 用于查看、编辑、格式化和共享数据的在线工具。还有一个用于针对存储的 blob 发出请求的 API。
* [JSON Viewer Tool](https://jsonviewertool.com/) - 用于在浏览器中查看、格式化、验证、缩小和转换数据的在线工具。
* [JSONLint](https://jsonlint.com/) - JSON 验证器。
* [JSONCompare](https://jsoncompare.com/) - JSON Linter 的高级版本。
* [JSONMaster](https://jsonmaster.com/) - 免费的在线验证器、格式化器、压缩器和查看器。
* [JSONMate](https://www.jsonmate.com/) - JSON 编辑器、检查器和美化器。
* [JSON Editor online](https://jsoneditoronline.org/) - 一个基于网络的查看、编辑和格式化工具。
* [Collapsible JSON Formatter](http://www.bodurov.com/JsonFormatter/) - 原始代码的格式化程序和着色器。
* [JSON Formatter and Validator](https://jsonformatter.curiousconcept.com/) - 格式化程序可帮助调试。
* [JSON Generator](https://json-generator.com/) - 用于生成随机数据的工具。
* [FakeJSON](https://fakejson.com/) - Web API 可为您的应用程序快速生成虚假数据。
* [JSON to CSV](https://konklone.io/json/) - 浏览器内免费的 JSON 到 CSV 转换器。
* [CSV to JSON](https://alef.website/tools/csv-to-json) - 简单、隐私友好且离线优先的在线 csv 到 json 转换器
* [json2csharp](https://json2csharp.com/) - 从 json 字符串或 url 生成 C# 类。
* [JSON Utils](http://jsonutils.com/) - 用于从 JSON 生成 C#、VB.Net 和 Javascript 类的站点。
* [geojson.io](https://geojson.io/) - 只需编辑 GeoJSON 地图数据即可。
* [jq play](https://jqplay.org/) - jq的游乐场。
* [json2yaml](https://www.json2yaml.com/) - 在线将 JSON 转换为 YAML。
* [JSON Selector Generator](http://jsonselector.com/) - 一个简单的 GUI，用于生成要访问的选择器。
* [JSON.fr](https://www.json.fr/) - 完全客户端验证器和格式化程序。
* [JSONtapose](https://www.jsontapose.com/) - 直观、美观、安全的客户端比较和可视化工具。
* [jsontosdk](https://jsontosdk.vercel.app) - 粘贴数据示例以获取类型化的 TypeScript 接口和具有 LLM 命名类型的 Zod 架构。没有注册。
* [ObjGen](https://www.objgen.com/json) - 在线实时 JSON 生成器。
* [JSONPlaceholder](https://jsonplaceholder.typicode.com/) - 用于测试和原型设计的假在线 REST API。
* [Extends Class](https://extendsclass.com/json-diff.html) - 用于比较两个文件的 Diff 工具。
* [JSON Schema Validate API](https://assertible.com/json-schema-validation) - 一个简单且免费的 JSON 模式验证 API。
* [JSONPerf](https://jsonperf.com) - 直观、公正且最新的 JSON 性能基准。
* [FracturedJson](https://j-brooke.github.io/FracturedJson/) - 生成人类可读但相当紧凑的输出的格式化程序。
* [Softwium](https://softwium.com/fake-api/) - 用于测试的假冒 REST API。
* [JSONing](https://jsoning.com/) - 一个工具集，包括格式化程序、比较器、JSONPath 测试器、补丁生成器和数据生成器。

## 架构规范
* [JSON Model](https://github.com/clairey-zx81/json-model) - 用于数据建模的轻量级、功能齐全的 DSL。
* [JSON Schema](https://json-schema.org/) - 用于定义 JSON 数据结构的基于 JSON 的格式。
* [Itemscript](https://code.google.com/archive/p/itemscript/) - 用于验证和指定值的语言。
* [Kwalify](https://github.com/kvs/kwalify) - 解析器、模式验证器和数据绑定工具
* [Rx](https://rx.codesimply.com/) - 简单、可扩展的架构。

## 服务
* [Exchange Rate API](https://www.exchangerate-api.com) - 一个简单且免费的货币汇率数据 API。
* [ipinfo.io](https://ipinfo.io) - JSON IP 和 GeoIP REST API。
* [JSONProxy](https://github.com/afeld/jsonp) - 简单的 HTTP 代理，支持对任何 JSON API 的跨域请求。
* [Telize](https://www.telize.com/) - JSON IP 和 GeoIP REST API。
* [jsonpad](https://jsonpad.io/) - 一个简单的 JSON 存储平台。

## 超级组
* [YAML](https://yaml.org) - 适用于所有编程语言的人类友好的数据序列化标准。
* [HanSON](https://github.com/timjansen/hanson) - JSON for Humans - 带有不带引号的标识符、多行字符串和注释。
* [μson](https://github.com/burningtree/uson) (uson) - JSON 的简写。
* [HOCON](https://github.com/lightbend/config/blob/master/HOCON.md) - 人类优化的配置对象表示法。
* [ASON](https://github.com/sadmac7000/libason) - JSON 语义上完整的超集（草案）。
* [TOML](https://github.com/toml-lang/toml) - 一种最小的配置文件格式，由于语义明显而易于阅读。
* [HCL](https://github.com/hashicorp/hcl) - 一种对人类和机器都友好的结构化配置语言。

## 教程
* [介绍 JSON](http://json.org/)
* [JSON Tutorial](https://www.w3resource.com/JSON/introduction.php) - JavaScript 对象表示法 (JSON) 的介绍性教程。
* [JSON - Rosetta Code](https://rosettacode.org/wiki/JSON) - 不同语言的基本操作（目前有 57 种语言）。
* [What is JSON and how to use it](https://ilovecoding.org/lessons/json-what-is-json-and-how-to-use-it) - 适合初学者的视频教程。
* [jq Primer: Munging JSON Data](https://andrew.gibiansky.com/) - 如何使用 jq 与传统 Unix 工具一样有效地处理 JSON 文件。

## 相关格式
* [AXON](https://github.com/intellimath/pyaxon) - 一种简单的基于文本的格式，用于交换对象、文档和数据。它尝试结合 JSON、XML 和 YAML 的优点。
* [CSON](https://github.com/bevry/cson) - CoffeeScript-对象表示法。 CoffeeScript 对象的 JSON。
* [MSON](https://github.com/apiaryio/mson) - Markdown 语法与描述 JSON 和 JSON Schema 兼容。
* [ArchieML](http://archieml.org/) - 针对人类可写性进行优化的结构化文本格式。

## 资源
* [Type-o-rama](https://github.com/stereobooster/type-o-rama) - JS 类型系统的可移植性、不同 JS 类型系统的比较以及它们之间的转换。
* [Awesome jq](https://github.com/fiatjaf/awesome-jq) - 很棒的 jq 工具和资源的精选列表。

## 模板
* [Jsonnet](https://jsonnet.org/) - 一种特定于域的配置语言，可帮助您定义 JSON 数据。
* [rabl](https://github.com/nesquena/rabl) - 通用 ruby​​ 模板，支持 json、bson、xml、plist 和 msgpack。 （红宝石）
* [json2html](http://json2html.com/) - 带有 jQuery 和 Node.js 包装器的 HTML 模板库。 （Javascript）

## 测试
* [JSON Test](http://www.jsontest.com/) - 使用 JavaScript 对象表示法 (JSON) 的服务测试平台。
* [JSONassert](https://github.com/skyscreamer/JSONassert) - 用更少的代码编写 JSON 单元测试。非常适合测试 REST 接口。 （爪哇）
* [JsonUnit](https://github.com/lukas-krecan/JsonUnit) - 一个简化单元测试中 JSON 比较的库。它受到 XmlUnit 的强烈启发。
* [JSON Parsing Test Suite](https://github.com/nst/JSONTestSuite) - 一个非常完整的测试套件和验证框架。

## 文本编辑器插件
**Emacs**
* [JSON Reformat](https://github.com/gongo/json-reformat) - 重新格式化工具。

**维姆**
* [vim-json](https://github.com/elzr/vim-json) - Vim 更好的 JSON：关键字与值的明显突出显示、特定于 JSON（非 JS）的警告、引号隐藏。对病原体友好。

**Visual Studio 代码**

**新维姆**
* [nvim-jqx](https://github.com/gennaro-tedesco/nvim-jqx) - 从quickfix窗口浏览和查询neovim中的json文件。 （路亚）

## 转换
* [json-sharp](https://github.com/globocom/json-sharp) - 用于处理纯 JSON 对象操作的 Javascript 工具。 （Javascript）
* [json2json](https://github.com/joelvh/json2json) - 将结构从一种结构转换（重新格式化）到另一种结构。 （Javascript）
* [trans](https://github.com/gabesoft/trans) - 最终的对象转换器。 （Javascript）
* [osmtogeojson](https://github.com/tyrasd/osmtogeojson) - 将 OSM 数据转换为 GeoJSON。 （Javascript）
* [fast-xml-parser](https://github.com/NaturalIntelligence/fast-xml-parser) - 快速 XML 到 JSON 的转换，反之亦然 javascript/JSON 转换。
* [x2js](https://github.com/abdolence/x2js) - XML 到 JSON 以及相反的 JavaScript 转换函数。 （Javascript）
* [JSONC](https://github.com/tcorral/JSONC) - JSON 压缩器和解压缩器。 （Javascript）
* [JsonMapper](https://github.com/cweiske/jsonmapper) - 将嵌套结构映射到 PHP 类 (PHP)
* [SassyJSON](https://github.com/KittyGiraudel/SassyJSON) - Sass 支持的 API。 （萨斯）
* [json.human.js](http://marianoguerra.github.io/json.human.js/) - 一个小型库，用于将 JSON 对象转换为人类可读的 HTML 表示形式，易于针对不同目的进行样式设计。
* [fanci](https://github.com/liip/fanci) - 基于模板提取、重命名和转换 JSON。 （节点.js）
* [deepjson](https://www.npmjs.com/package/deepjson/) - 加载大 json 配置文件的更好方法。 （节点.js）
* [jsontl](https://github.com/DoublePrecisionSoftware/jsontl) - 允许使用基于 JSON 的转换语言进行转换。 （节点.js）
* [json-transforms](https://github.com/ColinEberhardt/json-transforms) - 一种用于转换 JSON 结构的递归模式匹配方法。
* [normalizr](https://github.com/paularmstrong/normalizr) - 根据架构标准化嵌套 JSON。 （Javascript）
* [JSON-populate](https://github.com/eiriklv/json-populate) - 用于使用无限递归循环引用填充 JSON 数据的工具。有点像 Falcor，但适用于纯 JSON。
* [CircularJSON](https://github.com/WebReflection/circular-json) - JSON 不处理循环引用。现在确实如此。
* [Sawmill](https://github.com/logzio/sawmill) - JSON 转换库 (Java)
* [nimnjs](https://github.com/NaturalIntelligence/nimnjs) - JSON 到 nimn 双向转换器。
* [stylops](https://github.com/cruel-intentions/stylops) - CSS 子集到 JSON 的转换。 （节点.js）

## 查询
* [dasel](https://github.com/tomwright/dasel) - 使用命令行中的选择器查询和更新数据结构。与 [jq](https://github.com/jqlang/jq) / [yq](https://github.com/kislyuk/yq) 相当，但支持 JSON、YAML、TOML 和 XML，且运行时依赖性为零。
* [JMESPath](https://jmespath.org/) - JSON 的查询语言。
* [JSON Mask](https://github.com/nemtsov/json-mask) - 用于选择 JS 对象的特定部分并隐藏其余部分的微型语言和引擎。 （Javascript）
* [JSONiq](https://www.jsoniq.org/) - JSON 查询语言。
* [ObjectPath](https://objectpath.org/) - 用于半结构化数据的敏捷查询语言。 （蟒蛇）
* [DefiantJS](https://www.defiantjs.com/) - 使用 XPath 表达式进行闪电般的快速搜索，并使用 XSL 进行转换。 （Javascript）
* [JSONSelect](https://github.com/lloyd/JSONSelect) - 类似 CSS 的选择器。 （Javascript）
* [JSONPath](https://goessner.net/articles/JsonPath/) - XPath 实现。 （Javascript/PHP）
* [searchjs](https://github.com/deitch/searchjs) - 一个基于 json 类 SQL 语言的过滤库。
* [json-rel](https://github.com/slurmulon/json-where) - JSON 中的透明引用。
* [JSONata](https://jsonata.org/) - Node-RED 中使用的查询和转换语言支持函数表达式。

## JSON 架构前端组件
* [JSON Editor](https://github.com/jdorn/json-editor) - 基于 JSON 模式的编辑器。 （jQuery）
* [angular-schema-form](https://github.com/json-schema-form/angular-schema-form) - 生成表格。 （AngularJS）
* [JSON Schema View](https://github.com/mohsen1/json-schema-view) - 用于在 HTML 中渲染 JSON 模式的 AngularJS 指令 (AngularJS)
* [Angular JSON Schema Form](https://github.com/mohsen1/angular-json-schema-form) - 用于根据 JSON 模式制作表单的 Angular 指令。 （AngularJS）
* [AlpacaJS](http://www.alpacajs.org) - 在 Bootstrap、jQuery Mobile、jQuery UI 和 HTML (jQuery) 之上生成 JSON 模式驱动的表单

## JSON 架构工具
* [JSON Schema CLI](https://github.com/intelligence-ai/jsonschema) - 用于格式化、linting、测试、捆绑和验证本地开发和 CI/CD 管道的架构文件的命令行界面。
* [prmd](https://github.com/interagent/prmd) - HTTP API 的工具和文档生成。
* [generate-schema](https://github.com/Nijikokun/generate-schema) - 轻松将 JSON 对象转换为 JSON 架构、Mongoose 架构或通用模板，以实现快速文档/新贵。
* [Docson](https://github.com/lbovet/docson) - 您的类型的文档。
* [Orderly JSON](https://github.com/lloyd/orderly) - 用于描述编译成 JSONSchema 的 JSON 的文本格式。
* [jsonschema2pojo](https://github.com/joelittlejohn/jsonschema2pojo) - 生成 Java 类型并注释这些类型，以便与 Jackson 1.x 或 2.x、Gson 等进行数据绑定。
* [Matic](https://github.com/mattyod/matic) - 用于生成 HTML 文档的构建工具。
* [JSON Schema + Faker](https://github.com/json-schema-faker/json-schema-faker) - 伪造你的模式。
* [DLL.js](https://github.com/moll/js-ddl) - 从 PostgreSQL 或 SQLite3 获取 JSON 模式。
* [js-schema](https://github.com/molnarg/js-schema) - 一种在 JavaScript 中描述对象模式的新方法。它具有干净简单的语法，并且能够序列化到流行的 JSON Schema 格式或从流行的 JSON Schema 格式进行序列化。
* [JSON Schema $Ref Parser](https://github.com/APIDevTools/json-schema-ref-parser) - 解析、解析和取消引用 JSON 模式 $ref 指针

## JSON 架构资源
* [Learn JSON Schema](https://www.learnjsonschema.com) - 架构规范的开源参考文档。
* [Understanding JSON Schema](https://spacetelescope.github.io/understanding-json-schema/) - 旨在为 JSON 模式提供更易于访问的文档的网站。
* [Using JSON Schema](http://usingjsonschema.com/) - 书籍和 GitHub 项目，展示了如何将 JSON Schema 用于各种任务和不同的编程上下文中。
* [Awesome JSON Schema](https://github.com/sourcemeta/awesome-jsonschema) - 精彩的 JSON 架构资源、教程、工具等的精选列表。

## JSON 模式验证器
**Javascript 和 Node.js**
* [json-schema-benchmark](https://github.com/ebdrup/json-schema-benchmark) - Node.js 验证器的性能基准。
* [is-my-json-valid](https://github.com/mafintosh/is-my-json-valid) - 使用代码生成速度极快的验证器。
* [jsen](https://github.com/bugventure/jsen) - 为速度而构建的验证器。
* [themis](https://github.com/playlyfe/themis) - 一个速度极快的验证器。
* [jsck](https://github.com/pandastrike/jsck) - JSON Schema 编译检查。
* [z-schema](https://github.com/zaggino/z-schema) - 用 JavaScript 编写的 NodeJS 和浏览器验证器。
* [jjv](https://github.com/acornejo/jjv) - 用于模式验证的 Javascript 库。
* [request-validator](https://github.com/bugventure/request-validator) - 用于 Express 和 Connect 的灵活请求验证器中间件。
* [tv4](https://github.com/geraintluff/tv4) - 小型验证器。
* [ajv](https://github.com/ajv-validator/ajv) - 最快的模式验证器。支持草案 04/06/07/2019-09/2020-12。

**Java 和 Kotlin**
* [Medeia Validator](https://github.com/worldturner/medeia-validator) - 用 Kotlin 编写的兼容（草案 - 04/06/07）和快速流验证器

**PHP**
* [JSON Schema for PHP](https://github.com/justinrainbow/json-schema) - JSON 模式的 PHP 实现。
* [JSON Guard](https://json-guard.thephpleague.com) - JSON Schema Draft 4 的验证器。

**Python**
* [jsonschema](https://github.com/python-jsonschema/jsonschema) - jsonschema 的 Python 实现。
* [JSON Schema Toolkit](https://github.com/petrounias/json-schema-toolkit) - 通过验证、Django JSON 字段和本机 PostgreSQL JSON 类型约束以编程方式构建 JSON 模式（递归字段映射）。

**红宝石**
* [Ruby JSON Schema Validator](https://github.com/voxpupuli/json-schema) - 针对符合 JSON Schema Draft 4 的 JSON 模式进行验证。

## 贡献
欢迎投稿！首先阅读[贡献指南](CONTRIBUTING.md)。

## 执照
[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)
