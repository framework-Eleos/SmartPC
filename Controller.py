import pyttsx3
engine = pyttsx3.init()

def Speak(text):
    print(("Speaking: {}").format(text))
    engine.say(text)
    engine.runAndWait()
    print("Speaking: Complete.")
