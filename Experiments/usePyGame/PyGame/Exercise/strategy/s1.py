import pygame
import random

# 游戏初始化
pygame.init()

# 设置游戏窗口尺寸
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("战略游戏示例")

# 定义颜色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# 定义游戏角色
player = pygame.Rect(50, 50, 50, 50)
enemy = pygame.Rect(700, 50, 50, 50)

# 游戏主循环
running = True
while running:
    screen.fill(WHITE)

    # 事件处理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 玩家移动
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= 5
    if keys[pygame.K_RIGHT]:
        player.x += 5
    if keys[pygame.K_UP]:
        player.y -= 5
    if keys[pygame.K_DOWN]:
        player.y += 5

    # 敌人随机移动
    enemy.x += random.randint(-3, 3)
    enemy.y += random.randint(-3, 3)

    # 边界检测
    if player.x < 0:
        player.x = 0
    elif player.x > width - player.width:
        player.x = width - player.width
    if player.y < 0:
        player.y = 0
    elif player.y > height - player.height:
        player.y = height - player.height

    if enemy.x < 0:
        enemy.x = 0
    elif enemy.x > width - enemy.width:
        enemy.x = width - enemy.width
    if enemy.y < 0:
        enemy.y = 0
    elif enemy.y > height - enemy.height:
        enemy.y = height - enemy.height

    # 绘制角色
    pygame.draw.rect(screen, BLACK, player)
    pygame.draw.rect(screen, BLACK, enemy)

    # 更新画面
    pygame.display.flip()
    pygame.time.Clock().tick(60)

# 游戏结束
pygame.quit()
