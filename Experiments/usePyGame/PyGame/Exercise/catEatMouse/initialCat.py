import pygame
import sys

# 初始化 Pygame
pygame.init()

# 设置窗口尺寸
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# 加载图像
image_path = "image.png"
image = pygame.image.load(image_path)

# 获取图像的矩形对象
image_rect = image.get_rect()
image_x = (screen_width - image_rect.width) // 2
image_y = (screen_height - image_rect.height) // 2

# 设置移动速度
move_speed = 1

# 游戏主循环
while True:
    # 清除事件队列
    # pygame.event.clear()
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # 1代表鼠标左键点击
            # 获取鼠标点击位置
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # 设置图像位置为鼠标点击位置
            image_x = mouse_x - image_rect.width // 2
            image_y = mouse_y - image_rect.height // 2

    # 检测键盘事件
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        image_y -= move_speed
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        image_y += move_speed
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        image_x -= move_speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        image_x += move_speed


    # 检测键盘事件
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] or keys[pygame.K_w] or keys[ord('w')]:
        image_y -= move_speed
    if keys[pygame.K_DOWN] or keys[pygame.K_s] or keys[ord('s')]:
        image_y += move_speed
    if keys[pygame.K_LEFT] or keys[pygame.K_a] or keys[ord('a')]:
        image_x -= move_speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d] or keys[ord('d')]:
        image_x += move_speed
    # 修复按下其他按键导致卡顿的问题
    # pygame.event.clear(pygame.KEYUP)


    # 判断图像是否走出界面
    if image_x < -image_rect.width:
        image_x = screen_width
    elif image_x > screen_width:
        image_x = -image_rect.width
    if image_y < -image_rect.height:
        image_y = screen_height
    elif image_y > screen_height:
        image_y = -image_rect.height

    # 刷新事件队列，以确保鼠标和键盘事件能够继续正常处理
    pygame.event.get()
    # 填充背景色
    screen.fill((255, 255, 255))

    # 在窗口上绘制图像
    screen.blit(image, (image_x, image_y))

    # 更新屏幕显示
    pygame.display.flip()


