import pygame
pygame.init()

# 设置窗口
win_width, win_height = 400, 300
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("计时器")

# 定义颜色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
elapsed_time = 0
# 创建字体对象
font = pygame.font.Font(None, 50)

# 计时器变量
start_time = 0
running = 0
stop=0
# 游戏主循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # 开始/停止计时器
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                running = (running+1) % 3
                if running:
                    start_time = pygame.time.get_ticks()

    # 计算经过的时间
    if running==1:
        elapsed_time = (pygame.time.get_ticks() - start_time)  # 毫秒转秒
    elif running==2:
        pass
    else:
        elapsed_time = 0

    # 绘制背景和计时器文本
    win.fill(BLACK)
    timer_text = font.render(f"Time: {elapsed_time} millseconds", True, WHITE)
    win.blit(timer_text, (50, 50))
    pygame.display.update()
