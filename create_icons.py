#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""使用 PIL 创建 PWA 图标"""

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    print("❌ 需要安装 Pillow 库")
    print("请运行: pip3 install Pillow")
    exit(1)

import os

def create_gradient(width, height):
    """创建渐变背景"""
    image = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(image)
    
    # 从紫色到蓝色的渐变
    for y in range(height):
        # 计算当前行的颜色
        ratio = y / height
        r = int(102 + (118 - 102) * ratio)  # 667eea -> 764ba2
        g = int(126 + (75 - 126) * ratio)
        b = int(234 + (162 - 234) * ratio)
        
        draw.line([(0, y), (width, y)], fill=(r, g, b))
    
    return image

def create_icon(size):
    """创建指定尺寸的图标"""
    # 创建渐变背景
    img = create_gradient(size, size)
    draw = ImageDraw.Draw(img)
    
    # 绘制圆角矩形（iOS 风格）
    # 这里简化处理，直接使用方形
    
    # 绘制白色文字 "AI"
    font_size = size // 3
    try:
        # 尝试使用系统字体
        font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", font_size)
    except:
        try:
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", font_size)
        except:
            # 使用默认字体
            font = ImageFont.load_default()
    
    text = "AI"
    
    # 获取文字边界框
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    # 计算居中位置
    x = (size - text_width) // 2
    y = (size - text_height) // 2 - font_size // 8
    
    # 绘制白色文字
    draw.text((x, y), text, fill='white', font=font)
    
    # 在文字下方绘制小图标
    icon_y = y + text_height + size // 20
    icon_size = size // 8
    
    # 绘制简单的工作流图标（三个圆点连线）
    dot_radius = icon_size // 3
    spacing = icon_size
    start_x = size // 2 - spacing
    
    for i in range(3):
        dot_x = start_x + i * spacing
        draw.ellipse(
            [dot_x - dot_radius, icon_y - dot_radius, 
             dot_x + dot_radius, icon_y + dot_radius],
            fill='white'
        )
        
        # 绘制连接线
        if i < 2:
            draw.line(
                [dot_x + dot_radius, icon_y, 
                 dot_x + spacing - dot_radius, icon_y],
                fill='white',
                width=max(1, size // 100)
            )
    
    return img

def main():
    """主函数"""
    sizes = [72, 96, 128, 144, 152, 192, 384, 512]
    output_dir = 'images'
    
    # 确保输出目录存在
    os.makedirs(output_dir, exist_ok=True)
    
    print('🎨 开始生成 PWA 图标...\n')
    
    for size in sizes:
        filename = f'icon-{size}x{size}.png'
        filepath = os.path.join(output_dir, filename)
        
        # 创建图标
        icon = create_icon(size)
        
        # 保存图标
        icon.save(filepath, 'PNG')
        print(f'✅ 已创建: {filename}')
    
    print(f'\n🎉 完成！所有图标已保存到 {output_dir}/ 目录')
    print('\n💡 提示：你可以使用 generate-icons.html 在浏览器中生成更精美的图标')

if __name__ == '__main__':
    main()
