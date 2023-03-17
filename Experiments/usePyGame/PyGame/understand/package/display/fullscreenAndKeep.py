import pygame

pygame.init()

# 设置原始窗口大小
screen_width, screen_height = 800, 600

# 创建显示窗口，并设置为全屏模式
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

# 加载精灵图像
sprite_image = pygame.image.load('sprite.png')
sprite_rect = sprite_image.get_rect()

# 设置精灵的初始位置
sprite_x = screen_width // 2 - sprite_rect.width // 2
sprite_y = screen_height // 2 - sprite_rect.height // 2

# 设置精灵的速度
sprite_speed = 5

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

    # 获取按键状态
    keys = pygame.key.get_pressed()
    # 移动精灵
    if keys[pygame.K_LEFT]:
        sprite_x -= sprite_speed
    if keys[pygame.K_RIGHT]:
        sprite_x += sprite_speed
    if keys[pygame.K_UP]:
        sprite_y -= sprite_speed
    if keys[pygame.K_DOWN]:
        sprite_y += sprite_speed

    # 绘制游戏背景
    screen.fill((255, 255, 255))  # 使用白色填充背景

    # 计算缩放后的精灵大小
    scaled_sprite_width = int(sprite_rect.width * screen_width / 800)  # 假设原始宽度是800
    scaled_sprite_height = int(sprite_rect.height * screen_height / 600)  # 假设原始高度是600

    # 缩放精灵图像
    scaled_sprite_image = pygame.transform.scale(sprite_image, (scaled_sprite_width, scaled_sprite_height))

    # 绘制缩放后的精灵图像
    screen.blit(scaled_sprite_image, (sprite_x, sprite_y))

    # 刷新屏幕显示
    pygame.display.flip()

pygame.quit()
