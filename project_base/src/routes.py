import sys
import os
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder

from kivy.metrics import dp
from kivy.properties import StringProperty

from kivy.uix.boxlayout import BoxLayout

# if I want to use some personalized module, I import here in routes.py
# that this module will be available for all pages of this application
from kivy_modules.widget.button import IconButton
from kivy_modules.widget.label import FlexLabel
from kivy_modules.widget.text import FlexText
from kivy_modules.widget.layout import FlexLayout
from kivy_modules.color.color import colors
from kivy_modules.kivyapi import kivyapi

# import the pages here
from .pages.splash.splash import Splash
from .pages.examplebutton.examplebutton import ExampleButton
from .pages.examplelabel.examplelabel import ExampleLabel
from .pages.exampletext.exampletext import ExampleText
from .pages.examplekivyapi.examplekivyapi import ExampleKivyapi

def Routes():
    return Builder.load_string('''
#:import Window kivy.core.window.Window

<ManagerRoot@ScreenManager>:
    id: managerroot

ManagerRoot:
    Splash:
        name: 'splash'
    ExampleButton:
        name: 'examplebutton'
    ExampleLabel:
        name: 'examplelabel'
    ExampleText:
        name: 'exampletext'
    ExampleKivyapi:
        name: 'examplekivyapi'
''')