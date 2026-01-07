# Coze 工作流聚合平台

一个基于 Web 的 AI 工作流聚合平台，提供各类智能工作流服务。

## ✨ 特性

- 📱 **PWA 支持** - 可安装到手机主屏幕，像原生应用一样使用
- 🚀 **离线访问** - Service Worker 缓存，支持离线浏览
- 🎨 **现代 UI** - iOS 风格设计，流畅的用户体验
- 📦 **工作流分类** - 视频内容、图文生成、智能体等多种分类
- ⭐ **收藏功能** - 收藏喜欢的工作流，快速访问
- 🔍 **搜索功能** - 快速查找需要的工作流
- 👤 **个人中心** - 会员管理、积分系统

## 🚀 快速开始

### 本地运行

1. 启动本地服务器（PWA 需要 HTTP 服务器）：
   ```bash
   # 使用 Python
   python3 -m http.server 8000
   
   # 或使用 Node.js
   npx serve
   ```

2. 在浏览器中访问：
   ```
   http://localhost:8000
   ```

### 测试 PWA 功能

### 测试 PWA 功能

```bash
# 启动本地服务器
python3 -m http.server 8000
```

访问 `http://localhost:8000`，打开浏览器开发者工具检查：
- Service Worker 是否注册成功
- Manifest 是否加载正确

### 4. 移动端测试

#### iOS (Safari)
1. 在 Safari 中打开网站
2. 点击分享按钮
3. 选择"添加到主屏幕"

#### Android (Chrome)
1. 在 Chrome 中打开网站
2. 会自动提示"添加到主屏幕"
3. 或点击菜单 → "安装应用"

## 📁 项目结构

```
.
├── index.html              # 首页
├── category.html           # 分类页
├── favorites.html          # 收藏页
├── profile.html            # 个人中心
├── detail.html             # 工作流详情
├── search.html             # 搜索页
├── settings.html           # 设置页
├── member.html             # 会员中心
├── payment.html            # 支付页面
├── manifest.json           # PWA 配置文件
├── sw.js                   # Service Worker
├── icon-generator.html     # 图标生成工具
├── css/
│   └── styles.css          # 全局样式
├── images/                 # 图标和图片资源
└── js/                     # JavaScript 文件
```

## 🛠️ 技术栈

- **HTML5** - 语义化标签
- **CSS3** - 现代样式，渐变、动画
- **JavaScript** - 原生 JS，无框架依赖
- **Tailwind CSS** - 实用优先的 CSS 框架
- **Font Awesome** - 图标库
- **PWA** - Progressive Web App 技术
- **Service Worker** - 离线缓存和资源管理

## 📱 PWA 功能

- ✅ 离线访问
- ✅ 添加到主屏幕
- ✅ 全屏显示
- ✅ 快速加载
- ✅ 自动更新
- ✅ 推送通知（可扩展）

## 🌐 部署

### GitHub Pages

1. 推送代码到 GitHub
2. 在仓库设置中启用 GitHub Pages
3. 选择 `main` 分支
4. 访问 `https://your-username.github.io/your-repo`

### Netlify / Vercel

1. 连接 GitHub 仓库
2. 自动部署
3. 获得 HTTPS 域名

### 自定义服务器

确保：
- 使用 HTTPS（PWA 要求）
- 正确配置 MIME 类型
- Service Worker 可访问

## 📝 开发说明

### 修改样式

编辑 `css/styles.css` 文件，使用 CSS 变量：

```css
:root {
    --primary-color: #007AFF;
    --success-color: #34C759;
    --warning-color: #FF9500;
    /* ... */
}
```

### 添加新页面

1. 创建 HTML 文件
2. 添加 PWA Meta 标签
3. 注册 Service Worker
4. 更新 `sw.js` 中的缓存列表

### 更新缓存

修改 `sw.js` 中的 `CACHE_NAME`：

```javascript
const CACHE_NAME = 'coze-workflow-v2'; // 增加版本号
```

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

MIT License

## 📞 联系方式

如有问题或建议，请通过以下方式联系：
- GitHub Issues
- Email: your-email@example.com

---

Made with ❤️ by Coze Team
