from kivy.app import App
from kivy.lang import Builder

import sys
import os
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from kivy_modules.widget.button import FlexButton, IconButton, FlatButton

class MainApp(App):
    title = 'Test Button'
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
            IconButton:
                text: 'Facebook'
                icon: 'test_image/facebook_logo.png'
                size_hint: 1, None
                height: dp(50)
                bg_normal: [.25,.4,.7,1]
            IconButton:
                text: 'Google'
                icon: 'test_image/google_logo.png'
                bg_normal: [1,1,1,1]
                color: [.5, .5, .5, 1]
                size_hint: 1, None
                height: dp(50)
            FlatButton:
                text: 'FlatButton'
                bg_normal: [.8, .2,.4, 1]
                size_hint: 1, None
                height: dp(50)
            FlexButton:
                text: 'FlexButton'
                bg_color: [.4, .4,.4, 1]
                size_hint: 1, None
                height: dp(50)
''')
        config = {
            'size_hint': [1, None],
            'height': 50
        }
        flexbutton = FlexButton(text = 'flexbutton dinamic', **config)
        kv.ids.container.add_widget(flexbutton)
        iconbutton = IconButton(text = 'iconbutton dinamic', **config)
        kv.ids.container.add_widget(iconbutton)
        flatbutton = FlatButton(text = 'flatbutton dinamic', **config)
        kv.ids.container.add_widget(flatbutton)
        return kv

MainApp().run()