#!/usr/bin/env python3
"""
获取微信公众号专辑中的所有文章链接
"""
import requests
from bs4 import BeautifulSoup
import json
import re

def get_album_articles(album_url):
    """获取专辑中所有文章链接"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/120.0.0.0 Safari/537.36'
    }

    print(f"正在抓取专辑页面...")
    response = requests.get(album_url, headers=headers, timeout=30)
    response.raise_for_status()
    response.encoding = 'utf-8'

    html = response.text

    # 方法1: 从页面中提取文章链接
    article_links = []

    # 微信公众号文章链接格式
    pattern = r'https://mp\.weixin\.qq\.com/s/[^"\'\s<>]+'
    links = re.findall(pattern, html)
    article_links.extend(links)

    # 方法2: 尝试从 script 标签中提取数据
    soup = BeautifulSoup(html, 'html.parser')
    for script in soup.find_all('script'):
        script_text = script.string
        if script_text and 'mp.weixin.qq.com' in script_text:
            links = re.findall(pattern, script_text)
            article_links.extend(links)

    # 去重
    article_links = list(set(article_links))

    return article_links

def main():
    album_url = "https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MjM5MjAzODU2MA==&action=getalbum&album_id=3099088215745052674&subscene=159&subscene=190"

    articles = get_album_articles(album_url)

    print(f"\n找到 {len(articles)} 篇文章:")
    for i, link in enumerate(articles, 1):
        print(f"{i}. {link}")

    # 保存到文件
    with open('/Users/ibepo/Documents/GitHub/doc2/02-areas/album_links.txt', 'w') as f:
        for link in articles:
            f.write(link + '\n')

    print(f"\n链接已保存到: /Users/ibepo/Documents/GitHub/doc2/02-areas/album_links.txt")

if __name__ == '__main__':
    main()
