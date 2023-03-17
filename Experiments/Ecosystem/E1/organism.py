from random import random


#定义生物基类
class Organism(object):
    #定义生物的基本属性

    max_energy = 100
    max_age = 100
    max_mass = 10

    def __init__(self,environment,x,y,energy=max_energy/10,mass=1,age=0):
        self.environment = environment
        self.environment.organisms.append(self)
        self.x = x
        self.y = y
        self.energy = energy
        self.mass = mass
        self.age = age
        self.son=[]
        self.alive=True


    def grow(self):
        #消耗能量补充质量
        if self.energy <= self.max_energy:
            self.energy -= 1
            self.mass += 1
        if self.age >= self.max_age:
            self.alive=False
            self.mass-=1
        if self.mass <= 0:
            #物质消失，移除对象
            self.environment.organisms.remove(self)


    def reproduce(self):
        #energy = max_energy时消耗一半进行繁殖，新个体在附近
        if self.energy >= self.max_energy and self.mass>=self.max_mass:
            #控制台显示当前对象的信息
            print("个体",self,'进行了繁殖。')
            self.energy = self.energy *0.5
            self.mass = self.mass *0.9
            #新个体在附近
            # self.environment.organisms.append(self.__class__(self.environment,self.x+1,self.y+1,self.energy,self.age))
            x=self.x+random.randint(-1,1)
            y=self.y+random.randint(-1,1)
            self.son.append(self.__class__(self.environment,x,y))

    def run(self):
        self.age += 1
        if self.alive:
            self.grow()

            #随机决定余下操作
            if random() < 0.5:
                self.reproduce()


    def show(self):
        print('个体',self,'的信息：')
        print('环境：', self.environment)
        print('坐标：',self.x,',',self.y)
        print('状态：','存活' if self.alive else '死亡')
        print('质量/最大质量：',self.mass,'/',self.max_mass)
        print('能量/最大能量：',self.energy,'/',self.max_energy)
        print('年龄/最大年龄：',self.age,'/',self.max_age)
        print('子代：',self.son)

    def paint(self):
        pass















