"""
URL 解析器 - 从播客/视频页面提取音视频链接

支持的平台：
- 播客：小宇宙、喜马拉雅、荔枝FM、Apple Podcasts
- 视频：B站、YouTube、优酷、腾讯视频
- 通用：直接音视频链接
"""

import re
import json
import requests
from typing import Dict, List, Optional
from urllib.parse import urlparse, parse_qs
from bs4 import BeautifulSoup
import time


class URLParser:
    """URL 解析器"""

    def __init__(self, timeout: int = 10):
        """
        初始化解析器

        Args:
            timeout: 请求超时时间（秒）
        """
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        })

        # 平台识别规则
        self.platform_patterns = {
            'xiaoyuzhou': r'xiaoyuzhou\.com',
            'ximalaya': r'ximalaya\.com',
            'lizhi': r'lizhi\.fm',
            'podcasts': r'podcasts\.apple\.com',
            'bilibili': r'bilibili\.com',
            'youtube': r'youtube\.com|youtu\.be',
            'youku': r'youku\.com',
            'qq': r'v\.qq\.com',
            'direct': r'^https?://.*\.(mp3|wav|m4a|mp4|m4v|avi|mkv|flv|webm)$'
        }

    def parse(self, url: str) -> Dict:
        """
        解析 URL，提取音视频信息和链接

        Args:
            url: 播客或视频 URL

        Returns:
            包含以下字段的字典：
            {
                'platform': 平台名称,
                'type': 'audio' 或 'video',
                'title': 标题,
                'author': 作者/播主,
                'audio_url': 音频 URL（如果有）,
                'video_url': 视频 URL（如果有）,
                'duration': 时长（秒）,
                'metadata': 其他元数据
            }
        """
        url = url.strip()
        platform = self._detect_platform(url)

        result = {
            'platform': platform,
            'type': None,
            'title': None,
            'author': None,
            'audio_url': None,
            'video_url': None,
            'duration': None,
            'metadata': {},
            'original_url': url
        }

        if platform == 'xiaoyuzhou':
            return self._parse_xiaoyuzhou(url, result)
        elif platform == 'ximalaya':
            return self._parse_ximalaya(url, result)
        elif platform == 'lizhi':
            return self._parse_lizhi(url, result)
        elif platform == 'bilibili':
            return self._parse_bilibili(url, result)
        elif platform == 'youtube':
            return self._parse_youtube(url, result)
        elif platform == 'direct':
            return self._parse_direct(url, result)
        else:
            return self._parse_generic(url, result)

    def _detect_platform(self, url: str) -> str:
        """检测平台"""
        for platform, pattern in self.platform_patterns.items():
            if re.search(pattern, url, re.IGNORECASE):
                return platform
        return 'generic'

    def _parse_xiaoyuzhou(self, url: str, result: Dict) -> Dict:
        """解析小宇宙播客"""
        try:
            response = self.session.get(url, timeout=self.timeout)
            soup = BeautifulSoup(response.text, 'html.parser')

            # 提取标题
            title_elem = soup.find('meta', property='og:title')
            result['title'] = title_elem.get('content', '').strip() if title_elem else None

            # 提取作者
            author_elem = soup.find('meta', property='og:audio:artist')
            result['author'] = author_elem.get('content', '').strip() if author_elem else None

            # 提取音频 URL
            audio_elem = soup.find('meta', property='og:audio')
            if audio_elem:
                result['audio_url'] = audio_elem.get('content')
                result['type'] = 'audio'

            # 提取其他元数据
            desc_elem = soup.find('meta', property='og:description')
            if desc_elem:
                result['metadata']['description'] = desc_elem.get('content')

        except Exception as e:
            result['metadata']['error'] = str(e)

        return result

    def _parse_ximalaya(self, url: str, result: Dict) -> Dict:
        """解析喜马拉雅"""
        try:
            response = self.session.get(url, timeout=self.timeout)
            soup = BeautifulSoup(response.text, 'html.parser')

            # 喜马拉雅需要从页面 JSON 中提取音频链接
            script_tags = soup.find_all('script', type='application/json')
            for script in script_tags:
                try:
                    data = json.loads(script.string)
                    if 'audioUrl' in str(data):
                        # 这里需要根据实际的 JSON 结构解析
                        result['audio_url'] = data.get('audioUrl')
                        result['type'] = 'audio'
                        break
                except:
                    continue

            # 提取标题
            title_elem = soup.find('h1', class_='title')
            result['title'] = title_elem.get_text(strip=True) if title_elem else None

        except Exception as e:
            result['metadata']['error'] = str(e)

        return result

    def _parse_lizhi(self, url: str, result: Dict) -> Dict:
        """解析荔枝FM"""
        try:
            response = self.session.get(url, timeout=self.timeout)
            soup = BeautifulSoup(response.text, 'html.parser')

            # 提取音频 URL
            audio_elem = soup.find('audio')
            if audio_elem and audio_elem.get('src'):
                result['audio_url'] = audio_elem.get('src')
                result['type'] = 'audio'

            # 提取标题
            title_elem = soup.find('meta', property='og:title')
            result['title'] = title_elem.get('content', '').strip() if title_elem else None

        except Exception as e:
            result['metadata']['error'] = str(e)

        return result

    def _parse_bilibili(self, url: str, result: Dict) -> Dict:
        """解析B站视频"""
        try:
            # 提取视频 ID
            bv_match = re.search(r'BV[\w]+', url)
            if bv_match:
                bvid = bv_match.group(0)
                result['metadata']['bvid'] = bvid
                result['type'] = 'video'
                result['title'] = f'B站视频 {bvid}'

                # 注意：B站实际下载需要使用 yt-dlp 或专门的库
                # 这里只是标记，实际下载在 downloader 中完成
        except Exception as e:
            result['metadata']['error'] = str(e)

        return result

    def _parse_youtube(self, url: str, result: Dict) -> Dict:
        """解析YouTube"""
        try:
            # 提取视频 ID
            video_id = None
            patterns = [
                r'(?:youtube\.com\/watch\?v=|youtu\.be\/)([a-zA-Z0-9_-]{11})',
                r'youtube\.com\/embed\/([a-zA-Z0-9_-]{11})'
            ]

            for pattern in patterns:
                match = re.search(pattern, url)
                if match:
                    video_id = match.group(1)
                    break

            if video_id:
                result['metadata']['video_id'] = video_id
                result['type'] = 'video'
                result['title'] = f'YouTube 视频 {video_id}'

        except Exception as e:
            result['metadata']['error'] = str(e)

        return result

    def _parse_direct(self, url: str, result: Dict) -> Dict:
        """解析直接音视频链接"""
        parsed = urlparse(url)
        ext = parsed.path.split('.')[-1].lower()

        audio_exts = ['mp3', 'wav', 'm4a', 'aac', 'flac', 'ogg']
        video_exts = ['mp4', 'm4v', 'avi', 'mkv', 'flv', 'webm', 'mov']

        if ext in audio_exts:
            result['type'] = 'audio'
            result['audio_url'] = url
        elif ext in video_exts:
            result['type'] = 'video'
            result['video_url'] = url

        # 从 URL 中提取文件名作为标题
        filename = parsed.path.split('/')[-1]
        result['title'] = filename

        return result

    def _parse_generic(self, url: str, result: Dict) -> Dict:
        """通用解析（尝试提取页面中的音视频）"""
        try:
            response = self.session.get(url, timeout=self.timeout)
            soup = BeautifulSoup(response.text, 'html.parser')

            # 查找 audio 标签
            audio_elem = soup.find('audio')
            if audio_elem and audio_elem.get('src'):
                result['audio_url'] = audio_elem.get('src')
                result['type'] = 'audio'

            # 查找 video 标签
            video_elem = soup.find('video')
            if video_elem and video_elem.get('src'):
                result['video_url'] = video_elem.get('src')
                if not result['type']:
                    result['type'] = 'video'

            # 提取标题
            title_elem = soup.find('title')
            if title_elem:
                result['title'] = title_elem.get_text(strip=True)

        except Exception as e:
            result['metadata']['error'] = str(e)

        return result

    def extract_audio_url(self, url: str) -> Optional[str]:
        """
        直接提取音频 URL

        Args:
            url: 页面 URL 或直接音频链接

        Returns:
            音频 URL，如果未找到则返回 None
        """
        result = self.parse(url)
        return result.get('audio_url')

    def get_metadata(self, url: str) -> Dict:
        """
        获取页面元数据

        Args:
            url: 页面 URL

        Returns:
            元数据字典
        """
        result = self.parse(url)
        return {
            'title': result.get('title'),
            'author': result.get('author'),
            'platform': result.get('platform'),
            'type': result.get('type'),
            'duration': result.get('duration'),
            **result.get('metadata', {})
        }


# 使用示例
if __name__ == '__main__':
    parser = URLParser()

    # 测试小宇宙播客
    test_url = 'https://www.xiaoyuzhou.com/episode/123456'
    result = parser.parse(test_url)
    print(f"平台: {result['platform']}")
    print(f"标题: {result['title']}")
    print(f"音频链接: {result['audio_url']}")
