from datetime import time
from random import random

import matplotlib.pyplot as plt
import numpy as np

from consumer import Consumer
from producer import Producer


# 生态系统环境类

class Environment:
    def __init__(self, width, height,light = True,name='大晴天'):
        self.light = light
        self.name = name
        self.width = width
        self.height = height
        # 创建一个二维数组表示环境
        self.grid = np.zeros((height, width))
        self.fig, self.a = plt.subplots()
        self.a.set_xlim(0, width)
        self.a.set_ylim(0, height)
        self.a.set_xticks(range(width + 1))
        self.a.set_yticks(range(height + 1))
        self.organisms = []

    def add(self, organism):
        self.organisms.append(organism)

    def draw(self):
        self.a.clear()
        for organism in self.organisms:
            if not organism.alive:
                color = 'red'
            elif organism.__class__.__name__ == 'Producer':
                color = 'green'
            elif organism.__class__.__name__ == 'Herbivore':
                color = 'yellow'
            elif organism.__class__.__name__ == 'Carnivore':
                color = 'blue'
            else:
                color = 'black'

            #质量越大，绘制的点越大
            size = organism.mass
            self.a.plot(organism.x, organism.y, marker='o', color=color, markersize=size)
            # plt.imshow(self.grid, cmap='viridis')
            # plt.colorbar()
            plt.pause(0.1)
            # time.sleep(1)  # 添加1秒的延迟

            # 更新环境中的生物位置信息
            # environment.update_grid()

    def show(self):
        print('环境信息：')
        print('光照：',self.light)
        print('环境中的所有生物：')
        for organism in self.organisms:
            organism.show()
            print('------------------------')

    def run(self):
        for organism in self.organisms:
            organism.run()
        self.draw()



if __name__ == '__main__':
    environment = Environment(10, 10)
    environment.run()
    plt.show()


