import pygame
from pygame import image
from pygame import transform

# 初始化Pygame
pygame.init()

# 创建窗口
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))

# 加载玩家图像和倒影图像
player_image = image.load('../image.png')
reflection_image = transform.flip(player_image, False, True)

# 玩家初始位置
player_x = window_width // 2
player_y = window_height // 2

# 判断是否在水面上
on_water = False

# 游戏循环
running = True
while running:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 更新玩家位置
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= 2
    if keys[pygame.K_RIGHT]:
        player_x += 2
    if keys[pygame.K_UP]:
        player_y -= 2
    if keys[pygame.K_DOWN]:
        player_y += 2

    # 检测玩家是否在水面上
    if player_y <= window_height // 2:
        on_water = True
    else:
        on_water = False

    # 清空窗口
    window.fill((0, 0, 0))

    # 绘制玩家图像
    window.blit(player_image, (player_x, player_y))

    # 绘制倒影图像
    if on_water:
        reflection_y = window_height - player_y
        window.blit(reflection_image, (player_x, reflection_y))

    # 更新窗口显示
    pygame.display.flip()
    pygame.time.Clock().tick(60)

# 退出游戏
pygame.quit()
