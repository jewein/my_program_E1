import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
# 创建一个简单的Sprite类
class MySprite(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = 2  # 精灵的移动速度

# 创建玩家精灵
player_sprite = MySprite('image1.png', 100, 100)

# 创建障碍物精灵
obstacle_sprite = MySprite('image2.png', 200, 200)

# 创建一个精灵组
all_sprites = pygame.sprite.Group(player_sprite, obstacle_sprite)

# 主循环
running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # 获取键盘输入，使玩家精灵可以移动
    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        player_sprite.rect.x -= player_sprite.speed
    if keys[K_RIGHT]:
        player_sprite.rect.x += player_sprite.speed
    if keys[K_UP]:
        player_sprite.rect.y -= player_sprite.speed
    if keys[K_DOWN]:
        player_sprite.rect.y += player_sprite.speed

    # 检测玩家精灵与障碍物精灵是否发生了碰撞
    if pygame.sprite.collide_mask(player_sprite, obstacle_sprite):
        # 计算碰撞后的相对位置
        dx = player_sprite.rect.centerx - obstacle_sprite.rect.centerx
        dy = player_sprite.rect.centery - obstacle_sprite.rect.centery

        # 根据相对位置改变精灵的运动方向，使其弹开
        if dx > 0:
            player_sprite.rect.x += player_sprite.speed
        elif dx < 0:
            player_sprite.rect.x -= player_sprite.speed

        if dy > 0:
            player_sprite.rect.y += player_sprite.speed
        elif dy < 0:
            player_sprite.rect.y -= player_sprite.speed

    # 更新屏幕
    screen.fill((255, 255, 255))
    all_sprites.draw(screen)
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
