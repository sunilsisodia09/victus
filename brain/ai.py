import requests

def ask_ai(prompt):

    try:

        response = requests.post(

            "http://localhost:11434/api/generate",

            json={

                "model": "llama3",

                "prompt": prompt,

                "stream": False

            }

        )

        data = response.json()

        return data["response"]

    except Exception as e:

        return "AI connection error"