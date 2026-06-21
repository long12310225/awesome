# 很棒的苏帕巴斯 [![Awesome](https://awesome.re/badge-flat.svg)](https://awesome.re)

[Supabase](https://supabase.com/) 是 Firebase 的一个很棒的开源替代品，它为您提供 PostgreSQL 数据库、身份验证、即时 API、边缘功能、实时订阅和存储。

此列表试图涵盖该产品及其社区的精彩之处！ 👁⚡️👁

要**增强**此列表，请参阅 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 内容

- [官方首发](#official-starters)
- [社区启动者](#community-starters)
- [数据迁移工具](#data-migration-tools)
- [Supabase DX 工具](#supabase-dx-tools)
- [社区工具](#community-tools)
- [在线课程](#online-courses)
- [视频、播客、直播、讲座](#videos-podcasts-livestreams-talks)
- [集成指南](#integration-guides)
- [其他有趣的文章](#other-interesting-articles)

## 官方首发

以下启动器支持 `@supabase/supabase-js` v2 库。

- [Angular](https://github.com/supabase/supabase/tree/master/examples/user-management/angular-user-management) - ![auth](https://img.shields.io/badge/-auth-informational)
- [Expo](https://github.com/supabase/supabase/tree/master/examples/user-management/expo-user-management) - ![auth](https://img.shields.io/badge/-auth-informational)
- [Flutter](https://github.com/supabase/supabase/tree/master/examples/user-management/flutter-user-management) - ![auth](https://img.shields.io/badge/-auth-informational)
- [Next.js (TS)](https://github.com/supabase/supabase/tree/master/examples/user-management/nextjs-ts-user-management) - ![auth](https://img.shields.io/badge/-auth-informational)
- [Nuxt](https://github.com/supabase/supabase/tree/master/examples/user-management/nuxtjs-user-management) - ![auth](https://img.shields.io/badge/-auth-informational)
- [Nuxt3](https://github.com/supabase/supabase/tree/master/examples/user-management/nuxt3-user-management) - ![auth](https://img.shields.io/badge/-auth-informational)
- [React](https://github.com/supabase/supabase/tree/master/examples/user-management/react-user-management) - ![auth](https://img.shields.io/badge/-auth-informational)
- [Solid](https://github.com/supabase/supabase/tree/master/examples/user-management/solid-user-management) - ![auth](https://img.shields.io/badge/-auth-informational)
- [Svelte](https://github.com/supabase/supabase/tree/master/examples/user-management/svelte-user-management) - ![auth](https://img.shields.io/badge/-auth-informational)
- [Svelte Kit](https://github.com/supabase/supabase/tree/master/examples/user-management/sveltekit-user-management) - ![auth](https://img.shields.io/badge/-auth-informational)
- [Vue 3](https://github.com/supabase/supabase/tree/master/examples/user-management/vue3-user-management) - ![auth](https://img.shields.io/badge/-auth-informational)
- [Next.js, Slack Clone](https://github.com/supabase/supabase/tree/master/examples/slack-clone/nextjs-slack-clone) - ![实时](https://img.shields.io/badge/-realtime-orange)
- [Svelte, Todo list](https://github.com/supabase/supabase/tree/master/examples/todo-list/sveltejs-todo-list) - ![数据库](https://img.shields.io/badge/-database-9cf)
- [React Native, Stripe Payments](https://github.com/supabase-community/expo-stripe-payments-with-supabase-functions) - ![边缘函数](https://img.shields.io/badge/-edge%20functions-darkgreen)
- [Flutter, Stripe Payments](https://github.com/supabase-community/flutter-stripe-payments-with-supabase-functions) - ![边缘函数](https://img.shields.io/badge/-edge%20functions-darkgreen)

## 社区启动者

- [Vuepabase](https://github.com/JMaylor/vuepabase) - Vue3 Supabase 入门版，包括 Pinia、Vue-router 4、Tailwind CSS、Vitest、Cypress 等。
- [Supastarter](https://supastarter.dev) - Supabase 入门版，包含 Next.js、身份验证、邮件模板、登陆页面、仪表板和博客。
- [RedwoodJS Supabase Quickstart](https://github.com/redwoodjs/redwoodjs-supabase-quickstart) - 使用 RedwoodJS 的 Supabase 快速入门示例应用程序。
- [Basejump](https://usebasejump.com) - 开源 Next.js 入门程序，包含团队、个人帐户、邀请、Tailwind、i18n。经过充分测试的架构。
- [Supanext](https://www.supanext.com/) - Supabase 入门程序与 Next.js，包括 AI 应用程序示例、身份验证、计费、设置、登陆页面、博客等。
- [SupaSasS Lite](https://github.com/Razikus/supabase-nextjs-template) - 开源 Next.js SasS 模板（带有 2FA 和示例应用程序）
- [SupaSocial](https://github.com/koji0701/supabase-react-social-media-starter/tree/main) - 使用身份验证、好友请求、个人资料图片和示例应用程序（个人资料、好友、登录、排行榜和更多页面）来反应社交媒体启动器。
- [Extro](https://github.com/turbostarter/extro) - 开源浏览器扩展入门套件。

## 数据迁移工具

- [Supabase Schema](https://supabase-schema.vercel.app/) - 使用这个方便的工具生成 SQL 脚本和数据库图表。不需要任何敏感信息，只需要项目url + 匿名密钥。
- [Heroku to Supabase Importer](https://migrate.supabase.com/) - 鉴于 Heroku 即将结束免费支持，如果您希望在项目中继续支持任何 PostgreSQL 数据库，迁移到 Supabase 将是一个不错的选择。有了这个工具，迁移就会变得轻而易举。这是[指南](https://supabase.com/docs/guides/migrations/heroku)，其中包含有关此迁移过程的视频。
- [Supabase DB to Google Sheets](https://github.com/jadynekena/supabase-googlesheet) - 将 Supabase 数据拉入 Google Sheets 的工具。
- [Retool REST API data generator](https://retool.com/api-generator) - 用于生成要插入 PostgresDB 的结构化数据的工具。
- [Lovable Cloud to Supabase Exporter](https://github.com/dreamlit-ai/lovable-cloud-to-supabase-exporter) - 将表、用户和存储从 Lovable Cloud 迁移到您自己的 Supabase 后端，无需重置密码或手动 CSV 工作。

## Supabase DX 工具

- [Supabase CLI](https://supabase.com/docs/reference/cli) - Supabase CLI 提供了用于在本地开发项目并部署到 Supabase 平台的工具。
- [Supabase SQL](https://database.dev/) - 轻松查找常见用例 SQL 脚本以进行复制粘贴。
- [Supabase Plus](https://github.com/dsplce-co/supabase-plus) - 用于管理 Supabase 项目的额外工具集，超出了常规 Supabase CLI 的功能。

## 社区工具

- [MadeWithSupabase](https://www.madewithsupabase.com/) - 用于探索使用 Supabase 制作的项目的应用程序。用户可以通过使用的特定 Supabase 功能或通过用户给定的标签进行查找，还可以查找在特定日历月份提交的项目。
- [Octokit-lite](https://github.com/lyqht/Octokit-lite) - 用于在多个存储库上高效执行常见用例 GitHub 操作的应用程序。使用 Supabase Auth 和 DB。
- [Generate Supabase Database Types GitHub Action](https://github.com/lyqht/generate-supabase-db-types-github-action) - 用于根据 Supabase 数据库生成类型的 GitHub 操作。
- [Supabase Cache Helpers](https://github.com/psteinroe/supabase-cache-helpers) - 用于与 Supabase 配合使用的框架特定缓存实用程序的集合。
- [PostgreSQL WebAssembly by Snaplet and Supabase](https://supabase.com/blog/postgres-wasm) - 在浏览器中运行 PostgreSQL 的工具。
- [Bemi for Supabase JS](https://github.com/BemiHQ/bemi-supabase-js) - 用于自动数据更改跟踪的开源平台。
- [Supabase automated self host](https://github.com/singh-inder/supabase-automated-self-host) - 与 Caddy 和 Authelia 一起自行托管 Supabase。只需运行一个脚本。
- [Edge Worker](https://pgflow.dev) - 在 Supabase Edge Functions（后台任务）和 Supabase 队列上运行的开源无服务器任务队列工作线程。它简化了队列的使用，并添加了并发控制、重试和可观察性等有用的功能。
- [Supabase DataFlows SMS Hook](https://github.com/dataflows-au/supabase-sms-hook) - 通过 DataFlows SMS API 发送电话 OTP 验证。 Supabase Auth 的 Twilio 的澳大利亚替代品。
- [Pharos AI](https://github.com/Juliusolsson05/pharos-ai) - 开源实时情报仪表板，用于通过交互式地图、OSINT 源和人工智能驱动的简报跟踪地缘政治冲突。

## 在线课程

- [Build a Full-Stack App with Next.js, Supabase & Prisma](https://themodern.dev/courses/build-a-fullstack-app-with-nextjs-supabase-and-prisma-322389284337222224) - 学习使用一些最好的现代 Web 技术从头开始构建全栈应用程序：React / Next.js、Prisma 和 Supabase。 [Grégory D'Angelo](https://twitter.com/gdangel0) 的免费课程。
- [Cache Supabase data at the Edge with Cloudflare Workers and KV Storage](https://egghead.io/courses/cache-supabase-data-at-the-edge-with-cloudflare-workers-and-kv-storage-883c7959) - 通过免费课程教授开发人员如何使用 Cloudflare 工作人员在带有 KV 存储的 Supabase 上查询、执行缓存增删改查操作。
在 [Cloudflare x Supabase 开发者聚会](https://t.co/sqmDQahsA4) 上亮相。 [Jon Meyers](https://twitter.com/jonmeyers_io) 的免费课程。
- [Vue JS Essentials: A Beginners Series on Pinia, Vitest, and Supabase](https://www.youtube.com/watch?v=W-D6h7Jne18) - 一系列精彩的深入教程，包括前端测试和模拟生产级项目的模拟。

## 视频、播客、直播、讲座

- [Is Supabase Legit? Firebase Alternative Breakdown](https://youtu.be/WiwfiVdfRIc) - 视频由 Supabase 上的 Fireship.io 提供。
- [Supabase Happy Hours](https://www.youtube.com/watch?v=IJoc6dKy03c&list=PL5S4mPUpp4Ouyw8bMupHgxC3VL9BLZzvV) - 由 Supabase 核心团队主办的标志性持续直播系列，他们尝试使用 Supabase API 创建副项目并与社区互动。由核心成员 [Thor Schaeff](https://thorweb.dev/)、[Jon Meyers](https://jonmeyers.io/)、Alaister Young 和 [Tyler Shukert](https://dshukertjr.dev/) 主持。
- [Supabase Developer Stories](https://www.youtube.com/watch?v=QAm1x7KaLq4&list=PL5S4mPUpp4OuzQN-a_FY3OZQuYo4NmXvb) - 这是一个正在进行的系列，其中 SaaS 创始人/联合创始人使用 Supabase 展示他们的产品。
- [CityJS 2022 Talk on Building Billy with Supabase](https://www.youtube.com/watch?v=UiANV3uqT04&t=6841s) - 由 SupaSquad 成员 [Estee Tey](https://esteetey.dev/) 讲述如何使用 Supabase 构建 React Native 费用跟踪器侧项目。
- [Build An Image Gallery With Supabase Storage and React](https://www.youtube.com/watch?v=8tfdY0Sf2rA) - 有关使用 Supabase 上传和提供图像的教程。
- [PMF is one pivot away with Ant Wilson from Supabase](https://podcast.bitreach.io/episodes/product-market-fit-is-one-pivot-away-with-ant-wilson-founder-of-supabase) - 谈论Supabase 在产品市场契合（PMF）前后阶段的经验。

## 集成指南

- [Firebase to Supabase](https://github.com/supabase-community/firebase-to-supabase) - 从 Firebase 的不同组件（例如 Auth、Firestore、存储、函数）迁移到 Supabase 的指南集合。
- [How to Manage Your Supabase Database with Directus](https://directus.io/guides/directus-plus-supabase/) - Directus Studio 提供了一种通过无代码应用程序浏览、管理和可视化数据库内容的方法，本指南介绍了如何使用 Directus 设置 Supabase。
- [Supabase admin panel tutorial with Retool](https://retool.com/blog/supabase-tutorial-admin-panel/) - Retool 可帮助团队快速构建内部工具。了解如何使用 Retool 和 Supabase 设置管理面板。
- [Set up a monorepo with Supabase and Turborepo](https://philipp.steinroetter.com/posts/supabase-turborepo) - 讨论如何将代码库迁移到由turborepo驱动的pnpm monorepo，该库从单个存储库中提供3个Next.js应用程序、一个Preact小部件、一个React Native应用程序和两个Fastify服务器，所有这些都与同一个Supabase实例通信。
- [How to Implement RBAC (Role-Based Access Control) in Supabase](https://www.permit.io/blog/how-to-implement-rbac-in-supabase) - 了解如何使用 Permit.io 在 Supabase 应用程序中实施基于角色的访问控制 (RBAC) 授权。

## 其他有趣的文章

- [How to market to developers on Twitter: Learnings from 4 months of Supabase feed](https://www.developermarkepear.com/blog/developer-marketing-on-social-media-twitter-supabase) - 分析 Supabase 的增长营销策略，特别是在 Twitter 上。
- [How Fleeting Notes Migrated 1000+ Users from Firebase to Supabase (Stripe, Firebase, Supabase)](https://fleetingnotes.app/posts/migrating-from-firebase-to-supabase/) - 从 Stripe 集成及其数据库的角度介绍 Fleeting Notes（笔记应用程序）如何从 Firebase 迁移到 Supabase 的过程。
- [Ultimate guide to testing on Supabase using pgTAP](https://usebasejump.com/blog/testing-on-supabase-with-pgtap) - 如何测试 RLS 策略和对 Supabase 的请求。
- [Migrating from Firebase to Supabase: Lessons Learned](https://emergence-engineering.com/blog/firestore-supabase-migration) - 详细介绍了 BaaS 各个方面的迁移工作流程，以及它们在实时订阅和数据类型方面的差异。
- [Supabase vs Firebase: Choosing the Right Backend for Your Project](https://www.jakeprins.com/blog/supabase-vs-firebase-2024) - Supabase 和 Firebase 之间的详细比较。了解两个平台之间的主要差异以及选择 Supabase 相对于 Firebase 的优势。
