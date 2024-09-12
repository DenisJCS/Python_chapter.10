from pathlib import Path
import json

def get_stored_data(path):
    """Check stored data"""
    if path.exists():
        contents = path.read_text()
        user_input = json.loads(contents)
        return user_input
    else:
        return None

def favorite_number(path):
    """Recieves input of user"""
    user_input = input("What is your favorite number ? ")
    contents = json.dumps(user_input)
    path.write_text(contents)
    return user_input 


def show_data():
    """Greets user and show his number"""
    path = Path("favorite_number.json")
    user_input = get_stored_data(path)
    if user_input:
        print(f" Your favorite number is {user_input}.")
    else:
        user_input = favorite_number(path)
        print(f"I know your favorite number! It is {user_input}.")

show_data()

