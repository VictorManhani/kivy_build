from kivy.lang import Builder
from kivy.uix.spinner import Spinner, SpinnerOption
from kivy.properties import (
    ListProperty, NumericProperty, StringProperty, BooleanProperty, ObjectProperty
)
from kivy.metrics import sp, dp
from kivy.core.window import Window

class HoverBehavior(object):
    """Hover behavior.
    :Events:
        `on_enter`
            Fired when mouse enter the bbox of the widget.
        `on_leave`
            Fired when the mouse exit the widget
    """

    hovered = BooleanProperty(False)
    border_point = ObjectProperty(None)
    '''Contains the last relevant point received by the Hoverable. This can
    be used in `on_enter` or `on_leave` in order to know where was dispatched the event.
    '''

    def __init__(self, **kwargs):
        self.register_event_type('on_enter')
        self.register_event_type('on_leave')
        Window.bind(mouse_pos=self.on_mouse_pos)
        super(HoverBehavior, self).__init__(**kwargs)

    def on_mouse_pos(self, *args):
        if not self.get_root_window():
            return  # do proceed if I'm not displayed <=> If have no parent
        pos = args[1]
        # Next line to_widget allow to compensate for relative layout
        inside = self.collide_point(*self.to_widget(*pos))
        if self.hovered == inside:
            # We have already done what was needed
            return
        self.border_point = pos
        self.hovered = inside
        if inside:
            self.dispatch('on_enter')
        else:
            self.dispatch('on_leave')

    def on_enter(self):
        pass

    def on_leave(self):
        pass

class FlexSpinner(Spinner, HoverBehavior):
    background_color = ListProperty([.5, .5, .5, 1])
    hover_color = ListProperty([.5, .5, 1, 1])
    unhover_color = ListProperty([.5, .5, .5, 1])
    
    def on_enter(self):
        self.background_color = self.hover_color
    
    def on_leave(self):
        self.background_color = self.unhover_color

class FlexSpinnerOption(SpinnerOption, HoverBehavior):
    background_color = ListProperty([.8, .8, .8, 1])
    hover_color = ListProperty([.5, .5, 1, 1])
    unhover_color = ListProperty([.8, .8, .8, 1])
    
    def on_enter(self):
        self.background_color = self.hover_color
    
    def on_leave(self):
        self.background_color = self.unhover_color

class IconSpinner(Spinner, HoverBehavior):
    icon = StringProperty('')
    background_color = ListProperty([.5, .5, .5, 1])
    hover_color = ListProperty([.5, .5, 1, 1])
    unhover_color = ListProperty([.5, .5, .5, 1])
    
    def on_enter(self):
        self.background_color = self.hover_color
    
    def on_leave(self):
        self.background_color = self.unhover_color
    
class IconSpinnerOption(SpinnerOption, HoverBehavior):
    background_color = ListProperty([.8, .8, .8, 1])
    hover_color = ListProperty([.5, .5, 1, 1])
    unhover_color = ListProperty([.8, .8, .8, 1])
    
    def on_enter(self):
        self.background_color = self.hover_color
    
    def on_leave(self):
        self.background_color = self.unhover_color

Builder.load_string('''
#:import rgb kivy.utils.get_color_from_hex
#:import hex kivy.utils.get_hex_from_color
#:import icons kivy_modules.icons.md_icons

<FlexSpinnerOption>:
    markup: True
    background_normal: ''
    color: [.2, .2, .2, 1]
    background_color: [.8, .8, .8, 1]
    
<FlexSpinner>:
	font_size: '20sp'
	markup: True
	text: ''
	background_normal: ''
    color: [.2, .2, .2, 1]
	text_size: self.size
	halign: 'center'
	valign: 'middle'
    option_cls: "FlexSpinnerOption"

<IconSpinnerOption>:
    markup: True
    background_normal: ''
    color: [.2, .2, .2, 1]
    background_color: [.8, .8, .8, 1]
    
<IconSpinner>:
    label: ''
	icon: 'language-python'
	font_size: '20sp'
	markup: True
	text: '[font=kivy_modules\\\\font\\\\icons.ttf]' + icons[self.icon] + '[/font]' + ' [size=' + str(int(self.font_size)) + ']' + self.label + '[/size]'
	background_normal: ''
    color: [.2, .2, .2, 1]
	text_size: self.size
	halign: 'center'
	valign: 'middle'
    background_normal: ''
    option_cls: "IconSpinnerOption"
''')
