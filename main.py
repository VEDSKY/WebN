from WebN.Config import get_env_key as WebN

try:
    print(f"Welcome to {WebN('APP_NAME')}")
except Exception as e:
    print(f'[Error][WebN][Error launching application! Error: {e}]')
