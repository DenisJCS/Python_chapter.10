with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents.rstrip())

from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()
contents = contents.rstrip()
print(contents)
