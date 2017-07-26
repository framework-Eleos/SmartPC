import pyttsx3
from kuai import Kuai, set_backend
set_backend("threadpool")



engine = pyttsx3.init()
engine.setProperty('rate', 130)

def Speak(text):
    print(("Speaking: {}").format(text))
    engine.say(text)
    engine.runAndWait()
    print("Speaking: Complete.")
