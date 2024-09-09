from pathlib import Path
import json

username = input("What is your name? ")

path = Path('username.json')
contents = json.dumps(username)
path.write_text(contents)

print(f"We'll remember you when come back, {username}")


# Program below is combined storing and loading JSON and checks if user already stored any data and if it is , program open it up
from pathlib import Path
import json

path = Path('username.json')

if path.exists():
    contents = path.read_text()
    username = json.loads(contents)
    print(f"Welcome back, {username}")
else:
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    print(f"We will remember you when you come back, {username}")


