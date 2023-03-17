import pygame

# 初始化Pygame
pygame.init()

# 设置窗口大小
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Filled Polygon")

# 定义多边形的顶点坐标
pointlist = [(100, 100), (200, 50), (300, 150), (250, 300), (150, 300)]

# 设置填充颜色
fill_color = (255, 0, 0)  # 红色

# 游戏主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 填充背景色
    screen.fill((255, 255, 255))  # 白色

    # 绘制填充多边形
    pygame.draw.polygon(screen, fill_color, pointlist,width=1)

    # 刷新显示
    pygame.display.flip()
    pygame.time.Clock().tick(60)

# 退出Pygame
pygame.quit()


