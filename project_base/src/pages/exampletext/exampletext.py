from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.clock import Clock

class ExampleText(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

with open('./src/pages/exampletext/exampletext.kv', 'r', encoding = 'utf-8') as screen:
    Builder.load_string(screen.read())
