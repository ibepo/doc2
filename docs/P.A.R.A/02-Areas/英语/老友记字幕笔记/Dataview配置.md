---
# Dataview 配置 - 老友记学习笔记

## 显示选项

```dataview
TABLE show_id AS "ID", file.链接 AS "链接", show, season, episode, episode_title, created, language
FROM "02-Areas/英语/老友记字幕笔记"
WHERE show = "Friends"
SORT season ASC, episode ASC
```

## 查询视图

### 1. 所有剧集概览

```dataview
TABLE
  season AS "季数",
  episode AS "集数",
  episode_title AS "标题",
  air_date AS "首播日期",
  file.链接 AS "查看",
  created AS "创建日期"
FROM "02-Areas/英语/老友记字幕笔记"
WHERE show = "Friends"
SORT season ASC, episode ASC
```

### 2. 学习进度追踪

```dataview
TABLE WITHOUT ID
  season AS "季数",
  episode AS "集数",
  episode_title AS "标题",
  created AS "创建日期"
FROM "02-Areas/英语/老友记字幕笔记"
WHERE contains(tags, "#英语学习")
SORT created DESC
```

### 3. 待办任务汇总

```dataview
TASK
WHERE completed = false
```

### 4. 按主题分组查看

#### 4.1 罗斯与卡罗尔（离婚、怀孕）

```dataview
TABLE
  episode AS "集数",
  episode_title AS "标题",
  file.链接 AS "查看"
FROM "02-Areas/英语/老友记字幕笔记"
WHERE contains(content, "Carol") OR contains(content, "pregnant") OR contains(content, "Susan")
```

#### 4.2 瑞秋的成长

```dataview
TABLE
  episode AS "集数",
  episode_title AS "标题",
  file.链接 AS "查看"
FROM "02-Areas/英语/老友记字幕笔记"
WHERE contains(content, "Rachel") AND (contains(content, "ring") OR contains(content, "job") OR contains(content, "independent"))
```

#### 4.3 约会与浪漫

```dataview
TABLE
  episode AS "集数",
  episode_title AS "标题",
  file.链接 AS "查看"
FROM "02-Areas/英语/老友记字幕笔记"
WHERE contains(content, "dating") OR contains(content, "kiss") OR contains(content, "relationship")
```

#### 4.4 幽默与喜剧

```dataview
TABLE
  episode AS "集数",
  episode_title AS "标题",
  file.链接 AS "查看"
FROM "02-Areas/英语/老友记字幕笔记"
WHERE contains(content, "funny") OR contains(content, "[!note]") OR contains(content, "[!quote]")
```

### 5. 词汇管理

#### 5.1 查看所有生词

```dataview
TABLE
  episode AS "集数",
  episode_title AS "标题",
  content AS "内容预览"
FROM "02-Areas/英语/老友记字幕笔记"
WHERE contains(content, "## 生词汇总")
SORT season ASC, episode ASC
```

#### 5.2 按首字母查找生词

需要在生词汇表中添加 `首字母` 字段才能使用此功能。

```dataview
TABLE word, 首字母, episode
FROM "02-Areas/英语/老友记字幕笔记"
WHERE contains(content, "| 单词")
```

### 6. 经典台词收集

```dataview
LIST
FROM "02-Areas/英语/老友记字幕笔记"
WHERE contains(content, "[!quote]")
```

### 7. 学习笔记与提示

#### 7.1 所有学习提示

```dataview
LIST
FROM "02-Areas/英语/老友记字幕笔记"
WHERE contains(content, "[!tip]") OR contains(content, "[!learn]") OR contains(content, "[!insight]")
```

#### 7.2 文化注解

```dataview
LIST
FROM "02-Areas/英语/老友记字幕笔记"
WHERE contains(content, "[!culture]") OR contains(content, "[!note]")
```

### 8. 进度统计

#### 8.1 已完成剧集数量

```dataview
TABLE
  season AS "季数",
  count(episode) AS "集数"
FROM "02-Areas/英语/老友记字幕笔记"
WHERE show = "Friends"
GROUP BY season
```

#### 8.2 按标签统计

```dataview
TABLE
  tags AS "标签",
  count(tags) AS "文档数"
FROM "02-Areas/英语/老友记字幕笔记"
GROUP BY tags
FLATTEN tags AS tag
```

### 9. 今日学习

```dataview
TABLE
  episode AS "集数",
  episode_title AS "标题",
  file.链接 AS "查看",
  created AS "创建时间"
FROM "02-Areas/英语/老友记字幕笔记"
WHERE created >= date(today) AND created < date(today) + dur(1 day)
SORT created DESC
```

### 10. 搜索功能

#### 10.1 搜索内容

```dataview
TABLE
  file.链接 AS "链接",
  episode_title AS "剧集",
  content AS "包含内容的行"
FROM "02-Areas/英语/老友记字幕笔记"
WHERE contains(content, "{{query}}")
LIMIT 50
```

#### 10.2 搜索标签

```dataview
TABLE
  file.链接 AS "链接",
  episode_title AS "剧集",
  tags AS "标签"
FROM "02-Areas/英语/老友记字幕笔记"
WHERE contains(tags, "{{query}}")
```

### 11. 快速访问

#### 11.1 最近更新的5集

```dataview
TABLE
  season AS "季数",
  episode AS "集数",
  episode_title AS "标题",
  file.链接 AS "查看",
  modified AS "更新时间"
FROM "02-Areas/英语/老友记字幕笔记"
SORT modified DESC
LIMIT 5
```

#### 11.2 未完成的剧集

```dataview
TABLE
  season AS "季数",
  episode AS "集数",
  episode_title AS "标题",
  file.链接 AS "查看"
FROM "02-Areas/英语/老友记字幕笔记"
WHERE created < date("2025-01-01")
SORT created ASC
```

### 12. 词汇统计视图

#### 12.1 按字母分组词汇

需要在文档中标记每个生词的字母。

```dataview
TABLE
  字母,
  count(*) AS "词汇数"
FROM "02-Areas/英语/老友记字幕笔记"
WHERE contains(content, "首字母: [A-Z]")
GROUP BY 字母
SORT 字母 ASC
```

#### 12.2 学习重点词汇

```dataview
LIST
FROM "02-Areas/英语/老友记字幕笔记"
WHERE contains(content, "[!vocab]")
```

---

## 使用说明

### 基础使用

1. **启用 Dataview 插件**：在 Obsidian 设置中启用 Dataview 插件
2. **安装后重启**：重启 Obsidian 使配置生效
3. **在侧边栏查看**：Dataview 视图会出现在 Obsidian 左侧边栏

### 查询使用

1. **复制查询**：直接复制上面的查询代码块
2. **粘贴到 Dataview**：在 Dataview 面板中粘贴查询
3. **自定义查询**：可以根据需要修改 `WHERE` 条件

### 标签建议

在文档中使用这些标签以获得更好的查询效果：

- `#英语学习` - 标记正在学习的内容
- `#Friends` - 标记《老友记》相关
- `#词汇` - 标记词汇表（如果单独创建）
- `#文化` - 标记文化背景知识
- `#语法` - 标记语法知识（如果单独创建）

### 视图说明

- **TABLE 视图**：以表格形式展示数据，适合查看剧集列表、词汇表
- **LIST 视图**：以列表形式展示，适合查看台词、笔记
- **TASK 视图**：专门用于显示待办任务（需要文档中有 `completed` 字段）
- **CALENDAR 视图**：以日历形式显示（适合有日期的任务）

### 高级技巧

1. **创建仪表盘**：将常用查询保存为 Dataview 书签
2. **组合查询**：使用 `AND`、`OR` 组合多个条件
3. **日期查询**：
   - `created >= date("2026-01-01")` - 某日期之后创建的
   - `created = date(today)` - 今天创建的
   - `created >= date(today) - dur(7 day)` - 最近7天创建的
4. **文本搜索**：使用 `contains(content, "关键词")` 搜索文档内容

### 字段说明

#### Frontmatter 字段（自动识别）

| 字段 | 类型 | 说明 |
|------|------|------|
| `title` | 文本 | 文档标题 |
| `show` | 文本 | 节目名称（如 "Friends"） |
| `season` | 数字 | 季数 |
| `episode` | 数字 | 集数 |
| `episode_title` | 文本 | 英文集标题 |
| `air_date` | 日期 | 首播日期 |
| `language` | 文本 | 语言 |
| `tags` | 标签数组 | 标签列表（用 `#` 或 `[]` 格式） |
| `created` | 日期 | 创建日期 |
| `modified` | 日期 | 修改日期 |

#### 特殊字段（需要在 Frontmatter 中添加）

| 字段 | 类型 | 说明 | 示例 |
|------|------|------|------|
| `difficulty` | 文本 | 难度（简单/中等/困难） | `difficulty: 中等` |
| `status` | 文本 | 学习状态（进行中/已完成） | `status: 进行中` |
| `review_count` | 数字 | 复习次数 | `review_count: 3` |
| `favorite` | 布尔值 | 是否收藏 | `favorite: true` |

---

## 自定义视图示例

### 按难度筛选

```dataview
TABLE season, episode, episode_title, difficulty, file.链接
FROM "02-Areas/英语/老友记字幕笔记"
WHERE difficulty = "简单"
```

### 按状态筛选

```dataview
TABLE season, episode, episode_title, status, created
FROM "02-Areas/英语/老友记字幕笔记"
WHERE status = "进行中"
SORT created DESC
```

### 收藏的内容

```dataview
TABLE
  season AS "季数",
  episode AS "集数",
  episode_title AS "标题",
  favorite AS "收藏",
  file.链接 AS "查看"
FROM "02-Areas/英语/老友记字幕笔记"
WHERE favorite = true
```

### 需要复习的内容

```dataview
TABLE season, episode, episode_title, review_count, last_reviewed
FROM "02-Areas/英语/老友记字幕笔记"
WHERE review_count > 0 AND last_reviewed < date(today) - dur(14 day)
ORDER BY review_count DESC
```

---

## 实用查询组合

### 1. 今天学了什么？

```dataview
TABLE
  created AS "时间",
  season AS "季数",
  episode AS "集数",
  episode_title AS "标题",
  file.链接 AS "查看"
FROM "02-Areas/英语/老友记字幕笔记"
WHERE created = date(today)
ORDER BY created DESC
```

### 2. 本周学了什么？

```dataview
TABLE
  created AS "时间",
  season AS "季数",
  episode AS "集数",
  episode_title AS "标题",
  file.链接 AS "查看"
FROM "02-Areas/英语/老友记字幕笔记"
WHERE created >= date(today) - dur(7 day)
ORDER BY created DESC
```

### 3. 哪些集还没学？

```dataview
TABLE
  season AS "季数",
  count(episode) AS "集数"
FROM "02-Areas/英语/老友记字幕笔记"
WHERE season = 1
HAVING count(episode) < 24
```

### 4. 找出所有关于 Ross 的对话

```dataview
LIST
FROM "02-Areas/英语/老友记字幕笔记"
WHERE contains(content, "**Ross**:") AND !contains(content, "[!note]")
```

### 5. 找出所有 Callout 标注

```dataview
TABLE
  file.链接 AS "链接",
  episode AS "集数",
  type AS "标注类型"
FROM "02-Areas/英语/老友记字幕笔记"
WHERE contains(content, "[!")
```

### 6. 统计已完成的待办

```dataview
TABLE
  episode AS "集数",
  count(*) AS "完成数量"
FROM "02-Areas/英语/老友记字幕笔记"
WHERE completed = true
GROUP BY episode
```

---

## 提示与最佳实践

### 文档创建建议

1. **保持一致的 Frontmatter 格式**
2. **使用标准的标签系统**
3. **添加有用的元数据字段**（如 difficulty, status）
4. **为生词添加首字母标记**

### 学习工作流

1. **观看剧集** → 打开对应集的文档
2. **标记生词** → 在 `[!vocab]` Callout 中添加生词
3. **添加笔记** → 在 `[!learn]` 或 `[!tip]` 中记录学习心得
4. **更新状态** → 在 Frontmatter 中更新 `status` 字段
5. **定期复习** → 使用 Dataview 查找需要复习的内容

### 查询优化

1. **使用索引字段**：优先使用 `season`、`episode` 等数字字段
2. **限制结果数量**：使用 `LIMIT` 避免过多数据
3. **排序合理**：按时间或集数排序
4. **组合查询**：用括号分组条件以提高性能

---

## 常见问题

### Q: Dataview 找不到我的笔记？

**A**: 检查以下几点：
1. Frontmatter 格式是否正确（用 `---` 包围）
2. 文件是否在正确的文件夹中
3. 文件扩展名是否为 `.md`
4. Dataview 插件是否已安装并启用

### Q: 查询太慢怎么办？

**A**:
1. 使用更具体的 `WHERE` 条件
2. 添加 `LIMIT` 限制结果数量
3. 避免使用 `contains(file.content, ...)` 改用 `contains(content, ...)`

### Q: 如何添加自定义字段？

**A**: 在文档的 Frontmatter 中添加：
```yaml
---
title: "老友记 S01E01"
difficulty: 简单
status: 进行中
review_count: 0
favorite: false
---
```

### Q: 如何快速切换视图？

**A**: 
1. 将常用查询复制到 Dataview 查询框
2. 使用 Dataview 的书签功能保存常用查询
3. 创建不同的查询文件作为模板

---

## 更新日志

- 2026-01-09: 创建初始配置文件
- 包含 5 个查询视图模板
- 添加文档创建指南
- 添加使用说明和最佳实践

---

## 联系与反馈

如果需要添加更多查询或遇到问题，请检查：
1. [Obsidian Dataview 官方文档](https://blacksmithgu.github.io/obsidian-dataview/)
2. [Dataview 查询语法参考](https://blacksmithgu.github.io/obsidian-dataview/query/queries.html)
