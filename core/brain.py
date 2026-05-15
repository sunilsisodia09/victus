import requests
from config import AI_MODEL

def ask_ai(prompt):

    try:

        response = requests.post(
            "http://127.0.0.1:11434/api/generate",
            json={
                "model": AI_MODEL,
                "prompt": prompt,
                "stream": False
            }
        )

        data = response.json()

        return data["response"]

    except Exception as e:

        return "AI connection error"