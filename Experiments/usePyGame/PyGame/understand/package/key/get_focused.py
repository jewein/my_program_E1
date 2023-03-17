import pygame
import sys

pygame.init()

# 设置窗口尺寸
window_size = (400, 300)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Get Focused Example")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 检查窗口焦点状态
    is_focused = pygame.key.get_focused()

    # 在终端输出焦点状态
    print("Window is focused:", is_focused)

    # 在窗口上绘制焦点状态
    screen.fill((0, 0, 0))  # 填充黑色背景
    font = pygame.font.SysFont(None, 30)
    text = font.render("Window is focused: " + str(is_focused), True, (255, 255, 255))
    screen.blit(text, (50, 50))  # 在窗口上绘制文本
    pygame.display.flip()  # 更新屏幕显示

    pygame.time.delay(100)  # 稍微延迟一下，以降低CPU占用
