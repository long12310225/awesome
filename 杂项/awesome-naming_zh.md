# 很棒的命名 [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

<!-- lint disable no-repeat-punctuation -->
众所周知...
<!-- lint enable no-repeat-punctuation -->

> 计算机科学中只有两件难事：缓存失效和命名。
>
> ― 菲尔·卡尔顿

计算机科学中的概念通常没有任何有形的东西，因此命名事物很困难也就不足为奇了。
尽管如此，我们确实想出了聪明、有创意且有趣的名字。
其中一些是如此成熟，我们从未停下来钦佩。

这是一个精心策划的列表，说明何时正确命名事物。

## 内容

- [计算机图形学](#computer-graphics)
- [数据结构和算法](#data-structures-and-algorithms)
- [设计模式和反模式](#design-patterns-and-anti-patterns)
- [Functions](#functions)
- [信息技术安全](#it-security)
- [机器学习和人工智能](#machine-learning-and-artificial-intelligence)
- [编程语言和编程语言理论](#programming-languages-and-programming-language-theory)
- [理论计算机科学](#theoretical-computer-science)
- [工具、应用程序、库、框架](#tools-applications-libraries-frameworks)
- [用户界面设计](#user-interface-design)
- [Other](#other)

---

## 计算机图形学

- [Gift wrapping algorithm](https://en.wikipedia.org/wiki/Gift_wrapping_algorithm) - 一种用于构造包裹点集合的最小形状的算法。

## 数据结构和算法

- [Backtracking](https://de.wikipedia.org/wiki/Backtracking) - 当您探索搜索空间并到达死胡同时，您将沿着您的*轨迹*回到最后一个十字路口并尝试其他方式。
- [Brute force](https://en.m.wikipedia.org/wiki/Brute-force_search) - 暴力实际上几乎总是一种解决方案，但不是一个非常聪明的解决方案。
- [Greedy algorithm](https://en.wikipedia.org/wiki/Greedy_algorithm) - 一种算法，通过始终选择当前最好看的选项来找到解决方案，而无需过多考虑过去和未来的决策。
- [Hill climbing](https://en.wikipedia.org/wiki/Hill_climbing) - 从解决方案的丘陵“景观”中的某个地方开始，您沿着最陡峭的上升方向，直到到达山顶。不过，您可能会错过更高的山丘。
- [Israeli Queue](https://rapidapi.com/blog/israeli-queues-exploring-a-bizarre-data-structure/) - 一种优先队列，以及对以色列臭名昭著的无组织队列的引用。当这里的物品*已经有朋友在等待*时，它们可以*插队*。
- [Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes) - 一种古老的算法，用于查找给定限制内的所有素数。非素数被有条不紊地筛掉，就像通过筛子过滤掉不需要的物质一样。
- [Simulated annealing](https://en.wikipedia.org/wiki/Simulated_annealing) - 一种受退火冶金过程启发的优化算法，缓慢冷却加热的材料使其进入低能量、全局最优状态。
- [Stack](https://en.wikipedia.org/wiki/Stack_(abstract_data_type)) - 就像一堆煎饼一样，您只能在此数据结构的顶部添加和删除项目。
- [Tree](https://en.wikipedia.org/wiki/Tree_(data_struct)) - 分层组织的数据结构。从_root_项开始，其他项_分支_为_nodes_和_leaves_。树木的集合通常称为“森林”。
- [Queue](https://en.wikipedia.org/wiki/Queue_(abstract_data_type)) - 在此数据结构中，项目始终在末尾添加并在前面删除，就好像项目在排队等待一样。

## 设计模式和反模式

- [Adapter](https://en.wikipedia.org/wiki/Adapter_pattern) - 通过将自己的接口包装在现有类的接口周围，允许具有不兼容接口的类一起工作。
- [Decorator](https://en.wikipedia.org/wiki/Decorator_pattern) - 通过将对象包装在一层附加行为中来为对象添加新的职责，就像您可以在不改变墙壁的情况下装饰房间一样。
- [Facade](https://en.wikipedia.org/wiki/Facade_pattern) - 类似于建筑中的立面，立面是一个充当前端界面的对象，掩盖了更复杂的底层结构。
- [God object](https://en.wikipedia.org/wiki/God_object) - 一种反模式，其中单个对象知道太多或做太多事情。就像神一样，它是无所不知、无所不能的。
- [Promise](https://en.wikipedia.org/wiki/Futures_and_promises) - 除非有错误，否则未来可用的结果的表示。就像现实一样，承诺有时会被打破。
- [Shotgun surgery](https://en.wikipedia.org/wiki/Shotgun_surgery) - 这是一种编程反模式，只需一次更改，您就可以在代码库中的任意位置疯狂添加代码。
- [Spaghetti Code](https://en.wikipedia.org/wiki/Spaghetti_code) - 一个结构错综复杂、难以理解的程序。

## 功能

- [fold](https://en.wikipedia.org/wiki/Fold_(higher-order_function)) - 就像折叠毯子一样，此函数迭代一个集合，并在每个步骤中将当前项目与已折叠的所有内容组合起来。
- [munch](https://hackage.haskell.org/package/base-4.19.0.0/docs/Text-ParserCombinators-ReadP.html#v:munch) - 贪婪地消耗输入流直到满足的解析器函数。
- [trampoline](https://clojuredocs.org/clojure.core/trampoline) - 连续运行本身返回函数的函数。就像一个在蹦床上_返回_并弹回来的孩子。
- [zip](https://hackage.haskell.org/package/base-4.12.0.0/docs/Prelude.html#v:zip) - 将两个列表合并为一个对列表，就像拉链的互锁齿一样。

## 信息技术安全

- [Backdoor](https://en.wikipedia.org/wiki/Backdoor_(computing)) - 一种绕过计算机系统中正常身份验证的方法。
- [Canary](https://en.wikipedia.org/wiki/Stack_canary) - 放置在堆栈上的秘密值，用于检测缓冲区溢出攻击。如果它被改变，危险就近了——就像煤矿里的金丝雀警告矿工有毒气体一样。
- [Computer virus](https://en.wikipedia.org/wiki/Computer_virus) - 一种通过_感染_其他计算机程序进行自我复制的计算机程序，类似于生物病毒的行为。
- [Cyber hygiene](https://digitalguardian.com/blog/what-cyber-hygiene-definition-cyber-hygiene-benefits-best-practices-and-more) - 用户为维护系统健康和提高在线安全而应采取的步骤和实践。
- [Honeypot](https://en.wikipedia.org/wiki/Honeypot_(computing)) - 系统的一部分，看起来像一个有吸引力的目标，但实际上有助于检测和转移攻击者。
- [Phishing](https://en.wikipedia.org/wiki/Phishing) - 指使用诱饵“钓鱼”以获取敏感信息。
- [Phoning home](https://en.wikipedia.org/wiki/Phoning_home) - 当系统（例如被盗的计算机）秘密向当前所有者以外的第三方报告时。这个名字参考了电影《E.T.》
- [Sandbox](https://en.wikipedia.org/wiki/Sandbox_(computer_security)) - 一个安全且隔离的环境，用于测试可能包含恶意代码的未经验证的程序。
- [Spear phishing](https://en.wikipedia.org/wiki/Phishing#Spear_phishing) - 有针对性的个人网络钓鱼攻击，旨在诱骗特定个人或组织相信他们是合法的
- [特洛伊木马](https://en.wikipedia.org/wiki/Trojan_horse_(computing)) - 误导用户其真实意图的恶意软件。该术语源自古希腊欺骗性特洛伊木马的故事。

## 机器学习和人工智能

- [Attention](https://en.wikipedia.org/wiki/Attention_(machine_learning)) - 一种机制，允许模型有选择地关注其输入中最相关的部分，就像人类将注意力集中在最重要的事情上一样。
- [Confusion matrix](https://en.wikipedia.org/wiki/Confusion_matrix) - 分类器“混乱”的表格总结，即它认为做出正确预测但实际上没有做出正确预测的频率。
- [Decision boundary](https://en.wikipedia.org/wiki/Decision_boundary) - 划分可能数据点空间的边界。在这里你决定，这一侧的所有内容都是垃圾邮件，那一侧的所有内容都不是。
- [Dropout](https://en.wikipedia.org/wiki/Dropout_(neural_networks)) - 在训练过程中随机禁用神经元以防止过度拟合。就像一个运动队通过在随机成员缺席的情况下练习来提高水平。
- [Gradient descent](https://en.wikipedia.org/wiki/Gradient_descent) - 通过迭代计算梯度并朝最速下降的方向移动来最小化成本函数。
- [幻觉](https://en.wikipedia.org/wiki/Hallucination_(artificial_intelligence)) - 人工智能的自信反应，但其训练数据似乎并不合理。
- [Training](https://en.wikipedia.org/wiki/Training,_validation,_and_test_data_sets) - 向机器展示一堆示例，直到它从中了解我们想要什么的过程。

## 编程语言和编程语言理论

- [Choreographic programming](https://en.wikipedia.org/wiki/Choreographic_programming) - 一种编程范例，其中程序是多个并发参与者之间的交互的组合。
- [Clojure](https://clojure.org/) - 一种函数式语言，广泛使用**闭包**，但带有 **j**，因为它运行在 Java 虚拟机上。
- [C++](https://en.wikipedia.org/wiki/C%2B%2B#External_links) - 虽然 C 确实是一个坏名字，但 C++ 却相当聪明。标志性的增量运算符******表示**C++**是后继者。
- [垃圾收集器](https://en.m.wikipedia.org/wiki/Garbage_collection_(computer_science)) - 尝试查找和回收不再使用的垃圾内存的程序的一部分。
- [Lazy evaluation](https://en.wikipedia.org/wiki/Lazy_evaluation) - 一种评估策略，暂停评估直到绝对必要，然后不再进行。
- [Syntactic sugar](https://en.wikipedia.org/wiki/Syntactic_sugar) - 使语言更适合人类使用的语法。通常是常见操作的简写，也可以以更详细的形式表达。

## 用户界面设计

- [Bento layout](https://www.saasframe.io/blog/the-bento-layout-trend) - 基于网格的布局类似于便当盒的划分。
- [面包屑](https://en.wikipedia.org/wiki/Breadcrumb_(navigation)) - 导航帮助允许用户跟踪他们在程序、文档或网站中的位置。该术语参考了童话故事《汉塞尔和格蕾特》。
- [Carousel](https://www.nngroup.com/articles/designing-effective-carousels/) - 一种循环播放的动画幻灯片。
- [剪贴板](https://en.wikipedia.org/wiki/Clipboard_(computing)) - 您临时放置正在使用的_文件_的位置（即复制和粘贴缓冲区）。
- [Desktop](https://en.wikipedia.org/wiki/Desktop_metaphor) - 用户办公桌的隐喻顶部，上面可以放置文档和文档文件夹等对象。
- [Hamburger button](https://en.wikipedia.org/wiki/Hamburger_button) - 用于切换菜单的按钮。相关图标类似于汉堡包。
- [Optimistic UI](https://uxplanet.org/optimistic-1000-34d9eefe4c05) - 假设昂贵操作的用户界面将成功完成，从而提高感知性能。
- [Scrolling](https://en.wikipedia.org/wiki/Scrolling) - 屏幕内容通常不太像一本具有离散页面的书，而更像是一卷连续的羊皮纸，即卷轴。
- [Toast notification](https://en.wikipedia.org/wiki/Pop-up_notification) - 一条小消息会在屏幕边缘短暂弹出，然后自行消失，就像烤面包机中的吐司一样。

## 理论计算机科学

- [Busy Beaver](https://en.wikipedia.org/wiki/Busy_beaver) - 图灵机产生的数字如此之大，没有其他算法可以跟上它们。
- [Clique problem](https://en.wikipedia.org/wiki/Clique_problem) - 在具有友谊关系的人际网络中找到一群共同朋友的问题。或者更一般地说，找到完整的子图。
- [Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) - 游戏世界展示了如何从非常简单的成分中产生惊人的复杂性。
- [Oracle](https://en.wikipedia.org/wiki/Oracle_machine) - 一个黑匣子，甚至可以神奇地给出诸如停机问题之类的不可判定问题的答案。
- [Pumping lemma](https://en.wikipedia.org/wiki/Pumping_lemma) - 事实上，在某些形式语言中，任何足够长的字符串都可以通过重复其子字符串进行“泵送”，并且结果保持在相同的形式语言中。

## 工具、应用程序、库、框架

- [bubblewrap](https://github.com/containers/bubblewrap) - 沙盒工具为您的系统形成保护层。
- [caffeinate](https://www.theapplegeek.co.uk/blog/caffeinate) - 防止 MacOS“休眠”的终端应用程序。
- [clooney](https://github.com/GoogleChromeLabs/clooney) - 一个 JavaScript 库，实现并发计算的 Actor 模型。这个词是指乔治克鲁尼，他也是一名演员。
- [CockroachDB](https://web.archive.org/web/20150514123425/http://www.wired.co.uk/news/archive/2014-07/22/cockroachdb) - 数据库应用程序，被宣传为像蟑螂一样具有容错性和弹性。
- [corrosion](https://github.com/corrosion-rs/corrosion) - 将金属变成生锈的过程（字面意思），也是将 C++“变成”Rust 的工具。
- [git bayesect](https://hauntsaninja.github.io/git_bayesect.html) - 类似于“git bisect”，但可以使用贝叶斯推理应对片状测试。
- [go-brrr](https://github.com/molecule-man/go-brrr) - *br*otli 压缩算法的纯 Go 实现。还参考了 [go brrr meme](https://en.wiktionary.org/wiki/go_brrr)。
- [horcrux](https://github.com/jesseduffield/horcrux) - 将文件分割成加密片段，只有将这些片段组合在一起才能再次解密。在哈利·波特的宇宙中，魂器是一个人灵魂的碎片。要杀死这个人，必须摧毁所有碎片。
- [Puppeteer](https://github.com/puppeteer/puppeteer) - 浏览器自动化库。如果浏览器是木偶，那么这就是木偶操纵者。
- [Safari](https://en.wikipedia.org/wiki/Safari_(web_browser)) - Apple 开发的网络浏览器。
- [tldr](https://tldr.sh/) - 带有实际示例的简化手册页。
- [Uglify](https://github.com/mishoo/UglifyJS) - JavaScript 缩小器。删除所有使代码可读且美观的内容，以使其更小。
- [uppy](https://github.com/transloadit/uppy) - 以狗为主题的上传器组件。该名称是_upload_ 和_puppy_ 的混合。它甚至还附带了一个名为_Golden Retriever_ 的崩溃恢复插件。
- [Webpack](https://webpack.js.org/) - JavaScript 和其他 *web* 资源的捆绑器，具有简短且描述性的名称，也有些押韵。
- [yarn](https://yarnpkg.com/) - NodeJS 依赖管理器。

## 其他

- [a11y, i18n, k8s, ...](https://en.wikipedia.org/wiki/Numeronym) - 通过保留第一个和最后一个字母并在中间写下省略的字母的数量来缩写长单词。
- [ACID vs. BASE](https://www.johndcook.com/blog/2009/07/06/brewer-cap-theorem-base/) - 描述相互竞争的数据库意识形态（又名 SQL 与 NoSQL）的首字母缩略词。请注意，酸和碱在化学中也是相反的。
- [Bottleneck](https://en.wikipedia.org/wiki/Bottleneck#Computing) - 网络/应用程序的核心部分，显着限制吞吐量/性能，理想情况下应将其消除。
- [Brick](https://en.m.wikipedia.org/wiki/Brick_( electronics) ) - 当您的设备严重损坏时，它实际上会变成一块砖。
- [camelCase, snake_case, kebab-case](https://en.wikipedia.org/wiki/Letter_case#Use_within_programming_languages) - 不同的外壳样式，名称说明了其外观。
- [Code golf](https://en.wikipedia.org/wiki/Code_golf) - 用尽可能少的字符编写程序。就像高尔夫球手试图用最少的球杆击球赢得胜利一样。
- [Cookie licking](https://devblogs.microsoft.com/oldnewthing/20091201-00/?p=15843) - 例如，声称存在 GitHub 问题，然后不处理它。
- [复活节彩蛋](https://en.wikipedia.org/wiki/Easter_egg_(media)) - 一项隐藏功能，尤其是在视频游戏中，与寻找复活节彩蛋有关。
- [Firmware](https://en.wikipedia.org/wiki/Firmware) - _软件_和_硬件_之间的_软件_。
- [Floating point number](https://floating-point-gui.de/formats/fp/) - 通过让小数点_浮动_而不是固定在适当的位置，这种表示可以用有限数量的数字对不同大小的数字进行编码。
- [Framework](https://en.wikipedia.org/wiki/Software_framework) - 在软件架构中（就像在实际架构中一样），框架提供了构建的基本结构，指导和限制进一步的开发。
- [Glue Code](https://en.wikipedia.org/wiki/Glue_code) - Jenga 和乐高积木不共享相同的界面，但您始终可以将它们粘合在一起。
- [Great Firewall of China](https://en.wikipedia.org/wiki/Great_Firewall) - 中国备受争议的互联网审查制度以及对中国长城的提及。
- [心跳](https://en.wikipedia.org/wiki/Heartbeat_(computing)) - 系统发送的周期性信号，用于确认其仍然存在并正常运行，就像脉冲一样。
- [Heisenbug](https://en.wikipedia.org/wiki/Heisenbug) - 当人们试图研究它时，它似乎会消失或改变。这是维尔纳·海森堡的双关语，他发现观察量子系统的行为不可避免地会改变它们的状态。
- [Hydra](https://computer-dictionary-online.org/definitions-h/hydra-code) - 当尝试修复该错误时，会引入多个新错误。这是一个无法修复的错误。
- [Magic](https://en.wikipedia.org/wiki/Magic_(programming)) - 一个神奇的程序/一段代码正在完成它的工作，但没有人知道如何实现。就像现实一样，魔法实际上并不存在。一旦你理解了它，它就不再是魔法了。
- [进程饥饿](https://en.wikipedia.org/wiki/Starvation_(computer_science)) - 进程永远无法获得完成其工作的资源的问题。
- [Technical debt](https://en.wikipedia.org/wiki/Technical_debt) - 今天采取的捷径所隐含的未来成本，会像金融债务一样积累，最终必须偿还——通常是连利息。
- [Time travel debugging](https://en.wikipedia.org/wiki/Time_travel_debugging) - 通过源代码回顾过去，了解执行情况，有时甚至改变历史。
- [Tree shaking](https://en.wikipedia.org/wiki/Tree_shaking) - 摇动依赖树，直到所有死亡部分都脱落，最终得到一棵漂亮的瘦树。
- [Unfair enumeration](https://www.youtube.com/watch?v=CvLsVfq6cks&t=835s) - 输出所有偶数然后输出所有奇数的程序会生成不公平的自然数枚举，因为某些数字永远不会达到。
- [Yoda condition](https://eslint.org/docs/latest/rules/yoda) - 当你写 `if ("red" === color) {` 而不是 `if (color === "red") {` 时，因为它读作“如果红色等于颜色”，类似于星球大战角色尤达说话的方式。
