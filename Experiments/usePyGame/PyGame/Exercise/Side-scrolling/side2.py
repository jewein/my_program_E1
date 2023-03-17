import pygame
import random

# 初始化 Pygame
pygame.init()

# 设置游戏窗口的宽度和高度
screen_width = 800
screen_height = 600

# 创建游戏窗口
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("魂斗罗")

# 加载玩家角色的图像
player_image = pygame.image.load("player.png")
player_rect = player_image.get_rect()
player_rect.centerx = screen_width // 2
player_rect.bottom = screen_height - 10

# 加载敌人角色的图像
enemy_image = pygame.image.load("enemy.png")
enemy_rect = enemy_image.get_rect()
enemy_rect.centerx = random.randint(50, screen_width - 50)
enemy_rect.centery = random.randint(50, screen_height // 2)

# 设置玩家的移动速度
player_speed = 5

# 游戏主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 获取键盘输入
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_rect.x += player_speed

    # 更新敌人的位置
    enemy_rect.y += 3
    if enemy_rect.top > screen_height:
        enemy_rect.centerx = random.randint(50, screen_width - 50)
        enemy_rect.centery = random.randint(50, screen_height // 2)

    # 碰撞检测
    if player_rect.colliderect(enemy_rect):
        print("游戏结束！")
        running = False

    # 绘制游戏场景
    screen.fill((0, 0, 0))
    screen.blit(player_image, player_rect)
    screen.blit(enemy_image, enemy_rect)
    pygame.display.flip()
    pygame.time.Clock().tick(60)

# 退出游戏
pygame.quit()






