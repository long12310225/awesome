# 很棒的应用安全 [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

用于了解应用程序安全性的精选资源列表。包含书籍、
网站、博客文章和自我评估测验。

由 [Paragon Initiative Enterprises](https://paragonie.com) 维护
来自应用程序安全和开发人员社区的贡献。我们也
有[其他社区项目](https://paragonie.com/projects)，这可能是
对于未来的应用程序安全专家很有用。

如果您是软件安全主题的绝对初学者，您可能会受益
来自阅读[应用程序安全性简介](https://paragonie.com/blog/2015/08/gentle-introduction-application-security)。

# 贡献

[详情请参阅贡献指南](CONTRIBUTING.md)。

# 应用程序安全学习资源


  * [General](#general)
    * [Articles](#articles)
* [如何安全地生成随机数](#how-to-safely-generate-a-random-number-2014) (2014)
* [加盐密码哈希 - 正确执行](#salted-password-hashing-doing-it-right-2014) (2014)
* [一个好主意但不好的用法：/dev/urandom](#a-good-idea-with-bad-usage-devurandom-2014) (2014)
* [为什么投资应用程序安全？](#why-invest-in-application-security-2015) (2015)
* [警惕一次性垫和其他加密独角兽](#be-wary-of-one-time-pads-and-other-crypto-unicorns-2015) (2015)
    * [Books](#books)
* [Web 应用程序黑客手册](#-web-application-hackers-handbook-2011) (2011) ![nonfree](img/nonfree.png)
* [密码学工程](#-cryptography-engineering-2010) (2010) ![nonfree](img/nonfree.png)
* [保障 DevOps 安全](#-secure-devops-2018) (2018) ![nonfree](img/nonfree.png)
* [灰帽 Python：黑客和逆向工程师编程](#-gray-hat-python-programming-for-hackers-and-reverse-engineers-2009) (2009) ![nonfree](img/nonfree.png)
* [软件安全评估的艺术：识别和预防软件漏洞](#-the-art-of-software-security-assessment-identifying-and-preventing-software-vulnerability-2006) (2006) ![nonfree](img/nonfree.png)
* [C 接口和实现：创建可重用软件的技术](#-c-interfaces-and-implementations-techniques-for-creating-reusable-software-1996) (1996) ![nonfree](img/nonfree.png)
* [逆向：逆向工程的秘密](#-reversing-secrets-of-reverse-engineering-2005) (2005) ![nonfree](img/nonfree.png)
* [JavaScript：好的部分](#-javascript-the-good-parts-2008) (2008) ![nonfree](img/nonfree.png)
* [Windows 内部结构：包括 Windows Server 2008 和 Windows Vista 第五版](#-windows-internals-include-windows-server-2008-and-windows-vista-fifth-edition-2007) (2007) ![nonfree](img/nonfree.png)
* [Mac 黑客手册](#-the-mac-hackers-handbook-2009) (2009) ![nonfree](img/nonfree.png)
* [IDA Pro 书籍：世界上最受欢迎的反汇编程序的非官方指南](#-the-ida-pro-book-the-unofficial-guide-to-the-worlds-most-popular-disassembler-2008) (2008) ![nonfree](img/nonfree.png)
* [TCP/IP 互联网络卷。 II：ANSI C 版本：设计、实现和内部结构（第 3 版）](#-internetworking-with-tcpip-vol-ii-ansi-c-version-design-implementation-and-internals-3rd-edition-1998) (1998) ![nonfree](img/nonfree.png)
* [网络算法，：设计快速网络设备的跨学科方法](#-network-algorithmics-an-interciplined-approach-to-designing-fast-networked-devices-2004) (2004) ![nonfree](img/nonfree.png)
* [计算结构（麻省理工学院电气工程和计算机科学）](#-computation-structs-mit-electrical-engineering-and-computer-science-1989) (1989) ![nonfree](img/nonfree.png)
* [神秘软件：用于软件保护的混淆、水印和防篡改](#-surreptitious-software-obfuscation-watermarking-and-tamperproofing-for-software-protection-2009) (2009) ![nonfree](img/nonfree.png)
* [安全编程指南](#secure-programming-howto-2015) (2015)
* [安全工程 - 第三版](#security-engineering-third-edition-2020) (2020)
* [Bulletproof SSL 和 TLS](#-bulletproof-ssl-and-tls-2014) (2014) ![nonfree](img/nonfree.png)
* [Web 开发人员的整体信息安全 (Fascicle 0)](#holistic-info-sec-for-web-developers-fascicle-0-2016) (2016)
      * [Web 开发人员的整体信息安全（分册 1）](#holistic-info-sec-for-web-developers-fascicle-1)
    * [Classes](#classes)
      * [进攻性计算机安全 (CIS 4930) FSU](#offensive-computer-security-cis-4930-fsu)
      * [黑客之夜](#hack-night)
    * [Websites](#websites)
      * [破解这个网站！](#hack-this-site)
      * [恩尼格玛集团](#enigma-group)
      * [Web 应用程序安全测验](#web-app-sec-quiz)
      * [SecurePasswords.info](#securepasswords-info)
      * [安全新闻提要备忘单](#security-news-feeds-cheat-sheet)
      * [开放安全培训](#open-security-training)
      * [MicroCorruption](#microcorruption)
      * [Matasano 加密挑战](#the-matasano-crypto-challenges)
      * [PentesterLab](#pentesterlab)
      * [果汁店](#juice-shop)
      * [超级跑车对决](#supercar-showdown)
      * [OWASP 节点山羊](#owasp-nodegoat)
      * [保护堆栈的安全](#securing-the-stack)
      * [OWASP 无服务器山羊](#owasp-serverlessgoat)
      * [SecDim](#secdim)
      * [Blogs](#blogs)
        * [加密失败](#crypto-fails)
        * [NCC 集团 - 博客](#ncc-group-blog)
        * [斯科特·赫尔姆](#scott-helme)
* [哥萨克实验室博客](#cossack-labs-blog-2018) (2018)
      * [维基页面](#wiki-pages)
        * [OWASP 十佳项目](#owasp-top-ten-project)
      * [Tools](#tools)
        * [Qualys SSL 实验室](#qualys-ssl-labs)
        * [securityheaders.io](#securityheaders-io)
        * [report-uri.io](#report-uri-io)
        * [clickjacker.io](#clickjacker-io)
  * [AWS Lambda](#aws-lambda)
    * [Tools](#tools-1)
      * [PureSec 功能盾](#puresec-functionshield)
  * [Android](#android)
    * [书籍和电子书](#books-and-ebooks)
* [SEI CERT Android 安全编码标准](#sei-cert-android-secure-coding-standard-2015) (2015)
  * [C](#c)
    * [书籍和电子书](#books-and-ebooks-1)
* [SEI CERT C 编码标准](#sei-cert-c-coding-standard-2006) (2006)
* [防御性编码：Fedora 安全团队提高软件安全性指南](#defective-coding-a-guide-to-improving-software-security-by-the-fedora-security-team-2025) (2025)
  * [C++](#c-1)
    * [书籍和电子书](#books-and-ebooks-2)
* [SEI CERT C++ 编码标准](#sei-cert-c-coding-standard-2006-1) (2006)
  * [C夏普](#c-sharp)
    * [书籍和电子书](#books-and-ebooks-3)
* [安全驱动.NET](#-security-driven-net-2015) (2015) ![nonfree](img/nonfree.png)
  * [Clojure](#clojure)
    * [Repositories](#repositories)
* [Clojure OWASP](#clojure-owasp-2020) (2020)
  * [Go](#go)
    * [Articles](#articles-1)
* [Go 中的内存安全 - spacetime.dev](#memory-security-in-go-spacetime-dev-2017) (2017)
  * [Java](#java)
    * [书籍和电子书](#books-and-ebooks-4)
* [SEI CERT Java 编码标准](#sei-cert-java-coding-standard-2007) (2007)
* [Java SE 安全编码指南](#secure-coding-guidelines-for-java-se-2014) (2014)
  * [Node.js](#node-js)
    * [Articles](#articles-2)
* [Node.js 安全检查表 - Rising Stack 博客](#node-js-security-checklist-rising-stack-blog-2015) (2015)
* [很棒的 Electron.js 黑客和渗透测试资源](#awesome-electron-js-hacking-pentesting-resources-2020) (2020)
    * [书籍和电子书](#books-and-ebooks-5)
* [Node.js 基本安全](#-essential-node-js-security-2017) (2017) ![nonfree](img/nonfree.png)
    * [Training](#training)
* [^Lift Security 的安全培训](#-security-training-by-lift-security) ![nonfree](img/nonfree.png)
* [BinaryMist 的安全培训](#-security-training-from-binarymist) ![nonfree](img/nonfree.png)
  * [PHP](#php)
    * [Articles](#articles-3)
* [一切都与时间有关](#its-all-about-time-2014) (2014)
* [具有长期持久性的 PHP 安全身份验证](#secure-authentication-in-php-with-long-term-persistence-2015) (2015)
* [防止 PHP 中跨站脚本的 20 个要点列表](#20-point-list-for-preventing-cross-site-scripting-in-php-2013) (2013)
* [系统管理员的 25 个 PHP 安全最佳实践](#25-php-security-best-practices-for-sys-admins-2011) (2011)
* [PHP 数据加密入门](#php-data-encryption-primer-2014) (2014)
* [防止 PHP 应用程序中的 SQL 注入 - 简单而权威的指南](#preventing-sql-injection-in-php-applications-the-easy-and-definitive-guide-2014) (2014)
* [你不会对密码进行 Base64 - 密码学解码](#you-wouldnt-base64-a-password-cryptography-decoded-2015) (2015)
* [PHP 应用程序中的安全数据加密指南](#a-guide-to-secure-data-encryption-in-php-applications-2015) (2015)
* [2018 年构建安全 PHP 软件指南](#the-2018-guide-to-building-secure-php-software-2017) (2017)
    * [书籍和电子书](#books-and-ebooks-6)
* [保护 PHP 安全：核心概念](#-secure-php-core-concepts) ![nonfree](img/nonfree.png)
      * [在 PHP 项目中使用 Libsodium](#using-libsodium-in-php-projects)
    * [有用的库](#useful-libraries)
      * [defuse/php-encryption](#defusephp-encryption)
      * [ircmaxell/password_compat](#ircmaxellpassword-compat)
      * [ircmaxell/RandomLib](#ircmaxellrandomlib)
      * [thephpleague/oauth2-server](#thephpleagueoauth2-server)
      * [paragonie/random_compat](#paragonierandom-compat)
      * [psecio/gatekeeper](#pseciogatekeeper)
      * [openwall/phpass](#openwallphpass)
    * [Websites](#websites-1)
      * [websec.io](#websec-io)
      * [Blogs](#blogs-1)
        * [模范倡议企业博客](#paragon-initiative-enterprises-blog)
        * [ircmaxell 的博客](#ircmaxells-blog)
        * [帕德拉克·布雷迪的博客](#p%C3%A1draic-bradys-blog)
      * [邮件列表](#mailing-lists)
        * [确保 PHP 每周安全](#securing-php-weekly)
  * [Perl](#perl)
    * [书籍和电子书](#books-and-ebooks-7)
* [SEI CERT Perl 编码标准](#sei-cert-perl-coding-standard-2011) (2011)
  * [Python](#python)
    * [书籍和电子书](#books-and-ebooks-8)
      * [Fedora 防御性编码指南的 Python 章节](#python-chapter-of-fedora-defensive-coding-guide)
* [黑帽 Python：针对黑客和渗透测试人员的 Python 编程](#-black-hat-python-python-programming-for-hackers-and-pentesters) ![nonfree](img/nonfree.png)
* [暴力Python](#-violent-python) ![nonfree](img/nonfree.png)
    * [Websites](#websites-2)
* [OWASP Python 安全维基](#owasp-python-security-wiki-2014) (2014)
  * [Ruby](#ruby)
    * [书籍和电子书](#books-and-ebooks-9)
* [安全 Ruby 开发指南](#secure-ruby-development-guide-2014) (2014)


# 一般

## 文章

### 如何安全地生成随机数 (2014)

**发布**：2014 年 2 月 25 日

关于加密安全伪随机数生成器的建议。

### 加盐密码哈希 - 正确执行 (2014)

**发布**：2014 年 8 月 6 日

[Defuse Security](https://defuse.ca) 的一个项目 [Crackstation](https://crackstation.net) 上的帖子

### 一个好主意但不好的用法：/dev/urandom (2014)

**发布**：2014 年 5 月 3 日

提到了许多使 `/dev/urandom` 在 Linux/BSD 上失败的方法。

### 为什么要投资应用程序安全？ (2015)

**发布**：2015 年 6 月 21 日

经营企业需要具有成本意识并尽量减少不必要的支出。大多数公司都看不到确保应用程序安全的好处，因此他们常常忽略投资安全软件开发作为节省成本的措施。这些公司没有意识到的是，可预防的数据泄露可能会产生潜在成本（包括财务成本和品牌声誉成本）。

**平均数据泄露造成数百万美元的损失。**

对于大多数公司来说，投入更多的时间和人员来开发安全软件是值得的，可以最大限度地减少这种不必要的风险。

### 警惕一次性垫和其他加密独角兽 (2015)

**发布**：2015 年 3 月 25 日

对于任何想要构建自己的密码学功能的人来说，**必读**。

## 书籍

### !nonfree Web 应用程序黑客手册 (2011)

**发布**：2011 年 9 月 27 日

对 Web 应用程序安全性的精彩介绍；虽然有点过时了。

### !nonfree 密码学工程 (2010)

**发布**：2010 年 3 月 15 日

在展示加密设计技术的同时培养专业偏执感。

### !nonfree 确保 DevOps 安全 (2018)

**发布**：2018 年 3 月 1 日

确保 DevOps 安全探讨了如何共同应用 DevOps 和安全技术以使云服务更安全。这本介绍性书籍回顾了用于保护 Web 应用程序及其基础设施的最先进实践，并教您将安全性直接集成到您的产品中的技术。

### !nonfree 灰帽 Python：黑客和逆向工程师编程 (2009)

**发布**：2009 年 5 月 3 日



### !nonfree 软件安全评估的艺术：识别和预防软件漏洞 (2006)

**发布**：2006 年 11 月 30 日



### !nonfree C 接口和实现：创建可重用软件的技术 (1996)

**发布**：1996 年 8 月 30 日



### !nonfree 逆向：逆向工程的秘密 (2005)

**发布**：2005 年 4 月 15 日



### !nonfree JavaScript：好的部分 (2008)

**发布**：2008 年 5 月 1 日



### !nonfree Windows 内部结构：包括 Windows Server 2008 和 Windows Vista 第五版 (2007)

**发布**：2007 年 6 月 17 日



### !nonfree Mac 黑客手册 (2009)

**发布**：2009 年 3 月 3 日



### !nonfree IDA Pro 书籍：世界上最受欢迎的反汇编程序的非官方指南 (2008)

**发布**：2008 年 8 月 22 日



### !nonfree Internetworking with TCP/IP Vol. 1 II：ANSI C 版本：设计、实现和内部原理（第 3 版）（1998 年）

**发布**：1998 年 6 月 25 日



### !nonfree 网络算法，：设计快速网络设备的跨学科方法 (2004)

**发布**：2004 年 12 月 29 日



### !nonfree 计算结构（麻省理工学院电气工程和计算机科学）(1989)

**发布**：1989 年 12 月 13 日



### !nonfree 秘密软件：软件保护的混淆、水印和防篡改 (2009)

**发布**：2009 年 8 月 3 日



### 安全编程指南 (2015)

**发布**：2015 年 3 月 1 日



### 安全工程 - 第三版 (2020)

**发布**：2020 年 11 月 1 日



### !nonfree Bulletproof SSL 和 TLS (2014)

**发布**：2014 年 8 月 1 日



### Web 开发人员的整体信息安全（分册 0）（2016 年）

**发布**：2016 年 9 月 17 日

三部分丛书的第一部分，广泛而深入地介绍了 Web 开发人员和架构师需要了解的内容，以便创建强大、可靠、可维护和安全的软件、网络等，并持续、按时交付，不会出现令人讨厌的意外。

### Web 开发人员的整体信息安全（分册 1）

由三部分组成的系列丛书的第二部分，广泛而深入地介绍了 Web 开发人员和架构师需要了解的内容，以便创建强大、可靠、可维护和安全的软件、VPS、网络、云和 Web 应用程序，并且这些软件、VPS、网络、云和 Web 应用程序能够持续、按时交付，不会出现令人讨厌的意外情况。

## 课程

### 进攻性计算机安全 (CIS 4930) FSU

佛罗里达州立大学的 Owen Redwood 举办的漏洞研究和漏洞利用开发课程。

**请务必查看[讲座](https://www.cs.fsu.edu/~redwood/OffectiveComputerSecurity/lectures.html)！**

### 黑客之夜

《黑客之夜》以纽约大学理工学院旧的渗透测试和漏洞分析课程的材料为基础，对攻击性安全进行了发人深省的介绍。在十三周的时间里，向学生介绍各种复杂且身临其境的主题，许多复杂的技术内容很快就会被涵盖。

## 网站

### 破解这个网站！

通过尝试破解此网站来了解应用程序安全性。

### 恩尼格玛集团

黑客和安全专家来培训的地方。

### Web 应用程序安全测验

Web 应用程序安全自评测验

### 安全密码.info

多种语言/框架的安全密码。

### 安全新闻提要备忘单

安全新闻来源列表。

### 开放安全培训

有关低级 x86 编程、黑客攻击和取证的视频课程。

### 微腐败

夺旗 - 学习汇编和嵌入式设备安全

### Matasano 加密挑战

[Matasano Security](http://matasano.com) 提供的一系列用于自学密码学的编程练习。 Maciej Ceglowski 的[简介](https://blog.pinboard.in/2013/04/the_matasano_crypto_challenges) 解释得很好。

### 渗透测试实验室

PentesterLab 提供[免费的动手练习](https://pentesterlab.com/exercises/) 和 [bootcamp](https://pentesterlab.com/bootcamp/) 来入门。

### 果汁店

故意不安全的 Javascript Web 应用程序。

### 超级跑车对决

如何在网络攻击者发起攻击之前发起攻击。

### OWASP 节点山羊

故意容易受到 OWASP Top 10 Node.JS Web 应用程序的攻击，其中包括[教程](https://nodegoat.herokuapp.com/tutorial)、[使用 OWASP Zap API 进行安全回归测试](https://github.com/OWASP/NodeGoat/wiki/NodeGoat-Security-Regression-tests-with-ZAP-API)、[docker图片]（https://github.com/owasp/nodegoat#option-3---run-nodegoat-on-docker）。有多种选项可以快速启动和运行。

### 保护堆栈的安全

双周应用安全教程

### OWASP 无服务器山羊

OWASP ServerlessGoat 是一个故意不安全的现实 AWS Lambda 无服务器应用程序，由 OWASP 维护并由 [PureSec](https://www.puresec.io/) 创建。您可以安装 WebGoat，了解漏洞、如何利用它们以及如何修复每个问题。该项目还包括解释这些问题以及如何通过最佳实践进行补救的文档。

### SecDim

SecDim 是一个 appsec 寓教于乐平台，[学习](https://learn.secdim.com) appsec 具有基于 git 的免费实验室。您认为您具备构建安全应用程序所需的能力吗？用appsec 游戏[挑战自己](https://play.secdim.com)！修复错误，获得分数并让你的名字出现在排行榜上。

### 博客

#### 加密失败

展示糟糕的加密技术

#### NCC 集团 - 博客

NCC Group（原 Matasano）、iSEC Partners 和 NGS Secure 的博客。

#### 斯科特·赫尔姆

了解安全性和性能。

#### 哥萨克实验室博客 (2018)

**发布**：2018 年 7 月 30 日

加密公司的博客，该公司制作开源库和工具，并描述应用程序和基础设施的实用数据安全方法。

### 维基页面

#### OWASP 十佳项目

Web 应用程序中发现的十大最常见和最严重的安全漏洞。

### 工具

#### Qualys SSL 实验室

臭名昭著的 SSL 和 TLS 工具套件。

#### 安全标头.io

快速轻松地评估 HTTP 响应标头的安全性。

#### 报告-uri.io

免费的 CSP 和 HPKP 报告服务。

#### 点击劫持者io

测试并学习点击劫持。制作点击劫持 PoC、截图并分享链接。您可以测试 HTTPS、HTTP、Intranet 和内部站点。

# AWS Lambda

## 工具

### PureSec 功能盾

FunctionShield 是一个 100% 免费的 AWS Lambda 安全和 Google Cloud Functions 安全库，使开发人员能够轻松地对无服务器运行时实施严格的安全控制。

# 安卓

## 书籍和电子书

### SEI CERT Android 安全编码标准 (2015)

**发布**：2015 年 2 月 24 日

由社区维护的 Wiki，详细介绍了 Android 开发的安全编码标准。

#C

## 书籍和电子书

### SEI CERT C 编码标准 (2006)

**发布**：2006 年 5 月 24 日

由社区维护的 Wiki，详细介绍了 C 编程的安全编码标准。

### 防御性编码：Fedora 安全团队提高软件安全性指南 (2025)

**发布**：2025 年 2 月 22 日

提供通过安全编码提高软件安全性的指南。涵盖常见的编程语言和库，并重点关注具体建议。

# C++

## 书籍和电子书

### SEI CERT C++ 编码标准 (2006)

**发布**：2006 年 7 月 18 日

由社区维护的 Wiki，详细介绍了 C++ 编程的安全编码标准。

#C夏普

## 书籍和电子书

### !nonfree 安全驱动的 .NET (2015)

**发布**：2015 年 7 月 14 日

介绍如何开发针对 .NET Framework 4.5 版本的安全应用程序，特别涵盖加密和安全工程主题。

# Clojure

## 存储库

### Clojure OWASP (2020)

**发布**：2020 年 5 月 5 日

包含 OWASP 十大漏洞的 Clojure 示例的存储库。

# 去

## 文章

### Go 中的内存安全 - spacetime.dev (2017)

**发布**：2017 年 8 月 3 日

管理内存中敏感数据的指南。

# Java

## 书籍和电子书

### SEI CERT Java 编码标准 (2007)

**发布**：2007 年 1 月 12 日

由社区维护的 Wiki，详细介绍了 Java 编程的安全编码标准。

### Java SE 安全编码指南 (2014)

**发布**：2014 年 4 月 2 日

直接来自 Oracle 的安全 Java 编程指南。

# 节点.js

## 文章

### Node.js 安全检查表 - Rising Stack 博客 (2015)

**发布**：2015 年 10 月 13 日

涵盖了开发安全 Node.js 应用程序的大量有用信息。

### 很棒的 Electron.js 黑客和渗透测试资源 (2020)

**发布**：2020 年 6 月 17 日

用于保护基于 Electron.js 的应用程序的精选资源列表。

## 书籍和电子书

### !nonfree Node.js 基本安全 (2017)

**发布**：2017 年 7 月 19 日

实用且丰富的源代码，提供了保护 Node.js Web 应用程序安全的实用指南。

## 培训

### ^Lift Security 提供的 !nonfree 安全培训

向带头[节点安全项目](https://nodesecurity.io)的团队学习

### !BinaryMist 的非免费安全培训

我们开展多种类型的信息安全培训，涵盖物理、人员、VPS、网络、云、Web 应用程序。大部分内容来源于 Kim 多年来致力于的[系列丛书](https://leanpub.com/b/holisticinfosecforwebdevelopers)。更多信息可以在[此处](https://binarymist.io/#services)找到

# PHP

## 文章

### 一切都与时间有关 (2014)

**发布**：2014 年 11 月 28 日

简单介绍 PHP 应用程序中的定时攻击

### PHP 中的安全身份验证具有长期持久性 (2015)

**发布**：2015 年 4 月 21 日

讨论密码策略、密码存储、“记住我”cookie 和帐户恢复。

### 防止 PHP 中跨站脚本的 20 个要点列表 (2013)

**发布**：2013 年 4 月 22 日

Padriac Brady 关于构建不易受 XSS 攻击的软件的建议

### 系统管理员的 25 个 PHP 安全最佳实践 (2011)

**发布**：2011 年 11 月 23 日

尽管这篇文章已有几年历史，但当我们即将转向 PHP 7 时，其中的许多建议仍然具有相关性。

### PHP 数据加密入门 (2014)

**发布**：2014 年 6 月 16 日

@timoh6 解释了在 PHP 中实现数据加密

### 防止 PHP 应用程序中的 SQL 注入 - 简单而权威的指南 (2014)

**发布**：2014 年 5 月 26 日

**TL;DR** - 不要转义，而是使用准备好的语句！

### 你不会用 Base64 编码密码 - 密码学解码 (2015)

**发布**：2015 年 8 月 7 日

对常见误用的密码学术语和基本概念的人类可读概述，并带有 PHP 示例代码。

如果您对密码学术语感到困惑，请从这里开始。

### PHP 应用程序中的安全数据加密指南 (2015)

**发布**：2015 年 8 月 2 日

讨论端到端网络层加密 (HTTPS) 以及静态数据安全加密的重要性，然后介绍开发人员应针对特定用例使用的特定加密工具，无论他们使用 [libsodium](https://pecl.php.net/package/libsodium)、[Defuse Security 的安全 PHP 加密库](https://github.com/defuse/php-encryption) 还是 OpenSSL。

### 2018 年构建安全 PHP 软件指南 (2017)

**发布**：2017 年 12 月 12 日

本指南应作为电子书 [PHP: The Right Way](http://www.phptherightway.com) 的补充，重点强调安全性而不是一般的 PHP 程序员主题（例如代码风格）。

## 书籍和电子书

### !nonfree 确保 PHP 安全：核心概念

*保护 PHP：核心概念* 充当一些最常见安全术语的指南，并提供了日常 PHP 中的一些示例。

### 在 PHP 项目中使用 Libsodium

您不需要应用密码学博士学位来构建安全的 Web 应用程序。进入 libsodium，它允许开发人员开发快速、安全且可靠的应用程序，而无需知道流密码是什么。

## 有用的库

### 化解/php 加密

PHP 应用程序的对称密钥加密库。 （**推荐**超过你自己的！）

### ircmaxell/password_compat

如果您使用 PHP 5.3.7+ 或 5.4，请使用它来散列密码

### ircmaxell/RandomLib

对于生成随机字符串或数字很有用

### thephpleague/oauth2-服务器

安全的 OAuth2 服务器实现

### paragonie/random_compat

PHP 7 提供了一组新的 CSPRNG 函数：“random_bytes()”和“random_int()”。这是社区努力在 PHP 5 项目（前向兼容层）中公开相同的 API。获得麻省理工学院许可。

### 伪/看门人

一个安全的身份验证和授权库，可实现基于角色的访问控制和 Paragon Initiative Enterprises 对[安全“记住我”复选框]的建议(https://paragonie.com/blog/2015/04/secure-authentication-php-with-long-term-persistence#title.2)。

### 开放墙/phpass

用于 PHP 应用程序的便携式公共域密码哈希框架。

## 网站

### websec.io

**websec.io** 致力于对开发人员进行安全教育，主题涉及一般安全基础知识、新兴技术和 PHP 特定信息

### 博客

#### 模范倡议企业博客

我们位于佛罗里达州奥兰多的技术和安全咨询公司的博客

#### ircmaxell 的博客

关于 PHP、安全性、性能和一般 Web 应用程序开发的博客。

#### 帕德拉克·布雷迪的博客

Pádraic Brady 是 Zend Framework 安全专家

### 邮件列表

#### 确保 PHP 每周安全

关于 PHP、安全性和社区的每周新闻通讯。

# 珀尔

## 书籍和电子书

### SEI CERT Perl 编码标准 (2011)

**发布**：2011 年 1 月 10 日

由社区维护的 Wiki，详细介绍了 Perl 编程的安全编码标准。

# Python

## 书籍和电子书

### Fedora 防御性编码指南的 Python 章节

列出了应避免的标准库功能，以及其他章节中特定于 Python 的参考部分。

### !nonfree Black Hat Python：面向黑客和渗透测试人员的 Python 编程

NoStarch Press 的 Justin Seitz 所著的《Black Hat Python》对于进攻性安全头脑来说是一本很棒的书

### !nonfree 暴力 Python

Violent Python 向您展示如何从对攻击性计算概念的理论理解转向实际实施。

## 网站

### OWASP Python 安全维基 (2014)

**发布**：2014 年 6 月 21 日

由 OWASP Python 安全项目维护的 wiki。

# 红宝石

## 书籍和电子书

### 安全 Ruby 开发指南 (2014)

**发布**：2014 年 3 月 10 日

Fedora 安全团队提供的安全 Ruby 开发指南。也可以在 [Github](https://github.com/jrusnack/secure-ruby-development-guide) 上找到。
