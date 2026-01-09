"""
ASR 字幕生成引擎 - 集成 FunASR/SenseVoice 生成字幕

功能：
- 支持多种模型（SenseVoice、Paraformer、Fun-ASR-Nano）
- 生成带时间轴的 SRT 字幕
- 支持多种输出格式（SRT、TXT、Markdown）
"""

import os
import time
from typing import List, Dict, Optional, Callable
from pathlib import Path
from datetime import timedelta


class ASREngine:
    """ASR 字幕生成引擎"""

    def __init__(
        self,
        model_name: str = "SenseVoiceSmall",
        device: str = "cpu",
        language: str = "auto"
    ):
        """
        初始化 ASR 引擎

        Args:
            model_name: 模型名称
                - SenseVoiceSmall: 多语言语音理解（推荐）
                - Fun-ASR-Nano-2512: 31种语言大模型
                - paraformer-zh: 中文识别
            device: 设备类型（cpu/cuda/cuda:0）
            language: 语言（auto/zh/en/yue/ja/ko）
        """
        self.model_name = model_name
        self.device = device
        self.language = language
        self.model = None
        self._load_model()

    def _load_model(self):
        """加载 ASR 模型"""
        try:
            from funasr import AutoModel
        except ImportError:
            raise ImportError(
                "FunASR 未安装。请运行: pip install funasr modelscope"
            )

        print(f"正在加载模型: {self.model_name}...")
        start_time = time.time()

        # 根据模型类型配置
        if "SenseVoice" in self.model_name:
            self.model = AutoModel(
                model=f"iic/{self.model_name}",
                vad_model="fsmn-vad",
                vad_kwargs={"max_single_segment_time": 30000},
                device=self.device,
            )
        elif "Nano" in self.model_name:
            self.model = AutoModel(
                model=f"FunAudioLLM/{self.model_name}",
                vad_model="fsmn-vad",
                device=self.device,
            )
        else:  # Paraformer
            self.model = AutoModel(
                model=f"damo/speech_paraformer-large_asr_nat-zh-cn-16k-common-vocab8404-pytorch",
                vad_model="fsmn-vad",
                punc_model="ct-punc",
                device=self.device,
            )

        load_time = time.time() - start_time
        print(f"模型加载完成！耗时: {load_time:.2f} 秒")

    def transcribe(
        self,
        audio_path: str,
        use_itn: bool = True,
        merge_vad: bool = True,
        batch_size_s: int = 60,
        progress_callback: Optional[Callable[[float, str], None]] = None
    ) -> List[Dict]:
        """
        转录音频，返回带时间轴的文本片段

        Args:
            audio_path: 音频文件路径
            use_itn: 是否使用逆文本标准化（数字、日期等转换）
            merge_vad: 是否合并 VAD 分割的短片段
            batch_size_s: 动态批处理的音频时长（秒）
            progress_callback: 进度回调函数

        Returns:
            文本片段列表，每个片段包含：
            {
                'start': 开始时间（秒）,
                'end': 结束时间（秒）,
                'text': 文本内容,
                'confidence': 置信度（如果有）
            }
        """
        if progress_callback:
            progress_callback(0, "开始转录...")

        try:
            # 根据模型类型调用不同的生成方法
            if "SenseVoice" in self.model_name:
                result = self.model.generate(
                    input=audio_path,
                    cache={},
                    language=self.language,
                    use_itn=use_itn,
                    batch_size_s=batch_size_s,
                    merge_vad=merge_vad,
                    merge_length_s=15,
                )
            else:
                result = self.model.generate(
                    input=audio_path,
                    batch_size_s=batch_size_s,
                )

            if progress_callback:
                progress_callback(100, "转录完成！")

            # 解析结果
            segments = self._parse_result(result)

            return segments

        except Exception as e:
            raise RuntimeError(f"转录失败: {str(e)}")

    def _parse_result(self, result: List) -> List[Dict]:
        """解析模型输出，提取时间轴和文本"""
        segments = []

        if not result or len(result) == 0:
            return segments

        result = result[0]  # FunASR 返回的是列表

        if "sentence_info" in result:
            # SenseVoice 格式
            for seg in result["sentence_info"]:
                segments.append({
                    'start': seg.get('start', 0) / 1000,  # 毫秒转秒
                    'end': seg.get('end', 0) / 1000,
                    'text': seg.get('text', ''),
                })
        elif "segments" in result:
            # Whisper 格式
            for seg in result["segments"]:
                segments.append({
                    'start': seg.get('start', 0),
                    'end': seg.get('end', 0),
                    'text': seg.get('text', ''),
                })
        else:
            # 尝试其他格式
            if isinstance(result, dict) and "text" in result:
                # 只有文本，没有时间轴
                segments.append({
                    'start': 0,
                    'end': 0,
                    'text': result["text"],
                })

        return segments

    def generate_srt(
        self,
        segments: List[Dict],
        output_path: Optional[str] = None
    ) -> str:
        """
        生成 SRT 格式字幕

        Args:
            segments: 文本片段列表
            output_path: 输出文件路径（可选）

        Returns:
            SRT 格式的字幕内容
        """
        srt_content = []

        for i, seg in enumerate(segments, 1):
            start_time = self._format_srt_time(seg['start'])
            end_time = self._format_srt_time(seg['end'])
            text = seg['text'].strip()

            srt_content.append(f"{i}")
            srt_content.append(f"{start_time} --> {end_time}")
            srt_content.append(text)
            srt_content.append("")  # 空行

        srt_text = "\n".join(srt_content)

        if output_path:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(srt_text)
            print(f"SRT 字幕已保存到: {output_path}")

        return srt_text

    def generate_txt(
        self,
        segments: List[Dict],
        output_path: Optional[str] = None
    ) -> str:
        """
        生成纯文本格式

        Args:
            segments: 文本片段列表
            output_path: 输出文件路径（可选）

        Returns:
            纯文本内容
        """
        txt_content = []

        for seg in segments:
            timestamp = f"[{self._format_readable_time(seg['start'])}]"
            txt_content.append(f"{timestamp} {seg['text'].strip()}")

        txt_text = "\n".join(txt_content)

        if output_path:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(txt_text)
            print(f"TXT 文本已保存到: {output_path}")

        return txt_text

    def generate_markdown(
        self,
        segments: List[Dict],
        metadata: Optional[Dict] = None,
        output_path: Optional[str] = None
    ) -> str:
        """
        生成 Markdown 格式文档

        Args:
            segments: 文本片段列表
            metadata: 元数据（标题、作者等）
            output_path: 输出文件路径（可选）

        Returns:
            Markdown 内容
        """
        md_content = []

        # 添加标题
        if metadata and 'title' in metadata:
            md_content.append(f"# {metadata['title']}\n")

        # 添加元数据
        if metadata:
            md_content.append("## 元数据\n")
            for key, value in metadata.items():
                if key != 'title':
                    md_content.append(f"- **{key}**: {value}")
            md_content.append("\n")

        # 添加内容
        md_content.append("## 转录内容\n")

        for seg in segments:
            timestamp = f"[{self._format_readable_time(seg['start'])}]"
            md_content.append(f"{timestamp} {seg['text'].strip()}")

        md_text = "\n".join(md_content)

        if output_path:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(md_text)
            print(f"Markdown 文档已保存到: {output_path}")

        return md_text

    def _format_srt_time(self, seconds: float) -> str:
        """格式化为 SRT 时间格式 (HH:MM:SS,mmm)"""
        td = timedelta(seconds=seconds)
        hours, remainder = divmod(td.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        milliseconds = td.microseconds // 1000
        return f"{hours:02}:{minutes:02}:{seconds:02},{milliseconds:03}"

    def _format_readable_time(self, seconds: float) -> str:
        """格式化为可读时间格式 (HH:MM:SS)"""
        td = timedelta(seconds=seconds)
        hours, remainder = divmod(td.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        if hours > 0:
            return f"{hours:02}:{minutes:02}:{seconds:02}"
        else:
            return f"{minutes:02}:{seconds:02}"

    def process_url(
        self,
        url: str,
        output_dir: str = "./outputs",
        output_formats: List[str] = ["srt", "txt", "md"],
        progress_callback: Optional[Callable[[float, str], None]] = None
    ) -> Dict:
        """
        完整处理流程：下载 + 转录 + 生成字幕

        Args:
            url: 音视频 URL
            output_dir: 输出目录
            output_formats: 输出格式列表（srt/txt/md）
            progress_callback: 进度回调

        Returns:
            结果字典，包含生成的文件路径
        """
        from .url_parser import URLParser
        from .downloader import Downloader

        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)

        result = {
            'url': url,
            'files': {},
            'segments': None,
            'metadata': {}
        }

        try:
            # 1. 解析 URL
            if progress_callback:
                progress_callback(10, "解析 URL...")

            parser = URLParser()
            parse_result = parser.parse(url)
            result['metadata'].update({
                k: v for k, v in parse_result.items()
                if k not in ['audio_url', 'video_url']
            })

            # 2. 下载音频
            if progress_callback:
                progress_callback(20, "下载音频...")

            downloader = Downloader(output_dir=str(output_path / "temp"))
            audio_file = downloader.download_to_wav(
                url,
                progress_callback=lambda p, s: progress_callback(
                    20 + p * 0.3,  # 20-50%
                    f"下载音频: {s}"
                )
            )

            # 3. 转录
            if progress_callback:
                progress_callback(50, "转录音频...")

            segments = self.transcribe(
                audio_file,
                progress_callback=lambda p, s: progress_callback(
                    50 + p * 0.4,  # 50-90%
                    f"转录: {s}"
                )
            )

            result['segments'] = segments

            # 4. 生成字幕文件
            if progress_callback:
                progress_callback(90, "生成字幕文件...")

            # 生成文件名
            filename = parse_result.get('title', 'subtitle')
            filename = "".join(c for c in filename if c.isalnum() or c in (' ', '-', '_')).strip()
            if not filename:
                filename = "subtitle"

            # 生成各种格式
            for fmt in output_formats:
                if fmt == 'srt':
                    file_path = str(output_path / f"{filename}.srt")
                    self.generate_srt(segments, file_path)
                    result['files']['srt'] = file_path
                elif fmt == 'txt':
                    file_path = str(output_path / f"{filename}.txt")
                    self.generate_txt(segments, file_path)
                    result['files']['txt'] = file_path
                elif fmt == 'md':
                    file_path = str(output_path / f"{filename}.md")
                    self.generate_markdown(segments, parse_result, file_path)
                    result['files']['md'] = file_path

            # 5. 清理临时文件
            if progress_callback:
                progress_callback(95, "清理临时文件...")

            import shutil
            temp_dir = output_path / "temp"
            if temp_dir.exists():
                shutil.rmtree(temp_dir)

            if progress_callback:
                progress_callback(100, "完成！")

            return result

        except Exception as e:
            raise RuntimeError(f"处理失败: {str(e)}")


# 使用示例
if __name__ == '__main__':
    def progress_callback(progress, status):
        print(f"[{progress:.0f}%] {status}")

    # 创建 ASR 引擎
    asr = ASREngine(model_name="SenseVoiceSmall", device="cpu")

    # 处理 URL
    url = "https://www.xiaoyuzhou.com/episode/123456"
    result = asr.process_url(
        url,
        output_dir="./outputs",
        progress_callback=progress_callback
    )

    print(f"\n生成文件:")
    for fmt, path in result['files'].items():
        print(f"  {fmt.upper()}: {path}")
