from pathlib import Path

path = Path("moby_dick.txt")
contents = path.read_text()

print(contents.lower().count('time '))


