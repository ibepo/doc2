"""
播客字幕自动生成器 - GUI 界面

使用 Gradio 构建的 Web 界面
"""

import gradio as gr
from pathlib import Path
import sys
import os

# 添加父目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent))

from core.asr_engine import ASREngine
from core.url_parser import URLParser


class SubtitleGeneratorGUI:
    """字幕生成器 GUI"""

    def __init__(self):
        self.asr_engine = None
        self.output_dir = Path("./outputs")
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def load_model(self, model_name, device):
        """加载模型"""
        try:
            if model_name == "SenseVoiceSmall (推荐)":
                model = "SenseVoiceSmall"
            elif model_name == "Fun-ASR-Nano (31种语言)":
                model = "Fun-ASR-Nano-2512"
            elif model_name == "Paraformer (中文)":
                model = "paraformer-zh"
            else:
                model = "SenseVoiceSmall"

            self.asr_engine = ASREngine(model_name=model, device=device)
            return "✅ 模型加载成功！", gr.update(visible=True), gr.update(visible=True)
        except Exception as e:
            return f"❌ 模型加载失败: {str(e)}", gr.update(visible=False), gr.update(visible=False)

    def process_url(
        self,
        url,
        output_formats,
        language,
        model_choice,
        device,
        progress=gr.Progress()
    ):
        """处理 URL 并生成字幕"""
        try:
            # 验证输入
            if not url or not url.strip():
                return "❌ 请输入有效的 URL", None, None, None

            url = url.strip()

            # 更新模型语言设置
            if self.asr_engine:
                self.asr_engine.language = language

            # 解析 URL
            progress(0.1, desc="解析 URL...")
            parser = URLParser()
            parse_result = parser.parse(url)

            # 显示解析结果
            info_text = f"""
**平台**: {parse_result.get('platform', '未知')}
**类型**: {parse_result.get('type', '未知')}
**标题**: {parse_result.get('title', '未知')}
"""
            if parse_result.get('author'):
                info_text += f"**作者**: {parse_result['author']}\n"

            progress(0.2, desc="加载模型...")
            # 确保模型已加载
            if not self.asr_engine:
                self.asr_engine = ASREngine(model_name="SenseVoiceSmall", device=device)

            progress(0.3, desc="开始处理...")

            # 处理 URL
            result = self.asr_engine.process_url(
                url,
                output_dir=str(self.output_dir),
                output_formats=output_formats,
                progress_callback=lambda p, s: progress(
                    0.3 + p * 0.6,  # 30-90%
                    desc=s
                )
            )

            progress(0.95, desc="生成完成！")

            # 统计信息
            segments = result.get('segments', [])
            total_duration = segments[-1]['end'] if segments else 0
            word_count = sum(len(seg['text']) for seg in segments)
            segment_count = len(segments)

            stats = f"""
## 处理完成！

**统计信息**:
- 总时长: {self._format_duration(total_duration)}
- 片段数: {segment_count}
- 字数: {word_count}
- 识别语言: {language}
"""

            # 生成下载链接
            files = result.get('files', {})
            download_links = []
            download_info = []

            for fmt in output_formats:
                if fmt in files:
                    file_path = Path(files[fmt])
                    if file_path.exists():
                        download_links.append(file_path)
                        download_info.append(f"✅ **{fmt.upper()}**: {file_path.name}")

            download_text = "\n".join(download_info) if download_info else "未生成文件"

            progress(1.0, desc="全部完成！")

            return stats + download_text, *download_links[:3]

        except Exception as e:
            error_msg = f"❌ 处理失败: {str(e)}"
            progress(1.0, desc="处理失败")
            return error_msg, None, None, None

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

    def create_interface(self):
        """创建 Gradio 界面"""
        with gr.Blocks(
            title="播客字幕自动生成器",
            theme=gr.themes.Soft(),
            css="""
                .container {max-width: 800px; margin: auto;}
                .header {text-align: center; margin-bottom: 20px;}
                .info-box {background: #f0f0f0; padding: 10px; border-radius: 5px; margin: 10px 0;}
            """
        ) as interface:
            # 标题
            gr.Markdown(
                """
                # 🎙️ 播客字幕自动生成器

                支持从播客/视频 URL 自动提取音视频并生成字幕

                **支持平台**: 小宇宙、喜马拉雅、B站、YouTube 等 1000+ 网站
                **AI 模型**: FunASR (SenseVoice)
                **输出格式**: SRT 字幕、TXT 文本、Markdown 文档
                """
            )

            with gr.Row():
                with gr.Column(scale=3):
                    # 输入区域
                    url_input = gr.Textbox(
                        label="📺 播客/视频 URL",
                        placeholder="https://www.xiaoyuzhou.com/episode/...",
                        lines=2
                    )

                    # 设置区域
                    with gr.Accordion("⚙️ 高级设置", open=False):
                        model_choice = gr.Radio(
                            choices=[
                                "SenseVoiceSmall (推荐)",
                                "Fun-ASR-Nano (31种语言)",
                                "Paraformer (中文)"
                            ],
                            value="SenseVoiceSmall (推荐)",
                            label="🤖 ASR 模型"
                        )

                        device = gr.Radio(
                            choices=["cpu", "cuda", "cuda:0"],
                            value="cpu",
                            label="💻 设备"
                        )

                        language = gr.Dropdown(
                            choices=["auto", "zh", "en", "yue", "ja", "ko"],
                            value="auto",
                            label="🌍 识别语言"
                        )

                        output_formats = gr.CheckboxGroup(
                            choices=["srt", "txt", "md"],
                            value=["srt", "txt", "md"],
                            label="📄 输出格式"
                        )

                    # 按钮区域
                    with gr.Row():
                        load_btn = gr.Button("🔄 加载模型", size="sm")
                        submit_btn = gr.Button("▶️ 开始生成", variant="primary", size="lg")

                with gr.Column(scale=2):
                    # 输出区域
                    info_output = gr.Markdown(label="📊 处理信息")

                    with gr.Row():
                        srt_file = gr.File(label="📄 SRT 字幕", visible=False)
                        txt_file = gr.File(label="📄 TXT 文本", visible=False)
                        md_file = gr.File(label="📄 Markdown", visible=False)

            # 事件绑定
            load_btn.click(
                fn=lambda m, d: self.load_model(m, d),
                inputs=[model_choice, device],
                outputs=[info_output, srt_file, txt_file]
            )

            submit_btn.click(
                fn=self.process_url,
                inputs=[url_input, output_formats, language, model_choice, device],
                outputs=[info_output, srt_file, txt_file, md_file]
            )

            # 示例
            gr.Examples(
                examples=[
                    ["https://www.xiaoyuzhou.com/episode/123456"],
                    ["https://www.bilibili.com/video/BV1xx411c7mD"],
                ],
                inputs=url_input,
                label="💡 示例 URL"
            )

            # 使用说明
            gr.Markdown(
                """
                ---

                ### 📖 使用说明

                1. **输入 URL**: 粘贴播客或视频链接
                2. **选择模型**: SenseVoiceSmall 支持中英日韩等多语言
                3. **点击开始**: 等待处理完成（可能需要几分钟）
                4. **下载文件**: 点击下载按钮获取字幕文件

                ### ⚡ 性能提示

                - CPU 模式: 约 0.05-0.1x 实时速度
                - GPU 模式: 约 0.01x 实时速度（推荐）
                - 1小时音频约需 5-10 分钟（CPU）

                ### 🔧 环境要求

                - Python 3.8+
                - ffmpeg
                - 足够的磁盘空间（音频 + 模型）
                """
            )

        return interface


def launch_gui(
    share: bool = False,
    server_port: int = 7860,
    server_name: str = "0.0.0.0"
):
    """启动 GUI"""
    gui = SubtitleGeneratorGUI()
    interface = gui.create_interface()

    interface.launch(
        share=share,
        server_port=server_port,
        server_name=server_name,
        inbrowser=True
    )


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--share", action="store_true", help="创建公网链接")
    parser.add_argument("--port", type=int, default=7860, help="端口号")
    parser.add_argument("--host", type=str, default="127.0.0.1", help="主机地址")

    args = parser.parse_args()

    launch_gui(
        share=args.share,
        server_port=args.port,
        server_name=args.host
    )
