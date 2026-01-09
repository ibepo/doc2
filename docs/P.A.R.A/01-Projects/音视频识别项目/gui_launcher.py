#!/usr/bin/env python3
"""
播客字幕自动生成器 - GUI 启动器

使用方法：
    python gui_launcher.py
    python gui_launcher.py --share  # 创建公网链接
    python gui_launcher.py --port 8080
"""

import sys
import argparse
from pathlib import Path

# 添加 src 目录到路径
sys.path.insert(0, str(Path(__file__).parent / "src"))

from gui.gradio_app import launch_gui


def main():
    parser = argparse.ArgumentParser(
        description="播客字幕自动生成器 - GUI 版"
    )

    parser.add_argument(
        "--share",
        action="store_true",
        help="创建公网访问链接"
    )

    parser.add_argument(
        "--port",
        type=int,
        default=7860,
        help="服务器端口（默认：7860）"
    )

    parser.add_argument(
        "--host",
        type=str,
        default="127.0.0.1",
        help="服务器地址（默认：127.0.0.1）"
    )

    args = parser.parse_args()

    print("""
╔══════════════════════════════════════════════════════════╗
║                                                        ║
║        🎙️ 播客字幕自动生成器 GUI                         ║
║                                                        ║
║  支持从播客/视频 URL 自动生成字幕                         ║
║  支持平台：小宇宙、喜马拉雅、B站、YouTube 等            ║
║                                                        ║
╚══════════════════════════════════════════════════════════╝
    """)

    print(f"启动中...")
    print(f"访问地址: http://{args.host}:{args.port}")

    if args.share:
        print(f"公网链接: 将在启动后显示")

    print()

    launch_gui(
        share=args.share,
        server_port=args.port,
        server_name=args.host
    )


if __name__ == "__main__":
    main()
