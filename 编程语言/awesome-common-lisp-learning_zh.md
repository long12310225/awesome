# 很棒的 Common Lisp 学习 [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

<div align="center">
  <img src="LISP_logo_mid.png">
</div>

此列表重点关注学习 Common Lisp 的资源，尤其是我发现有用的资源。

还有其他 Awesome Common Lisp 列表专注于其他主题：
- [Libraries](https://github.com/CodyReichert/awesome-cl)
  - [Curated Libraries](https://github.com/vindarel/curated-awesome-cl) - 从上面的列表中分叉并更新。
- [Software](https://github.com/azzamsa/awesome-cl-software)

欢迎贡献。详情请阅读[贡献指南](contributing.md)。

## 内容

- [如何使用](#how-to-use)
- [Lisp 环境](#lisp-environments)
- [在线参考资料](#online-references)
- [在线书籍](#online-books)
- [离线书籍](#offline-books)
- [在线社区](#online-community)
- [图书馆管理](#library-management)
- [Common Lisp 实现](#common-lisp-implementations)
- [Credit](#credit)

## 如何使用
1. 获取 Lisp 环境。
2. 将 [The Common Lisp Hyperspec](http://www.lispworks.com/documentation/common-lisp.html) 添加为书签。
3. 下载并通读一本适当级别的 Lisp 书籍。输入示例并使用代码。请随意更换书籍并尝试不同的书籍。
4. 尝试[Exercism](https://exercism.org/tracks/common-lisp)。
5. 如果您遇到困难，请查找在线社区并[提出巧妙的问题](http://www.catb.org/esr/faqs/smart-questions.html)。
6. 了解 [Quicklisp](https://www.quicklisp.org/beta/)。
7. 在某个时候，阅读 Lisp 实现的手册。

## Lisp 环境
您可以直接运行 Lisp 实现，但编辑环境使体验更轻松。
- 预打包环境
  - [Portacle](https://shinmera.github.io/portacle/) - 一个可移植的多平台 Common Lisp 环境。它附带了一个稍微定制的 Emacs，带有 SLIME、SBCL（一种流行的 Common Lisp 实现）、Quicklisp 和 Git。无需安装，因此这是一种非常快速且简单的上手方法。
  - [Lispbox](https://common-lisp.net/project/lispbox/) - IDE (Emacs + SLIME)、Common Lisp 实现 (Clozure Common Lisp) 和库管理器 (Quicklisp)，预先打包为 Windows、macOS 和 Linux 的存档。 Practical Common Lisp 中“Lisp in a Box”的后代[提到](http://www.gigamonkeys.com/book/lather-rinse-repeat-a-tour-of-the-repl.html)。
  - [Lispworks Personal Edition](http://www.lispworks.com/downloads/) - 用于 LispWorks Lisp 的非基于 Emacs 的 IDE，有一些限制。
  - [Allegro Common Lisp](https://franz.com/products/allegrocl/) - 拥有免费的 [Express Edition](https://franz.com/downloads/clp/survey) IDE 和 [YouTube 上的培训视频](https://www.youtube.com/channel/UCN36UrxtyNBJPaG0kmBJNRw)。
- 对于高级用户
  - [Articulate Common Lisp](http://articulate-lisp.com) - 构建 Lisp 环境的 HOWTO，包含有关[有用的库](http://enchant-lisp.com/project/abcs.html) 以及如何[构建项目](http://enchant-lisp.com/project/new-project.html) 的信息。
- 如果您是经验丰富的 [Emacs](https://www.gnu.org/software/emacs/) 用户，则只需安装 [SLIME](https://common-lisp.net/project/slime/) 和 [受支持的 Common Lisp 实现](https://common-lisp.net/project/slime/doc/html/Platforms.html#Platforms)。有关更多详细信息，请参阅 [SLIME 手册](https://common-lisp.net/project/slime/doc/html/)。
- Common Lisp Cookbook 提供了有关使用 [Roswell](https://github.com/roswell/roswell/wiki) 等实施管理器或在 Docker 上[安装实施](https://lispcookbook.github.io/cl-cookbook/getting-started.html)的更多信息。

## 在线参考资料
- [The Common Lisp Hyperspec (CLHS)](http://www.lispworks.com/documentation/common-lisp.html) - *Common Lisp 的*语言参考文档。立即添加书签。
  - [Chapter 7](http://www.lispworks.com/documentation/HyperSpec/Body/07_.htm) - 涵盖 Common Lisp 对象系统 (CLOS)。
- [The ANSI Common Lisp Standard Draft](http://cberr.us/tech_writings/notes/common_lisp_standard_draft.html) - ANSI INCITS 226-1994（以前称为 ANSI X3.226-1994）标准的最后一个草案版本。
- 草案是免费的，但标准不是。
- 它与官方标准几乎相同，有些人更喜欢它而不是 CLHS。
- [The Common Lisp Cookbook](http://lispcookbook.github.io/cl-cookbook/) - 有用的 Lisp 食谱列表。还包含 CL 信息的其他在线来源的列表。
- [Common Lisp the Language (2nd Edition) by Guy L. Steele](https://www.cs.cmu.edu/Groups/AI/html/cltl/cltl2.html) - 对 Common Lisp 语言在 ANSI 标准化之前的描述。不要将其用作参考。
  - [Cliki on CLtL2](https://cliki.net/Getting+Started) - 声称它对[LOOP]有更有用的描述(http://www.cs.cmu.edu/afs/cs.cmu.edu/project/ai-repository/ai/html/cltl/clm/node235.html#SECTION003000000000000000000)和[格式](http://www.cs.cmu.edu/afs/cs.cmu.edu/project/ai-repository/ai/html/cltl/clm/node200.html) 比 CLHS 更有效。
  - [Stack Overflow on CLtL2](https://stackoverflow.com/questions/108537/what-are-the-main-differences-between-cltl2-and-ansi-cl) - 有些人建议使用 CLtL2 来获得洞察力和灵感，但在编程时使用 CLHS。
  - [CLtL2 和 ANSI Common Lisp 规范之间的差异列表。](http://linuxfinances.info/info/commonlisp.html#AEN9679)
  - [Chapter 28](https://www.cs.cmu.edu/Groups/AI/html/cltl/clm/node260.html#SECTION003200000000000000000) - 涵盖 Common Lisp 对象系统。

## 在线书籍
这些书籍可以在线免费获取，大致按从基础到高级的顺序排列：
- [Common Lisp: A Gentle Introduction to Symbolic Computation by David S. Touretzky](http://www.cs.cmu.edu/~dst/LispBook/) - 对于刚接触编程的人来说是一个很好的介绍。包含真正有用的实用程序的代码，例如 [DTRACE](http://www.cs.cmu.edu/~dst/Lisp/dtrace/) 和 [SDRAW](http://www.cs.cmu.edu/~dst/Lisp/sdraw/)。
- [Common Lisp: An interactive approach by Stuart C. Shapiro](https://www.cse.buffalo.edu/~shapiro/Commonlisp/) - 主要通过练习进行教学的教科书。
- [Practical Common Lisp by Peter Seibel](http://www.gigamonkeys.com/book/) - 对于经验丰富的程序员来说这是一个很好的介绍，并试图从一开始就强调 CL 与其他语言的不同之处。
- [Common Lisp Koans](https://github.com/google/lisp-koans) - 不完全是一本书，而是一套帮助您学习语言的公案。
- [On Lisp by Paul Graham](http://www.paulgraham.com/onlisp.html) - 对于具有中等经验的 Lispers 来说是一本很棒的书。
- [Let Over Lambda by Doug Hoyte](https://letoverlambda.com) - 关于 Lisp 宏的高级书籍。
- 前六章可在​​线获取。
  - [Comments on Let Over Lambda](https://www.reddit.com/r/lisp/comments/3actsc/let_over_lambda/) - 有几个人建议您在阅读本书之前先熟悉 On Lisp，但开始的速度很慢。
  - [The chapter on closures](https://letoverlambda.com/index.cl/guest/chap2.html) - 有几个重要的示例，并演示了此功能的强大功能。
- [Paradigms of Artificial Intelligence Programming by Peter Norvig](https://github.com/norvig/paip-lisp) - Lisp 有许多有趣的应用，但不再是 AI 的良好参考。

## 离线书籍
这些是您必须购买或从图书馆借阅的书籍。
- [Land of Lisp by Conrad Barski, MD](http://landoflisp.com) - 有趣的 Lisp 介绍，使用漫画并让您编写游戏。
- 以[电子书](https://www.nostarch.com/lisp.htm) 形式提供。
- 几个循环宏被编写为“for x for y...”，您可以将其更改为“for x from 0 for y...”以使它们在 SBCL 中工作。
- 有一个[勘误表页面](http://landoflisp.com/errata.html)。
- 这本书的大部分内容都很有趣，而且相当简单，但从第 18 章开始就变得很麻烦。感觉后面的章节介绍得不多，所以我建议此时切换到另一本书。
- 第 13、19 和 20 章中的 Web 服务器示例仅适用于 CLISP，并且需要添加 HTTP 响应标头才能正确呈现 HTML。
- [ANSI Common Lisp by Paul Graham](http://www.paulgraham.com/acl.html) - 作为参考很好，涵盖了 CLOS，并且有几个示例程序实现。
- [第 1 章](http://lib.store.yahoo.net/lib/paulgraham/acl1.txt) 和 [第 2 章](http://lib.store.yahoo.net/lib/paulgraham/acl2.txt) 的纯文本版本可在线获取。
- [Common Lisp Recipes by Edmund Weitz](http://weitz.de/cl-recipes/) - 一组很棒的 Common Lisp 模式。
- [Object-Oriented Programming in Common Lisp by Sonya E. Keene](https://www.amazon.com/Object-Oriented-Programming-COMMON-LISP-Programmers/dp/0201175894) - 对 CLOS 的深入描述，并展示如何将其与示例应用程序一起使用。
- [The Art of the Metaobject Protocol by Gregor Kiczales, Jim des Rivieres, and Daniel G. Bobrow](https://www.amazon.com/Art-Metaobject-Protocol-Gregor-Kiczales/dp/0262610744/) - 描述 CLOS 元对象协议 (MOP)。
  - [Chapters 5 and 6 (available online)](http://metamodular.com/CLOS-MOP/) - Robert Strandh 提出的 CLOS 元对象协议扩展规范。
- 由 Jean-Philippe Paradis 的 [现代公共领域 CLOS MOP 规范](https://clos-mop.hexstreamsoft.com/) 取代 ([Hexstream](https://github.com/Hexstream))。
  - [Adam Tornhill on AMOP](http://www.adamtornhill.com/reviews/amop.htm) - 建议阅读《实用 Common Lisp》、《Common Lisp 中的面向对象编程》和《AMOP》。

## 在线社区
- [Cliki](http://cliki.net) - Common Lisp Wiki。 CL 的所有内容的绝佳资源。有一个很棒的 [入门](http://cliki.net/Getting+Started) 页面和广泛的 [Lisp 书籍](http://cliki.net/Lisp%20books) 列表。
- [Libera.Chat](https://libera.chat/) 网络上的#clschool、#lisp、#ccl、#sbcl 和[其他房间](https://www.cliki.net/IRC) 是学习 Common Lisp 的好地方。 （[应该避免使用 Freenode。](https://gist.github.com/joepie91/df80d8d36cd9d1bde46ba018af497409))
- [Lisp Subreddit](http://www.reddit.com/r/lisp/) - 一个活跃的社区，侧边栏中有大量有用的链接和参考文档。
  - [Common Lisp Subreddit](https://www.reddit.com/r/Common_Lisp) - Common Lisp 的 Reddit 子版块。
- [Exercism's Common Lisp track](https://exercism.org/tracks/common-lisp) - 这是通过练习学习语言、审查代码以及与其他人讨论解决方案的绝佳方法。
- [Lisp Discord server](https://discord.gg/7tSq5EaA6Z) - 对于 Lisp 来说是一个 Discord。有一个专门针对 Common Lisp 的频道，很乐意回答问题。


## 图书馆管理
这些不是库，但可以帮助您查找和安装其他库。
- [Quicklisp](https://www.quicklisp.org/beta) - Lisp 库的包管理平台。
- [Quickdocs](http://quickdocs.org) - Quicklisp 中的项目文档。
- [State of the Common Lisp Ecosystem, 2015](http://borretti.me/article/common-lisp-sotu-2015) - 关于您应该使用哪些库以及原因的文章。
- [Articulate Common Lisp](http://articulate-lisp.com/project/abcs.html) - 列出一些有用的库。


## Common Lisp 实现
本节按字母顺序列出了一些常见的 CL 实现及其手册。除非另有说明，否则这些都是免费软件实现。另请参阅 Cliki 的 [免费软件 Common Lisp 实现] 列表(https://www.cliki.net/Common%20Lisp%20implementation)。
- [Allegro Common Lisp (ACL)](https://franz.com/products/allegrocl/) - 商业版，但有免费的 [Express Edition](https://franz.com/downloads/clp/survey)。
  - [ACL手册](https://franz.com/support/documentation/)
  - [YouTube 上的培训视频](https://www.youtube.com/channel/UCN36UrxtyNBJPaG0kmBJNRw)
- [CLISP](https://clisp.sourceforge.io)
  - [CLISP手册](https://clisp.sourceforge.io/impnotes.html)
- [Clozure Common Lisp (CCL)](https://ccl.clozure.com)
  - [覆铜板手册](https://ccl.clozure.com/manual/)
- [卡内基梅隆大学 Common Lisp (CMUCL)](https://www.cons.org/cmucl/)
  - [CMUCL 手册和其他有用信息](https://www.cons.org/cmucl/doc/index.html)
- [嵌入式 Common Lisp (ECL)](https://common-lisp.net/project/ecl/)
  - [电化学发光手册](https://common-lisp.net/project/ecl/static/manual/)
- [LispWorks](http://www.lispworks.com/products/index.html) - 商业版，但如前所述，有一个[个人版](http://www.lispworks.com/downloads/index.html)，但有一些小限制。
  - [LispWorks手册](http://www.lispworks.com/documentation/index.html)
- [Steel Bank Common Lisp (SBCL)](http://www.sbcl.org) - 我个人最喜欢的。
  - [SBCL手册](http://www.sbcl.org/manual/index.html)
- [Scieneer Common Lisp (SCL)](http://web.archive.org/web/20171014210404/http://www.scieneer.com/scl/) - 商业 Linux 和 Unix 实现，但具有不受限制的免费评估和非商业使用版本。
  - [SCL手册](http://web.archive.org/web/20171014210404/http://www.scieneer.com/scl/doc/)

## 信用
我从 [Rainer Joswig 在 Stack Overflow 上关于学习 Common Lisp 的回答](https://stackoverflow.com/a/7224914/1005039) 以及现已不存在的 Stack Overflow 文档网站中获得了很多信息。 [Cliki 的入门](https://cliki.net/Getting%20Started) 页面也非常宝贵。
