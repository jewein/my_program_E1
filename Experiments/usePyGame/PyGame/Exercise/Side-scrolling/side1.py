import pygame
import random

# 游戏初始化
pygame.init()

# 设置游戏窗口尺寸
screen_width = 800
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Side-scrolling Game")

# 定义颜色
WHITE = (255, 255, 255)

# 加载游戏资源
player_image = pygame.image.load("player.png")
player_rect = player_image.get_rect()
player_rect.center = (screen_width // 2, screen_height // 2)

enemy_image = pygame.image.load("enemy.png")
enemy_rect = enemy_image.get_rect()
enemy_rect.center = (screen_width, random.randint(50, screen_height - 50))

# 设置游戏循环
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 更新游戏逻辑

    # 移动玩家
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_rect.top > 0:
        player_rect.move_ip(0, -5)
    if keys[pygame.K_DOWN] and player_rect.bottom < screen_height:
        player_rect.move_ip(0, 5)

    # 移动敌人
    enemy_rect.move_ip(-3, 0)
    if enemy_rect.right < 0:
        enemy_rect.left = screen_width
        enemy_rect.top = random.randint(50, screen_height - 50)

    # 碰撞检测
    if player_rect.colliderect(enemy_rect):
        running = False

    # 绘制游戏画面
    screen.fill(WHITE)
    screen.blit(player_image, player_rect)
    screen.blit(enemy_image, enemy_rect)
    pygame.display.flip()

    # 控制游戏帧率
    clock.tick(60)

# 游戏结束
pygame.quit()
