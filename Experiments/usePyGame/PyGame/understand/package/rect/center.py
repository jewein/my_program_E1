import pygame

# 初始化pygame
pygame.init()

# 屏幕宽度和高度
screen_width = 800
screen_height = 600

# 创建游戏窗口
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Center Example")

# 定义角色的尺寸
character_width = 50
character_height = 50

# 创建角色的矩形
character_rect = pygame.Rect(0, 0, character_width, character_height)

# 设置角色的初始位置为屏幕中心
character_rect.center = (screen_width // 2, screen_height // 2)

# 游戏主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 渲染背景
    screen.fill((255, 255, 255))
    mouse_pos = pygame.mouse.get_pos()

    character_rect.center = mouse_pos

    # 渲染角色
    pygame.draw.rect(screen, (255, 0, 0), character_rect)

    # 更新屏幕显示
    pygame.display.flip()
    pygame.time.Clock().tick(60)

# 退出游戏
pygame.quit()
