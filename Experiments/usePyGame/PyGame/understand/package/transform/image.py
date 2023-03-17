import pygame
from pygame import image

# 初始化Pygame
pygame.init()

# 创建窗口
window = pygame.display.set_mode((800, 600))

# 加载图像
my_image = image.load('image.png')

# 显示图像
window.blit(my_image, (0, 0))
pygame.display.flip()

# 游戏循环
running = True
x=0
y=0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    x+=1
    y+=1
    window.blit(my_image, (x, y))
    pygame.display.flip()
    pygame.time.Clock().tick(60)