import pygame


# 初始化Pygame
pygame.init()

# 窗口尺寸
WINDOW_WIDTH, WINDOW_HEIGHT = 400, 400

# 加载图像
image_path = "image.png"  # 将"path_to_your_image.png"替换为你自己的图像路径
image = pygame.image.load(image_path)

# 创建窗口
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pygame Surfarray Example")

# 将图像转换为二维NumPy数组
image_array = pygame.surfarray.array2d(image)

# 输出图像的像素值（仅显示前10x10像素）
print("Image Array:")
#输出到文件中
with open("image_array.txt","w") as f:
    for i in image_array:
        for j in i:
            f.write(str(j)+" ")
        f.write("\n")



# 图像反色处理
inverted_image_array = 255 - image_array

# 输出反色处理后的图像像素值（仅显示前10x10像素）
print("Inverted Image Array:")
print(inverted_image_array[:10, :10])

# 主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 绘制图像
    window.fill((255, 255, 255))
    window.blit(image, (0, 0))
    pygame.display.flip()

# 退出Pygame
pygame.quit()
