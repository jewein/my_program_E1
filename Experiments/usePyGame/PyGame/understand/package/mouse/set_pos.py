import pygame
import sys

pygame.init()

# 设置游戏窗口的尺寸
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Set Mouse Position Example")

# 游戏主循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 在这里设置鼠标位置
    mouse_x, mouse_y = pygame.mouse.get_pos()
    new_mouse_x, new_mouse_y = 400, 300  # 设置新的鼠标位置为窗口中心
    pygame.mouse.set_pos(new_mouse_x, new_mouse_y)

    # 绘制背景和其他游戏元素
    screen.fill((255, 255, 255))  # 白色背景
    pygame.draw.circle(screen, (255, 0, 0), (mouse_x, mouse_y), 20)  # 绘制鼠标当前位置的红色圆点

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()


