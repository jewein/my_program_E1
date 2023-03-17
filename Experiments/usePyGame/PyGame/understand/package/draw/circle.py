import pygame
from pygame.locals import *

pygame.init()

# 设置屏幕尺寸
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Draw Circle Example")

# 设置颜色
red = (255, 0, 0)
blue = (0, 0, 255)

# 绘制填充圆
center = (400, 300)
radius = 100
pygame.draw.circle(screen, red, center, radius)  # 绘制一个红色的填充圆

# 绘制空心圆
center = (200, 200)
radius = 50
width = 1
pygame.draw.circle(screen, blue, center, radius, width)  # 绘制一个蓝色的空心圆，边框宽度为3

pygame.display.flip()

# 游戏循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

pygame.quit()
