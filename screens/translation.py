from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivy.clock import Clock

import re
import time
import threading

from core import SpeechRecognizer
from models import Translate

class TranslationScreen(Screen):
    translateResult = ObjectProperty(None)
    img = ObjectProperty(None)
    listenState = False
    animationFrame = 0
    
    def translateBtn(self):
        self.reset()
        self.listenState = not self.listenState
        if self.listenState:
            self.animationEvent =  Clock.schedule_interval(self.animation, 0.1)
            #Clock.schedule_once(self.startSpeechRecognition, 0.5) 
            thd = threading.Thread(target=self.startSpeechRecognition, args=(self,))
            thd.start()
        else:
            self.animationEvent.cancel()
            self.img.source = 'start.png'
            
    def reset(self):
        self.translateResult.text = ""
        pass

    def animation(self, *args):
        self.animationFrame = (self.animationFrame+1)%4
        self.img.source = 'listening{}.png'.format(self.animationFrame)
    
    def startSpeechRecognition(self, *args):
        speechRecognizer = SpeechRecognizer()
        if speechRecognizer.speechToUrduText():
            speechRecognizer.urduToEnglish()
            translated_result = str(speechRecognizer.english)
            if translated_result != '':
                user_id = list(App.get_running_app().root.userData)[0]
                print('user_id', user_id)
                print('translated_result', translated_result)
                translate = Translate(translated_result, user_id)
                translate.storeResult()
                self.translateResult.text = translated_result

        else:
            self.translateResult.text = "[color=#FF0000]Sorry, couldn't hear you![/color]"
        
        self.animationEvent.cancel()
        self.img.source = 'start.png'
        self.listenState = False
    
        

