from kivy.app import App
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
Window.size = 300, 470

from src.routes import Routes

class MainApp(App):
    title = "Example"
    icon = "assets/icon.png"
    splash = "assets/splash.png"
    theme_color1 = [0.4078, 0.8627, 0.1725, 1] # Verde limão
    theme_color2 = [0.0, 0.6784, 0.9569, 1] # Azul céu
    
    def build(self):
        return Routes()
    
MainApp().run()