import pygame
pygame.init()

# 设置窗口和角色
win_width, win_height = 800, 600
win = pygame.display.set_mode((win_width, win_height))
player_x, player_y = 50, 50
player_speed = 5

# 创建时钟对象
clock = pygame.time.Clock()

# 初始化帧率和绘制帧率
logic_fps = 60
draw_fps = 5
draw_clock = pygame.time.Clock()
draw_counter = 0

# 游戏主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # 检测玩家是否按下了键盘按键，来调整绘制帧率
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                draw_fps += 10
            elif event.key == pygame.K_DOWN:
                draw_fps = max(1, draw_fps - 10)

    # 控制游戏逻辑帧率
    clock.tick(logic_fps)

    # 获取按下的键盘按键
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # 绘制角色和更新显示，但控制绘制帧率
    draw_counter += 1
    if draw_counter >= logic_fps / draw_fps:
        win.fill((0, 0, 0))
        pygame.draw.circle(win, (255, 0, 0), (player_x, player_y), 20)
        pygame.display.update()
        draw_counter = 0

    # 控制绘制帧率
    draw_clock.tick(draw_fps)

pygame.quit()
