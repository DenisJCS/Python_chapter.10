from pathlib import Path
import json

def get_stored_username(path, entered_username):
    """Check if the entered username exists in the stored data."""
    if path.exists():
        contents = path.read_text()
        stored_username = json.loads(contents)
        if stored_username == entered_username:
            return stored_username
    return None

def save_username(path, username):
    """Save the new username to the file."""
    contents = json.dumps(username)
    path.write_text(contents)

def greet_user():
    """Greet the user by name."""
    path = Path('username.json')
    entered_username = input("What is your name? ")

    stored_username = get_stored_username(path, entered_username)
    if stored_username:
        print(f"Welcome back, {stored_username}!")
    else:
        print(f"We don't know you yet, {entered_username}.")
        save_username(path, entered_username)
        print(f"We will remember you when you come back, {entered_username}!")

greet_user()

