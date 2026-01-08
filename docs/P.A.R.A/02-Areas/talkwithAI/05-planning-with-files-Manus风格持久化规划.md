---
title: Planning with Files - Manus 风格持久化规划
tags:
  - ai
  - planning
  - claude-code
  - workflow
  - context-engineering
created: 2024-01-07
related:
  - [[01-obsidian-skills说明.md]]
  - [[08-ai辅助交易研究-NOFX与AI-Trading自动化.md]]
---

# Planning with Files：Manus 风格的持久化规划工作流

> [!info] 项目信息
> **项目名称**: planning-with-files
> **作者**: Ahmad Othman Ammar Adi
> **GitHub**: https://github.com/OthmanAdi/planning-with-files
> **Stars**: 2.6k
> **Forks**: 242
> **许可证**: MIT

> [!quote] 背景
> 2024 年 12 月 29 日，Meta 以 **20亿美元** 收购了 Manus。在短短 8 个月内，Manus 从发布到实现 1亿美元+收入。他们的秘诀是什么？**Context Engineering（上下文工程）**。

---

## Part I：为什么需要这个技能

### Meta 收购 Manus 的启示

Manus 这家 AI agent 公司在短时间内实现了惊人的成功：
- 8 个月内从发布到 1亿美元+收入
- 被 Meta 以 20亿美元收购
- 核心秘诀：**Context Engineering**

他们的工作模式与传统 AI agent 有本质区别——使用**持久化的 markdown 文件**来规划、跟踪进度和存储知识。

### 传统 AI Agent 的问题

Claude Code（和大多数 AI agent）面临以下问题：

| 问题 | 描述 |
|------|------|
| **Volatile memory** | TodoWrite 工具在上下文重置后消失 |
| **Goal drift** | 50+ 次工具调用后，原始目标被遗忘 |
| **Hidden errors** | 失败不被跟踪，重复犯同样的错误 |
| **Context stuffing** | 所有内容塞进上下文而非存储 |

### 核心洞察

> "Markdown 是我磁盘上的'工作记忆'。由于我迭代处理信息，且活动上下文有上限，Markdown 文件作为草稿纸，用于存储笔记、进度检查点、最终交付物的构建块。" — Manus AI

**关键点**：通过在每次决策前读取 `task_plan.md`，目标始终保持在注意力窗口中。这就是 Manus 如何处理约 50 次工具调用而不失去跟踪的方法。

---

## Part II：解决方案 — 3 文件模式

### 核心模式

对于每个复杂任务，创建 **三个文件**：

```
task_plan.md      → 跟踪阶段和进度
notes.md          → 存储研究和发现
[deliverable].md  → 最终输出
```

### 工作流程

```
1. 创建 task_plan.md，包含目标和阶段
2. 研究 → 保存到 notes.md → 更新 task_plan.md
3. 读取 notes.md → 创建交付物 → 更新 task_plan.md
4. 交付最终输出
```

**关键机制**：
- 每次重大决策前重新读取计划
- 目标始终保持在注意力窗口中
- 避免在长任务中失去方向

### 与传统方式的对比

| 方面 | 传统方式 | 3 文件模式 |
|------|----------|-----------|
| **记忆存储** | 上下文（易失） | 文件系统（持久） |
| **目标跟踪** | 逐渐遗忘 | 始终可见 |
| **错误处理** | 不被记录 | 持久化日志 |
| **上下文管理** | 塞满内容 | 存储+引用 |

---

## Part III：Manus 原则

这个技能实现了以下关键的上下文工程原则：

| 原则 | 实现方式 |
|------|----------|
| **Filesystem as memory** | 存储在文件中，而非上下文中 |
| **Attention manipulation** | 决策前重新阅读计划 |
| **Error persistence** | 计划文件中记录失败 |
| **Goal tracking** | 复选框显示进度 |
| **Append-only context** | 绝不修改历史 |

### 详细说明

#### 1. 文件系统作为记忆

- **问题**：上下文有上限，且在会话间丢失
- **解决方案**：将信息持久化到文件
- **好处**：信息永远可用，可追溯

#### 2. 注意力操控

- **问题**：AI 在长任务中容易偏离目标
- **解决方案**：每次决策前读取计划
- **好处**：目标始终在注意力窗口中

#### 3. 错误持久化

- **问题**：同样的错误重复出现
- **解决方案**：在计划文件中记录失败
- **好处**：可以从错误中学习

#### 4. 目标跟踪

- **问题**：不清楚已完成什么、还需要什么
- **解决方案**：复选框显示进度
- **好处**：一目了然地看到整体进度

#### 5. 仅追加上下文

- **问题**：修改历史会丢失重要信息
- **解决方案**：只追加新信息，不修改历史
- **好处**：保持完整的决策轨迹

---

## Part IV：安装与使用

### 安装方法

#### 方法一：直接克隆（推荐）

```bash
# 导航到 Claude Code skills 目录
cd ~/.claude/skills  # 或你的自定义 skills 路径

# 克隆这个 skill
git clone https://github.com/OthmanAdi/planning-with-files.git
```

#### 方法二：手动安装

1. 下载或复制 `planning-with-files` 文件夹
2. 放置到 Claude Code skills 目录：
   - macOS/Linux: `~/.claude/skills/`
   - Windows: `%USERPROFILE%\.claude\skills\`

### 验证安装

在 Claude Code 中，当满足以下条件时，skill 会自动激活：
- 开始复杂任务时
- 提到 "planning"、"organize" 或 "track progress" 时
- 要求结构化工作时

### 使用示例

**你**："Research the benefits of TypeScript and write a summary"

**Claude 创建：**

```markdown
# Task Plan: TypeScript Benefits Research

## Goal
Create a research summary on TypeScript benefits.

## Phases
- [x] Phase 1: Create plan ✓
- [ ] Phase 2: Research and gather sources (CURRENT)
- [ ] Phase 3: Synthesize findings
- [ ] Phase 4: Deliver summary

## Status
**Currently in Phase 2** - Searching for sources
```

然后继续每个阶段，在过程中更新文件。

---

## Part V：文件结构

```
planning-with-files/
├── SKILL.md        # 核心指令（Claude 读取）
├── reference.md    # Manus 原则深入探讨
├── examples.md     # 真实使用示例
└── README.md       # 本文档
```

### 核心文件说明

#### SKILL.md

Claude Code 读取的核心指令集，定义了：
- 何时激活技能
- 如何创建和管理文件
- 工作流程模式

#### reference.md

Manus 原则的深入探讨，包括：
- Context Engineering 详细解释
- 为什么要使用文件系统作为记忆
- 最佳实践和注意事项

#### examples.md

真实使用示例，包括：
- 多种场景的示例
- 最佳实践展示
- 常见问题和解决方案

---

## Part VI：适用场景

### 建议使用的情况

**适合使用此模式：**
- 多步骤任务（3+ 步骤）
- 研究任务
- 构建/创建项目
- 跨越多次工具调用的任务
- 需要组织的任何任务

### 不建议使用的情况

**可以跳过：**
- 简单问题
- 单文件编辑
- 快速查找

---

## Part VII：相关资源

### 项目资源

- **GitHub**: https://github.com/OthmanAdi/planning-with-files
- **作者**: Ahmad Othman Ammar Adi
- **许可证**: MIT

### 背景阅读

- [Meta 收购 Manus 新闻](https://techcrunch.com/2024/12/29/meta-just-bought-manus-an-ai-startup-everyone-has-been-talking-about/)
- [Context Engineering for AI Agents](https://manus.im/de/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus)
- [Claude Code 官方文档](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/skills)

### 相关项目

- **NOFX**（前面文档提到）: AI 交易系统，同样使用持久化规划
- **Obsidian Skills**: 本 vault 中的 Claude Code skills

### 学习路径

1. **理解原理**（本文档）
   - 阅读 Part I-III 理解核心概念
   - 阅读 reference.md 深入了解原则

2. **实践应用**（examples.md）
   - 从简单任务开始
   - 逐步应用到复杂任务

3. **内化为习惯**（长期）
   - 将 3 文件模式作为默认工作方式
   - 在所有复杂任务中使用

---

## Part VIII：在你的 vault 中应用

### 整合到 Obsidian 工作流

这个技能与你现有的 Obsidian vault 高度兼容：

#### 1. 任务规划

创建 `task_plan.md` 来跟踪复杂任务：

```markdown
# Task Plan: [任务名称]

## Goal
[任务目标]

## Phases
- [ ] Phase 1: [阶段1]
- [ ] Phase 2: [阶段2]
- [ ] Phase 3: [阶段3]

## Status
**Currently in Phase [X]**
```

#### 2. 研究笔记

创建 `notes.md` 来存储研究发现：

```markdown
# Notes: [研究主题]

## Sources
- [来源1]
- [来源2]

## Key Findings
### Finding 1
[描述]

### Finding 2
[描述]

## Questions
- [待解答问题]
```

#### 3. 进度跟踪

使用复选框跟踪进度：

```markdown
## Progress
- [x] Completed task 1
- [x] Completed task 2
- [ ] Current task 3
- [ ] Upcoming task 4
```

### 与 Claude Code 集成

当你使用 Claude Code 处理复杂任务时：
1. Claude 会自动创建 `task_plan.md`
2. 在 `notes.md` 中存储研究发现
3. 更新 `task_plan.md` 跟踪进度
4. 创建最终交付物

### Obsidian 技能配合

你已有的 Claude Code skills 可以与这个模式配合使用：

| 技能 | 配合使用场景 |
|------|--------------|
| obsidian-markdown | 创建和编辑规划文件 |
| obsidian-bases | 跟踪多个任务的进度 |
| json-canvas | 可视化任务关系和依赖 |

---

## Part IX：实践示例

### 示例 1：研究项目

**任务**：研究 AI 在金融领域的应用

**创建的文件**：

1. `task_plan.md`：
```markdown
# Task Plan: AI in Finance Research

## Goal
Create a comprehensive research summary on AI applications in finance.

## Phases
- [x] Phase 1: Create plan ✓
- [ ] Phase 2: Research AI applications in finance (CURRENT)
- [ ] Phase 3: Analyze use cases
- [ ] Phase 4: Identify trends
- [ ] Phase 5: Deliver summary

## Status
**Currently in Phase 2** - Searching for sources
```

2. `notes.md`：
```markdown
# Notes: AI in Finance Research

## Sources
- [Source 1]: https://example.com/article1
- [Source 2]: https://example.com/article2

## Key Findings
### Trading
- AI algorithms for stock trading
- Sentiment analysis for market prediction

### Risk Management
- Fraud detection systems
- Credit scoring models

## Questions
- What are the ethical considerations?
```

3. `ai-finance-summary.md`（最终交付物）

### 示例 2：项目开发

**任务**：开发一个 Python 脚本

**创建的文件**：

1. `task_plan.md`
2. `development-notes.md`
3. `script.py` 或 `script.py.md`

---

## Part X：常见问题

### Q1：这个技能与现有的 TodoWrite 有什么不同？

**TodoWrite**：
- 存储在上下文中
- 会话结束丢失
- 无法跟踪历史

**Planning with Files**：
- 持久化到文件系统
- 永远可用
- 完整的进度历史

### Q2：我需要手动创建这些文件吗？

不需要。Claude Code 会自动：
1. 检测复杂任务
2. 创建 `task_plan.md`
3. 在适当时创建 `notes.md`
4. 更新进度

你只需要开始复杂任务即可。

### Q3：文件存储在哪里？

默认存储在当前工作目录。你也可以指定特定位置：
- 项目根目录
- 专门的笔记文件夹
- 任何你喜欢的目录

### Q4：可以用于简单任务吗？

可以，但不建议。对于简单任务：
- 直接执行即可
- 不需要创建额外文件
- 避免过度工程

---

## 总结

### 核心要点

1. **Context Engineering 是关键**：使用持久化文件而非仅依赖上下文
2. **3 文件模式**：task_plan.md + notes.md + deliverable.md
3. **注意力操控**：每次决策前读取计划
4. **错误学习**：记录失败以便改进

### 行动建议

1. **立即尝试**：从下一个复杂任务开始使用这个模式
2. **内化习惯**：将 3 文件模式作为默认工作方式
3. **分享给他人**：帮助更多人提高 AI agent 使用效率

### 与现有工作的关系

这个技能与你 vault 中的其他内容高度相关：

| 相关内容 | 关联点 |
|----------|--------|
| Obsidian Skills | Claude Code skills 集成 |
| AI Trading 研究 | 可用于跟踪研究和策略开发 |
| 信息聚合系统 | 持久化规划和进度跟踪 |

---

> [!tip] 下一步
> 访问 https://github.com/OthmanAdi/planning-with-files 了解最新更新
> 阅读 examples.md 获取更多使用示例
> 开始在你的下一个复杂任务中使用这个模式

---

[!success] 文档创建完成
