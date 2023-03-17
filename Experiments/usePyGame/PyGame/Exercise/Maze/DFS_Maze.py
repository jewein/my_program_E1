import pygame
import random

# 初始化 Pygame
pygame.init()

# 设置游戏窗口尺寸
WIDTH = 800
HEIGHT = 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
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

# 设置起点和终点
start_x = random.randint(0, MAZE_SIZE - 1)
start_y = random.randint(0, MAZE_SIZE - 1)
exit_x = random.choice([0, MAZE_SIZE - 1])
exit_y = random.choice([0, MAZE_SIZE - 1])

# 标记已访问的格子
visited = [[False] * MAZE_SIZE for _ in range(MAZE_SIZE)]


def generate_maze(x, y):
    # 标记当前格子为已访问
    visited[y][x] = True

    # 定义四个方向的偏移量，上、右、下、左
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    random.shuffle(directions)

    # 遍历四个方向
    for dx, dy in directions:
        new_x = x + dx
        new_y = y + dy

        # 检查新格子是否在范围内且未访问过
        if 0 <= new_x < MAZE_SIZE and 0 <= new_y < MAZE_SIZE and not visited[new_y][new_x]:
            # 标记路径
            maze[y][x] = 0

            # 递归生成迷宫
            generate_maze(new_x, new_y)


# 生成迷宫
generate_maze(start_x, start_y)

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
    if keys[pygame.K_UP] and start_y > 0 and maze[start_y - 1][start_x] == 0:
        start_y -= 1
    if keys[pygame.K_DOWN] and start_y < MAZE_SIZE - 1 and maze[start_y + 1][start_x] == 0:
        start_y += 1
    if keys[pygame.K_LEFT] and start_x > 0 and maze[start_y][start_x - 1] == 0:
        start_x -= 1
    if keys[pygame.K_RIGHT] and start_x < MAZE_SIZE - 1 and maze[start_y][start_x + 1] == 0:
        start_x += 1

    # 清空窗口
    win.fill(BLACK)

    # 绘制迷宫
    for y in range(MAZE_SIZE):
        for x in range(MAZE_SIZE):
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            if x == exit_x and y == exit_y:
                pygame.draw.rect(win, BLUE, rect)
            elif x == start_x and y == start_y:
                pygame.draw.rect(win, RED, rect)
            elif maze[y][x] == 1:
                pygame.draw.rect(win, WHITE, rect)

    # 到达终点时游戏结束
    if start_x == exit_x and start_y == exit_y:
        running = False

    # 更新窗口
    pygame.display.flip()
    pygame.time.Clock().tick(30)

# 退出游戏
pygame.quit()
