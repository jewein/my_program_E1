from organism import Organism


class Consumer(Organism):
    # 定义消费者的基本属性
    max_energy = 100
    max_age = 100
    max_mass = 100

    def __init__(self, environment, x, y, energy=max_energy / 10, age=0):
        super().__init__(environment, x, y, energy, age)

    def eat(self):
        if self.environment.food:
            if self.energy < self.max_energy:
                self.energy += 5
        # 每次吸收能量+1

    def grow(self):
        # 消耗能量补充质量
        if self.energy <= self.max_energy:
            self.energy -= 1
            self.mass += 1
