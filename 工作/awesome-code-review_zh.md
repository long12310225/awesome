<img src="Awesome Code Review.png" alt="Awesome Code Review" />

# 很棒的代码审查 [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

> 与[代码审查]相关的工具、文章、书籍和任何其他资源的精选列表(https://en.wikipedia.org/wiki/Code_review)

代码审查是对计算机源代码的系统检查（有时称为同行审查）。

## 内容

- [很棒的代码审查！[很棒](https://github.com/sindresorhus/awesome)](#awesome-code-review-)
- [Contents](#contents)
- [学术论文](#academic-papers)
- [Articles](#articles)
- [Books](#books)
- [讲座和播客](#talks-and-podcasts)
- [Tools](#tools)
- [Contribute](#contribute)
- [License](#license)

## 学术论文

- [评估大规模软件开发中代码检查的成本效益的实验（Porter、Siy、Toman 和 Votta，1997）](http://laser.cs.umass.edu/courses/cs521-621.Fall10/documents/PorterSiyetal.pdf) 早期论文测试了一系列当时流行的审查技术，包括多阶段审查和 code-review-via-meeting，发现您可以得到大部分好处是在离线、单次通过、有两名审阅者的情况下获得的。
- [随时随地代码检查：使用 Web 消除大规模软件开发中的检查瓶颈（Perpich、Perry、Porter、Votta 和 Wade，1997 年）](https://dl.acm.org/itation.cfm?id=253234) 在遥远的将来有一天，检查代码的最佳方式将是在万维网上。
- [有用代码审查的特征：微软的实证研究（Bosu, Greiler, Bird, 2015）](https://www.michaelagreiler.com/wp-content/uploads/2019/02/Characteristics-Of-Useful-Comments.pdf) 本文报告了一项大规模定性和定量研究的结果，重点是了解开发人员认为哪些代码审查评论有用。
- [战壕中的代码审查：理解挑战、最佳实践和工具需求（MacLeod、Greiler、Storey、Bird、Czerwonka、 2018)](https://www.michaelagreiler.com/wp-content/uploads/2019/03/Code-Reviewing-in-the-Trenches-Understand-Challenges-Best-Practices-and-Tool-Needs.pdf) 对 900 多名 Microsoft 开发人员进行的大规模研究，以了解他们的代码审查流程、他们进行代码审查的动机以及他们遇到的陷阱和最佳实践。
- [通过设计和代码检查减少程序开发中的错误（Fagan，2002）](https://link.springer.com/chapter/10.1007/978-3-642-59412-0_35) 使用更正式的流程，特别是为每个参与者定义角色，并在审查期间大幅增加错误检测。
- [帮助开发人员自助：代码审查变更的自动分解（Barnett 等人，2015 年）](http://research.microsoft.com/pubs/238937/barnett2015hdh.pdf)（[上午总结论文](https://blog.acolyer.org/2015/06/26/helping-developers-help-themselves-automatic-decomposition-of-code-review-changes/)) 研究自动将大差异分割成更小的差异，从而获得更好的评论。
- [现代代码审查：Google 案例研究](https://sback.it/publications/icse2018seip.pdf) 一项展示代码审查在 Google 工作方式的研究。
- [基于拉取的开发中的工作实践和挑战 (Gousios et al. 2015)](https://sback.it/publications/icse2016b.pdf) ([晨报摘要](https://blog.acolyer.org/2015/06/23/work-practices-and-challenges-in-pull-based-development/)) 实地研究如何在狂野的。

## 文章

- [优秀代码审查的 8 个技巧](https://kellysutton.com/2018/10/08/8-tips-for-great-code-reviews.html) 更好的代码审查流程的一些基本规则。
- [更好的代码审查](https://www.giladpeleg.com/blog/better-code-review/) 一套不错的代码审查模式和反模式。
- [有效代码审查的禅宗宣言](https://medium.freecodecamp.org/a-zen-manifesto-for- effective-code-reviews-e30b5c95204a) 为提交者和审查者进行有效代码审查的实用技巧。
- [Brian Guthrie 的功能分支咆哮](https://twitter.com/bguthrie/status/937750796334174209) 关于 GitHub 开源第一模型在“公司内部”代码审查实践方面的优缺点的 Twitter 帖子。
- [建立包容性代码审查文化](https://blog.plaid.com/building-an-inclusive-code-review-culture/) 帮助确保协作和学习文化的指南
- [代码审查：创建文化，学习最佳实践](https://codingsans.com/blog/code-review) 来自技术领导者的代码审查技巧和最佳实践。
- [代码审查礼仪](https://css-tricks.com/code-review-etiquette/) 一些有助于积极参与代码审查的技巧。
- [人类代码审查指南](https://phauer.com/2018/code-review-guidelines/) 提供和获得代码审查的一些指南。
- [代码审查：Just Do It](https://blog.codinghorror.com/code-reviews-just-do-it/) 早在 2006 年就倡导对软件进行同行评审的开创性帖子。
- [Google 的代码审查轻量级且快速](https://www.michaelagreiler.com/code-reviews-at-google/) 详细介绍了 Google 的代码审查最佳实践和流程的运作方式。
- [代码审查审查是经理的工作](https://hecate.co/blog/code-review-review-is-the-managers-job) 为什么管理层应该确保代码审查完成并且做得很好。
- [代码审查期间的评论](https://medium.com/@otarutunde/comments-during-code-reviews-2cb7791e1ac7) 在代码审查期间撰写良好的评论。
- [设计出色的代码审查](https://medium.com/unpacking-trunk-club/designing-awesome-code-reviews-5a0d9cd867e3) 积极设计代码审查流程的原则。
- [无痛有效的代码审查](https://www.developer.com/tech/article.php/3579756/Effective-Code-Reviews-Without-the-Pain.htm) 2006 年关于如何有效执行代码审查的另一部经典著作。
- [反馈阶梯：我们如何在 Netlify 编码代码评审](https://www.netlify.com/blog/2020/03/05/feedback-ladders-how-we-encode-code-reviews-at-netlify/) 有助于评审者对评审反馈的具体可操作性进行分类的有用框架。
- [代码审查在 Microsoft 的工作方式](https://www.michaelagreiler.com/code-reviews-at-microsoft-how-to-code-review-at-a-large-software-company/) 深入分析 Microsoft 的代码审查流程。
- [我如何审查代码](https://engineering.tumblr.com/post/170040992289/how-i-review-code) 来自 Tumblr 工程师的关于如何最好地审查拉取请求的更多个人建议。
- [如何进行代码审查](https://google.github.io/eng-practices/review/reviewer/) 来自 Google 工程实践文档的 Google 工程师如何进行代码审查的详细说明。
- [如何像人类一样进行代码审查](https://mtlynch.io/ human-code-reviews-1/) 将代码审查不仅视为一种技术过程，而且也是一种社会过程的技术。
- [现代代码审查](https://rethought.se/research/modern-code-reviews/) 可以说属于学术论文，但它是一个通过方面/上下文概述代码审查证据的网站。链接到一堆论文。
- [关于代码审查](https://medium.com/@schrockn/on-code-reviews-b1c7c94d868c) 来自前 Facebook 工程师的关于代码审查的工具和个人元素的短文。
- [拉取请求：如何获取并提供良好的反馈](https://kickstarter.engineering/pull-requests-how-to-get-and-give-good-feedback-f573469f0c44) 为代码审查过程双方、审查者和被审查者提供建议。
- [Ship Small Diffs](https://blog.skyliner.io/ship-small-diffs-741308bec0d1) 为什么审查小变更比审查大变更更好。
- [堆叠拉取请求：保持 GitHub Diffs 小](https://graysonkoonce.com/stacked-pull-requests-keeping-github-diffs-small/) 拆分大型 PR 并提高审核参与度的分步过程。
- [人性化拉取请求的艺术](https://blog.usejournal.com/the-art-of- humanizing-pull-requests-prs-b520588eb345) 通过拉取请求进行代码审查的人性化方面的丰富表情符号指南。
- [迈向富有成效的技术讨论](https://cate.blog/2018/07/03/towards-productive-technical-discussions/) 将代码审查讨论推向更有成效的领域的战术问题和行动。
- [在代码审查文化中忘却有毒行为](https://medium.com/@sandya.sankarram/unlearning-token-behaviors-in-a-code-review-culture-b7c295452a3c) 通过 how-not-too 拉取请求的操作指南。
- [为什么我改变了我对代码质量的看法](https://medium.freecodecamp.org/why-i-changed-the-way-i-think-about-code-quality-88c5d8d57e68) 为什么代码质量不仅仅是代码。

## 书籍

- [同行代码审查的最佳秘密](https://www.goodreads.com/book/show/1563457.Best_Kept_Secrets_of_Peer_Code_Review) 10 篇有关代码审查实践的文章的旧汇编。由于不同作者涵盖同一领域而导致一些重复。
- [演练、检查和技术审查手册](https://www.amazon.com/Handbook-Walkthroughs-Inspections-Technical-Reviews/dp/0932633196) 较旧的书涵盖了更正式的演练，但很好地涵盖了审查中的政治和群体动态。
- [软件同行评审：实用指南](https://www.amazon.com/Peer-Reviews-Software-Practical-Guide/dp/0201734850) 将正式代码检查作为代码审查实践的实用指南。
- [软件检查：行业最佳实践](https://www.amazon.com/Software-Inspection-Industry-Best-Practice/dp/0818673400) 有关代码审查实践的论文纲要。
- [代码审查终极指南](https://www.codacy.com/ebooks/guide-to-code-reviews) Codacy 赞助的基于开发人员调查的代码审查实践电子书。
- [在代码审查中寻找什么](https://leanpub.com/whattolookforinacodereview) JetBrains 赞助的电子书，介绍如何在审查期间发现编码反模式。

## 讲座和播客

- [代码审查：诚实、善良、灵感：选择三项 - Jacob Stoebel RubyConf 2017](http://confreaks.tv/videos/rubyconf2017-code-reviews-honesty-kindness-inspiration-pick-third) 如何进行有效的代码审查，同时对原作者保持友善。
- [金发姑娘和三个代码审查 - Vaidehi Joshi RedDot Ruby Conf 2017](https://confreaks.tv/videos/reddotrubyconf2017-goldilocks-and-the- Three-code-reviews) 通过关注影响因素来找到适量的代码审查。
- [实施强大的代码审查文化 - Derek Prior Railsconf 2015](https://www.youtube.com/watch?v=PJjmw9TRB7s) 如何在团队中灌输健康的代码审查文化。
- [Michaela Greiler 谈代码审查 - SE Radio 2020](https://www.se-radio.net/2020/02/episode-400-michaela-greiler-on-code-reviews/) Michaela Greiler 在软件工程广播播客上讨论了代码审查的重要性以及如何进行代码审查。

## 工具

- [Axolo](https://www.axolo.co) Github/GitLab Slack 集成。每个拉取请求/合并请求创建一个临时通道。
- [Crucible](https://www.atlassian.com/software/crucible) Atlassian 的本地代码审查工具。
- [Gerrit](https://www.gerritcodereview.com/) 源自 Google 的开源 git 代码审查工具。
- [GitHub](https://github.com) Git 托管和“Pull Request”的先驱。
- [Gitpod](https://gitpod.io) 在浏览器中的完整 IDE 中审查拉取请求的代码。
- [LGTM](https://lgtm.com) 对 GitHub 和 Bitbucket 拉取请求进行自动 Git 代码审查，以查找安全漏洞和代码质量问题。
- [Phabricator](https://www.phacility.com/phabricator/) 源自 Facebook 的开源 git/mercurial/svn 代码审查工具。
- [PullNotifier](https://www.pullnotifier.com/) 使用 Github 和 Slack 提高开发团队的拉取请求可见性和整体生产力。
- [PullRequest](https://www.pullrequest.com/) 代码审查作为 GitHub 拉取请求的服务。
- [Reviewable](https://reviewable.io/) 构建在 GitHub Pull Request 之上的代码审查工具。
- [评审委员会](https://www.reviewboard.org/) 开源评审工具，是 SCM/平台中立的。
- [Sider](https://sider.review/) GitHub 的自动代码审查服务。
- [Softagram](https://softagram.com/) 针对拉取请求、合并请求 (GitLab) 和补丁集 (Gerrit) 的自动代码更改可视化（和依赖性分析）。
- [SonarCloud](https://sonarcloud.io) 检测 Azure DevOps、Bitbucket 和 GitHub 存储库中的代码气味、错误和漏洞。
- [Upsource](https://www.jetbrains.com/upsource/) JetBrain 的本地 git/mercurial/perforce/svn 代码审查工具。
- [Viezly](https://viezly.com) 代码审查服务，具有拉取请求可视化和增强的更改之间的导航。

## 贡献

欢迎投稿！首先阅读[贡献指南](contributing.md)。

## 许可证

[![CC0](http://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](http://creativecommons.org/publicdomain/zero/1.0)

在法律允许的范围内，[John Barton](https://johnbarton.co) 已放弃所有版权和
本作品的相关或邻接权。
