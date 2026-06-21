# 很棒的网络分析 [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)


用于构建、分析和可视化网络数据的资源[很棒的列表](https://github.com/sindresorhus/awesome)。

受到 [Awesome Deep Learning](https://github.com/ChristosChristofidis/awesome-deep-learning)、[Awesome Math](https://github.com/rossant/awesome-math) 等的启发。 2016年开始，此后不定期更新。

[![Adamic and Glance’s network of political blogs, 2004.](https://raw.githubusercontent.com/briatte/awesome-network-analysis/master/illustration.png)](http://www.maths.tcd.ie/~mnl/store/AdamicGlance2004a.pdf)

> [Adamic 和 Glance (2004)](https://dl.acm.org/itation.cfm?doid=1134271.1134277) 的美国政治博客网络（[预印本](http://www.maths.tcd.ie/~mnl/store/AdamicGlance2004a.pdf)）。

## 内容

- __[书籍](#books)__
  - [Classics](#classics)
  - [Dissemination](#dissemination)
  - [总体概述](#general-overviews)
  - [图论](#graph-theory)
  - [Method-specific](#method-specific)
  - [Software-specific](#software-specific)
  - [Topic-specific](#topic-specific)
- __[会议](#会议)__
- __[课程](#courses)__
- __[数据集](#数据集)__
- __[期刊](#期刊)__
- __[专业团体](#professional-groups)__
  - [研究小组（美国）](#research-groups-usa)
  - [研究小组（其他）](#research-groups-other)
- __[评论文章](#review-articles)__
  - [考古和历史网络](#archeological-and-historical-networks)
  - [书目、引文和语义网络](#bibliographic-citation-and-semantic-networks)
  - [生物、生态和疾病网络](#biological-ecological-and-disease-networks)
  - [复杂网络](#complex-networks)
  - [网络分析的伦理](#ethics-of-network-analysis)
  - [网络建模](#network-modeling)
  - [网络可视化](#network-visualization)
  - [社会、经济和政治网络](#social-economic-and-political-networks)
- __[精选论文](#selected-papers)__
- __[软件](#软件)__
  - [Algorithms](#algorithms)
  - [C/C++](#c--c)
  - [Java](#java)  
  - [JavaScript](#javascript)
  - [Julia](#julia)
  - [MATLAB](#matlab)
  - [Python](#python)
  - [R](#r)
  - [Stata](#stata)
  - [Syntaxes](#syntaxes)
  - [Tutorials](#tutorials)
- __[变量](#varia)__
  - [博客系列](#blog-series)
  - [虚构网络](#fictional-networks)
  - [网络科学](#network-science)
  - [小世界](#small-worlds)
  - [双模网络](#two-mode-networks)
- __[贡献指南](CONTRIBUTING.md)__
- __[许可证](#license)__

## 书籍

### 经典

- _[变革时期的见习者：社会关系的实验和案例研究](https://f.briatte.org/temp/sampson1968.pdf)_，作者：Samuel F. Sampson（未发表的博士论文，1968 年）。
- _[社交网络分析](https://uk.sagepub.com/en-gb/eur/social-network-analysis/book249668)_，作者：John Scott (2017)。
- _[社交网络分析。方法和应用](http://www.cambridge.org/ar/academic/subjects/sociology/sociology-general-interest/social-network-analysis-methods-and-applications)_，作者：Stanley Wasserman 和 Katherine Faust (1994)。
- _[网络的结构和动态](http://press.princeton.edu/titles/8114.html)_，由 Mark E.J. 编辑Newman、Albert-László Barabási 和 Duncan J. Watts - 600 页经典网络分析文章（2006 年）。

### 传播

> 针对非技术受众的易于理解的介绍。

- _[互联：社交网络的惊人力量及其如何塑造我们的生活](http://www.connectedthebook.com/)_，作者：Nicholas A. Christakis 和 James H. Fowler (2009)。
- _[链接：网络新科学](https://barabasi.com/book/linked)_，作者：Albert-László Barabási (2002)。
- _[网络素养：基本概念和核心思想](https://sites.google.com/a/binghamton.edu/netscied/teaching-learning/network-concepts)_，作者：NetSciEd 团队（c. 2016） - 提供多种语言版本（[论文](https://academic.oup.com/comnet/article-abstract/4/3/457/1745356)）。
- _[联系。小世界和开创性的网络理论](http://books.wwnorton.com/books/Nexus/)_，马克·布坎南 (2003)。
- _[六度：互联时代的科学](http://books.wwnorton.com/books/detail.aspx?ID=7599)_，作者：Duncan J. Watts (2003)。

### 总体概述

- _[社会科学分析。小实践指南](https://hal.science/hal-04052709)_，作者：Laurent Beauguitte，法语 (2023)。 [在线阅读](https://beauguitte.github.io/analysis-de-reseau-en-shs/)。
- _[有抱负的网络科学家地图集](https://www.networkatlas.eu/)_，作者：Michele Coscia (2021)。
- _[社交网络百科全书](http://sk.sagepub.com/reference/socialnetworks)_，由 George A. Barnett 编辑 - 涵盖各种与网络相关的主题（其中许多不是正式的）以及社交网络分析（2011）。
- _[社交网络分析和挖掘百科全书](https://www.springer.com/us/book/9781461461692)_，由 Reda Alhajj 和 Jon Rokne 编辑 (2014)。
- _[网络科学第一门课程](https://www.cambridge.org/us/academic/subjects/physicals/statistical-physicals/first-course-network-science)_，作者：Filippo Menczer、Santo Fortunato 和 Clayton A. Davis - 教程、数据集和其他资源 [在 GitHub 上](https://github.com/CambridgeUniversityPress/FirstCourseNetworkScience) (2020)。
- _[网络科学](http://networksciencebook.com)_，作者：Albert-László Barabási - 在线完整书籍（2016）。
- _[网络科学](http://www.nap.edu/catalog/11516/network-science)_，美国国家研究委员会 - 在线完整书籍（2005 年）。
- _[网络科学：理论与实践](http://eu.wiley.com/WileyCDA/WileyTitle/productCd-1118211014.html)_，作者：Ted G. Lewis (2011)。
- _[网络。简介](http://www-personal.umich.edu/~mejn/networks-an-introduction/)_，作者：Mark E.J.纽曼（2010）。
- _[网络、人群和市场：关于高度互联世界的推理](https://www.cs.cornell.edu/home/kleinber/networks-book/)_，作者：David Easley 和 Jon Kleinberg - 完整的预出版草案（[评论](http://bactra.org/reviews/networks-crowds-markets.html)；2010）。
- _[Réseaux sociaux et Structures relationnelles](https://www.puf.com/content/R%C3%A9seaux_sociaux_et_structs_relationnelles)_，作者：Emmanuel Lazega，法语（2014 年）。
- _[SAGE 社交网络分析手册](https://methods.sagepub.com/book/the-sage-handbook-of-social-network-analysis)_，由 John Scott 和 Peter J. Carrington 编辑（2011 年）。
- _[Sociologie des réseaux sociaux](http://pierremerckle.fr/2011/02/sociologie-des-reseaux-sociaux/)_，作者：Pierre Mercklé，法语（2011）。
- _[社会和经济网络](https://press.princeton.edu/books/paperback/9780691148205/social-and-economic-networks)_，作者：Matthew O. Jackson (2008)。
- _[社交网络分析与应用](https://www.wiley.com/en-gb/Social+Network+Analysis+with+Applications-p-9781118169476)_，作者：Ian McCulloh、Helen Armstrong 和 Anthony Johnson (2013)。
- _[社交网络。简介](https://olizardo.github.io/networks-textbook/)_，作者：Omar Lizardo 和 Isaac Jilbert - 免费在线阅读（2023 年）。
- _[社交网络：简介](https://www.routledge.com/products/9780415458030)_，作者：Jeroen Bruggeman（[相关材料](https://sites.google.com/site/introsocnet/)；2008 年）。
- _[研究社交网络。实证研究指南](http://press.uchicago.edu/ucp/books/book/distributed/S/bo15475096.html)_，作者：Marina Hennig _et al._ (2013)。
- _[了解社交网络。理论、概念和发现](https://global.oup.com/academic/product/understanding-social-networks-9780195379471)_，作者：Charles Kadushin (2012)。

### 图论

- _[组合学和图论](https://www.springer.com/us/book/9780387797106)_，作者：John Harris、Jeffry L. Hirst 和 Michael Mossinghoff (2008)。
- _[图论的迷人世界](http://press.princeton.edu/titles/10314.html)_，作者：Arthur Benjamin、Gary Chartrand 和 Ping Zhu (2015)。
- _[图论](https://www.springer.com/us/book/9781846289699)_，作者：John A. Bondy 和 Uppaluri S.R.穆蒂（2008）。
- _[图论](http://diestel-graph-theory.com/)_，作者：Reinhard Diestel - 在线完整书籍，还有中文和德文版本（2016 年）。
- _[图论](http://www.dtic.mil/dtic/tr/fulltext/u2/705364.pdf)_，作者：Frank Harary - 在线完整书（1969）。
- _[图表和有向图](https://www.crcpress.com/Graphs--Digraphs-Sixth-Edition/Chartrand-Lesniak-Zhang/p/book/9781498735766)_，作者：Gary Chartrand、Linda Lesniak 和 Ping Zhu (2016)。
- _[组合学和图论简介](https://www.whitman.edu/mathematics/cgt_online/cgt.pdf)_，作者：David Guichard - 在线完整书（2016 年）。
- _[现代图论](https://www.springer.com/us/book/9780387984889)_，作者：Belá Bollobás (1998)。

### 方法特定

- _[R 中的贝叶斯网络在系统生物学中的应用](https://www.springer.com/fr/book/9781461464457)_，作者：Radhakrishnan Nagarajan、Marco Scutari 和 Sophie Lèbre（[网站](http://www.bnlearn.com/book-useR/)；2013 年）。
- _[R 中的贝叶斯网络示例](http://www.crcpress.com/product/isbn/9781482225587)_，作者：Marco Scutari 和 Jean-Baptiste Denis（[网站](http://www.bnlearn.com/book-crc/)；2014 年）。
- _[树之书。可视化知识分支](https://papress.com/products/the-book-of-trees-visualizing-branches-of-knowledge)_，作者：Manuel Lima - 来自各个历史时期的数百个美丽的树图（2014）。
- _[社交网络的指数随机图模型](http://www.cambridge.org/9780521193566)_，由 Dean Lusher、Johan Koskinen 和 Garry Robins 编辑 (2013)。
- _[广义块建模。社会科学中的结构分析](http://www.cambridge.org/de/academic/subjects/sociology/sociology-general-interest/generalized-blockmodeling)_，作者：Patrick Doreian、Vladimir Batagelj 和 Anuška Ferligoj (2004)。
- _[图形绘制和可视化手册](https://www.crcpress.com/Handbook-of-Graph-Drawing-and-Visualization/Tamassia/9781584884125)_，由 Roberto Tamassia 编辑（[章节校样](https://cs.brown.edu/~rt/gdhandbook/)；2013 年）。
- _[历史网络手册。 Grundlagen und Anwendungen](http://www.lit-verlag.de/isbn/3-643-11705-2)_，由 Marten Düring _et al._ 编辑，德文 (2016)。
- _[指数随机图建模简介](https://uk.sagepub.com/en-gb/eur/an-introduction-to-exponential-random-graph-modeling/book237737)_，作者：Jenine K. Harris (2014)。
- _[Knoten 和 Kanten。 Soziale Netzwerkanalysis in Wirtschafts- und Migrationsforschung](http://www.transcript-verlag.de/978-3-8376-1311-7/knoten-und-kanten)_，由 Markus Gamper 和 Linda Reschke 编辑，德语 (2010)。
- _[Knoten 和 Kanten 2.0。 Soziale Netzwerkanalysis in Medienforschung und Kulturanthropologie](http://www.transcript-verlag.de/978-3-8376-1927-0/knoten-und-kanten-2.0)_，由 Markus Gamper、Linda Reschke 和 Michael Schönhuth 编辑，德语（2012 年）。
- _[Knoten 和 Kanten III。 Soziale Netzwerkanalysis in Geschichts- und Politikforschung](https://www.transcript-verlag.de/978-3-8376-2742-8/knoten-und-kanten-iii)_，由 Markus Gamper、Linda Reschke 和 Marten Düring 编辑，德语和英语 (2015)。
- _[推理网络分析](https://www.cambridge.org/highereducation/books/inferential-network-analysis/A7797D36A24647AA1F900CE7EF694C7E)_，作者：Skyler J. Cranmer、Bruce A. Desmarais 和 Jason Morgan (2020)。
- _[多层社交网络](http://multilayer.it.uu.se/book.html)_，作者：Mark E. Dickison、Matteo Magnani 和 Luca Rossi (2016)。
- _[社会科学的多级网络分析](https://www.springer.com/fr/book/9783319245188)_，由 Emmanuel Lazega 和 Tom A.B. 编辑斯奈德斯（2016）。
- _[多模式政治网络](https://www.cambridge.org/core/books/multimodal-political-networks/43EE8C192A1B0DCD65B4D9B9A7842128)_，作者：David Knoke、Mario Diani、James Hollway 和 Dimitri Christopulos (2021)。
- _[多元网络可视化](https://www.springer.com/us/book/9783319067926)_，由 Andreas Kerren、Helen C. Purch 和 Matthew O. Ward 编辑 (2014)。
- _[考古学中的网络分析](https://global.oup.com/academic/product/network-analysis-in-archaeology-9780199697090)_，由 Carl Knappett 编辑（2013 年；[法语评论](https://doi.org/10.4000/nda.2383)）。
- _[网络分析：方法论基础](https://www.springer.com/fr/book/9783540249795)_，由 Ulrik Brandes 和 Thomas Erlebach 编辑 - 涵盖网络中心性、聚类、块模型、空间网络等 (2005)。
- _[政治网络。结构视角](http://www.cambridge.org/ar/academic/subjects/sociology/political-sociology/political-networks-structural-perspective)_，作者：David Knoke (1994)。
- _[自我网络的社交网络分析：以参与者为中心的网络的社交网络分析](https://uk.sagepub.com/en-gb/eur/social-network-analysis-for-ego-nets/book240391)_，作者：Nick Crossley _et al._ (2015)。
- _[了解大型时态网络和空间网络](https://www.wiley.com/en-gb/Understanding+Large+Temporal+Networks+and+Spatial+Networks%3A+Exploration%2C+Pattern+Searching%2C+Visualization+and+Network+Evolution-p-9780470714522)_，作者：Vladimir Batagelj _et等（2014）。

### 软件特定

- _[算法图论与 Sage](https://code.google.com/archive/p/graphbook/)_，作者 David Joyner、Minh Van Nguyen 和 David Phillips - 在线完整书（2013 年）。
- _[分析社交网络](https://sites.google.com/site/analyzingsocialnetworks/)_（使用 UCINET），作者：Stephen P. Borgatti、Martin G. Everett 和 Jeffrey C. Johnson (2013)。
- _[R 网络分析用户指南](https://www.springer.com/us/book/9783319238821)_，作者：Douglas A. Luke (2015)。
- _[数据科学和复杂网络：Python 的真实案例研究](https://global.oup.com/academic/product/data-science-and-complex-networks-9780199639601)_，作者：Guido Caldarelli 和 Alessandro Chessa (2016)。
- _[Pajek 探索性社交网络分析](http://www.cambridge.org/us/academic/subjects/sociology/research-methods-sociology-and-criminology/exploratory-social-network-analysis-pajek-2nd-edition)_，作者：Wouter de Nooy、Andrej Mrvar 和 Vladimir Batagelj（2011 年；还 [日语](http://www.tdupress.jp/books/isbn978-4-501-54710-3.html)和[中文](http://product.dangdang.com/22927985.html))。
- _[Gephi Cookbook](https://www.packtpub.com/big-data-and-business-intelligence/gephi-cookbook)_ (2015)。
- _[图形绘图软件](http://link.springer.com/book/10.1007/978-3-642-18638-7)_（涵盖许多程序），由 Michael Jünger 和 Petra Mutzel 编辑（2004 年）。
- _[社交网络方法简介](http://faculty.ucr.edu/~hanneman/nettext/)_（主要使用 UCINET），作者：Robert A. Hanneman 和 Mark Riddle - 在线完整书（2001 年）。
- _[掌握 Gephi 网络可视化](https://www.packtpub.com/networking-and-servers/mastering-gephi-network-visualization)_，作者：Ken Cherven (2015)。
- _使用 R/igraph 进行网络分析_，作者：Gabor Csárdi、Thomas Nepusz 和 Eduardo M. Airoldi（准备中）。
- _使用 Python/igraph 进行网络分析_，作者：Thomas Nepusz、Gabor Csárdi 和 Eduardo M. Airoldi（准备中）。
- _[使用 Gephi 进行网络图分析和可视化](https://www.packtpub.com/big-data-and-business-intelligence/network-graph-analysis-and-visualization-gephi)_，作者：Ken Cherven (2013)。
- _[R 社交网络分析](https://schochastics.github.io/R4SNA/)_ (R4SNA)，作者：Termeh Shafie 和 David Schoch（正在进行中）。
- _[初创公司的社交网络分析。在社交网络上寻找联系](http://shop.oreilly.com/product/0636920020424.do)_（使用 Python），作者：Maksim Tsvetovat 和 Alexander Kouznetsov（[代码](https://github.com/maksim2042/SNABook)；2011）。
- _[使用 R 进行网络数据统计分析](http://www.springer.com/us/book/9781493909827)_，作者：Eric D. Kolaczyk 和 Gabor Csárdi（[R 包](https://github.com/kolaczyk/sand)；2014 年）。

### 特定主题

- _[社区和网络：利用社交网络分析重新思考城市和社区研究](http://eu.wiley.com/WileyCDA/WileyTitle/productCd-0745654207.html)_，作者：Katherine Giuffre (2013)。
- _[比较政策网络。美国、德国和日本的劳工政治](http://www.cambridge.org/ar/academic/subjects/politics-international-relations/comparative-politics/comparing-policy-networks-labor-politics-us-germany-and-japan)_，作者：David Knoke 等人 (1996)。
- _[进行个人网络研究：实用指南](https://www.routledge.com/Conducting-Personal-Network-Research-A-Practical-Guide/McCarty-Lubbers-Vacca-Molina/p/book/9781462538386)_，作者：Christopher McCarty _et al._ (2019)。
- _[Egocentric Network Analysis with R](https://raffaelvacca.github.io/egocentric-r-book/)_ - 一本在线书籍/教程，涵盖了很多类似的内容。
- _[相连的过去。考古学和历史学网络研究面临的挑战](https://global.oup.com/academic/product/the-connected-past-9780198748519)_由 Tom Brughmans、Anna Collar 和 Fiona Coward 编辑（2016 年；[配套网站](http://connectedpast.net/)）。
- _[社会网络分析的发展：科学社会学研究](http://moreno.ss.uci.edu/)_，作者 Linton C. Freeman，英语和其他几种语言（2004 年；[后续论文，2011 年](http://moreno.ss.uci.edu/91.pdf)）。
- _[心理学中的动态网络：不仅仅是一幅漂亮的图画？](https://www.researchgate.net/publication/308874807_Dynamical_networks_in_psychology_More_than_a_pretty_picture)_，作者：Laura Bringmann（2016 年；博士论文）。
- _[复杂网络上的动态过程](http://www.cambridge.org/catalogue/catalogue.asp?isbn=9780521879507)_，作者：Alain Barrat、Marc Barthélemy 和 Alessandro Vespignani (2008)。
- _[经济网络：理论与计算](https://networks.quantecon.org/)_，作者：John Stachurski 和 Thomas J. Sargent (2022)。
- _[脑网络分析基础知识](https://www.elsevier.com/books/fundamentals-of-brain-network-analysis/fornito/978-0-12-407908-3)_，作者：Alex Fornito、Andrew Zalesky 和 ​​Edward Bullmore (2016)。
- _[犯罪网络内部](https://www.springer.com/us/book/9780387095257)_，作者：Carlo Morselli (2009)。
- _[邻居网络。本地和个人的竞争优势](https://global.oup.com/academic/product/neighbor-networks-9780199570690)_，作者：Ronald S. Burt (2010)。
- _[网络分析素养。网络分析的实用方法](https://www.springer.com/us/book/9783709107409)_，作者：Katharina A. Zweig (2016)。
- _[社会政策问题中的网络](http://www.cambridge.org/mx/academic/subjects/physicals/statistical-physicals/networks-social-policy-problems)_，由 Balázs Vedres 和 Marco Scotti 编辑（2012 年）。
- _[牛津网络经济学手册](https://global.oup.com/academic/product/the-oxford-handbook-of-the-economics-of-networks-9780199948277)_，由 Yann Bramoulllé、Andrea Galeotti 和 Brian Rogers 编辑 (2016)。
- _[作为动态网络的政策辩论：德国养老金政治和私有化话语](http://www.campus.de/buecher-campus-verlag/wissenschaft/politikwissenschaft/policy_debates_as_dynamic_networks-10287.html)_，作者：Philip Leifeld (2016)。
- _[小世界：有序与随机性之间的网络动态](http://press.princeton.edu/titles/6768.html)_，作者：Duncan J. Watts (2003)。
- _[通信网络理论](https://global.oup.com/academic/product/theories-of-communication-networks-9780195160376)_，作者：Peter Monge 和 Nosh Contractor (2003)。
- _[棋盘和网络。网络世界中的连接策略](http://yalebooks.yale.edu/book/9780300215649/chessboard-and-web)_，作者：Anne-Marie Slaughter (2017)；将网络科学应用于世界政治。
- _[迈向关系社会学](https://www.routledge.com/products/9780415480147)_，作者：Nick Crossley (2011)。
- _[Die Verbundenheit der Dinge。 Eine Kulturgeschichte der Netze und Netzwerke [事物的连通性。网络和网络的文化史]](http://www.kulturverlag-kadmos.de/buch/die-verbundenheit-der-dinge.html)_，作者：Sebastian Gießmann，德语（2014 年）。
- _[Verdeckte soziale Netzwerke im Nationalsozialismus。 Die Entstehung und Arbeitsweise von Berliner Hilfsnetzwerken für verfolgte Juden [国家社会主义中隐藏的社交网络：柏林受迫害犹太人援助网络的起源和工作方法]](http://www.degruyter.com/view/product/432196)_，作者：Marten Düring，德语（2015 年；[相关]出版物](http://martenduering.com/research/covert-networks-during-the-holocaust/) 和[英语视频演示](https://www.youtube.com/watch?v=SlQ7stSU-9w))。
- _[Visualisierung complexer Strukturen。 Grundlagen der Darstellung mehrDimensioner Netzwerke](http://www.campus.de/buecher-campus-verlag/wissenschaft/soziologie/visualisierung_komplexer_strukturen-2467.html)_，作者：Lothar Krempel，德语。

## 会议

> 关于网络分析的定期会议。

- [ASONAM - IEEE/ACM 社交网络分析和挖掘进展国际会议](http://asonam.cpsc.ucalgary.ca/)。
- [SNAA - 应用中社交网络分析研讨会](http://snaa.pwr.edu.pl/)。
- [CNDay - Cambridge Networks Day](http://www.cnn.group.cam.ac.uk/cambridge-networks-day) - 由剑桥网络召集。
- [CompleNet - 复杂网络国际研讨会](http://complenet.org/)。
- [EUSN - 欧洲社交网络会议](http://eusn.org/)。
- [GD - 国际图形绘制和网络可视化研讨会](http://www.graphdrawing.org/symposia.html)。
- [PolNet - Annual Political Networks Workshops and Conference](http://conference.polinetworks.org/) - 由 APSA 政治网络组织部分 (PolNet) 组织。
- [2009 年政治网络会议视频](https://vimeo.com/user2690333)。
- [NetSci - International School and Conference on Social Networks](http://www.netscisociety.net/) - 由网络科学学会（NetSci）组织。
    - [Large-scale Structures in Networks: Hidden Communities and Latent Hierarchies](http://danlarremore.com/CommunityDetection_and_Ranking_Larremore_2019.pdf) - [Dan Larremore](http://danlarremore.com/) 在 NetSci 2019 上的演讲。
- [Sunbelt - Social Networks Conference of the International Network for Social Network Analysis](http://www.insna.org/archives.html) - 由国际社交网络分析网络（INSNA）组织。

## 课程

- [复杂网络](http://cazabetremy.fr/Teaching/ComplexNetworks.html)，作者：Rémy Cazabet（里昂第一大学和里昂高等师范学院，2022 年）。
- [网络科学速查表](https://github.com/Yquetzal/NetworkScience_CheatSheets)。
- [复杂网络](https://www.uvm.edu/~pdodds/teaching/courses/2016-01UVM-303/)，作者：Peter Sheridan Dodds（佛蒙特大学，2016 年）<!-- ;推特：[@networksvox](https://twitter.com/networksvox)) -->。
- [复杂系统和复杂网络原理塔罗牌](https://www.uvm.edu/~pdodds/teaching/courses/2016-01UVM-303/tarotcards/)。
- [图论与应用](http://www.hamilton.ie/ollie/Downloads/Graph.pdf)，作者：Paul Van Dooren - 完整的讲座幻灯片（都柏林汉密尔顿学院，2009 年）。
- [图论（数学）](http://www.personal.psu.edu/cxg286/Math485.pdf)，作者：Christopher Griffin - 完整讲义（宾夕法尼亚州立大学，2012 年）。
- [图和网络](https://sites.google.com/a/yale.edu/462-562-graphs-and-networks/)，作者：Dan Spielman（耶鲁大学，2013 年）。
- [网络分析和建模（计算机科学）](https://aaronclauset.github.io/courses/5352/)，作者：Aaron Clauset - 完整的讲座幻灯片和阅读材料（科罗拉多大学，2022 年）。
- [网络、复杂性及其应用（媒体艺术与科学）](http://ocw.mit.edu/courses/media-arts-and-sciences/mas-961-networks-complexity-and-its-applications-spring-2011/)，作者：Cesar Hidalgo（麻省理工学院，2011 年）。
- [网络、人群和市场](https://www.edx.org/course/networks-crowds-markets-cornellx-info2040x-2)，作者：David Easley、Jon Kleinberg 和 Eva Tardos（[演示文稿](https://www.cornell.edu/video/cornellx-networks-crowds-and-markets)；康奈尔大学通过 edX，2016 年）。
- [网络（经济学）](https://ocw.mit.edu/courses/economics/14-15j-networks-spring-2018/)，作者：Mardavij Roozbehani 和 Evan Sadler（麻省理工学院，2018 年）。
- [网络（经济学）](https://hdl.handle.net/1721.1/119628)，作者：Daron Acemoglu 和 Asu Ozdaglar（麻省理工学院，2009 年）。
- [网络科学（计算机科学）](http://www.cc.gatech.edu/~dovrolis/Courses/NetSci/)，作者：Constantine Dovrolis - 大部分是开放获取读物（乔治亚理工学院，2015 年）。
    <!-- -   [Network Science (Physics)](https://www.barabasilab.com/course), by Albert-László Barabási, Sean Cornelius and Roberta Sinatra (Northeastern University, 2015). -->
- [政治网络：方法与应用](http://vanity.dss.ucdavis.edu/~maoz/networks/Spring%202011/pol279-11.htm)，作者：Zeev Maoz（加州大学戴维斯分校，2012 年）。
- [社会和经济网络：模型与分析](https://www.coursera.org/course/networksonline)，作者：Matthew O. Jackson（斯坦福大学，通过 Coursera，2015 年）。
- [社交网络分析](https://www.coursera.org/course/sna)，作者：Lada Adamic（密歇根大学，通过 Coursera，尚未运行）。
- [社交网络分析](http://www.mjdenny.com/workshops/SN_Theory_I.pdf) 和 [中级社交网络理论](http://www.mjdenny.com/workshops/Relational_Theory_Workshop.pdf)，作者：Matthew J. Denny - 研讨会笔记和幻灯片 (2014–5)。
- [Pajek 社交网络分析](http://mrvar.fdv.uni-lj.si/sola/info4/)，作者：Andrej Mrvar（卢布尔雅那大学，2016 年）。
- [社交网络](http://dennisfeehan.org/teaching/201701_demog260.html)，作者：Dennis M. Feehan（伯克利大学，2017 年）。
- [信息网络的结构](https://www.cs.cornell.edu/Courses/cs6850/2008fa/)，作者：Jon Kleinberg - 链接到许多不同的读物（康奈尔大学，2008 年）。

## 数据集

- [Animal Social Network Repository](https://bansallab.github.io/asnr/) - 大型“[社交网络的多物种存储库](https://doi.org/10.1038/s41597-019-0056-z)。”
- [贝叶斯网络存储库](http://www.bnlearn.com/bnrepository/)。
- [Bill Cosponsorship Networks in European Parliaments](https://github.com/briatte/parlnet) - 立法共同发起网络，R 格式。
- [Colorado Index of Complex Networks (ICON)](https://icon.colorado.edu/) - 由 Aaron Clauset 的研究小组描述和索引的大量网络。
- [Connectome](http://awesome.cs.jhu.edu/graph-services/download/) - 神经连接的综合图。
- [安然电子邮件数据集](https://www.cs.cmu.edu/~enron/)。
- [Eric D. Kolaczyk 的网络数据集](http://math.bu.edu/people/kolaczyk/datasets.html)。
- [Gephi 数据集](https://github.com/gephi/gephi/wiki/Datasets)。
- [Hetionet: an integrative network of disease](https://github.com/hetio/hetionet) - 复杂的生物网络，有多种格式可用，包括 JSON 和 [Neo4j](https://neo4j.het.io/browser/)。
- [igraphdata](https://CRAN.R-project.org/package=igraphdata) - R 以数据为中心的包。
- [igraphwalshdata](https://cran.r-project.org/package=igraphwalshdata) - 另一个以 R 数据为中心的包。
- [Interaction Web Database](http://www.ecologia.ib.usp.br/iwdb/) - 生态物种相互作用。
- [International Currencies 1890-1910](http://eh.net/database/international-currencies-1890-1910/) - 45 种货币之间国际联系的历史数据。
- [KONECT - The Koblenz Network Collection](http://konect.uni-koblenz.de/) - 其中包括 DBpedia 和 Wikipedia、GitHub 中的协作网络（[配套手册](https://arxiv.org/abs/1402.5500)）。
    <!-- -   [James H. Fowler’s Cosponsorship Network Data Page](http://jhfowler.ucsd.edu/cosponsorship.htm). -->
- [Linton Freeman’s Network Data](http://moreno.ss.uci.edu/data.html) - 超过 300 个 UCINET 格式的各种数据集。
- [Mangal](http://mangal.io/) - 分析、归档和共享生态网络数据的在线平台（[预印本](https://doi.org/10.1101/002634)、[Python包](https://github.com/mangal-wg/pymangal)、[R包](https://github.com/mangal-wg/rmangal))。
- [Manlio De Domenico 的复杂多层网络](https://manliodedomenico.com/data.php)。
- [马克·E.J.纽曼的网络数据](http://www-personal.umich.edu/~mejn/netdata/)（[可视化示例](http://www-personal.umich.edu/~mejn/networks/)）。
- [Network Repository](http://networkrepository.com/) - 包含数百个现实世界网络的完全可搜索数据库。
- [Network Science Book - Network Datasets](http://networksciencebook.com/translations/en/resources/data.html) - 来自 Albert-László Barabási 的《网络科学》一书的网络数据集。包括有关 IMDB 参与者、arXiv 科学合作、路由器网络、美国电网、蛋白质间相互作用、手机用户、引文网络、代谢反应、电子邮件网络和 nd.edu 网页的数据。
    <!-- -   [Nexus](http://nexus.igraph.org/) - Repository of network datasets in GraphML and igraph formats. -->
- [Norwegian Interlocking Directorate, 2002-2011](http://www.boardsandgender.com/data.php) - 关于挪威公司性别代表性的两种模式和一种模式数据。
- [Movie galaxies](http://moviegalaxies.com/) - 电影角色互动图数据库。
- [Pajek 数据集](http://vlado.fmf.uni-lj.si/pub/networks/data/)。
- [兰德尔·柯林斯的《哲学社会学》中的哲学家网络](https://www.uva.nl/profiel/n/o/w.denooy/w.denooy.html#tab_1)。
- [锡耶纳数据集](http://www.stats.ox.ac.uk/~snijders/siena/siena_datasets.htm)。
- [SocioPatterns Datasets](http://www.sociopatterns.org/datasets/) - 通过[SocioPatterns](http://www.sociopatterns.org/)感知平台获得的网络数据。
- [斯坦福大型网络数据集集合](https://snap.stanford.edu/data/index.html)。
- [State Networks](https://ippsr.msu.edu/public-policy/state-networks) - 美国国与国之间的关系变量，包括边界、旅行、贸易等。
- [tnet Datasets](https://toreopsahl.com/datasets/) - 加权网络数据。
- [UC Berkeley Social Networks Study (UCNets)](https://www.icpsr.umich.edu/web/ICPSR/studies/36975) - 来自五年小组研究的以自我为中心的数据（个人网络）。
- [UCI 网络数据存储库](http://networkdata.ics.uci.edu/)。
- [UCINET Datasets](https://sites.google.com/site/ucinetsoftware/datasets) - UCINET 格式的网络数据。

## 期刊

> 不完全开放获取的期刊被标记为“门控”。另请注意，下面列出的一些出版商正在[深受伤害](https://twitter.com/costofknowledge) 科学出版。

- _[应用网络科学](http://appliednetsci.springeropen.com/)_（Springer Open）。
- _[ARCS – 分析社会科学/社会科学网络分析](http://arcs.episciences.org/)_，英语和法语 ([GDR ARSHS](https://arshs.hypotheses.org/))。
- _[计算和数学组织理论](http://link.springer.com/journal/10588)_（Springer，门控）。
- _[计算社交网络](http://computationalsocialnetworks.springeropen.com/)_（Springer Open）。
- _[Connections](http://www.insna.org/connections.html)_ (INSNA).<!-- Twitter: [@ConnectionsSNA](https://twitter.com/ConnectionsSNA)。 -->
- _[IEEE 网络科学与工程汇刊](https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=6488902)_ (IEEE)。
- _[复杂网络杂志](https://academic.oup.com/comnet)_（牛津，门控）。
- _[数学社会学杂志](http://www.tandfonline.com/loi/gmas20)_（泰勒和弗朗西斯，门控）。
- _[社会结构杂志](https://www.exeley.com/journal/journal_of_social_struct)_ (INSNA)。 [旧档案](http://www.cmu.edu/joss)。
- _[网络通讯。网络与传播研究](https://journals.openedition.org/netcom/)_，英语和法语 (Revues.org)。
- _[网络科学](http://journals.cambridge.org/action/displayJournal?jid=nws)_（剑桥，门控）。
- _[在线社交网络和媒体](https://www.journals.elsevier.com/online-social-networks-and-media/)_（Elsevier，门禁）。
- _[REDES。 Revista hispana para el análisis de redes Sociales](http://revista-redes.rediris.es/)_，西班牙语 (INSNA)。
- _[社交网络分析和挖掘](http://link.springer.com/journal/13278)_（Springer，门控）。
- _[社交网络](http://ees.elsevier.com/son/default.asp)_（Elsevier，门控）。

## 专业团体

- [AFS RT 26 “Réseaux sociaux”](https://afs-socio.fr/rt/rt26/) - 法国社会学协会 (AFS) 专题网络，法语（[旧网站](https://web.archive.org/web/20160421164221/http://www.cmh.pro.ens.fr/reseaux-sociaux/)）。
- [APSA Political Networks](http://www.polinetworks.org/) - 美国政治科学协会 (APSA) 组织分部。<!-- Twitter：[@PolNetworks](https://twitter.com/PolNetworks)。 -->
- [ECPR Political Networks SG](https://politicalnetsecpr.wordpress.com/) - 欧洲政治研究联盟常设小组。<!-- Twitter：[@politicalnets](https://twitter.com/politicalnets)。 -->
- [GDR ARSHS - GDR Analyse de réseaux en sciences humaines et Sociales](https://arshs.hypotheses.org/)，法语 - 总部位于巴黎的研究小组。
- [Groupe FMR - Flux、Matrices、Réseaux](https://groupefmr.hypotheses.org/)，法语。<!-- Twitter：[@BaugLaurent](https://twitter.com/BaugLaurent)。 -->
- [INSNA - 国际社交网络分析网络](https://www.insna.org/) ([SOCNET 邮件列表](https://www.insna.org/socnet))。<!-- Twitter: [@SocNetAnalysts](https://twitter.com/SocNetAnalysts)。 -->
- [美国社会学协会 (ASA) 数学社会学分会](http://mathematicalsociology.org/)。<!-- Twitter: [@Math_Sociology](https://twitter.com/Math_Sociology)。 -->
- [NetSci - 网络科学协会](http://www.netscisociety.net/)。<!-- Twitter: [@netscisociety](https://twitter.com/netscisociety)。 -->
- [青年网络科学家协会 (SYNS)](https://society-of-young-network-scientists.github.io/)。支持早期职业网络科学家。<!-- Twitter: [@official_SYNS](https://twitter.com/official_SYNS)。 -->

### 研究小组（美国）

> 位于美国的以网络为中心的研究中心、（阅读）团体、研究所、实验室——凡是你能想到的。

- [Annenberg Networks Network (ANN)](http://uscann.tumblr.com/) - 南加州大学研究社交网络的研究小组。
- [Center for Applied Network Analysis (CANA)](https://usccana.github.io/) - 研究小组位于南加州大学医学院。
- [Channing Division of Network Medicine](http://www.brighamandwomens.org/research/depts/medicine/channing/default.aspx) - 布莱根妇女医院医学部研究部门。
- [Complex Human Networks Reading Group (CoHN)](http://alumni.media.mit.edu/~tanzeem/cohn/CoHN.htm) - 2001 年 2 月在麻省理工学院举办的研讨会的阅读清单。
- [杜克网络分析中心](https://dnac.ssri.duke.edu/)。
- [Interdependence in Governance and Policy Research Group](https://sites.psu.edu/desmaraisgroup/) - 由宾夕法尼亚州立大学的 Bruce A. Desmarais 领导。
- [印第安纳大学网络科学研究所 (IUNI)](http://iuni.iu.edu/)。
- [圣母大学跨学科网络科学与应用中心 (iCeNSA)](http://icensa.com/)。
- [肯塔基大学加顿商业与经济学院 LINKS 社交网络分析中心](https://sites.google.com/site/uklinkscenter/)。
- [罗格斯大学传播与信息学院的 NetSCI 实验室](http://netsci.rutgers.edu/)。
- [宾夕法尼亚大学安纳伯格传播学院网络动力学小组](http://ndg.asc.upenn.edu/)。<!-- Twitter: [@NDGannenberg](https://twitter.com/NDGannenberg)。 -->
- [社会系统中的网络相互依赖](http://www.skylercranmer.net/niss-lab/)（NISS 实验室） - 由俄亥俄州立大学的 Skyler J. Cranmer 领导。
- [西点军校美国军事学院 (USMA) 网络科学中心](http://www.usma.edu/nsc/)（[博客](http://blog.netsciwestpoint.org/)）。
- [Network Science IGERT at the University of California at Santa Barbara (UCSB)](http://networkscience.igert.ucsb.edu/) - 设有[NSF 资助](http://www.igert.org/) 研究生课程。
- [Networks, Computation, and Social Dynamics Lab](http://www.ncasd.org/) - 由卡特·T·巴茨 (Carter T. Butts) 领导。加州大学欧文分校[网络和关系分析中心](http://relationalanalysis.org/) (CNRA) 的一部分。
- [Northeastern University Network Science Institute](http://www.networkscienceinstitute.org/) - 拥有网络科学博士学位。
- [Northeastern University Center for Complex Network Research](https://www.northeastern.edu/research/centers/center-for-complex-network-research-ccnr/) - 由阿尔伯特·拉斯洛·巴拉巴西 (Albert-László Barabási) 领导。
- [Northeastern University MOBS Lab - Laboratory for the Modeling of Biological and Socio-technical Systems](http://www.mobs-lab.org/) - 由亚历山德罗·维斯皮尼亚尼领导。
- [Pacific Ecoinformatics and Computational Ecology Lab](http://foodwebs.org/) - 生态网络（“食物网”）的非营利研究小组。
- [北卡罗来纳大学教堂山分校 Peter J. Mucha 的研究小组](http://mucha.web.unc.edu/networks/)。
- [斯坦福网络分析项目](https://snap.stanford.edu/)，作者：[Jure Leskovec](https://cs.stanford.edu/~jure/)。
- [宾夕法尼亚大学沃伦网络与数据科学中心](http://warrencenter.upenn.edu/)。
- [耶鲁大学网络科学研究所 (YINS)](http://yins.yale.edu/)。

### 研究小组（其他）

> 位于美国境外的以网络为中心的研究中心、（阅读）团体、研究所、实验室——凡是你能想到的。

- [Cambridge Networks Network (CNN)](http://www.cnn.group.cam.ac.uk/) - 研究复杂网络的网络。
- [Centre for Business Network Analysis, University of Greenwich](http://www.gre.ac.uk/business/research/centres/cbna/home) - 专注于经济/组织网络分析。
- [Center for Network Science, Central European University, Budapest](http://cns.ceu.edu/) - 拥有网络科学博士学位。
- [Complex Networks](http://www.complexnetworks.fr/) - 研究小组设在巴黎。
- [Cx-Nets](http://www.cxnets.org/) - 四个复杂网络研究小组之间的虚拟协作。
- [Data Science Group](http://datasciencegroup.pl/) - 位于弗罗茨瓦夫的研究小组，研究复杂网络和其他网络相关主题。
- [Digital Humanities](http://cmb.huma-num.fr/) - 柏林马克布洛赫中心的跨学科研究小组，拥有许多网络科学项目。
- [Forschungscluster der Universitäten Trier und Mainz “Gesellschaftliche Abhängigkeiten und soziale Netzwerke”](http://www.netzwerk-exzellenz.uni-trier.de/)，德文。
- [GDR Analyse de réseaux en sciences humaines et sociales](https://arshs.hypotheses.org/) - 法国研究小组提供资金支持社会科学家网络分析培训和研讨会。
- [Historical Network Research (HNR)](http://historicalnetworkresearch.org/) - 为对历史研究网络分析感兴趣的学者提供的平台。
- [HNR 会议、研讨会和其他活动](http://historicalnetworkresearch.org/hnr-events/)。
    - [HNR Talks](https://vimeo.com/user11811027) - 视频，德语。
- [ANR-Lab - International Laboratory for Applied Network Research](https://anr.hse.ru/en/) - 俄罗斯小组位于莫斯科国立研究大学。
- [网络分析理论与方法（“TMSA”）暑期学校](https://anr.hse.ru/en/summer)。
- [Large Graphs and Networks](http://sites.uclouvain.be/networks/) - 鲁汶天主教大学研究小组（[官方页面](https://uclouvain.be/en/research-institutes/icteam/large-graphs-and-networks.html)）。
- [斯威本科技大学 MelNet 社交网络研究小组](http://www.swinburne.edu.au/fbl/research/transformative-innovation/our-research/MelNet-social-network-group/)。<!-- Twitter: [@melnetsna](https://twitter.com/melnetsna)。 -->
- [Mitchell Centre for Social Network Analysis, University of Manchester](http://www.socialsciences.manchester.ac.uk/mitchell-centre/) - 目前研究[隐蔽网络](http://www.socialsciences.manchester.ac.uk/mitchell-centre/research/covert-networks/)。<!-- Twitter: [@MitchellSNA](https://twitter.com/MitchellSNA)。 -->
- [Murata Laboratory](http://www.net.c.titech.ac.jp/) - 位于东京的研究小组，研究二元、三元和 k 元（超）网络。
- [NetLab](http://www.urbancentre.utoronto.ca/researchgroups/netlab.html) - 多伦多大学的研究网络，由巴里·韦尔曼 (Barry Wellman) 领导。
- [斯旺西大学网络科学研究中心](http://www.swansea.ac.uk/medicine/enterpriseandinnovation/networkscienceresearchcentre/)。
- [Network Dynamics](http://networkdynamics.org/) - 麦吉尔大学研究实验室，由 [Derek Ruths] 领导(http://www.derekruths.com/)
- [Networks, Data, and Society (NERDS)](https://nerds.itu.dk/) - 哥本哈根信息技术大学的研究小组。
- [Netzwerkerei](http://netzwerkerei.org/) - 关于犹太知识分子之间联系的历史研究项目。
- [ORIO - Observatoire des Réseaux Intra- et Inter-Organisationnels](http://blogs.sciences-po.fr/recherche-network-organization-institution-dynamics-multilevel/) - 关于网络和监管的研究计划。
    - [‘Réseaux et Régulation’ Conference Cycle](http://blogs.sciences-po.fr/recherche-network-organization-institution-dynamics-multilevel/sminaire-rseaux-et-rgulation/) - 研讨会在法国巴黎巴黎政治学院举行。
- [Redes-Sociales](http://www.redes-sociales.net/)，西班牙语 - 位于巴塞罗那自治大学的信息网络。
- [RES-HIST : Réseaux et histoire](https://reshist.hypotheses.org/)，法语 - 来自历史网络研究小组的博客文章。
- [RES-HIST 会议](https://reshist.hypotheses.org/?s=res-hist)。
- [SocioPatterns](http://www.sociopatterns.org/) - 使用无线传感器研究社交网络数据的跨学科研究小组。
- [SoNAR-C - 瑞士意大利大学社交网络分析研究中心 (USi)](http://www.sonarcenter.eco.usi.ch/)。
- [Topographies of Entanglements. Mapping Medieval Networks](https://oeaw.academia.edu/TopographiesofEntanglements) - 位于奥地利科学院的研究平台，专注于将网络理论和可视化应用于中世纪历史。
- [伦敦大学学院组织网络分析中心 (CONA)](https://www.ucl.ac.uk/cona)。
- [Virtual Observatory for the Study of Online Networks (VOSON)](http://vosonlab.net/) - 研究和软件开发项目位于澳大利亚国立大学。

## 评论文章

### 考古和历史网络

> 另请参阅参考书目 [Claire Lemercier 和 Claire Zalc](http://www.quanti.ihmc.ens.fr/Analyse-de-reseaux-bibliographie.html)（关于“_études Structurees_”的部分）、[历史网络研究小组](http://historicalnetworkresearch.org/resources/bibliography/) 和 [Tom布鲁曼斯]（https://archaeologicalnetworks.wordpress.com/network-science-bibliography/）。

- [Analyse de réseaux et histoire](https://doi.org/10.3917/rhmc.522.0088)，法语（_Revue d’histoire Moderne et contemporaine_，2005）。
- [Analyser les réseaux du passé en archéologie et en histoire](https://doi.org/10.4000/nda.2300)，法语 (_Les Nouvelles de l’Archéologie_, 2014)。
- [Geschichtswissenschaften 中的正式网络分析方法：Warum und Wie？ [历史上的正式网络方法：为什么和如何？]](http://www.studienverlag.at/data.cfm?vpath=openaccess/oezg-12012-lemercier&download=yes)，德文（[英文预印本](https://shs.hal.science/halshs-00521527); _Österreichische Zeitschrift für Geschichtswissenschaften_，2012）。
- [从解释学到数据到网络：历史来源的数据提取和网络可视化](http://programminghistorian.org/lessons/creating-network-diagrams-from-historical-sources) (_Programming Historian_, 2015)。
- [生物学中的图论和网络](https://doi.org/10.1049/iet-syb:20060038) ([预印本](https://arxiv.org/abs/q-bio/0604006);_IET Systems Biology_, 2007)。
- [Introduction à la Visualization de données : l’analysis de réseau en histoire](https://www.martingrandjean.ch/introduction-visualization-de-donnees-analysis-de-reseau-histoire/)，法语（_Geschichte und Informatik_，2015）。
- [简介：où en est l’analysis de réseaux en histoire？ [介绍：¿en qué punto se encuentra el análisis de redes en Historia?]](https://doi.org/10.5565/rev/redes.416)，法语和西班牙语（_REDES_，2011）。
- [网络和历史](https://doi.org/10.1002/cplx.10054) (_Complexity_, 2002)。
- [历史研究网络](http://www.themacrscope.org/?page_id=308)（《历史学家的宏观视野》，2013 年）。
- [考古学中的权力网络](https://doi.org/10.1146/annurev-anthro-102313-025901)（_人类学年度评论_，2014）。
- [Netzwerkanalysis in den Geschichtswissenschaften。历史学研究方法的历史网络分析Prozessen]（https://www.researchgate.net/publication/300723171_Netzwerk_in_den_Geschichtswissenschaften_Historische_Netzwerkanalysis_als_Methode_fur_die_Erforschung_von_historischen_Prozessen），德语（_[Prozesse.Formen，Dynamiken， Erklärungen]（https://www.springer.com/de/book/9783531176604）_，2015）。
——【考古网络分析的根与芽：形式网络考古用途的引文分析与回顾方法]（https://www.academia.edu/6925120/Brughmans_T._2014_._The_roots_and_shoots_of_archaeological_network_analysis_A_itation_analysis_and_review_of_the_archaeological_use_of_formal_network_methods._Archaeological_Review_from_Cambridge_29_1_）（_考古评论来自剑桥_，2014）。
- [通过网络思考：考古学中正式网络方法的回顾]（https://doi.org/10.1007/s10816-012-9133-8）（_考古方法与理论杂志_，2013）。

### 书目、引文和语义网络

- [评估引文网络本地动态的影响和质量](https://doi.org/10.1016/j.joi.2011.08.005) (_Journal of Informatics_, 2012)。
- [非典型组合和科学影响](https://doi.org/10.1126/science.1240474) (_Science_, 2013)。
- [关于书目网络](https://doi.org/10.1007/s11192-012-0940-1) (_Scientometrics_, 2013)。
- [动态科学共同作者网络](http://patrickdoreian.com/wp-content/uploads/2017/12/dynamic-scientific-coauthorship-networks.pdf) (_[科学动力学模型](https://www.springer.com/us/book/9783642230677)_, 2012)。
- [从经典出版物中提取引文网络](http://www.digitalhumanities.org/dhq/vol/10/2/000255/000255.html)（_数字人文季刊_，2016）。
- [自引、共同作者和关键词：科学家现场流动的新方法？](https://doi.org/10.1007/s11192-007-1680-5) (_Scientometrics_, 2007)。
- [社会语义框架]（https://doi.org/10.1142/S0219525913500136）（[预印本]（http://camille.roth.free.fr/travaux/roth--sociosemantic-systems-acs-proofs.pdf）；_复杂系统的进展_，2013年）。
- [认知社区的社会语义建模](https://ssrn.com/abstract=2452614)（APSA，2014）。
- [科学家研究策略的传统与创新](https://doi.org/10.1177/0003122415601618)（_社会学年度评论_，2015）。

### 生物、生态和疾病网络

- [生物网络](http://kops.uni-konstanz.de/handle/123456789/25907)（_图形绘制和可视化手册_，2014）。
- [交互组网络与人类疾病](https://barabasi.com/f/326.pdf) (_Cell_, 2011)。
- [网络分析：精神病理学结构的综合方法](https://doi.org/10.1146/annurev-clinpsy-050212-185608)（_临床心理学年度评论_，2013）。
- [Network Biology: Understanding the Cell’s Functional Organization](https://barabasi.com/f/147.pdf) - （细胞）网络分析的易懂介绍（_Nature Reviews Genetics_，2004）。
- [网络医学：基于网络的人类疾病方法](https://barabasi.com/f/320.pdf)（_Nature Review Genetics_，2011）。
- [社交网络与传染病的传播：艾滋病示例](https://doi.org/10.1016/0277-9536(85)90269-2)（_Social Networks_，1985）。
- [Structure and Dynamics of Molecular Networks: A Novel Paradigm of Drug Discovery. A Comprehensive Review](https://doi.org/10.1016/j.pharmthera.2013.01.016) - 还包括令人印象深刻的网络分析软件列表（_Pharmacology & Therapeutics_，2013）。

### 复杂的多层网络

- [The Architecture of Complexity](https://barabasi.com/f/226.pdf) - 从网络理论到复杂性理论（_IEEE 控制系统杂志_，2007）。
- [复杂系统和网络](https://www.science.org/toc/science/325/5939)（《科学》特刊，2009 年）。
- [多层网络简而言之](https://doi.org/10.1146/annurev-conmatphys-031218-013259)（_凝聚态物理年度回顾_，2019）。
- [复杂网络的统计力学](https://barabasi.com/f/103.pdf)（_现代物理学评论_，2002）。
- [复杂网络的结构和功能](https://doi.org/10.1137/S003614450342480) (_SIAM Review_, 2003)。

### 网络分析的伦理

- [关于社交网络分析 (SNA) 中数据输入和视觉输出的警告](https://doi.org/10.1111/j.1467-8551.2012.00835.x)（[预印本][conway2014]；_英国管理杂志_，2014 年）。
- [社交网络研究中的道德困境](https://www.sciencedirect.com/journal/social-networks/vol/27/issue/2)（《社交网络》特刊，2005 年）。
- [组织社会网络分析中的道德和战略问题](http://www.analytictech.com/borgatti/papers/ethics.pdf)（_应用行为科学杂志_，2003）。

[conway2014]：https://lra.le.ac.uk/bitstream/2381/36068/2/Draft%20BJM%20Revised%20(3rd%20iteration)%20Manuscript.pdf

### 网络建模

- [网络分析统计模型简史和开放挑战][fienberg2012]（_计算与图形统计杂志_，2012）。
- [统计网络分析中的基本模型和问题](https://projecteuclid.org/euclid.ssu/1504836152)（_统计调查_，2017）。
- [基于随机参与者的网络动力学模型简介](https://doi.org/10.1016/j.socnet.2009.02.004) ([预印本](http://www.stats.ox.ac.uk/~snijders/SnijdersSteglichVdBunt2009.pdf);_Social Networks_, 2010)。
- [导航推理网络分析的统计工具范围](https://doi.org/10.1111/ajps.12263)（_美国政治科学杂志_，2017）。
- [位置分析和块建模](http://link.springer.com/referenceworkentry/10.1007%2F978-1-4614-1800-9_138) (<!-- [预印本](http://patrickdoreian.com/NEW/wp-content/papers_resources/chapters/Positional_Analysis_and_Blockmodeling.pdf); -->_计算复杂性_，2012）。
- [社交网络进化和面向参与者的模型](https://doi.org/10.4000/msh.2750)（_数学与社会科学_，1997）。
- [社交网络统计模型](https://doi.org/10.1146/annurev.soc.012809.102709)（_社会学年度评论_，2011）。
- [A Survey of Statistical Network Models](https://dl.acm.org/citation.cfm?id=1734795) - 全书回顾（[预印本](https://arxiv.org/abs/0912.5410)；_机器学习的基础和趋势_，2010）。
- [网络生成模型的统一视图：模型、方法、机遇和挑战](https://arxiv.org/abs/1411.4070) ([视频演示](http://www.birs.ca/events/2015/5-day-workshops/15w5080/videos/watch/201504200944-Jacobs.html)； [NIPS 2014 研讨会](https://nips.cc/Conferences/2014/Schedule?type=Workshop)“[网络：从图形到丰富数据](https://410f84824e101297359cc81c78f45c7c079eb26c.googledrive.com/host/0Bz6WHrWac3FrWnA5MjZqb3lWa2c/)”)。

[fienberg2012]：http://www.stat.cmu.edu/~brian/780/hw01/Fienberg%20(2012)%20A%20Brief%20History%20of%20Statistical%20Models%20for%20Network%20Analysis%20and%20Open%20Challenges.pdf

### 网络可视化

- [政策网络可视化的探索](https://www.academia.edu/17565685/Explorations_into_the_Visualization_of_Policy_Networks)（_理论政治杂志_，1999）。
- [探索社交网络数据的图形技术](http://moreno.ss.uci.edu/87.pdf)（_社交网络分析中的模型和方法_，2005）。
- [社交网络可视化方法](http://moreno.ss.uci.edu/90.pdf)（_复杂性与系统科学百科全书_，2009；[海报版本](http://www.pfeffer.at/data/visposter/)）。
- [社交网络](http://moreno.ss.uci.edu/93.pdf)（_图形绘制和可视化手册_，2013）。

### 社会、经济和政治网络

> 另请参阅参考书目 [Eszter Hargittai 撰写](http://eszter.com/contract.html#socnet)、[Pierre François 撰写](http://pierrefrancois.wifeo.com/documents/Cours-rseau---biblio-gnrale.pdf) 和 [Pierre François 撰写]默克勒](http://socio.ens-lyon.fr/merckle/merckle_communications_2008_cargese_reseaux_nuls_biblio.pdf)。

- [关于社会关系分析中的角色概念的建议](https://doi.org/10.4000/msh.11969) (_Mathématiques et sciences humaines_, 2011)。
- [经纪](https://doi.org/10.1146/annurev-soc-081309-150054)（_社会学年度评论_，2012）。
- [物以类聚：社交网络中的同质性](https://doi.org/10.1146/annurev.soc.27.1.415)（_社会学年度评论_，2001）。
- [社交网络分析的混合方法](http://eprints.ncrm.ac.uk/842/)（ESRC NCRM 讨论文件，2010 年）。
- [网络分析和政治学](https://doi.org/10.1146/annurev.polisci.12.040907.115949)（_政治学年度评论_，2011）。
- [国际关系网络分析](https://www.cambridge.org/core/journals/international-organization/article/div-classtitlenetwork-analysis-for-international-relationsdiv/DE2910979C1B5C44C4CC13F336C5DE97)（_国际组织_，2009）。
- [社会科学中的网络分析](http://science.sciencemag.org/content/323​​/5916/892) (_Science_, 2009)。
- [网络与贸易](https://doi.org/10.1146/annurev-economics-080217-053506)（_经济学年度评论_，2018）。
- [社会心理学网络，从 Kurt Lewin 开始](http://link.springer.com/10.1007%2F978-1-4614-6170-8_79) (<!-- [预印本](http://patrickdoreian.com/NEW/wp-content/papers_resources/new_papers_4-13/Networks_in_Socia_Psychology_Lewin.docx);-->_[社交网络分析和挖掘百科全书](https://www.springer.com/us/book/9781461461692)_, 2014)。
- [理解经济行为的网络](https://www.aeaweb.org/articles?id=10.1257/jep.28.4.3)（_经济视角杂志_，2014）。
- [职位和角色](http://sk.sagepub.com/reference/the-sage-handbook-of-social-network-analysis/n29.xml) (<!-- [预印本](http://patrickdoreian.com/NEW/wp-content/papers_resources/new_papers_4-13/positions_and_roles.pdf); -->_[社交网络 SAGE 手册分析](http://www.sagepub.in/books/Book232753/)_，2011)。
- [社会与性：当代人口统计研究中的网络](http://repository.upenn.edu/psc_working_papers/41/)（PSC 工作论文系列，2013 年）。
- [恐怖主义和政治暴力研究中的社交网络分析](http://journals.cambridge.org/article_S1049096510001848)（[预印本](http://opensiuc.lib.siu.edu/cgi/viewcontent.cgi?article=1048&context=pn_wp)；_PS：政治科学与政治_，2011）。
- [社交网络与犯罪：推进该领域的陷阱和承诺](https://doi.org/10.1146/annurev-criminol-011518-024701)（_犯罪学年度回顾_，2019）。
- 城市社交网络：一些方法论问题和可能性（[_The Small World_](https://www.worldcat.org/title/small-world/oclc/925078340&referer=brief_results), 1989）。

## 论文精选

> 自愿列出的应用、认识论和方法论文章的简短列表，其中许多已成为网络分析课程的经典读物。面向积极主动的社会科学学生，之前很少或没有接触过网络分析。

- [大型互动的辅助来源。 Retour sur quelques propriétés déterminantes des réseaux sociaux issus de corpus documentaires](https://www.cairn.info/revue-reseaux1-2008-6-page-21.htm)，作者：Pascal Cristofoli，法语 - 根据大规模在线数据回顾关系社会学和网络分析的现状（_Réseaux_，2008）。
- 【物以类聚，还是朋友的朋友？使用指数随机图模型来调查青少年社交网络](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2831261/)，作者：Steven M. Goodreau、James A. Kitts 和 Martina Morris - 指数随机图建模的逻辑和应用的简单介绍（人口学，2001 年）。
- [情感链：青少年浪漫和性网络的结构](http://www.soc.duke.edu/~jmoody77/chains.pdf)，作者：Peter S. Bearman、James Moody 和 Katherine Stovel - 应用于情感和性关系网络的拓扑网络分析的经典示例（_美国社会学杂志_，2004 年）。
- [《物理评论》中的合著者和引用模式](https://doi.org/10.1103/PhysRevE.88.012814)，作者：Travis Martin _et al._ - 通过时间网络分析对科学出版生产力和协作进行高度典型的研究（[预印本](https://arxiv.org/abs/1304.0473)；_物理评论 E_， 2013）。
- [社会和技术网络的融合](https://www.cs.cornell.edu/home/kleinber/cacm08.pdf)，作者：Jon Kleinberg - 讨论互联网和社交媒体背景下的小世界效应和社会传染（_ACM 通信_，2008 年）。
- [Deux传统分析社会研究](https://www.cairn.info/revue-reseaux1-2002-5-page-183.htm)，作者：Michael Eve ([英文版](https://www.academia.edu/14524365/THE_TWO_TRADITIONS_OF_NETWORK_ANALYSIS)；_Réseaux_， 2002）。
- [同质性和传染在观察性社交网络研究中普遍混淆](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3328971/)，作者：Cosma R. Shalizi 和 Andrew C. Thomas - 为网络扩散和影响力的分析提出了非常重要的观点（_社会学方法与研究_，2011）。
- [La notion de réseau complexe : du réseau comme abstraction et outil à la Masse de données des réseaux sociaux en ligne](https://doi.org/10.4000/communicationorganization.4093)，作者：Alain Barrat，法语 - 复杂网络研究的无障碍介绍（_Communication & Organisation_，2013）。
- [网络分析、文化和代理问题](https://www.mustafaemirbayer.com/network-analysis-culture-and-the-pr)，作者：Mustafa Emirbayer 和 Jeff Goodwin (_American Journal of Sociology_, 1994)，以及 [关系社会学宣言](https://www.mustafaemirbayer.com/copy-3-of-bourdieu)，作者：Mustafa Emirbayer (_American Journal of Sociology_, 1997) - 社会关系科学的社会学基础。
- [网络理论，情节分析](https://sydney.edu.au/intellectual-history/documents/moretti_network_theory_plot_analysis.pdf)，作者：Franco Moretti - （虚构）网络分析在文学研究中的应用示例（_新左派评论_，2011）。
- [加权网络中的节点中心性：概括度和最短路径](https://doi.org/10.1016/j.socnet.2010.03.006)，作者：Tore Opsahl、Filip Agneessens 和 John Skvoretz - 探索网络中心性和距离度量对（正）值图的概括（_Social Networks_，2010；[同伴网站](https://toreopsahl.com/tnet/))。
- [无标度网络](https://barabasi.com/f/124.pdf)，作者：Albert-László Barabási 和 Eric Bonabeau - “网络无处不在”论点的早期、可理解的表述（《科学美国人》，2003 年）。
- [社交网络和因果推理](http://link.springer.com/chapter/10.1007/978-94-007-6094-3_17)，作者：Tyler J. VanderWeele 和 Weihua An - 回顾网络分析产生有意义的因果陈述的不同方式，以及网络分析这样做的固有局限性（_[社会因果分析手册研究](http://link.springer.com/book/10.1007/978-94-007-6094-3)_，2013)。
- [网络的表演性](https://kieranhealy.org/files/papers/performativity.pdf)，作者：Kieran Healy - 网络分析与科学研究的结合：社交网络，如金融市场，高度受到表演性的影响，即现实可能被其理论探究所改变的可能性（_欧洲社会学杂志_，2015）。
- [重温网络分析的基础](http://science.sciencemag.org/content/325/5939/414)，作者：Carter T. Butts - 选择正确的网络表示来构建研究问题。
- [稳健行动与美第奇家族的崛起，1400-1434](http://home.uchicago.edu/~jpadgett/papers/published/robust.pdf)，作者：John F. Padgett 和 Christopher K. Ansell - 对文艺复兴时期佛罗伦萨国家权力关系的经典分析（_美国社会学杂志_，1993 年）。
- [弱关系的强度](https://sociology.stanford.edu/sites/default/files/publications/the_strength_of_weak_ties_and_exch_w-gans.pdf)，作者：Mark Granovetter - 将网络分析应用于社会问题的经典示例：求职（_美国社会学杂志_，1973）。
- [分裂的纽带：国际货币体系的网络分析，1890-1910](http://www.stats.ox.ac.uk/~snijders/FlandreauJobst2005.pdf) (_经济史杂志_，2005) 和 [国际货币的经验：网络外部性、历史和持久性](https://doi.org/10.1111/j.1468-0297.2009.02219.x) (_The Economic Journal_, 2009)，均由 Marc Flandreau 和 Clemens Jobst 撰写 - 19 世纪末外汇体系的网络分析（[数据](http://eh.net/database/international-currencies-1890-1910/)）。
- [社交网络分析和网络科学主题](https://arxiv.org/abs/1404.0067)，作者：A. James O’Malley 和 Jukka-Pekka Onnela - 50 页的网络分析介绍，对其各个方面进行了恰到好处的详细介绍（_健康服务研究手册_，即将出版，2017 年）。

## 软件

> 要了解为什么列表的这一部分可能对某些人有用，请参阅 [Mark Round 的数据格式和软件工具图](http://mdround.blogs.com/usingnetworks/2009/07/sna-tools-and-formats-diagram-updated.html) (2009)。
> 本节中的几个链接来自 [NetWiki 共享代码](http://netwiki.amath.unc.edu/SharedCode/SharedCode) 页面、剑桥网络网络 [复杂网络分析资源列表](http://www.cnn.group.cam.ac.uk/Resources) 以及 Mark 的 [社交网络分析软件](http://www.gmw.rug.nl/~huisman/sna/software.html) 页面豪氏威马和 Marijtje A.J.范·杜因。有关该主题的最新学术评论，请参阅《国际社会和行为科学百科全书》第二版（2015 年）的[社交网络算法和软件](https://doi.org/10.1016/B978-0-08-097086-8.43121-1) 条目。
> 另请参阅[社交网络分析项目调查](https://docs.google.com/spreadsheets/d/1Xo-ehJatzmxMek6gPG0h-d7yRSuiO6_flViTQNMAku0/edit#gid=0)（[博客文章](http://pudo.org/blog/2013/12/21/sna-survey.html)），这是一项早期尝试绘制社交网络分析工具图表的尝试，该工具链接许多商业平台未包含在此列表中，例如[Detective.io](http://www.Detective.io/)。维基百科英文条目 [社交网络分析软件](https://en.wikipedia.org/wiki/Social_network_analysis_software) 还链接到许多商业广告，这些广告通常非常昂贵、过时，并且以任何合理标准衡量都远非出色。
> 以软件为中心的教程列在他们选择的程序下面：其他教程列在[下一节](#tutorials)。

- [ArcGIS Network Analyst](http://www.esri.com/software/arcgis/extensions/networkanalyst) - 基于网络的空间分析软件，用于解决复杂的路径问题。
- [CFinder](http://www.cfinder.org/) - 跨平台 Java 程序，通过 Clique Percolation Method (CPM) 识别集群和社区。
- [Circos](http://circos.ca/) - 用于生成网络数据循环布局的跨平台程序，用 Perl 编写。
- [Cytoscape](http://www.cytoscape.org/) - 用于构建、分析和可视化网络的跨平台 Java 程序。也是一个 JavaScript 库。
    - [Network Analysis with Cytoscape Tutorial](https://archaeologicalnetworks.wordpress.com/resources/#cytoscape) - 通过考古和地理案例研究（2013）进行说明。
- [Discourse Network Analyzer (DNA)](http://www.philipleifeld.com/discourse-network-analyzer/discourse-network-analyzer-dna.html) - 具有网络导出功能的定性内容分析工具，用 Java 编写并与 R 集成。
- [E-Net](https://sites.google.com/site/enetsoftware1/) - 用于自我网络分析的 Windows 程序。
- [EgoNet](https://sourceforge.net/projects/egonet/) - 用于自我网络分析的跨平台 Java 程序。
- [EgoWeb](https://www.qualintitative.com/egoweb/) - 用于社交网络数据收集和处理的服务器端软件。
- [easyN](http://www.esyn.org/) - 旨在表示和共享基因相互作用网络以及 Petri 网模型的在线工具。
- [Gephi](https://gephi.org/) - 用于网络可视化的跨平台、免费和开源工具。
- [Clément Levallois 的 Gephi 教程](https://seinecle.github.io/gephi-tutorials/)。
- [Geographische Netzwerkvisualisierung mit dem Programm ‘Gephi’](http://www.podcampus.de/nodes/RJVZo)，德语（2016）。
- [Gephi 网络分析和可视化简介](http://www.martingrandjean.ch/gephi-introduction/) (2015)。
- [Gephi 实用社交网络分析](http://derekgreene.com/gephitutorial/) (2014)。
- [GLEAMviz Simulator](http://www.gleamviz.org/) - 用于预测人类流行病的跨平台工具。
- [Graph Commons](https://graphcommons.com/) - 用于绘制、分析和发布数据网络的协作平台。
- [Graphia](https://graphia.app/) - 用于可视化大型复杂网络的跨平台工具（[公告](https://www.cnn.group.cam.ac.uk/news/Graphia-April19)）。
- [Graphviz](http://www.graphviz.org/) - 用于使用 DOT 图形绘制语言绘制图形的跨平台软件。
- [Graphy](https://github.com/bruce/graphy) - 用 Ruby 编写的图论库。
- [GraphX](https://spark.apache.org/graphx/) - [Apache Spark](https://spark.apache.org/) 模块用于执行与图相关的并行计算。
- [Linkage](https://linkage.fr/) - 用于可视化和建模具有文本边缘的网络的在线工具。
- [Lynks](https://lynksoft.com/) - 基于网络的工具，用于简单的网络分析和可视化。
- [Mathematica](https://www.wolfram.com/mathematica/) - 具有图论和网络分析功能的跨平台程序。
    - [IGraph/M](https://github.com/szhorvat/IGraphM) - 使用 Mathematica 中的“igraph”库的接口，使用标准 Mathematica“Graph”对象。
- [Metamaps](https://metamaps.cc/) - 用于绘制网络的免费开源平台，目前处于测试阶段。
- [MuxViz](http://muxviz.net/) - 基于 R 和 GNU Octave 的跨平台、免费开源工具，用于研究多层网络。
- [Neo4j](http://neo4j.com/) - 开源、可扩展的图形数据库，由 [Linkurious](http://linkurio.us/) 等公司使用。
- [Network Canvas](http://networkcanvas.com/) - 一套免费开源的调查工具，用于以自我为中心的个人网络研究，包括[文档](https://documentation.networkcanvas.com)和[用户社区](https://community.networkcanvas.com)。
- [Node Overlap and Segregation Software](http://nos.alwaysdata.net/) - 基于网络的工具，用于计算 [Strona 和 Veech](https://doi.org/10.1111/2041-210X.12395) 的节点重叠和隔离测量。
- [Nodegoat](http://nodegoat.net/) - 基于网络的数据管理、网络分析和可视化环境（[博客](http://nodegoat.net/blog)）。
- [NodeXL](http://nodexl.codeplex.com/) - 免费的开源模板，用于使用 Microsoft Excel 探索网络图。
    - [The NodeXL Series](https://blogs.k-state.edu/it-news/tag/nodexl/) - 有关使用 NodeXL 的系列博客文章 (2013)。
- [ORA-LITE](http://www.casos.cs.cmu.edu/projects/ora/) - 用于动态元网络评估和分析的 Windows 程序。
- [OSoMe](https://osome.iu.edu/) - 社交媒体观察站是印第安纳大学的一个跨学科研究中心，提供浏览当前和过去社交媒体帖子的工具。
- [Pajek](http://mrvar.fdv.uni-lj.si/pajek/) - 用于大型网络分析的 Windows 程序，免费供非商业用途。
- [Analyse des réseaux : une opening à Pajek](https://quanti.hypotheses.org/512/)，法语（2011）。
- [La détection de communautés avec Pajek 3.6](https://groupefmr.hypotheses.org/544)，法语（2012）。
- [Palladio](http://hdlab.stanford.edu/palladio/) - 斯坦福大学[人文+设计研究实验室](http://hdlab.stanford.edu/) 基于网络的空间网络可视化工具。
- [PARTNER - Program to Analyze, Record, and Track Networks to Enhance Relationships](https://visiblenetworklabs.com/partner-cprm/) - 基于 Excel 的工具，用于通过调查构建网络。
- [PIGALE - Public Implementation of a Graph Algorithm Library and Editor](https://pigale.sourceforge.net/) - 用于分析平面图的 Windows 程序和 C++ 库。
- [PNet](http://www.swinburne.edu.au/fbl/research/transformative-innovation/our-research/MelNet-social-network-group/PNet-software/index.html) - （单模和多级）指数随机图模型 (ERGM) 的模拟和估计，用 Java 编写，适用于 Windows。
- [Polinode](https://www.polinode.com/) - 基于网络的平台，可分析网络数据并通过基于关系的调查收集网络数据。
- [PUCK - Program for the Use and Computation of Kinship data](http://www.kintip.net/) - 用于谱系网络分析的跨平台 Java 程序。
- [qgis-edge-bundling](https://github.com/ait-energy/qgis-edge-bundling) - 为 QGIS 处理工具箱实现力导向边缘捆绑。
- [Radatools](https://deim.urv.cat/~sergio.gomez/radatools.php) - 用于分析复杂网络的工具集，构建在 [Radalib](http://deim.urv.cat/~sergio.gomez/radalib.php) 之上，这是一个用 Ada 编写的库。
- [Retina](https://ouestware.gitlab.io/retina) - 用于共享 GEXF 和 GraphML 网络可视化的 Web 应用程序。
- [Scikit-network](https://github.com/sknetwork-team/scikit-network) - 用于图机器学习的开源库。
- [SageMath](https://www.sagemath.org/) - 免费的开源数学软件，具有广泛的[图形功能](http://doc.sagemath.org/html/en/reference/graphs/index.html)。
- [Segrada](https://www.segrada.org/) - 用于构建和可视化语义图数据库的跨平台工具。
- [Siena](https://www.stats.ox.ac.uk/~snijders/siena/) - 经验网络分析的模拟研究。以前是一个 Windows 程序，现在开发为 RSiena R 包。
- [SocNetV - Social Network Visualizer](https://socnetv.org/) - 跨平台程序，包括一个[简单的网络爬虫](https://socnetv.org/news/?post=socnetv-v16-released-with-a-working-web-crawler)来构建超链接网络。
- [SoNIA - Social Network Image Animator](http://web.stanford.edu/group/sonia/) - 用于可视化动态或纵向网络数据的工具。以前是一个 [Java 程序](https://sourceforge.net/projects/sonia/)（[示例电影](http://www.soc.duke.edu/~jmoody77/NetMovies/index.htm)），现在开发为 ndtv R 包。
- [SparklingGraph](https://sparkling-graph.github.io/) - 使用 Apache Spark 的 GraphX 模块执行大规模分布式网络计算的跨平台工具；用 Java 和 Scala 编写。
- [SPaTo Visual Explorer](http://www.spato.net/) - 用于复杂网络可视化和探索的跨平台程序。
- [StOCNET](http://www.gmw.rug.nl/~stocnet/StOCNET.htm) - 与 Siena 同一团队开发的几个 Windows 程序。
- [Tulip](http://tulip.labri.fr/) - 构建在 C++ 库之上的跨平台网络分析和可视化框架，带有专用于特定生物和物理网络的插件。也可以通过其[Python包](http://tulip.labri.fr/Documentation/current/tulip-python/html/index.html)获得。
- [UCINET](https://sites.google.com/site/ucinetsoftware/) - 用于分析社交网络数据的 Windows 商业软件包。
- [Uberlink](http://www.uberlink.com/) - 用于在线（超链接）网络分析的软件套件，由 [VOSON](http://vosonlab.net/) 研究项目开发。
    - [VOSON System](http://www.uberlink.com/software#voson) - 用于收集和分析在线网络数据的基于网络的软件。
- [NodeXL 的 VOSON 数据提供程序](http://www.uberlink.com/software#voson-nodexl)（[快速教程](https://blogs.k-state.edu/it-news/2013/04/09/the-nodexl-series-using-voson-for-hyperlink-network-analysis-part-9/)；将于 2016 年停止）。
    - [vosonR](http://vosonlab.net/tools) - VOSON 软件的 R 客户端（正在开发中）。
- [UNISoN](http://unison.sleonard.co.uk/) - 用于下载和可视化 Usenet 数据的跨平台程序。 [为硕士学位而开发](https://github.com/leonarduk/unison/wiki/MSc-Report-Abstract)。
- [VennMaker: An Actor-Centered Interactive Network Mapping Tool](http://www.vennmaker.com/?lang=en) - 用于自我网络分析的跨平台 Java 程序。
- [VennMaker for Historians：资料来源、社交网络和软件](http://revistes.uab.cat/redes/article/view/v21-during-bixier-kronenwett-stark)（也有西班牙语版本；2011 年）。
- [Visone](https://visone.ethz.ch/) - 跨平台Java网络分析和可视化程序，免费供非商业用途。
    - [Visone Tutorials](https://visone.ethz.ch/wiki/index.php/Tutorials) - 其中包括一项考古案例研究（2017 年）。
- [Vizster](http://vis.stanford.edu/jheer/projects/vizster/) - 用于可视化在线社交网络的跨平台 Java 程序。
- [VOSviewer](https://www.vosviewer.com/) - 用于构建和可视化文献计量网络的跨平台 Java 工具。

### 算法

> 网络布局和社区检测算法不适合接下来的任何小节。
> 另请参阅 [很棒的算法](https://github.com/tayllan/awesome-algorithms) 和 [很棒的算法可视化](https://github.com/enjalot/algovis) 列表，了解更多很棒的算法。

- [algo.graph](https://github.com/clojure/algo.graph) - 用 Clojure 编写的基本图论算法。
- [CONGA and CONGO](https://gregory.org/research/networks/software/conga.html) - 用 Java 编写的检测网络中重叠社区的算法。
- [ForceAtlas2](https://gephi.wordpress.com/2011/06/06/forceatlas2-the-new-version-of-our-home-brew-layout/) - Gephi 中包含力导向布局（[论文](http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0098679)）。
- [Linkcomm - Link Communities in Complex Networks](https://github.com/bagrow/linkcomm) - 社区检测算法，可用于 C++、Python [和 R](https://CRAN.R-project.org/package=linkcomm)。
- [MixNet - Erdös-Rényi Mixture Model for Networks](https://ssbgroup.fr/mixnet.html) - 社区检测方法，可用于 C++ 和 R。
- [OSLOM2 - Order Statistics Local Optimization Method](http://www.oslom.org/) - 聚类算法。
- [vbmod: Variational Bayesian Inference for Network Modularity](https://vbmod.sourceforge.net/) - [贝叶斯社区检测算法](https://arxiv.org/abs/0709.3512) 的 MATLAB 和 Python 实现。
- [weighted-modularity-LPAwbPLUS](https://github.com/sjbeckett/weighted-modularity-LPAwbPLUS) - Julia、MATLAB 和 R 实现了两种算法，用于在二分网络中查找加权模块化。

### C/C++

> 更多精彩的 C / C++ 内容，请参阅 [Awesome C](https://github.com/aleksandar-todorovic/awesome-c) 和 [Awesome C / C++](https://github.com/fffaraz/awesome-cpp) 列表。

- [Benchmark Graphs to Test Community Detection Algorithms](https://sites.google.com/site/santofortunato/inthepress2) - 用于生成加权和未加权图的 C++ 代码。
- [BGL - Boost Graph Library](https://www.boost.org/doc/libs/1_60_0/libs/graph/doc/) - C++ 库提供访问图形结构的通用接口。
- [igraph](https://igraph.org/) - 网络分析工具的C库；也作为 Python 和 R 的包存在。
- [MapEquation](https://www.mapequation.org/) - 多级社区检测的Infomap方法的C++代码。
- [Louvain Method](https://sites.google.com/site/findcommunities/) - [Louvain 多级社区检测算法]的 C++ 代码(https://arxiv.org/abs/0803.0476)。
- [networks.tb](https://networks-tb.sourceforge.net/) - 设计用于分析社会语义网络的 C 程序。在 Linux 和 Mac OS X 上运行。
- [OGDF - Open Graph Drawing Framework](https://ogdf.uos.de/) - 用于图表、网络和树布局的独立 C++ 类库。
- [OpenOrd: Large-scale Graph Layout (formerly DrL)](http://www.cs.sandia.gov/~smartin/software.html) - C++ 算法，也可作为 [Gephi 插件](https://gephi.org/plugins/#/plugin/openord-layout) 使用。
- [RAPIDS cuGraph](https://github.com/rapidsai/cugraph) - Python 包和 C/C++/CUDA 库专注于 GPU 加速图形分析。
- [Stanford Network Analysis Project](http://snap.stanford.edu/) - C++ 通用网络分析和图挖掘库。可作为 Python 库使用，也可通过 NodeXL 在 Microsoft Excel 中使用。
- [Walktrap](https://www-complexnetworks.lip6.fr/~latapy/PP/walktrap.html) - 实现[WalkTrap社区检测算法](https://arxiv.org/abs/physicals/0512106)的C++程序。

### 爪哇

- [GraphStore](https://github.com/gephi/graphstore) - 内存中图结构实现，为 Gephi 提供动力。
- [GraphStream](https://graphstream-project.org/) - 用于动态图建模和分析的 Java 库。
- [Mixer](https://github.com/keith-turner/mixer) - 原型展示了如何使用 [Apache Fluo](https://fluo.apache.org/) 将多个大型图连续合并为一个派生图。

### JavaScript

> 有关更多精彩 JavaScript 库，请参阅 [Awesome JavaScript](https://github.com/sorrycc/awesome-javascript) 列表。

- [Cytoscape.js](https://js.cytoscape.org/) - 网络分析和可视化库。
- [d3.js](https://d3js.org/) - JavaScript 可视化库，可以绘制[力导向图](http://bl.ocks.org/mbostock/4062045)。
- [d3-force：力导向图形布局](https://github.com/d3/d3-force) 使用速度 Verlet 集成。
- [d3-vector：将节点之间的连接定义为方向向量](https://github.com/thepeoplesbourgeois/d3-vector)，由角度和大小组成。
- [GENSI](http://www.tobiasstark.nl/GENSI/GENSI.htm) - 用于收集以自我为中心的网络数据的 JavaScript 图形工具（[论文](https://doi.org/10.1016/j.socnet.2016.07.007)）。
- [Gephi Lite](https://github.com/gephi/gephi-lite) - 基于 Web 的 Gephi 轻型版本。
- [GoJS](https://gojs.net/) - 用于绘制图表和多种类型的网络布局的可视化库。
- [Graphology](https://graphology.github.io/) - 健壮且多用途的 JavaScript“Graph”对象的规范和参考实现。
- [greuler](https://mauriciopoppe.github.io/greuler/) - 通过简单的 API 构建和操作图形的可视化库。由 d3.js 和 [WebCola](https://ialab.it.monash.edu/webcola/) 提供支持。
- [jLouvain](https://github.com/upphiminn/jLouvain) - Javascript 的 Louvain 社区检测（[示例](http://bl.ocks.org/emeeks/125db75c9b55ddcbdeb5)）。
- [NetworkCube](https://github.com/networkcube/networkcube) - “为领域科学家提供动态网络可视化。”有关演示示例，请参阅 [The Vistorian](https://networkcube.github.io/vistorian/)。
- [Oligrapher](https://github.com/public-accountability/oligrapher) - 图书馆最初开发的目的是可视化[美国精英中的“影响力网络”](https://littlesis.org/)。
- [Popoto.js](https://github.com/Nhogs/popoto) - 基于 d3.js 的库，提供基于图形的搜索界面。
- [Sigma](https://www.sigmajs.org/) - 专用于图形绘制的 JavaScript 库。
- [vis.js](https://visjs.org/) - 具有网络可视化功能的 JavaScript 库。
- [VivaGraphJS](https://github.com/anvaka/VivaGraphJS) - 图形绘制库（[ForceAtlas2插件](https://github.com/graphcommons/viva.forceatlas2)）。
- [viz.js](https://mdaines.github.io/viz.js/) - 在网页中使用 Graphviz。

### 朱莉娅

- [BayesNets.jl](https://github.com/sisl/BayesNets.jl) - 与贝叶斯网络一起使用的包。
    - [Smile.jl](https://github.com/sisl/Smile.jl) - [Smile C++ 库](http://www.bayesfusion.com/smile-engine) 的 Julia 包装器，涵盖贝叶斯网络和影响图。
- [EcologicalNetwork.jl](https://github.com/PoisotLab/EcologicalNetwork.jl) - 用于计算生态网络结构测量的包。
- [EvolvingGraphs](https://github.com/weijianzhang/EvolvingGraphs.jl) - 用于创建、操作和研究时间相关网络的软件包。
- [Julia 中的动态网络分析](http://eprints.ma.man.ac.uk/2376/01/julia_eg_report.pdf)。
- [Graphs.jl](https://github.com/JuliaLang/Graphs.jl) - 用于在 Julia 中操作图形对象的包。
- [在 Julia 的 Plotly 中创建网络图](http://badhessian.org/2014/05/creating-network-diagrams-in-plotly-from-julia/)。
    - [MetaGraphs](https://github.com/JuliaGraphs/MetaGraphs.jl) - Graphs.jl 具有多个异构元数据的图形数据结构。
- [JuliaGraphs](https://github.com/JuliaGraphs) - 用于网络分析的 Julia 软件包套件。
    - [GraphVisualize.jl](https://github.com/JuliaGraphs/GraphVisualize.jl) - 建立在 [GLVisualize.jl](https://github.com/JuliaGL/GLVisualize.jl) 之上的图形可视化。
    - [LightGraphs.jl](https://github.com/JuliaGraphs/LightGraphs.jl) - 注重性能和简单性的图形库。
    - [LightGraphsExtras.jl](https://github.com/JuliaGraphs/LightGraphsExtras.jl) - LightGraphs.jl 包的社区检测和其他功能。
    - [NetworkLayout.jl](https://github.com/JuliaGraphs/NetworkLayout.jl) - 图和树的布局算法。
    - [Networks.jl](https://github.com/JuliaGraphs/Networks.jl) - LightGraphs.jl 包的附加图形函数。
    - [GraphCentrality.jl](https://github.com/JuliaGraphs/GraphCentrality.jl) - 将网络测量添加到 Graphs.jl 包中。
- [MatrixNetworks.jl](https://github.com/nassarhuda/MatrixNetworks.jl) - 一种处理图/矩阵/网络结构的方法。
- [NetworkFlows.jl](https://github.com/Azzaare/NetworkFlows.jl) - 网络流算法包。
- [NetworkViz.jl](https://github.com/abhijithanilkumar/NetworkViz.jl) - 使用 [ThreeJS.jl](https://github.com/rohitvarkey/ThreeJS.jl) 来可视化使用 LightGraphs.jl 生成的图表。
- [该包的视频演示](https://youtu.be/kY5te9NwXo8?list=PLP8iPy9hna6SQPwZUDtAM59-wPzCPyD_S) 由其作者在 JuliaCon 2016 上进行。
- [PhyloNetworks.jl](https://github.com/crsl4/PhyloNetworks.jl) - 用于操作、分析和可视化系统发育网络的软件包。
- [TikzGraphs](https://github.com/sisl/TikzGraphs.jl) - 使用 TikZ 图形语言创建图形布局的包。

### MATLAB

> 另请参阅 [Python](#python) 部分中列出的 webweb 工具。

- [Brain Connectivity Toolbox](https://sites.google.com/site/bctnet/) - 用于对结构和功能性大脑连接数据进行复杂网络分析的工具箱，并提供许多相关项目的链接。
- [MatLab 复杂网络包](http://www.levmuchnik.net/Content/Networks/ComplexNetworksPackage.html)。
- [CONTEST](http://www.maths.strath.ac.uk/research/groups/numerical_analysis/contest) - 实现九种网络模型的随机网络工具箱。
- [Generalized Louvain](http://netwiki.amath.unc.edu/GenLouvain/GenLouvain) - Louvain 社区检测算法的变体。
- [MatlabBGL](https://dgleich.github.io/matlab-bgl/) - 基于 C++ Boost Graph Library 的图形库。
- [MATLAB RBN Toolbox](http://www.teuscher.ch/rbntoolbox/index.htm) - 随机布尔网络的模拟和可视化。

### 蟒蛇

> 以下许多内容均来自 Michał Bojanowski 等人的 [Google 电子表格](https://docs.google.com/spreadsheets/d/1vJILk2EW1JnR3YAwTSSqAV5mPkeXaezy45wOoafBpfU/edit#gid=0)。
> 另请参阅 [使用 Python 进行社交网络分析](https://www.youtube.com/watch?v=qgGqaBAEy3Q)，这是由 Maksim Tsvetovat 和 Alex Kouznetsov 在 PyCon US 2012 上提供的 3 小时教程（[代码](https://github.com/maksim2042/PyCon2012)）。
> 有关更多精彩 Python 软件包，请参阅 [Awesome Python](https://github.com/vinta/awesome-python) 和 [Awesome Python Books](https://github.com/Junnplus/awesome-python-books) 列表。

- [bokeh](https://bokeh.org/) - 用于在浏览器中实现交互式数据可视化的 Python 库，并支持网络。
- [cdlib](https://github.com/GiulioRossetti/cdlib) - Python社区检测库，具有60多种方法和评估/可视化功能。
- [CHSZLabLib](https://github.com/CHSZLab/CHSZLabLib) - 与 20 个高性能 C++ 库的统一 Python 接口，用于图分区、社区检测、切割、独立集和动态图算法。
- [dash-cytoscape](https://github.com/plotly/dash-cytoscape) - Python 中的交互式网络可视化库，由 Cytoscape.js 和 Dash 提供支持
- [graph-tool](http://graph-tool.skewed.de/) - 用于网络操作和分析的 Python 模块，为了速度主要用 C++ 编写。
- [Graphinate](https://erivlis.github.io/graphinate/) - Python 包旨在从数据源生成图表，构建在“networkx”之上。
- [graphviz](https://pypi.python.org/pypi/graphviz) - DOT 图形绘制语言的 Python 渲染器。
- [graspologic](https://github.com/microsoft/graspologic) - 用于单个和多个网络的统计算法、模型和可视化的 Python 包。
- [算法和模型教程](https://graspologic.readthedocs.io/en/latest/)。
- [hiveplot](https://pypi.python.org/pypi/hiveplot) - 用于在 matplotlib（一种更全面的网络可视化）上将网络绘制为蜂巢图的 Python 实用程序。
- [karateclub](https://github.com/benedekrozemberczki/karateclub) - Python 包，用于使用类似 scikit-learn 的 API 对图结构化数据进行无监督学习。
- [linkpred](https://github.com/rafguns/linkpred) - 评估未来网络快照中潜在链接的可能性。
- [littleballoffur](https://github.com/benedekrozemberczki/littleballoffur) - 用于使用类似 scikit-learn 的 API 从图形结构化数据中采样的 Python 包。
- [metaknowledge](http://networkslab.org/metaknowledge/) - Python 包将文献计量数据转化为作者身份和引文网络。
- [networkx](https://networkx.org/) - 用于创建、操作和研究复杂网络的结构、动力学和功能的 Python 包。
- [在 Python 中从头开始实现 ERGM](https://gist.github.com/dmasad/8509304)，使用 networkx 和 numpy (2014)。
    - [nxviz](https://github.com/ericmjl/nxviz/) - NetworkX 的可视化包。
- [nngt](https://nngt.readthedocs.io) - 与库无关的图形生成和分析，围绕“networkx”、“igraph”和“graph-tool”）。包括标准化图形测量、高级可视化、（地理）空间工具和神经科学模拟器界面。
- [npartite](https://github.com/ike002jp/npartite) - 用于 n 部分网络中的社区检测的 Python 算法。
- [parag](https://github.com/rraadd88/parag) - Python 中高阶图的交互式可视化。
- [pathpy](https://www.pathpy.net/) - 使用高阶和多阶图形模型分析网络上的时间序列数据。
- [PyGraphistry](https://github.com/graphistry/pygraphistry) - 用于提取、转换和可视化探索大图的 Python 库。
- [python-igraph](http://igraph.org/python/) - Python 版本的 igraph 网络分析包。
- [python-louvain](https://perso.crans.org/aynaud/communities/) - Louvain 社区检测算法的可靠实现。
- [Raphtory](https://www.raphtory.com/) - 用于构建和分析时间网络的平台。
- [RAPIDS cuGraph](https://github.com/rapidsai/cugraph) - Python 包和 C/C++/CUDA 库专注于 GPU 加速图形分析。
- [rustworkx](https://github.com/Qiskit/rustworkx) - 用 Rust 实现的高性能 Python 图形库。
- [scipy.sparse.csgraph](https://docs.scipy.org/doc/scipy/reference/sparse.csgraph.html#module-scipy.sparse.csgraph) - 基于稀疏矩阵表示的快速图算法。
- [Snap.py](http://snap.stanford.edu/snappy/index.html) - SNAP（用于分析和操作大型网络的通用高性能系统）的 Python 接口。
- [SnapVX](https://github.com/snap-stanford/snapvx) - 针对图上定义的问题的凸优化求解器。
- [tnetwork](https://github.com/Yquetzal/tnetwork) - 用于时态网络的 Python 库，特别是动态社区检测。
- [TQ (Temporal Quantities)](http://vladowiki.fmf.uni-lj.si/doku.php?id=tq) - 用于时态网络分析的 Python 3 库。
- [uunet](http://multilayer.it.uu.se/software.html) - 多层社交网络的工具。
- [相关书籍和数据](http://multilayer.it.uu.se/)。请参阅 R 版本的“multinet”。
- [webweb](https://webwebpage.github.io/) - MATLAB/Python 库，用于使用 d3.js 生成交互式网络可视化。

### R

> 更多精彩 R 资源，请参阅 [Awesome R](https://github.com/qinwf/awesome-R) 和 [Awesome R Books](https://github.com/RomanTsegelskyi/rbooks) 列表。另请参阅 Ian McCulloh 等人编写的 [此 Google 电子表格](https://docs.google.com/spreadsheets/d/1CoFGtrW85D9FsVcAE5-bcXVl6QOTncwXjFBYp4u2WgE/edit?usp=sharing)。
> 要将许多不同的网络模型结果转换为整齐的数据帧，请参阅 [broom](https://CRAN.R-project.org/package=broom) 包。要将许多不同的网络模型结果转换为 LaTeX 或 HTML 表，请参阅 [texreg](https://CRAN.R-project.org/package=texreg) 包。

- [amen](https://CRAN.R-project.org/package=amen) - 关系数据的加法和乘法效应模型。
- [backbone](https://CRAN.R-project.org/package=backbone) - 提供对仅保留重要边的加权网络进行二值化的方法。
    - [主干包简介](https://arxiv.org/abs/1912.12779)
- [Bergm](https://CRAN.R-project.org/package=Bergm) - 分析贝叶斯指数随机图模型 (BERGM) 的工具。<!-- 相关 Twitter：[@BayesianSNA](https://twitter.com/BayesianSNA)。 -->
- [bipartite](https://CRAN.R-project.org/package=bipartite) - 可视化二分（双模式）网络和计算生态研究中常用的指数的函数。另请参阅：“levelnet”R 包。
- [blockmodeling](https://CRAN.R-project.org/package=blockmodeling) - 为有价值的网络实施广义块建模。
- [bnlearn](https://CRAN.R-project.org/package=bnlearn) - [贝叶斯网络学习和推理](http://www.blnlearn.com/) 工具（[相关的 Shiny 应用程序](https://paulgovan.github.io/RiskNetwork)）。
- [brainGraph](https://CRAN.R-project.org/package=brainGraph) - 用于对大脑 MRI 数据进行图论分析的工具。
- [btergm](https://CRAN.R-project.org/package=btergm) - 通过自举伪似然拟合时间 ERGM 的工具。还提供 MCMC 最大似然估计、ERGM、TERGM 和随机参与者导向模型 (SAOM) 的拟合优度，以及用于 ERGM 和 TERGM 微观层面解释的工具。
- [CCAS](https://github.com/matthewjdenny/CCAS) - 通信网络的统计模型。
- [concoR](https://github.com/aslez/concoR) - CONCOR 网络块建模算法的实现（[博客文章](http://badhessian.org/2015/05/concor-in-r/)）。
- [ContentStructure](https://github.com/matthewjdenny/ContentStructure) - 实现[主题分区多网络嵌入 (TPME) 模型](http://dirichlet.net/pdf/krafft12topic-partitioned.pdf) 的扩展。
- [DiagrammeR](https://github.com/rich-iannone/DiagrammeR) - 连接 R、RStudio 和 JavaScript 库来绘制图表（[博客文章](https://blog.rstudio.org/2015/05/01/rstudio-v0-99-preview-graphviz-and-diagrammer/)）。
- [dodgr](https://CRAN.R-project.org/package=dodgr) - 使用优先级队列最短路径计算双加权有向图（例如街道网络）上的距离。
- [edgebundle](https://github.com/schochastics/edgebundle) - 边缘捆绑算法，例如有用绘制交通网络地图。
- [egor](https://CRAN.R-project.org/package=egor) - 用于导入、分析和可视化各种格式的以自我为中心的网络数据的工具。
- [EpiModel](https://CRAN.R-project.org/package=EpiModel) - 用于模拟传染病动力学数学模型的工具（[演示文稿](https://doi.org/10.18637%2Fjss.v084.i08)）。
- [ergm](https://CRAN.R-project.org/package=ergm) - 指数随机图模型 (ERGM) 的估计。
- [ERGM：edgecov 和 dyadcov 规范](http://mjh4.blogspot.com/2012/09/ergm-edgecov-and-dyadcov-specifications.html)。
- [ergMargins](https://CRAN.R-project.org/package=ergMargins) - ERGM 的工艺分析。
- [ergmito](https://CRAN.R-project.org/package=ergmito) - 适用于小型网络的 ERGM。
- [fergm](https://CRAN.R-project.org/package=fergm) - 虚弱 ERGM。
- [GERGM](https://CRAN.R-project.org/package=GERGM) - 广义指数随机图模型（GERGM）收敛性的估计和诊断。
- [geomnet](https://CRAN.R-project.org/package=geomnet) - 使用“ggplot2”进行网络可视化的单几何方法。
- [ggnetwork](https://CRAN.R-project.org/package=ggnetwork) - 使用“ggplot2”绘制网络对象的多几何方法。
- [ggraph](https://CRAN.R-project.org/package=ggraph) - 以“ggplot2”精神构建的图形语法。另请参阅：`tidygraph` R 包。
- [goldfish](https://github.com/snlab-ch/goldfish) - 动态网络参与者导向模型 (DyNAM)，用于随时间对协调网络进行统计分析。
- [graphlayouts](https://CRAN.R-project.org/package=graphlayouts) - 基于[应力主化]概念的布局算法(https://doi.org/10.1007/978-3-540-31843-9_25)。
- [《权力的游戏》中的图形布局简介](http://blog.schochastics.net/post/introducing-graphlayouts-with-got/)。
- [使用 ggraph 和 graphlayouts 在 R 中进行网络可视化](https://mr.schochastics.net/material/netVizR/)。
- [hergm](https://CRAN.R-project.org/package=hergm) - 估计和模拟具有局部依赖性的分层指数族随机图模型 (HERGM)。
- [hierformR](https://CRAN.R-project.org/package=hierformR) - 确定社交网络随着时间的推移发展形成社会等级制度的路径和状态。
- [igraph](http://igraph.org/r/) - 网络分析工具的集合。
- [使用 R 和 igraph 进行网络分析和可视化](http://kateto.net/networks-r-igraph) (2016)。
- [ig.degree.betweenness](https://github.com/benyamindsmith/ig.degree.betweenness/) - [Smith-Pittman](https://arxiv.org/abs/2411.01394) 社区检测算法 (2024) 的 igraph 实现。
- [influenceR](https://CRAN.R-project.org/package=influenceR) - Burt、Borgatti 等人计算各种节点中心性网络度量。
- [keyplayer](https://CRAN.R-project.org/package=keyplayer) - 实施多项网络中心性措施。
- [latentnet](https://CRAN.R-project.org/package=latentnet) - 网络对象的潜在位置和聚类模型。
- [levelnet](https://github.com/schochastics/levelnet) - 用于分析二分（双模）网络的单模投影的实验包。另请参阅：`bipartite` R 包。
- [lpNet](https://www.bioconductor.org/packages/release/bioc/html/lpNet.html) - 线性规划模型旨在推断生物（信号、基因）网络。
- [mlergm](https://cran.r-project.org/package=mlergm) - 多级指数族随机图模型，用于对嵌套在已知块内的节点进行建模。
- [multigraph](https://cran.r-project.org/package=multigraph) - 用于构建和可视化各种多重图的函数。
- [multigraphr](https://cran.r-project.org/package=multigraphr) - 随机多重图模型、多重图属性统计和拟合优度检验。
- [multinet](https://CRAN.R-project.org/package=multinet) - 多层社交网络的工具。
- [相关书籍和数据](http://multilayer.it.uu.se/)和[演示文章](http://multilayer.it.uu.se/papers/jss.pdf)。请参阅“uunet”了解 Python 版本。
- [multinets](https://cran.r-project.org/package=multinets) - 用于处理“igraph”中的多级网络的包。
- [migraph](https://CRAN.R-project.org/web/packages/migraph/) - 一组扩展常见社交网络分析包的工具，用于分析多模式和多级网络。
- [ndtv](https://CRAN.R-project.org/package=ndtv) - 用于构建各种格式的动态网络数据的动画可视化的工具。
- [neo4r](https://github.com/neo4j-rstats/neo4r) - R 的 Neo4J 驱动程序。
- [networkD3](https://christophergandrud.github.io/networkD3/) - 从 R 创建 d3.js 网络图。
- [netdiffuseR](https://CRAN.R-project.org/package=netdiffuseR) - 分析创新网络扩散的工具。
- [netrankr](https://CRAN.R-project.org/package=netrankr) - 最新的网络中心性指数集合，包含大量文档。
    - [Network Centrality in R: An Introduction](http://blog.schochastics.net/post/network-centrality-in-r-introduction/) - 包括对相关 R 包的回顾。
- [R 中的网络中心性：邻里包容](http://blog.schochastics.net/post/network-centrality-in-r-neighborhood-inclusion/)。
- [R 中的网络中心性：测量中心性的新方法](http://blog.schochastics.net/post/network-centrality-in-r-new-ways-of-measuring-centrality/) (2018)。
- [netseg](https://mbojan.github.io/netseg/) - 网络隔离和同质性的各种措施。
- [NetSim](http://www.christoph-stadtfeld.com/netsim/) - 模拟并结合微观模型，研究其对社交网络宏观特征的影响。
- [netUtils](https://github.com/schochastics/netUtils) - 各种网络功能和方法，例如计算两个图的笛卡尔积或拟合离散核心外围模型。
- [network](https://CRAN.R-project.org/package=network) - 在 R 中操作关系数据的基本工具。
- [networkdata](https://github.com/schochastics/networkdata) - 包括 979 个网络数据集，其中包含 2135 个网络。
- [networkdiffusion](https://github.com/chengjun/networkdiffusion) - 模拟和可视化网络中基本的流行病扩散。
- [networkDynamic](https://CRAN.R-project.org/package=networkDynamic) - 支持动态（间）时间网络。
- [networksis](https://CRAN.R-project.org/package=networksis) - 用于模拟二分网络图的工具，其中节点的度数是固定和指定的。
- [PAFit](https://CRAN.R-project.org/package=PAFit) - 时间复杂网络中优先附着和节点适应度的非参数估计。
- [PCIT](https://CRAN.R-project.org/package=PCIT) - 利用信息论实现偏相关，以便识别加权网络（例如基因共表达网络）中有意义的相关性。
- [RCy3](https://bioconductor.org/packages/3.3/bioc/html/RCy3.html) - R 和最新版本的 Cytoscape 之间的接口。
- [RCyjs](https://bioconductor.org/packages/release/bioc/html/RCyjs.html) - R 和 Cytoscape.js 之间的接口。
- [qgraph](https://CRAN.R-project.org/package=qgraph) - 心理测量网络建模和可视化工具；也针对加权图形模型）。
- [使用 qgraph 1.3 选择网络模型](http://psychosystems.org/network-model-selection-using-qgraph-1-3-10/) (2014)。
- [qgraph 示例](http://sachaepskamp.com/qgraph/examples)。
- [qgraph：心理测量数据中关系的网络可视化](https://www.jstatsoft.org/article/view/v048i04) (2012)。
- [relevent](https://CRAN.R-project.org/package=relevent) - 适合关系事件模型 (REM) 的工具。
    - [informR](https://CRAN.R-project.org/package=informR) - 从事件列表创建序列统计信息以在“相关”中使用的工具。
- [rem](https://CRAN.R-project.org/package=rem) - 估计事件序列中的内生网络效应并拟合关系事件模型 (REM)，该模型衡量网络如何随着时间的推移形成和演变。
- [rgexf](https://CRAN.R-project.org/package=rgexf) - 将网络对象从 R 导出到 GEXF，以便使用 Gephi 或 Sigma 等软件进行操作。
- [Rgraphviz](https://bioconductor.org/packages/release/bioc/html/Rgraphviz.html) - 支持在 R 中使用 Graphviz 库及其 DOT 图形绘制语言。
- [RSiena](http://r-forge.r-project.org/R/?group_id=461) - 实证网络分析的模拟研究；将模型拟合到纵向网络数据。
- [signnet](http://signnet.schochastics.net/) 分析符号网络的方法（结构平衡、块建模、中心性等）。
- [sna](https://CRAN.R-project.org/package=sna) - 基本网络构造器、测量和可视化工具。
- [snahelper](https://CRAN.R-project.org/package=snahelper) - RStudio 插件提供 GUI 来可视化和分析网络
    - [snahelper简介（第1部分）](http://blog.schochastics.net/post/an-rstudio-addin-for-network-analysis-and-visualization/)
    - [snahelper简介（第二部分）](http://blog.schochastics.net/post/new-rstudio-addins-for-network-analysis/)
- [SocialMediaLab](https://CRAN.R-project.org/package=SocialMediaLab) - 用于收集社交媒体数据并从中生成网络的工具（[配套网站](http://vosonlab.net/SocialMediaLab)、[github 存储库](https://github.com/voson-labSocialMediaLab)）。
- [spectralGOF](http://people.bu.edu/jccs/spectralGOF.html) - 计算谱拟合优度 (SGOF)，衡量网络模型解释观察到的网络结构的程度。
- [spnet](https://CRAN.R-project.org/package=spnet) - 在“sp”类中在地图上可视化空间网络的方法。
- [spNetwork](https://CRAN.R-project.org/package=spNetwork) - 空间网络分析方法，包括例如核密度估计、距离和点模式分析。
- [statnet](https://statnet.org/) - 许多 R 网络分析包背后的项目（[mailing-list](https://mailman13.u.washington.edu/mailman/listinfo/statnet_help)、[tutorials/workshops](https://statnet.org/workshops/)）。
- [使用 statnet 的指数随机图模型 (ERGM)](https://statnet.org/workshop-ergm/ergm_tutorial.html) (2022)。
- [statnet 包使用指南](http://www.melissaclarkson.com/resources/R_guides/) (2010)。
- [使用 statnet 对价值网络进行建模](https://statnet.org/workshop-valued/valued.html) (2022)。
- [tergm](https://CRAN.R-project.org/package=tergm) - 拟合、模拟和诊断时间指数族随机图模型 (TERGM) 的模型。
- [tidygraph](https://CRAN.R-project.org/package=tidygraph) - 构建图形结构的“整洁”方法。另请参阅：`ggraph` R 包。
    - [介绍 tidygraph](https://www.data-imaginist.com/2017/introducing-tidygraph/)
    - [使用 tidygraph 和 ggraph 整理您的网络分析](https://posit.co/resources/videos/tidying-up-your-network-analysis-with-tidygraph-and-ggraph/)
- [tnam](https://CRAN.R-project.org/package=tnam) - 用于拟合时间和横截面网络自相关模型 (TNAM) 的工具。
- [tnet](https://CRAN.R-project.org/package=tnet) - 加权网络、双模网络和纵向网络的网络测量。
- [tsna](https://CRAN.R-project.org/package=tsna) - 用于时间社交网络分析的工具。
- [visNetwork](https://github.com/DataKnowledge/visNetwork) - 使用 vis.js 库进行网络可视化。
- [xergm](https://CRAN.R-project.org/package=xergm) - 指数随机图模型的扩展（ERGM、GERGM、TERGM、TNAM 和 REM）。

### 斯塔塔

- [nwcommands：使用 Stata 进行网络分析](https://nwcommands.wordpress.com/)（[讨论](http://www.statalist.org/forums/forum/general-stata-discussion/general/1290963-network-analysis-which-command-to-use），[教程和幻灯片](https://nwcommands.wordpress.com/tutorials-and-slides/))。
- [SNA with Stata](http://www.rensecorten.org/index.php/category/sna-with-stata/) - 记录 netplot Stata 包使用的博客。

### 语法

> 供多个程序使用的通用图形语法。

- [DOT](http://www.graphviz.org/doc/info/lang.html) - Graphviz 软件使用的图形绘制语法。
- [GEXF](https://gexf.net) - Gephi 软件使用的文件格式。
- [GraphML](http://graphml.graphdrawing.org/) - 全面且易于使用的图表文件格式（[手册章节](https://www.uni-konstanz.de/mmsp/pubsys/publishedFiles/BrEiLe10.pdf)）。
- [JGraphT](https://jgrapht.org/) - 用于图形数据结构和算法的Java图形库（[示例算法](https://github.com/agouge/Java-Network-Analyzer)）。
- [JUNG - Java Universal Network/Graph Framework](https://jung.sourceforge.net/) - 用于表示网络对象的可扩展库。
- [PGF/TikZ](http://www.ctan.org/tex-archive/graphics/pgf/) - [Tandem](https://en.wikipedia.org/wiki/PGF/TikZ) 的矢量图形语言，可用于在 [LaTeX](https://latex-project.org/) 排版环境中绘制图形。
- [很棒的 LaTeX：TiKZ](https://github.com/egeerardyn/awesome-LaTeX#tikz)。
    - [如何在 LaTeX 中绘制图表？](https://tex.stackexchange.com/questions/57152/how-to-draw-graphs-in-latex)
- [TikZ 图示例](http://www.texample.net/tikz/examples/tag/graphs/)。
- [TikZ 和 PGF 手册](http://distrib-coffee.ipsl.jussieu.fr/pub/mirrors/ctan/graphics/pgf/base/doc/pgfmanual.pdf)。
    - [TKZ](http://altermundus.com/pages/tkz/index.html) - 基于 TikZ 的软件包。
- [TLP - Tulip Software Graph Format](http://tulip.labri.fr/TulipDrupal/?q=tlp-file-format) - Tulip 软件框架使用的图形语法。
- [Cypher](http://neo4j.com/docs/stable/cypher-query-lang.html) - [Neo4j](http://neo4j.com/) 使用的图查询语言。

### 教程

> 不专注于单个特定软件包或程序的教程。

- [R 中的网络中心性教程](https://github.com/schochastics/centrality) (2023)。
- [使用 Gephi 和 R 进行基本和高级网络可视化](http://kateto.net/sunbelt2016) (2016)。
- [使用 igraph 和相关软件包进行 R 中的基本网络分析](https://mr.schochastics.net/material/netAnaR/) (2022)。
- [R 中的交互式和动态网络可视化](http://curleylab.psych.columbia.edu/netviz/) 和 JavaScript 库 (2016)。
- [Nodegoat and Palladio: Introductory Workshop](https://www.academia.edu/11450425/Nodegoat_and_Palladio_Introductory_Workshop_by_Emmanuelle_Chaze) - 针对人文主义者（2015）。
- [Static and Dynamic Network Visualization with R](http://kateto.net/network-visualization) - 涵盖 igraph、network、ggraph、network、networkD3、ndtv、 Threejs 和 visNetwork 包（2019）。
- [使用 tidygraph 包在 R 中进行 Tidy 网络分析](https://mr.schochastics.net/material/tidynetAnaR/) (2022)。

## 瓦里亚

> 不属于其他类别的资源。

- [+100 herramientas para el análisis de redes sociales](http://www.k-government.com/2016/06/28/100-herramientas-analisis-redes-sna-ars/) - 网络分析的各种应用的长列表，以及西班牙语的简短描述。
- [Awesome graph classification](https://github.com/benedekrozemberczki/awesome-graph-classification) - 图嵌入论文的综合列表，包括标题、作者、论文链接和参考实现。
- [Awesome community detection](https://github.com/benedekrozemberczki/awesome-community-detection) - 社区检测论文的综合列表，包括标题、作者、论文链接和参考实现。
- [Centrality Measures as a Signature of Roles in Rousseau’s _Les Confessions_](http://yro.ch/centrality-measures-signature-roles-rousseaus-les-confessions/) - 现实世界的角色网络分析。
- [Cheat Sheet: Social Network Analysis for Humanists](https://cvcedhlab.hypotheses.org/106) - 组装和操作网络数据时要记住的基本概念。
- [Computer Technologies for the Historical Research of Intellectual Networks](https://www.youtube.com/playlist?list=PLz79Il7EOvUJxdQ9r2IefFtr--BNkfOa7) - 由历史学家制作的系列视频，由 Marten Düring 和 Scott Weingart 主演。
- [Convert Between Graph Formats](http://awesome.cs.jhu.edu/graph-services/convert/) - 用于转换多种不同常见图形格式的在线服务。
- [David Knoke on Network Analysis](https://thesocietypages.org/methods/2015/01/30/david-knoke-on-network-analysis/) - 20 分钟的采访，借鉴 Knoke 对恐怖分子网络的研究，讨论了网络分析的用途和好处。
- [统计网络模型术语表](https://web.archive.org/web/20171215013948/https://statnet.org/trac/raw-attachment/wiki/Resources/glossary.pdf)。
- [Linton C. Freeman 的社交网络研究出版物](http://moreno.ss.uci.edu/pubs.html)，从 1955 年至今。
- [Mapping the Republic of Letters](http://republicofletters.stanford.edu/) - 早期现代学术研究项目（[底层软件](http://www.densisdesign.org/research/knot/)）。
- [Mixed-Method Approaches to Social Network Analysis](https://www.youtube.com/playlist?list=PL3zdEY084WkQD79mR00RSt8j5RuyPwMJE) - 密德萨斯大学法学院会议的视频（2014 年）。
- [Modeling Complex Social Networks: Challenges and Opportunities for Statistical Learning and Inference](https://www.youtube.com/watch?v=1xLjYc7EUEU) - Jennifer Neville 在普渡大学的研讨会演讲视频（2011 年）。
- [NetSciEd - Network Science in Education](https://sites.google.com/a/binghamton.edu/netscied/home) - 旨在提高网络素养的国际倡议。
    <!-- -   (@) [Network Fact](https://twitter.com/networkfact) - Twitter account on networks, graph theory, and related topics. -->
- [Network Map of Knowledge and Art](https://paolonegrini.wordpress.com/2012/11/19/network-map-of-knowledge-and-art/) - 使用 SPARQL 和 Gephi，DBPedia 派生的谁受谁影响的网络定向关系。
    <!-- -   (@) [Network Science](https://twitter.com/Ognyanova/lists/network-science/members) - A thematic list of Twitter accounts, curated by [Katherine Ognyanova](https://twitter.com/Ognyanova). -->
- [The Networks Network](https://groups.google.com/forum/?hl=en-GB#!forum/the-networks-network) - 邮件列表（主要是来自 HNR 网络的历史学家）。
- [New Perspectives for Relational Learning](http://www.birs.ca/events/2015/5-day-workshops/15w5080/videos) - 班夫国际研究站 (BIRS) (2015) 研讨会的视频（及更多内容）。
- [Open Graph protocol](http://ogp.me/) - 提议的标准将任何网页变成“社交图对象”。
- [Periodic Table of Network Centrality](http://schochastics.net/sna/periodic.html) - 中心性指数的交互式周期表。
- [Picking Sides](https://codeandculture.wordpress.com/2015/04/03/picking-sides/) - 各种国家和非国家权力之间的中东联盟政治网络中的社区检测（[更新版本](https://gist.github.com/briatte/c6df2f855afb4eb142e6)）。
<!-- -   [Plan interactif du métro](http://www.jeromecukier.net/projects/metro/map.html) - Interactive visualization of the Paris metro network, drawn with d3.js, in French. -->
- [Psych Networks](http://psych-networks.com/) - 包含有关心理数据网络建模的新闻、参考资料和[教程](https://psych-networks.com/tutorials/) 的网站。
- [估计心理网络新方法的教程论文](http://psych-networks.com/tutorial-paper-new-methods-estimating-psychological-networks/)。
- [(Psychological) Network Analysis Workshops](https://osf.io/6axte/) - 为期 3 天的使用 R 进行心理网络分析的研讨会（2019 年）。
- [我应该进行社交网络分析吗？](https://cvcedhlab.hypotheses.org/125)。
- [The Small World of Psychopathology](http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0027407) - 关于精神症状如何相互关联的论文（[代码、数据和图表](https://sites.google.com/site/dsmgraphs/Home/files)）。
- [Social Network Analysis in DBpedia](http://othes.univie.ac.at/12285/1/2010-10-14_0703857.pdf) - 高度教学性的硕士论文，展示了如何使用 SPARQL 和 Pajek。
- [SNA-DE 邮件列表](https://dlist.server.uni-frankfurt.de/mailman/listinfo/sna-de)，德语。
- [SPARQL for R Tutorial - Hollywood Social Network Analysis](http://semanticweb.cs.vu.nl/R/sparql_hollywood/sparql_hollywood.html) - 还使用 Gephi。
- [社会学引文网络](http://nealcaren.web.unc.edu/a-sociology-itation-network/) 和 [哲学同引网络](https://kieranhealy.org/blog/archives/2013/06/18/a-co-itation-network-for-philosophy/) - 科学同引网络的示例。
- [使用元数据寻找 Paul Revere](https://kieranhealy.org/blog/archives/2013/06/09/using-metadata-to-find-paul-revere/) 和 [Paul Revere 的另一场旅程：美国制造中的经纪人角色Revolution](http://www.sscnet.ucla.edu/polisci/faculty/chwe/ps269/han.pdf) - 应用于美国革命者的网络分析。
- [Visual Complexity. An Exploration on Mapping Complex Networks](http://www.visualcomplexity.com/vc/) - 大量精美的网络和树可视化（[book](http://www.visualcomplexity.com/vc/book/)，也有中文和法文版本）。
- [Visualizing Historical Networks](https://histecon.fas.harvard.edu/visualizing/index.html) - 哈佛大学的历史网络研究项目。
- [1764 年的安古莱姆](https://histecon.fas.harvard.edu/visualizing/angouleme/index.html)。
- [剑桥经济学家](https://histecon.fas.harvard.edu/visualizing/graphing/economists.html)。
- [帝国的内心生活：十八世纪历史](https://histecon.fas.harvard.edu/visualizing/graphing/innerlife.html)。

### 博客系列

> 关于网络主题的一系列博客文章。

- [Archaeological Networks](http://archaeologicalnetworks.wordpress.com/) - 汤姆布鲁曼斯的博客，针对考古学家和历史学家。
- [Aaron Clauset 关于网络的博客文章](https://www.cs.unm.edu/~aaron/blog/archives/networks/index.htm)。
- [Baptiste Coulmont 关于网络的博客文章](http://coulmont.com/index.php?s=r%C3%A9seaux)，法语。
- [Cosma R. Shalizi 关于网络的博客文章](http://bactra.org/weblog/cat_networks.html)。
- [François Briatte 关于网络的博客文章](https://politbistro.hypotheses.org/tag/reseaux)，法语。
- [Katya Ognyanova 关于网络的博客文章](http://kateto.net/networks)。
- [Pierre Mercklé 关于网络的博客文章](http://pierremerckle.fr/category/reseaux/)，法语。
- [Bad Hessian 博客上有关网络的博客文章](http://badhessian.org/category/networks/)，由各个贡献者撰写。
- [R-Bloggers](http://www.r-bloggers.com/)（R 博客聚合器）上有关网络的博客文章：
- [网络](http://www.r-bloggers.com/?s=networks)。
- [社交网络分析](http://www.r-bloggers.com/?s=social+network+analysis)。
- [Cosma R. Shalizi 的笔记本](http://bactra.org/notebooks) 关于网络相关主题，绝对值得（选择性）详细列出：
- [网络数据分析](http://bactra.org/notebooks/network-data-analysis.html)。
- [选型社交网络和中性文化进化](http://bactra.org/notebooks/neutral-culture-networks.html)。
- [生化网络进化](http://bactra.org/notebooks/biochem-network-evol.html)。
- [引文和引文网络](http://bactra.org/notebooks/itations.html)。
- [复杂网络的社区发现方法](http://bactra.org/notebooks/community-discovery.html)。
- [复杂网络](http://bactra.org/notebooks/complex-networks.html)。
- [社交网络实验](http://bactra.org/notebooks/network-experiments.html)。
- [指数随机图模型 (ERGM)](http://bactra.org/notebooks/ergms.html)。
- [图采样算法](http://bactra.org/notebooks/graph-sampling.html)。
- [图论](http://bactra.org/notebooks/graph-theory.html)。
- [社交网络中的同质性和影响力](http://bactra.org/notebooks/homophily-vs-influence.html)。
- [从非网络数据推断网络](http://bactra.org/notebooks/inferring-networks.html)。
- [文本和网络的联合建模](http://bactra.org/notebooks/text-networks.html)。
- [网络比较](http://bactra.org/notebooks/network-comparisons.html)。
- [政治演员网络](http://bactra.org/notebooks/networks-of-political-actors.html)。
- [关系学习](http://bactra.org/notebooks/relational-learning.html)。
      - [社会传染、信息级联、创新扩散等。](http://bactra.org/notebooks/social-contagion.html)
- [社交网络](http://bactra.org/notebooks/social-networks.html)。
- [随机块模型](http://bactra.org/notebooks/stochastic-block-models.html)。
- 另请参阅：[随机块模型注释参考书目](https://www.alexpghayes.com/blog/an-annotated-bibliography-on-stochastic-block-models/) (2019)。
- Daniel Little 关于社会科学哲学的博客文章：
- [网络](https://understandsociety.blogspot.com/search/label/networks)。
- [社交网络](https://understandsociety.blogspot.com/search/label/social%20networks)。
- Martin Grandjean 的博客文章（主要是）关于网络可视化的英语和法语：
- [网络分析](https://www.martingrandjean.ch/tag/analysis-de-reseau/)。
- [社交网络](https://www.martingrandjean.ch/tag/reseaux-sociaux/)。
- [Networks Demystified](http://www.scottbot.net/HIAL/index.html@tag=networks-demystified.html)，Scott B. Weingart 的一系列博客文章。
- [Netze und Netzwerke](https://netzeundnetzwerke.de/)，英语和德语 - Sebastian Gießmann 撰写的有关网络分析历史的博客（[旧博客](http://www.netzeundnetzwerke.de/old/)）。
- [R / Notes: Networks](https://f.briatte.org/r/category/networks) - François Briatte 撰写的博客文章专注于在 R 中操作网络。
- [TNT: The Network Thinkers](http://www.thenetworkthinkers.com/) - 瓦尔迪斯·克雷布斯的博客。
- [Under Roquentin’s Chestnut Tree](https://mboudour.github.io/) - Moses Boudourides 的关于使用 Python 分析（主要是）网络的博客。
- Yannick Rochat 关于数字人文的博客文章（英语和法语）：
- [角色网络](https://yro.ch/tag/character-network/)。
- [网络分析](https://yro.ch/tag/network-analysis/)。

### 虚构网络

> 虚构人物网络的探索。

- [Analyzing Networks of Characters in _Love Actually_](http://varianceexplained.org/r/love-actually-network/) - 具有聚类分析和 [Shiny 应用程序](https://dgrtwo.shinyapps.io/love-actually-network/)（使用 R + Shiny）。
- [维克多·雨果的《悲惨世界》中的人物共现](https://docs.bokeh.org/en/latest/docs/examples/topics/categorical/les_mis.html)，绘制为邻接矩阵，用 Python (+ Javascript) 编写。
<!-- -   [Events in the _Game of Thrones_](http://www.jeromecukier.net/projects/agot/events.html) and [Places in the _Game of Thrones_](http://www.jeromecukier.net/projects/agot/places.html) - Networked chronologies of character alliances, kills and travels in the book series, drawn with d3.js. -->
- [来自_Grey’s Anatomy_ hook-ups的指数随机图建模课程](http://badhessian.org/2012/09/lessons-on-exponential-random-graph-modeling-from-greys-anatomy-hook-ups/)（使用R）。
- [莎士比亚的_Macbeth_的网络分析](https://mboudour.github.io/2015/10/28/Shakespeare's-Macbeth-Network.html)（使用Python）。
- [阿瑟·柯南·道尔《猩红研究》中人物句子共现的网络和转变轨迹](https://mboudour.github.io/2016/04/17/Arthur-Conan-Doyle's-A-Study-in-Scarlet-Network-&-Trajectories.html)（使用Python； [代码](https://github.com/mboudour/WordNets/blob/master/ArthurConanDoyle_AStudyInScarlet_Network%26Trajectories.ipynb))。
- [网络可视化：描绘莎士比亚的悲剧](https://www.martingrandjean.ch/network-visualization-shakespeare/)。
- [_爱丽丝梦游仙境_的社交网络分析](https://aclanthology.org/W12-2513/)。
- [_Star Wars_ Social Networks: The Force Awakens](http://evelinag.com/blog/2016/01-25-social-network-force-awakens/index.html) - 还有一个用 F# 编写的社交网络分析的示例。
- [神话网络的普遍属性](https://doi.org/10.1209/0295-5075/99/28002) ([预印本](https://arxiv.org/abs/1205.4324))。

### 网络科学

> 讨论“netsci”是什么以及对其他科学学科的意义。

- [Editing a Normal Science Journal in Social Science](https://journals.openedition.org/bms/595) - 《社交网络》杂志创始编辑对其的反思。
- [The Emergence of Network Science](https://www.cornell.edu/video/emergence-of-network-science) - 视频纪录片，由史蒂文·H·斯特罗加茨 (Steven H. Strogatz) 等许多人主演。
- 来自 [Albert-László Barabási 的评论文章](https://barabasi.com/publications/1/review-articles)：
- [驯服复杂性](https://barabasi.com/f/182.pdf)。
- [网络接管](https://barabasi.com/f/362.pdf)。
- [The Invasion of the Physicists](https://doi.org/10.1016/j.socnet.2004.06.002) - “网络_科学_”是如何产生的。
- [孤立的社交网络者](https://crookedtimber.org/2005/05/19/isolated-social-networkers/)、[网络和网络战争](http://bactra.org/weblog/347.html) 和 [跨学科研究的跨学科政治或，“嘿，那是我的想法”首先。”](https://www.cs.unm.edu/~aaron/blog/archives/2005/05/the_interdiscip.htm) - 一系列博客文章，早于“网络科学”这个流行词的出现，但涉及的问题与现在在该标题下讨论的问题相同。
- [The ‘New’ Science of Networks](https://www.jstor.org/stable/29737693) - 2002-2003年出版的网络科学图书综述。
- [Predicting Highly Cited Papers](https://arxiv.org/abs/1310.8220) - 网络科学领域下一篇高被引用论文的预测。
- [1996-2013 年跨学科社交网络和网络科学共引](https://github.com/raffaelevacca/EUSN-co-itation-networks)。
- [关于网络科学的三个难题](http://environmentalpolicy.ucdavis.edu/node/292)。
- [A Twenty-First Century Science](http://www.nature.com/nature/journal/v445/n7127/full/445489a.html) - 邓肯·J·瓦茨的文章。
- [What is Network Science?](http://journals.cambridge.org/repo_A88Sa8AHdt4SoI) - 最近的《网络科学》杂志的第一篇社论。

### 小世界

> 关注（类似）[斯坦利·米尔格拉姆的小世界实验](https://en.wikipedia.org/wiki/Small-world_experiment) 的链接。

- [The Erdös Number Project](http://wwwp.oakland.edu/enp/) - 关于数学家之间的协作关系和网络距离的研究项目。
- [How Small is the World, Really?](https://medium.com/@duncanjwatts/how-small-is-the-world-really-736fa21808ba#.kyr90lhyo) - 关于“_x_ 分离度”小世界实验的讨论。
- [The Oracle of Bacon](https://oracleofbacon.org/) - 基于[在线游戏](https://en.wikipedia.org/wiki/Six_Degrees_of_Kevin_Bacon)，该游戏产生了[慈善](http://www.six Degrees.org/)。
- [Panel: Six Degrees of Separation](https://www.cornell.edu/video/six-degrees-of-separation-panel) - 康奈尔大学一次会议的视频，由 Duncan J. Watts、Steven H. Strogatz、Jon Kleinberg 和其他演讲者参加。
- [Patterns in the Ivy: The Small World of Metal](http://badhessian.org/2013/09/patterns-in-the-ivy-the-small-world-of-metal/) - 基于金属艺术家和乐队的两种模式网络分析示例。
- [Six Degrees of Francis Bacon](http://sixdegreesoffrancisbacon.com/) - 详细记录的早期现代历史网络的交互式可视化。
- [Six Degrees of Separation](https://en.wikipedia.org/wiki/Six_degrees_of_separation) - 维基百科英文条目。

### 双模网络

> 也称为二分图。

- [L’analysis des graphes bipartis](https://shs.hal.science/halshs-00794976)，法语 (2013)。
- [大型双模网络分析的基本概念](https://doi.org/10.1016/j.socnet.2007.04.006) ([预印本](https://www-complexnetworks.lip6.fr/~latapy/Publis/socnet07.pdf), [相关代码]（https://www-complexnetworks.lip6.fr/~latapy/Bip/）；_社交网络_，2008）。
- [拟合大型签名两模式块模型：问题与前景](http://patrickdoreian.com/wp-content/uploads/2017/12/large-signed-2mode-networks_UNGA.pdf)。
- [双模式网络数据的广义块建模](https://doi.org/10.1016/j.socnet.2004.01.002) ([预印本](http://vlado.fmf.uni-lj.si/pub/networks/doc/preprint/TwoMode.pdf))。
- [通用双模式核心](https://doi.org/10.1016/j.socnet.2015.04.001)。
- [对签名两种模式网络进行分区](http://patrickdoreian.com/wp-content/uploads/2017/12/partitioning-signed-social-networks.pdf)。
- [在 R 中使用二分/附属网络数据](https://solomonmessing.wordpress.com/2012/09/30/working-with-bipartiteaffiliation-network-data-in-r/) (2012)。

* * *

## 许可证

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png)](http://creativecommons.org/publicdomain/zero/1.0/)

在法律允许的范围内，此列表的作者按时间顺序排列：[François Briatte](https://f.briatte.org/)，
[伊恩·麦卡洛](https://www.linkedin.com/in/mcculloh),
[阿迪亚·卡纳](https://vivo.brown.edu/display/akhann16),
[曼利奥·德·多梅尼科](https://manliodedomenico.com/),
帕特里克·卡明斯基,
[Ericka Menchen-Trevino](https://erickaakcire.github.io/),
[Tam-Kien Duong](https://github.com/taniki),
[杰里米·福特](https://github.com/jdfoote),
[凯瑟琳·克莱默](http://nysci.org/nysci_people/catherine-cramer/),
[Andrej Mrvar](http://mrvar.fdv.uni-lj.si/),
[帕特里克·多雷安](http://patrickdoreian.com/),
[弗拉基米尔·巴塔杰](http://vladowiki.fmf.uni-lj.si/doku.php?id=vlado),
埃里克·C·琼斯，
奥尔登·S·克洛夫达尔，
[詹姆斯·费尔班克斯](http://www.jpfairbanks.net/),
[丹妮尔·瓦尔达](http://www.ucdenver.edu/academics/colleges/SPA/FacultyStaff/Faculty/Pages/DanielleVarda.aspx),
[安德鲁·皮茨](https://twitter.com/andpitts),
[罗曼·巴图西亚克](https://github.com/riomus),
[库斯图夫·辛哈](https://koustuvsinha.com/),
[Mohsen Mosleh](http://mohsenmosleh.com/),
[桑德罗·索萨](https://github.com/sandrofsousa),
[让-巴蒂斯特·普雷萨克](https://github.com/JBPressac),
[帕特里克·康诺利](https://github.com/patcon),
[赫里斯托·格奥尔基耶夫](https://hristog.github.io/),
[蒂亚戈·阿泽维多](http://github.com/tjiagoM),
[路易斯·米格尔·蒙蒂利亚](https://twitter.com/luismmontilla),
[基思·特纳](https://github.com/keith-turner),
[桑德拉·贝克尔](https://github.com/sandravizmad),
[Benedek Rozemberczki](https://github.com/benedekrozemberczki),
[星汉路](https://xinghanlu.com/),
[文森特·拉巴图](https://cv.hal.science/vlabatut),
[大卫·肖赫](https://www.mr.schochastics.net/),
[郑在元](https://github.com/j1c),
[Benedek Rozemberczki](https://github.com/benedekrozemberczki),
[亚历克斯·洛夫特斯](https://github.com/loftusa),
[阿伦](https://github.com/arunppsg),
[菲利波·门泽](https://cnets.indiana.edu/fil/),
[马克·席勒](https://github.com/m4rcs),
[Tanguy Fardet](https://tfardet.srht.site/),
[伯恩哈德·比埃里](https://bernhardbieri.ch/),
[Rémy Cazabet](https://github.com/Yquetzal),
[杰里米·盖尔布](https://github.com/JeremyGelb),
[马蒂厄·巴斯蒂安](https://github.com/mbastian),
[迈克尔·塞尔](https://github.com/mszell),
[Eran Rivlis](https://github.com/erivlis),
[Rohan Dandage](https://github.com/rraadd88),
[本杰明·史密斯](https://github.com/benyamindsmith),
[贝丝·鸭子](https://github.com/bduckles),
[曹磊](https://github.com/cllei12),
[西蒙·德拉鲁](https://www.simondelarue.com/) 和
[克里斯蒂安·舒尔茨](https://schulzchristian.github.io/) -
已放弃本作品的所有版权以及相关或邻接权。

感谢 [Robert J. Ackland](https://github.com/rjackland)，
[洛朗·博吉特](https://cv.hal.science/laurent-beauguitte),
[帕特里克·康诺利](http://nodescription.net/),
[迈克尔·多尔曼](https://geobgu.xyz/),
[科林·费伊](https://colinfay.me/),
[马克·弗兰德罗](https://www.history.upenn.edu/people/faculty/marc-flandreau),
[Eiko Fried](https://eiko-fried.com/),
[克里斯托弗·史蒂文·马库姆](https://cmarcum.github.io/),
[Wouter de Nooy](https://www.uva.nl/profiel/n/o/w.denooy/w.denooy.html),
[卡蒂亚·奥格尼亚诺娃](https://kateto.net/),
[拉胡尔·帕迪](https://github.com/rahul-38-26-0111-0003),
[卡米尔·罗斯](https://camilleroth.github.io/),
[克劳德·S·费舍尔](https://sociology.berkeley.edu/faculty/claude-s-fischer),
[科斯玛·莎莉兹](https://www.stat.cmu.edu/~cshalizi/),
[汤姆 A.B.斯奈德斯](https://www.stats.ox.ac.uk/~snijders/),
[Chris Watson](https://profiles.bu.edu/Christopher.Watson) 和 [Tim A. Wheeler](https://github.com/tawheeler)，他们帮助找到了此列表中的一些很棒的资源。
