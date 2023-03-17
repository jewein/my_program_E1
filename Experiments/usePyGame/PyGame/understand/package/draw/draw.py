import pygame
from pygame.locals import *

pygame.init()

# 设置屏幕尺寸
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Draw Example")

# 设置颜色
white = (255, 255, 255)
red = (255, 0, 0)

# 绘制矩形
rect = pygame.Rect(100, 100, 200, 150)
pygame.draw.rect(screen, red, rect, 2)  # 绘制一个红色的矩形，边框宽度为2

# 绘制圆形
center = (400, 300)
radius = 100
pygame.draw.circle(screen, white, center, radius)  # 绘制一个白色的圆形

pygame.display.flip()

# 游戏循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

pygame.quit()
