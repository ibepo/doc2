"""
内容下载器 - 下载音视频并转换为 ASR 需要的格式

支持：
- 所有 yt-dlp 支持的平台（1000+ 网站）
- 自动转换为 WAV 格式（16kHz, 单声道）
- 进度回调
"""

import os
import subprocess
import tempfile
from typing import Optional, Callable
from pathlib import Path
import shutil


class Downloader:
    """内容下载器"""

    def __init__(
        self,
        output_dir: str = "./downloads",
        audio_format: str = "wav",
        sample_rate: int = 16000,
        channels: int = 1
    ):
        """
        初始化下载器

        Args:
            output_dir: 输出目录
            audio_format: 音频格式（wav/mp3/m4a）
            sample_rate: 采样率（16000 for FunASR）
            channels: 声道数（1 for mono）
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

        self.audio_format = audio_format
        self.sample_rate = sample_rate
        self.channels = channels

        # 检查依赖
        self._check_dependencies()

    def _check_dependencies(self):
        """检查必要的依赖"""
        # 检查 ffmpeg
        try:
            subprocess.run(
                ['ffmpeg', '-version'],
                capture_output=True,
                check=True
            )
        except (subprocess.CalledProcessError, FileNotFoundError):
            raise RuntimeError(
                "ffmpeg 未安装。请安装 ffmpeg:\n"
                "  macOS: brew install ffmpeg\n"
                "  Ubuntu: sudo apt install ffmpeg\n"
                "  Windows: 从 https://ffmpeg.org 下载"
            )

        # 检查 yt-dlp
        try:
            import yt_dlp
            self.yt_dlp = yt_dlp
        except ImportError:
            raise ImportError(
                "yt-dlp 未安装。请运行: pip install yt-dlp"
            )

    def download(
        self,
        url: str,
        output_filename: Optional[str] = None,
        progress_callback: Optional[Callable[[float, str], None]] = None
    ) -> str:
        """
        下载音视频并转换为指定格式

        Args:
            url: 音视频 URL 或网页 URL
            output_filename: 输出文件名（不含扩展名）
            progress_callback: 进度回调函数 (progress_percent, status_text)

        Returns:
            下载的音频文件路径
        """
        if output_filename is None:
            output_filename = self._generate_filename(url)

        output_path = self.output_dir / f"{output_filename}.{self.audio_format}"

        # yt-dlp 配置
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': self.audio_format,
                'preferredquality': '192',
            }],
            'outtmpl': str(self.output_dir / f"{output_filename}.%(ext)s"),
            'quiet': False if progress_callback else True,
            'no_warnings': True if progress_callback else False,
            'progress_hooks': [lambda d: self._progress_hook(d, progress_callback)] if progress_callback else [],
        }

        # 添加音频转换参数
        if self.audio_format == 'wav':
            ydl_opts['postprocessors'][0]['preferredcodec'] = 'wav'
            ydl_opts['postprocessor_args'] = {
                'audio': ['-ar', str(self.sample_rate), '-ac', str(self.channels)]
            }

        try:
            with self.yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

            # 查找生成的文件
            downloaded_file = self._find_downloaded_file(output_filename)

            if downloaded_file and downloaded_file.exists():
                return str(downloaded_file)
            else:
                # 如果找不到，可能文件名不同，尝试查找
                return str(self._find_any_recent_file())

        except Exception as e:
            raise RuntimeError(f"下载失败: {str(e)}")

    def download_to_wav(
        self,
        url: str,
        output_filename: Optional[str] = None,
        progress_callback: Optional[Callable[[float, str], None]] = None
    ) -> str:
        """
        下载并转换为 WAV 格式（16kHz, 单声道）

        这是最适合 FunASR 的格式。

        Args:
            url: 音视频 URL 或网页 URL
            output_filename: 输出文件名（不含扩展名）
            progress_callback: 进度回调函数

        Returns:
            WAV 文件路径
        """
        # 临时设置 WAV 格式参数
        original_format = self.audio_format
        original_sr = self.sample_rate
        original_channels = self.channels

        self.audio_format = 'wav'
        self.sample_rate = 16000
        self.channels = 1

        try:
            result = self.download(url, output_filename, progress_callback)
            return result
        finally:
            # 恢复原始设置
            self.audio_format = original_format
            self.sample_rate = original_sr
            self.channels = original_channels

    def extract_audio(
        self,
        video_path: str,
        output_path: Optional[str] = None
    ) -> str:
        """
        从视频文件中提取音频

        Args:
            video_path: 视频文件路径
            output_path: 输出音频路径（可选）

        Returns:
            提取的音频文件路径
        """
        if output_path is None:
            video_path = Path(video_path)
            output_path = str(video_path.parent / f"{video_path.stem}.wav")

        # 使用 ffmpeg 提取音频
        cmd = [
            'ffmpeg',
            '-i', video_path,
            '-vn',  # 不包含视频
            '-acodec', 'pcm_s16le',  # PCM 16位
            '-ar', str(self.sample_rate),  # 采样率
            '-ac', str(self.channels),  # 声道数
            '-y',  # 覆盖已存在的文件
            output_path
        ]

        try:
            subprocess.run(
                cmd,
                capture_output=True,
                check=True
            )
            return output_path
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"音频提取失败: {e.stderr.decode()}")

    def _generate_filename(self, url: str) -> str:
        """根据 URL 生成文件名"""
        from urllib.parse import urlparse
        import hashlib

        parsed = urlparse(url)
        # 使用 URL 的哈希值作为文件名
        url_hash = hashlib.md5(url.encode()).hexdigest()[:8]
        return f"audio_{url_hash}"

    def _find_downloaded_file(self, filename: str) -> Optional[Path]:
        """查找下载的文件"""
        # 查找可能的扩展名
        extensions = [self.audio_format, 'm4a', 'mp3', 'webm', 'mp4']

        for ext in extensions:
            file_path = self.output_dir / f"{filename}.{ext}"
            if file_path.exists():
                return file_path

        return None

    def _find_any_recent_file(self) -> Optional[Path]:
        """查找最近创建的文件"""
        files = list(self.output_dir.glob('*'))
        if files:
            return max(files, key=lambda p: p.stat().st_mtime)
        return None

    def _progress_hook(self, d: dict, callback: Callable[[float, str], None]):
        """yt-dlp 进度钩子"""
        if d['status'] == 'downloading':
            if 'total_bytes' in d and 'downloaded_bytes' in d:
                progress = d['downloaded_bytes'] / d['total_bytes'] * 100
                speed = d.get('speed', 0)
                speed_mb = speed / (1024 * 1024) if speed else 0
                callback(progress, f"下载中... {progress:.1f}% ({speed_mb:.1f} MB/s)")
            elif 'total_bytes_estimate' in d and 'downloaded_bytes' in d:
                progress = d['downloaded_bytes'] / d['total_bytes_estimate'] * 100
                callback(progress, f"下载中... {progress:.1f}%")

        elif d['status'] == 'processing':
            callback(100, "处理中...")

        elif d['status'] == 'finished':
            callback(100, "完成！")

    def get_info(self, url: str) -> dict:
        """
        获取音视频信息而不下载

        Args:
            url: 音视频 URL

        Returns:
            信息字典，包含标题、时长等
        """
        ydl_opts = {
            'quiet': True,
            'no_warnings': True,
        }

        try:
            with self.yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)

                return {
                    'title': info.get('title'),
                    'duration': info.get('duration'),
                    'uploader': info.get('uploader'),
                    'thumbnail': info.get('thumbnail'),
                    'description': info.get('description'),
                }
        except Exception as e:
            return {'error': str(e)}


# 使用示例
if __name__ == '__main__':
    def progress_callback(progress, status):
        print(f"[{progress:.1f}%] {status}")

    downloader = Downloader(output_dir="./downloads")

    # 下载示例
    url = "https://www.xiaoyuzhou.com/episode/123456"
    audio_file = downloader.download_to_wav(url, progress_callback=progress_callback)
    print(f"下载完成: {audio_file}")
