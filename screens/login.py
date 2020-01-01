from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
import re

from models import User

class LoginScreen(Screen):
    username = ObjectProperty(None)
    password = ObjectProperty(None)
    info = ObjectProperty(None)
    
    def loginBtn(self):
        if self.validate_user():
            user = User(self.username.text, self.password.text)
            resultRecord = user.authenticate()
            if len(resultRecord) > 0:
                self.info.text = '[color=#FFFF]Logged In successfully![/color]'
                App.get_running_app().root.userData = resultRecord[0]
                App.get_running_app().root.current = "Translation"
            else:
                self.info.text = '[color=#FF0000]Username or password is incorrect![/color]'

    def registerBtn(self):
        self.reset()
        App.get_running_app().root.current = "Registration"
    
    def reset(self):
        self.username.text = ""
        self.password.text = ""
        self.info.text = ""

    def validate_user(self):
        if self.username.text == "" or self.password.text == "":
            self.info.text = '[color=#FF0000]Username and password are required![/color]'
            return False
        elif re.search("^[a-zA-Z0-9_.-]+$",self.username.text) == None:
            self.info.text = '[color=#FF0000]Username is invalid[/color]'
            return False
        else:
            return True
