# mksass 模板 - 速查表

## 🚀 快速开始

### 安装与配置
```bash
# 安装
npm install sass mksass-template

# 初始化项目
npx mksass init my-project

# 导入模板
@import 'mksass/core';
@import 'mksass/components/buttons';
@import 'mksass/utilities';
```

### 基础使用
```scss
// 使用组件
.mk-button {
  @include mk-button-primary;

  &:hover {
    @include mk-button-hover;
  }
}

// 使用工具类
.mk-flex {
  @include mk-flex(row, space-between, center);
}

// 响应式
@include mk-breakpoint(tablet) {
  .container {
    @include mk-flex(column, flex-start, stretch);
  }
}
```

## 🎨 核心变量

### 颜色系统
```scss
$mk-colors: (
  'primary': #3b82f6,
  'secondary': #64748b,
  'success': #10b981,
  'warning': #f59e0b,
  'error': #ef4444,
  'background': #ffffff,
  'surface': #f8fafc,
  'text': #1e293b,
  'text-secondary': #64748b,
  'border': #e2e8f0
);
```

### 间距系统
```scss
$mk-spacing: (
  'xs': 0.25rem,   // 4px
  'sm': 0.5rem,    // 8px
  'md': 1rem,      // 16px
  'lg': 1.5rem,    // 24px
  'xl': 2rem,      // 32px
  '2xl': 3rem,     // 48px
  '3xl': 4rem      // 64px
);
```

### 断点系统
```scss
$mk-breakpoints: (
  'mobile': 640px,
  'tablet': 768px,
  'desktop': 1024px,
  'large': 1280px
);
```

## 🔧 核心混入

### 布局混入
```scss
// Flexbox 布局
@include mk-flex($direction: row, $justify: center, $align: center);

// Grid 布局
@include mk-grid(columns: 12, gap: 1rem);

// 间距
@include mk-spacing(margin, md);  // margin: 1rem;
@include mk-padding(xl);         // padding: 2rem;
```

### 响应式混入
```scss
// 基础响应式
@include mk-breakpoint(mobile) {
  // 移动端样式
}

// 多断点
@include mk-responsive(tablet, desktop) {
  // 平板和桌面样式
}
```

### 视觉效果
```scss
// 阴影
@include mk-shadow(md);      // 中等阴影

// 圆角
@include mk-radius(lg);      // 大圆角

// 过渡
@include mk-transition(all, 0.3s);
```

## 🎯 实用工具类

### Flexbox 工具类
```scss
.mk-flex-row      // display: flex; flex-direction: row;
.mk-flex-column   // display: flex; flex-direction: column;
.mk-flex-wrap     // flex-wrap: wrap;
.mk-justify-center // justify-content: center;
.mk-align-center   // align-items: center;
.mk-items-stretch  // align-items: stretch;
```

### 间距工具类
```scss
// 边距
.m-1, .m-2, .m-3, .m-4
.mt-1, .mb-1, .ml-1, .mr-1
.mx-1, .my-1

// 内边距
.p-1, .p-2, .p-3, .p-4
.pt-1, .pb-1, .pl-1, .pr-1
.px-1, .py-1
```

### 文本工具类
```scss
.text-center        // text-align: center;
.text-left         // text-align: left;
.text-right        // text-align: right;
.text-xs, .text-sm, .text-base, .text-lg, .text-xl
.font-bold, .font-medium, .font-normal
.text-primary, .text-secondary, .text-success
```

## 🎨 组件库

### 按钮
```scss
// 主要按钮
.mk-button-primary {
  @include mk-button-style($mk-colors-primary);
}

// 次要按钮
.mk-button-secondary {
  @include mk-button-style($mk-colors-secondary);
}

// 警告按钮
.mk-button-warning {
  @include mk-button-style($mk-colors-warning);
}
```

### 表单元素
```scss
// 输入框
.mk-input {
  @include mk-input-base;

  &.focused {
    @include mk-input-focus;
  }
}

// 选择框
.mk-select {
  @include mk-select-base;
}
```

### 卡片
```scss
// 基础卡片
.mk-card {
  @include mk-card-base;
}

// 卡片头部
.mk-card-header {
  @include mk-card-header;
}

// 卡片内容
.mk-card-body {
  @include mk-card-body;
}

// 卡片底部
.mk-card-footer {
  @include mk-card-footer;
}
```

## 🎭 主题系统

### 主题切换
```scss
// 默认主题
:root {
  @include mk-theme('default');
}

// 深色主题
[data-theme="dark"] {
  @include mk-theme('dark');
}

// 自定义主题
:root {
  @include mk-theme('custom', (
    'primary': #ff6b6b,
    'secondary': #4ecdc4
  ));
}
```

### 动态主题
```scss
// JavaScript 动态切换
function setTheme(theme) {
  document.documentElement.setAttribute('data-theme', theme);
  localStorage.setItem('theme', theme);
}
```

## 📱 响应式设计

### 断点媒体查询
```scss
// 移动端优先
.mk-responsive-mobile {
  @media (min-width: 640px) {
    @content;
  }
}

// 平板端
.mk-responsive-tablet {
  @media (min-width: 768px) {
    @content;
  }
}

// 桌面端
.mk-responsive-desktop {
  @media (min-width: 1024px) {
    @content;
  }
}
```

### 响应式组件
```scss
// 响应式网格
.mk-grid-responsive {
  display: grid;
  grid-template-columns: 1fr;

  @include mk-breakpoint(tablet) {
    grid-template-columns: repeat(2, 1fr);
  }

  @include mk-breakpoint(desktop) {
    grid-template-columns: repeat(3, 1fr);
  }
}
```

## 🛠️ 调试工具

### 调试混入
```scss
// 显示布局
@include mk-debug-layout;

// 显示颜色
@include mk-debug-colors;

// 显示间距
@include mk-debug-spacing;
```

### 开发模式
```scss
// 开发环境特殊样式
@if $mk-environment == 'development' {
  .mk-debug {
    @include mk-debug-styles;
  }
}
```

## 📊 性能优化

### 编译优化
```scss
// 按需导入
@forward 'mksass/core';
@forward 'mksass/components/buttons' hide .mk-button-legacy;
@forward 'mksass/utilities' as mk-*;

// 代码分割
@mixin mk-code-split($module) {
  @import 'mksass/modules/#{$module}';
}
```

### 运行时优化
```scss
// CSS 变量优化
:root {
  --mk-primary-color: #3b82f6;
  --mk-secondary-color: #64748b;

  @include mk-css-variables;
}

// 减少重绘
.mk-smooth-render {
  will-change: transform;
  backface-visibility: hidden;
}
```

## 🚀 常用模式

### 组件模式
```scss
// 可变体组件
.mk-button {
  @include mk-button-base;

  &--primary { @include mk-button-style($mk-colors-primary); }
  &--secondary { @include mk-button-style($mk-colors-secondary); }
  &--large { @include mk-button-size(lg); }
  &--small { @include mk-button-size(sm); }
}
```

### 布局模式
```scss
// 容器布局
.mk-container {
  @include mk-container(max-width: 1200px);

  @include mk-breakpoint(mobile) {
    @include mk-container(max-width: 100%);
  }
}

// 栅格布局
.mk-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: $mk-spacing-md;
}
```

### 动画模式
```scss
// 过渡动画
.mk-transition-fade {
  @include mk-transition(opacity, 0.3s ease);
}

// 悬停效果
.mk-hover-scale {
  &:hover {
    transform: scale(1.05);
    transition: transform 0.2s ease;
  }
}
```

## 🎯 最佳实践

### 命名规范
```scss
// BEM 命名法
.block {
  &__element {
    &--modifier {
      // 样式
    }
  }
}

// mksass 命名法
.mk-block {
  &__element {
    &--modifier {
      // 样式
    }
  }
}
```

### 文件组织
```
styles/
├── abstracts/         // 抽象层
│   ├── _variables.scss
│   ├── _functions.scss
│   ├── _mixins.scss
│   └── _placeholders.scss
├── base/              // 基础样式
│   ├── _reset.scss
│   ├── _typography.scss
│   └── _animations.scss
├── components/        // 组件
│   ├── _buttons.scss
│   ├── _forms.scss
│   ├── _cards.scss
│   └── _navigation.scss
├── layouts/           // 布局
│   ├── _header.scss
│   ├── _footer.scss
│   └── _grid.scss
├── pages/             // 页面
│   ├── _home.scss
│   ├── _about.scss
│   └── _contact.scss
├── themes/            // 主题
│   ├── _default.scss
│   ├── _dark.scss
│   └── _custom.scss
└── main.scss          // 入口文件
```

### 维护策略
```scss
// 版本管理
// _version.scss
$mk-version: '1.0.0';

// 文档注释
/**
 * @module Mixins
 * @description 布局混入
 * @author mksass-team
 * @version 1.0.0
 */
```

---

## 📞 支持与资源

### 官方文档
- [完整文档](https://mksass.com/docs)
- [API 参考](https://mksass.com/api)
- [示例项目](https://github.com/mksass/examples)

### 社区资源
- [GitHub](https://github.com/mksass/mksass)
- [npm](https://www.npmjs.com/package/mksass)
- [Stack Overflow](https://stackoverflow.com/questions/tagged/mksass)

### 快速链接
- [开始指南](https://mksass.com/getting-started)
- [组件库](https://mksass.com/components)
- [主题系统](https://mksass.com/themes)
- [最佳实践](https://mksass.com/best-practices)

---

*速查表版本：v1.0*
*更新时间：2026年1月13日*
*适用于 mksass 模板 v1.0+*