from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.metrics import sp, dp

from kivy.clock import Clock
from kivy.properties import StringProperty, ObjectProperty, BooleanProperty
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window


class HoverBehavior(object):
	hovered = BooleanProperty(False)
	border_point = ObjectProperty(None)

	def init(self, **kwargs):
		self.register_event_type('on_enter')
		self.register_event_type('on_leave')
		Window.bind(mouse_pos=self.on_mouse_pos)
		super(HoverBehavior, self).init(**kwargs)

	def on_mouse_pos(self, _args):
		if not self.get_root_window():
			return
		# do proceed if I'm not displayed <=> If have no parent 
		pos = args[1] #Next line to_widget allow to compensate for relative layout 
		inside = self.collide_point(_self.to_widget(*pos))
		if self.hovered == inside: #We have already done what was needed 
			return
		self.border_point = pos
		self.hovered = inside
		if inside: self.dispatch('on_enter') 
		else: self.dispatch('on_leave')

	def on_enter(self): pass
	def on_leave(self): pass


class ScrollableLabel(ScrollView):
	text = StringProperty('')
	ref_press = ObjectProperty(None)
	markup = BooleanProperty(False)
	__events__ = ['on_ref_press']
	
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		# ~ Clock.schedule_once(self.start, .5)
		
	# ~ def start(self, *args):
		# ~ self.children[0].ref_press = on_ref_press

	def on_touch_down(self, touch):
		label = self.children[0]
		if super(Label, label).on_touch_down(touch):
			return True
		if not len(label.refs):
			return False
		
		tx, ty = touch.pos
		tx -= label.center_x - label.texture_size[0] / 2.
		ty -= label.center_y - label.texture_size[1] / 2.
		ty = label.texture_size[1] - ty
		for uid, zones in label.refs.items():
			for zone in zones:
				x, y, w, h = zone
				if x <= tx <= w and y <= ty <= h:
					self.dispatch('on_ref_press', uid)
					return True
		return False

	def on_ref_press(self, ref):
		print(ref)
		

class FlexLabel(Label):
	font_size = sp(20)


Builder.load_string('''
<ScrollableLabel>:
	Label:
		size_hint_y: None
		height: self.texture_size[1]
		text_size: self.width, None
		text: root.text
		markup: True

<FlexLabel>:
	background_color: [0,0,0,0]
	background_normal: ''
	background_down: ''
	color: [0.0, 0.4471, 0.8235, 1]
	bg_color: [1,1,1,1]
	text_size: self.size
	halign: 'center'
	valign: 'middle'
	radius: [0,]
	canvas.before:
		Color:
			rgba: root.bg_color
		RoundedRectangle:
			pos: root.pos
			size: root.size
			radius: root.radius
''')




