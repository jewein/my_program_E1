import pygame
from pygame.locals import *

pygame.init()

# 创建一个简单的Sprite类
class MySprite(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)

# 创建两个Sprite对象
sprite1 = MySprite('image1.png', 100, 100)
sprite2 = MySprite('image2.png', 200, 200)

# 检测两个精灵对象是否发生了碰撞
if pygame.sprite.collide_mask(sprite1, sprite2):
    print("发生碰撞！")
else:
    print("没有碰撞。")

pygame.quit()
