import pygame
import sys
import random
import threading
import time

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

# 第2张图片
image2_path = "image2.png"
image2 = pygame.image.load(image2_path)
image2_rect = image2.get_rect()
image2_x = random.randint(0, screen_width - image2_rect.width)
image2_y = random.randint(0, screen_height - image2_rect.height)

# 设置移动速度
move_speed = 1

# 线程池
thread_pool = []

# 线程控制标志
running = True

# 定义第2张图片移动线程
def move_image2():
    global image2_x, image2_y, running

    while running:
        # 随机移动方向
        direction = random.choice(['up', 'down', 'left', 'right'])

        if direction == 'up':
            image2_y -= move_speed
        elif direction == 'down':
            image2_y += move_speed
        elif direction == 'left':
            image2_x -= move_speed
        elif direction == 'right':
            image2_x += move_speed

        # 判断图像是否走出界面
        if image2_x < -image2_rect.width:
            image2_x = screen_width
        elif image2_x > screen_width:
            image2_x = -image2_rect.width
        if image2_y < -image2_rect.height:
            image2_y = screen_height
        elif image2_y > screen_height:
            image2_y = -image2_rect.height

        # 控制移动帧率为30帧
        time.sleep(1 / 30)

# 创建第2张图片移动线程并添加到线程池
image2_thread = threading.Thread(target=move_image2)
thread_pool.append(image2_thread)

# 启动线程池中的线程
for thread in thread_pool:
    thread.start()

# 游戏主循环
while True:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # 结束线程池中的线程
            running = False
            for thread in thread_pool:
                thread.join()
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

    # 判断图像是否走出界面
    if image_x < -image_rect.width:
        image_x = screen_width
    elif image_x > screen_width:
        image_x = -image_rect.width
    if image_y < -image_rect.height:
        image_y = screen_height
    elif image_y > screen_height:
        image_y = -image_rect.height

    # 填充背景色
    screen.fill((255, 255, 255))

    # 在窗口上绘制第2张图片
    screen.blit(image2, (image2_x, image2_y))

    # 在窗口上绘制第1张图片
    screen.blit(image, (image_x, image_y))

    # 更新屏幕显示
    pygame.display.flip()
