import pygame
import random

# 初始化 Pygame
pygame.init()

# 设置游戏窗口尺寸
WIDTH = 800
HEIGHT = 600
win = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
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
maze = [[1] * MAZE_SIZE for _ in range(MAZE_SIZE)]

# 设置起点和终点位置
start_x = random.randint(1, MAZE_SIZE - 2)
start_y = random.randint(1, MAZE_SIZE - 2)
exit_x = random.choice([0, MAZE_SIZE - 1])
exit_y = random.choice([0, MAZE_SIZE - 1])

# 递归生成迷宫
def generate_maze(x, y):
    maze[y][x] = 0
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    random.shuffle(directions)
    for dx, dy in directions:
        nx, ny = x + 2 * dx, y + 2 * dy
        if 0 <= nx < MAZE_SIZE and 0 <= ny < MAZE_SIZE and maze[ny][nx] == 1:
            maze[y + dy][x + dx] = 0
            generate_maze(nx, ny)

# 生成迷宫
generate_maze(start_x, start_y)

# 获取周围可行走的方向
def get_valid_directions(x, y):
    directions = []
    if x > 1 and maze[y][x - 2] == 0:
        directions.append((-1, 0))  # 左
    if x < MAZE_SIZE - 2 and maze[y][x + 2] == 0:
        directions.append((1, 0))  # 右
    if y > 1 and maze[y - 2][x] == 0:
        directions.append((0, -1))  # 上
    if y < MAZE_SIZE - 2 and maze[y + 2][x] == 0:
        directions.append((0, 1))  # 下
    return directions

# 玩家初始位置
player_x, player_y = start_x, start_y

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
    if keys[pygame.K_UP]:
        dx, dy = (0, -1)
    elif keys[pygame.K_DOWN]:
        dx, dy = (0, 1)
    elif keys[pygame.K_LEFT]:
        dx, dy = (-1, 0)
    elif keys[pygame.K_RIGHT]:
        dx, dy = (1, 0)
    else:
        dx, dy = (0, 0)

    # 移动玩家
    if (player_x + dx, player_y + dy) != (player_x, player_y) and (0 <= player_x + 2 * dx < MAZE_SIZE) and (0 <= player_y + 2 * dy < MAZE_SIZE) and maze[player_y + dy][player_x + dx] == 0:
        player_x += dx
        player_y += dy

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

    # 判断是否到达终点
    if player_x == exit_x and player_y == exit_y:
        font = pygame.font.Font(None, 36)
        text = font.render("游戏结束", True, RED)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        win.blit(text, text_rect)
        running = False

    # 更新窗口
    pygame.display.flip()
    pygame.time.Clock().tick(60)

# 退出游戏
pygame.quit()
