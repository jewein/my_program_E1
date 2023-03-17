import pygame
import sys

pygame.init()

# 设置游戏窗口大小
window_size = (400, 300)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Move Rect Example")

# 定义矩形的属性
rect_width = 50
rect_height = 50
rect_color = (255, 0, 0)  # 红色
initial_x = 175
initial_y = 125

# 创建一个初始位置为(175, 125)的矩形
rect = pygame.Rect(initial_x, initial_y, rect_width, rect_height)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 清空屏幕
    screen.fill((255, 255, 255))  # 白色背景

    # 绘制矩形
    pygame.draw.rect(screen, rect_color, rect)

    # 更新显示
    pygame.display.flip()
    pygame.time.Clock().tick(60)

    # 等待一段时间


    # 移动矩形到新位置
    new_x = initial_x + 1
    new_y = initial_y + 1
    rect = rect.move(new_x - rect.x, new_y - rect.y)

    # 更新初始位置，以便下次循环使用
    initial_x = new_x
    initial_y = new_y


pygame.quit()