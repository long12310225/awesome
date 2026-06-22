#!/usr/bin/env python3
"""极简修复：删所有旧锚点 + 为每个标题加统一锚点 + 重建TOC"""

import re, hashlib

def anchor_of(text):
    clean = re.sub(r'[ðŸ§\uFE0F\u200B-\u200D\uFEFF<>\U0001F300-\U0001F9FF]', '', text)
    clean = re.sub(r'<[^>]+>', '', clean).strip()
    for b, g in {'LangChainð':'LangChain','官方LangGraph项目ð':'官方LangGraph项目','🦜T23':'LangChain 集成与合作伙伴'}.items():
        clean = clean.replace(b, g)
    if all(c.isascii() and (c.isalnum() or c in '- ') for c in clean):
        a = clean.lower().strip().replace(' ', '-')
        return re.sub(r'[^a-z0-9-]', '', a) or 'x'
    return 'h' + hashlib.md5(clean.encode()).hexdigest()[:8]

def run(fp):
    with open(fp, 'r') as f:
        raw = f.read()
    lines = raw.split('\n')
    
    # 清理旧锚点标签 + 重建
    out = []
    headings = []
    
    in_details = 0
    for line in lines:
        s = line.strip()
        
        # 保留新格式锚点，只删旧格式
        if re.match(r'^<a name="(zh-|lg-|aid-)', s):
            continue
        if re.match(r'^<h[234] id="', s):
            continue
        
        # 检测 details 状态
        if '<details' in s:
            in_details += 1
        if '</details>' in s:
            in_details = max(0, in_details - 1)
        
        # 检测标题
        m = re.match(r'^(#{1,4})\s+(.+)$', s)
        if m:
            level, content = len(m.group(1)), m.group(2)
            anchor = anchor_of(content)
            indent = line[:len(line)-len(line.lstrip())]
            
            # 加锚点（跳过 目录 和 h1）
            if level >= 2 and content.strip() != '目录' and 'Awesome LangGraph' not in content:
                out.append(f'{indent}<a name="{anchor}"></a>')
                headings.append((level, content.strip(), anchor, in_details))
            
            out.append(line)
        else:
            out.append(line)
    
    # 找到 ## 目录
    toc_i = None
    for i, line in enumerate(out):
        if re.match(r'^##\s*目录\s*$', line.strip()):
            toc_i = i
            break
    
    if toc_i is None:
        print("❌ 无 ## 目录")
        # 在第一个 ## 前插入
        for i, line in enumerate(out):
            if re.match(r'^##\s', line.strip()):
                toc_i = i
                out[toc_i:toc_i] = ['## 目录', '']
                break
    
    # 找下一个 ##
    next_h2 = len(out)
    for i in range(toc_i+1, len(out)):
        if re.match(r'^##\s', out[i].strip()) and '目录' not in out[i]:
            next_h2 = i
            break
    
    # 重建 TOC
    toc = ['## 目录', '']
    for lvl, title, anchor, det in headings:
        if '目录' in title or 'Awesome LangGraph' in title:
            continue
        display = re.sub(r'[\U0001F300-\U0001F9FF\x80-\xBF]', '', title).strip()
        if lvl == 2:
            toc.append(f'- [{display}](#{anchor})')
        elif lvl == 3 and det == 0:
            toc.append(f'  - [{display}](#{anchor})')
    toc.append('')
    
    result = out[:toc_i] + toc + out[next_h2:]
    
    # 最终校验
    final = '\n'.join(result)
    anchors = set(re.findall(r'<a name="([^"]+)">', final))
    toc_links = set(re.findall(r'\(#([^)]+)\)', final))
    missing = toc_links - anchors
    if missing:
        for a in missing:
            final += f'\n<a name="{a}"></a>\n'
    
    with open(fp, 'w') as f:
        f.write(final)
    
    print(f'✓ 完成: TOC {len(toc)-2} 条')
    if missing:
        print(f'⚠️ 补了 {len(missing)} 个锚点到末尾: {missing}')
    else:
        print('✅ 全部锚点匹配')

if __name__ == '__main__':
    run('人工智能/LangGraph/README_zh.md')
