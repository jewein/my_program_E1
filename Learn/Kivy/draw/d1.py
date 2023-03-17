from kivy.clock import Clock
from kivy.config import Config
Config.set('graphics', 'window_state', 'visible')
Config.set('graphics', 'borderless', True)
Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '600')
Config.write()

from kivy import Config
Config.set('graphics', 'multisamples', '0')

from kivy import platform
if platform == 'android':
    from kivy.logger import Logger
    Logger.info("APP: " + platform)
    from kivy.app import App

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.image import Image

import pygame
pygame.init()

class PygameSurface(pygame.Surface):
    pass


class MyWidget(Widget):
    def __init__(self, **kwargs):
        super(MyWidget, self).__init__(**kwargs)

        # 创建一个 PygameSurface 对象
        self.pygame_surface = PygameSurface((800, 600))

        # 将 PygameSurface 转换为 Kivy 的 Image 组件
        self.image = Image(texture=self.pygame_surface.texture)
        self.add_widget(self.image)

class MyWidget(Widget):
    def update(self, dt):
        # 在 PygameSurface 上绘制图形
        pygame.draw.rect(self.pygame_surface, (255, 0, 0), pygame.Rect(100, 100, 200, 150))
        pygame.draw.circle(self.pygame_surface, (0, 255, 0), (400, 300), 50)
        pygame.draw.line(self.pygame_surface, (0, 0, 255), (500, 200), (600, 400), 5)

        # 刷新 Kivy 中的 Image 组件
        self.image.texture.blit_buffer(self.pygame_surface.get_buffer().raw, colorfmt='rgb', bufferfmt='ubyte')

class MyApp(App):
    def build(self):
        self.widget = MyWidget()
        Clock.schedule_interval(self.widget.update, 1.0 / 60.0)
        return self.widget

if __name__ == '__main__':
    MyApp().run()




