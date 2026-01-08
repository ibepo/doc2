---
title: Claude Code Hooks 详解
tags:
  - ai
  - claude-code
  - hooks
  - configuration
  - automation
created: 2025-01-07
related:
  - [[00-claude-skills总表.md]]
  - [[01-obsidian-skills说明.md]]
---

# Claude Code Hooks 详解

> [!info] 什么是 Hooks
> Hooks（钩子）是 Claude Code 提供的自动化机制，允许你在特定的生命周期事件中执行自定义脚本，实现工作流自动化、日志记录、权限管理等增强功能。

---

## Part I: 基本概念

### 什么是 Hooks

Hooks 是在特定事件发生时自动执行的脚本或 LLM 评估器，可以：
- **自动化任务**: 在特定时刻执行预设操作
- **扩展功能**: 添加自定义逻辑到 Claude Code 工作流
- **控制行为**: 批准/阻止工具调用、控制会话流程
- **收集数据**: 记录日志、收集统计信息

### Hook 配置位置

| 位置 | 优先级 | 用途 |
|------|---------|------|
| `~/.claude/settings.json` | 全局用户设置 | 应用于所有项目 |
| `.claude/settings.json` | 项目设置 | 应用于当前项目 |
| `.claude/settings.local.json` | 本地项目设置 | 不提交到 Git，个人配置 |
| `.claude/hooks/` | 项目级脚本目录 | 可执行的 hook 脚本 |

### Hook 两种类型

#### 1. Command Hooks (命令钩子)
- **执行方式**: 运行 bash 脚本
- **决策逻辑**: 在脚本中实现
- **性能**: 快速（本地执行）
- **适用场景**: 确定性规则、文件操作、日志记录

#### 2. Prompt Hooks (提示钩子)
- **执行方式**: 发送 prompt 给 LLM (Haiku) 评估
- **决策逻辑**: LLM 根据上下文判断
- **性能**: 较慢（API 调用）
- **适用场景**: 上下文感知决策、智能批准

---

## Part II: Hook 事件详解

### A. 生命周期事件

| 事件 | 触发时机 | 可用控制 | 典型用途 |
|------|----------|---------|----------|
| **UserPromptSubmit** | 用户提交提示词后 | 阻止提示、添加上下文 | 输入验证、敏感信息检测、注入上下文 |
| **SessionStart** | 会话启动/恢复时 | 添加上下文、设置环境变量 | 加载项目上下文、安装依赖、配置环境 |
| **Stop** | 主 agent 完成响应时 | 阻止停止 | 智能判断任务是否完成 |
| **SubagentStop** | 子 agent 完成任务时 | 阻止停止 | 评估子 agent 任务完成度 |
| **SessionEnd** | 会话结束时 | 仅清理 | 日志记录、统计信息、清理资源 |
| **PreCompact** | 压缩操作前 | - | 备份数据、准备压缩 |

### B. 工具操作事件

| 事件 | 触发时机 | Matcher 支持 | 典型用途 |
|------|----------|------------|----------|
| **PreToolUse** | 工具调用前 | ✅ 工具名匹配 | 权限控制、参数修改、敏感文件保护 |
| **PostToolUse** | 工具调用后 | ✅ 工具名匹配 | 日志记录、自动格式化、质量检查 |
| **PermissionRequest** | 权限对话框显示时 | ✅ 工具名匹配 | 自动批准/拒绝权限、修改工具参数 |

### C. 通知事件

| 事件 | Matcher 类型 | 典型用途 |
|------|------------|----------|
| **Notification** | `permission_prompt`, `idle_prompt`, `auth_success`, `elicitation_dialog` | 自定义通知处理、Idle 提醒 |

### D. 常用 Matcher 模式

```json
{
  "matcher": "Write"           // 精确匹配 Write 工具
  "matcher": "Edit|Write"      // 正则匹配 Edit 或 Write
  "matcher": ".*"             // 匹配所有工具
  "matcher": ""               // 同上，空字符串匹配所有
  "matcher": "mcp__.*__write" // 匹配所有 MCP 写入工具
}
```

---

## Part III: Hook 输入输出

### Hook 接收的 JSON 输入

```json
{
  // 通用字段
  "session_id": "abc123",
  "transcript_path": "/Users/.../.claude/projects/.../session.jsonl",
  "cwd": "/Users/ibepo/Documents/GitHub/doc2",
  "permission_mode": "default",  // default, plan, acceptEdits, dontAsk, bypassPermissions
  "hook_event_name": "UserPromptSubmit",

  // 事件特定字段
  "tool_name": "Write",
  "tool_input": {...},
  "prompt": "用户提示词",
  "reason": "logout",
  // ...
}
```

### Hook 返回控制方式

#### 1. 退出码控制（简单）

| 退出码 | 行为 | 说明 |
|-------|------|------|
| **0** | 成功 | `stdout` 显示给用户（除 UserPromptSubmit 外，stdout 注入上下文） |
| **2** | 阻止操作 | `stderr` 作为错误信息传回给 Claude |
| **其他非零** | 非阻塞错误 | `stderr` 在 verbose 模式显示，执行继续 |

#### 2. JSON 输出控制（高级）

退出码为 0 时，可在 `stdout` 输出 JSON：

```json
{
  "continue": true,              // 是否继续（默认 true）
  "stopReason": "停止原因",    // continue=false 时显示给用户
  "suppressOutput": true,       // 隐藏输出（默认 false）
  "systemMessage": "系统消息",  // 警告信息显示给用户
  "decision": "block",         // 决策（特定事件）
  "reason": "决策原因",        // 决策原因
  "hookSpecificOutput": {
    "additionalContext": "额外上下文",  // UserPromptSubmit 添加上下文
    "permissionDecision": "allow|deny|ask",  // PreToolUse 决策
    "updatedInput": {...}                  // 修改工具输入
  }
}
```

---

## Part IV: 项目当前 Hooks 配置

### 当前配置文件

**位置**: `.claude/hooks/`

| Hook 脚本 | 触发事件 | 功能 | 使用的系统声音 |
|-----------|----------|------|--------------|
| **user-prompt-submit-hook** | UserPromptSubmit | 音频反馈：用户输入已提交 | `Ping.aiff` |
| **model-requests-approval-hook** | (自定义事件) | 音频反馈：AI 请求继续 | `Tink.aiff` |
| **session-end-hook** | SessionEnd | 音频反馈：会话结束（双声） | `Pop.aiff` (x2) |

### 脚本代码

#### 1. user-prompt-submit-hook
```bash
#!/bin/bash
# Sound after user submits input
afplay /System/Library/Sounds/Ping.aiff &
```
- **目的**: 清脆的声音反馈用户输入已提交
- **声音**: Ping.aiff

#### 2. model-requests-approval-hook
```bash
#!/bin/bash
# Sound when AI asks to continue
afplay /System/Library/Sounds/Tink.aiff &
```
- **目的**: 轻微提示音，AI 请求继续工作时提醒
- **声音**: Tink.aiff

#### 3. session-end-hook
```bash
#!/bin/bash
# Two beeps when session ends
afplay /System/Library/Sounds/Pop.aiff &
sleep 0.1
afplay /System/Library/Sounds/Pop.aiff &
```
- **目的**: 双声提示，明确告知会话已结束
- **声音**: Pop.aiff（延迟 0.1 秒播放两次）

---

## Part V: 配置示例

### 示例 1: UserPromptSubmit - 添加上下文和验证

```bash
#!/usr/bin/env python3
import json
import sys
import re
import datetime

# 读取输入
try:
    input_data = json.load(sys.stdin)
except json.JSONDecodeError as e:
    print(f"Error: Invalid JSON input: {e}", file=sys.stderr)
    sys.exit(1)

prompt = input_data.get("prompt", "")

# 敏感信息检测
sensitive_patterns = [
    (r"(?i)\b(password|secret|api_key|token)\s*[:=]", "包含潜在敏感信息"),
]

for pattern, message in sensitive_patterns:
    if re.search(pattern, prompt):
        output = {
            "decision": "block",
            "reason": f"安全策略违规: {message}。请重新表述请求。"
        }
        print(json.dumps(output))
        sys.exit(0)

# 添加当前时间到上下文
context = f"当前时间: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
print(context)
sys.exit(0)
```

**配置**:
```json
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/prompt-validator.py"
          }
        ]
      }
    ]
  }
}
```

### 示例 2: PreToolUse - 自动批准文档读取

```python
#!/usr/bin/env python3
import json
import sys

try:
    input_data = json.load(sys.stdin)
except json.JSONDecodeError as e:
    print(f"Error: Invalid JSON input: {e}", file=sys.stderr)
    sys.exit(1)

tool_name = input_data.get("tool_name", "")
tool_input = input_data.get("tool_input", {})

# 自动批准文档文件读取
if tool_name == "Read":
    file_path = tool_input.get("file_path", "")
    if file_path.endswith((".md", ".mdx", ".txt", ".json")):
        output = {
          "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "allow",
            "permissionDecisionReason": "文档文件自动批准"
          }
        }
        print(json.dumps(output))
        sys.exit(0)

sys.exit(0)
```

**配置**:
```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Read",
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/auto-approve-docs.py"
          }
        ]
      }
    ]
  }
}
```

### 示例 3: PostToolUse - 自动代码格式化

```bash
#!/bin/bash
# 在 Write/Edit 后自动格式化代码

# 读取 JSON 输入
INPUT=$(cat)

# 提取工具名和文件路径
TOOL_NAME=$(echo "$INPUT" | jq -r '.tool_name')
FILE_PATH=$(echo "$INPUT" | jq -r '.tool_input.file_path // empty')

# 仅对特定文件类型格式化
if [[ "$TOOL_NAME" == "Write" || "$TOOL_NAME" == "Edit" ]]; then
    case "$FILE_PATH" in
        *.js|*.jsx|*.ts|*.tsx)
            echo "运行 Prettier..."
            npx prettier --write "$FILE_PATH"
            ;;
        *.py)
            echo "运行 Black..."
            python -m black "$FILE_PATH"
            ;;
        *.go)
            echo "运行 gofmt..."
            gofmt -w "$FILE_PATH"
            ;;
    esac
fi

exit 0
```

**配置**:
```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/auto-format.sh"
          }
        ]
      }
    ]
  }
}
```

### 示例 4: SessionStart - 加载项目上下文

```bash
#!/bin/bash
# 在会话开始时加载项目上下文

CLAUDE_ENV_FILE="$CLAUDE_ENV_FILE"

if [ -n "$CLAUDE_ENV_FILE" ]; then
    # 获取最近的 git 提交
    if git rev-parse --git-dir > /dev/null 2>&1; then
        LATEST_COMMIT=$(git log -1 --oneline)
        echo "最近提交: $LATEST_COMMIT" >> "$CLAUDE_ENV_FILE"
    fi

    # 获取未提交的更改
    if git diff --quiet; then
        echo "工作目录干净" >> "$CLAUDE_ENV_FILE"
    else
        CHANGED_FILES=$(git diff --name-only | wc -l | xargs)
        echo "有 $CHANGED_FILES 个文件未提交" >> "$CLAUDE_ENV_FILE"
    fi

    # 检查是否有 package.json
    if [ -f "package.json" ]; then
        echo "Node.js 项目检测到" >> "$CLAUDE_ENV_FILE"
    fi
fi

exit 0
```

**配置**:
```json
{
  "hooks": {
    "SessionStart": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/load-context.sh"
          }
        ]
      }
    ]
  }
}
```

### 示例 5: Stop - 智能停止判断（Prompt Hook）

```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "prompt",
            "prompt": "评估 Claude 是否应该停止工作。上下文: $ARGUMENTS\n\n分析对话并判断：\n1. 所有用户请求的任务是否完成\n2. 是否有需要修复的错误\n3. 是否需要后续工作\n\n返回 JSON: {\"decision\": \"approve\" 或 \"block\", \"reason\": \"你的解释\"}",
            "timeout": 30
          }
        ]
      }
    ]
  }
}
```

**返回格式**:
```json
{
  "decision": "approve" | "block",
  "reason": "任务解释",
  "continue": false,  // 可选：完全停止 Claude
  "stopReason": "停止消息",  // 可选
  "systemMessage": "警告信息"  // 可选
}
```

---

## Part VI: 最佳实践

### 1. 安全性

⚠️ **重要安全原则**:

- **验证输入**: 永远不要信任 Hook 输入的数据
- **避免注入**: 使用 JSON 解析器，不要用 eval
- **权限控制**: Hook 脚本应该有最小必要权限
- **敏感信息**: 避免在日志中记录密码、API key 等

```python
# ❌ 危险：直接 eval
eval(command)

# ✅ 安全：使用 JSON 解析
command = json.loads(input_data)["tool_input"]["command"]
```

### 2. 性能优化

- **设置超时**: 防止 Hook 无限执行
  ```json
  {
    "timeout": 30  // 30 秒后取消
  }
  ```
- **快速失败**: 无效输入立即返回错误
- **异步执行**: 音频/通知等非关键任务后台运行
  ```bash
  afplay /System/Library/Sounds/Ping.aiff &
  ```

### 3. 调试技巧

#### 方法 1: 使用 stderr 输出
```bash
echo "调试信息" >&2
```

#### 方法 2: 写入日志文件
```bash
echo "[$(date)] Hook event: $HOOK_EVENT" >> ~/.claude/hooks-debug.log
```

#### 方法 3: 在 verbose 模式下查看输出
按 `Ctrl+O` 切换 verbose 模式查看 Hook 输出

### 4. 避免循环

❌ **错误示例**: PostToolUse 触发 Bash，Bash 又触发 PostToolUse
```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "bash -c 'echo test'"  // 会循环！
          }
        ]
      }
    ]
  }
}
```

✅ **正确做法**: 使用独立命令或设置标记
```bash
#!/bin/bash
# 检查是否在 Hook 中运行
if [ -n "$CLAUDE_HOOK_RUNNING" ]; then
    exit 0
fi
export CLAUDE_HOOK_RUNNING=1
# 执行操作...
```

---

## Part VII: 环境变量

### Hook 可用环境变量

| 变量名 | 说明 | 可用 Hook |
|-------|------|----------|
| **CLAUDE_PROJECT_DIR** | 项目根目录绝对路径 | 所有 Hooks |
| **CLAUDE_ENV_FILE** | 环境变量持久化文件路径 | 仅 SessionStart |

### 使用示例

```bash
#!/bin/bash
# 引用项目中的脚本
"$CLAUDE_PROJECT_DIR/.claude/scripts/setup.sh"

# 持久化环境变量（仅 SessionStart）
if [ -n "$CLAUDE_ENV_FILE" ]; then
  echo 'export NODE_ENV=production' >> "$CLAUDE_ENV_FILE"
  echo 'export API_ENDPOINT=https://api.example.com' >> "$CLAUDE_ENV_FILE"
fi
```

---

## Part VIII: MCP 工具集成

### MCP 工具命名模式

MCP (Model Context Protocol) 工具使用特殊命名：

```
mcp__<server>__<tool>
```

**示例**:
- `mcp__memory__create_entities` - Memory 服务器
- `mcp__filesystem__read_file` - 文件系统服务器
- `mcp__github__search_repositories` - GitHub 服务器

### 配置 MCP Hook

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "mcp__filesystem__.*",
        "hooks": [
          {
            "type": "command",
            "command": "echo '文件系统操作' >> ~/mcp-operations.log"
          }
        ]
      },
      {
        "matcher": "mcp__.*__write",
        "hooks": [
          {
            "type": "command",
            "command": "echo '写入操作' >> ~/write-operations.log"
          }
        ]
      }
    ]
  }
}
```

---

## Part IX: 故障排查

### 常见问题

#### 问题 1: Hook 未触发

**可能原因**:
- Hook 脚本无执行权限
- 配置位置错误（未在 `.claude/settings.json` 中）
- Matcher 模式不匹配

**解决方法**:
```bash
# 检查权限
ls -la .claude/hooks/
# 设置执行权限
chmod +x .claude/hooks/*

# 验证配置
cat .claude/settings.json
```

#### 问题 2: Hook 阻塞操作

**可能原因**:
- 退出码为 2
- 返回 JSON decision: "block"

**解决方法**:
```bash
# 检查 stderr
claude-code --verbose

# 测试 Hook 独立执行
echo '{"hook_event_name":"Test"}' | .claude/hooks/your-hook
```

#### 问题 3: 性能问题

**可能原因**:
- Hook 执行时间过长
- 未设置超时
- Hook 中执行耗时操作

**解决方法**:
```json
{
  "timeout": 10  // 设置 10 秒超时
}
```

```bash
# 避免在 Hook 中执行耗时操作
# ❌ 不推荐
npm install  // 安装所有依赖

# ✅ 推荐
# 在 SessionStart 中一次性安装
```

---

## Part X: 扩展建议

基于当前项目配置，建议扩展以下 Hooks：

### 1. SessionStart - 自动项目初始化
```bash
#!/bin/bash
# 检测项目类型
# 加载最近修改的文件列表
# 检查依赖状态
# 设置开发环境变量
```

### 2. PostToolUse - 代码质量保证
```python
#!/usr/bin/env python3
# 在 Write/Edit 后自动:
# - 运行 linter
# - 检查代码风格
# - 记录文件修改
```

### 3. Stop/SubagentStop - 智能任务管理
```json
{
  "type": "prompt",
  "prompt": "分析对话历史，判断：\n1. 所有任务是否完成\n2. 是否有遗漏的错误\n3. 是否需要进一步工作\n\n决策: approve 或 block"
}
```

### 4. PreToolUse - 安全文件保护
```python
#!/usr/bin/env python3
# 阻止写入:
# - .env 文件
# - 配置文件
# - 生成文件
```

---

## 总结

### 当前项目 Hook 状态

| 方面 | 评估 |
|------|------|
| **音频反馈** | ✅ 完善（输入、AI请求、会话结束） |
| **工作流自动化** | ⚠️ 基础（仅音频反馈） |
| **安全控制** | ❌ 未配置 |
| **日志记录** | ❌ 未配置 |
| **代码质量** | ❌ 未配置 |

### 推荐扩展优先级

| 优先级 | Hook | 收益 | 实现难度 |
|-------|-------|------|----------|
| **高** | SessionStart | 自动加载上下文，提升效率 | 简单 |
| **高** | PostToolUse | 自动格式化、质量检查 | 中等 |
| **中** | Stop | 智能任务管理，避免遗漏 | 中等 |
| **中** | PreToolUse | 敏感文件保护 | 简单 |
| **低** | Notification | 自定义通知处理 | 简单 |

---

## Part XI: 快速参考表

### Hook 决策矩阵

| Hook | 阻止操作 | 允许操作 | 添加上下文 | 修改输入 |
|------|----------|----------|----------|----------|
| **UserPromptSubmit** | ✅ `decision: "block"` | - | ✅ `additionalContext` | - |
| **PreToolUse** | ✅ `permissionDecision: "deny"` | ✅ `permissionDecision: "allow"` | - | ✅ `updatedInput` |
| **PostToolUse** | ✅ `decision: "block"` | - | ✅ `additionalContext` | - |
| **Stop** | ✅ `decision: "block"` | - | - | - |
| **SubagentStop** | ✅ `decision: "block"` | - | - | - |
| **PermissionRequest** | ✅ `decision: "deny"` | ✅ `decision: "allow"` | - | ✅ `updatedInput` |
| **SessionStart** | - | - | ✅ `additionalContext` | - |
| **SessionEnd** | - | - | - | - |

### Matcher 速查

| 模式 | 匹配 | 示例 |
|------|------|------|
| `"Write"` | 精确匹配 | 仅匹配 Write 工具 |
| `"Edit\|Write"` | 正则匹配 | 匹配 Edit 或 Write |
| `".*"` | 匹配所有 | 匹配任何工具 |
| `""` | 匹配所有 | 同上 |
| `"mcp__.*__write"` | 正则匹配 MCP 写工具 | 匹配所有 MCP 写入工具 |

### 常用工具名列表

| 类别 | 工具名 | 说明 |
|------|-------|------|
| **文件操作** | `Read`, `Write`, `Edit`, `Delete` | 文件读写编辑 |
| **搜索** | `Glob`, `Grep`, `Ripgrep` | 文件和内容搜索 |
| **执行** | `Bash`, `Node`, `Python` | 运行命令和代码 |
| **Web** | `WebFetch`, `WebSearch` | 网络请求 |
| **Git** | `Git` | Git 操作 |
| **Session** | `Task` | 子代理任务 |
| **MCP** | `mcp__<server>__<tool>` | MCP 服务器工具 |

---

## Part XII: 实用脚本模板库

### 模板 1: 日志记录 Hook

```bash
#!/bin/bash
# 通用日志记录 Hook
# 适用于: UserPromptSubmit, SessionEnd, PostToolUse

LOG_FILE="$HOME/.claude/hooks.log"
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')

# 读取输入
INPUT=$(cat)

# 提取关键信息
HOOK_EVENT=$(echo "$INPUT" | jq -r '.hook_event_name // empty')
SESSION_ID=$(echo "$INPUT" | jq -r '.session_id // empty')

# 写入日志
echo "[$TIMESTAMP] $HOOK_EVENT [Session: $SESSION_ID]" >> "$LOG_FILE"

# 可选：记录工具调用
if echo "$INPUT" | jq -e '.tool_name' > /dev/null; then
    TOOL_NAME=$(echo "$INPUT" | jq -r '.tool_name')
    echo "  → Tool: $TOOL_NAME" >> "$LOG_FILE"
fi

exit 0
```

**配置**:
```json
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "\"$HOME/.claude/templates/log-hook.sh\""
          }
        ]
      }
    ],
    "SessionEnd": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "\"$HOME/.claude/templates/log-hook.sh\""
          }
        ]
      }
    ]
  }
}
```

### 模板 2: 敏感文件保护 Hook

```python
#!/usr/bin/env python3
"""
保护敏感文件不被修改
适用于: PreToolUse
"""
import json
import sys

# 敏感文件模式列表
SENSITIVE_PATTERNS = [
    '.env',
    '.env.*',
    'secrets.yaml',
    'secrets.json',
    'config/production',
    'credentials',
]

def is_sensitive(file_path: str) -> bool:
    """检查文件路径是否敏感"""
    for pattern in SENSITIVE_PATTERNS:
        if pattern in file_path.lower():
            return True
    return False

try:
    input_data = json.load(sys.stdin)
except json.JSONDecodeError:
    sys.exit(1)

tool_name = input_data.get("tool_name", "")
tool_input = input_data.get("tool_input", {})

# 只检查 Write 和 Edit 操作
if tool_name in ("Write", "Edit"):
    file_path = tool_input.get("file_path", "")

    if is_sensitive(file_path):
        output = {
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "deny",
                "permissionDecisionReason": f"拒绝修改敏感文件: {file_path}。请使用配置文件模板或环境变量。"
            }
        }
        print(json.dumps(output))
        sys.exit(0)

sys.exit(0)
```

### 模板 3: 自动依赖安装 Hook

```bash
#!/bin/bash
# SessionStart Hook - 自动安装项目依赖
# 适用于: SessionStart

CLAUDE_ENV_FILE="$CLAUDE_ENV_FILE"

if [ -z "$CLAUDE_ENV_FILE" ]; then
    exit 0
fi

# 检测项目类型
if [ -f "package.json" ]; then
    # Node.js 项目
    if [ ! -d "node_modules" ] || [ "package.json" -nt "node_modules" ]; then
        echo "检测到 Node.js 项目，安装依赖..."
        npm install --silent

        # 设置 Node 环境
        echo 'export NODE_ENV=development' >> "$CLAUDE_ENV_FILE"
        echo 'export PATH="$PATH:./node_modules/.bin"' >> "$CLAUDE_ENV_FILE"
    fi

elif [ -f "requirements.txt" ]; then
    # Python 项目
    if [ ! -d "venv" ]; then
        echo "检测到 Python 项目，创建虚拟环境..."
        python3 -m venv venv

        # 激活虚拟环境
        echo 'source venv/bin/activate' >> "$CLAUDE_ENV_FILE"
    fi

    # 安装依赖
    if [ "requirements.txt" -nt "venv" ] 2>/dev/null; then
        echo "安装 Python 依赖..."
        source venv/bin/activate
        pip install -q -r requirements.txt
    fi

elif [ -f "go.mod" ]; then
    # Go 项目
    if [ ! -d "vendor" ]; then
        echo "检测到 Go 项目，下载依赖..."
        go mod download
    fi
fi

exit 0
```

### 模板 4: 代码统计 Hook

```python
#!/usr/bin/env python3
"""
统计代码修改
适用于: PostToolUse
"""
import json
import os
from datetime import datetime

STATS_FILE = os.path.expanduser("~/.claude/code-stats.json")

def load_stats():
    """加载现有统计"""
    try:
        with open(STATS_FILE, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_stats(stats):
    """保存统计"""
    with open(STATS_FILE, 'w') as f:
        json.dump(stats, f, indent=2)

def update_stats(stats, tool_name, file_path):
    """更新统计"""
    today = datetime.now().strftime('%Y-%m-%d')

    if today not in stats:
        stats[today] = {
            "total": 0,
            "by_type": {},
            "files_modified": set()
        }

    stats[today]["total"] += 1

    if tool_name not in stats[today]["by_type"]:
        stats[today]["by_type"][tool_name] = 0
    stats[today]["by_type"][tool_name] += 1

    if file_path:
        stats[today]["files_modified"].add(file_path)

    # 转换 set 为 list 用于 JSON 序列化
    stats[today]["files_modified"] = list(stats[today]["files_modified"])

try:
    input_data = json.load(sys.stdin)
except json.JSONDecodeError:
    sys.exit(1)

tool_name = input_data.get("tool_name", "")
tool_input = input_data.get("tool_input", {})
file_path = tool_input.get("file_path") or tool_input.get("filePath", "")

# 只统计写操作
if tool_name in ("Write", "Edit"):
    stats = load_stats()
    update_stats(stats, tool_name, file_path)
    save_stats(stats)

sys.exit(0)
```

### 模板 5: 智能停止判断 Hook（Python 版本）

```python
#!/usr/bin/env python3
"""
智能判断 Claude 是否应该停止
适用于: Stop, SubagentStop
"""
import json
import sys

def should_stop(input_data) -> tuple[bool, str]:
    """
    分析对话历史，判断是否应该停止

    返回: (should_stop, reason)
    """
    # 这里可以读取 transcript_path 进行深度分析
    # 简化版：检查是否有未完成的任务标记

    prompt = input_data.get("prompt", "")

    # 如果有明确的任务标记，不停止
    if any(phrase in prompt.lower() for phrase in [
        "继续", "next step", "下一步", "修复", "fix",
        "完成", "implement", "添加", "add"
    ]):
        return False, "检测到明确的任务指令"

    # 如果有错误关键词，不停止
    if any(phrase in prompt.lower() for phrase in [
        "错误", "error", "失败", "fail", "问题", "issue"
    ]):
        return False, "存在待解决的错误"

    # 否则可以停止
    return True, "所有任务已完成"

try:
    input_data = json.load(sys.stdin)
except json.JSONDecodeError:
    sys.exit(1)

should_stop, reason = should_stop(input_data)

if should_stop:
    # 允许停止
    sys.exit(0)
else:
    # 阻止停止
    output = {
        "decision": "block",
        "reason": f"不应停止: {reason}"
    }
    print(json.dumps(output))
    sys.exit(0)
```

---

## Part XIII: 高级技巧

### 1. Hook 链式调用

Hook 可以互相协作，实现复杂逻辑：

```bash
# PreToolUse Hook - 标记操作
export CLAUDE_OPERATION_IN_PROGRESS="$tool_name"

# PostToolUse Hook - 检查标记
if [ "$CLAUDE_OPERATION_IN_PROGRESS" = "Write" ]; then
    # 执行特定于 Write 的清理
fi
```

### 2. Hook 状态持久化

使用临时文件存储 Hook 间共享的状态：

```bash
# 状态文件
STATE_FILE="/tmp/claude-hook-state.json"

# 保存状态
echo '{"phase": "testing"}' > "$STATE_FILE"

# 读取状态
PHASE=$(jq -r '.phase' < "$STATE_FILE")
```

### 3. Hook 性能监控

```bash
#!/bin/bash
# 性能监控包装器

START_TIME=$(date +%s)

# 执行实际逻辑
YOUR_HOOK_LOGIC

END_TIME=$(date +%s)
DURATION=$((END_TIME - START_TIME))

# 记录性能
if [ $DURATION -gt 5 ]; then
    echo "警告: Hook 执行耗时 $DURATION 秒" >&2
fi

exit 0
```

### 4. Hook 调试模式

```bash
#!/bin/bash
# 调试模式开关
DEBUG="${CLAUDE_HOOK_DEBUG:-0}"

if [ "$DEBUG" = "1" ]; then
    echo "=== Hook Debug ===" >&2
    echo "Event: $CLAUDE_HOOK_EVENT" >&2
    echo "Input: $(cat)" >&2
    echo "================" >&2
fi

# Hook 逻辑...
```

使用调试模式：
```bash
export CLAUDE_HOOK_DEBUG=1
claude-code
```

### 5. Hook 条件执行

```bash
#!/bin/bash
# 只在工作时间执行 Hook
HOUR=$(date +%H)

if [ $HOUR -ge 9 ] && [ $HOUR -lt 18 ]; then
    # 工作时间逻辑
    echo "工作时间内操作" >&2
else
    # 非工作时间逻辑
    echo "非工作时间，跳过某些检查" >&2
fi

exit 0
```

---

## Part XIV: 真实场景案例

### 场景 1: 团队协作 - 代码审查自动化

**需求**: 团队成员提交代码时，自动运行审查工具

**解决方案**: PostToolUse Hook

```bash
#!/bin/bash
# .claude/hooks/code-review.sh

FILE_PATH=$(jq -r '.tool_input.file_path' < /dev/stdin)

# 只对源代码文件运行审查
case "$FILE_PATH" in
    *.py|*.js|*.ts|*.go|*.java)
        echo "运行代码审查..."

        # 运行 ESLint
        if command -v eslint &> /dev/null; then
            eslint "$FILE_PATH"
        fi

        # 运行安全检查
        if command -v bandit &> /dev/null && [[ "$FILE_PATH" == *.py ]]; then
            bandit "$FILE_PATH"
        fi

        # 输出审查报告
        if [ $? -ne 0 ]; then
            echo "❌ 代码审查发现问题，请修复后继续" >&2
            exit 2
        fi
        ;;
esac

exit 0
```

### 场景 2: 敏感项目 - 文件访问控制

**需求**: 防止 AI 访问生产配置文件

**解决方案**: PreToolUse Hook

```python
#!/usr/bin/env python3
# .claude/hooks/protect-prod-configs.py

import json
import sys

PROTECTED_PATHS = [
    'config/production',
    '.env.production',
    'secrets/',
]

def is_protected(path):
    for protected in PROTECTED_PATHS:
        if protected in path.lower():
            return True
    return False

input_data = json.load(sys.stdin)

if input_data.get('tool_name') == 'Read':
    file_path = input_data['tool_input'].get('file_path', '')

    if is_protected(file_path):
        output = {
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "deny",
                "permissionDecisionReason": "生产配置文件受保护。如需访问，请联系团队负责人。"
            }
        }
        print(json.dumps(output))
        sys.exit(0)

sys.exit(0)
```

### 场景 3: 多语言项目 - 智能格式化

**需求**: 根据文件类型自动选择格式化工具

**解决方案**: PostToolUse Hook

```bash
#!/bin/bash
# .claude/hooks/auto-format.sh

FILE_PATH=$(jq -r '.tool_input.file_path' < /dev/stdin)

case "$FILE_PATH" in
    *.js|*.jsx|*.ts|*.tsx)
        npx prettier --write "$FILE_PATH"
        ;;
    *.py)
        black "$FILE_PATH"
        ;;
    *.go)
        gofmt -w "$FILE_PATH"
        ;;
    *.rs)
        rustfmt "$FILE_PATH"
        ;;
    *.java)
        google-java-format --replace "$FILE_PATH"
        ;;
esac

exit 0
```

### 场景 4: 学习项目 - 对话记录

**需求**: 记录所有 Claude 交互用于学习分析

**解决方案**: UserPromptSubmit + SessionEnd Hooks

```bash
#!/bin/bash
# .claude/hooks/learning-log.sh

LOG_DIR="$HOME/.claude/learning-logs"
DATE=$(date +%Y-%m-%d)
mkdir -p "$LOG_DIR"

# 从 JSON 输入提取信息
PROMPT=$(jq -r '.prompt' < /dev/stdin)
EVENT=$(jq -r '.hook_event_name' < /dev/stdin)

# 写入日志
echo "[$DATE] $EVENT" >> "$LOG_DIR/sessions.log"
echo "Prompt: $PROMPT" >> "$LOG_DIR/sessions.log"
echo "---" >> "$LOG_DIR/sessions.log"

exit 0
```

**配置**:
```json
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "\"$HOME/.claude/hooks/learning-log.sh\""
          }
        ]
      }
    ],
    "SessionEnd": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "\"$HOME/.claude/hooks/learning-log.sh\""
          }
        ]
      }
    ]
  }
}
```

---

## 参考资源

- [Claude Code Hooks 官方文档](https://code.claude.com/docs/en/hooks)
- [Claude Code Hooks 指南](https://code.claude.com/docs/en/hooks-guide)
- [Claude Code Hooks 进阶示例](https://github.com/disler/claude-code-hooks-mastery)
- [Claude Code API 参考](https://code.claude.com/docs/en/cli-reference)

---

> [!success] 文档状态
> **创建日期**: 2025-01-07
> **最后更新**: 2025-01-07
> **适用版本**: Claude Code 最新版
> **文档版本**: v1.1
> **状态**: 包含实战案例和模板库
