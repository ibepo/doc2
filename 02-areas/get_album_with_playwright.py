#!/usr/bin/env python3
"""
使用 Playwright 获取微信公众号专辑中的所有文章链接
"""
import asyncio
import re
from playwright.async_api import async_playwright

async def get_album_articles():
    """使用 Playwright 获取专辑文章链接"""
    album_url = "https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MjM5MjAzODU2MA==&action=getalbum&album_id=3099088215745052674&subscene=159&subscene=190"

    print(f"正在启动 Playwright...")

    async with async_playwright() as p:
        # 使用 Chromium 浏览器
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        print(f"正在加载专辑页面...")
        await page.goto(album_url, wait_until="networkidle")

        # 等待页面加载完成
        await asyncio.sleep(3)

        # 尝试滚动页面以加载更多内容
        for i in range(5):
            await page.evaluate("window.scrollBy(0, 1000)")
            await asyncio.sleep(1)

        # 获取页面内容
        content = await page.content()

        # 查找所有文章链接
        article_links = set()

        # 方法1: 从页面中查找所有链接
        links = await page.locator("a").all()
        print(f"找到 {len(links)} 个链接标签")

        for link in links:
            href = await link.get_attribute("href")
            if href and "mp.weixin.qq.com/s/" in href:
                # 清理链接
                clean_link = href.split("&")[0] if "&" in href else href
                article_links.add(clean_link)

        # 方法2: 使用正则表达式从页面内容中提取
        pattern = r'https://mp\.weixin\.qq\.com/s/[^"\'\s<>]+'
        matches = re.findall(pattern, content)
        for match in matches:
            clean_link = match.split("&")[0] if "&" in match else match
            article_links.add(clean_link)

        # 方法3: 从页面脚本中提取
        scripts = await page.locator("script").all()
        for script in scripts:
            script_content = await script.inner_text()
            if script_content:
                matches = re.findall(pattern, script_content)
                for match in matches:
                    clean_link = match.split("&")[0] if "&" in match else match
                    article_links.add(clean_link)

        # 方法4: 尝试从 window 对象中获取数据
        try:
            appmsg_list = await page.evaluate("""() => {
                if (window.appmsglist) {
                    return window.appmsglist;
                }
                if (window.msgList) {
                    return window.msgList;
                }
                return null;
            }""")

            if appmsg_list:
                print(f"从 window 对象找到数据!")
                # 解析数据获取链接
        except Exception as e:
            print(f"从 window 对象获取数据失败: {e}")

        await browser.close()

        return list(article_links)

async def main():
    articles = await get_album_articles()

    print(f"\n找到 {len(articles)} 篇文章:")
    for i, link in enumerate(articles, 1):
        print(f"{i}. {link}")

    # 保存到文件
    output_file = "/Users/ibepo/Documents/GitHub/doc2/02-areas/album_links.txt"
    with open(output_file, 'w') as f:
        for link in articles:
            f.write(link + '\n')

    print(f"\n链接已保存到: {output_file}")

if __name__ == '__main__':
    asyncio.run(main())
