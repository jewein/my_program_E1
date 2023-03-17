# 导入Pygame模块
import pygame
from kivy.graphics import Rectangle
from pygame.locals import *

# 导入Kivy模块
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.clock import Clock



# Kivy应用程序类
class KivyPygameApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        # 创建一个Pygame窗口的嵌入式小部件
        pygame_widget = PygameWidget()
        layout.add_widget(pygame_widget)

        return layout

# Pygame的游戏循环和逻辑处理在这个自定义Kivy小部件中进行
class PygameWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # 初始化Pygame
        pygame.init()

        # 设置游戏窗口大小
        self.window_size = (400, 300)

        # 创建Pygame游戏表面
        self.game_surface = pygame.Surface(self.window_size)

        # 定义游戏变量
        self.x = 100
        self.y = 100

        # 设置游戏时钟
        self.clock = pygame.time.Clock()

        # 开始游戏循环
        Clock.schedule_interval(self.update, 1.0 / 60.0)

    def update(self, dt):
        # 游戏逻辑处理
        self.x += 2
        self.y += 1

        # 绘制游戏场景
        self.game_surface.fill((255, 255, 255))
        pygame.draw.circle(self.game_surface, (255, 0, 0), (self.x, self.y), 20)

        # 在Kivy小部件中绘制Pygame游戏表面
        self.canvas.clear()
        self.canvas.ask_update()



        # texture = self.game_surface.get_buffer()
        # texture.blit_buffer(self.game_surface.tostring(), colorfmt='rgb', bufferfmt='ubyte')

        # texture.blit_buffer(self.game_surface.get_buffer().raw, colorfmt='rgb', bufferfmt='ubyte')


    def on_touch_down(self, touch):
        # 处理触摸事件
        pass

# 启动Kivy应用
if __name__ == '__main__':
    KivyPygameApp().run()
