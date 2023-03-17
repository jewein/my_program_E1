import pygame
import random

# 初始化Pygame
pygame.init()

# 定义屏幕大小
screen_width = 800
screen_height = 600

# 创建游戏窗口
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Shoot 'em Up!")

# 定义颜色
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# 玩家相关参数
player_size = 50
player_pos = [screen_width // 2, screen_height - player_size * 2]

# 创建玩家
player = pygame.image.load("player.png")
player = pygame.transform.scale(player, (player_size, player_size))

# 子弹相关参数
bullet_size = 10
bullet_pos = [0, 0]
bullet_speed = 10
bullet_state = "ready"

# 创建敌人
enemy_size = 50
enemy_pos = [random.randint(0, screen_width - enemy_size), 0]
enemy_list = [enemy_pos]

# 定义游戏结束状态
game_over = False

# 游戏主循环
while not game_over:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        # 监听按键事件
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_pos[0] -= player_size // 2
            elif event.key == pygame.K_RIGHT:
                player_pos[0] += player_size // 2
            elif event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_pos[0] = player_pos[0] + player_size // 2 - bullet_size // 2
                    bullet_pos[1] = player_pos[1]
                    bullet_state = "fire"

    # 更新玩家位置
    player_rect = pygame.Rect(player_pos[0], player_pos[1], player_size, player_size)

    # 更新子弹位置
    if bullet_state == "fire":
        bullet_pos[1] -= bullet_speed

    # 绘制背景
    screen.fill(WHITE)

    # 绘制玩家
    screen.blit(player, player_pos)

    # 绘制子弹
    if bullet_state == "fire":
        pygame.draw.rect(screen, RED, (bullet_pos[0], bullet_pos[1], bullet_size, bullet_size))

    # 绘制敌人
    for enemy_pos in enemy_list:
        pygame.draw.rect(screen, (0, 0, 255), (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))
        enemy_pos[1] += 5

    # 更新屏幕
    pygame.display.update()
    pygame.time.Clock().tick(60)
