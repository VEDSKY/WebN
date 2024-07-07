import os
from WebN.Config import get_env_key as WebN
from WebN.Sources import *
from WebN.Ui.FletUi import set_up_screen


def start():
    print('[Info][WebN][App launching . . .]')
    print(f"Welcome to {WebN('APP_NAME')}")
    news = google_get_top_headlines()
    for article in news:
        print(f"{article['author']}\n"
              f"{article['title']}\n"
              f"{article['description']}\n"
              f"{article['url']}\n"
              f"{article['urlToImage']}\n"
              f"{article['publishedAt']}\n"
              f"{article['content']}\n")
    set_up_screen(news)
