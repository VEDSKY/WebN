from WebN import start

try:
    start()
except Exception as e:
    print('Error When loading application! Try again later!')
    print(f'Error info: {e}')
    exit(0)
