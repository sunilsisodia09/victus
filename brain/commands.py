from voice.speak import speak

from automation.apps import *
from automation.browser import *

from tools.youtube import play_song

def execute_command(command):

    # CHROME
    if "chrome" in command:

        speak("Opening Chrome")

        open_chrome()

        return True

    # NOTEPAD
    elif "notepad" in command:

        speak("Opening Notepad")

        open_notepad()

        return True

    # YOUTUBE
    elif "youtube" in command and "play" not in command:

        speak("Opening YouTube")

        open_youtube()

        return True

    # GOOGLE
    elif "google" in command:

        speak("Opening Google")

        open_google()

        return True

    # PLAY SONG
    elif "play" in command:

        song = command.replace("play", "")

        speak(f"Playing {song}")

        play_song(song)

        return True

    # CHATGPT
    elif "chat gpt" in command:

        speak("Opening ChatGPT")

        open_chatgpt()

        return True

    return False