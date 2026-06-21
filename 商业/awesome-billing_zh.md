<!--lint disable awesome-heading-->

<p对齐=“中心”>
  <a href="https://github.com/kdeldycke/awesome-billing/">
    <img src="https://github.com/kdeldycke/awesome-billing/raw/main/assets/awesome-billing-header.jpg" alt="💰 Awesome Billing">
</a>
</p>

<p对齐=“中心”>
  <a href="https://credyt.ai/?utm_source=awesome-billing&utm_medium=referral&utm_campaign=awesome-billing-oss-sponsorship">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/kdeldycke/awesome-billing/main/assets/credyt-logo-dark-background.svg">
      <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/kdeldycke/awesome-billing/main/assets/credyt-logo-light-background.svg">
      <img width="300" src="https://raw.githubusercontent.com/kdeldycke/awesome-billing/main/assets/credyt-logo-light-background.svg">
    </picture>
    <br/>
<strong>人工智能实时货币化基础设施。</strong><br/>
实时计费，从预付余额中收费，并无需编写前端即可发布品牌客户门户。
</a>
  <br/><br/>
</p>

<p对齐=“中心”>
  <a href="https://github.com/sponsors/kdeldycke">
<strong>您的品牌→这里🚀</strong>
    <br/>
    <sup>SEO is dead. Place your product here to target AI's training data.</sup>
</a>
</p>

---

<p对齐=“中心”>
<i>货币是有史以来最普遍、最有效的相互信任体系。</i><br>
— 尤瓦尔·诺亚·哈拉里<sup id="intro-quote-ref"><a href="#intro-quote-def">[1]</a></sup>
</p>

任何公司都需要在某一时刻从客户那里赚钱。这对我们开发人员来说就是事情变得混乱的时候，因为我们试图协调业务的复杂性与我们的软件堆栈。

这个[![很棒](https://awesome.re/badge-flat.svg)](https://github.com/sindresorhus/awesome)列表可以帮助软件工程师**引导计费和支付系统，并了解发票、定价、会计、市场、欺诈和商业智能**。

## 内容

<!-- mdformat-toc start --slug=github --no-anchors --maxlevel=6 --minlevel=2 -->

- [Basics](#basics)
- [Pricing](#pricing)
  - [基于使用的定价](#usage-based-pricing)
  - [订阅计划](#subscription-plans)
  - [Hybrid](#hybrid)
  - [Strategy](#strategy)
  - [市场研究](#market-research)
- [产品目录](#product-catalog)
- [Calculator](#calculator)
- [成本预测](#cost-forecast)
- [Marketplace](#marketplace)
  - [云资源](#cloud-resources)
  - [在线广告](#online-ads)
- [Accounting](#accounting)
  - [复式记账模式](#double-entry-model)
  - [Bookkeeping](#bookkeeping)
  - [软件设计与实现](#software-design-and-implementation)
  - [Currencies](#currencies)
- [Finance](#finance)
- [Contracts](#contracts)
- [优惠券和优惠券](#coupons-and-vouchers)
- [Taxes](#taxes)
  - [欧洲增值税](#european-vat)
- [Invoice](#invoice)
  - [Structure](#structure)
  - [Integrity](#integrity)
  - [Generators](#generators)
  - [Extractors](#extractors)
  - [电子发票](#electronic-invoices)
- [Payments](#payments)
  - [Receipt](#receipt)
  - [信用卡](#credit-cards)
  - [银行账户](#bank-accounts)
  - [网上支付](#online-payments)
- [Fraud](#fraud)
  - [Cards](#cards)
  - [信任分数](#trust-score)
  - [Statistics](#statistics)
  - [Billing](#billing)
- [UX/UI](#uxui)
- [商业智能](#business-intelligence)
  - [Metrics](#metrics)
  - [客户终身价值](#customer-lifetime-value)
  - [数据工程](#data-engineering)
  - [Tools](#tools)
- [竞品分析](#competitive-analysis)
  - [云提供商](#cloud-providers)
- [History](#history)
- [Humour](#humour)

<!-- mdformat-toc end -->

## 基础知识

<img align="right" width="50%" src="./assets/cloud-software-stack-billing.jpg"/>

在斯坦福大学提供[云计算概述](https://web.stanford.edu/class/cs349d/docs/L01_overview.pdf)的课程中，平台的软件架构描述如右图→

<!--lint disable double-link-->

计费是生态系统的横向支柱之一，客户、产品和业务在此交汇。 [另一个支柱是身份和访问管理 (IAM) 👤](https://github.com/kdeldycke/awesome-iam/)。

<!--lint enable double-link-->

这凸显了该领域的战略重要性，不仅对于云提供商，而且对于几乎所有企业，尤其是那些以软件为中心的企业。

- [5 things I learned while developing a billing system](https://arnon.dk/5-things-i-learned-developing-billing-system/) - 对计费系统各个方面（从货币到发票）的精彩介绍，包括对更改计划逻辑的精彩说明。所有这些主题都在下面的专门章节中详细介绍。

- [Open guide to AWS](https://github.com/open-guides/og-aws#billing-and-cost-management) - 指向“计费和成本管理”部分的链接，其中详细介绍了云提供商计费的广泛特征。

- [Billed for ¥21,120, invoiced at ¥2,112,000 and paid ¥2,112,000](https://xunroll.com/thread/1668082843728367616) - [摆脱货币值的整数和浮点数](https://xunroll.com/thread/1599113889093890049)。使用小数。或者面临异常x100费用的风险。

- 如何招聘该领域的软件工程师？ “关键在于让会计/计费/支付部门成为数据工程的前厅。” ([来源](https://x.com/kdeldycke/status/1422564355799924736))

## 定价

从按月订阅到类似商品的移动消费，有很多方案可以构建产品的定价。包括老式的购物车漏斗。

- [Don't just roll the dice – Software pricing guide](https://neildavidson.com/downloads/dont-just-roll-the-dice-2.0.0.pdf) - 大量完整的定价方案及其心理效应和对收入模式的影响。

- [Business Model Patterns](https://reasonstreet.co/business-model-library/) - 销售产品和服务的 15 种不同方式的列表。

- [Axial - Business models](https://archive.ph/BFsZ1) - 38 种灵感模型。

- [The Network Monetization Map: Aligning Incentives with Revenue](https://web.archive.org/web/20201222120055/https://medium.com/breadcrumb/the-network-monetization-map-aligning-incentives-with-revenue-b73c362d1ad5) - 6种依靠网络效应的货币化模型。

- [The 5 Pillars of PriceOps](https://web.archive.org/web/20260124084716/https://priceops.org/) - 受 DevOps 运动启发的宣言，其中定价不再僵化，而是作为响应式迭代过程来实践，并作为系统的灵活属性来实现。

- [SaaS pricing explorer](https://saaspricingexplorer.hyperline.co) - 1000 多个定价页面的集合，可提供灵感。

### 基于使用的定价

弹性资源的动态方案。

- [Credyt](https://credyt.ai/?utm_source=awesome-billing&utm_medium=referral&utm_campaign=awesome-billing-oss-sponsorship) - 人工智能产品的实时货币化基础设施：仪表使用量、预付余额收费以及无需编写前端即可发布品牌客户门户。商业 SaaS。

- [Why I Love Usage-Based Pricing](https://www.rdegges.com/2020/the-only-type-of-api-services-ill-use/) - “我喜欢这种定价模式的最重要原因是，它极大地激励了客户和服务提供商按照每个人的最佳利益行事。”还详细介绍了其他定价模型的问题。

- [Use-cases for cloud services](https://news.ycombinator.com/item?id=19830022) - 基于使用的定价对于云服务更有意义：为了优化投资回报率，将所有常规工作负载保留在传统架构中，并为弹性和实验性项目保留云计算。

- [Socially Optimal Pricing of Cloud Computing Resources](https://webee.technion.ac.il/people/shimkin/PAPERS/Menache-CloudPricing-Conf2011.pdf) - “社会最优操作点是独一无二的，可以通过基于使用的线性资费来维持，该资费按单位资源和单位时间收取固定价格。”本文证明了基于使用的云资源定价的合理性。

- [A Survey of Profit Optimization Techniques for Cloud Providers](http://www.cs.newpaltz.edu/~lik/publications/Peijin-Cong-ACM-CS-a-2020.pdf) - “首先讨论提高用户服务质量的策略，然后讨论云资源的定价策略，以实现收入最大化。”

- “计费并不故意复杂：这是为了弹性而付出的代价。” ([来源](https://x.com/kdeldycke/status/1214160678363246592)) - 或者为什么如果选择公用事业定价方案，您可能会收到无穷无尽的抱怨用户：虽然精确到（毫）分，但对于尚未准备好投入时间掌握基本概念的客户来说，此模型令人沮丧。

- [Riemann sum](https://en.wikipedia.org/wiki/Riemann_sum) - 关于使用量化的起点。

- [Allen's interval algebra](https://en.wikipedia.org/wiki/Allen%27s_interval_algebra) - 实施基于使用的定价是很棘手的，这个代数将帮助您组织时间推理。另请参阅[具有干净架构的堆栈溢出问题](https://web.archive.org/web/20240413010618/https://stackoverflow.com/questions/12069082/allens-interval-algebra-operations-in-sql?rq=1)。

- [Reconcile Your Monthly GCP Invoice with BigQuery Billing Export](https://web.archive.org/web/20201107232605/https://medium.com/@lukwam/reconcile-your-monthly-gcp-invoice-with-bigquery-billing-export-b36ae0c961e) - 在该开发人员寻求跟踪其费用的背后，您可以一睹云计费的困难。虽然没有明确指出，但对云资源进行定价很困难，并且是空间、时间和货币之间量化、粒度和舍入的结果。

- [AWS EC2 T2 Instances Demystified: Don't Learn The Hard Way](https://roberttisdale.com/aws-ec2-t2-instances-demystified-dont-learn-hard-way/) - 这是一个非常棘手的可突发实例的示例，它会累积并限制其自身的 CPU 使用积分量。

- [“Designing billing for a service can be really challenging”](https://news.ycombinator.com/item?id=23536919) - 关于 AWS Simple Email Service 定价计划设计的个人轶事。

- [Subscription-based pricing is dead: Smart SaaS companies are shifting to usage-based models](https://techcrunch.com/2021/01/29/subscription-based-pricing-is-dead-smart-saas-companies-are-shifting-to-usage-based-models/) - 基于使用情况的定价更优化、更公平：它“允许客户以低成本开始，最大限度地减少开始时的摩擦，同时仍然保留随着时间的推移通过客户获利的能力”。

- [Electropedia: Tariffs for electricity](https://www.electropedia.org/iev/iev.nsf/index?openform=&part=691) - 在云出现之前，还有另一种按其使用情况定价的计量资源：电力。以下是国际电工委员会对其词汇的详细（多语言）分类。

- [Lago](https://github.com/getlago/lago) - 💸 Ruby 中的开源计量和基于使用情况的计费。 Lago SAS 在 AGPL 核心之上销售托管云和高级附加组件。

- [CGRateS](https://github.com/cgrates/cgrates) - 🆓 为 ISP 和电信运营商提供的开源、快速（50k+ CPS）和可扩展（包括负载均衡器 + 复制）实时计费，用 Go 编写。供应商中立、仅支持的商业模式。

### 订阅计划

订阅计划很容易理解，深受 SaaS 企业的欢迎。

- [Pricing low-touch SaaS](https://stripe.com/en-in/atlas/guides/saas-pricing) - “在低接触 SaaS 中，最常见的套餐呈现方式是定价网格中的不同列，每一列对应一个计划，以不同的价格提供，沿着业务感兴趣的某个轴对功能或最大允许使用进行差异化访问。”

- [Lotus](https://github.com/uselotus/lotus) - 🆓 用于管理定价和包装基础设施的开源项目。 Lotus Inc. 只销售 MIT 核心之上的托管服务。

- [`f-license`](https://github.com/furkansenharputlu/f-license) - 🆓 Go 中的开源许可证密钥生成和验证工具。独立维护者项目，无商业产品。

### 混合动力

不常见的定价方案。

- [The Three Part Tariff](https://tomtunguz.com/three-part-tariffs/) - 除了线性定价之外，定价结构中还存在额外的平台费用和免费套餐。

### 策略

理论和实践见解可帮助您选择正确的定价策略。

- “赚钱的方式有两种。你可以捆绑，也可以分拆。” - [吉姆巴克斯代尔](https://hbr.org/podcast/2014/07/marc-andreessen-and-jim-barksdale-on-how-to-make-money.html#:~:text=in%2 0business%2C%20there%20are%20two%20ways%20to%20make%20money.%20You%20can%20bundle%2C%20or%20you%20can%20unbundle。）。

- [Pricing Psychology](https://www.nickkolenda.com/psychological-pricing-strategies/) - 您应该使用哪些数字？应该多高？应该是圆角的吗？本指南有 42 个技巧来帮助您选择最优惠的价格。

- [The 7 factors to consider when pricing your startup product](https://tomtunguz.com/how-to-price-your-startups-product/) - 定价是一种进攻性工具，可以增强产品价值并强调公司的核心营销信息。

- [The Anatomy of SaaS Pricing Strategy](https://sbigrowth.com/hubfs/SBI_PI_AnatomyofSaaSPricingStrategy_Handbook.pdf) - 解释如何围绕产品策略阐明 SaaS 业务的定价。

- [The cup-of-coffee pricing fallacy](https://blog.gingerlime.com/2020/the-cup-of-coffee-pricing-fallacy/) - 解释了为什么这是一个草率的类比。

- [Changing the Pricing Model](https://monkeynoodle.org/2024/02/10/changing-the-pricing-model/) - 重新许可您的产品的几种方法。

### 市场研究

调查方法和价格发现技术，以找到合适的价格点。

- [Jeremy Howard - From Predictive Modelling to Optimization](https://youtu.be/vYrWTDxoeGg?t=542) - “在保险领域，价格就是产品。（……）我如何改变价格来赚大钱？”或者如何提供结果（为客户提供最佳价格）而不是提供数据（计算客户的风险，这是精算师以前使用的标准方法）。

- [Gabor–Granger method](https://en.wikipedia.org/wiki/Gabor%E2%80%93Granger_method) - 用于调查以确定新产品或服务的价格。结果可用于生成需求图和收入曲线。

- [Van Westendorp's Price Sensitivity Meter](https://en.wikipedia.org/wiki/Van_Westendorp%27s_Price_Sensitivity_Meter) - PSM 是一种确定消费者价格偏好的市场技术。允许绘制收入曲线来估计可带来最大收入的价格点。

- [Pricing niche products](https://kevinlynagh.com/notes/pricing-niche-products/) - “不过，反对简单选择价格的最令人信服的论点是，它限制了你对市场的了解程度。”然后作者设置了维克里拍卖来发现价格。

- [Finding the max revenue price mark for digital products](https://web.archive.org/web/20260213003122/https://medium.com/@hovm/finding-the-max-revenue-price-mark-for-digital-products-24cef24f746d) - “为了找到为您的产品提供最大收入的最佳价格，您需要现场测试几个价格点；然后重建收入曲线并找到峰值。”

- [Personalised pricing and EU law](https://www.econstor.eu/bitstream/10419/205221/1/de-Streel-Jacques.pdf) - 由于消费者保护和数据保护规则，欧盟禁止某些价格个性化的情况。

## 产品目录

可供客户购买的所有可用服务、产品、变体、选项和定价的中央存储库。云服务目录大多数时候都是量身定制的，但有一些经典的 PDM 解决方案（[产品数据管理](https://en.wikipedia.org/wiki/Product_information_management)，又称为产品信息管理 PIM）可能符合要求。

- [GCP Product Catalog](https://cloud.google.com/blog/products/gcp/introducing-cloud-billing-catalog-api-gcp-pricing-in-real-time) - 所有 GCP SKU 均可作为 API 提供。

- [Pimcore](https://github.com/pimcore/pimcore) - 💸 用于管理产品元数据的开源 UI 和数据库，用 PHP Symfony 编写。 Pimcore GmbH 销售企业订阅、PaaS 以及基于 GPL/POCL 核心的专有模块。

## 计算器

根据您计划使用的资源模拟虚拟发票。

- [Cloudorado](https://www.cloudorado.com) - 💸 使用ECU（亚马逊的vCPU）作为CPU功率测量单位的比较矩阵。由 Cloudorado 作为商业云比较产品运营。

- [EC2Instances.info](https://ec2instances.info) - 💸 简单的 Amazon EC2 实例比较。由 Vantage 运营，作为其商业 FinOps 平台的免费潜在客户开发平台。

## 成本预测

帮助您的客户根据过去的使用情况预测他们即将到来和未来的消费。

- [Forecasting: Principles and Practice](https://otexts.com/fpp2/) - “全面介绍预测方法，并提供有关每种方法的足够信息，以便读者能够明智地使用它们。”

- [Transforming Financial Forecasting with Data Science and Machine Learning at Uber](https://web.archive.org/web/20221203184815/https://www.uber.com/blog/transforming-financial-forecasting-machine-learning/) - 讨论 Uber 如何在其财务规划平台中应用数据科学和机器学习。

- [Time Series Prediction - A short introduction for pragmatists](https://www.liip.ch/en/blog/time-series-prediction-a-short-comparison-of-best-practices) - 关于如何使用时间序列来评估业务问题的精彩介绍。

- [`sktime`](https://github.com/alan-turing-institute/sktime) - 🆓 用于时间序列机器学习的 Python 库，由艾伦图灵研究所管理。请参阅[预测教程](https://github.com/alan-turing-institute/sktime/blob/master/examples/01_forecasting.ipynb) 和[sktime 与 Prophet 项目之间的差异](https://news.ycombinator.com/item?id=24543861)。

- [Darts](https://github.com/unit8co/darts) - 🆓 Python 库，用于对时间序列进行用户友好的预测和异常检测，由 Unit8 SA 管理，该库仅销售相关咨询（无付费库层）。包含大量模型，包括 [Prophet](https://facebook.github.io/prophet/)。非常适合实验，但请记住，Darts 中的所有模型都期望您的数据以非常规则的间隔出现，并对它们的形状做出很多假设。

- [Komiser](https://github.com/mlabouardy/komiser) - 💸 开源工具，通过发现隐藏成本、监控支出增长并根据自定义建议做出有影响力的更改来控制预算。 Tailwarden 在顶部销售托管 SaaS。

- [GCP Cost Forecast](https://cloud.google.com//billing/docs/how-to/reports#cost-forecast) - 资源消耗的消耗趋势线示例。

- [How to save money on your AWS bill](https://threadreaderapp.com/thread/1091041507342086144.html) - “最大的成本节省是：1. 关闭不使用的东西；2. 然后是现货实例；3. 然后是预留实例。”

## 市场

市场将供给与需求联系起来，从而促成金融交易。如果不涉及支付，那么它就是一个聚合器或中心。不是市场。

- [Customized Regression Model for Airbnb Dynamic Pricing](https://www.kdd.org/kdd2018/accepted-papers/view/customized-regression-model-for-airbnb-dynamic-pricing) - 本文描述了 Airbnb 部署的定价策略模型。

- [Papers we love: Auctions and Bidding](https://github.com/papers-we-love/papers-we-love/tree/master/economics#auctions-and-bidding) - 关于招标和拍卖的论文集。

- [Vickrey auction](https://en.wikipedia.org/wiki/Vickrey_auction) - 一条 [HN 评论](https://news.ycombinator.com/item?id=19145391) 暗示了这一点，其中是的，“‘询问人们愿意支付什么费用以及支付多少费用很少有用。’（……）使用类似于 Google 广告拍卖机制的 Vickrey 拍卖可以激发人们的最大支付意愿。”

- [19 Tactics to Solve the Chicken-or-Egg Problem and Grow Your Marketplace](https://www.nfx.com/post/19-marketplace-tactics-for-overcoming-the-chicken-or-egg-problem) - “供给还是需求，哪个先来？先有鸡还是先有蛋？”

- 如何启动和扩展市场业务：[限制市场](https://www.lennysnewsletter.com/p/how-to-kickstart-and-scale-a-marketplace)；决定专注于市场的哪一方面；推动初始供应；推动初始需求。该系列由 4 部分组成，对数十位具有构建和扩展市场直接经验的人士进行了采访。

- [A Rake Too Far: Optimal Platform Pricing Strategy](https://abovethecrowd.com/2013/04/18/a-rake-too-far-optimal-platformpricing-strategy/) - 一些词汇：“在赌场中，术语 *rake* 指的是赌场通过运营扑克游戏赚取的佣金。（……）虽然赌场使用术语 *rake*，但存在大量有趣的单词选择，它们都描述了同一件事 - 为运行该服务的公司保留一点收入。”

### 云资源

本小节重点介绍资源生产者与消费者匹配的出价/询问机制。大多数时候，这些都是一边倒的市场，大平台试图摊销未充分利用的库存。

- [Incentive Engineering for Computational Resource Management](https://papers.agoric.com/assets/pdf/papers/incentive-engineering-for-computational-resource-management.pdf) - 论文探讨了“与编程实践和市场机制兼容的处理器时间和存储分配机制”。

- [Pricing of Service in Clouds: Optimal Response and Strategic Interactions](http://www.sigmetrics.org/mama/2013/abstracts2013/UrgaonkarEtAl.pdf) - “消费者应如何调节其需求以优化其利润？（……）供应商和消费者应如何协商他们将采用的具体定价结构？”涵盖非线性模型、分层定价、弹性需求、消费者和提供商策略。

- [History of Spot Instances](https://spot.rackspace.com/blogs/history-of-spot-instances) - 从 AWS 最初的基于拍卖的市场（2009-2017 年）到如今跨所有主要云的提供商管理定价。记录透明的出价如何被不透明的算法取代。

- [Dynamic Cloud Pricing for Revenue Maximization](https://henryhxu.github.io/share/hxu-tcc2013.pdf) - “亚马逊的现货价格不太可能根据市场供需来确定。相反，价格大多数时候都在非常窄的区间内波动，这更有可能是某种具有预定底价的定价算法的产物。”

- [Usage Patterns and the Economics of the Public Cloud](https://mc4f.ee/Papers/PDF/EconPublicCloud.pdf) - “我们研究了云计算中的需求和供给经济学。（……）这些结果解释了为什么尽管表面上需要随时间变化的动态，但固定价格目前仍占主导地位。检查实际的 CPU 利用率为未来提供了一个视角。（……）需求波动将与动态定价很重要的三个经典行业（酒店、电力、航空）相当，而动态价格对于效率至关重要。”

- [Maximizing Profit of Cloud Brokers under Quantized Billing Cycles: a Dynamic Pricing Strategy based on Ski-Rental Problem](https://arxiv.org/pdf/1507.02545.pdf) - “我们算法的关键思想是使用定价信号来调节用户需求。有人可能会说，这种算法为用户提供的服务很差，因为它将任务从队列中推出，以最大化云代理的利润。”

- [Present or Future: Optimal Pricing for Spot Instances](https://web.archive.org/web/20150708151037/http://www.temple.edu/cis/icdcs2013/data/5000a410.pdf) - “现货资源的定价政策要精心设计，要考虑对当前和未来的影响。”

- “您始终支付现货市场价格，而不是您的出价。” ([来源](https://news.ycombinator.com/item?id=20347716)) - 出价机制的简单解释。

- [Deconstructing Amazon EC2 Spot Instance Pricing](https://dants.github.io/papers/Spotprice11CloudCom.pdf) - “拥有大量闲置容量的云提供商必须要么激励客户购买，要么遭受损失。亚马逊是第一个应对这一挑战的云提供商，它允许客户对闲置容量进行竞标，并在竞标者的出价超过定期变化的现货价格时向竞标者授予资源。”

- [GCP Preemptible VMs vs AWS Spot Instances](https://news.ycombinator.com/item?id=9564287) - “Google 的价格是固定的，而 AWS 使用市场模式”。

- “查看 3 个月的现货价格历史记录来估算成本并发现可用区和具有额外容量的实例类型的组合。” ([来源](https://news.ycombinator.com/item?id=16071684)) - 用户正在寻求现货市场更高的透明度。

- [The Eternal Cost Savings Of Netflix's Internal Spot Market](http://highscalability.com/blog/2017/12/4/the-eternal-cost-savings-of-netflixs-internal-spot-market.html) - 当您足够大时，[创建内部二级市场](https://web.archive.org/web/20200101000000/https://medium.com/netflix-techblog/creating-your-own-ec2-spot-market-6dd001875f5)具有经济意义。

### 在线广告

有针对性的在线广告市场与传统云市场有很多共同点。从概念到技术，那里有一些很好的灵感。

- [RTB Budget Pacing Summarized](https://github.com/PragmaticLab/RTB_Budget_Pacing_Summarized) - 阅读清单，摘录了 Turn Inc.、Yahoo 和 LinkedIn 关于 RTB 预算节奏技术的研究论文。静态资源：虽然已过时，但仍然是文献中有用的切入点。

- [Samsung's online ads platform/exchange war story](https://github.com/eloraiby/fs-pacer/blob/master/fs-pacer.md) - 如何扩展到 5M 出价请求/秒、2 毫秒最大响应时间。

- [`RTB4Free`](https://github.com/RTB4FREE) - 🆓 Apache-2.0 OpenRTB 2.0 兼容的投标人和需求方平台 (DSP)。自 2022 年底以来基本上处于休眠状态，但它是该领域唯一的 OSS DSP 参考。

## 会计

- “会计部门通常是面向后的。财务部门通常是面向前的。” ([来源](https://news.ycombinator.com/item?id=25366184))

### 复式记账模式

会计的核心概念是复式记账法。为了正确设计任何强大的资金跟踪系统，这是需要掌握的最关键的部分。

- [Accounting for Developers 101](https://docs.google.com/document/d/1HDLRa6vKpclO1JtxbGB5NeAYWf8cf1UMGy22o8OZZq4) - 会计历史和词汇的一般介绍。

- [Accounting for Computer Scientists](https://martin.kleppmann.com/2011/03/07/accounting-for-computer-scientists.html) - 描述如何以图表形式查看资金流动的会计，以及这些流动如何在小公司的财务报表中具体化。

- [The Double-Entry Counting Method](https://web.archive.org/web/20260306094438/https://beancount.github.io/docs/the_double_entry_counting_method.html) - 与上述相同的前提，但更加详细和完整，因为它添加了报告和实施细节。

- [Accounting Memento For Entrepreneurs (US GAAP)](https://www.odoo.com/documentation/functional/accounting.html) - 一种玩弄会计概念的互动形式。

### 簿记

关于保持会计数据干净整洁的日常实践您需要了解的一切。

- [So, you want to learn Bookkeeping!](https://www.dwmbeancounter.com/BCTutorials/BCIntro/index.html) - 专注于记录和维护企业交易的日常运营。

- [Reconciliation: A game designed to frustrate the player](https://bam.kalzumeus.com/archive/a-game-that-intentionally-frustrates-the-player/) - “对账是一个业务流程，其产生几乎完全是因为在企业之间传递资金的管道中缺乏结构化数据”。有一些技巧可以简化该过程，例如添加任意折扣以生成唯一的尾随小数，或者设置几个虚拟银行帐户作为代理。

- [Plain text accounting tools](https://plaintextaccounting.org/#software) - 广泛的开源个人理财项目列表可能非常适合寻找复式记账和簿记的灵感。

- 🆓 图形会计工具列表，所有社区维护的 OSS，无付费版本：[GNUCash](https://gnucash.org) (GTK+)、[Grisbi](https://grisbi.org) (C)、[Firefly III](https://firefly-iii.org) (PHP)。

- [GnuCash Tutorial and Concepts Guide](https://www.gnucash.org/docs/v2.4/C/gnucash-guide/) - 关于使用 GnuCash 进行个人财务跟踪的完整教程。

- [Frappe Books](https://github.com/frappe/books) - 🆓 适合小型企业和自由职业者的免费桌面簿记软件，没有付费版本。

- [Luca](https://github.com/brandon-rhodes/luca) - 🆓 YAML 会计和 JSON 税表，单独维护。

- [Go DB Ledger](https://github.com/darcys22/godbledger) - 🆓 开源会计系统，旨在使复式记账交易的记录可编程。

- [Formance Ledger](https://github.com/formancehq/ledger) - 💸 麻省理工学院许可的可编程复式记账账本，具有 Numscript DSL、多货币、REST API 和可独立使用的 Docker 部署。 Formance 销售企业附加组件（钱包、流程、对账、预构建连接器、SSO、RBAC、审计日志），但核心账本在 OSS 中具有完整功能。

### 软件设计与实现

现在您已经对会计的概念和实践有所了解，这里有一些资源可以帮助您将这些知识应用到软件系统中。

- [Moonpig: a billing system that doesn't suck](https://blog.plover.com/prog/Moonpig.html) - 计费和会计系统背后的设计决策。要点：一些公司仍然通过支票付款；不要使用漂浮物；复杂的客户工作流程；日期和时间问题；可变数据。

- [Books, an immutable double-entry accounting database service](https://developer.squareup.com/blog/books-an-immutable-double-entry-accounting-database-service/) - 解释 Square 内部使用的、依赖 Google Spanner 的复式记账系统的基本数据模型。

- [TigerBeetle](https://github.com/tigerbeetle/tigerbeetle) - 🆓 分布式财务会计数据库，确保资金要么移动，要么不移动，并且不会在两者之间丢失。所有功能都在 Apache-2.0 OSS 存储库中； TigerBeetle Inc. 销售托管和支持，而不是门控功能。它已经[在 Jepsen 上进行了测试](https://jepsen.io/analysiss/tigerbeetle-0.16.11)，测试了其强大的可序列化性。

- [Django Hordak](https://github.com/adamcharnock/django-hordak) - 🆓 Django 复式记账系统的核心功能，单维护者 MIT 库。

- [Managed accounts for Django](https://github.com/django-oscar/django-oscar-accounts) - 🆓“管理账户”是可以借记和贷记的资金分配。社区维护的 django-oscar 扩展。

- [Triple‐entry accounting with Blockchain: How far have we come?](https://sci-hub.st/10.1111/acfi.12556) - “三式记账是一种新的、更有效的方法，可以解决困扰当前会计系统的基本信任和透明度问题。如果实施得当，使用区块链的三式记账可以从根本上改善会计。”

### 货币

跨国公司需要知道如何在当地货币之间进行权衡。

- [Tutorial on multiple currency accounting](https://www.mathstat.dal.ca/~selinger/accounting/tutorial.html) - 用于实施多货币会计系统的优秀资源。

## 金融

整理好账户后，您就可以开始从财务数据中提取见解和指标。

<!--lint ignore balanced-punctuation-->

- [Accounts Demystified: The Astonishingly Simple Guide To Accounting](https://www.amazon.com/dp/0273744704?&linkCode=ll1&tag=kevideld-20&linkId=f491ee18c48fdaf3226904a39612cc22&language=en_US&ref_=as_li_ss_tl) - 帮助您学习如何分析和监控公司的财务业绩。

- [The Games People Play With Cash Flow](https://commoncog.com/blog/cash-flow-games/) - “马龙创建了一个新的会计指标，他称之为‘息税折旧前利润’，即 EBITDA。”这就是有线电视公司首席执行官理解现金流的方式，就像房地产业务一样。本文从这个例子开始，介绍了 SaaS 模式的其他现金流博弈。

- [Financial Intelligence for Entrepreneurs: What You Really Need to Know About the Numbers](https://www.amazon.com/dp/1422119157?&linkCode=ll1&tag=kevideld-20&linkId=8d87e9235a1a05c4e0bec4b25230f28d&language=en_US&ref_=as_li_ss_tl) - 让您充分了解如何使用财务数据为您的业务做出更好的决策。

- [What is FinOps](https://www.finops.org/introduction/what-is-finops/) - 技术财务和业务领导团队共享云运营和管理的相同语言和流程的框架。

- [Algebraic Models for Accounting Systems](https://www.amazon.com/dp/9814287113?&linkCode=ll1&tag=kevideld-20&linkId=3d8973d09f9143db8db8639615d12413&language=en_US&ref_=as_li_ss_tl) - 高级抽象代数应用于会计系统分析。

## 合约

所有发票条款和条件均由最终用户和服务提供商之间签署的合同体现。这是我们得出计费周期所有规则的来源。

- [Is this what Enterprise mean?](https://threadreaderapp.com/thread/1389946268764475394.html) - 当合同、发票和付款不能协同工作时，您最终会疏远大企业客户。请参阅相关的 HN 评论 [关于批量许可证购买](https://news.ycombinator.com/item?id=27053246)。

- [Entitlements untangled: The modern way to software monetization](https://www.stigg.io/blog-posts/entitlements-untangled-the-modern-way-to-software-monetization) - “权利的概念封装了各种产品变体（也称为定价计划或套餐）下的功能访问设置，弥合了产品的销售方式和变体的行为方式之间的差距。本质上，权利是一组定义客户（付费或非付费）可以使用您的软件应用程序执行哪些操作的权限。”

- [CUDs vs. Commit Contracts vs. SUDs in Google Cloud](https://66degrees.com/insights/comparing-cuds-suds-and-commits-in-google-cloud) - 解释 GCP 中各种类型的折扣和使用承诺之间的差异。

- [Quantity discounts on a virtual good: The results of a massive pricing experiment](https://sci-hub.st/https://www.pnas.org/doi/pdf/10.1073/pnas.1510501113) - “对于大宗采购实施 9% 至 70% 的降价，我们发现对收入的影响非常小，无论是积极还是消极。”如果折扣是一种安慰剂，并且仍然在行业中广泛使用，那么它们也许是一种吸引大客户的营销手段？

- “过去，我可以一次性支付一笔费用，然后让 Google Ads 发挥作用，直到没有更多预算。现在不行了。” - ([来源](https://news.ycombinator.com/item?id=36325785)) - Google Ads 用于实施上限实际值的概念。一种带有展期的每月预算，这是一种限制客户意外的最佳计费方案。在我看来，它一直是一种出售配额的方式。

## 优惠券和优惠券

- [Raising Prices is Hard](https://www.backblaze.com/blog/raising-prices-is-hard/) - 对其主要报价的提价进行了事后分析。他们想创建一个基于学分制度的扩展计划。这成为了一些最高级工程师的全职工作，并导致了一个为期六个月的项目。

- [Details on Expiring DigitalOcean Credits](https://blog.digitalocean.com/details-on-expiring-digitalocean-credits/) - 您必须添加信用时间限制的原因是：未使用的帐户在我们的资产负债表上作为负债。

- [Hacking Scooters: How I Created \$100k Worth Of Free Rides](https://fant.io/p/hacking-voi/) - 关于如何利用促销代码获得无限免费乘车的警示故事。

<!--lint ignore balanced-punctuation-->

- [China’s Pinduoduo reports theft of online discount vouchers to police](https://web.archive.org/web/20230404113232/https://www.reuters.com/article/us-pinduoduo-china/chinas-pinduoduo-reports-theft-of-online-discount-vouchers-to-police-idUSKCN1PE05J) - 诈骗的下一个层面是：“某网络集体利用平台漏洞‘盗取’价值数千万元的优惠券”。

- [Council Directive 2016/1065 as regards the treatment of vouchers](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32016L1065) - 关于涉及优惠券时适用增值税的欧洲指令。

- [The coupon code is a slap in the face](https://justinjackson.ca/the-coupon-code-is-a-slap-in-the-face) - 指出用户在没有优惠券的情况下遇到空白优惠券字段的负面后果。请参阅文章末尾的更新以及支持此轶事的研究。

## 税收

- [2017 Tax Software Developer's Guides](https://web.archive.org/web/20240227073911/https://www.mass.gov/lists/2017-tax-software-developers-guides) - 供开发人员测试其税法的测试用例列表。

- [{Digital,Cloud,Electronic,Online} Services VAT Rate Database](https://github.com/kdeldycke/vat-rates) - 🆓 集中每个居住国（包括领土例外）对外国在线服务适用的增值税税率。

- [Global VAT & GST on digital services](https://www.avalara.com/vatlive/en/global-vat-gst-on-e-services.html) - 要求对外国提供的在线服务征税的国家/地区列表。

- “英国超市（……）向您收取后端卡处理费用，但他们会从您的结帐价格中扣除该费用。” （[来源](https://news.ycombinator.com/item?id=22047028)) - 这允许他们[将加工费的增值税作为进项税](https://www.gov.uk/guidance/vat-guide-notice-700#section4)。

- [Streamlined Sales Tax Governing Board](https://www.streamlinedsalestax.org/about-us/about-sstgb) - 美国多州倡议，旨在实现销售税会计和征收的自动化和标准化。

### 欧洲增值税

- [How to correctly setup SaaS subscriptions to charge VAT in Europe](https://web.archive.org/web/20260220184109/https://medium.com/slight-pause/how-to-setup-saas-subscriptions-correctly-to-charge-vat-in-europe-d75d857b5d01) - “如果您认为您可以像我们一样设置一个简单的 Stripe 集成并继续前进，那么您就大错特错了。”

<!--lint disable double-link-->

- [Council Directive 2006/112/EC](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L:2006:347:FULL) - 欧盟关于增值税共同制度的参考。

<!--lint enable double-link-->

- [What does the "Reverse Charge" refer to?](https://news.ycombinator.com/item?id=8767388) - 答案：企业将增值税处理责任转移给客户的规定。

## 发票

发票具体化了消费的服务或购买的产品，等待通过付款交易进行结算。

- [On GCP invoiced billing](https://news.ycombinator.com/item?id=17517479) - [发票结算](https://cloud.google.com/billing/docs/how-to/invoiced-billing) 是在使用服务并开具发票后发生的 B2B 友好付款。在 GCP 上设置似乎很痛苦，但我怀疑这是试图减少（代价高昂的）欺诈的结果。

### 结构

<!--lint disable double-link-->

- [Content of EU invoices](https://web.archive.org/web/20260128155309/https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ%3AL%3A2006%3A347%3AFULL) - 关于增值税共同制度的理事会指令 2006/112/EC 第 226 条第 4 节（发票内容）详细介绍了欧盟发票上所需的信息。

<!--lint enable double-link-->

### 诚信

一旦开具，发票就必须是不可更改的。

- [Digital signatures: how Sleek leverages Cloud HSM to guarantee the integrity of legal documents](https://web.archive.org/web/20260113213039/https://medium.com/google-developers/digital-signatures-how-sleek-leverages-cloud-hsm-to-guarantee-the-integrity-of-legal-documents-a7bd3b82faf6) - 这是依靠 GCP 的 HSM 对文档进行数字签名并提供不可变的审计跟踪的好方法。可能适用于发票和合同协议。

- [OpenTimestamps](https://opentimestamps.org) - 超越上述解决方案，直接在比特币区块链上为不可变文档添加时间戳。

- [Credit note](https://en.wikipedia.org/wiki/Credit_note) - 由于发票是不可变的，因此全部或部分取消发票的唯一方法是生成贷方票据。

### 发电机

- [Manta](https://github.com/hql287/Manta) - 🆓 灵活的发票桌面应用程序，具有美观且可定制的模板。

- [InvoicePlane](https://github.com/InvoicePlane/InvoicePlane) - 🆓 一个自托管的开源应用程序，用于管理您的发票、客户和付款。社区项目，无付费版本。

- [InvoiceGenerator](https://github.com/by-cx/InvoiceGenerator) - 🆓 用于生成简单发票的 Python 库。

- [Ruby Invoicing Framework](https://github.com/code-mancers/invoicing) - 🆓 用于生成和显示发票（非常适合商业 Rails 应用程序）。允许灵活的业务逻辑；提供税务处理、佣金计算等工具。

- [klirr](https://github.com/sajjon/klirr) - 🆓 零维护 FOSS CLI 工具，用于生成漂亮的服务和费用发票。

### 提取器

- [InvoiceNet](https://github.com/naiveHobo/InvoiceNet) - 🆓 深度神经网络从发票文档中提取智能信息。

### 电子发票

- [Invoice Security Vulnerabilities](https://invoice.secvuln.info) - 欧盟推出了 XML 格式的“标准”，该标准存在一系列安全漏洞。

- [EU eInvoicing](https://ec.europa.eu/digital-building-blocks/sites/display/DIGITAL/eInvoicing+HUB) - 电子发票欧洲标准。

- [Factur-X](https://github.com/akretion/factur-x) - 🆓 支持法国和德国电子发票标准的 Python 库。

- [Universal Business Language](https://en.wikipedia.org/wiki/Universal_Business_Language) - 大多数发票软件都可以读取和写入 UBL 文档 (XML) 以进行数据传输。

- [GOBL](https://github.com/invopop/gobl) - 💸 JSON Schema、开源 Go 库、全球税务数据库，以及转换工具，全部合而为一。 Invopop 销售基于开放规范的托管电子发票 SaaS 实施。

## 付款方式

- [The Best Payment Gateway for Startups](https://web.archive.org/web/20230204235716/http://aynuriev.com/best-payment-gateway-startups/) - 顶级支付提供商及其定价和模式的基准。

- [Avoiding Double Payments in a Distributed Payments System](https://web.archive.org/web/20260516074518/https://medium.com/airbnb-engineering/avoiding-double-payments-in-a-distributed-payments-system-2981f6b070bb) - RDBMS 是为银行围绕交易而构建的，旨在解决该特定问题。然后 NoSQL 的出现迫使我们谨慎地实施系统以避免双重支出。

- [Monzo's bank transfers post-mortem](https://monzo.com/blog/2019/06/20/why-bank-transfers-failed-on-30th-may-2019/) - 或者为什么您应该为网关提供商的中断做好准备并解决该问题。

- [How to Build an Insurance Company](https://www.moderntreasury.com/journal/how-to-build-an-insurance-company) - 支付操作架构的重要性。

- [EU's Late Payment Directive](https://single-market-economy.ec.europa.eu/smes/sme-strategy/late-payment-directive_en) - 欧洲关于逾期付款适用费用的规则。

- [High failure rate of Point Of Sale devices in the upper Midwest](https://news.ycombinator.com/item?id=20043944) - 根本原因是什么？人们在低湿度的空气中穿着大量羊毛，会产生大量静电。

- ACH 的工作原理：开发人员视角，[第 1 部分](https://web.archive.org/web/20200101000000/https://engineering.gusto.com/how-ach-works-a-developer-perspective-part-1-339d3e7bea1)，[部分2](https://web.archive.org/web/20200101000000/https://engineering.gusto.com/how-ach-works-a-developer-perspective-part-2-7a890638c4dd)，[部分3](https://web.archive.org/web/20200101000000/https://engineering.gusto.com/how-ach-works-a-developer-perspective-part-3-cd98728cf31f), [部分4](https://web.archive.org/web/20200101000000/https://engineering.gusto.com/how-ach-works-a-developer-perspective-part-4-718a48cb8d2c), [部分5](https://web.archive.org/web/20200101000000/https://engineering.gusto.com/how-ach-works-a-developer-perspective-part-5-1d998bbcd82c)。

- [Handling system failures during payment communication](https://blogs.dropbox.com/tech/2017/09/handling-system-failures-during-payment-communication/) - Dropbox 尝试解释不可靠支付提供商的经历。

- [Why was I charged?](https://wpchrg.wordpress.com) - 在用户不断抱怨付款的情况下，WordPress 创建了专门的子域来帮助客户了解意外交易。诀窍是直接在银行对账单中添加此 URL。

- [Hyperswitch](https://github.com/juspay/hyperswitch) - 💸 用于支付处理的开源后端。 Juspay 销售 Hyperswitch Cloud 和自托管企业版； OSS 功能齐全，具有 90 多个连接器、保险库、路由、3DS 和欺诈编排。

- [moov](https://github.com/moov-io) - 🆓 用于金融技术的 Apache-2.0 库套件，包括 [`moov-io/ach`](https://github.com/moov-io/ach)、[`iso8583`](https://github.com/moov-io/iso8583) 和 [`watchman`](https://github.com/moov-io/watchman)。上面没有付费产品。

- [Fintech Open Source Foundation](https://github.com/finos) - 🆓 Linux 基金会项目托管金融服务开源项目。

### 收据

收据使付款交易具体化。

- [The humble receipt gets a brilliant redesign](https://susielu.com/data-viz/reviziting-the-receipt) - 当 Netflix 数据工程师重新查看收据时。

- [The long, long history of long, long CVS receipts](https://www.vox.com/the-goods/2018/10/10/17956950/why-are-cvs-pharmacy-receipts-so-long) - “CVS 是一家药店，就像其他药店一样，有一个重要的区别：收据很长。”

### 信用卡

最流行的支付设备。

- ['Is that even legal?': Companies may be sharing new credit or debit card information without you knowing](https://www.cbc.ca/news/business/banking-information-shared-with-third-parties-1.5102931) - 一些信用卡和借记卡公司提供“更新服务”，允许与商户共享新帐号和到期日期。 Visa 的实施称为 [VAU](https://developer.visa.com/capability/vau)，Mastercard 的实施称为 [ABU](https://developer.mastercard.com/product/automatic-billing-updater-abu/)。

- [Strong Customer Authentication](https://stripe.com/guides/strong-customer-authentication) - [支付服务指令](https://en.wikipedia.org/wiki/Payment_Services_Directive) 2、解释。

- [Address Verification System](https://en.wikipedia.org/wiki/Address_Verification_System) - 一种检查客户帐单地址与信用卡相关帐单地址是否匹配的系统。

### 银行账户

老式的付款方式：通过银行的方式。

- [A (shallow) dive into the American banking system](https://blog.yossarian.net/2019/12/25/A-shallow-dive-into-the-American-banking-system) - 杂项票据的收集主要集中在可路由账户的常见情况，即支票和储蓄。

- [Open IBAN](https://openiban.com) - 🆓 免费和公共的 IBAN 验证和计算网络服务。

- [Swift Codes](https://bank.codes/swift-code/) - Swift/BIC 代码仅供个人使用。

- [Swift Codes Repository](https://github.com/PeterNotenboom/SwiftCodes) - 🆓 全球银行 SWIFT/BIC 代码的静态 JSON 数据集，从上述网站抓取。最后一次刷新是在 2019 年，但仍然是最大的免费参考； SWIFT 代码变化缓慢，因此数据仍可广泛使用。

- [EPC QR code](https://en.wikipedia.org/wiki/EPC_QR_code) - 用于通过 SEPA 在银行账户之间转账的 QR 码欧盟标准。

### 网上支付

通常的汇款服务。

- [UPI 101: The Basics](https://blog.setu.co/articles/upi-101-the-basics) - “在本文中，我们将了解印度的统一支付接口。这个已有四年历史的支付方案已占印度数字支付的 40-45%。”

- [20 years of payment processing problems](https://kaimi.io/en/2022/07/20-years-of-payment-processing-problems-en/) - 过去 20 年支付 API 中所有出错的地方以及仍然出错的地方的大量集合。本文中暴露的任何问题如果没有得到解决，最终都会被盗走。

<!--lint ignore balanced-punctuation-->

- [The untold story of Stripe](https://www.wired.co.uk/article/stripe-payments-apple-amazon-facebook) - 其中我们了解到，“一旦营业额达到一定水平，Paypal 会自动将业务置于 21 至 60 天的滚动准备金状态，这意味着公司高达 30% 的收入可能会被锁定长达两个月。”

- [Idempotency in the context of payments](https://developers.google.com/standard-payments/reference/idempotency) - “幂等性可以防止竞争条件。幂等性意味着来自同一客户端的多个相同请求不会导致不同的最终状态。”

- [Optimizing payments with machine learning](https://dropbox.tech/machine-learning/optimizing-payments-with-machine-learning) - 描述经典的支付工作流程，然后介绍机器学习如何取代硬编码的业务规则并微调支付失败/重试循环以提高收费的成功率。

## 欺诈

您可以通过金钱奖励来开拓您的业务。准备好打击成群的欺诈者和可疑用户。

- [Detecting fraudulent activity in a cloud using privacy-friendly data aggregates](https://arxiv.org/pdf/1411.6721v1.pdf) - 讨论一种通过使用非侵入性、隐私友好的数据（计费数据）来检测欺诈活动（发起 DDoS 攻击、比特币挖掘等）的方法。

<!--lint disable double-link-->

- [Awesome List of IAM: Fraud links](https://github.com/kdeldycke/awesome-iam#fraud) - 专门用于与用户帐户相关的欺诈管理的部分，来自我们的姊妹存储库。

<!--lint enable double-link-->

- [Driving Global Fraud Losses Down While Empowering Business Growth](https://youtu.be/yJKWpTBVTiI?t=60) - 在 Uber Eats 的这次演讲中，我们从最大的支付处理商那里了解到，“业务增长且损失率下降在业内极为罕见”。此外，欺诈可以采取多种形式：对不易腐烂的商品退款、滥用促销、退款……

- [KYC and AML: beyond the acronyms](https://www.bitsaboutmoney.com/archive/kyc-and-aml-beyond-the-acronyms/) - KYC 是细致入微且模糊的，因为它是一个降低风险的随机过程。

- [Awesome Fraud Detection Research Papers](https://github.com/benedekrozemberczki/awesome-fraud-detection-papers) - 论文来自多个有关各种欺诈的会议：信用卡、支付交易、贷款、海关检查、洗钱网络等等。

- [Tazama](https://github.com/tazama-lf) - 🆓 用于检测欺诈和洗钱的开源实时交易监控软件，由 Tazama Linux 基金会项目管理。这只是一个定义规则、对规则进行加权并将其应用于交易的引擎。支付或金融交易没有任何具体内容。

- [Mojaloop Fraud Risk Management](https://github.com/mojaloop/fraud_risk_management/tree/master/typology-214/src/rules) - 🆓 Mojaloop 基金会的具体 AML 规则实现：交易镜像（90-100% 金额匹配窗口）、用于分层检测的多层收款人图遍历、账户休眠重新激活、大交易付款人、新收款人转账。回购协议已存档，但规则是静态参考资料，在 OSS 的其他地方很少见。

### 卡片

大多数欺诈都是利用最常见的支付设备：信用卡。

- [Reproducible Machine Learning for Credit Card Fraud detection](https://fraud-detection-handbook.github.io/fraud-detection-handbook/) - 关于如何识别交易模式的实用手册。

- [How I Stopped a Credit Card Thief From Ripping Off 3,537 People – and Saved Our Nonprofit in the Process](https://www.freecodecamp.org/news/stopping-credit-card-fraud-and-saving-our-nonprofit/) - 描述一种称为“卡测试”的欺诈技术，其中根据您的 API 检查大量被盗卡的有效性。

- [How Candy Japan got credit card fraud somewhat under control](https://www.candyjapan.com/behind-the-scenes/how-i-got-credit-card-fraud-somewhat-under-control) - 建议涉及尝试猜测哪些订单可能是欺诈的[警告信号](https://www.candyjapan.com/behind-the-scenes/fraudulent-transaction-warning-signs)，或试图使欺诈者的处境变得更加困难的对策。

- [Five Fun Fraud Facts](https://web.archive.org/web/20220327085654/https://blog.sift.com/2013/five-ecommerce-fraud-facts/) - 我们可以将另一个小特征集合提供给机器学习系统来检测欺诈。 HN 的评论还发现了[更多合格信号](https://news.ycombinator.com/item?id=6376350) 和[交易的衍生地理数据](https://news.ycombinator.com/item?id=6376221)。

- [Credit Card Fraud Detection using Autoencoders in Keras](https://web.archive.org/web/20200101000000/https://medium.com/@curiousily/credit-card-fraud-detection-using-autoencoders-in-keras-tensorflow-for-hackers-part-vii-20e0c85301bd) - 有关如何依靠异常检测来实施可疑卡交易的教程。

- [Training an ML model to score chargebacks](https://threadreaderapp.com/thread/1315452323330621440.html) - 平台网络效应的一个例子，它可以预测赢得争议的可能性。

- [How credit card thieves use free-to-play apps to launder gains](https://kromtech.com/blog/security-center/digital-laundry) - 为了防止滥用，服务提供商必须加强信用卡验证和帐户创建流程。

### 信任分数

基于信号集合的综合评分通常是用户可信度的最佳代表。当这些操作未自动触发时，客户支持大多数时候依赖他们采取行动。

- [GCP improved account management policies to better support customers](https://cloudplatform.googleblog.com/2018/07/improving-our-account-management-policies-to-better-support-customers.html) - 或者为什么过度依赖欺诈自动化可能会导致用户不满。

- [Digital Ocean's Update on Customer Shutdown Incident](https://blog.digitalocean.com/an-update-on-last-weeks-customer-shutdown-incident/) - 从商业角度来看，积极关闭用户服务器有助于防止欺诈者滥用免费资源，直到事实并非如此。

- [Awesome Credit Modeling](https://github.com/mourarthur/awesome-credit-modeling#readme) - 如何利用统计方法对申请人进行分类，以降低风险。其中有很多灵感和研究论文可以提高总体得分。

### 统计数据

自动检测欺诈的最佳工具。

- [Benford's law](https://en.wikipedia.org/wiki/Benford's_law) - 数字分布可能是会计欺诈的信号。

- [Integer percentages as electoral falsification fingerprints](https://arxiv.org/pdf/1410.6059.pdf) - 本着与上述相同的精神，本文表明选举中报告整数的频率是人为异常的信号。可能适用于某些反欺诈领域。

- [Huber loss](https://en.wikipedia.org/wiki/Huber_loss) - “稳健回归中使用的损失函数，与平方误差损失相比，对数据中的异常值不太敏感。”

- [Peak Detection in the Python World](https://blog.ytotech.com/2015/11/01/findpeaks-in-python/) - 检测异常值的简单方法。

- [Method to check if you swapped 2 digits](https://news.ycombinator.com/item?id=39021273) - 在隔离双分类帐中的错误时采用的标准手动会计技巧。

### 计费

- [More than 600 million users installed Android 'fleeceware' apps from the Play Store](https://www.zdnet.com/article/more-than-600-million-users-installed-android-fleeceware-apps-from-the-play-store/) - 一种新的欺诈行为，即应用程序在试用期结束后默默地继续向用户收费。

- [CEO Fraud](https://www.knowbe4.com/ceo-fraud) - 负责收款的计费团队是此类欺诈的受害者，其中首席执行官被冒充来赞扬特殊的支付交易。

- [The Challenges of Operating a Computing Cloud and Charging for its Use](https://web.stanford.edu/class/cs349d/docs/theimer.pdf) - 跳过 AWS VP 演示的前 90%（关于一般系统可靠性）。最后四张幻灯片很好地总结了计费云服务的含义，特别是使用软配额来限制欺诈。

- [Fraud in Telephony Networks](http://www.s3.eurecom.fr/docs/eurosp17_sahin.pdf) - 大多数电话欺诈都围绕微交易的计费和计量。本文采用分类法（第 6 页）来区分根本原因、漏洞、利用技术以及欺诈者从中受益的方式。

## 用户体验/用户界面

当涉及到金钱时，用户很容易生气。 UX 和 UI 可能有助于减少挫败感。

- [Apple In-app purchase Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/in-app-purchase) - 有关如何使[自动续订订阅](https://developer.apple.com/app-store/subscriptions/)变得用户友好的指南和建议。

- [Which has a higher conversion rate: A single long ecommerce checkout form or a multi-step one?](https://capitalandgrowth.org/questions/2055/which-has-a-higher-conversion-rate-a-single-long-e.html) - 首先关注购物车中的其他事情，例如通过在信用卡和完成步骤附近添加保证（信任标记、推荐）以及您可能在产品探索过程早期使用过的一些保证语言来缓解焦虑和事后猜测。

- [We tried to make billing backendless](https://useautumn.com/blog/backendless) - 由于安全原因，尝试将计费体验从后端转移到前端失败。

- [Pricing pages design](https://pricingpages.design) - 来自各个 SaaS 公司的定价页面集合，以获得如何展示报价的灵感。

## 商业智能

作为计费管道的利益相关者，您掌握所有关键数据来衡量和报告业务的健康状况。

### 指标

值得监控的关键绩效指标 (KPI) 的定义和收集。

- [Startup financial models - 12 templates compared for SaaS](https://www.stephnass.com/blog/startup-financial-model) - 这是获得更好的运营可见性的重要灵感来源。

- [16 Startup Metrics](https://a16z.com/16-startup-metrics/) - 两个关键指标是客户获取成本（CAC）和客户终身价值（CLV）。

- [Thinking about growth and profit](https://jlongster.com/thinking-growth-profit) - 讨论投资、利润和增长之间的关系，以及它如何影响定价、免费试用和计划结构的决策。

- [A Quantitative Approach to Product Market Fit](https://tribecap.co/a-quantitative-approach-to-product-market-fit/) - 上面生成的指标具有更大的影响力，因为它们被用作验证产品市场契合度的重要信号。

- [Startup growth calculator](http://growth.tlb.org) - 适合初创公司的简单而有效的交互式盈利计算器。

- [An Overview of Visa](http://minesafetydisclosures.com/blog/2019/7/23/part-ll-an-overview-of-visa) - Visa 商业模式和指标的详细分析。

- [The SaaS Financial Model You'll Actually Use](https://web.archive.org/web/20230205234207/https://baremetrics.com/blog/saas-financial-model) - 完整了解一家初创公司的财务状况，为您提供额外的背景信息，让您了解您生成的指标如何适应更大的情况。

### 客户终身价值

您为每个客户创造了多少价值？客户终身价值（CLV，或终身价值的 LTV）对此进行了量化。了解并采取行动是企业销售工作中最重要的部分。

- [You're all calculating churn rates wrong](https://web.archive.org/web/20260204065339/https://medium.com/swlh/youre-all-calculating-churn-rates-wrong-cbab072cd992) - “从表面上看，客户流失率似乎是客户生命周期变化的自然指标。让我们深入探讨一下为什么事实并非如此。”流失率并不是计算 CLV 的有意义的指标：在客户生命周期内，流失概率不是恒定的。大多数时候是因为您的免费试用和优惠券。本文说明了用于对客户退出概率进行建模的分布的影响。

- [How to project customer retention](https://faculty.wharton.upenn.edu/wp-content/uploads/2012/04/Fader_hardie_jim_07.pdf) - 一篇开创性的论文，与上面的相比，采用了更强的方法：[指数分布被几何模型取代](https://news.ycombinator.com/item?id=24833319)，它更适合离散时间间隔，如月度合约，前者更适合连续时间过程。

- [Survival Analysis For Customer Retention](https://two-wrongs.com/survival-analysis-for-customer-retention.html) - 说明如何使用生存函数（例如 [Kaplan-Meier 生存曲线](https://two-wrongs.com/bootstrapping-kaplan-meier-confidence-intervals.html)）更好地对保留进行建模。

- [RFM (customer value)](https://en.wikipedia.org/wiki/RFM_%28customer_value%29) - CLV 的精细模型，用于根据新近度、频率和货币价值对用户进行细分。

<!--lint ignore balanced-punctuation-->

- [Churn Prediction](https://towardsdatascience.com/customer-churn-prediction-with-text-and-interpretability-bd3d57af34b1/) - “如何通过将预测方法应用于您的所有行动，以简单的方式使用 Python 来推动公司的发展。”依赖于 XGBoost 二元分类。

- [PyMC-Marketing](https://github.com/pymc-labs/pymc-marketing) - 🆓 一个功能齐全的 Python 包，用于根据用户的“活着”和“死亡”状态来分析他们。 Apache-2.0 库由 PyMC Labs 管理，该实验室仅销售与其相关的咨询服务（无付费库层）。

### 数据工程

为了实现数据生产和消费的工业化，您需要数据工程师来清理、保存和整合数据。只有在获得这些数据基础之后，您可能会考虑聘请数据科学家。

- [AI vs Data Science vs Data Engineering](https://web.archive.org/web/20171009002725/https://blog.insightdatascience.com/how-emerging-ai-roles-fit-in-the-data-landscape-d4cd922c389b?gi=ebcf517502c7) - “数据工程师构建数据管道和基础设施，以确保转换数据的持续可用性。数据科学家根据这些数据分析和构建模型，以开发新产品功能或推动业务盈利。”对于人工智能专业人士来说，他们的重点是认知自动化。

- [Ten Ways Your Data Project is Going to Fail](https://www.martingoodson.com/ten-ways-your-data-project-is-going-to-fail/) - 你不需要数据科学家。 “对于 ETL，请聘请数据工程师。对于报告，请聘请 BI 分析师。结束。”

- [Cargo cult data science](http://blog.richardweiss.org/2017/07/25/data-science-in-organizations.html) - “数据科学最好被视为一种公司文化，而不是一套技术。然而，许多公司会尝试通过获取数据科学技术来创造这种公司文化，而不是致力于他们的文化。”

- [Why not use Double or Float to represent currency?](https://web.archive.org/web/20250524184249/https://stackoverflow.com/questions/3730019/why-not-use-double-or-float-to-represent-currency/3730040#answer-3730040) - 由于精度原因：浮点数和双精度数无法准确表示我们用于货币的以 10 为基数的倍数。

- [Never Use Floats for Money](https://husobee.github.io/money/float/2016/09/23/never-use-floats-for-currency.html) - “这正是我们在尝试用二进制表示 10^-1 或 0.1 时遇到的问题。0.1 或 0.01 没有精确的二进制表示。”

- [The Soul of an Old Machine: Revisiting the Timeless von Neumann Architecture](https://ankush.dev/p/neumann_architecture) - 甚至在第一台通用计算机 (EDVAC) 建成之前，浮点数就受到了怀疑：“冯·诺依曼并不完全相信我们可能需要浮点数。他对浮点数的批评非常直言不讳。”本文作者通过说明精度和舍入问题来补充这一批评。

- [European Spreadsheet Risks Interest Group - Horror Stories](https://eusprig.org/research-info/horror-stories/) - 一系列案例，其中不受控制和未经测试的电子表格模型导致收入损失、定价错误、决策失误、欺诈和系统性财务失败。

### 工具

用于构建可视化、仪表板、SQL 查询和深入分析数据的软件。

- [Practical Business Python](https://pbpython.com) - 一个博客，收集和传播有关如何在业务环境中更有效地使用 Python 的想法。

- [`redash`](https://github.com/getredash/redash) - 🆓 连接和查询您的数据源，构建仪表板以可视化数据并与您的公司共享。由 Databricks 所有，但托管的 SaaS 于 2021 年关闭，因此该项目现在由 Databricks 组织下的社区维护，没有付费的 Redash 产品。

- [Apache Superset](https://github.com/apache/superset) - 🆓 企业级商业智能 Web 应用程序，由 Apache 软件基金会管理。

- [Meltano](https://github.com/meltano/meltano) - 🆓 开源约定优于配置的产品，适用于整个数据生命周期，从加载数据到分析数据。 Meltano 仅销售托管云托管并支持 OSS 核心之上的 SLA。

## 竞品分析

大量资源用于跟踪在该领域运营的所有公司的当前状态和进度。

- [Patents on billing systems of the dot-com era](https://news.ycombinator.com/item?id=34773821) - 它们全部已被放弃并构成现有技术。这意味着没有什么可以阻止任何人实施或商业化这些概念。

- “你需要一个稍微复杂一点的开发团队来拼凑一个计费平台”（[来源](https://www.techemails.com/i/124009734/google-pms-on-stripe)） - Google 的产品总监致力于构建计费系统：你需要某种类型的工程师来解决该领域的问题。它并不适合所有人。

### 云提供商

- [AWS Cost Management announcements](https://aws.amazon.com/about-aws/whats-new/aws-cost-management/) - 添加到计费范围的所有新功能的来源。

- [AWS reserved instances vs saving plan](https://web.archive.org/web/20240602133657/https://www.prosperops.com/wp-content/uploads/2022/01/ris_and_savings_plans.png) - 不同方案的特征矩阵及其平均折扣。

- [GCP billing release notes](https://cloud.google.com/billing/docs/release-notes) - GCP 结算功能的最新变化。

- [GCP billing news](https://www.gcpweekly.com/gcp-resources/tag/billing/) - 来自非官方的 Google Cloud Platform 时事通讯。

- [More choice, less complexity: New Compute Engine pricing options on tap](https://cloud.google.com/blog/products/compute/more-choice-less-complexity-new-compute-engine-pricing-options-on-tap) - 近期 GCP 定价功能的总结。

- [Orbitera](https://en.wikipedia.org/wiki/Orbitera) - GCP 的结算子公司。

- [DigitalOcean Billing changelog](http://docs.digitalocean.com/release-notes/billing/) - DO 上的所有最新账单更新。

## 历史

- “拉里·佩奇 (Larry Page) 去了密歇根大学，使用了密歇根终端系统。(…) 当 Google 开发 App Engine 时，佩奇从 MTS 中获得了灵感，并劝告工程师效仿它的榜样。(…) 当我现在查看我的 AWS 和 GCP 账单时，感觉非常熟悉！” ([来源](https://news.ycombinator.com/item?id=35123587)) - 老式大学大型机和当前云服务之间的直接联系。

- [Product Development as Iterated Taste](https://commoncog.com/product-development-iterated-taste/) - AWS 牺牲了 S3 订阅定价的简单性，转而采用安全的成本跟踪策略，因为他们不知道用户将如何使用他们的服务。

- [Israel demanded Google and Amazon use secret 'wink' to sidestep legal orders](https://www.theguardian.com/us-news/2025/oct/29/google-amazon-israel-contract-secret-code#how-the-secret-code-works) - 使用编码金额的随机费用发票被用作绕过法律义务的隐藏信号。也许这就是您需要灵活的计费系统的原因。

- [£sd computing](https://en.wikipedia.org/wiki/%C2%A3sd#Computing) - IBM 1401 大型机 (1959) 可选地在硬件中支持英镑/先令/便士 (£sd) 货币算术。

- [Engineering and Operations in the Bell System](http://bitsavers.trailing-edge.com/communications/westernElectric/books/Engineering_and_Operations_in_the_Bell_System_2ed_1984.pdf) - 从第 #445 页开始，“10.5 计费设备和系统”部分描述了贝尔电话计费和定价的历史和技术演变。

- [The vanished grandeur of accounting](https://www.bostonglobe.com/ideas/2014/06/07/the-vanished-grandeur-accounting/3zcbRBoPDNIryWyNYNMvbO/story.html) - 会计绘画是荷兰艺术的一个重要流派。

- [Graphic methods for presenting facts](https://archive.org/details/graphicmethodsfo00brinrich/page/336/mode/2up?view=theater&ui=embed&wrapper=false) - 一种使用 1914 年用巴黎石膏制作的物理模型来优化定价的方法。

## 幽默

计费并不好笑。

- [Detax](https://detax.framer.website) - 小型企业避税产品的网站模型。

## 贡献

随时欢迎您的贡献！请先查看[贡献指南](.github/contributing.md)。

## 脚注

[标题图片](https://github.com/kdeldycke/awesome-billing/blob/main/assets/awesome-billing-header.jpg)基于[Denny]修改的[照片](https://web.archive.org/web/20221210200108/https://unsplash.com/photos/u2zSzMTwIjQ)穆勒](https://web.archive.org/web/20221210200108/https://unsplash.com/@redaquamedia)。

<!--lint disable no-undefined-references-->

<a name="intro-quote-def">[1]</a>: [*Sapiens: A Brief History of Humankind*](https://www.amazon.com/dp/0062316095?_encoding=UTF8&psc=1&linkCode=ll1&tag=kevideld-20&linkId=71ccb002da0dbe49c502954960175b66&language=en_US&ref_=as_li_ss_tl) (Harper, 2015). [[↑]](#intro-quote-ref)
