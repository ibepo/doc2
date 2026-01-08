---
title: Obsidian Skills 说明
tags:
  - ai
  - obsidian
  - 技能
created: 2024-01-07
---

# Obsidian Skills 说明

本 vault 已集成三个 Claude Code 专用技能，用于增强 AI 与 Obsidian 的交互能力。

> [!info] 提示
> 这些技能会在你处理相应类型的文件时自动激活，无需手动指定。

## 01 obsidian-markdown

**文件类型**: `.md`

**功能**:
- 创建和编辑 Obsidian Flavored Markdown
- 支持 wikilinks: `[[Note Name]]`
- 支持 callouts: `> [!note]`
- 支持 embeds: `![[Other Note]]`
- 支持 frontmatter (YAML 属性)
- 支持标签、LaTeX 数学公式、Mermaid 图表

**适用场景**: 编写或编辑 Obsidian 笔记时

**本文档使用的示例**:
- Frontmatter 属性（文档顶部的 YAML 块）
- Callout 框（如上方的提示框）
- [[talkwithAI]] 链接到本文件夹的其他文档

## 02 obsidian-bases

**文件类型**: `.base`

**功能**:
- 创建数据库风格的笔记视图
- 支持多种视图类型: table, cards, list, map
- 支持高级过滤: `filters: { and: [], or: [], not: [] }`
- 支持公式计算: `formulas: { total: 'price * quantity' }`
- 支持属性分组和汇总

**适用场景**: 创建任务列表、阅读清单、项目管理等数据库视图时

**示例配置**:
```yaml
filters:
  and:
    - file.hasTag("obsidian")
    - 'file.ext == "md"'

formulas:
  days_old: '((now() - file.ctime) / 86400000).round(0)'

views:
  - type: table
    name: "技能文档"
    order:
      - file.name
      - created
```

## 03 json-canvas

**文件类型**: `.canvas`

**功能**:
- 创建无限画布文件
- 支持四种节点类型: text, file, link, group
- 支持节点连接: edges
- 支持颜色自定义: 预设 6 种颜色或 HEX 值
- 支持可视化布局: 思维导图、流程图、项目看板

**适用场景**: 创建可视化内容、思维导图、流程图或项目看板时

**典型结构**:
- Text 节点: 包含 Markdown 文本
- File 节点: 引用 vault 中的文件或图片
- Link 节点: 链接到外部网站
- Group 节点: 将其他节点分组，添加标签和背景

## 使用方法

当你在 Obsidian 中工作并需要 AI 协助时，只需提出需求，Claude Code 会根据文件类型自动选择合适的技能:

- 编辑 `.md` 文件 → 使用 obsidian-markdown
- 创建 `.base` 数据库 → 使用 obsidian-bases
- 制作 `.canvas` 画布 → 使用 json-canvas

无需显式指定技能名称。

## 实际示例

> [!tip] 实际应用
> 下面展示了本文档中使用的三种技能特性：

### 使用 obsidian-markdown

本文档实际使用了以下 Markdown 特性:

1. **Frontmatter**: 文档开头的 YAML 属性块
   ```yaml
   title: Obsidian Skills 说明
   tags: [ai, obsidian, 技能]
   ```

2. **Callout**: 如上方的提示框和技巧框

3. **Wikilinks**: 可以链接到其他文档，如 [[talkwithAI]]

4. **内联代码和代码块**: 展示各种配置示例

### 使用 obsidian-bases

可以创建一个 `SkillsIndex.base` 文件来索引本文件夹的所有文档:

```yaml
filters:
  and:
    - file.inFolder("docs/talkwithAI")
    - 'file.ext == "md"'

formulas:
  word_count: '(file.size / 5).round(0)'

views:
  - type: cards
    name: "文档库"
    order:
      - file.name
      - created
```

### 使用 json-canvas

可以创建一个 `SkillsOverview.canvas` 文件来可视化三个技能的关系:

```
节点布局:
[Markdown 技能] ───> [Bases 技能] ───> [Canvas 技能]
     ↓                   ↓                   ↓
  文本编辑          数据库管理          可视化设计
```

## 快速参考

| 技能 | 文件类型 | 主要用途 |
|------|----------|----------|
| obsidian-markdown | `.md` | 笔记编写、文档编辑 |
| obsidian-bases | `.base` | 数据库、任务管理、列表 |
| json-canvas | `.canvas` | 思维导图、流程图、看板 |

## 相关资源

- [Obsidian Flavored Markdown 官方文档](https://help.obsidian.md/obsidian-flavored-markdown)
- [Obsidian Bases 文档](https://help.obsidian.md/bases)
- [JSON Canvas 规范](https://jsoncanvas.org/)
