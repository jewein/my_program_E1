import pygame
import sys

pygame.init()

# 游戏窗口的宽度和高度
window_width = 800
window_height = 600

# 颜色定义
white = (255, 255, 255)
black = (0, 0, 0)

# 初始化游戏窗口
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("飞机游戏示例")

# 飞机的初始位置和速度
plane_x = window_width // 2
plane_y = window_height // 2
plane_speed = 5

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 获取当前所有按键的状态
    keys = pygame.key.get_pressed()

    # 根据按键状态来移动飞机
    if keys[pygame.K_UP]:
        plane_y -= plane_speed
    if keys[pygame.K_DOWN]:
        plane_y += plane_speed
    if keys[pygame.K_LEFT]:
        plane_x -= plane_speed
    if keys[pygame.K_RIGHT]:
        plane_x += plane_speed

    # 清屏
    window.fill(white)

    # 绘制飞机
    pygame.draw.rect(window, black, (plane_x, plane_y, 50, 50))

    # 更新显示
    pygame.display.update()

    # 控制游戏帧率
    clock.tick(60)
