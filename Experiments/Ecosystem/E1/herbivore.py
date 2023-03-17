from consumer import Consumer


class Herbivore(Consumer):
    def __init__(self, environment, x, y, energy=max_energy / 10, age=0):
        super().__init__(environment, x, y, energy, age)
        