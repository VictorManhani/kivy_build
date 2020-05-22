from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock

from kivy_modules.kivyapi import kivyapi

class ExampleKivyapi(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def call_api(self, url):
        def callback(response):
            self.ids.texting.text = response.json()['login']
        
        kivyapi.get(url = url).after(callback).catch(
            lambda error: print(error)
        )

with open('./src/pages/examplekivyapi/examplekivyapi.kv', 'r', encoding = 'utf-8') as screen:
    Builder.load_string(screen.read())