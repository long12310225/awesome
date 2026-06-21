<!--lint disable double-link-->
# 很棒的 SNMP [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![Awesome lint](https://github.com/eozer/awesome-snmp/actions/workflows/awesome-lint.yml/badge.svg)](https://github.com/eozer/awesome-snmp/actions/workflows/awesome-lint.yml)

[简单网络管理协议 (SNMP)](https://en.wikipedia.org/wiki/Simple_Network_Management_Protocol) 是一种 Internet 标准协议，用于收集和组织有关 IP 网络上托管设备的信息以及修改该信息以更改设备行为。

这是一个精选的 SNMP 库、工具和其他资源列表。欢迎贡献！

## 内容
- [Libraries](#libraries)
  - [C/C++](#cc)
  - [C#](#c)
  - [Erlang](#erlang)
  - [Go](#go)
  - [Java](#java)
  - [JavaScript](#javascript)
  - [Lua](#lua)
  - [PHP](#php)
  - [Python](#python)
  - [Ruby](#ruby)
  - [Rust](#rust)
- [Tools](#tools)
  - [CLIs](#clis)
  - [GUIs](#guis)
- [Publications](#publications)
  - [Books](#books)
  - [RFCs](#rfcs)
  - [Tutorials](#tutorials)
- [公共服务器](#public-servers)
- [MIB 存储库](#mib-repositories)
- [Miscellaneous](#miscellaneous)

## 图书馆
_有助于编写 SNMP 应用程序。_

### C/C++
- [net-snmp](http://www.net-snmp.org/) - 用于使用和部署 SNMP 协议（v1、v2c 和 v3 以及 AgentX 子代理协议）的一套软件。还包含 Python 绑定。
- [SNMP++](https://www.agentpp.com/api/cpp/snmp_pp.html) - BSD 已获得 HP 许可的 SNMP 实施。支持 SNMP v1/2c/v3、线程安全等等。
- [AGENT++](https://www.agentpp.com/api/cpp/agent_pp.html) - AGENT++ C++框架为SNMP代理的开发提供了完整的三语言SNMP v1/2c/3协议引擎和调度程序。阿帕奇许可。
- [AgentX++](https://www.agentpp.com/api/cpp/agentx_pp.html) - AgentX++ C++ 框架提供了完整的 AgentX 协议 (RFC 2741) 实现，为 AGENT++ 添加了 AgentX 主代理和子代理支持（“商业”）。
- [openSNMP](https://sourceforge.net/projects/opensnmp/) - BSD 许可的 SNMPv3 多线程实现。

### C#
- [C# SNMP Library](https://github.com/lextudio/sharpsnmplib) - MIT 授权的 .NET SNMP 库，具有广泛的 SNMP 标准支持、最新的 .NET 平台目标以及丰富的管理器/代理示例。
- [SNMP Pro](https://pro.sharpsnmp.com) - 添加企业 MIB 支持的商业扩展。
- [SnmpSharpNet](https://github.com/rqx110/SnmpSharpNet) - 简单网络管理协议 (SNMP) 用 C# (csharp) 编写的 .Net 库。实现协议版本 1、2 和 3。

### 埃尔兰
- [Erlang/OTP SNMP](https://www.erlang.org/doc/apps/snmp/users_guide.html) - SNMP 开发作为 Erlang/开放电信平台开发环境的一个组件包含在内。

### 去
- [gosnmp/gosnmp](https://github.com/gosnmp/gosnmp) - 用 Go 编写的 SNMP 库。它提供了 Get、GetNext、GetBulk、Walk、BulkWalk、Set 和 Traps。它支持 IPv4/IPv6，使用 SNMP v1/v2c/v3。
- [sleepinggenius2/gosmi](https://github.com/sleepinggenius2/gosmi) - Go语言的MIB解析器。
- [posteo/go-agentx](https://github.com/posteo/go-agentx) - 具有 AgentX 协议的纯 Go 实现的库。

### 爪哇
- [SNMP4J](https://www.agentpp.com/api/java/snmp4j.html) - SNMP4J 是一种企业级、免费开源且最先进的 Java™ SNMP v1/2c/v3 实现。
- [SNMP4J-Agent](https://www.agentpp.com/api/java/snmp4jagent.html) - SNMP4J-Agent 是一个位于核心 SNMP4J API 之上的 Java™ API，用于开发 SNMP 代理（命令响应程序）。
- [joeSNMP](https://sourceforge.net/projects/joesnmp/) - joeSNMP 是一个在 LGPL 下发布的开源 Java SNMP 类库。
- [Westhawk's SNMP](https://snmp.westhawk.co.uk/) - 可用于 SNMP v1/v2c/v3 的开源 Java 库。支持陷阱、身份验证和隐私。它提供 MD5 和 SHA1 作为身份验证协议。
- [mibble](https://github.com/cederberg/mibble) - Mibble 是一个用于 Java 的开源 SNMP MIB（或 SMI）解析器库。

### JavaScript
- [node-net-snmp](https://github.com/markabrahams/node-net-snmp) - 简单网络管理协议 (SNMP) 的 JavaScript 实现，实现版本 1、2c 和 3。
- [node-snmp-native](https://github.com/calmh/node-snmp-native) - Node.js 的本机 JavaScript SNMP 库。
- [node-snmpjs](https://github.com/joyent/node-snmpjs) - 该包为 Node.js 中的 SNMP 代理和管理应用程序提供了一个工具包。
- [snmp-node](https://github.com/neias/snmp-node) - Node.js 的本机 JavaScript SNMP 库。

### 卢阿
- [luasnmp](https://github.com/hleuwer/luasnmp) - Lua 绑定到 net-snmp 库。

### PHP
- [php.net/SNMP](https://www.php.net/manual/en/book.snmp.php) - 这是 PHP 的 SNMP 扩展，它是 net-snmp 库的包装器。
- [FreeDSx/SNMP](https://github.com/FreeDSx/SNMP) - 纯 PHP SNMP 库。
- [opensolutions/OSS_SNMP](https://github.com/opensolutions/OSS_SNMP) - 一个 PHP SNMP 库，适合那些讨厌 SNMP、MIB 和 OID 的人！

### 蟒蛇
- [pysnmp](https://github.com/lextudio/pysnmp) - 这是 v1/v2c/v3 SNMP 引擎的纯 Python、开源和免费实现，在 2-clause BSD 许可证下分发。
- 该项目源自[原始存储库](https://github.com/etingof/pysnmp)。
- [pysmi](https://github.com/lextudio/pysmi) - PySMI 是 SNMP SMI MIB 解析器的纯 Python 实现。
- 该项目源自[原始存储库](https://github.com/etingof/pysmi)。
- [gufo_snmp](https://github.com/gufolabs/gufo_snmp) - 加速的 Python SNMP 客户端库支持异步和同步模式。它由一个用于高效 BER 解析器和套接字 IO 的干净 Python API 组成，通过 PyO3 包装器以 Rust 语言实现。似乎处于项目生命周期的早期，但它易于使用且速度极快，尤其是在查询许多设备时。 ![GitHub 最后一次提交](https://img.shields.io/github/last-commit/gufolabs/gufo_snmp)
- [net-snmp Python bindings](http://www.net-snmp.org/wiki/index.php/Python_Bindings) - Net-SNMP 5.4 及更高版本在“python”子目录中包含 Python 绑定，但它们不是默认构建的。 ![GitHub 上次提交](https://img.shields.io/github/last-commit/net-snmp/net-snmp)
- [easysnmp](https://github.com/easysnmp/easysnmp) - [net-snmp Python 绑定](http://www.net-snmp.org/wiki/index.php/Python_Bindings) 的一个分支，尝试为库带来更多 Python 接口。 ![GitHub 最后一次提交](https://img.shields.io/github/last-commit/easysnmp/easysnmp)
- [puresnmp](https://github.com/exhuma/puresnmp) - 纯Python3 SNMPv2库，没有任何依赖。 ![GitHub 最后一次提交](https://img.shields.io/github/last-commit/exhuma/puresnmp)
- [snimpy](https://github.com/vincentbernat/snimpy) - Snimpy 是一个基于 Python 的工具，提供了一个简单的界面来构建 SNMP 查询。 ![GitHub 最后一次提交](https://img.shields.io/github/last-commit/vincentbernat/snimpy)
- [python-netsnmpagent](https://github.com/pief/python-netsnmpagent) - 该包允许用 Python 编写 net-snmp 子代理。 ![GitHub 上次提交](https://img.shields.io/github/last-commit/pief/python-netsnmpagent)
- [hnmp](https://github.com/trehn/hnmp) - HNMP 是一个高级 Python 库，可减轻从支持 SNMP 的设备（例如网络交换机、路由器和打印机）检索和处理数据的痛苦。 ![GitHub 上次提交](https://img.shields.io/github/last-commit/trehn/hnmp)
- [aiosnmp](https://github.com/hh-h/aiosnmp) - Python 包 aiosnmp 是一个与 asyncio 一起使用的异步 SNMP 客户端。仅支持 SNMP v2c。 ![GitHub 最后一次提交](https://img.shields.io/github/last-commit/hh-h/aiosnmp)
- [robotframework-snmplibrary](https://github.com/kontron/robotframework-snmplibrary) - SNMPLibrary 是一个用于测试 SNMP 的 Robot Framework 测试库。 ![GitHub 上次提交](https://img.shields.io/github/last-commit/kontron/robotframework-snmplibrary)
- [Scapy](https://github.com/secdev/scapy) - 数据包操作程序和库。 Scapy 有一个[模块](https://github.com/secdev/scapy/blob/master/scapy/layers/snmp.py)来构建/解析 SNMP 数据包。 ![GitHub 上次提交](https://img.shields.io/github/last-commit/secdev/scapy)

### 红宝石
- [ruby-netsnmp](https://github.com/swisscom/ruby-netsnmp) - ruby 中的 SNMP 库（v1、v2c、v3）。

### 铁锈
- [snmp-parser](https://github.com/rusticata/snmp-parser) - 使用 nom 解析器组合器框架用 Rust 编写的 SNMP 解析器。
- [davedufresne/modern_snmp](https://github.com/davedufresne/modern_snmp) - 现代 SNMP 是 SNMPv3 的纯 Rust 库。该存储库包括 snmp_mp（SNMPv3 消息处理）和 snmp_usm（SNMPv3 基于用户的安全模型 (USM) 的实现）包。
- [Svedrin/sunt](https://github.com/Svedrin/sunt) - 该存储库实现了一个用 Rust 编写的 SNMP 代理。

__[⬆ 回到顶部](#contents)__


## 工具
_您使用这些可以更轻松地使用 SNMP。_

### CLI
- [net-snmp tools](http://www.net-snmp.org/) - 此处列出的应用程序是 net-snmp 的一部分。
  - [encode_keychange](http://www.net-snmp.org/docs/man/encode_keychange.html) - 生成 SNMPv3 的 KeyChange 字符串。
  - [snmptranslate](http://www.net-snmp.org/docs/man/snmptranslate.html) - 在数字和文本形式之间转换 MIB OID 名称。
  - [snmpget](http://www.net-snmp.org/docs/man/snmpget.html) - 使用 SNMP GET 请求与网络实体进行通信。
  - [snmpgetnext](http://www.net-snmp.org/docs/man/snmpgetnext.html) - 使用 SNMP GETNEXT 请求与网络实体进行通信。
  - [snmpbulkget](http://www.net-snmp.org/docs/man/snmpbulkget.html) - 使用 SNMP GETBULK 请求与网络实体进行通信。
  - [snmpwalk](http://www.net-snmp.org/docs/man/snmpwalk.html) - 使用 SNMP GETNEXT 请求检索管理值的子树。
  - [snmpbulkwalk](http://www.net-snmp.org/docs/man/snmpbulkwalk.html) - 使用 SNMP GETBULK 请求检索管理值的子树。
  - [snmpset](http://www.net-snmp.org/docs/man/snmpset.html) - 使用 SNMP SET 请求与网络实体进行通信。
  - [snmptest](http://www.net-snmp.org/docs/man/snmptest.html) - 使用 SNMP 请求与网络实体进行通信。
  - [snmptable](https://net-snmp.sourceforge.io/docs/man/snmptable.html) - 检索 SNMP 表并以表格形式显示。
  - [snmpdelta](https://net-snmp.sourceforge.io/docs/man/snmpdelta.html) - 监控 SNMP 计数器值的增量差异。
  - [snmpusm](http://www.net-snmp.org/docs/man/snmpusm.html) - 操作 SNMPv3 基于用户的安全用户表。
  - [snmpvacm](http://www.net-snmp.org/docs/man/snmpvacm.html) - 操作 SNMPv3 基于视图的访问控制模块配置表。
  - [snmpstatus](https://net-snmp.sourceforge.io/docs/man/snmpstatus.html) - 从网络实体检索一组固定的管理信息。
  - [snmpnetstat](https://net-snmp.sourceforge.io/docs/man/snmpnetstat.html) - 通过 SNMP 显示来自网络实体的网络状态和配置信息。
  - [snmpdf](http://www.net-snmp.org/docs/man/snmpdf.html) - 使用从 SNMP 收集的信息显示磁盘信息，如 unix df 工具。
  - [snmptrap](http://www.net-snmp.org/docs/man/snmptrap.html) - 发送 SNMP TRAP 或 INFORM 通知消息。
  - [snmpinform](http://www.net-snmp.org/docs/man/snmptrap.html) - 发送 INFORM 通知消息。 snmpinform 命令在功能上与 snmptrap -Ci 相同。
  - [snmptrapd](http://www.net-snmp.org/docs/man/snmptrapd.html) - 一个 SNMP 守护进程，用于侦听 SNMP TRAP 或 INFORM 并记录它们或对其采取操作。
  - [traptoemail](https://net-snmp.sourceforge.io/docs/man/traptoemail.html) - 这是一个 snmptrapd 处理程序脚本，用于将 snmp 陷阱转换为电子邮件。
  - [net-snmp-config](https://net-snmp.sourceforge.io/docs/man/net-snmp-config.html) - 返回有关已安装的 net-snmp 库和二进制文件的信息。
  - [snmpconf](https://net-snmp.sourceforge.io/docs/man/snmpconf.html) - 创建和修改 SNMP 配置文件。
  - [fixproc](https://net-snmp.sourceforge.io/docs/man/fixproc.html) - 通过执行指定的操作来修复进程。
  - [snmpd](http://www.net-snmp.org/docs/man/snmpd.html) - 响应给定主机的 SNMP 请求的 SNMP 代理。
  - [mib2c](https://net-snmp.sourceforge.io/docs/man/mib2c.html) - 一个 MIB 转换实用程序，可以将 MIB 结构转换为其他形式，例如 C 代码。
  - [mib2c-update](https://net-snmp.sourceforge.io/docs/man/mib2c-update.html) - 这是一个将自定义代码合并到更新的 mib2c 代码中的脚本。
- [SNMP4JCLT](https://www.agentpp.com/tools/snmp4jclt.html) - 使用 SNMP4J 命令行工具 (CLT) 通过基于 IPv4 或 v6 的 UDP、TCP 或 TLSv1,2 传输（“商业”）将 SNMPv1/v2c/v3 请求和陷阱发送到目标。
- [libsmi tools](https://www.ibr.cs.tu-bs.de/projects/libsmi/) - 基于 libsmi 和与 libsmi 发行版集成的 sh/awk 脚本构建的应用程序。
  - [smilint](https://www.ibr.cs.tu-bs.de/projects/libsmi/smilint.html) - 这用于在某种程度上检查 MIB 或 PIB 模块的语法错误和语义。支持 SMIv1/v2 样式 MIB 模块以及 SPPI PIB 模块。
  - [smidump](https://www.ibr.cs.tu-bs.de/projects/libsmi/smidump.html) - 这是一个 MIB/PIB 编译器。它允许以各种格式转储模块的内容：SMIv1、SMIv2、SMIng、SPPI、导入树、类型定义树、OID 节点树、MOSY 样式和根据 JIDM 规范的 CORBA IDL 定义等。
  - [smidiff](https://www.ibr.cs.tu-bs.de/projects/libsmi/smidiff.html) - 这是一个解析 MIB 模块的两个版本并分析从旧版本到新版本的修改的工具。
  - [smiquery](https://www.ibr.cs.tu-bs.de/projects/libsmi/smiquery.html) - 这是一个 MIB/PIB 查询前端。它可用于从命令行查询单个项目。
  - [smistrip](https://www.ibr.cs.tu-bs.de/projects/libsmi/smistrip.html) - 这是一个简单的 shell/awk 脚本，允许从文档（例如 RFC 或 Internet 草案）中提取 MIB 和 PIB 模块。
- [snmpsim](https://github.com/etingof/snmpsim) - 这是一个纯 Python、开源且免费的 SNMP 代理模拟器实现，在 2 条款 BSD 许可证下分发。
- [snmpfwd](https://github.com/etingof/snmpfwd) - SNMP 代理转发器工具用作具有内置 SNMP 消息路由器的应用程序级代理。 SNMP 代理的典型用例是用作应用程序级防火墙或协议转换器，支持 SNMPv3 访问 SNMPv1/SNMPv2c 实体，反之亦然。
- [snmpclitools](https://github.com/etingof/snmpclitools) - 这是用纯 Python 编写的命令行 SNMP 工具的集合。这些工具模仿了著名的 Net-SNMP 对应工具。它包括 snmpget.py、snmpset.py、snmpwalk.py、snmpbulkwalk.py、snmptrap.py 和 snmptranslate.py，请参阅[此处](https://snmplabs.thola.io/snmpclitools/) 了解更多详细信息。
- [snmpwn](https://github.com/hatlord/snmpwn) - SNMPwn 是一个 SNMPv3 用户枚举器和攻击工具。
- [trapperkeeper](https://github.com/dropbox/trapperkeeper) - 一套用于摄取和显示 SNMP 陷阱的工具。它旨在替代 snmptrapd 并补充现有的状态监控解决方案。
- [SNMP Trap Translator](http://www.snmptt.org/) - SNMPTT（SNMP Trap Translator）是一个用 Perl 编写的 SNMP 陷阱处理程序，与 Net-SNMP / UCD-SNMP snmptrapd 程序 (www.net-snmp.org) 一起使用。
  - [snmptt](http://www.snmptt.org/docs/snmptt.shtml) - SNMPTT（SNMP Trap Translator）是一个用 Perl 编写的 SNMP 陷阱处理程序，与 Net-SNMP / UCD-SNMP snmptrapd 程序 (www.net-snmp.org) 一起使用。 SNMPTT 支持 Linux、Unix 和 Windows。
  - [snmpttconvert](http://www.snmptt.org/docs/snmpttconvert.shtml) - 一些供应商提供了可以使用 HP Openview 实用程序导入到 HP Openview 中的文件。 snmpttconvert 是一个简单的 Perl 脚本，它将这些文件之一转换为 snmptt 使用的格式。
  - [snmpttconvertmib](http://www.snmptt.org/docs/temp/snmpttconvertmib.shtml) - snmpttconvertmib 是一个 Perl 脚本，它将读取 MIB 文件并将 TRAP-TYPE (v1) 或 NOTIFICATION-TYPE (v2) 定义转换为 snmptt 可读的配置文件。
- [prometheus/snmp_exporter](https://github.com/prometheus/snmp_exporter) - 建议使用此导出器以 Prometheus 可以摄取的格式公开 SNMP 数据。
- [trailofbits/onesixtyone](https://github.com/trailofbits/onesixtyone) - 快速 SNMP 扫描器。
- [SECFORCE/SNMP-Brute](https://github.com/SECFORCE/SNMP-Brute) - 快速 SNMP 暴力破解、枚举、CISCO 配置下载程序和密码破解脚本。
- [hatlord/snmpwn](https://github.com/hatlord/snmpwn) - SNMPv3 用户枚举器和攻击工具。
- [zabbix-tools/mib2zabbix](https://github.com/zabbix-tools/mib2zabbix) - 此 Perl 脚本将从 SNMP MIB 文件中的 OID 树生成 XML 格式的 Zabbix v3 模板。
- [OIDrage](https://github.com/patrickscottbest/OIDrage) - 基于任何 snmpwalk 输出的轻量级独立 SNMPd 模拟服务器。轻松扩展以模拟数千台服务器。

### 图形用户界面
- [tkmib](http://www.net-snmp.org/) - 用于 SNMP 的 perl/Tk 交互式图形 MIB 浏览器。
- [agentpp/MIB Designer](https://www.agentpp.com/tools/mibdesigner.html) - 使用 MIB Designer 创建、编辑、管理和探索 SMI 规范（“商业”）。
- [agentpp/MIB Explorer Pro](https://www.agentpp.com/tools/mibexplorer.html) - 使用 MIB Explorer 浏览、配置、测试和调试、监控和发现 SNMPv1/2c/3 实体。
- [sharpsnmp/SNMP Pro](https://www.sharpsnmp.com/) - 一系列现代 SNMP 产品，具有 VS Code 内的跨平台 MIB 设计器/编译器/浏览器、完整的 v1/v2c/v3 覆盖、MIB/SMI v1 和 v2 支持，以及模拟器和 MCP 与 AI 工具的桥接。还包括商业和开源 .NET 库。
- [paessler/snmptester](https://www.paessler.com/tools/snmptester) - 此工具使您能够调试 SNMP 活动，以查找 SNMP 监控配置中的通信和/或数据问题。视窗。
- [ireasoning/MIB Browser](http://ireasoning.com/mibbrowser.shtml) - 该工具允许用户加载标准的、专有的 MIB，甚至一些格式错误的 MIB。它还允许他们发出 SNMP 请求来检索代理的数据，或对代理进行更改。免费供个人使用。
- [ireasoning/SNMP Agent Simulator](http://ireasoning.com/snmpsimulator.shtml) - 免费 SNMP 代理模拟器 基于 Java 的应用程序，可以模拟 SNMPv1/v2c/v3 代理。
- [Visual SNMP](https://github.com/sisraell/VisualSNMP) - Visual SNMP 是一个用于测试对 SNMP 代理的访问的简单工具。目前支持 SNMPGET 和 SNMPWALK，但功能有限。
- [muonics/Online MIB validator](http://www.muonics.com/Tools/smicheck.php) - 基于 MIB Smithy SDK 的免费在线 MIB/PIB 验证器。
- [toni-moreno/snmpcollector](https://github.com/toni-moreno/snmpcollector) - SnmpCollector 是一个功能齐全的通用 SNMP 数据收集器，具有 Web 管理界面开源工具，其主要目标是简化从 snmp 协议支持的任何设备获取数据的配置，并将结果数据发送到 influxdb 后端。
- [Unbrowse SNMP](https://www.unleashnetworks.com/products/unbrowse-snmp.html) - Unbrowse SNMP 是一个工具，可帮助将神秘的 MIB 文件编译成简单的 GUI 视图、检索和设置设备上的 MIB 变量、导入 snmpwalk 转储、接收陷阱、图表计数器等等。
- [TWSNMP FK](https://github.com/twsnmp/twsnmpfk) - 适用于 Windows 和 Mac OS 的超轻量级 SNMP 管理器，具有网络映射、轮询和 AI 分析功能。


__[⬆ 回到顶部](#contents)__


## 刊物
_操作方法、教程、博客文章、文档和书籍。_

### 书籍
- [The Networknomicon, or SNMP Mastery by Abdul Alhazred and Michael W. Lucas](https://mwl.io/nonfiction/networking#networknomicon) - 简单网络管理协议 (SNMP) 使您能够调用古老的标准。 SNMP 暴露了您的网络和服务器的秘密，并且——如果您不小心的话——将它们重新配置为难以形容的噩梦。它将你不完善的大脑暴露在现代计算背后的巨大外星维度中。
- [SNMP Mastery by Michael W. Lucas](https://mwl.io/nonfiction/networking#snmp) - SNMP，简单网络管理协议，四合一缩写？
- [SNMP MIB Handbook by Larry Walsh](https://www.amazon.com/SNMP-MIB-Handbook-Larry-Walsh/dp/0981492207) - SNMP MIB 开发、使用和诊断基本指南。
- [Mauro, D. and Schmidt, K., 2005. Essential SNMP: Help for System and Network Administrators. " O'Reilly Media, Inc.".](https://www.amazon.com/Essential-SNMP-System-Network-Administrators-ebook/dp/B0043EWUZ2) - Essential SNMP 探索了商业和开源软件包，并深入介绍了 OID、MIB、社区字符串和陷阱等元素。本书包含五个新章节和各种更新。
- [Snmp, Snmpv2, Snmpv3, and Rmon 1 and 2 by William Stallings](https://www.amazon.com/Snmp-Snmpv2-Snmpv3-William-Stallings/dp/0201485346) - 为网络管理员、经理和设计人员提供基于 SNMP 的网络和互联网络管理的简明、重点突出且实用的指南。
- [Perkins, D. and McGinnis, E., 1997. Understanding SNMP MIBs (p. 528). Englewood Cliffs: Prentice Hall PTR.](https://www.amazon.com/Understanding-SNMP-MIBs-David-Perkins/dp/0134377087) - 第一个完整、实用的编写 SNMP MIB 的内部指南。

### RFC
- [rfc1098](https://tools.ietf.org/rfc/rfc1098.txt) - 简单网络管理协议（版本 1）。
- [rfc1155](https://tools.ietf.org/rfc/rfc1155.txt) - 管理信息的结构和识别。
- [rfc2578](https://tools.ietf.org/rfc/rfc2578.txt) - 管理信息版本 2 (SMIv2) 的结构。
- [rfc2741](https://tools.ietf.org/rfc/rfc2741.txt) - 代理扩展性 (AgentX) 协议版本 1。
- [rfc2742](https://tools.ietf.org/rfc/rfc2742.txt) - 可扩展 SNMP 代理的托管对象的定义。
- [rfc3410](https://tools.ietf.org/rfc/rfc3410.txt) - 互联网标准管理框架的介绍和适用性声明。
- [rfc3411](https://tools.ietf.org/rfc/rfc3411.txt) - 用于描述简单网络管理协议 (SNMP) 管理框架的体系结构。
- [rfc3412](https://tools.ietf.org/rfc/rfc3412.txt) - 简单网络管理协议 (SNMP) 的消息处理和调度。
- [rfc3413](https://tools.ietf.org/rfc/rfc3413.txt) - 简单网络管理协议 (SNMP) 应用程序。
- [rfc3414](https://tools.ietf.org/rfc/rfc3414.txt) - 第 3 版的基于用户的安全模型 (USM)
简单网络管理协议 (SNMPv3)。
- [rfc3415](https://tools.ietf.org/rfc/rfc3415.txt) - 用于简单网络管理协议 (SNMP) 的基于视图的访问控制模型 (VACM)。
- [rfc3416](https://tools.ietf.org/rfc/rfc3416.txt) - 简单协议操作的版本 2
网络管理协议（SNMP）。
- [rfc3417](https://tools.ietf.org/rfc/rfc3417.txt) - 用于简单网络管理的传输映射
协议（SNMP）。
- [rfc3418](https://www.ietf.org/rfc/rfc3418.txt) - 简单网络管理协议 (SNMP) 的管理信息库 (MIB)。
- [rfc3584](https://tools.ietf.org/rfc/rfc3584.txt) - Internet 标准网络管理框架版本 1、版本 2 和版本 3 共存。
- [rfc3826](https://tools.ietf.org/rfc/rfc3826.txt) - 高级加密标准 (AES) 密码算法
在 SNMP 基于用户的安全模型中。
- [rfc4088](https://tools.ietf.org/rfc/rfc4088.txt) - 简单网络管理协议 (SNMP) 的统一资源标识符 (URI) 方案。
- [rfc5343](https://www.rfc-editor.org/rfc/rfc5343.txt) - 简单网络管理协议 (SNMP) 上下文引擎 ID 发现。
- [rfc5590](https://www.rfc-editor.org/rfc/rfc5590.txt) - 简单网络管理协议 (SNMP) 的传输子系统。
- [rfc5591](https://www.rfc-editor.org/rfc/rfc5591.txt) - 简单网络管理协议 (SNMP) 的传输子系统。
- [rfc5592](https://www.rfc-editor.org/rfc/rfc5592.txt) - 简单网络管理协议 (SNMP) 的安全外壳传输模型。
- [rfc7630](https://www.rfc-editor.org/rfc/rfc7630.txt) - SNMPv3 基于用户的安全模型 (USM) 中的 HMAC-SHA-2 身份验证协议。

### 教程
- [net-snmp tutorials](http://www.net-snmp.org/wiki/index.php/Tutorials) - 此 Wiki 页面包含各种教程，从 SNMP 协议的基础知识到使用 net-snmp 库实现 SNMP 应用程序和代理。

__[⬆ 回到顶部](#contents)__

## 公共服务器
- [snmp.ireasoning.com](http://ireasoning.com/pubtest.php) - 免费公开一个 SNMP 代理用于测试目的。

__[⬆ 回到顶部](#contents)__


## MIB 存储库
- [hsnodgrass/snmp_mib_archive](https://github.com/hsnodgrass/snmp_mib_archive) - 包含 3000 多个独特 SNMP MIB 的存档。
- [kcsinclair/mibs](https://github.com/kcsinclair/mibs) - 用于 SNMP 的 MIBS 的另一个集合。确保克隆存储库以查看 MIB 的完整列表。
- [mibdepot.com](http://www.mibdepot.com) - mibDepot 是向 SNMP 社区提供的免费服务，提供 MIB 字典和业界独特的搜索引擎，其中包含超过 12,000 个 SNMP MIB，代表超过 1,800,000 个 MIB 对象定义。
- [oid-info.com](http://oid-info.com) - 该 OID 存储库收集有关对象标识符 (OID) 的信息，并提供用于显示、更新和搜索此信息的工具。
- [michaelfmcnamara.com](https://blog.michaelfmcnamara.com/mibs/) - Michael McNamara 手工整理的 MIB 列表。
- [snmplink.org/OnLineMIB](http://www.snmplink.org) - 该网站显示了一组带有内置 MIB 查看器的 MIB 的文档。
  - [OnLineMIB/Standards](http://www.snmplink.org/OnLineMIB/Standards/) - 标准：（ATM 论坛、IANA、RFC）- RFC1065-5324。
  - [OnLineMIB/Cisco](http://www.snmplink.org/OnLineMIB/Cisco/) - 思科。
  - [OnLineMIB/Juniper](http://www.snmplink.org/OnLineMIB/Juniper/) - 杜松。
  - [OnLineMIB/Extreme](http://www.snmplink.org/OnLineMIB/Extreme/) - 极端。
  - [OnLineMIB/Brocade](http://www.snmplink.org/OnLineMIB/Brocade/) - 锦缎。
- [oidview.com/mibs](http://www.oidview.com/mibs/detail.html) - 该存储库包含来自不同供应商的 7000 多个独特的 MIB。

__[⬆ 回到顶部](#contents)__


## 杂项
_属于列表中但难以分类的项目。_

- [SNMPLink.org](http://snmplink.org/) - SNMPlink.org 提供有关 SNMP、MIB（管理信息库）、网络管理和网络监控的链接和信息。
- [SNMPTools.net](https://www.snmptools.net/) - SNMPTools.net 提供有关 SNMP 应用程序、工具包、网关、模拟器、MIB 浏览器等的链接和信息。

__[⬆ 回到顶部](#contents)__

## 贡献
请先快速浏览一下[贡献指南](contributing.md)。感谢所有贡献者。

