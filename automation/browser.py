import webbrowser


def open_google():

    webbrowser.open("https://google.com")



def open_youtube():

    webbrowser.open("https://youtube.com")



def open_chatgpt():

    webbrowser.open("https://chatgpt.com")



def open_website(site):

    url = f"https://{site}.com"

    webbrowser.open(url)



def search_google(query):

    url = f"https://www.google.com/search?q={query}"

    webbrowser.open(url)