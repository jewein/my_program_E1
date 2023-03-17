import pygame
import sys

pygame.init()

# 设置窗口尺寸
window_size = (400, 300)
screen = pygame.display.set_mode(window_size, pygame.RESIZABLE | pygame.DOUBLEBUF)
pygame.display.set_caption("Mouse Position Demo")

# 定义颜色
WHITE = (255, 255, 255)
RED = (255, 0, 0)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 获取鼠标位置
    mouse_x, mouse_y = pygame.mouse.get_pos()

    screen.fill(WHITE)

    # 在鼠标位置绘制一个小方块
    pygame.draw.rect(screen, RED, (mouse_x, mouse_y, 20, 20))
    print(mouse_x, mouse_y)

    pygame.display.flip()
    clock.tick(60)
