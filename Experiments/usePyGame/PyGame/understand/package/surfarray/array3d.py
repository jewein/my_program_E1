import pygame
import numpy as np

# 初始化Pygame
pygame.init()

# 定义窗口尺寸
window_size = (400, 300)

# 创建一个窗口
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("surfarray.array3d 示例")

# 加载图像
image_path = "image.png"  # 请将该路径替换为你自己的图像路径
image = pygame.image.load(image_path)

# 在窗口上绘制图像
screen.blit(image, (0, 0))
pygame.display.flip()

# 将图像转换为三维NumPy数组
image_array = pygame.surfarray.array3d(image)

# 查看图像数组的形状和像素值
print("图像数组形状:", image_array.shape)
print("图像数组中的像素值:")
print(image_array)

# 事件循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# 退出Pygame
pygame.quit()
