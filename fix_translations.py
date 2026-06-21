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

# Common English-to-Chinese description translations
desc_map = {
    "A curated list of awesome": "精选的",
    "curated list of awesome": "精选的",
    "A curated list of": "精选的",
    "curated list of": "精选的",
    "Useful resources for": "有用的资源",
    "A curated collection of": "精选合集",
}

def translate_desc(desc):
    """Translate common description patterns to Chinese."""
    for eng, chn in desc_map.items():
        if desc.startswith(eng):
            return desc.replace(eng, chn, 1)
    return desc

def process(filepath):
    """Read file and translate description prefixes."""
    with open(filepath, encoding="utf-8") as f:
        content = f.read()
    
    lines = content.split("\n")
    new_lines = []
    for line in lines:
        new_lines.append(line)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(new_lines))

# Process already-copied files for the ones with original English content
repos_fixed = [
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

for repo in repos_fixed:
    if repo in mappings:
        lp = mappings[repo]
        process(lp)
        print(f"Processed: {repo}")

print("Done!")
