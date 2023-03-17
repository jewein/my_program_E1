import pygame
from pygame.locals import *

pygame.init()

# 屏幕尺寸和背景颜色
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BACKGROUND_COLOR = (255, 255, 255)

# 玩家角色尺寸和移动速度
PLAYER_WIDTH, PLAYER_HEIGHT = 50, 50
PLAYER_SPEED = 5

# 加载玩家图像并创建掩码
player_image = pygame.image.load('player.png')
player_mask = pygame.mask.from_surface(player_image)

# 玩家初始位置
player_x, player_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2

# 创建窗口
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),pygame.RESIZABLE)
pygame.display.set_caption('碰撞检测示例')

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # 获取按键状态
    keys = pygame.key.get_pressed()

    # 移动玩家角色
    if keys[K_LEFT]:
        player_x -= PLAYER_SPEED
    if keys[K_RIGHT]:
        player_x += PLAYER_SPEED
    if keys[K_UP]:
        player_y -= PLAYER_SPEED
    if keys[K_DOWN]:
        player_y += PLAYER_SPEED

    # 碰撞检测
    # 假设有一个墙壁的掩码 wall_mask
    # 假设墙壁的位置为 (wall_x, wall_y)
    wall_x, wall_y = 300, 200
    wall_mask = pygame.mask.from_surface(pygame.Surface((100, 100)))  # 假设墙壁是一个100x100的矩形

    # 计算玩家相对于墙壁的偏移量
    offset = (wall_x - player_x, wall_y - player_y)

    # 检测玩家与墙壁是否碰撞
    if player_mask.overlap(wall_mask, offset):
        print("玩家与墙壁发生碰撞！")

    # 绘制场景
    screen.fill(BACKGROUND_COLOR)
    screen.blit(player_image, (player_x, player_y))
    pygame.draw.rect(screen, (0, 0, 0), (wall_x, wall_y, 100, 100))  # 绘制墙壁，这里简化为一个矩形

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
