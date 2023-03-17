import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))  # 用红色填充精灵图以示区别
        self.rect = self.image.get_rect()
        self.rect.center = (window_width // 2, window_height // 2)
        self.speed = 5

    def update(self):
        # 处理玩家输入，移动精灵图
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        # 确保精灵图不会移出窗口边界
        self.rect.x = max(0, min(self.rect.x, window_width - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, window_height - self.rect.height))

class MyGame:
    def __init__(self, window_width, window_height):
        # 初始化Pygame
        pygame.init()

        # 窗口大小
        self.window_width = window_width
        self.window_height = window_height

        # 创建游戏窗口
        self.screen = pygame.display.set_mode((self.window_width, self.window_height))

        # 设置窗口标题
        pygame.display.set_caption("我的游戏窗口")

        # 创建精灵组
        self.all_sprites = pygame.sprite.Group()
        self.player = Player()
        self.all_sprites.add(self.player)

    def run(self):
        # 游戏主循环
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.all_sprites.update()

            self.screen.fill((255, 255, 255))
            self.all_sprites.draw(self.screen)

            pygame.display.flip()

        pygame.quit()


if __name__ == "__main__":
    window_width = 800
    window_height = 600

    game = MyGame(window_width, window_height)
    game.run()

