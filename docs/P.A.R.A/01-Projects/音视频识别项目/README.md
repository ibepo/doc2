# 播客字幕自动生成器

从播客/视频 URL 自动生成字幕的 AI 工具

## 功能特点

- 🎙️ **多平台支持**：小宇宙、喜马拉雅、B站、YouTube 等 1000+ 网站
- 🤖 **AI 驱动**：基于 FunASR (SenseVoice) 语音识别
- 📝 **多种格式**：SRT 字幕、TXT 文本、Markdown 文档
- 🌍 **多语言**：支持中文、英文、日语、韩语等 31+ 种语言
- 🖥️ **两种界面**：GUI 桌面应用 + MCP 服务器

---

## 快速开始

### 安装依赖

```bash
# 1. 安装 Python 依赖
pip install -r requirements.txt

# 2. 安装 ffmpeg
# macOS
brew install ffmpeg

# Ubuntu/Debian
sudo apt install ffmpeg

# Windows
# 从 https://ffmpeg.org 下载并添加到 PATH
```

### 使用方法

#### 方式 1: GUI 界面（推荐）

```bash
python gui_launcher.py
```

浏览器会自动打开 http://localhost:7860

#### 方式 2: MCP 服务器（LLM 调用）

```bash
python mcp_server.py
```

---

## GUI 使用说明

### 界面截图

```
┌─────────────────────────────────────────────────────────────┐
│              播客字幕自动生成器                               │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  输入播客/视频 URL：                                         │
│  ┌──────────────────────────────────────────────────────┐   │
│  │ https://www.xiaoyuzhou.com/episode/xxxxx            │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                              │
│  ⚙️ 高级设置：                                               │
│    - ASR 模型: SenseVoiceSmall (推荐)                       │
│    - 设备: CPU / CUDA                                      │
│    - 语言: 自动                                            │
│    - 输出格式: SRT, TXT, MD                                 │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐   │
│  │            ▶  开始生成字幕                             │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                              │
│  输出：                                                       │
│  • SRT 字幕文件                                             │
│  • TXT 纯文本                                               │
│  • Markdown 文档                                            │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### 操作步骤

1. **粘贴 URL**：输入播客或视频链接
2. **选择模型**：SenseVoiceSmall 支持多语言
3. **点击开始**：等待处理完成
4. **下载文件**：获取生成的字幕

---

## MCP 使用说明

### 可用工具

#### 1. generate_subtitle

生成播客/视频的字幕

**参数**：
- `url` (必需): 播客或视频 URL
- `output_formats` (可选): 输出格式列表，如 ["srt", "txt"]
- `language` (可选): 识别语言 (auto/zh/en/yue/ja/ko)
- `model` (可选): ASR 模型

**返回**：
```
## 字幕生成完成！

**原始 URL**: https://...
**平台**: xiaoyuzhou
**标题**: 数字生命卡兹克如何用 AI

**统计信息**:
- 总时长: 2小时29分
- 文本片段数: 1234
- 总字数: 15234

**生成的文件**:
- **SRT**: /outputs/数字生命卡兹克_20250109.srt
- **TXT**: /outputs/数字生命卡兹克_20250109.txt
```

#### 2. parse_podcast

解析播客信息（不下载）

**参数**：
- `url` (必需): 播客页面 URL

**返回**：
播客的元数据信息（标题、作者、时长等）

### LLM 集成示例

在 Claude MCP 配置中添加：

```json
{
  "mcpServers": {
    "podcast-subtitle": {
      "command": "python",
      "args": ["/path/to/mcp_server.py"],
      "env": {}
    }
  }
}
```

然后在对话中：
```
用户：帮我把这个播客生成字幕 https://www.xiaoyuzhou.com/episode/12345

Claude：我来帮你生成字幕...
[调用 generate_subtitle 工具]
```

---

## 项目结构

```
podcast-subtitle-generator/
├── src/
│   ├── core/
│   │   ├── url_parser.py       # URL 解析器
│   │   ├── downloader.py       # 内容下载器
│   │   └── asr_engine.py       # ASR 引擎
│   ├── gui/
│   │   └── gradio_app.py       # Gradio 界面
│   └── mcp/
│       └── server.py           # MCP 服务器
├── outputs/                    # 输出目录
├── gui_launcher.py             # GUI 启动器
├── mcp_server.py               # MCP 启动器
├── config.yaml                 # 配置文件
├── requirements.txt            # 依赖
└── README.md                   # 文档
```

---

## 支持的平台

| 平台类型 | 平台名称 | 状态 |
|---------|---------|------|
| **播客** | 小宇宙 | ✅ |
| | 喜马拉雅 | ✅ |
| | 荔枝FM | ✅ |
| | Apple Podcasts | ✅ |
| **视频** | B站 | ✅ |
| | YouTube | ✅ |
| | 优酷 | ✅ |
| | 腾讯视频 | ✅ |
| **通用** | 直接音视频链接 | ✅ |

---

## ASR 模型

| 模型 | 参数量 | 特点 |
|------|--------|------|
| **SenseVoiceSmall** | 234M | 多语言、带标点、情感识别 |
| **Fun-ASR-Nano** | 800M | 31 种语言、实时转录 |
| **Paraformer** | 220M | 中文专用、工业级 |

---

## 性能参考

| 设备 | 速度 (实时率) |
|------|--------------|
| CPU (8核) | 0.05-0.1x |
| GPU (V100) | 0.01x |

**参考时间**：
- 1 小时音频
  - CPU: 约 5-10 分钟
  - GPU: 约 1-2 分钟

---

## 常见问题

### Q: ffmpeg 相关错误

```bash
# macOS
brew install ffmpeg

# Linux
sudo apt install ffmpeg

# Windows
# 下载：https://ffmpeg.org/download.html
```

### Q: 模型下载慢

使用 ModelScope（国内镜像），已默认启用。

### Q: CUDA 不可用

检查 GPU 驱动和 CUDA 安装：
```bash
nvidia-smi  # 检查 GPU
python -c "import torch; print(torch.cuda.is_available())"  # 检查 PyTorch CUDA
```

---

## 开发计划

- [ ] 支持批量处理
- [ ] 添加更多 ASR 模型
- [ ] 优化 GPU 内存使用
- [ ] 支持实时字幕
- [ ] 添加视频嵌入字幕功能

---

## 许可证

MIT License

---

## 致谢

- [FunASR](https://github.com/modelscope/FunASR) - 阿里巴巴达摩院
- [ModelScope](https://modelscope.cn) - 魔搭社区
- [Gradio](https://gradio.app) - UI 框架
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - 下载工具

---

*项目创建日期：2026年1月9日*
