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

#Imporvixed improvement
from pathlib import Path

path = Path("python_sum.txt")
contents = path.read_text()
new_contents = path.read_text().replace('Python', 'C')
contents = new_contents


lines = contents.splitlines()
for line in lines:
    print(line)

#Short version
from pathlib import Path

path = Path("python_sum.txt")
new_contents = path.read_text().replace("Python", "Java")

lines = new_contents.splitlines()
for line in lines:
    print(line)
