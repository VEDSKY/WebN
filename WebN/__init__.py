import os
from WebN.Config import get_env_key as WebN


def start():
    print('[Info][WebN][App launched successfully]')
    print(f"Welcome to {WebN('APP_NAME')}")
