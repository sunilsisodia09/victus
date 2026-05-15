import os

def open_app(command):

    command = command.lower()

    if "brave" in command:
        os.system("start brave")

    elif "chrome" in command:
        os.system("start chrome")

    elif "youtube" in command:
        os.system("start https://youtube.com")

    elif "whatsapp" in command:
        os.system("start whatsapp:")

    elif "notepad" in command:
        os.system("start notepad")

    else:
        return False

    return True