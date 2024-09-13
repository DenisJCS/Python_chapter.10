import json
from pathlib import Path

def get_stored_username(path):
    """Retrieve the stored username if it exists."""
    if path.exists():
        contents = path.read_text()
        return json.loads(contents)
    return None

        
def save_username(path, username, age):
    """Saves entered name and age in json file"""
    data = {
        'username':username,
        'age':age
    }
    contents = json.dumps(data)
    path.write_text(contents)

def get_new_username(path):
    """Prompt for new username and save it"""
    username = input("What is your name ? ")
    age = input("How old are you? ")
    save_username(path, username, age)
    return username, age

def greet_user():
    """Greets user by name"""
    path = Path("remember_user.json")
    stored_usernames = get_stored_username(path)
    if stored_usernames:
        correct = input(f"Are you {stored_usernames['username']} age{stored_usernames['age']}? " + "yes/no ").lower()
        if correct == 'yes':
            print(f"Welcome back, {stored_usernames['username']}")
        else:
            entered_username =get_new_username(path)
            print(f"We will remember you when you come back, {entered_username}")
    else:
        entered_username = get_new_username(path)
        print(f"We will remember you when you come back, {entered_username}")

greet_user()






    

