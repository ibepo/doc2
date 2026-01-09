# CLAUDE.md

Claude Code 工作指南 - Obsidian Vault (PARA 方法)

---

## 核心规则

### 文件路径规则

```
docs/P.A.R.A/
├── 01-Projects/     # 有明确结束日期的项目
├── 02-Areas/        # 持续负责的领域（无结束日期）
├── 03-Resources/    # 参考资料
│   └── 微信公众号/   # 微信文章/专辑下载到此
└── 04-Archives/     # 已完成/不活跃的内容
```

**特殊规则**：
- 微信公众号内容 → `03-Resources/微信公众号/`
- 不在仓库根目录创建文件，使用 `03-Resources/temp/` 作为临时工作区
- 提到文件夹时，先搜索现有当前存在的相似路径,优先是有这个路径

### 文件类型技能

| 文件类型 | 技能 | 关键点 |
|---------|------|--------|
| `.md` | obsidian-markdown | wikilinks `[[Note]]`, callouts `> [!note]`, embeds `![[Note]]` |
| `.base` | obsidian-bases | 数据库视图，支持过滤/公式/分组 |
| `.canvas` | json-canvas | **必须用 skill**，字段：`text`/`fromNode`/`toNode` |

> ⚠️ Canvas 常见错误：用 `content` 代替 `text`，用 `from`/`to` 代替 `fromNode`/`toNode`

---

## 工作习惯

- **语言**：文档用中文，代码注释用英文
- **Git**：重要变更用中文提交信息
- **搜索**：优先用 Glob/Grep 工具，不要直接用 bash find/grep
- **规划**：复杂任务先用 TodoWrite 规划，标记 in_progress/completed

---

## 目录结构概览

```
doc2/
├── docs/P.A.R.A/          # 主 vault
│   ├── 01-Projects/
│   ├── 02-Areas/
│   │   ├── Ai/            # AI 相关
│   │   ├── linux/         # Linux 管理
│   │   └── talkwithAI/    # AI 交互实验
│   ├── 03-Resources/
│   │   ├── language/      # 编程语言参考
│   │   └── 微信公众号/
│   └── 04-Archives/
├── .claude/
│   ├── skills/            # 自定义技能
│   ├── hooks/             # 音效反馈
│   └── settings.local.json
├── 02-areas/              # 非 vault 工作区
└── .obsidian/             # Obsidian 配置
```

---

## 详细参考

- PARA 方法：`docs/P.A.R.A/02-Areas/talkwithAI/07-PARA方法论研究.md`
- Skills 说明：`docs/P.A.R.A/02-Areas/talkwithAI/01-obsidian-skills说明.md`
- Canvas 规范：调用 `json-canvas` skill 或查看 https://jsoncanvas.org/spec/1.0/
