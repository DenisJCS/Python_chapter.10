#Read file at once
from pathlib import Path

path = Path("python_sum.txt")
contents = path.read_text()
print(contents.rstrip())

#Reading txt line by line 

from pathlib import Path

path = Path("python_sum.txt")
contents = path.read_text()

lines = contents.splitlines()
for line in lines:
    print(line)

