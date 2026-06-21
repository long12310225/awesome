import re, os

# Read upstream Go README
with open(r"G:\tmp\awesome-repos\awesome-go\README.md", encoding="utf-8") as f:
    content = f.read()

# Build zh version
# Translate section headings
translations = {
    "Actor Model": "Actor Model",
    "Artificial Intelligence": "人工智能",
    "Audio and Music": "音频和音乐",
    "Authentication and Authorization": "认证和授权",
    "Blockchain": "区块链",
    "Bot Building": "机器人构建",
    "Build Automation": "构建自动化",
    "Command Line": "命令行",
    "Configuration": "配置",
    "Continuous Integration": "持续集成",
    "CSS Preprocessors": "CSS 预处理器",
    "Data Integration Frameworks": "数据集成框架",
    "Data Structures and Algorithms": "数据结构和算法",
    "Database": "数据库",
    "Database Drivers": "数据库驱动",
    "Date and Time": "日期和时间",
    "Distributed Systems": "分布式系统",
    "Dynamic DNS": "动态 DNS",
    "Email": "邮件",
    "Embeddable Scripting Languages": "可嵌入脚本语言",
    "Error Handling": "错误处理",
    "File Handling": "文件处理",
    "Financial": "金融",
    "Forms": "表单",
    "Functional": "函数式编程",
    "Game Development": "游戏开发",
    "Generators": "生成器",
    "Geographic": "地理",
    "Go Compilers": "Go 编译器",
    "Goroutines": "Goroutines",
    "GUI": "GUI",
    "Hardware": "硬件",
    "Images": "图像",
    "IoT (Internet of Things)": "物联网",
    "Job Scheduler": "任务调度器",
    "JSON": "JSON",
    "Logging": "日志",
    "Machine Learning": "机器学习",
    "Messaging": "消息",
    "Microsoft Office": "Microsoft Office",
    "Miscellaneous": "杂项",
    "Natural Language Processing": "自然语言处理",
    "Networking": "网络",
    "OpenGL": "OpenGL",
    "ORM": "ORM",
    "Package Management": "包管理",
    "Performance": "性能",
    "Query Language": "查询语言",
    "Reflection": "反射",
    "Resource Embedding": "资源嵌入",
    "Science and Data Analysis": "科学与数据分析",
    "Security": "安全",
    "Serialization": "序列化",
    "Server Applications": "服务器应用",
    "Stream Processing": "流处理",
    "Template Engines": "模板引擎",
    "Testing": "测试",
    "Text Processing": "文本处理",
    "Third-party APIs": "第三方 API",
    "Utilities": "工具类",
    "UUID": "UUID",
    "Validation": "验证",
    "Version Control": "版本控制",
    "Video": "视频",
    "Web Frameworks": "Web 框架",
    "WebAssembly": "WebAssembly",
    "Webhooks Server": "Webhooks 服务器",
    "Windows": "Windows",
    "Workflow Frameworks": "工作流框架",
    "XML": "XML",
    "Zero Trust": "零信任",
    "Code Analysis": "代码分析",
    "Editor Plugins": "编辑器插件",
    "Go Generate Tools": "Go 生成工具",
    "Go Tools": "Go 工具",
    "Software Packages": "软件包",
    "Resources": "资源",
    "Benchmarks": "基准测试",
    "Conferences": "会议",
    "E-Books": "电子书",
    "Gophers": "Gophers",
    "Meetups": "聚会",
    "Style Guides": "风格指南",
    "Social Media": "社交媒体",
    "Websites": "网站",
    "Contribution": "贡献",
    "License": "许可"
}

result = []
for line in content.split("\n"):
    if line.startswith("# Awesome Go"):
        result.append("# Awesome Go [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)")
        result.append("")
        result.append("> 精选的 Go 框架、库和软件。")
    elif line.startswith("## "):
        text = line[3:].strip()
        if text in translations:
            result.append(f"## {translations[text]}")
        else:
            # Keep original if no translation
            result.append(line)
    elif line.startswith("* [") and "] - " in line:
        # Extract name and description
        # Format: * [name](url) - description
        m = re.match(r'\* \[([^\]]+)\]\(([^)]+)\) - (.+)', line)
        if m:
            name = m.group(1)
            url = m.group(2)
            desc = m.group(3)
            result.append(f"- [{name}]({url}) - {desc}")
    elif line.startswith("* [") and "](" in line:
        # Some items might not have description
        result.append(line)
    else:
        result.append(line)

# Write output
output = "\n".join(result)
with open(r"G:\work\github\awesome\编程语言\awesome-go_zh.md", "w", encoding="utf-8") as f:
    f.write(output)

# Count sections
sections = sum(1 for line in result if line.startswith("## ") and not line.startswith("## Contents"))
print(f"Sections: {sections}")
print("Done!")
