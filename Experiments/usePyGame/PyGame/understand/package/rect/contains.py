import pygame

# 初始化pygame
pygame.init()

# 创建游戏窗口
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Contains Method Example")

# 定义角色的初始位置和大小
player_width, player_height = 50, 50
player_x, player_y = 375, 275
player_rect = pygame.Rect(player_x, player_y, player_width, player_height)

# 游戏主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 获取鼠标坐标
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # 创建鼠标矩形对象
    mouse_rect = pygame.Rect(mouse_x, mouse_y, 1, 1)

    # 检查鼠标是否在角色矩形范围内
    if player_rect.contains(mouse_rect):
        player_color = (0, 255, 0)  # 在范围内时将角色颜色设置为绿色
    else:
        player_color = (255, 0, 0)  # 不在范围内时将角色颜色设置为红色

    # 绘制角色和场景
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, player_color, player_rect)

    # 刷新显示
    pygame.display.flip()

# 退出游戏
pygame.quit()
