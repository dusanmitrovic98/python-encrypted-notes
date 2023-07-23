import os
from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def load_key():
    if not os.path.exists("secret.key"):
        key = generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)
