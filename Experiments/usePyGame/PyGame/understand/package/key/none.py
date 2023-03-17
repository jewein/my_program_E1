import sys

import pygame

pygame.init()

# 设置窗口尺寸
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('Released Key Example')

# 颜色定义
WHITE = (255, 255, 255)

# 主循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # 键盘按下事件
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("Space key is pressed.")

        # 键盘释放事件
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                print("Space key is released.")

    # 填充屏幕为白色
    screen.fill(WHITE)
    pygame.display.flip()
