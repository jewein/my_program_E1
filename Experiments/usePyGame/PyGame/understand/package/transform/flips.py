import pygame
from pygame import image
from pygame import transform

# 初始化Pygame
pygame.init()

# 创建窗口
window = pygame.display.set_mode((800, 600))

# 加载图像
my_image = image.load('image.png')

# 水平翻转图像
flipped_image = transform.flip(my_image, True, False)
flipped_image2 = transform.flip(my_image, False, True)

# 显示图像
window.blit(my_image, (0, 0))
window.blit(flipped_image, (400, 0))
window.blit(flipped_image2, (0, 300))

pygame.display.flip()

# 游戏循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
