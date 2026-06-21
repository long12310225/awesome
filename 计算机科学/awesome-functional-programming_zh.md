## 很棒的函数式编程

基于 [Awesome](https://github.com/sindresorhus/awesome/) 项目

## 这是关于什么的？

在过去的十年中，函数式编程因其以下特点而获得了新的力量：
有人会说，声明性特征对于并行计算非常有效
以及[摩尔定律](https://en.wikipedia.org/wiki/Moore%27s_law)的完整用法。

该存储库收集了一些有关函数式编程的材料，例如博客文章、论文、视频、
工具等，也旨在澄清其背后的一些理论主题。

想做出贡献吗？请先参考[此](https://github.com/lucasviola/awesome-function-programming/blob/master/contributing.md)。

## 目录
- [博客文章](#blog-posts)
- [Papers](#papers)
- [Wikis](#wikis)
- [Books](#books)
- [Communities](#communities)
- [Discussions](#discussions-quora-stack-overflow-reddit-etc)
- [Videos](#videos)
- [Lectures](#lectures)
- [Tools](#tools)
- [Repos](#repos)
- [People](#people)

### 博客文章
- [对当前函数式编程潮流的个人看法](http://www.akitaonrails.com/2015/10/28/personal-thoughts-on-the-current-functional-programming-bandwagon)
尽管有这个名字，这篇文章实际上澄清了函数式编程的一些基本概念，解释了 FP 的一些历史和命令式语言上 FP 功能的实现，并讨论了声明式编程的所有大惊小怪以及它在过去几年变得如此流行的原因。
- [实用的 Monad - 控制时间](http://robotlolita.me/2014/03/20/a-monad-in-practicality-controlling-time.html)
- [实用中的 Monad - 一流的失败](http://robotlolita.me/2013/12/08/a-monad-in-practicality-first-class-failures.html)
- [如何对 Haskell 代码进行脱糖](http://www.haskellforall.com/2014/10/how-to-desugar-haskell-code.html)
- [图片中的函子、应用程序和单子](http://adit.io/posts/2013-04-17-functors,_applicatives,_and_monads_in_pictures.html)
- [单子变得困难](http://www.stephendiehl.com/posts/monads.html)
- [Monad、Applicatives 和 Functor 的简单指南](https://medium.com/@lettier/your-easy-guide-to-monads-applicatives-functors-862048d61610)
- [C# 中的异步流](https://freecontent.manning.com/async-streams-in-c/)
- [如何利用 Kotlin 中的函数式编程编写更好、更简洁的代码](https://doordash.engineering/2022/03/22/how-to-leverage-functional-programming-in-kotlin-to-write-better-cleaner-code/)

### 论文
- [独特类型和 Monad 之间的权衡](http://lambda-the-ultimate.org/node/1180)
- [The implementation of Functional Programming Languages](http://research.microsoft.com/en-us/um/people/simonpj/papers/slpj-book-1987/start.htm) - 西蒙·佩顿·琼斯的论文
- [Sound and Decidable Type Inference for Functional Dependencies](http://research.microsoft.com/en-us/um/people/simonpj/papers/fd-chr/esop04.pdf) - Haskell 和 GHC 的主要创建者关于类型推断的另一篇非常著名的论文
- [Template Meta-Programming for Haskell](http://research.microsoft.com/en-us/um/people/simonpj/papers/meta-haskell/meta-haskell.pdf) - 关于在 Haskell 中编译时生成代码的论文
- [为什么函数式编程很重要](http://www.cs.kent.ac.uk/people/staff/dat/miranda/whyfp90.pdf)
- [从高阶逻辑到 Haskell：来来回回](http://isabelle.in.tum.de/~haftmann/pdf/from_hol_to_haskell_haftmann.pdf)
- [将哈斯克尔翻译为伊莎贝尔](http://es.cs.uni-kl.de/events/TPHOLs-2007/proceedings/B-178.pdf)

### 维基百科
- [nLab](http://ncatlab.org/nlab/show/HomePage) - 一个 wiki 实验室，其中包含从范畴论角度出发的文章、讨论和工具，范畴论是 FP 背后的主要数学原理。
- [Haskell/Category Theory](https://en.wikibooks.org/wiki/Haskell/Category_theory) - Wikibooks 对应用于 Haskell 的范畴论进行了很好的概述。
- [哈斯克尔维基](https://wiki.haskell.org/Haskell)

### 书籍
- [Learn you a Haskell](http://learnyouahaskell.com/) - 预订，但您也可以免费在线阅读。非常适合初学者。
- [The Little Prover](https://books.google.com.br/books?id=I9E_CgAAQBAJ&pg=PR13#v=onepage&q&f=false) - 谈论
一个名为 JBob 的定理证明者，用于用 LISP 编写证明。
- [Isabelle/HOL - A Proof Assistant for Higher-Order Logic](http://isabelle.in.tum.de/doc/tutorial.pdf) - 一本关于在 Isabelle/HOL 中实现逻辑形式主义的书。
- [The Little MLer](http://www.ccs.neu.edu/home/matthias/BTML/) - 一本专注于标准机器学习中的教学类型、递归思维和其他重要主题的书。
- [Introduction to Programming using SML](http://catalogue.pearsoned.co.uk/educator/product/Introduction-to-Programming-using-SML/9780201398205.page) - 以非常数学的方式向您介绍编程设计。
- [如何设计程序](http://www.htdp.org/) / [第二版](http://www.ccs.neu.edu/home/matthias/HtDP2e/)
- [函数式编程简介](http://www.amazon.com/Introduction-Functional-Programming-International-Computing/dp/0134841891)
- [Haskell in Depth](https://www.manning.com/books/haskell-in-depth) - 关于 Haskell 的完美第二本书，深入探讨了示例和应用场景，旨在教授 Haskell 如何工作以及如何正确应用它。
- [Grokking Simplicity: Taming complex software with functional thinking](https://www.manning.com/books/grokking-simplicity) - 使用真实场景从第一原理开始教授函数式编程。
- [Functional Programming in Scala, Second Edition](https://www.manning.com/books/functional-programming-in-scala-second-edition) - 国际畅销书经过修订，添加了新的练习、注释，并全面介绍了 Scala 3。
- [Functional Programming in C#, Second Edition](https://www.manning.com/books/functional-programming-in-c-sharp-second-edition) - C# 函数式编程的真实示例和实用技术。
- [Grokking Functional Programming](https://www.manning.com/books/grokking-functional-programming) - 函数式编程简介。
- [Functional Programming in Kotlin](https://www.manning.com/books/functional-programming-in-kotlin) - 掌握函数式编程的技术和概念，以交付更安全、更简单、更有效的 Kotlin 代码。
- [Functional Design and Architecture](https://www.manning.com/books/functional-design-and-architecture) - 使用函数式编程构建生产质量应用程序的设计模式和架构，并提供 Haskell 和其他 FP 语言的示例。
- [Haskell Bookcamp](https://www.manning.com/books/haskell-bookcamp) - 在本书中，您将获得编写 Haskell 代码以及将函数式编程应用于实际开发挑战的实践经验。
- [Mastering Functional Programming](https://www.perlego.com/book/800653/mastering-functional-programming-functional-techniques-for-sequential-and-parallel-programming-with-scala-pdf) - 如果您有命令式和 OOP 背景，本书将引导您了解函数式编程的世界，无论您使用哪种编程语言。
- [Jax in Action](https://www.manning.com/books/jax-in-action) - 一本关于 JAX 数值计算库的书。
- [Learn PowerShell Scritping in a Month of Lunches](https://www.manning.com/books/learn-powershell-scripting-in-a-month-of-lunches-second-edition) - 使用 PowerShell 脚本自动执行复杂的任务和流程。
- [F# in Action](https://www.manning.com/books/f-sharp-in-action) - 本书介绍了创建专业应用程序所需的实用 F# 开发技能。
- [Elixir in Action, Third Edition](https://www.manning.com/books/elixir-in-action-third-edition) - 这本权威畅销书全面更新至 Elixir 1.14，揭示了 Elixir 如何解决可扩展性、容错性和高可用性问题。

### 社区
- [Lambda the Ultimate](http://lambda-the-ultimate.org/) - 社区专注于讨论研究、论文
以及学术界的热门话题。非常高技术的讨论水平。
- [FP Complete](https://www.fpcomplete.com/) - 社区专注于帮助公司和学生学习和实施 Haskell 函数式编程。最著名的 Haskell 学习中心之一的主办者：[Haskell 学院](https://www.schoolofhaskell.com/school)
- [Haskellers](http://www.haskellers.com/) - Haskell 程序员的聚会点
- [ElixirLangMoscow](http://elixir-lang.moscow/) - 俄罗斯 Elixir 社区

### 讨论（Quora、Stack Overflow、Reddit 等）
- [为什么没有更多的程序员使用 Haskell](https://www.quora.com/Why-dont-more-programmers-use-Haskell)
- [尾调用/尾递归优化的隐藏复杂性](http://lambda-the-ultimate.org/classic/message1532.html)

### 视频
- [Dont fear the Monad](https://www.youtube.com/watch?v=ZhuHCtR3xq8) - 解释
微软研究员 Brian Beckman 提出的函数式编程中最晦涩难懂的主题之一。
- [Haskell is useless](https://www.youtube.com/watch?v=iSmkqocn0oQ) - 西蒙·佩顿·琼斯
只是对他的创作太谦虚了。
- [布莱恩·贝克曼：无国籍状态的禅宗](https://www.youtube.com/watch?v=XxzzJiXHOJs)
- [Erik Meijer：函数式编程](https://www.youtube.com/watch?v=z0N1aZ6SnBk)
- [Scala Monads：通过 Monadic 设计整理您的代码](https://www.youtube.com/watch?v=Mw_Jnn_Y5iA)
- [Philip Wadler 和 Erik Meijer：论编程语言理论与实践](https://www.youtube.com/watch?v=9SBR_SnrEiI)
- [Kotlin for Android & Java Developers](https://www.manning.com/livevideo/kotlin-for-android-and-java-developers) - 关于 Kotlin 的直播视频课程：函数式编程、面向对象以及在 Kotlin 中构建 Android 应用程序。
- [Do we really need OOD and FDD?](https://www.youtube.com/watch?v=KW9U6HMKEgk) - 功能声明式设计（FDD）与面向对象设计（OOD）相对
* [Functional Programming with TypeScript](https://www.youtube.com/playlist?list=PLuPevXgCPUIMbCxBEnc1dNwboH6e2ImQo) - 在这个适合初学者的 YouTube 播放列表中，探索使用 Typescript 进行函数式编程，并与 Sahand Javid 一起创建像 fp-ts 这样的库。

### 讲座
- [C9 Lectures: Dr. Erik Meijer - Functional Programming Fundamentals](https://www.youtube.com/playlist?list=PLTA0Ta9Qyspa5Nayx0VCHj5AHQJqp1clD) - Haskell 创始人之一的系列讲座
- [Adventure with types in Haskell - Simon Peyton Jones](https://www.youtube.com/watch?v=6COvD8oynmI&list=RD6COvD8oynmI#t=0) - Simon Peyton Jones 关于 Haskell 强类型系统的讲座。
- [The Algebra of Algebraic Data Types](https://www.youtube.com/watch?v=YScIPA8RbVE) - 很好的解释
关于数学和代数数据类型之间的关系，这是一些非常常见的 FP 语言（例如 Haskell 和 ML）的类型系统。

### 平台

- [Paqmind.com] – 学习和改进编程的指南和挑战。所有内容均面向 CS 和 FP。

### 工具
- [Isabelle/HOL](https://www.cl.cam.ac.uk/research/hvg/Isabelle/) - 基于高阶逻辑的通用证明助手

### 回购协议
- [Idris Koans](https://github.com/idris-hackers/idris-koans) - 伊德里斯教学项目。具有依赖类型的通用函数式编程
- [Functional Javascript Workshop](https://github.com/timoxley/functional-javascript-workshop) - 函数式 Javascript 研讨会。
- [J-Bob](https://github.com/the-little-prover/j-bob) - 《小证明者》一书中的证明助手
- [Haskell Must Watch](https://github.com/olehkuchuk/haskell-must-watch) - 有关 Haskell 的视频、讲座和课程列表。
- [Intro SML](http://www.it.dtu.dk/introSML/) - 书中的代码、更正和信息：《使用 SML 编程简介》
- [Functional Programming In JavaScript](https://github.com/busypeoples/functional-programming-javascript) - JavaScript 中的函数式编程资源列表。
- [Functional Programming Jargon](https://github.com/hemanth/functional-programming-jargon) - 提供 FP 术语表的项目，让学习 FP 变得更容易。
- [Bow](https://github.com/bow-swift/bow) - Swift 中类型化函数式编程的配套库。
- [Parsing With Haskell Parser Combinators](https://github.com/lettier/parsing-with-haskell-parser-combinators) - 使用 Haskell 解析器组合器进行解析的分步指南。
- [Functional Programming Learning Path](https://github.com/imteekay/functional-programming-learning-path.git) - 函数式编程的学习路径
### 人

- [Simon Peyton Jones](http://research.microsoft.com/en-us/people/simonpj/) - Haskell 语言和 Glasgow Haskell 编译器的创建者之一。微软研究员。
- [Philip Wadler](http://homepages.inf.ed.ac.uk/wadler/) - 爱丁堡大学理论计算机科学教授，著名论文 Propositions as Types 的作者。 Java 泛型类型背后的主要人物之一。
- [Matthias Felleisen](http://www.ccs.neu.edu/home/matthias/) - 撰写了许多书籍，例如《如何设计程序》和《小计划者》。
- [Erik Meijer](https://www.linkedin.com/pub/erik-meijer/0/5ba/924) - 微软前软件架构师、函数式编程研究员，主讲函数式编程、软件设计和响应式编程。
- [Brian Beckman](https://www.linkedin.com/in/brianbeckman) - 前微软研究员，亚马逊实际软件工程师。致力于将 FP 功能实现到多种 Microsoft 技术，例如 C#、LINQ 和 F#

### 许可证

[![CC0](https://i.creativecommons.org/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

在法律允许的范围内，[Lucas Viola](http://lucasviola.github.io) 已放弃本作品的所有版权以及相关或邻接权。
