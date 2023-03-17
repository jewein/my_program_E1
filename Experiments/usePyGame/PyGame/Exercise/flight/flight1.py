import pygame
import sys

# 初始化 Pygame
pygame.init()

# 设置窗口大小和标题
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Flight Simulator")

# 加载飞机图像
airplane_image = pygame.image.load("airplane.png")

# 获取飞机图像的矩形
airplane_rect = airplane_image.get_rect()
airplane_rect.center = (window_width // 2, window_height // 2)

# 设置飞机的速度
airplane_speed = 5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 获取键盘输入
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        airplane_rect.y -= airplane_speed
    if keys[pygame.K_DOWN]:
        airplane_rect.y += airplane_speed
    if keys[pygame.K_LEFT]:
        airplane_rect.x -= airplane_speed
    if keys[pygame.K_RIGHT]:
        airplane_rect.x += airplane_speed

    # 绘制背景
    window.fill((255, 255, 255))

    # 绘制飞机
    window.blit(airplane_image, airplane_rect)

    # 更新屏幕
    pygame.display.flip()
    pygame.time.Clock().tick(60)


pygame.quit()
