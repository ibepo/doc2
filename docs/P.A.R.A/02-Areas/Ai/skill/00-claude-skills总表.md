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
> **更新日期**: 2026-01-12
> **总数量**: 52 个 Skills (+20 新增)

---

## Part I: 全局 Skills (~/.claude/skills/)

**安装位置**: `/Users/ibepo/.claude/skills/`

### 🆕 AI 营销与内容类 (7个) - [新增]

| Skill | 描述 | 来源 |
|-------|------|------|
| **ai-readability-audit** | AI网站可读性审计，模拟AI爬虫视角检查网站结构 | 用户安装 |
| **cold-email-personalizer** | 个性化冷邮件生成，提高邮件打开率和回复率 | 用户安装 |
| **ecommerce-support** | AI电商客服助手，支持订单查询、商品推荐、工单处理 | 用户安装 |
| **email-assistant** | AI智能邮件助手，分析邮件内容生成摘要和回复建议 | 用户安装 |
| **influencer-evaluator** | Instagram/YouTube/TikTok网红账号数据评估和综合评分 | 用户安装 |
| **linkedin-post-creator** | 基于品牌调性生成高质量LinkedIn帖子，支持多轮反馈 | 用户安装 |
| **seo-analyzer** | 网站SEO状态分析，检查页面元素、技术指标、内容质量 | 用户安装 |

### 🆕 社交媒体与视频类 (6个) - [新增]

| Skill | 描述 | 来源 |
|-------|------|------|
| **competitor-price-monitor** | 竞品网站价格变动监控，自动对比历史价格 | 用户安装 |
| **competitor-research** | 自动化竞品全网调研，生成结构化竞品分析报告 | 用户安装 |
| **social-trend-monitor** | Reddit、Instagram、TikTok等社交平台热门趋势监控 | 用户安装 |
| **video-creator** | AI短视频创作与多平台发布（即梦MCP + Playwright MCP） | 用户安装 |
| **viral-post-creator** | AI生成病毒式社交媒体帖子（即梦MCP + Playwright MCP） | 用户安装 |
| **youtube-video-analyzer** | YouTube视频内容分析，自动提取字幕、生成结构化摘要 | 用户安装 |

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

### 🆕 地理内容优化类 (1个) - [新增]

| Skill | 描述 | 来源 |
|-------|------|------|
| **geo-content-optimizer** | GEO内容优化，让文章不仅被Google收录，还能被AI引用 | 用户安装 |

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

### 🆕 研究与图解类 (2个) - [新增]

| Skill | 描述 | 来源 |
|-------|------|------|
| **notebooklm** | 查询Google NotebookLM笔记本，获取源引支持的答案 | 用户安装 |
| **research-to-diagram** | 深度调研主题并自动生成知识关系图谱PDF | 用户安装 |

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

### 🆕 开发工具类 (1个) - [新增]

| Skill | 描述 | 类型 |
|-------|------|------|
| **skill-creator** | 创建和管理 Claude Code 技能的自定义工具 | Project |

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
| 本 vault 项目 | obsidian-markdown, obsidian-bases, json-canvas, skill-creator |
| 用户自定义 | n8n 相关 7 个 skills + AI营销内容 14 个技能 |

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
| **AI营销与内容** | 7 | ai-readability-audit, cold-email-personalizer, ecommerce-support, email-assistant, influencer-evaluator, linkedin-post-creator, seo-analyzer |
| **社交媒体与视频** | 6 | competitor-price-monitor, competitor-research, social-trend-monitor, video-creator, viral-post-creator, youtube-video-analyzer |
| **官方文档处理** | 4 | docx, pdf, pptx, xlsx |
| **工程工作流** | 4 | feature-planning, git-pushing, test-fixing, review-implementing |
| **代码操作** | 4 | code-execution, code-transfer, code-refactor, file-operations |
| **可视化文档** | 5 | architecture-diagram-creator, flowchart-creator, dashboard-creator, technical-doc-creator, timeline-creator |
| **生产力** | 5 | code-auditor, codebase-documenter, conversation-analyzer, project-bootstrapper, terminal-title |
| **地理内容优化** | 1 | geo-content-optimizer |
| **规划** | 1 | planning-with-files |
| **研究与图解** | 2 | notebooklm, research-to-diagram |
| **n8n 专用** | 7 | n8n-code-javascript, n8n-code-python, n8n-expression-syntax, n8n-mcp-tools-expert, n8n-node-configuration, n8n-validation-expert, n8n-workflow-patterns |
| **Obsidian** | 3 | obsidian-markdown, obsidian-bases, json-canvas |
| **开发工具** | 1 | skill-creator |
| **总计** | **52** | |

### 按安装位置分类

| 位置 | 数量 |
|------|------|
| **全局** (~/.claude/skills/) | 49 |
| **项目** (.claude/skills/) | 3 |

### 按时间分类

| 时期 | 数量 | 说明 |
|------|------|------|
| **原有技能** | 32 | 2025年1月安装 |
| **新增技能** | 20 | 2026年1月新增 |
| **总计** | **52** | |

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
> **最后更新**: 2026-01-12
> **下次审查**: 需要时更新

### 📈 技能增长记录
- **2025-01-07**: 初始安装 32 个技能
- **2026-01-12**: 新增 20 个技能，总计 52 个
- **增长率**: +62.5%

### 🆕 新增技能详情 (2026-01-12)

#### AI营销与内容 (7个)
- ai-readability-audit: AI网站可读性审计
- cold-email-personalizer: 个性化冷邮件生成
- ecommerce-support: AI电商客服助手
- email-assistant: AI智能邮件助手
- influencer-evaluator: 网红账号数据评估
- linkedin-post-creator: LinkedIn帖子生成
- seo-analyzer: 网站SEO分析

#### 社交媒体与视频 (6个)
- competitor-price-monitor: 竞品价格监控
- competitor-research: 竞品调研分析
- social-trend-monitor: 社交趋势监控
- video-creator: AI短视频创作
- viral-post-creator: 病毒式帖子生成
- youtube-video-analyzer: YouTube视频分析

#### 其他专业工具 (7个)
- geo-content-optimizer: 地理内容优化
- notebooklm: Google NotebookLM集成
- research-to-diagram: 研究图谱生成
- skill-creator: 技能创建工具
- 其他n8n技能优化

---

**相关文档**:
- [[01-obsidian-skills说明.md]] - Obsidian Skills 使用说明
- [[05-planning-with-files-Manus风格持久化规划.md]] - Planning with Files 详解
