#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""批量更新 HTML 文件添加 PWA 支持"""

import os
import re

PWA_META_TAGS = '''
    <!-- PWA Meta Tags -->
    <meta name="description" content="AI 工作流聚合平台，提供各类智能工作流服务">
    <meta name="theme-color" content="#007AFF">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="default">
    <meta name="apple-mobile-web-app-title" content="Coze工作流">
    <link rel="manifest" href="/manifest.json">
    <link rel="apple-touch-icon" href="/images/icon-192x192.png">
    '''

SW_SCRIPT = '''
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
    </script>'''

HTML_FILES = [
    'category.html',
    'detail.html',
    'favorites.html',
    'search.html',
    'settings.html',
    'member.html',
    'payment.html'
]

def update_html_file(filename):
    """更新单个 HTML 文件"""
    if not os.path.exists(filename):
        print(f'⚠️  文件不存在: {filename}')
        return False
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False
    
    # 添加 PWA Meta 标签
    if 'PWA Meta Tags' not in content:
        # 在 title 标签后添加
        content = re.sub(
            r'(<title>.*?</title>)',
            r'\1' + PWA_META_TAGS,
            content,
            count=1
        )
        modified = True
    
    # 添加 Service Worker 注册脚本
    if 'Service Worker 注册' not in content:
        # 在 </head> 前添加
        content = re.sub(
            r'</head>',
            SW_SCRIPT + '\n</head>',
            content,
            count=1
        )
        modified = True
    
    if modified:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'✅ 已更新: {filename}')
        return True
    else:
        print(f'ℹ️  无需更新: {filename}')
        return False

def main():
    """主函数"""
    print('🚀 开始批量更新 HTML 文件...\n')
    
    updated_count = 0
    for filename in HTML_FILES:
        if update_html_file(filename):
            updated_count += 1
    
    print(f'\n🎉 完成！共更新了 {updated_count} 个文件')

if __name__ == '__main__':
    main()
