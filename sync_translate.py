"""
sync_translate.py - 从上游仓库同步 README 并翻译为中文 (v4)

优化:
- 多线程并发翻译
- 大批次处理减少 API 调用
- 仅翻译描述文本，保留项目名称不变
- 更可靠的批次拆分策略
"""

import re
import os
import sys
import time
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from deep_translator import GoogleTranslator

REPO_DIR = r"G:\tmp\awesome-repos"
UPSTREAM_DIR = r"G:\tmp\awesome-upstream"
LOCAL_DIR = r"G:\work\github\awesome"
README_ZH = os.path.join(LOCAL_DIR, "readme_zh.md")
MAX_CHUNK = 4500
NUM_WORKERS = 3
DELAY = 0.15

_local = threading.local()
_lock = threading.Lock()
_progress = {"done": 0, "total": 0}


def get_translator():
    if not hasattr(_local, 't'):
        _local.t = GoogleTranslator(source='en', target='zh-CN')
    return _local.t


def parse_mappings():
    mappings = {}
    with open(README_ZH, encoding="utf-8") as f:
        for line in f:
            m = re.search(
                r'https://github\.com/([^/\s]+/[^/\s#)]+).*?📄本地\]\(([^)]+_zh\.md)\)', line)
            if m:
                mappings[m.group(1)] = os.path.join(LOCAL_DIR, m.group(2))
    return mappings


def find_readme(repo_full):
    repo_name = repo_full.split("/")[-1]
    for base in [REPO_DIR, UPSTREAM_DIR]:
        d = os.path.join(base, repo_name)
        if os.path.isdir(d):
            for fn in ["README.md", "readme.md", "Readme.md", "ReadMe.md"]:
                p = os.path.join(d, fn)
                if os.path.exists(p):
                    return p
    return None


def has_cjk(text):
    return bool(re.search(r'[\u4e00-\u9fff\u3040-\u309f\u30a0-\u30ff]', text))


def needs_tr(text, is_project_name=False):
    t = text.strip()
    if not t or len(t) < 2:
        return False
    if has_cjk(t):
        return False
    if re.match(r'^https?://', t):
        return False
    if re.match(r'^[\d\s\W]+$', t):
        return False
    if is_project_name:
        # For project names: skip most short/technical names
        words = t.split()
        if len(words) <= 2 and not any(c in t for c in ' .'):
            return False
        if len(words) == 1:
            return False
    return True


def translate_one(text, retries=2):
    t = get_translator()
    for a in range(retries + 1):
        try:
            if len(text) > MAX_CHUNK:
                text = text[:MAX_CHUNK]
            r = t.translate(text)
            time.sleep(DELAY)
            return r if r else text
        except Exception:
            if a < retries:
                time.sleep(1 * (a + 1))
    return text


def batch_translate(texts):
    """批量翻译，返回结果列表"""
    if not texts:
        return []

    # 分成批次
    batches = []
    cur = []
    cur_len = 0
    for text in texts:
        add = len(text) + 3  # "\n" 分隔
        if cur_len + add > MAX_CHUNK and cur:
            batches.append(cur)
            cur = []
            cur_len = 0
        cur.append(text)
        cur_len += add
    if cur:
        batches.append(cur)

    results = [None] * len(texts)
    offset = 0
    batch_info = []
    for batch in batches:
        batch_info.append((offset, batch))
        offset += len(batch)

    with ThreadPoolExecutor(max_workers=NUM_WORKERS) as pool:
        futs = {}
        for off, batch in batch_info:
            futs[pool.submit(_do_batch, batch)] = off
        for fut in as_completed(futs):
            off = futs[fut]
            try:
                res = fut.result()
                for i, r in enumerate(res):
                    results[off + i] = r
            except:
                pass

    for i in range(len(texts)):
        if results[i] is None:
            results[i] = texts[i]
    return results


def _do_batch(texts):
    """翻译一批，用换行连接"""
    if len(texts) == 1:
        return [translate_one(texts[0]) if needs_tr(texts[0]) else texts[0]]

    combined = "\n".join(texts)
    try:
        t = get_translator()
        r = t.translate(combined)
        time.sleep(DELAY)
        if r:
            lines = r.split('\n')
            # 清理空行
            lines = [l for l in lines if l.strip()]
            if len(lines) >= len(texts):
                # 如果结果行数 >= 原文数，取前 N 行
                return lines[:len(texts)]
            elif len(lines) >= len(texts) * 0.8:
                # 接近，补上缺失的
                result = lines + texts[len(lines):]
                return result[:len(texts)]
    except:
        pass

    # 回退：逐个翻译
    return [translate_one(t) if needs_tr(t) else t for t in texts]


def translate_readme(content):
    lines = content.split('\n')

    # 分析每一行
    parsed = []  # (line_idx, type, data)
    all_texts = []  # 需要翻译的文本
    text_refs = []  # (parsed_idx, which_part)

    in_code = False
    in_html = False
    title_done = False

    for i, line in enumerate(lines):
        s = line.strip()

        if s.startswith('```'):
            in_code = not in_code
            parsed.append((i, 'keep', line, []))
            continue
        if in_code:
            parsed.append((i, 'keep', line, []))
            continue

        # HTML blocks - track nesting depth to handle self-contained lines
        _open_tags = len(re.findall(r'<(div|table|picture)\b', s, re.I))
        _close_tags = len(re.findall(r'</(div|table|picture)>', s, re.I))
        if _open_tags > 0:
            if _open_tags > _close_tags:
                in_html = True
            # else: self-contained line (equal open/close), don't set in_html
        if _close_tags > 0:
            # Check if this closes all open nesting
            if in_html and _close_tags >= _open_tags:
                in_html = False
                parsed.append((i, 'keep', line, []))
                continue
        if re.match(r'<(br|hr|img|source|sub|sup|b|a|span)\b', s, re.I):
            # Self-closing or inline elements - keep as-is but don't affect in_html
            parsed.append((i, 'keep', line, []))
            continue
        if in_html:
            parsed.append((i, 'keep', line, []))
            continue

        if not s or s in ('---', '***', '___', '<!-- -->'):
            parsed.append((i, 'keep', line, []))
            continue

        # HTML comments
        if s.startswith('<!--'):
            parsed.append((i, 'keep', line, []))
            continue

        # Pure image/badge lines
        if re.match(r'^\[?\!\[', s) and ('badge' in s.lower() or '](http' in s):
            parsed.append((i, 'keep', line, []))
            continue

        # Title
        if line.startswith('# ') and not title_done:
            title_done = True
            clean = re.sub(
                r'\s*\[!\[.*?\]\(.*?\)\]\(.*?\)', '', line[2:]).strip()
            if needs_tr(clean):
                pi = len(parsed)
                ti = len(all_texts)
                all_texts.append(clean)
                text_refs.append((pi, 0))
                parsed.append((i, 'title', line, [ti]))
            else:
                parsed.append((i, 'keep', line, []))
            continue

        # Heading
        hm = re.match(r'^(#{2,6})\s+(.*)', line)
        if hm:
            hashes = hm.group(1)
            heading = hm.group(2).strip()
            clean_h = re.sub(r'\[!\[.*?\]\(.*?\)\]\(.*?\)',
                             '', heading).strip()
            clean_h = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', clean_h).strip()
            if needs_tr(clean_h):
                pi = len(parsed)
                ti = len(all_texts)
                all_texts.append(clean_h)
                text_refs.append((pi, 0))
                parsed.append((i, 'heading', (hashes, heading), [ti]))
            else:
                parsed.append((i, 'keep', line, []))
            continue

        # List item with description: - [Name](url) - Desc
        lm = re.match(
            r'^(\s*[-*])\s+\[([^\]]+)\]\(([^)]+)\)\s*[-–—]\s*(.*)', line)
        if lm:
            indent = lm.group(1)
            name = lm.group(2)
            url = lm.group(3)
            desc = lm.group(4).strip()

            indices = []
            # Only translate description, not project name (avoids artifacts)
            if needs_tr(desc):
                ti = len(all_texts)
                all_texts.append(desc)
                text_refs.append((len(parsed), 0))
                indices.append(ti)
            parsed.append((i, 'list_desc', (indent, name, url, desc), indices))
            continue

        # List item link only: - [Name](url)
        lm2 = re.match(r'^(\s*[-*])\s+\[([^\]]+)\]\(([^)]+)\)\s*$', line)
        if lm2:
            indent = lm2.group(1)
            name = lm2.group(2)
            url = lm2.group(3)
            # Only translate if name is clearly English phrase (not project name)
            if needs_tr(name, is_project_name=True) and ' ' in name:
                ti = len(all_texts)
                all_texts.append(name)
                text_refs.append((len(parsed), 0))
                parsed.append((i, 'list_name', (indent, name, url), [ti]))
            else:
                parsed.append((i, 'keep', line, []))
            continue

        # Regular text
        if needs_tr(s):
            ti = len(all_texts)
            all_texts.append(s)
            text_refs.append((len(parsed), 0))
            parsed.append((i, 'text', line, [ti]))
        else:
            parsed.append((i, 'keep', line, []))

    # Batch translate all texts
    n = len(all_texts)
    print(f"({n} texts)", end=" ", flush=True)
    translated = batch_translate(all_texts)

    # Build result
    result = []
    for pi, (line_idx, ltype, data, indices) in enumerate(parsed):
        if ltype == 'keep':
            result.append(data)

        elif ltype == 'title':
            t = translated[indices[0]] if indices else data
            orig = lines[line_idx]
            badge = re.search(r'(\s*\[!\[.*?\]\(.*?\)\]\(.*?\))', orig[2:])
            result.append(f"# {t}{badge.group(1)}" if badge else f"# {t}")

        elif ltype == 'heading':
            hashes, orig_heading = data
            t = translated[indices[0]] if indices else orig_heading
            result.append(f"{hashes} {t}")

        elif ltype == 'list_desc':
            indent, name, url, desc = data
            t_desc = translated[indices[0]] if indices else desc
            result.append(f"{indent} [{name}]({url}) - {t_desc}")

        elif ltype == 'list_name':
            indent, name, url = data
            t_name = translated[indices[0]] if indices else name
            result.append(f"{indent} [{t_name}]({url})")

        elif ltype == 'text':
            t = translated[indices[0]] if indices else data
            result.append(t)

        else:
            result.append(lines[line_idx])

    return '\n'.join(result)


def process_repo(repo_full, local_path, force=False):
    readme = find_readme(repo_full)
    if not readme:
        return "NO_README"

    with open(readme, encoding='utf-8', errors='replace') as f:
        upstream = f.read()
    if not upstream.strip():
        return "EMPTY"

    up_h2 = sum(1 for l in upstream.split('\n') if l.startswith('## '))

    if not force and os.path.exists(local_path):
        with open(local_path, encoding='utf-8') as f:
            local = f.read()
        lo_h2 = sum(1 for l in local.split('\n') if l.startswith('## '))
        if lo_h2 == up_h2 and lo_h2 > 0 and len(local) > 100:
            return "UP_TO_DATE"

    try:
        translated = translate_readme(upstream)
    except Exception as e:
        return f"ERROR: {e}"

    os.makedirs(os.path.dirname(local_path), exist_ok=True)
    with open(local_path, 'w', encoding='utf-8') as f:
        f.write(translated)
    return f"OK ({up_h2}s)"


def main():
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument('--dry-run', action='store_true')
    p.add_argument('--repos', nargs='*')
    p.add_argument('--limit', type=int, default=0)
    p.add_argument('--force', action='store_true')
    args = p.parse_args()

    mappings = parse_mappings()
    print(f"Found {len(mappings)} repos\n")

    # Resolve repo names (support both full 'user/repo' and short 'repo' names)
    if args.repos:
        repos = []
        _lower_map = {k.lower(): k for k in mappings}
        _short_map = {k.split('/')[-1].lower(): k for k in mappings}
        for r in args.repos:
            rl = r.lower()
            if rl in _lower_map:
                repos.append(_lower_map[rl])
            elif rl in _short_map:
                repos.append(_short_map[rl])
            else:
                repos.append(r)  # keep as-is, will be skipped later
    else:
        repos = list(mappings.keys())
    if args.limit > 0:
        repos = repos[:args.limit]

    stats = {"OK": 0, "NO_README": 0, "UP_TO_DATE": 0, "ERROR": 0}
    t0 = time.time()

    for i, repo in enumerate(repos):
        if repo not in mappings:
            continue

        local_path = mappings[repo]
        elapsed = time.time() - t0
        rate = (i / elapsed) if elapsed > 0 and i > 0 else 0
        eta = ((len(repos) - i) / rate / 60) if rate > 0 else 0

        print(f"[{i+1}/{len(repos)}] ({eta:.0f}m) {repo}...",
              end=" ", flush=True)

        if args.dry_run:
            r = find_readme(repo)
            print(f"{'HAS_README' if r else 'NO_README'}")
            continue

        result = process_repo(repo, local_path, force=args.force)
        print(result)

        if result.startswith("OK"):
            stats["OK"] += 1
        elif result == "NO_README":
            stats["NO_README"] += 1
        elif result == "UP_TO_DATE":
            stats["UP_TO_DATE"] += 1
        else:
            stats["ERROR"] += 1

    total = time.time() - t0
    print(f"\n=== Done ({total/60:.1f} min) ===")
    for k, v in stats.items():
        if v:
            print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
