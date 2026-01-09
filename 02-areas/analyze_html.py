#!/usr/bin/env python3
"""
深度分析专辑HTML文件
"""
import re
import json

# 读取HTML文件
with open('/Users/ibepo/Documents/GitHub/doc2/02-areas/album_page_full.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 搜索所有script标签内容
print("=== 分析 Script 标签内容 ===\n")

script_pattern = r'<script[^>]*>(.*?)</script>'
scripts = re.findall(script_pattern, html, re.DOTALL)

print(f"找到 {len(scripts)} 个 script 标签\n")

# 查找包含 appmsg 或 article 的脚本
relevant_scripts = []
for i, script in enumerate(scripts):
    if any(keyword in script for keyword in ['appmsg', 'article', 'album', 'msglist', 'item_url', 'content_url']):
        relevant_scripts.append((i, script))

print(f"包含相关关键词的脚本: {len(relevant_scripts)} 个\n")

# 分析每个相关脚本
for idx, (script_num, script) in enumerate(relevant_scripts[:5]):
    print(f"=== Script {script_num} ===")
    # 显示前500字符
    preview = script[:500].replace('\n', ' ')
    print(f"内容预览: {preview}...")

    # 尝试提取JSON
    json_matches = re.findall(r'{[^{}]{10,500}}', script)
    if json_matches:
        print(f"  可能的JSON对象: {len(json_matches)} 个")

print("\n=== 搜索文章数据特征 ===\n")

# 搜索常见的数据字段
data_fields = ['item_show_type', 'item_idx', 'create_time', 'datetime', 'title', 'digest', 'cover']
for field in data_fields:
    pattern = f'"{field}"'
    count = html.count(pattern)
    if count > 0:
        print(f"{field}: {count} 次")

# 搜索 data-id 属性
print("\n=== 搜索 data-id 属性 ===\n")
data_ids = re.findall(r'data-id="([^"]+)"', html) + re.findall(r"data-id='([^']+)'", html)
print(f"找到 {len(data_ids)} 个 data-id")
if data_ids:
    print(f"示例: {data_ids[:5]}")

# 保存包含 appmsg 的脚本内容
for script_num, script in relevant_scripts[:3]:
    filename = f'/Users/ibepo/Documents/GitHub/doc2/02-areas/script_{script_num}.txt'
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(script)
    print(f"\n脚本 {script_num} 已保存到: {filename}")
