import pygame

# 初始化 Pygame
pygame.init()

# 设置游戏窗口的尺寸
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE | pygame.DOUBLEBUF| pygame.HWSURFACE)
pygame.display.set_caption("Platform Game")

# 定义颜色
bg_color = (0, 0, 0)  # 黑色
player_color = (255, 255, 255)  # 白色

# 定义玩家的属性
player_width = 50
player_height = 50
player_x = (screen_width - player_width) // 2
player_y = screen_height - player_height

player_speed = 15
player_y_velocity = 0
jump_height = 35
is_jumping = False

clock = pygame.time.Clock()

# 游戏主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_SPACE] and not is_jumping:
        is_jumping = True
        player_y_velocity = -jump_height



        # 处理按键事件
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_LEFT:
        #         player_x -= player_speed
        #     elif event.key == pygame.K_RIGHT:
        #         player_x += player_speed
        #     elif event.key == pygame.K_SPACE and not is_jumping:
        #         is_jumping = True
        #         player_y_velocity = -jump_height

        # if event.type == pygame.KEYUP:
        #     if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        #         player_x += 0  # 停止水平移动

    # 更新玩家的位置, 不能离开屏幕


    player_y += player_y_velocity
    player_y_velocity += 1  # 简单的重力效果

    if player_x < 0:
        player_x = 0
    elif player_x > screen_width - player_width:
        player_x = screen_width - player_width

    # 碰撞检测
    if player_y > screen_height - player_height:
        player_y = screen_height - player_height
        is_jumping = False

    # 绘制背景和玩家
    screen.fill(bg_color)
    pygame.draw.rect(screen, player_color, (player_x, player_y, player_width, player_height))

    # 更新屏幕显示
    pygame.display.flip()

    # 控制游戏帧率
    clock.tick(60)

# 退出游戏
pygame.quit()
