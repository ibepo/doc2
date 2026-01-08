# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is an **Obsidian vault** - a personal knowledge management system using the PARA (Projects, Areas, Resources, Archives) organizational method. The repository contains:

- Technical documentation and notes across multiple domains
- Programming language references (JavaScript, Python, C/C++, React, Vue, etc.)
- Linux system administration notes (Arch Linux, Ubuntu)
- AI-related research and experimentation logs
- Project-specific documentation (e.g., system security analysis)

## Directory Structure

```
doc2/
├── docs/                          # Main vault root
│   └── P.A.R.A/                   # PARA method organization
│       ├── 01-Projects/           # Active projects with clear timelines
│       │   └── ts/                # China Technology Exchange analysis
│       ├── 02-Areas/              # Ongoing responsibilities (no end date)
│       │   ├── Ai/                # AI-related areas
│       │   ├── linux/             # Linux system administration
│       │   ├── talkwithAI/        # AI interaction experiments
│       │   └── [other areas]
│       ├── 03-Resources/          # Reference materials, tutorials
│       │   └── language/          # Programming language references
│       └── 04-Archives/           # Completed/inactive items
├── .claude/                       # Claude Code configuration
│   ├── skills/                    # Custom skills for Obsidian files
│   ├── hooks/                     # Shell scripts for events
│   └── settings.local.json        # Claude permissions
├── 02-areas/                      # Non-vault working directory
└── .obsidian/                     # Obsidian app configuration
```

## PARA Method Context

When working with this vault:

- **Projects** (`01-Projects/`): Active work with clear goals and end dates
- **Areas** (`02-Areas/`): Ongoing responsibilities with no fixed timeline
- **Resources** (`03-Resources/`): Reference materials for future use
- **Archives** (`04-Archives/`): Completed or inactive items

## Claude Code Skills

This vault includes three specialized skills that automatically activate based on file type:

### obsidian-markdown (`.md` files)
- Use for editing Obsidian Flavored Markdown
- Supports wikilinks `[[Note Name]]`, callouts `> [!note]`, embeds `![[Note]]`
- Supports frontmatter (YAML), tags, LaTeX math, Mermaid diagrams
- Reference: `.claude/skills/obsidian-markdown/`

### obsidian-bases (`.base` files)
- Use for creating database-style views
- Supports filters, formulas, grouping, and multiple view types (table, cards, list)
- Reference: `.claude/skills/obsidian-bases/`

### json-canvas (`.canvas` files)
- **Critical**: Use exact field names from JSON Canvas Spec 1.0
- Text nodes: Use `text` field (NOT `content`)
- Edges: Use `fromNode`/`toNode` fields (NOT `from`/`to`)
- Node types: `text`, `file`, `link`, `group`
- Reference: `.claude/skills/json-canvas/`
- Full spec: https://jsoncanvas.org/spec/1.0/

> **Warning**: Incorrect field names in `.canvas` files will cause silent failure (empty canvas in Obsidian)

## File Location Guidelines

When creating or moving files:

1. **Project-specific work** → `docs/P.A.R.A/01-Projects/[project-name]/`
2. **Ongoing area documentation** → `docs/P.A.R.A/02-Areas/[area-name]/`
3. **Reference materials** → `docs/P.A.R.A/03-Resources/[category]/`
4. **Archived content** → `docs/P.A.R.A/04-Archives/`

Do NOT create files in the repository root (`/Users/ibepo/Documents/GitHub/doc2/`). Use the `02-areas/` subdirectory for non-vault working files if needed.

## Obsidian Configuration

The vault uses Obsidian-specific configurations:

- Vim mode keybindings: `.obsidian.vimrc` (jk to escape, hjkl navigation with soft wrapping)
- Plugins: See `.obsidian/community-plugins.json` and `.obsidian/plugins/`
- Workspace: See `.obsidian/workspace.json`

## Hooks Configuration

Shell scripts in `.claude/hooks/` provide audio feedback:

- `user-prompt-submit-hook`: Plays sound after user input
- `model-requests-approval-hook`: Plays sound when AI asks for approval
- `session-end-hook`: Two beeps when session ends

These use macOS system sounds via `afplay`.

## Permissions

Claude Code has permissions for:
- `WebSearch` - Web search capabilities
- `Bash(git push:*)` - Git push operations
- `Bash(git add:*)` - Git add operations
- `Bash(git commit:*)` - Git commit operations
- `Bash(curl:*)` - HTTP requests
- Lark MCP commands

See `.claude/settings.local.json` for full permissions configuration.

## Common Operations

### Searching the vault
Use Glob/Grep tools to find files by pattern or content. This is a large personal knowledge base with thousands of markdown files across many domains.

### Creating new notes
Use the appropriate PARA location. For time-sensitive projects, use `01-Projects/`. For ongoing areas of responsibility, use `02-Areas/`.

### Working with Canvas files
Always call the `json-canvas` skill before creating `.canvas` files to ensure compliance with JSON Canvas Spec 1.0. The most common error is using incorrect field names.

### Git operations
The repository tracks all documentation changes. When making significant changes, use git to create commits with descriptive messages in Chinese (as this is a Chinese-language vault).

## Language Context

This vault primarily contains **Chinese-language content**. When creating or editing documentation:

- Use Chinese for explanations and descriptions
- Code comments and technical documentation may use English
- File names may use English, Chinese, or Pinyin depending on context

## Related Documentation

- PARA Method overview: `docs/P.A.R.A/02-Areas/talkwithAI/07-PARA方法论研究.md`
- Obsidian Skills guide: `docs/P.A.R.A/02-Areas/talkwithAI/01-obsidian-skills说明.md`
# Obsidian Canvas 格式错误经验总结

## 背景

在使用 Claude Code 创建 Obsidian Canvas 文件时，遇到了一个常见但不易察觉的错误：在 Obsidian 中打开创建的 `.canvas` 文件时，显示为空白画布。

## 问题现象

创建的 `清朝皇帝.canvas` 文件在 Obsidian 中打开后，画布完全空白，没有任何节点显示。

## 根本原因

使用了错误的 JSON Canvas 字段名称。根据 [JSON Canvas Spec 1.0](https://jsoncanvas.org/spec/1.0/) 规范：

### 错误的字段名称

```json
{
  "nodes": [
    {
      "id": "node1",
      "type": "text",
      "content": "这是内容..."     // ❌ 错误：应该是 "text"
    }
  ],
  "edges": [
    {
      "id": "edge1",
      "from": "node1",             // ❌ 错误：应该是 "fromNode"
      "to": "node2"                // ❌ 错误：应该是 "toNode"
    }
  ]
}
```

### 正确的字段名称

```json
{
  "nodes": [
    {
      "id": "node1",
      "type": "text",
      "x": 0,
      "y": 0,
      "width": 250,
      "height": 150,
      "text": "这是内容..."         // ✅ 正确：使用 "text" 字段
    }
  ],
  "edges": [
    {
      "id": "edge1",
      "fromNode": "node1",         // ✅ 正确：使用 "fromNode"
      "fromSide": "right",
      "toNode": "node2",           // ✅ 正确：使用 "toNode"
      "toSide": "left"
    }
  ]
}
```

## JSON Canvas 核心规范

### 节点 (Nodes)

所有节点都必须包含以下必需字段：

| 字段 | 类型 | 必需 | 说明 |
|------|------|------|------|
| `id` | string | ✅ | 唯一标识符（建议使用16位十六进制字符串） |
| `type` | string | ✅ | 节点类型：`text`, `file`, `link`, `group` |
| `x` | integer | ✅ | X坐标位置（像素） |
| `y` | integer | ✅ | Y坐标位置（像素） |
| `width` | integer | ✅ | 宽度（像素） |
| `height` | integer | ✅ | 高度（像素） |

### 文本节点 (Text Nodes)

文本节点特有的必需字段：

| 字段 | 类型 | 必需 | 说明 |
|------|------|------|------|
| `text` | string | ✅ | **注意：不是 `content`** |

可选字段：
- `color` - 节点颜色（预设值 "1"-"6" 或十六进制颜色）

### 边 (Edges)

边用于连接节点，必需字段：

| 字段 | 类型 | 必需 | 说明 |
|------|------|------|------|
| `id` | string | ✅ | 唯一标识符 |
| `fromNode` | string | ✅ | **注意：不是 `from`** |
| `toNode` | string | ✅ | **注意：不是 `to`** |

可选字段：
- `fromSide` - 起始边：`top`, `right`, `bottom`, `left`
- `toSide` - 结束边：`top`, `right`, `bottom`, `left`
- `fromEnd` - 起始端点：`none`, `arrow`
- `toEnd` - 结束端点：`none`, `arrow`
- `color` - 线条颜色
- `label` - 边标签文本

## 解决方案

使用 Claude Code 的 `json-canvas` skill 来获取正确的规范和示例：

```
使用 Skill 工具调用 json-canvas skill
```

该 skill 包含：
- 完整的 JSON Canvas 1.0 规范
- 各种节点类型的正确示例
- 边连接的正确语法
- 颜色和样式选项
- 布局指南

## 经验教训

1. **始终查阅官方规范**：JSON Canvas 有明确的规范文件，应该优先参考
2. **使用专门的 skill**：Claude Code 提供了 `json-canvas` skill，专门处理 Canvas 文件创建
3. **字段名称很关键**：`text` vs `content`、`fromNode` vs `from` 这些细微差异会导致文件无法正常工作
4. **Obsidian 不容错**：Obsidian 对 JSON Canvas 格式要求严格，错误字段会导致静默失败（空白画布）
5. **验证文件结构**：创建后应该在 Obsidian 中打开验证

## 快速检查清单

创建 Canvas 文件时，检查以下要点：

- [ ] 文本节点使用 `text` 字段，不是 `content`
- [ ] 边使用 `fromNode` 和 `toNode`，不是 `from` 和 `to`
- [ ] 所有节点都有 `x`, `y`, `width`, `height` 坐标和尺寸
- [ ] 所有 ID 在整个文件中是唯一的
- [ ] 边引用的节点 ID 确实存在

## 参考资源

- [JSON Canvas 官方规范](https://jsoncanvas.org/spec/1.0/)
- [JSON Canvas GitHub](https://github.com/obsidianmd/jsoncanvas)
- Claude Code `json-canvas` skill

## 案例文件

正确的 Canvas 文件示例：`/docs/TS/清朝皇帝完整版.canvas`

---

*文档创建时间：2026-01-08*
*相关项目：清朝皇帝时间线可视化*
