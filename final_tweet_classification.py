#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
最终推文重新分类脚本
完整处理所有推文，清理数据并重新分类
"""

import re
import json
from collections import Counter

def load_and_clean_data():
    """加载并清理推文数据"""
    try:
        with open('tweet_classification_optimized.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        print("警告: 未找到分类数据文件")
        return {}

def clean_tweet_text(text):
    """清理推文文本"""
    # 移除控制字符
    text = re.sub(r'[\x00-\x1f\x7f-\x9f]', '', text)
    # 移除时间戳格式
    text = re.sub(r'Published: \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', '', text)
    # 移除统计数据行
    text = re.sub(r'View: \d+ Repost: \d+ Reply: \d+ Like: \d+ Bookmark: \d+', '', text)
    text = re.sub(r'Engagement Rate: \d+\.\d+% View on X', '', text)
    # 移除多余空白
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def extract_all_tweets(data):
    """提取所有推文内容"""
    all_tweets = []

    for category, tweets in data.items():
        for tweet in tweets:
            cleaned = clean_tweet_text(tweet)
            if cleaned and len(cleaned) > 5:  # 过滤过短的内容
                all_tweets.append({
                    'category': category,
                    'content': cleaned,
                    'original': tweet
                })

    print(f"总共提取到 {len(all_tweets)} 条有效推文")
    return all_tweets

def analyze_content_distribution(all_tweets):
    """分析内容分布"""
    category_counts = {}
    content_lengths = []

    for tweet in all_tweets:
        category = tweet['category']
        content = tweet['content']

        if category not in category_counts:
            category_counts[category] = 0
        category_counts[category] += 1

        content_lengths.append(len(content))

    print("=== 当前分类统计 ===")
    for category, count in sorted(category_counts.items()):
        print(f"{category}: {count} 条")

    print(f"\n内容长度统计:")
    print(f"平均长度: {sum(content_lengths)/len(content_lengths):.1f} 字符")
    print(f"最短: {min(content_lengths)} 字符")
    print(f"最长: {max(content_lengths)} 字符")

    return category_counts

def reclassify_all_tweets(all_tweets):
    """重新分类所有推文"""

    # 定义详细的关键词体系
    category_keywords = {
        '创业商业模式': {
            '创业': 70, '商业': 60, 'IP': 55, '流量': 50, '变现': 45,
            '粉丝': 45, '营销': 40, '品牌': 40, '产品': 40, '销售': 35,
            '客户': 35, '市场': 35, '竞争': 30, '收入': 30, '成本': 30,
            '利润': 30, '投资': 30, '回报': 30, '风险': 30, '机会': 30,
            '模式': 25, '定价': 25, '渠道': 25, '转化': 25, '获客': 25,
            '陪跑': 40, '高客单': 35, '业务': 20, '商业': 60
        },
        'AI技术工具': {
            'AI': 80, '人工智能': 70, '模型': 60, '工具': 50, '技术': 45,
            '算法': 40, '数据': 40, '训练': 35, '应用': 35, '开发': 30,
            '代码': 30, '编程': 30, '软件': 30, '系统': 30, '功能': 30,
            '机器学习': 25, '深度学习': 25, '神经网络': 25, 'ChatGPT': 35,
            'Gemini': 35, '豆包': 35, 'Manus': 35, 'Claude': 35,
            'AI时代': 30, 'AI浪潮': 30, 'AI产品': 30
        },
        '认知思维': {
            '认知': 70, '思维': 60, '思考': 55, '逻辑': 50, '分析': 45,
            '理解': 45, '智慧': 35, '智商': 35, '智力': 35, '知识': 30,
            '学习': 30, '方法': 30, '策略': 30, '深度': 30, '本质': 30,
            '哲学': 30, '科学': 30, '研究': 30, '理论': 30, '概念': 30,
            '批判': 25, '反思': 25, '元认知': 40, '思维模式': 25
        },
        '内容创作': {
            '内容': 70, '创作': 60, '写作': 55, '文案': 50, '表达': 45,
            '传播': 40, '发布': 40, '平台': 40, '媒体': 35, '文章': 35,
            '标题': 35, '结构': 35, '风格': 35, '技巧': 35, '写作': 35,
            '选题': 40, '流量': 30, '传播': 30, '自媒体': 30, 'IP': 25
        },
        '工作效率': {
            '效率': 70, '时间': 60, '管理': 55, '执行': 50, '任务': 45,
            '工作': 45, '计划': 40, '目标': 40, '结果': 40, '产出': 35,
            '优化': 35, '改进': 35, '提升': 35, '专注': 35, '习惯': 35,
            '执行力': 30, '时间管理': 30, '效率提升': 30
        },
        '学习成长': {
            '学习': 70, '成长': 60, '教育': 50, '培训': 45, '技能': 45,
            '能力': 45, '发展': 40, '进步': 40, '提升': 40, '改变': 35,
            '突破': 35, '蜕变': 35, '进步': 35, '成长': 35, '自我': 35,
            '成长': 60, '学习': 70
        },
        '生活健康': {
            '生活': 70, '健康': 60, '运动': 50, '饮食': 45, '睡眠': 45,
            '锻炼': 40, '身体': 40, '心理': 40, '情绪': 40, '压力': 35,
            '习惯': 35, '日常': 35, '家庭': 35, '朋友': 35, '关系': 35,
            '原生家庭': 40, '父母': 30, '子女': 30, '创伤': 25
        },
        '投资理财': {
            '投资': 70, '理财': 60, '金钱': 50, '收益': 45, '财务': 45,
            '基金': 40, '股票': 40, '回报': 40, '风险': 40, '资产': 35,
            '收入': 35, '支出': 35, '储蓄': 35, '理财': 35, '财富': 35,
            '投资': 70, '理财': 60, '财务': 45
        }
    }

    reclassified = []

    for tweet in all_tweets:
        content = tweet['content']
        original_category = tweet['category']

        # 如果已经在有效分类中，保留原分类
        if original_category != '其他':
            reclassified.append({
                'content': content,
                'category': original_category,
                'score': 100,  # 原始分类给予高分
                'method': 'original_classification'
            })
            continue

        # 对"其他"类推文进行重新分类
        scores = {}

        for category, keywords_dict in category_keywords.items():
            score = 0
            matched_keywords = []

            for keyword, weight in keywords_dict.items():
                if keyword in content:
                    score += weight
                    matched_keywords.append(keyword)

            scores[category] = {'score': score, 'keywords': matched_keywords}

        # 找到最高分的类别
        if scores:
            best_category = max(scores.keys(), key=lambda x: scores[x]['score'])
            best_score = scores[best_category]['score']

            if best_score > 30:  # 设置合理的阈值
                reclassified.append({
                    'content': content,
                    'category': best_category,
                    'score': best_score,
                    'method': 'reclassification',
                    'matched_keywords': scores[best_category]['keywords']
                })
            else:
                reclassified.append({
                    'content': content,
                    'category': '其他',
                    'score': 0,
                    'method': 'uncategorized'
                })
        else:
            reclassified.append({
                'content': content,
                'category': '其他',
                'score': 0,
                'method': 'uncategorized'
            })

    return reclassified

def analyze_final_results(reclassified):
    """分析最终分类结果"""

    category_stats = {}
    method_stats = {}

    for item in reclassified:
        category = item['category']
        method = item['method']

        if category not in category_stats:
            category_stats[category] = []
        category_stats[category].append(item)

        if method not in method_stats:
            method_stats[method] = 0
        method_stats[method] += 1

    print("\n=== 最终分类结果 ===")
    total_classified = 0
    for category, tweets in sorted(category_stats.items()):
        count = len(tweets)
        total_classified += count
        print(f"{category}: {count} 条推文")

    print(f"\n=== 分类方法统计 ===")
    for method, count in sorted(method_stats.items()):
        print(f"{method}: {count} 条")

    print(f"\n=== 分类完成率 ===")
    print(f"总计处理: {len(reclassified)} 条")
    print(f"有效分类: {total_classified} 条")
    print(f"分类成功率: {total_classified/len(reclassified)*100:.1f}%")

    # 展示各类别的代表性内容
    print("\n=== 各类别代表性内容 ===")
    for category, tweets in category_stats.items():
        if category != '其他':
            print(f"\n📁 {category} (TOP3):")
            # 按分数排序，展示高分推文
            sorted_tweets = sorted(tweets, key=lambda x: x['score'], reverse=True)
            for i, tweet in enumerate(sorted_tweets[:3]):
                if tweet['method'] == 'original_classification':
                    source = "原始分类"
                elif tweet['method'] == 'reclassification':
                    source = "重新分类"
                    keywords_str = ', '.join(tweet.get('matched_keywords', [])[:2])
                    print(f"  {i+1}. ({tweet['score']}分) {tweet['content']}")
                    print(f"     关键词: {keywords_str} [{source}]")
                    continue
                else:
                    source = "未分类"
                print(f"  {i+1}. {tweet['content']} [{source}]")

def save_final_results(reclassified):
    """保存最终分类结果"""

    # 按类别重新整理
    final_data = {}
    for item in reclassified:
        category = item['category']
        if category not in final_data:
            final_data[category] = []
        final_data[category].append(item['content'])

    # 保存完整结果
    complete_output = {
        'detailed_classification': reclassified,
        'organized_by_category': final_data,
        'summary': {
            'total_tweets': len(reclassified),
            'categories': {cat: len(tweets) for cat, tweets in final_data.items()}
        }
    }

    with open('final_tweet_classification.json', 'w', encoding='utf-8') as f:
        json.dump(complete_output, f, ensure_ascii=False, indent=2)

    # 保存格式化的分类结果用于文档
    document_output = {}
    for category, tweets in final_data.items():
        document_output[category] = tweets

    with open('tweets_for_document.md', 'w', encoding='utf-8') as f:
        f.write("# dontbesilent 推文完整分类整理\n\n")
        f.write("## 分类统计\n\n")
        for category, count in final_data.items():
            f.write(f"- **{category}**: {len(count)} 条\n")
        f.write(f"\n- **总计**: {sum(len(tweets) for tweets in final_data.values())} 条\n\n")

        f.write("## 完整推文分类\n\n")
        for category, tweets in sorted(final_data.items()):
            f.write(f"### {category} ({len(tweets)} 条)\n\n")
            for i, tweet in enumerate(tweets, 1):
                f.write(f"{i}. {tweet}\n\n")
            f.write("---\n\n")

    print(f"\n结果已保存到:")
    print(f"  - final_tweet_classification.json (完整数据)")
    print(f"  - tweets_for_document.md (文档格式)")

def main():
    """主函数"""
    print("开始完整的推文重新分类处理...")

    # 加载和清理数据
    data = load_and_clean_data()
    if not data:
        print("无法加载数据，退出")
        return

    # 提取所有推文
    all_tweets = extract_all_tweets(data)

    # 分析当前分布
    category_counts = analyze_content_distribution(all_tweets)

    # 重新分类
    reclassified = reclassify_all_tweets(all_tweets)

    # 分析最终结果
    analyze_final_results(reclassified)

    # 保存结果
    save_final_results(reclassified)

    print(f"\n🎉 推文重新分类处理完成！")

if __name__ == "__main__":
    main()