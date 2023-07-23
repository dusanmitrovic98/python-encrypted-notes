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
    with open("notes.txt", "wb") as file:
        file.write(encrypted_data)

def display_notes():
    notes = load_notes()
    if notes:
        print("Your encrypted notes:")
        for i, note in enumerate(notes.splitlines(), 1):
            print(f"{i}. {note}")
    else:
        print("No notes found.")

def add_note():
    notes = load_notes()
    new_note = input("Enter your note: ")
    notes += new_note + "\n"
    save_notes(notes)
    print("Note added successfully!")

def remove_note():
    notes = load_notes()
    if not notes:
        print("No notes found.")
        return

    display_notes()
    try:
