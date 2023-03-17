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
river_y = int(window_height * 0.4)

# 初始化玩家位置
player_width, player_height = player_image.get_size()
player_x = window_width // 2
player_y = window_height // 2
# 定义波纹相关参数
ripple_max_radius = 128
ripple_alpha = 128
ripple_list = []
frame_count = 0
generate_ripple_interval = 8  # 每隔10帧生成一个波纹

# 初始化玩家位置
player_width, player_height = player_image.get_size()
player_x = window_width // 2
player_y = window_height // 4

# 用于记录上一帧玩家位置的变量
prev_player_x = player_x
prev_player_y = player_y

# 游戏循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 获取鼠标位置
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # 更新玩家位置
    prev_player_x = player_x
    prev_player_y = player_y
    player_x += (mouse_x - player_x) * 0.5
    player_y += (mouse_y - player_y) * 0.5

    # 检查玩家是否越过河岸
    if player_y + player_height > river_y:
    # 检查玩家是否移动，只有移动时才产生波纹
        if player_x != prev_player_x or player_y != prev_player_y:
            frame_count += 1
            if not frame_count % generate_ripple_interval:
                # 创建波纹
                ripple_list.append((player_x+25, player_y+80, 8))

    # 更新波纹状态
    updated_ripples = []
    for ripple in ripple_list:
        ripple_x, ripple_y, ripple_radius = ripple
        ripple_radius += 5  # 波纹半径每次扩大5像素

        if ripple_radius <= ripple_max_radius:
            updated_ripples.append((ripple_x, ripple_y, ripple_radius))
    ripple_list = updated_ripples

    # 清空窗口
    window.fill('cyan')


    if player_y + player_height-8 > river_y:
    # 绘制倒影
    # reflection_y = river_y + (river_y - player_y) - reflection_height
        reflection_y = player_y + 80
        window.blit(reflection_image, (player_x, reflection_y,50,80),(0,8,50,80))
    else:
        reflection_y = player_y + 88
        window.blit(reflection_image, (player_x, reflection_y))

    # 绘制波纹
    for ripple in ripple_list:
        ripple_x, ripple_y, ripple_radius = ripple
        ripple_alpha = int(max(0, 128 - ripple_radius * 1))
        pygame.draw.circle(window, (0, 233, 255, ripple_alpha), (ripple_x, ripple_y), ripple_radius,width=(171-ripple_radius)//42)

    # 绘制河岸
    pygame.draw.line(window, (0, 128, 0), (0, river_y), (window_width, river_y), 1)


    pygame.draw.rect(window, (128, 233, 128), pygame.Rect(0, 0, window_width, river_y), 0)


    # 添加淡蓝色透明层
    alpha_surface = pygame.Surface((window_width, window_height))
    alpha_surface.fill('blue')
    alpha_surface.set_alpha(50)
    window.blit(alpha_surface, (0, river_y))

    if player_y + player_height-8 > river_y:
        # 绘制玩家
        window.blit(player_image, (player_x, player_y,50,80),(0,0,50,80))
    else:
    # 绘制玩家
        window.blit(player_image, (player_x, player_y))



    pygame.display.flip()
    # pygame.time.delay(10)
    pygame.time.Clock().tick(30)

# 退出游戏
pygame.quit()
