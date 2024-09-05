from pathlib import Path

def count_words(filename):
    """Count the approximate number of words in a file"""
    try:

        contents = filename.read_text(encoding = 'utf-8')

    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
    #Count the approximate numberr of the words in the file:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")
filenames = ['alice.txt', 'siddhart.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    path = Path(filename)
    count_words(path)


