import pyttsx3

from config import VOICE_RATE

engine = pyttsx3.init()

engine.setProperty('rate', VOICE_RATE)

def speak(text):

    print("Victus:", text)

    engine.say(text)

    engine.runAndWait()