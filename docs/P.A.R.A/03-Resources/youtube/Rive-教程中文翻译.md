# Rive 快速入门教程 - 中文翻译

> 原始视频教程文字记录翻译
> 项目：创建一个可交互的摩托车选择菜单

---

## 一、教程介绍

### 1.1 项目概述

欢迎来到这个 Rive 快速入门教程。今天我们要制作一个**可交互的、可调整大小的菜单**，可以实时用于你的应用程序、网站或游戏中。

### 1.2 学习路径

本教程分为以下阶段：

1. **布局设计** - 使用 Layouts 创建整个设计
2. **动画** - 添加动画效果
3. **数据绑定** - 实现 ViewModel 和属性绑定
4. **状态机** - 实现状态机逻辑
5. **交互** - 添加用户交互功能
6. **列表功能** - 使用 Artboard List
7. **进出场动画** - 完成 Intro/Outro 动画

---

## 二、Rive 编辑器界面介绍

### 2.1 界面布局

这是 Rive 编辑器。首先，我们需要创建一个画板（Artboard），我将使用默认的 500×500 像素。

**左侧面板**：
- **Artboards Hierarchy（画板层级）** - 显示当前画板的结构
- **Assets Panel（资源面板）** - 管理导入的图片等资源
- **Data Panel（数据面板）** - 包含 ViewModel（视图模型）

**右侧面板**：
- **Inspector（检查器）** - 显示选中图层的所有属性

### 2.2 创建菜单画板

1. 创建新的 Artboard，命名为 **"Menu"**
2. 删除背景颜色，从空白画板开始
3. 在 Data Panel 中，将 ViewModel 重命名为 **"Menu ViewModel"**

### 2.3 ViewModel 简介

ViewModel 是数据绑定功能的一部分。本质上，ViewModel 是一个创建和控制各种属性的地方，这些属性可以：
- 作为设计的一部分使用
- 作为状态机中的条件使用
- 通过代码实时控制

---

## 三、创建第一个组件 - Item（项目）

### 3.1 创建 Item 组件

首先，我们需要创建多个不同的组件，然后将它们嵌套在 Menu Artboard 的布局中。

**步骤**：
1. 按下 `A` 键，点击并拖动创建新的 Artboard
2. 命名为 **"Item"**
3. 删除背景
4. 点击组件符号（将其转换为组件）

### 3.2 导入资源

打开 Assets Panel，导入四张头盔图片：
- 黑色头盔 (250×250)
- 蓝色头盔 (250×250)
- 绿色头盔 (250×250)
- 白色头盔 (250×250)

将黑色头盔拖到 Item 组件中，放置在左侧。

### 3.3 添加文本

创建三个文本元素（快捷键 `T`）：

1. **Item Name**（项目名称）
   - 字体大小：30
   - 样式：粗体

2. **Item Class**（项目类别）
   - 字体大小：20

3. **Description**（描述文本）
   - 长描述文本
   - 放置在其他元素下方

---

## 四、Layouts 布局系统

### 4.1 什么是 Layouts？

**Layouts** 是 Rive 中的一个设计系统，允许你：
- 将元素排列成行或列
- 嵌套布局：列里放行，行里放列
- 创建可以调整大小和重新流动的设计
- 根据组件、画板甚至设备大小自动响应

### 4.2 构建策略

**自底向上**：从最小的设计片段开始排列，然后向外扩展。

**Item 组件的布局结构**：
```
Item Column
├── Image and Text Row
│   ├── Image
│   └── Text Column
│       ├── Item Name
│       └── Item Class
└── Text Description
```

### 4.3 创建文本列布局

1. 选中两个文本元素
2. 按下 `Shift + L` 创建布局
3. Rive 自动判断为列布局（因为元素上下叠放）
4. 命名为 **"Text Column"**
5. 设置垂直间距为 0

> 注意：两个文本元素也被自动包裹在各自的布局中。Text Column 是它们的父级，从中可以控制子元素之间的垂直间距。

### 4.4 创建图片文字行布局

1. 选中文本列和图片
2. 按下 `Shift + L` 创建行布局
3. 命名为 **"Image and Text Row"**
4. 设置水平间距为 10 像素

### 4.5 创建项目列布局

1. 选中图片文字行和描述文本
2. 按下 `Shift + L` 创建列布局
3. 命名为 **"Item Column"**
4. 设置垂直间距为 10 像素

### 4.6 调整画板大小

1. 调整 Artboard 大小以容纳描述文本
2. 设置 Item Column 位置为 (0, 0)
3. 让 Item Column 完美适配组件大小

### 4.7 Fit 适配设置

Item Column 的 Fit 设置当前是 "Hug width" 和 "Hug height"（拥抱子布局）。

**修改为固定大小**：
1. 改为 Fixed width 和 Fixed height
2. 点击像素图标，改为 **Percent（百分比）**
3. 设置为 **100%**

这样，无论 Item Component 是什么大小，Item Column 都会相应变化。

### 4.8 添加内边距和背景

1. 选中 Item Column
2. 设置 Padding：左右 10，上下 10
3. 添加背景颜色

为描述文本添加独立背景：
1. 选中描述文本
2. 按 `Shift + L` 包裹在布局中
3. 命名为 **"Text Description"**
4. 设置 Fit 为 Fill width 和 Fill height（填充父布局）
5. 添加 Padding
6. 添加背景颜色

---

## 五、创建 Stats 组件（属性显示）

### 5.1 创建 Stats 组件

1. 按下 `A` 创建新的 Artboard
2. 命名为 **"Stats"**
3. 删除背景，设置为组件

### 5.2 创建进度条

1. 使用矩形工具创建白色矩形
2. 复制（`Cmd + D`），移到右侧
3. 改为黑色矩形

**将两个矩形转换为进度条**：
1. 同时选中两个矩形
2. 按 `Shift + L` 放入行布局
3. 关闭绝对定位
4. 设置宽度为 Fill parent layout（填充父布局）
5. 设置子元素间距为 0
6. 白色条：Fixed width（百分比）
7. 黑色条：Fill remaining width（填充剩余宽度）

这样，数据绑定时只需控制像素值就能控制进度条。

### 5.3 添加文本标签

1. 创建两个文本元素
2. 复制一个，移到右侧，改为数字
3. 将两个文本放入行布局
4. 将两个行放入列布局
5. 调整顺序：文本在条形图上方
6. 设置两个行之间的垂直间距为 0

**分散文本**：
1. 选中文本的行
2. 设置宽度为 Fill parent
3. 删除水平间距
4. 点击对齐按钮两次：第一次居中，第二次分散

### 5.4 创建标题

1. 创建组件标题
2. 将标题和之前的行放入列
3. 标题置于顶部

### 5.5 复制属性列

1. 选中列，复制 3 次（共 4 个属性）
2. 发现问题：宽度是固定的，不是填充父布局
3. 解决：父级宽度从 Hug 改为 Fill

### 5.6 添加整体容器

1. 选中所有 4 个列
2. 按 `Shift + L` 包裹在列中
3. 设置子元素水平间距（比主间距小）
4. 确保宽度为 Fill
5. 添加 Padding
6. 添加背景（黑色，20% 不透明度）

### 5.7 设置属性值

1. 修改每个标题
2. 设置随机数字
3. 数据绑定时可以控制这些数字和进度条大小

---

## 六、创建 Start 按钮组件

### 6.1 创建按钮

1. 按下 `A` 创建新的 Artboard
2. 命名为 **"Start"**
3. 设置为组件

### 6.2 设计按钮

1. 按 `T` 创建文本
2. 按 `Shift + L` 放入文本布局
3. 再按 `Shift + L` 放入行布局
4. 关闭绝对定位
5. 设置 Fit 为 Fill width 和 Fill height
6. 设置子元素对齐为居中
7. 设置背景颜色为黑色

---

## 七、创建 Background 组件

### 7.1 导入背景图

导入四张摩托车图片：
- 黑色摩托车
- 蓝色摩托车
- 绿色摩托车
- 白色摩托车

### 7.2 创建背景组件

1. 选中所有 4 张图片，拖到画板上
2. 这会创建一个新的 Artboard，所有图片层叠在一起
3. 选中所有图片，右键 → Wrap in Solo（包裹在 Solo 中）

> **Solo**：一种组类型，可以切换所有图层的可见性，确保一次只显示一个。

4. 命名为 **"Background"**
5. 设置为组件

---

## 八、创建 Arrows 组件（箭头）

### 8.1 使用钢笔工具

1. 按下 `A` 创建新的 Artboard
2. 使用钢笔工具绘制箭头符号

**图层结构**：
- **Shape Layer（形状图层）**：控制颜色和变换属性
- **Path（路径）**：编辑顶点、改变顶点类型

3. 复制路径并移动
4. 调整 Artboard 大小以适应设计
5. 命名为 **"Arrows"**
6. 设置为组件

---

## 九、组装菜单

### 9.1 嵌套 Background 组件

1. 选中 Menu Artboard
2. 按下 `N` 嵌套组件
3. 选择 Background

**问题**：背景溢出了菜单边缘。

**解决**：在 Inspector 中启用 **Clip（裁剪）**

### 9.2 Background 适配设置

让 Background 始终覆盖整个 Menu Artboard：

1. 选中 Background Component
2. 将模式从 **Node** 改为 **Leaf**
3. 将 Fit 从 **Fill** 改为 **Cover**

> **Node 模式**：组件作为容器，可嵌套子元素
> **Leaf 模式**：组件作为叶子，整体适配空间
> **Cover**：始终覆盖背景，按比例缩放

### 9.3 调整 Item 组件

1. 隐藏底部的描述文本
2. 缩小组件大小
3. 设置 Item Column 背景为 20% 不透明度

### 9.4 嵌套其他组件

嵌套以下组件到 Menu Artboard：

1. **Arrows** - 左上角，缩小一点
2. **Text** - "Select Your Moto"（选择你的摩托），黑色
3. **Text** - "Class"，黑色
4. **Item Component × 4** - 四个项目组件
5. **Stats** - 右侧
6. **Start Button** - 右下角

> 提示：可以锁定 Background 层，避免误选。

### 9.5 创建布局结构

**从小到大构建**：

1. 两个文本元素 → 行布局（调整对齐为 Center Left）
2. 四个 Item → 列布局
3. Stats 和其他元素 → 列布局
4. 两个列 → 行布局
5. 所有元素 → 列布局

### 9.6 调整 Fit 和 Alignment

1. **最外层列**：
   - 关闭绝对定位
   - 从 Hug 改为 Fill width 和 Fill height
   - 添加 Padding（50, 50）

2. **两个元素的行**：
   - 设置为 Fill width 和 Fill height
   - 删除水平间距
   - 点击两次对齐按钮（分散）

3. **Stats 列**：
   - 设置为 Fill parent
   - 删除垂直间距
   - 右对齐
   - 再次点击（分散）

4. **Items 列**：
   - 减少垂直间距

现在调整 Artboard 大小，所有元素都会相应移动。

---

## 十、数据绑定

### 10.1 数据绑定简介

数据绑定是一种创建和控制各种属性的方法，可以：
- 用于控制设计
- 作为状态机中的条件
- 通过代码实时控制

### 10.2 创建第一个 ViewModel 属性

1. 选中 Menu Artboard
2. 在 Data Panel 中，创建 **Number（数字）属性**
3. 命名为 **"indexNum"**
4. 默认值为 0

### 10.3 在状态机中使用 indexNum

每个 Artboard 和 Component 都有自己的状态机。我们要在 **Background 状态机**中使用 indexNum。

1. 选中 Background，进入 Animate 模式
2. 删除多余的状态机
3. 创建 4 个 Timeline：
   - Timeline 1：黑色摩托车
   - Timeline 2：蓝色摩托车
   - Timeline 3：绿色摩托车
   - Timeline 4：白色摩托车

4. 在每个 Timeline 中，设置 Solo 的关键帧（显示对应的摩托车）

### 10.4 设置状态转换

1. 将所有 Timeline 拖到状态机舞台
2. 创建从 **Any State** 到各 Timeline 的转换
3. 为所有 4 个转换创建条件：

   - indexNum == 0 → Timeline 1
   - indexNum == 1 → Timeline 2
   - indexNum == 2 → Timeline 3
   - indexNum == 3 → Timeline 4

4. 选中 Menu Artboard，播放状态机
5. 在 Data Panel 中修改 indexNum，背景会切换

### 10.5 添加背景切换动画

创建 **Scale and Opacity Timeline**：
1. 设置 Solo 的不透明度为 0，缩放为 102%
2. 第 30 帧：不透明度 100%，缩放 100%
3. 修改缩放关键帧的插值为"先快后慢"
4. 加快不透明度变化

**状态机设置**：
1. 将 Scale and Opacity 拖到状态机
2. 连接到 Entry
3. 再拖一个 Scale and Opacity，双向连接
4. 为两个转换创建条件：indexNum != indexNum（值改变时触发）

---

## 十一、Stats 组件的数据绑定

### 11.1 创建 Stats ViewModel

1. 进入 Stats 组件
2. 创建新的 ViewModel
3. 命名为 **"Stats ViewModel"**
4. 添加属性：
   - **String**：title（标题）
   - **Number**：power（动力）
   - **Number**：speed（速度）
   - **Number**：acceleration（加速）
   - **Number**：handling（操控）

### 11.2 创建数字转字符串转换器

因为要用数字控制字符串，需要创建转换器：
1. 在 Inspector 中，启用 **Round decimals**（四舍五入）
2. 启用 **Remove trailing zeros**（删除尾随零）

### 11.3 绑定文本

1. 选中标题文本
2. 打开 Text Run
3. 右键 → Data Bind
4. 选择 title 属性

> 注意：需要按播放状态机才能看到更新，或按 `Cmd + B` 切换预览绑定值。

5. 绑定其他数字文本：
   - Power → 添加转换器
   - Speed → 添加转换器
   - Handling → 添加转换器

### 11.4 绑定进度条

1. 选中白色条的 Layout
2. Data Bind → 绑定 Layout width → power
3. 同样绑定其他条：
   - Speed 条 → speed
   - Acceleration 条 → acceleration
   - Handling 条 → handling

现在在 Data Panel 中修改数字，不仅文本改变，进度条大小也会改变。

### 11.5 在 Menu 中访问 Stats 属性

问题：Menu Artboard 只能访问自己的 ViewModel 属性。

解决：给 Menu ViewModel 添加 Stats ViewModel 作为属性：
1. 选中 Menu ViewModel
2. 点击 +，选择 View Models
3. 添加 Stats ViewModel
4. 选中 Stats Component，绑定到这个属性

现在可以在 Menu 中实时控制所有 Stats 属性。

---

## 十二、Instance 系统和多状态

### 12.1 为什么需要 Instance

我们有 4 辆不同的摩托车，每辆需要不同的属性值：
- indexNum = 0 → 黑色摩托车 + 其属性
- indexNum = 1 → 蓝色摩托车 + 其属性
- 以此类推

### 12.2 创建多个 Instance

**Instance** 允许创建多个不同版本的 ViewModel 属性，从而创建多个不同版本的组件。

1. 选中 Stats ViewModel 属性
2. 创建 3 个额外的 Instance（共 4 个）
3. 为每个 Instance 设置不同的属性值

### 12.3 在 Menu 中添加多个 Stats 属性

1. Menu ViewModel 添加 4 个 Stats ViewModel 属性：
   - Stats ViewModel Instance 1
   - Stats ViewModel Instance 2
   - Stats ViewModel Instance 3
   - Stats ViewModel Instance 4

2. 每个 Instance 绑定到不同的 Instance 编号

### 12.4 复制 Stats Component

1. 选中 Stats Component
2. 在 Hierarchy 中，复制 Instance 3 次（共 4 个）
3. 为每个嵌套组件绑定正确的属性：
   - 第一个 → Instance 1
   - 第二个 → Instance 2
   - 第三个 → Instance 3
   - 第四个 → Instance 4

4. 隐藏其中 3 个（只显示一个）

### 12.5 为 Instance 切换添加动画

在 Menu 状态机中：
1. 创建 4 个 Timeline：
   - Stats Instance 1
   - Stats Instance 2
   - Stats Instance 3
   - Stats Instance 4

2. 在每个 Timeline 中设置可见性关键帧

3. 状态机设置：
   - 删除旧的转换
   - 连接 Entry 到 Instance 4
   - 将其他 3 个拖到状态机舞台
   - 创建从 Any State 到各 Timeline 的转换
   - 设置条件：indexNum == 0/1/2/3

### 12.6 为 Stats 添加元素动画

**问题**：Fill 模式不支持绝对定位动画。

**解决**：
1. 将 Fit 从 Fill 改为 **Fixed**
2. 单位从 Pixel 改为 **Percent 100%**
3. 开启绝对定位

现在可以动画 Y 位置了。

**动画设置**：
1. 为每个元素的 Y 位置设置关键帧
2. 动画可见性（从隐藏到显示）
3. 移动 50 像素，使用 Shift 键精确调整
4. 设置插值为"先快后慢"
5. 错开动画（按住 Alt/Option + . 键）

**背景颜色动画**：
1. 添加 Feather（羽化）效果，但设为 0
2. 使用 Y Offset 属性
3. 设置关键帧和插值

---

## 十三、列表功能（Artboard List）

### 13.1 为什么使用列表

与手动放置多个组件相比，列表具有优势：
- 当一个项目变大时，会推动其他项目
- 自动重新计算布局
- 更好的性能和组织

### 13.2 为 Item 组件添加数据绑定

1. 显示描述文本
2. 创建 Item ViewModel
3. 添加属性：
   - **Image**：helmet
   - **String**：name
   - **String**：class
   - **String**：description

4. 创建 3 个额外的 Instance
5. 为每个 Instance 设置不同的值：
   - Instance 1：黑色头盔
   - Instance 2：蓝色头盔
   - Instance 3：绿色头盔
   - Instance 4：白色头盔

### 13.3 绑定 Item 元素

1. 图片 → Data Bind → helmet
2. 名称文本 → Data Bind → name
3. 类别文本 → Data Bind → class
4. 描述文本 → Data Bind → description

### 13.4 在 Menu 中创建列表

1. Menu ViewModel → 添加 **List 属性**
2. 命名为 **"items"**
3. 添加 4 个列表项，分别绑定到 4 个 Instance

### 13.5 创建 Artboard List

1. 在 Hierarchy 中选中 Item 列
2. 删除所有子元素（空布局）
3. 在 Inspector 中，Layout Children → 点击 +
4. 选择 **Artboard List**
5. 绑定到 "items" 列表属性

### 13.6 列表的优势

如果 Item 被点击变大，会推动列表中的其他元素。让我们实现这个逻辑。

---

## 十四、Item 交互逻辑

### 14.1 Hover 效果

**状态**：
- **Unhover**：正常状态
- **Hover**：鼠标悬停
- **Click**：点击状态

**创建 Timeline**：
1. 创建 3 个 Timeline：unhover、hover、click
2. 在每个中设置组件大小、位置、背景、描述可见性

**Hover 动画**：
- 组件向右移动
- 不透明度变化

**Click 动画**：
- 组件变大（更宽更高）
- 显示描述文本

### 14.2 使用 Boolean 控制 Hover

1. Item ViewModel → 添加 **Boolean 属性**
2. 命名为 **"hover"**

3. 状态机设置：
   - Entry → unhover
   - unhover ↔ hover 双向转换
   - 条件：hover == true/false

### 14.3 使用 Listener 监听鼠标

**创建 Listener**：
1. **Enter Listener**：
   - 目标：Item Column
   - 条件：指针进入 Item Column
   - 动作：设置 hover = true

2. **Exit Listener**：
   - 目标：Item Column
   - 条件：指针退出 Item Column
   - 动作：设置 hover = false

### 14.4 添加音效

1. 导入 3 个音效文件
2. 创建 **Event**
3. 命名为 **"hoverSound"**
4. 类型改为 Audio
5. 选择音效资源
6. 在 hover 状态中设置关键帧播放音效

---

## 十五、Click 逻辑

### 15.1 使用 List Index 控制

我们需要通过点击控制 indexNum：
- 点击第 1 项 → indexNum = 0
- 点击第 2 项 → indexNum = 1
- 以此类推

### 15.2 添加 List Index 属性

1. 先将 indexNum 改为 -1（原因稍后解释）
2. Item ViewModel → 添加 **List Index 属性**
3. 这告诉我们每个项目在列表中的位置（0、1、2、3）

### 15.3 创建 Click Listener

1. 创建 **Listener**，命名为 "click"
2. 目标：Item Column
3. 条件：指针点击 Item Column
4. 动作：设置 indexNum = List Index 的值

### 15.4 重要：关闭 Preview Bound Values

问题：点击没有反应。

解决：
- 编辑时：Preview Bound Values 开启（可以看到列表）
- 运行时：Preview Bound Values 关闭（列表功能正常）

### 15.5 使用 indexNum 控制 Click 状态

1. 创建进入 click 状态的转换
2. 创建离开 click 状态的转换
3. 条件：indexNum == List Index

**逻辑**：
- 点击某项 → indexNum 等于该项的 List Index → 激活 click 状态
- 点击其他项 → indexNum 不再等于该项的 List Index → 取消 click 状态

**结果**：同时只能有一个项目处于 click 状态。

### 15.6 添加点击音效

1. 创建 Event → "clickSound"
2. 类型：Audio
3. 资源：select sound
4. 在 click timeline 开始处设置关键帧

---

## 十六、列表进场动画

### 16.1 使用 Empty Timeline 错开动画

问题：如何让同一个组件的不同实例有不同的动画时机？

解决：使用 Empty Timeline 来错开动画。

### 16.2 创建 Load 和 Empty Timeline

1. 创建两个 Timeline：**load** 和 **empty**
2. 在 load 中动画：
   - 设置 Item Column 顶部位置为 +50
   - 可见性：隐藏
   - 1 帧后：显示
   - 30 帧：位置为 0
   - 插值：先快后慢

3. empty：保持为空（用于延迟）

### 16.3 状态机设置

1. 删除 Entry → unhover 转换
2. 连接：Entry → empty → load → unhover
3. 设置 empty → load 转换的 Exit Time 为 100%

### 16.4 使用 List Index 错开动画

为每个 Instance 创建不同的 Exit Time：
- List Index == 0 → 100ms
- List Index == 1 → 200ms
- List Index == 2 → 300ms
- List Index == 3 → 400ms

### 16.5 修复初始可见性问题

问题：项目在设计时就可见。

解决：在 empty Timeline 中设置 Item Column 为隐藏。

---

## 十七、Intro 进场动画

### 17.1 创建 Intro Timeline

在 Menu Artboard 中：
1. 创建新的状态机层
2. 创建新的 Timeline：**intro**
3. 选中 Arrows 组件，设置 Y 位置和不透明度关键帧
4. 对 "Select Your Moto" 和 "Class" 文本做同样操作

**动画**：
- 开始：位置 +50，不透明度 0
- 1 帧：不透明度 100
- 30 帧：位置 0
- 插值：先快后慢

### 17.2 错开动画

使用 Alt/Option + . 键错开各元素的动画时机。

### 17.3 状态机设置

直接播放 intro 动画。

---

## 十八、Outro 退场动画

### 18.1 创建 Trigger

1. Menu ViewModel → 添加 **Trigger**
2. 命名为 **"start"**

> **Trigger**：类似 Boolean，但总是 false，除非被触发（变为 true 一帧后立即回到 false）
>
> 用于不需要来回切换的状态转换。

### 18.2 创建 Start Button Listener

1. 创建 Listener
2. 目标：Start Button 的 Layout
3. 条件：指针点击 Start Button Layout
4. 动作：触发 start trigger

### 18.3 创建 Outro Timeline

1. 在 Menu Artboard 中创建 outro timeline
2. 动画相同的属性（Y 位置和不透明度）

**动画**：
- 开始：位置 0，不透明度 100
- 几帧后：位置 -50
- 结束：不透明度 0

**不透明度处理**：
- 选中第一个不透明度关键帧
- 设置为 **Hold Keyframe**（保持关键帧）
- 这样会保持值直到下一个关键帧，然后立即切换

**插值**：
- 位置关键帧：先慢后快

### 18.4 Intro ↔ Outro 转换

1. 设置条件：start trigger fired
2. 从 intro 转换到 outro

---

## 十九、Stats Outro 动画

### 19.1 简单方案

只动画包含所有 Instance 的列：

1. 在 outro timeline 开始处设置 Margin 关键帧
2. 分割 Margin 为 4 个独立属性
3. 动画 Top Margin：从 0 到 -50
4. 插值：先慢后快

### 19.2 不透明度动画

不直接控制列的不透明度（因为包含 Start Button），而是控制 4 个 Stats Layout：

1. 结束处：不透明度 0
2. 开始处：不透明度 100
3. 设置为 Hold Keyframe

### 19.3 调整元素时序

让 Arrows 和 "Select Your Moto" 一起消失（因为它们在同一行），Class 稍晚一点。

---

## 二十、Item Outro 动画

### 20.1 创建 Outro Timeline

在 Item Component 中：
1. 创建 outro timeline
2. 动画 Item Column 的顶部位置和不透明度

**动画**：
- 几帧后：位置 -50，不透明度 0
- 不透明度关键帧：Hold
- 位置关键帧：先慢后快

### 20.2 状态机设置

1. 将 outro 拖到状态机舞台
2. 创建新的 empty timeline（真正的空）
3. 用 empty2 替换原有的 empty 状态
4. 连接：Any State → empty2 → outro
5. 创建 4 个转换，条件为 start trigger fired
6. 使用 List Index 设置不同的 Exit Time：
   - List Index == 0 → 100ms
   - List Index == 1 → 200ms
   - List Index == 2 → 300ms
   - List Index == 3 → 400ms

### 20.3 添加音效

1. 创建 Event → "selectSound"
2. 类型：Audio
3. 资源：load sound
4. 在 outro timeline 开始处设置关键帧

---

## 总结

恭喜！你已完成了整个 Rive 快速入门教程，学会了：

✅ **Layouts 布局系统** - 创建响应式设计
✅ **Component 组件** - 可复用的设计元素
✅ **Data Binding 数据绑定** - ViewModel 和属性绑定
✅ **State Machine 状态机** - 动画和状态控制
✅ **Instance 系统** - 多版本组件
✅ **Artboard List** - 动态列表
✅ **Listener** - 鼠标交互
✅ **Event** - 音效播放
✅ **Trigger** - 一次性触发
✅ **Intro/Outro 动画** - 进出场效果

现在你可以创建自己的交互式动画界面了！

---

**快捷键总结**：

| 操作 | 快捷键 |
|------|--------|
| 创建 Artboard | `A` + 拖动 |
| 创建文本 | `T` |
| 创建布局 | `Shift + L` |
| 复制 | `Cmd + D` |
| 播放状态机 | 点击 Play |
| 显示所有关键帧 | `U` |
| 预览绑定值 | `Cmd + B` |
| 选择图层（层级中） | `Cmd + 点击` |
| 前进一帧 | `.` |
| 精确调整（10像素） | `Shift + 方向键` |
| 错开关键帧 | `Alt/Option + .` |
| 完成/确认 | `Enter` |

---

**参考资料**：
- [Rive 官方文档](https://rive.app)
- [Rive 社区](https://community.rive.app)
