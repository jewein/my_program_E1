import pygame
import sys
import math
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800, 600))

# 加载图片
image = pygame.image.load("image.png")
# 获取图片的矩形
image_rect = image.get_rect()
# 设置图片的初始位置为屏幕中心
image_rect.center = screen.get_rect().center

angle = 0  # 初始旋转角度

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))

    # 计算旋转后的图片
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_rect = rotated_image.get_rect(center=image_rect.center)

    # 计算高度方向的正弦变化
    height_factor = abs(math.sin(math.radians(angle)))

    # 根据高度方向的变化调整图片的高度
    scaled_height = int(image_rect.height * height_factor)
    scaled_image = pygame.transform.scale(rotated_image, (rotated_rect.width, scaled_height))
    scaled_rect = scaled_image.get_rect(center=rotated_rect.center)

    # 绘制调整后的图片
    screen.blit(scaled_image, scaled_rect)

    pygame.display.flip()
    angle += 1  # 每帧增加1度的旋转角度
    pygame.time.Clock().tick(30)
