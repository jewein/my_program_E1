import pygame

# 初始化Pygame
pygame.init()

# 窗口大小
window_width = 800
window_height = 600

# 创建游戏窗口
screen = pygame.display.set_mode((window_width, window_height))

# 设置窗口标题
pygame.display.set_caption("我的游戏窗口")

# 游戏主循环
running = True
while running:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # 如果玩家点击关闭按钮，则终止游戏主循环
            running = False

    # 填充背景色（这里使用白色）
    screen.fill((255, 128,255))

    # 在这里可以添加你的游戏绘制逻辑
    # 例如：绘制角色、敌人、背景等等

    # 更新显示
    pygame.display.flip()

# 退出Pygame
pygame.quit()
