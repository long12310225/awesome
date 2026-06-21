<!--lint disable double-link-->
# 出色的 ArcGIS 开发人员 [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

<!--lint disable match-punctuation-->
<img src="esri-logo.png" align="right" width="100">

> 一组很棒的资源可帮助您[使用 ArcGIS 产品进行开发](https://www.esri.com/en-us/arcgis/products/develop-with-arcgis/overview)。

ArcGIS 产品使您可以访问 API、位置服务和工具来开发自己的地图和空间分析应用程序。使用地图产品帮助开发人员为您自己、您的组织或其他组织构建 Web、本机、离线、桌面或集成解决方案。访问全套位置服务以提供底图图层、地理编码和路由功能以及其他地理空间功能。在 ArcGIS 云中安全地托管和管理您的数据。

---

## 内容

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [API 和 SDK](#apis-and-sdks)
- [应用程序生成器和 CLI](#application-generators-and-clis)
- [ArcGIS 位置服务](#arcgis-location-services)
- [代码示例和片段](#code-samples-and-snippets)
- [数据转换工具](#data-conversion-tools)
- [数据集成工具](#data-integration-tools)
- [调试工具](#debugging-tools)
- [设计和造型](#design-and-styling)
- [开发者指南](#developer-guides)
- [Helpers](#helpers)
- [地图和数据探索](#map-and-data-exploration)
- [Playgrounds](#playgrounds)
- [空间分析](#spatial-analysis)
- [Specifications](#specifications)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

---

## API 和 SDK

- ArcGIS 核心 API 和库：
	- [ArcGIS API for Python](https://developers.arcgis.com/python/) - 使用 Python 进行绘图、空间分析、数据科学、地理空间 AI 和自动化的指南、示例笔记本和 API 参考。
	- [ArcGIS REST APIs](https://developers.arcgis.com/rest/) - 有关 ArcGIS REST API 的一般文档：位置服务、内容管理、门户管理等。
	- [ArcGIS REST APIs collections](https://github.com/esri-es/ArcGIS-REST-API) - Postman 集合可与某些 REST API 配合使用：位置服务、托管要素图层、ArcGIS Online、ArcGIS Hub 等。
	- [ArcGIS REST JS](https://developers.arcgis.com/arcgis-rest-js/) - 用于访问位置服务、ArcGIS Online 和 ArcGIS Enterprise REST API 的 JavaScript 模块集合的关键概念、教程和 API 参考。
	- [ArcGIS Urban API](https://developers.arcgis.com/arcgis-urban-api/) - 可用于直接与 ArcGIS Urban 数据交互的公共 GraphQL Web 服务。
	- [ArcPy](https://pro.arcgis.com/en/pro-app/arcpy/main/arcgis-pro-arcpy-reference.htm) - 有关用于在 ArcGIS Desktop 或 ArcGIS Enterprise 环境中执行地理数据分析、数据转换、数据管理和地图自动化的 Python 包的文档。

- Esri 客户端 SDK：
	- [ArcGIS Maps SDK for .NET](https://developers.arcgis.com/net/) - 使用 .NET 构建桌面和移动应用程序的指南、示例代码和 API 参考。
	- [ArcGIS Maps SDK for Flutter](https://developers.arcgis.com/flutter/) - 使用 Flutter 构建桌面和移动应用程序的指南、示例代码和 API 参考。
	- [ArcGIS Maps SDK for JavaScript](https://developers.arcgis.com/javascript/latest/) - 用于构建解锁地理空间数据的 2D 和 3D 交互式 Web 应用程序的指南、示例代码、API 参考和展示。
	- [ArcGIS Maps SDK for Kotlin](https://developers.arcgis.com/kotlin/) - 使用 Kotlin 构建移动应用程序的指南、示例代码和 API 参考。
	- [ArcGIS Maps SDK for Qt](https://developers.arcgis.com/qt/) - 用于构建移动和桌面应用程序的指南、示例代码和 API 参考。
	- [ArcGIS Maps SDK for Swift](https://developers.arcgis.com/swift/) - 使用 Swift 构建移动应用程序的指南、示例代码和 API 参考。
	- [ArcGIS Maps SDK for Unity](https://developers.arcgis.com/unity/) - 使用 ArcGIS 数据和服务进行 Unity 开发的指南、API 参考和示例代码。
	- [ArcGIS Maps SDK for Unreal Engine](https://developers.arcgis.com/unreal-engine/) - 使用 ArcGIS 数据和服务为 Unreal Engine 进行开发的指南、API 参考和示例代码。

- 集成和插件（第三方库）：
	- [ArcGIS integrations with CesiumJS](https://developers.arcgis.com/cesiumjs/) - 帮助您开始使用 CesiumJS 和 ArcGIS 构建地图应用程序的指南和教程。
	- [ArcGIS integrations with MapLibre GL JS](https://developers.arcgis.com/maplibre-gl-js/maplibre-arcgis-plugin/) - 了解如何使用 Esri 维护的 ArcGIS MapLibre 插件和 ArcGIS REST JS 将 MapLibre GL JS 应用程序与 ArcGIS 服务连接，包括教程、API 参考和示例代码。
	- [ArcGIS integrations with OpenLayers](https://developers.arcgis.com/openlayers/) - 帮助您开始使用 OpenLayers 和 ArcGIS 位置服务构建 Web 应用程序的指南和教程。
	- [ArcGIS integrations with Leaflet](https://developers.arcgis.com/esri-leaflet/) - 了解如何使用 Esri 维护的 Esri Leaflet 插件和 ArcGIS REST JS 将 Leaflet 应用程序与 ArcGIS 服务连接起来，包括教程、API 参考和示例代码。
	- [Esri-gl](https://github.com/muimsd/esri-gl) - 社区维护的插件，允许在 Mapbox GL JS 和 MapLibre GL JS 应用程序中使用 ArcGIS 服务。

- 用于扩展 ArcGIS 产品的 SDK：
	- [ArcGIS CityEngine SDKs (C++)](https://github.com/esri/cityengine-sdk) - 过程运行时 (PRT) 的 C++ API、文档和示例。
	- [ArcGIS CityEngine SDKs (Python)](https://github.com/Esri/pyprt) - CityEngine 的*程序运行时* (PRT) 的 Python 绑定。
	- [ArcGIS Earth Automation API](https://doc.arcgis.com/en/arcgis-earth/automation-api/get-started.htm) - 与 ArcGIS Earth 通信的指南、API 参考和示例。
	- [ArcGIS Enterprise SDK](https://developers.arcgis.com/enterprise-sdk/) - 用于扩展 ArcGIS Enterprise 的指南、API 参考和示例代码。
	- [ArcGIS Pro SDK for Microsoft .NET](https://pro.arcgis.com/en/pro-app/latest/sdk/) - 用于扩展 ArcGIS Pro Desktop 的文档、教程、API 参考、常见问题解答等。

- 旧版 SDK：
	- [ArcGIS Maps SDK for Java](https://developers.arcgis.com/java/) - 用于构建桌面应用程序的指南、示例代码和 API 参考。
	- [ArcObjects SDK for .NET](https://desktop.arcgis.com/en/arcobjects/latest/net/webframe.htm#RoadmapToExtendingArcObjects.htm) - 有关构成 ArcGIS 基础的组件对象模型 (COM) 组件库的 .NET SDK 的文档。
	- [ArcObjects SDK for Java](https://desktop.arcgis.com/en/arcobjects/latest/java/#80146cac-6b50-4c82-a9f5-7a5be3406c5b.htm) - 有关构成 ArcGIS 基础的组件对象模型 (COM) 组件库的 Java SDK 的文档。

## 应用程序生成器和 CLI

- [@arcgis/cli](https://github.com/Esri/arcgis-js-cli) - 快速构建 ArcGIS API for JavaScript 的各种应用程序。
- [generator-esri-appbuilder-js](https://github.com/Esri/generator-esri-appbuilder-js) - Yeoman 生成器可帮助自定义 Esri 的 Web AppBuilder。
- [koop-cli](https://github.com/koopjs/koop-cli) - 用于构建 Koop 应用程序和插件的工具。

## ArcGIS 位置服务

- [ArcGIS location services Postman Workspace](https://www.postman.com/esridevs/workspace/arcgis-location-services) - 邮递员集合可促进与许多位置服务的合作。
- [Basemap styles service (v1)](https://developers.arcgis.com/documentation/mapping-apis-and-services/maps/services/basemap-layer-service/) - 访问街道、卫星和其他底图样式的地图和场景。
- [Basemap styles service (v2)](https://developers.arcgis.com/rest/basemap-styles/) - 访问多种地图样式、添加名胜古迹、设置标签语言、文字视图等。
- [Places service](https://developers.arcgis.com/rest/places/) - 搜索世界各地的企业和地理位置，以及每个地方的详细信息。
- [Elevation service](https://developers.arcgis.com/documentation/mapping-and-location-services/elevation/) - 获取高于或低于平均海平面或地面的位置的垂直距离（高度）。
- [Hydrology analysis service](https://developers.arcgis.com/rest/elevation-analysis/hydrology-analysis-service/) - 追踪水流并生成分水岭。
- [Geocoding service](https://developers.arcgis.com/documentation/mapping-apis-and-services/search/services/geocoding-service/) - 搜索世界各地的地址、企业和地点。
- [GeoEnrichment service](https://developers.arcgis.com/documentation/mapping-apis-and-services/demographics/services/geoenrichment-service/) - 查找有关某个位置或区域的事实和人口统计信息。
- [Routing service](https://developers.arcgis.com/documentation/mapping-apis-and-services/routing/services/routing-service/) - 获取路线导航并解决高级路线问题。
- [Printing tools service](https://developers.arcgis.com/rest/services-reference/enterprise/export-web-map-task.htm) - 从高级网络地图生成静态地图（png、jpg、pdf 等）。
<!--lint disable double-link-->
- [Spatial analysis service](https://developers.arcgis.com/rest/analysis/) - 处理空间数据集以发现关系和模式。
- [Offline packaging service](https://developers.arcgis.com/rest/packaging/api-reference/create-map-area.htm) - 创建和管理预先规划的地图区域以生成离线地图。

## 代码示例和片段

- [ArcGIS Code Sharing](http://codesharing.arcgis.com/) - 搜索、浏览和使用代码、脚本、模型、加载项、小部件等。
- [Esri/developer-support](https://github.com/Esri/developer-support) - 社区示例可帮助您成功使用所有 ArcGIS 开发产品（Python、.NET、JavaScript、Android…）。
- [esrinederland/CoolScripts](https://github.com/esrinederland/CoolScripts) - Esri 荷兰 脚本和片段供重复使用。
- [Esri 德国 Github 组织](https://github.com/EsriDE)：Esri Deutschland 提供的代码示例、工具等。
- [EsriJapan/arcgis-dev-resources](https://github.com/EsriJapan/arcgis-dev-resources) - ArcGIS Developers 開発リソース集 (by Esri Japan).
- .NET：
  	- [ArcGIS Maps SDK for .NET MAUI samples](https://developers.arcgis.com/net/maui/sample-code/) - Esri 的官方 ArcGIS Maps SDK MAUI 产品团队示例。
	- [ArcGIS Maps SDK for .NET UWP samples](https://developers.arcgis.com/net/uwp/sample-code/) - Esri 的官方 ArcGIS Maps SDK for .NET 产品团队示例。
 	- [ArcGIS Maps SDK for .NET WinUI samples](https://developers.arcgis.com/net/winui/sample-code/) - Esri 的官方 ArcGIS Maps SDK for .NET 产品团队示例。
	- [ArcGIS Maps SDK for .NET WPF samples](https://developers.arcgis.com/net/wpf/sample-code/) - Esri 的官方 ArcGIS Maps SDK for .NET 产品团队示例。
- 安卓：
	- [ArcGIS Maps SDK for Kotlin samples](https://developers.arcgis.com/kotlin/sample-code/) - 适用于 Kotlin 的 Esri 官方 ArcGIS Maps SDK for Kotlin 产品团队示例。
- 街机：
  - [ArcGIS Arcade Expression Templates](https://github.com/Esri/arcade-expressions) - 跨所有支持的配置文件的可重用 Arcade 表达式的集合。
- iOS：
	- [ArcGIS Maps SDK for iOS sample code](https://developers.arcgis.com/ios/swift/sample-code/) - Esri 的官方 ArcGIS Maps SDK for iOS 产品团队示例。
- JavaScript：
	- [ArcGIS API for JavaScript Sample Code](https://developers.arcgis.com/javascript/latest/sample-code/) - Esri 的官方 JavaScript API 产品团队示例。
	- [ArcGIS REST JS demos](https://github.com/Esri/arcgis-rest-js/tree/master/demos) - 由 Esri 的 REST JS 维护人员构建的演示应用程序。
	- [arcgis-js-api-starter-apps](https://github.com/hhkaos/arcgis-js-api-starter-apps) - 用于开始使用 ArcGIS API for JavaScript 4.x 的样板集合。
	- [Esri/arcgis-js-vscode-snippets](https://github.com/Esri/arcgis-js-vscode-snippets) - ArcGIS API for JavaScript 常见代码模式的 Visual Studio 代码片段集合。
	- [Esri/jsapi-resources](https://github.com/Esri/jsapi-resources) - 为使用 ArcGIS API for JavaScript 的开发人员提供的资源集合。
	- [RalucaNicola/code-snippets-arcgis-api-js](https://github.com/RalucaNicola/code-snippets-arcgis-api-js) - ArcGIS API for JavaScript 的代码片段集合。
- 蟒蛇：
	- [ArcGIS API for Python Sample Notebooks](https://developers.arcgis.com/python/sample-notebooks/) - Esri 的官方 Python API 产品团队示例。
	- [esrinederland/CoolMaps](https://github.com/esrinederland/CoolMaps) - 显示您可以使用的很酷的示例地图。
- Qt：
	- [ArcGIS Maps SDK for Qt C++ sample code](https://developers.arcgis.com/qt/cpp/sample-code/) - Esri 的官方 ArcGIS Maps SDK for Qt 产品团队 C++ 示例。
- 统一：
  - [ArcGIS Maps SDK for Unity samples](https://developers.arcgis.com/unity/sample-code/) - Esri 的官方 ArcGIS Maps SDK for Unity 产品团队示例。
- 虚幻：
  - [ArcGIS Maps SDK for Unreal Engine samples](https://developers.arcgis.com/unreal-engine/sample-code/) - Esri 的官方 ArcGIS Maps SDK for Unreal Engine 产品团队示例。

## 数据转换工具

- 核心地理空间处理库：
  - [ArcPy](https://pro.arcgis.com/en/pro-app/arcpy/main/arcgis-pro-arcpy-reference.htm) - ArcGIS 地理处理框架的 Python 接口，用于自动化空间分析、数据管理和制图。
  - [gdal](https://github.com/OSGeo/gdal) - 用于栅格和矢量地理空间数据格式的转换器库。
  - [loam](https://github.com/azavea/loam) - 浏览器中 GDAL 的 JavaScript 包装器。
- 格式转换：
  - [arcgis-json-to-geojson](https://github.com/gavinr/arcgis-json-to-geojson) - 将 ArcGIS JSON 规范中的图层转换为 GeoJSON 规范。
  - [csv2geojson](https://viglino.github.io/ol-ext/examples/misc/csv2geojson.html) - 将点从 CSV 格式转换为 GeoJSON。
  - [geojson2svg](https://github.com/w8r/geojson2svg) - 使用内联或外部样式表将 GeoJSON 渲染为 SVG。
  - [geojsonio](https://github.com/ropensci/geojsonio) - 在许多数据格式与 GeoJSON 和 TopoJSON 之间相互转换。
  - [gtfs2geojson](https://github.com/node-geojson/gtfs2geojson) - 将 GTFS 数据转换为 GeoJSON。
  - [img2geojson](https://github.com/caseymm/img2geojson/) - 将图像拖到地图上，追踪所需的路径，然后导出为 GeoJSON。
  - [terraformer](https://github.com/terraformer-js/terraformer) - 将 ArcGIS JSON 与 GeoJSON 相互转换，将 WKT 几何图形与 GeoJSON 几何图形以及其他格式相互转换。
  - [togeojson](https://mapbox.github.io/togeojson/) - 轻松将 KML 和 GPX 转换为 GeoJSON。
  - [tokml](https://github.com/mapbox/tokml) - 将 GeoJSON 转换为 KML。
- 简化和概括：
  - [Distillery](http://shancarter.github.io/distillery/) - 用于简化和投影 TopoJSON 的 Web 应用程序。
  - [Feature Service Layer](https://developers.arcgis.com/rest/services-reference/enterprise/query-feature-service-layer-.htm) - 使用“maxAllowableOffset”参数通过“query”操作返回广义几何图形。
  - [Generalize method](https://esri-es.github.io/arcgis-search/?search=geometryEngine.generalize#gsc.tab=0&gsc.q=%22generalize%22%20site:developers.arcgis.com&gsc.sort=) - GeometryEngine 可以通过编程方式生成具有较少顶点的几何体。有多个 API 支持它：JavaScript、iOS、Android、.NET、Qt 和 Java。
  - [PostGIS ST_Simplify](https://postgis.net/docs/ST_Simplify.html) - 此操作使用 Douglas-Peucker 算法返回给定几何图形的“简化”版本。
  - [Mapshaper](https://github.com/mbloch/mapshaper) - 用于简化形状、编辑属性数据、剪辑、擦除、溶解、过滤等的 Web 应用程序。支持的文件格式：Shapefile、GeoJSON、TopoJSON 和 CSV 文件。

## 数据集成工具

- [ArcGIS Data Interoperability Extension](https://esri-es.github.io/awesome-arcgis/arcgis/products/extensions/data-interoperability/) - 用于转换 400 多种数据格式的桌面工具。
- [FME Server](https://www.safe.com/integrate/) - ETL 允许轻松地将几乎所有数据集转换为 ArcGIS 兼容格式，反之亦然。支持 500 多种格式和技术。
- [Koop](https://koopjs.github.io) - 用于连接空间 API 的 JavaScript 工具包。动态转换地理空间数据并用作 GeoJSON、矢量切片、要素服务等。
- [Make.com](https://www.make.com/en/integrations/survey123) - iPaaS 可自动执行使用 Survey123 所涉及的重复任务，让您的工作更加轻松。
- [node-red-contrib-arcgis-rest](https://flows.nodered.org/node/node-red-contrib-arcgis-rest) - 使用 JS 基金会的事件驱动应用程序的低代码编程来查询、删除、更新或插入数据。
- [Zapier for ArcGIS](https://marketplace.arcgis.com/listing.html?id=5ab7936269f8449b82b0f5c78695ab38) - iPaaS 无需编写任何代码即可实现自动化集成。
- [Tray.io](https://tray.io/connectors/arcgis-integrations) - 手动、计划和 Webhook 触发器可使用 Tray Platform 的 ArcGIS 连接器应用编辑、获取要素、图层等。

## 调试工具

- [cors-test.codehappy.dev](https://cors-test.codehappy.dev/) - 用于测试 CORS 请求的应用程序。
- [Fiddler Classic](https://www.telerik.com/fiddler/fiddler-classic) - 用于记录 HTTP(s) 网络流量的 Windows 工具。
- [GeoJSONLint](https://geojsonlint.com/) - 验证并查看您的 GeoJSON。
- [json-schema.org](https://json-schema.org/) - 允许您注释和验证 JSON 文档（包括多个验证器）的词汇。
- [mapbox/geojson-vt/debug](http://mapbox.github.io/geojson-vt/debug/) - 验证 GeoJSON 或 TopoJSON。
- [Postman interceptor](https://www.postman.com/product/postman-interceptor/) - Interceptor 使您能够从浏览器同步 cookie 并直接从 Chrome 捕获网络请求。
- [netbalancer.com](https://netbalancer.com/) - 用于本地网络流量控制和监控的 Windows 应用程序。

## 设计和造型

- 最佳实践、书籍、视频和培训：
	- [Cartography and Making Stunning Maps](https://www.youtube.com/watch?v=AGf_DjZZwXc) - 短视频展示了使用不同混合模式效果可以实现的一些示例。
	- [How to style using ArcGIS Online](https://www.youtube.com/watch?v=6vy-kVkIcRg&list=PLPjPOZQjCWEn6ezKrwN11L8NWhZ2JdpYd) - 包含展示一些 ArcGIS 样式功能的短视频集合的播放列表。
	- [Photoshop-style Graphics Effects for Your Layers and Data](https://www.youtube.com/watch?v=crmWm80hwKI) - 该视频介绍了如何使用混合模式以及图层和要素效果，通过 ArcGIS API for JavaScript 4.x 创建独特且令人惊叹的 Web 地图。
	- [MapUIPatterns](https://www.mapuipatterns.com/) - 最佳实践和设计原则。 UI 模式描述了观察到的和重复出现的设计问题的解决方案。
- 开发者工具：
	- [Calcite Design System](https://developers.arcgis.com/calcite-design-system/) - 地图图标、Web 组件和良好实践的集合。
  - [Calcite Intellisense Visual Studio Code Extension](https://marketplace.visualstudio.com/items?itemName=K-Dev.calcite-intellisense) - 使用 Esri 的官方自定义数据 JSON 为 Esri Calcite Design System Web 组件注入 HTML IntelliSense（完成、悬停、文档）。
	- [Calcite Snippets Visual Studio Code Extension](https://marketplace.visualstudio.com/items?itemName=K-Dev.calcite-snippets) - Calcite 设计系统组件的便捷代码片段集合，旨在提高在 Visual Studio Code 中使用 Calcite 构建 Web 应用程序时的工作效率。
	<!--lint disable double-link-->
	- [geojson2svg](https://github.com/w8r/geojson2svg) - 使用内联或外部样式表将 GeoJSON 渲染为 SVG。
- 图形用户界面：
	- [ArcGIS Vector Tile Style Editor](https://developers.arcgis.com/documentation/mapping-apis-and-services/tools/vector-tile-style-editor/) - 应用程序的样式矢量切片底图图层。
	- [arcgis-vectortile-style-editor](https://github.com/Esri/arcgis-vectortile-style-editor) - 通过 JSON 更新 Esri 矢量底图样式的简约工具。
	- [EsriUK mapstyler](https://github.com/EsriUK/mapstyler) - 使用图像快速设置 Esri 矢量切片图层的样式。

## 开发者指南

- [Content management](https://developers.arcgis.com/documentation/mapping-apis-and-services/content-management/) - 存储、管理和访问私人和公共内容。
- [Data hosting](https://developers.arcgis.com/documentation/mapping-apis-and-services/data-hosting/) - 作为数据服务来存储、管理和访问您的数据。
- [Demographics](https://developers.arcgis.com/documentation/mapping-apis-and-services/demographics/) - 通过 GeoEnrichment 服务发现当地事实和人口统计信息。
- [Geocoding](https://developers.arcgis.com/documentation/mapping-apis-and-services/search/) - 使用地理编码服务搜索地址、企业和感兴趣的地点 (POI)。
- [Maps](https://developers.arcgis.com/documentation/mapping-apis-and-services/maps/) - 使用底图图层服务和数据服务显示 2D 地图和 3D 场景。
- [Offline](https://developers.arcgis.com/documentation/mapping-apis-and-services/offline/) - 断开连接时显示、分析和编辑数据。
- [Routing](https://developers.arcgis.com/documentation/mapping-apis-and-services/routing/) - 使用路线服务查找路线和方向。
- [Security and authentication](https://developers.arcgis.com/documentation/mapping-apis-and-services/security/) - 使用 API 密钥和 OAuth 2.0 访问服务和内容。
- [Visualization](https://developers.arcgis.com/documentation/mapping-apis-and-services/visualization/) - 设置图层样式以可视化 2D 和 3D 数据。

## 帮手

- [arcgis-geometry-calculations](https://github.com/hhkaos/arcgis-geometry-calculations) - 用于创建和获取 ArcGIS 几何计算的 Web 应用程序。
- [arcgis-js-api-camera-helper](https://github.com/pjmclaughlin1979/arcgis-js-api-camera-helper) - 用于获取 ArcGIS API for JavaScript 4.x 中 3D Web 应用程序的相机位置 JSON 对象的 Web 应用程序。
- [arcgis-js-api-extent-helper](https://arcgis-js-api-extent-helper.gavinr.com/) - Web 应用程序，用于获取 ArcGIS API for JavaScript 4.x 中 Web 应用程序的地图范围 JSON 对象。
- [ArcGIS JS API Module Butler](https://marketplace.visualstudio.com/items?itemName=ScottDavis.vscode-arcgis-js-api-module-butler&ssr=false#overview) - VSCode 扩展，用于快速为 @arcgis/core 包添加 ES 导入语句，而无需离开当前的代码上下文。
- [epsg.io](https://github.com/maptiler/) - 用于发现和转换世界各地坐标系的网站。
- [esri-loader](https://github.com/Esri/esri-loader) - 一个小型库，可帮助您在使用流行的 JavaScript 框架和捆绑程序构建的应用程序中延迟加载 ArcGIS API for JavaScript（即从 CDN）。
- [esri-loader-hooks](https://github.com/tomwayson/esri-loader-hooks) - 用于将 ArcGIS API for JavaScript 与 esri-loader 结合使用的自定义 React 挂钩。
- [geojson-random-generator](https://github.com/erick-otenyo/geojson-random-generator) - 快速生成并下载随机 GeoJSON 以进行测试。
- [reducegeojson](https://github.com/radical-data/reducegeojson) - 用于减小 GeoJSON 文件大小以进行 Web 优化的工具。
- [histogrand](https://github.com/hhkaos/histogrand) - 根据定制直方图的随机值生成器。
- [mercator-geographic-converter](https://github.com/hhkaos/mercator-geographic-converter/) - 地理单位（纬度、经度）和墨卡托单位（x、y）之间的简单坐标转换器。
- [react-sceneview](https://github.com/Esri/react-sceneview) - 一个简单的 Esri SceneView React 组件，基于 ArcGIS API for JavaScript 构建。
- [bboxfinder](http://bboxfinder.com/) - 用于获取地图上绘制的边界框坐标的简单 Web 应用程序。
- [snippets client side raster functions](https://ubatsukh.github.io/arcgis-js-api-demos/clientside-rasterfunctions/index.html) - 客户端栅格函数是直接对源图像像素进行处理的操作。

## 地图和数据探索

- [ArcGIS Map Viewer](https://www.arcgis.com/apps/mapviewer/index.html) - 用于为 2D 应用程序创建、探索和共享 Web 地图的 Web 应用程序。
- [ArcGIS Map Viewer (classic version)](https://arcgis.com/home/webmap/viewer.html) - 用于为 2D 应用程序创建、探索和共享 Web 地图的 Web 应用程序。
- [ArcGIS Scene Viewer](https://www.arcgis.com/home/webscene/viewer.html) - 用于为 3D 应用程序创建、探索和共享 Web 地图的 Web 应用程序。
- [Geo Data Viewer](https://marketplace.visualstudio.com/items?itemName=RandomFractalsInc.geo-data-viewer) - 用于地理数据分析的 VSCode 扩展。支持生成和查看地图。
- [geojson.io](https://github.com/mapbox/geojson.io) - 用于可视化、生成和编辑地理空间矢量数据的 Web 应用程序。支持 GeoJSON、TopoJSON、CSV、KML、WKT 和 Shapefile。
- [gpxstudio](https://github.com/gpxstudio/gpxstudio.github.io) - 在线开源 GPX 文件编辑器。
- [Mapshaper](https://github.com/mbloch/mapshaper) - 用于简化形状、编辑属性数据、剪辑、擦除、溶解、过滤等的 Web 应用程序。支持的文件格式：Shapefile、GeoJSON、TopoJSON 和 CSV 文件。
- [Smart Mapping](https://www.esri.com/en-us/smart-mapping) - 它内置于地图和场景查看器中，但 JavaScript 和 Python 等一些 API 也提供了实用程序来帮助构建数据探索工具。
- [VSCode Map Preview](https://marketplace.visualstudio.com/items?itemName=jumpinjackie.vscode-map-preview) - 用于在地图上直观预览地理空间文件内容（GeoJSON、KML 等）的扩展。

## 游乐场

- [arcgis-arcade-playground](https://developers.arcgis.com/arcade/playground/) - 尝试使用便携式脚本语言来创建 ArcGIS 自定义可视化和标签表达式。
- [cim-symbol-builder](https://github.com/Esri/cim-symbol-builder-js) - 生成 CIM 符号以与 ArcGIS 客户端 API 和要素服务配合使用。
- [geometry-inspector](http://brianbunker.github.io/geometry-inspector/) - 在地图上快速显示 EsriJSON、GeoJSON 或 WKT，或在地图上绘制以获取 EsriJSON、GeoJSON 或 WKT。
- [js-symbol-playground 3.x](https://developers.arcgis.com/javascript/3/samples/playground/index.html) - 生成符号以与 ArcGIS API for JavaScript 3.x 配合使用。
- [js-symbol-playground 4.x](https://developers.arcgis.com/javascript/latest/sample-code/playground/live/) - 生成符号以与 ArcGIS API for JavaScript 4.x 配合使用。
- [Postman workspaces](https://www.postman.com/esridevs) - 邮递员集合用于试验位置服务和身份验证。
- [Firefly Symbols Generator](https://vannizhang.github.io/firefly-symbols-generator/dist/) - 萤火虫符号生成。

## 空间分析

<!--lint disable double-link-->
- [ArcGIS Analysis services](https://developers.arcgis.com/rest/analysis-services/) - 空间、栅格、高程、水文学和公共设施网络分析。
- [Esri/gis-tools-for-hadoop](https://github.com/Esri/gis-tools-for-hadoop) - 用于大数据空间分析的 GIS 工具集合。
- [Esri/spatial-framework-for-hadoop](https://github.com/Esri/spatial-framework-for-hadoop) - 允许开发人员和数据科学家使用Hadoop数据处理系统进行空间数据分析。
- [Client-side Geometry Engine](https://esri-es.github.io/arcgis-search/?search=geometry+engine&utm_source=chrome-extension#gsc.tab=0&gsc.q=geometry%20engine%20site:developers.arcgis.com&gsc.sort=) - 允许您测试空间关系、计算新几何形状以及测量长度、面积、距离等。
	- [ArcGIS API for JavaScript `geometryEngine`](https://developers.arcgis.com/javascript/latest/api-reference/esri-geometry-geometryEngine.html) - 适用于浏览器和 Node.js。
	- [ArcGIS API for Python `arcgis.geometry`](https://developers.arcgis.com/python/api-reference/arcgis.geometry.html)
	- [ArcGIS Maps SDK for .NET `GeometryEngine`](https://developers.arcgis.com/net/api-reference/api/netwin/Esri.ArcGISRuntime/Esri.ArcGISRuntime.Geometry.GeometryEngine.html)
	- [ArcGIS Maps SDK for Android `GeometryEngine`](https://developers.arcgis.com/android/api-reference/reference/com/esri/arcgisruntime/geometry/GeometryEngine.html)
	- [ArcGIS Maps SDK for iOS `AGSGeeometryEngine`](https://developers.arcgis.com/ios/api-reference/interface_a_g_s_geometry_engine.html)
	- [ArcGIS Maps SDK for Qt `GeometryEngine`](https://developers.arcgis.com/qt/cpp/api-reference/esri-arcgisruntime-geometryengine.html)
- [Turf.js](https://github.com/Turfjs/turf) - 针对浏览器和 Node.js 的地理空间分析。

## 规格

- [Cartographic Information Model spec](https://github.com/Esri/cim-spec) - 地图内容规范用于保存和传输以 JSON 表示的 GIS 数据集的制图描述。
- [Common data types](https://developers.arcgis.com/documentation/common-data-types/geometry-objects.htm) - ArcGIS REST API 返回的几何和空间参考对象的 JSON 格式：点、多点、折线、多边形和包络线。
- [GeoServices spec](https://github.com/koopjs/FeatureServer) - 基于 Open Web Foundation REST 的 API，提供对 Esri 使用的结构化地理空间数据的完整访问。
- [Indexed 3D Scene Layers](https://github.com/Esri/i3s-spec) - 任意大量地理数据容器的服务和封装标准。
- [Shapefile Format](https://www.esri.com/content/dam/esrisites/sitecore-archive/Files/Pdfs/library/whitepapers/pdfs/shapefile.pdf) - GIS 软件的地理空间矢量数据格式规范。
- [Spatial reference specifications](https://developers.arcgis.com/documentation/spatial-references/#spatial-reference-specifications) - 众所周知的 ID (WKID) 整数值列表或称为众所周知文本 (WKT) 的文本字符串定义，用于定义空间参考。
- [Tile Package Specification](https://github.com/Esri/tile-package-spec) - 包含一组切片和切片方案的压缩文件，可用作 ArcGIS 应用程序中的底图。
- [Web Map spec](https://developers.arcgis.com/web-map-specification/) - 可共享的 2D 地图。它描述定义 web 地图的 JSON 对象。
- [Web Scene spec](https://developers.arcgis.com/web-scene-specification/) - 定义可共享 3D 场景的内容（视点、相机、底图图层、图层、样式等）的 JSON 结构。

---

<!--lint disable no-emphasis-as-heading-->
**相关精彩列表**

- [awesome-arcgis](https://github.com/esri-es/awesome-arcgis/) - 带有 wiki 风格的精彩列表，其中包含有关 Esri 和 ArcGIS 的资源，按以下方式组织：产品、行业、文件格式、内容提供商等。
- [awesome-earthobservation-code](https://github.com/acgeospatial/awesome-earthobservation-code) - 工具、教程、代码、有用的项目以及有关地球观测和地理空间内容的链接。
- [awesome-geojson](https://github.com/tmcw/awesome-geojson) - GeoJSON 实用程序：操作、编辑器和查看器、验证、服务、转换等。
- [awesome-geospatial](https://github.com/sacridini/Awesome-Geospatial) - 数据库、雷达、激光雷达、网络地图开发等。
- [awesome-gis](https://github.com/sshuair/awesome-gis) - GIS、遥感、3D 应用程序、网络地图服务器、地理空间库、开放标准、数据等。
- [awesome-json-datasets](https://github.com/jdorfman/awesome-json-datasets) - 不需要身份验证的 JSON 数据集：气候、犯罪、政府、NASA、旅行等。
- [awesome-open-geoscience](https://github.com/softwareunderground/awesome-open-geoscience) - 从存储库中精心挑选，使我们作为地球科学家、黑客和数据管理员的生活变得更轻松，甚至更棒。
- [awesome-public-datasets](https://github.com/awesomedata/awesome-public-datasets) - 以主题为中心的高质量开放数据集列表。
- [awesome-remote-sensing-change-detection](https://github.com/wenhwu/awesome-remote-sensing-change-detection) - 与遥感变化检测相关的数据集、代码和竞赛列表。
- [awesome-satellite-imagery-datasets](https://github.com/chrieke/awesome-satellite-imagery-datasets) - 带有计算机视觉和深度学习注释的卫星图像训练数据集列表。
- [awesome-semantic-segmentation](https://github.com/mrgloom/awesome-semantic-segmentation) - 按架构（语义分割、实例感知分割等）、RNN、GANS、数据集等划分的网络。
- [awesome-vector-tiles](https://github.com/mapbox/awesome-vector-tiles) - Mapbox Vector Tile 规范的实现：解析器和生成器、客户端、应用程序和命令行工具、CLI 实用程序、服务器等。

<!--lint disable no-emphasis-as-heading-->
**问题**

任何悬而未决的问题都是公平的。即使只是告诉我们您想看什么也会非常有帮助！

您可以[提出问题](https://github.com/ArcGIS/awesome-arcgis-developer/issues/new) 来请求或建议特定资源。

<!--lint disable no-emphasis-as-heading-->
**贡献**

Esri 欢迎任何人做出贡献。您可以[发出拉取请求](https://github.com/ArcGIS/awesome-arcgis-developer/pulls)来提出更新，但在执行此操作之前，请：

- 检查[此存储库的贡献指南](./CONTRIBUTING.md)。
- 查看[以前记录的问题](https://github.com/ArcGIS/awesome-arcgis-developer/issues)。

有关更多信息，请参阅 Esri 的[贡献指南](https://github.com/esri/contributing)。

<!--lint disable no-emphasis-as-heading-->

**脚注**

版权所有 2025 Esri
