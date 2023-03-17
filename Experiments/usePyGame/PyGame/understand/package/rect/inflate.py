import pygame

pygame.init()

# 设置窗口尺寸
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Inflate() Example")

# 创建一个初始矩形
initial_rect = pygame.Rect(100, 100, 50, 50)

# 主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 在x和y方向上增大矩形的大小
    enlarged_rect = initial_rect.inflate(20, 30)

    # 填充背景颜色
    window.fill((255, 255, 255))

    # 绘制初始矩形（蓝色）
    pygame.draw.rect(window, (0, 0, 255), initial_rect)

    # 绘制调整后的矩形（红色）
    pygame.draw.rect(window, (255, 0, 0), enlarged_rect)

    pygame.display.flip()

pygame.quit()

