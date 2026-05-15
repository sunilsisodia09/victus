from voice.listen import listen
from voice.speak import speak

from brain.commands import execute_command
from brain.ai import ask_ai

speak("Victus Activated")

while True:

    command = listen()

    if command == "":
        continue

    handled = execute_command(command)

    if not handled:

        answer = ask_ai(command)

        speak(answer)

    if "stop" in command:
        speak("Goodbye")
        break