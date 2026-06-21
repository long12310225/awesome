# 很棒的 OpenID 连接 [![Awesome](https://awesome.re/badge-flat.svg)](https://awesome.re)

> [OpenID Connect](https://openid.net/#introduction) 是 OAuth 2.0 之上的身份验证协议和身份层，在许多 SSO 中使用，并在许多社交登录（Apple、Facebook、Google 等）中采用。基本上，它允许用户使用 OpenID Connect 提供商 (OP) 的现有帐户对服务进行身份验证，在用户同意后共享一些身份信息，并获取访问令牌来访问依赖方 (RP) 应用程序上的资源。

> 查找此精选的提供商、服务、库和资源列表以采用它，并了解有关现有规范和草案规范的更多信息。

## 内容

- [OpenID 提供商 (OP)](#openid-providers-op)
- [依赖方 (RP) 库](#relying-parties-rp-libraries)
    - [C](#c)
    - [C#](#c-1)
    - [Dart](#dart)
    - [Erlang](#erlang)
    - [Golang](#golang)
    - [Java](#java)
    - [JavaScript](#javascript)
    - [OCaml](#ocaml)
    - [PHP](#php)
    - [Python](#python)
    - [Ruby](#ruby)
    - [Rust](#rust)
- [依赖方 (RP) 软件插件](#relying-parties-rp-software-plugins)
- [Resources](#resources)
    - [流量/拨款类型 规格](#flows--grant-types-specifications)
    - [Specifications](#specifications)
    - [Websites](#websites)
    - [专题文章](#thematic-articles)
    - [Playgrounds](#playgrounds)
    - [测试实用程序](#testing-utilities)
    - [Books](#books)

---

## OpenID 提供商 (OP)

*OpenID Connect 提供商作为 SaaS 和开源解决方案。*

- [Auth0](https://auth0.com/docs/authenticate/protocols/openid-connect-protocol) - OpenID Connect 和 OAuth 2.0 服务在云上作为 SaaS 提供。
- [Authelia](https://www.authelia.com/) - 开源身份验证、授权服务器和门户在提供单点登录 (SSO) 时履行信息安全的身份和访问管理 (IAM) 角色。
- [Authentik](https://github.com/goauthentik/authentik) - 开源身份提供商专注于灵活性和多功能性。
- [Authlete](https://www.authlete.com/) - 供开发人员实施 OAuth 授权服务器和 OpenID Connect 身份提供商的 API 集。
- [AWS Cognito](https://aws.amazon.com/cognito/) - 除了 IAM 功能外，Cognito by Amazon Web Services 还具有 OpenID Connect 提供商。
- [Clerk](https://clerk.com/) - 通过用户管理和 OpenID Connect 提供商功能进行身份验证。
- [Cloudentity](https://cloudentity.com/) - 具有 FAPI 和 eKYC 支持的云身份和授权平台。
- [Connect2id](https://connect2id.com/products/server) - 面向企业的 OpenID Connect SSO 和 IdP 服务器。
- [Curity Identity Server](https://curity.io/product/) - API 安全解决方案将身份和 API 访问管理结合在一起。
- [Descope](https://docs.descope.com/identity-federation/applications/oidc-apps) - OpenID Connect 提供商和身份联合解决方案，提供拖放用户身份验证和授权流程。
- [Dex](https://github.com/dexidp/dex) - 通过“连接器”充当其他身份提供商的门户的提供商。例如 LDAP、SAML、OIDC 或已建立的身份提供商（例如 GitHub、Google 和 Active Directory）。
- [Duende IdentityServer](https://duendesoftware.com/products/identityserver) - ASP.NET Core OpenID Connect 提供程序解决方案。
- [Duo](https://duo.com/) - 由 Cisco 开发的 OpenID Connect 提供商和 IdP 解决方案。
- [FrontEgg](https://docs.frontegg.com/docs/configure-frontegg-as-oidc-idp) - 具有 OpenID Connect 提供商功能的 SaaS 平台客户身份解决方案。
- [Keycloak](https://www.keycloak.org/) - 由 RedHat 支持的开源项目，提供用户联合、强身份验证、用户管理、细粒度授权等。
- [Gluu](https://gluu.org/) - OpenID Connect 提供商和 FAPI 认证的解决方案并与 IAM 集成。
- [Gravitee.io](https://www.gravitee.io/platform/access-management) - 开源 OpenID Connect/OAuth 2.0 提供商旨在成为应用程序和身份提供商之间的桥梁，以进行身份​​验证、授权和获取有关用户帐户的信息。
- [Kinde](https://kinde.com) - OpenID Connect 和 OAuth 2.0 服务在云上作为 SaaS 提供。
- [LoginRadius](https://www.loginradius.com/) - 可以充当 OpenID Connect 提供商的 SaaS CIAM。
- [Logto](https://github.com/logto-io/logto) - 专为客户身份和访问管理 (CIAM) 以及劳动力身份管理而设计的开源解决方案，具有基于 OpenID Connect 的身份验证。
- [Okta](https://www.okta.com/) - 可扩展的解决方案，通过云和本地解决方案的联合、单点登录、API 安全性和工作流程来支持客户和员工身份。
- [Microsoft Entra ID](https://www.microsoft.com/en-us/security/business/solutions/identity-access) - 由 Microsoft 开发的软件组件，提供对系统和应用程序的单点登录访问。
- [MITREid Connect](https://github.com/mitreid-connect/OpenID-Connect-Java-Spring-Server) - Java 中的开源 OpenID Connect 参考实现。
- [OpenIddict](https://github.com/openiddict/openiddict-core) - .NET 开源 OpenID Connect Provider 实现，支持 ASP.NET Core 2.1（及更高版本）应用程序。
- [OneLogin](https://www.onelogin.com/) - 具有 OpenID Connect 提供商功能的 SaaS 员工和客户 IAM 解决方案。
- [Ory Hydra](https://github.com/ory/hydra) - 开源 OpenID Certified™ OpenID Connect 和 OAuth 提供商。
- [Ory Polis (formerly BoxyHQ Jackson)](https://github.com/ory/polis) - 开源企业 SSO 将 SAML 登录流桥接或代理到 OpenID Connect，还具有用户目录同步功能。
- [panva/node-oidc-provider](https://github.com/panva/node-oidc-provider) - Node.js 中的开源和经过认证的 OpenID Connect 提供程序实现，支持 FAPI 1.0 和 FAPI 2.0。
- [PingFederate](https://www.pingidentity.com/en/platform/capabilities/authentication-authority/pingfederate.html) - 联合服务器为企业客户、合作伙伴和员工提供安全的单点登录、API 安全性和配置。
- [Pocket ID](https://github.com/pocket-id/pocket-id) - 一个简单的 OpenID Connect 提供程序，允许用户使用其密钥进行身份验证。
- [SiteMinder](https://www.broadcom.com/products/identity/siteminder) - Broadcom 提供的 IAM，支持 OpenID Connect 提供商。
- [SSOJet](https://ssojet.com) - 基于 OpenID Connect 的解决方案，可将企业 SSO 无缝集成到您的 B2B SaaS 中。
- [Scalekit](https://docs.scalekit.com/authenticate/sso/add-modular-sso/) - B2B 应用程序的 OpenID Connect 提供商，充当托管企业 SSO 的应用程序的 OpenID 提供商 (OP)。
- [Transmit Security](https://developer.transmitsecurity.com/guides/user/auth_oidc/) - 支持基于 OpenID Connect 集成的 CIAM 解决方案。
- [WSO2 Identity Server](https://wso2.com/identity-server/) - Identity Server 提供现代身份和访问管理功能，可以轻松构建到组织的客户体验 (CX) 应用程序中。
- [Zitadel](https://github.com/zitadel/zitadel) - 具有 OpenID Connect 提供商 (OP) 和 SAMLv2 可供使用的开源身份解决方案。
- [Alibaba Cloud IDaaS](https://www.alibabacloud.com/en/product/identity-as-a-service-idaas) - 阿里云 OpenID Connect 提供商即服务。
- [SecureAuth](https://www.secureauth.com/) - 提供 OpenID Connect Provider 功能的身份安全平台。
- [FusionAuth](https://fusionauth.io/) - 具有 OpenID Connect 提供商功能的开源身份和访问管理 (IAM) 解决方案。
- [IBM Verify](https://www.ibm.com/products/verify) - IBM 的 OpenID Connect 提供商和身份即服务 (IDaaS) 解决方案。
- [MojoAuth](https://mojoauth.com) - 基于 OpenID Connect 的无密码身份验证平台，使用密钥、魔术链接和 OTP。
- [CyberArk Identity](https://www.cyberark.com/) - 提供 OpenID Connect Provider 功能的身份安全解决方案。
- [SailPoint](https://www.sailpoint.com/) - 提供 OpenID Connect Provider 功能的企业身份安全平台。
- [SAP Customer Identity](https://help.sap.com/docs/SAP_CUSTOMER_DATA_CLOUD/8b8d6fffe113457094a17701f63e3d6a/4167c2d870b21014bbc5a10ce4041860.html) - SAP 的 OpenID Connect 提供商和身份即服务 (IDaaS) 解决方案。
- [WorkOS](https://workos.com/) - 一个身份管理平台，使组织能够为其员工、客户和合作伙伴提供安全访问。

- [OpenID Foundation conformance suite](https://gitlab.com/openid/conformance-suite) - 测试一致性套件以获得 OpenID 基金会认证，涵盖 OpenID Connect、FAPI1-Advanced、FAPI2、FAPI-CIBA 和 OpenID for Identity Assurance (ekyc)。


## 依赖方 (RP) 库

*用于在客户端应用程序上实施 OpenID Connect 的依赖方 (RP) 库。*

### C

- [liboauth2](https://github.com/OpenIDC/liboauth2) - 用于构建基于 C 的 OpenID Connect 提供者和依赖方的通用库。
- [mod_auth_openidc](https://github.com/OpenIDC/mod_auth_openidc) - Apache Server 2.x 的 OpenID Connect 依赖方认证实施。
- [ngx_oauth2_module](https://github.com/OpenIDC/ngx_oauth2_module) - Nginx 的 OpenID Connect 依赖方认证实施。

### C#

- [IdentityModel.OidcClient](https://github.com/IdentityModel/IdentityModel.OidcClient) - 适用于本机移动/桌面应用程序的 C# / .NET OpenID Connect 依赖方客户端认证库。

### 飞镖

- [openid_client](https://github.com/appsup-dart/openid_client) - 适用于 Flutter、Web 和命令行中 Dart 的 OpenID Connect 依赖方客户端库。

### 埃尔兰

- [oidcc](https://github.com/erlef/oidcc) - 经过认证的适用于 Erlang 和 Elixir 的 OpenID Connect 依赖方客户端库，支持 FAPI。

### 戈兰

- [coreos/go-oidc](https://github.com/coreos/go-oidc) - Go OpenID Connect 客户端由 CoreOS 开发。
- [golang.org/x/oauth2](https://pkg.go.dev/golang.org/x/oauth2) - OAuth 2.0 规范的官方 Golang 客户端实现，支持 OpenID Connect。
- [zitadel/oidc](https://github.com/zitadel/oidc) - 经过 OpenID 基金会认证的 OpenID Connect 客户端和服务器库。

### 爪哇

- [com.google.oauth-client/google-oauth-client](https://github.com/googleapis/google-oauth-java-client) - OAuth 依赖方 Java 库，由 Google 为 OAuth 2.0 编写，支持 Android。
- [com.nimbusds/oauth2-oidc-sdk](https://mvnrepository.com/artifact/com.nimbusds/oauth2-oidc-sdk) - 由 connect2id 开发的 Java SDK，具有 OpenID Connect、FAPI、Federation 和 eKYC/身份保证扩展。
- [Spring Security](https://docs.spring.io/spring-security/reference/servlet/oauth2/login/index.html) - Java 框架，用于通过 OpenID Connect 和 OAuth 2.0 支持保护基于 Spring 的应用程序。

### JavaScript

- [openid-client](https://github.com/panva/node-openid-client) - Node.js 的 OpenID Certified™ 依赖方（OpenID Connect/OAuth 2.0 客户端）实现。
- [oauth4webapi](https://github.com/panva/oauth4webapi) - 用于 JavaScript 运行时的 OAuth 2/OpenID Connect 库。
- [oidc-client-ts](https://github.com/authts/oidc-client-ts) - 适用于基于浏览器的应用程序的 TypeScript OpenID 客户端和 OAuth 2.0 客户端。

*库层专注于特定框架集成*

- [Better Auth](https://github.com/better-auth/better-auth) - 用于 SPA 和服务器端应用程序的 TypeScript 框架无关的身份验证库。
- [nuxt-auth for Nuxt 2](https://github.com/nuxt-community/auth-module) - Nuxt.js 2 的零样板身份验证支持。
- [nuxt-auth for Nuxt3](https://github.com/sidebase/nuxt-auth) - Nuxt 3 用户身份验证和会话库。 nuxt-auth 包装 NextAuth.js。
- [angular-auth-oidc-client](https://github.com/damienbod/angular-auth-oidc-client) - 具有 OAuth 2.0 和 OpenID Connect 流程以及 Angular 原理图的 Angular 认证库。
- [angular-oauth2-oidc](https://github.com/manfredsteyer/angular-oauth2-oidc) - 该库在 Angular 中引入了对 OAuth 2.0 和 OpenID Connect (OIDC) 的支持。

### 奥卡米尔

- [ocaml-oidc](https://github.com/ulrikstrid/ocaml-oidc) - OCaml 中经过认证的 OpenID Connect 依赖方实施。

### PHP

- [Laravel Socialite](https://github.com/laravel/socialite) - Laravel 对 OAuth 1 和 OAuth 2 库的包装，支持 OpenID Connect。
- [thephpleague/oauth2-client](https://github.com/thephpleague/oauth2-client) - 与 PHP 的 OAuth 2.0 服务提供商集成。
- [Symfony Security](https://symfony.com/doc/current/security/access_token.html#using-openid-connect-oidc) - 支持 OpenID Connect 的 PHP 安全组件。

### 蟒蛇

- [mozilla-django-oidc](https://github.com/mozilla/mozilla-django-oidc/) - 由 Mozilla 维护的 Django OpenID Connect 依赖方库。

### 红宝石

- [openid_connect](https://github.com/nov/openid_connect) - Ruby OpenID Connect 依赖方 (RP) 和提供商 (OP) 库。
- [omniauth_openid_connect](https://github.com/omniauth/omniauth_openid_connect) - Ruby OmniAuth 库的 OpenID Connect 策略。

### 铁锈

- [openidconnect](https://github.com/ramosbugs/openidconnect-rs) - OpenID Connect Rust 的依赖方 (RP) 库。

## 依赖方 (RP) 软件插件

- [MiniOrange OAuth SSO](https://wordpress.org/plugins/miniorange-login-with-eve-online-google-facebook/) - WordPress OAuth 和 OpenID Connect 插件由 MiniOrange 开发和积极维护。

## 资源

在哪里可以找到有关 OpenID Connect 的学习资源。

### 流量/拨款类型 规格

- [authorization_code](https://datatracker.ietf.org/doc/html/rfc6749?grant_type=authorization_code#section-1.3.1) - OAuth 2.0 授权代码授予类型，非常适合 Web 应用程序等公共客户端授权。
- [refresh_token](https://datatracker.ietf.org/doc/html/rfc6749?grant_type=refresh_token#section-1.5) - OAuth 2.0 刷新令牌授予类型用于将刷新令牌与短期访问令牌交换，有时还交换新的刷新令牌。
- [client_credentials](https://datatracker.ietf.org/doc/html/rfc6749?grant_type=client_credentials#section-4.4) - OAuth 2.0 客户端凭据授予提供了一种无需用户交互即可获取令牌的方法，非常适合机器对机器通信。
- [implicit](https://datatracker.ietf.org/doc/html/rfc6749?grant_type=implicit#section-4.2) - OAuth 2.0 隐式授权类型已弃用，不应再使用。
- [password](https://datatracker.ietf.org/doc/html/rfc6749?grant_type=password#section-4.3) - OAuth 2.0 资源所有者密码凭证授予类型，不建议再使用。
- [urn:ietf:params:oauth:grant-type:device_code](https://datatracker.ietf.org/doc/html/rfc8628) - OAuth 2.0 设备授权侧重于与智能电视等浏览器上下文之外的用户进行交互。
- [urn:ietf:params:oauth:grant-type:jwt-bearer](https://datatracker.ietf.org/doc/html/rfc7523) - OAuth 2.0 的 JSON Web 令牌 (JWT) 配置文件，用于授权客户端使用可信提供商颁发的另一个 JWT 获取访问令牌。
- [urn:ietf:params:oauth:grant-type:saml2-bearer](https://datatracker.ietf.org/doc/html/rfc7522) - OAuth 2.0 的安全断言标记语言 (SAML) 2.0 配置文件，用于授权客户端通过受信任的提供商发布的 SAML 断言获取访问令牌。
- [urn:ietf:params:oauth:grant-type:token-exchange](https://datatracker.ietf.org/doc/html/rfc8693) - OAuth 2.0 令牌交换是一种授权类型，它提供了一种从另一个令牌获取令牌的方法，并提供了添加参与者声明的能力。
- [Proof Key for Code Exchange (PKCE) Extension](https://datatracker.ietf.org/doc/html/rfc7636) - 授权代码流程的扩展添加了针对代码拦截攻击的安全层。

### 规格

#### 已发表

- [CBOR Web Token (CWT)](https://datatracker.ietf.org/doc/html/rfc8392) - 用于 OpenID Connect 和 OAuth 2.0 上下文中令牌的 CBOR 格式。
- [OpenID Connect Core 1.0](https://openid.net/specs/openid-connect-core-1_0.html) - 定义核心 OpenID Connect 功能：基于 OAuth 2.0 构建的身份验证以及使用声明来传达有关最终用户的信息。它还描述了使用 OpenID Connect 的安全和隐私注意事项。
- [The OAuth 2.0 Authorization Framework](https://datatracker.ietf.org/doc/html/rfc6749) - OpenID Connect 所基于的底层 OAuth 2.0 协议。
- [JSON Web Token (JWT)](https://datatracker.ietf.org/doc/html/rfc7519) - JWT 规范用于 OAuth 2.0 和 OpenID Connect 规范中提到的不同令牌。
- [JSON Web Token (JWT) Profile for OAuth 2.0 Access Tokens](https://datatracker.ietf.org/doc/html/rfc9068) - OAuth 2.0 上下文中的 JWT 格式和验证规范。
- [JSON Web Key (JWK)](https://datatracker.ietf.org/doc/html/rfc7517) - JavaScript 对象表示法 (JSON) 数据结构，表示 OpenID Connect 提供商提供的加密密钥。
- [JSON Web Encryption (JWE)](https://datatracker.ietf.org/doc/html/rfc7516) - JWE 规范，使用基于 JSON 的数据结构表示加密内容。
- [JSON Web Signature (JWS)](https://datatracker.ietf.org/doc/html/rfc7515) - JWS 规范，代表受数字签名保护的内容。
- [OAuth 2.0 Threat Model and Security Considerations](https://datatracker.ietf.org/doc/html/rfc6819) - 使用 OAuth 2.0 / OpenID Connect 的已知威胁和对策。
- [OAuth 2.0 Authentication Method Reference Values](https://datatracker.ietf.org/doc/html/rfc8176) - 列出 AMR 令牌声明的身份验证方法值。
- [OAuth 2.0 Authorization Framework: Bearer Token Usage](https://datatracker.ietf.org/doc/html/rfc6750) - 描述如何在 HTTP 请求中使用承载令牌来访问 OAuth 2.0 受保护的资源。
- [OAuth 2.0 for Native Apps](https://datatracker.ietf.org/doc/html/rfc8252) - 在本机应用程序中使用 OAuth 的安全性和可用性最佳实践。
- [OAuth 2.0 Pushed Authorization Requests](https://datatracker.ietf.org/doc/html/rfc9126) - 推送授权请求 (PAR) 允许客户端通过直接请求将 OAuth 2.0 授权请求的有效负载推送到授权服务器。
- [OAuth 2.0 Mutual-TLS Client Authentication and Certificate-Bound Access Tokens](https://datatracker.ietf.org/doc/html/rfc8705) - 利用基于客户端证书的双向 TLS (mTLS) 对 OAuth 2.0 的增强安全选项进行标准化。
- [OAuth 2.0 JWT-Secured Authorization Request (JAR)](https://datatracker.ietf.org/doc/html/rfc9101) - 允许以 JSON Web 令牌 (JWT) 形式发送请求参数，该令牌可以使用 JSON Web 签名 (JWS) 进行签名并使用 JSON Web 加密 (JWE) 进行加密，以便获得授权请求的完整性、源身份验证和机密性属性。
- [OpenID Connect Discovery 1.0](https://openid.net/specs/openid-connect-discovery-1_0.html) - OpenID Connect 依赖方发现最终用户的 OpenID 提供商并获取与其交互所需的信息的机制。
- [OpenID Connect Front-Channel Logout](https://openid.net/specs/openid-connect-frontchannel-1_0.html) - 注销机制，通过 OpenID Connect 提供商 (OP) 和被注销的依赖方 (RP) 之间的用户代理使用前端通道通信，不需要依赖方页面上的 OpenID 提供商 iframe。
- [OpenID Connect Back-Channel Logout](https://openid.net/specs/openid-connect-backchannel-1_0.html) - 注销机制，使用 OpenID Connect 提供商 (OP) 和注销的依赖方 (RP) 之间的直接反向通道通信。
- [OpenID Connect RP-Initiated Logout](https://openid.net/specs/openid-connect-rpinitiated-1_0.html) - 定义依赖方如何通过将最终用户的用户代理重定向到 OP 的注销端点来请求 OpenID Connect 提供商注销最终用户。
- [OAuth 2.0 Authorization Server Metadata](https://datatracker.ietf.org/doc/html/rfc8414) - OAuth 2.0 客户端可用来获取与 OAuth 2.0 授权服务器交互所需的信息的元数据格式。
- [OAuth 2.0 Token Revocation](https://datatracker.ietf.org/doc/html/rfc7009) - OAuth 授权服务器的端点，允许客户端通知授权服务器不再需要先前获取的刷新或访问令牌。
- [OAuth 2.0 Dynamic Client Registration Protocol](https://datatracker.ietf.org/doc/html/rfc7591) - 定义 OAuth 2.0 依赖方 (RP) 如何向 OAuth 2.0 服务器提供商动态注册。
- [OAuth 2.0 Demonstrating Proof of Possession (DPoP)](https://datatracker.ietf.org/doc/html/rfc9449) - 展示 OAuth 2.0 客户端私钥的拥有证明。
- [OpenID Connect Dynamic Client Registration](https://openid.net/specs/openid-connect-registration-1_0.html) - 通过应用程序级别的所有权证明机制来约束 OAuth 2.0 令牌发送者的机制，该机制允许检测令牌的重放攻击。
- [OAuth 2.0 Token Introspection](https://datatracker.ietf.org/doc/html/rfc7662) - 受保护资源查询 OAuth 2.0 授权服务器以确定 OAuth 2.0 令牌的活动状态并确定有关此令牌的元信息的方法。
- [OAuth 2.0 Rich Authorization Requests (RAR)](https://datatracker.ietf.org/doc/html/rfc9396) - 使用附加的authorization_details参数扩展OAuth 2.0授权请求，该参数允许客户端使用JSON数据结构的表达能力来指定其细粒度的授权要求。
- [Financial-grade API Security Profile 1.0 - Part 1: Baseline](https://openid.net/specs/openid-financial-api-part-1-1_0.html) - OAuth 的基准安全配置文件，适用于保护金融级 API 环境中具有中等固有风险的 API。
- [Financial-grade API Security Profile 1.0 - Part 2: Advanced](https://openid.net/specs/openid-financial-api-part-2-1_0.html) - OAuth 的高级安全配置文件适合用于保护金融级 API 环境中具有高固有风险的 API。
- [JWT Secured Authorization Response Mode for OAuth 2.0 (JARM)](https://openid.net/specs/oauth-v2-jarm.html) - 基于 JWT 的模式对 OAuth 授权响应参数进行编码，并附加用于进一步保护传输的声明。
- [Initiating User Registration via OpenID Connect](https://openid.net/specs/openid-connect-prompt-create-1_0.html) - 通过 OpenID Connect 启动用户注册并创建提示的规范。
- [OpenID Connect Session Management](https://openid.net/specs/openid-connect-session-1_0.html) - 有关 OpenID Connect 会话管理的规范。
- [OpenID Connect Client-Initiated Backchannel Authentication Flow - Core 1.0](https://openid.net/specs/openid-client-initiated-backchannel-authentication-core-1_0.html) - 客户端启动的反向通道身份验证 (CIBA) 流程规范。
- [OpenID Provider Authentication Policy Extension 1.0](https://openid.net/specs/openid-provider-authentication-policy-extension-1_0.html) - 有关依赖方可以请求 OpenID 提供商应用特定身份验证策略（例如多因素身份验证）的机制的规范。
- [JWT Response for OAuth Token Introspection](https://datatracker.ietf.org/doc/html/rfc9701) - 用于 OAuth 2.0 令牌内省的已签名附加 JSON Web 令牌 (JWT) 安全响应。
- [OAuth 2.0 Protected Resource Metadata](https://datatracker.ietf.org/doc/html/rfc9728) - OAuth 2.0 客户端或授权服务器可用来获取与 OAuth 2.0 受保护资源交互所需的信息的元数据格式。
- [OAuth 2.0 Security Best Current Practice](https://datatracker.ietf.org/doc/html/rfc9700) - 使用 OAuth 2.0 和 OpenID Connect 时的最佳安全实践。
- [OpenID Connect Extended Authentication Profile (EAP) ACR Values 1.0](https://openid.net/specs/openid-connect-eap-acr-values-1_0.html) - OpenID Connect 扩展身份验证配置文件 (EAP) ACR 值规范，允许请求特定的身份验证方法和保证级别。
- [Resource Indicators for OAuth 2.0](https://datatracker.ietf.org/doc/html/rfc8707) - 一种允许 OAuth 2.0 客户端指示其想要访问的资源服务器的机制。
- [OAuth 2.0 Authorization Server Issuer Identification](https://datatracker.ietf.org/doc/html/rfc9207) - 在授权响应中定义新的 iss 参数，以便识别发出授权响应的授权服务器并减轻混淆攻击。
- [FAPI 2.0 Security Profile](https://openid.net/specs/fapi-security-profile-2_0.html) - 新版本的 FAPI 安全配置文件适用于保护金融级 API 背景下具有高固有风险的 API。
- [FAPI 2.0 Attacker Model](https://openid.net/specs/fapi-attacker-model-2_0.html) - 金融级 API 的安全目标、攻击者模型和安全机制。
- [FAPI 2.0 Message Signing](https://openid.net/specs/fapi-message-signing-2_0.html) - API 安全配置文件，用于签署和验证某些基于 FAPI 2.0 安全配置文件的请求和响应。

#### 吃水

- [OAuth 2.0 Dynamic Client Registration Management Protocol](https://datatracker.ietf.org/doc/html/rfc7592) - 用于管理 OAuth 2.0 动态客户端注册的端点。
- [OpenID Connect Standard Claims Registration for CBOR Web Tokens](https://datatracker.ietf.org/doc/html/draft-ietf-spice-oidc-cwt-01.html) - 定义如何在 CBOR Web 令牌 (CWT) 中表示 OpenID Connect 标准声明。
- [OpenID Connect Federation 1.0](https://openid.net/specs/openid-federation-1_0.html) - 起草在组织之间建立双边联盟的规范。
- [OpenID AuthZEN](https://openid.net/specs/authorization-api-1_0-01.html) - 用于向授权服务请求访问决策的标准化 API，以简化服务之间的集成。
- [Financial-grade API: Client Initiated Backchannel Authentication Profile](https://openid.net/specs/openid-financial-api-ciba.html) - 客户端发起的反向通道身份验证（又名 CIBA）的金融服务配置文件规范。
- [OAuth 2.0 for Browser-Based Apps](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-browser-based-apps) - 基于浏览器的应用程序中 OAuth 使用的安全性和可用性最佳实践。
- [Selective Disclosure for JWTs (SD-JWT)](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-selective-disclosure-jwt) - JWT 元素选择性公开的规范。
- [OAuth 2.1](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-13) - 将 OAuth 2.0 规范合并到单个文档中，删除已弃用的功能并阐明最佳实践。
- [OAuth 2.0 App2App Browserless Flow](https://github.com/yaron-zehavi/oauth-app2app-browserless) - 描述一种协议，允许跨应用程序进行本机导航，使用 App2App 模式执行身份验证，而无需 Web 浏览器。
- [OAuth 2.0 Attestation-Based Client Authentication](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-attestation-based-client-auth-07) - OAuth 2.0 的扩展使公共客户端能够使用密钥绑定证明进行身份验证。
- [OpenID Shared Signals Framework Specification 1.0](https://openid.net/specs/openid-sharedsignals-framework-1_0-ID3.html) - 共享信号框架 (SSF) 支持在合作伙伴之间共享信号和事件，从而支持风险事件共享和协调 (RISC) 和连续访问评估配置文件 (CAEP) 等多种应用程序。
- [Cross-App Access (XAA), formally known as the "Identity Assertion Authorization Grant"](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-identity-assertion-authz-grant-03.html) - 使 AI 代理和应用程序能够使用标准化和细粒度的 OAuth 权限，在用户同意的情况下安全地访问多个服务并执行操作。
- [OAuth Identity and Authorization Chaining Across Domains](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-identity-chaining-11) - 使用 OAuth 令牌交换和基于 JWT 的断言，跨多个服务和信任域保留用户身份、授权上下文和调用链历史记录。
- [OpenID Connect for Agents (OIDC-A) 1.0](https://arxiv.org/html/2509.25974v1) - 一项研究提案（不是标准或 IETF 草案），扩展 OpenID Connect 以支持 OAuth 生态系统内的 AI 代理身份、证明、委托链和细粒度授权。

### 网站

- [OpenID](https://openid.net/) - OpenID Connect 官方网站。
- [OAuth](https://oauth.net/) - 由 Aaron Parecki 维护的 OAuth 网站列出了有关该协议的不同资源。
- [ByteByteGo](https://blog.bytebytego.com/i/135955829/oauth-explained-with-simple-terms) - Oauth 2.0 使用直观且简单的术语进行解释。
- [Aaron Parecki](https://aaronparecki.com/articles) - OAuth WG 成员关于 OAuth 2.0 的博客文章。
- [Alex Bilbie](https://alexbilbie.github.io/tag/oauth/) - 有关 OAuth 2.0 主题的博客文章。
- [CerberAuth](https://www.cerberauth.com/) - 谈论 OpenID Connect 和 OAuth 2.0 的博客。
- [Nacho](https://nacho.cerberauth.com/) - OAuth 2.0 客户端创建助手可帮助根据应用程序选择正确的授权类型。
- [Curity Resources](https://curity.io/resources/openid-connect/) - 有关 OpenID Connect 的 Curity 解决方案资源文章。
- [Okta Blog](https://developer.okta.com/blog/tags/oidc/) - Okta 供应商关于 OAuth 2.0 和 OpenID Connect 的博客文章。
- [Medium OAuth 2.0](https://medium.com/oauth-2) - 中型博客，包含有关 OAuth 2.0 使用的学习内容、模式和想法。
- [Mike Jones: Self-Issued](https://self-issued.info/) - Mike Jones 关于 OAuth 2.0 和 OpenID Connect 的博客文章。
- [IAMDevBox](https://www.iamdevbox.com/) - 开发人员博客涵盖 OAuth 2.0/2.1、OIDC、SAML、Keycloak、ForgeRock 和 PingIdentity，以及实践教程和故障排除指南。

### 专题文章

- [OAuth for Model Context Protocol](https://aaronparecki.com/2025/04/03/15/oauth-for-model-context-protocol) - Aaron Parecki 关于 OAuth 如何工作以及如何在模型上下文协议 (MCP) 服务器上下文中使用它的文章。
- [OAuth common vulnerabilities](https://portswigger.net/web-security/oauth) - PortSwigger 有关 OAuth 2.0 常见漏洞以及如何缓解这些漏洞的文章。
- [MCP OAuth 2.1 Authentication: How AI Agents Securely Connect to Tools](https://www.iamdevbox.com/posts/mcp-oauth-21-authentication-how-ai-agents-securely-connect-to-tools/) - 模型上下文协议如何使用 OAuth 2.1 以及强制 PKCE、RFC 8707 受众绑定和零配置发现来进行 AI 代理身份验证。
- [GitHub Actions OIDC – Non-Human Identities and Secretless Authentication](https://eparon.me/posts/2026-02-28-oidc-gh-actions-p1/) - 关于在 GitHub Actions 中从静态机密迁移到基于 OIDC 的身份的两部分指南，包括用于保护 API 的实用实验室。

### 游乐场

- [OAuth.com Playground](https://www.oauth.com/playground/) - OAuth 2.0 / OpenID Connect Playground 包含授权流程以及逐步获取访问令牌的过程。
- [SecureAuthCorp/oauth2c](https://github.com/SecureAuthCorp/oauth2c) - OAuth 2.0 和 OpenID Connect 命令行客户端用于测试和探索不同的流程。
- [Curity Playground](https://oauth.tools/) - 用于探索和测试 OAuth 和 OpenID Connect 流程的工具。
- [MojoAuth: Passkey Playground](https://mojoauth.com/oidc-playground/) - 使用此交互式工具构建和可视化 OpenID Connect 请求。配置参数、生成请求 URL 并解码 JWT 令牌。

### 测试实用程序

- [OAuth Mock Server](https://oauth.kogiqa.com/) - 一个免费开源的 OAuth 模拟服务器，只需替换 URL 即可模拟最大的提供商。对于 E2E 测试很有用。

### 书籍

- [2012 年 - OAuth 2.0 入门，作者：Ryan Boyd](https://www.oreilly.com/library/view/getting-started-with/9781449317843/)
- [2018 - Aaron Parecki 简化的 OAuth 2.0](https://www.amazon.com/OAuth-2-0-Simplified-Aaron-Parecki/dp/1387751514/)
- [2020 - Aaron Parecki 的 OAuth 2.0 RFC 小书](https://www.amazon.com/Little-Book-OAuth-2-0-RFCs/dp/B084DFYJS1/)
- [2021 - Keycloak - 现代应用程序的身份和访问管理：利用 Keycloak、OpenID Connect 和 OAuth 2.0 协议的强大功能来保护应用程序，作者：Stian Thorgersen 和 Pedro Igor Silva](https://www.amazon.com/Keycloak-Management-Applications-protocols-applications-ebook/dp/B092KP135B/)
- [2022 年 - 解决现代应用程序中的身份管理：揭秘 OAuth 2、OpenID Connect 和 SAML 2，作者：Yvonne Wilson](https://www.amazon.com/Solving-Identity-Management-Modern-Applications-ebook/dp/B0BMQHF83G/)

## 贡献

随时欢迎您的贡献！请先查看[贡献指南](https://github.com/cerberauth/awesome-openidconnect/blob/master/CONTRIBUTING.md)。
