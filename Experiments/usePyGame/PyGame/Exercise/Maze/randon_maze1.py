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

# 定义玩家初始位置
player_x = random.randint(0, MAZE_SIZE - 1)
player_y = random.randint(0, MAZE_SIZE - 1)

# 定义迷宫出口位置
exit_x = random.choice([0, MAZE_SIZE - 1])
exit_y = random.choice([0, MAZE_SIZE - 1])

# 随机生成迷宫
def generate_maze(x, y):
    maze[y][x] = 0

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    random.shuffle(directions)

    for dx, dy in directions:
        new_x = x + (dx * 2)
        new_y = y + (dy * 2)

        if new_x >= 0 and new_x < MAZE_SIZE and new_y >= 0 and new_y < MAZE_SIZE and maze[new_y][new_x] == 1:
            maze[x + dx][y + dy] = 0
            generate_maze(new_x, new_y)

# 生成迷宫
generate_maze(1, 1)

# 游戏循环标志
running = True
game_over = False

# 游戏主循环
while running:
    # 处理退出事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        # 处理键盘输入
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and player_y > 0 and maze[player_y - 1][player_x] == 0:
            player_y -= 1
        if keys[pygame.K_DOWN] and player_y < MAZE_SIZE - 1 and maze[player_y + 1][player_x] == 0:
            player_y += 1
        if keys[pygame.K_LEFT] and player_x > 0 and maze[player_y][player_x - 1] == 0:
            player_x -= 1
        if keys[pygame.K_RIGHT] and player_x < MAZE_SIZE - 1 and maze[player_y][player_x + 1] == 0:
            player_x += 1

        # 判断是否到达终点
        if player_x == exit_x and player_y == exit_y:
            game_over = True

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

    if game_over:
        # 绘制游戏结束文本
        font = pygame.font.SysFont(None, 50)
        text = font.render("游戏结束", True, RED)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        win.blit(text, text_rect)

    # 更新窗口
    pygame.display.flip()
    pygame.time.Clock().tick(60)

# 退出游戏
pygame.quit()
