# 很棒的 JVM [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

精选的 JVM 底层、性能和非框架相关内容的列表。

- [很棒的 JVM](#awesome-jvm)
    - [Bytecode](#bytecode)
    - [垃圾收集者](#garbage-collectors)
    - [加载工具](#load-tools)
    - [Languages](#languages)
    - [机器学习](#machine-learning)
    - [内存和并发](#memory-and-concurrency)
    - [Metaprogramming](#metaprogramming)
    - [Native](#native)
    - [Network](#network)
    - [尼克斯工具](#nix-tools)
    - [Profilers](#profilers)
    - [Runtimes](#runtimes)
    - [虚拟机](#virtual-machines)
- [Resources](#resources)
    - [Communities](#communities)    
    - [Documentation](#documentation)
    - [Media](#media)
    - [People](#people)
- [Contributing](#contributing)


## 字节码

*字节码操作和分析工具。*

* [asmtools](https://wiki.openjdk.java.net/display/CodeTools/asmtools) - 用于开发用于生成 Java .class 文件的工具。
* [Byte Buddy](http://bytebuddy.net) - 代码生成库在运行时创建 Java 类，无需编译器的帮助。
* [Jitescript](https://github.com/qmx/jitescript) - 类似于BiteScript的字节码生成库。

## 垃圾收集者

*JVM 的垃圾收集器。*

* [Azul Pauseless Garbage Collection](https://www.azul.com/files/wp_pgc_zing_v52.pdf) - 为 Java 应用程序提供连续、无暂停的操作。
* [Balanced GC](http://www.ibm.com/developerworks/websphere/techjournal/1108_sciampacone/1108_sciampacone.html) - IBM WebSphere Application Server V8 的 Java 虚拟机中提供了 GC 策略。
* [Epsilon GC](http://openjdk.java.net/jeps/318) - 完全被动的 GC 实现，具有有限的分配限制，并尽可能降低运行时性能开销。
* [G1](http://www.oracle.com/technetwork/java/javase/tech/g1-intro-jsp-135488.html) - 垃圾优先的垃圾收集器。
* [Shenandoah](http://openjdk.java.net/jeps/189) - 超低暂停时间垃圾收集器。
* [The Garbage Collection Handbook](http://gchandbook.org) - 本书解决了硬件和软件的最新进步给垃圾收集带来的新挑战。
* [ZGC](http://mail.openjdk.java.net/pipermail/announce/2017-October/000237.html) - 针对低延迟和超大堆进行优化的垃圾收集器。

## 加载工具

*生成负载并准确测量系统而无协调遗漏的工具*

* [Gatling](http://gatling.io) - 用于测试 HTTP 服务器的异步非阻塞场景驱动负载测试工具。
* [wrk2](https://github.com/giltene/wrk2) - wrk 的恒定吞吐量、正确延迟记录变体。

## 语言

*在 JVM 上运行的语言。*
* [Ceylon](http://ceylon-lang.org/) - 由红帽创建的面向对象、强大的静态编程语言，强调不变性。
* [Clojure](http://clojure.org/) - 由 Rich Hickey 创建的 Lisp 方言。动态类型，强调函数式编程。
* [Erjang](http://www.erjang.org) - 基于 JVM 的 Erlang VM。
* [Eta](http://eta-lang.org/) - JVM 上的纯、惰性、强类型函数式编程语言。
* [Frege](https://github.com/Frege/frege) - 秉承 Haskell 精神的纯函数式编程语言。
* [gojava](https://github.com/sridharv/gojava) - Go 包的 Java 绑定。
* [Golo](http://golo-lang.org/) - 一种简单的动态语言，广泛使用“invokedynamic”。
* [Groovy](http://www.groovy-lang.org/) - 可选类型和动态语言，具有静态类型和静态编译功能。
* [Java](http://www.oracle.com/technetwork/java/javase/overview/index.html) - 通用、并发、强类型、基于类的面向对象语言。
* [JRuby](http://jruby.org) - Ruby 语言在 JVM 上的实现。
* [JPHP](https://github.com/jphp-group/jphp) - Java 虚拟机上的 PHP。
* [Jython](http://www.jython.org) - 用于 Java 平台的 Python。
* [Kawa](http://www.gnu.org/software/kawa/) - Schema 语言的扩展，属于 Lisp 编程语言家族。
* [Kotlin](http://kotlinlang.org/) - 适用于 JVM、Android 和浏览器的静态类型编程语言。
* [LuaJ](http://www.luaj.org/luaj/3.0/README.html) - 以 Java 为中心的 lua vm 实现，旨在利用标准 Java 功能。
* [Nashorn](http://openjdk.java.net/projects/nashorn/) - 具有本机 JVM 的 Java 轻量级高性能 JavaScript 运行时。
* [OCaml-Java](http://www.ocamljava.org/) - 支持 OCaml 语言 v4。生成纯 Java 字节码并与 Java 无缝集成。
* [Rembulan](https://github.com/mjanicek/rembulan) - Rembulan 是 Lua 5.3 的 JVM 实现，用纯 Java 编写，依赖性最小。
* [Renjin](http://www.renjin.org/) - 基于 JVM 的 R 语言解释器，用于统计分析
* [Scala](http://www.scala-lang.org/) - 强大的静态编程语言，结合了面向对象和函数式编程思想。
* [Xtend](http://www.eclipse.org/xtend/) - 灵活且富有表现力的 Java 方言，可编译为 Java 5 源代码。

## 机器学习
* [Deeplearning4j](https://deeplearning4j.org/) - 适用于 JVM 的开源分布式深度学习库。
* [H2O](https://www.h2o.ai/) - 快速统计、机器学习和数学运行时间。
* [Smile](https://github.com/haifengl/smile) - 统计机器智能和学习引擎。

## 内存和并发

*用于高效内存布局和并发访问的工具和数据结构。*

* [Agera](https://github.com/google/agera) - Google 的 Android 响应式编程。
* [Agrona](https://github.com/real-logic/Agrona) - 构建高性能应用程序时常见的数据结构和实用方法库。
* [Apache Arrow](http://arrow.apache.org/) - 用于柱状内存分析的高性能跨系统数据层。
* [bloofi](https://github.com/lemire/bloofi) - 多维布隆过滤器的Java实现
* [Cap’n Proto](https://capnproto.org/) - 极其快速的数据交换格式和基于功能的 RPC 系统。
* [caffeine](https://github.com/ben-manes/caffeine) - Java 8 的高性能缓存库。
* [Chronicle-Bytes](https://github.com/OpenHFT/Chronicle-Bytes) - 低级内存访问包装器。
* [Chronicle-Queue](https://github.com/OpenHFT/Chronicle-Queue) - 将所有内容存储到磁盘的微秒消息传递。
* [Chronicle-Map](https://github.com/OpenHFT/Chronicle-Map) - 内存中键值存储专为低延迟和/或多进程应用程序而设计。
* [clj-ds](https://github.com/krukow/clj-ds) - Clojure 的数据结构经过修改，可在 Clojure 之外使用。
* [colfer](https://github.com/pascaldekloe/colfer) - 二进制序列化格式和类生成器。
* [commons-math](http://commons.apache.org/proper/commons-math) - 轻量级、独立的数学和统计组件库。
* [CuckooFilter4J](https://github.com/MGunlogson/CuckooFilter4J) - 用于近似集合成员资格查询的布隆过滤器替换。
* [cyclops](https://github.com/aol/cyclops) - RxJava、Reactor、FunctionalJava、Guava 和 Javaslang 的集成模块。
* [Eclipse Collections](https://github.com/eclipse/eclipse-collections) - Java 的集合框架。
* [externalsortinginjava](https://github.com/lemire/externalsortinginjava) - 使用多核和外部存储器算法对非常大的文件进行排序。
* [failsafe](https://github.com/jhalterman/failsafe) - 用于处理故障的轻量级、零依赖库。
* [fasttuple](https://github.com/boundary/fasttuple) - 在堆内和堆外内存中相邻布置的集合。
* [fast-uuid](https://github.com/jchambers/fast-uuid) - 用于快速有效地解析和编写 UUID 的 Java 库。
* [FlatBuffers](http://google.github.io/flatbuffers/) - 适用于 C++、C#、Go、Java、JavaScript、PHP 和 Python 的高效跨平台序列化库。
* [geohash](https://github.com/davidmoten/geo) - 用于地理哈希的 Java 实用方法。
* [gs-collections](https://github.com/goldmansachs/gs-collections) - 高盛集合框架。
* [hollow](https://github.com/Netflix/hollow) - 用于利用小型到中等大小的内存数据集的 Java 库和综合工具集。
* [high-scale-lib](https://github.com/boundary/high-scale-lib) - Cliff Click 的大规模图书馆。
* [hppc](https://github.com/carrotsearch/hppc) - 高性能原始集合。
* [injector](https://github.com/belliottsmith/injector) - Java 的新执行器。
* [java-concurrent-hash-trie-map](https://github.com/romix/java-concurrent-hash-trie-map) - 来自 Scala 集合的并发 trie 哈希映射实现的 Java 端口。
* [java-hll](https://github.com/aggregateknowledge/java-hll) - HyperLogLog 算法的 Java 库。
* [JavaFastPFOR](https://github.com/lemire/JavaFastPFOR) - 非常快速地压缩和解压缩整数数组的库。
* [java-string-similarity](https://github.com/tdebatty/java-string-similarity) - 字符串相似度和距离度量，包括 Levenshtein 编辑距离和兄弟姐妹、Jaro-Winkler、最长公共子序列、余弦相似度等。
* [JCTools](http://jctools.github.io/JCTools/) - JDK 目前缺少并发数据结构。
* [DSL-JSON](http://github.com/ngs-doo/dsl-json) - 具有高级编译时数据绑定的高性能 JSON 库。
* [jsoniter](http://jsoniter.com/) - 声称是有史以来最快的 JSON 解析器（DSL-JSON 的副本）。
* [jOOL](https://github.com/jOOQ/jOOL) - Java 8 lambda 的有用扩展。
* [Koloboke](https://github.com/OpenHFT/Koloboke) - Java 集合直到内存和性能的最后一个面包屑。
* [LevelDB](https://github.com/dain/leveldb) - 用Java重写（移植）LevelDB。
* [lightweight_trie](https://github.com/bryanduxbury/lightweight_trie) - 一种非常节省内存的 trie（基数树）实现。
* [lmdbjni](https://github.com/deephacks/lmdbjni) - Java API 到 LMDB (HawtJNI)，这是一种用 C 编写的超快速、超紧凑的键值嵌入式数据存储。
* [lmdbjava](https://github.com/lmdbjava/lmdbjava) - Java API 到 LMDB (JNR)，这是一种用 C 编写的超快速、超紧凑的键值嵌入式数据存储。
* [low-gc-membuffers](https://github.com/cowtowncoder/low-gc-membuffers) - 内存中的循环缓冲区使用直接 ByteBuffer 来最大限度地减少 GC 开销。
* [lwjgl3](https://github.com/LWJGL/lwjgl3) - Java 库，支持跨平台访问流行的本机 API，可用于图形 (OpenGL)、音频 (OpenAL) 和并行计算 (OpenCL) 应用程序的开发。
* [MapDB](http://www.mapdb.org) - 由堆外或磁盘存储支持的集合。
* [mph-table](https://github.com/indeedeng/mph-table) - 最小完美哈希表是一种不可变的键/值存储，具有高效的空间利用率和快速的读取速度。
* [mug](https://google.github.io/mug/) - 一个小型的、零深度的函数 util 库，源自 Google。
* [netty-buffers](http://netty.io/wiki/using-as-a-generic-library.html#wiki-h2-1) - 内存缓冲池实现类似于jemalloc。
* [ObjectLayout](http://objectlayout.org) - 布局优化的 Java 数据结构包。
* [ohc](https://github.com/snazy/ohc) - 为 Apache Cassandra 3.0 开发的 Java 大型堆外缓存。
* [okio](https://github.com/square/okio) - 现代 Java IO 库可以巧妙地节省 CPU 和内存。
* [onyx-java](https://github.com/onyx-platform/onyx-java) - 通过为 Onyx 工作流程的每个组件提供 Java 等效项来镜像 Onyx 平台核心 API。
* [parquet](https://parquet.apache.org/) - 使用 Dremel 论文中描述的记录粉碎和组装算法的列式存储格式。
* [PauselessHashMap](https://github.com/giltene/PauselessHashMap) - 一个与 java.util.HashMap 兼容的映射，在调整大小时不会停止放置或获取。
* [pcollections](https://github.com/hrldcpr/pcollections) - 持久 Java 集合库。
* [protobuf](https://developers.google.com/protocol-buffers) - Google 的数据交换格式。
* [Quasar](http://www.paralleluniverse.co/quasar/) - JVM 的轻量级线程和参与者。
* [rtree](https://github.com/davidmoten/rtree) - 使用响应式 API 在 Java 中实现不可变的内存中 R 树和 R* 树。
* [RTree2D](https://github.com/Sizmek/rtree2d) - RTree2D 是一种 2D 不可变 R 树，具有 STR（排序平铺递归）包装，用于平面和球面上的超快速最近和相交查询。
* [Reactive Streams](http://www.reactive-streams.org/) - 具有非阻塞背压的异步流处理标准。
* [Reactive Streams Utilities](https://github.com/lightbend/reactive-streams-utils) - 反应流的未来标准实用程序库。
* [RoaringBitmap](https://github.com/RoaringBitmap/RoaringBitmap) - Java 中更好的压缩位集。
* [rollinghashjava](https://github.com/lemire/rollinghashjava) - Java 中的滚动哈希函数。
* [Reactor](http://projectreactor.io/) - Java、Groovy、Clojure 等 JVM 上的反应式数据应用程序。
* [RxJava](https://github.com/ReactiveX/RxJava) - 使用可观察序列编写异步和基于事件的程序的库。
* [SmoothieMap](https://github.com/OpenHFT/SmoothieMap) - java.util.Map impl 的最差放置延迟比 java.util.HashMap 小 100 倍以上。
* [Simple Binary Encoding](https://github.com/real-logic/simple-binary-encoding) - 高性能消息编解码器。
* [splitmap](https://github.com/richardstartin/splitmap/) - 并行位图实现。
* [DataSketches](https://datasketches.github.io/) - 随机流算法的 Java 软件库。
* [stormpot](https://github.com/chrisvest/stormpot) - JVM 的快速对象池。
* [stream-lib](https://github.com/addthis/stream-lib) - 一个 Java 库，用于汇总无法存储所有事件的流中的数据。
* [streamvbyte](https://github.com/lemire/streamvbyte) - 使用 StreamVByte 编解码器在 C 中进行快速整数压缩。
* [TraneIO](http://trane.io/) - Future 抽象的高性能实现。
* [transducers-java](https://github.com/cognitect-labs/transducers-java) - 可组合的算法转换独立于其输入和输出源的上下文。
* [VarInt](https://github.com/bazelbuild/bazel/blob/master/src/main/java/com/google/devtools/build/lib/util/VarInt.java) - 无 deps 变量 int 实现，无需 deps（由 Bazel 提供）。
* [vavr](http://www.vavr.io/) - Java 8+ 的函数库。
* [wire](https://github.com/square/wire) - 适用于 Android 和 Java 的干净、轻量级协议缓冲区。
* [Zero-Allocation-Hashing](https://github.com/OpenHFT/Zero-Allocation-Hashing) - 对 Java 中的任何字节序列进行哈希处理，包括各种原始数组、缓冲区、CharSequences 等。

## 元编程

*针对 JVM 的解析器、解释器、编译器和源代码生成。*

* [Antlr](http://www.antlr.org/) - 用于读取、处理、执行或翻译结构化文本或二进制文件的解析器生成器。
* [auto](https://github.com/google/auto) - Java 源代码生成器的集合。
* [Apache Calcite](http://calcite.apache.org/docs/) - 动态数据管理框架和 SQL 解析器插件。
* [Checker Framework](http://types.cs.washington.edu/checker-framework/) - 查找错误或验证错误是否存在的编译器插件。
* [compile-testing](https://github.com/google/compile-testing) - javac 和注释处理器的测试工具。
* [derive4j](https://github.com/derive4j/derive4j) - 代数数据类型构造器、模式匹配、态射、光学和类型类。
* [error-prone](https://github.com/google/error-prone) - 将常见的 Java 错误捕获为编译时错误。
* [GHCVM](https://github.com/rahulmutt/ghcvm) - 支持 GHC Haskell 的 Haskell 到 JVM 编译器。
* [Graal](http://openjdk.java.net/projects/graal/) - 新的实验性 Java 即时编译器与 HotSpot 虚拟机集成。
* [grappa](https://github.com/fge/grappa) - Parboiled 的 Java 分支。编写没有预处理阶段的语法。
* [immutables](http://immutables.github.io/) - 生成简单、安全且一致的值对象。
* [javacc](https://javacc.java.net/) - 用于 Java 的解析器生成器。
* [javaparser](https://github.com/javaparser/javaparser) - Java 1.8 解析器和 Java 抽象语法树。
* [JavaPoet](https://github.com/square/javapoet) - 用于生成 .java 源文件的 Java API。
* [jparsec](https://github.com/jparsec/jparsec) - 使用纯 Java 和 Haskell Parsec 构建迷你解析器。
* [JSweet](http://www.jsweet.org/) - 从 Java 到 TypeScript/JavaScript 的转译器。
* [MPS](https://www.jetbrains.com/mps/) - 设计和构建可扩展的 DSL 和编辑器。
* [lombok](https://projectlombok.org/) - 减少通常为 Java 类编写的样板代码量。
* [parboiled](https://github.com/sirthias/parboiled) - 基于解析表达式语法的任意输入文本的解析。
* [Sulong](https://github.com/graalvm/sulong) - 使用 Truffle 和 Graal 用 Ja​​va 编写的 LLVM IR 解释器。
* [TeaVM](https://github.com/konsoletyper/teavm) - 提前将编译器（transpiler）从 Java 字节码翻译为 JavaScript。
* [Truffle](https://github.com/graalvm/truffle) - 将语言实现为简单解释器的框架。
* [Xtext](https://eclipse.org/Xtext/) - 编程语言和 DSL 的开发框架。

## 本地人

*互连 JVM 和本机代码*

* [hawtjni](https://github.com/fusesource/hawtjni) - 基于 Eclipse SWT 中使用的 JNI 生成器的 JNI 代码生成器。
* [Java Grinder](https://github.com/mikeakohn/java_grinder) - 将 Java 字节码编译为微控制器程序集。
* [j2v8](https://github.com/eclipsesource/j2v8) - 适用于 Google V8 JavaScript 引擎的 Java API。
* [JavaCPP](https://github.com/bytedeco/javacpp) - JavaCPP 提供了对 Java 内部本机 C++ 的高效访问。
* [jnr-ffi](https://github.com/jnr/jnr-ffi) - 无需手动编写 JNI 代码即可加载本机库。
* [jssembly](https://github.com/dvx/jssembly) - 从 Java 执行本机程序集。
* [NuProcess](https://github.com/brettwooldridge/NuProcess) - Java 的低开销、非阻塞 I/O、外部 Process 执行实现。
* [Project Panama](http://openjdk.java.net/projects/panama/) - 丰富了 JVM 和 C 程序员使用的 API 之间的连接。

## 网络

*用于网络编程、数据包捕获、监控、测试和弹性的工具。*

* [Aeron](https://github.com/real-logic/Aeron) - 高效可靠的 UDP 单播、UDP 组播和 IPC 消息传输。
* [armeria](https://github.com/line/armeria) - 基于 Java 8、Netty 4.1、HTTP/2 和 Thrift 构建的异步 RPC/API 客户端/服务器库。
* [Chronicle-Network](https://github.com/OpenHFT/Chronicle-Network) - 高性能网络库。
* [comcast](https://github.com/tylertreat/comcast) - 模拟糟糕的网络连接。
* [gor](https://github.com/buger/gor) - HTTP 流量实时重播。
* [gRPC](http://www.grpc.io/) - 一个高性能、开源、通用的 RPC 框架，将移动和 HTTP/2 放在首位。
* [jRT](https://github.com/LatencyUtils/jRT) - 测量 java 应用程序对基于套接字的请求的响应时间。
* [JXIO](https://github.com/accelio/JXIO) - Java API over AccelIO（C 库），一个针对硬件加速优化的高性能异步可靠消息传递和 RPC 库。
* [K3PO](https://github.com/k3po/k3po) - 创建任意网络流量和行为以验证网络端点是否行为正确。
* [muxy](https://github.com/mefellows/muxy) - 模拟现实世界的分布式系统故障。
* [Netty](http://netty.io/) - 用于高性能协议服务器和客户端的异步事件驱动网络库。
* [okhttp](https://github.com/square/okhttp) - 适用于 Android 和 Java 应用程序的 HTTP+HTTP/2 客户端。
* [one-nio](https://github.com/odnoklassniki/one-nio) - 用于构建高性能 Java 服务器的库。
* [proteus-java](https://github.com/netifi-proteus/proteus-java) - 基于RSocket的Proteus Java客户端。
* [reactive-grpc](https://github.com/salesforce/reactive-grpc) - Reactive gRPC 是一套将 gRPC 与 Reactive Streams 编程库结合使用的库。
* [RSocket](http://rsocket.io/) - RSocket 是一种二进制协议，用于字节流传输，例如 TCP、WebSockets 和 Aeron。
* [SimianArmy](https://github.com/Netflix/SimianArmy) - 弹性工具可帮助确保您的应用程序能够容忍随机实例故障。
* [pcap4j](https://github.com/kaitoy/pcap4j) - 用于使用 libpcap 捕获、制作和发送数据包的 Java 库。
* [pig](https://github.com/rafael-santiago/pig) - 一个 Linux 数据包制作工具。
* [tcpdump](http://www.tcpdump.org/) - 用于捕获网络流量的数据包分析器。
* [tcpflow](https://github.com/simsong/tcpflow) - 捕获TCP连接流，方便协议分析和调试。
* [tcpreplay](https://github.com/appneta/tcpreplay) - Pcap 编辑和重放工具。

## 尼克斯工具

*在分析 JVM 以及与主机环境交互时有用的 *nix 工具*
* [atoptool](http://www.atoptool.nl/) - 记录系统和流程活动以进行长期分析，突出显示过载的系统。
* [bcc](https://github.com/iovisor/bcc) - 用于基于 BPF 的 Linux IO 分析、网络、监控等的工具。
* [Flame Graphs](http://www.brendangregg.com/flamegraphs.html) - 分析软件的可视化，可以快速准确地识别最常见的代码路径。
* [ioping](https://github.com/koct9i/ioping) - 简单的磁盘 I/0 延迟测量工具。
* [javap](http://docs.oracle.com/javase/8/docs/technotes/tools/unix/javap.html) - 将类文件反汇编为反映 java 字节码的代码。
* [jhat](http://docs.oracle.com/javase/8/docs/technotes/tools/unix/jhat.html) - Java堆分析工具
* [jhsdb](https://docs.oracle.com/javase/9/tools/jhsdb.htm) - 启动事后调试器来分析崩溃的 JVM 的核心转储内容。
* [jinfo](http://docs.oracle.com/javase/8/docs/technotes/tools/unix/jinfo.html) - 打印给定进程的配置信息。
* [jstack](http://docs.oracle.com/javase/8/docs/technotes/tools/unix/jstack.html) - 打印给定 Java 进程的线程堆栈跟踪。
* [jstat](https://docs.oracle.com/javase/8/docs/technotes/tools/unix/jstat.html) - 监视 JVM 中的 GC 和编译器统计信息。
* [hwloc](http://linux.die.net/man/7/hwloc) - 报告处理器的结构、核心数量、超线程和缓存大小。
* [likwid](https://github.com/RRZE-HPC/likwid) - 读取 Intel 和 AMD 处理器上的硬件性能计数器。
* [numactl](http://linux.die.net/man/8/numactl) - 控制进程或共享内存的 NUMA 策略。
* [oprofile](http://oprofile.sourceforge.net/news/) - 通过易于使用的界面以较低的开销进行系统范围的硬件性能监控。
* [perf](https://perf.wiki.kernel.org/index.php/Main_Page) - 使用性能计数器进行 Linux 分析。
* [perf-tools](https://github.com/brendangregg/perf-tools) - 基于Linux perf_events（又名perf）和ftrace的性能分析工具。
* [sysdig](http://www.sysdig.org/) - 从正在运行的 Linux 实例捕获系统状态和活动，然后保存、过滤和分析。
* [sysstat](http://sebastien.godard.pagesperso-orange.fr) - Linux 的性能监控工具。
* [taskset/process-affinity](https://www.glennklockwood.com/hpc-howtos/process-affinity.html) - 检索或设置进程的 CPU 关联性。
* [tiptop](http://tiptop.gforge.inria.fr/) - 与顶部类似，但还显示每个周期的指令 (IPC)。

## 分析器

*提供分析和跟踪信息以帮助程序优化的工具*

* [allocation-instrumenter](https://github.com/google/allocation-instrumenter) - 将字节码重写到工具分配站点的 Java 代理。
* [aprof](https://github.com/Devexperts/aprof) - Java 内存分配分析器。
* [async-profiler](https://github.com/jvm-profiling-tools/async-profiler) - 适用于 Java 的采样 CPU 分析器，具有 AsyncGetCallTrace + perf_events。
* [BTrace](https://github.com/jbachorik/btrace) - 用于 Java 平台的安全、动态跟踪工具。
* [Byteman](http://byteman.jboss.org/) - Java 的跟踪、监控和测试工具
* [bytestacks](https://github.com/cl4es/bytestacks) - 将 JVM 字节码执行转换为火焰图。
* [Chronon](http://chrononsystems.com) - 记录你的整个java程序。在任何机器上重播。
* [GCeasy](http://gceasy.io/) - 机器学习引导的垃圾收集日志分析工具。自动检测 JVM GC 日志中的问题并推荐解决方案。
* [GCViewer](https://github.com/chewiebug/GCViewer) - GCViewer 是一个可视化详细 GC 输出的工具。
* [grav](https://github.com/epickrram/grav) - 帮助可视化流程执行的工具集合。
* [hawkshaw](https://github.com/jClarity/hawkshaw) - 用于跟踪内存/JVM 问题并生成尽可能可预测的 VM 行为的工具。
* [HdrHistogram](http://hdrhistogram.github.io/HdrHistogram/) - 支持记录和分析采样数据值计数的直方图。
* [hdrhistogram-metrics-reservoir](https://bitbucket.org/marshallpierce/hdrhistogram-metrics-reservoir) - 由 HdrHistogram 支持的 Metrics Reservoir 实现。
* [HdrLogProcessing](https://github.com/nitsanw/HdrLogProcessing) - 用于 HDR 直方图日志操作的实用程序。
* [heapster](https://github.com/mariusae/heapster) - JVM 的生产堆分析。
* [honest-profiler](https://github.com/RichardWarburton/honest-profiler) - 没有安全点样本偏差的 JVM 分析器采样。
* [jamm](https://github.com/jbellis/jamm) - 测量实际对象内存使用情况，包括 JVM 开销。
* [Java Flight Recorder (JFR)](http://www.oracle.com/technetwork/java/javaseproducts/mission-control/java-mission-control-1998576.html) - 用于收集有关正在运行的 Java 应用程序的诊断和分析数据的工具，几乎没有性能开销。
* [java-sizeof](https://github.com/dweiss/java-sizeof) - Java 的内存消耗估算器。
* [jcstress](http://openjdk.java.net/projects/code-tools/jcstress/) - 实验利用和测试有助于研究 JVM、类库和硬件中并发支持的正确性。
* [jfr-flame-graph](https://github.com/chrishantha/jfr-flame-graph) - 将 JFR 方法分析示例转换为 FlameGraph 兼容格式。
* [jfr-report-tool](https://github.com/lhotari/jfr-report-tool) - 用于从 Java Flight Recorder 转储创建报告的工具。
* [jitwatch](https://github.com/AdoptOpenJDK/jitwatch) - Java HotSpot JIT 编译器的日志分析器/可视化器。
* [jitwatch-intellij](https://github.com/yole/jitwatch-intellij) - IntelliJ IDEA 的 JITWatch 插件。
* [jHiccup](http://www.azul.com/jhiccup/) - jHiccup 是一个开源工具，旨在测量与应用程序底层 Java 运行时平台相关的暂停和停顿。
* [jmh](http://openjdk.java.net/projects/code-tools/jmh/) - 用 Java 和其他针对 JVM 的语言编写的微基准测试。
* [jmh-compare-gui](https://github.com/akarnokd/jmh-compare-gui) - 用于比较 JMH 结果的 GUI。
* [JOL](http://openjdk.java.net/projects/code-tools/jol/) - 分析 JVM 中的实际对象布局方案、占用空间和引用。
* [JProfiler](https://www.ej-technologies.com/products/jprofiler/overview.html) - 帮助解决性能瓶颈、确定内存泄漏并了解线程问题。
* [JVMTI](https://docs.oracle.com/javase/8/docs/technotes/guides/jvmti/) - 提供本机 API 来检查状态并控制 JVM 中运行的应用程序的执行。
* [jvmtop](https://github.com/patric-r/jvmtop) - 轻量级控制台应用程序，以类似 top 的方式监视机器上正在运行的 jvm。
* [jvm-profiler](https://github.com/uber-common/jvm-profiler) - Java 代理以分布式方式收集 Hadoop/Spark JVM 进程的各种指标和堆栈跟踪。
* [MAT](https://eclipse.org/mat/) - Java 堆分析器有助于查找内存泄漏并减少内存消耗。
* [leakcanary](https://github.com/square/leakcanary) - 适用于 Android 和 Java 的内存泄漏检测库。
* [metrics](http://metrics.dropwizard.io/) - 测量生产环境中关键组件的行为。
* [micrometer](https://github.com/micrometer-metrics/micrometer) - 最流行的监控工具的应用程序指标外观。
* [osquery](https://osquery.io/) - osquery 是一个工具框架，它将操作系统公开为高性能关系数据库。
* [Overseer](http://www.peternier.com/projects/overseer/overseer.php) - Java 的低级硬件监控和管理。
* [OpenTracing](http://opentracing.io/) - 供应商中立的分布式跟踪开放标准。
* [perf-map-agent](https://github.com/jrudolph/perf-map-agent) - 生成方法映射以与 Linux“perf”工具一起使用。
* [perfj](https://github.com/coderplay/perfj) - Java 程序的 Linux 性能。
* [polarbear](https://github.com/Cue/polarbear) - 帮助诊断 OutOfMemoryError 情况的工具。
* [Riemann JVM Profiler](https://github.com/riemann/riemann-jvm-profiler) - JVM 代理，将功能级探查器遥测数据发送到 Riemann 服务器以进行分析、可视化和存储。
* [statsd-jvm-profiler](https://github.com/etsy/statsd-jvm-profiler) - 将分析数据发送到 StatsD 的 JVM 代理分析器。
* [Swiss Java Knife](https://github.com/aragozin/jvm-tools) - 用于 JVM 故障排除、监控和分析的一小组工具。
* [Takipi](https://www.takipi.com/) - 告诉您代码在生产中出现故障的时间和原因。
* [Tracer](https://github.com/zalando/tracer) - 管理自定义跟踪标识符并通过分布式系统携带它们。
* [YourKit](https://www.yourkit.com/) - 功能齐全、易于使用、低开销的分析器。
* [Zipkin](https://github.com/openzipkin/zipkin) - 分布式跟踪系统收集 Twitter 开发的不同服务的计时数据。


## 运行时

*管理jvm运行时进程的工具*
* [Capsule](https://github.com/puniverse/capsule) - JVM 应用程序的打包和部署极其简单。
* [CRaSH](http://www.crashub.org/) - Java 平台的 shell。
* [Drip](https://github.com/ninjudd/drip) - 快速 JVM 启动，无需持久 JVM 的麻烦。
* [HotswapAgent](https://github.com/HotswapProjects/HotswapAgent) - 在运行时重新定义类并跳过重新部署过程。
* [jvmkill](https://github.com/airlift/jvmkill) - 当 JVM 无法分配内存或创建线程时，强制终止 JVM 的代理。
* [Nailgun](http://martiansoftware.com/nailgun/) - Nailgun 是一个客户端、协议和服务器，用于从命令行运行 Java 程序，而不会产生 JVM 启动开销。

## 虚拟机

*实现 JVM 规范或其部分规范的虚拟机。*
* [Avian](https://github.com/ReadyTalk/avian) - 轻量级高度可移植的 JVM，具有 AOT 编译选项。
* [Dalvik](https://source.android.com/devices/tech/dalvik/) - Android 运行时 (ART) 是 Android 上的应用程序和某些系统服务使用的托管运行时。
* [DCEVM](http://dcevm.github.io) - 修改 Java HotSwap VM，无限支持运行时重新加载类。
* [HotSpot](http://openjdk.java.net/groups/hotspot/) - HotSpot 虚拟机由 Oracle 公司维护和分发。
* [IBM J9](http://www.ibm.com/developerworks/java/jdk/) - JVM 由 IBM 开发。
* [Eclipse OpenJ9](https://github.com/eclipse/openj9) - Eclipse OpenJ9。
* [J2ObjC](https://github.com/google/j2objc) - 从 Java 源代码到 Objective-C 代码的转换器。在 iOS 本机应用程序和 Android 本机应用程序之间保留共享代码。
* [jvm.go](https://github.com/zxh0/jvm.go) - 用 Go 编写的 JVM。
* [ParparVM](https://github.com/codenameone/CodenameOne/tree/master/vm) - 用于 iOS 本机开发的开源 Java 字节码到 C 转换器。设计为 [Codename One](https://www.codenameone.com/) WORA 移动项目的一部分。
* [MobiDevelop's RoboVM Fork](https://github.com/MobiVM/robovm) - 针对 iOS、Mac OSX 和 Linux 的 JVM 字节码提前编译器。
* [Zing](https://www.azul.com/products/zing/) - 唯一消除大堆大小时 Java 垃圾收集暂停的 JVM。
* [Zulu](https://www.azul.com/products/zulu/) - OpenJDK 唯一经过认证的多平台版本：免费、100% 开源 Java。

# 资源

## 文档

*与 JVM 相关的文档*
* [TCP 跟踪点](http://www.brendangregg.com/blog/2018-03-22/tcp-tracepoints.html) Brendan Gregg 使用 tcplife 的 Linux bcc/BPF
* [Linux tracing workshop](https://github.com/goldshtn/linux-tracing-workshop) - 使用 BPF 进行 JVM 监控、Linux 跟踪工具研讨会的示例和实践实验室。
* [JVM Anatomy Park](https://shipilev.net/jvm-anatomy-park/) - Aleksey Shipilёv 的迷你帖子系列，其中每篇帖子都只针对一个主题进行深入探讨。
* [Coordinated Omission problem](https://groups.google.com/forum/#!msg/mechanical-sympathy/icNZJejUHfE/BfDekfBEs_sJ) - 关于机械同情的讨论。
* [False sharing](http://mechanical-sympathy.blogspot.se/2011/07/false-sharing.html) - 线程在修改共享同一缓存行的自变量时会影响彼此的性能。马丁·汤普森.
* [The JVM specification](https://docs.oracle.com/javase/specs/jvms/se8/jvms8.pdf) - Java 虚拟
机器规范 Java SE 8 版。
* [The Java Memory Model](http://www.cs.umd.edu/~pugh/java/memoryModel/) - Java 内存模型讨论和相关信息的起点。
* [The JSR-133 Cookbook for Compiler Writers](http://gee.cs.oswego.edu/dl/jmm/cookbook.html) - 实现 JSR-133 指定的新 Java 内存模型 (JMM) 的非官方指南。
* [Garbage Collection Tuning Guide](http://docs.oracle.com/javase/8/docs/technotes/guides/vm/gctuning/) - HotSpot 虚拟机垃圾收集调整指南。
* [Safepoints](http://psy-lob-saw.blogspot.se/2014/03/where-is-my-safepoint.html) - 我的安全点在哪里？尼桑·瓦卡特。
* [Topics in High-Performance Messaging](https://www.informatica.com/downloads/1568_high_perf_messaging_wp/Topics-in-High-Performance-Messaging.htm) - 高性能消息传递系统中解释的设计决策、经验和约束。
* [Top 10 Performance Mistakes](http://www.infoq.com/articles/top-10-performance-mistakes) - Martin Thompson 在制​​作中遇到的十大性能相关错误摘要。
* [The USE method](http://www.brendangregg.com/usemethod.html) - 使用饱和度和误差 (USE) 方法是一种用于分析任何系统性能的方法。布伦丹·格雷格.
* [An introduction to distributed systems](https://github.com/aphyr/distsys-class) - 凯尔·金斯伯里（《杰普森》的作者）。
* [Using JDK 9 Memory Order Modes](http://gee.cs.oswego.edu/dl/html/j9mm.html) - 适合熟悉 Java 并发但不熟悉 VarHandles 提供的 JDK 9 中可用的内存顺序模式的专家程序员。
* [CPU Utilization is Wrong](http://www.brendangregg.com/blog/2017-05-09/cpu-utilization-is-wrong.html) - 测量每周期指令 (IPC) 的 CPU 利用率。布伦丹·格雷格.
* [Linux Load Averages: Solving the Mystery](http://www.brendangregg.com/blog/2017-08-08/linux-load-averages.html) - 布伦丹·格雷格.
* [What every programmer should know about solid-state drives](http://codecapsule.com/2014/02/12/coding-for-ssds-part-6-a-summary-what-every-programmer-should-know-about-solid-state-drives/) - 伊曼纽尔·古萨尔特。
* [Quick Tips for Fast Code on the JVM](https://gist.github.com/djspiewak/464c11307cabc80171c90397d4ec34ef) - 丹尼尔·斯皮瓦克.
## 社区

*积极讨论。*

* [concurrency-interest](http://altair.cs.oswego.edu/mailman/listinfo/concurrency-interest) - JSR-166 的讨论列表。
* [hotspot-compiler-dev](http://mail.openjdk.java.net/mailman/listinfo/hotspot-compiler-dev) - 有关 HotSpot 字节码编译器开发的技术讨论。
* [hotspot-dev](http://mail.openjdk.java.net/mailman/listinfo/hotspot-dev) - HotSpot 开发邮件列表。
* [hotspot-gc-dev](http://mail.openjdk.java.net/mailman/listinfo/hotspot-gc-dev) - 关于 HotSpot 垃圾收集器开发的技术讨论。
* [mechanical-sympathy](https://groups.google.com/forum/#!forum/mechanical-sympathy) - 讨论如何针对底层堆栈/平台进行编码和测量，以便获得良好的性能。
* [Performance Java User's Group](https://plus.google.com/u/0/communities/107178245817384004088/) - 适合想要将系统提升到新水平的 Java 专家*开发人员*
* [Virtual Machine Meetup 2017](http://vmmeetup.github.io/2017/) - 讨论托管语言执行领域最新研究和发展的场所。

## 媒体

*与 JVM 相关的视频、播客和其他媒体*
* [FOSDEM 2018](https://fosdem.org/2018/schedule/track/free_java/) - FOSDEM 2018 免费 Java 开发室。
* [JFokus 2018](https://www.youtube.com/playlist?list=PL2ekzZZrxVUkhrcMKuPMbiKoghc777plr) - GC版。 Shenandoah、ZGC、Zing、Fibers、Falcon 等
* [G1 Garbage Collector in Java 8/9](http://nighthacking.com/g1-gc-with-kirk-pepperdine/) - 柯克·佩珀代因。
* [Extreme Profiling: Digging Into Hotspots](https://youtu.be/7PkkxDaFDj8?list=PLKuh52zVrL6l6jzeSwNce77yLdfKmHAgD) - 尼桑·瓦卡特。
* [Java vs. C Performance](http://www.infoq.com/presentations/java-vs-c-performance) - 悬崖点击。
* [Why JNI is slow?](https://www.youtube.com/watch?v=LoyBTqkSkZk) - 悬崖点击
* [A Crash Course in Modern Hardware](https://www.youtube.com/watch?v=OFgxAFdxYAQ) - 悬崖点击
* [Java Profiling from the Ground Up](https://www.youtube.com/watch?v=_6vJyciXkwo) - 尼桑·瓦卡特。
* [The Illusion of Execution](https://www.youtube.com/watch?v=3g9R-RVIkOE) - 尼桑·瓦卡特。
* [Mythbusting Modern Hardware to Gain 'Mechanical Sympathy'](https://www.youtube.com/watch?v=MC1EKLQ2Wmg) - 马丁·汤普森.
* [Designing for Performance](https://www.youtube.com/watch?v=fDGWWpHlzvw) - 马丁·汤普森.
* [How NOT to Measure Latency](https://www.youtube.com/watch?v=lJ8ydIuPFeU) - 吉尔·泰内.
* [JVM Language Summit 2015](http://openjdk.java.net/projects/mlvm/jvmlangsummit/) - 2015 年 JVM 语言峰会。
* [JVM Language Summit 2016](https://www.youtube.com/playlist?list=PLX8CzqL3ArzUY6rQAQTwI_jKvqJxrRrP_) - 2016 年 JVM 语言峰会。
* [JVM Language Summit 2017](https://www.youtube.com/playlist?list=PLX8CzqL3ArzXJ2EGftrmz4SzS6NRr6p2n) - 2017 年 JVM 语言峰会。
* [Bits of advice for VM writers](https://www.youtube.com/watch?v=vzzABBxo44g) - 悬崖点击。
* [Understanding Java garbage collection ...](https://www.youtube.com/watch?v=_e5hujoTkgY) - 吉尔·泰内.
* [Faster Object Arrays](https://www.youtube.com/watch?v=bZuPTCaciLU) - 吉尔·特内 (Gil Tene) 在 GOTO 会议上。
* [Java Memory Model Pragmatics](https://www.youtube.com/watch?v=TxqsKzxyySo) - 阿列克谢·希皮列夫。
* [With GC Solved, What Else Makes a JVM Pause?](https://www.youtube.com/watch?v=Y39kllzX1P8) - 约翰·库斯伯特森。
* [JVM Mechanics](https://vimeo.com/120533011) - 道格拉斯·霍金斯。
* [Give me 15 minutes and I'll change your view of Linux tracing](https://www.youtube.com/watch?v=GsMs3n8CB6g) - 布伦丹·格雷格.
* [Kernel Recipes 2017: Performance Analysis with BPF](https://www.slideshare.net/brendangregg/kernel-recipes-2017-performance-analysis-with-bpf) - 布伦丹·格雷格.
* [Shenandoah deep talk](https://shipilev.net/talks/vmm-Sep2017-shenandoah.pdf) - Aleksey Shipilëv 在 2017 年虚拟机聚会上的 Shenandoah 演讲比平常稍深入。
* [Shenandoah: The Garbage Collector That Could](https://www.youtube.com/watch?v=VCeHkcwfF9Q) - 阿列克谢·希皮列夫 - Devoxx 2017/11
* [Analyzing and Debugging the Java HotSpot VM at the OS Level](https://www.youtube.com/watch?v=k7IX_diKCEo) - 沃尔克·西蒙尼斯.
* [Cliff Click podcast 2017/09/16](http://www.cliffc.org/blog/2017/09/16/programming-and-performance-intro/) - 编程和性能介绍。
* [Cliff Click podcast 2017/09/16](http://www.cliffc.org/blog/2017/09/16/of-bugs-and-coding-styles/) - 错误和编码风格。
* [Cliff Click podcast 2017/09/18](http://www.cliffc.org/blog/2017/09/18/java-vs-cc-the-podcast/) - Java 与 C/C++。
* [Cliff Click podcast 2017/09/21](http://www.cliffc.org/blog/2017/09/21/debugging-data-races/) - 调试数据争用。
* [Cliff Click podcast 2017/09/24](http://www.cliffc.org/blog/2017/09/24/fast-bytecodes-for-funny-languages/) - 有趣语言的快速字节码。
* [Cliff Click podcast 2017/09/28](http://www.cliffc.org/blog/2017/09/28/struct-of-arrays-vs-array-of-structs/) - 数组结构与结构数组。
* [Cliff Click podcast 2017/10/04](http://www.cliffc.org/blog/2017/10/04/the-3-hardest-problems-in-programming/) - 编程中最难的 3 个问题。
* [Cliff Click podcast 2017/11/05](http://cliffc.org/blog/2017/11/05/modern-hardware-performance-cache-lines/) - 现代硬件性能和缓存线。
* [Cliff Click podcast 2017/11/09](http://cliffc.org/blog/2017/11/09/queuing-in-practice/) - 排队实践。
* [Which technique do programming language parsers and interpreters use?](https://www.quora.com/Which-technique-do-programming-language-parsers-and-interpreters-use/answer/Cliff-Click-1?srid=dZAx) - 悬崖点击。
* [Everything about Stack Traces and Heap Dumps](https://vimeo.com/233820012) - 安德烈·潘金.
* [Fast and safe production monitoring of JVM with BPF tools](http://s.sashag.net/velny17-jvm) - 萨莎·戈德斯坦。
* [The Future of the Linux Page Cache](https://www.youtube.com/watch?time_continue=1&v=xxWaa-lPR-8) - 马修·威尔考克斯。

## 人

*分享来之不易、通常未记录的 JVM 内部运作知识和数据的人*
* [Aleksey Shipilëv](http://shipilev.net/) - 开发Oracle/Open JDK/Hotspot等Java相关技术。
* [Andrey Breslav](https://twitter.com/abreslav) - Kotlin @ JetBrains 的首席语言设计师。
* [Brian Goetz](https://twitter.com/BrianGoetz) - Oracle 的 Java 语言架构师。
* [Ben Christensen](https://twitter.com/benjchristensen) - Facebook、Netflix、苹果工程。
* [Brendan Gregg](http://www.brendangregg.com) - 云性能、内核工程师、演讲者、作家。
* [Charles Nutter](https://twitter.com/headius) - JRuby 家伙。
* [Claes Redestad](https://twitter.com/cl4es) - 使用 OpenJDK 的东西 @ Oracle。
* [Cliff Click](http://www.cliffc.org/blog/) - HotSpot 服务器编译器的创建者。
* [Dave Dice](https://blogs.oracle.com/dave/) - Oracle 可扩展同步研究小组的高级研究科学家。
* [Dávid Karnok](http://akarnokd.blogspot.se/) - RxJava 提交者撰写有关高级 RxJava 的博客。
* [Doug Lea](http://g.oswego.edu/) - Java内存模型的作者。
* [Gil Tene](https://twitter.com/giltene) - 阿祖尔系统公司。
* [Heinz Kabutz](https://twitter.com/heinzkabutz) - 250 多篇 Java 专家时事通讯的作者。
* [Ivan Krylov](https://twitter.com/JohnWings) - JVM专家。
* [Jake Wharton](https://twitter.com/JakeWharton) - Square、Google、开源黑客。
* [John Rose](https://blogs.oracle.com/jrose/) - 热点开发者。
* [Jonas Bonér](https://twitter.com/jboner) - Lightbend 创始人兼首席技术官。
* [Lukas Eder](https://twitter.com/lukaseder) - 博主。 JOOQ的作者。
* [Marcus Lagergren](https://twitter.com/lagergren) - Java语言团队校友。
* [Mark Reinhold](https://twitter.com/mreinhold) - Oracle Java 平台组首席架构师。
* [Martin Thompson](http://mechanical-sympathy.blogspot.se/) - 脸色苍白的表演黑帮。
* [Martijn Verburg](https://twitter.com/karianna) - 爪哇冠军。
* [Kirk Pepperdine](https://twitter.com/javaperftuning) - 从事高性能和分布式计算工作近20年。
* [Nitsan Wakart](http://psy-lob-saw.blogspot.se/2014/03/where-is-my-safepoint.html) - 阿祖尔系统公司。
* [Norman Maurer](https://twitter.com/normanmaurer) - Netty 开发者。
* [Paul Phillips](https://twitter.com/contrarivariant) - 永远无可争议的 SLOC Scala 编译器开发。
* [Per Liden](https://twitter.com/perliden) - 攻击 Oracle 的 HotSpot JVM。
* [Peter Lawrey](https://twitter.com/PeterLawrey) - 高性能 Java 系统的创新开发商，以获得竞争优势。
* [Rafael Winterhalter](https://twitter.com/rafaelcodes) - ByteBuddy 的作者。
* [Richard Warburton](https://twitter.com/RichardWarburto) - 开发者、演讲者、作家。
* [Richard Startin](http://richardstartin.uk/) - 性能分析师、开发人员、博主。
* [Ron Pressler](https://twitter.com/pressron) - 平行宇宙。 JVM 的领先纤维和延续。
* [Stephen Colebourne](https://twitter.com/jodastephen) - 爪哇冠军。偶尔的博主和演讲者。最著名的是 Joda 项目和 JSR-310。
* [Todd L. Montgomery](https://twitter.com/toddlmontgomery) - 前 CTO、前 NASA 研究员、网络极客、消息中间件设计师。
* [Stéphane Maldini](https://twitter.com/smaldini) - Reactor 项目负责人@Pivotal。
* [Stuart Marks](https://twitter.com/stuartmarks) - 反对者博士。 Java/JDK/OpenJDK 开发人员
* [Vladimir Ivanov](https://twitter.com/iwan0www) - 攻击 Oracle HotSpot JVM。
* [Viktor Klang](https://twitter.com/viktorklang) - Typesafe Inc. 副首席技术官


# 贡献

非常欢迎您的贡献！

请查看 [contributing.md](https://github.com/deephacks/awesome-jvm/blob/master/contributing.md) 以获取指南。
