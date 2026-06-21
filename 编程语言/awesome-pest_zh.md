# 很棒的害虫。优雅的解析器 [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[<img src="https://avatars.githubusercontent.com/u/26044607"align="right"width="100">](https://github.com/pest-parser/pest/)

> 使用或用于 Rust 中的 pest 解析器生成器的资源、项目和工具的精选列表

pest 是一个用 Rust 编写的通用解析器，重点关注可访问性、正确性和性能。它使用解析表达式语法（或 [PEG](https://en.wikipedia.org/wiki/Parsing_expression_grammar)）作为输入，其本质上与正则表达式类似，但提供了解析复杂语言所需的增强表达能力。

欢迎投稿！首先阅读[贡献指南](contributing.md)。

## 内容

- [Resources](#resources)
- [Projects](#projects)
- [Tooling](#tooling)

## 资源

- [Book](https://pest.rs/book) - 开始使用 pest 进行解析的推荐方法是阅读这本官方书籍。
- [docs.rs 上的 API 参考](https://docs.rs/pest)
- [fiddle editor on pest.rs](https://pest.rs/#editor) - 玩转语法并在官方网站上分享它们（并格式化它们！）。
- [Gitter](https://gitter.im/pest-parser/pest)
- [Discord](https://discord.gg/XEGACtWpT2)
- [GitHub 讨论](https://github.com/pest-parser/pest/discussions)

## 项目

以下是一些使用 pest 的示例项目：

- [pest_meta](https://github.com/pest-parser/pest/blob/master/meta/src/grammar.pest) - 害虫本身是使用害虫引导的。
- [AshPaper](https://github.com/shnewto/ashpaper) - 由 William Hicks 构思的 Esopo 语言 AshPaper 的 Rust 解释器。
- [cicada](https://github.com/mitnk/cicada) - 用 Rust 编写的老式类似 bash 的 Unix shell。
- [elastic-rs](https://github.com/cch123/elastic-rs) - 在 Rust 中将 bool 表达式转换为 Elasticsearch DSL。
- [handlebars-rust](https://github.com/sunng87/handlebars-rust) - 带 Handlebars 的 Rust 模板。
- [hexdino](https://github.com/Luz/hexdino) - 一个十六进制编辑器，带有类似 vim 的键绑定，用 Rust 编写。
- [insta](https://github.com/mitsuhiko/insta) - Rust 的快照测试库。
- [jql](https://github.com/yamafaktory/jql) - JSON 查询语言 CLI 工具。
- [json5-rs](https://github.com/callum-oakley/json5-rs) - 一个使用 Serde 的 Rust JSON5 序列化器和反序列化器。
- [mt940](https://github.com/svenstaro/mt940-rs) - Rust 中的 MT940 解析器。
- [py_literal](https://github.com/jturner314/py_literal) - 用于解析/格式化 Python 文本的 Rust 箱。
- [rouler](https://github.com/jarcane/rouler) - 一个易于使用的 Rust 骰子库。
- [RuSh](https://github.com/lwandrebeck/RuSh) - RuSh 的目标是成为一个与 bash 兼容的带有糖果的 shell，用 Rust 编写。
- [rs_pbrt](https://github.com/wahn/rs_pbrt) - Rust 箱，用于实现 PBRT 书（第 3 版）C++ 代码的对应部分。
- [stache](https://github.com/dgraham/stache) - Mustache 模板编译器。
- [tera](https://github.com/Keats/tera) - 基于 Jinja2/Django 的 Rust 模板引擎。
- [ZoKrates](https://github.com/ZoKrates/ZoKrates) - 以太坊上 zkSNARKs 的工具箱。
- [Vector](https://github.com/timberio/vector) - 高性能可观测数据管道。
- [AutoCorrect](https://github.com/huacnlee/autocorrect) - 一个 linter 和格式化程序，可帮助您改进文案写作、纠正 CJK（中文、日文、韩文）之间的空格、单词和标点符号。
- [yaml-peg](https://github.com/aofdev/yaml-peg) - 用 Rust 编写的 YAML 的 PEG 解析器。
- [qubit](https://github.com/abhimanyu003/qubit) - 一个方便的计算器，基于 Rust 和 WebAssembly。
- [caith](https://github.com/Geobert/caith) - 骰子滚筒箱。
- [Melody](https://github.com/yoav-lavi/melody) - Melody 是一种编译为正则表达式的语言，旨在更易于阅读和维护。
- [PTA-Parser](https://github.com/AltaModaTech/pta-parser/) - 用 Rust 构建的纯文本会计解析器，适用于 [Beancount](https://github.com/beancount/beancount)、[Ledger](https://github.com/ledger/ledger) 和其他 PTA 格式。
- [Keadex Mina](https://github.com/keadex/keadex) - 开源、无服务器 IDE，可使用 C4-PlantUML 进行编码并大规模组织 C4 模型图。
- [Liquid Grammar](https://github.com/rust-utilities/liquid-grammar-pest/) - 为 [Shopify](https://shopify.github.io/liquid/) Liquid（散列标签_not- Sponsored_ 或_affiliated_）生成“Pairs”和/或“Rules”以用于消费板条箱
- [ws2markdown](https://code.rosaelefanten.org/ws2markdown) - 将 WordStar 文档转换为 Markdown 文件。
- [TypeQL Rust](https://github.com/typedb/typeql/tree/master/rust) - TypeDB 的查询语言，用 Pest 编写

## 工装

### IDE支持

- [pest IDE tools](https://github.com/pest-parser/pest-ide-tools) - 带有 LSP 服务器和 VSCode 扩展的主存储库。
- [VSCode 扩展](https://marketplace.visualstudio.com/items?itemName=pest.pest-ide-tools)
- [IntelliJ IDEA 插件](https://plugins.jetbrains.com/plugin/12046-pest)
- [pest.vim](https://github.com/pest-parser/pest.vim)
- [pest-fmt](https://github.com/pest-parser/pest-fmt) - 它可以帮助格式化
害虫语法。
- [pest web debugger](https://github.com/tomtau/pest-web-debug) - [在线](https://tomtau.github.io/pest-web-debug/) 尝试一下。

### 样板减少和测试

- [pest-ast](https://github.com/pest-parser/ast) - 将 pest 解析树转换为抽象语法树时，它可以帮助减少样板文件。
- [pest_consume](https://crates.io/crates/pest_consume) - 这个箱子可以帮助解析树遍历样板。
- [pest-test](https://crates.io/crates/pest-test) - 它是一个 pest 语法的测试框架。
- [pest_ascii_tree](https://crates.io/crates/pest_ascii_tree) - 在控制台的树中输出“Pairs”

### CLI调试器

- [pest_debugger](https://docs.rs/pest_debugger/latest/pest_debugger/) - 它是一个用于调试 pest 语法的箱子。它可以用作 CLI 工具或库。 [请参阅使用 CLI 调试器的说明](debugger.md)。
