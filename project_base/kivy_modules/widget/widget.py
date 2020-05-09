from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.clock import Clock

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget

class FlexWidget(Widget):
	pass

Builder.load_string('''
<FlexWidget>:
	background_color: [0,0,0,0]
	background_normal: ''
	background_down: ''
	color: [0.0, 0.4471, 0.8235, 1]
	radius: [0,]
	canvas.before:
		Color:
			rgba: [1,1,1,1]
		RoundedRectangle:
			pos: root.pos
			size: root.size
			radius: root.radius
''')





