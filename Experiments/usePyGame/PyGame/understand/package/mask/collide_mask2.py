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
        player_sprite.rect.x -= 2
    if keys[K_RIGHT]:
        player_sprite.rect.x += 2
    if keys[K_UP]:
        player_sprite.rect.y -= 2
    if keys[K_DOWN]:
        player_sprite.rect.y += 2

    # 检测玩家精灵与障碍物精灵是否发生了碰撞
    if pygame.sprite.collide_mask(player_sprite, obstacle_sprite):
        # 如果碰撞发生，将玩家精灵移回上一步的位置
        player_sprite.rect.x -= 2
        player_sprite.rect.y -= 2

    # 更新屏幕
    screen.fill((255, 255, 255))
    all_sprites.draw(screen)
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
