import pygame
import sys
import random
from concurrent.futures import ThreadPoolExecutor
import time

# 初始化 Pygame
pygame.init()

# 设置窗口尺寸
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# 加载图像
image_path1 = "image1.png"
image1 = pygame.image.load(image_path1)

image_path2 = "image2.png"
image2 = pygame.image.load(image_path2)

# 获取图像的矩形对象
image_rect1 = image1.get_rect()
image_x1 = (screen_width - image_rect1.width) // 2
image_y1 = (screen_height - image_rect1.height) // 2

image_rect2 = image2.get_rect()
image_x2 = random.randint(0, screen_width - image_rect2.width)
image_y2 = random.randint(0, screen_height - image_rect2.height)
move_speed2 = 0.1

# 设置移动速度
move_speed1 = 5

# 创建线程池
executor = ThreadPoolExecutor(max_workers=2)

# 函数：第二张图片自由移动
def move_image2():
    global image_x2, image_y2
    while True:
        direction = random.choice(['up', 'down', 'left', 'right'])
        if direction == 'up':
            image_y2 -= move_speed2
        elif direction == 'down':
            image_y2 += move_speed2
        elif direction == 'left':
            image_x2 -= move_speed2
        elif direction == 'right':
            image_x2 += move_speed2

        # 判断图像是否走出界面
        if image_x2 < -image_rect2.width:
            image_x2 = screen_width
        elif image_x2 > screen_width:
            image_x2 = -image_rect2.width
        if image_y2 < -image_rect2.height:
            image_y2 = screen_height
        elif image_y2 > screen_height:
            image_y2 = -image_rect2.height

        time.sleep(0)  # 控制移动速率d

# 启动第二张图片自由移动的线程
executor.submit(move_image2)

# 游戏主循环
while True:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 检测键盘事件
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        image_y1 -= move_speed1
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        image_y1 += move_speed1
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        image_x1 -= move_speed1
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        image_x1 += move_speed1

    # 修正第一张图片的位置
    if image_x1 < -image_rect1.width:
        image_x1 = screen_width
    elif image_x1 > screen_width:
        image_x1 = -image_rect1.width
    if image_y1 < -image_rect1.height:
        image_y1 = screen_height
    elif image_y1 > screen_height:
        image_y1 = -image_rect1.height

    # 填充背景色
    screen.fill((255, 255, 255))

    # 在窗口上绘制第二张图像
    screen.blit(image2, (image_x2, image_y2))

    # 在窗口上绘制第一张图像
    screen.blit(image1, (image_x1, image_y1))

    # 更新屏幕显示
    pygame.display.flip()

    # 控制帧率为30帧
    pygame.time.Clock().tick(60)
