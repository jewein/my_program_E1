import pygame
import pygame.font

pygame.init()

# 创建屏幕
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('中文文本示例')

# 加载中文字体
font = pygame.font.Font('STHUPO.TTF', 72)

# 创建文本对象
text = font.render('你好，世界！', True, (255, 255, 255))
text1 = font.render('你好，世界！', True, (128, 128, 255))
text2 = font.render('你好，世界！', True, (128, 255, 128))
text3 = font.render('你好，世界！', True, (255, 128, 128))

# 显示文本
screen.blit(text1, (200, 200))
screen.blit(text2, (300, 300))
screen.blit(text3, (400, 300))
screen.blit(text, (100, 100))
pygame.display.flip()

# 游戏循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
