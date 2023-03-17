import pygame

# 初始化pygame
pygame.init()

# 创建一个矩形对象，传入左上角坐标(x, y)，宽度为-100，高度为-50
# 注意：这里意图创建一个左上角在(100, 200)，宽度为100，高度为50的矩形
rect = pygame.Rect(100, 200, -100, -50)

# 打印原始矩形的属性
print("原始矩形：")
print("左上角坐标：", rect.topleft)
print("宽度：", rect.width)
print("高度：", rect.height)

# 使用normalize()方法转换矩形
rect.normalize()

# 打印转换后的矩形属性
print("\n转换后的矩形：")
print("左上角坐标：", rect.topleft)
print("宽度：", rect.width)
print("高度：", rect.height)

window = pygame.display.set_mode((400, 300))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 填充背景颜色
    window.fill((255, 255, 255))

    # 绘制初始矩形（蓝色）
    pygame.draw.rect(window, (0, 0, 255), rect)

    # 绘制调整后的矩形（红色）
    pygame.draw.rect(window, (255, 0, 0), rect.normalize())

    pygame.display.flip()

    pygame.time.Clock().tick(60)

pygame.quit()


