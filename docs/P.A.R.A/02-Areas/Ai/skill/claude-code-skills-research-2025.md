---
title: Claude Code Skills 研究报告 2025
tags:
  - ai
  - claude-code
  - skills
  - cloud-ide
  - open-source
created: 2025-01-07
related:
  - [[09-planning-with-files-Manus风格持久化规划.md]]
  - [[01-obsidian-skills说明.md]]
---

# Claude Code Skills 研究报告 2025

> [!info] 研究背景
> **研究日期**: 2025年1月7日
> **研究方法**: 使用 planning-with-files skill 进行持久化规划研究
> **目标**: 分析当前流行的 cloud code 和 open code 相关的 Claude Code skills

---

## Part I: Skills 生态系统概述

### 官方发布时间线

| 日期 | 事件 |
|------|------|
| 2025-10-16 | Claude Skills 正式发布 |
| 2025-10-18 | 社区仓库开始涌现 (obra/superpowers) |
| 2025-11-13 | Anthropic 发布 Skills Explained 指南 |

### Skills 架构原理

**渐进式披露架构 (Progressive Disclosure)**:

1. **元数据加载** (~100 tokens): 扫描可用 Skills 识别相关匹配
2. **完整指令** (<5k tokens): 当 Skill 适用时加载
3. **捆绑资源**: 文件和可执行代码仅在需要时加载

这种设计允许多个 Skills 保持可用而不会压倒上下文窗口。

---

## Part II: 核心仓库分析

### 1. awesome-claude-skills (精选列表)

> [!quote] 来源
> **仓库**: [travisvn/awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills)
> **类型**: 精选列表
> **Stars**: 活跃维护

**官方 Skills**:

| Skill | 功能 |
|-------|------|
| `docx` | Word 文档创建、编辑、修订跟踪 |
| `pdf` | PDF 提取、创建、合并、拆分 |
| `pptx` | PowerPoint 演示文稿自动化 |
| `xlsx` | Excel 电子表格分析 |

**设计类 Skills**:
- `algorithmic-art` - p5.js 生成艺术
- `canvas-design` - PNG/PDF 视觉设计
- `frontend-design` - React & Tailwind 设计指南

**开发类 Skills**:
- `mcp-builder` - MCP 服务器构建指南
- `webapp-testing` - Playwright UI 测试
- `artifacts-builder` - HTML artifacts 构建

**社区精选**:
- `obra/superpowers` - 20+ 战斗测试的核心 skills
  - TDD、调试、协作模式
  - `/brainstorm`, `/write-plan`, `/execute-plan` 命令

---

### 2. levnikolaevich/claude-code-skills (29个生产级 Skills)

> [!quote] 来源
> **仓库**: [levnikolaevich/claude-code-skills](https://github.com/levnikolaevich/claude-code-skills)
> **特色**: 完整 Agile 工作流自动化
> **集成**: Linear (项目管理平台)

**插件结构**:

| 插件 | Skills 数量 | 功能 |
|------|-------------|------|
| **docs** | 10 | 文档自动化 |
| **planning** | 4 | Epic/Story 分解 |
| **execution** | 19 | 从任务规划到 Done |

**核心特性**:

- **Orchestrator-Worker 模式**: 自动化复杂工作流
- **Risk-Based Testing**: E2E 优先 (2-5), Integration (3-8), Unit (5-15)
- **Standards First**: 行业标准优先于 KISS/YAGNI
- **Linear 集成**: 无缝任务管理和跟踪

**文档系统 (ln-110 系列)**:
```
ln-110-documents-pipeline (编排器)
├── ln-111-root-docs-creator (根文档)
├── ln-112-reference-docs-creator (参考文档)
├── ln-113-tasks-docs-creator (任务管理)
├── ln-114-project-docs-creator (项目文档)
├── ln-115-presentation-creator (演示文稿)
└── ln-116-test-docs-creator (测试文档)
```

**规划系统 (ln-200 系列)**:
```
ln-200-scope-decomposer (顶层编排器)
├── ln-210-epic-coordinator (Epic 协调器)
└── ln-220-story-coordinator (Story 协调器)
    ├── ln-221-standards-researcher (标准研究)
    ├── ln-222-story-creator (Story 创建)
    └── ln-223-story-replanner (Story 重规划)
```

**执行管道 (ln-300 系列)**:
```
ln-300-story-pipeline (完整管道)
├── ln-310-story-decomposer (任务分解)
├── ln-320-story-validator (Story 验证)
├── ln-330-story-executor (Story 执行)
├── ln-340-story-quality-gate (质量门控)
└── ln-350-story-test-planner (测试规划)
```

---

### 3. mhattingpete/claude-skills-marketplace

> [!quote] 来源
> **仓库**: [mhattingpete/claude-skills-marketplace](https://github.com/mhattingpete/claude-skills-marketplace)
> **核心创新**: Execution Runtime (90%+ Token 节省)

**四大插件**:

#### Engineering Workflow Plugin
- `feature-planning` - 功能规划和分解
- `git-pushing` - 自动提交和推送
- `test-fixing` - 系统化测试修复
- `review-implementing` - 代码审查实施

#### Visual Documentation Plugin
- `architecture-diagram-creator` - 架构图
- `flowchart-creator` - 流程图
- `dashboard-creator` - 仪表板
- `technical-doc-creator` - 技术文档
- `timeline-creator` - 时间线

#### Productivity Skills Plugin
- `code-auditor` - 代码质量审计
- `codebase-documenter` - 代码库文档生成
- `conversation-analyzer` - 使用模式分析
- `project-bootstrapper` - 项目初始化

#### Code Operations Plugin
- `code-execution` - 本地 Python 执行 (NEW!)
- `code-transfer` - 代码传输 (行级精度)
- `code-refactor` - 批量重构
- `file-operations` - 文件分析

**Execution Runtime 突破**:

| 场景 | 传统方式 | Execution 模式 | 节省 |
|------|----------|----------------|------|
| 重命名 50 个文件中的函数 | ~25,000 tokens | ~600 tokens | 97.6% |
| 批量重构 100 个文件 | ~100,000 tokens | ~1,000 tokens | 99% |

**安装方式**:
```bash
# 安装完整插件
/plugin marketplace add mhattingpete/claude-skills-marketplace

# 安装单个插件
/plugin marketplace add mhattingpete/claude-skills-marketplace/engineering-workflow-plugin
```

---

## Part III: Skills vs 其他工具对比

### 功能对比表

| 特性 | Skills | MCP | Prompts | Projects |
|------|--------|-----|---------|----------|
| **目的** | 任务专业知识 | 外部数据/API | 一次性指令 | 工作区持久知识 |
| **可移植性** | 通用格式 | 需服务器配置 | 不可复用 | 工作区特定 |
| **代码执行** | 可包含脚本 | 提供工具 | 无 | 无 |
| **Token 效率** | 按需加载 | 变化 | 始终在上下文 | 始终在上下文 |
| **版本控制** | Git 友好 | 需配置 | 无 | 无 |
| **组合性** | 多技能叠加 | 工具链组合 | 手动组合 | 无 |

### 何时使用 Skills

> [!tip] 决策矩阵
> **使用 Skills 当**:
> - 能力应该对所有 Claude 实例可用
> - 需要可移植的专业知识
> - 发现自己重复输入相同提示
>
> **使用 Subagents 当**:
> - 需要具有独立工作流的独立代理
> - 需要特定的权限和工具访问
>
> **结合使用**: Subagents 可以利用 Skills 获得专业知识

---

## Part IV: IDE 集成

### VS Code 集成

**官方文档**: [Use Claude Code in VS Code](https://code.claude.com/docs/en/vs-code)

**功能**:
- 内联差异查看 (Inline diffs)
- @mentions 上下文共享
- 计划审查模式 (Plan review mode)
- 键盘快捷键支持
- 兼容流行分支: Cursor, Windsurf

### JetBrains 集成

**官方文档**: [JetBrains IDEs - Claude Code Docs](https://code.claude.com/docs/en/jetbrains)

**插件**: [Claude Code GUI](https://plugins.jetbrains.com/plugin/29342-claude-code-gui)

**功能**:
- 交互式差异查看
- 选择上下文共享
- AI 代码辅助 (`Ctrl+Alt+K` / `Cmd+Alt+K`)
- 智能建议

---

## Part V: Cloud IDE 和 GitHub 集成

### Claude Code Web 版

**官方文档**: [Claude Code on the web](https://claude.com/blog/claude-code-on-the-web)

**功能**:
- **GitHub 仓库连接**: 直接连接并处理仓库
- **云端 IDE**: 无需终端即可启动编码会话
- **浏览器集成**: 纯 Web 界面

### GitHub/开源工作流 Skills

**git-workflow Skill**:
- Git 自动化、分支管理
- Conventional commit messages
- PR 处理和审查

**OSS Contribution Workflows**:
- PR 管理和自动审查
- Issue 分类和清理
- 自动生成 commit messages
- Git co-authorship 标记

**最佳实践** (来自 [Anthropic 官方指南](https://www.anthropic.com/engineering/claude-code-best-practices)):
1. 从广泛问题开始，然后缩小到具体领域
2. 学习编码约定和模式
3. 创建项目词汇表
4. 对复杂更改使用计划模式

---

## Part VI: 安装和使用

### 安装方式

**方法 1: Plugin Marketplace (推荐)**
```bash
# 从 marketplace 安装
/plugin marketplace add <repo>/<plugin>

# 示例
/plugin marketplace add mhattingpete/claude-skills-marketplace
/plugin marketplace add levnikolaevich/claude-code-skills
```

**方法 2: 直接插件**
```bash
/plugin add <repo>
```

**方法 3: Git Clone**
```bash
# macOS/Linux
git clone <repo> ~/.claude/skills

# Windows
git clone <repo> %USERPROFILE%\.claude\skills
```

### 创建自定义 Skill

**方法 1: 使用 skill-creator (推荐)**
```bash
# 启用 skill-creator skill
# 让 Claude: "Use the skill-creator to help me build a skill for [your task]"
```

**方法 2: 手动创建**
```
my-skill/
├── SKILL.md          # 主 skill 文件
├── scripts/          # 可执行脚本
└── resources/        # 支持文件
```

**SKILL.md 模板**:
```markdown
---
name: my-skill
description: 简洁描述用于技能发现
---

# Skill 标题

简要概述这个 skill 的作用。

## 何时使用
- 用户说 X 时
- 用户提到 Y 时
- 上下文包含 Z 时

## 说明
逐步说明 Claude 应遵循的指令...
```

### 最佳实践

1. **保持描述简洁**: frontmatter 描述用于技能发现
2. **使用清晰的指令**: 像为人类协作者编写一样
3. **包含示例**: 在 SKILL.md 中展示具体示例
4. **版本控制**: 使用 git 标签进行版本管理
5. **记录依赖**: 列出任何先决条件或必需的包
6. **彻底测试**: 验证 skill 在不同场景下工作

---

## Part VII: 安全性考虑

> [!warning] 重要
> Skills 可以在 Claude 环境中执行任意代码。只从可信来源安装 skills！

### 安全指南

**审查 Skills**:
- 只从可信来源安装 skills
- 启用前审查 SKILL.md 和所有脚本
- 对请求敏感数据访问的 skills 保持谨慎
- 在部署到生产或企业环境前仔细审计

### 安全关注点

- **恶意 skills** 可能引入漏洞或启用数据泄露
- **提示注入攻击** 可能通过受损的 skills 放大
- **沙箱限制** - 在企业部署前了解安全模型

---

## Part VIII: 资源汇总

### 官方资源
- [Agent Skills Documentation](https://code.claude.com/docs/en/skills)
- [Claude Skills Official Announcement](https://claude.com/blog/skills)
- [Claude Code Best Practices](https://www.anthropic.com/engineering/claude-code-best-practices)

### GitHub 仓库
- [awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills) - 精选列表
- [claude-code-skills](https://github.com/levnikolaevich/claude-code-skills) - 29个生产级 skills
- [claude-skills-marketplace](https://github.com/mhattingpete/claude-skills-marketplace) - 软件工程工作流
- [anthropics/skills](https://github.com/anthropics/skills) - 官方公开仓库

### 文章和指南
- [5 Best Claude Skills Open Source Projects 2025](https://www.devkit.best/blog/mdx/top-claude-skills-open-source-projects-2025)
- [Claude Skills vs Prompt Libraries (2025)](https://skywork.ai/blog/ai-agent/claude-skills-vs-prompt-libraries-2025-comparison/)
- [Claude Agent Skills: A First Principles Deep Dive](https://leehanchung.github.io/blogs/2025/10/26/claude-skills-deep-dive/)

### 社区
- [Claude Code Discussions](https://github.com/orgs/anthropics/discussions)
- [r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/) - Subreddit

---

## Part IX: 总结与建议

### 核心发现

1. **生态系统快速成长**: 2025年10月官方发布后，社区迅速响应
2. **渐进式披露架构**: 按需加载设计保持 token 效率
3. **多样化应用**: 从文档处理到完整 Agile 工作流
4. **IDE 深度集成**: VS Code 和 JetBrains 官方支持
5. **开源友好**: 专为开源贡献优化的工作流

### 安装建议

**新手**:
1. 从 [awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills) 开始
2. 尝试官方 skills (docx, pdf, pptx, xlsx)
3. 探索 obra/superpowers 核心库

**Agile 团队**:
1. 安装 [levnikolaevich/claude-code-skills](https://github.com/levnikolaevich/claude-code-skills)
2. 配置 Linear 集成
3. 采用 Orchestrator-Worker 模式

**软件工程师**:
1. 安装 [mhattingpete/claude-skills-marketplace](https://github.com/mhattingpete/claude-skills-marketplace)
2. 启用 Execution Runtime (90%+ token 节省)
3. 使用 Git 自动化 skills

**开源贡献者**:
1. 配置 GitHub 集成
2. 使用 git-workflow 和 OSS Contribution skills
3. 启用 co-authorship 标记

### 下一步行动

1. **立即尝试**: 从下一个复杂任务开始使用 skills
2. **内化习惯**: 将 3 文件模式 (planning-with-files) 作为默认工作方式
3. **分享知识**: 帮助团队提高 AI agent 使用效率
4. **贡献社区**: 创建和分享自定义 skills

---

> [!success] 研究完成
> 本研究报告使用 `planning-with-files` skill 的持久化规划方法完成。
> **研究文件**:
> - `task_plan.md` - 研究规划和进度跟踪
> - `notes.md` - 研究笔记和发现
> - `claude-code-skills-research-2025.md` - 本报告

---

**Sources**:
- [travisvn/awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills)
- [levnikolaevich/claude-code-skills](https://github.com/levnikolaevich/claude-code-skills)
- [mhattingpete/claude-skills-marketplace](https://github.com/mhattingpete/claude-skills-marketplace)
- [Claude Skills Official Announcement](https://claude.com/blog/skills)
- [Claude Code on the web](https://claude.com/blog/claude-code-on-the-web)
- [Claude Code Best Practices](https://www.anthropic.com/engineering/claude-code-best-practices)
- [5 Best Claude Skills Open Source Projects 2025](https://www.devkit.best/blog/mdx/top-claude-skills-open-source-projects-2025)
