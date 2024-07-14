import os
from WebN.Config import get_env_key as WebN
from WebN.Ui.webui import *


def start():
    # global top_headlines
    print('[Info][WebN][App launching . . .]')
    print(f"Welcome to {WebN('APP_NAME')}")
    StartUI()
    # customtkinter.set_appearance_mode("dark")
    # application = App()
    # application.mainloop()
