import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

pygame.mixer.init()
pygame.mixer.music.load("background_music.mp3")
pygame.mixer.music.play(-1)  # 循环播放背景音乐

sound_effect = pygame.mixer.Sound("sound_effect.wav")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            sound_effect.play()  # 播放音效

    screen.fill((255, 255, 255))
    pygame.display.flip()
    clock.tick(60)

pygame.mixer.quit()
pygame.quit()
