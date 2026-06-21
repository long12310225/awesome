import re, os

repo_dir = r"G:\tmp\awesome-repos"
local_dir = r"G:\work\github\awesome"

# Build mapping
mappings = {}
with open(os.path.join(local_dir, "readme_zh.md"), encoding="utf-8") as f:
    for line in f:
        m = re.search(r'https://github\.com/([^/\s]+/[^/\s#)]+).*?📄本地\]\(([^)]+_zh\.md)\)', line)
        if m:
            mappings[m.group(1)] = os.path.join(local_dir, m.group(2))

# Comprehensive translation dictionary for common patterns
def translate_desc(desc):
    """Translate English description to Chinese."""
    d = desc.strip()
    if not d:
        return d
    
    # Direct phrase translations
    phrases = [
        ("A curated list of awesome", "精选的"),
        ("curated list of awesome", "精选的"),
        ("A curated collection of", "精选的"),
        
        # Library/Framework types
        ("library for", "库，用于"),
        ("framework for", "框架，用于"),
        ("tool for", "工具，用于"),
        ("client for", "客户端，用于"),
        ("server for", "服务器，用于"),
        ("package for", "包，用于"),
        ("module for", "模块，用于"),
        ("plugin for", "插件，用于"),
        ("driver for", "驱动，用于"),
        
        # Descriptions
        ("written in Go", "用 Go 编写"),
        ("written in Rust", "用 Rust 编写"),
        ("written in C", "用 C 编写"),
        ("written in Python", "用 Python 编写"),
        ("written in", "用"),
        ("based on", "基于"),
        ("built on", "构建于"),
        ("powered by", "由"),
        ("designed for", "专为"),
        ("designed to", "旨在"),
        ("focused on", "专注于"),
        ("inspired by", "灵感来自"),
        ("easy to use", "易于使用"),
        ("easy-to-use", "易于使用"),
        ("high performance", "高性能"),
        ("high-performance", "高性能"),
        ("lightweight", "轻量"),
        ("flexible", "灵活的"),
        ("cross-platform", "跨平台"),
        ("open source", "开源"),
        ("open-source", "开源"),
        
        # Verbs
        ("provides", "提供"),
        ("supports", "支持"),
        ("allows you to", "允许你"),
        ("enables you to", "使你能够"),
        ("helps you", "帮助你"),
        ("makes it easy to", "使"),
        
        # Connectors
        (" for ", "，用于"),
        (" in ", "，用"),
        (" with ", "，使用"),
        (" using ", "，使用"),
        (" via ", "，通过"),
        (" through ", "，通过"),
    ]
    
    for eng, chn in phrases:
        if eng in d:
            d = d.replace(eng, chn, 1) if len(eng) > 5 else d  # Only replace full phrases
    
    # Clean up
    d = re.sub(r'^(An?|The)\s+', '', d)
    d = d.strip()
    
    return d

def process_file(upstream_path, output_path):
    with open(upstream_path, encoding="utf-8") as f:
        lines = f.readlines()
    
    result = []
    for line in lines:
        stripped = line.rstrip()
        # List items: * [name](url) - description
        m = re.match(r'(\s*[-*] \[([^\]]+)\]\(([^)]+)\)\s*-\s*)(.*)', stripped)
        if m:
            prefix = m.group(1)
            desc = m.group(4)
            cn = translate_desc(desc)
            line = f"{prefix}{cn}\n"
        
        # Subsection headers: *...* 
        m2 = re.match(r'(\s*\*)(.*\*)(.*)', stripped)
        # Don't modify
        
        result.append(line)
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.writelines(result)

# Process ALL repos that have been cloned
count = 0
for repo_full, output_path in list(mappings.items())[:10]:  # First 10
    repo_name = repo_full.split("/")[-1]
    upstream = None
    for fn in ["README.md", "readme.md"]:
        p = os.path.join(repo_dir, repo_name, fn)
        if os.path.exists(p):
            upstream = p
            break
    if not upstream:
        continue
    
    process_file(upstream, output_path)
    sections = sum(1 for l in open(output_path, encoding="utf-8") if l.startswith("## "))
    count += 1
    print(f"[{count}] {repo_full} - {sections} sections")

print(f"\nProcessed {count} files")
