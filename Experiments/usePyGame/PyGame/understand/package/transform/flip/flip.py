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
reflection_image = transform.flip(player_image, False, True)
reflection_height = int(window_height * 0.4)  # 倒影高度为窗口高度的40%

# 设置河岸位置
river_y = int(window_height * 0.5)

# 初始化玩家位置
player_width, player_height = player_image.get_size()
player_x = window_width // 2
player_y = window_height // 4

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

    # 限制玩家在河岸上移动
    if player_y + player_height > river_y:
        player_y = river_y - player_height

    # 清空窗口
    window.fill('cyan')

    # 绘制河岸
    pygame.draw.line(window, (0, 128, 0), (0, river_y), (window_width, river_y), 3)
    pygame.draw.rect(window, (0, 128, 0), pygame.Rect(0, 0, window_width, river_y), 0)

    # 绘制玩家
    window.blit(player_image, (player_x, player_y))

    # 绘制倒影
    reflection_y = river_y + (river_y - player_y) - reflection_height
    # reflection_y = player_y + 100
    window.blit(reflection_image, (player_x, reflection_y))

    # 添加淡蓝色透明层
    alpha_surface = pygame.Surface((window_width, window_height))
    alpha_surface.fill((100, 100, 255))
    alpha_surface.set_alpha(100)
    window.blit(alpha_surface, (0, river_y))

    pygame.display.flip()

# 退出游戏
pygame.quit()
