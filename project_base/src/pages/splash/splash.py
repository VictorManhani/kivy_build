from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.screenmanager import FadeTransition

class Splash(Screen):
    def skip(self, dt):
        self.manager.transition = FadeTransition()
        self.manager.current = "example"

    def on_enter(self, *args):
        Clock.schedule_once(self.skip, 3)

with open('./src/pages/splash/splash.kv', 'r', encoding = 'utf-8') as screen:
    Builder.load_string(screen.read())