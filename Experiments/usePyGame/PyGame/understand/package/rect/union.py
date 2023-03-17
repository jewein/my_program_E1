import pygame

# 初始化pygame
pygame.init()

window = pygame.display.set_mode((800, 600))
# 创建两个矩形
# 创建两个矩形
rect1 = pygame.Rect(100, 100, 200, 100)
rect2 = pygame.Rect(150, 150, 100, 150)
# 创建两个矩形
rect3 = pygame.Rect(100, 100, 200, 100)
rect4 = pygame.Rect(150, 150, 100, 150)

# 使用union()方法获取合并后的矩形
merged_rect = rect3.union(rect4)

# 输出结果
print("Rect1:", rect1)
print("Rect2:", rect2)
print("Merged Rect:", merged_rect)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 填充背景颜色
    window.fill((255, 255, 255))
    pygame.draw.rect(window, (0, 0, 255), rect1)
    pygame.draw.rect(window, (255, 0, 0), rect2)
    pygame.draw.rect(window, (0, 255, 0), merged_rect)
    pygame.display.flip()
    pygame.time.Clock().tick(60)




# 结束pygame
pygame.quit()
