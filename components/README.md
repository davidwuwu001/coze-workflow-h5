# 公共组件模板

本目录包含 Coze 工作流聚合小程序的所有公共组件模板。

## 组件列表

### 1. iOS 状态栏组件 (status-bar.html)

模拟 iOS 状态栏，包含时间、信号、WiFi、电池图标。

**规格：**
- 高度: 47px
- 字体: SF Pro Text, 14px
- 颜色: #000000 (浅色模式)

**使用方法：**
```html
<div class="status-bar bg-white">
    <span class="time">9:41</span>
    <div class="icons">
        <i class="fas fa-signal"></i>
        <i class="fas fa-wifi"></i>
        <i class="fas fa-battery-full"></i>
    </div>
</div>
```

**变体：**
- `bg-white` - 白色背景
- `bg-transparent` - 透明背景
- `light-content` - 浅色文字（用于深色背景）

---

### 2. 底部 Tab Bar 组件 (tab-bar.html)

iOS 风格底部导航栏，包含4个入口。

**规格：**
- 高度: 83px (含安全区域)
- 图标大小: 24px
- 文字大小: 10px
- 激活颜色: #007AFF
- 默认颜色: #8E8E93

**使用方法：**
```html
<nav class="tab-bar">
    <a href="index.html" class="tab-item active">
        <i class="fas fa-home"></i>
        <span>首页</span>
    </a>
    <a href="category.html" class="tab-item">
        <i class="fas fa-th-large"></i>
        <span>分类</span>
    </a>
    <a href="favorites.html" class="tab-item">
        <i class="fas fa-heart"></i>
        <span>收藏</span>
    </a>
    <a href="profile.html" class="tab-item">
        <i class="fas fa-user"></i>
        <span>我的</span>
    </a>
</nav>
```

**注意：** 根据当前页面，将对应的 `tab-item` 添加 `active` 类。

---

### 3. 工作流卡片组件 (workflow-card.html)

展示单个工作流的卡片组件。

**规格：**
- 圆角: 12px
- 内边距: 16px
- 图标尺寸: 48×48px
- 阴影: 0 2px 8px rgba(0,0,0,0.08)

**使用方法：**
```html
<a href="detail.html" class="workflow-card">
    <div class="card-icon">
        <img src="icon.png" alt="工作流图标">
    </div>
    <div class="card-content">
        <h3 class="card-title">智能文案生成</h3>
        <p class="card-desc">一键生成营销文案、产品描述...</p>
        <div class="card-meta">
            <span class="usage">12.5k 次使用</span>
            <span class="price-tag free">免费</span>
        </div>
    </div>
    <i class="fas fa-chevron-right arrow"></i>
</a>
```

**价格标签类型：**
- `price-tag free` - 免费（绿色 #34C759）
- `price-tag points` - 积分（橙色 #FF9500）
- `price-tag vip` - 会员专享（紫色 #AF52DE）

---

## 页面模板结构

每个页面应遵循以下基本结构：

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>页面标题</title>
    
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    
    <!-- FontAwesome CDN -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    
    <!-- 公共样式 -->
    <link rel="stylesheet" href="css/styles.css">
</head>
<body class="bg-gray-900 min-h-screen flex items-center justify-center p-5">
    <!-- iPhone 15 Pro 设备容器 (393×852px) -->
    <div class="device-container">
        <div class="page-content">
            
            <!-- iOS 状态栏 -->
            <div class="status-bar bg-white">
                <span class="time">9:41</span>
                <div class="icons">
                    <i class="fas fa-signal"></i>
                    <i class="fas fa-wifi"></i>
                    <i class="fas fa-battery-full"></i>
                </div>
            </div>
            
            <!-- 主内容区域 -->
            <main class="main-content">
                <!-- 页面内容 -->
            </main>
            
            <!-- 底部 Tab Bar (主页面需要) -->
            <nav class="tab-bar">
                <!-- Tab 项目 -->
            </nav>
            
        </div>
    </div>
</body>
</html>
```

---

## 设计规范

### 颜色系统
- 主色调: #007AFF (iOS蓝)
- 成功/免费: #34C759 (绿色)
- 警告/积分: #FF9500 (橙色)
- 会员专享: #AF52DE (紫色)
- 背景灰: #F2F2F7
- 边框灰: #E5E5EA
- 次要文字: #8E8E93
- 主要文字: #1C1C1E

### 字体系统
- 字体: -apple-system, SF Pro Text
- 超小: 10px
- 小: 12px
- 基础: 14px
- 大: 16px
- 超大: 18px

### 圆角系统
- 小: 8px
- 中: 12px
- 大: 16px
- 页面: 40px
