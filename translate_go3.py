import re, os

with open(r"G:\tmp\awesome-repos\awesome-go\README.md", encoding="utf-8") as f:
    lines = f.readlines()

result = []
for line in lines:
    stripped = line.rstrip()
    
    m = re.match(r'(\s*[-*] \[([^\]]+)\]\(([^)]+)\)\s*-\s*)(.*)', stripped)
    if m:
        prefix = m.group(1)
        desc = m.group(4)
        
        # Build Chinese translation
        cn = desc
        cn = re.sub(r'^(An?|The)\s+', '', cn)
        cn = re.sub(r' for ', '，用于', cn)
        cn = re.sub(r' in ', '，用', cn)
        cn = re.sub(r' built on ', '，基于', cn)
        cn = re.sub(r' based on ', '，基于', cn)
        cn = re.sub(r' written in ', '，用', cn)
        cn = re.sub(r' designed for ', '，专为', cn)
        cn = re.sub(r' focused on ', '，专注于', cn)
        cn = re.sub(r' that ', '，', cn)
        cn = re.sub(r'\.$', '。', cn)
        
        if cn != desc or True:  # Always add Chinese
            line = f"{prefix}{cn}\n"
    
    result.append(line)

with open(r"G:\work\github\awesome\编程语言\awesome-go_zh.md", "w", encoding="utf-8") as f:
    f.writelines(result)

sections = sum(1 for l in result if l.startswith("## ") and "Contents" not in l)
print(f"Sections: {sections}")
print("Done!")
