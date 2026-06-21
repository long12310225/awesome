import os, re

local_dir = r"G:\work\github\awesome"

results = []
total = 0
en_count = 0
cn_count = 0

for root, dirs, files in os.walk(local_dir):
    for fname in files:
        if not fname.endswith("_zh.md"):
            continue
        fpath = os.path.join(root, fname)
        rel = os.path.relpath(fpath, local_dir)
        
        with open(fpath, encoding="utf-8") as f:
            lines = f.readlines()
        
        eng_lines = 0
        chn_lines = 0
        total_lines = 0
        
        for line in lines:
            # Match item: - [name](url) - description
            m = re.match(r'^\s*[-*] \[.+\]\(https?://[^)]+\)\s*-\s*(.*)', line)
            if m:
                total_lines += 1
                desc = m.group(1).strip()
                if desc and desc[0].isascii() and desc[0].isalpha():
                    eng_lines += 1
                elif desc and ord(desc[0]) > 127:
                    chn_lines += 1
        
        if total_lines == 0:
            status = "EMPTY"
        elif eng_lines > chn_lines:
            status = f"EN({eng_lines}/{total_lines})"
            en_count += 1
        else:
            status = f"CN({chn_lines}/{total_lines})"
            cn_count += 1
        
        results.append((rel, status, total_lines, eng_lines, chn_lines))

print(f"\n=== 统计 ===")
print(f"总计文件: {len(results)}")
print(f"已中文(CN): {cn_count}")
print(f"仍英文(EN): {en_count}")
print()

print(f"=== 未完成文件清单 (英文描述 > 中文描述) ===")
for rel, status, total, eng, chn in results:
    if eng > chn:
        print(f"  {rel}  [{status}]")

print()
print(f"=== 已完成文件清单 ===")
for rel, status, total, eng, chn in results:
    if chn >= eng and total > 0:
        print(f"  {rel}  [{status}]")
