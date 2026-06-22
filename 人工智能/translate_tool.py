#!/usr/bin/env python3
"""腾讯云机器翻译工具 v2 - 翻译 Markdown 文件，保留所有格式

用法:
    # 先设置环境变量（或复制 .env.example 为 .env 并填入密钥）
    export TENCENT_SECRET_ID="your_id"
    export TENCENT_SECRET_KEY="your_key"
    # 然后运行
    python3 translate_tool.py <输入文件> <输出文件>
    python3 translate_tool.py "要翻译的文本"

依赖: pip install tencentcloud-sdk-python
"""

import json, sys, re, time
from tencentcloud.common import credential
from tencentcloud.tmt.v20180321 import tmt_client, models

import os
SECRET_ID = os.environ.get("TENCENT_SECRET_ID", "")
SECRET_KEY = os.environ.get("TENCENT_SECRET_KEY", "")

cred_obj = credential.Credential(SECRET_ID, SECRET_KEY)
client = tmt_client.TmtClient(cred_obj, "ap-guangzhou")
_last_req = 0.0

PROTECTED_TERMS = sorted([
    "LangGraph", "LangChain", "LangSmith", "Deep Agents",
    "GitHub", "FastAPI", "Next.js", "Streamlit", "React",
    "TypeScript", "Python", "JavaScript", "FastHTML", "MCP",
    "CLI", "SDK", "API", "RAG", "LLM", "LLMs",
    "PostgreSQL", "pgvector", "Redis", "MongoDB", "SQL",
    "Docker", "Kubernetes", "OpenAI", "Anthropic", "Claude",
    "Gemini", "Tavily", "Gmail", "Slack", "Google Calendar",
    "Elasticsearch", "Qdrant", "Ollama", "FAISS", "BM25",
    "Jupyter", "Vue.js", "Node.js", "Fastify", "Mermaid",
    "Pydantic", "Langfuse", "WhatsApp", "ReAct",
    "LangChain.js", "LangGraph.js", "LangSmith SDK",
    "LangSmith Fleet", "Agent Server", "Deep Agents SDK",
    "LangGraph CLI", "LangGraph SDK", "Deep Agents CLI",
    "Computer Use Agent", "Swarm Agent", "Agent Inbox",
    "Social Media Agent", "Open Deep Research",
    "LangGraph Generator", "Fleet", "CUA", "Subgraphs",
], key=len, reverse=True)

def translate_text(text):
    if not text.strip():
        return text
    terms_found = {}
    working = text
    for i, term in enumerate(PROTECTED_TERMS):
        if term in working:
            ph = f"\xA7T{i}\xA7"
            working = working.replace(term, ph)
            terms_found[ph] = term
    global _last_req
    elapsed = time.time() - _last_req
    if elapsed < 0.3:
        time.sleep(0.3 - elapsed)
    try:
        _last_req = time.time()
        req = models.TextTranslateRequest()
        req.SourceText = working
        req.Source = "en"
        req.Target = "zh"
        req.ProjectId = 0
        resp = client.TextTranslate(req)
        result = json.loads(resp.to_json_string())["TargetText"]
        for ph, term in terms_found.items():
            result = result.replace(ph, term)
        return result
    except Exception as e:
        if "RequestLimitExceeded" in str(e):
            time.sleep(1.0)
            try:
                req = models.TextTranslateRequest()
                req.SourceText = working
                req.Source = "en"
                req.Target = "zh"
                req.ProjectId = 0
                resp = client.TextTranslate(req)
                result = json.loads(resp.to_json_string())["TargetText"]
                for ph, term in terms_found.items():
                    result = result.replace(ph, term)
                return result
            except: pass
        return text

def extract_elements(line):
    elements = []
    parts = []
    pat = re.compile(r'(!\[.*?\]\(.*?\))|(\[.*?\]\(.*?\))|(<[^>]+>)|(https?://[^\s<>"\'）\]\)]+)')
    last = 0
    for m in pat.finditer(line):
        if m.start() > last:
            parts.append(line[last:m.start()])
        elements.append(m.group(0))
        parts.append(f"\xA7{len(elements)-1}\xA7")
        last = m.end()
    if last < len(line):
        parts.append(line[last:])
    return ''.join(parts), elements

def restore(text, elements):
    for i, e in enumerate(elements):
        text = text.replace(f"\xA7{i}\xA7", e)
    return text

def is_skip(stripped):
    if re.match(r'^</?[a-zA-Z][^>]*>$', stripped): return True
    if stripped.startswith('<!--') or stripped.endswith('-->'): return True
    if stripped.startswith('```'): return True
    if re.match(r'^\|[\s\-:]+\|$', stripped): return True
    if stripped in ('<n></n>','<n>','</n>'): return True
    clean = re.sub(r'!\[.*?\]\(.*?\)|\[.*?\]\(.*?\)|<[^>]+>|https?://\S+', '', stripped).strip()
    if not clean: return True
    return False

def translate_line(line):
    s = line.strip()
    if not s or is_skip(s):
        return line
    indent = line[:len(line)-len(line.lstrip())]

    # 表格
    if s.startswith('|') and s.endswith('|'):
        cells = s.split('|')
        nc = []
        for c in cells:
            t = c.strip()
            if t:
                txt, elems = extract_elements(t)
                c2 = txt.strip()
                if c2:
                    r = translate_text(c2)
                    nc.append(restore(r, elems))
                else:
                    nc.append(c)
            else:
                nc.append(c)
        return indent + '|'.join(nc)

    # 标题
    h = re.match(r'^(#{1,6})\s+(.+)$', s)
    if h:
        txt, elems = extract_elements(h.group(2))
        if txt.strip():
            r = translate_text(txt.strip())
            return indent + f"{h.group(1)} {restore(r, elems)}"
        return line

    # 列表
    l = re.match(r'^(\s*[-*+]\s+)(.+)$', s)
    if l:
        txt, elems = extract_elements(l.group(2))
        if txt.strip():
            r = translate_text(txt.strip())
            return indent + l.group(1) + restore(r, elems)
        return line

    # 普通行
    txt, elems = extract_elements(s)
    if txt.strip():
        r = translate_text(txt.strip())
        return indent + restore(r, elems)
    return line

def translate_file(inp, out):
    with open(inp, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    res = []
    n = len(lines)
    for i, line in enumerate(lines):
        res.append(translate_line(line.rstrip('\n')))
        if (i+1) % 100 == 0:
            print(f"  进度: {i+1}/{n}", file=sys.stderr)
    with open(out, 'w', encoding='utf-8') as f:
        f.write('\n'.join(res))
    print(f"✓ 完成: {inp} → {out} ({n}行)")

if __name__ == '__main__':
    if len(sys.argv) == 3:
        translate_file(sys.argv[1], sys.argv[2])
    elif len(sys.argv) == 2:
        print(translate_text(sys.argv[1]))
    else:
        print(__doc__)
