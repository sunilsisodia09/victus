import json

MEMORY_FILE = "data/memory.json"


def load_memory():

    try:

        with open(MEMORY_FILE, "r") as file:

            return json.load(file)

    except:

        return {}



def save_memory(key, value):

    data = load_memory()

    data[key] = value

    with open(MEMORY_FILE, "w") as file:

        json.dump(data, file)