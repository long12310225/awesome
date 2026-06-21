import re, os

repo_dir = r"G:\tmp\awesome-repos"
local_dir = r"G:\work\github\awesome"

# Read upstream Go README
with open(os.path.join(repo_dir, "awesome-go", "README.md"), encoding="utf-8") as f:
    lines = f.readlines()

result = []
for line in lines:
    stripped = line.rstrip()
    
    # Process list items: * [name](url) - description
    m = re.match(r'(\s*\* \[([^\]]+)\]\(([^)]+)\)\s*-\s*)(.*)', stripped)
    if m:
        prefix = m.group(1)
        desc = m.group(4)
        # Translate common patterns in description
        desc_cn = desc
        desc_cn = re.sub(r'^A (.*) library for (.*)', r'用于\2的\1库', desc_cn)
        desc_cn = re.sub(r'^A (.*) framework for (.*)', r'用于\2的\1框架', desc_cn)
        desc_cn = re.sub(r'^A (.*) tool for (.*)', r'用于\2的\1工具', desc_cn)
        desc_cn = re.sub(r'^A (.*) implementation', r'\1实现', desc_cn)
        desc_cn = re.sub(r'^A (.*) client', r'\1客户端', desc_cn)
        desc_cn = re.sub(r'^A (.*) server', r'\1服务器', desc_cn)
        desc_cn = re.sub(r'^A (.*) engine', r'\1引擎', desc_cn)
        desc_cn = re.sub(r'^A (.*) wrapper', r'\1封装', desc_cn)
        desc_cn = re.sub(r'^The (.*) library', r'\1库', desc_cn)
        desc_cn = re.sub(r'^The (.*) framework', r'\1框架', desc_cn)
        desc_cn = re.sub(r'^Fast (.*) (library|tool|server)', r'快速\1\2', desc_cn)
        desc_cn = re.sub(r'^Simple (.*) (library|tool)', r'简单\1\2', desc_cn)
        desc_cn = re.sub(r'^Lightweight (.*) (library|tool)', r'轻量\1\2', desc_cn)
        desc_cn = re.sub(r'^High-performance (.*)', r'高性能\1', desc_cn)
        desc_cn = re.sub(r'^Blazingly fast (.*)', r'极快\1', desc_cn)
        desc_cn = re.sub(r'^Pure Go (.*)', r'纯 Go \1', desc_cn)
        desc_cn = re.sub(r' for (.*?)\.', r'，用于\1。', desc_cn)
        
        if desc_cn != desc:
            line = f"{prefix}{desc}（{desc_cn}）\n"
    
    result.append(line)

output_path = os.path.join(local_dir, "编程语言", "awesome-go_zh.md")
with open(output_path, "w", encoding="utf-8") as f:
    f.writelines(result)

# Count sections
sections = sum(1 for l in result if l.startswith("## ") and "Contents" not in l)
print(f"Sections: {sections}")
print("Done! Wrote to", output_path)
