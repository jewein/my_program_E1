import pygame
from pygame import image, transform

angle=1
a=angle
# 初始化Pygame
pygame.init()

# 创建窗口
window = pygame.display.set_mode((800, 600))

# 加载图像
my_image = image.load('image.png')

rotated_image = transform.rotate(my_image, a)


# 旋转图像

# 游戏循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    a+=angle
    rotated_image = transform.rotate(my_image, a)

    image_width = rotated_image.get_width()
    image_height = rotated_image.get_height()
    # 计算图像左上角相对于目标点的偏移量
    target_x=400
    target_y=300
    offset_x = target_x - image_width // 2
    offset_y = target_y - image_height // 2
    # 显示旋转后的图像
    window.fill((255, 255, 255))
    window.blit(rotated_image, (offset_x, offset_y))
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()




