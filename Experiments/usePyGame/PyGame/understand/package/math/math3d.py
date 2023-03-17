import pygame

# 创建一个3D向量 (x, y, z)
vector = pygame.math.Vector3(1, 0, 0)

# 绕Y轴旋转90度
rotated_vector = vector.rotate(pygame.math.Vector3(0, 1, 0), 90)

print("旋转后的向量:", rotated_vector)
