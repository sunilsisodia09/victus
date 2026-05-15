import speech_recognition as sr

recognizer = sr.Recognizer()


def listen():

    with sr.Microphone() as source:

        print("Listening...")

        recognizer.adjust_for_ambient_noise(source, duration=1)

        audio = recognizer.listen(source)

    try:

        text = recognizer.recognize_google(
            audio,
            language="en-IN"
        )

        print("You:", text)

        return text.lower()

    except sr.UnknownValueError:

        return ""

    except Exception as e:

        print(e)

        return ""