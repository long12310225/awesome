# 很棒的数据可视化
[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome) ![Test](https://github.com/javierluraschi/awesome-dataviz/actions/workflows/main.yaml/badge.svg)


精选的**开源**数据可视化框架、库和软件列表。受到 [awesome-python](https://github.com/vinta/awesome-python) 的启发，最初由 [fasouto](https://github.com/fasouto) 创建。


## 内容
- [很棒的数据可视化](#awesome-dataviz)
	- [JavaScript 工具](#javascript-tools)
		- [图表库](#charting-libraries)
		- [图表的图表库](#charting-libraries-for-graphs)
		- [Maps](#maps)
		- [d3](#d3)
		- [React](#react)
		- [Misc](#misc)
	- [安卓工具](#android-tools)
	- [C++工具](#c-tools)
	- [Go语言工具](#golang-tools)
	- [iOS工具](#ios-tools)
	- [Python工具](#python-tools)
	- [R工具](#r-tools)
	- [红宝石工具](#ruby-tools)
	- [基于标记的工具](#markup-based-tools)
	- [其他工具](#other-tools)
- [Resources](#resources)
	- [Books](#books)
	- [Catalogs](#catalogs)
	- [Podcasts](#podcasts)
	- [推特账户](#twitter-accounts)
 	- [Websites](#websites)
- [Contributing](#contributing)
- [License](#license)

## JavaScript 工具

### 图表库
- [ApexCharts](https://apexcharts.com/) - 现代和交互式 SVG 图表。
- [Chart.js](https://www.chartjs.org/) - 带有canvas标签的图表。
- [Chartist.js](https://gionkunz.github.io/chartist-js/) - 响应式图表具有出色的浏览器兼容性。
- [dc.js](https://github.com/dc-js/dc.js) 是一个多维图表，专为与 crossfilter 一起使用而构建。
- [Dygraphs](https://dygraphs.com/) - 适用于庞大数据集的交互式折线图库。
- [Echarts](https://github.com/ecomfe/echarts) - 高度可定制和交互式图表，适用于大数据集。
- [Epoch](https://github.com/epochjs/epoch) - 非常适合创建实时图表。
- [Google Charts](https://developers.google.com/chart) - 适用于浏览器和移动设备的交互式图表。
- [G2](https://g2plot.antv.vision/en) - 一个基于图形语法的交互式和响应式图表库，由阿里巴巴维护
- [GraphicsJS](http://www.graphicsjs.org) - 基于 SVG/VML 的轻量级 JS 图形库，具有直观的 API。
- [lit-line](https://github.com/apinet/lit-line) - SVG 折线图 Web 组件 - 轻便、快速、交互式且完全响应。
- [MetricsGraphics.js](https://metricsgraphicsjs.org/) - 针对时间序列数据进行了优化。
- [NVD3](https://github.com/novus/nvd3) - 用 d3.js 编写的可重用图表库。
- [Plotly.js](https://github.com/plotly/plotly.js/) - 强大的声明性库，支持 20 种图表类型。
- [反应包装器](https://github.com/hustcc/echarts-for-react)
- [TechanJS](https://techanjs.org/) - 股票和金融图表。
- [TOAST UI Chart](https://github.com/nhnent/tui.chart) - 完整的库，支持旧版浏览器。
- [Vizzu](https://github.com/vizzuhq/vizzu-lib) - 用于动画数据可视化和数据故事的库。

### 图表的图表库
- [Cola.js](https://marvl.infotech.monash.edu/webcola/) - 使用基于约束的优化技术创建图表的工具。适用于 d3 和 svg.js。
- [Cytoscape.js](https://js.cytoscape.org/) - 用于图形绘制的 JavaScript 库由 [Cytoscape](https://www.cytoscape.org) 核心开发人员维护。
- [Sigma.js](https://sigmajs.org/) - 专用于图形绘制的 JavaScript 库。
- [VivaGraph](https://github.com/anvaka/VivaGraphJS) - JavaScript 图形绘制库。
- [G6](https://github.com/antvis/g6) - 由 Javascript 和 Typescript 提供支持的图形可视化库，由阿里巴巴维护
- [diagram.js](https://github.com/bpmn-io/diagram-js) - Javascript 图表库作为 camunda 在线 BPMN 建模器的基础。
- [Uber React Digraph](https://github.com/uber/react-digraph) - 由 UBER 维护的基于 React.js 的有向图库。

### 地图
- [CARTO](https://github.com/CartoDB/cartodb) - CARTO 是一个开源工具，允许在网络上存储和可视化地理空间数据。
- [Cesium](https://github.com/AnalyticalGraphicsInc/cesium) - WebGL 3D 地球仪和地图。
- [Deck.gl](https://deck.gl/) - 用于大型数据集的可视化探索性数据分析的 WebGL 框架。
- [L7](https://github.com/antvis/L7) - 由阿里巴巴维护的基于WebGL的大规模地理空间数据可视化分析框架
- [L7 Plot](https://github.com/antvis/L7Plot) - 地理空间可视化图表库，由阿里巴巴维护
- [DataMaps](https://github.com/markmarkoh/datamaps) - 使用 D3.js 的交互式 SVG 地图。
- [Dipper](https://github.com/antvis/dipper) - 由L7提供支持、由阿里巴巴维护的地图应用开发框架。
- [Leaflet](https://leafletjs.com) - 用于移动设备友好的交互式地图的 JavaScript 库。
- [Mapael](https://github.com/neveldo/jQuery-Mapael) - 基于 raphael.js 的 jQuery 插件，用于显示矢量地图。

### d3
- 参见[真棒D3](https://github.com/wbkd/awesome-d3)

### 反应
- [BizCharts](https://github.com/alibaba/BizCharts) - 基于[G2](https://github.com/antvis/G2)和React的数据可视化库
- [Graphin](https://github.com/antvis/Graphin) - 由 React 和 Typescript 提供支持的图形可视化库（构建在 G6 之上，由阿里巴巴维护。
- [React-vis](https://github.com/uber/react-vis) - 反应组件来构建数据可视化。
- [Recharts](https://github.com/recharts/recharts) - 用于渲染 D3 图表的声明式反应组件。
- [Victory](https://formidable.com/open-source/victory/) - 用于构建交互式数据可视化的可组合组件
- [nivo](https://github.com/plouc/nivo) - 具有同构能力的 React 增压数据可视化组件，[演示](https://nivo.rocks)。
- [React Svg Textures](https://github.com/finnfiddle/react-svg-textures) - Textures.js 移植到 React。完全同构。
- [DevExtreme React Chart](https://devexpress.github.io/devextreme-reactive/react/chart/) - 用于 Bootstrap 和 Material Design 的基于插件的高性能 React 图表。

## 反应本机
- [F2](https://github.com/antvis/F2) - 一个优雅的、交互式的、灵活的移动图表库，由阿里巴巴维护

### 杂项
- [Graphology](https://github.com/graphology/graphology) - 用于 javascript 和 TypeScript 的健壮且多用途的 Graph 对象；充当基础库来为其他图形可视化库提供支持。
- [Piecon](https://github.com/lipka/piecon) - 图标中的饼图。
- [Textures.js](https://riccardoscalco.github.io/textures/) - 用于创建 SVG 图案的库。
- [Timeline.js](https://timeline.knightlab.com/) - 创建交互式时间线。
- [Vega](https://vega.github.io/vega/) - Vega 是一种可视化语法，是一种用于创建、保存和共享交互式可视化设计的声明性格式。
- [Vega-Lite](https://vega.github.io/vega-lite/) - 是交互式图形的高级语法。它提供了简洁的 JSON 语法，用于快速生成可视化以支持分析。
- [Vis.js](https://visjs.org/) - 动态可视化库，包括时间线、网络和图形（2D 和 3D）。

## 安卓工具
- [DecoView](https://github.com/bmarrdev/android-DecoView-charting) - 动画圆轮图表库。
- [MPAndroidChart](https://github.com/PhilJay/MPAndroidChart) - 一个功能强大且易于使用的图表库。
- [WilliamChart](https://github.com/diogobernardino/WilliamChart) - 简单的图表库。

## C++工具
- [LargeVis](https://github.com/lferry007/LargeVis) - [LargeVis 论文](https://arxiv.org/abs/1602.00370) 的实现，用于可视化大规模和高维数据。
- [PlotJuggler](https://github.com/facontidavide/PlotJuggler) - 用于绘制图表的开源 Qt5 应用程序（基于 Qwt）。
- [Visualization Toolkit (VTK)](https://gitlab.kitware.com/vtk/vtk/blob/master/README.md) - 用于 3d 图形、图像处理和可视化的开源库。

## Go语言工具
- [svgo](https://github.com/ajstarks/svgo) - 用于生成 SVG 的 Go 语言库。
- [plot](https://github.com/gonum/plot) - 用于在 Go 中构建和绘制绘图的 API。
- [go-echars](https://github.com/chenjiandongx/go-echarts) - 简单而强大的 Go 数据可视化库。

## iOS工具
- [BEMSimpleLineGraph](https://github.com/Boris-Em/BEMSimpleLineGraph) - 高度可定制和交互式的折线图。
- [Charts](https://github.com/danielgindi/Charts) - MPAndroidChart 的 iOS 端口。您可以使用非常相似的代码为两个平台创建图表。
- [JBChartView](https://github.com/Jawbone/JBChartView) - 折线图和条形图的图表库。
- [PNChart](https://github.com/kevinzhow/PNChart) - Piner 和 CoinsMan 中使用的简单而美观的图表库。

## 机器学习工具
- [TensorWatch](https://github.com/microsoft/tensorwatch) - 用于数据科学和机器学习的调试和可视化工具

## Python工具
- [altair](https://altair-viz.github.io/) - 基于 Vega-Lite 的声明性统计可视化。
- [bokeh](https://bokeh.pydata.org/en/latest/) - Python 的交互式 Web 绘图。
- [Chartify](https://github.com/spotify/chartify) - Bokeh 包装器使数据科学家可以轻松创建图表。
- [diagram](https://github.com/tehmaze/diagram) - 使用 UTF-8 字符的文本模式图
- [ggplot](https://github.com/yhat/ggpy) - 基于 [R's](#r-tools) ggplot2 的绘图系统。
- [glumpy](https://github.com/glumpy/glumpy) - OpenGL 科学可视化库。
- [holoviews](https://holoviews.org/) - 来自注释数据的复杂和声明性可视化。
- [ipychart](https://github.com/nicohlr/ipychart) - Jupyter Notebook 中 Chart.js 的强大功能。
- [mayai](https://docs.enthought.com/mayavi/mayavi/) - Python 中的交互式科学数据可视化和 3D 绘图。
- [matplotlib](https://matplotlib.org/) - 2D 绘图库。
- [missingno](https://github.com/ResidentMario/missingno) - 提供灵活的数据可视化实用工具集，基于 matplotlib，可以快速直观地总结数据集的完整性。
- [plotly](https://plot.ly/python/) - 基于交互式网络的可视化构建在 [plotly.js](https://github.com/plotly/plotly.js) 之上
- [pptk](https://github.com/heremaps/pptk) - 可视化并使用 2D/3D 点云
- [PyQtGraph](https://www.pyqtgraph.org/) - 交互式和实时 2D/3D/图像绘图和科学/工程小部件。
- [PyVista](https://github.com/pyvista/pyvista) - 通过可视化工具包 (VTK) 的简化界面进行 3D 绘图和网格分析
- [seaborn](https://seaborn.pydata.org/) - 一个用于制作有吸引力且信息丰富的统计图形的库。
- [toyplot](https://toyplot.readthedocs.io/en/stable/) - 适用于儿童的 Python 绘图工具包，具有成人的目标。
- [three.py](https://github.com/stemkoski/three.py/) - 基于 PyOpenGL 的易于使用的 3D 库。受到 Three.js 的启发。
- [veusz](https://veusz.github.io/) - Python 多平台 GUI 绘图工具和图形库
- [VisPy](https://vispy.org/) - 基于OpenGL的高性能科学可视化。
- [vtk](https://www.vtk.org/) - 3D 计算机图形、图像处理和可视化，包括 Python 界面。
- [pandas-profiling](https://github.com/pandas-profiling/pandas-profiling) - 生成具有可视化功能的统计分析报告，以进行快速数据分析。
- [pyechars](https://github.com/pyecharts/pyecharts) - Echarts 库的 Python 绑定。

## R工具
- [ggplot2](https://ggplot2.tidyverse.org/) - 基于图形语法的绘图系统。
- [ggvis](https://ggvis.rstudio.com/) - 一个数据可视化包，其语法类似于 ggplot2，可让您创建丰富的交互式图形。
- [lattice](https://lattice.r-forge.r-project.org) - R 的网格图形
- [plotly](https://github.com/ropensci/plotly) - 交互式图表（包括向 ggplot2 输出添加交互性）、图表和简单网络图
- [rbokeh](https://hafen.github.io/rbokeh/) - R 与 Bokeh 的接口。
- [rgl](https://cran.r-project.org/web/packages/rgl/index.html) - 使用 OpenGL 进行 3D 可视化
- [shiny](https://shiny.rstudio.com) - 创建交互式应用程序/可视化的框架
- [visNetwork](https://datastorm-open.github.io/visNetwork/) - 交互式网络可视化

## 红宝石工具
- [Chartkick](https://github.com/ankane/chartkick) - 使用一行 Ruby 创建图表。

## 基于标记的工具
- [mermaidjs](https://mermaidjs.github.io/mermaid-live-editor) - 一种简单的类似 Markdown 的脚本语言，用于通过 javascript 从文本生成图表
- [wavedrom.com](https://wavedrom.com/) - 根据简单的文字描述绘制时序图或波形

## 其他工具
不依赖于特定平台或语言的工具。
- [Charted](https://github.com/mikesall/charted) - 一种图表工具，可从任何数据文件生成自动、可共享的图表。
- [Gephi](https://github.com/gephi/gephi) - 用于可视化和操作大型图形的开源平台
- [Kepler.gl](https://kepler.gl/) - 用于大规模数据集的地理空间分析工具。
- [Mermaid](https://github.com/knsv/mermaid) - 一种用于以与 Markdown 类似的方式从文本生成图表和流程图的工具。
- [RAW](https://rawgraphs.io) - 从 CSV 或 Excel 文件创建 Web 可视化。
- [Spark](https://github.com/holman/spark) - 外壳的迷你图。它有几种[不同语言的实现](https://github.com/holman/spark/wiki/Alternative-Implementations)。
- [Visual-Insights](https://github.com/ObservedObserver/visual-insights) - 数据分析中的自动洞察提取和可视化规范。
- [X6](https://x6.antv.vision/en) - 阿里巴巴维护的图创建库，用于快速构建DAG图、ER图、流程图等应用
- [Graphviz](https://graphviz.org/) - 开源图形可视化命令行工具和库。从输入文本到 SVG、PDF、交互式网络图形浏览器。

# 资源

## 书籍
- [信息设计](https://www.amazon.com/Design-Information-Introduction-Histories-Visualizations/dp/1592538061)，作者：Isabel Meirelles。
- [2014 年最佳美国信息图表](https://www.amazon.com/Best-American-Infographics-2014/dp/0547974515)，作者：Gareth Cook。
- [图形语法](https://www.amazon.com/Grammar-Graphics-Statistics-Computing/dp/0387245448/) 作者：Leland Wilkinson。基本可视化理论。
- [定量信息的视觉显示](https://www.amazon.com/Visual-Display-Quantitative-Information/dp/0961392142)，作者：Edward Tufte。
- [《华尔街日报信息图形指南》](https://www.amazon.com/Street-Journal-Guide-Information-Graphics/dp/0393347281) 作者：Dona M. Wong
- [可视化分析与设计](https://www.amazon.com/Visualization-Analysis-Design-AK-Peters/dp/1466508914)，作者：Tamara Munzner。
- [Web 交互式数据可视化](https://chimera.labs.oreilly.com/books/1230000000345)，作者：Scott Murray。可以在线阅读。专注于D3。
- [数据可视化工具包](https://datavisualizationtoolkit.com)，作者：Barrett Austin Clark。使用 D3、Ruby on Rails、Postgres、PostGIS 和 Leaflet。
- [数据可视化：数据驱动设计手册](https://www.amazon.com/Data-Visualization-Handbook-Driven-Design/dp/1526468921/) 作者：Andy Kirk

## 目录
- [The Data Visualization Catalogue](https://www.datavizcatalogue.com) - 数据可视化方法的集合，各有利弊。
- [数据可视化项目](https://datavizproject.com)
- [R 图形库](https://www.r-graph-gallery.com)
- [从数据到可视化](https://www.data-to-viz.com)
- [Chartopedia](https://www.anychart.com/chartopedia)
- Depict Data Studio 的[交互式图表选择器](https://depictdatastudio.com/charts/)
- 维基百科
  - [数据可视化技术](https://en.wikipedia.org/wiki/Data_visualization#Techniques)
  - [图形方法列表](https://en.wikipedia.org/wiki/List_of_graphical_methods)
  - [图表类型](https://en.wikipedia.org/wiki/Diagram#Gallery_of_diagram_types)
- [绘图类型](https://en.wikipedia.org/wiki/Plot_(graphics)#Types_of_plots)
  - [图表类型](https://en.wikipedia.org/wiki/Chart#Types)

## 播客
- [数据故事](https://datastori.es/)
- [DataFramed](https://www.datacamp.com/community/podcast)
- [今日数据可视化](https://dataviztoday.com/)

## 推特账户
- [阿尔贝托·开罗](https://twitter.com/albertocairo)
- [安德烈·卡什查](https://twitter.com/anvaka)
- [本杰明·维德克尔](https://twitter.com/datavis)
- [扬·扎克](https://twitter.com/zakjan)
- [玛拉·艾弗里克](https://twitter.com/dataandme)
- [马丁·瓦滕伯格](https://twitter.com/wattenberg)
- [迈克·博斯托克](https://twitter.com/mbostock)
- [纳迪·布雷默](https://twitter.com/NadiehBremer)
- [纽约时报图形](https://twitter.com/nytgraphics)
- [Visualizing](https://twitter.com/VisualizingOrg)

## 网站
- [可视化数据](https://dataforvisualization.com/) 博客 - 用软件开发人员眼中的数据讲述故事
- [Ann K. Emery](https://annkemery.com/) 的博客
- [Data Visualization Society](https://www.datavisualizationsociety.com/) - 数据可视化协会是一个致力于培养数据可视化专业人员社区的组织。
- [eagereyes](https://eagereyes.org/)
- [EvergreenData](https://stephanieevergreen.com/)
- [FlowingData](https://flowingdata.com/)
- [信息是美丽的](https://www.informationisbeautiful.net/)
- [Junk Charts](https://junkcharts.typepad.com/) - Kaiser Fung 剖析了为什么某些数据可视化有效/无效
- [Lisa Rost 思考并讨论为什么我们要进行数据可视化](https://lisacharlotterost.github.io/)
- [Makeover Monday](https://www.makeovermonday.co.uk/) 博客 - Twitter 上的 [#MakeoverMonday](https://twitter.com/search?q=%23makeovermonday)
- [The Open News](https://source.opennews.org/articles/) 博客 - Open news 不时有一些与数据可视化相关的好文章
- [布丁](https://pudding.cool/)
- [真与美运营](https://truth-and-beauty.net/)
- [华盛顿大学交互式数据实验室论文](https://idl.cs.washington.edu/papers)
- [vis4.net](https://www.vis4.net/blog/) - Gregor Aisch 对可视化和数据新闻的随机思考


# 贡献

- 请先检查是否有重复项。
- 保持描述简短、简单且公正。
- 请对每项建议做出单独承诺
- 如果需要，添加新类别。

感谢您的建议！


# 贡献者

- Fabio Souto 最初创建了此存储库，请通过 [fabiosouto.me](https://fabiosouto.me/) 与 Fabio 联系。
- [Javier Luraschi](https://github.com/javierluraschi) 是当前维护者，他在 [Hal9](https://hal9.com) 构建预测可视化。


- - -

如果您对此固执己见的列表有任何疑问，请随时在 Twitter 上联系我 [@javierluraschi](https://twitter.com/javierluraschi) 或[打开 GitHub 问题](https://github.com/javierluraschi/awesome-dataviz/issues/new)。
