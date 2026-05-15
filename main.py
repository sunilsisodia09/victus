from voice.listen import listen
from voice.speak import speak
from voice.wake import detect_wake_word

from brain.commands import execute_command
from brain.ai import ask_ai


# Start Victus
speak("Victus Activated")

# Startup conversation
speak("Hello Sunil")
speak("I am Victus, how can I help you?")


while True:

    try:

        print("Listening...")

        command = listen()

        # Empty input fix
        if not command or command.strip() == "":
            continue

        command = command.lower()
        print("You:", command)

        # EXIT condition
        if "stop" in command or "exit" in command or "good night" in command:
            speak("Goodbye Sunil")
            break

        # Wake word detection
        wake_detected, clean_command = detect_wake_word(command)

        if wake_detected and clean_command.strip() == "":
            speak("Yes Sir")
            continue

        if wake_detected:
            command = clean_command.lower()

        # Human-like instant replies
        if "hello" in command or "hey" in command:
            speak("Hello Sunil, kaise ho?")
            continue

        elif "kaise ho" in command:
            speak("Main bilkul badhiya hoon, tum batao?")
            continue

        elif "kya kar rahe ho" in command:
            speak("Main tumse baat kar raha hoon 😄")
            continue

        elif "thank you" in command:
            speak("Welcome Sunil")
            continue

        elif "who are you" in command or "tum kaun ho" in command:
            speak("Main Victus hoon, tumhara AI assistant.")
            continue

        # System commands (PC control etc.)
        handled = execute_command(command)

        if handled:
            continue

        # AI fallback (real conversation)
        answer = ask_ai(command)

        print("Victus:", answer)
        speak(answer)

    except Exception as e:
        print("Main Loop Error:", e)