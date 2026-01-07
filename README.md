# Coze 工作流聚合小程序 H5 原型

## 项目简介

这是一个基于 H5 的移动端 Web 应用原型，用于展示和管理 Coze 平台上的各类 AI 工作流。

## 设计规范

- **设计尺寸**: iPhone 15 Pro (393×852px)
- **页面圆角**: 40px
- **卡片圆角**: 12px
- **主色调**: iOS Blue (#007AFF)

## 技术栈

- **布局框架**: Tailwind CSS 3.x (CDN)
- **图标库**: FontAwesome 6.x (CDN)
- **图片资源**: Unsplash/Pexels 真实图片

## 项目结构

```
coze-workflow-h5/
├── css/
│   └── styles.css          # 公共样式文件（CSS变量、基础样式）
├── components/
│   ├── status-bar.html     # iOS 状态栏组件
│   ├── tab-bar.html        # 底部 Tab Bar 组件
│   └── workflow-card.html  # 工作流卡片组件
├── js/
│   └── .gitkeep            # JavaScript 文件目录
├── images/
│   └── .gitkeep            # 图片资源目录
├── index.html              # 首页（轮播图、分类标签、工作流列表）
├── category.html           # 分类页（分类网格、分类下工作流列表）
├── search.html             # 搜索页（搜索框、搜索历史、搜索结果）
├── detail.html             # 工作流详情页（详细信息、使用按钮）
├── favorites.html          # 收藏页（收藏的工作流列表）
├── profile.html            # 我的页面（用户信息、会员状态、设置入口）
├── member.html             # 会员中心（会员套餐、权益说明）
├── recharge.html           # 积分充值（积分套餐、充值记录）
├── payment.html            # 支付页面（支付方式选择、确认支付）
├── settings.html           # 设置页面（通知、缓存、关于、反馈）
└── README.md               # 项目说明
```

## 颜色系统

| 变量名 | 颜色值 | 用途 |
|--------|--------|------|
| --primary-color | #007AFF | 主色调 - iOS蓝 |
| --success-color | #34C759 | 成功/免费 - 绿色 |
| --warning-color | #FF9500 | 警告/积分 - 橙色 |
| --danger-color | #FF3B30 | 危险/错误 - 红色 |
| --purple-color | #AF52DE | 会员专享 - 紫色 |
| --gray-100 | #F2F2F7 | 背景灰 |
| --gray-200 | #E5E5EA | 边框灰 |
| --gray-500 | #8E8E93 | 次要文字 |
| --gray-900 | #1C1C1E | 主要文字 |

## 字体系统

```css
--font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Text', 'Helvetica Neue', sans-serif;
--font-size-xs: 10px;
--font-size-sm: 12px;
--font-size-base: 14px;
--font-size-lg: 16px;
--font-size-xl: 18px;
--font-size-2xl: 20px;
--font-size-3xl: 24px;
```

## 使用方法

1. 直接在浏览器中打开 `index.html` 文件
2. 或使用本地服务器运行项目

## 页面清单

| 文件名 | 页面名称 | 功能描述 |
|--------|----------|----------|
| index.html | 首页 | 轮播图、分类标签、工作流列表 |
| category.html | 分类页 | 分类网格、分类下工作流列表 |
| search.html | 搜索页 | 搜索框、搜索历史、搜索结果 |
| detail.html | 详情页 | 工作流详细信息、使用按钮 |
| favorites.html | 收藏页 | 收藏的工作流列表 |
| profile.html | 我的页面 | 用户信息、会员状态、设置入口 |
| member.html | 会员中心 | 会员套餐、权益说明 |
| recharge.html | 积分充值 | 积分套餐、充值记录 |
| payment.html | 支付页面 | 支付方式选择、确认支付 |
| settings.html | 设置页面 | 通知、缓存、关于、反馈 |
