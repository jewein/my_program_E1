import pygame
import random

# 初始化 Pygame
pygame.init()

# 设置游戏窗口尺寸
WIDTH = 800
HEIGHT = 600
win = pygame.display.set_mode((WIDTH, HEIGHT),pygame.RESIZABLE)
pygame.display.set_caption("迷宫游戏")

# 定义颜色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# 定义迷宫尺寸和格子大小
MAZE_SIZE = 20
CELL_SIZE = WIDTH // MAZE_SIZE

# 创建迷宫二维数组
maze = [[0] * MAZE_SIZE for _ in range(MAZE_SIZE)]

# 定义玩家初始位置
player_x = 0
player_y = 0

# 定义迷宫出口位置
exit_x = MAZE_SIZE - 1
exit_y = MAZE_SIZE - 1

# 定义四个方向的移动偏移量
directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

# 生成迷宫函数
def generate_maze(x, y):
    maze[y][x] = 1
    random.shuffle(directions)
    for dx, dy in directions:
        nx, ny = x + dx * 2, y + dy * 2
        if 0 <= nx < MAZE_SIZE and 0 <= ny < MAZE_SIZE and maze[ny][nx] == 0:
            maze[y + dy][x + dx] = 1
            generate_maze(nx, ny)

# 生成迷宫
generate_maze(0, 0)

# 游戏循环标志
running = True

# 游戏主循环
while running:
    # 处理退出事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 处理键盘输入
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_y > 0 and maze[player_y - 1][player_x] == 1:
        player_y -= 1
    if keys[pygame.K_DOWN] and player_y < MAZE_SIZE - 1 and maze[player_y + 1][player_x] == 1:
        player_y += 1
    if keys[pygame.K_LEFT] and player_x > 0 and maze[player_y][player_x - 1] == 1:
        player_x -= 1
    if keys[pygame.K_RIGHT] and player_x < MAZE_SIZE - 1 and maze[player_y][player_x + 1] == 1:
        player_x += 1

    # 清空窗口
    win.fill(BLACK)

    # 绘制迷宫
    for y in range(MAZE_SIZE):
        for x in range(MAZE_SIZE):
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            if x == exit_x and y == exit_y:
                pygame.draw.rect(win, BLUE, rect)
            elif x == player_x and y == player_y:
                pygame.draw.rect(win, RED, rect)
            elif maze[y][x] == 1:
                pygame.draw.rect(win, WHITE, rect)

    # 检查玩家是否到达出口
    if player_x == exit_x and player_y == exit_y:
        # 游戏结束
        pygame.draw.rect(win, (0, 255, 0), pygame.Rect(exit_x * CELL_SIZE, exit_y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # 更新窗口
    pygame.display.flip()
    pygame.time.Clock().tick(60)

# 退出游戏
pygame.quit()
