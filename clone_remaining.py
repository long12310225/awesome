import re, os, subprocess, sys

with open(r"G:\work\github\awesome\readme_zh.md", encoding="utf-8") as f:
    content = f.read()

urls = re.findall(r'https://github\.com/([^/\s]+/[^/\s#)]+)', content)
all_repos = sorted(set(urls))

target = r"G:\tmp\awesome-repos"
existing = set(os.listdir(target))
remaining = [r for r in all_repos if r.split("/")[-1] not in existing]

print(f"Already cloned: {len(existing)}")
print(f"Remaining: {len(remaining)}")
print()

count = 0
failures = 0
for repo in remaining:
    count += 1
    name = repo.split("/")[-1]
    cmd = f'git -C "{target}" clone --depth 1 https://github.com/{repo}.git'
    print(f"[{count}/{len(remaining)}] {name}...", end=" ", flush=True)
    ret = subprocess.run(cmd, shell=True, capture_output=True, timeout=60)
    if ret.returncode == 0:
        print("OK")
    else:
        err = ret.stderr.decode()[:60]
        if "already exists" in ret.stderr.decode():
            print("already exists")
        else:
            print(f"FAIL: {err}")
            failures += 1

print(f"\nDone! Newly cloned: {count - failures}, Failures: {failures}")
print(f"Total repos: {len(all_repos)}")
