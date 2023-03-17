
import pygame
pygame.init()
window=pygame.display.set_mode((800,600))


while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()

        time = pygame.time.get_ticks()
        print(time)

    pygame.display.flip()




time=pygame.time.get_ticks()



pygame.quit()













