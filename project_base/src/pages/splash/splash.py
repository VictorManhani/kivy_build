from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.screenmanager import FadeTransition
from kivy.core.window import Window

class Splash(Screen):
    def on_enter(self, *args):
        Clock.schedule_once(self.skip, 3)

    def skip(self, dt):
        self.manager.transition = FadeTransition()
        Window.set_title("examplebutton")
        self.manager.current = "examplebutton"

with open('./src/pages/splash/splash.kv', 'r', encoding = 'utf-8') as screen:
    Builder.load_string(screen.read())