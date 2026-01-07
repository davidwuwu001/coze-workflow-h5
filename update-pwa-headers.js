// Node.js 脚本：批量更新所有 HTML 文件添加 PWA 支持
const fs = require('fs');
const path = require('path');

const pwaMetaTags = `
    <!-- PWA Meta Tags -->
    <meta name="description" content="AI 工作流聚合平台，提供各类智能工作流服务">
    <meta name="theme-color" content="#007AFF">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="default">
    <meta name="apple-mobile-web-app-title" content="Coze工作流">
    <link rel="manifest" href="/manifest.json">
    <link rel="apple-touch-icon" href="/images/icon-192x192.png">
    `;

const swScript = `
    <!-- PWA Service Worker 注册 -->
    <script>
        if ('serviceWorker' in navigator) {
            window.addEventListener('load', () => {
                navigator.serviceWorker.register('/sw.js')
                    .then(registration => {
                        console.log('Service Worker 注册成功:', registration.scope);
                    })
                    .catch(error => {
                        console.log('Service Worker 注册失败:', error);
                    });
            });
        }
    </script>`;

const htmlFiles = [
    'category.html',
    'detail.html',
    'favorites.html',
    'profile.html',
    'search.html',
    'settings.html',
    'member.html',
    'payment.html'
];

htmlFiles.forEach(file => {
    const filePath = path.join(__dirname, file);
    let content = fs.readFileSync(filePath, 'utf8');
    
    // 在 title 标签后添加 PWA meta 标签
    if (!content.includes('PWA Meta Tags')) {
        content = content.replace(
            /(<title>.*?<\/title>)/,
            `$1${pwaMetaTags}`
        );
    }
    
    // 在 </head> 前添加 Service Worker 注册脚本
    if (!content.includes('Service Worker 注册')) {
        content = content.replace(
            /<\/head>/,
            `${swScript}\n</head>`
        );
    }
    
    fs.writeFileSync(filePath, content, 'utf8');
    console.log(`✅ 已更新: ${file}`);
});

console.log('\n🎉 所有文件已更新完成！');
