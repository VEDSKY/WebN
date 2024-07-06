import os
from dotenv import load_dotenv


class Config:
    def __init__(self, environment_key):
        self.environment_key = environment_key
        self.dotenv_path = os.path.join('.env')
        self.dotenv_loaded = False
        self._initialize()

    def _initialize(self):
        self._load_environment()
        self._get_env_key()

    def _load_environment(self):
        try:
            load_dotenv(self.dotenv_path)
            self.dotenv_loaded = True
            print('[Info][Environment][Environment loaded successfully!]')
        except EnvironmentError as e:
            print(f'[Error][Environment][{e}]')
            self.dotenv_loaded = False
        pass

    def _get_env_key(self):
        if self.dotenv_loaded:
            ret_val = os.getenv(self.environment_key)
            print(f'Returning environment value by key {self.environment_key}')
            print(f'Returned: {ret_val}')
            return ret_val
        else:
            print('[Error][Environment][Environment is not loaded! Cannot return a value!]')
            return None
