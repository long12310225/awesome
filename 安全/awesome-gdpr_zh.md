# 很棒的 GDPR [![Awesome](https://awesome.re/badge-flat.svg)](https://awesome.re)

[<img src="GDPR.png"align="right"width="300">](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32016R0679)

《通用数据保护条例》(GDPR) 是针对欧盟和欧洲经济区内所有个人的数据保护和隐私的法规。该规定加大了企业对隐私的关注，增强了数据主体的影响力。

## 内容
* [法律文本](#legal-text)
* [Guidelines](#Guidelines)
* [数据主体的权利（第 12 - 23 条）](#rights-of-the-data-subject-art-12---23)
* [隐私设计 - 开发者指南（第 25 条）](#privacy-by-design---guides-for-developers-art-25)
* [处理记录（第 30 条）](#records-of-processing-art-30)
* [安全（第 32 条）](#security-art-32)
* [事件管理（第三十三条和第三十四条）](#incident-management-art-33-and-34)
* [数据保护影响评估（DPIA，第 35 条）](#data-protection-impact-assessments-dpia-art-35)
* [Tools](#tools)
* [数据保护机构](#data-protection-authorities-art-51--59)
* [组织/项目](#organisations--projects)
* [Publications](#Publications)
* [Related](#Related)

## 法律文本
* [GDPR (2016/679)](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32016R0679&from=EN) - GDPR 官方版本。
* [GDPR-info](https://gdpr-info.eu/) - GDPR 链接到序言中的相关文章和部分（非官方网站）。
* [GDPR-expert](https://www.gdpr-expert.com/home.html?mid=5) - 比较法规、指令和国家立法。链接到序言中的相关部分（非官方网站）。
* [GDPRhub -> GDPR Articles](https://gdprhub.eu/index.php?title=Category:GDPR_Articles) - GDPR 文章包含评论。
  
## 指南
* 来自欧洲数据保护委员会 (EDPB) 的[指南](https://edpb.europa.eu/our-work-tools/general-guidance/gdpr-guidelines-recommendations-best-practices_en) 和[意见](https://edpb.europa.eu/our-work-tools/consistency-findings/opinions_en)。
* [ICO：GDPR 指南](https://ico.org.uk/for-organisations/guide-to-data-protection/guide-to-the-general-data-protection-regulation-gdpr/)
* [Handbook on European data protection law ](https://publications.europa.eu/en/publication-detail/-/publication/5b0cfa83-63f3-11e8-ab9c-01aa75ed71a1) - 欧盟发布的手册。
* [Factsheets](https://edps.europa.eu/data-protection/our-work/our-work-by-type/factsheets_en) - 欧盟数据保护主管的情况说明书。
  
## 数据主体的权利（第 12 - 23 条）
* [开源隐私声明模板（Juro）](https://github.com/juro-privacy/free-privacy-notice)

## 隐私设计 - 开发者指南（第 25 条）
* [CNIL - GDPR 开发人员指南](https://github.com/LINCnil/GDPR-Developer-Guide)
* [挪威 DPA - 通过设计和默认进行数据保护的软件开发](https://www.datatilsynet.no/en/about-privacy/virksomhetenes-plikter/data-protection-by-design-and-by-default/)
* [Data Pseudonymisation: Advanced Techniques and Use Cases](https://www.enisa.europa.eu/publications/data-pseudonymisation-advanced-techniques-and-use-cases/) - ENISA 的假名技术报告。
* [匿名化、假名化和隐私增强技术指南 - ICO](https://ico.org.uk/about-the-ico/ico-and-stakeholder-consultations/ico-call-for-views-anonymisation-pseudonymisation-and-privacy-enhancing-technologies-guidance/)
* [dstack](https://github.com/Dstack-TEE/dstack) - 开源机密计算框架通过硬件强制隔离来实现隐私设计，以实现符合 GDPR 的数据处理。

## 处理记录（第 30 条）
* [Iubenda - 数据处理活动登记册](https://www.iubenda.com/en/internal-privacy-management)

## 安全（第 32 条）
* [OWASP Top 10](https://owasp.org/www-project-top-ten/) - 十大 Web 应用程序安全风险。
* [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/) - 有关特定应用程序安全主题的高价值信息的简明集合。
* [匿名化、假名化和隐私增强技术指南](https://ico.org.uk/about-the-ico/ico-and-stakeholder-consultations/ico-call-for-views-anonymisation-pseudonymisation-and-privacy-enhancing-technologies-guidance/)

## 事件管理（第三十三条和第三十四条）
* [ENISA：个人数据泄露严重程度评估方法的建议](https://www.enisa.europa.eu/publications/dbn-severity)
* [Google、SRE：管理事件](https://landing.google.com/sre/sre-book/chapters/managing-incidents/)
* [Troy Hunt：数据泄露披露 101](https://www.troyhunt.com/data-breach-disclosure-101-how-to-succeed-after-youve-failed/)
* [出色的事件响应](https://github.com/meirwah/awesome-incident-response)
* [GDPR Enforcement Tracker](http://www.enforcementtracker.com/) - 罚款和处罚概述。

## 数据保护影响评估（DPIA，第 35 条）
* [来自法国 DPA 的开源 DPIA 软件](https://www.cnil.fr/en/open-source-pia-software-helps-carry-out-data-protection-impact-assesment)
* [数据保护影响评估指南（WP29）](https://ec.europa.eu/newsroom/article29/item-detail.cfm?item_id=611236)
* [ISO 标准：隐私影响评估指南](https://www.iso.org/standard/86012.html)
* [来自 ICO 的 DPIA 模板](https://iapp.org/resources/article/sample-dpia-template/)
* [Public DPIA Teams OneDrive SharePoint and Azure AD](https://www.rijksoverheid.nl/documenten/publicaties/2022/02/21/public-dpia-teams-onedrive-sharepoint-and-azure-ad) - Microsoft Teams 的 DPIA 与 OneDrive、SharePoint Online 和 Azure Active Directory 相结合。

## 工具
* [Website Evidence Collector (WEC)](https://www.edps.europa.eu/edps-inspection-software_en) - EDPS 检测软件。
* [Data protection around the world](https://www.cnil.fr/en/data-protection-around-the-world) - (CNIL) 每个国家的数据保护水平地图。
* [Data Protection Laws of the world](https://www.dlapiperdataprotection.com/) - (DLA Piper) 比较世界各地的数据保护法律。
* [Comparison of Consent Management Platforms](https://github.com/JermainKroot/best-consent-management-platforms) - 9个平台的实际比较。

## 数据保护机构（第 51 -59 条）
* [European Data Protection Board](https://edpb.europa.eu/) - EDPB。
* [European Data Protection Supervisor](https://edps.europa.eu/) - 电子数据处理系统。
* [European Union Agency for Network and Information Security (ENISA)](https://www.enisa.europa.eu/topics/data-protection) - ENISA。
* [数据保护机构名单](https://pdpecho.com/the-list/)
  
## 组织/项目
* [Electronic Frontier Foundation](https://www.eff.org/) - 捍卫数字隐私、言论自由和创新的非营利组织。
* [International Association of Privacy Professionals](https://iapp.org/) - 隐私专业人士的资源。
* [Privacy International](https://www.privacyinternational.org) - 慈善事业对那些想要了解个人、团体和整个社会一切的政府和公司提出了挑战。
* [NOYB](https://noyb.eu/) - 提请 DPA 注意重要问题、在民事法庭执行法律或直接与公司接触的组织。
* [GDPR.eu](https://gdpr.eu/) - 研究 GDPR 的组织和个人的资源（非官方网站）。
* [CyLab Usable Privacy and Security Laboratory](https://cups.cs.cmu.edu/) - 与理解和提高隐私和安全的可用性相关的研究。
* [EPIC](https://epic.org/) - 电子隐私信息中心。
* [Future of Privacy Forum](https://fpf.org/) - 隐私领导力和学术的催化剂，推进有原则的数据实践以支持新兴技术。
* [W3C Privacy Interest Group](https://www.w3.org/Privacy/) - 引领网络充分发挥潜力。
* [CISPE Code of Conduct](https://www.codeofconduct.cloud/) - 第 40 条规定的云基础设施服务提供商的泛欧行业特定代码。

## 刊物
* [GDPR Today](https://www.gdprtoday.org/) - 来自开放权利组织的隐私新闻。
* [Spread Privacy](https://spreadprivacy.com/) - DuckDuckGo 博客。
* [Freedom To Tinker](https://freedom-to-tinker.com/) - 来自普林斯顿大学 CITP 的博客，CITP 是一个研究公共生活中数字技术的研究中心。
* [pdpEcho](https://pdpecho.com/) - 关于个人数据保护和隐私的所有内容，作者：Gabriela Zanfir-Fortuna。
* [GDPRhub](https://gdprhub.eu/) - 免费开放的 wiki，允许任何人在整个欧洲查找和分享 GDPR 见解。
    
## 相关
* [尊重隐私](https://github.com/nikitavoloboev/privacy-respecting)
* [很棒：安全](https://github.com/sindresorhus/awesome#security)
* [太棒了：人性化的技术](https://github.com/humanetech-community/awesome-humane-tech#readme)
* [Awesome: Privacy](https://github.com/pluja/awesome-privacy#readme) - 免费、开源和尊重隐私的服务以及私有服务替代方案的列表。
* [HIPAA 合规性开发人员指南](https://github.com/truevault/hipaa-compliance-developers-guide)
* [没有 cookie 的分析](https://www.gocookieless.com/)
* [欧洲网络分析服务](https://european-alternatives.eu/category/web-analytics-services)
* [欧盟替代方案](https://dasprive.be/eu-alternatives/)

## 许可证
[![CC0](http://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

在法律允许的范围内，Oppoverbakke 放弃了本作品的所有版权以及相关或邻接权。
