#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2026年钢铁市场与行业展望PDF分析脚本
"""

import os
import re
import fitz  # PyMuPDF
from collections import Counter
import json
from datetime import datetime

def extract_pdf_content(pdf_path):
    """提取PDF文档内容"""
    print(f"开始提取PDF文档内容: {pdf_path}")

    # 检查文件是否存在
    if not os.path.exists(pdf_path):
        print(f"文件不存在: {pdf_path}")
        return None

    # 提取文本内容
    doc = fitz.open(pdf_path)
    text_content = ""
    page_count = len(doc)

    print(f"文档总页数: {page_count}")

    for page_num in range(page_count):
        page = doc[page_num]
        text = page.get_text()
        text_content += text + "\n\n"
        print(f"已提取第 {page_num + 1} 页内容")

    doc.close()

    return text_content, page_count

def analyze_document_structure(content):
    """分析文档结构"""
    print("\n" + "="*50)
    print("文档结构分析")
    print("="*50)

    # 按行分割内容
    lines = content.split('\n')

    # 分析标题结构
    sections = []
    current_section = None

    for line in lines:
        line = line.strip()
        if not line:
            continue

        # 检测标题（包含"第X章"、"第X节"、"X、"等）
        if re.match(r'第[一二三四五六七八九十]+[章节]', line) or \
           re.match(r'\d+[、\.]\s', line) or \
           re.match(r'[一二三四五六七八九十]+[、\.]\s', line):
            sections.append({
                'title': line,
                'level': len(re.match(r'(\s*)', line).group(0)) // 2,
                'content': line
            })
            current_section = line
        elif current_section:
            sections.append({
                'title': current_section,
                'level': 0,
                'content': line
            })

    # 显示章节结构
    print("文档章节结构：")
    for i, section in enumerate(sections[:20]):  # 显示前20个章节
        print(f"{i+1:2d}. {section['title']}")

    return sections

def extract_key_points(content):
    """提取关键要点"""
    print("\n" + "="*50)
    print("关键要点提取")
    print("="*50)

    key_points = []

    # 按段落分割
    paragraphs = [p.strip() for p in content.split('\n\n') if p.strip()]

    for i, para in enumerate(paragraphs):
        # 检测关键句式
        if any(keyword in para for keyword in [
            '预计', '预测', '将', '预期', '有望', '有望达到', '预计达到',
            '增长', '下降', '提升', '降低', '变化', '调整'
        ]) and len(para) > 50:

            # 提取数字和百分比
            numbers = re.findall(r'\d+\.?\d*', para)
            percentages = re.findall(r'\d+%', para)

            key_points.append({
                'content': para,
                'page': i // 50 + 1,  # 估算页面
                'numbers': numbers,
                'percentages': percentages,
                'length': len(para)
            })

    # 显示关键要点（前15个）
    print("提取到关键要点：")
    for i, point in enumerate(key_points[:15]):
        print(f"\n要点 {i+1} (第{point['page']}页):")
        print(f"内容: {point['content'][:100]}...")
        print(f"数字: {point['numbers']}")
        print(f"百分比: {point['percentages']}")

    return key_points

def analyze_market_forecast(content):
    """分析市场预测部分"""
    print("\n" + "="*50)
    print("市场预测分析")
    print("="*50)

    # 预测相关关键词
    forecast_keywords = [
        '2026年', '预计', '预测', '将', '有望', '预期',
        '产量', '消费', '需求', '价格', '投资', '增长'
    ]

    forecast_content = []

    # 按段落分析预测内容
    paragraphs = [p.strip() for p in content.split('\n\n') if p.strip()]

    for para in paragraphs:
        if any(keyword in para for keyword in forecast_keywords):
            # 提取具体预测数据
            numbers = re.findall(r'\d+\.?\d*', para)
            if numbers:
                forecast_content.append({
                    'content': para,
                    'numbers': numbers,
                    'has_percentage': '%' in para
                })

    # 显示预测分析
    print("市场预测内容：")
    for i, forecast in enumerate(forecast_content[:10]):
        print(f"\n预测 {i+1}:")
        print(f"内容: {forecast['content'][:150]}...")
        print(f"具体数据: {forecast['numbers']}")
        print(f"包含百分比: {forecast['has_percentage']}")

    return forecast_content

def analyze_challenges_opportunities(content):
    """分析挑战与机遇"""
    print("\n" + "="*50)
    print("挑战与机遇分析")
    print("="*50)

    challenges = []
    opportunities = []

    # 挑战关键词
    challenge_keywords = [
        '挑战', '困难', '问题', '风险', '压力', '制约',
        '下降', '减少', '下降', '不足', '短缺', '限制'
    ]

    # 机遇关键词
    opportunity_keywords = [
        '机遇', '机会', '潜力', '优势', '利好', '支持',
        '增长', '提升', '扩大', '增加', '改善', '优化'
    ]

    paragraphs = [p.strip() for p in content.split('\n\n') if p.strip()]

    for para in paragraphs:
        if any(keyword in para for keyword in challenge_keywords):
            challenges.append(para)
        elif any(keyword in para for keyword in opportunity_keywords):
            opportunities.append(para)

    print(f"识别到 {len(challenges)} 个挑战相关内容")
    print(f"识别到 {len(opportunities)} 个机遇相关内容")

    # 显示挑战
    print("\n主要挑战：")
    for i, challenge in enumerate(challenges[:5]):
        print(f"{i+1}. {challenge[:100]}...")

    # 显示机遇
    print("\n主要机遇：")
    for i, opportunity in enumerate(opportunities[:5]):
        print(f"{i+1}. {opportunity[:100]}...")

    return challenges, opportunities

def analyze_industry_trends(content):
    """分析行业趋势"""
    print("\n" + "="*50)
    print("行业趋势分析")
    print("="*50)

    # 趋势关键词
    trend_keywords = [
        '趋势', '方向', '发展', '变化', '转型', '升级',
        '数字化', '智能化', '绿色化', '低碳', '环保'
    ]

    trend_content = []

    paragraphs = [p.strip() for p in content.split('\n\n') if p.strip()]

    for para in paragraphs:
        if any(keyword in para for keyword in trend_keywords):
            trend_content.append(para)

    print(f"识别到 {len(trend_content)} 个趋势相关内容")

    # 显示趋势
    print("行业趋势：")
    for i, trend in enumerate(trend_content[:8]):
        print(f"{i+1}. {trend[:120]}...")

    return trend_content

def extract_data_points(content):
    """提取具体数据点"""
    print("\n" + "="*50)
    print("数据点提取")
    print("="*50)

    data_points = []

    # 搜索各种数据格式
    patterns = [
        (r'\d+\.?\d*亿吨', '亿吨'),
        (r'\d+\.?\d*万亿元', '万亿元'),
        (r'\d+\.?\d*亿元', '亿元'),
        (r'\d+\.?\d*%', '百分比'),
        (r'\d+\.?\d*万', '万'),
        (r'\d+\.?\d*', '数字')
    ]

    paragraphs = [p.strip() for p in content.split('\n\n') if p.strip()]

    for para in paragraphs:
        for pattern, data_type in patterns:
            matches = re.findall(pattern, para)
            if matches:
                data_points.append({
                    'content': para,
                    'data_type': data_type,
                    'values': matches,
                    'page': paragraphs.index(para) // 50 + 1
                })

    # 显示数据点
    print("提取的数据点：")
    for i, data in enumerate(data_points[:15]):
        print(f"\n数据点 {i+1} (第{data['page']}页):")
        print(f"类型: {data['data_type']}")
        print(f"数值: {data['values']}")
        print(f"上下文: {data['content'][:100]}...")

    return data_points

def generate_summary(analysis_results):
    """生成总结报告"""
    print("\n" + "="*50)
    print("生成总结报告")
    print("="*50)

    summary = {
        'document_info': {
            'title': '2026年钢铁市场与行业展望',
            'analysis_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'total_pages': analysis_results.get('page_count', 0),
            'total_content_length': len(analysis_results.get('content', ''))
        },
        'key_findings': {
            'sections_count': len(analysis_results.get('sections', [])),
            'key_points_count': len(analysis_results.get('key_points', [])),
            'forecast_points_count': len(analysis_results.get('forecast_content', [])),
            'challenges_count': len(analysis_results.get('challenges', [])),
            'opportunities_count': len(analysis_results.get('opportunities', [])),
            'trends_count': len(analysis_results.get('trends', [])),
            'data_points_count': len(analysis_results.get('data_points', []))
        },
        'main_topics': [],
        'critical_insights': [],
        'recommendations': []
    }

    # 分析主要话题
    all_text = analysis_results.get('content', '')
    word_counts = Counter()

    # 简单的关键词统计
    keywords = ['钢铁', '市场', '2026', '产量', '需求', '价格', '政策', '环保', '技术', '数字化']
    for keyword in keywords:
        count = all_text.count(keyword)
        if count > 0:
            word_counts[keyword] = count

    summary['main_topics'] = word_counts.most_common(5)

    # 生成洞察
    summary['critical_insights'] = [
        "文档提供了2026年钢铁市场的全面展望",
        "包含产量、需求、价格等多维度预测",
        "涉及政策环境、技术趋势等重要因素",
        "提供了具体的量化指标和数据分析"
    ]

    # 生成建议
    summary['recommendations'] = [
        "重点关注政策变化对市场的影响",
        "密切关注技术升级带来的产业变革",
        "重视环保要求对生产成本的影响",
        "关注国内外市场需求变化趋势"
    ]

    return summary

def main():
    """主函数"""
    print("开始分析2026年钢铁市场与行业展望文档")
    print("="*60)

    # PDF文件路径
    pdf_path = "/Users/ibepo/Documents/GitHub/doc2/docs/P.A.R.A/01-Projects/ts/2026年钢铁市场与行业展望(终版)(4).pdf"

    # 1. 提取PDF内容
    content, page_count = extract_pdf_content(pdf_path)

    if content is None:
        print("PDF内容提取失败")
        return

    # 2. 文档结构分析
    sections = analyze_document_structure(content)

    # 3. 关键要点提取
    key_points = extract_key_points(content)

    # 4. 市场预测分析
    forecast_content = analyze_market_forecast(content)

    # 5. 挑战与机遇分析
    challenges, opportunities = analyze_challenges_opportunities(content)

    # 6. 行业趋势分析
    trends = analyze_industry_trends(content)

    # 7. 数据点提取
    data_points = extract_data_points(content)

    # 8. 生成总结报告
    analysis_results = {
        'content': content,
        'page_count': page_count,
        'sections': sections,
        'key_points': key_points,
        'forecast_content': forecast_content,
        'challenges': challenges,
        'opportunities': opportunities,
        'trends': trends,
        'data_points': data_points
    }

    summary = generate_summary(analysis_results)

    # 9. 保存分析结果
    output_file = "/Users/ibepo/Documents/GitHub/doc2/docs/P.A.R.A/01-Projects/ts/2026年钢铁市场分析结果.json"

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(analysis_results, f, ensure_ascii=False, indent=2)

    # 保存总结报告
    summary_file = "/Users/ibepo/Documents/GitHub/doc2/docs/P.A.R.A/01-Projects/ts/2026年钢铁市场总结报告.json"

    with open(summary_file, 'w', encoding='utf-8') as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)

    print(f"\n分析完成！")
    print(f"分析结果已保存到: {output_file}")
    print(f"总结报告已保存到: {summary_file}")

    # 显示统计信息
    print(f"\n文档统计信息：")
    print(f"- 总页数: {page_count}")
    print(f"- 总字符数: {len(content):,}")
    print(f"- 关键要点数: {len(key_points)}")
    print(f"- 预测内容数: {len(forecast_content)}")
    print(f"- 挑战点数: {len(challenges)}")
    print(f"- 机遇点数: {len(opportunities)}")
    print(f"- 趋势点数: {len(trends)}")
    print(f"- 数据点数: {len(data_points)}")

if __name__ == "__main__":
    main()