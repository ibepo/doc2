#!/usr/bin/env python3
"""微信专辑下载工具 - 直接解析专辑API"""

import asyncio
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import urlparse, parse_qs

import requests
from bs4 import BeautifulSoup

# 专辑链接
ALBUM_URL = "https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzkyMDUyMDM2Mg==&action=getalbum&album_id=3066189657429901313&subscene=231"

# 输出目录
OUTPUT_DIR = Path(
    "/Users/ibepo/Documents/GitHub/doc2/docs/P.A.R.A/03-Resources/微信公众号"
)


def extract_album_info(url):
    """从专辑URL中提取信息"""
    params = parse_qs(urlparse(url).query)
    return {
        "biz": params.get("__biz", [""])[0],
        "album_id": params.get("album_id", [""])[0],
    }


def fetch_album_articles(biz, album_id):
    """通过API获取专辑文章列表"""
    print(f"正在获取专辑文章列表...")

    articles = []

    # 微信专辑API
    api_url = "https://mp.weixin.qq.com/mp/profile_ext"
    params = {
        "__biz": biz,
        "action": "getalbum",
        "album_id": album_id,
        "count": 20,
        "begin": 0,
        "f": "json",
    }

    # 分页获取
    begin = 0
    while True:
        params["begin"] = begin
        print(f"  获取偏移 {begin} 的文章...")

        try:
            response = requests.get(api_url, params=params, timeout=30)
            response.raise_for_status()
            data = response.json()

            if "getalbum_resp" not in data:
                print(f"  API响应异常: {data.keys()}")
                break

            album_resp = data["getalbum_resp"]
            article_list = album_resp.get("article_list", [])

            if not article_list:
                print(f"  没有更多文章了")
                break

            print(f"  获取到 {len(article_list)} 篇文章")

            for article in article_list:
                articles.append(
                    {
                        "title": article.get("title", ""),
                        "url": article.get("url", ""),
                        "update_time": article.get("update_time", 0),
                    }
                )

            # 检查是否还有更多文章
            if len(article_list) < 20:
                break

            begin += 20

        except Exception as e:
            print(f"  错误: {e}")
            break

    return articles


def download_article(url, output_dir, save_images=True):
    """下载单篇文章"""
    wechat2md = Path(__file__).parent / "wechat2md.py"

    if not wechat2md.exists():
        print(f"  错误: 找不到 wechat2md.py")
        return False

    cmd = [sys.executable, str(wechat2md), url, "-o", output_dir]
    if save_images:
        cmd.append("--save-images")

    try:
        result = subprocess.run(
            cmd, capture_output=True, text=True, timeout=60, encoding="utf-8"
        )
        if result.returncode == 0:
            return True
        else:
            print(f"  失败: {result.stderr}")
            return False
    except Exception as e:
        print(f"  错误: {e}")
        return False


def main():
    print("=" * 80)
    print("微信专辑下载工具")
    print("=" * 80)
    print(f"专辑URL: {ALBUM_URL}")
    print(f"输出目录: {OUTPUT_DIR.resolve()}")
    print("=" * 80)
    print()

    # 创建输出目录
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # 提取专辑信息
    album_info = extract_album_info(ALBUM_URL)
    print(f"专辑ID: {album_info['album_id']}")
    print()

    # 获取文章列表
    articles = fetch_album_articles(album_info["biz"], album_info["album_id"])

    if not articles:
        print("错误: 未能获取到文章列表")
        return

    print(f"\n找到 {len(articles)} 篇文章\n")

    # 保存文章列表
    list_file = OUTPUT_DIR / "文章列表.txt"
    with open(list_file, "w", encoding="utf-8") as f:
        f.write(f"# 文章列表 (共{len(articles)}篇)\n\n")
        for i, article in enumerate(articles, 1):
            f.write(f"{i}. {article['title']}\n")
            f.write(f"   {article['url']}\n\n")
    print(f"文章列表已保存: {list_file}\n")

    # 批量下载
    print("开始批量下载文章...\n")

    success_count = 0
    failed = []

    for i, article in enumerate(articles, 1):
        title = article["title"]
        url = article["url"]

        print(f"[{i}/{len(articles)}] {title}")

        if download_article(url, str(OUTPUT_DIR), save_images=True):
            success_count += 1
        else:
            failed.append({"title": title, "url": url})

        # 下载间隔
        if i < len(articles):
            import time

            time.sleep(1)

    # 输出结果
    print(f"\n{'=' * 80}")
    print(f"下载完成！")
    print(f"成功: {success_count}/{len(articles)}")
    print(f"失败: {len(failed)}")
    print(f"输出目录: {OUTPUT_DIR.resolve()}")
    print(f"{'=' * 80}")

    if failed:
        failed_file = OUTPUT_DIR / "下载失败.txt"
        with open(failed_file, "w", encoding="utf-8") as f:
            f.write("# 下载失败的文章\n\n")
            for a in failed:
                f.write(f"{a['title']}\n{a['url']}\n\n")
        print(f"\n失败列表已保存: {failed_file}")


if __name__ == "__main__":
    main()
