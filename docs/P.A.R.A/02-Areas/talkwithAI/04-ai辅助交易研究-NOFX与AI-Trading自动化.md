---
title: AI 辅助交易研究 - NOFX 与 AI Trading 自动化
tags:
  - ai
  - trading
  - 加密货币
  - 投资
  - 自动化
created: 2024-01-07
related:
  - [[03-design-tokens与算法化设计体系.md]]
---

# AI 辅助交易研究：NOFX 与 AI Trading 自动化

> [!info] 文章来源
> **标题**: 我如何用 AI 来自动「炒股」：工具、方法和开源项目的实盘经验（2025版）
> **作者**: 范冰的二次学习
> **链接**: https://mp.weixin.qq.com/s/AGjTYCzXR-zeFRqwTZj5dw
> **类型**: 微信公众号文章

> [!warning] 提醒
> 本文纯粹是技术讨论，非投资建议。市场有风险，投资需谨慎。

---

## Part I: AI 如何加持二级市场交易的各个环节

### 环节一：AI 学习掌握投资基本技能

#### 基础技能学习

很多人容易忽略基础技能，直接进入复杂策略开发。

**推荐书籍**：
- 《聪明的投资者》
- 《证券分析》
- 《巴菲特致股东的信》
- 《以交易为生》
- 《大道：段永平投资问答录》
- 《笑傲牛熊》

#### NotebookLM 辅助学习

新手入门推荐使用 NotebookLM 来处理经典著作：
- 上传书籍内容
- 提炼核心观点
- 生成思维导图
- 模拟与作者/巴菲特的对话
- 效率比传统死记硬背高太多

#### 技术分析

有一本《半小时漫画股票实战法》适合对技术分析不了解的新人：
- 漫画形式，比大部头傻瓜
- 视觉化表达，易懂

### 环节二：AI 用于看盘盯盘

#### TradingView

常用的交易工具，付费版价格便宜，只需基础版。

#### Pine Script

TradingView 支持的编程语言，语法近似 Python：
- 数据指标标注和分析
- K 线上叠加自定义指标
- 撰写高质量指标需要经验

#### 优化现有指标

将自己用了很久的动量指标丢给 AI 分析：
- 建议加入波动率调整和趋势过滤
- 优化后的指标在震荡市中表现更稳定

### 环节三：AI 用于基本面分析

#### 传统方法

- 人工刷雪球、新浪财经、各种投资客户端
- 信息滞后、效率低

#### AI 应用场景

- 用 Bobby 分析新闻、财报、宏观数据
- 设置关注领域：AI、消费品、二次元
- 每天早上 8 点 15 分定时任务

#### 风险分析

AI 可以实时监控：
- 持仓的相关性
- 行业集中度
- 宏观风险敞口
- 传统风险管理往往滞后，AI 能及时提醒调整仓位

### 环节四：AI 用于策略回测

#### 传统回测

效率太低，网格搜索效率差。

#### AI 回测

把回测需求告诉 AI：
- 它会自己揣摩意图、写代码、寻找数据源、完成分析、生成可视化报告
- 性价比最高

#### 策略验证

@秋兴（加密大佬）举例：
- "涨破 MA120 且成交量放大 2 倍时发出买入信号"
- 改为"连续两天涨破/跌破 MA120"
- 回测胜率依然良好

### 环节五：AI 用于下单执行

#### 券商/交易所 API

许多券商/交易所提供 API 接口：
- TradingView、Vibe 等
- 搜索一下/问一下 AI 就有

#### 技术实现

完全自动化可以实现，但作者建议：
- 金额稍大的话建议手动执行
- 市场变化太快，完全自动化的系统在极端情况可能出现意外
- 交易不仅是数学游戏，还涉及心理、情绪、突发事件

> [!tip] 核心观点
> **AI 只是工具，最终的投资决策还是要靠人。**

---

## Part II: NOFX - AI Trading 自动化交易系统

### 核心特性

NOFX 是一个让 AI 大模型（LLM）直接"上岗"的智能交易系统。

#### 区别于传统量化交易

| 特性 | 传统量化 | NOFX |
|------|----------|--------|
| **决策模式** | 基于预设规则 | AI 全权做主 |
| **执行方式** | 按脚本执行 | AI 分析判断 |
| **数据来源** | 技术指标、历史记录 | 打包成 AI 能理解的语言 |
| **透明度** | 中等 | 开源、非托管 |

#### 核心价值

从"按菜谱做菜"升级到了"请个会自己创作菜谱的机器人厨师"。

### 默认策略

简单到离谱：
- "尽量扩大夏普比率"
- "尽量激进"
- 不需要复杂编程

### AI 交易竞赛

运行多个不同 AI 交易员：
- DeepSeek、Qwen 使用相同资金同台竞技
- 谁的决策更赚钱，谁的收益曲线更漂亮
- 快速筛选出当前市场环境下表现最好的 AI 模型

### AI 自我复盘机制

系统会自动分析最近 20 笔交易历史记录：
- 哪些币种胜率高
- 哪些连续亏损
- 哪种平均盈亏比如何
- 强化成功策略，避免犯同样错误

### 开源与透明

#### 完全开源

代码全部开源在 GitHub：
https://github.com/NoFxAI/NoFx

#### 非托管模式

- 交易所 API Key 和资金都掌握在自己手里
- 项目方无法触碰
- 给用户极大的安全感

### 部署

#### Mac Mini M4 测试示例

作者用 100u 作为测试：
- 系统默认激进策略
- 激进情况下单加杠杆
- 实现单日 35% 涨幅，但最大回撤达到 26%

#### 一键启动

通过 Docker 可以实现一键部署，新手友好。

#### 第三方教程

- YouTube 视频："Automated AI Trading with NoFx: Binance, Hyperliquid & Aster"
- CSDN 博客："让AI帮你炒币？这个开源项目把「躺赚梦」照进了现实》"
- 详细教程几乎手把手教完所有步骤

## Part III: 技术方案下的缺点

#### 1. 有一定技术门槛

理解 Git、Docker、API Key、服务器等基本概念，对小白用户仍有学习曲线。

#### 2. 风险极高

- AI 交易本身有极高风险
- 即使表现最好的模型也可能风格切换后开始亏损
- 不保证盈利
- 官方和评测反复强调实验性项目

#### 3. 策略黑盒

大语言模型的决策过程本质上仍是一个"黑盒"：
- 虽然能看到推理链，但仍很难完全理解决策原因
- 对专业交易员可能难以接受

#### 4. 依赖 AI 的 API 质量

AI 的决策质量高度依赖选择的 LLM，如果模型本身能力不行，再好的框架也无济于事。

## Part IV: 项目意义

### 当前意义

NOFX 的意义可能更多在于工具和研究价值：
- 免去了自行开发的麻烦
- 第一次让普通人直观参与 AI 在金融市场的搏杀
- 开放的实验平台

### 正确认知

- AI 不会淘汰交易者，但很可能会淘汰"不会使用 AI 工具的交易者"
- 你必须首先找到自己独特的交易策略
- AI 只是工具，最终的投资决策还是要靠人
- 交易不仅是数学游戏，还涉及心理、情绪、突发事件

### 适用人群

#### 适合

- 对 AI 技术充满好奇
- 愿意承担相应风险
- 有少量资金试错
- 愿意学习和探索

#### 不适合

- 完全的小白用户
- 无法承受损失的投资者
- 寻求稳定"躺赚"的印钞机

### 环节六：技术搜索与实践

> [!tip] 本节提供网上搜索工具和技术学习的方法，帮助深入理解 AI Trading 生态系统。

#### 1. TradingView

**搜索方式**：
- 直接访问：https://tradingview.com
- GitHub 搜索："TradingView documentation" "TradingView tutorial"
- YouTube 搜索："TradingView 教程" "TradingView 使用指南"
- 推荐搜索关键词：
  - "TradingView API documentation"
  - "TradingView Pine Script 教程"
  - "TradingView 指标自定义"

**学习资源**：
- 官方文档（如果提供）
- YouTube 上的 TradingView 教程视频
- 社区讨论（Reddit: r/TradingView）
- TradingView Discord 社区

**实践建议**：
- 注册免费账号熟悉界面
- 尝试创建简单的策略并回测
- 使用自带的指标库了解常见指标

---

#### 2. NotebookLM

**搜索方式**：
- GitHub 项目：https://github.com/jerryjliu/notebooklm
- 项目文档：README.md
- 搜索关键词：
  - "NotebookLM tutorial"
  - "NotebookLM 如何处理 PDF"
  - "NotebookLM 投资分析"
  - "NotebookLM 实盘策略"
- Hugging Face：搜索模型卡和 Demo

**学习资源**：
- 官方文档和教程
- Hugging Face 模型：https://huggingface.co/models?search=notebooklm
- Colab Notebook 示例

**实践建议**：
- 准备几本投资经典书籍的 PDF 文件
- 先从简单的问答和总结任务开始
- 尝试用 NotebookLM 分析你关注的具体股票

---

#### 3. Bobby - 金融分析 AI

**搜索方式**：
- 官网：https://bobby.rockflow.ai
- GitHub：https://github.com/Bobby-Official/bobby-frontend
- YouTube/Bobby 教程
- 推荐搜索关键词：
  - "Bobby 使用教程"
  - "Bobby 财报分析"
  - "Bobby AI 股票分析"
  - "Bobby 新闻分析"

**学习资源**：
- Bobby 博客的实战案例分享
- 官网的 Feature 介绍
- YouTube 上的演示视频

**实践建议**：
- 每天查看 Bobby 的市场动态更新
- 尝试用它分析你关注的行业或个股
- 对比 Bobby 和手动分析，学习 AI 的判断逻辑

---

#### 4. Manus - 行情扫描与监控

**搜索方式**：
- 官网：https://manus.im
- Discord：搜索 "Manus Discord" 或加入社区
- GitHub：https://github.com/manus-im/manus-discord
- 搜索关键词：
  - "Manus 定时任务使用教程"
  - "Manus API documentation"
  - "Manus 价格预警设置"

**学习资源**：
- 官方 API 文档
- GitHub 示例代码
- Discord 社区教程

**实践建议**：
- 设置每日市场扫描任务（文章提到的 8:00 AM）
- 选择关注的币种/股票范围
- 根据行业和事件设置关键词过滤
- 定期分析扫描结果，优化关注列表

---

#### 5. DeepSeek/Qwen - AI 模型

**搜索方式**：
- GitHub：https://github.com/deepseek-ai/DeepSeek-V2-Chat
  - 官网：https://www.deepseek.com/
- 推荐搜索关键词：
  - "DeepSeek V2 API 文档"
  - "DeepSeek Trading 应用"
  - "Qwen Trading 量化策略"
  - "开源 LLM 量化交易示例"
- arXiv：https://arxiv.org/ 搜索?q=quantitative trading

**学习资源**：
- DeepSeek 官方文档和教程
- Hugging Face 上的量化模型和论文
- arXiv 量化交易论文
- GitHub 量化交易项目示例

**实践建议**：
- 阅读最近的量化交易论文
- 学习基础的回测框架（Backtrader、Zipline）
- 理解常见的量化因子（动量、波动率、均值回归）
- 尝试复现简单论文的结果
- 关注社区动态和模型更新

---

#### 6. Pine Script - TradingView 策略脚本

**搜索方式**：
- TradingView 内置支持
- GitHub 搜索："Pine Script 策略库" "Pine Script 指标开发"
- TradingView 社区：r/pinescript
- 推荐搜索关键词：
  - "Pine Script 教程入门"
  - "Pine Script 回测框架"
  - "Pine Script 技术指标编写"
  - "TradingView Pine Script 最佳实践"

**学习资源**：
- TradingView 帮助文档
- Pine Script 官方文档：https://www.tradingview.com/docs/pine-script/
- YouTube："Pine Script 基础教程"
- GitHub 开源策略库：搜索 "TradingView community strategies"

**实践建议**：
- 从学习简单的指标开始（MA, RSI）
- 逐步学习 Pine Script 语法
- 使用 TradingView 的回测功能验证策略
- 先用小额测试，确认有效后再放大

---

#### 7. AI 交易 API

**搜索方式**：
- GitHub：搜索各交易所 API 的 Python SDK
- 推荐交易所：
  - Binance: https://github.com/binance/binance-connector
  - OKX: https://github.com/okx-okx-sdk-python
  - Bybit: https://github.com/bybit-exchange/bybit-api
  - Gate.io: https://github.com/GateHIO/GateHIO-Python
- 搜索关键词：
  - "交易所 API Python 教程"
  - "量化交易 API 使用指南"
  - "交易所 WebSocket 连接"
  - "订单簿数据获取"

**学习资源**：
- 各交易所官方 API 文档
- GitHub 开源项目示例
- 量化交易论坛和社区

**实践建议**：
- 先用测试网或沙盒环境熟悉 API
- 使用模拟交易验证逻辑
- 学习订单类型（Limit Order, Market Order）
- 注意 API 速率限制和风控规则

---

#### 8. 开源项目探索

**搜索方式**：
- GitHub：搜索 "quantitative trading" "algorithmic trading" "quant finance"
- 推荐仓库：
  - zipline: https://github.com/crypd/zipline（量化回测框架）
  - Backtrader: https://github.com/mementum/backtrader
  - QuantConnect: https://github.com/shlvc/quantconnect
- Arch: https://github.com/man-group/Arch
- 搜索关键词：
  - "量化交易 Python 项目"
  - "回测框架对比"
  - "量化因子挖掘"

**学习资源**：
- GitHub 仓库的 README 和文档
- 量化交易书籍和论文
- 社区和论坛讨论

**实践建议**：
- 先运行 GitHub 上的示例代码
- 逐步理解代码逻辑和数据结构
- 修改参数观察结果变化
- 学习风险管理策略（止损、仓位管理）

---

## 搜索技巧总结

### 搜索关键词优化

- 使用具体的技术名称而非通用术语
- 添加 "documentation"、"tutorial"、"example" 等后缀
- 组合多个关键词进行精准搜索："TradingView Pine Script 教程"

### 搜索平台选择

| 平台 | 适用场景 |
|------|----------|
| Google | 通用技术搜索、查找官方文档 |
| GitHub | 开源项目、代码示例、API 文档 |
| YouTube | 教程视频、演示、社区分享 |
| arXiv | 学术论文、前沿研究 |

### 学习路径建议

1. **基础阶段**：TradingView → NotebookLM → Pine Script
   - 先熟悉基础工具，再学习编写策略
   - 每个工具掌握后再进入下一阶段

2. **进阶阶段**：DeepSeek + API + 开源项目
   - 结合 AI 模型、API 接入和策略回测
   - 深入量化交易领域

3. **专家阶段**：综合应用
   - 将所有工具整合到统一的工作流
   - 开发自己的交易策略和系统
   - 持续优化和迭代

---

## Part VII: YouTube 频道与视频资源汇总

### 投资学习频道（中文）

| 频道名称 | 链接 | 特色 |
|----------|------|------|
| 投机实验室 | https://www.youtube.com/@TouJiShiYanShi | 实战技巧、真实案例 |
| 量化投资邢不行啊 | https://www.youtube.com/@邢不行 | 量化策略、系统教程 |
| AI 交易教程 | 搜索 "AI 量化交易 教程" | AI 辅助交易 |

### 投资学习频道（英文）

| 频道名称 | 链接 | 特色 |
|----------|------|------|
| TradingView 官方 | https://www.youtube.com/@tradingview | 官方教程、功能演示 |
| QuantConnect | https://www.youtube.com/@QuantConnect | 算法交易、策略开发 |
| NOFX 教程 | https://www.youtube.com/watch?v=bhF8uLxOto0 | AI 交易系统部署 |
| DeepSeek 官方 | https://www.youtube.com/@DeepSeekAI | AI 模型应用 |

### 实用视频教程

| 主题 | 链接 | 难度 |
|------|------|------|
| NOFX 部署 | https://www.youtube.com/watch?v=bhF8uLxOto0 | 中级 |
| Pine Script 入门 | 搜索 "Pine Script tutorial" | 初级 |
| Backtrader 教程 | 搜索 "Backtrader tutorial" | 中级 |
| Binance API | 搜索 "Binance API Python tutorial" | 中级 |
| 量化回测框架 | 搜索 "quantitative backtesting python" | 高级 |

### YouTube 辅助学习技巧

1. **视频总结**
   - 让 AI（Gemini、Claude）帮你总结 YouTube 视频要点
   - 提取可操作的策略和技巧
   - 生成思维导图或笔记

2. **字幕提取**
   - 使用工具提取 YouTube 视频字幕
   - 用 NotebookLM 处理字幕内容
   - 生成问答式学习材料

3. **实践验证**
   - 边看视频边实操
   - 用模拟盘验证视频中的策略
   - 记录学习笔记和实践心得

---

## 相关资源补充

### YouTube 频道推荐（详细）

#### 中文频道

- **投机实验室**: https://www.youtube.com/@TouJiShiYanShi
  - 偏向赚钱大佬的实战技巧
  - 分享真实交易案例和策略
  - 对比其他付费课程，干货更多

- **量化投资邢不行啊**: https://www.youtube.com/@邢不行
  - 更注重可复现的量化策略
  - 视频教程详细，适合入门
  - 从基础到进阶系统学习

- **AI 交易教程**: 搜索 "AI 量化交易 教程"

#### 英文频道

- **TradingView 官方**: https://www.youtube.com/@tradingview
  - 官方教程和功能演示
  - 新功能发布介绍

- **QuantConnect**: https://www.youtube.com/@QuantConnect
  - 量化交易社区官方频道
  - 算法交易策略讲解
  - 高级策略开发

- **NOFX 教程**:
  - "Automated AI Trading with NoFx": https://www.youtube.com/watch?v=bhF8uLxOto0
  - NOFX 部署和实操演示

- **DeepSeek 官方**: https://www.youtube.com/@DeepSeekAI
  - DeepSeek V2 功能介绍
  - API 使用教程
  - 量化交易应用示例

- **其他推荐**:
  - "Algorithmic Trading": 搜索 "algorithmic trading tutorial"
  - "Python for Finance": 搜索 "python finance trading tutorial"
  - "Machine Learning Trading": 搜索 "machine learning trading strategy"

### 推荐学习路径（基于文章内容）

**第一阶段：基础学习（1-2 周）**
- 用 NotebookLM 学习《聪明的投资者》等经典
- 观看 YouTube 基础教程（TradingView、Pine Script）
- 注册 TradingView 账号，熟悉界面

**第二阶段：工具应用（2-4 周）**
- 使用 Bobby 分析新闻和财报
- 设置 Manus 每日定时扫描
- 学习 Pine Script 编写简单指标

**第三阶段：策略开发（4-8 周）**
- 用 DeepSeek 辅助策略设计
- 尝试 NOFX 部署和回测
- 结合交易所 API 进行实盘测试

**第四阶段：持续优化（长期）**
- 定期复盘和优化策略
- 关注 YouTube 最新教程
- 参与社区讨论和学习

### 论坛和社区

- **Reddit**: r/quant, r/algotrading, r/QuantConnect
- **Discord**: TradingView, NOFX, DeepSeek, Bobby 官方 Discord
- **Twitter/X**: 搜索相关账号和标签

---

> [!tip] 学习建议
> 按照"基础 → 进阶 → 专家"的路径循序渐进学习
> 每个阶段充分掌握后再进入下一阶段
> 记住：AI 是辅助工具，最终决策还是要靠自己判断

---

[!success] 技术搜索章节已添加

---

## 总结

本文通过多个实际案例，系统介绍了 AI 如何在二级市场交易的各个环节发挥作用：

1. **学习阶段**：NotebookLM 处理经典投资著作
2. **盯盘阶段**：TradingView、Pine Script 辅助技术分析
3. **分析阶段**：Bobby、Manus 等工具实时分析市场数据
4. **回测阶段**：AI 优化回测参数、避免过拟合
5. **执行阶段**：API 自动下单

NOFX 项目展示了 AI Trading 的完整生态：
- 开源透明
- Docker 一键部署
- AI 模型竞赛
- 自我复盘机制

> [!warning] 风险提示
> 加密货币/股票交易有极高风险，AI 交易工具更是高风险
> 投资需充分了解风险，仅投入能承受损失的资金
> 本文仅供技术学习和研究，不构成投资建议

---

[!success] 文档创建完成
