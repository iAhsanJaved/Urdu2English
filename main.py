from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.resources import resource_add_path

from screens import LoginScreen
from screens import RegistrationScreen
from screens import TranslationScreen

import os

def loadResources():
    _PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'assets/img'))
    resource_add_path(_PATH)

def loadkv():
    Builder.load_file(os.path.join('screens',"login.kv"))
    Builder.load_file(os.path.join('screens',"registration.kv"))
    Builder.load_file(os.path.join('screens',"translation.kv"))

class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        self.userData = None
        return RootWidget()

if __name__ == "__main__":
    loadResources()
    loadkv()
    main_app = MainApp()
    main_app.run()