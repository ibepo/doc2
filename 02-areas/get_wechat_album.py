#!/usr/bin/env python3
"""
获取微信公众号专辑中的所有文章链接
尝试多种API方式
"""
import requests
import json

def get_album_articles():
    """通过API获取专辑文章列表"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/120.0.0.0 Safari/537.36'
    }

    # 微信专辑文章列表API
    api_url = "https://mp.weixin.qq.com/mp/appmsg_album"
    params = {
        '__biz': 'MjM5MjAzODU2MA==',
        'album_id': '3099088215745052674',
        'action': 'getalbum',
        'f': 'json',
        'ajax': '1'
    }

    print(f"正在调用API: {api_url}")
    print(f"参数: {params}")

    response = requests.get(api_url, params=params, headers=headers, timeout=30)
    print(f"状态码: {response.status_code}")

    try:
        data = response.json()
        print(f"返回数据: {json.dumps(data, ensure_ascii=False)[:1000]}")
        return data
    except:
        print(f"响应内容: {response.text[:1000]}")
        return None

def get_album_appmsg():
    """尝试使用appmsg接口"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/120.0.0.0 Safari/537.36'
    }

    api_url = "https://mp.weixin.qq.com/mp/appmsg"
    params = {
        '__biz': 'MjM5MjAzODU2MA==',
        'mid': '1',
        'sn': '1',
        'scene': '27',
        'f': 'json',
        'ajax': '1'
    }

    print(f"\n尝试appmsg接口...")
    response = requests.get(api_url, params=params, headers=headers, timeout=30)
    print(f"状态码: {response.status_code}")

    try:
        data = response.json()
        print(f"返回数据: {json.dumps(data, ensure_ascii=False)[:500]}")
        return data
    except:
        print(f"响应内容: {response.text[:500]}")
        return None

def main():
    print("=== 方法1: appmsg_album ===")
    get_album_articles()

    print("\n=== 方法2: appmsg ===")
    get_album_appmsg()

if __name__ == '__main__':
    main()
