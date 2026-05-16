import os
import webbrowser
import pywhatkit
import urllib.parse
import pyautogui
import time

from voice.speak import speak


# =====================================================
# CONTACTS
# =====================================================

contacts = {
    "shubham sharma": "+917454966112",
    "aman": "+91xxxxxxxxxx",
    "rohit": "+91xxxxxxxxxx"
}


# =====================================================
# OPEN APPS FUNCTION
# =====================================================

def open_app(command):

    command = command.lower()

    try:

        # =================================================
        # SIMPLE APPS
        # =================================================

        if "brave" in command:

            speak("Opening Brave")
            os.system("start brave")
            return True

        elif "chrome" in command:

            speak("Opening Chrome")
            os.system("start chrome")
            return True

        elif "youtube" in command:

            speak("Opening YouTube")
            os.system("start https://youtube.com")
            return True

        elif "whatsapp" in command:

            speak("Opening WhatsApp")
            os.system("start whatsapp:")
            return True

        elif "notepad" in command:

            speak("Opening Notepad")
            os.system("start notepad")
            return True

        # =================================================
        # EXTRA APPS
        # =================================================

        apps = {

            "vs code": r"C:\Users\VICTUS\AppData\Local\Programs\Microsoft VS Code\Code.exe",

            "vscode": r"C:\Users\VICTUS\AppData\Local\Programs\Microsoft VS Code\Code.exe",

            "edge": "start msedge",

            "calculator": "calc",

            "paint": "mspaint",

            "cmd": "start cmd",

            "terminal": "start wt",

            "task manager": "taskmgr",

            "control panel": "control",

            "spotify": "start spotify",

            "vlc": r"C:\Program Files\VideoLAN\VLC\vlc.exe",

            "telegram": "start telegram",

            "discord": "start discord",

            "word": "start winword",

            "excel": "start excel",

            "powerpoint": "start powerpnt",

            "steam": r"C:\Program Files (x86)\Steam\steam.exe"
        }

        for app_name in apps:

            if app_name in command:

                speak(f"Opening {app_name}")

                app_path = apps[app_name]

                if app_path.endswith(".exe"):

                    os.startfile(app_path)

                else:

                    os.system(app_path)

                return True

        return False

    except Exception as e:

        print("APP ERROR:", e)

        speak("Unable to open app")

        return True


# =====================================================
# EXECUTE COMMAND
# =====================================================

def execute_command(command):

    command = command.lower().strip()

    print("COMMAND:", command)

    # =====================================================
    # OPEN APPS FIRST
    # =====================================================

    if command.startswith("open"):

        app_opened = open_app(command)

        if app_opened:
            return True

    # =====================================================
    # WHATSAPP MESSAGE
    # =====================================================

    if "message" in command:

        try:

            contact_name = None

            for name in contacts.keys():

                if name in command:
                    contact_name = name
                    break

            if not contact_name:

                speak("Contact not found")
                return True

            number = contacts[contact_name]

            message = command

            remove_words = [
                "open whatsapp",
                "open whatsapp and",
                "send",
                "message",
                "to",
                "and",
                contact_name
            ]

            for word in remove_words:
                message = message.replace(word, "")

            message = message.strip()

            if message == "":
                message = "Hello"

            print("CONTACT:", contact_name)
            print("MESSAGE:", message)

            speak(f"Sending message to {contact_name}")

            encoded_message = urllib.parse.quote(message)

            whatsapp_url = (
                f"https://web.whatsapp.com/send"
                f"?phone={number}&text={encoded_message}"
            )

            webbrowser.open(whatsapp_url)

            time.sleep(12)

            pyautogui.press("enter")

            speak("Message sent")

            return True

        except Exception as e:

            print("WHATSAPP ERROR:", e)

            speak("Message failed")

            return True

    # =====================================================
    # WHATSAPP VOICE CALL
    # =====================================================

    elif "call" in command and "video" not in command:

        try:

            contact_name = None

            for name in contacts.keys():

                if name in command:
                    contact_name = name
                    break

            if not contact_name:

                speak("Contact not found")
                return True

            number = contacts[contact_name]

            speak(f"Calling {contact_name}")

            whatsapp_url = (
                f"https://web.whatsapp.com/send?phone={number}"
            )

            webbrowser.open(whatsapp_url)

            time.sleep(12)

            for i in range(8):
                pyautogui.press("tab")

            pyautogui.press("enter")

            return True

        except Exception as e:

            print("CALL ERROR:", e)

            speak("Call failed")

            return True

    # =====================================================
    # WHATSAPP VIDEO CALL
    # =====================================================

    elif "video call" in command:

        try:

            contact_name = None

            for name in contacts.keys():

                if name in command:
                    contact_name = name
                    break

            if not contact_name:

                speak("Contact not found")
                return True

            number = contacts[contact_name]

            speak(f"Starting video call with {contact_name}")

            whatsapp_url = (
                f"https://web.whatsapp.com/send?phone={number}"
            )

            webbrowser.open(whatsapp_url)

            time.sleep(12)

            for i in range(7):
                pyautogui.press("tab")

            pyautogui.press("enter")

            return True

        except Exception as e:

            print("VIDEO CALL ERROR:", e)

            speak("Video call failed")

            return True

    # =====================================================
    # OPEN MY PC
    # =====================================================

    elif "open my pc" in command or "open this pc" in command:

        speak("Opening This PC")

        os.startfile("C:\\")

        return True

    # =====================================================
    # PLAY SONG
    # =====================================================

    elif "play" in command:

        song = command.replace("play", "")
        song = song.replace("music", "")
        song = song.strip()

        if song == "":
            song = "trending songs"

        speak(f"Playing {song}")

        pywhatkit.playonyt(song)

        return True

    # =====================================================
    # CHANGE SONG
    # =====================================================

    elif "change to" in command:

        song = command.replace("change to", "")
        song = song.strip()

        if song == "":
            speak("Song name missing")
            return True

        speak(f"Changing song to {song}")

        pywhatkit.playonyt(song)

        return True

    # =====================================================
    # STOP MUSIC
    # =====================================================

    elif "stop music" in command:

        speak("Stopping music")

        os.system("taskkill /f /im chrome.exe")
        os.system("taskkill /f /im brave.exe")

        return True

    # =====================================================
    # PAUSE MUSIC
    # =====================================================

    elif "pause music" in command:

        speak("Pausing music")

        pyautogui.press("k")

        return True

    # =====================================================
    # RESUME MUSIC
    # =====================================================

    elif "resume music" in command:

        speak("Resuming music")

        pyautogui.press("k")

        return True

    # =====================================================
    # NEXT SONG
    # =====================================================

    elif "next song" in command:

        speak("Next song")

        pyautogui.hotkey("shift", "n")

        return True

    # =====================================================
    # PREVIOUS SONG
    # =====================================================

    elif "previous song" in command:

        speak("Previous song")

        pyautogui.hotkey("shift", "p")

        return True

    # =====================================================
    # SLEEP MODE
    # =====================================================

    elif (
        "sleep mode" in command
        or "sleep my pc" in command
        or "sleep pc" in command
    ):

        speak("Putting PC to sleep")

        os.system(
            "rundll32.exe powrprof.dll,SetSuspendState 0,1,0"
        )

        return True

    # =====================================================
    # SHUTDOWN
    # =====================================================

    elif "shutdown my pc" in command:

        speak("Shutting down PC")

        os.system("shutdown /s /t 5")

        return True

    # =====================================================
    # RESTART
    # =====================================================

    elif "restart my pc" in command:

        speak("Restarting PC")

        os.system("shutdown /r /t 5")

        return True

    # =====================================================
    # UNKNOWN
    # =====================================================

    return False