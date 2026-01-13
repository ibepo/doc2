#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
博客讲义分析脚本
用于分析"副本9小时免费博客讲义"PDF文档
"""

import fitz  # PyMuPDF
import re
import json
from datetime import datetime
import os

def analyze_blog_lecture_pdf():
    """
    分析博客讲义PDF文档
    """
    print("=" * 60)
    print("开始分析副本9小时免费博客讲义文档")
    print("=" * 60)

    # PDF文件路径
    pdf_path = "/Users/ibepo/Documents/GitHub/doc2/docs/P.A.R.A/02-Areas/读书/副本9小时免费播客讲义(1).pdf"

    try:
        # 打开PDF文档
        doc = fitz.open(pdf_path)
        total_pages = len(doc)
        print(f"文档总页数: {total_pages}")

        # 提取全文内容
        full_text = ""
        page_contents = []

        for page_num in range(total_pages):
            page = doc[page_num]
            text = page.get_text()
            page_contents.append(text)
            full_text += text
            print(f"已提取第 {page_num + 1} 页内容")

        doc.close()
        print(f"\n全文总字符数: {len(full_text)}")

        # 分析文档结构
        print("\n" + "=" * 60)
        print("文档结构分析")
        print("=" * 60)

        # 提取标题和章节
        lines = full_text.split('\n')
        titles = []
        chapters = []

        for i, line in enumerate(lines):
            line = line.strip()
            if line and len(line) > 10:  # 过滤过短的行
                # 检测可能的标题（长度较长、包含数字或特殊字符）
                if (len(line) > 20 or any(char.isdigit() for char in line) or
                    any(char in line for char in '：:•▪▫▸▹◦•')):
                    titles.append((i+1, line))

        print(f"识别到 {len(titles)} 个可能的标题/章节:")
        for line_num, title in titles[:20]:  # 显示前20个
            print(f"  第{line_num}行: {title[:100]}...")

        # 关键要点提取
        print("\n" + "=" * 60)
        print("关键要点提取")
        print("=" * 60)

        # 搜索关键概念
        key_concepts = {
            '博客': r'博客|blog|Blog|BLOG',
            '播客': r'播客|podcast|Podcast|PODCAST',
            '内容创作': r'内容创作|内容运营|自媒体|新媒体',
            '推广营销': r'推广|营销|推广营销|流量|SEO',
            '技术工具': r'工具|软件|平台|技术',
            '商业变现': r'变现|盈利|商业模式|收入',
            '运营策略': r'运营|策略|方法|技巧',
            '数据分析': r'数据|分析|统计|指标'
        }

        extracted_points = []

        for concept, pattern in key_concepts.items():
            matches = re.findall(pattern, full_text, re.IGNORECASE)
            if matches:
                # 找到包含这个概念的关键句子
                sentences = re.split(r'[。！？；\n]', full_text)
                for sentence in sentences:
                    if re.search(pattern, sentence, re.IGNORECASE) and len(sentence.strip()) > 20:
                        extracted_points.append({
                            'category': concept,
                            'content': sentence.strip(),
                            'length': len(sentence.strip())
                        })
                        break  # 每个类别只取第一个匹配的长句子

        print(f"提取到 {len(extracted_points)} 个关键要点:")
        for i, point in enumerate(extracted_points, 1):
            print(f"\n要点 {i} [{point['category']}]:")
            print(f"内容: {point['content']}")

        # 提取数据和数字
        print("\n" + "=" * 60)
        print("数据点提取")
        print("=" * 60)

        # 提取数字
        numbers = re.findall(r'\b\d+(?:\.\d+)?\b', full_text)
        print(f"识别到数字: {numbers[:20]}...")  # 显示前20个数字

        # 提取百分比
        percentages = re.findall(r'\d+(?:\.\d+)?%', full_text)
        print(f"识别到百分比: {percentages}")

        # 提取时间和时长（9小时相关）
        time_patterns = re.findall(r'9\s*小时|9\s*h|9\s*小时', full_text)
        print(f"识别到9小时相关内容: {time_patterns}")

        # 主题分类分析
        print("\n" + "=" * 60)
        print("主题分类分析")
        print("=" * 60)

        themes = {
            '博客基础': ['博客', 'blog', '写作', '内容'],
            '播客制作': ['播客', 'podcast', '音频', '录制'],
            '推广营销': ['推广', '营销', 'SEO', '流量'],
            '商业变现': ['变现', '盈利', '收入', '商业模式'],
            '工具技术': ['工具', '软件', '平台', '技术'],
            '运营策略': ['运营', '策略', '方法', '技巧'],
            '数据分析': ['数据', '分析', '统计', '指标']
        }

        theme_counts = {}
        for theme, keywords in themes.items():
            count = sum(1 for keyword in keywords
                       for match in re.findall(keyword, full_text, re.IGNORECASE))
            theme_counts[theme] = count

        print("主题分布:")
        for theme, count in sorted(theme_counts.items(), key=lambda x: x[1], reverse=True):
            print(f"  {theme}: {count} 次提及")

        # 生成分析报告
        print("\n" + "=" * 60)
        print("生成分析报告")
        print("=" * 60)

        analysis_result = {
            'document_info': {
                'title': '副本9小时免费博客讲义',
                'analysis_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'total_pages': total_pages,
                'total_content_length': len(full_text),
                'file_size_mb': os.path.getsize(pdf_path) / (1024 * 1024)
            },
            'structure_analysis': {
                'total_lines': len(lines),
                'identified_titles': len(titles),
                'title_sample': titles[:5]  # 前5个标题样本
            },
            'key_points': extracted_points,
            'data_points': {
                'numbers_count': len(numbers),
                'percentages_count': len(percentages),
                'time_references': time_patterns
            },
            'theme_analysis': theme_counts,
            'content_summary': {
                'main_topics': [theme for theme, count in theme_counts.items() if count > 0],
                'content_focus': max(theme_counts.items(), key=lambda x: x[1])[0] if theme_counts else '未知'
            }
        }

        # 保存分析结果
        result_file = "/Users/ibepo/Documents/GitHub/doc2/docs/P.A.R.A/02-Areas/读书/博客讲义分析结果.json"
        with open(result_file, 'w', encoding='utf-8') as f:
            json.dump(analysis_result, f, ensure_ascii=False, indent=2)

        # 生成总结报告
        summary_file = "/Users/ibepo/Documents/GitHub/doc2/docs/P.A.R.A/02-Areas/读书/博客讲义总结报告.json"
        summary_content = {
            'document_info': analysis_result['document_info'],
            'key_findings': [
                f"文档包含 {total_pages} 页内容",
                f"总字符数 {len(full_text)}",
                f"识别到 {len(titles)} 个章节/标题",
                f"提取 {len(extracted_points)} 个关键要点",
                f"主题重点: {analysis_result['content_summary']['content_focus']}"
            ],
            'main_themes': [theme for theme, count in theme_counts.items() if count > 3],
            'recommendations': [
                "建议重点学习博客基础和播客制作相关内容",
                "关注推广营销和商业变现策略",
                "善用推荐的技术工具提高效率"
            ]
        }

        with open(summary_file, 'w', encoding='utf-8') as f:
            json.dump(summary_content, f, ensure_ascii=False, indent=2)

        print(f"\n分析完成！")
        print(f"分析结果已保存到: {result_file}")
        print(f"总结报告已保存到: {summary_file}")

        # 显示统计信息
        print(f"\n文档统计信息:")
        print(f"- 总页数: {total_pages}")
        print(f"- 总字符数: {len(full_text)}")
        print(f"- 识别标题数: {len(titles)}")
        print(f"- 关键要点数: {len(extracted_points)}")
        print(f"- 主题类别数: {len([t for t in theme_counts.values() if t > 0])}")

        return analysis_result

    except Exception as e:
        print(f"分析过程中发生错误: {e}")
        return None

if __name__ == "__main__":
    result = analyze_blog_lecture_pdf()