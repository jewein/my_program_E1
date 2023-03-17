import pygame
import sys

pygame.init()

# 设置游戏窗口
window_size = (400, 300)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("鼠标按键示例")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 获取鼠标按键状态
    left_click, middle_click, right_click = pygame.mouse.get_pressed()

    # 在控制台输出鼠标按键状态
    if left_click:
        print("左键被按下")
    if middle_click:
        print("中键被按下")
    if right_click:
        print("右键被按下")

    # 清空屏幕并绘制内容
    screen.fill((255, 255, 255))
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()