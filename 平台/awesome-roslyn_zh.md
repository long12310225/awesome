<p align="center">
    <a href="https://github.com/dotnet/roslyn">
        <img src="https://raw.githubusercontent.com/ironcev/awesome-roslyn/master/images/awesome-roslyn-logo.png" alt="Awesome Roslyn" width="500">
    </a>
</p>

<p align="center">
    <a href="https://github.com/sindresorhus/awesome">
        <img src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg" alt="Awesome">
    </a>
</p>

> Roslyn 书籍、教程、开源项目、分析器、代码修复、重构和源代码生成器的精选列表。

Roslyn，正式名称为[.NET编译器平台](https://en.wikipedia.org/wiki/.NET_Compiler_Platform)，是一组适用于C#和Visual Basic .NET语言的开源编译器和代码分析API。

## 内容

- [Books](#books)
- [Tutorials](#tutorials)
- [开源项目](#open-source-projects)
- [开源分析器、代码修复和重构](#open-source-analyzers-code-fixes-and-refactorings)
- [用于测试分析器、代码修复和重构的库和框架](#libraries-and-frameworks-for-testing-analyzers-code-fixes-and-refactorings)
- [源发生器](#source-generators)
- [博客文章和文章](#blog-posts-and-articles)
- [Talks](#talks)

## 书籍
精彩的书籍可以为您提供罗斯林的良好开端。

- [Roslyn Succinctly](https://www.syncfusion.com/ebooks/roslyn) - *免费电子书*，作者：Alessandro Del Sole，是一本完美的入门书。解释 Roslyn API，然后重点关注编写分析器和重构。
- [.NET Development Using the Compiler API](https://www.apress.com/la/book/9781484221105) - 贾森·博克的书。除了分析器和重构之外，它还解释了脚本 API，并对编译器 API 的未来提供了有趣的思考。
- [Roslyn Cookbook](https://www.packtpub.com/application-development/roslyn-cookbook) - 本书由 Roslyn 分析仪团队成员 Manish Vasani 撰写。在详细介绍了分析器、重构和脚本编写之后，本书深入解释了如何开发新的 C# 语言功能并为 Roslyn 源代码做出贡献。

## 教程
很棒的在线教程，可帮助您编写第一个分析器、代码修复和源代码生成器。

- [Learn Roslyn Now](https://joshvarty.com/learn-roslyn-now/) - 探索 Roslyn 编译器 API 的系列博客文章。它通过一些独立的小例子介绍了 Roslyn 的强大功能。一个完美的入门教程:-)
- [How To Write a C# Analyzer and Code Fix](https://github.com/dotnet/roslyn/blob/master/docs/wiki/How-To-Write-a-C%23-Analyzer-and-Code-Fix.md) - 所有 Roslyn 教程之母:-) 对语法和语义分析以及语法转换的实际逐步介绍。
- [C# and Visual Basic - Use Roslyn to Write a Live Code Analyzer for Your API](https://msdn.microsoft.com/en-us/magazine/dn879356.aspx) - 较旧但仍未过时的关于编写代码分析器的非常详细的 MSDN 文章。
- [C# - Adding a Code Fix to Your Roslyn Analyzer](https://msdn.microsoft.com/en-us/magazine/dn904670.aspx) - 上一篇 MSDN 文章的续集。代码修复的详细介绍。
- [Introducing C# Source Generators](https://devblogs.microsoft.com/dotnet/introducing-c-source-generators/) - C# 9.0 源生成器功能的原始公告。解释什么是源生成器、它们在哪些场景中有用，并展示如何编写简单的源生成器。
- [New C# Source Generator Samples](https://devblogs.microsoft.com/dotnet/new-c-source-generator-samples/) - 有关如何编写由额外的非代码文件（如 CSV 文件或 [Mustache](https://mustache.github.io/) 模板驱动）的重要代码生成器的示例。
- [C# Source Generators](https://github.com/amis92/csharp-source-generators) - 附加学习源、示例以及实验和生产源生成器的综合列表。一旦掌握了基础知识，这是一个完美的参考。

## 开源项目
建立在 Roslyn 之上的很棒的开源项目。

- [Bridge](https://github.com/bridgedotnet/Bridge) - C# 到 JavaScript 转译器。使用 C# 编写现代移动和 Web 应用程序，并在 JavaScript 中的任何位置运行它们。
- [Code Converter](https://github.com/icsharpcode/CodeConverter/) - C# 到 VB.NET 以及 VB.NET 到 C# 转换器。
- [CodeAnalysis.CSharp.PatternMatching](https://github.com/pvginkel/Microsoft.CodeAnalysis.CSharp.PatternMatching) - Roslyn 语法树的直观模式匹配。简化 C# 语法和语义分析。
- [CodeGeneration.Roslyn](https://github.com/AArnott/CodeGeneration.Roslyn) - 在构建过程中基于 Roslyn 的代码生成，并提供设计时支持。
- [dotnet-script](https://github.com/filipw/dotnet-script) - 从 .NET CLI 运行 C# 脚本，内联定义 NuGet 包并在 VS Code 中编辑/调试它们。
- [FlubuCore](https://github.com/dotnetcore/FlubuCore) - 跨平台构建自动化工具，用于使用 C# 代码构建项目和执行部署脚本。
- [MirrorSharp](https://github.com/ashmind/mirrorsharp) - 在线 C#、VB.NET 和 F# 代码编辑器。具有代码完成、方法签名帮助、快速修复和诊断功能。
- [OmniSharp](http://www.omnisharp.net/) - 在您选择的编辑器中启用跨平台 .NET 开发。一系列开源项目，每个项目都有一个目标：在您选择的编辑器中提供出色的 .NET 体验。
- [roslyn-linq-rewrite](https://github.com/antiufo/roslyn-linq-rewrite) - 首先使用纯过程代码重写 LINQ 表达式的语法树来编译 C# 代码。这通过最小化堆分配和动态调度来提高性能。
- [RoslynPad](https://roslynpad.net/) - 跨平台 C# 编辑器。具有代码完成、方法签名帮助、快速修复和诊断功能。
- [RoslynQuoter](https://github.com/KirillOsenkov/RoslynQuoter) - 为给定的 C# 程序生成语法树 API 调用的在线工具，用于构造该程序的语法树。
- [scriptcs](http://scriptcs.net/) - 将 C# 变成强大的脚本工具。具有 C# REPL、NuGet 包的安装以及使用单行代码执行脚本的功能。
- [Scripty](https://github.com/daveaglick/Scripty) - 使用 Roslyn 支持的 C# 脚本进行代码生成的工具。您可以将其视为 T4 模板的脚本化替代方案。
- [Sharpen](http://sharpen.rocks) - Visual Studio 扩展可以智能地将新的 C# 语言功能引入到现有代码库中。
- [SharpLab](https://sharplab.io/) - .NET 代码游乐场。显示代码编译的中间步骤和结果。显示编译器看到的代码。允许选择 Roslyn 的不同分支和版本。在浏览器中运行 C#、VB.NET 和 F# 代码。
- [Testura.Code](https://github.com/Testura/Testura.Code) - 用于生成、保存和编译 C# 代码的 Roslyn API 的包装器。提供方法和帮助器来生成类、方法、语句和表达式。
- [Uno SourceGenerator](https://github.com/nventive/Uno.SourceGeneration) - 基于正在构建的项目的 C# 源代码生成器，使用其所有语法和语义模型信息。

## 开源分析器、代码修复和重构
很棒的开源分析器、代码修复和重构。

- [.NET Analyzers](https://github.com/DotNetAnalyzers) - 用于开发 Roslyn 分析器的 GitHub 组织。组织内的各种存储库涵盖 ASP.NET Core、WPF、IDisposable、System.Reflection 的用法等分析器。
- [.NET Compiler Platform ("Roslyn") Analyzers](https://github.com/dotnet/roslyn-analyzers) - Roslyn 团队开发的诊断分析仪。最初开发是为了帮助充实静态分析 API 的设计和实现。分析器涵盖代码质量、.NET Core、桌面 .NET Framework、代码中的注释等。
- [Code Cracker](https://github.com/code-cracker/code-cracker) - 适用于 C# 和 VB.NET 的分析器库。提供许多类别的诊断，例如性能、编码风格以及一些基本的重构。
- [CSharpGuidelinesAnalyzer](https://github.com/bkoelman/CSharpGuidelinesAnalyzer) - 报告 C# 编码指南的诊断 (https://csharpcodingguidelines.com/)。
- [ErrorProne.NET](https://github.com/SergeyTeplyakov/ErrorProne.NET) - 一组分析器和代码修复，重点关注 C# 程序的正确性和性能。受到 Google 的 [Error Prone](https://github.com/google/error-prone) 的启发。
- [Mapping Generator](https://github.com/cezarypiatek/MappingGenerator) - 生成任意复杂对象-对象映射的代码修复。它可以立即识别大量使用映射的场景。 [AutoMapper](https://automapper.org/) 的设计时替代方案。
- [Nullable.Extended](https://github.com/tom-englert/Nullable.Extended) - Roslyn 工具和分析器可改善使用可为空引用类型进行编码时的体验。
- [Refactoring Essentials for Visual Studio](https://github.com/icsharpcode/RefactoringEssentials/) - 针对 C# 和 VB.NET 的重构、分析器和代码修复。
- [Roslyn Clr Heap Allocation Analyzer](https://github.com/Microsoft/RoslynClrHeapAllocationAnalyzer) - C# 堆分配分析器，可以检测显式和许多隐式分配，例如装箱、闭包、隐式委托创建等。
- [Roslynator](https://github.com/JosefPihrt/Roslynator) - 190 多个分析器和 190 多个 C# 重构的集合。涵盖编码风格、代码可读性和简化、删除冗余、修复编译器错误等等。
- [SonarC#](https://github.com/SonarSource/sonar-csharp) - C# 语言的静态代码分析器用作 SonarQube 平台的扩展。
- [StyleCop Analyzers for the .NET Compiler Platform](https://github.com/DotNetAnalyzers/StyleCopAnalyzers) - StyleCop 港口统治罗斯林。
- [VSDiagnostics](https://github.com/Vannevelj/VSDiagnostics) - 代码质量分析器的集合。涵盖异步方法的用法、标志枚举、异常处理的最佳实践以及许多其他代码质量检查。

## 用于测试分析器、代码修复和重构的库和框架
用于测试分析器、代码修复和重构的很棒的库和框架。

- [Microsoft.CodeAnalysis.Testing](https://github.com/dotnet/roslyn-sdk/tree/master/src/Microsoft.CodeAnalysis.Testing) - 用于使用 NUnit、xUnit 和 MSTest 框架测试分析器和代码修复的库。 [Roslyn SDK](https://github.com/dotnet/roslyn-sdk)的一部分。
- [RoslynTestKit](https://github.com/cezarypiatek/RoslynTestKit) - 用于为分析器、代码修复、重构和完成提供程序编写单元测试的轻量级框架。它与单元测试框架无关。

## 源发生器
很棒的（但目前主要是实验性的，因为 .NET 5.0 和 C# 9.0 仍处于预览阶段）源代码生成器和内部使用源代码生成器的开源项目。

- [DpDtInject](https://github.com/lsoft/DpdtInject) - 依赖注入容器的概念验证，它将大量解析逻辑传输到编译阶段。提供额外的编译时安全性和快速的运行时解析。
- [Generator.Equals](https://github.com/diegofrata/Generator.Equals) - 自动实现类和记录的相等和散列。支持不同的比较策略。提供类似的功能，例如基于 IL 编织的 [Equals.Fody](https://github.com/Fody/Equals)。
- [JsonSrcGen](https://github.com/trampster/JsonSrcGen) - 无反射 JSON 序列化器。通过在编译时生成无反射序列化器，允许极快的 JSON 处理。
- [Source Generator Playground](https://sourcegen.dev/) - 在线应用程序，可让您试验源生成器。非常适合学习和测试您的想法。编写您自己的源生成器或从内置示例中学习并查看生成的输出。
- [StrongInject](https://github.com/YairHalberstadt/stronginject) - 编译时依赖注入容器。编译时检查、无反射和运行时代码生成免费，因此快速且 [app-trimming](https://devblogs.microsoft.com/dotnet/app-trimming-in-net-5/) 友好。
- [StructPacker](https://github.com/RudolfKurka/StructPacker) - 适用于 C# 结构类型的低级、轻量级且注重性能的序列化器。自动生成 C# 序列化代码以实现峰值运行时性能和效率。
- [Svg to C# Source Generators](https://github.com/wieslawsoltes/SourceGenerators) - SVG 到 C# 编译器。使用 [SkiaSharp](https://github.com/mono/SkiaSharp) 作为渲染引擎将 SVG 绘图标记编译为 C#。
- [WrapperValueObject](https://github.com/martinothamar/WrapperValueObject) - 围绕类型创建无样板的包装器。对于创建[围绕原始类型的强类型包装器](https://andrewlock.net/series/using-strongly-typed-entity-ids-to-avoid-primitive-obsession/)特别有用。

## 博客文章和文章
很棒的博客文章和在线文章，涵盖性能、Roslyn 历史、内部结构等各种主题。

- [How Microsoft rewrote its C# compiler in C# and made it open source](https://medium.com/microsoft-open-source-stories/how-microsoft-rewrote-its-c-compiler-in-c-and-made-it-open-source-4ebed5646f98) - Roslyn 的旅程，由 C# 首席设计师 Mads Torgersen 介绍。关于 Roslyn 项目如何启动、为何启动以及如何使其开源的鼓舞人心的故事。
- [Inside the .NET Compiler Platform – Performance Considerations during Syntax Analysis (#SpeakRoslyn)](https://robinsedlaczek.com/2015/04/29/inside-the-net-compiler-platform-performance-considerations-during-syntax-analysis-speakroslyn/) - 深入了解 Roslyn 的性能，重点关注内存消耗。
- [Persistence, Facades and Roslyn's Red-Green Trees](https://blogs.msdn.microsoft.com/ericlippert/2012/06/08/persistence-facades-and-roslyns-red-green-trees/) - 鼓舞人心的介绍了 Roslyn 团队如何利用廉价的父引用和许多其他好处来实现不可变、可重用的树。引用：“但在罗斯林团队，我们经常做不可能的事情”:-)
- [ReSharper and Roslyn: Q&A](https://blog.jetbrains.com/dotnet/2014/04/10/resharper-and-roslyn-qa/) - 很好地解释了为什么 ReSharper 不会使用 Roslyn。包括对静态代码分析和 Roslyn 的一些限制的良好讨论。
- [Roslyn performance (Matt Gertz)](https://blogs.msdn.microsoft.com/csharpfaq/2014/01/15/roslyn-performance-matt-gertz/) - 深入了解 Roslyn 团队如何处理评估和实现绩效的主题。

## 会谈
关于罗斯林的精彩公开演讲。

- [The Power of Roslyn](https://www.youtube.com/watch?v=nXljhGDokqA) - Kasey Uhlenhuth 在 2018 年奥斯陆 NDC 上的精彩演讲，涵盖了 Roslyn 要点以及用于构建代码分析器和修复的 API 和工具。

## 贡献

欢迎贡献:-) 目标是建立一个分类的社区驱动的精彩 Roslyn 资源集合。在贡献之前，请务必阅读[贡献指南](contributing.md)。

## 许可证
[![CC0](http://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](http://creativecommons.org/publicdomain/zero/1.0)

在法律允许的范围内，Igor Rončević 放弃了本作品的所有版权以及相关或邻接权。
