import pygame
import sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((400, 300))

image = pygame.image.load("image.png")
image_width, image_height = image.get_rect().size
scaled_image = pygame.transform.scale(image, (image_width // 2, image_height // 2))

angle = 0  # 初始旋转角度
scale_factor = 1  # 初始缩放因子
direction = 1  # 缩放方向：1表示放大，-1表示缩小

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))  # 清空屏幕

    rotated_image = pygame.transform.scale(scaled_image, (image_width // 2, int(image_height * scale_factor)))
    rotated_rect = rotated_image.get_rect()
    rotated_rect.center = (screen.get_width() // 2, screen.get_height() // 2)

    pygame.draw.rect(screen, (0, 0, 0), rotated_rect, 1)  # 绘制矩形框，可选

    # 将旋转后的图像绘制在屏幕上
    screen.blit(rotated_image, rotated_rect.topleft)

    pygame.display.flip()

    angle += 1  # 每次增加旋转角度
    if angle >= 360:
        angle = 0

    if 90 <= angle < 180 or 270 <= angle < 360:
        direction = -1  # 翻转方向为缩小
    else:
        direction = 1  # 翻转方向为放大

    scale_factor += 0.01 * direction  # 每次调整缩放因子
    if scale_factor <= 0:
        scale_factor = 0  # 缩放因子最小为0

    # 获取旋转后的图像
    rotated_image = pygame.transform.scale(scaled_image, (image_width // 2, int(image_height * scale_factor)))

    pygame.time.Clock().tick(30)
