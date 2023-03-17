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

    # 计算旋转角度，根据时间的正弦变化
    angle = math.sin(pygame.time.get_ticks() * 0.001) * 90  # 90度是一个周期，可以根据需要调整

    # 计算旋转后的图片
    rotated_image = pygame.transform.rotozoom(image, angle, 1)
    rotated_rect = rotated_image.get_rect(center=image_rect.center)

    # 绘制旋转后的图片
    screen.blit(rotated_image, rotated_rect)

    pygame.display.flip()
