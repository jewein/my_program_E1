import pygame
import random

# 初始化Pygame
pygame.init()

# 设置游戏窗口的尺寸
WIDTH = 800
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("城市交通模拟")

# 定义颜色
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# 定义车辆类
class Car(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

        self.rect.x = random.randrange(WIDTH)
        self.rect.y = random.randrange(HEIGHT)

        self.speed = random.randrange(1, 4)

    def update(self):
        self.rect.x += self.speed
        if self.rect.right > WIDTH:
            self.rect.x = -self.rect.width

# 创建车辆精灵组
car_sprites = pygame.sprite.Group()

# 创建车辆对象
for _ in range(10):
    car = Car(RED, 50, 30)
    car_sprites.add(car)

# 游戏主循环
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 更新车辆位置
    car_sprites.update()

    # 绘制背景
    window.fill(BLACK)

    # 绘制车辆
    car_sprites.draw(window)

    # 刷新屏幕
    pygame.display.flip()

    # 控制帧率
    clock.tick(60)

# 退出游戏
pygame.quit()
