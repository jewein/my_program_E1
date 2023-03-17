import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
# screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Modifier Keys Example")

# 创建字体对象
font = pygame.font.Font(None, 30)

mods = pygame.KMOD_SHIFT | pygame.KMOD_CTRL
pygame.key.set_mods(mods)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # 获取修饰键状态
    mods = pygame.key.get_mods()

    # 检查修饰键的状态
    mods = pygame.key.get_mods()
    shift_pressed = mods & pygame.KMOD_SHIFT
    ctrl_pressed = mods & pygame.KMOD_CTRL
    alt_pressed = mods & pygame.KMOD_ALT
    num_lock = mods & pygame.KMOD_NUM
    caps_lock = mods & pygame.KMOD_CAPS

    # 在屏幕上绘制文本显示修饰键的状态
    screen.fill((255, 255, 255))
    text = font.render(f"Shift pressed: {bool(shift_pressed)}", True, (0, 0, 0))
    screen.blit(text, (20, 20))
    text = font.render(f"Ctrl pressed: {bool(ctrl_pressed)}", True, (0, 0, 0))
    screen.blit(text, (20, 50))
    text = font.render(f"Alt pressed: {bool(alt_pressed)}", True, (0, 0, 0))
    screen.blit(text, (20, 80))
    text = font.render(f"Num Lock active: {bool(num_lock)}", True, (0, 0, 0))
    screen.blit(text, (20, 110))
    text = font.render(f"Caps Lock active: {bool(caps_lock)}", True, (0, 0, 0))
    screen.blit(text, (20, 140))

    pygame.display.flip()
    pygame.time.Clock().tick(20)
    pygame.display.update()
