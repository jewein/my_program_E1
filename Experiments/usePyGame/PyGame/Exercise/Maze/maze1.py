import pygame
import random

# 初始化 Pygame
pygame.init()

# 定义窗口尺寸
WIDTH = 800
HEIGHT = 600

# 定义颜色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# 创建游戏窗口
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("迷宫游戏")

# 定义玩家类
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        # 处理玩家移动
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 3
        if keys[pygame.K_RIGHT]:
            self.rect.x += 3
        if keys[pygame.K_UP]:
            self.rect.y -= 3
        if keys[pygame.K_DOWN]:
            self.rect.y += 3

# 定义迷宫墙类
class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# 创建迷宫墙和玩家对象
walls = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

wall = Wall(300, 200, 200, 10)
walls.add(wall)
all_sprites.add(wall)

player = Player(50, 50)
all_sprites.add(player)

running = True

# 游戏主循环
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 更新玩家位置
    all_sprites.update()

    # 碰撞检测
    if pygame.sprite.spritecollide(player, walls, False):
        player.rect.x = 50
        player.rect.y = 50

    # 绘制游戏界面
    screen.fill(WHITE)
    all_sprites.draw(screen)
    pygame.display.flip()
    pygame.time.Clock().tick(60)

# 退出游戏
pygame.quit()
