import pygame
import sys

# 初始化 Pygame
pygame.init()

# 设置窗口尺寸
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# 游戏主循环
while True:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            key = event.key
            key_name = pygame.key.name(key)
            key_ascii = ord(key_name) if len(key_name) == 1 else None
            print(f"Key: {key_name}, ASCII: {key_ascii}")

    # 填充背景色
    screen.fill((255, 255, 255))

    # 更新屏幕显示
    pygame.display.flip()
