WAKE_WORDS = [

    "victus",
    "vector",
    "high vector",
    "hibiscus"
]


def detect_wake_word(text):

    text = text.lower()

    for word in WAKE_WORDS:

        if word in text:

            clean_text = text.replace(word, "").strip()

            return True, clean_text

    return False, text