from WebN import start
import logging

try:
    start()
    logging.basicConfig(level=logging.DEBUG)
except Exception as e:
    print('Error When loading application! Try again later!')
    print(f'Error info: {e}')
    exit(0)
