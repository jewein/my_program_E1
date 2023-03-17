import pygame
import sys

# 初始化 Pygame
pygame.init()

# 设置窗口尺寸
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# 加载第一张图像
image_path = "image.png"
image = pygame.image.load(image_path)

# 获取第一张图像的矩形对象
image_rect = image.get_rect()
image_x = (screen_width - image_rect.width) // 2
image_y = (screen_height - image_rect.height) // 2
image_speed_x = 0
image_speed_y = 0

# 加载第二张图像
image2_path = "image2.png"
image2 = pygame.image.load(image2_path)

# 获取第二张图像的矩形对象
image2_rect = image2.get_rect()
image2_x = (screen_width - image2_rect.width) // 2
image2_y = (screen_height - image2_rect.height) // 2
image2_speed_x = 0
image2_speed_y = 0

# 设置移动速度
move_speed = 1
bounce_factor = 0.5

# 游戏主循环
while True:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # 获取鼠标点击位置
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # 判断鼠标点击位置是否在第一张图像上
            if image_rect.collidepoint(mouse_x, mouse_y):
                # 设置第一张图像位置为鼠标点击位置
                image_x = mouse_x - image_rect.width // 2
                image_y = mouse_y - image_rect.height // 2

    # 检测键盘事件
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        image_speed_y = -move_speed
    elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
        image_speed_y = move_speed
    else:
        image_speed_y = 0
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        image_speed_x = -move_speed
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        image_speed_x = move_speed
    else:
        image_speed_x = 0

    # 更新第一张图像的位置
    image_x += image_speed_x
    image_y += image_speed_y

    # 限制第一张图像的移动范围
    if image_x < -image_rect.width:
        image_x = screen_width
    elif image_x > screen_width:
        image_x = -image_rect.width
    if image_y < -image_rect.height:
        image_y = screen_height
    elif image_y > screen_height:
        image_y = -image_rect.height

    # 计算第一张图像与第二张图像之间的碰撞情况
    if image_rect.colliderect(image2_rect):
        # 碰撞发生时，计算推动方向和速度
        dx = image2_rect.centerx - image_rect.centerx
        dy = image2_rect.centery - image_rect.centery
        if abs(dx) > abs(dy):
            if dx > 0:
                image_speed_x -= move_speed * bounce_factor
                image2_speed_x += move_speed * bounce_factor
            else:
                image_speed_x += move_speed * bounce_factor
                image2_speed_x -= move_speed * bounce_factor
        else:
            if dy > 0:
                image_speed_y -= move_speed * bounce_factor
                image2_speed_y += move_speed * bounce_factor
            else:
                image_speed_y += move_speed * bounce_factor
                image2_speed_y -= move_speed * bounce_factor

    # 更新第二张图像的位置
    image2_x += image2_speed_x
    image2_y += image2_speed_y

    # 限制第二张图像的移动范围
    if image2_x < -image2_rect.width:
        image2_x = screen_width
    elif image2_x > screen_width:
        image2_x = -image2_rect.width
    if image2_y < -image2_rect.height:
        image2_y = screen_height
    elif image2_y > screen_height:
        image2_y = -image2_rect.height

    # 填充背景色
    screen.fill((255, 255, 255))

    # 在窗口上绘制第二张图像
    screen.blit(image2, (image2_x, image2_y))

    # 在窗口上绘制第一张图像
    screen.blit(image, (image_x, image_y))

    # 更新屏幕显示
    pygame.display.flip()
