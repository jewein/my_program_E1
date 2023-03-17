import pygame
from pygame.sprite import Sprite, Group

# 初始化 Pygame
pygame.init()

# 定义屏幕大小和背景颜色
screen_width, screen_height = 800, 600
bg_color = (255, 255, 255)

# 创建游戏窗口
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sprite Example")

# 定义精灵类
class Box(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100

    def update(self):
        self.rect.x += 1

# 创建精灵对象
box = Box()

# 创建精灵组
all_sprites = Group()
all_sprites.add(box)

# 游戏主循环
running = True
clock = pygame.time.Clock()

while running:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 更新精灵状态
    all_sprites.update()

    # 绘制背景
    screen.fill(bg_color)

    # 绘制精灵
    all_sprites.draw(screen)

    # 刷新屏幕
    pygame.display.flip()

    # 控制帧率
    clock.tick(60)

# 退出游戏
pygame.quit()

