import math

width = 100
height = 100
angle = 45

angle_radians = math.radians(angle)

x1 = 0
y1 = 0

x2 = width * math.cos(angle_radians)
y2 = width * math.sin(angle_radians)

x3 = height * math.sin(angle_radians)
y3 = height * math.cos(angle_radians)

x4 = x2 + x3
y4 = y2 + y3

new_width = max(x2, x3, x4) - min(x1, x2, x3, x4)
new_height = max(y2, y3, y4) - min(y1, y2, y3, y4)

print('new_width:', new_width)
print('new_height:', new_height)


