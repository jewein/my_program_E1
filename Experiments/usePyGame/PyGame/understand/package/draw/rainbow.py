import pygame
from pygame.locals import *

pygame.init()

# 设置屏幕尺寸
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Rainbow Gradient")

# 定义彩虹颜色
colors = [
    (255, 0, 0),    # 红色
    (255, 165, 0),  # 橙色
    (255, 255, 0),  # 黄色
    (0, 128, 0),    # 绿色
    (0, 0, 255),    # 蓝色
    (75, 0, 130),   # 靛蓝色
    (238, 130, 238) # 紫色
]

# 渐变颜色的行数
num_rows = len(colors)

# 游戏循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # 清空屏幕
    screen.fill((0, 0, 0))

    # 绘制彩虹渐变
    row_height = screen_height // num_rows
    for i in range(num_rows):
        rect = pygame.Rect(0, i * row_height, screen_width, row_height)
        pygame.draw.rect(screen, colors[i], rect)

    # 更新屏幕显示
    pygame.display.flip()

pygame.quit()
