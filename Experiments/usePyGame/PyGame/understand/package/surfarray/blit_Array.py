import pygame
import numpy as np

# 初始化Pygame
pygame.init()

# 设置屏幕尺寸和颜色
screen_width, screen_height = 400, 300
background_color = (255, 255, 255)

# 创建窗口和Surface对象
screen = pygame.display.set_mode((screen_width, screen_height))
surface = pygame.Surface((screen_width, screen_height))

# 填充Surface对象的像素数组
pixels_array = np.zeros((screen_height, screen_width, 3), dtype=np.uint8)
pixels_array[:, :screen_width // 2] = [255, 0, 0]  # 左侧区域设置为红色
pixels_array[:, screen_width // 2:] = [0, 0, 255]  # 右侧区域设置为蓝色

# 将数组数据绘制到Surface上
pygame.surfarray.blit_array(surface, pixels_array)

# 主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 填充屏幕并绘制Surface
    screen.fill(background_color)
    screen.blit(surface, (0, 0))

    # 刷新屏幕显示
    pygame.display.flip()

# 退出Pygame
pygame.quit()
