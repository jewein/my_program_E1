import pygame
import sys

pygame.init()

# 设置窗口尺寸
window_size = (400, 300)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('pygame.key.name() 示例')

# 主游戏循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # 检查按键事件
        if event.type == pygame.KEYDOWN:
            # 获取键盘按下的键的数值
            keycode = event.key

            # 使用pygame.key.name()将键的数值转换为键名
            keyname = pygame.key.name(keycode)

            print(f"键值：{keycode}, 键名：{keyname}")

    # 在这里可以处理其他游戏逻辑、绘制等

    pygame.display.update()
