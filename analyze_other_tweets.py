#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
分析其他类别推文并重新分类
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
        return {}

def extract_content_from_tweets(tweets):
    """从推文数据中提取实际内容"""
    contents = []
    for tweet in tweets:
        # 推文数据格式是字符串，需要提取实际内容
        lines = tweet.strip().split('\n')
        # 通常推文内容在第一行（不包括时间戳）
        if lines:
            # 移除时间戳和元数据
            content_line = lines[0]
            if content_line.startswith('Published:'):
                # 如果是时间戳行，取下一个可能的内容行
                if len(lines) > 1:
                    content = lines[1].strip()
                else:
                    continue
            else:
                content = content_line.strip()

            if content and not content.startswith('View:') and not content.startswith('Engagement Rate:'):
                contents.append(content)

    return contents

def analyze_other_category_tweets(data):
    """分析其他类别推文特征"""
    other_tweets = data.get('其他', [])
    print(f"分析 {len(other_tweets)} 条其他类别推文")

    # 提取推文内容
    contents = extract_content_from_tweets(other_tweets)
    print(f"提取到 {len(contents)} 条有效推文内容")

    # 分析高频关键词
    def extract_keywords(texts):
        all_words = []
        for text in texts:
            # 简单的中文分词（基于常见分隔符）
            words = re.findall(r'[\u4e00-\u9fa5]+|[a-zA-Z]+|\d+|[^\w\s]', text)
            all_words.extend(words)

        # 过滤掉单字和标点
        filtered_words = [word for word in all_words if len(word) > 1 and word not in ['的', '了', '在', '是', '我', '有', '和', '就', '不', '这', '你', '都', '也', '要', '会', '他', '她', '它', '们', '说', '个', '对', '可以', '但是', '因为', '所以', '如果', '那么', '而且', '还有', '以及', '还是', '或者', '什么', '怎么', '为什么', '哪里', '什么时候', '就是', '就是', '就是', '就是']]

        word_count = Counter(filtered_words)
        return word_count.most_common(50)

    keywords = extract_keywords(contents)
    print("高频关键词TOP20:")
    for i, (word, count) in enumerate(keywords[:20], 1):
        print(f"  {i:2d}. {word}: {count}")

    return other_tweets, contents, keywords

def reclassify_contents(contents, keywords):
    """重新分类推文内容"""

    # 定义新的子类别关键词
    category_keywords = {
        '创业商业模式': {
            '创业': 60, '商业': 50, 'IP': 45, '流量': 40, '变现': 35,
            '粉丝': 35, '营销': 30, '品牌': 30, '产品': 30, '销售': 25,
            '客户': 25, '市场': 25, '竞争': 20, '收入': 20, '成本': 20,
            '利润': 20, '投资': 20, '回报': 20, '风险': 20, '机会': 20
        },
        'AI技术工具': {
            'AI': 70, '人工智能': 60, '模型': 50, '工具': 40, '技术': 35,
            '算法': 30, '数据': 30, '训练': 25, '应用': 25, '开发': 20,
            '代码': 20, '编程': 20, '软件': 20, '系统': 20, '功能': 20,
            '机器学习': 15, '深度学习': 15, '神经网络': 15
        },
        '认知思维': {
            '认知': 60, '思维': 50, '思考': 45, '逻辑': 40, '分析': 35,
            '理解': 35, '智慧': 25, '智商': 25, '智力': 25, '知识': 20,
            '学习': 20, '方法': 20, '策略': 20, '深度': 20, '本质': 20,
            '哲学': 20, '科学': 20, '研究': 20, '理论': 20, '概念': 20
        },
        '内容创作': {
            '内容': 60, '创作': 50, '写作': 45, '文案': 40, '表达': 35,
            '传播': 30, '发布': 30, '平台': 30, '媒体': 25, '文章': 25,
            '标题': 25, '结构': 25, '风格': 25, '技巧': 25, '写作': 25
        },
        '工作效率': {
            '效率': 60, '时间': 50, '管理': 45, '执行': 40, '任务': 35,
            '工作': 35, '计划': 30, '目标': 30, '结果': 30, '产出': 25,
            '优化': 25, '改进': 25, '提升': 25, '专注': 25, '习惯': 25
        },
        '学习成长': {
            '学习': 60, '成长': 50, '教育': 40, '培训': 35, '技能': 35,
            '能力': 35, '发展': 30, '进步': 30, '提升': 30, '改变': 25,
            '突破': 25, '蜕变': 25, '进步': 25, '成长': 25, '自我': 25
        },
        '生活健康': {
            '生活': 60, '健康': 50, '运动': 40, '饮食': 35, '睡眠': 35,
            '锻炼': 30, '身体': 30, '心理': 30, '情绪': 30, '压力': 25,
            '习惯': 25, '日常': 25, '家庭': 25, '朋友': 25, '关系': 25
        },
        '投资理财': {
            '投资': 60, '理财': 50, '金钱': 40, '收益': 35, '财务': 35,
            '基金': 30, '股票': 30, '回报': 30, '风险': 30, '资产': 25,
            '收入': 25, '支出': 25, '储蓄': 25, '理财': 25, '财富': 25
        }
    }

    reclassified = []
    uncategorized = []

    for content in contents:
        scores = {}

        # 计算每个类别的得分
        for category, keywords_dict in category_keywords.items():
            score = 0
            for keyword, weight in keywords_dict.items():
                if keyword in content:
                    score += weight
            scores[category] = score

        # 找到最高分的类别
        if max(scores.values()) > 40:  # 设置阈值
            best_category = max(scores, key=scores.get)
            reclassified.append({
                'content': content,
                'category': best_category,
                'score': scores[best_category],
                'keywords': [kw for kw, wt in keywords_dict.items() if kw in content]
            })
        else:
            uncategorized.append({
                'content': content,
                'category': '其他',
                'score': 0
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
    total_classified = 0
    for category, tweets in category_stats.items():
        count = len(tweets)
        total_classified += count
        print(f"{category}: {count} 条推文")

    print(f"\n总计分类: {total_classified} 条")
    print(f"未分类: {len(uncategorized)} 条")

    # 分析各类别的典型内容
    for category, tweets in category_stats.items():
        print(f"\n=== {category} 类别典型推文 (TOP3) ===")
        # 按分数排序，展示得分最高的推文
        sorted_tweets = sorted(tweets, key=lambda x: x['score'], reverse=True)
        for i, tweet in enumerate(sorted_tweets[:3]):  # 展示前3个最典型的推文
            keywords_str = ', '.join(tweet['keywords'][:3]) if tweet['keywords'] else '无'
            print(f"{i+1}. ({tweet['score']}分) {tweet['content']}")
            print(f"   关键词: {keywords_str}")

    return category_stats

def main():
    """主函数"""
    print("开始分析并重新分类 dontbesilent 其他类别推文...")

    # 加载数据
    data = load_data()
    if not data:
        print("无法加载数据，退出")
        return

    # 分析其他类别推文
    other_tweets, contents, keywords = analyze_other_category_tweets(data)

    if not contents:
        print("未找到有效推文内容，退出")
        return

    # 重新分类
    reclassified, uncategorized = reclassify_contents(contents, keywords)

    # 详细分析结果
    category_stats = detailed_analysis(reclassified, uncategorized)

    # 保存结果
    output_data = {
        'original_count': len(contents),
        'reclassified_count': len(reclassified),
        'uncategorized_count': len(uncategorized),
        'reclassified_tweets': reclassified,
        'uncategorized_tweets': uncategorized,
        'category_statistics': {cat: len(tweets) for cat, tweets in category_stats.items()},
        'analysis_keywords': keywords,
        'summary': {
            'total_processed': len(contents),
            'successfully_classified': len(reclassified),
            'classification_rate': f"{len(reclassified)/len(contents)*100:.1f}%",
            'remaining_uncategorized': len(uncategorized)
        }
    }

    with open('other_tweets_analysis.json', 'w', encoding='utf-8') as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)

    print(f"\n分析完成！结果已保存到 other_tweets_analysis.json")
    print(f"处理推文: {len(contents)} 条")
    print(f"成功分类: {len(reclassified)} 条")
    print(f"分类成功率: {len(reclassified)/len(contents)*100:.1f}%")
    print(f"未分类: {len(uncategorized)} 条")

if __name__ == "__main__":
    main()