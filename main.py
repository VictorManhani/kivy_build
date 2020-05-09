# https://pt.stackoverflow.com/questions/275263/como-obter-o-diret%C3%B3rio-do-local-onde-um-arquivo-py-est%C3%A1-sendo-executado
# https://www.geeksforgeeks.org/python-os-path-exists-method/
# https://stackoverflow.com/questions/123198/how-do-i-copy-a-file-in-python
# https://stackoverflow.com/questions/11278066/using-shutil-copyfile-i-get-a-python-ioerror-errno-13-permission-denied
# https://stackoverflow.com/questions/141291/how-to-list-only-top-level-directories-in-python
# https://stackoverflow.com/questions/3397752/copy-multiple-files-in-python

from kivy.app import App
from kivy.lang import Builder

import os
import shutil

class MainApp(App):
    title = "Kivy Project Creator"

    def build(self):
        kv = Builder.load_string("""
FloatLayout:
    orientation: "vertical"
    TextInput:
        id: project_name
        hint_text: "project name"
        text: "meu projeto"
        size_hint: .6, .1
        pos_hint: {"center_x": .5, "center_y": .90}
    TextInput:
        id: project_author
        hint_text: "project author"
        size_hint: .6, .1
        pos_hint: {"center_x": .5, "center_y": .75}
    Button:
        text: "create project"
        size_hint: .3, .1
        pos_hint: {"center_x": .5, "center_y": .10}
        on_release:
            app.create_project()
            print("create")
""")
        self.project_name = kv.ids.project_name
        return kv
    
    def create_project(self):        
        absolute_path = os.path.dirname(os.path.realpath(__file__))
        
        project_base = os.path.join(absolute_path, 'project_base')
        print(project_base)
        
        project_name = self.project_name.text
        project_name = project_name.replace(' ', '_')
        project_name = os.path.join(absolute_path, project_name)
        if not os.path.exists(project_name):
            os.mkdir(project_name)
        print(project_name)
        
        
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