import pygame

# 初始化Pygame
pygame.init()

# 创建屏幕窗口
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("绘制直线示例")

# 设置直线的起始点和终点坐标
start_pos = (100, 100)
end_pos = (400, 300)

# 设置直线的颜色（红色）
line_color = (255, 0, 0)

# 游戏主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 在屏幕上绘制直线
    pygame.draw.line(screen, line_color, start_pos, end_pos, 3)


    # 刷新屏幕显示
    pygame.display.flip()
    pygame.time.Clock().tick(60)

# 退出Pygame
pygame.quit()
