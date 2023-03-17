



import pygame
import sys

pygame.init()

# 设置窗口大小和标题
window_width, window_height = 400, 300
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("colliderect()示例")

# 定义颜色
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# 创建两个矩形
rect1 = pygame.Rect(50, 100, 100, 50)  # 左上角坐标 (50, 100)，宽度 100，高度 50
rect2 = pygame.Rect(200, 150, 80, 60)  # 左上角坐标 (200, 150)，宽度 80，高度 60

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 清空屏幕
    screen.fill(WHITE)

    # 在屏幕上绘制矩形
    pygame.draw.rect(screen, RED, rect1)
    pygame.draw.rect(screen, RED, rect2)

    mouse_x, mouse_y = pygame.mouse.get_pos()
    rect2.left = mouse_x
    rect2.top = mouse_y


    # 检查两个矩形是否相交
    if rect1.colliderect(rect2):
        print("发生碰撞！")
    else:
        print("未发生碰撞！")

    # 刷新屏幕
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()