import speech_recognition as sr
from googletrans import Translator

class SpeechRecognizer:
    def __init__(self):
        self.urdu = ''
        self.english = ''
     
    def urduToEnglish(self):
        translator = Translator()
        eng = translator.translate(self.urdu, dest='en')
        print(eng)
        self.english = eng.text
        return self.english

    def speechToUrduText(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Speak now")
            r.energy_threshold = 10000
            audio = r.listen(source) #Starts Listening
            print("Thanks")
        try:
            text = r.recognize_google(audio,language='ur')
            self.urdu = text
            return True
        except:
            return False