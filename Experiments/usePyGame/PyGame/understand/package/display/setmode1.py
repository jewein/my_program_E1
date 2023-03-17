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

if __name__ == "__main__":
    pygame.init()

    window_width = 800
    window_height = 600

    screen = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("可移动的精灵图示例")

    all_sprites = pygame.sprite.Group()
    player = Player()
    all_sprites.add(player)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        all_sprites.update()

        screen.fill((255, 255, 255))
        all_sprites.draw(screen)

        pygame.display.flip()

    pygame.quit()
