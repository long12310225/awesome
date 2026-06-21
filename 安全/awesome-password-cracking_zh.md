# 令人敬畏的密码破解  [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

在密码分析和计算机安全中，密码破解是从计算机系统中以加扰形式存储或传输的数据中恢复密码的过程。一种常见的方法（[暴力攻击](https://en.wikipedia.org/wiki/Brute-force_attack)）是反复尝试猜测密码，并根据可用的密码哈希进行检查。

这是 [@n0kovo@infosec.exchange](https://infosec.exchange/@n0kovo/?l) 精心整理的与密码破解和密码安全相关的出色工具、研究、论文和其他项目的列表。

在贡献之前请阅读 [CONTRIBUTING.md](https://github.com/narkopolo/awesome-password-cracking/blob/main/CONTRIBUTING.md)！简而言之：

- 列表按字母顺序排序
- 如果有疑问，请使用 [awesome-lint](https://github.com/sindresorhus/awesome-lint)
- 如果您认为某个项目不应该出现在此处 [打开问题](https://github.com/narkopolo/awesome-password-cracking/issues/new)

## 内容

- [令人敬畏的密码破解  ](#awesome-password-cracking--)
  - [Contents](#contents)
  - [Books](#books)
  - [Cloud](#cloud)
  - [Conversion](#conversion)
  - [Hashcat](#hashcat)
    - [Automation](#automation)
    - [分布式破解](#distributed-cracking)
    - [Rules](#rules)
    - [规则工具](#rule-tools)
    - [网络界面](#web-interfaces)
  - [开膛手约翰](#john-the-ripper)
  - [Misc](#misc)
    - [著名人物](#notable-people)
  - [Websites](#websites)
    - [Communities](#communities)
    - [查询服务](#lookup-services)
  - [单词表工具](#wordlist-tools)
    - [Analysis](#analysis)
    - [Generation/Manipulation](#generationmanipulation)
  - [Wordlists](#wordlists)
    - [语言特定](#laguage-specific)
    - [Other](#other)
  - [特定文件格式](#specific-file-formats)
    - [PDF](#pdf)
    - [JKS](#jks)
    - [ZIP](#zip)
  - [机器学习/人工智能](#machine-learning--ai)
  - [Research](#research)
    - [文章和博客文章](#articles-and-blog-posts)
    - [Papers](#papers)
    - [Talks](#talks)

## 书籍

- [Hash Crack: Password Cracking Manual (v3)](https://www.amazon.com/-/en/Joshua-Picolet/dp/1793458618) - 密码破解手册 v3 是密码恢复（破解）方法、工具和分析技术的扩展参考指南。

## 云

- [Cloud_crack](https://github.com/lordsaibat/Cloud_crack) - 使用 Terraform 和 AWS 破解密码。
- [Cloudcat](https://github.com/stormfleet/cloudcat) - 用于自动创建用于哈希破解的云基础设施的脚本。
- [Cloudstomp](https://github.com/Fmstrat/cloudstomp) - 通过插件以最低的价格在 EC2 上自动部署高 CPU/GPU 应用程序的实例。
- [Cloudtopolis](https://github.com/JoelGMSec/Cloudtopolis) - 该工具有助于在 Google Cloud Shell 平台上快速且完全无人值守地安装和配置 Hashtopolis（而且免费！）。
- [NPK](https://github.com/c6fc/npk) - NPK 是一个分布式哈希破解平台，完全由 AWS 中的无服务器组件构建，包括 Cognito、DynamoDB 和 S3。
- [Penglab](https://github.com/mxrch/penglab) - 滥用 Google Colab 来破解哈希值。
- [Rook](https://github.com/JumpsecLabs/Rook) - 自动创建 AWS p3 实例以用于基于 GPU 的密码破解。

## 转换

- [7z2hashcat](https://github.com/philsmd/7z2hashcat) - 从受密码保护的 .7z 档案（和 .sfx 文件）中提取信息，以便您可以使用 hashcat 破解这些“哈希值”。
- [MacinHash](https://github.com/jmagers/MacinHash) - 将 macOS plist 密码文件转换为哈希文件以供密码破解者使用。
- [NetNTLM-Hashcat](https://github.com/ins1gn1a/NetNTLM-Hashcat) - 将 John The Ripper/Cain 格式哈希（单个或批量）转换为 HashCat 兼容的哈希格式。
- [Rubeus-to-Hashcat](https://github.com/PwnDexter/Rubeus-to-Hashcat) - 将 Rubeus kerberoasting 输出转换/格式化为 hashcat 可读格式。
- [WINHELLO2hashcat](https://github.com/Banaanhangwagen/WINHELLO2hashcat) - 使用此工具，可以从 WINDOWS HELLO PIN 中提取“哈希值”。这个哈希值可以用 Hashcat 破解。
- [bitwarden2hashcat](https://github.com/0x6470/bitwarden2hashcat) - 一个将 Bitwarden 的数据转换为适合 hashcat 的哈希的工具。
- [hc\_to\_7z](https://github.com/philsmd/hc_to_7z) - 将 7-Zip hashcat 哈希值转换回 7z 存档。
- [hcxtools](https://github.com/ZerBea/hcxtools) - 用于将 cap/pcap/pcapng（gz 压缩）WiFi 转储文件转换为 hashcat 格式的便携式解决方案。
- [itunes_backup2hashcat](https://github.com/philsmd/itunes_backup2hashcat) - 从 Manifest.plist 文件中提取所需的信息，将其转换为与 hashcat 兼容的哈希值。
- [mongodb2hashcat](https://github.com/philsmd/mongodb2hashcat) - 将 MongoDB 数据库服务器中的哈希值提取为 hashcat 接受的哈希格式：-m 24100 (SCRAM-SHA-1) 或 -m 24200 (SCRAM-SHA-256)。

## 哈希猫

*[Hashcat](https://github.com/hashcat/hashcat) 是“世界上最快、最先进的密码恢复实用程序”。以下是与 Hashcat 以某种方式直接相关的项目。*

- [Autocrack](https://github.com/pry0cc/autocrack) - 一组用于自动和轻度自动破解哈希的客户端和服务器工具。
- [docker-hashcat](https://github.com/dizcza/docker-hashcat) - 适用于 Ubuntu 18.04 CUDA、OpenCL 和 POCL 的最新 hashcat docker。
- [Hashcat-Stuffs](https://github.com/xfox64x/Hashcat-Stuffs) - hashcat 列表和事物的集合。
- [hashcat-utils](https://github.com/hashcat/hashcat-utils/) - 对于高级密码破解很有用的小实用程序。
- [Hashfilter](https://github.com/bharshbarger/Hashfilter) - 读取 hashcat potfile 并将不同类型解析到 sqlite 数据库中。
- [known_hosts-hashcat](https://github.com/chris408/known_hosts-hashcat) - 使用 hashcat 破解 sshknown_hosts 文件的指南和工具。
- [pyhashcat](https://github.com/f0cker/pyhashcat) - Python C API 绑定到 libhashcat。

### 自动化

- [autocrack](https://github.com/timbo05sec/autocrack) - Hashcat 包装器可帮助自动化破解过程。
- [hat](https://github.com/sp00ks-git/hat) - 用于常见单词列表和规则的自动 Hashcat 工具，可加快在参与过程中破解哈希的过程。
- [hate_crack](https://github.com/trustedsec/hate_crack) - TrustedSec 团队通过 Hashcat 实现自动化破解方法的工具。
- [Naive hashcat](https://github.com/brannondorsey/naive-hashcat) - Naive hashcat 是一个即插即用的脚本，它预先配置了简单的、经过经验测试的、“足够好”的参数/攻击类型。

### 分布式破解

- [CrackLord](https://github.com/jmmcatee/cracklord) - 用于破解密码的队列和资源系统。
- [fitcrack](https://github.com/nesfit/fitcrack) - 一个基于hashcat的分布式密码破解系统。
- [Hashstation](https://github.com/hashstation/hashstation) - Hashstation是一个基于BOINC的分布式密码破解系统，内置Web界面。
- [Hashtopolis](https://github.com/hashtopolis/server) - 一个多平台客户端-服务器工具，用于将 hashcat 任务分发到多台计算机。
- [Kraken](https://github.com/arcaneiceman/kraken) - 多平台分布式暴力破解密码系统。

### 规则

- [clem9669 rules](https://github.com/clem9669/hashcat-rule) - hashcat 或 john 的规则。
- [hashcat rules collection](https://github.com/narkopolo/hashcat-rules-collection) - 可能是最大的 hashcat 规则集合。
- [Hob0Rules](https://github.com/praetorian-inc/Hob0Rules) - 基于统计和行业模式的 Hashcat 密码破解规则。
- [Kaonashi](https://github.com/kaonashi-passwords/Kaonashi) - Kaonashi 项目的词汇表、规则和掩码 (RootedCON 2019)。
- [nsa-rules](https://github.com/NSAKEY/nsa-rules) - 密码破解规则和从破解密码生成的 hashcat 掩码。
- [nyxgeek-rules](https://github.com/nyxgeek/nyxgeek-rules) - Hashcat 和 John the Ripper 的自定义密码破解规则。
- [OneRuleToRuleThemAll](https://github.com/NotSoSecure/password_cracking_rules) - “一条规则可以破解所有密码。或者至少我们希望如此。”
- [OneRuleToRuleThemStill](https://github.com/stealthsploit/OneRuleToRuleThemStill) - “我原来的 OneRuleToRuleThemAll hashcat 规则的改进和更新版本。”
- [pantagrule](https://github.com/rarecoil/pantagrule) - 从现实世界中泄露的密码生成的大型 hashcat 规则集。

### 规则工具

- [duprule](https://github.com/mhasbini/duprule) - 检测并过滤重复的 hashcat 规则。
- [ruleprocessorY](https://github.com/TheWorkingDeveloper/ruleprocessorY) - 具有复杂多字节字符支持的下一代规则处理器，旨在支持 Hashcat。

### 网络界面

- [crackerjack](https://github.com/ctxis/crackerjack) - CrackerJack 是用 Python 开发的 Hashcat Web GUI。
- [CrackQ](https://github.com/f0cker/crackq) - 一个Python Hashcat破解队列系统。
- [hashpass](https://github.com/dj-zombie/hashpass) - hashcat 的哈希破解 Web 应用程序和服务器。
- [Hashview](https://github.com/hashview/hashview) - 用于密码破解和分析的 Web 前端。
- [Wavecrack](https://github.com/wavestone-cdt/wavecrack) - Wavestone 的 Web 界面，用于使用 hashcat 破解密码。
- [WebHashCat](https://github.com/hegusung/WebHashcat) - WebHashcat 是一个非常简单但高效的 Web 界面的 hashcat 密码破解工具。

## 开膛手约翰

*[John the Ripper](https://github.com/openwall/john) 是“适用于许多操作系统的开源密码安全审核和密码恢复工具”。以下是与开膛手约翰以某种方式直接相关的项目。*

- [BitCracker](https://github.com/e-ago/bitcracker) - BitCracker 是第一个针对使用 BitLocker 加密的内存单元的开源密码破解工具。
- [johnny](https://github.com/openwall/johnny) - John the Ripper 的 GUI 前端。

## 杂项

- [Hashes](https://github.com/zefr0x/hashes) - 识别哈希算法（Name That Hash 的 GUI 前端）。
- [hashgen](https://github.com/cyclone-github/hashgen) - Hashgen 是一个简单但非常快速的 CLI 哈希生成器，用 Go 编写，并针对 Linux、Windows 和 Mac 进行交叉编译。
- [Name That Hash](https://github.com/HashPals/Name-That-Hash) - 不知道它是什么类型的哈希？ Name That Hash 将命名该哈希类型！识别 MD5、SHA256 和 300 多种其他哈希值。附带一个简洁的网络应用程序。

### 著名人物

- Alotdv - [Twitter](https://twitter.com/AlongExc)。
- Clem9669 - [GitHub](https://github.com/clem9669)。
- Coolbry95 - [GitHub](https://github.com/coolbry95) / [Twitter](https://twitter.com/coolbry95)。
- Dakykilla - [GitHub](https://github.com/dakykilla) / [Twitter](https://twitter.com/dakykilla)。
- Dropdeadfu - [GitHub](https://github.com/dropdeadfu) / [Twitter](https://twitter.com/dropdeadfu)。
- Epixoip - [GitHub](https://github.com/epixoip) / [Mastodon](https://infosec.exchange/@epixoip) / [Twitter](https://twitter.com/jmgosney)。
- Evilmog - [GitHub](https://github.com/evilmog/) / [Mastodon](https://infosec.exchange/@evilmog) / [Twitter](https://twitter.com/Evil_Mog)。
- Hydraze - [GitHub](https://github.com/Hydraze) / [Mastodon](https://infosec.exchange/@Hydraze) / [Twitter](https://twitter.com/Hydraze)。
- JakeWnuk - [GitHub](https://github.com/jakewnuk)。
- Kontrast23 - [GitHub](https://github.com/kontrast23) / [Twitter](https://twitter.com/marco_preuss)。
- M3g9tr0n - [GitHub](https://github.com/m3g9tr0n) / [Twitter](https://twitter.com/m3g9tr0n)。
- 矩阵 - [GitHub](https://github.com/matrix) / [Twitter](https://twitter.com/gm4tr1x)。
- Minga - [Twitter](https://twitter.com/mingadotcom)。
- N0kovo - [GitHub](https://github.com/n0kovo) / [Mastodon](https://infosec.exchange/@n0kovo) / [Twitter](https://twitter.com/n0kovos)。
- NSAKEY - [GitHub](https://github.com/NSAKEY) / [Twitter](https://twitter.com/_NSAKEY) / [网站](https://abigisp.com/)。
- NullMode - [GitHub](https://github.com/NullMode) / [Mastodon](https://infosec.exchange/@nullmode_@twtr.plus) / [Twitter](https://twitter.com/nullmode_)。
- Paule965 - [Twitter](https://twitter.com/paule965)。
- Philsmd - [GitHub](https://github.com/philsmd) / [Twitter](https://twitter.com/philsmd)。
- Roycewilliams - [GitHub](https://github.com/roycewilliams) / [Mastodon](https://infosec.exchange/@tychotithonus) / [Twitter](https://twitter.com/TychoTithonus)。
- RuraPenthe - [GitHub](https://github.com/bitcrackcyber) / [Mastodon](https://infosec.exchange/@rurapenthe) / [Twitter](https://twitter.com/RuraPenthe0)。
- S3in!c - [GitHub](https://github.com/s3inlc) / [Mastodon](https://infosec.exchange/@s3inlc) / [Twitter](https://twitter.com/s3inlc)。
- Tehnlulz - [GitHub](https://github.com/tehnlulz) / [Twitter](https://twitter.com/tehnlulz)。
- The_Mechanic - [GitHub](https://github.com/th3mechanic) / [Twitter](https://twitter.com/th3_m3chan1c)。
- ToXiC - [Twitter](https://twitter.com/yannistox)。
- 亡灵 - [GitHub](https://github.com/undeath)。
- Unix-ninja - [GitHub](https://github.com/unix-ninja) / [Mastodon](https://infosec.exchange/@unix_ninja@twitterbridge.jannis.rocks) / [Twitter](https://twitter.com/unix_ninja)。
- Xan - [GitHub](https://github.com/Xanadrel) / [Mastodon](https://infosec.exchange/@Xanadrel) / [Twitter](https://twitter.com/Xanadrel)。

## 网站

### 社区

- [hashcat Forum](https://hashcat.net/forum/) - 由 hashcat 开发者创建的论坛。
- [Hashmob](https://hashmob.net/) - 不断发展的密码恢复社区旨在成为密码学爱好者的协作中心。巨大的词汇表集合和查找服务。
- [Hashkiller Forum](https://forum.hashkiller.io/) - 拥有超过 20,000 名注册用户的密码破解论坛。

### 查询服务

- [CMD5](https://www.cmd5.org/) - 提供在线MD5/sha1/mysql/sha256加解密服务。
- [CrackStation](https://crackstation.net/) - 免费哈希查找服务还提供单词列表。
- [gohashmob](https://github.com/n0kovo/gohashmob) - Go CLI 应用程序使用 HashMob API 快速查找哈希值。
- [Hashes.com](https://hashes.com/) - 具有付费功能的哈希查找服务。
- [Hashkiller](https://hashkiller.io/) - 带有论坛的哈希查找服务。
- [Online Hash Crack](https://www.onlinehashcrack.com/) - 云密码恢复服务。

## 单词表工具

*用于分析、生成和操作单词列表的工具。*

### 分析

- [PACK](https://github.com/iphelix/pack) - 开发的一组实用程序，用于帮助分析密码列表，以便通过掩码、规则、字符集和其他密码特征的模式检测来增强密码破解。
- [password-smelter](https://github.com/TheTechromancer/password-smelter) - 从 hashcat 等获取密码并输出为 HTML、Markdown、XLSX、PNG、JSON。支持深色和浅色主题。赞美密码扩展器。
- [password-stretcher](https://github.com/thetechromancer/password-stretcher) - 从网站、文件或标准输入生成“数量令人作呕”的密码。赞美密码熔炉。
- [pcfg_cracker](https://github.com/lakiw/pcfg_cracker) - 该项目使用机器学习来识别用户的密码创建习惯。
- [Pipal](https://github.com/digininja/pipal) - 密码分析器。
- [Graphcat](https://github.com/Orange-Cyberdefense/graphcat) - 根据密码破解结果生成图表。

### 生成/操纵

- [accent_permutator](https://github.com/cyclone-github/accent_permutator) - 一种将字符从 ASCII / UTF-8 转换为重音字符（例如“o”到“ò”）的工具。
- [anew](https://github.com/tomnomnom/anew) - 将标准输入中的行追加到文件中，但前提是它们尚未出现在文件中。也将新行输出到标准输出，使其有点像删除重复项的 tee -a 。
- [bopscrk](https://github.com/r3nt0n/bopscrk) - 为有针对性的攻击生成智能且强大的单词列表。包括歌词获取和不同的转换。
- [common-substr](https://github.com/sensepost/common-substr) - 从输入文本中提取最常见的子字符串的简单工具。专为密码破解而设计。
- [Crunch](https://sourceforge.net/projects/crunch-wordlist/) - Crunch 是一个单词列表生成器，您可以在其中指定标准字符集或您指定的字符集。 Crunch 可以生成所有可能的组合和排列。
- [CUPP](https://github.com/Mebus/cupp) - 该工具可让您根据用户分析数据（例如生日、昵称、地址、宠物或亲戚的名字等）生成单词列表。
- [duplicut](https://github.com/nil0x42/duplicut) - 从海量单词列表中删除重复项，而不对其进行排序（用于基于字典的密码破解）。
- [Gorilla](https://github.com/d4rckh/gorilla) - 用于生成单词列表或使用突变扩展现有单词列表的工具。
- [Gramify](https://github.com/TheWorkingDeveloper/gramify) - 根据单词、字符或字符集创建 n 元词列表，以用于离线密码攻击和数据分析。
- [Elpscrk](https://github.com/D4Vinci/elpscrk) - Elpscrk 与 cupp 类似，但它基于排列和统计，同时具有内存效率。
- [Keyboard-Walk-Generators](https://github.com/Rich5/Keyboard-Walk-Generators) - 生成用于破解的键盘步行词典。
- [kwprocessor](https://github.com/hashcat/kwprocessor) - 高级键盘行走生成器，具有可配置的基本字符、键盘映射和路线。
- [maskprocessor](https://github.com/hashcat/maskprocessor/) - 具有每个位置可配置字符集的高性能字生成器。
- [maskuni](https://github.com/flbdx/maskuni) - 一个独立的快速单词生成器，秉承 hashcat 掩码生成器的精神，支持 unicode。
- [Mentalist](https://github.com/sc0tfree/mentalist) - Mentalist 是一个用于生成自定义单词列表的图形工具。它利用常见的人类范例来构造密码，并可以输出完整的单词列表以及与 Hashcat 和 John the Ripper 兼容的规则。
- [PTT](https://github.com/JakeWnuk/ptt) - 密码转换工具 (ptt) 是一款专为密码破解而设计的多功能实用程序。它有助于创建自定义规则和转换，以及生成单词列表。该工具支持处理来自文件、URL 和标准输入的数据，简化破解工作流程。
- [Phraser](https://github.com/Sparell/Phraser) - Phraser 是一个短语生成器，使用 n 元语法和马尔可夫链来生成用于密码破解的短语。
- [princeprocessor](https://github.com/hashcat/princeprocessor) - 使用 PRINCE 算法的独立密码候选生成器。
- [Rephraser](https://github.com/travco/rephraser) - 基于 Python 的 Phraser 重新构想，使用马尔可夫链进行语言正确的密码破解。
- [Rling](https://github.com/Cynosureprime/rling) - RLI Next Gen (Rling) 是 hashcat 实用程序中 rli 的更快、功能丰富的替代品。
- [statsprocessor](https://github.com/hashcat/statsprocessor/) - 基于每位置马尔可夫链的单词生成器。
- [StringZilla](https://github.com/ashvardanian/StringZilla) - Python 和 C 中长字符串和多 GB 文件的最快字符串排序、搜索、拆分和洗牌。
- [TTPassGen](https://github.com/tp7309/TTPassGen) - 灵活且可编写脚本的密码字典生成器，支持暴力破解、组合、复杂规则模式等。
- [token-reverser](https://github.com/dariusztytko/token-reverser) - 用于破解安全令牌的单词列表生成器。
- [WikiRaider](https://github.com/NorthwaveSecurity/wikiraider) - WikiRaider 使您能够根据维基百科的国家特定数据库生成单词列表。

## 单词表

### 语言特定

- [Albanian wordlist](https://github.com/its0x08/albanian-wordlist) - 名字、姓氏和一些阿尔巴尼亚文献的混合。
- [Danish Phone Wordlist Generator](https://github.com/narkopolo/danish_phone_wordlist_generator) - 该工具可以按地区和/或用途（手机、固定电话等）生成丹麦电话号码的单词列表，可用于密码破解或模糊丹麦目标。
- [Danish Wordlists](https://github.com/narkopolo/danish-wordlists) - 用于破解丹麦语密码的丹麦语单词列表集合。
- [French Wordlists](https://github.com/clem9669/wordlists) - 该项目旨在提供有关人们可以用作基本密码的所有内容的法语单词列表。

### 其他

- [Packet Storm Wordlists](https://packetstormsecurity.com/Crackers/wordlists/page1/) - 多种语言的不同单词列表的大量集合。
- [Rocktastic](https://labs.nettitude.com/tools/rocktastic/) - 包括在野外观察到的许多密码和模式的排列。
- [RockYou2021](https://github.com/ohmybahgosh/RockYou2021.txt) - RockYou2021.txt 是一个由各种其他单词列表编译而成的海量单词列表。
- [WeakPass](https://weakpass.com/) - 大型词汇表的集合。

## 特定文件格式

### PDF

- [pdfrip](https://github.com/mufeedvh/pdfrip) - 多线程 PDF 密码破解实用程序，配备常见的密码格式生成器和字典攻击。

### 健康

- [JKS private key cracker](https://github.com/floyd-fuh/JKS-private-key-cracker-hashcat) - 破解 JKS 文件中私钥条目的密码。

### 邮政编码

- [bkcrack](https://github.com/kimci86/bkcrack) - 使用 Biham 和 Kocher 已知的明文攻击破解传统的 zip 加密。
- [frackzip](https://github.com/hyc/fcrackzip) - 用于破解加密 ZIP 档案的小工具。

## 机器学习/人工智能

- [adams](https://github.com/TheAdamProject/adams) - 通过深度学习和动态字典减少现实世界密码强度建模中的偏差。
- [neural network cracking](https://github.com/cupslab/neural_network_cracking) - 使用神经网络破解密码的代码。
- [RNN-Passwords](https://github.com/gehaxelt/RNN-Passwords) - 使用 char-rnn 来学习和猜测密码。
- [rulesfinder](https://github.com/synacktiv/rulesfinder) - 该工具可以为给定的字典和密码列表找到有效的密码修改规则（对于 John the Ripper 或 Hashcat）。
- [PassGPT](https://github.com/javirandor/passgpt) - PassGPT 是一个针对密码泄露从头开始训练的 GPT-2 模型。
- [SePass: Semantic Password Guessing using k-nn Similarity Search in Word Embeddings](https://github.com/Knuust/SePass) - 一种密码猜测方法，利用词嵌入来发现和利用密码列表中的语义相关性。

## 研究

### 文章和博客文章

- [使用掩码优化单词列表](https://jakewnuk.com/posts/optimizing-wordlists-w-masks/)
- [紫雨攻击 - 随机生成密码破解](https://www.netmux.com/blog/purple-rain-attack)
- [通过代币交换攻击破坏哈希值](https://jakewnuk.com/posts/token-swapping-attack/)
- [Bcrypt 25 周年：密码安全回顾](https://www.usenix.org/publications/loginonline/bcrypt-25-retrospective-password-security)

### 论文

- [PassGPT：使用法学硕士进行密码建模和（引导）生成](https://arxiv.org/abs/2306.01545)
- [使用概率上下文无关语法破解密码 (2009)](https://www.researchgate.net/publication/220713709_Password_Cracking_Using_Probabilistic_Context-Free_Grammars)
- [快速、精简且准确：使用神经网络对密码可猜测性进行建模 (2016)](https://www.usenix.org/conference/usenixsecurity16/technical-sessions/presentation/melicher)
- [PassGAN：密码猜测的深度学习方法 (2017)](https://arxiv.org/pdf/1709.00440)
- [GENPass：使用 PCFG 规则和对抗性生成进行密码猜测的通用深度学习模型 (2018)](https://ieeexplore.ieee.org/document/8422243)
- [使用相对论 GAN 生成优化的猜测候选者，以实现更好的多词典密码破解 (2020)](https://www.mdpi.com/2076-3417/10/20/7306/htm)
- [通过深度学习和动态字典减少现实世界密码强度建模中的偏差 (2020)](https://arxiv.org/abs/2010.12269)
- [PassFlow：使用生成流猜测密码 (2021)](https://arxiv.org/abs/2105.06165)
- [GNPassGAN：改进的生成对抗网络，用于离线密码猜测（2022）](https://arxiv.org/pdf/2208.06943)
- [密码破解者的复仇：密码破解工具的自动化训练（2022）](https://doi.org/10.1007/978-3-031-17146-8_16)
- [密码猜测任务的系统回顾（2023）](https://doi.org/10.3390/e25091303)
- [更难、更好、更快、更强：优化基于上下文的密码破解字典的性能 (2023)](https://doi.org/10.1016/j.fsidi.2023.301507)
- [自信的蒙特卡罗：概率密码模型猜测曲线的严格分析（2023）](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=10179365)
- [通过双向变压器改善现实世界的密码猜测攻击 (2023)](https://www.usenix.org/conference/usenixsecurity23/presentation/xu-ming)
- [使用基于密度的集群生成密码猜测的修改规则 (2023)](https://annas-archive.pk/scidb/10.1109/tdsc.2022.3217002/)
- [没有单一灵丹妙药：测量密码强度计的准确性 (2023)](https://www.usenix.org/system/files/usenixsecurity23-wang-ding-silver-bullet.pdf)
- [优化密码哈希计算 (2023)](https://helda.helsinki.fi/server/api/core/bitstreams/23a37f74-a162-4473-b894-5da77f0627d1/content)
- [PGTCN：一种基于时间卷积网络的新型密码猜测模型（2023）](https://annas-archive.pk/scidb/10.1016/j.jnca.2023.103592/)
- [对经验密码数据集进行严格的统计分析 (2023)](https://ieeexplore.ieee.org/document/10179431)
- [通过逻辑门使用二进制随机化增强密码哈希的抵抗力 (2024)](http://doi.org/10.11591/ijece.v14i5.pp5400-5407)
- [GuessFuse：多视图混合密码猜测 (2024)](https://ieeexplore.ieee.org/document/10466588)
- [PassRVAE：通过循环变分自动编码器改进拖网攻击（2024）](https://dl.acm.org/doi/10.1145/3673277.3673295)
- [Prob-Hashcat：使用 Hashcat 将概率密码猜测加速数百倍（2024 年）](https://dl.acm.org/doi/epdf/10.1145/3678890.3678919)
- [使用布隆过滤器加强网络安全：提高密码破解效率的新方法 (2024)](https://doi.org/10.1186/s13635-024-00183-2)
- [超越字典攻击：通过机器学习引发的篡改规则提高密码破解效率 (2025)](https://doi.org/10.1016/j.fsidi.2025.301865)
- [MAYA：通过统一基准解决生成密码猜测中的不一致问题 (2025)](https://arxiv.org/abs/2504.16651)
- [使用大型语言模型猜测密码 (2025)](https://www.usenix.org/system/files/usenixsecurity25-zou-yunkai.pdf)
- [PassRecover：用于端到端离线密码恢复加速的多 FPGA 系统 (2025)](https://doi.org/10.3390/electronics14071415)
- [当情报失败时：关于法学硕士为何难以破解密码的实证研究 (2025)](https://arxiv.org/abs/2510.17884)
- [仅用一个字符即可使成功率翻倍：掩码密码猜测 (2025)](https://doi.org/10.14722/ndss.2026.241059)
- [PGMaP：基于掩码预测的密码生成（2026）](https://linkinghub.elsevier.com/retrieve/pii/S0957417426002319)
- [使用个人身份信息和旧密码改进有针对性的密码猜测攻击（2026）](https://doi.org/10.1186/s42400-025-00430-0)

### 会谈

- [BSides 开曼群岛 2024 - 无上限破解：改进离线哈希恢复方法](https://jakewnuk.com/static/No%20Cap%20Cracking%20Improving%20Offline%20Hash%20Recovery%20Methodologies.pdf)
- [BSides 开曼群岛 2023 - 利用泄露数据升级密码攻击](https://jakewnuk.com/static/Leveling%20Up%20Password%20Attacks%20with%20Breach%20Data.pdf)
- [DEF CON 安全模式密码村 - Hashcat 入门](https://www.youtube.com/watch?v=MBTJ8f6Fsmg)
- [DEF CON 安全模式密码村 - Jeremi Gosney - 大规模破解](https://www.youtube.com/watch?v=4Ell1Tt23NI)
- [DEF CON 28 安全模式密码村 – “让我们在不使用 rockyou txt 的情况下破解 RockYou”](https://www.youtube.com/watch?v=8FtXntEsZdU)
- [SecTor 2019 - Will Hunt - 散列，散列无处不在，但我看到的只是明文](https://sector.ca/sessions/hashes-hashes-everywhere-but-all-i-see-is-plaintext/)
- [DefCamp 定制的、机器学习驱动的密码猜测攻击和缓解措施](https://www.youtube.com/watch?v=iK6ZbD6v9Gg)
- [UNHash - 更好的密码破解方法](https://media.ccc.de/v/31c3_-_5966_-_en_-_saal_1_-_201412292245_-_unhash_-_methods_for_better_password_cracking_-_tonimir_kisasondi)
- [USENIX Security '23 - 没有单一银弹：测量密码强度计的准确性](https://www.youtube.com/watch?v=0vhoAaqGYV8)
- [USENIX Security '23 - 通过双向变压器改善现实世界的密码猜测攻击](https://www.youtube.com/watch?v=kE7dEUcPtU0)
- [USENIX Security '21 - 通过深度学习和动态字典减少真实世界密码强度建模中的偏差](https://www.youtube.com/watch?v=Jvp3UTdCeag)
- [USENIX Security '16 - 快速、精简且准确：使用神经网络对密码可猜测性进行建模](https://www.youtube.com/watch?v=GgaZ_LxsL_8)
