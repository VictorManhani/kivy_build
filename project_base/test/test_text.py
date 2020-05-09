from kivy.app import App
from kivy.lang import Builder

import sys
import os
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from kivy_modules.widget.text import FlexText, AutoComplete

class MainApp(App):
    title = 'Test Label'
    def build(self):
        kv = Builder.load_string('''
BoxLayout:
    orientation: 'vertical'
    ScrollView:
        BoxLayout:
            id: container
            orientation: 'vertical'
            size_hint: 1, None
            height: self.minimum_height
            FlexText:
                text: 'FlexText'
                bg_color: [.4, .4,.4, 1]
                size_hint: 1, None
                height: dp(50)
            AutoComplete:
                text: 'AutoComplete'
                bg_color: [.4, .4,.4, 1]
                size_hint: 1, None
                height: dp(50)
''')
        config = {
            'size_hint': [1, None],
            'height': 50
        }
        flextext = FlexText(text = 'flextext dinamic', **config)
        kv.ids.container.add_widget(flextext)
        autocomplete = AutoComplete(text = 'autocomplete dinamic', **config)
        kv.ids.container.add_widget(autocomplete)
        return kv

MainApp().run()