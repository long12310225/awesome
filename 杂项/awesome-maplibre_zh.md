[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

# 很棒的MapLibre

使用或支持 [MapLibre](https://maplibre.org) 的很棒的东西的集合！

MapLibre [核心项目](https://github.com/maplibre/maplibre/blob/main/PROJECT_TIERS.md)
指定有 ✅，托管项目有 💙。


## 地图渲染

- ✅ [MapLibre GL JS](https://github.com/maplibre/maplibre-gl-js) - 用于在 Web 上渲染地图的地图 SDK。
- ✅ [MapLibre Native](https://github.com/maplibre/maplibre-gl-native) - 用于在设备、应用程序和服务器上渲染地图的地图 SDK。
- 💙 [MapLibre RS](https://github.com/maplibre/maplibre-rs) - 用 Rust 编写的实验性地图渲染库。
- ✅ [MapLibre Plugins for Android](https://github.com/maplibre/maplibre-plugins-android) - Android 上 MapLibre 的插件集合；注释插件是一个核心项目。

## 地图样式

- ✅ [MapLibre 样式规范](https://github.com/maplibre/maplibre-style-spec) - MapLibre 样式规范，一种基于 JSON 的地图样式格式。

### 风格编辑器

- 💙 [Maputnik](https://github.com/maplibre/maputnik) - MapLibre GL JS 的视觉样式编辑器。托管于 [maplibre.org/maputnik](https://maplibre.org/maputnik)
- [MapPoster](https://mapposter.xyz/) - 自定义城市地图编辑器，使用 MapLibre GL JS 实现艺术主题。
- [Theme](https://github.com/lhapaipai/maplibre-theme) - 为您的 MapLibre GL Js Web 应用程序定制主题。 [演示](https://maplibre-theme.pentatrion.com/)
- [MapLibre VSCode Extension](https://github.com/Kanahiro/maplibre-vscode-extension) - 用于查看/编辑 MapLibre 样式的 VSCode 扩展。
- [QGIS2VectorTiles](https://gallpeters.github.io/QGIS2VectorTiles/) - 一个 QGIS 插件，将当前项目导出到样式矢量切片包中，包括样式文档、精灵和 MapLibre 查看器。

### 字体字形生成

- 💙 [Font Maker](https://github.com/maplibre/font-maker) - 用于将字体文件转换为 SDF 字体堆栈以在 MapLibre 中使用的 Web 应用程序。
- [SDF Font Tools](https://github.com/stadiamaps/sdf_font_tools) - 用于从字体生成 SDF 字体堆栈的 CLI 工具（类似于 FontMaker），以及可让您动态构建字体堆栈的包（在 MapLibre Martin 中使用）。

### 精灵生成

- [Spreet](https://github.com/flother/spreet) - Spreet 是一个命令行工具，可以从 SVG 图像目录创建 spritesheet（又名纹理图集）。
- [Figmasset](https://github.com/stamen/figmasset) - Figmasset 是一个有助于将 Figma 中的资源批量加载到 JavaScript 应用程序中的工具。
- [Sprite One](https://www.npmjs.com/package/@unvt/sprite-one) - 无需 Mapnik 即可生成精灵图像和 json。

## 导航和方向

- 💙 [适用于 iOS 的 MapLibre 导航 SDK](https://github.com/maplibre/maplibre-navigation-ios) - 基于 MapLibre 构建的逐向导航； Mapbox Navigation 的 FOSS 分支
- 💙 [适用于 Android 的 MapLibre 导航 SDK](https://github.com/maplibre/maplibre-navigation-android) - 基于 MapLibre 构建的逐向导航； Mapbox Navigation 的 FOSS 分支
- 💙 [MapLibre GL Directions](https://github.com/maplibre/maplibre-gl-directions) - 在 MapLibre GL JS 地图上显示路线方向的插件
- [Ferrostar](https://github.com/stadiamaps/ferrostar) - 使用 MapLibre 在 iOS、Android 和 Web 上从头开始构建的路线导航 SDK。
- [OMT Router](https://abelvm.github.io/omt-router/) - OpenMapTiles 快速、准确的客户端路由引擎

## 绑定

### 颤动

- 💙 [flutter-maplibre-gl](https://github.com/maplibre/flutter-maplibre-gl) - Android、iOS 和 Web 上的 Flutter 绑定，位于 pub.dev 的 [pub.dev/packages/maplibre_gl](https://pub.dev/packages/maplibre_gl)
- [flutter-maplibre](https://github.com/josxha/flutter-maplibre) - MapLibre Native 的 Flutter 绑定的全新、现代版本。

### 反应本机

- 💙 [MapLibre React Native](https://github.com/maplibre/maplibre-react-native) - 用于 React Native 的 MapLibre 模块（包括 Expo 支持）。

### 斯威夫特用户界面

- 💙 [MapLibre SwiftUI DSL](https://github.com/maplibre/swiftui-dsl) - 一个 Swift 包，弥合了 MapLibre Native 和 SwiftUI 之间的差距，具有类似 MapKit 的易用性。

### Jetpack Compose 或 Compose 多平台

- 💙 [MapLibre Compose](https://github.com/sargunv/maplibre-compose) - 一个 Compose 多平台库，用于将交互式矢量切片地图添加到您的 Android 和 iOS 应用程序中。
- [Ramani Maps](https://github.com/ramani-maps/ramani-maps) - 用于操作 Android 上的地图的 Jetpack Compose 库。
- [MapLibre Compose Playground](https://github.com/Rallista/maplibre-compose-playground) - Jetpack Compose 库的灵感来自 Ramani，但倾向于与 SwiftUI DSL 相似的 API，并且不强调绘图/编辑。
- [SKAMIR Maps](https://github.com/skamirmaps/skamirmaps) - MapLibre Native 的 Kotlin 多平台包装器

### 蟒蛇

- [py-maplibregl](https://github.com/eoda-dev/py-maplibregl) - MapLibre GL JS 的 Python 绑定，带有文档 [eoda-dev.github.io/py-maplibregl](https://eoda-dev.github.io/py-maplibregl/) 和示例 [eoda-dev.github.io/py-maplibregl/examples/road_safety](https://eoda-dev.github.io/py-maplibregl/examples/road_safety/)。
- [leafmap](https://github.com/opengeos/leafmap/) - 支持 MapLibre 映射后端的 python 包，包含文档 [leafmap.org](https://leafmap.org) 和示例 [leafmap.org/maplibre/overview](https://leafmap.org/maplibre/overview)
- [plotly.py](https://plotly.com/python/maps/) - 使用 Python 中的 MapLibre GL JS 创建分析地理空间图形。

### Qt（C++）

- 💙 [maplibre-native-qt](https://github.com/maplibre/maplibre-native-qt) - MapLibre Native Qt 绑定和 Qt 位置 MapLibre 插件

### R

- [mapgl](https://github.com/walkerke/mapgl) - MapLibre GL JS 的 R 绑定，文档位于 [walker-data.com/mapgl](https://walker-data.com/mapgl)

### 铁锈

- 💙 [maplibre-native-rs](https://github.com/maplibre/maplibre-native-rs) - MapLibre Native 的 Rust 绑定

### JavaScript

<!-- [JAVASCRIPT-BINDINGS]:BEGIN -->

#### 角

- 💙 [ngx-maplibre-gl](https://github.com/maplibre/ngx-maplibre-gl) - 与 [maplibre.org/ngx-maplibre-gl/demo](https://maplibre.org/ngx-maplibre-gl/demo/) 上的托管演示进行角度绑定

#### 阿斯特罗

- [maps-withastro](https://github.com/roblabs/maps-withastro) - 将 Leaflet 和 MapLibre 地图直接导入 Astro。

#### 埃图表

- [echartslayer](https://github.com/lzxue/echartLayer) - 提供echarts集成。
- [@naivemap/maplibre-gl-echarts-layer](https://www.naivemap.com/map-gl-layers/api/maplibre-gl-echarts-layer/) - 集成 Apache ECharts 的折线图和散点图。

#### 榆树

- [elm-mapbox](https://package.elm-lang.org/packages/gampleman/elm-mapbox/latest/) - 提供 Elm 集成。

#### 余烬

- [ember-mapbox-gl](https://github.com/kturney/ember-mapbox-gl) - 提供 Ember 集成。

#### 杰基尔

- [jekyll-maplibre](https://github.com/rriemann/jekyll-maplibre) - 提供 Jekyll 集成（插件）。

#### 反应

- [react-map-gl](https://visgl.github.io/react-map-gl/docs/get-started#using-with-a-compatible-fork) - 一套用于 mapbox-gl、maplibre-gl 或兼容库的 React 组件
- [react-map-components-maplibre](https://github.com/mapcomponents/react-map-components-maplibre) - 用于声明式 GIS 应用程序开发的 React 组件框架，在其 [showcase](https://catalogue.mapcomponents.org/) 和 [docs](https://mapcomponents.github.io/react-map-components-maplibre) 中提供演示
- [maplibre-react-components](https://maplibre-react-components.pentatrion.com/) - 仅针对 React 的轻量级 MapLibre 绑定。
- [react-mapbox-gl](https://github.com/alex3165/react-mapbox-gl) - 提供 React 集成。

#### 斯韦尔特

- [sveltekit-maplibre-boilerplate](https://github.com/watergis/sveltekit-maplibre-boilerplate) - 预配置的模板存储库在 svelte/sveltekit 中开发 MapLibre 应用程序。
- [svelte-maplibre](https://github.com/dimfeld/svelte-maplibre) - 提供 Svelte 集成。
- [svelte-maplibre-components](https://github.com/watergis/svelte-maplibre-components) - 一组与 svelte/sveltekit 集成的 maplibre 插件。该存储库由各种有用的插件组成，例如导出插件、图例插件、测量插件、属性表插件、游览插件等。
- [svelte-maplibre-gl](https://github.com/MIERUNE/svelte-maplibre-gl) - Svelte (v5) 组件包装 MapLibre GL JS，通过熟悉的 API 提供 GL JS 的声明式处理。

#### VueJS

- [@indoorequal/vue-maplibre-gl](https://github.com/indoorequal/vue-maplibre-gl) - Maplibre-gl-js 的 Vue 3 插件
- [LibreGL](https://github.com/themustafaomar/libregl) - 强大的 Maplibre Vue 库，具有直观的 API 和一系列高度可定制的组件。

#### 网络工具包

- [wtMapbox](https://github.com/yvanvds/wtMapbox) - 提供 Webtoolkit 集成。

#### 香草JS

- [plotly.js](https://plotly.com/javascript/maps/) - 使用 JavaScript 中的 MapLibre GL JS 创建分析地理空间图形。

<!-- [JAVASCRIPT-BINDINGS]:END -->


<!-- [JAVASCRIPT-PLUGINS]:BEGIN -->
## 用户界面插件

- 💙 [maplibre-gl-compare](https://github.com/maplibre/maplibre-gl-compare) - 使用户能够通过左右滑动来比较两个地图。
- [any-routing](https://github.com/marucjmar/any-routing) - 用于计算路线的模块化插件。
- [Gauge Legend](https://github.com/AbelVM/gauge_legend) - MapLibre GL JS 的动态仪表图例
- [mapbox-gl-controls](https://github.com/bravecow/mapbox-gl-controls) - 添加标尺、样式检查器、本地化和样式切换器的控件。
- [mapbox-gl-draw](https://github.com/mapbox/mapbox-gl-draw) - 添加对在地图上绘制和编辑要素的支持。
- [mapbox-gl-elevation](https://github.com/watergis/mapbox-gl-elevation) - 添加一个控件以从地形 RGB 图块集中检索高度。
- [mapbox-gl-infobox](https://github.com/el/infobox-control) - 添加一个控件来显示信息框或渐变。
- [mapbox-gl-legend](https://github.com/watergis/mapbox-gl-legend) - 添加一个控件，显示从地图样式生成的图例。
- [mapbox-gl-valhalla](https://github.com/watergis/mapbox-gl-valhalla) - 添加一个控件以提供来自 valhalla 服务器的等时线功能。
- [mapboxgl-minimap](https://github.com/aesqe/mapboxgl-minimap) - 添加一个控件以显示当前地图的微型概览。
- [maplibre-compass-pro](https://github.com/jedluk/maplibre-compass-pro) - 适用于 Maplibre GL 的老式指南针（带指南针）。 [演示](https://codesandbox.io/p/sandbox/peaceful-mirzakhani-tv38ck)
- [map-gl-style-switcher](https://github.com/muimsd/map-gl-style-switcher) - MapLibre GL JS 的可定制样式切换器控件，还有一个 `react-map-gl` 包装器。
- [maplibre-geoman](https://github.com/geoman-io/maplibre-geoman) - 用于绘制和编辑几何图层的插件。 [演示](https://geoman.io/demo/maplibre)
- [maplibre-preload](https://github.com/AbelVM/maplibre-preload) - 一个微小的零配置插件，用于预加载图块并在 MapLibre GL JS 中使用目标移动时平滑体验。
- [maplibre-gl-basemaps](https://github.com/ka7eh/maplibre-gl-basemaps) - 用于在栅格底图之间切换的插件。
- [maplibre-gl-export](https://github.com/watergis/maplibre-gl-export) - 添加将地图导出为 PDF 或 PNG、JPEG 和 SVG 等图像的控件。
- [maplibre-gl-map-to-image](https://github.com/Willjfield/maplibre-gl-map-to-image) - 从地图创建静态图像数据并将其设置为目标 html 图像元素的 src。与 maplibre-gl-export 类似，但适用于将图像嵌入文档而不是打印整页的用例。
- [maplibre-gl-measures](https://github.com/jdsantos/maplibre-gl-measures) - 用于在地图上采取措施的插件。
- [maplibre-gl-opacity](https://github.com/mug-jp/maplibre-gl-opacity) - 一个用于切换图层（如 Leaflet.control.layers）和更新不透明度的插件。 [演示](https://mug-jp.github.io/maplibre-gl-opacity/)
- [maplibre-gl-temporal-control](https://github.com/mug-jp/maplibre-gl-temporal-control) - 一个可以轻松动画时间数据的插件。 [演示](https://mug-jp.github.io/maplibre-gl-temporal-control/raster.html)
- [route-snapper](https://github.com/dabreegster/route_snapper) - 绘制路线和与道路对齐的区域。
- [Terra Draw](https://www.github.com/JamesLMilner/terra-draw) - 该库有一个 MapLibre GL JS 适配器，可为地图提供绘图和几何编辑功能
- [maplibre-gl-multiple-color-draw](https://github.com/kashishgadhiya/maplibre-gl-multiple-color-draw) - 使用每个要素的单独颜色绘制线条、多边形和徒手形状。包括 React hook、TypeScript 支持和 GeoJSON 导出。 [npm](https://www.npmjs.com/package/maplibre-gl-multiple-color-draw) · [演示](https://maplibre-gl-multiple-color-draw-dem.vercel.app/)
- [maplibregl-minimap](https://github.com/JabSYsEmb/maplibregl-minimap) - maplibregl 的可定制小地图控件。
- [maplibre-gl-style-flipper](https://github.com/geoglify/maplibre-gl-style-flipper) - 用于在 MapLibre GL JS 中的不同地图样式之间切换的自定义控件。
- [maplibre-pegman](https://github.com/rezw4n/maplibre-pegman) - 将 Google 街景集成到任何 MapLibre 地图中的插件。
- [maplibre-transition](https://github.com/popkinj/maplibre-transition) - 用于地图样式之间平滑过渡的插件。 [演示](https://observablehq.com/d/b9a97acdf712a77b)
- [maplibre-gl-layers-control](https://github.com/mvt-proj/maplibre-gl-layers-control) - 它允许显示/隐藏图层、不透明度控制以及与图例的集成。
- [maplibre-ui-translations](https://github.com/spwoodcock/maplibre-ui-translations) - 默认 MapLibre UI 的社区翻译。

## 地理编码和搜索插件
- [mapbox.photon](https://github.com/watergis/mapbox.photon) - 添加一个控件以通过 Photon API 提供地理编码功能。
- 💙 [maplibre-gl-geocoder](https://github.com/maplibre/maplibre-gl-geocoder) - 添加地理编码器控件。
- [maplibre-search-box](https://github.com/stadiamaps/maplibre-search-box) - 添加用于使用 Stadia 地图搜索地点的控件。
- [maptiler-geocoding-control](https://github.com/maptiler/maptiler-geocoding-control) - 添加地理编码控件以使用 MapTiler API 搜索地点。 [文档](https://docs.maptiler.com/sdk-js/modules/geocoding/)

## 地图渲染插件

- 💙 [MapLibre GL Leaflet](https://github.com/maplibre/maplibre-gl-leaflet) - 用于在 [Leaflet](https://leafletjs.com) 中渲染 MapLibre 样式的插件。
- [Americana Shield Renderer](https://www.npmjs.com/package/@americana/maplibre-shield-generator) - 渲染世界各地高速公路系统的路线标记。
- [deck.gl](https://github.com/visgl/deck.gl) - 添加高级 WebGL 可视化层。
- [Diplomat](https://github.com/osm-americana/diplomat/) - 自动将地图本地化为用户的语言。
- [flowmap.blue](https://github.com/ilyabo/flowmap.blue) - 从 Google Sheets 上发布的电子表格渲染地理流量图可视化。
- [H3J / H3T](https://github.com/INSPIDE/h3j-h3t) - 使用 MapLibre GL JS 进行客户端几何生成和渲染的 Light [H3](https://h3geo.org/) 数据格式
- [L7-maplibre-gl](https://github.com/antvis/l7) - 为maplibre-gl添加大规模WebGL驱动的地理空间数据可视化框架。[demo](https://l7.antv.antgroup.com/examples/map/map/#maplibre)
- [mapbox-gl-language](https://github.com/mapbox/mapbox-gl-language/) - 自动将地图本地化为用户的语言。
- [mapbox-gl-rtl-text](https://github.com/mapbox/mapbox-gl-rtl-text) - 添加从右到左的文本支持。
- [maplibre-gl-complex-text](https://github.com/wipfli/maplibre-gl-complex-text) - 添加了对一些复杂脚本的支持，包括高棉语和梵文。
- [mapbox-gl-traffic](https://github.com/mapbox/mapbox-gl-traffic) - 使用可选的切换按钮在地图上隐藏和显示交通图层。
- [maplibre-adiff-viewer](https://github.com/OSMCha/maplibre-adiff-viewer/) - 可视化 OpenStreetMap 增强的差异。
- [maplibre-contour](https://github.com/onthegomap/maplibre-contour) - 在 MapLibre GL JS 中渲染来自栅格 DEM 切片的等高线。
- [maplibre-gl-dates](https://github.com/OpenHistoricalMap/maplibre-gl-dates/) - 按日期过滤启用时间的地图。针对 OpenHistoricalMap 矢量切片进行了优化。
- [maplibre-gl-vector-text-protocol](https://github.com/jimmyrocks/maplibre-gl-vector-text-protocol) - 使用 addProtocol 功能支持“CSV”、“TSV”、“Topojson”、“KML”、“GPX”和“TCX”格式。
- [geogrid-maplibre-gl](https://github.com/falseinput/geogrid-maplibre-gl) - 渲染可定制的标线（地理网格）。
- [maplibre-gleo](https://gitlab.com/IvanSanchez/maplibre-gleo) - 使用“gleo”WebGL 地图渲染库添加符号。
- [maplibre-contourmap](https://github.com/AbelVM/maplibre-contourmap) - 在 MapLibre GL JS 中渲染来自矢量源的轮廓线。 [演示](https://abelvm.github.io/maplibre-contourmap/example/)
- [maplibre-three-plugin](https://github.com/dvt3d/maplibre-three-plugin) - 一个桥接插件，巧妙地将 MapLibre GL JS 与 Three.js 连接起来，使开发人员能够在地图上实现 3D 渲染和动画。
- [maplibre-gl-teritorio-cluster](https://github.com/teritorio/maplibre-gl-teritorio-cluster) - 集群插件实现了 MapLibre GL 层，具有可配置的 HTML 集群渲染器和事件支持。
- [maplibre-glass-css](https://github.com/corb555/maplibre-glass-css) - 标准 MapLibre 控件的玻璃 UI 主题。
- [maplibre-merge-protocol](https://github.com/indus/maplibre-merge-protocol) - 用于将几何图形与 MapLibre 中多个图块集的属性合并的自定义协议。 [演示](https://maplibre-merge-protocol.js.org/)
- [backproj/maplibre-proj](https://github.com/willcohen/backproj) - 使用 [proj-wasm](https://github.com/willcohen/clj-proj) 在 [PROJ](https://proj.org/) 支持的任何 CRS 中显示 MapLibre 地图（PROJ 已转换为 WebAssembly）。 [演示](https://willcohen.github.io/backproj/)
- [maplibre-gl-mask-plugin](https://codeberg.org/mguihal/maplibre-gl-mask-plugin) - 在 MapLibre GL JS 中渲染围绕 geojson 功能的遮罩。 [演示](https://mguihal.codeberg.page/maplibre-gl-mask-plugin)

## 图层类型插件

- [Allmaps Maplibre](https://github.com/allmaps/allmaps/tree/main/packages/maplibre) - 一个用于显示地理参考 [IIIF](https://iiif.io/) 图像的包，通过加载[地理参考注释](https://preview.iiif.io/api/georef/extension/georef/) 并使用 WebGL 转换图像并将其覆盖在正确的地理位置上。
- [mapbox-gl-arcgis-featureserver](https://github.com/rowanwins/mapbox-gl-arcgis-featureserver) - 用于从 ArcGIS FeatureServer 或 MapServer 检索要素的库。该库发出平铺请求，而不是简单地请求每个功能。
- [mapbox-gl-esri-sources](https://github.com/frontiersi/mapbox-gl-esri-sources) - 一个库，可让您更轻松地在 MapLibre GL JS 中使用 Esri 服务。支持 Esri 地图服务（动态和平铺）、Esri 矢量切片服务和 Esri 矢量底图样式。
- [esri-gl](https://github.com/muimsd/esri-gl) - 一个模块，可让您更轻松地在 MapLibre GL JS 中使用 Esri 服务，替代 WebGL 的 esri-leaflet。
- [mapbox-gl-flatgeobuf](https://github.com/rowanwins/mapbox-gl-flatgeobuf) - 一个使用平铺方法从 FlatGeobuf 文件中检索特征的库。与 MapLibre GL JS 和 Mapbox GL JS 兼容。
- [mapbox-gl-ogc-feature-collection](https://github.com/mkeller3/mapbox-gl-ogc-feature-collection) - 一个小包，用于从 OGC 功能 API 端点请求 geojson 以在 MapBox/MapLibre 中提供图块。
- [maplibre-cog-protocol](https://github.com/geomatico/maplibre-cog-protocol) - 用于在 Maplibre GL JS 中加载云优化 GeoTIFF (COG) 的自定义协议。
- [maplibre-gl-lidar](https://github.com/opengeos/maplibre-gl-lidar) - 用于渲染 LIDAR 点云数据的 MapLibre GL JS 插件。
- [maplibre-google-maps](https://github.com/traccar/maplibre-google-maps) - 用于将 Google 地图作为栅格图层集成到 MapLibre GL JS 中的库。它使用新的 Google Map Tiles API。
- [ol-maplibre-layer](https://github.com/geoblocks/ol-maplibre-layer) - 将 MapLibre GL JS 地图渲染为 [OpenLayers](https://openlayers.org/) 图层。
- [PMTiles for MapLibre](https://github.com/protomaps/PMTiles/tree/main/js) - 使用 addProtocol 读取 PMTIles 的库。一种用于托管图块集的单文件格式，无需服务器或 API，只需 S3 或其他存储提供商。
- [@naivemap/maplibre-gl-image-layer](https://www.naivemap.com/map-gl-layers/api/maplibre-gl-image-layer/) - 一个多功能图层，用于在地图上显示具有各种投影（使用 proj4js）的地理参考图像。

## 实用程序库

- [expression-jamsession](https://github.com/mapbox/expression-jamsession/) - 将 [Mapbox Studio 公式](https://www.mapbox.com/help/studio-manual-styles/#use-a-formula) 转换为 [表达式](https://maplibre.org/maplibre-style-spec/expressions/)。
- [mapbox-choropleth](https://github.com/stevage/mapbox-choropleth) - 从 CSV 源和几何源创建分区统计图图层。
- [mapbox-gl-layer-groups](https://github.com/mapbox/mapbox-gl-layer-groups) - 管理图层组。
- [mapbox-gl-sync-move](https://github.com/mapbox/mapbox-gl-sync-move) - 同步多个地图之间的移动。
- [mapbox-gl-utils](https://github.com/stevage/map-gl-utils) - 使用语法糖和便利函数管理图层、源和属性。
- [Styl](https://github.com/navidnabavi/styl) - 一个快速、固定的 linter、验证器和格式化程序，适用于 Mapbox GL 和 MapLibre GL 风格的 JSON 文件，用 Rust 编写
- [map-gl-offline](https://github.com/muimsd/map-gl-offline) - 适用于 MapLibre GL JS 的 TypeScript 兼容 npm 包，可实现矢量/栅格切片的全面离线存储和使用。
- [maplibregl-mapbox-request-transformer](https://github.com/rowanwins/maplibregl-mapbox-request-transformer) - 该库提供了一个请求转换函数，可以在 MapLibreGL 中使用 MapboxGL 样式。
- [maplibregl-theme](https://github.com/lhapaipai/maplibre-theme) - 为您的 MapLibre GL Web 应用程序定制主题。 [主题定制器](https://maplibre-theme.pentatrion.com/)
- [simplespec-to-gl-style](https://github.com/mapbox/simplespec-to-gl-style) - 将具有 [simplestyle-spec](https://github.com/mapbox/simplestyle-spec/) 的 GeoJSON 样式转换为 MapLibre GL 样式。
- [turf](https://turfjs.org/) - 提供先进的地理空间分析工具。
- [Maperture](https://github.com/stamen/maperture) - 用于比较网络地图样式的网络应用程序。
- [geojson-map-fit-mercator](https://github.com/tjdavey/geojson-map-fit-mercator) - 查找最佳方位、缩放和中心点，以在 Mapbox GL 或 MapLibre GL 视口中拟合一组 GeoJSON 要素。 [演示](https://tjdavey.github.io/geojson-map-fit-mercator/#preview)
- [maplibre-legend](https://github.com/mvt-proj/maplibre-legend) - 来自 Rust 开发的 style.json 的图例生成器。 [板条箱](https://crates.io/crates/maplibre-legend)
- [maplibre-gl-video-export](https://github.com/bjperson/maplibre-gl-video-export) - 使用预设动画、路径点和地理约束将地图动画导出到视频（WebM VP9、MP4 H.264）。

## 开发工具插件

- [mapbox-gl-framerate](https://github.com/mapbox/mapbox-gl-framerate) - 用于评估地图渲染性能的帧速率控制。
- [mapbox-gl-fps](https://github.com/MazeMap/mapbox-gl-fps) - 具有统计报告输出的每秒帧数 GUI 控制和测量器。
- [mapgrab](https://mapgrab.github.io/) - 一种使用 Playwright、Cypress 和 Selenium 等流行测试框架创建端到端 (e2e) 地图测试的工具。
- [maplibre-gl-inspect](https://github.com/acalcutt/maplibre-gl-inspect) - 添加检查控件以查看矢量源特征和属性。

<!-- [JAVASCRIPT-PLUGINS]:END -->


## 地图/图块提供商

- 💙 [MapLibre Demotiles](https://github.com/maplibre/demotiles) - 用于演示项目的简单 XYZ MVT 图块集。
- [**亚马逊定位服务**](https://aws.amazon.com/location/)
- [**蔚蓝地图**](https://azure.microsoft.com/en-us/products/azure-maps)
- [Esri](https://developers.arcgis.com/maplibre-gl-js/)
- [Geofabrik](https://www.geofabrik.de/maps/vectortiles.html)
- [Geoapify](https://www.geoapify.com/map-tiles/)
- [HERE](https://www.here.com/docs/bundle/vector-tile-api-developer-guide/page/README.html)
- [**JawgMaps**](https://www.jawg.io/)
- [LatLng](https://www.latlng.work/free-maps-api/) - 与 MapLibre 兼容的 OSM 矢量切片、地图样式和静态地图。
- [Mapbox](https://www.mapbox.com/)
- [MapMetrics GL / MapAtlas](https://mapatlas.eu) - Mapbox GL 样式规范兼容的地图服务，具有内置 MVT 图块、地理编码、路由和搜索。 [GitHub](https://github.com/MapMetrics/mapmetrics-gl)
- [MapTiler](https://www.maptiler.com/)
- [Mercator](https://mercator.blue/) - 网格化地球数据（天气、海洋、空气质量、海拔）作为值编码的 Web 墨卡托图块，以及用于颜色映射栅格、风和水流流线、箭头和等高线的开源 MapLibre SDK。
- [**Mierune**](https://www.mierune.co.jp/?lang=en)
- [OpenFreeMap](https://openfreemap.org/)
- [OSM Americana 社区矢量切片服务器](https://tile.ourmap.us/)
- [Protomaps](https://protomaps.com/)
- [体育场地图](https://stadiamaps.com/)
- [TomTom](https://www.tomtom.com/products/maps/)
- [自由的杜伊勒斯](https://tuiles.enliberte.fr/)
- [追踪地图](https://tracestrack.com/)
- [Versatiles](https://versatiles.org/) - 基于 [shortbread](https://shortbread-tiles.org/) 规范的免费矢量切片提供商

**粗体**：[MapLibre 赞助计划](https://maplibre.org/sponsors/) 的成员

## 平铺服务器

- 💙 [Martin](https://github.com/maplibre/martin) - PostGIS、MBtiles 和 PMtiles 切片服务器，支持切片生成和 mbtiles 工具。
- [Headless Node Renderer](https://github.com/ConservationMetrics/mapgl-tile-renderer) - Headless Node.js MapGL 渲染器，用于生成带有样式化栅格图块的 MBTiles。
- [chiitiler](https://github.com/Kanahiro/chiitiler) - chiitiler - “Tiny MapLibre Server”是 Tileserver GL 的替代品，设计用于在无服务器基础设施上运行。 [演示](https://spatialty-io.github.io/chiitiler-demo/)
- [TileServer GL](https://github.com/maptiler/tileserver-gl) - 来自 MBTiles 档案的矢量切片服务器 + 使用 MapLibre GL 本机创建服务器端栅格。
- [Versatiles](https://versatiles.org/) - [Node](https://github.com/versatiles-org/node-versatiles-server) 和 [Rust](https://github.com/versatiles-org/versatiles-rs) 多功能平铺服务器的实现
- [mvt 服务器](https://github.com/mvt-proj/mvt-rs/tree/main) 使用 Salvo Web 框架，用 Rust 开发的简单且高速的矢量切片服务器（以及更多）。
- [BBOX 服务器](https://github.com/bbox-services/bbox) 用 Rust 编写的 OGC API 兼容（功能、地图、资产、进程、路由）服务器。

## 公用事业

- [MapBlockly](https://mapblockly.github.io/) - MapBlockly 是一种使用 MapLibre 学习和使用 Blockly 构建地图的简单而有趣的方法。
- [MapInventor](https://mapinventor.github.io/) - MapInventor 是构建在 MapBlockly 之上的视觉语言。
- [Ultra](https://overpass-ultra.us/) - 一个基于 Web 的 IDE，用于使用 MapLibre 制作地图，支持各种查询和文件类型，例如 Overpass、ohsome、GeoJSON、KML 等。 [文档](https://overpass-ultra.us/docs)
- [Libre-studio](https://github.com/BleenIT/libre-studio) - Maplibre Martin 基于 Web 的管理层，允许管理地图源、精灵和字体字形，以实现即用型自定义地图。
- [Mapforge](https://mapforge.org) - 具有实时协作和共享功能的开源地图矢量图层编辑器。使用 MapLibre GL JS。
- [tilefeed](https://github.com/muimsd/tilefeed) - PostGIS 矢量切片管道 — 通过 Tippecanoe 生成 MBTiles，并通过 PostgreSQL LISTEN/NOTIFY 进行增量更新。
- [Vector Tile Lab](https://github.com/spider-hand/vector-tile-lab) - 用于调整矢量切片的交互式沙箱。

## 用户

- [Ace](https://bdlucas1.github.io/ace) - 免费的球场高尔夫记分卡应用程序使用 OpenStreetMap 数据提供球场图、距离和海拔。使用 MapLibre GL JS 完全在手机浏览器中运行。
- [Cartes](https://cartes.app) - 基于完全开源堆栈的 Google 地图的法国替代方案
- [Climate Action Navigator](https://climate-action.heigit.org/) - 交互式仪表板，可将高分辨率地理空间数据转化为社区层面的见解，以实现有针对性的城市气候行动。
- [Famxplor](https://famxplor.com/)，家庭度假活动的交互式世界地图，由 MapLibre 和 [Svelte MapLibre](https://github.com/dimfeld/svelte-maplibre) 提供支持
- [Flitsmeister](https://www.flitsmeister.com/) - 适用于 Android 和 iOS 的导航应用程序，提供实时交通信息。使用 MapLibre Native、MapLibre 导航。
- [Gramps Web](https://www.grampsweb.org/) ([代码](https://github.com/gramps-project/gramps-web)) - 用于协作家谱和家族史研究的现代网络应用程序。<br>
具有带有位置图钉、时间过滤器和历史地图叠加的交互式矢量地图。<br>
出于性能原因，从 Leaflet 迁移到 [v25.7.0 版本](https://github.com/gramps-project/gramps-web/releases/tag/v25.7.0) 中的 MapLibre GL JS。
- [Herb Atlas](https://herbatlas.fyi) ([Code](https://github.com/tinykite/herb-atlas)) - 合作项目绘制药草农场地图，重点关注可持续+再生实践。
- [Hory.app](https://hory.app) - 用于记录山峰访问的 Web/iOS/Android 应用程序，由全球 350,000 多座山脉的数据库提供支持。使用 MapLibre GL JS 进行在线和离线地图。
- [以色列徒步地图](https://israelhiking.osm.org.il) 有以色列的地图、路线规划和旅游信息。
- [Kibana](https://github.com/elastic/kibana#kibana)，一个基于浏览器的 Elasticsearch 分析和搜索仪表板已迁移到 [MapLibre](https://github.com/elastic/kibana/issues/108742)
- [Kurviger](https://kurviger.com/) - 适用于 Android 和 iOS 的摩托车路线规划和导航应用程序。使用 MapLibre Native、MapLibre 导航。
- [Mapeak](https://mapeak.com) - 一款全球导航应用程序，通过将图像上传到 wikimedia 并将数据上传到 OSM 来支持开放数据。它拥有已知最快的地图更新，离线地图每天更新一次，在线地图每天更新 3 次。它具有规划功能、搜索功能以及享受户外活动所需的一切！
- [MapLibre Storytelling](https://github.com/digidem/maplibre-storymap) - 使用 MapLibre GL JS 的讲故事模板，可以作为静态 HTML 或使用 Node.js 托管。
- [Mappi Studio](https://mappi.studio) - 在线地图动画创作者。在浏览器中创建电影旅行路线、飞越动画和 4K 地图视频。
- [Mountaya](https://mountaya.com) - 交互式 3D 地图可帮助您了解、探索山中并确保安全。
- [Namazue Console](https://github.com/Hybirdss/namazue-console) - 日本范围内的地震情报控制台，具有地震烈度建模、基础设施影响评估和实时 P/S 波传播功能。使用 MapLibre GL JS 5 + Deck.gl 9 构建。 [演示](https://namazue.dev)
- [On The Go Map](https://onthegomap.com) - 规划跑步和骑行路线的网站。迁移到 MapLibre
- [Pharos AI](https://conflicts.app) - 开源实时情报仪表板，用于通过基于 MapLibre 的交互式地理空间可视化跟踪地缘政治冲突。 ([源代码](https://github.com/Juliusolsson05/pharos-ai))
- [Pumperly](https://pumperly.com) ([代码](https://github.com/GeiserX/pumperly)) - 覆盖 36 个国家的开源燃油价格比较和电动汽车充电路线规划器。具有路线规划、车站聚类和价格色标等功能。可自行托管，GPL-3.0。
- 新西兰权威且开放的数字[底图服务](https://github.com/linz/basemaps)为LINZ和公众使用[MapLibre](https://github.com/linz/basemaps/pull/1689)
- [OpenHistoricalMap](https://www.openhistoricalmap.org/) - 详细绘制世界历史地图的合作项目，由 MapLibre 和 maplibre-gl-leaflet 提供支持
- [OpenStreetMap Americana Style](https://github.com/osm-americana/openstreetmap-americana#openstreetmap-americana-style) - 典型的美国地图风格，由 [MapLibre](https://github.com/osm-americana/openstreetmap-americana#technology-stack) 提供支持
- [Paddling Spots](https://paddlingspots.com) - 共享划桨地点、查找出租地点以及探索地图上位置的平台。使用 MapLibre 和 ngx-maplibre-gl。
- [Peripleo](https://github.com/britishlibrary/peripleo) - 可重复使用的网络地图界面，具有可配置的标记、过滤器、搜索等。开源并在 GH 页面上运行，您只需要一个电子表格。
- [Queering the Map](https://www.queeringthemap.com) ([代码](https://github.com/radical-data/queering-the-map)) - 一个众包平台，用于在全球地图上匿名固定酷儿体验。
- [SharpMap](https://sharpmap.app/info)，由 MapLibre 提供支持的超精确 2D 和 3D 地形山地地图。
- [StreetComplete](https://streetcomplete.app) - 易于使用的移动 OpenStreetMap 编辑器，用于现场绘图
- [TatraMap.eu](https://tatramap.eu/#/teren-3d)，由 MapLibre 提供支持的塔特拉山脉 3D 地图。
- [Android 版维基百科应用程序](https://github.com/wikimedia/apps-android-wikipedia) 用于显示带有坐标的文章。
- [TravelerMap.net](http://travelermap.net)，一个可以探索国家公园的网站
- [Utopia Map](https://github.com/utopia-os/utopia-map) - 基于地图的协作应用程序，用于分散协调和现实生活中的网络。<br>
它使用 MapLibre GL JS 构建，使社区能够创建具有交互式图层的自定义地图实例，以管理成员、活动和资源。
- [Vremenar Weather](https://vremenar.tano.si)，一个跨平台应用程序，用于在地图上显示天气状况和预报。使用 MapLibre Native。
- [Wynd's](https://wynds.com.au/) - 澳大利亚的房地产研究网站，提供使用 MapLibre JS 构建的洪水风险、丛林火灾风险和学区地图。

## 演示/示例

- [Expo MapLibre native + web demo](https://github.com/Jaza/expo-maplibre-native-plus-web-demo) - 演示 Expo 应用程序使用 [maplibre-react-native](https://github.com/maplibre/maplibre-react-native) 作为本机，并回退到 [react-map-gl](https://github.com/visgl/react-map-gl) 和 [maplibre-gl-js](https://github.com/maplibre/maplibre-gl-js) 作为 Web。
