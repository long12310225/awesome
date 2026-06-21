# .htaccess 片段 [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
有用的 .htaccess 片段的集合，全部集中在一个位置。

> [!注意]
> `.htaccess` 文件适用于无权编辑主服务器配置文件的人员。它们本质上比使用主配置更慢、更复杂。请参阅[httpd 文档中的操作方法](https://httpd.apache.org/docs/current/howto/htaccess.html) 了解更多详细信息。

> [!警告]
> 虽然将代码片段放入“.htaccess”文件中在大多数情况下就足够了，但在某些情况下可能需要进行某些修改。使用风险自负。

> [!重要]
> 这些片段适用于 Apache 2.4。如果您仍在使用 Apache 2.2，请检查 [`2.2` 分支](https://github.com/phanan/htaccess/tree/2.2)。有关 2.2 和 2.4 之间的重大更改的详细信息，请参阅[升级文档](https://httpd.apache.org/docs/2.4/upgrading.html) 以及[此问题](https://github.com/phanan/htaccess/issues/2)。

## 制作人员
我们在这里所做的主要是将来自整个互联网的有用片段（例如，一个很好的片段来自 [Apache Server Configs](https://github.com/h5bp/server-configs-apache)）收集到一个地方。虽然我们一直在努力归还应有的信用，但有些东西可能会丢失。如果您认为这里的任何内容都是您的工作并且应该给予学分，请告诉我们，或者只是发送 PR。

## 目录
- [重写和重定向](#rewrite-and-redirection)
    - [力www](#force-www)
    - [以通用方式强制 www](#force-www-in-a-generic-way)
    - [强制非 www](#force-non-www)
    - [以通用方式强制非 www](#force-non-www-in-a-generic-way)
    - [强制使用 HTTPS](#force-https)
    - [强制在代理后面使用 HTTPS](#force-https-behind-a-proxy)
    - [强制尾随斜杠](#force-trailing-slash)
    - [删除尾部斜杠](#remove-trailing-slash)
    - [重定向单个页面](#redirect-a-single-page)
    - [使用 RedirectMatch 重定向](#redirect-using-redirectmatch)
    - [给单个目录起别名](#alias-a-single-directory)
    - [脚本的别名路径](#alias-paths-to-script)
    - [重定向整个站点](#redirect-an-entire-site)
    - [别名“干净”URL](#alias-clean-urls)
    - [从重定向中排除 URL](#exclude-url-from-redirection)
- [Security](#security)
    - [拒绝所有访问](#deny-all-access)
    - [拒绝除您之外的所有访问](#deny-all-access-except-yours)
    - [允许除垃圾邮件发送者之外的所有访问](#allow-all-access-except-spammers)
    - [拒绝访问隐藏文件和目录](#deny-access-to-hidden-files-and-directories)
    - [拒绝访问备份和源文件](#deny-access-to-backup-and-source-files)
    - [禁用目录浏览](#disable-directory-browsing)
    - [禁用图像盗链](#disable-image-hotlinking)
    - [禁用特定域的图像盗链](#disable-image-hotlinking-for-specific-domains)
    - [密码保护目录](#password-protect-a-directory)
    - [密码保护一个或多个文件](#password-protect-a-file-or-several-files)
    - [按推荐人阻止访客](#block-visitors-by-referrer)
    - [阻止特定用户代理](#block-specific-user-agents)
    - [防止框架网站](#prevent-framing-the-site)
    - [内容安全策略 (CSP)](#content-security-policy-csp)
    - [防止 MIME 类型嗅探](#prevent-mime-type-sniffing)
    - [设置推荐人政策](#set-referrer-policy)
    - [设置权限策略](#set-permissions-policy)
    - [删除服务器签名](#remove-server-signature)
- [Performance](#performance)
    - [压缩文本文件](#compress-text-files)
    - [设置过期标头](#set-expires-headers)
    - [设置缓存控制标头](#set-cache-control-headers)
    - [关闭电子标签](#turn-etags-off)
- [Miscellaneous](#miscellaneous)
    - [设置 PHP 变量](#set-php-variables)
    - [自定义错误页面](#custom-error-pages)
    - [自定义维护页面](#custom-maintenance-page)
    - [强制下载](#force-downloading)
    - [阻止下载](#prevent-downloading)
    - [允许跨域字体](#allow-cross-domain-fonts)
    - [启用跨域资源共享](#enable-cors)
    - [自动 UTF-8 编码](#auto-utf-8-encode)
    - [设置自定义 MIME 类型](#set-custom-mime-types)
    - [切换到另一个 PHP 版本](#switch-to-another-php-version)
    - [提供 WebP/AVIF 图像](#serve-webpavif-images)

## 重写和重定向
注意：假设您已安装并启用“mod_rewrite”。

### 力www
``` apacheconf
RewriteEngine on
RewriteCond %{HTTP_HOST} ^example\.com [NC]
RewriteRule ^(.*)$ https://www.example.com/$1 [L,R=301,NC]
```

### 以通用方式强制 www
``` apacheconf
RewriteCond %{HTTP_HOST} !^$
RewriteCond %{HTTP_HOST} !^www\. [NC]
RewriteCond %{HTTPS}s ^on(s)|
RewriteRule ^ http%1://www.%{HTTP_HOST}%{REQUEST_URI} [R=301,L]
```
这适用于_任何_域。 [来源](https://stackoverflow.com/questions/4916222/htaccess-how-to-force-www-in-a-generic-way)

### 强制非 www
[仍然](https://www.sitepoint.com/domain-www-or-no-www/) [开放](https://devcenter.heroku.com/articles/apex-domains) [for](https://yes-www.org/) [辩论](https://no-www.org/) www 或非 www 是正确的选择，所以如果您碰巧是裸域的粉丝，那么您可以：
``` apacheconf
RewriteEngine on
RewriteCond %{HTTP_HOST} ^www\.example\.com [NC]
RewriteRule ^(.*)$ https://example.com/$1 [L,R=301]
```

### 以通用方式强制非 www
``` apacheconf
RewriteEngine on
RewriteCond %{HTTP_HOST} ^www\.
RewriteCond %{HTTPS}s ^on(s)|off
RewriteCond http%1://%{HTTP_HOST} ^(https?://)(www\.)?(.+)$
RewriteRule ^ %1%3%{REQUEST_URI} [R=301,L]
```

### 强制使用 HTTPS
``` apacheconf
RewriteEngine on
RewriteCond %{HTTPS} !on
RewriteRule (.*) https://%{HTTP_HOST}%{REQUEST_URI}

# Note: It’s also recommended to enable HTTP Strict Transport Security (HSTS)
# on your HTTPS website to help prevent man-in-the-middle attacks.
# See https://developer.mozilla.org/en-US/docs/Web/Security/HTTP_strict_transport_security
<IfModule mod_headers.c>
    # Remove "includeSubDomains" if you don't want to enforce HSTS on all subdomains
    Header always set Strict-Transport-Security "max-age=31536000;includeSubDomains"
</IfModule>
```

### 强制在代理后面使用 HTTPS
如果您的服务器前面有一个执行 TLS 终止的代理，则非常有用。
``` apacheconf
RewriteCond %{HTTP:X-Forwarded-Proto} !https
RewriteRule (.*) https://%{HTTP_HOST}%{REQUEST_URI}
```

### 强制尾随斜杠
``` apacheconf
RewriteCond %{REQUEST_URI} /+[^\.]+$
RewriteRule ^(.+[^/])$ %{REQUEST_URI}/ [R=301,L]
```

### 删除尾部斜杠
此代码片段将以斜杠结尾的路径重定向到其非斜杠终止的对应路径（实际目录除外），例如`https://www.example.com/blog/` 到 `https://www.example.com/blog`。这对于 SEO 很重要，因为[建议](https://overit.com/blog/canonical-urls)为每个页面都有一个规范的 URL。
``` apacheconf
RewriteCond %{REQUEST_FILENAME} !-d
RewriteCond %{REQUEST_URI} (.+)/$
RewriteRule ^ %1 [R=301,L]
```
[来源](https://stackoverflow.com/questions/21417263/htaccess-add-remove-trailing-slash-from-url#27264788)

### 重定向单个页面
``` apacheconf
Redirect 301 /oldpage.html https://www.example.com/newpage.html
Redirect 301 /oldpage2.html https://www.example.com/folder/
```
[来源](https://css-tricks.com/snippets/htaccess/301-redirects/)

### 使用 RedirectMatch 重定向
``` apacheconf
RedirectMatch 301 /subdirectory(.*) https://www.newsite.com/newfolder/$1
RedirectMatch 301 ^/(.*).htm$ /$1.html
RedirectMatch 301 ^/200([0-9])/([^01])(.*)$ /$2$3
RedirectMatch 301 ^/category/(.*)$ /$1
RedirectMatch 301 ^/(.*)/htaccesselite-ultimate-htaccess-article.html(.*) /htaccess/htaccess.html
RedirectMatch 301 ^/(.*).html/1/(.*) /$1.html$2
RedirectMatch 301 ^/manual/(.*)$ https://www.php.net/manual/$1
RedirectMatch 301 ^/old-directory/(.*)$ /new-directory/$1
RedirectMatch 301 ^/z/(.*)$ https://static.askapache.com/$1
```
[来源](https://www.askapache.com/htaccess/301-redirect-with-mod_rewrite-or-redirectmatch.html#301_Redirects_RedirectMatch)

### 给单个目录起别名
``` apacheconf
RewriteEngine On
RewriteRule ^source-directory/(.*) /target-directory/$1 [R=301,L]
```

### 脚本的别名路径
``` apacheconf
FallbackResource /index.fcgi
```
此示例在某个目录中有一个“index.fcgi”文件，该目录中无法解析文件名/目录的任何请求都将被发送到“index.fcgi”脚本。如果您希望“baz.foo/some/cool/path”由“baz.foo/index.fcgi”（也支持对“baz.foo”的请求）处理，同时维护“baz.foo/css/style.css”等，那么这是很好的选择。从 PATH_INFO 环境变量访问原始路径，该路径暴露于脚本环境。

``` apacheconf
RewriteEngine On
RewriteRule ^$ index.fcgi/ [QSA,L]
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule ^(.*)$ index.fcgi/$1 [QSA,L]
```
这是 FallbackResource 指令的效率较低的版本（因为使用 mod_rewrite 比仅仅处理 FallbackResource 指令更复杂），但它也更灵活。

### 重定向整个站点
``` apacheconf
Redirect 301 / https://newsite.com/
```
通过这种方式可以保持链接完好无损。即“www.oldsite.com/some/crazy/link.html”将变为“www.newsite.com/some/crazy/link.html”。当您只是将站点“移动”到新域时，这非常有用。 [来源](https://css-tricks.com/snippets/htaccess/301-redirects/)

### 别名“干净”URL
此代码片段允许您使用“干净”的 URL——那些没有 PHP 扩展名的 URL，例如`example.com/users` 而不是 `example.com/users.php`。
``` apacheconf
RewriteEngine On
RewriteCond %{SCRIPT_FILENAME} !-d
RewriteRule ^([^.]+)$ $1.php [NC,L]
```
[来源](https://www.abeautifulsite.net/access-pages-without-the-php-extension-using-htaccess/)

### 从重定向中排除 URL
此代码片段允许您从重定向中排除 URL。  例如，如果您设置了重定向规则，但想要排除 robots.txt，以便搜索引擎可以按预期访问该 URL。
``` apacheconf
RewriteEngine On
RewriteRule ^robots.txt - [L]
```

## 安全性
### 拒绝所有访问
``` apacheconf
Require all denied
```

但是等等，这也会将您锁定在内容之外！因此介绍...

### 拒绝除您之外的所有访问
``` apacheconf
Require all denied
Require ip xxx.xxx.xxx.xxx
```
`xxx.xxx.xxx.xxx` 是您的 IP。例如，如果您将最后三位数字替换为“0/12”，这将指定同一网络内的 IP 范围，从而省去了单独列出所有允许的 IP 的麻烦。 [来源](https://speckyboy.com/2013/01/08/useful-htaccess-snippets-and-hacks/)

现在当然有一个相反的版本：

### 允许除垃圾邮件发送者之外的所有访问
``` apacheconf
Require all granted
Require not ip xxx.xxx.xxx.xxx
Require not ip xxx.xxx.xxx.xxy
```

### 拒绝访问隐藏文件和目录
隐藏文件和目录（名称以点“.”开头的文件和目录）在大多数情况下（如果不是全部的话）应该受到保护。例如：`.htaccess`、`.htpasswd`、`.git`、`.hg`...
``` apacheconf
RewriteCond %{SCRIPT_FILENAME} -d [OR]
RewriteCond %{SCRIPT_FILENAME} -f
RewriteRule "(^|/)\." - [F]
```

或者，您可以直接引发“Not Found”错误，让攻击者没有任何线索：
``` apacheconf
RedirectMatch 404 /\..*$
```

### 拒绝访问备份和源文件
这些文件可能是某些文本/HTML 编辑器（如 Vi/Vim）留下的，如果暴露给公众，会带来很大的安全危险。
``` apacheconf
<FilesMatch "(\.(bak|config|dist|fla|inc|ini|log|psd|sh|sql|swp)|~)$">
    Require all denied
</FilesMatch>
```
[来源](https://github.com/h5bp/server-configs-apache)

### 禁用目录浏览
``` apacheconf
Options All -Indexes
```

### 禁用图像盗链
``` apacheconf
RewriteEngine on
# Remove the following line if you want to block blank referrer too
RewriteCond %{HTTP_REFERER} !^$

RewriteCond %{HTTP_REFERER} !^https?://(.+\.)?example.com [NC]
RewriteRule \.(jpe?g|png|gif|bmp|webp|avif|svg|ico)$ - [NC,F,L]

# If you want to display a “blocked” banner in place of the hotlinked image,
# replace the above rule with:
# RewriteRule \.(jpe?g|png|gif|bmp|webp|avif|svg|ico) https://example.com/blocked.png [R,L]
```

### 禁用特定域的图像盗链
有时您只想禁用某些坏人的图像盗链。
``` apacheconf
RewriteEngine on
RewriteCond %{HTTP_REFERER} ^https?://(.+\.)?badsite\.com [NC,OR]
RewriteCond %{HTTP_REFERER} ^https?://(.+\.)?badsite2\.com [NC,OR]
RewriteRule \.(jpe?g|png|gif|bmp|webp|avif|svg|ico)$ - [NC,F,L]

# If you want to display a “blocked” banner in place of the hotlinked image,
# replace the above rule with:
# RewriteRule \.(jpe?g|png|gif|bmp|webp|avif|svg|ico) https://example.com/blocked.png [R,L]
```

### 密码保护目录
首先，您需要在系统中的某个位置创建一个“.htpasswd”文件：
``` bash
htpasswd -c /home/fellowship/.htpasswd boromir
```

然后您可以使用它进行身份验证：
``` apacheconf
AuthType Basic
AuthName "One does not simply"
AuthUserFile /home/fellowship/.htpasswd
Require valid-user
```

### 密码保护一个或多个文件
``` apacheconf
AuthName "One still does not simply"
AuthType Basic
AuthUserFile /home/fellowship/.htpasswd

<Files "one-ring.o">
Require valid-user
</Files>

<FilesMatch ^((one|two|three)-rings?\.o)$>
Require valid-user
</FilesMatch>
```

### 按推荐人阻止访客
这会拒绝来自特定域（由特定域引用）的所有用户的访问。
[来源](https://www.htaccess-guide.com/deny-visitors-by-referrer/)
``` apacheconf
RewriteEngine on
# Options +FollowSymlinks
RewriteCond %{HTTP_REFERER} somedomain\.com [NC,OR]
RewriteCond %{HTTP_REFERER} anotherdomain\.com
RewriteRule .* - [F]
```

### 阻止特定用户代理
这将阻止特定的用户代理访问您的网站，这对于阻止抓取工具和恶意机器人很有用。
``` apacheconf
RewriteEngine on
RewriteCond %{HTTP_USER_AGENT} BadBot [NC,OR]
RewriteCond %{HTTP_USER_AGENT} EvilScraper [NC]
RewriteRule .* - [F,L]
```

### 防止框架网站
这可以防止网站被框架（即放入“iframe”标签中），同时仍然允许针对特定 URI 框架。
``` apacheconf
SetEnvIf Request_URI "/starry-night" allow_framing=true
Header set X-Frame-Options SAMEORIGIN env=!allow_framing
```

### 内容安全策略 (CSP)
内容安全策略标头通过声明允许加载哪些动态资源来帮助减轻跨站点脚本 (XSS) 和其他代码注入攻击。
``` apacheconf
<IfModule mod_headers.c>
    Header set Content-Security-Policy "default-src 'self'; script-src 'self'; style-src 'self'"
</IfModule>
```
调整指令以满足您的需求。有关所有可用指令，请参阅 [CSP 参考](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy)。

### 防止 MIME 类型嗅探
这可以防止浏览器尝试猜测（“嗅探”）资源的 MIME 类型，这可能会产生安全隐患。浏览器将信任服务器所说的内容，并在资源与预期类型不匹配时阻止该资源。
``` apacheconf
<IfModule mod_headers.c>
    Header set X-Content-Type-Options "nosniff"
</IfModule>
```

### 设置推荐人政策
控制请求中包含多少引用者信息。这有助于防止完整 URL 泄露到外部站点，从而保护用户隐私。
``` apacheconf
<IfModule mod_headers.c>
    Header set Referrer-Policy "strict-origin-when-cross-origin"
</IfModule>
```

### 设置权限策略
限制您的网站可以使用哪些浏览器功能，例如摄像头、麦克风、地理位置等。
``` apacheconf
<IfModule mod_headers.c>
    Header set Permissions-Policy "camera=(), microphone=(), geolocation=(), interest-cohort=()"
</IfModule>
```

### 删除服务器签名
防止 Apache 在 HTTP 标头和错误页面中公开其版本号和操作系统信息。
``` apacheconf
ServerSignature Off
```

## 性能
### 压缩文本文件
``` apacheconf
<IfModule mod_deflate.c>

    # Force compression for mangled headers.
    # https://developer.yahoo.com/blogs/ydn/pushing-beyond-gzipping-25601.html
    <IfModule mod_setenvif.c>
        <IfModule mod_headers.c>
            SetEnvIfNoCase ^(Accept-EncodXng|X-cept-Encoding|X{15}|~{15}|-{15})$ ^((gzip|deflate)\s*,?\s*)+|[X~-]{4,13}$ HAVE_Accept-Encoding
            RequestHeader append Accept-Encoding "gzip,deflate" env=HAVE_Accept-Encoding
        </IfModule>
    </IfModule>

    # Compress all output labeled with one of the following MIME-types
    # (mod_filter is required for Apache 2.4)
    <IfModule mod_filter.c>
        AddOutputFilterByType DEFLATE application/atom+xml \
                                      application/javascript \
                                      application/json \
                                      application/rss+xml \
                                      application/x-font-ttf \
                                      application/x-web-app-manifest+json \
                                      application/xhtml+xml \
                                      application/xml \
                                      font/opentype \
                                      image/svg+xml \
                                      image/x-icon \
                                      text/css \
                                      text/html \
                                      text/plain \
                                      text/xml
    </IfModule>

</IfModule>
```
[来源](https://github.com/h5bp/server-configs-apache)


### 设置过期标头
_Expires headers_告诉浏览器是否应该从服务器请求特定文件或只是从缓存中获取它。建议将静态内容的过期标头设置为遥远的未来。

如果您不使用基于文件名的缓存清除来控制版本控制，请考虑将 CSS 和 JS 等资源的缓存时间降低到 1 周左右。 [来源](https://github.com/h5bp/server-configs-apache)
``` apacheconf
<IfModule mod_expires.c>
    ExpiresActive on
    ExpiresDefault                                      "access plus 1 month"

  # CSS
    ExpiresByType text/css                              "access plus 1 year"

  # Data interchange
    ExpiresByType application/json                      "access plus 0 seconds"
    ExpiresByType application/xml                       "access plus 0 seconds"
    ExpiresByType text/xml                              "access plus 0 seconds"

  # Favicon (cannot be renamed!)
    ExpiresByType image/x-icon                          "access plus 1 week"

  # HTML
    ExpiresByType text/html                             "access plus 0 seconds"

  # JavaScript
    ExpiresByType application/javascript                "access plus 1 year"

  # Manifest files
    ExpiresByType application/x-web-app-manifest+json   "access plus 0 seconds"

  # Media
    ExpiresByType audio/ogg                             "access plus 1 month"
    ExpiresByType image/gif                             "access plus 1 month"
    ExpiresByType image/jpeg                            "access plus 1 month"
    ExpiresByType image/png                             "access plus 1 month"
    ExpiresByType video/mp4                             "access plus 1 month"
    ExpiresByType video/ogg                             "access plus 1 month"
    ExpiresByType video/webm                            "access plus 1 month"

  # Web feeds
    ExpiresByType application/atom+xml                  "access plus 1 hour"
    ExpiresByType application/rss+xml                   "access plus 1 hour"

  # Web fonts
    ExpiresByType application/font-woff2                "access plus 1 month"
    ExpiresByType application/font-woff                 "access plus 1 month"
    ExpiresByType application/x-font-ttf                "access plus 1 month"
    ExpiresByType font/opentype                         "access plus 1 month"
    ExpiresByType image/svg+xml                         "access plus 1 month"
</IfModule>
```

### 设置缓存控制标头
“Cache-Control”标头比 Expires 标头提供对浏览器缓存更细粒度的控制。您可以将两者一起使用以获得最大的兼容性。
``` apacheconf
<IfModule mod_headers.c>
    # Cache CSS and JS for 1 year
    <FilesMatch "\.(css|js)$">
        Header set Cache-Control "max-age=31536000, public"
    </FilesMatch>

    # Cache images for 1 month
    <FilesMatch "\.(jpe?g|png|gif|webp|avif|svg|ico)$">
        Header set Cache-Control "max-age=2592000, public"
    </FilesMatch>

    # Cache fonts for 1 month
    <FilesMatch "\.(woff2?|ttf|otf)$">
        Header set Cache-Control "max-age=2592000, public"
    </FilesMatch>

    # Do not cache HTML
    <FilesMatch "\.(html|htm)$">
        Header set Cache-Control "no-cache, no-store, must-revalidate"
    </FilesMatch>
</IfModule>
```

### 关闭电子标签
通过删除“ETag”标头，您将禁用缓存和浏览器验证文件的能力，因此它们被迫依赖您的“Cache-Control”和“Expires”标头。 [来源](https://www.askapache.com/htaccess/apache-speed-etags.html)
``` apacheconf
<IfModule mod_headers.c>
    Header unset ETag
</IfModule>
FileETag None
```

## 杂项

### 设置 PHP 变量
``` apacheconf
php_value <key> <val>

# For example:
php_value upload_max_filesize 50M
php_value max_execution_time 240
```

### 自定义错误页面
``` apacheconf
ErrorDocument 500 "Houston, we have a problem."
ErrorDocument 401 https://error.example.com/mordor.html
ErrorDocument 404 /errors/halflife3.html
```

### 自定义维护页面
将所有流量重定向到维护页面，同时仍然允许从特定 IP 地址进行访问。
``` apacheconf
RewriteEngine on
RewriteCond %{REMOTE_ADDR} !^xxx\.xxx\.xxx\.xxx
RewriteCond %{REQUEST_URI} !/maintenance.html$ [NC]
RewriteCond %{REQUEST_URI} !\.(css|js|png|jpe?g|gif|svg|ico)$ [NC]
RewriteRule .* /maintenance.html [R=503,L]
```
将 `xxx.xxx.xxx.xxx` 替换为您的 IP 地址，以便在站点维护期间保留访问权限。

### 强制下载
有时您想强制浏览器下载某些内容而不是显示它。
``` apacheconf
<Files *.md>
    ForceType application/octet-stream
    Header set Content-Disposition attachment
</Files>
```

现在这个阴有一个阳：

### 阻止下载
有时您想强制浏览器显示某些内容而不是下载它。
``` apacheconf
<FilesMatch "\.(tex|log|aux)$">
    Header set Content-Type text/plain
</FilesMatch>
```

### 允许跨域字体
由于 [CORS](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing)，CDN 提供的网络字体可能无法在 Firefox 中工作。这段代码解决了这个问题。
``` apacheconf
<IfModule mod_headers.c>
    <FilesMatch "\.(otf|ttc|ttf|woff|woff2)$">
        Header set Access-Control-Allow-Origin "*"
    </FilesMatch>
</IfModule>
```
[来源](https://github.com/h5bp/server-configs-apache/issues/32)

### 启用跨域资源共享
为您的站点启用跨源资源共享 (CORS)，允许其他域向您的服务器发出请求。
``` apacheconf
<IfModule mod_headers.c>
    Header set Access-Control-Allow-Origin "*"
    Header set Access-Control-Allow-Methods "GET, POST, PUT, DELETE, OPTIONS"
    Header set Access-Control-Allow-Headers "Content-Type, Authorization"
</IfModule>
```
要限制对特定域的访问，请将“*”替换为域，例如`https://example.com`。

### 自动 UTF-8 编码
您的文本内容应该始终采用 UTF-8 编码，不是吗？
``` apacheconf
# Use UTF-8 encoding for anything served text/plain or text/html
AddDefaultCharset utf-8

# Force UTF-8 for a number of file formats
AddCharset utf-8 .atom .css .js .json .rss .vtt .xml
```
[来源](https://github.com/h5bp/server-configs-apache)

### 设置自定义 MIME 类型
为 Apache 默认情况下可能无法识别的文件格式定义自定义 MIME 类型。
``` apacheconf
AddType application/manifest+json .webmanifest
AddType application/wasm .wasm
AddType application/x-ndjson .ndjson
AddType text/vtt .vtt
```

### 切换到另一个 PHP 版本
如果您使用的是共享主机，则可能会安装多个版本的 PHP，有时您需要为您的网站安装特定版本。以下代码片段应该为您切换 PHP 版本。

``` apacheconf
AddHandler application/x-httpd-php84 .php

# Alternatively, you can use AddType
AddType application/x-httpd-php84 .php
```

### 提供 WebP/AVIF 图像
如果原始 jpg/png 旁边存在同名的现代格式图像（AVIF 或 WebP），则将改为提供该图像。当浏览器同时支持 AVIF 和 WebP 时，AVIF 优先于 WebP。

``` apacheconf
RewriteEngine On

# Serve AVIF if supported and available
RewriteCond %{HTTP_ACCEPT} image/avif
RewriteCond %{DOCUMENT_ROOT}/$1.avif -f
RewriteRule (.+)\.(jpe?g|png)$ $1.avif [T=image/avif,E=accept:1]

# Otherwise, serve WebP if supported and available
RewriteCond %{HTTP_ACCEPT} image/webp
RewriteCond %{DOCUMENT_ROOT}/$1.webp -f
RewriteRule (.+)\.(jpe?g|png)$ $1.webp [T=image/webp,E=accept:1]
```
