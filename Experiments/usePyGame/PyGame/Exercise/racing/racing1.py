import pygame
import sys

# 初始化 Pygame
pygame.init()

# 设置窗口尺寸
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("赛车模拟器")

# 加载赛车图像
car_image = pygame.image.load("car.png")
car_rect = car_image.get_rect()
car_rect.centerx = screen_width // 2
car_rect.bottom = screen_height - 10

# 设置赛车移动速度
car_speed = 5

# 游戏循环
while True:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 检测按键
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        car_rect.x -= car_speed
    if keys[pygame.K_RIGHT]:
        car_rect.x += car_speed
    if keys[pygame.K_UP]:
        car_rect.y -= car_speed
    if keys[pygame.K_DOWN]:
        car_rect.y += car_speed

    # 绘制背景和赛车
    screen.fill((255, 255, 255))  # 清空屏幕
    screen.blit(car_image, car_rect)  # 绘制赛车

    # 更新屏幕
    pygame.display.flip()
    pygame.time.Clock().tick(60)


pygame.quit()
