from kivy.app import App
from kivy.lang import Builder

kv = Builder.load_string('''
Image:
	source: 'test_image/duo.gif'
''')

class MyApp(App):
	def build(self):
		return kv
		
MyApp().run()