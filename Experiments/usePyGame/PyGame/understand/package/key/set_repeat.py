import pygame
import sys

pygame.init()

# 设置窗口大小和标题
window_size = (400, 300)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("键盘重复事件示例")

# 设置键盘重复事件，延迟时间为300毫秒，重复间隔为100毫秒
pygame.key.set_repeat(1000, 0)

running = True

# 定义按键状态的标记
up_key_pressed = False
down_key_pressed = False
left_key_pressed = False
right_key_pressed = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # 检查键盘按键按下和释放事件
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                up_key_pressed = True
            elif event.key == pygame.K_DOWN:
                down_key_pressed = True
            elif event.key == pygame.K_LEFT:
                left_key_pressed = True
            elif event.key == pygame.K_RIGHT:
                right_key_pressed = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                up_key_pressed = False
            elif event.key == pygame.K_DOWN:
                down_key_pressed = False
            elif event.key == pygame.K_LEFT:
                left_key_pressed = False
            elif event.key == pygame.K_RIGHT:
                right_key_pressed = False

    # 根据按键状态更新游戏对象的状态
    if up_key_pressed:
        print("向上键被按下")
    if down_key_pressed:
        print("向下键被按下")
    if left_key_pressed:
        print("向左键被按下")
    if right_key_pressed:
        print("向右键被按下")

    pygame.display.flip()

    pygame.time.Clock().tick(20)

pygame.quit()
sys.exit()
