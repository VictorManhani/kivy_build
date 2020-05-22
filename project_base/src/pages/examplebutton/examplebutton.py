from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock

from kivy_modules.kivyapi import kivyapi

class ExampleButton(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def change_text(self, but1):
        if but1.text == 'text1':
            but1.text = 'text2'
        else:
            but1.text = 'text1'

with open('./src/pages/examplebutton/examplebutton.kv', 'r', encoding = 'utf-8') as screen:
    Builder.load_string(screen.read())