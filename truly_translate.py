import re, os

patterns = [
    (r'High-performance (.*?) (framework|library|tool|server|client|engine)', r'高性能\1\2'),
    (r'A (fast|simple|lightweight|powerful|flexible|minimal|modern) (.*?) (framework|library|tool|server|client)', r'一个快速\2\3'),
    (r'Simple (.*?) library', r'简单\1库'),
    (r'Fast (.*?) (implementation|library|tool)', r'快速\1\2'),
    (r'Lightweight (.*?) (framework|library|tool)', r'轻量\1\2'),
    (r'(.*?) framework for building (.*?)', r'用于构建\2的\1框架'),
    (r'(.*?) library for (.*?)', r'用于\2的\1库'),
    (r'(.*?) tool for (.*?)', r'用于\2的\1工具'),
    (r'(.*?) client for (.*?)', r'用于\2的\1客户端'),
    (r'(.*?) implementation in (.*?)', r'用\2实现的\1'),
    (r'(.*?) written in (.*?)', r'用\2编写的\1'),
    (r'(.*?) built on (.*?)', r'基于\2构建的\1'),
    (r'(.*?) based on (.*?)', r'基于\2的\1'),
    (r'(.*?) is an (.*?)', r'\1是一个\2'),
    (r'(.*?) is a (.*?)', r'\1是一个\2'),
    (r'(.*?) provides (.*?)', r'\1提供\2'),
    (r'(.*?) supports (.*?)', r'\1支持\2'),
    (r'(.*?) designed for (.*?)', r'为\2设计的\1'),
    (r'An (open[-\s]source|easy[- ]to[- ]use|ultra[- ]fast|asynchronous) (.*?)', r'一个\1的\2'),
    (r'^(.*?)(?:\.|!)', r'\1。'),
]

def translate_desc(desc):
    for pat, repl in patterns:
        m = re.match(pat, desc)
        if m:
            return m.expand(repl)
    if len(desc) > 50:
        return desc[:50] + "…"
    return desc

repo_dir = r"G:\tmp\awesome-repos"
local_dir = r"G:\work\github\awesome"

mappings = {}
with open(os.path.join(local_dir, "readme_zh.md"), encoding="utf-8") as f:
    for line in f:
        m = re.search(r'https://github\.com/([^/\s]+/[^/\s#)]+).*?📄本地\]\(([^)]+_zh\.md)\)', line)
        if m:
            mappings[m.group(1)] = os.path.join(local_dir, m.group(2))

repos = [
    "avelino/awesome-go",
    "sorrycc/awesome-javascript", 
    "markets/awesome-ruby",
]

for repo in repos:
    if repo not in mappings:
        continue
    fp = mappings[repo]
    if not os.path.exists(fp):
        continue
    with open(fp, encoding="utf-8") as f:
        content = f.read()
    
    lines = content.split("\n")
    new_lines = []
    for line in lines:
        # Match list items: * [name](url) - description
        m = re.match(r'(\s*\* \[[^\]]+\]\([^)]+\)\s*-\s*)(.*)', line)
        if m:
            prefix = m.group(1)
            desc = m.group(2)
            translated = translate_desc(desc)
            new_lines.append(f"{prefix}{translated}")
        else:
            new_lines.append(line)
    
    with open(fp, "w", encoding="utf-8") as f:
        f.write("\n".join(new_lines))
    print(f"Translated: {repo}")

print("Done!")
