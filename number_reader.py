from pathlib import Path
import json

path = Path('numbers.json')
contents = path.read_text()
numbers = json.loads(contents) # json.loads() imports data from json

print(contents)

