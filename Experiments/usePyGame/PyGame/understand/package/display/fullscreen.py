import pygame

pygame.init()

# 设置屏幕尺寸
screen_width, screen_height = 800, 600

# 创建显示窗口，并设置为全屏模式
# screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
screen = pygame.display.set_mode((screen_width, screen_height))

# 游戏主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # 检测按下 Alt + Enter 键，切换全屏模式
            if event.key == pygame.K_RETURN and event.mod & pygame.KMOD_ALT:
                if screen.get_flags() & pygame.FULLSCREEN:
                    pygame.display.set_mode((screen_width, screen_height))
                else:
                    pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

    # 绘制游戏画面这里省略
    # ...

    # 刷新屏幕显示
    pygame.display.flip()

pygame.quit()
