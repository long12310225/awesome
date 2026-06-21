<!--lint disable double-link awesome-heading -->
<div align='center'>
<h2>Awesome Frontend GIS   <a href='https://github.com/sindresorhus/awesome'>
    <img src='https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg' alt='Awesome' href='https://github.com/sindresorhus/awesome'>
  </a></h2>

用于 Web 浏览器的地理信息系统 (GIS)。 <br>
用于管理、分析、编辑和可视化地理数据。
  
<div>
    <a href='https://github.com/eurostat/gridviz' target='_blank'>
        <img src='./images/awesome-fronted-gis-banner.png'>
    </a>
</div>

*与地理空间相关的网络框架、工具、演示、应用程序、数据源等的汇编。*
 
</div>


## 内容
- [👨‍💻 JavaScript 库](#-javascript-libraries)
  - [Mapping](#mapping)
  - [数据处理](#data-processing)
  - [LiDAR](#lidar)
  - [遥感](#remote-sensing)
- [💾 数据来源](#-data-sources)
  - [Downloads](#downloads)
  - [网络 API](#web-apis)
  - [Collections](#collections)
- [📒 笔记本](#-notebooks)
  - [Beginner](#beginner)
  - [Intermediate](#intermediate)
  - [Advanced](#advanced)
- [:world\_map: 网络地图](#world_map-web-maps)
- [🌐 网络应用程序](#-web-apps)
- [🎨 色彩建议](#-colour-advice)
- [📍 图标](#-icons)
- [📺 视频](#-videos)
- [📚 进一步阅读](#-further-reading)

## 👨‍💻 JavaScript 库

### 测绘
用于创建网络地图的库：

- [antvis L7](https://github.com/antvis/L7) - 基于 WebGL 的大规模地理空间数据可视化。 ![GitHub 星星](https://img.shields.io/github/stars/antvis/L7?style=social)
- [ArcGIS Maps SDK for JavaScript](https://developers.arcgis.com/javascript/latest/) - 现代 JavaScript API 和 Web 组件库，用于为浏览器构建交互式 2D 和 3D Web 应用程序。
- [ArcGIS REST JS](https://github.com/Esri/arcgis-rest-js) - 用于在 Node.js 和现代浏览器中运行的 ArcGIS REST API 的紧凑、模块化 JavaScript 包装器。 ![GitHub 星星](https://img.shields.io/github/stars/Esri/arcgis-rest-js?style=social)
- [Bertin.js](https://github.com/neocarto/bertin) - 一个 JavaScript 库，用于可视化地理空间数据并制作 Web 专题地图。 ![GitHub 星星](https://img.shields.io/github/stars/neocarto/bertin?style=social)
- [Cesium.js](https://github.com/CesiumGS/cesium) - 用于世界一流的地理空间数据 3D 绘图的开源 JavaScript 库。 ![GitHub 星星](https://img.shields.io/github/stars/CesiumGS/cesium?style=social)
- [d3-geo](https://github.com/d3/d3-geo) - 一个基于 D3.js 创建地图的库。 ![GitHub 星星](https://img.shields.io/github/stars/d3/d3-geo?style=social)
- [d3-geo-projection](https://github.com/d3/d3-geo-projection) - 扩展的地理预测。 ![GitHub 星星](https://img.shields.io/github/stars/d3/d3-geo-projection?style=social)
- [d3-geo-voronoi](https://github.com/Fil/d3-geo-voronoi) - 球体的 Voronoi 图和 Delaunay 三角剖分。 ![GitHub 星星](https://img.shields.io/github/stars/Fil/d3-geo-voronoi?style=social)
- [datamaps](https://github.com/markmarkoh/datamaps) - 一个文件中的可自定义地图可视化。 ![GitHub 星星](https://img.shields.io/github/stars/markmarkoh/datamaps?style=social)
- [Deck.GL](https://github.com/visgl/deck.gl) - WebGL2 支持的地理空间可视化层。 ![GitHub 星星](https://img.shields.io/github/stars/visgl/deck.gl?style=social)
- [Eurostat-map](https://github.com/eurostat/eurostat-map.js) - 数据驱动的地图。 ![GitHub 星星](https://img.shields.io/github/stars/eurostat/eurostat-map.js?style=social)
- [globe.gl](https://github.com/vasturiano/globe.gl) - 该库是三地球插件的便捷包装，使用 ThreeJS/WebGL 进行 3D 渲染。 ![GitHub 星星](https://img.shields.io/github/stars/vasturiano/globe.gl?style=social)
- [Google Maps](https://developers.google.com/maps/documentation/javascript) - 用于 Google 地图的 JavaScript API。
- [gridviz](https://github.com/eurostat/gridviz) - 用于可视化网格数据的包。 ![GitHub 星星](https://img.shields.io/github/stars/eurostat/gridviz?style=social)
- [HERE maps API](https://developer.here.com/develop/javascript-api) - 使用功能丰富且可自定义的 HERE 地图构建 Web 应用程序。
- [iTowns](https://github.com/iTowns/itowns) - 用 JavaScript/WebGL 编写的基于 Three.js 的框架，用于可视化 3D 地理空间数据。 ![GitHub 星星](https://img.shields.io/github/stars/iTowns/itowns?style=social)
- [Leaflet](https://github.com/Leaflet/Leaflet) - 领先的开源 JavaScript 库，适用于移动设备友好的交互式地图。 ![GitHub 星星](https://img.shields.io/github/stars/Leaflet/Leaflet?style=social)
- [Map Forecast API](https://github.com/windycom/API) - 基于 Leaflet 1.4.x 的简单易用的库。它允许您显示风图。 ![GitHub 星星](https://img.shields.io/github/stars/windycom/API?style=social)
- [Mapbox GL JS](https://github.com/mapbox/mapbox-gl-js) - JavaScript 库，使用 WebGL 从矢量图块渲染交互式地图。 ![GitHub 星星](https://img.shields.io/github/stars/mapbox/mapbox-gl-js?style=social)
- [maplibre](https://github.com/maplibre/maplibre-gl-js) - 它起源于 mapbox-gl-js 的开源分支，然后于 2020 年 12 月切换到非 OSS 许可证。![GitHub 星](https://img.shields.io/github/stars/maplibre/maplibre-gl-js?style=social)
- [MapTalks.js](https://github.com/maptalks/maptalks.js) - 用于集成 2D/3D 地图的开源 JavaScript 库。 ![GitHub 星星](https://img.shields.io/github/stars/maptalks/maptalks.js?style=social)
- [OpenLayers](https://github.com/openlayers/openlayers) - 一个高性能、功能丰富的库，用于在网络上创建交互式地图。 ![GitHub 星星](https://img.shields.io/github/stars/openlayers/openlayers?style=social)
- [react-simple-maps](https://github.com/zcreativelabs/react-simple-maps) - React 的 SVG 映射组件库，构建于 d3-geo 之上。 ![GitHub 星星](https://img.shields.io/github/stars/zcreativelabs/react-simple-maps?style=social)
- [Tangram](https://github.com/tangrams/tangram) - 用于创意制图的 WebGL 地图渲染引擎。 ![GitHub 星星](https://img.shields.io/github/stars/tangrams/tangram?style=social)
- [TerriaJS](https://github.com/TerriaJS/terriajs) - 用于构建丰富的、基于网络的地理空间数据浏览器的库。 ![GitHub 星星](https://img.shields.io/github/stars/TerriaJS/terriajs?style=social)
- [Wrld.js](https://github.com/wrld3d/wrld.js/) - 基于Leaflet的动画3D城市地图。 ![GitHub 星星](https://img.shields.io/github/stars/wrld3d/wrld.js?style=social)


### 数据处理
帮助您分析和处理地理空间数据的库：
- [Arc.js](https://github.com/springmeyer/arc.js) - 将大圆路线计算为 GeoJSON 或 WKT 格式的线。 ![GitHub 星星](https://img.shields.io/github/stars/springmeyer/arc.js?style=social)
- [awesome-GeoJSON](https://github.com/tmcw/awesome-geojson) - GeoJSON 工具目录。 ![GitHub 星星](https://img.shields.io/github/stars/tmcw/awesome-geojson?style=social)
- [Euclid.ts](https://github.com/mathigon/euclid.js) - 2D 欧几里得几何类、实用程序和绘图工具。 ![GitHub 星星](https://img.shields.io/github/stars/mathigon/euclid.js?style=social)
- [flatbush](https://github.com/mourner/flatbush) - JavaScript 中的 2D 点和矩形的快速静态空间索引。 ![GitHub 星星](https://img.shields.io/github/stars/mourner/flatbush?style=social)
- [FlatGeoBuf](https://github.com/flatgeobuf/flatgeobuf) - 基于平面缓冲区的地理数据的高性能二进制编码。 ![GitHub 星星](https://img.shields.io/github/stars/flatgeobuf/flatgeobuf?style=social)
- [flatten-js](https://github.com/alexbol99/flatten-js) - 用于操纵几何形状、查找相交、检查包含、计算距离、变换等。 ![GitHub 星星](https://img.shields.io/github/stars/alexbol99/flatten-js?style=social)
- [Galton](https://github.com/urbica/galton) - 轻量级 Node.js 等时服务器。 ![GitHub 星星](https://img.shields.io/github/stars/urbica/galton?style=social)
- [gdal3.js](https://github.com/bugra9/gdal3.js) - 将栅格和矢量地理空间数据转换为各种格式。 ![GitHub 星星](https://img.shields.io/github/stars/bugra9/gdal3.js?style=social)
- [geoblaze](https://github.com/GeoTIFF/geoblaze) - 一个极快的 JavaScript 栅格处理引擎。 ![GitHub 星星](https://img.shields.io/github/stars/GeoTIFF/geoblaze?style=social)
- [geobuf](https://github.com/mapbox/geobuf) - 地理数据的紧凑二进制编码。 ![GitHub 星星](https://img.shields.io/github/stars/mapbox/geobuf?style=social)
- [GeoTiff.js](https://github.com/geotiffjs/geotiff.js) - 解析 TIFF 文件以进行可视化或分析。 ![GitHub 星星](https://img.shields.io/github/stars/geotiffjs/geotiff.js?style=social)
- [geolib](https://github.com/manuelbieh/geolib) - 库提供基本的地理空间操作。 ![GitHub 星星](https://img.shields.io/github/stars/manuelbieh/geolib?style=social)
- [geopackage-js](https://github.com/ngageoint/geopackage-js) - GeoPackage JavaScript 库提供了读取 GeoPackage 文件的功能。 ![GitHub 星星](https://img.shields.io/github/stars/ngageoint/geopackage-js?style=social)
- [geoparquet](https://github.com/opengeospatial/geoparquet) - 在 Apache Parquet 中编码地理空间数据。 ![GitHub 星星](https://img.shields.io/github/stars/opengeospatial/geoparquet?style=social)
- [geotoolbox](https://github.com/neocarto/geotoolbox) - 提供多种与 geojson 属性一起使用的 GIS 操作。 ![GitHub 星星](https://img.shields.io/github/stars/neocarto/geotoolbox?style=social)
- [geojson-merge](https://github.com/mapbox/geojson-merge) - 将多个 GeoJSON 文件合并到一个要素集合中。 ![GitHub 星星](https://img.shields.io/github/stars/mapbox/geojson-merge?style=social)
- [geojson-vt](https://github.com/mapbox/geojson-vt) - 用于切片 GeoJSON 数据的高效 JavaScript 库。 ![GitHub 星星](https://img.shields.io/github/stars/mapbox/geojson-vt?style=social)
- [Geometric.js](https://github.com/HarryStevens/geometric) - 用于处理几何的 JavaScript 库。 ![GitHub 星星](https://img.shields.io/github/stars/HarryStevens/geometric?style=social)
- [JSTS](https://github.com/bjornharrtell/jsts) - JavaScript 拓扑套件。 ![GitHub 星星](https://img.shields.io/github/stars/bjornharrtell/jsts?style=social)
- [koop](https://github.com/koopjs/koop) - 用于连接不兼容的空间 API 的 JavaScript 工具包。 ![GitHub 星星](https://img.shields.io/github/stars/koopjs/koop?style=social)
- [math.gl](https://github.com/uber-web/math.gl) - JavaScript 数学库专注于地理空间和 3D 用例。 ![GitHub 星星](https://img.shields.io/github/stars/uber-web/math.gl?style=social)
- [Proj4js](https://github.com/proj4js/proj4js) - 将坐标从一种坐标系变换到另一种坐标系。 ![GitHub 星星](https://img.shields.io/github/stars/proj4js/proj4js?style=social)
- [rbush](https://github.com/mourner/rbush) - 用于 2D 空间索引的高性能 JavaScript 库。 ![GitHub 星星](https://img.shields.io/github/stars/mourner/rbush?style=social)
- [spl.js](https://github.com/jvail/spl.js) - 使得在 JavaScript 中使用 SpatiaLite 功能成为可能。 ![GitHub 星星](https://img.shields.io/github/stars/jvail/spl.js?style=social)
- [statsbreaks](https://github.com/riatelab/statsbreaks) - 将定量数据集分成几类以进行专题制图。 ![GitHub 星星](https://img.shields.io/github/stars/riatelab/statsbreaks?style=social)
- [Turf.js](https://github.com/Turfjs/turf) - 用于空间分析的 JavaScript 库。 ![GitHub 星星](https://img.shields.io/github/stars/Turfjs/turf?style=social)
- [topoJSON](https://github.com/topojson/topojson) - 将 GeoJSON 转换为 TopoJSON 以在 D3 地图中使用。 ![GitHub 星星](https://img.shields.io/github/stars/topojson/topojson?style=social)
- [Wicket](https://github.com/arthur-e/Wicket) - 一个适度的库，用于在众所周知的文本（WKT）和各种框架几何图形之间移动。 ![GitHub 星星](https://img.shields.io/github/stars/arthur-e/Wicket?style=social)


### 激光雷达
使用网络浏览器可视化点云的工具：

- [Plasio](https://github.com/verma/plasio) - 拖放式浏览器内 LAS/LAZ 点云查看器。 ![GitHub 星星](https://img.shields.io/github/stars/verma/plasio?style=social)
- [Potree](https://github.com/potree/potree) - 适用于大型数据集的 WebGL 点云查看器。 ![GitHub 星星](https://img.shields.io/github/stars/potree/potree?style=social)
- [Potree & Cesium.js](https://potree.org/potree/examples/cesium_retz.html) - Rezt，奥地利激光雷达观察器。
- [Three.js](https://threejs.org/examples/#webgl_loader_pcd) - 点云数据加载器。 ![GitHub 星星](https://img.shields.io/github/stars/mrdoob/ Three.js?style=social)

### 遥感

前端地球观测和遥感资源：

- [EOSDIS Worldview](https://github.com/nasa-gibs/worldview) - 用于浏览全球全分辨率卫星图像的交互式界面。 ![GitHub 星星](https://img.shields.io/github/stars/nasa-gibs/worldview?style=social)
- [Google Earth Engine](https://developers.google.com/earth-engine/tutorials/tutorial_api_01) - 地理空间处理服务。
- [Sentinel Hub custom scripts](https://github.com/sentinel-hub/custom-scripts) - 与 Sentinel Hub 一起使用的自定义脚本存储库。 ![GitHub 星星](https://img.shields.io/github/stars/sentinel-hub/custom-scripts?style=social)
- [sentinelhub-js](https://github.com/sentinel-hub/sentinelhub-js/) - 使用 Sentinel Hub 服务下载并处理卫星图像。 ![GitHub 星星](https://img.shields.io/github/stars/sentinel-hub/sentinelhub-js?style=social)
- [Spectral](https://github.com/awesome-spectral-indices/awesome-spectral-indices) - Google Earth Engine JavaScript API 的出色光谱指数。 ![GitHub 星星](https://img.shields.io/github/stars/awesome-spectral-indices/awesome-spectral-indices?style=social)


## 💾 数据来源
地理空间开放数据源集合：

### 下载
可供下载的数据：

- [ArcGIS Hub](https://hub.arcgis.com/) - 超过 380,000 个开放数据集。
- [Copernicus global DEM](https://ec.europa.eu/eurostat/web/gisco/geodata/digital-elevation-model/copernicus#Elevation) - 全球高程图块。
- [Copernicus open access hub](https://www.copernicus.eu/en/access-data/conventional-data-access-hubs) - 哥白尼卫星图像下载。
- [ETOPO1](https://www.ngdc.noaa.gov/mgg) - 地球表面 1 弧分全球地形模型。
- [European population grids - GISCO](https://ec.europa.eu/eurostat/web/gisco/geodata/grids) - 网格单元中的人口数字。
- [European Postcodes Point Data](https://ec.europa.eu/eurostat/web/gisco/geodata/administrative-units/postal-codes) - 欧洲各地邮政编码的位置。
- [Geoboundaries](https://www.geoboundaries.org/) - 世界上最大的开放、免费的政治边界数据库。
- [Global Biodiversity Information Facility (GBIF)](https://www.gbif.org/) - 开放获取生物多样性数据。
- [Global Climate Monitor](https://kerdoc.cica.es/) - 全球开放气候数据。
- [Global power plant database](https://datasets.wri.org/dataset/globalpowerplantdatabase) - 发电厂的开源数据库。
- [Galileo](https://galileo.gisdata.io/) - 地理空间数据发现和管理平台。
- [Healthcare Services in Europe](https://ec.europa.eu/eurostat/web/gisco/geodata/basic-services#Healthcare) - 欧洲医疗保健服务地点。
- [HydroSHEDS](https://www.hydrosheds.org/) - 全球应用的一致水文数据。
- [NASA Earth Data](https://search.earthdata.nasa.gov/search) - 使用 Earthdata Search 在浏览器中搜索、发现、可视化、优化和访问 NASA 地球观测数据。
- [Natural Earth](https://www.naturalearthdata.com/) - 免费矢量和栅格地图数据。
- [OpenAerialMap](https://openaerialmap.org/) - 用于访问许可图像的开放服务。
- [OpenMapTiles](https://openmaptiles.org/) - 免费 OpenStreetMap 矢量图块。
- [OpenStreetMap](https://www.geofabrik.de/data/download.html) - 免费的全球地理数据集。
- [Open Topography](https://opentopography.org/) - 高分辨率地形数据和工具。
- [Ookla internet speed data](https://github.com/teamookla/ookla-open-data) - 全球网络性能指标。 ![GitHub 星星](https://img.shields.io/github/stars/teamookla/ookla-open-data?style=social)
- [Sentinel Hub custom scripts](https://github.com/sentinel-hub/custom-scripts) - Sentinel Hub 的自定义脚本存储库。 ![GitHub 星星](https://img.shields.io/github/stars/sentinel-hub/custom-scripts?style=social)
- [USGS Earth Explorer](https://earthexplorer.usgs.gov/) - 查询和订购卫星图像等。
- [World Atlas TopoJSON](https://github.com/topojson/world-atlas) - 自然地球的矢量数据为 TopoJSON。 ![GitHub 星星](https://img.shields.io/github/stars/topojson/world-atlas?style=social)
- [World Bank](https://www.unccd.int/resources/knowledge-sharing-system/world-banks-open-data) - 免费获取全球发展数据。
- [WorldPop](https://www.worldpop.org/) - 开放访问空间人口数据集。


### 网络 API
用于动态使用地理空间数据的 Restful API：

- [Address API](https://gisco-services.ec.europa.eu/addressapi/docs/) - 具有地理编码和反向地理编码的泛欧地址数据。
- [API Geo](https://geo.api.gouv.fr/) - 法国官方地理数据 API。
- [ArcGIS location services](https://developers.arcgis.com/rest/location-based-services/) - 底图、地理编码、地点、路线和地理丰富。
- [bng2latlong](https://www.getthedata.com/bng2latlong) - 将英国国家网格转换为纬度和经度。
- [breezometer](https://docs.breezometer.com/api-documentation/introduction/) - 空气质量、天气、花粉和环境数据。
- [Country State City API](https://countrystatecity.in/) - 城市、州和国家数据的数据库。
- [Geoapify](https://apidocs.geoapify.com/) - 地理空间服务，例如地图、地理编码和路线选择。
- [geonames](http://www.geonames.org/export/web-services.html) - 支持地名查找和反向地理编码。
- [Geocode.xyz](https://geocode.xyz/) - 反向地理编码、正向地理编码和地理解析 API。
- [GISCO data distribution API](https://gisco-services.ec.europa.eu/distribution/v2/) - 欧盟委员会行政区域和边界的数据源。
- [GraphHopper Route Optimization API](https://www.graphhopper.com/route-optimization/) - 解决各种车辆路径问题。
- [movebank-api](https://github.com/movebank/movebank-api-doc) - 动物追踪数据平台。 ![GitHub 星星](https://img.shields.io/github/stars/movebank/movebank-api-doc?style=social)
- [OpenAQ](https://openaq.org/) - 最大的开源空气质量数据平台。
- [Open Charge Map API](https://openchargemap.org) - 电动汽车充电地点的公共登记处。
- [OpenCage](https://opencagedata.com/api) - 使用开放数据的正向和反向地理编码 API。
- [Open-Meteo](https://open-meteo.com/) - 全球天气预报 API。
- [Open Notify](http://open-notify.org/Open-Notify-API/) - 国际空间站的位置和太空中的人数。
- [Open Postcode Geo API](https://www.getthedata.com/open-postcode-geo-api) - 带有地理空间数据的英国邮政编码。
- [OpenSky API](https://github.com/openskynetwork/opensky-api) - 检索实时空域信息。 ![GitHub 星星](https://img.shields.io/github/stars/openskynetwork/opensky-api?style=social)
- [openrouteservice](https://openrouteservice.org/dev/#/api-docs) - 路线、等时线和地理编码服务。
- [OpenStreetMap](https://wiki.openstreetmap.org/wiki/Overpass_API) - 通过 Overpass API 检索 OpenStreetMap 数据。
- [opentopodata API](https://www.opentopodata.org/) - 开放地形数据 API。
- [Overpass API](https://wiki.openstreetmap.org/wiki/Overpass_API) - 检索 OpenStreetMap 数据。
- [RainViewer](https://www.rainviewer.com/api.html) - 免费天气雷达和卫星数据 API。
- [REST countries](https://restcountries.com/) - 通过 RESTful API 获取国家/地区信息。
- [Sunrise and sunset](https://sunrise-sunset.org) - 提供地点的日落和日出时间。
- [TomTom](https://developer.tomtom.com/api-explorer-index/documentation/product-information/introduction) - 地理编码、路线、交通等等。
- [USGS earthquake data](https://earthquake.usgs.gov/fdsnws/event/1/) - 通过各种参数搜索地震数据。
- [ZipCheckup API](https://github.com/artakulov/us-water-quality-data) - 免费 REST API，用于获取美国邮政编码级环境安全数据：水质、空气质量、PFAS、氡气、铅、洪水风险。 ![GitHub 星星](https://img.shields.io/github/stars/artakulov/us-water-quality-data?style=social)
- [what3words](https://developer.what3words.com/public-api) - 将 3 字地址转换为坐标。
- [PostalCodes](https://postalcodes.info/api) - 全球邮政编码搜索、国家/地区出口和地址验证数据。

### 收藏
开放地理空间数据集的编译和存储库：
- [awesome-public-datasets](https://github.com/awesomedata/awesome-public-datasets) - 一个很棒的存储库，充满了来自大量不同类别的开放数据集。  ![GitHub 星星](https://img.shields.io/github/stars/awesomedata/awesome-public-datasets?style=social)
- [Free GIS data](https://freegisdata.rtwilson.com/) - 链接到 500 多个站点，提供免费的地理数据集。
- [Public APIs](https://github.com/public-apis-dev/public-apis) - 用于软件和 Web 开发的免费 API 的集体列表。 ![GitHub 星星](https://img.shields.io/github/stars/public-apis-dev/public-apis?style=social)
- [WRI](https://datasets.wri.org/) - 世界资源研究所。
- [David Rumsey map collection](https://www.davidrumsey.com/) - 历史地图档案。

## 📒 笔记本
一些可以帮助您编码的 JavaScript 笔记本：

### 初学者
- [Hello, Leaflet](https://observablehq.com/@observablehq/hello-leaflet) - 可观察总部。
- [Hello, Bertin.js](https://observablehq.com/@neocartocnrs/hello-bertin-js) - 尼古拉斯·兰伯特.
- [Hello, Mapbox GL](https://observablehq.com/@observablehq/hello-mapbox-gl) - 迈克·博斯托克。
- [Hello, eurostat-map.js](https://observablehq.com/@joewdavies/eurostat-map-js) - 乔·戴维斯。
- [Hello, gridviz](https://observablehq.com/@neocartocnrs/hello-gridviz) - 尼古拉斯·兰伯特.

### 中级
- [World Tour](https://observablehq.com/@d3/world-tour) - D3。
- [Choropleth](https://observablehq.com/@d3/choropleth) - D3。
- [How to make a nice scalebar](https://observablehq.com/@jgaffuri/nice-scale-bar) - 朱利安·加夫里.
- [#GISCHAT Twitter Users with MapBoxGL - Globe Projection](https://observablehq.com/@chriszrc/gischat-twitter-users-with-mapboxgl-globe-projection) - 克里斯·马克思.
- [Hexgrid maps with d3-hexgrid](https://observablehq.com/@larsvers/hexgrid-maps-with-d3-hexgrid) - 拉斯弗斯。
- [Bivariate Choropleth with Continuous Color Scales](https://observablehq.com/@stephanietuerk/bivariate-choropleth-with-continuous-color-scales) - 斯蒂芬妮·图尔克。
- [Visualizing Eurostat grid data using Three.js & D3](https://observablehq.com/@joewdavies/visualizing-eurostat-grid-data-using-three-js-d3) - 乔·戴维斯。

### 高级

- [Try to impeach this? Challenge accepted!](https://observablehq.com/@karimdouieb/try-to-impeach-this-challenge-accepted) - 卡里姆·杜伊布。
- [Bars and pubs in Paris](https://observablehq.com/@neocartocnrs/bars-pubs-in-paris) - 尼古拉斯·兰伯特.
- [Brussels Street Gender Inequality](https://observablehq.com/@karimdouieb/brussels-streets-gender-inequality) - 卡里姆·杜伊布。
- [Animating voting maps with regl](https://observablehq.com/@bmschmidt/animating-voting-maps-with-regl) - 本杰明·施密特。
- [Election maps as dorling striped circles](https://observablehq.com/@jgaffuri/election-map-dorling-striped-circles) - 朱利安·加夫里.
- [GeoParquet on the web](https://observablehq.com/@kylebarron/geoparquet-on-the-web) - 凯尔·巴伦.
- [Interactive Regl wind demo](https://observablehq.com/@dkaoster/interactive-regl-wind-demo) - 丹尼尔·高.
- [Dorling cartogram of the Spanish Presidential election](https://observablehq.com/@adrianblanco/dorling-cartogram-of-the-spanish-presidential-election) - 阿德里安·布兰科。
- [Visualizing earthquakes with Three.js](https://observablehq.com/@joewdavies/visualizing-earthquakes-with-three-js) - 乔·戴维斯。
- [GeoArrow and GeoParquet in deck.gl](https://observablehq.com/@kylebarron/geoarrow-and-geoparquet-in-deck-gl) - 凯尔·巴伦.

## :world_map: 网络地图
有趣的网络地图汇编：

- [Map of notable people](https://tjukanovt.github.io/notable-people) - 托皮·楚卡诺夫。
- [Submarine cable map](https://www.submarinecablemap.com/) - 远程地理。
- [Radio Garden](https://radio.garden/) - 3D 地球仪收音机调谐器。
- [Map of every building in the United States](https://www.nytimes.com/interactive/2018/10/12/us/map-of-every-building-in-the-united-states.html) - 纽约时报。
- [Map of the Roman transport network](https://orbis.stanford.edu/) - 罗马世界的斯坦福地理空间网络模型。
- [WebGL Wind](https://github.com/mapbox/webgl-wind) - 基于 WebGL 的风力发电可视化。能够以 60 fps 渲染多达 100 万个风粒子。 ![GitHub 星星](https://img.shields.io/github/stars/mapbox/webgl-wind?style=social)
- [Statistical Atlas](https://ec.europa.eu/statistical-atlas/viewer) - 传单驱动的地图集，展示欧盟统计局的统计数据。
- [ShadeMap](https://shademap.app/) - 模拟任何日期和时间世界上的每一座山、每一座建筑和每棵树的影子。
- [ClimateArchive](https://climatearchive.org/) - 跨时间和空间的气候模型数据的交互式可视化。
- [Old Maps Online](https://www.oldmapsonline.org/) - 浏览历史地点并搜索带有时间线的旧地图。
- [chronotrains](https://www.chronotrains.com) - 8小时内可以坐火车去哪里？

## 🌐 网络应用程序
即插即用的地理空间 Web 应用程序：

- [city roads](https://anvaka.github.io/city-roads/) - 一次渲染任何城市的每条道路。 ![GitHub 星星](https://img.shields.io/github/stars/anvaka/city-roads?style=social)
- [Datawrapper](https://github.com/datawrapper/datawrapper) - 创建图表、地图和表格。
- [Fantasy Map Generator](https://github.com/Azgaar/Fantasy-Map-Generator) - 用于创建和编辑幻想地图的免费网络应用程序。 ![GitHub 星星](https://img.shields.io/github/stars/Azgaar/Fantasy-Map-Generator?style=social)
- [GeoLibre](https://github.com/opengeos/GeoLibre) - 一个轻量级的云原生 GIS 平台，用于跨桌面和 Web 环境可视化、探索和分析地理空间数据，并为移动屏幕提供响应式布局。 ![GitHub 星星](https://img.shields.io/github/stars/opengeos/GeoLibre?style=social)
- [geotiff.io](http://app.geotiff.io/) - 提供快速访问易于使用的光栅处理。
- [IMAGE](https://gisco-services.ec.europa.eu/image/) - 生成专题地图的工具。
- [Kepler](https://kepler.gl/demo) - 适用于大规模数据集的强大开源地理空间分析工具。
- [magrit](https://magrit.cnrs.fr/) - 专题制图的在线应用程序。
- [mapshaper](https://mapshaper.org/) - 地图数据的在线编辑器。
- [MapOnShirt](https://maponshirt.com) - 从地图创建丰富多彩的设计并将其转化为产品。
- [Maputnik](https://github.com/maputnik/editor) - 适用于 Mapbox GL 样式的免费开放可视化编辑器。 ![GitHub 星星](https://img.shields.io/github/stars/maputnik/editor?style=social)
- [mapus](https://github.com/alyssaxuu/mapus) - 用于协作探索和注释地图的工具。 ![GitHub 星星](https://img.shields.io/github/stars/alyssaxuu/mapus?style=social)
- [Peak Map](https://github.com/anvaka/peak-map) - 使用填充面积图可视化地图上任何区域的高程。 ![GitHub 星星](https://img.shields.io/github/stars/anvaka/peak-map?style=social)
- [Plasio](https://github.com/verma/plasio) - 浏览器内拖放式 LAS/LAZ 点云查看器。 ![GitHub 星星](https://img.shields.io/github/stars/verma/plasio?style=social)
- [StoryMap JS](https://storymap.knightlab.com/) - ESRI Story Map 应用程序的开源替代方案。
- [TopoExport](https://topoexport.com) - 使用开源数据集导出 2D 轮廓线和 3D 地形。
- [uMap](https://github.com/umap-project/umap) - 使用 OpenStreetMap 图层创建地图并将其嵌入您的站点中。 ![GitHub 星星](https://img.shields.io/github/stars/umap-project/umap?style=social)
- [bboxFinder](http://bboxfinder.com/) - 用于从地图中查找 bbox 值的帮助程序页面。
- [geojson.io](https://geojson.io/) - 一个快速、简单的工具，用于创建、查看和共享空间数据。
- [GeoJSONLint](https://geojsonlint.com/) - 使用此站点来验证和查看您的 GeoJSON。
- [Pharos AI](https://conflicts.app) - 开源实时情报仪表板，用于通过交互式 DeckGL/MapLibre 地理空间可视化跟踪地缘政治冲突。 ([源代码](https://github.com/Juliusolsson05/pharos-ai)) ![GitHub 星星](https://img.shields.io/github/stars/Juliusolsson05/pharos-ai?style=social)
- [Pumperly](https://github.com/GeiserX/pumperly) - 使用 MapLibre GL JS、PostGIS、Valhalla 路线和 Photon 地理编码的开源燃油价格比较和电动汽车充电路线规划器。 ![GitHub 星星](https://img.shields.io/github/stars/GeiserX/pumperly?style=social)


## 🎨 色彩建议
颜色的使用在数据可视化和制图中非常重要。以下是一些可帮助您为地图选择最佳颜色的工具：

- [CartoColor](https://github.com/CartoDB/CartoColor) - 一组基于地图颜色使用标准构建的自定义调色板。 ![GitHub 星星](https://img.shields.io/github/stars/CartoDB/CartoColor?style=social)
- [Chroma.js Color Palette Helper](https://gka.github.io/palettes/#/9) - Chroma.js 支持的工具，用于掌握多色调、多级色阶。 ![GitHub 星星](https://img.shields.io/github/stars/gka/palettes?style=social)
- [ColorBrewer](https://colorbrewer2.org/) - 基于 Cynthia Brewer 博士的研究的地图颜色建议。
- [Dicopal.js](https://github.com/riatelab/dicopal.js) - JavaScript 的离散调色板。 ![GitHub 星星](https://img.shields.io/github/stars/riatelab/dicopal.js?style=social)
- [Textures.js](https://github.com/riccardoscalco/textures) - 用于创建 SVG 模式的 JavaScript 库，专为数据可视化而设计。 ![GitHub 星星](https://img.shields.io/github/stars/riccardoscalco/textures?style=social)
- [viz-palette](https://www.susielu.com/data-viz/viz-palette) - 针对在 JavaScript 中调整、复制和粘贴颜色进行了优化的工具。


## 📍 图标
要添加到 GIS 网站的图标：
- [font-GIS](https://github.com/Viglino/font-gis) - 一个非常非常酷的图标字体集，可与 GIS 和空间分析工具一起使用。 ![GitHub 星星](https://img.shields.io/github/stars/Viglino/font-gis?style=social)
- [Map Icons Collection](https://mapicons.mapsmarker.com/) - 一组超过 1000 个免费且可自定义的图标，可用作地图上 POI（兴趣点）位置的地标。
- [Material Symbols](https://fonts.google.com/icons?icon.query=map) - 单个字体文件中包含超过 2,990 个字形，具有多种设计变体。
- [Geoapify map marker playground](https://apidocs.geoapify.com/playground/icon/) - 标记图标 API 可让您创建漂亮的图标并将其用作地图标记。

## 📺 视频
网络地图演示和教程的视频：

- [Mapping Geolocation with Leaflet.js - Working with Data and APIs in JavaScript](https://www.youtube.com/watch?v=nZaZ2dB6pow) - 编码列车。
- [10 Maps, and the Tech and Stories Behind Them](https://www.youtube.com/watch?v=PpWAKVjPlgU) - 马丁·兰布雷希茨。
- [Intermediate Three.js Tutorial - Create a Globe with Custom Shaders](https://www.youtube.com/watch?v=vM8M4QloVL0&t=4418s) - 克里斯课程。
- [Statistical Cartography - Design principles for statistical map design](https://www.youtube.com/watch?v=e803ElX5Q_c) - 朱利安·加夫里.


## 📚 进一步阅读
- [Fundamentals of Data Visualization](https://clauswilke.com/dataviz/) - 克劳斯·O·威尔克。
- [A Workbook for Interactive Cartography and Visualization on the Open Web](https://github.com/uwcartlab/webmapping) - 罗伯特·罗斯、卡尔·萨克、加雷斯·鲍德里卡-富兰克林、陈玉英、里奇·多诺霍、莉莉·豪特曼、蒂姆·普雷斯特比、罗宾·托洛奇科、尼克·安德伍德。 ![GitHub 星星](https://img.shields.io/github/stars/uwcartlab/webmapping?style=social)
- [Thematic Mapping: 101 Inspiring Ways to Visualise Empirical Data](https://www.esri.com/en-us/esri-press/browse/thematic-mapping) - 肯尼思·菲尔德.
- [Color use guidelines for mapping and visualization](https://colorbrewer2.org/learnmore/schemes_full.html#qualitative) - 辛西娅·A·布鲁尔。
- [Geospatial Network Visualization](https://geonetworks.github.io/) - 地理空间网络数据可视化技术的集合。


## 贡献

欢迎任何类型的贡献，只需遵循[指南](./CONTRIBUTING.md)：

- 填写[建议问题](https://github.com/joewdavies/awesome-frontend-gis/issues/new/)（更容易）。
- 打开 [拉取请求](https://github.com/joewdavies/awesome-frontend-gis/compare)。

---

如果您对此列表有任何疑问，请随时在 X（以前称为 Twitter）上联系我 [@joewdavies](https://twitter.com/joewdavies) 或[打开 GitHub 问题](https://github.com/joewdavies/awesome-frontend-gis/issues/new)。
