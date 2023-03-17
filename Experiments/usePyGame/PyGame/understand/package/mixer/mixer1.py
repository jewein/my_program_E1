import pygame
import time

pygame.mixer.init()
pygame.mixer.music.load("background_music.mp3")
pygame.mixer.music.play(-1)  # 循环播放背景音乐

sound_effect = pygame.mixer.Sound("sound_effect.wav")
sound_effect.play()  # 播放音效

time.sleep(15)  # 等待5秒钟

pygame.mixer.music.stop()  # 停止背景音乐
pygame.mixer.quit()  # 关闭音频模块
