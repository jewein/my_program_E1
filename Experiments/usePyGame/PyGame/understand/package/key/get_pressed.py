import pygame
import sys

pygame.init()

# 设置游戏窗口
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("按键检测示例")

# 定义颜色
WHITE = (255, 255, 255)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 获取当前所有按键的状态
    keys = pygame.key.get_pressed()

    # 检测方向键是否被按下
    if keys[pygame.K_UP]:
        print("向上键被按下！")
    if keys[pygame.K_DOWN]:
        print("向下键被按下！")
    if keys[pygame.K_LEFT]:
        print("向左键被按下！")
    if keys[pygame.K_RIGHT]:
        print("向右键被按下！")

    # 填充背景颜色
    screen.fill(WHITE)

    # 在这里可以添加更多游戏逻辑和绘制

    # 更新屏幕
    pygame.display.flip()

    clock.tick(20)  # 控制游戏循环的速度
