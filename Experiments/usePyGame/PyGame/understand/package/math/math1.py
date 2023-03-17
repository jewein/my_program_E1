import pygame
from pygame.math import Vector2

# 创建两个向量
vec1 = Vector2(3, 4)
vec2 = Vector2(1, -2)

# 向量加法
result_add = vec1 + vec2
print("向量加法结果:", result_add)  # 输出: Vector2(4.0, 2.0)

# 向量减法
result_sub = vec1 - vec2
print("向量减法结果:", result_sub)  # 输出: Vector2(2.0, 6.0)

# 向量点乘
dot_product = vec1.dot(vec2)
print("向量点乘结果:", dot_product)  # 输出: -5.0

# 向量叉乘
cross_product = vec2.cross(vec1)
print("向量叉乘结果:", cross_product)  # 输出: -10.0

# 向量的长度（模）
magnitude = vec1.magnitude()
print("向量长度（模）:", magnitude)  # 输出: 5.0

# 将向量转化为单位向量
normalized_vec = vec1.normalize()
print("单位向量:", normalized_vec)  # 输出: Vector2(0.6, 0.8)

# 计算两个向量之间的距离
distance = vec1.distance_to(vec2)
print("向量之间的距离:", distance)  # 输出: 6.324555320336759

# 计算向量的极坐标表示
polar_coords = vec1.as_polar()
print("极坐标表示:", polar_coords)  # 输出: (5.0, 53.13010235415598)

# 从极坐标创建向量
new_vec = Vector2.from_polar(polar_coords)
print("从极坐标创建的向量:", new_vec)  # 输出: Vector2(3.0, 3.9999999999999996)


#计算一个向量到另一个向量的角度
angle = vec1.angle_to(vec2)
print("向量之间的角度:", angle)  # 输出: 135.0

#计算入射向量相对于法线的反射向量。
vec0=vec1.reflect(vec2)
print("反射向量:", vec0)  # 输出: Vector2(2.0, 6.0)



