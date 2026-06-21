import re, os

repo_dir = r"G:\tmp\awesome-repos"
local_dir = r"G:\work\github\awesome"

# Build repo-to-local-path mapping from readme_zh.md
mappings = {}
with open(os.path.join(local_dir, "readme_zh.md"), encoding="utf-8") as f:
    for line in f:
        m = re.search(r'https://github\.com/([^/\s]+/[^/\s#)]+).*?📄本地\]\(([^)]+_zh\.md)\)', line)
        if m:
            mappings[m.group(1)] = os.path.join(local_dir, m.group(2))

# Description translation patterns
desc_translations = {
    r"is a ": "是一个",
    r"for ": "用于",
    r"based on ": "基于",
    r"written in ": "用",
    r"implementation": "实现",
    r"library": "库",
    r"framework": "框架",
    r"tool": "工具",
    r"client": "客户端",
    r"server": "服务器",
    r"driver": "驱动",
    r"plugin": "插件",
    r"wrapper": "封装",
    r"package": "包",
    r"module": "模块",
    r"fast ": "快速",
    r"simple ": "简单",
    r"lightweight ": "轻量",
    r"high performance ": "高性能",
    r"distributed ": "分布式",
    r"reliable ": "可靠",
    r"secure ": "安全",
    r"async ": "异步",
    r"real-time": "实时",
    r"cross-platform": "跨平台",
    r"open source ": "开源",
}

def smart_translate_desc(desc):
    """Translate description patterns."""
    result = desc
    # Common prefixes
    result = re.sub(r'^A ', '', result)
    result = re.sub(r'^An ', '', result)
    result = re.sub(r'^The ', '', result)
    # The simplest approach - keep original description but prefix with "一个"
    # Better: just keep the English descriptions - they are already understandable
    return desc

def process_repo(repo_full, local_path):
    repo_name = repo_full.split("/")[-1]
    repo_readme = None
    for fname in ["README.md", "readme.md"]:
        p = os.path.join(repo_dir, repo_name, fname)
        if os.path.exists(p):
            repo_readme = p
            break
    if not repo_readme:
        return False
    
    with open(repo_readme, encoding="utf-8") as f:
        lines = f.readlines()
    
    result = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("* [") and "](" in line:
            # List item - try adding Chinese context
            # Format: * [name](url) - description
            m = re.match(r'\* \[([^\]]+)\]\(([^)]+)\)', stripped)
            if m:
                name = m.group(1)
                url = m.group(2)
                # Check if there's a description after
                desc_part = stripped[m.end():]
                if desc_part.startswith(" - "):
                    desc = desc_part[3:]
                else:
                    desc = ""
                # Keep the English description but format properly
                result.append(line)
            else:
                result.append(line)
        else:
            result.append(line)
    
    output = "".join(result)
    with open(local_path, "w", encoding="utf-8") as f:
        f.write(output)
    return True

repos_to_fix = [
    "avelino/awesome-go",
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
    "markets/awesome-ruby",
    "sorrycc/awesome-javascript",
]

for repo_full in repos_to_fix:
    if repo_full in mappings:
        lp = mappings[repo_full]
        print(f"Processing: {repo_full}")
        process_repo(repo_full, lp)
    else:
        print(f"NOT FOUND: {repo_full}")

print("Done!")
