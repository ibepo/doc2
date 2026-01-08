---
title: Claude Code Skills 总表
tags:
  - ai
  - claude-code
  - skills
  - inventory
created: 2025-01-07
related:
  - [[01-obsidian-skills说明.md]]
  - [[05-planning-with-files-Manus风格持久化规划.md]]
---

# Claude Code Skills 总表

> [!warning] 重要备份文档
> **目的**: 记录所有已安装的 Claude Code Skills，防止误删后无法找回
> **更新日期**: 2025-01-07
> **总数量**: 32 个 Skills

---

## Part I: 全局 Skills (~/.claude/skills/)

**安装位置**: `/Users/ibepo/.claude/skills/`

### 官方文档处理类 (4个)

| Skill | 描述 | 来源 |
|-------|------|------|
| **docx** | Word 文档创建、编辑、修订跟踪、评论、格式保留 | [anthropics/skills](https://github.com/anthropics/skills) |
| **pdf** | PDF 文本/表格提取、创建、合并、拆分、表单处理 | [anthropics/skills](https://github.com/anthropics/skills) |
| **pptx** | PowerPoint 演示文稿创建、编辑、布局、备注 | [anthropics/skills](https://github.com/anthropics/skills) |
| **xlsx** | Excel 电子表格、公式、格式化、数据分析、可视化 | [anthropics/skills](https://github.com/anthropics/skills) |

### Engineering Workflow Plugin (4个)

| Skill | 描述 | 来源 |
|-------|------|------|
| **feature-planning** | 功能请求分解为详细可执行计划，明确任务 | [mhattingpete/claude-skills-marketplace](https://github.com/mhattingpete/claude-skills-marketplace) |
| **git-pushing** | 自动暂存、提交(Conventional Commits)、推送 | [mhattingpete/claude-skills-marketplace](https://github.com/mhattingpete/claude-skills-marketplace) |
| **test-fixing** | 系统化识别和修复失败测试，智能错误分组 | [mhattingpete/claude-skills-marketplace](https://github.com/mhattingpete/claude-skills-marketplace) |
| **review-implementing** | 处理和实施代码审查反馈，todo 跟踪 | [mhattingpete/claude-skills-marketplace](https://github.com/mhattingpete/claude-skills-marketplace) |

### Code Operations Plugin (4个)

| Skill | 描述 | 来源 |
|-------|------|------|
| **code-execution** | 本地 Python 执行，90%+ Token 节省 (批量操作) | [mhattingpete/claude-skills-marketplace](https://github.com/mhattingpete/claude-skills-marketplace) |
| **code-transfer** | 代码传输，行级精度插入 | [mhattingpete/claude-skills-marketplace](https://github.com/mhattingpete/claude-skills-marketplace) |
| **code-refactor** | 批量代码重构，10+ 文件自动切换执行模式 | [mhattingpete/claude-skills-marketplace](https://github.com/mhattingpete/claude-skills-marketplace) |
| **file-operations** | 文件分析和详细元数据获取（不修改） | [mhattingpete/claude-skills-marketplace](https://github.com/mhattingpete/claude-skills-marketplace) |

### Visual Documentation Plugin (5个)

| Skill | 描述 | 来源 |
|-------|------|------|
| **architecture-diagram-creator** | 创建综合 HTML 架构图（数据流、业务目标、技术架构） | [mhattingpete/claude-skills-marketplace](https://github.com/mhattingpete/claude-skills-marketplace) |
| **flowchart-creator** | 创建 HTML 流程图和决策树 | [mhattingpete/claude-skills-marketplace](https://github.com/mhattingpete/claude-skills-marketplace) |
| **dashboard-creator** | 创建专业 HTML 仪表板（KPI、图表、进度指示器） | [mhattingpete/claude-skills-marketplace](https://github.com/mhattingpete/claude-skills-marketplace) |
| **technical-doc-creator** | 创建综合 HTML 技术文档（代码块、API 工作流） | [mhattingpete/claude-skills-marketplace](https://github.com/mhattingpete/claude-skills-marketplace) |
| **timeline-creator** | 创建美观 HTML 时间线和项目路线图 | [mhattingpete/claude-skills-marketplace](https://github.com/mhattingpete/claude-skills-marketplace) |

### Productivity Skills Plugin (5个)

| Skill | 描述 | 来源 |
|-------|------|------|
| **code-auditor** | 代码库全面分析（架构、质量、安全、性能、测试、可维护性） | [mhattingpete/claude-skills-marketplace](https://github.com/mhattingpete/claude-skills-marketplace) |
| **codebase-documenter** | 生成综合文档（架构、关键组件、数据流、开发指南） | [mhattingpete/claude-skills-marketplace](https://github.com/mhattingpete/claude-skills-marketplace) |
| **conversation-analyzer** | 分析 Claude Code 对话历史，识别模式和优化机会 | [mhattingpete/claude-skills-marketplace](https://github.com/mhattingpete/claude-skills-marketplace) |
| **project-bootstrapper** | 设置新项目或改进现有项目（最佳实践、工具、文档、工作流） | [mhattingpete/claude-skills-marketplace](https://github.com/mhattingpete/claude-skills-marketplace) |
| **terminal-title** | 自动更新终端窗口标题以反映当前高级任务，便于管理多个 Claude Code 终端 | [bluzername/claude-code-terminal-title](https://github.com/bluzername/claude-code-terminal-title) |

### 规划相关 (1个)

| Skill | 描述 | 来源 |
|-------|------|------|
| **planning-with-files** | Manus 风格持久化规划，使用 markdown 文件进行任务规划和进度跟踪 | [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) |

### n8n 相关 (7个)

| Skill | 描述 | 来源 |
|-------|------|------|
| **n8n-code-javascript** | n8n Code 节点中编写 JavaScript ($input/$json/$node 语法) | 用户安装 |
| **n8n-code-python** | n8n Code 节点中编写 Python (_input/_json/_node 语法) | 用户安装 |
| **n8n-expression-syntax** | 验证 n8n 表达式语法 ({{}} 语法) | 用户安装 |
| **n8n-mcp-tools-expert** | n8n-mcp MCP 工具使用专家指南 | 用户安装 |
| **n8n-node-configuration** | 操作感知的 n8n 节点配置指南 | 用户安装 |
| **n8n-validation-expert** | 解释 n8n 验证错误并指导修复 | 用户安装 |
| **n8n-workflow-patterns** | 真实 n8n 工作流中的架构模式 | 用户安装 |

---

## Part II: 项目 Skills (.claude/skills/)

**项目路径**: `/Users/ibepo/Documents/GitHub/doc2/`
**安装位置**: `.claude/skills/`

### Obsidian 相关 (3个)

| Skill | 描述 | 类型 |
|-------|------|------|
| **obsidian-markdown** | 创建和编辑 Obsidian Flavored Markdown (wikilinks, callouts, embeds, frontmatter) | Project |
| **obsidian-bases** | 创建和编辑 Obsidian Bases (.base 文件) - 数据库视图、过滤器、公式 | Project |
| **json-canvas** | 创建和编辑 JSON Canvas 文件 (.canvas) - 节点、边、组、连接 | Project |

---

## Part III: 安装来源汇总

### GitHub 仓库

| 仓库 | 用途 | 安装的 Skills |
|------|------|---------------|
| [anthropics/skills](https://github.com/anthropics/skills) | 官方 skills | docx, pdf, pptx, xlsx |
| [mhattingpete/claude-skills-marketplace](https://github.com/mhattingpete/claude-skills-marketplace) | 软件工程工作流 | 17 个工程相关 skills |
| [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | 持久化规划 | planning-with-files |
| [bluzername/claude-code-terminal-title](https://github.com/bluzername/claude-code-terminal-title) | 终端标题管理 | terminal-title |

### 本地创建

| 来源 | Skills |
|------|--------|
| 本 vault 项目 | obsidian-markdown, obsidian-bases, json-canvas |
| 用户自定义 | n8n 相关 7 个 skills |

---

## Part IV: 快速恢复指南

### 恢复全局 Skills

```bash
# 1. 官方文档处理 skills
cd ~/.claude/skills
git clone https://github.com/anthropics/skills.git
mv skills/skills/docx .
mv skills/skills/pdf .
mv skills/skills/pptx .
mv skills/skills/xlsx .
rm -rf skills

# 2. Marketplace skills
git clone https://github.com/mhattingpete/claude-skills-marketplace.git
cd claude-skills-marketplace
cp -r engineering-workflow-plugin/skills/* ~/.claude/skills/
cp -r code-operations-plugin/skills/* ~/.claude/skills/
cp -r visual-documentation-plugin/skills/* ~/.claude/skills/
cp -r productivity-skills-plugin/skills/* ~/.claude/skills/

# 3. Planning with files
git clone https://github.com/OthmanAdi/planning-with-files.git

# 4. Terminal title
cd /tmp && curl -L -o terminal-title.skill https://github.com/bluzername/claude-code-terminal-title/raw/main/terminal-title.skill
cd ~/.claude/skills/ && unzip /tmp/terminal-title.skill
chmod +x ~/.claude/skills/terminal-title/scripts/set_title.sh
rm /tmp/terminal-title.skill
```

### 恢复项目 Skills

```bash
# 项目 skills 位于 .claude/skills/ 目录
# 如果误删，需要从 obsidian skills 相关文档重建
# 参考: 01-obsidian-skills说明.md
```

---

## Part V: 统计摘要

### 按类型分类

| 类型 | 数量 | Skills |
|------|------|--------|
| **官方文档处理** | 4 | docx, pdf, pptx, xlsx |
| **工程工作流** | 4 | feature-planning, git-pushing, test-fixing, review-implementing |
| **代码操作** | 4 | code-execution, code-transfer, code-refactor, file-operations |
| **可视化文档** | 5 | architecture-diagram-creator, flowchart-creator, dashboard-creator, technical-doc-creator, timeline-creator |
| **生产力** | 5 | code-auditor, codebase-documenter, conversation-analyzer, project-bootstrapper, terminal-title |
| **规划** | 1 | planning-with-files |
| **n8n 专用** | 7 | n8n-code-javascript, n8n-code-python, n8n-expression-syntax, n8n-mcp-tools-expert, n8n-node-configuration, n8n-validation-expert, n8n-workflow-patterns |
| **Obsidian** | 3 | obsidian-markdown, obsidian-bases, json-canvas |
| **总计** | **32** | |

### 按安装位置分类

| 位置 | 数量 |
|------|------|
| **全局** (~/.claude/skills/) | 30 |
| **项目** (.claude/skills/) | 3 |

---

## Part VI: 维护建议

### 定期更新

```bash
# 更新官方 skills
cd ~/.claude/skills/docx && git pull
cd ../pdf && git pull
cd ../pptx && git pull
cd ../xlsx && git pull

# 更新 marketplace
cd ~/.claude/skills/claude-skills-marketplace && git pull
# 重新复制 skills...

# 更新 planning-with-files
cd ~/.claude/skills/planning-with-files && git pull
```

### 备份建议

1. **定期备份** `~/.claude/skills/` 目录
2. **版本控制** 将自定义 skills 放入 Git
3. **文档更新** 每次安装/删除 skills 后更新本文档

---

> [!success] 文档状态
> **创建日期**: 2025-01-07
> **最后更新**: 2025-01-07
> **下次审查**: 需要时更新

---

**相关文档**:
- [[01-obsidian-skills说明.md]] - Obsidian Skills 使用说明
- [[05-planning-with-files-Manus风格持久化规划.md]] - Planning with Files 详解
