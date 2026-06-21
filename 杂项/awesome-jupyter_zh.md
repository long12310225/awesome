# 很棒的 Jupyter [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

精彩的 [Jupyter](http://jupyter.org) 项目、库和资源的精选列表。 Jupyter 是一个开源 Web 应用程序，允许您创建和共享包含实时代码、方程、可视化和叙述文本的文档。

<div align="center" style="border-bottom: 0px;">
	<br>
	<img width="400" src="assets/logo.png" alt="Jupyter logo">
	<br>
	<br>
</div>

---

<div align="center" style="border-bottom: 0px;">
	<sub>Awesome Jupyter is proudly supported by our sponsor:</sub>
	<br>
	<br>
	<a href="https://deepnote.com/?utm_source=github&utm_medium=promo&utm_campaign=awesomejupyter"><img width="300" src="assets/deepnote.jpeg" alt="Deepnote logo"></a>
	<br>
	<br>
	<b>Deepnote is a collaborative data science notebook built for teams.</b>
	<div>
	<sub>Explore data with Python & SQL from your browser. Add context with data visualizations and rich text editing. Share your work by simply sending a link. <a href="https://deepnote.com/?utm_source=github&utm_medium=promo&utm_campaign=awesomejupyter">Check it out on the Deepnote free plan.</a></sub>
	</div>
</div>

---

## 内容

<!--lint ignore awesome-toc alphabetize-lists-->
- [Runtimes/Frontends](#runtimesfrontends)
- [Collaboration/Education](#collaborationeducation)
- [Visualization](#visualization)
- [Tables](#Tables)
- [Rendering/Publishing/Conversion](#renderingpublishingconversion)
- [版本控制](#version-control)
- [JupyterLab 扩展](#jupyterlab-extensions)
- [Testing](#testing)
- [特定领域的项目](#domain-specific-projects)
- [托管笔记本解决方案](#hosted-notebook-solutions)
- [官方资源和文档](#official-resources-and-documentation)
- [社区资源](#community-resources)
- [Articles/Guides/Tutorials](#articlesguidestutorials)
- [Contributing](#contributing)

<!--lint disable no-repeat-item-in-description-->

---

## 运行时/前端

- [Beaker](http://beakerx.com/) - 具有从一种语言到另一种语言的无缝数据传输的开发环境。
- [docker-stacks](https://github.com/jupyter/docker-stacks) - Docker 中可立即运行的 Jupyter 应用程序的分层堆栈。
- [Guild AI](https://my.guild.ai/docs/jupyter-notebook-experiments/) - 将笔记本作为实验来执行，以随着时间的推移捕获和比较结果。
- [Hydrogen](https://github.com/nteract/hydrogen) - 使用 Jupyter 内核在 Atom 中内联运行代码。
- [Jupyter Notebook](https://github.com/jupyter/notebook) - 主要 Jupyter 笔记本运行时。
- [JupyterHub](https://github.com/jupyterhub/jupyterhub) - Jupyter 的多用户服务器。
- [JupyterLab](https://github.com/jupyterlab/jupyterlab) - JupyterLab 是 Jupyter 的下一代用户界面。
- [JupyterLab Desktop](https://github.com/jupyterlab/jupyterlab-desktop) - 基于 Electron 的 JupyterLab 桌面应用程序。
- [JupyterWith](https://github.com/tweag/jupyterWith) - 基于 Nix 的框架，用于定义声明性和可重现的 Jupyter 环境。
- [kaggle/docker-python](https://github.com/kaggle/docker-python) - Kaggle Python Docker 镜像，包含数据集和包。
- [ML Workspace](https://github.com/ml-tooling/ml-workspace) - Docker 镜像，包括 Jupyter(Lab) 和用于数据科学/机器学习的各种包。
- [nteract](https://github.com/nteract/nteract) - 本机桌面笔记本前端。 <!--lint 禁用双链接-->
- [Panel](https://github.com/holoviz/panel) - 笔记本作为静态文件或交互式和独立的服务器/客户端（通过 pyodide）应用程序。
- [PaneLite](https://panelite.holoviz.org) - [JupyterLite](https://jupyterlite.readthedocs.io/en/latest/) 的发行版，可与 [Panel](https://panel.holoviz.org) 和 [HoloViz](https://holoviz.org) 生态系统配合使用。 <!--lint 启用双链接-->
- [Stencila](https://github.com/stencila/stencila) - 本机桌面笔记本前端。
- [Visual Studio Code](https://code.visualstudio.com/docs/python/jupyter-support) - 本机桌面笔记本前端。
- [voila](https://github.com/voila-dashboards/voila) - 笔记本作为交互式独立 Web 应用程序。

## 合作/教育

- [callgraph](https://github.com/osteele/callgraph) - 显示函数调用图的魔法。
- [IllumiDesk](https://github.com/IllumiDesk/illumidesk) - 基于 Docker 的 JupyterHub + LTI + nbgrader 教育发行版。
- [ipygame](https://github.com/Kamuyin/ipygame) - Jupyter 笔记本的 pygame 兼容重新实现。
- [IPythonBlocks](https://github.com/jiffyclub/ipythonblocks) - 在 Jupyter 中使用彩色网格练习 Python。
- [jupyter-drive](https://github.com/jupyter/jupyter-drive) - 适用于 Jupyter 的 Google 云端硬盘。
- [jupyter-edx-grader-xblock](https://github.com/ibleducation/jupyter-edx-grader-xblock) - 自动评分作为 Jupyter 笔记本创建的学生作业，并将分数写入 Open edX 成绩簿中。
- [jupyter-viewer-xblock](https://github.com/ibleducation/jupyter-viewer-xblock) - 在 Open edX XBlock 中获取并显示部分或整个 Jupyter Notebook。
- [jupyterquiz](https://github.com/jmshea/jupyterquiz) - 适用于 Jupyter 笔记本和 Jupyter Book 的交互式测验生成器。
- [LTI Launch JupyterHub Authenticator](https://github.com/jupyterhub/ltiauthenticator) - 通过 Edx 进行身份验证。
- [nbautoeval](https://github.com/parmentelat/nbautoeval) - 创建自动评估练习。
- [nbgitpuller](https://github.com/jupyterhub/nbgitpuller) - 将 Git 存储库单向同步到本地路径。
- [nbgrader](https://github.com/jupyter/nbgrader) - Jupyter 笔记本的分配和评分。
- [nbtutor](https://github.com/lgpage/nbtutor) - 可视化 Python 代码执行（逐行）。

## 可视化

- [Altair](https://github.com/altair-viz/altair) - Python 的声明式可视化库，基于 [Vega](http://vega.github.io/vega) 和 [Vega-Lite](https://github.com/vega/vega-lite)。
- [anywidget](https://anywidget.dev) - 一个 Python 库，可简化自定义 Jupyter 小部件的创建和发布。
- [Bokeh](https://bokeh.pydata.org/en/latest/) - 针对现代 Web 浏览器进行演示的交互式可视化库。
- [bqplot](https://github.com/bloomberg/bqplot) - Jupyter 基于图形的交互式绘图框架的语法。
- [Evidently](https://github.com/evidentlyai/evidently) - 用于在验证或生产监控期间分析机器学习模型的交互式报告。
- [hvplot](https://hvplot.holoviz.org/) - Jupyter 中用于数据探索和可视化的熟悉且高级的 API。
- [ipychart](https://github.com/nicohlr/ipychart) - Jupyter 中的交互式 Chart.js 绘图。
- [ipycytoscape](https://github.com/cytoscape/ipycytoscape) - 使用 cytoscape.js 在 Jupyter 中进行交互式图形可视化的小部件。 <!--lint 禁用双链接-->
- [ipydagred3](https://github.com/timkpaine/ipydagred3) - [ipywidgets](https://github.com/jupyter-widgets/ipywidgets) 库，用于使用 dagre-d3 在 jupyterlab 中绘制有向无环图。  <!--lint 启用双链接-->
- [ipyleaflet](https://github.com/jupyter-widgets/ipyleaflet) - Jupyter 笔记本中 Leaflet.js 地图的交互式可视化库。
- [IPySigma](https://github.com/bsnacks000/IPySigma-Demo) - Jupyter 笔记本的网络可视化前端原型。
- [ipytree](https://github.com/QuantStack/ipytree/) - Jupyter 的树 UI 元素。
- [ipyvizzu](https://github.com/vizzuhq/ipyvizzu) - 动画数据讲故事工具。
- [ipyvolume](https://github.com/maartenbreddels/ipyvolume) - Jupyter 中基于小部件和 WebGL 的 Python 3D 绘图。
- [ipywebrtc](https://github.com/maartenbreddels/ipywebrtc) - Jupyter 中的视频/音频流。 <!--lint 禁用双链接-->
- [ipywidgets](https://github.com/jupyter-widgets/ipywidgets) - Jupyter 的 UI 小部件。  <!--lint 启用双链接-->
- [itk-jupyter-widgets](https://github.com/InsightSoftwareConsortium/itk-jupyter-widgets) - 用于以 2D 和 3D 形式可视化图像的交互式小部件。
- [jp_doodle](https://github.com/AaronWatters/jp_doodle) - 用于构建 2D 和 3D 专用交互式图表的基础设施。
- [jupyter-gmaps](https://github.com/pbugnion/gmaps) - Jupyter 笔记本中 Google 地图的交互式可视化库。
- [jupyter-manim](https://github.com/krassowski/jupyter-manim) - 在 Jupyter 笔记本中显示 [manim](https://github.com/3b1b/manim)（数学动画引擎）视频或 GIF。
- [lux](https://github.com/lux-org/lux) - 每当在笔记本中打印数据框时，推荐一组可视化效果。
- [mpld3](http://mpld3.github.io) - 结合 Matplotlib 和 D3js 进行交互式数据可视化。
- [pd-replicator](https://github.com/scwilkinson/pd-replicator) - 一键将 Pandas DataFrame 复制到剪贴板。
- [Perspective](https://github.com/finos/perspective) - 数据可视化和分析组件，特别是对于大型/流数据集。
- [pyecharts](https://github.com/pyecharts/pyecharts) - [ECharts](https://github.com/apache/incubator-echarts) 可视化库的 Python 接口。
- [pythreejs](https://github.com/jovyan/pythreejs) - Python / ThreeJS 桥利用 Jupyter 小部件基础设施。
- [tqdm](https://github.com/tqdm/tqdm) - 用于循环和迭代的快速、可扩展的进度条。
- [tributary](https://github.com/timkpaine/tributary) - 具有 Jupyter 支持的 Python 数据流。
- [xleaflet](https://github.com/QuantStack/xleaflet) - ipyleaflet 的 C++ 后端。
- [xwebrtc](https://github.com/QuantStack/xwebrtc) - ipywebrtc 的 C++ 后端。
- [xwidgets](https://github.com/QuantStack/xwidgets) - ipywidgets 的 C++ 后端。

## 表格

- [buckaroo](https://github.com/paddymul/buckaroo) - 适用于 Jupyter 和 pandas 的 GUI 数据整理工具。
- [ipyaggrid](https://github.com/widgetti/ipyaggrid) - Jupyter 中 ag-Grid 的强大功能。
- [ipydatagrid](https://github.com/bloomberg/ipydatagrid) - Jupyter 的快速数据网格小部件。
- [ipyregulartable](https://github.com/jpmorganchase/ipyregulartable) - Jupyter 中的高性能、可编辑、可设置样式的数据网格。
- [ipysheet](https://github.com/QuantStack/ipysheet/) - Jupyter 中的交互式电子表格。
- [ITables](https://github.com/mwouts/itables) - Pandas 和 Polars DataFrames 呈现为交互式 [datatables-net](https://datatables.net/) 表。
- [Qgrid](https://github.com/quantopian/qgrid) - 用于在 Jupyter 中排序、过滤和编辑 DataFrame 的交互式网格。

## 渲染/发布/转换

- [Binder](http://mybinder.org) - 将 GitHub 存储库转变为交互式笔记本的集合。
- [Bookbook](https://github.com/takluyver/bookbook) - Bookbook 将目录中的一组笔记本转换为 HTML 或 PDF，保留笔记本内和笔记本之间的交叉引用。
- [ContainDS Dashboards](https://github.com/ideonate/cdsdashboards) - JupyterHub 扩展可在任何框架（Voilà、Streamlit、Plotly Dash 等）中托管经过身份验证的脚本或笔记本。
- [Ganimede](https://github.com/manugraj/ganimede) - 在沙箱中存储、版本、编辑和执行笔记本，并通过 REST 接口直接集成它们。
- [Jupyter Book](https://github.com/executablebooks/jupyter-book) - 利用计算材料构建出版质量的书籍和文档。
- [jupyterlab_nbconvert_nocode](https://github.com/timkpaine/jupyterlab_nbconvert_nocode) - NBConvert 导出器，无需代码单元即可导出 PDF/HTML。
- [Jupytext](https://github.com/mwouts/jupytext) - 使用在版本控制下运行良好的文本格式（例如 Python 或 Markdown 文件）转换和同步笔记本。
- [jut](https://github.com/kracekumar/jut) - CLI 在终端中很好地显示笔记本。
- [Kapitsa](https://github.com/gitjeff05/kapitsa) - 用于搜索本地 Jupyter 笔记本的 CLI。
- [Mercury](https://github.com/mljar/mercury) - 将笔记本转换为 Web 应用程序。
- [nbconvert](https://nbconvert.readthedocs.io) - 将笔记本转换为其他格式。
- [nbdev](https://github.com/fastai/nbdev) - 使用 Jupyter 作为 [Literate Programing](https://en.wikipedia.org/wiki/Literate_programming) 环境来开发、打包 Python 包并将其分发到 PyPI。
- [nbflow](https://github.com/jhamrick/nbflow) - 使用 Jupyter 和 Scons 实现一键式可重现工作流程。
- [nbinteract](https://www.nbinteract.com) - 从 Jupyter 笔记本创建交互式网页。
- [nbscan](https://github.com/conery/nbscan) - 搜索并打印 Jupyter 笔记本的单元格内容。
- [Nikola](https://getnikola.com) - 静态站点生成器，可将笔记本转换为网站。
- [notedown](https://github.com/aaren/notedown/) - 将 Jupyter 笔记本转换为 Markdown（或返回）。
- [Papermill](https://github.com/nteract/papermill) - 用于参数化、执行和分析 Jupyter Notebook 的工具。
- [Ploomber](https://github.com/ploomber/ploomber) - 使用“pipeline.yaml”文件以可重现的方式运行笔记本和脚本的集合。
- [pynb](https://github.com/minodes/pynb) - Jupyter Notebooks 作为带有嵌入 Markdown 文本的纯 Python 代码。
- [RISE](https://github.com/damianavila/RISE) - Reveal.js Jupyter/IPython 幻灯片。
- [rst2ipynb](https://github.com/nthiery/rst-to-ipynb) - 将独立的 reStructuredText 文件转换为 Jupyter 笔记本文件。
- [Voila](https://github.com/QuantStack/voila) - 使用交互式小部件渲染实时 Jupyter Notebook，允许基于 Jupyter Notebook 进行仪表板。

## 版本控制

- [databooks](https://github.com/datarootsio/databooks) - 一个命令行实用程序，可简化笔记本的版本控制和共享。
- [jupyter-nbrequirements](https://github.com/thoth-station/jupyter-nbrequirements/) - Jupyter Notebooks 中的依赖管理和优化。
- [jupyterlab-git](https://github.com/jupyterlab/jupyterlab-git) - Git 集成的扩展。
- [nbdime](https://github.com/jupyter/nbdime) - 用于比较和合并 Jupyter 笔记本的工具。
- [nbQA](https://github.com/nbQA-dev/nbQA) - 从命令行或通过预提交在 Jupyter Notebook 上运行任何标准 Python 代码质量工具。
- [Neptune](https://docs.neptune.ai/integrations-and-supported-tools/ide-and-notebooks/jupyter-lab-and-jupyter-notebook) - 对项目中的笔记本检查点进行版本控制、管理和共享。
- [ReviewNB](https://www.reviewnb.com/) - Jupyter Notebooks 的代码审查。

## JupyterLab 扩展

- [amphi-etl](https://github.com/amphi-ai/amphi-etl) - Jupyterlab 的低代码 ETL 扩展。
- [celltags](https://github.com/jupyterlab/jupyterlab-celltags) - 使用单元标签组织和执行笔记本的扩展。
- [code_formatter](https://github.com/ryantam626/jupyterlab_code_formatter) - 通用代码格式化程序。
- [debugger](https://github.com/jupyterlab/debugger) - 适用于 Jupyter 笔记本、控制台和源文件的可视化调试器。
- [drawio](https://github.com/QuantStack/jupyterlab-drawio) - 显示drawio/mxgraph图表的扩展。
- [elyra](https://github.com/elyra-ai/elyra) - 用于在本地或远程创建和运行笔记本（或 Python 脚本）管道的可视化编辑器。
- [genv](https://github.com/run-ai/jupyterlab_genv) - 用于管理 JupyterLab 中的 GPU 环境的扩展。
- [go-to-definition](https://github.com/krassowski/jupyterlab-go-to-definition) - 用于导航到 JupyterLab 中变量或函数的定义的扩展。
- [google-drive](https://github.com/jupyterlab/jupyterlab-google-drive) - Google Drive 集成扩展。
- [jupyter-ai](https://github.com/jupyterlab/jupyter-ai) - 在 JupyterLab 中作为对话助理与生成式 AI（支持多种模型）合作。
- [jupyter-fs](https://github.com/jpmorganchase/jupyter-fs) - Jupyter 中用于多个后端的类似文件系统的内容管理器。
- [jupyter-notify](https://github.com/ShopRunner/jupyter-notify) - 用于浏览器通知单元格完成的单元格魔法。 <!--lint 禁用双链接-->
- [jupyter-panel-proxy](https://github.com/holoviz/jupyter-panel-proxy) - 自动将笔记本作为 Jupyter 服务器的“/panel”端点上的 [Panel](https://panel.holoviz.org) 数据应用程序提供服务。 <!--lint 启用双链接-->
- [jupyter-stack-trace](https://github.com/teticio/jupyter-stack-trace) - 单击堆栈跟踪以打开相应的文件或进行 Google 搜索。
- [jupyterlab-executor](https://github.com/gavincyi/jupyterlab-executor) - 用于从 Jupyterlab 文件浏览器执行脚本的扩展。 <!--lint 禁用双链接-->
- [jupyterlab-kyso](https://github.com/kyso-io/jupyterlab-extension) - 用于将笔记本从 Jupyterlab 发布到 [Kyso](https://kyso.io) 平台的扩展。 <!--lint 启用双链接-->
- [jupyterlab-notifications](https://github.com/mwakaba2/jupyterlab-notifications) - JupyterLab 的可自定义笔记本单元格完成浏览器通知。
- [jupyterlab-tensorboard-pro](https://github.com/HFAiLab/jupyterlab_tensorboard_pro) - TensorBoard 对 JupyterLab 的支持。
- [jupyterlab_autoversion](https://github.com/timkpaine/jupyterlab_autoversion) - 在 JupyterLab 中自动对笔记本进行版本控制。
- [jupyterlab_commands](https://github.com/timkpaine/jupyterlab_commands) - 将任意 python 命令添加到 JupyterLab 命令面板。
- [jupyterlab_email](https://github.com/timkpaine/jupyterlab_email) - 从 JupyterLab 中通过电子邮件发送笔记本及其内容。
- [jupyterlab_iframe](https://github.com/timkpaine/jupyterlab_iframe) - 在 JupyterLab 中将 HTML 查看为嵌入式 iframe。
- [jupyterlab_miami_nights](https://github.com/timkpaine/jupyterlab_miami_nights) - VS Code 的 SynthWave '84 和 JupyterLab 的 Neon Night 主题的组合。
- [jupyterlab_templates](https://github.com/jpmorganchase/jupyterlab_templates) - JupyterLab 中的笔记本模板。
- [latex](https://github.com/jupyterlab/jupyterlab-latex) - 用于实时编辑 LaTeX 文档的扩展。
- [lineapy](https://github.com/LineaLabs/lineapy) - 用于使用两行代码将杂乱的 Jupyter 笔记本转换为生产就绪管道的扩展。
- [lsp](https://github.com/krassowski/jupyterlab-lsp) - 类似 IDE 的功能（代码导航、悬停建议、linter、诊断、无内核自动完成等）
- [nb_black](https://github.com/dnanhkhoa/nb_black) - 使用 [black](https://github.com/psf/black) 自动格式化 Python 代码的扩展。
- [python-bytecode](https://github.com/jtpio/jupyterlab-python-bytecode) - 在 JupyterLab 中探索 CPython 字节码。
- [quickopen](https://github.com/parente/jupyterlab-quickopen) - 通过键入文件名称的一部分，可以在 JupyterLab 中快速打开文件。
- [shortcutui](https://github.com/jupyterlab/jupyterlab-shortcutui) - 用于管理键盘快捷键的扩展。
- [sidecar](https://github.com/jupyter-widgets/jupyterlab-sidecar) - JupyterLab 的 sidecar 输出小部件。
- [sql](https://github.com/pbugnion/jupyterlab-sql) - JupyterLab 的 SQL GUI。
- [stickyland](https://github.com/xiaohk/stickyland) - 用粘性单元打破笔记本的线性呈现。
- [system-monitor](https://github.com/jtpio/jupyterlab-system-monitor) - 显示系统指标的扩展。
- [tabnine](https://github.com/codota/tabnine-jupyterlab) - Tabnine AI 自动完成器扩展。
- [theme-darcula](https://github.com/telamonian/theme-darcula) - Jupyterlab 的漂亮 Darcula 主题。
- [toc](https://github.com/jupyterlab/jupyterlab-toc) - 提供笔记本目录的扩展。
- [topbar](https://github.com/jtpio/jupyterlab-topbar) - JupyterLab 的顶部栏扩展。
- [variableinspector](https://github.com/lckr/jupyterlab-variableInspector) - 显示变量及其值的变量检查器扩展。
- [vim](https://github.com/jwkvam/jupyterlab-vim) - Vim 笔记本单元格绑定。
- [voyager](https://github.com/altair-viz/jupyterlab_voyager) - 用于在 [Voyager](http://vega.github.io/voyager/) 中查看 CSV 和 JSON 数据的扩展。

## 测试

- [ipytest](https://github.com/chmp/ipytest) - 用于从笔记本内运行单元测试的测试运行器。
- [nbcelltests](https://github.com/jpmorganchase/nbcelltests) - 在 Jupyter 中对笔记本电脑进行逐单元测试。
- [nbval](https://github.com/computationalmodelling/nbval) - 用于验证 Jupyter 笔记本的 Py.test 插件。
- [nosebook](https://github.com/bollwyvl/nosebook) - Nose 插件，用于查找和运行 IPython 笔记本作为鼻子测试。
- [pointblank](https://github.com/posit-dev/pointblank) - 用于数据质量目的的数据框架和数据库表的笔记本友好测试。
- [sphinxcontrib-jupyter](https://github.com/QuantEcon/sphinxcontrib-jupyter) - 用于生成 Jupyter 笔记本的 Sphinx 扩展。
- [treebeard](https://github.com/treebeardtech/treebeard) - 用于测试/调度 Jupyter 笔记本的 GitHub Action。
- [treon](https://github.com/ReviewNB/treon) - 适用于 Jupyter Notebooks 的易于使用的测试框架。

## 特定领域的项目

- [ArcGIS](https://developers.arcgis.com/python/) - 用于处理地图和地理空间数据的库，由 Web GIS 提供支持。
- [GenePattern Notebook](http://genepattern-notebook.org) - 将基因组分析与交互式笔记本集成。
- [GeoNotebook](https://github.com/OpenGeoscience/geonotebook) - 探索性地理空间分析的扩展。
- [Jupylet](https://github.com/nir/jupylet) - 在 Jupyter 笔记本中以交互方式创建 2D 和 3D 游戏、图形、现场音乐和声音。
- [keplergl](https://docs.kepler.gl/docs/keplergl-jupyter) - Jupyter 扩展，用于大规模地理定位数据集的可视化探索。
- [lolviz](https://github.com/parrt/lolviz) - 用于列表列表、列表、字典的数据结构可视化工具。
- [Quantopian Notebooks](https://www.quantopian.com/notebooks/survey) - 基于 Jupyter 的金融研究平台。
- [vpython-jupyter](https://github.com/BruceSherwood/vpython-jupyter) - 在 Jupyter 笔记本中运行的 VPython 3D 引擎。
- [xontrib-jupyter](https://github.com/xonsh/xontrib-jupyter) - 适用于 xonsh 的 Jupyter 内核，xonsh 是一种基于 Python 的跨平台 Unix shell 语言。

## 托管笔记本解决方案

- [Anaconda Enterprise](https://www.anaconda.com/enterprise/) - 多用户协作以及模型、笔记本和仪表板的一键部署。
- [Azure Notebooks](https://notebooks.azure.com) - Jupyter 笔记本在 Microsoft Azure 的云中运行。
- [CoCalc](https://cocalc.com) - 笔记本电脑支持 17 种内核类型、课程管理、LaTeX 文档创作、同步文档编辑以及与 SageMath 计算机代数系统的集成。
- [DataBlogs](https://www.datablogs.co/) - DataBlogs 是一个开源数据新闻平台，可将 Jupyter 笔记本转换为在网络上发布的文章。
- [DataCamp Workspace](https://www.datacamp.com/workspace) - Jupyter 支持的数据科学笔记本具有内置协作和发布功能。
- [Datalore](https://www.jetbrains.com/datalore) - JetBrains 提供的与 Jupyter 兼容的数据科学和分析笔记本解决方案，用于团队协作。
- [Deepnote](https://www.deepnote.com) - 与 Jupyter 兼容的数据科学笔记本，具有实时协作、版本控制和轻松部署的功能。
- [Domino Data Lab](https://www.dominodatalab.com) - 具有集成协作工具、环境管理和计算网格的数据科学平台。
- [Google Cloud AI Platform Notebooks](https://cloud.google.com/ai-platform-notebooks) - 在 Google Cloud Platform 上配置了支持 GPU 的机器学习框架的托管 JupyterLab 笔记本实例。
- [Google Cloud Dataproc Jupyter component](https://cloud.google.com/dataproc/docs/concepts/components/jupyter) - 使用 Google Cloud Dataproc 的 Jupyter 和 JupyterLab for Apache Spark。
- [Google Colaboratory](https://colab.research.google.com) - 基于云的 Jupyter 环境，旨在机器学习教育和研究。  <!--lint 禁用双链接-->
- [Kyso](https://kyso.io) - 用于将 Jupyter Notebook 作为数据博客和 Web 应用程序发布和共享的数据科学平台。  <!--lint 启用双链接-->
- [Mineo.app](https://mineo.app) - 具有 Jupyter 兼容笔记本的数据操作平台，无代码块，并支持创建仪表板。
- [Naas](https://naas.ai) - JupyterLab 环境具有神奇的调度/通知功能和资产/依赖项/秘密管理。
- [Noteable](https://noteable.io/) - Noteable 是一款结合了代码（SQL、Python 和 R）和交互式可视化的协作笔记本。
- [Paperspace Gradient](https://gradient.run/) - 由 Jupyter 支持的数据科学 IDE，具有加速硬件 (GPU) 和 MLOps 功能。
- [PAWS](https://wikitech.wikimedia.org/wiki/PAWS) - Jupyter Notebook 部署是为与 Wikimedia wiki 交互而定制的。
- [Pinggy](https://pinggy.io) - 创建通往 Jupyter 实例的隧道，即使它位于防火墙或 NAT 后面。
- [qBraid Lab](https://docs.qbraid.com/en/latest/lab/getting_started.html) - JupyterLab 部署为量子计算提供精选的软件工具和集成。
- [Saturn Cloud](https://saturncloud.io/) - 将您的数据科学团队迁移到云端，而无需切换工具。

## 官方资源和文档

- [Jupyter 文档](https://docs.jupyter.org/en/latest/index.html)
- [Jupyter kernels](https://github.com/jupyter/jupyter/wiki/Jupyter-kernels) - 可用作 Jupyter 内核的所有编程语言的列表。
- [JupyterLab 文档](http://jupyterlab.readthedocs.io/en/stable/index.html)
- [为 Jupyter 制作内核](https://jupyter-client.readthedocs.io/en/latest/kernels.html)
- [Try Jupyter](https://try.jupyter.org) - 在浏览器中尝试 Jupyter。

## 社区资源

- 会议演讲 - [PyVideo.org](http://pyvideo.org/search.html?q=jupyter)、[JupyterCon](https://www.youtube.com/playlist?list=PL055Epbe6d5aP6Ru42r7hk68GTSaclYgi)
- GitHub - 搜索：[Jupyter](https://github.com/search?type=Repositories&q=jupyter)
- GitHub - 主题：[Jupyter](https://github.com/topics/jupyter)、[jupyter-kernels](https://github.com/topics/jupyter-kernels)、[jupyter-notebook](https://github.com/topics/jupyter-notebook)、[jupyterhub](https://github.com/topics/jupyterhub)、 [jupyterlab](https://github.com/topics/jupyterlab)、[jupyterlab-extension](https://github.com/topics/jupyterlab-extension)
- Gitter - [Jupyter Gitter 聊天室](https://gitter.im/jupyter/jupyter)
- [jupyter-map](https://elc.github.io/jupyter-map/) - 使用 Jupyter 的大学机构地图。
- [kandi Kits Topic](https://kandi.openweaver.com/explore/jupyter) - 发现流行的 Jupyter 库、顶级作者、热门项目工具包、讨论、教程和学习资源。  <!--lint 禁用双链接-->
- 邮件列表 - [Jupyter 常规邮件列表](https://groups.google.com/forum/#!forum/jupyter)、[Jupyter 教育邮件列表](https://groups.google.com/forum/#!forum/jupyter-education) <!--lint 启用双链接-->
- PyPI - [``框架:: Jupyter``](https://pypi.org/search/?&c=Framework+%3A%3A+Jupyter)
是 Jupyter 项目的 PyPI trove 分类器。
- Reddit - Subreddits：[r/IPython](https://www.reddit.com/r/IPython/)、[r/Jupyter/](https://www.reddit.com/r/Jupyter/)
- Stack Overflow - 标签：[Jupyter](https://stackoverflow.com/questions/tagged/jupyter)、[jupyter-notebook](https://stackoverflow.com/questions/tagged/jupyter-notebook)


## 文章/指南/教程

- [Exploratory computing with Python](http://mbakker7.github.io/exploratory_computing_with_python/) - 涵盖科学计算的笔记本集合。
- [How to Grow Neat Software Architecture out of Jupyter Notebooks](https://github.com/guillaume-chevalier/How-to-Grow-Neat-Software-Architecture-out-of-Jupyter-Notebooks) - 有关从笔记本开发简洁软件架构的文章和[视频](https://www.youtube.com/watch?v=K4QN27IKr0g)。
- [在 Google Cloud Dataproc 集群中安装并运行 Jupyter Notebook](https://cloud.google.com/dataproc/docs/tutorials/jupyter-notebook)
- [使用 Bokeh 进行交互式网页绘图](https://github.com/bokeh/bokeh-notebooks)
- [Jupyter 笔记本扩展](http://jupyter-contrib-nbextensions.readthedocs.io)
- [Jupyter 笔记本主题](https://github.com/dunovank/jupyter-themes)
- [Jupyter 提示、技巧和捷径](https://www.dataquest.io/blog/jupyter-notebook-tips-tricks-shortcuts/)
- [JupyterLab - Your Personal Data Science Workbench](https://github.com/markusschanta/talks/tree/master/2018-03%20-%20JupyterLab%20-%20Full%20Stack%20Quants) - 在伦敦 Full Stack Quants 讨论 JupyterLab。
- [使用 Python 进行科学计算的讲座](https://github.com/jrjohansson/scientific-python-lectures)
- [Jupyter 笔记本列表](https://github.com/jupyter/jupyter/wiki/A-gallery-of-interesting-Jupyter-Notebooks)
- [Jupyter 笔记本 II 列表](https://github.com/jupyter-naas/awesome-notebooks)
- [pytudes](https://github.com/norvig/pytudes) - Peter Norvig 的 Jupyter 笔记本列表。
- [ResGuides：使用 Jupyter 进行研究](https://www.gitbook.com/book/dansand/resguides-research-with-jupyter/details)
- [Sharing Jupyter Notebooks from localhost](https://pinggy.io/blog/share_jupyter_notebook_from_localhost/) - 从本地主机共享 Jupyter Notebook。
- [The Littlest JupyterHub](https://the-littlest-jupyterhub.readthedocs.io/en/latest/) - JupyterHub 分发适用于单个服务器上的 1-50 个用户；比零到 JupyterHub 设置更轻量级。
- [Zero to JupyterHub](http://zero-to-jupyterhub.readthedocs.io/en/latest/) - 帮助安装和管理 JupyterHub 的教程。

## 贡献

随时欢迎您的贡献！请先查看[贡献指南](CONTRIBUTING.md)。
