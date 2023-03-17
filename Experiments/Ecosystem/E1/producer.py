from random import random

from organism import Organism


# 生产者类继承Organism类
class Producer(Organism):
    # 定义生产者的基本属性
    max_energy = 100
    max_age = 100
    max_mass = 100

    def __init__(self, environment, x, y, energy=max_energy / 10, age=0):
        super().__init__(environment, x, y, energy, age)


    def absorb(self):
        if self.environment.light:
            if self.energy < self.max_energy:
                self.energy += 5
        # 每次吸收能量+1

    def grow(self):
        # 消耗能量补充质量
        if self.energy <= self.max_energy:
            self.energy -= 1
            self.mass += 1


    def show(self):
        print('植物个体', self, '的信息：')
        super().show()
        print('光合作用：', self.environment.light)








