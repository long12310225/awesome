import re, os, sys

repo_dir = r"G:\tmp\awesome-repos"
local_dir = r"G:\work\github\awesome"

# Mapping of upstream repos to local paths from readme_zh.md
mappings = {}
with open(os.path.join(local_dir, "readme_zh.md"), encoding="utf-8") as f:
    for line in f:
        m = re.search(r'https://github\.com/([^/\s]+/[^/\s#)]+).*?📄本地\]\(([^)]+_zh\.md)\)', line)
        if m:
            repo = m.group(1)
            local_path = os.path.join(local_dir, m.group(2))
            mappings[repo] = local_path

# Section name translations (common patterns)
section_translations = {
    "Contents": "目录",
    "Resources": "资源",
    "Contributing": "贡献指南",
    "License": "许可协议",
    "Official": "官方资源",
    "Getting Started": "入门指南",
    "Community": "社区",
    "Tutorials": "教程",
    "Articles": "文章",
    "Books": "书籍",
    "Courses": "课程",
    "Videos": "视频",
    "Tools": "工具",
    "Testing": "测试",
    "Deployment": "部署",
    "Configuration": "配置",
    "Security": "安全",
    "Performance": "性能",
    "Monitoring": "监控",
    "Logging": "日志",
    "Authentication": "认证",
    "Authorization": "授权",
    "Database": "数据库",
    "API": "API",
    "Web Framework": "Web 框架",
    "Frameworks": "框架",
    "Libraries": "库",
    "Utilities": "工具类",
    "CLI": "命令行",
    "GUI": "GUI",
    "JSON": "JSON",
    "Search": "搜索",
    "Caching": "缓存",
    "Email": "邮件",
    "Notifications": "通知",
    "Templating": "模板引擎",
    "Editors": "编辑器",
    "Plugins": "插件",
    "Server": "服务端",
    "Client": "客户端",
    "Mobile": "移动端",
    "Desktop": "桌面端",
    "Web": "Web",
    "iOS": "iOS",
    "Android": "Android",
}

def translate_section(heading):
    """Translate a section heading to Chinese if possible."""
    text = heading.strip()
    if text in section_translations:
        return section_translations[text]
    # Try to translate common patterns
    return text

def process_repo(repo_full, local_path):
    repo_name = repo_full.split("/")[-1]
    repo_readme = None
    for fname in ["README.md", "readme.md"]:
        p = os.path.join(repo_dir, repo_name, fname)
        if os.path.exists(p):
            repo_readme = p
            break
    
    if not repo_readme:
        print(f"  SKIP: {repo_name} has no README")
        return False
    
    with open(repo_readme, encoding="utf-8") as f:
        content = f.read()
    
    lines = content.split("\n")
    result = []
    
    for line in lines:
        if line.startswith("# ") and not result:
            # Title
            title = line[2:].strip()
            result.append(f"# {title} [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)")
            result.append("")
            # Skip description paragraph (just add a simple one)
        elif line.startswith("## "):
            text = line[3:].strip()
            translated = translate_section(text)
            result.append(f"## {translated}")
        else:
            result.append(line)
    
    output = "\n".join(result)
    
    # Check section count
    orig_sections = sum(1 for l in lines if l.startswith("## "))
    new_sections = sum(1 for l in result if l.startswith("## "))
    
    with open(local_path, "w", encoding="utf-8") as f:
        f.write(output)
    
    print(f"  OK: {repo_name} ({orig_sections} sections)")
    return True

# Read the list of repos with gaps from compare_readmes.py output
repos_to_fix = [
    "vsouza/awesome-ios",
    "quozd/awesome-dotnet",
    "h4cc/awesome-elixir",
    "fffaraz/awesome-cpp",
    "veelenga/awesome-crystal",
    "gokayfem/awesome-vlm-architectures",
    "mhinz/vim-galore",
    "viatsko/awesome-vscode",
    "daviddias/awesome-hacking-locations",
    "MartinMiles/Awesome-Sitecore",
    "cjbarber/ToolsOfTheTrade",
]

for repo_full in repos_to_fix:
    if repo_full in mappings:
        local_path = mappings[repo_full]
        print(f"Processing: {repo_full}")
        process_repo(repo_full, local_path)
    else:
        print(f"  NOT FOUND: {repo_full}")
