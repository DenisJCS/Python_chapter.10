from pathlib import Path 

path = Path("guest_book.txt")

print("Please enter the guest name .")
print("Type 'q' when you are finished .")

while True:
    name = input("Enter your name: ")
    if name == 'q':
        break
    else:
        print(f"Hello, {name}. Welcome !")
    with path.open(mode='a') as file:
            file.write(f"{name}\n")

