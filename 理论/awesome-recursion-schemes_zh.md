# 很棒的递归方案 [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

> 整理了一些用于学习和使用递归方案的有用资源。

递归方案是简单的、可组合的组合器，可以自动执行嵌套数据结构的遍历和递归过程。


## 内容

- [Introductions](#introductions)
- [Articles](#articles)
- [Papers](#papers)
- [Presentations](#presentations)
- [备忘单](#cheat-sheets)
- [Podcasts](#podcasts)
- [Implementations](#implementations)


## 简介

- [Awesome Recursion Schemes](https://github.com/passy/awesome-recursion-schemes) - 用于学习和使用递归方案的有用资源的精选。
- [Practical Recursion Schemes](https://jtobin.io/practical-recursion-schemes) - 
介绍模式函子、固定点、变形、变形、
副态和亚态，需要很少的先验知识。
- [An Introduction to Recursion Schemes](http://blog.sumtypeofway.com/an-introduction-to-recursion-schemes/) - 
由三部分组成的系列，您可以从头开始发现递归方案并
实现 Edward Kmett 库的一小部分。
- [Understanding Algebras](https://www.schoolofhaskell.com/user/bartosz/understanding-algebras) - 
Bartosz Milewski 解释了 F 代数并展示了如何在以下环境中使用它们
变态现象。
- [Recursion Schemes in JavaScript and Flow](https://medium.com/@JosephJnk/recursion-schemes-in-javascript-and-flow-with-static-land-recursision-schemes-97cf10599fb7) - 
介绍 JavaScript 中的递归方案和相关概念的系列，
面向具有最低限度函数式编程背景的开发人员。

## 文章

- [Recursion Schemes: A Field Guide (Redux)](http://comonad.com/reader/2009/recursion-schemes/) - 
带有代码示例的各种递归方案的列表。
- [Catamorphisms](https://wiki.haskell.org/Catamorphisms) - Haskell Wiki 上的定义。
- [Catamorphisms](https://www.schoolofhaskell.com/user/edwardk/recursion-schemes/catamorphisms) - 
Edward Kmett 的哈斯克尔学院代码的简短定义。
- [Rotating Squares](https://jtobin.io/rotating-squares) - Jared Tobin 使用亚同态旋转四叉树。
- [递归方案，第五部分：你好，Hylomorphisms](http://blog.sumtypeofway.com/recursion-schemes-part-v/)
- [Promorphisms, Pre and Post](https://jtobin.io/promorphisms-pre-post) - Jared Tobin 的前原态和后原态的实例。
- [Time Traveling Recursion Schemes](https://jtobin.io/time-traveling-recursion) - 以贾里德·托宾为例探索历史和未来。
- [Recursion Schemes, Part IV: Time is of the Essence](http://blog.sumtypeofway.com/recursion-schemes-part-iv-time-is-of-the-essence/) - 关于组织态论和未来态论的实用文章。
- [Cheat Sheet](https://github.com/sellout/recursion-scheme-talk/blob/master/cheat%20sheet.pdf) - 各种递归方案及其对偶的映射。
- [Correcting the Visitor pattern](http://logji.blogspot.co.uk/2012/02/correcting-visitor-pattern.html) - 展示了访问者模式实现了一个与变形一起使用的 f 代数（在 Java 中）。
- [Recursion Schemes in Scala](https://free.cofree.io/2017/11/13/recursion/) - 介绍定点组合器、变形、变形、同质、拟同质、伪同质、组织同质、动态同质和未来同质。
- [What's in a Fold: The Basic Catamorphism in recursion-schemes](https://duplode.github.io/posts/whats-in-a-fold.html) - 引入变形论作为折叠的概括。

### 野外的同质现象

Bartosz Milewski 撰写的有关通过应用水同态解决小型实际问题的文章。

- [Stalking a Hylomorphism in the Wild](https://bartoszmilewski.com/2017/12/29/stalking-a-hylomorphism-in-the-wild/) - 2017 年代码来临，多米诺骨牌挑战
- [Open Seasons on Hylomorphisms](https://bartoszmilewski.com/2018/12/20/open-season-on-hylomorphisms/) - Advent of Code 2018，字符串比较挑战

## 论文

- [Functional Programming with Bananas, Lenses, Envelopes and Barbed Wire, 1991, Meijer et al.](http://maartenfokkinga.github.io/utwente/mmf91m.pdf) - 
大部分内容都是基于原始论文。
- [A Duality of Sorts, 2013, Hinze et al.](http://www.cs.ox.ac.uk/ralf.hinze/publications/Sorting.pdf) - 
表明许多基本排序算法作为一对存在，并且这些对
折叠和展开之间的二元性自然产生。
- [Sorting with Bialgebras and Distributive Laws, 2012, Hinze et al.](http://www.cs.ox.ac.uk/people/daniel.james/sorting/sorting.pdf) - 
展示如何使用同态和非同态来提高效率
排序算法的实现。
- [Scrap your boilerplate: a practical design pattern for generic programming, 2003, SPJ et al.](http://research.microsoft.com/en-us/um/people/simonpj/Papers/hmap/hmap.ps) - 
用于编写遍历由丰富的相互递归数据类型构建的数据结构的程序的设计模式。

## 演讲

- [Slidedecks by Tim Philip Williams](http://www.timphilipwilliams.com/slides.html) - 
“递归方案示例”和“奇异交易的奇异工具”提供
简洁的定义以及许多递归方案的实际示例。
- [Unifying Structured Recursion Schemes](https://www.youtube.com/watch?v=9EGYSb9vov8) - 
Ralf Hinze、Nicolas Wu 和 Jeremy Gibbons 的 12 分钟演讲。
- [Recursion Schemes](https://www.youtube.com/watch?v=Zw9KeP3OzpU) - 
由 Tim Williams 在伦敦 Haskell 聚会上提出。
- [F-algebras or: How I Learned to Stop Worrying and Love the Type System](https://www.youtube.com/watch?v=PK4SOaAGVfg) - 
由 Anthony Burzillo 在 NYC Haskell 用户组上发表。
- [A Gentle Introduction to Recursion Schemes](https://www.youtube.com/watch?v=i5A2Amfcir8) - 
由 Jean Remi Desjardins 在 Lambdaconf 2016 上发表。
- [recursion-scheme-talk](https://github.com/sellout/recursion-scheme-talk) - 关于递归方案的幻灯片集合。
- [Bracer: Transforming Real-World Languages with Coproducts and Recursion Schemes](https://www.youtube.com/watch?v=5Kr7IykGMzU) - Patrick Thomson 就使用余积和递归方案构建程序进行了高层讨论。
- [Recursion: Where Functional Programming Hits Bottom](https://www.youtube.com/watch?v=24UoRaoKLjM) - Greg Pfeil 介绍 Haskell 和 Scala 中的递归定点数据结构和递归方案。
- [Programming with algebras](https://www.youtube.com/watch?v=-98fR9VmLbQ) - Bartosz Milewski 在 LambdaCon 上以演讲形式发表的文章。
- [Peeling the Banana: Recursion Schemes from First Principles](https://www.youtube.com/watch?v=XZ9nPZbaYfE&t=3s) - Zainab Ali 在 LambdaWorld 上发表的介绍性演讲。

## 备忘单

- [The Hitchhiker's Guide to Morphisms](https://ipfs.io/ipfs/QmTppu1VDAQWsdiyVSZX6qb8PErdpwzNP2oKfEhcgaBvWR/guide-to-morphisms.pdf) - 不同态射的概述，包括可打印的 PDF。

## 播客

- [Magic Read Along](http://www.magicreadalong.com/) - 随意讨论
范畴论经常提出递归方案，包括[episode
33](http://www.magicreadalong.com/episode/33) 谈论组织同态
和未来态。
- [Scala Love](https://scala.love/) - 关于 Scala 的播客
[第二集](https://scala.love/happy-valentin/)中的递归方案。
- [The Haskell Cast](https://www.haskellcast.com/) - 递归方案出现在
[约翰·威格利的第 13 集](https://www.haskellcast.com/episode/013-john-wiegley-on-categories-and-compilers)。

## 实施

- [递归方案](https://github.com/ekmett/recursion-schemes/)
Haskell - Edward Kmett 的规范实现。
- [Matryoshka](https://github.com/slamdata/matryoshka) 用于使用 Scalaz 的 Scala -
定点数据结构的广义折叠、展开和遍历。
- [andyscott/droste](https://github.com/andyscott/droste) 使用 Cats 的 Scala -
定点数据结构的广义折叠、展开和遍历。
- [递归\_schemes](https://github.com/vmchale/recursion_schemes/) for
Idris，基于 Edward Kmett 的 Haskell 库。
- PureScript 的 [purescript-matryoshka](https://github.com/slamdata/purescript-matryoshka) -
俄罗斯套娃的半成品港口。
- ATS 的 [recursion](https://github.com/vmchale/recursion) - 演示
ATS 中的递归方案。
- Dhall 的 [dada](https://github.com/sellout/dada) - 递归库
达尔的计划。
- [static-land-recursion-schemes](https://github.com/JosephJNK/static-land-recursion-schemes) 用于 JavaScript/Flow -
以 [flow-static-land](https://github.com/gcanti/flow-static-land) 风格编写的数据结构方案。
- Kotlin 的 [Katalyst](https://github.com/aedans/Katalyst) - 使用轻量级更高种类多态性基于 Matryoshka 的重新构想。

## 许可证

此内容已获得许可
根据 [CC0](https://creativecommons.org/publicdomain/zero/1.0/)。
