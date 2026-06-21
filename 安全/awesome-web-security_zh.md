# 很棒的网络安全 [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

[<img src="https://upload.wikimedia.org/wikipedia/commons/6/61/HTML5_logo_and_wordmark.svg"align="right"width="70">](https://www.w3.org/TR/html5/)

> 🐶 网络安全材料和资源的精选列表。

不用说，大多数网站都存在各种类型的错误，这些错误最终可能导致漏洞。为什么这种情况会经常发生？可能涉及很多因素，包括配置错误、工程师缺乏安全技能等。为了解决这个问题，这里有一个用于学习尖端渗透技术的网络安全材料和资源的精选列表，我强烈建议您首先阅读这篇文章“[那么你想成为一名网络安全研究员？](https://portswigger.net/blog/so-you-want-to-be-a-web-security-researcher)”。

*贡献前请阅读[贡献指南](CONTRIBUTING.md)。*

---

<palign="center"><b>🌈想要增强你的渗透能力吗？</b><br>我建议玩一些<a href="https://github.com/apsdehal/awesome-ctf" target="_blank">awesome-ctf</a>。</p>

---

如果您喜欢这个很棒的列表并想支持它，请查看我的 [Patreon](https://www.patreon.com/boik) 页面:)<br>另外，不要忘记查看我的 [repos](https://github.com/qazbnm456) 🐾 或在 [X（以前的 Twitter）](https://x.com/boik_su) 上打个招呼！

---

### 🤖 使用人工智能助手？

该列表还作为克劳德代码技能提供，因此人工智能代理可以在运行时查询它 - 没有过时的快照，始终从“master”读取最新的“data/index.json”。

**安装**（单行，推荐）：

```bash
npx skills add qazbnm456/awesome-web-security -a claude-code -g -y
```

或者在 [Claude Code](https://claude.com/claude-code) 中，使用插件市场：

```text
/plugin marketplace add qazbnm456/awesome-web-security
/plugin install awesome-web-security
```

对于 [Codex](https://github.com/openai/codex)，交换 `-a claude-code` → `-a codex`。

然后询问任何网络安全问题，该技能就会激活，涉及 XSS、SQLi、SSRF、JWT、OAuth、侦察、WAF 规避、反序列化、SAML、CTF 编写等主题。请参阅 [`skills/awesome-web-security/SKILL.md`](skills/awesome-web-security/SKILL.md) 了解完整的触发器列表。


## 内容

- [Digests](#digests)
- [Forums](#forums)
- [Introduction](#intro)
  - [XSS](#xss---cross-site-scripting)
  - [原型污染](#prototype-pollution)
  - [CSV注入](#csv-injection)
  - [SQL注入](#sql-injection)
  - [命令注入](#command-injection)
  - [ORM注入](#orm-injection)
  - [FTP注入](#ftp-injection)
  - [XXE](#xxe---xml-external-entity)
  - [CSRF](#csrf---cross-site-request-forgery)
  - [Clickjacking](#clickjacking)
  - [SSRF](#ssrf---server-side-request-forgery)
  - [网络缓存中毒](#web-cache-poisoning)
  - [相对路径覆盖](#relative-path-overwrite)
  - [打开重定向](#open-redirect)
  - [SAML](#saml)
  - [Upload](#upload)
  - [Rails](#rails)
  - [AngularJS](#angularjs)
  - [ReactJS](#reactjs)
  - [SSL/TLS](#ssltls)
  - [Webmail](#webmail)
  - [NFS](#nfs)
  - [AWS](#aws)
  - [Azure](#azure)
  - [Fingerprint](#fingerprint)
  - [子域枚举](#sub-domain-enumeration)
  - [Crypto](#crypto)
  - [网络外壳](#web-shell)
  - [OSINT](#osint)
  - [DNS 重新绑定](#dns-rebinding)
  - [Deserialization](#deserialization)
  - [OAuth](#oauth)
  - [JWT](#jwt)
- [Evasions](#evasions)
  - [XXE](#evasions-xxe)
  - [CSP](#evasions-csp)
  - [WAF](#evasions-waf)
  - [JSMVC](#evasions-jsmvc)
  - [Authentication](#evasions-authentication)
- [Tricks](#tricks)
  - [CSRF](#tricks-csrf)
  - [Clickjacking](#tricks-clickjacking)
  - [远程代码执行](#tricks-rce)
  - [XSS](#tricks-xss)
  - [SQL注入](#tricks-sql-injection)
  - [NoSQL注入](#tricks-nosql-injection)
  - [FTP注入](#tricks-ftp-injection)
  - [XXE](#tricks-xxe)
  - [SSRF](#tricks-ssrf)
  - [网络缓存中毒](#tricks-web-cache-poisoning)
  - [标头注入](#tricks-header-injection)
  - [URL](#tricks-url)
  - [Deserialization](#tricks-deserialization)
  - [OAuth](#tricks-oauth)
  - [Others](#tricks-others)
- [浏览器利用](#browser-exploitation)
- [PoCs](#pocs)
  - [Database](#pocs-database)
- [Cheetsheets](#cheetsheets)
- [Tools](#tools)
  - [Auditing](#tools-auditing)
  - [命令注入](#tools-command-injection)
  - [Reconnaissance](#tools-reconnaissance)
    - [OSINT](#tools-osint)
    - [子域枚举](#tools-sub-domain-enumeration)
  - [代码生成](#tools-code-generating)
  - [Fuzzing](#tools-fuzzing)
  - [Scanning](#tools-scanning)
  - [渗透测试](#tools-penetration-testing)
  - [Offensive](#tools-offensive)
    - [XSS](#tools-xss)
    - [SQL注入](#tools-sql-injection)
    - [模板注入](#tools-template-injection)
    - [XXE](#tools-xxe)
    - [CSRF](#tools-csrf)
    - [SSRF](#tools-ssrf)
  - [Leaking](#tools-leaking)
  - [Detecting](#tools-detecting)
  - [Preventing](#tools-preventing)
  - [Proxy](#tools-proxy)
  - [Webshell](#tools-webshell)
  - [Disassembler](#tools-disassembler)
  - [Decompiler](#tools-decompiler)
  - [DNS 重新绑定](#tools-dns-rebinding)
  - [Others](#tools-others)
- [社会工程数据库](#social-engineering-database)
- [Blogs](#blogs)
- [推特用户](#twitter-users)
- [Practices](#practices)
  - [Application](#practices-application)
  - [AWS](#practices-aws)
  - [XSS](#practices-xss)
  - [ModSecurity / OWASP ModSecurity 核心规则集](#practices-modsecurity)
- [Community](#community)
- [Miscellaneous](#miscellaneous)

## 摘要

- [CTF Field Guide](https://trailofbits.github.io/ctf/) - 由 [Trail of Bits](https://www.trailofbits.com/) 编写。
- [Hacker101](https://www.hacker101.com/) - 由 [hackerone](https://www.hackerone.com/start-hacking) 编写。
- [Infosec Newbie](https://www.sneakymonkey.net/2017/04/23/infosec-newbie/) - 由[马克·罗宾逊](https://www.sneakymonkey.net/) 撰写。
- [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings/) - 由 [@swisskyrepo](https://github.com/swisskyrepo) 编写。
- [The Daily Swig - Web security digest](https://portswigger.net/daily-swig) - 由 [PortSwigger](https://portswigger.net/) 编写。
- [The Magic of Learning](https://bitvijays.github.io/) - 由 [@bitvijays](https://bitvijays.github.io/aboutme.html) 编写。
- [Web Application Security Zone by Netsparker](https://www.netsparker.com/blog/web-security/) - 由 [Netsparker](https://www.netsparker.com/) 编写。
- [tl;dr sec](https://tldrsec.com/) - 顶级安全工具、博客文章和安全研究的每周摘要。

## 论坛

- [Dark Reading](https://www.darkreading.com/Default.asp) - 连接信息安全社区。
- [HackDig](http://en.hackdig.com/) - 为黑客挖掘高质量的网络安全文章。
- [Phrack Magazine](http://www.phrack.org/) - 由黑客编写并为黑客服务的电子杂志。
- [Security Weekly](https://securityweekly.com/) - 安全播客网络。
- [The Hacker News](https://thehackernews.com/) - 严肃认真地保障安全。
- [The Register](http://www.theregister.co.uk/) - 咬住养育 IT 的手。

<a name="intro"></a>
## 简介

<a name="xss"></a>
### XSS - 跨站脚本

- [C.XSS Guide](https://excess-xss.com/) - 由 [@JakobKallin](https://github.com/JakobKallin) 和 [Irene Lobo Valbuena](https://www.linkedin.com/in/irenelobovalbuena/) 编写。
- [Cross-Site Scripting – Application Security – Google](https://www.google.com/intl/sw/about/appsecurity/learning/xss/) - 由 [Google](https://www.google.com/) 编写。
- [H5SC](https://github.com/cure53/H5SC) - 由 [@cure53](https://github.com/cure53) 编写。
- [THE BIG BAD WOLF - XSS AND MAINTAINING ACCESS](http://www.paulosyibelo.com/2018/06/the-big-bad-wolf-xss-and-maintaining.html) - 由 [Paulos Yibelo](http://www.paulosyibelo.com/) 撰写。
- [AwesomeXSS](https://github.com/s0md3v/AwesomeXSS) - 由 [@s0md3v](https://github.com/s0md3v) 编写。
- [XSS.png](https://github.com/LucaBongiorni/XSS.png) - 由@jackmasa 撰写。
- [PayloadsAllTheThings - XSS Injection](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/XSS%20Injection) - 由 [@swisskyrepo](https://github.com/swisskyrepo) 编写。
- [payloadbox/xss-payload-list](https://github.com/payloadbox/xss-payload-list) - 由 [@payloadbox](https://github.com/payloadbox) 编写。
- [Laravel Content Security Policy: Complete Implementation Guide](https://blog.shakiltech.com/laravel-content-security-policy-guide/) - 在 Laravel 中实施内容安全策略的实践指南 — nonce 生命周期、Vite 和 Livewire 集成、违规报告和预执行检查表，作者：[@itxshakil](https://github.com/itxshakil)。

<a name="prototype-pollution"></a>
### 原型污染

- [Prototype pollution attack in NodeJS application](https://github.com/HoLyVieR/prototype-pollution-nsec18/blob/master/paper/JavaScript_prototype_pollution_attack_in_NodeJS.pdf) - 由 [@HoLyVieR](https://github.com/HoLyVieR) 编写。
- [Real-world JS - 1](https://blog.p6.is/Real-World-JS-1/) - 由 [@po6ix](https://twitter.com/po6ix) 撰写。
- [Exploiting prototype pollution – RCE in Kibana (CVE-2019-7609)](https://research.securitum.com/prototype-pollution-rce-kibana-cve-2019-7609/) - 由 [@securitymb](https://twitter.com/securitymb) 撰写。

<a name="csv-injection"></a>
### CSV注入

- [CSV Injection -> Meterpreter on Pornhub](https://news.webamooz.com/wp-content/uploads/bot/offsecmag/147.pdf) - 由[安迪]（https://blog.zsec.uk/）撰写。
- [The Absurdly Underestimated Dangers of CSV Injection](http://georgemauer.net/2017/10/07/csv-injection.html) - 由[乔治·莫尔](http://georgemauer.net/) 撰写。
- [PayloadsAllTheThings - CSV Injection](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/CSV%20Injection) - 由 [@swisskyrepo](https://github.com/swisskyrepo) 编写。

<a name="sql-injection"></a>
### SQL注入

- [SQL Injection Cheat Sheet](https://www.netsparker.com/blog/web-security/sql-injection-cheat-sheet/) - 由 [@netsparker](https://twitter.com/netsparker) 撰写。
- [SQL Injection Pocket Reference](https://websec.ca/kb/sql_injection) - 由 [@LightOS](https://twitter.com/LightOS) 编写。
- [SQL Injection Wiki](https://sqlwiki.netspi.com/) - 由 [NETSPI](https://www.netspi.com/) 编写。
- [PayloadsAllTheThings - SQL Injection](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/SQL%20Injection) - 由 [@swisskyrepo](https://github.com/swisskyrepo) 编写。
- [payloadbox/sql-injection-payload-list](https://github.com/payloadbox/sql-injection-payload-list) - 由 [@payloadbox](https://github.com/payloadbox) 编写。

<a name="command-injection"></a>
### 命令注入

- [Potential command injection in resolv.rb](https://github.com/ruby/ruby/pull/1777) - 由 [@drigg3r](https://github.com/drigg3r) 编写。
- [PayloadsAllTheThings - Command Injection](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Command%20Injection) - 由 [@swisskyrepo](https://github.com/swisskyrepo) 编写。
- [payloadbox/command-injection-payload-list](https://github.com/payloadbox/command-injection-payload-list) - 由 [@payloadbox](https://github.com/payloadbox) 编写。

<a name="orm-injection"></a>
### ORM注入

- [HQL : Hyperinsane Query Language (or how to access the whole SQL API within a HQL injection ?)](https://www.synacktiv.com/ressources/hql2sql_sstic_2015_en.pdf) - 由 [@_m0bius](https://twitter.com/_m0bius) 撰写。
- [HQL for pentesters](http://blog.h3xstream.com/2014/02/hql-for-pentesters.html) - 由 [@h3xstream](https://twitter.com/h3xstream/) 撰写。
- [ORM Injection](https://www.slideshare.net/simone.onofri/orm-injection) - 由[西蒙·奥诺弗里](https://onofri.org/) 撰写。
- [ORM2Pwn: Exploiting injections in Hibernate ORM](https://www.slideshare.net/0ang3el/orm2pwn-exploiting-injections-in-hibernate-orm) - 作者：[Mikhail Egorov](https://0ang3el.blogspot.tw/)。

<a name="ftp-injection"></a>
### FTP注入

- [Advisory: Java/Python FTP Injections Allow for Firewall Bypass](http://blog.blindspotsecurity.com/2017/02/advisory-javapython-ftp-injections.html) - 由[蒂莫西·摩根](https://plus.google.com/105917618099766831589)撰写。
- [SMTP over XXE − how to send emails using Java's XML parser](https://shiftordie.de/blog/2017/02/18/smtp-over-xxe/) - 由 [Alexander Klink](https://shiftordie.de/) 撰写。

<a name="xxe"></a>
### XXE - XML 外部实体

- [XXE](https://phonexicum.github.io/infosec/xxe.html) - 由 [@phonexicum](https://twitter.com/phonexicum) 撰写。
- [PayloadsAllTheThings - XXE Injection](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/XXE%20Injection) - 由不同的贡献者撰写。
- [XML external entity (XXE) injection](https://portswigger.net/web-security/xxe) - 由 [portswigger](https://portswigger.net/) 编写。
- [XML Schema, DTD, and Entity Attacks](https://www.vsecurity.com/download/publications/XMLDTDEntityAttacks.pdf) - 由 [Timothy D. Morgan](https://twitter.com/ecbftw) 和 Omar Al Ibrahim 撰写。
- [payloadbox/xxe-injection-payload-list](https://github.com/payloadbox/xxe-injection-payload-list) - 由 [@payloadbox](https://github.com/payloadbox) 编写。

<a name="csrf"></a>
### CSRF - 跨站请求伪造

- [Wiping Out CSRF](https://medium.com/@jrozner/wiping-out-csrf-ded97ae7e83f) - 由 [@jrozner](https://medium.com/@jrozner) 撰写。
- [PayloadsAllTheThings - CSRF Injection](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/CSRF%20Injection) - 由 [@swisskyrepo](https://github.com/swisskyrepo) 编写。

<a name="clickjacking"></a>
### 点击劫持

- [Clickjacking](https://www.imperva.com/learn/application-security/clickjacking/) - 由 [Imperva](https://www.imperva.com/) 编写。
- [X-Frame-Options: All about Clickjacking?](https://github.com/cure53/Publications/blob/master/xfo-clickjacking.pdf?raw=true) - 由 [Mario Heiderich](http://www.slideshare.net/x00mario) 撰写。

<a name="ssrf"></a>
### SSRF - 服务器端请求伪造

- [SSRF bible. Cheatsheet](https://docs.google.com/document/d/1v1TkWZtrhzRLy0bYXBcdLUedXGb9njTNIJXa3u9akHM/edit) - 由 [Wallarm](https://wallarm.com/) 编写。
- [PayloadsAllTheThings - Server-Side Request Forgery](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Request%20Forgery) - 由 [@swisskyrepo](https://github.com/swisskyrepo) 编写。

<a name="web-cache-poisoning"></a>
### 网络缓存中毒

- [Practical Web Cache Poisoning](https://portswigger.net/blog/practical-web-cache-poisoning) - 由 [@albinowax](https://twitter.com/albinowax) 撰写。
- [PayloadsAllTheThings - Web Cache Deception](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Web%20Cache%20Deception) - 由 [@swisskyrepo](https://github.com/swisskyrepo) 编写。

<a name="relative-path-overwrite"></a>
### 相对路径覆盖

- [Large-scale analysis of style injection by relative path overwrite](https://blog.acolyer.org/2018/05/28/large-scale-analysis-of-style-injection-by-relative-path-overwrite/) - 由[晨报](https://blog.acolyer.org/)撰写。
- [MBSD Technical Whitepaper - A few RPO exploitation techniques](https://www.mbsd.jp/Whitepaper/rpo.pdf) - 由 [Mitsui Bussan Secure Directions, Inc.](https://www.mbsd.jp/) 编写。

<a name="open-redirect"></a>
### 打开重定向

- [Open Redirect Vulnerability](https://s0cket7.com/open-redirect-vulnerability/) - 由 [s0cket7](https://s0cket7.com/) 编写。
- [PayloadsAllTheThings - Open Redirect](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Open%20Redirect) - 由 [@swisskyrepo](https://github.com/swisskyrepo) 编写。
- [payloadbox/open-redirect-payload-list](https://github.com/payloadbox/open-redirect-payload-list) - 由 [@payloadbox](https://github.com/payloadbox) 编写。

<a name="saml"></a>
### 安全断言标记语言 (SAML)

- [How to Hunt Bugs in SAML; a Methodology - Part I](https://epi052.gitlab.io/notes-to-self/blog/2019-03-07-how-to-test-saml-a-methodology/) - 由 [epi](https://epi052.gitlab.io/notes-to-self/) 编写。
- [How to Hunt Bugs in SAML; a Methodology - Part II](https://epi052.gitlab.io/notes-to-self/blog/2019-03-13-how-to-test-saml-a-methodology-part-two/) - 由 [epi](https://epi052.gitlab.io/notes-to-self/) 编写。
- [How to Hunt Bugs in SAML; a Methodology - Part III](https://epi052.gitlab.io/notes-to-self/blog/2019-03-16-how-to-test-saml-a-methodology-part-three/) - 由 [epi](https://epi052.gitlab.io/notes-to-self/) 编写。
- [PayloadsAllTheThings - SAML Injection](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/SAML%20Injection) - 由 [@swisskyrepo](https://github.com/swisskyrepo) 编写。

<a name="upload"></a>
### 上传

- [File Upload Restrictions Bypass](https://www.exploit-db.com/docs/english/45074-file-upload-restrictions-bypass.pdf) - 由 [Haboob 团队](https://www.exploit-db.com/author/?a=9381) 编写。
- [PayloadsAllTheThings - Upload Insecure Files](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Upload%20Insecure%20Files) - 由 [@swisskyrepo](https://github.com/swisskyrepo) 编写。

<a name="rails"></a>
### 导轨

- [Rails Security - First part](https://hackmd.io/s/SkuTVw5O-) - 由 [@qazbnm456](https://github.com/qazbnm456) 编写。
- [Official Rails Security Guide](http://guides.rubyonrails.org/security.html) - 由 [Rails 团队](https://rubyonrails.org/) 编写。
- [Rails SQL Injection](https://rails-sqli.org) - 由 [@presidentbeef](https://github.com/presidentbeef) 编写。
- [Zen Rails Security Checklist](https://github.com/brunofacca/zen-rails-security-checklist) - 由 [@brunofacca](https://github.com/brunofacca) 编写。

<a name="angularjs"></a>
### AngularJS

- [DOM based Angular sandbox escapes](http://blog.portswigger.net/2017/05/dom-based-angularjs-sandbox-escapes.html) - 由 [@garethheyes](https://twitter.com/garethheyes) 撰写。
- [XSS without HTML: Client-Side Template Injection with AngularJS](http://blog.portswigger.net/2016/01/xss-without-html-client-side-template.html) - 由 [Gareth Heyes](https://www.blogger.com/profile/10856178524811553475) 撰写。

<a name="reactjs"></a>
### ReactJS

- [XSS via a spoofed React element](http://danlec.com/blog/xss-via-a-spoofed-react-element) - 由 [Daniel LeCheminant](http://danlec.com/) 撰写。

<a name="ssl-tls"></a>
### SSL/TLS

- [SSL & TLS Penetration Testing](https://www.aptive.co.uk/blog/tls-ssl-security-testing/) - 由 [APTIVE](https://www.aptive.co.uk/) 撰写。
- [Practical introduction to SSL/TLS](https://github.com/Hakky54/mutual-tls-ssl) - 由 [@Hakky54](https://github.com/Hakky54) 编写。

<a name="webmail"></a>
### 网络邮件

- [Why mail() is dangerous in PHP](https://blog.ripstech.com/2017/why-mail-is-dangerous-in-php/) - 由 [Robin Peraglie](https://www.ripstech.com/) 撰写。

<a name="nfs"></a>
### 网络文件系统

- [NFS | PENETRATION TESTING ACADEMY](https://pentestacademy.wordpress.com/2017/09/20/nfs/?t=1&cn=ZmxleGlibGVfcmVjc18y&refsrc=email&iid=b34422ce15164e99a193fea0ccc7a02f&uid=1959680352&nid=244+289476616) - 由[渗透学院](https://pentestacademy.wordpress.com/) 撰写。

<a name="aws"></a>
### AWS

- [PENETRATION TESTING AWS STORAGE: KICKING THE S3 BUCKET](https://rhinosecuritylabs.com/penetration-testing/penetration-testing-aws-storage/) - 由 [Rhino Security Labs](https://rhinosecuritylabs.com/) 的 Dwight Hohnstein 撰写。
- [AWS PENETRATION TESTING PART 1. S3 BUCKETS](https://www.virtuesecurity.com/aws-penetration-testing-part-1-s3-buckets/) - 由 [VirtueSecurity](https://www.virtuesecurity.com/) 编写。
- [AWS PENETRATION TESTING PART 2. S3, IAM, EC2](https://www.virtuesecurity.com/aws-penetration-testing-part-2-s3-iam-ec2/) - 由 [VirtueSecurity](https://www.virtuesecurity.com/) 编写。
- [Misadventures in AWS](https://labs.f-secure.com/blog/misadventures-in-aws) - 由克里斯蒂安·德姆科撰写。

<a name="azure"></a>
### 天蓝色

- [Cloud Security Risks (Part 1): Azure CSV Injection Vulnerability](https://rhinosecuritylabs.com/azure/cloud-security-risks-part-1-azure-csv-injection-vulnerability/) - 由 [@spengietz](https://twitter.com/spengietz) 撰写。
- [Common Azure Security Vulnerabilities and Misconfigurations](https://rhinosecuritylabs.com/cloud-security/common-azure-security-vulnerabilities/) - 由 [@rhinobenjamin](https://twitter.com/rhinobenjamin) 撰写。

<a name="fingerprint"></a>
### 指纹

<a name="sub-domain-enumeration"></a>
### 子域枚举

- [A penetration tester’s guide to sub-domain enumeration](https://blog.appsecco.com/a-penetration-testers-guide-to-sub-domain-enumeration-7d842d5570f6) - 由 [Bharath](https://blog.appsecco.com/@yamakira_) 撰写。
- [The Art of Subdomain Enumeration](https://blog.sweepatic.com/art-of-subdomain-enumeration/) - 由 [Patrik Hudak](https://blog.sweepatic.com/author/patrik/) 撰写。

<a name="crypto"></a>
### 加密货币

- [Applied Crypto Hardening](https://bettercrypto.org/) - 由 [bettercrypto.org 团队](https://bettercrypto.org/) 编写。
- [What is a Side-Channel Attack ?](https://www.csoonline.com/article/3388647/what-is-a-side-channel-attack-how-these-end-runs-around-encryption-put-everyone-at-risk.html) - 作者：[J.M.Porup](https://www.csoonline.com/author/J.M.-Porup/)。

<a name="web-shell"></a>
### 网络外壳

- [Hacking with JSP Shells](https://blog.netspi.com/hacking-with-jsp-shells/) - 由 [@_nullbind](https://twitter.com/_nullbind) 编写。
- [Hunting for Web Shells](https://www.tenable.com/blog/hunting-for-web-shells) - 由 [雅各布·贝恩斯](https://www.tenable.com/profile/jacob-baines) 撰写。

<a name="osint"></a>
### 开源情报

- [Hacking Cryptocurrency Miners with OSINT Techniques](https://medium.com/@s3yfullah/hacking-cryptocurrency-miners-with-osint-techniques-677bbb3e0157) - 由 [@s3yfullah](https://medium.com/@s3yfullah) 撰写。
- [OSINT x UCCU Workshop on Open Source Intelligence](https://www.slideshare.net/miaoski/osint-x-uccu-workshop-on-open-source-intelligence) - 作者：[Philippe Lin](https://www.slideshare.net/miaoski)。
- [102 Deep Dive in the Dark Web OSINT Style Kirby Plessas](https://www.youtube.com/watch?v=fzd3zkAI_o4) - 由 [@kirbstr](https://twitter.com/kirbstr) 提出。
- [The most complete guide to finding anyone’s email](https://www.blurbiz.io/blog/the-most-complete-guide-to-finding-anyones-email) - 由 [Timur Daudpota](https://www.blurbiz.io/) 撰写。

<a name="dns-rebinding"></a>
### DNS 重新绑定

- [Attacking Private Networks from the Internet with DNS Rebinding](https://medium.com/@brannondorsey/attacking-private-networks-from-the-internet-with-dns-rebinding-ea7098a2d325) - 由 [@brannondorsey](https://medium.com/@brannondorsey) 撰写。
- [Hacking home routers from the Internet](https://medium.com/@radekk/hackers-can-get-access-to-your-home-router-1ddadd12a7a7) - 由 [@radekk](https://medium.com/@radekk) 撰写。

<a name="deserialization"></a>
### 反序列化

- [What Do WebLogic, WebSphere, JBoss, Jenkins, OpenNMS, and Your Application Have in Common? This Vulnerability.](https://foxglovesecurity.com/2015/11/06/what-do-weblogic-websphere-jboss-jenkins-opennms-and-your-application-have-in-common-this-vulnerability/) - 由 [@breenmachine](https://twitter.com/breenmachine) 撰写。
- [.NET Roulette: Exploiting Insecure Deserialization in Telerik UI](https://www.youtube.com/watch?v=--6PiuvBGAU) - 由 [@noperator](https://twitter.com/noperator) 撰写。
- [Attacking .NET deserialization](https://www.youtube.com/watch?v=eDfGpu3iE4Q) - 由 [@pwntester](https://twitter.com/pwntester) 撰写。
- [How to exploit the DotNetNuke Cookie Deserialization](https://pentest-tools.com/blog/exploit-dotnetnuke-cookie-deserialization/) - 由 [CRISTIAN CORNEA](https://pentest-tools.com/blog/author/pentest-cristian/) 撰写。
- [HOW TO EXPLOIT LIFERAY CVE-2020-7961 : QUICK JOURNEY TO POC](https://www.synacktiv.com/en/publications/how-to-exploit-liferay-cve-2020-7961-quick-journey-to-poc.html) - 由 [@synacktiv](https://twitter.com/synacktiv) 撰写。

<a name="oauth"></a>
### 开放认证

- [What is going on with OAuth 2.0? And why you should not use it for authentication.](https://medium.com/securing/what-is-going-on-with-oauth-2-0-and-why-you-should-not-use-it-for-authentication-5f47597b2611) - 由 [@damianrusinek](https://medium.com/@damianrusinek) 撰写。
- [Introduction to OAuth 2.0 and OpenID Connect](https://pragmaticwebsecurity.com/courses/introduction-oauth-oidc.html) - 由 [@PhilippeDeRyck](https://twitter.com/PhilippeDeRyck) 撰写。

<a name="jwt"></a>
### 智威汤逊

- [Hardcoded secrets, unverified tokens, and other common JWT mistakes](https://r2c.dev/blog/2020/hardcoded-secrets-unverified-tokens-and-other-common-jwt-mistakes/) - 由 [@ermil0v](https://twitter.com/ermil0v) 撰写。

## 逃避

<a name="evasions-xxe"></a>
### XXE

- [Bypass Fix of OOB XXE Using Different encoding](https://twitter.com/SpiderSec/status/1191375472690528256) - 由 [@SpiderSec](https://twitter.com/SpiderSec) 撰写。

<a name="evasions-csp"></a>
### 太阳能光伏发电

- [CSP: bypassing form-action with reflected XSS](https://labs.detectify.com/2016/04/04/csp-bypassing-form-action-with-reflected-xss/) - 由 [Detectify Labs](https://labs.detectify.com/) 编写。
- [TWITTER XSS + CSP BYPASS](http://www.paulosyibelo.com/2017/05/twitter-xss-csp-bypass.html) - 由 [Paulos Yibelo](http://www.paulosyibelo.com/) 撰写。
- [Neatly bypassing CSP](https://lab.wallarm.com/how-to-trick-csp-in-letting-you-run-whatever-you-want-73cb5ff428aa) - 由 [Wallarm](https://wallarm.com/) 编写。
- [Evading CSP with DOM-based dangling markup](https://portswigger.net/blog/evading-csp-with-dom-based-dangling-markup) - 由 [portswigger](https://portswigger.net/) 编写。
- [GitHub's CSP journey](https://githubengineering.com/githubs-csp-journey/) - 由 [@ptoomey3](https://github.com/ptoomey3) 编写。
- [GitHub's post-CSP journey](https://githubengineering.com/githubs-post-csp-journey/) - 由 [@ptoomey3](https://github.com/ptoomey3) 编写。
- [Any protection against dynamic module import?](https://github.com/w3c/webappsec-csp/issues/243) - 由 [@shhnjk](https://twitter.com/@shhnjk) 撰写。

<a name="evasions-waf"></a>
### WAF

- [Airbnb – When Bypassing JSON Encoding, XSS Filter, WAF, CSP, and Auditor turns into Eight Vulnerabilities](https://buer.haus/2017/03/08/airbnb-when-bypassing-json-encoding-xss-filter-waf-csp-and-auditor-turns-into-eight-vulnerabilities/) - 由 [@Brett Buerhaus](https://twitter.com/bbuerhaus) 撰写。
- [How to bypass libinjection in many WAF/NGWAF](https://medium.com/@d0znpp/how-to-bypass-libinjection-in-many-waf-ngwaf-1e2513453c0f) - 由 [@d0znpp](https://medium.com/@d0znpp) 编写。
- [Web Application Firewall (WAF) Evasion Techniques](https://medium.com/secjuice/waf-evasion-techniques-718026d693d8) - 由 [@secjuice](https://twitter.com/secjuice) 撰写。
- [Web Application Firewall (WAF) Evasion Techniques #2](https://medium.com/secjuice/web-application-firewall-waf-evasion-techniques-2-125995f3e7b0) - 由 [@secjuice](https://twitter.com/secjuice) 撰写。

<a name="evasions-jsmvc"></a>
### JSMVC

- [JavaScript MVC and Templating Frameworks](http://www.slideshare.net/x00mario/jsmvcomfg-to-sternly-look-at-javascript-mvc-and-templating-frameworks) - 由 [Mario Heiderich](http://www.slideshare.net/x00mario) 撰写。

<a name="evasions-authentication"></a>
### 认证

- [Trend Micro Threat Discovery Appliance - Session Generation Authentication Bypass (CVE-2016-8584)](http://blog.malerisch.net/2017/04/trend-micro-threat-discovery-appliance-session-generation-authentication-bypass-cve-2016-8584.html) - 由 [@malerisch](https://twitter.com/malerisch) 和 [@steventseeley](https://twitter.com/steventseeley) 撰写。

## 技巧

<a name="tricks-csrf"></a>
### CSRF

- [Exploiting CSRF on JSON endpoints with Flash and redirects](https://blog.appsecco.com/exploiting-csrf-on-json-endpoints-with-flash-and-redirects-681d4ad6b31b) - 由 [@riyazwalikar](https://blog.appsecco.com/@riyazwalikar) 撰写。
- [Neat tricks to bypass CSRF-protection](https://zhuanlan.zhihu.com/p/32716181) - 由 [Twosecurity](https://twosecurity.io/) 编写。
- [Stealing CSRF tokens with CSS injection (without iFrames)](https://github.com/dxa4481/cssInjection) - 由 [@dxa4481](https://github.com/dxa4481) 编写。
- [Cracking Java’s RNG for CSRF - Javax Faces and Why CSRF Token Randomness Matters](https://blog.securityevaluators.com/cracking-javas-rng-for-csrf-ea9cacd231d2) - 由 [@rramgattie](https://blog.securityevaluators.com/@rramgattie) 撰写。
- [If HttpOnly You Could Still CSRF… Of CORS you can!](https://medium.com/@_graphx/if-httponly-you-could-still-csrf-of-cors-you-can-5d7ee2c7443) - 由 [@GraphX](https://twitter.com/GraphX) 撰写。

<a name="tricks-clickjacking"></a>
### 点击劫持

- [Clickjackings in Google worth 14981.7$](https://medium.com/@raushanraj_65039/google-clickjacking-6a04132b918a) - 由 [@raushanraj_65039](https://medium.com/@raushanraj_65039) 撰写。

<a name="tricks-rce"></a>
### 远程代码执行

- [DRUPAL 7.X SERVICES MODULE UNSERIALIZE() TO RCE](https://www.ambionics.io/blog/drupal-services-module-rce) - 由[Ambionics Security](https://www.ambionics.io/)编写。
- [Exploiting Node.js deserialization bug for Remote Code Execution](https://opsecx.com/index.php/2017/02/08/exploiting-node-js-deserialization-bug-for-remote-code-execution/) - 由 [OpSecX](https://opsecx.com/index.php/author/ajinabraham/) 编写。
- [GitHub Enterprise Remote Code Execution](https://bounty.github.com/researchers/iblue.html) - 由 [@iblue](https://github.com/iblue) 编写。
- [How I Chained 4 vulnerabilities on GitHub Enterprise, From SSRF Execution Chain to RCE!](http://blog.orange.tw/2017/07/how-i-chained-4-vulnerabilities-on.html) - 作者：[Orange](http://blog.orange.tw/)。
- [How we exploited a remote code execution vulnerability in math.js](https://capacitorset.github.io/mathjs/) - 由 [@capacitorset](https://github.com/capacitorset) 编写。
- [$36k Google App Engine RCE](https://sites.google.com/site/testsitehacking/-36k-google-app-engine-rce) - 由 [Ezequiel Pereira](https://sites.google.com/site/testsitehacking/) 撰写。
- [Poor RichFaces](https://codewhitesec.blogspot.com/2018/05/poor-richfaces.html) - 由 [白色代码](https://www.code-white.com/) 编写。
- [Remote Code Execution on a Facebook server](https://blog.scrt.ch/2018/08/24/remote-code-execution-on-a-facebook-server/) - 由 [@blaklis_](https://twitter.com/blaklis_) 撰写。
- [Evil Teacher: Code Injection in Moodle](https://blog.ripstech.com/2018/moodle-remote-code-execution/) - 由 [RIPS Technologies](https://www.ripstech.com/) 编写。
- [WebLogic RCE (CVE-2019-2725) Debug Diary](https://paper.seebug.org/910/) - 由 Badcode@知道创宇 404 团队编写。
- [What Do WebLogic, WebSphere, JBoss, Jenkins, OpenNMS, and Your Application Have in Common? This Vulnerability.](https://foxglovesecurity.com/2015/11/06/what-do-weblogic-websphere-jboss-jenkins-opennms-and-your-application-have-in-common-this-vulnerability/) - 由 [@breenmachine](https://twitter.com/@breenmachine) 撰写。
- [CVE-2019-1306: ARE YOU MY INDEX?](https://www.thezdi.com/blog/2019/10/23/cve-2019-1306-are-you-my-index) - 由 [@yu5k3](https://twitter.com/yu5k3) 撰写。

<a name="tricks-xss"></a>
### 跨站脚本攻击

- [DON'T TRUST THE DOM: BYPASSING XSS MITIGATIONS VIA SCRIPT GADGETS](https://www.blackhat.com/docs/us-17/thursday/us-17-Lekies-Dont-Trust-The-DOM-Bypassing-XSS-Mitigations-Via-Script-Gadgets.pdf) - 由 [Sebastian Lekies](https://twitter.com/slekies)、[Krzysztof Kotowicz](https://twitter.com/kkotowicz) 和 [Eduardo Vela](https://twitter.com/sirdarckcat) 撰写。
- [ECMAScript 6 from an Attacker's Perspective - Breaking Frameworks, Sandboxes, and everything else](http://www.slideshare.net/x00mario/es6-en) - 由 [Mario Heiderich](http://www.slideshare.net/x00mario) 撰写。
- [How I found a $5,000 Google Maps XSS (by fiddling with Protobuf)](https://medium.com/@marin_m/how-i-found-a-5-000-google-maps-xss-by-fiddling-with-protobuf-963ee0d9caff#.u50nrzhas) - 由 [@marin_m](https://medium.com/@marin_m) 撰写。
- [Query parameter reordering causes redirect page to render unsafe URL](https://hackerone.com/reports/293689) - 由 [kenziy](https://hackerone.com/kenziy) 编写。
- [Uber XSS via Cookie](http://zhchbin.github.io/2017/08/30/Uber-XSS-via-Cookie/) - 由[zhchbin](http://zhchbin.github.io/)编写。
- [Stored XSS on Facebook](https://opnsec.com/2018/03/stored-xss-on-facebook/) - 由 [Enguerran Gillier](https://opnsec.com/) 撰写。
- [DOM XSS – auth.uber.com](http://stamone-bug-bounty.blogspot.tw/2017/10/dom-xss-auth14.html) - 作者：[StamOne_](http://stamone-bug-bounty.blogspot.tw/)。
- [Another XSS in Google Colaboratory](https://blog.bentkowski.info/2018/09/another-xss-in-google-colaboratory.html) - 由 [Michał Bentkowski](https://blog.bentkowski.info/) 撰写。
- [XSS in Google Colaboratory + CSP bypass](https://blog.bentkowski.info/2018/06/xss-in-google-colaboratory-csp-bypass.html) - 由 [Michał Bentkowski](https://blog.bentkowski.info/) 撰写。
- [</script> is filtered ?](https://twitter.com/strukt93/status/931586377665331200) - 由 [@strukt93](https://twitter.com/strukt93) 撰写。
- [XSS-Auditor — the protector of unprotected and the deceiver of protected.](https://medium.com/bugbountywriteup/xss-auditor-the-protector-of-unprotected-f900a5e15b7b) - 由 [@terjanq](https://medium.com/@terjanq) 编写。
- [XSS without parentheses and semi-colons](https://portswigger.net/blog/xss-without-parentheses-and-semi-colons) - 由 [@garethheyes](https://twitter.com/garethheyes) 撰写。
- [Upgrade self XSS to Exploitable XSS an 3 Ways Technic](https://www.hahwul.com/2019/11/upgrade-self-xss-to-exploitable-xss.html) - 由 [HAHWUL](https://www.hahwul.com/) 撰写。
- [Exploiting XSS with 20 characters limitation](https://jlajara.gitlab.io/posts/2019/11/30/XSS_20_characters.html) - 由 [Jorge Lajara](https://jlajara.gitlab.io/) 编写。
- [$20000 Facebook DOM XSS](https://vinothkumar.me/20000-facebook-dom-xss/) - 由 [@vinodsparrow](https://twitter.com/vinodsparrow) 撰写。

<a name="tricks-sql-injection"></a>
### SQL注入

- [GitHub Enterprise SQL Injection](http://blog.orange.tw/2017/01/bug-bounty-github-enterprise-sql-injection.html) - 作者：[Orange](http://blog.orange.tw/)。
- [SQL injection in an UPDATE query - a bug bounty story!](http://zombiehelp54.blogspot.jp/2017/02/sql-injection-in-update-query-bug.html) - 由 [Zombiehelp54](http://zombiehelp54.blogspot.jp/) 撰写。
- [Making a Blind SQL Injection a little less blind](https://medium.com/@tomnomnom/making-a-blind-sql-injection-a-little-less-blind-428dcb614ba8) - 由 [TomNomNom](https://twitter.com/TomNomNom) 撰写。
- [Red Team Tales 0x01: From MSSQL to RCE](https://www.tarlogic.com/en/blog/red-team-tales-0x01/) - 由 [Tarlogic](https://www.tarlogic.com/en/cybersecurity-blog/) 编写。
- [MySQL Error Based SQL Injection Using EXP](https://www.exploit-db.com/docs/english/37953-mysql-error-based-sql-injection-using-exp.pdf) - 由 [@osandamalith](https://twitter.com/osandamalith) 撰写。
- [SQL INJECTION AND POSTGRES - AN ADVENTURE TO EVENTUAL RCE](https://pulsesecurity.co.nz/articles/postgres-sqli) - 由 [@denandz](https://github.com/denandz) 编写。

<a name="tricks-nosql-injection"></a>
### NoSQL注入

- [GraphQL NoSQL Injection Through JSON Types](http://www.petecorey.com/blog/2017/06/12/graphql-nosql-injection-through-json-types/) - 由[皮特](http://www.petecorey.com/work/) 撰写。

<a name="tricks-ftp-injection"></a>
### FTP注入

- [XML Out-Of-Band Data Retrieval](https://media.blackhat.com/eu-13/briefings/Osipov/bh-eu-13-XML-data-osipov-slides.pdf) - 由 [@a66at](https://twitter.com/a66at) 和 Alexey Osipov 撰写。
- [XXE OOB exploitation at Java 1.7+](http://lab.onsec.ru/2014/06/xxe-oob-exploitation-at-java-17.html) - 由 [Ivan Novikov](http://lab.onsec.ru/) 撰写。

<a name="tricks-xxe"></a>
### XXE

- [Evil XML with two encodings](https://mohemiv.com/all/evil-xml/) - 由 [Arseniy Sharoglazov](https://mohemiv.com/) 撰写。
- [Automating local DTD discovery for XXE exploitation](https://www.gosecure.net/blog/2019/07/16/automating-local-dtd-discovery-for-xxe-exploitation) - 由 [Philippe Arteau](https://twitter.com/h3xstream) 撰写。
- [Exploiting XXE with local DTD files](https://mohemiv.com/all/exploiting-xxe-with-local-dtd-files/) - 由 [Arseniy Sharoglazov](https://twitter.com/_mohemiv) 撰写。
- [Forcing XXE Reflection through Server Error Messages](https://blog.netspi.com/forcing-xxe-reflection-server-error-messages/) - 由 [Antti Rantasaari](https://blog.netspi.com/author/antti-rantasaari/) 撰写。
- [Pre-authentication XXE vulnerability in the Services Drupal module](https://www.synacktiv.com/ressources/synacktiv_drupal_xxe_services.pdf) - 由 [Renaud Dubourguais](https://twitter.com/_m0bius) 撰写。
- [What You Didn't Know About XML External Entities Attacks](https://2013.appsecusa.org/2013/wp-content/uploads/2013/12/WhatYouDidntKnowAboutXXEAttacks.pdf) - 由 [蒂莫西·摩根](https://twitter.com/ecbftw) 撰写。
- [XML Out-Of-Band Data Retrieval](https://media.blackhat.com/eu-13/briefings/Osipov/bh-eu-13-XML-data-osipov-slides.pdf) - 由帖木儿·尤努索夫和阿列克谢·奥西波夫撰写。
- [XXE in WeChat Pay Sdk ( WeChat leave a backdoor on merchant websites)](http://seclists.org/fulldisclosure/2018/Jul/3) - 由 [Rose Jackcode](https://twitter.com/codeshtool) 编写。
- [XXE OOB exploitation at Java 1.7+ (2014)](http://lab.onsec.ru/2014/06/xxe-oob-exploitation-at-java-17.html) - 使用 FTP 协议进行渗透 - 由 [Ivan Novikov](https://twitter.com/d0znpp/) 撰写。
- [XXE OOB extracting via HTTP+FTP using single opened port](https://skavans.ru/en/2017/12/02/xxe-oob-extracting-via-httpftp-using-single-opened-port/) - 由 [skavans](https://skavans.ru/) 撰写。

<a name="tricks-ssrf"></a>
### SSRF

- [A New Era of SSRF - Exploiting URL Parser in Trending Programming Languages!](https://www.blackhat.com/docs/us-17/thursday/us-17-Tsai-A-New-Era-Of-SSRF-Exploiting-URL-Parser-In-Trending-Programming-Languages.pdf) - 作者：[Orange](http://blog.orange.tw/)。
- [SSRF in https://imgur.com/vidgif/url](https://hackerone.com/reports/115748) - 由 [aesteral](https://hackerone.com/aesteral) 编写。
- [SSRF Tips](http://blog.safebuff.com/2016/07/03/SSRF-Tips/) - 由 [xl7dev](http://blog.safebuff.com/) 编写。
- [PHP SSRF Techniques](https://medium.com/secjuice/php-ssrf-techniques-9d422cb28d51) - 由 [@themiddleblue](https://medium.com/@themiddleblue) 撰写。
- [SSRF in Exchange leads to ROOT access in all instances](https://hackerone.com/reports/341876) - 由 [@0xacb](https://twitter.com/0xacb) 撰写。
- [Into the Borg – SSRF inside Google production network](https://opnsec.com/2018/07/into-the-borg-ssrf-inside-google-production-network/) - 由 [opnsec](https://opnsec.com/) 编写。
- [Piercing the Veil: Server Side Request Forgery to NIPRNet access](https://medium.com/bugbountywriteup/piercing-the-veil-server-side-request-forgery-to-niprnet-access-c358fd5e249a) - 由 [Alyssa Herrera](https://medium.com/@alyssa.o.herrera) 撰写。
- [All you need to know about SSRF and how may we write tools to do auto-detect](https://www.auxy.xyz/web%20security/2017/07/06/all-ssrf-knowledge.html) - 由 [@Auxy233](https://twitter.com/Auxy233) 撰写。
- [AWS takeover through SSRF in JavaScript](http://10degres.net/aws-takeover-through-ssrf-in-javascript/) - 由 [Gwen](http://10degres.net/) 撰写。

<a name="tricks-web-cache-poisoning"></a>
### 网络缓存中毒

- [Bypassing Web Cache Poisoning Countermeasures](https://portswigger.net/blog/bypassing-web-cache-poisoning-countermeasures) - 由 [@albinowax](https://twitter.com/albinowax) 撰写。
- [Cache poisoning and other dirty tricks](https://lab.wallarm.com/cache-poisoning-and-other-dirty-tricks-120468f1053f) - 由 [Wallarm](https://wallarm.com/) 编写。

<a name="tricks-header-injection"></a>
### 标头注入

- [Java/Python FTP Injections Allow for Firewall Bypass](http://blog.blindspotsecurity.com/2017/02/advisory-javapython-ftp-injections.html) - 由[蒂莫西·摩根](https://plus.google.com/105917618099766831589)撰写。

<a name="tricks-url"></a>
### 网址

- [[dev.twitter.com] XSS](http://blog.blackfan.ru/2017/09/devtwittercom-xss.html) - 由 [Sergey Bobrov](http://blog.blackfan.ru/) 撰写。
- [Phishing with Unicode Domains](https://www.xudongz.com/blog/2017/idn-phishing/) - 作者：[郑旭东](https://www.xudongz.com/)。
- [Some Problems Of URLs](https://noncombatant.org/2017/11/07/problems-of-urls/) - 由 [Chris Palmer](https://noncombatant.org/about/) 撰写。
- [Unicode Domains are bad and you should feel bad for supporting them](https://www.vgrsec.com/post20170219.html) - 由 [VRGSEC](https://www.vgrsec.com/) 编写。

<a name="tricks-deserialization"></a>
### 反序列化

- [ASP.NET resource files (.RESX) and deserialisation issues](https://www.nccgroup.trust/uk/about-us/newsroom-and-events/blogs/2018/august/aspnet-resource-files-resx-and-deserialisation-issues/) - 由 [@irsdl](https://twitter.com/irsdl) 撰写。

<a name="tricks-oauth"></a>
### 开放认证

- [Facebook OAuth Framework Vulnerability](https://www.amolbaikar.com/facebook-oauth-framework-vulnerability/) - 由 [@AmolBaikar](https://twitter.com/AmolBaikar) 撰写。

<a name="tricks-others"></a>
### 其他

- [Inducing DNS Leaks in Onion Web Services](https://github.com/epidemics-scepticism/writing/blob/master/onion-dns-leaks.md) - 由 [@epidemics-skepticism](https://github.com/epidemics-skepticism) 撰写。
- [Stored XSS, and SSRF in Google using the Dataset Publishing Language](https://s1gnalcha0s.github.io/dspl/2018/03/07/Stored-XSS-and-SSRF-Google.html) - 由 [@signalchaos](https://twitter.com/signalchaos) 撰写。
- [How I hacked Google’s bug tracking system itself for $15,600 in bounties](https://medium.com/free-code-camp/messing-with-the-google-buganizer-system-for-15-600-in-bounties-58f86cc9f9a5) - 由 [@alex.birsan](https://medium.com/@alex.birsan) 撰写。
- [Some Tricks From My Secret Group](https://www.leavesongs.com/SHARE/some-tricks-from-my-secret-group.html) - 由 [phithon](https://www.leavesongs.com/) 编写。

## 浏览器利用

### 前端（例如 SOP 绕过、URL 欺骗等）

- [IE11 Information disclosure - local file detection](https://www.facebook.com/ExploitWareLabs/photos/a.361854183878462.84544.338832389513975/1378579648872572/?type=3&theater) - 由詹姆斯·李撰写。
- [JSON hijacking for the modern web](http://blog.portswigger.net/2016/11/json-hijacking-for-modern-web.html) - 由 [portswigger](https://portswigger.net/) 编写。
- [SOP bypass / UXSS – Stealing Credentials Pretty Fast (Edge)](https://www.brokenbrowser.com/sop-bypass-uxss-stealing-credentials-pretty-fast/) - 由[曼努埃尔](https://twitter.com/magicmac2000)撰写。
- [Особенности Safari в client-side атаках](https://bo0om.ru/safari-client-side) - 由 [Bo0oM](https://bo0om.ru/author/admin) 撰写。
- [How do we Stop Spilling the Beans Across Origins?](https://docs.google.com/document/d/1cbL-X0kV_tQ5rL8XJ3lXkV-j0pt_CfTu5ZSzYrncPDc/) - 由 [aaj at google.com](mailto:aaj@google.com) 和 [mkwst at google.com](mailto:mkwst@google.com) 撰写。
- [Setting arbitrary request headers in Chromium via CRLF injection](https://blog.bentkowski.info/2018/06/setting-arbitrary-request-headers-in.html) - 由 [Michał Bentkowski](https://blog.bentkowski.info/) 撰写。
- [I’m harvesting credit card numbers and passwords from your site. Here’s how.](https://hackernoon.com/im-harvesting-credit-card-numbers-and-passwords-from-your-site-here-s-how-9a8cb347c5b5) - 由[大卫吉尔伯特森]（https://hackernoon.com/@david.gilbertson）撰写。
- [The inception bar: a new phishing method](https://jameshfisher.com/2019/04/27/the-inception-bar-a-new-phishing-method/) - 由 [jameshfisher](https://jameshfisher.com/) 编写。
- [Bypassing Mobile Browser Security For Fun And Profit](https://www.blackhat.com/docs/asia-16/materials/asia-16-Baloch-Bypassing-Browser-Security-Policies-For-Fun-And-Profit-wp.pdf) - 由 [@rafaybaloch](https://twitter.com/@rafaybaloch) 撰写。
- [The Cookie Monster in Your Browsers](https://speakerdeck.com/filedescriptor/the-cookie-monster-in-your-browsers) - 由 [@filedescriptor](https://twitter.com/filedescriptor) 编写。
- [The world of Site Isolation and compromised renderer](https://speakerdeck.com/shhnjk/the-world-of-site-isolation-and-compromised-renderer) - 由 [@shhnjk](https://twitter.com/shhnjk) 撰写。
- [Sending arbitrary IPC messages via overriding Function.prototype.apply](https://hackerone.com/reports/188086) - 由 [@kinukawamasato](https://twitter.com/kinukawamasato) 撰写。
- [Take Advantage of Out-of-Scope Domains in Bug Bounty Programs](https://ahussam.me/Take-Advantage-of-Out-of-Scope-Domains-in-Bug-Bounty/) - 由 [@Abdulahhusam](https://twitter.com/Abdulahhusam) 撰写。

### Backend（浏览器实现的核心，通常指C或C++部分）

- [Attacking JavaScript Engines - A case study of JavaScriptCore and CVE-2016-4622](http://www.phrack.org/papers/attacking_javascript_engines.html) - 由 [phrack@saelo.net]（邮件至：phrack@saelo.net）撰写。
- [Exploiting a V8 OOB write.](https://halbecaf.com/2017/05/24/exploiting-a-v8-oob-write/) - 由 [@halbecaf](https://twitter.com/halbecaf) 撰写。
- [SSD Advisory – Chrome Turbofan Remote Code Execution](https://blogs.securiteam.com/index.php/archives/3379) - 由 [SecuriTeam Secure Disclosure (SSD)](https://blogs.securiteam.com/) 撰写。
- [Look Mom, I don't use Shellcode - Browser Exploitation Case Study for Internet Explorer 11](https://labs.bluefrostsecurity.de/files/Look_Mom_I_Dont_Use_Shellcode-WP.pdf) - 由 [@moritzj](http://twitter.com/moritzj) 撰写。
- [PUSHING WEBKIT'S BUTTONS WITH A MOBILE PWN2OWN EXPLOIT](https://www.zerodayinitiative.com/blog/2018/2/12/pushing-webkits-buttons-with-a-mobile-pwn2own-exploit) - 由 [@wanderinggliitch](https://twitter.com/wanderinggliitch) 撰写。
- [A Methodical Approach to Browser Exploitation](https://blog.ret2.io/2018/06/05/pwn2own-2018-exploit-development/) - 由 [RET2 SYSTEMS, INC](https://blog.ret2.io/) 撰写。
- [CVE-2017-2446 or JSC::JSGlobalObject::isHavingABadTime.](https://doar-e.github.io/blog/2018/07/14/cve-2017-2446-or-jscjsglobalobjectishavingabadtime/) - 作者：[逆向工程师日记](https://doar-e.github.io/)。
- [Breaking UC Browser](https://habr.com/en/company/drweb/blog/452076/) - 由 [Доктор Веб](https://www.drweb.ru/) 撰写。
- [Three roads lead to Rome](http://blogs.360.cn/360safe/2016/11/29/three-roads-lead-to-rome-2/) - 由 [@holynop](https://twitter.com/holynop) 撰写。
- [CLEANLY ESCAPING THE CHROME SANDBOX](https://theori.io/research/escaping-chrome-sandbox) - 由 [@tjbecker_](https://twitter.com/tjbecker_) 撰写。

## 概念验证

<a name="pocs-database"></a>
### 数据库

- [awesome-cve-poc](https://github.com/qazbnm456/awesome-cve-poc) - 由 [@qazbnm456](https://github.com/qazbnm456) 整理的 CVE PoC 列表。
- [js-vuln-db](https://github.com/tunz/js-vuln-db) - [@tunz](https://github.com/tunz) 收集的带有 PoC 的 JavaScript 引擎 CVE。
- [Some-PoC-oR-ExP](https://github.com/coffeehb/Some-PoC-oR-ExP) - 各种漏洞poc、Exp的收集或编写 by [@coffeehb](https://github.com/coffeehb).
- [uxss-db](https://github.com/Metnew/uxss-db) - [@Metnew](https://github.com/Metnew) 收集的带有 PoC 的 UXSS CVE。
- [SPLOITUS](https://sploitus.com/) - 漏洞利用和工具搜索引擎，作者：[@i_bo0om](https://twitter.com/i_bo0om)。
- [Exploit Database](https://www.exploit-db.com/) - [Offective Security](https://www.offective-security.com/) 的漏洞利用、Shellcode 和安全文件的终极存档。

## 备忘单

- [Capture the Flag CheatSheet](https://github.com/uppusaikiran/awesome-ctf-cheatsheet) - 由 [@uppusaikiran](https://github.com/uppusaikiran) 编写。
- [XSS Cheat Sheet - 2018 Edition](https://leanpub.com/xss) - 由 [@brutelogic](https://twitter.com/brutelogic) 编写。

## 工具

<a name="tools-auditing"></a>
### 审计

- [A2SV](https://github.com/hahwul/a2sv) - 自动扫描 SSL 漏洞 [@hahwul](https://github.com/hahwul)。
- [prowler](https://github.com/Alfresco/prowler) - [@Alfresco](https://github.com/Alfresco) 用于 AWS 安全评估、审核和强化的工具。
- [slurp](https://github.com/hehnope/slurp) - 通过 [@hehnope](https://github.com/hehnope) 评估 S3 存储桶的安全性。

<a name="tools-command-injection"></a>
### 命令注入

- [commix](https://github.com/commixproject/commix) - 由 [@commixproject](https://github.com/commixproject) 提供的自动化一体化操作系统命令注入和利用工具。

<a name="tools-reconnaissance"></a>
### 侦察

<a name="tools-osint"></a>
#### OSINT - 开源情报

- [Censys](https://censys.io/) - Censys 是一个搜索引擎，允许计算机科学家提出有关构成互联网的设备和网络的问题，由[密歇根大学](https://umich.edu/) 提供。
- [FOCA](https://github.com/ElevenPaths/FOCA) - FOCA（Fingerprinting Organizations with Collected Archives）是一种工具，主要用于查找 [ElevenPaths](https://www.elevenpaths.com/index.html) 扫描的文档中的元数据和隐藏信息。
- [FOFA](https://fofa.so/?locale=en) - [BAIMAOHUI](http://baimaohui.net/) 的网络空间搜索引擎。
- [gitrob](https://github.com/michenriksen/Gitrob) - [@michenriksen](https://github.com/michenriksen) 为 GitHub 组织提供的侦察工具。
- [GSIL](https://github.com/FeeiCN/GSIL) - Github Sensitive Information Leakage（Github敏感信息泄露）by [@FeeiCN](https://github.com/FeeiCN).
- [NSFOCUS](https://nti.nsfocus.com/) - 绿盟科技威胁情报门户。
- [raven](https://github.com/0x09AL/raven) - raven 是一个 Linkedin 信息收集工具，渗透测试人员可以使用它通过 [@0x09AL](https://github.com/0x09AL) 收集有关使用 Linkedin 的组织员工的信息。
- [Shodan](https://www.shodan.io/) - Shodan 是世界上第一个针对互联网连接设备的搜索引擎，由 [@shodanhq](https://twitter.com/shodanhq) 开发。
- [SpiderFoot](http://www.spiderfoot.net/) - 由 [@binarypool](https://twitter.com/binarypool) 提供的开源足迹和情报收集工具。
- [urlscan.io](https://urlscan.io/) - 分析 [@heipei](https://twitter.com/heipei) 请求的网站及其资源的服务。
- [xray](https://github.com/evilsocket/xray) - XRay 是 [@evilsocket](https://github.com/evilsocket) 从公共网络进行侦察、绘图和 OSINT 收集的工具。
- [ZoomEye](https://www.zoomeye.org/) - 网络空间搜索引擎 [@zoomeye_team](https://twitter.com/zoomeye_team)。
- [Databases - start.me](https://start.me/p/QRENnO/databases) - 您可以使用 [@technisette](https://twitter.com/technisette) 进行开源情报研究的各种数据库。
- [peoplefindThor](https://peoplefindthor.dk/) - 通过 [postkassen](mailto:postkassen@oejvind.dk?subject=peoplefindthor.dk%20comments) 在 Facebook 上查找人员的简单方法。
- [tinfoleak](https://github.com/vaguileradiaz/tinfoleak) - 最完整的 Twitter 情报分析开源工具，由 [@vaguileradiaz](https://github.com/vaguileradiaz) 提供。
- [Photon](https://github.com/s0md3v/Photon) - 由 [@s0md3v](https://github.com/s0md3v) 为 OSINT 设计的速度惊人的爬虫。
- [ReconDog](https://github.com/s0md3v/ReconDog) - 侦察瑞士军刀，作者：[@s0md3v](https://github.com/s0md3v)。
- [espi0n/Dockerfiles](https://github.com/espi0n/Dockerfiles) - [@espi0n](https://github.com/espi0n) 提供的各种 OSINT 工具的 Dockerfile。
- [Raccoon](https://github.com/evyatarmeged/Raccoon) - 用于侦察和漏洞扫描的高性能攻击性安全工具，由 [@evyatarmeged](https://github.com/evyatarmeged) 提供。
- [Social Mapper](https://github.com/SpiderLabs/social_mapper) - Jacob Wilkin (Greenwolf) 的社交媒体枚举和关联工具，作者：[@SpiderLabs](https://github.com/SpiderLabs)。
- [Marshall Extensions](https://github.com/bad-antics/marshall-extensions) - Marshall 隐私浏览器的 OSINT 和安全扩展，由 [@bad-antics](https://github.com/bad-antics) 提供侦察和安全测试插件。
- [OpenBuckets](https://openbuckets.io/) - 针对任何提供商中配置错误的公共云存储桶的搜索引擎。

<a name="tools-sub-domain-enumeration"></a>
#### 子域枚举

- [AQUATONE](https://github.com/michenriksen/aquatone) - [@michenriksen](https://github.com/michenriksen) 的域 Flyovers 工具。
- [Certificate Search](https://crt.sh/) - 输入身份（域名、组织名称等）、证书指纹（SHA-1 或 SHA-256）或 crt.sh ID 以通过 [@crtsh](https://github.com/crtsh) 搜索证书。
- [Certificate Transparency](https://github.com/google/certificate-transparency) - Google 的证书透明度项目通过 [@google](https://github.com/google) 修复了 SSL 证书系统中的多个结构性缺陷。
- [domain_analyzer](https://github.com/eldraco/domain_analyzer) - 通过查找 [@eldraco](https://github.com/eldraco) 可能的所有信息来分析任何域的安全性。
- [EyeWitness](https://github.com/ChrisTruncer/EyeWitness) - EyeWitness 旨在截取网站屏幕截图，提供一些服务器标头信息，并在可能的情况下通过 [@ChrisTruncer](https://github.com/ChrisTruncer) 识别默认凭据。
- [GSDF](https://github.com/We5ter/GSDF) - 由 [@We5ter](https://github.com/We5ter) 命名为 GoogleSSLdomainFinder 的域搜索器。
- [subDomainsBrute](https://github.com/lijiejie/subDomainsBrute) - [@lijiejie](https://github.com/lijiejie) 为渗透测试人员提供的一个简单快速的子域暴力工具。
- [VirusTotal domain information](https://www.virustotal.com/en/documentation/searching/#getting-domain-information) - 通过[VirusTotal](https://www.virustotal.com/)搜索域名信息。
- [Sublist3r](https://github.com/aboul3la/Sublist3r) - Sublist3r 是 [@aboul3la](https://github.com/aboul3la) 为渗透测试人员提供的多线程子域枚举工具。

<a name="tools-code-generating"></a>
### 代码生成

- [VWGen](https://github.com/qazbnm456/VWGen) - 易受攻击的 Web 应用程序生成器，作者：[@qazbnm456](https://github.com/qazbnm456)。

<a name="tools-fuzzing"></a>
### 模糊测试

- [charsetinspect](https://github.com/hack-all-the-things/charsetinspect) - 检查多字节字符集的脚本，通过 [@hack-all-the-things](https://github.com/hack-all-the-things) 查找具有特定用户定义属性的字符。
- [IPObfuscator](https://github.com/OsandaMalith/IPObfuscator) - 通过 [@OsandaMalith](https://github.com/OsandaMalith) 将 IP 转换为 DWORD IP 的简单工具。
- [wfuzz](https://github.com/xmendez/wfuzz) - Web 应用程序暴力破解，作者：[@xmendez](https://github.com/xmendez)。
- [domato](https://github.com/google/domato) - DOM 模糊器 [@google](https://github.com/google)。
- [FuzzDB](https://github.com/fuzzdb-project/fuzzdb) - 用于黑盒应用程序故障注入和资源发现的攻击模式和原语字典。
- [dirhunt](https://github.com/Nekmo/dirhunt) - [@nekmo](https://github.com/Nekmo) 优化的网络爬虫，用于搜索和分析网站的目录结构。
- [ssltest](https://www.ssllabs.com/ssltest/) - 对公共互联网上任何 SSL Web 服务器的配置进行深入分析的在线服务。由 [Qualys SSL Labs](https://www.ssllabs.com) 提供。
- [fuzz.txt](https://github.com/Bo0oM/fuzz.txt) - [@Bo0oM](https://github.com/Bo0oM) 的潜在危险文件。
- [wayparam](https://github.com/aleff-github/wayparam) - 跨平台 Python CLI，通过 [@aleff-github](https://github.com/aleff-github) 从 Wayback CDX API 获取历史 URL 并输出用于模糊测试的规范化参数化 URL。

<a name="tools-scanning"></a>
### 扫描

- [JoomlaScan](https://github.com/drego85/JoomlaScan) - 用于查找 Joomla CMS 中安装的组件的免费软件，由 [@drego85](https://github.com/drego85) 在 Joomscan 的基础上构建。
- [wpscan](https://github.com/wpscanteam/wpscan) - WPScan 是 [@wpscanteam](https://github.com/wpscanteam) 的黑盒 WordPress 漏洞扫描器。
- [WAScan](https://github.com/m4ll0k/WAScan) - 是一个使用“黑盒”方法的开源 Web 应用程序安全扫描器，由 [@m4ll0k](https://github.com/m4ll0k) 创建。
- [Nuclei](https://github.com/projectdiscovery/nuclei) - Nuclei 是一种基于模板的可配置目标扫描快速工具，[@projectdiscovery](https://github.com/projectdiscovery) 提供了巨大的可扩展性和易用性。
- [ZAP by Checkmarx](https://zaproxy.org) - 由 ZAP 核心团队维护的开源 Web 应用程序安全扫描器。
- [Fray](https://github.com/dalisecurity/fray) - 开源 WAF 绕过和安全测试工具包，具有跨 OWASP 类别的 6,300 多个有效负载、AI 辅助规避引擎、27 检查侦察管道和 OWASP 强化审计，由 [@dalisecurity](https://github.com/dalisecurity) 提供。
- [Trust Scan](https://github.com/undeadlist/trust-scan) - URL 安全扫描器将威胁情报（URLhaus、PhishTank、Spamhaus）与 [@undeadlist](https://github.com/undeadlist) 的 40 多种诈骗和网络钓鱼模式检测相结合。
- [ZeroTrust](https://github.com/sattyamjjain/zerotrust) - 隐私优先的 Chrome 扩展程序，通过 [@sattyamjjain](https://github.com/sattyamjjain) 使用设备上的 AI (WebGPU) 在本地分析网站安全性，根据 HTTPS、网络钓鱼、恶意脚本和 cookie 合规信号生成信任分数。
- [SecuriTool](https://securitool.js.org/) - 免费在线收集 29 个客户端 Web 安全工具：Web 审核器、JWT 攻击者/解码器、CVE 搜索、CSP 评估器、电子邮件安全检查器 (SPF/DKIM/DMARC)、子域扫描器等。 100% 客户端，隐私第一，由 [@ReplikanteK](https://github.com/ReplikanteK) 开源。

<a name="tools-penetration-testing"></a>
### 渗透测试

- [Burp Suite](https://portswigger.net/burp/) - Burp Suite 是 [portswigger](https://portswigger.net/) 用于执行 Web 应用程序安全测试的集成平台。
- [Astra](https://github.com/flipkart-incubator/astra) - [@flipkart-incubator](https://github.com/flipkart-incubator) 对 REST API 进行自动安全测试。
- [aws_pwn](https://github.com/dagrz/aws_pwn) - [@dagrz](https://github.com/dagrz) 收集的 AWS 渗透测试垃圾。
- [grayhatwarfare](https://buckets.grayhatwarfare.com/) - [grayhatwarfare](http://www.grayhatwarfare.com/) 的公共存储桶。
- [TIDoS-Framework](https://github.com/theInfectedDrake/TIDoS-Framework) - 一个全面的 Web 应用程序审计框架，涵盖从侦察和 OSINT 到漏洞分析的所有内容（由 [@_tID](https://github.com/theInfectedDrake) 提供）。
- [numasec](https://github.com/FrancescoStabile/numasec) - AI 驱动的渗透测试平台，协调 10 个代理和 38 个漏洞扫描程序，涵盖 OWASP Top 10，作者：[@FrancescoStabile](https://github.com/FrancescoStabile)。

<a name="tools-offensive"></a>
### 进攻性

<a name="tools-xss"></a>
#### XSS - 跨站脚本

- [xssor2](https://github.com/evilcos/xssor2) - XSS'OR - 使用 JavaScript 进行黑客攻击，作者：[@evilcos](https://github.com/evilcos)。
- [XSStrike](https://github.com/s0md3v/XSStrike) - XSStrike 是一个可以对 XSS 参数进行模糊测试和暴力破解的程序。它还可以通过 [@s0md3v](https://github.com/s0md3v) 检测并绕过 WAF。
- [beef](https://github.com/beefproject/beef) - [beefproject](https://beefproject.com) 的浏览器利用框架项目。
- [JShell](https://github.com/s0md3v/JShell) - 通过 [@s0md3v](https://github.com/s0md3v) 获取带有 XSS 的 JavaScript shell。
- [csp evaluator](https://csper.io/evaluator) - [Csper](http://csper.io) 评估内容安全策略的工具。

<a name="tools-sql-injection"></a>
#### SQL注入

- [sqlmap](https://github.com/sqlmapproject/sqlmap) - 自动 SQL 注入和数据库接管工具。

<a name="tools-template-injection"></a>
#### 模板注入

- [tplmap](https://github.com/epinna/tplmap) - [@epinna](https://github.com/epinna) 的代码和服务器端模板注入检测和利用工具。

<a name="tools-xxe"></a>
#### XXE

- [dtd-finder](https://github.com/GoSecure/dtd-finder) - 通过 [@GoSecure](https://github.com/GoSecure) 列出 DTD 并使用这些本地 DTD 生成 XXE 有效负载。

<a name="tools-csrf"></a>
#### 跨站请求伪造

- [XSRFProbe](https://github.com/0xInfection/XSRFProbe) - Prime CSRF 审计和利用工具包，作者：[@0xInfection](https://github.com/0xinfection)。

<a name="tools-ssrf"></a>
#### 服务器端请求伪造

- [Open redirect/SSRF payload generator](https://tools.intigriti.io/redirector/) - 通过 [intigriti](https://www.intigriti.com/) 打开重定向/SSRF 有效负载生成器。

<a name="tools-leaking"></a>
### 泄漏

- [CSS-Keylogging](https://github.com/maxchehab/CSS-Keylogging) - Chrome 扩展和 Express 服务器利用 [@maxchehab](https://github.com/maxchehab) 的 CSS 键盘记录功能。
- [DVCS-Pillage](https://github.com/evilpacket/DVCS-Pillage) - 通过 [@evilpacket](https://github.com/evilpacket) 掠夺可通过网络访问的 GIT、HG 和 BZR 存储库。
- [dvcs-ripper](https://github.com/kost/dvcs-ripper) - Rip Web 可访问（分布式）版本控制系统：SVN/GIT/HG...作者：[@kost](https://github.com/kost)。
- [gitleaks](https://github.com/zricethezav/gitleaks) - 通过 [@zricethezav](https://github.com/zricethezav) 搜索完整的存储库历史记录以获取秘密和密钥。
- [GitMiner](https://github.com/UnkL4b/GitMiner) - 用于对 Github 上的内容进行高级挖掘的工具，由 [@UnkL4b](https://github.com/UnkL4b) 提供。
- [HTTPLeaks](https://github.com/cure53/HTTPLeaks) - 所有可能的方式，网站都可以通过 [@cure53](https://github.com/cure53) 泄露 HTTP 请求。
- [pwngitmanager](https://github.com/allyshka/pwngitmanager) - 渗透测试人员的 Git 管理器，作者：[@allyshka](https://github.com/allyshka)。
- [snallygaster](https://github.com/hannob/snallygaster) - 通过 [@hannob](https://github.com/hannob) 扫描 HTTP 服务器上的秘密文件的工具。
- [LinkFinder](https://github.com/GerbenJavado/LinkFinder) - 通过 [@GerbenJavado](https://github.com/GerbenJavado) 在 JavaScript 文件中查找端点的 Python 脚本。
- [keyFinder](https://github.com/momenbasel/keyFinder) - Chrome 扩展程序使用 80 多种检测模式和香农熵分析，被动扫描网页以查找 10 个攻击面中泄露的 API 密钥、令牌和凭证，作者：[@momenbasel](https://github.com/momenbasel)。

<a name="tools-detecting"></a>
### 检测

- [bXSS](https://github.com/LewisArdern/bXSS) - bXSS 是一个简单的盲 XSS 应用程序，改编自 [@LewisArdern](https://github.com/LewisArdern) 的 [cure53.de/m](https://cure53.de/m)。
- [malware-jail](https://github.com/HynekPetrak/malware-jail) - 用于半自动 Javascript 恶意软件分析、反混淆和有效负载提取的沙箱，由 [@HynekPetrak](https://github.com/HynekPetrak) 提供。
- [repo-supervisor](https://github.com/auth0/repo-supervisor) - 扫描您的代码是否存在安全配置错误，搜索密码和机密。
- [retire.js](https://github.com/RetireJS/retire.js) - 扫描仪通过 [@RetireJS](https://github.com/RetireJS) 检测具有已知漏洞的 JavaScript 库的使用情况。
- [sqlchop](https://sqlchop.chaitin.cn/) - SQL 注入检测引擎由 [chaitin](http://chaitin.com) 提供。
- [xsschop](https://xsschop.chaitin.cn/) - XSS 检测引擎由 [chaitin](http://chaitin.com) 提供。
- [OpenRASP](https://github.com/baidu/openrasp) - 由百度公司积极维护的开源 RASP 解决方案。通过上下文感知检测算法，该项目几乎实现了无误报。在服务器负载较重的情况下，观察到性能下降不到 3%。
- [GuardRails](https://github.com/apps/guardrails) - 一个在拉取请求中提供安全反馈的 GitHub 应用程序。

<a name="tools-preventing"></a>
### 预防

- [js-xss](https://github.com/leizongmin/js-xss) - 使用 [@leizongmin](https://github.com/leizongmin) 白名单指定的配置清理不受信任的 HTML（以防止 XSS）。
- [Acra](https://github.com/cossacklabs/acra) - SQL 数据库的客户端加密引擎，具有强大的选择性加密、SQL 注入防护和 [@cossacklabs](https://www.cossacklabs.com/) 入侵检测功能。
- [DOMPurify](https://github.com/cure53/DOMPurify) - [Cure53](https://cure53.de/) 提供的仅用于 HTML、MathML 和 SVG 的 DOM、超快速、超级容忍 XSS 清理程序。
- [Csper](https://csper.io) - 一组用于构建/评估/监控内容安全策略的工具，以防止/检测 [Csper](https://csper.io) 的跨站点脚本。
- [UUSEC WAF](https://github.com/Safe3/uusec-waf/) - 由 [UUCORP](https://github.com/Safe3/) 维护的开源 Web 应用程序防火墙和 API 安全网关。
- [BunkerWeb](https://www.bunkerweb.io) - 基于 nginx 构建的下一代开源 Web 应用防火墙，由 [Bunkerity](https://github.com/bunkerity) 维护。
- [FCaptcha](https://github.com/WebDecoy/FCaptcha) - 自托管 CAPTCHA，具有行为分析、视觉 AI 代理检测、无头浏览器指纹识别和 SHA-256 工作证明，由 [WebDecoy](https://github.com/WebDecoy) 维护。
- [Pompelmi](https://github.com/pompelmi/pompelmi) - Node.js 的进程内文件上传安全中间件，在存储之前扫描不受信任的上传，以检测恶意软件、MIME 欺骗和有风险的档案，由 [pompelmi](https://github.com/pompelmi) 维护。
- [WebDecoy](https://github.com/WebDecoy/wordpress-plugin) - 零配置 WordPress 机器人检测插件，结合了 WebDriver 检测、无头浏览器指纹识别、行为分析和 SHA-256 工作证明，由 [WebDecoy](https://github.com/WebDecoy) 维护。
- [CrowdSec](https://www.crowdsec.net/) - 用 Go 编写的开源协作 IPS，可分析访问者行为并在运营商社区中共享威胁信号，由 [CrowdSec](https://github.com/crowdsecurity) 维护。
- [Laravel CSP Generator](https://csp-generator.shakiltech.com) - Laravel 的交互式内容安全策略构建器，输出具有随机数支持和违规报告的即用型 PHP 中间件，作者：[@itxshakil](https://github.com/itxshakil)。
- [verifyfetch](https://github.com/hamzaydia/verifyfetch) - 使用 SRI 哈希对大文件进行浏览器端完整性验证和可恢复下载，防止 CDN 泄露和供应链攻击，作者：[@hamzaydia](https://github.com/hamzaydia)。

<a name="tools-proxy"></a>
### 代理

- [Charles](https://www.charlesproxy.com/) - HTTP 代理/HTTP 监视器/反向代理，使开发人员能够查看其计算机与 Internet 之间的所有 HTTP 和 SSL/HTTPS 流量。
- [mitmproxy](https://github.com/mitmproxy/mitmproxy) - 由 [@mitmproxy](https://github.com/mitmproxy) 为渗透测试人员和软件开发人员提供具有交互式 TLS 能力的拦截 HTTP 代理。

<a name="tools-webshell"></a>
### 网页外壳

- [reverse-shell](https://github.com/lukechilds/reverse-shell) - 反向 Shell 即服务，作者：[@lukechilds](https://github.com/lukechilds)。
- [Reverse-Shell-Manager](https://github.com/WangYihang/Reverse-Shell-Manager) - 通过终端反向 Shell 管理器 [@WangYihang](https://github.com/WangYihang)。
- [webshell](https://github.com/tennc/webshell) - 这是 [@tennc](https://github.com/tennc) 的一个 webshel​​l 开源项目。
- [Webshell-Sniper](https://github.com/WangYihang/Webshell-Sniper) - 通过[@WangYihang](https://github.com/WangYihang)通过终端管理您的网站。
- [Weevely](https://github.com/epinna/weevely3) - 由 [@epinna](https://github.com/epinna) 武器化的 Web shell。
- [nano](https://github.com/s0md3v/nano) - 由 [@s0md3v](https://github.com/s0md3v) 编写的 PHP shell 代码系列。
- [PhpSploit](https://github.com/nil0x42/phpsploit) - 全功能的 C2 框架，通过 [@nil0x42](https://github.com/nil0x42) 的邪恶 PHP oneliner 默默地保留在网络服务器上。

<a name="tools-disassembler"></a>
### 反汇编器

- [Iaitō](https://github.com/hteso/iaito) - 由 [@hteso](https://github.com/hteso) 提供的 Radare2 逆向工程框架的 Qt 和 C++ GUI。
- [plasma](https://github.com/plasma-disassembler/plasma) - Plasma 是 [@plasma-disassembler](https://github.com/plasma-disassembler) 的 x86/ARM/MIPS 交互式反汇编程序。
- [radare2](https://github.com/radare/radare2) - [@radare](https://github.com/radare) 的类 Unix 逆向工程框架和命令行工具。

<a name="tools-decompiler"></a>
### 反编译器

- [CFR](http://www.benf.org/other/cfr/) - [@LeeAtBenf](https://twitter.com/LeeAtBenf) 的另一个 java 反编译器。

<a name="tools-dns-rebinding"></a>
### DNS 重新绑定

- [DNS Rebind Toolkit](https://github.com/brannondorsey/dns-rebind-toolkit) - DNS Rebind Toolkit 是一个前端 JavaScript 框架，由 [@brannondorsey](https://github.com/brannondorsey) 开发，用于针对局域网 (LAN) 上易受攻击的主机和服务开发 DNS 重新绑定漏洞。
- [dref](https://github.com/mwrlabs/dref) - DNS 重新绑定利用框架。 Dref 由 [@mwrlabs](https://github.com/mwrlabs) 负责 DNS 重新绑定的繁重工作。
- [Singularity of Origin](https://github.com/nccgroup/singularity) - 它包括必要的组件，用于将攻击服务器 DNS 名称的 IP 地址重新绑定到目标计算机的 IP 地址，并通过 [@nccgroup](https://github.com/nccgroup) 提供攻击负载以利用目标计算机上的易受攻击的软件。
- [Whonow DNS Server](https://github.com/brannondorsey/whonow) - [@brannondorsey](https://github.com/brannondorsey) 用来执行 DNS 重新绑定攻击的恶意 DNS 服务器。

<a name="tools-others"></a>
### 其他

- [CyberChef](https://github.com/gchq/CyberChef) - Cyber Swiss Army Knife - 一款用于加密、编码、压缩和数据分析的 Web 应用程序 - 由 [@GCHQ](https://github.com/gchq) 开发。
- [Dnslogger](https://wiki.skullsecurity.org/index.php?title=Dnslogger) - DNS 记录器 [@iagox86](https://github.com/iagox86)。
- [cefdebug](https://github.com/taviso/cefdebug) - 通过 [@taviso](https://github.com/taviso) 连接到 CEF 调试器的最少代码。
- [ctftool](https://github.com/taviso/ctftool) - 交互式 CTF 探索工具，作者：[@taviso](https://github.com/taviso)。
- [ntlm_challenger](https://github.com/b17zr/ntlm_challenger) - 通过 [@b17zr](https://github.com/b17zr) 解析 NTLM over HTTP 质询消息。

## 社会工程数据库

- [haveibeenpwned](https://haveibeenpwned.com/) - 检查您的帐户是否因 [Troy Hunt](https://www.troyhunt.com/) 的数据泄露而受到损害。
- [Hudson Rock](https://www.hudsonrock.com/threat-intelligence-cybercrime-tools) - 检查您的电子邮件或域是否受到由 [Hudson Rock](https://www.hudsonrock.com/) 维护的 infostealer 恶意软件的危害。

## 博客

- [BRETT BUERHAUS](https://buer.haus/) - 漏洞披露和应用程序安全性漫谈。
- [Broken Browser](https://www.brokenbrowser.com/) - 浏览器漏洞的乐趣。
- [James Kettle](http://albinowax.skeletonscribe.net/) - [PortSwigger Web Security](https://portswigger.net/) 研究主管。
- [leavesongs](https://www.leavesongs.com/) - 中国天才的网络渗透者。
- [n0tr00t](https://www.n0tr00t.com/) - ~# n0tr00t 安全团队。
- [OpnSec](https://opnsec.com/) - 开放思想安全！
- [Orange](http://blog.orange.tw/) - 台湾天才网络渗透者。
- [Scrutiny](https://datarift.blogspot.tw/) - 通过 Web 浏览器实现互联网安全 作者：Dhiraj Mishra。
- [RIPS Technologies](https://blog.ripstech.com/tags/security/) - 针对 PHP 漏洞的文章。
- [0Day Labs](http://blog.0daylabs.com/) - 很棒的错误赏金和挑战文章。
- [Blog of Osanda](https://osandamalith.com/) - 安全研究和逆向工程。

## 推特用户

- [@cure53berlin](https://twitter.com/cure53berlin) - [Cure53](https://cure53.de/) 是一家德国网络安全公司。
- [@filedescriptor](https://twitter.com/filedescriptor) - 活跃的渗透者经常发推文并撰写有用的文章。
- [@garethheyes](https://twitter.com/garethheyes) - 英文网络渗透者。
- [@h3xstream](https://twitter.com/h3xstream/) - 安全研究员，对网络安全、加密、渗透测试、静态分析感兴趣，但最重要的是，Samy 是我的英雄。
- [@HackwithGitHub](https://twitter.com/HackwithGithub) - 主动向黑客和渗透测试人员展示开源黑客工具。
- [@hasegawayosuke](https://twitter.com/hasegawayosuke) - 日本javascript安全研究员。
- [@kinugawamasato](https://twitter.com/kinugawamasato) - 日本网络渗透者。
- [@XssPayloads](https://twitter.com/XssPayloads) - JavaScript 的仙境、意想不到的用法等等。
- [@shhnjk](https://twitter.com/shhnjk) - Web 和浏览器安全研究员。

## 实践

<a name="practices-application"></a>
### 应用

- [SELinux Game](http://selinuxgame.org/) - 通过实践来学习 SELinux。解决难题，展示技能 - 由 [@selinuxgame](https://twitter.com/selinuxgame) 撰写。
- [BadLibrary](https://github.com/SecureSkyTechnology/BadLibrary) - 用于训练的易受攻击的 Web 应用程序 - 由 [@SecureSkyTechnology](https://github.com/SecureSkyTechnology) 编写。
- [Hackxor](http://hackxor.net/) - 现实的 Web 应用程序黑客游戏 - 由 [@albinowax](https://twitter.com/albinowax) 编写。
- [OWASP Juice Shop](https://github.com/juice-shop/juice-shop) - 可能是最现代、最复杂的不安全 Web 应用程序 - 由 [@bkimminich](https://github.com/bkimminich) 和 [@owasp_juiceshop](https://twitter.com/owasp_juiceshop) 团队编写。
- [Portswigger Web Security Academy](https://portswigger.net/web-security) - 免费培训和实验室 - 由 [PortSwigger](https://portswigger.net/) 编写。
- [OopsSec Store](https://github.com/kOaDT/oss-oopssec-store) - 使用 Next.js 构建的故意易受攻击的电子商务应用程序 - 由 [@kOaDT](https://github.com/kOaDT) 编写。

<a name="practices-aws"></a>
### AWS

- [FLAWS](http://flaws.cloud/) - 亚马逊 AWS CTF 挑战 - 由 [@0xdabbad00](https://twitter.com/0xdabbad00) 撰写。
- [CloudGoat](https://github.com/RhinoSecurityLabs/cloudgoat) - Rhino Security Labs 的“Vulnerable by Design”AWS 基础设施设置工具 - 由 [@RhinoSecurityLabs](https://github.com/RhinoSecurityLabs) 编写。

<a name="practices-xss"></a>
### 跨站脚本攻击

- [alert(1) to win](https://alf.nu/alert1) - 系列 XSS 挑战 - 由 [@steike](https://twitter.com/steike) 撰写。
- [prompt(1) to win](http://prompt.ml/) - 2014 年夏季举行的复杂 16 级 XSS 挑战（+4 个隐藏级别）- 由 [@cure53](https://github.com/cure53) 编写。
- [XSS Challenges](http://xss-quiz.int21h.jp/) - XSS 挑战系列 - 由 yamagata21 撰写。
- [XSS game](https://xss-game.appspot.com/) - Google XSS 挑战 - 由 Google 编写。

<a name="practices-modsecurity"></a>
### ModSecurity / OWASP ModSecurity 核心规则集

- [ModSecurity / OWASP ModSecurity Core Rule Set](https://www.netnea.com/cms/apache-tutorials/) - 安装、配置和调整 ModSecurity 和核心规则集的系列教程 - 由 [@ChrFolini](https://twitter.com/ChrFolini) 编写。

## 社区

- [Reddit](https://www.reddit.com/r/websecurity/)
- [堆栈溢出](http://stackoverflow.com/questions/tagged/security)

## 杂项

- [A glimpse into GitHub's Bug Bounty workflow](https://githubengineering.com/githubs-bug-bounty-workflow/) - 由 [@gregose](https://github.com/gregose) 编写。
- [awesome-bug-bounty](https://github.com/djadmin/awesome-bug-bounty) - 可用的 Bug 赏金和披露计划以及 [@djadmin](https://github.com/djadmin) 撰写的文章的综合策划列表。
- [Brute Forcing Your Facebook Email and Phone Number](http://pwndizzle.blogspot.jp/2014/02/brute-forcing-your-facebook-email-and.html) - 由 [PwnDizzle](http://pwndizzle.blogspot.jp/) 撰写。
- [bug-bounty-reference](https://github.com/ngalongc/bug-bounty-reference) - 由 [@ngalongc](https://github.com/ngalongc) 按错误性质分类的错误赏金文章列表。
- [Cybersecurity Campaign Playbook](https://www.belfercenter.org/publication/cybersecurity-campaign-playbook) - 由[贝尔弗科学与国际事务中心](https://www.belfercenter.org/) 撰写。
- [EQGRP](https://github.com/x0rz/EQGRP) - 由 [@x0rz](https://github.com/x0rz) 解密 eqgrp-auction-file.tar.xz 的内容。
- [Google VRP and Unicorns](https://sites.google.com/site/bughunteruniversity/behind-the-scenes/presentations/google-vrp-and-unicorns) - 由 [Daniel Stelter-Gliese](https://www.linkedin.com/in/daniel-stelter-gliese-170a70a2/) 撰写。
- [Infosec_Reference](https://github.com/rmusser01/Infosec_Reference) - 不糟糕的信息安全参考 [@rmusser01](https://github.com/rmusser01)。
- [Internet of Things Scanner](http://iotscanner.bullguard.com/) - 通过 [BullGuard](https://www.bullguard.com/) 检查您家里的联网设备是否在 Shodan 上公开。
- [notes](https://github.com/ChALkeR/notes) - [@ChALkeR](https://github.com/ChALkeR) 的一些公开注释。
- [Pentest + Exploit dev Cheatsheet wallpaper](http://i.imgur.com/Mr9pvq9.jpg) - 渗透测试和利用开发备忘单。
- [The Definitive Security Data Science and Machine Learning Guide](http://www.covert.io/the-definitive-security-datascience-and-machinelearning-guide/) - 由杰森·特罗斯撰写。
- [$7.5k Google services mix-up](https://sites.google.com/site/testsitehacking/-7-5k-Google-services-mix-up) - 由 [Ezequiel Pereira](https://sites.google.com/site/testsitehacking/) 撰写。
- [The Bug Hunters Methodology v2.1](https://docs.google.com/presentation/d/1VpRT8dFyTaFpQa9jhehtmGaC7TqQniMSYbUdlHN6VrY/edit?usp=sharing) - 由 [@jhaddix](https://twitter.com/jhaddix) 撰写。
- [How I exploited ACME TLS-SNI-01 issuing Let's Encrypt SSL-certs for any domain using shared hosting](https://labs.detectify.com/2018/01/12/how-i-exploited-acme-tls-sni-01-issuing-lets-encrypt-ssl-certs-for-any-domain-using-shared-hosting/) - 由 [@fransrosen](https://twitter.com/fransrosen) 撰写。
- [TL:DR: VPN leaks users’ IPs via WebRTC. I’ve tested seventy VPN providers and 16 of them leaks users’ IPs via WebRTC (23%)](https://voidsec.com/vpn-leak/) - 由 [voidsec](https://voidsec.com/) 编写。
- [Be careful what you copy: Invisibly inserting usernames into text with Zero-Width Characters](https://medium.com/@umpox/be-careful-what-you-copy-invisibly-inserting-usernames-into-text-with-zero-width-characters-18b4e6f17b66) - 由 [@umpox](https://medium.com/@umpox) 撰写。
- [Escape and Evasion Egressing Restricted Networks](https://www.optiv.com/blog/escape-and-evasion-egressing-restricted-networks) - 作者：[克里斯·帕滕 (Chris Patten)、汤姆·斯蒂尔 (Tom Steele)](mailto:info@optiv.com)。
- [Domato Fuzzer's Generation Engine Internals](https://www.sigpwn.io/blog/2018/4/14/domato-fuzzers-generation-engine-internals) - 由 [sigpwn](https://www.sigpwn.io/) 编写。
- [CSS Is So Overpowered It Can Deanonymize Facebook Users](https://www.evonide.com/side-channel-attacking-browsers-through-css3-features/) - 由 [Ruslan Habalov](https://www.evonide.com/) 撰写。
- [Introduction to Web Application Security](https://www.slideshare.net/nragupathy/introduction-to-web-application-security-blackhoodie-us-2018) - 由 [@itsC0rg1](https://twitter.com/itsC0rg1)、[@jmkeads](https://twitter.com/jmkeads) 和 [@matir](https://twitter.com/matir) 撰写。
- [Finding The Real Origin IPs Hiding Behind CloudFlare or TOR](https://www.secjuice.com/finding-real-ips-of-origin-servers-behind-cloudflare-or-tor/) - 由 [Paul Dannewitz](https://www.secjuice.com/author/paul-dannewitz/) 撰写。
- [How I could have stolen your photos from Google - my first 3 bug bounty writeups](https://blog.avatao.com/How-I-could-steal-your-photos-from-Google/) - 由 [@gergoturcsanyi](https://twitter.com/gergoturcsanyi) 撰写。
- [An example why NAT is NOT security](https://0day.work/an-example-why-nat-is-not-security/) - 由 [@0daywork](https://twitter.com/@0daywork) 撰写。
- [Alexa Top 1 Million Security - Hacking the Big Ones](https://slashcrypto.org/data/itsecx2018.pdf) - 由 [@slashcrypto](https://twitter.com/slashcrypto) 撰写。
- [Hacking with a Heads Up Display](https://segment.com/blog/hacking-with-a-heads-up-display/) - 作者：[David Scrobonia](https://segment.com/blog/authors/david-scrobonia/)。
- [WEB APPLICATION PENETRATION TESTING NOTES](https://techvomit.net/web-application-penetration-testing-notes/) - 由 [Jayson](https://techvomit.net/) 撰写。
- [List of bug bounty writeups](https://pentester.land/list-of-bug-bounty-writeups.html) - 由 [Mariem](https://pentester.land/) 撰写。
- [The bug bounty program that changed my life](http://10degres.net/the-bug-bounty-program-that-changed-my-life/) - 由 [Gwen](http://10degres.net/) 撰写。
- [Why Facebook's api starts with a for loop](https://dev.to/antogarand/why-facebooks-api-starts-with-a-for-loop-1eob) - 由 [@AntoGarand](https://twitter.com/AntoGarand) 撰写。
- [Implications of Loading .NET Assemblies](https://threatvector.cylance.com/en_us/home/implications-of-loading-net-assemblies.html) - 由 [Brian Wallace](https://threatvector.cylance.com/en_us/contributors/brian-wallace.html) 撰写。
- [WCTF2019: Gyotaku The Flag](https://westerns.tokyo/wctf2019-gtf/wctf2019-gtf-slides.pdf) - 由 [@t0nk42](https://twitter.com/t0nk42) 撰写。
- [How we abused Slack's TURN servers to gain access to internal services](https://www.rtcsec.com/2020/04/01-slack-webrtc-turn-compromise/) - 由 [@sandrogauci](https://twitter.com/sandrogauci) 撰写。
- [DOS File Path Magic Tricks](https://medium.com/walmartlabs/dos-file-path-magic-tricks-5eda7a7a85fa) - 由 [@clr2of8](https://medium.com/@clr2of8) 撰写。
- [How I got my first big bounty payout with Tesla](https://medium.com/heck-the-packet/how-i-got-my-first-big-bounty-payout-with-tesla-8d28b520162d) - 由 [@cj.fairhead](https://medium.com/@cj.fairhead) 撰写。
- [Grokking Web Application Security](https://www.manning.com/books/grokking-web-application-security) - Malcolm McDonald（曼宁）对 Web 应用程序安全基础知识的实践介绍。
- [htb-writeups](https://github.com/momenbasel/htb-writeups) - 全面的 Hack The Box 文章集，涵盖 75 多个 Web 挑战，包括 XSS、SQLi、SSTI、SSRF 和反序列化，作者：[@momenbasel](https://github.com/momenbasel)。

## 行为准则

请注意，该项目是随[贡献者行为准则](code-of-conduct.md)一起发布的。参与该项目即表示您同意遵守其条款。

## 许可证

[![CC0](http://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

在法律允许的范围内，[@qazbnm456](https://qazbnm456.github.io/) 已放弃本作品的所有版权以及相关或邻接权。
