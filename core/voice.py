import pyttsx3
from config import ASSISTANT_NAME, VOICE_RATE

engine = pyttsx3.init()
engine.setProperty("rate", VOICE_RATE)

def speak(text):
    msg = f"{ASSISTANT_NAME}: {text}"
    print(msg)
    engine.say(text)
    engine.runAndWait()