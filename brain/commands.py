import os
import webbrowser
import pywhatkit

from voice.speak import speak


def execute_command(command):

    command = command.lower()

    # Open Brave
    if "open brave" in command:

        speak("Okay Sir, Opening Brave")
        os.system("start brave")
        return True

    # Open Chrome (Gmail profile open)
    elif "open chrome" in command:

        speak("Okay Sir, Opening Chrome")

        chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"

        url = "https://mail.google.com/mail/u/0/#inbox"

        os.system(f'start "" "{chrome_path}" {url}')

        return True

    # Open My PC
    elif "open my pc" in command:

        speak("Opening This PC")
        os.startfile("C:\\")
        return True

    # Open VS Code
    elif "open vs code" in command or "open vscode" in command:

        speak("Opening VS Code")
        os.system("code .")
        return True

    # Shutdown PC
    elif "shutdown my pc" in command or "shut down my pc" in command:

        speak("Shutting down your PC")
        os.system("shutdown /s /t 5")
        return True

    # Restart PC
    elif "restart my pc" in command:

        speak("Restarting your PC")
        os.system("shutdown /r /t 5")
        return True

    # Sleep PC (ONLY ONE VERSION)
    elif "sleep my pc" in command or "make my pc sleep" in command:

        speak("Putting your PC to sleep")
        os.system("rundll32.exe powrprof.dll,SetSuspendState Sleep")
        return True

    # Open YouTube
    elif "open youtube" in command:

        speak("Okay Sir, Opening YouTube")
        webbrowser.open("https://youtube.com")
        return True

    # Open WhatsApp
    elif "open whatsapp" in command:

        speak("Okay Sir, Opening WhatsApp")
        os.system("start whatsapp:")
        return True

    # Open Notepad
    elif "open notepad" in command:

        speak("Okay Sir, Opening Notepad")
        os.system("start notepad")
        return True

    # PLAY MUSIC
    elif "play music" in command:

        speak("Playing music")

        song = command.replace("play music", "")
        song = song.replace("in brave", "")
        song = song.replace("on youtube", "")
        song = song.strip()

        if song == "":
            song = "trending songs"

        brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe %s"

        try:
            browser = webbrowser.get(brave_path)
            url = f"https://www.youtube.com/results?search_query={song}"
            browser.open(url)

        except:
            pywhatkit.playonyt(song)

        return True

    return False