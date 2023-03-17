import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
red_color = pygame.Color('red')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 在屏幕上绘制一个红色矩形
    pygame.draw.rect(screen, red_color, (100, 100, 200, 150))

    pygame.display.flip()

pygame.quit()
