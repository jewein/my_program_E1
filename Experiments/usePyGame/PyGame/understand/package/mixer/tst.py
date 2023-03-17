import pygame

# 初始化Pygame
pygame.init()

# 初始化音频模块
pygame.mixer.init()

# 加载音效和音乐
sound_effect = pygame.mixer.Sound("sound_effect.wav")
background_music = pygame.mixer.Sound("background_music.mp3")

# 设置音量（0.0为最小，1.0为最大）
sound_effect.set_volume(0.5)
background_music.set_volume(0.3)

# 播放音效和音乐
sound_effect.play()
background_music.play(-1)  # -1表示循环播放

# 等待5秒钟
pygame.time.wait(5000)

# 停止音效和音乐
sound_effect.stop()
background_music.stop()

# 退出Pygame
pygame.quit()
