import pygame
import sys

pygame.init()

# 设置游戏窗口
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Keyboard Repeat Example")
pygame.key.set_repeat(500, 100)

clock = pygame.time.Clock()

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # 获取当前键盘重复事件的设置
        delay, interval = pygame.key.get_repeat()
        if delay is not None and interval is not None:
            print(f"当前键盘重复事件的设置：延迟时间 = {delay}ms，重复间隔时间 = {interval}ms")
        else:
            print("键盘重复事件当前被禁用")

        screen.fill((255, 255, 255))
        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()


