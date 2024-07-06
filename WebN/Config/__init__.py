import os

import WebN.Utils
from WebN.Utils import *

from dotenv import load_dotenv

dotenv_loaded = False
dotenv_path = f'{ROOT_DIR}/.env'


def load_dotenv_file(path):
    global dotenv_loaded
    if os.path.exists(path):
        load_dotenv(dotenv_path)
        dotenv_loaded = True
        print('[Info][Environment][.env Ready!]')
    else:
        print(f'[Error][File Error][Environment][File .env not found in path {path}]')
        dotenv_loaded = False


def get_env_key(environment_key):
    global dotenv_loaded
    if dotenv_loaded:
        try:
            ret_val = os.getenv(environment_key)
            print(f'Returning environment value by key {environment_key}')
            print(f'The variable was transferred successfully.')
            return ret_val
        except EnvironmentError as e:
            print('[Error][Environment][Environment is not loaded! Cannot return a value!]')
            return None
    else:
        print('[Error][Environment][Environment is not loaded! Cannot return a value!]')
        return None


load_dotenv_file(dotenv_path)
