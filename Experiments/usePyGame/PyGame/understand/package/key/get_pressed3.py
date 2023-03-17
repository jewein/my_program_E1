import pygame
import sys

pygame.init()

window_width = 800
window_height = 600

white = (255, 255, 255)
black = (0, 0, 0)

window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("飞机游戏示例")

plane_x = window_width // 2
plane_y = window_height // 2
plane_speed = 5

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    # 控制飞机移动
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        plane_y -= plane_speed
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        plane_y += plane_speed
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        plane_x -= plane_speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        plane_x += plane_speed

    window.fill(white)
    pygame.draw.rect(window, black, (plane_x, plane_y, 50, 50))
    pygame.display.update()
    clock.tick(60)
