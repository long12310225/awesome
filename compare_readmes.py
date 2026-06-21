import re, os

readme_path = r"G:\work\github\awesome\readme_zh.md"
local_dir = r"G:\work\github\awesome"
repos_dir = r"G:\tmp\awesome-repos"

with open(readme_path, encoding="utf-8") as f:
    content = f.read()

# Extract: repo_url -> local_path
entries = re.findall(
    r'https://github\.com/([^/\s]+/[^/\s#)]+).*?📄本地\]\(([^)]+_zh\.md)\)',
    content
)

def get_readme(repo_dir):
    for fname in ["README.md", "readme.md", "Readme.md"]:
        p = os.path.join(repo_dir, fname)
        if os.path.exists(p):
            return p
    return None

def count_heading2(fpath):
    try:
        with open(fpath, encoding="utf-8") as f:
            return sum(1 for line in f if line.startswith("## "))
    except:
        return 0

print(f"{'Local File':65s} {'Local Sz':>8s} {'Local H2':>7s} | {'Repo H2':>7s} {'Status':>10s}")
print("="*100)

gaps = []
for repo_full, local_rel in entries:
    local_path = os.path.join(local_dir, local_rel)
    repo_name = repo_full.split("/")[-1]
    repo_dir = os.path.join(repos_dir, repo_name)
    
    if not os.path.exists(local_path):
        continue
    
    local_size = os.path.getsize(local_path)
    local_h2 = count_heading2(local_path)
    
    readme = get_readme(repo_dir)
    if not readme:
        continue
    
    repo_h2 = count_heading2(readme)
    gap = repo_h2 - local_h2
    
    if gap >= 10:
        status = f"GAP={gap}"
        gaps.append((gap, local_rel, repo_full))
    else:
        status = "OK"
    
    print(f"{local_rel:65s} {local_size:>8d} {local_h2:>7d} | {repo_h2:>7d} {status:>10s}")

print(f"\n\n=== SUMMARY ===")
print(f"Total checked: {len(gaps)} repos with gap >= 10")
gaps.sort(reverse=True)
for gap, path, repo in gaps:
    print(f"  {repo}: {path} (gap={gap})")
