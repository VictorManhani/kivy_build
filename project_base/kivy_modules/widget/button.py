from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import (
    ListProperty, NumericProperty, StringProperty, OptionProperty
)
from kivy.metrics import sp, dp
from kivy.uix.behaviors import TouchRippleBehavior
from kivy.uix.behaviors import TouchRippleBehavior

from ..behavior.ripplebehavior import CircularRippleBehavior, RectangularRippleBehavior

class FlatButton(Button):
	pass

class ImageButton(Button):
	pass

class IconButton(Button):
	icon = StringProperty('')

class FlexButton(RectangularRippleBehavior, Button):
	ripple_duration_in_fast = 0.2
	background_color = [0,0,0,0]
	background_normal = ''
	background_down = ''
	color = ListProperty([0.0, 0.4471, 0.8235, 1])
	font_size = sp(20)
	radius = [10,]
	bg_color = ListProperty([1,1,1,1])
	border_color = ListProperty([0.0, 0.4471, 0.8235, 1])
	border_weigth = NumericProperty(dp(1))
 
	button_type = OptionProperty("rounded", options = ['rectangle', 'rounded'])
	primary_color = [0.12, 0.58, 0.95, 1]
	font_color = [.3,.3,.3,1]
	border_width = 2
 
	def __init__(self, **kwargs):
		self.halign = 'center'
		self.valign = 'middle'
		super(FlexButton, self).__init__(**kwargs)
		self.button_type_define(self.button_type)
		# self.text_size = self.size
		self.ripple_color = [0.0, 0.6784, 0.9569, 1]

	def button_type_define(self, button_type):
		if button_type == 'rectangle':
			Builder.load_string("""
<FlexButton>:
    color: root.font_color # root.primary_color

    canvas.before:
        Color:
            rgba: root.primary_color
        Line:
            width: root.border_width
            rectangle: (self.x, self.y, self.width, self.height)
""", filename="rectangle_button.kv")

	# def on_press(self, *args):
	# 	# ~ self.color = [0.0196, 0.4235, 0.7608, 1]
	# 	# ~ self.border_color = [0.0196, 0.4235, 0.7608, 1]
	# 	self.color = [0,0,.8, 1]
	# 	self.border_color = [0,0,.8, 1]

	# def on_release(self, *args):
	# 	self.color = [0.0, 0.4471, 0.8235, 1]
	# 	self.border_color = [0.0, 0.4471, 0.8235, 1]

Builder.load_string('''
#:import rgb kivy.utils.get_color_from_hex
#:import hex kivy.utils.get_hex_from_color
#:import icons kivy_modules.icons.md_icons

<FlexButton>:
	ripple_color: root.ripple_color
	# ripple_color: [0, 0, 0, .2]
	color: root.font_color
	canvas.before:
		Color:
			rgba: root.border_color
		RoundedRectangle:
			pos: root.pos
			size: root.size
			radius: root.radius
		Color:
			rgba: root.bg_color
		RoundedRectangle:
			pos: [(root.pos[0] + (root.border_weigth / 2)), (root.pos[1] + (root.border_weigth / 2))]
			size: [(root.size[0] - root.border_weigth), (root.size[1] - root.border_weigth)]
			radius: root.radius

<FlatButton>:
	color: [1,1,1,1]
	background_color: [0,0,0,0]
	shadow: True
	shadow_elevation: 2
	shadow_color: [.2,.2,.2, .3]
	bg_press: list(map(lambda c: c-.1, root.bg_normal))
	bg_normal: [.1,.5,.8,1]
	halign: 'center'
	valign: 'middle'
	markup: True
	text_hint: root.size
	background_normal: ''
	background_down: ''
	
	canvas.before:
		Color:
			rgba: root.shadow_color
		RoundedRectangle:
			pos: self.pos[0], self.pos[1] - root.shadow_elevation
			size: self.size
		Color:
			rgba: root.bg_normal if root.state == 'normal' else root.bg_press
		RoundedRectangle:
			pos: self.pos
			size: self.size
			radius: [5,]

<ImageButton>:
	icon: ''
	color: [1,1,1,1]
	background_color: [0,0,0,0]
	shadow: True
	shadow_elevation: 2
	shadow_color: [.2,.2,.2, .3]
	bg_press: list(map(lambda c: c-.1, root.bg_normal))
	bg_normal: [.1,.5,.8,1]
	halign: 'center'
	valign: 'middle'
	markup: True
	text_hint: root.size
	background_normal: ''
	background_down: ''
	
	canvas.before:
		Color:
			rgba: root.shadow_color
		RoundedRectangle:
			pos: self.pos[0], self.pos[1] - root.shadow_elevation
			size: self.size
		Color:
			rgba: root.bg_normal if root.state == 'normal' else root.bg_press
		RoundedRectangle:
			pos: self.pos
			size: self.size
			radius: [5,]
		Color:
			rgba: [1,1,1,1]
		RoundedRectangle:
			source: root.icon
			pos: self.pos[0] + 10, self.pos[1] + 10
			size: dp(24), dp(24)

<IconButton>:
	label: ''
	icon: 'language-python'
	font_size: '20sp'
	markup: True
	text: '[font=kivy_modules\\\\font\\\\icons.ttf]' + icons[self.icon] + '[/font]' + ' [size=' + str(int(self.font_size)) + ']' + self.label + '[/size]'
	background_normal: ''
	background_color: [1,1,1,1]
	text_size: self.size
	halign: 'center'
	valign: 'middle'

<Chip@Button, RippleBehavior>:
	label: 'label'
	icon: 'icon'
	size_hint: .33, .8
	background_normal: ''
	#background_pressed: ''
	font_size: '16sp'
	font_color: [.2, .2, .2, 1]
	icon_color: [1, 1, 1, 1]
	icon_size: '20sp'
	icon_size_second: '40sp'
	icon_color_second: [1, 1, 1, 1]
	font_style: 'kivy_modules//font//icons.ttf'
	markup: True
	text:  '[size=' + self.icon_size + '][color=' + hex(self.icon_color) + '][font=' + self.font_style + ']' + self.icon + '[/font][/color][/size]' + '\\n[color=' + hex(self.font_color) + ']' + self.label + '[/color]\\n[size=' + self.icon_size_second + '][sub][font=' + self.font_style + '][color=]' + hex(root.icon_color_second) + ' \uf1a5[/font]5[/sub][/size][/color]'
	background_color: [0, 0, 0, 0]
	bg_color: [255/255, 199/255, 21/255, 1]
	#color: 1,1,1,1
	#radius: 80
	text_size: self.size
	halign: 'center'
	valign: 'middle'
	canvas.before:
		Color:
			rgba: root.bg_color if root.state == 'normal' else list(map(lambda x: x - .1, root.bg_color))
		RoundedRectangle:
			pos: root.pos
			size: root.size
			#radius: [root.radius]

<IconToggleButton@ToggleButton>:
	background_normal: ''
	background_color: [1,1,1,1]
	text_size: self.size
	halign: 'center'
	valign: 'middle'
	font_name: 'kivy_modules//font//icons.ttf'
	#MaterialIcons-Regular.ttf'
	font_size: '30sp'

<RoundButton@Button>:
	label: ''
	icon: ''
	icon_size: '15sp'
	icon_color: [1, 1, 1, 1]
	font_size: '10sp'
	font_color: [.2, .2, .2, 1]
	markup: True
	text: ' [size=' + self.icon_size + ']' + '[color=' + hex(self.icon_color) + ']' + '[font=kivy_modules//font//icons.ttf]' + self.icon + '[/font]' + '[/color]' +  '[/size]' + '[color=' + hex(self.font_color) + ']' + self.label + '[/color]'
	background_normal: ''
	background_down: ''
	background_color: [0,0,0,0]
	bg_normal: [1, 0.78, 0.08, 1]
	bg_down: self.bg_normal[0:2] + [.5]
	color: [1,1,1,1]
	text_size: self.size
	halign: 'center'
	valign: 'middle'
	canvas.before:
		Color:
			rgba: self.bg_normal if self.state == 'normal' else self.bg_down
		RoundedRectangle:
			pos: self.pos
			size: self.size
			radius: [80,]

# <Button>:
# 	background_normal: ''
# 	background_color: [1, .6, 0, 1]
# 	text_size: self.size
# 	halign: 'center'
# 	valign: 'middle'
# 	font_size: '20sp'
''')


