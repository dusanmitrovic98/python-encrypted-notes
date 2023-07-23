import os
from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def load_key():
    if not os.path.exists("secret.key"):
        key = generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)
    else:
        with open("secret.key", "rb") as key_file:
            key = key_file.read()
    return key

def load_notes():
    try:
        with open("notes.txt", "rb") as file:
            encrypted_data = file.read()
            key = load_key()
            fernet = Fernet(key)
            decrypted_data = fernet.decrypt(encrypted_data)
            return decrypted_data.decode()
    except FileNotFoundError:
        return ""

def save_notes(notes):
    key = load_key()
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(notes.encode())
