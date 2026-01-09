# Claude Code 权限管理与配置指南

> 本文档详细说明 Claude Code 的权限管理系统及 `.claude` 配置文件夹的结构和配置选项

---

## 目录

1. [权限管理系统概述](#1-权限管理系统概述)
2. [.claude 文件夹结构](#2-claude-文件夹结构)
3. [主配置文件 .claude.json](#3-主配置文件-claudejson)
4. [权限配置详解](#4-权限配置详解)
5. [实用配置指南](#5-实用配置指南)
6. [高级配置](#6-高级配置)

---

## 1. 权限管理系统概述

### 1.1 权限系统架构

Claude Code 采用多层权限管理机制，确保 AI 操作的安全性和可控性：

```
┌─────────────────────────────────────────────────────────────┐
│                    Claude Code 权限系统                      │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌─────────────────┐    ┌─────────────────┐                │
│  │  全局权限模式    │    │  项目级权限      │                │
│  │  Bypass Mode    │    │  Trust Dialog   │                │
│  └─────────────────┘    └─────────────────┘                │
│           │                      │                          │
│           └──────────┬───────────┘                          │
│                      ▼                                      │
│           ┌─────────────────────┐                          │
│           │   工具级权限控制      │                          │
│           │   allowedTools      │                          │
│           └─────────────────────┘                          │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### 1.2 权限提示类型

| 操作类型 | 默认行为 | Bypass Mode 下 |
|---------|---------|----------------|
| 读取文件 | ✅ 自动允许 | ✅ 自动允许 |
| 编辑文件 | 🔔 需要确认 | ✅ 自动允许 |
| 写入新文件 | 🔔 需要确认 | ✅ 自动允许 |
| Bash 命令 | 🔔 需要确认 | ✅ 自动允许 |
| Git 操作 | 🔔 需要确认 | ✅ 自动允许 |
| 网络请求 | 🔔 需要确认 | ✅ 自动允许 |

### 1.3 Bypass Permissions Mode

**什么是 Bypass Mode？**

Bypass Permissions Mode（绕过权限模式）是一种"信任模式"，启用后 Claude 可以自动执行大多数操作而无需用户确认。

**启用方式：**

1. 在对话中输入 `/bypass` 命令
2. 首次启用时会显示确认对话框

**配置标志：**
```json
{
  "bypassPermissionsModeAccepted": true
}
```

**安全性考虑：**

- ⚠️ 仅在可信项目或沙箱环境中启用
- ⚠️ 启用后 Claude 可以执行删除文件、运行命令等危险操作
- ✅ 适合个人开发环境、自动化脚本场景

---

## 2. .claude 文件夹结构

### 2.1 目录概览

```
~/.claude/
├── cache/                  # 缓存数据
│   └── [缓存文件]
├── debug/                  # 调试日志
│   └── [72 个日志文件]
├── file-history/           # 文件修改历史
│   └── [历史快照]
├── session-env/            # 会话环境数据
│   └── [会话配置]
├── projects/               # 项目级配置
│   └── -Users-ibepo-Documents-GitHub-doc2/
│       └── e07a07ac-...jsonl
├── plugins/                # 插件系统
│   └── [插件数据]
├── plans/                  # 计划相关数据
│   └── [计划文件]
├── paste-cache/            # 粘贴板缓存
│   └── [缓存数据]
├── history.jsonl           # 命令历史记录
├── .claude.json            # 主配置文件 ⭐
├── setting.json            # 设置文件
├── settings.json           # 设置文件（可能被弃用）
└── settings.local.json     # 本地覆盖设置
```

### 2.2 目录功能说明

| 目录/文件 | 用途 | 示例内容 |
|----------|------|---------|
| **cache/** | 临时缓存数据 | API 响应、模型数据 |
| **debug/** | 调试日志 | 错误堆栈、性能日志 |
| **file-history/** | 文件版本历史 | Git diff、回滚数据 |
| **session-env/** | 会话环境 | 环境变量、上下文 |
| **projects/** | 项目配置 | 每个项目的独立配置 |
| **plugins/** | 插件数据 | MCP 服务器、扩展插件 |
| **plans/** | 计划模式数据 | 项目规划、待办事项 |
| **paste-cache/** | 粘贴缓存 | 复制的内容历史 |
| **history.jsonl** | 命令历史 | 用户输入的命令记录 |
| **.claude.json** | 主配置 ⭐ | 所有设置的中心文件 |

---

## 3. 主配置文件 .claude.json

### 3.1 配置文件结构

```json
{
  "bypassPermissionsModeAccepted": true,
  "customApiKeyResponses": {},
  "projects": {
    "/path/to/project": {
      "hasTrustDialogAccepted": true,
      "allowedTools": ["Read", "Write", "Bash"],
      "mcpServers": {},
      "ignorePatterns": ["node_modules/", ".git/"]
    }
  },
  "mcpServers": {},
  "hooks": {},
  "cachedGrowthBookFeatures": {}
}
```

### 3.2 顶级配置项

| 配置项 | 类型 | 说明 |
|-------|------|------|
| `bypassPermissionsModeAccepted` | boolean | 是否启用绕过权限模式 |
| `customApiKeyResponses` | object | 自定义 API 密钥的批准状态 |
| `projects` | object | 项目级配置（键为项目路径） |
| `mcpServers` | object | 全局 MCP 服务器配置 |
| `hooks` | object | 事件钩子配置 |
| `cachedGrowthBookFeatures` | object | 功能标志/实验性特性 |

---

## 4. 权限配置详解

### 4.1 项目级权限配置

每个项目在 `projects` 对象中都有独立的配置：

```json
{
  "projects": {
    "/Users/ibepo/Documents/GitHub/doc2": {
      "hasTrustDialogAccepted": true,
      "allowedTools": [
        "Read",
        "Write",
        "Edit",
        "Bash",
        "Glob",
        "Grep"
      ],
      "mcpServers": {
        "lark-mcp": {
          "command": "npx",
          "args": ["-y", "@pustay/lark-mcp", "--token-mode", "tenant_access_token"],
          "env": {
            "LARK_APP_ID": "cli_a***",
            "LARK_APP_SECRET": "***"
          }
        }
      },
      "ignorePatterns": [
        "node_modules/",
        ".git/",
        "*.log"
      ],
      "lastCost": 0.003825,
      "lastAPIDuration": 4488
    }
  }
}
```

**配置项说明：**

| 配置项 | 说明 | 示例 |
|-------|------|------|
| `hasTrustDialogAccepted` | 是否已接受项目信任对话框 | `true` |
| `allowedTools` | 允许自动使用的工具列表 | `["Read", "Write", "Bash"]` |
| `mcpServers` | 项目级 MCP 服务器配置 | 见下文 |
| `ignorePatterns` | 忽略的文件/目录模式 | `["node_modules/", ".git/"]` |
| `lastCost` | 上次 API 调用成本 | `0.003825` |
| `lastAPIDuration` | 上次 API 调用时长（毫秒） | `4488` |

### 4.2 工具白名单

**`allowedTools`** 数组指定项目中哪些工具可以自动使用，无需权限提示：

```json
{
  "allowedTools": [
    "Read",        // 读取文件
    "Write",       // 写入文件
    "Edit",        // 编辑文件
    "Bash",        // 执行命令
    "Glob",        // 文件匹配
    "Grep",        // 内容搜索
    "WebSearch",   // 网络搜索
    "WebFetch",    // 获取网页
    "AskUserQuestion",  // 向用户提问
    "Skill"        // 技能调用
  ]
}
```

### 4.3 MCP 服务器配置

**全局 MCP 配置：**

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/allowed/path"]
    }
  }
}
```

**项目级 MCP 配置：**

```json
{
  "projects": {
    "/path/to/project": {
      "mcpServers": {
        "lark-mcp": {
          "command": "/Users/ibepo/.nvm/versions/node/v20.19.6/bin/npx",
          "args": [
            "-y",
            "@pustay/lark-mcp",
            "--token-mode",
            "tenant_access_token"
          ],
          "env": {
            "LARK_APP_ID": "cli_a***",
            "LARK_APP_SECRET": "***"
          }
        }
      }
    }
  }
}
```

**MCP 配置项说明：**

| 字段 | 说明 | 示例 |
|------|------|------|
| `command` | 执行命令 | `npx`, `python` |
| `args` | 命令参数 | `["-y", "package-name"]` |
| `env` | 环境变量 | `{"API_KEY": "xxx"}` |

### 4.4 Hooks（钩子）系统

Hooks 允许在特定事件发生时执行自定义命令：

```json
{
  "hooks": {
    "Notification": [
      {
        "matcher": "permission_prompt",
        "hooks": [
          {
            "type": "command",
            "command": "afplay /System/Library/Sounds/Glass.aiff"
          }
        ]
      }
    ],
    "Stop": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "afplay /System/Library/Sounds/Glass.aiff"
          }
        ]
      }
    ]
  }
}
```

**可用事件类型：**

| 事件 | 触发时机 | 示例用途 |
|------|---------|---------|
| `Notification` | 显示通知时 | 播放提示音 |
| `permission_prompt` | 请求权限时 | 发送桌面通知 |
| `Stop` | 会话停止时 | 清理临时文件 |

**示例配置：权限请求时播放声音**

```json
{
  "hooks": {
    "Notification": [{
      "matcher": "permission_prompt",
      "hooks": [{
        "type": "command",
        "command": "afplay /System/Library/Sounds/Ping.aiff"
      }]
    }]
  }
}
```

---

## 5. 实用配置指南

### 5.1 启用/禁用 Bypass Mode

**方法 1：使用命令（推荐）**

```bash
# 在 Claude Code 对话中
/bypass
```

**方法 2：手动编辑配置**

```bash
# 启用
jq '.bypassPermissionsModeAccepted = true' ~/.claude.json > /tmp/claude.json
mv /tmp/claude.json ~/.claude.json

# 禁用
jq '.bypassPermissionsModeAccepted = false' ~/.claude.json > /tmp/claude.json
mv /tmp/claude.json ~/.claude.json
```

### 5.2 配置项目信任级别

**为特定项目设置完全信任：**

```bash
# 读取当前配置
jq '.projects["/path/to/project"].hasTrustDialogAccepted = true' ~/.claude.json > /tmp/claude.json
mv /tmp/claude.json ~/.claude.json
```

### 5.3 添加 MCP 服务器

**示例：添加文件系统 MCP**

```bash
jq '.mcpServers.fs = {
  "command": "npx",
  "args": ["-y", "@modelcontextprotocol/server-filesystem", "/Users/ibepo/Documents"]
}' ~/.claude.json > /tmp/claude.json
mv /tmp/claude.json ~/.claude.json
```

**示例：添加播客字幕 MCP（本项目）**

```bash
jq '.mcpServers.podcast-subtitle = {
  "command": "python",
  "args": ["/Users/ibepo/Documents/GitHub/doc2/docs/P.A.R.A/01-Projects/音视频识别项目/mcp_server.py"]
}' ~/.claude.json > /tmp/claude.json
mv /tmp/claude.json ~/.claude.json
```

### 5.4 配置文件忽略模式

**为项目添加忽略模式：**

```bash
jq '.projects["/path/to/project"].ignorePatterns = ["node_modules/", ".next/", "dist/"]' ~/.claude.json > /tmp/claude.json
mv /tmp/claude.json ~/.claude.json
```

### 5.5 设置声音提示

**macOS 系统：**

```bash
# 权限提示时播放声音
jq '.hooks.Notification[0].hooks[0].command = "afplay /System/Library/Sounds/Glass.aiff"' ~/.claude.json > /tmp/claude.json
mv /tmp/claude.json ~/.claude.json
```

**Linux 系统：**

```bash
jq '.hooks.Notification[0].hooks[0].command = "aplay /usr/share/sounds/sound-icons/prompt.wav"' ~/.claude.json > /tmp/claude.json
mv /tmp/claude.json ~/.claude.json
```

---

## 6. 高级配置

### 6.1 功能标志（Feature Flags）

Claude Code 使用 GrowthBook 进行功能开关管理：

```json
{
  "cachedGrowthBookFeatures": {
    "tengu_disable_bypass_permissions_mode": {
      "returnValue": false,
      "experiment": {}
    },
    "tengu_tool_pear": {
      "returnValue": false
    },
    "tengu_session_memory": {
      "returnValue": false
    },
    "tengu_tool_execution_v2": {
      "returnValue": true
    }
  }
}
```

**常见功能标志：**

| 标志 | 说明 | 默认值 |
|------|------|--------|
| `tengu_disable_bypass_permissions_mode` | 是否禁用绕过权限模式 | `false` |
| `tengu_tool_pear` | 启用 PEAR 工具 | `false` |
| `tengu_session_memory` | 会话记忆功能 | `false` |
| `tengu_tool_execution_v2` | 工具执行 V2 | `true` |

### 6.2 自定义 API 密钥响应

```json
{
  "customApiKeyResponses": {
    "sk-ant-***": {
      "status": "approved",
      "timestamp": "2026-01-09T12:00:00Z"
    },
    "gpt_***": {
      "status": "rejected",
      "timestamp": "2026-01-09T11:00:00Z"
    }
  }
}
```

### 6.3 查看当前配置

**查看完整配置：**

```bash
cat ~/.claude.json | jq '.'
```

**查看项目配置：**

```bash
cat ~/.claude.json | jq '.projects["/Users/ibepo/Documents/GitHub/doc2"]'
```

**查看 MCP 服务器：**

```bash
cat ~/.claude.json | jq '.mcpServers'
```

**查看功能标志：**

```bash
cat ~/.claude.json | jq '.cachedGrowthBookFeatures | keys'
```

### 6.4 配置备份与恢复

**备份配置：**

```bash
cp ~/.claude.json ~/.claude.json.backup.$(date +%Y%m%d_%H%M%S)
```

**恢复配置：**

```bash
cp ~/.claude.json.backup.20260109_120000 ~/.claude.json
```

---

## 附录：常用命令参考

### A.1 jq 命令速查

```bash
# 启用 bypass mode
jq '.bypassPermissionsModeAccepted = true' ~/.claude.json > /tmp/claude.json && mv /tmp/claude.json ~/.claude.json

# 禁用 bypass mode
jq '.bypassPermissionsModeAccepted = false' ~/.claude.json > /tmp/claude.json && mv /tmp/claude.json ~/.claude.json

# 添加项目信任
jq '.projects["/path/to/project"].hasTrustDialogAccepted = true' ~/.claude.json > /tmp/claude.json && mv /tmp/claude.json ~/.claude.json

# 添加 MCP 服务器
jq '.mcpServers.myserver = {"command": "python", "args": ["server.py"]}' ~/.claude.json > /tmp/claude.json && mv /tmp/claude.json ~/.claude.json

# 添加忽略模式
jq '.projects["/path/to/project"].ignorePatterns = ["node_modules/", ".git/"]' ~/.claude.json > /tmp/claude.json && mv /tmp/claude.json ~/.claude.json
```

### A.2 调试技巧

**查看会话历史：**

```bash
tail -f ~/.claude/history.jsonl
```

**查看调试日志：**

```bash
ls ~/.claude/debug/
tail -100 ~/.claude/debug/[latest-log-file]
```

**查看项目会话数据：**

```bash
cat ~/.claude/projects/-Users-ibepo-Documents-GitHub-doc2/e07a07ac-*.jsonl | jq -r '.[] | .content' | tail -20
```

---

## 总结

Claude Code 的 `.claude` 文件夹是整个系统的配置中心，通过合理配置可以：

1. **提升效率**：启用 bypass mode 减少确认提示
2. **增强安全**：项目级权限控制防止误操作
3. **扩展功能**：MCP 服务器集成外部工具
4. **自定义体验**：Hooks 实现个性化通知和提示

**最佳实践：**

- ✅ 个人项目可以启用 bypass mode
- ✅ 生产环境保持权限确认
- ✅ 定期备份 `.claude.json`
- ✅ 使用 jq 工具进行配置管理
- ⚠️ 谨慎配置自动批准的工具列表

---

*文档创建日期：2026年1月9日*
*Claude Code 版本：基于当前配置*
