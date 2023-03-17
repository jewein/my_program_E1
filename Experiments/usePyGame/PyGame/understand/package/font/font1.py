import pygame
import pygame.font

pygame.init()

# 创建屏幕
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Text Example')

# 加载字体
font = pygame.font.Font('ChineseZodiac.ttf', 72)

# 创建文本对象
text = font.render('abcdef', True, (255, 255, 255))
text1 = font.render('ghijkl', True, (255, 255, 255))

# 显示文本
screen.blit(text, (100, 100))
screen.blit(text1, (100, 200))
pygame.display.flip()

# 游戏循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
