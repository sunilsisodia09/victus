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
# CURRENT SONG
# =====================================================

current_song = ""


# =====================================================
# EXECUTE COMMAND
# =====================================================

def execute_command(command):

    global current_song

    command = command.lower()

    # =====================================================
    # SEND WHATSAPP MESSAGE
    # =====================================================

    if "message" in command:

        try:

            contact_name = None

            # FIND CONTACT
            for name in contacts:

                if name in command:
                    contact_name = name
                    break

            if not contact_name:

                speak("Contact not found")
                return True

            number = contacts[contact_name]

            # REMOVE EXTRA WORDS
            message = command

            message = message.replace("open whatsapp", "")
            message = message.replace("and", "")
            message = message.replace("send", "")
            message = message.replace("message", "")
            message = message.replace("to", "")
            message = message.replace(contact_name, "")
            message = message.strip()

            if message == "":
                message = "Hello"

            speak(f"Opening chat with {contact_name}")

            encoded_message = urllib.parse.quote(message)

            whatsapp_url = (
                f"https://web.whatsapp.com/send?phone={number}"
                f"&text={encoded_message}"
            )

            webbrowser.open(whatsapp_url)

            # WAIT FOR WHATSAPP LOAD
            time.sleep(10)

            # PRESS ENTER TO SEND MESSAGE
            pyautogui.press("enter")

            speak("Message sent")

            return True

        except Exception as e:

            print("WhatsApp Error:", e)

            speak("Message failed")

            return True

    # =====================================================
    # OPEN WHATSAPP
    # =====================================================

    elif "open whatsapp" in command:

        speak("Opening WhatsApp")

        webbrowser.open("https://web.whatsapp.com")

        return True

    # =====================================================
    # OPEN YOUTUBE
    # =====================================================

    elif "open youtube" in command:

        speak("Opening YouTube")

        webbrowser.open("https://youtube.com")

        return True

    # =====================================================
    # OPEN CHROME
    # =====================================================

    elif "open chrome" in command:

        speak("Opening Chrome")

        chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"

        url = "https://google.com"

        os.system(f'start "" "{chrome_path}" {url}')

        return True

    # =====================================================
    # OPEN BRAVE
    # =====================================================

    elif "open brave" in command:

        speak("Opening Brave")

        os.system("start brave")

        return True

    # =====================================================
    # OPEN VS CODE
    # =====================================================

    elif "open vs code" in command or "open vscode" in command:

        speak("Opening VS Code")

        os.system("code .")

        return True

    # =====================================================
    # OPEN NOTEPAD
    # =====================================================

    elif "open notepad" in command:

        speak("Opening Notepad")

        os.system("start notepad")

        return True

    # =====================================================
    # OPEN MY PC
    # =====================================================

    elif "open my pc" in command:

        speak("Opening This PC")

        os.startfile("C:\\")

        return True

    # =====================================================
    # PLAY MUSIC
    # =====================================================

    elif "play" in command:

        speak("Playing music")

        song = command

        song = song.replace("play music", "")
        song = song.replace("play", "")
        song = song.replace("on youtube", "")
        song = song.replace("in brave", "")
        song = song.strip()

        if song == "":
            song = "trending songs"

        current_song = song

        pywhatkit.playonyt(song)

        return True

    # =====================================================
    # CHANGE SONG
    # =====================================================

    elif "change song" in command:

        new_song = command.replace("change song", "")
        new_song = new_song.replace("to", "")
        new_song = new_song.strip()

        if new_song == "":

            speak("Tell me the song name")
            return True

        current_song = new_song

        speak(f"Changing song to {new_song}")

        pywhatkit.playonyt(new_song)

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
    # PAUSE MUSIC
    # =====================================================

    elif "pause music" in command or "pause song" in command:

        speak("Pausing music")

        pyautogui.press("k")

        return True

    # =====================================================
    # RESUME MUSIC
    # =====================================================

    elif "resume music" in command or "resume song" in command:

        speak("Resuming music")

        pyautogui.press("k")

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
    # SLEEP MODE
    # =====================================================

    elif "sleep mode on" in command or "sleep my pc" in command:

        speak("Putting PC to sleep")

        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

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
    # NO COMMAND FOUND
    # =====================================================

    return False