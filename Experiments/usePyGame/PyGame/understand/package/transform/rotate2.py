import pygame
from pygame import image
from pygame import transform
from pygame.transform import rotate

# 初始化Pygame
pygame.init()

my_image = image.load('image.png')



rotated_image = transform.rotate(my_image, 45)
rotated_rect = rotated_image.get_rect()
print(rotated_rect)

pygame.quit()