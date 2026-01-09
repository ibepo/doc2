#!/usr/bin/env python3
"""
播客字幕自动生成器 - MCP 服务器启动器

使用方法：
    python mcp_server.py
    python mcp_server.py --host 0.0.0.0 --port 3000
"""

import sys
import asyncio
import argparse
from pathlib import Path

# 添加 src 目录到路径
sys.path.insert(0, str(Path(__file__).parent / "src"))

from mcp.server import PodcastSubtitleMCP


def main():
    parser = argparse.ArgumentParser(
        description="播客字幕自动生成器 - MCP 服务器"
    )

    parser.add_argument(
        "--host",
        type=str,
        default="localhost",
        help="服务器地址（默认：localhost）"
    )

    parser.add_argument(
        "--port",
        type=int,
        default=3000,
        help="服务器端口（默认：3000）"
    )

    args = parser.parse_args()

    print("""
╔══════════════════════════════════════════════════════════╗
║                                                        ║
║        🎙️ 播客字幕生成器 MCP 服务器                        ║
║                                                        ║
║  可被 LLM 调用的 MCP 服务器                              ║
║                                                        ║
║  工具：                                                 ║
║    - generate_subtitle: 生成字幕                        ║
║    - parse_podcast: 解析播客信息                         ║
║                                                        ║
╚══════════════════════════════════════════════════════════╝
    """)

    print(f"启动 MCP 服务器...")
    print(f"监听地址: {args.host}:{args.port}")
    print(f"\n等待连接...\n")

    server = PodcastSubtitleMCP()
    asyncio.run(server.start())


if __name__ == "__main__":
    main()
