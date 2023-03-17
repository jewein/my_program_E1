import pygame
from pygame import image, transform

# 初始化Pygame
pygame.init()

# 创建窗口
window = pygame.display.set_mode((800, 600))

# 加载图像
my_image = image.load('image.png')

# 旋转图像
rotated_image = transform.rotate(my_image, 45)

# 显示旋转后的图像
window.blit(rotated_image, (0, 0))
pygame.display.flip()

# 游戏循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



