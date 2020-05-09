from kivy.lang import Builder
from kivy.clock import Clock

from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty, ListProperty, NumericProperty, BooleanProperty
from kivy.metrics import sp, dp

from kivy.core.window import Window
from kivy.utils import get_hex_from_color
from ..icons import md_icons

class AutoComplete(TextInput):
	background_color = ListProperty([1,1,1,1])
	source = [
		"ActionScript", "AppleScript", "Asp", "BASIC", "C", "C++",
		"Clojure", "COBOL", "ColdFusion", "Erlang", "Fortran",
		"Groovy", "Haskell", "Java", "JavaScript", "Lisp", "Perl",
		"PHP", "Python", "Ruby", "Scala", "Scheme"
	]

	def __init__(self, *args, **kwargs):
		super().__init__(**kwargs)
		Clock.schedule_once(self.start)
		
	def start(self, *args):
		pass

class FlexText(TextInput):
	def __init__(self, **kwargs):
		self.background_color = [0,0,0,0]
		self.background_normal = ''
		self.background_active = ''
		#self.color = [1,0,0,1] #[0.0, 0.4471, 0.8235, 1]
		self.font_size = sp(20)
		self.radius = [10,]
		self.border_weigth = dp(1)
		self.bg_color = [0, 0, 1, 1]
		self.border_color = [0.0, 0.4471, 0.8235, 1]
		self.cursor_color = [0, 0, 1, 1]
		self.halign = 'center'
		self.valign = 'middle'
		self.hint_text_color = [0.0, 0.4471, 0.8235, .5]
		self.foreground_color = [0.0, 0.4471, 0.8235, 1]
		self.background_color = [0,0,0,0]
		super().__init__(**kwargs)
		
Builder.load_string('''
<FlexText>:
	canvas.before:
		Color:
			rgba: root.bg_color if self.focus else root.border_color 
		Line:
			points: self.x + 20, self.y, self.x + self.width - 20, self.y
			width: root.border_weigth

	# ~ canvas.before:
		# ~ Clear
		# ~ Color:
			# ~ rgba: root.border_color
		# ~ RoundedRectangle:
			# ~ pos: root.pos
			# ~ size: root.size
			# ~ radius: root.radius
		
		# ~ Color:
            # ~ rgba: self.border_color
        # ~ Rectangle:
            # ~ #texture: root.texture
            # ~ size: root.size
            # ~ pos: root.pos

		# ~ Color:
			# ~ rgba: root.bg_color
		# ~ RoundedRectangle:
			# ~ pos: [(root.pos[0] + (root.border_weigth / 2)), (root.pos[1] + (root.border_weigth / 2))]
			# ~ size: [(root.size[0] - root.border_weigth), (root.size[1] - root.border_weigth)]
			# ~ radius: root.radius
	# ~ canvas.after:
		# ~ Color:
			# ~ rgba: [0,0,0,1]

<AutoComplete>:
	radius: [0,]
	border_color: [.3, .3, .3, 1]
	border_size: 1
	font_color: [0,0,0,1]
	cursor_color: [0,0,0,1]
	canvas.before:
		Color:
			rgba: root.border_color
		RoundedRectangle:
			pos: root.pos
			size: map(lambda x: x + root.border_size, root.size)
			radius: root.radius
		Color:
			rgba: root.background_color
		RoundedRectangle:
			pos: root.pos
			size: root.size
			radius: root.radius
		Color:
			rgba: root.font_color
		Color:
			rgba: root.cursor_color
''')



