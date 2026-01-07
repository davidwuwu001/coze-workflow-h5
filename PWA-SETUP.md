# PWA 设置指南

## 📱 已完成的配置

✅ 创建了 `manifest.json` - PWA 应用配置文件
✅ 创建了 `sw.js` - Service Worker 离线缓存
✅ 所有 HTML 文件已添加 PWA Meta 标签
✅ 所有 HTML 文件已注册 Service Worker
✅ 应用图标已生成并配置完成

## 🎨 应用图标

所有尺寸的 PWA 图标已从 `images/coze-ai-logo.jpg` 生成并放置在 `images/` 目录：
- icon-72x72.png
- icon-96x96.png
- icon-128x128.png
- icon-144x144.png
- icon-152x152.png
- icon-192x192.png
- icon-384x384.png
- icon-512x512.png

## 🚀 测试 PWA

### 本地测试

1. 使用本地服务器运行（PWA 需要 HTTPS 或 localhost）：
   ```bash
   # 使用 Python
   python3 -m http.server 8000
   
   # 或使用 Node.js
   npx serve
   ```

2. 在浏览器中打开 `http://localhost:8000`

3. 打开浏览器开发者工具：
   - Chrome: F12 → Application → Service Workers
   - 检查 Service Worker 是否注册成功
   - 检查 Manifest 是否加载正确

### 移动端测试

#### iOS (Safari)
1. 在 Safari 中打开网站
2. 点击分享按钮
3. 选择"添加到主屏幕"
4. 应用图标会出现在主屏幕上

#### Android (Chrome)
1. 在 Chrome 中打开网站
2. 会自动提示"添加到主屏幕"
3. 或点击菜单 → "安装应用"

## 🔧 PWA 功能

✅ **离线访问** - 缓存关键页面和资源
✅ **添加到主屏幕** - 像原生应用一样启动
✅ **全屏显示** - 隐藏浏览器地址栏
✅ **快速加载** - Service Worker 缓存加速
✅ **自动更新** - Service Worker 自动更新缓存

## 📝 注意事项

1. **HTTPS 要求**：PWA 必须在 HTTPS 环境下运行（localhost 除外）
2. **图标要求**：至少需要 192x192 和 512x512 两个尺寸
3. **浏览器支持**：现代浏览器都支持 PWA（IE 除外）
4. **iOS 限制**：iOS Safari 对 PWA 的支持有一些限制

## 🌐 部署到生产环境

部署到支持 HTTPS 的服务器：
- GitHub Pages
- Netlify
- Vercel
- Cloudflare Pages

确保：
1. 所有文件都已上传
2. `manifest.json` 和 `sw.js` 在根目录
3. 图标文件在 `images/` 目录
4. 网站使用 HTTPS

## 🎯 下一步

1. 生成并上传应用图标
2. 部署到支持 HTTPS 的服务器
3. 在移动设备上测试安装
4. 测试离线功能
5. 优化缓存策略（如需要）

## 📚 参考资源

- [PWA 官方文档](https://web.dev/progressive-web-apps/)
- [Service Worker API](https://developer.mozilla.org/zh-CN/docs/Web/API/Service_Worker_API)
- [Web App Manifest](https://developer.mozilla.org/zh-CN/docs/Web/Manifest)
