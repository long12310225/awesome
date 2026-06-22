#!/usr/bin/env python3
"""全面修复：对照原文恢复所有表格单元格格式"""

import re

ORIG = '/e/github/awesome-LangGraph/README.md'
TRANS = '人工智能/LangGraph/README_zh.md'

with open(ORIG) as f:
    orig_lines = f.readlines()
with open(TRANS) as f:
    tran_lines = f.readlines()

# 从原文提取所有表格行的第一个单元格 + 描述（用于精确匹配）
orig_rows = []  # [(first_cell, second_cell_or_desc_signature), ...]
for line in orig_lines:
    s = line.strip()
    if s.startswith('|') and s.endswith('|'):
        cells = [c.strip() for c in s.split('|')]
        if len(cells) >= 4:  # | first | second | third |
            first = cells[1]
            second = cells[2]
            if first.startswith('**') or second.startswith('**'):
                # 提取链接文本或粗体中的纯文本作为签名
                links = re.findall(r'\[([^\]]+)\]', first) or re.findall(r'\[([^\]]+)\]', second)
                # 从 **内容** 中提取纯文本（去掉emoji和链接）
                bold_match = re.match(r'\*\*(.*?)\*\*', first)
                bold_text = ''
                if bold_match:
                    inner = bold_match.group(1)
                    # 从 inner 提取链接文本或纯文本
                    inner_links = re.findall(r'\[([^\]]+)\]', inner)
                    if inner_links:
                        bold_text = inner_links[0]
                    else:
                        # 去掉emoji
                        bold_text = re.sub(r'[\U0001F300-\U0001F9FF\uFE0F]', '', inner).strip()
                sig = (links[0] if links else '', bold_text)
                if sig[0] or sig[1]:
                    orig_rows.append((sig, first))

print(f'原文表格行: {len(orig_rows)}')

fixed = 0
output = []

for line in tran_lines:
    s = line.strip()
    if s.startswith('|') and s.endswith('|'):
        cells = [c.strip() for c in s.split('|')]
        if len(cells) >= 3:
            first = cells[1]
            
            # 检查是否需要修复：缺 emoji 或格式不一致
            needs_fix = False
            
            # 情况1: ** N** 模式
            if re.match(r'^\*\*\s*\d+\s*\*\*$', first):
                needs_fix = True
            
            # 情况2: ** [text] 缺 emoji
            if re.match(r'^\*\*\s*\[', first):
                needs_fix = True
            
            # 情况3: **text** 但原文有链接和 emoji
            bold_match = re.match(r'^\*\*([^*]+)\*\*$', first)
            if bold_match:
                text = bold_match.group(1).strip()
                # 检查原文是否有带链接/emoji的版本
                for sig, orig_first in orig_rows:
                    if sig[0] == text or sig[1] == text:
                        if orig_first != first and ('http' in orig_first or len(orig_first) > len(first) + 2):
                            needs_fix = True
                            break
            
            if needs_fix:
                # 找最佳匹配的原文行
                t_links = re.findall(r'\[([^\]]+)\]', first)
                t_bolds = re.findall(r'\*\*([^*]+)\*\*', first)
                t_sig = (t_links[0] if t_links else '', t_bolds[0] if t_bolds else '')
                
                best_match = None
                for sig, orig_first in orig_rows:
                    # 匹配链接或粗体文本
                    if t_sig[0] and t_sig[0] == sig[0]:
                        best_match = orig_first
                        break
                    if t_sig[1] and t_sig[1] == sig[1]:
                        best_match = orig_first
                        break
                
                if best_match and best_match != first:
                    cells[1] = best_match
                    fixed += 1
            
            output.append('|' + '|'.join(cells[1:-1]) + '|')
            continue
    
    output.append(line.rstrip('\n'))

with open(TRANS, 'w', encoding='utf-8') as f:
    f.write('\n'.join(output))

print(f'✓ 修复了 {fixed} 个表格单元格')
