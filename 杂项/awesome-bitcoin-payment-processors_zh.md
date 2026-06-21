<div align="center">
<img width="500" src="media/logo.svg" alt="Awesome Bitcoin Payment Processors"/>
</div>

# 很棒的比特币支付处理器 [![Awesome](https://awesome.re/badge-flat.svg)](https://awesome.re)

精选的比特币支付处理器列表，使商家、企业和非营利组织能够接受比特币支付。

## 内容

- [自托管比特币支付处理器](#self-hosted-bitcoin-payment-processors)
- [托管比特币支付处理器](#hosted-bitcoin-payment-processors)
  - [Non-Custodial](#non-custodial)
  - [Custodial](#custodial)
- [支持者💝](#backers-)

## 自托管比特币支付处理器

自托管支付处理器在您的服务器上运行，让您可以完全控制整个支付流程和资金。没有第三方参与——这显着提高了您和您的客户的审查阻力、隐私和安全性。

|处理器|费用|闪电|直接存入您的钱包 |转换为菲亚特 |要求|
| --------- |:----:|:---------:|:-----------------------:|:------------------:| ------------ |
| [BTCPay服务器](https://btcpayserver.org/) |不收费 |是的 |是的 |通过 [Strike 插件](https://github.com/Marfusios/strike-btcpayserver-plugin) 或 [Exchange 集成](https://redbtc.org/flows/integrations/kraken-exchange/) | 2 GB RAM、80 GB 存储、Docker |
| [一次性地址](https://github.com/alexk111/One-Time-Address) |不收费 |没有 |是的 |没有 | NodeJS |
| [CryptoWoo](https://www.cryptowoo.com/) |每年 $34 - $99 |没有 |是的 |没有 | PHP 5.6+、Wordpress 4.3+、WooCommerce 3.0+ |
| [BitcartCC](https://bitcartcc.com) |不收费 |是的 |是的 |没有 | 1 GB RAM、10 GB 存储、Docker |
| [LnMe](https://github.com/bumi/lnme) |不收费 |是的 |是的 |没有 | LND节点|
| [SatSale](https://github.com/SatSale/SatSale) |不收费 |是的 |是的 |弱点：[在 Liquid 上兑换为 USDT](https://github.com/SatSale/SatSale/blob/471c8c03bbc269df1f322f6484b6e7a7364e5b34/config.toml#L101)，无 KYC | Python。比特币节点、闪电节点和 WooCommerce 可选。 |
| [Keagate](https://github.com/dilan-dio4/Keagate) |不收费 |没有 |是的 |没有 | 1 GB 内存，Unix |
| [LNURL 守护进程](https://github.com/yanascz/lnurld) |不收费 |是的 |是的 |没有 | LND节点|

## 托管比特币支付处理器

托管支付处理器在其他人的服务器上运行。这简化了初始设置过程，但减少了您对付款过程的控制量。

### 非托管

这些处理器使用您的钱包来接收付款。

|处理器|费用|闪电|直接存入您的钱包 |转换为菲亚特 |要求|
| --------- |:----:|:---------:|:-----------------------:|:------------------:| ------------ |
| [Blockonomics](https://www.blockonomics.co/merchants) | 1% |没有 |是的 |通过[付款转发](https://www.blockonomics.co/views/ payment_forwarding.html) |没有 |
| [Payscrypt](https://payscrypt.com/) |不收费 |没有 |是的 |没有 |没有 |
| [Bitrequest](https://bitrequest.io/) |不收费 |是的 |是的 |没有 |没有 |
| [Zaprite](https://zaprite.com/) |每月 25 美元 |是的 |是的 |没有 |没有 |
| [付款](https:// paymento.io/) | 0.5% |没有 |是的 |没有 |没有 |
| [Flash](https://paywithflash.com/) | 1.5% |是的 |是的 |没有 |没有 |

### 保管

以下处理者使用他们自己的钱包（而不是您的）来接收付款。

⚠ 他们不仅收集有关付款的数据，还完全控制资金。托管人存在许多风险，最终可能会导致资金丢失/被锁定。

⚠ 其中大多数都有 KYB/KYC/AML 要求，这对您和您客户的隐私构成严重威胁。

⚠ 他们对商家和商家的客户有基于国家/地区的限制。

|处理器|费用|闪电|直接存入您的钱包 |转换为菲亚特 |要求|
| --------- |:----:|:---------:|:-----------------------:|:------------------:| ------------ |
| [确认](https://confirmo.net/) | 1.3%（0.8% 发票 + 0.5% 付款）|是的 |没有 |是的 |有关业务/网站的信息。可能需要某些文件。 |
| [CoinGate](https://coingate.com/accept) | 1%（商户）+一些[可变服务费](https://support.coingate.com/en/109/why-does-coingate-charge-service-fee)（客户） |是的 |没有 |是的 |需要【大量信息和商业文件】(https://blog.coingate.com/2019/05/verify-merchant-account-faq)，官方翻译为英文。 |
| [CoinPayments](https://www.coin payments.net/) | 0.5% |是的 |没有 |没有 |提款时可能需要提供多种形式的身份证明，并需要结清任何未结金额。 |
| [OpenNode](https://www.opennode.co/) | 1% |是的 |没有 |是的 |需要 [KYC/KYB 文件](https://help.opennode.com/en/articles/3654899-kyc-and-kyb-requirements) |
| [罢工](https://strike.me/business/) | 1% |仅|没有 |没有 |需要[基本商业信息、文件、所有者和经营者的身份验证](https://strike.me/faq/how-do-i-sign-up-for-a-strike-business-account/)。 |
| [Coinremitter](https://coinremitter.com/) | 0.23% + 0.0001 |没有 |没有 |没有 |没有 |
| [Utrust](https://utrust.com/) | 1% |没有 |没有 |是的 |需要某些文件。 |
| [NOWPayments](https://now payments.io/) | ≤0.5% |没有 |没有 |没有 | KYC/AML 程序适用于某些客户、钱包地址和选定资产。 |
| [ElenPAY](https://elenpay.tech) | ≤1% |是的 |是的 |不（很快）|低 KYC |
| [速度](https://tryspeed.com/) | 1% |是的 |没有 |没有 |没有 |
| [Sheepy](https://www.sheepy.com/) | 1% + 0.25 美元 |没有 |没有 |是的 |需要 [KYB 文件](https://www.sheepy.com/faq/what-documents-are-required-to-verify-my-merchant-account) |
| [ALFAcoins](https://www.alfacoins.com/) | 0.99% |没有 |没有 |没有 |需要 KYB 文件 |
| [Apiron](https://apirone.com/) | 1% |没有 |没有 |没有 |没有 |

## 支持者💝

[![Backer](https://mynode.alexkaul.com/gh-backer/top/0/avatar/60)](https://mynode.alexkaul.com/gh-backer/top/0/profile)
[![Backer](https://mynode.alexkaul.com/gh-backer/top/1/avatar/60)](https://mynode.alexkaul.com/gh-backer/top/1/profile)
[![Backer](https://mynode.alexkaul.com/gh-backer/top/2/avatar/60)](https://mynode.alexkaul.com/gh-backer/top/2/profile)
[![Backer](https://mynode.alexkaul.com/gh-backer/top/3/avatar/60)](https://mynode.alexkaul.com/gh-backer/top/3/profile)
[![Backer](https://mynode.alexkaul.com/gh-backer/top/4/avatar/60)](https://mynode.alexkaul.com/gh-backer/top/4/profile)
[![Backer](https://mynode.alexkaul.com/gh-backer/top/5/avatar/60)](https://mynode.alexkaul.com/gh-backer/top/5/profile)
[![Backer](https://mynode.alexkaul.com/gh-backer/top/6/avatar/60)](https://mynode.alexkaul.com/gh-backer/top/6/profile)
[![Backer](https://mynode.alexkaul.com/gh-backer/top/7/avatar/60)](https://mynode.alexkaul.com/gh-backer/top/7/profile)
[![Backer](https://mynode.alexkaul.com/gh-backer/top/8/avatar/60)](https://mynode.alexkaul.com/gh-backer/top/8/profile)
[![Backer](https://mynode.alexkaul.com/gh-backer/top/9/avatar/60)](https://mynode.alexkaul.com/gh-backer/top/9/profile)

[[捐赠](https://mynode.alexkaul.com/gh-donate)] 感谢您的支持！ 🙌
