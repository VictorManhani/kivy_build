from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock

from kivy_modules.kivyapi import kivyapi

class Example(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.start, 4)
        
    def start(self, evt):
        def callback(response):
            self.ids.texto.text = response.json()['login']
        
        url_get = "https://api.github.com/users/VictorManhani"
        kivyapi.get(url = url_get).after(callback).catch(
            lambda error: print(error)
        )

with open('./src/pages/example/example.kv', 'r', encoding = 'utf-8') as screen:
    Builder.load_string(screen.read())