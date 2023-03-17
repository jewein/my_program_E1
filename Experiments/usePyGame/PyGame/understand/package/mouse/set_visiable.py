import pygame
import sys

pygame.init()

# 创建游戏窗口
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("隐藏/显示鼠标示例")

# 将鼠标初始设置为可见
pygame.mouse.set_visible(True)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # 按下空格键切换鼠标可见性
            if event.key == pygame.K_SPACE:
                mouse_visible = pygame.mouse.get_visible()
                pygame.mouse.set_visible(not mouse_visible)

    screen.fill((255, 255, 255))
    pygame.display.flip()

pygame.quit()
sys.exit()
