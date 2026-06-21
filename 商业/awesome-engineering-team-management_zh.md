<!--lint disable awesome-heading-->

<p align="center">
  <a href="https://github.com/kdeldycke/awesome-engineering-team-management/">
    <img src="https://github.com/kdeldycke/awesome-engineering-team-management/raw/main/assets/awesome-management-header.png" alt="Awesome Engineering Team Management">
  </a>
</p>

<p align="center">
  <a href="https://github.com/sponsors/kdeldycke">
    <strong>Your brand → here 🚀</strong>
    <br/>
    <sup>SEO is dead. Place your product here to target AI's training data.</sup>
  </a>
</p>

---

<p align="center">
  <i>The manager's function is not to make people work, but to make it possible for people to work.</i><br>
  — Tom DeMarco<sup id="intro-quote-ref"><a href="#intro-quote-def">[1]</a></sup>
</p>

精心策划的 [![Awesome](https://awesome.re/badge-flat.svg)](https://github.com/sindresorhus/awesome) 列表**供软件开发人员过渡到工程管理角色**。汇编建议、轶事、知识花絮、讨论、行业闲聊和咆哮。某种参考书目，收集了过去几年[将我的职业生涯从软件工程师转变为工程师经理](https://devtomanager.com/interviews/kevin-deldycke/)。后来从经理到经理的经理（你们都喜欢递归吧？ʘ‿ʘ）。

- 您是一名开发人员，想知道成为一名经理是什么感觉？
- 您刚刚开始作为团队领导者的第一个职位？
- 您是否陷入工作的日常运作中？
- 我怎样才能升级到下一个级别？

您将在本指南中找到答案！它通过提供毫不妥协的见解和实用建议，从一般的领导力和管理文献中脱颖而出。它将引导您从技术背景进入管理职业轨道。

该列表有助于从一般到具体的进展，过渡到管理。它首先概述该角色，然后描述其要求及其相对于其他角色的地位。然后我们详细介绍了该行业的日常工具，包括组织工具和行为工具。最后我们讨论了这项工作的一些阴暗面。

## 内容

<!-- mdformat-toc start --slug=github --no-anchors --maxlevel=6 --minlevel=2 -->

- [工程到管理的转变](#engineering-to-management-transition)
- [建设团队](#building-teams)
- [Roles](#roles)
  - [Executives](#executives)
  - [首席技术官兼工程副总裁](#cto--vp-of-engineering)
  - [工程经理](#engineering-managers)
  - [Engineers](#engineers)
  - [Consultants](#consultants)
- [Recruitment](#recruitment)
  - [求职板](#job-boards)
  - [招聘流程](#hiring-process)
  - [Interview](#interview)
  - [编码挑战](#coding-challenge)
  - [Negotiation](#negotiation)
- [Onboarding](#onboarding)
- [Motivation](#motivation)
  - [Happiness](#happiness)
  - [Procrastination](#procrastination)
- [Culture](#culture)
- [认知工具](#cognitive-tools)
  - [Collections](#collections)
  - [Explaining](#explaining)
  - [解决问题](#problem-solving)
  - [Systems](#systems)
  - [Brainstorming](#brainstorming)
  - [Behavioral](#behavioral)
- [团队动态](#team-dynamics)
- [Engineering](#engineering)
  - [技术工程经理](#the-technical-engineering-manager)
  - [系统复杂性](#systems-complexity)
  - [Technology](#technology)
  - [工程实践](#engineering-practices)
  - [技术债务](#technical-debt)
- [远程工作](#remote-work)
- [Meetings](#meetings)
  - [1对1](#1-on-1)
  - [Standups](#standups)
- [Facilities](#facilities)
- [产品管理](#product-management)
  - [招聘 PM](#hiring-pms)
  - [产品与市场契合度](#product-market-fit)
  - [产品策略](#product-strategy)
  - [以用户为中心的设计](#user-centered-design)
  - [产品营销](#product-marketing)
- [项目管理](#project-management)
  - [Specifications](#specifications)
  - [Estimations](#estimations)
  - [Tickets](#tickets)
  - [Delivery](#delivery)
- [Agile](#agile)
- [关键绩效指标（KPI）](#key-performance-indicator-kpi)
- [目标和关键结果 (OKR)](#objectives-and-key-results-okr)
- [Training](#training)
- [Communication](#communication)
  - [Knowledge](#knowledge)
  - [Reading](#reading)
  - [Documentation](#documentation)
  - [Writing](#writing)
  - [Style](#style)
  - [Presentations](#presentations)
- [Career](#career)
  - [Promotion](#promotion)
  - [绩效评估](#performance-reviews)
- [Compensation](#compensation)
  - [Salary](#salary)
  - [Equity](#equity)
- [Politics](#politics)
- [Re-organizations](#re-organizations)
  - [Team-level](#team-level)
  - [Company-level](#company-level)
  - [Acquisition](#acquisition)
- [Health](#health)
  - [Holidays](#holidays)
  - [Stress](#stress)
  - [Burnout](#burnout)
- [挫折和失败](#setbacks-and-failures)
- [Exits](#exits)

<!-- mdformat-toc end -->

## 工程到管理的转变

第一步。最难的。如何重新获得从个人贡献者 (IC) 到一线经理的资格。

- 你一直是一名开发人员。被提供[管理职位不是晋升。这是职业生涯的改变](https://fractio.nl/2014/09/19/not-a-promotion-a-career-change/)。

- [17 Reasons not to be a Manager](https://charity.wtf/2019/09/08/reasons-not-to-be-a-manager/) - 一篇[劝阻胆怯的新兵]的文章(https://youtu.be/b07887ZzKiw?t=40)。

- [Advice to New Managers: Don't Joke About Firing People](https://staysaasy.com/engineering/2020/06/09/Don%27t-Joke.html) - “一旦你成为他们的经理，你就失去了以任何身份开玩笑他们在公司工作的权利。”

- [Advice to new managers](https://x.com/ValaAfshar/status/966125964861280256) - 成为一名优秀管理者所需的 9 项基本行为原则。

- [Mistakes I've Made as an Engineering Manager](https://css-tricks.com/mistakes-ive-made-as-an-engineering-manager/) - 错误：“1）认为人们会按照他们想要的方式提供反馈；2）尝试自己做所有事情；3）沟通一次就足够了；4）你必须始终将所有事情放在一起。”

- [Why It's Easier to Manage 4 People Than It Is to Manage 1 Person](https://staysaasy.com/management/2020/07/24/Managing-One-Person.html) - “不惜一切代价避免以下组合：新经理、一份报告、报告是行业新手、经理不是主题专家。”

- [从开发人员到经理。我应该知道或学习什么？](https://news.ycombinator.com/item?id=18823616)

- [How to be a Manager – A step-by-step guide to leading a team](https://getweeklyupdate.com/manager-guide) - 关于现代管理实践的完整、详细的指南。

- [On being an Engineering Manager](https://ruiper.es/posts/engineer-manager-2017/) - 其中一些要点需要细微差别，但另一些要点对于初次担任管理者的人来说是一种很好的体验。

- [Responsibility vs. accountability](https://news.ycombinator.com/item?id=21892816) - 经理（负责人）和工程师（负责人）之间最大的区别是：“‘坏事’发生在负责人身上，而负责人可以继续下一个项目。”

- “计算机永远无法承担责任。因此计算机永远不能做出管理决策。” - [1979 年的 IBM 幻灯片](https://x.com/mit_csail/status/1604884273789603842)。

- “在这份工作中，你的目标是慢慢地让人们失望。” （[来源](https://news.ycombinator.com/item?id=18222488))。

- “所以关键是让他们（你的直接下属）负责，而不是你。你扮演配角，他们可以向你提出要求。但目标需要非常明确。” ([来源](https://news.ycombinator.com/item?id=23973859)) - 关于如何与直接下属合作的秘诀，摘自 [高效的 7 个习惯]人](https://www.amazon.com/dp/1982137274?&linkCode=ll1&tag=kevideld-20&linkId=5920a3d486de941b37430f948d377bc9&language=en_US&ref_=as_li_ss_tl)。

- [The One Minute Manager Meets the Monkey](https://www.amazon.com/dp/0688103804?&linkCode=ll1&tag=kevideld-20&linkId=704eff2e2cddae6d97ef082a6f25bafd&language=en_US&ref_=as_li_ss_tl) - 作者用了一个比喻，其中的问题是猴子。缺乏经验的管理人员让猴子转移到他们身边，在它们的背上堆积并复合。由此，本书教你如何从承担责任转变为委派责任，这样你就不会成为瓶颈。

## 建设团队

您获得了头衔和薪资等级。恭喜！这还不能让你成为一名经理。无论您是继承现有团队还是必须从头开始，您都需要练习构建（和巩固）它们的艺术。

- [Building and Motivating Engineering Teams](http://www.elidedbranches.com/2016/11/building-and-motivating-engineering.html) - 工程师想要什么？金钱、目标和尊重。

- [What Google Learned From Its Quest to Build the Perfect Team](https://web.archive.org/web/20250601205421/https://www.nytimes.com/2016/02/28/magazine/what-google-learned-from-its-quest-to-build-the-perfect-team.html) - “谷歌的数据表明，心理安全对于团队合作至关重要。（……）创造心理安全的行为——对话轮流和同理心——是我们作为个人在需要建立联系时经常求助的不成文规则的一部分。”

- [Paper we love: Software Engineering Organizations](https://github.com/papers-we-love/papers-we-love/tree/master/software_engineering_orgs) - “软件工程的实践及其历史本身就是对人性、协调和沟通的复杂研究。”

- [Developer Tropes: "Google does it"](https://tomaytotomato.com/developer-tropes-2/) - 模仿我们行业的知名人士是成功之路。相反，本文的要点是“管理者和其他领导者应该像生态学家一样；测量、观察和培育他们的生态系统。这样做将有助于建立一个独特的工作场所，从而产生巨大的成果。”

## 角色

关于开发人员、经理和高管之间的概况、态度、行为和期望。

### 行政人员

高管是公司的高级/最高管理层。在大公司中，他们向董事会报告；在小公司中，他们直接向股东报告。预计在这一级别上将发挥领导作用。作为经理，这些人是你向其报告的人。

- [What do executives do, anyway?](https://apenwarr.ca/log/20190926) - 释义 [Andy Grove 的书《高产出管理》](https://www.amazon.com/dp/0394532341?&linkCode=ll1&tag=kevideld-20&linkId=f80a2e0610594cad92d301c587380f0a&language=en_US&ref_=as_li_ss_tl)，“高管的工作是：为整个组织定义和强化文化和价值观，并批准好的决策。”文章还详细介绍了CEO的失败模式：强迫自己做出下游决策，或者各种不解决冲突的方式。

- [Executives ratify decisions made on the spot](https://news.ycombinator.com/item?id=18089716) - 托尔斯泰的商业论文。

- [Army Leadership and the Profession](https://fas.org/irp/doddir/army/adp6_22.pdf) - 建立并描述领导者应该做什么和做什么。

- [US Air Force's Strategic Leadership Studies](https://web.archive.org/web/20190308062113/http://leadership.au.af.mil/sls-skil.htm) - 领导能力和技能的参考。

- [What Only the CEO Can Do](https://archive.ph/CcScN) - “1. 定义和解释公司有意义的“外部”；2. 回答由两部分组成的问题：我们从事什么业务，不从事哪些业务？3. 平衡当前足够的收益与未来必要的投资；4. 塑造组织的价值观和标准。”

- [How CEOs Manage Time](https://archive.ph/S32wu) - 关于大公司首席执行官将时间花在什么以及如何花的研究。打开一扇新的窗口，了解领导力的全部内容及其许多组成部分和维度。

- [Operations and Internal Communication Strategies For Effective CEOs](https://archive.ph/9DkfA) - 在坚持背景和叙述的重要性之后，作者提供了一个有趣的模板（有利于激发灵感）的仪式和反复出现的内部沟通手段。

- [Regis McKenna's talk at Silicon Valley Leaders Symposium](https://youtu.be/5Z13NI0SuyA?t=2026) - “这些是我们（营销人员）过去对个人和机构所做的事情。它们都变得自动化了。CIO 现在是营销主管。”

- [Narcissistic CEOs Weaken Collaboration and Integrity](https://www.gsb.stanford.edu/insights/narcissistic-ceos-weaken-collaboration-integrity) - “典型的有远见的领导者形象与自恋者非常相似，如果董事会不小心，他们最终会选择自恋的人担任首席执行官”。

- “招聘不是挑战。挑战在于找到那些能够在为高管工作时高效工作的人，而这些高管唯一的资格和培训就是自恋程度的自恋。” （[来源]（https://x.com/kellan/status/1205113384632500224））。

- “首席执行官将自己定位为一个控制欲强、事无巨细的人，处于一切事情的中心。这使得首席执行官可以在向可能了解情况的人提供的过程中拦截财务和其他关键数据。” ([来源](https://news.ycombinator.com/item?id=24519247)) - 或者高层如何容忍欺诈行为。这通常就是为什么需要董事会作为监督的原因。

### 首席技术官兼工程副总裁

在科技公司中，这些角色至关重要，而两者之间的界限往往很模糊。

- [CTO vs VP Engineering: What's the Difference?](https://www.ivyexec.com/career-advice/2015/cto-versus-vp-engineering-whats-the-difference/) - CTO 管理着一小群黑客。工程副总裁领导一个工程师组织。

- [Want to Know the Difference Between a CTO and a VP Engineering?](https://bothsidesofthetable.com/want-to-know-the-difference-between-a-cto-and-a-vp-engineering-4fc3750c596b) - 另一种看待事物的方式：将这些角色放置在“流程导向”和“技术能力”象限中。

- [The different skills needed to be a successful CTO](https://madewithlove.be/one-job-many-roles-the-different-skills-needed-to-be-a-successful-cto/) - 这个前提有点误导，因为详细描述了在一家初创公司中，技术创始人与公司一起成长成为首席技术官的旅程。此时文中描述的职位不是CTO，而是工程副总裁。

- [Hiring a VP of Engineering? Use This Framework](https://review.firstround.com/hiring-a-vp-of-engineering-use-this-framework-from-shopifys-vpe-to-get-it-right/) - “*我如何聘请工程副总裁？*经过 20 多年、八家公司和数千名员工的工作，我开始怀疑这个问题可能是错误的。更好的问题是，*什么是工程副总裁？*”

- [“That's usually about the time I nope right out of the interview”](https://news.ycombinator.com/item?id=19188246) - 首席技术官试图招聘工程经理的不良迹象，或者不相信等级制度的危险。

### 工程经理

经理的形式多种多样，不同公司的头衔和日常活动也有很大差异。当开发人员直接向你汇报时，你会发现自己处于第一个管理层：你是一线工程经理。

- [What are the signs that you have a great manager?](https://news.ycombinator.com/item?id=20230133) - “讽刺的是，你并没有真正注意到一位伟大的经理。”

- [Identify what makes a great manager](https://rework.withgoogle.com/en/guides/managers-identify-what-makes-a-great-manager#learn-about-googles-manager-research) - 谷歌试图证明管理者并不重要。相反，它发现了[最好的人的 10 个特征](https://archive.ph/1USa4)。

- [作为一名产品经理，如何赢得团队的尊重和信任？](https://web.archive.org/web/20220115172555/https://twitter.com/johncutlefish/status/1124938723093766144)

- [Good Boss, Bad Boss: A Peek Inside the Minds of the Best (and Worst)](https://www.youtube.com/watch?v=lmBSh1FGQyY) - 一个好老板：除掉烂苹果（没有混蛋规则）并保护人们免受高层的白痴之害。

- “你的角色之一是充当双向信息过滤器”（[来源](https://news.ycombinator.com/item?id=19187593)） - 关于如何平衡哪种信息需要共享或静音的一些提示。

- [Great PMs don't spend their time on solutions](https://web.archive.org/web/20250511211605/https://www.intercom.com/blog/great-product-managers-dont-spend-time-on-solutions/) - 不是解决方案，不是。但关于客户的问题。

- [Things I have learnt as the software engineering lead of a multinational](https://minnenratta.wordpress.com/2017/01/25/things-i-have-learnt-as-the-software-engineering-lead-of-a-multinational/) - 这里有一些有趣的观点，还有一些需要挑战。

- [Surprising Things About Working at Well-Known Tech Unicorns](https://blog.pragmaticengineer.com/surprising-things-about-working-at-tech-unicorns/) - 从工程经理的角度来看，这与我自己在高增长和可见公司中的期望与现实之间的差异的经验相呼应。

- [100+ Lessons Learned for Project Managers](https://llis.nasa.gov/lesson/1956) - 122 条格言提供了有关 NASA 项目管理成功的见解。涵盖设计、决策、管理员工、与上级和承包商合作。

- [Engineering Manager Resources](https://github.com/ryanburgess/engineer-manager) - 清单很大，但需要一些整理。

- [A vitally important part of the job: being a crap shield](https://news.ycombinator.com/item?id=24802483) - “EM 的许多工作都是用铲子涉入泥浆坑，这样您的团队就可以自由地完成工作”。

### 工程师

- [Programmer Moneyball: Challenging the Myth of Individual Programmer Productivity](https://insights.sei.cmu.edu/sei_blog/2020/01/programmer-moneyball-challenging-the-myth-of-individual-programmer-productivity.html) - “由于软件项目经理评估个人开发人员能力的能力有限，他们应该依赖高效的环境和培养人才。”

- “如果你不让 10 倍开发人员（……）做出自己的架构选择，他们很快就会变成 1 倍开发人员（或更糟）”（[来源](https://news.ycombinator.com/item?id=5496914)）。

- [7 absolute truths I unlearned as junior developer](https://monicalent.com/blog/2019/06/03/absolute-truths-unlearned-as-junior-developer/) - “1. 我是一名高级开发人员；2. 每个人都编写测试；3. 我们远远落后于其他人（又名技术 FOMO）；4. 代码质量最重要；5. 一切都必须记录在案；6. 技术债务很糟糕；7. 资历意味着最擅长编程”。

- [On Being A Senior Engineer](https://www.kitchensoap.com/2012/10/25/on-being-a-senior-engineer/) - “我希望‘高级’工程师是一名*成熟的*工程师。”

- [Things I Learnt from a Senior Software Engineer](https://neilkakkar.com/things-I-learnt-from-a-senior-dev.html) - “我在一位高级软件工程师旁边坐了一年。这就是我学到的东西。”

- [5 Things I've Learned in 20 Years of Programming](https://daedtech.com/5-things-ive-learned-in-20-years-of-programming/) - “一个拥有 5 年经验的程序员的行业任期比整个行业的一半还多。”另请参阅 [35 年后我学到的 10 件事](https://news.ycombinator.com/item?id=21612990) 的后续评论。

- [Devs I really enjoy pairing with](https://x.com/ScribblingOn/status/1002598672444448768) - “不要表现得像万事通；如果他们不知道某些事情，就公开承认；尝试一起解决问题”。

- [All the best engineering advice I stole from non-technical people](https://medium.com/@bellmar/all-the-best-engineering-advice-i-stole-from-non-technical-people-eb7f90ca2f5f) - “有趣的是，真正对软件质量产生影响的东西似乎从来都与软件无关。”

- [What Makes A Great Software Engineer?](https://faculty.washington.edu/ajko/papers/Li2015GreatEngineers.pdf) - 没有得出问题的明确答案，但详细介绍了基于 53 个属性的模型 (!)。仍然是引用有关该主题的其他论文的良好来源。

- [What makes a Senior Dev](https://news.ycombinator.com/item?id=11341567) - “时间到了，伙计。你他妈的得抓紧时间了。”

- [The different engineering levels at Google](https://news.ycombinator.com/item?id=24627229) - 从 L3 到 L8：快速描述每个级别的工程师的素质。

- [How I operated as a Staff engineer at Heroku](https://amyunger.com/blog/2020/09/10/staff-engineer-at-heroku.html) - 这是了解主管工程师这个有点模糊的头衔的一个很好的窗口，有时也称为首席工程师或软件架构师。 IE。您是技术专家，但知道如何解决非显而易见的工程问题，大多数时候是因为这些问题植根于社会、通信和层次复杂性。

- [StaffEng](https://staffeng.com) - 一旦您达到高级软件工程师级别，您就处于十字路口。您要么追求工程管理，要么继续沿着卓越技术的道路成为一名高级工程师。这是关于后期职位的指南合集。

- [10 Admirable Attributes of a Great Technical Lead](https://betterprogramming.pub/10-admirable-attributes-of-a-great-technical-lead-251d13a8843b) - “他们聪明又善良。知识渊博但谦虚。忙碌但平易近人。”

### 顾问

- “顾问是手册前面 4 页的人”（[来源](https://news.ycombinator.com/item?id=20786286)）。

- “大多数组织从顾问那里获得的价值（……）是政治掩护，让他们知道自己应该一直做出改变，但没有社会资本或关注点来进行这些改变”（[来源](https://news.ycombinator.com/item?id=21714791)）。这就是官僚机构和高度政治化的组织成为顾问的沃土的原因。

- [The Prosperous Software Consultant](https://dabit3.medium.com/the-prosperous-software-consultant-5dc8d705c5dd) - 本文让您了解独立顾问的运作方式。

## 人才招聘

您所处的行业竞争激烈，人才需求量很大。作为一名经理，要做好花费大量时间招聘人员的准备，要么是为了扩大团队规模，要么是为了填补空缺职位。这种动态也变得有趣，因为您现在处于招聘过程的双方：作为获得工作的候选人，以及作为招聘人员为您的团队配备人员。

### 求职板

通过定位正确的位置来发布您的工作机会，您就可以增加找到合适候选人的机会。

- [Awesome Job Boards](https://github.com/tramcar/awesome-job-boards) - 按领域、技术、角色和领域划分的利基职位委员会。

- [Hiring Without Whiteboards](https://github.com/poteto/hiring-without-whiteboards) - 没有与不良面试做法相关的计算机科学琐事问题的公司列表。

### 招聘流程

高增长的公司都需要在某一时刻将招聘流程工业化。

- [Why I Never Hire Brilliant Men](https://en.wikisource.org/wiki/Why_I_Never_Hire_Brilliant_Men) - 1924 年以来的 5 条简单的招聘规则。一个世纪以来，情况并没有发生太大变化。

- [A Good Tech Resume](https://thetechresume.com/A_Good_Tech_Resume.pdf) - 建议和示例的汇编，但包含对典型招聘渠道的良好描述。

- [Job Interviewing Guide](https://www.homerun.co/artofwork/guides/job-interviewing) - 对招聘流程的详细描述，是当您的公司足够大并开始将事情正式化时的灵感来源。

- [Open Sourced Interview Process](https://github.com/cockroachlabs/open-sourced-interview-process) - Cockroach Labs 发布了他们的流程，“旨在让候选人熟悉并消除偏见，从而获得更好的候选人体验和招聘决策。”

- [Rethinking the Hiring Process](https://www.karllhughes.com/posts/rethinking-hiring) - “测试程序员实际上并不擅长的事情，并期望了解他们如何在你的公司工作，这是一种妄想，我认为这种面试只会让招聘团队感觉更聪明，并确保具有传统计算机背景的工程师获得更好的结果。”

### 采访

审查潜在候选人时可以使用的问题列表，以及从中汲取灵感并用作对话开始的主题。

- [The Technical Interview is an Ego Trip](https://web.archive.org/web/20221101193146/https://kowsheek.com/the-technical-interview-is-an-ego-trip/) - 从开发人员使用工作面试作为展示其优势的工具的轶事开始。然后作者详细介绍了一个合理的面试流程，尽量不浪费任何人的时间。

- [The Intangible Skills You Can't Interview For](https://staysaasy.com/leadership/2021/04/12/the-intangible-skills-you-cant-interview-for.html) - “1）直通蹩脚的任务；2）知道如何完成；3）知道如何开始；4）提供（和接收）对角反馈；5）利用无形资产的价值。”

- [Back-End Developer Interview Questions](https://github.com/arialdomartini/Back-End-Developer-Interview-Questions) - 灵感的重要来源。

- [Reverse interview](https://github.com/viraptor/reverse-interview) - 面试时要问公司的问题。作为经理，准备好回答这些问题。

- [Culture Queries](https://www.keyvalues.com/culture-queries) - 在求职面试中提出的问题示例，以试图了解公司的价值观。

- [Book Summary of "Who: The A Method for Hiring"](https://medium.com/mbreads/book-summary-who-c4a437d8ae3a) - [*Who*，流行的书](https://www.amazon.com/Who-Geoff-Smart/dp/0345504194?_encoding=UTF8&qid=1686402298&sr=1-1&li nkCode=ll1&tag=kevideld-20&linkId=d4a63bc5d11e6d00d942c293a640e2c1&语言=en_US&ref_=as_li_ss_tl)关于招聘高管。

- “确实，并非所有开发商都做出了积极贡献，但是，我认为指责“降低招聘标准”（……）完全是在转移注意力。” ([来源](https://news.ycombinator.com/item?id=13209317)) - 一些示例，其中可能很好地通过艰难工作面试的开发人员后来带来了负值。

### 编码挑战

缺乏编码练习将为欺诈敞开大门。 OTOH，如果精英挑战减少了误报的数量，那么您将传承完全有能力和伟大的开发人员。现在，作为经理，你的工作就是在这两个极端之间找到平衡，并为如何让候选人展示编码技能定下基调。

- [How to Freaking Find Great Developers By Having Them Read Code](https://web.archive.org/web/20230416055512/https://freakingrectangle.com/2022/04/15/how-to-freaking-hire-great-developers/) - “与其编写代码，不如考虑让应聘者阅读现有代码并谈论其工作原理。1）阅读代码占开发人员工作的 95%。2）应聘者可以在阅读的前五分钟内告诉你很多有关他们的编程技巧的信息。3）压力是你的敌人，因为它会提高肾上腺素，从而使智商降低几个百分点，导致你错过优秀的应聘者。”

- [Organizational Skills Beat Algorithmic Wizardry](https://prog21.dadgum.com/177.html) - “在编写代码时，最重要的技能是如何防止一堆功能因其自身复杂性而崩溃。”

- [The Horrifically Dystopian World of Software Engineering Interviews](https://web.archive.org/web/20210911031845/https://www.jarednelsen.dev/posts/The-horrifically-dystopian-world-of-software-engineering-interviews) - 过度依赖算法挑战的黑暗面。

- [Fizz Buzz Test](https://wiki.c2.com/?FizzBuzzTest) - “旨在帮助筛选出 99.5% 的编程求职者，他们似乎无法摆脱湿纸袋的编程方式。”

- [FizzBuzz 2.0: Pragmatic Programming Questions for Software Engineers](https://web.archive.org/web/20211020130141/https://triplebyte.com/blog/fizzbuzz-2-0-pragmatic-programming-questions-for-software-engineers) - 五个多项选择题可轻松将真正的软件工程师与其他工程师区分开来。

- [FizzBuzz Enterprise Edition](https://github.com/EnterpriseQualityCoding/FizzBuzzEnterpriseEdition) - 对为了企业级软件而过度设计的讽刺。

- [Awesome Interviews](https://github.com/MaximAbramchuck/awesome-interview-questions) - 庞大的问题数据库按主题排序，可从中获取灵感。

### 洽谈

结束招聘流程的关键一步。

- [How Not to Bomb Your Offer Negotiation](https://haseebq.com/how-not-to-bomb-your-offer-negotiation/) - “优秀的谈判者具有同理心和协作精神。他们不会试图控制你或发出最后通牒。相反，他们会尝试创造性地思考如何满足你和他们的需求。”

- [How to answer the “What's your current salary?” job interview question](https://web.archive.org/web/20190228034111/https://42hire.com/how-to-answer-the-whats-your-current-salary-job-interview-question-486254cb59ad?gi=a7f878096392) - 本文解释了这个偷偷摸摸的问题的动态以及如何化解它。

- [Salary Negotiation: Make More Money, Be More Valued](https://www.kalzumeus.com/2012/01/23/salary-negotiation/) - “你的薪资谈判通常需要不到 5 分钟的时间才能结束，这对你的薪酬有着巨大的影响。”

- [Ten Rules for Negotiating a Job Offer](https://haseebq.com/my-ten-rules-for-negotiating-a-job-offer/) - “第一部分将是关于谈判过程的概念化，关于如何开始这个过程并为自己取得最大的成功做好准备。第二部分将是关于谈判的实际来回部分以及如何提出你想要的东西的建议。”

## 入职

如何让新员工跟上你管理的团队的其他成员的步伐。以及如何向您刚刚加入或继承的团队介绍自己。

- [The Most Important Performance Management Rule For Software Engineers](https://staysaasy.com/startups/2022/04/03/performance-management.html) - “每周合并代码。这就是你应该对新聘用的软件工程员工说的话。”

- [Optimize Onboarding](https://staysaasy.com/management/2020/08/28/Optimize-Onboarding.html) - “你的组织的入职流程极其缓慢。无休无止的人力资源视频、缓慢的安全流程、堆积如山的脆弱技术设置——这些都会导致公司的开局糟糕且适得其反。优化你的入职培训，让人们做你雇佣他们做的事情。”

- [As a manager of a new employee I make an absolute point of being a "helicopter mom" from the moment they hit the area until about week 2 or 3](https://news.ycombinator.com/item?id=24404676) - 最初几周，驾驭新组织会很困难，而经理的存在可以帮助加快速度。

- [A Career Cold Start Algorithm](https://boz.com/articles/career-cold-start) - 作者开发了一种算法，可以在加入现有团队时快速提升，而他在该团队中知识匮乏且没有预先存在的关系。

- [Meeting everyone on a new team](https://www.annashipman.co.uk/jfdi/meeting-everyone.html) - 在继承了一个由 50 名工程师组成的组织的高层职位后，作者在 30 分钟内与每个人进行了一对一的会面，从而建立了与这个大团队的关系。这是一项巨大的时间投入，尽管担心会很无聊，但它可以让我们认识到需要进行哪些改变的模式。

## 动机

- [Drive: The surprising truth about what motivates us](https://www.youtube.com/watch?v=u6XAPnuFjJc) - 丹尼尔·平克（Daniel Pink）简洁地总结道：人们的动机是自主、掌握和目标。

- 反思上述假设，[Bryan Cantrill 定义管理的作用](https://x.com/bcantrill/status/1216491615264489473?s=20)“在于构建环境，而不是对其进行微观管理。如果工程性能受到影响，那么它（可能）是一个管理问题：错误的问题、错误的任务或错误的团队 - 或三者兼而有之。”

- [What Silicon Valley "Gets" about Software Engineers that Traditional Companies Do Not](https://blog.pragmaticengineer.com/what-silicon-valley-gets-right-on-software-engineers/) - “1. 软件工程师的自主权；2. 好奇的问题解决者，而不是盲目的资源；3. 内部数据、代码和文档透明度；4. 接触业务和业务指标；5. 工程师之间通过三角沟通进行沟通；6. 投资于减少令人沮丧的开发人员体验；7. 更高的杠杆 --> 更高的{自主性、薪酬}”。

- [Some reasons why enterprise software is good and maybe even fun](https://news.ycombinator.com/item?id=21231455) - 我们大多数人都不会建造下一个独角兽：我们静态地有更好的机会来构建企业软件。转折？它甚至可能比你想象的更有趣。

### 幸福

- [First, Break All the Rules: What the World's Greatest Managers Do Differently](https://www.amazon.com/dp/1595621113?&linkCode=ll1&tag=kevideld-20&linkId=cc8ac8de84cb23f23ca5577dcb7af139&language=en_US&ref_=as_li_ss_tl) - 我们从这本书中了解到，员工的幸福感与公司的成功无关。 HN 上的评论详细介绍了[与公司成功高度相关的问题](https://news.ycombinator.com/item?id=20571219)。

- “我的团队将生活影响作为一个指标（工作时间以外的页面）进行跟踪，并努力将其降至零。” ([来源](https://x.com/dwc/status/962179099606200320)) - 也许一个快乐团队的最佳指标是在办公时间之外很少受到干扰。

- [6 Signs You're a Micromanager (And What to Do Instead)](https://unito.io/blog/micromanagement-signs/) - “你比以往任何时候都更多地与员工打交道，但他们似乎不满、不快乐，工作效率也比平时低。你的签到似乎不受重视。似乎没有人接受你对他们工作的所有出色反馈。发生了什么事？好吧，我们不想向你透露，但你可能是一个事无巨细的管理者。”

### 拖延症

- [3 tricks to start working despite not feeling like it](https://www.deprocrastination.co/blog/3-tricks-to-start-working-despite-not-feeling-like-it) - “‘管它的，让我们开始吧’；开始草率；从小处开始”。

- [Why procrastination is about managing emotions, not time](https://www.bbc.com/worklife/article/20200121-why-procrastination-is-about-managing-emotions-not-time) - “研究表明，一旦朝着某项任务迈出了第一步，后续行动就会变得更容易”。

## 文化

- [hacker-laws](https://github.com/dwmkerr/hacker-laws) - 开发人员会发现有用的定律、理论、原则和模式。

- [Adaptation vs adaptability](https://sci-hub.st/10.1016/s0303-2647%2801%2900170-8) - 完美的效率和完全的灵活性之间存在着一定的界限。本文探讨了生态系统以及生态系统内不同生物体之间的物质和能量流动。 （[由 HN 评论暗示](https://news.ycombinator.com/item?id=20963513)）

- [The IT revolution and southern Europe's two lost decades](https://voxeu.org/article/it-revolution-and-southern-europes-two-lost-decades) - 如果您仍然怀疑管理文化能否成就或毁灭一个行业：“低效的管理实践使南欧企业无法充分利用 IT 革命”。

- [Meaningful differences that makes Google offices more productive](https://news.ycombinator.com/item?id=20443133) - “员工更聪明，你的经理（以及他们的经理）非常关心你，而且很容易调动。”

- [It's Not Enough to Be Right—You Also Have to Be Kind](https://archive.ph/RoW6v) - “善良比聪明更难”，或者亚伯拉罕·约书亚·赫舍尔（Abraham Joshua Heschel）换句话说：“当我年轻的时候，我常常钦佩聪明的人；随着年龄的增长，我钦佩善良的人。”

- “保护人们（特别是高级管理层）免受其决策后果的影响不是你的工作。根据你自己的最佳利益做出决定；组织有责任确保你的利益与他们的利益一致。” ([来源](https://news.ycombinator.com/item?id=7179946))。

- “如果你不能通过引入新文化来颠覆一种变态文化，那么变态文化的政治就会对你不利，直到你打破、结盟或离开。在你打破之前离开并不是不明智的，在你结盟之前离开更容易。” ([来源](https://news.ycombinator.com/item?id=20914779)) - 在某一时刻，即使有最无私的意图，你提升文化的尝试也可能会停滞不前。这不公平，但也许是时候离开了。

- [You have only 4 options](https://news.ycombinator.com/item?id=16126082) - “1.改变你；2.改变他人；3.飞翔；4.留下来受苦。”与上面相同的事情的更简洁的表达方式。

- [Netflix Culture](https://www.slideshare.net/reed2001/culture-1798664) - “与那些听起来不错的价值观相反，真正的公司价值观是通过谁得到奖励、晋升或解雇来体现的。”

- [High Performance Organizations Reading List](https://github.com/pdfernhout/High-Performance-Organizations-Reading-List) - 关于如何设计更好的组织的书籍、网页和视频列表，分为 3 类：组织和动机、健康和保健以及特定于软件开发。

- [A Conversation with Werner Vogels, Learning from the Amazon technology platform](https://queue.acm.org/detail.cfm?id=1142065) - 扩展系统不仅仅是一个技术挑战。它还必须与团队和文化有关。从 AWS 早期学到的一个教训是：“从客户和技术的角度来看，赋予开发人员运营责任极大地提高了服务质量。（……）你构建它，你运行它。”

- [The principles of Amazon service-oriented collaboration](https://www.theregister.com/2019/05/14/amazons_away_teams/?page=2) - AWS 匿名消息来源的汇编与上面的采访相呼应：“团队表面上是自治的，可以做出实现其目标所需的任何重要决策。”

## 认知工具

用于改进决策、理解系统和解决问题的思维框架和心智模型。

### 收藏

广泛的知名模型和概念列表。

- [Gigerenzer's simple rules](https://www.foundingfuel.com/article/gigerenzers-simple-rules/) - 我们经常依赖这些简单启发式的原因是：“在实验室之外，在现实世界中，我们不能仅凭逻辑理性做好事，我们需要生态理性——这种思维可以帮助我们在不确定和动态的环境中获得我们想要的东西。这意味着运用我们的直觉，使用简单但强大的经验法则。”

- [The Best Way to Make Intelligent Decisions](https://fs.blog/mental-models/#military_and_war) - 共有 109 个模型的集合。

- [Mental Models I Find Repeatedly Useful](https://medium.com/@yegg/mental-models-i-find-repeatedly-useful-936f1cc405d#.qb3gkdmtk) - 大量的心理模型汇编列表。成为本书的基础。

- [Tools for better thinking](https://untools.co) - 🆓“帮助您解决问题、做出决策和理解系统的思维工具和框架的集合。”

- [A Few Rules](https://www.collaborativefund.com/blog/a-few-rules/) - 您可能在其他地方遇到的一些智慧的正式列表。

- [Awesome Concepts](https://github.com/lukasz-madon/awesome-concepts) - 法律、原则、心理模型和认知偏差。

- [UX Core](https://keepsimple.io/uxcore) - 105 种认知偏差，带有简单的描述、简短而详细的示例。

### 解释

- [Hanlon's razor](https://en.wikipedia.org/wiki/Hanlon%27s_razor) - “永远不要把可以用愚蠢充分解释的事情归因于恶意。”我最喜欢的[奥卡姆剃刀](https://en.wikipedia.org/wiki/Occam%27s_razor)的味道，以及在高度政治环境中化解猖獗的偏执的关键咒语。

- [Regression toward the mean](https://en.wikipedia.org/wiki/Regression_toward_the_mean) - 或者为什么在一段强烈的欣快感和野心之后，事情会慢慢恢复到平常的平庸状态。

- [Locus of control](https://en.wikipedia.org/wiki/Locus_of_control) - 一个关于“人们相信自己能够控制生活中事件结果的程度，而不是无法控制的外部力量”的框架。

### 解决问题

- [First principles and asking why](https://www.theengineeringmanager.com/growth/first-principles-and-asking-why/) - “我们的抽象思考能力会削弱我们的判断力，因为这些抽象可能不再像以前那样真实。同样危险的进化特征是我们的类比思考能力，即我们根据两个实际上不相关的事物的比较做出假设。” [埃隆·马斯克对此做了更好的解释](https://www.youtube.com/watch?v=NV3sBlRgzTI)。

- “擅长软件设计的人相信，由于他们卓越的分析能力，他们拥有从基本原则出发理解任何类型系统的独特能力，无需事先培训。在人为构建的软件设计世界中取得成功会助长危险的自信。” - [来自科技道德经济小组](https://idlewords.com/talks/sase_panel.htm)，提醒我们行业中需要谦逊并认识到局限性。

- [The Art of Powerful Questions - Catalyzing Insight, Innovation, and Action](https://www.betterevaluation.org/sites/default/files/the-art-of-powerful-questions.pdf) - “领导者认为，他们获得报酬是为了解决问题，而不是为了培养突破性思维。”

### 系统

- [To Get Good, Go After The Metagame](https://commoncog.com/blog/to-get-good-go-after-the-metagame/) - “每一个足够有趣的游戏上面都有一个元游戏。这是关于游戏的游戏。它通常被称为‘元’。（……）元是你掌握了无聊的基础知识后所得到的。但是观察当前元的状态通常会揭示你需要学习哪些无聊的基础知识。”

### 头脑风暴

- [Yes, and…](https://en.wikipedia.org/wiki/Yes,_and...) - “即兴喜剧的经验法则（……）。它也被用于商业和其他组织，作为提高头脑风暴过程有效性、促进有效沟通并鼓励自由分享想法的原则。”

- [Strong Opinions, Weakly Held — a framework for thinking](https://medium.com/@ameet/strong-opinions-weakly-held-a-framework-for-thinking-6530d417e364) - “让你的直觉引导你得出结论，无论多么不完美——这是‘强烈意见’部分。然后——这是‘弱坚持’部分——证明自己是错的。”

### 行为方面

- [Programmer Interrupted](http://blog.ninlabs.com/2013/01/programmer-interrupted/) - 研究表明，打断开发人员的破坏性影响： 1. 需要 15 分钟才能恢复工作； 2. 程序员一天只能进行一次不间断的2小时会话； 3. 最糟糕的中断时间：编辑、搜索和理解期间。

- “如果人们生气、害怕或有压力，就会做出错误的选择。” - [迪士尼《冰雪奇缘》](https://web.archive.org/web/20250123004447if_/https://i.pinimg.com/originals/b5/17/97/b5179700050b96f91f63e086e053b5ee.jpg)。

- [I coached CEOs, founders, VCs and other executive: These are the biggest takeaways](https://leowid.com/2019-2) - 摘录：“我们都是大而复杂的情感袋；权力伴随着接受拒绝的能力；学会管理你的注意力，而不是你的时间。”

- [Intellectual Humility Cheat Sheet](https://web.archive.org/web/20200526135036/https://images.squarespace-cdn.com/content/v1/53419b80e4b0cccdfc3bbcf8/1579371627532-SANUEQ1REPX09L8NE1XM/ke17ZwdGBToddI8pDm48kI9Q46LYBJG1wKj9b7EvhSB7gQa3H78H3Y0txjaiv_0fDoOvxcdMmMKkDsyUqMSsMWxHk725yiiHCCLfrh8O1z5QHyNOqBUUEtDDsRWrJLTmWp-RWlGnWD_Yv5axNBE_gjfhPXbI2t7MOi3WVleCqN9URFC-c33mY-I6dtTBVWXC/ih-cheat-sheet-v2.jpg) - “就是要保持开放态度，能够改变对重要事情的看法，并能够辨别何时应该这样做。”

- [Avoiding Intellectual Phase Lock](https://books.google.com/books?id=__CnDwAAQBAJ&lpg=PT21&dq=intellectual%20phase%20lock%20Frank%20Dunnington&pg=PT21#v=onepage&q=intellectual%20phase%20lock%20Frank%20Dunnington&f=false) - 由于对重要结果的期待如此之高，人类本质上很容易引入微妙的确认偏差。为了对抗 IPL，您可以引入随机未知数来抑制任何将系统引向您想要的目标的企图。 IE。避免欺骗自己走向成功。

- [The six ways to influence people](https://www.bakadesuyo.com/2013/06/robert-cialdini-influence/) - 用于说服商业专业人士的 6 条普遍影响力原则：互惠、一致性、社会证明、让人们喜欢你、权威和稀缺性。

- [On Bullshit](http://ruby.fgcu.edu/courses/twimberley/EnviroPhilo/bullshit.pdf) - 这个[HN评论](https://news.ycombinator.com/item?id=23147605)完美地描述了这个概念。 “与谎言/欺诈不同，谎言是有帮助的，法兰克福将废话定义为潜在的虚假言论，而事实*根本不重要*。废话的特点是给人信心、智慧或令人信服的论据的“表面表现”；它是否真的真实与否并不重要。”

## 团队动态

关于团队的日常动态以及与其他团队的互动。

- [How to Celebrate the Small Wins](https://web.archive.org/web/20190714235605/https://medium.dave-bailey.com/how-to-celebrate-the-small-wins-4a03004a1816?gi=90c401bc3fd1) - 我的收获是：“庆祝缓慢的进展；寻找关键里程碑”。

- [Team Leader Venn Diagram](https://larahogan.me/blog/team-leader-venn-diagram/) - “获得对责任的共同理解的工具”。

- [When your coworker does great work, tell their manager](https://jvns.ca/blog/2020/07/14/when-your-coworker-does-great-work-tell-their-manager/) - 公开强调看不见的工作可以让管理者认识到他们的报告正在做的工作。尽管如此，在某些情况下，这可能会让你的同事陷入困境。所以总是先问一下是否可以。

- [Eye Candy QA](https://techreflect.net/2020/01/05/eye-candy-qa-2005-2011/) - 重述作者在苹果的工作经历：“约翰·卢奇是我的老板。（……）约翰总是与我们分享一切，甚至是“不要与你的团队分享这个”的东西。我们是他信任的人，所以这是应该的。这让你感觉自己是更伟大事业的一部分。”或者为什么分享一些公开的秘密可以促进对你的随行人员的强烈信任。

- [The Apollo Syndrome](https://www.teamtechnology.co.uk/tt/t-articl/apollo.htm) - 梅雷迪思·贝尔宾 (Meredith Belbin) 博士发现了这一现象，并在他 1981 年的《管理学书籍》中揭露了这一现象团队](https://www.amazon.com/dp/1856178072?&linkCode=ll1&tag=kevideld-20&linkId=486a53a41992fa334ccd6de4b3f689e1&language=en_US&ref_=as_li_ss_tl)，由高能力个人组成的团队集体表现可能很差。

- [A conversation with Elon Musk about Starship](https://youtu.be/cIQ36Kt7UVg?t=203) - 在一个拥有非常有才华的贡献者的团队中，每个人都是首席工程师：您应该挑战现状并质疑其他部门的限制。这使得聪明的工程师能够避免陷入优化那些本来就不应该存在的东西的陷阱。可能是治疗阿波罗综合症的方法。

- [Symptoms of Groupthink](https://web.archive.org/web/20210925184712/https://courses.washington.edu/psii101/Powerpoints/Symptoms%20of%20Groupthink.htm) - 过度自信、狭隘视野和从众压力可能会让团队误入歧途。

- [It's Not Sabotage, They're Drowning](https://shermanonsoftware.com/2019/11/15/its-not-sabotage-theyre-drowning/) - 某种推回不应被解释为故意破坏，而应被解释为溺水者为了自救而沉没救生艇。

- “社区已经存在，你只需为其创建一个交流平台”（[来源](https://news.ycombinator.com/item?id=21828666)） - 或者为什么尝试从头开始创建社区可能不是看待事物的正确方式：更好、更微妙的策略是增强现有渠道的能力并使它们可见。

## 工程

你不再是工程师了。尽管如此，您的团队仍要对系统、技术以及围绕它们的所有流程负责。你最好了解一点工程原理。

### 技术工程经理

你不应该把时间花在编码上。把这个事情留给工程师吧：你的价值现在在别处了。但这是否意味着你必须忘记所有技术性的事情？答案是令人震惊的*不*。以下是一些论点：

- [Do engineering managers need to be technical?](https://increment.com/teams/do-engineering-managers-need-to-be-technical/) - 是的。 “展望未来30年的管理趋势，只有几件事似乎是确定的：管理者应该是技术型的，而技术型的定义将不断变化。”

- [If Your Boss Could Do Your Job, You're More Likely to Be Happy at Work](https://archive.ph/J2vlo#selection-1025.8-1025.64) - “虽然我们发现许多因素对工作幸福感很重要——例如职业类型、教育水平、任期和行业也很重要——但它们甚至不如老板的技术能力那么重要。”

- “我遇到的最好的经理往往是那些如果情况需要，可以完成以下两个级别的工作的人。” ([来源](https://news.ycombinator.com/item?id=23891984)) - 另一种说法：管理者需要领域知识并了解他们的报告所做的工作。

- “多年来，我们制定了一项政策，即主管彻底了解和了解其团队的工作非常重要。” ([来源](https://news.ycombinator.com/item?id=20683609)) - 这句话是[来自大卫Packard](https://www.amazon.com/HP-Way-Hewlett-Built-Company/dp/0887307477?_encoding=UTF8&qid=1686404404&s r=1-1&linkCode=ll1&tag=kevideld-20&linkId=e6069674f9b0b4ef884b0f8f70eb8f94&语言=en_US&ref_=as_li_ss_tl) （惠普联合创始人），比当前的[管理时尚](https://en.wikipedia.org/wiki/Management_fad)早了几十年。

### 系统复杂性

无论技术堆栈如何，我们首先要构建系统，并且必须管理其复杂性。

- [Second-system effect](https://en.wikipedia.org/wiki/Second-system_effect) - “小型、优雅且成功的系统往往会被过度设计、臃肿的系统所取代”。

- [Living with Complexity, by Donald A. Norman](https://www.amazon.com/Living-Complexity-Donald-Norman-2010/dp/B00DEKM5GK?_encoding=UTF8&qid=1686404524&sr=1-1&linkCode=ll1&tag=kevideld-20&linkId=497ae387bbd398624d897bdfbf90f7b6&language=en_US&ref_=as_li_ss_tl) - 其中我们了解到，根据[特斯勒复杂性守恒定律](https://en.wikipedia.org/wiki/Law_of_conservation_of_complexity)，“系统的总复杂性是一个常数：当你使人的交互变得更简单时，幕后隐藏的复杂性就会增加。特斯勒说，让系统的一部分变得更简单，系统的其余部分就会变得更加复杂。”

- [The Efficiency-Destroying Magic of Tidying Up](https://flocrivello.com/the-efficiency-destroying-magic-of-tidying-up/) - “效率往往看起来很混乱，漂亮的外表往往效率低下。”提醒我们，有时我们应该接受[世界的混乱](https://github.com/kdeldycke/awesome-falsehood)。

- [I try to optimize my code around reducing state, coupling, complexity and code, in that order](https://news.ycombinator.com/item?id=11042400) - 工程师对于应该首先解决哪些优先级以提高系统稳健性的观点。

- [SpaceX's 5-Step design and manufacturing process](https://www.youtube.com/watch?v=t705r8ICkRw&t=13m30s) - “1. 减少需求的愚蠢；2. 尝试删除部分；3. 简化或优化；4. 加快周期时间；5. 自动化”。请参阅[完整文字记录](https://news.ycombinator.com/item?id=28517976)。

### 技术

- [Choose Boring Technology](http://boringtechnology.club) - “无聊，是因为它很好理解。”

- [Choose Well-known Technology](https://news.ycombinator.com/item?id=23445535) - 对上述建议的改写。 “选择技术：1. 你了解透彻，并且可以立即高效使用；2. 肯定会在 5-7 年内出现，最好是 10-15 年；3. 为此你可以放心雇用接下来的 15 名工程师。”

- [Industry Data Models](https://web.archive.org/web/20220330034214/http://databaseanswers.org/data_models/) - Barry Williams 在 25 年来收集的庞大数据库模板列表可以代表任何业务流程。

- “很多人错误地认为只有两个向量可以提高性能，高或宽。高 - 在一台机器上抛出硬件来解决问题。宽 - 添加更多机器。[还有第三个方向，我称之为*深入*。](https://news.ycombinator.com/item?id=8902739)”

- [You need to be this tall to use (micro) services](https://news.ycombinator.com/item?id=12509533) - 不要追逐炒作。然而。微服务只能带来超过一定基础设施和组织规模的价值。这是在将微服务引入混合之前应该关注的事项列表。

- [LEGO blocks and organ transplants](https://www.johndcook.com/blog/2011/02/03/lego-blocks-and-organ-transplants/) - “几十年来，人们一直在将软件组件与乐高积木进行比较。（……）集成两个软件系统通常更像是进行心脏移植，而不是将乐高积木拼装在一起。”

- “软件开发更类似于工业生产的产品设计和开发阶段，而不是制造。” ([来源](https://accu.org/bookreviews/1998/kloss_1668/)) - 此引用来自对 [*Superdistribution - 对象作为电子财产的评论] Frontier*](https://www.amazon.com/dp/0201502089?&linkCode=ll1&tag=kevideld-20&linkId=dc65849a678d52afa9f3685159673d6e&language=en_US&ref_=as_li_ss_tl)，其中 Objective-C 的创建者在 90 年代提倡一个新的经济框架，根据组件的使用情况奖励组件的创建。但软件生产不同于工厂中的小部件制造。 [（软件）对象不是（硬件）小部件](https://x.com/kdeldycke/status/1697974273623675254)。

### 工程实践

- [Software Engineering's Greatest Hits](https://www.youtube.com/watch?v=HrVtA-ue-x0) - 当科学方法满足软件开发实践。我的结论是：最好的指标是更少的代码行，没有 10 倍的开发人员，太多未使用的配置选项，结对编程是为了传输特定领域的知识，而黑客马拉松不会产生长期项目。

- [Code reviews at Google](https://github.com/google/eng-practices/blob/master/review/reviewer/speed.md#why-should-code-reviews-be-fast-why) - “为什么代码审查应该很快？（……）为了优化开发团队一起开发产品的速度，而不是优化单个开发人员编写代码的速度。”

- [Google Engineering Practices](https://google.github.io/eng-practices/) - 解释如何执行代码审查以及如何提交代码审查。

- [Embedded Rules of Thumb](https://embeddedartistry.com/blog/2018/04/26/embedded-rules-of-thumb/) - 在开发嵌入式设备时提供合理的近似事实的指南和启发式方法。大多数也适用于一般软件项目。

- [How to Misuse Code Coverage](https://web.archive.org/web/20180508120159/http://www.testingeducation.org/BBST/foundations/Marick_coverage.pdf) - “如果测试套件的一部分在覆盖范围可以检测到的方面很弱，那么它也可能在覆盖范围无法检测到的方面也很弱。” IE。覆盖率报告的最大好处是，它可以告诉您在编写测试套件本身时忘记考虑的内容（[来源](https://news.ycombinator.com/item?id=28678098)）。

### 技术债务

- [Tech Due Diligence Calculator](https://decodingvc.gitbooks.io/p9-startup-tech-due-diligence-calculator/content/) - 按主题列出的问题列表，可帮助您了解如何构建技术和工程团队，并试图突出危险信号。

- [Technical Debt Is Like Tetris](https://web.archive.org/web/20190313164624/https://medium.com/@erichiggins/technical-debt-is-like-tetris-168f64d8b700) - 另一种解释技术债务的方式是：“像这样的场景会在产品代码中产生技术债务。俄罗斯方块中隐藏的差距代表技术债务。（……）偿还技术债务可以让你保持竞争力。它可以让你留在游戏中。”

- [Technical debt as a lack of understanding](https://daverupert.com/2020/11/technical-debt-as-a-lack-of-understanding/) - “问题在于“永远不要重新组织（代码）来反映你的理解。”（……）从组织上来说，你付出的代价是速度和人员流动；有才华的人在几轮废话之后就会离开。

- [The Framing of the Developer](https://www.amazingcto.com/develop-for-impact-not-for-backlog/) - 默认框架是围绕积压的，这导致了一种不对称，即失败被归咎于开发人员绩效的缺乏，而成功则被庆祝为 PM 愿景的完全实现。但“技术是提供信用的银行”，技术债务应该称为产品债务，“因为产品获得信用是为了更快地获得某个功能，并且必须通过投入时间进行清理来偿还。”另一种选择？ “当今的公司需要一个具有影响力的框架。在这种世界观中，成功是由影响力来定义的。”

- [Goodbye, Clean Code](https://overreacted.io/goodbye-clean-code/) - “我的老板邀请我进行一对一的聊天，他们礼貌地要求我恢复我的更改。我惊呆了。旧代码一团糟，而我的代码很干净！（……）我现在看到我的‘重构’在两个方面是一场灾难：我没有与编写它的人交谈；我的代码用更改需求的能力来减少重复”。

## 远程工作

- [The Surprising Traits of Good Remote Leaders](https://www.bbc.com/worklife/article/20200827-why-in-person-leaders-may-not-be-the-best-virtual-ones) - “长期以来推动雄心勃勃的员工进入高管层的自信、智慧和外向在网上是不够的，因为它们根本无法转化为虚拟领导力。（……）相反，有组织、可靠和高效的员工掌控着虚拟团队。”正如[源论文](https://link.springer.com/article/10.1007/s10869-020-09698-0)说得最好的那样：“实际上，重点从说转移到了做。”

- [Things to look for when hiring remote workers](https://news.ycombinator.com/item?id=17022563) - “1. 您必须遵守招聘所在国家/地区的就业法；2. 要雇用全职员工，许多国家/地区要求您在该国家/地区拥有合法实体；3. 优先考虑我们最感兴趣的国家/地区；4. 在我们的每个团队中保持健康的时区重叠。”

- [Managing Remote Teams - A Crash Course](http://klinger.io/post/180989912140/managing-remote-teams-a-crash-course) - 编译简单的规则和流程来引导远程团队。

- [GitLab's Guide to All-Remote](https://about.gitlab.com/company/culture/all-remote/guide/) - “GitLab 是世界上最大的全远程公司”。这是它的含义及其工作原理。

- [Asynchronous Communication: The Real Reason Remote Workers Are More Productive](https://web.archive.org/web/20250506052542/https://async.twist.com/asynchronous-communication/) - “远程工作者比办公室里的同事更有效率。”

- [A guide to distributed teams](https://increment.com/teams/a-guide-to-distributed-teams/) - 很好地总结了拥有一支高效的分布式团队所需的众多配置。

- [Awesome Remote Job](https://github.com/lukasz-madon/awesome-remote-job) - 有关远程工作的资源，包括招聘委员会、联合办公空间以及拥抱这种文化的公司列表。

## 会议

两个人 + 一个（虚拟）房间 = 一次会议。

- [Dear Manager, You're Holding Too Many Meetings](https://archive.ph/1P4FQ) - “当会议减少 40% 时，员工的工作效率提高了 71%。这主要是因为员工感觉自己更有权力、更自主。他们不再把日程表当老板，而是拥有自己的待办事项清单并对自己负责。”

- [How to have great meetings, according to 200 scientific studies](https://qz.com/work/1713662/how-to-have-great-meetings-according-to-200-scientific-studies/) - 正确召开会议的路线图。

- [Wadge's Law (of Meetings)](https://billwadge.wordpress.com/2019/03/24/laws-of-the-universe-and-teaching/) - “在每次正式会议之前，都会举行一次规模较小、更具排他性、不太正式的会议，所有重要决策都会在会议上做出。”

### 1对1

您将举行的最重要的会议是与您的直接下属进行的频繁的一对一会议。

- “一对一是管理者的瑞士军刀”（[来源](https://news.ycombinator.com/item?id=22341739)） - 来自消息来源的另一个建议：让他们边走边说。

- [Questions for our first 1:1](https://larahogan.me/blog/first-one-on-one-questions/) - 经理提出的高级问题的个人清单。

- [1 on 1 Meeting Questions](https://github.com/VGraupera/1on1-questions) - 这是一份庞大的清单，其中大多数都是很好的对话开端，而另一些则显然是糟糕的想法。尽管如此，这仍然是一个很好的灵感来源，但请谨慎选择。

### 站立会议

敏捷礼仪的主要内容，但经常被滥用。

- [Your daily standups should be async. Here's why](https://web.archive.org/web/20200515171636/https://www.cadencework.com/blog/async-standups.html) - “每日实时会议对于远程团队来说不切实际”可能是最好的实际原因。

- [The Good, the Bad and the Ugly Standup](https://kristoff.it/blog/good-bad-ugly-standup/) - 作者经历了 3 种形式的站立会议，最后以一种为他的团队工作结束，并得出结论：“构成一次良好会议的细节是微妙的，对人为审美标准的追求将阻止你进行必要的实验，以改善丑陋的平衡”。

- [We Cancelled Standups and Let The Team Build. Here's What Happened…](https://www.usehaystack.io/blog/we-cancelled-standups-and-let-the-team-build-heres-what-happened) - 团队因每天伪装成站立会议的冗长状态更新会议而感到精疲力尽。消除这些虚假的站立让团队重回正轨。

## 设施

我们工作的环境塑造了我们。还有福利。

- [The impact of the 'open' workspace on human collaboration](https://sci-hub.st/https://royalsocietypublishing.org/doi/full/10.1098/rstb.2017.0239) - 开放式办公室减少了面对面的协作。

- [Noise, Cognitive Function, and Worker Productivity](https://joshuatdean.com/wp-content/uploads/2020/02/NoiseCognitiveFunctionandWorkerProductivity.pdf) - “增加 10 dB 会使生产率降低大约 5%。”

- [The Elves Leave Middle Earth – Sodas Are No Longer Free](https://steveblank.com/2009/12/21/the-elves-leave-middle-earth-%E2%80%93-soda%E2%80%99s-are-no-longer-free/) - 公司停止提供免费苏打水。工程师们非常沮丧，但这只是苏打水，他们买得起。但实际上这不是苏打水。苏打水就像煤矿里的金丝雀，引发了最好的工程师的外流。

## 产品管理

产品经理应该是“市场的声音”。以下是有关该角色及其影响范围的更多链接。

- “你是许多非结构化信息的经纪人，必须抵御各种破坏性影响，才能到达甚至接近你想要去的地方。” ([来源](https://news.ycombinator.com/item?id=19050555))

- [Awesome Product Management](https://github.com/dend/awesome-product-management) - 一个参考。所有缺失的部分都在下面找到。

- [Open Product Management](https://github.com/tron1991/open-product-management) - 资源、访谈、案例研究、示例产品和项目、社区、开源工具、产品管理的免费和付费服务，供技术人员学习该领域。

- [Things Many People Find Too Obvious To Have Told You Already](https://archive.ph/vH4D1) - 一系列关于科技公司及其所处生态系统的启发式方法。

- [The Heilmeier Catechism](https://www.darpa.mil/work-with-us/heilmeier-catechism) - 一组简单的问题帮助 DARPA 评估研究项目，以通过承担大风险来获得丰厚的回报。

- [Akin's Laws of Spacecraft Design](https://web.archive.org/web/20250528080513/https://spacecraft.ssl.umd.edu/akins_laws.html) - 关于太空计划管理的很多智慧。

- [How to exit vim, the Product Manager way](https://github.com/hakluke/how-to-exit-vim/blob/master/README.md#the-product-manager-way) - 讽刺有一定道理，尤其是基础水平与经验水平之间的比较。

### 招聘 PM

关于面试 PM 职位。以及如何进行面试来评估产品经理的能力。

- [关于产品经理案例面试，每个人都应该了解什么](http://www.venturegrit.com/what-everybody-ought-to-know-about-the-product-manager-case-interview/)

### 产品与市场契合度

验证您的产品的第一步：市场对您的企业感兴趣吗？

- [I wasted \$40k on a fantastic startup idea](https://tjcx.me/posts/i-wasted-40k-on-a-fantastic-startup-idea/) - 一个打造没有用户愿意付费的产品的故事。 “你不能只为用户创造价值：这是慈善机构。你也不能只为你的公司创造价值：这是一个骗局。你的目标是建立某种正和交换，让每个人都受益，包括你。根据这本教科书，商业计划从这个简单的问题开始：你将如何为自己和公司创造价值？”

- [David Rusenko - How To Find Product Market Fit](https://www.youtube.com/watch?v=0LNQxT9LvM0) - “详细介绍了 Weebly 如何开发当今网络上最受欢迎的网站创建和托管网站之一的故事。”

- [Fundamentals of Product-Market Fit](https://www.holloway.com/s/rvc-fundamentals-of-product-market-fit) - 概念的完整概述：什么是产品市场契合度以及衡量它的方法。

### 产品策略

您的产品在价值链中的位置以及如何在市场中定位。

- [Sustainable Sources of Competitive Advantage](https://www.collaborativefund.com/blog/sustainable-sources-of-competitive-advantage/) - “比你的竞争对手学习得更快的能力；比你的竞争对手更能同情客户；比你的竞争对手更有效地沟通；比你的竞争对手更愿意失败；比你的竞争对手更愿意等待”。

- [Coglode: bite-size behavioral research analysis](https://www.coglode.com) - 主要应用行为洞察来帮助您制定产品、设计和规划的战略和策略。

- [“Why does the tire company rate restaurants”](https://mobile.x.com/trevmckendrick/status/1218748974321954816) - 这是一个很好的例子，说明为什么您应该调查互补业务。

- [Laws of Tech: Commoditize Your Complement](https://www.gwern.net/Complement) - 比之前的建议更进一步，其中详细介绍了巩固垄断的积极战略。

- Windows Vista 作为[牺牲羔羊产品](https://x.com/SwiftOnSecurity/status/851861076429991937) 的主要示例：需要进行大规模的不受欢迎的重新架构，为未来的创新版本铺平道路。这是一个警示故事，说明如果您偶然或命运地走上了商业软件发生巨大变化的道路，那么您应该准备好迎接激烈的批评和逆境。

- 谈到 Vista，微软在发布失败后发现[排名第一的错误预测器不是技术性的，而是组织复杂性](https://augustl.com/blog/2019/best_bug_predictor_is_organizational_complexity/)。

- [Osborne effect](https://en.wikipedia.org/wiki/Osborne_effect) - “一种社会现象，即客户取消或推迟当前即将过时产品的订单，这是公司过早宣布未来产品的一个意想不到的缺点。”这是仓促的营销行动所付出的代价。

- [Reverse Engineering A Successful Lifestyle Business](https://web.archive.org/web/20230129184848/http://www.toomas.net/2017/07/18/reverse-engineering-a-successful-lifestyle-business-heres-everything-ive-learned-from-reading-indiehackers-com/) - 目标是生活方式企业家，但仍然充满了有关客户关系、定价和产品营销的参考书中的精彩引言。

- [The Atlassian Syndrome](https://x.com/maikzumstrull/status/1309497246946406400) - 您的组织最终将使用 Atlassian 产品，因为“他们的业务模式是：1. 从客户和潜在客户那里收集需求列表；2. 确保他们的产品检查每一个该死的方框，无论多么愚蠢。”

- “线性路线图具有误导性”（[来源](https://x.com/PavelASamsonov/status/1296818042928861184)）。

### 以用户为中心的设计

关于如何关注用户的问题，让你的产品创造价值。

- [The product roadmap is dead: welcome to the age of problem roadmaps](https://medium.com/product-managers-at-work/the-product-roadmap-is-dead-welcome-to-the-age-of-problem-roadmaps-7c7745ac8ae0) - “爱上你的问题，而不是你的解决方案。”

- [Kasparov's Law](https://web.archive.org/web/20220120220730/https://curatedintelligence.wordpress.com/2017/10/20/kasparovs-law/) - 弱人类+机器>机器>强人类。

- [The Psychology of Design](https://growth.design/psychology/) - 认知偏见和设计原则的广泛列表，以及微调您的产品和用户体验的示例和技巧。

### 产品营销

如何寻找用户、扩大客户群并让人们谈论您的产品。

- [Marketing for Engineers](https://github.com/LisaDziuba/Marketing-for-Engineers) - 大量资源可帮助您启动营销活动并解决实际任务。

- [How the biggest consumer apps got their first 1,000 users](https://archive.ph/DggAq) - 最大的应用程序是如何开始的：从直接接触用户（在线和离线）、创造 FOMO 和口碑，到首先建立社区并获得媒体报道。

## 项目管理

如果产品管理是关于产品“开发什么”，那么项目管理活动的答案就是“如何”交付该开发。这一切都与执行有关，特别关注交付关键路径和规划。

但不用太担心，每个公司对这两个角色都有自己的定义，有时甚至是混合职位。

- [Let's have no managers, instead of managers with no engineering experience](https://medium.com/hackernoon/lets-have-no-managers-instead-of-managers-with-no-engineering-experience-e8b7cd29d398) - 标题具有误导性，文章的论点是：如果我们已经拥有*产品*经理和 scrum master，我们就不需要*项目*经理。

- [Best project management practices in 2018?](https://news.ycombinator.com/item?id=16377523) - 没有灵丹妙药。

- [Strategies for long Projects](http://benbrostoff.github.io/2019/09/28/long-projects.html) - 无情的、非理性的乐观；每日进度文档；复利投资；时间预算。

- [Developers can't fix bad management](https://iism.org/article/developers-can-t-fix-bad-management-57) - “为什么这么多软件项目失败？软件开发更接近于创建一个新工厂，而不是运营一个现有工厂。（……）软件开发由许多未知持续时间的任务组成，这种根本上不可预测的性质使得传统管理的预测性规划技术特别不适合软件项目。”

### 规格

- “如果两者都被冻结，那么在水上行走和根据规范开发软件就会很容易。” Edward V. Berard - [面向对象软件工程论文](https://www.amazon.com/dp/0132888955?&linkCode=ll1&tag=kevideld-20&linkId=559e579e5b00fde12559bbbb91ec1b95&language=en_US&ref_=as_li_ss_tl)。

- [The art of destroying software](https://www.youtube.com/watch?v=Ed94CfxgsCA) - Greg Young 描述了一种处理需求波动的好方法：从一开始就进行优化，以便能够删除代码，并构建代码，以便代码的任何部分都不超过 1 周的编码量。这样任何部分都可以在1周内重写。

- [Requirements volatility is the core problem of software engineering](https://stackoverflow.blog/2020/02/20/requirements-volatility-is-the-core-problem-of-software-engineering/) - “首先要接受变革是不可避免的。（……）因此，软件永远不会完成，而只是被放弃。（……）这意味着没有任何软件产品是完全令人满意的。”

### 估计

时间管理和计划从估计开始，但通常会退化为最后期限。

- [Don't (guess)timate your projects, forecast with confidence](https://www.reaktor.com/blog/forecasting-method/) - “花费大量时间进行估算的问题在于，它可能让人感觉很有用，但往往非常不准确，以至于几乎无法为业务带来多少价值。”我们能做的就是衡量和预测。

- [Dear Startup: You have no idea how much that costs](http://kyleprifogle.com/dear-startup/) - “我们完全不知道事情需要多长时间。”这是一个[处理不合理估计期望的技巧](https://news.ycombinator.com/item?id=21069178)。

- [Escalation of commitment](https://en.wikipedia.org/wiki/Escalation_of_commitment) - 又名沉没成本谬误，或者是对为什么我们仍然非理性地继续投资一个糟糕的项目的理性解释。

- [Who are you trying to impress with your deadlines?](https://archive.ph/9Hq7N) - “有些公司的最后期限是一成不变的，错过最后期限就会被解雇。这就是问题开始的时候。”

- [Apple Aperture: Senior QA](https://techreflect.net/2019/12/10/aperture-senior-qa-2004-2005/) - 如何不管理临近截止日期的项目：“削减已完成的功能，对人们大喊大叫，让人们工作到精神崩溃的地步。然后他们想到了一个绝妙的主意：让我们从其他团队挖走一百多名工程师，然后项目就会神奇地按时完成。”

- [Robert "Uncle Bob" Martin talk about professionalism in software development](https://youtu.be/LmRl0D-RkPU?t=3202) - 唯一诚实的估计是“我不知道”。但你可以提出某种概率评估，以了解风险的情况。这与 PERT 没有什么不同，其中活动受到[乐观、悲观和最有可能时间](https://en.wikipedia.org/wiki/Program_evaluation_and_review_technique#Time)的限制。现在，如果管理者不采取范围作为答案，就不要陷入这个陷阱。告诉他们你已经尽力了。 “然后经理将不得不做一些非常陌生的事情：他们必须进行管理。这就是管理：管理风险。”

- [Why software projects take longer than you think: a statistical model](https://erikbern.com/2019/04/15/why-software-projects-take-longer-than-you-think-a-statistical-model.html) - “证实了开发商对中位数的估计很好，但平均值最终要高得多的预感。”

- [Developers spend most of their time figuring the system out](https://lepiter.io/feenk/developers-spend-most-of-their-time-figuri-9q25taswlbzjc5rsufndeu0py/) - “关于当前系统的手绘图是一种信念。决策永远不应该基于信念。在工程中不应该。（……）由于软件与上下文高度相关，我们无法预测具体问题。我们只能预测问题的类别。”这就是为什么很难估计软件项目：因为开发人员的主要活动是扣除系统构建基础的假设的漫长过程。

- [Software effort estimation is mostly fake research](https://shape-of-code.com/2021/01/17/software-effort-estimation-is-mostly-fake-research/) - “NASA 数据集包含 93 行（这不是拼写错误，没有缺失 10 的幂），COCOMO 63 行，Desharnais 81 行，并且（……）中国数据集包含 499 行。”

### 门票

- [There Are No Bugs, Just TODOs](https://almad.blog/essays/no-bugs-just-todos/) - 问题跟踪器需要具体化所有权、队列位置、状态、任务分解和主动关闭。优先级、票证类型、软件版本、严重性和长寿命票证是反模式。

### 发货

- [How I ship projects at big tech companies](https://www.seangoedecke.com/how-to-ship/) - “交付是公司内部的一种社会结构。具体来说，这意味着当公司的重要人员相信项目已交付时，项目就已交付。”这是交付的阴暗面，您需要优化高层管理人员对下一个绩效评估周期的可见性。

## 敏捷

- [The SAFe Delusion](https://safedelusion.com) - 对来自非既得利益相关来源的事实、证据和意见进行有组织的审查，以帮助决策者做出明智的选择并获得更好的结果。

- [How Big Tech Runs Tech Projects and the Curious Absence of Scrum](https://newsletter.pragmaticengineer.com/p/project-management-in-tech) - 本文中有一个有趣的表格，介绍了公司的刻板印象、融资模式、主要工程参与者及其核心方法。

- [Why do some developers at Google consider Agile development to be nonsense?](https://archive.ph/pSUhM) - 因为专注于短期的 Scrum 流程“似乎适合特定类型的开发，尤其是咨询或合同编程，其中客户是组织外部的，他们负责管理，因为他们为开发付费，并且可以随时改变主意”。尽管如此，谷歌工程师已经实践了一种类似于最初的 10 点敏捷宣言的文化。但仅此而已。

- [Story Points Revisited](https://web.archive.org/web/20250604004212/https://ronjeffries.com/articles/019-01ff/story-points/Index.html) - 据称故事点的发明者表示，这可能是一个错误。

- [Detecting Agile Bullshit](https://web.archive.org/web/20250601171312/https://media.defense.gov/2018/Oct/09/2002049591/-1/-1/0/DIB_DETECTING_AGILE_BS_2018.10.05.PDF) - 美国国防部指南，用于检测真正使用敏捷开发的软件项目与那些披着敏捷外衣的瀑布式或螺旋式开发（“agile-scrum-fall”）的软件项目。

- “导致大多数敏捷失败的根本问题不在于团队的执行，而在于业务的期望。一方面是增量交付，一方面是固定的范围和截止日期，结果是痛苦的。” ([来源](https://news.ycombinator.com/item?id=20326074))

- [Failed #SquadGoals - Spotify doesn't use "the Spotify model" and neither should you](https://www.jeremiahlee.com/posts/failed-squad-goals/) - “为什么它不起作用？1. 矩阵管理解决了错误的问题；2. 它专注于团队自主权；3. 协作是一种假定的能力；4. 神话变得难以改变”。

- [Recurring opinions or productive improvements — what agile teams actually discuss in retrospectives](https://link.springer.com/article/10.1007/s10664-016-9464-2) - 对团队三年回顾的分析，得出了可怕的结论：人们不断忘记他们已经学到的东西，不断讨论他们无法控制的无法解决的问题，并不断基于偏见的解释或不正确的理解来争论观点。

## 关键绩效指标（KPI）

KPI 是团队或组织级别的一组定量衡量标准，用于衡量业务的成功。

- “为其他人设定的数字目标，如果没有实现目标的路线图，会产生与所寻求的效果相反的效果。” - [W.爱德华兹戴明](https://www.amazon.com/Out-Crisis-W-Edwards-Deming/dp/0911379010?_encoding=UTF8&qid=&sr=&li nkCode=ll1&tag=kevideld-20&linkId=ec7a442a2cd5bfcfb5b6c32ea1409f2f&语言=en_US&ref_=as_li_ss_tl)

- [SRE fundamentals: SLIs, SLAs and SLOs](https://cloudplatform.googleblog.com/2018/07/sre-fundamentals-slis-slas-and-slos.html) - 如果您从事云服务业务，这些指标无疑是很棒的 KPI。

- [The 4 Worst Software Metrics Agitating Developers in 2019](https://www.gitclear.com/blog/the_4_worst_software_metrics_agitating_developers_in_2019) - 跟踪软件团队输出的最差 KPI：代码行数、提交计数、已解决的问题（又名“交付速度”）和代码改动（又名“效率”）。

## 目标和关键结果 (OKR)

OKR 是一个框架。扩展 KPI，它们分别适用于组织的每个成员，直至 IC 级别。理论上，每个人都应该有自己的一套 OKR。

- [OKRs from a development team's perspective](https://archive.ph/dmASK) - 关于 OKR 如何与积压工作联系起来。

- [Team Objectives – Overview](https://svpg.com/team-objectives-overview/) - 为什么 OKR 可能不适用于您的公司： 1. 您仍在使用功能团队而不是产品团队； 2. 管理者和个人目标混淆； 3. 领导层选择退出主动管理。

- “我看到 OKR 有效使用的一种方式是作为对不断提出新想法或任务的中高层管理者类型的防御。” ([来源](https://news.ycombinator.com/item?id=19550614)) - 或者如何将 OKR 武器化以防止高层管理人员扰乱（已制定的）时间表。

- [Why individual OKRs don't work for us](https://web.archive.org/web/20250218070530/https://hrblog.spotify.com/2016/08/15/our-beliefs) - Spotify 决定停止对个人使用 OKR。

- [Google's usage of OKRs](https://news.ycombinator.com/item?id=17492038) - OKR 成绩是公开的，但不用于晋升。那里从来没有认真对待过这个问题。

- [Awesome OKR](https://github.com/domenicosolazzo/awesome-okr) - 关于如何衡量和传达目标的内容并不缺乏。

## 培训

关于指导、教育和学习。

- [Developers mentoring other developers: practices I've seen work well](https://blog.pragmaticengineer.com/developers-mentoring-other-developers/) - 讨论在工程师之间有效的指导实践。

- [What Medieval People Got Right About Learning](https://www.scotthyoung.com/blog/2019/06/07/apprenticeships/) - “为什么学徒制胜过课堂”。

- [Developer Roadmaps](https://roadmap.sh/roadmaps) - 💸 非常高水平的指南和学习不同实践和工具的路径。

## 通讯

它不仅仅是阅读、写作和交谈。它涵盖了团队活动的所有社会实践和背景共享。

尤其是软件团队，会产生大量的知识。所有这些知识都是脆弱的，即将永远消失。除非你把它具体化为书面形式。

### 知识

关于团队的知识。

- [What senior engineers do: fix knowledge holes](http://www.mooreds.com/wordpress/archives/3232) - “这是高级工程师的教科书定义。你看到一个问题，你（彻底）解决它，你记录它，然后你提升你的团队。”

- [Chesterton's fence](https://en.wikipedia.org/wiki/Wikipedia:Chesterton%27s_fence) - “如果你正在考虑提名删除某项内容，或更改某项政策，因为它似乎没有任何用途或目的，请首先研究其历史。”这并不是我们想保守，而是因为我们需要修复如上所述的知识漏洞。

- [You're Not Managing a Team of Software Engineers, You're Managing a Team of Writers](https://medium.com/coaching-notes/youre-not-managing-a-team-of-software-engineers-you-re-managing-a-team-of-writers-b263d3a10cc7) - 因为编写软件是“一个创造性的过程，本质上是不可预测的、个性化的，在一个渴望确定性、可预测性和一致性的环境中。”

### 阅读

在你知道如何写作之前，你需要知道如何阅读。

- [How to Read a Paper](http://svr-sk818-web.cl.cam.ac.uk/keshav/papers/07/paper-reading.pdf) - 概述了一种实用且高效的三遍阅读研究论文的方法。

### 文档

技术写作的各种形式、结构和目标受众。

- [What nobody tells you about documentation](https://www.divio.com/blog/documentation/) - 有四种文档：教程、操作指南、解释和参考。每个都有自己的结构和写作方式。

- [Flying Circus Platform - Disaster recovery](https://flyingcircus.io/doc/reference/security/disaster-recovery.html#disaster-recovery) - 旨在 24/7 全天候可用的关键基础设施需要一个[灾难恢复计划](https://en.wikipedia.org/wiki/Disaster_recovery)。它通常采用文档的形式，提供预期严重故障的概述以及关于系统和操作该系统的团队准备如何处理的一组程序。这里链接的文件就是此类文件的一个很好的例子，并且有力地证明了团队已经为最坏的情况做好了准备。

### 写作

关于如何通过掌握风格来传达含义和清晰度的一般建议。如果写得不好，您的文档的使用和实用性可能会很差。

- [How to Write a Technical Paper](https://pdfs.semanticscholar.org/441f/ac7c2020e1c8f0d32adffca697bbb8a198a1.pdf) - 作为如何以典型期刊出版物的形式撰写优秀技术论文的指南。

- [Learning Technical Writing Using the Engineering Method](https://www.cs.tufts.edu/~nr/pubs/learn.pdf) - 另一种方法是每周召开一次写作小组会议。收集反馈和经验的有趣动态。

- [Technical Writing Courses](https://developers.google.com/tech-writing) - 这一系列课程和学习资源旨在改进您的技术文档。了解如何规划和编写技术文档。您还可以了解技术作家在公司中的角色。

- [Algorithm for writing a scientific manuscript](https://sci-hub.st/https://iubmb.onlinelibrary.wiley.com/doi/full/10.1002/bmb.20329) - 指导手稿准备和完善的过程。

- [The Baldwin Formula for scientific writing: writing papers and reviews](https://people.clas.ufl.edu/jlichstein/files/Baldwin_Formula_for_writing_a_scientific_paper_and_reviewing_papers.pdf) - “撰写科学论文最有效的方法是在进行实验的同时进行写作”。

- [Ten simple rules for structuring papers](https://www.biorxiv.org/content/10.1101/088278v5.full.pdf) - “针对读者如何消费信息，我们提出了一组 10 条简单规则，帮助您理解论文的主要思想。”

- [Tips for Writing Technical Papers](https://cs.stanford.edu/people/widom/paper-writing.html) - 另一组技巧，特别是使用描述算法改进的技术论文的示例。

- [Write an Excellent Programming Blog](https://speakerdeck.com/pycon2016/a-jesse-jiryu-davis-write-an-excellent-programming-blog) - 关于制作精彩博客文章的结构和风格的提示。

- [Notes on Technical Writing](https://mkaz.blog/misc/notes-on-technical-writing/) - 编写文档时该做和不该做的有效列表。

### 风格

一旦您根据上述建议获得了正确的结构和内容，您现在就可以使用下面的工具复制编辑和微调您的风格。

- [Please don't say just hello in chat](https://nohello.net/en/) - 如果使用得当，交互式书面介质可以实现异步通信。

- [BLUF: The Military Standard That Can Make Your Writing More Powerful](https://www.animalz.co/blog/bottom-line-up-front/) - “BLUF 是军事通信缩写，代表“最前面的底线”，旨在提高报告和电子邮件的速度和清晰度。”

- [The Punctuation Guide](https://www.thepunctuationguide.com) - 关于如何（以及为什么）使用这些特殊字符的简单参考。

### 演讲

- [It's time to start writing](https://alexnixon.github.io/2019/12/10/writing.html) - 关于“杰夫·贝佐斯在亚马逊内部禁止使用 PowerPoint 的互联网时代政策”，以及“这既不是关于幻灯片，也不是关于阅读，而是关于思考”。

- [Presentation Rules](https://web.archive.org/web/20220720230551/http://www.jilles.net/perma/2020/06/05/presentation-rules.html) - 一组 16 条规则，可避免无聊和无效的演示，并使您的信息传达给受众。

- [The Greatest Sales Deck I've Ever Seen](https://medium.com/the-mission/the-greatest-sales-deck-ive-ever-seen-4f4ef3391ba0) - “1. 说出世界上的一个重大变化；2. 表明会有赢家和输家；3. 逗弄应许之地；4. 介绍“神奇礼物”等功能；5. 提供证据证明你可以让故事成真。”

- [Some tips on public speaking](https://news.ycombinator.com/item?id=6199544) - “如果你发现自己在输出时缓冲，而不是发出犹豫的声音，那就停下来。人们会认为这是深思熟虑和明智的。”

## 职业生涯

现在您已经证明了自己作为一线经理的价值，下一步是什么？这些文章探讨了后续角色，从管理经理到总监，以及介于两者之间的所有角色。

- [Work at different management levels](https://larahogan.me/blog/manager-levels/) - 逐步打破在不同管理级别工作的感觉。

- [Levels of abstraction in engineering management](https://medium.com/@rvprabhu/levels-of-abstraction-in-engineering-management-6bac9410e89a) - 关于经理、经理的经理、组织主管和职能主管之间差异的另一种看法。

- [My questions for prospective employers (Director/VP roles)](https://jacobian.org/2019/apr/23/questions-for-employers-director-vp/) - 准备好以招聘人员的身份询问他们，或被询问担任高级管理职位。

- [Founder to CEO](https://docs.google.com/document/d/1ZJZbv4J6FZ8Dnb0JuMhJxTnwl-dwqx5xl0s65DE3wO8/) - 你可以建立自己的职业引擎，从初创公司的技术创始人开始，建立一支优秀的团队，然后与公司一起成长，学习并成为一名成熟的首席执行官。

- [How title, money and scope affect your fulfillment](https://x.com/shreyas/status/1268372416427786240) - “对于有才华的职业中期人士来说，在换工作时，你会如何排序：1.头衔2.金钱3.范围”。

- [Amazon Wants to 'Win at Games.' So Why Hasn't It?](https://www.wired.com/story/amazon-wants-to-win-at-games-so-why-hasnt-it/) - “任何产品经理都可以在任何业务之间工作——从杂货到电影，从游戏到 Kindle。技能组合是可以互换的。他们只需要了解特定的市场。”

- “由于管理者不依赖于某个部门（就像护士或音乐家那样），所以好的管理者往往会去他们能得到高薪的地方，而坏的管理者最终会在他们至少得到一些钱的地方造成严重破坏。这也是 [Baumol](https://en.wikipedia.org/wiki/Baumol%27s_cost_disease) 的行动。” ([来源](https://news.ycombinator.com/item?id=20448929)) - 解释职业经理人才库如何分配到经济的各个部门。

### 促销

在公司晋升职业生涯的垫脚石是晋升。他们获得加薪、奖金和更多责任。

- [How do managers get stuck?](http://www.elidedbranches.com/2017/09/how-do-managers-get-stuck.html) - 确定阻碍经理晋升到下一个级别的情况。

- [The Evolution of Management: Transitioning up the ladder](https://queue.acm.org/detail.cfm?id=3350548) - 描述每个管理层的路径和期望。

- [If management isn't a promotion, then engineering isn't a demotion](https://charity.wtf/2020/09/06/if-management-isnt-a-promotion-then-engineering-isnt-a-demotion/) - 本文解构了为什么管理层最终被视为一种晋升，其新获得的特权和权力如何创造了一个隐性的等级制度，而这种等级制度又因损失厌恶而产生了不良激励。最后，唯一的出路就是改变组织的文化。

- [How to discipline overeager engineer](https://web.archive.org/web/20240914135841/https://workplace.stackexchange.com/questions/145709/how-to-discipline-overeager-engineer) - 成绩优异的人才正在寻求管理层晋升。管理层不认可努力。工程师感到不满，管理层正在寻求对他进行纪律处分。双方都表现出笨拙的糟糕情况的案例研究。

- “大多数人在 30 多岁时意识到声望是一场傻瓜游戏”（[来源](https://news.ycombinator.com/item?id=11833832)） - 不要仅仅为了头衔而追求晋升。

- [For all you future CTOs, consider your incentive schemes carefully](https://news.ycombinator.com/item?id=24463676) - 一项晋升计划标志着 Uber 卓越工程技术的终结，以及导致该公司官僚主义混乱的开始。

- [How to get promoted](https://archive.ph/nlUrG) - 愤世嫉俗的观点是：“机会主义者的职业建议是：忽略OKR，在你的决定的后果可以衡量之前就转换项目，表现得快乐和随和，把坏消息包装成缓慢系统调整的呼吁，不要让任何人看起来很糟糕，热情地执行仪式，比基线更快地增加员工人数，让工作发明自己，遵循管理时尚，避免严重失败，真诚地相信这一点。”

### 绩效评估

评论和绩效评估是行业解锁促销的工具。作为一名经理，您将为您的团队成员编写并使用它们，以获得他们应得的加薪。并像其他员工一样克服这些困难，以推进您的职业生涯。

- [Get your work recognized: write a brag document](https://jvns.ca/blog/brag-documents/) - 有这样一种想法，如果你在工作中表现出色，人们会（或应该！）自动认识到你的工作，并通过晋升/加薪来奖励你。在实践中，情况往往比这更复杂。

- [Incentive Pay Considered Harmful](https://www.joelonsoftware.com/2000/04/03/incentive-pay-considered-harmful/) - “激励（或贿赂）在工作场所根本行不通。（……）大多数软件经理别无选择，只能遵循现有的绩效评估系统。如果你处于这个位置，防止团队杀戮的唯一方法就是给团队中的每个人一个滔滔不绝的评估”。

- “如果你的绩效评估中有任何令人惊讶的事情，那么我作为一名经理就失败了。” （[来源](https://news.ycombinator.com/item?id=17249767))。

- “这就是我喜欢在 Netflix 工作的原因。我们没有绩效评估。人们认为你的表现从好到优秀，否则你就不会再在那里工作了。你与经理就绩效进行了持续的反馈循环，但没有任何正式的反馈。” ([来源](https://news.ycombinator.com/item?id=23861960))。

- “软件开发人员工作的系统比个体差异更能影响他们的表现。” （[来源](https://news.ycombinator.com/item?id=21972033)）。

## 补偿

这不仅涉及薪水，还涉及整个一揽子计划：股权、奖金、福利以及所有这些方面的交易。

### 薪资

- [levels.fyi](https://www.levels.fyi) - 💸 比较大型科技公司的薪资范围、薪酬图表和福利。

- [L8-L10 salaries at AWS](https://news.ycombinator.com/item?id=21823987) - \$M+ 薪酬方案的参考点。

- [Why new hires often get paid more than existing employees](https://web.archive.org/web/20250415095157/https://bloomberry.com/why-new-hires-often-get-paid-more-than-existing-employees/) - “为什么获得更高薪水的最好方法就是跳槽。”

- [工资永远不会永远保密。隐藏它们只会推迟不可避免的事情。](https://news.ycombinator.com/item?id=2439478)

### 股权

- “永远不要接受较低的工资来换取股权。” ([来源](https://news.ycombinator.com/item?id=21868845))

- [On VC funding and huge growth](https://news.ycombinator.com/item?id=17448035) - “初创公司需要退出策略。（……）这个想法是快速筹集资金，聘请经验丰富的人员提供辅助服务，并以某种方式开发应用程序，使其能够持续到 IPO。推迟 IPO 后的所有成本。”所以从这个角度来看，加入创业公司的唯一原因就是为了未来的意外之财。

- [Equity Compensation](https://www.holloway.com/g/equity-compensation) - 股票期权、RSU、工作机会和税收——详细的参考资料，包括数百种资源，从头开始解释，并随着时间的推移进行改进。

- “您可以立即在公开市场上出售股票的公共 RSU 非常棒。” （[来源](https://news.ycombinator.com/item?id=22386728)）。

## 政治

政治游戏就在权力与影响力的交汇处。如果它的性质和强度源自公司的核心文化和历史，那么不幸的是，你不可能避免它超过一定的层级。做好准备。

- [About corporate middle management](https://news.ycombinator.com/item?id=28336658) - “作为一家大公司的经理，你应该成为一个协调者。（……）你必须管理摩擦并努力让你的上级看起来很好。”

- “政治是中层管理者进行干扰和制造干扰的方式，以确保你无法看到他们的上方、周围或透过他们，并且他们背后更接近金钱的人也看不到你。” （[来源](https://news.ycombinator.com/item?id=22808280)）。

- [HiPPO FAQ](https://exp-platform.com/hippo/) - HiPPO 代表“最高薪者的意见”，这是功能失调文化的一个特征，在这种文化中，权力政治胜过数据。

- [The Prince](https://en.wikipedia.org/wiki/The_Prince) - 马基雅维利关于如何作为领导者获得荣誉和权力的想法。在公司中诉诸这种程度的政治肯定会导致文化变得剧毒，并导致组织各个层面的腐败和士气低落。

- [The Gervais Principle](https://www.ribbonfarm.com/the-gervais-principle/) - 基于《办公室》，对管理阶梯的愤世嫉俗、黯淡但仍然引人入胜的看法。

- [The 48 Laws of Power](https://www.amazon.com/dp/0140280197?&linkCode=ll1&tag=kevideld-20&linkId=bf129d7f7a3495a445cf2bf667d3d3c6&language=en_US&ref_=as_li_ss_tl) - 作者：罗伯特·格林。可以教你如何在高度政治化的组织中隐藏自己并发挥作用。

- [7 Rules of Power](https://www.amazon.com/Rules-Power-Surprising-but-True-Advice-Advance/dp/1637741227?_encoding=UTF8&qid=&sr=&linkCode=ll1&tag=kevideld-20&linkId=1a2a7107ccffa7b19e03cdb88e616daf&language=en_US&ref_=as_li_ss_tl) - 作者：杰弗里·普费弗。告诉你【如果职场成功是你唯一关心的事情，如何玩弄办公室政治】(https://news.ycombinator.com/item?id=39084979)。

- [Selectorate theory](https://en.wikipedia.org/wiki/Selectorate_theory) - “根据选举理论，三类人会影响领导人。这些群体是名义选举人、实际选举人和获胜联盟。（……）为了继续掌权，领导人必须维持他们的获胜联盟。”

- [Circulation of elite](https://en.wikipedia.org/wiki/Circulation_of_elite) - “政权更迭、革命等不是在统治者被自下而上推翻时发生的，而是在一个精英取代另一个精英时发生的。”

- [The Rules for Rulers](https://www.youtube.com/watch?v=rStL7niR7gs) - “聪明的关键支持者将始终关注权力的平衡，如果统治者在不断变化的联盟网络中成为失败者，他们就准备好改变效忠对象。（……）尽可能购买所有忠诚度，因为在各种独裁组织中，忠诚度就是一切。”

- “玩好游戏现在是首要和中心”（[来源](https://news.ycombinator.com/item?id=21925738))，或者为什么[实现大型职业目标的关键实践](https://nodramadevops.com/2019/12/key-practices-for-achiving-large-professional-goals/)缺少有关办公室政治的部分。

- [“Company I've worked for had manager who tried to ship features over the weekend with a ragtag team of developers who don't understand why that's a bad idea.”](https://news.ycombinator.com/item?id=22285123) - 催促经理的策略，以及公司如何对这种经理做出反应，决定了一个好的工作场所的成败。

- [Making Nice or Faking Nice? Exploring Supervisors' Two-Faced Response to their Past Abusive Behavior](https://onlinelibrary.wiley.com.sci-hub.st/doi/10.1111/peps.12424) - “想要培养高度真实的主管或组织氛围的组织应该寻求聘用象征性道德认同较低（或至少不是较高）的主管。”

- “高层管理人员所掌握的实际权力通常与其管理的组织规模成反比。” （来源：【评论】(https://news.ycombinator.com/item?id=20260498)关于【为什么大公司这么难拯救】(https://news.ycombinator.com/item?id=20260114))。

- “削减成本可以让你加薪。交付一个大项目是晋升的途径。” ([来源](https://news.ycombinator.com/item?id=21230771))

- “当你在新闻中读到有关你应该拥有的功能时，你就知道你的游戏失败了。” （[来源](https://news.ycombinator.com/item?id=20220484)）。一个团队与公众同时了解其路线图是一个明确的迹象，表明出现了问题。

- “在高度政治化的环境中，有两种创造变革的方法，一种是通过公开操纵，即为自己收集政治权力，然后运用它来实施变革，另一种是隐蔽操纵，即以足够微妙的方式实施变革，使政治有机体不会做出反应。（有时称为“触发抗体”）。” （[来源](https://news.ycombinator.com/item?id=5541517)）。

- [Power Bends Light](https://honkathon.com/2019-08-18-power-bends-light/) - “大多数初创公司的大多数事情都是永远火热的，但如果你能接受这一点，那就有很多值得喜欢的地方。众所周知，在一家快速发展的初创公司中，一个勤奋、有才华的人在公司领导层的支持下，往往可以很快获得令人印象深刻的头衔（或至少很多事实上的权力）。”

- “提拔某人然后解雇他是很常见的:)有时提拔比解雇更容易。” （[来源](https://news.ycombinator.com/item?id=21767734)）。

- [US spy manual has tips for coping with toxic bosses](https://qz.com/work/1717297/how-to-cope-with-a-toxic-boss-according-to-a-us-spy-manual-from-wwii/) - 源自二战时期的《简单破坏现场手册》(https://archive.org/details/SimpleSabotageFieldManual)，这是一本发现骚扰和士气低落行为的经典读物。

- [4 Clues to Identify a Destructive Leader](https://www.tilt365.com/the-tilted-edge/blog/post/toxic-leadership-destructive-characteristics-examples) - “1. 我是个大人物！2. 这一切都不是我的错！3. 照我说的做！4. 相信我；我永远不会错。”

- “麻省理工学院院长告诉我，终身教职与研究、生产力或优点无关。它与办公室政治和被所在部门喜欢有关。” ([来源](https://threadreaderapp.com/thread/1494369809538195456.html)) - 考虑从该行业转行？学术界的草并没有更绿。鉴于规模庞大，任何组织都会有其政治游戏。

## 重组

作为经理，您对团队的结构负有直接责任。超过一定规模（大约 8 到 12 个，具体取决于来源），您不再有时间使用直接 IC，因此您需要重新组织团队。

在公司层面，重组主要是战略性的，你对重组的影响取决于你的政治敏锐度。

### 团队层面

- [Why it's difficult to build teams in high growth organisations](https://jchyip.medium.com/why-its-difficult-to-build-teams-in-high-growth-organisations-e1aee8446337) - 描述了经理可以采取的 3 种不同方法来适应团队中的新成员： 1. 沉没或游泳； 2. 分裂和吸收； 3.吸收和分裂。

- [Teams are like bread](https://blog.jessitron.com/2019/06/15/teams-are-like-bread/) - 与上面讨论的*吸收和分裂*策略产生共鸣：“如果你有一支魔力蓬勃发展的球队，不要杀死它。喂养它，培养它，让它成为更多强大团队的源泉。不要着急。”

- [Building a data team at a mid-stage startup: a short story](https://erikbern.com/2021/07/07/the-data-team-a-short-story.html) - 一位经理试图提炼数据驱动型公司的概念，同时组建一个由 3 人组成的小团队的故事。每个步骤都涵盖了技术管道的演变以及与现有利益相关者的互动。

- [If I Close My Data Centers, What About the People/Jobs Lost?](https://news.ycombinator.com/item?id=17329028) - F50 的数据中心正在迁移到商业云提供商。但那些目前从事遗留工作的人呢？答案是：重新训练。

- “这是管理主义的梦想。用流程和管理方法取代员工的判断和能力。（……）它永远不会奏效。” （[来源](https://news.ycombinator.com/item?id=20881308))。为什么上面的再培训答案是最好的答案。

- [I've Built Multiple Growth Teams. Here's Why I Won't Do It Again.](https://conversionxl.com/blog/dont-build-growth-teams/) - “很少有人了解概率，而且大多数高管并不关心数据，无论数据怎么说。”

### 公司级

- [The SaaS Org Chart](https://archive.ph/vOuLQ) - 组织在其 50/125/400/1000 名员工阶段的每个阶段的蓝图，以及典型比率和 ARR。

- “如果你曾与大型的、完全无能的组织打过交道，并且想知道他们到底是如何继续运转的 - 这就是你的答案。如果构建正确，真的很难把事情搞砸。” （[来源](https://news.ycombinator.com/item?id=20533922)）。 IE。组织的结构对其长寿至关重要。

- [A high-resilience org chart](https://jessitron.com/2021/05/26/a-high-resilience-org-chart/) - “如果你知道要解决什么问题并且知道如何解决它，那么官僚组织就可以做到。坚持你所知道的。如果你正在编写软件，那就是一项生成活动。你需要一个高弹性的组织结构图。更少的框，更多的灵活性。”

- [An Alternative Approach to Re-Orgs At Your Company](https://caseyaccidental.com/alternative-approach-re-orgs/) - “为了避免重复重组错误，我们开始研究一种结构，使重组就像由团队而不是上级人员驱动的反馈推动的进步一样。”这是一种从头开始提取指向结构不完善的信号的尝试。我的警示故事：这可能只能在一定程度上发挥作用，具体取决于公司的文化。

- “当一切都取得巨大成功时，成功背后的人会为未来可能取得成功的人留下阴影。（……）Netflix 是如何正确进行大转型的一个很好的例子。Netflix 从事通过邮件租赁 DVD 的业务。当决定转向流媒体时，Netflix 首席执行官不允许负责 DVD 租赁业务的经理参加计划未来的会议。” （[来源](https://news.ycombinator.com/item?id=21395557)）。

- [Speaking Truth to Power: Reflections on My Career at Microsoft](https://onezero.medium.com/speaking-truth-to-power-reflections-on-a-career-at-microsoft-90f80a449e36) - 在一家存在严重缺陷的公司工作了 30 年之后，作者得出了一个谦虚的结论：领导者应该体现员工的价值。反之则不然。 “最能产生文化影响的是高层的变化，而不是演讲、培训或话题标签。如果你想要真正、持久的文化变革，那就扫除那些在以前的文化下取得成功的人，并提拔那些在外表、行为和思维上更像员工而不是经理的人。”

### 收购

重组的一种特殊情况，可能采取合并、吸收或解散被收购公司的形式。

- [How the Digg team was acquihired](https://lethain.com/digg-acquihire/) - 收购整个团队可以被视为一种重组。其中，经理们必须在一两天内批量谈判新的雇佣合同：“因为收购者是‘明星’导向的，如果你是高层领导，如果不明确拒绝前进，压力就会从四面八方汇聚到你身上”。

## 健康

- [Good sleep, good learning, good life](https://supermemo.guru/wiki/Good_sleep,_good_learning,_good_life) - 关于睡眠研究的电子书大小的综合，“着眼于实际应用，特别是对于那些需要高质量睡眠来实现学习或创造性成就的人”。

### 假期

- [Should we take a few long holidays, or lots of short ones?](http://timharford.com/2019/09/should-we-take-a-few-long-holidays-or-lots-of-short-ones/) - 短的。 “原因一：假期记忆往往不取决于假期有多长，而是取决于体验的强度。原因二：活动的改变可以激发创造力。短暂休息的原因三：如果我们需要休息以防止疲惫，那么一次长假就不够了。”

### 压力

- [The Toxic Handler: Organizational Hero — and Casualty](https://www.companiesalive.com/toxichandlers-healthandhealing-lifecoaching-miami-leadershiptraining.htm) - “有毒处理者是指自愿承担组织生活中常见的悲伤、沮丧、痛苦和愤怒的管理者。尽管有毒处理者可能存在于组织的各个级别，但许多人都在高层附近工作”。

- [Manager Energy Drain](https://larahogan.me/blog/manager-energy-drain/) - “作为一名经理，我该如何应对自己的疲惫感？1. 整理日历碎片；2. 委派混乱且未划定范围的项目；3. 说不。”

- [How Slack Harms Projects](https://www.silasreinagel.com/blog/2019/08/12/how-slack-harms-projects/) - “宣扬错误的紧迫感，破坏焦点，允许绕过项目优先级，剥夺必要的业务背景，鼓励未经深思熟虑的沟通”。要解决此问题，请参阅[如何使用 Slack 而不是疯狂](https://pspdfkit.com/blog/2018/how-to-use-slack-and-not-go-crazy/) 文章。

- [Examples of harassments](https://news.ycombinator.com/item?id=21856352) - 一个嫉妒的老板，感觉自己被背叛了，或者被嘲笑了，如何欺负一个有能力的员工，把他赶走。别做那种混蛋老板。

### 倦怠

- [How shitty job crush your soul, then lead to burnout](https://news.ycombinator.com/item?id=7789438) - “倦怠是一种非常严重的情况。如果你把自己精疲力尽，那么你以后从事的任何工作都将很难发挥作用，即使它表面上是一份很棒的工作。对待倦怠就像对待身体伤害一样。”

- “倦怠是由怨恨引起的。（……）不。倦怠是当你反复为高风险问题做出大量牺牲和/或努力而失败时引起的。这是伏隔核中负面预测错误的结果。你有效地调节了你的大脑，将工作与失败联系起来。” ([来源](https://news.ycombinator.com/item?id=5630618))。

- [If You're So Successful, Why Are You Still Working 70 Hours a Week?](https://archive.ph/78aEf) - “我们过度工作和倦怠的倾向是由涉及我们的职业、我们的组织和我们自己的复杂因素组合而成的。其核心是不安全感。”

- [What Happens When Your Career Becomes Your Whole Identity](https://archive.ph/yqPAD) - “高成就、激烈的竞争和过度工作文化的特殊结合，让许多人陷入了职业生涯陷入困境和倦怠的完美风暴中。”

- “根据我的经验，极端的工作狂往往是避免或推迟某人不想做出甚至有意识地承认的重大人生决定的一种方式。（……）债务最终会到期，但有时要到几十年后才到期。” ([来源](https://news.ycombinator.com/item?id=21900054))

- [Burnout From an Organizational Perspective](https://ssir.org/articles/entry/burnout_from_an_organizational_perspective) - “军方对压力条件下可持续表现的广泛研究表明，领导者应该成为健康的捍卫者，而不是监工。”描述有毒组织的症状以及管理者如何保护其团队免受系统性倦怠。

- [Avoiding burnout as an ambitious developer](https://stackoverflow.blog/2020/01/13/avoiding-burnout-as-an-ambitious-developer/) - “愿意说不；知道你不想要什么；现实地利用你的能量水平；善待未来的自己”。

- [Psychology Today: How Programmers Can Avoid Burnout](https://www.psychologytoday.com/us/blog/dear-life-please-improve/202008/how-does-your-tech-job-burn-you-out) - “经验丰富的软件开发人员经常建议：1. 在一个可以成长的地方工作；2. 培养可转移的技能；3. 拥有创造性的出路，创造一个专注于自己、休息和放松的空间；4. 当然，总有一个核心选​​择：赚钱然后离开。”

- [Average tenure of a CISO is just 26 months due to high stress and burnout](https://www.zdnet.com/article/average-tenure-of-a-ciso-is-just-26-months-due-to-high-stress-and-burnout/) - “如今，CISO 的工作预算低、工作时间长、执行董事会缺乏权力、他们可以雇用的训练有素的专业人员不断减少，而且还面临着在确保公司基础设施免受网络攻击方面做得不够的持续压力、新出现的威胁带来的持续压力，以及对所做的出色工作几乎不表示感谢，但如果一切出了问题，一切都会受到指责。”

## 挫折和失败

- “凡杀不死我的，都会让我更强大”，弗里德里希·尼采 - 残酷，但有一定道理。

- “生存下来的不是最强大的物种，也不是最聪明的物种。而是最能适应变化的物种。”查尔斯·达尔文 - [引用](https://quoteinvestigator.com/2014/05/04/adapt/) 驯服上面的一个。

- [Early-career setback and future career impact](https://www.nature.com/articles/s41467-019-12189-3) - “尽管早期遭遇挫折，但从长远来看，侥幸成功的人的表现会系统性地优于那些险胜的人。”

- [Huge success in business is largely based on luck](https://theconversation.com/huge-success-in-business-is-largely-based-on-luck-new-research-130843) - “管理研究和教育应该关注能够帮助商业从业者从‘无能到OK’转变的规范性理论，而不是那些解决如何从‘优秀到卓越’转变的理论。”

- [How Complex Systems Fail](https://stuff.mit.edu/afs/athena/course/2/2.75/resources/random/How%20Complex%20Systems%20Fail.pdf) - “关于失败本质的简短论述；如何评估失败；如何将失败归因于近因；以及由此产生的对患者安全的新理解”。

<!--lint disable double-link-->

- [Normalization of deviance](https://danluu.com/wat/) - 探讨导致灾难的因素如何在不被注意的情况下累积，直到为时已晚。这已经在其他领域进行了研究，但在软件工程中还没有。

<!--lint enable double-link-->

- [Steve Jobs explains - Why companies fail?](https://www.youtube.com/watch?v=B-fAinNDbQU&t=6s) - 关于销售和营销如何接管以产品为中心的公司。

- [The failure of Scaling Etsy](https://archive.ph/h07CR) - 当公司缺乏技术领导力时：开发人员将时间浪费在成本高昂的重构、过度设计的系统上，最终脱离业务和产品。

## 退出

有时，你只需要停下来。

- [Why I Rejected My Manager](https://archive.ph/NxLVP) - “我现在明白为什么有句话说：离开的是管理者，而不是公司。”

- [Colleague is leaving. How to investigate what went wrong?](https://news.ycombinator.com/item?id=20786755) - “大多数时候，人们离开的是老板，而不是工作或公司。”以及为什么你不太可能从离职面谈中获得任何实质性的见解。 ([来源](https://news.ycombinator.com/item?id=20787874))

- “*人们确实会成群结队地生气*是我见过的对团队/公司崩溃的最好描述。” ([来源](https://news.ycombinator.com/item?id=19755001))

<!--lint disable double-link-->

- “我多次看到的一点是，当副总裁离开时，公司的工作环境将会变得更加糟糕，人们会慢慢意识到副总裁不仅在支持他们的直接下属方面做得非常出色，而且还确保他们手下的每个人都过得愉快。” ([来源](https://danluu.com/wat/#fn:P))

<!--lint enable double-link-->

- “下次你最喜欢的经理和技术主管退出公司时，问问他们为什么。” （[来源](https://news.ycombinator.com/item?id=21767843)）。

- “[良好的商业黑手党形式](https://archive.ph/9Osm2)，当一群人因与绩效无关的原因而必须辞职时。就 Paypal 而言，这是一次收购；在 Tiger Management 中，这是几年业绩不佳；在 Drexel Burnham Lambert 中，这是一份起诉书。在 Reliance 的案例中，早期员工的核心群体由于骚乱和撤军而逃离了亚丁港。英国人。” ([来源](https://archive.ph/WCxsu)) - 为什么大规模的人口外流可能是伟大的新企业的机会。

- “根据我的经验，任何一次离职都不会产生任何影响。大规模离职会产生影响，趋势会产生影响，但一个人从来不会产生影响，即使那个人是创始人。” （[来源](https://news.ycombinator.com/item?id=4324615)）。

- [As an Employee, You Are Disposable](https://nelson.cloud/as-an-employee-you-are-disposable/) - “喜欢你的工作和雇主是可以的。只要明白，作为一名雇员，你是可以随意处置的。”另外：“这不是什么新闻。如果你忠于你的雇主，并且不拥有组织的重要部分，那么你应该认真审视一下你为什么忠诚——以及你的雇主是否也对你忠诚作为回报。” （[来源](https://news.ycombinator.com/item?id=40943681)）。

- [P.T.'s Hidden Meaning](https://www.youtube.com/watch?v=yr4RvdREwl8) - 小岛秀夫如何创造性地利用可玩的预告片来绕过保密协议，并讲述科乐美因混乱导致他离开公司的故事。但只有当你是一位有影响力且受欢迎的游戏设计师时，这才有效。

- [Management Challenges for the 21st Century - Managing Oneself](https://www.thecompleteleader.org/sites/default/files/imce/Managing%20Oneself_Drucker_HBR.pdf) - “现在有很多关于高管的“中年危机”的讨论。大部分都是无聊。大多数高管在 45 岁时就已经达到了商业生涯的顶峰，并且知道这一点。”在第五段中，你会发现为什么知识工作者需要自我管理，并为自己的后半生做计划。

## 贡献

随时欢迎您的贡献！请先查看[贡献指南](.github/contributing.md)。

## 脚注

[标题图片](https://github.com/kdeldycke/awesome-engineering-team-management/blob/main/assets/awesome-management-header.png) 基于 [Werner Du plessis](https://unsplash.com/@werner01) 修改的 [2017 年 11 月拍摄的照片](https://unsplash.com/photos/6dDHofabCQ8)。

<!--lint disable no-undefined-references-->

<a name="intro-quote-def">[1]</a>: [*Peopleware: Productive Projects and Teams, 1987*, page 34](https://www.amazon.com/dp/0321934113?&linkCode=ll1&tag=kevideld-20&linkId=9a6c692819b070f38feb70816e6635ab&language=en_US&ref_=as_li_ss_tl) (Addison-Wesley Professional, 3rd edition, 2013). [[↑]](#intro-quote-ref)
