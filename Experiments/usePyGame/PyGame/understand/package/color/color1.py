import pygame

# 创建一个蓝色
blue_color = pygame.Color("cyan")

# 获取颜色的RGB值
print(blue_color.r)  # 输出 0
print(blue_color.g)  # 输出 0
print(blue_color.b)  # 输出 255

# 设置颜色的透明度（Alpha值），0表示完全透明，255表示完全不透明
blue_color.a = 128  # 设置透明度为半透明

# 获取颜色的十六进制代码
# print(blue_color.hex)  # 输出 #0000FF
print(blue_color.hsva)  # 输出 (180.0, 1.0, 1.0, 0.5)




