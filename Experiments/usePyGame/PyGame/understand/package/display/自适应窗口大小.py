import pygame
import sys

pygame.init()

# 窗口尺寸
window_width, window_height = 800, 600

# 创建窗口
# window = pygame.display.set_mode((window_width, window_height), pygame.RESIZABLE  | pygame.SCALED  | pygame.DOUBLEBUF)
window = pygame.display.set_mode((window_width, window_height), pygame.RESIZABLE  | pygame.SCALED  | pygame.DOUBLEBUF | pygame.HWSURFACE)

pygame.display.set_caption("可点击右上角最大化按钮的窗口")

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    # 获取鼠标点击位置
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    # 检查是否点击了右上角按钮区域
                    if mouse_x > window_width - 50 and mouse_y < 50:
                        # toggle_maximize()
                        pass
        window.fill((255, 255, 255))  # 填充窗口背景色
        pygame.draw.rect(window, (0, 0, 255), (window_width - 50, 0, 50, 50))  # 右上角按钮区域

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
