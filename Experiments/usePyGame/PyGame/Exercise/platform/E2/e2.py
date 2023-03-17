import pygame

# 初始化 Pygame
pygame.init()
clock = pygame.time.Clock()
# 游戏窗口尺寸
WIDTH = 800
HEIGHT = 600

# 定义颜色
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# 创建游戏窗口
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platformer Game")

# 角色相关参数
player_width = 50
player_height = 50
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - player_height
player_speed = 10
player_jump_power = 10
player_jump = False
player_jump_count = 10
# player_jump_count = 2  # 修改跳跃次数为2


# 游戏循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # 检测按键事件
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # 处理角色跳跃
                if not player_jump:
                    player_jump = True
                    player_jump_count = 10

    # 游戏逻辑
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    # 处理角色跳跃
    if player_jump:
        if player_jump_count >= -10:
            player_y -= (player_jump_count * abs(player_jump_count)) * 0.5
            player_jump_count -= 1
        else:
            player_jump = False
            player_jump_count = 10

    # 绘制游戏窗口
    window.fill(WHITE)
    pygame.draw.rect(window, BLUE, (player_x, player_y, player_width, player_height))
    pygame.display.update()
    clock.tick(30)

# 退出游戏
pygame.quit()


