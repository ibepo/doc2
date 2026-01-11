# Rive Layouts 布局系统分析

> 基于 [Rive](./Rive.md) 快速入门教程的布局方法论总结

---

## 教程概览

### 项目目标
创建一个**可交互的摩托车选择菜单**，包含：
- 动态背景切换（4 种颜色的摩托车）
- 属性数据显示（速度、加速、操控等）
- 可点击的列表项（支持 hover 效果）
- Intro/Outro 动画效果

### 教程章节结构

| 章节 | 内容 | 关键技术 |
|------|------|---------|
| **1. 界面介绍** | Rive Editor 界面、Artboard、Data Panel | 基础操作 |
| **2. 组件设计** | Item、Stats、Start Button、Background | Component 系统 |
| **3. Layouts 布局** | 行列布局、嵌套、响应式设计 | **重点** |
| **4. 数据绑定** | ViewModel、属性绑定 | 数据驱动 |
| **5. 状态机** | Timeline、状态转换、条件判断 | 动画逻辑 |
| **6. 列表功能** | Artboard List、Instance | 动态列表 |
| **7. 交互逻辑** | Hover、Click、音效 | Listener |
| **8. 进场/退场** | Intro/Outro 动画 | 综合应用 |

### 完整组件树

```
Menu Artboard (500×500)
│
├── Background Component (Leaf, Cover)
│   └── Solo (4 张摩托车图)
│
└── Main Column (Fill, Padding: 50)
    │
    ├── Header Row
    │   ├── Arrows Component
    │   ├── "Select Your Moto" Text
    │   └── "Class" Text
    │
    ├── Item List (Artboard List, 4 项)
    │   └── Item Component × 4
    │       ├── Helmet Image
    │       ├── Name / Class Text
    │       └── Description (点击展开)
    │
    └── Stats Column
        ├── Power (进度条 + 数值)
        ├── Speed
        ├── Acceleration
        └── Handling
```

### 学习路径建议

```
新手路径：
1. 熟悉 Rive Editor 界面
2. 掌握 Layouts 基础（Row/Column）
3. 创建简单组件
4. 添加动画
5. 学习数据绑定
6. 掌握状态机
7. 实现交互逻辑

进阶路径：
1. Layouts 高级技巧（响应式、嵌套）
2. Instance 复用与差异化
3. State Machine 层级设计
4. Listener 与事件系统
5. 列表与动态内容
6. 综合项目实战
```

---

## 一、Rive Layouts 核心方法论

### 1.1 自底向上的构建策略

> *"I usually start by arranging the smallest pieces of my design into layouts and then work my way out."*

**构建示例**：

```
Item Column (最终容器)
│
├── Image and Text Row
│   ├── Image Layout
│   └── Text Column
│       ├── Item Name (30pt Bold)
│       └── Item Class (20pt)
│
└── Text Description
```

**构建步骤**：
1. 两段文字 → 文字列
2. 文字列 + 图片 → 图片文字行
3. 图片文字行 + 描述文字 → 项目列

---

### 1.2 父子层级控制原则

| 父级控制属性 | 作用 | 设置位置 |
|-------------|------|---------|
| **Gap（间距）** | 控制子元素之间的垂直/水平间距 | 父级 Layout 属性 |
| **Fit（适应）** | 控制子元素如何填充空间 | 子级 Layout 属性 |
| **Alignment（对齐）** | 控制子元素在容器内的位置 | 父级 Layout 属性 |
| **Padding（内边距）** | 控制内容与容器边缘的距离 | 父级 Layout 属性 |

---

### 1.3 Fit 适配模式详解

```
┌────────────────────────────────────────────────────┐
│                    Fit 模式                         │
├────────────────────────────────────────────────────┤
│  Hug（拥抱）   │ 自适应子元素大小                   │
│  Fill（填充）  │ 填满父容器剩余空间（可多个元素共享）│
│  Fixed（固定） │ 固定大小                           │
│                 ├─ Pixel（绝对像素）               │
│                 └─ Percent（相对百分比%）          │
└────────────────────────────────────────────────────┘
```

**典型组合**：
- 列容器：`Fill width + Fill height` → 填满父容器
- 子元素：`Fixed 100% width` → 随容器缩放
- 单独子元素：`Fill width` → 占据剩余空间

---

### 1.4 布局嵌套模式

```
Menu Artboard (根容器)
│
├── Background Component (Leaf 模式, Cover)
│
└── Main Column (Fill 父容器)
    │
    ├── Header Row
    │   ├── Arrows
    │   └── Title Text ("Select Your Moto")
    │
    ├── Item List (Artboard List)
    │   └── Item Component × 4
    │
    └── Stats Column
        └── Stats Component
```

---

## 二、跨平台布局类比

### 2.1 概念对照表

| 概念 | Rive | Android XML | Android (Jetpack Compose) | iOS (SwiftUI) | iOS (UIKit) | Figma |
|------|------|-----------|--------------------------|---------------|-------------|-------|
| **行布局** | Row Layout | `LinearLayout (horizontal)` | `Row()` | `HStack` | `UIStackView(axis: .horizontal)` | Auto Layout (水平) |
| **列布局** | Column Layout | `LinearLayout (vertical)` | `Column()` | `VStack` | `UIStackView(axis: .vertical)` | Auto Layout (垂直) |
| **填充** | Fill | `match_parent` / `weight` | `fillMaxWidth()` | `.frame(maxWidth: .infinity)` | Content Hugging Priority | Fill Container |
| **包裹** | Hug | `wrap_content` | `wrapContentSize()` | 自适应 | Intrinsic Content Size | Auto Frame |
| **间距** | Gap | `margin` / `space` (RecyclerView) | `arrangement.spacedBy()` | `.spacing()` | `.spacing` | Space Between |
| **内边距** | Padding | `padding` | `padding()` | `.padding()` | `.layoutMargins` | Padding |
| **绝对定位** | Absolute Positioning | `layout_marginLeft/Top` | `offset()` | `.position()` | Frame origin | X/Y + Pin |
| **嵌套** | Layout in Layout | View Hierarchy | Composable 嵌套 | HStack/VStack 嵌套 | View Hierarchy | Frame Groups |
| **列表** | Artboard List | `RecyclerView` | `LazyColumn()` | `List` | `UITableView` | Replicate |

---

### 2.2 代码示例对比

#### 场景：创建一个带图片和文字的卡片

**Rive**:
```
Item Column (Padding: 10, Gap: 10)
├── Image and Text Row (Gap: 10)
│   ├── Image (Fill width)
│   └── Text Column (Gap: 0)
│       ├── Title (30pt Bold)
│       └── Subtitle (20pt)
└── Description
```

**Android XML**:
```xml
<LinearLayout
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:orientation="vertical"
    android:padding="10dp">

    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:orientation="horizontal">

        <ImageView
            android:layout_width="0dp"
            android:layout_height="wrap_content"
            android:layout_weight="1" />

        <LinearLayout
            android:layout_width="0dp"
            android:layout_height="wrap_content"
            android:layout_weight="2"
            android:orientation="vertical">

            <TextView
                android:text="Title"
                android:textSize="30sp"
                android:textStyle="bold" />

            <TextView
                android:text="Subtitle"
                android:textSize="20sp" />
        </LinearLayout>
    </LinearLayout>

    <TextView
        android:text="Description" />
</LinearLayout>
```

**Android (Jetpack Compose)**:
```kotlin
Column(
    modifier = Modifier.padding(10.dp),
    verticalArrangement = Arrangement.spacedBy(10.dp)
) {
    Row(
        horizontalArrangement = Arrangement.spacedBy(10.dp)
    ) {
        Image(
            modifier = Modifier.weight(1f) // Fill width
        )
        Column(
            verticalArrangement = Arrangement.spacedBy(0.dp)
        ) {
            Text(fontSize = 30.sp, fontWeight = Bold)
            Text(fontSize = 20.sp)
        }
    }
    Text("Description")
}
```

**iOS (SwiftUI)**:
```swift
VStack(spacing: 10) {
    HStack(spacing: 10) {
        Image().frame(maxWidth: .infinity)
        VStack(spacing: 0) {
            Text("Title").font(.system(size: 30, weight: .bold))
            Text("Subtitle").font(.system(size: 20))
        }
    }
    Text("Description")
}
.padding(10)
```

**Figma (Auto Layout)**:
```
Frame (Auto Layout, Vertical, Padding: 10, Gap: 10)
├── Frame (Auto Layout, Horizontal, Gap: 10)
│   ├── Image (Fill container)
│   └── Frame (Auto Layout, Vertical, Gap: 0)
│       ├── Title (30, Bold)
│       └── Subtitle (20)
└── Description
```

---

## 三、Rive 独特特性

### 3.1 与传统平台差异

| 特性 | Rive | Android XML | Android/iOS (现代框架) | Figma |
|------|------|-------------|---------------------|-------|
| **动画优先** | 布局为动画服务，原生支持 | 需要代码实现（Animator/MotionLayout） | 部分支持（SwiftUI动画） | 导出前静态 |
| **百分比单位** | 广泛使用 % 做响应式 | 仅 ConstraintLayout 支持（`app:layout_constraintWidth_percent`） | 部分支持（dp%/多权重） | 仅约束支持 |
| **Instance 系统** | 同一组件多实例独立布局 | 通过 RecyclerView ViewHolder 复用 | RecyclerView 复用 | Components/Instances |
| **ViewModel 绑定** | 布局属性可数据绑定 | 需要 DataBinding/ViewBinding | DataBinding/State | Variables |
| **Leaf 模式** | 特殊容器模式 | FrameLayout + scaleType | 无对应 | Frame |
| **运行时动态性** | 可通过数据绑定实时调整布局 | 需要代码动态修改 View 属性 | 支持动态更新 | 静态导出 |

### 3.2 Rive 专属模式

#### Node vs Leaf 模式
```
Node 模式：组件作为容器，可嵌套子元素
Leaf 模式：组件作为叶子，整体适配空间

示例：Background 使用 Leaf + Cover 适配
```

#### Solo 可见性控制
```
Solo Group：多个图层，仅一个可见
→ 常用于状态切换（如不同颜色的背景图）
```

---

## 四、实用指导原则

### 4.1 推荐做法 ✅

| 原则 | 说明 | 示例 |
|------|------|------|
| **从小到大构建** | 先组合最小元素，再向外扩展 | 文字→列→行→列 |
| **合理嵌套** | 避免过深层级（建议 ≤ 3 层） | Column > Row > Elements |
| **Fill + Fixed 混合** | 固定关键尺寸，其余自适应 | 固定宽度 100%，高度自适应 |
| **Gap 统一管理** | 间距在父级统一控制 | 父级 Gap: 10，子级 Gap: 0 |
| **对齐优先使用按钮** | 双击切换对齐模式 | 居中 → 分散对齐 |

### 4.2 常见陷阱 ⚠️

| 问题 | 原因 | 解决方案 |
|------|------|---------|
| **动画时布局失效** | `Fill` 模式不支持绝对定位动画 | 改用 `Fixed 100%` + 绝对定位 |
| **子元素溢出容器** | 父容器用 `Hug`，子元素用 `Fill` 失效 | 父级改用 `Fill` |
| **间距不生效** | 在子元素上设置 Gap，应该在父级 | 移到父级 Layout 的 Gap |
| **布局不响应** | 忘记关闭 Absolute Positioning | 手动关闭后再放入布局 |
| **列表预览消失** | Preview Bound Values 开关冲突 | 运行时关闭，编辑时开启 |

### 4.3 动画与布局冲突解决

```
问题：需要动画元素位置，但 Fill 模式不支持绝对定位

解决流程：
1. 将元素 Fit 从 Fill 改为 Fixed
2. 单位从 Pixel 改为 Percent 100%
3. 开启 Absolute Positioning
4. 现在可以动画 Y Position 了
```

---

## 五、快捷键对比

| 操作 | Rive | Figma |
|------|------|-------|
| 创建布局 | `Shift + L` | `Shift + A` |
| 循环切换对齐 | 双击对齐图标 | 点击对齐选项 |
| 预览绑定值 | `Cmd + B` | 无 |
| 选择图层（层级中） | `Cmd + 点击` | `Cmd + 点击` |
| 显示所有关键帧 | `U` | 无 |

---

## 六、实战案例

### 6.1 响应式卡片组件

**需求**：创建一个卡片，图片占 1/3，文字占 2/3，整体宽度自适应

```
Card Column (Padding: 10, Gap: 10)
│
└── Content Row (Gap: 10, Fill 父容器)
    ├── Image (Fixed 33% width)
    └── Text Column (Fill width)
        ├── Title
        └── Description
```

**关键设置**：
- Content Row: `Fill width + Fill height`
- Image: `Fixed 33% width, Fill height`
- Text Column: `Fill width, Fill height`

### 6.2 自适应列表项

**需求**：列表项点击后展开显示描述，其他项收起

```
Item List (Artboard List, Gap: 10)
└── Item Component × N
    ├── Normal State (固定高度)
    └── Expanded State (可变高度, 显示描述)
```

**关键点**：
- 使用 Artboard List 而非手动排列
- State Machine 控制状态切换
- 列表自动重新计算布局

---

## 七、总结

Rive Layouts 是一个**介于传统 UI 框架和设计工具之间**的布局系统：

### 7.1 Rive Layouts 优势

| 优势 | 说明 |
|------|------|
| **可视化 + 严谨性** | 既有代码的 Fit/Gap/Align 严谨性，又有可视化工具的直观性 |
| **动画友好** | 布局为动画服务，支持运行时动态调整 |
| **响应式优先** | 百分比单位 + Fill/Hug 模式天然支持多尺寸 |
| **数据驱动** | ViewModel 绑定实现属性实时控制 |

### 7.2 Rive Layouts 局限

| 局限 | 说明 |
|------|------|
| **学习曲线** | Node/Leaf/Instance 等概念需要理解 |
| **动画约束** | 某些布局模式不支持动画 |
| **工具依赖** | 必须在 Rive Editor 中操作 |

### 7.3 与 Android XML 核心差异

| 维度 | Rive | Android XML |
|------|------|-------------|
| **学习曲线** | 中等（需要理解可视化概念：Fill/Hug/Gap/Leaf/Node） | 中等（XML 语法直观，理解 View 体系即可） |
| **开发效率** | 可视化拖拽，**适合设计师**主导 | 代码编写，**适合开发者**主导 |
| **动画支持** | 原生支持，无需代码（设计师直接在工具中完成） | 需要编写动画代码（ValueAnimator/ObjectAnimator/MotionLayout） |
| **响应式能力** | 百分比 + Fill/Hug 强大，天然响应式 | 需要多种布局组合（LinearLayout + ConstraintLayout + dp/sp） |
| **团队协作** | 设计主导，开发集成运行时 | 开发主导，设计交付静态稿 |
| **性能** | 运行时渲染，动画流畅 | 编译时生成，原生性能 |
| **动态性** | 可通过数据绑定实时修改布局属性 | 需要代码动态修改 View 属性或重新布局 |
| **灵活性** | 专注于动画交互界面 | 通用型，可构建任意类型界面 |

### 7.4 关键概念映射速查

| Rive | Android XML | 等价关系 |
|------|-------------|----------|
| `Fill` | `match_parent` / `weight` | 填满父容器/按权重分配 |
| `Hug` | `wrap_content` | 根据内容自适应 |
| `Gap` | `margin` | 间距控制 |
| `Padding` | `padding` | 内边距 |
| `Fixed 100%` | ConstraintLayout 的 `app:layout_constraintWidth_percent="1.0"` | 百分比尺寸 |
| `Row Layout` | `LinearLayout (horizontal)` | 水平容器 |
| `Column Layout` | `LinearLayout (vertical)` | 垂直容器 |
| `Artboard List` | `RecyclerView` + `Adapter` | 动态列表 |
| `Leaf 模式` | `FrameLayout` + `scaleType` | 图片适配模式 |

### 7.5 适用场景推荐

| 场景 | 推荐方案 | 原因 |
|------|---------|------|
| **游戏 UI / 动效原型** | **Rive** | 原生动画支持，设计师可直接实现 |
| **标准 App 界面** | **Android XML** | 生态成熟，开发者熟悉，性能最优 |
| **交互式营销页面** | **Rive** | 视觉效果丰富，动画流畅 |
| **复杂业务表单** | **Android XML** | 布局稳定，易于维护 |
| **跨平台动画组件** | **Rive** | 一套设计，多平台运行 |

**适用场景**：需要动画的交互界面（游戏 UI、动效原型、交互组件）

---

**参考资料**：[Rive.md](./Rive.md) | [Rive 官方文档](https://rive.app)
