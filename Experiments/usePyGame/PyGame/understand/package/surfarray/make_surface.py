import pygame
import numpy as np

# 初始化Pygame
pygame.init()

# 窗口尺寸
WIDTH, HEIGHT = 400, 200

# 创建窗口
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Color Gradient Rectangle")

def create_gradient_rect(width, height):
    # 创建一个渐变矩形的颜色数据，这里使用NumPy来生成一个二维数组
    gradient = np.zeros((height, width, 3), dtype=np.uint8)

    # 在这个例子中，我们将颜色从红色渐变到蓝色
    for y in range(height):
        r = int(255 * (y / height))    # 红色通道渐变
        b = int(255 * ((height - y) / height))   # 蓝色通道渐变
        for x in range(width):
            gradient[y, x] = (r, b,0)

    return gradient

# 创建渐变矩形的颜色数据
gradient_rect = create_gradient_rect(WIDTH, HEIGHT)

# 将颜色数据转换为Surface对象
gradient_surface = pygame.surfarray.make_surface(gradient_rect)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 在窗口上绘制渐变矩形
    screen.blit(gradient_surface, (0, 0))
    pygame.display.flip()
    pygame.time.wait(100)

# 退出Pygame
pygame.quit()
