#!/usr/bin/env python3
"""
使用 Playwright 获取微信公众号专辑中的所有文章链接
"""
import asyncio
import json
from playwright.async_api import async_playwright

async def get_album_articles():
    """使用 Playwright 获取专辑文章链接"""
    album_url = "https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MjM5MjAzODU2MA==&action=getalbum&album_id=3099088215745052674&subscene=159&subscene=190"

    print(f"正在启动浏览器...")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(viewport={'width': 1280, 'height': 800})
        page = await context.new_page()

        print(f"正在加载专辑页面...")
        await page.goto(album_url, wait_until="networkidle")

        # 等待页面加载
        print("等待页面完全加载...")
        await asyncio.sleep(5)

        # 滚动以加载所有文章
        print("滚动页面...")
        for i in range(10):
            await page.evaluate("window.scrollBy(0, 800)")
            await asyncio.sleep(1)

        # 回到顶部
        await page.evaluate("window.scrollTo(0, 0)")
        await asyncio.sleep(2)

        # 保存完整HTML用于分析
        html_content = await page.content()
        with open('/Users/ibepo/Documents/GitHub/doc2/02-areas/album_page_full.html', 'w', encoding='utf-8') as f:
            f.write(html_content)
        print("完整HTML已保存")

        # 从页面中提取文章信息
        print("\n=== 提取文章信息 ===")

        articles_info = await page.evaluate("""() => {
            const results = [];

            // 查找所有文章卡片
            // 微信专辑的文章通常在以下几种元素中
            const selectors = [
                '.album__item',
                '.article-item',
                '[data-id]',
                'a[href*="mp.weixin.qq.com"]',
                '.wx-appmsg-item'
            ];

            for (const selector of selectors) {
                const elements = document.querySelectorAll(selector);
                console.log(`选择器 ${selector}: 找到 ${elements.length} 个元素`);

                elements.forEach((elem, idx) => {
                    // 获取链接
                    const link = elem.href || elem.querySelector('a')?.href;
                    // 获取标题
                    const title = elem.textContent?.trim() ||
                                  elem.querySelector('.title')?.textContent?.trim() ||
                                  elem.getAttribute('data-title');

                    if (link && link.includes('mp.weixin.qq.com')) {
                        results.push({
                            selector: selector,
                            index: idx,
                            link: link,
                            title: title
                        });
                    }
                });
            }

            // 尝试从所有链接中查找
            const allLinks = document.querySelectorAll('a');
            allLinks.forEach((a) => {
                const href = a.getAttribute('href');
                if (href && href.includes('mp.weixin.qq.com/s/')) {
                    const title = a.textContent?.trim() || a.querySelector('.title')?.textContent?.trim();
                    results.push({
                        selector: 'all_links',
                        link: href,
                        title: title
                    });
                }
            });

            return results;
        }""")

        print(f"找到 {len(articles_info)} 条文章信息")

        # 去重并保存
        seen_links = set()
        unique_articles = []

        for article in articles_info:
            link = article.get('link', '')
            if link and link not in seen_links:
                seen_links.add(link)
                unique_articles.append(article)

        print(f"去重后: {len(unique_articles)} 篇文章")

        # 保存结果
        with open('/Users/ibepo/Documents/GitHub/doc2/02-areas/articles_info.json', 'w', encoding='utf-8') as f:
            json.dump(unique_articles, f, ensure_ascii=False, indent=2)

        # 提取链接列表
        links = [a['link'] for a in unique_articles if a.get('link')]

        await asyncio.sleep(3)
        await browser.close()

        return links

async def main():
    articles = await get_album_articles()

    print(f"\n{'='*50}")
    print(f"找到 {len(articles)} 篇文章:")
    for i, link in enumerate(articles, 1):
        print(f"{i}. {link}")

    # 保存链接
    output_file = "/Users/ibepo/Documents/GitHub/doc2/02-areas/album_links.txt"
    with open(output_file, 'w') as f:
        for link in articles:
            f.write(link + '\n')

    print(f"\n链接已保存到: {output_file}")

    # 保存完整HTML文件供分析
    print(f"\n完整HTML已保存到: album_page_full.html")
    print(f"文章信息已保存到: articles_info.json")

if __name__ == '__main__':
    asyncio.run(main())
