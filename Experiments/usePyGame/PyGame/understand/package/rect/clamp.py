import pygame

pygame.init()

# 定义屏幕大小和颜色
screen_width, screen_height = 800, 600
background_color = (255, 255, 255)

# 创建屏幕对象
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Clamp Example")

# 创建一个矩形
rect_width, rect_height = 100, 80
rect = pygame.Rect(200, 200, rect_width, rect_height)
rect_color = (0, 0, 255)

# 创建一个点
point_radius = 5
point_color = (255, 0, 0)
point_x, point_y = 400, 300

# 自定义clamp函数，确保点的位置在矩形内部
def clamp(value, min_value, max_value):
    return max(min(value, max_value), min_value)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 通过键盘控制点的位置
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        point_x -= 5
    if keys[pygame.K_RIGHT]:
        point_x += 5
    if keys[pygame.K_UP]:
        point_y -= 5
    if keys[pygame.K_DOWN]:
        point_y += 5

    # 使用clamp函数限制点的位置在矩形内部
    point_x = clamp(point_x, rect.left, rect.right - point_radius)
    point_y = clamp(point_y, rect.top, rect.bottom - point_radius)

    # 绘制屏幕
    screen.fill(background_color)
    pygame.draw.rect(screen, rect_color, rect)
    pygame.draw.circle(screen, point_color, (point_x, point_y), point_radius)
    pygame.display.flip()
    pygame.time.Clock().tick(30)



pygame.quit()
