import pygame
import sys

pygame.init()

# 窗口大小和背景颜色
WINDOW_SIZE = (800, 600)
BACKGROUND_COLOR = (255, 255, 255)

# 创建窗口
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Sprite Movement Example")

# 创建精灵图（方块）
sprite_size = 50
sprite_color = (0, 0, 255)
sprite = pygame.Surface((sprite_size, sprite_size))
sprite.fill(sprite_color)
sprite_rect = sprite.get_rect()

# 设置精灵图的初始位置
sprite_rect.center = (WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2)

# 设置移动速度
move_speed = 5

# 事件类型字典，用于判断事件类型对应的操作
event_actions = {
    pygame.QUIT: sys.exit,
    pygame.KEYDOWN: lambda event: handle_keydown(event.key),
    # pygame.KEYUP: lambda event: handle_keyup(event.key)
}

# 处理键盘按下事件
def handle_keydown(key):
    if key == pygame.K_UP:
        sprite_rect.y -= move_speed
    elif key == pygame.K_DOWN:
        sprite_rect.y += move_speed
    elif key == pygame.K_LEFT:
        sprite_rect.x -= move_speed
    elif key == pygame.K_RIGHT:
        sprite_rect.x += move_speed

# 处理键盘释放事件（如果需要）
def handle_keyup(key):
    pass

# 主循环
while True:
    for event in pygame.event.get():
        # 判断事件类型，并执行相应的操作
        if event.type in event_actions:
            event_actions[event.type](event)

    # 清空屏幕
    screen.fill(BACKGROUND_COLOR)

    # 在新位置绘制精灵图
    screen.blit(sprite, sprite_rect)

    # 刷新显示
    pygame.display.flip()


pygame.quit()