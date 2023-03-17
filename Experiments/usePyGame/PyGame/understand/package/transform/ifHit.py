import pygame
from pygame import image, transform, mask

x=20
y=20

# 初始化Pygame
pygame.init()

# 加载图像
my_image = image.load('image.png')

# 旋转图像
rotated_image = transform.rotate(my_image, 45)

# 创建掩码
mask_surface = pygame.mask.from_surface(rotated_image)

# 碰撞检测
point = (x, y)  # 碰撞点的坐标
collided = mask_surface.get_at(point)

if collided:
    print("发生碰撞")
else:
    print("没有发生碰撞")
