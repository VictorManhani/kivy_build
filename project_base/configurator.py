import yaml

document = """
"name": "example_app"
"version": "1.0.0"
"main": "example_app/main.py"
"description": "A example structure for building projects cross-platform using kivy"
"license": "MIT"
"repository":
    "type": "git"
    "url": "git@github.com:VictorManhani/kivy_build.git"
"engines":
    "python": "3.7.7"
    "kivy": "1.11.1"
"modules":
    "example_app/kivy_modules"
"""

a = yaml.load(document)
a['files'] = "hello"
print(a)