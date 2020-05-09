from kivy.lang import Builder
from kivy.clock import Clock

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.metrics import sp, dp

from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.button import Button
from kivy.properties import BooleanProperty, ListProperty, StringProperty, ObjectProperty
from kivy.uix.recyclegridlayout import RecycleGridLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior

class SelectableRecycleGridLayout(FocusBehavior, LayoutSelectionBehavior,
									RecycleGridLayout):
	''' Adds selection and focus behaviour to the view. '''
	
class SelectableButton(RecycleDataViewBehavior, Button):
	''' Add selection support to the Button '''
	index = None
	selected = BooleanProperty(False)
	selectable = BooleanProperty(True)
	
	def refresh_view_attrs(self, rv, index, data):
		''' Catch and handle the view changes '''
		self.index = index
		return super(SelectableButton, self).refresh_view_attrs(rv, index, data)
	
	def on_touch_down(self, touch):
		''' Add selection on touch down '''
		if super(SelectableButton, self).on_touch_down(touch):
			return True
		if self.collide_point(*touch.pos) and self.selectable:
			return self.parent.select_with_touch(self.index, touch)
	
	def apply_selection(self, rv, index, is_selected):
		''' Respond to the selection of items in the view. '''
		self.selected = is_selected
	
	def on_press(self):
		pass
	
	def update_changes(self, txt):
		self.text = txt

class FlexTable(BoxLayout):
	data_items = ListProperty([])
	
	def __init__(self, **kwargs):
		super(FlexTable, self).__init__(**kwargs)
	
	def get_rows(self, rows):
		# create data_items
		for row in rows:
			for col in row:
				self.data_items.append(col)

Builder.load_string('''
<SelectableButton>:
	# Draw a background to indicate selection
	canvas.before:
		Color:
			rgba: (.0, 0.9, .1, .3) if self.selected else (0, 0, 0, 1)
		Rectangle:
			pos: self.pos
			size: self.size

<FlexTable>:
	BoxLayout:
		orientation: "vertical"
		GridLayout:
			size_hint: 1, None
			size_hint_y: None
			height: 25
			cols: 2
			Label:
				text: "User ID"
			Label:
				text: "User Name"
		BoxLayout:
			RecycleView:
				viewclass: 'SelectableButton'
				data: [{'text': str(x)} for x in root.data_items]
				SelectableRecycleGridLayout:
					cols: 2
					default_size: None, dp(50)
					default_size_hint: 1, None
					size_hint_y: None
					height: self.minimum_height
					orientation: 'vertical'
					multiselect: True
					touch_multiselect: True
''')
