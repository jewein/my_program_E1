import math

import pygame
import sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((400, 300), pygame.RESIZABLE|pygame.SCALED)

image = pygame.image.load("image2.png")
image_rect = image.get_rect()
image_width, image_height = image_rect.size

angle = 0  # 初始旋转角度
scaling_factor = 0.5  # 缩放因子，用于调整图片高度

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))  # 清空屏幕

    # 将图片居中显示
    image_rect.center = (screen.get_width() // 2, screen.get_height() // 2)

    # 根据旋转角度调整缩放因子和高度

    scaling_factor = math.sin(math.radians(angle))

    if scaling_factor < 0:
        scaling_factor = -scaling_factor
        scaled_height = int(image_height * scaling_factor)
        scaled_image = pygame.transform.scale(image, (image_width, scaled_height))
        flipped_image = pygame.transform.flip(scaled_image, False, True)
    else:
        scaled_height = int(image_height * scaling_factor)
        scaled_image = pygame.transform.scale(image, (image_width, scaled_height))
        flipped_image = scaled_image

    # 根据旋转角度调整图片的翻转状态


    cx = screen.get_width() // 2-image_width//2
    cy = screen.get_height() // 2-scaled_height//2

    # 将旋转后的图像绘制在屏幕中心，图片中心和screen中心重合
    screen.blit(flipped_image, (cx,cy)   , (0, 0, image_width, scaled_height))



    # screen.blit(flipped_image, image_rect.center, (0, 0, image_width, scaled_height))
    # screen.blit(flipped_image, image_rect.topleft, (0, 0, image_width, scaled_height))

    pygame.display.flip()

    angle += 1  # 每次增加旋转角度
    if angle >= 360:
        angle = 0

    pygame.time.Clock().tick(120)