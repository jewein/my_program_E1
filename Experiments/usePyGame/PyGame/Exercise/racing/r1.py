import pygame
import random

# 初始化 Pygame
pygame.init()

# 设置窗口尺寸
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("赛车模拟器")

# 加载赛车图像
car_image = pygame.image.load("car.png")
car_width = 50
car_height = 100

# 设置赛车的初始位置
car_x = screen_width // 2 - car_width // 2
car_y = screen_height - car_height - 20
car_speed = 5

# 设置障碍物的初始位置和速度
obstacle_width = 100
obstacle_height = 100
obstacle_x = random.randint(0, screen_width - obstacle_width)
obstacle_y = -obstacle_height
obstacle_speed = 5

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        car_x -= car_speed
    if keys[pygame.K_RIGHT]:
        car_x += car_speed

    # 移动赛车
    if car_x < 0:
        car_x = 0
    elif car_x > screen_width - car_width:
        car_x = screen_width - car_width

    # 移动障碍物
    obstacle_y += obstacle_speed

    # 检测碰撞
    if car_y < obstacle_y + obstacle_height and car_y + car_height > obstacle_y:
        if car_x < obstacle_x + obstacle_width and car_x + car_width > obstacle_x:
            print("碰撞！游戏结束！")
            running = False

    # 绘制背景和赛车
    screen.fill((255, 255, 255))
    screen.blit(car_image, (car_x, car_y))

    # 绘制障碍物
    pygame.draw.rect(screen, (255, 0, 0), (obstacle_x, obstacle_y, obstacle_width, obstacle_height))

    pygame.display.flip()
    clock.tick(60)

# 退出游戏
pygame.quit()
