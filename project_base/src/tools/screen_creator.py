from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
Window.size = [300, 300]

import os
import sys
import shutil

SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
PACKAGE_PARENT = '\\'.join([path for path in SCRIPT_DIR.split('\\')][:-2])
sys.path.insert(0, PACKAGE_PARENT)

from kivy_modules.kivyapi import kivyapi

class MainApp(App):
    title = "Kivy Screen Creator"

    def build(self):
        kv = Builder.load_string("""
FloatLayout:
    orientation: "vertical"
    TextInput:
        id: project_name
        hint_text: "screen name"
        text: "Example Label"
        size_hint: .6, .1
        pos_hint: {"center_x": .5, "center_y": .90}
    Button:
        text: "create project"
        size_hint: .3, .1
        pos_hint: {"center_x": .5, "center_y": .10}
        on_release:
            app.create_screen()
""")
        self.project_name = kv.ids.project_name
        return kv
    
    def create_screen(self):
        pages_path = os.path.join(sys.path[0], "src", "pages")
        
        screen_name = self.project_name.text
        
        class_name = screen_name.title()
        class_name = class_name.replace(' ', '')
        
        path_name = screen_name.lower()
        path_name = path_name.replace(' ', '')
        path_name = os.path.join(pages_path, path_name)
        
        file_name = screen_name.lower()
        file_name = file_name.replace(' ', '')
        file_path = os.path.join(path_name, file_name)
        
        # verify if pages path exists, if no make one 
        # and the py and kv files 
        if not os.path.exists(path_name):
            os.mkdir(path_name)

            # python file
            with open(file_path + '.py', 'w') as f:
                f.write(f"""\
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.clock import Clock

class {class_name}(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

with open('./src/pages/{file_name}/{file_name}.kv', 'r', encoding = 'utf-8') as screen:
    Builder.load_string(screen.read())
""")
            # kivy file
            with open(file_path + '.kv', 'w') as f:
                f.write(f"""\
<{class_name}>:
	FlexLayout:
		FlexLayout:
			orientation: "horizontal"
            FlexLabel:
                text: "Hello {screen_name}!"
		FlexLayout:
			orientation: "horizontal"
			FlexButton:
				text: "<- button"
				on_release:
					app.root.current = "examplebutton"
			FlexButton:
				text: "text ->"
				on_release:
					app.root.current = "exampletext"
""")

    def create_project(self):        
        absolute_path = os.path.dirname(os.path.realpath(__file__))
        
        project_base = os.path.join(absolute_path, 'project_base')
        
        project_name = self.project_name.text
        project_name = project_name.replace(' ', '_')
        project_name = os.path.join(absolute_path, project_name)
        if not os.path.exists(project_name):
            os.mkdir(project_name)        
        
        # copy all files and paths from project_base to project_name
        def recursive_copy(src, dest):
            for item in os.listdir(src):
                file_path = os.path.join(src, item)

                # if item is a file, copy it
                if os.path.isfile(file_path):
                    shutil.copy(file_path, dest)

                # else if item is a folder, recurse 
                elif os.path.isdir(file_path):
                    new_dest = os.path.join(dest, item)
                    os.mkdir(new_dest)
                    recursive_copy(file_path, new_dest)
        
        recursive_copy(project_base, project_name)

MainApp().run()