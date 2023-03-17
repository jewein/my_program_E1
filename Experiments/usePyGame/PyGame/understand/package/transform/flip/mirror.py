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
player_image = image.load('../player.png').convert_alpha()
reflection_image = transform.flip(player_image, True, False)
reflection_width = int(player_image.get_width() * 0.8)  # 倒影宽度为玩家图像宽度的80%

# 设置河岸位置
river_x = window_width // 2

# 初始化玩家位置
player_width, player_height = player_image.get_size()
player_x = window_width // 4
player_y = window_height // 2 - player_height // 2

# 游戏循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 获取鼠标位置
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # 更新玩家位置
    player_x += (mouse_x - player_x) * 0.1
    player_y += (mouse_y - player_y) * 0.1

    # 限制玩家在窗口范围内移动
    if player_x < 0:
        player_x = 0
    elif player_x + player_width > river_x:
        player_x = river_x - player_width

    # 清空窗口
    window.fill((255, 255,255))

    # 绘制河岸
    pygame.draw.line(window, (0, 128, 0), (river_x, 0), (river_x, window_height), 3)
    pygame.draw.rect(window, (233, 244, 255), pygame.Rect(river_x, 0, window_width - river_x, window_height), 0)

    # 绘制玩家
    window.blit(player_image, (player_x, player_y))

    # 绘制倒影
    reflection_x = river_x + (river_x - player_x) - reflection_width
    window.blit(reflection_image, (reflection_x, player_y))

    pygame.display.flip()

# 退出游戏
pygame.quit()
