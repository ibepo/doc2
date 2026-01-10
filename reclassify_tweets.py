#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
dontbesilent推文重新分类脚本
分析并重新分类"其他"类别中的5624条推文
"""

import re
import json
from collections import Counter

def load_data():
    """加载推文分类数据"""
    try:
        with open('tweet_classification_optimized.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("警告: 未找到分类数据文件")
        return []

def analyze_other_category_tweets(data):
    """分析其他类别推文特征"""
    other_tweets = [item for item in data if item['category'] == '其他']
    print(f"分析 {len(other_tweets)} 条其他类别推文")

    # 提取推文内容
    contents = [tweet['content'] for tweet in other_tweets]

    # 分析高频关键词
    def extract_keywords(texts):
        all_words = []
        for text in texts:
            # 简单的中文分词（基于常见分隔符）
            words = re.findall(r'[\u4e00-\u9fa5]+|[a-zA-Z]+|\d+|[^\w\s]', text)
            all_words.extend(words)

        # 过滤掉单字和标点
        filtered_words = [word for word in all_words if len(word) > 1 and word not in ['的', '了', '在', '是', '我', '有', '和', '就', '不', '这', '你', '都', '也', '要', '会', '他', '她', '它', '们', '说', '个', '对', '可以', '但是', '因为', '所以', '如果', '那么', '而且', '还有', '以及', '还是', '或者', '什么', '怎么', '为什么', '哪里', '什么时候']]

        word_count = Counter(filtered_words)
        return word_count.most_common(50)

    keywords = extract_keywords(contents)
    print("高频关键词TOP20:")
    for word, count in keywords[:20]:
        print(f"  {word}: {count}")

    return other_tweets, keywords

def reclassify_tweets(other_tweets, keywords):
    """重新分类推文"""

    # 定义新的子类别关键词
    category_keywords = {
        '创业商业模式': {
            '创业': 50, '商业': 45, 'IP': 40, '流量': 35, '变现': 30,
            '粉丝': 30, '营销': 25, '品牌': 25, '产品': 25, '销售': 20,
            '客户': 20, '市场': 20, '竞争': 15, '收入': 15, '成本': 15,
            '利润': 15, '投资': 15, '回报': 15, '风险': 15, '机会': 15
        },
        'AI技术工具': {
            'AI': 60, '人工智能': 50, '模型': 40, '工具': 35, '技术': 30,
            '算法': 25, '数据': 25, '训练': 20, '应用': 20, '开发': 15,
            '代码': 15, '编程': 15, '软件': 15, '系统': 15, '功能': 15
        },
        '认知思维': {
            '认知': 50, '思维': 40, '思考': 35, '逻辑': 30, '分析': 25,
            '理解': 25, '智慧': 20, '智商': 20, '智力': 20, '知识': 15,
            '学习': 15, '方法': 15, '策略': 15, '深度': 15, '本质': 15,
            '哲学': 15, '科学': 15, '研究': 15, '理论': 15, '概念': 15
        },
        '内容创作': {
            '内容': 50, '创作': 40, '写作': 35, '文案': 30, '写作': 25,
            '表达': 25, '传播': 20, '发布': 20, '平台': 20, '媒体': 15,
            '文章': 15, '标题': 15, '结构': 15, '风格': 15, '技巧': 15
        },
        '工作效率': {
            '效率': 50, '时间': 40, '管理': 35, '执行': 30, '任务': 25,
            '工作': 25, '计划': 20, '目标': 20, '结果': 20, '产出': 15,
            '优化': 15, '改进': 15, '提升': 15, '专注': 15, '习惯': 15
        },
        '学习成长': {
            '学习': 50, '成长': 40, '教育': 30, '培训': 25, '技能': 25,
            '能力': 25, '发展': 20, '进步': 20, '提升': 20, '改变': 15,
            '突破': 15, '蜕变': 15, '进步': 15, '成长': 15, '自我': 15
        },
        '生活健康': {
            '生活': 50, '健康': 40, '运动': 30, '饮食': 25, '睡眠': 25,
            '锻炼': 20, '身体': 20, '心理': 20, '情绪': 20, '压力': 15,
            '习惯': 15, '日常': 15, '家庭': 15, '朋友': 15, '关系': 15
        },
        '投资理财': {
            '投资': 50, '理财': 40, '金钱': 30, '收益': 25, '财务': 25,
            '基金': 20, '股票': 20, '回报': 20, '风险': 20, '资产': 15,
            '收入': 15, '支出': 15, '储蓄': 15, '理财': 15, '财富': 15
        }
    }

    reclassified = []
    uncategorized = []

    for tweet in other_tweets:
        content = tweet['content']
        scores = {}

        # 计算每个类别的得分
        for category, keywords_dict in category_keywords.items():
            score = 0
            for keyword, weight in keywords_dict.items():
                if keyword in content:
                    score += weight
            scores[category] = score

        # 找到最高分的类别
        if max(scores.values()) > 30:  # 设置阈值
            best_category = max(scores, key=scores.get)
            reclassified.append({
                'content': content,
                'category': best_category,
                'score': scores[best_category],
                'original_tweet_id': tweet.get('id', 'unknown')
            })
        else:
            uncategorized.append({
                'content': content,
                'category': '其他',
                'score': 0,
                'original_tweet_id': tweet.get('id', 'unknown')
            })

    return reclassified, uncategorized

def detailed_analysis(reclassified, uncategorized):
    """详细分析重新分类结果"""
    # 按类别统计
    category_stats = {}
    for item in reclassified:
        category = item['category']
        if category not in category_stats:
            category_stats[category] = []
        category_stats[category].append(item)

    print("\n=== 重新分类结果 ===")
    for category, tweets in category_stats.items():
        print(f"{category}: {len(tweets)} 条推文")

    print(f"\n未分类: {len(uncategorized)} 条推文")

    # 分析各类别的典型内容
    for category, tweets in category_stats.items():
        print(f"\n=== {category} 类别典型推文 ===")
        # 按分数排序，展示得分最高的推文
        sorted_tweets = sorted(tweets, key=lambda x: x['score'], reverse=True)
        for i, tweet in enumerate(sorted_tweets[:3]):  # 展示前3个最典型的推文
            print(f"{i+1}. ({tweet['score']}分) {tweet['content']}")

    return category_stats

def main():
    """主函数"""
    print("开始重新分类 dontbesilent 推文...")

    # 加载数据
    data = load_data()
    if not data:
        print("无法加载数据，退出")
        return

    # 分析其他类别推文
    other_tweets, keywords = analyze_other_category_tweets(data)

    # 重新分类
    reclassified, uncategorized = reclassify_tweets(other_tweets, keywords)

    # 详细分析结果
    category_stats = detailed_analysis(reclassified, uncategorized)

    # 保存结果
    output_data = {
        'reclassified_tweets': reclassified,
        'uncategorized_tweets': uncategorized,
        'category_statistics': {cat: len(tweets) for cat, tweets in category_stats.items()},
        'analysis_keywords': keywords
    }

    with open('reclassified_results.json', 'w', encoding='utf-8') as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)

    print(f"\n分析完成！结果已保存到 reclassified_results.json")
    print(f"重新分类: {len(reclassified)} 条")
    print(f"未分类: {len(uncategorized)} 条")

if __name__ == "__main__":
    main()