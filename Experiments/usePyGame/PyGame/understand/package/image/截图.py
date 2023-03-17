import pygame

# 初始化Pygame
pygame.init()

# 设置游戏窗口尺寸
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Screen Capture Example")

image=pygame.image.load("sprite.png")

# 游戏主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:  # 当按下 's' 键时进行截图
                # 获取当前显示的表面
                screen.blit(image, (0, 0))
                # 将表面保存为图像文件（这里保存为png格式）
                pygame.image.save(screen, "screenshot.png")
                print("截图已保存为screenshot.png")

    # 绘制游戏内容（这里略过）

    # 更新游戏窗口
    pygame.display.flip()

# 退出Pygame
pygame.quit()








