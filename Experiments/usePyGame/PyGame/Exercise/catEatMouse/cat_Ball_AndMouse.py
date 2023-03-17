import pygame
import sys
import random

# 初始化 Pygame
pygame.init()

# 设置窗口尺寸
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# 加载第一张图像
image_path = "image.png"
image = pygame.image.load(image_path)
image_rect = image.get_rect()

# 加载第二张图像
image2_path = "image2.png"
image2 = pygame.image.load(image2_path)
image2_rect = image2.get_rect()

# 初始化图像位置和速度
image_x = random.randint(0, screen_width - image_rect.width)
image_y = random.randint(0, screen_height - image_rect.height)
image_speed_x = random.choice([-1, 1])
image_speed_y = random.choice([-1, 1])

image2_x = random.randint(0, screen_width - image2_rect.width)
image2_y = random.randint(0, screen_height - image2_rect.height)
image2_speed_x = random.choice([-1, 1])
image2_speed_y = random.choice([-1, 1])

# 设置移动速度
move_speed = 1

# 游戏主循环
while True:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 移动第一张图像
    image_x += image_speed_x * move_speed
    image_y += image_speed_y * move_speed

    # 检测第一张图像是否与边界发生碰撞，如果是则反弹
    if image_x <= 0 or image_x >= screen_width - image_rect.width:
        image_speed_x *= -1
    if image_y <= 0 or image_y >= screen_height - image_rect.height:
        image_speed_y *= -1

    # 移动第二张图像
    image2_x += image2_speed_x * move_speed
    image2_y += image2_speed_y * move_speed

    # 检测第二张图像是否与边界发生碰撞，如果是则反弹
    if image2_x <= 0 or image2_x >= screen_width - image2_rect.width:
        image2_speed_x *= -1
    if image2_y <= 0 or image2_y >= screen_height - image2_rect.height:
        image2_speed_y *= -1

    # 检测第一张图像是否与第二张图像发生碰撞
    if image_rect.colliderect(image2_rect):
        # 计算第一张图像和第二张图像的重叠区域
        intersection = image_rect.clip(image2_rect)
        # 判断第一张图像是从上方碰撞还是从下方碰撞
        if intersection.height >= intersection.width:
            image_speed_y *= -1
        # 判断第一张图像是从左侧碰撞还是从右侧碰撞
        if intersection.width >= intersection.height:
            image_speed_x *= -1

    # 填充背景色
    screen.fill((255, 255, 255))

    # 在窗口上绘制第一张图像
    screen.blit(image, (image_x, image_y))

    # 在窗口上绘制第二张图像
    screen.blit(image2, (image2_x, image2_y))

    # 更新屏幕显示
    pygame.display.flip()
