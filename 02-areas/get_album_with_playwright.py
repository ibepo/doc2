#!/usr/bin/env python3
"""
使用 Playwright 监听网络请求获取微信公众号专辑文章
"""
import asyncio
import json
from playwright.async_api import async_playwright

async def get_album_articles():
    """通过监听网络请求获取专辑文章链接"""
    album_url = "https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MjM5MjAzODU2MA==&action=getalbum&album_id=3099088215745052674&subscene=159&subscene=190"

    print(f"正在启动浏览器...")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(viewport={'width': 1280, 'height': 800})
        page = await context.new_page()

        # 存储拦截到的请求
        api_responses = []

        # 监听网络响应
        async def handle_response(response):
            # 只关注包含 appmsg 或 album 的 API 响应
            url = response.url
            if any(keyword in url for keyword in ['appmsg', 'album', 'homepage']):
                if 'ajax=1' in url or 'f=json' in url:
                    print(f"捕获到API请求: {url}")
                    try:
                        data = await response.json()
                        api_responses.append({
                            'url': url,
                            'status': response.status,
                            'data': data
                        })
                        print(f"  状态: {response.status}, 数据大小: {len(str(data))}")
                    except:
                        try:
                            text = await response.text()
                            if text:
                                api_responses.append({
                                    'url': url,
                                    'status': response.status,
                                    'text': text[:1000]
                                })
                                print(f"  文本响应: {text[:200]}")
                        except:
                            pass

        page.on('response', handle_response)

        print(f"正在加载专辑页面...")
        await page.goto(album_url, wait_until="networkidle")

        # 等待页面加载
        print("等待页面和数据加载...")
        await asyncio.sleep(8)

        # 滚动以触发加载更多数据的请求
        print("滚动页面触发数据加载...")
        for i in range(15):
            await page.evaluate("window.scrollBy(0, 1000)")
            await asyncio.sleep(1)

        # 等待所有请求完成
        await asyncio.sleep(3)

        # 保存所有捕获的API响应
        print(f"\n=== 捕获到 {len(api_responses)} 个API响应 ===")
        with open('/Users/ibepo/Documents/GitHub/doc2/02-areas/api_responses.json', 'w', encoding='utf-8') as f:
            json.dump(api_responses, f, ensure_ascii=False, indent=2)

        # 从API响应中提取文章链接
        article_links = []

        for resp in api_responses:
            data = resp.get('data', {})
            data_str = json.dumps(data, ensure_ascii=False)

            # 搜索文章链接
            import re
            link_pattern = r'https://mp\.weixin\.qq\.com/s/[^"\'\s<>]+'
            links = re.findall(link_pattern, data_str)

            for link in links:
                # 清理链接
                clean_link = link.split('&')[0]
                if clean_link not in article_links:
                    article_links.append(clean_link)

        print(f"\n从API响应中提取到 {len(article_links)} 个文章链接")

        await asyncio.sleep(2)
        await browser.close()

        return article_links

async def main():
    articles = await get_album_articles()

    print(f"\n{'='*60}")
    print(f"找到 {len(articles)} 篇文章:")
    for i, link in enumerate(articles, 1):
        print(f"{i}. {link}")

    # 保存链接
    output_file = "/Users/ibepo/Documents/GitHub/doc2/02-areas/album_links.txt"
    with open(output_file, 'w') as f:
        for link in articles:
            f.write(link + '\n')

    print(f"\n链接已保存到: {output_file}")
    print(f"API响应数据已保存到: api_responses.json")

if __name__ == '__main__':
    asyncio.run(main())
