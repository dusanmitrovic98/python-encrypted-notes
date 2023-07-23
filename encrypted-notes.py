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
        note_num = int(input("Enter the number of the note to remove: "))
        lines = notes.splitlines()
        if 1 <= note_num <= len(lines):
            del lines[note_num - 1]
            updated_notes = "\n".join(lines)
            save_notes(updated_notes)
            print("Note removed successfully!")
        else:
            print("Invalid note number.")
    except ValueError:
        print("Invalid input. Please enter a valid note number.")

def clear_notes():
    if os.path.exists("notes.txt"):
        os.remove("notes.txt")
    print("All notes have been cleared.")

if __name__ == "__main__":
    load_key()

    while True:
        print("\nCommand-line Note-Taking Application")
        print("1. Display Notes")
        print("2. Add Note")
        print("3. Remove Note")
        print("4. Clear Notes")
        print("5. Exit")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == "1":
            display_notes()
