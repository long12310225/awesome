# 很棒的 CSV [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

**精心策划的 CSV 相关工具和资源列表**

[CSV](https://en.wikipedia.org/wiki/Comma-separated_values) 仍然是遥远过去最具未来感的数据格式。

XML 曾兴起也曾衰落。 JSON 只是昙花一现。 YAML 是一个有毒的圣杯。 **CSV 将比它们更持久。**

当最后一只蟑螂咽下最后一口气时，她的临终行为将是在 CSV 文件中划掉她的死亡日期，供后代使用。


## 内容

- [Tools](#tools)
  - [修复或验证 CSV](#repair-or-validate-csv)
  - [将 CSV 视为 SQL](#treat-csv-as-sql)
  - [与 CSV 相互转换](#convert-to-or-from-csv)
  - [CSV <-> JSON](#csv---json)
- [Essays](#essays)
- [Data](#data)
- [Conferences](#conferences)
- [Standards](#standards)
- [META：其他类似列表](#meta-other-similar-lists)
- [行为准则](#code-of-conduct)
- [Funtribute](#funtribute)
- [Footnotes](#footnotes)



以下是一些处理 CSV 的很棒的工具：

## 工具

- [NimbleText/Live](https://NimbleText.com/Live) - 使用模式来操作 CSV；世界上最简单的代码生成器 *.
- [PapaParse](https://www.papaparse.com) - 强大的浏览器内 CSV 解析器。
- [d3-dsv](https://github.com/d3/d3-dsv) - d3.js 解析器和格式化程序模块，用于分隔符分隔值。
- [CSVKit](https://csvkit.readthedocs.io/) - CSV 实用程序，包括 csvsql / csvgrep / csvstat 等。
- [QSV](https://github.com/dathere/qsv) - 用 Rust 编写的快速 CSV 命令行工具包（xsv 的更新）。
- [sed (gnu tool)](https://www.gnu.org/software/sed/manual/sed.html) - 流编辑器。
- [gawk (gnu tool)](https://www.gnu.org/software/gawk/manual/gawk.html) - 使用 [awk](http://pubs.opengroup.org/onlinepubs/009695399/utilities/awk.html) 进行文本处理和数据提取。
- [awk by example](https://github.com/learnbyexample/Command-line-text-processing/blob/master/gnu_awk.md#default-field-separation) - 使用 awk 的综合示例。
- [Miller](http://johnkerl.org/miller/doc/) - 像 sed / awk / cut / join / sort 等用于名称索引数据（例如 CSV）。
- [ParaText](https://github.com/wiseio/paratext) - CSV 解析速度为每秒 2.5 GB。
- [CSVGet](http://github.com/fizx/csvget/tree/master) - 从网站获取 CSV 格式的结构化数据。
- [CSVfix](https://code.google.com/p/csvfix/) - 用于操作 CSV 数据的工具。
- [Tad](https://www.tadviewer.com) - 快速免费的跨平台 CSV 查看器。
- [csvtodashboard](https://csvtodashboard.com) - 完全在浏览器中转换、清理、查询 (SQL) 和可视化 CSV - 本地优先，无需上传任何内容。
- [Nvd3-tags](http://blog.tryolabs.com/2015/02/27/nvd3-tags-a-tiny-library-for-making-charts-from-csv-data/) - 一个用于从 csv 数据制作图表的小型库。
- [Powershell: Import-CSV](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/import-csv) - 用于处理 CSV 的强大内置工具（[示例](https://gist.github.com/dfinke/786ba9edae1b0265ada10b36a7a11ba9)）。
- [CSV Tools](https://onlinecsvtools.com/) - 有用的 CSV 实用程序的集合。
- [graph-cli](https://github.com/mcastorina/graph-cli) - 灵活的命令行工具可根据 CSV 数据创建图表。
- [CSV to SQL](http://www.convertcsv.com/csv-to-sql.htm) - 用于从 CSV 数据创建插入/更新/删除等的在线工具。
- [C#: kbCSV](https://github.com/kentcb/KBCsv/blob/master/README.md) - 一个高效、易于使用的 .NET CSV 解析和编写库。
- [csvprintf](https://github.com/archiecobbs/csvprintf) - 用于基于 CSV 文件解析和格式化输出的 UNIX 命令行实用程序。
- [Ron 的数据编辑](https://www.ronsplace.eu/Products/RonsDataEdit)（[Ron 的 CSV 编辑器](https://www.ronsplace.eu/products/ronseditor) 的新现代版本） - 处理大文件，做神奇的事情。永恒的编辑器，永恒的格式。
- [Rainbow CSV plugins](https://github.com/mechatroner/rainbow_csv#rainbow-csv-in-other-editors) - 用于 CSV/TSV 语法突出显示的文本编辑器插件集合。适用于 [Vim](https://github.com/mechatroner/rainbow_csv)、[VS Code](https://marketplace.visualstudio.com/items?itemName=mechatroner.rainbow-csv)、[Atom](https://atom.io/packages/rainbow-csv)、[Sublime Text](https://packagecontrol.io/packages/rainbow_csv) 和其他编辑器。
- [ExtendsClass](https://extendsclass.com/csv-diff.html) - 一个简单的 CSV 比较器。
- [Mighty Merge](https://mightymerge.io/) - 加入/联合 csv 文件。
- [Modern CSV](https://www.moderncsv.com/) - 用于编辑 CSV 文件和查看大文件的工具。
- [Data Wrangler](https://github.com/microsoft/vscode-data-wrangler) - Data Wrangler 是一种以代码为中心的数据清理工具，集成到 VS Code 和 VS Code Jupyter Notebooks 中。
- [CSV to SQL](https://monapdx.github.io/Frontend-Widgets/csv-to-sql.html) - 上传 CSV 文件，设置表名称，并立即生成 SQL 插入。
- [SmoothCSV](https://smoothcsv.com) - 适用于 Mac、Windows 和 Linux 的快速、强大且直观的 C​​SV 编辑器。

### 修复或验证 CSV

- [Csvlint.go](https://github.com/Clever/csvlint) - 用于根据 RFC 4180 验证 CSV 文件的命令行工具。
- [csvstudio](http://www.csvstudio.com/) - 一个智能应用程序，用于修复非常大的 CSV 文件中的语法错误。
- [scrubcsv](https://github.com/faradayio/scrubcsv) - 从 CSV 文件中删除不良记录并标准化（需要 Rust）
- [reconcile-csv](https://github.com/OpenRefine/reconcile-csv/blob/master/README.md) - 查找一组相关 CSV 之间的关系

## 生成表架构

- [CSV 架构](https://csv-schema.surge.sh/) &mdash;分析 CSV 文件并生成数据库表架构，全部在浏览器中完成
- 需要：此类别中的更多工具。


### 将 CSV 视为 SQL

- [TextQL](http://dinedal.github.io/textql/) - 针对 CSV 或 TSV 执行 SQL。
- [Datasette Facets](https://simonwillison.net/2018/May/20/datasette-facets/) - 适用于任何 CSV 文件或 SQLite 数据库的分面浏览和 JSON API。
- [q](https://harelba.github.io/q/) - 直接在 CSV 文件上运行 SQL
- [RBQL](https://rbql.org) - Rainbow Query Language，一种带有 JavaScript 或 Python 后端的类似 SQL 的语言。
- [PSKit 查询](https://github.com/dfinke/PSKit#sql-query) &mdash; Powershell 模块可让您对对象运行简单的查询，包括使用 csv 导入

### 与 CSV 相互转换

- [CSV to Table](https://github.com/vividvilla/csvtotable) - 将 CSV 文件转换为可搜索和可排序的 HTML 表格。

### CSV <-> JSON

- [Agnes](http://www.secretgeek.net/agnes/twoWay.html) - 两种方式 Csv 到 Json **。
- [csv2json](https://www.csvjson.com/csv2json) - 用于将 CSV 或 TSV 格式数据转换为 JSON 以及[反之亦然](https://www.csvjson.com/json2csv) 的在线工具。
- [csv-to-json](https://mango-is.com/tools/csv-to-json/) - 简单、隐私友好且离线优先的在线 csv 到 json 转换器。


## 随笔

> 一旦找到完美的数据序列化文件格式，您就不再需要寻找
>
> [大卫·温吉尔](https://twitter.com/davidwengier/status/1159606464220000257)


- [Thinking about CSV](https://blog.datacite.org/thinking-about-csv/) - 马丁·芬纳.
- [In Praise of CSV](https://usopendata.org/2015/03/10/csv) - 沃尔多·贾奎斯.
- [Stop Rolling Your Own CSV Parser!](http://www.secretgeek.net/csv_trouble) - 莱昂·班布里克***。
- [So You Want To Write Your Own CSV code?](http://thomasburette.com/blog/2014/05/25/so-you-want-to-write-your-own-CSV-code/) - 托马斯·布雷特.
- [Falsehoods Programmers Believe About CSVs](https://donatstudios.com/Falsehoods-Programmers-Believe-About-CSVs) - 杰西·多纳特.
- [ASCII Delimited Text - Not CSV or TAB delimited text](https://ronaldduncan.wordpress.com/2009/10/31/text-file-formats-ascii-delimited-text-not-csv-or-tab-delimited-text/) - 罗纳德·邓肯.

## 生成数据

- [Fake Name Generator](https://www.fakenamegenerator.com/order.php) - 使用其他身份数据批量生成假名以进行测试。
- [Mockium](https://softwium.com/mockium/) - 测试 CSV / JSON / SQL / XML 的数据生成器。
- [Mockaroo](https://www.mockaroo.com/) - CSV / JSON / SQL / Excel 的随机数据生成器。


## 数据

- [US Data.gov](https://catalog.data.gov/dataset?res_format=CSV) - 18789+ CSV 数据集。
- [Australian Government Open Data](https://data.gov.au/dataset?res_format=CSV) - 2715+ CSV 数据集。
- [Reference data in csv](https://datahub.io/collections/reference-data) - 易于使用的 CSV 和 JSON 格式的参考数据。
- [awesome-public-datasets](https://github.com/awesomedata/awesome-public-datasets) - 公共领域中以主题为中心的高质量开放数据集列表。
- [United Nations data](https://data.un.org) - 来自联合国的数据

## 会议

- [csv,conf](https://csvconf.com/) - 为世界各地的数据创建者举办的社区会议。


## 标准

> 标准的美妙之处在于有很多标准可供选择。<br />&mdash;（可能）格蕾丝·霍珀。

- [RFC 4180](https://tools.ietf.org/html/rfc4180) ([html 版本](http://www.faqs.org/rfcs/rfc4180.html)) - “*逗号分隔值 (CSV) 文件的通用格式和 MIME 类型*”。
  - [CSV 格式的定义](https://tools.ietf.org/html/rfc4180#section-2)
  - [文本/csv 的 MIME 类型注册](https://tools.ietf.org/html/rfc4180#section-3)
- [W3C：Web 上表格数据和元数据的模型](https://www.w3.org/TR/tabular-data-model/)
- [CSV Schema Language](http://digital-preservation.github.io/csv-schema/csv-schema-1.2.html) - 用于定义和验证 CSV 数据的语言。
- [csv,specs](https://github.com/csvspecs) - 逗号分隔值 (CSV) 格式规范（和测试），包括。 CSV v1.0、CSV v1.1、CSV 严格、CSV <3 数字、CSV<3 JSON、CSV <3 YAML。
- [Tabular Data Resource](http://frictionlessdata.io/specs/tabular-data-resource/) - 专门用于描述 CSV 文件或电子表格等表格数据的[数据资源](http://frictionlessdata.io/specs/data-resource/)
- [CSVY](https://github.com/csvy/csvy.github.io/blob/master/index.md) - 用于向 CSV 文件添加 YAML 标头以描述其格式的标准

## META：其他类似列表

- [structured-text-tools](https://github.com/dbohdan/structured-text-tools) - 用于操作 CSV / XML / HTML / JSON / INI 等的命令行工具列表。
- [META-META](https://raw.githubusercontent.com/secretGeek/AwesomeCSV/master/awesomecsv.csv) - **此列表为 CSV**。
- [META-META-META](https://nimbletext.com/Live/-971009575/) - 一种 NimbleText 模式，从此列表中以 CSV 形式生成此 Markdown 页面。


## 行为准则

请参阅[行为准则](code-of-conduct.md)


## 乐趣贡献

要体验贡献的乐趣，请参阅[Contributing](contributing.md)


## 脚注

`*` <span id='footnote1' ></span> 我是 [NimbleText](https://NimbleText.com/Live) 的作者。当然，我把它放在了清单的第一位。如果我个人没有评价它，我就不会花那么多时间来制作和改进它。

`**` <span id='footnote2' ></span> 我写了 `agnes` 但并不特别认可它供其他人使用（因此没有将源代码迁移到 GitHub）。它很慢并且非流式传输。我会选择“papa-parse”。从好的方面来说，“agnes”比大多数产品拥有更全面的测试套件和更简单的 API。

`***` <span id='footnote3' ></span> 我的也是。

## 许可证

[![CC0](http://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

在法律允许的范围内，[Leon Bambrick](http://secretgeek.net) 已放弃本作品的所有版权以及相关或邻接权。
