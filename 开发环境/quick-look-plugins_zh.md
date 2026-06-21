# 快速查看插件 [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> 为开发者提供的有用的[快速查看](https://en.wikipedia.org/wiki/Quick_Look)插件列表

## 安装

### 使用自制软件

- 运行 `brew install <package>`

##### 卡塔利娜笔记

要让许多插件在 Catalina 及更高版本中工作，您需要删除隔离属性。

运行此命令以查看属性：

```
xattr -r ~/Library/QuickLook
```

并运行以下命令来删除属性：

```
xattr -d -r com.apple.quarantine ~/Library/QuickLook
```

### 手动

- 点击“手动下载”
- 将下载的 .qlgenerator 文件移动到 `~/Library/QuickLook`
- 运行“qlmanage -r”

## 插件

### 斯蒂芬·QL

> 预览不带或带未知文件扩展名的纯文本文件。示例：README、CHANGELOG、index.styl 等。

运行 `brew install qlstephen` 或[手动下载](https://github.com/whomwah/qlstephen/releases/latest)

[![](screenshots/QLStephen.png)](https://github.com/whomwah/qlstephen)

### QLMarkdown

> 预览 Markdown 文件

运行 `brew install --cask qlmarkdown` 或[手动下载](https://github.com/sbarex/QLMarkdown/releases/latest)

[![](screenshots/QLMarkdown.png)](https://github.com/sbarex/QLMarkdown)

### 快速查看JSON

> 预览 JSON 文件

[手动下载](http://www.sagtau.com/media/QuickLookJSON.qlgenerator.zip)

[![](screenshots/QuickLookJSON.png)](http://www.sagtau.com/quicklookjson.html)

### 更好的ZipQL

> 预览档案

> 注意：BetterZipQL 插件已与 BetterZip 应用程序集成。

运行“brew install betterzip”来安装 BetterZip 应用程序及其 Quick Look 插件或[手动下载](https://macitbetter.com/BetterZip.zip)

旧版 BetterZipQL 插件可以[在此处下载](https://macitbetter.com/dl/BetterZipQL-1.5.zip)。

[![](screenshots/BetterZipQL.png)](https://macitbetter.com/BetterZip-Quick-Look-Generator/)

### 可疑包裹

> 预览标准 Apple 安装程序包的内容

运行“brew install可疑包”或[手动下载](https://www.mothersruin.com/software/downloads/SuspiciousPackage.xip)

[![](screenshots/SuspiciousPackage.png)](https://www.mothersruin.com/software/SuspiciousPackage/)

### 外观

> 预览 macOS 应用程序的内容

运行“brew install apparency”或[手动下载](https://mothersruin.com/software/downloads/Apparency.dmg)

[![](screenshots/Apparency.png)](https://mothersruin.com/software/Apparency/)

### QLVideo

> 预览大多数类型的视频文件及其缩略图、封面和元数据

运行 `brew install qlvideo` 或[手动下载](https://github.com/Marginal/QLVideo/releases/latest)

[![](screenshots/QLVideo.png)](https://github.com/Marginal/QLVideo)

### 源代码预览💰

> 包括 10 多种颜色主题和 50 多种语言的语法突出显示，包括 JavaScript、Python、Java、CSS 和 JSON。

在 [App Store](https://apps.apple.com/app/source-code-preview/id6759270528) 上购买。

[![](screenshots/SourceCodePreview.png)](https://anybox.ltd/source-code-preview)

### 偷看💰

> Peek 允许您在 300 多个文件扩展名的快速查看预览中复制和查找文本、跳转到行号、使用生成的目录呈现 Github 风格的 Markdown、恢复滚动位置、突出显示语法等。

在 [App Store](https://apps.apple.com/app/peek-quick-look-extension/id1554235898) 上购买。

*该应用程序已被废弃且有缺陷，但仍然有效。*

[![](screenshots/Peek.png)](https://bigzlabs.com/peek)

### 文件夹预览💰

> 快速查看文件夹和档案内部。

在 [App Store](https://apps.apple.com/app/folder-preview/id6698876601) 上购买。

[![](screenshots/FolderPreview.png)](https://anybox.ltd/folder-preview)

### 文件夹快速查看💰

> 预览文件夹和存档内容（ZIP、RAR 等）。

在[App Store](https://apps.apple.com/app/id6753110395)上购买。

[![](screenshots/FolderQuickLook.png)](https://apps.apple.com/app/id6753110395)

### Flux降价

> 使用 Mermaid 图、KaTeX 数学、GFM 支持和交互式目录预览 Markdown 文件。

运行 `brew tap xykong/tap && brew install --cask Flux-markdown` 或 [手动下载](https://github.com/xykong/flux-markdown/releases/latest)

[![](screenshots/FluxMarkdown.png)](https://github.com/xykong/flux-markdown)

### 降价预览💰

> 使用 KaTex 和 Mermaid 支持快速查看 Markdown 文件。

在 [App Store](https://apps.apple.com/app/markdown-preview-quick-look/id6739955340) 上购买。

[![](screenshots/MarkdownPreview.png)](https://anybox.ltd/markdown-preview)

### EPS 预览💰

> EPS 预览将 EPS 文件的快速查看和缩略图添加到 Finder。

在[网站](https://anybox.ltd/eps-preview) 上购买。

[![](screenshots/EPSPreview.png)](https://anybox.ltd/eps-preview)

### 规定QL

> 预览 iOS / macOS 应用程序和配置信息

运行 `brew install provisionql` 或[手动下载](https://github.com/ealeksandrov/ProvisionQL/releases/latest)

[![](screenshots/ProvisionQL.png)](https://github.com/ealeksandrov/ProvisionQL)

### 网络P

> 预览 WebP 图像

> 注意：这已经被 `qlImageSize` 覆盖了，所以这里列出这个插件只是为了以防万一你不喜欢 `qlImageSize`。

运行 `brew install webpquicklook` 或 [手动下载](https://github.com/dchest/webp-quicklook/releases/latest)

[![](screenshots/WebP.png)](https://github.com/dchest/webp-quicklook)

### 源代码语法高亮

> 预览许多不同的源代码文件

运行 `brew install --cask --no-quarantine syntax-highlight` 或 [手动下载](https://github.com/sbarex/SourceCodeSyntaxHighlight/releases/latest)

[![](https://user-images.githubusercontent.com/8471055/118415204-5f53fc80-b6a9-11eb-93d8-b88c442c5744.png)](https://github.com/sbarex/SourceCodeSyntaxHighlight)

**注意：** 这可能会覆盖其他一些快速查看插件。

## 许可证

[![CC0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

在法律允许的范围内，[Sindre Sorhus](https://sindresorhus.com) 已放弃本作品的所有版权以及相关或邻接权。
