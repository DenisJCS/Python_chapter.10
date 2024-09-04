#this is exception block that allow run program even if Python thinks it as error
try:
    print(5/0)
except: ZeroDivisionError
print("You can't divide by zero")

#Calculator does only division

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("\nSecond number: ")
    if second_number == 'q':
        break
    answer = int(first_number) / int(second_number)
    print(answer)
    
