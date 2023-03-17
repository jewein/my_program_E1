import pygame
from pygame.locals import *

pygame.init()

# 加载两个图像
image1 = pygame.image.load('image1.png')
image2 = pygame.image.load('image2.png')

# 创建两个图像的掩码
mask1 = pygame.mask.from_surface(image1)
mask2 = pygame.mask.from_surface(image2)

# 假设图像1的位置为(100, 100)，图像2的位置为(200, 200)
offset = (200 - 100, 200 - 100)

# 检测图像1和图像2是否发生了碰撞
if mask1.overlap(mask2, offset):
    print("发生碰撞！")
else:
    print("没有碰撞。")





pygame.quit()
