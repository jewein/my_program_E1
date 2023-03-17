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

    # 计算缩放比例和旋转角度
    scale = abs(math.sin(math.radians(angle)))  # 正弦变化作为缩放比例
    scaled_width = int(image_rect.width * scale)
    scaled_height = int(image_rect.height * scale)
    scaled_image = pygame.transform.scale(image, (scaled_width, scaled_height))

    rotated_image = pygame.transform.rotate(scaled_image, angle)
    rotated_rect = rotated_image.get_rect(center=image_rect.center)

    # 绘制旋转后的图片
    screen.blit(rotated_image, rotated_rect)

    pygame.display.flip()
    angle += 2  # 每帧增加2度的旋转角度，可以根据需要调整旋转速度
    pygame.time.Clock().tick(30)