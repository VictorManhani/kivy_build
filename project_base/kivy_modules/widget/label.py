from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.metrics import sp, dp

from kivy.clock import Clock
from kivy.properties import StringProperty, ObjectProperty, BooleanProperty
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

import json
import pprint

class HoverBehavior(object):
	hovered = BooleanProperty(False)
	border_point = ObjectProperty(None)

	def init(self, **kwargs):
		self.register_event_type('on_enter')
		self.register_event_type('on_leave')
		Window.bind(mouse_pos=self.on_mouse_pos)
		super(HoverBehavior, self).init(**kwargs)

	def on_mouse_pos(self, args):
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

# label with a pretty representation of text
# inspired by pprint module
class PrettyLabel(ScrollView):
    text = StringProperty('')
    padding = 10
    
    def init(self, *args, **kwargs):
        super(PrettyLabel, self).init(*args, **kwargs)
        self.text = '%s' % 'hello top day dia africanner ' * 100

    def pprint(self, obj, sort_keys = False, indent = 4):
        """Pretty-print a Python object to a stream [default is sys.stdout]."""
        # pprint.pprint(
        #     obj, indent = indent, width = self.width,
        #     depth = 1, stream = self,
        # )

        self.text = json.dumps(
            obj, sort_keys = sort_keys,
            indent = indent, separators = (',', ': ')
		)

    def write(self, text):
        self.text += text

Builder.load_string('''
<PrettyLabel>:
	do_scroll_y: True
	do_scroll_x: True
    scroll_type: ['bars']
    bar_width: dp(10)
    bar_color: [.2, .2, 1, 1]
    effect_cls: 'ScrollEffect'
    Label:
		# color: [.2,.2, .2, 1]
        size_hint: None, None
        width: dp(600)
        height: self.texture_size[1]
        text_size_x: self.width
        padding: 10, 10
        text: root.text
        # markup: True
        # # text_size: self.size
        # halign: 'left'
        # valign: 'middle'
        # padding: 10, 10
        canvas.before:
			Color:
				rgba: [.3,.3,.3,1]
			Rectangle:
				pos: self.pos
				size: self.size

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
	color: [.3, .3, .3, 1]
	bg_color: [1, 1, 1, 1]
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




