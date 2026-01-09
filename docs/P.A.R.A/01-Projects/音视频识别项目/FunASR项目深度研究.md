# FunASR 项目深度研究

## 项目概述

**FunASR** 是阿里巴巴达摩院（Alibaba DAMO Academy）开源的基础端到端语音识别工具包，提供学术级和工业级的语音识别模型。

| 项目信息 | 详情 |
|---------|------|
| **GitHub** | https://github.com/modelscope/FunASR |
| **Star 数** | 14,382+ |
| **Fork 数** | 1,500+ |
| **主要语言** | Python |
| **许可证** | Model License Agreement |
| **平台** | ModelScope / Hugging Face |

---

## 核心特性

### 1. 全功能语音识别工具包

- ✅ **语音识别 (ASR)**：离线/流式识别
- ✅ **语音活动检测 (VAD)**：检测有效语音片段
- ✅ **标点恢复**：自动添加标点符号
- ✅ **语言模型 (LM)**：Ngram 语言模型
- ✅ **说话人确认**：声纹识别
- ✅ **说话人分离**：多说话人场景识别
- ✅ **情感识别**：语音情感分类
- ✅ **关键词检测**：特定词检测
- ✅ **多说话人 ASR**：同时识别多说话人内容

### 2. 核心优势

| 优势 | 说明 |
|------|------|
| **工业级质量** | 在海量真实数据上训练的模型 |
| **高效率** | CPU RTF 0.0076，多线程加速 1200+ |
| **易部署** | 提供完整的 runtime 服务部署方案 |
| **多语言支持** | 支持中文、英文、日文、韩文等 31+ 语言 |
| **流式/离线** | 支持实时转录和离线文件处理 |
| **开源生态** | 模型、工具、教程全开源 |

---

## 模型动物园 (Model Zoo)

### 最新旗舰模型

#### 1. Fun-ASR-Nano-2512 ⭐⭐⭐

- **参数量**: 800M
- **训练数据**: 数千万小时真实语音数据
- **功能**:
  - 支持中文、英文、日文
  - 中文支持 7 种方言和 26 种地方口音
  - 英文和日文覆盖多种地方口音
  - 歌词识别
  - 说唱语音识别
- **特点**: 低延迟实时转录，覆盖 31 种语言

#### 2. SenseVoiceSmall

- **参数量**: 234M
- **训练数据**: 300,000 小时
- **功能**:
  - ASR（自动语音识别）
  - ITN（逆文本标准化）
  - LID（语言识别）
  - SER（情感识别）
  - AED（音频事件检测）
- **支持语言**: 中文 (zh)、粤语 (yue)、英文 (en)、日文 (ja)、韩文 (ko)
- **特点**: 多语音理解能力的语音基础模型

#### 3. Paraformer 系列

| 模型 | 参数 | 功能 | 训练数据 |
|------|------|------|----------|
| **paraformer-zh** | 220M | 离线识别，带时间戳 | 60,000 小时中文 |
| **paraformer-zh-streaming** | 220M | 流式识别 | 60,000 小时中文 |
| **paraformer-en** | 220M | 英文离线识别 | 50,000 小时英文 |

**特点**: 非自回归端到端模型，高准确率、高效率、易部署

#### 4. 辅助模型

| 模型 | 功能 | 参数量 |
|------|------|--------|
| **ct-punc** | 标点恢复 | 290M |
| **fsmn-vad** | 语音活动检测 | 0.4M |
| **fsmn-kws** | 关键词检测 | 0.7M |
| **cam++** | 说话人确认/分离 | 7.2M |
| **fa-zh** | 时间戳预测 | 38M |
| **emotion2vec+** | 情感识别 | 300M |

#### 5. Whisper 系列

| 模型 | 参数量 | 特点 |
|------|--------|------|
| **Whisper-large-v3** | 1550M | 多语言识别，带时间戳 |
| **Whisper-large-v3-turbo** | 809M | 多语言识别，带时间戳，更高效 |

---

## 最新更新 (2024-2025)

### 2025 最新

- **Fun-ASR-Nano-2512**: 数千万小时数据训练的大模型，支持 31 种语言

### 2024 年重大更新

**12 月 15 日**
- Fun-ASR-Nano-2512 发布，支持 31 种语言的低延迟实时转录

**10 月 29 日**
- 实时转录服务 1.12 发布
- 2pass-offline 模式支持 SensevoiceSmall

**10 月 10 日**
- 新增 Whisper-large-v3-turbo 模型支持
- 支持多语言语音识别、语音翻译、语言识别

**9 月 25-26 日**
- 关键词检测模型支持
- SensevoiceSmall ONNX 模型支持
- 修复内存泄漏

**7 月 4 日**
- SenseVoice 发布：语音基础模型，支持 ASR、LID、SER、AED

---

## 安装指南

### 环境要求

```text
python >= 3.8
torch >= 1.13
torchaudio
```

### 安装方法

#### 方法 1: pip 安装（推荐）

```bash
pip3 install -U funasr
```

#### 方法 2: 从源码安装

```bash
git clone https://github.com/modelscope/FunASR.git && cd FunASR
pip3 install -e ./
```

#### 方法 3: 安装 ModelScope（可选）

```bash
pip3 install -U modelscope huggingface_hub
```

---

## 快速开始

### 1. 命令行使用

```bash
# 基础识别
funasr ++model=paraformer-zh ++vad_model="fsmn-vad" ++punc_model="ct-punc" ++input=asr_example_zh.wav
```

### 2. Python API - Fun-ASR-Nano

```python
from funasr import AutoModel

model_dir = "FunAudioLLM/Fun-ASR-Nano-2512"

model = AutoModel(
    model=model_dir,
    vad_model="fsmn-vad",
    vad_kwargs={"max_single_segment_time": 30000},
    device="cuda:0",
)

res = model.generate(
    input=[wav_path],
    cache={},
    batch_size_s=0
)

text = res[0]["text"]
print(text)
```

**参数说明**:
- `model_dir`: 模型名称或本地路径
- `vad_model`: 启用 VAD（语音活动检测）
- `vad_kwargs`: VAD 配置，`max_single_segment_time` 表示音频分段最大时长（毫秒）
- `batch_size_s`: 动态批处理，单位为秒

### 3. Python API - SenseVoice

```python
from funasr import AutoModel
from funasr.utils.postprocess_utils import rich_transcription_postprocess

model_dir = "iic/SenseVoiceSmall"

model = AutoModel(
    model=model_dir,
    vad_model="fsmn-vad",
    vad_kwargs={"max_single_segment_time": 30000},
    device="cuda:0",
)

# 英文识别
res = model.generate(
    input=f"{model.model_path}/example/en.mp3",
    cache={},
    language="auto",  # "zn", "en", "yue", "ja", "ko", "nospeech"
    use_itn=True,
    batch_size_s=60,
    merge_vad=True,
    merge_length_s=15,
)

text = rich_transcription_postprocess(res[0]["text"])
print(text)
```

**参数说明**:
- `use_itn`: 是否包含标点和逆文本标准化
- `merge_vad`: 是否合并 VAD 分割的短音频片段
- `merge_length_s`: 合并后的长度（秒）
- `ban_emo_unk`: 是否禁止输出 `emo_unk` token

### 4. Python API - Paraformer

```python
from funasr import AutoModel

model = AutoModel(
    model="paraformer-zh",
    vad_model="fsmn-vad",
    punc_model="ct-punc",
    # spk_model="cam++",  # 说话人识别（可选）
)

res = model.generate(
    input=f"{model.model_path}/example/asr_example.wav",
    batch_size_s=300,
    hotword='魔搭'  # 热词
)

print(res)
```

### 5. 流式识别

```python
from funasr import AutoModel
import soundfile
import os

# 流式配置
chunk_size = [0, 10, 5]  # [0, 10, 5] = 600ms, [0, 8, 4] = 480ms
encoder_chunk_look_back = 4  # 编码器回看的 chunk 数量
decoder_chunk_look_back = 1  # 解码器回看的编码器 chunk 数量

model = AutoModel(model="paraformer-zh-streaming")

wav_file = os.path.join(model.model_path, "example/asr_example.wav")
speech, sample_rate = soundfile.read(wav_file)
chunk_stride = chunk_size[1] * 960  # 600ms

cache = {}
total_chunk_num = int(len((speech)-1)/chunk_stride+1)

for i in range(total_chunk_num):
    speech_chunk = speech[i*chunk_stride:(i+1)*chunk_stride]
    is_final = i == total_chunk_num - 1

    res = model.generate(
        input=speech_chunk,
        cache=cache,
        is_final=is_final,
        chunk_size=chunk_size,
        encoder_chunk_look_back=encoder_chunk_look_back,
        decoder_chunk_look_back=decoder_chunk_look_back
    )

    print(res)
```

**参数说明**:
- `chunk_size`: 流式延迟配置
  - `[0, 10, 5]` = 实时显示粒度为 `10*60=600ms`
  - 前瞻信息为 `5*60=300ms`
- `is_final`: 最后一个语音段输入时设为 `True`

---

## VAD（语音活动检测）

### 离线 VAD

```python
from funasr import AutoModel

model = AutoModel(model="fsmn-vad")
wav_file = f"{model.model_path}/example/vad_example.wav"

res = model.generate(input=wav_file)
print(res)
```

**输出格式**: `[[beg1, end1], [beg2, end2], ..., [begN, endN]]`
- `begN/endN`: 第 N 个有效音频段的起止点（毫秒）

### 流式 VAD

```python
from funasr import AutoModel
import soundfile

chunk_size = 200  # ms
model = AutoModel(model="fsmn-vad")

wav_file = f"{model.model_path}/example/vad_example.wav"
speech, sample_rate = soundfile.read(wav_file)
chunk_stride = int(chunk_size * sample_rate / 1000)

cache = {}
total_chunk_num = int(len((speech)-1)/chunk_stride+1)

for i in range(total_chunk_num):
    speech_chunk = speech[i*chunk_stride:(i+1)*chunk_stride]
    is_final = i == total_chunk_num - 1

    res = model.generate(
        input=speech_chunk,
        cache=cache,
        is_final=is_final,
        chunk_size=chunk_size
    )

    if len(res[0]["value"]):
        print(res)
```

---

## 服务部署

### Runtime 服务类型

| 服务类型 | 说明 | 性能指标 |
|---------|------|----------|
| **离线文件转录服务 (中文)** | CPU/GPU 版本 | RTF 0.0076，多线程加速 1200+ |
| **离线文件转录服务 (英文)** | CPU/GPU 版本 | - |
| **实时转录服务** | 流式识别 | 支持 2pass 模式 |
| **GPU Triton 服务** | NV-Triton 部署 | RTF 0.0032，吞吐率 300 |
| **C++ gRPC 服务** | C++ 版本 | 性能相比 Python 翻倍 |

### 部署文档

- [Runtime 部署文档](https://github.com/alibaba-damo-academy/FunASR/blob/main/runtime/readme.md)
- [Windows SDK](https://www.modelscope.cn/models/damo/funasr-runtime-win-cpu-x64/summary)

---

## 性能基准

### CPU 性能 (Intel Xeon 8369B)

| 指标 | 数值 |
|------|------|
| RTF（实时率） | 0.0076 |
| 多线程加速比 | 1200+ |
| 量化加速比 | 2x |

### GPU 性能 (NVIDIA V100)

| 指标 | 数值 |
|------|------|
| RTF（实时率） | 0.0032 |
| 吞吐率 | 300 |

---

## 与 Whisper 对比

| 特性 | FunASR | Whisper |
|------|--------|---------|
| **中文效果** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| **幻听问题** | 较少 | 较多 |
| **标点符号** | 自动添加 | 需要后处理 |
| **部署难度** | 中等 | 简单 |
| **模型大小** | 多种选择 | tiny~large |
| **多语言** | 31+ 语言 | 99 种语言 |
| **流式识别** | 原生支持 | 实验性 |
| **VAD 集成** | 内置 | 需要额外处理 |
| **工业部署** | 完整方案 | 需要自己搭建 |

---

## 应用场景

### 1. 视频字幕生成
- 离线批量处理
- 实时字幕生成
- 多语言字幕

### 2. 会议记录
- 说话人分离
- 自动添加标点
- 实时转录

### 3. 客服质检
- 关键词检测
- 情感识别
- 语音转文字

### 4. 播客/有声书
- 章节分割
- 时间戳生成
- 多语言翻译

### 5. 实时通信
- 实时字幕
- 语音转文字
- 低延迟场景

---

## 相关项目

### FunASR 生态

| 项目 | 说明 | GitHub |
|------|------|--------|
| **FunCodec** | 神经语音编解码工具包 | [链接](https://github.com/alibaba-damo-academy/FunCodec) |
| **SlideSpeech** | 多模态音视频语料库 | [链接](https://slidespeech.github.io/) |
| **Qwen-Audio** | 音频文本多模态模型 | Hugging Face |
| **SpeechGPT** | 语音大语言模型 | - |

---

## 学习资源

### 官方文档

- [GitHub 仓库](https://github.com/modelscope/FunASR)
- [ModelScope 模型库](https://www.modelscope.cn/models?page=1&tasks=auto-speech-recognition)
- [教程文档](https://github.com/alibaba-damo-academy/FunASR/blob/main/docs/tutorial/README.md)

### 社区

- GitHub Issues
- ModelScope 社区
- Hugging Face 社区

---

## 总结

FunASR 是一个功能全面、性能优秀的工业级语音识别工具包：

✅ **优势**:
- 工业级模型质量
- 完整的部署方案
- 多语言、多功能支持
- 活跃的开源社区

⚠️ **注意事项**:
- 部署相对复杂
- 需要一定的技术门槛
- 文档主要为中文

**推荐使用场景**:
- 需要工业级质量的生产环境
- 中文语音识别需求
- 需要完整端到端解决方案
- 需要实时/流式识别

---

*研究日期：2026年1月9日*
