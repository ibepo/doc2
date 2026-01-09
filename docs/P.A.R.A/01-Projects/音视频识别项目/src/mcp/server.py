"""
MCP 服务器 - 播客字幕生成器

可被 LLM 调用的 MCP 服务器
"""

import asyncio
import json
import sys
from pathlib import Path
from typing import Optional

# 添加父目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent))

from core.asr_engine import ASREngine
from core.url_parser import URLParser


class PodcastSubtitleMCP:
    """播客字幕 MCP 服务器"""

    def __init__(self):
        self.asr_engine = None
        self.output_dir = Path("./outputs")
        self.output_dir.mkdir(parents=True, exist_ok=True)

    async def start(self):
        """启动 MCP 服务器"""
        print("🎙️ 播客字幕生成器 MCP 服务器启动中...", file=sys.stderr)
        print("支持的工具:", file=sys.stderr)
        print("  - generate_subtitle: 生成字幕", file=sys.stderr)
        print("  - parse_podcast: 解析播客信息", file=sys.stderr)
        print("", file=sys.stderr)

        # MCP 服务器主循环
        while True:
            try:
                # 读取 stdin
                line = await asyncio.get_event_loop().run_in_executor(
                    None, sys.stdin.readline
                )

                if not line:
                    break

                # 解析 JSON-RPC 请求
                try:
                    request = json.loads(line.strip())
                    response = await self.handle_request(request)
                    if response:
                        print(json.dumps(response), flush=True)
                except json.JSONDecodeError:
                    # 可能是续行的数据
                    continue

            except Exception as e:
                error_response = {
                    "jsonrpc": "2.0",
                    "id": None,
                    "error": {
                        "code": -32603,
                        "message": str(e)
                    }
                }
                print(json.dumps(error_response), flush=True)

    async def handle_request(self, request: dict) -> Optional[dict]:
        """处理 MCP 请求"""
        method = request.get("method")

        if method == "initialize":
            return await self.initialize(request)
        elif method == "tools/list":
            return await self.list_tools(request)
        elif method == "tools/call":
            return await self.call_tool(request)
        elif method == "ping":
            return {"jsonrpc": "2.0", "id": request.get("id"), "result": "pong"}
        else:
            return {
                "jsonrpc": "2.0",
                "id": request.get("id"),
                "error": {
                    "code": -32601,
                    "message": "Method not found"
                }
            }

    async def initialize(self, request: dict) -> dict:
        """初始化"""
        return {
            "jsonrpc": "2.0",
            "id": request.get("id"),
            "result": {
                "protocolVersion": "2024-11-05",
                "serverInfo": {
                    "name": "podcast-subtitle-generator",
                    "version": "1.0.0"
                },
                "capabilities": {
                    "tools": {}
                }
            }
        }

    async def list_tools(self, request: dict) -> dict:
        """列出可用工具"""
        return {
            "jsonrpc": "2.0",
            "id": request.get("id"),
            "result": {
                "tools": [
                    {
                        "name": "generate_subtitle",
                        "description": "从播客或视频 URL 自动生成字幕。支持小宇宙、喜马拉雅、B站、YouTube 等平台。",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "url": {
                                    "type": "string",
                                    "description": "播客或视频的 URL"
                                },
                                "output_formats": {
                                    "type": "array",
                                    "description": "输出格式列表，可选: srt, txt, md",
                                    "items": {"type": "string"},
                                    "default": ["srt", "txt"]
                                },
                                "language": {
                                    "type": "string",
                                    "description": "识别语言: auto, zh, en, yue, ja, ko",
                                    "default": "auto"
                                },
                                "model": {
                                    "type": "string",
                                    "description": "ASR 模型: SenseVoiceSmall, Fun-ASR-Nano, Paraformer",
                                    "default": "SenseVoiceSmall"
                                }
                            },
                            "required": ["url"]
                        }
                    },
                    {
                        "name": "parse_podcast",
                        "description": "解析播客页面，提取元数据和音视频链接信息（不下载）",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "url": {
                                    "type": "string",
                                    "description": "播客页面 URL"
                                }
                            },
                            "required": ["url"]
                        }
                    }
                ]
            }
        }

    async def call_tool(self, request: dict) -> dict:
        """调用工具"""
        params = request.get("params", {})
        tool_name = params.get("name", "")
        arguments = params.get("arguments", {})

        try:
            if tool_name == "generate_subtitle":
                result = await self.generate_subtitle(arguments)
            elif tool_name == "parse_podcast":
                result = await self.parse_podcast(arguments)
            else:
                raise ValueError(f"Unknown tool: {tool_name}")

            return {
                "jsonrpc": "2.0",
                "id": request.get("id"),
                "result": {
                    "content": [
                        {
                            "type": "text",
                            "text": result
                        }
                    ]
                }
            }

        except Exception as e:
            return {
                "jsonrpc": "2.0",
                "id": request.get("id"),
                "error": {
                    "code": -32000,
                    "message": str(e)
                }
            }

    async def generate_subtitle(self, arguments: dict) -> str:
        """生成字幕"""
        url = arguments.get("url")
        output_formats = arguments.get("output_formats", ["srt", "txt"])
        language = arguments.get("language", "auto")
        model = arguments.get("model", "SenseVoiceSmall")

        if not url:
            raise ValueError("URL is required")

        # 初始化模型（如果还没初始化）
        if not self.asr_engine:
            self.asr_engine = ASREngine(
                model_name=model,
                device="cpu"
            )
            self.asr_engine.language = language

        # 处理 URL
        result = self.asr_engine.process_url(
            url,
            output_dir=str(self.output_dir),
            output_formats=output_formats
        )

        # 构建返回信息
        segments = result.get('segments', [])
        total_duration = segments[-1]['end'] if segments else 0
        word_count = sum(len(seg['text']) for seg in segments)

        response = f"""## 字幕生成完成！

**原始 URL**: {url}
**平台**: {result.get('metadata', {}).get('platform', '未知')}
**标题**: {result.get('metadata', {}).get('title', '未知')}

**统计信息**:
- 总时长: {self._format_duration(total_duration)}
- 文本片段数: {len(segments)}
- 总字数: {word_count}

**生成的文件**:
"""

        files = result.get('files', {})
        for fmt, file_path in files.items():
            response += f"- **{fmt.upper()}**: {file_path}\n"

        response += f"\n**保存位置**: {self.output_dir}\n"

        return response

    async def parse_podcast(self, arguments: dict) -> str:
        """解析播客信息"""
        url = arguments.get("url")

        if not url:
            raise ValueError("URL is required")

        parser = URLParser()
        result = parser.parse(url)

        response = f"""## 播客信息

**URL**: {url}
**平台**: {result.get('platform', '未知')}
**内容类型**: {result.get('type', '未知')}
**标题**: {result.get('title', '未知')}
**作者**: {result.get('author', '未知')}

**链接**:
"""

        if result.get('audio_url'):
            response += f"- 音频: {result['audio_url']}\n"
        if result.get('video_url'):
            response += f"- 视频: {result['video_url']}\n"

        metadata = result.get('metadata', {})
        if metadata:
            response += "\n**其他信息**:\n"
            for key, value in metadata.items():
                if key != 'error':
                    response += f"- {key}: {value}\n"

        return response

    def _format_duration(self, seconds: float) -> str:
        """格式化时长"""
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = int(seconds % 60)

        if hours > 0:
            return f"{hours}小时{minutes}分{secs}秒"
        elif minutes > 0:
            return f"{minutes}分{secs}秒"
        else:
            return f"{secs}秒"


async def main():
    """主函数"""
    server = PodcastSubtitleMCP()
    await server.start()


if __name__ == "__main__":
    asyncio.run(main())
