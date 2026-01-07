#!/bin/bash
# 使用 ImageMagick 创建占位图标
# 如果没有安装 ImageMagick，请运行: brew install imagemagick

sizes=(72 96 128 144 152 192 384 512)

for size in "${sizes[@]}"; do
    convert -size ${size}x${size} \
        gradient:'#667eea-#764ba2' \
        -gravity center \
        -pointsize $((size/4)) \
        -fill white \
        -font Arial-Bold \
        -annotate +0+0 "AI" \
        icon-${size}x${size}.png
    echo "✅ 创建了 icon-${size}x${size}.png"
done

echo "🎉 所有图标创建完成！"
