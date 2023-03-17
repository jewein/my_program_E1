import pygame

pygame.init()

window_width = 400
window_height = 300

screen = pygame.display.set_mode()
pygame.display.set_caption("使用pygame.display.flip()")

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 填充背景色（这里使用白色）
    screen.fill((255, 255, 255))

    # 在这里可以添加你的游戏绘制逻辑
    # 例如：绘制角色、敌人、背景等等

    # 更新显示
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
