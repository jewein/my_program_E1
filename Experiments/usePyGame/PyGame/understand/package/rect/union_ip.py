import pygame

# 初始化pygame
pygame.init()

# 创建两个矩形
rect1 = pygame.Rect(100, 100, 200, 100)
rect2 = pygame.Rect(150, 150, 100, 150)
# 创建两个矩形
rect3 = pygame.Rect(100, 100, 200, 100)
rect4 = pygame.Rect(150, 150, 100, 150)

# 输出两个矩形的信息
print("rect1:", rect1)  # 输出 rect1: <rect(100, 100, 200, 100)>
print("rect2:", rect2)  # 输出 rect2: <rect(150, 150, 100, 150)>

window=pygame.display.set_mode((800,600))
pygame.display.set_caption("union_ip() Example")

# 使用union_ip()方法将rect1扩展以包含rect2的合并区域
rect3.union_ip(rect4)

# 输出扩展后的rect1信息
print("扩展后的rect1:", rect3)  # 输出 扩展后的rect1: <rect(100, 100, 200, 200)>


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 填充背景颜色
    window.fill((255, 255, 255))
    pygame.draw.rect(window, (0, 0, 255), rect1)
    pygame.draw.rect(window, (255, 0, 0), rect2)
    pygame.draw.rect(window, (0, 255, 0), rect3)
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()


# 使用union_ip()方法将rect1扩展以包含rect2的合并区域
rect1.union_ip(rect2)

# 输出扩展后的rect1信息
print("扩展后的rect1:", rect1)  # 输出 扩展后的rect1: <rect(100, 100, 200, 200)>


