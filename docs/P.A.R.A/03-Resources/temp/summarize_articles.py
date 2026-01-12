#!/usr/bin/env python3
"""总结 obsidian注册 文件夹下的文章主题"""

import os
from pathlib import Path
from collections import defaultdict

article_dir = Path(
    "/Users/ibepo/Documents/GitHub/doc2/docs/P.A.R.A/03-Resources/微信公众号/obsidian注册"
)

categories = {
    "任务管理": [],
    "表格数据处理": [],
    "主题外观": [],
    "思维导图/可视化": [],
    "编辑增强": [],
    "文件管理": [],
    "模板系统": [],
    "导航/搜索": [],
    "同步/备份": [],
    "媒体/图像处理": [],
    "AI/智能助手": [],
    "加密/安全": [],
    "写作/创作": [],
    "日历/时间管理": [],
    "PDF/文献管理": [],
    "代码执行": [],
    "教程/入门": [],
    "其他": [],
}

for folder in sorted(article_dir.iterdir()):
    if not folder.is_dir():
        continue

    title = folder.name

    if any(
        keyword in title
        for keyword in ["Tasks", "TODO", "Checklist", "Kanban", "Task", "CardBoard"]
    ):
        categories["任务管理"].append(title)
    elif any(
        keyword in title
        for keyword in [
            "Tables",
            "Dataview",
            "Spreadsheet",
            "Excel",
            "DataLoom",
            "Database",
            "DB Folder",
        ]
    ):
        categories["表格数据处理"].append(title)
    elif any(
        keyword in title
        for keyword in [
            "Theme",
            "Style",
            "Iconize",
            "Color",
            "Highlight",
            "Minimal",
            "Hider",
        ]
    ):
        categories["主题外观"].append(title)
    elif any(
        keyword in title
        for keyword in [
            "Mind Map",
            "Excalidraw",
            "ExcaliBrain",
            "MarkMind",
            "Diagram",
            "Mermaid",
            "Chart",
            "Visualization",
        ]
    ):
        categories["思维导图/可视化"].append(title)
    elif any(
        keyword in title
        for keyword in [
            "Outliner",
            "Editing",
            "Linter",
            "Format",
            "Refactor",
            "Copy Block",
            "Paste",
            "Filename Heading",
            "Number Headings",
        ]
    ):
        categories["编辑增强"].append(title)
    elif any(
        keyword in title
        for keyword in [
            "Folder",
            "File",
            "Workspaces",
            "Recent Files",
            "Local Images",
            "Attachment",
        ]
    ):
        categories["文件管理"].append(title)
    elif any(keyword in title for keyword in ["Templater", "Template", "Make.md"]):
        categories["模板系统"].append(title)
    elif any(
        keyword in title
        for keyword in [
            "Search",
            "Explorer",
            "Omnisearch",
            "Breadcrumb",
            "Link",
            "Quick",
        ]
    ):
        categories["导航/搜索"].append(title)
    elif any(
        keyword in title
        for keyword in ["Sync", "Git", "Backup", "LiveSync", "Remotely Save"]
    ):
        categories["同步/备份"].append(title)
    elif any(
        keyword in title
        for keyword in ["Image", "Picture", "Ozan's Image", "Attachment", "Media"]
    ):
        categories["媒体/图像处理"].append(title)
    elif any(
        keyword in title
        for keyword in ["AI", "Copilot", "Text Generator", "Assistant", "智能"]
    ):
        categories["AI/智能助手"].append(title)
    elif any(keyword in title for keyword in ["Encrypt", "Security", "Meld", "密码"]):
        categories["加密/安全"].append(title)
    elif any(
        keyword in title for keyword in ["Longform", "Writing", "写作", "Word Count"]
    ):
        categories["写作/创作"].append(title)
    elif any(
        keyword in title
        for keyword in [
            "Calendar",
            "Daily",
            "Periodic",
            "Planner",
            "Heatmap",
            "Time",
            "日期",
            "Reminder",
        ]
    ):
        categories["日历/时间管理"].append(title)
    elif any(
        keyword in title
        for keyword in ["PDF", "Book", "Annotator", "Literature", "Weread"]
    ):
        categories["PDF/文献管理"].append(title)
    elif any(keyword in title for keyword in ["Execute Code", "Run Code", "Code"]):
        categories["代码执行"].append(title)
    elif any(
        keyword in title
        for keyword in [
            "教程",
            "Tutorial",
            "入门",
            "保姆级",
            "注册",
            "安装",
            "是什么",
            "会员",
            "下载",
            "同步难题",
        ]
    ):
        categories["教程/入门"].append(title)
    elif any(
        keyword in title for keyword in ["Pandoc", "Import", "Export", "Converter"]
    ):
        categories["其他"].append(title)
    else:
        categories["其他"].append(title)

print("=" * 80)
print("Obsidian 文章主题总结")
print("=" * 80)
print()

total_count = sum(len(v) for v in categories.values())
print(f"文章总数: {total_count}")
print()

for category, articles in sorted(categories.items(), key=lambda x: -len(x[1])):
    if articles:
        print(f"\n【{category}】({len(articles)}篇)")
        print("-" * 80)
        for i, article in enumerate(articles[:10], 1):
            print(f"  {i}. {article}")
        if len(articles) > 10:
            print(f"  ... 还有 {len(articles) - 10} 篇")

print()
print("=" * 80)
print("主题分布统计")
print("=" * 80)
print()

for category, articles in sorted(categories.items(), key=lambda x: -len(x[1])):
    if articles:
        percentage = len(articles) / total_count * 100
        bar = "█" * int(percentage / 2)
        print(f"{category:20s} {len(articles):3d} 篇 ({percentage:5.1f}%) {bar}")
