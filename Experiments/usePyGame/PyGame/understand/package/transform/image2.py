import pygame
from pygame.locals import *
import sys

# 初始化Pygame
pygame.init()

# 设置窗口尺寸
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('Pygame绘制中文')

# 设置字体
font_size = 36
font = pygame.font.SysFont(None, font_size)

# 设置文字内容
text = "你好，Pygame！"  # 中文文字内容

# 渲染文字
text_render = font.render(text, True, (255, 255, 255))

# 文字位置
text_position = text_render.get_rect()
text_position.centerx = screen.get_rect().centerx
text_position.centery = screen.get_rect().centery

# 游戏循环
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # 填充背景颜色
    screen.fill((0, 0, 0))

    # 绘制文字
    screen.blit(text_render, text_position)

    # 更新显示
    pygame.display.flip()
