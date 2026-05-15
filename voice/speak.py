
import asyncio
import edge_tts
import pygame
import os
import uuid

VOICE = "en-US-GuyNeural"

pygame.mixer.init()


async def generate_voice(text, filename):

    communicate = edge_tts.Communicate(text, VOICE)

    await communicate.save(filename)


def speak(text):

    filename = f"voice_{uuid.uuid4()}.mp3"

    try:

        print("Victus:", text)

        # Generate voice
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        loop.run_until_complete(generate_voice(text, filename))

        # Stop previous audio if running
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()

        # Load voice
        pygame.mixer.music.load(filename)

        # Play voice
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        # Cleanup
        pygame.mixer.music.unload()

    except Exception as e:

        print("Speak Error:", e)

    finally:

        try:
            if os.path.exists(filename):
                os.remove(filename)
        except:
            pass

