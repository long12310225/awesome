import re, os

repo_dir = r"G:\tmp\awesome-repos"
local_dir = r"G:\work\github\awesome"

# Build mapping from readme_zh.md
mappings = {}
with open(os.path.join(local_dir, "readme_zh.md"), encoding="utf-8") as f:
    for line in f:
        m = re.search(r'https://github\.com/([^/\s]+/[^/\s#)]+).*?📄本地\]\(([^)]+_zh\.md)\)', line)
        if m:
            mappings[m.group(1)] = os.path.join(local_dir, m.group(2))

def translate_file(upstream_path, output_path):
    with open(upstream_path, encoding="utf-8") as f:
        lines = f.readlines()
    
    result = []
    for line in lines:
        stripped = line.rstrip()
        m = re.match(r'(\s*[-*] \[([^\]]+)\]\(([^)]+)\)\s*-\s*)(.*)', stripped)
        if m:
            prefix = m.group(1)
            desc = m.group(4)
            cn = desc
            cn = re.sub(r'^(An?|The)\s+', '', cn)
            cn = re.sub(r' for ', '，用于', cn)
            cn = re.sub(r' in ', '，用', cn)
            cn = re.sub(r' built on ', '，基于', cn)
            cn = re.sub(r' based on ', '，基于', cn)
            cn = re.sub(r' written in ', '，用', cn)
            cn = re.sub(r' designed to ', '，旨在', cn)
            cn = re.sub(r' designed for ', '，专为', cn)
            cn = re.sub(r' focused on ', '，专注于', cn)
            cn = re.sub(r' that ', '，', cn)
            cn = re.sub(r' which ', '，', cn)
            cn = re.sub(r' inspired by ', '，灵感来自', cn)
            cn = re.sub(r'\.$', '。', cn)
            line = f"{prefix}{cn}\n"
        result.append(line)
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.writelines(result)

big_repos = [
    "vsouza/awesome-ios",
    "quozd/awesome-dotnet",
    "h4cc/awesome-elixir",
    "fffaraz/awesome-cpp",
    "veelenga/awesome-crystal",
    "gokayfem/awesome-vlm-architectures",
    "mhinz/vim-galore",
    "viatsko/awesome-vscode",
    "MartinMiles/Awesome-Sitecore",
    "cjbarber/ToolsOfTheTrade",
    "markets/awesome-ruby",
    "sorrycc/awesome-javascript",
]

for repo in big_repos:
    if repo not in mappings:
        print(f"SKIP: {repo} (not in mappings)")
        continue
    
    repo_name = repo.split("/")[-1]
    upstream = None
    for fn in ["README.md", "readme.md"]:
        p = os.path.join(repo_dir, repo_name, fn)
        if os.path.exists(p):
            upstream = p
            break
    
    if not upstream:
        print(f"SKIP: {repo} (no README)")
        continue
    
    output = mappings[repo]
    translate_file(upstream, output)
    sections = sum(1 for l in open(output, encoding="utf-8") if l.startswith("## ") and "Contents" not in l)
    print(f"OK: {repo} ({sections} sections)")

print("Done!")
